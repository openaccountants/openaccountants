---
name: zm-payroll-social
description: "Payroll and social contributions for Zambia, 2026: PAYE monthly bands 0% to 37%, skills development levy 0.5%, PAYE return by the 10th, NAPSA and NHIMA status under the National Pension Scheme Act 2026. Trigger on Zambia payroll, PAYE return, skills levy, NAPSA, NHIMA, ITF/P16, employer obligations ZRA. For employers and payroll providers. Rates not readable on official pages are marked unverified."
jurisdiction: ZM
category: payroll
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Charge year 2026.

## Who this applies to

Every employer, including those whose staff earn below the threshold: they still register and file. Zambians employed by exempt missions use the PAYE direct scheme. Self-employed: see [Income tax](zm-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| PAYE band 1 | First K5,100 a month, 0% | 2026 | https://www.zra.org.zm/tax-information/ |
| PAYE band 2 | K5,100.01 to K7,100, 20% | 2026 | same |
| PAYE band 3 | K7,100.01 to K9,200, 30% | 2026 | same |
| PAYE band 4 | Above K9,200, 37% | 2026 | same |
| Skills Development Levy | 0.5% of gross emoluments, borne by the employer | 2026 | https://www.zra.org.zm/wp-content/uploads/2023/06/Skills-Development-Levy.pdf |
| NAPSA rate | unverified: old file 5% employee plus 5% employer; prescribed by regulation under Act of 2026, s. 24 | 2026 | unverified |
| NAPSA ceiling | unverified: old files gave K34,164 and K37,236 earnings equivalents | 2026 | unverified |
| NHIMA rate | unverified: old files disagreed, 1% total against 2% total | 2026 | unverified |

Bands in full are held here; [Income tax](zm-income-tax.md) applies them. The old pack figure of 37.5% was out of date against ZRA's 2026 page.

## The base

Emoluments: wages, salaries, overtime, leave pay, commissions, fees, bonuses, all cash allowances, and employer-paid rent, bills, school fees and club fees. Exempt per ZRA: pension benefits, gratuity, redundancy, severance, salary in lieu of notice, repatriation, ex gratia to a surviving spouse, medical and funeral expenses, labour day awards, per diem. Since 2018 pension contributions are not deducted before chargeable income. Casual workers use casual tables. Employer deduction for each differently abled employee: K2,500 (s. 43D, from 1 January 2026).

## Deadlines and filing

PAYE return ITF/P16 and payment by the 10th of the following month. Skills levy is reported on the same return; ZRA's due date page says on or before the 10th. Under the National Pension Scheme Act 2026, an employer applies to register within one month of the first employee and files monthly returns; the Act starts on a date to be appointed, and the employer may not deduct its own share from pay (s. 24(4)).

**How to file PAYE.** Log in at the ZRA portal (www.zra.org.zm, tax portal) with TPIN, password and captcha, enter the one-time password sent to email and phone, then choose Returns, File a return. Enter tax type PAYE, account name, return period (for example 1 to 31 January). Click Next. Answer the questions (ZDA licence? skills levy?). Enter each employee: TPIN, chargeable income, tax deducted, tax credit if any, adjustments. Click Next. Confirm the summary, click Submit. A reference number is generated. The return can be amended.

Leaver: give form ITF/P13. PAYE refund claim: ITF/1A on the portal within 6 years of employment ending (3 years for a deceased person's claim).

## Penalties and interest

PAYE late return: 1,000 penalty units (individual) or 2,000 (company) per month or part month; one unit is K0.40. Late payment: 5% plus Bank of Zambia discount rate plus 2%. Skills levy: late return 1,000 units per month; late payment 5%; incorrect return per ZRA page negligence 25%, fraud 75%. National Pension Scheme Act: failure to register as an employer is an offence.

## Cross-border points

Tax is charged on emoluments for work in Zambia. Treaty relief and expatriate rules: not read; refer.

## Two worked examples that recompute

**Simple.** ZRA's K15,000 example.

```oa-check
name: PAYE K15,000
inputs:
  pay: 15000
steps:
  - b2: (7100 - 5100) * 0.20
  - b3: (9200 - 7100) * 0.30
  - b4: (pay - 9200) * 0.37
  - paye: b2 + b3 + b4
expected:
  paye: 3176.00
  b4: 2146.00
```

**Edge: pay inside band 3, with levy.** Gross K8,000.

```oa-check
name: PAYE and levy K8,000
inputs:
  pay: 8000
steps:
  - paye: 400 + (pay - 7100) * 0.30
  - sdl: pay * 0.005
expected:
  paye: 670.00
  sdl: 40.00
```

## Ask the client first

- Number of staff, and first hire date?
- Gross pay and all benefits paid by the employer?
- Casual or permanent?
- Annual turnover (levy exemption)?
- Any differently abled employees?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) (No. 2) Act No. 17 of 2025, whole Act; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf | 2026-11-01 |
| National Pension Scheme Act 2026, ss. 1, 18, 24; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2072%2C%20The%20National%20Pension%20Scheme%20Act%20%281%29.pdf | 2026-11-01 |
| ZRA Tax Information page, Turnover Tax and PAYE sections; read for the figures cited | https://www.zra.org.zm/tax-information/ | 2026-11-01 |
| ZRA Payment Due Dates page; read for the figures cited | https://www.zra.org.zm/payment-due-dates/ | 2026-11-01 |
| ZRA Penalties page (penalty unit K0.30: stale against the 2026 leaflets); read for the figures cited | https://www.zra.org.zm/penalties/ | 2026-11-01 |
| ZRA leaflet PAYE (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/PAYE.pdf | 2026-11-01 |
| ZRA Guide to Filing Tax Returns (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Guide-to-Filing-Tax-Returns.pdf | 2026-11-01 |
| ZRA leaflet Post-Registration Requirements (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Post-Registration-Requirements.pdf | 2026-11-01 |
| ZRA leaflet Skills Development Levy (2023); read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2023/06/Skills-Development-Levy.pdf | 2026-11-01 |

Not yet confirmed: NAPSA rate, ceiling and remittance date (napsa.co.zm opens only its home page; no contribution page found); commencement of the 2026 Act; NHIMA rate and base (no official rate page found; Act 25 of 2026 only changes the Board); minimum wage orders; levy exemption wording (a K800,000 employer test appears in the leaflet but the OCR is partial); levy wilful default rate (ZRA page prints 5%, likely a typo).

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
