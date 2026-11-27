---
name: ro-vat-return
description: "Romanian VAT for 2026: normal and small-enterprise registration, 21% and 11% rates, qualifying 9% housing transition, deductions, monthly or quarterly D300, D394, D390, reverse charge, refunds and late payment. Includes a transaction matrix, two recomputing examples and explicit holds for special regimes and historical cases. Trigger: Romania VAT, TVA, D300, D394, D390, decont de TVA. Related: romania-einvoice, ro-corporate-income-tax, ro-cross-border."
version: 1.5
type: filing-howto
jurisdiction: RO
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# Romania VAT (TVA): rates, registration, D300, D394 and RO e-TVA (2026)

This skill covers Romanian VAT for the 2026 calendar year: who is in, the rates, registration, the D300 return and its rows, the information returns, the pre-filled RO e-TVA return, reverse charge, EU trade, refunds and penalties.

Use the current D300 assistance program from [ANAF](https://static.anaf.ro/static/10/Anaf/Declaratii_R/300.html), for periods beginning in 2026. This Guide uses Title VII of Legea 227/2015 (Fiscal Code), the Fiscal Procedure Code and the orders in Sources. References below to the Code mean the [ANAF consolidated Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm). Its methodological norms can retain obsolete wording: the operative statute controls.

Related Guides: [romania-einvoice](romania-einvoice.md), [ro-corporate-income-tax](ro-corporate-income-tax.md), [ro-cross-border](ro-cross-border.md), [ro-tax-overview](ro-tax-overview.md).

## Who this applies to

A taxable person carries on an economic activity independently, regardless of its purpose or result (art. 269). First obtain the VAT registration, establishment, reporting period, transaction date, supply description, counterparty VAT number, invoices, previous balance and business-use evidence.

| Group | Treatment |
|---|---|
| Normal registration under art. 316 | Follow the D300 method below; deductions depend on use and documentation. Income-tax micro-enterprise status does not determine this VAT treatment. |
| Romanian-established small enterprise | Art. 310 exemption up to 395,000 lei turnover; no input deduction and no VAT shown on invoices. Turnover under art. 310(2) covers Romanian-place taxable/would-be-taxable supplies, exemptions with deduction and specified non-incidental financial/property exemptions; fixed tangible assets and intangible asset transfers are excluded. Exempt-only activity under art. 310(3) does not itself force registration. New means-of-transport EU supplies are excluded from the exemption. |
| EU-only registration under art. 317; non-established supplier | These are separate registration/liability tests, not permission to use the normal D300 method. See the specific holds in Sources. |

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate (art. 291(1), as rewritten by Legea 141/2025 art. II pt. 42, in force 1 August 2025) | 21% | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Reduced rate (art. 291(2)) | 11% | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Transitional rate for one home bought by an individual (up to 120 sq m useful area excluding household annexes and 600,000 lei including land but excluding VAT, no other reduced-rate home bought since 1 January 2023) with an advance contract signed by 1 August 2025 and a dwelling habitable as such at delivery by 31 July 2026, with the notary checking the acquisition register; for contracts signed 3 to 31 July 2025, a 20% advance of the home value excluding VAT paid in full by 31 July 2025 (Legea 141/2025 art. III(1) and (2)) | 9% | to 31 July 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| In force date of the rate change (Legea 141/2025 art. VII(1)) | 1 August 2025 | 2025 | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Small-enterprise exemption threshold, annual turnover (art. 310(1)) | 395,000 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Quarterly period turnover ceiling; prior-year qualifying turnover and no prior-year intra-EU goods acquisitions, art. 322(2); BNR exchange rate at prior 31 December, norms 103(2) | EUR 100,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Domestic reverse charge on mobile phones, chips, consoles, tablets, laptops: minimum per invoice, excluding VAT (art. 331(7)) | 22,500 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Input VAT on road vehicles not used only for business (art. 298(1)) | 50% deductible | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Late payment interest (Procedure Code art. 174(5)) | 0.02% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Late payment penalty (Procedure Code art. 176(2)) | 0.01% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Non-declaration penalty on tax set by ANAF (Procedure Code art. 181(1)) | 0.08% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |

**What the 11% rate covers** (art. 291(2), letters a to n):
- medicines for human use;
- food, including drinks, for human and animal consumption, and live domestic animals and birds, except alcoholic drinks, non-alcoholic drinks under NC code 2202, foods with added sugar whose total sugar is at least 10 g per 100 g (infant milk powder excepted) and food supplements;
- water supply and sewerage, and water for irrigation in agriculture;
- fertilisers, pesticides, seeds and agricultural services of the kinds listed by joint order (chemical fertilisers and pesticides until 31 December 2031, art. 291(3^3));
- school textbooks, books, newspapers and magazines, printed or electronic, except mainly video, music or advertising content;
- entry to castles, museums, memorial houses, monuments, zoos and botanical gardens;
- firewood and agglomerated wood pellets/briquettes under the NC codes in art. 291(2)(i)-(j); non-agglomerated sawdust/waste requires heating-fuel end use and the beneficiary’s declaration (until 31 December 2029, art. 291(3^4));
- heat in the cold season (1 November to 31 March) to households, legally defined public/private hospitals and schools, qualifying NGOs/religious bodies and accredited public/private providers of the listed social services;
- buildings delivered as social policy: old people's and pensioners' homes, children's homes and rehabilitation centres for disabled minors;
- hotel and similar accommodation, including camping pitches;
- restaurant and catering services, except alcoholic drinks and NC 2202 drinks.

This is a category checklist: apply the exact product codes and recipient/use conditions in art. 291(2), rather than treating every medical device, school supply or soft drink as reduced-rated. Anything outside the statutory reduced list, and not exempt, is at 21%. Since 1 August 2025 there is no 19%, 5% or 9% rate in art. 291. The 9% rate survives only in Legea 141/2025 art. III: for the transitional homes above, and, until 1 August 2026, for buildings sold to town halls for subsidised rent under advance contracts signed by 1 August 2025 (art. III(4)). D300 has a separate row 11 for it.

**Which rate applies when the rate changes.** Generally the rate in force at the taxable event; apply the statutory event/timing rules for the particular supply. Where an invoice or advance came first, the rate at that earlier date applies and is regularised to the rate at delivery (art. 291(4) and (6)). Imports and intra-EU acquisitions take the rate for the same goods supplied in Romania (art. 291(7) and (8)).

## The taxable base

**Ordinary domestic base.** The consideration received or receivable, including price-linked subsidies, is the starting point (art. 286(1)(a)). Do not classify a bank movement as a VAT supply without the underlying invoice and supply facts. Special base adjustments, foreign currency and imports are held below.

**Chargeability.** Generally at the taxable event, or earlier invoice/advance under art. 282(1)-(2). Cash accounting has different eligibility, payment and deduction rules; do not apply the ordinary timing to it (specific hold below).

**Deduction.** Purchases must serve operations giving deduction rights under art. 297(4), and satisfy art. 299 documentation. A compliant invoice is required; payment evidence is also required where cash accounting applies. For ordinary Romanian established-to-established transactions, art. 319(1^1) ties invoice status to OUG 120/2021. The reverse-charge purchase matrix does not guarantee recovery: apply these same conditions.

- **Vehicles:** art. 298 limits deduction to 50% for vehicles not used exclusively in economic activity, including purchase/lease and related costs. The restriction does not cover vehicles above 3,500 kg or more than 9 seats including the driver; specified emergency/security/courier vehicles require exclusive qualifying use. Sales/purchasing agents, paid passenger transport, paid services including driving schools, rental/leasing and trading stock have statutory exceptions. All remain subject to ordinary deduction conditions; a van’s N1 classification alone is not sufficient.
- **Mixed activity:** allocate exclusive-use costs to activities with/without deduction; common costs generally use pro rata (art. 300(3)-(5)), with the investment exception in art. 300(5). The detailed annual formula and capital-goods adjustments remain on hold below.
- **Alcohol/tobacco:** art. 297(7)(b) blocks deduction except resale, use for supplying services and the specified art. 270(8)(b)/271(5)(b) cases. Do not treat every business dinner or gift as automatically deductible.

## Deadlines and filing

**Registration.** An exempt business exceeding the art. 310 threshold must request registration by the crossing date. Tax the whole crossing transaction, not only the excess; it may also tax earlier transactions on that same day (art. 310(6)). For late registration ANAF backdates and establishes output less allowable input tax, or a negative balance if input exceeds output (art. 310(6^1)). A taxpayer discovering its own delay uses art. 310(6^2)-(6^3), reporting the adjustment after registration rather than filing all missed D300 periods (art. 323(4)). Initial registration, voluntary entry and cancellation are separate tests; see holds.

**Period.** Month is the default. Quarterly treatment uses the EUR 100,000 prior-year turnover test and no prior-year intra-EU goods acquisitions (art. 322(2)); use the specific annualisation rules for businesses registering during the year (art. 322(3)-(5)). Quarterly filers give the art. 322(6) declaration by 25 January, except those requesting deregistration for the small-enterprise exemption. When a quarterly filer makes a taxable EU goods acquisition: first-month chargeability changes to monthly from that month; second-month chargeability creates a first-two-month period then monthly from month three; third-month chargeability changes from the next quarter. Notify within 5 working days of that acquisition month-end; monthly treatment continues for the current and next year (art. 322(7)-(8)). Special approved half-year/year periods and ex-officio registration periods are held below.

| Filing | Deadline and action | Official source URL |
|---|---|---|
| D300 under art. 316 | 25th of the month following the period; pay by the same deadline (art. 323, 326). A 25 December deadline moves to 21 December, or the preceding working day if 21 December is not working. Other holiday rollover dates are held below. | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_174_2026.pdf |
| D394 domestic listing | 30th after the D300 reporting period, including periods with no reportable operations; January monthly reporting uses 28/29 February. Do not include EU acquisitions/services required in D390. | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_77_2022.pdf |
| D390 VIES | Monthly, by the following 25th, for reportable EU goods/services and call-off-stock events under art. 325; not a nil return. EU B2B services exempt in the customer state are excluded. | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_705_2020.pdf |

**Filing steps.** Use ANAF’s D300 assistance program (OPANAF 174/2026, annex 2). Select period/year, enter identification and applicable special-status boxes; reconcile the sales/purchase journals, deductions, adjustments and brought-forward balances. Submit electronically through ANAF’s electronic-declarations service; retain the submission and processing receipt and resolve errors. Use the D300 refund box only under the refund conditions below. Keep a payment/offset record for the amount due.

**D300 rows (OPANAF 174/2026)**, for orientation:
- rows 1 and 2: intra-EU supplies exempt under art. 294(2)(a) and (d), and their regularisations;
- rows 3 and 3.1: supplies with place of supply outside Romania and the other art. 294(2)(b)-(c) supplies included by the form, of which qualifying intra-EU B2B services;
- rows 5 to 8: intra-EU acquisitions of goods and other reverse-charge purchases, collected side;
- row 9: domestic supplies at 21%; row 10: at 11%; row 11: at 9% under Legea 141/2025 art. III;
- row 12 (12.1 at 21%, 12.2 at 11%): domestic reverse-charge purchases, collected side; row 13: domestic reverse-charge sales;
- row 14: exempt with deduction; row 15: exempt without deduction;
- row 19: total VAT collected;
- rows 20 to 23: reverse-charge purchases, deductible side; row 24: purchases at 21%; row 25: at 11%; row 26: domestic reverse charge;
- row 30: total deductible; row 31: deducted after art. 297, 298 and 300; row 34: pro rata and adjustments; row 35: total deducted;
- row 36 or 37: negative amount or VAT payable for the period; row 44 or 45: balance payable or negative balance at the end.

**RO e-TVA.** Reconcile the pre-filled information with the underlying records; it is not an assessment (OUG 70/2024 art. 3(5)). OUG 89/2025 art. XII repealed the art. 5(8) reply obligation and art. 7 fine from 1 January 2026. Do not use the historical “accept or explain within 20 days” rule. Current notice timing, comparisons and cash-accounting suspension expiry are explicitly held below because the current consolidated ordinance was unavailable.

**RO e-Factura.** For invoices within the mandatory scheme, the 2026 transmission deadline is 5 working days from issue, capped at 5 working days after the latest issue date under art. 319(16); compute it under Regulation 1182/71 (OUG 89/2025 art. X, XIV). Scope exceptions, B2G/B2C commencement, non-established recipients, formats and penalties need the separate e-invoice review below.

**Refunds.** Under art. 303(7), tick the D300 refund box or carry the negative balance forward. A balance of 5,000 lei or less must normally be carried forward; insolvency has a separate statutory exception, held below. A requested refund is not also carried forward. Withdrawal is possible by notification until the refund/assessment decision is communicated (art. 303(8)). Do not promise an automatic refund in 45 days; processing, inspection and foreign-business refunds are held below.

## Penalties and interest

Ordinary late payment attracts interest of **0.02% daily** plus penalty of **0.01% daily**, from the day after maturity through extinguishment inclusive (Procedure Code art. 174(1),(5), 176). Interest remains payable where art. 181 instead imposes a non-declaration penalty. Its **0.08% daily** applies to undeclared/incorrectly declared principal established by an assessment, replacing the 0.01% penalty. Reduction by 75% requires payment/offset by art. 156(1)’s deadline, or completion of an instalment plan. The principal cap excludes judicially established evasion, whose penalty is increased by 100%; the under-50-lei and official-interpretation exceptions in art. 181(6)-(7) also apply. Filing fines and their procedural exceptions are held below.

## Cross-border points

Use this matrix only for a normally registered art. 316 business, with the stated liability/exemption established. “Input” means the VAT before any restriction; actual deduction is separate. The [2026 D300 form and instructions](https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_174_2026.pdf) control every row.

| Transaction | 2026 D300 destination and condition |
|---|---|
| Domestic ordinary sale | 9 at 21%; 10 at 11%; qualifying Legea 141/2025 art. III 9% sale at 11. |
| Domestic ordinary purchase | 24 at 21%; 25 at 11%; eligible capital assets use their transaction/rate row, not a universal “capital row 27”. |
| Taxable intra-EU goods acquisition | Output 5 (5.1 when applicable), input 20 (20.1); Romanian rate for those goods, not automatically 21% (art. 291(8), 326(2)). |
| General-rule B2B services bought from a non-established supplier | Output 7, input 22; EU services also 7.1/22.1 and D390. Art. 278(2) locates the supply at the receiving business/fixed establishment; art. 307(2) applies only where the supplier is not established for that supply and does not use the Romanian SME exemption. A foreign VAT charge does not itself decide liability. |
| General-rule EU B2B service sale | 3 and subset 3.1, plus D390 if not exempt in the customer state; other outside-Romania supplies at 3 as applicable. Special place-of-supply cases are held below. |
| Exempt EU goods supply | 1; corrections 2. Require transport to another Member State, the customer’s valid other-state VAT number, evidence under art. 294(3), and D390 compliance under art. 294(2^1), subject to the satisfactory-justification exception. Small-enterprise and margin-scheme exclusions remain relevant. |
| Export/exempt supply | 14 for exemptions with deduction not already at 1–3; 15 for without-deduction supplies. Establish the exemption and its documents first; special exemptions are held below. |
| Domestic reverse charge | Supplier 13; recipient output 12 (12.1/12.2), input 26 (26.1/26.2). Both parties must be registered under art. 316. The supplier omits VAT; recipient self-assesses and deducts only as allowed (art. 331(1),(3),(5)). |

**Domestic reverse-charge categories.** Art. 331(2) covers specified waste/scrap, statutory timber, qualifying cereals/technical plants, emissions/green certificates, qualifying electricity/gas traders, taxable buildings/land, specified gold, mobile phones, pre-integration chips, consoles, tablets and laptops. Electronics require at least **22,500 lei excluding VAT of those goods on an invoice**. Letters c–f and i–l apply through 31 December 2026 (art. 331(6)-(7)); energy trader licensing/declarations, product-code and gold conditions must be established before using the matrix, and are held below.

## Worked examples

### Example 1: monthly filer, February 2026 return, paid 30 days late

A Bucharest SRL files monthly. In February 2026 it sells goods at 21% for 100,000 lei and catering at 11% for 20,000 lei, both excluding VAT. It buys stock at 21% for 40,000 lei. It also pays 10,000 lei plus VAT to run a car at most 3,500 kg and at most 9 seats including the driver, with no statutory exception, which the director also uses privately, so only 50% of that VAT is deductible (art. 298(1)). The D300 is due on Wednesday 25 March 2026 (art. 323(1)). The company files on time but pays on 24 April 2026, 30 days late (26 March to 24 April inclusive, Procedure Code art. 174(1)).

Collected VAT is 21,000 lei (row 9) plus 2,200 lei (row 10), so 23,200 lei. Deductible VAT is 8,400 lei on stock plus half of the 2,100 lei car VAT, so 9,450 lei. VAT payable is 13,750 lei. Interest at 0.02% a day for 30 days is 82.50 lei, and the late penalty at 0.01% a day is 41.25 lei. There is no late-D300 filing in these facts. Assume ordinary accrual accounting, compliant invoices, full taxable business use of stock, no other adjustments/balances and payment extinguishment on 24 April.

```oa-check
name: Romania February 2026 D300, monthly SRL, paid 30 days late
inputs:
  sales_21: 100000
  sales_11: 20000
  stock_21: 40000
  car_costs_21: 10000
  days_late: 30
steps:
  - vat_row_9: sales_21 * 21 / 100
  - vat_row_10: sales_11 * 11 / 100
  - collected: vat_row_9 + vat_row_10
  - input_stock: stock_21 * 21 / 100
  - input_car_full: car_costs_21 * 21 / 100
  - input_car_deductible: input_car_full * 50 / 100
  - deducted: input_stock + input_car_deductible
  - payable: collected - deducted
  - interest: payable * 2 / 10000 * days_late
  - late_penalty: payable * 1 / 10000 * days_late
expected:
  collected: 23200
  deducted: 9450
  payable: 13750
  interest: 82.50
  late_penalty: 41.25
```

### Example 2: small enterprise crosses 395,000 lei in September 2026

A consultancy PFA in Cluj uses the small-enterprise exemption. Its prices are agreed excluding VAT. Its turnover from January to 14 September 2026 is 372,000 lei. On 15 September it invoices a business client 40,000 lei. That takes its 2026 turnover to 412,000 lei, above the 395,000 lei threshold (art. 310(1)). It must apply to register by 15 September, and the normal regime applies from that invoice onwards (art. 310(6)). So the crossing invoice carries VAT at 21%, as does the 15,000 lei it invoices later in September. Assume the whole consultancy supply occurs on 15 September, art. 310 turnover has been correctly measured, no earlier optional same-day taxation, and compliant purchases for fully taxable business use give deductible input VAT of 1,200 lei from that date.

The crossing invoice carries 8,400 lei of VAT and the later work 3,150 lei, so 11,550 lei is collected. After deducting 1,200 lei, 10,350 lei is payable. Turnover above the threshold on the crossing day is 17,000 lei. That figure is a check only: the whole crossing invoice is taxed, not just the excess. Had the PFA not registered, ANAF would register it from 15 September anyway and assess the same 10,350 lei, plus interest (art. 310(6^1)).

```oa-check
name: Romania small enterprise crosses 395,000 lei threshold, September 2026
inputs:
  turnover_before: 372000
  crossing_invoice: 40000
  later_invoices: 15000
  threshold: 395000
  input_vat_after: 1200
steps:
  - turnover_at_crossing: turnover_before + crossing_invoice
  - excess_on_crossing_day: turnover_at_crossing - threshold
  - vat_crossing: crossing_invoice * 21 / 100
  - vat_later: later_invoices * 21 / 100
  - collected: vat_crossing + vat_later
  - payable: collected - input_vat_after
expected:
  turnover_at_crossing: 412000
  excess_on_crossing_day: 17000
  vat_crossing: 8400
  collected: 11550
  payable: 10350
```

## Historical cases retained

Original inputs are preserved below; conditional results use the 2026 matrix and deduction rules above. **HOLD** means no filing/deduction outcome is authorised from these facts. For every held case: Check this point with one of our partner accountants.

| Original case | Inputs and disposition |
|---|---|
| EC1 | Hotel in Italy with Italian 10% VAT: HOLD local accommodation and foreign-refund conditions; do not conclude that foreign VAT is permanently irrecoverable. |
| EC2 / old Test 2 | US SaaS monthly EUR 50, approximately RON 250, no VAT: on the ordinary B2B/liability conditions, 7/22 each 52.50 at an assumed documented RON 250 base and 21% rate. EUR conversion itself remains held. |
| EC3 / old Test 3 | German goods, DE VAT number; French machinery EUR 10,000, 0% invoice: 5/20 if taxable acquisition established; domestic goods rate and documented lei base required, so no invented EUR conversion or automatic net-zero deduction. |
| EC4 | Car RON 100,000 + 21,000 VAT, mixed use: 10,500 deductible if art. 298 restriction applies and normal invoice/use conditions met; other 10,500 not deducted. |
| EC5 / old Test 6 | Scrap between Romanian VAT registrants; Test 6 net RON 10,000: if statutory scrap and both art. 316 registered, 12/26 each 2,100 at 21%; supplier 13. Net zero only with full deduction. |
| EC6 | Credit note reducing earlier invoice: HOLD adjustment date/rate and appropriate correction row; do not simply overwrite the original filed return. |
| EC7 | Pre-filled D300 differs from books: reconciliation retained; old 20-day accept/explain outcome withdrawn. Current notice mechanics are held below. |
| EC8 / EC17 | Invoice 31 July 2025 at 19%, paid August; July contract with July 19%/August 21% portions: HOLD historical chargeable-event, advance and regularisation analysis. The 2026 year has not been substituted for these original dates. |
| EC9 / EC15 | China goods through Constanța; authorised deferred import VAT: HOLD customs liability, documents, authorisation and D300 mapping; old “art. 326^1” and universal row 25 are not usable. |
| EC10 / EC11 / old Test 8 | Promotional items RON 50 each; gift RON 200 + 42 VAT: HOLD protocol/promotion, input deduction and any deemed-supply tax; the old blanket RON 100 input-tax block is withdrawn. |
| EC12 | ANAF cancellation notice: HOLD grounds, effective date, missing returns and re-registration procedure; do not promise a mandatory inspection in every case. |
| EC13 | Processed timber between Romanian VAT registrants: apply 13/12/26 only after proving the statutory timber classification; this classification remains held. |
| EC14 | Smartphones RON 30,000 between Romanian companies: 12/26 when both art. 316 registered and the electronics invoice-value test is met; full deduction remains conditional. |
| EC16 | Delivery car RON 60,000 + 12,600 VAT: up to 12,600 deductible only with demonstrated exclusive economic use or a proved statutory exception and normal deduction conditions. |
| Old Test 1 | Office supplies net 1,000, VAT 210, gross 1,210 RON: row 24 before restrictions; 210 deductible with ordinary invoice/business-use conditions. |
| Old Test 4 | Mixed-use car net 80,000 + 16,800 VAT RON: 8,400 deductible and 8,400 not deducted if the art. 298 restriction applies. |
| Old Test 5 | US export EUR 5,000: HOLD export evidence and lei conversion; not the historical row 8. Conditional destination is 14 when the export exemption is established. |
| Old Test 7 | Hotel RON 500 + 45 VAT at 9%, business trip before July 2026: HOLD invoice correction/date. The original amounts are preserved but 9% is not a 2026 hotel rate. |
| Old Test 9 | Mixed-use car fuel RON 500 + 105 VAT: 52.50 deductible and 52.50 not deducted on the same restriction/documentation conditions; purchase row 24 before restriction. |
| Old Test 10 | IT consulting to Bulgarian B2B client EUR 2,000: 3/3.1 and D390 on the ordinary B2B/customer-state conditions; lei conversion remains held. |
| Old Test 11 | Wine RON 1,000 + 210 VAT, purchaser not a bar/restaurant: HOLD actual use and art. 297(7)(b) exceptions; business label alone does not decide deduction. |
| Old Test 12 | Business client dinner RON 500 + 105 VAT at 21%: HOLD invoice components/rates, business purpose and deduction; the historical blanket recovery and CIT 2% comparison are not usable. |

## Ask the client first

Obtain registration/CUI, establishment, prior/current turnover under the correct definition, acquisitions and fiscal vector; supply dates and classification; customer VAT numbers and transport documents; invoices/e-invoice status; car specifications/use and exceptions; exempt activity, cash accounting, prior balances, notices and filing receipts. Stop the affected computation where these facts are missing.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code, operative art. 269, 278(2), 282, 286, 291, 294, 297–300, 303, 307, 310, 322–326, 331 and relevant norms; ANAF consolidation states Legea 204/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-11-27: read the retained rules and their conditions; held areas below are not presented as proved |
| Procedure Code art. 174, 176, 181 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-11-27: daily accrual, substitution, reductions and exceptions |
| Legea 141/2025 art. II pt. 42, III, VII | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-11-27: rate change and housing conditions also printed in the consolidated Code |
| D300 OPANAF 174/2026, annexes 1–2 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_174_2026.pdf | 2026-11-27: form rows, electronic completion and deadlines including December exception |
| ANAF D300 assistance page | https://static.anaf.ro/static/10/Anaf/Declaratii_R/300.html | 2026-11-27: current 2026 program |
| D394 OPANAF 77/2022, annex instructions | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_77_2022.pdf | 2026-11-27: report scope, nil period, deadline and January exception |
| D390 OPANAF 705/2020, annex 2 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_705_2020.pdf | 2026-11-27: monthly reportable events and 25th deadline |
| OUG 70/2024 art. 3(5), original act | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_70_2024.pdf | 2026-11-27: pre-filled return is not an assessment; current notice mechanics held |
| OUG 89/2025 art. X, XII–XIV | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf | 2026-11-27: 2026 five-working-day transmission rule and repeal of reply duty/fine |

**Not yet confirmed — non-usable holds.** Each item below preserves a previously covered topic but gives no operational result. Check this point with one of our partner accountants.

- Art. 317 registration/D301 liability, initial/voluntary art. 316 registration, non-established suppliers/fiscal representatives, small-enterprise exit and cancellation/reactivation; EU cross-border SME scheme (including the historical EUR 85,000 domestic/EUR 100,000 EU assertions).
- Cash accounting: January–February 2026 ceiling, March–December 5,000,000 lei and 2027 5,500,000 lei eligibility/exit and transaction exceptions. These figures are historical inputs to the hold, not sufficient eligibility tests.
- RO e-TVA notice procedure: previously stated minimum 20% and 5,000 lei comparison, 5th-day delivery, regularisation/error/data exceptions and 30 September/1 October 2026 cash-accounting suspension/revival. The consolidated ordinance at legislatie.just.ro could not be read; the original acts and OUG 89/2025 do not by themselves prove all later amendments.
- Exemption classification under art. 292 (medical, education, social care, financial/insurance, lettings/old property, postal and gambling), property options, international transport and related financial intermediation, transfer of business, traveller exports previously EUR 175, customs/deferred imports and foreign VAT refunds.
- Detailed base discounts/cancellations/returns/credit notes, incidental charges, import base and currency conversion; historical pre-August 2025 19%/9%/5% supplies and advance regularisations. Apply no historical rates to a 2026 transaction from this hold.
- Pro-rata exclusions, rounding, provisional/final annual computation and investment adjustments; capital-goods definition and 5/20-year adjustment rules (old RON 2,500 accounting threshold is not a proved VAT test); gifts, promotional/protocol, luxury/personal-use purchases and deemed supplies.
- OSS/EUR 10,000 distance-sales/e-services tests; special place-of-supply cases including foreign hotels/restaurants/taxis; special travel-agent, second-hand, gold, farmer and group/consolidation regimes; electricity/gas trader licensing/declarations, cereal product codes, gold conditions and timber classification.
- D406 SAF-T population, phases, frequencies, deadlines, reconciliation and penalties: historical M+2/14th, M+3 and M+4 claims and compulsory 20-day replies are withdrawn, not reusable deadlines. Annual small-enterprise notices/suspension; ex-officio and special half-year/year fiscal periods; ordinary holiday rollover and refund processing/inspection/insolvency rules.
- D300/D394/D390 fines and relief conditions; non-declaration disputes outside the ordinary conditions stated above; e-Factura scope, exceptions, B2G/B2C commencement, non-established recipients, format/archiving and fines (including the old 15% invoice-total assertion).
- The old Malta comparison and direct-tax reference numbers (CIT, micro-enterprise, dividends, CAS/CASS, employment, local/construction taxes) are not Romanian VAT filing authority. They are held for the relevant separate jurisdiction/tax Guide; no inference that micro-enterprise income-tax status removes VAT obligations is authorised.

> Contributed by OpenAccountants.
