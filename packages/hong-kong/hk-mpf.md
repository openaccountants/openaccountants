---
name: hk-mpf
description: Use this skill whenever asked about Hong Kong Mandatory Provident Fund (MPF) contributions. Trigger on phrases like "MPF", "Mandatory Provident Fund", "強積金", "employer contribution Hong Kong", "employee contribution HK", "MPF self-employed", "TVC", "voluntary contributions", "MPF cap", "relevant income MPF", "MPFA", or any question about MPF contribution rates, caps, voluntary contributions, tax deductions, and self-employed obligations. ALWAYS read this skill before advising on MPF matters.
version: 1.0
jurisdiction: HK
tax_year: 2024
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - hk-salaries-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HK Mpf

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country / Territory | Hong Kong SAR, China |
| System | Mandatory Provident Fund (MPF / 強制性公積金) |
| Currency | HKD (Hong Kong Dollar) only |
| Governing legislation | Mandatory Provident Fund Schemes Ordinance (MPFSO), Cap. 485 |
| Regulator | Mandatory Provident Fund Schemes Authority (MPFA / 積金局) |
| Portal | mpfa.org.hk |
| Validated by | Pending — requires sign-off by a Hong Kong CPA or MPF intermediary |
| Skill version | 1.0 |

### Core Contribution Parameters (2024/25)

**Core Contribution Parameters (2024/25)**

| Parameter | Amount |
| --- | --- |
| Employer mandatory contribution rate | 5% of relevant income |
| Employee mandatory contribution rate | 5% of relevant income |
| Maximum relevant income | HK$30,000/month |
| Minimum relevant income | HK$7,100/month |
| Maximum mandatory contribution (each party) | HK$1,500/month |
| Minimum mandatory contribution (each party) | HK$355/month (if income ≥$7,100) |
| Self-employed mandatory rate | 5% of relevant income |
| Self-employed max contribution | HK$1,500/month or HK$18,000/year |
| Voluntary contribution (TVC) -- tax deduction cap | HK$60,000/year |

### Who Must Join MPF

**Who Must Join MPF**

| Category | MPF Required | Exceptions |
| --- | --- | --- |
| Employees aged 18--64 | YES | Domestic helpers, self-employed hawkers, statutorily exempt |
| Self-employed aged 18--64 | YES |  |
| Casual employees (<60 days in construction/catering) | YES (Industry Scheme) |  |
| Part-time employees | YES (if employed ≥60 days) |  |
| Employees aged 65+ | NO (can join voluntarily) |  |
| Domestic helpers | NO (exempt) |  |
| Civil servants (pre-2000 terms) | NO (covered by pension) |  |
| ORSO scheme members | Exempt if scheme is MPFSO-exempted |  |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown relevant income | Apply minimum ($7,100 threshold) until confirmed |
| Unknown employment start date | Assume 60-day rule applies (must enrol within 60 days) |
| Self-employed vs employee | Check control test; if ambiguous, treat as employee |
| Unknown fund choice | Employee must be given choice; default = employer's scheme |
| TVC vs employer voluntary | TVC = tax deductible; employer voluntary (SVC) = not deductible to employee |

## Section 2 -- Rules

### 2.1 Mandatory Contributions

**2.1 Mandatory Contributions**

| Party | Rate | On | Monthly Cap | Monthly Floor |
| --- | --- | --- | --- | --- |
| Employer | 5% | Relevant income | HK$1,500 (on $30,000) | No minimum (pays even if income <$7,100) |
| Employee | 5% | Relevant income | HK$1,500 (on $30,000) | HK$0 if income <$7,100 |
| Self-employed | 5% | Relevant income | HK$1,500/month | HK$0 if income <$7,100 |

Important distinctions:
- If employee earns <HK$7,100/month: employer still contributes 5%, but employee contributes 0%
- If employee earns >HK$30,000/month: both capped at HK$1,500/month each
- Relevant income includes: wages, salary, leave pay, fees, commission, bonus, gratuity, perquisites (monetary)

### 2.2 Relevant Income Definition (MPFSO Sec. 2)

- **Relevant Income -- Included** — Wages, salary, overtime pay; Commission, bonus; Leave pay (annual, sick, maternity, paternity); Fees, tips; End-of-year payments, gratuities  _(MPFSO Sec. 2)_
- **Relevant Income -- Excluded** — Severance payment (Employment Ordinance); Long service payment (Employment Ordinance); Housing benefit / housing allowance (non-cash only); Reimbursement of expenses  _(MPFSO Sec. 2)_

### 2.3 Self-Employed Persons

**2.3 Self-Employed Persons**

| Rule | Detail |
| --- | --- |
| Mandatory contribution | 5% of relevant income |
| Relevant income | Net self-employment income (assessable profits for tax) |
| Contribution frequency | Monthly or annually (taxpayer's choice) |
| Monthly basis | 5% of monthly relevant income, max $1,500/month |
| Annual basis | 5% of annual relevant income, max $18,000/year |
| Income below $7,100/month | No mandatory contribution required |
| Deadline (monthly) | Within 30 days after end of contribution period |
| Deadline (annual) | Within 30 days after end of financial year |

### 2.4 Enrolment Requirements

**2.4 Enrolment Requirements**

| Scenario | Deadline |
| --- | --- |
| New employee | Employer must enrol within 60 days of start |
| New self-employed | Must join MPF scheme within 60 days of becoming self-employed |
| Change of employer | New employer re-enrols; employee can consolidate old accounts |
| Casual employees (construction/catering) | Day 1 enrolment via Industry Scheme |

### 2.5 Vesting

**2.5 Vesting**

| Type | Vesting Rule |
| --- | --- |
| Employee mandatory contributions | 100% vested immediately (employee's money) |
| Employer mandatory contributions | 100% vested immediately |
| Employer voluntary contributions | May have vesting schedule (per scheme rules) |
| Employee voluntary contributions | 100% vested immediately |

## Section 3 -- Voluntary Contributions and Tax Deductions

### 3.1 Tax Deductible Voluntary Contributions (TVC)

**3.1 Tax Deductible Voluntary Contributions (TVC)**

| Feature | Detail |
| --- | --- |
| Legislation | IRO Sec. 26J (effective 2019/20 onwards) |
| Who can claim | Any MPF scheme member (employee, self-employed, non-employed) |
| Contribution to | Special TVC account in MPFA-approved scheme |
| Tax deduction limit | HK$60,000 per year |
| Combined cap | TVC + QDAP (qualifying deferred annuity) together capped at HK$60,000 |
| Scheme | Must be designated TVC account (NOT regular voluntary/SVC) |
| Withdrawal | Only at age 65, retirement, permanent departure, or other qualifying events |
| Tax deduction claimed on | BIR60 (Part 8.5) |

### 3.2 Special Voluntary Contributions (SVC) -- Non-Deductible

**3.2 Special Voluntary Contributions (SVC) -- Non-Deductible**

| Feature | Detail |
| --- | --- |
| Employer SVC | Employer contributes extra; may have vesting schedule |
| Employee SVC | Employee contributes extra to existing scheme; NOT tax-deductible |
| Difference from TVC | SVC goes into regular account; TVC goes into special TVC account |
| Withdrawal rules | Per scheme governing rules (may allow earlier withdrawal than TVC) |

### 3.3 Computation of Tax Benefit (TVC)

- **TVC Tax Benefit Computation** — Annual TVC contribution (max $60,000) × Marginal tax rate (2% to 17% progressive, or 15% standard) = Tax saving Example: - TVC contribution: $60,000 - Marginal rate: 17% - Tax saving: $60,000 × 17% = $10,200

## Section 4 -- Computation Examples

### Example 1 -- Standard Employee (Income $25,000/month)

**Example 1 -- Standard Employee (Income $25,000/month)**

| Party | Calculation | Monthly Amount |
| --- | --- | --- |
| Employer | 5% × $25,000 | $1,250 |
| Employee | 5% × $25,000 | $1,250 |
| Total to MPF account |  | $2,500 |

Annual: Employee contributes $15,000 (deductible up to $18,000 cap for salaries tax).

### Example 2 -- High-Income Employee ($80,000/month)

**Example 2 -- High-Income Employee ($80,000/month)**

| Party | Calculation | Monthly Amount |
| --- | --- | --- |
| Employer | 5% × $30,000 (capped) | $1,500 |
| Employee | 5% × $30,000 (capped) | $1,500 |
| Total to MPF account |  | $3,000 |

Annual employee mandatory: $18,000 (fully deductible -- equals cap).

### Example 3 -- Low-Income Employee ($6,000/month)

**Example 3 -- Low-Income Employee ($6,000/month)**

| Party | Calculation | Monthly Amount |
| --- | --- | --- |
| Employer | 5% × $6,000 | $300 |
| Employee | 0% (below $7,100 threshold) | $0 |
| Total to MPF account |  | $300 |

### Example 4 -- Self-Employed (Annual Profit $500,000)

**Example 4 -- Self-Employed (Annual Profit $500,000)**

| Basis | Calculation | Annual Amount |
| --- | --- | --- |
| Monthly equivalent | $500,000 / 12 = $41,667 |  |
| Mandatory (capped) | 5% × $30,000 × 12 | $18,000/year |
| Additional TVC (optional) | Up to $60,000 | Tax-deductible |
| Maximum total |  | $78,000/year |

## Section 5 -- Filing and Administrative

### 5.1 Employer Obligations

**5.1 Employer Obligations**

| Obligation | Deadline |
| --- | --- |
| Enrol new employee | Within 60 days of employment start |
| Pay contributions | Within 10 days after end of contribution period (wage period) |
| Provide pay-record | Monthly to employee showing MPF details |
| Report cessation | Notify trustee of employee termination within 30 days |
| Maintain records | 7 years |

### 5.2 Penalties for Non-Compliance

**5.2 Penalties for Non-Compliance**

| Offence | Penalty |
| --- | --- |
| Failure to enrol employee | Fine up to HK$350,000 + imprisonment up to 3 years |
| Late contribution (employer) | 5% surcharge on outstanding amount |
| Failure to pay contribution | Fine up to HK$350,000 + imprisonment up to 3 years |
| Deducting from employee wages for employer share | Fine up to HK$350,000 + imprisonment up to 3 years |
| Self-employed failure to join | Fine up to HK$50,000 + imprisonment up to 6 months |

### 5.3 Withdrawal Events (Mandatory + TVC)

**5.3 Withdrawal Events (Mandatory + TVC)**

| Event | Requirement |
| --- | --- |
| Retirement (age 65) | Full withdrawal permitted |
| Early retirement (age 60) | Must provide statutory declaration of permanent cessation of employment |
| Permanent departure from HK | Statutory declaration + evidence |
| Total incapacity | Medical evidence |
| Terminal illness | Medical evidence |
| Small balance (account <$5,000) | No contributions for 12 months + statutory declaration |
| Death | Paid to estate/beneficiary |

## Section 6 -- Edge Cases

### 6.1 Multiple Employments

- **Multiple Employments** — Each employer must contribute separately; Employee contributes 5% to each scheme; Combined employee contributions may exceed $18,000/year tax deduction cap; Tax deduction still capped at $18,000 for mandatory across all employments

### 6.2 Employee Becomes Self-Employed

- **Employee Becomes Self-Employed** — Employee account becomes "preserved" on leaving employment; Self-employed opens new self-employed account; May consolidate accounts into one personal account; Previous employer contributions preserved until qualifying event

### 6.3 Part-Time / Multiple Part-Time Jobs

- **Part-Time / Multiple Part-Time Jobs** — Each employer with ≥60 days employment must enrol; Income threshold ($7,100) applies per employment separately; Part-time worker earning $5,000 from employer A and $4,000 from employer B: Employer A: contributes 5% × $5,000 = $250; employee contributes $0 (below threshold); Employer B: contributes 5% × $4,000 = $200; employee contributes $0 (below threshold)

### 6.4 Non-Monetary Benefits

- **Non-Monetary Benefits** — Non-cash benefits (housing, company car) are NOT relevant income for MPF; Only monetary payments count towards MPF calculation; Exception: if benefit is commutable to cash at employee's option, it may be relevant income

### 6.5 MPF Offset Mechanism

**6.5 MPF Offset Mechanism**

| Item | Rule |
| --- | --- |
| Severance payment offset | Employer may offset SP against employer MPF contributions (from accrued benefits derived from employer contributions) |
| Long service payment offset | Same as above |
| Abolition (planned) | Government announced phased abolition from 2025 -- transition period applies |
| Current position (2024/25) | Offset still permitted during transition |

## Section 7 -- MPFA Approved Schemes

**Section 7 -- MPFA Approved Schemes**

| Scheme Type | Description |
| --- | --- |
| Master Trust Scheme | Most common; pooled scheme managed by trustees (e.g., Manulife, AIA, HSBC, Sun Life) |
| Employer-Sponsored Scheme | Set up by single employer for its employees |
| Industry Scheme | For casual employees in construction and catering |

Current approved trustees (major):
- HSBC Provident Fund Trustee
- Manulife (International) Limited
- AIA Company (Trustee)
- Sun Life Trustee Company
- Bank Consortium Trust Company
- BOCI-Prudential Trustee Limited

## Section 8 -- Reference Material

**Section 8 -- Reference Material**

| Topic | Reference |
| --- | --- |
| MPFSO (full ordinance) | Cap. 485, Laws of Hong Kong |
| Contribution rules | MPFSO Sec. 7A, 7C, Schedule 2 |
| Relevant income | MPFSO Sec. 2, Schedule 1 |
| Self-employed | MPFSO Sec. 6C, 7D |
| Tax deduction (TVC) | IRO Sec. 26J |
| Tax deduction (mandatory) | IRO Sec. 12(1)(e) |
| Enrolment | MPFSO Sec. 7, 7A |
| Penalties | MPFSO Sec. 43A, 43B, 43E |
| Withdrawal | MPFSO Schedule 1, Part 1--8 |
| Offset | MPFSO Sec. 12A, Schedule 12 |
| MPFA official site | mpfa.org.hk |
| Fund performance | MPFA Fund Performance Platform |
| Minimum/maximum income | Government Gazette (updated periodically) |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Hong Kong CPA, MPF intermediary, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
