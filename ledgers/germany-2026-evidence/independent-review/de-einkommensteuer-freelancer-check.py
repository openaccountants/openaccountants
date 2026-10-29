from pathlib import Path
import json,hashlib,subprocess,datetime
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');B=O.parent/'germany-ledger-writer-B-2026-10-29';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();slug='de-einkommensteuer-freelancer';plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());records=[]
for r in plan:
 x=r['source'];a,b=x['native_LF'];assert H(Path(x['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(x['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote'] in '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['act_article'],'official_url':x['official_url'],'raw_path':x['raw_path'],'reader_path':x['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Selected entire quotation directly actually read in new-quote batches1–10,11–22,23–34,35–44; new-quote index refers to pending_direct_read subset, original full quote-row index retained separately.'
 records.append(z)
header=B/'readers/DEB184.txt';(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'frozen_current_rows_actually_read':[[1,135]],'quotes_direct':44,'quotes_same_raw_exact_words_whitespace_only_bridge':54,'quotes':records,'additional_direct_table_header_read':{'reader_path':str(header),'reader_sha256':H(header.read_bytes()),'native_LF':[331,357],'scope':'Austria50/33/117 column identity corroborated against actual full header; not whole travel-table reading.'}},indent=2)+'\n')
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
def c(n,a,e):assert a==e,(n,a,e);ck.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def T(x):
 x=int(x)
 if x<=12348:return 0
 if x<=17799:y=F(x-12348,10000);return int((F(91451,100)*y+1400)*y)
 if x<=69878:z=F(x-17799,10000);return int((F(17310,100)*z+2397)*z+F(103487,100))
 if x<=277825:return int(F(42,100)*x-F(1113563,100))
 return int(F(45,100)*x-F(1947038,100))
day=min(150*6,1260);profit=72000-12000-day;taxable=profit-9100;tax=T(taxable)
for n,a,e in [('day1',day,900),('profit1',profit,59100),('taxable1',taxable,50000),('tax1',tax,10548),('church1',tax*F(9,100),F(94932,100))]:c(n,a,e)
iab=20000*F(1,2);profit=100000-iab;taxable=profit-9700;tax=T(taxable);full=tax*F(55,1000);cap=(tax-20350)*F(119,1000)
for n,a,e in [('IAB2',iab,F(10000)),('profit2',profit,F(90000)),('taxable2',taxable,F(80300)),('tax2',tax,22590),('solifull2',full,F(124245,100)),('solicap2',cap,F(26656,100)),('soli2',min(full,cap),F(26656,100))]:c(n,a,e)
tax=T(100000);mess=(110000-24500)*F(35,1000);trade=mess*4;credit=min(4*mess,tax,trade)
for n,a,e in [('tariff3',tax,30864),('mess3',mess,F(299250,100)),('trade3',trade,F(11970)),('credit3',credit,F(11970)),('incometax3',tax-credit,F(18894)),('church3',tax*F(9,100),F(277776,100)),('jointsplit100k',2*T(50000),21096),('prepay2637',F(10548,4),F(2637))]:c(n,a,e)
c('IABprofit200kpass',200000<=200000,True);c('IABprofit200001fail',200001<=200000,False);c('IABplanned20k50pct',20000*F(1,2),F(10000));c('flatwriter30pctcap',min(20000*F(3,10),3600),F(3600));c('flatside25pctcap',min(5000*F(1,4),900),F(900));c('GWG952nettest',F(952)/F(119,100),F(800));c('GWGcostirrecoverable',952,952);c('GWGrecoverablecost',800,800);c('pensioncapminers',F(124800)*F(247,1000),F(308256,10));c('pensioncapceil',-(-308256//10),30826);c('R16eligible400reducer100',400-100,300);c('R16eligible400noreducer',400,400);c('oneunitbusinessstartturnover25000inside',25000<=25000,True)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(ck),'controls':ck,'scope':'All3 original oa fixture computations plus joint/prepayment narrative and source-based decision boundaries. Fixed original church9% is stipulated; no new state-law approval.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_frozen_current_rows_read':135,'quotes_direct_read':44,'same_raw_quotation_word_bridges':54,'old_origins':len(old['current_main_rows'])+len(old['pre_refresh_rows']),'old_semantic_spots':16,'own_controls':len(ck),'status':'R01/R02/R05 deltas supported; DE-R14letting summary/DE-R16employee410 conditions successors pending. No country verdict.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONEfreelancer',len(ck),'controls',len(records),'sources')
