---
name: fiji-payroll
description: Use this skill whenever asked about Fiji payroll processing for employed persons. Trigger on phrases like "Fiji payroll", "PAYE Fiji", "FNPF contribution", "Fiji National Provident Fund", "SRT Fiji", "Social Responsibility Tax", "ECAL Fiji", "Environment Climate Adaptation Levy", "FRCS PAYE", "tax withholding Fiji", "employer FNPF", "net salary Fiji", "minimum wage Fiji", "salary calculation Fiji", "gross to net Fiji", "TPOS Fiji", "FJD payroll", or any question about computing employee pay, withholding tax (PAYE/SRT/ECAL), or FNPF social contributions for Fiji-based employees. This skill covers PAYE income tax withholding (a final tax for employment-only income), Social Responsibility Tax, the Environment & Climate Adaptation Levy, FNPF employee and employer contributions, the national minimum wage, non-resident taxation, and FRCS/FNPF filing obligations. ALWAYS read this skill before processing any Fiji payroll.
jurisdiction: FJ
domain: payroll
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# fiji-payroll

## Fiji Payroll Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Fiji |
| Currency | FJD only (Fijian Dollar, $) |
| Standard pay frequency | Monthly or fortnightly (weekly permitted) |
| Tax year | Calendar year (1 January -- 31 December) [FRCS] |
| Tax withholding system | PAYE -- final withholding tax for employment-only income [FRCS, "New PAYE Structure" public notice] |
| Income tax authority | Fiji Revenue & Customs Service (FRCS) -- https://frcs.org.fj |
| Social contribution authority | Fiji National Provident Fund (FNPF) -- https://myfnpf.com.fj |
| Labour authority | Ministry of Employment, Productivity & Industrial Relations (MEPIR) |
| Key legislation | Income Tax Act 2015; Tax Administration Act 2009; Fiji National Provident Fund Act 2011; Employment Relations Act 2007 |
| Filing portal | FRCS Taxpayer Online Services (TPOS) |
| Has personal income tax? | YES -- collected via PAYE as a final tax |
| Validated by | Pending -- requires sign-off by a Fiji-licensed accountant |
| Skill version | 0.1 |

### Statutory Payroll Components at a Glance (resident employee)

**Statutory Payroll Components at a Glance**

| Component | Employee | Employer | Base / threshold |
| --- | --- | --- | --- |
| Income tax (PAYE) | 0% -- 20% progressive | withhold & remit | tax-free to $30,000; 20% marginal cap [FRCS Tax Rates] |
| Social Responsibility Tax (SRT) | 18% -- 24% | withhold & remit | only chargeable income > $270,000 [FRCS Tax Rates] |
| Environment & Climate Adaptation Levy (ECAL) on income | 10% | withhold & remit | only chargeable income > $270,000 [HLB Fiji; **[RESEARCH GAP — reviewer to confirm against live FRCS ECAL page]**] |
| FNPF | 8% | 10% | gross ordinary wages, no cap [FNPF Employers, eff. 1 Jan 2024] |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- ask. Non-residents have NO tax-free threshold (flat 20%) |
| Unknown whether income exceeds $270,000 | Treat as below $270,000 (no SRT/ECAL) and flag to reviewer if near threshold |
| Unknown FNPF membership / age | Treat employee aged 15+ as FNPF-mandatory; STOP if under 15 |
| Unknown whether figure is "ordinary wages" vs total remuneration | Use ordinary/gross wages for FNPF; STOP if composition unclear |
| Unknown pay frequency | Assume monthly; annualise for bracket computation |
| Voluntary FNPF top-ups | Assume none unless evidenced |
| Sector minimum wage applies | STOP -- check for a Wages Regulation Order before assuming national minimum |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — gross (ordinary) wages for the period, pay frequency, residency status (resident / non-resident), and confirmation the employee is an FNPF member (or eligible, aged 15+).
- **Recommended inputs** — annualised gross, FNPF member number, FRCS Tax Identification Number (TIN), employment start date, age, and any voluntary FNPF election.
- **Ideal inputs** — full payslip history for the year (for cumulative PAYE reconciliation), employment contract showing ordinary wage vs allowances, sector/industry (to check Wages Regulation Orders), and bank statements showing salary credits and statutory remittances.

### Refusal Catalogue

- **R-FJ-1 -- Residency unknown** — Resident employees get a $30,000 tax-free threshold; non-residents are taxed at a flat 20% from the first dollar [FRCS]. Confirm residency status before computing PAYE.  _(FRCS)_
- **R-FJ-2 -- High-earner thresholds** — SRT and ECAL on income apply only above $270,000 chargeable income [FRCS Tax Rates; HLB Fiji]. If annual chargeable income is at or near $270,000, escalate to a licensed accountant — the stacked PAYE + SRT + ECAL computation must be reviewed.  _(FRCS Tax Rates; HLB Fiji)_
- **R-FJ-3 -- ECAL provenance** — The ECAL-on-income rate (10% above $270,000) could not be confirmed verbatim from the live FRCS ECAL page during research [RESEARCH GAP]. Do not present ECAL figures as definitive — flag for reviewer confirmation.
- **R-FJ-4 -- Penalty figures** — Specific FRCS PAYE penalties and the FNPF late-payment penalty rate were not confirmed from primary sources [RESEARCH GAP]. Do not state exact penalty amounts — refer to 'penalties under the Tax Administration Act 2009 / FNPF Act 2011' and escalate.
- **R-FJ-5 -- Termination / final pay / redundancy** — Termination pay, redundancy, and leave-on-termination computations are outside this skill's scope. Escalate to a licensed accountant.
- **R-FJ-6 -- Fringe benefits / non-cash remuneration** — Fringe benefit tax and the taxation of non-cash benefits are outside this skill's scope. Escalate to a licensed accountant.

## Section 3 -- PAYE Income Tax Withholding (Residents)

- **PAYE deduction and final tax rule** — The employer deducts PAYE each pay period using the FRCS tax tables / the 2024 PAYE Regulation 6 formula and an approved calculator/Excel filing template [FRCS]. PAYE is a final tax for employees whose only income is employment income — those employees do not file an annual return [FRCS, "New PAYE Structure" notice].  _(FRCS, "New PAYE Structure" notice)_

### 3.1 Resident PAYE Brackets (current, YA 2022 onward; unchanged 2024/2025) [FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/]

**Resident PAYE Brackets**  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/)_

| Chargeable income (FJD) | Income tax |
| --- | --- |
| 0 -- 30,000 | Nil (tax-free threshold = $30,000) |
| 30,001 -- 50,000 | 18% of excess over $30,000 |
| 50,001 -- 270,000 | $3,600 + 20% of excess over $50,000 |
| 270,001 -- 300,000 | $47,600 + 20% of excess over $270,000 |
| 300,001 -- 350,000 | $53,600 + 20% of excess over $300,000 |
| 350,001 -- 400,000 | $63,600 + 20% of excess over $300,000 |
| 400,001 -- 450,000 | $73,600 + 20% of excess over $400,000 |
| 450,001 -- 500,000 | $83,600 + 20% of excess over $450,000 |
| 500,001 -- 1,000,000 | $93,600 + 20% of excess over $500,000 |
| 1,000,001+ | $193,600 + 20% of excess over $1,000,000 |

- **Top income-tax marginal rate** — The top income-tax marginal rate is 20%. Above $270,000, SRT (Section 4) and ECAL (Section 5) stack on top.  _(FRCS Tax Rates)_

Bracket discrepancy note: A secondary FRCS public-notice summary ("New PAYE Structure") describes the bands above $270,000 with combined rates like 33%/39% — these reflect the combined PAYE + SRT marginal rate after SRT was integrated into PAYE for administration. The FRCS Tax Rates page shows the components separately (20% income tax + the SRT schedule). This skill treats income tax (20% cap) and SRT as separate stacked components per the Tax Rates page. The combined effective top marginal rate is ~44% (20% + 24%) on income over $1M.

### 3.2 Computation Method

- **PAYE computation method** — Annual income tax = bracket base + (rate × (chargeable income − bracket floor)) Period PAYE        = annual income tax ÷ number of pay periods (cumulatively adjusted)  _(FRCS)_
- **Tax-free threshold as personal allowance** — PAYE is computed on annualised chargeable income, divided across pay periods, and trued up cumulatively over the year via the FRCS PAYE formula. The $30,000 tax-free threshold IS the personal allowance — there is no separate allowance.  _(FRCS)_

## Section 4 -- Social Responsibility Tax (SRT) -- High Earners Only

- **SRT applicability** — SRT applies only to chargeable income above $270,000 and is collected through PAYE for employees [FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/].  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/)_

**SRT bracket table**  _(FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/)_

| Chargeable income (FJD) | SRT |
| --- | --- |
| 0 -- 270,000 | Nil |
| 270,001 -- 300,000 | 18% of excess over $270,000 |
| 300,001 -- 350,000 | $5,400 + 19% of excess over $300,000 |
| 350,001 -- 400,000 | $14,900 + 20% of excess over $350,000 |
| 400,001 -- 450,000 | $24,900 + 21% of excess over $400,000 |
| 450,001 -- 500,000 | $35,400 + 22% of excess over $450,000 |
| 500,001 -- 1,000,000 | $46,400 + 23% of excess over $500,000 |
| 1,000,001+ | $161,400 + 24% of excess over $1,000,000 |

## Section 5 -- Environment & Climate Adaptation Levy (ECAL) on Income

- **ECAL rate on income** — 10% on chargeable income exceeding $270,000 — the same high-earner band as SRT, in addition to income tax and SRT. Collected via PAYE for employees.  _(HLB Fiji -- https://www.hlbfiji.com/an-introduction-to-environmental-climate-and-adaptation-levy-ecal/)_
- **ECAL on income formula** — ECAL on income = 10% × (chargeable income − $270,000), where chargeable income > $270,000  _(HLB Fiji -- https://www.hlbfiji.com/an-introduction-to-environmental-climate-and-adaptation-levy-ecal/)_

[RESEARCH GAP — reviewer to confirm] The primary FRCS ECAL page returned a 404 during research. The 10%-above-$270,000 figure is corroborated by HLB Fiji and multiple secondary sources but was not timestamped against the live FRCS page for 2025. Confirm before publishing as definitive.

Note: ECAL also separately applies as 10% on prescribed-service businesses and certain luxury items — these are not payroll-relevant and are out of scope here.

## Section 6 -- Non-Resident Employees

**Non-resident rules table**

| Rule | Detail | Source |
| --- | --- | --- |
| PAYE rate | Flat **20% from the first dollar** of chargeable income — NO $30,000 tax-free threshold | FRCS personal income tax materials |
| SRT | Applies above $270,000 as for residents | FRCS Tax Rates |
| ECAL on income | Applies above $270,000 as for residents | HLB Fiji **[RESEARCH GAP]** |
| FNPF | FNPF covers employees working in Fiji; applicability to short-term non-resident assignees **[RESEARCH GAP — reviewer to confirm coverage rules for non-residents]** | FNPF Act 2011 |

## Section 7 -- FNPF -- Mandatory Social / Pension Contributions

- **FNPF effective date** — FNPF is the primary mandatory social contribution. Rates are effective 1 January 2024 and confirmed current for 2025.  _(FNPF "Employers" -- https://myfnpf.com.fj/employers/)_

### 7.1 Contribution Rates

**Contribution Rates table**

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 8% | gross / ordinary wages |
| Employer | 10% | gross / ordinary wages |
| **Total compulsory** | **18%** |  |

Arithmetic check: 8% (employee) + 10% (employer) = 18% total. ✓

### 7.2 Rules

**FNPF Rules table**

| Rule | Detail | Source |
| --- | --- | --- |
| Ceiling / cap | NONE — contributions on full ordinary wages | FNPF Employers |
| Minimum floor | None stated by FNPF — contributions on actual wages | FNPF Employers |
| Voluntary top-ups | Employer may pay voluntary additional contributions above the mandated 10% | FNPF Employers |
| Coverage | Employers must register all employees aged 15+ not already members (Registration of Employee Form) | FNPF Employers |
| Remittance frequency | Monthly | FNPF Employers |
| Schedule / payment deadline | Schedule due by the **14th**; payment by end of month / last working day following the contribution month | **[RESEARCH GAP — secondary employer guides; FNPF page states only "payable monthly"]** |
| Late-payment penalty | Reported at **10% per month** on the outstanding amount | **[RESEARCH GAP — reviewer to confirm against FNPF Act 2011]** |

## Section 8 -- PAYE Employer Obligations, Filing & Remittance

**PAYE Employer Obligations table**  _(FRCS PAYE structure notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/; corroborated by employer guides)_

| Obligation | Detail |
| --- | --- |
| Registration | Employer must register with FRCS for PAYE and hold a TIN; employees must have TINs |
| Deduction | Deduct PAYE (incl. SRT & ECAL where applicable) each pay period using FRCS tax tables / 2024 PAYE Regulation 6 formula |
| Final tax | PAYE is a final tax for employees with employment income only — no annual return required |
| Filing portal | FRCS Taxpayer Online Services (TPOS) |
| Monthly return + remittance | By the **15th of the following month** **[RESEARCH GAP — from employer guides; not captured verbatim from a primary FRCS page]** |
| Penalties | Penalties and interest for late filing/payment under the Tax Administration Act 2009; exact amounts vary **[RESEARCH GAP — no specific statutory figure confirmed from a primary source]** |

## Section 9 -- Minimum Wage

**Minimum Wage table**

| Item | Value | Source |
| --- | --- | --- |
| National minimum wage | **FJD $5.00 per hour**, effective 1 April 2025 | Fiji Govt -- https://www.fiji.gov.fj/Media-Centre/News/MINIMUM-WAGE-INCREASE-TO-$5-00-AN-HOUR-BY-1ST-APRI |
| Phasing | $4.00 → $4.50 (1 Aug 2024) → $5.00 (1 Apr 2025) | WageIndicator |
| Sector minimums | Wages Regulation Orders apply on top in certain industries (e.g. construction foreman ~$7.54/hr from Apr 2025) | WageIndicator |
| Governing law | Employment Relations Act 2007; underpayment is a criminal offence | MEPIR |

## Section 10 -- Corporate Income Tax (Context -- Not Payroll)

**Corporate Income Tax table**

| Item | Value | Source |
| --- | --- | --- |
| Standard corporate income tax rate | **25%** (2024) | FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ |
| Concessions | E.g. 15% for up to 7 years for qualifying entities; reduced rate for new South Pacific Stock Exchange listings | FRCS Tax Rates |

Note: One aggregator cited 20%; the FRCS Tax Rates page states 25%. Use the FRCS figure (25%).

## Section 11 -- Transaction / Payment Pattern Library

### 11.1 Salary Credits (employee bank statement -- credits)

**Salary Credits table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| SALARY, PAY, WAGES, NET PAY | Net salary payment | After PAYE/SRT/ECAL + 8% FNPF withheld |
| FORTNIGHT PAY, MONTHLY SALARY | Net salary payment | Confirm pay frequency for annualisation |
| BACK PAY, ARREARS | Net salary (catch-up) | May straddle periods — re-annualise PAYE |
| FNPF REFUND, FNPF ADJUSTMENT | Contribution adjustment | NOT income |

### 11.2 Employer Debit Patterns (employer bank statement -- debits)

**Employer Debit Patterns table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| FRCS, PAYE, TAX REMITTANCE, TPOS | PAYE + SRT + ECAL remittance to FRCS | Liability until remitted |
| FNPF, FNPF CONTRIBUTION, FNPF EMPLOYER | FNPF contribution (8% employee + 10% employer) | Employer 10% is an expense; employee 8% is withheld |
| NET WAGES, PAYROLL RUN, SALARY DISBURSEMENT | Net salary disbursement to employees |  |
| FNPF VOLUNTARY | Voluntary FNPF top-up | Confirm policy/contract |

### 11.3 Exclusions

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not a payroll transaction |
| LOAN, ADVANCE REPAYMENT | EXCLUDE from PAYE base | Not remuneration unless contractually pay |
| EXPENSE REIMBURSEMENT | EXCLUDE | Reimbursement, not wages (confirm composition) |

## Section 12 -- Worked Examples

All figures in FJD. PAYE per Section 3.1; FNPF per Section 7.1 (employee 8%, employer 10%). Examples assume employment income only and full-year employment unless stated.

### Example 1 -- Resident below the tax-free threshold ($20,000/yr)

**Input:** Resident, annual gross ordinary wages $20,000.

```
PAYE: $20,000 < $30,000 threshold              = $0
FNPF (employee 8%): 0.08 × 20,000              = $1,600.00
Total employee deductions                       = $1,600.00
Net pay                                          = 20,000 − 1,600 = $18,400.00
Employer FNPF (10%): 0.10 × 20,000             = $2,000.00
Total employer cost                              = 20,000 + 2,000 = $22,000.00
```

### Example 2 -- Resident in the 18% band ($45,000/yr)

**Input:** Resident, annual gross $45,000. Monthly pay.

```
PAYE: 18% × (45,000 − 30,000) = 0.18 × 15,000  = $2,700.00
FNPF (employee 8%): 0.08 × 45,000              = $3,600.00
Total employee deductions                       = 2,700 + 3,600 = $6,300.00
Net pay (annual)                                = 45,000 − 6,300 = $38,700.00
Employer FNPF (10%): 0.10 × 45,000             = $4,500.00
─ Monthly view ─
Gross 45,000/12                                 = $3,750.00
PAYE 2,700/12                                   = $225.00
FNPF 3,600/12                                   = $300.00
Net monthly = 3,750 − 225 − 300                 = $3,225.00
```

### Example 3 -- Resident in the 20% band ($80,000/yr)

**Input:** Resident, annual gross $80,000.

```
PAYE: 3,600 + 20% × (80,000 − 50,000)
     = 3,600 + 0.20 × 30,000 = 3,600 + 6,000   = $9,600.00
SRT / ECAL: income < $270,000                   = $0
FNPF (employee 8%): 0.08 × 80,000              = $6,400.00
Total employee deductions                       = 9,600 + 6,400 = $16,000.00
Net pay                                          = 80,000 − 16,000 = $64,000.00
Employer FNPF (10%): 0.10 × 80,000             = $8,000.00
```

### Example 4 -- High earner with SRT + ECAL ($320,000/yr)

**Input:** Resident, annual chargeable income $320,000.

```
Income tax (PAYE): 53,600 + 20% × (320,000 − 300,000)
     = 53,600 + 0.20 × 20,000 = 53,600 + 4,000  = $57,600.00
SRT: 5,400 + 19% × (320,000 − 300,000)
     = 5,400 + 0.19 × 20,000 = 5,400 + 3,800     = $9,200.00
ECAL (on income): 10% × (320,000 − 270,000)
     = 0.10 × 50,000                              = $5,000.00   [RESEARCH GAP — confirm ECAL]
FNPF (employee 8%): 0.08 × 320,000              = $25,600.00
Total employee deductions
     = 57,600 + 9,200 + 5,000 + 25,600           = $97,400.00
Net pay = 320,000 − 97,400                       = $222,600.00
Employer FNPF (10%): 0.10 × 320,000             = $32,000.00
```

### Example 5 -- Non-resident employee ($60,000/yr)

**Input:** Non-resident, annual gross $60,000. No tax-free threshold (Section 6).

```
PAYE: flat 20% × 60,000                          = $12,000.00
SRT / ECAL: income < $270,000                    = $0
FNPF (employee 8%): 0.08 × 60,000               = $4,800.00   [RESEARCH GAP — confirm FNPF coverage for non-residents]
Total employee deductions                        = 12,000 + 4,800 = $16,800.00
Net pay = 60,000 − 16,800                        = $43,200.00
Employer FNPF (10%): 0.10 × 60,000              = $6,000.00
```

### Example 6 -- Minimum-wage worker ($5.00/hr, 40 hrs/wk)

**Input:** Resident, $5.00/hr × 40 hrs × 52 weeks = $10,400/yr.

```
Annual gross: 5.00 × 40 × 52                     = $10,400.00
PAYE: $10,400 < $30,000 threshold                = $0
FNPF (employee 8%): 0.08 × 10,400               = $832.00
Net pay = 10,400 − 832                           = $9,568.00
Employer FNPF (10%): 0.10 × 10,400              = $1,040.00
```

## Section 13 -- Tier 1 Rules (Deterministic -- Apply Mechanically)

- **Tax-free threshold residents only** — Tax-free threshold $30,000 applies to residents ONLY. Non-residents pay flat 20% from $1.  _(FRCS)_
- **Income tax marginal rate cap** — Income tax marginal rate caps at 20% — never apply more than 20% as the income-tax component.  _(FRCS Tax Rates)_
- **SRT applies only above $270,000** — SRT applies ONLY above $270,000 chargeable income — zero below.  _(FRCS Tax Rates)_
- **ECAL applies only above $270,000** — ECAL on income applies ONLY above $270,000 — zero below.  _(HLB Fiji; RESEARCH GAP)_
- **FNPF rate composition** — FNPF = 8% employee + 10% employer, no cap, on ordinary wages.  _(FNPF, eff. 1 Jan 2024)_
- **PAYE is final tax** — PAYE is a final tax for employment-only income — no annual return for those employees.  _(FRCS)_
- **Tax year definition** — Tax year = calendar year (1 Jan – 31 Dec).  _(FRCS)_
- **Employer withholding responsibility** — All employee deductions (PAYE/SRT/ECAL + 8% FNPF) are withheld and remitted by the employer.
- **Annualisation requirement** — Annualise before applying brackets, then allocate to pay periods cumulatively.

## Section 14 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 Catalogue table**

| Issue | Why it needs judgement |
| --- | --- |
| Income at/near $270,000 | Triggers SRT + ECAL stacking; combined marginal rate jumps materially |
| "Ordinary wages" definition for FNPF | Whether allowances/bonuses/overtime are inside the FNPF base affects the 18% total |
| Non-resident FNPF coverage | Applicability to short-term assignees is unconfirmed [RESEARCH GAP] |
| Mid-year start/leave | Cumulative PAYE true-up; annualisation assumptions break |
| Sector Wages Regulation Order | Sector minimum may exceed national $5.00/hr |
| Voluntary FNPF top-ups | Tax treatment and employer-policy interaction |
| Fringe benefits / non-cash pay | Out of scope — fringe benefit tax rules apply (escalate) |
| Penalty exposure | Exact FRCS/FNPF penalty figures unconfirmed [RESEARCH GAP] |

## Section 15 -- Excel Working Paper Template

Suggested columns for a per-employee monthly payroll working paper:

**Excel Working Paper Template columns**

| Column | Content |
| --- | --- |
| A | Employee name |
| B | TIN |
| C | FNPF member number |
| D | Residency (R / NR) |
| E | Pay period |
| F | Gross ordinary wages (period) |
| G | Annualised gross (=F × periods/year) |
| H | Annual income tax (PAYE) per Section 3.1 / Section 6 |
| I | SRT (annual) per Section 4 (0 if ≤ $270,000) |
| J | ECAL on income (annual) per Section 5 (0 if ≤ $270,000) |
| K | Period PAYE+SRT+ECAL (=(H+I+J)/periods) |
| L | FNPF employee (=F × 8%) |
| M | Net pay (=F − K − L) |
| N | FNPF employer (=F × 10%) |
| O | Total employer cost (=F + N) |

**Control totals (must reconcile):**
- Sum of column K = PAYE/SRT/ECAL remitted to FRCS for the period.
- Sum of (L + N) = total FNPF remitted (employee 8% + employer 10% = 18%).
- Sum of column M = total net salary disbursed.

## Section 16 -- Bank Statement / Terminology Reading Guide

**Terminology Reading Guide table**

| Term / abbreviation | Meaning |
| --- | --- |
| FRCS | Fiji Revenue & Customs Service (income tax authority) |
| FNPF | Fiji National Provident Fund (mandatory pension/social fund) |
| PAYE | Pay As You Earn — employment income tax withholding |
| SRT | Social Responsibility Tax (high earners, > $270,000) |
| ECAL | Environment & Climate Adaptation Levy |
| TPOS | Taxpayer Online Services (FRCS filing portal) |
| TIN | Tax Identification Number |
| WRO | Wages Regulation Order (sector minimum wage instrument) |
| MEPIR | Ministry of Employment, Productivity & Industrial Relations |
| Ordinary wages | Base wages used for FNPF contribution calculation |
| $ / FJD | Fijian Dollar (the only currency in this skill) |

## Section 17 -- Onboarding Fallback

If the minimum viable inputs (Section 2) are not available:

1. Ask for **residency status** first — it changes the entire PAYE computation.
2. Ask for **annual or period gross ordinary wages** and **pay frequency**.
3. Confirm **FNPF membership / age 15+**.
4. If the employee may earn **> $270,000**, STOP and escalate (SRT + ECAL stacking).
5. If sector-specific (construction, hospitality, etc.), check for a **Wages Regulation Order** before assuming the national minimum wage.
6. Produce an **estimated** computation clearly labelled as draft, and route to a Fiji-licensed accountant for sign-off.

## Section 18 -- Reference Material and Test Suite

### Key Sources

**Key Sources table**

| Topic | Reference |
| --- | --- |
| Resident PAYE brackets; SRT; corporate 25% | FRCS Tax Rates -- https://frcs.org.fj/tax-rates-and-codes/ |
| PAYE as final tax; PAYE structure | FRCS public notice -- https://frcs.org.fj/public-notice/customer-service-new-pay-as-you-earn-paye-structure/ |
| FNPF 8%/10%, coverage, monthly remittance | FNPF Employers -- https://myfnpf.com.fj/employers/ |
| ECAL on income (10% > $270,000) | HLB Fiji -- https://www.hlbfiji.com/an-introduction-to-environmental-climate-and-adaptation-levy-ecal/ **[RESEARCH GAP]** |
| Minimum wage $5.00/hr (1 Apr 2025) | Fiji Govt -- https://www.fiji.gov.fj/Media-Centre/News/MINIMUM-WAGE-INCREASE-TO-$5-00-AN-HOUR-BY-1ST-APRI |
| Governing legislation | Income Tax Act 2015; Tax Administration Act 2009; FNPF Act 2011; Employment Relations Act 2007 |

### Test Suite (recompute to the cent before relying on this skill)

1. **Resident $20,000:** PAYE $0; FNPF employee $1,600; net $18,400; employer FNPF $2,000. ✓
2. **Resident $45,000:** PAYE $2,700 (18% × 15,000); FNPF employee $3,600; net $38,700; employer FNPF $4,500. ✓
3. **Resident $80,000:** PAYE $9,600 (3,600 + 20% × 30,000); FNPF employee $6,400; net $64,000; employer FNPF $8,000. ✓
4. **Resident $320,000:** PAYE $57,600; SRT $9,200; ECAL $5,000; FNPF employee $25,600; total deductions $97,400; net $222,600; employer FNPF $32,000. ✓
5. **Non-resident $60,000:** PAYE $12,000 (flat 20%); FNPF employee $4,800; net $43,200; employer FNPF $6,000. ✓
6. **Minimum wage 40 hrs/wk:** annual $10,400; PAYE $0; FNPF employee $832; net $9,568; employer FNPF $1,040. ✓
7. **FNPF total check:** employee 8% + employer 10% = 18% on ordinary wages, no cap. ✓
8. **SRT/ECAL boundary:** chargeable income of exactly $270,000 → SRT $0 and ECAL $0 (both apply only to the *excess over* $270,000). ✓
9. **Bracket continuity:** income tax at $50,000 = $3,600; at $270,000 = $47,600; at $300,000 = $53,600; at $1,000,000 = $193,600. ✓

## PROHIBITIONS

- NEVER apply the $30,000 tax-free threshold to a non-resident — non-residents pay flat 20% from the first dollar.
- NEVER apply an income-tax marginal rate above 20% — additional burden above $270,000 comes from SRT and ECAL, not income tax.
- NEVER charge SRT or ECAL on income at or below $270,000.
- NEVER cap or floor FNPF — it is 8% employee + 10% employer on full ordinary wages with no ceiling.
- NEVER omit the employer's 10% FNPF when computing total employer cost.
- NEVER treat PAYE as non-final for an employment-only employee, nor force them to file an annual return.
- NEVER state exact FRCS or FNPF penalty figures — they are unconfirmed [RESEARCH GAP]; cite the governing Act and escalate.
- NEVER present ECAL figures as definitive without flagging the [RESEARCH GAP] on the FRCS ECAL source.
- NEVER assume the national minimum wage applies where a sector Wages Regulation Order may set a higher rate.
- NEVER present payroll computations as definitive — always label as estimated and direct to a Fiji-licensed accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax practitioner in Fiji) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
