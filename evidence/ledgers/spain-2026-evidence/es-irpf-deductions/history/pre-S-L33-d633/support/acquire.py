from pathlib import Path
import json,runpy,re,hashlib
P=Path(__file__).resolve().parent;E=runpy.run_path(str(P.parent/'es-beckham/ledger-engine.py'));R=E['ROOT'];K=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'](P);b=(R/'skills/international/spain/es-irpf-deductions.md').read_text();us=list(dict.fromkeys(u.split('#')[0] for u in re.findall(r'\]\((https?[^)]+)\)',b) if 'openaccountants' not in u));missing=[]
# Country existing raw/reader pairs: re-use exact URL and bytes, never inferred nearest document.
known=[]
for folder in P.parent.iterdir():
 f=folder/'source-identities.json'
 if folder==P or not f.exists():continue
 for z in json.loads(f.read_text()):known.append((z,folder))
for i,u in enumerate(us):
 try:K.cached('S'+str(i),u);continue
 except Exception:pass
 hit=next(((z,folder) for z,folder in known if z['url']==u),None)
 if hit:z,folder=hit;K.local('S'+str(i),u,folder/z['raw'],folder/z['reader'])
 else:missing.append(dict(key='S'+str(i),url=u))
(P/'url-index.json').write_text(json.dumps(dict(enumerate(us)),indent=2)+'\n');K.save();(P/'missing-cached-sources.json').write_text(json.dumps(missing,indent=2)+'\n');print('Guide',hashlib.sha256(b.encode()).hexdigest(),'pairs',len(K.identities),'missing',len(missing),'uniqueURLs',len(us));print(json.dumps(missing,indent=2))
