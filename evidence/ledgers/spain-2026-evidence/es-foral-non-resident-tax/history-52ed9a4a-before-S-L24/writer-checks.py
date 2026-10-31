from pathlib import Path
from decimal import Decimal as D
import json,re,hashlib,runpy,subprocess
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];checks=[]
def ck(name,condition,detail=''):
 checks.append(dict(name=name,pass_=bool(condition),detail=detail))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',s).strip()
g=R/'skills/international/spain/es-foral-non-resident-tax.md';guide=g.read_text();Q=json.loads((P/'quotes.json').read_text());sel=json.loads((P/'selected-quotes-for-writer-read.json').read_text());rows=json.loads((P/'claim-rows.json').read_text());old=json.loads((P/'old-topics.json').read_text());earliest=json.loads((P/'earliest-old-topics.json').read_text())
ck('Guide unchanged from supplied frozen body',g.read_bytes()==(P/'frozen-guide.txt').read_bytes())
ck('Guide exact pinned identity',sha(g)=='5c0d3b2b279a8a1cd11080c4d025a4bad14303c764c2245797ec9b8d84effed9')
for x in json.loads((P/'source-identities.json').read_text()):
 for k in ['raw','reader']:ck(x['key']+' '+k+' byte identity',sha(P/x[k])==x[k+'_sha256'])
for z in sel:
 native=(P/z['reader']).read_text().split('\n');actual=norm('\n'.join(native[z['LF_start']-1:z['LF_end']]))
 ck(z['key']+' exact original-language native interval',actual==z['quote'],str(z['LF_start'])+'–'+str(z['LF_end']))
for i,row in enumerate(rows):
 native='\n'.join(guide.split('\n')[row['lf']-1:]);ck('current row '+str(i+1)+' exact Guide wording',row['wording'] in native.split('\n\n')[0])
ck('all current units have a row',set(x['lf']for x in rows)==set(x[0]for x in E['units'](guide)))
ck('all frozen original units mapped',[(x['old_lf'],x['wording'])for x in old if x.get('old_lf')]==[(lf,u)for lf,sec,u in E['units']((P/'frozen-guide.txt').read_text())])
ck('all first-branch units mapped',[(x['old_lf'],x['wording'])for x in earliest]==[(lf,u)for lf,sec,u in E['units']((P/'earliest-branch-guide.md').read_text())])
ck('all old-topic destinations explicit',all(x['destination']for x in old+earliest))
ck('own three-province PIT33+CIT44 vectors',len([x for x in sel if x['key'].startswith(('PIT_coef_','CIT_coef_'))])==231)
# Separating source checks address actual failed draft selectors, year scope and procedural distinctions.
for key,parts in {
 'B211':['un mes','fecha de la transmisión'],'A211':['un mes','fecha de la transmisión'],'G211':['un mes','fecha de la transmisión'],
 'BJanuary':['31','enero'],'BJanuaryEffect':['primera vez','2023'],'A296calendar':['enero inmediato siguiente'],
 'N210zero':['cuota cero','1 al 31 de enero'],'G210windows':['tres meses','un mes'],
 'ATlate':['seis meses','duodécimo','doce meses posteriores'],'BTcollection':['incompatibles','0,5','20 por ciento'],
 'StateOwnuseGeneral':['2 por ciento'],'StateOwnuseDA55':['2026','1 de enero de 2012'],
 'NC_small23':['23 por 100','19 por 100'],'NC_micro19':['50 por 100'],
 'B_PITexception':['31 de diciembre de 1994','1995'],'A_PITexception':['31 de diciembre de 1994','1995'],
 'G_PITexception':['31 de diciembre de 1994','1995']}.items():ck(key+' operative distinguishing conditions',all(v in Q[key]['quote']for v in parts))
ck('2027 future scale not operative2026 quote','20261002' in Q['StateOwnuse']['url'] and '100.000,00' not in Q['StateOwnuse']['quote'])
ck('G210 sale quote excludes obsolete own-use filing paragraph','inmobiliarias imputadas' not in Q['G210windows']['quote'])
for n,actual,expected in [
 ('residential rent', (D(12000)-D(2000)-D(3000))*D('.19'),D(1330)),
 ('employment net', (D(20000)-D(1200))*D('.19'),D(3572)),('employment refund',D(3800)-D(3572),D(228)),
 ('dividend', (D(6000)-D(1500))*D('.19'),D(855)),('Navarra imputation',D(100000)*D('.011')*D('.19'),D(209)),
 ('sale indexed basis',D(203000)*D('1.249'),D(253547)),('sale gain',D(398500)-D(253547),D(144953)),
 ('sale final tax',D(144953)*D('.19'),D('27541.07')),('sale net balance',D('27541.07')-D(12000),D('15541.07')),
 ('local remittance',D(10000)*D('.20'),D(2000)),('State remittance',D(10000)*D('.19'),D(1900)),
 ('PE no imported resident surcharge',D(190000)*D('.24'),D(45600)),('PE final result',D(104000)*D('.24')-D(5000),D(19960)),
 ('PE60percent',D(19960)*D('.6'),D(11976)),('PE40percent',D(19960)*D('.4'),D(7984)),
 ('withholding',D(6000)*D('.19'),D(1140)),('withholding60',D(1140)*D('.6'),D(684)),('withholding40',D(1140)*D('.4'),D(456)),
 ('interest full year',D(10000)*D('.040625'),D('406.25')),('interest73days',D(10000)*D('.040625')*D(73)/D(365),D('81.25')),
 ('1994ordinary',D(100000)*D('2.030'),D(203000)),('1994Dec31',D(100000)*D('2.156'),D(215600))]:ck(n,actual==expected,str(actual))
proc=subprocess.run(['python3','scripts/check-examples.py',str(g.relative_to(R))],cwd=R,text=True,capture_output=True);(P/'oa-check-result.txt').write_text(proc.stdout+proc.stderr);ck('original two oa examples',proc.returncode==0 and '2 oa-check blocks' in proc.stdout)
report=dict(guide_sha256=sha(g),ledger_sha256=sha(R/'ledgers/es-foral-non-resident-tax.md'),checks=len(checks),failures=[x for x in checks if not x['pass_']],results=checks,scope='Writer integrity and finite source/arithmetic controls; not independent review, accountant attestation or whole-country completion.')
(P/'writer-check-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='results'},ensure_ascii=False));raise SystemExit(bool(report['failures']))
