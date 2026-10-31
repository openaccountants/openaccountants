from pathlib import Path
import json,re,hashlib
p=Path('ledgers/spain-2026-evidence/es-foral-income-tax');path=Path('ledgers/es-foral-income-tax.md');t=path.read_text();rows=json.loads((p/'rows.json').read_text());units=json.loads((p/'all-guide-units.json').read_text());covered={z['guide_LF']for z in rows};dispositions={};pending=[]
headers={33,50,75,76,86,87,104,105,183,220,221,231,232,255,256,280,281,345,361,429,430,443,444,460,461,493,494,512,513,524,525,542,543,559,560,571,572,601,602,613,614,703,747}
pointers={119,407,565,639,649,669,679,691}
for z in units:
 lf=z['line']
 if lf in covered:continue
 if lf in headers:dispositions[lf]='Table column heading/separator; no independently asserted tax figure. Governing body rows are separately quoted.'
 elif lf in pointers:dispositions[lf]='Primary-source pointer only; governing substantive paragraph/table rows immediately above carry the quotation chain. No additional legal rule or amount introduced.'
 elif lf in[835,836,837,838,839,841]:dispositions[lf]='Client intake/evidence question; no asserted tax computation.'
 elif lf==714:dispositions[lf]='Explicit retained implementation/source limitation. Not a positive tax calculation or an inferred zero; detailed territory rows701–712 preserve the supplied scope and ordinary residuals.'
 else:pending.append(lf)
lines=t.splitlines()
for i,line in enumerate(lines):
 m=re.match(r'^\| (\d+) \|',line)
 if m and int(m[1])in dispositions and '| Evidence gaps'not in line:
  # Only disposition-table lines have four unescaped columns, unlike quote rows / old-topic rows.
  parts=re.split(r'(?<!\\)\|',line)
  if len(parts)==6 and parts[2].strip().startswith(('The base','Deadlines','Ask','Cross-border')):parts[-2]=' '+dispositions[int(m[1])]+' ';lines[i]='|'.join(parts)
lines[1]=lines[1].replace('; HEAD0b5e62451de50220ac6d80c7813d547d08108641.', '; initial freeze HEAD0b5e62451de50220ac6d80c7813d547d08108641; current bound body includes the parent’s bounded v0.7 Gipuzkoa charity-base correction. The original1b9fb618 Guide/identity/rows are retained underhistory-1b9fb618-guide. No claim that the repaired body was already in that initial commit.')
path.write_text('\n'.join(lines)+'\n');(p/'non-rule-dispositions.json').write_text(json.dumps({'dispositions':dispositions,'pending_substantive_units':pending},ensure_ascii=False,indent=2)+'\n');print('explicitnonrules',len(dispositions),'pending',pending)
