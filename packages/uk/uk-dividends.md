---
name: uk-dividends
description: Use this skill whenever asked about UK dividend income taxation. Trigger on phrases like "dividend tax UK", "dividend allowance", "dividend income", "company dividends", "director dividends", "salary vs dividends", "dividend voucher", "SA100 dividends", "foreign dividends UK", "dividend waiver", "dividend tax rates", "8.75%", "33.75%", "39.35%", "10.75%", "35.75%", "April 2026 dividend hike", "Autumn Budget 2025 dividend", "Scottish dividend tax", or any question about computing, declaring, or optimising dividend income for UK individual taxpayers. Covers dividend allowance, rates, salary-vs-dividend planning for company directors, foreign dividends and double tax relief, dividend waivers, and interaction with other income. ALWAYS read this skill before touching any UK dividend work.
version: 1.1
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on: - uk-income-tax-sa100
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Dividends

## UK Dividend Income Skill v1.1

Changelog: v1.1 — standardised on 3-year structure (2024-25 prior, 2025-26 current, 2026-27 from 6 April 2026); promoted Autumn Budget 2025 dividend rate hike (10.75% / 35.75%) into full Quick Reference table, added combined comparison table and a 2026-27 worked example.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by James Power on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Dividends

- **Dividend allowance 2025-26** — £500  _(ITA 2007 s.13A)_
- **Dividend allowance 2024-25** — £500  _(ITA 2007 s.13A)_
- **Basic rate** — 8.75%  _(ITA 2007)_
- **Higher rate (£50,271--£125,140)** — 33.75%  _(https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past)_
- **Additional rate** — 39.35%  _(ITA 2007)_
- **Optimal salary** — £12,570 (PA level) or £5,000 (ST level)  _(Tax planning)_
- **Employer NIC secondary threshold** — £5,000/year  _(SSCBA 1992)_
- **Basic rate (2026-27)** — 10.75% (up from 8.75%)  _(Finance (No.2) Bill 2024-26)_
- **Higher rate (2026-27)** — 35.75% (up from 33.75%)  _(Finance (No.2) Bill 2024-26)_
- **Additional rate (2026-27)** — 39.35% (unchanged)  _(Finance (No.2) Bill 2024-26)_
- **Dividend allowance (2026-27)** — £500 (unchanged)  _(ITA 2007 s.13A)_
- **Combined CT + higher-rate dividend (2026-27)** — ~51.78% (up from ~50.28%)  _(Calculated)_
- **Impact on salary-vs-dividend** — Dividend advantage over salary narrows materially from 6 April 2026  _(Tax planning note)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income Tax on Dividend Income |
| Currency | GBP only |
| Tax year | 6 April to 5 April |
| Primary legislation | Income Tax Act 2007 (ITA 2007), ss. 8-21; Income Tax (Trading and Other Income) Act 2005 (ITTOIA), Part 4 |
| Supporting legislation | Corporation Tax Act 2009 (company-side); ITA 2007 s. 13A (dividend allowance); Finance Act 2022 (1.25% increase) |
| Tax authority | HMRC |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January following the tax year |
| SA100 box | Box 4 (UK dividends); Box 5 (foreign dividends) on the main SA100 or SA106 (Foreign) supplementary pages |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 1.1 |

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

### Dividend Tax Rates (2026-27) — from 6 April 2026

Announced at Autumn Budget 2025 and enacted via Finance (No. 2) Bill 2024-26. Basic and higher rates increase by 2 percentage points; the additional rate is unchanged. The £500 dividend allowance is unchanged for 2026-27, and the income tax bands remain frozen through 2027-28 (Personal Allowance £12,570; basic rate band cap £50,270; additional rate threshold £125,140).

**Dividend Tax Rates (2026-27)**

| Tax band | Rate on dividends above allowance |
| --- | --- |
| Basic rate (£12,571--£50,270) | 10.75% |
| Higher rate (£50,271--£125,140) | 35.75% |
| Additional rate (over £125,140) | 39.35% |

### Combined Comparison — All Three Years

**Combined Comparison — All Three Years**

| Band | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Basic rate | 8.75% | 8.75% | 10.75% |
| Higher rate | 33.75% | 33.75% | 35.75% |
| Additional rate | 39.35% | 39.35% | 39.35% |
| Dividend allowance | £500 | £500 | £500 |

### Dividend Allowance History

**Dividend Allowance History**

| Tax year | Allowance |
| --- | --- |
| 2024-25 | £500 |
| 2025-26 | £500 |
| 2023-24 | £1,000 |
| 2022-23 | £2,000 |
| 2021-22 | £2,000 |
| 2017-18 to 2020-21 | £2,000 |
| 2016-17 | £5,000 |

### How the Dividend Allowance Works

- **Dividend nil rate** — The first £500 of dividend income in the tax year is taxed at 0% (the "dividend nil rate")
- **Allowance mechanism** — The allowance does NOT reduce taxable income — it is a nil-rate band
- **Dividends above allowance** — Dividends above £500 are taxed at the dividend rate for the taxpayer's band
- **Counts towards total income** — The £500 still counts towards total income for determining which band other income/dividends fall into
- **Transfer/carry forward** — Cannot be transferred to a spouse; cannot be carried forward
- **Per person basis** — Applies per person, not per source

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown income band | STOP — dividend tax rate depends on total income |
| Unknown whether UK or foreign dividend | Treat as UK (no withholding tax complication) |
| Unknown whether dividend is from own company | STOP — affects IR35/salary-vs-dividend analysis |
| Unknown dividend waiver | Ignore waiver (full entitlement taxable) |

## Section 2 -- Computation Rules

### 2.1 Order of Taxation

- **Statutory order of taxation** — Income is taxed in this statutory order: 1. Non-savings income (employment, self-employment, property, pensions) 2. Savings income (interest) 3. Dividend income (last). This means dividends sit on top of all other income. A taxpayer with £45,000 salary has only £5,270 of basic rate band remaining (£50,270 - £45,000) before dividends push into the higher rate band.

### 2.2 Full Computation

- **Full computation steps** — Step 1: Calculate total income from all sources Step 2: Deduct personal allowance (£12,570) from non-savings income first Step 3: Apply non-savings rates to non-savings income Step 4: Apply savings rates to savings income (including PSA) Step 5: Apply dividend rates to dividend income Dividend tax: First £500: 0% (dividend allowance) Remainder in basic rate band: 8.75% Remainder in higher rate band: 33.75% Remainder in additional rate band: 39.35%

### 2.3 Personal Allowance Reduction

- **PA taper** — If adjusted net income exceeds £100,000, the personal allowance is reduced by £1 for every £2 above £100,000. It is fully withdrawn at £125,140. Dividends count towards adjusted net income for this purpose, creating an effective marginal rate of ~60% in the £100,000--£125,140 band.

## Section 3 -- Company Director: Salary vs Dividends Optimisation

### 3.1 The Core Trade-Off

**The Core Trade-Off**

| Payment type | Corporation Tax | Employee NIC | Employer NIC | Income Tax | Net in pocket |
| --- | --- | --- | --- | --- | --- |
| Salary | Deductible (reduces CT) | 8% (above £12,570) + 2% (above £50,270) | 13.8% (above £9,100) | 20%/40%/45% | Lower gross, but CT saved |
| Dividend | NOT deductible (paid from post-CT profits) | None | None | 8.75%/33.75%/39.35% | No NIC, but CT already paid |

### 3.2 Optimal Strategy (2024-25, Single Director-Shareholder)

**Optimal Strategy (2024-25, Single Director-Shareholder)**

| Component | Amount | Rationale |
| --- | --- | --- |
| Salary | £12,570 (PA level) | Tax-free; employer NIC: 13.8% × (£12,570 - £9,100) = £479; CT deduction saves 25% × £12,570 = £3,143 |
| Dividends | Remainder of profits | 0% on first £500; 8.75% on remainder within basic rate band |
| NIC threshold salary alternative | £9,100 (Secondary Threshold) | Zero employer NIC; small sacrifice of personal allowance |

Optimal for most single directors: Salary at £12,570, dividends for the rest up to the basic rate band limit. Beyond basic rate, the combined CT + dividend tax rate increases. The strategy above is calibrated to the 2024-25 tax year (rates unchanged for 2025-26).

2026-27 impact: The Autumn Budget 2025 dividend hike (basic 8.75% → 10.75%; higher 33.75% → 35.75%) narrows the dividend advantage over salary, particularly for higher-rate director-shareholders. The combined CT + higher-rate dividend cost rises from ~50.28% to ~51.78%, eroding most of the gap against the salary route. Single directors should still favour salary at the Primary Threshold plus dividends, but the savings vs. a pure-salary extraction will be materially smaller from 6 April 2026 — re-run the comparison annually.

### 3.3 Combined Effective Rates (2024-25)

**Combined Effective Rates (2024-25)**

| Income band | Salary effective rate | Dividend effective rate |
| --- | --- | --- |
| Up to PA (£12,570) | NIC only (employer) | 0% (within PA + allowance) |
| Basic rate | 20% IT + 8% NIC + 13.8% ER NIC = ~34.25% (offset by CT deduction) | 25% CT + 8.75% on remainder = ~32.19% combined |
| Higher rate | 40% IT + 2% NIC + 13.8% ER NIC = ~49.03% (offset by CT deduction) | 25% CT + 33.75% on remainder = ~50.28% combined |
| Additional rate | 45% IT + 2% NIC + 13.8% ER NIC = ~53.43% (offset by CT deduction) | 25% CT + 39.35% on remainder = ~54.51% combined |

### 3.4 Important Caveats

- **Salary commercial justification** — Salary must be commercially justifiable (not artificially low to avoid NIC)
- **HMRC challenge** — HMRC can challenge under employment intermediaries legislation
- **Employment contract** — Director must draw a proper employment contract
- **Lower Earnings Limit** — Salary below the Lower Earnings Limit (£6,396 for 2024-25) means no qualifying year for State Pension — consider paying at least this level
- **Distributable profits** — Dividends require distributable profits — cannot pay dividends from a loss-making company

## Section 4 -- Foreign Dividends

### 4.1 Reporting

- **Reporting pages** — Foreign dividends are reported on the SA106 (Foreign) supplementary pages, or SA100 Box 5 if straightforward
- **Gross amount** — Report the gross amount (before foreign tax deducted)
- **GBP conversion** — Convert to GBP at the exchange rate on the date the dividend was paid (or the rate used by the paying agent)

### 4.2 Double Tax Relief (DTR)

**Double Tax Relief (DTR)**

| Method | Detail |
| --- | --- |
| Treaty relief | Credit for foreign tax paid, limited to UK tax on the same income |
| Unilateral relief | Available even without a treaty (ITA 2007 s. 18) — credit for foreign tax up to UK tax |
| Maximum credit | Lower of: foreign tax paid, or UK tax attributable to the foreign income |
| Excess foreign tax | Cannot be carried forward or refunded; effectively wasted |

### 4.3 Common Foreign Dividend Withholding Rates

**Common Foreign Dividend Withholding Rates**

| Country | Typical WHT on dividends | Treaty rate (to UK) |
| --- | --- | --- |
| USA | 30% (statutory) | 15% (treaty) |
| Ireland | 25% | 15% |
| France | 25% | 15% |
| Germany | 26.375% (incl. Soli) | 15% |
| Australia | 0% (franked) / 30% (unfranked) | 15% |
| Canada | 25% | 15% |

### 4.4 US Dividends and W-8BEN

UK residents receiving US dividends should file Form W-8BEN with their US broker to claim the 15% treaty rate (instead of 30%). The 15% US withholding tax is then credited against UK dividend tax via DTR.

## Section 5 -- Transaction Pattern Library

### 5.1 Dividend Income Patterns (Credits)

**Dividend Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DIVIDEND, DIV PAYMENT, INTERIM DIV, FINAL DIV | UK dividend income | Report gross amount on SA100 Box 4 |
| [Company name] DIVIDEND VOUCHER | UK dividend income | Voucher is the primary evidence — retain |
| HARGREAVES LANSDOWN DIV, AJ BELL DIV, FIDELITY | UK dividend income | Platform-held investments; platforms provide tax certificate |
| VANGUARD DISTRIBUTION, ISHARES DISTRIBUTION | UK dividend income (if UK fund) | Check if income or accumulation units |
| FOREIGN DIV, OVERSEAS DIVIDEND, USD PAYMENT | Foreign dividend | Report on SA106; convert to GBP; claim DTR |
| REIT DIVIDEND, PROPERTY INCOME DISTRIBUTION | UK PID — taxed as property income | NOT taxed as dividend — treated as property income at normal rates |
| SCRIP DIVIDEND, STOCK DIVIDEND | UK dividend | Taxable at the cash equivalent value |

### 5.2 Exclusions

**Exclusions**

| Pattern | Treatment |
| --- | --- |
| CAPITAL RETURN, RETURN OF CAPITAL | NOT dividend income — reduces cost base for CGT |
| ISA DIVIDEND | EXEMPT — no tax reporting required |
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

### Example 1 -- Basic Rate Taxpayer

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

Input: Same as Example 1 — Employment income £30,000, UK dividends £8,000, no other income — but for the 2026-27 tax year (from 6 April 2026).

Computation:
Total income: £38,000
Personal allowance: £12,570 (unchanged — frozen through 2027-28)
Taxable non-savings: £17,430 (at 20% = £3,486)
Remaining basic rate band: £50,270 - £30,000 = £20,270

Dividend tax (2026-27 rates):
  First £500: 0%                = £0
  Remaining £7,500: 10.75%      = £806.25

Total dividend tax: £806.25

Cost of the rate hike: £806.25 − £656.25 = £150 extra on the same £8,000 of dividends, purely from the basic rate moving from 8.75% to 10.75%. A higher-rate taxpayer in the same position would see proportionally larger increases at 35.75% vs 33.75%.

### Example 2 -- Dividend Straddling Basic/Higher Rate

Input: Salary £48,000. UK dividends £10,000.

Computation:
Taxable salary: £48,000 - £12,570 = £35,430
Remaining basic rate band: £50,270 - £48,000 = £2,270

Dividend tax:
  First £500: 0%                        = £0
  Next £1,770 (fills basic rate band): 8.75% = £154.88
  Remaining £7,730: 33.75%              = £2,608.88

Total dividend tax: £2,763.76

### Example 3 -- Director Salary + Dividends

Input: Company profit before salary: £60,000. Director takes £12,570 salary, rest as dividends. Corporation Tax 25%.

Computation:
Company:
  Profit: £60,000
  Salary: £12,570 (deductible)
  Employer NIC: 13.8% × (£12,570 - £9,100) = £479 (deductible)
  Taxable profit: £60,000 - £12,570 - £479 = £46,951
  Corporation Tax: £46,951 × 25% = £11,738
  Available for dividends: £46,951 - £11,738 = £35,213

Director:
  Salary: £12,570 (covered by PA = £0 IT)
  Employee NIC: 8% × (£12,570 - £12,570) = £0
  Dividends: £35,213
    First £500: 0%
    Next £37,200 remaining basic rate band: 8.75% on £34,713 = £3,037.39

Total tax paid (company + personal): £11,738 + £479 + £3,037.39 = £15,254.39
Total extracted: £12,570 + £35,213 = £47,783
Effective combined rate: 24.2%

### Example 4 -- Foreign Dividends with DTR

Input: US dividends $5,000 (GBP equivalent £3,950). US withholding tax 15% = $750 (£593). Higher rate UK taxpayer.

Computation:
Gross foreign dividend: £3,950
UK tax at 33.75%: £3,950 × 33.75% = £1,333.13
(Less dividend allowance applied: £500 × 33.75% saving = £168.75)
Adjusted: (£3,950 - £500) × 33.75% = £1,164.38
DTR credit: £593 (limited to UK tax on the foreign income)
UK tax payable: £1,164.38 - £593 = £571.38

## Section 8 -- Edge Cases

### 8.1 Accumulation Units in Funds

- **Accumulation units taxable** — Income within accumulation units is still taxable to the investor — even though no cash is received. The fund manager issues a tax voucher showing the notional distribution. This is often overlooked.

### 8.2 Dividends vs Interest from Corporate Bonds

- **Corporate bond returns** — Returns from corporate bonds are interest (savings income), not dividends. Taxed at savings rates with the Personal Savings Allowance (£1,000 basic / £500 higher / £0 additional). Do not confuse with dividend rates.

### 8.3 REIT Dividends

- **PID taxation** — Property Income Distributions (PIDs) from UK REITs are taxed as property income at normal income tax rates (20%/40%/45%), NOT at dividend rates. The dividend allowance does NOT apply to PIDs. The ordinary part of a REIT dividend is taxed as a normal dividend.

### 8.4 Close Company Loans (Section 455)

- **Section 455 tax** — If a director borrows from their close company, the company pays Section 455 tax (33.75%). If the loan is written off, the director is taxed as if receiving a dividend. The Section 455 tax is refunded to the company.

### 8.5 Dividend in Specie

- **Dividend in specie** — A company can pay a dividend by transferring an asset (not cash). The dividend value is the market value of the asset. The company may have a Corporation Tax liability on the disposal of the asset.

## Section 9 -- Filing Requirements

**Filing Requirements**

| Scenario | Action |
| --- | --- |
| Total dividends ≤ £500 | No Self Assessment required (covered by allowance) |
| Total dividends > £500, all UK, basic rate taxpayer | May need to complete SA100; HMRC may collect via Simple Assessment or PAYE code adjustment |
| Higher/additional rate taxpayer with dividends | Must file SA100 |
| Foreign dividends of any amount | Must file SA100 + SA106 |
| Company director taking dividends | Must file SA100 |

## PROHIBITIONS

NEVER apply dividend rates to REIT Property Income Distributions — they are taxed at normal income tax rates
NEVER carry forward or transfer the unused dividend allowance
NEVER ignore the Personal Allowance taper for incomes between £100,000 and £125,140
NEVER pay dividends without distributable reserves — this is a Companies Act breach
NEVER apply the dividend allowance to ISA dividends — ISA income is already exempt
NEVER forget that dividends still count as income for threshold purposes (PA taper, child benefit charge, student loan)
NEVER advise on salary-vs-dividends without checking State Pension qualifying year implications
NEVER present dividend tax computations as definitive — always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ Book a call (https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at openaccountants.com/network.

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
