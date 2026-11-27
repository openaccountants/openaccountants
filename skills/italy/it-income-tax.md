---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed
  individuals (lavoratori autonomi, liberi professionisti) under regime
  ordinario. Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF",
  "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni",
  "detrazioni", "addizionale regionale", "addizionale comunale", "regime
  ordinario", "acconti IRPEF", "no tax area", "INPS Gestione Separata", "rivalsa
  INPS" or any Italian income tax question for a professional. It covers the
  2025 and 2026 periods: IRPEF bands, the art. 13 detrazione, deductions, the
  addizionali, Quadro RE, filing and penalties. The middle rate is 35% for 2025
  and 33% for 2026. Regime forfettario appears only as an entry gate and
  comparison. This Tier 2 draft supports source checking and reviewer questions;
  it does not authorise filing, payment or a tax position.
version: 2.5
jurisdiction: IT
tax_year: 2026
tax_year_notes: "Ordinary professional income for calendar 2025 and 2026; 35% middle band in 2025, 33% in 2026. Form references are Redditi PF 2026 for 2025 income only. PF 2027 was not read; do not infer its rows or final dates. D.Lgs. 117/2026 applies from 1 January 2027; no later-period computation is supplied."
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
type: computation
---

# Italy income tax for self-employed professionals v2.5

> **General reference only.** Prepare an estimate and a source-linked working paper for professional review. This Guide does not authorise filing or payment.

## Who this applies to

Italian-resident individuals carrying on an art or profession habitually, even if not exclusively, under **regime ordinario** (TUIR arts 2, 3 and 53). Income periods are calendar years (art. 7). Keep **2025 and 2026 separate**. Quadro RE references below mean **Redditi PF 2026, for 2025 income**. They are not a claim about the unread Redditi PF 2027 form.

Collect itemised invoices, receipt/payment dates, processor reports, asset schedules, CU withholding certificates, contribution statements, F24 receipts, prior return, regime/election evidence and fiscal domicile at 1 January of each year. Use EUR. Search existing records before asking for missing facts. Bank totals or a narration alone do not establish income, deductibility, IVA, residence, contribution status or a local rate. Park an unresolved line as Needs Input, at any amount; never invent a percentage or silently omit it from a completed result.

### Refusals and narrow holds

Stop the affected computation, retain its inputs, and say **"Check this point with one of our partner accountants."** These controls preserve the original refusal IDs:

| ID | Trigger and action |
|---|---|
| R-IT-1 | Bank totals without itemised documents: no Quadro RE figure. |
| R-IT-2 | Regime unknown or mixed: establish the regime and any changeover first. |
| R-IT-3 | Forfettario eligibility or exit uncertain: apply the gate below, then stop preparation under that regime. |
| R-IT-4 | Non-resident or disputed residence, including art. 2(2-bis): resident-only computation stops; no automatic ordinary-resident reliefs. |
| R-IT-5 | Vehicle deduction above the supported art. 164 limb: no higher percentage without its conditions. |
| R-IT-6 | Forfettario year: comparison only; this Guide does not prepare that return. The former `it-regime-forfettario` pointer is not a usable companion. |
| R-IT-7 | Employment, pension, rental, capital, partnership or other income, company/association or business income: the complete mixed return needs separate treatment. |
| R-IT-8 | CPB, impatriati, copyright/sports/volunteer income or other special RE rows: hold that treatment. |
| R-IT-9 | Foreign tax credit or treaty claim: hold the cross-border adjustment. |
| R-IT-10 | A later income period, or PF 2027 rows/final filing or payment timetable: hold that request, while retaining the proven 2026 ordinary income computation. |

The workflow-base employee and mixed-income fixtures are not supplied. Outputs are working papers labelled **estimated, not reviewed**, with confirmed facts and Needs Input shown separately.

## Rates, bands and thresholds

### IRPEF and the self-employment detrazione

RC below means total income **before art. 10 charges**, net of the main home and appurtenances. It is not taxable income. Apply bands to income **after** deductible charges. The art. 13(5) relief does not combine with art. 13(1)–(4). Truncate positive statutory ratios to the first four decimals; cap total detrazioni at gross tax (arts 13(6), (6-bis), 11(3)).

| Rule | Amount and conditions | Period | Official source |
|---|---|---|---|
| IRPEF slices | 23% to EUR 28,000; 35% above 28,000 to 50,000; 43% above 50,000. EUR 6,440 on first band, EUR 14,140 on first two | 2025 | [TUIR art. 11](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2025-12-31) |
| IRPEF slices | 23% to EUR 28,000; 33% above 28,000 to 50,000; 43% above 50,000. EUR 6,440 on first band, EUR 13,700 on first two | 2026 | [TUIR art. 11; enacted L. 199/2025 art. 1(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-11-27) |
| Art. 13(5)(a) | RC up to EUR 5,500: EUR 1,265 | 2025–2026 | [TUIR art. 13](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-11-27) |
| Art. 13(5)(b) | RC above EUR 5,500 to 28,000: EUR 500 + 765 × truncate4((28,000 − RC)/22,500) | 2025–2026 | [TUIR art. 13](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-11-27) |
| Art. 13(5)(b-bis) | RC above EUR 28,000 to 50,000: EUR 500 × truncate4((50,000 − RC)/22,000); nil above 50,000 | 2025–2026 | [TUIR art. 13](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-11-27) |
| Art. 13(5-ter) | Add EUR 50 where RC is above EUR 11,000 and at most 17,000, including art. 53 professional income | 2025–2026 | [TUIR art. 13(5), (5-ter)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-11-27) |

EUR 5,500 is the simple no-other-income/no-charge result EUR 1,265 ÷ 23%, not a separate exemption band. For RC EUR 6,000, paid contributions EUR 500, taxable income is EUR 5,500: gross tax EUR 1,265, relief EUR 1,247.94, net EUR 17.06. With contributions EUR 1,000, taxable is EUR 5,000 and net tax is nil. Excess detrazione is not refunded; withholding credits are separate.

### Personal charges and high-income limits

| Rule | Amount and operative conditions | Period | Official source |
|---|---|---|---|
| Art. 15 oneri rate | 19%, if not deducted in computing an income category; individual eligibility, limits and payment conditions still apply. The printed 22% does not override this operative provision | 2025–2026 | [D.Lgs. 446/1997 art. 49](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art49!vig=2026-11-27) |
| Aggregate expense cap | RC above EUR 75,000 to 100,000: EUR 14,000; above 100,000: EUR 8,000; multiply by qualifying-child coefficient | 2025–2026 | [TUIR art. 16-ter(1)–(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-11-27) |
| Family coefficient | 0.50/0.70/0.85/1 for no/one/two/more than two qualifying children in the household; 1 also for a qualifying disabled child. Art. 12(2) conditions must be established | 2025–2026 | [TUIR art. 16-ter(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-11-27) |
| Expense-cap exclusions | Medical costs and specified innovative start-up/SME investments; interest on loans/mortgages and listed insurance contracted by 31 December 2024; instalments of qualifying expenses incurred by that date. For later multi-year expenses count the annual expense instalment | 2025–2026 | [TUIR art. 16-ter(4), (5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-11-27) |
| Art. 15 phase-out | Full to RC EUR 120,000; above that multiply by max((240,000 − RC)/120,000, 0). Exempt from this phase-out: art. 15(1)(a), (b), (1-ter) interest and (1)(c) medical costs | 2025–2026 | [TUIR art. 15(3-bis)–(3-quater)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig=2026-11-27) |
| Additional cut | RC above EUR 200,000: EUR 440 off the aggregate detrazione for 19% oneri other than medical costs, political donations and catastrophe insurance; after the preceding caps/phase-out, floor zero for those credits | 2026 only | [TUIR art. 16-ter(5-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-11-27) |

For art. 15(1-ter) construction-mortgage interest the cap is EUR 2,582.28 (five million lire), rate 19%. The mortgage must be from 1998 onward, secured by a mortgage, for construction of the main home; the owner/right-holder must contract within six months before or eighteen months after work begins. Further ministerial conditions must be confirmed before using it. Example 5 assumes qualifying interest, not that a bank narration proves eligibility.

### Forfettario entry gate and comparison only

| Test | Condition | Period | Official source |
|---|---|---|---|
| Prior-year gate | Aggregate revenue/fees, annualised, at most EUR 85,000 and specified staff/collaborator spending at most EUR 20,000 gross | 2025–2026 | [L. 190/2014 art. 1(54), (55)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-11-27) |
| Employment exclusion | Prior-year employment/similar income above EUR 35,000, unless employment ended; the standing EUR 30,000 is temporarily raised | 2025–2026 | [L. 207/2024 art. 1(12), amended by L. 199/2025 art. 1(27)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-11-27) |
| Exit | Failed gate/exclusion: following year. Receipts above EUR 100,000: same-year exit, IVA from the crossing operation | 2025–2026 | [L. 190/2014 art. 1(71)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-11-27) |
| Comparison tax | 15% substitute tax on receipts × applicable coefficient less qualifying paid contributions; replaces IRPEF/addizionali/IRAP | 2025–2026 | [L. 190/2014 art. 1(64)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-11-27) |
| New activity | 5% in start year and next four only if no activity in preceding three years, no mere continuation (except compulsory practice), and any predecessor's prior-year receipts meet the statutory ceiling | 2025–2026 | [L. 190/2014 art. 1(65)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-11-27) |

Also test every exclusion in art. 1(57): special IVA/forfait regimes; non-residence (with the EU/EEA information-exchange/75%-Italian-income exception); predominantly buildings, building land or new-vehicle sales; partnership/association/family-business participation or control of linked SRL/association-in-participation activity; predominantly current/recent-employer or linked-party work (two preceding periods, compulsory-practice exception). An ordinary-regime election can bind for at least three years (comma 70). Passing the receipts test alone does not settle the regime. Forfettario receipts are not subject to advance withholding, with the required declaration (comma 67).

Only the existing 2025 professional comparison uses the 78% coefficient. Other coefficient categories (construction/real estate, intermediaries, street trade, food/retail/hospitality and other activities), ATECO 2025 mapping and actual forfettario preparation remain non-usable here. Check this point with one of our partner accountants.

## The base

### Income, contributions and withholding

Use cash receipts and expenses, subject to statutory exceptions, not invoice dates. A receipt in the year after the withholding agent paid it belongs to the year of that agent's withholding obligation (art. 54(1)). Exclude legal contributions imposed on the payer, analytically recharged job expenses and shared-premises recharges (art. 54(2)); associated excluded recharges are not deductible (art. 54-ter(1)). Costs paid directly by the client are not a benefit in kind (art. 54(3)).

The optional **4% Gestione Separata rivalsa is taxable compensi**, unlike a legal payer-borne cassa integrative contribution (L. 662/1996 art. 1(212); PF 2026 RE2). Do not assume it was charged. Paid compulsory personal contributions are art. 10(1)(e) oneri, not Quadro RE costs: RP21 → RP39 → RN3 for the 2025 form. Never split them 50/50 or deduct them twice. Establish cassa/GS status and actual payments; contribution rates/caps belong to `it-inps-contributions` or the fund statement, not an assumed percentage of receipts.

Resident professional compensation paid by an art. 23 withholding agent generally bears **20% on account at payment**, not the printed unamended 15%: read DPR 600/1973 art. 25 with D.L. 688/1982 art. 5, D.L. 69/1989 art. 33 and L. 449/1997 art. 21(11)(b). Reconcile CU to gross fees and RE26; withholdings reduce tax, not income. The later business-payment withholding is not the professional rate.

### Expense matrix

All figures require documented professional use. Exclude recoverable IVA; irrecoverable IVA needs its own established treatment. A merchant/bank brand never fixes a deduction.

| Cost | Deduction and conditions | Period | Official source |
|---|---|---|---|
| Ordinary running costs | Documented expenses incurred in the profession; no personal costs. Processor fees, software subscriptions, professional/legal fees, professional insurance, stationery and bank charges follow their actual nature | 2025–2026 | [TUIR art. 54(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54!vig=2026-11-27) |
| Movable asset | Immediate deduction permitted at unit cost at most EUR 516.40. Above: depreciation within ministerial coefficients, halved in first period; not an automatic full expense | 2025–2026 | [TUIR art. 54-quinquies(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-11-27) |
| Mixed-use movable goods | 50%, except vehicles governed by art. 164; depreciation/lease rules still apply | 2025–2026 | [TUIR art. 54-quinquies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-11-27) |
| Mixed-use premises | 50% of rent or cadastral income, provided no other exclusively professional property in the same comune; 50% of related services/ordinary maintenance. No floor-area percentage | 2025–2026 | [TUIR art. 54-quinquies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-11-27) |
| Extraordinary property works | Equal deductions in year incurred and next five; mixed-use property: 50% of costs on that schedule | 2025–2026 | [TUIR art. 54-quinquies(2), (3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-11-27) |
| Public electronic-communication terminal equipment | 80% of depreciation, rent/hire, use and maintenance costs within the provision; do not apply this to software merely because it is online | 2025–2026 | [TUIR art. 54-quinquies(4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-11-27) |
| Ordinary hotel/food | 75%, capped in total at 2% of compensi; outside representation/training categories | 2025–2026 | [TUIR art. 54-septies(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-11-27) |
| Representation | 1% of compensi; traceable payment from 18 June 2025. Identify nature before applying it; hotel/food element also subject to its 75% rule | 2025–2026 | [TUIR art. 54-septies(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-11-27); [PF 2026 RE16](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Training | Qualifying master/course/conference fees, travel and stay fully deductible within EUR 10,000 annually; payment-traceability conditions below remain applicable | 2025–2026 | [TUIR art. 54-septies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-11-27) |
| Accredited certification/orientation | Fully deductible within EUR 5,000 annually only for personalised services listed in the statute, tied to real appropriate employment opportunities and supplied by accredited bodies | 2025–2026 | [TUIR art. 54-septies(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-11-27) |
| Ordinary professional car/motorcycle/moped | 20%, one vehicle for an individual professional; purchase caps EUR 18,075.99/4,131.66/2,065.83; annual hire caps EUR 3,615.20/774.69/413.17, time-apportioned. Leasing uses the proportional purchase-cost restriction | 2025–2026 | [TUIR art. 164(1)(b)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-11-27); [PF 2026 RE7/RE9](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026) |
| Employee mixed-use vehicle | 70% only when assigned for most of the period; not 100% because an employee uses it. A professional's exclusive-use description alone does not satisfy the full impresa-instrumental limb | 2025–2026 | [TUIR art. 164(1)(a), (b-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-11-27) |
| Vehicle fuel | The applicable art. 164 share, only with qualifying credit/debit/prepaid-card payment | 2025–2026 | [TUIR art. 164(1-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-11-27) |

**Traceability:** the domestic costs covered are hotel/food and travel/transport **by taxi/NCC under L. 21/1992**, not a blanket card-only rule for every train or airline payment. Art. 54(2-bis) includes an analytically reimbursed covered cost in income when untraceably paid; art. 54-ter(5-bis) requires tracing when an otherwise excluded expense becomes deductible for non-reimbursement. Art. 54-septies(6-bis) requires it for covered deductible costs. Under converted D.L. 84/2025 art. 1(5), the reimbursement limbs apply from the start of 2025; other covered directly borne costs and representation from 18 June 2025. Hold a disputed transition/payment date or an unclear journey category rather than applying a guessed start date. Check this point with one of our partner accountants.

An unreimbursed analytically charged expense can become deductible on an art. 54-ter(2)–(4) insolvency/enforcement/prescription event, or under (5) when at most EUR 2,500 including related fee and still unpaid one year after invoicing. Establish the precise event; foreign equivalents require adequate information exchange. No automatic deduction merely because the client is late.

Non-payment insurance is fully deductible (art. 54-septies(4)). Staff expenses follow (5); no deduction for the compensation to spouse, minor/permanently incapacitated children (including foster/adopted) or ascendants listed in (6). Do not infer a payroll or family-relief result from this short rule.

### Computation and form bridge

For an ordinary professional with no other income, special relief, credit adjustment or historic loss:

```text
professional income = gross compensi (including GS rivalsa) − deductible professional costs
RC = professional income, before paid art. 10 contributions, net of main-home income
 taxable = max(RC − art. 10 charges, 0)
gross IRPEF = 23% first 28,000 + year's middle rate next 22,000 + 43% excess
net IRPEF = max(gross IRPEF − art. 13 relief − eligible other detrazioni, 0)
IRPEF balance/credit = net IRPEF − established credits − withholding − acconti/prior credits
```

PF 2026 (2025 income): RE2 col. 2 gross fees net of IVA; RE6 total receipts; RE20 expenses; RE21 col. 5 = RE6 − RE20; RE23/RE25 income carried to RN; RE26 withholding. Personal contributions go to RP21/RN3, not RE. RN4 is taxable income, RN5 gross tax, RN26 net tax, RN33 withholding, RN34 Differenza and RN38 acconti. The full RN4 formula includes RN1 columns 2 and 3; do not omit those adjustments in a case requiring them. RV1 = RN1 col. 5 − RN2 − RN3. These line numbers must not be transplanted to PF 2027.

Current professional losses reduce same-year total income (art. 8(1)); the ordinary business carry-forward limb in art. 8(3) is not a general professional-loss rule. PF 2026 RE24 addresses surviving 2006/2007 losses. Historic loss utilisation needs its own schedule. Foreign-currency receipts/costs use payment-day exchange rate or nearest preceding day, otherwise that month's rate (art. 9(2)). Return entries are whole euros; calculations below show cents before return rounding.

**Working paper:** keep tabs for source transactions, deductible-cost adjustments, RE reconciliation, personal contributions, RC/taxable/IRPEF, withholding/acconti, addizionali and unresolved facts. Keep F24 IRPEF/addizionali out of professional expenses; identify contributions and tax prepayments separately. Retain documents and receipts; this Guide sets no substitute retention period.

### Addizionali

Apply the actual region/comune's year-specific rate/bands/exemptions to taxable income; domicile is at 1 January. Both require net IRPEF to be due under their statutes; the PF 2026 instructions also exclude a residual amount not exceeding EUR 10.33. Regional addizionale is not deductible. The regional base is 1.23%, not a universal minimum payable rate. The municipal ordinary variation cap is 0.8 points, not proof that no special-law higher rate exists. Never substitute those figures for the client's official row.

The municipal acconto is 30% of the charge on prior-year taxable income at prior-year rate/exemption. PF 2026 RV17 is the 2026 acconto. For Lombardia/Milan, Lazio/Roma, Veneto and every other locality, obtain the applicable official row and concessions. The old Molise/Friuli/Veneto/Umbria and twelve-comune survey is not an authority for a client's rate; higher-rate legal bases and D.Lgs. 147/2026 first-use conditions remain held. Check this point with one of our partner accountants.

## Deadlines and filing

For **2025 income, filed in 2026**, Redditi PF online runs 15 April to **2 November 2026** (31 October is Saturday). Paper, only where permitted, runs 15 April–30 June. Use the Agenzia reserved services/Entratel/Fisconline or an authorised intermediary; keep the acceptance receipt. An ordinary professional obliged to annual IVA files online; this is not a 730 preparation Guide.

| Payment | Date or rule | Period | Official source |
|---|---|---|---|
| General saldo/first acconto | 30 June 2026, or 30 July with 0.40% | 2025 saldo/2026 acconto | [DPR 435/2001 art. 17](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig=2026-11-27) |
| Qualifying ISA activities, including listed exclusions/regimes and participating partners | 20 July 2026 without surcharge; following 30 days with 0.80%, 20 August 2026 after the statutory August deferral. Confirm approved ISA and receipts within its limit | 2026 only | [D.L. 89/2026 art. 6, historical text](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-05-22;89~art6!vig=2026-05-23); [L. 113/2026 art. 1(2), saved effects](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2026-06-26;113~art1!vig=2026-11-27) |
| Second/sole acconto | 30 November 2026 | 2026 acconto | [PF 2026 RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| Acconto base | 100% of RN34/RN61 col. 4 Differenza, after required recalculations. Below EUR 52 in the whole-euro form: none; a lower forecast can be paid, with underpayment risk | 2026 acconto | [PF 2026 RN62](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |
| Split | General 40%/60%; qualifying ISA population 50%/50%. If first amount does not exceed EUR 103, pay once in November. Do not round a boundary into a different test | 2026 acconto | [DPR 435/2001 art. 17(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig=2026-11-27); [D.L. 124/2019 art. 58](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-10-26;124~art58!vig=2026-11-27) |
| Payment floor | No payment/compensation where each return tax/addizionale is at most EUR 12 | PF 2026 | [PF 2026 payment instructions](https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026) |

Use F24 online, showing the correct tax year: 4001 saldo, 4033 first acconto, 4034 second/sole, 3801 regional, 3844 municipal saldo and 3843 municipal acconto (PF 2026 instructions). Reconcile actual receipts. The 1–20 August deferral follows D.L. 223/2006 art. 37(11-bis). Instalment plans need their applicable payment provisions, not an assumed flat monthly percentage. Check this point with one of our partner accountants.

A return within 90 days remains valid with late-filing sanctions; beyond 90 days it is omitted but remains a collection title (DPR 322/1998 art. 2(7)). PF 2027 rows and final calendar, non-resident post, 730 lateness/fallback and post-2026 recodified filing/payment procedures remain non-usable here under R-IT-10. The ordinary 2026 income computation above is retained.

## Penalties and interest

The following is the operative pre-2027 text for violations from **1 September 2024** (D.Lgs. 87/2024 art. 5), not the old 30%/15% payment regime. Earlier violations and the post-2026 recodification require separate treatment.

| Offence | Base sanction and conditions | Official source |
|---|---|---|
| Omitted return | 120% of tax, minimum EUR 250; no tax: EUR 250–1,000, potentially doubled for accounting-record obligations | [D.Lgs. 471/1997 art. 1(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-11-27) |
| Filed beyond 90 days | Within assessment limitation period and before formal knowledge of access/inspection/verification/assessment: three times art. 13(1), 75%; no-tax sanctions as above; no art. 13 ravvedimento reduction | [D.Lgs. 471/1997 art. 1(1-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-11-27); [D.Lgs. 472/1997 art. 13(2-ter)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-11-27) |
| Inaccurate return | 70% extra tax/credit used, minimum EUR 150. Fraud increases by half to double. Outside fraud, reduction by one-third only where extra tax/minor credit is below both 3% and EUR 30,000, or a qualifying timing error; no Treasury loss: EUR 250 | [D.Lgs. 471/1997 art. 1(2)–(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-11-27) |
| Voluntary integrative return | Within assessment period and before formal knowledge of access/inspection/verification/assessment: double art. 13(1), 50%; if no tax, EUR 150 minimum | [D.Lgs. 471/1997 art. 1(2-bis)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-11-27) |
| Late payment | 25%; halved for at most 90 days; for at most 15 days further multiply by days/15, before ravvedimento | [D.Lgs. 471/1997 art. 13(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-11-27) |
| Return within 90 days | Ravvedimento: one-tenth of omission minimum, EUR 25 on EUR 250, with separate unpaid-tax consequences | [D.Lgs. 472/1997 art. 13(1)(c)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-11-27) |

For payment ravvedimento, art. 13(1)(a)/(a-bis)/(b)/(b-bis) gives respectively 1/10 within 30 days, 1/9 within 90 days, 1/8 within the relevant return term (or year if no periodic return), then 1/7. Tax, reduced sanction and legal interest accruing daily must be regularised. For Agenzia-administered taxes an inspection alone is not the initial blanket bar: art. 13(1-ter) excludes that bar but preserves notification of assessment/liquidation and the specified automated-control communications. Legal interest is 2% annually from 1 January 2025 (DM 10 December 2024) and 1.60% from 1 January 2026 (DM 10 December 2025); split a period across the applicable years. Post-audit/draft-assessment reductions, aggregation and omitted-invoice IVA sanctions need their own verified treatment. Check this point with one of our partner accountants.

## Cross-border points

Residents are taxed on worldwide income under art. 3; the art. 2 majority-of-period test includes fractions of days, civil-law residence, Italian domicile (main personal/family relations) or presence, with a rebuttable registration presumption. Do not equate citizenship, one Italian bank account or a foreign client with residence.

Non-resident source/deductions/withholding exceptions (including art. 24(3-bis)), treaty credits, foreign withholding and remittance reporting are non-usable here: R-IT-4/R-IT-9. Crypto/NFT/capital gains, occasional work and its separate contribution gate, IRES/IRAP, rental income, employment/pension reliefs, cuneo fiscale and family detrazioni retain their separate-topic routing: `it-cross-border`, `italy-crypto-tax`, `it-irpef-employees`, `italy-payroll`, `it-irap` and `it-impatriati` as applicable. Check this point with one of our partner accountants. Cross-border IVA belongs to `italy-vat-return`.

## Two worked examples that recompute

All names are fixtures. Each example shows a decision. Figures are estimates.

### Example 1: Quadro RE limits and the 2 bases

Period 2026. Milan designer, resident, regime ordinario, Gestione Separata confirmed, no other income. Compensi received EUR 60,000 plus EUR 2,400 rivalsa. Hotel and food EUR 3,000, all paid by card. Training EUR 12,000, all course fees with no hotel or food. Other deductible costs EUR 6,000. Contributions paid EUR 8,000. Ritenute EUR 5,000. Acconti EUR 3,000.

The decision is whether rivalsa is income, whether the limits bite, and which income drives the detrazione. Hotel and food meet the 2% limit, not the 75% figure. RC is before contributions, whereas the bands use income after contributions. The prior version's method deducted contributions in Quadro RE, took 75% and full training, and is shown for comparison.

```oa-check
name: IT 2026 Quadro RE limits with detrazione on reddito complessivo
inputs:
  fees: 60000
  rivalsa: 2400
  hospitality: 3000
  training: 12000
  other_costs: 6000
  contributions: 8000
  ritenute: 5000
  acconti: 3000
steps:
  - compensi: fees + rivalsa
  - hospitality_deductible: min(hospitality * 0.75, compensi * 0.02)
  - training_deductible: min(training, 10000)
  - expenses: hospitality_deductible + training_deductible + other_costs
  - rc: compensi - expenses
  - taxable: max(rc - contributions, 0)
  - gross_tax: 0.23 * min(taxable, 28000) + 0.33 * max(min(taxable, 50000) - 28000, 0) + 0.43 * max(taxable - 50000, 0)
  - ratio: floor((50000 - rc) / 22000 * 10000) / 10000
  - detrazione: 500 * ratio
  - net_tax: max(gross_tax - detrazione, 0)
  - balance: net_tax - ritenute - acconti
  - legacy_income: compensi - hospitality * 0.75 - training - other_costs - contributions
  - legacy_gross: 0.23 * min(legacy_income, 28000) + 0.33 * max(min(legacy_income, 50000) - 28000, 0)
  - legacy_ratio: floor((50000 - legacy_income) / 22000 * 10000) / 10000
  - legacy_net: legacy_gross - 500 * legacy_ratio
  - understatement: net_tax - legacy_net
expected:
  hospitality_deductible: 1248
  training_deductible: 10000
  rc: 45152
  taxable: 37152
  gross_tax: 9460.16
  detrazione: 110.15
  net_tax: 9350.01
  balance: 1350.01
  legacy_net: 8109.3
  understatement: 1240.71
```

The balance due is EUR 1,350.01 of IRPEF before addizionali, which stay Needs Input until the Milan rows are confirmed. The prior method would understate net IRPEF by EUR 1,240.71.

### Example 2: regime comparison for the 2025 period

Period 2025. Fixture client in Veneto with fiscal domicile there at 1 January 2025, ATECO 74.10, compensi EUR 70,000, costs EUR 20,000, 2024 compensi EUR 70,000, no employment income, no exclusion in art. 1(57). Contributions EUR 9,000 are assumed equal in both cases for comparison only; actual contributions under each regime come from `it-inps-contributions`. Regional rate 1.23% is the original fixture input; actual Veneto concessions must be established before applying it to a real taxpayer. Comunale rate 0.8% is a confirmed fixture input, with income above any exemption. Both local percentages are hypothetical confirmed case inputs, not a statement of every taxpayer’s rates. The client asks which is cheaper.

The decision is the comparison, not a recommendation. At RC of exactly EUR 50,000, art. 13(5)(b-bis) gives a detrazione of 0. The forfettario line carries 2 cases. The 5% rate applies only if art. 1(65) is met; otherwise 15%. A forfettario year stops under R-IT-6, so this example supports the conversation only and does not prepare that year.

```oa-check
name: IT 2025 ordinary and forfettario comparison, no recommendation
inputs:
  compensi: 70000
  costs: 20000
  contributions: 9000
  regional_rate: 0.0123
  comunale_rate: 0.008
  coefficient: 0.78
steps:
  - rc: compensi - costs
  - taxable: max(rc - contributions, 0)
  - gross_tax: 0.23 * min(taxable, 28000) + 0.35 * max(min(taxable, 50000) - 28000, 0) + 0.43 * max(taxable - 50000, 0)
  - detrazione: 500 * max(50000 - rc, 0) / 22000
  - net_tax: max(gross_tax - detrazione, 0)
  - regional: taxable * regional_rate
  - comunale: taxable * comunale_rate
  - ordinary_total: net_tax + regional + comunale
  - forfettario_income: max(compensi * coefficient - contributions, 0)
  - substitute_15: forfettario_income * 0.15
  - substitute_5: forfettario_income * 0.05
  - difference_15: ordinary_total - substitute_15
expected:
  taxable: 41000
  gross_tax: 10990
  net_tax: 10990
  regional: 504.3
  comunale: 328
  ordinary_total: 11822.3
  forfettario_income: 45600
  substitute_15: 6840
  substitute_5: 2280
  difference_15: 4982.3
```

Ordinary is EUR 11,822.30 and forfettario is EUR 6,840 at 15%, or EUR 2,280 at 5% if art. 1(65) is met. Present both and refer the choice to a Commercialista. IVA and contribution differences are not included.

### Example 3: low income, the EUR 50 increase and the floor

Period 2026. Case A: RC EUR 15,000, contributions EUR 3,000. Case B: RC EUR 5,000, contributions EUR 1,200, ritenute EUR 1,000.

In Case A the operative statute applies to art. 53 income: detrazione EUR 991.94 and net IRPEF EUR 1,768.06. The former EUR 941.94/EUR 1,818.06 alternative is retained below only as rejected legacy arithmetic, not an available tax position. The law wins over a narrower form summary. In Case B net tax stops at zero; unused relief EUR 391 is not refunded, while the EUR 1,000 withholding remains a credit. No PF 2027 line mapping is inferred.

```oa-check
name: IT 2026 art. 13 detrazione band, increase and zero floor
inputs:
  rc_a: 15000
  contributions_a: 3000
  rc_b: 5000
  contributions_b: 1200
  ritenute_b: 1000
steps:
  - taxable_a: rc_a - contributions_a
  - gross_a: taxable_a * 0.23
  - ratio_a: floor((28000 - rc_a) / 22500 * 10000) / 10000
  - detrazione_a_statute: 500 + 765 * ratio_a + 50
  - rejected_legacy_detrazione_a: 500 + 765 * ratio_a
  - net_a_statute: max(gross_a - detrazione_a_statute, 0)
  - rejected_legacy_net_a: max(gross_a - rejected_legacy_detrazione_a, 0)
  - taxable_b: rc_b - contributions_b
  - gross_b: taxable_b * 0.23
  - net_b: max(gross_b - 1265, 0)
  - unused_b: max(1265 - gross_b, 0)
  - credit_b: ritenute_b - net_b
expected:
  gross_a: 2760
  detrazione_a_statute: 991.94
  rejected_legacy_detrazione_a: 941.94
  net_a_statute: 1768.06
  rejected_legacy_net_a: 1818.06
  gross_b: 874
  net_b: 0
  unused_b: 391
  credit_b: 1000
```

### Example 4: late payment by days late

Tax of EUR 1,000 unpaid at the due date, for a violation after 1 September 2024 within the pre-2027 law covered here. The decision is which limb applies. Interest and ravvedimento are left out and go to the reviewer.

```oa-check
name: IT late payment sanction at 10, 40 and 120 days
inputs:
  tax: 1000
  days_short: 10
steps:
  - sanction_10_days: tax * 0.125 * days_short / 15
  - sanction_40_days: tax * 0.125
  - sanction_120_days: tax * 0.25
expected:
  sanction_10_days: 83.33
  sanction_40_days: 125
  sanction_120_days: 250
```

### Example 5: the EUR 440 reduction and its floor

Period 2026. RC EUR 250,000, net of the main home, contributions EUR 10,000. Two children in the household who meet art. 12(2), so art. 16-ter limit EUR 8,000 x 0.85 = EUR 6,800. Case A: EUR 2,500 of art. 15(1-ter) interest on a 2025 mortgage to build the main home, which art. 15(3-quater) keeps whole, within the EUR 2,582.28 cap and the limit. The qualifying mortgage, ownership, construction, main-home and ministerial conditions are assumed established for this fixture; no additional personal charge is claimed. Case B: the same interest at EUR 1,000. Case C: EUR 3,000 of university fees under art. 15(1)(e), which art. 15(3-quater) does not protect. None includes medical costs.

The decision is what art. 15(3-bis) leaves and whether the reduction can pass the detrazione for those charges. RC is above EUR 240,000, so art. 15(3-bis)(b) leaves nil in Case C, at the operative 19% rate. Case B stops at 0. The text reduces the detrazione 'spettante in relazione ai seguenti oneri', and this file reads it as not cutting other tax.

```oa-check
name: IT 2026 art. 16-ter(5-bis) reduction with floor
inputs:
  rc: 250000
  contributions: 10000
  interest_a: 2500
  interest_b: 1000
  fees_c: 3000
steps:
  - taxable: rc - contributions
  - gross_tax: 6440 + 7260 + 0.43 * (taxable - 50000)
  - limit: 8000 * 0.85
  - detrazione_a: max(min(min(interest_a, 2582.28), limit) * 0.19 - 440, 0)
  - detrazione_b: max(min(min(interest_b, 2582.28), limit) * 0.19 - 440, 0)
  - ratio_c: max(240000 - rc, 0) / 120000
  - detrazione_c: max(min(fees_c, limit) * 0.19 * ratio_c - 440, 0)
  - net_a: gross_tax - detrazione_a
  - net_b: gross_tax - detrazione_b
  - net_c: gross_tax - detrazione_c
expected:
  gross_tax: 95400
  limit: 6800
  detrazione_a: 35
  detrazione_b: 0
  ratio_c: 0
  detrazione_c: 0
  net_a: 95365
  net_b: 95400
  net_c: 95400
```

### Historical 2026 case H1: Graphic designer in Milan, regime ordinario, 2026

Fees received in 2026, net of VAT: EUR 60,000, of which EUR 40,000 from business clients that withheld 20%. Deductible costs paid: EUR 14,000. Gestione separata contributions paid in 2026: EUR 9,000. No other income, no oneri giving a detrazione.

Net professional income is 60,000 less 14,000 = EUR 46,000, which is also total income. Taxable income is 46,000 less the 9,000 contributions = EUR 37,000. Gross tax: 23% of 28,000 = 6,440, plus 33% of 9,000 = 2,970, total EUR 9,410. The self-employed detrazione uses total income: (50,000 - 46,000) / 22,000 = 0.181818, cut to 0.1818, times 500 = EUR 90.90. Net IRPEF EUR 9,319.10. Withholdings were 20% of 40,000 = EUR 8,000, so EUR 1,319.10 is the estimated balance before the unverified final 2027 payment timetable, before the surcharges at the Lombardy and Milan rates and before acconti.

```oa-check
name: Self-employed designer, fees EUR 60,000, regime ordinario (2026 bands)
inputs:
  fees: 60000
  costs: 14000
  contributions: 9000
  fees_withheld: 40000
steps:
  - net_income: fees - costs
  - taxable: net_income - contributions
  - band_23: min(taxable, 28000) * 0.23
  - band_33: (min(taxable, 50000) - 28000) * 0.33
  - gross_tax: band_23 + band_33
  - ratio: floor((50000 - net_income) / 22000 * 10000) / 10000
  - detrazione: round(500 * ratio, 2)
  - net_irpef: gross_tax - detrazione
  - withholding: fees_withheld * 0.2
  - balance: net_irpef - withholding
expected:
  net_income: 46000
  taxable: 37000
  gross_tax: 9410.00
  ratio: 0.1818
  detrazione: 90.90
  net_irpef: 9319.10
  withholding: 8000.00
  balance: 1319.10
```

### Historical 2026 case H2: Consultant above EUR 75,000 with one child, the art. 16-ter cap (2026)

Net professional income EUR 95,000 (total income). Gestione separata contributions paid EUR 15,000. One qualifying child. Oneri at 19% paid in 2026: EUR 12,000, none medical, all from contracts made after 2024, each already within its own limit.

Taxable income is 95,000 less 15,000 = EUR 80,000. Gross tax: 13,700 on the first 50,000 plus 43% of 30,000 = 12,900, total EUR 26,600. Total income is above EUR 50,000, so there is no self-employed detrazione. Total income is above EUR 75,000 and not above 100,000, so the oneri count only up to 14,000 x 0.70 = EUR 9,800. Total income is not above EUR 120,000, so no phase-out, and not above EUR 200,000, so no EUR 440 cut. Detrazione: 19% of 9,800 = EUR 1,862. Net IRPEF EUR 24,738, before withholdings, acconti and the surcharges. Without the cap the detrazione would have been 19% of 12,000 = EUR 2,280.

```oa-check
name: Consultant, total income EUR 95,000, art. 16-ter cap, one child (2026)
inputs:
  net_income: 95000
  contributions: 15000
  oneri_19: 12000
  coefficient: 0.70
steps:
  - taxable: net_income - contributions
  - band_23: min(taxable, 28000) * 0.23
  - band_33: (min(taxable, 50000) - 28000) * 0.33
  - band_43: max(taxable - 50000, 0) * 0.43
  - gross_tax: band_23 + band_33 + band_43
  - autonomo: 500 * clamp((50000 - net_income) / 22000, 0, 1)
  - cap: 14000 * coefficient
  - allowed: min(oneri_19, cap)
  - phase: clamp((240000 - net_income) / 120000, 0, 1)
  - detrazione_19: round(allowed * 0.19 * phase, 2)
  - net_irpef: gross_tax - autonomo - detrazione_19
expected:
  taxable: 80000
  gross_tax: 26600.00
  autonomo: 0
  cap: 9800.00
  allowed: 9800.00
  phase: 1
  detrazione_19: 1862.00
  net_irpef: 24738.00
```


### Bank line fixtures

Period 2025 fixtures carried from the prior version. They classify one line and stop. Each assumes the client's facts are confirmed.

**1. Intesa Sanpaolo, Milan, graphic designer.** `03/01/2025;;BONIFICO DA STUDIO GAMBA SRL;;3.500,00`. SEPA credit from a client SRL. Valentina has no pension fund. Confirm the amount is ex-IVA. Cash basis: compensi EUR 3,500.

**2. UniCredit, Turin, IT consultant.** `10/01/2025 | VB DA ACCENTURE SRL | AVERE EUR 6,500.00`. Monthly fee from one client: EUR 6,500 x 10 months = EUR 65,000 for the year. Compensi EUR 6,500. Flag single-client concentration and confirm no forfettario election: R-IT-6 applies if one is active.

**3. FinecoBank, Rome, photographer.** `15/03/2025;NEXI POS VERSAMENTO;Entrata;7.000,00`. Nexi settles net of fees. Match the merchant report for the gross amount and fee. Compensi EUR 7,000, or the gross figure if higher, with the fee as an expense.

**4. N26 Italy, Florence, translator.** `2025-05-20,STRIPE,,,STRIPE PAYOUT,22000.00,,,`. Payout net of fees. The prior version used about EUR 22,660 gross and EUR 660 of fees as an illustration; take the true figures from the Stripe report. Compensi on that illustration EUR 22,660, fee EUR 660 deductible under regime ordinario.

**5. Hype Business, Naples, e-commerce.** `2025-07-15;SUMUP PAYOUT;ENTRATA;15.000,00`. SumUp settlement. An e-commerce seller may earn business income, in which case Quadro RE does not apply and R-IT-7 stops the file. Confirm lavoro autonomo or impresa before any Quadro RE entry.

**6. BancoBPM, Bergamo, architect in Inarcassa.** `20/04/2025 | BONIFICO DA STUDIO ARCHITETTURA XYZ | AVERE EUR 8,500.00`. Gestione Separata does not apply to an Inarcassa member on the client's stated facts. The cassa percentage is held, so collect the annual statement. Compensi EUR 8,500 subject to the integrative contribution exclusion in art. 54(2)(a).

### Historical fixture reconciliation

These retain the original years and numerical inputs; they are not evidence that a real taxpayer paid the stated charges. The ordinary computations below are conditional on the listed expenses being allowable and the contributions actually paid. A held result cannot be used for filing. No unsupported INPS rate, guessed processor fee, bank format or local rate is adopted.

The six brief bank fixtures also existed with **2026** dates: Intesa 3 January EUR 3,500; UniCredit 10 January EUR 6,500; Fineco 15 March EUR 7,000; N26 20 May EUR 22,000; Hype 15 July EUR 15,000; BancoBPM Bergamo 20 April EUR 8,500, Inarcassa status. Keep those 2026 variants separate from the 2025 strings above. No cassa rate follows from the architect's profession alone.

| Historical case | Original inputs retained | Reconciliation or narrow hold |
|---|---|---|
| 2025 early Test 1 | Fees 60,000; rivalsa 2,400; costs 15,000; paid GS 7,800; withholding 12,000; Lombardia 1.58%, Milan 0.8% claimed | RC 47,400; taxable 39,600; gross 10,500; art. 13 relief 59.05; net 10,440.95; IRPEF credit 1,559.05. Local rates are unproven fixture assumptions, not Lombardia law: arithmetic would be 625.68 + 316.80, total taxes 11,383.43, net credit 616.57, but that combined outcome is non-usable until the official local rows are established. Check this point with one of our partner accountants. |
| 2025 early Test 2 | Fees 5,000; rivalsa 200; expenses nil; paid GS 1,300 | RC 5,200; taxable 3,900; gross 897; art. 13 relief 1,265; net zero and no addizionali. |
| 2025 early Test 3 | Fees 150,000; rivalsa 6,000; costs 30,000; contributions 15,000; Lazio 3.33%, Roma 0.9% claimed | RC 126,000; taxable 111,000; IRPEF 40,370. Hypothetical flat local arithmetic 3,696.30 + 999 = total 45,065.30 is not a verified regional-band outcome. Check this point with one of our partner accountants. |
| 2025 early Test 4 | Car fuel/insurance/maintenance 12,000; fees 80,000 | For one qualifying ordinary vehicle, with required payment evidence: 20% = 2,400 deductible; 9,600 disallowed. No purchase-cost/depreciation assumption is hidden in this running-cost test. |
| 2025 early Test 5 / 2026 acconti | 2025 Differenza 8,000 after reliefs/withholding | If general 40/60 population: 3,200 and 4,800. If qualifying ISA population: 4,000 and 4,000. Use the applicable 2026 payment dates above; do not default to non-ISA. |
| 2025 early Test 6 | Fees 50,000; GS rivalsa 2,000, formerly omitted | Gross compensi 52,000 when received; no deduction for charging rivalsa. |
| 2025 early Test 7 | Tax 5,000 due 30 June, paid 15 September; 77 days | Base 12.5%, reduction 1/9 within 90 days: sanction 69.44; 2025 legal interest 2% × 5,000 × 77/365 = 21.10; extra 90.54. The old 15%, 1/8 and 2.5% were wrong for this 2025 case. This assumes timely full regularisation and no statutory bar. |
| 2025 original UniCredit IT consultant | Fees 90,000; costs 20,000; paid GS 23,607; single; shown credits 18,000 and 9,000; contribution debit 1,967.25; Adobe 79; bank fee 10; successive bank balances 75,000/84,000/82,032.75/81,953.75/81,943.75 | RC 70,000; taxable 46,393; no art. 13 relief; IRPEF 12,877.55 before credits/addizionali. No 50/50 contribution split. Old local 1.7%/0.5% were unsourced assumptions, not applicable rates. Check this point with one of our partner accountants. |
| 2025 original Intesa forfettario designer | Fees 55,000; ATECO 74.10; coefficient 78%; bank credits 8,500/5,000; Figma 45; train 89; SDD 2.50; bank balances 34,200/39,200/39,155/39,066/39,063.50 | Comparison base before contributions 42,900. The old inferred contribution reduction/rate and 7,314 charge were not established; no substitute-tax total or savings range is usable. R-IT-6. Check this point with one of our partner accountants. |
| 2025 original BancoBPM lawyer | Fees 120,000; costs 30,000; Cassa Forense paid 15,000; credits 25,000/10,000; contribution 3,750; rent 1,200; subscription 350; balances 98,000/108,000/104,250/103,050/102,700 | RC 90,000; contributions outside RE; taxable 75,000; IRPEF 24,890 before other reliefs/credits/addizionali. A legal payer-borne integrative contribution is not taxable GS rivalsa; confirm its actual invoice nature. |
| 2025 original MPS home office | Fees 38,000; 70m² home/10m² study; rent 900 monthly/10,800 annual; utilities 180/2,160; direct costs 4,000; internet 35; credits 5,000/3,200; balances 18,500/21,700/21,520/20,620/20,585; old claimed GS half 4,980 | If genuinely mixed-use with no other exclusive property in the comune: rent/services deduction 6,480, not 14.3%/1,854. RC before any unlisted adjustment is 27,520 if the 4,000 does not overlap those costs. No actual full-year paid contribution figure or safe completed tax result is established. Check this point with one of our partner accountants. |
| 2025 original BPER start-up developer | First year; fees 42,000; claimed 78%/5%; credits 12,000/6,500; GitHub 180; AWS 245; bank 8; balances 32,000/38,500/38,320/38,075/38,067; old approximate contributions 5,600 | Conditional coefficient arithmetic 32,760; the old assumed 35% GS reduction and eligibility were not established. No usable 1,358 final tax. R-IT-6. Check this point with one of our partner accountants. |
| 2025 original Fineco architect | Fees ex-IVA 150,000; costs 45,000; acconti 18,000; credits 36,600/24,400; F24 9,000; Inarcassa 3,500; rent 2,500; balances 142,000/166,400/157,400/153,900/151,400; claimed annual contributions 21,000 | RC 105,000. If 21,000 is proven paid, taxable 84,000, IRPEF 28,760, balance 10,760. The old decomposition of 36,600 as 30,000 plus 6,000 IVA was arithmetically inconsistent; do not infer IVA from the bank total. Confirm invoices and annual contributions before using the balance. Check this point with one of our partner accountants. |
| 2025 later Intesa designer | Credits 3,500/2,200/1,850 net Stripe/4,100; bank 4.50; monthly Fastweb 35.90 and Adobe 59.99; F24 1,200 + 1,800; paid GS 1,800; accountant 500; train 89 | Fixed known receipts 9,800 plus actual Stripe gross; other documented costs 1,658.02 (4.50 + 344.64 + 719.88 + 500 + 89), contributions deducted once outside RE. Reject guessed 2.9% + 0.30 processor pricing and automatic monthly annualisation without records. Original illustrative gross Stripe 1,905.81/total 11,705.81 is preserved only as unproven input, no completed tax. Check this point with one of our partner accountants. |
| 2025 later UniCredit consultant | Fees 6,500 × 10 = 65,000; Microsoft 12.50 monthly = 150; bank 3 monthly = 36; training 250; GS acconti actually paid 8,500 | With all stated annual costs confirmed, costs 436, RC 64,564, taxable 56,064, no art. 13 relief; IRPEF 16,747.52. Deduct paid 8,500, not an inferred 26.07% charge. Software is not an 80% terminal cost. |
| 2025 later Fineco photographer | Receipts 28,000 + 7,000 net processor; rent 600 monthly/7,200; utilities 120 monthly/1,440; equipment 3,500; insurance 350; old 25%/875 depreciation and 26.07%/9,124.50 GS | Gross processor receipts, ministerial coefficient/first-period reduction and actual paid contributions are unresolved. Known receipts before gross-up less non-asset costs = 26,010; no completed tax. Check this point with one of our partner accountants. |
| 2025 later N26 translator | Stripe net 22,000/illustrative gross 22,660 and fee 660; PayPal net 5,500/illustrative gross 5,664 and fee 164; total illustrative gross 28,324; Fastweb deduction 344; Adobe 720; claimed GS 7,378 | Processor arithmetic reconciles 28,324 − 824 = 27,500 net. If reports confirm the illustrations and 7,378 is actual paid contributions, RC = 26,436, taxable 19,058, gross 4,383.34; relief 553.17 and net 3,830.17 before credits/addizionali. Without that evidence no completed result. Check this point with one of our partner accountants. |
| 2025 later Hype e-commerce | SumUp 15,000; refunds 800; hosting/platform 500; claimed INPS 3,701.94 | 15,000 − 800 = 14,200 receipts before any processor correction; less 500 = 13,700 before contributions. Business-vs-professional/occasional status is unresolved: no Quadro RE/IRPEF result. Check this point with one of our partner accountants. |
| 2025 later BancoBPM architect | Gross fees 85,000; Inarcassa status; earlier illustrative subjective 14.5% + integrative 4%; later 2026 bank receipt 8,500 | Exactly 85,000 is not above the gate; an ordinary election or other facts can still require ordinario. Gross-band tax before any expense/contribution is 29,190 at 2025 rates, not a final liability. No assumed cassa percentage or deductible amount. Check this point with one of our partner accountants. |

Bank-format rules are withdrawn as untested defaults. Retain each original transaction/date/amount as a fixture; detect delimiter, decimal separator, date format, account transfers and completed/reversed status from the actual export. No test here proves a bank's live CSV layout. The contribution percentages and fee estimates above are quoted historical inputs requiring evidence, not current rates.

## Ask the client first

Search the records first. Resolve regime and residence, the period and other income, receipts gross of processor fees and withholding, IVA, every cost's nature/use/payment, contribution status and actual paid amounts, fiscal domicile and official local rows, prior return/acconti/CU, and qualifying family/personal-charge facts. Use no default local or contribution rate.

Before delivery, reconcile documents to RE, contributions to RP/RN, RC to taxable income, the correct year's bands, statutory ratios and credit floor, withholding/acconti, local rates and all holds. An internal transfer, loan principal, tax refund or ambiguous reimbursement must be identified from its source rather than classified from a bank label. Keep an acceptance/F24 receipt only after an authorised filing/payment actually occurred.

## Sources

Read 27 November 2026. Statutes were read in the native Normattiva browser; PDF passages were read directly in memory from Agenzia delle Entrate. The 2025 historical art. 11 text was read separately. Current art. 13 and the expense provisions explicitly show their operative windows through 31 December 2026; D.Lgs. 192/2024 commencement and D.L. 84/2025 transition provisions were read with them. Form references are for 2025 income only.

| Source | Official URL | Read on and scope |
|---|---|---|
| TUIR, DPR 917/1986 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-11-27 | 2026-11-27; arts 2, 3(1), 7, 8(1)/(3), 9(2), 10(1)(e), 11 (also 2025-12-31), 13, 15(1-ter)/(3-bis)–(3-quater), 16-ter, 53, 54, 54-ter, 54-quinquies, 54-septies and 164, at the matching article URL patterns linked above |
| L. 199/2025 art. 1(3), (4), (27) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-11-27 | 2026-11-27; enacted 2026 middle-rate change, EUR 440 cut and temporary employment gate extension |
| L. 207/2024 art. 1(12) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-11-27 | 2026-11-27; operative 2025/2026 employment threshold |
| L. 190/2014 art. 1(54)–(57), (64), (65), (67), (70), (71) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-11-27 | 2026-11-27; entry/exit, exclusions, election and comparison only |
| D.Lgs. 446/1997 arts 49, 50 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art49!vig=2026-11-27 | 2026-11-27; operative 19% oneri rule; regional base, tax base, due-tax condition and domicile in art. 50 at matching URL |
| D.Lgs. 360/1998 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-11-27 | 2026-11-27; ordinary variation cap, exemptions, due-tax test, domicile and acconto |
| L. 662/1996 art. 1(212) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1996-12-23;662~art1!vig=2026-11-27 | 2026-11-27; right to 4% rivalsa, not the obsolete payment dates in the same paragraph |
| DPR 600/1973 art. 25 and operative rate chain | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art25!vig=2026-11-27 | 2026-11-27; resident professional withholding, D.L. 688/1982 art. 5, D.L. 69/1989 art. 33 and L. 449/1997 art. 21(11)(b) each read directly |
| D.L. 84/2025 art. 1 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2025-06-17;84~art1!vig=2026-11-27 | 2026-11-27; converted tracing rules and commencement, with L. 108/2025 conversion annotation |
| DPR 322/1998 art. 2 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-11-27 | 2026-11-27; filing window, Saturday extension and late-return validity |
| DPR 435/2001 art. 17 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig=2026-11-27 | 2026-11-27; saldo, interest option and acconto boundaries |
| D.L. 124/2019 art. 58 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2019-10-26;124~art58!vig=2026-11-27 | 2026-11-27; ISA 50/50 split and referenced population |
| D.L. 89/2026 art. 6; L. 113/2026 art. 1(2) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-05-22;89~art6!vig=2026-05-23 | 2026-11-27; 2026 deferral/population, and later repeal/saved effects at the L. 113 URL linked above |
| D.Lgs. 471/1997 arts 1, 13; D.Lgs. 472/1997 art. 13; D.Lgs. 87/2024 art. 5 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-11-27 | 2026-11-27; each operative provision read at matching act/article URL; pre-2027 windows and 1 September 2024 transition |
| D.Lgs. 117/2026, attached TU arts 376, 377 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117:1~art377!vig=2026-11-27 | 2026-11-27; 1 January 2027 commencement and repeal of DPR 917 arts 1–191, not a later-year article mapping |
| Agenzia, Redditi PF 2026 Fascicolo 1 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf1_istruzioni_2026_agg-28-05-2026 | 2026-11-27; RP21/RP39, RN3/RN4/RN5/RN34/RN62, RV1/due-tax conditions, F24 codes, payment floor and rounding; only the cited portions |
| Agenzia, Redditi PF 2026 Fascicolo 3 | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf3_istruzioni_2026_agg-13-05-2026 | 2026-11-27; RE2/RE6/RE7/RE9/RE10/RE12/RE14–RE17/RE19–RE26, specific compensation/expense/row passages, not every special regime in the fascicle |

| MEF, legal interest for 2025 and 2026 | https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=25A06705&atto.dataPubblicazioneGazzetta=2025-12-13&tipoSerie=serie_generale&tipoVigenza=originario | 2026-11-27; full DM 10 December 2025 and DM 10 December 2024 (GU 16 December 2024, code 24A06721), actual 1.60%/2% operative sentences |
| Agenzia, 2026 filing calendar | https://www.agenziaentrate.gov.it/portale/modello-redditi-persone-fisiche-2026/quando-e-come-presentare-il-modello-redditi-persone-fisiche | 2026-11-27; filing year explicitly 2025 income, dates, digital route and PF Web/RedditiOnLine PF |
| L. 190/2014 Annex 4 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~all4!vig=2026-11-27 | 2026-11-27; selected Annex 4 in native viewer, whole coefficient table; professional ATECO 2007 group 78% used only in the existing comparison |
| D.L. 223/2006 art. 37(11-bis) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=2026-11-27 | 2026-11-27; reused unchanged applicable exact quote from private italy-vat-return proof ITV11; scope is covered 1–20 August obligations |

**Resolved source conflicts.** Law controls: art. 13(5-ter) includes art. 53 income; art. 54-quinquies prints EUR 516.40 rather than the form's EUR 516.46; qualifying training travel/stay follows art. 54-septies(3), despite RE17's narrower hotel/food instruction; D.Lgs. 446/1997 art. 49 fixes 19% despite TUIR art. 15(1)'s printed 22%; the directly read withholding amendment chain fixes 20%. A conflicting form implementation is a filing review point, not a second tax position.

**Later law.** D.Lgs. 117/2026 arts 376–377 were actually read: it applies from 1 January 2027 and repeals the old articles from that date. This does not transplant new numbering into the 2025/2026 computation. No proposed 2027 budget figure is used as enacted law.

Not yet confirmed: no usable outcome is supplied here for PF 2027 form rows/final timetable or later tax periods; actual local rates/concessions and special-law higher-rate bases; disputed 2025 tracing transition cases; ministerial asset coefficients, property leasing/depreciation and disposal/intangible special cases; special employee/family/mixed/non-resident/foreign-credit regimes; actual cassa/INPS parameters; forfettario return preparation and coefficients other than the conditional historical comparison; specific mortgage ministerial eligibility; special penalties and instalment plans and old medical/cash-limit/record-retention edge cases. For each affected point: **Check this point with one of our partner accountants.** These are non-usable holds, not permission to substitute a default. The ordinary professional income computation and its supported cases remain usable as estimates.
