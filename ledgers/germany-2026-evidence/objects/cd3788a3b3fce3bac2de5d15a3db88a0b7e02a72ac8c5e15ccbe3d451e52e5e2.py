from writer import *
import difflib
quote('PR.PAP-KRV',194,246,254,'BMF PAP2026 input KRV')
d=O/'DE-B10-professional-pension-VSP';d.mkdir(exist_ok=True);p=R/'skills/international/germany/de-payroll.md';before=p.read_text();a=next(l for l in before.split('\n') if l.startswith('- Pension:'));b=next(l for l in before.split('\n') if l.startswith('**Other PAP inputs'))
aa='- Pension: pay up to EUR 101,400 x 9.3% for employees compulsorily insured in the statutory pension scheme or exempt under § 6(1) no. 1 SGB VI for a professional pension scheme ([§ 39b(2) sentence 5 no. 3(a) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)). Apply the PAP marker KRV: 0 for compulsory cover in the statutory or a professional pension scheme, or voluntary cover after exemption from compulsory insurance; 1 otherwise.'
bb=b.replace('KRV, PKV','KRV (0 for the qualifying pension-cover branches just described, 1 otherwise), PKV')
options={'finding':'DE-B10','Guide_sha256':sha(p),'exact_before':[a,b],'options':[{'label':'A recommended narrow restoration','exact_after':[aa,bb],'reason':'Restore the omitted professional-scheme branch and identify the actual PAP marker, leaving all arithmetic unchanged.'},{'label':'B shorter marker-only route','exact_after':[a.replace('unless not in the statutory scheme (PAP marker KRV = 1)','where the actual PAP KRV marker is 0; its definition includes qualifying professional-scheme cover'),b],'reason':'Less explicit statutory exemption chain; not selected.'}],'sources':[Q['PR.deduct'],Q['PR.PAP-KRV']],'read_on':DATE,'authorization':'Parent standing authority: save two sourced options then select narrow A in assigned Guide.'}
(d/'two-options-and-evidence.json').write_text(json.dumps(options,ensure_ascii=False,indent=2)+'\n');(d/'de-payroll.before.md').write_text(before)
anchor=next(l for l in before.split('\n') if l.startswith('| Retirement-age pension'));source='| Pension Vorsorgepauschale and professional schemes: EStG § 39b(2) sentence 5 no. 3(a); PAP 2026 KRV definition | https://www.gesetze-im-internet.de/estg/__39b.html ; https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 | 2026-10-29 |'
ops=[{'before':a,'after':aa},{'before':b,'after':bb},{'before':'version: 1.2\n','after':'version: 1.3\n'},{'before':anchor,'after':anchor+'\n'+source}];after=before
for x in ops:assert after.count(x['before'])==1;after=after.replace(x['before'],x['after'])
z=after
for x in reversed(ops):assert z.count(x['after'])==1;z=z.replace(x['after'],x['before'])
assert z==before
same=lambda pat:re.findall(pat,before,re.S)==re.findall(pat,after,re.S)
assert same(r'```oa-check\n.*?```') and same(r'<!-- openaccountants-cta-block -->.*')
u=lambda t:re.findall(r'https?://[^\s)>|]+',t);it=iter(u(after));assert all(any(x==v for x in it) for v in u(before))
assert [l for l in before.split('\n') if l.startswith('## ')]==[l for l in after.split('\n') if l.startswith('## ')]
p.write_text(after);(d/'de-payroll.after.md').write_text(after);(d/'exact-operations.json').write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n');(d/'exact.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True))));(d/'writer-application-proof.json').write_text(json.dumps({'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':sha(p),'full_inverse_exact':True,'old_cases_URL_order_H2_CTA_preserved':True,'operation_count':4,'writer_not_independent':True},indent=2)+'\n');render_quotes();print(sha(p))
