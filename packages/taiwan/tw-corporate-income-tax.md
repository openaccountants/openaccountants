---
name: tw-corporate-income-tax
description: "Use this skill for Taiwan profit-seeking enterprise income tax (營利事業所得稅) for tax year 2026, returns due 31 May 2027 for calendar-year enterprises. It covers the 20% rate, the NT$120,000 exemption and the half-excess cap up to NT$200,000, the 5% surtax on undistributed earnings, the September provisional payment of half the prior year's tax, 10-year loss carry-forward, late filing surcharges and final withholding on dividends (21%), interest (20% or 15%) and royalties (20%) paid to non-residents. Built from the law, not reviewed by an accountant."
jurisdiction: TW
tax_year: 2026
tax_year_notes: "Tax year 2026 (民國115年度) for calendar-year enterprises: provisional tax 1 to 30 September 2026, final return 1 to 31 May 2027."
version: "2.0"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Taiwan profit-seeking enterprise income tax (營利事業所得稅), tax year 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Taiwan.

## Who this applies to

Profit-seeking enterprises (companies, sole proprietorships and partnerships, limited partnerships) with their head office in Taiwan are taxed on worldwide income, with a credit for foreign tax; enterprises with their head office abroad are taxed on Taiwan-source income, largely by final withholding where there is no fixed place of business or agent in Taiwan. Authority: Ministry of Finance through the National Taxation Bureaus. Individual owners' tax: `tw-income-tax`. Business tax on sales: `taiwan-vat`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Taxable income up to NT$120,000 | Exempt | Income Tax Act art. 5 | https://www.ntbt.gov.tw/singlehtml/0baa381b53034993a08862dfde2243b9?cntId=08f87d2104c04266a40e67c00d7c5c5a |
| Taxable income above NT$120,000 | 20% | On the whole taxable income | same |
| Half-excess cap | Tax = (income less 120,000) x 1/2 | Where taxable income is NT$200,000 or less | same |
| Surtax on undistributed earnings | 5% | Filed and paid 1 to 31 May of the year after the income year's return (2026 earnings: May 2028) | same |
| Annual return (calendar year) | 1 to 31 May of the following year | Next working day if the last day is a holiday; special year ends: within the 5th month after year end | same |
| Late filing surcharge (滯報金) / failure to file (怠報金) | 20% of the assessed tax if not filed within 15 days of the late filing notice | Lower surcharge if filed within 15 days of the notice (rate not restated) | same |
| Loss carry-forward | 10 years | Companies with complete books using blue returns or CPA certification (Income Tax Act art. 39) | same |
| Provisional tax (暫繳) | Half of the prior year's final tax | Paid and filed 1 to 30 September 2026 for calendar-year enterprises; or a trial computation on six months' results where books are CPA-certified | https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=5fe89bb53a38459ab2c8ac493a57e13a |
| Provisional tax exemption | NT$2,000 or less | Half of the prior year's tax at or below this need not be filed | same |
| Non-resident withholding, dividends | 21% | Treaty rates 3% to 15% | https://www.mof.gov.tw/singlehtml/191?cntId=82761 |
| Non-resident withholding, royalties | 20% | Same | same |
| Non-resident withholding, interest on bonds, bills, securitised products and repos | 15% | Other interest 20% | same |
| Late payment surcharge | 1% per 3 days, capped at 10% | Tax Collection Act art. 20 | https://www.ntbt.gov.tw/singlehtml/2dbb2b6ec3714b469267299f687be37c?cntId=6047d2df3fb144a6abb413dd828da9b7 |
| Basic tax (AMT), enterprises | Basic income exemption 60萬 (600 thousand NT dollars) | Not adjusted for 2026 | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c |

## The base

1. **Accounting profit** for the year, adjusted to tax rules (non-deductible items, depreciation, entertainment limits).
2. **Less** tax-exempt income (with its related costs), and **losses** of the previous 10 years where the conditions are met (exempt income must first absorb losses).
3. **Taxable income (課稅所得額).** Exempt if NT$120,000 or less; otherwise 20%, capped at half the excess over 120,000 while income is NT$200,000 or less (the cap stops binding at 200,000, where both give 40,000).
4. **Less credits:** foreign tax on foreign-source income (limited to the Taiwan tax on it), Mainland-source tax credit, provisional tax and withholding.
5. **Basic tax:** compare with the basic tax under the Income Basic Tax Act (rate not confirmed here) and pay the higher.
6. **Undistributed earnings:** in the May after the year's return is filed (for 2026: May 2028), compute that year's undistributed earnings and pay 5% on them; a zero or negative result must still be filed. Branches of foreign companies were outside this surtax under the old file (not confirmed here).

## Deadlines and filing

- **Provisional:** 1 to 30 September 2026 (tax year 2026, calendar year); no extension unless the last day falls on a holiday. If not filed, the bureau assesses half of the prior year's tax and adds daily interest.
- **Final:** 1 to 31 May 2027, together with the undistributed earnings return for 2025. Online filers send signed attachments by 30 June.
- **Cessation, merger or transfer:** final and undistributed earnings returns within 45 days.

## Penalties and interest

Late payment: 1% for each 3 days late up to 10%, then interest. Failure to file after a late filing notice: 20% of the assessed tax if still not filed 15 days after the notice. Under-reporting: fines under Income Tax Act art. 110 (rates not restated).

## Cross-border points

- Non-resident enterprises without a fixed place of business in Taiwan: final withholding on dividends 21%, royalties 20%, interest 20% (15% on bonds and similar); tax treaties reduce dividends, interest and royalties to 3% to 15%.
- Resident enterprises: foreign tax credit; Mainland China-source income is taxed with a credit for Mainland tax.
- Payments to residents (interest, royalties, professional fees) carry withholding; the rate is on the Not yet confirmed line, so take it from the MOF withholding rules before applying it.
- Global minimum tax: whether and how it applies to in-scope MNE groups is on the Not yet confirmed line (no MOF page read).

## Two worked examples that recompute

**Example 1: small company, taxable income NT$180,000 and NT$1,000,000.** At 180,000: 20% gives 36,000, but the cap is (180,000 less 120,000) x 1/2 = 30,000, so tax is NT$30,000. At 1,000,000: 20% = NT$200,000 (the cap no longer applies).

```oa-check
name: TW 2026 enterprise tax with the half-excess cap
inputs:
  small: 180000
  large: 1000000
steps:
  - small_tax: min(small * 0.20, (small - 120000) / 2)
  - large_tax: min(large * 0.20, (large - 120000) / 2)
expected:
  small_tax: 30000
  large_tax: 200000
```

**Example 2: decision, distribute 2026 earnings or retain them.** A company has 2026 after-tax earnings of NT$800,000. If none is distributed by the end of 2027, the 5% surtax on 2026 undistributed earnings is filed and paid in May 2028 (the year after the 2026 return): NT$40,000. If it distributes them during 2027, the surtax falls away but shareholders are taxed on the dividends (individuals at their marginal rate or 28%, see `tw-income-tax`; non-residents 21%). A non-resident parent receiving the 800,000 pays 168,000 at 21% unless a treaty lowers it. The deciding figures are the shareholders' dividend rate against 5%.

```oa-check
name: TW 2026 undistributed earnings surtax vs non-resident dividend tax
inputs:
  earnings: 800000
steps:
  - surtax_if_retained: earnings * 0.05
  - nonresident_dividend_tax: earnings * 0.21
expected:
  surtax_if_retained: 40000
  nonresident_dividend_tax: 168000
```

## Ask the client first

1. Entity type, head office location and accounting year end.
2. Taxable income estimate for 2026 and prior-year tax (provisional payment).
3. Losses brought forward and whether books are CPA-certified or on blue returns.
4. Foreign or Mainland-source income and tax paid.
5. Planned distributions and shareholder residence.
6. Payments to non-residents (dividends, interest, royalties, service fees).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Taipei National Taxation Bureau, profit-seeking enterprise income tax page. Read for the rate table, 120,000 exemption, half-excess formula, May filing, 5% undistributed earnings, late filing surcharge, 10-year losses and 45-day cessation returns | https://www.ntbt.gov.tw/singlehtml/0baa381b53034993a08862dfde2243b9?cntId=08f87d2104c04266a40e67c00d7c5c5a | 2026-11-14 |
| MOF, 2026 provisional tax news. Read for the 1 to 30 September 2026 window, half of prior-year tax and the NT$2,000 exemption | https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=5fe89bb53a38459ab2c8ac493a57e13a | 2026-11-14 |
| MOF, withholding rates on non-resident dividends, interest and royalties. Read for 21%, 20%, 15% and treaty range 3% to 15% | https://www.mof.gov.tw/singlehtml/191?cntId=82761 | 2026-11-14 |
| Taipei National Taxation Bureau, surcharge calculation. Read for the 10% cap and 3-day steps | https://www.ntbt.gov.tw/singlehtml/2dbb2b6ec3714b469267299f687be37c?cntId=6047d2df3fb144a6abb413dd828da9b7 | 2026-11-14 |
| MOF, 2026 amounts table (PDF). Read for the enterprise basic income exemption of 60萬 | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c | 2026-11-14 |

Not yet confirmed: resident withholding rate on interest, royalties and professional fees (old file: 10%); the global minimum tax rate (old file: 15%); the enterprise basic tax rate (old file: 12%) and any 15% global minimum tax rate for MNE groups; resident withholding rates (old file: 10%); the exclusion of foreign branches from the undistributed earnings surtax; the number of tax treaties (old file: about 35); the lower late filing surcharge rate.
