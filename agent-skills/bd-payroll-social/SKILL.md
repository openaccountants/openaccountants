---
name: bd-payroll-social
description: "Bangladesh 2026 employer provident-fund, Progoti alternative and workers profit-participation duties, distinguishing them from salary withholding and voluntary solo-worker pension choices."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bd-payroll-social"
  jurisdiction: "BD"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bangladesh employer funds and social obligations v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Employers and establishments subject to the Bangladesh Labour Act. This owns employment-fund conditions; salary tax is in bd-payroll and voluntary individual scheme choice in bd-social-contributions. Do not import a universal payroll percentage.

## Ask the client first

- Establishment/worker coverage under the Labour Act and permanent headcount.
- Written worker request, request date, existing PF rules and institutional Progoti participation.
- Basic wages, permanent service, contrary agreement and fund recognition.
- Paid-up capital, fixed assets, statutory net profit and export/foreign-investment sector status.

## The method, step by step

### Duties card

| Condition | Duty or rate | Official source |
|---|---|---|
| Establishment with at least 100 permanent workers and written PF request by at least 2/3 of workers | PF must be constituted; see institutional Progoti alternative and refusal conditions in the same provision | Labour Act section 264(10): https://bdlaws.minlaw.gov.bd/act-print-952/section-print-26316.html |
| PF requested under that provision | Necessary rules and fund operating within 6 months after request | Section 264(11): https://bdlaws.minlaw.gov.bd/act-print-952/section-print-26316.html |
| Existing PF, permanent worker after 1 year of service, absent contrary agreement | Employee contribution 7%-8% of monthly basic wages; employer matches | Section 264(9): https://bdlaws.minlaw.gov.bd/act-print-952/section-print-26316.html |
| Qualifying institutional Progoti alternative | Employer and employee each 50%; written unwillingness affects employer duty for that worker | Section 264(10): https://bdlaws.minlaw.gov.bd/act-print-952/section-print-26316.html |
| Company/establishment meets either scope test | Paid-up capital at least BDT 10,000,000 (1 crore, in words on the page) or fixed assets at least BDT 20,000,000 (2 crore, in words on the page) at year end; notified and specified export/foreign-investment sector rules also need checking | Section 232: https://bdlaws.minlaw.gov.bd/act-952/section-26285.html |
| WPPF/welfare contribution within covered chapter | 5% of statutory prior-year net profit, split 80:10:10 among participation, welfare and Workers Welfare Foundation funds | Section 234: https://bdlaws.minlaw.gov.bd/act-952/section-26287.html |

1. Test Labour Act/worker coverage before applying a fund duty. The old unqualified three-quarters-request rule is replaced by the current section 264 condition above. Small-employer, individual pension and institutional participation are not interchangeable.
2. Obtain the fund rules, trustee information, worker request and service/basic-wage data. Apply an actual applicable agreement rather than mechanically charging a percentage to gross salary. Keep employee deductions and employer expense/liability separate.
3. If using institutional Progoti as the statutory alternative, document participation, interested/unwilling workers and matching obligations. A worker voluntarily opening an individual pension account is not proof that the employer has satisfied section 264.
4. Apply WPPF scope separately. Section 232 includes notification and sector arrangements for fully export-oriented/foreign-exchange investment sectors. Use the statutory definition of net profit and current fund provisions; do not take any profit figure from a bank summary. Section 234 requires fund establishment and a distribution calendar; obtain the exact applicable dates before making a payment.
5. Gratuity/termination benefits require the employment facts, service rules, Labour Act ground for termination and any approved fund. Do not treat every termination as an identical gratuity award. Salary withholding/remittance belongs to [payroll](bd-payroll.md).

## Worked cases

### Provident fund contribution

Illustrative covered permanent worker with completed qualifying service, no contrary agreement and basic wages 30,000 under a fund using 7%. Employee pays 2,100 and employer 2,100, combined 4,200. Gross remuneration is not substituted for basic wages.

```oa-check
name: Provident fund matched basic wage contribution
inputs:
  basic_wages: 30000
  fund_rate: 0.07
steps:
  - employee: basic_wages * fund_rate
  - employer: employee
  - combined: employee + employer
expected:
  employee: 2100
  employer: 2100
  combined: 4200
```

### WPPF allocation after the legal base is established

Illustrative covered company's independently established statutory profit base 1,000,000 gives fund contribution 50,000, allocated 40,000/5,000/5,000. This does not establish that accounting profit equals statutory net profit or that an export-sector alternative is inapplicable.

```oa-check
name: WPPF statutory base and allocation
inputs:
  statutory_profit: 1000000
steps:
  - fund_total: statutory_profit * 0.05
  - participation: fund_total * 0.80
  - welfare: fund_total * 0.10
  - foundation: fund_total * 0.10
  - allocated: participation + welfare + foundation
expected:
  fund_total: 50000
  participation: 40000
  welfare: 5000
  foundation: 5000
  allocated: 50000
```

## When to refuse or refer

Refer disputed worker/establishment coverage, agreements, fund recognition, statutory-profit base, sector central funds, employee refusal and gratuity/termination. Do not conclude every benefit is optional or every freelancer owes a national contribution.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for complete current provident-fund/Progoti conditions, contribution/service and request-period rules, section 264 | https://bdlaws.minlaw.gov.bd/act-print-952/section-print-26316.html | 2026-11-14 |
| Read for WPPF scope, alternative tests, notifications and sector exception, section 232 | https://bdlaws.minlaw.gov.bd/act-952/section-26285.html | 2026-11-14 |
| Read for fund establishment, contribution, allocation and transitional exception, section 234 | https://bdlaws.minlaw.gov.bd/act-952/section-26287.html | 2026-11-14 |

Not yet confirmed: Entity-specific fund recognition/rules, the exact statutory net-profit reconciliation, sector central-fund and gratuity amounts, and payment dates/filings for those case-specific funds. No universal social-insurance percentage is asserted.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bd-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bd-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
