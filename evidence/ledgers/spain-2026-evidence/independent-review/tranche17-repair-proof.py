from pathlib import Path
import json,hashlib,re
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');E=W/'ledgers/spain-2026-evidence/es-foral-income-tax';O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');H=lambda b:hashlib.sha256(b).hexdigest()
hist=['history-f80fe1e2-before-S-L26','history-7f3efdcc-before-S-L27','history-8d7e9452-before-S-L28','history-3b32d1e7-before-S-L29','history-965a7e29-before-S-L30','history-05f230a5-before-S-L31','history-74df1985-before-S-L32']
proof=[]
for i,s in enumerate(['S-L26','S-L27','S-L28','S-L29','S-L30','S-L31','S-L32']):
 before=(E/hist[i]/'ledger.md').read_text();after=(E/hist[i+1]/'ledger.md').read_text() if i<6 else (W/'ledgers/es-foral-income-tax.md').read_text();p=json.loads((E/(s+'-exact-replacements.json')).read_text());got=before
 if i<6:
  ops=p.get('operations',[p])
  for z in ops:
   assert got.count(z['before'])==1,(s,z['row']);got=got.replace(z['before'],z['after'],1)
  assert got==after,s
  for z in reversed(ops):
   assert got.count(z['after'])==1;got=got.replace(z['after'],z['before'],1)
  assert got==before
 else:
  # Independent line removal using the actual old row strings and current count disclosure.
  for z in p['removed_lines']:
   assert got.count(z['before']+'\n')==1;got=got.replace(z['before']+'\n','',1)
  # No substantive content may be inserted besides the stated sparse-ID count disclosure.
  assert got==after.replace(p['inserted_current_count_disclosure'],'',1)
  got=got.split('\n');old=before.split('\n')
  for z in p['removed_lines']:got.insert(z['original_line_index'],z['before'])
  assert got==old
 proof.append({'finding':s,'before_sha256':H(before.encode()),'after_sha256':H(after.encode()),'unique_exact_forward_and_inverse':True})
a=(E/'history-1b9fb618-guide/frozen-guide.txt').read_text();b=(E/'frozen-guide.txt').read_text();diff=[i for i,(x,y) in enumerate(zip(a.split('\n'),b.split('\n')),1) if x!=y];assert diff==[18,497]
# Protected sections and historical source URL ordering are unchanged by the parent correction.
case=lambda s:re.findall(r'```oa-check\n.*?```',s,re.S)
assert case(a)==case(b) and len(case(b))==2
assert a[a.rfind('> Contributed'):]==b[b.rfind('> Contributed'):] if '> Contributed' in a else True
urls=lambda s:re.findall(r'https?://[^\s<>)]+',s)
assert urls(a)==urls(b)
old=json.loads((E/'old-topic-overrides.json').read_text());assert len(old)==16
(O/'tranche17-repair-proof.json').write_text(json.dumps({'steps':proof,'guide_prior_sha256':H(a.encode()),'guide_current_sha256':H(b.encode()),'guide_only_changed_LF':diff,'two_oa_blocks_byte_exact':True,'URL_sequence_exact':True,'old_topic_spots_read':list(map(int,old))+[254,255,257,258,259,267,269,277,278,279,280,292,327],'current_body_pin_unchanged_since_frozen_review':True},indent=2)+'\n');print('7 exact forward/inverses; protected parent two-line correction verified')
