from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
from hashlib import sha256
from collections import Counter
import ast,re,json,difflib,yaml
P=Path(__file__).resolve().parent.parent; O=P/'fresh-independent'; UI=P.parent/'clm-joint-signed-allocation'
b=(P/'before-v1.3.md').read_text(); n=(P/'proposed-v1.4.md').read_text(); checks=[]
def check(name,v,detail=None):
 checks.append({'name':name,'pass':bool(v),'detail':detail}); assert v,name
h=lambda p:sha256(p.read_bytes()).hexdigest()
check('frozen candidate SHA',h(P/'proposed-v1.4.md')=='40b24c16565a99479623b8fda382d00467a31e19e91780f1e74dbe58c73f746e')
check('candidate bytes',(P/'proposed-v1.4.md').stat().st_size==470201)
bm=yaml.safe_load(b.split('---',2)[1]);nm=yaml.safe_load(n.split('---',2)[1]);check('protected metadata', {k:v for k,v in bm.items() if k!='version'}=={k:v for k,v in nm.items() if k!='version'})
check('version only metadata advance',str(bm['version'])=='1.3' and str(nm['version'])=='1.4')
blocks=lambda s:re.findall(r'```oa-check\n(.*?)```',s,re.S)
check('two complete oa blocks preserved',len(blocks(n))==2 and blocks(n)==blocks(b))
def ev(x,env):
 if isinstance(x,ast.Constant):return D(str(x.value))
 if isinstance(x,ast.Name):return env[x.id]
 if isinstance(x,ast.BinOp):
  a,c=ev(x.left,env),ev(x.right,env)
  return {ast.Add:lambda:a+c,ast.Sub:lambda:a-c,ast.Mult:lambda:a*c,ast.Div:lambda:a/c}[type(x.op)]()
 if isinstance(x,ast.Call):return {'min':min,'max':max,'abs':abs}[x.func.id](*[ev(z,env) for z in x.args])
 raise Exception(ast.dump(x))
oa=[]
for block in blocks(n):
 z=yaml.safe_load(block); env={k:D(str(v)) for k,v in z['inputs'].items()}
 for k,v in z['steps'].items():env[k]=ev(ast.parse(str(v),mode='eval').body,env)
 outcomes={k:{'actual':str(env[k]),'expected':str(v),'pass':env[k]==D(str(v))} for k,v in z['expected'].items()}
 check(z['name']+' independently recomputed',all(x['pass'] for x in outcomes.values()));oa.append({'name':z['name'],'results':outcomes})
head=lambda s:re.findall(r'^## .+$',s,re.M)
check('all headings preserved',head(b)==head(n))
url=lambda s:re.findall(r'https?://[^\s<>\)\]]+',s)
check('all old URL multiplicities',not(Counter(url(b))-Counter(url(n))),len(url(b)))
# Explicit subsequence test.
it=iter(url(n));check('old URLs in original order',all(any(x==u for x in it) for u in url(b)))
check('full CTA preserved',b[b.index('<!-- openaccountants-cta-block -->'):]==n[n.index('<!-- openaccountants-cta-block -->'):])
check('whole intake and examples sections preserved',b[b.index('## Two worked examples'):b.index('## Sources')]==n[n.index('## Two worked examples'):n.index('## Sources')])
ind=lambda s:s[s.index('**CLM individual signed-loss branch.**'):s.index('**CLM joint return') if '**CLM joint return' in s else s.index('**Precise remaining boundaries.**')]
check('entire individual CLM branch exact',ind(b)==ind(n))
ops=[{'tag':t,'old_start':i+1,'old_end':j,'new_start':k+1,'new_end':l,'old':b.splitlines(keepends=True)[i:j],'new':n.splitlines(keepends=True)[k:l]} for t,i,j,k,l in difflib.SequenceMatcher(None,b.splitlines(keepends=True),n.splitlines(keepends=True),autojunk=False).get_opcodes() if t!='equal']
# Own allowed-delta reconstruction, not writer's build script.
expected=b.replace('version: 1.3\n','version: 1.4\n',1)
newparas=n[n.index('**CLM joint return'):n.index('**Precise remaining boundaries.**')]
expected=expected.replace('**Precise remaining boundaries.**',newparas+'**Precise remaining boundaries.**',1)
for a,c in [('Apart from the individual CLM branch just identified,','Apart from the individual CLM branch and the separately supplied one-entitled-mover joint cap branch just identified,'),('Signed joint CLM claims and the other regions remain unconfirmed.','CLM joint claims outside that supplied one-entitled-mover positive-N-above-positive-G branch, including exact both-entitled signed aggregation and cent rounding, and the other regions remain unconfirmed.'),('Castilla-La Mancha signed joint relocation attribution and signed populations outside the supplied positive-numerator individual method','Castilla-La Mancha joint relocation attribution outside the supplied one-entitled-mover positive-N-above-positive-G cap branch, including both-entitled signed aggregation and exact cent rounding, and signed populations outside the supplied positive-numerator individual method')]:
 check('one exact boundary replacement: '+a[:40],expected.count(a)==1);expected=expected.replace(a,c,1)
newrows=''.join(x for x in n.splitlines(keepends=True) if x.startswith('| [LIRPF joint rules') or x.startswith('| [Official Renta2025 OPEN simulator]'))
lines=expected.splitlines(keepends=True);last=max(i for i,x in enumerate(lines) if x.startswith('|'));lines.insert(last+1,newrows);expected=''.join(lines)
check('all other baseline bytes unchanged',expected==n)
q=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
calc=[]
for label,gain,eligible,actual in [('J1',1000,20000,'289.75'),('J2',1000,11000,'265.61'),('J3',2000,11000,'325.55')]:
 G=D(20000)-D(9000)+D(gain);B=G-D(3400);QGC=(B-D(5550))*D('.095');QSC=D(1000)*D('.095');ratio=D(eligible)/G*QGC
 r={'case':label,'G':str(G),'B':str(B),'QGC':str(QGC),'QSC':str(QSC),'selected_N':str(eligible),'direct_ratio_raw':str(ratio),'direct_ratio_cents':str(q(ratio)),'actual_UI':actual}
 if label=='J1':check('one mover capped credit',min(D(500),QGC)==D(actual));check('savings remains95',QGC+QSC-D(actual)==D(95));check('incorrect aggregate J1 ratio',q(D(11000)/G*QGC)==D('265.60'))
 else:check(label+' unresolved cent mismatch',q(ratio)!=D(actual))
 calc.append(r)
check('84.62% times384.75 diagnostic',D('84.62')/100*D('384.75')==D('325.575450'))
check('diagnostic rounds325.58',q(D('84.62')/100*D('384.75'))==D('325.58'))
for name,amt in [('J1-joint-summary.ax.txt','289,75'),('J1-repeat-summary.ax.txt','289,75'),('J2-joint-summary.ax.txt','265,61'),('J3-joint-summary.ax.txt','325,55')]:check(name+' actual joint ANEXOB',bool(re.search('button '+re.escape(amt)+', ID: ANEXOB',(UI/name).read_text())))
check('repeat spouse no entitlement checkbox', '714 checkbox (settable, integer) Value: 0' in (UI/'J1-repeat-spouse-not-entitled.ax.txt').read_text())
check('both entitled spouse checked','1192 checkbox (settable, integer) Value: 1' in (UI/'J2-both-eligible-input.ax.txt').read_text())
ui_manifest=json.loads((UI/'ROOT-UI-MANIFEST.json').read_text());check('all original UI manifest assets rehashed',all(h(UI/z['path'])==z['sha256'] and (UI/z['path']).stat().st_size==z['bytes'] for z in ui_manifest['files']),len(ui_manifest['files']))
manifest=json.loads((P/'frozen-manifest.json').read_text());check('all writer frozen artifact hashes',all(h(P/z['path'])==z['sha256'] and (P/z['path']).stat().st_size==z['bytes'] for z in manifest['files']),len(manifest['files']))
r0=(P/'root-independent/README-before.md').read_text();r1=(P/'root-independent/README-proposed.md').read_text()
check('README exact proposed SHA',h(P/'root-independent/README-proposed.md')=='18f77758ef5a3beee9a72e8cedc96379e720cdd04e883f1fc3f9718d166f8fa6')
y0=yaml.safe_load(r0.split('---',2)[1]);y1=yaml.safe_load(r1.split('---',2)[1]);check('README all non-IT-IND fields preserved',{k:v for k,v in y0.items() if k!='partial'}=={k:v for k,v in y1.items() if k!='partial'} and {k:v for k,v in y0['partial'].items() if k!='IT-IND'}=={k:v for k,v in y1['partial'].items() if k!='IT-IND'})
check('README only one line changed',sum(1 for t,i,j,k,l in difflib.SequenceMatcher(None,r0.splitlines(),r1.splitlines()).get_opcodes() if t!='equal')==1)
check('README body exact',r0.split('---',2)[2]==r1.split('---',2)[2]);check('README retains partial same domains',set(y0['partial'])==set(y1['partial']))
for f,data in [('controls.json',checks),('oa-recomputed.json',oa),('signed-joint-recomputed.json',calc),('exact-diff-ledger.json',ops)]: (O/f).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'all_pass':all(x['pass'] for x in checks),'oa':len(oa),'changed_opcodes':len(ops)}))
