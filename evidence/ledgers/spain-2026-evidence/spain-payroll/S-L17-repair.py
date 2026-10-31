# Historical one-time S-L17 transformation. Already applied; original7361 history is immutable.
from pathlib import Path
import json,shutil
P=Path('ledgers/spain-2026-evidence/spain-payroll');H=P/'history/pre-S-L17-7361de30';H.mkdir(parents=True,exist_ok=True)
for n in ['quotes.json','actual-read-quotes.json','build-ledger.py','check-ledger.py','ledger-summary.json','ledger-check-results.json','claim-rows.json']:
 if not (H/n).exists():shutil.copy2(P/n,H/n)
if not (H/'ledger.md').exists():shutil.copy2(Path('ledgers/spain-payroll.md'),H/'ledger.md')
Q=json.loads((P/'quotes.json').read_text());a=(P/'sources/S5.reader.txt').read_text().split('\n')
for k,zs in Q.items():
 if k.startswith('algo'):
  for z in zs:
   if z['source']=='S5':
    z['quote']='\n'.join(a[z['LF_start']-1:z['LF_end']]);z['line_convention']='literal LF split on \\n; PDF formfeed is a character, not an extra line'
(P/'quotes.json').write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n')
s=(P/'check-ledger.py').read_text();old="(P/z['reader']).read_text().splitlines()[z['LF_start']-1:z['LF_end']]";new="((P/z['reader']).read_text().split('\\n') if z.get('line_convention') else (P/z['reader']).read_text().splitlines())[z['LF_start']-1:z['LF_end']]";assert old in s;s=s.replace(old,new)
# Independently name each required operative call, rather than checking a self-repeated quote alone.
s=s.replace("c('2 original examples'", """for k,call in [('algoRED20','RED20 = REDONDEAR1 (RED20)'),('algoDesc','MINDESG = REDONDEAR1 (MINDESG)'),('algoDesc3','MINDES3= REDONDEAR1 (MINDES3)'),('algoAS65','65AS = REDONDEAR1 (65AS)'),('algoAS75','75AS = REDONDEAR1 (75AS)'),('algoDISDES','DISDES = REDONDEAR1 (DISDES)'),('algoDISAS','DISAS = REDONDEAR1 (DISAS)'),('algoASISDES','ASISDES = REDONDEAR1 (ASISDES)'),('algoASISAS','ASISAS = REDONDEAR1 (ASISAS)'),('algoNormal','MINOPAGO = TRUNCAR (MINOPAGO)'),('algoNormal','TIPO = TRUNCAR (TIPO)'),('algoAnnual','IMPORTE = REDONDEAR1 (IMPORTE)'),('algoReg','TIPOREG = TRUNCAR (TIPOREG)'),('algoReg','MINOPAGO = TRUNCAR (MINOPAGO)'),('algoRegAnnual','IMPORTE = REDONDEAR1 (IMPORTE)'),('algoGuard','TIPOREG = TRUNCAR (TIPOREG)')]:
 c('native named call '+k+call,any(call in z['quote'] for z in json.loads((P/'quotes.json').read_text())[k]),True)
c('2 original examples'""")
(P/'check-ledger.py').write_text(s)
