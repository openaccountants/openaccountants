---
name: venezuela-income-tax
description: "Compute Venezuela individual income tax for tax year 2026 from documented, legally classified income. Covers resident Tarifa 1 marginal bands in tax units, the 774 UT standard versus supported itemized personal deductions, personal/family tax reductions, residence and source, ordinary self-employed costs, source-separated losses, nonresident salary and professional bases, foreign-tax credits, annual/estimated-return statutory duties, withholding credits and an auditable bank-to-return workpaper. Use for ISLR persona natural, tarifa 1, desgravamen único, rebajas, sustraendo, RIF and declaración definitiva or estimada. Current UT currency value, administrative filing and withholding instructions, employment-bonus judicial interpretation and separate payroll-contribution amounts remain explicitly unconfirmed where no accessible primary text establishes them."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/venezuela-income-tax"
  jurisdiction: "VE"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Venezuela: individual income tax (ISLR), 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer layer.** A Venezuelan resident/domiciliary generally computes tax on worldwide income, while a nonresident without a PE/fixed base is taxed on Venezuelan-source enrichment. Ordinary resident individuals use the eight marginal Tarifa 1 bands below, ending at 34%, after legally permitted costs and either supported personal deductions or the alternative 774 U.T. standard deduction. Apply eligible 10-U.T. personal/family tax reductions after the tariff computation, then supported withholding/advances and any properly limited foreign-tax credit. Nonresident individuals generally use 34% on their applicable statutory net base; a professional fee's 90% presumed base is not the rule for every payment. [LISLR arts. 1-4, 8, 39, 50-60, 83](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

**Essential limits.** The current bolívar value of the tax unit (U.T.) has not been confirmed from accessible primary material. Produce a sourced U.T. computation and a conditional currency formula, not a guessed bolívar balance. Employment/bonus classification also needs the legal documents and current controlling interpretation: the 2015 gazette's art. 31 is quoted as printed, but inaccessible judicial/administrative material prevents this Guide from certifying every bonus's treatment. A description containing BONO is not an exemption. This is a tier-2 source-based rewrite, without accountant approval.

The primary texts opened/read on 11 November 2026 are the **Ley de Impuesto sobre la Renta** (LISLR), consolidated in official Gaceta 6.210 Extraordinario of 30 December 2015, and the **Código Orgánico Tributario** (COT), official Gaceta 6.507 Extraordinario of 29 January 2020. Government hosts provide these gazette facsimiles; the filenames refer to other laws in the same multi-law publications. Exact statutory conditions, visual table transcription and old-topic destinations are retained in the review evidence. Later unconfirmed administrative measures are not represented as absent.

## Who this applies to

Use this Guide for individuals, including ordinary self-employed professionals, contractors, employees and landlords. Establish the income's legal category before a computation. Companies/assimilated entities, a consortium or partnership/member allocation, and a deceased estate require the applicable distinct rules in arts. 7-10; this Guide does not turn them into the same taxpayer because a bank account is in an individual's name. The annual job here is individual ISLR, not an IVA return or payroll-contribution assessment. [LISLR arts. 7-10](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=6).

### Residence, domicile and source

LISLR art. 1 taxes a resident/domiciliary's income regardless of domestic or foreign source; a nonresident/non-domiciliary's income must have its source/cause in Venezuela. A foreign taxpayer with a Venezuelan PE/fixed base is taxed on domestic and foreign income attributable to it, not automatically the entire foreign enterprise's income. Art. 6 identifies Venezuelan-source causes, including domestic economic activity, work/capital used in Venezuela, domestic property and locally exploited rights. A foreign currency, payer bank or Zelle account does not alone make income foreign-source. [LISLR arts. 1, 6-7](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

Under COT art. 30, domicile includes more than 183 days, continuous or discontinuous, in the calendar year **or the immediately preceding year**. A home/residence in Venezuela is a separate ground unless the person spends more than 183 days in another country that year and proves fiscal residence there. Its official-duty ground, foreign residence certificate rule and rebuttable Venezuelan-nationality presumption also matter. LISLR art. 51 requires both no more than 183 current-calendar-year days **and no COT domicile** for nonresident status; its prior-year continuous-presence sentence does not displace the current COT's wider tests. Exactly 183 days does not defeat another domicile ground. [COT art. 30](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=5); [LISLR art. 51](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

A domestic construction/installation/assembly PE duration limb over six months is not a six-month exemption for every agency/fixed-place/service case. An individual performing independent services through a fixed base must analyze art. 7's actual conditions. Any treaty claim requires the actual in-force treaty, entitled residence and the evidence required by art. 3, including official translation/legalization of foreign residence certificates. No treaty rate or tie-breaker is assumed here. [LISLR arts. 3, 7](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).

### Classify investment and exempt receipts before aggregation

Art. 14(9) exempts the specified natural-person interest from term deposits, mortgage certificates, savings certificates and other savings instruments governed by the identified banking/special laws, and returns from public-offer mutual/investment funds. It does not exempt every loan, foreign instrument or receipt labeled INTERESES. Art. 14(6) separately exempts the identified retirement/pension/disability payments, including the stipulated heir transfers. Insurance indemnities in art. 14(5) have an exception for compensation of losses already included in costs/deductions; national-public-debt bonds and other Republic-issued titles have the art. 14(12) rule. Identify instrument, issuer, recipient and actual statutory conditions; a current sector exoneration or BCV-instrument measure not established here remains unconfirmed. Dividends require their separate chapter analysis rather than automatic ordinary-rate treatment. [LISLR arts. 14, 64-76](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=7).

### Employment and bonus classification limit

The printed art. 31 treats regular or incidental consideration/utility from dependent personal services as net enrichment, regardless of salary character, except travel allowances and food bonus. Art. 16 separately sets documentary normal/necessary conditions for its representation/travel exclusions; art. 14 has specified employment indemnity, pension and insurance exemptions with their own conditions. Do not turn a general payroll label into proof of any of those categories. [LISLR arts. 14, 16, 31](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=7).

The printed statute is not, by itself, a completed current payroll interpretation. Official TSJ decision text concerning the employment-base interpretation could not be read through direct access, the ordinary browser route or the dated archive attempt. **The controlling employment/bonus interpretation, and the treatment of Guerra Económica or another named bonus beyond the statutory text, remain not yet confirmed.** Obtain current primary legal corroboration and professional classification before finalizing the employment base. Record salary, recurring/extraordinary benefits, food benefit, travel allowance and any other claimed exemption separately; do not include all bonuses automatically or exclude all nonsalary bonuses automatically. The tax-on-income method below can then run on the properly established net amount.

## Rates, bands and thresholds

### Resident Tarifa 1

All band endpoints are annual taxable net enrichment in U.T., after the applicable personal deduction. The rate applies only to the fraction in its band. The subtraction column and cumulative tax are derived arithmetic from the enacted bands, not additional legal allowances. For the active band, `tariff_tax_UT = taxable_UT × rate - derived_subtraction_UT`. At a boundary, either adjacent formula agrees. [LISLR art. 50, Tarifa 1](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

| Taxable enrichment in U.T. | Marginal rate | Derived subtraction U.T. | Cumulative tariff tax at upper endpoint U.T. | Official source |
|---|---|---|---|---|
| Through 1,000 | 6% | 0 | 60 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50; visually read first row) |
| Over 1,000 through 1,500 | 9% | 30 | 105 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 1,500 through 2,000 | 12% | 75 | 165 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 2,000 through 2,500 | 16% | 155 | 245 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 2,500 through 3,000 | 20% | 255 | 345 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 3,000 through 4,000 | 24% | 375 | 585 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 4,000 through 6,000 | 29% | 575 | 1,165 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |
| Over 6,000 | 34% | 875 | No upper endpoint | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50) |

### Other statutory amounts and conditions

| Item | Amount or test, with conditions | Official source |
|---|---|---|
| Annual-tax unit | Use the UT value in force at fiscal close; for a nonannual tax period COT uses the value effective at the start. Current bolívar amount unconfirmed | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3 (COT art. 3, third paragraph) |
| Resident standard personal deduction | Optional 774 U.T.; if used, art. 57's itemized personal deductions are unavailable | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 58) |
| Mortgage-interest personal deduction | Paid qualifying principal-home acquisition-loan interest, not principal; at most 1,000 U.T. per tax year, with art. 57 evidence/non-reimbursement conditions | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 57(4)) |
| Principal/permanent-home rent personal deduction | Paid qualifying home rent, at most 800 U.T. per tax year, with art. 57 evidence/non-reimbursement conditions | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 57(4)) |
| Education personal deduction | Paid domestic educational institution costs for taxpayer/descendants not older than 25; no age limit for special education; art. 57 gives no separate numeric monetary cap for this item | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 57(1)) |
| Taxpayer reduction | 10 U.T. annually for a resident individual | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 59) |
| Spouse reduction | 10 U.T. for spouse not separated as to property; unavailable when spouses declare separately | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 59(1), first paragraph) |
| Qualifying direct ascendant/descendant reduction | 10 U.T. each, supported by taxpayer and resident in Venezuela; adult descendants must be unable to work, or studying and younger than 25; shared support divides the reduction; official-duty exception below | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 59(2), second/third paragraphs) |
| Resident annual-return tests | Annual global net enrichment over 1,000 U.T. **or** gross income over 1,500 U.T.; statutory primary agricultural/stockbreeding/fishing/pisciculture gross threshold over 2,625 U.T. under its conditions | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16 (LISLR art. 77) |
| Nonresident annual return | Venezuelan enrichment/loss declared whatever its amount, under the Regulation; withholding does not itself prove no return is needed | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17 (LISLR art. 79) |
| Estimated-return enabling threshold | Prior-year net enrichment over 1,500 U.T. permits the executive to require specified categories/arrangements; not proof of one universal present calendar or instalment rule | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17 (LISLR art. 80) |
| Operating losses | Matching-source income within the next three tax periods; use in each period at most 25% of that current enrichment; no foreign loss offset against territorial enrichment | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14 (LISLR art. 55), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5 (art. 4) |
| Nonresident individual general rate | 34% on the legally applicable net base, subject to special regimes and actual treaty entitlement | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (LISLR art. 50, sole paragraph) |
| Nonresident noncommercial professional base | 90% of gross, without prejudice to technical-service art. 41; combined with art. 50, ordinary 34% tax equals 30.6% of gross by multiplication | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=12 (LISLR art. 39), https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |

The old Guide's historical bolívar UT values, percentage increase and resulting bolívar lookup table are not established here as current official inputs. Retain the conversion **method**: if confirmed fiscal-close UT is `U` bolívares, 10 U.T. is `10 × U`, 774 U.T. is `774 × U`, and the 800/1,000/1,500-U.T. limits are `800 × U`, `1000 × U`, `1500 × U`. Keep the providencia, its effective date and the relevant fiscal close with every real currency figure. [COT art. 3](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3).

## The base

### The method, step by step

**Income timing (art. 5).** Recognize income when the producing operation occurs. For multi-year credit assignments/discounts, recognize the assignee's proportionate benefit. Rents/subrents and the specified bank, insurance, credit-institution and art. 7(b-e) lending income follow accrual. Dependent employment and fortuitous gains follow payment. Reconcile opening/closing receivables and accruals to payments; bank receipts alone do not establish the year. Ordinary services performed in December and collected in January remain in the operation year. [LISLR art. 5](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).

**Expense timing (art. 32).** Match permitted expenses accrued during the tax year to operation-available income. For payment-available income, use expenses actually paid that year, retaining applicable art. 27(5)-(6) depreciation/fixed-asset-loss allowances. Preserve art. 27(3), (11), (20) and its twelfth/thirteenth paragraphs: paid taxes, paid rental-property administration/conservation, paid R&D and qualifying donation conditions remain controlling. This timing step does not resolve the employment-base interpretation caveat above. [LISLR arts. 27 and 32](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

1. **Establish taxpayer and period.** Determine residence/domicile, source and any fixed base, spouse/property regime and applicable ordinary/special income category. The current calendar/alternative-fiscal-year procedures must be evidenced; a business individual does not acquire an unverified alternative year by changing a spreadsheet. [LISLR arts. 1, 7-8, 51, 54, 77-81](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).
2. **Reconcile records to gross income.** Match invoices, contracts, employer statements, platforms and bank receipts. Separate transfers, loans, refunds, tax-account movements and exempt receipts. Art. 16's gross income covers sales/services, rents and other regular/incidental receipts, with statutory exclusions; source depends on arts. 1/6, not account location. Retain both original currency and properly supported conversion. [LISLR arts. 1, 6, 14, 16](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).
3. **Compute each business/source net amount before personal deductions.** Deduct permitted corresponding costs and art. 27 expenses under their evidence/timing tests; a bank debit is not automatically a deduction. Keep dependent-service net enrichment and specialist proportional bases separate. Do not treat wage net cash after payroll deductions as the legal employment-tax base. [LISLR arts. 4-5, 21, 23, 27, 31-32](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).
4. **Apply eligible source-separated operating losses.** Track each vintage, prior use and next-three-period expiry. Use at most 25% of the matching-source current enrichment. Do not net foreign losses against territorial income or treat an uncompensated inflation loss as an ordinary carryforward. Keep an applicable inflation analysis separate from this ordinary personal-deduction calculation. [LISLR arts. 4, 55, 181](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).
5. **Choose one resident personal-deduction method.** Compare art. 58's 774 U.T. standard with the documented amount actually permitted by art. 57, including caps, eligible persons, domestic-provider conditions, paid-year proof and reimbursements. No standard-plus-itemized combination. Deduction selection never excuses evidence for business expenses, income classification or residence. [LISLR arts. 57-58](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).
6. **Apply the appropriate tariff/base.** Compute ordinary resident taxable net enrichment and each Tarifa 1 band. Keep separately proportional items outside the ordinary band calculation. For a nonresident, use the established statutory net base and applicable 34% rule or specific exception, not the resident 774-U.T. election or personal reductions. [LISLR arts. 31, 39, 50, 57-60, 76](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).
7. **Compute personal/family reductions and foreign-tax credit.** Establish each art. 59 entitlement and allocation; subtract these tax reductions after tariff, not from taxable income. Apply art. 2's foreign-tax credit only to qualifying tax actually paid within the proper cap. If requested reductions/credits exceed assessed tax, record the issue; no automatic refundable excess is established here. [LISLR arts. 2, 59-60](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).
8. **Reconcile advances to annual liability.** Withholding and qualifying estimated payments are tax on account under art. 83. Match certificates and actual credit/payment records, then compute a payable balance or supported excess-payment claim under art. 56; a negative spreadsheet number is not proof of a cash refund. [LISLR arts. 56, 83-85](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).
9. **Close an auditable return workpaper.** Keep gross-to-net schedules, source/year/loss allocations, personal election and family evidence, the actual UT ruling/FX rates, statutory computation and current authorized filing/payment instructions. Reconcile to the live return only after its fields, deadline and acknowledgement process have been read. [LISLR arts. 77-89, 96](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).

For positive ordinary resident taxable income `B` in U.T., recompute directly:

`tax_UT = .06 × min(B,1000) + .09 × min(max(B-1000,0),500) + .12 × min(max(B-1500,0),500) + .16 × min(max(B-2000,0),500) + .20 × min(max(B-2500,0),500) + .24 × min(max(B-3000,0),1000) + .29 × min(max(B-4000,0),2000) + .34 × max(B-6000,0)`.

The eight subtraction amounts are derived by continuity from this formula. Do not apply 34% to all resident income just because it exceeds the top threshold. A negative current net result requires the source/vintage loss workpaper, not a negative Tarifa 1 charge. [LISLR arts. 50, 55](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

### Personal deductions: standard versus supported itemized amounts

Art. 58 offers resident individuals a single 774-U.T. alternative to **all art. 57 deductions**. It does not remove the need to prove an income-producing cost, a withholding credit or an exemption. Compare documented itemized deductions with the standard before choosing; do not assume an expense category or a reimbursement that was not established. [LISLR arts. 57-58](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

Art. 57 permits:

- Education paid to domestic teaching institutions for the taxpayer or descendants not older than 25; the age ceiling does not apply to special education. The article supplies no separate monetary limit, but the actual eligible payment remains necessary.
- Hospitalization, surgery and maternity insurance premiums paid to companies domiciled in Venezuela. A life-insurance description alone does not establish this category; the old pattern SEGURO DE VIDA is not an automatic deduction.
- Domestic medical, dental and hospitalization services for the taxpayer and persons within art. 59. This is not a rule that any purchase at a pharmacy qualifies as a medical-service payment.
- Paid interest on a qualifying principal-home acquisition loan, capped at 1,000 U.T. per tax year, or paid rent for the permanent home, capped at 800 U.T. The loan principal is not qualifying interest, and a business-property payment is not automatically a personal-home deduction.

Art. 57 states no separate numerical monetary cap for its education, qualifying insurance or medical-service items; actual eligible payments and the remaining conditions still control. No amount may be deducted again if it was deductible as a business cost/expense. Payments must fall within the tax year, with vouchers required by art. 57; no reimbursement from employer, contractor, insurer or substitute entity may be claimed. Shared education/insurance payments are divided among the paying taxpayers; the receipt must bear the payee's RIF. The third paragraph deems its specified expenses abroad domestic for the listed Venezuelan diplomatic/consular/public officials and official-entity representatives abroad in official functions; do not silently deny that exception or extend it to every expatriate. [LISLR art. 57, all paragraphs](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

### Credits, spouses and dependants

Art. 59 gives a resident individual a 10-U.T. tax reduction, plus 10 U.T. for a spouse not separated as to property and 10 U.T. for each qualifying supported direct ascendant/descendant resident in Venezuela. Adult descendants qualify only if unable to work or studying and younger than 25. The education-deduction age test (not older than 25) and student-descendant credit test (younger than 25) differ; preserve that boundary. The specified official-duty group in art. 57's third paragraph may receive the art. 59(2) reduction even for supported ascendants/descendants abroad. [LISLR art. 59](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

Spouses not separated as to property are ordinarily one taxpayer under art. 54 and declare jointly under art. 78, including separately administered own-property income. Art. 54's printed exception expressly allows the married woman to declare the listed employment or noncommercial-professional enrichment separately; a current interpretation permitting any different election is not assumed here. Spouses separated by marriage contract, judgment or judicial declaration declare all enrichment separately under art. 78. In separate declarations there is no spouse reduction, and only one spouse claims family-charge reductions under art. 59's first paragraph; where several taxpayers support the same qualifying person, divide that person's reduction under its second paragraph. Record family, property-regime and support documents before counting persons. [LISLR arts. 54, 59, 78](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

### Documented business costs and expenses

Art. 21 computes corresponding gross profit by deducting permitted costs of goods/services. Art. 23 accepts direct-seller invoice cost only where prices do not exceed normal market prices, with required seller RIF and the foreign-purchase invoice exception; an unsupported affiliate debit note is insufficient. Common taxable/exempt costs are apportioned under art. 15 and territorial/foreign common costs under art. 23's seventh paragraph. [LISLR arts. 15, 21, 23](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=8).

Art. 27's ordinary expense rule requires normal/necessary income-producing expenditure, not already costed, with domestic and timing conditions unless a stated exception applies. Rent of dedicated income-producing premises, business professional/legal/accounting services, office materials, publicity, business-bank charges, software/hosting and telecoms are **candidates to test**, not automatic deductions from bank labels. Keep actual business purpose, invoice, allocation and payment/accrual evidence. Mixed home/office, internet or telephone expense needs supported business use; no arbitrary percentage is supplied. Capital acquisition is not a recurring subscription merely because its description says SOFTWARE. Depreciation/amortization must satisfy art. 27(5), without duplicate cost and with the location/use and reasonable-life conditions; a current regulatory rate table was not confirmed. [LISLR arts. 23, 27-28, 32](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=8).

The first paragraph of art. 27 prohibits the specified taxpayer/spouse/minor-descendant remuneration and participating-partner/manager arrangements; a sole proprietor cannot deduct a wage paid to themselves merely by moving money between accounts. Interest requires income-producing borrowed capital and applicable related-party restrictions. Bad debts need the specific business-origin, prior-inclusion and writeoff/insolvency-or-uneconomic-collection conditions in art. 27(8); an expected-loss reserve is insufficient. R&D has its actual-payment condition, rented-property administration its 10%-of-gross-rent ceiling, and ISLR itself is excluded under the fifth paragraph. Personal living costs and drawings do not meet the income-producing test; fines/late-payment charges are not assumed deductible without specific legal support. [LISLR art. 27, including (2), (8), (11), (20), first, fourth and fifth paragraphs](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

Employment consideration is treated as net enrichment by printed art. 31; do not deduct ordinary business costs from salary simply because both appear in the same bank account. Build and evidence the business/professional net-income schedule separately. The exact current employment/bonus interpretation remains subject to the limit above. Personal art. 57 deductions or the art. 58 election are a separate step. [LISLR arts. 27, 31, 57-58](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=9).

### Operating losses and inflation referral

Maintain territorial and foreign loss schedules separately. Art. 55 permits same-source operating-loss use in the next three tax periods, no more than 25% of the relevant current enrichment in any period. Art. 4 prevents a foreign loss from offsetting territorial enrichment or loss. Keep actual loss returns, vintage, earlier utilization and expiry. The rule is not an unrestricted three-calendar-year deduction from any income. [LISLR arts. 4, 55](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=5).

An included commercial self-employed taxpayer can raise separate art. 171 inflation-adjustment questions. Its exclusions include designated special taxpayers and the listed financial businesses; art. 181 denies carryforward of uncompensated net inflation losses. Do not insert an accounting inflation adjustment into the personal-deduction line or treat an inflation loss as an ordinary operating loss. The full specialized inflation method, actual INPC and implementation measures require separately sourced work; art. 186's printed FX/indexed-adjustment sentence is incomplete and its full interpretation is not established here. [LISLR arts. 171, 181, 186, 193](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=26).

### Separate tax units, currencies and contribution bases

Keep **income-tax units**, **currency translation**, **penalty exchange multiples** and **payroll-contribution wage bases** separate. The annual UT comes from COT art. 3 at fiscal close. Foreign-source gross income uses the BCV fiscal-year-average methodology in art. 16; foreign tax credited uses its actual payment-date exchange rate under art. 2. A blanket rule using one transaction spot rate for every annual income/credit line is not supported by these provisions. The current authoritative rule/rate for other domestic foreign-currency expense/income situations remains a documented input, not a guessed default. [COT art. 3](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3); [LISLR arts. 2, 16](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

No current minimum wage, economic income-floor dollar amount or payroll base is inferred from an old UT or a bonus announcement. Those figures do not automatically set the taxable employment base, an IVSS/FAOV cap, or the penalty currency. The old statutory/economic wage comparison is retained as a **measurement warning**, with current amounts/bases unresolved below.

### Bank-statement triage and terms

Treat the following labels as discovery cues only. Match the actual payer, invoice, service, legal character, currency and underlying documents before deciding the tax line. A bank statement alone supports a provisional reconciliation; it does not establish a deductible expense, exemption, tax-paid credit, residence or source. Where no complete bank statement exists, reconcile the alternative books/payroll/invoice evidence; do not manufacture completeness. Books and entries require supporting documents under art. 88, and local expense invoices must meet art. 89's issuer-RIF/format requirements. [LISLR arts. 16, 88-89](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=8).

| Pattern or term | Provisional destination | Evidence and condition before final treatment |
|---|---|---|
| ABONO, TRANSFERENCIA, PAGO RECIBIDO, DEPÓSITO, client name | Receipt reconciliation | Determine whether income, loan, capital or own transfer; match counterparty and contract |
| HONORARIOS, SERVICIOS, FACTURA, COBRO FACTURA | Professional/business receipt candidate | Match invoice and performance; separate any actual IVA charged without inventing its rate |
| STRIPE, PAYPAL, WISE, BINANCE payout; Zelle RECEIVED/SENT | Platform/account reconciliation | Gross sales/fees, own transfers and currency require platform/contract evidence; payout is not automatically net taxable profit |
| SALARIO, NÓMINA, SUELDO, employer name | Employment schedule | Employer statement, gross benefits and withholding; apply established employment classification |
| CESTATICKET, BONO, GUERRA ECONÓMICA | Separate classification register | Food benefit/other bonus documents and current governing interpretation; label is not an exemption |
| ALQUILER, CANON DE ARRENDAMIENTO received | Rental-income schedule | Property, lease, source and actual availability; distinguish home expense from rent received |
| INTERESES, RENDIMIENTOS | Investment schedule | Debtor/instrument/source and actual exemption/proportional-regime evidence |
| DIVIDENDOS | Separate dividend analysis | Do not place every dividend into ordinary Tarifa 1; arts. 64-76 require distinct base/rate analysis |
| DEVOLUCIÓN ISLR, REINTEGRO SENIAT | Tax-credit/refund reconciliation | Match prior tax/payment/refund; not automatically a new service receipt |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS, loan/capital repayment | Nonincome movement candidate | Match both accounts or loan principal; unexplained deposits remain unresolved |
| Office rent, accountant/legal services, materials, publicity, bank charges, software, telecoms | Business expense candidates | Apply the separate normal/necessary, evidence, timing, allocation and capital tests above |
| COLEGIO, UNIVERSIDAD, MATRÍCULA | Itemized education candidate | Eligible institution/person/age, paid-year receipt/RIF, no reimbursement; only without standard election |
| SEGURO HCM, insurance, HOSPITALIZACIÓN | Itemized insurance candidate | Actual hospitalization/surgery/maternity cover with domiciled provider; not any life-insurance premium |
| MÉDICO, ODONTÓLOGO, CLÍNICA, HOSPITAL | Itemized medical candidate | Domestic services to eligible person; paid-year evidence, no reimbursement |
| HIPOTECA, INTERESES HIPOTECARIOS | Personal-home interest candidate | Separate principal, establish qualifying acquisition loan and apply 1,000-U.T. cap |
| ALQUILER VIVIENDA paid | Personal-home rent candidate | Actual permanent-home rent, 800-U.T. cap; not ordinary business rent |
| RESTAURANTE, COMIDA, ENTRETENIMIENTO, MERCADO, SUPERMERCADO, FARMACIA | Personal/unresolved debit | No automatic business or medical-service deduction from a label |
| MULTA, SANCIÓN, INTERÉS MORATORIO, RETIRO PERSONAL | Separate nonclaimed/unresolved debit | Do not assume an income-producing deductible expense; personal drawings excluded from cost schedule |
| PAGO ISLR, RETENCIÓN, COMPROBANTE, ANTICIPO, DECLARACIÓN ESTIMADA | Tax-payment/credit schedule | Match tax period, certificate and actual entitlement; not both expense and credit |
| IVA, SENIAT IVA | IVA reconciliation | Establish actual collected/input/remitted amounts and legal treatment separately; no universal deduction or ordinary-income assumption |
| IVSS, SEGURO SOCIAL, FAOV, INCES, unemployment or workplace risk | Payroll/parafiscal register | Distinct employee/employer bases, caps and law; no combined normal-salary percentage |
| RIF | Identification evidence | Verify taxpayer/payee registration and invoice details, not an amount or tax base |

This table operationalizes the evidence and classification tests already cited; it does not introduce a tax exemption by substring. “Credit/abono” can mean a bank deposit or an accounting recognition event; determine which. “Cargo/débito” is a debit, not necessarily a tax deduction. “Pago móvil” describes a payment method, not a tax category.

For Banesco, Banco de Venezuela (BDV), Mercantil and BBVA Provincial, read the **actual supplied export** rather than assuming a fixed PDF/CSV schema. Normalize date/value date, description, counterparty/reference, debit, credit, balance and currency; reconcile opening plus movements to closing. Preserve the original DD/MM/YYYY or other format until parsed unambiguously. Bank names and platform labels are practical intake examples; current export availability/format is unconfirmed. USD/Zelle records remain in original currency with separately evidenced conversion. This preserves the prior bank-format topic without claiming an unchanged live product specification.

### Working-paper output

Produce one reconciled schedule, not a return-ready assurance:

```text
VENEZUELA INDIVIDUAL ISLR WORKPAPER
Fiscal period: ____   Residence/domicile/source conclusion: ____
RIF / spouse property regime / dependent-person evidence: ____
Applicable UT (bolívares per unit), official ruling and close-date test: ____
Original records, completeness gaps and currency/FX method: ____
A. Gross receipts by legal category and source; nonincome transfers reconciled
B. Permitted business costs/expenses and timing, with invoice/market-price proof
C. Established employment net enrichment and bonus/exemption classification
D. Territorial/foreign operating-loss vintages, eligible use and expiry
E. Ordinary net enrichment before personal deductions; separate proportional items
F. Personal election: 774 UT OR permitted itemized education/insurance/medical/
   principal-home interest (cap1000)/home rent (cap800); paid proof and reimbursements
G. Taxable ordinary UT base; all eight marginal bands or active-band subtraction
H. Personal/family reductions: eligible persons, shared support, separate returns
I. Foreign-tax credit: income inclusion, actual paid tax, FX date and cap
J. Annual tax after valid reductions/credit, separately taxed items reconciled
K. Valid withholding and estimated advances; prior excess-payment claims
L. Payable balance or supported excess-payment claim; no automatic refund assumed
Current official return fields/calendar/payment/acknowledgement evidence: ____
Professional-review issues: classification, unit, source, election, credits, timing
```

## Deadlines and filing

LISLR art. 77 sets resident-individual annual-return tests of net enrichment over 1,000 U.T. or gross income over 1,500 U.T.; retain its separate qualifying primary-sector test over 2,625 U.T. The statutory primary-activity definition concerns direct exploitation/breeding and the permitted on-farm complementary processing, with its alcohol/pesca exclusions. Nonresident individuals declare Venezuelan enrichment/loss regardless of amount under art. 79 and the Regulation. A source withholding does not establish a general return exemption. [LISLR arts. 77, 79](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).

Art. 80 permits estimated-return requirements for specified categories whose prior-year **net enrichment** exceeded 1,500 U.T., under implementing forms/conditions/dates; it also permits alternative prior-return-based advances and special estimates for relevant extraordinary income. It does not say that every nonemployee's gross fees over that figure automatically trigger the same estimate, six instalments or biweekly calendar. Art. 85 permits specified advance arrangements up to twelve portions within a year and a possible 75% amount under executive rules. Current implementing requirements must be obtained before deciding an actual advance. At 1,490 U.T. prior net enrichment, the art. 80 **over-1,500 enabling limb** is not met; do not convert that limited result into a universal no-advance conclusion. [LISLR arts. 80, 85, 193](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17).

Arts. 77/81/82/85 send filing/self-assessment periods and procedures to the Regulation or authorized administrative rules. The old universal deadline/no-extension assertion, alternative business-year election, fixed instalment arrangement and special biweekly advances are **not confirmed** here. In particular, a 2026 close can require a later calendar; a prior-year due date is not proof of the current filing date. Obtain the actual taxpayer-specific ordinary/special-taxpayer calendar, relevant extensions and short-period instructions before quoting a date. COT art. 10 supplies working-day/continuous-month rules and nonworking-expiry extensions; it does not supply the missing calendar. [LISLR arts. 77, 80-85](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16); [COT art. 10](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3).

### Withholding, registration and submission sequence

LISLR art. 84 requires withholding where designated at payment or accounting credit, whichever first; credit means the payer's books/records recognition. Art. 196 continues Decree 1.808 pending the envisaged providencias, but does not establish the current percentage/code for a particular payment. No single professional/technical withholding rate, missing-RIF uplift, current resident payroll percentage or remittance day is adopted from the old secondary-source table. Nonresident net-liability examples below are not proof of a particular current withholding instruction. [LISLR arts. 83-85, 196](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17).

COT art. 27 makes the agent solely liable for withheld amounts and jointly liable with the taxpayer for a withholding failure; unauthorized withholding and supporting-proof conditions also apply. Reconcile the individual's actual certificates to receipts, tax period and credit; do not deduct withheld ISLR from income and again credit it against tax. An excessive advance can be requested against subsequent tax under art. 56, without prejudice to the refund right; establish the real request process rather than promising cash recovery. [COT art. 27](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=4); [LISLR arts. 56, 83](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

Before submitting:

1. Confirm RIF, residence, spouse/family facts and actual fiscal period; art. 96 requires the relevant taxpayer/withholding-agent registration. Current online registration steps, cost/free-status and validity/renewal rules were not confirmed.
2. Complete the income/source/cost and personal-deduction/credit workpaper. Match each original statement, invoice, certificate and period; identify unresolved employment interpretation and other evidence gaps.
3. Open the current authorized SENIAT return and official instructions; match its actual fields for gross/net income, deductions, family reductions, foreign credit, withholding/advances and balance. **Form names, box numbers, attachments and menu paths remain unconfirmed**; do not invent them from an old screen.
4. Establish the actual calendar and payment reference, submit through the permitted medium and preserve the return, acknowledgement and payment evidence. A prepared spreadsheet does not prove submission or settlement.

These workpaper/record instructions implement LISLR arts. 77-89/96; live portal details are not asserted as law. Direct SENIAT access and the earlier ordinary-browser visit failed on 11 November 2026; no usable dated archive instruction set was obtained. This Guide supplies an ordinary statutory calculation, not an executable current filing walkthrough. [LISLR arts. 77-89, 96](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=16).

LISLR art. 97 requires notice of the specified residence/domicile/company-seat changes within 20 days; COT art. 35 separately gives a maximum month for its listed changes. Track both where applicable under COT art. 10 instead of replacing one with the other. Departure, retained Venezuelan property and fixed-base/short-period duties remain separate questions; a flight does not establish no return or an exit-tax exemption. [LISLR art. 97](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=18); [COT arts. 10, 35](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3).

## Penalties and interest

Use the actual statutory offence, not the old approximate 100-300-times range. COT art. 103 imposes 150 highest-valued-currency exchange-rate multiples and, where premises exist, ten continuous days' closure for nonfiling or delay over one year; an incomplete or up-to-one-year late return attracts 100 multiples. Its listed missing/incomplete/late communications, substitute-return and unauthorized-medium offences attract 50 multiples. A missing low-tax information return has its separate 2,000-multiple/closure sanction and a late return 1,000 multiples. Closure applies to all establishments/branches. Art. 108 increases relevant chapter **formal pecuniary sanctions by 200%**, resulting in three times the ordinary fine for designated special taxpayers; it is not a general multiplier for material offences. [COT arts. 103, 108](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=13).

COT art. 110's ordinary no-extension/no-stated-audit late payment is 0.28% per day up to 100% within the first year, with an additional 50% after one year and additional 150% after two years. Payment in audit/determination is routed as applicable to art. 112, and an obtained extension excludes these art. 110 sanctions. Art. 112 generally gives 100%-300% of omitted tax for illegitimate tax-revenue reduction, without prejudice to art. 119; its limited property-valuation exception and conditional 30% accepted-and-paid-assessment route under arts. 195-196 are not universal discounts. The latter route requires filing/rectification/payment within art. 195's fifteen working days after notice; interest and other applicable fines remain, and a partial acceptance/payment limits that treatment to the accepted/paid portion. [COT arts. 110, 112, 195-196](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=14).

Withholding failures are separate under art. 115: ordinary nonpublic-agent nonwithholding 500% of unwithheld tax, short withholding 100% of shortfall, late remittance 5% per day for at most 100 days, then the specified 1,000% nonremittance/criminal-consequence route. Verification/audit and express public-agent exceptions matter; accepting an assessment does not remove art. 115's sanctions. Do not substitute these rates for an individual's ordinary late annual payment. [COT art. 115](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=15).

COT art. 66 charges automatic late-payment interest from the payment deadline to discharge at **1.2 times the applicable active bank rate**, with the BCV prior-month six-largest-bank average, excluded preferential portfolios and publication/fallback conditions. Actual period rates are needed. Arts. 91-92 use the highest-valued officially quoted currency, not an assumed USD or UT: fixed multiples use payment-date exchange value, while percentage fines translate at the offence date then settle at payment-date value. Actual rates/dates remain inputs. Live enforcement should receive professional legal review. [COT arts. 66, 91-92](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=9).

## Cross-border points

Foreign income remains subject to the residence/source tests, not automatic exclusion. Art. 2 credits qualifying foreign income tax **actually paid** on included foreign-source income up to Venezuelan global tax multiplied by foreign net enrichment divided by global net enrichment; separately proportional items have their own Venezuelan-item cap. Use payment-date FX for the tax paid, distinct from art. 16's average-year foreign-gross-income conversion. Keep assessment, payment receipt, income inclusion and source mapping; no excess-credit carryforward/refund is invented. Treaty relief requires art. 3 evidence and the actual treaty. [LISLR arts. 1-4, 16](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

A nonresident individual's ordinary 34% applies to the legal net base. Art. 39 gives noncommercial professional enrichment a 90%-of-gross base without prejudice to art. 41; the printed art. 31 treats dependent-service consideration as net enrichment, subject to the unresolved current employment interpretation above. A technical-assistance/technological/royalty classification, PE/fixed base, separately taxed dividend or other specialist case can change the base/regime and needs its actual law. Do not assign a resident standard deduction, ordinary company tariff, automatic treaty exemption or a guessed administrative withholding percentage. The separate cross-border Guide is tracked through [PR #1452](https://github.com/openaccountants/openaccountants/pull/1452); it is not treated as main coverage until merged. [LISLR arts. 31, 39-50, 64-76](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=12).

### Separate payroll and parafiscal register

Preserve separate questions for **IVSS**, **employment/unemployment insurance**, **FAOV housing**, **INCES training** and **LOPCYMAT workplace risk**. For each, establish employee/employer obligation, covered person, applicable wage/benefit base, cap, period and actual current primary rate before calculation. INCES profit-sharing/benefit questions are distinct from monthly payroll. The old combined percentage on normal wages is not a valid computation where component bases differ. This income-tax Guide does not establish the contribution figures or a deduction from employment net enrichment by listing these regimes.

The existing [social-contributions](venezuela-social-contributions.md) and [payroll](venezuela-payroll.md) Guides are still on 2025 at this baseline and need separate source-based updates; do not use their historical figures as 2026 evidence. Current IVSS risk-class rates/normal-wage cap, employment-insurance rates/cap, FAOV integral-wage base/cap, INCES employee profit-sharing/employer-payroll bases and LOPCYMAT risk rates/implementation remain **not yet confirmed** here. The same applies to statutory minimum wage and any indexed economic income floor; neither a historical wage amount nor an executive bonus label establishes a current contribution cap. IVA is a separate tax: [the IVA Guide](venezuela-iva.md) is also being updated independently, and no current rate or small-taxpayer exemption is supplied from the old personal-income example.

## Two worked examples that recompute

### Example 1: resident standard deduction and family reductions

Assume legally established ordinary net enrichment before personal deductions of 20,000 U.T., no additional business costs/losses, resident status, a valid 774-U.T. standard election, and a spouse not separated as to property plus two qualifying supported resident minor children. There are no separate declarations, shared-support adjustments, foreign credit or proportional items. Taxable enrichment is 19,226 U.T.; tariff tax is 5,661.84 U.T.; the four 10-U.T. reductions total 40 U.T., leaving 5,621.84 U.T. before advances. For an illustrative validated advance of 100 U.T., payable tax is 5,521.84 U.T. The former 5,300-bolívar withholding scenario can instead be reconciled as `5621.84 × confirmed U - 5300` only once the actual UT and the certificate are established; no current UT amount is assumed. [LISLR arts. 50, 58-59, 83](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

```oa-check
name: Resident standard deduction family reductions and advances in tax units
inputs:
  net_enrichment_ut: 20000
  standard_ut: 774
  eligible_persons: 4
  validated_advance_ut: 100
steps:
  - taxable_ut: net_enrichment_ut - standard_ut
  - tariff_tax_ut: taxable_ut * 0.34 - 875
  - reductions_ut: eligible_persons * 10
  - annual_after_reductions_ut: tariff_tax_ut - reductions_ut
  - payable_ut: annual_after_reductions_ut - validated_advance_ut
expected:
  taxable_ut: 19226
  tariff_tax_ut: 5661.84
  reductions_ut: 40
  annual_after_reductions_ut: 5621.84
  payable_ut: 5521.84
```

### Example 2: itemized rent cap and the election decision

Assume resident ordinary net enrichment of 8,000 U.T., documented qualifying permanent-home rent of 13,953.49 U.T. and eligible education of 2,000 U.T. paid domestically in the year, with proper receipts/RIF, no reimbursements or business double deduction. Rent is capped at 800 U.T.; itemized deductions are 2,800 U.T.; taxable income is 5,200 U.T. and tariff tax 933 U.T. The 774-U.T. alternative gives taxable income 7,226 U.T. and tariff tax 1,581.84 U.T., so valid itemization saves 648.84 U.T. before equal personal reductions. If the education/rent evidence fails, do not choose this itemized result merely because it is lower. [LISLR arts. 50, 57-58](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

```oa-check
name: Valid itemized rent and education compared with the standard election
inputs:
  net_enrichment_ut: 8000
  paid_rent_ut: 13953.49
  eligible_education_ut: 2000
steps:
  - rent_allowed_ut: min(paid_rent_ut, 800)
  - itemized_ut: rent_allowed_ut + eligible_education_ut
  - itemized_base_ut: net_enrichment_ut - itemized_ut
  - itemized_tax_ut: itemized_base_ut * 0.29 - 575
  - standard_base_ut: net_enrichment_ut - 774
  - standard_tax_ut: standard_base_ut * 0.34 - 875
  - itemization_saving_ut: standard_tax_ut - itemized_tax_ut
expected:
  rent_allowed_ut: 800
  itemized_ut: 2800
  itemized_base_ut: 5200
  itemized_tax_ut: 933
  standard_base_ut: 7226
  standard_tax_ut: 1581.84
  itemization_saving_ut: 648.84
```

### Preserved scenario checks

The prior Guide's remaining tests are retained with their legal limits. These are hypothetical arithmetic, not current administrative withholding instructions or currency-unit assertions.

```oa-check
name: Bottom band and taxpayer reduction
inputs:
  net_enrichment_ut: 1500
steps:
  - taxable_ut: net_enrichment_ut - 774
  - tariff_tax_ut: taxable_ut * 0.06
  - after_taxpayer_reduction_ut: tariff_tax_ut - 10
expected:
  taxable_ut: 726
  tariff_tax_ut: 43.56
  after_taxpayer_reduction_ut: 33.56
```

For a nonresident noncommercial professional without PE/fixed base, established technical-service classification or treaty relief, the old hypothetical 200,000-unit fee gives the art. 39/50 liability below. For a legally established ordinary taxable employment amount of 500,000 currency units, the 34% arithmetic is also retained, but it does not resolve the bonus/employment-base interpretation or the current withholding instruction. [LISLR arts. 31, 39, 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=12).

```oa-check
name: Nonresident professional base and separately established employment base
inputs:
  professional_gross: 200000
  established_employment_net: 500000
steps:
  - professional_base: professional_gross * 0.90
  - professional_liability: professional_base * 0.34
  - employment_liability: established_employment_net * 0.34
expected:
  professional_base: 180000
  professional_liability: 61200
  employment_liability: 170000
```

```oa-check
name: Exact 6000 tax-unit boundary with taxpayer reduction
inputs:
  taxable_ut: 6000
steps:
  - lower_band_tax_ut: taxable_ut * 0.29 - 575
  - upper_band_tax_ut: taxable_ut * 0.34 - 875
  - after_taxpayer_reduction_ut: lower_band_tax_ut - 10
expected:
  lower_band_tax_ut: 1165
  upper_band_tax_ut: 1165
  after_taxpayer_reduction_ut: 1155
```

At 1,490 U.T. prior net enrichment, the art. 80 over-1,500 enabling test is not met; current category/other-advance rules remain separate as explained under filing. The old receipt-only professional example remains: a documented 860,000-currency-unit service receipt is reconciled to the invoice and actual IVA first, then divided by the **confirmed** UT; no assumption that “no IVA charged” means an exemption. The old food-bonus receipt example is retained as a classification register item, not an automatic exempt-income result. The old withholding certificate example remains a tax-on-account credit subject to actual evidence, not an expense. [LISLR arts. 16, 31, 80, 83](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=8).

## Ask the client first

1. What is the actual tax period, RIF and residence/domicile conclusion, including current/prior-calendar-year presence, home, citizenship and foreign residence evidence? Is there a Venezuelan fixed base or a treaty claim?
2. Provide all bank/platform statements, invoices/contracts, employer gross-benefit and withholding statements, other income/asset records and source/currency details. Which receipts are own transfers, loans, capital, refunds or separately taxed income?
3. For employment, identify food/travel benefits, ordinary/extraordinary bonuses, indemnities/pensions and the actual primary legal interpretation supporting each inclusion/exclusion. A name in the bank memo is insufficient.
4. Provide documented business costs/expenses, mixed-use allocation, prior source-specific loss vintages and inflation issues; then identify standard versus eligible itemized personal deductions, paid-year receipts/RIF and any reimbursement.
5. What are the spouse/property/separate-declaration facts, eligible supported ascendants/descendants, their age/residence/study/disability status and shared support? Provide actual withholding/advance and foreign-tax-paid evidence.
6. Provide the fiscal-close UT ruling, applicable FX evidence, current return/calendar and special-taxpayer notice, plus prior definitive/estimated returns, residence/domicile changes and any late filing/payment. Which final filing/credit/refund steps remain unsupported?

### Onboarding fallback and when to refuse or refer

With incomplete answers, prepare a **provisional** record reconciliation and a specific missing-evidence list; do not invent residence, a zero business-use allocation, a deductible category, spouse/dependent entitlements, an exemption or a current UT. Do not silently elect a personal method without the required facts. The standard alternative does not justify a final return based on bank records alone.

Stop a final amount where residence/source, current unit, legally established employment base, expense/credit evidence or current required procedure is missing. Refer companies/member allocations, live enforcement, disputed salary/bonus interpretation, treaty/PE questions, complex inflation or multicurrency issues and IVA/payroll calculations to their separately sourced work. Preserve a supported U.T. calculation where possible and identify precisely what prevents conversion or filing. This retains the old refusal/prohibition topics without unsupported automatic defaults.

## Sources

| Primary source | Official URL | Read on | Exact native wording and extent read |
|---|---|---|---|
| LISLR, official Gaceta 6.210 Extraordinario, 30 December 2015 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf | 2026-11-11 | Consolidated personal provisions and neighbors: arts. 1-32, 39-60, 64-89, 96-97, 171, 181, 186, 193, 196. Tarifa 1 visually read on PDF page 13, including the 6%/9% cells missing from text extraction; its eight rows are explicitly transcribed in review evidence. Art. 58: “setecientas setenta y cuatro unidades tributarias (774 U.T.)”; art. 59: “diez (10) unidades tributarias”; art. 31: “independientemente de su carácter salarial, distintas de viáticos y bono de alimentación”. Current judicial interpretation is not established from this printed sentence alone. |
| COT, official Gaceta 6.507 Extraordinario, 29 January 2020 | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf | 2026-11-11 | Arts. 3, 10, 27, 30, 35, 66, 91-92, 103, 108, 110, 112, 115, 195-196 and relevant neighbors read. Art. 3: “la unidad tributaria aplicable será la que esté vigente al cierre del ejercicio fiscal respectivo”; art. 103: “por un plazo de diez (10) días continuos”. Native extraction headers/duplicates are excluded from quotation evidence only after printed-source checks. |

**Not yet confirmed:** current fiscal-close UT bolívar value/effective-date evidence and historical UT currency/increase claims; current controlling judicial/administrative interpretation of employment, bonuses and named benefits under art. 31, including the inaccessible official TSJ text; domestic foreign-currency conversion rules/rates not established by arts. 2/16; specific 2026 sector/personal exonerations; current annual/short-period/alternative-year calendars, extensions, estimated/special-taxpayer advances and instalments; actual SENIAT return/registration fields, fees, acknowledgements, attachments and payment/credit/refund procedures; current withholding tables/codes, missing-RIF effects and remittance schedules; current depreciation tables, INPC/implementation and art. 186 interpretation; actual IVSS, employment-insurance, FAOV, INCES and LOPCYMAT rates/bases/caps and current wage/economic-floor inputs; current IVA rate/exemption for a specific invoice; bank-specific export formats; treaty-specific status/rates and other specialist bases; actual BCV penalty/interest rates and treatment of personal reductions exceeding tax. These topics remain in this Guide or its explicit referrals rather than being silently dropped. No missing figure is filled from memory or a secondary summary.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `venezuela-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/venezuela-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
