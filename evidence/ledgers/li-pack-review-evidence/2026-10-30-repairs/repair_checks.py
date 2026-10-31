from pathlib import Path
import json,re,subprocess,hashlib,collections,urllib.parse
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/liechtenstein-pack-2026-10-30/repository');W=R.parent/'review';OLD='89507147db70dad74f1389f9abdb03616bd33613';NEW='c92542a3a82f818521abf464ccea3796632e92a6'
def old(path):return subprocess.check_output(['git','show',OLD+':'+path],cwd=R).decode()
def sha(b):return hashlib.sha256(b).hexdigest()
slugs=['li-payroll-social','li-transfer-pricing','li-cross-border','liechtenstein-vat','li-corporate-income-tax','li-income-tax','li-company-formation','li-tax-overview']
continuity=[];newrows=[];maps=[];guidechecks=[]
for slug in slugs:
 p='ledgers/'+slug+'.writer.json';a=json.loads(old(p));b=json.load(open(R/p));newbyid={x['id']:x for x in b['rules']}
 for x in a['rules']:
  y=newbyid[x['id']];diff={k:{'old':x.get(k),'new':y.get(k)}for k in set(x)|set(y)if x.get(k)!=y.get(k)}
  ok=not diff or (x['id']=='LI-VAT-024' and set(diff)=={'rule_or_figure'} and 'NOT REGISTERED'in y['rule_or_figure']) or (x['id'].startswith('LI-ROUTE-') and set(diff)=={'evidence_sha256'} and y['evidence_sha256']==sha((R/y['repository_evidence']).read_bytes()))
  continuity.append({'id':x['id'],'unchanged':not diff,'permitted_change':diff,'pass':ok})
 oldids={x['id']for x in a['rules']};newrows.extend(x for x in b['rules']if x['id']not in oldids)
 # preserve map source texts/hashes, independently check source and destination retention claims.
 oldmaps={x['id']:x for x in a['old_topic_destinations']};newmaps=b['old_topic_destinations'];pre=(R/'ledgers'/(slug+'-evidence')/'predecessor-guide.md').read_text();curr=(R/b['guide']).read_text();annex=R/'ledgers'/(slug+'-evidence')/'retained-original-controls.md';pool=curr+('\n'+annex.read_text()if annex.exists()else'')
 checks=[]
 for x in newmaps:
  base=oldmaps[x['id']];checks.append({'id':x['id'],'old_text_preserved':x['old_text']==base['old_text'],'old_hash_preserved':x['old_sha256']==base['old_sha256'],'old_text_present_in_predecessor':x['old_text']in pre,'exact_claim_valid':not x.get('exact_retained')or x['old_text']in pool,'destination':x['destination']})
 maps.append({'slug':slug,'count':len(checks),'checks':checks,'pass':len(checks)==len(oldmaps)and all(x['old_text_preserved']and x['old_hash_preserved']and x['old_text_present_in_predecessor']and x['exact_claim_valid']for x in checks)})
 gp=b['guide'];prev=old(gp);current=(R/gp).read_text()
 def refs(s):return {m[1].strip().casefold():m[2].strip()for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',s,re.M)}
 ar,br=refs(prev),refs(current);defs=collections.Counter(m[1].strip().casefold()for m in re.finditer(r'^\[([^\]]+)\]:',current,re.M))
 brokenrefs=[m[2]for m in re.finditer(r'\[([^\]\n]+)\]\[([^\]\n]+)\]',current)if m[2].casefold()not in br]
 brokenlocal=[]
 for m in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)',current):
  target=m[1].split('#')[0]
  if not target or re.match(r'[a-zA-Z]+:',target):continue
  if not (R/gp).parent.joinpath(urllib.parse.unquote(target)).exists():brokenlocal.append(target)
 # YAML metadata independent line mapping: no field changed except version.
 def fm(s):return dict(re.findall(r'^(\w+):\s*([^\n]*)',s.split('---',2)[1],re.M))
 af,bf=fm(prev),fm(current);fmdiff={k:[af.get(k),bf.get(k)]for k in set(af)|set(bf)if af.get(k)!=bf.get(k)}
 cta=lambda s:s[s.index('<!-- openaccountants-cta-block -->'):]
 blocks=lambda s:re.findall(r'```oa-check\n(.*?)```',s,re.S)
 guidechecks.append({'guide':gp,'sha256':sha((R/gp).read_bytes()),'reference_definition_duplicates':{k:v for k,v in defs.items()if v>1},'missing_reference_links':brokenrefs,'missing_local_links':brokenlocal,'old_official_reference_targets_retained':all(v in br.values()for v in ar.values()if v.startswith('https:')),'metadata_changes':fmdiff,'only_permitted_metadata_change':set(fmdiff)<= {'version'},'cta_unchanged':cta(prev)==cta(current),'current_example_blocks_unchanged':blocks(prev)==blocks(current),'current_blocks':len(blocks(current))})
# All original preserved source and evidence files remain exact, except intentional author guides/ledgers/check-output metadata.
frozen=json.load(open(R/'ledgers/li-payroll-social-evidence/writer-freeze-89507147.json'));priorreview=[]
for p in (R/'ledgers/li-pack-review-evidence/2026-10-30-89507147').iterdir():
 if p.is_file():priorreview.append({'file':p.name,'copy_sha256':sha(p.read_bytes()),'private_sha256':sha((W/p.name).read_bytes()),'pass':p.read_bytes()==(W/p.name).read_bytes()})
# Independent original quote identity for added groups.
def norm(s):return ''.join(c for c in re.sub(r'L\d+(?:@P\d+(?:-\d+)?)?:\s*','',s).casefold()if c.isalnum())
for x in newrows:
 source=R/x['source_observation'];x['independent_quote_identity']=norm(x['exact_original_language_quote'])in norm(source.read_text());x['independent_source_hash_matches']=sha(source.read_bytes())==x['source_text_sha256']
summary={'candidate':NEW,'original':OLD,'continuity':continuity,'original_row_count':len(continuity),'new_rows':newrows,'new_row_count':len(newrows),'total_row_count':len(continuity)+len(newrows),'old_topic_maps':maps,'guide_checks':guidechecks,'historical_review_copies':priorreview,'original_freeze_copy_byte_exact':old('ledgers/li-payroll-social-evidence/writer-freeze.json').encode()==(R/'ledgers/li-payroll-social-evidence/writer-freeze-89507147.json').read_bytes()}
(W/'repair-checks-raw.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
print('original row continuity',len(continuity),all(x['pass']for x in continuity));print('new rows',len(newrows),[x['id']for x in newrows]);print('maps',[(x['slug'],x['pass'])for x in maps]);print('guide check failures',[x for x in guidechecks if x['reference_definition_duplicates']or x['missing_reference_links']or x['missing_local_links']or not x['old_official_reference_targets_retained']or not x['only_permitted_metadata_change']or not x['cta_unchanged']or not x['current_example_blocks_unchanged']]);print('prior review exact',all(x['pass']for x in priorreview),'freeze copy exact',summary['original_freeze_copy_byte_exact'])
