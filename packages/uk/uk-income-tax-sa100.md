---
name: uk-income-tax-sa100
description: >
  Use this skill whenever asked about UK income tax for individuals filing SA100 Self Assessment. Trigger on phrases like "income tax UK", "SA100", "personal allowance", "tax bands", "tax computation", "marriage allowance", "savings allowance", "dividend allowance", "Scottish tax rates", "payments on account", "tax reducers", "tax relief", or any question about computing a UK individual's income tax liability. Covers personal allowance (including taper), income tax bands for rUK and Scotland, marriage allowance, savings and dividend allowances, tax reducers, the final tax computation, and payments on account. ALWAYS read this skill before touching any UK income tax return work.
version: 2.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Income Tax (SA100) -- Individual Tax Computation Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | United Kingdom |
| Tax | Income Tax (rUK rates or Scottish rates) |
| Currency | GBP only |
| Tax year | 6 April 2024 -- 5 April 2025 |
| Primary legislation | Income Tax Act 2007 (ITA 2007); ITEPA 2003; ITTOIA 2005 |
| Supporting legislation | Finance Act 2024; Finance Act 2025; Scotland Act 2016; TMA 1970 |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January 2026 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- UK-qualified accountant (ACA/ACCA/CTA) |
| Skill version | 2.0 |

### Income Tax Bands -- England, Wales, Northern Ireland (rUK) [T1]

| Band | Taxable Income | Rate |
|---|---|---|
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Basic rate | GBP 12,571 -- 50,270 | 20% |
| Higher rate | GBP 50,271 -- 125,140 | 40% |
| Additional rate | Over GBP 125,140 | 45% |

### Scottish Income Tax Bands (2024/25) [T1]

| Band | Taxable Income | Rate |
|---|---|---|
| Personal allowance | GBP 0 -- 12,570 | 0% |
| Starter rate | GBP 12,571 -- 14,876 | 19% |
| Basic rate | GBP 14,877 -- 26,561 | 20% |
| Intermediate rate | GBP 26,562 -- 43,662 | 21% |
| Higher rate | GBP 43,663 -- 75,000 | 42% |
| Advanced rate | GBP 75,001 -- 125,140 | 45% |
| Top rate | Over GBP 125,140 | 48% |

Scottish rates apply ONLY to non-savings, non-dividend income. Savings and dividends always use UK-wide rates.

### Key Allowances and Thresholds [T1]

| Item | Amount |
|---|---|
| Personal allowance | GBP 12,570 |
| PA taper threshold | GBP 100,000 adjusted net income |
| PA fully withdrawn | GBP 125,140 |
| Basic rate band | GBP 37,700 |
| Personal savings allowance (basic rate) | GBP 1,000 |
| Personal savings allowance (higher rate) | GBP 500 |
| Personal savings allowance (additional rate) | GBP 0 |
| Starting rate for savings band | GBP 5,000 (reduced by non-savings income above PA) |
| Dividend allowance | GBP 500 |
| Marriage allowance transfer | GBP 1,260 (tax reducer GBP 252) |
| Annual pension allowance | GBP 60,000 |

### Dividend Rates [T1]

| Band | Rate |
|---|---|
| Within basic rate band | 8.75% |
| Within higher rate band | 33.75% |
| Within additional rate band | 39.35% |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Unknown residency | UK resident (but STOP if genuinely unclear) |
| Unknown Scottish status | rUK rates |
| Unknown income category | Non-savings income |
| Unknown pension contribution method | Relief at source |
| Unknown marriage allowance eligibility | Do not apply |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- P60 (employment income), self-employment profit from SA103, and confirmation of residency status and Scottish taxpayer status.

**Recommended** -- P11D (benefits in kind), bank interest certificates, dividend vouchers, pension contribution statements, Gift Aid records, prior year SA302 (tax calculation).

**Ideal** -- all supplementary pages (SA103, SA105, SA106), complete records of all income sources, prior year payments on account made.

### Refusal Catalogue

**R-UK-IT-1 -- Non-resident or split-year treatment.** "Non-resident and split-year cases have different rules and may involve the remittance basis. Out of scope. Escalate."

**R-UK-IT-2 -- Non-domiciled individuals.** "The remittance basis for non-doms requires specialist advice. Out of scope."

**R-UK-IT-3 -- Trust income.** "Income from trusts (SA107) has specific rules. Out of scope."

**R-UK-IT-4 -- Complex pension annual allowance.** "Tapered annual allowance, money purchase annual allowance, and carry-forward calculations beyond basic require specialist review. Escalate."

**R-UK-IT-5 -- Capital gains.** "Capital gains are computed separately on SA108. This skill covers income tax only."

---

## Section 3 -- Transaction Pattern Library

For SA100, the "transactions" are not bank statement lines but rather income items from various sources flowing into the tax computation. This pattern library maps income types to the correct SA100 section and tax treatment.

### 3.1 Employment Income Patterns

| Source Document | SA100 Section | Treatment | Notes |
|---|---|---|---|
| P60 (annual certificate) | TR3 (Employment) | Gross pay before PAYE deducted | PAYE tax goes to "tax deducted" |
| P45 (leaver certificate) | TR3 | Gross pay for period employed | May need to combine with P60 from new employer |
| P11D (benefits in kind) | TR3 | Add to employment income | Car benefit, medical insurance, etc. |
| Tips, bonuses (not on P60) | TR3 | Add to employment income | Must be declared even if not on P60 |
| Redundancy payment | TR3 | First GBP 30,000 exempt. Excess taxable. | [T2] Confirm composition of payment |
| Employer pension contribution | EXCLUDE | Not taxable income to employee | Employer contribution does not appear on SA100 |

### 3.2 Self-Employment Income Patterns

| Source | SA100 Section | Treatment | Notes |
|---|---|---|---|
| SA103 taxable trading profit | TR4 (Self-employment) | Attach SA103 | Computed per uk-self-employment-sa103 skill |
| Multiple self-employments | TR4 | Separate SA103 for each trade | Combined for Class 4 NIC |

### 3.3 Savings Income Patterns

| Source | SA100 Section | Treatment | Notes |
|---|---|---|---|
| Bank interest (UK) | TR5 (Savings) | Gross amount | Most banks pay interest gross since 2016 |
| Building society interest | TR5 | Gross amount | Same |
| Government bond interest (gilts) | TR5 | Gross amount | Savings income |
| NS&I interest (non-ISA) | TR5 | Gross amount | Premium Bond prizes are tax-free |
| ISA interest | EXCLUDE | Tax-free | Do not include |
| P2P lending interest | TR5 | Gross amount | Savings income |

### 3.4 Dividend Income Patterns

| Source | SA100 Section | Treatment | Notes |
|---|---|---|---|
| UK company dividends | TR6 (Dividends) | Gross dividend | No tax credit since 2016 |
| Overseas dividends | TR6 or SA106 | Gross amount in GBP | May have foreign tax credit |
| Investment fund dividends | TR6 | As per tax voucher | Some funds pay interest distributions |
| Scrip dividends | TR6 | Cash equivalent | Taxable as dividend |

### 3.5 Pension Income Patterns

| Source | SA100 Section | Treatment | Notes |
|---|---|---|---|
| State pension | TR5 (Pensions) | Full amount taxable | No tax deducted at source |
| Private/occupational pension | TR5 | Gross amount | PAYE usually deducted |
| Pension lump sum (25% tax-free) | Partly TR5 | Only 75% taxable | First 25% is tax-free |
| Drawdown income | TR5 | Full amount taxable | No tax-free element (25% already taken) |

### 3.6 Pension Contribution Patterns (Deductions)

| Source | Treatment | Notes |
|---|---|---|
| Personal pension (relief at source) | Gross up: contribution x 100/80. Extends basic rate band. Higher/additional relief via SA100. | Net contribution already includes 20% basic rate relief claimed by pension provider. |
| Workplace pension (net pay) | Already deducted from gross pay. No further claim. | Already reflected in P60 gross figure. |
| SIPP contribution | Same as relief at source | Gross up for higher rate relief. |

### 3.7 Other Income Patterns

| Source | SA100 Section | Treatment | Notes |
|---|---|---|---|
| Rental income (net) | TR6 (Property) | Attach SA105 | Separate computation |
| Foreign income | SA106 | Separate computation | May involve double tax relief |
| Miscellaneous income | SA101 | Various | Catch-all |

---

## Section 4 -- Worked Examples

### Example 1 -- Basic Rate Taxpayer (Employment Only)

**Input:** Employment GBP 35,000. PAYE deducted GBP 4,486. No other income.

**Computation:**
- Personal allowance: GBP 12,570
- Taxable income: 35,000 - 12,570 = GBP 22,430
- Tax: 22,430 x 20% = GBP 4,486
- Less PAYE: GBP 4,486
- Balance: GBP 0

### Example 2 -- Employment + Self-Employment + Dividends

**Input:** Employment GBP 40,000 (PAYE GBP 5,486). Self-employment profit GBP 20,000. Dividends GBP 5,000.

**Computation:**
- Total income: GBP 65,000
- Personal allowance: GBP 12,570
- Taxable: GBP 52,430
- Non-savings (GBP 60,000 - 12,570 = GBP 47,430): 37,700 x 20% = GBP 7,540. Remaining 9,730 x 40% = GBP 3,892.
- Dividends (GBP 5,000 -- all in higher rate band): 500 at 0% (dividend allowance) + 4,500 x 33.75% = GBP 1,518.75
- Total tax: 7,540 + 3,892 + 1,518.75 = GBP 12,950.75
- Less PAYE: GBP 5,486
- Balance via SA: GBP 7,464.75
- Class 4 NIC on self-employment: (20,000 - 12,570 would be wrong -- combined profits) -- Class 4 on GBP 20,000 SE profit: min(20,000, 50,270-already used) x 6% -- see SA103 skill for precise calc.

### Example 3 -- Personal Allowance Taper

**Input:** Total income GBP 115,000. GBP 10,000 gross pension contribution (relief at source).

**Computation:**
- Adjusted net income: 115,000 - 10,000 = GBP 105,000
- PA reduction: (105,000 - 100,000) / 2 = GBP 2,500
- Personal allowance: 12,570 - 2,500 = GBP 10,070
- Basic rate band extended by pension: 37,700 + 10,000 = GBP 47,700
- Higher rate threshold: 10,070 + 47,700 = GBP 57,770

### Example 4 -- Scottish Taxpayer with Savings

**Input:** Scottish taxpayer. Employment GBP 50,000. Bank interest GBP 3,000.

**Computation:**
- Non-savings (Scottish rates): 50,000 - 12,570 = GBP 37,430 taxable
  - Starter (2,306): 19% = GBP 438.14
  - Basic (11,685): 20% = GBP 2,337.00
  - Intermediate (17,101 -- up to 43,662-12,570=31,092): 21% = GBP 3,591.21
  - Higher (37,430 - 31,092 = 6,338): 42% = GBP 2,661.96
- Savings (UK rates): GBP 3,000 -- taxpayer is higher rate
  - PSA: GBP 500 at 0%
  - Remaining: GBP 2,500 at 40% = GBP 1,000
- Total: 9,028.31 + 1,000 = GBP 10,028.31

### Example 5 -- Marriage Allowance

**Input:** Spouse A income GBP 10,000. Spouse B income GBP 28,000 (basic rate). Election made.

**Computation:**
- Spouse A: PA reduced to GBP 11,310. Income GBP 10,000 < GBP 11,310. Tax = GBP 0.
- Spouse B: Tax = (28,000 - 12,570) x 20% = GBP 3,086. Less marriage allowance reducer GBP 252. Tax = GBP 2,834.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Income Ordering [T1]

**Legislation:** ITA 2007, ss 6-22

Mandatory order: (1) Non-savings income fills bands first. (2) Savings income next. (3) Dividends on top. This ordering is required by law and affects which rates apply.

### 5.2 Personal Allowance [T1]

GBP 12,570. Tapers at GBP 1 for every GBP 2 above GBP 100,000 adjusted net income. Fully withdrawn at GBP 125,140. Effective 60% marginal rate in taper zone.

Adjusted net income = Total income - gross pension contributions - grossed-up Gift Aid.

### 5.3 Savings Allowance and Starting Rate [T1]

Personal savings allowance: GBP 1,000 (basic rate), GBP 500 (higher rate), GBP 0 (additional rate). Starting rate for savings: GBP 5,000 at 0%, reduced by GBP 1 for each GBP 1 of non-savings income above PA.

### 5.4 Dividend Allowance [T1]

GBP 500 at 0% rate. Uses up the basic rate band -- it is NOT a deduction from income. Dividends above the allowance: 8.75% / 33.75% / 39.35%.

### 5.5 Marriage Allowance [T1]

Transfer GBP 1,260 from spouse with income below PA to basic-rate spouse. Reducer = GBP 252 (always at 20%, even for Scottish taxpayers). Recipient must NOT be higher/additional rate.

### 5.6 Basic Rate Band Extension [T1]

Extended by: gross pension contributions (relief at source) + grossed-up Gift Aid donations. Example: GBP 4,000 gross pension = basic rate band becomes GBP 41,700.

### 5.7 Payments on Account [T1]

Required if prior year SA liability > GBP 1,000 AND less than 80% deducted at source. POA1: 31 January (50% of prior year). POA2: 31 July (50%). Balance: 31 January following year.

### 5.8 Filing and Penalties [T1]

Online deadline: 31 January following tax year. Late filing: GBP 100 immediate, then GBP 10/day after 3 months, then 5% of tax at 6 and 12 months. Late payment: 5% at 30 days, 6 months, 12 months.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Personal Allowance Taper Planning [T2]

Pension contributions and Gift Aid can reduce adjusted net income below GBP 100,000 to restore the PA. Legitimate planning strategy. Flag for reviewer to confirm contribution amounts are within annual allowance.

### 6.2 High Income Child Benefit Charge [T2]

Applies where adjusted net income exceeds GBP 60,000 (from 2024/25). Charge = 1% of child benefit for every GBP 200 of income between GBP 60,000 and GBP 80,000. At GBP 80,000+: 100% clawback. Flag for reviewer to confirm benefit amounts.

### 6.3 Reducing Payments on Account [T2]

Client can apply (SA303) to reduce POAs if they expect lower liability. If estimate is too low, HMRC charges interest from original due date. Flag before reducing.

### 6.4 Pension Annual Allowance [T2]

GBP 60,000 standard. Tapers to GBP 10,000 for adjusted income over GBP 260,000. 3-year carry forward of unused allowance available. Excess triggers annual allowance charge at marginal rate. Flag for specialist review if near limits.

### 6.5 Multiple Income Sources Band Allocation [T2]

When savings and dividends push income across rate band boundaries, the interaction of PSA, dividend allowance, and band extensions can be complex. Flag for reviewer to verify computation.

---

## Section 7 -- Excel Working Paper Template

```
SA100 TAX COMPUTATION -- Tax Year 2024/25

A. INCOME
  A1. Employment income (P60 gross)                ___________
  A2. Benefits in kind (P11D)                      ___________
  A3. Self-employment profit (from SA103)          ___________
  A4. Savings income (bank interest)               ___________
  A5. Dividend income                              ___________
  A6. Pension income                               ___________
  A7. Property income (from SA105)                 ___________
  A8. Other income                                 ___________
  A9. TOTAL INCOME                                 ___________

B. DEDUCTIONS FROM TOTAL INCOME
  B1. Trading losses (sideways relief)             ___________
  B2. Gross pension contributions (for ANI)        ___________
  B3. Gift Aid (grossed up, for ANI)               ___________
  B4. Adjusted net income                          ___________

C. PERSONAL ALLOWANCE
  C1. Standard PA                                  12,570
  C2. Taper reduction (if ANI > 100,000)           ___________
  C3. Available PA                                 ___________

D. TAXABLE INCOME
  D1. Non-savings taxable                          ___________
  D2. Savings taxable                              ___________
  D3. Dividend taxable                             ___________
  D4. Total taxable                                ___________

E. TAX COMPUTATION
  E1. Tax on non-savings (rUK or Scottish)         ___________
  E2. Tax on savings (with PSA + starting rate)    ___________
  E3. Tax on dividends (with allowance)            ___________
  E4. Total income tax                             ___________
  E5. Less: tax reducers (MA, EIS, etc.)           ___________
  E6. Income tax charged                           ___________
  E7. Less: PAYE deducted                          ___________
  E8. Less: tax on savings at source               ___________
  E9. Less: payments on account                    ___________
  E10. TAX DUE / (REFUND)                          ___________

F. CLASS 4 NIC (from SA103)                        ___________

G. TOTAL DUE (E10 + F)                             ___________

REVIEWER FLAGS:
  [ ] Scottish or rUK rates confirmed?
  [ ] PA taper checked?
  [ ] Income ordering correct (non-savings > savings > dividends)?
  [ ] Marriage allowance eligibility verified?
  [ ] All T2 items flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

SA100 is primarily compiled from official documents (P60, P11D, interest certificates, dividend vouchers) rather than raw bank statements. However, bank statements may be needed to identify:

| Item | What to Look For |
|---|---|
| Undeclared bank interest | INTEREST PAID lines on personal account |
| Dividends received | DIVIDEND lines, share platform payouts |
| Rental income | Regular credits from tenants |
| Pension income | Monthly credits from pension providers |
| Gift Aid payments | Debits to charities |
| Pension contributions | Debits to SIPP providers |
| Student loan repayments | SLC deductions (informational only -- collected via PAYE) |

---

## Section 9 -- Onboarding Fallback

If the client cannot provide all documents immediately:

1. Start with P60 and any SA103 computation
2. Ask for bank statements to identify savings interest and dividends
3. Apply conservative defaults
4. Generate working paper with flags
5. Present questions:

```
ONBOARDING QUESTIONS -- UK INCOME TAX (SA100)
1. Are you a Scottish taxpayer? (main residence in Scotland)
2. Employment income -- do you have your P60 and P11D?
3. Self-employment -- have you completed your SA103?
4. Bank interest received in the year?
5. Dividends received in the year?
6. Pension income (state and/or private)?
7. Rental income?
8. Pension contributions made (personal, not workplace)?
9. Gift Aid donations made?
10. Married/civil partner -- is marriage allowance being claimed?
11. Payments on account already made for 2024/25?
12. PAYE tax deducted (from P60)?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Income categorisation | ITA 2007, ss 6-22 |
| Personal allowance | ITA 2007, s35 |
| PA taper | ITA 2007, s35(4) |
| Basic rate band | ITA 2007, s10 |
| Savings allowance | ITA 2007, ss 12A-12B |
| Dividend allowance | ITTOIA 2005, s13A |
| Marriage allowance | ITA 2007, s55B |
| Scottish rates | Scotland Act 2016 |
| Pension relief | FA 2004, ss 188-195 |
| Gift Aid | ITA 2007, s414 |
| Payments on account | TMA 1970, ss 59A-59B |
| Filing/penalties | TMA 1970, ss 8-12, 93, 97 |

---

## PROHIBITIONS

- NEVER compute tax without categorising income as non-savings, savings, or dividends
- NEVER apply Scottish rates to savings or dividend income
- NEVER apply marriage allowance if recipient is higher/additional rate
- NEVER ignore PA taper for adjusted net income above GBP 100,000
- NEVER apply PSA to additional rate taxpayers (it is GBP 0)
- NEVER treat dividend allowance as a deduction -- it is a 0% rate band
- NEVER apply starting rate for savings if non-savings income exceeds GBP 17,570
- NEVER compute POAs based on current year -- always prior year SA liability
- NEVER advise on non-domiciled or remittance basis -- escalate
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
