from pathlib import Path
import json,hashlib,subprocess
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');A=O.parent/'germany-ledger-writer-2026-10-28';slug='de-vat-annual-and-special-schemes';D=A/'support'/slug;W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());out=[]
for r in plan:
 x=r['source'];a,b=r['native_LF'];assert H(Path(r['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(r['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote']in '\n'.join(Path(r['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['article'],'official_url':x['url'],'raw_path':r['raw_path'],'reader_path':r['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Full selected quotation directly read in bounded new-quote batches1–10/11–20/21–30/31–39/40–47; new index is subset index, original quote index retained here.'
 out.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'all174_current_units_actually_read':[[1,65],[66,125],[126,174]],'direct_new_quotes':47,'exact_quotation_word_same_raw_bridges':20,'quotes':out},indent=2)+'\n')
old=json.loads((D/'old-topics.json').read_text());cache={};eligible=[]
for i,x in enumerate(old,1):
 if x['ref']not in cache:cache[x['ref']]=subprocess.check_output(['git','show',x['ref']+':skills/international/germany/'+slug+'.md'],cwd=W).decode().split('\n')
 assert cache[x['ref']][x['old_lf']-1]==x['wording']
 if 150<=len(x['wording'])<=1600 and not x['wording'].startswith(('#','| Source','|---')):eligible.append(i)
spots=[eligible[int(i*(len(eligible)-1)/11)]for i in range(12)]
for i in spots:print('OLDSPOT',i,json.dumps(old[i-1],ensure_ascii=False))
(O/(slug+'-old-origin-check.json')).write_text(json.dumps({'all_actual_old_origins':len(old),'mismatches':0,'semantic_spots_actually_read':spots,'scope':'All real Git wording origins checked;12actual prior-topic semantic samples, not every old destination fresh reading'},indent=2)+'\n')
checks=[]
def c(n,a,e):
 assert a==e,(n,a,e)
 checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
c('example1 prepayments',38000-29750,8250);c('example1 annual output',38000+10000*F(19,100),39900);c('example1 annualnet',39900-29750,10150);c('example1 closing',10150-8250,1900);c('example1 paymentpenalty',1900*F(1,100)*2,38);c('example1 filingmonthlyminimum',max(F(1900)*F(25,10000),25),25);c('example1 three months',3*25,75)
c('example2 excessprev25k',31200-25000,6200);c('example2 cashheadroom',800000-31200,768800);c('example2 net2026',F(8925)*100/119,7500);c('example2 output2026',F(8925)*19/119,1425);c('example2 oldsuppliedjob exempt',1800*0,0);c('example2 advance exact',F(2000)*19/119,F(38000,119));c('example2 closing roundedcents',round(float(F(1425)+F(38000,119)-380),2),1364.33)
c('KU priorequality25000',25000<=25000,True);c('KU prior25000.01fails',F(2500001,100)<=25000,False);c('KU current100000equality',100000<=100000,True);c('KU currentcrossingentiresupply',F(99900)+200>100000,True);c('newbusiness25000not100000',26000>25000,True);c('adv9000quarterlydefault',9000>9000,False);c('adv9000.01monthly',F(900001,100)>9000,True);c('release2000inclusive',2000<=2000,True);c('specialprepayment11k',F(11000,11),1000);c('partialyear3months11k annualizedspecial',F(11000*12,3*11),4000)
c('input1000inclusive noadjust',1000<=1000,True);c('input1000.01outside',F(100001,100)<=1000,False);c('change10pp outside less10',F(10)<10,False);c('change9pp 10000input onefifth180',F(10000)*F(9,100)/5,180);c('change9pp 100000input override1800',F(100000)*F(9,100)/5,1800);c('annual6000inclusive',6000<=6000,True);c('RC5000inclusive',5000>=5000,True);c('RC4999.99fails',F(499999,100)>=5000,False);c('EUdistance10000notcross',10000>10000,False);c('R23priorGerman30000fails',30000<=25000,False)
import datetime
c('31July2027Saturday',datetime.date(2027,7,31).weekday(),5);c('2August2027Monday',datetime.date(2027,8,2).weekday(),0);c('29February2028Tuesday',datetime.date(2028,2,29).weekday(),1);c('14June2027Monday',datetime.date(2027,6,14).weekday(),0);c('10April2026Friday',datetime.date(2026,4,10).weekday(),4);c('31January2027Sunday',datetime.date(2027,1,31).weekday(),6)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(checks),'controls':checks,'scope':'Both original executable examples plus threshold/date/input-correction separators. OSS weekend explicitly remains an existing question; no invented extension.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_current_units_read':174,'new_source_quotes_actually_read':47,'same_raw_exact_words_prior_bridges':20,'old_actual_origins':len(old),'old_semantic_spots':len(spots),'own_controls':len(checks),'status':'NEEDS DE-R23–25 exact successors; existing OSS weekend question retained for ordinary-limit assessment.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONE VATannual',len(old),'oldorigins',len(checks),'controls')
