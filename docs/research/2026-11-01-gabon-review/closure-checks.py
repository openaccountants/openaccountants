import pathlib,json,subprocess,hashlib,re,sys
sys.path.insert(0,'/Users/michaelcutajar/Documents/ChatGPT/OA/output/finland-pack-2026-10-26/validation-deps')
import yaml
P=pathlib.Path('.');O=P/'docs/research/2026-11-01-gabon-review';W=P/'docs/research/2026-11-01-gabon-pack';H='d90a78e28adb1804d0e1fd904886dc16c00cd2bb';B='59c23acba2ad66dd2bb29ffc81ffbb9289769ef8'
def git(*a):return subprocess.check_output(['git',*a])
def sha(b):return hashlib.sha256(b).hexdigest()
def front(b):return yaml.safe_load(b.decode().split('---',2)[1])
def white(s):return re.sub(r'\s+',' ',s).strip()
receipt=json.loads((W/'writer-corrections.json').read_text());files=[]
for path,expected in receipt['candidate_files'].items():
 b=(P/path).read_bytes();files.append({'path':path,'sha256':sha(b),'expected_sha256':expected,'matches_frozen_writer_receipt':sha(b)==expected,'git_blob':git('hash-object',path).decode().strip()})
assert len(files)==6 and all(f['matches_frozen_writer_receipt'] for f in files)
before=json.loads(git('show',H+':'+str(W/'rules.json')));after=json.loads((W/'rules.json').read_text());bm={r['id']:r for r in before};am={r['id']:r for r in after}
changed=[rid for rid in bm if bm[rid]!=am[rid]];assert set(changed)=={'I-SHARES','P-CNSS','P-CAR','V-PRORATA','V-DOMCAP','V-FORESTCAP'}
support=[]
for rid,slug in [('P-CAR','ga-payroll-social'),('V-PRORATA','ga-vat-gst')]:
 ss=am[rid]['supporting_sources'];assert len(ss)==1
 s=ss[0];pdf=P/'../sources/cgi-2025.pdf';b=pdf.read_bytes();n=s['pdf_page_1_based'];text=subprocess.check_output(['pdftotext','-f',str(n),'-l',str(n),'-layout',str(pdf),'-']).decode();q=s['exact_original_language_quote'];ledger=(W/'ledgers'/(slug+'.md')).read_text();block=re.search(r'^## '+rid+r'\n(.*?)(?=^## |\Z)',ledger,re.M|re.S).group(1)
 support.append({'rule_id':rid,**s,'source_hash_matches':sha(b)==s['source_sha256'],'quote_on_claimed_actual_pdf_page':white(q) in white(text),'quote_in_matching_ledger_block':q in block,'url_and_hash_in_matching_ledger_block':s['official_url'] in block and s['source_sha256'] in block})
assert all(s['source_hash_matches'] and s['quote_on_claimed_actual_pdf_page'] and s['quote_in_matching_ledger_block'] and s['url_and_hash_in_matching_ledger_block'] for s in support)
meta=[]
for old in json.loads((O/'metadata.json').read_text()):
 slug=old['guide'];path='skills/gabon/'+slug+'.md';b=(P/path).read_bytes();prior=git('show',H+':'+path);m=front(b);prior_m=front(prior);s=b.decode();prior_s=prior.decode();ver=re.search(r'^# .* v([\d.]+)$',s,re.M)
 blocks=re.findall(r'```oa-check\n(.*?)```',s,re.S);prior_blocks=re.findall(r'```oa-check\n(.*?)```',prior_s,re.S)
 marker=b'<!-- openaccountants-cta-block -->';cta=True if marker not in prior else prior[prior.index(marker):]==b[b.index(marker):]
 hold=lambda x: re.search(r'^\*\*2026 draft and currency hold\.\*\*.*$',x,re.M).group(0)
 notconfirmed=lambda x: re.search(r'^Not yet confirmed:.*$',x,re.M).group(0)
 row={'guide':slug,'sha256':sha(b),'unchanged_from_original_candidate':b==prior,'description_words':len(m['description'].split()),'description_unchanged':m['description']==prior_m['description'],'version':m['version'],'h1_matches_version':bool(ver) and ver.group(1)==str(m['version']),'cta_unchanged':cta,'examples_byte_identical':blocks==prior_blocks,'example_count':len(blocks),'currency_hold_unchanged':hold(s)==hold(prior_s),'not_yet_confirmed_unchanged':notconfirmed(s)==notconfirmed(prior_s),'platform_and_author_fields_unchanged':{k:m.get(k)==prior_m.get(k) for k in ['authored_by','trust_label','license','review_status','drafted_by','approved_by','validation_status','validated','verified_by','reviewed_by']}}
 assert row['description_unchanged'] and row['h1_matches_version'] and row['cta_unchanged'] and row['examples_byte_identical'] and row['currency_hold_unchanged'] and row['not_yet_confirmed_unchanged'] and all(row['platform_and_author_fields_unchanged'].values())
 assert (b==prior)==(slug not in ['ga-vat-gst','ga-payroll-social'])
 meta.append(row)
unchanged=[]
for path in [str(W/'source-manifest.json'),str(W/'guide-inventory.json'),'skills/gabon/README.md',str(W/'old-files.json'),str(W/'old-topics.json'),str(W/'old-topic-map.md'),str(W/'README.md')]:
 b=(P/path).read_bytes();prior=git('show',H+':'+path);unchanged.append({'path':path,'sha256':sha(b),'unchanged_from_original_candidate':b==prior});assert b==prior
readme=front((P/'skills/gabon/README.md').read_bytes());assert len(readme['partial'])==7
findings={'F1':'closed: direct attribution precedes ratio, shared inputs only, original 90 percent hold preserved','F2':'closed: adjacent baseline non-cumulation expressly stated with CGI citation and currentness/commencement hold','F3':'closed: no employer total asserted in P-CNSS rule or matching ledger; pension split and branches unchanged','F4':'closed: both threshold source locators now article208 PDF73','minor_I_SHARES':'closed: six children expressly stated in rule and ledger'}
assert 'employer total18%' not in am['P-CNSS']['rule']
assert am['V-DOMCAP']['pdf_page_1_based']==73 and am['V-FORESTCAP']['pdf_page_1_based']==73
assert 'six children' in am['I-SHARES']['rule']
result={'date':'2026-11-01','prior_candidate':H,'base':B,'scope':'Frozen working-tree six-file repair closure; accepted only by exact content hashes, not by a new commit id','status':'Focused corrections accepted; original source review passes for the explicitly partial research draft only','findings':findings,'candidate_files':files,'writer_corrections_receipt_sha256':sha((W/'writer-corrections.json').read_bytes()),'unique_rule_records':len(after),'changed_rule_ids':changed,'supporting_source_checks':support,'guide_checks':meta,'historical_and_preservation_files':unchanged,'domain_partial_count':len(readme['partial']),'unchanged_example_blocks':sum(m['example_count'] for m in meta),'current_law_attestation':False,'country_complete':False,'authorized_publication_action_performed':False}
(O/'CLOSURE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Accepted frozen files:',len(files));print('Changed rules:',changed);print('Example blocks unchanged:',sum(m['example_count'] for m in meta));print('Partial domains:',len(readme['partial']));print('Receipt SHA256:',result['writer_corrections_receipt_sha256'])
