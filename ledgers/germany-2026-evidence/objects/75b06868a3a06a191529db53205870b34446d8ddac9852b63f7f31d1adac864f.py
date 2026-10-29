"""Complete rental writer inventory and bind its exact finite evidence chain."""
from pathlib import Path
import json,hashlib,re,subprocess,sys,datetime
B=Path(__file__).parent
ROOT=Path('/Users/michaelcutajar/Documents/ChatGPT/OA')
G=ROOT/'.claude/worktrees/europe-germany/skills/international/germany/de-rental-income.md'
sha=lambda b:hashlib.sha256(b).hexdigest()
save=lambda n,d:(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(B/'build-core-evidence.py')],check=True)
subprocess.run([sys.executable,str(B/'build-old-topics.py')],check=True)
core=json.loads((B/'current-core-bindings.json').read_text())
quotes=json.loads((B/'actual-source-quotes-core.json').read_text())
catalog=json.loads((B/'cited-source-identities-candidates.json').read_text())['sources']
sources={v['source_id']:v for v in catalog.values()}
byid={q['id']:q for q in quotes}
current=G.read_text().splitlines()
guide_sha=sha(G.read_bytes())
CORE={x['native_LF']:x for x in core}
EXTRA={
3:(['R01','R04','R07','R08','R11','R14','R18','R20','R22','R23','R24','R42','R57','R59','R62','R68','R70','R73','R74','R95','R96'],'Scoped summary of the bound methods and explicit sibling exclusions.'),
35:(['R83','R04','R11','R14','R18','R20','R22','R24','R28','R119','R85','R86','R87'],'Year framing; dated2025/2026commuting distinction is explicit in192.'),
183:(['R18','R19','R24','R42','R112','R113'],'Writer order of operations follows building-cost denominator and cost-apportionment bases; co-owner allocation is illustrative, determination outside scope.'),
185:(['R04','R07','R11','R18','R20','R24','R32','R33'],'Conservative temporary workflow pending actual missing facts, not a determination that unresolved works are legally production cost.'),
189:(['R120','R47'],'Actual official forms and their scoped uses; ELSTER route is the source medium, not an assertion of a universal electronic-filing obligation.'),
194:([],'Historical route observation and explicit2025line-map limitation. DE-L25 corrects unsupported publication-absence inference; exact prior observations and failures retained.'),
196:(['R120'],'Dated2025form-table label; bank keywords are editorial, not official return labels.'),
200:(['R133'],'Dated2025form fields6–12.'),
201:(['R49'],'Dated2025form fields13–19; bank keywords editorial.'),
202:(['R49'],'Dated2025form fields20–24; bank keywords editorial.'),
203:(['R49','R50'],'Dated2025form fields25–31.'),
204:(['R44'],'Dated2025form totalincome32, official example.'),
205:(['R35','R37','R94','R39','R134'],'Dated2025form depreciation33–45 headings;7h/7i calculations excluded.'),
206:(['R40'],'Dated2025form interest/financing46–51.'),
207:(['R41','R20','R21'],'Dated2025form maintenance55–72.'),
208:(['R51','R52'],'Dated2025form passed/unpassed73–78; particular bank keyword mapping is editorial and distinguished in212.'),
209:(['R51','R52','R39','R27'],'Dated2025form other-cost80–83; income-related examples subject to9(1), no automatic expense eligibility.'),
210:(['R45','R46','R50','R52','R42'],'Dated2025form result/share/cut/grant fields85–89.'),
212:(['R40','R41','R50','R51','R52','R32','R27','R131'],'Explicit editorial keyword interpretation, with income/asset/trust exclusions. No official keyword list invented.'),
219:(['R101','R102','R130','R56'],'Scoped correction/criminal referral with actual interest-period qualification; does not select a complete procedural route.'),
224:(['R111','R112','R120'],'Resident foreign-income/reporting scope and actual-treaty referral; no unsourced general treaty result selected.'),
230:(['R44','R45','R46'],'Fixture provenance: invented first case, actual official2025second case, all before tariff.'),
303:(['R04','R07','R11','R12','R14','R133'],'Decision-fact intake, no invented client facts.'),
304:(['R03','R07','R13','R20','R24','R47','R48','R62'],'Decision-fact intake, no invented client facts.'),
305:(['R32','R35','R122','R123'],'Decision-fact intake, no invented client facts.'),
306:(['R24','R42','R43','R58'],'Decision-fact intake, no invented client facts.'),
307:(['R18','R19','R33','R41'],'Decision-fact intake, no invented client facts.'),
308:(['R111','R108','R76','R120','R131'],'Decision-fact intake; co-owner/treaty/determination outcomes handed off.'),
340:([],'Precise Not-yet-confirmed scope and historical route/body-read limits. This is not proof of absence or a completed specialist/treaty method. DE-L25/26 settle only their named old questions; original limits preserved in their preimages.'),
}
scope={30:'Declared excluded/specialist scope; not a substantive outcome.',31:'Sibling routing links; existing paths are preserved.',226:'Part-year routing to sibling.'}
rows=[]
in_oa=False
oa_case=0
for n,s in enumerate(current,1):
 if not s.strip():continue
 if s=='```oa-check':
  in_oa=True;oa_case+=1
 if n in CORE:
  x=CORE[n];kind='rule_or_figure_or_fixture';anchors=x['anchors'];note=x['status']
 elif n in EXTRA:
  anchors,note=EXTRA[n];kind='scope_limit' if n in [194,340] else 'rule_summary_or_method_or_intake'
 elif n in scope:
  anchors=[];note=scope[n];kind='scope_routing'
 elif in_oa:
  anchors=['R04','R27','R29','R30','R31','R41'] if oa_case==1 else ['R24','R42','R44','R45','R46']
  note=f'Original executable case{oa_case}; exact block retained. Fixture inputs are not statutory thresholds; parameter rules and expected arithmetic independently checked.'
  kind='original_executable_fixture'
 elif n<=16:
  kind='preserved_metadata';anchors=[];note='Existing identity/protected trust metadata; version/date record actual writer changes, not independent attestation.'
 elif s.startswith('#'):
  kind='structure';anchors=[];note='Heading; all operative amounts/methods have separate bound rows.'
 elif s.startswith('|---') or s.startswith('| Item |') or s.startswith('| Rent including') or s.startswith('| Lines |') or s.startswith('| Source |'):
  kind='structure';anchors=[];note='Table header or separator; no independent operative amount.'
 elif 314<=n<=338:
  kind='historical_source_record';anchors=[];note='Preserved original source URL/read-on citation record. Root actual read date is29October2026 in the quote index; earlier dates are not relabelled as root reads.'
 elif n>=342 or n==20:
  kind='protected_reference_disclaimer_or_CTA';anchors=[];note='Protected original reference/CTA language, retained exactly; no new tax or attestation claim.'
 elif n in [108,147]:
  kind='source_pointer';anchors=['R88','R89','R90','R91','R92','R93'] if n==108 else ['R53','R57','R59','R66','R68'];note='Pointer to the actual bound official letter/handbook quotations.'
 elif s in ['---','```']:
  kind='structure';anchors=[];note='Structural marker.'
 else:raise AssertionError(('Unclassified current unit',n,s))
 assert all(x in byid for x in anchors),(n,anchors)
 assert not any(x in note.lower() for x in ['partial:','pending:','needs source','needs reading']), (n,note)
 rows.append(dict(native_LF=n,section=next((current[i][2:] for i in range(n-1,-1,-1) if current[i].startswith('## ')),'metadata/title'),
   wording=s,classification=kind,anchors=anchors,disposition=note,guide_sha256=guide_sha))
 if s=='```' and in_oa:in_oa=False
assert oa_case==2 and not in_oa
assert len(rows)==sum(bool(s.strip()) for s in current)

# Validate quote identity, exact reader containment and true native-LF positions.
checks=[]
for q in quotes:
 src=sources[q['source_id']];raw=Path(src['path']).read_bytes();reader=Path(src['reader_path']).read_bytes();text=reader.decode()
 assert sha(raw)==q['source_sha256'] and sha(reader)==q['reader_sha256']
 excerpt=q['exact_original_language_quote'];display=text.splitlines(keepends=True)
 lo,hi=q['selected_reader_display_lines'];start=sum(len(x) for x in display[:lo-1]);stop=sum(len(x) for x in display[:hi])
 at=text.index(excerpt,start,stop)
 native=[text[:at].count('\n')+1,text[:at+len(excerpt)-1].count('\n')+1]
 assert native==q['reader_native_LF'],q['id']
 checks.append({'quote':q['id'],'source_id':q['source_id'],'exact_containment':True,'raw_reader_hashes':True,'native_LF':native})
save('current-rule-rows.json',rows)
save('source-quotes.json',quotes)
used={q['source_id'] for q in quotes}
save('source-identities.json',[sources[x] for x in sorted(used)])
save('quote-binding-checks.json',checks)
old=json.loads((B/'old-topics.json').read_text())
controls=json.loads((B/'writer-arithmetic-core.json').read_text())
assert all(x['result']=='PASS' for x in controls)
main=(B/'main-baseline.md').read_text()
blocks=lambda t:re.findall(r'```oa-check\n.*?```',t,re.S)
assert blocks(main)==blocks(G.read_text()) and len(blocks(main))==2
original=(B/'pre-refresh-original.md').read_text()
assert original.split('<!-- openaccountants-cta-block -->')[1]==G.read_text().split('<!-- openaccountants-cta-block -->')[1]
save('final-writer-checks.json',dict(current_units=len(rows),exact_quote_checks=len(checks),source_identities=len(used),
    pre_refresh_origins=len(old['pre_refresh_rows']),main_origins=len(old['main_baseline_rows']),unclassified=0,
    original_oa_byte_exact=2,writer_controls=len(controls),scope_limits='Explicit per-row/Guide limits retained; not an ordinary full-country completeness verdict.',
    independent_review='not yet performed'))
esc=lambda s:str(s).replace('|','\\|').replace('\n','<br>')
a=['# de-rental-income figure ledger','',
   'Writer ledger prepared for the different whole-country reviewer. No independent PASS or accountant attestation.','',
   f'Guide SHA256 `{guide_sha}`. Actual source read date29October2026. {len(rows)}current units; {len(quotes)}selected exact quote anchors; {len(used)}source identities; {len(controls)}writer arithmetic/calendar controls;2original executable blocks preserved byte-exact.','',
   'Source hashes and exact quote native-LF coordinates are checked in quote-binding-checks.json. PDF page breaks remain in the quoted text; selected display coordinates are separately recorded. Earlier coordinate/old-destination drafts and failures are preserved. RNT08 is an official indexed web observation, not rawHTML; the open503 failures remain separate. The2019deposit reasoning is corroborative with its2021appeal reversal explicitly retained; it is not presented as an unreversed BFHholding.','',
   '## Figures, rules, fixtures and scope','', '| Current LF | Section | Wording | Classification | Quote IDs | Disposition |','|---|---|---|---|---|---|']
for x in rows:a.append('| '+' | '.join(esc(x[k]) if k!='anchors' else ','.join(x[k]) for k in ['native_LF','section','wording','classification','anchors','disposition'])+' |')
a+=['','## Exact original-language source quotations','']
for q in quotes:
 a+=['### '+q['id']+' '+q['act_article'],'',q['official_url'],'',
     f'Read{q["read_on"]}; {q["source_id"]} nativeLF{q["reader_native_LF"]}; source kind: {q["source_kind"]}.','',
     '```text',q['exact_original_language_quote'],'```','',q['note'],'']
a+=['## Old topics carried','',
    'Every nonblank original source unit has a concrete destination. Full old/current wording and specific notes are in old-topics.json. Earlier source-unconfirmed items remain as limits or are explicitly settled by the named sourced correction; archival text is not silently deleted.','',
    '| Origin | Old LF | Current LF | Disposition |','|---|---|---|---|']
for key in ['pre_refresh_rows','main_baseline_rows']:
 for x in old[key]:a.append('| '+esc(x['origin'])+' | '+str(x['old_native_LF'])+' | '+','.join(map(str,x['destination_current_native_LF']))+' | '+esc(x['status'])+' |')
a+=['','## Writer changes and remaining limits','',
    'DE-L22 restores the pre2006historic housing cut-off. DE-L24 restores five omitted case/rule details. DE-L25 distinguishes route failure from publication absence and binds the dated2025commuting rate. DE-L26 resolves furnished market comparison from the actual court method. DE-L27 qualifies interest and actual-treaty referrals. Each has saved options, preimages, operations and exact inverse proofs.','',
    'The2026form/line numbers and later update of the2004letter remain unconfirmed. The shorter-life letter, rental first-place classification, sale-month AfA, heirs-community treatment, foreign-treaty outcomes and paid-usufruct-waiver letter remain explicit limits. This ledger does not convert those limits into positive instructions.']
(B/'de-rental-income.md').write_text('\n'.join(a)+'\n')
save('reading-progress.json',{'date':'2026-10-29','status':'Writer ledger complete with precise retained limits; ready for different country review, not independent PASS.',
    'current_guide_sha256':guide_sha,'current_units':len(rows),'exact_quotes':len(quotes),'source_identities':len(used),
    'old_topic_origins':len(old['pre_refresh_rows'])+len(old['main_baseline_rows']),'unclassified':0,'writer_controls':len(controls),
    'actual_read_scope_index':'actual-read-scopes.json','quote_checks':'quote-binding-checks.json'})
print(json.dumps({'status':'writer ledger prepared','Guide_sha256':guide_sha,'ledger_sha256':sha((B/'de-rental-income.md').read_bytes()),
 'current_units':len(rows),'quotes':len(quotes),'old_origins':len(old['pre_refresh_rows'])+len(old['main_baseline_rows']),
 'controls':len(controls),'sources':len(used),'independent_review':False},indent=2))
