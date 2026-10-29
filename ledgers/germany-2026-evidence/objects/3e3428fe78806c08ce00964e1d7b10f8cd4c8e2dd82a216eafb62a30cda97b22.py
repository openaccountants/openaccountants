from pathlib import Path
import json,re,hashlib,difflib
P=Path(__file__).resolve().parent;R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');ops=json.loads((P/'exact-operations.json').read_text());h=lambda s:hashlib.sha256(s if isinstance(s,bytes) else s.encode()).hexdigest();proof={}
for slug,oo in ops.items():
 p=R/'skills/international/germany'/f'{slug}.md';old=(P/'before'/p.name).read_text();current=p.read_text();new=old;prefixes=[old]
 for o in oo:
  assert new.count(o['old'])==1,(slug,o['reason']);new=new.replace(o['old'],o['new'],1);prefixes.append(new)
 inverse=new
 for o in reversed(oo):assert inverse.count(o['new'])==1;inverse=inverse.replace(o['new'],o['old'],1)
 assert inverse==old
 blocks=lambda t:re.findall(r'```oa-(?:check|example)\b.*?```',t,re.S)
 assert blocks(old)==blocks(new),(slug,'oa changed')
 # Preserve full original worked-example prose as well as executable blocks.
 headings=list(re.finditer(r'^## .+$',old,re.M));examples=[]
 for i,m in enumerate(headings):
  if 'example' in m.group().lower():
   end=headings[i+1].start() if i+1<len(headings) else len(old);segment=old[m.start():end];assert segment in new;examples.append(h(segment))
 fm=lambda t:t.split('---',2)[1];ofm=fm(old);nfm=fm(new);assert re.sub(r'(?m)^(version|last_updated): .+$',r'\1: <content-version-or-date>',ofm)==re.sub(r'(?m)^(version|last_updated): .+$',r'\1: <content-version-or-date>',nfm)
 urls=lambda t:re.findall(r'https?://[^\s<>|)]+',t)
 prior=iter(urls(new));assert all(any(y==x for y in prior) for x in urls(old))
 # Full content after intake CTA marker/contribution remains exact.
 for marker in ['<!-- openaccountants-cta-block -->','<!-- openaccountants-cta-block -->']:
  if marker in old:assert old[old.index(marker):]==new[new.index(marker):]
 assert [x for x in old.split('\n') if x.startswith('> Contributed')]==[x for x in new.split('\n') if x.startswith('> Contributed')]
 prior=(P/'first-four-preservation-proof.json'); priorproof=json.loads(prior.read_text()) if prior.exists() else {}; assert current in prefixes or h(current)==priorproof.get(slug,{}).get('after_sha256'),(slug,'baseline drift'); (P/'after'/p.name).write_text(new);p.write_text(new)
 (P/'support'/f'{slug}.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before/'+slug,tofile='after/'+slug)))
 sm=difflib.SequenceMatcher(a=old.split('\n'),b=new.split('\n'),autojunk=False);lm={}
 for tag,a,b,c,d in sm.get_opcodes():
  if tag=='equal':
   for x in range(a,b):lm[str(x+1)]={'start':c+x-a+1,'end':c+x-a+1,'disposition':'byte-exact old line'}
  elif tag=='replace':
   for x in range(a,b):lm[str(x+1)]={'start':c+1,'end':d,'disposition':'bounded finding correction; exact old/new text in operations and diff'}
  elif tag=='delete':raise AssertionError((slug,'unexpected deletion'))
 (P/'support'/f'{slug}.line-map.json').write_text(json.dumps(lm,indent=2)+'\n')
 proof[slug]={'path':str(p),'before_sha256':h(old),'after_sha256':h(new),'bytes':len(new.encode()),'operations':len(oo),'full_inverse':True,'original_executable_blocks':len(blocks(old)),'original_executable_blocks_exact':True,'original_full_worked_example_sections_sha256':examples,'original_full_worked_examples_exact':True,'protected_frontmatter_exact_except_content_version_and_date':True,'original_URL_occurrences_preserved_in_order':True,'attribution_CTA_exact':True,'native_line_map':str(P/'support'/f'{slug}.line-map.json')}
(P/'preservation-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
