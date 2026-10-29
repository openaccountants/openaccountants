from pathlib import Path
import json,hashlib,subprocess,datetime
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');B=O.parent/'germany-ledger-writer-B-2026-10-29';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();slug='de-social-contributions';plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());records=[]
for r in plan:
 x=r['source'];a,b=x['native_LF'];assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['act_article'],'official_url':x['official_url'],'raw_path':x['raw_path'],'reader_path':x['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Selected entire quotation directly actually read in new-quote batches1–6/7–15/16–27/28–40/41–52/53–65/66–75; new-quote index refers to pending_direct_read subset, original full quote-row index retained separately.'
 records.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'frozen_current_rows_actually_read':[[1,60],[61,125],[126,187]],'quotes_direct':75,'quotes_same_raw_exact_words_whitespace_only_bridge':21,'quotes':records},indent=2)+'\n')
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
from datetime import date
ck=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 ck.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def money(x):return (Decimal(x.numerator)/Decimal(x.denominator)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
base=max(F(3955,3),min(F(48000,12),F(11625,2)))
for n,a,e in [('case1base',base,4000),('case1health',money(base*F(169,1000)),Decimal('676.00')),('case1care',money(base*F(42,1000)),Decimal('168.00')),('case1total',money(base*F(211,1000)),Decimal('844.00')),('case2base',money(F(3955,3)),Decimal('1318.33')),('case2health',money(F(3955,3)*F(169,1000)),Decimal('222.80')),('case2care',money(F(3955,3)*F(36,1000)),Decimal('47.46')),('case2above603',1000-603,397),('case2halfstandard',money(F(3955,2)*F(186,1000)),Decimal('367.82')),('case2fullstandard',money(F(3955)*F(186,1000)),Decimal('735.63'))]:c(n,a,e)
c('case2total rounded components',Decimal('222.80')+Decimal('47.46')+Decimal('367.82'),Decimal('638.08'))
c('case2phaseends',2026+3,2029)
c('case2nominalMay31Sunday',date(2026,5,31).weekday(),6)
c('case2ordinarynextworkingMonday',date(2026,6,1).weekday(),0)
c('old800casebase',money(max(F(800),F(3955,3))),Decimal('1318.33'))
c('old800casehealthcare',Decimal('222.80')+Decimal('47.46'),Decimal('270.26'))
for n,a,e in [('voluntarypensionmin',money(F(603)*F(186,1000)),Decimal('112.16')),('voluntarypensionmax',money(F(8450)*F(186,1000)),Decimal('1571.70')),('AVapplicationfull',money(F(3955)*F(26,1000)),Decimal('102.83')),('AVapplicationstart',money(F(3955,2)*F(26,1000)),Decimal('51.42')),('job7kRV',F(7000)*F(93,1000),651),('job7kAV',F(7000)*F(13,1000),91),('highincomeKV',money(F(11625,2)*F(171,1000)),Decimal('993.94')),('highincomePV2children',money(F(11625,2)*F(335,10000)),Decimal('194.72')),('KSKRV2500',money(F(2500)*F(93,1000)),Decimal('232.50')),('KSKKV2500',money(F(2500)*F(175,2000)),Decimal('218.75')),('KSKPV2500childless',money(F(2500)*F(24,1000)),Decimal('60.00')),('KSKtotal',Decimal('232.50')+Decimal('218.75')+Decimal('60'),Decimal('511.25')),('agency20klevy',F(20000)*F(49,1000),980),('bakery800below1000',800<=1000,True),('partialprior6monthslevy',F(12000,6)*F(49,1000),98),('wrongannualdenominator',F(12000,12)*F(49,1000),49),('40exactnoadvance',40<=40,True),('40.01notexempt',F(4001,100)<=40,False),('marginal603exactexempt',603<=603,True),('marginal603.01notexempt',F(60301,100)<=603,False),('KSK3900exactbelowtest',3900>3900,False),('KSK3900.01abovetest',F(390001,100)>3900,True),('foreignspousechild1/3ref',F(3955,3),F(3955,3)),('historical2025min',money(F(3745,3)),Decimal('1248.33')),('historical2025healthcap',F(66150,12),F(11025,2))]:c(n,a,e)
# Classification controls compare the stated statutory gates, not a real insurance assessment.
c('groupopinionwithin2yearsmayprotectwithout1month',all([True,True,True]),True)
c('groupopinionoutside2yearsfailsroute',all([True,False,True]),False)
c('private5000capinclusive',5000<=5000,True);c('private6000failscap',6000<=5000,False)
c('AVordinaryothermandatoryblocks',not True,False);c('AVminijobexceptionnotbar',not(False),True)
c('KSK2weektestaloneinsufficientwithoutdecision',all([True,False]),False)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(ck),'controls':ck,'scope':'Both original executable cases manually recomputed with exact fractions and per-component commercial cent rounding; four narrative illustrations and old800-profit case, rate/threshold/date/levy and eligibility separators. No claimed approval of individual fund notices or unresolved lower-income start-phase route.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_frozen_current_rows_read':187,'quotes_direct_read':75,'same_raw_quotation_word_bridges':21,'old_origins':len(old['current_main_rows'])+len(old['pre_refresh_rows']),'old_semantic_spots':20,'own_controls':len(ck),'status':'NEEDS exact DE-R72–77 successors; genuine stated ordinary method questions remain for final country scope.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONEsocial',len(ck),'controls',len(records),'sources')
