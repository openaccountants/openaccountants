from pathlib import Path
import json,sys,shutil,re,hashlib
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-slovakia');E=R/'ledgers/slovakia-2026-evidence';O=Path(__file__).parent;sys.path.insert(0,str(E));import writer as w
# Preserve the exact predecessor ledger/support objects; no original seal is rewritten.
slugs=['slovakia-vat-registration-4-7-7a','sk-payroll-social','slovakia-vat-return']
for sl in slugs:
 for p in [R/f'ledgers/{sl}.md',*(E/sl).glob('*.json')]:
  q=O/'before-ledgers'/sl/p.name;q.parent.mkdir(parents=True,exist_ok=True)
  if not q.exists():shutil.copyfile(p,q)
for f in ['vat-ledgers.py','payroll-ledger.py']:
 if not (O/('before-'+f)).exists():shutil.copyfile(E/f,O/('before-'+f))
# Administrative A1 observation is a web-tool response, never presented as EU legislation or original HTML.
A=O.parent/'root-SK-A1-current-source'; sid='SP.A1.current-admin'
w.receipts[sid]={'file':str(A/'official-tool-response.json'),'sha256':w.sha(A/'official-tool-response.json'),'url':json.loads((A/'source-observation.json').read_text())['official_url']}
w.scope(sid,sid,A/'official-selected-reader.txt',51,126,'Sociálna poisťovňa: current administrative one-state/work-state, multistate/A1 and Article16 guidance',[(51,51),(119,121),(124,126)],'Retained official web-tool response JSON acquired/read by root; this writer actually read physical LF51–52,119–126. Web labels are one less than physical LF. This is administrative guidance, not the direct text of Regulation883. Failed EUR-Lex robot receipts remain failed acquisitions.')
w.scopes[sid]['actual_read_ranges']=[[51,52],[119,126]];w.scopes[sid]['source_kind']='Retained official web-tool response JSON, not original HTML or direct EU regulation'
w.CAT.write_text(json.dumps(w.scopes,ensure_ascii=False,indent=2)+'\n');w.render_sources()
# Reproducible A1 supplement appended to source builder; previous source operations remain intact.
p=E/'payroll-sources.py';s=p.read_text();addon="\n# Current administrative A1 observation retained by root; no direct EU-law acquisition claim.\nA=Path("+repr(str(A))+")\nsid='SP.A1.current-admin'\nreceipts[sid]={'file':str(A/'official-tool-response.json'),'sha256':sha(A/'official-tool-response.json'),'url':json.loads((A/'source-observation.json').read_text())['official_url']}\nscope(sid,sid,A/'official-selected-reader.txt',51,126,'Sociálna poisťovňa: current administrative one-state/work-state, multistate/A1 and Article16 guidance',[(51,51),(119,121),(124,126)],"+repr(w.scopes[sid]['note'])+")\nscopes[sid]['actual_read_ranges']=[[51,52],[119,126]]\nscopes[sid]['source_kind']='Retained official web-tool response JSON, not original HTML or direct EU regulation'\nCAT.write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\\n');render_sources()\n"
if "# Current administrative A1 observation retained by root" not in s:p.write_text(s+addon)
# All 66 registrations read against the current Guide and retained operative source scopes.
reg=json.loads((O/'before-ledgers/slovakia-vat-registration-4-7-7a/rows.json').read_text())
changes={
1:['VAT4.status','VAT7.goods','VAT7a.services','VAT49.deduction','VAT2024.registration'],
3:['VAT4.status','VAT7.goods','VAT11.acquisitions','VAT7a.services','VAT2024.registration','VAT2024.rates'],
6:['VAT27.rates','VAT.annex7.goods19','VAT.annex7.goods5','VAT.annex7.services','FS.VAT2026foods'],
11:['VAT11.acquisitions'],12:['VAT7a.services'],13:['VAT49.deduction'],14:['VAT78.return'],15:['VAT77.period'],16:['VAT2024.registration','VAT85kn.oldtransition'],17:['VAT2024.rates','VAT2024.goods-decision','VAT2024.services-decision'],
22:['VAT85kn.oldtransition','VAT2024.registration','VAT2024.rates','VAT2024.goods-decision','VAT2024.services-decision'],
26:['VAT4.status','VAT27.rates','VAT49.deduction','VAT51.documents','VAT69.reverse','VAT78.return','VAT7a.services'],27:['VAT27.rates','VAT69.reverse','VAT49.deduction','VAT51.documents'],
33:['VAT7.goods','VAT7a.services'],34:['VAT78.return'],35:['VAT77.period','VAT78.return'],36:['VAT77.period'],37:['VAT80.EC'],38:['VAT72.invoice','VAT73.deadline','VAT74.wording'],39:['VAT76.retention'],40:['TC27.weekend'],
43:['VAT70.records','VAT72.invoice','VAT73.deadline','VAT74.wording','VAT76.retention'],46:['Form.REGDPv24','VAT4.status','VAT7.goods','VAT7a.services'],48:['TC154.registration','TC155.ranges','TC155.first'],
51:['TC155.ranges','TC155.first','VAT69.reverse','VAT78.return'],52:['VAT4.status','FS.registration.voluntary','VAT7.goods','VAT7a.services'],53:['VAT7a.services','VAT15.services','VAT27.rates','VAT69.reverse','VAT78.return'],54:['VAT7a.services','VAT15.services','VAT69.reverse','VAT68f.foreignSME'],55:['VAT7a.services','VAT15.services','VAT69.reverse'],
57:['VAT7a.services','VAT15.services','VAT69.reverse','VAT27.rates','VAT78.return','VAT49.deduction','VAT51.documents','VAT55.initial'],63:['VAT4.status','VAT22.base','VAT27.rates'],64:['VAT4.status','VAT7a.services','VAT7.goods','VAT11.acquisitions','VAT15.services','VAT49.deduction','VAT55.initial'],65:['VAT2024.rates','VAT2024.goods-decision','VAT2024.services-decision','VAT27.rates','VAT7.goods','VAT7a.services']}
for r in reg:
 if r['row'] in changes:r['source_scopes']=changes[r['row']]
# Persist complete finite review decision for every row, including unchanged routes.
audit=[]
for r,b in zip(reg,json.loads((O/'before-ledgers/slovakia-vat-registration-4-7-7a/rows.json').read_text())):
 assert all(k in w.scopes for k in r['source_scopes'])
 audit.append({'row':r['row'],'Guide_LF':[r['LF_start'],r['LF_end']],'exact_claim':r['guide_wording'],'before':b['source_scopes'],'after':r['source_scopes'],'disposition':'Corrected source routing only' if b['source_scopes']!=r['source_scopes'] else 'Existing source routing checked and retained','operative_source_provisions':{k:w.scopes[k]['article'] for k in r['source_scopes']}})
(O/'SK-L10-all-66-row-route-review.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
# Render only changed figure-row cells and header; old-topic text remains byte-exact except the three explicit correction annotations below.
allchanges={}
for sl in slugs:
 b=json.loads((O/f'before-ledgers/{sl}/rows.json').read_text());rows=reg if sl==slugs[0] else json.loads(json.dumps(b))
 guide=R/f'skills/international/slovakia/{sl}.md';gl=guide.read_text().split('\n');ledger=(O/f'before-ledgers/{sl}/{sl}.md').read_text();oldsha=re.search(r'Guide SHA256 `([0-9a-f]+)`',ledger).group(1);ledger=ledger.replace('Guide SHA256 `'+oldsha+'`','Guide SHA256 `'+w.sha(guide)+'`',1)
 for r in rows:
  if sl=='sk-payroll-social' and r['row']==38:r['source_scopes']=['Social138','Social138c','SP.table','SP.employee-2026'];r['classification']='Current employee social base, separate trainer deduction and unreduced employer accident/guarantee bases; pre-2026 backpay transition remains expressly qualified.'
  if sl=='sk-payroll-social' and r['row']==40:r['source_scopes']=['Health10b','Health13','Health16','Health16a','Health12','Health38ezk']
  if sl=='sk-payroll-social' and r['row']==62:r['source_scopes']=['SP.A1','SP.A1.current-admin'];r['classification']='Official administrative quotations support the bounded one-state/work-state, multistate/A1 and Article16 distinction. Direct Regulation883 Art11(1)/13 body was not reacquired; robot receipts remain acquisition failures, never quoted as law.'
  if sl=='slovakia-vat-return' and r['row']==31:r['classification']='Mixed-use vehicle rule and goods self-supply exclusion limited to the nondeducted extent; no whole-goods exemption inferred.'
  r['guide_wording']='\n'.join(gl[r['LF_start']-1:r['LF_end']])
  if r!=b[r['row']-1]:
   pat=r'^\| '+f'{r["row"]:03d}'+r' \|.*$';m=re.search(pat,ledger,re.M);assert m,(sl,r['row']);old=m.group(0);prefix=old.split(' | ')[1];word=r['guide_wording'].replace('|','\\|').replace('\n','<br>');basis=', '.join(f'[{k}](slovakia-2026-evidence/source-quotes.md#{k.lower().replace(".","-")})' for k in r['source_scopes']);new=f'| {r["row"]:03d} | {prefix} | {word} | {basis}. {r["classification"]} |';ledger=ledger[:m.start()]+new+ledger[m.end():]
 used=sorted({k for r in rows for k in r['source_scopes']});start=ledger.index('\n\n',ledger.index('Each source ID below'))+2;end=ledger.index('\n\n## Complete old-topic',start);ledger=ledger[:start]+', '.join('`'+k+'`' for k in used)+ledger[end:]
 (R/f'ledgers/{sl}.md').write_text(ledger);(E/sl/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');cov=json.loads((O/f'before-ledgers/{sl}/coverage.json').read_text());cov.update(guide_sha256=w.sha(guide),source_scopes=used);(E/sl/'coverage.json').write_text(json.dumps(cov,indent=2)+'\n')
 oldmap=json.loads((O/f'before-ledgers/{sl}/old-topics.json').read_text());oldmap['guide_sha256']=w.sha(guide)
 if sl=='sk-payroll-social':oldmap['bounded_successor_corrections']=['SK-L04: current LF77 trainer income/138c deduction and pre-2026 backpay transition qualification; old blanket exempt-income wording corrected.','SK-L05: current LF81 uses independent HealthAct10b/13 base; social-base treatment not imported.']
 if sl=='slovakia-vat-return':oldmap['bounded_successor_corrections']=['SK-L09: current LF66 private goods self-supply exemption is only to the extent inputVAT was not deducted; no full-asset exemption.']
 (E/sl/'old-topics.json').write_text(json.dumps(oldmap,ensure_ascii=False,indent=2)+'\n')
 allchanges[sl]=[{'row':r['row'],'before':b[r['row']-1],'after':r} for r in rows if r!=b[r['row']-1]]
# Keep builders reproducible without rerunning passed source or old-topic selections.
s=(O/'before-vat-ledgers.py').read_text();start=s.index("r=[e(3,3,'VAT4.status'");end=s.index('\nov=',start);rs='r=[\n'+''.join(' e('+str(r['LF_start'])+','+str(r['LF_end'])+','+','.join(repr(x) for x in r['source_scopes'])+',kind='+repr(r['classification'])+'),\n' for r in reg)+']';s=s[:start]+rs+s[end:]
s=s.replace("e(66,66,'VAT85n.vehicles')","e(66,66,'VAT85n.vehicles',kind='Mixed-use vehicle rule and goods self-supply exclusion limited to the nondeducted extent; no whole-goods exemption inferred.')")
(E/'vat-ledgers.py').write_text(s)
s=(O/'before-payroll-ledger.py').read_text();s=s.replace("e(77,77,'Social138','SP.table','SP.employee-2026'","e(77,77,'Social138','Social138c','SP.table','SP.employee-2026'");s=s.replace("e(81,81,'Health13'","e(81,81,'Health10b','Health13'");s=s.replace("e(144,145,'SP.A1',","e(144,145,'SP.A1','SP.A1.current-admin',");(E/'payroll-ledger.py').write_text(s)
(O/'exact-ledger-before-after-rows.json').write_text(json.dumps(allchanges,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({sl:{'ledger_sha256':w.sha(R/f'ledgers/{sl}.md'),'rows_sha256':w.sha(E/sl/'rows.json'),'Guide_sha256':w.sha(R/f'skills/international/slovakia/{sl}.md'),'changed_rows':len(allchanges[sl])} for sl in slugs},indent=2))
