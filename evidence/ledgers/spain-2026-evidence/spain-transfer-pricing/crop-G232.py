import pdfplumber,hashlib,json
from pathlib import Path
p=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-fresh-whole-pack-review-0f104150/sources/fe5409c75fbb0b81c8bc.body');out=Path(__file__).parent/'G232-right-column.reader.txt';parts=[]
with pdfplumber.open(p)as doc:
 for i,page in enumerate(doc.pages):parts.append(f'PAGE {i+1}\n'+(page.crop((page.width/2,0,page.width,page.height)).extract_text()or''))
out.write_text('\n\n'.join(parts));out.with_suffix('.json').write_text(json.dumps({'raw':str(p),'raw_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'reader_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'derivation':'pdfplumber right-half crop of bilingual pages; raw unchanged; original-language Spanish only; page markers added'},indent=2));print(out)
