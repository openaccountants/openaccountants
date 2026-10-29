from pathlib import Path
import sys,json,hashlib,shutil
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-slovakia'); E=R/'ledgers/slovakia-2026-evidence'; O=Path(__file__).parent
sys.path.insert(0,str(E)); import writer as w
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
files=['source-scopes.json','source-quotes.md','pit-sources.py','xb-sources.py','tp-sources.py','payroll-sources.py']
for f in files:
 p=O/('before-'+f)
 if not p.exists():shutil.copyfile(E/f,p)
before=json.loads((O/'before-source-scopes.json').read_text()); unchanged=before['ITA2.residence']
updates={'ITA45.relief':[(4,21),(22,26),(28,42)],'ITA17f.exit':[(4,17),(18,35),(36,59),(61,84)],'TPG3.full':[(114,139),(140,152)],'Social138':[(4,22),(24,53),(69,75),(80,104),(114,149),(150,151)]}
for k,qr in updates.items():
 d=w.scopes[k]; lines=w.lf(d['reader_path']); assert sha(d['raw_path'])==d['raw_sha256'];assert sha(d['reader_path'])==d['reader_sha256']
 d['quotations']=[{'LF_start':a,'LF_end':b,'quote':w.ws('\n'.join(lines[a-1:b]))} for a,b in qr];d['read_date']='2026-10-29'
w.scope('Social138c',10,'sources/10.txt',9219,9224,'§ 138c',[(9219,9224)],'Actual retained current provision read 2026-10-29; €300 monthly deduction limited to the lower assessment base.')
ops={'pit-sources.py':("[(4,21),(28,42)]","[(4,21),(22,26),(28,42)]"),'xb-sources.py':("[(4,17),(36,59),(61,84)]","[(4,17),(18,35),(36,59),(61,84)]"),'tp-sources.py':("('TPG3.full',111,152,[(116,139),(140,152)])","('TPG3.full',111,152,[(114,139),(140,152)])"),'payroll-sources.py':("section('Social138',10,'138',1,151,[(4,16)","section('Social138',10,'138',1,151,[(4,22)")}
for f,(a,b) in ops.items():
 s=(O/('before-'+f)).read_text();assert s.count(a)==1;s=s.replace(a,b)
 if f=='payroll-sources.py':s+="\nscope('Social138c',10,'sources/10.txt',9219,9224,'§ 138c',[(9219,9224)],'Actual retained current provision read 2026-10-29; €300 monthly deduction limited to the lower assessment base.')\n"
 (E/f).write_text(s)
w.CAT.write_text(json.dumps(w.scopes,ensure_ascii=False,indent=2)+'\n');w.render_sources()
assert w.scopes['ITA2.residence']==unchanged
changed=[k for k in before if before[k]!=w.scopes[k]];assert set(changed)==set(updates),changed
assert set(w.scopes)-set(before)=={'Social138c'}
bridge={k:{'before':before.get(k),'after':w.scopes[k]} for k in [*updates,'Social138c']}
(O/'exact-before-after-bridge.json').write_text(json.dumps(bridge,ensure_ascii=False,indent=2)+'\n')
checks={'changed_existing_keys':changed,'added_keys':['Social138c'],'root_ITA2_residence_byte_identity':True,'source_scopes_before_sha256':sha(O/'before-source-scopes.json'),'successors':{f:sha(E/f) for f in files},'literal_quotes_verified':all(q['quote']==w.ws('\n'.join(w.lf(d['reader_path'])[q['LF_start']-1:q['LF_end']])) for k,d in w.scopes.items() if k in bridge for q in d['quotations'])}
(O/'checks.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks,indent=2))
