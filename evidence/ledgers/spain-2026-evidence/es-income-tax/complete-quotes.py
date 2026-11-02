from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;Q=json.loads((P/'quotes.pending-read.json').read_text());I=json.loads((P/'source-identities.json').read_text());U={x['key']:x['url'] for x in I};A={x['key']:(P/x['reader']).read_text().splitlines() for x in I}
def span(k,s,art,rr):
 for lo,hi in rr:Q.setdefault(k,[]).append(dict(source=s,article=art,url=U[s],reader='sources/'+s+'.reader.txt',LF_start=lo,LF_end=hi,quote='\n'.join(A[s][lo-1:hi]),read_on='2026-10-28'))
Q.pop('_MISSING',None)
Q['foreignLaw']=[];span('foreignLaw','S0','7.p',[(1503,1511)])
Q['foreignReg']=[];span('foreignReg','S16','6',[(1526,1536)])
Q['expatExcess']=[];span('expatExcess','S16','9.A.3.b.4',[(1672,1676)])
span('paymentExempt','S16','109.5',[(6242,6242)])
span('savings','S0','46.a',[(3789,3793)])
span('savingsLoss','S0','49.1.b',[(3906,3910)])
span('asset','S16','22.4',[(2107,2121)])
span('citySource','S16','58',[(3233,3261)])
span('foreignManual','S20','AEAT2025 manual expressly includes TEAC2024 correction',[(20,27),(31,47)])
span('foreignTEAC','S21','19July2024 unified criterion',[(1,15),(217,227)])
span('depreciation','S22','official simplified linear table',[(88,186)])
span('progressManual','S24','AEAT progression method / printed precision discrepancy',[(99,162)])
span('concurrentManual','S25','AEAT actual-base eligibility / augmented rate base / average',[(101,189)])
span('cityManual','S26','AEAT mixed-source formula / printed final error',[(162,194)])
span('allocation','S0','67.1.a current rented-home state-only',[(5112,5118)])
span('listEffect','S18','current list and period-specific application',[(i+1,i+1) for i,x in enumerate(A['S18']) if any(n in x for n in ['2026','se inicien','aplicación','Entrada en vigor']) and len(x)>65])
span('noncoop','S19','DA10',[(769,771)])
# Scale rows retain native table labels and exact published numbers; endpoints displayed in the Guide are derived opening+width.
for art,n in [('63',6),('65',5),('66',5),('76',5)]:
 a=A['S0'];st=next(i for i,x in enumerate(a) if x.startswith('Artículo '+art+'.'));st=next(i for i in range(st,len(a)) if a[i].strip() in ['0','0,00']);vals=[]
 for i in range(st,len(a)):
  x=a[i].strip()
  if re.match(r'^Se |^Artículo ',x):break
  if re.fullmatch(r'[\d.,]+',x) or 'adelante' in x.lower():vals.append(i+1)
 for j in range(n):
  lo,hi=vals[j*4],vals[j*4+3];span('scale'+art+'_'+str(j),'S0',art,[(lo,hi)])
 for i in range(vals[min(n*4,len(vals))-1],min(vals[min(n*4,len(vals))-1]+18,len(a))):
  if ('se minorará' in a[i] or 'mínimo personal' in a[i]) and len(a[i])>50:span('scaleMethod','S0',art,[(i+1,i+1)])
# Native selected original enactment effect confirms8October, alongside current67/68.6 andDT15.
span('rentalEffect','S23','DF11 original commencement',[(i+1,i+1) for i,x in enumerate(A['S23']) if 'entrará en vigor el día siguiente' in x])
(P/'quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');print('keys',len(Q),'anchors',sum(len(x) for x in Q.values()))
