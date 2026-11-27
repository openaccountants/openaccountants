---
name: no-income-tax
description: >
  Use this skill whenever asked about Norwegian income tax for self-employed individuals (enkeltpersonforetak), alone or alongside wages, for income years 2025 and 2026. Trigger on phrases like "Norwegian tax", "trinnskatt", "alminnelig inntekt", "personfradrag", "skattemelding", "RF-1175", "naeringsoppgave", "enkeltpersonforetak", "self-employed tax Norway", or any question about filing or computing income tax for a Norwegian self-employed client. Covers alminnelig inntekt (22%), trinnskatt (5 brackets), personinntekt, trygdeavgift, skjermingsfradrag, personfradrag, minstefradrag, naeringsinntekt computation, deductible expenses, depreciation, the naeringsspesifikasjon that replaced RF-1175, filing deadlines, and penalties. ALWAYS read this skill before touching any Norwegian income tax work.
version: 2.4
jurisdiction: "NO"
tax_year: 2026
tax_year_notes: "Label 2026 means the income year 1 January to 31 December 2026. Income year 2025 is also covered, and every figure names its year."
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
type: computation
---
# Norway income tax for self-employed individuals (enkeltpersonforetak) v2.4

> **General reference only.** This Guide supports an estimated working paper, not an approved filing or payment. Resolve the named holds before using the affected outcome.

## Who this applies to

Full-year Norwegian-resident natural persons with an ordinary enkeltpersonforetak (ENK), alone or alongside wages, in **income year 2025 or 2026**. The ordinary income period is the calendar year (skatteloven § 14-1). Keep each year's inputs and rates separate: the 2025 return is filed in 2026; the 2026 return in 2027. This Guide is not a complete unattended return-preparation contract.

Before calculating, confirm the year, business status, tax residence, tax municipality, age, national-insurance coverage, spouse participation, income categories, opening/closing capital and both kinds of carried losses. A bank narration alone proves none of these. Obtain the full-year bank statements, ledger, invoices, platform gross-sales/fees reconciliations, VAT records, wage/benefit statements, prior returns, asset register and actual credited tax payments. Missing evidence is an input hold; do not invent zero income, expenses or payments. Sources: [income period](https://lovdata.no/lov/1999-03-26-14/§14-1), [return preparation](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/).

**Scope holds.** Companies; partnerships; business conversions/restructuring (omdanning); uncertain business/hobby/employment status; spouse allocation or multiple businesses; agriculture, forestry, reindeer, fishing/product-levy and petroleum regimes; Svalbard; pension/benefit computations; and a non-calendar accounting year do not receive a final liability here. Check this point with one of our partner accountants. Preserve the client's facts and identify the affected computation. Residence, foreign income and currency holds appear under Cross-border points.

## Rates, bands and thresholds

All amounts are NOK. The rates below are for the named income year, not a combined fiscal year. Ordinary-income tax is separate from personal-income bracket tax and national insurance.

### Tax on alminnelig inntekt

The 22% in the prior version is a sum of 3 rates on the same base, and its parts changed between the years.

| Item | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Fellesskatt, general | 6.6% | 8.25% | Stortingets skattevedtak 2025 and 2026 § 3-2 (FOR-2024-12-13-3203; FOR-2025-12-18-2747): https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Fellesskatt, Finnmark county and Karlsøy, Kvænangen, Kåfjord, Lyngen, Nordreisa, Skjervøy and Storfjord municipalities | 3.1% | 4.75% | Skattevedtak 2025 and 2026 § 3-2: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Municipal income tax, maximum | 12.75% | 11.35% | Skattevedtak 2025 and 2026 § 3-8: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| County income tax, maximum | 2.65% | 2.40% | Skattevedtak 2025 and 2026 § 3-8: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Total at the maximum, general | 22.00% | 22.00% | Sum of the rows above (computed): https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Total at the maximum, Finnmark and the named municipalities | 18.50% | 18.50% | Sum of the rows above (computed): https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |

Maximum local rates apply unless lower rates are adopted (§ 3-8 of each annual decision). The municipality relevant to the northern zone is the tax municipality under skatteloven § 3-1. Share/dividend income subject to an upward adjustment is outside these ordinary ENK calculations: check it with one of our partner accountants.

### Trinnskatt on personinntekt

Trinnskatt applies to personinntekt under skatteloven chapter 12 for class 0 and class 1. Each rate applies to the part of the income between its threshold and the next. The resolutions read contain no lower rate for Finnmark.

| Trinn | Income year | Above (NOK) | Rate | Official source |
| --- | --- | --- | --- | --- |
| 1 | 2025 | 217,400 | 1.7% | Skattevedtak 2025 § 3-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 |
| 2 | 2025 | 306,050 | 4.0% | Skattevedtak 2025 § 3-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 |
| 3 | 2025 | 697,150 | 13.7% | Skattevedtak 2025 § 3-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 |
| 4 | 2025 | 942,400 | 16.7% | Skattevedtak 2025 § 3-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 |
| 5 | 2025 | 1,410,750 | 17.7% | Skattevedtak 2025 § 3-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 |
| 1 | 2026 | 226,100 | 1.7% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 2 | 2026 | 318,300 | 4.0% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 3 | 2026 | 725,050 | 13.7% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 4 | 2026 | 980,100 | 16.8% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |
| 5 | 2026 | 1,467,200 | 17.8% | Skattevedtak 2026 § 3-1 and Skatteetaten: https://www.skatteetaten.no/satser/trinnskatt/ |

### Allowances and fixed deductions

| Item | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Personfradrag, class 1 | NOK 108,550 | NOK 114,540 | Skattevedtak 2025 and 2026 § 6-3, skatteloven § 15-4, and Skatteetaten: https://www.skatteetaten.no/satser/personfradrag/ https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Class 0 | No personfradrag | No personfradrag | Skatteloven § 15-4(6): https://lovdata.no/lov/1999-03-26-14/§15-4 |
| Minstefradrag, wages | 46%, maximum NOK 92,000 | 46%, maximum NOK 95,700 | Skatteloven § 6-32, skattevedtak § 6-1, and Skatteetaten: https://www.skatteetaten.no/satser/minstefradrag/ https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Minstefradrag, pension | 40%, maximum NOK 73,150 | 40%, maximum NOK 75,400 | Skatteloven § 6-32, skattevedtak § 6-1: https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Wage and pension together | Sum, capped at NOK 92,000 | Sum, capped at NOK 95,700 | Skatteloven § 6-32(1): https://lovdata.no/lov/1999-03-26-14/§6-32 https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Finnmark and named municipalities deduction, on tax computation only | NOK 30,000 (Practice) | NOK 45,000 | 2026: skatteloven § 15-5(2) as amended by lov 22 Dec 2025 nr. 119, https://lovdata.no/lov/1999-03-26-14/§15-5. 2025: Skatte-ABC 2025 T-12-1, https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/t-12-tiltakssonen-i-finnmark-og-nord-troms/T-12.001/ |
| Trial work deduction | None | NOK 125,000, tapered 40% above NOK 345,000 | Skattevedtak 2026 § 6-6, skatteloven § 6-86: https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |

The northern deduction requires tax residence in the named area under § 3-1, entitlement to personfradrag and age at least 17 at year end (§ 15-5). It reduces the tax computation only, not assessed ordinary income, bracket tax or national insurance. Full-year resident class 1 amounts are used here; no personfradrag in class 0. For pensions, the two minimum deductions are added subject to the wage cap; do not combine actual wage costs and the corresponding minstefradrag. Pension credit and low-income tax limitation outcomes are held below.

For **2026 only**, the work deduction requires actual selection: 8% of those born in 1991–2006 and on the Norwegian tax register on 31 October 2025, selected randomly. It lasts five income years. Eligible income is § 5-10 employment income excluding unemployment benefits, calculated business personal income and § 12-2(f) remuneration; the deduction is capped at eligible income and cannot create/increase a carried loss or a loss transferred to a spouse. It is an ordinary-income deduction only. The PAYE/foreign-worker standard deduction and Svalbard exclusions in § 6-86(7) apply. Confirm selection; age alone is insufficient. [Skatteloven § 6-86](https://lovdata.no/lov/1999-03-26-14/§6-86).

### Trygdeavgift

The base is personinntekt under skatteloven § 12-2 (folketrygdloven § 23-3). Stortinget sets the rates each year.

| Income type | 2025 | 2026 | Official source |
| --- | --- | --- | --- |
| Høy sats: beregnet personinntekt from an enkeltpersonforetak (næringsinntekt) | 10.9% | 10.8% | Folketrygd resolutions 2025 §§ 6 to 8 (FOR-2024-12-13-3204): https://lovdata.no/dokument/LTI/forskrift/2024-12-13-3204 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 and 2026 (FOR-2025-12-18-2748) with Skatteetaten: https://www.skatteetaten.no/satser/trygdeavgift/ |
| Mellomsats: lønnsinntekt (employment) | 7.7% | 7.6% | Same resolutions: https://www.skatteetaten.no/satser/trygdeavgift/ https://lovdata.no/dokument/LTI/forskrift/2024-12-13-3204 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 |
| Lav sats: pensjonsinntekt (pension), and personinntekt of a person under 17 or over 69 | 5.1% | 5.1% | Same resolutions, folketrygdloven § 23-3(2): https://www.skatteetaten.no/satser/trygdeavgift/ |
| Mellomsats on business income: care of a child in the carer's own home, where the child has not turned 12 before the end of the year or has a special need for care | 7.7% | 7.6% | Folketrygdloven § 23-3(2) nr. 2: https://lovdata.no/lov/1997-02-28-19/§23-3 https://lovdata.no/dokument/LTI/forskrift/2024-12-13-3204 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 |
| No contribution | Income up to NOK 99,650 | Income up to NOK 99,650 | 2026: folketrygdloven § 23-3(4), https://lovdata.no/lov/1997-02-28-19/§23-3. 2025: Skatte-ABC 2025 P-16-4.3 (Practice), https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/p-16-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-16.027/P-16.035/ |
| Maximum | 25% of the income above NOK 99,650 | 25% of the income above NOK 99,650 | Same sources: https://www.skatteetaten.no/satser/trygdeavgift/ |

Use the ordinary middle/high rates from the year the person turns 17 through the year they turn 69; the lower rate applies outside that interval. Confirm Norwegian insurance coverage separately from tax residence. Apply the floor and 25% cap **once to total personal income**, after summing the category-rate charges. Own-home childcare has the middle rate only with the child-age/special-care and location conditions in the table; its expense/minimum-deduction computation is a scope hold here. Product-levy businesses and NAV benefit classifications are also scope holds.

### Business shielding rate

| Income year | Maximum rate and condition | Official source |
| --- | --- | --- |
| 2025 | 4.6% for ENK; not the shareholder rate | https://www.skatteetaten.no/satser/skjermingsrente-for-aksjer-og-enkeltpersonforetak/ |

Choose a lower rate only in whole percentage points, clearly and by timely filing; otherwise the maximum applies (FSFIN § 12-12-10). The **2026 maximum is not supplied here**: it is set after the income year. A positive-basis 2026 shield is a non-usable outcome pending the year's published rate. Check this point with one of our partner accountants. A documented zero-basis case can still use the ordinary method. [Rate timing](https://www.skatteetaten.no/satser/skjermingsrente-for-aksjer-og-enkeltpersonforetak/), [election](https://lovdata.no/forskrift/1999-11-19-1158/§12-12-10).

### Depreciation groups

The rates are maxima in skatteloven § 14-43(1), read in the current consolidated text. The threshold of NOK 30,000 has applied from income year 2024.

| Group | Assets | Maximum rate | Official source |
| --- | --- | --- | --- |
| a | Office machines | 30% | Skatteloven §§ 14-41 and 14-43: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| b | Acquired goodwill | 20% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| c | Trailers, lorries, buses, vans, taxis and vehicles for transporting disabled people | 24% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| d | Passenger cars, tractors, machinery, tools, instruments, fixtures and fittings | 20% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| e | Ships, vessels and rigs | 14% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| f | Aircraft and helicopters | 12% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| g | Electric power transmission and distribution installations and electrotechnical equipment in power undertakings, and such assets used in other business | 5% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| h | Buildings and structures, hotels, lodging houses and eating places | 4% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| i | Commercial buildings | 2% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |
| j | Fixed technical installations in buildings | 10% | Same: https://lovdata.no/lov/1999-03-26-14/§14-43 |

Simple buildings/structures whose construction implies a life no more than 20 years may use 10%. Agricultural livestock buildings, fruit and berry fields have special rates; they remain outside this ordinary-business computation. Check this point with one of our partner accountants.

## The base

### Compute the two bases separately

1. Reconcile earned revenue, platform gross sales, refunds and fees, stock, receivables/payables and tax depreciation to business profit. Business income/costs generally follow unconditional rights/obligations, not bank dates (§ 14-2); wages follow the cash/access rule in § 14-3. Keep loans, own-account transfers and drawings out of business sales/expenses. Owner withdrawals of goods/services need their own valuation: check this point with one of our partner accountants.
2. Compute ordinary income from business profit, wages and other ordinary income, less the relevant wage/pension deduction, other established deductions and ordinary carried losses. Apply personfradrag and, if eligible, the northern deduction in the tax calculation; floor that tax base at zero and apply the ordinary rate. Do not apply minstefradrag to ordinary ENK profit. Own-home childcare is the § 6-31(1)(d) exception and remains a scope hold.
3. Compute business personal income from business ordinary income **before carried ordinary losses**. Add actual capital costs/losses, except customer-receivable losses and qualifying financial-institution/bond interest within the § 12-11(2)(a) debt ceiling (shield basis before financial debt deduction, after supplier credit/customer prepayments). Other interest is added back. Add the special deductions listed in § 12-11(2)(b) if such a scope-held regime is present. Subtract actual capital income and gains on the § 12-11(3) capital objects, excluding customer-receivable income; then the elected shield and usable negative business personal income. The farm-property/milk-quota/forestry gain exception is outside ordinary ENK scope.
4. Add wages to the non-negative business personal-income remainder. Apply bracket tax once to total personal income, using each band's marginal rate only up to the next threshold. Apply the insurance type rates separately, then the single aggregate floor/cap. A negative business remainder never reduces wage/pension personal income.
5. Add the three taxes, apply only separately established credits, and subtract evidenced withholding/advance payments. Keep interest separate. A positive balance is estimated restskatt; a negative one is estimated tilgode. Show unrounded working-paper arithmetic; reconcile assessment/payment rounding to the actual notice rather than treating an illustrative floor as the statutory final balance.

Sources: [timing](https://lovdata.no/lov/1999-03-26-14/§14-2), [minimum deduction](https://lovdata.no/lov/1999-03-26-14/§6-32), [personal-income bridge](https://lovdata.no/lov/1999-03-26-14/§12-11), [negative personal income](https://lovdata.no/lov/1999-03-26-14/§12-13), and the annual decisions above.

### Shield basis

The ordinary shield is the non-negative mean of opening and closing eligible values multiplied by the elected year's rate. Include lasting/significant operating assets, pooled smaller assets, stock, customer receivables, acquired goodwill and other acquired intangibles **that have worked in the business**. A physical asset must actually have been taken into use; delivery/saldo entry alone is insufficient. Deduct financial-institution/bond debt, supplier credits and customer prepayments. Exclude welfare assets mainly used outside working hours. Capitalised, undeducted research/development costs may be included. Tax values generally apply; § 12-12(2)(e) gives the historic-cost/assessment-value exception for non-depreciable assets, continuation of a 1999 book-value election, and the normal-business-value ceiling on disproportionately valuable assets. The initial valuation method binds later years. [Skatteloven § 12-12](https://lovdata.no/lov/1999-03-26-14/§12-12).

Part-year business, alternative stock/receivables averaging, spouse allocation and joint/separate calculation units are **non-usable special outcomes** here; retain the opening/closing balances and dates. Check this point with one of our partner accountants.

### Expenses and transaction classification

The general rule is a cost incurred to acquire, maintain or secure taxable income; private costs are excluded (§ 6-1). A cost totalling **NOK 10,000 or more** must be paid through a bank/authorized payment provider. Aggregate payments for the same delivery/service/contract and periodic payments deducted in the same year. A denied cash payment cannot enter depreciation basis or acquisition value (§ 6-51). Documentation and business purpose are required; an uncertain cost stays unclaimed pending evidence. [General rule](https://lovdata.no/lov/1999-03-26-14/§6-1), [bank rule](https://lovdata.no/lov/1999-03-26-14/§6-51).

| Item | Treatment and conditions | Source |
| --- | --- | --- |
| Ordinary supplies, premises, accountancy, advertising, transaction fees, business cover and travel | Apply § 6-1 to documented business costs; separate private portions and assets. A merchant name is only a clue. Mixed-purpose travel, personal insurance and tax-dispute legal costs have no deductible outcome here. Check this point with one of our partner accountants. | https://lovdata.no/lov/1999-03-26-14/§6-1 |
| Client meals | Modest customer/business-contact hospitality during business hours or immediately linked to negotiations/demonstrations; at work, or a nearby restaurant when no reasonable on-site catering exists. No spirits/tobacco deduction; spirits with a meal also deny the food. Restaurant ceiling per person/occasion: **2025 NOK 579; 2026 NOK 592**. Above it the **whole meal** is disallowed, not just the excess. | FSSD § 6-21-2: https://lovdata.no/forskrift/1999-11-22-1160/§6-21-2 ; annual § 10: https://lovdata.no/dokument/SF/forskrift/2024-11-27-2889 https://lovdata.no/dokument/SF/forskrift/2025-11-07-2216 |
| Gifts/attention | Ordinary gifts to business contacts, their families, their personnel or their customers are not deductible. Fixed-branded gifts designed for advertising in quantity: limit **2025 NOK 317; 2026 NOK 324 per item**. Simple attentions: the same respective limits per occasion; death wreaths have no such limit. | FSSD §§ 6-21-4 to 6-21-6: https://lovdata.no/forskrift/1999-11-22-1160/§6-21-5 ; annual § 10: https://lovdata.no/dokument/SF/forskrift/2024-11-27-2889 https://lovdata.no/dokument/SF/forskrift/2025-11-07-2216 |
| Home office | Exclusive business room: mixed living/bedroom use gives **no** deduction, including no standard fallback. In an eligible owner-occupied tax-exempt home use either actual attributable costs or the standard, not both. **2025 standard NOK 2,192**; **2026 authority standard NOK 2,240**. Eligibility includes use of at least half as own home by rental value, or a larger let share with annual rent no more than NOK 20,000. No deemed rent to oneself. Shared actual costs split by rental value, or area for equivalent parts where rental value is difficult; rented homes use supported actual allocation. No own/spouse cleaning-labour deduction; the standard is not prorated for part-year use. Accounting-treated homes and later sale outcomes are held. | 2025 § 1-3-26: https://lovdata.no/dokument/SF/forskrift/2025-12-01-2404 ; 2026 amount: https://www.skatteetaten.no/satser/hjemmekontor-standardfradrag/ ; eligibility: https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/bruke-egen-bolig-i-naring/ ; allocation: https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-14-bolig--hjemmekontor-mv/B-14.002/B-14.004/ |
| Phone/internet | Enter documented business EK costs, then reverse private use up to **NOK 4,392 annually**, limited to total costs; field **6998** in the current næringsspesifikasjon. Substantiate any claim of no private use. Apply asset rules to equipment. A future 2026 return's final field layout must be confirmed when released. | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/telefon-og-internett/ |
| Education | Maintenance/updating of qualifications already used for income may qualify; acquiring a new qualification/degree has no deduction in these fixtures. | https://www.skatteetaten.no/nn/person/skatt/hjelp-til-rett-skatt/arbeid-trygd-og-pensjon/utdanning/fradrag-for-kostnader-til-utdanning/ |
| Trade/union dues | Membership alone proves no deduction. The former 2025 amount and wage-cap interaction were unresolved. No claim under this Guide until eligibility, year and §§ 6-18 to 6-20 limits are established. Check this point with one of our partner accountants. | https://lovdata.no/lov/1999-03-26-14/§6-19 |
| Income tax, trygdeavgift, refunds and penalties | Track personal tax prepayments/refunds outside profit; do not manufacture an expense from a bank tax payment. Deductibility of a tax/penalty/charge requires its specific category; no general tax-dispute, fine or tvangsmulkt deduction is authorized here. Check this point with one of our partner accountants. | Workflow hold; https://lovdata.no/lov/1999-03-26-14/§6-15 |

### Vehicles

For an ordinary mixed-use car, business-vehicle status requires at least **6,000 business km per car/year** (look across three years) or business use exceeding half of total use. A wholly business-used car and the special heavy-lorry/bus categories have separate tests: check this point with one of our partner accountants. Document business trips; commuting/private driving is not to be relabelled business travel. [Skatte-ABC B-5-3.3](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-5-bil--fradrag-for-bilkostnader/B-5.007/B-5.010/).

| 2025 private transport only | Rate/condition | Source |
| --- | --- | --- |
| Car not taxed as yrkesbil | NOK 3.50 per documented business km; no duplicate fuel/depreciation claim covered by the rate ([B-5-3.7](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-5-bil--fradrag-for-bilkostnader/B-5.007/B-5.020/)) | Takseringsregler § 1-3-20: https://lovdata.no/dokument/SF/forskrift/2025-12-01-2404 |
| Boat; snowmobile/ATV; heavy motorcycle over 125 cc; moped/light motorcycle up to 125 cc | NOK 7.50; NOK 10.00; NOK 2.95; NOK 2.00 per km respectively | https://lovdata.no/dokument/SF/forskrift/2025-12-01-2404 |
| Supplements | NOK 1.00/km per passenger; NOK 1.00/km on forest/construction roads; NOK 1.00/km for equipment unsuitable for boot/roof rack | https://lovdata.no/dokument/SF/forskrift/2025-12-01-2404 |

A business vehicle uses relevant actual costs/depreciation with a private-use reversal, not the private-car km rate. **2026 deduction rates, precise private-use benefit/list-price/cost-cap/van-method outcomes, extra toll/ferry/parking/damage deductions and a mixed-purpose journey are held**, not silently chosen. Retain age, list price, business/private kilometres, electronic logbook and costs. Check this point with one of our partner accountants. The 2026 allowance rate is not proof of the final deduction rate.

### Depreciation and losses

A depreciating business asset goes on saldo when it is both lasting, with a life of at least 3 years, and significant, costing NOK 30,000 or more including MVA where there is no right to deduct it (skatteloven § 14-40(1)). An asset below either test may be deducted in the year of acquisition or depreciated (§ 14-40(2)): depreciation is the client's choice, and the default is the deduction. An improvement to an asset on saldo always goes on saldo (§ 14-40(3)).

Both limbs matter:

- Cost under NOK 30,000, life 3 years or more: deduct or depreciate.
- Cost of NOK 30,000 or more, life under 3 years: deduct, or spread over the expected life (Skatte-ABC 2025 D-3-1.1.1).
- A physical asset that does not lose value through wear or age cannot be deducted at any cost (D-3-1.1.2).
- A new physical asset is taken to last 3 years or more unless a shorter life is probable. Intention to sell does not count ([D-3-2](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/d-3-driftsmiddel--direkte-fradragsforing/D-3.007/)).

Groups a to d are pooled by trade and municipality; groups e to i have an individual balance per asset; group j is per building (§ 14-41). The base is the opening balance plus cost of the year's additions (§ 14-42(2)), and depreciation is taken on that sum. On sale in groups a to d and j, the price reduces the balance so far as it is not taken to income (§ 14-44(2)). In groups e to i, gain or loss goes to the gain and loss account, and so does a negative balance in group b (§§ 14-44(3) and 14-45). A negative balance in groups a, c, d or j is taken to income at no less than the group's maximum rate (§ 14-46). On the gain and loss account, a positive balance is taken to income at no less than 20%, and a negative balance may be deducted at up to 20% (§ 14-45(4)). Sources: [asset elections and non-wasting assets](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/d-3-driftsmiddel--direkte-fradragsforing/D-3.001/D-3.002/), [saldo rules](https://lovdata.no/lov/1999-03-26-14/§14-40). The NOK 30,000 tests in § 14-47 apply at the end of the income year, before that year's deduction or income entry. Under NOK 30,000, a depreciation base or a loss balance on the account may be deducted in full (§ 14-47(1)). Under NOK 30,000, a negative balance in groups a, c, d or j or a gain balance on the account must be taken to income in full (§ 14-47(2)).

Ordinary loss: set current deductible losses against other ordinary income and then the spouse's income; the uncovered amount carries forward (§ 6-3). Apply carried losses oldest first under § 14-6. Cessation can permit carryback under § 14-7; composition/bankruptcy and historic expired losses need a separate check, not an unlimited-loss promise. The June 2026 amendment to § 14-6 commences **1 January 2027**, so it does not replace the 2025/2026 rule. [Loss provisions](https://lovdata.no/lov/1999-03-26-14/§14-6).

Negative calculated business personal income is separate: it cannot offset wages/pensions outside the business, but can be claimed against later positive calculated personal income of the same business. Failure to use it at the first opportunity loses that amount (§ 12-13). Keep the two loss schedules separately. The small-business exemption below can prevent negative personal-income carryforward if no personal-income statement is filed. [Skatteloven § 12-13](https://lovdata.no/lov/1999-03-26-14/§12-13).

### VAT, patterns and working paper

For a registered seller, reconcile sales excluding output MVA; recovered input MVA is not a second income-tax cost. Unrecoverable MVA follows the underlying expense/asset, not an automatic deduction. Registration is not decided by calendar-year receipts alone: the ordinary statutory test is taxable turnover/withdrawals **above NOK 50,000 over twelve months**. Verify registration date and invoice rate before extracting MVA. The original 25% fixtures below assume that precise rate; reduced-rate/exemption classification is held for VAT review. [MVA § 2-1](https://lovdata.no/lov/2009-06-19-58/§2-1), [asset cost includes non-recoverable VAT](https://lovdata.no/lov/1999-03-26-14/§14-40).

Bank patterns remain clues: customer/FAKTURA/HONORAR and platform payouts require gross-sales reconciliation; LØNN is checked to wage statements; rent, interest/dividends and NAV transfers require category evidence. Premises, cover, accountant/legal bills, supplies, ads, courses/dues, software, post and bank/platform fees follow the expense/asset tests. Fuel, parking, meals and capital purchases use their specific branches. Own-account transfers, loan principal, drawings, VAT settlements and tax payments are separately reconciled. No untested bank-format promise remains: inspect the actual DNB, Nordea, SpareBank 1, Handelsbanken, Sbanken, Revolut or Wise fields and signs. Innbetaling/utbetaling/overføring identify direction only; AvtaleGiro/kort/gebyr/nettgiro do not prove business purpose.

The working paper keeps: net sales; supported operating costs and depreciation; profit; ordinary-income deductions and losses; personfradrag/northern/trial deductions; the capital/shield/negative-personal-income bridge; combined wages/business personal income; the three tax components; credited payments; estimated balance; and every unresolved input. Reconcile each total to documents and the return. Mark the output **estimated, not reviewed**.

## Deadlines and filing

| Step | Rule and condition | Official source |
| --- | --- | --- |
| Return | ENK owners: end of May after the income year, ordinarily 31 May; other persons end of April. Spouses with different deadlines can use the later deadline. Weekend deadline application follows the statutory time-computation rule, not a guess from an invoice date. Thus 2025 ENK filing is 1 June 2026 (31 May is Sunday); 2026 ENK filing is 31 May 2027. | Skatteforvaltningsforskriften § 8-2-3: https://lovdata.no/forskrift/2016-11-23-1360/§8-2-3 ; skatteforvaltningsloven § 5-5: https://lovdata.no/lov/2016-05-27-14/§5-5 ; domstolloven § 149: https://lovdata.no/lov/1915-08-13-5/§149 |
| Extension | Apply before the deadline. Statutory special-difficulty or accountant/auditor named-client conditions apply; individual extension no later than 30 June. A general extension requires the Directorate's decision. | https://lovdata.no/forskrift/2016-11-23-1360/§8-2-5 ; https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/ |
| Advance tax | Normally four equal terms: 15 March, 15 June, 15 September, 15 December of the income year; earliest three weeks after notice. Under NOK 2,000: 15 June. If issued late, allocate to remaining terms under § 10-20(1); a special uneven-income schedule requires the authority's determination. A missed term accelerates later terms. Payment weekends/holidays move to the next working day. Acceleration does not change the original due dates used to calculate interest (§ 11-1(3)). | Skattebetalingsloven §§ 10-1, 10-2, 10-20: https://lovdata.no/lov/2005-06-17-67/§10-20 |
| Residual tax | Three weeks after dispatch of assessment, no earlier than 20 August. At least NOK 1,000: two equal terms, second five weeks after the first. Follow the notice, including payment despite a correction/appeal. | https://lovdata.no/lov/2005-06-17-67/§10-21 |
| Additional advance | Payment by 31 May of the assessment year avoids residual-tax interest on that paid amount; weekend/holiday payment-date adjustment applies. The date for the 2025 income-year balance is 1 June 2026, not an invented 2025/26 tax period. | https://lovdata.no/lov/2005-06-17-67/§11-5 ; https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/forskuddsskatt/tilleggsforskudd/ |

RF-1175 is no longer the current return attachment (out of use from income year 2023). Use the personal skattemelding and business information/næringsspesifikasjon. Current workflow: log in on skatteetaten.no or begin in supported accounting/year-end software; accounting/audit-duty ENKs must use such software for the specification. If absent, search **næring**, choose **Inntekter, kostnader, eiendeler og gjeld i næring**, then **Gå til næringsspesifikasjon**. Enter/reconcile income, costs, assets, tax adjustments and personal-income/loss schedules; debt linked to the owner personally stays in the personal return. Check for duplicated personal/business entries, check the personal return, submit and retain the receipt. No-activity/new/closed ENKs still submit. The eventual **2026 return's final screen/form is not certified here**: confirm it when released. [Skatteetaten ENK instructions](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/), [retired RF-1175](https://www.skatteetaten.no/skjema/naringsoppgave-1/).

**Small-business distinction:** § 8-2-1 provides an exemption from the specification for operating income **not exceeding NOK 50,000**, not exemption from the return or tax. It excludes companies under § 2-2(1)/(2); § 2-3, § 14-81/82 taxpayers; spouse-split income; multiple businesses or taxable municipalities; taxi/goods-transport reporters; the combined letting/depreciation-report case; accounting-duty persons; VAT-registration-liable persons; and Svalbard taxpayers. Documentation/retention remain mandatory. If no personal-income statement is filed under this exemption, personal income equals business income and negative calculated personal income cannot carry forward. The website's simplified specification is a practical filing route, not a different legal threshold. [Full exemption and exclusions](https://lovdata.no/forskrift/2016-11-23-1360/§8-2-1).

Register/update estimated profit in the tax deduction card and reconcile other income/withholding. Do not assume the first-year advance is zero or treat an estimate change as invoice cancellation. The current authority sends advance invoices through eFaktura or the Altinn inbox; it is not a reason to describe Altinn as the current tax-return filing form. [Advance-tax instructions](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/forskuddsskatt/forskuddsskatt-for-enkeltpersonforetak/).

Check the assessment against all three taxes and actual credits. The normal self-correction window is the last three income years; open the right year, correct business/personal entries together and submit again. Older years or an authority decision need the appropriate change/appeal route. [Return/correction instructions](https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/).

Keep primary records under bokføringsloven § 13(1) nos. 1–4 for **five years** after year end, and secondary nos. 5–8 for **three years six months**; ordered, secured, readable and printable throughout. Originally electronic booked information is electronically available for three years six months under § 13 b, subject to the applicable exception; this is not a blanket digital-only-storage rule. Apply any longer specific retention requirement. The June 2026 amendment starts **1 January 2027**. [Bokføringsloven §§ 13, 13 b](https://lovdata.no/lov/2004-11-19-73/§13).

## Penalties and interest

| Item | Rule | Source |
| --- | --- | --- |
| Tvangsmulkt | A conditional enforcement measure for missing/obviously defective mandatory information, not an automatic flat late-return fee. Notice identifies commencement, deadline and amount. Ordinary chapter 7/8 rate: half a court fee/day; statutory cap 50 court fees. Special circumstances can lower the rate or raise it to at most three court fees/day. Do not choose the court-fee year from the income year alone. | Skatteforvaltningsloven §§ 14-1, 14-2: https://lovdata.no/lov/2016-05-27-14/§14-1 ; forskrift § 14-1-1: https://lovdata.no/forskrift/2016-11-23-1360/§14-1-1 |
| Tilleggsskatt | Wrong/incomplete or omitted mandatory information that can produce a tax advantage: normally 20% of that advantage; 10% where the same information was given by the specified chapter 7 third party or § 8-9 company. It is not a separate ordinary-negligence rate ladder. | https://lovdata.no/lov/2016-05-27-14/§14-3 |
| Exceptions | Excusable circumstances; correct/complete prefilled data; obvious arithmetic/writing mistakes; the specific seller-VAT exception; qualifying voluntary correction not prompted by control/third-party data; additional tax under NOK 1,000 for each matter; death. Timing errors use net deferral advantage. Imposed enforcement fine offsets additional tax for the same failure to file. | §§ 14-3 to 14-5: https://lovdata.no/lov/2016-05-27-14/§14-4 |
| Aggravated additional tax | Intent or gross negligence plus the statutory awareness condition: another 20% or 40% of evaded tax, only in addition to ordinary additional tax; § 14-4 exceptions still apply. Authority-specific penalty, prosecution/prison and appeal calculations are non-usable here. Check this point with one of our partner accountants. | § 14-6: https://lovdata.no/lov/2016-05-27-14/§14-6 |
| Late-payment interest | Runs separately on overdue tax from due date to payment, at the applicable half-year rate. Do not apply a historical rate to a forecast. The old 2025/2026 half-year percentages and specific kroner fine outcomes are not authorized calculations here; confirm the notice period/rate. Check this point with one of our partner accountants. | https://lovdata.no/lov/2005-06-17-67/§11-1 |
| Residual-tax interest | From 1 July in the income year to first residual-tax term; the § 11-6(2) policy-rate basis is reduced by 22% (multiplication by 0.78, not subtraction of 22 percentage points). No final percentage supplied without the relevant year's basis. Payment by the additional-advance deadline avoids interest on the paid amount. | https://lovdata.no/lov/2005-06-17-67/§11-5 |

## Cross-border points

Residence/exit day tests, dual/part-year residence, foreign-source income/PE, foreign tax credit/treaty allocation, foreign-currency conversion and foreign platform sourcing have **no usable final outcome here**. Keep residence dates, countries, currencies and tax paid. Check this point with one of our partner accountants. Route residence to `no-individual-residence`, share income to `no-capital-gains`, companies to `no-corporate-income-tax`, and insurance detail to `no-social-contributions`; a sibling's existence is not proof of its figures.

**Other retained topic holds:** pension tax credit/low-income tax limitation, wealth tax/asset valuations/debt discounts, parental childcare deductions/frikort, PAYE/non-resident/EEA relief, cessation/carryback/insolvency special outcomes, trade-dues limits, tax-dispute costs, personal insurance, mixed-purpose travel, home sale and accounting-treated home offices require their own operative eligibility proof before any outcome is used. Check this point with one of our partner accountants. The ordinary ENK method above remains usable for confirmed domestic facts; these holds cannot be treated as zero liabilities or automatic exemptions.

## Two worked examples that recompute

These are invented fixtures. Each assumes a full-year resident who turns 17 to 69 in the income year, outside the Finnmark area, class 1, municipal and county rates at the maximum, confirmed Norwegian national-insurance membership, no special regime and a confirmed profile. Each covers a client type in the base's slot 13. Results are estimated, not reviewed.

### Example 1: self-employed consultant, 2025

Income year 2025. An enkeltpersonforetak with a mean skjermingsgrunnlag of NOK 200,000 has næringsinntekt of NOK 660,000, no wages, no capital items and no losses. Forskuddsskatt paid was NOK 190,000 on Skatteetaten's statement. The client takes the maximum 2025 skjermingsrente of 4.6%.

```oa-check
name: NO 2025 self-employed, both bases, balance
inputs:
  naeringsinntekt: 660000
  shield_basis: 200000
  shield_rate: 0.046
  personfradrag: 108550
  forskuddsskatt: 190000
steps:
  - shield: max(shield_basis, 0) * shield_rate
  - personinntekt: naeringsinntekt - shield
  - general_tax: max(naeringsinntekt - personfradrag, 0) * 0.22
  - trinn_1: max(min(personinntekt, 306050) - 217400, 0) * 0.017
  - trinn_2: max(min(personinntekt, 697150) - 306050, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygd_rate: personinntekt * 0.109
  - trygd_cap: max(personinntekt - 99650, 0) * 0.25
  - trygdeavgift: min(trygd_rate, trygd_cap)
  - total: general_tax + trinnskatt + trygdeavgift
  - balance: total - forskuddsskatt
  - illustrative_whole_krone: floor(balance)
expected:
  shield: 9200
  personinntekt: 650800
  general_tax: 121319
  trinnskatt: 15297.05
  trygdeavgift: 70937.20
  total: 207553.25
  balance: 17553.25
  illustrative_whole_krone: 17553
```

The 22% is on NOK 551,450, which is næringsinntekt less personfradrag. Trinnskatt and trygdeavgift are on NOK 650,800, which is næringsinntekt less the shield. Neither number replaces the other. The unrounded working-paper balance is NOK 17,553.25, or an illustrative NOK 17,553 if rounded down (illustrative rounding only; reconcile to the notice). Paying it as tilleggsforskudd by 31 May 2026 or, as that was a Sunday, the first working day after avoids rentetillegg.

**Decision: deduct or depreciate.** Same client. Suppose the NOK 660,000 is before an office machine bought for NOK 25,000 with a 5 year life, and taken into use in the business in 2025. It is below NOK 30,000, so the client may deduct it or put it in group a. This is the client's election and the fixture does not make it.

```oa-check
name: NO 2025 under NOK 30,000 asset, deduct versus depreciate
inputs:
  profit_before_asset: 660000
  cost: 25000
  group_rate: 0.30
  shield_rate: 0.046
  base_shield: 9200
  personfradrag: 108550
steps:
  - profit_deduct: profit_before_asset - cost
  - person_deduct: profit_deduct - base_shield
  - tax_deduct: max(profit_deduct - personfradrag, 0) * 0.22 + (306050 - 217400) * 0.017 + (person_deduct - 306050) * 0.04 + person_deduct * 0.109
  - depreciation: cost * group_rate
  - closing_balance: cost - depreciation
  - extra_shield: closing_balance / 2 * shield_rate
  - profit_pool: profit_before_asset - depreciation
  - person_pool: profit_pool - base_shield - extra_shield
  - tax_pool: max(profit_pool - personfradrag, 0) * 0.22 + (306050 - 217400) * 0.017 + (person_pool - 306050) * 0.04 + person_pool * 0.109
  - first_year_gap: tax_pool - tax_deduct
expected:
  tax_deduct: 198328.25
  depreciation: 7500
  closing_balance: 17500
  extra_shield: 402.50
  tax_pool: 204725.78
  first_year_gap: 6397.53
```

The direct deduction costs NOK 198,328.25 of tax for 2025 against NOK 204,725.78 with the pool, so it is NOK 6,397.53 cheaper in year 1. The pool keeps NOK 17,500 for later years and adds a small shield, so the gap is mainly timing. The pool's extra shield rests on Skatte-ABC 2025 E-5-6.2.3, which keeps a pooled smaller asset in the basis. It assumes the machine really was taken into use in the business in 2025, because the asset must have worked there (skatteloven § 12-12(2) and Skatte-ABC 2025 E-5-6.2.10). A machine only delivered and put on saldo adds no shield. The figure also assumes the opening balance was 0 and uses the simple mean. The prior version's 18,000 and 25,000 laptop examples treated these assets as mandatory saldo items, which was wrong under the NOK 30,000 threshold.

### Example 2: wages and a sole trader, 2026

Income year 2026. A client has wages of NOK 400,000 and næringsinntekt of NOK 300,000. Beregnet personinntekt is NOK 300,000: the business has no assets or debt, so there is no shield, and the held 2026 skjermingsrente does not matter. The client was not drawn for the trial deduction. Forskuddstrekk on the wage certificate was NOK 100,000, and forskuddsskatt paid was NOK 70,000.

```oa-check
name: NO 2026 mixed wage and business income
inputs:
  wages: 400000
  business: 300000
  personfradrag: 114540
  forskuddstrekk: 100000
  forskuddsskatt: 70000
steps:
  - minstefradrag: min(wages * 0.46, 95700)
  - ordinary_income: wages - minstefradrag + business
  - general_tax: max(ordinary_income - personfradrag, 0) * 0.22
  - personinntekt: wages + business
  - trinn_1: max(min(personinntekt, 318300) - 226100, 0) * 0.017
  - trinn_2: max(min(personinntekt, 725050) - 318300, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygd_rate: wages * 0.076 + business * 0.108
  - trygd_cap: max(personinntekt - 99650, 0) * 0.25
  - trygdeavgift: min(trygd_rate, trygd_cap)
  - total: general_tax + trinnskatt + trygdeavgift
  - balance: total - forskuddstrekk - forskuddsskatt
  - illustrative_whole_krone: floor(balance)
expected:
  minstefradrag: 95700
  ordinary_income: 604300
  general_tax: 107747.20
  trinnskatt: 16835.40
  trygdeavgift: 62800
  total: 187382.60
  balance: 17382.60
  illustrative_whole_krone: 17382
```

Minstefradrag is on the wages only. Trinnskatt is on all NOK 700,000 of personinntekt in one schedule, whilst trygdeavgift keeps each income type at its own rate. The unrounded working-paper balance is NOK 17,382.60, or an illustrative NOK 17,382 if rounded down (illustrative rounding only; reconcile to the notice).

### Example 3: employee only, 2025

Income year 2025. An employee with wages of NOK 600,000 and no business, with forskuddstrekk of NOK 150,000 on the certificate.

```oa-check
name: NO 2025 employee only, refund
inputs:
  wages: 600000
  personfradrag: 108550
  forskuddstrekk: 150000
steps:
  - minstefradrag: min(wages * 0.46, 92000)
  - general_tax: max(wages - minstefradrag - personfradrag, 0) * 0.22
  - trinn_1: max(min(wages, 306050) - 217400, 0) * 0.017
  - trinn_2: max(min(wages, 697150) - 306050, 0) * 0.04
  - trinnskatt: trinn_1 + trinn_2
  - trygdeavgift: min(wages * 0.077, max(wages - 99650, 0) * 0.25)
  - total: general_tax + trinnskatt + trygdeavgift
  - refund: forskuddstrekk - total
expected:
  minstefradrag: 92000
  general_tax: 87879
  trinnskatt: 13265.05
  trygdeavgift: 46200
  total: 147344.05
  refund: 2655.95
```

### Fixtures and tests

```oa-check
name: NO trygdeavgift floor and cap, and loss in both bases
inputs:
  low_income: 120000
  floor_income: 99650
  mid_income: 200000
  current_year: 400000
  prior_loss: 150000
  prior_negative_personinntekt: 150000
steps:
  - at_floor: min(floor_income * 0.109, max(floor_income - 99650, 0) * 0.25)
  - low_rate_charge: low_income * 0.109
  - low_cap: max(low_income - 99650, 0) * 0.25
  - low_trygd: min(low_rate_charge, low_cap)
  - mid_trygd: min(mid_income * 0.109, max(mid_income - 99650, 0) * 0.25)
  - ordinary_base: max(current_year - prior_loss, 0)
  - personinntekt_no_negative: current_year
  - personinntekt_with_negative: max(current_year - prior_negative_personinntekt, 0)
expected:
  at_floor: 0
  low_trygd: 5087.50
  mid_trygd: 21800
  ordinary_base: 250000
  personinntekt_no_negative: 400000
  personinntekt_with_negative: 250000
```

```oa-check
name: NO gain and loss account at NOK 20,000, and a pooled asset used or unused
inputs:
  gain_balance: 20000
  loss_balance: 20000
  larger_balance: 30000
  limit: 30000
  annual_share: 0.20
  closing_balance: 17500
  shield_rate: 0.046
  used: 1
  unused: 0
steps:
  - gain_under_limit: 1 - min(floor(gain_balance / limit), 1)
  - gain_minimum_income: gain_balance * (gain_under_limit + (1 - gain_under_limit) * annual_share)
  - loss_under_limit: 1 - min(floor(loss_balance / limit), 1)
  - loss_maximum_deduction: loss_balance * (loss_under_limit + (1 - loss_under_limit) * annual_share)
  - loss_without_full_deduction: loss_balance * annual_share
  - larger_under_limit: 1 - min(floor(larger_balance / limit), 1)
  - larger_minimum_income: larger_balance * (larger_under_limit + (1 - larger_under_limit) * annual_share)
  - extra_shield_used: used * closing_balance / 2 * shield_rate
  - extra_shield_unused: unused * closing_balance / 2 * shield_rate
expected:
  gain_minimum_income: 20000
  loss_maximum_deduction: 20000
  loss_without_full_deduction: 4000
  larger_minimum_income: 6000
  extra_shield_used: 402.50
  extra_shield_unused: 0
```

| Fixture | Expected result |
| --- | --- |
| Payment 15/03/2025 ; DNB Innbetaling ; DESIGN STUDIO AS ; Faktura 2025-003 ; +125,000.00 ; NOK | Check the invoice. Registered client, invoice at 25%: driftsinntekt NOK 100,000, MVA NOK 25,000 excluded. Not registered: driftsinntekt NOK 125,000. Invoice not seen: Needs Input |
| Card 22/04/2025 ; SpareBank 1 Kort ; RESTAURANT MAAEMO ; Kundelunsj ; -2,500.00 ; NOK, 4 persons | NOK 625 per person is above NOK 579, so the whole NOK 2,500 is non-deductible. The prior version's NOK 2,236 was wrong. Headcount unknown: no deduction |
| Card 03/06/2025 ; DNB Kort ; ELKJOP ; LAPTOP ; -18,000.00 ; NOK | Under NOK 30,000: deduct NOK 18,000, or if the client chooses, group a at 30%, NOK 5,400 |
| Card 15/05/2025 ; Nordea Kort ; CLAS OHLSON ; KONTORSTOL ; -4,500.00 ; NOK | Driftskostnad, deductible in full if the client does not choose depreciation |
| Client claims minstefradrag of NOK 104,450 on næringsinntekt of NOK 500,000 | Reject. It does not apply to næringsinntekt outside § 6-31(1)(d). The figure is also not the cap for either year |
| Næringsinntekt NOK 600,000, 2025, no shield | Tax on alminnelig NOK 108,119.00 on (600,000 − 108,550) × 22%. Trinnskatt NOK 13,265.05, spanning trinn 1 and 2. Trygdeavgift NOK 65,400.00 at 10.9% |
| Næringsinntekt NOK 1,200,000, 2025, no shield | Trinnskatt NOK 93,769.50, through trinn 4 |
| Næringsinntekt NOK 200,000, 2025 | No trinnskatt. Alminnelig tax and trygdeavgift only |
| Laptop NOK 25,000, client chooses the pool | Group a, 30%, NOK 7,500. Without that choice, deduct NOK 25,000 |
| Gain and loss account, gain balance NOK 20,000 | Under NOK 30,000, so all NOK 20,000 goes to income. At NOK 30,000, at least NOK 6,000 |
| Gain and loss account, loss balance NOK 20,000 | Under NOK 30,000, so the client may deduct all NOK 20,000. Otherwise up to NOK 4,000 |
| Private car, 4,000 km of documented business driving | 2025: NOK 14,000. 2026: Needs Input, with no rate assumed |
| Group a machine delivered and put on saldo in 2025, with a closing balance of NOK 17,500 | Taken into use in the business: extra shield NOK 402.50. Not taken into use: NOK 0 |

### Historical cases retained with their original years and inputs

These fixtures preserve earlier versions' facts; they do not import their old rates. Unless stated otherwise, the tax fixtures assume ordinary covered adults, full-year residence outside the northern zone, class 1 and no shield/other deductions. Unknown facts remain input holds.

| Original case/input | Corrected destination/result |
| --- | --- |
| 2025 gross revenue NOK 800,000, allowable expenses NOK 200,000, no other income/loss | Profit NOK 600,000. Ordinary tax NOK 108,119; bracket tax NOK 13,265.05; insurance NOK 65,400; total NOK 186,784.05. The prior 11.0% contribution and threshold-plus-one arithmetic are rejected. |
| 2025 business personal income NOK 1,200,000, no shield | Bracket tax NOK 93,769.50, including NOK 43,019.20 in step 4. |
| 2025 business profit/personal income NOK 200,000 | Bracket tax zero; ordinary tax NOK 20,119; insurance NOK 21,800. |
| 2025 equipment NOK 30,000, life at least three years | Capitalize at the exact threshold; if ordinary machinery group d, maximum NOK 6,000; if office machine group a, maximum NOK 9,000. Document the type. |
| Registered 2025 receipts NOK 500,000 including 25% MVA | Sales NOK 400,000 and output MVA NOK 100,000, conditional on registration/invoice evidence. |
| 2025 living-room work area, client claims 30% housing costs | Dual-use room: neither actual office deduction nor standard fallback. |
| 2025 previous ordinary loss NOK 100,000, current profit NOK 200,000 | Ordinary income before personal allowance NOK 100,000. A prior negative personal-income amount is a separate input; ordinary loss alone does not reduce business personal income. |
| 2025 expected annual advance tax NOK 200,000 | Normally four NOK 50,000 terms, subject to actual notice, timing and weekend rules; missed terms do not simply turn into restskatt and erase arrears/interest. |
| 2025 gross revenue NOK 80,000, client claims RF-1175 exemption | Above the NOK 50,000 specification threshold; use the current specification, not retired RF-1175. |
| 2025 consultant pays NOK 50,000 for a new law degree | No deduction authorized for this new-profession fixture. |
| Historical claim of 7.9% insurance on ENK profit | Reject; use the applicable year's confirmed category/rate, 10.9% ordinary ENK for 2025 and 10.8% for 2026. |
| 2026 employee wages NOK 700,000 | Minstefradrag NOK 95,700; ordinary tax NOK 107,747.20; bracket tax NOK 16,835.40; insurance NOK 53,200; total NOK 177,782.60. |
| 2026 ENK profit NOK 450,000 plus wages NOK 60,000, zero shield | Wage deduction NOK 27,600; ordinary tax NOK 80,929.20; bracket tax NOK 9,235.40; insurance NOK 53,160; total NOK 143,324.60. |
| 2026 ENK profit/personal income NOK 600,000, zero shield | Ordinary tax NOK 106,801.20; bracket tax NOK 12,835.40; insurance NOK 64,800; total NOK 184,436.60. |
| 2026 wages NOK 60,000 plus business personal income/profit NOK 60,000 | Wage deduction NOK 27,600; ordinary and bracket taxes zero; category insurance NOK 11,040, capped once to NOK 5,087.50. |
| 2026 machine NOK 30,000 with three-year life, group d | Maximum depreciation NOK 6,000, no immediate full-expense default. |
| Selected 2026 trial participant, business profit/personal income NOK 400,000, zero shield, no other deductions | Tentative work deduction NOK 103,000; ordinary tax NOK 40,141.20, subject to verified selection and statutory caps. No bracket/insurance-base reduction. |
| Historical EK cost NOK 3,000 with private use | Private addition NOK 3,000; net deduction zero. |
| 2026 otherwise qualifying restaurant meal NOK 600/person | Above NOK 592, so whole meal deduction zero. |
| 2026 older class-two van, business need, list price NOK 400,000, age over three years at 1 January; alternative 2,000 electronically recorded private km | Inputs retained. **No usable benefit/method-election outcome here** until year-specific valuation and ENK cost-cap conditions are proven. Check this point with one of our partner accountants. |

## Ask the client first

Read the documents first; ask only unresolved facts in one message. Confirm legal form, income year, residence/municipality, age and insurance; special regimes/spouse/foreign facts; business accounts/stock/assets/debt and VAT dates/invoices; wages/benefits/other income; both carried-loss schedules; office exclusivity/ownership/letting, vehicle/logbook, phone private use, meal attendees and business purpose; capitalisation elections and opening/closing shield values; actual work-deduction selection; and payment evidence.

Before handoff, reconcile both income bases, all three taxes, credits and every retained case to the chosen year's source. Test all scope/input holds, document alternatives and keep unresolved outcomes non-usable. No amount threshold suppresses a question that changes treatment.

## Sources

Read on **2026-11-27**, only the operative sections stated below and the linked guidance passages used above. Lovdata full-document table-of-contents responses alone were not counted as reads: section-specific pages were opened to read the actual paragraphs and neighbouring conditions. Official text was read in memory; no source-capture files were saved while backup storage was offline.

| Source/read scope | Official URL | Date read |
| --- | --- | --- |
| 2025 tax decision §§ 3-1, 3-2, 3-8, 6-1, 6-3: bands, ordinary components and allowances | https://lovdata.no/dokument/STV/forskrift/2024-12-13-3203 | 2026-11-27 |
| 2026 tax decision same sections plus § 6-6 trial amount | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | 2026-11-27 |
| 2025 and 2026 folketrygd decisions §§ 6–8: category rates | https://lovdata.no/dokument/LTI/forskrift/2024-12-13-3204 https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 | 2026-11-27 |
| Folketrygdloven § 23-3: categories, age, threshold and phase-in | https://lovdata.no/lov/1997-02-28-19/§23-3 | 2026-11-27 |
| Skatteloven §§ 6-1/3, 6-30/32, 6-51, 6-86, 12-10/13, 14-1/7, 14-40/47, 15-4/5: deduction, base, shield, loss and depreciation conditions | https://lovdata.no/lov/1999-03-26-14/§12-11 https://lovdata.no/lov/1999-03-26-14/§14-40 | 2026-11-27 |
| FSFIN § 12-12-10 and authority ENK shielding page: election and 2025 rate; no 2026 rate asserted | https://lovdata.no/forskrift/1999-11-19-1158/§12-12-10 https://www.skatteetaten.no/satser/skjermingsrente-for-aksjer-og-enkeltpersonforetak/ | 2026-11-27 |
| Skatte-ABC 2025 E-5-6.2: pooled small assets and actual use | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.054/E-5.056/ | 2026-11-27 |
| FSSD §§ 6-21-2 to 6-21-6; annual satsforskrift § 10: hospitality/gift/attention conditions and year limits | https://lovdata.no/forskrift/1999-11-22-1160/§6-21-2 https://lovdata.no/dokument/SF/forskrift/2024-11-27-2889 https://lovdata.no/dokument/SF/forskrift/2025-11-07-2216 | 2026-11-27 |
| 2025 takseringsregler §§ 1-3-20, 1-3-26; home-office standard/eligibility/allocation guidance; annual 2026 amount is authority guidance, no final 2026 valuation regulation asserted | https://lovdata.no/dokument/SF/forskrift/2025-12-01-2404 https://www.skatteetaten.no/satser/hjemmekontor-standardfradrag/ https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/bruke-egen-bolig-i-naring/ | 2026-11-27 |
| ENK EK, education and ordinary mixed-car classification guidance | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/telefon-og-internett/ https://www.skatteetaten.no/nn/person/skatt/hjelp-til-rett-skatt/arbeid-trygd-og-pensjon/utdanning/fradrag-for-kostnader-til-utdanning/ https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/2025/b-5-bil--fradrag-for-bilkostnader/B-5.007/B-5.010/ | 2026-11-27 |
| Skatteforvaltningsforskriften §§ 8-2-1/8, 14-1-1; administration law §§ 5-5, 14-1/6; domstolloven § 149 | https://lovdata.no/forskrift/2016-11-23-1360/§8-2-1 https://lovdata.no/lov/2016-05-27-14/§14-1 https://lovdata.no/lov/1915-08-13-5/§149 | 2026-11-27 |
| Payment law §§ 10-1/2, 10-20/21, 11-1, 11-5/6 and official ENK filing/advance instructions | https://lovdata.no/lov/2005-06-17-67/§10-20 https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/enk/ https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/forskuddsskatt/forskuddsskatt-for-enkeltpersonforetak/ | 2026-11-27 |
| Bookkeeping law §§ 13, 13 b: retention/electronic availability and future commencement | https://lovdata.no/lov/2004-11-19-73/§13 | 2026-11-27 |

Not yet confirmed: the published 2026 ENK shielding rate; final 2026 valuation/deduction rates and return layout; the specifically held expense, vehicle, penalty/interest-notice, rounding, residence/currency, special-regime and historical personal-tax outcomes named above. **These are non-usable holds, not open factual assertions:** Check this point with one of our partner accountants. Original case years/inputs are retained; no 2025/2026 substitution is permitted.
