"""Independent read-only content checks; writes only this review's evidence."""
import datetime
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PRIVATE = ROOT.parent / "sources/rental-review-20261101"
CONTENT = "a64f729d0ad3245df3ff3838d143b4263c0edc07"
PRIOR = "ea5f83bc4f60aad2b7f5fff85e921d27e0b360fa"
MAIN = "59c23acba2ad66dd2bb29ffc81ffbb9289769ef8"
WRITER = ROOT / "evidence/ledgers/togo-rental-20261101"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

def blob(commit, path):
    return git("show", f"{commit}:{path}")

def norm(text):
    return re.sub(r"\s+", " ", text).strip()

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

comments = [
    ("LPF100 opening, physical253/printed252", "Full opening specifies gross rents due to owners from letting immovables belonging to them. Guide preserves owner/property/gross-rent conditions."),
    ("LPF100 payer list, physical253-254/printed252-253", "Read all four classes across page break: collectivites publiques, organisations internationales, public/private legal persons, and natural persons exercising artisanal/commercial/noncommercial activity. Guide preserves every class; ordinary private tenant is outside the enumeration."),
    ("LPF100 solidarity physical253; economic burden physical254", "Joint payment liability is explicit, separately from legal tenant duty and owner's economic burden. Both are retained. No innocent-owner safe harbour asserted."),
    ("LPF100 rate paragraph, physical253/printed252", "8.75% applies to gross rents. Annual income/property assessment deductions do not reduce this stated gross collection base. The single collection is not duplicated."),
    ("LPF100 first allocation bullet, physical253/printed252", "3.75 percentage points of gross rent are allocated against property tax within the 8.75% collection. Read with full preceding rate/credit paragraph and second bullet; not 3.75% of withholding."),
    ("LPF100 second allocation bullet, physical253/printed252", "5 percentage points of gross rent allocated against income tax; sum 3.75+5=8.75. Final income assessment remains in sibling Guide."),
    ("LPF101 entire clause, physical254/printed253", "Recipients of property income not undergoing article100 withholding must pay declared provisional advances at8.75%, under article100 framework. Not final tax, exemption or automatic refund."),
    ("LPF100 complete credit sentence, physical253/printed252", "Actual acquittement proof plus issued assessment bulletins condition the deduction. Tenant cash deduction alone proves neither remittance nor credit. No final-liability/refund claim inferred."),
    ("LPF100 complete credit sentence, physical253/printed252", "Read after establishment of assessment bulletins for those taxes. Guide preserves both timing and separate tax allocations, with credit excess held."),
    ("LPF101 entire clause plus LPF100 list, physical253-254", "Article101 ordinary private-tenant branch follows non-withholding condition. It does not clear listed tenant noncompliance: Guide expressly retains separate default reconciliation and joint liability. No safe harbour invented."),
    ("LPF100 final sentence, physical254/printed253", "Exact deadline refers to month following period au titre de laquelle le loyer est paye. Guide follows rental period wording, keeps cash date separately and holds advances/arrears/straddling-period ambiguity."),
    ("LPF101 entire clause, physical254/printed253", "Same relative period deadline, on declaration. Full source does not name current form/boxes/portal/payment reference; Guide explicitly holds those operational steps."),
    ("LPF100-101 entire section3, physical253-254", "No numeric sanction/interest formula in these two clauses. Guide keeps joint liability and paid-proof condition and routes administration without inventing a penalty or declaring no penalties exist."),
    ("LPF100 legal payer list, physical253/printed252", "International organisations appear affirmatively in listed withholding tenants. No universal exemption; treaty/privilege/nonresident and currency questions remain held."),
    ("LPF100 full rule, physical253-254", "Ordinary corporate tenant is public/private legal-person class. Independently recomputed200000 gross,17500 withholding,182500 owner cash,7500 property and10000 income components. May single-period example gives15June. Credit conditions retained."),
    ("LPF100 list and101 full clause, physical253-254", "Business natural-person tenant belongs to list; ordinary private tenant outside listed classes pays full rent and owner declares advance. Independently recomputed17500 and182500 both branches, but responsible party differs. Listed tenant default excluded, final assessments retained."),
    ("LF2026 article21 physical14; art2 physical3; signature physical45", "Full amendment list read visually: LPF creations4bis/99bis/514bis; amendments16,22,23,49,50,62,64,97,205,210,238,367,461,544. No100/101. Art2 distinguishes IRPP2025, IS closed from31December2025, other fiscal provisions from1January2026 subject to contrary provision. Signed31December2025. Only bounded overlay finding; not complete later-law chain."),
]
ledger = json.loads((WRITER / "tg-rental-withholding.json").read_text())
assert len(ledger) == len(comments) == 17
cgi = (PRIVATE / "cgi-252-255.txt").read_text()
lf = (ROOT.parent / "sources/lf2026-14.txt").read_text()
reviews = []
for row, (locator, comment) in zip(ledger, comments):
    corpus = lf if row["source_id"] == "lf2026" else cgi
    reviews.append({
        "id": row["id"], "act_article": row["act_article"],
        "writer_quote": row["original_language_quote"],
        "quote_normalized_exact_match": norm(row["original_language_quote"]) in norm(corpus),
        "quote_verdict": "exact short anchor; corroborated against full actual clause and neighbours",
        "locator_checked": locator, "writer_physical_pages": row["physical_pages"],
        "source_rule_verdict": "confirmed within explicit conditional scope",
        "guide_verdict": "accepted for source fidelity; no correction required",
        "findings": comment,
    })
assert all(r["quote_normalized_exact_match"] for r in reviews)
write("ledger-row-review.json", reviews)
(OUT / "ledger-row-review.tsv").write_text("id\tquote_exact_normalized\tlocator\tverdict\tfindings\n" + "".join("\t".join([r["id"],str(r["quote_normalized_exact_match"]),r["locator_checked"],r["guide_verdict"],r["findings"]])+"\n" for r in reviews))

frozen = []
paths = git("diff", "--name-only", PRIOR, CONTENT).decode().splitlines()
for path in paths:
    candidate = blob(CONTENT, path)
    actual = (ROOT / path).read_bytes()
    frozen.append({"path":path,"git_blob":git("rev-parse",f"{CONTENT}:{path}").decode().strip(),"sha256":sha(candidate),"bytes":len(candidate),"working_equals_frozen":actual==candidate})
assert all(r["working_equals_frozen"] for r in frozen)
writer_freeze = json.loads((WRITER / "freeze-receipt.json").read_text())
assert all(sha(blob(CONTENT,r["path"])) == r["sha256"] for r in writer_freeze["files"])

prior_paths = git("ls-tree","-r","--name-only",PRIOR,"skills/togo","docs/research/2026-11-01-togo-pack","docs/research/2026-11-01-togo-review","evidence/ledgers/togo-property-20261101","evidence/ledgers/togo-property-review-20261101").decode().splitlines()
preserved=[]
for path in prior_paths:
    if path == "skills/togo/README.md":
        continue
    previous=blob(PRIOR,path)
    preserved.append({"path":path,"sha256":sha(previous),"git_blob":git("rev-parse",f"{PRIOR}:{path}").decode().strip(),"frozen_equals_prior":blob(CONTENT,path)==previous,"working_equals_prior":(ROOT/path).read_bytes()==previous})
assert len(preserved)==57
assert all(r["frozen_equals_prior"] and r["working_equals_prior"] for r in preserved)
addition=json.loads((WRITER/"readme-addition.json").read_text())
assert blob(CONTENT,"skills/togo/README.md") == blob(PRIOR,"skills/togo/README.md") + addition["append_exact"].encode()
write("preservation-receipt.json", {"prior_commit":PRIOR,"prior_guides":9,"prior_evidence_files":48,"complete_independent_tree_inventory":True,"files":preserved,"readme_exact_prior_plus_recorded_append":True,"old_body_units_replaced":0,"old_topics_destination":"All nine prior bodies and48 prior evidence files remain byte-identical; no prior topic moved or cut."})

sources=[]
for s in json.loads((WRITER/"source-identities.json").read_text()):
    data=Path(s["private_cache"]).read_bytes()
    sources.append({**s,"reviewer_sha256":sha(data),"reviewer_bytes":len(data),"identity_pass":sha(data)==s["sha256"] and len(data)==s["bytes"]})
assert all(r["identity_pass"] for r in sources)
artifacts=[]
for path in sorted(PRIVATE.iterdir()):
    if path.is_file():
        artifacts.append({"private_cache":str(path),"sha256":sha(path.read_bytes()),"bytes":path.stat().st_size,"purpose":"reviewer-produced extraction or visually inspected full page image"})
write("private-source-artifacts.json", {"read_on":"2026-11-01","source_pdfs":sources,"artifacts":artifacts,"scope":"CGI/LPF physical252-255 extracted with own pdftotext;253-254 full page images read; LF2026 full physical14,3,45 images read. Raw text/PNG remain outside Git. Cached original reused; no new whole-code or later-law-chain read claimed."})

spec=importlib.util.spec_from_file_location("rental_review_checks",ROOT/"scripts/skill_checks.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
shape=module.run_all(str(ROOT/"skills/togo/tg-rental-withholding.md"))
assert len(shape)==15 and not any(shape.values())
commands=[
 ["python3","scripts/skill_checks.py","skills/togo/tg-rental-withholding.md"],
 ["python3","scripts/check-examples.py","--require","skills/togo/tg-rental-withholding.md"],
 ["python3","scripts/check-sync-integrity.py","--base",MAIN,"--head",CONTENT,"--strict-metadata"],
 ["python3","scripts/validate-guides.py","--changed-only","--no-index-check"],
 ["git","diff","--check",f"{MAIN}..{CONTENT}"],
]
executions=[]
for command in commands:
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    executions.append({"command":command,"exit_code":p.returncode,"stdout":p.stdout,"stderr":p.stderr})
assert all(r["exit_code"]==0 for r in executions)
gross=Decimal("200000")
withholding=gross*Decimal("0.0875")
property_component=gross*Decimal("0.0375")
income_component=gross*Decimal("0.05")
assert withholding==17500 and property_component==7500 and income_component==10000
assert property_component+income_component==withholding
cases=[
 {"case":"Corporate tenant, May2026 identified single monthly period","gross_rent":str(gross),"withholding":str(withholding),"landlord_cash":str(gross-withholding),"property_component":str(property_component),"income_component":str(income_component),"component_total":str(property_component+income_component),"deadline":datetime.date(2026,6,15).isoformat(),"legal_decision":"Legal-person tenant in article100 class; paid proof and assessment bulletins still required for separate credits."},
 {"case":"Business natural person versus ordinary private tenant outside enumerated classes","business_withholding":str(withholding),"business_landlord_cash":str(gross-withholding),"private_tenant_full_rent":str(gross),"owner_declared_advance":str(withholding),"private_landlord_cash_after_advance":str(gross-withholding),"legal_decision":"Article100 tenant route versus article101 owner route; full-rent versus net-rent cashflows differ before owner advance. Listed-tenant default excluded, solidarity not waived, final assessments not computed."},
]
guide=blob(CONTENT,"skills/togo/tg-rental-withholding.md").decode()
fm=guide.split("---",2)[1]
platform=["review_status","license","authored_by","trust_label","drafted_by","approved_by","validation_status","validated","verified_by","reviewed_by","reviewed_on"]
later_delta=[]
for path in git("diff","--name-only",CONTENT,"HEAD").decode().splitlines():
    data=blob("HEAD",path)
    later_delta.append({"path":path,"sha256":sha(data),"bytes":len(data),"interpretation":"later validation receipt only; source review remains bound to original content"})
assert [r["path"] for r in later_delta]==["evidence/ledgers/togo-rental-20261101/committed-validation.json"]
write("mechanical-receipt.json",{
 "review_date":"2026-11-01","content_commit":CONTENT,"prior_commit":PRIOR,"main_base":MAIN,"head_at_receipt":git("rev-parse","HEAD").decode().strip(),
 "result":"accepted for bounded source fidelity; no source correction required; independent review complete",
 "frozen_files":frozen,"writer_freeze_all_hashes_match":True,"later_evidence_delta":later_delta,
 "shape_checks":shape,"commands":executions,"independently_recomputed_cases":cases,
 "platform_written_keys_found":[k for k in platform if re.search(rf"^{k}:",fm,re.M)],
 "cta_found":"openaccountants-cta-block" in guide or "## Talk to" in guide,
 "general_reference_notice_present":"**General reference only.**" in guide,
 "two_validator_warnings_preserved":["Property slug has no tax-domain mapping; no country cell checked","Rental withholding inferred as PR while TG PR also holds payroll-social, a distinct job"],
 "scope":"Source fidelity of this addition only. Not accountant attestation, authenticated filing, complete-country coverage, later-law continuity certification or merge permission. No Guide/source/earlier-evidence edit, commit, push, PR or queue action by reviewer."
})

allowance=[]
substitutions=[
 ("skills/togo/tg-rental-withholding.md","Independent source review of this addition is pending;","Independent source review of this conditional addition completed on 2026-11-01;"),
 ("skills/togo/README.md","independent source review is pending for this addition.","independent source review completed on 2026-11-01 for this conditional addition."),
]
for path,old,new in substitutions:
    before=blob(CONTENT,path)
    assert before.decode().count(old)==1
    after=before.replace(old.encode(),new.encode(),1)
    allowance.append({"path":path,"before_sha256":sha(before),"literal_from":old,"literal_to":new,"expected_after_sha256":sha(after),"only_permitted_change":"one exact status literal substitution; all other bytes fixed"})
write("status-only-allowance.json",{"bound_content_commit":CONTENT,"review_result":"accepted within retained holds; no substantive source corrections needed","optional_writer_reconciliation":allowance,"conditions":["Preserve original writer freeze and all initial independent review files exactly","Keep original writer evidence as the historical pending checkpoint","No platform-key or CTA additions, no attestation/full-coverage/current-workflow or merge claim","Record actual before/after hashes and literal-only comparison in a new additive receipt before treating a reconciled version as covered","Any other Guide/README byte change requires a new focused content review"]})
print(json.dumps({"rows":len(reviews),"quote_matches":sum(r["quote_normalized_exact_match"] for r in reviews),"shape_checks":len(shape),"example_blocks":2,"command_exits":[r["exit_code"] for r in executions],"preserved_files":len(preserved),"frozen_files":len(frozen),"result":"accepted within retained holds"},indent=2))
