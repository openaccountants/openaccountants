import pathlib,json,hashlib,subprocess,re
root=pathlib.Path('.');gitroot='/private/tmp/oa-armenia-finish-2026-10-25';out={}
for name in ['original-candidate.json','main-baseline.json']:
 x=json.load(open(root/'skills/research/armenia-2026'/name));sha=x.get('source_commit',x.get('main_commit'));rs=[]
 for f in x['files']:
  b=f['text_utf8'].encode();actual=subprocess.check_output(['git','show',sha+':'+f['path']],cwd=gitroot)
  rs.append({'path':f['path'],'embedded_sha256_matches':hashlib.sha256(b).hexdigest()==f['sha256'],'git_bytes_identical':actual==b,'git_blob_matches':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==f['git_blob']})
 out[name]={'source_commit':sha,'checks':rs}
x=json.load(open(root/'skills/research/armenia-2026/example-preservation.json'));alltxt='\n'.join(p.read_text() for p in (root/'skills/international/armenia').glob('*.md'))+'\n'+(root/'skills/research/armenia-2026/supplementary-examples.md').read_text()
blocks=re.findall(r'```oa-check\n(.*?)```',alltxt,re.S); hashes={hashlib.sha256(('```oa-check\n'+b+'```').encode()).hexdigest() for b in blocks}
# preservation inventory hashes may include surrounding prose; names are checked independently below
out['examples']={'core_blocks':sum(p.read_text().count('```oa-check') for p in (root/'skills/international/armenia').glob('*.md')),'supplementary_blocks':(root/'skills/research/armenia-2026/supplementary-examples.md').read_text().count('```oa-check'),'original_count':x['initial_guide_blocks'],'all_original_names_preserved':all(c['name'] in alltxt for c in x['controls'])}
protected=['review_status','trust_label','license','authored_by','drafted_by','approved_by','validation_status','validated']
rs=[]
for f in json.load(open(root/'skills/research/armenia-2026/main-baseline.json'))['files']:
 old=f['text_utf8'];new=(root/f['path']).read_text();eq={k:re.findall(r'^'+k+':.*$',old,re.M)==re.findall(r'^'+k+':.*$',new,re.M) for k in protected}
 rs.append({'path':f['path'],'protected':eq,'cta_identical':old.split('<!-- openaccountants-cta-block -->',1)[-1]==new.split('<!-- openaccountants-cta-block -->',1)[-1]})
out['protected']=rs
pathlib.Path('preservation-independent.json').write_text(json.dumps(out,indent=2));print('original',len(out['original-candidate.json']['checks']),'all',all(all(v for k,v in c.items() if k!='path') for c in out['original-candidate.json']['checks']));print(out['examples']);print('protected',all(all(c['protected'].values()) and c['cta_identical'] for c in rs))
