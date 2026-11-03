---
name: gm-payroll-social
description: "payroll and social contributions for The Gambia (tax year 2026): PAYE, SSHFC NPF, FPS and IICF, expatriate quota tax of D30,000 and D100,000. Built from official GRA, SSHFC and Ministry of Justice pages."
jurisdiction: GM
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gambia Payroll and Social Contributions

## Who this applies to

Employers and employees in The Gambia. PAYE goes to GRA; contributions go to the Social Security and Housing Finance Corporation (SSHFC). NPF is 15% of basic salary; FPS covers member institutions; IICF is employer funded. Which scheme a given employer joins is a fact to ask.

## Rates, bands and thresholds

Basis for 2026: the rows below come from the GRA and SSHFC pages live on 1 November 2026. The Income and Value Added Tax Act 2012 and any 2026 amending Act could not be opened, so a 2026 change that GRA has not published is not reflected.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Band 1: D0 to D36,000 a year | 0% | 2026 | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 |
| Band 2: D36,001 to D46,000 | 5% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 3: D46,001 to D56,000 | 10% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 4: D56,001 to D66,000 | 15% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 5: D66,001 to D76,000 | 20% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 6: above D76,000 | 25%; the GRA table runs at 25% to its last row, D100,000 a month | 2026 | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 |
| NPF employee | 5% of basic salary | 2026 | https://www.sshfc.gm/national-provident-fund |
| NPF employer | 10% of basic salary | 2026 | https://www.sshfc.gm/national-provident-fund |
| FPS employer | 15% of gross salary (basic plus fixed allowances); employee pays nothing | 2026 | https://www.sshfc.gm/federated-pension-scheme |
| IICF employer | 1% of basic plus fixed allowances, ceiling D15 | 2026 | https://www.sshfc.gm/industrial-injury-compensation-fund |
| Expatriate quota tax: ECOWAS citizen or special status | D30,000 a year, from the 2026 Notice dated March 2026 (D10,000 before) | 2026 | https://www.gra.gm/download-file/221f7a81-6596-11f1-b086-029254d29bb1 |
| Expatriate quota tax: all others | D100,000 a year (D50,000 before) | 2026 | https://www.gra.gm/download-file/221f7a81-6596-11f1-b086-029254d29bb1 |
| Expatriate share of workforce | Up to 20%; above needs Minister of Finance approval | 2026 | https://www.gra.gm/download-file/8d0c9e3d-d217-11ed-9b31-029254d29bb1 |

Monthly PAYE above D76,000 a year: ((annual gross - 76,000) * 25% + 5,000) / 12.

## The base

PAYE covers wages, salaries, bonuses, leave pay, overtime, fees, allowances, commissions, termination and other supplemental pay, in cash, cheque or bank deposit, domestic or foreign. No deductions are allowed. Exempt: the President, non-commissioned officers of the Armed Forces, foreign diplomats, government pensioners, those exempted by the President with National Assembly approval, and foreign employment income already taxed there. PAYE is final unless the employee has other income.

Expatriate quota tax falls on the employer, who must not recover it from the employee. Exempt: religious or charitable institutions in respect of clergy, imams, missionaries, doctors and teachers; diplomatic missions; international organisations; investors and sole proprietors in the informal sector. A self-employed non-Gambian in a small indigenous business is not liable.

## Deadlines and filing

| Item | Due |
|---|---|
| PAYE schedule and payment | 15 days after month end |
| NPF, FPS | 15th of the following month |
| Expatriate notice to the Commissioner General | 1 January |
| Quota application to EQAB Technical Committee, one per employee | 31 January, or 14 days after start |
| Expatriate tax | 14 days after start; continuing employees 31 January |

For good cause the Commissioner General may extend expatriate tax if 50% is paid and the balance within 90 days.

### How to file on the GRA portal
1. Go to https://www.gra.gm and log in with portal credentials. A new user creates temporary credentials first and registers for a TIN.
2. Select the tax type, then complete the return form or upload it.
3. Upload supporting documents and submit.
4. The system sends an instant e-acknowledgement, then a notice with a document ID used to pay.
5. Pay by bank or another listed platform. The system sends a URL to print the receipt.
To amend or extend, use the same login, select the tax type, return and period, complete the request, upload reasons and submit; GRA notifies approval or rejection. Paper returns go to the nearest DTD office, or to Kanifing Revenue Office for the Large Taxpayer Unit. Box numbers are not listed here because the form could not be read as a PDF.

## Penalties and interest

SSHFC late payment: 2.5% of the unpaid amount for each month or part month, under NPF and FPS. PAYE offences: failure to file, false information, improper TIN use, obstruction; amounts are on the Not yet confirmed line. Objection within 30 days, then the Tax Tribunal, then the Court of Appeal.

## Cross-border points

Residents earning employment income abroad are liable subject to the foreign source rule. Every non-Gambian employee triggers quota tax unless an exemption above applies.

## Two worked examples that recompute

Basic D20,000 plus fixed allowances D5,000 a month, NPF employer.

```oa-check
name: Monthly payroll
inputs:
  basic: 20000
  gross: 25000
steps:
  - ee_npf: basic * 0.05
  - er_npf: basic * 0.10
  - iicf: min(gross * 0.01, 15)
  - paye: ((gross * 12 - 76000) * 0.25 + 5000) / 12
expected:
  ee_npf: 1000.00
  er_npf: 2000.00
  iicf: 15.00
  paye: 5083.33
```

Decision: an ECOWAS or non-ECOWAS hire. Annual quota tax is D30,000 or D100,000, a D70,000 yearly difference that falls on the employer.

```oa-check
name: Quota tax gap
inputs:
  ecowas: 30000
  other: 100000
steps:
  - gap: other - ecowas
expected:
  gap: 70000.00
```

## Ask the client first

- Basic and fixed allowances?
- NPF or FPS employer?
- Any other income for the employee?
- Nationality of non-Gambian staff and start date?
- Share of non-Gambian staff in the workforce?

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA Income Tax Table 2025 (monthly table; band edges and last row read, latest table on the GRA downloads page), read for the rows cited | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA PAYE brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |
| SSHFC National Provident Fund page (contribution section), read for the rows cited | https://www.sshfc.gm/national-provident-fund | 2026-11-01 |
| SSHFC Federated Pension Scheme page (contribution section), read for the rows cited | https://www.sshfc.gm/federated-pension-scheme | 2026-11-01 |
| SSHFC Industrial Injuries Compensation Fund page (contribution section), read for the rows cited | https://www.sshfc.gm/industrial-injury-compensation-fund | 2026-11-01 |
| Expatriate Quota Pay Roll Tax Notice, 2026, under Payroll Tax Act Cap. 83:04 s.21 (whole), read in full for this skill | https://www.gra.gm/download-file/221f7a81-6596-11f1-b086-029254d29bb1 | 2026-11-01 |
| GRA Payroll Tax brochure (whole; amounts superseded by the 2026 Notice), read in full for this skill | https://www.gra.gm/download-file/8d0c9e3d-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA E-Filing brochure (whole), read in full for this skill | https://www.gra.gm/download-file/7937e6d9-48f3-11ef-b086-029254d29bb1 | 2026-11-01 |

Not yet confirmed: The Income and Value Added Tax Act 2012, SSHFC Act 2015 text and any 2026 amendment. The Notice date is handwritten and reads as 10 March 2026; GRA published it the same day. "Special status" in the Notice is undefined there. The SSHFC NPF reform notice page held only placeholder text. Whether the SSHFC pages reflect 2026 (FPS page dated 2017). PAYE penalty amounts. PAYE form box numbers. 

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
