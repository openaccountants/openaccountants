from pathlib import Path
import json,hashlib,copy,shutil
P=Path(__file__).resolve().parent;ROOT=P.parents[2];LEDGER=ROOT/'ledgers/es-foral-income-tax.md'
def delimit(rows):
 # Article94 is the sole attribution-payment paragraph at native1075. Everything after the next heading belongs to other provisions/reference matter.
 out=[];removed=[]
 for z in rows:
  if z['provision']=='Navarra DF174/1999 current article94' and not z['quote'].startswith('El pago fraccionado correspondiente a los rendimientos de actividades empresariales'):
   removed.append(z)
  else:out.append(z)
 rows[:]=out
 return removed
if __name__=='__main__':
 h=P/'history-74df1985-before-S-L32';h.mkdir(exist_ok=True)
 for f in ['rows.json','actual-source-read-scopes.json','handover.json','writer-status.md','write-ledger.py','navarra-supplement.py','old-topic-overrides.json','writer-separating-controls.json']:
  if (h/f).exists():assert (h/f).read_bytes()==(P/f).read_bytes()
  else:shutil.copyfile(P/f,h/f)
 
 if (h/'ledger.md').exists():assert (h/'ledger.md').read_bytes()==LEDGER.read_bytes()
 else:shutil.copyfile(LEDGER,h/'ledger.md')
 assert hashlib.sha256(LEDGER.read_bytes()).hexdigest()=='74df19856a5cf41afc1da883e856bbf3e0423da0c9a9ab1ed169caa1fcc2fffb'
 rows=json.loads((P/'rows.json').read_text());before=copy.deepcopy(rows);removed=delimit(rows);assert [z['id']for z in removed]==list(range(2409,2556));assert len(rows)==2530;assert {z['guide_LF']for z in before}=={z['guide_LF']for z in rows};assert all(z==before[z['id']-1]for z in rows)
 (h/'removed-rows-original.json').write_text(json.dumps(removed,ensure_ascii=False,indent=2)+'\n')
 scopes=json.loads((P/'actual-source-read-scopes.json').read_text());oldscopes=copy.deepcopy(scopes);sm={z['row']:z for z in scopes['rows']};scopes['rows']=[z for z in scopes['rows']if z['row']not in range(2409,2556)];assert len(scopes['rows'])==2530 and scopes['unmatched']==[]
 cats=[(2409,2409,'Additional-provision section heading'),(2410,2415,'DF174/1999 DA1 annuity reversion/certain-payment/counterinsurance'),(2416,2444,'DF174/1999 DA2 prior employment-in-kind valuations'),(2445,2448,'DF174/1999 DA3 fixed-asset register'),(2449,2462,'DF174/1999 DA4 credit-institution information obligations'),(2463,2466,'Historical annotation/deletion notes, not article94'),(2467,2468,'DF174/1999 DA9 exchange-traded funds'),(2469,2469,'Transitional-provision section heading'),(2470,2471,'DF174/1999 DT1 continuing filing/formal norms'),(2472,2473,'DF174/1999 DT2 pre1999 housing accounts'),(2474,2476,'DF174/1999 DT3 corporate-tax-credit dividends'),(2477,2478,'DF174/1999 DT4 information procedure'),(2479,2479,'Historical DT deletion annotation'),(2480,2483,'DF174/1999 DT6 reclassified rural land gains'),(2484,2484,'Derogatory-provision section heading'),(2485,2492,'DF174/1999 sole derogatory provision'),(2493,2493,'Final-provision section heading'),(2494,2495,'DF174/1999 DF1 delegated rulemaking'),(2496,2499,'DF174/1999 DF2 commencement/application'),(2500,2555,'Editorial normative-reference/amendment index and compilation disclaimer, not operative article94')]
 disposition=[]
 for z in removed:
  rid=z['id'];scope=sm[rid];cat=next(c for lo,hi,c in cats if lo<=rid<=hi);native=rid-1333;assert z['quote']==' '.join(Path(z['reader']).read_text().split('\n')[native-1].split())
  disposition.append(dict(original_id=rid,former_attached_guide_LF=739,actual_source_identity=cat,native_LF=[native,native],former_first_match_LF=[scope['LF_start'],scope['LF_end']],historical_archive=str(h.relative_to(ROOT))+'/removed-rows-original.json',archive_lookup_id=rid,disposition='Removed from active Guide quotation coverage: extraneous source tail beyond article94. Preserved verbatim as historical/reference-only evidence; no new Guide rule asserted and no deletion of source body.',active_guide_coverage=False))
 (P/'S-L32-removal-disposition-map.json').write_text(json.dumps(disposition,ensure_ascii=False,indent=2)+'\n')
 text=LEDGER.read_text();lines=text.split('\n');ops=[dict(original_line_index=i,row=int(l.split('|')[1].strip()),before=l)for i,l in enumerate(lines)if l.startswith('| ')and l.split('|')[1].strip().isdigit()and int(l.split('|')[1].strip())in range(2409,2556)];assert len(ops)==147
 out='\n'.join(l for i,l in enumerate(lines)if i not in {z['original_line_index']for z in ops});restored=out.split('\n')
 for op in ops:restored.insert(op['original_line_index'],op['before'])
 assert '\n'.join(restored)==text
 marker='Active quotation rows: 2,530. Stable original row IDs are retained with the explicitly archived S-L32 gap 2409–2555; this gap contributes no current Guide coverage.\n';out=out.replace('| # | Guide section',marker+'| # | Guide section',1)
 LEDGER.write_text(out);(P/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');(P/'actual-source-read-scopes.json').write_text(json.dumps(scopes,ensure_ascii=False,indent=2)+'\n')
 # Full inverse also removes the single active-count disclosure before restoring all removed lines.
 inv=out.replace(marker,'').split('\n')
 for op in ops:inv.insert(op['original_line_index'],op['before'])
 assert '\n'.join(inv)==text
 (P/'S-L32-exact-replacements.json').write_text(json.dumps(dict(finding='S-L32 bounded extraneous source-tail removal, no Guide edit',removed_lines=ops,inserted_current_count_disclosure=marker,exact_inverse=True,active_rows=2530,removed_rows=147,legitimate_article94_row=2408,legitimate_article94_native_LF=1075,all354_covered_Guide_units_unchanged=True,retained_row_IDs_unchanged=True),ensure_ascii=False,indent=2)+'\n')
 script=P/'write-ledger.py';s=script.read_text();assert s.count('L.save()')==1;s=s.replace('L.save()',"delimit94=runpy.run_path(str(L.p/'S-L32-delimit-article94.py'))['delimit']\ndelimit94(L.rows)\nL.save()");script.write_text(s)
 status=(P/'writer-status.md').read_text().replace('The ledger contains2,677 original-language quotation rows','The active ledger contains2,530 original-language quotation rows (the original2,677-row collection is retained in history)');status+='\nS-L32: article94 ends at genuine row2408/native1075. Exactly147 extraneous tail rows2409–2555/native1076–1222 are removed from active coverage, preserved verbatim with a complete old-ID→archive/provision/reference-only disposition map. Stable legitimate IDs and all354 covered Guide units remain unchanged. Current count2530; prior2677 counts describe preserved predecessors only. The source/Guide body, old-topic map, all arithmetic controls and original oa evidence remain exact. No new legal method or broader source reading claimed.\n';(P/'writer-status.md').write_text(status)
 (P/'S-L32-checks.json').write_text(json.dumps(dict(before_rows=2677,active_rows=2530,removed=147,removed_original_ids=[2409,2555],native_removed_LF=[1076,1222],retained_row_objects_exact=True,retained_scope_objects_exact=True,covered_Guide_units_before=354,covered_Guide_units_after=354,guide_sha256=hashlib.sha256((ROOT/'skills/international/spain/es-foral-income-tax.md').read_bytes()).hexdigest(),old_topic_map_exact=(h/'old-topic-overrides.json').read_bytes()==(P/'old-topic-overrides.json').read_bytes(),controls_exact=(h/'writer-separating-controls.json').read_bytes()==(P/'writer-separating-controls.json').read_bytes(),boundary_actual_read=[1074,1084],editorial_end_actual_read=[1211,1222],no_whole_removed_tail_substantive_read_claim=True),indent=2)+'\n')
 paths=[ROOT/z['path']for z in json.loads((h/'handover.json').read_text())]+[P/'S-L32-delimit-article94.py',P/'S-L32-exact-replacements.json',P/'S-L32-removal-disposition-map.json',P/'S-L32-checks.json'];pins=[dict(path=str(p.relative_to(ROOT)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(p.read_bytes()))for p in paths];(P/'handover.json').write_text(json.dumps(pins,indent=2)+'\n')
 for p in[LEDGER,P/'rows.json',P/'actual-source-read-scopes.json',P/'handover.json',P/'S-L32-exact-replacements.json',P/'S-L32-removal-disposition-map.json']:print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),len(p.read_bytes()))
