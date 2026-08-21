---
name: my-epf-socso
description: Use this skill whenever asked about Malaysia EPF (KWSP), SOCSO (PERKESO), or EIS contributions. Trigger on phrases like "EPF Malaysia", "KWSP", "Kumpulan Wang Simpanan Pekerja", "SOCSO", "PERKESO", "EIS", "Employment Insurance System", "employer contribution Malaysia", "employee contribution Malaysia", "i-Saraan", "self-employed EPF", "social security Malaysia", or any question about mandatory employment contributions in Malaysia. Covers EPF rates, SOCSO rates, EIS rates, self-employed options, and registration. ALWAYS read this skill before advising on Malaysian employment contributions.
version: 1.0
jurisdiction: MY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: MUHAMMAD HANIS MAT HUSSIN
review_status: current
depends_on: - my-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MY Epf Socso

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malaysia |
| Systems | EPF (KWSP), SOCSO (PERKESO), EIS (SIP) |
| Currency | MYR (Malaysian Ringgit / RM) |
| Contribution year | Calendar month |
| Primary legislation | EPF Act 1991; Employees' Social Security Act 1969 (Act 4); Employment Insurance System Act 2017 (Act 800) |
| Authorities | KWSP (EPF), PERKESO (SOCSO), PERKESO (EIS) |
| Validated by | Pending |
| Validation date | Pending |
| Skill version | 1.0 |

## Section 2 -- EPF (Employees Provident Fund / KWSP)

### 2.1 EPF Contribution Rates -- Malaysian Citizens and Permanent Residents

**EPF Contribution Rates -- Malaysian Citizens and Permanent Residents**

| Employee Category | Monthly Salary | Employee Rate | Employer Rate | Total |
| --- | --- | --- | --- | --- |
| Under 60 years | ≤RM5,000 | 11% | 13% | 24% |
| Under 60 years | >RM5,000 | 11% | 12% | 23% |
| Age 60 -- 75 | Any | 5.5% | 6.5% (≤RM5,000) / 6% (>RM5,000) | ~12% |
| Age 75+ | Any | 0% | 0% | 0% |

### 2.2 EPF -- Foreign Employees (from 1 October 2025)

**EPF -- Foreign Employees (from 1 October 2025)**

| Category | Employee Rate | Employer Rate | Total |
| --- | --- | --- | --- |
| Non-Malaysian citizen (under 60) | 2% | 2% | 4% |
| Non-Malaysian citizen (60+) | 2% | 2% | 4% |
| Permanent Residents | Same as Malaysian citizens | Same as Malaysian citizens | Same |
| Registered before 1 August 1998 | Same as Malaysian citizens | Same as Malaysian citizens | Same |

### 2.3 EPF Key Rules

**EPF Key Rules**

| Item | Detail |
| --- | --- |
| Maximum contribution | No statutory cap on wages for EPF; contribution based on actual wages |
| Remittance deadline | 15th of the following month |
| Computation | Per KWSP Third Schedule (rounded to nearest ringgit) |
| Tax deduction | Employee EPF contribution deductible as personal relief (max RM7,000 combined with life insurance) |
| Employer deduction | Employer EPF contribution is a deductible business expense |

### 2.4 EPF for Self-Employed (i-Saraan)

**EPF for Self-Employed (i-Saraan)**

| Item | Detail |
| --- | --- |
| Scheme | i-Saraan (voluntary) |
| Who | Self-employed, freelancers, gig workers, homemakers |
| Contribution | Any amount, up to RM100,000/year |
| Government incentive | Government matches 20% of contribution, up to RM350/year (subject to annual budget) |
| Tax relief | Contributions eligible for personal tax relief under life insurance + EPF (max RM7,000) |
| Registration | Via KWSP portal (kwsp.gov.my) or KWSP counters |
| No employer contribution | Self-employed pays full amount; no employer share |

## Section 3 -- SOCSO (Social Security Organisation / PERKESO)

### 3.1 Overview

SOCSO provides social security protection for employees covering employment injury and invalidity.

### 3.2 SOCSO Contribution Rates (from 1 October 2024)

**SOCSO Contribution Rates (from 1 October 2024)**

| Scheme | Employer Rate | Employee Rate | Total |
| --- | --- | --- | --- |
| Employment Injury Scheme (EIS) + Invalidity Scheme | 1.75% | 0.5% | 2.25% |
| Employment Injury Scheme only (employees ≥60, first-time contributors ≥55) | 1.25% | 0% | 1.25% |

### 3.3 SOCSO Wage Ceiling

**SOCSO Wage Ceiling**

| Item | Amount |
| --- | --- |
| Wage ceiling (from 1 October 2024) | RM6,000/month |
| Previous ceiling (before October 2024) | RM5,000/month |
| Wages above ceiling | Only the ceiling amount applies for contribution calculation |

### 3.4 Maximum Monthly SOCSO Contribution

**Maximum Monthly SOCSO Contribution**

| Component | Employer | Employee | Total |
| --- | --- | --- | --- |
| Full scheme (EIS + Invalidity) | RM105.00 | RM30.00 | RM135.00 |
| Employment Injury only (≥60) | RM75.00 | RM0 | RM75.00 |

Note: Actual amounts are per the PERKESO Third Schedule contribution table (stepped amounts, not pure percentages).

### 3.5 SOCSO for Self-Employed

**SOCSO for Self-Employed**

| Item | Detail |
| --- | --- |
| Scheme | Self-Employment Social Security Scheme (Act 789) |
| Coverage | Selected categories of self-employed (e.g., taxi drivers, fishermen, farmers, gig workers) |
| Registration | Via PERKESO portal |
| Contribution | Based on insured monthly earnings bracket (RM13.10 -- RM49.40/month) |
| Benefits | Employment injury benefits, invalidity pension, funeral benefit |

## Section 4 -- EIS (Employment Insurance System)

### 4.1 Overview

EIS provides temporary financial assistance to employees who lose their jobs, plus re-employment placement and training.

### 4.2 EIS Contribution Rates

**EIS Contribution Rates**

| Party | Rate | Wage Ceiling |
| --- | --- | --- |
| Employee | 0.2% | RM6,000/month |
| Employer | 0.2% | RM6,000/month |
| Maximum per party | RM12/month |  |
| Total maximum | RM24/month |  |

### 4.3 EIS Eligibility

**EIS Eligibility**

| Category | Covered |
| --- | --- |
| Malaysian citizens, under 60, private sector | Yes |
| Permanent residents, under 60, private sector | Yes |
| Foreign employees | Generally not covered |
| Government employees | Not covered |
| Domestic workers | Not covered |
| Self-employed | Not covered |
| Employees aged 60+ | Not required |

### 4.4 EIS Benefits

**EIS Benefits**

| Benefit | Detail |
| --- | --- |
| Job Search Allowance | Up to 6 months of payments |
| Early Re-employment Allowance | Lump sum for finding work before JSA expires |
| Training fees | For approved re-skilling programmes |
| Reduced Income Allowance | If new job pays significantly less |

## Section 5 -- Combined Contribution Summary

### 5.1 Employee Earning RM4,000/month (Malaysian citizen, under 60)

**Employee Earning RM4,000/month (Malaysian citizen, under 60)**

| System | Employee | Employer | Total |
| --- | --- | --- | --- |
| EPF (11% / 13%) | RM440 | RM520 | RM960 |
| SOCSO (~per table) | ~RM20 | ~RM70 | ~RM90 |
| EIS (0.2% / 0.2%) | RM8 | RM8 | RM16 |
| **Total** | **~RM468** | **~RM598** | **~RM1,066** |

### 5.2 Employee Earning RM8,000/month (Malaysian citizen, under 60)

**Employee Earning RM8,000/month (Malaysian citizen, under 60)**

| System | Employee | Employer | Total |
| --- | --- | --- | --- |
| EPF (11% / 12%) | RM880 | RM960 | RM1,840 |
| SOCSO (capped at RM6,000) | ~RM30 | ~RM105 | ~RM135 |
| EIS (capped at RM6,000) | RM12 | RM12 | RM24 |
| **Total** | **~RM922** | **~RM1,077** | **~RM1,999** |

## Section 6 -- Registration and Compliance

### 6.1 Employer Registration

**Employer Registration**

| System | Registration | Deadline |
| --- | --- | --- |
| EPF | Register within 7 days of hiring first employee | KWSP portal or counter |
| SOCSO | Register within 30 days of hiring first employee | PERKESO portal (assist.perkeso.gov.my) |
| EIS | Registered together with SOCSO | Same registration |

### 6.2 Monthly Submission Deadlines

**Monthly Submission Deadlines**

| System | Deadline |
| --- | --- |
| EPF | 15th of following month |
| SOCSO + EIS | 15th of following month (combined submission) |

### 6.3 Penalties for Non-Compliance

**Penalties for Non-Compliance**

| Offence | EPF Penalty | SOCSO/EIS Penalty |
| --- | --- | --- |
| Late contribution | Dividend loss + 10% late payment charge | 6% per annum interest |
| Failure to register | Fine up to RM10,000 or imprisonment ≤3 years | Fine up to RM10,000 |
| Failure to contribute | Fine up to RM10,000 or imprisonment ≤3 years per offence | Fine up to RM10,000 or imprisonment ≤2 years |

## Section 7 -- Tax Treatment

**Tax Treatment**

| Contribution | Tax Treatment |
| --- | --- |
| Employee EPF contribution | Personal relief up to RM7,000 (combined with life insurance premiums) |
| Employer EPF contribution | Deductible business expense for employer |
| Employee SOCSO/EIS contribution | Personal relief up to RM350 |
| Employer SOCSO/EIS contribution | Deductible business expense for employer |
| Self-employed i-Saraan | Personal relief under EPF/life insurance category |

## Section 8 -- Reference Material

### Key Portals

**Key Portals**

| System | URL |
| --- | --- |
| EPF (KWSP) | https://www.kwsp.gov.my |
| i-Saraan registration | https://www.kwsp.gov.my |
| SOCSO (PERKESO) | https://www.perkeso.gov.my |
| EIS | https://eis.perkeso.gov.my |
| Contribution tables | Available on respective portals |

### Key Legislation

**Key Legislation**

| System | Act |
| --- | --- |
| EPF | Employees Provident Fund Act 1991 |
| SOCSO | Employees' Social Security Act 1969 (Act 4) |
| Self-employed SOCSO | Self-Employment Social Security Act 2017 (Act 789) |
| EIS | Employment Insurance System Act 2017 (Act 800) |

## Prohibitions

- NEVER apply Malaysian citizen EPF rates to foreign employees -- separate rates apply from October 2025
- NEVER exceed the SOCSO/EIS wage ceiling of RM6,000 in contribution calculations
- NEVER assume self-employed persons must contribute to EPF -- i-Saraan is voluntary
- NEVER claim employee SOCSO/EIS relief above the RM350 cap
- NEVER combine employee and employer contributions when calculating personal tax relief
- NEVER present calculations as definitive -- always verify against the official KWSP/PERKESO contribution tables

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
