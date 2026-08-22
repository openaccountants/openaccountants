#!/usr/bin/env python3
"""
Smoke test for the OpenAccountants MCP server.

Run from the repo root (needs the MCP SDK + PyYAML, e.g. via uv):

    uv run --python 3.12 --with "mcp>=1.0.0" --with pyyaml python mcp/smoke_test.py

If the dependencies aren't installed the server can't be imported. The test
then runs a minimal filesystem check and still exits NON-ZERO, because "the
server does not import" is a failure, not a pass. Set OA_SMOKE_ALLOW_FALLBACK=1
to opt into the old lenient behaviour when you are deliberately running without
the SDK.

Exits 0 on success, 1 on failure.
"""

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

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
    # A server that cannot be imported is a broken server. Exiting 0 here let a
    # dependency upgrade that removes `mcp.server.fastmcp` (mcp 2.x does exactly
    # that) report ALL CHECKS PASSED while nothing worked.
    lenient = os.environ.get("OA_SMOKE_ALLOW_FALLBACK") == "1"
    if failures:
        print(f"FAILED -- {failures} check(s).")
    elif lenient:
        print("FILESYSTEM CHECKS PASSED (server not importable; fallback allowed).")
    else:
        print("FAILED -- server could not be imported; filesystem checks alone are not a pass.")
        print("         Install the SDK, or set OA_SMOKE_ALLOW_FALLBACK=1 to allow it.")
    sys.exit(0 if (not failures and lenient) else 1)


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
check("explicit tier 2 stays research-verified",
      gs["quality_tier"] == "research-verified", gs["quality_tier"])
check("tier 2 does not expose a reviewer as verified", gs["verified_by"] is None,
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

# --- submit_feedback ------------------------------------------------------
print("\nsubmit_feedback (general):")
fb = S.submit_feedback("Cyprus is missing from the catalogue.")
check("returns github_url", "github_url" in fb and fb["github_url"].startswith(
    "https://github.com/openaccountants/openaccountants/issues/new?"), fb.get("github_url"))
check("title auto-generated", fb["title"] == "Feedback", fb.get("title"))
check("labels = ['feedback']", fb["labels"] == ["feedback"], str(fb.get("labels")))
check("body includes the summary", "Cyprus is missing" in fb["body"])
check("body includes submitted-via footer", "submit_feedback" in fb["body"])

print("submit_feedback (skill-specific, rated):")
fb_skill = S.submit_feedback(
    summary="Rates look right but home-office deduction is outdated.",
    skill_slug="malta-income-tax",
    jurisdiction="mt",
    rating=4,
)
check("skill title auto", fb_skill["title"] == "Skill feedback: malta-income-tax (MT)",
      fb_skill.get("title"))
check("skill-feedback label added", "skill-feedback" in fb_skill["labels"],
      str(fb_skill["labels"]))
check("body mentions slug + jurisdiction + rating",
      "malta-income-tax" in fb_skill["body"]
      and "MT" in fb_skill["body"]
      and "4/5" in fb_skill["body"])
check("url contains url-encoded labels",
      "labels=feedback%2Cskill-feedback" in fb_skill["github_url"],
      fb_skill["github_url"])

print("submit_feedback validation:")
for label, fn in [
    ("empty summary rejected", lambda: S.submit_feedback("")),
    ("rating > 5 rejected", lambda: S.submit_feedback("ok", rating=6)),
    ("rating < 1 rejected", lambda: S.submit_feedback("ok", rating=0)),
]:
    try:
        fn()
        check(label, False, "did NOT raise")
    except Exception:
        check(label, True)

print("submit_feedback (long summary truncated):")
long_fb = S.submit_feedback("x" * 8000)
check("long body truncated under 6000 bytes",
      len(long_fb["body"].encode("utf-8")) <= 6500,  # 6000 + truncation note
      f"body bytes = {len(long_fb['body'].encode('utf-8'))}")
check("truncation note present", "truncated" in long_fb["body"].lower())

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
sfb = S.skill_feedback("malta-income-tax", "MT")
check("skill-feedback prompt embeds slug + jurisdiction",
      "malta-income-tax" in sfb and "MT" in sfb)
check("skill-feedback prompt points at submit_feedback tool",
      "submit_feedback" in sfb)


async def _registry() -> None:
    tools = {t.name for t in await S.mcp.list_tools()}
    check("6 tools registered",
          tools == {"list_skills", "get_skill", "get_skill_sections",
                    "search_skills", "start", "submit_feedback"},
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
