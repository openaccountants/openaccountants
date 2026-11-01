---
name: td-income-tax
description: "Compute Chad personal income tax for 2026 from established net labour categories, separate ordinary rental and other capital income, and build a documented salary base. Covers fiscal domicile, Chad and foreign salary, conditional allowance exemptions, mandatory contribution deductions, marginal annual bands, employer withholding and the annual salary statement. Use for Chad IRPP, taxable salary, transport allowance, rental income, investment income or resident versus nonresident intake. It produces a gross-tax working paper before collection credits. Business-profit bases, disposal gains, live payroll tables, complete treaty relief and the individual annual filing calendar remain explicit gaps; the pack remains partial and this is not a filing-ready return."
jurisdiction: TD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.1
---

# Chad personal income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with employment, business/professional, property or investment income connected with Chad. For 2026, CGI article 1 separates labour income from capital income; article 9(II) aggregates net labour categories for the progressive scale. This Guide computes the ordinary annual labour scale after the category bases have been established, develops the salary base, and separates net rent and other capital income. It does not complete a BIC/BNC return or calculate a property's disposal gain. [Finance law 2026, arts 3–4](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=3); [CGI arts 8–9](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=9).

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

## The base

1. Establish each category separately. Labour includes salaries, taxable industrial/commercial/agricultural/mining and artisanal profit, majority-manager remuneration, and noncommercial professional profit. Capital includes property income and financial income. Assess spouses separately on their own income; for community income use their legal shares, or one half each if no allocation rule exists. [CGI arts 1, 4, 9](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=7); [LF arts 3–4](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=3).
2. Salary working paper: reconcile cash pay, bonuses, indemnities and benefits to contracts and payroll. Residents' salary is taxable even where the employer/activity is abroad. For a person domiciled abroad, article 44 requires both activity in Chad and employer domiciled/established there. A broader nonresident or treaty question requires separate analysis. [CGI art 44](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=22).
3. Remove only a documented article 45 exemption. Transport and employment-expense allocations have the conditions in the table. Pensions are exempt under article 45(1). Disability salary exemption is now article 45(18), with disability defined by the Labour Code and ILO texts: LF article 5's deletion from article 3 is not abolition, because LF article 8 reinstates it in article 45. The unchanged article 3(4) separately exempts salaries of graduates under 35 and workers recruited by real-regime enterprises for five years; establish its precise eligible recruitment facts before using it. [LF arts 5, 8](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=6); [CGI art 3(4)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=8).
4. Add taxable benefits valued under article 46, then deduct actual mandatory social-security contributions and qualifying compulsory retirement deductions within article 47's limit. Do not treat 3.5% of uncapped gross salary as an automatic deduction. Benefits with high-standard housing or cash-substitution issues require a separate article 46 valuation working paper. [CGI arts 46–48](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=23).
5. Sum established net labour categories and apply the marginal bands. Do not apply the top band to all income. Keep capital categories outside that sum. [CGI art 9(II)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=9); [LF art 3](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=4).
6. For ordinary unfurnished property income outside a business, CGI articles 12–14 start with collected gross receipts, tenant-paid owner expenses and relevant subsidies; net property income is gross less qualifying property charges. Article 14 allows a 30% flat charge deduction for ordinary property, or justified actual costs; the special article 10(1)(d) ownership-right income instead has a 5% flat allowance. Article 15 carries a property deficit against the next five years' net income. Do not use the ordinary allowance for furnished lettings or business property without first classifying under articles 10 and 17. [CGI arts 10–17](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=10).
7. Apply 10% to established individual net rent and 15% to other established net capital categories. Withholding is a separate collection step: LF article 15 changes rental prepayment to 10% for individuals and 15% for legal persons; equipment hire retains its distinct wording. Reconcile certificates before concluding the final balance; this Guide's examples are gross category tax before credits, not an instruction to charge both tax and withholding cumulatively. [LF arts 3, 14–15](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=21).

## Deadlines and filing

Employer collection is monthly under CGI article 847, using the administration's payroll scale. Remit by the 15th of the following month under article 848. Article 849 requires an e-TAX-generated declaration and a notified copy recording the date, unique declaration number and administration logo. Reconcile the month's taxable base, withholding, submitted declaration, payment and acknowledgement. The administration's live payroll scale and current screen/field identifiers have not been obtained; do not fabricate a monthly rounding or annualisation convention. [CGI arts 847–850](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=167).

Article 986 requires employers' annual named salary statement during January, with identity/address/job, pay after pension deductions, benefits, withheld IRPP and payment period. Article 987 requires individual detail above annual remuneration of 60,000 and aggregate reporting below that figure. Foreign-pay recipients domiciled in Chad supply corresponding information under article 994. [CGI arts 986–994](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=189).

For an individual's annual declaration, articles 983–985 require income by nature, foreign receipts separately and the administration's signed form to the residence tax office. The reviewed text here does not establish a general 30 April IRPP deadline. Obtain the current applicable annual calendar/form before filing. Business declarations have their own rules in the corporate-tax Guide. [CGI arts 983–985](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=188).

## Penalties and interest

Employer withholding retained but not remitted within article 848's deadline attracts 1.5% for each month or part, capped at 50%, under article 1042; prosecution is separately preserved. Assessment omissions/inaccuracies attract article 1038's 1.5% monthly interest with its own start/end calculation. Failure to declare after notice triggers article 1039's assessed tax plus 100%, 150% for repeat failure, and interest; article 1040 caps that non-declaration interest at 50%. Do not mechanically add assessment and recovery charges for the same period: article 1044 governs recovery after an assessment notice on a different base and timeline. [CGI arts 1038–1044](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=204).

## Cross-border points

Retain both residence and source evidence, the applicable convention and foreign tax certificates. Article 117's foreign financial-income relief requires a convention and actual foreign tax, and excludes cases with exemption or refund under it. Article 105 separately addresses nondomiciled people holding a Chad residence using the greater of actual Chad income and five times rental value; do not conclude nonresident tax solely from salary. Departure/cessation cases route to articles 106–108. Treaty-by-treaty entitlement, credits, PE questions, nonresident professional withholding and exit calculations remain outside this computation. [CGI arts 105–108, 117](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef#page=35).

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

## Ask the client first

- Where were homes available, stays, personal/economic interests and assignments during the relevant year and twelve-month periods?
- Which receipts are salary, business/professional profit, rent, property gains or financial income, and where did each arise?
- What cash pay, benefits, actual compulsory contributions and evidence of each claimed allowance/exemption exist?
- Are there furnished/business properties, losses, community property, departure events or special employment statuses?
- Which payroll/annual declarations, withholding certificates, foreign taxes and convention claims already exist?

## Sources

| Primary source | Read on | Actual scope read |
|---|---|---|
| [Enacted finance law 2026, law 008/AN-SENAT/2025](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) | 2026-11-01 | Arts 1, 3–5, 8, 13–15; printed pp 1, 3–6, 15–16, 21–22; original/new blocks and adjacent clauses, bands and exemptions visually inspected |
| [Official CGI 2025, dated archive of ministry PDF, captured 2025-07-20](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) | 2026-11-01 | Arts 2–17, 44–48, 105–108, 117, 847–850, 983–994, 1038–1044; salary/property bases, residency, filing and penalties. Baseline reconciled with the listed 2026 amendments; not a whole-code review |

Not yet confirmed: full BIC/BNC and agricultural profit methods, property-disposal gain bases and special reliefs; complete benefit valuation where article 46's cash and housing provisions interact; live administration payroll scale, monthly rounding, IRPP annual due date and form/box/payment-reference workflow; complete treaty, foreign-credit, nonresident professional and exit computations; interactions between the 2026 category approach and older global-income deductions/credits. These gaps keep IT-IND partial. Historical 2025 figures are not independent evidence of current law. Independent AI source review is pending for this expansion; no accountant attestation.

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
