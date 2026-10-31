import sys,importlib.util,json,re,hashlib
from pathlib import Path
sys.path.insert(0,'scripts')
sp=importlib.util.spec_from_file_location('vg','scripts/validate-guides.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
r=Path(__file__).parent
slugs=['fo-payroll-contributions','fo-company-registration-reporting']
ps={f'skills/international/faroe-islands/{n}.md' for n in slugs}
errors=[];warnings=[]
v.check_guides(v.load_build_index(),errors,warnings,only_files=ps)
o={'schema':{'errors':errors,'warnings':warnings},'preservation':{}}
x=json.loads((r/'payroll-formation-exact-replacements.json').read_text())
for n in slugs:
 p=Path(f'skills/international/faroe-islands/{n}.md');new=p.read_text();old=(r/'baselines'/f'{n}.original.txt').read_text();inv=new
 for z in reversed(x[n]):
  assert inv.count(z['new'])==1,(n,z['new'][:60])
  inv=inv.replace(z['new'],z['old'])
 assert inv==old,n
 blocks=lambda s:re.findall(r'^```oa-check\n.*?^```',s,re.M|re.S)
 assert blocks(new)==blocks(old),(n,'oa')
 assert len(blocks(new))==(2 if n==slugs[0] else 0)
 assert re.findall('^## .*',new,re.M)==re.findall('^## .*',old,re.M)
 urls=lambda s:re.findall(r'https?://[^\s)>]+',s)
 it=iter(urls(new));assert all(any(v==q for v in it) for q in urls(old))
 cta=lambda s:s[s.index('<!-- openaccountants-cta-block -->'):]
 assert cta(new)==cta(old)
 o['preservation'][n]={'exact_inverse':True,'main_oa_blocks':len(blocks(new)),'oa_byte_exact':True,'all_original_H2_order':True,'original_URL_occurrence_subsequence':True,'CTA_byte_exact':True,'original_words':len(old.split()),'current_words':len(new.split()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
(r/'payroll-formation-validation.json').write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps(o,indent=2));assert not errors
