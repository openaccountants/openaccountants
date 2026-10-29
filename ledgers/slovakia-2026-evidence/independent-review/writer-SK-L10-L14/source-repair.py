from pathlib import Path
import sys,json,shutil,hashlib
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-slovakia');E=R/'ledgers/slovakia-2026-evidence';O=Path(__file__).parent
sys.path.insert(0,str(E));import writer as w
for f in ['source-scopes.json','source-quotes.md','vat-sources.py','payroll-sources.py']:
 if not (O/('before-'+f)).exists():shutil.copyfile(E/f,O/('before-'+f))
before=json.loads((O/'before-source-scopes.json').read_text())
updates={'VAT78.return':[(3,49),(65,70)],'VAT4.status':[(3,38),(40,60),(69,99),(96,118),(119,151),(151,170),(183,187)],'VAT49.deduction':[(3,10),(11,24),(25,74)],'VAT4b.group':[(3,18),(18,37),(39,52)]}
for k,qr in updates.items():
 d=w.scopes[k];assert w.sha(d['raw_path'])==d['raw_sha256'];assert w.sha(d['reader_path'])==d['reader_sha256'];ls=w.lf(d['reader_path']);d['quotations']=[{'LF_start':a,'LF_end':b,'quote':w.ws('\n'.join(ls[a-1:b]))} for a,b in qr];d['read_date']='2026-10-29'
w.scope('TC154.registration',20,w.scopes['TC154.return-duty']['reader_path'],13,14,'TaxCode §154(1)(b)',[(13,14)])
w.scope('VAT2024.goods-decision',16,'sources/16.txt',2446,2451,'Historical 2024 VAT §7(3)',[(2446,2451)],'Historical seven-day decision only, not the 2026 rule.')
w.scope('VAT2024.services-decision',16,'sources/16.txt',2468,2473,'Historical 2024 VAT §7a(3)',[(2468,2473)],'Historical seven-day decision only, not the 2026 rule.')
w.scope('Health10b',18,'sources/18.txt',3435,3494,'Health Act §10b(1)(a), (2)–(4)',[(3435,3466),(3480,3494)],'Employee health scope read separately from social insurance; intervening other-income categories3467–3479 read but not quoted.')
s=(O/'before-vat-sources.py').read_text()
ops=[("('VAT78.return','78',[(3,49),(67,70)])","('VAT78.return','78',[(3,49),(65,70)])"),("('VAT4.status','4',[(3,38),(40,60),(96,118),(119,151),(183,187)])","('VAT4.status','4',[(3,38),(40,60),(69,99),(96,118),(119,151),(151,170),(183,187)])"),("('VAT49.deduction','49',[(3,10),(25,74)])","('VAT49.deduction','49',[(3,10),(11,24),(25,74)])"),("('VAT4b.group','4b',[(3,18),(39,52)])","('VAT4b.group','4b',[(3,18),(18,37),(39,52)])")]
for a,b in ops:assert s.count(a)==1;s=s.replace(a,b)
s+='\n'+"scope('TC154.registration',20,scopes['TC154.return-duty']['reader_path'],13,14,'TaxCode §154(1)(b)',[(13,14)])\nscope('VAT2024.goods-decision',16,'sources/16.txt',2446,2451,'Historical 2024 VAT §7(3)',[(2446,2451)],'Historical seven-day decision only, not the 2026 rule.')\nscope('VAT2024.services-decision',16,'sources/16.txt',2468,2473,'Historical 2024 VAT §7a(3)',[(2468,2473)],'Historical seven-day decision only, not the 2026 rule.')\nrender_sources()\n"
(E/'vat-sources.py').write_text(s)
s=(O/'before-payroll-sources.py').read_text()+"\nscope('Health10b',18,'sources/18.txt',3435,3494,'Health Act §10b(1)(a), (2)–(4)',[(3435,3466),(3480,3494)],'Employee health scope read separately from social insurance; intervening other-income categories3467–3479 read but not quoted.')\nrender_sources()\n";(E/'payroll-sources.py').write_text(s)
w.CAT.write_text(json.dumps(w.scopes,ensure_ascii=False,indent=2)+'\n');w.render_sources()
changed={k:{'before':before.get(k),'after':v} for k,v in w.scopes.items() if before.get(k)!=v};assert set(changed)==set(updates)|{'TC154.registration','VAT2024.goods-decision','VAT2024.services-decision','Health10b'}
assert before['ITA2.residence']==w.scopes['ITA2.residence']
(O/'source-exact-before-after.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2)+'\n');print(w.sha(w.CAT),w.sha(E/'source-quotes.md'))
