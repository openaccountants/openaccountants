import json, hashlib, pathlib, re, subprocess
b=pathlib.Path('evidence/research/gibraltar-2026/completion-2026-10-31');o=b/'independent-review'; cp=json.loads((b/'checkpoint.json').read_text()); rows=json.loads((b/'ledger.json').read_text()); h=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
needs={
1:'GMTA s2(2)–(3): application to fiscal years and separate IIR date; the quote currently proves only commencement.',
2:'Article1.1: two of four years, proportional adjustment for a non12month year, Article6.1 crossreference. The750m fragment omits these.',
3:'GMTA s3 whole Wholly Domestic Group definition, location s3(4), and s15 Part4 treatment. The fragment identifies no threshold/location rule.',
4:'GMTA ss12–17: specified parent IIR charge, disapplied UTPR articles, Investment/Insurance Investment exclusion and separate constituent/JV joint liability. Current Wholly Domestic fragment is unrelated.',
5:'Rule3AA(1),(3),(16): scope of both Acts, ordinarily resident/registered/established constituent entity and UPE definition. Current Approved Election fragment is unrelated.',
6:'Rules3(55),3AA(2),(4)–(6): written request and approval, approval date, mandatory approval when requirements met and charge disapplication. Current fragment stops before the operative words.',
7:'Rule3AA(9)(b): finish quote through not yet due; distinguish basisperiod start from election/approval dates.',
8:'Rule3AA(8):30day rejection-notification trigger and grounds as well as both recipients.',
9:'Rule3AA(10)–(14): cessation/notice, no more than18months, reasonable steps and Commissioner determination alongside18month fragment.',
10:'Rule3AA(15): PartVI/Schedule4 and election after1March2025. Approved Election fragment is unrelated.',
11:'ITA40(6)(a)–(b): counteract/disregard election and all three context factors; motive fragment only proves the trigger.',
12:'Label as retained research boundary, not a legally proved absence of all channels. A generic Approved Election fragment does not establish a negative.',
13:'GMTA s11: finish quote through fifteen percent; s18 ties computation to modified Model Rules.',
14:'Separate excerpts for ss4/6 interpretation timing,19 disapplications,20 QDMTT-only safe-harbour exclusion,21–22 covered-tax exclusions,23–25 pools/formula,8 averageFX. Formula alone covers one component.',
15:'GMTA s7 election effect. Formula quote is unrelated to elections; remaining computational exclusions are a scope declaration.',
16:'GMTA ss26–27: ordinary15months, conditional18months with both tests, UPE/DFE versus DLE and supporting information.',
17:'GMTA28(1)–(4): effective reportingyear QCAA, actual foreign filing, required notifications, Part3/4 notifier roles as well as3month timing.',
18:'GMTA29(2)–(3): payer and multipleparent joint liability, alongside due date.',
19:'Tie the15/18month arithmetic to both conditions. The old404 claim has no identified URL/receipt in this35row ledger; preserve its original dated provenance or identify its exact oldURL.',
20:'Quote/register separately: cohort dates,28February deadline, sixmonth registration; GMTAREG1 including registering entity; ID/director authorisation; fields/role/new-versus-CbC steps; changes/outofscope sixmonths/newDLE12months. Current single deadline quote covers one fact only.',
21:'Notification §4/GIR §1:2024 Reporting Fiscal Year common understanding and section48 penalty relief. Current3month quote is unrelated.',
22:'Notification Appendix1 steps1–10: TIN, Reports/Unscheduled/delegation, A–G fields, Preview/Report, Valid/Invalid, Edit/resubmit/Actions. Current3month quote is unrelated.',
23:'GIR §4–8/Appendix1: dissemination, no test environment, four validation rules and exact codes, upload/receipt versus validity, rejection and step9 accepted-amendment gap. XML-format quote covers only format.',
24:'GMTA1 fields1–6, authorised signatory, liability trigger, separate return, due date; statutory18month conditions control shorthand form note. Email quote covers only destination.',
25:'GMTA1 p3 banktransfer only, unique assigned topup reference and assistance contact/phone. Email-submission quote is unrelated to payment.',
26:'GMTA ss33–35: assessment/amendment limits and imported appeal rule in addition to retention s30.',
27:'GMTA52(1)–(3): finish tenyear endpoint and refund/certification provisions; add ITA61(2) for the ordinarysixyear comparison, which GMTA52 alone does not establish.',
28:'GMTA44(1)(a)–(b): both2% and5%, remaining tax plus first surcharge,30day trigger. Current2percent fragment cannot substantiate5% or compound base.',
29:'GMTA43,45,47,48:1000/5000/500/further1000, onemonth trigger, discretion, statutory shall may defect. Current fragment contains none of the amounts.',
30:'Use ownlaw location/coveredtax/commencement/foreignfiling locators or label as crossreference control; notification timing quote alone does not substantiate those distinctions.',
31:'GMTA8 fiscalyear average sterling conversion as well as25 formula; mark all numerical inputs and resulting illustrative amounts as recomputed.',
32:'Same full s44 evidence asGMT28; mark illustrative principal and derived amounts as assumptions/calculations.',
33:'Label as writer/client evidence checklist; a fragment of Wholly Domestic Group definition does not source the entire checklist as a new legal duty.',
34:'Label as writer process controls, referencing the legal tests already evidenced; no generic deadline fragment as proof of all controls.',
35:'GIR Appendix1 step9 acceptedamendment instructions and official Act index for displayed version issue; separate inherited research limits/process assertions from statutory propositions.'}
process={12,33,34,35}
out=[]
for i,r in enumerate(rows,1):
 text=(b/r['reader_file']).read_text();norm=lambda s:re.sub(r'\s+',' ',s).strip()
 out.append({'id':r['id'],'statement_sha256':r['statement_sha256'],'read_on':'2026-10-31','official_url':r['official_url'],'source_locator':r['act_article_or_document_section'],'writer_quote_present_verbatim_after_whitespace_normalisation':norm(r['quote']) in norm(text),'full_source_assessment':'retained process/scope control; no new substantive tax rule asserted' if i in process else 'no substantive tax discrepancy found against full cited primary text and relevant neighbouring sections','writer_quote_evidence':'needs expansion or process classification; not a whole-row pass from the supplied fragment','required_repair':needs[i]})
(o/'row-review.json').write_text(json.dumps(out,indent=2)+'\n')
manifest={p:d for g in ['guide_files','evidence_files'] for p,d in cp[g].items()};manifest[str(b/'checkpoint.json')]=h(b/'checkpoint.json')
for p in ['AGENTS.md','CLAUDE.md','docs/skill-template.md','docs/OWNERS.md','scripts/validate-guides.py','scripts/skill_checks.py','scripts/check-examples.py']:manifest[p]=h(p)
changed=[p for p,d in manifest.items() if h(p)!=d]
if changed:raise RuntimeError('REVIEW INPUT CHANGED: '+str(changed))
(o/'input-hashes.json').write_text(json.dumps({'reviewed_commit':'393be24383a0fee17a7fcc3ea6a6bd2d87d4076a','review_base':'53696ccc7','hash_algorithm':'sha256','files':manifest,'unchanged_at_review_end':True},indent=2)+'\n')
preserv=json.loads((o/'preservation-results.json').read_text()); verdict={'reviewed_commit':'393be24383a0fee17a7fcc3ea6a6bd2d87d4076a','review_scope':'minimum-tax delta full35row primary-source review; sixGuide mechanical preservation; README truthfulness and validation; not completecountry acceptance','verdict':'CHANGES_REQUESTED_EVIDENCE','ledger_rows_checked':35,'new_substantive_tax_errors_found':0,'blocking_findings':[{'id':'R1','type':'writer ledger sourcequote completeness','count':'one systematic evidence defect across grouped rows; each35row disposition in row-review.json','required':'Repair writer quotes/process classification and bind new ledger hashes; request bounded closure of evidence repairs.'}],'country_complete':False,'ready_for_review':False,'push_or_merge_authorised_by_this_review':False,'validation':{'seven_guides_skill_checks':'70/70 pass','whole_country_examples':{'files':19,'blocks':29,'failures':0},'whole_changed_country_validation':{'errors':11,'warning_groups':55,'pass':False}},'preservation':preserv,'input_manifest_sha256':h(o/'input-hashes.json'),'reviewer':'independent Codex agent; not writer; no accountant attestation'}
(o/'verdict.json').write_text(json.dumps(verdict,indent=2)+'\n')
summary='\n'.join(f"| {r['id']} | {needs[i]} |" for i,r in enumerate(rows,1))
report=f'''# Independent Gibraltar continuation review, 31 October 2026

Verdict: **changes requested to writer evidence**. No substantive tax-content error was found in the reviewed minimum-tax delta against the full supplied official texts. This does not accept all35 ledger rows on their quote fragments, certify country completeness or establish a green PR.

Reviewed commit: `393be24383a0fee17a7fcc3ea6a6bd2d87d4076a`, base `53696ccc7`. The reviewer did not write the Guides. No Guide, prior review, writer ledger or checkpoint was edited; no commit, external message, filing, payment, push or merge was made. Exact Guide/evidence/standard/script hashes are in [input-hashes.json](input-hashes.json). Every checkpoint hash matched before review and at completion.

## Finding R1: the full ledger does not yet provide evidence for every rule

The35 grouped rows contain verbatim snippets but many snippets omit their own operative figure, or concern a different provision entirely. GMT04 quotes a Wholly Domestic Group fragment for IIR/UTPR/investment/joint-liability rules; GMT10 uses an Approved Election fragment for the post1March2025 antiavoidance rule; GMT13 stops before fifteen percent; GMT21–22 quote a notification deadline for commonunderstanding relief and A–G portal workflow; GMT25 quotes GMTA1 email submission for banktransfer/payment-reference/contact requirements; GMT28/32 quote only a two-percent fragment for five-percent and compound-base calculations. The ledger must distinguish writer process declarations from statutory obligations.

This is a systematic writer-evidence defect, not evidence that those Guide rules are false. The reviewer read the complete relevant primary text and neighbours rather than awarding whole-row approval from the fragments. [row-review.json](row-review.json) contains a separate assessment for every row. Repair the evidence while retaining the unchanged Guide bytes where the official text supports them; then obtain a bounded evidence-repair closure. In particular GMT27 also needs ITA61(2) for its ordinarysixyear comparison; the cited GMTA52 establishes only the minimum-tax tenyear claim period.

| Row | Required evidence repair or classification |
|---|---|
{summary}

## Sources actually checked

Seven Gibraltar PDFs were independently fetched on31October2026 over ordinary HTTPS, each returning200 and exactly the checkpoint SHA256. [fetch-receipts.json](fetch-receipts.json) records URLs/bytes/hashes. Direct shell fetch initially failed because of sandbox DNS; ordinary web/browser was tried; the same ordinary HTTPS fetch succeeded with network permission. No CAPTCHA or disguised request was used. The OECD direct request returned403; the official PDF was read through the web tool, Article1.1 plus neighbouring1.2–1.5. No archive was needed. The official AEOI landing page independently showed links to the four current operational PDFs; the official Act index displayed both Current Version and outofdate labels as disclosed.

The full GMTA text was read, particularly ss2–8,11–30,33–36,43–49,52 and their surrounding provisions; rr3(55),3AA(1)–(16); ITA40(6) and61; OECD1.1 and neighbours; all sections and appendices in the10February registration,1June notification,11June GIR guidance and June GMTA1. Four supplied rendered pages were visually inspected for registration fields, Preview/Report, receipt-versus-validation, and payment instructions. All35 writer snippets occur in the supplied primary extraction after whitespace normalisation; presence alone is not sufficiency. General fullGloBE computation, safeharbours, allocation, elections/cessation, acceptedGIR amendments and live authority acknowledgement remain in their expressly unconfirmed scope. No fiscalyear OECD guidance reconciliation was inferred from merely fetching the2021 Model Rules.

## Preservation and arithmetic

[Preservation results](preservation-results.json) independently reproduce all1179 nonblank original body lines in order across six Guides, allowing only the documented link/version/rowURL/read-date formatting repairs. All12 executable blocks are byte-exact. All six before snapshots match the base Git blobs. The minimum-tax30unit map retains every unit marked exact, both original controls are byte-exact, and the three changed map units are the disclosed review-status and superseded operational-gap disclosures. No old substantive rule was lost: **Lost content restored:0**.

The170 moved historical evidence files match both the manifest and their pre-move Git blobs byteforbyte. Existing completed reviews keep their scopes. These mechanical checks do not freshly reattest the old substantive tax work.

Both examples were independently recomputed:0.03×800000+2000=26000;26000×0.85=22100;zero-percentage case retains2000. On unpaid10000, first surcharge200, second510 when both remain unpaid, total10710; second500 if first surcharge was paid. Threshold boundary controls produce two qualifying years for740/750/760/730 and one for740/749/760/730.31December2024 plus15/18calendar months gives31March/30June2026; tenyear endpoint31December2034. Hypothetical election dates retain their explicit assumptions. No example proves input derivation or taxpayer eligibility.

## Validation and publication limits

Independent reruns: seven canonical tax Guides70/70 mechanical checks pass;19Markdown files/29oa-check blocks/0failures. Whole changed-country validation **fails with11errors and55warning groups**, matching the writer log. [validation-guides.log](validation-guides.log) records them. The eight old Guides with errors remain the writer's identified list; no waiver follows from their age. System/bundled Python initially lacked PyYAML; the existing validation-deps path supplied it for the final exact runs. An accidental fulltree help invocation was interrupted and is not validation evidence.

The README retains all sevenpartial entries, limits the current operational addition, preserves earlier review scope and still includes other tax jobs beyond the core domains. Its description of the ledger as complete needs to be read as a writer claim pending R1 repair. Country completeness, every applicable tax job, the inherited validation failures, and a green existing PR remain outstanding. This review does not set professional-review metadata, promote trust or treat partialpublication as achievement of the user's whole objective.
'''
(o/'review.md').write_text(report)
print('files written',len(manifest),'input hashes');print('input manifest',h(o/'input-hashes.json'));print('verdict',h(o/'verdict.json'));print('report',h(o/'review.md'))
