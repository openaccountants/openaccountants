from pathlib import Path
import ast,re,json,hashlib,subprocess,collections
from decimal import Decimal,ROUND_FLOOR,ROUND_CEILING
import yaml
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/liechtenstein-pack-2026-10-30/repository')
O=R.parent/'followup-20261031/independent-review'
BASE='b41220632936e5c1a211254030b6acb659f6870a'
G='skills/international/liechtenstein/li-income-tax.md'
D=lambda x:Decimal(str(x))
def ev(expr,env):
 def go(n):
  if isinstance(n,ast.Constant):return D(n.value)
  if isinstance(n,ast.Name):return env[n.id]
  if isinstance(n,ast.UnaryOp):return -go(n.operand) if isinstance(n.op,ast.USub) else go(n.operand)
  if isinstance(n,ast.BinOp):
   a,b=go(n.left),go(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
  if isinstance(n,ast.Call):
   a=[go(x) for x in n.args]
   if n.func.id=='min':return min(a)
   if n.func.id=='max':return max(a)
   if n.func.id=='floor':return a[0].to_integral_value(rounding=ROUND_FLOOR)
   if n.func.id=='ceil':return a[0].to_integral_value(rounding=ROUND_CEILING)
  raise ValueError(ast.dump(n))
 return go(ast.parse(str(expr),mode='eval').body)
checks=[]
for p in [R/G,R/'ledgers/li-income-tax-evidence/valuation-20261031/valuation-controls.md']:
 t=p.read_text()
 for m in re.finditer(r'```oa-check\n(.*?)```',t,re.S):
  d=yaml.safe_load(m[1]);env={k:D(v) for k,v in d['inputs'].items()}
  steps=d['steps'] if isinstance(d['steps'],list) else [d['steps']]
  for step in steps:
   for k,e in step.items():env[k]=ev(e,env)
  outcomes={k:{'computed':str(env[k]),'expected':str(v),'difference':str(abs(env[k]-D(v))),'pass':abs(env[k]-D(v))<=D('.000001')} for k,v in d['expected'].items()}
  checks.append({'file':str(p.relative_to(R)),'line':t[:m.start()].count('\n')+1,'name':d['name'],'block_sha256':hashlib.sha256(m[1].encode()).hexdigest(),'expected':outcomes,'pass':all(x['pass']for x in outcomes.values())})
assert len(checks)==6 and all(x['pass'] for x in checks)
(O/'arithmetic.json').write_text(json.dumps({'method':'Reviewer-authored Decimal AST evaluation, independent of writer scripts and repository checker. Absolute tolerance 0.000001 CHF for displayed six-decimal repeating values. No workbook native recalculation.','executions':len(checks),'expected_fields':sum(len(x['expected'])for x in checks),'results':checks},indent=2))
def old(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=R,text=True)
prior=json.loads(old('ledgers/li-income-tax.writer.json'));now=json.loads((R/'ledgers/li-income-tax.writer.json').read_text())
a,b=old(G),(R/G).read_text()
prior_meta=yaml.safe_load(a.split('---')[1]);new_meta=yaml.safe_load(b.split('---')[1])
meta_diff={k:[prior_meta.get(k),new_meta.get(k)]for k in set(prior_meta)|set(new_meta) if prior_meta.get(k)!=new_meta.get(k)}
old_blocks=re.findall(r'```oa-check\n(.*?)```',a,re.S);new_blocks=re.findall(r'```oa-check\n(.*?)```',b,re.S)
def cta(t):return t[t.index('## Talk to an accountant'):]
# Exact source table rows preserve URLs and their read dates; changed gap prose is assessed manually.
source_a=a[a.index('## Sources'):];source_b=b[b.index('## Sources'):]
source_rows=[l for l in source_a.splitlines() if l.startswith('|')]
refs=re.findall(r'^\[([^\]]+)\]:\s*(\S+)',b,re.M);refmap=dict(refs)
used=re.findall(r'\]\[([^\]]+)\]',b)
continuity={'base':BASE,'original_rules':len(prior['rules']),'unchanged_original_rules':prior['rules']==now['rules'][:len(prior['rules'])], 'new_rules':len(now['rules'])-len(prior['rules']),'old_topic_objects':len(prior['old_topic_destinations']),'old_topic_objects_equal':prior['old_topic_destinations']==now['old_topic_destinations'],'explicit_successor_map_equal':prior['explicit_successor_map']==now['explicit_successor_map'],'old_two_examples_exact':old_blocks==new_blocks,'metadata_changes':meta_diff,'cta_exact':cta(a)==cta(b),'cta_extraction':cta(b),'source_table_rows_preserved':all(l in source_b for l in source_rows),'old_reference_urls_preserved':all(pair in refs for pair in re.findall(r'^\[([^\]]+)\]:\s*(\S+)',a,re.M)),'duplicate_reference_definitions':[k for k,n in collections.Counter(x[0]for x in refs).items()if n>1],'unresolved_references':sorted(set(used)-set(refmap))}
assert continuity['unchanged_original_rules'] and continuity['old_topic_objects_equal'] and continuity['old_two_examples_exact'] and continuity['source_table_rows_preserved'] and continuity['old_reference_urls_preserved']
assert not continuity['duplicate_reference_definitions'] and not continuity['unresolved_references']
(O/'continuity.json').write_text(json.dumps(continuity,indent=2,default=str))
print(json.dumps({'executions':len(checks),'expected_fields':sum(len(x['expected'])for x in checks),'arithmetic':'PASS','continuity':continuity},indent=2,default=str))
