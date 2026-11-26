---
name: hk-corporate-income-tax
description: "Use this skill for Hong Kong profits tax on corporations and unincorporated businesses for the year of assessment 2026/27 (1 April 2026 to 31 March 2027), the year that contains most of 2026. It covers the territorial source rule, the two-tiered rates (8.25% and 16.5% for corporations, 7.5% and 15% for unincorporated businesses, split at HKD 2,000,000), the connected-entity nomination rule, the FSIE regime, the 15% global minimum tax and HKMTT for large groups, provisional tax, filing under the block extension scheme and penalties. Built from the law, not reviewed by an accountant."
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (1 April 2026 to 31 March 2027). Filing dates shown apply to the 2025/26 return cycle and include the July and October 2026 IRD extensions. The 2026/27 cycle is listed under Not yet confirmed."
version: "2.1"
last_updated: 2026-11-26
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
| Connected entities | One entity only takes the two-tiered rates | Test connections at the end of the basis period. The elected entity gets the lower band for that year. Normal rates of 16.5% or 15% apply to the other entities’ ordinary assessable profits | https://www.ird.gov.hk/eng/faq/2tr.htm |
| One-off reduction, YA 2025/26 final tax | 100%, capped at HKD 3,000 per business | Not for provisional tax; enacted, gazetted 22 May 2026 | https://www.ird.gov.hk/eng/tax/budget.htm |
| Renovation of business premises | Deducted over 5 years in equal instalments | Qualifying capital expenditure, from the year it is incurred. Domestic buildings are excluded under s. 16F, with hotels and guesthouses outside the domestic-building definition | https://www.ird.gov.hk/eng/pdf/dipn05.pdf |
| Plant and machinery annual allowance | 10%, 20% or 30% on reducing value | Rates set by the Board of Inland Revenue. Check the 60% initial allowance and any full-deduction rule for the asset | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf#page=12 |
| Global minimum tax (IIR) and HKMTT | 15% | MNE groups with consolidated revenue of EUR 750 million or more in at least two of the four preceding fiscal years; fiscal years beginning on or after 1 January 2025 | https://www.ird.gov.hk/eng/tax/bus_beps.htm |
| Profits tax return, accounting date code "N" (1 April to 30 November 2025) | No ordinary block extension | 2025/26 profits tax returns, represented taxpayers. Check the separate e-filing extension | https://www.ird.gov.hk/eng/pdf/bel26e.pdf |
| Code "D" (1 to 31 December 2025) | 31 August 2026 (paper), 2 October 2026 (electronic) | 2025/26 returns under the block extension scheme. Electronic deadline requires the applicable e-filing extension | https://www.ird.gov.hk/eng/pdf/bel26ea.pdf |
| Code "M" (1 January to 31 March 2026) | 30 November 2026 (paper), 30 December 2026 (electronic) | Same conditions as code "D". Qualifying loss returns may be extended to 1 February 2027 on request under the March letter | https://www.ird.gov.hk/eng/pdf/bel26eb.pdf |
| Surcharge on unpaid tax | 5% initially, then a possible further 10% | The second surcharge applies to the amount still in default 6 months after the due date, including the unpaid initial surcharge | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf#page=37 |
| Additional tax (s. 82A) | Up to treble the tax undercharged | In lieu of prosecution, for incorrect returns and failures | https://www.ird.gov.hk/eng/pol/ppo.htm |
| Prosecution for failure to file or incorrect return (s. 80(2)) | Fine of HKD 10,000 plus treble the tax undercharged | Without reasonable excuse. Wilful evasion (s. 82) carries HKD 50,000, treble the tax and up to 3 years’ imprisonment | same |

## The base

1. **Start from the accounts profit** for the basis period, generally the accounting year ending between 1 April 2026 and 31 March 2027 for YA 2026/27. Check special basis period rules on commencement, cessation or a change of accounting date.
2. **Identify offshore profits and gains on capital assets.** These generally fall outside the s. 14 charge. Before excluding an amount, apply the deeming provisions and the FSIE rules below. Hong Kong does not withhold tax on ordinary dividend or interest payments.
3. **Include deemed Hong Kong receipts once.** Section 15 covers specified film, tape and recording payments for Hong Kong use. Specified IP royalties for Hong Kong use are also covered, as are those for use outside Hong Kong if the payer deducts the amount in computing Hong Kong assessable profits.
4. **Apply the FSIE regime** (from 1 January 2023): for a member of a multinational enterprise group carrying on business in Hong Kong, specified foreign-sourced interest, dividends, IP income and disposal gains (disposal gains other than equity from 1 January 2024) are chargeable when received in Hong Kong, unless the entity meets the exception for that income type.
5. **Deduct allowable expenses** incurred in producing chargeable profits (s. 16). Add back disallowed amounts already charged in the accounts, including book depreciation, and deduct the statutory capital allowances. Section 17 restricts private and capital expenses and remuneration or interest paid to a proprietor.
6. **Apply the two-tiered rates** to assessable profits, after checking the connected-entity nomination.
7. **Large groups:** determine which Hong Kong entities are liable for IIR or HKMTT and which must file the top-up tax return. Check whether group filing satisfies an entity’s obligation. The Pillar Two Portal opened top-up tax return filing on 26 October 2026.

### Payments to non-residents

For royalties chargeable through a Hong Kong payer under s. 20B, the payer retains enough to meet the tax when paying or crediting the amount. Under s. 21A the deemed profit is generally 30% of the sum. It is 100% for an associate payment unless the Commissioner is satisfied that no person carrying on a trade, profession or business in Hong Kong ever owned the IP in whole or part. A royalty taxable under s. 14 in the recipient’s own Hong Kong business follows the ordinary profits computation.

For a corporate recipient, the standard 16.5% rate produces 4.95% or 16.5% of gross royalties on the respective deemed bases. The 8.25% rate produces 2.475% or 8.25% on the portion within the recipient’s eligible HKD 2 million assessable-profit band across all payers. Check the treaty and any specific concession before calculating the liability. Where other payers may also report profits for the recipient, the IRD instructs the payer to retain tax using the standard rate.

## Deadlines and filing

- **Return issue:** the 2025/26 bulk issue was on 1 April 2026 (2 April for inactive corporation and partnership files due for review). The ordinary profits tax return period is one month. First returns for file prefixes 23 and 97 normally allow three months unless IRD specifies otherwise. A sole proprietor reports on BIR60, ordinarily due within three months from issue when the taxpayer wholly owned an unincorporated business during the year.
- **2026/27:** returns are expected to issue in April 2027 under a new block extension letter.
- **Provisional tax:** IRD generally charges it using the preceding year’s assessed profits. Credit provisional tax paid against the final tax for the same year of assessment, then against the following year’s provisional tax. Holdover applications are possible on statutory grounds.
- **E-filing for the 2025/26 cycle:** for the ordinary voluntary extension, apply at least 7 working days before the return is otherwise due and file electronically through the Business Tax Portal. The March letter provides an additional month, subject to the later code "D" and "M" dates in the table. Separate arrangements apply to mandatory e-filing. The 1 February 2027 date also applies to approved code "M" loss cases filed electronically.

## Penalties and interest

Unpaid tax: the Commissioner may add 5% to unpaid tax and take recovery action under IRO Part XII. After 6 months in default, a further 10% can apply to the amount remaining unpaid including the initial surcharge. For qualifying late or incorrect returns, s. 82A permits additional tax up to treble the tax undercharged in lieu of prosecution. See the table for the s. 80(2) and s. 82 penalties.

## Cross-border points

- Territorial source: an offshore claim needs evidence of where the profit-producing operations took place.
- FSIE: match each type of foreign-sourced income to the applicable economic substance, participation or nexus exception. Qualifying intra-group disposal gains can also get a deferral.
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

**Example 2: sole proprietorship or company with HKD 3,000,000 of ordinary assessable profits.** For the eligible sole proprietor, 7.5% × HKD 2,000,000 plus 15% × HKD 1,000,000 gives HKD 300,000. The eligible corporation pays HKD 330,000 as in example 1. The HKD 30,000 difference is in profits tax before considering personal assessment or the owner’s salaries tax position. If another connected entity elects the two-tiered rate, the company pays 16.5% × HKD 3,000,000 = HKD 495,000.

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
| IRD, July 2026 circular extending code "D" paper and electronic returns | https://www.ird.gov.hk/eng/pdf/bel26ea.pdf | 2026-11-26 |
| IRD, October 2026 circular extending code "M" paper and electronic returns | https://www.ird.gov.hk/eng/pdf/bel26eb.pdf | 2026-11-26 |
| IRD, instalments and the further surcharge after six months | https://www.ird.gov.hk/eng/faq/ins.htm | 2026-11-26 |
| IRD, practice note 22 paras 27–34 on deemed royalty profits | https://www.ird.gov.hk/eng/pdf/dipn22.pdf#page=13 | 2026-11-26 |
| IRD, pro forma profits tax calculation with depreciation allowances as deductions | https://www.ird.gov.hk/eng/pdf/ir957ae.pdf | 2026-11-26 |
| IRD, practice note 5 on refurbishment deductions | https://www.ird.gov.hk/eng/pdf/dipn05.pdf | 2026-11-26 |
| IRD, FSIE scope and income-specific exceptions | https://www.ird.gov.hk/eng/tax/bus_fsie.htm | 2026-11-26 |
| IRD, individual filing deadline when reporting sole proprietorship profit on BIR60 | https://www.ird.gov.hk/eng/tax/ind_ctr.htm | 2026-11-26 |

Not yet confirmed: the 2026/27 block extension dates and any 2026/27 one-off profits tax reduction. The IRD has published the one-off reduction for 2025/26.
