---
name: er-payroll-social
description: "Payroll in Eritrea: withholding under the Income Tax Proclamation, the National Pension covering public and private sectors, and the Labour Proclamation 118/2001 figures for hours, overtime, leave, notice and severance. Covers tax year 2026 in Eritrea from the gazette text. Use for questions such as: payroll tax in Eritrea, employer duties in Eritrea, Eritrea pension contributions, overtime pay in Eritrea, severance in Eritrea."
jurisdiction: ER
category: payroll
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea Payroll and Social Contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The newest income tax text we could open is Legal Notice 119/2012 and the newest sales tax text is Proclamation 117/2001. The Ministry of Justice list dated 2023 shows no later amendment to either. Nothing dated 2023 to 2026 could be opened, so check with the Inland Revenue Department that no later change exists.

## Who this applies to

Employers in Eritrea with employees. The National Pension covers both the public and private sectors (Proc 135/2003 art 4). No private sector contribution rate appears in that proclamation.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Employment band 1 | 2% | Monthly taxable income up to 200 Nakfa | Proc 116/2001 art 2, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Employment band 2 | 10% | 201 to 1,200 | same |
| Employment band 3 | 20% | 1,201 to 2,500 | same |
| Employment band 4 | 25% | 2,501 to 3,500 | same |
| Employment band 5 | 30% | Over 3,500 | same |
| Regular hours | 8 a day, 48 a week |  | Labour Proc 118/2001 art 48, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf |
| Overtime, day | 1.25 times | 6:00 to 22:00 | art 53, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf |
| Overtime, night | 1.5 times | 22:00 to 6:00 | same |
| Overtime, rest day | 2 times |  | same |
| Overtime, public holiday | 2.5 times |  | same |
| Annual leave | 14 working days plus 1 a year | Cap 35 | art 56, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf |
| Notice | 7, 14, 21 or 30 days | Under 1 year; 1 to 2; over 2 to 5; beyond that, unless the contract provides otherwise | art 30, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf |
| Severance | 2, 3, 4 weeks of wages a year | First 5 years; years 6 to 10; after 10; on last wage | art 32, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf |

## The base

Tax is on all pay in cash and benefits in kind (Proc 62/1994 art 10), see [Income tax](er-income-tax.md). Monthly, with longer payments prorated.

## Deadlines and filing

Withhold, declare and pay to the Inland Revenue Department within one month from the end of the month (arts 13, 14). Steps: compute pay, apply bands, deliver declaration and payment, keep the receipt.

## Penalties and interest

An employer who fails to deduct and transmit is personally liable (art 14). Late payment costs 5% a month up to 50% (art 64).

## Cross-border points

Pay from abroad to a foreign representative is exempt under 183 days in a year; beyond that it is taxed for the entire stay (art 31(3); Legal Notice 20/1995 art 8). The 2% tax on citizens abroad is outside payroll, see [Income tax](er-income-tax.md). National service rules are outside this skill.

## Two worked examples that recompute

**Case 1: gross 5,000.** Tax is 1,064.

```oa-check
name: Monthly pay
inputs:
  pay: 5000
steps:
  - band_1: min(pay, 200) * 0.02
  - band_2: (min(pay, 1200) - min(pay, 200)) * 0.10
  - band_3: (min(pay, 2500) - min(pay, 1200)) * 0.20
  - band_4: (min(pay, 3500) - min(pay, 2500)) * 0.25
  - band_5: (pay - min(pay, 3500)) * 0.30
  - tax: band_1 + band_2 + band_3 + band_4 + band_5
expected:
  tax: 1064.00
```

**Case 2, a decision: terminate after 7 years?** Weekly wage 1,000: five years at 2 weeks plus two at 3 is 16 weeks, 16,000 Nakfa.

```oa-check
name: Severance after seven years
inputs:
  week: 1000
steps:
  - first: 5 * 2 * week
  - next: 2 * 3 * week
  - total: first + next
expected:
  total: 16000.00
```

## Ask the client first

- Monthly cash pay and benefits?
- Local or foreign employee, and days present?
- Length of service?
- More than one employer?
- Does the contract change notice?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Proclamation 62/1994, read in full (scan, OCR) | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-01 |
| Proclamation 116/2001, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf | 2026-11-01 |
| Income Tax Regulations, Legal Notice 20/1995, arts 7 to 20 and penalties read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf | 2026-11-01 |
| National Pension Establishment Proclamation 135/2003, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-135-2003/eritrean-proc-135-2003.pdf | 2026-11-01 |
| Labour Proclamation 118/2001, arts 30, 32, 48 to 56 read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-118-2001/eritrean-proc-118-2001.pdf | 2026-11-01 |
| Ministry of Justice, thematic list of domestic legislations, section 16 read | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-01 |

Scans were read by OCR and the key rate pages checked by eye. The Library of Congress item pages show a security check, which we did not pass; the PDFs came straight from its public file host. Scanned gazettes use "Birr" in 1994 and "Nakfa" in later amendments.

Not yet confirmed: Private sector pension contribution rate, wage base and cap: Proc 136/2003 covers the public sector and was not read; no private rate was found. Whether the 2% rehabilitation tax on salaries in Proc 17/1991 art 4 survives Proc 66/1994: not read, so do not withhold it on this skill alone. National Service Proclamation 82/1995 and its pay effect: not read. Exact severance eligibility in art 32(1). No published 2026 amendment, circular or form could be opened; the Ministry of Finance site did not connect. No official portal or online filing page could be opened either.

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
