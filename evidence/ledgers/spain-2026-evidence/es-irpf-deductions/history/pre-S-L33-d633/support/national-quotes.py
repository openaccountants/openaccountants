from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;I=json.loads((P/'source-identities.json').read_text());U={x['key']:x['url'] for x in I};A={x['key']:(P/x['reader']).read_text().split('\n') for x in I};Q={}
def span(k,s,art,lo,hi):
 for i in range(lo-1,hi):
  x=A[s][i]
  if not x.strip() or re.match(r'^\s*(?:\[\[ID:|\[Bloque|Subir|Jurisprudencia)',x):continue
  Q.setdefault(k,[]).append(dict(source=s,article=art,url=U[s],reader='sources/'+s+'.reader.txt',LF_start=i+1,LF_end=i+1,quote=x,read_on='2026-10-28',line_convention='literal LF'))
def active(k,s,header):
 a=A[s];st=next(i for i,x in enumerate(a) if re.match(r'^\s*'+header,x));en=next((i for i in range(st+1,len(a)) if re.match(r'^\s*(?:Artículo |Disposición |Se (?:modifica|añade|renumera)|Seleccionar redacción:|Texto añadido)',a[i])),len(a));span(k,s,header,st+2,en)
for k,s,header in [('Nat69','S0',r'Artículo\s+69\.'),('Nat70','S0',r'Artículo\s+70\.'),('Nat81','S0',r'Artículo\s+81\.'),('Nat81bis','S0',r'Artículo\s+81 bis\.'),('Nat67','S0',r'Artículo\s+67\.'),('Nat77','S0',r'Artículo\s+77\.'),('NatDT15','S0',r'Disposición transitoria decimoquinta\.'),('NatDT18','S0',r'Disposición transitoria decimoctava\.'),('NatDA50','S0',r'Disposición adicional quincuagésima\.'),('NatDA58','S0',r'Disposición adicional quincuagésima octava\.'),('NatDA62','S0',r'Disposición adicional sexagésima segunda\.'),('Gift16','S1',r'Artículo\s+16\.'),('Gift17','S1',r'Artículo\s+17\.'),('Gift18','S1',r'Artículo\s+18\.'),('Gift19','S1',r'Artículo\s+19\.'),('Gift24','S1',r'Artículo\s+24\.'),('Legacy70','S2',r'Artículo\s+70\.'),('Legacy78','S2',r'Artículo\s+78\.'),('NatR60','S3',r'Artículo\s+60\.'),('NatR60bis','S3',r'Artículo\s+60 bis\.'),('LegacyR54','S12',r'Artículo\s+54\.'),('LegacyR55','S12',r'Artículo\s+55\.')]:active(k,s,header)
span('NatStartup','S0','68.1',5185,5215);span('NatBusiness','S0','68.2',5217,5243);span('NatDonations','S0','68.3',5245,5253);span('NatHeritage','S0','68.5',5297,5307);span('NatRental2026','S0','68.6',5309,5321)
a=A['S2'];st=next(i for i,x in enumerate(a) if re.match(r'^Artículo\s+68\.',x));end=next(i for i in range(st+1,len(a)) if a[i].startswith('2. Deducciones en actividades económicas'));span('Legacy68home','S2','68.1(pre-repeal)',st+2,end)
# Preserved2014 rental calculation is unchanged in the cited2012 snapshot; the exact historical text is distinguished from new2026rent.
st=next(i for i in range(end,len(a)) if a[i].startswith('7. Deducción por alquiler'));en=next(i for i in range(st+1,len(a)) if a[i].startswith('Se modifica'));span('Legacy68rent','S2','68.7(pre-repeal)',st+1,en)
(P/'National-selected-quotes.pending-read.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n');print('groups',len(Q),'paragraphs',sum(len(v) for v in Q.values()))
for k in ['Gift16','Gift17','Gift18','Gift19','Gift24','NatDT15','NatDT18','Legacy70','Legacy78']:
 print('\n###',k)
 for z in Q[k]:print(z['source'],z['LF_start'],z['quote'])
