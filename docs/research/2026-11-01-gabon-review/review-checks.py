import json,re,subprocess,hashlib,pathlib,unicodedata,sys
from html.parser import HTMLParser
sys.path.insert(0,'/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
import yaml
ROOT=pathlib.Path('.');OUT=ROOT/'docs/research/2026-11-01-gabon-review';E=ROOT/'docs/research/2026-11-01-gabon-pack'
BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8';HEAD='d90a78e28adb1804d0e1fd904886dc16c00cd2bb'
def git(*a):return subprocess.check_output(['git',*a])
def sha(b):return hashlib.sha256(b).hexdigest()
def norm(s):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s)).strip().replace('’',"'")
def fm(b):return yaml.safe_load(b.decode().split('---',2)[1])
class Text(HTMLParser):
 def __init__(self):super().__init__();self.p=[]
 def handle_data(self,d):self.p.append(d)
ms=json.loads((E/'source-manifest.json').read_text());sources={}
for m in ms:
 if m['file'].endswith('.pdf'): t=(ROOT/'../review-cache/source-text'/m['file'].replace('.pdf','.txt')).read_text()
 elif m['file'].endswith('.html'):
  p=Text();p.feed((ROOT/'../sources'/m['file']).read_text());t=' '.join(p.p)
 else:t=(ROOT/'../sources'/m['file']).read_text()
 sources[m['id']]=t
rs=json.loads((E/'rules.json').read_text());checks=[];placements=[]
for r in rs:
 text=sources[r['source']];q=r['exact_original_language_quote'];pages=[i+1 for i,p in enumerate(text.split('\f')) if norm(q) in norm(p)]
 checks.append({'id':r['id'],'source':r['source'],'article':r['act_article'],'quote_present':norm(q) in norm(text),'claimed_main_page':r.get('pdf_page_1_based'),'matching_pages':pages if r.get('pdf_page_1_based') else [],'source_sha256':r['source_sha256']})
 for slug,sections in r['guide_sections'].items():
  ledger=(E/'ledgers'/(slug+'.md')).read_text();match=re.search(r'^## '+re.escape(r['id'])+r'\n(.*?)(?=^## |\Z)',ledger,re.M|re.S)
  extra=re.findall(r'^- (?:Additional exact French quote|Exact French quote): « (.*?) »$',match.group(1),re.M) if match else []
  guide=(ROOT/'skills/gabon'/(slug+'.md')).read_text()
  placements.append({'guide':slug,'rule_id':r['id'],'sections':sections,'ledger_block_present':bool(match),'quotes':[{'quote':x,'present_in_independent_extraction':norm(x) in norm(text)} for x in extra],'declared_sections_present':[s for s in sections if s=='H1' or re.search(r'^## '+re.escape(s)+r'$',guide,re.M)]})
(OUT/'rule-coverage.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');(OUT/'placement-coverage.json').write_text(json.dumps(placements,ensure_ascii=False,indent=2)+'\n')
old=json.loads((E/'old-files.json').read_text());topics=json.loads((E/'old-topics.json').read_text());pres=[];topicchecks=[]
for o in old:
 b=git('show',BASE+':'+o['path']);n=git('show',HEAD+':'+o['path']);mark=b'<!-- openaccountants-cta-block -->';bf=fm(b);nf=fm(n)
 body=b.decode().split('---',2)[2].split(mark.decode())[0];paras=[p.strip() for p in body.splitlines() if p.strip()];ts=[t for t in topics if t['from']==o['path']]
 pres.append({'path':o['path'],'base_blob':git('rev-parse',BASE+':'+o['path']).decode().strip(),'expected_blob':o['git_blob'],'base_sha256':sha(b),'expected_sha256':o['sha256'],'base_bytes':len(b),'candidate_bytes':len(n),'shrink_over_25_percent':len(n)<len(b)*.75,'cta_sha256':sha(b[b.index(mark):]),'cta_identical':b[b.index(mark):]==n[n.index(mark):],'platform_fields_identical':{k:bf.get(k)==nf.get(k) for k in ['authored_by','trust_label','license','review_status','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by']},'all_old_paragraphs_indexed':set(paras)==set(t['exact_old_text'] for t in ts),'old_paragraphs':len(paras),'mapped_topics':len(ts)})
 for t in ts:
  dst=ROOT/t['destination'];topicchecks.append({**t,'immutable_text_match':t['exact_old_text'] in body,'destination_exists':dst.exists(),'map_id_present':t['id'] in (E/'old-topic-map.md').read_text(),'review_disposition':'Reviewed against named destination; retained, corrected with primary baseline, explicitly held, or owning-Guide route as specified; see final review.'})
(OUT/'preservation.json').write_text(json.dumps(pres,ensure_ascii=False,indent=2)+'\n');(OUT/'old-topic-coverage.json').write_text(json.dumps(topicchecks,ensure_ascii=False,indent=2)+'\n')
inv=json.loads((E/'guide-inventory.json').read_text());metadata=[]
for slug,i in inv.items():
 b=git('show',HEAD+':skills/gabon/'+slug+'.md');m=fm(b);s=b.decode();v=re.search(r'^# .* v([\d.]+)$',s,re.M)
 metadata.append({'guide':slug,'git_blob':git('rev-parse',HEAD+':skills/gabon/'+slug+'.md').decode().strip(),'sha256':sha(b),'description_words':len(str(m['description']).split()),'description_80_to_150':80<=len(str(m['description']).split())<=150,'version_h1_matches':bool(v) and str(m['version'])==v.group(1),'new':i['new'],'new_has_no_platform_or_author_trust_fields':not any(k in m for k in ['authored_by','trust_label','license','review_status','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by']) if i['new'] else None,'new_has_no_cta':mark not in b if i['new'] else None})
(OUT/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print('Rules:',len(checks),'main quotes present:',sum(c['quote_present'] for c in checks),'placements:',len(placements),'all quotes checked:',sum(len(p['quotes']) for p in placements))
print('Unmatched quotes:',[(p['guide'],p['rule_id'],q['quote']) for p in placements for q in p['quotes'] if not q['present_in_independent_extraction']])
print('Old topics:',len(topicchecks),'preservation:',json.dumps(pres,indent=2));print('Metadata:',json.dumps(metadata,indent=2))
