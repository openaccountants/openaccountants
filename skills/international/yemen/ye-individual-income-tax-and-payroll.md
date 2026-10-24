---
name: ye-individual-income-tax-and-payroll
description: >
  Yemen source-cited individual income-tax and payroll draft based on selected provisions of Law 17/2010. Covers residence, annual resident bands, non-resident employment rate, income exclusions, employer withholding and employee obligations. Later amendments and administration-specific application remain unresolved, including the Sana'a-issued 2020 small-business employee exemption. Includes annual boundaries and a regular monthly payroll example applying articles 65–67; not a complete payroll engine.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://agoyemen.net/lib_details.php?id=198"
    title: "Public Prosecution: Law 17/2010, articles 3, 40, 48–50, 62–67 and 98–102"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/8-2021/"
    title: "Tax and Customs Authority: Sana'a-issued Law 8/2020, article 160(c)"
    as_of: "2026-10-22"
---

# Yemen: individual income tax and payroll withholding

## Scope and residence

This is a translation of selected provisions of the 2010 law, not a certified current nationwide schedule. Establish the administering office, business/work location, period and applicable amendments first. Current territorial application and the complete amendment chain remain unresolved. [Law 17/2010](https://agoyemen.net/lib_details.php?id=198).

Article 3 treats a natural person as resident if they have a permanent residence in Yemen; or, without such a permanent residence, spend at least **183 days**, continuously or intermittently, in a twelve-month period ending in the tax year; or are a Yemeni working abroad receiving employment income from Yemen. Do not substitute a calendar-year-only day count or assume nationality alone determines residence. Treaty residence, day-count detail and administrative evidence remain separate work. [Article 3](https://agoyemen.net/lib_details.php?id=198).

## Employment income and exclusions

Article 48 includes cash/in-kind employment benefits regardless of label or written contract, including Yemen-source payments for work inside or outside Yemen and foreign-source payments for work performed in Yemen. Directors' remuneration falls within the specified categories. This does not mean every foreign transfer is employment income. [Article 48](https://agoyemen.net/lib_details.php?id=198).

Article 49 excludes amounts prescribed for pension contributions under the applicable laws and regulations and job-related expense allowances within the implementing regulation's limits and criteria. A payroll label such as “travel allowance” is not sufficient evidence. Article 50 includes specific exemptions for pensions/end-of-service entitlements and compensation for work accidents and occupational injuries under the applicable rules; diplomatic and international-organisation cases have their own conditions. Daily-wage income also depends on regulatory criteria. The complete regulations and exemption eligibility have not been verified here. No social-contribution percentage is inferred from these income-tax provisions. [Articles 49–50](https://agoyemen.net/lib_details.php?id=198).

## General resident bands and the payroll override

Article 62 sets the general annual resident schedule: **YER120,000 exempt; the next YER120,000 at 10%; the next YER600,000 at 15%; excess above YER840,000 at 20%**. However, **article 65(a) caps resident salary/wage progression at 15%**. The general 20% top band must not be used for resident employment income. Article 63(f) separately sets **20%** on non-resident employment income. [Articles 62–65](https://agoyemen.net/lib_details.php?id=198).

Article 65(b) permits only one annual exemption where multiple direct income taxes apply, and article 65(c) prorates the YER120,000 resident exemption when the assessment period is shorter than twelve months. Article 67 explicitly determines payroll tax monthly on net monthly income using **one-twelfth of the article 62 bands**, read with the article 65 cap. This establishes a statutory monthly band basis; it does not settle all arrears, variable payments or part-year cases. [Articles 65 and 67](https://agoyemen.net/lib_details.php?id=198).

Article 66 separately charges specified other taxable employment benefits/entitlements at **15% without an exemption deduction**, subject to article 65. It distinguishes those amounts from the complete monthly salary including statutory allowances. Classify bonuses, overtime and other benefits before applying the ordinary monthly bands; do not simply combine every payment into the example's regular salary. [Article 66](https://agoyemen.net/lib_details.php?id=198).

## Withholding, return and payment

Article 99 requires monthly withholding by the employer when income is paid, with regard to the period to which the income relates based on the month of service. Other income/entitlements are withheld on payment and included in the monthly return. Under article 100 the employer must remit even if it failed to deduct from the employee. [Articles 99–100](https://agoyemen.net/lib_details.php?id=198).

Article 101(a) requires the return and payment within the **first ten days of each month for the preceding month**. Article 101(b) makes an employee working simultaneously for multiple employers personally responsible for tax differences within that same period, without removing each employer's withholding duty. Article 102 puts remittance on the recipient where the employer/payer is non-resident or lacks a centre or establishment in Yemen, under implementing procedures. Remote work does not automatically remove the recipient's obligation. [Articles 101–102](https://agoyemen.net/lib_details.php?id=198).

Article 40's original small-enterprise payroll rule instead uses a quarterly return/payment within the first ten days of the fourth month. Determine classification and amendments before choosing this exception. The Sana'a-issued Law 8/2020 adds article 160(c), including an employee exemption for specified small/micro enterprises. Its full eligibility and administration-specific application must be reconciled before using either the old quarterly rule or the later exemption. This Guide applies neither automatically. [Article 40](https://agoyemen.net/lib_details.php?id=198); [Law 8/2020](https://tax.gov.ye/8-2021/).

## Example 1: resident band boundaries

Assume the resident annual schedule governs, all relevant exclusions have already been determined, and no separate exemption applies. At YER120,000 the annual tax is zero. At YER840,000, tax is YER12,000 plus YER90,000, totalling YER102,000. No amount exceeds the general upper boundary in this example; resident salary progression is in any event capped at 15% by article 65.

```oa-check
name: Yemen annual resident exemption and upper band boundary
inputs:
  exempt_amount: 120000
  first_taxed_band: 120000
  first_rate: 0.10
  second_taxed_band: 600000
  second_rate: 0.15
steps:
  - tax_at_exemption: exempt_amount * 0
  - tax_at_840000: first_taxed_band * first_rate + second_taxed_band * second_rate
expected:
  tax_at_exemption: 0
  tax_at_840000: 102000
```

## Example 2: regular monthly resident versus non-resident salary

Assume YER100,000 regular monthly employment income after relevant exclusions, with no separately taxed article 66 payments, part-month complication or further relief. The resident monthly bands give YER10,000 exempt, YER10,000 at 10%, and the remaining YER80,000 at 15% because article 65 caps progression. Tax is YER13,000. The non-resident 20% rate gives YER20,000. Twelve identical resident months total YER156,000. This assumes exactly the same eligible salary and status in all twelve months.

```oa-check
name: Yemen monthly payroll with resident 15 percent cap
inputs:
  monthly_income: 100000
  exempt_band: 10000
  first_taxed_band: 10000
  first_rate: 0.10
  resident_capped_rate: 0.15
  nonresident_rate: 0.20
  months: 12
steps:
  - resident_tax: first_taxed_band * first_rate + (monthly_income - exempt_band - first_taxed_band) * resident_capped_rate
  - nonresident_tax: monthly_income * nonresident_rate
  - resident_twelve_identical_months: resident_tax * months
expected:
  resident_tax: 13000
  nonresident_tax: 20000
  resident_twelve_identical_months: 156000
```

## Intake and outstanding work

Obtain residence/home evidence, travel dates, nationality where relevant, work locations, employer residence/establishment, payment and service dates, simultaneous employers, gross cash/in-kind pay, deductions and supporting documents, and employer classification. Still open: current amendments by administration, complete variable-pay and arrears methods, benefit valuation, regulatory allowance limits, small-enterprise exemption eligibility, social contributions, operational forms/payment channels, reconciliation, corrections and penalties. No comprehensive individual or payroll coverage or professional attestation is claimed.

## Sources

- [Public Prosecution, Law 17/2010](https://agoyemen.net/lib_details.php?id=198), articles cited above, retrieved 22 October 2026. Arabic controls over this translation.
- [Tax and Customs Authority, Law 8/2020](https://tax.gov.ye/8-2021/), retrieved 22 October 2026. Application outside the issuing administration has not been established.

## Disclaimer

Source-cited research draft. Confirm governing law, administration, facts and procedures before running payroll or filing.
