from pathlib import Path
import json,hashlib,re,runpy,subprocess,decimal,datetime
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];G=R/'skills/international/spain/es-irpf-deductions.md';b=G.read_text();I=json.loads((P/'source-identities.json').read_text());Q=json.loads((P/'actual-read-quotes.json').read_text());rows=json.loads((P/'claim-rows.json').read_text());old=json.loads((P/'old-topics.json').read_text());checks=[]
def ok(name,value):
 assert value,name;checks.append(dict(check=name,result='PASS'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ok('root supplied current v2.4 Guide binding',sha(G)=='02b2f58679014052448ff45b1623f105d910701443908d4c24a797528feaa92b')
for z in I:
 ok('raw unchanged '+z['key'],sha(P/z['raw'])==z['raw_sha256']);ok('reader unchanged '+z['key'],sha(P/z['reader'])==z['reader_sha256'])
readers={z['reader']:(P/z['reader']).read_text().split('\n') for z in Q}
for z in Q:ok('exact literalLF '+z['section']+'/'+z['key']+':'+str(z['LF_start']),z['quote'] in '\n'.join(readers[z['reader']][z['LF_start']-1:z['LF_end']]))
for z in rows:ok('exact current '+z['id'],z['wording'] in b)
needed=[]
for lf,sec,u in E['units'](b):
 if u.startswith(('#','<!--','---')) or re.match(r'^\|[\s|:-]+$',u) or (u.startswith('|') and re.match(r'^\|[\s|:-]+$',b.split('\n')[lf])):continue
 needed.append(lf)
ok('every substantive/operational current unit recorded',set(needed)<=set(x['lf'] for x in rows))
for ref in ['62b7639a5a68324a83a96bb0190fff8b7c76f8c5',E['FROZEN']]:
 bb=subprocess.check_output(['git','show',ref+':skills/international/spain/es-irpf-deductions.md'],cwd=R,text=True);orig=[(lf,sec,u) for lf,sec,u in E['units'](bb)];mapped=[(z['old_lf'],z['section'],z['wording']) for z in old if z['ref']==ref];ok('all actual comparator units exact '+ref,orig==mapped)
orig=subprocess.check_output(['git','show',E['FROZEN']+':skills/international/spain/es-irpf-deductions.md'],cwd=R,text=True)
blocks=lambda t:re.findall(r'```oa-check\n[\s\S]*?```',t)
ok('exactly two original main oa blocks byte-exact',len(blocks(b))==2 and blocks(b)==blocks(orig))
ok('old unsupported topics explicitly disclosed',all(next(z for z in old if z['old_lf']==lf and z['ref'].startswith('62b'))['destination'].startswith('Not yet confirmed: historical') for lf in [62,227]))
D=decimal.Decimal;C=lambda n:D(str(n)).quantize(D('.01'),rounding=decimal.ROUND_HALF_UP);calc=[]
def eq(label,value,expected):
 a=C(value);e=C(expected);ok('math '+label,a==e);calc.append(dict(control=label,computed=str(a),expected=str(e),status='computed from sourced constants plus stated fictional inputs; not official worked-example quote'))
# Supplemental fixtures for the writer-owned regions; root Murcia/Galicia and B Valencia
# retain their separate actual control files, not falsely called this writer's own controls.
eq('Catalan ordinary rent',min(D(6000)*D('.1'),D(500)),500);eq('Catalan victim rent',min(D(6000)*D('.2'),D(1000)),1000);eq('Catalan separate grants',500+1000,1500);eq('Catalan current quota',2375+(28000-22000)*D('.16')-5550*D('.095'),2807.75);eq('Catalan quota after rent',D('2807.75')-1500,1307.75)
eq('legacy State9040',9040*D('.075'),678);eq('Catalan enhanced9040',9040*D('.09'),813.60);eq('Catalan total enhanced',9040*D('.165'),1491.60);eq('Catalan mixed equal',6000*D('.09')+3040*D('.075'),768);eq('Catalan proportional countercontrol',4520*D('.165'),745.80);eq('Catalan unequal',3000*D('.09')+6040*D('.075'),723);eq('Catalan unequal proportion',2260*D('.09')+6780*D('.075'),711.90);eq('Catalan firstdeclarant countercontrol',9000*D('.075')+40*D('.09'),678.60);eq('Catalan observed remaining quota',D('10545.25')-723,9822.25)
eq('Catalan rural rehabilitation aid subtraction',6000*D('.15')-500,400);eq('Catalan thalidomide established rates',10000*D('.275'),2750);eq('Catalan forest tax cap',min(10000*D('.15'),20000*D('.05')),1000)
eq('Andalucian ganancial vet each',min(600/D(2)*D('.3'),100),90);eq('CLM ordinary rent amended500',min(4000*D('.15'),500),500);eq('CLM rural annual cap',12000*D('.15'),1800)
eq('Balearic child184days660cap',660*D(184)/365,D('332.7123287671232876712328767'));eq('Balearic child184days900cap',900*D(184)/365,D('453.6986301369863013698630137'))
# Ordinary cap-only individual sharing separates actual own payments from credit cap division.
eq('Balearic ordinary payer2000 halfcap660',min(2000*D('.4'),660/D(2)),330);eq('Balearic ordinary payer1000 halfcap660',min(1000*D('.4'),660/D(2)),330);eq('Balearic enhanced payer1000 halfcap900',min(1000*D('.5'),900/D(2)),450)
eq('Canary prior home/reinvest threshold',max(0,min(12000,25000+12000-30000)),7000);eq('Canary threshold merely reached',max(0,min(12000,18000+12000-30000)),0);eq('Canary regional6000 4pct',6000*D('.04'),240);eq('Canary 15pct quota cap',1000*D('.15'),150);eq('Canary combinedregional legacyplusown',678+150,828);eq('Canary quota1000 remaining',1000-828,172);eq('Canary total home relief',678+828,1506);eq('Canary quota700 availableown',min(240,700*D('.15'),700-678),22)
eq('Canary ordinary health',min(5000*D('.12'),500),500);eq('Canary OR increment once',min(5000*D('.12'),600),600);eq('Canary higherincome cap',min(5000*D('.12'),150),150);eq('Canary two worker contributions',2*min(3000*D('.2'),500),1000);eq('Canary fixed plus two contributions',600+2*min(3000*D('.2'),500),1600);eq('Canary quota after combined credits',2000-1600,400)
eq('CyL project30000 investor',min(30000*D('.2'),10000),6000);eq('CyL project20000 investor',min(20000*D('.2'),10000),4000);eq('CyL project60000 investor',min(60000*D('.2'),10000),10000);eq('CyL project40000 investor',min(40000*D('.2'),10000),8000);eq('CyL oldplusnew12000',10000*D('.15')+9040*D('.075'),2178);eq('CyL oldplusnew6000',6000*D('.15')+6000*D('.075'),1350);eq('CyL ruralplusnationallegacy',1500+2*678,2856)
eq('Ext grant total net',28000-12000,16000);eq('Ext annual grant net',14000-6000,8000);eq('Ext rental cap-before-day',D('.15')*9040*200/275,986.18);eq('Ext rental netgrant day',D('.15')*8000*200/275,872.73);eq('Ext all275rented',D('.15')*9040,1356);eq('Ext Jan1after364',D('.15')*9040*300/364,1117.58);eq('Ext wrong365 countercontrol',D('.15')*8000*200/365,657.53);eq('Ext fictional local offeredrent cap',30000*D('.3'),9000);eq('Ext offer700 annual',700*12,8400)
ok('Ext 2026 exact calendar rental200/offered75',(datetime.date(2026,10,17)-datetime.date(2026,4,1)).days+1==200 and (datetime.date(2026,12,31)-datetime.date(2026,10,18)).days+1==75)
eq('Rioja separate nursery300',1000*D('.3'),300);eq('Rioja separate nursery200',1000*D('.2'),200);eq('Rioja nursery combined',300+200,500);eq('Rioja nursery twoentitled each',500/D(2),250);eq('Rioja quota after nursery',D('724.30')-500,224.30);eq('Rioja five months',5*100,500);eq('Rioja five months shared',500/D(2),250)
# Attribution uses source-specific own2026 schedules, not the old software's changed rates.
for name,q,expected in [('CLM',1660.50,79.07),('Cantabria',1480.25,70.49),('Canary',1564.21,74.49)]:eq(name+'attributionQ*N/G',D(str(q))*1000/21000,expected)
eq('Aragon attributedquota',D('1629.94')*1000/21000,77.62);eq('Aragon30pct afterTround',C(D('1629.94')*1000/21000)*D('.3'),23.29)
eq('liquidable aid98571',D(1000)*20700/21000,985.71);eq('Ast aid ownrates',C(D(1000)*20700/21000)*D('.1585'),156.24);eq('Ext aid own2026rates',C(D(1000)*20700/21000)*D('.1464'),144.31);eq('Gal aid ownrates',C(D(1000)*20700/21000)*D('.1549'),152.69);eq('Gal aid roundedliquidable98635',D('1000.64')*20700/21000,986.35);eq('Gal aid centseparator',C(D('1000.64')*20700/21000)*D('.1549'),152.79);eq('Val directaid notBLfactor',1000*D('.0742'),74.20);eq('Bal aid BLbase',D(1000)*23500/25000,940);eq('Bal aid combinedgeneralrates',940*D('.1771'),166.47);eq('Bal war activitynetbase',D(20000)/100000*30000,6000);eq('Bal war credit',D(20000)/100000*30000*D('.0886'),531.60)
for v,expect in [(7000,137.75),(8000,232.75),(8600,289.75),(9600,384.75)]:eq('CLM generalquota'+str(v),(v-5550)*D('.095'),expect)
eq('jointG12000',20000-9000+1000,12000);eq('jointB8600',12000-3400,8600);eq('both-entitled counterratio26560',D('289.75')*11000/12000,265.60);eq('both-entitled counterratio32556',D('384.75')*11000/13000,325.56)
eq('employee largeaid before19f',396000+15000-1500,409500);eq('employee after19f',409500-2000-3500,404000);eq('employee unionceiling',1000+800,1800)
(P/'supplementary-numeric-controls.json').write_text(json.dumps(calc,ensure_ascii=False,indent=2)+'\n');summary=dict(guide_sha256=sha(G),ledger_sha256=sha(R/'ledgers/es-irpf-deductions.md'),source_pairs=len(I),native_quotes=len(Q),exact_current_clauses=len(rows),old_units=len(old),own_supplementary_numeric_controls=len(calc),checks=len(checks),failures=0,limits='Writer controls only; independent review still required. Root Murcia/Galicia37 and B Valencia91 controls are separately attributed. No broader Guide/repo/schema rerun.');(P/'ledger-check-results.json').write_text(json.dumps(dict(summary=summary,checks=checks),ensure_ascii=False,indent=2)+'\n');print(summary)
