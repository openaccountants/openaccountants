import sys,json,hashlib,subprocess
from pathlib import Path
slug=sys.argv[1];p=Path('ledgers/spain-2026-evidence')/slug;rows=json.loads((p/'rows.json').read_text());units=json.loads((p/'all-guide-units.json').read_text());covered={r['guide_LF']for r in rows};remaining=[u for u in units if u['line']not in covered];body=(p/'frozen-guide.txt').read_text();now=Path('skills/international/spain')/(slug+'.md');assert now.read_text()==body
out=subprocess.run(['python3','scripts/check-examples.py',str(now)],capture_output=True,text=True);(p/'example-check.txt').write_text(out.stdout+out.stderr);assert out.returncode==0
(p/'writer-status.md').write_text(f'''# {slug}: writer handover

Frozen HEAD 0b5e62451de50220ac6d80c7813d547d08108641. {len(rows)} source-quotation rows. The full current body inventory is in all-guide-units.json; {len(remaining)} unquoted units are table headings/workflow introductions or client questions. Every substantive legal/numeric paragraph/table unit is represented, sometimes by several quotations. A represented compound paragraph is not a claim that one excerpt alone proves every condition: read the additional rows and the exact provision scopes together. Actual original-language quotations were read on 28 October 2026 from pinned retained sources. Tables preserve exact statutory cells; hypothetical inputs and computed outputs are labelled. No new law is inferred from the presence of a downloaded source.

Old-topic table uses actual retained main where available. Otherwise the table explicitly identifies the earliest branch body as an additional comparator, not a previously published main. Changed or unsupported old wording is not represented as exact preservation. Existing source conflicts and precise ordinary reservations are carried in the frozen scope. Both original oa-check blocks pass (example-check.txt); this is a selected Guide check, not a repeated whole-pack audit. No Guide, Git state, generated content or platform content was changed.

Writer evidence is ready for a different reviewer. It is not independent PASS, accountant attestation or country completion.
''')
files=[Path('ledgers')/(slug+'.md'),p/'rows.json',p/'source-read-receipts.json',p/'writer-status.md',p/'example-check.txt']
record=[{'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size}for f in files];(p/'handover.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
