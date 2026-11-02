from pathlib import Path
import hashlib,json,re,subprocess
R=Path(__file__).resolve().parents[5];D=Path(__file__).resolve().parent
BASE='3ad7f3e98';CANDIDATE='e154e1b7bf107d7e9efa01c7622a91e89850da8a'
sha=lambda x:hashlib.sha256(x).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def original(rel):return subprocess.check_output(['git','show',BASE+':'+rel],cwd=R)
expected={'moldova-income-tax':24,'md-corporate-income-tax':13,'moldova-payroll':18,'moldova-tax-optimization':8,'moldova-social-contributions':20,'md-company-formation':9,'md-tax-overview':12}
changes=[];snapshots=[];base_text={}
for p in sorted((R/'skills/moldova').glob('*.md')):
 if p.name=='README.md':continue
 rel=str(p.relative_to(R));b=original(rel);base_text[rel]=b.decode()
 out=D/'original-guides'/p.name
 if out.exists():assert out.read_bytes()==b
 else:out.parent.mkdir(exist_ok=True);out.write_bytes(b)
 snapshots.append({'path':rel,'original_snapshot':str(out.relative_to(R)),'original_sha256':sha(b)})
# Every citation target is expanded from the document's own unchanged definition.
for slug,wanted in expected.items():
 rel=f'skills/moldova/{slug}.md';s=base_text[rel]
 refs={m.group(1).strip().casefold():m.group(2) for m in re.finditer(r'^\[([^\]]+)\]:\s*(https?://\S+)\s*$',s,re.M)}
 start=s.index('## Rates, bands and thresholds');end=s.find('\n## ',start+4);assert end>start
 section=s[start:end];old_lines=section.splitlines(keepends=True);new_lines=[];row_changes=[]
 for offset,line in enumerate(old_lines):
  if line.lstrip().startswith('|'):
   expansions=[]
   def expand(m):
    label,key=m.group(1),m.group(2);url=refs[key.strip().casefold()]
    expansions.append({'reference':key,'label':label,'url':url,'definition_exact':True})
    return f'[{label}]({url})'
   new=re.sub(r'\[([^\]\n]+)\]\[([^\]\n]+)\]',expand,line)
   if new!=line:
    row_changes.append({'old_line':s.count('\n',0,start)+offset+1,'before':line.rstrip('\n'),'after':new.rstrip('\n'),'expansions':expansions})
   new_lines.append(new)
  else:new_lines.append(line)
 assert len(row_changes)==wanted,(slug,len(row_changes),wanted)
 newsection=''.join(new_lines);new=s[:start]+newsection+s[end:]
 # Reversal proves that no other table/prose/source bytes changed.
 rev=new
 for row in row_changes:assert rev.count(row['after'])==1;rev=rev.replace(row['after'],row['before'],1)
 assert rev==s
 changes.append({'file':rel,'kind':'same-target rate-table citation format only','affected_rows':wanted,'rows':row_changes})
 (R/rel).write_text(new)
property_rel='skills/moldova/md-property-tax.md';s=base_text[property_rel]
fixes=[
 ('MD-PW-001','[Code 277(2)–(3),278]','[Code 277(3)–(4),278]','277(3)–(4)'),
 ('MD-PW-001','[Code 280(1¹)–(1²)]','[Code 280(1¹)]','280(1¹)'),
 ('MD-PW-001','article 281(1¹) uses','article 281(1) uses','281(1)'),
 ('MD-PW-001','under article 281(4).','under article 281(3).','281(3)'),
 ('MD-PW-001','[Code 281(3)–(5),282¹]','[Code 281(2),(2¹),(3),(4),282¹]','281(2),(2¹),(3),(4),282¹'),
 ('MD-PW-001','under 277(1)(e¹);','under 277(1)(f);','277(1)(f)'),
 ('MD-PW-002','and permanent disabled-person carers','and family members who permanently maintain and care for persons with disabilities','283(1)(k)'),
 ('MD-PW-002',"Free-zone administrations have article 283(5)'s managed-property exemption.","Free-zone administrations have article 283(5)'s exemption for land and plots while held in their management.",'283(5)')]
for fid,before,after,pin in fixes:
 assert s.count(before)==1,(fid,before,s.count(before));s=s.replace(before,after,1)
 changes.append({'file':property_rel,'finding':fid,'kind':'required pinpoint or exemption-condition repair','before':before,'after':after,'operative_article':pin,'official_url':'https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro','source_evidence':'evidence/ledgers/md-country-evidence/property-wealth-20261031/sources/property-wealth-current-code-20261031.json','evidence_read_date':'2026-10-31','fresh_successful_live_read_claimed':False})
(R/property_rel).write_text(s)
# Only the nine changed Guides advance versions; no read date/platform field is touched.
versioned=list(expected)+['md-property-tax','md-wealth-tax']
for slug in versioned:
 rel=f'skills/moldova/{slug}.md';p=R/rel;s=p.read_text() if p.exists() else base_text[rel]
 old=re.search(r'^version: "([0-9.]+)"$',s,re.M).group(1);parts=old.split('.');parts[-1]=str(int(parts[-1])+1);new='.'.join(parts)
 h1=re.search(r'^# .+$',s,re.M).group();newh1=re.sub(r' v'+re.escape(old)+r'$', ' v'+new,h1) if re.search(r' v'+re.escape(old)+r'$',h1) else h1+' v'+new
 assert s.count(f'version: "{old}"')==1;s=s.replace(f'version: "{old}"',f'version: "{new}"',1);s=s.replace(h1,newh1,1);p.write_text(s)
 changes.append({'file':rel,'finding':'MD-PW-003' if slug in ['md-property-tax','md-wealth-tax'] else 'legacy citation-format version','kind':'version and matching H1 only','old_version':old,'new_version':new,'old_H1':h1,'new_H1':newh1})
dump(D/'original-guide-manifest.json',{'candidate_commit':CANDIDATE,'review_preservation_commit':subprocess.check_output(['git','rev-parse',BASE],cwd=R,text=True).strip(),'Guides':snapshots})
dump(D/'changes.json',{'date':'2026-10-31','scope':'Eight required property corrections, two new H1 repairs, and exact-target inline citations in 104 legacy rate rows; no original source/ledger/review mutation.','changes':changes,'same_target_citation_rows':sum(expected.values()),'new_law_read_claimed':False,'source_access_record':'../independent-review/source-access.json','publication_reuse_clearance':False})
print(json.dumps({'legacy_rows':sum(expected.values()),'property_corrections':len(fixes),'Guides_versioned':len(versioned),'original_Guides':len(snapshots)}))
