---
name: ye-social-contributions
description: >
  Yemen private-sector social insurance research draft under Law 13 bis/2013 and institution guidance. Covers scope, registration and contribution controls, with an unresolved discrepancy over the additional employer work-injury charge. Conditional calculations are not payment instructions. Territorial application and current implementation remain unverified.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://gcss.ye/law/"
    title: "General Corporation for Social Security: Law 13 bis/2013"
    as_of: "2026-10-22"
  - url: "https://gcss.ye/guides-of-sub/"
    title: "General Corporation for Social Security: contribution services guide"
    as_of: "2026-10-22"
---

# Yemen: social contributions and registration

## Status: unresolved employer-rate discrepancy

This local research draft is **not ready for operational payroll use**. The institution's law and service guide disagree on the employer total. Resolve the governing instrument and implementation with the administering office before calculation or payment. Its website identifies its headquarters in Sana'a; application under other administrations is not established. The 2026 metadata is the research year, not certification of current nationwide law.

## Statutory baseline

Law 13 bis/2013 repeals Law 26/1991 in article 128. Articles 5–10 cover private-sector workers aged at least 18, without nationality discrimination; one employee suffices. Self-employed coverage is voluntary; public-service and specified diplomatic/international categories are excluded. Register both employer and workers.

Article 3 includes permanent allowances in wages, excluding incentive bonuses and overtime. Article 18 uses January/July wages, with a separate new-joiner rule needing reconciliation. Article 19's thirty-times-minimum limit concerns pension treatment; excess attracts supplementary insurance, not automatic contribution exemption.

Article 32 separately lists employer pension **11%**, employee **7%**, and employer work-injury **2%**. Articles 23–24 govern service periods and payment; same-month entry/exit requires a full contribution. Article 24 provides late-payment and reporting penalties. These are statutory provisions, not a verified current collection schedule. [Law 13 bis/2013, articles 3, 5–10, 18–24, 32 and 128](https://gcss.ye/law/).

## Institution guidance and practical controls

The contribution guide instead displays **18% total: employer 11%, employee 7%**, without explaining the law's separate injury charge. It requires registration within two weeks of starting activity and monthly payment within the first 15 days of the following month. It lists establishment registration, worker entry/exit, wage schedules and monthly payment forms. Obtain current forms and receipts from the responsible branch; do not infer current form fees from an undated web table.

For voluntary self-employed insurance, it describes **18% of a selected wage band**, subject to eligibility and prior insured wage constraints. Registration and continued payment are conditions. The displayed band schedule and subsequent changes need period-specific confirmation. [Contribution guide, compulsory and voluntary sections](https://gcss.ye/guides-of-sub/).

## Example 1: quantify the unresolved difference

Assume YER100,000 is an independently established contribution base. The website guidance yields employer YER11,000 and employee YER7,000. Adding the separately stated statutory injury component would increase employer cost by YER2,000 and combined employer/employee contributions from YER18,000 to YER20,000. **Neither total is selected here as the amount payable.** This comparison identifies the question that needs a controlling source.

```oa-check
name: Yemen social contribution source discrepancy
inputs:
  established_base: 100000
  employer_pension_rate: 0.11
  employee_rate: 0.07
  separate_injury_rate: 0.02
steps:
  - employer_pension: established_base * employer_pension_rate
  - employee: established_base * employee_rate
  - guidance_total: employer_pension + employee
  - injury_component: established_base * separate_injury_rate
  - statutory_components_total: guidance_total + injury_component
expected:
  employer_pension: 11000
  employee: 7000
  guidance_total: 18000
  injury_component: 2000
  statutory_components_total: 20000
```

## Example 2: accepted voluntary band

Assume eligibility, applicable scheme, a YER50,000 band and the 18% rate have independently been established. Monthly contribution is YER9,000. This calculation does not establish admission, band availability or nationwide application.

```oa-check
name: Yemen conditional voluntary contribution
inputs:
  accepted_band: 50000
  established_rate: 0.18
steps:
  - contribution: accepted_band * established_rate
expected:
  contribution: 9000
```

## Intake and remaining work

Collect location, administering branch, age, employment category, other pension coverage, contracts, wage components, January/July payrolls, joining/leaving dates and existing insurance records. Preserve the rate discrepancy with any branch response and its legal basis. Do not silently choose the lower rate or treat the difference as rounding.

Needed before operational acceptance: authentic issuance/publication date, implementing regulations, later amendments, injury-branch commencement or exemption evidence, current minimum/bands, precise new-joiner and partial exit-month rules, territorial application, corrections/appeals and benefits. The institution's reproduced law leaves day/month of issuance blank. No country-completion or professional-attestation claim is made.

## Sources

- [Institution reproduction of Law 13 bis/2013](https://gcss.ye/law/), with downloadable PDF corroborating article 32.
- [Institution contribution guide](https://gcss.ye/guides-of-sub/).

## Disclaimer

Source-cited research draft with an unresolved material rate discrepancy. Do not use as a payroll instruction.
