---
name: sri-lanka-corporate-tax
description: "ALWAYS read this skill before touching any Sri Lanka corporate income tax work for a resident company, year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like Sri Lanka corporate tax, Sri Lanka CIT, company tax Sri Lanka, 30% corporate rate Sri Lanka, betting and gaming tax Sri Lanka, liquor tobacco tax Sri Lanka, Inland Revenue Act 24 of 2017 company, or year of assessment 2026/27 company. Covers the Inland Revenue Act No. 24 of 2017 as amended up to Act No. 11 of 2026, the 30% standard rate, the 15% rate on qualifying foreign-currency income remitted through a bank, the 45% rate on betting and gaming and on domestic liquor and tobacco, the 30% rate on investment-asset gains, the 14% remittance tax, instalments, return dates and penalties. Out of scope are personal income tax, withholding, SSCL, VAT, banking and insurance regimes, groups and transfer pricing."
version: "2.1"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27), 1 April 2026 to 31 March 2027"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Sri Lanka Corporate Income Tax, year of assessment 2026/27, v2.1

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
- **Company rates for 2026/27:** First Schedule paragraph 4(2C)(d) has excluded liquor and tobacco exports from the higher rate since 1 April 2025. Act No. 11 of 2026 section 36(4) inserted the export exclusion into the earlier paragraph 4(2B)(b), with effect from 1 April 2022 under section 1(3).

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
| Remittance tax on a non-resident person with a Sri Lankan permanent establishment | 14% of gross remitted profits | Section 62 and First Schedule paragraph 9. Pay by the 30th day after remitting. The 0% rate applies to remittances of qualifying retained and reinvested income. | same |
| Late filing penalty | Greater of 5% of tax owing plus 1% per month or part month, or Rs. 50,000 plus Rs. 10,000 per month or part month, capped at Rs. 400,000 per return | Section 178 | same |
| Late payment penalty | 20% of unpaid tax, or 10% of an unpaid instalment | Section 179. The penalty applies after 14 days from the due date. For the 20% penalty, a later due date in an assessment notice or a payment extension under section 151 takes precedence where applicable. | same |
| Late payment interest | one and one-half per cent per month or part month | Sections 157 and 159(1) | same |
| Underpayment from a negligent or intentional incorrect statement or material omission in the return | 25% of the underpayment, or 75% if it exceeds Rs. 10,000,000 or 25% of the tax liability for the period | Section 180 | same |
| Failure to register | Up to Rs. 50,000 | Section 177 of the consolidated Act. Companies incorporated or registered in Sri Lanka must apply for tax registration within 30 days of incorporation or registration under section 102(1A). | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |

### Steps

1. Compute taxable income under the IRA from the accounts (business income, investment income, deductions, capital allowances and losses: detail not set out here, see Not yet confirmed).
2. Split out each applicable special-rate stream. Verify the source or overseas use and bank remittance for the 15% streams. Apply 45% to betting and gaming and to qualifying domestic liquor and tobacco profits. Apply 30% to taxable investment-asset gains after checking exemptions.
3. Tax the remainder at 30%.
4. Deduct instalments paid (`sri-lanka-provisional-tax-ait`) and eligible withholding credits (`sri-lanka-withholding-tax`). Pay the ordinary balance by 30 September 2027 under section 82(2)(c)(ii). File the annual return by 30 November 2027 under section 93(1).
5. For a non-resident company with a branch, add remittance tax at 14% where it applies.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Sector or rate unclear | Confirm the activity and any special rate before finalising |
| 15% concession claimed | Verify foreign source or overseas use, payment in foreign currency and bank remittance to Sri Lanka |
| Betting, gaming, liquor or tobacco activity | Apply 45% unless the income is from export of liquor or tobacco (then the normal rate) |
| SME or sector concession asserted | Do not apply: the 14% SME and sector rates in paragraph 4(2) and (2A) ended for periods after 30 September 2022, and none is confirmed for 2026/27 |
| Asset is business or investment asset | Confirm the classification and exemptions. A business asset gain enters the business computation under section 6(2)(c). A taxable investment asset gain is generally taxed separately at 30%. Gains on quoted Colombo Stock Exchange shares are exempt under Third Schedule paragraph (h). Section 37(3) prevents double counting where a gain is included in business income. |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Export of liquor or tobacco products | Ordinary taxable export profits use the 30% rate. Paragraph 4(2C)(d) excludes exports from 45% from 1 April 2025. The 2026 amendment added the export exclusion to the earlier 40% provision. |
| IT services exporter paid in foreign currency but funds kept abroad | Not remitted through a bank: 30% |
| Taxable investment-asset gain | 30%, separate from the business stream and excluded from instalments. File the gain return and pay within 30 days after the end of the month of realisation under sections 82(2)(c)(i) and 93(2). |
| 0% remittance tax on retained income | Retain the year's total income in Sri Lanka for at least three years from the first day of the following year of assessment and invest it in business expansion, eligible Colombo Stock Exchange securities, Treasury bills, Treasury bonds or Sri Lanka International Sovereign Bonds. |
| Remitted profits | Section 62(3) includes relevant Sri Lankan taxable profits retained abroad and excludes dividends paid by a resident company. |
| Historic 24% or 28% rates | Do not use for 2026/27; 30% since 1 April 2023 |
| Old 40% rate for betting, gaming, liquor and tobacco | Applied before 1 April 2025 only |
| BOI agreement company | Refer: agreement terms may give other rates |
| Banking, insurance, unit trusts, NGOs, charities | Other paragraphs of the First Schedule; refer |

## Worked cases

### Case 1: standard company with a foreign-currency services stream

Taxable income Rs. 50,000,000, of which Rs. 10,000,000 is from IT services used outside Sri Lanka, paid in US dollars and remitted through a bank to Sri Lanka. Tax is 30% of Rs. 40,000,000 plus 15% of Rs. 10,000,000.

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

A liquor manufacturer has Rs. 50,000,000 of taxable profit and can sell domestically or export the same output. Domestic sale is taxed at 45% and export at the 30% standard rate. The company also sold unquoted shares held as investment assets at a taxable gain of Rs. 5,000,000, taxed at 30%. Export saves Rs. 7,500,000 of income tax on the same profit.

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
| Quarterly instalments | 15 August 2026, 15 November 2026, 15 February 2027 and 15 May 2027 under section 90(2). Use prior-year tax unless section 90(3) requires a current-year estimate. See `sri-lanka-provisional-tax-ait`. |
| Statement of estimated tax | Section 91 applies to years beginning before 1 April 2026. For 2026/27, check the separate IRD instalment declaration requirements. |
| Return of income | Eight months after the year end, so by 30 November 2027 (section 93(1)), through IRD e-Services |
| Balance of tax | Pay ordinary income tax by 30 September 2027, six months after year end. Late payment can incur the section 179 penalty and interest from the due date at 1.5% per month or part month. |
| TIN | Section 103(6) has effect from 1 April 2026. The IRD certificate procedure for the persons specified in section 102(3) started on 1 November 2026. Both parties must produce a certificate when transferring shares of a company incorporated in Sri Lanka. See the IRD circular for covered financial accounts and other transactions. |

## Completion checklist

- [ ] Each income stream mapped to its rate
- [ ] 15% claimed only after checking foreign source or overseas use, foreign currency and qualifying bank remittance
- [ ] Liquor or tobacco export kept out of the 45% rate
- [ ] Investment-asset gains checked for exemptions and taxable gains at 30% kept out of instalments
- [ ] Instalment and withholding credits deducted
- [ ] Payment and return due dates and penalties noted

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for First Schedule paragraphs 4 and 9, Third Schedule paragraph (h), and sections 6, 37, 62, 82, 90 to 93, 157, 159 and 177 to 180 in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-24 |
| Read for sections 1(3), 23 (new section 102(1A)), 24 (section 103(6)) and 36(4) (liquor and tobacco export wording) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |
| Read for the company rates table and the remittance tax rows of the IRD tax chart (the latest chart on the site) | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for the amending Acts and the final payment and annual filing deadlines | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Income%20Tax.aspx?menuid=1201 | 2026-11-24 |
| IRD instalment calculation and declaration circular SEC/2026/E/06 (Re-Revised) | https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2026_E_06_ReRiv_E.pdf | 2026-11-24 |
| IRD TIN certificate circular SEC/2026/E/07 | https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2026_E_07_E.pdf | 2026-11-24 |

The linked IRD tax chart is for 2025/26. The company rates for 2026/27 follow the Act. Loss carry-forward, capital allowances and any company-specific concessions need a separate check.
