---
name: bd-social-contributions
description: "Bangladesh 2026 voluntary individual pension choices, Surokkha, Progoti, Probash and Samata; distinguish self-employed participation from employer-specific provident-fund and labour obligations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-social-contributions"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh self-employed pension choices v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For a solo self-employed individual choosing a Universal Pension scheme. This is not a universal payroll percentage. Employers must separately assess the Labour Act and fund duties in bd-payroll-social; voluntary individual enrollment does not establish that an employer has no statutory obligation.

## Ask the client first

- Citizenship/NID, age, residence and employment/self-employment.
- Existing pension/fund membership and employer institutional participation.
- Affordable monthly contribution, income eligibility and intended scheme.
- Contribution records and tax-rebate eligibility.

## The method, step by step

### Scheme card

| Scheme and conditions | Contribution/eligibility | Official source |
|---|---|---|
| Surokkha, self-employed/informal-sector citizen | Monthly BDT 1,000, 2,000, 3,000 or 5,000 | Current replacement schedule, page 2: https://www.upension.gov.bd/assets/public/files/up-doc-8.pdf?v=11 |
| Progoti, private employees/owners; employer participates institutionally | Monthly BDT 2,000, 3,000, 5,000 or 10,000; employer and employee each 50% | Rule 3(b) and replacement schedule, page 3: https://www.upension.gov.bd/assets/public/files/up-doc-5.pdf?v=11 ; https://www.upension.gov.bd/assets/public/files/up-doc-8.pdf?v=11 |
| Samata, participant below the poverty line using BBS income limits published from time to time | Rule 3(d) describes the current annual limit as BDT 60,000 (in words on the page); verify the applicable BBS limit. Monthly BDT 1,000, subscriber 500 and government 500 | Rule 3(d) and replacement schedule, page 3: https://www.upension.gov.bd/assets/public/files/up-doc-5.pdf?v=11 ; https://www.upension.gov.bd/assets/public/files/up-doc-8.pdf?v=11 |
| Standard joining ages; older participant exception | Bangladeshi NID holders aged 18-50; entry above 50 requires special consideration, with pension from the age reached after 10 continuous years of subscriptions | Rule 4(1): https://www.upension.gov.bd/assets/public/files/up-doc-5.pdf?v=11 |

1. A solo freelancer's voluntary scheme choice is separate from income tax and employee payroll. Route staff/fund/gratuity matters to [payroll/social](bd-payroll-social.md); do not conclude that an employer can opt out of labour law.
2. Choose Surokkha for self-employment, Progoti for private employment/owners, Probash for eligible Bangladeshis abroad, or Samata where the statutory low-income condition is met. Probash contributions use the prescribed foreign-currency channel; do not assume its tiers equal the domestic schemes.
3. Apply Rule 4 eligibility before registration. An expatriate without an NID can use a passport but must obtain and submit the NID copy as soon as possible and supply renewed/reissued passport copies. A person receiving a social-security-programme benefit must surrender that benefit before joining the applicable scheme; do not assume the benefits can be combined. Register through https://www.upension.gov.bd with the required identity, bank and nominee details, select the scheme/contribution and retain the pension ID and payment confirmations. Rules 4-5 and the NPA brief describe registration and bank/card/MFS/counter payment routes; check the actual portal before payment (https://www.upension.gov.bd/assets/public/files/up-doc-5.pdf?v=11).
4. The NPA brief describes contribution tax concession and exempt pension benefits. Apply the actual [PIT](bangladesh-pit.md) investment qualifications and cap rather than deducting the entire payment from income. Future pension amounts are contingent, not guaranteed returns.
5. Preserve employer PF and gratuity documents separately. Do not conflate the Universal Pension scheme with a universal compulsory self-employed social-security percentage.

## Worked cases

### Decision: affordable Surokkha contribution

Compare the published 1,000 and 2,000 monthly options: annual contributions are 12,000 and 24,000, difference 12,000. These are derived annual cash commitments, not promised pension payouts or guaranteed tax savings.

```oa-check
name: Surokkha contribution budget comparison
inputs:
  lower_monthly: 1000
  higher_monthly: 2000
  months: 12
steps:
  - lower_annual: lower_monthly * months
  - higher_annual: higher_monthly * months
  - difference: higher_annual - lower_annual
expected:
  lower_annual: 12000
  higher_annual: 24000
  difference: 12000
```

### Edge: institutional Progoti split

At a 2,000 monthly institutional contribution, employee and employer each pay 1,000. Over 12 months each contributes 12,000; the fund receives 24,000. Individual enrollment without institutional participation does not automatically create this employer match.

```oa-check
name: Institutional Progoti equal share
inputs:
  monthly_total: 2000
  months: 12
steps:
  - employee_monthly: monthly_total * 0.50
  - employer_monthly: monthly_total * 0.50
  - employee_annual: employee_monthly * months
  - employer_annual: employer_monthly * months
  - combined_annual: employee_annual + employer_annual
expected:
  employee_monthly: 1000
  employer_monthly: 1000
  employee_annual: 12000
  employer_annual: 12000
  combined_annual: 24000
```

## When to refuse or refer

Refer citizenship/age exceptions, arrears, nominations/death claims, scheme loans/conversion and employer duties. Never promise pension yields or assume eligibility for the government share or an investment rebate.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for original gazetted Rules 3-5 scheme scope, complete eligibility and registration/payment conditions | https://www.upension.gov.bd/assets/public/files/up-doc-5.pdf?v=11 | 2026-11-14 |
| Read for August 2024 removal of Pratyay additions and replacement contribution schedule, pages 1-3 | https://www.upension.gov.bd/assets/public/files/up-doc-8.pdf?v=11 | 2026-11-14 |
| Read for official source identity: English rules labelled Unofficial translation | https://www.upension.gov.bd/Public/Laws | 2026-11-14 |
| Read for comparison of Rules 3-5 and 12-13; this is an unofficial English translation, read with the original and later schedule | https://www.upension.gov.bd/assets/public/files/scheme%20rules_English.pdf?v=47 | 2026-11-14 |
| Read for scheme participation, Progoti institutional split, registration/payment channels and tax-benefit description | https://www.upension.gov.bd/Public/PensionBriefEn | 2026-11-14 |
| Read for rebate formula and income exclusions | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |

Not yet confirmed: Live NPA portal fields, the BBS poverty-income limit applicable to a particular Samata application, exact fund/gratuity duties and taxpayer-specific rebate qualification. The old English Probash schedule differs because the August 2024 gazette replaced the schedule; do not use that older schedule. The generic assertion that employer benefits are always optional is not retained.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
