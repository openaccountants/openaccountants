---
name: serbia-social-contributions
description: Use this skill whenever asked about Serbian payroll taxes and mandatory social security contributions (doprinosi za obavezno socijalno osiguranje) for employees and employers in the Republic of Serbia. Trigger on phrases like "Serbia payroll tax", "how much social contributions in Serbia", "PIO contribution", "RFZO health contribution", "Serbia salary tax 10%", "non-taxable salary amount", "neoporezivi iznos", "minimum contribution base", "maximum contribution base", "PPP-PD return", "Serbia net to gross", "gross to net Serbia", "annual personal income tax Serbia", "PP GPDG", or any question about Serbian payroll, salary tax, or social insurance obligations. Also trigger when classifying bank statement transactions that relate to Poreska uprava (Tax Administration), PIO Fund, RFZO, or NSZ payments from Serbian banks (Banca Intesa, Komercijalna banka, OTP, Raiffeisen, UniCredit). This skill covers the flat 10% salary tax, the monthly non-taxable amount, employee (19.90%) and employer (15.15%) contribution rates split across PIO / RFZO / NSZ, floor/ceiling contribution bases, the consolidated PPP-PD monthly return, the annual supplementary PIT (PP GPDG), minimum wage, penalties, and bank statement classification patterns. ALWAYS read this skill before touching any Serbian payroll or social contribution work.
version: 0.1
jurisdiction: RS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Serbia Social Security Contributions & Payroll Tax

## Serbia Social Security Contributions & Payroll Tax Skill v0.1

> **Tier 2 (research-verified) skill.** Figures are drawn from PwC Worldwide Tax Summaries, KPMG Serbia tax alerts, Eurofast, Orbitax, and Serbian law-firm summaries, cross-referenced to the *Law on Personal Income Tax* and the *Law on Mandatory Social Insurance Contributions*. It has NOT yet been signed off by a Serbian licensed tax advisor. Treat every output as an estimate pending professional review. Items marked **[RESEARCH GAP — reviewer to confirm]** require a licensed Serbian advisor to verify against primary sources before production use.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Serbia (Republic of Serbia)
- **Primary legislation** — Law on Mandatory Social Insurance Contributions (Zakon o doprinosima za obavezno socijalno osiguranje); Law on Personal Income Tax (Zakon o porezu na dohodak građana)
- **Supporting legislation** — Labour Law (Zakon o radu) — minimum wage; amendments adopted Dec 2025 (Official Gazette RS); minimum wage Official Gazette RS Nos. 67/2025 and 78/2025
- **Tax authority** — Tax Administration of the Republic of Serbia (Poreska uprava) — eporezi.purs.gov.rs; Ministry of Finance (mfin.gov.rs)
- **Social funds** — PIO Fund (pension/disability, pio.rs); RFZO (health, rfzo.rs); NSZ (unemployment, nsz.gov.rs)
- **Salary tax** — Flat 10% on gross salary minus the monthly non-taxable amount  _(PwC / KPMG)_
- **Non-taxable monthly amount (2025)** — RSD 28,423 (1 Jan–31 Dec 2025)  _(Eurofast / KPMG)_
- **Non-taxable monthly amount (2026)** — RSD 34,221 (from 1 Jan 2026; next indexation 1 Jan 2027)  _(KPMG Dec 2025 alert)_
- **Employee social contribution rate** — 19.90% of gross (14% PIO + 5.15% RFZO + 0.75% NSZ)  _(PwC)_
- **Employer social contribution rate** — 15.15% of gross (10% PIO + 5.15% RFZO; no unemployment)  _(PwC)_
- **Combined social burden** — 35.05% of gross (19.90% employee + 15.15% employer)  _(PwC / Eurofast)_
- **Minimum monthly contribution base (2025)** — RSD 45,950  _(Eurofast)_
- **Minimum monthly contribution base (2026)** — RSD 51,297  _(Orbitax)_
- **Maximum monthly contribution base (2025)** — RSD 656,425  _(Eurofast)_
- **Maximum monthly contribution base (2026)** — RSD 732,820 (annual max RSD 8,793,840)  _(Orbitax)_
- **Monthly return** — PPP-PD (consolidated salary tax + contributions), filed/paid at each salary payment  _(Tax Administration / KPMG)_
- **Annual return** — PP GPDG (supplementary PIT for residents above threshold), due 15 May following year  _(KPMG)_
- **Currency** — RSD (Serbian dinar) only
- **Validated by** — Pending — requires sign-off by a Serbian licensed tax advisor
- **Validation date** — Pending

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Serbia (Republic of Serbia) |
| Primary legislation | Law on Mandatory Social Insurance Contributions (Zakon o doprinosima za obavezno socijalno osiguranje); Law on Personal Income Tax (Zakon o porezu na dohodak građana) |
| Supporting legislation | Labour Law (Zakon o radu) — minimum wage; amendments adopted Dec 2025 (Official Gazette RS); minimum wage Official Gazette RS Nos. 67/2025 and 78/2025 |
| Tax authority | Tax Administration of the Republic of Serbia (Poreska uprava) — eporezi.purs.gov.rs; Ministry of Finance (mfin.gov.rs) |
| Social funds | PIO Fund (pension/disability, pio.rs); RFZO (health, rfzo.rs); NSZ (unemployment, nsz.gov.rs) |
| Salary tax | Flat 10% on gross salary minus the monthly non-taxable amount — PwC / KPMG |
| Non-taxable monthly amount (2025) | RSD 28,423 (1 Jan–31 Dec 2025) — Eurofast / KPMG |
| Non-taxable monthly amount (2026) | RSD 34,221 (from 1 Jan 2026; next indexation 1 Jan 2027) — KPMG Dec 2025 alert |
| Employee social contribution rate | 19.90% of gross (14% PIO + 5.15% RFZO + 0.75% NSZ) — PwC |
| Employer social contribution rate | 15.15% of gross (10% PIO + 5.15% RFZO; no unemployment) — PwC |
| Combined social burden | 35.05% of gross (19.90% employee + 15.15% employer) — PwC / Eurofast |
| Minimum monthly contribution base (2025) | RSD 45,950 — Eurofast |
| Minimum monthly contribution base (2026) | RSD 51,297 — Orbitax |
| Maximum monthly contribution base (2025) | RSD 656,425 — Eurofast |
| Maximum monthly contribution base (2026) | RSD 732,820 (annual max RSD 8,793,840) — Orbitax |
| Monthly return | PPP-PD (consolidated salary tax + contributions), filed/paid at each salary payment — Tax Administration / KPMG |
| Annual return | PP GPDG (supplementary PIT for residents above threshold), due 15 May following year — KPMG |
| Currency | RSD (Serbian dinar) only |
| Validated by | Pending — requires sign-off by a Serbian licensed tax advisor |
| Validation date | Pending |

**Contribution overview (per fund):**

**Contribution overview (per fund)**

| Fund | Employee | Employer | Combined |
| --- | --- | --- | --- |
| Pension & disability (PIO) | 14% | 10% | 24% |
| Health (RFZO) | 5.15% | 5.15% | 10.30% |
| Unemployment (NSZ) | 0.75% | 0% | 0.75% |
| **TOTAL** | **19.90%** | **15.15%** | **35.05%** |

*Verify the TOTAL row: employee 14 + 5.15 + 0.75 = 19.90; employer 10 + 5.15 + 0 = 15.15; combined 24 + 10.30 + 0.75 = 35.05. All reconcile. Source: PwC Serbia — Individual — Other taxes.*

**Conservative defaults:**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown tax year (2025 vs 2026) | STOP — ask which period applies; parameters differ materially |
| Gross salary below the minimum base | Apply contributions on the minimum base (RSD 51,297/mo in 2026; RSD 45,950 in 2025) |
| Gross salary above the maximum base | Cap contributions at the maximum base (RSD 732,820/mo in 2026; RSD 656,425 in 2025) |
| Unknown number of working hours in month (min-wage check) | Ask — minimum wage is hourly x hours worked; do not assume 160 vs 184 |
| Unknown residency for annual PIT | Treat as resident and flag for reviewer; only residents file PP GPDG on worldwide income |
| Unknown whether new-hire relief applies | Do NOT apply relief; flag for reviewer (relief extended to 31 Dec 2026 — KPMG) |
| Penalty / interest quantification | Do not estimate; escalate to a licensed advisor |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Minimum viable -- the tax year (2025 or 2026) and the employee's monthly GROSS salary in RSD. Without the tax year, STOP: the non-taxable amount, the floor base and the ceiling base all differ between 2025 and 2026.

Recommended -- whether the employee is a Serbian tax resident, the number of working hours in the month (for minimum-wage adequacy checks), and whether any new-hire / start-up employment relief is claimed.

Ideal -- the employer's PPP-PD filings for the period, the employee's annual net income (for the supplementary PP GPDG), age as at 31 December (under-40 deduction), number of dependent family members, and bank statements showing remittances to Poreska uprava / PIO / RFZO / NSZ.

### Refusal catalogue

- **R-RS-SSC-1 -- Tax year not specified** — Trigger: the period (2025 vs 2026) is not provided. Message: "The Serbian non-taxable salary amount, minimum contribution base and maximum contribution base all changed between 2025 and 2026. 2025: non-taxable RSD 28,423, min base RSD 45,950, max base RSD 656,425. 2026: non-taxable RSD 34,221, min base RSD 51,297, max base RSD 732,820. Confirm the tax year before I compute anything."  _(R-RS-SSC-1)_
- **R-RS-SSC-2 -- Penalty / default-interest computation** — Trigger: client has overdue tax or contributions and wants the penalty quantified. Message: "Default interest on overdue taxes and contributions accrues daily at the statutory rate (NBS reference rate + 10 percentage points) under the Law on Tax Procedure and Tax Administration (ZPPPA), plus misdemeanour fines. The exact RSD fine ranges are not pinned in this skill [RESEARCH GAP — reviewer to confirm]. Do not estimate penalties; escalate to a licensed Serbian advisor."  _(R-RS-SSC-2)_
- **R-RS-SSC-3 -- Entrepreneur lump-sum / 'other income' contributions** — Trigger: client is a self-employed entrepreneur (paušalac), or has 'other income' (royalties, contracts of service) where contribution mechanics differ. Message: "Self-employed entrepreneurs and 'other income' use type-specific contribution bases not fully detailed in this skill [RESEARCH GAP — reviewer to confirm]. This skill covers employment income (salary). Escalate to a licensed advisor for entrepreneur or other-income contributions."  _(R-RS-SSC-3)_
- **R-RS-SSC-4 -- Cross-border / non-resident posting** — Trigger: employee is a non-resident, posted worker, or covered by an EU/bilateral social security agreement. Message: "Social security coverage for cross-border and posted workers depends on Serbia's bilateral social-security agreements and A1/certificate-of-coverage rules. This is outside the scope of this skill. Escalate to a licensed advisor."  _(R-RS-SSC-4)_
- **R-RS-SSC-5 -- New-hire / start-up employment relief** — Trigger: employer claims reduced tax/contributions for newly hired employees. Message: "New-hire employment relief (reduced contributions/tax for certain new employees) is extended through 31 December 2026 (KPMG Dec 2025 alert), but eligibility conditions and the exact relief rates are not detailed here [RESEARCH GAP — reviewer to confirm]. Do not apply the relief without reviewer confirmation."  _(R-RS-SSC-5)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for Serbian bank statement transactions related to payroll tax and social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference (payee, *primalac*, or payment description) as it appears in the bank statement. Serbian payroll tax and contribution remittances are statutory obligations — EXCLUDE them from any VAT return; they are not business supplies. Employer contributions are a deductible payroll cost; employee contributions and salary tax are amounts withheld from gross pay (not an additional employer cost).

### 3.1 Salary tax and consolidated remittances

**Salary tax and consolidated remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PORESKA UPRAVA, PURS | EXCLUDE -- tax/contributions remittance | Tax Administration; often the consolidated PPP-PD payment |
| POREZ NA ZARADE, POREZ NA ZARADU | EXCLUDE -- salary tax (10%) | "Tax on salaries" |
| PPP-PD, PPP PD | EXCLUDE -- consolidated payroll return payment | Salary tax + all contributions |
| DOPRINOSI, DOPRINOS | EXCLUDE -- social contributions | "Contributions" |

### 3.2 Fund-specific contribution remittances

**Fund-specific contribution remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PIO, FOND PIO, PENZIJSKO | EXCLUDE -- pension & disability (PIO) | 24% combined base |
| RFZO, ZDRAVSTVENO, ZDRAVSTVENO OSIGURANJE | EXCLUDE -- health (RFZO) | 10.30% combined base |
| NSZ, NEZAPOSLENOST, OSIGURANJE ZA SLUCAJ NEZAPOSLENOSTI | EXCLUDE -- unemployment (NSZ) | 0.75% (employee only) |

### 3.3 Salary / wage payments (exclude from contribution classification)

**Salary/wage payments exclude patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ZARADA, PLATA, ISPLATA ZARADE (outgoing) | EXCLUDE -- net salary paid to employee | Not a contribution payment |
| ZARADA, PLATA (incoming) | EXCLUDE -- employment income received | Not a contribution payment |
| AKONTACIJA ZARADE | EXCLUDE -- salary advance | Not a contribution payment |

### 3.4 Other tax payments (NOT payroll social contributions)

**Other tax payments patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PDV, POREZ NA DODATU VREDNOST | EXCLUDE -- VAT, not a contribution | Standard 20% / reduced 10% |
| POREZ NA DOBIT | EXCLUDE -- corporate income tax (15%) | Not a social contribution |
| POREZ PO ODBITKU, WHT | EXCLUDE -- withholding tax on non-residents (20%/25%) | Not a social contribution |
| GODISNJI POREZ, PP GPDG | EXCLUDE -- annual supplementary PIT | Personal, not employer payroll |

### 3.5 Benefit receipts (received -- not contributions)

**Benefit receipts patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENZIJA, FOND PIO (incoming) | EXCLUDE -- pension received | Benefit, not a contribution |
| NAKNADA ZA NEZAPOSLENOST | EXCLUDE -- unemployment benefit received | Benefit, not a contribution |
| BOLOVANJE, NAKNADA RFZO | EXCLUDE -- sick-leave reimbursement | Benefit, not a contribution |

## Section 4 -- Worked examples

Six payroll classifications and computations for a hypothetical Serbian employer. Unless stated, **2026 parameters** are used (non-taxable RSD 34,221; min base RSD 51,297; max base RSD 732,820) per KPMG Dec 2025 alert and Orbitax. All arithmetic recomputed end-to-end.

### Example 1 -- Standard mid-range salary (2026)

**Input line:**
`25.01.2026 ; ISPLATA ZARADE — JANUAR ; DEBIT ; ZARADA M. PETROVIC ; -108,572.10 ; RSD`

**Scenario:** Gross monthly salary RSD 150,000 (2026), resident employee, between floor and ceiling.

**Reasoning (net pay derivation):**
- Salary tax base = 150,000 − 34,221 (non-taxable) = 115,779. Salary tax = 10% x 115,779 = **11,577.90**.
- Employee contributions: base = 150,000 (within floor/ceiling). 19.90% x 150,000 = **29,850.00**.
- Net pay = 150,000 − 11,577.90 − 29,850.00 = **108,572.10** (matches the statement line).
- Employer contributions (paid on top): 15.15% x 150,000 = **22,725.00**.
- Total employer cost = 150,000 + 22,725.00 = **172,725.00**.

**Classification:** Net salary line EXCLUDE from VAT — payroll. Reconcile to the PPP-PD: salary tax RSD 11,577.90 + employee contributions RSD 29,850.00 + employer contributions RSD 22,725.00.

### Example 2 -- Salary below the minimum contribution base (2026)

**Input line:**
`25.02.2026 ; ISPLATA ZARADE — FEBRUAR ; DEBIT ; ZARADA J. JOVANOVIC ; -29,214.00 ; RSD`

**Scenario:** Part-time arrangement, gross RSD 40,000 (2026), below the floor base RSD 51,297.

**Reasoning:**
- Salary tax base = 40,000 − 34,221 = 5,779. Salary tax = 10% x 5,779 = **577.90**.
- Contribution base = max(40,000, 51,297) = **51,297** (floor applies). Employee contributions = 19.90% x 51,297 = **10,208.10**.
- Net pay = 40,000 − 577.90 − 10,208.10 = **29,214.00** (matches).
- Employer contributions = 15.15% x 51,297 = **7,771.50**.
- Total employer cost = 40,000 + 7,771.50 = **47,771.50**.

**Classification:** EXCLUDE from VAT — payroll. Note: contributions are computed on the RSD 51,297 floor even though gross pay is lower (Eurofast / Orbitax). Reviewer should also confirm minimum-wage adequacy (Section 8).

### Example 3 -- High salary above the maximum contribution base (2026)

**Input line:**
`25.03.2026 ; ISPLATA ZARADE — MART ; DEBIT ; ZARADA D. NIKOLIC ; -667,590.92 ; RSD`

**Scenario:** Senior role, gross RSD 900,000 (2026), above the ceiling base RSD 732,820.

**Reasoning:**
- Salary tax has NO contribution-base cap: base = 900,000 − 34,221 = 865,779. Salary tax = 10% x 865,779 = **86,577.90**.
- Contribution base = min(900,000, 732,820) = **732,820** (ceiling applies). Employee contributions = 19.90% x 732,820 = **145,831.18**.
- Net pay = 900,000 − 86,577.90 − 145,831.18 = **667,590.92** (matches).
- Employer contributions = 15.15% x 732,820 = **111,022.23**.
- Total employer cost = 900,000 + 111,022.23 = **1,011,022.23**.

**Classification:** EXCLUDE from VAT — payroll. The salary tax is on full gross-less-non-taxable; only contributions are capped at the ceiling base (Orbitax).

### Example 4 -- Consolidated remittance to the Tax Administration (PPP-PD)

**Input line:**
`05.02.2026 ; PORESKA UPRAVA ; DEBIT ; PPP-PD POREZ I DOPRINOSI 01/2026 ; -64,152.90 ; RSD`

**Scenario:** The employer's consolidated PPP-PD remittance for the Example 1 employee (salary tax + all contributions).

**Reasoning:**
- Salary tax = 11,577.90 + employee contributions 29,850.00 + employer contributions 22,725.00 = **64,152.90** (matches).
- This is the single consolidated PPP-PD payment that funds PIO, RFZO and NSZ plus the 10% salary tax.

**Classification:** EXCLUDE from VAT. Matches "PORESKA UPRAVA" / "PPP-PD" (patterns 3.1). Statutory remittance; the employer-contribution portion (RSD 22,725.00) is a deductible payroll cost.

### Example 5 -- VAT payment misread as a contribution (do NOT confuse)

**Input line:**
`15.02.2026 ; PORESKA UPRAVA ; DEBIT ; PDV 01/2026 ; -240,000.00 ; RSD`

**Reasoning:**
- Counterparty is "PORESKA UPRAVA" but the reference says "PDV" (VAT, pattern 3.4). This is a Value Added Tax remittance (standard 20%), NOT a payroll social contribution. Do not include it in payroll/contribution totals.

**Classification:** EXCLUDE from any contribution classification — this is VAT. Handle under the Serbia VAT skill, not this skill.

### Example 6 -- Annual supplementary PIT (PP GPDG), 2025 income

**Scenario:** A Serbian resident has net annual income of RSD 20,000,000 for 2025 (over the RSD 5,439,096 threshold), no dependents, aged over 40 at 31 Dec 2025. Compute the annual (supplementary) PIT due with PP GPDG (filed by 15 May 2026). 2025 thresholds apply.

**Reasoning (KPMG Feb 2026 alert):**
- Income above the non-taxable threshold = 20,000,000 − 5,439,096 = 14,560,904.
- Standard personal deduction = RSD 725,213. Deduction cap = 50% x 14,560,904 = 7,280,452; the RSD 725,213 deduction is below the cap, so allowed in full.
- Taxable base = 14,560,904 − 725,213 = 13,835,691.
- Band 1 (10% up to RSD 10,878,192): 10% x 10,878,192 = **1,087,819.20**.
- Band 2 (15% above RSD 10,878,192): 15% x (13,835,691 − 10,878,192) = 15% x 2,957,499 = **443,624.85**.
- Annual PIT due = 1,087,819.20 + 443,624.85 = **1,531,444.05**.

**Classification:** Personal obligation of the individual, EXCLUDE from VAT and from employer payroll. File PP GPDG online by 15 May 2026. Note: this supplementary PIT is **separate from and on top of** the monthly 10% salary tax already withheld; it is not a contribution. Reviewer to confirm the exact ordering of deductions vs the 10%/15% bracket break [RESEARCH GAP — reviewer to confirm].

## Section 5 -- Tier 1 rules

These rules apply when the data is clear and all required inputs are available. Apply exactly as written. All figures cite their source; figures without a confirmed source carry a [RESEARCH GAP] marker.

### Rule 1 -- Salary tax formula (flat 10%)

- **Salary tax formula** — salary_tax = 10% x (gross_salary - non_taxable_monthly_amount)  _(Eurofast / KPMG)_
- **Non-taxable amount / cap note** — Non-taxable amount: RSD 28,423 (2025) / RSD 34,221 (2026) — Eurofast / KPMG. The salary tax base is NOT capped by the contribution ceiling. If gross < non-taxable amount, salary tax is zero (never negative).  _(Eurofast / KPMG)_

### Rule 2 -- Employee contributions = 19.90% of the contribution base

- **Employee contributions formula** — employee_contributions = 19.90% x contribution_base = 14% PIO + 5.15% RFZO + 0.75% NSZ  _(PwC)_
- **Withholding note** — Withheld by the employer from gross pay — PwC.  _(PwC)_

### Rule 3 -- Employer contributions = 15.15% of the contribution base

- **Employer contributions formula** — employer_contributions = 15.15% x contribution_base = 10% PIO + 5.15% RFZO + 0% NSZ (no employer unemployment)  _(PwC)_
- **Paid on top note** — Paid on top of the employee's gross salary — PwC.  _(PwC)_

### Rule 4 -- Contribution base floor and ceiling

- **Contribution base clamp formula** — contribution_base = clamp(gross_salary, min_base, max_base)  _(Eurofast / Orbitax)_
- **Min base** — RSD 45,950 (2025) / RSD 51,297 (2026). Contributions are due on at least the minimum even if actual pay is lower.  _(Eurofast / Orbitax)_
- **Max base** — RSD 656,425/mo (2025) / RSD 732,820/mo (2026); annual max RSD 8,793,840 (2026). No contributions accrue above the cap.  _(Eurofast / Orbitax)_
- **Applicability of floor/ceiling** — Floor/ceiling apply to BOTH employee and employer contributions. They do NOT apply to the 10% salary tax base.

### Rule 5 -- Net pay derivation

- **Net pay and employer cost formula** — net_pay = gross_salary - salary_tax - employee_contributions total_employer_cost = gross_salary + employer_contributions

### Rule 6 -- Combined social burden = 35.05%

- **Combined social burden** — 19.90% (employee) + 15.15% (employer) = 35.05% of gross, subject to the floor/ceiling base.  _(PwC / Eurofast)_

### Rule 7 -- Monthly reporting via PPP-PD

- **Monthly reporting** — The 10% salary tax and all contributions are reported and paid via the consolidated electronic PPP-PD return at each salary payment (with the salary, not on a fixed monthly day).  _(Tax Administration / KPMG)_

### Rule 8 -- Annual (supplementary) PIT for residents — PP GPDG

- **Filing threshold and deadline** — Residents with net 2025 income above RSD 5,439,096 (3x average annual salary) must file PP GPDG by 15 May 2026.  _(KPMG)_
- **Annual PIT rates** — 10% on net income above the threshold up to RSD 10,878,192; 15% above that.  _(KPMG / PwC)_
- **Standard and dependent deductions** — Standard personal deduction RSD 725,213 (40% of average annual salary); RSD 271,955 per dependent (15%); combined deductions capped at 50% of net income.  _(KPMG)_
- **Under-40 additional deduction** — Taxpayers under 40 on 31 Dec 2025 get an additional deduction of RSD 5,439,096 on employment/self-employment income.  _(KPMG)_

### Rule 9 -- Non-taxable amount is indexed annually

- **Indexation** — The monthly non-taxable salary amount is indexed annually; the next change is scheduled for 1 January 2027. Do not roll a prior year's figure forward without confirming the published value.  _(KPMG Dec 2025 alert)_

### Rule 10 -- Minimum wage adequacy

- **Minimum wage rates** — Net minimum wage is set per working hour: RSD 308/hr (Jan–Sep 2025), RSD 337/hr (Oct–Dec 2025, Official Gazette RS 67/2025), RSD 371/hr (from 1 Jan 2026, Official Gazette RS 78/2025). Monthly minimum = hourly rate x working hours in the month (160–184 hrs). Confirm the employee's net pay is not below the applicable minimum.  _(Zunic Law / RS Partners)_

## Section 6 -- Tier 2 catalogue (reviewer judgement)

When data is ambiguous or circumstances are unclear, flag these for reviewer confirmation. Do not resolve them autonomously.

### T2-1 -- Tax-year boundary (December/January payroll)

- **Trigger / Issue / Action** — Trigger: salary paid in early January for December work, or vice versa. Issue: The non-taxable amount and contribution bases switch on 1 January. Whether the 2025 or 2026 parameters apply depends on the date of *payment*, not the period worked. Misapplying the year changes the salary tax and the floor/ceiling. Action: Flag for reviewer; confirm the payment date and which parameter set applies.

### T2-2 -- New-hire / start-up employment relief

- **Trigger / Issue / Action** — Trigger: employer claims reduced contributions/tax for newly hired employees. Issue: Relief is extended through 31 December 2026 (KPMG), but eligibility conditions and exact relief amounts are not detailed here [RESEARCH GAP — reviewer to confirm]. Action: Do NOT apply relief; flag for reviewer.

### T2-3 -- Residency for the annual PIT

- **Trigger / Issue / Action** — Trigger: individual has foreign income or split-year residency. Issue: Only Serbian residents are taxed on worldwide income via PP GPDG. Residency status drives whether and on what base the annual PIT applies. Action: Flag for reviewer; confirm residency and worldwide-income scope.

### T2-4 -- Deduction-ordering for the annual PIT

- **Trigger / Issue / Action** — Trigger: computing PP GPDG where personal/dependent deductions and the 10%/15% bracket interact. Issue: The exact ordering of deductions versus the RSD 10,878,192 bracket break, and whether the 50%-of-net-income cap is measured on gross net income or income-above-threshold, is not fully pinned [RESEARCH GAP — reviewer to confirm]. Action: Flag for reviewer before finalising the annual PIT figure.

### T2-5 -- Entrepreneurs and 'other income'

- **Trigger / Issue / Action** — Trigger: self-employed entrepreneur (lump-sum / paušalac) or 'other income' (royalties, service contracts). Issue: Contribution bases are type-specific and not detailed here [RESEARCH GAP — reviewer to confirm]. Action: Flag for reviewer; this skill covers employment income only.

### T2-6 -- Penalties and default interest

- **Trigger / Issue / Action** — Trigger: overdue tax or contributions. Issue: Default interest accrues daily (NBS reference rate + 10 p.p.) plus misdemeanour fines under ZPPPA; exact RSD fine ranges are not pinned here [RESEARCH GAP — reviewer to confirm]. Action: Do not estimate; escalate to a licensed advisor.

## Section 7 -- Excel working paper template

When producing a Serbian payroll computation, structure the working paper as follows:

```
SERBIA PAYROLL & SOCIAL CONTRIBUTIONS -- WORKING PAPER
Employer: [name]            Employee: [name]
Tax year: [2025 / 2026]     Pay period: [month/year]
Prepared: [date]

INPUT DATA
  Gross monthly salary:            RSD [____]
  Tax resident:                    [YES/NO]
  Working hours in month:          [____]
  New-hire relief claimed:         [YES/NO -> if YES, FLAG]

PARAMETERS (select by tax year)
  Non-taxable monthly amount:      RSD [28,423 (2025) / 34,221 (2026)]
  Minimum contribution base:       RSD [45,950 (2025) / 51,297 (2026)]
  Maximum contribution base:       RSD [656,425 (2025) / 732,820 (2026)]
  Net minimum wage per hour:       RSD [308 / 337 / 371 — by period]

SALARY TAX (flat 10%, no base cap)
  Salary tax base (gross - non-tax): RSD [____]
  Salary tax (10%):                  RSD [____]

CONTRIBUTION BASE
  clamp(gross, min_base, max_base):  RSD [____]

EMPLOYEE CONTRIBUTIONS (19.90%)
  PIO (14%):                         RSD [____]
  RFZO (5.15%):                      RSD [____]
  NSZ (0.75%):                       RSD [____]
  Total employee (19.90%):           RSD [____]

EMPLOYER CONTRIBUTIONS (15.15%)
  PIO (10%):                         RSD [____]
  RFZO (5.15%):                      RSD [____]
  Total employer (15.15%):           RSD [____]

RESULTS
  Net pay (gross - tax - emp.contr): RSD [____]
  Total employer cost (gross + 15.15%): RSD [____]
  Consolidated PPP-PD remittance:    RSD [salary tax + 19.90% + 15.15%]

MINIMUM-WAGE CHECK
  Monthly minimum (hourly x hours):  RSD [____]
  Net pay >= minimum?                [YES/NO -> if NO, FLAG]

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP items]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide (Serbian)

### How payroll tax and contribution remittances appear on Serbian bank statements

**Common Serbian banks:** Banca Intesa, Komercijalna banka (NLB Komercijalna), OTP banka, Raiffeisen banka, UniCredit Bank Srbija, AIK Banka.

**Tax Administration / consolidated:**
- Payee (primalac): "PORESKA UPRAVA" or "PORESKA UPRAVA RS" / "PURS"
- Reference: "PPP-PD", "POREZ NA ZARADE", "POREZ I DOPRINOSI", with a period (e.g. "01/2026")
- Amount: salary tax + employee 19.90% + employer 15.15% for the period

**Fund-specific (where remitted separately):**
- "FOND PIO" / "PIO" -- pension & disability
- "RFZO" / "ZDRAVSTVENO" -- health
- "NSZ" -- unemployment

**Key Serbian payroll terms:**
- *Zarada* / *plata* = salary / wage
- *Bruto* = gross; *neto* = net
- *Porez na zarade* = tax on salaries (the 10%)
- *Doprinosi* = contributions
- *Neoporezivi iznos* = non-taxable amount
- *Najniža osnovica* = minimum (lowest) base; *najviša osnovica* = maximum (highest) base
- *Minimalna zarada* = minimum wage

**Key identification tips:**
1. Payroll-tax/contribution remittances are outgoing (DEBIT) to "PORESKA UPRAVA" or a named fund.
2. The 10% salary tax is on gross minus the non-taxable amount; contributions are on the clamped base — the two bases differ for low and high earners.
3. Do not confuse "PDV" (VAT), "POREZ NA DOBIT" (corporate tax), or "POREZ PO ODBITKU" (non-resident WHT) with payroll social contributions — all may show "PORESKA UPRAVA" as payee.
4. Net salary lines ("ISPLATA ZARADE" to the employee) are payroll, not contributions.
5. Match the consolidated remittance to the PPP-PD: it should equal salary tax + 19.90% + 15.15% for the period.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for remittances** -- identify outgoing payments matching Section 3 patterns ("PORESKA UPRAVA", "PPP-PD", "PIO", "RFZO", "NSZ", "DOPRINOSI").
2. **Identify the consolidated PPP-PD line** -- this funds salary tax + all contributions for the period.
3. **Reverse-engineer approximate gross** (employment income, within floor/ceiling): if total remittance R = salary tax + 19.90%G + 15.15%G and salary tax = 10%(G − non_taxable), then for a salary between the floor and ceiling base, R = 0.10(G − N) + 0.3505G = 0.4505G − 0.10N, so G ≈ (R + 0.10N) / 0.4505 (N = non-taxable amount for the year). Treat as an estimate only.
4. **Confirm the tax year** from the period reference (e.g. "01/2026" -> 2026 parameters).
5. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Tax year, residency, contribution-base position (floor/ceiling), and any new-hire relief have not been independently verified. Reviewer must confirm before relying on these figures."

### Parameter table by tax year

**Parameter table by tax year**  _(Eurofast / KPMG Dec 2025; Eurofast / Orbitax; Orbitax (2026); Zunic Law / RS Partners; PwC / KPMG; PwC)_

| Parameter | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Non-taxable monthly salary amount | RSD 28,423 | RSD 34,221 | Eurofast / KPMG Dec 2025 |
| Minimum monthly contribution base | RSD 45,950 | RSD 51,297 | Eurofast / Orbitax |
| Maximum monthly contribution base | RSD 656,425 | RSD 732,820 | Eurofast / Orbitax |
| Maximum annual contribution base | [RESEARCH GAP — 2025 not captured] | RSD 8,793,840 | Orbitax (2026) |
| Net minimum wage per hour | RSD 308 (Jan–Sep) / RSD 337 (Oct–Dec, OG 67/2025) | RSD 371 (OG 78/2025) | Zunic Law / RS Partners |
| Salary tax rate | 10% flat | 10% flat | PwC / KPMG |
| Employee contribution rate | 19.90% | 19.90% | PwC |
| Employer contribution rate | 15.15% | 15.15% | PwC |

### Contribution split (per fund)

**Contribution split (per fund)**  _(PwC / Eurofast)_

| Fund | Employee | Employer | Combined | Source |
| --- | --- | --- | --- | --- |
| Pension & disability (PIO) | 14% | 10% | 24% | PwC |
| Health (RFZO) | 5.15% | 5.15% | 10.30% | PwC |
| Unemployment (NSZ) | 0.75% | 0% | 0.75% | PwC |
| **TOTAL** | **19.90%** | **15.15%** | **35.05%** | PwC / Eurofast |

### Annual supplementary PIT thresholds (2025 income, filed 2026)

**Annual supplementary PIT thresholds (2025 income, filed 2026)**  _(KPMG Feb 2026 alert; KPMG / PwC)_

| Item | Value | Source |
| --- | --- | --- |
| Filing threshold (3x avg annual salary) | RSD 5,439,096 | KPMG Feb 2026 alert |
| 10%/15% bracket break (6x avg annual salary) | RSD 10,878,192 | KPMG / PwC |
| Standard personal deduction (40%) | RSD 725,213 | KPMG Feb 2026 alert |
| Dependent deduction (15% each) | RSD 271,955 per dependent | KPMG Feb 2026 alert |
| Combined deductions cap | 50% of net income | KPMG Feb 2026 alert |
| Under-40 additional deduction | RSD 5,439,096 | KPMG Feb 2026 alert |
| PP GPDG deadline (2025 income) | 15 May 2026 | KPMG Feb 2026 alert |

### Context rates (NOT social contributions)

**Context rates (NOT social contributions)**  _(PwC; PwC Corporate WHT)_

| Item | Rate | Source |
| --- | --- | --- |
| Corporate income tax | 15% flat | PwC |
| VAT standard | 20% | PwC |
| VAT reduced | 10% (some secondary sources state 8% — see caveats) | PwC |
| Non-resident WHT (dividends, interest, royalties, lease, services) | 20% (25% to tax-haven jurisdictions; reducible under treaties) | PwC Corporate WHT |

### Forms

**Forms**  _(Tax Administration / KPMG; KPMG)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| PPP-PD | Consolidated monthly salary tax + all contributions return | Filed/paid at each salary payment; electronic via Tax Administration portal | Tax Administration / KPMG |
| PP GPDG | Annual (supplementary) PIT for residents above threshold | 15 May of the following year (15 May 2026 for 2025 income); online only | KPMG |

### Penalties

**Penalties**  _(Law on Tax Procedure (ZPPPA); [RESEARCH GAP — reviewer to confirm against ZPPPA / Contributions Law])_

| Item | Detail | Source |
| --- | --- | --- |
| Late filing/payment | Default interest at the statutory rate (NBS reference rate + 10 p.p., daily) plus fines | Law on Tax Procedure (ZPPPA) |
| Misdemeanour fines (legal entities) | Fines for failure to calculate/pay contributions or file returns; exact RSD ranges not pinned | [RESEARCH GAP — reviewer to confirm against ZPPPA / Contributions Law] |

### Test suite

All figures recomputed end-to-end. Unless stated, **2026 parameters** (non-taxable RSD 34,221; floor RSD 51,297; ceiling RSD 732,820).

**Test 1 (mid-range, 2026):** Gross RSD 150,000. Salary tax = 10% x (150,000 − 34,221) = 11,577.90. Employee contr = 19.90% x 150,000 = 29,850.00. Net pay = 108,572.10. Employer contr = 15.15% x 150,000 = 22,725.00. Employer cost = 172,725.00.

**Test 2 (below floor, 2026):** Gross RSD 40,000. Salary tax = 10% x (40,000 − 34,221) = 577.90. Contribution base = 51,297 (floor). Employee contr = 19.90% x 51,297 = 10,208.10. Net pay = 29,214.00. Employer contr = 15.15% x 51,297 = 7,771.50.

**Test 3 (above ceiling, 2026):** Gross RSD 900,000. Salary tax = 10% x (900,000 − 34,221) = 86,577.90. Contribution base = 732,820 (ceiling). Employee contr = 19.90% x 732,820 = 145,831.18. Net pay = 667,590.92. Employer contr = 15.15% x 732,820 = 111,022.23.

**Test 4 (consolidated PPP-PD, Test 1):** Remittance = 11,577.90 + 29,850.00 + 22,725.00 = 64,152.90.

**Test 5 (2025 parameters, mid-range):** Gross RSD 150,000. Salary tax = 10% x (150,000 − 28,423) = 12,157.70. Employee contr = 19.90% x 150,000 = 29,850.00. Net pay = 150,000 − 12,157.70 − 29,850.00 = 107,992.30. Employer contr = 15.15% x 150,000 = 22,725.00.

**Test 6 (gross below non-taxable amount, 2026):** Gross RSD 30,000. Salary tax base = 30,000 − 34,221 = negative -> salary tax = 0 (never negative). Contribution base = 51,297 (floor). Employee contr = 19.90% x 51,297 = 10,208.10. Net pay = 30,000 − 0 − 10,208.10 = 19,791.90. (Reviewer must also check this against the applicable minimum wage.)

**Test 7 (annual PIT, 2025 income, RSD 20,000,000, no dependents, over 40):** Above threshold = 14,560,904. Less standard deduction 725,213 (below the 50% cap of 7,280,452) -> base 13,835,691. 10% x 10,878,192 = 1,087,819.20; 15% x 2,957,499 = 443,624.85; total = 1,531,444.05.

**Test 8 (annual PIT below threshold):** Resident net 2025 income RSD 5,000,000 < RSD 5,439,096 threshold -> no PP GPDG filing obligation; annual supplementary PIT = 0.

### Prohibitions

- NEVER compute Serbian payroll without confirming the tax year (2025 vs 2026) — the non-taxable amount and bases differ.
- NEVER apply the contribution floor/ceiling to the 10% salary tax base — the salary tax has no base cap.
- NEVER compute contributions below the minimum base for a salary under the floor — the floor still applies.
- NEVER accrue contributions on the portion of salary above the maximum base.
- NEVER conflate the monthly 10% salary tax with the annual supplementary PIT (PP GPDG) — they are separate.
- NEVER add an employer unemployment (NSZ) contribution — there is none (employer is PIO + RFZO only).
- NEVER roll forward a prior year's non-taxable amount or base without confirming the published value (indexed annually; next change 1 Jan 2027).
- NEVER apply new-hire / start-up employment relief without reviewer confirmation.
- NEVER estimate penalties or default interest — escalate to a licensed advisor.
- NEVER treat "PDV", "POREZ NA DOBIT", or "POREZ PO ODBITKU" remittances as payroll social contributions.
- NEVER present figures marked [RESEARCH GAP] as confirmed — these require a licensed Serbian advisor.
- NEVER present Serbian payroll figures as definitive — label as estimated pending professional review.

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
