from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import hashlib, json, re, difflib

ROOT = Path(__file__).resolve().parent
GUIDES = Path('/Users/michaelcutajar/Documents/ChatGPT/OA/.claude/worktrees/europe-spain/skills/international/spain')
def sha(b): return hashlib.sha256(b).hexdigest()
def cents(v): return Decimal(v).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
def write_json(name, value): (ROOT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')
checks=[]
def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append({'name':name, 'actual':str(actual), 'expected':str(expected), 'pass':True})

cases = [
 {'id':'CLM-A', 'wages_gross':'22000', 'wages_other_expense':'2000', 'wages_net':'20000',
  'activity_gross':'0','activity_ordinary_rental_expense':'13000','activity_net':'-13000',
  'general_capital_gross':'0','general_capital_expense':'0','general_capital_net':'0','other_general_gain':'0',
  'G':'7000','B':'7000','S':'1000','selected_work_activity_N':'7000','QGE':'137.75','QGC':'137.75',
  'QSE':'95.00','QSC':'95.00','regional_total':'232.75','move_credit':'137.75','regional_liquid':'95.00',
  'explanation':'Activity loss belongs in the entitled individual mover\'s aggregate employment/activity numerator. This case alone is not an N>G discriminator.'},
 {'id':'CLM-B', 'wages_gross':'22000','wages_other_expense':'2000','wages_net':'20000',
  'activity_gross':'0','activity_ordinary_rental_expense':'0','activity_net':'0',
  'general_capital_gross':'1000','general_capital_expense':'14000','general_capital_net':'-13000','other_general_gain':'0',
  'G':'7000','B':'7000','S':'1000','selected_work_activity_N':'20000','QGE':'137.75','QGC':'137.75',
  'QSE':'95.00','QSC':'95.00','regional_total':'232.75','move_credit':'137.75','regional_liquid':'95.00',
  'explanation':'Loss outside employment/activity makes N>G. Actual credit equals QGC and does not consume the savings quota.'},
 {'id':'CLM-C', 'wages_gross':'22000','wages_other_expense':'2000','wages_net':'20000',
  'activity_gross':'0','activity_ordinary_rental_expense':'0','activity_net':'0',
  'general_capital_gross':'1000','general_capital_expense':'14000','general_capital_net':'-13000','other_general_gain':'1000',
  'G':'8000','B':'8000','S':'1000','selected_work_activity_N':'20000','QGE':'232.75','QGC':'232.75',
  'QSE':'95.00','QSC':'95.00','regional_total':'327.75','move_credit':'232.75','regional_liquid':'95.00',
  'explanation':'An additional positive general gain separates the observed QGC ceiling from a ratio using all positive components as denominator.'}
]
cases.append(dict(cases[2], id='CLM-D', B='7000', QGE='137.75', QGC='137.75',
                  regional_total='232.75', move_credit='137.75', global_pension_reduction='1000',
                  explanation='C inputs retained, valid individual pension contribution1000 accepted as a1000 reduction. Actual B7000<G8000 and move credit137.75 leave95 savings quota.'))
for c in cases:
 d={k:Decimal(v) for k,v in c.items() if k not in ['id','explanation']}
 check(c['id']+' wage net',d['wages_gross']-d['wages_other_expense'],d['wages_net'])
 check(c['id']+' activity net',d['activity_gross']-d['activity_ordinary_rental_expense'],d['activity_net'])
 check(c['id']+' general-capital net',d['general_capital_gross']-d['general_capital_expense'],d['general_capital_net'])
 check(c['id']+' general BI',d['wages_net']+d['activity_net']+d['general_capital_net']+d['other_general_gain'],d['G'])
 check(c['id']+' general BL',d['G']-d.get('global_pension_reduction',Decimal('0')),d['B'])
 check(c['id']+' work/activity aggregate N',d['wages_net']+d['activity_net'],d['selected_work_activity_N'])
 qg=cents((d['B']-Decimal('5550'))*Decimal('.095'))
 check(c['id']+' regional general quota',qg,d['QGC'])
 check(c['id']+' state general quota',qg,d['QGE'])
 qs=cents(d['S']*Decimal('.095'))
 check(c['id']+' regional savings quota',qs,d['QSC'])
 check(c['id']+' state savings quota',qs,d['QSE'])
 check(c['id']+' regional total',qg+qs,d['regional_total'])
 cap=min(Decimal('500'),qg,cents(qg*d['selected_work_activity_N']/d['G']))
 check(c['id']+' bounded cap method matches actual UI',cap,d['move_credit'])
 check(c['id']+' regional settlement',qg+qs-cap,d['regional_liquid'])
check('B unrestricted ratio before nominal cap',cents(Decimal('137.75')*Decimal('20000')/Decimal('7000')),Decimal('393.57'))
check('B unrestricted ratio after available total quota',min(Decimal('232.75'),Decimal('393.57')),Decimal('232.75'))
check('C unrestricted ratio before nominal cap',cents(Decimal('232.75')*Decimal('20000')/Decimal('8000')),Decimal('581.88'))
check('C unrestricted ratio after nominal and total quota caps',min(Decimal('500'),Decimal('327.75'),Decimal('581.88')),Decimal('327.75'))
check('C alternative all-positive-component denominator',cents(Decimal('232.75')*Decimal('20000')/Decimal('21000')),Decimal('221.67'))
check('B actual distinguishes unrestricted',Decimal(cases[1]['move_credit']) != Decimal('232.75'),True)
check('C actual distinguishes unrestricted',Decimal(cases[2]['move_credit']) != Decimal('327.75'),True)
check('C actual distinguishes positive component denominator',Decimal(cases[2]['move_credit']) != Decimal('221.67'),True)
check('D pension within ordinary annual amount',Decimal('1000') <= Decimal('1500'),True)
check('D pension within30%work/activity limit',Decimal('1000') <= Decimal('20000')*Decimal('.30'),True)
check('D unrestricted ratio before total quota cap',cents(Decimal('137.75')*Decimal('20000')/Decimal('8000')),Decimal('344.38'))
check('D unrestricted ratio after total quota cap',min(Decimal('232.75'),Decimal('344.38')),Decimal('232.75'))
check('D actual distinguishes unrestricted ratio',Decimal(cases[3]['move_credit']) != Decimal('232.75'),True)

common={
 'source':'Actual public AEAT Renta2025 OPEN version1.19 visible UI, 27October2026',
 'url':'https://www2.agenciatributaria.gob.es/wlpl/PARE-RW25/OPEN/index.zul?EJER=2025&TACCESO=COLAB',
 'own_tab':'1623102812','browser':'Brave1','other_tabs_not_claimed':['1623102787','1623102767'],
 'fictional_identity':{'nif':'12345678Z','name':'PRUEBA ASIGNACION','dob':'1980-01-01','sex':'male','civil_status':'single','region':'CASTILLA-LA MANCHA','individual_only':True},
 'common_inputs':{'children_ascendants_disability':False,'wage_SS_union_professional_legal_expenses':'0','wage_irregular_reduction':'0','national_unemployed_move_extra_expense_checkbox':False,'savings_interest_gross':'1000','savings_expenses':'0','all_withholdings':'0','global_BL_reductions':'0','other_credits':'0','move_current_year_checkbox':True,'move_prior_year_checkbox':False},
 'activity_inputs':{'type':'A05 remainder of professional activities','assessment':'N direct normal','gross_receipts':'0','rental_cost':'13000 only in A; zero in B/C','other_expenses_reductions':'0','IAE_detail':'not completed; these are calculation probes, not validated or file-ready returns'},
 'general_capital_inputs':{'classification':'rental of movable assets/business/mines, general basket','gross':'1000 in B/C','necessary_deductible_cost':'14000 in B/C','irregular_reduction':'0'},
 'general_gain_input_C':{'box':'other non-transfer general gains, amount gains','amount':'1000','loss':'0','status':'a hypothetical already-classified taxable general gain; the experiment does not establish a real receipt\'s classification'},
 'eligibility_assumptions':'Qualifying labour-related move, qualifying rural zone and work location, initial BL ceiling and residence continuity are assumed. The calculator checkbox does not prove those facts.',
 'observations':cases,
 'repeat':'After C, gain reset to zero and B re-observed. Then capital gross/cost reset to zero, activity rental cost restored13000, A repeated with the same result; full repeated quota AX saved. For D, C was recreated and ordinary individual pension contribution1000 entered; eligible reduction1000, B7000 and separate quota/result bodies actually observed.',
 'export':'The UI Guardar(.ses) control was attempted once with a documented download listener; listener timed out after20seconds. No successful session export is claimed. AX and screenshots are actual captured UI evidence.',
 'limits':'No2026 calculator tested; no filing or presentation clicked; finite UI controls do not expose internal engine code or establish every signed/joint/reduction case.'
}
write_json('browser-observations.json',common)

current=(GUIDES/'es-irpf-deductions.md').read_bytes()
before=current.decode()
(ROOT/'before-es-irpf-deductions.md').write_bytes(current)
intro='''**CLM individual signed-loss branch.** For an individual entitled mover, combine that person's reduced net employment and activity income in `N`; an activity loss is not omitted merely because the move was for employment. If a loss in another general-income category leaves positive `G` and `B` but makes that positive aggregate `N` exceed `G`, the CLM move attribution is limited to `QGC`: the credit before available-quota settlement is `min(500,QGC)`. It does not absorb savings quota. This is a legal application of the unchanged employment/activity-quota ceiling in art.12quater(1)(b), supported by actual fictional Renta2025 OPEN1.19 controls, rather than a tested2026 return campaign. For net wages20,000, net activity loss13,000 and savings1,000, `N=G=B=7,000` and `QGC=137.75`, so the credit is137.75. Replacing the activity loss with a general-capital loss13,000 gives `N=20,000>G=7,000`; the credit remains137.75, leaving95 savings quota. Adding a positive general gain1,000 makes `G=B=8,000` and `QGC=232.75`; the credit is232.75, still leaving95 savings quota. The under65 personal minimum is5,550. A further control retains `N=20,000`, `G=8,000` and savings1,000 and adds a valid individual pension contribution1,000: `B=7,000`, `QGC=137.75`, credit137.75 and regional liquid quota95. The first three controls have no global base reductions; the fourth confirms the separate pension-reduction step. No other credits apply. The current2026 scale and unchanged cap reproduce these amounts. Do not extend this individual CLM result to signed joint claims, other regions, an unestablished or nonpositive selected numerator, or shared wage/thalidomide expenses ([enacted cap, Law2/2021 DF9.Dosbis](https://www.boe.es/buscar/doc.php?id=BOE-A-2021-11513); [older BOE consolidation, operative art.12quater unchanged by the2026 amendment](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a1-6); [actual2026 amendment, art.18 and DF6](https://docm.jccm.es/portaldocm/verArchivoHtml.do?ruta=2026%2F03%2F30%2Fhtml%2F2026_2465.html&tipo=rutaDocm); [pension reduction, LIRPF51–52](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52); [AEAT cap and individual/joint income wording](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/10-cumplimentacion-irpf-deducciones-autonomicas/10_7-castilla-mancha/10_7_16-traslado-vivienda-habitual.html)).

'''
anchor='**Precise remaining boundaries.** '
assert before.count(anchor)==1
proposed=before.replace(anchor,intro+anchor,1)
old='The worksheet does not prescribe allocation where signed category income or losses make the selected numerator exceed general BI; do not silently cap that numerator or impose a favourable loss priority.'
new='Apart from the individual CLM branch just identified, the worksheet does not prescribe allocation where signed category income or losses make the selected numerator exceed general BI; do not silently cap that numerator or impose a favourable loss priority. Signed joint CLM claims and the other regions remain unconfirmed.'
assert proposed.count(old)==1
proposed=proposed.replace(old,new,1)
(ROOT/'proposed-es-irpf-deductions.md').write_text(proposed)
(ROOT/'surgical-proposal.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),proposed.splitlines(True),fromfile='es-irpf-deductions.md frozen current',tofile='private proposal only')))
oa=lambda s:re.findall(r'```oa-check\s*\n.*?```',s,re.S)
check('two original oa blocks retained',len(oa(before)),2)
check('all complete oa blocks byte-identical',oa(before),oa(proposed))
check('frontmatter byte-identical',before.split('---',2)[1],proposed.split('---',2)[1])
cta='<!-- openaccountants-cta-block -->'
check('full CTA and later platform text identical',before[before.index(cta):],proposed[proposed.index(cta):])
from collections import Counter
urls=lambda s:Counter(re.findall(r'https?://[^\s)>]+',s))
check('no original URL occurrence lost',bool(urls(before)-urls(proposed)),False)
check('no Guide mutation during evidence build',(GUIDES/'es-irpf-deductions.md').read_bytes(),current)
for name in ['README.md','es-income-tax.md']:
 b=(GUIDES/name).read_bytes();(ROOT/('before-'+name)).write_bytes(b)
write_json('controls.json',{'count':len(checks),'all_pass':True,'checks':checks})

(ROOT/'draft-options.md').write_text('''# Two private draft options, no Guide edit

Option A: add the bounded individual CLM method and its four discriminating controls immediately before the remaining-boundaries paragraph. Keep the existing positive-income table and controls unchanged. Narrow only the signed-loss reservation for that same individual CLM population. This is the supplied private surgical proposal.

Option B: retain the universal signed-loss reservation and add only a labelled CLM2025 official-calculator observation paragraph. State that the unchanged2026 law and scale reproduce the four numbers, while leaving adoption of a general individual N>G rule pending the root review. This publishes the new evidence without treating the finite probes as a complete signed-income allocation specification.

Both options keep signed joint CLM cases, every other region, shared wage/thalidomide expenses and the new Balearic rate open. Neither calls the observed result the internal calculator algorithm or an independently tested2026 return. All original examples, metadata, byline, CTA and source URLs remain.
''')

sources=[
 ('clm-current.html','https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368','art.12quater(1)(a)–(d)/(2),13bis; consolidated header31Jan2023/update pending. Actual relevant body read, not treated as a completed2026 consolidation.'),
 ('clm-original-law2-2021.html','https://www.boe.es/buscar/doc.php?id=BOE-A-2021-11513','DF9.Dosbis enacted original12quater, full cap/eligibility text.'),
 ('clm-law1-2026.html','https://docm.jccm.es/portaldocm/verArchivoHtml.do?ruta=2026%2F03%2F30%2Fhtml%2F2026_2465.html&tipo=rutaDocm','art18 entire eleven changes and DF6 actual current enactment: no12quater or13bis alteration. IRPF amendments apply from2025.'),
 ('aeat-clm2025.html','https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/10-cumplimentacion-irpf-deducciones-autonomicas/10_7-castilla-mancha/10_7_16-traslado-vivienda-habitual.html','complete2025 instructions, aggregate employment/activity of entitled contributor(s); input only year-of-move checkbox.'),
 ('lirpf-current.html','https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764','actual current19,20,26,48,51(1),52(1),56,74,76,77 read; excerpts retained.'),
 ('clm-current-authority-index.ax.txt','https://portaltributario.jccm.es/informacion-general/normativa-tributaria?field_titulo_a_mostrar_value=2026&term_node_tid_depth=All','actual browser view of regional index: Law8/2013 updated30Mar2026. Link itself ends literalellipsis, so linked consolidated body not read.')
]
write_json('source-read-receipts.json',[{'file':'sources/'+n,'url':u,'scope':s,'read_date':'2026-10-27','sha256':sha((ROOT/'sources'/n).read_bytes()),'bytes':(ROOT/'sources'/n).stat().st_size} for n,u,s in sources])
write_json('access-results.json',{'current_calculator':'Own new Brave tab1623102812 worked. Old tabs untouched.','failed_routes':[{'route':'non-escalated curl to BOE/AEAT','result':'DNS restricted; successful authorised escalated download followed'},{'url':'https://portaltributario.jccm.es/sites/portaltributario.castillalamancha.es/files/documentos/legislacion/20260415/ley_8-2013_21_de_noviembre_consolidada_v2.pdf','result':'web timeout, direct curl404; not read'},{'url':'https://portaltributario.jccm.es/node/1036','result':'web timeout, curl404; consultation body not read'},{'route':'actual current regional normative index via browser','result':'successful; current Law8/2013 link malformed with literalellipsis; actual index retained'}]})
write_json('frozen-guides.json',{n:{'sha256':sha((GUIDES/n).read_bytes()),'bytes':(GUIDES/n).stat().st_size} for n in ['README.md','es-income-tax.md','es-irpf-deductions.md']})

(ROOT/'report.md').write_text('''# Independent source assessment: CLM signed-income allocation

The new actual official2025 calculator evidence supports a bounded individual CLM signed-loss method, including an actually observed ordinary personal-pension B<G control. It does not close Spain I03, other regions, joint signed allocation, common wage/thalidomide expenses or Balearic3sexties' rate. No Guide, README or Git edits were made. A private surgical proposal and two options are supplied for root review.

## Concrete result and corrected test population

For one entitled individual mover, statutory/AEAT wording includes both employment and activity income. Net wages20,000 plus activity loss13,000 therefore gives selected aggregate N7,000, not20,000. The actual calculator confirms G=B7,000, general regional quota137.75, savings regional quota95, CLM0207 credit137.75 and regional liquid quota95. That original activity-loss case alone cannot distinguish a cap from the correctly aggregated numerator.

The decisive replacement uses a loss outside employment/activity: movable-asset rental general capital gross1,000 less necessary costs14,000 gives net−13,000. Net wages20,000 remain the whole selected work/activity numerator. Actual G=B7,000, QGC137.75 and QSC95 produce credit137.75. An unrestricted N/G result393.57 would consume the full232.75 regional quota at final settlement, unlike the observed137.75.

Adding an already-classified taxable non-transfer general gain1,000 gives G=B8,000, QGC232.75, QSC95, regional total327.75 and credit232.75, leaving95. Unrestricted N/G yields581.88 before nominal/final caps and327.75 after them. A denominator of21,000 made from positive components gives221.67. Both differ from actual232.75. The observed controls support limiting individual CLM attribution to QGC when its positive aggregate employment/activity numerator exceeds positive G. They do not reveal the engine's internal algorithm or establish all possible signed cases.

A fourth actual control retains C's N20,000/G8,000/S1,000 and adds an ordinary individual pension contribution1,000. The input dialog accepted it and the worksheet displayed an eligible reduction1,000; summary B is7,000. Actual QGC137.75, QSC95, total232.75, move credit137.75 and regional liquid95 confirm the cap after B<G. Unrestricted attribution344.38 would instead consume232.75. The contribution is below the ordinary1,500 annual limit and30% of the20,000 net work/activity sum under current LIRPF51/52.

## Source and2026 bridge

Actual enacted Law2/2021 DF9.Dosbis introduced Law8/2013 art12quater:500, initial BL ceiling, employment/activity regional-quota ceiling, joint entitled-contributor scope and residence continuity. Freshly downloaded BOE consolidated art12quater matches that operative wording. BOE's header is only consolidated through2023 and flags an update in progress, so it was not silently treated as a completed2026 source.

The actual DOCM Law1/2026 art18 was read through all eleven changes, with DF6. It changes rental caps and other listed provisions, adds12octies/nonies, and leaves12quater and the13bis scale unchanged; its IRPF amendments apply from2025. The current regional authority index visibly lists Law8/2013 updated30March2026. Its linked body is malformed and the search's oldPDF route returned404; neither was claimed read. The actual enactment, unchanged cap and current national quota/base rules provide the legal bridge. Application of the observed individual cap to2026 is expressly a legal inference, not an observed2026 programme result.

Fresh current LIRPF51/52 supports the fourth control's ordinary pension reduction. Fresh current LIRPF19/20 confirms wage22,000 less ordinary2,000 expense gives net20,000 and no low-wage reduction; the separate unemployed-move expense was not selected. Art26(1)(b) supplies the necessary-cost basis for the separate general-capital loss;48 distinguishes net category loss from the25%-limited general capital-gain-loss basket. Arts56/74/76 retain separate minima/general/savings tax;77(2) separately prevents a negative regional liquid quota. Current CLM13bis9.5% first band, minimum5,550 and savings9.5% reproduce all four observed amounts under2026 law. All entitlement facts remain assumptions of fictional probes.

## Scope of suggested delta

Option A inserts only a bounded individual CLM paragraph before the precise remaining-boundaries text and narrows that reservation by the same scope. The existing positive0≤N≤G table, reductions/rounding methods and every executable example stay unchanged. Option B publishes only the observed controls plus legal bridge, retaining broader method adoption pending root review. No source permits transferring the CLM ceiling to Aragón, Cantabria, Canarias or aid/thalidomide methods by analogy.

Still ordinary and open: signed joint CLM returns (including a non-entitled spouse's loss), general signed allocation for other regions/credits, negative or unestablished eligible numerators, shared employment costs/reductions between wages and thalidomide aid, new Balearic3sexties combined-versus-regional rate, and other reduction types/intersections outside the supplied individual control population; the ordinary1000 personal-pension reduction was actually observed in D. This is an independent source assessment, not an accountant attestation or a whole-country completeness finding.

## Evidence and controls

browser-observations.json is the typed input/action/result receipt; actual AX bodies and PNGs retain common wage/savings fields, loss input, general gain, move checkbox, summary and separate quota components. B and A were repeated after C. No filing was made. The optional.ses download listener timed out and no export success is asserted. Private proposed copy preserves all complete oa blocks, frontmatter, CTA and every prior URL occurrence. controls.json contains independent Decimal recomputations and preservation assertions. frozen-guides.json pins the three actual source files and manifest.json pins every evidence artifact except itself.
''')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='manifest.json']
write_json('manifest.json',{'scope':'source-only CLM individual signed-loss assessment and private proposal; no Guide/Git edits','files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(files)]})
print(json.dumps({'controls':len(checks),'all_pass':True,'proposal_sha256':sha(proposed.encode()),'manifest_sha256':sha((ROOT/'manifest.json').read_bytes()),'guide_sha256':sha(current),'files':len(files)},indent=2))
