#!/usr/bin/env python3
"""Read-only reproduction of the review's committed-byte and source checks."""
from pathlib import Path
import collections,hashlib,html.parser,json,os,re,subprocess,sys,xml.etree.ElementTree as E,zipfile
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
EV=OUT.parent
BASE='46c01152da0fdd1b722f61190c88413d0a195d02'
HEAD='0bce9f9c7ed1776eab90ae912096a03a6d7dba12'
INITIAL='5e157a7f7f361b8fa6c714496cb6deb1a7fc0742'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(rev,path):return git('show',rev+':'+path)
def norm(t):return re.sub(r'\s+',' ',t).strip()
class Parser(html.parser.HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.ignore=0
 def handle_starttag(self,t,a):
  if t in ('script','style'):self.ignore+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.ignore=max(self.ignore-1,0)
 def handle_data(self,t):
  if not self.ignore and t.strip():self.text.append(t.strip())
def extract(path):
 if path.suffix=='.html':
  p=Parser();p.feed(path.read_text());return '\n'.join(p.text)
 if path.suffix=='.docx':
  x=E.fromstring(zipfile.ZipFile(path).read('word/document.xml'));return '\n'.join(''.join(n.itertext()) for n in x.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
 if path.suffix=='.pdf':
  z=subprocess.run(['pdftotext','-layout',str(path),'-'],capture_output=True,text=True);return z.stdout if z.returncode==0 else None
 return path.read_text()
r={'base':BASE,'candidate':HEAD,'initial':INITIAL,'actual_merge_base':git('merge-base','origin/main',HEAD).decode().strip(),'files':{},'sources':{},'preservation':{},'old_topics':{}}
for path in sorted((ROOT/'skills/bahrain').glob('*.md')):
 rel=str(path.relative_to(ROOT));a=blob(BASE,rel);b=blob(INITIAL,rel);c=blob(HEAD,rel)
 info={'sha256':sha(c),'git_blob':git('rev-parse',HEAD+':'+rel).decode().strip(),'working_tree_matches_candidate':c==path.read_bytes(),'same_as_base':c==a,'same_as_initial':c==b}
 if path.name.startswith('bh-') and c!=a:
  marker=b'<!-- openaccountants-cta-block -->';info['cta_suffix_equals_base']=c[c.index(marker):]==a[a.index(marker):];info['cta_suffix_equals_initial']=c[c.index(marker):]==b[b.index(marker):]
  keys=['review_status','trust_label','license','authored_by','drafted_by','approved_by','validation_status','validated']
  field=lambda text,k:re.search(rb'^'+k.encode()+rb':.*$',text,re.M)
  info['platform_fields_equal_base']=all((field(a,k).group() if field(a,k) else None)==(field(c,k).group() if field(c,k) else None) for k in keys)
  info['baseline_bytes']=len(a);info['candidate_bytes']=len(c);info['shrink_fraction']=1-len(c)/len(a)
 r['files'][rel]=info
rows=json.loads((EV/'claim-rows.json').read_text())
for name,s in json.loads((EV/'source-identities.json').read_text()).items():
 p=ROOT/s['file'] if s['file'].startswith('../') else EV/s['file'];rd=ROOT/s['reader'] if s['reader'].startswith('../') else EV/s['reader'];text=extract(p)
 r['sources'][name]={'original_sha256':sha(p.read_bytes()),'matches_recorded_original':sha(p.read_bytes())==s['sha256'],'reader_matches_recorded':sha(rd.read_bytes())==s['reader_sha256'],'independent_extraction_equals_reader':text==rd.read_text(),'quoted_rows':[x['id'] for x in rows if x['source']==name],'quotes_present':all(norm(x['quote_original_language']) in norm(text or '') for x in rows if x['source']==name)}
old=json.loads((EV/'old-topics.json').read_text());bad=[];false=[];missing={};counts=collections.Counter();cache={}
for x in old:
 slug,period,_=x['id'].split('/');key=(slug,period)
 if key not in cache:cache[key]=blob(BASE if period=='baseline' else INITIAL,'skills/bahrain/'+slug+'.md').decode()
 lines=cache[key].splitlines();ix=x['original_line']-1
 if '\n'.join(lines[ix:ix+len(x['original_text'].splitlines())])!=x['original_text'] or sha(x['original_text'].encode())!=x['sha256']:bad.append(x['id'])
 counts[key]+=1
 if x['disposition'].startswith('Retained verbatim') and x['original_text'] not in blob(HEAD,'skills/bahrain/'+slug+'.md').decode():false.append(x['id'])
for key,raw in cache.items():
 slug,period=key;lines=raw.splitlines();covered=set()
 for x in old:
  if x['id'].startswith(slug+'/'+period+'/'):covered.update(range(x['original_line'],x['original_line']+len(x['original_text'].splitlines())))
 start=next(i for i,t in enumerate(lines[1:],1) if t=='---')+1;end=next((i for i,t in enumerate(lines) if t=='<!-- openaccountants-cta-block -->'),len(lines));missing['/'.join(key)]=[i+1 for i in range(start,end) if lines[i].strip() and i+1 not in covered]
 snapshot=EV/period/(slug+'.md');r['preservation']['/'.join(key)]={'snapshot_equals_git':snapshot.read_bytes()==raw.encode(),'nonempty_body_lines_unmapped':missing['/'.join(key)]}
r['old_topics']={'count':len(old),'counts_by_snapshot':{'/'.join(k):v for k,v in counts.items()},'row_location_or_hash_failures':bad,'false_retained_verbatim':false,'all_body_lines_covered':not any(missing.values())}
(OUT/'byte-source-preservation-audit.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':HEAD,'files':len(r['files']),'source_records':len(r['sources']),'grouped_claims':len(rows),'old_blocks':len(old),'source_failures':[k for k,v in r['sources'].items() if not all([v['matches_recorded_original'],v['reader_matches_recorded'],v['independent_extraction_equals_reader'],v['quotes_present']])],'oldtopic_failures':bad,'false_retained':false},indent=2))
