from writer import *
from decimal import Decimal as D,ROUND_HALF_UP,ROUND_CEILING,ROUND_FLOOR
import datetime,importlib.util,sys
p=R/'skills/international/germany/de-payroll.md';s='de-payroll';d=O/'support'/s
checks=[]
def ck(k,a,b):assert a==b,(k,a,b);checks.append({'name':k,'actual':str(a),'expected':str(b)})
def floor(x):return D(x).to_integral_value(rounding=ROUND_FLOOR)
def ceil(x):return D(x).to_integral_value(rounding=ROUND_CEILING)
def money(x):return D(x).quantize(D('.01'),rounding=ROUND_HALF_UP)
def tariff(x):
 x=floor(x)
 if x<=12348:return D(0)
 if x<=17799:y=(x-12348)/10000;return floor((D('914.51')*y+1400)*y)
 if x<=69878:z=(x-17799)/10000;return floor((D('173.10')*z+2397)*z+D('1034.87'))
 if x<=277825:return floor(D('.42')*x-D('11135.63'))
 return floor(D('.45')*x-D('19470.38'))
def up56(x):return max(2*(tariff(x*D('1.25'))-tariff(x*D('.75'))),floor(x*D('.14')))
def v56(x):
 if x>34939:return up56(D(34939))+floor((min(x,D(222260))-34939)*D('.42'))+floor(max(x-222260,D(0))*D('.45'))
 z=up56(x)
 if x>14071:z=min(z,up56(D(14071))+floor((x-14071)*D('.42')))
 return z
def pap(y,cl,kv=D('2.9'),care=None,children=D(0),krv=0,alv=0):
 y=D(y);care=D('.018') if cl==2 else D('.024') if care is None else care
 rv=min(y,D(101400))*D('.093') if krv==0 else D(0);kp=min(y,D(69750))*(kv/200+D('.07')+care)
 vv=rv+kp
 if alv==0 and cl!=6:vv=max(vv,rv+min(D(1900),kp+min(y,D(101400))*D('.013')))
 vv=ceil(vv);z=floor(y-(D(1266) if cl!=6 else D(0))-(D(4260) if cl==2 else D(0))-vv)
 def tax(t):return 2*tariff(t/2) if cl==3 else v56(t) if cl in [5,6] else tariff(t)
 t=tax(z);jb=tax(z-children*(D(9756) if cl in [1,2,3] else D(4878)))
 return vv,z,t,jb
for y,expected in [(20000,[380,0,0,2234,2766]),(60000,[9389,8091,4822,15364,15895]),(100000,[23248,21634,15012,30157,30689])]:
 for cl,e in zip([1,2,3,5,6],expected):ck(f'actualPAPoriginaltable {y} class{cl}',pap(y,cl)[2],D(e))
v,z,t,j=pap(60000,1);ck('oa1VSP',v,D(12090));ck('oa1ZVE',z,D(46644));ck('oa1monthlytax',floor(t/12*100)/100,D('782.41'));ee=D(465)+65+D('437.5')+120;ck('oa1EE',ee,D('1087.50'));ck('oa1net',5000-floor(t/12*100)/100-ee,D('3130.09'))
v,z,t,j=pap(108000,3,D('2.5'),D('.0155'),D(2));ck('oa2VSP',v,D(16266));ck('oa2ZVE',z,D(90468));ck('oa2annual',t,D(17826));ck('oa2month',t/12,D('1485.50'));ck('oa2childbase',j,D(11626));ck('oa2church',j*D('.08'),D('930.08'));ck('oa2EE',money(D(8450)*D('.093'))+money(D(8450)*D('.013'))+money(D('5812.5')*D('.0855'))+money(D('5812.5')*D('.0155')),D('1482.76'));ck('oa2ERcare',money(D('5812.5')*D('.018')),D('104.63'))
for n,ee0,ees in [(0,'.024','.029'),(1,'.018','.023'),(2,'.0155','.0205'),(3,'.013','.018'),(4,'.0105','.0155'),(5,'.008','.013')]:
 r=D('.024') if n==0 else D('.018')-max(D(n-1),D(0))*D('.0025');ck(f'care{n}outside',r,D(ee0));ck(f'care{n}Saxony',r+D('.005'),D(ees))
ck('minimum603',ceil(D('13.9')*130/3),D(603));ck('old556',ceil(D('12.82')*130/3),D(556))
for name,r,e in [('health','.13','78.39'),('pension','.15','90.45'),('tax','.02','12.06'),('employee','.036','21.71')]:ck('minijob'+name,money(D(603)*D(r)),D(e))
F=D('.6619');G=D(603);AE=D(1000);bt=F*G+(2000/(2000-G)-G/(2000-G)*F)*(AE-G);be=2000/(2000-G)*(AE-G);ck('midijobtotalbase',money(bt),D('854.06'));ck('midijobEEbase',money(be),D('568.36'));ck('DE-B11childlesscorrect',money(bt*D('.006')),D('5.12'));ck('DE-B11wrongsecondbase',money(be*D('.006')),D('3.41'));ck('DE-B11difference',money(bt*D('.006'))-money(be*D('.006')),D('1.71'))
ck('DE-B10professionalKRV0VSP',pap(60000,1,krv=0)[0],D(12090));ck('DE-B10incorrectKRV1VSP',pap(60000,1,krv=1)[0],D(6510));ck('DE-B10taxseparator',pap(60000,1,krv=1)[2]-pap(60000,1,krv=0)[2],D(1948))
ck('AktivMayroom',D(2000)*8,D(16000));ck('Aktiv500taxed',D(2500)-2000,D(500));ck('oldbonus500exempt',min(D(800),D(2000)-1500),D(500));ck('oldbonus300taxed',D(800)-500,D(300));ck('lateTax',floor(D(1275)/50)*50*D('.01'),D('12.5'));ck('lateSV',floor(D(3480)/50)*50*D('.01'),D('34.5'));ck('10OctSat',datetime.date(2026,10,10).weekday(),5);ck('12OctMon',datetime.date(2026,10,12).weekday(),0);ck('2027Feb28Sunday',datetime.date(2027,2,28).weekday(),6);ck('2026Feb28Saturday',datetime.date(2026,2,28).weekday(),5)
# The age/fullpension/waiver cases directly separate own statutory branches, no mathematical pension-age determination assumed.
for full,waive,rvexpected in [(False,False,True),(True,False,False),(True,True,True)]:ck(f'B09 post-age full{full} waiver{waive}:RV',not full or waive,rvexpected)
used={k for r in json.loads((d/'rows.json').read_text()) for k in r['source_quote_ids']}
for k in used:
 q=Q[k];assert sha(q['raw_path'])==q['raw_sha256'];assert sha(q['reader_path'])==q['reader_sha256'];assert q['exact_quote'] in '\n'.join(lf(q['reader_path'])[q['native_LF'][0]-1:q['native_LF'][1]])
sys.path[:0]=[str(R/'scripts'),'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'];sp=importlib.util.spec_from_file_location('e',R/'scripts/check-examples.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);blocks,fail=m.check_file(str(p));assert blocks==2 and not fail
sp=importlib.util.spec_from_file_location('schema',R/'scripts/validate-guides.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);er=[];wa=[];m.check_guides(m.load_build_index(),er,wa,only_files={'skills/international/germany/de-payroll.md'});assert not er and not wa,(er,wa)
r=subprocess.run(['git','diff','--check','--','skills/international/germany/de-payroll.md'],cwd=R,text=True,capture_output=True);assert r.returncode==0,r.stdout+r.stderr
base=(O/'DE-B09-retirement-branch-distinction/de-payroll.before.md').read_text();cur=p.read_text();ops=[]
for folder in ['DE-B09-retirement-branch-distinction','DE-B10-professional-pension-VSP','DE-B11-transition-care-allocation']:ops+=json.loads((O/folder/'exact-operations.json').read_text())
z=base
for x in ops:assert z.count(x['before'])==1;z=z.replace(x['before'],x['after'])
assert z==cur
for x in reversed(ops):assert z.count(x['after'])==1;z=z.replace(x['after'],x['before'])
assert z==base
visual=[{'path':str(x),'sha256':sha(x),'actual_visual_read_on':DATE} for x in sorted((d/'PAP-visual').glob('page-*.png'))]
out={'Guide_sha256':sha(p),'ledger_sha256':sha(O/'ledgers'/f'{s}.md'),'fresh_controls':checks,'original_oa_blocks':blocks,'oa_failures':fail,'own_quote_hash_literal_checks':len(used),'all_three_corrections_exact_composition_and_inverse':True,'original_oa_URL_H2_CTA_preservation':'Each correction exactproof retained; complete inverse recovers original baseline.','schema_errors':er,'schema_warnings':wa,'scoped_diff':r.stdout+r.stderr,'visual_PAP_reads':visual,'precise_limits':['Saxony transition allocation is excluded from the generic half-rate worksheet; ordinary published F federalGazette notice itself unread; statechurchrateallocation/2027healthvalue/certificateSundaymove remain explicitcurrentGuide reservations.','BVV wrong /bvv route404 preserved; successful /beitrvv sources acquired/read separately.','Initial Reader helper lacked __file__; corrected only helper namespace, no raw or Guide change.'],'not_independent_review':True};(d/'writer-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(blocks,len(checks),len(used),sha(O/'ledgers'/f'{s}.md'))
