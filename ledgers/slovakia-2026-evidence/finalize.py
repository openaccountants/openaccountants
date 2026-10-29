from writer import *
from old_topics import units
from datetime import date
out=ARCH.parent/'sk-ledger-writer-2026-10-28';out.mkdir(exist_ok=True)
slugs=['slovakia-pit','sk-corporate-income-tax','sk-payroll-social','sk-cross-border','sk-transfer-pricing','slovakia-vat-return','slovakia-vat-registration-4-7-7a']
original=json.loads((EVID/'current-guide-identities.json').read_text());successor=json.loads((EVID/'guide-successors.json').read_text());orig={Path(r['path']).stem:r for r in original};checks=[];inventory=[]
def test(n,v):
 assert v,n;checks.append({'name':n,'pass':True})
for k,s in scopes.items():
 rr=s.get('actual_read_ranges',[[s['actual_read_LF_start'],s['actual_read_LF_end']]])
 for q in s['quotations']:test('Quoted scope actually read '+k+':'+str(q['LF_start']),any(lo<=q['LF_start']<=q['LF_end']<=hi for lo,hi in rr))
 test('Official URL present '+k,s['official_url'].startswith('https://'))
for slug in slugs:
 g=REPO/f'skills/international/slovakia/{slug}.md';l=REPO/f'ledgers/{slug}.md';gd=g.read_text();ld=l.read_text();expected=successor[0]['root_successor_sha256'] if slug=='slovakia-pit' else orig[slug]['sha256']
 test('Pinned exact Guide '+slug,sha(g)==expected)
 rs=json.loads((EVID/slug/'rows.json').read_text());old=json.loads((EVID/slug/'old-topics.json').read_text())
 test('Current ledger binds Guide '+slug,sha(g) in ld)
 test('Exactly2 original oa blocks '+slug,len(re.findall(r'^```oa-check\s*$',gd,re.M))==2)
 for r in rs:
  test('Exact Guide text '+slug+':'+str(r['row']),'\n'.join(lf(g)[r['LF_start']-1:r['LF_end']])==r['guide_wording'])
  for ref in r['source_scopes']:test('Resolvable source '+slug+':'+str(r['row'])+':'+ref,ref in scopes)
 test('Main all old units '+slug,[r['unit'] for r in old['rows']]==list(range(1,len(old['rows'])+1)))
 pre=old['earliest_preimage'];oldtext=subprocess.check_output(['git','show','origin/main:skills/international/slovakia/'+slug+'.md'],cwd=REPO)
 test('Main exact old hash '+slug,hashlib.sha256(oldtext).hexdigest()==old['main_sha256'])
 test('Main all actual blocks '+slug,len(units(oldtext.decode()))==len(old['rows']))
 for r in old['rows']:test('Old unit digest '+slug+str(r['unit']),hashlib.sha256(r['old_text'].encode()).hexdigest()==r['old_unit_sha256'])
 if pre['present']:
  test('Earliest complete map '+slug,[r['unit'] for r in pre['rows']]==list(range(1,pre['complete_old_units']+1)))
 inventory.append({'slug':slug,'guide_path':str(g),'guide_sha256':sha(g),'guide_bytes':g.stat().st_size,'ledger_path':str(l),'ledger_sha256':sha(l),'ledger_bytes':l.stat().st_size,'rule_rows':len(rs),'main_old_units':len(old['rows']),'earliest_old_units':pre.get('complete_old_units',0),'rows_json':str(EVID/slug/'rows.json'),'old_topic_map':str(EVID/slug/'old-topics.json'),'source_ids':sorted(set(x for r in rs for x in r['source_scopes']))})
# Demonstrate raw→derived provenance independently of selected-read assertion.
provenance=[]
for p in sorted((EVID/'shared').glob('*-article-*.txt')):
 sid=p.name.split('-')[0];native=ARCH/f'sources/{sid}.txt';blob=p.read_text();rawreader=native.read_text();pos=rawreader.find(blob.rstrip('\n'))
 test('Derived operative article literal '+p.name,pos>=0)
 lo=rawreader.count('\n',0,pos)+1;hi=lo+blob.rstrip('\n').count('\n')
 provenance.append({'derived_path':str(p),'derived_sha256':sha(p),'native_reader_path':str(native),'native_reader_sha256':sha(native),'native_LF_start':lo,'native_LF_end':hi,'raw_path':receipts[sid]['file'],'raw_sha256':receipts[sid]['sha256'],'actual_read':'Acquisition/extraction only; actual selected reads are separately catalogued, not implied by this comparison.'})
(EVID/'derived-article-provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
cmd=['python3','scripts/check-examples.py']+[str(REPO/f'skills/international/slovakia/{s}.md') for s in slugs];r=subprocess.run(cmd,cwd=REPO,text=True,capture_output=True)
(out/'original-example-checks.txt').write_text(r.stdout+r.stderr);test('14 actual original oa examples pass',r.returncode==0 and '14 oa-check blocks, 0 failures' in r.stdout)
# Preserve named source acquisition failures; none is a law quotation.
failures=[{'scope':'Payroll Regulation883/2004 Art11(1)/13 exact law excerpt','retained_actual_quote_scope':'SP.A1: actual pages6–9, native281–506; work-state Art11(3)(a),24monthArt12 and Art16exception; no literal Art11(1)/13 quotation asserted.','attempts':['Retained sources/03.html is JS robot challenge','Official EN consolidated EUR-Lex TXT route web result3lines JS robot challenge,29October2026','Normal urllib exact TXT route failed DNS29October2026','Hidden IAB creation returned Browser is not available: iab; no tab/body created'],'status':'Narrow direct-regulation quotation-evidence limitation, not an inferred contrary legal rule. Parent separately attempted two PDF routes, also challenge bodies; those are not reused as regulation text.'},{'scope':'Intrastat derived reader','failure':'Initial utf8 decode rejected; initial ISO8859-2 candidate rejected before citation; actual declared windows-1250 used. Raw unchanged.'},{'scope':'Derivative line bounds','failure':'Initial xb16PE bound178 beyond154 and CIT30 bound55 beyond50 asserted before invalid scope persisted; corrected exact bounds.'},{'scope':'Earliest VAT derivative extraction','failure':'16historical85kn exact header absent; script stopped beforeTC27 extract. Existing current85kntransition is separately read; TC27 exact current extracted subsequently.'},{'scope':'Semantic old-topic locator selfcheck','failure':'Prior-review fallback selected six irrelevant payroll destinations. Exact previous row identities retained privately, replaced by explicit current methods. No Guide change.'}]
(out/'writer-failure-history.json').write_text(json.dumps(failures,ensure_ascii=False,indent=2)+'\n')
(EVID/'final-writer-checks.json').write_text(json.dumps({'role':'Writer mechanical coverage/provenance only; no independent legal verdict.','count':len(checks),'checks':checks},indent=2)+'\n')
(EVID/'writer-progress.json').write_text(json.dumps({'date':DATE,'role':'Writer only; all7ledgers ready for a different fresh review, not independently cleared','Guides_unchanged_by_this_writer':True,'ledger_progress':inventory,'remaining':[],'retained_VAT_questions':['annual included-supplies denominator zero','fixed-gross crossing-supply payer-status circularity','TaxCode155(4) applicability to specialVAT78a(15)fine'],'separate_quotation_evidence_limit':'Payroll directEUArt11(1)/13 body unavailable; actualSPagencyA1coverage and failedroutes clearlydistinguished.'},indent=2)+'\n')
(out/'seven-guide-ledger-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
print(len(checks),'finite identity/coverage/provenance checks passed')
for x in inventory:print(x['slug'],x['rule_rows'],x['guide_sha256'],x['ledger_sha256'])
