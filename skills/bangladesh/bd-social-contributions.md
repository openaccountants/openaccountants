---
name: bd-social-contributions
description: "Bangladesh 2026 voluntary individual pension choices, Surokkha, Progoti, Probash and Samata; distinguish self-employed participation from employer-specific provident-fund and labour obligations."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - social-contributions-workflow-base
tier: 2
domain: payroll
type: decision
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
| Surokkha, self-employed/informal-sector citizen | Monthly BDT 1,000, 2,000, 3,000 or 5,000 | NPA scheme brief and Rules schedule: https://www.upension.gov.bd/assets/public/files/scheme%20rules_English.pdf?v=47 |
| Progoti, private employees/owners; employer participates institutionally | Monthly BDT 2,000, 3,000, 5,000 or 10,000; employer and employee each 50% | NPA brief: https://www.upension.gov.bd/Public/PensionBriefEn |
| Samata, qualifying low-income participant | Annual income not exceeding BDT 60,000 under Rules; monthly BDT 1,000, subscriber 500 and government 500 | Rules 3 and schedule: https://www.upension.gov.bd/assets/public/files/scheme%20rules_English.pdf?v=47 |
| Standard joining ages; older participant exception | Ages 18-50; older entrants require at least 10 years of subscription under the Rules | Rule 4: https://www.upension.gov.bd/assets/public/files/scheme%20rules_English.pdf?v=47 |

1. A solo freelancer's voluntary scheme choice is separate from income tax and employee payroll. Route staff/fund/gratuity matters to [payroll/social](bd-payroll-social.md); do not conclude that an employer can opt out of labour law.
2. Choose Surokkha for self-employment, Progoti for private employment/owners, Probash for eligible Bangladeshis abroad, or Samata where the statutory low-income condition is met. Probash contributions use the prescribed foreign-currency channel; do not assume its tiers equal the domestic schemes.
3. Register through https://www.upension.gov.bd with required identity, bank and nominee details, select the scheme/contribution and retain the pension ID and payment confirmations. The NPA brief describes online banking/card/MFS and counter payment routes; check the current portal before payment.
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
| Read for Rules 3-4 scheme scope/eligibility and schedule contribution tiers; Rules 12-13 contingency and scheme conversion | https://www.upension.gov.bd/assets/public/files/scheme%20rules_English.pdf?v=47 | 2026-11-14 |
| Read for scheme participation, Progoti institutional split, registration/payment channels and tax-benefit description | https://www.upension.gov.bd/Public/PensionBriefEn | 2026-11-14 |
| Read for rebate formula and income exclusions | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |

Not yet confirmed: Live NPA portal eligibility and any later scheme amendment applicable to the applicant; Probash tier discrepancy between the English rules schedule and NPA brief (not used here), exact fund/gratuity duties and taxpayer-specific rebate qualification. The generic assertion that employer benefits are always optional is not retained.
