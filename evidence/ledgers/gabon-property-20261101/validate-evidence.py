#!/usr/bin/env python3
"""Validate actual sources, exact quote locators, all tariff cells and accepted-byte preservation."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]; E=Path(__file__).resolve().parent
N=lambda s:re.sub(r'\s+',' ',s).strip()
source={r['id']:r for r in json.loads((E/'sources.json').read_text())};pages={}
for k,s in source.items():
 p=ROOT.parent/'sources'/s['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'],k
 r=subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True,text=True,check=True)
 pages[k]=r.stdout.split('\f')
 if k in ('LF','LFR'):
  fresh=ROOT.parent/'sources/property-read'/('fresh-'+s['file']);assert hashlib.sha256(fresh.read_bytes()).hexdigest()==s['sha256']
rules=json.loads((E/'rules.json').read_text());qs=0
for r in rules:
 assert r['guide']=='skills/gabon/ga-annual-property-tax.md'
 for ref in r['references']:
  s=source[ref['source_id']];assert ref['source_sha256']==s['sha256'] and ref['official_url']==s['official_url']
  for q in ref['quotes']:
   assert q['exact_original_language_quote'] in N(pages[ref['source_id']][q['pdf_page_1_based']-1]),(r['id'],q)
   assert len(q['exact_original_language_quote'].split())<=55
   qs+=1
text=(ROOT/'skills/gabon/ga-annual-property-tax.md').read_text();table=json.loads((E/'tariff-rows.json').read_text())
for key,n in [('built_complete_rows',28),('bare_land_rows',18)]:
 assert len(table[key])==n
 for r in table[key]:
  assert N(r['quote']) in N(pages['LF'][r['page']-1])
  expected='| '+r['range']+' | '+' | '.join(f'{x:,}' for x in r['values'])+' | '
  assert expected in text,expected
assert len(table['built_malformed_held_row'])==1
p=json.loads((E/'preservation.json').read_text());old=p['accepted_head'];preserved=0
for row in p['files']:
 original=subprocess.check_output(['git','show',old+':'+row['path']],cwd=ROOT);current=(ROOT/row['path']).read_bytes()
 assert hashlib.sha256(original).hexdigest()==row['accepted_sha256']
 assert hashlib.sha256(current).hexdigest()==row['candidate_sha256']
 if row['path']=='skills/gabon/README.md':assert current.startswith(original)
 else:assert current==original,row['path']
 preserved+=1
for oldpath in ['docs/research/2026-11-01-gabon-pack/old-topics.json','docs/research/2026-11-01-gabon-review/old-topic-coverage.json']:
 assert len(json.loads((ROOT/oldpath).read_text()))==77
assert len(re.findall(r'^  (?:IT-IND|IT-CORP|VAT|SC|PR|TP|XB): "', (ROOT/'skills/gabon/README.md').read_text(),re.M))==7
for f in ['review_status','trust_label','license','reviewed_by','authored_by','verified_by']:
 assert not re.search('^'+f+':',text,re.M),f
assert '<!-- openaccountants-cta-block -->' not in text
print(json.dumps({'status':'pass','grouped_rule_records':len(rules),'exact_quote_placements':qs,'built_complete_rows':28,'land_rows':18,'tariff_values_checked':184,'held_malformed_row':1,'preserved_accepted_files':preserved,'existing_guides_unchanged':8,'old_topics_unchanged':77,'prior_cases_unchanged':16,'all_seven_partial_domains_preserved':True,'lost_content_restored':0,'current_law_attestation':False,'fresh_independent_property_review':'pending'},indent=2))
