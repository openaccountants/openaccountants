from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
import json
P=Path(__file__).parent;checks=[]
def cents(x):return x.quantize(D('.01'),rounding=ROUND_HALF_UP)
def check(id,actual,expected,scope):
 assert actual==expected,(id,actual,expected)
 checks.append({'id':id,'actual':str(actual),'expected':str(expected),'scope':scope,'arithmetic':'PASS'})
def scale(x):
 x=max(D('0'),D(x));out=D('0');previous=D('0')
 for end,rate in [(D('12450'),D('.095')),(D('20200'),D('.12')),(D('35200'),D('.15')),(D('60000'),D('.185')),(D('1e15'),D('.225'))]:
  part=min(x,end)-previous
  if part>0:out+=part*rate
  if x<=end:return cents(out)
  previous=end
 return cents(out)
def quota(G,joint='3400',pension='0',savings='1000',minimum='5550'):
 G=D(G);r=D(joint);p=D(pension);m=D(minimum);ss=D(savings)
 b=max(D('0'),G-r);remain=max(D('0'),r-G);ss=max(D('0'),ss-remain);b=max(D('0'),b-p)
 qg=scale(b)-scale(min(b,m));spill=max(D('0'),m-b);qs=max(D('0'),ss-spill)*D('.095')
 return b,cents(qg),cents(qs)
W=D('20000');L=D('-9000');K=D('1000');G=W+L+K;b,qg,qs=quota(G)
check('J1-general-rendimientos',W+L,D('11000'),'Current LIRPF48(a); wage and current professional loss integrate without a25%capital-loss limit')
check('J1-general-BI',G,D('12000'),'Positive general non-transfer gain added under48(b), not savings')
check('J1-joint-reduction',G-b,D('3400'),'LIRPF84(2).3 general first; no saving remainder here')
check('J1-general-BL',b,D('8600'),'Both spouses joint; no other general-base reduction')
check('J1-one-joint-minimum',D('5550'),D('5550'),'LIRPF84(2).2/57: under65 basic minimum once, not11100')
check('J1-gross-general-before-minimum',scale(b),D('817.00'),'CLM13bis first band9.5%')
check('J1-minimum-tax',scale('5550'),D('527.25'),'Minimum tax subtracted under LIRPF74(1).2')
check('J1-QGC',qg,D('289.75'),'Current law scale/minimum calculation; independent of software')
check('J1-QSC',qs,D('95.00'),'General BL exceeds5550, no minimum spillover; first savings band9.5%')
check('J1-regional-gross',qg+qs,D('384.75'),'General and savings quotas distinguished')
check('J1-total-BL',b+D('1000'),D('9600'),'Separate initial joint BL eligibility ceiling31485 passes; not attribution denominator')
N=W;raw=qg*N/G;wrongraw=qg*(W+L)/G
check('J1-eligible-member-N',N,D('20000'),'CLM12quater(1)(c),LIRPF11; only declarant is entitled')
check('J1-raw-eligible-ratio',cents(raw),D('482.92'),'Diagnostic raw ratio before QGC cap, not an uncapped authorised deduction')
check('J1-QGC-cap-hypothesis',min(D('500'),qg,cents(raw)),D('289.75'),'Current legal cap/eligible-member interpretation supported by root actual2025 J1 result; not my UI observation')
check('J1-competing-combined-N',W+L,D('11000'),'Alternative combines non-entitled spouse activity into numerator; distinguish from eligible-member selection')
check('J1-competing-credit',cents(wrongraw),D('265.60'),'Competing265.60 outcome, not the expected eligible-only method')
check('J1-distinguishing-difference',qg-cents(wrongraw),D('24.15'),'Observable difference between hypotheses')
check('J1-regional-liquid-if-cap',qg+qs-qg,D('95.00'),'Does not absorb savings tax')
# Both entitled uses statutory500 each and one combined attribution limit, not separate per-member caps.
check('J2-nominal-both-entitled',D('500')*2,D('1000'),'CLM12quater(1)(c); AEAT actual2025 unique-return limit on total1000')
check('J2-selected-combined-N',W+L,D('11000'),'Both spouses entitled: AEAT expressly aggregates both employment/activity results')
check('J2-predicted-ratio',cents(qg*(W+L)/G),D('265.60'),'Prediction from source scope; requires parent actual UI confirmation, no2026 software claim')
check('J2-predicted-credit',min(D('1000'),qg,cents(qg*(W+L)/G)),D('265.60'),'One overall cap on total nominal deduction')
check('J2-predicted-regional-liquid',qg+qs-cents(qg*(W+L)/G),D('119.15'),'Prediction only until actual result supplied')
# No general gain makes the two headline hypotheses coincide and cannot discriminate.
b0,q0,s0=quota(W+L)
check('J0-without-gain-G',W+L,D('11000'),'Source classifications otherwise unchanged')
check('J0-without-gain-B',b0,D('7600'),'Joint3400 remains')
check('J0-QGC',q0,D('194.75'),'Current law scale/minimum')
check('J0-one-eligible-cap',min(D('500'),q0,cents(q0*W/(W+L))),D('194.75'),'Prediction: capped eligible-member ratio')
check('J0-combined-hypothesis',cents(q0*(W+L)/(W+L)),D('194.75'),'Same as QGC; not discriminating')
# Additional diagnostic variants; no assertion these have been run in software.
b2,q2,s2=quota('13000')
check('D01-general-gain2000-QGC',q2,D('384.75'),'Hypothetical extra positive non-transfer gain changes G/B/QGC but not selected employment/activity')
check('D01-both-eligible-ratio',cents(q2*(W+L)/D('13000')),D('325.56'),'Prediction only, not observed')
bp,qp,sp=quota(G,pension='1000')
check('D02-pension-after-joint-B',bp,D('7600'),'LIRPF84(2).3 applies joint before51 reduction; valid1000 contribution assumed')
check('D02-pension-QGC',qp,D('194.75'),'General BL reduction changes quota, not G')
check('D02-both-eligible-ratio',cents(qp*(W+L)/G),D('178.52'),'Predicted diagnostic; no actualUI/2026 campaign claim')
bm,qm,sm=quota('8950')
check('D03-minimum-equality-B',bm,D('5550'),'Joint3400 plus basicmin5550; all positive G')
check('D03-minimum-equality-QGC',qm,D('0.00'),'No general tax to attribute despite positive selected income; no savings absorption')
check('D03-minimum-equality-QSC',sm,D('95.00'),'Minimum wholly consumed in generalBL at equality')
bs,qgs,qss=quota('7000')
check('D04-minimum-spillover-B',bs,D('3600'),'Independent positive-G variant')
check('D04-general-tax-zero',qgs,D('0.00'),'General minimum covers allgeneralBL')
check('D04-savings-minimum-spillover',qss,D('0.00'),'Remaining1950 minimum absorbs savings1000; do not infer a positive work attribution')
# Limits of deduction-source inference. These do not invent zero/negative selected numerator rules.
check('U01-negative-only-eligible','UNRESOLVED','UNRESOLVED','Spouse-only entitlement withN−9000 not established by positive-selected J1/J2; no silentmax(0)')
check('U02-nonpositive-G','UNRESOLVED','UNRESOLVED','No denominator-zero/negative general-base prescription from this bounded test')
check('U03-nominal1000-not-tested-by-binding-cap','SOURCE ONLY','SOURCE ONLY','J2 cap265.60 is below500, so observedJ2 alone does not distinguish500nominal from1000; statutory/manual wording supplies1000')
(P/'independent-decimal-controls.json').write_text(json.dumps({'kind':'Source-only independent Decimal arithmetic, with observed root J1 provenance and explicitly labelled unobserved predictions. No browser operation or Guide mutation.','checks':checks},indent=2)+'\n');print('checks',len(checks),'PASS')
# Actual root results now disprove the two direct aggregate predictions above. Retain the mathematical predictions as diagnostics, not verified method outputs.
observed={x['case']:x for x in json.loads((P/'actual-root-ui-values.json').read_text())}
hypotheses=[]
for id,G,B,Q in [('J2',D('12000'),D('8600'),D('289.75')),('J3',D('13000'),D('9600'),D('384.75'))]:
 actual=D(observed[id]['ANEXOB']);n=D('11000')
 candidates={
 'aggregate_final_cent':cents(Q*n/G),
 'aggregate_percentage_2dp':cents(Q*(n/G*100).quantize(D('.01'),rounding=ROUND_HALF_UP)/100),
 'each_member_quota_cent_then_sum':cents(Q*D('20000')/G)+cents(Q*D('-9000')/G),
 'general_average_percentage_4dp_then_allocation':cents((Q/B*100).quantize(D('.0001'),rounding=ROUND_HALF_UP)*B/G*n/100),
 'statutory_display_average_percentage_2dp_then_allocation':cents((Q/B*100).quantize(D('.01'),rounding=ROUND_HALF_UP)*B/G*n/100)}
 for k,v in candidates.items():hypotheses.append({'case':id,'hypothesis':k,'calculated':str(v),'actual_saved_root_UI':str(actual),'matches':v==actual,'authority_status':'NOT ESTABLISHED; matching two finite outputs does not identify an authoritative algorithm.'})
 assert candidates['aggregate_final_cent']!=actual
 assert candidates['each_member_quota_cent_then_sum']==actual
(P/'rounding-hypothesis-controls.json').write_text(json.dumps({'scope':'Actual root J2/J3 refute direct aggregate final-cent rounding. Per-member-rounded numerical coincidence is not certified as statutory/administrative method. LIRPF74(2)display precision alone does not establish this allocation.','comparisons':hypotheses},indent=2)+'\n')
for c in checks:
 if c['id'].startswith('J2-predicted') or c['id'] in ['D01-both-eligible-ratio']:
  c['scope']='Direct aggregate-ratio arithmetic diagnostic only; actual root J2/J3 results differ. This is NOT an established exact-credit method.'
(P/'independent-decimal-controls.json').write_text(json.dumps({'kind':'Independent Decimal arithmetic. All numerical assertions hold, but the direct aggregate model FAILS actual J2/J3 by one cent. No browser operations or live Guide mutation.','checks':checks},indent=2)+'\n')
# No-loss proof on the full private candidate.
from hashlib import sha256
from collections import Counter
b=(P/'before-v1.3.md').read_text();s=(P/'proposed-v1.4.md').read_text();oa=lambda t:__import__('re').findall(r'```oa-check\b[\s\S]*?```',t);re=__import__('re');urls=lambda t:Counter(re.findall(r'https?://[^\s<>\]\)]+',t));fm=lambda t:re.sub(r'(?m)^version: .*\n','',t.split('---',2)[1]);ind=lambda t:t[t.index('**CLM individual signed-loss branch.**'):t.index('\n\n',t.index('**CLM individual signed-loss branch.**'))]
by=b[b.index('<!-- openaccountants-cta-block -->'):]
# Existing team attribution is in frontmatter; this Guide has no separate body byline.
proof={'before_sha256':sha256(b.encode()).hexdigest(),'before_bytes':len(b.encode()),'proposed_sha256':sha256(s.encode()).hexdigest(),'proposed_bytes':len(s.encode()),'whole_original_oa_blocks_exact':oa(b)==oa(s),'oa_blocks':len(oa(s)),'whole_individual_CLM_paragraph_byte_exact':ind(b)==ind(s),'old_URL_occurrences':sum(urls(b).values()),'all_old_URL_multiplicities_retained':not bool(urls(b)-urls(s)),'protected_metadata_except_version_exact':fm(b)==fm(s),'H1_exact_no_old_body_version':re.findall(r'^# .*$',b,re.M)==re.findall(r'^# .*$',s,re.M),'H2_sequence_exact':re.findall(r'^## .*$',b,re.M)==re.findall(r'^## .*$',s,re.M),'byline_and_full_CTA_byte_exact':s.endswith(by),'live_Guide_baseline_unchanged':Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain/skills/international/spain/es-irpf-deductions.md').read_text()==b}
assert proof['oa_blocks']==2
assert all(proof[k] for k in ['whole_original_oa_blocks_exact','whole_individual_CLM_paragraph_byte_exact','all_old_URL_multiplicities_retained','protected_metadata_except_version_exact','H1_exact_no_old_body_version','H2_sequence_exact','byline_and_full_CTA_byte_exact','live_Guide_baseline_unchanged'])
(P/'private-preservation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
