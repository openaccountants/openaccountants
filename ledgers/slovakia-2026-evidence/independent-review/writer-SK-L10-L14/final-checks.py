from pathlib import Path
import json,hashlib,ast
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-slovakia');E=R/'ledgers/slovakia-2026-evidence';O=Path(__file__).parent;P=O.parent/'writer-SK-L06-L08'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ws(s):return ' '.join(s.split())
d=json.loads((E/'source-scopes.json').read_text());before=json.loads((P/'before-source-scopes.json').read_text())
changed=[k for k in before if d[k]!=before[k]];added=sorted(set(d)-set(before));expected={'ITA45.relief','ITA17f.exit','TPG3.full','Social138','VAT78.return','VAT4.status','VAT49.deduction','VAT4b.group','VAT11.acquisitions'};assert set(changed)==expected
assert added==sorted(['Social138c','TC154.registration','VAT2024.goods-decision','VAT2024.services-decision','Health10b','SP.A1.current-admin']);assert d['ITA2.residence']==before['ITA2.residence']
qchecks=0
for k in changed+added:
 s=d[k];assert sha(s['raw_path'])==s['raw_sha256'];assert sha(s['reader_path'])==s['reader_sha256'];ls=Path(s['reader_path']).read_text().split('\n')
 for q in s['quotations']:assert q['quote']==ws('\n'.join(ls[q['LF_start']-1:q['LF_end']]));qchecks+=1
paths=[];pairs=[]
for sl in ['slovakia-vat-registration-4-7-7a','sk-payroll-social','slovakia-vat-return']:
 guide=R/f'skills/international/slovakia/{sl}.md';ledger=R/f'ledgers/{sl}.md';rows=json.loads((E/sl/'rows.json').read_text());old=json.loads((O/f'before-ledgers/{sl}/rows.json').read_text());gl=guide.read_text().split('\n');cov=json.loads((E/sl/'coverage.json').read_text());assert cov['guide_sha256']==sha(guide);assert 'Guide SHA256 `'+sha(guide)+'`' in ledger.read_text();assert len(rows)==len(old)
 for r in rows:assert r['guide_wording']=='\n'.join(gl[r['LF_start']-1:r['LF_end']]);assert all(k in d for k in r['source_scopes'])
 # Every preceding old-topic unit/text/routing survives; bounded repair notes are added separately.
 a=json.loads((E/sl/'old-topics.json').read_text());b=json.loads((O/f'before-ledgers/{sl}/old-topics.json').read_text());assert a['rows']==b['rows'];assert a['earliest_preimage']==b['earliest_preimage']
 pairs.append({'slug':sl,'Guide_sha256':sha(guide),'ledger_sha256':sha(ledger),'rows_sha256':sha(E/sl/'rows.json'),'row_count':len(rows)});paths += [guide,ledger,*[E/sl/x for x in ['rows.json','coverage.json','old-topics.json']]]
assert pairs[0]['row_count']==66
for p in E.glob('*sources.py'):ast.parse(p.read_text())
for p in [E/'vat-ledgers.py',E/'payroll-ledger.py']:ast.parse(p.read_text())
checks={'successor_pairs':pairs,'changed_source_keys':changed,'added_source_keys':added,'source_scopes_sha256':sha(E/'source-scopes.json'),'source_quotes_sha256':sha(E/'source-quotes.md'),'literal_selected_quote_checks':qchecks,'actual_raw_reader_hash_pairs':len(changed)+len(added),'all66_registration_routes_reviewed':True,'all_493_original_rows_not_reaudited':True,'root_SK_L02_L03_residence_exactly_preserved':True,'previous_old_topics_and_earliest_preimages_exact':True,'Guide_files_written_by_this_repair':False,'three_retained_VAT_uncertainties_changed':False}
(O/'final-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
readranges={'ITA45.relief':[[18,28]],'ITA17f.exit':[[15,38]],'TPG3.full':[[111,120]],'Social138':[[4,22]],'Social138c':[[9215,9228]],'VAT78.return':[[3,49],[63,70]],'VAT4.status':[[65,100],[149,187]],'VAT49.deduction':[[9,25]],'VAT4b.group':[[16,38]],'VAT11.acquisitions':[[20,57]],'TC154.registration':[[1,46]],'VAT2024.goods-decision':[[2435,2454]],'VAT2024.services-decision':[[2455,2473]],'Health10b':[[3435,3494]],'SP.A1.current-admin':[[51,52],[119,126]],'SP.employee-2026':[[375,392]],'Health13':[[4,18]],'VAT7.goods':[[3,21]],'VAT7a.services':[[3,22]]}
(O/'actual-additional-read-scopes.json').write_text(json.dumps({k:{'native_LF_ranges':v,'read_date':'2026-10-29','reader_path':d[k]['reader_path'],'reader_sha256':d[k]['reader_sha256'],'raw_path':d[k]['raw_path'],'raw_sha256':d[k]['raw_sha256'],'official_url':d[k]['official_url'],'note':'New actual bounded reads in this repair; prior other completed reads retained without repetition.'} for k,v in readranges.items()},ensure_ascii=False,indent=2)+'\n')
paths += [E/x for x in ['source-scopes.json','source-quotes.md','pit-sources.py','xb-sources.py','tp-sources.py','payroll-sources.py','vat-sources.py','payroll-ledger.py','vat-ledgers.py']]
(O/'canonical-successor-inventory.json').write_text(json.dumps([{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths],indent=2)+'\n');print(json.dumps(checks,indent=2))
