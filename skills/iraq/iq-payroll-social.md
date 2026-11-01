---
name: iq-payroll-social
version: 0.3
description: "Federal Iraq payroll research with public sector 2019 calculation extracts, separate private-employment and social-insurance holds, and no current payroll clearance. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Payroll and Social Contributions 0.3

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Historical federal payroll source extracts. The GCT 2019 explanatory circular is expressly about state departments and the public sector, including its temporary-contract and permanent-staff examples. It is not a private-sector contribution schedule. Private employment, social insurance and the Kurdistan Region are held separately.

## Rates, bands and thresholds

**2019 public sector source only, subject to IQ-CURRENT.** Income tax's annual scale belongs in [individual income tax](iq-income-tax.md); do not treat the scan's rounded monthly band endpoints as a new annual scale.

| Source scope and condition | Historical amount | Official URL |
|---|---|---|
| GCT 2019 notes 1–2, permanent state staff: deduct from nominal salary for pension before tax | 10% of nominal salary | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf |
| Same circular note 3, single / spouse taxed separately | IQD 2,500,000 annual allowance | same |
| Same note, housewife spouse or qualifying merged income | IQD 4,500,000 total annual allowance | same |
| Same note, wife with husband unable to work, medical committee certification and note 7 merger/branch conditions | IQD 5,000,000 annual allowance | same |
| Same note, self-independent widow or divorced woman (المستقلة بذاتها) | IQD 3,200,000 annual allowance | same |
| Same note, employee older than 63 | IQD 300,000 extra annual allowance | same |
| Same note, each legally qualifying child, regardless of number | IQD 200,000 annual allowance | same |

These amounts do not establish entitlement without the family conditions. Complete child eligibility and private-sector treatment remain held.

## The base

The 2019 state/public-sector notes tax salary and overtime, exclude allowances (mukhassasat), and deduct the stated pension contribution for permanent state staff. Do not apply that exclusion or pension percentage to a private employee. Notes 4–8 require court custody evidence for a divorced man, permit only one housewife spouse, and require the relevant joint signed January merger request and GCT branch evidence for the special spouse cases; an incapacity case also needs the competent medical committee report. A married woman otherwise has her own single allowance. Note 9 permits correction before the financial year ends. All are historical source conditions subject to IQ-CURRENT.

## Deadlines and filing

Law 113 art. 17(3) makes the employer liable to deliver the tax required even if not deducted; art. 18 requires the requested staff/payment information within the authority's specified period. These old-consolidation extracts do not establish current remittance dates, employer registration, the current withholding return, all marital-status tables, submission, receipt or payment reference. The Minister's operative timetable must be established before filing.

## Penalties and interest

Held. Article 17(4) in the consolidation links additions to non-delivery within 21 days of Minister-set dates; the date-setting instrument and later changes have not been established. Do not replace that with a guessed universal monthly deadline or a complete penalty formula.

## Cross-border points

Gather nationality, residence, months present, foreign pay and assignment details. Historical resident/nonresident source distinctions are in [income tax](iq-income-tax.md). Non-Iraqi allowance proration, social-insurance treaties, secondments and cross-region administration are not cleared by this circular.

## Two worked examples that recompute

Recompute the 2019 circular's **public sector** cases, not a current payroll bill. The scan's monthly arithmetic rounds its band endpoints; an annual calculation can differ at the smallest currency unit. IQ-CURRENT applies.

Temporary contract staff, nominal monthly pay IQD 700,000, qualifying housewife spouse, no children: circular case is IQD 42,083.

```oa-check
name: 2019 public contract example
inputs:
  pay: 700000
steps:
  - taxable: pay - 375000
  - tax: round((taxable - 83333) * 0.15 + 5833)
expected:
  tax: 42083
```

Decision boundary: permanent state staff on the same nominal pay first deduct the state pension, giving the circular's IQD 31,583. Applying the permanent-staff deduction to the temporary example would understate the illustrated tax by IQD 10,500. This is a classification check, not a choice of pension system.

```oa-check
name: 2019 permanent classification difference
inputs:
  pay: 700000
steps:
  - permanent_base: pay - pay * 0.10 - 375000
  - permanent_tax: round((permanent_base - 83333) * 0.15 + 5833)
  - contract_tax: round((pay - 375000 - 83333) * 0.15 + 5833)
  - difference: contract_tax - permanent_tax
expected:
  permanent_tax: 31583
  difference: 10500
```

## Ask the client first

- Federal Iraq or Kurdistan Region, and pay period?
- State permanent, state temporary contract, or private employer?
- Nominal salary, overtime, allowances and actual pension deductions?
- Family status, dependency, custody, spouse income and merger documents?
- Nationality, months present, other employment and foreign assignment?
- Employer notices, registration and social-insurance category?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| 2019 GCT withholding circular: PDF pp. 3–6 notes 1–12 visually read; state/public-sector heading and worked cases checked | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf | 2026-11-01 |
| Law 113: PDF pp. 18–19 art. 17(1)–(4) and art. 18 read visually with neighbours | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT** complete later amendments and 2026 payroll table; **IQ-PAY-PRIVATE** private-sector income base, allowance/exemption limits, non-Iraqi full-month proration, child dependency/age/income conditions, multiple employers and secondary employment; **IQ-PAY-PROCEDURE** employer registration, forms/tables, current remittance dates (including the inherited 15-day claim), returns, receipts, refunds and penalties; **IQ-SOCIAL** operative social-insurance legislation, commencement/transitions, contribution rates, oil categories, wage base, ceiling, registration, remittance, benefits and cross-border coordination. Neither the old employee/employer percentages nor a public pension deduction is evidence of the present private-sector liability.

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
