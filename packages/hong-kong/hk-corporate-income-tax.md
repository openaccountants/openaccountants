---
name: hk-corporate-income-tax
description: "Use this skill for Hong Kong profits tax on corporations and unincorporated businesses for the year of assessment 2026/27 (1 April 2026 to 31 March 2027), the year that contains most of 2026. It covers the territorial source rule, the two-tiered rates (8.25% and 16.5% for corporations, 7.5% and 15% for unincorporated businesses, split at HKD 2,000,000), the connected-entity nomination rule, the FSIE regime, the 15% global minimum tax and HKMTT for large groups, provisional tax, filing under the block extension scheme and penalties. Built from the law, not reviewed by an accountant."
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (1 April 2026 to 31 March 2027). Filing dates shown are the 2025/26 cycle (returns issued 1 April 2026), the latest the IRD has published; the 2026/27 cycle is listed under Not yet confirmed."
version: "2.0"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Hong Kong profits tax (corporations and unincorporated businesses), year of assessment 2026/27

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Hong Kong.

## Who this applies to

Persons, including corporations, partnerships, trustees and bodies of persons, carrying on a trade, profession or business in Hong Kong, on profits arising in or derived from Hong Kong from that business, excluding profits from the sale of capital assets (Inland Revenue Ordinance (IRO), Cap. 112, s. 14). Hong Kong taxes on a territorial basis: a resident can derive profits from abroad without Hong Kong tax, and a non-resident can be taxed on Hong Kong-sourced profits. Source is a question of fact.

Out of scope here: salaries tax (`hk-salaries-tax`), MPF (`hk-mpf`), company set-up (`hk-company-formation`), property tax and stamp duty (`hong-kong-tax`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Corporation, first HKD 2,000,000 of assessable profits | 8.25% | Two-tiered rates, YA 2018/19 onwards; only one nominated entity per group of connected entities | https://www.ird.gov.hk/eng/tax/bus_pft.htm |
| Corporation, assessable profits above HKD 2,000,000 | 16.5% | Same | same |
| Unincorporated business, first HKD 2,000,000 | 7.5% | Same | same |
| Unincorporated business, above HKD 2,000,000 | 15% | Same | same |
| Connected entities | One entity only takes the two-tiered rates | The nominated entity; the others pay 16.5% or 15% on all profits | https://www.ird.gov.hk/eng/faq/2tr.htm |
| One-off reduction, YA 2025/26 final tax | 100%, capped at HKD 3,000 per business | Not for provisional tax; enacted, gazetted 22 May 2026 | https://www.ird.gov.hk/eng/tax/budget.htm |
| Renovation of business premises | Deducted over 5 years in equal instalments | From the year the expenditure is incurred | https://www.ird.gov.hk/eng/tax/bus_pft.htm |
| Plant and machinery annual allowance | 10%, 20% or 30% on reducing value | Rates set by the Board of Inland Revenue | same |
| Global minimum tax (IIR) and HKMTT | 15% | MNE groups with consolidated revenue of EUR 750 million or more in at least two of the four preceding fiscal years; fiscal years beginning on or after 1 January 2025 | https://www.ird.gov.hk/eng/tax/bus_beps.htm |
| Profits tax return, accounting date code "N" (1 April to 30 November 2025) | No extension | 2025/26 returns, represented taxpayers | https://www.ird.gov.hk/eng/pdf/bel26e.pdf |
| Code "D" (1 to 31 December 2025) | Extended to 17 August 2026 | Same | same |
| Code "M" (1 January to 31 March 2026) | Extended to 16 November 2026 | Same; further extension to 1 February 2027 for loss cases on request | same |
| Surcharge on unpaid tax | 5% on the whole balance of the demand notice | Recovery action under IRO Part XII | https://www.gov.hk/en/residents/taxes/taxfiling/consequences/consequencenotpaytax.htm |
| Additional tax (s. 82A) | Up to treble the tax undercharged | In lieu of prosecution, for incorrect returns and failures | https://www.ird.gov.hk/eng/pol/ppo.htm |
| Prosecution for failure to file or incorrect return (s. 80(2)) | Fine of HKD 10,000 plus treble the tax undercharged | Wilful evasion (s. 82): HKD 50,000, treble the tax and 3 years' imprisonment | same |

## The base

1. **Start from the accounts profit** for the basis period (the year of account ending in the year of assessment; for 2026/27, an accounting year ending between 1 April 2026 and 31 March 2027).
2. **Remove offshore profits and capital profits.** Profits not arising in or derived from Hong Kong, and profits from the sale of capital assets, are not chargeable (s. 14). Hong Kong has no tax on capital gains as such and no withholding tax on dividends or interest paid.
3. **Add deemed Hong Kong receipts.** Sums for the use in Hong Kong of films, tapes and sound recordings, and of patents, designs, trade marks, copyright and similar rights (and, if deductible to the payer, their use outside Hong Kong), are deemed Hong Kong receipts (s. 15).
4. **Apply the FSIE regime** (from 1 January 2023): for a member of a multinational enterprise group carrying on business in Hong Kong, specified foreign-sourced interest, dividends, IP income and disposal gains (disposal gains other than equity from 1 January 2024) are chargeable when received in Hong Kong, unless the entity meets the exception for that income type.
5. **Deduct expenses** incurred in producing chargeable profits (s. 16); disallow private, capital and proprietor's own remuneration or interest items (s. 17). Add capital allowances.
6. **Apply the two-tiered rates** to assessable profits, after checking the connected-entity nomination.
7. **Large groups:** a Part 4AA entity of an in-scope MNE group also computes IIR or HKMTT top-up tax and files a top-up tax return (the Pillar Two Portal opened top-up tax return filing on 26 October 2026).

### Payments to non-residents

Royalties paid to a non-resident for IP used in Hong Kong are taxed through the payer, which must withhold and pay the tax on the non-resident's behalf (IRO s. 20B and s. 21A). The deemed profit percentages (30% of the sum, or 100% where the IP was once owned by a person carrying on business in Hong Kong) and the resulting effective rates (4.95% and 16.5%) in the old file are not confirmed on an official page in this pass; see Sources.

## Deadlines and filing

- **Return issue:** profits tax returns for 2025/26 were issued on 1 April 2026 (2 April 2026 for some groups). A return is normally due within one month; represented taxpayers get the block extension by accounting date code (rates table).
- **2026/27:** returns are expected to issue in April 2027 under a new block extension letter.
- **Provisional tax:** with each final assessment, the IRD charges provisional tax for the next year based on the profits just assessed. It is applied first against the final tax of that next year; any excess goes to the following year's provisional tax. Holdover applications are possible on statutory grounds.
- **E-filing:** a further one-month extension is available for profits tax returns filed electronically through the IRD's portal.

## Penalties and interest

Unpaid tax: the Commissioner may add a 5% surcharge on the whole outstanding balance of the demand notice and take recovery action under IRO Part XII; any further surcharge on amounts still unpaid later is on the Not yet confirmed line, so do not apply one. Late or incorrect returns: additional tax up to treble the tax undercharged (s. 82A) or prosecution (s. 80(2), fine HKD 10,000 plus treble the tax undercharged). Wilful evasion (s. 82): HKD 50,000, treble the tax undercharged and up to 3 years' imprisonment.

## Cross-border points

- Territorial source: an offshore claim needs evidence of where the profit-producing operations took place.
- FSIE: foreign dividends, interest, IP income and disposal gains received in Hong Kong by an MNE entity are taxed unless an exception (economic substance, participation, nexus) is met.
- Hong Kong has comprehensive double taxation arrangements, including with the Mainland; treaty rates are not restated here.
- Pillar Two: IIR and HKMTT at 15% for in-scope groups from fiscal years beginning on or after 1 January 2025.

## Two worked examples that recompute

**Example 1: a company with HKD 3,000,000 of assessable profits in 2026/27, no connected entities.** Tax: 8.25% of HKD 2,000,000 = HKD 165,000, plus 16.5% of HKD 1,000,000 = HKD 165,000; total HKD 330,000.

```oa-check
name: HK 2026/27 corporation, two-tiered profits tax on HKD 3m
inputs:
  profits: 3000000
steps:
  - lower: min(profits, 2000000) * 0.0825
  - upper: max(profits - 2000000, 0) * 0.165
  - tax: lower + upper
expected:
  lower: 165000
  upper: 165000
  tax: 330000
```

**Example 2: decision, sole proprietorship or company for HKD 3,000,000 of profits.** Unincorporated: 7.5% of HKD 2,000,000 = 150,000 plus 15% of 1,000,000 = 150,000; total HKD 300,000. Corporation: HKD 330,000 (example 1). Hong Kong does not tax dividends, so the company's extra cost is HKD 30,000 a year at this profit level; the deciding factors are limited liability, the owner's salaries tax position on profits drawn as salary, and whether a connected entity already holds the two-tiered nomination (in which case the company pays 16.5% on everything: HKD 495,000).

```oa-check
name: HK 2026/27 unincorporated vs corporation on HKD 3m
inputs:
  profits: 3000000
steps:
  - sole: min(profits, 2000000) * 0.075 + max(profits - 2000000, 0) * 0.15
  - company: min(profits, 2000000) * 0.0825 + max(profits - 2000000, 0) * 0.165
  - company_not_nominated: profits * 0.165
  - extra_cost: company - sole
expected:
  sole: 300000
  company: 330000
  company_not_nominated: 495000
  extra_cost: 30000
```

## Ask the client first

1. Entity type (company, partnership, sole proprietor) and accounting year end.
2. Connected entities, and which one (if any) is nominated for the two-tiered rates.
3. Where the profit-producing operations take place, and any offshore claim.
4. Foreign-sourced income received in Hong Kong, and whether the entity belongs to an MNE group (FSIE); group consolidated revenue (Pillar Two).
5. Royalties or other payments to non-residents.
6. Whether a tax representative files (block extension) and any provisional tax holdover.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRD, profits tax page. Read for s. 14 charge, deductions, renovation, capital allowances and the two-tiered rates | https://www.ird.gov.hk/eng/tax/bus_pft.htm | 2026-11-14 |
| IRD FAQ on two-tiered rates. Read for the connected-entity nomination rule | https://www.ird.gov.hk/eng/faq/2tr.htm | 2026-11-14 |
| GovHK, profits tax rates. Read for the rate table | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/profitsrates.htm | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for territorial source, FSIE, deemed receipts, basis of assessment and provisional tax | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, 2026-27 Budget tax measures. Read for the YA 2025/26 reduction of 100% capped at HKD 3,000 | https://www.ird.gov.hk/eng/tax/budget.htm | 2026-11-14 |
| IRD, block extension circular letter for 2025/26 returns (PDF). Read for the N, D and M code dates and the loss-case extension | https://www.ird.gov.hk/eng/pdf/bel26e.pdf | 2026-11-14 |
| IRD, global minimum tax and HKMTT. Read for the 15% rate, EUR 750 million threshold and 1 January 2025 start | https://www.ird.gov.hk/eng/tax/bus_beps.htm | 2026-11-14 |
| IRD penalty policy. Read for ss. 80, 82 and 82A penalties | https://www.ird.gov.hk/eng/pol/ppo.htm | 2026-11-14 |
| GovHK, consequence of not paying tax on time. Read for the 5% surcharge | https://www.gov.hk/en/residents/taxes/taxfiling/consequences/consequencenotpaytax.htm | 2026-11-14 |

Not yet confirmed: the 2026/27 block extension dates (letter not yet issued); the further 10% surcharge after six months; the royalty deemed profit percentages under s. 21A (30% and 100%) and the effective rates 4.95%, 2.475%, 16.5% and 8.25% (Cap. 112 text on elegislation.gov.hk did not load as text); any 2026/27 one-off profits tax reduction (none announced in the 2026-27 Budget for 2026/27).
