---
name: hk-salaries-tax
description: Use this skill whenever asked about Hong Kong salaries tax. Trigger on phrases like "Hong Kong tax", "salaries tax", "BIR60", "IRD", "net chargeable income", "standard rate", "progressive rate HK", "personal allowance Hong Kong", "provisional tax HK", "tax return Hong Kong", or any question about computing, filing, or planning salaries tax for an individual in Hong Kong. This skill covers progressive and standard rate calculations, allowances, deductions, provisional tax, and BIR60 filing. ALWAYS read this skill before advising on Hong Kong salaries tax.
version: 1.0
jurisdiction: HK
tax_year: 2024
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HK Salaries Tax

## Hong Kong Salaries Tax -- Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country / Territory | Hong Kong SAR, China |
| Tax | Salaries Tax (薪俸稅) |
| Currency | HKD (Hong Kong Dollar) only |
| Year of Assessment | 1 April -- 31 March (2024/25 = 1 Apr 2024 -- 31 Mar 2025) |
| Primary legislation | Inland Revenue Ordinance (IRO), Cap. 112 |
| Tax authority | Inland Revenue Department (IRD) |
| Filing portal | ird.gov.hk / eTAX (etax.ird.gov.hk) |
| Filing deadline | 1 month from BIR60 issue (usually June/July); eTAX: 1 extra month |
| Validated by | Pending — requires sign-off by a Hong Kong CPA or tax representative |
| Skill version | 1.0 |

### Tax Calculation Method

- **Salaries tax method** — Salaries tax is the LOWER of: 1. Progressive rates on Net Chargeable Income (after deductions AND allowances) 2. Standard rate on Net Income (after deductions but BEFORE allowances)

### Progressive Tax Rates (2024/25 onwards)

**Progressive Tax Rates (2024/25 onwards)**

| Net Chargeable Income Band (HK$) | Rate | Tax in Band | Cumulative Tax |
| --- | --- | --- | --- |
| First 50,000 | 2% | 1,000 | 1,000 |
| Next 50,000 | 6% | 3,000 | 4,000 |
| Next 50,000 | 10% | 5,000 | 9,000 |
| Next 50,000 | 14% | 7,000 | 16,000 |
| Remainder | 17% | — | — |

### Standard Rate (2024/25 onwards -- Two-Tiered)

**Standard Rate (2024/25 onwards -- Two-Tiered)**

| Net Income (HK$) | Rate |
| --- | --- |
| First 5,000,000 | 15% |
| Exceeding 5,000,000 | 16% |

### Personal Allowances (2024/25)

**Personal Allowances (2024/25)**

| Allowance | Amount (HK$) |
| --- | --- |
| Basic allowance | 132,000 |
| Married person's allowance | 264,000 |
| Child allowance (each child) | 130,000 |
| Child allowance -- year of birth (additional) | 130,000 |
| Dependent parent/grandparent (aged 60+) | 50,000 |
| Dependent parent/grandparent (aged 60+, living together) | 100,000 |
| Dependent parent/grandparent (aged 55--59) | 25,000 |
| Dependent parent/grandparent (aged 55--59, living together) | 50,000 |
| Dependent brother/sister allowance | 37,500 |
| Single parent allowance | 132,000 |
| Disabled dependant allowance | 75,000 |
| Personal disability allowance | 75,000 |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown marital status | Apply basic allowance (HK$132,000) only |
| Unknown whether children qualify | Do not claim child allowance |
| Unknown dependent parent arrangement | Do not claim additional allowance for living together |
| MPF deduction cap | Apply HK$18,000 cap per employee |
| Unknown whether progressive or standard rate lower | Calculate both; apply lower |
| Tax reduction year | Apply 2024/25 reduction: 100%, ceiling HK$1,500 |

### 2.1 Charge to Salaries Tax (IRO Sec. 8)

- **Charge to salaries tax** — Salaries tax is charged on every person in respect of income arising in or derived from Hong Kong from: Office or employment; Pension; Lump sum payments in connection with services rendered in Hong Kong  _(IRO Sec. 8)_

### 2.2 Assessable Income

**Assessable Income**

| Component | Treatment |
| --- | --- |
| Salary, wages, commission | Fully assessable |
| Bonus (discretionary or contractual) | Fully assessable |
| Leave pay, end-of-contract gratuity | Fully assessable (time-apportioned if partly HK service) |
| Housing benefit (provided by employer) | Add rental value: 10% of net income (4% if hotel, 8% if hostel) |
| Share options/awards | Assessable at exercise/vesting (gain = market value - cost) |
| Employer MPF contributions | NOT assessable (exempt under IRO Sec. 8(1A)) |
| Reimbursed expenses (wholly business) | NOT assessable if solely for business |
| Education benefit for children | Assessable as perquisite |
| Severance / long service payment | Exempt up to statutory entitlement |

### 2.3 Deductions (IRO Sec. 12)

**Deductions (IRO Sec. 12)**  _(IRO Sec. 12)_

| Deduction | Limit (2024/25) |
| --- | --- |
| Self-education expenses | HK$100,000 |
| MPF mandatory contributions (employee) | HK$18,000 |
| Approved charitable donations | 35% of assessable income |
| Elderly residential care expenses | HK$100,000 |
| Home loan interest | HK$100,000 (max 20 years of assessment) |
| Qualifying premiums (VHIS) | HK$8,000 per insured person |
| Qualifying annuity premiums (QDAP) | HK$60,000 |
| MPF voluntary contributions (TVC) | HK$60,000 |
| Domestic rent deduction | HK$100,000 |

- **QDAP + TVC combined cap** — QDAP + TVC deduction combined cap = HK$60,000.  _(IRO Sec. 12)_

### 2.4 Rental Value of Quarters (IRO Sec. 9)

- **Rental value of quarters** — If employer provides housing: Rental value = 10% of net income (after other deductions) for a house/flat; 8% for a service occupancy (hostel); 4% for hotel/boarding house; If employer pays rent (not provides quarters): assessable as Place of Residence benefit, but capped at rent paid or 10% rental value, whichever lower  _(IRO Sec. 9)_

### 3.1 Progressive Rate Calculation

- **Progressive rate calculation worksheet** — A. ASSESSABLE INCOME A1. Salary / wages / commission                      ___________ A2. Bonus / allowances                               ___________ A3. Rental value of quarters (10% of net)            ___________ A4. Share option gains                               ___________ A5. Other perquisites                                ___________ A6. Total Assessable Income                          ___________ B. DEDUCTIONS (Section 12) B1. MPF mandatory contributions (max $18,000)        ___________ B2. Self-education expenses (max $100,000)           ___________ B3. Charitable donations (max 35% of A6)             ___________ B4. Home loan interest (max $100,000)                ___________ B5. QDAP + TVC (combined max $60,000)                ___________ B6. VHIS premiums (max $8,000 per person)            ___________ B7. Domestic rent (max $100,000)                     ___________ B8. Total Deductions                                 ___________ C. NET INCOME (A6 - B8)                                 ___________ [Used for standard rate calculation] D. ALLOWANCES D1. Basic / Married                                  ___________ D2. Child allowances                                 ___________ D3. Dependent parent/grandparent                     ___________ D4. Other allowances                                 ___________ D5. Total Allowances                                 ___________ E. NET CHARGEABLE INCOME (C - D5)                       ___________ [Used for progressive rate calculation] F. TAX COMPUTATION F1. Progressive tax on E                             ___________ F2. Standard rate tax on C (15% on first $5M, 16% excess) ___________ F3. Tax payable = LOWER of F1 and F2                 ___________ G. TAX REDUCTION (2024/25) G1. 100% reduction, capped at $1,500                 ___________ H. FINAL TAX (F3 - G1)                                  ___________ I. PROVISIONAL TAX I1. Less: provisional tax already paid for 2024/25   ___________ I2. Plus: provisional tax for 2025/26                ___________ I3. NET AMOUNT PAYABLE                               ___________

### 3.2 Worked Example -- Single Employee

**Worked Example -- Single Employee**

| Item | Amount (HK$) |
| --- | --- |
| Annual salary | 600,000 |
| Bonus | 50,000 |
| Total assessable income | 650,000 |
| Less: MPF mandatory (capped) | (18,000) |
| Net income | 632,000 |
| Less: Basic allowance | (132,000) |
| Net chargeable income | 500,000 |

Progressive tax:
- First 50,000 × 2% = 1,000
- Next 50,000 × 6% = 3,000
- Next 50,000 × 10% = 5,000
- Next 50,000 × 14% = 7,000
- Remaining 300,000 × 17% = 51,000
- Total progressive = **67,000**

Standard rate: 632,000 × 15% = **94,800**

Tax payable = lower = **HK$67,000**
Less 2024/25 reduction (100%, max $1,500): **HK$65,500**

### 3.3 Worked Example -- Married with Children

**Worked Example -- Married with Children**

| Item | Amount (HK$) |
| --- | --- |
| Annual salary | 1,200,000 |
| Total assessable income | 1,200,000 |
| Less: MPF mandatory (capped) | (18,000) |
| Net income | 1,182,000 |
| Less: Married allowance | (264,000) |
| Less: 2 children | (260,000) |
| Net chargeable income | 658,000 |

Progressive tax:
- First 200,000 at bands = 16,000
- Remaining 458,000 × 17% = 77,860
- Total progressive = **93,860**

Standard rate: 1,182,000 × 15% = **177,300**

Tax payable = lower = **HK$93,860**
Less 2024/25 reduction: **HK$92,360**

### 4.1 BIR60 (Tax Return -- Individuals)

**BIR60 (Tax Return -- Individuals)**

| Item | Detail |
| --- | --- |
| Form | BIR60 (個別人士報稅表) |
| Issue date | Usually first working day of May |
| Filing deadline (paper) | 1 month from date of issue (usually early June) |
| Filing deadline (eTAX) | 1 additional month (usually early July) |
| Extension | Automatic if filed via eTAX; further extension with tax representative |
| Singed by | Taxpayer (paper) or digital certificate/eTAX password (online) |

### 4.2 Provisional Salaries Tax (IRO Sec. 63E)

**Provisional Salaries Tax (IRO Sec. 63E)**  _(IRO Sec. 63E)_

| Rule | Detail |
| --- | --- |
| Basis | Estimated at 100% of current year final tax |
| Payment | In two instalments (75% + 25%) |
| First instalment | Usually January |
| Second instalment | Usually April |
| Holdover | Can apply if income expected to drop >10% or allowances increase |
| Holdover deadline | 28 days before first instalment due or 14 days before second |

### 4.3 Objection and Appeal

**Objection and Appeal**

| Step | Deadline |
| --- | --- |
| Objection to assessment | Within 1 month of Notice of Assessment |
| Form | Written notice to Assessor stating grounds |
| Appeal to Board of Review | Within 1 month of Commissioner's determination |
| Appeal to Court | Within 1 month of Board's determination |

### 5.1 Non-Hong Kong Employment (Sec. 8(1A)(b))

- **Non-Hong Kong employment** — If employment is exercised partly outside Hong Kong: Income is time-apportioned (HK days / total days); Only HK-sourced portion is assessable; "60-day rule": visits totalling ≤60 days in a year = exempt  _(IRO Sec. 8(1A)(b))_

### 5.2 Lump Sum Payments (Sec. 11D)

- **Lump sum payments** — Gratuity, severance: assessable if connected to HK employment; Retirement scheme lump sum: exempt if from recognised scheme and meets conditions; Golden handshake: fully assessable  _(IRO Sec. 11D)_

### 5.3 Personal Assessment (IRO Sec. 41)

- **Personal Assessment** — Individuals may elect Personal Assessment to: Set off business losses against salaries income; Claim home loan interest deduction; Pool married couple's income for progressive rates. Requirements: Hong Kong permanent resident OR temporary resident for full year; Married couple must both elect if one does; May be beneficial when one spouse has losses/low income  _(IRO Sec. 41)_

### 5.4 Joint Assessment vs Separate Taxation (Married Couples)

**Joint Assessment vs Separate Taxation (Married Couples)**

| Method | When Beneficial |
| --- | --- |
| Joint assessment | One spouse has low/no income; unused allowances transfer |
| Separate taxation | Both spouses have high income; standard rate applies separately |
| Personal assessment (joint) | Business losses to offset; mortgage interest claim |

### 5.5 Domestic Rent Deduction (from 2022/23)

**Domestic Rent Deduction (from 2022/23)**

| Rule | Detail |
| --- | --- |
| Cap | HK$100,000 per year |
| Condition | Taxpayer not provided with quarters by employer |
| Condition | Property not owned by taxpayer or connected person |
| Condition | Tenancy agreement registered with Rating and Valuation Department |
| Married | Each spouse claims up to $100,000 if separate tenancies; or total $200,000 if joint assessment |

### 5.6 Tax Reduction History (Recent Years)

**Tax Reduction History (Recent Years)**

| Year of Assessment | Reduction | Ceiling |
| --- | --- | --- |
| 2022/23 | 100% | HK$6,000 |
| 2023/24 | 100% | HK$3,000 |
| 2024/25 | 100% | HK$1,500 |
| 2025/26 (proposed) | 100% | HK$3,000 |

## Section 6 -- Penalties and Surcharges

**Penalties and Surcharges**  _(IRO Sec. 80(2))_

| Offence | Penalty |
| --- | --- |
| Late filing without reasonable excuse | Up to HK$10,000 + 3× tax undercharged (IRO Sec. 80(2)) |
| Failure to notify chargeability | Fine up to HK$10,000 + 3× tax undercharged |
| Incorrect return | Fine up to HK$10,000 + 3× tax undercharged; or on conviction HK$50,000 + imprisonment |
| Late payment surcharge | 5% immediately on overdue amount; additional 10% after 6 months |
| Fraud or wilful evasion | Fine up to HK$50,000 + 3× tax + imprisonment up to 3 years |

## Section 7 -- Key Dates Calendar

**Key Dates Calendar**

| Date | Event |
| --- | --- |
| 1 April | Start of Year of Assessment |
| Early May | BIR60 issued by IRD |
| Early June | Filing deadline (paper) |
| Early July | Filing deadline (eTAX) |
| Oct--Nov | Notice of Assessment issued |
| January | First instalment of provisional tax due |
| 31 March | End of Year of Assessment |
| April | Second instalment of provisional tax due |

## Section 8 -- Reference Material

**Reference Material**

| Topic | Reference |
| --- | --- |
| Charge to salaries tax | IRO Sec. 8 |
| Assessable income | IRO Sec. 9 |
| Deductions | IRO Sec. 12, 12AA, 12B, 12BA, 16AA, 26I, 26J |
| Allowances | IRO Sec. 28--33 |
| Progressive rates | IRO Schedule 2 |
| Standard rate | IRO Sec. 12B / Schedule 2 |
| Provisional tax | IRO Sec. 63--63J |
| Personal assessment | IRO Sec. 41--43 |
| Domestic rent deduction | IRO Sec. 26J |
| Two-tiered standard rate | Inland Revenue (Amendment) (Taxation Proposals Relating to 2024-25 Budget) Ordinance |
| IRD official site | ird.gov.hk |
| eTAX portal | etax.ird.gov.hk |
| Salaries Tax computation guide | DIPN No. 9 (Rev. 2024) |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Hong Kong CPA, tax representative, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
