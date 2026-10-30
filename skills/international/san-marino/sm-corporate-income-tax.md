---
name: sm-corporate-income-tax
description: >
  San Marino corporate income tax (IGR on legal persons) for tax year 2026, under Law 166/2013 Title III as reformed by Law 141/2025 and Delegated Decree 156/2026. Covers company residence by registered office or effective management, the 18% rate for tax years 2026 to 2030 (statutory 17%), the base from accounting profit, expense limits, depreciation under Annex D, the 70% annual cap on loss carryforward, the 50% rate cut for qualifying new companies, the 10% own-capital increase deduction, foreign tax credit, the 35% and 55% advances due 31 August and 30 November, the 31 July return and balance, late interest and late-filing charges. Use for San Marino company tax, SRL or SPA tax, new-company incentive, corporate losses and corporate filing questions. Special sector regimes, reorganisations and insolvency need their own facts.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
---

# San Marino corporate income tax v0.4

Tax year: the company's tax period in 2026 (calendar year for most companies). Currency EUR. Authority: UO Ufficio Tributario (Tax Office).

Law 141/2025 reformed IGR from tax year 2026 ([Law 141/2025, art 54(1)][l141]); Delegated Decree 156/2026 of 12 October 2026 amended it again from tax year 2026 ([DD 156/2026, art 19][dd156]). The official coordinated IGR text (updated to 22 December 2025) includes Law 141/2025 but not DD 156/2026.

## 1. Who this applies to

- **Resident** legal persons and assimilated entities pay IGR on worldwide income. A legal person is resident if its registered office (sede legale) **or** its place of effective management is in San Marino for most of the tax period ([IGR art 42(1)-(2)][igr]).
- **Non-resident** legal persons pay IGR on San Marino-source income listed in article 5, including business carried on through a San Marino permanent establishment ([IGR arts 4-5, 42(1)(f)][igr]).
- Partnerships are transparent: profit is attributed to partners ([IGR art 10(3)][igr]). Sole traders and professionals use `sm-income-tax` (18% separate rate).

Out of scope: special regimes for banks, insurers and financial companies, reorganisations, insolvency (changed by DD 156/2026, arts 13-14) and technology-company regimes.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Corporate IGR rate, tax years 2026 to 2030 | 18% of taxable income | 2026 | [Law 141/2025, art 54(6)][l141] |
| Statutory corporate rate (applies again from 2031 unless changed) | 17% | 2026 | [IGR art 43(1); Annex C, art C2][igr] |
| Loss carryforward | No time limit; use capped at 70% of taxable business income each year | 2026 | [IGR art 46(5)][igr] |
| New-activity incentive (qualifying new company) | 50% cut in the rate for the first five tax periods: 9% in 2026 | 2026 | [IGR art 73(1)(c), (2)][igr]; [Law 141/2025, art 54(6)][l141] |
| New-activity licence-fee relief | No first licence fee; no annual licence fee for the next three years | 2026 | [IGR art 73(1)(a)-(b)][igr] |
| Own-capital (equity) increase deduction | 10% of the year's increase in own capital, net of the year's result; unused amounts lapse | 2026 | [IGR art 74(1)-(3)][igr] |
| Accelerated depreciation (tangible assets, not buildings) | Up to 20% extra in each of the first two tax periods | 2026 | [IGR Annex D, art D3(3)][igr] |
| Higher depreciation for intensive use or obsolescence | Up to 50% above the ordinary coefficient, buildings excluded, only after a ruling request to the Tax Office | 2026 | [IGR Annex D, art D3(1)-(2)][igr] |
| Intangible assets | Up to 20% a year | 2026 | [IGR Annex D, art D4(1)][igr] |
| First advance | 35% of prior-year IGR (net of foreign tax credits on business income), by 31 August | 2026 | [IGR art 124(2)][igr] |
| Second advance | 55% of the same basis, by 30 November | 2026 | [IGR art 124(2)][igr] |
| Return and balance | 31 July following the tax year | 2026 | [IGR arts 93(1), 124(1)][igr] |
| Late payment interest | Legal rate plus 2 points | 2026 | [IGR art 128(2)][igr] |

## 3. The base

1. **Start from the accounts.** Taxable income is business income determined under Title III from complete accounts and fiscal records, with income and costs in the correct period ([IGR arts 45-48][igr]). An unrecorded receipt is still taxable; a capital asset is depreciated, not expensed when paid.
2. **Disallowed costs.** Income taxes, related tax penalties and interest, and costs of criminal activity are not deductible; directors' pay is deductible under its payment rule ([IGR art 49][igr]). Article 50 sets ceilings for general costs such as advertising, data processing and entertainment; DD 156/2026 repealed article 50(4-bis)(b) ([IGR art 50][igr]; [DD 156/2026, art 20][dd156]).
3. **Depreciation and provisions.** Use the Annex D coefficients by asset group, recorded in the depreciable-assets register. Depreciation starts in the first period the asset is used or usable, at the full annual rate regardless of month. New companies can start depreciation in the first period with revenue ([IGR Annex D, arts D1-D3][igr]). Non-capitalised research and advertising costs are deductible in the year or spread over that year and the next three ([IGR Annex D, art D4(4)][igr]).
4. **Related parties.** Dealings with companies that control, are controlled by or share a controller with the taxpayer are valued at normal value where that increases income ([IGR art 46(4)][igr]). Use `sm-transfer-pricing`.
5. **Crypto-assets.** Year-end valuation gains and losses on crypto-assets do not count in income, whatever the accounting entry ([IGR art 46(5-bis)][igr]).
6. **Incentives.** The 10% own-capital deduction uses the year's increase in own capital, excluding the year's result, retained-earnings reserves made under Title IV Chapter I and legally required reserves. If shareholders later reduce capital other than for losses, the benefit is repaid in proportion ([IGR art 74][igr]).
7. **Losses.** Documented tax losses carry forward without time limit and can absorb at most 70% of the year's taxable business income ([IGR art 46(5)][igr]). Keep a schedule by year of origin.
8. **Tax.** Apply 18% to the result. Then deduct foreign tax credit (section 6), advances paid and tax withheld on account ([IGR art 124(3)][igr]).

### New-activity incentive conditions

The 50% rate cut applies to a newly formed capital company whose shareholders and beneficial owners have not carried on a similar business in the twelve months before the request, and which hires at least one full-time employee (a full-time director counts) within six months of authorisation to operate and a second within 24 months ([IGR art 73(2)][igr]). The cut runs for the first five tax periods; the company can defer the start to no later than the first period after the one in which the new activity starts ([IGR art 73(1)(c)][igr]). It applies only on the company's option ([IGR art 73(4)][igr]). Losing a condition (including through a share transfer) ends the benefit for the current and later periods ([IGR art 73(2), (5)][igr]). Intangible-asset businesses are also subject to Decree-Law 76/2018 ([IGR art 73(6-bis)][igr]). For 2026 the cut applies to the 18% rate, giving 9%.

## 4. Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Annual electronic return, transmitted by 24:00 | 31 July following the tax year (31 July 2027 for 2026) | [IGR art 93(1), (4)][igr] |
| Balance of tax | Same date as the return | [IGR art 124(1)][igr] |
| First advance (35%) | 31 August of the tax year | [IGR art 124(2)][igr] |
| Second advance (55%) | 30 November of the tax year | [IGR art 124(2)][igr] |
| Withholding remittance as payer | By the two-month period after the one in which tax was withheld | [IGR art 125(1)][igr] |

Advances are not due if the activity is suspended or ceased before the due date ([IGR art 124(2)][igr]). Amounts owed can be set off against IGR, import-tax or other Tax Office credits on the taxpayer's fiscal account ([IGR art 126][igr]). Keep the payment receipt until the assessment period ends ([IGR arts 124(1), 127][igr]).

A return filed within 30 days after 31 July is valid with the late-filing charge; a later return is null and cannot support a refund claim, though tax shown on it can still be collected ([IGR art 93(2)-(3)][igr]).

## 5. Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late return (art 137(2)(a)) | 400 | [IGR art 139(1)(d), replaced by DD 156/2026, art 16][dd156] |
| Late return filed within 30 days of the deadline | 200 | [DD 156/2026, art 16][dd156] |
| Late payment interest | Legal interest rate plus 2 points, from the due date to payment; not charged on penalties | [IGR art 128][igr] |
| Assessment paid within 60 days of notice | Penalties reduced by 50% | [IGR art 129][igr] |

Articles 138 and 139 set separate penalties for non-payment, late payment, failure to withhold and false or omitted returns ([IGR arts 137-139][igr]).

## 6. Cross-border points

- **Foreign tax credit.** Final, non-refundable foreign tax on foreign income included in the base is credited up to the share of net San Marino tax that foreign income bears to total income, computed per State ([IGR art 44][igr]). For income not earned through a foreign permanent establishment, foreign income for this fraction is total income x foreign gross receipts / total receipts ([IGR art 44(8)][igr]).
- **Permanent establishment.** A construction or installation site is a San Marino permanent establishment only if it lasts more than three months ([IGR art 4][igr]).
- **Payments abroad.** Withholding on dividends (5% to individuals), interest (13%), professional services (20%) and equipment rentals (10%): see `sm-cross-border`.
- **International advance agreements** on transfer prices, PE status and entry and exit values: Delegated Decree 116/2026, see `sm-transfer-pricing`.

## 7. Two worked examples that recompute

### Example 1: ordinary company with brought-forward losses

Book profit 100,000; a 2,000 tax penalty was expensed and is added back; 90,000 of documented losses are brought forward. Pre-loss taxable income 102,000. Loss use is capped at 70%: 71,400. Taxable income 30,600; IGR at 18% = 5,508. Losses carried forward: 18,600.

```oa-check
name: San Marino 2026 corporate bridge with 70% loss cap
inputs:
  book_profit: 100000
  nondeductible_tax_penalty: 2000
  documented_unused_losses: 90000
  statutory_loss_limit: 0.70
  rate_2026: 0.18
steps:
  pre_loss_taxable_income: book_profit + nondeductible_tax_penalty
  annual_loss_ceiling: pre_loss_taxable_income * statutory_loss_limit
  losses_used: min(documented_unused_losses, annual_loss_ceiling)
  taxable_income_after_losses: pre_loss_taxable_income - losses_used
  ordinary_igr: taxable_income_after_losses * rate_2026
  losses_remaining: documented_unused_losses - losses_used
expected:
  pre_loss_taxable_income: 102000
  annual_loss_ceiling: 71400
  losses_used: 71400
  taxable_income_after_losses: 30600
  ordinary_igr: 5508
  losses_remaining: 18600
```

### Example 2: qualifying new company, advances in the next year (edge case)

A new company meets every article 73 condition and has opted in. Taxable income 200,000. Ordinary IGR at 18% would be 36,000; with the 50% cut the rate is 9% and IGR is 18,000. In the following year its advances use 18,000 (no foreign credits) as the basis: 6,300 by 31 August and 9,900 by 30 November.

```oa-check
name: San Marino 2026 new-company half rate and next-year advances
inputs:
  taxable_income: 200000
  rate_2026: 0.18
  rate_reduction: 0.50
  first_advance_fraction: 0.35
  second_advance_fraction: 0.55
steps:
  ordinary_igr: taxable_income * rate_2026
  reduced_rate: rate_2026 * (1 - rate_reduction)
  reduced_igr: taxable_income * reduced_rate
  first_advance_next_year: reduced_igr * first_advance_fraction
  second_advance_next_year: reduced_igr * second_advance_fraction
expected:
  ordinary_igr: 36000
  reduced_rate: 0.09
  reduced_igr: 18000
  first_advance_next_year: 6300
  second_advance_next_year: 9900
```

The same rules give: a qualifying own-capital increase of 100,000 gives a 10,000 deduction that year only; with prior-year IGR of 20,000 less 2,000 foreign business-income credits, advances are 6,300 and 9,900, and a current-year IGR of 23,000 leaves a balance of 6,800.

## 8. Ask the client first

1. Registered office and where the board actually meets and decides, with dates.
2. Full accounts, fiscal ledgers, depreciable-assets register and any related-party dealings.
3. Loss schedule by year of origin, as shown in earlier returns.
4. Formation date, new-activity request and option, shareholders' and beneficial owners' prior activity, and hiring dates.
5. Prior-year IGR, advances paid and withholding suffered.
6. Foreign income and foreign tax paid, by State, with final assessments.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025: arts 4-5, 10, 42-50, 73-74, 93, 124-129, 137-139, Annexes C and D | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |
| Law 141/2025 of 12 November 2025, art 54 (commencement, 18% rate 2026-2030) | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html | 2026-10-30 |
| Delegated Decree 156/2026 of 12 October 2026, arts 13-14, 16, 19-20 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33 | 2026-10-30 |

Not yet confirmed: the 2026 legal interest rate; the full Annex D coefficient table by asset group; participation exemption and treatment of dividends received; the current implementing circular for article 73; the 2027 return forms.

[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[l141]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[dd156]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33

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
