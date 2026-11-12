---
name: ca-fed-t1-return
description: Use this skill whenever asked about a Canadian federal T1 General individual income tax return for a self-employed sole proprietor. Trigger on phrases like "T1 return", "personal tax Canada", "federal tax brackets", "basic personal amount", "CPP self-employed", "CPP2", "self-employment tax Canada", "net income", "taxable income", "federal tax calculation", "non-refundable credits", "instalment payments", or any question about computing federal tax for a self-employed individual in Canada. ALWAYS read this skill before touching any T1 return work.
version: 2.1
jurisdiction: CA
tax_year: 2025
last_updated: 2026-11-08
source_checked: 2026-10-17
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# CA Fed T1 Return

## Canada T1 General Individual Return -- Self-Employed Skill v2.1

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### T1 Return

- **$0–$57,375 (2025)** — 14.5% (blended: 15% Jan-Jun, 14% Jul-Dec)  _(https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/reducing-remuneration-subject-income-tax.html)_
- **$57,375.01–$114,750 (2025)** — 20.5% (2026: $58,523.01–$117,045)  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)_
- **$114,751–$177,882 (2025)** — 26%  _(https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/reducing-remuneration-subject-income-tax.html)_
- **$177,883–$253,414 (2025)** — 29%  _(https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/reducing-remuneration-subject-income-tax.html)_
- **$253,415+ (2025)** — 33%  _(https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/reducing-remuneration-subject-income-tax.html)_
- **BPA (2025) — net income ≤$177,882** — $16,129  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html)_
- **BPA (2025) — net income ≥$253,414** — $14,538  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html)_
- **BPA reduction formula (2025)** — $16,129 − $1,591 × (NI − $177,882) / $75,532  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf)_
- **CPP rate (both portions, 2025)** — 11.9%  _(CRA — CPP contribution rates — canada.ca; Canada Pension Plan Act s.10)_
- **CPP2 rate (both portions, 2025)** — 8.0%
- **First ceiling (YMPE, 2025)** — $71,300  _(CRA — CPP contribution rates, maximums and exemptions — canada.ca)_
- **Second ceiling (YAMPE, 2025)** — $81,200  _(CRA — CPP contribution rates, maximums and exemptions — canada.ca)_
- **Basic exemption (2025)** — $3,500  _(Canada Pension Plan Act s.20; CRA — Schedule 8)_
- **Max CPP contribution (2025)** — $8,068.20
- **Max QPP2 contribution (2025)** — $792.00
- **CPP deductible portion** — 50% of base contributions plus all first and second additional contributions (line 22200); the other 50% of base contributions is the line 31000 credit  _([ITA s.60(e); CRA — Line 22200](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf))_
- **EI rate (2025)** — $1.64/$100  _(CRA — EI premium rates and maximums — canada.ca; Employment Insurance Act Part VII.1)_
- **Max EI premium (2025)** — $1,077.48  _(CRA — EI premium rates and maximums — canada.ca)_
- **Quebec EI rate (2025)** — $1.31/$100  _([CRA — EI premium rates and maximums — canada.ca](https://www.canada.ca/en/employment-social-development/news/2024/09/canada-employment-insurance-commission-confirms-2025-employment-insurance-premium-rate.html))_
- **Waiting period** — 12 months  _(Employment Insurance Act s.152.07; CRA — Self-employed EI — canada.ca)_
- **Self-employed filing** — June 15  _(ITA s.150(1)(d))_
- **Payment due** — April 30 (interest from May 1)  _(ITA s.156.1(1); CRA — Paying income tax — canada.ca)_
- **Late filing penalty** — 5% + 1%/month (max 12)  _(ITA s.162(1))_
- **Repeat offender penalty** — 10% + 2%/month (max 20)  _(ITA s.162(2))_
- **Net tax owing threshold** — > $3,000 in the current year AND either of the two prior years ($1,800 for Quebec residents)  _(ITA s.156(1); CRA — Instalments for individuals — canada.ca)_
- **Canada employment amount (line 31260)** — $1,471 (2025); $1,501 (2026). Employment income only; not for the self-employed  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html; https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)_
- **Eligible dividends (2025 and 2026)** — gross-up 38%; federal dividend tax credit 15.0198% of the grossed-up (taxable) amount  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12000-taxable-amount-dividends-eligible-other-than-eligible-taxable-canadian-corporations.html; https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4015/t5-guide-return-investment-income.html)_
- **Other than eligible dividends (2025 and 2026)** — gross-up 15%; federal dividend tax credit 9.0301% of the grossed-up (taxable) amount  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12000-taxable-amount-dividends-eligible-other-than-eligible-taxable-canadian-corporations.html; https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4015/t5-guide-return-investment-income.html)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada -- Federal |
| Tax | Federal income tax + CPP/CPP2 self-employed |
| Currency | CAD only |
| Tax year | Calendar year |
| Primary legislation | Income Tax Act (ITA), R.S.C. 1985, c. 1 (5th Supp.) |
| Supporting legislation | Canada Pension Plan Act; Employment Insurance Act |
| Tax authority | Canada Revenue Agency (CRA) |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Form | T1 General + Schedule 1 (Federal Tax) + Schedule 8 (CPP) |
| Filing deadline | June 15 (self-employed); payment due April 30 |
| Contributor | Open Accountants Community |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |
| Skill version | 2.1 |

### Federal Tax Brackets (2025)

**Federal Tax Brackets (2025)**

| Taxable Income (CAD) | Rate | Cumulative Tax |
| --- | --- | --- |
| 0 -- 57,375 | 14.5%* | 8,319 |
| 57,376 -- 114,750 | 20.5% | 20,081 |
| 114,751 -- 177,882 | 26% | 36,495 |
| 177,883 -- 253,414 | 29% | 58,399 |
| 253,415+ | 33% | 58,399+ |

*14.5% is a blended rate for 2025 (15% Jan-Jun, 14% Jul-Dec).

### Basic Personal Amount (2025)

**Basic Personal Amount (2025)**

| Net Income | BPA |
| --- | --- |
| $177,882 or less | $16,129 |
| $177,882 -- $253,414 | Graduated reduction |
| $253,414+ | $14,538 |

### CPP Self-Employed (2025)

**CPP Self-Employed (2025)**

| Item | Value |
| --- | --- |
| CPP rate (both portions) | 11.9% |
| CPP2 rate (both portions) | 8.0% |
| First ceiling (YMPE) | $71,300 |
| Second ceiling (YAMPE) | $81,200 |
| Basic exemption | $3,500 |
| Max CPP contribution | $8,068.20 |
| Max CPP2 contribution | $792.00 |

Half of base CPP plus all first and second additional (CPP2) contributions are deductible (line 22200); the other half of base CPP is a non-refundable credit (line 31000).

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown province | STOP -- province required |
| Unknown RRSP room | $0 deduction |
| Unknown EI opt-in | Not opted in |
| Unknown BPA reduction | Apply full clawback formula |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- net self-employment income (from T2125), province of residence on December 31, SIN, date of birth, marital status.

**Recommended** -- other income sources (T4, T5, T3), RRSP deduction, tax instalments paid, prior year NOA.

**Ideal** -- complete T-slip package, full deduction schedule, prior year carryforwards, CPP/EI elections.

### Refusal Catalogue

- **R-CA-T1-1 -- Non-residents** — Non-resident returns have different rules. Out of scope.
- **R-CA-T1-2 -- Deceased / bankruptcy returns** — Require specialist handling. Escalate.
- **R-CA-T1-3 -- Trust income allocation** — Out of scope.
- **R-CA-T1-4 -- Provincial tax computation** — Provincial tax is separate. Use the appropriate provincial skill.

## Section 3 -- Transaction Pattern Library

The T1 skill consumes outputs from the T2125 skill (net business income) and T-slips. Transaction pattern classification is in the `ca-fed-t2125` skill. This skill assembles the return from those inputs.

## Section 4 -- Worked Examples

### Example 1 -- Standard Self-Employed

**Input:** Net business income $85,000. RRSP $10,000. No other income. No EI. Ontario.

**Computation:**
- Total income: $85,000
- CPP: max $8,068.20. CPP2: max $792.00. Total: $8,860.20
- CPP deduction (line 22200): half of base CPP $3,356.10 + first additional $1,356.00 + CPP2 $792.00 = $5,504.10
- Net income: $85,000 - $10,000 - $5,504.10 = $69,495.90
- Taxable income: $69,495.90
- Federal tax: $57,375 x 14.5% + $12,120.90 x 20.5% = $8,319.38 + $2,484.78 = $10,804.16
- BPA credit: $16,129 x 14.5% = $2,338.71
- CPP credit (line 31000, half of base CPP): $3,356.10 x 14.5% = $486.63
- Basic federal tax: $10,804.16 - $2,825.34 = $7,978.82
- Plus CPP payable: $8,860.20
- Total before provincial: $16,839.02

### Example 2 -- Low Income, Below BPA

**Input:** Net business income $14,000. No RRSP.

**Computation:**
- CPP: ($14,000 - $3,500) x 11.9% = $1,249.50
- CPP deduction (line 22200): half of base CPP $519.75 + first additional $210.00 = $729.75
- Net income: $14,000 - $729.75 = $13,270.25
- Federal tax: $13,270.25 x 14.5% = $1,924.19
- Credits exceed tax: federal tax = $0
- CPP payable: $1,249.50

### Example 3 -- High Income, Top Bracket

**Input:** Net business income $300,000. RRSP $32,490 (max).

**Computation:**
- CPP + CPP2: $8,860.20. CPP deduction (line 22200): $5,504.10
- Net income: $300,000 - $32,490 - $5,504.10 = $262,005.90
- Federal tax through brackets: $58,399.85 (tax on the first $253,414) + $8,591.90 x 33% ($2,835.33) = $61,235.18
- BPA: $14,538 (reduced for high income). Credit: $2,108.01
- CPP credit: $3,356.10 x 14.5% = $486.63
- Basic federal tax: $61,235.18 - $2,108.01 - $486.63 = $58,640.54

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 T1 Income Flow

- **T1 Income Flow** — Total income (line 15000) -> Net income (line 23600, after deductions including the line 22200 CPP deduction: half of base CPP plus all first and second additional contributions) -> Taxable income (line 26000) -> Federal tax (Schedule 1).

### 5.2 CPP Self-Employed Computation

- **CPP Self-Employed Computation** — On Schedule 8. If earnings < $3,500: no CPP. If $3,500-$71,300: (earnings - $3,500) x 11.9%. If > $71,300: max $8,068.20. CPP2: earnings $71,300-$81,200 at 8.0%. Half of base CPP is credited (line 31000); the other half of base CPP plus all first and second additional contributions is deducted (line 22200).  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf)_

### 5.3 EI Self-Employed (Voluntary)

- **EI Self-Employed (Voluntary)** — Rate $1.64/$100, max $1,077.48 (Quebec: $1.31). Covers special benefits only (maternity, parental, sickness). 12-month waiting period. Non-refundable credit at 14.5%.  _(https://www.canada.ca/en/employment-social-development/news/2024/09/canada-employment-insurance-commission-confirms-2025-employment-insurance-premium-rate.html)_

### 5.4 Filing Deadlines

- **Filing Deadlines** — Self-employed filing: June 15. Payment due: April 30 (interest from May 1). Late filing: 5% + 1%/month (max 12). Repeat offender: 10% + 2%/month (max 20).

### 5.5 Instalment Requirements

- **Instalment Requirements** — Required if net tax owing > $3,000 ($1,800 for Quebec residents) in the current year AND either of the two prior years. Due: March 15, June 15, September 15, December 15.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Multiple Income Sources

- **Multiple Income Sources** — CPP on self-employment must account for CPP already paid through employment. Schedule 8 integrates. Flag if both T4 and T2125 income.

### 6.2 BPA Reduction for High Earners

- **BPA Reduction for High Earners** — BPA = $16,129 - $1,591 x (net income - $177,882) / $75,532. Flag if net income between $177,882 and $253,414.

### 6.3 Medical Expenses and Charitable Donations

- **Medical Expenses and Charitable Donations** — Medical: amounts > lesser of 3% of net income or $2,834. Charitable: 14.5% on first $200 + 29%/33% on excess. Flag for reviewer.  _(https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf)_

## Section 7 -- Excel Working Paper Template

```
CANADA T1 -- Working Paper (2025)

A. TOTAL INCOME
  A1. Self-employment (T2125 line 13500)          ___________
  A2. Employment (T4)                              ___________
  A3. Interest / dividends                         ___________
  A4. Other income                                 ___________
  A5. Total income (line 15000)                    ___________

B. NET INCOME
  B1. RRSP deduction                               ___________
  B2. CPP deduction (line 22200)                   ___________
  B3. Other deductions                             ___________
  B4. Net income (line 23600)                      ___________

C. TAXABLE INCOME
  C1. Loss carryovers                              ___________
  C2. Taxable income (line 26000)                  ___________

D. FEDERAL TAX
  D1. Tax on taxable income                        ___________
  D2. Non-refundable credits (x 14.5%)             ___________
  D3. Basic federal tax                            ___________
  D4. CPP payable (Schedule 8)                     ___________
  D5. EI payable (if opted in)                     ___________
  D6. Provincial tax (separate skill)              ___________
  D7. Total payable                                ___________
  D8. Less: instalments and withholding            ___________
  D9. Balance owing / (refund)                     ___________

REVIEWER FLAGS:
  [ ] Province confirmed?
  [ ] CPP/CPP2 computed on Schedule 8?
  [ ] BPA reduction applied if high income?
  [ ] Instalment interest checked?
  [ ] Payment deadline April 30 noted?
```

## Section 8 -- Bank Statement Reading Guide

The T1 skill does not directly process bank statements. Bank statement classification is handled by the `ca-fed-t2125` skill. T1 consumes the net business income from T2125.

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- CANADA T1
1. Full legal name and SIN?
2. Date of birth?
3. Marital status as of December 31?
4. Province of residence on December 31?
5. Net self-employment income (from T2125)?
6. Other income sources (T4, investments, rental)?
7. RRSP deduction amount?
8. Tax instalments paid during the year?
9. Tax withheld at source (T4 slips)?
10. Opted into EI special benefits?
11. Prior year Notice of Assessment available?
12. CPP/QPP already paid through employment?
```

## Section 10 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Tax brackets | ITA s. 117(2) |
| BPA | ITA s. 118(1)(c) |
| CPP self-employed | CPP Act s. 10 |
| CPP2 | CPP Act amendments 2024 |
| EI self-employed | Employment Insurance Act, Part VII.1 |
| Filing deadlines | ITA s. 150(1)(d) |
| Instalments | ITA s. 156(1) |
| Non-refundable credits | ITA s. 118-118.95 |
| Canada employment amount | ITA s. 118(10) -- NOT for self-employed |

## PROHIBITIONS

- NEVER apply tax brackets without first computing net income and taxable income
- NEVER forget the line 22200 CPP deduction from net income (half of base CPP plus all first and second additional contributions)
- NEVER apply the Canada employment amount to self-employment income
- NEVER treat EI as mandatory for self-employed
- NEVER compute provincial tax in this skill
- NEVER assume BPA is always $16,129 -- it reduces for high earners
- NEVER allow home office expenses to create a business loss
- NEVER omit CPP2 for earnings above YMPE
- NEVER forget payment deadline is April 30 even though filing is June 15
- NEVER present calculations as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner) before filing or acting upon.
