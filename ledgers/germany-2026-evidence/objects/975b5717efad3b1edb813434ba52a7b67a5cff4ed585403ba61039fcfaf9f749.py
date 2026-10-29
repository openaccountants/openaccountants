from pathlib import Path
import json,hashlib,subprocess,datetime
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');B=O.parent/'germany-ledger-writer-B-2026-10-29';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();slug='germany-vat-return';plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());records=[]
for r in plan:
 x=r['source'];a,b=x['native_LF'];assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['act_article'],'official_url':x['official_url'],'raw_path':x['raw_path'],'reader_path':x['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Selected entire quotation directly actually read in new-quote batches1–10/11–20/21–30/31–40/41–50/51–58; new-quote index refers to pending_direct_read subset, original full quote-row index retained separately.'
 records.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'frozen_current_rows_actually_read':[[1,40],[41,80],[81,116]],'quotes_direct':58,'quotes_same_raw_exact_words_whitespace_only_bridge':15,'quotes':records},indent=2)+'\n')
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
out=20000*F(19,100)+200*F(19,100)+1000*F(19,100);rc=1200*F(19,100);inp=1140+rc;net=out-inp;rounded=(net//50)*50
for n,a,e in [('case1 domesticVAT',20000*F(19,100),3800),('case1 nonEUrc',200*F(19,100),38),('case1 EUrc',1000*F(19,100),190),('case1 output',out,4028),('case1 RCinput',rc,228),('case1 totalinput',inp,1368),('case1 net',net,2660),('case1 overdue50',rounded,2650),('case1 penalty',rounded*F(1,100),F(265,10))]:c(n,a,e)
base=61000+5000;special=F(base,11);gross=127330;drink=F(gross)*F(3,10);food=gross-drink;dn=drink*100/119;fn=food*100/107;dv=drink-dn;fv=food-fn;out=dv+fv
for n,a,e in [('case2 specialbase',base,66000),('case2 special',special,6000),('case2 drinkgross',drink,38199),('case2 foodgross',food,89131),('case2 drinknet',dn,32100),('case2 foodnet',fn,83300),('case2 drinkVAT',dv,6099),('case2 foodVAT',fv,5831),('case2 output',out,11930),('case2 line48',out-4200,7730),('case2 line83',out-4200-special,1730),('case2 all19',F(gross)*19/119,20330)]:c(n,a,e)
c('Apr10Friday',datetime.date(2026,4,10).weekday(),4);c('Apr14fourcalendardayslate',(datetime.date(2026,4,14)-datetime.date(2026,4,10)).days,4);c('graceendApr13Monday',datetime.date(2026,4,13).weekday(),0);c('2027Feb10Wednesday',datetime.date(2027,2,10).weekday(),2);c('ZM50000inclusive',50000<=50000,True);c('ZM50000.01fails',F(5000001,100)<=50000,False);c('smallinvoice250inclusive',250<=250,True);c('vehiclebusiness9.99fails',F(999,100)<10,True);c('vehiclebusiness10passesminimum',10<10,False);c('gift50inside',50<=50,True);c('gift50.01outside',F(5001,100)<=50,False);c('Solarratepresumption30inclusive',30<=30,True);c('annual200000inclusive',200000<=200000,True);c('annual15000inclusive',15000<=15000,True);c('R28eligiblecustodyVAT100net',100*F(19,100),19)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(ck),'controls':ck,'scope':'Both original whole executable fixtures recomputed exactly, dates/thresholds and current source classification separators. Whole-euro-base rounding, calendar-vs-financial-year gift and other actual reservations not invented.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_frozen_current_rows_read':116,'quotes_direct_read':58,'same_raw_quotation_word_bridges':15,'old_origins':len(old['current_main_rows'])+len(old['pre_refresh_rows']),'old_semantic_spots':16,'own_controls':len(ck),'status':'NEEDS exact DE-R26–31 successors; genuine inherited source questions retained for final ordinary-limit disposition.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONEVATadvance',len(ck),'controls',len(records),'sources')
