---
name: australia-payroll
description: >
  Use this skill whenever asked about Australian payroll, PAYG withholding,
  superannuation guarantee, Single Touch Payroll, or employer obligations in
  Australia. Trigger on phrases like "PAYG", "pay as you go withholding",
  "superannuation", "super guarantee", "STP", "Single Touch Payroll",
  "STP Phase 2", "Medicare levy", "tax file number", "TFN declaration",
  "HECS-HELP", "STSL", "Fair Work", "NES", "national employment standards",
  "modern award", "payslip Australia", "ATO payroll", "BAS", "IAS",
  "activity statement", "annual leave", "long service leave",
  "minimum wage Australia", or any question about running payroll in Australia.
  ALWAYS read this skill before processing any Australian payroll work.
version: 2.1
jurisdiction: AU
tax_year: 2025
last_updated: 2026-08-02
review_status: pending_review
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia -- Payroll Skill v2.0

## Australia -- Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD ($) only |
| Tax year (income year) | 1 July -- 30 June |
| Primary legislation | Income Tax Assessment Act 1997; Superannuation Guarantee (Administration) Act 1992; Fair Work Act 2009 |
| Tax authority | Australian Taxation Office (ATO) |
| Workplace regulator | Fair Work Ombudsman (FWO) |
| Reporting system | Single Touch Payroll (STP) Phase 2 |
| Pay frequency | Weekly, fortnightly, monthly (fortnightly most common) |
| Employer registration | ABN + PAYG withholding registration via ATO |
| Validated by | Pending -- requires sign-off by an Australian CPA, CA, or registered tax agent |
| Skill version | 2.0 |

## Section 2 -- Income Tax Withholding (PAYG)

PAYG withholding is calculated per pay period using ATO tax tables (Schedule 1 -- NAT 1004) or the Statement of Formulas. The employer applies the appropriate coefficients based on weekly/fortnightly/monthly earnings.

### Resident Individual Tax Rates (2026--27)

**Resident Individual Tax Rates (2025--26)**

| Taxable Income (AUD) | Rate | Tax on This Income |
| --- | --- | --- |
| 0 -- 18,200 | 0% | Nil |
| 18,201 -- 45,000 | 15% | 15c for each $1 over $18,200 |
| 45,001 -- 135,000 | 30% | $4,020 plus 30c for each $1 over $45,000 |
| 135,001 -- 190,000 | 37% | $31,020 plus 37c for each $1 over $135,000 |
| 190,001+ | 45% | $51,370 plus 45c for each $1 over $190,000 |

These rates **exclude** the Medicare levy (2%). From 1 July 2026 the rate on $18,201--$45,000 dropped from 16% to 15% (Treasury Laws Amendment (More Cost of Living Relief) Act 2025); it drops again to 14% from 1 July 2027.

### Medicare Levy

**Medicare Levy**

| Item | Detail |
| --- | --- |
| Standard rate | 2% of taxable income |
| Low-income threshold (single) | No levy up to $28,011; reduced levy $28,012--$35,014 |
| Low-income threshold (family) | No levy up to $47,238; reduced $47,239--$59,048 |
| Medicare Levy Surcharge | 1.0%--1.5% additional for high earners without private hospital cover |

- **Medicare levy incorporation** — The Medicare levy is incorporated into PAYG withholding calculations via the tax tables.

### Tax File Number (TFN) Declaration

- **TFN declaration requirement** — Every new employee must complete a TFN declaration. If no TFN is provided, withhold at the top marginal rate (45% + Medicare levy = 47%) from the first dollar.

### Study and Training Support Loans (STSL)

- **STSL description** — Formerly HECS-HELP. Compulsory repayments are withheld via PAYG based on Schedule 8 thresholds. Updated STSL repayment thresholds apply from 24 September 2025, reducing compulsory repayments for most borrowers.

## Section 3 -- Social Security: Employee Deductions

Australia does not have a separate employee social security contribution. The Medicare levy (2%) serves a similar function but is collected through PAYG withholding, not as a separate line item.

### Employee-Side Deductions Summary

**Employee-Side Deductions Summary**

| Deduction | Rate | Ceiling | Notes |
| --- | --- | --- | --- |
| PAYG income tax | Progressive (see above) | No ceiling | Includes Medicare levy in tax tables |
| STSL repayment | 1%--10% (income-based) | No ceiling | Only if employee has HELP/STSL debt |
| Salary sacrifice (super) | Voluntary | Concessional cap $32,500/year (2026-27) | Pre-tax; reduces PAYG withholding base |

There is no employee-paid social insurance premium equivalent to NIC (UK) or social security tax (US).

|---|
| SG rate | 12% of qualifying earnings |
| Maximum contribution base | $270,830 per year (ANNUAL, year-to-date basis; quarterly base abolished for earnings paid from 1 Jul 2026) |
| Minimum earnings threshold | Abolished (no $450/month threshold from 1 Jul 2022) |
| Payment deadline | Received by the employee's fund within **7 business days of each payday** (clearing house receipt does not count) |
| Eligible employees | All employees 18+; under-18s working 30+ hours/week |

**Deadline exceptions:** new employee / new fund -- 20 business days for the first contribution; out-of-cycle payments (bonuses) ride with the next regular payday's deadline; ATO exceptional-circumstances determinations -- 20 business days.

**Legacy:** quarterly due dates (28 Oct/28 Jan/28 Apr/28 Jul) apply only to earnings paid up to 30 June 2026; the final quarterly deadline was 28 July 2026. The ATO Small Business Super Clearing House closed permanently on 1 July 2026 -- small employers now use payroll-software super payments or commercial clearing houses.

12% is the final scheduled SG rate (reached 1 July 2025). No further increases are planned.

### Superannuation Guarantee Charge (SGC) -- redesigned from 1 July 2026

For earnings paid from 1 July 2026, SGC is **ATO-assessed per payday** (no SGC statement is lodged; the ATO matches STP data against fund reporting). Components:
- The final SG shortfall (12% of qualifying earnings unpaid)
- Notional earnings (GIC-rate interest, compounding daily from the day after the deadline)
- An administrative uplift (starts at 60% of shortfall + notional earnings; reduced for clean history and voluntary disclosure, to 0% if disclosed within 30 days with a clean 2-year record)
- Choice loading (25%, capped at $1,200 per notice period) where choice-of-fund rules were breached

The redesigned SGC **is tax-deductible** (GIC on late SGC and the late payment penalty are not). Old-regime SGC for quarters before 1 July 2026 remains non-deductible. Unpaid SGC 28 days after assessment triggers a Notice to Pay, then a 25% or 50% late payment penalty. First-year ATO approach: PCG 2026/1.

### Workers' Compensation Insurance

- **Workers' compensation insurance** — Mandatory in all states/territories. Premium rates vary by industry, state, and claims history. Typically 1%--5% of wages for office-based roles.

### Payroll Tax (State/Territory)

**Payroll Tax (State/Territory)**

| State/Territory | Threshold (Annual) | Rate |
| --- | --- | --- |
| NSW | $1,200,000 | 4.85% |
| VIC | $900,000 | 4.85% |
| QLD | $1,300,000 | 4.75% |
| WA | $1,000,000 | 5.50% |
| SA | $1,500,000 | Varies (0%--4.95%) |
| TAS | $1,250,000 | 4.00% |
| ACT | $2,000,000 | 6.85% |
| NT | $1,500,000 | 5.50% |

- **Payroll tax nature** — Payroll tax is a state/territory tax on total Australian wages above the threshold. Interstate employers must register in each jurisdiction where they have employees.

## Section 5 -- Minimum Wage and Overtime

### National Minimum Wage (from 1 July 2025)

**National Minimum Wage (from 1 July 2025)**

| Category | Rate |
| --- | --- |
| Adult (full-time, 38 hrs/week) | $24.95/hour ($948.10/week) |
| Junior rates | Percentage of adult rate by age (under awards) |
| Casual loading | 25% on top of base rate (in lieu of leave entitlements) |

- **Modern award coverage** — Most employees are covered by a modern award, which sets higher minimum rates by classification level.

### Overtime (Under Awards)

**Overtime (Under Awards)**

| Period | Typical Award Rate |
| --- | --- |
| First 2 hours overtime (Mon--Sat) | 150% (time and a half) |
| After 2 hours overtime | 200% (double time) |
| Sunday work | 200% |
| Public holiday work | 250% |

- **Overtime rate variability** — Exact rates depend on the applicable modern award or enterprise agreement. The Fair Work Act does not prescribe a single universal overtime rate.

### Maximum Ordinary Hours

- **Maximum ordinary hours** — 38 hours/week under the NES. Can be averaged over up to 26 weeks if permitted by the award or agreement.

## Section 6 -- Mandatory Benefits

### Annual Leave

- **Annual leave entitlement** — 4 weeks per year (pro-rata for part-time). Accrues progressively. Shift workers may receive 5 weeks. 17.5% annual leave loading is common under awards (paid on top of base rate when leave is taken).

### Personal / Carer's Leave (Sick Leave)

- **Personal/Carer's leave entitlement** — 10 days per year for full-time employees (pro-rata for part-time). Accumulates year to year with no cap. Paid at the base rate of pay.

### Compassionate / Bereavement Leave

- **Compassionate/bereavement leave entitlement** — 2 days per occasion (paid for permanent employees).

### Long Service Leave

- **Long service leave entitlement** — Governed by state/territory legislation. Typically 8.67 weeks after 10 years of continuous service. Some states allow pro-rata access after 5--7 years.

### Parental Leave

**Parental Leave**

| Type | Duration | Payment |
| --- | --- | --- |
| Government Paid Parental Leave | Up to 22 weeks (increasing to 26 weeks by Jul 2026) | National minimum wage rate |
| Unpaid parental leave | Up to 12 months (can request additional 12 months) | Nil (job-protected) |

### Public Holidays

- **Public holidays entitlement** — 8 national public holidays. Additional state/territory-specific holidays. Employees (except casuals) are entitled to be absent on public holidays without loss of pay.

### Redundancy Pay (NES)

**Redundancy Pay (NES)**

| Years of Service | Weeks of Pay |
| --- | --- |
| 1--2 years | 4 weeks |
| 2--3 years | 6 weeks |
| 3--4 years | 7 weeks |
| 4--5 years | 8 weeks |
| 5--6 years | 10 weeks |
| 6--7 years | 11 weeks |
| 7--8 years | 13 weeks |
| 8--9 years | 14 weeks |
| 9--10 years | 16 weeks |
| 10+ years | 12 weeks |

- **Small business exemption** — Small business employers (< 15 employees) are exempt from NES redundancy pay.

## Section 7 -- Payslip Requirements

- **Payslip issuance timing** — Payslips must be issued within 1 working day of payday (Fair Work Act s536, Fair Work Regulations r3.36).  _(Fair Work Act s536, Fair Work Regulations r3.36)_

### Mandatory Payslip Contents

- Employer's name and ABN
- Employee's name
- Pay period and payment date
- Gross and net amounts paid
- Hourly rate (or annual salary)
- Hours worked (if hourly or pay varies)
- All loadings, allowances, bonuses, incentive payments, penalty rates -- separately itemised
- All deductions (PAYG withholding, salary sacrifice, union fees, etc.)
- Superannuation contributions (employer and any salary sacrifice)
- Name of superannuation fund

### Leave Balances

Not strictly required on payslips but must be provided to employees on request. Best practice is to include annual leave and personal leave balances.

## Section 8 -- Filing Obligations

### Single Touch Payroll (STP) Phase 2

**Single Touch Payroll (STP) Phase 2**

| Item | Detail |
| --- | --- |
| Reporting frequency | Each pay event (each time employees are paid) |
| Method | STP-enabled payroll software submits to ATO |
| Content | Gross payments, PAYG withheld, super liability, employee details, income types, country codes |
| Finalisation deadline | 14 July following end of financial year |
| Closely held payees | May report quarterly; finalise by 14 July |

### PAYG Withholding Remittance

**PAYG Withholding Remittance**

| Employer Size | Reporting | Payment Due |
| --- | --- | --- |
| Small withholders (< $25,000 annual PAYG) | Quarterly BAS | 28 days after quarter end |
| Medium withholders ($25,000--$1M) | Monthly IAS | 21st of following month |
| Large withholders (> $1M) | Monthly IAS + may need to pay more frequently | 21st of following month |

### Superannuation Remittance

| Item | Detail |
|---|---|
| Payment deadline (earnings paid from 1 Jul 2026) | Received by the employee's fund within **7 business days of each payday** (clearing house receipt does not count) |
| New employee / new fund | 20 business days for the first contribution |

**Legacy:** quarterly due dates (28 Oct / 28 Jan / 28 Apr / 28 Jul) apply only to earnings paid up to 30 June 2026; the final quarterly deadline was 28 July 2026.

### Annual Obligations

**Annual Obligations**

| Task | Deadline |
| --- | --- |
| STP finalisation | 14 July |
| PAYG payment summary (now replaced by STP income statement) | Via STP -- no separate form required |
| Workers' comp annual declaration | Per state insurer schedule |
| Payroll tax annual reconciliation | Per state revenue office (typically July/August) |

### Penalties

**Penalties**

| Violation | Consequence |
|---|---|
| Late SG payment | SGC (ATO-assessed per payday): shortfall + notional earnings (GIC rate) + administrative uplift (up to 60%) + choice loading; deductible (the late payment penalty and GIC on unpaid SGC are not) -- see Section 4 |
| Failure to withhold PAYG | Employer liable for amount that should have been withheld |
| Late BAS/IAS lodgement | General interest charge (GIC) + potential failure-to-lodge penalty |
| Payslip non-compliance | Up to $16,500 per contravention (individual); $82,500 (body corporate) |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Full-Time Monthly Employee

Annual salary $85,000. Paid monthly. No STSL debt.

1. Monthly gross: $85,000 ÷ 12 = $7,083.33
2. PAYG withholding: per Schedule 1 tax table coefficients (~$1,475/month incl. Medicare, 2026-27 rates)
3. Super guarantee: $7,083.33 × 12% = $850.00 (employer cost, received by the fund within 7 business days of the payday)
4. Net pay: $7,083.33 - $1,475.00 - deductions

### Pattern 2 -- Casual Employee with Loading

Base rate $28.50/hour under award. Casual loading 25% = $35.63/hour. Works 25 hours.

1. Gross: 25 × $35.63 = $890.75
2. PAYG: per weekly tax table for $890.75
3. Super: $890.75 × 12% = $106.89 (employer cost)
4. No leave accrual (casual loading compensates)

### Pattern 3 -- Employee with Salary Sacrifice to Super

Annual salary $120,000. Sacrifices $10,000/year to super.

1. Taxable salary: $110,000 (reduced PAYG base)
2. Employer SG: $120,000 × 12% = $14,400 (calculated on pre-sacrifice OTE)
3. Concessional super cap: $32,500 (2026-27) (includes SG $14,400 + sacrifice $10,000 = $24,400; within cap)
4. The $10,000 is taxed at 15% inside the super fund instead of the employee's marginal rate

### Pattern 4 -- STSL Repayment

Employee earning $65,000 with HELP debt. STSL repayment rate from Schedule 8 tables: approximately 4.5%. Annual repayment: $65,000 × 4.5% = $2,925, withheld progressively via PAYG.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Australian-specific rules |
| australia-bookkeeping | Payroll journals: salaries + super + payroll tax to P&L; PAYG liability + super liability + net pay to BS |
| australia-bas | PAYG withholding reported on BAS/IAS; GST does not apply to wages |
| australia-stp | STP Phase 2 reporting is the primary payroll compliance mechanism |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

> Contributed by Ryan Duguid.

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
