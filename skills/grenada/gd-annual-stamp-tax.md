---
name: gd-annual-stamp-tax
description: >
  Grenada annual stamp tax on business gross receipts for 2026. Covers the base (the
  preceding year's gross receipts), 0.5% below EC$300,000 and 0.7% at EC$300,000 or
  more with the first EC$36,000 exempt, the EC$100 minimum, the 31 March return, the
  2026 extension to 30 April, nine monthly instalments from April to December, the late
  filing and late payment penalties and interest, and the rate cliff at EC$300,000.
  Trigger phrases include Grenada annual stamp tax, AST Grenada, gross receipts tax.
version: 1.0
jurisdiction: GD
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Grenada annual stamp tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Annual stamp tax (AST) under the Annual Stamp Tax Act, Chapter 16A (Act 36 of 1992 as amended), for the 2026 tax year, which is based on 2025 gross receipts. It is a tax on a business's gross receipts, not a duty on a property transfer document, and not VAT ([gd-vat-registration](gd-vat-registration.md)). Amounts are EC$. The Inland Revenue Division (IRD) site now redirects to a social media page; its June 2026 page is read from a web.archive.org copy.

## Ask the client first

1. Is the person engaged in a business (individual, trust, estate, company, partnership)? Is it registered with the Comptroller for AST?
2. Gross receipts for 2025, by type (sales of goods and services, investment, rental, interest, dividends, royalties, commissions and fees, other income not of a capital nature).
3. Any capital receipts in that total (excluded).
4. Has the 2026 return been filed, and which instalments have been paid?
5. Any special relief or exemption claimed (with the instrument)?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Rate, gross receipts under EC$300,000 | 0.5% | [IRD annual stamp tax page, archived 6 June 2026](https://web.archive.org/web/20260606105014/https://www.ird.gd/taxes/annual-stamp-tax) |
| Rate, gross receipts of EC$300,000 and above | 0.7% (effective 2018) | same |
| Exemption | The first EC$36,000 is exempt when applying the rate | same |
| Minimum tax | EC$100 | same |
| Return | By 31 March of the assessment year (s.6(2)) | [Annual Stamp Tax Act Cap. 16A](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap16A-ANNUAL-STAMP-TAX-ACT.pdf) |
| 2026 extension | Filing and payment of AST, personal and corporate income tax extended to 30 April 2026 | [IRD press release, 31 March 2026](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) |
| Payment | Nine equal monthly instalments, April to December of the year the tax is payable (s.13(1)) | [Annual Stamp Tax Act Cap. 16A](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap16A-ANNUAL-STAMP-TAX-ACT.pdf) |
| Late filing penalty | Greater of: 5% of tax owing plus 1% a month; or EC$500 plus EC$100 a month; limited to EC$10,000 | [IRD annual stamp tax page, archived 6 June 2026](https://web.archive.org/web/20260606105014/https://www.ird.gd/taxes/annual-stamp-tax) |
| Late payment fee | 20% of the tax due but not paid | same |
| Interest | 1.5% a month or part month, compounded | same |
| Failure to pay (offence) | Fine not exceeding the sum of ten thousand dollars on summary conviction (s.16) | [Annual Stamp Tax Act Cap. 16A](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap16A-ANNUAL-STAMP-TAX-ACT.pdf) |

### Steps

1. **Base:** 2025 gross receipts (Second Schedule list), excluding capital receipts. Never use accounting profit.
2. **Rate:** choose the rate on the whole gross receipts **before** the exemption: under 300,000 is 0.5%, 300,000 or more is 0.7%. It is not a two-band marginal calculation.
3. **Tax:** (gross receipts minus 36,000) x rate, not less than EC$100.
4. **File** by 31 March (30 April for 2026 only).
5. **Pay** in nine equal monthly instalments from April to December.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Consolidated Act text shows 0.25% and 0.5% bands | Superseded: the IRD page lists them only for periods before 2016, then a 2016 rate, then the current rates in the table above (effective 2018) | [IRD page, archived](https://web.archive.org/web/20260606105014/https://www.ird.gd/taxes/annual-stamp-tax); [Act Cap. 16A](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap16A-ANNUAL-STAMP-TAX-ACT.pdf) |
| Act s.13(2) says interest at 2% a month | The IRD page shows the lower compounded monthly rate in the table above; confirm the operative rule with the IRD before computing interest | same |
| 2026 extension | Applies to 2026 only; do not roll it into 2027 | [IRD press release](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) |
| Revised instalment schedule after the extension | The release does not set one; reconcile with the IRD | same |
| Receipts below EC$36,000 | Interaction of the exemption and the EC$100 minimum not resolved; ask the IRD | [IRD page, archived](https://web.archive.org/web/20260606105014/https://www.ird.gd/taxes/annual-stamp-tax) |

## Worked cases

### Case 1: two businesses

Gross receipts 200,000: rate 0.5% on 164,000 = 820. Gross receipts 400,000: rate 0.7% on 364,000 = 2,548, paid as nine instalments of about 283.11.

```oa-check
name: Grenada annual stamp tax on 200,000 and 400,000 gross receipts
inputs:
  low: 200000
  high: 400000
  exempt: 36000
steps:
  - low_tax: (low - exempt) * 0.005
  - high_tax: (high - exempt) * 0.007
  - instalment: round(high_tax / 9, 2)
expected:
  low_tax: 820
  high_tax: 2548
  instalment: 283.11
```

### Case 2 (decision): what the EC$300,000 cliff costs

At gross receipts of 299,000 the tax is 0.5% of 263,000 = 1,315. At 300,000 it is 0.7% of 264,000 = 1,848, so 1,000 more receipts cost 533 more tax. Check that receipts are measured correctly (capital receipts out, every income type in) when a business is near 300,000; do not defer or reclassify receipts without a legal basis.

```oa-check
name: Grenada stamp tax cliff at 300,000
inputs:
  below: 299000
  at: 300000
  exempt: 36000
steps:
  - tax_below: (below - exempt) * 0.005
  - tax_at: (at - exempt) * 0.007
  - extra_tax: tax_at - tax_below
expected:
  tax_below: 1315
  tax_at: 1848
  extra_tax: 533
```

## When to refuse or refer

- Special exemptions, hurricane or disaster relief, and capital-receipt questions.
- Businesses with no receipts or receipts below the exemption: confirm the minimum with the IRD.
- Penalty and interest disputes: refer.

## Filing and payment

1. Register with the Comptroller (s.3A) and file the return of 2025 gross receipts by 31 March 2026, extended to 30 April 2026.
2. Pay in nine equal monthly instalments from April to December; online through GTAX or at the IRD.
3. Keep the receipts schedule reconciled to accounts and bank, with each inclusion or exclusion documented.

## Completion checklist

- Base is prior-year gross receipts, not profit.
- Rate chosen before the exemption; 36,000 deducted; minimum 100.
- Return filed; nine instalments scheduled.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD annual stamp tax page (web.archive.org copy of 6 June 2026; the live site redirects to Facebook): read for the 0.5% and 0.7% rates, the EC$36,000 exemption, the EC$100 minimum, past rates, gross receipts, the penalties, interest and instalments | https://web.archive.org/web/20260606105014/https://www.ird.gd/taxes/annual-stamp-tax | 2026-11-14 |
| Annual Stamp Tax Act Cap. 16A (consolidated to Act 14 of 2005): read for ss.3, 3A, 5, 6(2), 13, 15, 16 and the Schedules | https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap16A-ANNUAL-STAMP-TAX-ACT.pdf | 2026-11-14 |
| IRD press release, 31 March 2026: read for the extension to 30 April 2026 | https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf | 2026-11-14 |

Not yet confirmed: the amending Acts for the 0.5%, 0.7% and EC$36,000 figures (only the IRD page states them; the consolidated Act predates them); whether interest is 1.5% compounded or the Act's 2%; the instalment schedule after the 2026 extension; treatment of receipts below EC$36,000.
