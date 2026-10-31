from pathlib import Path
import json,hashlib,re,collections,difflib
W=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain');O=Path('/Users/michaelcutajar/Documents/ChatGPT/OA/output/europe-closeout-2026-10-27/spain-ledger-review');E=W/'ledgers/spain-2026-evidence/es-irpf-deductions';G=W/'skills/international/spain/es-irpf-deductions.md'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();N=lambda s:' '.join(s.split());J=lambda p:json.loads(p.read_text());D=lambda n,a:(O/n).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
u=J(O/'tranche18-unique-quotes.json');covered={};fresh=[]
for b in J(O/'tranche18-source-read-batches.json')[:8]:fresh.extend(b if isinstance(b,list) else b['quotes'])
for b in J(O/'tranche18-residual-source-batches.json'):fresh.extend(b['quotes'])
for q in fresh:covered[q['i']]={'method':'new actual bounded quote reading','quote_rows':q['quote_rows']}
for fn,key in [('tranche18-exact-prior-ledger-reuse.json','quote_i'),('tranche18-prior-regional-reuse.json','quote_i')]:
 a=J(O/fn)
 if isinstance(a,dict):a=a['reuse']
 for z in a:covered.setdefault(z[key],{'method':'exact attributed prior read reuse','receipt':fn})
for z in J(O/'tranche18-prior-core-catalogue-reuse.json')['reuse']:covered.setdefault(z['i'],{'method':'earlier independent normalized core read reuse','receipt':'tranche18-prior-core-catalogue-reuse.json'})
for z in J(O/'tranche18-contained-quotes.json'):
 assert z['inside'] in covered,z
 covered.setdefault(z['i'],{'method':'same-reader quote wholly contained in actually assessed quotation','inside':z['inside']})
assert len(covered)==len(u),(len(covered),len(u),[z['i'] for z in u if z['i'] not in covered])
allrows={n for z in u if z['i'] in covered for n in z['quote_rows']};assert allrows==set(range(1,6346))
D('tranche18-source-coverage-final.json',{'scope':'All selected quotations assessed. No full-source-body reading implied. Unadopted auxiliary-emission proposal excluded.','unique_reader_quote_pairs':len(u),'selected_scope_rows':len(allrows),'exclusive_counts':dict(collections.Counter(z['method'] for z in covered.values())),'coverage':covered})
# S-L33 finite proof
hist=E/'history/pre-S-L33-d633/support';print('histfiles', [p.name for p in hist.iterdir()][:7]);ops=J(E/'S-L33-operations.json');now=(E/'check-ledger.py').read_text();before=now
for z in reversed(ops):assert before.count(z['after'])==1;before=before.replace(z['after'],z['before'],1)
oldcheck=hist/'check-ledger.py';assert before==oldcheck.read_text()
a=J(hist/'supplementary-numeric-controls.json');b=J(E/'supplementary-numeric-controls.json');changes=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y];assert len(a)==len(b)==89 and len(changes)==5
for z in J(E/'S-L33-artifact-manifest.json'):assert H(W/z['path'])==z['sha256']
assert H(W/'ledgers/es-irpf-deductions.md')=='d633dd1d7044ab3ec29efd14fbe5aed88286bbe77ed25678b18eb905417e037e'
for f in ['claim-rows.json','actual-read-quotes.json','old-topics.json','source-identities.json']:assert (E/f).read_bytes()==(hist/f).read_bytes(),f
D('tranche18-S-L33-independent-proof.json',{'manifest_sha256':H(E/'S-L33-artifact-manifest.json'),'five_exact_checker_operations':len(ops),'full_inverse':True,'changed_numeric_records_zero_based':changes,'unchanged_numeric_records':84,'Guide_ledger_sources_claims_oldmap_unchanged':True,'own_recomputation':'separate tranche18-controls.json'})
# Preservation: frozen published old body -> exact current two-line delta
old=(E/'published-guide.md').read_text();cur=G.read_text();aa=old.split('\n');bb=cur.split('\n');delta=[(i+1,x,y) for i,(x,y) in enumerate(zip(aa,bb)) if x!=y];assert len(aa)==len(bb) and [x[0] for x in delta]==[4,1261]
assert aa[4:1260]==bb[4:1260] and aa[1261:]==bb[1261:]
case=lambda s:re.findall(r'```oa-check\s*\n.*?```',s,re.S)
if not case(cur):case=lambda s:re.findall(r'```oa\s*\n.*?```',s,re.S)
assert case(old)==case(cur) and len(case(cur))==2
url=lambda s:re.findall(r'https?://[^\s)<>]+',s)
assert url(old)==url(cur)
D('tranche18-preservation.json',{'current_Guide_sha256':H(G),'published_baseline_sha256':H(E/'published-guide.md'),'exact_changed_native_LF':[4,1261],'delta':delta,'all_other_bytes_in_lines_exact':True,'original_two_oa_exact':True,'ordered_URLs_exact':True,'protected_metadata_byline_CTA': 'all identical except authorised versionLF4; body delta1261 is sourced S-L25 scope correction'})
# Actual origin identities and all exact old routes, independent semantic spots remain documented separately
oldunits=J(E/'old-topics.json');bodies={'62b7639a5a68324a83a96bb0190fff8b7c76f8c5':(E/'prior-main-guide.md').read_text(),'0b5e62451de50220ac6d80c7813d547d08108641':old};assert all(N(x['wording']) in N(bodies[x['ref']]) for x in oldunits)
exact=0
for x in oldunits:
 if x['destination'].startswith('Current LF') and ':exact original unit.' in x['destination']:
  assert N(x['wording']) in N(cur);exact+=1
D('tranche18-old-origin-integrity.json',{'old_units':len(oldunits),'all_actual_origin_wordings_present':True,'exact_current_destinations_checked':exact,'semantic_spots':'separate tranche18-old-topic-spots.json; not all1413units freshly reread'})
print('PASS',len(u),len(allrows),len(fresh),collections.Counter(z['method'] for z in covered.values()),'oldunits',len(oldunits),'exact',exact)
