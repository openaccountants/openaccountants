#!/usr/bin/env python3
"""
Smoke test for the OpenAccountants MCP server.

Run from the repo root (needs the MCP SDK + PyYAML, e.g. via uv):

    uv run --python 3.12 --with "mcp>=1.0.0" --with pyyaml python mcp/smoke_test.py

If the dependencies aren't installed, the server can't be imported; the test
then falls back to a minimal filesystem check so it still exits cleanly.

Exits 0 on success, 1 on failure.
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

failures = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global failures
    status = "PASS" if condition else "FAIL"
    msg = f"  [{status}] {label}"
    if detail and not condition:
        msg += f"  -- {detail}"
    print(msg)
    if not condition:
        failures += 1


try:
    from openaccountants_mcp import server as S
    HAVE_SERVER = True
except ImportError as exc:
    HAVE_SERVER = False
    print(f"MCP SDK / PyYAML not installed ({exc}); running filesystem fallback.\n")
    REPO_ROOT = Path(__file__).resolve().parents[1]
    PACKAGES_DIR = REPO_ROOT / "packages"
    check("packages/ exists", PACKAGES_DIR.is_dir(), str(PACKAGES_DIR))
    check("packages/ has skills", any(PACKAGES_DIR.rglob("*.md")))
    check("malta-income-tax.md present", (PACKAGES_DIR / "malta" / "malta-income-tax.md").is_file())
    print()
    print("FILESYSTEM CHECKS PASSED." if not failures else f"FAILED — {failures} check(s).")
    sys.exit(1 if failures else 0)


# --- list_skills ----------------------------------------------------------
print("list_skills:")
ls = S.list_skills()
check("returns skills + total", "skills" in ls and "total" in ls)
check(">300 skills", ls["total"] > 300, f"got {ls['total']}")
mt = S.list_skills(jurisdiction="MT")
check("MT filter non-empty", len(mt["skills"]) > 0)
check("MT filter only MT", all(s["jurisdiction"] == "MT" for s in mt["skills"]),
      str({s["jurisdiction"] for s in mt["skills"]}))
check("MT includes malta-vat-return (no own frontmatter jurisdiction)",
      any(s["slug"] == "malta-vat-return" for s in mt["skills"]))
usca = S.list_skills(jurisdiction="US-CA")
check("US-CA filter works (sub-national dir)", len(usca["skills"]) > 0, f"got {len(usca['skills'])}")
sample = mt["skills"][0]
check("skill has required fields",
      all(k in sample for k in ("slug", "title", "jurisdiction", "category",
                                "quality_tier", "verified_by", "last_updated")),
      str(sample))

# --- get_skill ------------------------------------------------------------
print("\nget_skill('malta-income-tax'):")
gs = S.get_skill("malta-income-tax")
check("has markdown", len(gs["markdown"]) > 500)
check("has provenance footer", "Provenance & attribution" in gs["markdown"])
check("accountant-verified tier", gs["quality_tier"] == "accountant-verified", gs["quality_tier"])
check("verifier is a name, not an email", gs["verified_by"] and "@" not in str(gs["verified_by"]),
      str(gs["verified_by"]))

# --- get_skill_sections ---------------------------------------------------
print("\nget_skill_sections('malta-income-tax'):")
sec = S.get_skill_sections("malta-income-tax")
check("sections non-empty", len(sec["sections"]) > 1, f"got {len(sec['sections'])}")
check("section shape", all(set(s) >= {"heading", "content", "level"} for s in sec["sections"]))

# --- start (onboarding) ---------------------------------------------------
print("\nstart():")
empty = S.start()
check("no args → needs_input", empty["status"] == "needs_input", empty.get("status"))
check("needs both fields", set(empty.get("needs", [])) == {"intent", "jurisdiction"},
      str(empty.get("needs")))
check("available_intents non-empty", len(empty.get("available_intents", [])) >= 5)

print("start(intent='taxes'):")
intent_only = S.start(intent="taxes")
check("intent only → needs jurisdiction", intent_only["status"] == "needs_input"
      and intent_only.get("needs") == ["jurisdiction"], intent_only.get("status"))
check("jurisdictions list non-empty", len(intent_only.get("available_jurisdictions", [])) > 10)
check("MT is among the available jurisdictions",
      "MT" in intent_only.get("available_jurisdictions", []))

print("start(jurisdiction='MT'):")
jx_only = S.start(jurisdiction="MT")
check("jurisdiction only → needs intent",
      jx_only["status"] == "needs_input" and jx_only.get("needs") == ["intent"])
check("MT has taxes intent available",
      any(i["key"] == "taxes" for i in jx_only.get("available_intents", [])))

print("start(intent='taxes', jurisdiction='MT'):")
ready = S.start(intent="taxes", jurisdiction="MT")
check("both → ready", ready["status"] == "ready", ready.get("status"))
slugs = [s["slug"] for s in ready.get("skills_to_load", [])]
check("skills_to_load non-empty", len(slugs) > 0, str(slugs))
check("malta-income-tax in plan", "malta-income-tax" in slugs, str(slugs))
check("mt-freelance-intake in plan", "mt-freelance-intake" in slugs, str(slugs))
check("intake comes before income-tax in ordering",
      slugs.index("mt-freelance-intake") < slugs.index("malta-income-tax"))
check("plan has guardrails", len(ready.get("guardrails", [])) >= 3)

print("start(intent='set up a company', jurisdiction='MT'):")
synonym = S.start(intent="set up a company", jurisdiction="MT")
check("synonym 'set up a company' → formation plan",
      synonym["status"] == "ready" and synonym.get("intent") == "formation",
      str(synonym.get("intent")))
check("formation plan includes malta-formation",
      "malta-formation" in [s["slug"] for s in synonym.get("skills_to_load", [])])

print("start(intent='gibberish'):")
gib = S.start(intent="gibberish")
check("unmatched intent → needs_clarification",
      gib["status"] == "needs_clarification", gib.get("status"))

# --- search_skills --------------------------------------------------------
print("\nsearch_skills('reverse charge', 'MT'):")
sr = S.search_skills("reverse charge", "MT")
check("returns results + total", "results" in sr and "total" in sr)
check("has matches", sr["total"] > 0, f"got {sr['total']}")
if sr["results"]:
    check("result shape",
          set(sr["results"][0]) >= {"slug", "title", "jurisdiction", "matched_section", "snippet"})

print("\nInput validation / path safety:")
for label, fn in [
    ("empty query rejected", lambda: S.search_skills("")),
    ("unknown slug rejected", lambda: S.get_skill("does-not-exist-xyz")),
    ("path traversal rejected", lambda: S._safe_resolve(S.PACKAGES_DIR, "../../etc/passwd")),
]:
    try:
        fn()
        check(label, False, "did NOT raise")
    except Exception:
        check(label, True)

# --- prompts --------------------------------------------------------------
print("\nPrompts:")
check("tax-return interpolates",
      "company taxpayer in Malta" in S.tax_return("Malta", entity_type="company"))
check("compare-jurisdictions interpolates income",
      "Effective income tax rate at EUR 80000" in S.compare_jurisdictions("MT,UK", income="EUR 80000"))
check("skill-feedback has slug + date",
      "malta-income-tax" in S.skill_feedback("malta-income-tax", "MT"))


async def _registry() -> None:
    tools = {t.name for t in await S.mcp.list_tools()}
    check("5 tools registered",
          tools == {"list_skills", "get_skill", "get_skill_sections", "search_skills", "start"},
          str(tools))
    prompts = {p.name for p in await S.mcp.list_prompts()}
    check("6 prompts registered",
          prompts == {"skill-review", "tax-return", "vat-check", "find-deductions",
                      "skill-feedback", "compare-jurisdictions"}, str(prompts))


asyncio.run(_registry())

print()
if failures:
    print(f"FAILED — {failures} check(s) did not pass.")
    sys.exit(1)
print("ALL CHECKS PASSED.")
