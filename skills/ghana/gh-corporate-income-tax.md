---
name: gh-corporate-income-tax
description: >
  Use this skill to compute or review Ghana corporate income tax for tax year 2026. It covers resident and non-resident companies, the 25% general rate, sector rates for hotels, non-traditional exports, farming and leasing loans, manufacturing by location, free zones, mining and petroleum, the 5% rate for concession holders, capital allowances, five-year loss carry-forward, thin capitalisation, minimum chargeable income of 5% of turnover, the Growth and Sustainability Levy, withholding credits, quarterly instalments, forms DT 101 and DT 102 on ETAX, and penalties. Trigger on "Ghana company tax", "CIT Ghana", "corporate income tax GRA", "capital allowance Ghana", "provisional tax Ghana", "minimum chargeable income". Individuals are in ghana-pit; cross-border withholding is in gh-cross-border.
version: 0.2
jurisdiction: GH
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026 (year of assessment). Law: Income Tax Act, 2015 (Act 896) as amended; Revenue Administration Act, 2016 (Act 915).

## Who this applies to

Companies incorporated in Ghana or elsewhere, and bodies taxed like them: societies, pension funds, governments, partnerships with at least twenty limited partners, unit trusts with at least twenty beneficiaries ([GRA](https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/)). A non-resident company with a Ghanaian permanent establishment is taxed in the same manner as a resident. A company is resident if incorporated under Ghanaian company law, or if its management and control is exercised in Ghana at any time in the year ([Act 896 s.101(4)](https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf)). Residents are taxed on worldwide income, non-residents on Ghana income.

## Rates, bands and thresholds

| Item | Rate | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| General rate | 25% | Default | 2026 | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ |
| Hotels | 22% | Principally in the hotel industry | 2026 | same |
| Non-traditional exports | 8% | Income from those exports | 2026 | same |
| Bank loans to farming, loans to leasing companies | 20% | That income only | 2026 | same |
| Manufacturing in regional capitals | 18.5% | Except Accra and Tema | 2026 | same |
| Manufacturing elsewhere | 12.5% | Outside Accra, Tema and regional capitals | 2026 | same |
| Free zone, domestic sales | 25% | After the 10-year holiday | 2026 | same |
| Free zone, exports | 15% | After the 10-year holiday | 2026 | same |
| Petroleum, minerals | 35% | Income from those operations | 2026 | same |
| Sixth Schedule concessions | 5% of chargeable income | During the concession period | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Lottery operations | 20% of gross gaming revenue | First Schedule para 7A | 2026 | same |
| Young entrepreneurs after 5-year holiday | 15% Accra, Tema; 12.5% other capitals; 10% elsewhere; 5% three northern regions | Listed sectors | 2026 | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ |
| Minimum chargeable income | 5% of turnover | Losses declared for previous five years; not first five years of operations; not farming | 2026 | https://gra.gov.gh/wp-content/uploads/2024/05/Practice-Note-on-the-Application-of-Minimum-Chargeabe-Income-under-the-Income-Tax-Act-2015-Act-896.pdf |
| Thin capitalisation | 3 to 1 debt to equity | Non-financial resident entity 50% or more held by exempt persons, such as non-residents; interest and exchange loss on the excess debt are not deductible (s.33) | 2026 | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf |
| Growth and Sustainability Levy, Category A | 5% of profit before tax | Banks, insurers, telecoms, breweries, oil marketing and others listed | 2026 | https://www.mofep.gov.gh/sites/default/files/reports/revenue/2025%20Annual%20Tax%20Revenue%20Performance%20Report.pdf |
| GSL, mining and upstream oil and gas | 3% of gross production | Rate raised by the 2025 amendment; gold changed later, see Sources | 2026 | same |
| GSL, Category C | 2.5% of profit before tax | All other entities (Act 1095 Schedule). Due even in a tax holiday (Act 1095 s.2) | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/GROWTH-AND-SUSTAINABILITY-LEVY-ACT-2023-ACT-1095.pdf |

Concession periods in the GRA table: agro processing and cocoa by-products 5 years, tree crops 10, cash crops and livestock 5, cattle 10, waste processing 7, low-cost housing. The rate during a holiday is the 5% above, then 25%.

| Capital allowance class | Assets | Rate | Method | Official URL |
|---|---|---|---|---|
| 1 | Computers and data equipment | 40% | Reducing balance | https://gra.gov.gh/domestic-tax/capital-allowance/ |
| 2 | Vehicles, construction equipment, manufacturing plant, plantation costs | 30% | Reducing balance | same |
| 3 | Rail, ships, aircraft, public utility plant, office furniture, other assets | 20% | Reducing balance | same |
| 4 | Buildings and permanent structures | 10% | Straight line | same |
| 5 | Intangibles | 1 / useful life | Straight line | same |
| Petroleum | Separate pool | 20% | Straight line | same |
| Excise stamp machinery | Affixing excise stamps | 50% | Importer or manufacturer of excisable goods | same |

## The base

1. Start with accounting profit. Assessable income is worldwide for residents, Ghana-source for non-residents.
2. Add back book depreciation; deduct capital allowance. Formula: basis x rate x days / 365. The asset must be owned, used in the business and held at period end. Unused allowance does not carry over.
3. Deduct expenses wholly incurred in earning income. GSL is not deductible ([Act 1095 s.3](https://gra.gov.gh/wp-content/uploads/2023/04/GROWTH-AND-SUSTAINABILITY-LEVY-ACT-2023-ACT-1095.pdf)).
4. Foreign exchange: revenue losses on debts or holdings deduct. Unrealised losses do not; nor do losses between two residents. Capital losses may be capitalised ([Act 1094 s.4](https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf)).
5. Deduct unrelieved losses of any of the previous five years ([Act 1094 s.3](https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf)).
6. Apply the thin capitalisation limit and the anti-avoidance rule (s.34).
7. Test minimum chargeable income: if the five-year loss test is met, tax is 25% of 5% of turnover when that exceeds the normal result. Tax paid on it is no credit for another year, and unrelieved losses still carry forward ([Practice Note 4.3, 4.4](https://gra.gov.gh/wp-content/uploads/2024/05/Practice-Note-on-the-Application-of-Minimum-Chargeabe-Income-under-the-Income-Tax-Act-2015-Act-896.pdf)).
8. Apply the rate, then credit withholding tax, instalments and foreign tax credit (s.112).

Gains on assets of a business go into the annual return and are taxed at the business rate ([GRA](https://gra.gov.gh/domestic-tax/tax-types/capital-gains-tax/)). A resident payer that is not an individual withholds 3% (resident seller) or 10% (non-resident) of the consideration ([Act 1094 s.13](https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf)).

## Deadlines and filing

| Obligation | Date | Form | Official URL |
|---|---|---|---|
| Register tax type | On starting | Portal or Taxpayer Service Centre | https://gra.gov.gh/domestic-tax/tax-registration/ |
| Estimate | Within the first quarter; can be revised to the last day of the basis period | DT 102, DT 102A | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ |
| Instalments, December year end | 31 March, 30 June, 30 September, 31 December | Portal payment | same |
| GSL estimate | By the first instalment; pay quarterly on the same dates | GRA form | https://gra.gov.gh/wp-content/uploads/2023/04/GROWTH-AND-SUSTAINABILITY-LEVY-ACT-2023-ACT-1095.pdf |
| Annual return | Four months after year end: 30 April 2027 for 2026 | DT 101 | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf |
| Transfer pricing return | Four months after year end | See [gh-transfer-pricing](gh-transfer-pricing.md) | https://gra.gov.gh/wp-content/uploads/2023/12/Transfer-Pricing-Regulations-2020-LI-24121-_231207_142107.pdf |

A non-December basis period pays on the last day of months 3, 6, 9 and 12 of that period (s.121(2)(a)). Section 124 counts the return from year of assessment; confirm with GRA the due date for a non-December period.

**Filing DT 101 on ETAX ([ITAS](https://gra.gov.gh/itas-faqs/)):**

1. Activate the company account at www.etax.gra.gov.gh with TIN and the registered contact, and update the profile.
2. Open the company income tax return. Review pre-filled data.
3. Enter the accounts, capital allowance schedule, and rates by income class. Upload accounts and withholding certificates.
4. A duly authorised manager signs the declaration (Act 915 s.28). A paid preparer signs too (s.29).
5. Submit and keep the acknowledgement. Pay any balance in ETAX through Ghana.gov.

## Penalties and interest

| Failure | Consequence | Official URL |
|---|---|---|
| Late return | GHS 500 plus GHS 10 a day | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |
| Late payment | 125% of the Bank of Ghana policy rate, compounded monthly | same |
| Estimate below 90% of correct tax | Interest on the shortfall | same |
| No proper records | 75% of the tax if deliberate; otherwise lesser of that and GHS 250, monthly | same |
| False statement | 100% or 30% of the shortfall | https://gra.gov.gh/domestic-tax/tax-offences-and-penalties/ |

## Cross-border points

- Dividends, interest, service fees and royalties to non-residents: see [gh-cross-border](gh-cross-border.md).
- Related-party terms: see [gh-transfer-pricing](gh-transfer-pricing.md).
- Branches pay 8% on repatriated profits ([GRA](https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/)).

## Two worked examples that recompute

**Example 1: standard company.** Accounting profit GHS 1,000,000, depreciation 200,000, capital allowance 260,000. Chargeable income GHS 940,000. Tax at 25%, GHS 235,000. Instalments paid 150,000 and withholding credits 35,000 leave GHS 50,000 with the return.

```oa-check
name: Company with 940,000 chargeable income
inputs:
  profit: 1000000
  depreciation: 200000
  allowance: 260000
  paid: 185000
steps:
  - chargeable: profit + depreciation - allowance
  - tax: chargeable * 0.25
  - balance: tax - paid
expected:
  chargeable: 940000.00
  tax: 235000.00
  balance: 50000.00
```

**Example 2: does minimum chargeable income bite?** A company past its first five years has declared losses for five years. In 2026 it has turnover GHS 8,000,000 and chargeable income nil. Minimum chargeable income is 400,000, so tax is GHS 100,000. If it had GHS 500,000 of ordinary chargeable income, tax of 125,000 is higher, and that applies.

```oa-check
name: Minimum chargeable income on 8,000,000 turnover
inputs:
  turnover: 8000000
  normal: 0
steps:
  - mci: turnover * 0.05
  - base: max(mci, normal)
  - tax: base * 0.25
expected:
  tax: 100000.00
```

## Ask the client first

1. Year end, and when operations began.
2. Sector, location, free zone status, any concession and its start date.
3. Five-year loss history and turnover.
4. Related parties, foreign shareholders, debt to equity.
5. Which GSL category applies.
6. Fixed assets by class.

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA, Corporate Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ | 2026-11-01 |
| Income Tax (Amendment) Act, 2023 (Act 1094), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf | 2026-11-01 |
| GRA Practice Note on Minimum Chargeable Income, OCR, whole note | https://gra.gov.gh/wp-content/uploads/2024/05/Practice-Note-on-the-Application-of-Minimum-Chargeabe-Income-under-the-Income-Tax-Act-2015-Act-896.pdf | 2026-11-01 |
| Income Tax Act, 2015 (Act 896), OCR of scan; ss 33, 101, 102, 112, 121, 124, 125 read | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |
| Ministry of Finance, 2025 Annual Tax Revenue Performance Report; GSL passages and Appendix Table 9 read | https://www.mofep.gov.gh/sites/default/files/reports/revenue/2025%20Annual%20Tax%20Revenue%20Performance%20Report.pdf | 2026-11-01 |
| Growth and Sustainability Levy Act, 2023 (Act 1095), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/GROWTH-AND-SUSTAINABILITY-LEVY-ACT-2023-ACT-1095.pdf | 2026-11-01 |
| GRA, Capital Allowance page, page read in full | https://gra.gov.gh/domestic-tax/capital-allowance/ | 2026-11-01 |
| GRA, Withholding Tax page (rates table, last edited 2022), page read in full | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ | 2026-11-01 |
| GRA, Capital Gains Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/capital-gains-tax/ | 2026-11-01 |
| GRA, Tax Registration page, page read in full | https://gra.gov.gh/domestic-tax/tax-registration/ | 2026-11-01 |
| GRA, Tax Offences and Penalties page, page read in full | https://gra.gov.gh/domestic-tax/tax-offences-and-penalties/ | 2026-11-01 |
| GRA, ITAS FAQs, page read in full | https://gra.gov.gh/itas-faqs/ | 2026-11-01 |
| Transfer Pricing Regulations, 2020 (L.I. 2412); regs 11, 12, 13, 16 read | https://gra.gov.gh/wp-content/uploads/2023/12/Transfer-Pricing-Regulations-2020-LI-24121-_231207_142107.pdf | 2026-11-01 |

Not yet confirmed: (1) The GRA CIT page says businesses pay 1% during holidays; Act 1094 sets 5%, and the Act is followed. (2) Text of the GSL amendment Act 1131 and of a 2026 GSL amendment for gold was not opened; the Finance Ministry report confirms the 3% rate and the sunset to 2028, but the current gold rate is not confirmed. The Category A and C rates are from Act 1095 as enacted; the amendment was not read to confirm they are unchanged. Example figures here leave GSL out. (3) Act 896 is the 2015 scan; later amendments other than Act 1094 and the Act 1178 notice were not read, including Acts 1066 and 1071. (4) Financial Sector Recovery Levy status for 2026. (5) DT 101 screen layout on ETAX.

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
