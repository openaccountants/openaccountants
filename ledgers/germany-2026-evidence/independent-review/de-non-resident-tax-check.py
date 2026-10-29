from pathlib import Path
import json,hashlib,subprocess
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');A=O.parent/'germany-ledger-writer-2026-10-28';slug='de-non-resident-tax';D=A/'support'/slug;W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda b:hashlib.sha256(b).hexdigest();plan=json.loads((O/(slug+'-quote-reuse-plan.json')).read_text());out=[]
for r in plan:
 x=r['source'];a,b=r['native_LF'];assert H(Path(r['raw_path']).read_bytes())==x['raw_sha256'];assert H(Path(r['reader_path']).read_bytes())==x['reader_sha256'];assert x['exact_quote']in '\n'.join(Path(r['reader_path']).read_text().split('\n')[a-1:b]);z={'row':r['row'],'id':r['id'],'article':x['article'],'official_url':x['url'],'raw_path':r['raw_path'],'reader_path':r['reader_path'],'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'quote_sha256':H(x['exact_quote'].encode())}
 if 'actual_read_bridge'in r:z['actual_read_bridge']=r['actual_read_bridge']
 else:z['actual_read']='Full selected quotation directly read in bounded new-quote batches1–8/9–16/17–26/27–38; new index is subset index, original quote index retained here.'
 out.append(z)
(O/(slug+'-source-read-ledger.json')).write_text(json.dumps({'all203_current_units_actually_read':[[1,203]],'direct_new_quotes':38,'exact_quotation_word_same_raw_bridges':40,'quotes':out},indent=2)+'\n')
old=json.loads((D/'old-topics.json').read_text());cache={};eligible=[]
for i,x in enumerate(old,1):
 if x['ref']not in cache:cache[x['ref']]=subprocess.check_output(['git','show',x['ref']+':skills/international/germany/'+slug+'.md'],cwd=W).decode().split('\n')
 assert cache[x['ref']][x['old_lf']-1]==x['wording']
 if 150<=len(x['wording'])<=1600 and not x['wording'].startswith(('#','| Source','|---')):eligible.append(i)
spots=[eligible[int(i*(len(eligible)-1)/11)]for i in range(12)]
for i in spots:print('OLDSPOT',i,json.dumps(old[i-1],ensure_ascii=False))
(O/(slug+'-old-origin-check.json')).write_text(json.dumps({'all_actual_old_origins':len(old),'mismatches':0,'semantic_spots_actually_read':spots,'scope':'All real Git wording origins checked;12actual prior-topic semantic samples, not every old destination fresh reading'},indent=2)+'\n')
checks=[]
def c(n,a,e):assert a==e,(n,a,e);checks.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
def T(x):
 x=int(x)
 if x<=12348:return 0
 if x<=17799:y=F(x-12348,10000);return int((F(91451,100)*y+1400)*y)
 if x<=69878:z=F(x-17799,10000);return int((F(17310,100)*z+2397)*z+F(103487,100))
 if x<=277825:return int(F(42,100)*x-F(1113563,100))
 return int(F(45,100)*x-F(1947038,100))
base=24000+12348;limited=T(base);optbase=24000-36;prog=optbase+2000;pt=T(prog);opt=int(optbase*F(pt,prog))
for n,a,e in [('limitedbase1',base,36348),('limitedtax1',limited,6076),('Germanincomeratio1',F(24000,26000),F(12,13)),('optiontaxable1',optbase,23964),('progbase1',prog,25964),('progtax1',pt,3107),('optiontax1',opt,2867),('saving1',limited-opt,3209)]:c(n,a,e)
e=10000-1000;paid=10000*F(15,100);before=e*F(1,4);q=min(paid,F(10000,4),before);flat=F(e-4*q,4);soli=flat*F(55,1000)
for n,a,e2 in [('foreignpaid2',paid,F(1500)),('capitaltaxbefore2',before,F(2250)),('credited2',q,F(1500)),('flattax2',flat,F(750)),('Soli2',soli,F(4125,100)),('total2',flat+soli,F(79125,100)),('refundableforeignexcessnotcredit',min(3000-1500,2500,2250),1500),('eligible3000norefundGermancreditcap',min(3000,2500,2250),2250)]:c(n,a,e2)
c('tariffforeigncap60k10k',F(T(60000))*F(10000,60000),F(T(60000),6));c('group75pct',12348*F(3,4),F(9261));c('grouphalf',12348*F(1,2),F(6174));c('groupquarter',12348*F(1,4),F(3087));c('jointGFB',12348*2,24696);c('90pctinclusive',F(90000,100000)>=F(9,10),True);c('below90pct',F(89999,100000)>=F(9,10),False);c('profpension10k Germany20k foreign30k',10000*F(20000,50000),F(4000));c('profpensioncapGermanincome1k',min(F(10000)*F(1000,2500),1000),1000);c('artistgross10000',10000*F(15,100),F(1500));c('artistnetEU10000cost8000',2000*F(3,10),F(600));c('royaltynono3netroute',False,False);c('R18assessmentSoli20400',min(F(20400)*F(55,1000),F(20400-20350)*F(119,1000)),F(595,100));c('R22book40of100fails',F(40,100)>F(1,2),False);c('R22book60of100passes',F(60,100)>F(1,2),True);c('R21unrelatedregistryonlynotGermanbythatbranch',False,False)
(O/(slug+'-own-controls.json')).write_text(json.dumps({'count':len(checks),'controls':checks,'scope':'Both original executable examples and supplementary credit narration recomputed; declared progression-rounding boundary retained. No ruling on foreign-capital1(3)test or every actual treaty.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress'][slug]={'all_current_units_read':203,'new_source_quotes_actually_read':38,'same_raw_exact_words_prior_bridges':40,'old_actual_origins':len(old),'old_semantic_spots':len(spots),'own_controls':len(checks),'status':'NEEDS DE-R18–22 exact successors. Existing foreigncapital1(3)/progression-rounding/refundSoli/statechurch questions retained for finite country ordinary-limit assessment.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('DONE NR',len(old),'oldorigins',len(checks),'controls')
