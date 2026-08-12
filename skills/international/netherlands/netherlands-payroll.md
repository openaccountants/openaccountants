---
name: netherlands-payroll
description: Use this skill whenever asked about Dutch payroll, loonheffing, wage tax, social security contributions, or employer obligations in the Netherlands. Trigger on phrases like "loonheffing", "loonbelasting", "Dutch payroll", "Netherlands payroll", "volksverzekeringen", "AOW premie", "WW premie", "WAO", "WIA", "Aof", "Awf", "ZVW", "Zvw bijdrage", "zorgverzekeringswet", "vakantiegeld", "holiday allowance", "loonaangifte", "30% ruling", "werkgeversheffing", "minimumloon", "minimum wage Netherlands", "payslip Netherlands", "loonstrook", "social insurance Netherlands", or any question about running payroll in the Netherlands. ALWAYS read this skill before processing any Dutch payroll work.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Payroll

## Netherlands -- Payroll Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Currency | EUR (€) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Wet op de loonbelasting 1964; Wet financiering sociale verzekeringen (Wfsv) |
| Tax authority | Belastingdienst (Dutch Tax Administration) |
| Social insurance bodies | UWV (employee insurance); SVB (national insurance) |
| Reporting system | Loonaangifte (payroll tax return) via Digipoort |
| Pay frequency | Monthly (most common) |
| Employer registration | Loonheffingennummer via Belastingdienst |
| Validated by | Pending -- requires sign-off by a Dutch registeraccountant or payroll specialist |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (Loonheffing)

Loonheffing combines wage tax (loonbelasting) and national insurance premiums (premies volksverzekeringen) into a single withholding. The employer withholds based on published tax tables (white or green table) using the loonheffingskorting (payroll tax credit) if applicable.

### Combined Brackets -- Under State Pension Age (2026)

**Combined Brackets -- Under State Pension Age (2026)**

| Bracket | Annual Wage (EUR) | Combined Rate | Composition |
| --- | --- | --- | --- |
| 1 | 0 -- 38,883 | 35.75% | 8.10% tax + 17.90% AOW + 0.10% Anw + 9.65% Wlz |
| 2 | 38,883 -- 78,426 | 37.56% | 37.56% tax only |
| 3 | 78,426+ | 49.50% | 49.50% tax only |

### Combined Brackets -- At or Above State Pension Age (2026)

**Combined Brackets -- At or Above State Pension Age (2026)**

| Bracket | Annual Wage (EUR) | Combined Rate | Composition |
| --- | --- | --- | --- |
| 1 | 0 -- 38,883 | 17.85% | 8.10% tax + 0.10% Anw + 9.65% Wlz |
| 2 | 38,883 -- 78,426 | 37.56% | Tax only |
| 3 | 78,426+ | 49.50% | Tax only |

- **AOW premie exemption for AOW-age recipients** — AOW-age recipients do not pay AOW premie (17.90%), reducing the bracket 1 rate.

### Loonheffingskorting (Payroll Tax Credits -- 2026)

Employees may request the loonheffingskorting via only one employer (prevents double credit). Key credits:

**Loonheffingskorting (Payroll Tax Credits -- 2026)**

| Credit | Maximum Amount (EUR) | Notes |
| --- | --- | --- |
| Algemene heffingskorting (general) | ~3,362 | Phases out above ~24,813; zero at ~78,426 |
| Arbeidskorting (employment credit) | ~5,599 | Phases out above ~43,071; zero at ~124,935 |
| Ouderenkorting (elderly) | ~1,963 | For AOW-age recipients; phases out at higher income |

### 30% Ruling (Extraterritorial Costs)

- **30% Ruling** — Qualifying inbound employees may receive up to 30% of their employment income tax-free through 2026, capped at the 2026 WNT norm of EUR 262,000 (maximum allowance EUR 78,600) for a maximum of 5 years. From 1 January 2027 the standard percentage becomes 27%, with grandfathering for employees who already used the ruling before 2024.

## Section 3 -- Social Security: Employee Deductions

Employee deductions in the Netherlands are primarily collected through the combined loonheffing (bracket 1 includes AOW, Anw, Wlz premiums). There are no separate employee premiums for WW or WAO/WIA -- those are employer-only.

### National Insurance Premiums Embedded in Loonheffing (2026)

**National Insurance Premiums Embedded in Loonheffing (2026)**

| Premium | Rate | Ceiling | Notes |
| --- | --- | --- | --- |
| AOW (state pension) | 17.90% | Bracket 1 only (up to EUR 38,883) | Not payable at/above AOW age |
| Anw (surviving dependants) | 0.10% | Bracket 1 only |  |
| Wlz (long-term care) | 9.65% | Bracket 1 only |  |

### Zorgverzekeringswet (ZVW) -- Health Insurance

**Zorgverzekeringswet (ZVW) -- Health Insurance**

| Type | Rate (2026) | Maximum Income |
| --- | --- | --- |
| Werkgeversheffing (employer levy, standard) | 6.10% | EUR 79,409 |
| Werknemersbijdrage (employee/DGA contribution) | 4.85% | EUR 79,409 |

- **ZVW payer distinction** — Most employees pay the werkgeversheffing (employer levy form), which is technically paid by the employer but treated as taxable wage. DGAs (directeur-grootaandeelhouder) and certain others pay the lower employee rate, which is withheld from gross pay.

## Section 4 -- Social Security: Employer Contributions

Employer contributions are calculated on the SV-loon (social insurance wage) up to the maximum premium wage (maximumpremieloon).

### Employer-Only Premiums (2026)

**Employer-Only Premiums (2026)**

| Premium | Rate | Maximum Premium Wage | Notes |
| --- | --- | --- | --- |
| AWf low (WW -- permanent/indefinite contracts) | 2.74% | EUR 79,409 | Indefinite contracts, written, not on-call |
| AWf high (WW -- flexible/temporary contracts) | 7.74% | EUR 79,409 | Fixed-term, on-call, no written contract |
| Aof low (WAO/WIA -- small employers) | 6.27% | EUR 79,409 | Employer < 25× avg premium wage |
| Aof high (WAO/WIA -- large employers) | 7.63% | EUR 79,409 | Employer ≥ 25× avg premium wage |
| Whk (return-to-work fund) | ~1.52% avg | EUR 79,409 | Differentiated per employer |
| Wko (childcare surcharge) | 0.50% | EUR 79,409 |  |
| Ufo (flex workers fund) | 0.68% | EUR 79,409 |  |
| ZVW werkgeversheffing | 6.10% | EUR 79,409 | Also counted as employer cost |

### Total Indicative Employer Cost (2026)

**Total Indicative Employer Cost (2026)**

| Scenario | Approximate Rate |
| --- | --- |
| Small employer, permanent staff (AWf low + Aof low + Whk avg + Wko + Ufo + ZVW) | ~17.81% |
| Large employer, temporary staff (AWf high + Aof high + Whk avg + Wko + Ufo + ZVW) | ~24.17% |

These are on top of gross salary. The actual Whk rate is employer-specific and communicated by the Belastingdienst.

## Section 5 -- Minimum Wage and Overtime

### Statutory Minimum Hourly Wage (Wettelijk Minimumloon -- WML)

**Statutory Minimum Hourly Wage (Wettelijk Minimumloon -- WML)**

| Period | Gross Hourly Rate (21+) | Reference Monthly Wage |
| --- | --- | --- |
| 1 Jan 2026 | EUR 14.71 | EUR 2,294.40 |
| 1 Jul 2026 | EUR 14.99 | EUR 2,337.00 |

- **Youth minimum wage and adjustment frequency** — Youth minimum wages apply for ages 15--20 (percentage of adult rate). The minimum wage is adjusted every 6 months (January and July).

### Overtime

- **Overtime premium** — No statutory overtime premium exists in Dutch law. Overtime compensation is regulated by the applicable Collective Labour Agreement (CAO) or individual employment contract. Common CAO premiums range from 125% to 200% depending on timing (evening, weekend, public holiday).

### Working Hours

- **Maximum working hours** — Maximum 12 hours per shift and 60 hours per week under the Arbeidstijdenwet (Working Hours Act). Averaged over 4 weeks, maximum is 55 hours/week; over 16 weeks, maximum is 48 hours/week.  _(Arbeidstijdenwet (Working Hours Act))_

## Section 6 -- Mandatory Benefits

### Holiday Allowance (Vakantiegeld)

- **Vakantiegeld** — Minimum 8% of gross annual salary. Typically paid as a lump sum in May or June. Accrues monthly. Must be paid upon termination for accrued but unpaid amounts.

### Holiday Entitlement

- **Holiday entitlement** — Minimum 4× weekly working hours per year (20 days for full-time). Statutory days expire 6 months after the year of accrual. Many CAOs provide additional (bovenwettelijke) days.

### 13th Month

- **13th month** — Not legally required. Commonly provided via CAO or employment contract (typically one month's salary paid in December).

### Sick Leave (Ziektewet)

**Sick Leave (Ziektewet)**

| Year | Employer Obligation | Minimum |
| --- | --- | --- |
| Year 1 (weeks 1--52) | 70% of salary | Must be topped up to at least minimum wage |
| Year 2 (weeks 53--104) | 70% of salary | No minimum wage floor in year 2 |

- **Sick leave employer obligations** — Employer bears the cost for up to 2 years (104 weeks). Many CAOs require 100% in year 1 and 70% in year 2. Employer must follow a reintegration plan (Wet verbetering poortwachter).  _(Wet verbetering poortwachter)_

### Maternity Leave (Zwangerschaps- en bevallingsverlof)

- **Maternity leave** — 16 weeks at 100% of daily wage (max dagloon), funded by UWV. Starts 4--6 weeks before expected delivery date.

### Partner/Paternity Leave (Geboorteverlof)

- **Partner/Paternity leave** — 1 week at 100% pay (employer-funded) + 5 additional weeks at 70% of daily wage (UWV-funded, taken within 6 months of birth).

### Transitievergoeding (Transition Payment on Dismissal)

- **Transition payment** — 1/3 of monthly salary per year of service. Applies to all terminations (employer-initiated or end of fixed-term contract).

## Section 7 -- Payslip Requirements

Employers must provide a payslip (loonstrook) the first time they pay the employee and whenever there is a change in pay or deductions. Under the WML, the payslip must include:

### Mandatory Payslip Contents

- **Mandatory payslip contents** — Employee name and period; Gross salary; Applicable minimum hourly wage for the employee's age; Itemised deductions (loonheffing, pension, etc.); Net salary; Number of hours worked (if variable); Overtime, holiday allowance, and other components separately stated; Name and address of employer  _(WML)_

### Recommended Additional Items

- **Recommended additional items** — Employer and employee pension contributions; Holiday days balance; Cumulative year-to-date figures; BSN (burger service nummer) reference; CAO reference

## Section 8 -- Filing Obligations

### Loonaangifte (Payroll Tax Return)

**Loonaangifte (Payroll Tax Return)**

| Item | Detail |
| --- | --- |
| Frequency | Per pay period (monthly for most employers) |
| Filing method | Electronically via Digipoort (payroll software) |
| Deadline | Last day of the month following the pay period |
| Content | Employee-level data: BSN, wages, loonheffing, premiums, days worked |

### Payment of Loonheffingen

**Payment of Loonheffingen**

| Item | Detail |
| --- | --- |
| Deadline | Same as filing: last day of following month |
| Method | Bank transfer to Belastingdienst |
| Reference | Betalingskenmerk from the tax return |

### Annual Obligations

**Annual Obligations**

| Task | Deadline |
| --- | --- |
| Jaaropgave (annual statement) to employees | Before 1 March |
| Correctie-berichten (corrections to prior returns) | Within 5 years |
| Pensioenfonds reporting | Per fund requirements |

### Penalties

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late filing / late payment | Up to 3% of payroll tax due (minimum EUR 50) |
| Incorrect or incomplete return | Fines up to EUR 5,514 per occurrence |
| Failure to withhold loonheffing | Employer liable for tax + possible criminal prosecution |
| Underpayment of minimum wage | Fine up to EUR 10,000 per employee per violation |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Standard Monthly Employee (Indefinite Contract)

Gross monthly salary EUR 4,000. Under AOW age. Loonheffingskorting applied.

1. Loonheffing: computed from tax tables (approx. 35.75% on first EUR 3,240/month minus heffingskorting)
2. ZVW werkgeversheffing: EUR 4,000 × 6.10% = EUR 244 (added to taxable wage, then employer cost)
3. Employer AWf low: EUR 4,000 × 2.74% = EUR 109.60
4. Employer Aof: EUR 4,000 × 6.27% = EUR 250.80
5. Pension: per fund; typical employee contribution 4--6% of pensionable salary

### Pattern 2 -- Temporary Contract Employee

Same gross but AWf high rate applies: EUR 4,000 × 7.74% = EUR 309.60. Employer cost difference: EUR 200/month higher vs permanent contract. This incentivises permanent contracts.

### Pattern 3 -- Holiday Allowance Payment (May)

Employee earns EUR 48,000/year. Vakantiegeld = EUR 48,000 × 8% = EUR 3,840. Paid in May as a separate component. Subject to loonheffing at the special table rate (bijzondere beloningen).

### Pattern 4 -- 30% Ruling Employee

Gross salary EUR 6,000/month. In 2026, 30% is the extraterritorial allowance = EUR 1,800 tax-free. Taxable wage = EUR 4,200. Loonheffing is calculated on EUR 4,200 only. The employee must meet the 2026 minimum salary requirement: EUR 48,013 taxable annual salary, or EUR 36,497 for an under-30 employee with a qualifying master degree.

### Pattern 5 -- Sick Employee (Week 1--52)

Employee earning EUR 3,500/month falls ill. Employer pays 70% = EUR 2,450. CAO requires 100% in year 1, so employer pays EUR 3,500. Employer must continue all social security premiums on the actual wage paid.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Dutch-specific rules |
| netherlands-bookkeeping | Payroll journals: gross salary + ER premiums to P&L; net pay + loonheffing + pension liabilities to BS |
| netherlands-vat | No BTW on salaries; but salary components that are payments in kind may trigger BTW |
| netherlands-einvoice | Payslips are not e-invoices but share employer identification requirements |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
