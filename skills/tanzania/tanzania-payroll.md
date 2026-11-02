---
name: tanzania-payroll
description: Use this skill whenever asked about Tanzania payroll processing for employed persons. Trigger on phrases like "Tanzania payroll", "PAYE Tanzania", "TRA PAYE", "NSSF contribution", "PSSSF", "SDL Tanzania", "Skills Development Levy", "WCF Tanzania", "Workers Compensation Fund", "ITX 300.01.E", "net salary Tanzania", "tax withholding Tanzania", "employer NSSF", "minimum wage Tanzania", "gross to net Tanzania", "salary calculation Tanzania", "TZS payroll", "Tanzanian Shilling salary", "non-resident PAYE Tanzania", "Zanzibar PAYE", or any question about computing employee pay, income-tax (PAYE) withholding, or social-security and payroll levies for Tanzania-based employees. This skill covers PAYE income-tax withholding by the employer, NSSF/PSSSF social security, the Skills Development Levy (SDL), the Workers Compensation Fund (WCF), minimum wage, and filing obligations to TRA / NSSF / WCF. ALWAYS read this skill before processing any Tanzania payroll.
jurisdiction: TZ
tax_year: 2026
last_updated: 2026-07-13
authored_by: Baraka Cassian, CPA, CA, CTA
reviewed_by: Baraka Cassian
review_status: current
trust_label: Checked by Baraka Cassian
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania Payroll

## Tanzania Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** A small number of figures carry `[RESEARCH GAP — reviewer to confirm]` markers (notably the full sectoral minimum-wage schedule, the floating late-payment interest rate, and any NSSF wage ceiling). A licensed Tanzanian tax practitioner / accountant must reconcile those before any output is presented as final.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Baraka Cassian** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### tanzania-payroll

- **PAYE band 1 - tax-free threshold (resident, monthly)** — 0% on taxable income TZS 0 - 270,000/month  _(Income Tax Act, Cap 332, s.81 & First Schedule)_
- **PAYE band 2 (resident, monthly)** — 8% of amount over TZS 270,000 (TZS 270,001 - 520,000)  _(Income Tax Act, Cap 332, First Schedule)_
- **PAYE band 3 (resident, monthly)** — TZS 20,000 + 20% of amount over TZS 520,000 (TZS 520,001 - 760,000)  _(Income Tax Act, Cap 332, First Schedule)_
- **PAYE band 4 (resident, monthly)** — TZS 68,000 + 25% of amount over TZS 760,000 (TZS 760,001 - 1,000,000)  _(Income Tax Act, Cap 332, First Schedule)_
- **PAYE band 5 - top rate (resident, monthly)** — TZS 128,000 + 30% of amount over TZS 1,000,000  _(Income Tax Act, Cap 332, First Schedule)_
- **PAYE annual tax-free threshold** — TZS 3,240,000 per annum (270,000 x 12)  _(Income Tax Act, Cap 332, First Schedule)_
- **Non-resident employee - employment income** — 15% flat, final tax  _(Income Tax Act, Cap 332, First Schedule (non-resident rate), read with s.81 (employer withholding))_
- **PAYE remittance deadline** — On or before the 7th day of the month following the month of deduction  _(Income Tax Act, Cap 332, s.84(1); Tax Administration Act, Cap 438)_
- **Employer half-year PAYE/SDL statement** — Semi-annual employer return due within 30 days after the end of each six-month calendar period  _(Income Tax Act, Cap 332, s.84(2))_
- **SDL rate (Mainland)** — 3.5% of total gross emoluments (payroll cash costs)  _(Vocational Education and Training Act, Cap 82, s.14 (as amended by Finance Act 2023))_
- **SDL employer threshold** — Applies only to employers with 10 or more employees  _(VETA Act, Cap 82 (as amended))_
- **SDL return filing where exempt** — Employers not liable to SDL are NOT required to file SDL returns  _(VETA Act, Cap 82 (as amended by Finance Act 2023))_
- **SDL rate (Zanzibar)** — 5% of gross emoluments  _(Zanzibar VETA legislation)_
- **SDL payment deadline** — With monthly PAYE, on or before the 7th day of the following month  _(VETA Act, Cap 82; Tax Administration Act, Cap 438)_
- **NSSF contribution (private sector)** — 20% of employee wages, joint employer/employee  _(NSSF Act, Cap 50, s.13)_
- **NSSF employee share cap** — Employee share may not exceed 10% of monthly wage (splits 10/10 or 15/5)  _(NSSF Act, Cap 50, s.13)_
- **WCF tariff** — 0.5% of cash sums paid to employees (wage bill); employer-only cost, monthly  _(Workers Compensation Act, Cap 263; Workers Compensation (Payment of Tariff) Regulations)_
- **HESLB loan deduction** — Employer deducts 15% of monthly salary of each HESLB loan beneficiary  _(Higher Education Students' Loans Board Act, Cap 178)_
- **Minimum wage instrument (private sector)** — Labour Institutions (Minimum Wage for Private Sector) Order 2025, GN 605A of 13 Oct 2025  _(Labour Institutions Act, Cap 300 - GN 605A of 2025)_
- **Minimum wage range (private sector)** — Sector-specific: from TZS 175,000/month (lowest agriculture band) to TZS 765,900/month (highest bands, e.g. international mining/energy)  _(GN 605A of 2025 sector schedules)_
- **Benefits in kind - general rule** — Taxable as employment income, generally at market value  _(Income Tax Act, Cap 332, s.7 read with s.27)_

**Car benefit - annual taxable values**  _(Income Tax Act, Cap 332, s.27(1)(b) quantification table)_

| Engine size | Annual taxable value |
| --- | --- |
| <=1000cc | TZS 250,000 |
| 1001-2000cc | 500,000 |
| 2001-3000cc | 1,000,000 |
| >3000cc | 1,500,000 |

- **Housing benefit quantification** — Lower of market rental value; and the higher of (i) 15% of employee's total annual income (excl. housing) and (ii) employer's expenditure claimed on the premises  _(Income Tax Act, Cap 332, s.27(1)(c))_
- **Preferential (low-interest) loan benefit** — Benefit = difference between BoT statutory rate and actual rate charged  _(Income Tax Act, Cap 332, s.27 (statutory rate per Bank of Tanzania))_
- **Employer statutory on-cost summary (private, SDL-liable)** — Approx. 14% on top of gross payroll: NSSF 10% + SDL 3.5% + WCF 0.5%  _(Derived from NSSF Act, VETA Act, WC Act)_

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | United Republic of Tanzania (Mainland; Zanzibar PAYE rates identical) |
| Currency | Tanzanian Shilling (TZS) only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) (PwC — Tax administration) |
| Income tax | YES — PAYE (Pay-As-You-Earn), progressive 0% / 8% / 20% / 25% / 30%, employer-withheld monthly (TRA; Income Tax Act, Cap. 332) |
| Non-resident employment income | Flat **15%** final tax on Tanzania-source employment income (PwC — Taxes on personal income) |
| Tax authority | TRA (Tanzania Revenue Authority) |
| Social security authority | NSSF (private sector) / PSSSF (public sector) |
| Payroll levies | SDL — Skills Development Levy (3.5%, employer-only, ≥10 staff); WCF — Workers Compensation Fund (0.5%, employer-only) |
| PAYE + SDL monthly deadline | **7th day of the following month** (TRA — SDL/PAYE) |
| NSSF monthly deadline | **Within one month of the salary month** (i.e. by end of the following month) (NSSF) |
| WCF monthly deadline | **Within the following month** (e.g. July contributions by 31 August) (WCF) |
| Annual individual return | Within **6 months of year-end**; estimate within 3 months of start of year of income (employment-only earners generally covered by PAYE) (TRA; PwC) |
| Key legislation | Income Tax Act (Cap. 332); NSSF Act; PSSSF Act; Vocational Education & Training Act (SDL); Workers Compensation Act |
| Payment form | **ITX 300.01.E — Employment Taxes Payment Credit Slip** (PAYE + SDL); **NSSF/CON.5** (NSSF schedule) |
| Filing portal | TRA online portal (IDRAS / e-filing); NSSF online; WCF online (www.wcf.go.tz) |
| Validated by | Pending -- requires sign-off by a licensed Tanzanian tax practitioner |
| Skill version | 0.1 |

> Figures verified against TRA, NSSF and WCF official sites and PwC Worldwide Tax Summaries
> (last reviewed 14 Jan 2026).

## Section 2 -- Income Tax Withholding (PAYE — Pay-As-You-Earn)

Tanzania **does** levy personal income tax on employees. The employer is the **withholding agent**: it deducts PAYE monthly from payroll and remits it to TRA by the **7th of the following month** using form **ITX 300.01.E** (TRA — SDL/PAYE). The brackets below are expressed on **MONTHLY taxable employment income in TZS**.

### PAYE Progressive Table — Monthly Taxable Income (resident, CONFIRMED)

**PAYE Progressive Table — Monthly Taxable Income (resident, CONFIRMED)**  _(TRA — Income tax for individuals (`tra.go.tz/page/income-tax-for-individuals`); PwC — Taxes on personal income)_

| Monthly taxable income (TZS) | Marginal rate | Tax (cumulative at top of band) |
| --- | --- | --- |
| 0 – 270,000 | **NIL** | TZS 0 |
| 270,001 – 520,000 | **8%** of excess over 270,000 | TZS 20,000 |
| 520,001 – 760,000 | **20%** of excess over 520,000 | 20,000 + 48,000 = TZS 68,000 |
| 760,001 – 1,000,000 | **25%** of excess over 760,000 | 68,000 + 60,000 = TZS 128,000 |
| Over 1,000,000 | **30%** of excess over 1,000,000 | — |

Note: the lowest taxed band is **8%** (a secondary calculator source that stated 9% is incorrect; TRA and PwC both confirm 8%).

- **Annual tax-free threshold** — TZS 3,240,000 (= 270,000 × 12)  _(TRA)_
- **Top marginal rate** — 30%  _(TRA; PwC)_
- **Zanzibar PAYE rates** — Zanzibar PAYE rates are identical to Mainland  _(PwC)_

**Subtract-method constants (resident)**

| Band (TZS) | Rate | Subtract (TZS) |
| --- | --- | --- |
| 270,001 – 520,000 | 8% | 21,600 |
| 520,001 – 760,000 | 20% | 84,000 |
| 760,001 – 1,000,000 | 25% | 122,000 |
| 1,000,001+ | 30% | 172,000 |

*Continuity check (subtract constants tie out to the cumulative column):*
- At 520,000 → 0.08 × 520,000 − 21,600 = 41,600 − 21,600 = **TZS 20,000**. Tie out.
- At 760,000 → 0.20 × 760,000 − 84,000 = 152,000 − 84,000 = **TZS 68,000**. Tie out.
- At 1,000,000 → 0.25 × 1,000,000 − 122,000 = 250,000 − 122,000 = **TZS 128,000**. Tie out.
- Band entry 1,000,001 → 0.30 × 1,000,001 − 172,000 = **TZS 128,000.30** ≈ continuous with 128,000. Tie out.

### Non-resident employment income

**Non-resident employment income table**

| Item | Detail | Source |
| --- | --- | --- |
| Non-resident PAYE | Flat **15%** on Tanzania-source employment income | PwC — Taxes on personal income |
| Nature | **Final tax** — no further individual return required | PwC |

### Withholding mechanism

- PAYE is **withheld monthly by the employer** from payroll and remitted to TRA by the **7th** of the following month on form **ITX 300.01.E** via the TRA online portal (TRA — SDL/PAYE).
- Annual: final individual return due within **6 months of year-end**; a statement of estimated tax is due within **3 months of the start of the year of income** (relevant for individuals with non-employment income) (PwC — Tax administration).

## Section 3 -- NSSF Social Security (Private Sector — Employee + Employer)

Private-sector employees contribute to the **National Social Security Fund (NSSF)**. The employer deducts, schedules and pays both the employer and employee shares (NSSF — Rate of contributions).

### NSSF Contribution (basis: gross monthly salary)

**NSSF Contribution (basis: gross monthly salary)**  _(NSSF — Rate of contributions; PwC — Other taxes)_

| Item | Total | Employer | Employee | Basis | Source |
| --- | --- | --- | --- | --- | --- |
| NSSF | **20%** | **10%** (≥ 10%) | **10%** (≤ 10%) | Gross monthly salary | NSSF — Rate of contributions; PwC — Other taxes |

- **Total contribution basis** — Total contribution is 20% of the employee's gross monthly salary, a joint employer/employee contribution  _(NSSF)_
- **Employee share cap and splits** — The employee's share must not exceed 10%; the employer covers at least 10%. The common arrangement is 10% / 10%. The employer may also pay the full 20%, or other splits (e.g. 15% employer / 5% employee) are permitted provided the employee share ≤ 10%  _(NSSF)_
- **No statutory wage ceiling/floor** — No statutory wage ceiling/floor is stated on the NSSF rate page — the contribution is a straight percentage of gross salary. [RESEARCH GAP — reviewer to confirm absence of an NSSF contribution ceiling with NSSF]
- **Filing form** — NSSF/CON.5 (schedule of contributing employees)  _(NSSF)_
- **NSSF deadline** — Remit within one month from the month of salary payment (i.e. by the end of the following month)  _(NSSF)_

*Column check (default split):* employer 10% + employee 10% = **20%** total. Tie out.

### PSSSF (Public Sector)

**PSSSF (Public Sector) table**  _(PwC — Other taxes)_

| Item | Total | Employer (typical) | Employee (typical) | Source |
| --- | --- | --- | --- | --- |
| PSSSF | **20%** | 15% | 5% | PwC — Other taxes |

- **PSSSF applicability** — The Public Service Social Security Fund (PSSSF) applies to public-sector employees, not the typical private employer. Same total 20%; the employer recovers up to 5% from the employee (i.e. employee 5% / employer 15% typical)  _(PwC)_

*Column check:* employer 15% + employee 5% = **20%** total. Tie out.

## Section 4 -- SDL — Skills Development Levy (Employer-only)

**SDL table**  _(TRA — Skills Development Levy; PwC — Other taxes)_

| Item | Rate | Who pays | Basis | Threshold | Source |
| --- | --- | --- | --- | --- | --- |
| SDL | **3.5%** | Employer only | Total gross cash emoluments for the month | Employers with **≥ 10 employees** | TRA — Skills Development Levy; PwC — Other taxes |

- **SDL basis clarification** — 3.5% of total gross cash emoluments paid to all employees in the month. (The authoritative TRA figure is 3.5%; some secondary sources stated 4% — TRA and PwC both confirm 3.5%.)  _(TRA)_
- **SDL headcount threshold** — Only employers with 10 or more employees are liable for SDL  _(TRA)_
- **SDL collection and form** — Collected by TRA; same payment form ITX 300.01.E  _(TRA)_
- **SDL deadline** — 7th day of the month following the payroll month (same as PAYE)  _(TRA)_

## Section 5 -- WCF — Workers Compensation Fund (Employer-only)

**WCF table**  _(WCF (`wcf.go.tz`); PwC — Other taxes)_

| Item | Rate | Who pays | Basis | Sector | Source |
| --- | --- | --- | --- | --- | --- |
| WCF | **0.5%** | Employer only | Monthly wage bill (gross employee earnings) | Private **and** public | WCF (`wcf.go.tz`); PwC — Other taxes |

- **WCF rate harmonisation** — 0.5% of the employer's monthly wage bill — the same rate now applies to both private and public sector (the previously differentiated 1% private / 0.5% public rates have been harmonised to 0.5%)  _(WCF)_
- **WCF filing** — Filed/paid online at www.wcf.go.tz  _(WCF)_
- **WCF deadline** — Monthly, payable within the month or the following month (e.g. July contributions by 31 August). Quarterly/semi-annual/annual schedules are possible with Director-General approval  _(WCF)_

## Section 6 -- Combined Employer / Employee Payroll Burden

For a **private employer with ≥ 10 employees** (so SDL applies), on a resident employee using the default NSSF 10%/10% split:

**Combined Employer / Employee Payroll Burden table**

| Item | Employee | Employer | Basis |
| --- | --- | --- | --- |
| PAYE | 0–30% progressive (withheld) | (withholding agent) | monthly taxable income |
| NSSF | 10% | 10% | gross |
| SDL | — | 3.5% | total gross emoluments (≥ 10 staff) |
| WCF | — | 0.5% | gross wage bill |

- **Employer on-cost above gross salary** — 10% (NSSF) + 3.5% (SDL) + 0.5% (WCF) = 14% of gross for employers with ≥ 10 staff
- **Fewer than 10 employees on-cost** — If the employer has fewer than 10 employees, SDL does not apply. The employer on-cost is then NSSF 10% + WCF 0.5% = 10.5% of gross. PAYE and NSSF still apply in full.

## Section 7 -- Minimum Wage (Private Sector)

Tanzania has **no single national minimum wage** — minimum wages are **sectoral**.

**Minimum wage instrument/structure table**  _(TanzLII (GN 605A/2025); PKF; VELMA Law)_

| Item | Detail | Source |
| --- | --- | --- |
| Current order | **Labour Institutions (Minimum Wage for Private Sector) Order, 2025 (GN 605A/2025)**, in force **from 1 January 2026**; replaces the 2022 order | TanzLII (GN 605A/2025); PKF; VELMA Law |
| Structure | **16 sectors / 46 sub-sectors** regulated; average increase 33.4% vs the 2022 order | PKF; VELMA Law |

### Representative sectoral minimum wages (TZS/month)

**Representative sectoral minimum wages (TZS/month)**  _(PKF; VELMA Law)_

| Sector (example) | Monthly minimum (TZS) | Source |
| --- | --- | --- |
| Default / unspecified sectors | 175,000 | PKF; VELMA Law |
| Agriculture (crop / animal) | 175,000 | PKF; VELMA Law |
| Domestic workers | 80,000 | PKF; VELMA Law |
| Fishing / aquaculture | 300,000 | PKF; VELMA Law |
| 4-/5-star hotels | 375,000 | PKF; VELMA Law |
| Telecommunications | 644,000 | PKF; VELMA Law |
| International mining / energy | up to ~765,900 | PKF; VELMA Law |

> **[RESEARCH GAP — reviewer to confirm]** The full **46-sub-sector** schedule could not be extracted from a single authoritative source. The figures above are **representative**; the complete schedule must be pulled from the **TanzLII gazette (GN 605A/2025)** before being treated as final. Always use the employee's specific sub-sector rate.

## Section 8 -- Conservative Defaults

**Conservative Defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Residency status | Assume **resident** (progressive table) only if confirmed; if status unknown, FLAG | Non-resident is flat 15% final — materially different |
| NSSF split | Use **10% employee / 10% employer** | Default; employee share capped at 10% |
| Headcount unknown (for SDL) | Compute **without** SDL but FLAG; never silently apply 3.5% | SDL applies only at ≥ 10 employees |
| Headcount ≥ 10 confirmed | Apply **SDL 3.5%** (employer) | Statutory once threshold met |
| Public vs private sector | Default **private** (NSSF + SDL + WCF); switch to PSSSF if public | PSSSF only for public-sector staff |
| NSSF wage ceiling | Apply 20% on **full gross** (no cap) and FLAG | No ceiling found on the NSSF rate page |
| Tax year | Default to **2026** brackets/rates | Skill tax_year is 2026 |
| Currency | Tanzanian Shilling (TZS) | Local currency |
| Minimum-wage sub-sector unknown | Do NOT pick a figure — request the sub-sector and use GN 605A/2025 | Sectoral; no national floor |

When an input is missing or ambiguous, apply the **conservative** assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

### Required inputs before computing payroll

1. Gross monthly salary in TZS (and any non-cash/benefit components).
2. **Residency status** (resident → progressive; non-resident → flat 15% final).
3. Sector / sub-sector (drives the minimum-wage check under GN 605A/2025).
4. **Number of employees** on the payroll (drives SDL liability at ≥ 10).
5. Whether the employer is **private (NSSF)** or **public (PSSSF)**.
6. NSSF split if non-standard (employer may pay full 20%; employee share ≤ 10%).
7. Tax/fiscal year (2026 vs later schedules).
8. Pay frequency.

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE — request salary in TZS |
| Residency status unknown | REFUSE — resident vs non-resident changes PAYE entirely (progressive vs flat 15%) |
| Request to omit PAYE, NSSF, SDL or WCF to "save money" | REFUSE — statutory; escalate to accountant |
| Request to apply SDL where headcount is < 10 | REFUSE — SDL only applies at ≥ 10 employees |
| Request to apply SDL at 4% | REFUSE — TRA-confirmed rate is 3.5% |
| Request to set an exact minimum-wage figure without the sub-sector | REFUSE — sectoral; request sub-sector and use GN 605A/2025 |
| Self-employed / non-employment income mixed in | REFUSE payroll path — route to a Tanzania income-tax skill (annual return) |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |

## Section 10 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins. Tanzanian statements appear in **English and Kiswahili**.

### Salary credits (money arriving in an employee account)

**Salary credits table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARY`, `MSHAHARA`, `MISHAHARA`, `PAYROLL`, `NET PAY` | Net salary payment |
| `MALIPO YA MSHAHARA`, `WAGE`, `TRANSF.* [employer]` | Net salary payment |
| `NSSF REFUND`, `MAREJESHO NSSF` | NSSF refund/adjustment — not income |
| `TRA REFUND`, `PAYE REFUND` | PAYE refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `TRA`, `PAYE`, `ITX 300`, `KODI`, `WITHHOLDING TAX` | PAYE withholding remitted to TRA (ITX 300.01.E) |
| `SDL`, `SKILLS DEVELOPMENT LEVY`, `TOZO YA UJUZI` | Skills Development Levy remitted to TRA (3.5%, ≥ 10 staff) |
| `NSSF`, `MICHANGO NSSF`, `CON.5`, `PENSION` | NSSF contribution (employer + employee shares) |
| `PSSSF` | PSSSF contribution (public-sector) |
| `WCF`, `FIDIA YA WAFANYAKAZI`, `WORKERS COMPENSATION` | Workers Compensation Fund (0.5%, employer-only) |
| `NET WAGES`, `MALIPO YA MISHAHARA`, `SALARY RUN`, `DISBURSEMENT` | Net wages disbursed to employees |

## Section 11 -- Worked Examples

> All figures use the **2026** resident PAYE table and 2026 contribution rates. Default NSSF split is 10% employee / 10% employer. SDL (3.5%) is shown only where the employer has ≥ 10 staff. WCF (0.5%) and SDL are employer-only and do **not** reduce employee net pay. Amounts rounded to the shilling.

### Example 1 — Low earner below the PAYE threshold

**Inputs:** Gross salary TZS 250,000/month. Resident. NSSF 10%/10%.

- PAYE: 250,000 ≤ 270,000 → **TZS 0**.
- NSSF employee 10% × 250,000 = **TZS 25,000**.
- **Employee deductions total** = 0 + 25,000 = **TZS 25,000**.
- **Net pay** = 250,000 − 25,000 = **TZS 225,000**.

*Bank line example:* `MSHAHARA — JANUARY` credit **TZS 225,000**.

### Example 2 — Earner in the 8% PAYE band

**Inputs:** Gross salary TZS 400,000/month. Resident. NSSF 10%/10%.

- PAYE: 400,000 in 8% band → 0.08 × 400,000 − 21,600 = 32,000 − 21,600 = **TZS 10,400**.
  - Verify by band: 0.08 × (400,000 − 270,000) = 0.08 × 130,000 = **10,400**. Tie out.
- NSSF employee 10% × 400,000 = **TZS 40,000**.
- **Employee deductions total** = 10,400 + 40,000 = **TZS 50,400**.
- **Net pay** = 400,000 − 50,400 = **TZS 349,600**.

### Example 3 — Mid earner in the 20% PAYE band

**Inputs:** Gross salary TZS 700,000/month. Resident. NSSF 10%/10%.

- PAYE: 700,000 in 20% band → 0.20 × 700,000 − 84,000 = 140,000 − 84,000 = **TZS 56,000**.
  - Verify by bands: 20,000 (up to 520k) + 0.20 × (700,000 − 520,000) = 20,000 + 36,000 = **56,000**. Tie out.
- NSSF employee 10% × 700,000 = **TZS 70,000**.
- **Employee deductions total** = 56,000 + 70,000 = **TZS 126,000**.
- **Net pay** = 700,000 − 126,000 = **TZS 574,000**.

### Example 4 — Higher earner in the 30% PAYE band

**Inputs:** Gross salary TZS 1,500,000/month. Resident. NSSF 10%/10%.

- PAYE: 1,500,000 in 30% band → 0.30 × 1,500,000 − 172,000 = 450,000 − 172,000 = **TZS 278,000**.
  - Verify by bands: 128,000 (up to 1,000k) + 0.30 × (1,500,000 − 1,000,000) = 128,000 + 150,000 = **278,000**. Tie out.
- NSSF employee 10% × 1,500,000 = **TZS 150,000**.
- **Employee deductions total** = 278,000 + 150,000 = **TZS 428,000**.
- **Net pay** = 1,500,000 − 428,000 = **TZS 1,072,000**.

### Example 5 — Employer total cost of the mid earner (TZS 700,000, ≥ 10 staff)

Building on Example 3 (gross TZS 700,000), private employer with ≥ 10 employees:

**Employer cost table**

| Employer cost item | Computation | Amount (TZS) |
| --- | --- | --- |
| Gross salary | — | 700,000 |
| NSSF employer 10% | 10% × 700,000 | 70,000 |
| SDL 3.5% | 3.5% × 700,000 | 24,500 |
| WCF 0.5% | 0.5% × 700,000 | 3,500 |
| **Total employer cost** | sum | **798,000** |

*Check:* 700,000 + 70,000 + 24,500 + 3,500 = **798,000**. Tie out.
(Employer-on-top burden = TZS 98,000 = **14%** of gross.)

### Example 6 — Non-resident employee (flat 15% final)

**Inputs:** Non-resident, Tanzania-source employment income TZS 700,000/month.

- PAYE = flat **15% × 700,000 = TZS 105,000** (final tax; no further return).
- Net of PAYE = 700,000 − 105,000 = **TZS 595,000**.

> NSSF may still apply to a non-resident working in Tanzania depending on the engagement; the **15% PAYE is a final income-tax**, separate from any social-security liability. Confirm NSSF applicability for the specific contract with the reviewer.

## Section 12 -- Tier 1 Rules (hard, non-negotiable)

- **Rule 1** — PAYE is employer-withheld monthly and remitted to TRA by the 7th of the following month on ITX 300.01.E; never skip it for salaried staff  _(TRA)_
- **Rule 2** — Use the monthly resident taxable-income table and apply the subtract-method constants exactly (21,600 / 84,000 / 122,000 / 172,000). The lowest taxed band is 8%, not 9%.
- **Rule 3** — Non-residents pay a flat 15% final tax on Tanzania-source employment income — never apply the progressive table to a confirmed non-resident  _(PwC)_
- **Rule 4** — NSSF is 20% total (default 10%/10%); the employee share must not exceed 10%  _(NSSF)_
- **Rule 5** — SDL (3.5%) is employer-only and applies only at ≥ 10 employees; the rate is 3.5%, not 4%  _(TRA)_
- **Rule 6** — WCF (0.5%) is employer-only and applies to both private and public sector  _(WCF)_
- **Rule 7** — PAYE + SDL share the 7th-of-next-month deadline; NSSF and WCF are due within the following month  _(TRA; NSSF; WCF)_
- **Rule 8** — Minimum wage is sectoral under GN 605A/2025 (in force 1 Jan 2026) — there is no national floor; use the employee's sub-sector rate
- **Rule 9** — Every output is an estimate pending licensed-accountant sign-off

## Section 13 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Question | Why it needs a reviewer |
| --- | --- |
| Full 46-sub-sector minimum-wage schedule (GN 605A/2025) | Only representative figures extracted; full list needs the gazette text |
| Existence of an NSSF contribution ceiling | None found on the NSSF rate page; confirm explicitly with NSSF |
| Late-payment interest rate | Floats with the Bank of Tanzania discount rate (compounded); no fixed % published |
| Non-resident NSSF liability | Depends on the specific contract / secondment arrangement |
| Non-standard NSSF splits (e.g. 15%/5%, employer pays full 20%) | Permitted provided employee share ≤ 10%; depends on employer policy |
| Treatment of benefits in kind / allowances in the PAYE and NSSF base | Edge cases not fully nailed from primary sources |

## Section 14 -- Excel Working Paper Template

Suggested layout (one row per employee per month):

**Excel Working Paper Template table**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross monthly salary (TZS) | input |
| C | Resident? (Y/N) | input |
| D | Headcount ≥ 10? (Y/N) | input (drives SDL) |
| E | PAYE (monthly) | resident: nested IF on B (subtract constants); non-resident: `=B*15%` |
| F | NSSF employee | `=B*10%` |
| G | Employee deductions | `=E+F` |
| H | Net pay | `=B-G` |
| I | NSSF employer | `=B*10%` |
| J | SDL (employer) | `=IF(D="Y", B*3.5%, 0)` |
| K | WCF (employer) | `=B*0.5%` |
| L | Total employer cost | `=B+I+J+K` |

- **Resident PAYE formula for column E (2026, monthly)** — =IF(B<=270000,0, IF(B<=520000, B*0.08-21600, IF(B<=760000, B*0.20-84000, IF(B<=1000000, B*0.25-122000, B*0.30-172000))))
- **Non-resident PAYE formula** — =B*0.15 (flat, final)

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology guide table**

| Term (English / Kiswahili) | Meaning |
| --- | --- |
| Salary / Mshahara (pl. Mishahara) | Salary / wage |
| Malipo ya mshahara | Salary payment |
| PAYE | Pay-As-You-Earn income-tax withholding |
| TRA (Tanzania Revenue Authority) / Mamlaka ya Mapato Tanzania | Tax authority |
| Kodi | Tax |
| ITX 300.01.E | Employment Taxes Payment Credit Slip (PAYE + SDL) |
| NSSF / Mfuko wa Hifadhi ya Jamii | National Social Security Fund (private sector) |
| PSSSF | Public Service Social Security Fund (public sector) |
| NSSF/CON.5 | NSSF schedule of contributing employees |
| SDL / Tozo ya Maendeleo ya Ujuzi | Skills Development Levy (3.5%, employer-only, ≥ 10 staff) |
| WCF / Mfuko wa Fidia kwa Wafanyakazi | Workers Compensation Fund (0.5%, employer-only) |
| Net pay / Malipo halisi | Take-home pay after deductions |
| Mkazi / Asiye mkazi | Resident / non-resident (15% flat final PAYE) |

## Section 16 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of payroll and TRA/NSSF/WCF receipts to back-solve the rates actually applied.
2. **Unknown residency** → do not compute PAYE; confirm resident vs non-resident first (progressive vs flat 15% final).
3. **Unknown headcount** → default SDL OFF, FLAG; confirm before the first remittance (SDL at ≥ 10).
4. **Unknown sector** → do not assert a minimum wage; request the sub-sector and check GN 605A/2025.
5. **Year ambiguity** → default 2026 table/rates; switch only for periods in a later year of income.
6. **Public vs private** → confirm; PSSSF (public) vs NSSF (private) change the contribution path.

## Section 17 -- Filing, Forms & Deadlines

**Filing, Forms & Deadlines table**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | PwC — Tax administration |
| PAYE | Withheld and remitted to TRA **monthly**, by the **7th** of the following month, on **ITX 300.01.E** via the TRA online portal (IDRAS) | TRA — SDL/PAYE; PwC |
| SDL | Paid to TRA **monthly**, by the **7th** of the following month, on **ITX 300.01.E** (employers with ≥ 10 employees) | TRA — Skills Development Levy |
| NSSF | Declared on **NSSF/CON.5** and paid **within one month** of the salary month | NSSF — Rate of contributions |
| WCF | Paid online (`wcf.go.tz`) **within the following month** (e.g. July → by 31 August); other schedules with DG approval | WCF |
| Annual individual return | Within **6 months of year-end**; estimate within **3 months of start of year of income** | PwC — Tax administration |
| Registration | Any person conducting business must register with TRA and obtain a **TIN**; PAYE/withholding registration is part of business registration | TRA |

## Section 18 -- Penalties & Interest

Governed by TRA rules (TRA — Interest, penalties & offences).

**Penalties & Interest table**

| Item | Detail | Source |
| --- | --- | --- |
| Currency point | **TZS 20,000** (official TRA value) | TRA |
| Interest on late payment of tax | Charged at the **statutory rate = Bank of Tanzania discount rate, compounded** (variable; TRA publishes no fixed %) | TRA |
| Failure to file return / pay on time | Per month (or part-month) the failure continues: the **higher of** (a) **2.5%** of tax assessed less tax already paid, or (b) **5 currency points (TZS 100,000)** for an individual / **15 currency points (TZS 300,000)** for a body corporate | TRA; PwC — Tax administration |

> **[RESEARCH GAP — reviewer to confirm]** The exact interest percentage is **not** a fixed figure — it floats with the Bank of Tanzania discount rate and is compounded. Confirm the current statutory rate at the relevant date with TRA before quoting any number.

## Section 19 -- Reference Material

**Reference Material table**

| Topic | Figure | Source |
| --- | --- | --- |
| PAYE NIL band | 0 – 270,000 TZS/month (annual TZS 3,240,000) | TRA; PwC |
| PAYE bands | 8% / 20% / 25% / 30% at 520k / 760k / 1,000k edges | TRA; PwC (Income Tax Act Cap. 332) |
| Non-resident PAYE | 15% flat, final | PwC |
| NSSF | 20% total (default 10% ee / 10% er), gross; employee share ≤ 10% | NSSF; PwC |
| PSSSF (public) | 20% total (typical 5% ee / 15% er) | PwC |
| SDL | 3.5% employer-only, total gross emoluments, ≥ 10 employees | TRA; PwC |
| WCF | 0.5% employer-only, gross wage bill, both sectors | WCF; PwC |
| PAYE / SDL deadline | 7th of following month (ITX 300.01.E) | TRA |
| NSSF deadline | Within one month of salary month (NSSF/CON.5) | NSSF |
| WCF deadline | Within the following month | WCF |
| Annual return | Within 6 months of year-end | PwC |
| Currency point | TZS 20,000 | TRA |
| Minimum wage | Sectoral (GN 605A/2025, in force 1 Jan 2026); no national floor | TanzLII; PKF; VELMA Law |

Key authorities: TRA (`tra.go.tz`, IDRAS / online portal), NSSF (`nssf.go.tz`), WCF (`wcf.go.tz`), TanzLII (gazette GN 605A/2025). Big-4/secondary: PwC Worldwide Tax Summaries (individual + corporate other taxes), PKF, VELMA Law.

## Section 20 -- Test Suite

Each test recomputes end-to-end. Expected values use the 2026 resident PAYE table and 2026 rates
(NSSF 10%/10%).

- **Test 1 - Sub-threshold earner** — Gross TZS 250,000/mo, resident. Expected: PAYE = TZS 0; NSSF employee TZS 25,000; net TZS 225,000.  _(Section 20 -- Test Suite)_
- **Test 2 - 8% band** — Gross TZS 400,000/mo, resident. PAYE TZS 10,400; NSSF employee TZS 40,000; net TZS 349,600.  _(Section 20 -- Test Suite)_
- **Test 3 - 20% band** — Gross TZS 700,000/mo, resident. PAYE TZS 56,000; NSSF employee TZS 70,000; net TZS 574,000.  _(Section 20 -- Test Suite)_
- **Test 4 - 30% band** — Gross TZS 1,500,000/mo, resident. PAYE TZS 278,000; NSSF employee TZS 150,000; net TZS 1,072,000.  _(Section 20 -- Test Suite)_
- **Test 5 - Employer cost** — Gross TZS 700,000/mo, ≥ 10 staff. NSSF employer TZS 70,000; SDL TZS 24,500; WCF TZS 3,500; total employer cost TZS 798,000 (burden 14% of gross).  _(Section 20 -- Test Suite)_
- **Test 6 - Non-resident** — TZS 700,000/mo Tanzania-source. PAYE = TZS 105,000 (15% flat, final); net of PAYE TZS 595,000.  _(Section 20 -- Test Suite)_
- **Test 7 - Bracket continuity** — At monthly 520,000 → PAYE TZS 20,000; at 760,000 → PAYE TZS 68,000; at 1,000,000 → PAYE TZS 128,000 (subtract constants 21,600 / 84,000 / 122,000 / 172,000 tie out).  _(Section 20 -- Test Suite)_
- **Test 8 - SDL threshold guard** — An employer with 9 employees computing SDL is WRONG — SDL applies only at ≥ 10. With ≥ 10 it is 3.5%, never 4%.  _(Section 20 -- Test Suite)_
- **Test 9 - Rate guard** — Applying 9% as the lowest taxed band is WRONG — the lowest taxed band is 8%.  _(Section 20 -- Test Suite)_
- **Test 10 - Minimum-wage refusal** — Asserting a single national minimum wage → REFUSE; minimum wage is sectoral (GN 605A/2025) — request the sub-sector.  _(GN 605A/2025)_

## PROHIBITIONS

- **PAYE withholding obligation** — NEVER skip PAYE withholding for salaried employees — the employer is the legal withholding agent.  _(PROHIBITIONS)_
- **Lowest band rate guard** — NEVER apply the 9% lowest band — the TRA-confirmed lowest taxed band is 8%.  _(PROHIBITIONS)_
- **Non-resident flat rate rule** — NEVER apply the resident progressive table to a confirmed non-resident — they pay a flat 15% final.  _(PROHIBITIONS)_
- **SDL applicability and rate** — NEVER apply SDL where the employer has fewer than 10 employees, and NEVER use 4% — SDL is 3.5%.  _(PROHIBITIONS)_
- **NSSF employee share cap** — NEVER let the employee NSSF share exceed 10% — the employee share is capped at 10% (total 20%).  _(PROHIBITIONS)_
- **WCF/SDL employer-only** — NEVER treat WCF or SDL as employee deductions — both are employer-only.  _(PROHIBITIONS)_
- **NSSF wage ceiling assumption** — NEVER assume an NSSF wage ceiling without confirming one exists — none was found in the sources.  _(PROHIBITIONS)_
- **Minimum wage sectoral rule** — NEVER assert a single national minimum wage — it is sectoral under GN 605A/2025; use the sub-sector rate.  _(PROHIBITIONS)_
- **Late-payment interest floating rate** — NEVER quote a fixed late-payment interest percentage — it floats with the Bank of Tanzania discount rate.  _(PROHIBITIONS)_
- **Estimated computation disclaimer requirement** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Tanzanian accountant.  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax practitioner in Tanzania) before implementation.

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
