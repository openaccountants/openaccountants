---
name: dm-vat
description: >
  Commonwealth of Dominica VAT for 2026. Covers the 15% standard rate and the 10% rate
  for accommodation and diving activity, registration at EC$250,000 of annual taxable
  supplies, the three-month test (over EC$62,500 in three months with the next nine
  months taking the total past EC$250,000, apply within 21 calendar days) under SRO 49 of
  2016, the return within 20 calendar days after each period, payment by the 20th, the
  10% late payment penalty, and the tax fraction. Trigger phrases include Dominica VAT,
  Dominica VAT registration, Dominica VAT return, 15% VAT Dominica.
version: 1.0
jurisdiction: DM
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: vat-gst
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Dominica VAT

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Value Added Tax in the Commonwealth of Dominica for 2026, under the VAT Act and the VAT Regulations (SRO 9 of 2006) as amended by SRO 49 of 2016, as published by the Inland Revenue Division (IRD). Covers rates, registration, returns and payment, and output tax arithmetic. Amounts are EC$. It does not settle every exemption, input deduction rule, import liability or place-of-supply question.

## Ask the client first

1. Taxable supplies (standard-rated, accommodation and zero-rated) for the last 12 months and the last 3 months, and a supportable forecast for the next 9 months.
2. What is supplied: ordinary goods and services, accommodation or diving activity, zero-rated or exempt supplies?
3. Is the business a promoter of public entertainment or an auctioneer (special rules)?
4. Are prices quoted including VAT?
5. Tax period, output VAT and supported input VAT for the period.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Standard rate | 15% of the value of every taxable supply | [IRD value added tax](https://ird.gov.dm/tax-laws/value-added-tax) |
| Accommodation and diving activity | 10% | same |
| Return | Within 20 calendar days after the end of each tax period, whether or not tax is payable | same |
| Payment | By the 20th of the following month; an extension to file does not extend payment | same |
| Late payment penalty | 10% | same |
| Annual registration test | Standard-rated, accommodation and zero-rated supplies of EC$250,000 or more (registration guide); the FAQ says "in excess of" | [IRD VAT registration guide 2018](https://ird.gov.dm/phocadownload/guides/VAT%20-%20Registration%20Guide%202018.pdf) |
| Three-month test, reg.6(4) as amended | Taxable supplies over EC$62,500 in 3 months and reasonable grounds that those 3 months plus the next 9 will exceed EC$250,000; from 1 September 2016 | [SRO 49 of 2016](https://www.dominica.gov.dm/laws/2016/Value%20Added%20Tax%20%28Amendment%29%20Regulations%2C%202016%2C%20SRO%2049%20of%202016.pdf) |
| Applying under the three-month test | Within 21 calendar days after the end of that 3-month period | [SRO 9 of 2006](https://www.dominica.gov.dm/laws/2006/sro9-2006.pdf) |
| Public entertainment without approval | Fine EC$10,000 or two years' imprisonment or both, plus 15% of the value of tickets printed | [IRD value added tax](https://ird.gov.dm/tax-laws/value-added-tax) |

### Steps

1. **Monitor turnover** monthly against both tests; do not wait for the year end.
2. **Register** when either test is met; apply within 21 calendar days for the three-month test.
3. **Classify** each supply: 15%, 10% (qualifying accommodation or diving only, not a whole mixed package), zero-rated or exempt.
4. **Output tax:** net value x rate; on an inclusive price, price x 15/115 (or 10/110).
5. **Input tax:** only on supported invoices for taxable business use; do not treat all purchase VAT as recoverable.
6. **Return** within 20 calendar days, nil returns included; **pay** by the 20th.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Annual supplies exactly EC$250,000 | Guide says "or more", FAQ says "in excess of"; treat as registrable until the Act wording is checked | [IRD registration guide](https://ird.gov.dm/phocadownload/guides/VAT%20-%20Registration%20Guide%202018.pdf); [IRD FAQ](https://ird.gov.dm/f-a-q) |
| Filing extension granted | Payment date unchanged | [IRD value added tax](https://ird.gov.dm/tax-laws/value-added-tax) |
| Hotel package with meals and tours | The 10% rate is for accommodation and diving activity only; split the package | same |
| Public entertainment promoter or auctioneer | Special registration rules; check separately | same |
| Imports, reverse charge, refunds, deregistration, apportionment | Not covered; refer | not covered |

## Worked cases

### Case 1: output tax both ways and the reduced rate

A standard-rated supply of EC$10,000 before VAT: VAT 1,500, total 11,500. The tax inside 11,500 inclusive is 11,500 x 15/115 = 1,500. A qualifying accommodation supply of 10,000: VAT 1,000. If the 1,500 is paid late, the late payment penalty is 150.

```oa-check
name: Dominica VAT 15% and 10% on 10,000, and the tax fraction
inputs:
  net: 10000
steps:
  - standard_vat: net * 0.15
  - gross: net + standard_vat
  - fraction_vat: gross * 0.15 / 1.15
  - accommodation_vat: net * 0.10
  - late_penalty: standard_vat * 0.10
expected:
  standard_vat: 1500
  gross: 11500
  fraction_vat: 1500
  accommodation_vat: 1000
  late_penalty: 150
```

### Case 2 (decision): must a new business register now?

A business had taxable supplies of EC$70,000 in its first three months and a supportable forecast of 200,000 for the next nine. Both parts of the three-month test are met: 70,000 is 7,500 over 62,500, and 270,000 is 20,000 over 250,000. It must apply within 21 calendar days after the three months end. With a forecast of 170,000 instead, the 12-month total is 240,000, under 250,000, and the test is not met yet; keep monitoring.

```oa-check
name: Dominica three-month VAT registration test
inputs:
  three_months: 70000
  next_nine: 200000
  low_nine: 170000
steps:
  - over_quarter: three_months - 62500
  - twelve_months: three_months + next_nine
  - over_year: twelve_months - 250000
  - low_twelve: three_months + low_nine
  - low_margin: low_twelve - 250000
expected:
  over_quarter: 7500
  twelve_months: 270000
  over_year: 20000
  low_twelve: 240000
  low_margin: -10000
```

## When to refuse or refer

- The exact annual threshold boundary: resolve from the VAT Act before advising a business at exactly EC$250,000.
- Exemptions, zero-rating, blocked inputs, apportionment, imports, refunds and deregistration.
- Interest on late payment and late filing penalties: not on the IRD pages read.

## Filing and payment

1. Apply for registration on the IRD form (see the 2018 registration guide).
2. File the return for each tax period within 20 calendar days after it ends, even if nil.
3. Pay by the 20th of the following month to avoid the 10% late payment penalty ([IRD value added tax](https://ird.gov.dm/tax-laws/value-added-tax)).
4. Reconcile sales to output tax and keep support for every input claim.

## Completion checklist

- Both registration tests checked monthly.
- Each supply at 15%, 10%, zero or exempt; packages split.
- Return within 20 days; paid by the 20th.
- Inputs supported.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD value added tax page: read for the 15% and 10% rates, the 20-day return, payment by the 20th, extensions, the 10% late payment penalty and the public entertainment rule | https://ird.gov.dm/tax-laws/value-added-tax | 2026-11-14 |
| IRD VAT registration guide 2018, Part I: read for the EC$250,000 or more annual test and the three-month test | https://ird.gov.dm/phocadownload/guides/VAT%20-%20Registration%20Guide%202018.pdf | 2026-11-14 |
| IRD FAQ: read for "in excess of $250,000" | https://ird.gov.dm/f-a-q | 2026-11-14 |
| SRO 9 of 2006, VAT Regulations: read for regulation 6(4), applying within 21 calendar days after the 3-month period | https://www.dominica.gov.dm/laws/2006/sro9-2006.pdf | 2026-11-14 |
| SRO 49 of 2016, VAT (Amendment) Regulations: read for regulation 3 substituting EC$62,500 and EC$250,000 in regulation 6, in force 1 September 2016 | https://www.dominica.gov.dm/laws/2016/Value%20Added%20Tax%20%28Amendment%29%20Regulations%2C%202016%2C%20SRO%2049%20of%202016.pdf | 2026-11-14 |

Not yet confirmed: the VAT Act wording at exactly EC$250,000; interest and late filing penalties; any 2026 rate change (none shown on the IRD VAT page); special registration rules for auctioneers.
