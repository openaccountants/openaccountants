from pathlib import Path
import json,runpy,re
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];Kit=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'];K=Kit(P);b=(R/'skills/international/spain/es-income-tax.md').read_text();us=list(dict.fromkeys(u.split('#')[0] for u in re.findall(r'\]\((https?[^)]+)\)',b) if 'openaccountants' not in u));missing=[]
for i,u in enumerate(us):
 try:K.cached('S'+str(i),u)
 except Exception as e:missing.append([i,u,str(e)])
(P/'url-index.json').write_text(json.dumps(dict(enumerate(us)),indent=2)+'\n');K.save();print('sourcepairs',len(K.identities),'missing',missing)
