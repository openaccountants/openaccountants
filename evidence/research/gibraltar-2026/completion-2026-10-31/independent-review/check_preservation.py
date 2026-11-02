import json, pathlib, hashlib, subprocess, re
root=pathlib.Path.cwd();b=root/'evidence/research/gibraltar-2026/completion-2026-10-31';o=b/'independent-review'
h=lambda d:hashlib.sha256(d).hexdigest()
def body(s):return s.split('---',2)[2]
def blocks(s):return re.findall(r'^```oa-check[^\n]*\n.*?^```',s,re.M|re.S)
cp=json.loads((b/'checkpoint.json').read_text()); errors=[]
for g in ['guide_files','evidence_files']:
 for p,d in cp[g].items():
  if h((root/p).read_bytes())!=d:errors.append('checkpoint:'+p)
res=[];total=0
for r in json.loads((b/'mechanical-preservation.json').read_text()):
 p=r['file'];old=(b/'mechanical-before'/pathlib.Path(p).name).read_text();new=(root/p).read_text()
 base=subprocess.check_output(['git','show','53696ccc7:'+p]).decode()
 if old!=base:errors.append('before-not-base:'+p)
 oldlines=body(old).splitlines();newlines=body(new).splitlines();count=0
 for e in r['body_line_checks']:
  a=oldlines[e['old_line']-1];z=newlines[e['new_line']-1]
  if a!=e['original']:errors.append('wrong-old-map:'+p+':'+str(e['old_line']))
  z=z.replace('../../evidence/research/','../../research/').replace('../../docs/research/','../../../docs/research/')
  norm=lambda t:re.sub(r' v\d+(?:\.\d+)+',' vVERSION',t)
  ok=norm(a)==norm(z) or z.startswith(a+'; read on ') or (a.startswith('|') and z.startswith(a.rstrip(' |')))
  if not ok:errors.append('substantive-change:'+p+':'+str(e['old_line']))
  count+=1
 actual=sum(bool(l.strip()) for l in oldlines)
 if count!=actual:errors.append('incomplete-map:'+p)
 sameblocks=blocks(old)==blocks(new)
 if not sameblocks:errors.append('blocks:'+p)
 res.append({'file':p,'old_body_nonblank_lines':actual,'mapped_lines':count,'blocks_byte_exact':len(blocks(old)) if sameblocks else False});total+=count
old=(b/'gi-global-minimum-tax.before.txt').read_text();new=(root/'skills/gibraltar/gi-global-minimum-tax.md').read_text();topics=json.loads((b/'old-topics.json').read_text())['rows']; missing=[]
for r in topics:
 if r['status']=='exact text retained' and r['text'] not in new:missing.append(r['id'])
 if r['text'] not in old:errors.append('old-topic-not-before:'+str(r['id']))
# Check writer map covers every old paragraph/list/control apart from headings and source table.
newblocks=blocks(new);oldblocks=blocks(old)
if oldblocks!=newblocks:errors.append('minimum-blocks-changed')
paths=json.loads((b/'path-migration.json').read_text())['files'];badpaths=[]
for r in paths:
 if h((root/r['new']).read_bytes())!=r['sha256']:badpaths.append(r['new'])
 # The move happened before review_base; compare exact pre-move blob via commit ancestry.
try:
 movecommit=subprocess.check_output(['git','log','--format=%H','-1','--',paths[0]['new']]).decode().strip()
 for r in paths:
  d=subprocess.check_output(['git','show',movecommit+'^:'+r['old']],stderr=subprocess.DEVNULL)
  if h(d)!=r['sha256']:badpaths.append('historical:'+r['old'])
except subprocess.CalledProcessError: errors.append('historical-move-source-unavailable')
result={'errors':errors,'mechanical_files':res,'old_body_lines':total,'mechanical_oa_blocks':sum(r['blocks_byte_exact'] or 0 for r in res),'old_topics':len(topics),'exact_old_topic_prose_missing':missing,'minimum_oa_blocks_byte_exact':len(oldblocks),'historical_moved_files':len(paths),'move_errors':badpaths}
(o/'preservation-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
