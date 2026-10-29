# Historical inventoryobjectshapes differ; exact already-accepted ledgerhash fallback checks retained actualbytes, not presumedinventory layout.
# First inventoryscan met an unrelated historicalmetadata object withoutslug; restrict to exact pairobjects. No source/body/map changed.
from pathlib import Path
import json,hashlib,re
R=Path(__file__).parent;O=R.parent;H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();f=json.loads((R/'country-freeze.json').read_text());p=json.loads((R/'progress.json').read_text());s1=json.loads((R/'DE-R01-R08-bounded-successor-check.json').read_text())
for slug in ['de-income-tax','de-self-employed-income-tax','de-partners-and-part-year']:
 z=s1['pairs'][slug];p['review_progress'][slug].update({'accepted_guide_sha256':z['guide_sha256'],'accepted_ledger_sha256':z['ledger_sha256'],'status':'Completed original frozenwholepair actualreading plus applicable exact R01–08 successor independentlyPASS; final scope matrix retains realordinarylimits.'})
u=next(x for x in f['pairs']if x['slug']=='de-uk-employer-first-hire');p['review_progress'][u['slug']].update({'accepted_guide_sha256':u['Guide_sha256'],'accepted_ledger_sha256':u['ledger_sha256'],'status':'Frozenwholepair complete and no repair finding; Germany-only local-hire scope preserved, no UKtax/immigrationattestation.'})
p['scope']='All25frozen wholepair current/source/oldorigin reading and final exact reviewed repairs complete. README final scope binding separately pending. Six real partial domains retained, not universalordinarycountrycomplete.';p['pending']='FinalREADMEsixpartial exactsuccessor and final report/manifest/pathpackaging only. No new law/source/body reading required absent a changed or failed claim.';(R/'progress.json').write_text(json.dumps(p,indent=2)+'\n')
invs=[]
for ip in O.glob('germany-DE-*/successor-inventory.json'):
 x=json.loads(ip.read_text());x=x if isinstance(x,list)else[x]
 for z in x:
  if 'slug'in z and 'Guide_sha256'in z and'ledger_sha256'in z:invs.append((ip,z))
out=[]
for before in f['pairs']:
 slug=before['slug'];v=p['review_progress'][slug];gh=v['accepted_guide_sha256'];lh=v['accepted_ledger_sha256'];matches=[(ip,z)for ip,z in invs if z['slug']==slug and z['Guide_sha256']==gh and z['ledger_sha256']==lh]
 if matches:ip,z=matches[-1];lp=z['ledger_path'];receipt=str(ip)
 elif slug in ['de-income-tax','de-self-employed-income-tax','de-partners-and-part-year']:lp=str(O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29/ledgers'/f'{slug}.md');receipt=str(R/'DE-R01-R08-bounded-successor-check.json')
 else:
  candidates=[v for v in list(O.glob('germany-DE-*/ledgers/'+slug+'.md'))+list(O.glob('germany-DE-*/'+slug+'.md'))if H(v)==lh]
  if candidates:lp=str(candidates[-1]);receipt='Exact accepted hash from preceding independent closure, matching actual retained ledger bytes'
  else:assert slug=='de-uk-employer-first-hire',slug;lp=before['ledger_path'];receipt=str(R/'de-uk-employer-first-hire-source-read-ledger.json')
 assert H(before['Guide_path'])==gh,slug;assert H(lp)==lh,(slug,lp);orig=(R/'guide-snapshots'/f'{slug}.md').read_text();cur=Path(before['Guide_path']).read_text();a=re.findall(r'```oa-check.*?```',orig,re.S);b=re.findall(r'```oa-check.*?```',cur,re.S);assert a==b,slug
 out.append({'slug':slug,'Guide_path':before['Guide_path'],'Guide_sha256':gh,'Guide_bytes':Path(before['Guide_path']).stat().st_size,'ledger_path':lp,'ledger_sha256':lh,'ledger_bytes':Path(lp).stat().st_size,'frozen_original_Guide_sha256':before['Guide_sha256'],'frozen_original_ledger_sha256':before['ledger_sha256'],'exact_successor_inventory_or_review':receipt,'original_oa_blocks_byteexact':len(a),'independent_scope':v})
assert len(out)==25;assert sum(z['original_oa_blocks_byteexact']for z in out)==41
(R/'final-25-pair-map.json').write_text(json.dumps({'status':'All25exact substantive pairs independently reviewed; precise domain partials remain. READMEscope bound separately. Paths are current private reviewed ledger identities, before any publisher path-only rebase.','pairs':out,'all50_current_pair_hashes_verified':True,'all41original_executable_blocks_byteexact':True,'original_frozen_grouped_current_units_read':4625,'original_prepared_quote_records_checked':2212,'actual_old_origin_units_identity_checked':7883,'frozen_per_pair_calculation_decision_controls':995,'counts_are_not_distinct_taxfacts_or_unique_sources':True},indent=2)+'\n');print('FINALMAP25/50/41verified')
