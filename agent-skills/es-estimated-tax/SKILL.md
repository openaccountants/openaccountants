---
name: es-estimated-tax
description: "Calculates 2026 Spanish quarterly IRPF advances for ordinary common-territory self-employed taxpayers. Covers Modelo 130 cumulative direct assessment, quarter-only agricultural receipts, activity-specific withholding exemptions, low-prior-income reductions, negative-result utilisation and the legacy home-loan adjustment. Explains Modelo 131 payment mechanics and the need for an activity-specific module worksheet, distinguishing the ordinary statutory baseline from AEAT's expressly preserved 2026 post-repeal entry and election route. Includes Ceuta and Melilla rate reductions and the Q3/Q4 La Palma extension, filing windows, annual crediting and sourced penalties. Use for pagos fraccionados, IRPF trimestral, Modelo 130, Modelo 131, autonomous-worker estimated tax, a 70% withholding test, quarterly losses or prior-quarter payments. Foral and non-resident computations remain separate."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/es-estimated-tax"
  jurisdiction: "ES"
  tax_year: "2026"
  last_updated: "2026-10-28"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Spain: quarterly IRPF advances, 2026

**Sourced from the law.** Independent whole-pack review and accountant sign-off are pending. Calculate quarterly IRPF advances from the correct activity and period. An advance is a payment toward annual IRPF, not a deductible business expense.

## Who this applies to

Ordinary common-territory IRPF taxpayers carrying on an economic activity calculate payments under [RIRPF arts. 109–112](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a109). Direct assessment uses Modelo 130; objective assessment uses Modelo 131. Establish the actual tax method, activity and residence first. Corporate taxpayers use the corporate instalment route; [Bizkaia, Álava, Gipuzkoa and Navarra personal-business instalments](es-foral-income-tax.md) use their separately supplied territorial methods and the stated payment boundaries. IRNR uses its own payment rules. A Spanish resident's foreign customer or foreign income does not by itself remove their resident IRPF obligations.

Test the withholding exemption **per eligible activity before computing a payment**. Professionals qualify where at least 70% of the preceding calendar year's activity receipts bore withholding/payments on account. Agricultural/livestock and forestry activities have corresponding tests excluding current/capital subsidies and compensation from their denominator. Ordinary business activities do not inherit the professional exemption. In an activity's start year, use the qualifying withholding share for the payment period under art. 109.5 and the form instructions, rather than inventing a previous-year amount. An exempt activity has no return/payment obligation for that activity; another non-exempt activity can still require a return. The exemption ratio is the share of **receipts subject to withholding**, not tax withheld divided by turnover ([art. 109](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a109)).

For an income-attribution entity, each partner/member makes their own payment in proportion to their profit share; do not file the individual's Modelo 130 in the entity's name ([art. 112](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a112)).

## Rates, bands and thresholds

| Item | Rule/amount | Tax year | Official source |
|---|---|---|---|
| Direct assessment, non-agricultural section | 20% of positive net income from 1 January to quarter end | 2026 | [RIRPF art. 110.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Objective assessment, ordinary non-agricultural activities | 4% of the relevant module net income; 3% with employee units above zero up to one; 2% with no employee units | 2026 | [Art. 110.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110); [Modelo 131 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html) |
| Objective assessment, no determinable base data | 2% of the quarter's eligible sales/receipts | 2026 | [Art. 110.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Agriculture/livestock/forestry/fishing | 2% of quarter receipts, excluding capital grants and compensation | 2026 | [Art. 110.1.c](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Qualifying Ceuta/Melilla activity | Reduce the above payment percentages by 60%, so 20% becomes 8% and 2% becomes 0.8%; do not reduce the income base by 60% | 2026 | [Art. 110.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Qualifying La Palma activity | The equivalent reduction applies to Q3/Q4 payments; it is not retroactively applied to Q1/Q2 instalment rates | Q3–Q4 2026 | [LIRPF DA 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-8); [Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |
| Eligible activity's withholding exemption | At least 70% of the specified receipt base | 2026 | [RIRPF art. 109.2–109.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a109) |
| General reduction of module net income | 5%, included in the net-module worksheet used for payments; do not subtract it a second time from the tax payment | 2026 | [Orden HAC/1425/2025 DA 1](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272#da) |
| Legacy habitual-home financing: direct non-farming route | 2% of cumulative net income, cap 660.14 **per quarter**; foreseeable gross annual receipts below 33,007.20 and qualifying DT 18 home expenditure | 2026 | [RIRPF art. 110.3.d.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110); [gazetted Modelo 130, annex I](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf) |
| Legacy home financing: farming route | 2% of eligible quarter receipts, aggregate annual cap 660.14; foreseeable annual receipts below 33,007.20 | 2026 | [Art. 110.3.d.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Legacy home financing: module route | 0.5% of eligible module net income; other no-data/farming routes use the specified 2%; overall annual cap 660.14 | 2026 | [Art. 110.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110); [Modelo 131 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html) |

The taxpayer can elect higher payment percentages under art. 110.4. A new professional's eligible 7% invoice-withholding rate, instead of the ordinary 15%, is a separate payer withholding rule and does not lower the ordinary 20% payment percentage. It requires the statutory no-professional-activity-in-the-prior-year condition and written payer communication ([RIRPF art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95)).

The prior-year low-net-income reduction is a cash reduction **after** the relevant withholding/prior-payment steps, not a reduction of current turnover:

| Prior-year net income from economic activities, EUR | Reduction per quarter, EUR | Tax year | Official source |
|---|---|---|---|
| At most 9,000 | 100 | 2026 | [RIRPF art. 110.3.c](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 9,000.01–10,000 | 75 | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 10,000.01–11,000 | 50 | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 11,000.01–12,000 | 25 | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Above 12,000 | 0 | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |

Use prior-year activity net income before irregular-income and subsequent net-income reductions, including the applicable attributed activity amounts. No prior-year activity means zero for this test. If both forms are filed, their combined reduction cannot exceed the quarterly entitlement; an unused permitted reduction can be used against positive later payments of the **same year** ([Modelo 130 instructions, box 13](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html)).

### Objective-method entry limits: ordinary text and the published 2026 route

| Preceding-year measure | Ordinary statutory baseline, EUR | 2026 published AEAT route, EUR | Official statutory source |
|---|---|---|---|
| Non-agricultural activity receipts | 150,000 | 250,000 | [LIRPF art. 31.1.3.b.a′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31) |
| Subset requiring invoices to business/professional customers | 75,000 | 125,000 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31) |
| Agricultural/livestock/forestry receipts | 250,000 | 250,000 | [Art. 31.1.3.b.b′](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31) |
| Purchases/services excluding capital assets, including subcontracting | 150,000 | 250,000 | [Art. 31.1.3.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31) |

Apply related-family/common-management aggregation and annualise the specified prior-year start-period amounts. Being below a receipts limit alone does not establish entry: check eligible activity/IAE, specific activity magnitudes, renunciation, incompatibility and VAT/IGIC coordination under the Act and annual order. The annual order's art. 3 refers back to the statutory 2026 limits; it does not itself enact the higher thresholds ([Orden HAC/1425/2025 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272#a3)).

The earlier25October read identified a real textual difference: current **LIRPF DT 32 ends the extension at2024**, after notes removing the non-convalidated extensions. That ordinary text is retained, but it is not the full 2026 administrative answer. AEAT's **1 April 2026 effects note expressly considers both RDL 16/2025 and RDL 2/2026 after non-convalidation and maintains the former higher limits for 2026**. Its current eligibility page supplies the 2026 amounts in the administrative column above. Apply that published 2026 route, retain its authority and the taxpayer's actual method history, and do not treat either repealed decree as live legislation. This corrects the prior instruction to use the lower figures as the operational answer. ([DT 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dttrigesimasegunda); [AEAT eligibility](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html); [AEAT post-repeal explanation](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html).)

For a full preceding year, an otherwise eligible trader with 200,000 total ordinary receipts,100,000 required-invoice B2B receipts and 220,000 relevant purchases passes the three 2026 numerical limits. Amounts exactly 250,000/125,000/250,000 pass; any applicable limb0.01 higher fails. A prior six-month activity with 100,000/50,000/110,000 annualises to 200,000/100,000/220,000 before comparison. If an identical/similar activity with common direction and shared means requires aggregating 60,000 additional receipts,260,000 fails the receipts test. These controls do not replace the annual-order activity computation or the other eligibility gates. ([AEAT current limits and aggregation](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html); [LIRPF 31](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a31).)

The post-repeal note's IRPF section also confirms validity of renunciations/revocations submitted while the two decrees operated. Retain the actual filing and date: RDL 2/2026 art. 11 provided **5–16 February 2026** and recognised December 2025 submissions, plus January 2026 submissions made while RDL 16/2025 operated. A 30 January filing is not preserved by that latter limb alone. A 15 February submission meets the exceptional date test; 17 February is outside it and needs a different applicable route. For an established activity, RIRPF 33 recognises **timely filing of the first-quarter direct-assessment instalment declaration** as implicit renunciation; do not replace the filing act with proof that cash was collected. For a genuine new start, use its separate statutory route for the payment on account corresponding to the **first quarter of exercising that activity**, within the prescribed period. Renunciation normally lasts at least **three years** and continues unless revoked within the applicable window; exceeding the relevant preceding-year eligibility limit makes the renunciation treated as not presented. RIRPF 35 retains the same-year exception for existing activities when a new activity starts outside módulos or with a renunciation; it does not create an unrestricted later-return election. Continuing thresholds do not reopen a window or prove a particular return correction. ([RDL 2/2026 art. 11](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2547#a1-3); [AEAT post-repeal note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html); [RIRPF33–36](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a33).)

## The base

### Modelo 130

Use the underlying verified [IRPF activity computation](es-income-tax.md): taxable receipts less allowable expenses, depreciation and the relevant method's adjustments. Preserve cash/accrual elections and timing. The form applies eligible art. 32.1 irregular-income reduction when calculating the instalment net amount. Do not deduct income-tax advances, recoverable VAT or a processor's net payout as if each were an activity expense.

| Box | Calculation | Official source |
|---|---|---|
| 01–03 | Cumulative non-farming receipts less cumulative deductible costs from 1 January to quarter end, giving signed net income | [Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |
| 04 | Applicable percentage × positive box 03; zero if net income is negative | [RIRPF art. 110.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 05 | Sum of earlier quarters' positive box 07 amounts, less their box 16 amounts; not simply earlier cash paid | [Gazetted annex I](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf) |
| 06–07 | Eligible year-to-date withholding, then `04 − 05 − 06`, preserving a negative result | [RIRPF art. 110.3.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 08–11 | Quarter-only farming/livestock/forestry/fishing receipts, current grants included and capital grants/compensation excluded; applicable percentage less eligible same-quarter withholding | [RIRPF art. 110.1.c/110.3.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 12 | `max(0, 07 + 11)`; do not carry a raw negative cumulative base as a separate credit | [Gazetted annex I](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf) |
| 13–14 | Allocated low-prior-income reduction, then signed `12 − 13` | [RIRPF art. 110.3.c](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 15 | Unused negative box 19 amounts from earlier quarters of this year, capped at positive box 14 | [Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |
| 16 | Eligible legacy-home adjustment, capped also at positive `14 − 15` | [RIRPF art. 110.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| 17–19 | `17 = 14 − 15 − 16`; box 18 is the earlier payable amount for a qualifying supplementary return for this same period; `19 = 17 − 18` | [Gazetted annex I, page 13622](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf) |

Eligible year-to-date withholding in the non-farming direct section concerns professional activities, economic urban-property letting and the specified image-rights activities; do not deduct payments withheld **by** this taxpayer from employees/suppliers. Farming/livestock/forestry use the statutory quarter withholding; the fishing route has no corresponding withholding subtraction in box 10 under the instructions. Separate qualified Ceuta/Melilla/La Palma income from activities not entitled to the reduced percentage.

A positive result is payable. A negative final result in Q1–Q3 is recorded as **A deducir** for permitted later positive payments in the same year; Q4 uses the negative-return route. A cumulative activity loss already affects the next quarter's cumulative base; it is not also a box 15 credit. A negative box 19 created by the low-income reduction is different. Neither is an automatic quarterly cash refund. Preserve each earlier return's boxes, payment and unused-credit balance; generic AEAT bank wording or an April debit alone does not prove a Modelo 130 payment.

### Legacy home adjustment and the two official-text errors

First verify entitlement under LIRPF DT 18, including the qualifying pre-2013 acquisition/rehabilitation history. It is not the national rental credit. Construction/extension payments do not qualify for this instalment adjustment. For direct assessment, apply the statutory below-33,007.20 forecast-gross-income test, annualising first-quarter receipts as prescribed. For a fixed module worksheet, test the prescribed module net amount; where no base data exist, use the specified forecast-sales test instead. The Modelo 131 instructions combine its fixed-module and no-data routes for the threshold. Farming uses the relevant forecast receipts excluding capital grants and compensation. Mixed farming/non-farming routes, concurrent 130/131 obligations and the specified employer housing communication prevent this adjustment ([RIRPF art. 110.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110); [LIRPF DT 18](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtdecimoctava)).

The current AEAT Modelo 130 web instructions wrongly append an annual 660.14 cap to the **non-farming** direct route and describe box 19's subtraction in reverse. The regulation and gazetted form resolve both: non-farming direct relief has a **660.14 per-quarter** ceiling, and box 19 is **17 minus 18**. The farming route's 660.14 cap is annual. Do not carry either web-text error into a calculation ([RIRPF art. 110.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110); [Orden HAP/258/2015 annex I](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf)).

### Modelo 131

Obtain an activity-specific annual-order module worksheet; this Guide does not replace all IAE module values, employment/investment incentives, correction indices, seasonal rules or agricultural indices. Ordinary data are fixed at 1 January or commencement, using prior-year data where the regulation prescribes. Employee units use the instruction's hours-based measure to two decimals, not a headcount rounded down to zero. Seasonal/part-year cases need the annual order's specific daily/period computation.

Box 01 aggregates the relevant module net income after applicable adjustments and the 2026 general reduction; box 02 sums each activity's applicable employee-band payment. Boxes 03/04 handle the no-data quarter-sales route, and 05/06 the agricultural/livestock/forestry quarter route. The specified qualifying young-farmer/agricultural-worker DA 6 route reduces that last payment by 25% only after its conditions are verified. Box 07 sums 02, 04 and 06; box 08 deducts eligible quarter withholding; box 09 allocates the low-prior-income reduction; box 10 is `07 − 08 − 09`. Box 11 uses eligible prior negative results up to positive box 10. Box 12 is the qualifying home adjustment, also limited by positive `10 − 11` and the remaining annual 660.14 ceiling. Boxes 13–15 then give `13 = 10 − 11 − 12`, less the prior same-period payable amount in box 14 for a qualifying supplementary return, producing `15 = 13 − 14` ([Modelo 131 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html)).

## Deadlines and filing

| Obligation | Window/rule | Tax year | Official source |
|---|---|---|---|
| Q1 / Q2 / Q3 returns and payment | Days 1–20 of April / July / October | 2026 | [RIRPF art. 111.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a111) |
| Q4 return and payment | Days 1–30 of January following the year; apply the official non-working-day calendar to the final filing date | 2026 income, 2027 filing | [RIRPF art. 111.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a111) |
| No amount payable, obligation still exists | Submit the prescribed negative/to-deduct return; do not confuse this with an art. 109-exempt activity | 2026 | [RIRPF art. 111.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a111) |
| Forms and prescribed presentation route | Modelo 130/131 through the applicable AEAT electronic or permitted generated-paper route; retain filing/payment evidence | current procedure | [Orden EHA/672/2007 arts. 1–2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6032); [current 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |

Use the period's actual direct-debit cutoff, which is separate from the return deadline. Filing, payment and any deferral request are separate records. Preserve the justificante/CSV, NRC or other actual payment confirmation and complete earlier-period calculations. VAT Modelo 303 and payer withholding Modelo 111 are different obligations; the same payee/date does not establish the same tax. Credit advances against annual IRPF with the actual withholding and other applicable prepayments ([LIRPF art. 79](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a79)).

### Payment route and evidence

For a payable Modelo130, the current AEAT instructions offer direct debit using the **complete account IBAN**. A non-collaborating bank account in the **SEPA zone** uses the specified collection intermediation by a collaborating entity; being a SEPA account alone is not the entire procedure. In the payable/NRC route, the available options include **account charge, credit/debit card or Bizum**, with the last alternatives introduced from2025. Keep the actual NRC/payment confirmation with the filing receipt.

The instructions also list **acknowledgement of debt with a deferral or offset request, payment by transfer, or entry in the tax current-account system**, each subject to its own actual eligibility/procedure. Selecting a debt-request route does not itself prove that the tax was paid or the request approved. The cash-at-an-authorised-bank option in the cited text expressly refers to a generated-paper **2025 predeclaration**. Verify the permitted route for the actual period rather than treating that dated instruction as a blanket2026paper authorisation. Sources: [actual Modelo130 instructions, payment section](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), which cite HAP/2194/2013 arts.4/6–9 and EHA/1658/2009 art.5bis for the non-collaborating SEPA-account route.

**Ceuta 2026 base change.** [LIRPF DA64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18) raises simplified direct assessment's combined provisions/hard-to-justify allowance to **10%**, retaining the ordinary 2,000 cap and other conditions, for the specified Ceuta activity entitled to art. 68.4 relief. It also raises the general módulos net-yield reduction to **10%** for qualifying Ceuta activity. These are alternative assessment routes, not two deductions against the same profit. For instalments, apply the changes only to 2026 periods whose filing window begins **more than one month after 3 September 2026**. The ordinary October window began 1 October and fails this test; the first ordinary affected quarterly window is **January2027 for Q4 2026**. Keep this base change separate from the **60% reduction in payment percentages**, and do not extend Ceuta's enhancement to Melilla/La Palma. See [es-income-tax](es-income-tax.md#ceuta-and-melilla-scale-source-and-tax-credit-calculation) for the annual calculation. Source read **2026-10-27**.

## Penalties and interest

| Event | Rule | Tax year | Official source |
|---|---|---|---|
| Voluntary late tax-due return without prior request, within 12 months | 1% plus 1% for each complete month late; article excludes corresponding penalty/pre-filing interest | 2026 | [LGT art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Such return after 12 months | 15%, plus interest after that initial 12-month period | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Conditions for surcharge reduction satisfied | 25% reduction | 2026 | [LGT art. 27.5](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Executive collection | 5%, 10% or 20% according to payment/enforcement stage, with applicable interest in the ordinary enforcement case | 2026 | [LGT art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28) |
| Underpayment offence | Minor 50%; serious 50–100%; very serious 100–150%, with classification and statutory reductions | 2026 | [LGT arts. 188 and 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) |
| Ordinary late return without economic loss | 200, halved in the specified no-prior-request case | 2026 | [LGT art. 198](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198) |
| Default interest | Segment by applicable period rate; AEAT records 4.0625% under the continued budget for 2026 until replacement | 2026 | [LGT art. 26](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a26); [AEAT interest rule](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) |

Do not assign every late return an underpayment penalty or every below-threshold underpayment the minor classification: conduct, concealment, false records and the actual statutory conditions matter. A cash shortage does not change the filing deadline; evaluate the actual collection/deferral position separately.

## Cross-border points

Establish residence and the competent common-territory or foral system. A non-resident's Spanish business/PE is dealt with under IRNR, not an assumed Modelo 130 computation. Conversely, a Spanish-resident professional's invoice to an overseas customer can affect withholding and the 70% test while the underlying business receipts remain in resident IRPF. Identify actual obliged withholding payers rather than treating every foreign receipt as exempt income.

Ceuta/Melilla's reduced payment percentages require the actual art. 68.4 entitlement. La Palma's statutory extension applies to the instalment windows not begun on the September 2026 commencement date; current AEAT instructions identify Q3 and Q4. Keep that instalment timing distinct from annual territorial credit coverage ([LIRPF DA 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-8)).

## Two worked examples that recompute

### Q2: cumulative direct assessment

Hypothetical established non-exempt activity, no territorial/home/low-income adjustment: year-to-date receipts **30,000**, allowable expenses **10,000**, eligible withholding **500**. Prior Q1 positive box 07 is **1,500**, with no box 16. Net income is **20,000**; 20% gives **4,000**. Deduct **1,500** and **500**, leaving **2,000 payable**. Prior-year net income exceeds the low-income reduction ceiling. Each input is a stated example fact.

```oa-check
name: Modelo 130 Q2 cumulative computation
inputs:
  receipts_ytd: 30000
  allowable_costs_ytd: 10000
  prior_positive_box07: 1500
  prior_box16: 0
  withholding_ytd: 500
steps:
  net_ytd: receipts_ytd - allowable_costs_ytd
  box04: max(0, net_ytd) * 0.20
  box05: prior_positive_box07 - prior_box16
  box07: box04 - box05 - withholding_ytd
  box12: max(0, box07)
  payable: box12
expected:
  net_ytd: 20000.00
  box04: 4000.00
  payable: 2000.00
```

### A loss and the low-income reduction are different carry mechanisms

Hypothetical non-exempt business, prior-year net activity income **8,500**, no withholding, home adjustment, other activity or supplementary return. Q1 cumulative net income is **−3,000**. Box 04 and box 12 are zero; the **100** low-prior-income reduction creates **−100** in the final result, available for later positive quarters of the same year. The loss itself is not a **3,000** carried tax credit.

At Q2, cumulative net income has recovered to **1,500**. The ordinary payment is **300**, with no earlier positive box 07 to subtract. Deduct Q2's **100** reduction and then the earlier unused **100**, leaving **100 payable**. The Q1 business loss already affected the new cumulative income; deducting it again as a separate credit would count it twice.

```oa-check
name: Modelo 130 business loss versus unused low-income credit
inputs:
  q1_net_ytd: -3000
  q2_net_ytd: 1500
  quarterly_reduction: 100
steps:
  q1_box04: max(0, q1_net_ytd) * 0.20
  q1_box12: max(0, q1_box04)
  q1_result: q1_box12 - quarterly_reduction
  prior_unused: max(0, -q1_result)
  q2_box04: max(0, q2_net_ytd) * 0.20
  q2_box14: q2_box04 - quarterly_reduction
  q2_box15: min(max(0, q2_box14), prior_unused)
  q2_payable: q2_box14 - q2_box15
expected:
  q1_box04: 0.00
  q1_result: -100.00
  prior_unused: 100.00
  q2_box04: 300.00
  q2_payable: 100.00
```

## Ask the client first

1. What is the activity/IAE, direct or objective method, competent territory, start/cessation date and any existing election or exclusion history?
2. What proportion of the relevant prior-year receipts bore withholding, or what is that proportion for the start-year payment period, separately for each activity?
3. What are cumulative non-farming receipts/costs, quarter-only farming receipts, eligible withholding, and the corresponding underlying ledgers/certificates?
4. What were prior-year activity net income and every earlier current-year return's relevant boxes, home adjustments, payments and unused negative results?
5. Is there documented Ceuta/Melilla/La Palma entitlement, a legacy qualifying home loan, another 130/131 activity or an employer housing communication?

## Sources

| Source | Coverage | Read on |
|---|---|---|
| [RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 95 and 109–112: withholding distinction, exemptions, rates, reductions, dates and attribution | 2026-10-25 |
| [Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 31, 79; DT 18/32; DA 57: method entry, annual crediting, home and La Palma transitions | 2026-10-25 |
| [AEAT Modelo 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) | Current page updated 11 September 2026, boxes/filing and La Palma; two errors resolved against regulation/gazetted form above | 2026-10-25 |
| [AEAT Modelo 131 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-131-irpf______sionales-estimacion-objetiva-fraccionado_/instrucciones.html) | Module payment worksheet, employee units, quarter reductions and home annual cap | 2026-10-25 |
| [Orden EHA/672/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6032), [Orden HAP/258/2015](https://www.boe.es/buscar/doc.php?id=BOE-A-2015-1656) and [gazetted annexes](https://www.boe.es/boe/dias/2015/02/19/pdfs/BOE-A-2015-1656.pdf) | Form approvals; page 13622 physically viewed: box 19 is 17−18 and non-farming home cap is per quarter | 2026-10-25 |
| [Orden HAC/1425/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-25272) | 2026 annual module order, art. 3 references statutory entry limits; DA 1 provides 5% general reduction | 2026-10-25 |
| [AEAT module entry page](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Updated 13 October 2026; its higher-limit extension claim is recorded as contrary to current DT 32, not used as legislative authority | 2026-10-25 |
| [Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Arts. 26–28, 188, 191, 198: interest, surcharge, collection and penalties | 2026-10-25 |
| [AEAT interest calculation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) | Continued-budget 2026 interest rate | 2026-10-25 |
| [AEAT1April2026 post-repeal effects note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html), [IVA eligibility](https://sede.agenciatributaria.gob.es/Sede/iva/regimenes-tributacion-iva/regimen-simplificado/quien-se-aplica-regimen-simplificado.html), [IRPF eligibility](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Published2026 higher limits and preserved submission routes, distinguished from the ordinary consolidated statutory text and the remaining legal-reconciliation boundary | 2026-10-27 |
| [RDL16/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-26458), [27January repeal](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2024), [RDL2/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2547), [26February repeal](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-4667) | Actual extending provisions and non-convalidation history; neither decree presented as currently in force | 2026-10-27 |

| [AEAT Modelo130 payment instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) | Restore full SEPA/intermediated account, NRC/account-charge/card/Bizum and debt-request/transfer/current-account options; retain explicit2025paper vintage | 2026-10-28 |


**Not yet confirmed:** the exact legal reconciliation beyond AEAT's published post-repeal explanation or case-specific correction of a filed election/return; the published 2026 AEAT thresholds and preserved submission routes are supplied above; complete activity-specific/seasonal module computations and exceptional annual-order adjustments; IRNR payment computations, the precise Navarra partial-start annualisation/form-rounding boundaries recorded in [the foral Guide](es-foral-income-tax.md), and period-specific direct-debit cutoffs. These are not replaced with assumed eligibility or invented amounts.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `es-estimated-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/es-estimated-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
