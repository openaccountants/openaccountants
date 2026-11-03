"""Read-only checks of frozen writer content; writes reviewer evidence in this folder only."""
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
BASE = "59c23acba2ad66dd2bb29ffc81ffbb9289769ef8"
CANDIDATE = "47c65b0646ba12ab7949ae08eaadbb45456e1d8f"
WRITER = ROOT / "evidence/ledgers/togo-property-20261101"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def blob(commit, path):
    return git("show", f"{commit}:{path}")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


comments = [
    "257 creates annual built/unbuilt property tax. Separate annual ownership job from rental income/transfer jobs; no combined rate asserted.",
    "All nine points of 258 read, including mobile storage/operating tools exclusion, indispensable land, commercial land and >100-metre advertising land. Guide is an inclusive scope summary, not a replacement of the full enumeration.",
    "259 requires urban agglomeration plus approved subdivision, or outside land intended for nonagricultural construction. Do not infer taxable urban status from vacancy.",
    "260(1) lists four rights-holder groups. 260(2) has specific no-indemnity reversion construction lease, tenant amortisation value/next-year entry subject to 262, owner's rent/prestations and solidarity. Specific computation explicitly held.",
    "LF article 2 p3: subject to contrary provisions, other fiscal provisions apply from 1 January 2026. Independently rendered/read original page. Ledger quote is only title/opening, not commencement evidence.",
    "275: 7.5% of net cadastral income. Quote omits the decisive rate, though independently read clause confirms it.",
    "270: 1 January cadastral rental value less 50%, enumerated ownership costs; indispensable construction land included where relevant. Quote omits the percentage.",
    "276: 0.5% of market value. Original quote ends before the rate; underlying figure verified.",
    "272: unbuilt market value at 1 January of assessment year. Source clause supports date, quotation opening does not fully reproduce it.",
    "273: recent transfers of subject/comparable neighbouring land, then direct estimate if none/usefully recent. Source supports evidence hierarchy.",
    "274 assigns market-value determination to cadastre. Original quote includes following heading; harmless locator spillover.",
    "262: regularly declared construction/reconstruction/additions, two years commercial/industrial/professional, five residential, starting following completion year. Separate financial/public-economic-enterprise mortgage/dation acquisition recovery branch read.",
    "All eleven 261 branches read. Ledger's full-rule summary is grounded, but Guide must state omitted qualifying conditions explicitly; see correction 1 in review record.",
    "All six 268 branches read: nonproductive specified public land, selection nurseries of listed creators, school land, built-taxable land, actual 1 January qualifying cultivation, state railway ways. Guide is a bounded screen referring to exact provision.",
    "269 exempts rural immovables. Vacancy alone proves neither rural status nor scope exclusion. Quote fully contains this short rule plus a neighbouring heading.",
    "263 rural conversion into rental housing or factory gets five years beginning year after conversion works finish. Not a general five-year commercial construction exemption.",
    "264 denies temporary exemption to commercial/industrial and 258 advertising land; taxable from following assignment year. No ordinary new-building exemption for those plots.",
    "265 irregular subdivision accesses only still-running exemption period, from year regular authorisation is obtained. No new full window begins then.",
    "LPF100: payment proof plus assessment bulletins; 8.75% withheld allocated 3.75% property and 5% income. LPF101 has separate no-withholding advance. Guide correctly holds full calculation, does not deduct whole withholding or infer refund.",
    "LPF85: whole-year 1 January tax, spontaneous receiver payment, two equal payments by 31 May and 31 October, landowner/tenant solidarity. Opening quote alone omits instalment dates.",
    "LPF86: declaration by 31 May from owners/principal tenants or their managers; tenant names/premises/rent/charges, free occupants, own/vacant premises and taxable unbuilt area. Full five-item list read.",
    "LPF87: new/rebuilt/added construction and size/use changes within four months definitive realisation; no declaration gives assessment from 1 January after presumed completion. Not a universal late-payment fine.",
    "266: permit alternative or works-opening declaration within four months; nature/use/area/title or cadastre identification, plan/sketch; also completion declaration within four months; written authority-issued form. No current form identifier inferred.",
    "267: late construction/end declarations permit unexpired fraction only from 1 January following production; first post-completion year never exempt because of lateness.",
    "281: territorial tax service of prefecture/commune where property lies. Not owner's residence.",
    "282: cadastral mutation at owners' diligence; cadastral/titled locations need prior entry/transcription as text states. 284 adds specific titled-parcel assessment-name transcription rule, correctly distinguished.",
    "283: pending mutation, former owner/natural heirs remain assessed and can be compelled to pay; recourse against new owner preserved.",
    "284: correction for actual 1 January ownership, title transcription condition, civil ownership dispute postpones assessment-name decision until final judgment. Not all tax collection suspended.",
    "285: correction decisions affect relevant and subsequent years until necessary assessment-bulletin corrections.",
    "266 last paragraphs: assessment from year following completion; first-bulletin addition counts years elapsed to discovery including discovery year; maximum addition five times current annual contribution. Guide holds actual calculation for dates/notice.",
    "278 full paragraphs: commercial/industrial vacancy/non-use; involuntary, >=3 months, all or separately rentable/exploitable part; following-month start through end of cessation month; LPF374+ claim.",
    "279 full clause: total/partial destruction or voluntary demolition during year; claim; following month after destruction or opening demolition works. Guide's compressed next-month rule correctly read with this source.",
    "280 full clause: extraordinary disappearance of unbuilt immovable; following month, on claim under374+. Not ordinary development or vacant land relief.",
    "LPF374 entire a-g read. Normal deadline 31 December following relevant event year; (g) selects year vacancy minimum duration is reached. Guide appropriately says select actual event.",
    "LPF375 grants taxpayer claim period equal to administration's period where recovery/reassessment procedure; Guide does not assume universal ordinary deadline.",
    "LPF376 all six numbered points plus regularisation/stamp-duty paragraphs read. Ledger includes French/individual concept but Guide omits admissibility details and audit notices; correction2 required.",
    "LPF377 full mandate timing plus exceptions read: bar lawyers, status/function representatives, personally demanded signatories, public/ministry officers for taxes they must pay. Guide explicitly gates on exception; no unsupported automatic mandate waiver.",
    "LPF378 foreign-domiciled claimant must elect Togo domicile. Original short quote contains complete rule.",
    "262 with265-267,270,275: 2023 completion gives 2024-25 commercial vs2024-28 residential;2026 taxed75000 vs0,3 residential exempt assessment years left including2026. Independently recomputed and flags timely declaration/regularisation/use assumptions.",
    "LF21 replacement271 p20 visually read in full. Lease/comparison/direct hierarchy retained; qualifying balance-sheet commercial/industrial premises/installations 6% market includingland/incorporated assets. 270/275/LPF85 give6m/3m/225000/112500. Prefer 'business' to 'company' in generic translation of entreprises.",
]
assert len(comments) == 40
ledger = json.loads((WRITER / "tg-property-tax.json").read_text())
cgi = (ROOT.parent / "sources/cgi2025.txt").read_text()
lf = (ROOT.parent / "sources/lf2026-ocr.txt").read_text()
row_review = []
for row, comment in zip(ledger, comments):
    q = norm(row["original_language_quote"])
    corpus = lf if row["source_id"] == "lf2026" else cgi
    exact = q in norm(corpus)
    quote_kind = "article-opening locator; strengthen to decisive figure/condition clause"
    if row["id"] in ("P11", "P15", "P38"):
        quote_kind = "short rule substantively present; inspect neighbour spillover if any"
    if row["id"] == "P40":
        quote_kind = "6% and land anchored; strengthen to include asset qualification"
    row_review.append({
        "id": row["id"], "act_article": row["act_article"],
        "source_rule_verdict": "confirmed against full clauses and neighbours within conditional scope",
        "guide_verdict": "correction required: condition/procedure completeness" if row["id"] in ("P13", "P36") else "substantive source fidelity confirmed within stated holds",
        "original_quote_normalized_exact_match": exact,
        "quote_evidence_verdict": quote_kind,
        "independent_findings": comment,
    })
(OUT / "ledger-row-review.json").write_text(json.dumps(row_review, indent=2, ensure_ascii=False) + "\n")
(OUT / "ledger-row-review.tsv").write_text("id\tsource_rule_verdict\tguide_verdict\tquote_exact_normalized\tquote_evidence_verdict\tindependent_findings\n" + "".join("\t".join([r["id"], r["source_rule_verdict"], r["guide_verdict"], str(r["original_quote_normalized_exact_match"]), r["quote_evidence_verdict"], r["independent_findings"]]) + "\n" for r in row_review))

spec = importlib.util.spec_from_file_location("property_review_checks", ROOT / "scripts/skill_checks.py")
checks_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks_module)
checks = checks_module.run_all(str(ROOT / "skills/togo/tg-property-tax.md"))

commands = [
    ["python3", "scripts/skill_checks.py", "skills/togo/tg-property-tax.md"],
    ["python3", "scripts/check-examples.py", "--require", "skills/togo/tg-property-tax.md"],
    ["python3", "scripts/validate-guides.py", "--no-index-check"],
]
execution = []
for command in commands:
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    execution.append({"command": command, "exit_code": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr})

paths = git("ls-tree", "-r", "--name-only", BASE, "skills/togo", "docs/research/2026-11-01-togo-pack", "docs/research/2026-11-01-togo-review").decode().splitlines()
preserved = []
for path in paths:
    if path == "skills/togo/README.md":
        continue
    expected = blob(BASE, path)
    frozen = blob(CANDIDATE, path)
    actual = (ROOT / path).read_bytes()
    preserved.append({"path": path, "sha256": sha(actual), "base_blob": git("rev-parse", f"{BASE}:{path}").decode().strip(), "frozen_equals_base": frozen == expected, "working_equals_base": actual == expected})

addition = json.loads((WRITER / "readme-addition.json").read_text())
readme_base = blob(BASE, "skills/togo/README.md")
readme = (ROOT / "skills/togo/README.md").read_bytes()
guide = (ROOT / "skills/togo/tg-property-tax.md").read_text()
fm = guide.split("---", 2)[1]
platform_keys = ["review_status", "license", "authored_by", "trust_label", "drafted_by", "approved_by", "validation_status", "validated", "verified_by", "reviewed_by", "reviewed_on"]
frozen_paths = json.loads((WRITER / "freeze-receipt.json").read_text())["files"]
frozen_checks = []
for entry in frozen_paths:
    actual = (ROOT / entry["path"]).read_bytes()
    committed = blob(CANDIDATE, entry["path"])
    frozen_checks.append({"path": entry["path"], "sha256": sha(actual), "matches_writer_frozen_sha256": sha(actual) == entry["sha256"], "matches_frozen_commit": actual == committed, "git_blob": git("rev-parse", f"{CANDIDATE}:{entry['path']}").decode().strip()})

sources = []
for source in json.loads((WRITER / "source-identities.json").read_text()):
    actual = pathlib.Path(source["private_cache"]).read_bytes()
    sources.append({"id": source["id"], "official_url": source["official_url"], "private_cache": source["private_cache"], "sha256": sha(actual), "bytes": len(actual), "matches_recorded_identity": sha(actual) == source["sha256"] and len(actual) == source["bytes"]})

receipt = {
    "review_date": "2026-11-01", "candidate_commit": CANDIDATE, "base_commit": BASE,
    "head_at_receipt": git("rev-parse", "HEAD").decode().strip(),
    "result": "corrections required; no status-only reconciliation authorised yet",
    "source_identities": sources,
    "frozen_content_checks": frozen_checks,
    "shape_checks": checks,
    "commands": execution,
    "earlier_full_validator_diagnostic": {
        "command": ["python3", "scripts/validate-guides.py", "--help"], "exit_code": 1,
        "stdout": "checked 9 guides (3 non-guide .md files skipped)\nchecked 0 generated package frontmatter block(s)\nWARN: 0 same-job groups, see skills/DUPLICATES.md\nERROR: index.json is stale (`counts` differs) — regenerate with: python3 scripts/build-index.py\nERROR: llms-full.txt is stale (its embedded docs or the guide inventory changed) — regenerate: python3 scripts/build-llms-full.py\n\nvalidation FAILED: 2 error(s), 1 warning group(s)\n",
        "interpretation": "--help is not handled; it runs validation. Generated files deliberately not changed in source-only review."
    },
    "preservation": {
        "old_guide_count": sum(r["path"].startswith("skills/") for r in preserved),
        "prior_evidence_count": sum(r["path"].startswith("docs/") for r in preserved),
        "files": preserved,
        "readme_is_exact_base_plus_recorded_addition": readme == readme_base + addition["append_exact"].encode(),
        "replaced_guide_body_units": 0,
    },
    "platform_written_keys_found": [k for k in platform_keys if re.search(rf"^{k}:", fm, re.M)],
    "cta_found": "openaccountants-cta-block" in guide or "## Talk to" in guide,
    "required_general_reference_notice_present": "**General reference only.**" in guide,
    "quote_normalized_exact_matches": sum(r["original_quote_normalized_exact_match"] for r in row_review),
    "independent_examples": [
        {"case": "commercial asset", "market_value": 100000000, "rental_value": 100000000 * 6 // 100, "net_cadastral_income": 3000000, "annual_tax": 225000, "each_instalment": 112500},
        {"case": "2023 completion assessment2026", "commercial_exempt_years": [2024, 2025], "residential_exempt_years": [2024, 2025, 2026, 2027, 2028], "ordinary_tax": 75000, "commercial_tax": 75000, "residential_tax": 0, "residential_exempt_years_left_including2026": 3},
    ],
}
(OUT / "mechanical-receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"shape_checks": len(checks), "shape_failures": sum(bool(v) for v in checks.values()), "command_exits": [r["exit_code"] for r in execution], "old_guides": receipt["preservation"]["old_guide_count"], "prior_evidence": receipt["preservation"]["prior_evidence_count"], "preservation_failures": sum(not r["frozen_equals_base"] or not r["working_equals_base"] for r in preserved), "readme_append_exact": receipt["preservation"]["readme_is_exact_base_plus_recorded_addition"], "frozen_failures": sum(not r["matches_writer_frozen_sha256"] or not r["matches_frozen_commit"] for r in frozen_checks), "source_identity_failures": sum(not r["matches_recorded_identity"] for r in sources), "quote_matches": receipt["quote_normalized_exact_matches"], "quote_unmatched_ids": [r["id"] for r in row_review if not r["original_quote_normalized_exact_match"]]}, indent=2))
