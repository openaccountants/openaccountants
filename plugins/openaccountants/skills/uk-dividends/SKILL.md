---
name: uk-dividends
description: "Use this skill whenever asked about UK dividend income taxation. Trigger on phrases like \"dividend tax UK\", \"dividend allowance\", \"dividend income\", \"company dividends\", \"director dividends\", \"salary vs dividends\", \"dividend voucher\", \"SA100 dividends\", \"foreign dividends UK\", \"dividend waiver\", \"dividend tax rates\", \"8.75%\", \"33.75%\", \"39.35%\", \"10.75%\", \"35.75%\", \"April 2026 dividend hike\", \"Autumn Budget 2025 dividend\", \"Scottish dividend tax\", or any question about computing, declaring, or optimising dividend income for UK individual taxpayers. Covers dividend allowance, rates, salary-vs-dividend planning for company directors, foreign dividends and double tax relief, dividend waivers, and interaction with other income. ALWAYS read this skill before touching any UK dividend work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-dividends"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# UK Dividends

## UK Dividend Income Skill v1.2

Changelog: v1.2 (2026-10-23): 2026/27 is now the working year. Example 3 recomputed at the 19% small profits rate with 15% employer NIC above GBP 5,000; Example 4 at the 35.75% upper rate; salary and dividend tables moved to 2026/27 rates; unsourced country withholding table replaced by a pointer to `uk-foreign-tax-and-withholding`; Sources table added.

v1.1: standardised on 3-year structure (2024-25 prior, 2025-26 current, 2026-27 from 6 April 2026); promoted Autumn Budget 2025 dividend rate hike (10.75% / 35.75%) into full Quick Reference table, added combined comparison table and a 2026-27 worked example.

## Rates and thresholds, 2026/27 (6 April 2026 to 5 April 2027)

> Source-cited draft: not reviewed by an accountant.

### Dividends and director pay, 2026/27

- **Dividend allowance (dividend nil rate)**: £500  _(ITA 2007 s.13A; https://www.gov.uk/tax-on-dividends)_
- **Dividend ordinary rate (basic rate band)**: 10.75%, up from 8.75%  _(Finance Act 2026 s.4; https://www.legislation.gov.uk/ukpga/2026/11/section/4)_
- **Dividend upper rate (higher rate band)**: 35.75%, up from 33.75%  _(Finance Act 2026 s.4)_
- **Dividend additional rate**: 39.35%, unchanged  _(https://www.gov.uk/tax-on-dividends)_
- **Section 455 charge on loans to participators**: 35.75%, tied to the dividend upper rate  _(https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note)_
- **Employer (secondary) NIC**: 15% above the secondary threshold of £5,000 a year  _(https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027)_
- **Employee primary threshold**: £242 a week (£12,570 a year); employee rate 8%, 2% above the upper earnings limit  _(same page)_
- **Lower earnings limit**: £129 a week (£6,708 a year)  _(same page)_
- **Corporation tax**: 19% on profits of £50,000 or less, 25% over £250,000, marginal relief in between  _(https://www.gov.uk/corporation-tax-rates)_

## Section 1 -- Quick Reference

**Quick Reference**  _(https://assets.publishing.service.gov.uk/media/69c14d07cfa346b9d4704a8d/SA100-2026.pdf)_

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income Tax on Dividend Income |
| Currency | GBP only |
| Tax year | 6 April to 5 April |
| Primary legislation | Income Tax Act 2007 (ITA 2007), ss. 8-21; Income Tax (Trading and Other Income) Act 2005 (ITTOIA), Part 4 |
| Supporting legislation | Corporation Tax Act 2009 (company-side); ITA 2007 s. 13A (dividend allowance); Finance Act 2022 (1.25% increase); Finance Act 2026 s. 4 (2 point increase from 2026/27) |
| Tax authority | HMRC |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January following the tax year |
| SA100 box | Box 4 (UK dividends); Box 5 (other dividends); Box 6 (foreign dividends up to £500) and Box 7 (tax taken off foreign dividends) on the main SA100, or SA106 (Foreign) supplementary pages |
| Status | Source-cited draft: not reviewed by an accountant |
| Skill version | 1.2 |

### Dividend Tax Rates (2024-25)

**Dividend Tax Rates (2024-25)**

| Tax band | Rate on dividends above allowance |
| --- | --- |
| Basic rate (£12,571--£50,270) | 8.75% |
| Higher rate (£50,271--£125,140) | 33.75% |
| Additional rate (over £125,140) | 39.35% |

### Dividend Tax Rates (2025-26)

**Dividend Tax Rates (2025-26)**

| Tax band | Rate on dividends above allowance |
| --- | --- |
| Basic rate (£12,571--£50,270) | 8.75% |
| Higher rate (£50,271--£125,140) | 33.75% |
| Additional rate (over £125,140) | 39.35% |

### Dividend Tax Rates (2026-27): from 6 April 2026

Announced at Autumn Budget 2025 and enacted by Finance Act 2026 (c. 11). Basic and higher rates increase by 2 percentage points; the additional rate is unchanged. The £500 dividend allowance is unchanged for 2026-27, and the income tax bands remain frozen through 2030-31 (Personal Allowance £12,570; basic rate band cap £50,270; additional rate threshold £125,140).

**Dividend Tax Rates (2026-27)**

| Tax band | Rate on dividends above allowance |
| --- | --- |
| Basic rate (£12,571--£50,270) | 10.75% |
| Higher rate (£50,271--£125,140) | 35.75% |
| Additional rate (over £125,140) | 39.35% |

### Combined Comparison: All Three Years

**Combined Comparison: All Three Years**

| Band | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Basic rate | 8.75% | 8.75% | 10.75% |
| Higher rate | 33.75% | 33.75% | 35.75% |
| Additional rate | 39.35% | 39.35% | 39.35% |
| Dividend allowance | £500 | £500 | £500 |

### Dividend Allowance History

**Dividend Allowance History**  _(https://www.gov.uk/government/publications/income-tax-dividend-allowance-reduction/income-tax-dividend-allowance-reduction)_

| Tax year | Allowance |
| --- | --- |
| 2026-27 | £500 |
| 2025-26 | £500 |
| 2024-25 | £500 |
| 2023-24 | £1,000 |
| 2022-23 | £2,000 |
| 2021-22 | £2,000 |
| 2018-19 to 2020-21 | £2,000 |
| 2016-17 to 2017-18 | £5,000 |

### How the Dividend Allowance Works

- **Dividend nil rate**: The first £500 of dividend income in the tax year is taxed at 0% (the "dividend nil rate")
- **Allowance mechanism**: The allowance does NOT reduce taxable income: it is a nil-rate band
- **Dividends above allowance**: Dividends above £500 are taxed at the dividend rate for the taxpayer's band
- **Counts towards total income**: The £500 still counts towards total income for determining which band other income/dividends fall into
- **Transfer/carry forward**: Cannot be transferred to a spouse; cannot be carried forward
- **Per person basis**: Applies per person, not per source

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown income band | STOP: dividend tax rate depends on total income |
| Unknown whether UK or foreign dividend | Treat as UK (no withholding tax complication) |
| Unknown whether dividend is from own company | STOP: affects IR35/salary-vs-dividend analysis |
| Unknown dividend waiver | Ignore waiver (full entitlement taxable) |

## Section 2 -- Computation Rules

### 2.1 Order of Taxation

- **Statutory order of taxation**: Income is taxed in this statutory order: 1. Non-savings income (employment, self-employment, property, pensions) 2. Savings income (interest) 3. Dividend income (last). This means dividends sit on top of all other income. A taxpayer with £45,000 salary has only £5,270 of basic rate band remaining (£50,270 - £45,000) before dividends push into the higher rate band.

### 2.2 Full Computation

- **Full computation steps**: Step 1: Calculate total income from all sources Step 2: Deduct personal allowance (£12,570) from non-savings income first Step 3: Apply non-savings rates to non-savings income Step 4: Apply savings rates to savings income (including PSA) Step 5: Apply dividend rates to dividend income Dividend tax (2026/27): First £500: 0% (dividend allowance) Remainder in basic rate band: 10.75% Remainder in higher rate band: 35.75% Remainder in additional rate band: 39.35%

### 2.3 Personal Allowance Reduction

- **PA taper**: If adjusted net income exceeds £100,000, the personal allowance is reduced by £1 for every £2 above £100,000. It is fully withdrawn at £125,140. Dividends count towards adjusted net income for this purpose, creating an effective marginal rate of ~60% in the £100,000--£125,140 band.

## Section 3 -- Company Director: Salary vs Dividends Optimisation

### 3.1 The Core Trade-Off

**The Core Trade-Off**  _(https://www.gov.uk/government/publications/changes-to-the-class-1-national-insurance-contributions-secondary-threshold-the-secondary-class-1-national-insurance-contributions-rate-and-the-empl/changes-to-the-class-1-national-insurance-contributions-secondary-threshold-the-secondary-class-1-national-insurance-contributions-rate-and-the-empl)_

| Payment type | Corporation Tax | Employee NIC | Employer NIC | Income Tax | Net in pocket |
| --- | --- | --- | --- | --- | --- |
| Salary | Deductible (reduces CT) | 8% (above £12,570) + 2% (above £50,270) | 15% (above £5,000) from 6 April 2025; 13.8% (above £9,100) before | 20%/40%/45% | Lower gross, but CT saved |
| Dividend | NOT deductible (paid from post-CT profits) | None | None | 10.75%/35.75%/39.35% (2026/27) | No NIC, but CT already paid |

### 3.2 Salary at the primary threshold (2026-27, single director-shareholder)

**Salary and dividends (2026-27, single director-shareholder)**  _(https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027; https://www.gov.uk/corporation-tax-rates)_

| Component | Amount | Rationale |
| --- | --- | --- |
| Salary | £12,570 (primary threshold and personal allowance) | No income tax and no employee NIC. Employer NIC: 15% × (£12,570 - £5,000) = £1,135.50. Salary and employer NIC (£13,705.50) are deductible for corporation tax: 19% if profits are £50,000 or less, 25% over £250,000, marginal relief in between. |
| Dividends | Remainder of post-tax profits | 0% on the first £500; 10.75% on the rest within the basic rate band; 35.75% above it |
| Alternative salary | £5,000 (secondary threshold) | No employer NIC. Below the lower earnings limit (£6,708 for 2026-27) it gives no State Pension qualifying year. |

Employment Allowance does not help here. If a company has only one director, that director must not be the only employee liable for secondary Class 1 NIC (https://www.gov.uk/claim-employment-allowance/eligibility).

From 6 April 2026 the dividend ordinary and upper rates are 2 points higher (Finance Act 2026 s.4). Re-run the salary and dividend comparison for each client each year. The right answer turns on the company's corporation tax rate and on the director's other income.

### 3.3 Combined effective rates (2026-27)

Each rate is the share of £1 of company profit that ends up as tax when the profit is paid out by one route. Salary route: the company pays salary plus 15% employer NIC, so £1 of profit buys £1 / 1.15 of salary; the director then pays income tax and employee NIC on it. Dividend route: corporation tax first, then dividend tax on what is left. Dividend allowance and personal allowance ignored.

**Combined effective rates (2026-27)**

| Director's band | Salary route (IT + employee NIC + 15% employer NIC) | Dividend route, company at 19% CT | Dividend route, company at 25% CT |
| --- | --- | --- | --- |
| Basic rate | 1 - (1 - 0.28) / 1.15 = 37.39% | 1 - 0.81 × 0.8925 = 27.71% | 1 - 0.75 × 0.8925 = 33.06% |
| Higher rate | 1 - (1 - 0.42) / 1.15 = 49.57% | 1 - 0.81 × 0.6425 = 47.96% | 1 - 0.75 × 0.6425 = 51.81% |
| Additional rate | 1 - (1 - 0.47) / 1.15 = 53.91% | 1 - 0.81 × 0.6065 = 50.87% | 1 - 0.75 × 0.6065 = 54.51% |

At 25% corporation tax, a higher-rate or additional-rate director now pays more tax by dividend than by salary on the marginal pound. Check the company's rate before advising.

### 3.4 Important Caveats

- **Salary commercial justification**: Salary must be commercially justifiable (not artificially low to avoid NIC)
- **HMRC challenge**: HMRC can challenge under employment intermediaries legislation
- **Employment contract**: Director must draw a proper employment contract
- **Lower Earnings Limit**: Salary below the Lower Earnings Limit (£6,708 for 2026-27: £129 a week) means no qualifying year for State Pension. Consider paying at least this level.
- **Distributable profits**: Dividends require distributable profits: cannot pay dividends from a loss-making company

## Section 4 -- Foreign Dividends

### 4.1 Reporting

- **Reporting pages**: Foreign dividends are reported on the SA106 (Foreign) supplementary pages, or SA100 Box 6 if they are £500 or less (foreign tax in Box 7)  _(https://assets.publishing.service.gov.uk/media/69c14d07cfa346b9d4704a8d/SA100-2026.pdf)_
- **Gross amount**: Report the gross amount (before foreign tax deducted)
- **GBP conversion**: Convert to GBP at the exchange rate on the date the dividend was paid (or the rate used by the paying agent)

### 4.2 Double Tax Relief (DTR)

**Double Tax Relief (DTR)**  _(https://www.legislation.gov.uk/ukpga/2010/8/section/9)_

| Method | Detail |
| --- | --- |
| Treaty relief | Credit for foreign tax paid, limited to UK tax on the same income |
| Unilateral relief | Available even without a treaty (TIOPA 2010 s. 9): credit for foreign tax up to UK tax |
| Maximum credit | Lower of: foreign tax paid, or UK tax attributable to the foreign income |
| Excess foreign tax | Cannot be carried forward or refunded; effectively wasted |

### 4.3 Foreign withholding rates

Withholding on foreign dividends depends on the paying country's law and its treaty with the UK. Read the treaty for the country concerned, and use `uk-foreign-tax-and-withholding` for the credit method and treaty rates. Credit is capped at the treaty rate even when more was withheld; reclaim the excess from the foreign tax authority, not from HMRC.

No foreign tax credit relief is available on dividends that fall within the £500 dividend allowance, because no UK tax is paid on them (SA106 notes 2026).

### 4.4 US Dividends and W-8BEN

UK residents receiving US dividends should give their US broker Form W-8BEN so the broker withholds at the treaty rate for portfolio dividends (15%, UK-US treaty Art 10(2)(b), see `uk-foreign-tax-and-withholding`) instead of 30%. The US tax withheld at the treaty rate is then credited against UK dividend tax.

## Section 5 -- Transaction Pattern Library

### 5.1 Dividend Income Patterns (Credits)

**Dividend Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DIVIDEND, DIV PAYMENT, INTERIM DIV, FINAL DIV | UK dividend income | Report gross amount on SA100 Box 4 |
| [Company name] DIVIDEND VOUCHER | UK dividend income | Voucher is the primary evidence: retain |
| HARGREAVES LANSDOWN DIV, AJ BELL DIV, FIDELITY | UK dividend income | Platform-held investments; platforms provide tax certificate |
| VANGUARD DISTRIBUTION, ISHARES DISTRIBUTION | UK dividend income (if UK fund) | Check if income or accumulation units |
| FOREIGN DIV, OVERSEAS DIVIDEND, USD PAYMENT | Foreign dividend | Report on SA106; convert to GBP; claim DTR |
| REIT DIVIDEND, PROPERTY INCOME DISTRIBUTION | UK PID: taxed as property income | NOT taxed as dividend: treated as property income at normal rates |
| SCRIP DIVIDEND, STOCK DIVIDEND | UK dividend | Taxable at the cash equivalent value |

### 5.2 Exclusions

**Exclusions**

| Pattern | Treatment |
| --- | --- |
| CAPITAL RETURN, RETURN OF CAPITAL | NOT dividend income: reduces cost base for CGT |
| ISA DIVIDEND | EXEMPT: no tax reporting required |
| PENSION FUND DIVIDEND | Not directly taxable to individual (within pension wrapper) |

## Section 6 -- Dividend Waivers

A shareholder may waive their right to a dividend. This is typically used in family company planning.

**Dividend Waivers Rules**

| Rule | Detail |
| --- | --- |
| Must be a deed of waiver | Executed before the dividend is declared |
| Must be unconditional | Cannot be conditional on another shareholder receiving more |
| Settlement legislation (ITTOIA s. 624) | If waiver is an "arrangement" to divert income to spouse, HMRC can tax the waiving shareholder |
| HMRC scrutiny | Waivers are commonly challenged; must have genuine commercial purpose |
| Safe approach | Waiver of all shares of one class, well in advance of dividend declaration |

## Section 7 -- Worked Examples

### Example 1 -- Basic Rate Taxpayer (2025-26 rates, for comparison)

Input: Employment income £30,000. UK dividends received £8,000. No other income.

Computation:
Total income: £38,000
Personal allowance: £12,570
Taxable non-savings: £17,430 (at 20% = £3,486)
Remaining basic rate band: £50,270 - £30,000 = £20,270

Dividend tax:
  First £500: 0%                = £0
  Remaining £7,500: 8.75%       = £656.25

Total dividend tax: £656.25

### Example 1b -- Same Scenario Under 2026-27 Rates

Input: Same as Example 1: Employment income £30,000, UK dividends £8,000, no other income: but for the 2026-27 tax year (from 6 April 2026).

Computation:
Total income: £38,000
Personal allowance: £12,570 (unchanged: frozen through 2030-31)
Taxable non-savings: £17,430 (at 20% = £3,486)
Remaining basic rate band: £50,270 - £30,000 = £20,270

Dividend tax (2026-27 rates):
  First £500: 0%                = £0
  Remaining £7,500: 10.75%      = £806.25

Total dividend tax: £806.25

Cost of the rate hike: £806.25 − £656.25 = £150 extra on the same £8,000 of dividends, purely from the basic rate moving from 8.75% to 10.75%. A higher-rate taxpayer in the same position would see proportionally larger increases at 35.75% vs 33.75%.

### Example 2 -- Dividend Straddling Basic/Higher Rate (2025-26 rates)

Input: Salary £48,000. UK dividends £10,000.

Computation:
Taxable salary: £48,000 - £12,570 = £35,430
Remaining basic rate band: £50,270 - £48,000 = £2,270

Dividend tax:
  First £500: 0%                        = £0
  Next £1,770 (fills basic rate band): 8.75% = £154.88
  Remaining £7,730: 33.75%              = £2,608.88

Total dividend tax: £2,763.76

### Example 3 -- Director Salary + Dividends (2026-27)

Input: Company profit before salary £60,000, accounting period inside the financial year from 1 April 2026, no associated companies. The director is the only employee, so no Employment Allowance. Salary £12,570; all post-tax profit paid as dividends. No other income.

Computation:
Company:
  Profit: £60,000
  Salary: £12,570 (deductible)
  Employer NIC: 15% × (£12,570 - £5,000) = £1,135.50 (deductible)
  Taxable profit: £60,000 - £12,570 - £1,135.50 = £46,294.50
  Corporation Tax: profit is £50,000 or less, so the 19% small profits rate applies: £46,294.50 × 19% = £8,795.96
  Available for dividends: £46,294.50 - £8,795.96 = £37,498.54

Director:
  Salary: £12,570 (covered by the personal allowance, £0 income tax)
  Employee NIC: 8% × (£12,570 - £12,570) = £0
  Dividends: £37,498.54, all inside the £37,700 basic rate band
    First £500: 0%
    Remaining £36,998.54 at 10.75% = £3,977.34

Total tax (company + personal): £8,795.96 + £1,135.50 + £3,977.34 = £13,908.80
Total extracted: £12,570 + £37,498.54 = £50,068.54
Tax as a share of the £60,000 profit: 23.18%

```oa-check
name: Director salary 12,570 plus dividends, company profit 60,000 (2026/27)
inputs:
  profit: 60000
  salary: 12570
  secondary_threshold: 5000
  dividend_allowance: 500
  basic_band: 37700
steps:
  - employer_nic: (salary - secondary_threshold) * 0.15
  - taxable_profit: profit - salary - employer_nic
  - corporation_tax: round(taxable_profit * 0.19, 2)
  - dividends: taxable_profit - corporation_tax
  - dividend_tax: round((min(dividends, basic_band) - dividend_allowance) * 0.1075, 2)
  - total_tax: corporation_tax + employer_nic + dividend_tax
  - extracted: salary + dividends
  - share_of_profit_pct: round(total_tax / profit * 100, 2)
expected:
  employer_nic: 1135.50
  taxable_profit: 46294.50
  corporation_tax: 8795.96
  dividends: 37498.54
  dividend_tax: 3977.34
  total_tax: 13908.80
  extracted: 50068.54
  share_of_profit_pct: 23.18
```

### Example 4 -- Foreign Dividends with Foreign Tax Credit Relief (2026-27)

Input: US dividends $5,000 (GBP equivalent £3,950). US withholding tax at the 15% treaty rate = $750 (£593). Higher rate UK taxpayer whose other income already uses the basic rate band. No other dividends.

Computation:
Gross foreign dividend: £3,950
First £500: dividend nil rate (no UK tax, so no credit on this slice)
UK tax on the rest at 35.75%: (£3,950 - £500) × 35.75% = £1,233.38
Credit: lower of US tax (£593) and UK tax on the dividend (£1,233.38) = £593
UK tax payable on the dividend: £1,233.38 - £593 = £640.38

```oa-check
name: Higher-rate taxpayer, US dividend 3,950 with 593 US tax (2026/27)
inputs:
  dividend: 3950
  us_tax: 593
  dividend_allowance: 500
steps:
  - uk_tax: round((dividend - dividend_allowance) * 0.3575, 2)
  - credit: min(us_tax, uk_tax)
  - uk_tax_payable: uk_tax - credit
expected:
  uk_tax: 1233.38
  credit: 593.00
  uk_tax_payable: 640.38
```

## Section 8 -- Edge Cases

### 8.1 Accumulation Units in Funds

- **Accumulation units taxable**: Income within accumulation units is still taxable to the investor: even though no cash is received. The fund manager issues a tax voucher showing the notional distribution. This is often overlooked.

### 8.2 Dividends vs Interest from Corporate Bonds

- **Corporate bond returns**: Returns from corporate bonds are interest (savings income), not dividends. Taxed at savings rates with the Personal Savings Allowance (£1,000 basic / £500 higher / £0 additional). Do not confuse with dividend rates.

### 8.3 REIT Dividends

- **PID taxation**: Property Income Distributions (PIDs) from UK REITs are taxed as property income at normal income tax rates (20%/40%/45%), NOT at dividend rates. The dividend allowance does NOT apply to PIDs. The ordinary part of a REIT dividend is taxed as a normal dividend.

### 8.4 Close Company Loans (Section 455)

- **Section 455 tax**: If a director borrows from their close company, the company pays Section 455 tax (33.75%; 35.75% for loans made from 6 April 2026). If the loan is written off, the director is taxed as if receiving a dividend. The Section 455 tax is refunded to the company.  _(https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note)_

### 8.5 Dividend in Specie

- **Dividend in specie**: A company can pay a dividend by transferring an asset (not cash). The dividend value is the market value of the asset. The company may have a Corporation Tax liability on the disposal of the asset.

## Section 9 -- Filing Requirements

**Filing Requirements**  _(https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends)_

| Scenario | Action |
| --- | --- |
| Total dividends ≤ £500 | No Self Assessment required (covered by allowance) |
| Total dividends > £500 and up to £10,000, not already in Self Assessment | Tell HMRC after 5 April and before 5 October: ask HMRC to update your tax code or contact the helpline |
| Dividends over £10,000 (any tax band) | Must file SA100; if you do not usually send a return, register by 5 October after the tax year |
| Foreign dividends (unless your only foreign income is dividends, total dividends including UK dividends are within the £500 dividend allowance and you have no other income to report) | Must file SA100 + SA106 |
| Company director taking dividends | Must file SA100 if dividends exceed £10,000 or you already send a Self Assessment return |

## PROHIBITIONS

NEVER apply dividend rates to REIT Property Income Distributions: they are taxed at normal income tax rates
NEVER carry forward or transfer the unused dividend allowance
NEVER ignore the Personal Allowance taper for incomes between £100,000 and £125,140
NEVER pay dividends without distributable reserves: this is a Companies Act breach
NEVER apply the dividend allowance to ISA dividends: ISA income is already exempt
NEVER forget that dividends still count as income for threshold purposes (PA taper, child benefit charge, student loan)
NEVER advise on salary-vs-dividends without checking State Pension qualifying year implications
NEVER present dividend tax computations as definitive: always label as estimated

## Sources

| Source | URL | Read on |
|---|---|---|
| GOV.UK, Tax on dividends (2026/27 rates, allowance) | https://www.gov.uk/tax-on-dividends | 2026-10-23 |
| GOV.UK, How to report tax on dividends (GBP 10,000 line, 5 October) | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends | 2026-10-23 |
| Finance Act 2026 s.4 (dividend ordinary and upper rates) | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-10-23 |
| ITA 2007 s.13A (dividend nil rate) | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-10-23 |
| HMRC technical note, change to tax rates for property, savings and dividend income (s.455 rate) | https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note | 2026-10-23 |
| GOV.UK, Rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-23 |
| GOV.UK, Employment Allowance eligibility | https://www.gov.uk/claim-employment-allowance/eligibility | 2026-10-23 |
| GOV.UK, Corporation Tax rates | https://www.gov.uk/corporation-tax-rates | 2026-10-23 |
| GOV.UK, Marginal Relief for Corporation Tax | https://www.gov.uk/guidance/corporation-tax-marginal-relief | 2026-10-23 |
| TIOPA 2010 s.9 (unilateral relief) | https://www.legislation.gov.uk/ukpga/2010/8/section/9 | 2026-10-23 |
| SA100 2026 form (dividend boxes) | https://assets.publishing.service.gov.uk/media/69c14d07cfa346b9d4704a8d/SA100-2026.pdf | 2026-10-23 |

Not yet confirmed: foreign withholding rates for countries other than the US (see `uk-foreign-tax-and-withholding` for treaty rates); Scottish taxpayers use UK dividend rates but Scottish bands for non-savings income (see `uk-scottish-income-tax`).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-dividends` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-dividends. If neither is available, confirm every figure against the official source pages cited above before relying on it.
