from pathlib import Path
import json
P=Path('ledgers/spain-2026-evidence/es-social-contributions');q=json.loads((P/'quotes.json').read_text())
def setspan(k,src,art,rr):
 a=(P/'sources'/(src+'.reader.txt')).read_text().splitlines();old=q.get(k,[]);url=next(z['url'] for z in json.load(open(P/'source-identities.json')) if z['key']==src);q[k]=[]
 for lo,hi in rr:q[k].append(dict(source=src,article=art,url=url,quote='\n'.join(a[lo-1:hi]),reader='sources/'+src+'.reader.txt',LF_start=lo,LF_end=hi,read_on='2026-10-28'))
a=(P/'sources/S1.reader.txt').read_text().splitlines()
for j in range(1,12):
 lo=next(i+1 for i in range(590,680) if a[i].strip()==str(j));setspan('group'+str(j),'S1','3',[(lo,lo+3)])
setspan('AT','S0','DA61 II.a',[(18517,18521)]);setspan('ATgate','S0','DA61 office conditions',[(18565,18565)]);setspan('AT97','S0','DA61 code97',[(18495,18499)])
setspan('equality','S8','TGSS Prórroga Tarifa Plana',[(494,494)])
setspan('floor','S0','308.1.a.4',[(12785,12787)]);q['floor']+=json.load(open(P/'quotes.json'))['floor'][:1]
setspan('regCompare','S6','46.2.5.a/b/c',[(2749,2753),(2761,2761)])
setspan('regSigned','S6','46.2.5.b/c/d;2.7',[(2753,2753),(2761,2761),(2767,2767),(2777,2777)])
setspan('regDeadlines','S6','46.2.5.b/c',[(2755,2755),(2763,2763)])
setspan('regElection','S6','46.2.6',[(2769,2773)])
setspan('suspension','S1','6.2/3/4/5/6',[(717,717),(721,731),(733,735),(741,745)])
setspan('houseUnemp','S1','35',[(1862,1874)])
setspan('houseProration','S1','15.1/2',[(1203,1213)])
setspan('agrProtected','S1','14.5–7',[(1105,1123)])
setspan('compatibility','S0','342.1/3',[(14260,14260),(14268,14268)]);q['compatibility']+=json.load(open(P/'quotes.json'))['compatibility'][1:]
# Keep only precise current-year native quote fragments; old2021image constants are separately visually transcribed.
setspan('RED05','S12','selected2026 operating passage',[(468,480)])
setspan('interest','S0','31.3',[(2676,2676)])
setspan('_int','S2','explicit2026confirmation',[(86,86)]);q['interest']+=q.pop('_int')
setspan('_floor','S1','18.4',[(1388,1388)]);q['floor']=q['floor'][:1]+q.pop('_floor')
setspan('_mode','S1','14.1.a',[(989,995)]);q['agrMode']+=q.pop('_mode')
setspan('_week','S0','253.1 weekly exception',[(10365,10365)]);q['agrInclusion']+=q.pop('_week')
setspan('late','S0','30.1/2',[(2634,2648)])
setspan('IPREM','S19','DA90.b',[(16348,16354)])
q['IPREM']+=[]
for source,art,rr in [('S20','SEPE current2026 table',[(376,396)]),('S21','official2026 IPREM row',[(133,148)])]:
 setspan('_tmp',source,art,rr);q['IPREM']+=q.pop('_tmp')
setspan('_bonus','S16','current debt compliance',[(415,415)])
q['houseBonus']=q['houseBonus'][:1]+q.pop('_bonus')
setspan('benefitIT','S0','321.1',[(13349,13351)])
setspan('_IT','S1','37.4',[(1898,1898)]);q['benefitIT']+=q.pop('_IT')
setspan('_IT','S18','ordinaryITbenefit',[(340,348)]);q['benefitIT']+=q.pop('_IT')
setspan('_agr','S1','14.3.b',[(1089,1091)]);q['agrInactivity']+=q.pop('_agr')
setspan('agrUnemp','S1','34.1–3',[(1840,1850)])
setspan('_agr','S1','14.6/7',[(1119,1123)]);q['agrUnemp']+=q.pop('_agr')
setspan('_duration','S0','338.1/3',[(14056,14056),(14070,14096),(14100,14100)]);q['cessation']=q.pop('_duration')+q['cessation'][1:]
q.update(json.loads((P/'formula-quotes.json').read_text()))
for _key,_rows in q.items():q[_key]=list({(_z['source'],_z['LF_start'],_z['LF_end'],_z['quote']):_z for _z in _rows}.values())
(P/'quotes.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
f=P/'build-ledger.py';s=f.read_text().replace("137:['highbase','reg']","137:['highbase','regElection']").replace("143:['reg']","143:['regCompare','regSigned','regDeadlines']").replace("146:['reg']","146:['regCompare']").replace("147:['reg']","147:['regSigned']").replace("148:['reg']","148:['regDeadlines']").replace("158:['equality','reducedextension','reg']","158:['equality','reducedextension','regSigned']").replace("324:['interesttrigger','interest','reg']","324:['interesttrigger','interest','regDeadlines']").replace("elif lf==306:ks=['reg']","elif lf==306:ks=['regDeadlines']").replace("['floor','group7']","['floor','group7']").replace("ks=['group'+str([1,2,3,4,8][n])] if n<5 else ['cap']","ks=([\'group4\',\'group5\',\'group6\',\'group7\'] if n==3 else [\'group8\',\'group9\',\'group10\',\'group11\'] if n==4 else [\'group\'+str(n+1)]) if n<5 else ['cap']")
f.write_text(s)
