from pathlib import Path
import json
P=Path(__file__).resolve().parent;Q=json.loads((P/'quotes.json').read_text());ids=json.loads((P/'source-identities.json').read_text());U={x['key']:x['url'] for x in ids}
def span(k,s,art,lo,hi):
 a=(P/'sources'/(s+'.reader.txt')).read_text().splitlines();Q.setdefault(k,[]).append(dict(source=s,article=art,url=U[s],reader='sources/'+s+'.reader.txt',LF_start=lo,LF_end=hi,quote='\n'.join(a[lo-1:hi]),read_on='2026-10-28'))
Q['scaleMethod']=[z for z in Q['scaleMethod'] if z['LF_start']!=4987]
span('scaleMethod','S0','63.2',4750,4750);span('scaleMethod','S0','74.1/2',5598,5604)
span('concurrentManual','S25','actual Bg eligibility before augmented rate-setting',95,99)
Q['foreignTEAC']=[Q['foreignTEAC'][0]]
span('foreignTEAC','S21','unified final criterion',225,227)
span('late','S27','27.2 penalty/interest exclusion',2211,2211)
span('offence','S27','191 classification limbs',8200,8229)
span('collection','S27','28 interest incompatibility',2282,2286)
span('filing','S0','96.2 exclusive-source conditions/96.3 specific triggers',7226,7228);span('filing','S0','96.3 specific triggers',7242,7254)
span('citySource','S0','68.4.3',5273,5299)
span('foreignReg','S16','6',1534,1536)
(P/'quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
