---
name: td-income-tax
description: "Prepare Chad personal income working papers for 2026 from salary, ordinary positive business and professional bases, and separate rental and other capital categories. Covers fiscal domicile, documented salary allowances and mandatory deductions, marginal annual bands, BIC expense adjustments, BNC receipts and spouse limits, IGL routing, business reporting and collection evidence. Use for Chad IRPP, self-employment, professional fees, salary, rent or resident intake. Four cases recompute salary, category separation and positive BIC/BNC bases. Final personal settlement, individual losses, conflicting filing rules, special agriculture and deleted global-income provisions remain explicit holds; this is a partial preparation method."
jurisdiction: TD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.2
---

# Chad personal income tax v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with employment, business/professional, property or investment income connected with Chad. For 2026, CGI article 1 separates labour income from capital income; article 9(II) aggregates net labour categories for the progressive scale. This Guide computes the ordinary annual labour scale after the category bases have been established, develops the salary base, and separates net rent and other capital income. It also develops ordinary positive business and professional category bases below. It does not complete the final personal tax settlement or a property-disposal gain calculation. [Finance law 2026, arts 3–4](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=3); [CGI arts 8–9](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=9).

Subject to international conventions, fiscal domicile brings Chad and foreign income into the relevant categories. Domicile tests are alternatives: a home available as owner/usufructuary or tenant (lease or successive leases at least one year), principal stay, economic interests, and the specific government-service/departure situations in article 2. The text contains both more than 183 days in twelve months and more than 183 days in a year: do not reduce residence to a single calendar-day test. A nonresident is taxable on Chad income; salary article 44(II) has its own source conditions. Resolve any conflicting residence/treaty conclusion before computing. [CGI art 2, carried forward by LF art 4](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4).

## Rates, bands and thresholds

Tax year: 2026. Amounts are XAF (FCFA). Bands below are marginal, applied to annual net labour income, not to gross pay or capital income.

| Item and condition | Rate or amount | Official source |
|---|---|---|
| Labour income up to 800,000 | 0% | [LF art 3, CGI art 1(IV)](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Labour slice over 800,000 to 6,000,000 | 10.5% | [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Labour slice over 6,000,000 to 7,500,000 | 15% | [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Labour slice over 7,500,000 to 9,000,000 | 20% | [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Labour slice over 9,000,000 to 12,000,000 | 25% | [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Labour slice above 12,000,000 | 30% | [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Net capital income, per category, excluding rent | 15% | [LF art 3, CGI art 1(V)](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Individual's net rental-income category | 10% | [LF art 3, CGI art 1(V)](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4) |
| Transport allowance, only where it benefits all personnel | Exempt up to 30% of each employee's monthly basic salary | [CGI art 45(13), retained by LF art 8](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=16) |
| Special expense allocations actually used for their employment purpose | Exempt only within 15% of aggregate salaries plus those allocations | [CGI art 45(2), LF art 8](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=15) |
| Mandatory pension/retirement deductions | Limit 3.5% of remuneration; mandatory social-security deductions separately deductible | [CGI art 47](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=23) |

### Business regime and professional limits

Determine the business regime before applying a net-profit scale. The salary scale is not an IGL turnover tax.

| Business/professional condition | Figure or rule | Official source |
|---|---|---|
| Ordinary BIC RSI, subject to special activity rules | Annual turnover excluding tax at least 50million and below 500million; exact 500million boundary held | [CGI38–40,999](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| Natural-person IGL, not already real/RSI and outside special activity rules | Turnover below 50million; own listed IRPP/VAT/patente/employer/training taxes substituted, third-party withholding retained | [CGI31,37](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category A / B qualifying ordinary activity | A:30million to below50million; B:20million to below30million; 5% of declared turnover | [CGI31,33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category C, N'Djamena Zone1 only |15million to below20million:850,000 | [CGI32–33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category D, same Zone1 condition |10million to below15million:600,000 | [CGI32–33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category E, same Zone1 condition |5million to below10million:350,000 | [CGI32–33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category F, same Zone1 condition |3million to below5million:160,000 | [CGI32–33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| IGL category G, same Zone1 condition |2million to below3million:40,000 | [CGI32–33](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| BNC studies/assistance fees paid to persons outside CEMAC |Deduct within 10% of turnover, not the BIC head-office profit cap | [CGI53(II)(3)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| BNC spouse remuneration, actual work required |Deduct up to60,000 a month | [CGI53(II)(4)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |

Article32 defines other zones but its recovered fixed-tariff table only shows Zone1. Other-zone fixed tariffs, below-category-G cases and special livestock-export/vehicle regimes under34–35 remain held. Do not extrapolate these fixed amounts to all Chad businesses.

## The base

1. Establish each category separately. Labour includes salaries, taxable industrial/commercial/agricultural/mining and artisanal profit, majority-manager remuneration, and noncommercial professional profit. Capital includes property income and financial income. Assess spouses separately on their own income; for community income use their legal shares, or one half each if no allocation rule exists. [CGI arts 1, 4, 9](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=7); [LF arts 3–4](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=3).
2. Salary working paper: reconcile cash pay, bonuses, indemnities and benefits to contracts and payroll. Residents' salary is taxable even where the employer/activity is abroad. For a person domiciled abroad, article 44 requires both activity in Chad and employer domiciled/established there. A broader nonresident or treaty question requires separate analysis. [CGI art 44](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=22).
3. Remove only a documented article 45 exemption. Transport and employment-expense allocations have the conditions in the table. Pensions are exempt under article 45(1). Disability salary exemption is now article 45(18), with disability defined by the Labour Code and ILO texts: LF article 5's deletion from article 3 is not abolition, because LF article 8 reinstates it in article 45. The unchanged article 3(4) separately exempts salaries of graduates under 35 and workers recruited by real-regime enterprises for five years; establish its precise eligible recruitment facts before using it. [LF arts 5, 8](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=6); [CGI art 3(4)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=8).
4. Add taxable benefits valued under article 46, then deduct actual mandatory social-security contributions and qualifying compulsory retirement deductions within article 47's limit. Do not treat 3.5% of uncapped gross salary as an automatic deduction. Benefits with high-standard housing or cash-substitution issues require a separate article 46 valuation working paper. [CGI arts 46–48](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=23).
5. Sum established net labour categories and apply the marginal bands. Do not apply the top band to all income. Keep capital categories outside that sum. [CGI art 9(II)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=9); [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4).
6. For ordinary unfurnished property income outside a business, CGI articles 12–14 start with collected gross receipts, tenant-paid owner expenses and relevant subsidies; net property income is gross less qualifying property charges. Article 14 allows a 30% flat charge deduction for ordinary property, or justified actual costs; the special article 10(1)(d) ownership-right income instead has a 5% flat allowance. Article 15 carries a property deficit against the next five years' net income. Do not use the ordinary allowance for furnished lettings or business property without first classifying under articles 10 and 17. [CGI arts 10–17](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=10).
7. Apply 10% to established individual net rent and 15% to other established net capital categories. Withholding is a separate collection step: LF article 15 changes rental prepayment to 10% for individuals and 15% for legal persons; equipment hire retains its distinct wording. Reconcile certificates before concluding the final balance; this Guide's examples are gross category tax before credits, not an instruction to charge both tax and withholding cumulatively. [LF arts 3, 14–15](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=21).

### Ordinary positive business and professional categories

8. **BIC classification and records.** Articles16–17 cover individual commercial, industrial, artisan and agricultural profit, including specified property dealing, furnished/business-equipment lettings and farming. Classify those receipts before using the ordinary property allowance. Members' allocated profit under5/42 and majority-manager remuneration under43 have separate rules; do not treat every manager as a sole trader or give every manager an automatic expense allowance. Agricultural regimes under21–24 differ from general turnover boundaries; do not force every farmer into the ordinary table. [CGI5,16–24,42–43](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
9. **BIC profit bridge.** Articles19–20/25 use period results and a net-assets bridge adjusted for capital contributions and drawings, not a universal cash-in/cash-out shortcut. Include business disposal results; stocks use lower cost/closing market and work in progress cost. Apply article26's five cumulative expense conditions and its activity-specific caps/disallowances. Those article26 rules are individual BIC rules, imported by company article134, so the [corporate Guide's article26 working-paper detail](td-corporate-income-tax.md) can be reused only where its predicate applies. Do not import company tax rates,20,000 profit rounding or article134's corporate loss rule into personal IRPP. Gain reinvestment/drawings under29–30 and special agriculture remain separate analyses. [CGI19–30,134](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
10. **BNC receipts.** For an ordinary permanently established professional under49, reconcile fee receipts, actually collected advances, replacement fees and noncash consideration. Separate genuine client third-party disbursement advances in a distinct account; incidental reimbursements/subsidies linked to the profession are not automatically exempt. These are article50–52 rules, not a universal election between cash and accrual. Unpaid/uncertain-right cases need separate analysis. [CGI49–52](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
11. **BNC expenses.** Start from total receipts less expenses necessary for the profession under53, including its specified professional gains/cessation indemnities. Support actual professional rent, eligible asset depreciation, training/research/events, and taxes other than IRPP. Apply its own foreign studies/assistance and spouse limits from the table; spouse-training deductions additionally need effective exclusive collaboration, direct training/activity link and business interest. Do not substitute BIC article26 caps by analogy. Article54 excludes personal/nonbusiness/sumptuary spend, asset purchase principal, loan principal/investments and criminal fines. Capital assets use supported depreciation rather than immediate capital deduction. Literary/artistic/scientific averaging and professional gains under55–56 are special, not a consultant-wide option. [CGI53–56](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
12. **Regime and final-balance gates.** BNC57–58 has its own real/RSI wording, including an express lower-RSI VAT authorisation in58(II). Do not use a broad general-registration assumption for that case. Carry a supported positive net labour category to the article9(II) labour sum only after regime/exemption is established; do not add IGL turnover to the progressive base. For real/RSI individual activities16–17,149–152 also requires a separate minimum-fiscal working paper using the [corporate Guide's minimum rule](td-corporate-income-tax.md). Pure49BNC scope is not established by149's16–17 wording. Article152 credits annual minimum against annual IRPP, but allocation against aggregate labour and priority with collection credits is not resolved here. Keep final settlement held. [CGI31,37–40,57–58,149–152](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
13. **Loss and collection control.** LF18 deletes the whole former Revenu global subsection96–108, including96's old business-loss bridge. Do not re-import the corporate carryforward as a settled individual loss rule. Track article120 prepayments, Treasury121 and professional124 collection separately using the actual registered-taxpayer predicates and certificates. LPF L.147 requires invoice date/number, withholding payer, gross and withheld amount attached to the annual declaration; missing support prevents the deduction. The statutory surplus treatment and interaction with other credit rules remain held, rather than promised as a refund. [LF16–18](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=23); [CGI861–863 and LPF L.147](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

## Deadlines and filing

Employer collection is monthly under CGI article 847, using the administration's payroll scale. Remit by the 15th of the following month under article 848. Article 849 requires an e-TAX-generated declaration and a notified copy recording the date, unique declaration number and administration logo. Reconcile the month's taxable base, withholding, submitted declaration, payment and acknowledgement. The administration's live payroll scale and current screen/field identifiers have not been obtained; do not fabricate a monthly rounding or annualisation convention. [CGI arts 847–850](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=167).

Article 986 requires employers' annual named salary statement during January, with identity/address/job, pay after pension deductions, benefits, withheld IRPP and payment period. Article 987 requires individual detail above annual remuneration of 60,000 and aggregate reporting below that figure. Foreign-pay recipients domiciled in Chad supply corresponding information under article 994. [CGI arts 986–994](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=189).

For an individual's annual declaration, articles 983–985 require income by nature, foreign receipts separately and the administration's signed form to the residence tax office. The reviewed text here does not establish a general 30 April IRPP deadline. Obtain the current applicable annual calendar/form before filing. Individual business/professional declarations have the separate rules in the paragraphs below; the corporate Guide does not supply their final personal settlement. [CGI arts 983–985](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=188).

Ordinary calendar-year BIC real/RSI: articles998–1000/1005–1006 require results within four months (ordinary30April), DSF/support and the applicable books;1004 requires CEMAC-approved expert validation. This does not make the corporate31May payment deadline a personal payment rule. BNC1002 specifically requires the first two months of the year, including58RSI and57real, while other cross-references point toward four months; obtain an office resolution of that conflict rather than promising a single BNC filing date. Keep a daily BNC journal and vouchers under1002–1003. [CGI998–1006](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

IGL1011 requires activity declaration within30days and prior turnover declaration by28February, with assessment/payment at filing; article31's year-end wording is not permission to delay that filing payment. Minimum-fiscal842 expressly distinguishes normal monthly and RSI quarterly payment, but152 contains conflicting monthly wording. Ordinary final personal settlement, IGL special tariffs and live forms remain unresolved. [CGI31,842,1011](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

## Penalties and interest

Employer withholding retained but not remitted within article 848's deadline attracts 1.5% for each month or part, capped at 50%, under article 1042; prosecution is separately preserved. Assessment omissions/inaccuracies attract article 1038's 1.5% monthly interest with its own start/end calculation. Failure to declare after notice triggers article 1039's assessed tax plus 100%, 150% for repeat failure, and interest; article 1040 caps that non-declaration interest at 50%. Do not mechanically add assessment and recovery charges for the same period: article 1044 governs recovery after an assessment notice on a different base and timeline. [CGI arts 1038–1044](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=204).

## Cross-border points

Retain both residence and source evidence, the applicable convention and foreign tax certificates. Article 117(III–IV)'s separate foreign financial-income relief requires a convention and actual foreign tax, and excludes cases with exemption or refund under it. LF article18 deletes the entire former Revenu global subsection, which extends through CGI108. The former article105 five-times rental-value floor and articles106–108 departure rules therefore cannot be used as current operative rules. Their replacement or interaction with surviving residence and cessation provisions remains held; do not infer nonresident liability solely from salary. Treaty-by-treaty entitlement, credits, PE questions, nonresident professional withholding and exit calculations remain outside this computation. [CGI art117](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF art18](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=25).

## Two worked examples that recompute

### Salary after verified mandatory contributions

Taxable cash plus already-valued benefits is 8,000,000. Payroll documents establish 280,000 of deductible mandatory social contributions; no exemption or other category applies. Net labour income is 7,720,000. The first taxable slice gives 546,000, the next 225,000 and the last 44,000: annual gross IRPP is 815,000. The contribution is an input supported by documents, not a new CNPS rate rule.

```oa-check
name: Salary with actual mandatory deduction
inputs:
  remuneration: 8000000
  mandatory_contribution: 280000
steps:
  net: remuneration - mandatory_contribution
  slice_105: max(0, min(net, 6000000) - 800000) * 0.105
  slice_15: max(0, min(net, 7500000) - 6000000) * 0.15
  slice_20: max(0, min(net, 9000000) - 7500000) * 0.20
  slice_25: max(0, min(net, 12000000) - 9000000) * 0.25
  slice_30: max(0, net - 12000000) * 0.30
  tax: slice_105 + slice_15 + slice_20 + slice_25 + slice_30
expected:
  net: 7720000
  tax: 815000
```

### Decide which category a receipt belongs in

A resident has established net labour income 12,000,000, net ordinary rent 2,000,000 and other net capital income 1,000,000. Apply the labour scale to labour only: 1,821,000. Rent is 200,000 and other capital is 150,000. Gross category tax is 2,171,000 before withholding/credits. Combining every receipt into labour would produce 2,721,000, overstating this working paper by 550,000; that comparison is an error check, not an election. The decision turns on the actual nature of the income.

```oa-check
name: Labour versus separate rent and capital categories
inputs:
  labour: 12000000
  net_rent: 2000000
  other_net_capital: 1000000
steps:
  labour_tax: (6000000 - 800000) * 0.105 + 1500000 * 0.15 + 1500000 * 0.20 + (labour - 9000000) * 0.25
  rent_tax: net_rent * 0.10
  capital_tax: other_net_capital * 0.15
  gross_tax: labour_tax + rent_tax + capital_tax
  incorrect_combined: labour_tax + (net_rent + other_net_capital) * 0.30
  overstatement: incorrect_combined - gross_tax
expected:
  labour_tax: 1821000
  gross_tax: 2171000
  incorrect_combined: 2721000
  overstatement: 550000
```

### Ordinary BIC positive category base

A documented RSI trader has turnover80,000,000, other allowable same-period costs49,200,000 and bank-paid hospitality800,000. The article26 hospitality limit is400,000. Personal spend1,000,000 and a600,000cash-paid expense are excluded; neither is in the allowable-cost input. Net BIC is30,400,000. This stops at the category base: no minimum/withholding credit is subtracted from profit, and final personal balance is held.

```oa-check
name: BIC documented expense limits before personal settlement
inputs:
  turnover: 80000000
  other_allowable_costs: 49200000
  hospitality_paid: 800000
  personal_spend: 1000000
  cash_expense: 600000
steps:
  hospitality_cap: turnover * 0.005
  hospitality_allowed: min(hospitality_paid, hospitality_cap)
  hospitality_disallowed: hospitality_paid - hospitality_allowed
  excluded_costs: personal_spend + cash_expense + hospitality_disallowed
  positive_bic: turnover - other_allowable_costs - hospitality_allowed
expected:
  hospitality_allowed: 400000
  excluded_costs: 2000000
  positive_bic: 30400000
```

### BNC client funds and actual spouse work

An ordinary RSI professional receives fees60,000,000 and a separate2,000,000genuine client-disbursement deposit held in the client account. Paid business rent is6,000,000, other justified professional costs30,000,000 and actual spouse services120,000monthly. Only60,000monthly spouse pay is allowed,720,000annual. Personal spend600,000is excluded and outside the allowed-cost input. Net BNC is23,280,000; including client funds as fees or all spouse pay would be wrong. No disputed accrual, nonresident or final-credit facts are assumed.

```oa-check
name: BNC genuine client deposit and spouse deduction limit
inputs:
  fee_receipts: 60000000
  separate_client_deposit: 2000000
  rent_paid: 6000000
  other_professional_costs: 30000000
  spouse_monthly_paid: 120000
  months: 12
steps:
  total_cash_received: fee_receipts + separate_client_deposit
  professional_receipts: total_cash_received - separate_client_deposit
  spouse_allowed: min(spouse_monthly_paid, 60000) * months
  spouse_disallowed: spouse_monthly_paid * months - spouse_allowed
  positive_bnc: professional_receipts - rent_paid - other_professional_costs - spouse_allowed
expected:
  professional_receipts: 60000000
  spouse_allowed: 720000
  spouse_disallowed: 720000
  positive_bnc: 23280000
```

## Ask the client first

- Where were homes available, stays, personal/economic interests and assignments during the relevant year and twelve-month periods?
- Which receipts are salary, business/professional profit, rent, property gains or financial income, and where did each arise?
- What cash pay, benefits, actual compulsory contributions and evidence of each claimed allowance/exemption exist?
- Are there furnished/business properties, losses, community property, departure events or special employment statuses?
- Which payroll/annual declarations, withholding certificates, foreign taxes and convention claims already exist?

## Sources

| Primary source | Read on | Actual scope read |
|---|---|---|
| [Enacted finance law 2026, law 008/AN-SENAT/2025](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) | 2026-11-01 | Arts 1, 3–5, 8, 13–18; printed pp 1, 3–6, 15–16, 21–22; original/new blocks and adjacent clauses, bands and exemptions visually inspected |
| [Official CGI 2025, dated archive of ministry PDF, captured 2025-07-20](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) | 2026-11-01 | Arts 2–60, 96–108 (historical deleted subsection only), 117, 149–152, 861–863, LPF L.147, 998–1011, 847–850, 983–994, 1038–1044; salary/property bases, residency, filing and penalties. Baseline reconciled with the listed 2026 amendments; not a whole-code review |

Not yet confirmed: agricultural regime gaps, special business/professional gains, below-category-G/other-zone/special IGL tariffs, BNC filing-period conflict and complete final personal settlement, property-disposal gain bases and special reliefs; complete benefit valuation where article 46's cash and housing provisions interact; live administration payroll scale, monthly rounding, IRPP annual due date and form/box/payment-reference workflow; complete treaty, foreign-credit, nonresident professional and exit computations, including replacement of the deleted CGI96–108 global-income/housing/departure provisions; interactions between the 2026 category approach and older global-income deductions/credits. These gaps keep IT-IND partial. The 2026 deletion of96–108 supersedes earlier ledger30’s operative105housing/departure claim. Article117(I) references to deleted98–99/global-income credits are held; only separately bounded117(III–IV) foreign-financial provisions are used above. Historical2025figures are not independent evidence of current law. For independent AI source review and its limits, see the [country README](README.md). No accountant attestation.

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
