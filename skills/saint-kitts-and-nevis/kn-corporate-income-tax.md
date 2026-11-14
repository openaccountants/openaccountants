---
name: kn-corporate-income-tax
description: >
  Saint Kitts and Nevis corporation tax for 2026 under the Income Tax Act, Cap. 20.22.
  Covers who is charged (companies only; resident companies on worldwide income and
  non-resident companies on income of a local permanent establishment, s.3A from Act 12
  of 2021), the rate conflict (33% in s.32(1)(b) and the IRD instalment FAQ against the
  25% from 1 January 2024 announced in the 2024 budget), the return 3.5 months after
  year end (15 April 2026 for a 31 December 2025 year end), quarterly instalments on
  the 15th of March, June, September and December, the 25% understatement penalty, and
  the CIT-101 information return for international companies and Nevis entities.
  Trigger phrases include St Kitts corporate tax, Nevis company tax rate, CIT-100,
  CIT-101, St Kitts income tax return.
version: 1.0
jurisdiction: KN
tax_year: 2026
tax_year_notes: "2026 filings (returns for 2025 year ends) and 2026 instalments. The rate to apply is unresolved between 33% (Act, 2017 revision) and 25% (announced from 1 January 2024)."
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis corporation tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Federal corporation tax in 2026 under the Income Tax Act, Cap. 20.22 (2017 revision) and later amendments, administered by the Inland Revenue Department. Individuals have no ordinary income tax (s.3(3)) and unincorporated businesses pay the 4% business tax: [kn-unincorporated-business-tax](kn-unincorporated-business-tax.md). Withholding on payments to non-residents: [kn-nonresident-withholding](kn-nonresident-withholding.md). Concessions and Nevis entity rules: [kn-special-regimes](kn-special-regimes.md). Amounts are EC$.

## Ask the client first

1. Is the company resident (incorporated or managed in the Federation) or a non-resident company with a permanent establishment here?
2. Its year end, and the chargeable income for the year.
3. Is it an international company, a Nevis business corporation or a Nevis LLC (CIT-101 information return)?
4. Does it hold an approval or tax holiday (it must still file)?
5. Instalments paid so far for the year.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Rate in the Act, s.32(1)(b) | Corporation tax of 33% on income earned in 2013 (assessed 2014) and later years | [Income Tax Act, Cap. 20.22, s.32](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| Rate in IRD instalment guidance | Instalments are one quarter of the tax estimated at 33% on chargeable income | [IRD FAQs](https://www.sknird.com/faqs/) |
| Rate announced in the 2024 budget | 25% for registered corporations from January 2024 (amending instrument not found) | [SKNIS, 13 December 2023](https://www.sknis.gov.kn/2023/12/13/corporate-income-tax-rate-in-st-kitts-and-nevis-set-at-25-from-january-2024/) |
| Return | 3.5 months after year end: by 15 April for a 31 December year end; filed even if inactive or on a tax holiday | [IRD corporate income tax page](https://www.sknird.com/corporate-income-tax/) |
| Instalments | On the 15th of March, June, September and December (Amendment Act No. 6 of 2006, s.44(6)) | same |
| Understatement penalty | 25% of the underpayment from an incorrect statement or material omission | [IRD FAQs](https://www.sknird.com/faqs/) |

### The base

- **Only companies are charged.** For income accruing on or after 1 May 1980, s.3(3) takes persons other than companies out of the s.3 charge; the old personal rates and allowances in the Act are read with that exclusion.
- **Residence (s.3A, inserted by Act 12 of 2021, published 26 March 2021).** A resident company is assessed on income wherever it arises; a non-resident company carrying on business through a local permanent establishment on income attributable to it. Apply the Act's establishment tests and exceptions; verify residence, deductions, loss relief and any special regime.
- **Dividends.** A company may not deduct tax at the corporation rate from dividends (s.32(2)).
- **Pandemic reduction.** A 2021 IRD advisory set a conditional reduction for April 2020 to June 2021; historical only.

### Steps

1. **Chargeable income** for the year, under the Act's deduction rules.
2. **Rate:** decide 33% or 25% (see the boundary table) and record why.
3. **Instalments:** a quarter of the estimated tax on each 15 March, June, September and December.
4. **Return** (CIT-100) 3.5 months after year end, with payment of the balance, through SMARTS.
5. **CIT-101** information return where the company is an international company, a Nevis business corporation or LLC.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| 33% or 25%? | The Act (2017 revision) and IRD's instalment FAQ print 33%; the 2024 budget announced 25% for registered corporations from 1 January 2024 and the government describes it as in place. The amending instrument, its period, coverage and conditions were not found. Ask IRD in writing and file on the rate it confirms | [Cap. 20.22, s.32](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf); [IRD FAQs](https://www.sknird.com/faqs/); [SKNIS](https://www.sknis.gov.kn/2023/12/13/corporate-income-tax-rate-in-st-kitts-and-nevis-set-at-25-from-january-2024/) |
| 31 December 2025 year end | IRD confirmed filing and payment by 15 April 2026 | [IRD notices](https://www.sknird.com/announcements-upcoming-events/) |
| International company, Nevis IBC or LLC | CIT-101 information return (September 2023 instructions); the entity stays responsible even when an agent files; taxable entities also file CIT-100 | [CIT-101 guidelines, September 2023](https://eservicesskn.sknird.com/ServiceProvider/Documents/CIT-101%20Guidelines%20Revised%20September%202023.pdf) |
| Non-resident filer | IRD's filing page uses wider language than s.3A; confirm the return obligation for a non-company | [IRD corporate income tax page](https://www.sknird.com/corporate-income-tax/) |
| Payments to residents of rent, royalties and some interest | s.37 retained in the 2017 revision; confirm its current application and interaction with s.3(3) | [Cap. 20.22, ss.36 and 37](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf) |
| Disagreeing with an assessment | Follow s.61 objection procedure | [IRD corporate income tax page](https://www.sknird.com/corporate-income-tax/) |

## Worked cases

### Case 1: quarterly instalments at the IRD rate

Estimated chargeable income EC$400,000 at 33%: tax 132,000, so 33,000 on each instalment date.

```oa-check
name: St Kitts corporation tax instalments on 400,000 at 33%
inputs:
  income: 400000
steps:
  - tax: income * 0.33
  - instalment: tax / 4
expected:
  tax: 132000
  instalment: 33000
```

### Case 2 (decision): file at 33% or 25%?

Chargeable income EC$400,000. At 33% tax is 132,000; at 25% it is 100,000; the gap is 32,000. Filing at 25% without IRD confirmation risks the 25% understatement penalty on the gap, 8,000 (derived), plus interest. Until IRD confirms the rate in writing, pay at the rate IRD's own guidance uses and claim the difference once the instrument is confirmed.

```oa-check
name: St Kitts corporation tax 33% vs 25% on 400,000
inputs:
  income: 400000
steps:
  - tax_33: income * 0.33
  - tax_25: income * 0.25
  - gap: tax_33 - tax_25
  - penalty_on_gap: gap * 0.25
expected:
  tax_33: 132000
  tax_25: 100000
  gap: 32000
  penalty_on_gap: 8000
```

## When to refuse or refer

- Choosing the rate without IRD confirmation.
- Residence and permanent establishment disputes; treaties.
- Tax holidays and approvals: [kn-special-regimes](kn-special-regimes.md).
- Losses and deductions not read here.

## Filing and payment

1. Register with IRD; pay instalments on the 15th of March, June, September and December.
2. File CIT-100 through SMARTS 3.5 months after year end (15 April for 31 December), with payment.
3. File CIT-101 where required.

## Completion checklist

- Company status and residence settled; rate decided and recorded.
- Four instalments; return 3.5 months after year end.
- CIT-101 where the entity type requires it.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act Cap. 20.22 (2017 revision): read for s.3(3) (no charge on non-companies from 1 May 1980), s.32 (33%), ss.36 and 37 | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_22-Income-Tax-Act.pdf | 2026-11-14 |
| Income Tax (Amendment) Act 12 of 2021: read for s.3A (resident and permanent establishment basis) | https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf | 2026-11-14 |
| IRD corporate income tax page: read for the 3.5-month return, 15 April, instalment dates and filing while inactive | https://www.sknird.com/corporate-income-tax/ | 2026-11-14 |
| IRD FAQs: read for instalments at 33% and the 25% understatement penalty | https://www.sknird.com/faqs/ | 2026-11-14 |
| SKNIS, 13 December 2023: read for the 25% rate announced from January 2024 | https://www.sknis.gov.kn/2023/12/13/corporate-income-tax-rate-in-st-kitts-and-nevis-set-at-25-from-january-2024/ | 2026-11-14 |
| IRD CIT-101 guidelines, September 2023: read for the information return | https://eservicesskn.sknird.com/ServiceProvider/Documents/CIT-101%20Guidelines%20Revised%20September%202023.pdf | 2026-11-11 |
| IRD announcements (March and April 2026 filing notices): read for the 15 April 2026 deadline | https://www.sknird.com/announcements-upcoming-events/ | 2026-11-11 |

Not yet confirmed: the instrument for the 25% rate and its coverage; deductions, losses and capital allowances (not read); late filing penalties; the CIT-101 and IRD announcement pages were read by Ryan Duguid on 2026-11-11 and not re-opened here.
