---
name: montenegro-social-contributions
description: Use this skill whenever asked about Montenegro social security contributions and payroll deductions for employees, self-employed individuals (entrepreneurs), or employers. Trigger on phrases like "Montenegro social contributions", "PIO contribution", "pension and disability insurance Montenegro", "how much salary tax in Montenegro", "Montenegrin payroll", "Europe Now reform", "Evropa sad", "IOPPD return", "net to gross Montenegro", "employer cost Montenegro", "Montenegro minimum wage", "prirez surtax", or any question about Montenegrin salary taxes and contributions. Also trigger when classifying bank statement transactions that relate to Poreska uprava / Uprava prihoda i carina debits, salary payments, or social contribution remittances from Montenegrin banks (CKB, NLB, Hipotekarna, Lovćen, Erste, Prva banka). Also trigger when computing personal income tax (porez na dohodak) on salary under the post-October-2024 "Europe Now 2.0" schedule, or when reconciling the IOPPD monthly return. This skill covers the post-reform employee PIO (10%), unemployment (0.5% + 0.5%), abolished health contribution (0%), Labour Fund (0.2%), the 0/9/15% salary PIT bands, the EUR 700 exemption, the municipal surtax, minimum-wage floors, the IOPPD filing cycle, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Montenegrin social-contribution or salary-tax work.
version: 0.1
jurisdiction: ME
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro Social Security Contributions & Salary Tax

## Montenegro Social Security Contributions & Salary Tax Skill v0.1

> **Tier 2 — research-verified, NOT accountant-verified.** Figures are drawn from PwC Worldwide Tax Summaries (last reviewed 27 March 2026) and corroborating law-firm commentary (BDK Advokati, CEE Legal Matters), **not** directly from the Montenegrin Official Gazette or a downloadable Poreska uprava rate schedule. A warranted Montenegrin accountant must confirm every figure against the current Law on Mandatory Social Insurance Contributions and the latest minimum-wage decree before this skill is used for filing. See Section 11 for known research gaps.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Montenegro (Crna Gora) |
| Primary legislation | Law on Mandatory Social Insurance Contributions (*Zakon o doprinosima za obavezno socijalno osiguranje*), as amended by "Europe Now" (2022) and "Europe Now 2.0" (effective ~1 Oct 2024) [PwC; BDK Advokati] |
| Supporting legislation | Personal Income Tax Law (*Zakon o porezu na dohodak fizičkih lica*); Corporate Profit Tax Law; VAT Law [PwC] |
| Tax authority | Poreska uprava Crne Gore / Uprava prihoda i carina Crne Gore (Tax Administration / Revenue and Customs Administration), Ministry of Finance [gov.me/en/taxadministration] |
| E-filing portal | ePrijava / Taxis — https://eprijava.tax.gov.me [gov.me] |
| Currency | EUR (Montenegro uses the euro unilaterally) [PwC] |
| Employee PIO (pension/disability) | 10% of gross salary [PwC] |
| Employee unemployment | 0.5% of gross salary [PwC] |
| Employee health | 0% — abolished [CEE Legal Matters; Europe Now reforms] |
| **Combined employee contribution** | **10.5% of gross salary** (10% PIO + 0.5% unemployment) [TaxRavens] |
| Employer PIO | 0% — eliminated by Europe Now 2.0 (previously 5.5%) [PwC; BDK Advokati] |
| Employer unemployment | 0.5% of gross salary [PwC] |
| Employer Labour Fund (Fond rada) | 0.2% of gross salary [TaxRavens — verify, see §11] |
| **Combined employer contribution** | **~0.7% of gross salary** (0.5% unemployment + 0.2% Labour Fund) [TaxRavens] |
| Salary PIT | 0% to EUR 700; 9% on EUR 700.01–1,000; 15% above EUR 1,000 (monthly gross) [PwC] |
| Municipal surtax (prirez) | 13% of the PIT amount in most municipalities; 15% in Podgorica and Cetinje [PwC] |
| PIO annual ceiling | EUR 68,765/year (PwC, stated "for 2024") — **lowest-confidence figure, see §11** [PwC] |
| Net minimum wage (standard) | EUR 670/month (roles up to secondary education) [countryeconomy.com] |
| Net minimum wage (degree roles) | EUR 800/month (university-degree roles; dual structure from Sept 2024) [countryeconomy.com] |
| Monthly payroll return | IOPPD — filed electronically to Poreska uprava by the 15th of the following month, paid simultaneously [Mellow] |
| Validated by | Pending — requires sign-off by a warranted Montenegrin accountant |
| Validation date | Pending |

**Read this whole section before computing or classifying anything.**

**Has personal income tax?** Yes. Montenegro levies a progressive personal income tax on salary on top of social contributions. This skill computes both the contributions and the salary PIT, because in Montenegrin payroll they are withheld and remitted together on a single IOPPD return.

## Section 2 — Rate and contribution tables

### 2.1 Social contribution rates (post-"Europe Now 2.0", effective ~1 Oct 2024)

**Social contribution rates table**  _(PwC / CEE Legal Matters / TaxRavens)_

| Contribution | Employee | Employer | Total | Source |
| --- | --- | --- | --- | --- |
| Pension & disability (PIO) | 10.0% | 0.0% | 10.0% | PwC |
| Unemployment insurance | 0.5% | 0.5% | 1.0% | PwC |
| Health insurance | 0.0% | 0.0% | 0.0% (abolished) | CEE Legal Matters |
| Labour Fund (Fond rada) | 0.0% | 0.2% | 0.2% | TaxRavens — verify, §11 |
| **Total contributions** | **10.5%** | **0.7%** | **11.2%** | TaxRavens |

- **All rates basis** — All rates are a percentage of gross salary, subject to the minimum-wage floor (§2.4) and the PIO annual ceiling (§2.5).  _(§2.4, §2.5)_

**Arithmetic check.** Employee column: 10.0 + 0.5 + 0.0 + 0.0 = **10.5%**. Employer column: 0.0 + 0.5 + 0.0 + 0.2 = **0.7%**. Total column: 10.0 + 1.0 + 0.0 + 0.2 = **11.2%**, which equals 10.5% + 0.7%. Consistent.

> These supersede the pre-reform burden (employee ~24%, employer ~10%) that many EOR/payroll websites still publish. **Treat any pre-October-2024 rate table as STALE.** [TaxRavens; §11 caveat 6]

### 2.2 Personal income tax on salary (monthly gross) — 0 / 9 / 15

**PIT bands table**  _(PwC)_

| Band (monthly gross) | Rate | Source |
| --- | --- | --- |
| EUR 0 – 700.00 | 0% (fully exempt) | PwC |
| EUR 700.01 – 1,000.00 | 9% on the portion in this band | PwC |
| Above EUR 1,000.00 | 15% on the portion above EUR 1,000 | PwC |

**Marginal-tax build-up table**

| Gross monthly | PIT computed | Running PIT |
| --- | --- | --- |
| 700.00 | 0% × 700 | EUR 0.00 |
| 1,000.00 | + 9% × 300 (700.01→1,000) | EUR 27.00 |
| above 1,000 | + 15% × (gross − 1,000) | EUR 27.00 + 0.15 × (gross − 1,000) |

**Marginal-tax build-up (this skill uses the progressive/marginal reading — see §11 caveat 3):**

So the maximum PIT in the 9% band is **9% × 300 = EUR 27.00**, and PIT on any gross above EUR 1,000 is **EUR 27.00 + 15% × (gross − 1,000)**.

### 2.3 Municipal surtax (prirez)

- **Surtax basis** — The surtax is charged on the assessed PIT amount, not on income.  _(PwC)_

**Municipal surtax table**  _(PwC)_

| Municipality | Surtax rate (on PIT amount) | Source |
| --- | --- | --- |
| Podgorica, Cetinje | 15% | PwC |
| All other municipalities | 13% | PwC |

### 2.4 Minimum-wage floors (net)

**Minimum-wage floors table**  _(countryeconomy.com)_

| Role category | Net minimum/month | Source |
| --- | --- | --- |
| Up to secondary-school (high-school) diploma | EUR 670 | countryeconomy.com |
| University-degree-required roles | EUR 800 | countryeconomy.com |

- **Contribution base floor** — The effective contribution base cannot fall below the applicable net minimum wage grossed up. **The exact gross-up factor is a RESEARCH GAP — reviewer to confirm against the SSC Law.**  _(PwC)_

### 2.5 PIO annual ceiling

- **PIO annual ceiling** — EUR 68,765 (stated for 2024) EUR/year  _(PwC)_

**This is the single lowest-confidence number in the skill — see §11 caveat 1. One secondary source (TaxRavens) cites a materially lower figure (~EUR 54,533/year), which is unreconciled.**

### 2.6 Reference — corporate profit tax (CIT) and VAT (context only)

**CIT and VAT reference table**  _(PwC)_

| Tax | Rate | Source |
| --- | --- | --- |
| CIT — profit up to EUR 100,000 | 9% | PwC |
| CIT — profit EUR 100,000.01 – 1,500,000 | EUR 9,000 + 12% on profit above EUR 100,000 | PwC |
| CIT — profit above EUR 1,500,000 | EUR 177,000 + 15% on profit above EUR 1,500,000 | PwC |
| VAT standard | 21% | PwC |
| VAT reduced | 7% (bread, milk/dairy, medicines, schoolbooks) | PwC |
| VAT — exports | 0% | PwC |

These are not part of payroll but are listed so an agent does not misattribute a CIT/VAT line as a contribution.

**CIT cumulative-tax check.** At EUR 100,000 profit: 9% × 100,000 = EUR 9,000 ✓ (matches the base of the second band). At EUR 1,500,000: EUR 9,000 + 12% × (1,500,000 − 100,000) = 9,000 + 12% × 1,400,000 = 9,000 + 168,000 = **EUR 177,000** ✓ (matches the base of the third band). Consistent. [A 15% VAT figure also appears on PwC for certain hospitality/accommodation supplies — see §11 caveat 4; treat 7% as the standard reduced rate.]

## Section 3 — Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown exact employee/employer split | Employee = 10.5% of gross (10% PIO + 0.5% unemployment); employer = ~0.7% (0.5% unemployment + 0.2% Labour Fund) [TaxRavens] |
| Labour Fund cannot be confirmed for the period | Use employer 0.5% (unemployment only); flag that Labour Fund 0.2% may also apply [§11] |
| Municipality not stated | Apply 15% surtax (Podgorica/Cetinje high case) as the conservative figure [PwC] |
| Gross salary unknown but minimum-wage role | Use the grossed-up applicable net minimum (EUR 670 standard / EUR 800 degree role) as the floor [countryeconomy.com] |
| 15% PIT band mechanics unclear | Use the marginal reading (15% only on the portion above EUR 1,000) but flag for reviewer [§11 caveat 3] |
| PIO ceiling relevance unclear | Apply the EUR 68,765 cap but mark it [RESEARCH GAP — reviewer to confirm] [§11 caveat 1] |
| Salary in non-EUR currency | STOP — Montenegro is EUR-only; convert and confirm rate before computing |

## Section 4 — Required inputs and refusal catalogue

### Required inputs

- **Required inputs** — **Minimum viable** — monthly gross salary in EUR and worker type (employee vs entrepreneur/self-employed). Without gross salary, STOP; do not compute. **Recommended** — municipality of the employer (for surtax 13% vs 15%), role qualification level (for the minimum-wage floor), and whether annual income approaches the PIO ceiling. **Ideal** — the employer's IOPPD return for the month, the employment contract (gross vs net agreed), and a bank statement showing the salary debit and the contribution/tax remittances.

### Refusal catalogue

- **R-ME-SSC-1** — Trigger: the input cites employee ~24% / employer ~10%, or a residual health-insurance contribution. Message: "Those are pre-October-2024 rates. Europe Now 2.0 reduced the employee burden to 10.5% (10% PIO + 0.5% unemployment), eliminated the employer PIO contribution, and abolished health contributions. Recompute using the post-reform schedule and confirm the period."  _(§11 caveat 6)_
- **R-ME-SSC-2** — Trigger: annual income is at or above ~EUR 55,000 and the result depends on the PIO cap. Message: "The PIO annual ceiling is the lowest-confidence figure in this skill — PwC states EUR 68,765 'for 2024' while another source cites ~EUR 54,533. Do not finalise a high-earner computation that turns on the cap without a warranted accountant confirming the current ceiling."  _(§11 caveat 1)_
- **R-ME-SSC-3** — Trigger: self-employed worker whose contribution base or whether the activity is the primary income source is unclear. Message: "Self-employed contributions depend on the base used and whether the activity is the worker's primary income source. Confirm the base and primary-source status per case before computing."  _(§11 caveat 7)_
- **R-ME-SSC-4** — Trigger: unpaid IOPPD or contribution arrears. Message: "Specific Montenegrin penalty and default-interest amounts were not confirmed from an authoritative source in this skill's research. Default interest accrues and fines apply, but do not quantify arrears — escalate to a warranted accountant."  _(§11 caveat 5)_
- **R-ME-SSC-5** — Trigger: the question is actually about VAT or corporate profit tax. Message: "That is a VAT (21%/7%) or CIT (9/12/15%) matter, not a payroll contribution. The §2.6 reference is context only; load the relevant Montenegro VAT or CIT skill before advising."

## Section 5 — Payment / transaction pattern library

This is the deterministic pre-classifier for bank statement transactions related to Montenegrin payroll, social contributions, and salary tax. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement.

**Key principle.** Employee contributions and PIT are statutory deductions withheld from the gross — they are not separate business supplies and EXCLUDE from any VAT return. Employer contributions are a payroll cost.

### 5.1 Contribution & salary-tax remittances to the tax authority

**Contribution & salary-tax remittance patterns**

| Pattern (Montenegrin / English) | Treatment | Notes |
| --- | --- | --- |
| PORESKA UPRAVA | EXCLUDE — tax/contribution remittance | Tax Administration |
| UPRAVA PRIHODA I CARINA, UPC | EXCLUDE — tax/contribution remittance | Revenue & Customs Administration |
| DOPRINOSI, DOPRINOS | EXCLUDE — social contribution remittance | "contributions" |
| PIO, PENZIJSKO, PENZIJSKO I INVALIDSKO | EXCLUDE — pension/disability contribution | PIO |
| ZA NEZAPOSLENOST, OSIGURANJE OD NEZAPOSLENOSTI | EXCLUDE — unemployment insurance |  |
| FOND RADA | EXCLUDE — Labour Fund contribution | Employer 0.2% [verify, §11] |
| POREZ NA DOHODAK, POREZ NA ZARADE | EXCLUDE — salary PIT remittance | Personal income tax on salary |
| PRIREZ | EXCLUDE — municipal surtax remittance | On PIT amount |
| IOPPD | EXCLUDE — combined PIT+contribution remittance | Monthly return payment |

### 5.2 Contribution remittances on specific Montenegrin banks

**Bank remittance patterns**

| Bank | Typical reference | Treatment |
| --- | --- | --- |
| CKB (Crnogorska komercijalna banka) | "PORESKA UPRAVA" / "DOPRINOSI" | EXCLUDE — remittance |
| NLB Banka | "UPRAVA PRIHODA" / "POREZ NA ZARADE" | EXCLUDE — remittance |
| Hipotekarna banka | "DOPRINOSI" / "PIO" | EXCLUDE — remittance |
| Lovćen banka | "PORESKA UPRAVA" | EXCLUDE — remittance |
| Erste Bank (Podgorica) | "POREZ I DOPRINOSI" | EXCLUDE — remittance |
| Prva banka Crne Gore | "DOPRINOSI / POREZ" | EXCLUDE — remittance |

### 5.3 Salary / payroll lines (not a contribution remittance)

**Salary/payroll line patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ZARADA, NETO ZARADA, PLATA (outgoing) | EXCLUDE — net salary payment to employee | The contributions/PIT are remitted separately to Poreska uprava |
| ZARADA, PLATA (incoming) | EXCLUDE — employment income received | Not a contribution |
| AKONTACIJA ZARADE | EXCLUDE — salary advance | Not a contribution |

### 5.4 Other tax lines (do NOT confuse with payroll contributions)

**Other tax line patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PDV, POREZ NA DODATU VRIJEDNOST | EXCLUDE here — VAT, not a contribution | Load the VAT skill |
| POREZ NA DOBIT | EXCLUDE here — corporate profit tax | Not payroll |
| PENZIJA, PENZIJSKI ČEK (incoming) | EXCLUDE — pension benefit received | Not a contribution paid |

## Section 6 — Worked examples

Six examples for a hypothetical Montenegrin employer running payroll, with realistic bank-statement lines in EUR. All PIT uses the marginal reading (§2.2) and the named municipality's surtax (§2.3). All amounts are recomputed to the cent.

### Example 1 — Salary at the EUR 700 exemption ceiling (Podgorica)

**Input line:**
`05.02.2025 ; ZARADA — M. POPOVIĆ JAN 2025 ; DEBIT ; NETO ZARADA ; -626.50 ; EUR`

**Reasoning (gross EUR 700.00):**
- PIT: 0% × 700 = **EUR 0.00** (entirely within the exempt band).
- Surtax: 15% × 0 = **EUR 0.00**.
- Employee PIO: 10% × 700 = EUR 70.00.
- Employee unemployment: 0.5% × 700 = EUR 3.50.
- Total employee deductions = 0 + 0 + 70.00 + 3.50 = **EUR 73.50**.
- Net pay = 700.00 − 73.50 = **EUR 626.50** ✓ (matches the statement line).
- Employer contributions: 0.5% × 700 = EUR 3.50 + 0.2% × 700 = EUR 1.40 = EUR 4.90. Total employer cost = 700 + 4.90 = **EUR 704.90**.

**Classification:** Net salary EXCLUDE from VAT; contributions + PIT remitted via IOPPD by 15 Feb 2025.

### Example 2 — Salary at the EUR 1,000 band ceiling (Podgorica, 15% surtax)

**Input line:**
`05.03.2025 ; ZARADA — A. VUKOVIĆ FEB 2025 ; DEBIT ; NETO ZARADA ; -863.95 ; EUR`

**Reasoning (gross EUR 1,000.00):**
- PIT: 0% × 700 = 0; 9% × (1,000 − 700) = 9% × 300 = EUR 27.00; nothing above 1,000. PIT = **EUR 27.00**.
- Surtax: 15% × 27.00 = **EUR 4.05**.
- Employee PIO: 10% × 1,000 = EUR 100.00.
- Employee unemployment: 0.5% × 1,000 = EUR 5.00.
- Total employee deductions = 27.00 + 4.05 + 100.00 + 5.00 = **EUR 136.05**.
- Net pay = 1,000.00 − 136.05 = **EUR 863.95** ✓.
- Employer cost: 0.5% × 1,000 = 5.00 + 0.2% × 1,000 = 2.00 = EUR 7.00. Total = 1,000 + 7.00 = **EUR 1,007.00**.

**Classification:** EXCLUDE from VAT; remit via IOPPD by 15 Mar 2025.

### Example 3 — Mid-level salary (Podgorica, 15% surtax)

**Input line:**
`05.04.2025 ; ZARADA — J. NIKOLIĆ MAR 2025 ; DEBIT ; NETO ZARADA ; -1,586.45 ; EUR`

**Reasoning (gross EUR 2,000.00):**
- PIT: 0 + 9% × 300 + 15% × (2,000 − 1,000) = 27.00 + 150.00 = **EUR 177.00**.
- Surtax: 15% × 177.00 = **EUR 26.55**.
- Employee PIO: 10% × 2,000 = EUR 200.00.
- Employee unemployment: 0.5% × 2,000 = EUR 10.00.
- Total employee deductions = 177.00 + 26.55 + 200.00 + 10.00 = **EUR 413.55**.
- Net pay = 2,000.00 − 413.55 = **EUR 1,586.45** ✓.
- Employer cost: 0.5% × 2,000 = 10.00 + 0.2% × 2,000 = 4.00 = EUR 14.00. Total = 2,000 + 14.00 = **EUR 2,014.00**.

**Classification:** EXCLUDE from VAT; remit via IOPPD by 15 Apr 2025.

### Example 4 — Higher salary in a 13%-surtax municipality (Nikšić)

**Input line:**
`05.05.2025 ; ZARADA — S. ĐUROVIĆ APR 2025 ; DEBIT ; NETO ZARADA ; -2,678.24 ; EUR`

**Reasoning (gross EUR 3,500.00, Nikšić → 13% surtax):**
- PIT: 0 + 9% × 300 + 15% × (3,500 − 1,000) = 27.00 + 375.00 = **EUR 402.00**.
- Surtax: 13% × 402.00 = **EUR 52.26**.
- Employee PIO: 10% × 3,500 = EUR 350.00.
- Employee unemployment: 0.5% × 3,500 = EUR 17.50.
- Total employee deductions = 402.00 + 52.26 + 350.00 + 17.50 = **EUR 821.76**.
- Net pay = 3,500.00 − 821.76 = **EUR 2,678.24** ✓.
- Employer cost: 0.5% × 3,500 = 17.50 + 0.2% × 3,500 = 7.00 = EUR 24.50. Total = 3,500 + 24.50 = **EUR 3,524.50**.

**Classification:** EXCLUDE from VAT; remit via IOPPD by 15 May 2025.

### Example 5 — Contribution/tax remittance to the tax authority (not salary)

**Input line:**
`14.04.2025 ; PORESKA UPRAVA CRNE GORE ; DEBIT ; IOPPD POREZ I DOPRINOSI MAR 2025 ; -190.55 ; EUR`

**Reasoning (for the Example 3 employee, gross EUR 2,000):**
This is the employer remitting, in one IOPPD payment, the withheld employee PIT + surtax + employee contributions plus the employer contributions: PIT 177.00 + surtax 26.55 = 203.55 tax; employee contributions 210.00; employer contributions 14.00. The exact split between "porez" and "doprinosi" sub-lines depends on the bank narrative; the EUR 190.55 here is illustrative of one sub-component and must be reconciled to the full IOPPD. Matches "PORESKA UPRAVA" (pattern 5.1).

**Classification:** EXCLUDE from VAT — statutory remittance. Reconcile against the filed IOPPD; flag if the bank line does not tie to the computed total.

### Example 6 — Ambiguous tax-authority debit (could be VAT or arrears)

**Input line:**
`20.06.2025 ; UPRAVA PRIHODA I CARINA ; DEBIT ; UPLATA PO RJEŠENJU ; -4,100.00 ; EUR`

**Reasoning:**
Matches "UPRAVA PRIHODA I CARINA" (pattern 5.2) but the reference "uplata po rješenju" (payment per assessment/decision) is irregular and could be VAT, CIT, a payroll arrears assessment, or penalties/default interest. Cannot allocate without the underlying *rješenje* (assessment) document. Penalty and default-interest mechanics are a research gap (§11 caveat 5).

**Classification:** EXCLUDE from VAT. Flag for reviewer — request the assessment to split principal contributions/tax (and identify whether it is payroll, VAT or CIT) from penalties/interest.

## Section 7 — Tier 1 rules

Apply exactly as written when the gross salary, worker type, and municipality are known and the figure does not turn on the PIO ceiling.

### Rule 1 — Employee deduction formula

- **Employee deduction formula** — employee_PIT     = PIT_marginal(gross)                      # 0 / 9% / 15% per §2.2 surtax           = surtax_rate × employee_PIT                # 13% or 15% per §2.3 employee_PIO     = 10%  × gross employee_unemp   = 0.5% × gross net_pay          = gross − employee_PIT − surtax − employee_PIO − employee_unemp Where PIT_marginal(gross) = 0 if gross ≤ 700; 9% × (gross − 700) if 700 < gross ≤ 1,000; 27.00 + 15% × (gross − 1,000) if gross > 1,000.  _(PwC)_

### Rule 2 — Employer cost formula

- **Employer cost formula** — employer_unemp     = 0.5% × gross employer_labourfund= 0.2% × gross      # verify per §11 total_employer_cost= gross + employer_unemp + employer_labourfund Employer PIO is 0% and employer health is 0% post-reform.  _(PwC; CEE Legal Matters)_

### Rule 3 — Health insurance is abolished

- **Health insurance abolished** — Neither employer nor employee pays a mandatory health contribution. Healthcare is budget-financed. Do not add any health line.  _(CEE Legal Matters)_

### Rule 4 — First EUR 700 of monthly gross salary is exempt

- **EUR 700 exemption** — PIT applies only above EUR 700/month.  _(PwC)_

### Rule 5 — Surtax is on the PIT amount, not on income

- **Surtax base** — surtax = surtax_rate × PIT, never surtax_rate × gross. 15% in Podgorica/Cetinje, 13% elsewhere.  _(PwC)_

### Rule 6 — Contribution base floor is the minimum wage

- **Minimum wage floor** — The effective contribution base cannot be below the applicable net minimum wage grossed up (EUR 670 standard / EUR 800 degree role). The exact gross-up is [RESEARCH GAP — reviewer to confirm].  _(countryeconomy.com; PwC)_

### Rule 7 — PIO ceiling

- **PIO ceiling application** — PIO is not levied on annual income above EUR 68,765 (PwC, "for 2024"). Above the cap, stop applying the 10% PIO. Flag the cap as low-confidence (§11 caveat 1).  _(PwC)_

### Rule 8 — Monthly remittance via IOPPD

- **IOPPD filing deadline** — The employer files the IOPPD (calculated and paid taxes and contributions on salaries) electronically to Poreska uprava via ePrijava/Taxis by the 15th of the month following the month the salary was paid; tax and contributions are remitted simultaneously with filing.  _(Mellow)_

### Rule 9 — Entrepreneurial income PIT (annual)

- **Entrepreneurial income PIT bands** — For self-employed/entrepreneurial income (not salary): 0% up to EUR 8,400; 9% on EUR 8,400.01–12,000; 15% above EUR 12,000 (annual). Self-employed pay both the employee and the (now 0%) employer portions on a base of at least the minimum wage.  _(PwC; TaxRavens)_

### Rule 10 — Combined burden shorthand

- **Combined burden shorthand** — Employee statutory deduction ≈ 10.5% of gross (contributions) plus PIT; employer cost ≈ 0.7% of gross.  _(TaxRavens)_

## Section 8 — Tier 2 catalogue (reviewer judgement)

When data is ambiguous or the result turns on a low-confidence figure, flag for reviewer.

### T2-1 — High earner near or above the PIO ceiling

**Trigger:** annual income ≈ EUR 55,000+. **Issue:** PwC's EUR 68,765 cap is a 2024 figure; TaxRavens cites ~EUR 54,533. The two are unreconciled and the 2025/2026 indexed cap is unconfirmed. **Action:** flag; do not finalise without the current SSC Law ceiling. [§11 caveat 1]

### T2-2 — 15% PIT band mechanics

**Trigger:** gross above EUR 1,000. **Issue:** sources differ on whether 15% applies to the whole gross or only the portion above EUR 1,000. This skill uses the marginal reading. **Action:** flag; confirm the exact mechanics against the PIT Law. [§11 caveat 3]

### T2-3 — Labour Fund (Fond rada) applicability

**Trigger:** any employer-cost computation. **Issue:** the 0.2% Labour Fund comes only from TaxRavens and is not itemised by PwC. **Action:** flag; if unconfirmed, present employer cost both with (0.7%) and without (0.5%) the Labour Fund. [§11 caveat 2]

### T2-4 — Self-employed / freelancer base

**Trigger:** self-employed worker, especially outbound contractors. **Issue:** the base and whether the activity is the primary income source drive the contribution. **Action:** flag; confirm base rules per case. [§11 caveat 7]

### T2-5 — Stale pre-reform rates in source documents

**Trigger:** prior workings or EOR quotes show ~24% employee / ~10% employer or a health contribution. **Issue:** these predate Europe Now 2.0 (Oct 2024). **Action:** recompute on the post-reform schedule; flag the discrepancy. [§11 caveat 6]

### T2-6 — Minimum-wage floor and gross-up

**Trigger:** low-paid or part-time worker near the EUR 670/800 floor. **Issue:** the gross-up factor that converts the net minimum to a contribution base is unconfirmed. **Action:** flag; apply the floor conservatively and confirm the gross-up. [Rule 6]

## Section 9 — Excel working paper template

MONTENEGRO PAYROLL — SALARY TAX & CONTRIBUTIONS WORKING PAPER
Employer: [name]            Employee: [name]
Month / Year: [____]        Municipality: [____]  (surtax 13% / 15%)
Prepared: [date]

INPUT DATA
  Gross monthly salary (EUR):        [____]
  Worker type:                       [Employee / Entrepreneur]
  Role qualification:                [Up to secondary / University]
  Applicable net minimum (floor):    [EUR 670 / EUR 800]
  Annual income near PIO cap?        [YES/NO — if YES, FLAG, see §11]

PERSONAL INCOME TAX (marginal, §2.2)
  Band 0–700 @ 0%:                   EUR 0.00
  Band 700.01–1,000 @ 9%:            EUR [9% × (min(gross,1000)−700)]
  Above 1,000 @ 15%:                 EUR [15% × max(gross−1000,0)]
  Total PIT:                         EUR [____]
  Surtax @ [13%/15%] of PIT:         EUR [____]

EMPLOYEE CONTRIBUTIONS
  PIO 10% × gross:                   EUR [____]
  Unemployment 0.5% × gross:         EUR [____]
  Health 0% (abolished):             EUR 0.00
  Total employee contributions:      EUR [____]   (= 10.5% × gross)

NET PAY
  Net = gross − PIT − surtax
        − employee contributions:    EUR [____]

EMPLOYER COST
  Unemployment 0.5% × gross:         EUR [____]
  Labour Fund 0.2% × gross [verify]: EUR [____]
  PIO 0%, Health 0%:                 EUR 0.00
  Total employer cost (gross + ~0.7%): EUR [____]

IOPPD REMITTANCE
  Total to Poreska uprava
    (PIT + surtax + all contributions): EUR [____]
  IOPPD filing/payment due:          15th of following month

REVIEWER FLAGS
  [List any Tier 2 / research-gap flags]

## Section 10 — Bank statement & terminology reading guide

### How payroll items appear on Montenegrin bank statements

**Net salary (outgoing to employee):** "ZARADA", "NETO ZARADA", "PLATA", "AKONTACIJA ZARADE". Recurs monthly; net of all deductions.

**Tax/contribution remittance (outgoing to authority):** "PORESKA UPRAVA", "UPRAVA PRIHODA I CARINA", "DOPRINOSI", "POREZ NA ZARADE", "PIO", "FOND RADA", "PRIREZ", "IOPPD". Typically a single combined IOPPD payment by the 15th of the following month.

**Key Montenegrin terms:**

**Key Montenegrin terms table**

| Term | Meaning |
| --- | --- |
| Zarada / plata | Salary / wage |
| Bruto / neto | Gross / net |
| Doprinosi | Contributions |
| PIO (penzijsko i invalidsko osiguranje) | Pension & disability insurance |
| Osiguranje od nezaposlenosti | Unemployment insurance |
| Zdravstveno osiguranje | Health insurance (abolished — 0%) |
| Fond rada | Labour Fund |
| Porez na dohodak / porez na zarade | Personal income tax / salary tax |
| Prirez | Municipal surtax |
| IOPPD | Monthly return of calculated & paid taxes and contributions |
| Poreska uprava | Tax Administration |
| Rješenje | Assessment / decision |

1. Net salary debits go to an individual; remittances go to "Poreska uprava" / "Uprava prihoda i carina".
2. The combined IOPPD remittance should reconcile to (employee PIT + surtax + employee contributions + employer contributions) for all employees that month.
3. Do not classify "PDV" (VAT) or "porez na dobit" (CIT) lines as payroll contributions.
4. Inbound "penzija" credits are pension benefits received, not contributions paid.

## Section 11 — Research gaps & caveats (read before relying on any figure)

**PRIMARY SOURCE LIMITATION.** Figures come from PwC Worldwide Tax Summaries (reviewed 27 March 2026) and law-firm commentary (BDK Advokati, CEE Legal Matters), not from the Montenegrin Official Gazette or a parsed Poreska uprava rate schedule. The gov.me pages and the ePrijava/Taxis portal were identified but not parsed for raw figures. A warranted Montenegrin accountant must confirm everything below before filing.

**PIO annual ceiling [LOWEST CONFIDENCE].** EUR 68,765 is explicitly a "2024" PwC figure; the 2025/2026 indexed cap is unconfirmed, and TaxRavens cites a materially lower ~EUR 54,533. [RESEARCH GAP — reviewer to confirm the current ceiling.]

**Labour Fund 0.2%.** Sourced only from TaxRavens; not itemised by PwC. [RESEARCH GAP — reviewer to confirm it still applies and at what rate.]

**15% PIT band mechanics.** Sources differ on full-gross vs marginal application above EUR 1,000. This skill uses the marginal reading. [RESEARCH GAP — reviewer to confirm.]

**VAT reduced rate.** PwC references both 7% and a 15% rate for certain hospitality/accommodation supplies. Standard reduced rate treated here as 7%. [RESEARCH GAP — reviewer to confirm the 15% reclassification.]

**Penalties & VAT registration threshold.** Specific penalty/default-interest amounts were not confirmed; the EUR 30,000 VAT registration threshold (cited by PwC) is also unconfirmed against a primary source. [RESEARCH GAP — reviewer to confirm.]

**Stale pre-reform rates.** Many EOR/payroll sites still publish employee ~24% / employer ~10% and a health contribution. These are STALE; the October-2024 Europe Now 2.0 figures in this skill supersede them.

**Self-employed/freelancer contributions.** Depend on the base and on whether the activity is the worker's primary income source. [RESEARCH GAP — confirm per case.]

**Minimum-wage gross-up.** The factor converting the EUR 670/800 net minimum into a contribution base is unconfirmed. [RESEARCH GAP — reviewer to confirm.]

## Section 12 — Reference material & test suite

### 12.1 Reference — net-pay table (marginal PIT, Podgorica 15% surtax, employee 10.5%)

**Net-pay table (marginal PIT, Podgorica 15% surtax, employee 10.5%)**  _(§2.1/§2.2 [PwC])_

| Gross/month | PIT | Surtax (15%) | Employee contrib (10.5%) | Net pay | Source basis |
| --- | --- | --- | --- | --- | --- |
| EUR 700.00 | 0.00 | 0.00 | 73.50 | 626.50 | §2.1/§2.2 [PwC] |
| EUR 1,000.00 | 27.00 | 4.05 | 105.00 | 863.95 | §2.1/§2.2 [PwC] |
| EUR 2,000.00 | 177.00 | 26.55 | 210.00 | 1,586.45 | §2.1/§2.2 [PwC] |
| EUR 3,500.00 | 402.00 | 60.30 | 367.50 | 2,670.20 | §2.1/§2.2 [PwC] |

*(Row 4 here uses Podgorica 15% surtax = 15% × 402.00 = 60.30, so net = 3,500 − 402.00 − 60.30 − 367.50 = 2,670.20. Example 4 in §6 used Nikšić 13% surtax, giving a different surtax and net — both are correct for their stated municipality.)*

**Check, row 3:** employee contrib = 10.5% × 2,000 = 210.00 ✓; net = 2,000 − 177.00 − 26.55 − 210.00 = 1,586.45 ✓.

### 12.2 Forms and deadlines

**Forms and deadlines**  _(Mellow / PwC)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| IOPPD | Monthly combined return of PIT + employee/employer contributions on salaries; e-filed via ePrijava/Taxis, paid simultaneously | 15th of the month after salary payment | Mellow |
| Annual PIT return (GPP) | Annual reconciliation for multiple-source / self-employment income | End of April following the tax year (verify exact date with Poreska uprava) | PwC |
| Corporate profit tax return | Annual CIT return | End of March following the tax year | PwC |

### 12.3 Thresholds

**Thresholds**  _(PwC)_

| Threshold | Value | Source |
| --- | --- | --- |
| Salary PIT exemption | First EUR 700/month of gross is exempt | PwC |
| Entrepreneurial income exemption | First EUR 8,400/year exempt | PwC |
| PIO annual ceiling | EUR 68,765/year (PwC "2024" — low confidence, §11) | PwC |
| VAT registration threshold | EUR 30,000 taxable turnover in preceding 12 months (verify) | PwC |

### 12.4 Penalties

**Penalties**  _(PwC)_

| Item | Detail | Source |
| --- | --- | --- |
| Late filing / late payment | Default interest on overdue taxes & contributions; fines for failure to file IOPPD or to withhold/remit. **Specific amounts not confirmed — [RESEARCH GAP, §11 caveat 5].** | PwC |

### 12.5 Test suite

**Test 1 — Gross EUR 700, Podgorica.** PIT 0.00; surtax 0.00; employee contrib 73.50; net = **EUR 626.50**. (§6 Ex 1)

**Test 2 — Gross EUR 1,000, Podgorica.** PIT = 9% × 300 = 27.00; surtax = 15% × 27 = 4.05; employee contrib = 105.00; net = 1,000 − 136.05 = **EUR 863.95**. (§6 Ex 2)

**Test 3 — Gross EUR 2,000, Podgorica.** PIT = 27 + 15% × 1,000 = 177.00; surtax = 26.55; employee contrib = 210.00; net = **EUR 1,586.45**. (§6 Ex 3)

**Test 4 — Gross EUR 3,500, Nikšić (13% surtax).** PIT = 27 + 15% × 2,500 = 402.00; surtax = 13% × 402 = 52.26; employee contrib = 367.50; net = **EUR 2,678.24**. (§6 Ex 4)

**Test 5 — Employer cost on gross EUR 2,000.** unemployment 0.5% × 2,000 = 10.00; Labour Fund 0.2% × 2,000 = 4.00; PIO 0; health 0; total employer cost = 2,000 + 14.00 = **EUR 2,014.00**.

**Test 6 — Health contribution.** Expected = **EUR 0.00** (abolished). Any non-zero health line is wrong.

**Test 7 — Entrepreneur, annual income EUR 8,400.** Entrepreneurial PIT = **EUR 0.00** (within the EUR 8,400 exemption); contributions still due on at least the minimum-wage base — flag base per §8 T2-4.

**Test 8 — Pre-reform input (employee 24%, employer 10%).** Expected response: REFUSE/recompute per R-ME-SSC-1; correct figures are employee 10.5%, employer ~0.7%.

### 12.6 Prohibitions

- **Never use pre-October-2024 rates** — NEVER use pre-October-2024 rates (employee ~24% / employer ~10%, or any health contribution) — Europe Now 2.0 superseded them.  _(§12.6)_
- **Never add health-insurance contribution** — NEVER add a health-insurance contribution — it is abolished (0%).  _(§12.6)_
- **Never compute surtax on gross** — NEVER compute surtax on gross — it is charged on the PIT amount.  _(§12.6)_
- **Never finalise high-earner result without PIO ceiling confirmation** — NEVER finalise a high-earner result that turns on the PIO ceiling without reviewer confirmation of the current cap (the EUR 68,765 figure is low-confidence).  _(§12.6)_
- **Never present Labour Fund 0.2% as certain** — NEVER present the Labour Fund 0.2% as certain — it is sourced from one secondary site; show employer cost with and without it if unconfirmed.  _(§12.6)_
- **Never apply full-gross 15% reading without flagging** — NEVER apply the full-gross 15% reading without flagging — this skill uses the marginal reading pending confirmation.  _(§12.6)_
- **Never quantify penalties or arrears** — NEVER quantify penalties or arrears — escalate to a warranted accountant.  _(§12.6)_
- **Never classify VAT or CIT as payroll contribution** — NEVER classify a VAT ("PDV") or CIT ("porez na dobit") line as a payroll contribution.  _(§12.6)_
- **Never treat figures as definitive** — NEVER treat figures as definitive — this is a Tier 2 research-verified skill; label outputs as estimates and direct the client to Poreska uprava / a warranted accountant.  _(§12.6)_
- **Never compute in non-EUR currency** — NEVER compute in a non-EUR currency without converting and confirming — Montenegro is EUR-only.  _(§12.6)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
