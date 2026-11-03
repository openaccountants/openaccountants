import hashlib,json,re,subprocess
from pathlib import Path
root=Path.cwd(); out=root/'evidence/ledgers/malawi-corporate-label-review-20261101'; repair=root/'evidence/ledgers/malawi-corporate-label-repair-20261101'
sha=lambda b:hashlib.sha256(b).hexdigest()
def write(n,v): (out/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def git(path):return subprocess.check_output(['git','show','HEAD:'+path])
manifest=json.loads((repair/'candidate-repair.json').read_text()); guide=manifest['guide']; before=git(guide); actual=(root/guide).read_bytes(); expected=before.decode()
for r in manifest['literal_replacements']:
 assert expected.count(r['before'])==1
 expected=expected.replace(r['before'],r['after'],1)
assert expected.encode()==actual
assert sha(actual)=='8c7103980ebe451c36547efa01dff3da3ef9d5b8461740fe8c81147016ea14d1'
reverse=actual.decode()
for r in reversed(manifest['literal_replacements']):reverse=reverse.replace(r['after'],r['before'],1)
assert reverse.encode()==before
prior=[]
for path,claimed in manifest['prior_malawi_file_sha256'].items():
 base=git(path)
 if path==guide:
  assert sha(base)==claimed
  continue
 work=(root/path).read_bytes() if (root/path).exists() else base
 assert work==base and sha(work)==claimed
 prior.append({'path':path,'sha256':sha(work),'byte_exact':True,'read_from':'working file' if (root/path).exists() else 'unchanged Git object; sparse checkout'})
tracked=subprocess.check_output(['git','diff','--name-only','HEAD']).decode().splitlines();assert tracked==[guide]
old=json.loads((repair/'old-topic-destinations.json').read_text()); blocks=[x for x in before.decode().split('---',2)[2].lstrip('\n').split('\n\n') if x.strip()];assert len(blocks)==34 and blocks==[r['old_text'] for r in old['all_corporate_body_units']]
newblocks=[x for x in actual.decode().split('---',2)[2].lstrip('\n').split('\n\n') if x.strip()];assert len(newblocks)==34
changed=[]
for i,(a,b) in enumerate(zip(blocks,newblocks),1):
 assert sha(a.encode())==old['all_corporate_body_units'][i-1]['old_sha256']
 if a!=b:changed.append(i)
assert changed==[1,11],changed
checks=re.findall(r'```oa-check\n.*?```',before.decode(),re.S); assert checks==re.findall(r'```oa-check\n.*?```',actual.decode(),re.S) and len(checks)==2
assert before.split(b'<!-- openaccountants-cta-block -->')[1]==actual.split(b'<!-- openaccountants-cta-block -->')[1]
write('candidate-preservation.json',{'baseline_head':manifest['baseline_head'],'accepted_guide_sha256':sha(actual),'reverse_literals_restore_exact':True,'tracked_changes_only':[guide],'exact_replacements':manifest['literal_replacements'],'prior_files':prior,'all_old_corporate_body_units':34,'changed_body_units':changed,'all_old_units_destination_checked':True,'corporate_oa_checks_unchanged':2,'full_CTA_unchanged':True,'metadata_only_version_changes':True,'lost_topics':0,'map_probe_note':'Initial pre-CTA-only exploratory block count was28; map covers full body including CTA. Full-body independent reconstruction correctly matches all34 records.'})
source=[]
for name,expectedhash,page,image in [('tax-dec2025','7b88a2aedc98847d243abfcd651869b5ff106df71e06f9cf5f0a9542a306fc46',4,root.parent/'sources/tax-dec2025-page4.png'),('tax-principal','381000c90309e1685cbb6f9e5ee338e14307978e56cf9b50faae2971c45f60e2',86,Path('/tmp/mw-share-independent-review/principal-86.png'))]:
 pdf=root.parent/'sources'/f'{name}.pdf';data=pdf.read_bytes();assert sha(data)==expectedhash
 text=subprocess.check_output(['pdftotext','-f',str(page),'-l',str(page),'-layout',str(pdf),'-']).decode(); (out/f'{name}-p{page}.txt').write_text(text)
 source.append({'source':name,'pdf_sha256':sha(data),'bytes':len(data),'page':page,'independently_extracted_text_sha256':sha(text.encode()),'visually_read_image':str(image),'image_sha256':sha(image.read_bytes()),'read_on':'2026-11-01','scope':'actual narrow original page and neighbours on that page; no full-law/currentness reread','fresh_fetch':False})
write('source-review.json',{'sources':source,'verdicts':[{'id':'C1/S19','verdict':'PASS','reason':'Original Act36p4s5 literally deletes(hb). Neighbouring66B/s6 text confirms this is First Schedule amendment, not an OCR/ledger label.'},{'id':'C2/S20','verdict':'PASS','reason':'Original historical principalp86 has(ha)interest,(hb)deposit interest,(hc)listed-share one-year exemption,(hd)personal/domestic assets. Paragraph-label equivalence is not established.'},{'id':'C3','verdict':'PASS','reason':'Corporate1.4 expressly supports neither removal nor continued availability and holds earlier/straddling gains, consistent with accepted S19/S20 and shareGuide66.'}],'independent_accepted_rows_reopened':2,'other29row_review_not_repeated':True,'new_legal_conclusions':False})
readme=(root/'skills/malawi/README.md').read_text(); changes=[{'before':'No current-year source acceptance or publication approval is claimed.','after':'No current-year or live-use acceptance is claimed. Conditional research publication is accepted only under the focused disposition below; F4 remains open.'},{'before':'Independent review remains unaccepted because the currentness finding is open.','after':'Operative-current-law acceptance remains withheld because F4 is open; conditional research publication is accepted only under the focused disposition below.'},{'before':'Fresh independent review accepts this new job for cited-text fidelity only; F4, currentness, appointed-cutover, live-use, publication and accountant-attestation holds remain.','after':'Fresh independent review accepts this new job for cited-text fidelity only; F4, currentness, appointed-cutover, live-use, publication-currentness and accountant-attestation holds remain.'}]
prospective=readme
for change in changes:assert prospective.count(change['before'])==1;prospective=prospective.replace(change['before'],change['after'],1)
append='''\n## Focused corporate correction and conditional publication\n\nThe [focused independent review](../../evidence/ledgers/malawi-corporate-label-review-20261101/review.md) accepts the corporate v1.4 correction at SHA-256 `8c7103980ebe451c36547efa01dff3da3ef9d5b8461740fe8c81147016ea14d1`. The active corporate Guide now holds the unresolved (hb)/(hc) paragraph chain without approving either removal or continuing exemption. The [additive correction ledger](../../evidence/ledgers/malawi-corporate-label-repair-20261101/correction-ledger.md) supersedes the old corporate ledger row 12 and destination-map removal description for current reading; those historical files remain unchanged.\n\nThe reviewed PR 1216 formation, cross-border and listed-share additions, together with this bounded corporate correction, are accepted for publication as conspicuously conditional, partial source research. This supersedes only the blanket publication nonacceptance in the [earlier focused closure](../../evidence/ledgers/malawi-review-closure-20261101/closure.md), the [Act 3 delta review](../../evidence/ledgers/malawi-act3-review-20261101/review.md) and their corresponding historical README checkpoint wording. Their operative-law and live-use findings remain effective. Historical findings and receipts remain immutable; the older references to no publication acceptance do not bar this conditional research publication.\n\nF4 remains OPEN. Actual appointed TAA/2021 cutover notices including the identified GN 21/23 chain, complete operative/currentness chain, general-law commencement and period allocation, the paragraph-label mismatch and every other stated job hold remain unresolved. All nine Guides retain their live-use stops, and all seven domains remain partial. No operative 2026 position, live calculation, withholding, payment, filing, accountant attestation or country completion is approved. The earlier 67-record/four-case and 29-record/two-case acceptances retain their original boundaries. This is content publication readiness only; required GitHub checks and a genuine native approving review remain separate merge gates.\n'''
prospective+=append
write('permitted-readme-status.json',{'status':'prospective exact literals only; reviewer did not edit README','path':'skills/malawi/README.md','before_sha256':sha(readme.encode()),'literal_replacements':changes,'append_exactly':append,'expected_after_sha256':sha(prospective.encode()),'expected_after_git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=prospective.encode()).decode().strip(),'restrictions':'Apply each once and append once; no rules, figures, examples, trust fields, hold removal, partial-domain change or historical receipt edits authorised. Preserve a separate parent reconciliation receipt.'})
(out/'prospective-README.md.txt').write_text(prospective)
print(json.dumps({'accepted_guide_sha256':sha(actual),'prior_files_exact':len(prior),'old_body_units':34,'changed_units':changed,'readme_before':sha(readme.encode()),'readme_expected_after':sha(prospective.encode())}))
