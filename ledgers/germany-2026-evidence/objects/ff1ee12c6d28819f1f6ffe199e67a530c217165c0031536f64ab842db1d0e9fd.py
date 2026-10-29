from pathlib import Path
from decimal import Decimal as D,ROUND_FLOOR
import json,hashlib,re,sys,importlib.util,contextlib,io,subprocess,datetime
Q=Path(__file__).resolve().parent;O=Q.parent;P=O/'germany-DE-R01-R04-PIT-writer-repair-2026-10-29';R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-germany');H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();sys.path.insert(0,str(R/'scripts'));sys.path.insert(0,'/Users/michaelcutajar/Library/Python/3.9/lib/python/site-packages')
# Canonical full-paragraph replacement allows a simple unambiguous inverse.
p=Q/'R10-exact-operations.json';ops=json.loads(p.read_text());before=(Q/'before/de-trade-tax.md').read_text();after=(Q/'after/de-trade-tax.md').read_text();oldline=next(l for l in before.split('\n') if 'Not yet confirmed:' in l);newline=next(l for l in after.split('\n') if 'Not yet confirmed:' in l);ops[1]['old']=oldline;ops[1]['new']=newline;p.write_text(json.dumps(ops,ensure_ascii=False,indent=2)+'\n')
p=Q/'proof-and-inventory.json';proof=json.loads(p.read_text());proof['other_six_pairs_unchanged_by_R09_operation']=proof.pop('other_six_pairs_unchanged');p.write_text(json.dumps(proof,indent=2)+'\n');trade=json.loads((Q/'R10-proof-and-inventory.json').read_text());manifest=json.loads((P/'artifact-manifest.json').read_text());mismatches=[x['path'] for x in manifest['artifacts'] if H(P/x['path'])!=x['sha256']];assert not mismatches
# Exact source/reader quote check, no new acquisition or implied all-law reading.
for id,x in json.loads((Q/'own-actual-read-quotes.json').read_text()).items():
 assert H(Path(x['raw_path']))==x['raw_sha256'] and H(Path(x['reader_path']))==x['reader_sha256'];a,b=x['native_LF'];assert '\n'.join(Path(x['reader_path']).read_text().split('\n')[a-1:b])==x['exact_quote']
controls=[]
for amount,w in [('10000','1500'),('10001','1500'),('10006','1500'),('10007','1501')]:
 intermediate=D(amount)*D('.15');actual=intermediate.to_integral_value(rounding=ROUND_FLOOR);assert actual==D(w);controls.append({'id':'R09.positive-'+amount,'taxable_income':amount,'intermediate':str(intermediate),'assessment':str(actual),'expected':w,'pass':True,'scope':'Stipulated ordinary positive assessed KSt; not a rule for all bases, surcharges or refunds.'})
def module(name,path):
 s=importlib.util.spec_from_file_location(name,str(path));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ce=module('r09_examples',R/'scripts/check-examples.py');vg=module('r09_validator',R/'scripts/validate-guides.py');files=set();examples={};canonical={}
for slug,pr,rowsname,opsname in [('de-corporate-tax',proof,'rows.json','exact-operations.json'),('de-trade-tax',trade,'trade-rows.json','R10-exact-operations.json')]:
 p=R/'skills/international/germany'/f'{slug}.md';assert H(p)==pr['after_Guide_sha256'];assert H(Q/'ledgers'/f'{slug}.md')==pr['ledger_sha256'];old=(Q/'before'/p.name).read_text();new=(Q/'after'/p.name).read_text();assert p.read_text()==new
 oo=json.loads((Q/opsname).read_text());forward=old
 for x in oo:assert forward.count(x['old'])==1;forward=forward.replace(x['old'],x['new'],1)
 assert forward==new;reverse=new
 for x in reversed(oo):assert reverse.count(x['new'])==1;reverse=reverse.replace(x['new'],x['old'],1)
 assert reverse==old
 for row in json.loads((Q/'support'/rowsname).read_text()):
  a,b=row['native_LF'];assert row['wording']=='\n'.join(new.split('\n')[a-1:b])
 n,f=ce.check_file(str(p));assert not f;examples[slug]={'blocks':n,'failures':f};files.add(str(p.relative_to(R)));canonical[slug]={'Guide_sha256':pr['after_Guide_sha256'],'Guide_bytes':pr['bytes'],'ledger_path':str(Q/'ledgers'/f'{slug}.md'),'ledger_sha256':pr['ledger_sha256'],'current_rows':pr['current_rows']}
oldinv=json.loads((P/'successor-inventory.json').read_text())
for slug,x in oldinv.items():
 if slug not in canonical:assert H(Path(json.loads((P/'preservation-proof.json').read_text())[slug]['path']))==x['Guide_sha256']
errors=[];warnings=[]
with contextlib.redirect_stdout(io.StringIO()) as out:vg.check_guides(vg.load_build_index(),errors,warnings,only_files=files)
assert not errors and not warnings;diff=subprocess.run(['git','diff','--check','--',*sorted(files)],cwd=R,capture_output=True,text=True);assert diff.returncode==0
check={'writer_only':True,'controls':controls,'original_case_checks':examples,'original_case_count':4,'schema':{'files':2,'errors':errors,'warnings':warnings,'stdout':out.getvalue()},'scoped_diff_check':{'returncode':diff.returncode,'stdout':diff.stdout,'stderr':diff.stderr},'prior_seven_seal_member_rehashes':len(manifest['artifacts']),'mismatches':mismatches,'other_five_Guide_ledger_pairs_exact_prior_seal':True,'both_full_inverses':True,'all_current_row_native_wording_exact':True,'remaining_form_Munich_reservations_exact':True}
(Q/'writer-checks.json').write_text(json.dumps(check,indent=2)+'\n');(Q/'successor-inventory.json').write_text(json.dumps(canonical,indent=2)+'\n')
(Q/'writer-report.md').write_text('''# Germany R09–10 minimal writer successors, 29 October 2026

These two targets supersede only the corporate and trade pairs in the immutable R01–08 seven-Guide bundle. They require different independent review; this is no country PASS or accountant attestation.

DE-R09 adds the actual KStG §31(1) assessed-tax rounding step and a positive €10,001 ×15%=€1,500.15 →€1,500 separator outside the two original cases. It does not invent a common rounding rule for bases, surcharges or refunds. The whole selected native LF7 was actually read; exact own original-language quotation, official URL, raw/reader hashes and read date are in own-actual-read-quotes.json. Earlier R07/08 corporate conditions remain exact.

DE-R10 removes only the obsolete semicolon-delimited statement that any Abfärbung de minimis limit is unconfirmed. The supplied BFH/BMF dual-gate own-activity method remains exact, and the ELSTER2026 form and Munich2026 decision reservations remain byte-exact. Its earlier contradictory Sources statement is preserved as the first-seal preimage.

Both Guides have monotonic versions, exact preimages/operations/full inverses and complete successor current-row/old-topic bindings. Original examples, URL occurrence order, bylines, CTA and protected metadata are retained. Four new positive rounding controls, both Guides' four original examples and scoped schema0/0/diff checks pass. All87 members of the prior writer seal rehash unchanged; the other five pairs remain exact. The original25-Guide country freeze and all original writer chains remain untouched.

Final two targets are pinned in successor-inventory.json. Unchanged original/source anchors remain by reference to the first seal; no fresh read is invented. The exact R01–08 original source/reading/protection ledgers continue to apply to their unchanged bytes. C's independent exact successor check remains required.\n''')
entries=[{'path':str(p.relative_to(Q)),'sha256':H(p),'bytes':p.stat().st_size} for p in sorted(Q.rglob('*')) if p.is_file() and p.name not in ['artifact-manifest.json','freeze.json'] and '__pycache__' not in p.parts];mp=Q/'artifact-manifest.json';mp.write_text(json.dumps({'status':'Writer successors, different review pending','artifacts':entries},indent=2)+'\n');freeze={'created_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'role':'writer','report_sha256':H(Q/'writer-report.md'),'artifact_manifest_sha256':H(mp),'members':len(entries),'two_successor_pairs':canonical,'prior_seven_writer_manifest_sha256':H(P/'artifact-manifest.json'),'prior_other_five_pairs_unchanged':True};fp=Q/'freeze.json';fp.write_text(json.dumps(freeze,indent=2)+'\n');print(json.dumps({**freeze,'freeze_sha256':H(fp)},indent=2))
