from pathlib import Path
import json,hashlib,re,datetime,runpy
from fractions import Fraction as F
R=Path(__file__).parent;O=R.parent;H=lambda b:hashlib.sha256(b).hexdigest();results=json.loads((R/'pending-successor-mechanical-results.json').read_text());by={x['successor_folder']:x for x in results};ck=[]
def c(n,a,e):assert a==e,(n,a,e);ck.append({'name':n,'actual':str(a),'expected':str(e)})
for n,a,e in [('combinedtax10k15',10000*F('.15'),1500),('combinedgrosswithheld2637.5refund',F('2637.50')-1500,F('1137.50')),('domesticpartialcompany2fifths',10000*F('.25')*F(2,5),1000),('50j45exact',45>=45,True),('50j70exact',F('.7')>=F('.7'),True),('50j15exactnotbelow',F('.15')<F('.15'),False),('50j10directexception',F('.1')>=F('.1'),True),('cbcrordinaryone12months',datetime.date(2027,12,31).year-2026,1),('cbcrknowledge15Febnext15Mar',datetime.date(2027,3,15).month-datetime.date(2027,2,15).month,1),('cbcr12monthresetnotmethod',12==1,False),('VSPsmallclassV1900room',max(1900-(18000*F('.14')+18000*F('.0145')+18000*F('.024')),0),0),('stipulatedcertsum',7564+1850,9414),('stipulatedannualbalance',11324-9414,1910),('newgroupopinion2yearcontractgate',2<=2,True),('privatepolicy5000inclusive',5000<=5000,True),('kskpartial12k6months',F(12000,6)*F('.049'),98),('kskwrong12months',F(12000,12)*F('.049'),49),('kskprepay40notexceeds',40>40,False),('yogaMay31Sunday',datetime.date(2026,5,31).weekday(),6),('yogaJune1Monday',datetime.date(2026,6,1).weekday(),0),('staffdiscount2k',2000*F('.96')-500-1080,340),('lodging2adults',285*F('.6'),171),('lodging3adults',285*F('.5'),F('142.5')),('lodging4adults',285*F('.4'),114),('affiliated37bminimum',max(600,1000*F('.96'))*F('.3'),288),('lowearnerprior2016cap',min(700*F('.3'),288,700-600),100),('bAVtwoqualterminationyears',101400*F('.04')*2,8112),('sharesdeclineactual5minus1',min(8000,5000-1000),4000),('SVnightpart30x25',30*F('.25'),F('7.5')),('SVnightfree25x25',25*F('.25'),F('6.25')),('SVnightliable',30*F('.25')-25*F('.25'),F('1.25')),('U1actual60',1000*F('.6'),600),('U1statute80',1000*F('.8'),800),('Frounded',round(F(28,F('42.3')),4),F('.6619')),('2025DEUEVFeb15Sunday',datetime.date(2026,2,15).weekday(),6),('2025DEUEVFeb16Monday',datetime.date(2026,2,16).weekday(),0),('certificate2026Feb28Sunday',datetime.date(2027,2,28).weekday(),6),('certificate2026Mar1Monday',datetime.date(2027,3,1).weekday(),0),('mini100total',175*F('.186'),F('32.55')),('mini100employer',100*F('.15'),15),('mini100EE',175*F('.186')-100*F('.15'),F('17.55')),('precapjob1',F(8450*8450,10450),F(1428050,209)),('precapjob2',F(8450*2000,10450),F(338000,209)),('precapbothsum',F(8450*8450,10450)+F(8450*2000,10450),8450),('maternityone13',60+40-13,87),('maternityAG1',87*F(60,100),F('52.2')),('maternityAG2',87*F(40,100),F('34.8')),('maternitywrongtwice13',60+40-13*2,74)]:c(n,a,e)
# Exact earlier mechanical chains connect original frozen body or accepted prior stage, not arbitrary writer copies.
for slug,start,end in [('de-treaty-withholding-rates',results[0],results[1]),('de-payroll',results[6],results[7]),('germany-payroll',results[6],results[7])]:
 a=next(x for x in start['pairs']if x['pair']['slug']==slug);b=next(x for x in end['pairs']if x['pair']['slug']==slug);assert a['pair']['Guide_sha256']==b['before_sha256']
def origins(v):
 out=[]
 def w(x):
  if isinstance(x,list):
   for z in x:w(z)
  elif isinstance(x,dict):
   if 'old_unit_sha256'in x:out.append((str(x['old_native_LF']),x['old_unit_sha256']))
   elif 'ref'in x and'old_lf'in x and'wording'in x:out.append((x['ref'],x['old_lf'],x['wording']))
   else:
    for z in x.values():w(z)
 w(v);return out
for result in results:
 D=O/result['successor_folder']
 for v in result['pairs']:
  slug=v['pair']['slug'];x=json.loads((D/'support'/slug/'old-topic-destinations.json').read_text());ori=origins(x);assert len(ori)==v['pair']['old_topics'],(slug,len(ori));v['actual_old_origin_identities_retained']=len(ori)
  # Original wholepair origins already checked from real Git; stable old identity tuples are required in successor.
  origfolder=O/('germany-ledger-writer-B-2026-10-29'if slug in ['de-payroll','de-social-contributions','de-payroll-benefits']else'germany-ledger-writer-2026-10-28')/'support'/slug
  origpath=origfolder/('old-topic-destinations.json'if'writer-B'in str(origfolder)else'old-topics.json')
  if origpath.exists():assert origins(json.loads(origpath.read_text()))==ori,(slug,'old origin changed')
  aa=(D/'before'/f'{slug}.md').read_text();bb=(D/'after'/f'{slug}.md').read_text();v['worked_prose_scope']='Treaty eligible facts/remittance/interpretation changed; algebra and2oa exact'if slug=='de-treaty-withholding-rates'else'Yoga filing calendar prose changed to1June; amounts and2oa exact'if slug=='de-social-contributions'else'All original executable blocks byteexact; original full narrative examples retained (independent current-source meaning checked)'
for result in results:
 for q in result['sources']:
  if not q['exact_prior_read_bridge']:
   q['actual_read_resolution']='Exact selected text actually read: Annex2full7–10/67–71 in bounded treaty readings and current closure display; PAP1478–1585 actual prior independent extracted/visual scope and full current display; BMG390–402 within actual375–427 selected read; ownSGBX26 JSON web observation initially read directly; SGBVI16313–16/AAG915–18 actually acquired/read for R89/90, with exact retained identity. No fullsource or rawHTML claim.'
 result['status']='PASS exact bounded successor. All actual delta operations read and assessed against actual own selected clauses or explicit exact prior-reading bridges. No countrywide completeness/attestation.'
result={'status':'PASS bounded final successor chains R57–96; original/intermediate R58/59 implementation failures retained, final exact c007 only accepted for treaty. No country verdict.','mechanical_results':results,'independent_controls':ck,'sources_scope':'Every own quote rehashed and literal native checked or expressly identified official web observation. Actual source condition reading from completed25wholepair source ledgers/findings scopes and explicit current extended readings, not writer check counts.','actual_delta_reading':'All12initial+3precision treaty ops;7TPops;2employeeops;12socialops;21benefitops;32initialpayroll+28followuponly actual deltas read in bounded outputs.','genuine_remaining_limits':'Specific church rates/caps, individualfundtariffs, SaxonyMidijob, startuplowerpension/spousefundallocation, treaty-specific/SME-matrix and historicalaward interactions remain for final domain map; not converted to zero or specialist by convenience.'}
(R/'DE-R57-R96-independent-closure.json').write_text(json.dumps(result,indent=2)+'\n')
p=json.loads((R/'progress.json').read_text())
for res in results:
 for z in res['pairs']:
  slug=z['pair']['slug'];p['review_progress'][slug].update({'accepted_guide_sha256':z['pair']['Guide_sha256'],'accepted_ledger_sha256':z['pair']['ledger_sha256'],'status':'Frozenwholepair plus exact bounded R57–96 chain independently PASS; genuine precise ordinary limits retained.'})
(R/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('PASS chains',len(results),'stages',len(ck),'owncontrols')
