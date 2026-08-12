---
name: kosovo-payroll
description: Use this skill whenever asked about Kosovo payroll processing for employed persons. Trigger on phrases like "Kosovo payroll", "Kosova paga", "tatimi mbi pagat", "personal income tax Kosovo", "tatimi në të ardhura personale", "withholding tax Kosovo", "mbajtja në burim", "pension contribution Kosovo", "kontributi pensional", "KPST", "Trusti pensional", "ATK", "TAK", "Administrata Tatimore e Kosovës", "EDI declaration", "WM form Kosovo", "net salary Kosovo", "paga neto", "gross to net Kosovo", "PAYE Kosovo", "employer contributions Kosovo", "minimum wage Kosovo", "paga minimale", "secondary employer Kosovo", "benefit in kind Kosovo", or any question about computing employee pay, withholding personal income tax, or mandatory pension contributions for Kosovo-based employees. This skill covers PIT monthly withholding (progressive 0%/8%/10% bands for the primary employer, flat 10% for secondary employers), mandatory pension contributions (5% employee + 5% employer to KPST), voluntary supplementary pension, benefit-in-kind thresholds, minimum wage, new-hire reporting, and the monthly WM declaration and annual reconciliation. ALWAYS read this skill before processing any Kosovo payroll.
version: 0.1
jurisdiction: XK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kosovo Payroll

## Kosovo Payroll Skill v0.1

**Tier 2 — research-verified. Figures below are sourced from the Tax Administration of Kosovo (Administrata Tatimore e Kosovës — TAK/ATK), Law No. 05/L-028 on Personal Income Tax as amended by Law No. 08/L-142 (effective 23 August 2024), Law No. 04/L-101 on Pension Funds, Law No. 03/L-222 on Tax Administration and Procedures, the Kosovo Pension Savings Trust (Trusti i Kursimeve Pensionale të Kosovës — KPST), PwC Worldwide Tax Summaries (last reviewed 13 Jan 2026), and Bloomberg Tax/Law. NOT yet signed off by a licensed Kosovo accountant or tax adviser. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Kosovo (Republic of Kosovo / Republika e Kosovës) |
| Currency | EUR only (Kosovo uses the euro despite not being a eurozone member) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) (PwC) |
| Tax withholding system | Monthly PIT withholding by the employer; computed on the monthly bands to match the pay period (Bloomberg Law; PwC) |
| Income tax authority | Tax Administration of Kosovo (Administrata Tatimore e Kosovës — TAK/ATK), portal atk-ks.org, filing via the EDI electronic declaration system |
| Pension authority | Kosovo Pension Savings Trust (Trusti i Kursimeve Pensionale të Kosovës — KPST); contributions collected via TAK; supervised by the Central Bank of Kosovo (BQK) |
| Key legislation | Law No. 05/L-028 on Personal Income Tax (as amended by Law No. 08/L-142, eff. 23 Aug 2024); Law No. 04/L-101 on Pension Funds; Law No. 03/L-222 on Tax Administration and Procedures |
| Filing portal | TAK EDI electronic declaration system (via atk-ks.org) |
| Validated by | Pending -- requires sign-off by a licensed Kosovo accountant / tax adviser |
| Skill version | 0.1 |

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Kosovo-specific content.**

### The single most important Kosovo fact

- **Primary vs secondary employer PIT treatment** — The PIT bands an employer applies depend on whether it is the employee's PRIMARY or SECONDARY employer. The primary (main) employer withholds on the progressive monthly bands 0% / 8% / 10%. A secondary employer withholds a flat 10% on all wage income it pays, with no 0% or 8% band — the employee then reconciles on the annual return. If you do not know the employee's status, default to primary (progressive) only if you have confirmed there is no other employer; otherwise treat the second job as secondary and apply the flat 10%.  _(Bloomberg Law; TAK Notice on Law No. 08/L-142)_

## Section 2 -- Income Tax Withholding (tatimi mbi pagat)

The employer withholds personal income tax (PIT) monthly. The 4% band was removed and the brackets reset by Law No. 08/L-142, effective 23 August 2024; the same brackets apply for 2025 and 2026 on the evidence reviewed. (Bloomberg Law; TAK Notice; PwC)

### Monthly Wage Bands — PRIMARY employer (2025)

**Monthly Wage Bands — PRIMARY employer (2025)**  _(Bloomberg Law; TAK Notice; PwC — withholding on wages is computed monthly to match the pay period)_

| Band | Monthly PIT base (EUR) | Rate |
| --- | --- | --- |
| 1 | 0.00 -- 250.00 | 0% |
| 2 | 250.01 -- 450.00 | 8% |
| 3 | above 450.00 | 10% |

- **Maximum tax in 8% band** — The maximum tax in the 8% band is EUR 16.00 (8% × the EUR 200.00 width of the 250.01–450.00 band; verify: 0.08 × 200 = 16.00 ✓). Everything above EUR 450.00 of base is taxed at 10%.  _(Bloomberg Law; TAK Notice; PwC)_

### Secondary employer — flat 10%

- **Secondary employer flat rate** — A secondary employer withholds a flat 10% on all wage income it pays — no 0% or 8% band is applied. The employee reconciles the total across all employers on the annual PIT return.  _(Bloomberg Law)_

### Annual Bands — reconciliation / equivalent (2025)

**Annual Bands — reconciliation / equivalent (2025)**  _(PwC)_

| Band | Annual income (EUR) | Rate |
| --- | --- | --- |
| 1 | 0.00 -- 3,000.00 | 0% |
| 2 | 3,000.01 -- 5,400.00 | 8% |
| 3 | above 5,400.00 | 10% |

- **Annual bands derivation and usage** — The annual bands are the monthly bands × 12 (250 × 12 = 3,000 ✓; 450 × 12 = 5,400 ✓) and drive the annual reconciliation, not each individual pay run. Each pay run uses the MONTHLY bands.  _(PwC income determination; Bloomberg Law)_

### Monthly Withholding Method (primary employer)

- **Deterministic withholding order** — 1. Start with gross salary (paga bruto). 2. Subtract the 5% mandatory employee pension contribution (Section 3). Only the mandatory pension is tax-deductible, so it reduces the PIT base. 3. Add any taxable benefit in kind to the extent it exceeds EUR 65/month (Section 5). 4. The result is the monthly PIT base. 5. Apply the monthly bands: 0% on the first EUR 250.00, 8% on EUR 250.01–450.00, 10% on the portion above EUR 450.00. 6. The sum is the withheld PIT for the month. The employer then adds the 5% employer pension contribution on top of gross (an employer cost, not a deduction — see Section 4).  _(PwC — other taxes / income determination)_

**[T2-1 — reviewer to confirm the exact PIT base definition.]** PwC and Bloomberg describe monthly wage bands and confirm that only the mandatory 5%+5% pension is tax-deductible; this skill therefore computes the PIT base as gross less the 5% employee pension (plus any BIK above EUR 65). A reviewer should confirm against the live TAK/EDI WM form mechanics whether the employee pension is deducted before applying the wage bands.

## Section 3 -- Contributions: Employee Deductions (Pension)

- **No employee social security beyond pension** — Kosovo has no employee social-security tax beyond the mandatory pension. The employee pays a 5% mandatory pension contribution, withheld from gross and remitted to the Kosovo Pension Savings Trust (KPST) via TAK.  _(PwC — other taxes)_

**Employee pension contributions table**  _(PwC — other taxes)_

| Contribution | Rate | Payer | Authority | Note |
| --- | --- | --- | --- | --- |
| Mandatory pension — employee share | 5% of gross salary | Employee (withheld) | KPST (collected via TAK) | The only mandatory employee deduction besides PIT |
| Voluntary supplementary pension — employee | up to 15% of gross salary | Employee (elective) | KPST | Optional; see Section 4 note on deductibility |

### Total mandatory employee deductions

**Total mandatory employee deductions**  _(PwC — other taxes)_

| Item | Rate / basis |
| --- | --- |
| PIT | 0% / 8% / 10% monthly bands (primary) or flat 10% (secondary) on the PIT base |
| Mandatory pension | 5% of gross salary |

Both are withheld from gross wage. (PwC — other taxes)

## Section 4 -- Contributions: Employer Contributions (Pension)

- **Employer pension contribution and PIT not employer cost** — The employer pays a 5% mandatory pension contribution on top of gross salary, remitted to KPST via TAK. There is no employer social-security, health, or unemployment levy beyond the mandatory pension. PIT is fully employee-borne (withheld), not an employer cost.  _(PwC — other taxes)_

**Employer pension contributions table**

| Contribution | Rate | Payer | Authority | Ceiling | Note |
| --- | --- | --- | --- | --- | --- |
| Mandatory pension — employer share | 5% of gross salary | Employer (on top of gross) | KPST (via TAK) | See base cap below | Sole mandatory employer-borne contribution |
| Voluntary supplementary pension — employer | up to 15% of gross salary | Employer (elective) | KPST | — | Optional |

### Combined mandatory pension

**Combined mandatory pension**  _(PwC — other taxes)_

| Share | Rate of gross |
| --- | --- |
| Employee | 5% |
| Employer | 5% |
| **Total mandatory pension** | **10%** |

(verify: 5% + 5% = 10% ✓) (PwC — other taxes)

### Voluntary supplementary pension

- **Total employer cost formula** — Total employer cost = gross salary + (5% × gross salary) = gross × 1.05. PIT does not appear in employer cost because it is withheld from the employee's gross, not added on top.  _(PwC)_
- **Voluntary contribution limits and deductibility** — Voluntary supplementary contributions of up to 15% each (employer and employee, 30% combined maximum) are permitted, but only the mandatory 5% + 5% is tax-deductible — voluntary amounts are optional and do not reduce the PIT base. **[T2-2 — reviewer to confirm the tax treatment of any elected voluntary contribution before relying on it.]**  _(PwC — other taxes)_

### Pension contribution wage-base cap

- **Pension base cap unresolved** — PwC states the mandatory contribution base is capped between a minimum and a maximum wage threshold set by law. No authoritative EUR maximum-base figure was located in this research. **[RESEARCH GAP — reviewer to confirm the EUR minimum and maximum monthly contribution base with KPST/TAK before relying on it for high earners.]**  _(PwC — other taxes)_

### Benefit-in-kind threshold

- **BIK tax-free threshold** — Benefits in kind are taxable as wages to the extent they exceed EUR 65 per month. The first EUR 65/month of benefits in kind is tax-free; only the excess is added to the PIT base.  _(PwC — income determination)_

### National Minimum Gross Wage (paga minimale)

**National Minimum Gross Wage (paga minimale)**

| Period | Monthly gross (EUR) | Note |
| --- | --- | --- |
| Through 2025 | 350.00 | In force during 2025 (Balkanweb / WageIndicator, reporting Government decision) |
| From 1 January 2026 | 425.00 | Government decision 10/273, 31 Oct 2025 (Balkanweb; WageIndicator) |
| From 1 July 2026 | 500.00 | Government decision 10/273 (Balkanweb) |

- **Apply EUR 350 to 2025 only** — Apply EUR 350 to 2025 pay periods only. The EUR 425 and EUR 500 figures take effect in 2026 and must NOT be applied to 2025 runs.  _(Balkanweb; WageIndicator)_

### Working hours and overtime

**[RESEARCH GAP — reviewer to confirm]** Statutory overtime multipliers, maximum weekly hours, and night/weekend/holiday premiums under the Kosovo Labour Law were not part of this research dataset. A reviewer should populate these from the Labour Law (Ligji i Punës) and any applicable collective agreement before relying on overtime figures.

## Section 6 -- Conservative Defaults

When an input is unknown, the skill MUST apply the conservative default below and flag the assumption in its output rather than guessing a more favourable figure.

**Conservative Defaults table**

| Field | Default | Rationale |
| --- | --- | --- |
| Employer status (primary vs secondary) | **Primary** ONLY if it is confirmed the employee has no other employer; otherwise treat a second job as **secondary** (flat 10%) | Secondary employment is withheld at a flat 10% with no 0%/8% band; defaulting wrongly to primary would under-withhold. (Bloomberg Law) |
| Mandatory pension | **5% employee + 5% employer, no voluntary top-up** | Voluntary contributions are optional and not assumed unless elected. (PwC) |
| PIT base | **Gross − 5% employee pension (+ BIK above EUR 65)** | Only the mandatory pension is deductible; flag pending reviewer confirmation of the exact WM-form base. (PwC) **[T2-1]** |
| Minimum wage | **EUR 350/month for 2025 pay periods; EUR 425 from 1 Jan 2026** | EUR 350 was the rate in force during 2025; the increase takes effect 1 Jan 2026. (Balkanweb; WageIndicator) |
| Benefit in kind | **Tax-free only up to EUR 65/month; excess added to PIT base** | Statutory threshold. (PwC) |
| Pension base cap | **No cap applied unless a confirmed EUR maximum base is supplied** | The cap exists per PwC but no EUR figure was located; flag for high earners. **[RESEARCH GAP]** |
| Employer cost estimate | **Gross × 1.05** (add 5% employer pension) | Single mandatory employer-borne contribution; PIT is not an employer cost. (PwC) |
| Remittance timing | **15th of the following month** for the monthly WM declaration and payment | Statutory monthly cadence via TAK EDI. (PwC — tax administration) |

## Section 7 -- Required Inputs and Refusal Catalogue

### Required inputs before any computation

- **Required inputs list** — 1. Gross monthly salary (paga bruto) in EUR. 2. Employer status — is this the employee's PRIMARY or SECONDARY employer? (Drives progressive bands vs flat 10%.) 3. Pay period (month and year) — to pick the correct minimum wage and band figures (2025 vs 2026). 4. Whether any benefit in kind is provided, and its monthly value (taxable above EUR 65). 5. Whether any voluntary supplementary pension is elected (and by whom) — otherwise mandatory 5% + 5% only. 6. Whether the employee is a new hire this period — triggers TAK notification at least one day before the start date.

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal Catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Posted workers / cross-border social-security coordination / totalization | Requires treaty and KPST/TAK determinations — see `cross-border-payroll-coordination`. |
| Non-resident employees, double-tax-treaty relief, expat tax-equalisation | Treaty residency and tie-breaker analysis is beyond a domestic payroll run. |
| Pension base cap for very high earners | The EUR maximum contribution base is unconfirmed in this research. **[RESEARCH GAP]** |
| Tax treatment of elected voluntary supplementary pension | Deductibility/mechanics unresolved here. **[T2-2]** |
| Severance / termination payment taxation | Not in scope; route to a reviewer. |
| Self-employed / sole-trader contributions | Different regime — out of scope for employer payroll. |
| Exact EUR fine amounts for late filing | Available only as graduated fixed amounts under Law 03/L-222 not extracted here. **[RESEARCH GAP]** |
| Overtime / night / holiday premium computation | Labour Law multipliers not in this research dataset. **[RESEARCH GAP]** |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Kosovo bank-statement lines for payroll. Match on the uppercased description fragment. Descriptions appear in Albanian (sq), Serbian (sr) and English.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (SQ / EN) | Classification |
| --- | --- |
| `PAGA`, `PAGA NETO`, `PAGESA E PAGES` | Net salary payment |
| `SALARY`, `WAGES`, `NET SALARY` | Net salary payment (English variant) |
| `PARADHENIE`, `AVANS` | Salary advance (not final pay) |
| `SHTESA`, `BONUS`, `KOMPENSIM` | Allowance / bonus (check taxability) |
| `MEDITJE`, `PER DIEM` | Per-diem / travel allowance (may be tax-exempt up to limits — verify) |
| `KTHIM TATIMI`, `TAX REFUND` | PIT refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (SQ / EN) | Classification |
| --- | --- |
| `TATIMI NE BURIM`, `TATIMI MBI PAGAT`, `ATK`, `TAK` | PIT withheld, remitted to the Tax Administration |
| `KONTRIBUTI PENSIONAL`, `PENSION`, `KPST`, `TRUSTI` | Mandatory pension contribution remittance (employee 5% + employer 5%) to KPST |
| `WM`, `EDI` | Reference tag for the monthly WM declaration / EDI payment batch |
| `PAGESA E PAGAVE`, `PAYROLL`, `LISTA E PAGAVE` | Net wages disbursed to employees |

PIT is remitted to TAK; the mandatory pension (5% + 5%) is collected by TAK and routed to KPST. Both are declared together on the monthly WM declaration via the EDI system (Section 12). **[T2-3 — the exact WM form code was not verified against a live TAK/EDI page; treat the WM label as the commonly used wage/withholding form and confirm on the EDI portal.]**

## Section 9 -- Worked Examples

All examples use 2025 figures. The mandatory pension is 5% employee + 5% employer. The PIT base is gross less the 5% employee pension (plus any BIK above EUR 65) per the Section 2 method **[T2-1]**. Primary-employer examples use the progressive monthly bands (0% / 8% / 10%); the secondary-employer example uses the flat 10%. Every line below was recomputed end-to-end.

### Example 1 — Standard primary-employer employee, EUR 500 gross/month

Bank statement context: `PAGA NETO … 456,50 EUR` credited to the employee; `ATK … 18,50 EUR` (PIT) and `KPST … 50,00 EUR` (pension, 5%+5%) debited from the employer.

**Example 1 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 500.00 |
| Employee pension (5% of 500) | — | 25.00 |
| PIT base | 500 − 25 | 475.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–475) | 25 × 10% | 2.50 |
| Total PIT | 0 + 16 + 2.50 | 18.50 |
| **Net pay** | 500 − 25 − 18.50 | **456.50** |
| Employer pension (5% of 500) | on top of gross | 25.00 |
| **Total employer cost** | 500 + 25 | **525.00** |

### Example 2 — Minimum-wage worker (2025), EUR 350 gross/month, primary

**Example 2 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 350.00 |
| Employee pension (5% of 350) | — | 17.50 |
| PIT base | 350 − 17.50 | 332.50 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–332.50) | 82.50 × 8% | 6.60 |
| PIT — band 3 (10% above 450) | none | 0.00 |
| Total PIT | — | 6.60 |
| **Net pay** | 350 − 17.50 − 6.60 | **325.90** |
| Employer pension (5% of 350) | on top | 17.50 |
| **Total employer cost** | 350 + 17.50 | **367.50** |

### Example 3 — Low earner inside the 0% band, EUR 250 gross/month, primary

**Example 3 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 250.00 |
| Employee pension (5% of 250) | — | 12.50 |
| PIT base | 250 − 12.50 | 237.50 |
| PIT — band 1 (0% — base ≤ 250) | 237.50 × 0% | 0.00 |
| Total PIT | — | 0.00 |
| **Net pay** | 250 − 12.50 − 0 | **237.50** |
| Employer pension (5% of 250) | on top | 12.50 |
| **Total employer cost** | 250 + 12.50 | **262.50** |

Note EUR 250 is below the 2025 statutory minimum wage of EUR 350 for a full-time worker — used here only to illustrate a base that stays entirely within the 0% band. Do not run a full-time worker below the minimum wage.

### Example 4 — Mid earner across all three bands, EUR 1,000 gross/month, primary

**Example 4 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary | — | 1,000.00 |
| Employee pension (5% of 1,000) | — | 50.00 |
| PIT base | 1,000 − 50 | 950.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–950) | 500 × 10% | 50.00 |
| Total PIT | 0 + 16 + 50 | 66.00 |
| **Net pay** | 1,000 − 50 − 66 | **884.00** |
| Employer pension (5% of 1,000) | on top | 50.00 |
| **Total employer cost** | 1,000 + 50 | **1,050.00** |

### Example 5 — Secondary employer, EUR 800 gross/month, FLAT 10%

**Example 5 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Gross salary (from this secondary job) | — | 800.00 |
| Employee pension (5% of 800) | — | 40.00 |
| PIT base | 800 − 40 | 760.00 |
| PIT — flat 10% (no 0%/8% band) | 760 × 10% | 76.00 |
| **Net pay** | 800 − 40 − 76 | **684.00** |
| Employer pension (5% of 800) | on top | 40.00 |
| **Total employer cost** | 800 + 40 | **840.00** |

A secondary employer applies a flat 10% to all wage income — no 0% or 8% band. The employee reconciles the combined income across all employers on the annual PIT return (where the progressive annual bands apply). (Bloomberg Law) **[T2-4 — whether the secondary employer applies the 10% to gross or to gross-less-pension was not verified; this example deducts the 5% pension first, consistent with the deductibility rule, and flags it for review.]**

### Example 6 — Primary employee with a benefit in kind, EUR 600 gross + EUR 100/month BIK

**Example 6 computation table**

| Step | Computation | EUR |
| --- | --- | --- |
| Cash gross salary | — | 600.00 |
| Employee pension (5% of 600) | — | 30.00 |
| Cash base after pension | 600 − 30 | 570.00 |
| Taxable BIK (excess over 65) | 100 − 65 | 35.00 |
| PIT base | 570 + 35 | 605.00 |
| PIT — band 1 (0% on first 250) | 250 × 0% | 0.00 |
| PIT — band 2 (8% on 250.01–450) | 200 × 8% | 16.00 |
| PIT — band 3 (10% on 450.01–605) | 155 × 10% | 15.50 |
| Total PIT | 0 + 16 + 15.50 | 31.50 |
| **Net cash pay** | 600 − 30 − 31.50 | **538.50** |
| Employer pension (5% of cash gross 600) | on top | 30.00 |
| **Total employer cash cost** | 600 + 30 | **630.00** (plus the cost of providing the EUR 100 benefit) |

Only the EUR 35 BIK excess over the EUR 65/month threshold enters the PIT base; the first EUR 65 is tax-free. (PwC — income determination) **[T2-5 — whether the taxable BIK also enters the pension base was not resolved; this example applies the 5% pension to cash gross only and flags it.]**

## Section 10 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **T1-1 Monthly wage PIT primary** — Monthly wage PIT (PRIMARY employer): 0% on the first EUR 250, 8% on EUR 250.01–450.00, 10% above EUR 450.00. The 4% band was removed and brackets reset by Law No. 08/L-142, effective 23 Aug 2024.  _(Bloomberg Law; TAK Notice)_
- **T1-2 Secondary employer flat rate** — SECONDARY employers withhold a flat 10% on all wage income they pay; no 0%/8% band. The employee reconciles on the annual return.  _(Bloomberg Law)_
- **T1-3 Annual PIT bands** — Annual PIT bands (reconciliation/equivalent): 0% to EUR 3,000; 8% on EUR 3,000.01–5,400; 10% above EUR 5,400 (= monthly bands × 12). Each pay run uses the MONTHLY bands, not the annual bands.  _(PwC)_
- **T1-4 Mandatory pension** — Mandatory pension: 5% withheld from the employee + 5% paid by the employer = 10% of gross salary, remitted to KPST via TAK.  _(PwC — other taxes)_
- **T1-5 Voluntary supplementary pension** — Voluntary supplementary pension up to 15% each (employer + employee, 30% combined) is permitted, but only the mandatory 5%+5% is tax-deductible.  _(PwC — other taxes)_
- **T1-6 Employer cost formula** — Employer cost = gross salary + 5% employer pension (gross × 1.05). PIT is fully employee-borne via withholding and is NOT an employer cost.  _(PwC)_
- **T1-7 Monthly computation** — Withholding on wages is computed monthly to match the pay period; the monthly bands drive each pay run.  _(PwC income determination; Bloomberg Law)_
- **T1-8 BIK threshold** — Benefits in kind are taxable as wages to the extent they exceed EUR 65/month; the first EUR 65/month is tax-free.  _(PwC — income determination)_
- **T1-9 Monthly WM deadline** — Monthly WM declaration and payment of withheld PIT and pension contributions is due by the 15th of the following month via the TAK EDI system.  _(PwC — tax administration)_
- **T1-10 Annual PIT return deadline** — The annual individual PIT return is due 31 March of the following year; the tax period is the calendar year.  _(PwC)_
- **T1-11 New-hire notification** — The employer must notify TAK of each new hire at least one day before the employee starts work.  _(PwC — tax administration)_
- **T1-12 Minimum gross wage** — Minimum gross wage (full-time): EUR 350/month during 2025; EUR 425 from 1 Jan 2026 and EUR 500 from 1 Jul 2026 (Government decision 10/273). Apply EUR 350 to 2025 pay periods only.  _(Balkanweb; WageIndicator)_
- **T1-13 Currency** — Currency is the euro (EUR); Kosovo uses the euro despite not being a eurozone member.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | Exact PIT base definition on the WM form | Confirm whether the 5% employee pension (and BIK above EUR 65) is deducted before applying the monthly wage bands, against the live TAK/EDI WM form mechanics. |
| **[T2-2]** | Tax treatment of elected voluntary supplementary pension | Only the mandatory 5%+5% is confirmed deductible; the mechanics for voluntary amounts are unresolved here. |
| **[T2-3]** | Exact WM form code / EDI form name | The 'WM' label was not verified against a live TAK page; confirm the precise wage-withholding declaration code on the EDI portal. |
| **[T2-4]** | Secondary-employer 10% base | Whether the flat 10% applies to gross or gross-less-pension was not verified. |
| **[T2-5]** | Pension base for benefits in kind | Whether the taxable BIK excess enters the 5% pension base was not resolved. |
| **[T2-6]** | Pension contribution wage-base cap (EUR maximum) | PwC confirms a min/max base exists; no EUR maximum figure was located. Confirm with KPST/TAK before relying on it for high earners. |
| **[T2-7]** | Overtime / night / holiday premiums under the Labour Law | Not researched here — confirm from the Kosovo Labour Law (Ligji i Punës) and any collective agreement. |
| **[T2-8]** | Exact EUR fixed fines for late filing under Law 03/L-222 | Only the 15%–25% understatement penalty and the monthly interest mechanism are confirmed; the fixed-fine schedule was not extracted. |
| **[T2-9]** | Per-diem / travel-allowance and severance tax limits | Not in this research dataset — reviewer to populate. |

## Section 12 -- Filing Obligations

### Monthly — WM declaration

**Monthly WM declaration table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **WM** — Statement of Tax Withheld on Wages and Pension Contributions | Monthly declaration and payment of PIT withheld on wages plus the mandatory (5% + 5%) pension contributions; filed electronically via the TAK EDI system. | By the **15th** day of the month following the pay period. (PwC — tax administration) **[T2-3 — exact WM form code unverified.]** |
| Payment of PIT + pension contributions | Remittance of withheld PIT and pension contributions to TAK (pension routed to KPST) | Same as the WM deadline — the 15th of the following month. (PwC) |
| WM withholding statement (other withholdings) | Statement / payment of other amounts subject to withholding; same monthly cadence | 1st–15th of the following month. (PwC) |

### Annual

**Annual filing table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Annual Personal Income Tax Return (individual) | Annual reconciliation of PIT, including where the taxpayer had multiple employers (primary + secondary) | **31 March** of the following year. (PwC) |

### Employee registration

**Employee registration table**

| Item | Requirement | Timing |
| --- | --- | --- |
| New-hire notification to TAK | Employer must notify TAK of each new employee | **At least one day before** the employee starts work. (PwC — tax administration) |

## Section 13 -- Penalties

**[RESEARCH GAP — reviewer to confirm exact figures]** Law No. 03/L-222 on Tax Administration and Procedures prescribes fixed administrative fines for late filing (a graduated schedule), but the exact EUR amounts were not extracted in this research. Only the understatement penalty band and the monthly interest mechanism are confirmed.

**Penalties table**

| Trigger | Consequence |
| --- | --- |
| Late submission of a tax return (incl. the WM declaration) | Fixed mandatory administrative fines under Law No. 03/L-222 (graduated fixed amounts). **[Exact EUR schedule unconfirmed — reviewer to supply.]** (PwC — corporate tax administration) |
| Understatement / under-declaration of tax | **15% to 25% of the under-declared tax**, depending on the magnitude of the understatement. (PwC — corporate tax administration) |
| Late payment of tax / contributions | **Interest accrues monthly** (per month or part-month) at a rate set annually by the Ministry of Finance, marginally above the commercial bank lending rate; calculated for up to 10 years from the due date. (Law No. 03/L-222) |
| Record-keeping | **[RESEARCH GAP — retention period not confirmed in this research; reviewer to confirm against Law No. 03/L-222.]** |

## Section 14 -- Excel Working Paper Template

**Excel Working Paper Template**

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | Fiscal/personal number | Input | TAK / employee ID |
| C | Employer status (P/S) | Input | P = primary (progressive), S = secondary (flat 10%) |
| D | Gross salary (EUR) | Input | paga bruto |
| E | Employee pension (5%) | Computed | `D * 5%` |
| F | Taxable BIK (excess over 65) | Input/Computed | `MAX(bik - 65, 0)` |
| G | PIT base | Computed | `D - E + F` |
| H | PIT — band 1 (0%) | Computed | `0` |
| I | PIT — band 2 (8%) | Computed | `IF(C="S", 0, MAX(MIN(G,450)-250,0) * 8%)` |
| J | PIT — band 3 (10%) | Computed | `IF(C="S", G*10%, MAX(G-450,0) * 10%)` |
| K | PIT withheld | Computed | `H + I + J` |
| L | Net pay | Computed | `D - E - K` |
| M | Employer pension (5%) | Computed | `D * 5%` |
| N | Total employer cost | Computed | `D + M` |

Footer checks: sum of column K ties to the WM declaration PIT line; sum of (E + M) ties to the KPST pension remittance (10% of total gross); sum of L ties to the total net wages disbursed; sum of N ties to total employer cost. For a secondary employer (C="S"), the flat 10% applies to the whole PIT base (column J), and columns H and I are zero. **[T2-4]**

## Section 15 -- Kosovo Bank Statement & Terminology Reading Guide

**Terminology Reading Guide**

| Albanian / term | English | Relevance |
| --- | --- | --- |
| Paga bruto | Gross salary | Starting figure for all computations |
| Paga neto | Net salary | What the employee receives |
| Tatimi mbi pagat / tatimi në burim | Wage tax / withholding tax | PIT withheld monthly |
| Tatimi në të ardhura personale | Personal income tax (PIT) | The tax being withheld |
| Kontributi pensional | Pension contribution | 5% employee + 5% employer |
| KPST / Trusti i Kursimeve Pensionale | Kosovo Pension Savings Trust | Receives the mandatory pension |
| ATK / TAK / Administrata Tatimore e Kosovës | Tax Administration of Kosovo | Receives PIT; runs the EDI system |
| EDI | Electronic declaration system | Electronic filing of the WM declaration |
| WM | Wage / withholding declaration | Monthly PIT + pension declaration **[T2-3]** |
| Paga minimale | Minimum wage | EUR 350 (2025) / EUR 425 (Jan 2026) / EUR 500 (Jul 2026) |
| Përfitim në natyrë | Benefit in kind | Taxable above EUR 65/month |
| Punëdhënësi parësor | Primary employer | Applies progressive 0%/8%/10% bands |
| Punëdhënësi dytësor | Secondary employer | Applies flat 10% |
| Meditje | Per diem / travel allowance | May be tax-exempt up to limits (verify) |
| BQK | Central Bank of Kosovo | Supervises KPST |

## Section 16 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 6 conservative default and clearly flag the assumption. 1. What is the employee's gross monthly salary in EUR? 2. Is this the employee's primary or secondary employer? (Primary → progressive 0%/8%/10%; secondary → flat 10%.) 3. Which month and year is this pay run for? (Determines minimum wage and band figures — 2025 vs 2026.) 4. Is any benefit in kind provided, and what is its monthly value? (Taxable above EUR 65/month.) 5. Is any voluntary supplementary pension elected, and by whom? (If none → mandatory 5% + 5% only.) 6. Is the employee a new hire this period? (Triggers TAK notification at least one day before the start date.)

## Section 17 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (PIT + mandatory pension) | **This skill (kosovo-payroll.md)** |
| Kosovo personal income tax (annual / self-employment) | kosovo-income-tax.md |
| Kosovo VAT (TVSH) returns | kosovo-vat.md |
| Cross-border / posted workers / coordination | cross-border-payroll-coordination.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- Payroll → Bookkeeping: Gross wages and the 5% employer pension are expenses; withheld PIT and the 5% employee pension are liabilities until remitted via the monthly WM declaration.
- Payroll → Income tax: Employees with more than one employer (primary + secondary, the latter withheld at flat 10%) reconcile on the annual PIT return due 31 March.
- Payroll → Pension: Mandatory contributions (5% + 5%) paid through payroll build the employee's KPST pension entitlement.

## Section 18 -- Reference Material

**Reference Material table**

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Kosovo — Individual — Taxes on personal income (annual bands, tax year) | PwC Worldwide Tax Summaries (last reviewed 13 Jan 2026) | https://taxsummaries.pwc.com/kosovo/individual/taxes-on-personal-income |
| 2 | Kosovo — Individual — Other taxes (mandatory & voluntary pension, base cap) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/kosovo/individual/other-taxes |
| 3 | Kosovo — Individual — Tax administration (filing deadlines, new-hire notice) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/kosovo/individual/tax-administration |
| 4 | Kosovo — Individual — Income determination (BIK EUR 65 threshold, monthly computation) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/kosovo/individual/income-determination |
| 5 | Kosovo — Corporate — Tax administration (15%–25% understatement penalty, late-payment interest) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/kosovo/corporate/tax-administration |
| 6 | Kosovo Tax Agency Announces Changes to Personal Income Tax Rates (monthly EUR 250/450 bands, removal of 4% band, secondary-employer 10%) | Bloomberg Tax/Law | https://news.bloomberglaw.com/crypto/kosovo-tax-agency-announces-changes-to-personal-income-tax-rates |
| 7 | Law No. 03/L-222 on Tax Administration and Procedures (penalties and interest) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/wp-content/uploads/2017/07/Ligji-_03-L-222_E.pdf |
| 8 | Notice to taxpayers — Personal Income Tax rates are changed (Law No. 08/L-142, eff. 23 Aug 2024) | Tax Administration of Kosovo (ATK) | https://www.atk-ks.org/en/notice-to-taxpayers-personal-income-tax-rates-are-changed/ |
| 9 | Kosovo minimum wage decision — EUR 425 (Jan 2026) / EUR 500 (Jul 2026), prior EUR 350 | Balkanweb / News24 (reporting Government decision 10/273) | https://www.balkanweb.com/en/425-euro-nga-janari-dhe-500-nga-korriku-hyn-ne-fuqi-vendimi-per-pagen-minimale-ne-kosove/ |
| 10 | Minimum Wage Updated in Kosovo from 01 January 2026 | WageIndicator.org | https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2026/minimum-wage-updated-in-kosovo-from-01-january-2026-january-01-2026 |

Primary authorities: Tax Administration of Kosovo — TAK/ATK (https://www.atk-ks.org); Kosovo Pension Savings Trust — KPST (https://www.trusti.org); Central Bank of Kosovo — BQK (https://www.bqk-kos.org); filing via the TAK EDI electronic declaration system. **Research caveat:** Several figures rely on TAK/EDI mechanics summarized by PwC and Bloomberg Law rather than a direct fetch of the ATK page, because atk-ks.org repeatedly failed with a TLS certificate-verification error during the research session. The WM form code, the pension base EUR maximum cap, and the fixed EUR late-filing fine amounts were not verified against live ATK pages and are flagged as Tier 2 items or research gaps above.

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2025 figures, mandatory pension 5% + 5%, and the Section 2 PIT-base method (gross − 5% pension + BIK above 65).
1. Standard primary earner. EUR 500 gross, primary, no BIK. Expect: pension EUR 25.00, PIT base EUR 475.00, PIT EUR 18.50 (0 + 16.00 + 2.50), net EUR 456.50, employer pension EUR 25.00, total employer cost EUR 525.00.
2. Minimum-wage worker (2025). EUR 350 gross, primary. Expect: pension EUR 17.50, PIT base EUR 332.50, PIT EUR 6.60, net EUR 325.90, employer cost EUR 367.50.
3. 0% band only. EUR 250 gross, primary. Expect: pension EUR 12.50, PIT base EUR 237.50, PIT EUR 0.00, net EUR 237.50, employer cost EUR 262.50.
4. All three bands. EUR 1,000 gross, primary. Expect: pension EUR 50.00, PIT base EUR 950.00, PIT EUR 66.00 (0 + 16.00 + 50.00), net EUR 884.00, employer cost EUR 1,050.00.
5. Secondary employer flat rate. EUR 800 gross, secondary. Expect: pension EUR 40.00, PIT base EUR 760.00, PIT EUR 76.00 (flat 10%, no 0%/8% band), net EUR 684.00, employer cost EUR 840.00.
6. Benefit in kind. EUR 600 cash gross + EUR 100/month BIK, primary. Expect: taxable BIK EUR 35.00 (100 − 65), pension EUR 30.00, PIT base EUR 605.00, PIT EUR 31.50 (0 + 16.00 + 15.50), net cash EUR 538.50, employer cash cost EUR 630.00.
7. 8%-band ceiling check. Confirm the maximum tax in the 8% band is EUR 16.00 (8% × the EUR 200 band width) for any primary employee whose base reaches EUR 450.
8. Annual = monthly × 12 check. Confirm the annual bands (3,000 / 5,400) equal the monthly bands (250 / 450) × 12, and that each pay run uses the MONTHLY bands.
9. Employer-cost-only check. Confirm the 5% employer pension is added on top of gross, is NEVER deducted from the employee's net pay, and that PIT is NOT an employer cost.
10. Pension split check. Confirm the mandatory pension is exactly 5% employee + 5% employer = 10% of gross, with no voluntary top-up assumed.
11. Filing check. Confirm PIT AND pension contributions are declared together on the monthly WM declaration via the TAK EDI system, due the 15th of the following month, with the annual PIT return due 31 March.
12. Primary/secondary fallback. Status unknown — confirm the skill treats a known second job as secondary (flat 10%) and flags the assumption, rather than defaulting to the progressive bands.

## PROHIBITIONS

- **Prohibitions list** — - NEVER apply the progressive 0%/8%/10% bands at a SECONDARY employer — a secondary employer withholds a flat 10%. - NEVER reintroduce the 4% band — it was removed by Law No. 08/L-142, effective 23 August 2024. - NEVER deduct the 5% employer pension contribution from the employee's net pay — it is an employer cost paid on top of gross. - NEVER treat PIT as an employer cost — PIT is fully employee-borne via withholding. - NEVER apply the ANNUAL bands (3,000 / 5,400) to a single pay run — each pay run uses the MONTHLY bands (250 / 450). - NEVER tax the first EUR 65/month of benefits in kind — only the excess above EUR 65 enters the PIT base. - NEVER assume voluntary supplementary pension — apply the mandatory 5% + 5% only unless an election is confirmed; only the mandatory amount is tax-deductible. - NEVER apply a pension base cap with an invented EUR maximum — the EUR cap figure is an unconfirmed RESEARCH GAP; route high earners to a reviewer. - NEVER run a full-time employee below the statutory minimum wage (EUR 350 in 2025; EUR 425 from 1 Jan 2026). - NEVER apply the EUR 425 or EUR 500 minimum wage to a 2025 pay period — those take effect in 2026. - NEVER miss the monthly WM deadline (15th of the following month) or the annual PIT return deadline (31 March). - NEVER quote a specific late-filing fine amount or pension base cap — those are unconfirmed RESEARCH GAPS pending reviewer confirmation. - NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Kosovo accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Kosovo) before implementation.

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
