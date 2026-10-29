"""Explicit semantic destinations for every nonblank old rental source unit."""
from pathlib import Path
import json, hashlib
B=Path(__file__).parent
R=Path('/Users/michaelcutajar/Documents/ChatGPT/OA')
G=R/'.claude/worktrees/europe-germany/skills/international/germany/de-rental-income.md'
current=G.read_text().splitlines()
old=(B/'pre-refresh-original.md').read_text().splitlines()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

# Native old LF: current destination LF(s). These were compared semantically after
# reading the old and current bodies. Metadata/structure is marked separately below.
M={22:[24,25,82,95,115,129,154,167,173,189],24:[24,25,26],25:[28,192],
26:[194],27:[29,69],28:[31,226,303,308],
32:[303],33:[304],34:[305],35:[125,306],36:[307],37:[304,158,162],38:[303],39:[308],41:[185],
45:[24,25],46:[189],47:[67,69],48:[87,88],49:[82,86,89],50:[95,102],
51:[115],52:[117],53:[75,77],54:[129,130,131,135,141],55:[166,167,168,183],
56:[189,190,191,192,193],57:[173,175],59:[183],63:[35],
67:[39,40,41],68:[42,86],69:[43,95],70:[44,98],71:[45,98,102],72:[46,115],
73:[48,121],74:[49,50,129,131],75:[51,76],76:[52,76],77:[55,167],78:[56,168],
79:[54,176],80:[57,190],81:[59,162],82:[58,193],83:[60,216],
89:[67],90:[68],91:[69],95:[82],96:[83,340],97:[84],98:[85],99:[86],
100:[87],101:[88],102:[89],103:[91],
105:[93],107:[95],109:[97],110:[98],111:[99],112:[100],113:[101],
115:[95],117:[102],118:[103],119:[104],120:[105],122:[108],
126:[73],128:[75],129:[76],130:[77],134:[112],135:[113],136:[114],
137:[115],138:[117],142:[121,340],146:[125],150:[129],151:[130,135,141],152:[131],
154:[133],155:[134],156:[135,136,137,138,139,140,141],157:[142],158:[143],
162:[151],163:[152,189],164:[153],165:[147,154,155,156,157],166:[158],
170:[162],174:[166],175:[167],176:[168],177:[169],178:[149,150,157],179:[193],
183:[173],184:[174],185:[175],186:[176],187:[177],188:[178],
194:[82],195:[86],196:[86],197:[97],198:[98],199:[102],200:[115],201:[117],
202:[129,130,131],203:[143],204:[173],205:[176],206:[193],207:[190],208:[162],
212:[230],216:[90],217:[90],218:[90],219:[90,193],220:[90],221:[90],
225:[116],226:[116],227:[116],228:[116],
232:[266],233:[268],234:[268],235:[268],236:[268],
240:[106],241:[106],242:[106],243:[106],244:[106],
248:[179],249:[179],250:[179],254:[193],255:[193],256:[192],
260:[25,30],261:[27,223,224],262:[135,149,150,157],263:[154,155,156,158],
264:[83,84,340],265:[103,104,30],266:[116],267:[30],268:[121,143,169,340],
269:[31,173,223,224],273:[189],274:[190],275:[191],276:[216],277:[193],
281:[192,216],282:[192,216],283:[192,194],287:[194,196],
291:[200],292:[201],293:[202],294:[203],295:[204],296:[205],297:[206],
298:[207],299:[208],300:[209],301:[210],303:[212],
307:[24,189,194],308:[67,69],309:[82,86,87,88,89],310:[95,97,98,100,102],
311:[115,117],312:[77],313:[129,130,131,134,135],314:[166,167,168,193],
315:[173,175,176],316:[191,216,20],320:[314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338],
324:[20,353,354,355],
}
heading_map={'## Scope':[22], '## Ask the client first':[301], '## The method, step by step':[181],
 '## Figures for 2026':[33], '## The rules':[63], '## Boundaries and exceptions':[125,145,221],
 '## Worked cases':[228], '## When to refuse or refer':[30,340], '## Filing and payment':[187],
 '## Returns being filed now: tax year 2025':[192], '## Anlage V line map (2025 form)':[196],
 '## Completion checklist':[183,185,301], '## Sources':[310], '## Disclaimer':[20],
 '### Werbungskosten':[71], '### Maintenance or production cost':[110], '### Furniture':[119],
 '### Cheap lets':[123], '### Vacancy, holiday flats and short-term lets':[145],
 '### VAT option on commercial lets':[160], '### Losses':[164], '### Sale within ten years':[171],
 '### Building depreciation':[80], '### Income and timing':[65]}
case_head={214:[90],223:[116],230:[264],238:[106],246:[179],252:[193]}
M.update(case_head)
rows=[]
for n,s in enumerate(old,1):
 if not s.strip():continue
 if n in M:
  dest=M[n]; status='Carried to the listed current wording'
  note='Semantic writer comparison; source validation is separately recorded, not implied by this destination.'
  if n in [156,165,178,262,313]:note+=' Earlier source-unconfirmed/referral material is retained and expanded with actual handbook quotations; current legal scope remains explicit.'
  if n==97:note+=' Explicit pre2006 gate restored by root DE-L22; prior v1.1 omission retained in before.md.'
  if n in [135,163,216,217,218,219,220,227,282]:note+=' Complete omitted detail restored by DE-L24 after the initial destination-table draft overstated full carriage. That exact draft is preserved under DE-L24-options.'
  if n in [219,227]:note+=' Prior arithmetic is represented by the retained prose inputs/result or bound equation; all original arithmetic separately recomputed.'
  if n in [96,187,268]:note+=' Remaining Not-yet-confirmed limits remain visible; no unsupported positive rule added.'
  if n==142:note+=' Earlier furniture-market uncertainty was resolved by actual BFHIXR14/17 reading and DE-L26. The old question and exact wording remain in the retained preimage.'
  if n==26:note+=' DE-L25 distinguishes empty source response from publication absence; historical source observations remain preserved.'
 elif n<=18:
  dest=[min(n,len(current))];status='Metadata/title retained or dated version/summary updated';note='Not a separate legal proposition; exact original preserved in pre-refresh-original.md.'
 elif n>=326:
  offset=next(i+1 for i,v in enumerate(current) if v=='<!-- openaccountants-cta-block -->')-326
  dest=[n+offset];status='Protected CTA/footer carried byte exact';note='Preservation checked against original suffix.'
 elif s.startswith('#'):
  matches=[v for k,v in heading_map.items() if s.startswith(k)]
  assert matches,(n,s)
  dest=matches[0];status='Section heading relocated';note='Structural label; detailed old substantive rows have their own destinations.'
 elif s.startswith('|'):
  # Only structural table header/separator lines reach this branch.
  assert all(k not in s for k in ['Straight-line','Loss','Private sale','EUR','%']), (n,s)
  dest=[33 if n<85 else 123 if n<160 else 171 if n<210 else 196]
  status='Structural table header retained in successor table';note='No independent tax rule in this header/separator.'
 elif s=='---':
  dest=[18];status='Structure';note='Horizontal rule only.'
 else:raise AssertionError((n,s))
 assert all(1<=v<=len(current) for v in dest),(n,dest)
 rows.append(dict(origin='pre-refresh 3e241566^',old_native_LF=n,old_wording=s,
   destination_current_native_LF=dest,destination_wording=[current[v-1] for v in dest],status=status,note=note))

# Main1.1 is also an explicit old population. All original sentences remain at
# the same coordinates except the sourced84 repair and the two dated metadata fields.
baseline=(B/'main-baseline.md').read_text().splitlines()
assert len(baseline)==len(current)
mainrows=[]
for n,s in enumerate(baseline,1):
 if not s.strip():continue
 assert s==current[n-1] or n in [4,7,84,90,113,116,121,152,192,194,219,224,340],(n,s,current[n-1])
 mainrows.append(dict(origin='main62b7639a baseline',old_native_LF=n,old_wording=s,
   destination_current_native_LF=[n],status='Carried byte exact' if s==current[n-1] else 'DE-L22/DE-L24/DE-L25/DE-L26 sourced restoration/precision or version/date update'))
payload={'status':'WRITER semantic old-topics destination table; not independent review',
 'current_guide_sha256':sha(G),'old_sha256':sha(B/'pre-refresh-original.md'),
 'main_baseline_sha256':sha(B/'main-baseline.md'),'pre_refresh_rows':rows,'main_baseline_rows':mainrows,
 'unmapped_substantive_units':0}
(B/'old-topics.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'old_origins':len(rows),'main_origins':len(mainrows),'unmapped':0}))
