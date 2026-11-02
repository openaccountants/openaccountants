from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parents[4];D=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest();m=json.loads((D/'source-publication-map.json').read_text());checks=[]
def check(name,passed,detail=None):
 checks.append({'check':name,'passed':bool(passed),'detail':detail});assert passed,(name,detail)
for g in m['accepted_Guides_and_README']:check('Exact accepted Guide/README '+g['path'],sha((R/g['path']).read_bytes())==g['sha256'])
for p in m['already_public_evidence_relocations']:check('Exact prior public evidence '+p['current_path'],sha((R/p['current_path']).read_bytes())==p['sha256'])
for p in m['private_source_captures']:check('Raw source omitted '+p['private_original_path'],not (R/p['private_original_path']).exists())
for research in ['27f350e898af9e7218a470d0aab4e475d724e06e','e154e1b7bf107d7e9efa01c7622a91e89850da8a','6a76c6dd877fc734f069bf7c145c8381abcc7df1']:
 check('Unpublished research is not publication ancestry '+research,subprocess.run(['git','merge-base','--is-ancestor',research,'HEAD'],cwd=R).returncode==1)
check('Existing PR head remains ancestor',subprocess.run(['git','merge-base','--is-ancestor',m['existing_public_PR_head'],'HEAD'],cwd=R).returncode==0)
check('Current public main merged',subprocess.run(['git','merge-base','--is-ancestor',m['integrated_public_main'],'HEAD'],cwd=R).returncode==0)
# Scan all newly published country files for exact omitted source payloads; old public bytes are preserved separately.
rawhashes={p['sha256'] for p in m['private_source_captures']};matches=[];newfiles=[]
for p in (R/'evidence/ledgers/md-country-evidence').rglob('*'):
 if not p.is_file():continue
 if sha(p.read_bytes()) in rawhashes:matches.append(str(p.relative_to(R)))
check('No omitted raw payload duplicated under another country-evidence path',not matches,matches)
# Original source ledger and review bytes are unchanged from the accepted research tree.
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',m['accepted_research_commit'],'--','evidence/ledgers/md-country-evidence'],cwd=R,text=True).splitlines();omitted={p['private_original_path'] for p in m['private_source_captures']}
# One batch subprocess avoids repeatedly reading the same Git pack.
proc=subprocess.Popen(['git','cat-file','--batch'],cwd=R,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for rel in paths:
 if rel in omitted:continue
 proc.stdin.write((m['accepted_research_commit']+':'+rel+'\n').encode());proc.stdin.flush();header=proc.stdout.readline().decode().strip().split();assert header[1]=='blob';raw=proc.stdout.read(int(header[2]));assert proc.stdout.read(1)==b'\n'
 check('Accepted evidence unchanged '+rel,(R/rel).read_bytes()==raw)
proc.stdin.close();proc.wait()
for g in m['accepted_Guides_and_README']:
 if Path(g['path']).name=='README.md':continue
 for suffix in ['.md','.writer.json']:
  rel='evidence/ledgers/'+Path(g['path']).stem+suffix
  original=subprocess.check_output(['git','show',m['accepted_research_commit']+':'+rel],cwd=R);check('Accepted purpose-specific ledger unchanged '+rel,(R/rel).read_bytes()==original)
readme=(R/'skills/moldova/README.md').read_text();check('Partial and independent source limits retained','partial' in readme and 'bounded' in readme)
check('No misleading comprehensive-coverage promotion','all seven domains' not in readme.lower() or 'partial' in readme.lower())
result={'date':'2026-10-31','scope':'Publication selection/preservation only; substantive review and arithmetic reuse the accepted records. No rights clearance or fresh successful source read asserted.','checks':len(checks),'failures':0,'accepted_Guides':13,'accepted_README':1,'private_captures':49,'public_evidence_relocations':669,'details':checks}
(D/'publication-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='details'}))
