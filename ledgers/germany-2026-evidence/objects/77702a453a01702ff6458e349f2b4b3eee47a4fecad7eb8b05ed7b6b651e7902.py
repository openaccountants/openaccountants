from writer import *
from decimal import Decimal as D,ROUND_HALF_UP
import importlib.util,datetime
spec=importlib.util.spec_from_file_location('oa',R/'scripts/check-examples.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
p=R/'skills/international/germany/de-capital-gains.md';blocks,fail=m.check_file(str(p));assert blocks==4 and not fail,(blocks,fail)
checks=[]
def chk(k,actual,expected):
 assert actual==expected,(k,actual,expected);checks.append({'name':k,'actual':str(actual),'expected':str(expected)})
def money(x):return x.quantize(D('.01'),rounding=ROUND_HALF_UP)
chk('original1tax',(D(1500)+2500-1000)*D('.25'),D(750));chk('original1Soli',D(750)*D('.055'),D('41.25'));chk('original1total',D(750)*D('1.055'),D('791.25'))
t=money(D(3000)/D('4.08'));chk('original2tax',t,D('735.29'));chk('original2church',money(t*D('.08')),D('58.82'));chk('original2Soli',money(t*D('.055')),D('40.44'));chk('original2total',t+money(t*D('.08'))+money(t*D('.055')),D('834.55'));chk('original2sharecarry',D(2500)-2000,D(500))
chk('original3twoBankBeforeAllowance',D(5000)-3000,D(2000));chk('original4base2026',D(50000)*D('.7')*D('.032'),D(1120));chk('original4taxable',D(1120)*D('.7'),D(784));chk('original4base2025',D(50000)*D('.7')*D('.0253'),D('885.5'))
chk('original5gain900',D(10900)-10000,D(900));chk('original5gain1100',D(11100)-10000,D(1100));chk('Freigrenze999',D(999)<1000,True);chk('Freigrenze1000',D(1000)<1000,False)
chk('original6taxablegain',D(100000)*D('.6')-D(40000)*D('.6'),D(36000));chk('original6initialallowance',D(9060)*D('.02'),D('181.20'));chk('original6threshold',D(36100)*D('.02'),D(722));chk('original6remainingallowance',max(D('181.2')-max(D(36000)-722,D(0)),D(0)),D(0))
chk('old0.9%below',D('.009')<D('.01'),True);chk('old1%qualifies',D('.01')>=D('.01'),True);chk('propertyquota50notmore',D(50)>50,False);chk('propertyquota50.01',D('50.01')>50,True)
chk('2025deadline31Jul2026weekday',datetime.date(2026,7,31).weekday(),4);chk('2025adviser28FebSunday',datetime.date(2027,2,28).weekday(),6);chk('2025adviser1MarMonday',datetime.date(2027,3,1).weekday(),0);chk('2026deadline31JulSaturday',datetime.date(2027,7,31).weekday(),5);chk('2026deadline2AugMonday',datetime.date(2027,8,2).weekday(),0);chk('2026adviser29FebTuesday',datetime.date(2028,2,29).weekday(),1)
chk('supplementaryflatcombinedrate',D('.25')*D('1.055'),D('.26375'));chk('original7ownUseCalendarYears',len(set(range(2024,2027))),3) # stipulated Jan2024 through June2026 own-use spans sale year and two preceding calendar years
used={x for r in json.loads((O/'support/de-capital-gains/rows.json').read_text()) for x in r['source_quote_ids']};qchecks=0
for k in used:
 q=Q[k];assert sha(q['raw_path'])==q['raw_sha256'];assert sha(q['reader_path'])==q['reader_sha256'];assert q['exact_quote'] in '\n'.join(lf(q['reader_path'])[q['native_LF'][0]-1:q['native_LF'][1]]);qchecks+=1
out={'Guide_sha256':sha(p),'actual_oa_blocks':blocks,'oa_failures':fail,'fresh_arithmetic_date_controls':checks,'used_actual_source_quote_hash_literal_checks':qchecks,'no_Guide_write':True,'not_independent_review':True,'root_repaired_source_backed_findings':['DE-B01','DE-B02'],'pending_source_backed_Guide_findings':[]};(O/'support/de-capital-gains/writer-checks.json').write_text(json.dumps(out,indent=2)+'\n');print(blocks,'originalexamples;',len(checks),'controls;',qchecks,'actualquotes')
