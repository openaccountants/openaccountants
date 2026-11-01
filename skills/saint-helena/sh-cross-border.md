---
name: sh-cross-border
description: >
  Saint Helena island cross-border tax for tax year 2026. Covers non-resident taxation by source, permanent establishment business income, withholding on deposit interest, the foreign tax credit, associates and arm's length reallocation (the transfer pricing rule), tax avoidance, leaving the island, customs duty and land transfer duty. Use for non-resident, foreign tax, transfer pricing, import duty or property purchase questions on St Helena. Does not apply to Ascension or Tristan da Cunha.
version: 0.3
jurisdiction: SH
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Saint Helena island: cross-border points v0.3

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. It covers Saint Helena island only, not Ascension or Tristan da Cunha, which have separate laws.

## Who this applies to

Non-residents with Saint Helena income, residents with foreign tax, associated parties, importers, and buyers of land.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Scope of tax | Income earned, accrued or derived in or from Saint Helena (s.8) | 2026 | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 |
| Foreign tax credit | Credit for foreign tax paid by a resident, capped at the Saint Helena tax on that income; written claim within 4 years of the year end, up to 2 more if allowed (s.50) | 2026 | same |
| Withholding | 10% on bank-deposit interest paid by listed payers; remit within 15 days after month end; final if correctly deducted (ss.25 to 27) | 2026 | same |
| Withholding statement | Payee certificate at time of payment (Regulation 18); regulations 11 and 13 to 16 apply (Regulation 19) | 2026 | same |
| Arm's length | Commissioner may reallocate income, deductions or credits between associates (s.78) | 2026 | same |
| Stamp duty on land | 2.5% to £150,000; 3% on £150,000 to £500,000; 5% above £500,000 (Schedule Item D(a)) | 2026 | https://www.sainthelena.gov.sh/documents/20250707_Stamp-Duties-Ordinance_CONSOLIDATED |
| Second residential property | Additional 2.5% on full value if the buyer already owns residential property on St Helena (Item D(b)) | 2026 | same |
| First home relief | 0% to £100,000 for qualifying first-time buyers of a primary residence (Item D(c), (d)) | 2026 | same |
| Customs duty | Set line by line in the tariff, for example 5% or 20% ad valorem; the sample lines are 9619.00.40 at 5% and 9701.10.00 at 20% | 2026 | https://www.sainthelena.gov.sh/documents/St-Helena-Tariff-July-2025.pdf |

## The base

Non-residents: income from employment exercised on the island, wherever paid; business income attributable to activity there, including through a permanent establishment; and property income paid by a resident, deducted by a permanent establishment, or from property on the island (s.2). Tax Guide 12 states that tax is charged only on income earned in Saint Helena. Section 50 still gives a credit where a resident is liable on foreign-source income.

Transfer pricing: s.78 is the only rule. An associate is any person who acts or may act on the other's directions, including a spouse or child. The Ordinance prescribes no documentation or country-by-country report. Section 79 lets the Commissioner disregard or recharacterise a scheme with a main purpose of tax avoidance, or a transaction without substantial economic effect.

Customs: HM Customs controls imports and exports at Jamestown, Rupert's and the airport. The revenue it collects is based on import taxes; the page says the market does not allow for export tariffs. Liquor duty and excise also apply (HM Customs page).

## Deadlines and filing

Foreign tax credit: apply in writing with all information needed, including any refund of the foreign tax (s.50(2)). A later refund of foreign tax is repayable within 30 days (s.50(4)).

Leaving: file at least 14 days before departure if s.37(3) applies. The Commissioner may demand tax early if a person may leave without paying (Regulation 24).

Withholding: deduct when paying, remit within 15 days after month end, give a certificate at payment.

Imports: classify the goods on the tariff, then enter them with HM Customs. Customs opens Mondays to Fridays 09:00 to 15:00.

Land: duty on a transfer is payable under the Stamp Duties Ordinance. The additional 2.5% is refunded if the only other home is sold within six months. First home relief is clawed back on specified events within five years.

## Penalties and interest

Failure to deduct withholding: s.69, on top of the tax. Late remittance: 10% plus 1% a month (s.67). A s.78 adjustment that shows a false statement can lead to s.68 penalties.

## Cross-border points

Saint Helena is the subject of this skill. Check the other country's rules for its side. Whether any double tax arrangement covers Saint Helena is not confirmed: see below. Ascension and Tristan da Cunha are separate.

## Two worked examples that recompute

Example 1: resident with £10,000 foreign income, £3,000 foreign tax, and £2,600 Saint Helena tax on that income. The credit is capped at £2,600.

```oa-check
name: Credit cap
inputs:
  foreign_tax: 3000
  sh_tax: 2600
steps:
  - unrelieved: foreign_tax - sh_tax
expected:
  unrelieved: 400.00
```

Example 2: land only, £200,000, standard rates.

```oa-check
name: Stamp duty
inputs:
  first: 150000
  rest: 50000
steps:
  - duty: first * 0.025 + rest * 0.03
expected:
  duty: 5250.00
```


## Ask the client first

- Resident or non-resident?
- Where is the work or activity done?
- Foreign tax paid, and any refund?
- Related-party transactions?
- Goods imported, by HS code?
- Land being bought, and existing property owned?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Ordinance 2012 and Income Tax Regulations 2012, consolidation authoritative at 1 October 2021, read for the sections and regulations cited | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 | 2026-11-01 |
| Tax Guide 12, Questions on Taxes and Allowances (April 2024), read in full | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-12-Questions-on-Taxes-Allowances-on-St-Helena | 2026-11-01 |
| Stamp Duties Ordinance 1987, consolidated, read for Schedule Item D | https://www.sainthelena.gov.sh/documents/20250707_Stamp-Duties-Ordinance_CONSOLIDATED | 2026-11-01 |
| St Helena Tariff, July 2025, read for the schedule layout and the lines cited | https://www.sainthelena.gov.sh/documents/St-Helena-Tariff-July-2025.pdf | 2026-11-01 |
| HM Customs page, read in full | https://www.sainthelena.gov.sh/st-helena/government/portfolios/safety-security-and-home-affairs/hm-customs/ | 2026-11-01 |
| Government press releases, listing page 15 (23 March 2026 bill outcome; ExCo diesel item), read for the items cited; the listing page moves as new items appear | https://www.sainthelena.gov.sh/category/press-releases/page/15/ | 2026-11-01 |

Not yet confirmed: Double tax arrangements. Any withholding on non-resident dividends, royalties or fees: the Ordinance's withholding Part covers deposit interest only, and no other was found. The 2026 customs duty changes on alcohol, tobacco and vaping (ExCo Memo 05/2026): outcome not read, so the July 2025 tariff may be out of date on those lines. Diesel exemption extended to 31 March 2028 by ExCo approval; the order itself was not read. Excise tariffs and Liquor Duty rates. Stamp duty exemptions and the footnote stating the consolidation is authoritative at 1 April 2019 though it carries L.N. 23 of 2025.

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
