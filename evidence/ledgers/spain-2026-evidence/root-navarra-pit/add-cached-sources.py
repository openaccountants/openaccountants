from pathlib import Path
import json,re,runpy,hashlib,shutil
P=Path(__file__).resolve().parent;repo=P.parents[2];m=runpy.run_path(str(repo/'ledgers/spain-2026-evidence/group-b-ledger-lib.py'));g=(repo/'skills/international/spain/es-foral-income-tax.md').read_text();ids=json.loads((P/'source-identities.json').read_text());errors=[]
urls={}
for label,u in re.findall(r'\[([^]]+)\]\((https?://[^\s]+)\)',g):
 for key in ['HL','HR','E','S26','HC','DS','ES']:
  if label==key+': official housing/IRPF source':urls[key]=u
urls['IPREM2026']='https://vivienda.castillalamancha.es/iprem'
urls['LPGE']='https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128'
urls['CIT']='https://www.boe.es/buscar/act.php?id=BOE-A-2017-2356'
for key,u in urls.items():
 if any(x['key']==key for x in ids):continue
 try:
  x=m['source'](u);z=dict(key=key,label=key,url=u,original_raw=x['raw'],original_reader=x['reader'],acquired='2026-10-28')
  for kind,s,ext in [('raw',x['raw'],'.body'),('reader',x['reader'],'.reader.txt')]:
   dst=P/'sources'/(key+ext);shutil.copyfile(s,dst);z[kind]=str(dst.relative_to(P));z[kind+'_sha256']=hashlib.sha256(dst.read_bytes()).hexdigest()
  ids.append(z)
 except Exception as e:errors.append([key,u,str(e)])
(P/'source-identities.json').write_text(json.dumps(ids,ensure_ascii=False,indent=2)+'\n');(P/'source-add-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2)+'\n');print('new sources',len(urls),'errors',errors)
