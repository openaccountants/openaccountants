from pathlib import Path
import hashlib,json,re,subprocess,os,sys
R=Path.cwd(); E=R/'evidence/ledgers/malawi-share-review-20261101'; W=R/'evidence/ledgers/malawi-share-withholding-20261101'; S=R.parent/'sources'
HEAD='245cc5692e07d82581cbbfdf7b1255c776e2f7f4'; CONTENT='c28f56992498fad54901da39966ff87af897da84'; BASE='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'; PRIOR='067535f8a04a85f74271816950766a46b7541a15'
def git(*args):return subprocess.run(['git',*args],capture_output=True,check=True).stdout
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,v):(E/n).write_text(json.dumps(v,indent=2)+'\n')
assert git('rev-parse','HEAD').decode().strip()==HEAD
assert git('merge-base',HEAD,'origin/main').decode().strip()==BASE
baseline=json.loads((W/'baseline.json').read_text()); preserved=[]
for p,expected in baseline['prior_guide_and_evidence_sha256'].items():
 prior=git('show',PRIOR+':'+p); current=git('show',HEAD+':'+p)
 assert sha(prior)==expected and prior==current
 if (R/p).exists():assert (R/p).read_bytes()==current
 preserved.append({'path':p,'sha256':expected,'prior_blob_sha256':sha(prior),'reviewed_head_sha256':sha(current),'equal':True})
assert len(preserved)==60
old=json.loads((W/'old-topics.json').read_text()); rows=old['complete_old_body_units']; independently=[]
for p in sorted(set(x['old_file'] for x in rows)):
 text=git('show',PRIOR+':'+p).decode(); lines=text.splitlines(); boundary=next(i for i,l in enumerate(lines[1:],1) if l=='---')+1
 # Reconstruct nonempty body blocks from actual pinned Git lines, independent of the writer's map.
 blocks=[]; start=None
 for i in range(boundary,len(lines)+1):
  if i<len(lines) and lines[i].strip():
   if start is None:start=i
  elif start is not None:
   blocks.append((start+1,'\n'.join(lines[start:i])+('\n' if i==len(lines) and text.endswith('\n') else '')));start=None
 mapped=[x for x in rows if x['old_file']==p]
 assert len(blocks)==len(mapped)
 for (line,txt),m in zip(blocks,mapped):
  assert txt==m['old_text'] and line==m['old_line'] and sha(txt.encode())==m['sha256']
  assert m['destination']==p+'#L'+str(line)
  assert git('show',HEAD+':'+p).decode().splitlines()[line-1:line-1+len(txt.splitlines())]==txt.splitlines()
  independently.append({'old_file':p,'unit':m['unit'],'line':line,'sha256':sha(txt.encode()),'destination':m['destination'],'verdict':'exact retained destination'})
assert len(independently)==257
write('old-topics.json',{'baseline':PRIOR,'reviewed_head':HEAD,'independently_reconstructed_units':len(independently),'lost_content':0,'units':independently})
readme=(R/'skills/malawi/README.md').read_text(); oldread=git('show',PRIOR+':skills/malawi/README.md').decode(); restored=readme.split('\n## Listed-share withholding draft backup\n')[0].replace('IT-IND: [mw-income-tax, mw-listed-share-withholding]','IT-IND: [mw-income-tax]').replace('IT-CORP: [mw-corporate-income-tax, mw-listed-share-withholding]','IT-CORP: [mw-corporate-income-tax]');assert restored==oldread
new=(R/'skills/malawi/mw-listed-share-withholding.md').read_bytes(); assert sha(new)=='dadf1168b02e6983ba5f5eb5704f93f99aef70ef01b57b43ece40cb33963309c'
for f in ['review_status:','trust_label:','license:','verified_by:','reviewed_by:','reviewed_on:','openaccountants-cta-block']:assert f.encode() not in new
changed=git('diff','--name-only',PRIOR,HEAD).decode().splitlines(); assert all(p in ['skills/malawi/README.md','skills/malawi/mw-listed-share-withholding.md'] or p.startswith('evidence/ledgers/malawi-share-withholding-20261101/') for p in changed)
write('frozen-and-preservation.json',{'head':HEAD,'content_head':CONTENT,'actual_full_merge_base':BASE,'accepted_prior_head':PRIOR,'guide_sha256':sha(new),'readme_sha256':sha(readme.encode()),'eight_prior_guides_and_52_evidence_exact':True,'all_prior_preserved':preserved,'old_body_units':257,'readme_restored_exact':True,'all_seven_partial_declarations_preserved':True,'no_platform_fields_or_cta_added':True,'no_figure_owner_move':True,'changed_paths_since_prior':changed,'scope':'source fidelity only; F4/currentness/appointed cutover/live-use/publication/accountant holds retained'})
manifest=json.loads((W/'source-read-manifest.json').read_text()); sources=[]
for m in manifest:
 p=S/(m['source']+'.pdf');b=p.read_bytes();reader=S/m['reader']; assert sha(b)==m['pdf_sha256'] and len(b)==m['pdf_bytes'] and sha(reader.read_bytes())==m['reader_sha256']
 sources.append({'source':m['source'],'official_url':m['official_url'],'pdf_sha256':sha(b),'pdf_bytes':len(b),'reader_sha256':sha(reader.read_bytes()),'read_on':'2026-11-01','acquisition':'existing original PDF cache; no fresh remote download claimed','reviewer_scope':m['actually_read_scope'] if m['source'] not in ['tax-principal','taa-2021'] else ({'tax-principal':'Definitions adjusted basis/amount realized/basis/capital asset/gain/loss/disposal pp9–11; ss11–14/opening15 pp19–20; s102A and ss103–104A pp70–71; First Schedule pp84–86; Fourteenth Schedule pp110–112; withholding regulations1–7/opening8 pp124–127. Principal86 and70 independently rendered and visually read.','taa-2021':'s1 and opening2; selected definitions pp8–9; ss60–63 and neighbouring payment text pp42–45; s73 with adjacent72/74 pp51–53; ss128–129 pp79–80.'}[m['source']]),'fresh_current_law_acceptance':False})
visuals=[]
for p in [S/'taxation-act3-2026-media-ocr/page-5.png',S/'taxation-act3-2026-media-ocr/page-6.png',S/'tax-dec2025-page4.png',Path('/tmp/mw-share-independent-review/principal-86.png'),Path('/tmp/mw-share-independent-review/principal-70.png'),Path('/tmp/mw-share-independent-review/act3-1.png')]:visuals.append({'path':str(p),'sha256':sha(p.read_bytes()),'read_on':'2026-11-01','actually_visually_read':True})
write('source-reads.json',{'sources':sources,'visual_pages':visuals,'appointed_notices_read':False,'current_law_acceptance':False,'scope_caveat':'Manifest scope is selected source-text review, not proof of every intervening amendment. Cached original PDFs, readers and decisive scans were read; no new download or full-current-law survey claimed.'})
# Actual committed validators. No writer receipt is run or overwritten.
env=os.environ.copy();env['PYTHONPATH']='/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps'; receipt={'head':HEAD,'base':BASE,'commands':[]}
commands=[['python3','scripts/skill_checks.py','skills/malawi/mw-listed-share-withholding.md'],['python3','scripts/check-examples.py','--require','skills/malawi/mw-listed-share-withholding.md','skills/malawi/mw-company-formation.md','skills/malawi/mw-cross-border-tax.md'],['python3','scripts/check-sync-integrity.py','--base',BASE,'--strict-metadata','--head',HEAD],['python3','scripts/validate-guides.py','--changed-only','--no-index-check'],['git','diff','--check',BASE,HEAD]]
for cmd in commands:
 p=subprocess.run(cmd,capture_output=True,text=True,env=env);receipt['commands'].append({'argv':cmd,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});write('committed-validation.json',receipt);print(' '.join(cmd));print(p.stdout);print(p.stderr);assert p.returncode==0
receipt['all_pass']=True;write('committed-validation.json',receipt)
print('Preserved 8 Guides, 52 evidence files; 257 exact old-body destinations; 10 source hashes/readers match; actual validators passed.')
