from pathlib import Path
import ast,re,json,hashlib,collections
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
import yaml
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/liechtenstein-pack-2026-10-30/repository')
W=R.parent/'review'
D=lambda x:Decimal(str(x))
def evaluate(s,env):
 def visit(n):
  if isinstance(n,ast.Constant):return D(n.value)
  if isinstance(n,ast.Name):return env[n.id]
  if isinstance(n,ast.UnaryOp):return -visit(n.operand) if isinstance(n.op,ast.USub) else visit(n.operand)
  if isinstance(n,ast.BinOp):
   a,b=visit(n.left),visit(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
   raise ValueError(ast.dump(n))
  if isinstance(n,ast.Call) and isinstance(n.func,ast.Name):
   args=[visit(a)for a in n.args]; f=n.func.id
   if f=='min':return min(args)
   if f=='max':return max(args)
   if f=='floor':return args[0].to_integral_value(rounding=ROUND_FLOOR)
   if f=='ceil':return args[0].to_integral_value(rounding=ROUND_CEILING)
   if f=='abs':return abs(args[0])
   if f=='round':return args[0].quantize(Decimal(1).scaleb(-int(args[1]) if len(args)>1 else 0))
  raise ValueError(ast.dump(n))
 return visit(ast.parse(str(s),mode='eval').body)
files=list((R/'skills/international/liechtenstein').glob('*.md'))+list((R/'ledgers').glob('li*-evidence/retained-original-controls.md'))
checks=[]
for p in files:
 for match in re.finditer(r'```oa-check\n(.*?)```',p.read_text(),re.S):
  block=match.group(1); data=yaml.safe_load(block); env={k:D(v)for k,v in data['inputs'].items()}
  for step in (data['steps'] if isinstance(data['steps'],list) else [data['steps']]):
   for key,expression in step.items():env[key]=evaluate(expression,env)
  result={key:{'computed':str(env[key]),'expected':str(value),'pass':abs(env[key]-D(value))<=Decimal('0.0000001')}for key,value in data['expected'].items()}
  checks.append({'file':str(p.relative_to(R)),'line':p.read_text()[:match.start()].count('\n')+1,'name':data['name'],'block_sha256':hashlib.sha256(block.encode()).hexdigest(),'checks':result,'pass':all(v['pass']for v in result.values())})
(W/'arithmetic-review.json').write_text(json.dumps({'method':'Independent Decimal AST evaluator authored for this review; no writer scripts or repository checker imported. Semantic and legal assumptions assessed separately in full-pack-review.md.','executions':len(checks),'distinct_exact_blocks':len(set(c['block_sha256']for c in checks)),'expected_fields':sum(len(c['checks'])for c in checks),'results':checks},indent=2))
print('independent arithmetic',len(checks),'executions',len(set(c['block_sha256']for c in checks)),'distinct',sum(len(c['checks'])for c in checks),'expected fields','failures',[c['name']for c in checks if not c['pass']])
# Full predecessor executable preservation, using preserved complete guides independently of maps.
preservation=[]
for p in (R/'ledgers').glob('li*-evidence/predecessor-guide.md'):
 oldblocks=re.findall(r'```oa-check\n(.*?)```',p.read_text(),re.S); current=R/'skills/international/liechtenstein'/(p.parent.name.removesuffix('-evidence')+'.md'); pool=current.read_text();annex=p.parent/'retained-original-controls.md'
 if annex.exists():pool+='\n'+annex.read_text()
 for b in oldblocks:preservation.append({'predecessor':str(p.relative_to(R)),'name':yaml.safe_load(b)['name'],'sha256':hashlib.sha256(b.encode()).hexdigest(),'exact_retained':('```oa-check\n'+b+'```')in pool})
(W/'predecessor-controls.json').write_text(json.dumps(preservation,indent=2));print('predecessor controls',len(preservation),'retained',sum(x['exact_retained']for x in preservation))
# Table values compare physical-source rows and current Guide rows, independently of writer ledger.
socialsrc=(R/'ledgers/li-payroll-social-evidence/sources/25-non-employed-table.txt').read_text()
def money(s):return D(s.replace("'",'').replace(',',''))
socialrows=[]
for line in socialsrc.splitlines():
 m=re.match(r'\s*(bis|ab)\s*([\d\x27.]+)\s+([\d\x27.]+)\s+([\d\x27.]+)\s+([\d\x27.]+)\s*$',line)
 if m:socialrows.append((m[1],money(m[2]),money(m[5])))
guide=(R/'skills/international/liechtenstein/li-payroll-social.md').read_text(); grows=[]
for line in guide.splitlines():
 m=re.match(r'\| (Up to|From) ([\d,]+) \| ([\d,.]+) \|',line)
 if m:grows.append(('bis'if m[1]=='Up to'else'ab',money(m[2]),money(m[3])))
assert socialrows==grows,(socialrows,grows)
# statutory article19 excerpt -> numerical tariff tuples
s=(R/'ledgers/li-payroll-social-evidence/sources/05.txt').read_text();s=s[s.index('                                   Art. 1945'):s.index('                                  Art. 2047')]
stat=[]
for line in s.splitlines():
 m=re.search(r'bis ([\d ]+) Franken \([^)]*\): 0',line)
 if m:stat.append((0,int(m[1].replace(' ','')),D(0),D(0)));continue
 m=re.search(r'von ([\d ]+) Franken bis ([\d ]+) Franken: ([\d,]+) · x - ([\d ]+)',line)
 if m:stat.append((int(m[1].replace(' ','')),int(m[2].replace(' ','')),D(m[3].replace(',','.')),D(m[4].replace(' ',''))));continue
 m=re.search(r'von ([\d ]+) Franken oder mehr: ([\d,]+) · x - ([\d ]+)',line)
 if m:stat.append((int(m[1].replace(' ','')),None,D(m[2].replace(',','.')),D(m[3].replace(' ',''))))
g=(R/'skills/international/liechtenstein/li-income-tax.md').read_text(); guide_tariffs=[]
for line in g.splitlines():
 m=re.match(r'\| Up to ([\d,]+) \| 0 \|',line)
 if m:guide_tariffs.append((0,int(m[1].replace(',','')),D(0),D(0)));continue
 m=re.match(r'\| ([\d,]+)–([\d,]+) \| ([\d.]+)% × x − ([\d,]+) \|',line)
 if m:guide_tariffs.append((int(m[1].replace(',','')),int(m[2].replace(',','')),D(m[3])/100,D(m[4].replace(',',''))));continue
 m=re.match(r'\| ([\d,]+) or more \| ([\d.]+)% × x − ([\d,]+) \|',line)
 if m:guide_tariffs.append((int(m[1].replace(',','')),None,D(m[2])/100,D(m[3].replace(',',''))))
assert stat==guide_tariffs,(stat,guide_tariffs)
assert len(stat)==27 and len(socialrows)==32
(W/'table-review.json').write_text(json.dumps({'non_employed':{'count':len(socialrows),'source_rows':socialrows,'guide_rows':grows,'pass':True},'personal_tariffs':{'count':len(stat),'statutory_rows':stat,'guide_rows':guide_tariffs,'pass':True}},indent=2,default=str));print('tables',len(socialrows),'nonemployed',len(stat),'personal tariff rows PASS')
