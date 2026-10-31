from pathlib import Path
import json,runpy
P=Path(__file__).resolve().parent;K=runpy.run_path(str(P.parent/'es-modelo-111/source-kit.py'))['Kit'](P)
for z in json.loads((P/'source-identities.json').read_text()):K.local(z['key'],z['url'],P/z['raw'],P/z['reader'])
rows=json.loads((P/'missing-source-locator-records.json').read_text());missing=[];chosen=[]
for m in json.loads((P/'missing-cached-sources.json').read_text()):
 hit=None
 for filename,z in rows:
  if m['url'] not in z.values():continue
  parent=Path(filename).parent
  raw=z.get('raw_path') or z.get('raw') or z.get('retained_path') or z.get('path');reader=z.get('reader_path') or z.get('reader')
  if isinstance(raw,dict):raw=raw.get('path')
  if isinstance(reader,dict):reader=reader.get('path')
  if not isinstance(raw,str):continue
  raw=Path(raw);raw=raw if raw.is_absolute() else parent/raw
  if not raw.exists():continue
  if isinstance(reader,str):reader=Path(reader);reader=reader if reader.is_absolute() else parent/reader
  else:
   candidates=[raw.with_suffix('.reader.txt'),Path(str(raw)+'.reader.txt'),raw.with_suffix('.txt')]
   if 'AX' in raw.name:candidates.insert(0,raw)
   reader=next((p for p in candidates if p.exists()),None)
  if reader and reader.exists():hit=(raw,reader,filename,z);break
 if hit:
  raw,reader,f,z=hit;K.local(m['key'],m['url'],raw,reader);chosen.append(dict(key=m['key'],url=m['url'],record=f,raw=str(raw),reader=str(reader),capture_kind='official browser AX, not HTTP response' if raw==reader else 'retained raw and separate reader'))
 else:missing.append(m)
K.save();(P/'additional-cache-locators.json').write_text(json.dumps(chosen,indent=2)+'\n');(P/'missing-cached-sources-final.json').write_text(json.dumps(missing,indent=2)+'\n');print('allpairs',len(K.identities),'remaining',missing)
