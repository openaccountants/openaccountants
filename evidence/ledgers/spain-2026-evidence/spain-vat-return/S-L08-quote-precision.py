from pathlib import Path
import json,hashlib,shutil,runpy
m=runpy.run_path('ledgers/spain-2026-evidence/group-b-ledger-lib.py');PDF='https://www.boe.es/boe/dias/2026/01/26/pdfs/BOE-A-2026-1761.pdf';q=m['snippet'](PDF,'Por cuotas soportadas en operaciones interiores corrientes',900)
assert '38 39' in q
for slug,sha in [('spain-vat-return','8f9c3a82'),('es-vat-return','339c7368')]:
 p=Path('ledgers/spain-2026-evidence')/slug;l=Path('ledgers')/(slug+'.md');h=p/('history-'+sha+'-S-L08');h.mkdir(exist_ok=True)
 for f in [l,p/'rows.json',p/'handover.json']:
  if not (h/f.name).exists():shutil.copy2(f,h/f.name)
 rows=json.loads((p/'rows.json').read_text());s=l.read_text();changed=[]
 for row in rows:
  if any(x in row['provision']for x in ['currentimports','intracommunitycurrentinput','domesticcapital','importcapital','intracommunitycapital']):
   old=row['quote'];s=s.replace(old.replace('|','\\|'),q.replace('|','\\|'));row['quote']=q;changed.append(row['id'])
 l.write_text(s);(p/'rows.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
 (p/'S-L08-disposition.json').write_text(json.dumps(dict(changed_rows=changed,source=PDF,reader='303-selected-pages12-and14.reader.txt',actual_read='Selected reader LF72–77, including actual 38/39 at LF77; approved PDF page12 rendered image visually reread 2026-10-28. Original extracted otal remains exact at LF68/83, not silently normalised.',quote=q),indent=2,ensure_ascii=False)+'\n')
