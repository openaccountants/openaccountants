---
name: es-social-contributions
description: Use this Guide to calculate Spanish social-security contributions for ordinary self-employed RETA workers and employers in the Régimen General in 2026. It covers annual computable income, the calendar-day monthly average, contribution bands, chosen and final bases, generic deductions, company and family floors, coverage rates, starting-fee conditions, bonuses, annual regularisation and pluriactividad refunds. For payroll it covers assessable remuneration, extra-pay proration, overtime, contribution groups, employer and employee shares, occupational tariffs, capped bases, MEI and solidarity, plus household salary bands and agricultural monthly, daily and inactivity methods. Trigger phrases include cuota de autónomos, RETA, cotización, TGSS, regularización, tarifa plana, Seguridad Social, RLC and payroll contributions. Obtain the actual registration, base, coverage and assessment records when reconciling an individual charge; the labelled public starting-fee worksheet also supplies a prospective administrative calculation.
version: 2.4
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-28
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish social contributions: RETA and employer payroll v2.4

Compute 2026 contributions from the worker's status, assessable income, contribution base and coverage. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off. Amounts below are euros.

## Who this applies to

This Guide covers ordinary self-employed workers in RETA and employers/employees in the Régimen General. Determine the correct inclusion under [LGSS arts. 136 and 305](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a305) before calculating: a shareholder/director is not automatically an ordinary employee. Identify an individual business, a working shareholder/director within art. 305.2.b/e, or a collaborating relative within letter k. Their income definitions, generic deduction and minimum-base rules differ.

Social security is state-wide, including the foral territories. Use the relevant tax administration's income information for RETA regularisation; a different income-tax administration does not exclude the worker from these contribution rules ([LGSS art. 308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)). First establish the applicable state for an international worker under the cross-border section.

Income tax, payroll withholding and quarterly tax instalments are separate computations in [es-income-tax](es-income-tax.md), [spain-payroll](spain-payroll.md) and [es-estimated-tax](es-estimated-tax.md). Household employees and agricultural employees use the dedicated methods below. Sea workers, self-employed agriculture, artists, training contracts and other special systems require their own applicable base rules; do not apply the ordinary full-time table to them. The ordinary rates and bases below apply from **1 January 2026** under [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296).

## Rates, bands and thresholds

### Debt-interest rate

| Item | Annual rate | Verified year | Official source |
|---|---:|---|---|
| Legal-money rate | 3.25% |2026,current authority read27October |[AEAT2026confirmation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html) |
| Social Security default interest | 4.0625%,calculated as3.25%×1.25 |2026,current authority read27October |[LGSS31.3](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a31),[AEAT2026rate](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html) |

Apply the rate only to principal/surcharge and accrual periods for which the debt-interest rules below actually require interest. It is not a flat penalty on every late payment.

### RETA income bands and chosen monthly bases

Every row below is for **2026** under [order art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10). Income is the statutory monthly average calculated in the next section, not turnover or the bank debit. The reduced table ends **below** 1,166.70; that exact amount starts general band 1.

| Table/band | Monthly computable income | Minimum base | Maximum base | Official source |
|---|---:|---:|---:|---|
| Reduced 1 | ≤670 | 653.59 | 718.94 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Reduced 2 | >670 to 900 | 718.95 | 900.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Reduced 3 | >900 and <1,166.70 | 849.67 | 1,166.70 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 1 | ≥1,166.70 to 1,300 | 950.98 | 1,300.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 2 | >1,300 to 1,500 | 960.78 | 1,500.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 3 | >1,500 to 1,700 | 960.78 | 1,700.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 4 | >1,700 to 1,850 | 1,143.79 | 1,850.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 5 | >1,850 to 2,030 | 1,209.15 | 2,030.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 6 | >2,030 to 2,330 | 1,274.51 | 2,330.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 7 | >2,330 to 2,760 | 1,356.21 | 2,760.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 8 | >2,760 to 3,190 | 1,437.91 | 3,190.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 9 | >3,190 to 3,620 | 1,519.61 | 3,620.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 10 | >3,620 to 4,050 | 1,601.31 | 4,050.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 11 | >4,050 to 6,000 | 1,732.03 | 5,101.20 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 12 | >6,000 | 1,928.10 | 5,101.20 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |

| RETA item | Amount/rule | Year | Official source |
|---|---|---|---|
| Common contingencies (CC) | 28.30% | 2026 | [Order art. 18.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Occupational contingencies | 1.30%, comprising IT 0.66% and permanent incapacity/death/survivors 0.64% | 2026 | [Art. 18.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Cessation and training | 0.90% and 0.10%; SETA cessation uses 2.20% | 2026 | [Art. 37.5–6](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-9) |
| MEI | 0.90% of CC base, worker pays | 2026 | [Art. 18.2.c](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| IT covered in another regime, no voluntary RETA IT election | Reduce the CC quota by 0.055 × that quota | 2026 | [Art. 18.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| No occupational cover in an eligible exception | Additional 0.10% on chosen base | 2026 | [Art. 18.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Generic income deduction | 7%; 3% for art. 305.2.b/e after 90 days in those categories | Current | [LGSS art. 308.1.c.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308) |
| Company/family floor | Final base at least group 7 minimum 1,424.40 once the 90-day test applies; 2025 provisional base can continue during 2026 | 2026 | [LGSS art. 308.1.a.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308), [order art. 18.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Pluriactividad | Refund 50% of total CC above 17,323.68; capped at 50% of RETA CC paid | 2026 | [Order art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |

For ordinary full RETA coverage with the same base for every line, the **derived sum** is `28.30 + 1.30 + 0.90 + 0.10 + 0.90 = 31.50%`. This is arithmetic from the statutory components, before an applicable exception or bonus. The [TGSS summary](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) prints 31.40% while listing those same components. Follow the order. Keep separate component amounts and reconcile rounding with the TGSS assessment.

### Régimen General, ordinary full-time employment

| Contribution group | Minimum CC base | Maximum CC base | Year and source |
|---|---:|---:|---|
| 1, engineers/graduates and senior management | 1,989.30/month | 5,101.20/month | [2026 order art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 2, technical engineers/qualified assistants | 1,649.70/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 3, administrative/workshop heads | 1,435.20/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 4–7 | 1,424.40/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 8–11, daily-paid categories | 47.48/day | 170.04/day | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| Accident/occupational base | Ordinary full-month floor 1,424.50 (= 1,221 × 7/6); ceiling 5,101.20/month | Art. 2 sets SMI plus one-sixth, subject to an absolute minimum of 1,424.40. Apply applicable daily/partial-period rules | [2026 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a2); [2026 SMI art. 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815#a1) |

| Contribution | Employer | Employee | Year and source |
|---|---:|---:|---|
| CC | 23.60% | 4.70% | [2026 art. 4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a4) |
| MEI, CC base | 0.75% | 0.15% | [2026 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-8) |
| Unemployment, indefinite and listed equivalent contracts | 5.50% | 1.55% | [2026 art. 33.2.a.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| Unemployment, other fixed-term contracts | 6.70% | 1.60% | [2026 art. 33.2.a.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| FOGASA | 0.20% | 0 | [2026 art. 33.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| Training | 0.60% | 0.10% | [2026 art. 33.2.c](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| AT/EP | Applicable activity/occupation tariff | 0 | [LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37) |
| Additional overtime, force majeure | 12% of overtime pay | 2% | [2026 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a5) |
| Additional other overtime | 23.60% of overtime pay | 4.70% | [2026 art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a5) |

The lower unemployment rate also applies to the listed training/professional-practice, relief, substitution and surviving interinidad contracts, and any contract with a worker whose recognised disability is at least 33%. A conversion to indefinite uses the lower rate from conversion. The contribution base for unemployment, FOGASA and training is the **AT/EP base** ([art. 33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5)). Do not apply an ordinary percentage to a training contract where the order requires its special quota method.

| Slice of assessable monthly remuneration above ceiling | Employer | Employee | Year and source |
|---|---:|---:|---|
| Above 5,101.20 up to 5,611.32 | 0.96% | 0.19% | [2026 solidarity, order art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |
| Above 5,611.32 up to 7,651.80 | 1.04% | 0.21% | [2026 art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |
| Above 7,651.80 | 1.22% | 0.24% | [2026 art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |

### Earlier-year regularisation

Use the year being regularised. Do not apply 2026 rates to a 2025 base difference.

| Item | 2025 figure | Official source |
|---|---|---|
| Maximum base | 4,909.50/month | [Orden PJC/178/2025, arts. 2/18](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| MEI | 0.80%; employer 0.67%, employee 0.13% | [2025 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| Pluriactividad threshold | 16,672.66 | [2025 art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| Special company/family and no-income-return minimum | 1,000 under the temporary 2023–2025 rule | [RDL 13/2022 DT 7](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) |

The 2025 solidarity slices below are retained **only for 2025 corrections**; apply the positive amount in each band separately and add the employer/employee components. They do not replace the 2026 table.

| 2025 monthly remuneration slice | Employer | Employee | Official source |
|---|---:|---:|---|
| Above 4,909.50 through 5,400.45 | 0.77% | 0.15% | [Order PJC/178/2025 art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780#a1-9) |
| Above 5,400.45 through 7,364.25 | 0.83% | 0.17% | [Art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780#a1-9) |
| Above 7,364.25 | 0.98% | 0.19% | [Art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780#a1-9) |

## The base

### RETA income and choice

1. **Build annual computable income across activities** under [LGSS art. 308.1.c.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308). Direct assessment uses IRPF net income plus the proprietor's social-security and alternative-mutual contributions deducted in reaching it. Modules use rendimiento neto previo, except agriculture/forestry/livestock use rendimiento neto previo minorado. Attributed income uses the specific direct/modules attribution rule in that article; do not add back a cost twice.
2. **Include the statutory shareholder income.** For art. 305.2.b, add gross cash/in-kind equity income from entities in which the worker has at least 33% at corporate-tax accrual, or at least 25% as administrator, plus work income from those entities. Include the article's work/capital income for cooperative working members and art. 305.2.c/d/e partners or co-owners. Do not substitute only dividends or only accounting profit.
3. **Deduct generic expenses:** multiply qualifying aggregate income by 93%, or 97% where the 3%/90-day company category applies ([art. 308.1.c.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)).
4. **Use days, not a presumed number of months.** Let `D` be calendar days of registration subject to regularisation after statutory exclusions. `monthly_income = annual_computable_income_after_generic_deduction / D × 30`. Use actual registration and benefit records to establish D. Do not assume annual/12, or divide by the number of bank debits ([RD 2064/1995 arts. 44.2.a and 46.2.1–2](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44)).
5. Select the band and a provisional base within its limits, with the company/family floor when applicable. Apply every covered contribution component, then a legally applicable bonus. Keep MEI separate: it is not reduced by ordinary contribution bonuses ([LGSS art. 127 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-5)).

**Provisional high bases and special periods.** [Order art. 18.5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) permits the specified unchanged pre-2023 high base, or a lower base, during 2026 despite income implying a lower band. The separate regularisation election in [RD 2064 art. 46.2.6](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46) can preserve eligible provisional bases up to the 31 December 2022 base by renouncing refund by the last day of the month after notification. Distinguish these rules; do not assume every base change destroys that separate election.

Late registration and office registration have the exact nonregularisable periods and general-band-1 minimum in [RD 2064 art. 44.3.c/d](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44), with a possible higher inspection base. Failure to file IRPF, or a direct-assessment return declaring no relevant income, uses the group 7 minimum under art. 44.3.e. Exclude the statutory reduced-fee periods and benefit-related bases/periods from regularisation as directed in art. 46.1–2. Do not treat every sickness day as an independently regularisable month.

### Annual regularisation

Follow [RD 2064 art. 46.2](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46):

- Calculate D and monthly income as above. Calculate `average_provisional_base = (sum of provisional monthly bases − bases attributable to excluded days) / D × 30`, using proportionate exclusions from the TGSS record.
- If this average is within the applicable minimum/maximum, provisional bases become final. If below, the final base is the band minimum; if above, it is the maximum, subject to the historical-base election.
- For an adjustment, retain the **signed difference for each month** between final and provisional base. Prorate band limits for partial registration months. Apply that month's rates, benefits and other contribution data, then net the differences. Do not calculate every full-year case as twelve identical debits or discard negative monthly differences.
- A net amount due is payable by the last day of the month following notice, without surcharge/interest if paid by then. A refund is automatic, without interest, before 30 April of the year following the tax administration's income communication. Existing unpaid provisional debts and their surcharges/interest are not erased ([LGSS art. 308.1.c.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)).

For **pluriactividad**, include employer **and** employee CC from employment plus RETA CC. `refund = min(0.50 × max(total_CC − 17,323.68, 0), 0.50 × RETA_CC_paid)`. TGSS pays within four months after regularisation, subject to the statutory data/special-case exceptions ([LGSS art. 313](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a313); [order art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10)). This is not a refund of every type of contribution.

### Reduced starting fee and family/territorial bonuses

[Ley 20/2007 art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a3-5) allows the starting reduction for first registration or no RETA registration in the preceding two years; use three years if the previous registration enjoyed it. Request it at registration. It runs from the effective registration date through the next twelve complete calendar months, with no cessation/training contribution during it. A further twelve complete months requires expected annual computable income **below** annual SMI, an application before that period starts, and the condition in each year if it spans two. The first period is not regularised; the extension is tested under art. 38 ter.6. Disability ≥33%, gender-violence and terrorism cases use 24 and 36 complete months instead. The article excludes joining relatives through the second degree and the specified religious members, but expressly includes qualifying company/cooperative members.

**Equality with SMI: published TGSS assessment.** The [current TGSS system guide, “Prórroga Tarifa Plana”](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24/44b5f09d-6c25-4dcd-8210-c21700c67096?changeLanguage=es), expressly says that annual net income **equal to or above** SMI leads TGSS to reclaim contributions not paid because of the extended benefit and to treat that extension period as regularisable, recalculating the provisional base and quota as applicable. Current [RD 2064 art. 44.3.f](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44) likewise sends equal-or-higher income to the ordinary base rules. Do not model equality as an automatically retained extension. This does not regularise the unconditional initial period.

Test each calendar year of the extension separately. If an extension spans two calendar years and has annual net income below the first year's SMI but exactly equal to the second year's SMI, the published TGSS route reassesses only the affected extension months in the second year. It does not remove the first year's qualifying reduction. Apply art. 38 ter.6's proportional-income rule for the affected months and the regularisation method above, using actual bases, coverage and notice. Reconcile against reduced contributions actually assessed and paid, rather than treating the advertised flat fee as a verified new-2026 award.

**Precise remaining textual issue.** Art. 38 ter.2/3 requires expected income strictly below SMI, and current art. 44.3.f expressly includes equality in its ordinary-base exception. The narrower literal mismatch is the “exceeds” wording for regularisation in art. 38 ter.6 and [RD 2064 art. 46.1](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46), compared with TGSS's explicit equal-or-higher assessment explanation. Treatment of a legal challenge to that literal regularisation wording is not established here. That reservation does not make TGSS's published equality practice unknown.

**Ordinary complete-month fee: published TGSS administrative worksheet.** The [current Importass guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia), read 28 October 2026, contains the 2026 tables and states in its tariff answer that the ordinary fee is 80 plus MEI, with a **total 88.64 per month**. For an independently qualifying ordinary initial-period claimant, use **88.64 × the number of complete covered 2026 calendar months** as the contribution expected under that published administrative representation. The advertised total already includes its stated MEI: do not add another 0.9% charge to 88.64. Applying that current, unqualified answer to new 2026 ordinary registrations is a labelled administrative reading of its current 2026 context, not a conclusion that an 80 extension has been enacted or that a particular person has already received an award. No individual login/registration/assessment is required to demonstrate this published worksheet; actual record reconciliation remains necessary when establishing what a particular person was assessed and paid.

First establish the existing 38 ter gates above: initial registration or the applicable two-/three-year gap, request at registration, qualifying RETA status and no excluded family-collaborator/religious category. Retain the current TGSS conditions of being up to date with tax/Social Security obligations and resolving incompatible incentives. This finite monetary worksheet is for the ordinary initial period with no competing pluriactivity benefit, special 24/36-month route, territorial enhancement, late registration or partial month. The initial period has no annual-SMI income gate and is not annual-income regularised. For a later extension, independently establish the prior application and each year's below-SMI condition, using the supplied equality/above-SMI reassessment method; this initial-period quotation does not guarantee an extension. A published monthly figure is not evidence that an unrequested or ineligible reduction has been granted ([LETA 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a38ter); [TGSS tariff conditions](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia)).

**Positive separator and reconciliation.** A hypothetical ordinary sole-trader first registers effectively 1 July 2026, requests the reduction at registration, is current on tax/Social Security obligations and meets all the stated ordinary conditions, with no competing incentive or special case. For the three complete initial-period months July–September 2026, the published administrative worksheet gives `3 × 88.64 = 265.92`. This result remains 265.92 if the independently established annual computable income is above SMI, because the initial period is unconditional on that income test. Without a valid reduction request/entitlement, use the ordinary contribution method and actual applicable base/coverage; do not return zero or automatically charge the advertised reduced total. The 265.92 is the **published-route expected contribution**, not an asserted individual settlement, proof of payment or a new universally reconciled statutory amount.

**Countertext retained alongside the positive method.** LETA 38 ter.1 delegates the annual amount to PGE; RDL 13/2022 DT 5 expressly fixes 80 for 2023–2025 and remits 2026 onward to PGE. Budget prorogation and RDL 3/2026 art 3.4's express **table** rollover do not themselves expressly print a general new 2026 tariff amount in the provisions examined. The separate TGSS system explanation still expressly describes 80 for 2023–2025. Fresh targeted 2026 RED instructions repeat the table/MEI provisions without supplying that monetary bridge in the selected passages; they are not evidence of an enacted 80 extension ([DT 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482#dt-5); [RDL 3/2026 art 3/DA 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548#a3); [Budget Law 38](https://www.boe.es/buscar/act.php?id=BOE-A-2003-21614#a38); [TGSS system explanation](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24/44b5f09d-6c25-4dcd-8210-c21700c67096?changeLanguage=es); [BNR 02/2026 art 3](https://www.seg-social.es/descarga/es/BNR%2002_2026); [BNR 05/2026](https://www.seg-social.es/wps/wcm/connect/wss/61f4db39-8366-4d8f-863b-34332b1d527a/BNR%2B5_2026.pdf?MOD=AJPERES)).

The monetary arithmetic is also genuinely inconsistent: RD 2064 art 44.3(f) selects the first general-band minimum, and the 2026 order gives 950.98 and 0.90% MEI. `950.98 × 0.009 = 8.55882`; an explicitly diagnostic nearest-cent calculation gives 8.56, so a **stipulated**, not independently enacted, 80 component would total 88.56 and 265.68 for three months. That differs by 0.08 per month/0.24 for the example from the published 88.64/265.92. Neither this diagnostic nor truncation derives TGSS's 88.64. The worksheet deliberately uses the authority's **literal advertised total**, not a fabricated base, rounded formula or statutory correction. It does not instruct payment of 88.56 instead of a TGSS assessment. An express general 2026 monetary enactment/prorogation interpretation, authoritative reconciliation of the MEI amount, a contrary/current corrected TGSS tariff and any dispute over the assessed amount remain precise ordinary source questions. Preserve actual dated assessment/payment evidence when available; that factual reconciliation is separate from supplying the public administrative method ([RD 2064 art 44.3(f)](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44); [order 18.1/2(c)](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10); [LGSS 127 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-5)).

The current statutory monetary authority for a **new 2026** reduced fee remains unconfirmed in this pass. [RDL 13/2022 DT 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) fixes the stated amounts for 2023–2025 and refers later years to annual budgets. The [TGSS guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) advertises 80 plus MEI, but its displayed total does not reconcile with its stated base/rate. Use the individual's TGSS award and assessment to document the amount; do not certify a general 2026 amount from this discrepancy. This precise gap does not prevent an ordinary full-rate computation.

The [family-collaborator bonus, art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a35), covers the listed spouse/partner/relatives through second degree who collaborate in the business and were not registered in the preceding five years. It is 50% for eighteen months and 25% for the following six, applied to CC on **general-band-1 minimum**, rather than the whole chosen-base quota. A qualifying unmarried partner requires the article's five-year continuous cohabitation and registry/public-document evidence. Apply the separate final-base floor when relevant.

For **Ceuta/Melilla**, verify residence, activity and the applicable sector list. [Ley 20/2007 art. 36](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a36), amended by [RDL 22/2026 art. 36/DF 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429), changes the CC bonus from 50% to **75% for quotas accrued from 1 October 2026**. The revised list is agriculture/fishing/aquaculture; industry except energy/water; commerce; tourism; hospitality and other services with the specified fixed-wing air/financial-insurance/real-estate exclusions. Use the earlier wording, including its building-construction exclusion, for earlier quotas. Do not reduce other contingencies by this CC-only bonus.

### Employer payroll calculation

Build assessable remuneration under [LGSS art. 147](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a147). Include cash/in-kind pay and remuneration due even if not yet paid, with only the statutory exclusions and limits. Add the prorated annual extra/irregular pay: annual estimate/12 for monthly remuneration, or /365 × days for daily remuneration ([order art. 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1)). Expenses are not excluded merely because the payroll labels them allowances; apply the actual art. 147.2 conditions.

Maintain separate **CC** and **AT/EP** bases. Overtime is excluded from CC but included for occupational protection; its additional contribution is calculated separately without reducing the AT/EP base. Apply the group minimum and ceiling to CC, and the occupational floor/ceiling to AT/EP. Compute CC/MEI on CC; unemployment/FOGASA/training and the employer's AT/EP tariff on AT/EP. Deduct only the employee shares from pay; the employer pays both shares to TGSS ([LGSS art. 147.2.e](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a147); [order arts. 1–5/16/33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)).

Obtain actual **CNAE-2025 and occupation** for the tariff in [LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37). Table II's office rate of 1.50% (IT 0.80%, IMS 0.70%) requires exclusive office work in office premises without exposure to the enterprise's activity risks. A job title alone is insufficient. Do not substitute one assumed office rate for every business. Use the part-time, multiple-employment and suspension base methods below where applicable.

For solidarity, use assessable remuneration under [LGSS art. 19 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-4), rather than cash paid. For a full monthly period, calculate the three slices as `s1 = min(max(R − 5,101.20, 0), 510.12)`, `s2 = min(max(R − 5,611.32, 0), 2,040.48)`, `s3 = max(R − 7,651.80, 0)`. Multiply each by the employer/employee rates above. Daily workers use maximum daily base × contribution days; monthly partial periods use the proportional monthly maximum ([order art. 17.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9)). Solidarity is additional to capped ordinary contributions and does not apply to RETA.

### Part-time, multiple jobs and suspension periods

For ordinary part-time work, [order art. 38](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-10) uses remuneration for ordinary **and complementary** hours, plus the attributable weekly-rest/public-holiday, extra-pay and other annual-pay portions. Build CC and AT/EP separately; do not multiply the full-time monthly minimum by an assumed percentage without testing the statutory hourly floor.

| 2026 part-time group | Minimum CC base per actual hour | Official source |
|---|---:|---|
| 1 | 11.98 | [Order art. 39](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-11) |
| 2 | 9.94 | [Art. 39](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-11) |
| 3 | 8.65 | [Art. 39](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-11) |
| 4–11 | 8.58 | [Art. 39](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-11) |
| AT/EP floor, every group | 8.58 | [Art. 38.3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-10) |

With actual hours H, `CC_base = min(max(assessable_CC_pay, H ×group_hourly_floor), applicable_general_maximum)` and `AT_base = min(max(assessable_AT_pay, H ×8.58), applicable_maximum)`. Force-majeure overtime enters AT/EP and its separate additional contribution, not CC. Apply each employer/employee component to its proper base and test solidarity separately. The same lower unemployment-contract tests apply; part-time status does not by itself require the higher fixed-term rate.

For **multiple employment**, [arts. 10/41](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-2) distribute the overall maximum proportionately across actual employers' pay. The full-time rule also distributes the appropriate minimum (use the highest applicable group minimum for the allocation where categories differ). Use the TGSS allocation and actual concurrent employment evidence; do not give each employer an independent full ceiling when combined pay exceeds it. This is distinct from employment-plus-RETA pluriactividad.

For **full-time IT/risk/care suspensions**, contribution obligations continue. [Art. 6.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a6) uses the preceding month's CC base for IT/pregnancy or lactation risk/co-responsible infant care, and the **month before the preceding month** for birth/childcare leave. For monthly remuneration with the relevant whole reference month, divide the reference base by 30; for daily pay or an incomplete reference month, divide by its contribution days. Multiply the daily result by the applicable suspension days (30 for a full monthly period), using the same-month starter rules where necessary and the current group minimum unless a legal exception applies. Occupational contributions continue at the actual occupation tariff; overtime uses the article's prior-year average. Partial-time birth/childcare combines the benefit base in proportion to leave with actual remunerated working time under art. 6.6. A missing salary payment does not make the contribution base zero.

For **part-time IT/risk/birth/care suspensions**, [art. 40](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a4-2) uses the corresponding daily regulatory benefit base for every calendar suspension day, including the prescribed hypothetical base if no IT/birth subsidy entitlement arose. For ordinary part-time IT, [LGSS art. 248.1.c](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a248) divides the relevant partial-time bases since the last registration, limited to the specified three months before the month preceding the event, by their calendar days. Birth/childcare uses art. 248.1.b's twelve-month reference before the preceding month, sum/365, or the shorter-record/start exceptions. Do not divide by worked hours or apply only working days to the suspended-period contribution.

If the worker remains registered **without remuneration** but the contribution obligation remains, [art. 7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a7) uses the group minimum for CC and the occupational minimum, proportionate to those days, with its stated public-service exceptions.

For **ERTE/reduced hours/suspension**, [art. 9](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a9) uses different worker and employer reference periods. The worker's ordinary unemployment-protected base uses the last six months' contribution average; RED uses the specified 180-day occupational-base average (or shorter proven period). The employer's CC/AT bases use the six calendar months before the month preceding each continuous situation, with registration-day weighting and the specific recent-starter rules; apply the unworked-time proportion for reduced hours. Preserve the continuous-period and reference-base schedule, including prior non-working/suspension contribution periods. Do not reduce the entire employer charge by the salary-reduction percentage or assume an exemption without its award/conditions.

Finally, [art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a2-10) adds **33.62** payable by the employer when a fixed-term contract **shorter than thirty days** ends in 2026. Test the listed agricultural/household/coal/artist, substitution and training exceptions; a short substitution contract is not charged merely because it is fixed-term. Keep this employer-only amount out of the worker's deductions.

### Household employees: salary-band base and complete ordinary quota

Determine each household employment relationship separately. Monthly remuneration includes cash, valued salary in kind and **annual extra pay divided by twelve**. Use that total to select the 2026 base; a bank debit or monthly cash salary excluding extras is not the base ([order art. 15](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7)).

| Monthly remuneration including extra-pay proration | Monthly contribution base | Year | Official source |
|---|---:|---|---|
| ≤329.00 | 306.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 329.01–510.00 | 436.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 510.01–693.00 | 602.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 693.01–877.00 | 785.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 877.01–1,061.00 | 970.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 1,061.01–1,242.00 | 1,151.00 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| 1,242.01–1,424.40 | 1,424.40 | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| ≥1,424.41 | Actual monthly remuneration | 2026 | [Art. 15.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |

Apply the minimum-remuneration **band floor** in art. 15.2 before settling: full-time/160 hours monthly/40 weekly uses the band's base for full SMI plus extras. Monthly-paid part-time work uses proportionate SMI plus extras; genuinely hourly external work uses the all-in statutory hourly minimum times actual monthly hours. If pay basis is unknown, TGSS treats it as monthly unless the employer proves hourly payment. Full-time 2026 SMI with extras is **1,424.50**, so its base falls in the actual-remuneration band; do not lower it to 1,424.40 ([RD 126/2026 arts. 1/3/4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815); [order art. 15.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7)).

| Household component on the band base | Employer | Employee | Year and source |
|---|---:|---:|---|
| CC | 23.60% | 4.70% | [2026 art. 15.3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7) |
| AT/EP, household tariff code 97 | 1.50% (IT 0.80%, IMS 0.70%) | 0 | [2026 LGSS DA 61, code 97](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37) |
| Unemployment, indefinite including fixed-discontinuous | 5.50% | 1.55% | [2026 order art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-7) |
| Unemployment, fixed-term | 6.70% | 1.60% | [2026 art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-7) |
| FOGASA | 0.20% | 0 | [2026 art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-7) |
| MEI | 0.75% | 0.15% | [2026 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-8) |

For registered household employment, [RDL 16/2022 DA 1.1](https://www.boe.es/buscar/act.php?id=BOE-A-2022-14680#da) reduces **employer CC by 20%** and bonuses **employer unemployment/FOGASA by 80%**. Current [TGSS guidance](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Empleo%2Bdel%2Bhogar/guia) requires being current with Social Security and tax debts. Reduce the relevant employer component, never the employee contribution, AT/EP or MEI. A recognised qualifying **45% large-family CC benefit replaces, rather than adds to, the 20%**, while the unemployment/FOGASA bonuses remain; verify the family category, single supported worker and actual TGSS entitlement. The separate DA 1.2 income/wealth-based 30/45% alternative depends on its regulatory implementation and SEPE/TGSS recognition, so it is not an automatic extra discount. For age-62-or-over IT, LGSS art. 144.4's **75% employer-CC reduction** requires that actual IT situation; do not apply it to ordinary working pay or invent cumulative relief ([LGSS art. 144.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a144); [TGSS](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Empleo%2Bdel%2Bhogar/guia)).

With only ordinary 20/80 relief and an indefinite contract, compute `employer = B×23.6%×0.8 + B×1.5% + B×5.5%×0.2 + B×0.2%×0.2 + B×0.75%`. Employee contributions are `B×(4.7%+1.55%+0.15%)`; for fixed-term replace unemployment by 6.7/1.6%. There is no ordinary household training component in art. 35. Keep component rounding and any special period/award separately. The employer pays both shares and withholds the employee share from salary; the former under-60-hours option to shift registration/payment duties to the employee ended **1 January 2023** ([RDL 16/2022 DA 2](https://www.boe.es/buscar/act.php?id=BOE-A-2022-14680#da-2)).

### Agricultural employees: activity, daily work and inactivity

These are **employees in the agricultural special system**, not self-employed SETA workers. Establish the contribution group, actual registered days, jornadas reales, contract and chosen monthly/daily modality. Build each assessable CC/occupational base under LGSS art. 147, with the following 2026 limits ([order art. 14.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6)).

| Group | Monthly minimum / maximum | Jornada real minimum / maximum | Year and official source |
|---|---|---|---|
| 1 | 1,989.30 / 5,101.20 | 86.49 / 221.79 | [2026 art. 14.1.a/b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |
| 2 | 1,649.70 / 5,101.20 | 71.73 / 221.79 | [2026 art. 14.1.a/b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |
| 3 | 1,435.20 / 5,101.20 | 62.40 / 221.79 | [2026 art. 14.1.a/b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |
| 4–11 | 1,424.40 / 5,101.20 | 61.93 / 221.79 | [2026 art. 14.1.a/b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |

Monthly mode is compulsory for indefinite contracts **except fixed-discontinuous**, and optional for other eligible contracts. Communicate and maintain the election for the employment period. LGSS art. 255.2.b makes **monthly mode the default without an express election**. Starts/ends not on month boundaries use the statutory proportional days where the activity lasts at least **30 consecutive calendar days**. Daily mode clamps each real-work day's assessable base to the daily limits and aggregates it; **22 or more real-work days in the calendar month use the monthly base rule**. Do not simply multiply a daily minimum by 30 in monthly mode ([art. 14.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6)).

| Activity component | Employer | Employee | Year and official source |
|---|---:|---:|---|
| CC, group 1, before reduction | 23.60% | 4.70% | [2026 art. 14.3.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |
| CC, groups 2–11, before reduction | 21.20% | 4.70% | [2026 art. 14.3.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |
| Unemployment, fixed employment; qualifying art. 33.2.a.1 temporary/disability categories | 5.50% | 1.55% | [2026 art. 34.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-6) |
| Unemployment, other eventual employment | 6.70% | 1.60% | [2026 art. 34.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-6) |
| FOGASA | 0.10% | 0 | [2026 art. 34.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-6) |
| Training | 0.15% | 0.03% | [2026 art. 34.3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-6) |
| MEI on CC base | 0.75% | 0.15% | [2026 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-8) |
| AT/EP on occupational base | Actual activity/occupation tariff | 0 | [2026 art. 14.3.a/LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6) |

**Employer CC reduction during actual activity.** Group 1's reduction is **8.10 percentage points**, producing **15.50%**, with employer CC capped at **279/month or 12.68 per real-work day**. For groups 2–11, the 2026 order's official formula image expressly uses the **2021 reduction evaluated at the 2026 base**. In percentage-point units define `r21 = 7.36 × (1 + (B−K)/B ×2.52×6.15/7.36)`, where K is **986.70 monthly** or **42.90 daily**. Then `r26 = r21 + (8.10−r21)/10×5`. Calculate `B×(21.20−r26)/100`, then constrain employer CC to **179.44–279.00/month** or **8.16–12.68 per real-work day**, before summing daily amounts. Use proportional reductions for the statutory partial monthly period. The 2021 source supplies the referenced formula only; do not import its rates, old minima or 101.47 floor into 2026 ([2026 art. 14.4 and formula](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6); [PCM/1353/2021 art. 13.4.b](https://www.boe.es/buscar/doc.php?id=BOE-A-2021-20075); [LGSS DT 18](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#dtdecimoctava)).

**Inactivity inside a registration month.** First establish inclusion for inactivity under LGSS art. 253: ordinarily at least **30 real-work days in a continuous 365-day period** and an express application within **three calendar months** after the last qualifying day, effective the first day of the month after application. Apply its exclusion/re-entry and assimilated-day rules to the actual TGSS record. There is **no inactivity** where at least **five real-work days per week for the same employer** fulfil the applicable collective agreement. For an included worker outside that exception, if registered calendar days R exceed real-work days J times **1.3636**, inactive days are `D = R−J×1.3636`; otherwise zero. Use the group-7 monthly minimum **1,424.40/30 =47.48 daily**. The worker alone pays `D×47.48×11.50%`, plus separate **0.90% MEI** on that inactivity base. Where the worker had **at most 55 real-work days in 2025**, reduce the inactivity CC quota by **19.11%** in 2026, leaving MEI unreduced. Do not round away the 1.3636 day adjustment before calculating the assessed base ([arts. 14.2/3.b and 16](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6); [LGSS arts. 253/255](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a253); [LGSS art. 127 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-5)).

For IT, pregnancy/breastfeeding risk, birth/care or shared nursing-infant care arising during activity, the employer CC treatment changes: indefinite workers use **15.50% group 1** or **2.75% groups 2–11** under the general suspension rules; temporary/fixed-discontinuous workers use that route on contracted days they could not work. Unscheduled days use inactivity treatment, except the statutory birth/nursing-benefit deemed-contribution periods. The protected-activity situations also have a **2.75-point unemployment-quota reduction**, separate from CC. Contributory unemployment uses the art. 8 base and **11%** rate under art. 14.6. No additional overtime quota applies in this employee agricultural system, while assessable remuneration still follows its legal bases ([arts. 14.5–7/34.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-6)).

### Benefit and bank-record boundaries

For ordinary RETA temporary incapacity, [LGSS art. 321](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a321) starts common-contingency entitlement on day 4, and occupational entitlement on the day after leave begins. The [Social Security benefit page](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365) sets the ordinary 60% days 4–20/75% from day 21 common-contingency rates and 75% occupational rate. Eligibility and regulatory-base calculation require the actual coverage and contribution record; do not promise a benefit from the bank debit. After sixty days of temporary incapacity with benefit entitlement, the mutua or SEPE pays the contribution quotas under [order art. 37.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-9).

For cessation, [LGSS arts. 338–339](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a338) use the prior twelve continuous months' contribution-base average, ordinarily multiplied by 70%. Test legal cessation, at least twelve qualifying months within the prior twenty-four, the 4–24-month duration scale and eighteen-month interval after prior recognition. A voluntary closure alone does not establish legal cessation.

For a right arising in 2026, calculate the ordinary monthly bounds from **600 × 7/6 = 700**. The monthly 600 IPREM is fixed by [LPGE 31/2022 DA90(b)](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128#da-90) and confirmed in the current [SEPE 2026 table](https://sepe.es/HomeSepe/prestaciones-desempleo/Cuantias-anuales.html) and [official 2026 IPREM table](https://vivienda.castillalamancha.es/iprem). The one-sixth increase comes directly from art. 339.4; this calculation does not select an annual IPREM convention.

| Dependent children | Ordinary monthly floor | Ordinary monthly cap | Year / official source |
|---|---:|---:|---|
| None | 560.00 (80%) | 1,225.00 (175%) | 2026; [LGSS art.339.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a339) |
| One | 749.00 (107%) | 1,400.00 (200%) | 2026; [LGSS art.339.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a339) |
| Two or more | 749.00 (107%) | 1,575.00 (225%) | 2026; [LGSS art.339.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a339) |

Apply `min(cap, max(floor, 70% × average base))`. If the claimant belongs to a category legally choosing a minimum contribution base below the ordinary RETA minimum, omit the floor under [RD 1541/2011 art. 13.2(d)](https://www.boe.es/buscar/act.php?id=BOE-A-2011-17173#a13); retain the cap. [Social Security's current calculation guidance](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/10538/2277?changeLanguage=es) confirms this exception. The specified partial cessations in art. 331.1.a(4)/(5) and temporary partial force majeure instead pay **50% of average base with neither floor nor cap**. Part-time employee hours do not create a separate proportional cessation-benefit cap.

For the child test in art. 339.4, require age under 26 or disability at least 33% at an older age, income below SMI excluding proportional extra payments, and cohabitation. [RD 1541/2011 art. 13.2(a)–(c)](https://www.boe.es/buscar/act.php?id=BOE-A-2011-17173#a13) supplies the income presumption, economic-support/maintenance exception to cohabitation and adjustment when the child count changes.

Under [art. 342](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a342), continuing the activity causing a qualifying partial cessation requires monthly net earnings no higher than the lower of SMI and the prior contribution base. Existing employee work in pluriactivity is compatible only if the preceding four months' average monthly remuneration plus the cessation benefit is **strictly below SMI**. Social Security's current guidance expressly excludes proportional extra payments from that SMI comparator: **1,221 monthly in 2026**. Equality fails the pluriactivity test; a low part-time wage alone does not establish entitlement.

Treat a TGSS debit as an identification clue. Obtain the base report, assessment and award before calling it RETA, employer RLC, reduced fee, regularisation or pluriactividad refund. Keep principal, interest, surcharge and refund nature separate. For direct-assessment IRPF, the [AEAT contribution-booking guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html) puts a regularisation in the year settled; do not amend the original year solely for that adjustment. An extra settlement payment **increases that year's deductible contribution expense**. A refund **reduces that year's contribution expense**; if the refund exceeds contributions paid in that year, the excess becomes **additional activity income**, rather than a negative expense carried into the original year. For example, a 1,100 refund with 800 current-year contributions gives zero net contribution expense and 300 additional income. Its 2025 box numbers are not assumed to be the approved 2026 return boxes.

## Deadlines and filing

| Action | Rule | Official source |
|---|---|---|
| RETA payment | Within the same month; use the assessed collection document/direct-debit arrangement | [RD 1415/2004 art. 56.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a56) |
| Employer payment | During the month following accrual | [RD 1415 art. 56.1](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a56) |
| RETA electronic dealings | Use authorised RED or the applicable electronic-office service | [Orden ESS/484/2013 art. 2.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362#a2) |
| Employers' RED obligation | Régimen General regardless of headcount; household and bullfighting exceptions in art. 2.3 | [Order ESS/484 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362#a2) |
| Base change requested Jan–Feb / Mar–Apr / May–Jun | Effective 1 March / 1 May / 1 July | [RD 2064 art. 45](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a45) |
| Base change requested Jul–Aug / Sep–Oct / Nov–Dec | Effective 1 September / 1 November / 1 January next year | [RD 2064 art. 45](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a45) |
| Regularisation due/refund | Due by month-end after notice; refund before 30 April after income-communication year | [RD 2064 art. 46.2.5](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46) |

Reconcile payroll workers/days/bases with the TGSS settlement and its payment receipt. Do not substitute a bank debit for a filed contribution record or apply the special artist quarterly option to every autónomo. For a regularisation notice, retain the tax-income communication, excluded-day schedule, provisional/final base schedule and due-date evidence.

**Dated 2026 order catch-up windows.** PJC/297/2026 was published **31 March 2026**. DT 1 gives direct-settlement differences on settlements from 1 February until the **last day of the month after TGSS notifies the update**, without surcharge. Simplified-settlement differences from 1 January are assessed when the systems/data are available and collected by the specified direct debit. Self-assessment differences from 1 January had a nominal no-surcharge endpoint of 31 May 2026. Because that was a Sunday, RD 1415/2004 art. 8(b) moves the payment endpoint to the preceding business day, ordinarily Friday 29 May 2026, subject to the applicable holiday calendar. This historical window is closed. ([RD1415/2004 art.8(b)](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a8)). Under DT 3, qualifying RETA/first-group sea workers who had elected the then-maximum base could elect between their existing and applicable maximum by **30 April 2026**, effective **1 January 2026**. The calendar windows have closed; do not present them as fresh elections or replace a notice-specific deadline ([order DT 1/3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#dt)).

## Penalties and interest

Contribution surcharges depend on compliance with the art. 29 data/settlement duties, as well as payment timing. They are separate from an administrative infringement fine.

| Late-payment situation | Surcharge | Official source |
|---|---:|---|
| Art. 29 duties met; paid in first calendar month after payment deadline | 10% | [LGSS art. 30.1.a.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Same duties met; paid from second subsequent month | 20% | [Art. 30.1.a.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Duties not met; paid before end of demand/assessment payment period | 20% | [Art. 30.1.b.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Duties not met; paid from end of that period | 35% | [Art. 30.1.b.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Non-contribution public-law Social Security debt | 20% | [Art. 30.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |

[LGSS art. 31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a31) makes interest exigible after fifteen days from the enforcement notice/deduction-procedure communication, and in the specified suspended-appeal case. Principal accrues from its original payment deadline; surcharge interest accrues from exigibility. The rate is the legal-money rate during each accrual period **increased by 25%**, unless the budget sets another rate. For the verified2026interval,the legal rate is **3.25%**,so art31.3gives **4.0625% annually** (`3.25%×1.25`). AEAT explicitly confirms those2026rates under the continued budget provisions;this does not import a foral tax-interest rule into Social Security ([currentAEAT2026confirmation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html)). Calculate each applicable rate interval separately;10000of unchanged principal accruing for a full365-day2026year gives406.25,and73eligible days on that365-day basis gives81.25. Those controls assume the statutory interest trigger and stated accrual days;they do not impose interest during an excluded regularisation window. Keep principal and surcharge accrual dates separate,and use the corresponding official rate for another year or an enacted in-year rate change. A25%relative increase is not25percentagepoints. A RETA regularisation paid within its special notice deadline has no such surcharge/interest.

## Cross-border points

Establish applicable social-security legislation before charging Spanish contributions. [Regulation 883/2004 arts. 11–13](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731) provides one applicable Member State, ordinary work-state rules, qualifying temporary-posting exceptions and multi-state-work rules. In particular, simultaneous employment in one Member State and self-employment in another follows the employment-state rule under art. 13.3. Do not treat a foreign client, foreign bank account or tax treaty as proof of social-security exemption.

Obtain the applicable-legislation determination and its evidence before computing an international worker's quotas. The detailed A1 application, non-EU agreements and special telework exceptions are outside this ordinary Spanish computation. Once Spanish legislation applies, use the relevant Spanish regime and income scope; ordinary international clients do not by themselves justify refusing a domestic RETA computation. Foral IRPF information remains relevant to the statewide regularisation under [LGSS art. 308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308).

## Two worked examples that recompute

### 1. Individual autónomo: statutory day average and a chosen base

Hypothetical 2026 records establish **180 calendar days subject to regularisation**, direct-assessment activity net income 10,000 after deducting own RETA of 1,200, ordinary individual status, full coverage and no bonus. Add back 1,200 and deduct 7%: 10,416. The statutory monthly income is `10,416 / 180 × 30 = 1,736`, in general band 4. A chosen base of 1,200 lies between 1,143.79 and 1,850. For one complete month on that base, CC is 339.60, occupational 15.60, cessation 10.80, training 1.20 and MEI 10.80, total **378.00**. The regularisation comparison still uses the actual provisional-base schedule; the example does not infer it from the income day count ([RD 2064 arts. 44/46](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46); [order arts. 18/37](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10)).

```oa-check
name: RETA 2026 day average and full-coverage month
inputs:
  net_irpf: 10000
  own_contributions_deducted: 1200
  regularisable_days: 180
  chosen_base: 1200
steps:
  computable_income: (net_irpf + own_contributions_deducted) * 0.93
  monthly_income: computable_income / regularisable_days * 30
  minimum_margin: chosen_base - 1143.79
  maximum_margin: 1850 - chosen_base
  cc: chosen_base * 0.283
  occupational: chosen_base * 0.013
  cessation: chosen_base * 0.009
  training: chosen_base * 0.001
  mei: chosen_base * 0.009
  contribution: cc + occupational + cessation + training + mei
expected:
  computable_income: 10416
  monthly_income: 1736
  minimum_margin: 56.21
  maximum_margin: 650
  cc: 339.60
  occupational: 15.60
  cessation: 10.80
  training: 1.20
  mei: 10.80
  contribution: 378
```

### 2. Employer: capped worker, solidarity, part-time and household controls

An ordinary monthly group-1 employee has **6,000 of assessable remuneration for October 2026**, already including extra-pay proration, no overtime, an indefinite contract and no contribution relief. The verified work facts meet table II(a)'s exclusive-office conditions, giving the statutory 1.50% AT/EP tariff. Both ordinary bases are capped at 5,101.20. Solidarity uses 510.12 in the first slice and 388.68 in the second. On the separately rounded component working paper, employer contributions are **1,648.98**, employee deductions **333.37**; employer cost is **7,648.98** before other costs. Cash after employee social contributions is 5,666.63 **before IRPF withholding**, which must be computed separately. A second worker in the same payroll provides a part-time floor control: group 1, 80 actual hours and 900 assessable remuneration including proration, no overtime. CC is floored at 80 ×11.98 =958.40, while AT remains 900 because its floor is 686.40. Reconcile component rounding with the final TGSS settlement ([order arts. 3/4/16/17/33/38/39](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296); [LGSS DA 61 table II(a)](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37)).

A separate household relationship in the same comparison has lawful part-time pay of **900/month including extras**, an indefinite contract, all ordinary 20/80 relief conditions met and no special award. The salary band gives **970**, rather than 900, as contribution base. With components rounded to cents, employer CC is **183.14**, occupational **14.55**, unemployment **10.67**, FOGASA **0.39** and MEI **7.28**, total **216.03**. Employee CC/unemployment/MEI are **45.59/15.04/1.46**, total **62.09**. The employer remits **278.12** and cash after employee contributions is **837.91**, before any separate applicable tax deduction. Do not charge household training or apply the 20/80 relief to the employee share ([order arts. 15/16/35](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-7); [RDL 16/2022 DA 1](https://www.boe.es/buscar/act.php?id=BOE-A-2022-14680#da)).

```oa-check
name: October 2026 payroll cap and employer-employee solidarity
inputs:
  remuneration: 6000
  cap: 5101.20
  parttime_hours: 80
  parttime_pay: 900
  household_pay: 900
  household_band_base: 970
steps:
  base: min(remuneration, cap)
  slice_one: min(max(remuneration - cap, 0), 510.12)
  slice_two: min(max(remuneration - 5611.32, 0), 2040.48)
  slice_three: max(remuneration - 7651.80, 0)
  employer_cc: round(base * 0.236, 2)
  employer_unemployment: round(base * 0.055, 2)
  employer_fogasa: round(base * 0.002, 2)
  employer_training: round(base * 0.006, 2)
  employer_mei: round(base * 0.0075, 2)
  employer_occupational: round(base * 0.015, 2)
  employer_solidarity: round(slice_one * 0.0096, 2) + round(slice_two * 0.0104, 2) + round(slice_three * 0.0122, 2)
  employee_cc: round(base * 0.047, 2)
  employee_unemployment: round(base * 0.0155, 2)
  employee_training: round(base * 0.001, 2)
  employee_mei: round(base * 0.0015, 2)
  employee_solidarity: round(slice_one * 0.0019, 2) + round(slice_two * 0.0021, 2) + round(slice_three * 0.0024, 2)
  employer_total: employer_cc + employer_unemployment + employer_fogasa + employer_training + employer_mei + employer_occupational + employer_solidarity
  employee_total: employee_cc + employee_unemployment + employee_training + employee_mei + employee_solidarity
  employer_cost: remuneration + employer_total
  before_irpf_cash: remuneration - employee_total
  parttime_cc_base: min(max(parttime_pay, parttime_hours * 11.98), cap)
  parttime_at_base: min(max(parttime_pay, parttime_hours * 8.58), cap)
  household_employer_cc: round(household_band_base * 0.236 * 0.8, 2)
  household_occupational: round(household_band_base * 0.015, 2)
  household_employer_unemployment: round(household_band_base * 0.055 * 0.2, 2)
  household_fogasa: round(household_band_base * 0.002 * 0.2, 2)
  household_employer_mei: round(household_band_base * 0.0075, 2)
  household_employee_cc: round(household_band_base * 0.047, 2)
  household_employee_unemployment: round(household_band_base * 0.0155, 2)
  household_employee_mei: round(household_band_base * 0.0015, 2)
  household_employer_total: household_employer_cc + household_occupational + household_employer_unemployment + household_fogasa + household_employer_mei
  household_employee_total: household_employee_cc + household_employee_unemployment + household_employee_mei
  household_remitted: household_employer_total + household_employee_total
  household_before_tax_cash: household_pay - household_employee_total
expected:
  base: 5101.20
  slice_one: 510.12
  slice_two: 388.68
  slice_three: 0
  employer_solidarity: 8.94
  employee_solidarity: 1.79
  employer_total: 1648.98
  employee_total: 333.37
  employer_cost: 7648.98
  before_irpf_cash: 5666.63
  parttime_cc_base: 958.40
  parttime_at_base: 900
  household_employer_cc: 183.14
  household_occupational: 14.55
  household_employer_unemployment: 10.67
  household_fogasa: 0.39
  household_employer_mei: 7.28
  household_employee_cc: 45.59
  household_employee_unemployment: 15.04
  household_employee_mei: 1.46
  household_employer_total: 216.03
  household_employee_total: 62.09
  household_remitted: 278.12
  household_before_tax_cash: 837.91
```

## Ask the client first

1. Which regime, employment/shareholding/director/family status, registration dates, contribution days, benefits and applicable-state determination are documented?
2. What activity income, own contributions, company work/capital income and tax-administration records establish the RETA annual numerator?
3. Which provisional bases, actual coverage, reduced-fee/bonus awards and regularisation notices apply to each period?
4. For payroll, what remuneration, in-kind items, annual extra pay, overtime, group, contract, working time, CNAE and actual occupation establish each base and rate?
5. What employment and RETA CC payments support a pluriactividad refund, including the employer share?
6. What filed settlement, demand/enforcement dates and bank receipts distinguish principal, adjustments, surcharge and interest?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296) | 2026 employee/RETA bases, component rates, solidarity, pluriactividad and long-IT contribution payer, arts. 1–5, 16–18, 33/37 | 2026-10-26 |
| [LGSS, RDL 8/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724) | Regime inclusion, assessable pay, MEI, solidarity, income definition, regularisation, surcharge/interest, office tariff and benefit boundaries | 2026-10-26 |
| [RD 2064/1995](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579) | Arts. 44–46, calendar-day denominator, average provisional base, signed monthly adjustments, exclusions and historical-base election | 2026-10-26 |
| [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409), [RDL 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482), [RDL 22/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429) | Starting-fee eligibility/periods, family bonus, transitional amounts and Ceuta/Melilla effective date | 2026-10-26 |
| [RD 1415/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836), [Orden ESS/484/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362) | Payment periods, art.8(b) preceding-business-day adjustment and mandatory electronic dealings | 2026-10-27 |
| [Orden PJC/178/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) | Earlier-year contribution ceiling, MEI and pluriactividad threshold | 2026-10-26 |
| [TGSS autonomous-worker guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) | Administrative explanation; bounded literal 88.64 complete-month expected-contribution worksheet, with combined-rate/reduced-fee discrepancies and unreconciled statutory authority retained, not substituted for the order | 2026-10-28 |
| [BNR 02/2026](https://www.seg-social.es/descarga/es/BNR%2002_2026), [BNR 05/2026](https://www.seg-social.es/wps/wcm/connect/wss/61f4db39-8366-4d8f-863b-34332b1d527a/BNR%2B5_2026.pdf?MOD=AJPERES), [RDL 3/2026 art 3/DA 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2548#a3), [budget-prorogation 38](https://www.boe.es/buscar/act.php?id=BOE-A-2003-21614#a38) | Targeted 2026 operating passages establish table/MEI context, not an express DT 5 monetary extension; literal published administrative total and diagnostic statutory-input total remain distinguished | 2026-10-28 |
| [Social Security, temporary incapacity](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365), [AEAT RETA-booking guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html) | Ordinary benefit percentage boundaries and year of booking a settled regularisation | 2026-10-26 |
| [Regulation 883/2004, arts. 11–13](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731) | Applicable-state gateway; read in a normal browser after automated access was blocked | 2026-10-26 |
| [2025 order art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780#a1-9), [2026 order DT 1/3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#dt) | Restored 2025 solidarity comparative bands/splits and dated catch-up/election windows | 2026-10-27 |
| [2026 order arts. 14–16/34–35](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296), [incorporated 2021 formula, art. 13](https://www.boe.es/buscar/doc.php?id=BOE-A-2021-20075), [RDL 16/2022 DA 1/2](https://www.boe.es/buscar/act.php?id=BOE-A-2022-14680), [TGSS household guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Empleo%2Bdel%2Bhogar/guia) | Household salary bands, components and ordinary relief; agricultural monthly/daily/inactivity bases, components, visually read reduction formulas and protected-period routes | 2026-10-27 |
| [LGSS arts.331/338–339/342](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a339), [RD1541/2011 art.13](https://www.boe.es/buscar/act.php?id=BOE-A-2011-17173#a13) | Cessation rate, monthly bounds, child/low-base exceptions, partial cases and pluriactivity | 2026-10-27 |
| [LPGE31/2022 DA90](https://www.boe.es/buscar/act.php?id=BOE-A-2022-22128#da-90), [SEPE2026 figures](https://sepe.es/HomeSepe/prestaciones-desempleo/Cuantias-anuales.html), [official2026 IPREM table](https://vivienda.castillalamancha.es/iprem) | Monthly600 IPREM and continued2026 indicator, distinct from annual conventions | 2026-10-27 |
| [Social Security cessation calculation](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/10538/2277?changeLanguage=es) | Current operational bounds, lawful lower-minimum-base exception and SMI comparator excluding proportional extra pay | 2026-10-27 |
|[AEATcurrent2026legal/default-interestconfirmation](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/guia-principales-novedades/otras-cuestiones-interes.html) |2026legal3.25%anddefault4.0625%;LGSS31.3selects the SocialSecurityformula andexistingtrigger/accrualrules remain separate |2026-10-27 |
| [TGSS current system guide, Prórroga Tarifa Plana](https://www.seg-social.es/wps/portal/wss/internet/HerramientasWeb/9d2fd4f1-ab0f-42a6-8d10-2e74b378ee24/44b5f09d-6c25-4dcd-8210-c21700c67096?changeLanguage=es), [current LETA art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a3-5), [RD 2064 arts. 44/46](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44) | Published equality/above-SMI extension assessment, separate calendar years and exact remaining regularisation-text boundary | 2026-10-27 |

**Not yet confirmed:** the general 2026 statutory monetary bridge and authoritative MEI/assessment reconciliation beyond the supplied literal 88.64 complete-month published-TGSS administrative worksheet, including a contrary/corrected tariff or legal challenge; the legal reconciliation of the literal 'exceeds' regularisation wording in art. 38 ter.6/RD 2064 art. 46.1 at exactly SMI, despite art. 44.3.f's equal-or-higher ordinary-base rule and TGSS's explicit assessment route above. Sea, self-employed agricultural, artist/training and other special-system contribution calculations, non-EU coordination, case-specific ERTE exemptions and individual benefit awards remain outside the supplied ordinary, household and agricultural-employee computations. Independent whole-pack review remains outstanding.

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
