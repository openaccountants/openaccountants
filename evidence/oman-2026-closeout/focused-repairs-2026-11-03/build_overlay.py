"""Focused F01–F13 evidence overlay. Never regenerates or edits frozen evidence."""
from pathlib import Path
import json,hashlib,re,copy,subprocess
ROOT=Path(__file__).resolve().parents[3];OLD=ROOT/'evidence/oman-2026-closeout/closeout-2026-11-03';REV=ROOT/'evidence/oman-2026-closeout/independent-closeout-2026-11-03';OUT=Path(__file__).resolve().parent
BASE='b013d729d9e373886c373f9a383a77f9e7e0ef9c'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(name,x):(OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
rows={r['id']:r for r in json.loads((OLD/'effective-source-ledger.json').read_text())}
findings=json.loads((REV/'findings.json').read_text());snips=json.loads((REV/'finding-source-snippets.json').read_text())
expected={id for f in findings for id in f['rows']}
assert len(expected)==17
patches={id:{'id':id,'findings':[f['id'] for f in findings if id in f['rows']],'replaces_fields':{},'source_read_on_preserved':rows[id]['read_on'],'excerpt_checked_on':'2026-11-03','status':'writer repair for focused independent closure; no independent PASS'} for id in expected}
def raw(path):return (ROOT/path).read_text()
def fragment(path,a,b,pages):
 t=raw(path);q='\n'.join(t.split('\n')[a-1:b]).strip()
 assert q
 return {'quote':q,'raw_text_cache':path,'newline_lines':[a,b],'physical_pdf_pages':pages,'cached_text_sha256':sha((ROOT/path).read_bytes())}
def passage(path,start,end,pages):
 t=raw(path);a=t.index(start);b=t.index(end,a);q=t[a:b].strip()
 assert q
 last=b-1
 while t[last].isspace():last-=1
 return {'quote':q,'raw_text_cache':path,'newline_lines':[t[:a].count('\n')+1,t[:last].count('\n')+1],'physical_pdf_pages':pages,'cached_text_sha256':sha((ROOT/path).read_bytes())}
def setquotes(id,frags):
 p=patches[id]['replaces_fields'];p.update(quote='\n\n'.join(x['quote'] for x in frags),quote_fragments=frags,excerpt_checked_on='2026-11-03',quote_scope='Complete decisive selected passages for consolidated findings; source-read dates preserved, continuation excerpts checked3November2026. Newline locators count only LF; physical PDF pages and exact text control.')
def extend(id,fragment):
 prior=rows[id].get('quote_fragments')
 frags=[{'quote':rows[id]['quote'],'provenance':'Earlier accepted/recorded excerpt retained; see frozen source row.'}]
 setquotes(id,frags+[fragment])
IT='../sources/prior-writer/itlaw.txt';IN='../sources/dc6c07a154ab.txt';RE='../sources/d093475a3da6.txt';FI='../sources/00e2a9830c8f.txt';RT='../sources/debd4cf3d454.txt'
setquotes('ITL-159bis-4',[fragment(IT,2114,2119,[88])]);patches['ITL-159bis-4']['replaces_fields']['pdf_page']=88
setquotes('ITL-159bis-5',[fragment(IT,2122,2134,[89])]);patches['ITL-159bis-5']['replaces_fields']['pdf_page']=89
setquotes('G02',[fragment(RE,439,449,[13]),fragment(RE,451,465,[14])])
# Preserve the accepted fee/exemption clauses; replace only the misplaced insurance fragment.
setquotes('G04',[{'quote':rows['G04']['quote_fragments'][0]['quote'],'provenance':'Frozen first fragment; accepted within recorded scope.'},fragment(FI,1251,1260,[30])])
# Exact section anchors avoid the old splitlines()/formfeed-versus-LF locator mismatch.
setquotes('G05',[passage(IN,'2.7   Time of Deduction\n','2.12 Mixed Use for Economic and Non-Economic Purpose',[18,19,20,21,22,23,24])])
p=patches['G05']['replaces_fields'];p['conditions']=rows['G05']['conditions']+' Pre-registration deduction additionally requires application within30days of effective registration on the prescribed form and all supporting details/documents (items1–9), including inventory at the day before registration and recognised-auditor verification if claimed goods exceedOMR50000. TA decides within30days after receiving details/documents; silence is rejection. Deduct only starting with the tax period following the period in which approval is notified. Lookbacks alone do not establish a deductible current-period amount.'
setquotes('G06',[passage(IN,'2.13 Blocked Input Tax\n','2.14 Mixed Use for Taxable and Exempt Supplies',[29,30])])
# Relevant non-economic attribution plus complete periodic and annual formulas, without unrelated examples.
setquotes('G07',[
passage(IN,'2.12 Mixed Use for Economic and Non-Economic Purpose\n','Example',[25]),
passage(IN,'2.14 Mixed Use for Taxable and Exempt Supplies\n','Example: A School',[31,32,33]),
fragment(IN,1214,1258,[35,36])])
setquotes('G08',[passage(RT,'3.3 VAT return payment or refund\n','3.5 Correction of VAT returns',[13])])
setquotes('G09',[passage(RT,'3.5 Correction of VAT returns\n','5. Penalties\n',[13,14])])
patches['P23']['replaces_fields']['conditions']='Art33: sole-employer filing on request only where the person has no income other than salary/wages, membership fees or pensions paid by one employer. End-of-service income is not an art33 sole-employer category. General charge and art43 withholding on end-of-service remain unchanged. Return includes gross/net/taxable income and tax due.'
patches['A02']['replaces_fields']['conditions']='FAQ2:3%taxpayers file within3months;15%taxpayers within4months with auditedaccounts. SME-regime-exempt filing is not a blanket3month rule for every exemption. Zero-revenue/expense return and non-practice letter require BOTH noactivity AND noworkers during the tax year; letter stamped AND signed. Exempt taxpayers supply exemption evidence.'
for id in ['VAT-20','VAT-23','VAT-24']:
 patches[id]['replaces_fields']['conditions']='Oman taxable recipient, Oman place of supply under23/24 and an applicable standard-rated service required for the5%current sentence. Art24 special place rules: transport begins; property location; non-taxable transport rental disposal; telecom/e-services actual use/benefit; listed restaurant/hotel/cultural/etc services actual performance. Deduct input only for eligible taxable-business use with required evidence and blocked-input restrictions. Foreign supplier name alone proves none of these conditions. Published box2b context unchanged.'
art28=next(x for x in snips if x['finding']=='F12')
for id,index,article in [('P08',0,'28'),('P21',1,'30 final paragraph')]:
 extend(id,{'quote':art28['quotes'][index],'raw_source':'../sources/pit-official.pdf','physical_pdf_pages':[14],'gazette_page':20,'article':article,'language':'Arabic original','method':'Exact independent-review transcript checked against previously read cached original page; no OCR/English-to-Arabic invention.','review_snippet_source':'../independent-closeout-2026-11-03/finding-source-snippets.json#F12'})
patches['SPL128']['replaces_fields']['conditions']='Employer1%monthlywage, calculateddaily. Coverage/exclusions are closed by available law art127, explicit controlling cross-reference to supplemental SPL127 (physicalPDFp53/printed51): compulsory Omanis in Oman including temporary/training/retired; exclude self-employed,part-time,GCC-working/overseas Omanis; non-Omani categories require Boarddecision. Preserve genuine Boardcategory/start decisions and historical maternity/sick commencement conflicts; no stale core127hold.'
for id,p in patches.items():
 src=rows[id];p['source_identity']={k:src[k] for k in ['raw_path','raw_sha256','official_url','source_language','act','article']};assert sha((ROOT/src['raw_path']).read_bytes())==src['raw_sha256']
 if 'quote' not in p['replaces_fields']:p['unchanged_quote_ref']='../closeout-2026-11-03/effective-source-ledger.json#'+id
 p['replaces_fields']['excerpt_checked_on']='2026-11-03'
dump('source-overrides.json',[patches[id] for id in sorted(patches)])
# Fixed baseline identity, all current Guide hashes, and complete rebasing of423source uses.
guides={p.stem:p for p in (ROOT/'skills/oman').glob('*.md') if p.stem!='README'}
texts={g:p.read_text().split('\n') for g,p in guides.items()};manifest=[]
for g,p in guides.items():
 old=subprocess.check_output(['git','show',BASE+':'+str(p.relative_to(ROOT))],cwd=ROOT)
 manifest.append({'guide':g,'path':str(p.relative_to(ROOT)),'reviewed_baseline_sha256':sha(old),'current_sha256':sha(p.read_bytes()),'changed':old!=p.read_bytes(),'same_line_count':len(old.decode().split('\n'))==len(texts[g])})
assert all(x['same_line_count'] for x in manifest)
dump('guide-manifest.json',manifest)
uses=[];changeduses=[]
for id,r in rows.items():
 for old in r['placements']:
  g=old['guide'];a=old['line_start'];b=old['line_end'];t='\n'.join(texts[g][a-1:b])
  u={'source_id':id,'guide':g,'line_start':a,'line_end':b,'current_text_sha256':sha(t.encode()),'unchanged_text':t==old['text']}
  uses.append(u)
  if not u['unchanged_text']:changeduses.append({**u,'current_text':t,'prior_text_sha256':sha(old['text'].encode())})
assert len(uses)==423
# No source placement is dropped. Current Guide hash comes from the manifest, not frozen baseline field.
dump('current-source-uses.json',{'baseline':'../closeout-2026-11-03/effective-source-ledger.json','guide_hashes':'guide-manifest.json','mapping_rule':'Existing source-id/Guide/line span, current text fetched from current Guide and checked by current_text_sha256. Frozen old guide_sha256 is historical only.','uses':uses,'changed_text_uses':changeduses})
# Preserve all169original topic identities/atomic linkages without copying old paragraphs again.
topics=json.loads((OLD/'effective-topic-destinations.json').read_text());topicmap=[]
for r in topics:
 def cur(p):
  g=p['guide'];a=p['line_start'];b=p['line_end'];t='\n'.join(texts[g][a-1:b])
  return {'guide':g,'line_start':a,'line_end':b,'current_text_sha256':sha(t.encode())}
 item={'original_topic_id':r['id'],'original_snapshot':r['snapshot'],'original_snapshot_sha256':r['snapshot_sha256'],'current_destinations':[cur(p) for p in r['effective_destinations']]}
 if 'atomic_destinations' in r:item['atomic_destinations']=[{'original_bullet_index':i+1,'current_destinations':[cur(p) for p in atom['destinations']]} for i,atom in enumerate(r['atomic_destinations'])]
 topicmap.append(item)
assert len(topicmap)==169
dump('current-topic-links.json',{'original_blocks_and_dispositions':'../closeout-2026-11-03/effective-topic-destinations.json','mapping_rule':'Original169block identities, snapshot texts/hashes and per-bullet semantic dispositions preserved. Apply current source-condition repairs F01–F13 beside those links; no old topic dropped. Lines stay identical; only current Guide hashes/text identity change.','topics':topicmap})
# Compact current tables for the three affected Guides: frozen unchanged rows plus exact override deltas.
for g in ['om-income-tax','om-corporate-income-tax','oman-vat']:
 rr=[p for p in patches.values() if any(x['guide']==g for x in rows[p['id']]['placements'])]
 body=[f'# {g}: current focused ledger overlay','',f"Baseline independent review: `{BASE}`, FIX. Source overrides here repair onlyF01–F13; no independentPASS. Current GuideSHA256: `{sha(guides[g].read_bytes())}`.",'','Use the frozen per-Guide ledger for unchanged source content; replace exactly the listed source fields with `source-overrides.json`. Use `current-source-uses.json` for every current placement/hash, including unchanged source rows whose paragraph changed. Old169topic identity/atomic linkage is preserved by `current-topic-links.json`.','', '| Source | Finding | Current Guide spans | Current rule/condition override |','|---|---|---|---|']
 def e(s):return str(s).replace('|','\\|').replace('\n','<br>')
 for p in rr:
  spans=[str(x['line_start'])+'–'+str(x['line_end']) for x in rows[p['id']]['placements'] if x['guide']==g]
  body.append('| '+' | '.join(map(e,[p['id'],','.join(p['findings']),', '.join(spans),p['replaces_fields'].get('conditions','Source quotation/locator completed; operative condition unchanged.')]))+' |')
 body+=['','## Changed current paragraphs / rows','', '| Lines | Source IDs | Current exact text |','|---|---|---|']
 grouped={}
 for u in changeduses:
  if u['guide']==g:
   key=(u['line_start'],u['line_end']);grouped.setdefault(key,{'text':u['current_text'],'ids':[]})['ids'].append(u['source_id'])
 for (a,b),v in sorted(grouped.items()):body.append('| '+' | '.join(map(e,[f'{a}–{b}',','.join(v['ids']),v['text']]))+' |')
 body+=['','## Changed source quotations / controlling references','']
 for p in rr:
  body += [f"### {p['id']} ({','.join(p['findings'])})",'',f"Source: {p['source_identity']['official_url']}; {p['source_identity']['act']} art/section {p['source_identity']['article']}. Language: {p['source_identity']['source_language']}.",f"RawSHA256 `{p['source_identity']['raw_sha256']}`. Originalsource-read {p['source_read_on_preserved']}; excerptcontinuationcheck2026-11-03.",'']
  if 'quote' in p['replaces_fields']:body += ['> '+l if l else '>' for l in p['replaces_fields']['quote'].split('\n')]+['']
  else:body += ['Quotation unchanged: '+p['unchanged_quote_ref']+'.','']
 (OUT/f'{g}-ledger-overlay.md').write_text('\n'.join(x.rstrip() for x in body).rstrip()+'\n')
# Preserve all20writer files and every original independent-review artifact byte for byte.
preserved=[]
for folder in [OLD,REV]:
 for p in sorted(folder.rglob('*')):
  if not p.is_file():continue
  target=str(p.relative_to(ROOT));b=subprocess.check_output(['git','show','HEAD:'+target],cwd=ROOT)
  preserved.append({'path':target,'sha256':sha(p.read_bytes()),'matches_HEAD':b==p.read_bytes()})
assert all(x['matches_HEAD'] for x in preserved)
# The original20file writer freeze includes its self-excluding artifact manifest.
assert len([x for x in preserved if '/closeout-2026-11-03/' in x['path']])==20
protection=[]
for g,p in guides.items():
 old=subprocess.check_output(['git','show',BASE+':'+str(p.relative_to(ROOT))],cwd=ROOT).decode();now=p.read_text()
 fields=['review_status','trust_label','tier','license']
 samefields={k:re.search('^'+k+':.*$',old,re.M).group()==re.search('^'+k+':.*$',now,re.M).group() for k in fields}
 protection.append({'guide':g,'protected_fields_match':samefields,'cta_tail_identical':old.split('<!-- openaccountants-cta-block -->')[1]==now.split('<!-- openaccountants-cta-block -->')[1],'oa_check_blocks_identical':re.findall(r'```oa-check\n.*?```',old,re.S)==re.findall(r'```oa-check\n.*?```',now,re.S)})
assert all(all(x['protected_fields_match'].values()) and x['cta_tail_identical'] and x['oa_check_blocks_identical'] for x in protection)
dump('preservation-and-integrity.json',{'baseline_independent_review_candidate':BASE,'source_override_count':len(patches),'exact_finding_ids':[f['id'] for f in findings],'canonical_rows_total_preserved':169,'prior_review_pass_rows_preserved':149,'fixed_rows_for_focused_closure':17,'preparation_only_rows_unchanged':3,'all423source_uses_retained':len(uses)==423,'all169original_topic_links_retained':len(topicmap)==169,'frozen_writer20files_and_original_review_unchanged':preserved,'protected_fields_and_examples':protection})
print('Saved17source overrides,423current source uses,169originaltopic links,3affectedGuideledger tables. Frozenwriter20files+review unchanged.')
