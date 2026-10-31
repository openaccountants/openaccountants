from pathlib import Path
import json,runpy,re
P=Path(__file__).resolve().parent;Kit=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'];K=Kit(P);R=P.parents[2];b=(R/'skills/international/spain/es-social-contributions.md').read_text();us=list(dict.fromkeys(u.split('#')[0] for u in re.findall(r'\]\((https?[^)]+)\)',b) if 'openaccountants' not in u));missing=[]
for i,u in enumerate(us):
 if 'eur-lex' in u:continue
 try:K.cached('S'+str(i),u)
 except Exception as e:missing.append([i,u,str(e)])
K.save();(P/'url-index.json').write_text(json.dumps(dict(enumerate(us)),indent=2)+'\n');print('acquired',len(K.identities),'missing',missing)
