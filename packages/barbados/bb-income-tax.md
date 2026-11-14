---
name: bb-income-tax
description: >
  Barbados personal income tax for income year 2026, for employees, pensioners
  and the self-employed. Covers the BBD 25,000 personal allowance (the 2026 band
  rates in BRA's policy note are held as not yet confirmed until the amending
  Act is found), who must file, the 30 April return in TAMIS, self-employed
  prepayments of 25% in June, September and December, PAYE, the reverse tax
  credit, NIS for the self-employed (17% to the BBD 64,320 ceiling plus 0.25%
  Resilience and Regeneration Fund) and withholding at 15% for non-treaty
  non-residents. Trigger on Barbados income tax, BRA, TAMIS, PIT Barbados,
  self-employed Barbados, personal allowance Barbados. Built from BRA and NIS
  pages; not reviewed by an accountant.
version: 1.0
jurisdiction: BB
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Barbados Personal Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals liable to Barbados income tax under the Income Tax Act, Cap. 73, for **income year 2026** (calendar year), administered by the Barbados Revenue Authority (BRA) through TAMIS. Amounts are BBD. Income tax is levied on persons resident or non-resident in Barbados; there is no tax on capital, and the system is self-assessment.

- **In:** employees, pensioners, self-employed persons, mixed income.
- **Out:** companies (use `bb-corporate-income-tax`), employer PAYE and NIS mechanics (use `bb-payroll-social`), VAT (use `barbados-vat`), treaty claims and expatriate structures (refer).

### Refusals

- **R-BB-1, residency unknown:** stop; residence decides scope and allowances.
- **R-BB-2, non-resident or treaty claim:** refer.
- **R-BB-3, company or partnership return:** out of scope.
- **R-BB-4, transaction labelled a capital gain that may be trading income:** refer.
- **R-BB-5, arrears or BRA enforcement:** refer.
- **R-BB-6, VAT:** use `barbados-vat`.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Personal allowance used in PAYE codes | BBD 25,000 | Each employed person starts with BBD 25,000 (code 250W or 250M) | BRA, guide to PAYE: https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE |
| PAYE starting point | Wage or salary over BBD 481 a week or BBD 2,083 a month | Employees | BRA, guide to PAYE: https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE |
| Who must file | Employees with annual income above BBD 25,000; contributory pensioners with income above BBD 75,000 (from income year 2025) | Return due 30 April of the following year in TAMIS | BRA, personal income tax: https://bra.gov.bb/Popular-Topics/Employed-Retired-Persons/PIT |
| Self-employed prepayments | 25% of the prior year's tax in each of June, September and December | Based on the prior-year return; balance with the return | BRA, self-employment: https://bra.gov.bb/Popular-Topics/Self-Employment/ |
| Reverse tax credit eligibility | Income of BBD 25,000 or less a year and not more than BBD 2,083.33 a month; worked at least four months earning at least BBD 1,000 a month or BBD 250 a week | Employed residents | BRA, reverse tax credit: https://bra.gov.bb/Credits-Rebates/Reverse-Tax-Credit |
| NIS, self-employed | 17.00% of insurable earnings (13.50 NI, 2.00 non-contributory, 0.50 training levy, 1.00 health service) | Plus 0.25% Resilience and Regeneration Fund on gross earnings from 1 April 2025 | NIS, contribution rates and earnings ceilings: https://www.nis.gov.bb/contribution-rates/ |
| NIS insurable earnings ceiling 2026 | BBD 5,360 a month (BBD 64,320 a year, computed: 12 x 5,360); BBD 1,238 a week from 5 January 2026 | Contribution rates unchanged | NIS, increase in earnings ceiling 2026: https://www.nis.gov.bb/increase-in-earnings-ceiling-2026/ |
| Withholding, non-treaty non-residents | 15% | Treaty ranges: dividends 0 to 15%, interest 5 to 15%, royalties 5 to 15%, management fees 0 to 15% | BRA, withholding tax: https://bra.gov.bb/Popular-Topics/Companies/Withholding-Tax |

### Formula

```
taxable income = assessable income - personal allowance and other allowances and deductions
tax = band rates applied to taxable income (2026 band rates: see Not yet confirmed)
self-employed NIS = 17% x min(insurable earnings, 64,320) + 0.25% x gross earnings
```

## The base

- **Assessable income** includes employment income (salary, wages, bonuses, commissions, taxable allowances) and self-employment income (gross receipts less allowable deductions).
- **Basic salary for PAYE** is total remuneration less taxable allowances and benefits (BRA example: BBD 7,500 less travel BBD 500, entertainment BBD 700 and bonus BBD 1,000 = BBD 5,300).
- **Wholly and exclusively**: business expenses must be incurred in producing the income; mixed-use costs are apportioned; capital items are not expensed.
- **Not deductible**: fines, income tax itself, private expenses.
- **Credits**: the reverse tax credit for low-income employees (self-employed not eligible); other tax credits on the BRA tax credits page.
- **Earlier version's rules kept for review**: residential rental income at 15% on gross receipts, 15% final withholding on local interest above BBD 100 and on local dividends, 50% exemption of royalties, the pensioner allowance of BBD 40,000, spouse allowance BBD 3,000, deduction caps (trade union BBD 240, medical exam BBD 750, renewable energy 150% to BBD 10,000, employer shares, donations up to 10%), and the 182-day residence test: see Not yet confirmed.

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown residency | Stop |
| Unknown allowances | BBD 25,000 only |
| Unknown business-use share | 0% deduction |
| Unknown expense category | Not deductible |

### Bank statement patterns (kept)

| Pattern | Treatment |
|---|---|
| Client transfers, INVOICE, FEES, STRIPE, PAYPAL, WISE payouts | Business income (net of VAT if registered) |
| SALARY, WAGES | Employment income, PAYE deducted |
| RENT RECEIVED | Rental income (see Not yet confirmed) |
| OFFICE RENT, ACCOUNTANT, LEGAL, MARKETING, SOFTWARE SUBSCRIPTIONS, BANK CHARGES | Deductible if business |
| BARBADOS LIGHT AND POWER, BWA, FLOW, DIGICEL | Business share only |
| RESTAURANT, GROCERIES, PERSONAL, FINES, BRA TAX PAYMENT, DRAWINGS | Not deductible |
| LAPTOP, VEHICLE, EQUIPMENT | Capital; wear and tear allowance |
| NIS PAYMENT | Not a business expense of a self-employed person for PIT (see Not yet confirmed) |
| OWN TRANSFER | Exclude |

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | TIN (13 digits) through TAMIS | Before income starts |
| 2 | Employees: employer applies the PAYE code | Each pay |
| 3 | Self-employed: prepay 25% of prior-year tax | June, September, December |
| 4 | Employer uploads filing information to TAMIS; individual files the PIT return in TAMIS | By 30 April 2027 for 2026 |
| 5 | Pay any balance | With the return |

## Penalties and interest

Penalties for late filing and late payment were not confirmed on a BRA page read for this version; see Not yet confirmed.

## Cross-border points

- Non-treaty non-residents bear 15% withholding; treaties give 0 to 15% (BRA withholding page).
- Residence, domicile and remittance rules: see Not yet confirmed.

## Two worked examples that recompute

### Example 1: Employee on BBD 60,000 and BBD 100,000 in 2026, taxable income

At BBD 60,000, taxable income after the BBD 25,000 allowance is BBD 35,000, all in the lower band. At BBD 100,000, taxable income is BBD 75,000: BBD 50,000 in the lower band and BBD 25,000 in the upper band. The tax on each band waits for the 2026 band rates (see Not yet confirmed).

```oa-check
name: BB 2026 employee taxable income and band split at 60k and 100k
inputs:
  pay_a: 60000
  pay_b: 100000
  allowance: 25000
steps:
  - taxable_a: pay_a - allowance
  - taxable_b: pay_b - allowance
  - lower_band_b: min(taxable_b, 50000)
  - upper_band_b: max(taxable_b - 50000, 0)
expected:
  taxable_a: 35000
  taxable_b: 75000
  lower_band_b: 50000
  upper_band_b: 25000
```

### Example 2: Self-employed, profit BBD 80,000: is NIS capped?

Insurable earnings are capped at BBD 64,320, so NIS is 17% x BBD 64,320 = BBD 10,934.40, plus 0.25% Resilience and Regeneration Fund on the full BBD 80,000 = BBD 200. Taxable income for income tax is BBD 55,000; the tax on it waits for the 2026 band rates (see Not yet confirmed).

```oa-check
name: BB 2026 self-employed NIS cap and income tax
inputs:
  profit: 80000
  ceiling: 64320
  allowance: 25000
steps:
  - nis: min(profit, ceiling) * 0.17
  - rrf: profit * 0.0025
  - taxable: profit - allowance
expected:
  nis: 10934.40
  rrf: 200
  taxable: 55000
```

## Ask the client first

1. Resident and domiciled in Barbados in 2026?
2. Employed, self-employed, pensioner, or a mix? Total income?
3. Allowances and deductions claimed beyond the BBD 25,000 basic allowance?
4. Prior-year tax (prepayments) and PAYE deducted?
5. Rental, interest, dividend or royalty income, and any withholding suffered?
6. Income at or below BBD 25,000 (reverse tax credit)?

## Sources

| Source | URL | Read on |
|---|---|---|
| BRA, Policy Note OGC No. 001/2026: read in full for the 2026 rates BRA says it applies and its worked examples (an administrative note, not an enactment) | https://bra.gov.bb/attachment?file=Attachments%2FPolicy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026.pdf&name=Policy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026 | 2026-11-14 |
| BRA, Income Tax Act legislation page: read for the list of amending Acts (latest 2025-30; no 2026 amending Act listed) | https://bra.gov.bb/About/Legislation-Regulations/Income-Tax-Act | 2026-11-14 |
| Parliament of Barbados, bills and resolutions list: read for 2026 bills (no Income Tax (Amendment) Bill or Act, 2026 listed) | https://www.barbadosparliament.com/bills/ | 2026-11-14 |
| Provisional Collection of Taxes Act, Cap. 85: read for s. 3 (provisional effect of a new tax or rate increase in budget proposals) | https://bra.gov.bb/attachment?file=Attachments%2fProvisional+Collection+of+Taxes+Act%2c+Cap.+85.pdf&name=Provisional+Collection+of+Taxes+Act%2c+Cap.+85 | 2026-11-14 |
| BRA, personal income tax page: read for who must file and the 30 April date | https://bra.gov.bb/Popular-Topics/Employed-Retired-Persons/PIT | 2026-11-14 |
| BRA, guide to PAYE: read for the PAYE threshold, BBD 25,000 basic allowance, tax codes and the 15th remittance date | https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE | 2026-11-14 |
| BRA, self-employment page: read for the 25% prepayments | https://bra.gov.bb/Popular-Topics/Self-Employment/ | 2026-11-14 |
| BRA, reverse tax credit: read for eligibility | https://bra.gov.bb/Credits-Rebates/Reverse-Tax-Credit | 2026-11-14 |
| BRA, withholding tax: read for 15% non-treaty and treaty ranges | https://bra.gov.bb/Popular-Topics/Companies/Withholding-Tax | 2026-11-14 |
| NIS, contribution rates and earnings ceilings (via Firecrawl; the site blocks scripts): read for the self-employed and private sector tables, the Resilience and Regeneration Fund and the ceiling history | https://www.nis.gov.bb/contribution-rates/ | 2026-11-14 |
| NIS, increase in earnings ceiling 2026 (via Firecrawl): read in full | https://www.nis.gov.bb/increase-in-earnings-ceiling-2026/ | 2026-11-14 |

Not yet confirmed: the pensioner allowance of BBD 40,000 and spouse allowance of BBD 3,000; the 182-day residence test and the treatment of resident non-domiciled persons; 15% flat tax on residential rental income; 15% final withholding on local interest over BBD 100 and local dividends; the 50% royalty exemption; the deduction caps listed under The base; late filing (earlier version: BBD 500 plus 5%), late payment (5%) and 1% a month interest; the salaried 50% / 50% payment schedule (30 April, 30 September); the earlier version's non-resident withholding rates of nil on interest and royalties from 1 April 2019 and 25% on dividends from untaxed profits; whether self-employed NIS is deductible; stamp duty rates; the 2026 personal income tax rates: BRA's Policy Note OGC No. 001/2026 says BRA applies 11.5% (taxable income to BBD 50,000) and 27.5% (above) from income year 2026, down from 12.5% and 28.5%, following the 16 March 2026 budget, but no Income Tax (Amendment) Act, 2026 appears on BRA's Income Tax Act legislation page or on Parliament's bills list (both read 14 Nov 2026), and the Provisional Collection of Taxes Act, Cap. 85, s. 3 gives provisional effect only to a new tax or a rate increase, not a cut; the earlier 12.5% and 28.5% rates were not found in an enactment read for this version either, so confirm the rates with BRA before computing or filing.
