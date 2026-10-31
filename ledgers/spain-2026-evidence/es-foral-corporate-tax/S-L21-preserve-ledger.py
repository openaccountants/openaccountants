from pathlib import Path
import json,hashlib
p=Path('ledgers/spain-2026-evidence/es-foral-corporate-tax');out=Path('ledgers/es-foral-corporate-tax.md');old=(p/'history-1000ad1a-before-S-L21/ledger.md').read_text();fresh=out.read_text();ops=[]
for i in[785,789]:
 a=next(x for x in old.splitlines()if x.startswith('| '+str(i)+' |'));b=next(x for x in fresh.splitlines()if x.startswith('| '+str(i)+' |'));assert old.count(a)==1;ops.append({'row':i,'before':a,'after':b});old=old.replace(a,b)
out.write_text(old);(p/'S-L21-exact-ledger-replacements.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');print(hashlib.sha256(out.read_bytes()).hexdigest())
