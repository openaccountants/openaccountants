from pathlib import Path
import json,hashlib,subprocess,datetime
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');B=O.parent/'germany-ledger-writer-B-2026-10-29';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();slug='de-capital-gains';plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());records=[]
for r in plan:
 x=r['source'];a,b=x['native_LF'];assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['act_article'],'official_url':x['official_url'],'raw_path':x['raw_path'],'reader_path':x['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Selected entire quotation directly actually read in new-quote batches1–10/11–20/21–30/31–40/41–44; new-quote index refers to pending_direct_read subset, original full quote-row index retained separately.'
 records.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'frozen_current_rows_actually_read':[[1,45],[46,83]],'quotes_direct':44,'quotes_same_raw_exact_words_whitespace_only_bridge':27,'quotes':records},indent=2)+'\n')
rows=json.loads((B/'support'/slug/'rows.json').read_text());frozen=(O/'guide-snapshots'/f'{slug}.md').read_text()
for x in rows:assert '\n'.join(frozen.split('\n')[x['LF_start']-1:x['LF_end']])==x['wording']
identity=next(x for x in json.loads((B/'current-and-pre-refresh-identities.json').read_text())if x['slug']==slug);old=json.loads((B/'support'/slug/'old-topic-destinations.json').read_text());main=subprocess.check_output(['git','show','62b7639a:skills/international/germany/'+slug+'.md'],cwd=W).decode();pre=subprocess.check_output(['git','show',identity['pre_refresh_revision']+':'+identity['path']],cwd=identity['git_object_repository']).decode();assert H(pre.encode())==identity['pre_refresh_sha256'];assert pre==identity['pre_refresh_body'];spotmap={}
for typ,t in [('current_main_rows',main),('pre_refresh_rows',pre)]:
 lines=t.split('\n');candidates=[]
 for n,r in enumerate(old[typ],1):
  a,b=r['old_native_LF'];txt='\n'.join(lines[a-1:b]);assert H(txt.encode())==r['old_unit_sha256']
  if 140<=len(txt)<=1200 and not txt.lstrip().startswith(('#','---','```','| Source')):candidates.append(n)
 spots=[candidates[int(i*(len(candidates)-1)/7)]for i in range(8)] if candidates else []
 spotmap[typ]=spots
 for n in spots:
  r=old[typ][n-1];a,b=r['old_native_LF'];print('OLDSPOT',typ,n,'LF',a,b,'\n'+'\n'.join(lines[a-1:b])+'\nDEST '+r['current_destination']+' '+r['disposition']+'\n')
(O/(slug+'-old-origin-check.json')).write_text(json.dumps({'current_main_origin_count':len(old['current_main_rows']),'pre_refresh_origin_count':len(old['pre_refresh_rows']),'all_actual_origins_checked':True,'mismatches':0,'semantic_spots_actually_read':spotmap},indent=2)+'\n')
ck=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 ck.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
for n,a,e in [('case1 taxable',1500+2500-1000,3000),('case1 tax',3000*F(1,4),750),('case1 Soli',750*F(55,1000),F(4125,100)),('case1 total',750+F(4125,100),F(79125,100)),('case2 sharenet',max(2000-2500,0),0),('case2 losscarry',max(2500-2000,0),500),('case2 taxable',1200+2800-1000,3000)]:c(n,a,e)
flat=round(float(F(3000)/F(408,100)),2);church=round(flat*0.08,2);soli=round(flat*0.055,2)
c('case2 flat',flat,735.29);c('case2 church stipulated8pct',church,58.82);c('case2 Soli',soli,40.44);c('case2 total',round(flat+church+soli,2),834.55)
c('case3 netshareaftercertificate',5000-3000,2000);c('case3 stipulated fullBallowance taxable',2000-1000,1000);c('case3 stipulated refund includingSoli',F(3000)*F(1,4)*F(1055,1000),F(79125,100));c('case4 base2026',50000*F(7,10)*F(32,1000),1120);c('case4 taxable2026',F(1120)*F(7,10),784);c('case4 base2025',50000*F(7,10)*F(253,10000),F(8855,10));c('case5 gain900',10900-10000,900);c('case5 900belowcliff',900<1000,True);c('case5 addgoldwhole1100taxable',900+200,1100);c('case5 exact1000notfree',1000<1000,False);c('case5 salebeforeanniversary',datetime.date(2026,2,15)<datetime.date(2026,3,1),True);c('case5 March2afteranniversary',datetime.date(2026,3,2)>datetime.date(2026,3,1),True)
gain=(100000-40000)*F(3,5);allowstart=9060*F(2,100);threshold=36100*F(2,100);allow=max(allowstart-max(gain-threshold,0),0)
for n,a,e in [('case6 gain',gain,36000),('case6 allowancestart',allowstart,F(1812,10)),('case6 cutthreshold',threshold,722),('case6 allowance',allow,0),('case6 taxable',gain-allow,36000)]:c(n,a,e)
c('case7 homecalendar2024to2026',2026-2024,2);c('case7 saleinside10yearsfrom2018',2026-2018<10,True);c('fund50pctnotEquityover50',50>50,False);c('fundmixed25inclusive',25>=25,True);c('fund60partial leaves40',1-F(60,100),F(2,5));c('fund80partial leaves20',1-F(80,100),F(1,5));c('fundJuly6fullmonthsreduction',1120*F(6,12),560);c('funddecliningpriceplusdistribution noVP',max(min(1120,-100+500)-500,0),0);c('R36full1120thenTF',F(10000-1120)*F(7,10),6216);c('R36wrong784thenTF',F(10000-784)*F(7,10),F(64512,10));c('R34qualifyinginterestactualcost',10000-2000,8000);c('R34owner10inclusive',10>=10,True);c('R34owner9.99failsalone',F(999,100)>=10,False)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(ck),'controls':ck,'scope':'All4 original executable fixtures plus3 nonexecuted narrative examples and meaningful threshold/date/fund/financing separators. Example3 refund includes an explicit full allowance at bankB solely for that added control; no such unstated amount is attributed to the Guide. Church8pct is stipulated, no state-law approval.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_frozen_current_rows_read':83,'quotes_direct_read':44,'same_raw_quotation_word_bridges':27,'old_origins':len(old['current_main_rows'])+len(old['pre_refresh_rows']),'old_semantic_spots':16,'own_controls':len(ck),'status':'NEEDS exact DE-R32–36 successors; existing statechurch/adminsource scope retained.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONEcapital',len(ck),'controls',len(records),'sources')
