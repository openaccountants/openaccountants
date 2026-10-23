---
name: ro-vat-return
description: "Use this skill for Romanian VAT (TVA, taxa pe valoarea adăugată) in tax year 2026: who must register, the 21% standard rate and 11% reduced rate set by Legea 141/2025 from 1 August 2025 and what the 11% list covers, the 9% transitional rate for homes ending 31 July 2026, the 395,000 lei small-enterprise exemption, monthly or quarterly D300 returns due on the 25th, the D394 local listing due on the 30th, the D390 EU listing, RO e-TVA pre-filled returns and compliance notices, RO e-Factura in five working days, domestic and EU reverse charge, intra-EU supplies, the 50% car restriction, refunds, interest and fines. Trigger phrases: Romanian VAT, TVA Romania, D300, decont de TVA, D394, e-TVA, cota TVA 21%, plafon 395.000 lei, VAT registration Romania. Out of scope: e-invoice formats and validation (romania-einvoice), company tax (ro-corporate-income-tax), residence and withholding (ro-cross-border), the system overview (ro-tax-overview)."
jurisdiction: RO
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 1.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania VAT (TVA): rates, registration, D300, D394 and RO e-TVA (2026)

This skill covers Romanian VAT for the 2026 calendar year: who is in, the rates, registration, the D300 return and its rows, the information returns, the pre-filled RO e-TVA return, reverse charge, EU trade, refunds and penalties.

The law is Title VII of Legea 227/2015 (Codul fiscal, "the Fiscal Code") and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Every article below was read on 23 October 2026 in ANAF's consolidated texts, both shown as last updated by Legea 170/2026. ANAF notes that these consolidations are not an official republication. The current rates come from Legea 141/2025, art. II pt. 42, which rewrote art. 291(1) and (2) and took effect on 1 August 2025 (art. VII(1) of that law). Older drafts of this skill credited the change to OUG 59/2025; that was wrong. Superscript article numbers are written as 278^1, 13^2 and so on.

Related skills: [romania-einvoice](romania-einvoice.md) (RO e-Factura formats, validation, archiving), [ro-corporate-income-tax](ro-corporate-income-tax.md), [ro-cross-border](ro-cross-border.md), [ro-tax-overview](ro-tax-overview.md). [romania-vat-return](romania-vat-return.md) is an older alias of this skill and points here.

## Who this applies to

**Taxable person.** Anyone who carries on an economic activity independently, whatever the purpose or result (art. 269). A supply of goods or services for consideration with its place in Romania is taxable unless exempt (art. 268).

Sort the client first:

| Group | Test | What follows |
|---|---|---|
| A. Established in Romania, normal VAT registration | Registered under art. 316 | Charges VAT, deducts input VAT, files D300, D394 and, for EU trade, D390 |
| B. Established in Romania, small enterprise | Annual turnover not above 395,000 lei (art. 310(1)) | Exempt without deduction; must not show VAT on invoices (art. 310(10)); registers when the threshold is crossed |
| C. Registered only for EU trade | Under art. 317 (intra-EU acquisitions above the limits, or B2B services bought from or sold to the EU) | Files a special return (D301) for taxable acquisitions and D390 |
| D. Not established in Romania | No seat or fixed establishment in Romania | Registers only if it makes supplies in Romania for which it is the person liable; most B2B services and many B2B goods supplies are reverse charged to the Romanian customer (art. 307) |

**Out of scope here:** customs procedure for imports, the special schemes for travel agents (art. 311), second-hand goods (art. 312) and investment gold (art. 313), and the e-invoice file format (romania-einvoice).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate (art. 291(1), as rewritten by Legea 141/2025 art. II pt. 42, in force 1 August 2025) | 21% | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Reduced rate (art. 291(2)) | 11% | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Transitional rate for one home bought by an individual (up to 120 sq m and 600,000 lei excluding VAT, no other reduced-rate home bought since 1 January 2023) with an advance contract signed by 1 August 2025 and delivery by 31 July 2026; for contracts signed 3 to 31 July 2025, a 20% advance paid by 31 July 2025 (Legea 141/2025 art. III(1) and (2)) | 9% | to 31 July 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| In force date of the rate change (Legea 141/2025 art. VII(1)) | 1 August 2025 | 2025 | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Small-enterprise exemption threshold, annual turnover (art. 310(1)) | 395,000 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| EU cross-border small-enterprise scheme, EU-wide turnover cap (art. 310^1(1)(a)) | EUR 100,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Quarterly return allowed if prior-year turnover did not exceed this, and no intra-EU acquisitions (art. 322(2)); lei value at the BNR rate for 31 December of the prior year (HG 1/2016 norms, pt. 103(2)) | EUR 100,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| VAT cash accounting ceiling, 1 March to 31 December 2026 (art. 282(3)(a), set by OUG 8/2026) | 5,000,000 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_8_2026.pdf |
| VAT cash accounting ceiling from 1 January 2027 (art. 282(3)(b)) | 5,500,000 lei | 2027 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| EU distance sales and e-services threshold (art. 278^1(1)(c)) | EUR 10,000 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Domestic reverse charge on mobile phones, chips, consoles, tablets, laptops: minimum per invoice, excluding VAT (art. 331(7)) | 22,500 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Input VAT on road vehicles not used only for business (art. 298(1)) | 50% deductible | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Export to a non-EU traveller: the supply plus VAT must be above (art. 294(1)(b)(iii)) | EUR 175 | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| RO e-TVA significant difference, both tests (OUG 70/2024 art. 5(1), as amended by OUG 87/2024) | 20% and 5,000 lei | 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_87_2024.pdf |
| Late payment interest (Procedure Code art. 174(5)) | 0.02% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Late payment penalty (Procedure Code art. 176(2)) | 0.01% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Non-declaration penalty on tax set by ANAF (Procedure Code art. 181(1)) | 0.08% per day | 2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |

**What the 11% rate covers** (art. 291(2), letters a to n):
- medicines for human use;
- food, including drinks, for human and animal consumption, and live domestic animals and birds, except alcoholic drinks, non-alcoholic drinks under NC code 2202, foods with added sugar of at least 10 g per 100 g (infant milk powder excepted) and food supplements;
- water supply and sewerage, and water for irrigation in agriculture;
- fertilisers, pesticides, seeds and agricultural services of the kinds listed by joint order (chemical fertilisers and pesticides until 31 December 2031, art. 291(3^3));
- school textbooks, books, newspapers and magazines, printed or electronic, except mainly video, music or advertising content;
- entry to castles, museums, memorial houses, monuments, zoos and botanical gardens;
- firewood, pellets and briquettes to individuals and to legal persons as end users (until 31 December 2029, art. 291(3^4));
- heat in the cold season (1 November to 31 March) to households, hospitals, schools, NGOs, religious bodies and social service providers;
- buildings delivered as social policy: old people's and pensioners' homes, children's homes and rehabilitation centres for disabled minors;
- hotel and similar accommodation, including camping pitches;
- restaurant and catering services, except alcoholic drinks and NC 2202 drinks.

Anything not on that list, and not exempt, is at 21%. Since 1 August 2025 there is no 5% or 9% rate in art. 291. The 9% rate survives only in Legea 141/2025 art. III: for the transitional homes above, and, until 1 August 2026, for buildings sold to town halls for subsidised rent under advance contracts signed by 1 August 2025 (art. III(4)). D300 has a separate row 11 for it.

**Which rate applies when the rate changes.** The rate in force when the chargeable event happens (delivery or performance). Where an invoice or advance came first, the rate at that earlier date applies and is regularised to the rate at delivery (art. 291(4) and (6)). Imports and intra-EU acquisitions take the rate for the same goods supplied in Romania (art. 291(7) and (8)).

## The taxable base

**Base.** Everything the supplier receives or will receive for the supply, including taxes and duties other than VAT and incidental costs charged to the customer (art. 286). Reduced by discounts and by cancelled or returned supplies (art. 287). For imports, the customs value plus duties and incidental costs to the first destination (art. 289). Foreign currency converts at the BNR or ECB rate, or the bank's rate if the contract says so, on the date VAT becomes chargeable (art. 290(2)).

**When VAT is due.** At delivery or performance, or earlier on an invoice or advance (art. 282(1) and (2)). A taxpayer under the ceiling that opts for cash accounting charges VAT when it is paid, and its customers deduct it only when they pay (art. 282(3) to (8)).

**Exempt without deduction** (art. 292): medical care, education, social care, financial and insurance services, lettings of immovable property (except hotels, parking, fixed machinery, safes), sales of old buildings and of land that is not building land. Letting and old-building sales can be opted into tax (art. 292(3)).

**Exempt with deduction** (art. 294): exports, intra-EU supplies of goods to a customer with a valid VAT number from another member state, international transport and related services.

**Deduction.** Input VAT on purchases used for taxable supplies is deductible (art. 297), with an invoice that meets art. 319 (art. 299). Between Romanian established taxpayers, only an invoice that meets the RO e-Factura rules counts as an invoice (art. 319(1^1)). Restrictions:
- road vehicles not used only for business: 50% of input VAT on purchase, lease and running costs (art. 298(1)). Full deduction for vehicles over 3,500 kg or with more than 9 seats, and for taxis, driving schools, rental and leasing, sales agents, couriers, security and emergency vehicles, and vehicles held as stock (art. 298(2) and (3));
- mixed businesses deduct by direct allocation and a pro rata for common costs (art. 300);
- capital goods are adjusted over 5 years, or 20 for immovable property, when use changes (art. 305).

**No losses.** VAT has no losses. An excess of input over output VAT is a negative amount, which is carried forward or claimed back (see Deadlines and filing).

## Deadlines and filing

**Registration** (art. 316). A Romanian business registers before it starts if it expects turnover above 395,000 lei, or if it opts in. A small enterprise that crosses the threshold during the year must apply at the latest on the date it crosses. The normal regime applies from that date, starting with the transaction that crosses it (art. 310(6)). If it registers late, ANAF registers it from the crossing date and collects the VAT it should have charged minus the VAT it could have deducted (art. 310(6^1)).

**Return period** (art. 322). The calendar month is the default. A business whose prior-year turnover did not exceed EUR 100,000 and that made no intra-EU acquisitions files quarterly, and confirms this by a declaration of changes by 25 January (art. 322(6)). A quarterly filer that makes a taxable intra-EU acquisition becomes monthly from the month set by art. 322(7), for the rest of that year and the next (art. 322(8)). A business that registers during the year declares its expected turnover for the rest of the year and files quarterly if that stays under the limit scaled to the months left (art. 322(3)). A small enterprise that registers after crossing 395,000 lei annualises its turnover for the year: above EUR 100,000 it files monthly, otherwise quarterly unless it made an intra-EU acquisition (art. 322(4)). A business registered by ANAF of its own motion files monthly in the year of registration (HG 1/2016 norms, pt. 103(1)).

| Return | Who | Due | Source |
|---|---|---|---|
| D300 VAT return (decont de TVA), form approved by OPANAF 174/2026 from the January 2026 period | Everyone registered under art. 316 | 25th of the month after the month (art. 323(1)); quarterly filers, 25th of the month after the quarter | OPANAF 174/2026 |
| Payment of VAT | Same | Same day as the D300 (art. 326(1)) | Fiscal Code |
| D394 local sales and purchases listing | Everyone registered under art. 316, even with nothing to report | 30th of the month after the D300 period; for a January monthly period, the last day of February | OPANAF 3769/2015 as amended by OPANAF 77/2022 |
| D390 VIES recapitulative statement | Registered under art. 316 or 317 with intra-EU supplies, acquisitions or B2B services | 25th of the month after each month with such operations (art. 325) | OPANAF 705/2020 |
| D301 special return | Persons registered only under art. 317, and others liable under art. 307(2) to (6) without art. 316 registration | 25th of the month after the month VAT became chargeable (art. 324(2)) | Fiscal Code |
| D406 SAF-T file | Taxpayers in the SAF-T phases | Under the SAF-T orders; not covered here | Procedure Code art. 59^1 |

The annual small-enterprise notices in art. 324(4) to (6) are suspended from 1 January 2024 to 31 December 2026 (OUG 115/2023 art. LXII, noted in ANAF's consolidated code).

**D300 rows (OPANAF 174/2026)**, for orientation:
- rows 1 and 2: intra-EU supplies exempt under art. 294(2)(a) and (d), and their regularisations;
- rows 3 and 3.1: supplies with place of supply outside Romania, of which intra-EU B2B services;
- rows 5 to 8: intra-EU acquisitions of goods and other reverse-charge purchases, collected side;
- row 9: domestic supplies at 21%; row 10: at 11%; row 11: at 9% under Legea 141/2025 art. III;
- row 12 (12.1 at 21%, 12.2 at 11%): domestic reverse-charge purchases, collected side; row 13: domestic reverse-charge sales;
- row 14: exempt with deduction; row 15: exempt without deduction;
- row 19: total VAT collected;
- rows 20 to 23: reverse-charge purchases, deductible side; row 24: purchases at 21%; row 25: at 11%; row 26: domestic reverse charge;
- row 30: total deductible; row 31: deducted after art. 297, 298 and 300; row 34: pro rata and adjustments; row 35: total deducted;
- row 36 or 37: negative amount or VAT payable for the period; row 44 or 45: balance payable or negative balance at the end.

**RO e-TVA pre-filled return** (OUG 70/2024, as amended by OUG 87/2024 and OUG 89/2025):
- ANAF puts a pre-filled D300 in the taxpayer's electronic account by the 5th of the month after the D300 deadline (art. 3(2)). It is not a tax assessment (art. 3(5)).
- Where a row of the filed D300 differs from it by at least 20% and at least 5,000 lei, ANAF sends a "Notificarea de conformare RO e-TVA" by the same 5th day (art. 5(1) and (5)). It may also send one below the threshold on risk grounds (art. 5(6)). Regularisation rows are not compared (art. 5(3)).
- From 1 January 2026, OUG 89/2025 art. XII repealed art. 5(8) (the duty to answer within 20 days), art. 7 (the fine for not answering) and art. 8(1) and (3) (the risk indicators tied to the answer). For businesses on cash accounting, art. 5 and 8 were suspended until 30 September 2026 (OUG 89/2025 art. XIII), so from 1 October 2026 they receive compliance notices too.
- In practice: reconcile the D300 to e-Factura before filing. A difference ANAF flags still feeds its risk analysis and can lead to an inspection.

**RO e-Factura.** From 1 January 2026, invoices must be sent to RO e-Factura within 5 working days of issue, and no later than 5 working days after the latest issue date in art. 319(16) (OUG 120/2021 art. 10(7), as rewritten by OUG 89/2025 art. X pt. 2). From the same date this also covers supplies with place in Romania to customers that are not established but are VAT-registered in Romania, except intra-EU supplies to a customer with another member state's VAT number (art. 10(1^1)). Format, B2C and penalties: [romania-einvoice](romania-einvoice.md).

**Refunds** (art. 303). A negative balance can be carried forward, or claimed by ticking the refund box on the D300; the return is then the refund claim (art. 303(7)). ANAF processes it under OPANAF 3699/2015. Its general deadline for deciding a taxpayer's request is 45 days, extended when it asks for more evidence (Procedure Code art. 77). A claim can be withdrawn until ANAF issues its decision (art. 303(8)). EU businesses not registered in Romania reclaim Romanian VAT through their home state, and Romanian businesses reclaim other states' VAT through ANAF (art. 302).

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| VAT paid late | Interest 0.02% per day plus late penalty 0.01% per day, from the day after the due date to the day of payment | Procedure Code art. 174(1) and (5), 176(1) and (2) |
| Tax not declared or declared wrongly, then set by ANAF in an assessment | Non-declaration penalty 0.08% per day instead of the 0.01% penalty; cut by 75% if paid by the due date in the assessment or rescheduled; capped at the tax | Procedure Code art. 181(1), (2), (11); art. 176(4) |
| D300 or D394 not filed on time | Fine 1,000 to 5,000 lei for medium and large taxpayers, 500 to 1,000 lei for others | Procedure Code art. 336(1)(b), (2)(d) |
| D390 not filed on time | Fine 1,000 to 5,000 lei | Procedure Code art. 337(1)(a), (2)(a) |
| D390 wrong or incomplete | Fine 500 to 1,500 lei; none if corrected by the next D390 deadline before ANAF finds it | Procedure Code art. 337(1)(b), (2)(b), (3) |
| Late registration after crossing 395,000 lei | Registration backdated to the crossing date; VAT due on supplies since then less deductible VAT, plus interest | Fiscal Code art. 310(6^1) |
| Invoice not sent through RO e-Factura | Fine of 15% of the invoice total, for the issuer and for a recipient that books it | OUG 120/2021 art. 13^2 (see romania-einvoice) |

## Cross-border points

- **Intra-EU supply of goods.** Exempt with deduction if the goods leave Romania for another member state and the customer has a valid VAT number there; report it in D390 and on D300 row 1 (art. 294(2)).
- **Intra-EU acquisition of goods.** Taxable in Romania at the domestic rate; the buyer self-assesses (rows 5 and 20). A quarterly filer becomes monthly (art. 322(7)).
- **B2B services.** The general rule taxes services where the customer is established (art. 278(2)). A Romanian business buying from abroad self-assesses under art. 307(2) (rows 7 and 22). Selling to an EU business, it reports row 3.1 and D390.
- **Distance sales and e-services to EU consumers.** Taxed in the customer's state once EU-wide sales pass EUR 10,000 a year (art. 278^1). The Union OSS (art. 315) replaces registering in each state.
- **Non-established businesses.** Where the customer is a Romanian VAT-registered business, the customer is usually liable (art. 307(2)). An EU business that must register in Romania can do so directly or through a fiscal representative. A non-EU business must appoint a fiscal representative (art. 316(7)).
- **Domestic reverse charge** (art. 331), only between two Romanian VAT-registered parties: waste and scrap, timber, cereals and technical plants, emission and green certificates, electricity and gas to traders, buildings and land taxed by law or by option, investment gold under option, and mobile phones, chips, consoles, tablets and laptops from 22,500 lei per invoice. The cereals, certificates, energy and electronics items (letters c to f and i to l) run until 31 December 2026 (art. 331(6)).
- **Treaties** do not affect VAT. Residence for income tax: [ro-cross-border](ro-cross-border.md).

## Worked examples

### Example 1: monthly filer, February 2026 return, paid 30 days late

A Bucharest SRL files monthly. In February 2026 it sells goods at 21% for 100,000 lei and catering at 11% for 20,000 lei, both excluding VAT. It buys stock at 21% for 40,000 lei. It also pays 10,000 lei plus VAT to run a car the director also uses privately, so only 50% of that VAT is deductible (art. 298(1)). The D300 is due on Wednesday 25 March 2026 (art. 323(1)). The company files on time but pays on 24 April 2026, 30 days late (26 March to 24 April inclusive, Procedure Code art. 174(1)).

Collected VAT is 21,000 lei (row 9) plus 2,200 lei (row 10), so 23,200 lei. Deductible VAT is 8,400 lei on stock plus half of the 2,100 lei car VAT, so 9,450 lei. VAT payable is 13,750 lei. Interest at 0.02% a day for 30 days is 82.50 lei, and the late penalty at 0.01% a day is 41.25 lei. The return was filed on time, so no fine applies.

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

A consultancy PFA in Cluj uses the small-enterprise exemption. Its prices are agreed excluding VAT. Its turnover from January to 14 September 2026 is 372,000 lei. On 15 September it invoices a business client 40,000 lei. That takes its 2026 turnover to 412,000 lei, above the 395,000 lei threshold (art. 310(1)). It must apply to register by 15 September, and the normal regime applies from that invoice onwards (art. 310(6)). So the crossing invoice carries VAT at 21%, as does the 15,000 lei it invoices later in September. Input VAT on its purchases from 15 September is 1,200 lei and is deductible.

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

## Ask the client first

1. Is the business established in Romania, and is it registered under art. 316, art. 317, or neither? If neither, what was its turnover so far this year and in 2025, measured as art. 310(2) says?
2. Did 2025 turnover exceed EUR 100,000, and has it made any intra-EU acquisition of goods? That decides monthly or quarterly.
3. What does it sell? Check each line against the 11% list. Does it sell homes that are still at 9% until 31 July 2026?
4. Does it trade with other EU states, buy services from abroad, or sell online to consumers in other states?
5. Does it use cars privately, make exempt supplies, or use cash accounting?
6. Has it had a RO e-TVA compliance notice, or are there e-Factura invoices it has not booked?

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code, Legea 227/2015, Title VII (art. 265 to 334), with the HG 1/2016 methodological norms (pt. 103) printed in the same page, ANAF consolidated text last updated by Legea 170/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Fiscal Procedure Code, Legea 207/2015 (art. 75, 77, 174, 176, 181, 336, 337), ANAF consolidated text last updated by Legea 170/2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| Legea 141/2025, art. II pt. 42 (art. 291 rates), art. III (9% transitional rate), art. VII(1) (in force 1 August 2025), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-10-23 |
| OUG 8/2026 (cash accounting ceiling), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_8_2026.pdf | 2026-10-23 |
| OUG 89/2025, art. X (RO e-Factura 5 working days, non-established VAT-registered customers), art. XII to XIV (RO e-TVA changes from 1 January 2026), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf | 2026-10-23 |
| OUG 70/2024 (RO e-TVA), original text, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_70_2024.pdf | 2026-10-23 |
| OUG 87/2024, art. III (RO e-TVA timing, 20% and 5,000 lei threshold, compliance notice), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_87_2024.pdf | 2026-10-23 |
| OPANAF 174/2026, D300 form, rows and deadlines, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_174_2026.pdf | 2026-10-23 |
| ANAF, D300 form page (OPANAF 174/2026 from the January 2026 period) | https://static.anaf.ro/static/10/Anaf/Declaratii_R/300.html | 2026-10-23 |
| OPANAF 77/2022 amending OPANAF 3769/2015, D394 deadline, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_77_2022.pdf | 2026-10-23 |
| ANAF, D394 form page | https://static.anaf.ro/static/10/Anaf/Declaratii_R/394.html | 2026-10-23 |
| OPANAF 705/2020, D390 VIES form and deadline, ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_705_2020.pdf | 2026-10-23 |
| OUG 115/2023, art. LXVIII pt. 15 (OUG 120/2021 art. 13^2, 15% fine), ANAF copy | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_115_2023.pdf | 2026-10-23 |

Not yet confirmed: legislatie.just.ro did not load on 2026-10-23, so OUG 70/2024 and OUG 120/2021 were read as their original texts plus the amending acts listed, not as consolidated texts; an amendment made after OUG 89/2025 would not show here. When the 25th falls on a weekend or public holiday, Procedure Code art. 75 sends the computation to the Civil Procedure Code, which was not read for this skill, so the roll-over to the next working day is not stated here; Example 1 uses a period whose deadline is a working day. The cash accounting ceiling for 1 January to 28 February 2026, before OUG 8/2026 took effect, was not checked.
