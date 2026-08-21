---
name: tw-nhi
description: Use this skill whenever asked about Taiwan National Health Insurance (NHI) contributions. Trigger on phrases like "NHI Taiwan", "健保", "全民健康保險", "健保費", "supplementary premium", "補充保費", "NHI self-employed", "health insurance Taiwan", "NHIA", "衛生福利部中央健康保險署", or any question about computing, paying, or understanding NHI premiums for self-employed individuals in Taiwan. This skill covers the general premium rate, supplementary premium, insured payroll categories, and payment obligations. ALWAYS read this skill before advising on Taiwan NHI.
version: 1.0
jurisdiction: TW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - tw-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# TW Nhi

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Taiwan (Republic of China / 中華民國) |
| System | National Health Insurance (全民健康保險 / NHI) |
| Currency | TWD / NTD (New Taiwan Dollar) only |
| Governing legislation | National Health Insurance Act (全民健康保險法) |
| Regulator | National Health Insurance Administration (NHIA / 衛生福利部中央健康保險署) |
| Portal | nhi.gov.tw |
| General premium rate | 5.17% (since January 1, 2021) |
| Supplementary premium rate | 2.11% (since January 1, 2021) |
| Validated by | Pending — requires sign-off by a Taiwan CPA or labour law practitioner |
| Skill version | 1.0 |

### Core Contribution Parameters (2025)

**Core Contribution Parameters (2025)**

| Parameter | Value |
| --- | --- |
| General premium rate (一般保險費率) | 5.17% |
| Supplementary premium rate (補充保險費率) | 2.11% |
| Average number of dependants factor | 0.56 (as of 2025) |
| Minimum insured payroll | NT$28,590 (aligned with minimum wage 2025) |
| Maximum insured payroll | NT$219,500 (Grade 61, highest tier) |
| Self-employed contribution ratio | 100% (insured bears full premium) |
| Employee contribution ratio | 30% (employer 60%, government 10%) |

### Insured Categories Relevant to Self-Employed

**Insured Categories Relevant to Self-Employed**

| Category | Who | Premium Split |
| --- | --- | --- |
| Category 1-2 | Employers, self-employed, professionals practising independently | Insured 100%, Government 0% |
| Category 1-3 | Employees of ≥5 person firms | Insured 30%, Employer 60%, Gov 10% |
| Category 2 | Members of occupational unions without specific employer | Insured 60%, Government 40% |
| Category 3 | Farmers, fishermen | Insured 30%, Government 70% |
| Category 6 | Veterans, low-income, others | Various (mostly government-subsidised) |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown insured category | Check registration status at NHIA |
| Unknown insured payroll | Use minimum (NT$28,590) until confirmed |
| Unknown number of dependants | Assume 0 dependants until confirmed |
| Self-employed vs union member | Self-employed if registered business; union if no specific employer |
| Unknown supplementary premium liability | Flag for verification |

## Section 2 -- General Premium (一般保險費)

### 2.1 Premium Formula

- **Employee premium formula (Category 1-3)** — Monthly premium = Insured payroll × 5.17% × (1 + dependants) × contribution ratio Where: - Contribution ratio for employee = 30% - Dependants: up to 3 can be registered under one insured person (For employees (Category 1-3))
- **Self-employed / employer premium formula (Category 1-2)** — Monthly premium = Insured payroll × 5.17% × (1 + dependants) × 100% Self-employed pays the FULL premium (no employer/government share). (For self-employed / employers (Category 1-2))
- **Union member premium formula (Category 2)** — Monthly premium = Insured payroll × 5.17% × (1 + dependants) × 60% Government subsidises 40%. (For union members (Category 2))

### 2.2 Insured Payroll Bracket Table (Selected Tiers, 2025)

**Insured Payroll Bracket Table (Selected Tiers, 2025)**

| Grade | Monthly Insured Payroll (NT$) | Self-Employed Premium (0 dependants) | Self-Employed Premium (1 dependant) |
| --- | --- | --- | --- |
| 1 | 28,590 | 1,478 | 2,956 |
| 6 | 33,300 | 1,722 | 3,444 |
| 7 | 34,800 | 1,799 | 3,598 |
| 8 | 36,300 | 1,877 | 3,754 |
| 10 | 40,100 | 2,073 | 4,146 |
| 15 | 50,600 | 2,616 | 5,232 |
| 20 | 60,800 | 3,143 | 6,286 |
| 25 | 72,800 | 3,764 | 7,528 |
| 30 | 87,600 | 4,529 | 9,058 |
| 40 | 115,500 | 5,971 | 11,942 |
| 50 | 150,000 | 7,755 | 15,510 |
| 61 | 219,500 | 11,348 | 22,696 |

*Premium = Insured Payroll × 5.17% × (1 + number of dependants). Rounded to nearest NT$.*

### 2.3 Rules for Self-Employed Payroll Declaration

**Rules for Self-Employed Payroll Declaration**

| Rule | Detail |
| --- | --- |
| Minimum declaration | Must declare at least NT$28,590 (minimum wage 2025) |
| If employer with ≥5 employees | Must declare at highest tier or prove lower income |
| If employer with <5 employees | Must declare at least the average of Category 1-3 members (NT$38,200 from Jan 2024) |
| Professionals (lawyers, CPAs, doctors, architects) with ≥5 employees | Must declare at maximum tier (NT$219,500) unless proven lower |
| Professionals with <5 employees or no employees | May self-certify; minimum = average (NT$38,200) |
| Freelancers without employees (小專技) | Minimum = Grade 6 (NT$33,300) |

## Section 3 -- Supplementary Premium (補充保險費)

### 3.1 What Triggers Supplementary Premium

- **Supplementary premium general rule** — The supplementary premium (2.11%) applies to certain types of income exceeding thresholds, paid as a separate deduction at source.

**What Triggers Supplementary Premium table**

| Income Type | Trigger Threshold | Rate | Payer |
| --- | --- | --- | --- |
| Bonus (exceeding 4× monthly insured payroll) | >4× monthly insured payroll in single payment | 2.11% on excess | Employer deducts |
| Part-time salary (non-primary employment) | Single payment ≥NT$28,590 | 2.11% | Employer deducts |
| Professional practice income (執行業務收入) | Single payment ≥NT$28,590 | 2.11% | Payer deducts |
| Dividends (股利所得) | Single payment ≥NT$28,590 | 2.11% | Payer deducts |
| Interest income (利息所得) | Single payment ≥NT$28,590 | 2.11% | Bank deducts |
| Rental income (租金收入) | Single payment ≥NT$28,590 | 2.11% | Tenant/payer deducts |

### 3.2 Supplementary Premium Caps

**Supplementary Premium Caps**

| Limit | Amount |
| --- | --- |
| Maximum per single payment | NT$10,000,000 (supplementary premium capped at this) |
| Maximum supplementary premium per payment | NT$211,000 (2.11% × NT$10,000,000) |

### 3.3 Exemptions from Supplementary Premium

**Exemptions from Supplementary Premium**

| Situation | Exempt? |
| --- | --- |
| Self-employed person's own professional income already included in insured payroll | YES |
| Dividend income of those in government-subsidised categories (Category 5, 6) | YES |
| Interest income below NT$28,590 per single payment | YES (below threshold) |
| Salary from primary employer | YES (covered by general premium) |
| Retirement pension / severance | YES |
| Income of low/middle-income households | YES |

### 3.4 Supplementary Premium Computation Example

Freelancer receives a single payment of NT$100,000 from a client for professional services:

```
Supplementary premium = NT$100,000 × 2.11% = NT$2,110
Client deducts NT$2,110 and remits to NHIA.
Freelancer receives NT$97,890.
```

## Section 4 -- Registration and Payment

### 4.1 Registration for Self-Employed

**Registration for Self-Employed**

| Scenario | Where to Register |
| --- | --- |
| Registered business with employees | Through the business's group insurance applicant (投保單位) |
| Sole proprietor / freelancer with business registration | Through local area office or professional association (公會) |
| Professional practitioner (lawyer, CPA, doctor) | Through respective professional association |
| No business registration / informal | Through occupational union (職業工會) -- Category 2 |
| Unemployed / between jobs | Through local township office (公所) or via dependent registration |

### 4.2 Payment Methods

**Payment Methods**

| Method | Detail |
| --- | --- |
| Bank auto-debit (轉帳代繳) | Monthly automatic deduction from bank account |
| Convenience store (便利商店) | 7-Eleven, FamilyMart, Hi-Life, OK mart |
| Post office | Over-the-counter or ATM |
| Online banking | Through bank's bill payment system |
| NHIA mobile app | NHI Express (全民健保快易通) |
| Credit card | Set up periodic payment |
| Telecom billing | Add to phone bill (limited) |

### 4.3 Payment Schedule

**Payment Schedule**

| Type | Frequency | Due Date |
| --- | --- | --- |
| General premium (self-employed) | Monthly | By the last day of the following month |
| General premium (employee) | Monthly | Employer remits by the last day of the following month |
| Supplementary premium | At source | Payer remits by the last day of the month following payment |

### 4.4 Late Payment

**Late Payment**

| Item | Penalty |
| --- | --- |
| Late general premium | 0.1% per day overdue (滯納金), max 15% of premium owed |
| Non-payment >2 months | Benefits suspended (card locked); resume upon payment of arrears |
| After benefits suspended | May still seek emergency care; full premium arrears required for reinstatement |

## Section 5 -- Tax Deductibility

### 5.1 Income Tax Deduction for NHI Premiums

**Income Tax Deduction for NHI Premiums**

| Rule | Detail |
| --- | --- |
| NHI general premiums | Fully deductible under itemised deductions (NO cap) |
| Other insurance premiums | Capped at NT$24,000 per person per year |
| Supplementary premium paid | Deductible as business expense (if professional income) |
| NHI premiums as business expense | NOT allowed -- personal deduction only |

### 5.2 How to Claim

- If choosing itemised deductions: NHI premiums are listed separately (no cap)
- If choosing standard deduction: NHI premiums are NOT additionally claimed
- eFiling system pre-fills NHI premium data from NHIA records
- Self-employed: include in personal tax return under itemised deductions

## Section 6 -- Computation Examples

### Example 1 -- Self-Employed Freelancer, No Dependants

**Example 1 table**

| Item | Value |
| --- | --- |
| Declared insured payroll | NT$45,800 (Grade 12) |
| Rate | 5.17% |
| Dependants | 0 |
| Contribution ratio | 100% |
| Monthly premium | NT$45,800 × 5.17% × 1 = **NT$2,368** |
| Annual premium | NT$2,368 × 12 = **NT$28,416** |

### Example 2 -- Self-Employed with Spouse and 1 Child

**Example 2 table**

| Item | Value |
| --- | --- |
| Declared insured payroll | NT$60,800 (Grade 20) |
| Rate | 5.17% |
| Dependants | 2 (spouse + child) |
| Contribution ratio | 100% |
| Monthly premium | NT$60,800 × 5.17% × 3 = **NT$9,430** |
| Annual premium | NT$9,430 × 12 = **NT$113,160** |

### Example 3 -- Supplementary Premium on Dividends

**Example 3 table**

| Item | Value |
| --- | --- |
| Dividend payment received | NT$500,000 |
| Rate | 2.11% |
| Supplementary premium | NT$500,000 × 2.11% = **NT$10,550** |
| Deducted at source by company | NT$10,550 |
| Net dividend received | NT$489,450 |

### Example 4 -- Employee (for Comparison)

**Example 4 table**

| Item | Value |
| --- | --- |
| Monthly salary | NT$60,800 (Grade 20) |
| Rate | 5.17% |
| Dependants | 1 |
| Employee share (30%) | NT$60,800 × 5.17% × 2 × 30% = **NT$1,886** |
| Employer share (60%) | NT$60,800 × 5.17% × 2 × 60% = **NT$3,771** |
| Government share (10%) | NT$60,800 × 5.17% × 2 × 10% = **NT$629** |

## Section 7 -- Edge Cases

### 7.1 Dual Status (Employee + Self-Employed)

- Must register under primary status (usually higher-income activity)
- Cannot be double-insured
- If employed AND running a business: insured through employment (Category 1-3)
- Supplementary premium still applies on non-primary income (e.g., side business, dividends)

### 7.2 New Business Registration

- Must register with NHIA within 30 days of starting business
- If previously insured via employer, transfer is automatic upon employer reporting cessation
- Gap in coverage: premiums still owed (mandatory universal coverage, no opt-out)

### 7.3 Overseas Residence

**Overseas Residence**

| Rule | Detail |
| --- | --- |
| Leaving Taiwan >6 months | May apply to suspend NHI (停保) |
| Returning from suspension | 3-month waiting period before reinstatement (or pay arrears for gap) |
| Re-entry within 6 months of suspension | Must resume NHI from re-entry date |
| Permanent departure | Cancel NHI registration; rejoin upon return to Taiwan |

### 7.4 Dependant Registration

- Up to 3 dependants can be registered under one insured person
- If >3 dependants, the 4th+ must register under another insured family member
- Dependants include: spouse, lineal ascendants/descendants, siblings under certain conditions
- Each additional dependant multiplies the premium (dependant factor)

### 7.5 Maximum Premium Cap

For self-employed at highest tier with 3 dependants:
- NT$219,500 × 5.17% × 4 = NT$45,393/month
- Annual: NT$544,716

This represents the absolute maximum NHI premium obligation.

## Section 8 -- Reference Material

**Reference Material table**

| Topic | Reference |
| --- | --- |
| NHI Act | 全民健康保險法 (National Health Insurance Act) |
| Premium rate (5.17%) | NHI Act Art. 18; Executive Yuan announcement (effective 2021.01.01) |
| Supplementary premium (2.11%) | NHI Act Art. 31 |
| Insured payroll brackets | 全民健康保險投保金額分級表 (NHIA announcement) |
| Category definitions | NHI Act Art. 10 |
| Contribution ratios | NHI Act Art. 27 |
| Supplementary premium items | NHI Act Art. 31, Supplementary Premium Regulations |
| Tax deductibility | Income Tax Act Art. 17 (itemised deductions) |
| Late payment | NHI Act Art. 35 |
| Suspension (停保) | NHI Act Art. 22 |
| NHIA official site | nhi.gov.tw |
| NHI Express app | Available on iOS/Android |
| Premium calculator | nhi.gov.tw premium calculator tool |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Taiwan CPA (會計師), labour law practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
