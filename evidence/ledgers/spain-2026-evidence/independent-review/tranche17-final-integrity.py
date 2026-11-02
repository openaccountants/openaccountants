from pathlib import Path
import json,hashlib,re
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');E=W/'ledgers/spain-2026-evidence/es-foral-income-tax';O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();N=lambda s:' '.join(s.split())
rows=json.loads((E/'rows.json').read_text());sc={z['row']:z for z in json.loads((E/'actual-source-read-scopes.json').read_text())['rows']};bad=[];ell=0;readerids={}
for x in rows:
 s=sc[x['id']];p=Path(s['reader']);p=p if p.is_absolute() else W/p
 readerids[str(p)]=H(p)==s['reader_sha256'];lines=p.read_text().split('\n');parts=s.get('native_quote_parts',[s]);t=N(' '.join('\n'.join(lines[z['LF_start']-1:z['LF_end']]) for z in parts));qs=re.split(r'\[\s*(?:…|\.\.\.)\s*\]',x['quote']);pos=0
 if len(qs)>1:ell+=1
 for q in qs:
  q=N(q)
  if not q:continue
  k=t.find(q,pos)
  if k<0:bad.append(x['id']);break
  pos=k+len(q)
assert not bad,bad
assert all(readerids.values())
initial=json.loads((E/'history-f80fe1e2-before-S-L26/rows.json').read_text());old={z['id']:z for z in initial};now={z['id']:z for z in rows};removed=sorted(set(old)-set(now));changed=[i for i in now if old[i]!=now[i]]
assert removed==list(range(2409,2556));assert changed==[72,74,76,109,111,113,225,918,919,920,1295,1315],changed
for s in ['S-L26','S-L27','S-L28','S-L29','S-L30','S-L31','S-L32']:
 proof=json.loads((E/(s+'-exact-replacements.json')).read_text());assert proof['exact_inverse']
prev=E/'history-74df1985-before-S-L32';pre=json.loads((prev/'rows.json').read_text());assert [z for z in pre if z['id'] not in removed]==rows
map32=json.loads((E/'S-L32-removal-disposition-map.json').read_text());assert H(E/'S-L32-removal-disposition-map.json')=='1fba650e7397fa2f030000c1a101e64c2d51f2f84f99abdf67fa8ae1545eb7d5'
hand=json.loads((E/'handover.json').read_text());hp=[]
for z in hand:
 p=W/z['path'];hp.append({'path':z['path'],'sha256':H(p),'pass':H(p)==z['sha256']})
assert all(z['pass'] for z in hp)
guide=W/'skills/international/spain/es-foral-income-tax.md';assert H(guide)=='67f9038dc36b4ae6809d235c1bb4fa881ee96b411123657edf359e5c84e109de';assert guide.read_bytes()==(E/'frozen-guide.txt').read_bytes()
ledger=W/'ledgers/es-foral-income-tax.md';assert H(ledger)=='75f77f9a374ee3730b7d061e2b30cc7228294dcaca5f8135e33e534c71de2aca'
res={'guide_sha256':H(guide),'ledger_sha256':H(ledger),'current_rows':len(rows),'all_nativeLF_quote_matches':True,'explicit_ellipsis_rows':ell,'distinct_current_readers':len(readerids),'reader_hash_mismatches':[],'initial_rows':len(initial),'changed_retained_ids':changed,'unchanged_retained_rows':len(rows)-len(changed),'removed_reference_only_ids':[2409,2555],'removed_count':len(removed),'scope_row1315':'two separate native parts checked in order, not continuous reading','rule_wordings':len(set(z['guide_wording'] for z in rows)),'non_rules':len(json.loads((E/'non-rule-dispositions.json').read_text())['dispositions']),'handover_checks':hp,'history_inverse_records_rehashed':[{'file':s+'-exact-replacements.json','sha256':H(E/(s+'-exact-replacements.json'))} for s in ['S-L26','S-L27','S-L28','S-L29','S-L30','S-L31','S-L32']]}
(O/'tranche17-final-integrity.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ['handover_checks','history_inverse_records_rehashed']})
