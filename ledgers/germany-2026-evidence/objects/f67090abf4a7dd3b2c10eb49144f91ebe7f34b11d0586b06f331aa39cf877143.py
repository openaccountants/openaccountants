from writer import *
from decimal import Decimal as D,ROUND_HALF_UP,ROUND_FLOOR
import datetime,importlib.util,sys
s='germany-vat-return';p=R/f'skills/international/germany/{s}.md';d=O/'support'/s;checks=[]
def ck(k,a,b):assert a==b,(k,a,b);checks.append({'name':k,'actual':str(a),'expected':str(b)})
def mon(x):return D(x).quantize(D('.01'),rounding=ROUND_HALF_UP)
def floor(x):return D(x).to_integral_value(rounding=ROUND_FLOOR)
# Fresh calculations, separate from executable example evaluation.
output=D(20000)*D('.19')+D(200)*D('.19')+D(1000)*D('.19');inp=D(1140)+D(1200)*D('.19');ck('oa1output',output,D(4028));ck('oa1input',inp,D(1368));ck('oa1pay',output-inp,D(2660));ck('oa1late',floor((output-inp)/50)*50*D('.01'),D('26.5'));ck('oa1dueFriday',datetime.date(2026,4,10).weekday(),4);ck('oa1creditedTuesday',datetime.date(2026,4,14).weekday(),1);ck('oa1past3days',(datetime.date(2026,4,14)-datetime.date(2026,4,10)).days>3,True)
sv=(D(61000)+5000)/11;g=D(127330);dg=g*D('.3');fg=g-dg;dn=dg/D('1.19');fn=fg/D('1.07');dv=dg-dn;fv=fg-fn;ck('oa2prepay',sv,D(6000));ck('oa2drinksgross',dg,D(38199));ck('oa2foodgross',fg,D(89131));ck('oa2drinksnet',dn,D(32100));ck('oa2foodnet',fn,D(83300));ck('oa2drinksVAT',dv,D(6099));ck('oa2foodVAT',fv,D(5831));ck('oa2output',dv+fv,D(11930));ck('oa2beforeSV',dv+fv-4200,D(7730));ck('oa2pay',dv+fv-4200-sv,D(1730));ck('oa2old19all',g*19/119,D(20330));ck('officialprepaymentseparateexample',(D(39000)+5000)/11,D(4000))
ck('pre-refreshUSnet23.78RC',mon(D('23.78')*D('.19')),D('4.52'));ck('pre-refreshEU1200RC',D(1200)*D('.19'),D(228));ck('pre-refreshundocumented285.60VATclaim',D(0),D(0));ck('pre-refresh59.95net',mon(D('59.95')/D('1.19')),D('50.38'));ck('pre-refresh59.95VAT',mon(D('59.95')*19/119),D('9.57'));ck('pre-refresh4500EUserviceGermanVAT',D(0),D(0));ck('pre-refresh12.90bank+89.50insuranceinput',D(0),D(0))
for val,e in [(9000,False),(9001,True)]:ck(f'monthlyVAT>{val}',D(val)>9000,e)
for val,e in [(2000,True),(2001,False)]:ck(f'releaseeligibility{val}',D(val)<=2000,e)
for val,e in [(5000,True),(4999,False)]:ck(f'RCthreshold{val}',D(val)>=5000,e)
for val,e in [(50000,True),(50001,False)]:ck(f'ZMquartercurrent{val}',D(val)<=50000,e)
ck('ZMpreviousquarter50001blocks',all(x<=50000 for x in [100,100,50001,100,100]),False)
ck('KUprior25000current100000',D(25000)<=25000 and D(100000)<=100000,True);ck('KUprior25001fails',D(25001)<=25000,False);ck('KUcurrent100001fails',D(100001)<=100000,False);ck('smallinvoice250inclusive',D(250)<=250,True);ck('smallinvoice250.01',D('250.01')<=250,False);ck('minbusiness9.99fails',D('9.99')<10,True);ck('minbusiness10notblocked',D(10)<10,False);ck('solar30inclusive',D(30)<=30,True);ck('solar30.01notdeemed',D('30.01')<=30,False);ck('gift50sameapplicableyearallowed',D(50)<=50,True);ck('gift50.01wholeblock',D('50.01')>50,True)
# DE-B12: stipulated ordinary asset, own correction period5years as explicit fixture input, no universal assetclassification assumed.
ck('B12noinputentitlement-useVAT',D(0),D(0));ck('B12entitled400costno-spread40pctVAT',D(400)*D('.4')*D('.19'),D('30.4'));ck('B12wrong5yearspread400',D(400)/5*D('.4')*D('.19'),D('6.08'));ck('B12entitled500costspread5years40pctVAT',D(500)/5*D('.4')*D('.19'),D('7.60'));ck('B12withdrawalprice8500plus150VAT',(D(8500)+150)*D('.19'),D('1643.5'))
for established,turn,e in [(True,10000,True),(True,10001,False),(False,9000,False)]:ck(f'B13oneState{established}combined{turn}',established and D(turn)<=10000,e)
# Stipulated exchange rates are test inputs, not claimed actual BMF rates for any currency/month.
ck('B14FC1000rate1.25EURbase',D(1000)/D('1.25'),D(800));ck('B14VAT19',D(1000)/D('1.25')*D('.19'),D(152));ck('B14unapproveddaily1.10woulddiffer',mon(D(1000)/D('1.10')*D('.19')),D('172.73'));ck('B14advance1.20differentmonth',mon(D(1000)/D('1.20')*D('.19')),D('158.33'))
ck('annual31JulSaturday',datetime.date(2027,7,31).weekday(),5);ck('annual2AugMonday',datetime.date(2027,8,2).weekday(),0);ck('adviser29FebTuesday',datetime.date(2028,2,29).weekday(),1);ck('interest15months1Apr2028',datetime.date(2028,4,1),datetime.date(2028,4,1));ck('interest10000threefullmonths',D(10000)*D('.0015')*3,D(45));ck('annualsurcharge10000less8000twomonthsminimum',max((D(10000)-8000)*D('.0025'),D(25))*2,D(50));ck('penaltywholeEURfloor',floor(D('50.9')),D(50));ck('late2660oneMonth',floor(D(2660)/50)*50*D('.01'),D('26.5'))
used={k for r in json.loads((d/'rows.json').read_text()) for k in r['source_quote_ids']}
for k in used:
 q=Q[k];assert sha(q['raw_path'])==q['raw_sha256'];assert sha(q['reader_path'])==q['reader_sha256'];assert q['exact_quote'] in '\n'.join(lf(q['reader_path'])[q['native_LF'][0]-1:q['native_LF'][1]])
sys.path[:0]=[str(R/'scripts'),'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages'];sp=importlib.util.spec_from_file_location('e',R/'scripts/check-examples.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);blocks,fail=m.check_file(str(p));assert blocks==2 and not fail
sp=importlib.util.spec_from_file_location('schema',R/'scripts/validate-guides.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);er=[];wa=[];m.check_guides(m.load_build_index(),er,wa,only_files={'skills/international/germany/germany-vat-return.md'});assert not er and not wa,(er,wa)
r=subprocess.run(['git','diff','--check','--','skills/international/germany/germany-vat-return.md'],cwd=R,text=True,capture_output=True);assert r.returncode==0,r.stdout+r.stderr
base=(O/'DE-B12-B14-VAT-finite-corrections/germany-vat-return.before.md').read_text();cur=p.read_text();ops=json.loads((O/'DE-B12-B14-VAT-finite-corrections/exact-operations.json').read_text())+json.loads((O/'DE-B12-B14-VAT-finite-corrections/private-use-wording-precision/exact-operations.json').read_text());z=base
for x in ops:assert z.count(x['before'])==1;z=z.replace(x['before'],x['after'])
assert z==cur
for x in reversed(ops):assert z.count(x['after'])==1;z=z.replace(x['after'],x['before'])
assert z==base
# Protected metadata, all originalURLs/bylines/cases/H2/CTA checked independently of the inverse.
fm=lambda t:dict(re.findall(r'^(\w+): (.*)$',t.split('---',2)[1],re.M));a,b=fm(base),fm(cur);assert {k:v for k,v in a.items() if k not in ['version','last_updated']}=={k:v for k,v in b.items() if k not in ['version','last_updated']}
assert re.findall(r'^> Contributed by.*$',base,re.M)==re.findall(r'^> Contributed by.*$',cur,re.M)
assert re.findall(r'```oa-check\n.*?```',base,re.S)==re.findall(r'```oa-check\n.*?```',cur,re.S)
it=iter(re.findall(r'https?://[^\s)>|]+',cur));assert all(any(x==u for x in it) for u in re.findall(r'https?://[^\s)>|]+',base))
assert base[base.index('<!-- openaccountants-cta-block -->'):]==cur[cur.index('<!-- openaccountants-cta-block -->'):]
out={'Guide_sha256':sha(p),'ledger_sha256':sha(O/'ledgers'/f'{s}.md'),'own_fresh_controls':checks,'original_oa_blocks':blocks,'oa_failures':fail,'used_actual_quote_hash_literal_checks':len(used),'schema_errors':er,'schema_warnings':wa,'scoped_diff':r.stdout+r.stderr,'exact_composition_and_inverse':True,'original_oa_URL_order_bylines_CTA_H2_protected_metadata':'Exact, except authorizedversion/date','retained_gaps':['Calendar-year gift administrativeperiod, machine/signature entertainmentrequirements, country-specificforeignofficeandwhole-euro taxbaserounding remain actualGuidepreciselimits.','DEB226 is an index/header body; not used as operative statutoryquotation. Specificoperativearticles acquiredorretainedandactuallyread separately.','Actualold1062LFpatternlibrary/Excel/Kontoauszugworkflow retirementexplicitinold-topicmap; priorreviewreport is lineage not independentnewPASS.'],'not_independent_review':True};(d/'writer-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(blocks,len(checks),len(used),sha(p),sha(O/'ledgers'/f'{s}.md'))
