---
name: sri-lanka-corporate-tax
description: "ALWAYS read this skill before touching any Sri Lanka corporate income tax work for a resident company, year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like Sri Lanka corporate tax, Sri Lanka CIT, company tax Sri Lanka, 30% corporate rate Sri Lanka, betting and gaming tax Sri Lanka, liquor tobacco tax Sri Lanka, Inland Revenue Act 24 of 2017 company, or year of assessment 2026/27 company. Covers the Inland Revenue Act No. 24 of 2017 as amended up to Act No. 11 of 2026, the 30% standard rate, the 15% rate on qualifying foreign-currency income remitted through a bank, the 45% rate on betting and gaming and on domestic liquor and tobacco, the 30% rate on investment-asset gains, the 14% remittance tax, instalments, return dates and penalties. Out of scope are personal income tax, withholding, SSCL, VAT, banking and insurance regimes, groups and transfer pricing."
version: "2.0"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27), 1 April 2026 to 31 March 2027"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Sri Lanka Corporate Income Tax, year of assessment 2026/27, v2.0

Built from the law: not yet approved by an accountant. Produced by OpenAccountants (openaccountants.com). Not tax advice.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country | Sri Lanka |
| Tax | Corporate income tax, charged under section 2(1)(a) and the First Schedule paragraph 4 of the Inland Revenue Act No. 24 of 2017 (IRA) |
| Currency | LKR |
| Year of assessment | 1 April 2026 to 31 March 2027 (YA 2026/27) |
| Law | IRA as amended by Acts No. 10 of 2021, 45 of 2022, 4 and 14 of 2023, 2 of 2025 and 11 of 2026 |
| Authority | Inland Revenue Department (IRD) |

- **In:** resident companies computing taxable income and tax for the year; the special-rate lines below.
- **Out:** personal tax (`sri-lanka-income-tax`), withholding (`sri-lanka-withholding-tax`), instalments in detail (`sri-lanka-provisional-tax-ait`), SSCL (`sri-lanka-sscl`), VAT (`sri-lanka-vat`), banking, insurance and other sector regimes, group taxation, transfer pricing, reorganisations.
- **No change to the company rates for 2026/27:** Act No. 11 of 2026 did not amend paragraph 4 rates. Its item (4) confirmed, from 1 April 2022, that the liquor and tobacco higher rate does not reach exports.

## Ask the client first

1. Sector: ordinary trading, betting and gaming, liquor or tobacco (domestic or export)?
2. Any services income used outside Sri Lanka, or foreign-source income, earned in foreign currency and remitted through a bank to Sri Lanka? Evidence of the bank remittance?
3. Any gains from the realisation of investment assets in the year?
4. Draft or audited accounts, prior-year return and the taxable income computation.
5. Instalments paid and withholding (AIT/WHT) credits for the year.
6. Is it a non-resident company with a Sri Lanka branch (remittance tax)?

## The method, step by step

### Rates, bands and thresholds

| Income of a company | Rate | Conditions | Source |
| --- | --- | --- | --- |
| Standard rate on taxable income | 30% | From 1 April 2023; paragraph 4(1)(d) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Services rendered for use outside Sri Lanka, paid in foreign currency and remitted through a bank | 15% | From 1 April 2025; paragraph 4(2C)(a) | same |
| Foreign-source gains and profits earned in foreign currency and remitted through a bank | 15% | From 1 April 2025; paragraph 4(2C)(b) | same |
| Betting and gaming | 45% | From 1 April 2025 (40% before); paragraph 4(2C) | same |
| Manufacture and sale or import and sale of liquor or tobacco, other than export | 45% | From 1 April 2025; export of such products is not at 45% | same |
| Gains from the realisation of investment assets | 30% | From 1 October 2022; paragraph 4(4) | same |
| Remittance tax on a non-resident person | 14% | Tax chart, remittance tax row; 0% on remittances of retained income invested for three years, per the chart | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Late filing penalty | Greater of 5% of tax owing plus 1% a month, or fifty thousand rupees plus ten thousand rupees a month; capped at four hundred thousand rupees | Section 178 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Late payment penalty | 20% of tax due but not paid | Not paid within 14 days of the due date; section 179(1) | same |
| Late payment interest | one and one-half per cent per month or part month | Sections 157 and 159(1) | same |
| Underpayment from negligence or intent | 25%; 75% if over Rs. 10,000,000 or over 25% of the liability | Section 180 | same |
| Failure to register | Up to fifty thousand rupees | Section 177 (in the consolidated Act: https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf); companies must register within 30 days of incorporation (new section 102(1A)) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |

### Steps

1. Compute taxable income under the IRA from the accounts (business income, investment income, deductions, capital allowances and losses: detail not set out here, see Not yet confirmed).
2. Split out each special-rate stream: 15% remitted foreign-currency income (only with bank remittance evidence), 45% betting and gaming and domestic liquor and tobacco, 30% investment-asset gains.
3. Tax the remainder at 30%.
4. Deduct instalments paid (`sri-lanka-provisional-tax-ait`) and withholding credits (`sri-lanka-withholding-tax`); the balance is payable with the return.
5. For a non-resident company with a branch, add remittance tax at 14% where it applies.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Sector or rate unclear | Apply 30% standard |
| 15% concession claimed | Apply 30% until foreign currency and bank-remittance evidence is seen |
| Betting, gaming, liquor or tobacco activity | Apply 45% unless the income is from export of liquor or tobacco (then the normal rate) |
| SME or sector concession asserted | Do not apply: the 14% SME and sector rates in paragraph 4(2) and (2A) ended for periods after 30 September 2022, and none is confirmed for 2026/27 |
| Asset is business or investment asset | Flag for the practitioner; the rate is 30% either way for a company, but the base and instalment rules differ |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Export of liquor or tobacco products | Not at 45%; taxed at the 30% standard rate (paragraph 4(2C)(d), confirmed by Act No. 11 of 2026 from 1 April 2022) |
| IT services exporter paid in foreign currency but funds kept abroad | Not remitted through a bank: 30% |
| Investment-asset gain | 30%, separate from the business stream; excluded from instalments |
| Historic 24% or 28% rates | Do not use for 2026/27; 30% since 1 April 2023 |
| Old 40% rate for betting, gaming, liquor and tobacco | Applied before 1 April 2025 only |
| BOI agreement company | Refer: agreement terms may give other rates |
| Banking, insurance, unit trusts, NGOs, charities | Other paragraphs of the First Schedule; refer |

## Worked cases

### Case 1: standard company with a foreign-currency services stream

Taxable income Rs. 50,000,000, of which Rs. 10,000,000 is IT services for overseas clients paid in US dollars and remitted through a Sri Lankan bank. Tax: 30% of 40,000,000 plus 15% of 10,000,000.

```oa-check
name: Company with remitted foreign-currency services, YA 2026/27
inputs:
  taxable_income: 50000000
  remitted_fx_services: 10000000
steps:
  - standard_part: (taxable_income - remitted_fx_services) * 0.30
  - fx_part: remitted_fx_services * 0.15
  - total_tax: standard_part + fx_part
expected:
  standard_part: 12000000
  fx_part: 1500000
  total_tax: 13500000
```

### Case 2: decision, sell liquor at home or export

A liquor manufacturer has Rs. 50,000,000 of profit and can sell domestically or export the same output. Domestic sale is taxed at 45%, export at the 30% standard rate. The company also sold shares held as investment assets at a gain of Rs. 5,000,000, taxed at 30%. Export saves Rs. 7,500,000 of income tax on the same profit.

```oa-check
name: Liquor profit, domestic against export, plus investment gain
inputs:
  profit: 50000000
  investment_gain: 5000000
steps:
  - domestic_tax: profit * 0.45
  - export_tax: profit * 0.30
  - saving_by_export: domestic_tax - export_tax
  - gain_tax: investment_gain * 0.30
  - total_if_domestic: domestic_tax + gain_tax
expected:
  domestic_tax: 22500000
  export_tax: 15000000
  saving_by_export: 7500000
  gain_tax: 1500000
  total_if_domestic: 24000000
```

## When to refuse or refer

- R-LK-CT-1: banking, insurance and sector special regimes. Out of scope; escalate.
- R-LK-CT-2: SME or concessionary sector rates. Any such rate must be verified against the current IRA and IRD guidance; this skill asserts only the rates in the table.
- R-LK-CT-3: group taxation, transfer pricing, reorganisations. Out of scope; escalate.
- R-LK-CT-4: cross-skill. Personal tax to `sri-lanka-income-tax`; WHT and AIT to `sri-lanka-withholding-tax`; instalments to `sri-lanka-provisional-tax-ait`; SSCL to `sri-lanka-sscl`; VAT to `sri-lanka-vat`; betting and gaming levy to `sri-lanka-betting-gaming-excise`.
- Never file or instruct filing; produce a working paper for practitioner review.

## Filing and payment

| Item | Detail |
| --- | --- |
| Year of assessment | 1 April 2026 to 31 March 2027 |
| Quarterly instalments | 15 August 2026, 15 November 2026, 15 February 2027, 15 May 2027 (section 90(2)); from 2026/27 based on the prior year's tax (`sri-lanka-provisional-tax-ait`) |
| Statement of estimated tax | Section 91 now applies only to years before 1 April 2026 (Act No. 11 of 2026) |
| Return of income | Eight months after the year end, so by 30 November 2027 (section 93(1)), through IRD e-Services |
| Balance of tax | Paid with the return; late payment penalty 20% after 14 days and interest at 1.5% a month |
| TIN | New section 103(6): a TIN certificate is needed for share transfers, bank accounts and other listed purposes from 1 April 2026 |

## Completion checklist

- [ ] Each income stream mapped to its rate
- [ ] 15% claimed only with bank-remittance evidence
- [ ] Liquor or tobacco export kept out of the 45% rate
- [ ] Investment-asset gains at 30% and out of instalments
- [ ] Instalment and withholding credits deducted
- [ ] Return due date and penalties noted

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for First Schedule paragraph 4 (rates for companies, subparagraphs (1), (2), (2A), (2B), (2C), (4)), sections 90 to 93, 157, 159, 177 to 180, in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-14 |
| Read for sections 1(3), 23 (new section 102(1A)), 24 (section 103(6)) and 36(4) (liquor and tobacco export wording) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |
| Read for the company rates table and the remittance tax rows of the IRD tax chart (the latest chart on the site) | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for the list of amending Acts on the IRD income tax page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Income%20Tax.aspx?menuid=1201 | 2026-11-14 |

Not yet confirmed: the IRD has not published a 2026/27 tax chart (the latest page is headed for the prior year; the company rates in the Act are unchanged); loss carry-forward and capital allowance detail (Second and Fourth Schedules not read for this rewrite); the remittance tax conditions in the Act (only the chart was read); any SME or sector rate for 2026/27.
