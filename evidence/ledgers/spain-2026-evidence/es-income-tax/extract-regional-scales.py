from pathlib import Path
import re,json
P=Path('ledgers/spain-2026-evidence/es-income-tax');G=Path('skills/international/spain/es-income-tax.md').read_text().splitlines()
spec=[(1,'611-1',65,72),(2,'4',80,84),(3,'23',92,96),(4,'2',104,111),(5,'1',119,124),(6,'31',132,139),(7,'2',147,151),(8,'2',159,169),(9,'110-1',177,185),(10,'13 bis',193,197),(11,'18 bis',205,211),(12,'1',219,227),(13,'1',235,243),(14,'1',251,255),(15,'1',263,267)]
out=[]
for src,art,gl,gh in spec:
 a=(P/'sources'/f'S{src}.reader.txt').read_text().splitlines();st=next(i for i,x in enumerate(a) if re.match(r'^\s*Artículo\s+'+re.escape(art)+r'\.',x));en=next((i for i in range(st+1,len(a)) if re.match(r'^\s*Artículo\s+',a[i])),len(a));block=a[st:en]
 # Locate every desired opening/quota/width/rate tuple in native numeric runs, keeping exact original-language spans.
 vals=[]
 for i in range(st,en):
  v=a[i].strip().replace('\u202f','').replace('%','').replace(' ','').replace('\xa0','').replace(' ','').replace('»','')
  if re.fullmatch(r'[\d.,]+',v):vals.append((i+1,v))
  elif v=='–' and src==4 and i>st+20:vals.append((i+1,'0'))
 def norm(s):return float(s.replace('.','').replace(',','.'))
 for lf in range(gl,gh+1):
  cells=[x.strip() for x in G[lf-1].split('|')[1:-1]];wanted=[float(x.replace('%','')) if x!='No upper limit' else None for x in cells[:4]];hit=[]
  for j in range(len(vals)-3):
   vv=[norm(z[1]) for z in vals[j:j+4]]
   if vv[:2]==wanted[:2] and ((wanted[2] is None and (vv[2]==wanted[3] or vv[3]==wanted[3])) or vv==wanted):hit=vals[j:j+4];break
  if wanted[2] is None:
   for j in range(len(vals)-2):
    if [norm(z[1]) for z in vals[j:j+3]]==[wanted[0],wanted[1],wanted[3]]:hit=vals[j:j+3];break
  if not hit: print('MISSING',src,art,lf,wanted);continue
  lo,hi=hit[0][0],hit[-1][0];out.append(dict(guide_lf=lf,source='S'+str(src),article=art,LF_start=lo,LF_end=hi,quote='\n'.join(a[lo-1:hi])))
(P/'regional-scale-native-anchors.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('anchors',len(out))
for z in out:print(z['guide_lf'],z['source'],z['article'],f"LF{z['LF_start']}–{z['LF_end']}",z['quote'].replace('\n',' / '))
