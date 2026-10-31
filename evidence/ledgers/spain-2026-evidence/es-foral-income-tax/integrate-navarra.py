# Parent writer's actual Navarra selections; no independent-review claim.
pn=Path('ledgers/spain-2026-evidence/root-navarra-pit')
for fp in [pn/'mixed-fragment.json',pn/'core-fragment.json',pn/'giving-landlord-fragment.json',pn/'home-pension-fragment.json',pn/'advance-residence-fragment.json',pn/'residence-fragment.json',pn/'other-fragment.json']:
 if not fp.exists():continue
 for z in json.loads(fp.read_text()):
  assert I[z['guide_LF']]==z['guide_wording']
  rp=Path(z['source_reader']);assert __import__('hashlib').sha256(rp.read_bytes()).hexdigest()==z['source_reader_SHA256']
  u=z['official_URL'];L.rows.append(dict(id=len(L.rows)+1,section=next(v['section']for v in L.units if v['line']==z['guide_LF']),guide_LF=z['guide_LF'],guide_wording=z['guide_wording'],provision=z['act_article'],url=u,quote=z['source_quote'],read_on=z['source_read_date'],kind=z['classification'],note=z['note']+' Actual Navarra selection/read by parent writer; integrated without an independent-review verdict.',raw_sha256=z['source_raw_SHA256'],reader=z['source_reader']))
  L.sources[u]=dict(selected_url=u,actual_raw_sha256=z['source_raw_SHA256'],reader=z['source_reader'],reader_sha256=z['source_reader_SHA256'],parent_writer_fragment=str(fp),parent_actual_native_LF=z['source_native_LF'])
