from pathlib import Path
import json,hashlib,subprocess
from fractions import Fraction as F
O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/germany-ledger-independent-review-2026-10-29');A=O.parent/'germany-ledger-writer-2026-10-28';D=A/'support/leaving-germany-exit-tax';W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();q=json.loads((D/'actual-read-quotes.json').read_text());bank={json.loads(p.read_text())['id']:json.loads(p.read_text()) for p in (A/'sources').glob('*.identity.json')};records=[]
for n,x in enumerate(q,1):
 s=bank[x['source']];assert H(Path(s['raw_path']))==x['raw_sha256'];rp=Path(s['reader_path']);assert H(rp)==x['reader_sha256'];a=x.get('LF_start',x.get('paragraph'));b=x.get('LF_end',a);assert x['exact_quote']in '\n'.join(rp.read_text().split('\n')[a-1:b]);records.append({'row':n,'id':x['id'],'article':x['article'],'url':x['url'],'raw_path':s['raw_path'],'reader_path':str(rp),'raw_sha256':x['raw_sha256'],'reader_sha256':x['reader_sha256'],'native_LF':[a,b],'paragraph_id':x.get('paragraph'),'quote_sha256':hashlib.sha256(x['exact_quote'].encode()).hexdigest(),'actual_read':'Full selected quote actually read in bounded batches1–9,10–20,21–27; paragraph-normalised readers not raw HTML. Source-wide reading not asserted.'})
(O/'leaving-germany-exit-tax-source-read-ledger.json').write_text(json.dumps({'all_current_units_actually_read':[[1,112]],'all_quotes_actually_read':records},indent=2)+'\n')
old=json.loads((D/'old-topics.json').read_text());cache={}
for x in old:
 ref=x['ref']
 if ref not in cache:cache[ref]=subprocess.check_output(['git','show',ref+':skills/international/germany/leaving-germany-exit-tax.md'],cwd=W).decode().split('\n')
 assert cache[ref][x['old_lf']-1]==x['wording']
spots=[i for i in [3,10,20,34,47,65,84,99] if i<=len(old)]
for i in spots:print('OLDSPOT',i,json.dumps(old[i-1],ensure_ascii=False))
(O/'leaving-germany-exit-tax-old-origin-check.json').write_text(json.dumps({'all_actual_origins_checked':len(old),'mismatches':0,'semantic_spots_actually_read':spots},indent=2)+'\n')
c=[]
def ck(n,a,e):assert a==e,(n,a,e);c.append({'name':n,'actual':str(a),'expected':str(e),'pass':True})
ck('fictional fair value minusbasis',2000000-25000,1975000);ck('60pcttaxablegain',F(1975000)*F(3,5),F(1185000));ck('same result partialreceipts lesspartialbasis',F(2000000)*F(3,5)-F(25000)*F(3,5),F(1185000));ck('fullholdingallowancegone',max(0,9060-max(0,1975000-36100)),0)
for value,e in [(500000,False),(F(50000001,100),True)]:ck('distribution exceedsquarter'+str(value),value>F(2000000,4),e)
for sh,e in [(F(99,100),False),(F(1),True)]:ck('personalsharethreshold'+str(sh),sh>=1,e)
for years,e in [(6,False),(7,True)]:ck('coveredyears'+str(years),years>=7,e)
for v,e in [(16500,False),(16501,True)]:ck('extendedincome'+str(v),v>16500,e)
for v,e in [(62000,False),(62001,True)]:ck('absoluteincomeinterest'+str(v),v>62000,e)
ck('end10yearsafter2026',2026+10,2036);ck('netcostpartialsale10k',F(10000)*F(3,5),F(6000));ck('two thirds escape equality',F(20000)>=F(30000)*F(2,3),True);ck('below2thirds noescape',F(1999999,100)>=F(30000)*F(2,3),False)
(O/'leaving-germany-exit-tax-own-controls.json').write_text(json.dumps({'count':len(c),'controls':c,'scope':'Original hypothetical narrative recomputed, not a printed full exit-tax liability example; no original oa blocks. Actual date/amount/personal gates, recent free-transfer exception pendingDE-R11.'},indent=2)+'\n')
p=json.loads((O/'progress.json').read_text());p['review_progress']['leaving-germany-exit-tax']={'current_units_read':112,'all_selected_quotes_direct_read':27,'old_origins':len(old),'old_semantic_spots':len(spots),'own_controls':len(c),'status':'NEEDS DE-R11 exact recent-free-transfer predecessor-share-test correction. Other narrow source-chain/referral limits retained.'};(O/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print('EXITactualscope',112,len(q),len(old),len(c))
