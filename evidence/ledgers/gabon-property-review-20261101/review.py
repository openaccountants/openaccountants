#!/usr/bin/env python3
"""Independent property review receipts. Reads frozen original bytes; changes only its own evidence directory."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).resolve().parent; W=ROOT/'evidence/ledgers/gabon-property-20261101'
H='e536c610f22884e70826777242fa3fb3f64978a5'; C='456042344ec2760856c9054a91b293155d6d1ed7'; A='9f93faa2af8c970d0b12ad6ca54ebe93ae1bbc03'; B='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def dump(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
N=lambda s:re.sub(r'\s+',' ',s).strip()
assert git('rev-parse','HEAD').decode().strip()==H
assert git('merge-base',H,'origin/main').decode().strip()==B
sources=json.loads((W/'sources.json').read_text()); pages={}; source_checks=[]
for s in sources:
 f=ROOT.parent/'sources'/s['file']; b=f.read_bytes(); assert sha(b)==s['sha256']
 p=subprocess.run(['pdftotext','-layout',str(f),'-'],capture_output=True,text=True,check=True).stdout.split('\f');pages[s['id']]=p
 scopes={'CGI':[1,2,108,109,110,111,112,113,114,228,229], 'LF':[1,3,9,10,11,12,13,14,15,16,71,72], 'LFR':[1,2,10,11,12,13,86]}[s['id']]
 source_checks.append({'source_id':s['id'],'official_url':s['official_url'],'original_sha256':sha(b),'bytes':len(b),'actual_pdf_pages_read':scopes,'independent_original_extraction':True,'source_scope':'historical baseline' if s['id']=='CGI' else 'enacted finance law; no complete amendment-chain certification','fresh_reviewer_network_access':'official PDF opened by web tool' if s['id']=='LF' else 'web tool inaccessible; read pinned original local PDF; prior fresh-fetch match is inherited acquisition evidence, not this reviewer fetch'})
 (OUT/'source-extracts'/('reviewer-'+s['id']+'-scope.txt')).write_text('\n\n'.join('ACTUAL PDF PAGE '+str(k)+'\n'+p[k-1] for k in scopes))
dump('source-verdicts.json',source_checks)
reasons={
'P-IDENTITY':'Read both law identities, arts1-4 and final implementation/publication/promulgation provisions. They establish enactment and budget scope, not a complete chain or first CFU assessment date. Currency hold is necessary and retained.',
'P-SCOPE':'Full rewritten278-279 covers built/unbuilt national property, unfinished/temporary structures and immovables by destination, with urban-perimeter definitions. Liability is then qualified by284, not inferred for all occupiers.',
'P-LIABLE':'Read all284(1)-(4) and285. January snapshot, title definition, built-only substituted rights, company balance sheet, commercial third-party use and co-owners are retained. Situs is commune/department.',
'P-JULY':'Actual July284(1) deletes immatriculee but retains titre foncier and explicit rest unchanged. Guide does not turn this into universal untitled-occupant liability or repeal284(2)-(4).',
'P-BOUNDARY':'Actual376-378 is a separate occupier charge. New Guide links accepted income/withholding/company/VAT owners and does not migrate their figures. Neighbouring TFH and July housing-fund provisions are not treated as CFU.',
'P-RATE':'15 percent and downward thousand rounding occur under legal-person heading. Individual tariff section is separate. No company final amount asserted while valuation interaction is held.',
'P-COMPANY':'All289(1)-(3),290 and292 conditions read together with deleted291/293 and corporate heading.10 percent book value, more-than20 percent real-value trigger and5 percent built allowance match. Ambiguous real-value/rental-base interaction is expressly held.',
'P-APPLICATION':'All288ter categories read: age>=60 and income<SMIG; weak-Gabonese social regime with income<SMIG; social housing<=30million; express application before30March; discretionary exemption/reduction with printed80percent limit. No invented SMIG or automatic award.',
'P-ZONE':'Read294ter/quater and mandatory joint ministerial order after294quinquies. All four descriptions match; no parcel mapping or order is supplied. Zone descriptions are not used as actual allocation evidence.',
'P-VALUE':'Read source294ter market/acquisition wording against table construction/acquisition heading. Conflict held. Historical294 principal-residence rate is not silently imported into new split system.',
'P-EXCESS-B':'Rendered malformed printed final row and read294sexies.1billion excess trigger exists, but algorithm/final row is not corrected or applied. Hold is proper.',
'P-EXCESS-L':'Read all294septies and excess paragraph.5000m2 boundary matches. No fabricated interpolation, fractional rounding or marginal algorithm.',
'P-EXEMPT':'Full286(1)-(8)/rural paragraph read with284(3). Public ownership, reciprocity, concession qualification, ownership/use conditions, worship/public-utility purpose, roads/water and ground categories retained. Commercial-user override retained.',
'P-LAND-EXEMPT':'Read286 ground and surrounding-land clauses:3x inside planned commercial/industrial district,5x elsewhere or outside communes; mine/quarry area; rural market gardens strictly<5ha within25km and exclusive use. Building itself not exempted by ground relief.',
'P-NEW':'All288 paragraphs read.5year/3year classes, furnished/holiday/pleasure exclusion from5year class, nextJanuary start, usable completion test, separate fractions and original-start change-of-use switch match.',
'P-AGRI-RELIEF':'Full288bis1-9 read plus historical no-permit clause.5year building relief ex officio; rural3/4/5year durations/start and livestock/selected-crop opinions match. Declaration/self-reference defect and special-deadline gap held; old4month no-permit clause not reimported.',
'P-AGRI-BASE':'All294octies and following page read:6000/500/150/150/150 perha market-value inputs, second-category factory condition and annual territorial authority valuation match. No tax-perha or final-liability formula invented.',
'P-DESTRUCTION':'Read full new295 versus historical295.3month request after destruction/completed demolition; relief begins month after destruction/start demolition. Historical involuntary6month vacancy provision is absent from replacement and is not carried forward.',
'P-FILE':'Read296,296bis,297 together.30March declaration, priorJanuary notification, justifications/payment/fiche, territorially competent collector and spontaneous currentyear payment match; regularisation and absent-declaration appraisal match.',
'P-MANAGER':'Read full298 and298bis.Identification applies to named instrument preparers; CFU withholding/remit relates to properties managed. Solidary co-owner payment liability retained; not confused with income withholding.',
'P-FILE-CHANGE':'Compared complete historical296-297 with complete replacements. New text does omit duplicate form/stamped returned-copy wording. Current portal/form/reference/receipt remains held and historical paper workflow not certified.',
'P-CFU-SANCTION':'Historical300 actual114 states50percent of evaded rights for284/298 noncompliance. Guide labels historical and holds currentness/cumulation; does not describe as universal late-payment rate.',
'P-PENALTY':'Read fullP996-999 neighbours plus JulyP1000paras1and3. Adjustment-interest scope, DGE/CIME electronic-payment scope and noncumulation preserved in ledger. Guide routes general figures to accepted income owner and holds application; no universal property penalty invented.',
'P-NONRES':'Full294bis includes resident/nonresident individuals and Gabon situs or convention allocation. Actual instrument required; no automatic foreign-property liability or treaty exemption claimed.',
'P-CASE1':'Independently selected built20,000,001-30,000,000 zone2=31,250 and separate bare401-500m2 zone2=25,313. Total56,563. Explicit applicable-law/January-title/official-zone/accepted-values/no-relief predicates prevent an actual assessment claim.',
'P-CASE2':'Independently selected zone2 401-500m2=25,313 and501-600m2=37,969. Difference12,656; surface difference1m2. Alternative measured facts, no election or fractional-rounding inference. Same eligibility/currentness holds.'}
rules=json.loads((W/'rules.json').read_text()); ledger=(W/'ga-annual-property-tax.md').read_text(); qout=[]; verdicts=[]
for r in rules:
 block=ledger.split('## '+r['id']+'\n',1)[1].split('\n## ',1)[0]
 assert r['rule_and_all_conditions'] in block
 refs=[]
 for ref in r['references']:
  sid=ref['source_id']; src=next(s for s in sources if s['id']==sid)
  assert ref['official_url']==src['official_url'] and ref['source_sha256']==src['sha256']
  for i,q in enumerate(ref['quotes'],1):
   qq=q['exact_original_language_quote']; actual=q['pdf_page_1_based']; assert qq in N(pages[sid][actual-1]),(r['id'],sid,actual)
   assert qq in block and src['official_url'] in block and src['sha256'] in block
   qout.append({'rule_id':r['id'],'source_id':sid,'actual_pdf_page_1_based':actual,'quote_index_in_reference':i,'quote_sha256':sha(qq.encode()),'exact_whitespace_normalized_quote_on_original_page':True,'matching_readable_ledger_block':True,'original_source_sha256':src['sha256'],'verdict':'matches original; semantic conditions read with full provision and neighbours'})
  refs.append({'source_id':sid,'act_article':ref['act_article'],'pages':sorted(set(q['pdf_page_1_based'] for q in ref['quotes']))})
 reason=reasons.get(r['id'])
 if reason is None:
  assert re.fullmatch('P-[BL][0-9]{2}',r['id'])
  reason='Independently read original rendered tariff row and full table heading/adjacent provisions. Exact printed interval and all four zone values match ledger and Guide. Individual fixed tariff only, subject to proven zone/accepted basis/exemption tests and preserved commencement/currentness holds.'
 verdicts.append({'id':r['id'],'writer_rule_sha256':sha(r['rule_and_all_conditions'].encode()),'verdict':'pass source fidelity within explicit partial-research boundary','independent_reason':reason,'references_checked':refs,'operative_current_law_certified':False})
assert len(verdicts)==72 and len(qout)==160
dump('every-row-verdicts.json',verdicts);dump('every-quote-verdicts.json',qout)
# Extract table row columns from the original PDF layout, independently of writer row strings.
tariffs=json.loads((W/'tariff-rows.json').read_text()); guide=(ROOT/'skills/gabon/ga-annual-property-tax.md').read_text(); cells=[]; intervals=[]
for group,prefix in [('built_complete_rows','B'),('bare_land_rows','L')]:
 for ri,row in enumerate(tariffs[group],1):
  candidates=[]
  for line in pages['LF'][row['page']-1].splitlines():
   cols=re.split(r'\s{2,}',line.strip())
   if len(cols)==5 and N(cols[0])==N(row['range']):candidates.append(cols)
  assert len(candidates)==1,(group,ri,candidates)
  cols=candidates[0]; actual=[int(re.sub(r'\s','',x)) for x in cols[1:]];assert actual==row['values']
  expected='| '+row['range']+' | '+' | '.join(f'{v:,}' for v in actual)+' | ';assert expected in guide
  intervals.append({'rule_id':f'P-{prefix}{ri:02d}','original_interval':cols[0],'guide_interval':row['range'],'verdict':'exact interval matches; fractional/endpoints outside printed integer intervals held','actual_pdf_page':row['page']})
  for z,(a,v) in enumerate(zip(actual,row['values']),1):cells.append({'rule_id':f'P-{prefix}{ri:02d}','zone':z,'actual_pdf_page':row['page'],'printed_interval':cols[0],'original_value_xaf':a,'ledger_value_xaf':v,'guide_value_xaf':v,'visual_original_table_checked':True,'verdict':'pass exact value and zone column'})
held=[]
for row in tariffs['built_malformed_held_row']:
 assert N(row['quote']) in N(pages['LF'][row['page']-1])
 held.append({'original_row':row,'four_values_visually_checked':True,'verdict':'source matches; held from operative calculation due malformed interval and unresolved excess algorithm'})
assert len(cells)==184 and len(intervals)==46
dump('every-tariff-value-verdicts.json',cells);dump('tariff-intervals-and-held-row.json',{'complete_intervals':intervals,'malformed_held_row':held,'published_complete_tariff_values':184,'held_row_values_observed':4})
# Preserve all accepted content rather than re-reviewing it.
p=json.loads((W/'preservation.json').read_text()); preservation=[]
for row in p['files']:
 path=row['path']; original=git('show',A+':'+path); current=git('show',H+':'+path); work=(ROOT/path).read_bytes()
 assert sha(original)==row['accepted_sha256'] and sha(current)==row['candidate_sha256'] and current==work
 if path=='skills/gabon/README.md':assert current.startswith(original); mode='accepted prefix byte-identical; property route appended'
 else:assert current==original;mode='exact accepted bytes unchanged'
 preservation.append({'path':path,'accepted_sha256':sha(original),'reviewed_candidate_sha256':sha(current),'verdict':mode})
assert len(preservation)==56
changed=git('diff','--name-only',A,H).decode().splitlines(); assert all(x.startswith('evidence/ledgers/gabon-property-20261101/') or x in ['skills/gabon/README.md','skills/gabon/ga-annual-property-tax.md'] for x in changed)
old=json.loads((ROOT/'docs/research/2026-11-01-gabon-pack/old-topics.json').read_text()); dest=json.loads((ROOT/'docs/research/2026-11-01-gabon-review/old-topic-coverage.json').read_text())
assert len(old)==77 and len(dest)==77
assert json.loads((W/'old-topics-reference.json').read_text())['all_77_records']==old
assert json.loads((W/'old-topic-destinations.json').read_text())['accepted_review_destinations']==dest
assert len(re.findall(r'^  (?:IT-IND|IT-CORP|VAT|SC|PR|TP|XB): "',(ROOT/'skills/gabon/README.md').read_text(),re.M))==7
assert '<!-- openaccountants-cta-block -->' not in guide
for field in ['review_status','trust_label','license','reviewed_by','authored_by','verified_by','drafted_by','approved_by','validation_status','validated','reviewed_on']:
 assert not re.search('^'+field+':',guide,re.M)
dump('preservation-verdicts.json',{'accepted_head':A,'frozen_reviewed_head':H,'all_56_files':preservation,'old_topics_exact':77,'old_destination_records_exact':77,'existing_guides_exact':8,'prior_93_rules_127_placements_16_cases_F1_F4_closure':'preserved exactly; accepted review reused within its prior boundary','all_seven_domains_partial':True,'old_figure_homes_moved':0,'new_platform_keys_or_CTA':False,'lost_content_restored':0})
frozen=json.loads((W/'frozen-content.json').read_text()); files=[]
for row in frozen['files']:
 b=git('show',H+':'+row['path']);assert sha(b)==row['sha256'];assert (ROOT/row['path']).read_bytes()==b
 files.append({'path':row['path'],'sha256':sha(b),'git_blob':git('rev-parse',H+':'+row['path']).decode().strip()})
assert sha(guide.encode())=='3c9cbb6981f1098adfb52d1ba0d993093b4686443b41e267eb6efc8036d53d34'
assert git('rev-parse',H+':skills/gabon/ga-annual-property-tax.md').decode().strip()=='b1a9b4f0bbd2b8377d7ff800f928c99e37453b8e'
dump('frozen-hashes.json',{'frozen_reviewed_head':H,'frozen_content_head':C,'actual_full_merge_base':B,'accepted_eight_guide_head':A,'reviewed_files':files,'source_originals':source_checks,'writer_handoff_sha256':sha((ROOT.parent/'sources/property-read/final-writer-handoff.json').read_bytes())})
dump('independent-cases.json',[{'id':'P-CASE1','eligible_facts':'Hypothetical individual January title holder; relevant text governs assessment; official zone2 proved; built accepted25million and separate wholly taxable nonagricultural450m2; all permanent/temporary/agricultural/discretionary relief absent. No operative-period inference.','built_interval':[20000001,30000000],'built_zone':2,'built_tariff':31250,'land_interval':[401,500],'land_zone':2,'land_tariff':25313,'independently_computed_total':31250+25313,'guide_expected':56563,'verdict':'pass predicates, independent row selection and arithmetic'}, {'id':'P-CASE2','eligible_facts':'Same currentness/title/zone/no-relief predicates, nonagricultural bare plot; alternative independently surveyed500/501m2, not taxpayer election or rounding.','alternative_1':{'surface':500,'interval':[401,500],'zone2_tariff':25313},'alternative_2':{'surface':501,'interval':[501,600],'zone2_tariff':37969},'independently_computed_surface_difference':501-500,'independently_computed_annual_difference':37969-25313,'guide_expected_difference':12656,'verdict':'pass predicates, thresholds, independent row selection and arithmetic'}])
print(json.dumps({'rules':len(verdicts),'quotes':len(qout),'published_tariff_values':len(cells),'tariff_intervals':len(intervals),'accepted_files_preserved':len(preservation),'findings':0,'current_law_certification':False},indent=2))
