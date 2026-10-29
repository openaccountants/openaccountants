from writer import *
import datetime,difflib
p=R/'skills/international/germany/de-payroll.md';d=O/'DE-B09-retirement-branch-distinction';choice=json.loads((d/'two-options-and-evidence.json').read_text());before=p.read_text();assert sha(p)==choice['Guide_sha256'];bp=d/'de-payroll.before.md';assert not bp.exists();bp.write_text(before)
source='| Retirement-age pension and unemployment distinction: SGB VI § 5(4), § 172(1); SGB III § 28(1) no. 1, § 346(3) | https://www.gesetze-im-internet.de/sgb_6/__5.html ; https://www.gesetze-im-internet.de/sgb_3/__28.html ; https://www.gesetze-im-internet.de/sgb_6/__172.html ; https://www.gesetze-im-internet.de/sgb_3/__346.html | 2026-10-29 |'
anchor=next(l for l in before.split('\n') if l.startswith('| Minimum wage regulation MiLoV4'))
ops=[{'before':choice['exact_before'],'after':choice['options'][0]['exact_after']},{'before':'version: 1.1\n','after':'version: 1.2\n'},{'before':'last_updated: 2026-10-26\n','after':'last_updated: 2026-10-29\n'},{'before':anchor,'after':anchor+'\n'+source}]
after=before
for op in ops:assert after.count(op['before'])==1;after=after.replace(op['before'],op['after'])
z=after
for op in reversed(ops):assert z.count(op['after'])==1;z=z.replace(op['after'],op['before'])
assert z==before
oa=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S);assert len(oa(before))==2 and oa(before)==oa(after)
url=lambda t:re.findall(r'https?://[^\s)>|]+',t);it=iter(url(after));assert all(any(x==u for x in it) for u in url(before))
fm=lambda t:dict(re.findall(r'^(\w+): (.*)$',t.split('---',2)[1],re.M));a,b=fm(before),fm(after);assert {k:v for k,v in a.items() if k not in ['version','last_updated']}=={k:v for k,v in b.items() if k not in ['version','last_updated']}
cta=lambda t:t[t.index('<!-- openaccountants-cta-block -->'):];assert cta(before)==cta(after);assert [l for l in before.split('\n') if l.startswith('## ')]==[l for l in after.split('\n') if l.startswith('## ')]
p.write_text(after);(d/'de-payroll.after.md').write_text(after);(d/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(d/'exact.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='de-payroll.before.md',tofile='de-payroll.after.md')));(d/'writer-application-proof.json').write_text(json.dumps({'root_selected':'Option A, explicit parent delegation2026-10-29; no concurrent root edits to sevenBGuides','before_sha256':sha(bp),'after_sha256':sha(p),'operations':len(ops),'full_inverse_exact':True,'original_oa_blocks':2,'oa_bytes_exact':True,'old_URL_order_preserved':True,'protected_metadata_exact':True,'H2_order_exact':True,'CTA_exact':True,'writer_not_independent':True},indent=2)+'\n');print(sha(p))
