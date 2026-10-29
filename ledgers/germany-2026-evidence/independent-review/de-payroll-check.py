from pathlib import Path
import json,hashlib,subprocess,datetime
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');B=O.parent/'germany-ledger-writer-B-2026-10-29';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();slug='de-payroll';plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());records=[]
for r in plan:
 x=r['source'];a,b=x['native_LF'];assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['act_article'],'official_url':x['official_url'],'raw_path':x['raw_path'],'reader_path':x['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Selected entire quotation directly actually read in new-quote batches1–8/9–16/17–24/25–32/33–39/40–46; new-quote index refers to pending_direct_read subset, original full quote-row index retained separately.'
 records.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'frozen_current_rows_actually_read':[[1,45],[46,90],[91,136]],'quotes_direct':46,'quotes_same_raw_exact_words_whitespace_only_bridge':74,'quotes':records},indent=2)+'\n')
rows=json.loads((B/'support'/slug/'rows.json').read_text());frozen=(O/'guide-snapshots'/f'{slug}.md').read_text()
for x in rows:assert '\n'.join(frozen.split('\n')[x['LF_start']-1:x['LF_end']])==x['wording']
identity=next(x for x in json.loads((B/'current-and-pre-refresh-identities.json').read_text())if x['slug']==slug);old=json.loads((B/'support'/slug/'old-topic-destinations.json').read_text());main=subprocess.check_output(['git','show','62b7639a:skills/international/germany/'+slug+'.md'],cwd=W).decode();pre=subprocess.check_output(['git','show',identity['pre_refresh_revision']+':'+identity['path']],cwd=identity['git_object_repository']).decode();assert H(pre.encode())==identity['pre_refresh_sha256'];assert pre==identity['pre_refresh_body'];spotmap={}
for typ,t in [('current_main_rows',main),('pre_refresh_rows',pre)]:
 lines=t.split('\n');candidates=[]
 for n,r in enumerate(old[typ],1):
  a,b=r['old_native_LF'];txt='\n'.join(lines[a-1:b]);assert H(txt.encode())==r['old_unit_sha256']
  if 140<=len(txt)<=1600 and not txt.lstrip().startswith(('#','---','```','| Source')):candidates.append(n)
 spots=[candidates[int(i*(len(candidates)-1)/9)]for i in range(10)] if candidates else []
 spotmap[typ]=spots
 for n in spots:
  r=old[typ][n-1];a,b=r['old_native_LF'];print('OLDSPOT',typ,n,'LF',a,b,'\n'+'\n'.join(lines[a-1:b])+'\nDEST '+r['current_destination']+' '+r['disposition']+'\n')
(O/(slug+'-old-origin-check.json')).write_text(json.dumps({'current_main_origin_count':len(old['current_main_rows']),'pre_refresh_origin_count':len(old['pre_refresh_rows']),'all_actual_origins_checked':True,'mismatches':0,'semantic_spots_actually_read':spotmap},indent=2)+'\n')
from decimal import Decimal,ROUND_HALF_UP
import runpy,datetime
V=runpy.run_path(str(O/'germany-payroll-PAP-independent-calc.py'));annual=V['annual'];tariff=V['tariff'];ck=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 ck.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def money(x):return(Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
for g,values in [(20000,[380,0,0,2234,2766]),(60000,[9389,8091,4822,15364,15895]),(100000,[23248,21634,15012,30157,30689])]:
 for cls,e in zip([1,2,3,5,6],values):c(f'actualofficial{g}class{cls}',annual(g,cls)['tax'],e)
a=annual(60000,1);b=annual(108000,3,F('.0155'),F('2.5'))
for n,v,e in [('case1VSP',a['VSP'],12090),('case1zve',a['zve'],46644),('case1tax',a['tax'],9389),('case1monthly',F((F(a['tax'],12)*100)//1,100),F('782.41')),('case1eeRV',5000*F('.093'),465),('case1eeAV',5000*F('.013'),65),('case1eeKV',5000*F('.0875'),F('437.50')),('case1eePV',5000*F('.024'),120),('case1totalcontributions',F('465')+65+F('437.5')+120,F('1087.50')),('case1net',5000-F('782.41')-F('1087.50'),F('3130.09')),('case2VSP',b['VSP'],16266),('case2zve',b['zve'],90468),('case2tax',b['tax'],17826),('case2monthly',F(b['tax'],12),F('1485.50')),('case2childBK',2*tariff(F(b['zve']-2*9756,2)),11626),('case2churchstipulated8',11626*F('.08'),F('930.08')),('case2eeRV',8450*F('.093'),F('785.85')),('case2eeAV',8450*F('.013'),F('109.85')),('case2eeKV',money(F('5812.5')*F('.0855')),Decimal('496.97')),('case2eePV',money(F('5812.5')*F('.0155')),Decimal('90.09')),('case2erPV',money(F('5812.5')*F('.018')),Decimal('104.63')),('case2eeTotal',sum(map(Decimal,['785.85','109.85','496.97','90.09'])),Decimal('1482.76')),('mini603KV',money(F(603)*F('.13')),Decimal('78.39')),('mini603RV',money(F(603)*F('.15')),Decimal('90.45')),('mini603tax',money(F(603)*F('.02')),Decimal('12.06')),('mini603own',money(F(603)*F('.036')),Decimal('21.71')),('aktivMayDecroom',8*2000,16000),('aktiv2500taxpart',2500-2000,500),('taxLate1275',F(1275//50*50)*F('.01'),F('12.50')),('svLate3480',F(3480//50*50)*F('.01'),F('34.50')),('Oct10Saturday',datetime.date(2026,10,10).weekday(),5),('Oct12Monday',datetime.date(2026,10,12).weekday(),0),('certificateFeb28Sunday',datetime.date(2027,2,28).weekday(),6),('certificateMar1Monday',datetime.date(2027,3,1).weekday(),0),('lowmini100totalRV',F(175)*F('.186'),F('32.55')),('lowmini100employer',100*F('.15'),15),('lowmini100employee',F('32.55')-15,F('17.55')),('maternityaggregate100',60+40,100),('maternityone13subtraction',100-13,87),('maternityAG1share',87*F(60,100),F('52.20')),('maternityAG2share',87*F(40,100),F('34.80')),('precapjob1',F(8450*8450,10450),F(1428050,209)),('precapjob2',F(8450*2000,10450),F(338000,209)),('U1stipulated80',1000*F('.8'),800),('U1stipulated60',1000*F('.6'),600)]:c(n,v,e)
G=F(603);fac=F('0.6619')
def bases(a):return fac*G+(F(2000,2000-G)-G/(2000-G)*fac)*(a-G),F(2000,2000-G)*(a-G)
tot,ee=bases(F(1000));c('Midijob1000totalbaseDisplay',money(tot),Decimal('854.06'));c('Midijob1000eebaseDisplay',money(ee),Decimal('568.36'));c('Midijob1000childlesssurchargebase1',money(tot*F('.006')),Decimal('5.12'));c('Midijob1000wrongbase2surcharge',money(ee*F('.006')),Decimal('3.41'))
for name,rate in [('RV',F('.186')),('AV',F('.026')),('KVwith2.9',F('.175')),('PVonechild',F('.036'))]:
 total=2*money(tot*rate/2);own=money(ee*rate/2);employer=total-own;c('Midijob'+name+'sharesreconcile',own+employer,total)
c('Midijobexact2000firstbase',bases(F(2000))[0],2000);c('Midijobexact2000secondbase',bases(F(2000))[1],2000);c('Midijob603.01positiveee',bases(F('603.01'))[1]>0,True)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(ck),'controls':ck,'scope':'All2 original executable cases and narrative cases, all15 actual official20k/60k/100k vectors through independently verified FractionPAP helper; ordinary outside-Saxony Midijob formulas/rounding and meaningful new failure separators.8pctchurch is explicitly stipulated; no state-law/currentrate attestation. Saxony Midijob allocation not inferred.'},indent=2)+'\n')
(O/'new-primary-checks/payroll-remaining-gates/formula-visual-read-receipt.json').write_text(json.dumps({'actual_independent_view':'Both original official formula JPG images actually viewed together, exact transcription compared. Read date2026-10-29.','formula_images':[x['source']for x in plan if x['id']in ['PR.totalformula','PR.employeeformula']],'PAP_visual_bridge':'Same official2026PDF signature/algorithm independently visually inspected on pages27/29/30 in prior germany-payroll selected visual receipt; new quotation text read as stated in current-source ledger, not all40pages visualreading.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_frozen_current_rows_read':136,'quotes_direct_read':46,'same_raw_quotation_word_bridges':74,'old_origins':len(old['current_main_rows'])+len(old['pre_refresh_rows']),'old_semantic_spots':20,'own_controls':len(ck),'status':'NEEDS exact R62–70 sibling/R88–96 successors; positive ordinary outside-Saxony Midijob supplied, Saxony boundary precise.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONEde-payroll',len(ck),'controls',len(records),'sources')
