---
name: ps-individual-income-tax-and-payroll
description: >
  Palestine individual income-tax and employer withholding research draft from the Official Gazette Bureau consolidated Income Tax Decree-Law 8 of 2011. Covers domestic residence tests, annual tax bands, resident allowances, spouse rules, wage deductions, remittance and employer records. Includes reproducible annual calculations and band boundaries. Later amendments, current payroll instructions, social contributions and territorial administration remain unverified. The annual examples are not certified monthly withholding tables, and the draft does not establish uniform administration across Palestinian territories or complete country coverage.
jurisdiction: PS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين"
    title: "Official Gazette Bureau consolidated Income Tax Decree-Law 8/2011, articles 1, 4, 12, 14, 16, 18–19, 30–31 and 36"
    as_of: "2026-10-22"
---

# Palestine: individual income tax and payroll withholding

## Source and territorial limits

This research translation uses the official Arabic consolidated text, whose amendment list includes 4/2014, 5/2015 and 14/2016. Later legislation, emergency measures and current payroll instructions have not been fully reconciled. Establish the actual tax administration and territorial application for the worker and employer; the Guide does not assert uniform application in the West Bank, Gaza or East Jerusalem. Arabic controls over this translation. [Official consolidated law](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Residence before allowances

Article 1 defines a Palestinian individual as resident after **at least 120 days** in Palestine in the income year, whether continuous or interrupted. It separately includes a Palestinian employed at any time during the year by the Palestinian Authority or a local authority, inside or outside Palestine. A non-Palestinian individual uses **at least 183 days**, continuous or interrupted. These are domestic tests; do not substitute nationality alone, a residence permit or a treaty tie-breaker. Arrival/departure-day counting and dual-residence relief need further verification. [Article 1](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 4 ordinarily calculates tax by calendar year. Residence, taxable source, exemptions and employer withholding must be tested separately; passing a residence day count does not establish that every receipt is taxable. [Articles 1, 3–4](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Annual rates and resident allowances

Article 16(1) applies progressive bands to an individual's **taxable income**:

| Annual taxable slice, ILS | Rate |
|---|---:|
| First 75,000 | 5% |
| Next 75,000 | 10% |
| Above 150,000 | 15% |

Apply each rate only to its slice, not the whole salary at the highest rate reached. [Article 16(1)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 12(1) grants resident individuals an annual **ILS36,000** allowance. For private-sector transport, it allows the actual transport allowance paid or **10% of annual gross salary**, whichever is lower. Public-sector fixed transport allowance has a separate actual-paid rule. Preserve allowance and payroll evidence; the private-sector percentage is not an automatic deduction without an actual allowance. Contributions to the specified pension, savings, health, social-security and other minister-approved funds require their own eligibility evidence. [Article 12(1)(a)–(d)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Housing relief is either a once-only **ILS30,000** purchase/build allowance or actual interest on a loan from a **bank, lending institution or housing institution**, spent on purchasing or building a dwelling, capped at **ILS4,000 annually for no more than ten years**, supported by documents. University relief is **ILS6,000 per year per qualifying student**, for the taxpayer, spouse or children at the specified post-secondary institutions, limited to two students and excluding scholarship/sponsored cases. These are separate conditions, not automatic payroll adjustments. [Article 12(1)(e)–(f)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 14 treats spouses as separate taxpayers, allows each the statutory allowances except that the housing and education allowances are granted to one spouse, and permits a request to combine incomes. Do not duplicate those family allowances or assume joint assessment without the request and applicable procedure. Article 12(2) permits Cabinet changes to allowances; current amending measures still need checking. [Articles 12(2), 14](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Worked example 1: assumed annual resident calculation

Assume ILS120,000 gross annual salary, full eligibility for the ILS36,000 allowance, no other relief or exempt income, and no credits. Taxable income is ILS84,000. Tax is ILS3,750 on the first band plus ILS900 on the remaining ILS9,000: **ILS4,650**. This is an annual computation; dividing it by twelve does not prove the lawful monthly withholding method.

```oa-check
name: Palestine annual resident salary example
inputs:
  gross_salary: 120000
  allowance: 36000
steps:
  - taxable_income: gross_salary - allowance
  - first_band_tax: 75000 * 0.05
  - second_band_tax: (taxable_income - 75000) * 0.10
  - total_tax: first_band_tax + second_band_tax
expected:
  taxable_income: 84000
  first_band_tax: 3750
  second_band_tax: 900
  total_tax: 4650
```

## Worked example 2: band boundary and higher income

At established taxable income of ILS150,000, tax is **ILS11,250**. At ILS200,000, the excess ILS50,000 adds ILS7,500, producing **ILS18,750**. These inputs are already after allowed deductions/exemptions; do not subtract the annual allowance a second time.

```oa-check
name: Palestine annual band boundary and third band
inputs:
  boundary_income: 150000
  higher_taxable_income: 200000
steps:
  - boundary_tax: 75000 * 0.05 + 75000 * 0.10
  - additional_tax: (higher_taxable_income - boundary_income) * 0.15
  - higher_tax: boundary_tax + additional_tax
expected:
  boundary_tax: 11250
  additional_tax: 7500
  higher_tax: 18750
```

## Employer withholding and remittance

Article 31(3) requires the employer or person paying salary, wages, allowances, bonuses or equivalent remuneration to deduct the tax when paying and remit it with a detailed statement **within fifteen days of payment**. This is not fifteen days after month-end. Article 30(5)'s general thirty-day withholding rule expressly yields to article 31; do not use it to extend the wage deadline. Current monthly tables, cumulative adjustments, rounding and approved forms remain unverified. [Articles 30(5), 31(3)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Maintain the employee register required by article 31(5): names, wages, allowances, exemptions and changes. Comply with an assessor's direction to increase or reduce withholding under paragraph 6. Paragraph 10 requires a certificate stating the withheld amount and withholding/remittance dates; a deduction without payment to the department is not equivalent to a remitted credit. Failure to deduct or pay can be collected from the responsible employer under paragraph 12. [Article 31(5)–(6), (10), (12)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

The assessor can treat wage withholding as final under article 31(4) where no return is filed and no other income sources exist, with the specified two-year reconsideration power. Do not describe all employees as automatically exempt from returns. Articles 18–19 state the general return obligation/four-month deadline, subject to authorised exemptions for categories of individuals. [Articles 18–19, 31(4)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Penalties, controls and remaining work

The retrieved article 36(4) prints a **2% monthly late-remittance penalty** for withheld tax not delivered on time, with discretionary relief for reasons outside the taxpayer's control. Confirm current law, month counting, interaction with other charges and any relief before quoting a penalty. [Article 36](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

For each payroll, retain identity/residence evidence, dates and place of work, remuneration classification, approved allowances, calculation workings, deduction statement, actual payment receipt and employee certificate. Social-security contributions, employment-law entitlements, pensions, benefits valuation, nonresident source rules, treaty relief and current operational channels are separate unresolved topics. No social-insurance exemption is inferred from this income-tax law.

## Sources

- [Official Gazette Bureau consolidated Income Tax Decree-Law 8/2011](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين), read 22 October 2026. Each claim's statutory locator appears above.

## Disclaimer

Source-cited draft, not professionally attested. Confirm current law, territorial administration and payroll procedures before filing or paying.
