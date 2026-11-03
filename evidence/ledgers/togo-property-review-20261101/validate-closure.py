"""Additive closure evidence only. Never import/run the initial evidence writer."""
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
WRITER = ROOT / "evidence/ledgers/togo-property-20261101"
BASE = "59c23acba2ad66dd2bb29ffc81ffbb9289769ef8"
ORIGINAL = "47c65b0646ba12ab7949ae08eaadbb45456e1d8f"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


repairs_path = WRITER / "reviewer-repairs.json"
repairs = json.loads(repairs_path.read_text())
initial = json.loads((OUT / "initial-review-freeze.json").read_text())
initial_checks = [{"path": p["path"], "sha256": sha((ROOT / p["path"]).read_bytes()), "unchanged": sha((ROOT / p["path"]).read_bytes()) == p["sha256"]} for p in initial["files"]]
assert all(p["unchanged"] for p in initial_checks)
assert sha((OUT / "initial-review-freeze.json").read_bytes()) == "84db394d6b4ea1a6701673694f3f6b72f17083feb4abf0ec4d81724fc10bc6f7"

original_guide = git("show", f"{ORIGINAL}:skills/togo/tg-property-tax.md")
reconstructed = original_guide
literal_receipts = []
for item in repairs["guide_literal_changes"]:
    assert sha(reconstructed) == item["before_sha256"]
    old, new = item["before"].encode(), item["after"].encode()
    assert reconstructed.count(old) == 1
    reconstructed = reconstructed.replace(old, new, 1)
    assert sha(reconstructed) == item["after_sha256"]
    literal_receipts.append({"before_sha256": item["before_sha256"], "after_sha256": item["after_sha256"], "one_exact_replacement": True})
guide = (ROOT / "skills/togo/tg-property-tax.md").read_bytes()
assert reconstructed == guide
assert sha(guide) == "d2ae6e75d798a027beada4f4308daceeadb5a811b92e5748af9a4ba8b2023bb9"
original_blocks = re.findall(rb"```oa-check\n.*?\n```", original_guide, re.S)
current_blocks = re.findall(rb"```oa-check\n.*?\n```", guide, re.S)
assert len(current_blocks) == 2 and current_blocks == original_blocks
original_cases = original_guide.split(b"## Two worked examples that recompute\n", 1)[1].split(b"## Ask the client first", 1)[0]
current_cases = guide.split(b"## Two worked examples that recompute\n", 1)[1].split(b"## Ask the client first", 1)[0]
assert original_cases == current_cases

old_rows = json.loads(git("show", f"{ORIGINAL}:evidence/ledgers/togo-property-20261101/tg-property-tax.json"))
rows = json.loads((WRITER / "tg-property-tax.json").read_text())
assert len(rows) == 40 and [r["id"] for r in rows] == [r["id"] for r in old_rows]
cgi = (ROOT.parent / "sources/cgi2025.txt").read_text()
lf = (ROOT.parent / "sources/lf2026-ocr.txt").read_text()
cache = ROOT.parent / "sources/property-20261101/independent-review"
cgi_scope = (cache / "cgi257-287-independent-extract.txt").read_text()
lpf85 = (cache / "lpf85-87-independent-extract.txt").read_text()
lpf100 = (cache / "lpf100-101-independent-extract.txt").read_text()
lpf374 = (cache / "lpf374-378-independent-extract.txt").read_text()
md = (WRITER / "tg-property-tax.md").read_text()
review_rows = []
for before, row in zip(old_rows, rows):
    changed = [k for k in set(before) | set(row) if before.get(k) != row.get(k)]
    allowed = {"original_language_quote", "additional_original_language_quotes"}
    if row["id"] in ("P13", "P36", "P40"):
        allowed.add("rule")
    assert set(changed) <= allowed
    quotes = [row["original_language_quote"], *row.get("additional_original_language_quotes", [])]
    if row["source_id"] == "lf2026":
        corpus = lf
        source_scope = "LF article2 p3" if row["id"] == "P05" else "LF article21 replacementCGI271 p20"
    elif row["act_article"].startswith("LPF"):
        n = int(re.search(r"\d+", row["act_article"])[0])
        corpus = lpf85 if n < 90 else lpf100 if n < 110 else lpf374
        source_scope = row["act_article"]
    else:
        corpus = cgi_scope
        source_scope = row["act_article"]
    matched = [norm(q) in norm(corpus) for q in quotes]
    assert all(matched), (row["id"], matched)
    human_rows = [line for line in md.splitlines() if line.startswith("|" + row["id"] + "|")]
    assert len(human_rows) == 1
    cells = human_rows[0].split("|")[1:-1]
    assert cells[1] == row["section"] and cells[2] == row["rule"]
    assert cells[4] == "; ".join(quotes)
    assert row["official_url"] in cells[3] and row["act_article"] in cells[3]
    review_rows.append({"id": row["id"], "source_scope": source_scope, "changed_fields": sorted(changed), "quotes": [{"quote": q, "normalized_exact_in_relevant_source_scope": ok} for q, ok in zip(quotes, matched)], "markdown_json_agree": True, "closure_verdict": "confirmed: decisive source anchor(s), full-rule source reading retained; condition/procedure corrections checked where applicable"})
(OUT / "closure-row-review.json").write_text(json.dumps(review_rows, indent=2, ensure_ascii=False) + "\n")

source_receipts = []
for source in json.loads((WRITER / "source-identities.json").read_text()):
    data = pathlib.Path(source["private_cache"]).read_bytes()
    assert sha(data) == source["sha256"] and len(data) == source["bytes"]
    source_receipts.append({"id": source["id"], "sha256": sha(data), "bytes": len(data), "unchanged": True})
old_receipt = json.loads((OUT / "mechanical-receipt.json").read_text())
preservation = []
for item in old_receipt["preservation"]["files"]:
    data = (ROOT / item["path"]).read_bytes()
    assert sha(data) == item["sha256"]
    assert data == git("show", f"{BASE}:{item['path']}")
    preservation.append({"path": item["path"], "sha256": sha(data), "matches_base_and_initial_review": True})
assert sum(p["path"].startswith("skills/") for p in preservation) == 8
assert sum(p["path"].startswith("docs/") for p in preservation) == 22
assert (ROOT / "skills/togo/README.md").read_bytes() == git("show", f"{ORIGINAL}:skills/togo/README.md")

spec = importlib.util.spec_from_file_location("closure_checks", ROOT / "scripts/skill_checks.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
checks = mod.run_all(str(ROOT / "skills/togo/tg-property-tax.md"))
assert len(checks) == 15 and not any(checks.values())
commands = []
for cmd in [["python3", "scripts/skill_checks.py", "skills/togo/tg-property-tax.md"], ["python3", "scripts/check-examples.py", "--require", "skills/togo/tg-property-tax.md"], ["python3", "scripts/validate-guides.py", "--no-index-check"]]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert p.returncode == 0
    commands.append({"command": cmd, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr})

candidate_files = ["skills/togo/tg-property-tax.md", "skills/togo/README.md", "evidence/ledgers/togo-property-20261101/tg-property-tax.json", "evidence/ledgers/togo-property-20261101/tg-property-tax.md", "evidence/ledgers/togo-property-20261101/reviewer-repairs.json", "evidence/ledgers/togo-property-20261101/source-identities.json"]
candidate_hashes = [{"path": path, "sha256": sha((ROOT / path).read_bytes()), "bytes": len((ROOT / path).read_bytes())} for path in candidate_files]
for record in repairs["ledger_changes"]:
    assert sha(git("show", f"{ORIGINAL}:{record['path']}")) == record["before_sha256"]
    assert sha((ROOT / record["path"]).read_bytes()) == record["after_sha256"]

status_changes = [
    {"path": "skills/togo/tg-property-tax.md", "before": "Independent source review is pending; no accountant attestation or comprehensive country coverage is claimed.", "after": "Independent source review completed on 2026-11-01 for this conditional working paper; no accountant attestation or comprehensive country coverage is claimed."},
    {"path": "skills/togo/README.md", "before": "Independent source review is pending for this addition.", "after": "Independent source review completed on 2026-11-01 for this conditional addition."},
    {"path": "evidence/ledgers/togo-property-20261101/tg-property-tax.md", "before": "Source review closure is pending.", "after": "Independent source review closed on 2026-11-01 for this conditional working paper."},
]
for change in status_changes:
    before = (ROOT / change["path"]).read_bytes()
    assert before.count(change["before"].encode()) == 1
    after = before.replace(change["before"].encode(), change["after"].encode(), 1)
    change.update({"before_sha256": sha(before), "after_sha256": sha(after), "occurrences": 1})
(OUT / "status-only-allowance.json").write_text(json.dumps({"date": "2026-11-01", "basis": "focused conditional source-fidelity closure", "permission_scope": "Only these three exact factual status substitutions against the specified before hashes; preserve all other content and initial review/writer evidence. No attestation, complete-coverage, later-law continuity or merge permission.", "changes": status_changes}, indent=2, ensure_ascii=False) + "\n")

receipt = {"date": "2026-11-01", "result": "accepted for conditional read-source working-paper fidelity after corrections", "original_candidate_commit": ORIGINAL, "base": BASE, "head_at_closure": git("rev-parse", "HEAD").decode().strip(), "exact_candidate_files": candidate_hashes, "initial_review_files_unchanged": initial_checks, "guide_repair_literal_replay": literal_receipts, "guide_reconstructed_exactly": reconstructed == guide, "cases_prose_and_blocks_unchanged": True, "case_block_sha256": [sha(b) for b in current_blocks], "source_artifacts": source_receipts, "all_40_rows_checked": True, "anchor_count": sum(len(r["quotes"]) for r in review_rows), "all_anchors_exact_in_relevant_source_scope": True, "both_ledger_formats_agree": True, "old_guide_count": 8, "prior_evidence_count": 22, "preservation": preservation, "README_unchanged_from_frozen_addition": True, "shape_checks": checks, "commands": commands, "status_only_allowance_sha256": sha((OUT / "status-only-allowance.json").read_bytes()), "acceptance_limits": "Conditional statutory working paper against the read 2025 CGI/LPF and signed2026 LF overlay. All later-law/forms/workflow/specialcase/valuation/penalty/credit/claim-stay holds persist. No accountant attestation, full-country coverage or merge permission."}
(OUT / "closure-receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"accepted": True, "guide_sha256": sha(guide), "rows": len(rows), "anchors": receipt["anchor_count"], "initial_review_unchanged": True, "preservation": "8 Guides +22 prior evidence exact", "shape_checks": 15, "oa_check_blocks": len(current_blocks), "status_only_changes": status_changes}, indent=2, ensure_ascii=False))
