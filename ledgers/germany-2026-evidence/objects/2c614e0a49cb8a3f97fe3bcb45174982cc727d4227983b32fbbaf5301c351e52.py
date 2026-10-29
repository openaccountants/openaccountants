from writer import *
from decimal import Decimal as D,ROUND_FLOOR,ROUND_CEILING
import importlib.util,datetime
p=R/'skills/international/germany/de-einkommensteuer-freelancer.md';spec=importlib.util.spec_from_file_location('oa',R/'scripts/check-examples.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);blocks,fail=m.check_file(str(p));assert blocks==3 and not fail
Ck=[]
def ck(n,a,b):assert a==b,(n,a,b);Ck.append({'name':n,'actual':str(a),'expected':str(b)})
def floor(x):return D(x).to_integral_value(rounding=ROUND_FLOOR)
def tariff(v):
 x=floor(v)
 if x<=12348:t=D(0)
 elif x<=17799:
  y=(x-12348)/10000;t=(D('914.51')*y+1400)*y
 elif x<=69878:
  z=(x-17799)/10000;t=(D('173.10')*z+2397)*z+D('1034.87')
 elif x<=277825:t=D('.42')*x-D('11135.63')
 else:t=D('.45')*x-D('19470.38')
 return floor(t)
def soli(t,joint=False):return floor(max(D(0),min(D('.055')*t,D('.119')*(t-(40700 if joint else 20350))))*100)/100
ck('original translator day cost',min(D(150)*6,D(1260)),D(900));ck('translator profit',D(72000)-12000-900,D(59100));ck('translator taxable',D(59100)-9100,D(50000));ck('translator tax',tariff(50000),D(10548));ck('translator Soli',soli(tariff(50000)),D(0));ck('translator church9 stipulated',tariff(50000)*D('.09'),D('949.32'))
ck('consultant IAB',D(20000)*D('.5'),D(10000));ck('consultant profit',D(100000)-10000,D(90000));ck('consultant taxable',D(90000)-9700,D(80300));ck('consultant tax',tariff(80300),D(22590));ck('consultant fullSoli',D(22590)*D('.055'),D('1242.45'));ck('consultant Soli',soli(tariff(80300)),D('266.56'))
ck('trader tariff',tariff(100000),D(30864));mess=(D(110000)-24500)*D('.035');ck('trader Messbetrag',mess,D('2992.50'));gt=mess*4;credit=min(mess*4,D(30864),gt);ck('trader GT',gt,D(11970));ck('trader credit',credit,D(11970));ck('trader netIT',tariff(100000)-credit,D(18894));ck('trader Soli aftercredit',soli(tariff(100000)-credit),D(0));ck('trader church beforecredit',tariff(100000)*D('.09'),D('2777.76'));ck('joint original100k splitting',2*tariff(D(100000)/2),D(21096));ck('joint Soli',soli(D(21096),True),D(0));ck('original advance',D(10548)/4,D(2637));ck('original corrected KU chair eligible cost',D(952)/D('1.19'),D(800));ck('corrected KU expense',D(952),D(952));ck('fullcredit expense',D(952)-152,D(800));ck('fullcredit VAT',D(952)-800,D(152));ck('original late4startedmonths',4*max(D(2000)*D('.0025'),D(25)),D(100))
for x,v in [(12348,0),(12349,0),(17799,1034),(17800,1035),(69878,18250),(69879,18213),(277825,105550),(277826,105551)]:
 # Expected direct statute coefficients evaluated separately, not assumed continuity.
 if x==69878:v=18213
 ck('tariff boundary '+str(x),tariff(x),D(v))
ck('floor taxable cents',tariff(D('50000.99')),tariff(50000));ck('Soli exact20350',soli(D(20350)),D(0));ck('Soli20351 truncatedcent',soli(D(20351)),D('.11'));ck('Soli highfull',soli(D(40000)),D(2200));ck('daycap210',min(D(210)*6,D(1260)),D(1260));ck('daycap211',min(D(211)*6,D(1260)),D(1260));ck('miners raw',D(124800)*D('.247'),D('30825.600'));ck('miners ceil', (D(124800)*D('.247')).to_integral_value(rounding=ROUND_CEILING),D(30826));ck('jointpensioncap',2*D(30826),D(61652));ck('health sickpay reduction',D(1000)*D('.96'),D(960));ck('insurancebasic exceedcap',max(D(4000),D(2800)),D(4000));ck('lossCF2026 excess',D(1000000)+(D(1500000)-1000000)*D('.7'),D(1350000));ck('lossCF2028 excess',D(1000000)+(D(1500000)-1000000)*D('.6'),D(1300000));ck('credit tariffshare binding',min(D(4000),D(2000),D(5000)),D(2000));ck('credit actualGT binding',min(D(4000),D(7000),D(3000)),D(3000));ck('IAB testedprofit excludesoldaddback',D(204000)-5000,D(199000));ck('IAB eligible199k',D(199000)<=200000,True);ck('IAB200001 cliff',D(200001)<=200000,False);ck('IAB opencap separate',min(D(20000)*D('.5'),D(200000)-195000),D(5000));ck('IAB thirdyear2026',2026+3,2029);ck('prepay399 fails',D(399)>=400,False);ck('prepay400 passes',D(400)>=400,True);ck('2026selfSaturday',datetime.date(2027,7,31).weekday(),5);ck('2026adviserTuesday',datetime.date(2028,2,29).weekday(),1);ck('2025adviserSunday',datetime.date(2027,2,28).weekday(),6)
# Independently apply every exact root replacement to its retained input and reverse it.
bind=[]
for folder,expected in [('germany-root-DE-B03-L19-2026-10-29','c80a3678a2bd6edd3461fc56b35c09496980a857079c7386b259927f44764987'),('germany-root-DE-B04-2026-10-29','24b5037c53e61ddfe3fbabce6ec11fbd53cde225ff07c70abaa36587376f9e20')]:
 d=O.parent/folder;a=d/'de-einkommensteuer-freelancer.before.md';j=d/'de-einkommensteuer-freelancer.root-proof.json';z=json.loads(j.read_text());b=a.read_text();before=b
 for op in z['operations']:assert b.count(op['before'])==1;b=b.replace(op['before'],op['after'])
 assert hashlib.sha256(b.encode()).hexdigest()==expected
 for op in reversed(z['operations']):assert b.count(op['after'])==1;b=b.replace(op['after'],op['before'])
 assert b==before
 bind.append({'proof':str(j),'proof_sha256':sha(j),'before_sha256':sha(a),'reproduced_after_sha256':expected,'inverse_exact':True})
rows=json.loads((O/'support/de-einkommensteuer-freelancer/rows.json').read_text());used={k for r in rows for k in r['source_quote_ids']}
for k in used:
 q=Q[k];assert sha(q['raw_path'])==q['raw_sha256'];assert sha(q['reader_path'])==q['reader_sha256'];assert q['exact_quote'] in '\n'.join(lf(q['reader_path'])[q['native_LF'][0]-1:q['native_LF'][1]])
before=(O.parent/'germany-root-DE-B03-L19-2026-10-29/de-einkommensteuer-freelancer.before.md').read_text();after=p.read_text();oa=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S);assert oa(before)==oa(after)
oldurls=re.findall(r'https?://[^\s)>|]+',before);newurls=re.findall(r'https?://[^\s)>|]+',after);it=iter(newurls);assert all(any(x==u for x in it) for u in oldurls)
out={'Guide_sha256':sha(p),'ledger_sha256':sha(O/'ledgers/de-einkommensteuer-freelancer.md'),'row_count':len(rows),'literal_actual_quote_checks':len(used),'original_oa_blocks':blocks,'oa_failures':fail,'fresh_numeric_date_controls':Ck,'original_cases':{'1':'Translator original/current oa1 recomputed.','2':'Consultant original/current oa2 recomputed.','3':'Trader original/current oa3 recomputed.','4':'Joint100k splitting recomputed.','5':'10548/4prepayment recomputed.','6':'Old KU chair answer corrected DE-B04; original incorrect result preserved as history.','7':'Four startedmonths100 recomputed.'},'root_binding_proofs':bind,'original_oa_exact':True,'old_URL_order_preserved':True,'writer_only_not_independent':True,'retained_limits':['2026 ELSTER coordinate/name release not established;2025 names labelled.','Client state church-law rate/rounding not established by federal8/9booklet.','Underlying6April2023flatcostletter notread; actual2026EÜR instructions read.','Linked2010GWG ruling503 acquisition failure preserved; combined current own statutory reading is labelled, not express ruling.']};(O/'support/de-einkommensteuer-freelancer/writer-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(blocks,len(Ck),len(used),sha(O/'ledgers/de-einkommensteuer-freelancer.md'))
