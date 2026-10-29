from pathlib import Path
import urllib.request,json,re,hashlib,concurrent.futures
O=Path(__file__).resolve().parent;P=O/'targeted-sources';P.mkdir(exist_ok=True);M=json.loads((O/'selected-existing-evidence-map.json').read_text());C=json.loads((O/'source-candidate-catalog.json').read_text())
urls=sorted(set(u for g in M for u in g['cited_URLs'] if u not in C and re.match(r'https://www.gesetze-im-internet.de/[^/]+/(?:__|art_)',u)))
urls += ['https://www.gesetze-im-internet.de/estg/__25.html'] if 'https://www.gesetze-im-internet.de/estg/__25.html' not in urls and 'https://www.gesetze-im-internet.de/estg/__25.html' not in C else []
def f(u):
 name=re.sub('[^a-zA-Z0-9.-]+','-',u.split('gesetze-im-internet.de/')[1]);path=P/name
 d={'official_url':u,'date':'2026-10-29','reason':'Specific missing operative citation in an assigned frozen Guide, not a broad source search. Acquisitiononly; actualreadingseparate.'}
 try:
  with urllib.request.urlopen(u,timeout=30) as r:b=r.read();d.update({'status':r.status,'final_url':r.url,'raw_path':str(path),'raw_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
  path.write_bytes(b)
 except Exception as e:d['error']=repr(e)
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(f,urls))
(P/'named-citation-acquisition-receipts.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'namedmissingcitations attempted;success',sum(x.get('status')==200 for x in rows));print([x for x in rows if 'error'in x])
