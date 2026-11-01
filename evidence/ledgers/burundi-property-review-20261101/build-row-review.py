#!/usr/bin/env python3
"""Record independently read clause verdicts; this does not infer legal correctness mechanically."""
from pathlib import Path
import json,subprocess,hashlib
R=Path(__file__).resolve().parents[3];E=Path(__file__).resolve().parent
HEAD='f2ae4ea5b9463c5e959b2e3e44147e49facafbed'
ledger=json.loads(subprocess.check_output(['git','show',HEAD+':evidence/ledgers/burundi-property-20261101/bi-property-transactions.json'],cwd=R))
notes={
1:'Final art.252 read with arts.249–251 and signature; 1 January 2026 commencement confirmed visually, physical249/printed246.',
2:'Final art.277 read with arts.275–276 and signature; 01 July 2026 commencement confirmed visually at physical267.',
3:'Art.2 expressly makes the annex integral and identifies three duty types; this is not a claim that historic tariffs are the final 2026 bill.',
4:'Full art.3(4) includes joint acquirers, buildings/parts, inter vivos, death and enforceable judgment; ledger summary is accurate.',
5:'January full art.138(b) distinguishes VAT-exclusive rate base from qualification by the higher market/counter-expertise value. Case2 expressly assumes the taxable base equals that evidenced amount.',
6:'January text says égale ou supérieure; equality at BIF500m qualifies. No exclusive-threshold error.',
7:'July full art.146(b), including its preceding vehicle limb and following property limb, confirms5% VAT-exclusive base for built/unbuilt property/fractions.',
8:'July text says égale ou supérieure at BIF500m. Both alternative valuations and higher-value selector retained.',
9:'January138(c) first says à partir du troisième then specifies10% if le troisième meets threshold. No5%+10% stacking; later-acquisition interpretation expressly held.',
10:'Final purchaser-liability sentence follows the complete property clauses, not an annual wealth schedule. No payer reversal.',
11:'July146(c) spans physical44–45; continuation read through10% and purchaser sentence. Same bounded third-property treatment as January.',
12:'July final sentence makes acquirer liable. No residence concession appears in these clauses; none invented.',
13:'January140 expressly replaces annexIV, fixes0.5% total claim/credit, and includes BIF50m cap. Full clause visually checked.',
14:'July148 fully replaces annexIV at0.5% total claim/credit and ends without cap; following149 begins separately. Importing January cap would contradict this replacement.',
15:'January142 A/B/C/D/E rates150000/100000/50000/25000/12000 BIF per are visually confirmed; joint order required for category composition/location/application.',
16:'January142 maximum3000000 BIF per title confirmed; it does not cap all conveyancing taxes.',
17:'July150 continues from physical45 onto46; all five per-are rates and joint-order clause read. No address-to-category inference made.',
18:'July150 maximum3000000 BIF title value/fee read in context after rates and before implementing order.',
19:'January139 uses un pour mille and visible1‰; approved estimate, urban house, serviced/unserviced land and prior authorisation conditions retained. Separate missing permit-insurance prerequisite R2.',
20:'July147 uses un pour mille and visible1‰ despite OCR1%; full clause and fines read. Separate missing permit-insurance prerequisite R2.',
21:'Art.4 exchange uses agreed value of the prestation giving higher duty if monetised. Rule is valuation, not a new2026tariff.',
22:'Art.5 three triggers, certified/signed foot-of-deed declaration and registrar/two signing witnesses for non-writer all confirmed.',
23:'Art.6 general market-value floor and art.7 BIF contract currency match; special arts.8–10 rules kept next to them.',
24:'Arts.19–20 registrar substitution/expertise and competent local court ordered expertise on parties request confirmed; no final value appeal result invented.',
25:'Art.8 expressly75% full-ownership-market-value floor for priced usufruct including limited time; undetermined price uses full market value.',
26:'Art.9 expressly distinguishes usufruct reserved by transferor versus not reserved; literal reference to art.6 retained rather than inventing actuarial formula.',
27:'Art.10 exemption is proportional-only, fixed duties remain, and prior full-value payment must be by bare owner or predecessor from whom rights derive.',
28:'Art.11 cumulative dues for entire duration confirmed; no sale tariff assigned.',
29:'Arts.12–13 distinguish remaining dues on transfer of emphyteusis from full-market-value underlying property; both read fully.',
30:'Art.14 State/administrative establishments receive three-duty exemption only inward; communes proportional-only and inward. Principal-text proposition passes, but current gift-to-State/subdivision exemption overlay missing from Guide: R4 (January207/July226).',
31:'Art.15 legal-personality religious/scientific/philanthropic inward gratuitous transfer and same-nature outward institution conditions read; proportional-only. Do not extend this limit to qualifying gifts to State/subdivisions under budget overlay R4.',
32:'January103 pre-emption for understated built/unbuilt disposal and104 ministerial tariff update read; unavailable order correctly held, historic annex not made a current quote.',
33:'July108–109 same pre-emption and joint minister tariff update confirmed. No inference that search absence repeals a tariff.',
34:'January94 undefined-use supply/coefficient and226–227 gifts/mixed-use/implementing order read. Routing is bounded; no unverified full VAT allocation asserted. Sources scope needs R3.',
35:'July95 adds natural-person undefined-use industrial/commercial location gate;246 related-person gift exception and repeated-gift text and247mixed-use implementing order read. Guide routes computation, does not claim universal family exemption.',
36:'Art.23 initial extract obligation and60calendar-day validity confirmed; full continuation contains separate weekly notary duty missing from Guide, R1.',
37:'Art.25 applies where changes affect consistance since title; survey/sketch/title updating and underlying registered real-right cases retained.',
38:'January141 full authentic-form/deposit requirement and ministerial format order read across41–42; Guide avoids using it as proved operational form.',
39:'January141 fees/taxes must be mentioned and exigible no later than30days after authentic signature; distinct from art24communication60days.',
40:'July149 full authentic-form/deposit/format-order clause read. Urban lease wording retained; no outside-city exemption invented.',
41:'July149 repeats no-later-than30days after authentic signature fee/tax schedule; no merger with60-day registration clock.',
42:'Art.24 titled-property/real-right mutation communication to territorially competent registrar within60days following signature; no invented working-day unit.',
43:'Art.32 communal-certificate sale requires buyer conversion within60jours ouvrables from signature; distinct from art24.',
44:'January217 explicitly requires built-property title-transfer dossier to contain fire-insurance certificate. Art215 separately relevant to building permit, R2.',
45:'July237 repeats built-property transfer fire-insurance dossier requirement; neighbouring235 independently conditions building permit, R2.',
46:'Art.26 request within8days following constitutive deed plus updated expertise value at deed date under banking law; registrar register/sign/seal retained.',
47:'Art.26 final sentence forbids mandate-to-mortgage annotations and partial inscriptions; no unsupported secured-credit fraction chosen.',
48:'Art.30 communal land services condition, debtor/grantor/possible surety and alternative competent issuers retained; certificate is not presented as general tax clearance for every sale.',
49:'Art.33 certificate to both creditor/debtor and references, act numbers, inscription date, covered claim, validity and renewal confirmed.',
50:'January143 five months from1January2026, holder obligation and directorate form posted on justice site read. No implied specific last-day convention or January50%fine.',
51:'July150owner obligation and151holder application before31March2027/form read; no express earlier waiver in text, none asserted.',
52:'Art.18 entry after duties payment; challenge cannot attenuate/defer payment, restitution reserved. No claim to actual payment channel.',
53:'January139 requires both authorisation reference and payment proof displayed; fine wording separately identifies non-display of reference.',
54:'July147 same two-part display duty confirmed; no automatic combined fine inference.',
55:'Art.24 late communication1%duties/week, increases to5%if attributable to transferor; buyer damages reserved. Does not include distinct notary list breach, R1.',
56:'Art.26 late mortgage request1%duties/month borne by creditor; no monthly charge applied to transfer notification.',
57:'Arts.16–17 shortfall at least one fifth of market value triggers evaded-duty equal fine; jointly/indivisibly on transferor and acquirer if alienation contract, other fiscal sanctions reserved.',
58:'Art.27 fine equals evaded proportional duties for partial inscription/concealed total mortgage debt; assisting public/notarial officer also caught for debt/transaction-price concealment.',
59:'July151 expressly50%secured-title amount for holder missing first-paragraph deadline; no corresponding January fine inserted.',
60:'January139500000BIF reference non-display and1000000BIF unauthorised start plus1‰expert estimate/expert cost confirmed visually; separate offences not automatically added.',
61:'July147 same fine amounts, estimate basis and taxpayer expert cost confirmed visually; future implementing order held.',
62:'Art.21 two years from registration for evaded-duty/fine recovery and two years from action arising for restitution; later procedure/fraud interaction expressly held.',
63:'61*50000=3050000; min with3000000=3000000; separate eventual deadline fine0.5*3000000=1500000. Category and area assumed evidenced, no timely2026fine.',
64:'Second499m is below clause threshold; second500m*0.05=25m; third500m*0.10=50m; difference25m. Count and taxable base expressly assumed proved.',
65:'12bn*0.005=60m; Januarymin(60m,50m)=50m; July60m; difference10m. Full replacements read and actual chargeable period expressly assumed.',
66:'80m*0.001=80000; separate unauthorised estimate same amount gives80000+1000000=1080000 before expert costs. No automatic display fine.'}
rows=[]
for x in ledger:
 i=int(x['id'][1:]);rows.append(dict(id=x['id'],verdict='PASS: proposition supported within stated scope',article=x['article'],source_sha256=x['source_sha256'],pdf_locator=x['pdf_locator'],official_url=x['official_url'],reviewer_note=notes[i]))
assert len(rows)==66
(E/'row-review.json').write_text(json.dumps(dict(frozen_head=HEAD,read_date='2026-11-01',row_count=66,rows=rows),ensure_ascii=False,indent=2)+'\n')
lines=['# Every-row source review','',f'Frozen head `{HEAD}`. All66original propositions pass under stated holds; separate completeness findings R1–R4 prevent acceptance until repaired. These are source-fidelity verdicts only.','', '| Row | Article / physical PDF locator | Verdict and independent reading |','|---|---|---|']
for x in rows:lines.append(f"| {x['id']} | {x['article']}; {x['pdf_locator']} | {x['verdict']}. {x['reviewer_note']} |")
(E/'row-review.md').write_text('\n'.join(lines)+'\n')
