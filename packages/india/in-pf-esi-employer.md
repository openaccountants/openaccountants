---
name: in-pf-esi-employer
description: Use this skill whenever asked about Indian EPF (Employees' Provident Fund), ESI (Employees' State Insurance), or employer social security obligations. Trigger on phrases like "PF contribution India", "EPF employer", "ESI contribution", "provident fund India", "PF admin charges", "EDLI", "EPS pension", "ECR filing", "PF return", "ESI threshold", "PF applicability", "12% PF", "employer PF obligation", or any question about computing, depositing, or filing EPF/ESI in India. This skill covers EPF contribution rates, EPS, EDLI, ESI rates and thresholds, applicability criteria, monthly filing (ECR), and compliance deadlines. ALWAYS read this skill before touching any Indian PF/ESI employer work.
version: "1.0"
jurisdiction: IN
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mayur Deokar
review_status: current
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IN Pf Esi Employer

## India EPF & ESI -- Employer Obligations Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mayur Deokar** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### EPF and ESI

- **Employer total** — 12% of Basic + DA  _(EPF Act 1952)_
- **EPF account** — 3.67%  _(EPF Act)_
- **EPS (pension)** — 8.33% (capped at ₹15,000/month = max ₹1,250/mo)  _(EPF Act)_
- **Employee contribution** — 12% of Basic + DA  _(EPF Act 1952)_
- **EPF Admin** — 0.50% of total EPF wages (min ₹500/month if >20 employees)  _(EPFO notification)_
- **EDLI (life insurance)** — 0.50% of Basic+DA (capped at ₹15,000) = max ₹75/mo  _(EPFO notification)_
- **EDLI Admin** — Nil (removed 01-04-2017)  _(EPFO notification)_
- **Employer ESI** — 3.25% of gross wages  _(ESI Act 1948)_
- **Employee ESI** — 0.75% of gross wages  _(ESI Act 1948)_
- **Total ESI** — 4%  _(ESI Act)_
- **ECR (EPF monthly)** — 15th of following month  _(EPFO)_
- **ESI monthly** — 15th of following month  _(ESIC)_
- **Employer total EPF contribution** — 12% of Basic + DA  _(EPF Act 1952)_
- **EPF account split (employer)** — 3.67%  _(EPF Act)_
- **EPS (pension)** — 8.33% (capped at ₹15,000/month = max ₹1,250/mo)  _(EPF Act)_
- **Employee EPF contribution** — 12% of Basic + DA  _(EPF Act 1952)_
- **PF wage ceiling** — ₹15,000/month (statutory; many contribute on actual)  _(EPF Act)_
- **EPF applicability** — Establishments with 20+ persons  _(EPF Act)_
- **EPF Admin** — 0.50% of total EPF wages (min ₹500/month if >20 employees)  _(EPFO notification)_
- **EDLI (life insurance)** — 0.50% of Basic+DA (capped at ₹15,000) = max ₹75/mo  _(EPFO notification)_
- **EDLI Admin** — Nil (removed 01-04-2017)  _(EPFO notification)_
- **EDLI death benefit** — Up to ₹7,00,000  _(EPFO)_
- **Employer ESI contribution** — 3.25% of gross wages  _(ESI Act 1948)_
- **Employee ESI** — 0.75% of gross wages  _(ESI Act 1948)_
- **Total ESI** — 4%  _(ESI Act)_
- **ESI wage ceiling** — ₹21,000/month (₹25,000 for disability)  _(ESI Act)_
- **ESI applicability** — Establishments with 10+ persons (notified areas)  _(ESI Act)_
- **ECR (EPF monthly) filing deadline** — 15th of following month  _(EPFO)_
- **ESI monthly filing deadline** — 15th of following month  _(ESIC)_
- **Late payment penalty** — 12% per annum (simple interest) + damages 1% per month or part thereof from the date of default  _(EPF Act / ESI Acts)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax/Contribution | EPF (Provident Fund) + ESI (State Insurance) |
| Currency | INR only |
| Applicable period | FY 2025-26 (April 2025 -- March 2026) |
| EPF legislation | Employees' Provident Funds and Miscellaneous Provisions Act, 1952 |
| ESI legislation | Employees' State Insurance Act, 1948 |
| Administering bodies | EPFO (Employees' Provident Fund Organisation); ESIC (ESI Corporation) |
| Filing portal (EPF) | Unified Portal (unifiedportal-emp.epfindia.gov.in) |
| Filing portal (ESI) | ESIC Portal (esic.gov.in) |
| Skill version | 1.0 |

### EPF Contribution Summary

**EPF Contribution Summary**

| Component | Employer (%) | Employee (%) | On |
| --- | --- | --- | --- |
| EPF (Provident Fund) | 3.67% | 12% | Basic + DA |
| EPS (Employee Pension Scheme) | 8.33% | Nil | Basic + DA (capped at ₹15,000/month) |
| **Total employer contribution** | **12%** | -- | Basic + DA |
| **Total employee contribution** | -- | **12%** | Basic + DA |

### Employer Administrative Charges

**Employer Administrative Charges**

| Charge | Rate | On |
| --- | --- | --- |
| EPF Admin charges | 0.50% | Total EPF wages (minimum ₹500/month if >20 employees) |
| EDLI (Employees' Deposit Linked Insurance) | 0.50% | Basic + DA (capped at ₹15,000/month) |
| EDLI Admin charges | Nil (removed w.e.f. 01-04-2017) | -- |

### ESI Contribution Summary

**ESI Contribution Summary**

| Component | Rate | On |
| --- | --- | --- |
| Employer ESI | 3.25% | Gross wages (all components except certain exclusions) |
| Employee ESI | 0.75% | Gross wages |
| **Total ESI** | **4%** | Gross wages |

### ESI Wage Ceiling

**ESI Wage Ceiling**

| Threshold | Amount |
| --- | --- |
| ESI applicability (employee) | Gross wages ≤ ₹21,000/month |
| ESI applicability (disability employee) | Gross wages ≤ ₹25,000/month |

### Applicability Thresholds

**Applicability Thresholds**

| Scheme | Applies When |
| --- | --- |
| EPF | Establishment employs 20 or more persons |
| ESI | Establishment employs 10 or more persons (in notified areas) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether establishment is covered | Verify employee count -- do not assume |
| Unknown wage components | Include all regular earnings as PF wages unless specifically excluded |
| Unknown ESI area notification | Check ESIC notification for the area |

## Section 2 -- EPF Detailed Rules

### 2.1 Wage Components for PF

**Wage Components for PF**

| Included in Basic + DA (PF Wages) | Excluded from PF Wages |
| --- | --- |
| Basic salary | House Rent Allowance (HRA) |
| Dearness Allowance (DA) | Overtime allowance |
| Retaining allowance | Bonus (statutory or otherwise) |
| Cash value of food concession (if not provided) | Commission |
|  | Conveyance allowance |
|  | Retrenchment compensation |
|  | Gratuity |

- **PF wage ceiling (voluntary cap)** — ₹15,000/month is the statutory wage ceiling for EPF. Employers may choose to contribute on actual Basic + DA even if above ₹15,000 (most large employers do this). EPS is always capped at ₹15,000/month.

### 2.2 Employer 12% Breakup

**Employer 12% Breakup**

| Component | Rate | Cap |
| --- | --- | --- |
| EPF account (employee's individual PF) | 3.67% | On full PF wages |
| EPS (Pension fund) | 8.33% | Capped at ₹15,000/month (max ₹1,250/month to EPS) |
| If PF wages > ₹15,000 | Balance of 8.33% above cap goes to EPF | Full 12% effectively goes to EPF |

**Example:** Employee with Basic + DA = ₹30,000/month:
- Employer EPF = ₹30,000 × 3.67% = ₹1,101
- Employer EPS = ₹15,000 × 8.33% = ₹1,250 (capped)
- Remaining to EPF = (₹30,000 × 8.33%) − ₹1,250 = ₹2,499 − ₹1,250 = ₹1,249
- Total employer to EPF account = ₹1,101 + ₹1,249 = ₹2,350
- Total employer contribution = ₹30,000 × 12% = ₹3,600 (split between EPF and EPS)

### 2.3 EDLI (Employees' Deposit Linked Insurance)

**EDLI Details**

| Item | Detail |
| --- | --- |
| Purpose | Life insurance for EPF members |
| Employer contribution | 0.50% of Basic + DA (capped at ₹15,000/month) |
| Maximum EDLI contribution | ₹75/month per employee |
| Benefit on death | Up to ₹7,00,000 (₹7 lakh) |
| Employee contribution | Nil |

### 2.4 International Workers

**International Workers PF Treatment**

| Scenario | PF Treatment |
| --- | --- |
| Indian employee sent abroad (no SSA country) | PF continues on Indian salary |
| Foreign national working in India (from SSA country) | Exempt from PF if covered in home country |
| Foreign national from non-SSA country | PF mandatory at full rate |

- **SSA** — Social Security Agreement (India has SSAs with ~20 countries).

## Section 3 -- ESI Detailed Rules

### 3.1 Wage Components for ESI

- **Basis of ESI calculation** — ESI is calculated on **gross wages** (broader than PF wages)

**Wage Components for ESI**

| Included | Excluded |
| --- | --- |
| Basic salary | Annual bonus (statutory) |
| DA | Retrenchment compensation |
| HRA | Encashment of leave on superannuation |
| City Compensatory Allowance | Gratuity |
| Overtime (for contribution purposes) |  |
| All other regular cash payments |  |

### 3.2 Contribution Period and Benefit Period

**Contribution and Benefit Periods**

| Contribution Period | Benefit Period |
| --- | --- |
| 1 April -- 30 September | 1 January -- 30 June (following) |
| 1 October -- 31 March | 1 July -- 31 December (following) |

### 3.3 ESI Benefits

**ESI Benefits**

| Benefit | Coverage |
| --- | --- |
| Medical benefit | Full medical care for employee and family |
| Sickness benefit | 70% of wages for up to 91 days |
| Maternity benefit | Full wages for 26 weeks |
| Disablement benefit | 90% of wages (temporary); pension (permanent) |
| Dependants' benefit | 90% of wages as pension to dependants |
| Funeral expenses | ₹15,000 |

### 3.4 Crossing the ESI Threshold

- **Crossing the ESI threshold mid-period** — If an employee's wages exceed ₹21,000/month mid-contribution period: - ESI contributions continue for the remainder of that contribution period - Employee ceases to be covered from the next contribution period - Employer must ensure coverage for the full 6-month period once started

## Section 4 -- Filing and Payment

### 4.1 EPF -- ECR (Electronic Challan cum Return)

**ECR Details**

| Item | Detail |
| --- | --- |
| What is ECR | Monthly return declaring employee-wise PF contributions |
| Due date | 15th of the following month |
| Payment mode | Online through EPFO Unified Portal |
| Format | Upload employee data (UAN, name, wages, contribution breakup) |
| Late payment penalty | Simple interest at 12% per annum on delayed deposits |
| Damages | 5% to 25% per annum depending on delay period |

### 4.2 ESI -- Monthly Contribution

**ESI Monthly Contribution Details**

| Item | Detail |
| --- | --- |
| Due date | 15th of the following month |
| Payment mode | Online through ESIC portal |
| Return | Half-yearly return (now largely subsumed in monthly online filing) |
| Late payment penalty | Simple interest at 12% per annum |
| Damages | Up to 25% of arrears |

### 4.3 Annual Returns

**Annual Returns**

| Return | Due Date | Covers |
| --- | --- | --- |
| EPF Annual Return (Form 3A/6A) | Now via monthly ECR (no separate annual) | Automated through monthly ECR |
| ESI Return (Form 5) | Half-yearly (11 May and 11 November) | Contribution register |

## Section 5 -- Computation Examples

### Example 1: Standard Employee (PF + ESI applicable)

Employee: Basic = ₹12,000/month, DA = ₹3,000/month, HRA = ₹5,000/month
Gross = ₹20,000/month (below ₹21,000 ESI threshold)

**Example 1 Calculation Table**

| Component | Employer | Employee |
| --- | --- | --- |
| EPF (on Basic + DA = ₹15,000) | ₹15,000 × 3.67% = ₹550.50 | ₹15,000 × 12% = ₹1,800 |
| EPS (capped at ₹15,000) | ₹15,000 × 8.33% = ₹1,249.50 | Nil |
| Total PF employer | ₹1,800 (12% of ₹15,000) | ₹1,800 |
| EDLI | ₹15,000 × 0.50% = ₹75 | Nil |
| PF Admin | ₹15,000 × 0.50% = ₹75 | Nil |
| ESI (on gross ₹20,000) | ₹20,000 × 3.25% = ₹650 | ₹20,000 × 0.75% = ₹150 |
| **Total employer cost** | **₹2,600** | -- |
| **Total employee deduction** | -- | **₹1,950** |

### Example 2: Higher Salary (PF only, ESI not applicable)

Employee: Basic + DA = ₹40,000/month, Gross = ₹65,000/month (above ₹21,000 ESI threshold)

**Example 2 Calculation Table**

| Component | Employer | Employee |
| --- | --- | --- |
| EPF (on ₹40,000, if contributing on actual) | ₹40,000 × 3.67% = ₹1,468 | ₹40,000 × 12% = ₹4,800 |
| EPS (capped at ₹15,000) | ₹15,000 × 8.33% = ₹1,250 | Nil |
| Remaining to EPF | ₹40,000 × 8.33% − ₹1,250 = ₹2,082 | Nil |
| Total PF employer | ₹4,800 (12% of ₹40,000) | ₹4,800 |
| EDLI | ₹15,000 × 0.50% = ₹75 | Nil |
| PF Admin | ₹40,000 × 0.50% = ₹200 | Nil |
| ESI | Not applicable (gross > ₹21,000) | Not applicable |
| **Total employer cost** | **₹5,075** | -- |

## Section 6 -- Edge Cases

### 6.1 Establishments with < 20 Employees

- **EPF applicability for small establishments** — EPF is mandatory for establishments with 20+ employees. Establishments with fewer may voluntarily register. Once registered, coverage continues even if numbers drop below 20.

### 6.2 Contract Labour

- **Contract labour PF/ESI responsibility** — The principal employer is responsible for PF/ESI of contract workers if the contractor fails to deposit. Both principal employer and contractor must be registered.

### 6.3 Fixed-Term Employees

- **Fixed-term employee coverage** — Fixed-term employees are entitled to same PF/ESI benefits as regular employees from day one. No waiting period.

### 6.4 Exempted Establishments (PF Trust)

- **PF Trust exemption** — Large employers may apply for EPF exemption to manage their own PF trust. Must provide equal or better benefits. Trust must maintain accounts as per EPFO norms.

### 6.5 VPF (Voluntary Provident Fund)

- **VPF rules** — Employee may contribute above 12% voluntarily (up to 100% of Basic + DA). Employer contribution remains at 12% -- no additional employer obligation for VPF.

### 6.6 New Establishments

- **New establishment registration deadlines** — A new establishment must register with EPFO within one month of employing 20 persons. ESI registration within 15 days of applicability.

## Section 7 -- Prohibitions

- NEVER compute PF on gross salary -- PF is on Basic + DA only
- NEVER exceed the EPS ceiling (₹15,000/month) for pension calculation
- NEVER apply ESI to employees earning above ₹21,000/month gross (unless mid-period crossing)
- NEVER miss the 15th of the month deadline without accounting for interest/damages
- NEVER assume all establishments are covered -- verify employee count threshold
- NEVER confuse employer contribution rate (12%) with employee rate (12%) -- they are separate obligations
- NEVER ignore admin charges and EDLI when computing total employer cost
- NEVER present calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CA, CMA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
