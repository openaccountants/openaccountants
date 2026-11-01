#!/usr/bin/env python3
from pathlib import Path
import ast, decimal, hashlib, json, os, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
BASE='a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297'; FREEZE='a61fda399fa613455862d3cc72d5c403cd330ccc'
sys.path.insert(0,str(ROOT/'scripts'))
from frontmatter_yaml import load_frontmatter
D=decimal.Decimal
def git(*a):return subprocess.run(['git',*a],cwd=ROOT,capture_output=True,check=True).stdout

def front(t):return load_frontmatter(t.split('---',2)[1])
def evaluate(expr,env):
 tree=ast.parse(str(expr),mode='eval')
 def ev(n):
  if isinstance(n,ast.Expression):return ev(n.body)
  if isinstance(n,ast.Constant):return D(ast.get_source_segment(str(expr),n))
  if isinstance(n,ast.Name):return env[n.id]
  if isinstance(n,ast.UnaryOp):return -ev(n.operand) if isinstance(n.op,ast.USub) else ev(n.operand)
  if isinstance(n,ast.BinOp):
   a,b=ev(n.left),ev(n.right)
   return {ast.Add:lambda:a+b,ast.Sub:lambda:a-b,ast.Mult:lambda:a*b,ast.Div:lambda:a/b}[type(n.op)]()
  if isinstance(n,ast.Call):return {'min':min,'max':max,'abs':abs}[n.func.id](*[ev(a) for a in n.args])
  raise ValueError(ast.dump(n))
 return ev(tree)
paths=sorted((ROOT/'skills/benin').glob('bj-*.md')); receipt={'pinned_base':BASE,'freeze':FREEZE,'actual_head':git('rev-parse','HEAD').decode().strip()}
manifest=json.loads((ROOT/'evidence/ledgers/benin-draft-20261101/candidate-hashes.json').read_text())
receipt['freeze_hashes']={rel:hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==x['sha256'] for rel,x in manifest['files'].items()}
receipt['freeze_preserved']=all(receipt['freeze_hashes'].values()) and receipt['actual_head']==FREEZE
platform={'review_status','license','authored_by','trust_label','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by','reviewed_on'}
receipt['guides']={}; receipt['examples']=[];maptext=(ROOT/'evidence/ledgers/benin-old-topics.md').read_text()
for p in paths:
 rel=str(p.relative_to(ROOT));text=p.read_text();meta=front(text);oldrun=subprocess.run(['git','show',f'{BASE}:{rel}'],cwd=ROOT,capture_output=True)
 info={'description_words':len(str(meta['description']).split()),'description_80_150':80<=len(str(meta['description']).split())<=150,'strict_types':type(meta['tax_year']) is int and type(meta['tier']) is int,'tax_year':meta['tax_year'],'tier':meta['tier'],'platform_keys':sorted(platform & set(meta))}
 if oldrun.returncode==0:
  old=oldrun.stdout.decode(); oldmeta=front(old); marker='<!-- openaccountants-cta-block -->'; topics=[x for x in old.split(marker)[0].splitlines() if x.startswith('#') or re.match(r'^- \*\*',x)]
  info.update(baseline_sha256=hashlib.sha256(oldrun.stdout).hexdigest(),baseline_bytes=len(oldrun.stdout),candidate_bytes=p.stat().st_size,cta_tail_byte_identical=old.split(marker,1)[1]==text.split(marker,1)[1],all_platform_and_human_fields_identical={k:meta.get(k)==oldmeta.get(k) for k in platform},baseline_topics=len(topics),all_topics_exactly_in_map=all(f'{p.name}: {t}' in maptext for t in topics),version_before=str(oldmeta.get('version')),version_now=str(meta.get('version')),date_before=str(oldmeta.get('last_updated')),date_now=str(meta.get('last_updated')))
 else:info['new_no_platform_keys']=not bool(platform & set(meta))
 receipt['guides'][p.name]=info
 for block in re.findall(r'```oa-check\n(.*?)\n```',text,re.S):
  data=load_frontmatter(block);env={k:D(str(v)) for k,v in data['inputs'].items()}
  for k,expr in data['steps'].items():env[k]=evaluate(expr,env)
  expected=data['expected'];results={k:{'independent_decimal':str(env[k]),'given_expected':str(v),'matches':abs(env[k]-D(str(v)))<=D('0.01')} for k,v in expected.items()}
  receipt['examples'].append({'guide':p.name,'name':data['name'],'results':results,'passed':all(v['matches'] for v in results.values())})
receipt['topic_map_rows']=sum(1 for l in maptext.splitlines() if l.startswith('| bj-'))
receipt['ledger_rows']={p.name:len(re.findall(r'^\| \d+ \|',p.read_text(),re.M)) for p in (ROOT/'evidence/ledgers').glob('bj-*.md')}
receipt['commands']=[]
commands=[['python3','scripts/skill_checks.py',*[str(p.relative_to(ROOT)) for p in paths]],['python3','scripts/check-examples.py','--require',*[str(p.relative_to(ROOT)) for p in paths]],['python3','evidence/ledgers/benin-draft-20261101/pinned-validation.py'],['git','diff','--check',BASE],['git','diff','--check','--cached']]
for cmd in commands:
 r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);receipt['commands'].append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(HERE/'mechanical-preservation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'freeze_preserved':receipt['freeze_preserved'],'descriptions':{k:v['description_words'] for k,v in receipt['guides'].items()},'examples':len(receipt['examples']),'all_example_results_match':all(e['passed'] for e in receipt['examples']),'topics':receipt['topic_map_rows'],'ledger_rows':sum(receipt['ledger_rows'].values()),'commands':[{'command':x['argv'][:2],'exit':x['exit_code']} for x in receipt['commands']]},indent=2))
