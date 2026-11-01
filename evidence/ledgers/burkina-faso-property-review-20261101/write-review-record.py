#!/usr/bin/env python3
"""Materialize independent row verdicts and review boundaries, not Guide edits."""
import pathlib,json,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[3]; OUT=pathlib.Path(__file__).resolve().parent; SRC=ROOT.parent/'sources'
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
rows=json.loads((ROOT/'evidence/ledgers/burkina-faso-property-20261101/bf-company-property-tax.json').read_text())
notes=[
'Full art.251 enumerates precisely these five forms and ties liability to immovables they possess; local-authority destination is express. No all-IS-company extension.',
'Full art.252 first sentence fixes the owner/usufructuary at January 1 for the entire year. Guide does not invent a sale apportionment.',
'Art.252 second sentence expressly names the owner of the land for a construction lease, not automatically the building user.',
'Both exclusive-object condition and exceptions for exploited/non-sale properties retained; this is sociétés par action, not all property businesses.',
'Second bullet of art.253 names SONAPOST. No other ordinary exemption is claimed.',
'Full art.254 first paragraph supplies January rental value and 50% deduction for dépérissement/maintenance/repair. Read with next paragraph.',
'Full art.254 second paragraph removes deduction where grosses réparations are borne by tenant. Ordinary maintenance is not silently equated with major repairs.',
'Art.255(1) runs across pp.107–108: actual letting price or hypothetical rent for self-occupation, supporting case 1.',
'Full art.255(2) covers sols, all buildings and indispensable immediate land dependencies in assessment of the constructions. No cadastral contribution base imported.',
'Full first two paragraphs of art.255(3): authentic/normal oral leases, then comparison with regularly established or notoriously known rents. Order retained.',
'Third paragraph of art.255(3) permits direct appraisal only if neither earlier procedure applies. Market value, regional average property-return by type and application all retained.',
'Art.255(4) applies industrial/commercial land assigned-use valuation. No invented tariff or yield.',
'Full art.255(5) binds owner throughout construction-lease term and specifies annuity amortising works and lessee charges. Cash ground rent is not substituted; executable annuity method remains held.',
'Art.256 sets 10%. It is on the applicable art.254–255 base, so Guide rejects an unconditional 5%-of-rent rule.',
'Full art.257 chapeau: owner/usufructuary where appropriate, before November 1 annually, in writing to assessment agents on administration model. Not a verified payment date.',
'Art.257 expressly uses day of production for declaration particulars; art.254 uses January 1 for base. Guide preserves both dates.',
'Full art.257 item 1 read, including tenant personal/corporate identity omitted from short quoted fragment but retained in rule and Guide, let-premises description, principal rent and relevant charges.',
'Quote and substance are art.257 item 2. Writer locator 257(2)–(3) is overinclusive but includes exact operative item; item 3 is separately covered by P30. No correction needed.',
'Gazette p.18 article 34 expressly says Pour compter du 1er janvier 2026 before replacing article 772. Publication date January 2 is not substituted for commencement.',
'Full first replacement bullet: declaration inaccuracy/omission of assessment elements, 25% droits dus, XOF100000 floor. Full chapeau identifies TFS/article257, not a generic sanction.',
'Full second replacement bullet: late payment 10% droits dus plus 1% per month or fraction. Guide does not establish the first late day or sanction accumulation.',
'Full third replacement bullet: taxation d’office, 25% droits dus with XOF500000 floor. Distinct from P20 lower floor. Scanned signed text checked rather than trusting OCR cing.',
'Full art.271 exemption list and chapter heading read: general built contribution excludes immovables of legal persons subject to TFS. Does not establish every property-tax exemption.',
'Full art.273 exemption list and art.272 scope read: corresponding unbuilt contribution exclusion for land of persons subject to TFS. Distinct contribution base and taxable persons read through arts.274–275.',
'Full art.675 names direct taxes and assimilated taxes, bordereaux avis de versement, avis d’imposition or enforceable title. Guide uses as general collection rule only.',
'Full art.677 read, including spontaneous declarations/notices, insufficient spontaneous payment and adjustment branches. Guide does not transform this into a TFS calendar.',
'Both paragraphs of art.678 read: general spontaneous payment at due date except express provisions and immediate exigibility of notified adjustments. Art.679 additional triggers also read; enforcement remains held.',
'Full art.671 read: enumerated legal methods and conditions, relevant dating rules, universal official receipt. No authenticated channel or operative electronic ministerial instrument is claimed.',
'Full art.672 requires mention on notices/declarations of total/partial payment, date and receipt number. Guide carries these particulars.',
'Art.257 item 3 expressly requires description of vacant premises; Guide has separate bullet. No vacancy exemption invented.'
]
assert len(notes)==len(rows)==30
human=(ROOT/'evidence/ledgers/burkina-faso-property-20261101/bf-company-property-tax.md').read_text()
verdicts=[]
for row,note in zip(rows,notes):
    assert f"## {row['id']} |" in human
    verdicts.append({'id':row['id'],'writer_rule':row['rule'],'article':row['article'],'printed_and_physical_page':row['physical_page'],'official_url':row['official_url'],'source_sha256':row['source_sha256'],'source_quote_checked':True,'human_ledger_and_json_agree':True,'full_clause_and_conditions_checked':True,'guide_fidelity_verdict':'pass within stated scope','review_note':note})
save('row-checks.json',{'frozen_head':'13a38f884550d6d220f79100a8fbc1404842a1de','read_date':'2026-11-01','row_count':30,'distinct_numeric_figures':False,'method':'Each JSON and human-ledger record checked against full primary provision and Guide sentence, not a string-match-only audit. Short excerpts need not contain every condition because full clauses were read.','rows':verdicts})
sources=[]
for name,refetched,url,scope in [
('cgi-2026.pdf','cgi-refetched.pdf','https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf','Edition identification/preface and warning pp.1–6; full TFS chapter arts.251–257 pp.107–108, adjacent arts.245–250 and258–262 pp.106–109; residence/contribution boundary art.268 and full arts.269–275 pp.112–114, first valuation-order clauses p.115; full collection arts.669–679 pp.286–288 and neighbouring enforcement clauses; full art.772 with arts.769–774 pp.307–308 and following sanction boundaries p.309. CGI pp.107–108 independently rendered and visually read.'),
('finance-2026-gazette.pdf','finance-refetched.pdf','https://dgi.bf/wp-content/uploads/2026/01/JOURNAL-OFFICIEL-N%C2%B001-SPECIAL-LOI-DE-FINANCES-2026.pdf','Promulgation p.2 visually read against cached OCR, full signed article34/replacementCGI772 and adjacent articles32–33 p.18 independently rendered and visually read; surrounding articles30–31 p.17 and35–36 p.19 read against OCR. Gazette page18 is physical/printed18; embedded law manuscript footers31–32 are not Gazette locators. No full-law amendment-chain certification.')]:
    cached=(SRC/name).read_bytes(); fresh=(SRC/'property-review-20261101'/refetched).read_bytes();assert cached==fresh
    sources.append({'official_url':url,'read_date':'2026-11-01','sha256':sha(cached),'bytes':len(cached),'independent_refetch_matches':True,'cached_source':str(SRC/name),'independently_refetched':str(SRC/'property-review-20261101'/refetched),'actual_read_scope':scope})
save('source-read-log.json',{'date':'2026-11-01','web_open':'Both official URL web opens timed out. Direct curl retrieval of both official URLs succeeded independently, without bypassing any access restriction.','scope':'Only cited primary sources and relevant neighbouring clauses. No research beyond them was needed because no substantive source-fidelity check failed.','sources':sources,'raw_materials_outside_git':[{'path':str(p),'sha256':sha(p.read_bytes())} for p in sorted((SRC/'property-review-20261101').iterdir()) if p.is_file()]})
save('findings.json',{'frozen_head':'13a38f884550d6d220f79100a8fbc1404842a1de','blocking_findings':[],'substantive_corrections_required':0,'nonblocking_locator_observation':{'row':'P18','observation':'Writer cites art.257(2)–(3); quoted rent-free clause is specifically item2. The range includes it and P30 separately covers vacancy. No substantive misstatement or correction requirement.'},'status':'accepted for limited conditional source fidelity','not_attestation':True})
# Narrow exact status-only wording permitted to parent after reading this acceptance.
replacements=[
('skills/burkina-faso/bf-company-property-tax.md','This new job is a source-based writer draft pending independent review, without accountant attestation.','This new job has completed independent conditional source review for this workpaper scope, without accountant attestation.'),
('skills/burkina-faso/README.md','Its [writer ledger](../../evidence/ledgers/burkina-faso-property-20261101/bf-company-property-tax.md) is pending independent review.','Its [writer ledger](../../evidence/ledgers/burkina-faso-property-20261101/bf-company-property-tax.md) has completed [independent conditional source review](../../evidence/ledgers/burkina-faso-property-review-20261101/review.md).')]
status=[]
for p,old,new in replacements:
    data=(ROOT/p).read_bytes();assert data.decode().count(old)==1; altered=data.decode().replace(old,new).encode()
    status.append({'path':p,'before_sha256':sha(data),'old_exact':old,'new_exact':new,'after_sha256_if_only_this_replacement':sha(altered)})
save('status-only-permission.json',{'accepted_content_head':'13a38f884550d6d220f79100a8fbc1404842a1de','authority':'Reviewer acceptance scope only; does not create user authority for unrelated actions. Parent may reconcile these two stale status literals only. No change performed by reviewer.','replacements':status,'conditions':['Preserve every other byte of these files.','Preserve all writer ledgers, initial validation, freezes and earlier evidence as historical receipts.','Append a status identity receipt recording resulting hashes; rerun relevant validation.','No tier/attestation field, figure, domain coverage, law/rule, case, metadata version or source-hold change is covered.','Any other substantive edit requires a fresh source review.'],'excluded':['commit','push','PR edit/comment','merge','issue closure','production or generation changes']})
print('Wrote 30 independent row verdicts, source identities, findings and exact status-only hashes.')
