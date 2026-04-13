---
name: ca-fed-t1-return
description: >
  Use this skill whenever asked about a Canadian federal T1 General individual income tax return for a self-employed sole proprietor. Trigger on phrases like "T1 return", "personal tax Canada", "federal tax brackets", "basic personal amount", "CPP self-employed", "CPP2", "self-employment tax Canada", "net income", "taxable income", "federal tax calculation", "non-refundable credits", "instalment payments", or any question about computing federal tax for a self-employed individual in Canada. ALWAYS read this skill before touching any T1 return work.
version: 2.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t2125
---

# Canada T1 General Individual Return -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
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
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

### Federal Tax Brackets (2025)

| Taxable Income (CAD) | Rate | Cumulative Tax |
|---|---|---|
| 0 -- 57,375 | 14.5%* | 8,319 |
| 57,376 -- 114,750 | 20.5% | 20,081 |
| 114,751 -- 177,882 | 26% | 36,495 |
| 177,883 -- 253,414 | 29% | 58,399 |
| 253,415+ | 33% | 58,399+ |

*14.5% is a blended rate for 2025 (15% Jan-Jun, 14% Jul-Dec).

### Basic Personal Amount (2025)

| Net Income | BPA |
|---|---|
| $177,882 or less | $16,129 |
| $177,882 -- $253,414 | Graduated reduction |
| $253,414+ | $14,538 |

### CPP Self-Employed (2025)

| Item | Value |
|---|---|
| CPP rate (both portions) | 11.9% |
| CPP2 rate (both portions) | 8.0% |
| First ceiling (YMPE) | $71,300 |
| Second ceiling (YAMPE) | $81,200 |
| Basic exemption | $3,500 |
| Max CPP contribution | $8,068.20 |
| Max CPP2 contribution | $792.00 |

Half of CPP/CPP2 is deductible (line 22200); half is a non-refundable credit.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown province | STOP -- province required |
| Unknown RRSP room | $0 deduction |
| Unknown EI opt-in | Not opted in |
| Unknown BPA reduction | Apply full clawback formula |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- net self-employment income (from T2125), province of residence on December 31, SIN, date of birth, marital status.

**Recommended** -- other income sources (T4, T5, T3), RRSP deduction, tax instalments paid, prior year NOA.

**Ideal** -- complete T-slip package, full deduction schedule, prior year carryforwards, CPP/EI elections.

### Refusal Catalogue

**R-CA-T1-1 -- Non-residents.** "Non-resident returns have different rules. Out of scope."

**R-CA-T1-2 -- Deceased / bankruptcy returns.** "Require specialist handling. Escalate."

**R-CA-T1-3 -- Trust income allocation.** "Out of scope."

**R-CA-T1-4 -- Provincial tax computation.** "Provincial tax is separate. Use the appropriate provincial skill."

---

## Section 3 -- Transaction Pattern Library

The T1 skill consumes outputs from the T2125 skill (net business income) and T-slips. Transaction pattern classification is in the `ca-fed-t2125` skill. This skill assembles the return from those inputs.

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Self-Employed

**Input:** Net business income $85,000. RRSP $10,000. No other income. No EI. Ontario.

**Computation:**
- Total income: $85,000
- CPP: max $8,068.20. CPP2: max $792.00. Total: $8,860.20
- CPP employer-half deduction: $4,430.10
- Net income: $85,000 - $10,000 - $4,430.10 = $70,569.90
- Taxable income: $70,569.90
- Federal tax: $57,375 x 14.5% + $13,194.90 x 20.5% = $8,319.38 + $2,704.95 = $11,024.33
- BPA credit: $16,129 x 14.5% = $2,338.71
- CPP employee-half credit: $4,430.10 x 14.5% = $642.36
- Basic federal tax: $11,024.33 - $2,981.07 = $8,043.26
- Plus CPP payable: $8,860.20
- Total before provincial: $16,903.46

### Example 2 -- Low Income, Below BPA

**Input:** Net business income $14,000. No RRSP.

**Computation:**
- CPP: ($14,000 - $3,500) x 11.9% = $1,249.50
- Net income: $14,000 - $624.75 = $13,375.25
- Federal tax: $13,375.25 x 14.5% = $1,939.41
- Credits exceed tax: federal tax = $0
- CPP payable: $1,249.50

### Example 3 -- High Income, Top Bracket

**Input:** Net business income $300,000. RRSP $32,490 (max).

**Computation:**
- CPP + CPP2: $8,860.20. Employer-half: $4,430.10
- Net income: $300,000 - $32,490 - $4,430.10 = $263,079.90
- Federal tax through brackets: $61,588.75
- BPA: $14,538 (reduced for high income). Credit: $2,108.01
- CPP credit: $642.36
- Basic federal tax: $58,838.38

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 T1 Income Flow

Total income (line 15000) -> Net income (line 23600, after deductions including CPP employer-half) -> Taxable income (line 26000) -> Federal tax (Schedule 1).

### 5.2 CPP Self-Employed Computation

On Schedule 8. If earnings < $3,500: no CPP. If $3,500-$71,300: (earnings - $3,500) x 11.9%. If > $71,300: max $8,068.20. CPP2: earnings $71,300-$81,200 at 8.0%. Half deducted, half credited.

### 5.3 EI Self-Employed (Voluntary)

Rate $1.64/$100, max $1,077.48 (Quebec: $1.30). Covers special benefits only (maternity, parental, sickness). 12-month waiting period. Non-refundable credit at 14.5%.

### 5.4 Filing Deadlines

Self-employed filing: June 15. Payment due: April 30 (interest from May 1). Late filing: 5% + 1%/month (max 12). Repeat offender: 10% + 2%/month (max 20).

### 5.5 Instalment Requirements

Required if net tax owing > $3,000 in current year AND either of two prior years. Due: March 15, June 15, September 15, December 15.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Multiple Income Sources

CPP on self-employment must account for CPP already paid through employment. Schedule 8 integrates. Flag if both T4 and T2125 income.

### 6.2 BPA Reduction for High Earners

BPA = $16,129 - $1,591 x (net income - $177,882) / $75,532. Flag if net income between $177,882 and $253,414.

### 6.3 Medical Expenses and Charitable Donations

Medical: amounts > lesser of 3% of net income or $2,759. Charitable: 15% on first $200 + 29%/33% on excess. Flag for reviewer.

---

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
  B2. CPP employer-half (line 22200)               ___________
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

---

## Section 8 -- Bank Statement Reading Guide

The T1 skill does not directly process bank statements. Bank statement classification is handled by the `ca-fed-t2125` skill. T1 consumes the net business income from T2125.

---

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

---

## Section 10 -- Reference Material

| Topic | Reference |
|---|---|
| Tax brackets | ITA s. 117(2) |
| BPA | ITA s. 118(1)(c) |
| CPP self-employed | CPP Act s. 10 |
| CPP2 | CPP Act amendments 2024 |
| EI self-employed | Employment Insurance Act, Part VII.1 |
| Filing deadlines | ITA s. 150(1)(d) |
| Instalments | ITA s. 156(1) |
| Non-refundable credits | ITA s. 118-118.95 |
| Canada employment amount | ITA s. 118(10) -- NOT for self-employed |

---

## PROHIBITIONS

- NEVER apply tax brackets without first computing net income and taxable income
- NEVER forget the CPP employer-half deduction from net income
- NEVER apply the Canada employment amount to self-employment income
- NEVER treat EI as mandatory for self-employed
- NEVER compute provincial tax in this skill
- NEVER assume BPA is always $16,129 -- it reduces for high earners
- NEVER allow home office expenses to create a business loss
- NEVER omit CPP2 for earnings above YMPE
- NEVER forget payment deadline is April 30 even though filing is June 15
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
