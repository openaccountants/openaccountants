---
name: belarus-social-contributions
description: Use this skill whenever asked about Belarus social insurance contributions (FSZN / ФСЗН), Belgosstrakh occupational-accident insurance, or personal income tax (PIT / подоходный налог) withholding on Belarusian payroll. Trigger on phrases like "how much social contributions do I pay in Belarus", "FSZN rate", "ФСЗН", "Social Protection Fund", "Belarus payroll tax", "28% pension 6% social", "1% employee contribution", "Belgosstrakh accident insurance", "Belarus PIT 13%", "увеличенная ставка подоходного налога", "High Technology Park payroll", "HTP FSZN base", "self-employed FSZN Belarus", "individual entrepreneur contributions", or any question about Belarusian payroll on-costs, contribution ceilings, or PIT thresholds. Also trigger when classifying bank statement transactions that relate to FSZN debits, Belgosstrakh premiums, PIT (подоходный налог) remittances, or salary (зарплата) payments from Belarusbank, Belarusbank, Belinvestbank, Priorbank, BPS-Sberbank, Alfa-Bank or other Belarusian banks. This skill covers FSZN employer/employee rates, the Belgosstrakh accident-insurance premium, self-employed/IP contributions, contribution floors and ceilings, the HTP base benefit, the 13%/25%/30% PIT scale, payment and reporting deadlines (4-fund / ПУ forms), bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Belarus social-contribution or payroll-PIT work.
version: 0.1
jurisdiction: BY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus Social Insurance Contributions (FSZN) + Payroll PIT

## Belarus Social Insurance Contributions (FSZN) + Payroll PIT -- Skill v0.1

**Confidence: MEDIUM.** Belarus is NOT covered by the PwC / Deloitte / EY / KPMG Worldwide Tax Summaries (taxsummaries.pwc.com/belarus returns 404). Figures below rely on the official President of Belarus portal (president.gov.by), the official Social Protection Fund portal (ssf.gov.by), the Lloyds/Standard Bank International Trade Portal, Bloomberg Tax, and specialist Belarusian payroll/EOR providers (eor.by, spex.by, globalization-partners). Several figures carry an explicit **[RESEARCH GAP -- reviewer to confirm]** marker and MUST be verified against the Russian-language Tax Code (Налоговый кодекс) and current FSZN regulations before any filing. Belarus is also under extensive international sanctions affecting banking/payment practicalities (not the statutory rates).

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Republic of Belarus
- **Primary Legislation** — Tax Code of the Republic of Belarus (Налоговый кодекс); Law No. 138-Z on social insurance + Decree/Law on mandatory FSZN contributions; Law on mandatory state social insurance against industrial accidents and occupational diseases (Belgosstrakh)
- **Social Insurance Authority** — Social Protection Fund of the Population (FSZN / ФСЗН), Ministry of Labour and Social Protection — ssf.gov.by
- **Accident-Insurance Insurer** — Belgosstrakh (Belarusian Unitary Insurance Enterprise)
- **Tax Authority (PIT)** — Ministry of Taxes and Duties (MNS / nalog.gov.by)
- **Currency** — BYN (Belarusian ruble) only
- **Employer FSZN** — 34% of gross (28% pension + 6% social)  _(lloydsbanktrade / eor.by)_
- **Employee FSZN** — 1% of gross wages (withheld by employer)  _(lloydsbanktrade / globalization-partners)_
- **Combined FSZN** — 35% of gross wages
- **Belgosstrakh (accident)** — 0.6% base, employer-paid; adjusted by industry risk class  _(lloydsbanktrade / eor.by)_
- **Employer total on-cost** — ~34.6% of gross (34% FSZN + 0.6% Belgosstrakh) before any HTP base reduction
- **Self-employed / IP FSZN** — 35% total (29% pension + 6% social)  _(search corroboration of FSZN rules)_
- **PIT standard rate (2025)** — 13% flat on most employment income, withheld at source  _(lloydsbanktrade / president.gov.by)_
- **PIT increased rate (2025)** — 25% on annual income above BYN 220,000  _(eor.by / president.gov.by)_
- **PIT scale (2026)** — 13% up to BYN 350,000; 25% BYN 350,001–600,000; 30% above BYN 600,000  _(president.gov.by / Bloomberg Tax)_
- **Minimum wage (2025)** — BYN 726 / month  _(WageIndicator / globalization-partners)_
- **Minimum wage (2026)** — BYN 858 / month  _(WageIndicator)_
- **FSZN payment** — Day wages are paid; in practice no later than the 20th of the following month  _(search corroboration)_
- **FSZN reporting** — Quarterly — Form 4-fund (4-фонд), personalised ПУ-3 / ПУ-6  _(search corroboration)_
- **Validated by** — Pending — requires sign-off by a Belarusian tax/payroll professional
- **Validation date** — Pending

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Belarus |
| Primary Legislation | Tax Code of the Republic of Belarus (Налоговый кодекс); Law No. 138-Z on social insurance + Decree/Law on mandatory FSZN contributions; Law on mandatory state social insurance against industrial accidents and occupational diseases (Belgosstrakh) |
| Social Insurance Authority | Social Protection Fund of the Population (FSZN / ФСЗН), Ministry of Labour and Social Protection — ssf.gov.by |
| Accident-Insurance Insurer | Belgosstrakh (Belarusian Unitary Insurance Enterprise) |
| Tax Authority (PIT) | Ministry of Taxes and Duties (MNS / nalog.gov.by) |
| Currency | BYN (Belarusian ruble) only |
| Employer FSZN | 34% of gross (28% pension + 6% social) (lloydsbanktrade / eor.by) |
| Employee FSZN | 1% of gross wages (withheld by employer) (lloydsbanktrade / globalization-partners) |
| Combined FSZN | 35% of gross wages |
| Belgosstrakh (accident) | 0.6% base, employer-paid; adjusted by industry risk class (lloydsbanktrade / eor.by) |
| Employer total on-cost | ~34.6% of gross (34% FSZN + 0.6% Belgosstrakh) before any HTP base reduction |
| Self-employed / IP FSZN | 35% total (29% pension + 6% social) (search corroboration of FSZN rules) |
| PIT standard rate (2025) | 13% flat on most employment income, withheld at source (lloydsbanktrade / president.gov.by) |
| PIT increased rate (2025) | 25% on annual income above BYN 220,000 (eor.by / president.gov.by) |
| PIT scale (2026) | 13% up to BYN 350,000; 25% BYN 350,001–600,000; 30% above BYN 600,000 (president.gov.by / Bloomberg Tax) |
| Minimum wage (2025) | BYN 726 / month (WageIndicator / globalization-partners) |
| Minimum wage (2026) | BYN 858 / month (WageIndicator) |
| FSZN payment | Day wages are paid; in practice no later than the 20th of the following month (search corroboration) |
| FSZN reporting | Quarterly — Form 4-fund (4-фонд), personalised ПУ-3 / ПУ-6 (search corroboration) |
| Validated by | Pending — requires sign-off by a Belarusian tax/payroll professional |
| Validation date | Pending |

**Contribution overview (per gross wage)**

| Contribution | Payer | Rate | Component |
| --- | --- | --- | --- |
| FSZN pension insurance | Employer | 28% | Part of 34% employer total |
| FSZN social insurance | Employer | 6% | Part of 34% employer total |
| FSZN pension insurance | Employee (withheld) | 1% | Employee share |
| **Total FSZN (employer + employee)** | **Combined** | **35%** | **34% + 1% = 35%** |
| Belgosstrakh accident insurance | Employer | 0.6% base | On top of FSZN; risk-class adjusted |

- **Arithmetic check** — 28% + 6% = 34% employer; 34% + 1% employee = 35% combined. Belgosstrakh (0.6%) sits OUTSIDE the 35% FSZN total.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether HTP resident | Apply full-gross FSZN (34% employer + 1% employee) + 0.6% Belgosstrakh — do NOT assume the HTP base reduction |
| Unknown annual income vs PIT threshold | Use 13% PIT for all employment income unless annual income demonstrably exceeds the 25% threshold (BYN 220,000 for 2025 / BYN 350,000 for 2026) |
| Unknown Belgosstrakh risk class | Use 0.6% base premium |
| Unknown self-employed status | Use 35% (29% pension + 6% social) on at least the 12-minimum-wage annual floor |
| Unknown whether a debit is FSZN or PIT | Classify by reference text; if still ambiguous, flag for reviewer |
| Unknown payment date | Use the 20th-of-following-month outer limit (do not assume earlier compliance) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- employment status (employee vs self-employed/IP), gross monthly remuneration in BYN, and the tax year (2025 vs 2026 changes the PIT scale and minimum wage).

**Recommended** -- whether the employer is a High Technology Park (HTP) resident, the annual cumulative income (to test the 25%/30% PIT thresholds), and the Belgosstrakh occupational risk class.

**Ideal** -- FSZN personalised account statements (ПУ forms), payroll register, prior-year annual tax return, and bank statements showing FSZN/Belgosstrakh/PIT remittances.

### Refusal catalogue

- **R-BY-SSC-1** — Trigger: annual income approaches or exceeds the high-income threshold (BYN 220,000 in 2025; BYN 350,000 in 2026). Message: "The increased PIT rate (25%, and 30% from 2026) is reconciled by the individual via an annual tax return, not by simple payroll withholding. The exact year of application of the BYN 350,000 / 600,000 thresholds is a [RESEARCH GAP -- reviewer to confirm]. Escalate to a Belarusian tax professional."  _(R-BY-SSC-1 -- Annual increased-rate (25%/30%) PIT reconciliation)_
- **R-BY-SSC-2** — Trigger: a precise accident-insurance figure is requested for a specific industry. Message: "The Belgosstrakh premium is 0.6% as a base, but the actual rate depends on the assigned occupational risk class and coefficients (commonly cited ~0.2%–0.9%, up to ~1.5 for high-risk trades). Confirm against the specific tariff certificate. Do not quote a precise rate without it."  _(R-BY-SSC-2 -- Belgosstrakh risk-class tariff)_
- **R-BY-SSC-3** — Trigger: an individual entrepreneur asks whether the 6% social-insurance portion is mandatory. Message: "Whether the social-insurance portion is mandatory or voluntary for IPs, and the 29%+6% split, must be confirmed against current FSZN rules [RESEARCH GAP -- reviewer to confirm]. Escalate to a Belarusian payroll professional."  _(R-BY-SSC-3 -- Self-employed / IP voluntary vs mandatory social portion)_
- **R-BY-SSC-4** — Trigger: a computation depends on the 5×-average-wage ceiling or the HTP average-wage base. Message: "The FSZN ceiling (five times the national average monthly wage) and the HTP base (~BYN 2,000 in 2025) move with Belstat statistics. Verify the current Belstat average-wage figure before relying on the cap [RESEARCH GAP -- reviewer to confirm]."  _(R-BY-SSC-4 -- FSZN ceiling and HTP base figures)_
- **R-BY-SSC-5** — Trigger: questions about how to actually remit funds cross-border. Message: "Belarus is under extensive international sanctions affecting banking and payment routing. This skill covers statutory rates only, not payment mechanics. Escalate banking questions to a sanctions-aware adviser."  _(R-BY-SSC-5 -- Sanctions / payment practicalities)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for Belarusian bank statement transactions related to payroll, social contributions, and PIT. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference as it appears in the statement (Cyrillic or transliterated). FSZN, Belgosstrakh and PIT remittances are statutory obligations — EXCLUDE from any VAT return; treat per the notes for payroll-cost classification.

### 3.1 FSZN (Social Protection Fund) contributions

**3.1 FSZN (Social Protection Fund) contributions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ФСЗН, FSZN | EXCLUDE -- FSZN contribution | Pension (28%/29%) + social (6%) + employee (1%) |
| ФОНД СОЦИАЛЬНОЙ ЗАЩИТЫ, SOCIAL PROTECTION FUND | EXCLUDE -- FSZN contribution | Full authority name |
| ОТЧИСЛЕНИЯ В ФСЗН, STRAHOVYE VZNOSY | EXCLUDE -- FSZN contribution | "Insurance contributions" |
| ПЕНСИОННОЕ СТРАХОВАНИЕ, PENSION INSURANCE | EXCLUDE -- FSZN pension portion | 28% employer / 1% employee |
| СОЦИАЛЬНОЕ СТРАХОВАНИЕ | EXCLUDE -- FSZN social portion | 6% employer |

### 3.2 Belgosstrakh occupational-accident insurance

**3.2 Belgosstrakh occupational-accident insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| БЕЛГОССТРАХ, BELGOSSTRAKH | EXCLUDE -- accident insurance | Employer premium, ~0.6% base |
| СТРАХОВАНИЕ ОТ НЕСЧАСТНЫХ СЛУЧАЕВ | EXCLUDE -- accident insurance | "Insurance against accidents" |
| ОБЯЗАТ. СТРАХ. ОТ НС И ПЗ | EXCLUDE -- accident insurance | Industrial accidents / occupational diseases |

### 3.3 Personal income tax (PIT) — NOT FSZN; do not confuse

**3.3 Personal income tax (PIT) pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ПОДОХОДНЫЙ НАЛОГ, PODOHODNYY NALOG | EXCLUDE -- PIT, not FSZN | 13% (25%/30% on high income) |
| МНС, MNS, INSPEKTSIYA PO NALOGAM | EXCLUDE -- tax authority remittance | Ministry of Taxes and Duties |
| НАЛОГ НА ДОХОДЫ ФИЗ. ЛИЦ | EXCLUDE -- PIT | Tax on income of individuals |

### 3.4 Salary and payroll (exclude from contribution classification)

**3.4 Salary and payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ЗАРПЛАТА, ЗАРАБОТНАЯ ПЛАТА, ZARPLATA (outgoing) | EXCLUDE -- payroll expense | Net wage payment; not a contribution |
| АВАНС (outgoing) | EXCLUDE -- salary advance | Not a contribution |
| ЗАРПЛАТА, SALARY (incoming) | EXCLUDE -- employment income received | Not a contribution |

### 3.5 FSZN benefits received (not contributions paid)

**3.5 FSZN benefits received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ПЕНСИЯ, PENSIYA (incoming) | EXCLUDE -- pension income received | Not a contribution |
| ПОСОБИЕ, BENEFIT (incoming) | EXCLUDE -- temporary disability / maternity benefit | Reimbursed via FSZN; not a contribution paid |

## Section 4 -- Worked examples

Six bank statement classifications and computations for a hypothetical Belarusian employer and self-employed individual. All amounts in BYN. Statement lines use a typical Belarusbank/Priorbank export format.

### Example 1 -- Employer FSZN remittance on standard payroll

**Scenario:** Employer pays an employee gross BYN 3,000/month (2025), not HTP resident.

**Input line:**
`20.02.2025 ; ФСЗН ОТЧИСЛЕНИЯ ЯНВАРЬ ; ДЕБЕТ ; -1,020.00 ; BYN`

**Reasoning:**
Matches "ФСЗН" (pattern 3.1). Employer FSZN = 34% × BYN 3,000 = BYN 1,020.00 (28% pension = BYN 840 + 6% social = BYN 180). This is the employer's January contribution, remitted by the 20th of February. Employee's 1% (BYN 30) is withheld separately from wages. EXCLUDE from VAT; record as a payroll on-cost.

**Classification:** EXCLUDE -- FSZN employer contribution (BYN 1,020.00 = 34% of BYN 3,000).

### Example 2 -- Employee 1% FSZN + 13% PIT withheld from wages

**Scenario:** Same BYN 3,000 gross. Employee deductions (2025).

**Reasoning:**
- Employee FSZN (1%) = BYN 3,000 × 1% = **BYN 30.00** (withheld).
- PIT base = gross less employee FSZN? In Belarus PIT is generally computed on gross income; for a conservative estimate ignoring personal deductions, PIT = BYN 3,000 × 13% = **BYN 390.00**.
- Net to employee = 3,000 − 30 − 390 = **BYN 2,580.00** (before any personal/child deductions, which reduce PIT).

**Classification:** Employee FSZN BYN 30.00 (EXCLUDE -- FSZN); PIT BYN 390.00 (EXCLUDE -- PIT). Net pay BYN 2,580.00. [Note: personal monthly deduction ~BYN 192 only applies where monthly income ≤ ~BYN 1,164, so it does NOT apply at BYN 3,000 — see Section 10.]

### Example 3 -- Belgosstrakh accident-insurance premium

**Scenario:** Same BYN 3,000 gross, base risk class.

**Input line:**
`20.02.2025 ; БЕЛГОССТРАХ СТРАХ ВЗНОС ; ДЕБЕТ ; -18.00 ; BYN`

**Reasoning:**
Matches "БЕЛГОССТРАХ" (pattern 3.2). Premium = 0.6% × BYN 3,000 = BYN 18.00. This is employer-only, on top of the 34% FSZN. Total employer on-cost = BYN 1,020.00 + BYN 18.00 = BYN 1,038.00 (= 34.6% × 3,000). EXCLUDE from VAT.

**Classification:** EXCLUDE -- Belgosstrakh accident insurance (BYN 18.00 = 0.6% of BYN 3,000). [Risk class assumed base — RESEARCH GAP if a higher coefficient applies.]

### Example 4 -- HTP resident: reduced FSZN base

**Scenario:** HTP resident employer, employee gross BYN 6,000/month (2025). HTP allows FSZN to be calculated on a base capped at the national average monthly wage (~BYN 2,000 in 2025) instead of full salary (eor.by / spex.by).

**Reasoning:**
- WITHOUT HTP: employer FSZN = 34% × 6,000 = BYN 2,040.00.
- WITH HTP base (~BYN 2,000): employer FSZN = 34% × 2,000 = **BYN 680.00**. Employee 1% = 2,000 × 1% = **BYN 20.00**.
- Saving on employer FSZN ≈ BYN 1,360/month. PIT is still computed on full gross: 13% × 6,000 = BYN 780.00 (assuming below the 25% annual threshold).

**Classification:** EXCLUDE -- FSZN at HTP base (employer BYN 680.00). [HTP base ~BYN 2,000 is a Belstat-linked figure — RESEARCH GAP; verify current average wage.]

### Example 5 -- High earner crossing the 25% PIT threshold (2025)

**Scenario:** Executive with cumulative 2025 annual income of BYN 260,000.

**Reasoning:**
- 13% applies to the first BYN 220,000: 220,000 × 13% = **BYN 28,600.00**.
- 25% applies to income above BYN 220,000: (260,000 − 220,000) × 25% = 40,000 × 25% = **BYN 10,000.00**.
- Total PIT = 28,600 + 10,000 = **BYN 38,600.00**.
- The 25% portion is reconciled via the annual tax return (due 31 March); payroll only withholds 13% at source (eor.by / president.gov.by).

**Classification:** Payroll withholds 13% at source; the additional BYN 10,000 (25% band) is reconciled on the annual return. Flag for reviewer — annual reconciliation required (R-BY-SSC-1).

### Example 6 -- Self-employed / individual entrepreneur (IP) FSZN floor (2025)

**Scenario:** IP with low/irregular income; minimum-wage floor applies.

**Reasoning:**
- Annual FSZN floor = 12 × monthly minimum wage = 12 × BYN 726 = **BYN 8,712** base (search corroboration).
- FSZN = 35% × BYN 8,712 = **BYN 3,049.20/year** (29% pension = BYN 2,526.48 + 6% social = BYN 522.72).
- Contributions are due on actual income or this floor, whichever applies. The mandatory vs voluntary status of the 6% social portion is a [RESEARCH GAP -- reviewer to confirm].

**Classification:** EXCLUDE -- IP FSZN (BYN 3,049.20/year minimum on the 12-minimum-wage floor). Flag for reviewer (R-BY-SSC-3).

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Employer FSZN formula

- **Employer FSZN formula** — Employer FSZN = gross_wages × 34%   (28% pension + 6% social)  _(lloydsbanktrade / eor.by. Subject to the FSZN ceiling (Rule 7) and the HTP base option (Rule 8).)_

### Rule 2 -- Employee FSZN formula

- **Employee FSZN formula** — Employee FSZN = gross_wages × 1%   (withheld and remitted by employer)  _(lloydsbanktrade / globalization-partners. Combined employer + employee FSZN = 35%.)_

### Rule 3 -- Belgosstrakh accident insurance

- **Belgosstrakh formula** — Belgosstrakh = gross_payroll × 0.6%   (base; employer-only; risk-class adjusted)  _(lloydsbanktrade / eor.by. Sits OUTSIDE the 35% FSZN total. Use 0.6% unless the specific industry risk class/coefficient is known (commonly ~0.2%–0.9%).)_

### Rule 4 -- PIT standard rate and withholding

- **PIT standard rate and withholding** — PIT is a flat 13% on most employment income, withheld at source by the employer at the time of salary payment. Remitted on the day funds are received from the bank for wages.  _(lloydsbanktrade / president.gov.by)_

### Rule 5 -- PIT increased rates (2025)

- **PIT increased rates (2025)** — For tax year 2025, an increased rate of 25% applies to annual income above BYN 220,000. The increased-rate portion is reconciled by the individual via the annual tax return — payroll withholds only 13% at source.  _(eor.by / president.gov.by)_

### Rule 6 -- PIT scale (2026)

- **PIT scale (2026)** — For 2026, the Tax Code amendment signed December 2025 sets: 13% up to BYN 350,000; 25% on BYN 350,001–600,000; 30% above BYN 600,000. Dividends remain on a separate 13%/25% scale. The exact year of application of the BYN 350,000 / 600,000 thresholds is a [RESEARCH GAP -- reviewer to confirm] — sources most consistently describe these as 2026 figures, with the 2025 25% threshold being BYN 220,000.  _(president.gov.by / Bloomberg Tax)_

### Rule 7 -- FSZN ceiling (maximum base)

- **FSZN ceiling (maximum base)** — FSZN contributions are capped at a base of five times the national average monthly wage of the month preceding payment. The exact BYN ceiling moves with Belstat statistics — [RESEARCH GAP -- reviewer to confirm] the current average wage before applying the cap.  _(search corroboration)_

### Rule 8 -- HTP resident base option

- **HTP resident base option** — High Technology Park (HTP) resident companies may calculate FSZN on a base capped at the national average monthly wage (~BYN 2,000 in 2025) rather than full salary, sharply reducing payroll on-costs. The ~BYN 2,000 figure is Belstat-linked — [RESEARCH GAP -- reviewer to confirm]. PIT is still computed on full gross.  _(eor.by / spex.by)_

### Rule 9 -- Self-employed / IP FSZN

- **IP FSZN formula** — IP FSZN = max(actual_income, 12 × monthly_minimum_wage) × 35%   (29% pension + 6% social)  _(2025 floor = 12 × BYN 726 = BYN 8,712 (search corroboration). The 29%/6% split and whether the social portion is mandatory or voluntary are a [RESEARCH GAP -- reviewer to confirm].)_

### Rule 10 -- Payment timing

- **Payment timing** — FSZN contributions are paid on the day wages are actually paid for the month, no later than the established wage-payment day — in practice no later than the 20th of the month following the reporting month where wages are paid later. PIT is remitted at the time of salary payment.  _(search corroboration)_

### Rule 11 -- Reporting cadence

- **Reporting cadence** — FSZN personalised reporting (Form 4-fund / 4-фонд, plus ПУ-3 / ПУ-6 personalised account data) is submitted quarterly. The annual individual tax return (for increased-rate reconciliation) is due by 31 March of the following year, with tax payable by ~1 June.  _(search corroboration (eor.by))_

### Rule 12 -- These are personal/statutory obligations, not VAT supplies

- **Not VAT supplies** — FSZN, Belgosstrakh and PIT remittances are EXCLUDED from any VAT return. Employer FSZN and Belgosstrakh are deductible payroll on-costs for corporate income tax; employee FSZN (1%) and PIT are withheld from gross wages.

## Section 6 -- Tier 2 catalogue

When data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- HTP residency status unconfirmed

- **T2-1** — Trigger: Employer may be an HTP resident but residency is not documented. Issue: HTP residency caps the FSZN base at the average monthly wage (~BYN 2,000), changing employer FSZN from 34% of full gross to a much smaller figure. Applying it wrongly under- or over-states contributions materially. Action: Flag for reviewer. Do NOT apply the HTP base reduction without documented residency.

### T2-2 -- Annual income near the 25%/30% PIT thresholds

- **T2-2** — Trigger: Cumulative annual income approaches BYN 220,000 (2025) / BYN 350,000 or 600,000 (2026). Issue: The increased-rate portion is reconciled via the annual return, not payroll withholding. The exact application year of the BYN 350,000 / 600,000 thresholds is unsettled in the sources. Action: Flag for reviewer (R-BY-SSC-1). Confirm the threshold year against the Tax Code.  _(R-BY-SSC-1)_

### T2-3 -- Belgosstrakh risk class unknown

- **T2-3** — Trigger: Industry/occupation has elevated accident risk but no tariff certificate is provided. Issue: The 0.6% base can rise with risk-class coefficients (commonly to ~0.9%, up to ~1.5 for high-risk trades). Action: Flag for reviewer (R-BY-SSC-2). Use 0.6% base as a placeholder and label it as such.  _(R-BY-SSC-2)_

### T2-4 -- Self-employed / IP social-portion treatment

- **T2-4** — Trigger: An IP queries the 6% social-insurance portion. Issue: Whether the 6% social portion is mandatory or voluntary for IPs, and the 29%+6% split, are not firmly sourced. Action: Flag for reviewer (R-BY-SSC-3). Confirm against current FSZN rules.  _(R-BY-SSC-3)_

### T2-5 -- FSZN ceiling application

- **T2-5** — Trigger: A high earner's gross exceeds five times the average monthly wage. Issue: The ceiling caps the contributable base; the exact BYN figure moves with Belstat statistics. Action: Flag for reviewer (R-BY-SSC-4). Verify the current average wage before capping.  _(R-BY-SSC-4)_

### T2-6 -- Personal/child/disability PIT deductions

- **T2-6** — Trigger: Low-income employee or employee with children/dependants or privileged status. Issue: The basic (~BYN 192), child (~BYN 56/107) and vulnerable-category (~BYN 272) monthly deductions are 2025 figures, indexed annually, and the basic deduction only applies where monthly income ≤ ~BYN 1,164. Action: Flag for reviewer. Confirm 2025/2026 deduction amounts and eligibility against the Tax Code.

## Section 7 -- Excel working paper template

When producing a Belarus payroll/contribution computation, structure the working paper as follows:

```
BELARUS PAYROLL / FSZN COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [2025 / 2026]
Prepared: [date]

INPUT DATA
  Employment status:             [Employee / Self-employed-IP]
  Gross monthly remuneration:    BYN [____]
  HTP resident employer:         [YES / NO]
  Cumulative annual income:      BYN [____]   (tests 25%/30% PIT)
  Belgosstrakh risk class:       [____]   (default base 0.6%)

EMPLOYER CONTRIBUTIONS
  FSZN base (full gross or HTP): BYN [____]
  Pension (28%):                 BYN [____]
  Social (6%):                   BYN [____]
  FSZN employer total (34%):     BYN [____]
  Belgosstrakh (0.6% base):      BYN [____]
  Employer total on-cost:        BYN [____]   (~34.6% of base before HTP)

EMPLOYEE DEDUCTIONS
  FSZN employee (1%):            BYN [____]
  PIT basic deduction (if elig): BYN [____]   (only if monthly income ≤ ~1,164)
  PIT child/dependant deduction: BYN [____]
  PIT base:                      BYN [____]
  PIT at 13%:                    BYN [____]
  PIT 25%/30% (annual return):   BYN [____]   (reconciled, NOT payroll)
  Net pay:                       BYN [____]

SELF-EMPLOYED / IP (if applicable)
  Actual income:                 BYN [____]
  12 × minimum wage floor:       BYN [____]   (2025: 12 × 726 = 8,712)
  FSZN base (greater of):        BYN [____]
  FSZN at 35% (29% + 6%):        BYN [____]

DEADLINES
  FSZN payment:                  by ~20th of following month
  FSZN 4-fund / ПУ report:       quarterly
  Annual PIT return:             31 March (following year)

REVIEWER FLAGS / RESEARCH GAPS
  [List any Tier 2 flags and [RESEARCH GAP] items here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contribution/PIT debits appear on Belarusian bank statements

Belarusian statements are usually in Russian (Cyrillic); transliterated Latin variants appear in some exports. Common originating banks: Belarusbank (Беларусбанк), Belinvestbank, Priorbank, BPS-Sberbank, Alfa-Bank Belarus.

**FSZN contributions:**
- Description: "ФСЗН", "ФОНД СОЦИАЛЬНОЙ ЗАЩИТЫ", "ОТЧИСЛЕНИЯ В ФСЗН", "СТРАХОВЫЕ ВЗНОСЫ"
- Timing: by the 20th of the month following the reporting month (where wages paid later)
- Amount: 34% of the FSZN base for the employer portion; 1% withheld separately

**Belgosstrakh:**
- Description: "БЕЛГОССТРАХ", "СТРАХОВАНИЕ ОТ НЕСЧАСТНЫХ СЛУЧАЕВ"
- Amount: ~0.6% of payroll (risk-class adjusted)

**PIT:**
- Description: "ПОДОХОДНЫЙ НАЛОГ", "НАЛОГ НА ДОХОДЫ ФИЗ. ЛИЦ", "МНС"
- Timing: at salary payment
- Amount: 13% of PIT base (increased-rate portion reconciled annually)

**Key identification tips:**
1. Contribution/tax debits are always outgoing (ДЕБЕТ), never credits.
2. FSZN employer debits should be ~34% of the gross payroll base; if materially smaller, suspect an HTP base reduction (flag T2-1).
3. Belgosstrakh debits are small (~0.6%) and separate from FSZN.
4. Do not confuse outgoing "ФСЗН" debits with incoming "ПЕНСИЯ" / "ПОСОБИЕ" credits (benefits received).
5. PIT ("ПОДОХОДНЫЙ НАЛОГ" / "МНС") is a tax remittance, NOT a social contribution — keep them separate.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for FSZN, Belgosstrakh and PIT debits** — identify all outgoing payments matching Section 3 patterns.
2. **Reverse-engineer the payroll base:**
   - Employer FSZN debit ÷ 0.34 ≈ gross payroll base (if NOT HTP).
   - If the implied base is suspiciously low relative to known salaries, suspect HTP base capping (~BYN 2,000) — flag T2-1.
   - Belgosstrakh debit ÷ 0.006 ≈ payroll base (cross-check).
   - PIT debit ÷ 0.13 ≈ PIT base (for income below the 25% threshold).
3. **Sum contributions by period** to confirm monthly/quarterly cadence.
4. **Flag for reviewer:** "Contribution and PIT figures derived from bank statement amounts only. HTP residency, Belgosstrakh risk class, annual income vs the 25%/30% PIT thresholds, and the 2026 threshold year have not been independently verified. Reviewer must confirm before filing."

### PIT scale

**PIT scale**  _(eor.by / president.gov.by; Bloomberg Tax)_

| Year | Rate | Band (annual income) | Source |
| --- | --- | --- | --- |
| 2025 | 13% | up to BYN 220,000 | eor.by / president.gov.by |
| 2025 | 25% | above BYN 220,000 | eor.by / president.gov.by |
| 2026 | 13% | up to BYN 350,000 | president.gov.by / Bloomberg Tax |
| 2026 | 25% | BYN 350,001 – 600,000 | president.gov.by / Bloomberg Tax |
| 2026 | 30% | above BYN 600,000 | president.gov.by / Bloomberg Tax |
| 2025–2026 | 13% / 25% | dividends (separate scale) | president.gov.by |

The 2026 threshold-year is a **[RESEARCH GAP -- reviewer to confirm]** (see Rule 6).

### Other headline rates

**Other headline rates**  _(lloydsbanktrade)_

| Tax | Rate | Source |
| --- | --- | --- |
| Corporate income tax (standard, 2025) | 20% (raised from 18% in 2023) | lloydsbanktrade |
| VAT standard (2025) | 20% | lloydsbanktrade |
| VAT reduced (foods/crops/medicines/medical devices) | 10% | lloydsbanktrade |
| VAT telecom services | 25% | lloydsbanktrade |

### Contribution rates (summary)

**Contribution rates (summary)**  _(lloydsbanktrade / eor.by / globalization-partners / search corroboration)_

| Contribution | Payer | Rate | Source |
| --- | --- | --- | --- |
| FSZN pension | Employer | 28% | lloydsbanktrade / eor.by |
| FSZN social | Employer | 6% | lloydsbanktrade / eor.by |
| FSZN employer total | Employer | 34% | (28% + 6%) |
| FSZN pension | Employee | 1% | lloydsbanktrade / globalization-partners |
| FSZN combined | Both | 35% | (34% + 1%) |
| Belgosstrakh accident | Employer | 0.6% base (~0.2%–0.9% risk-adjusted) | lloydsbanktrade / eor.by |
| FSZN self-employed/IP | Self/IP | 35% (29% pension + 6% social) | search corroboration |

### Thresholds and bases

**Thresholds and bases**  _(WageIndicator / globalization-partners / eor.by / spex.by / research data)_

| Item | Value | Source |
| --- | --- | --- |
| Minimum wage 2025 | BYN 726/month (from BYN 626) | WageIndicator / globalization-partners |
| Minimum wage 2026 | BYN 858/month | WageIndicator |
| IP FSZN floor | 12 × monthly min wage = BYN 8,712 (2025) | search corroboration |
| FSZN ceiling | 5 × national average monthly wage (preceding month) | search corroboration; Belstat figure [RESEARCH GAP] |
| HTP FSZN base cap | national average monthly wage (~BYN 2,000 in 2025) | eor.by / spex.by; Belstat figure [RESEARCH GAP] |
| PIT basic monthly deduction | ~BYN 192 where monthly income ≤ ~BYN 1,164 (2025) | research data; indexed [RESEARCH GAP] |
| PIT child deduction | ~BYN 56/month per child; ~BYN 107 for 2+ children / single parent (2025) | research data; indexed [RESEARCH GAP] |
| PIT vulnerable-category deduction | ~BYN 272/month (2025) | research data; indexed [RESEARCH GAP] |

### Forms and deadlines

**Forms and deadlines**  _(search corroboration / eor.by)_

| Form / action | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| 4-fund (4-фонд), ПУ-3, ПУ-6 | Quarterly FSZN contribution + personalised account reporting | Quarterly | search corroboration |
| FSZN contribution payment | Remit pension (28%/29%) + social (6%) + employee (1%) | Day wages paid; no later than ~20th of following month | search corroboration |
| PIT remittance (employer) | Withhold and remit 13% PIT | At salary payment | search corroboration |
| Annual individual tax return | Reconcile 25%/30% PIT and other declarable income | 31 March following year (tax payable ~1 June) | eor.by |

### Penalties

**Penalties**  _(research data / Code of Administrative Offences)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Late FSZN payment | Penalty interest (peni) on overdue contributions + administrative fines | research data / Code of Administrative Offences |
| Late PIT / underwithholding | Penalty interest + administrative fines on the tax agent (employer) | research data |
| Late/incorrect FSZN reporting | Administrative fines for failure to submit or inaccurate ПУ data | research data |

### Worked-figure cross-check (2025, BYN 3,000 gross, non-HTP)

**Worked-figure cross-check (2025, BYN 3,000 gross, non-HTP)**  _(internal computation)_

| Line | Computation | Amount |
| --- | --- | --- |
| Employer FSZN pension (28%) | 3,000 × 0.28 | 840.00 |
| Employer FSZN social (6%) | 3,000 × 0.06 | 180.00 |
| Employer FSZN total (34%) | 840 + 180 | 1,020.00 |
| Belgosstrakh (0.6%) | 3,000 × 0.006 | 18.00 |
| Employer total on-cost | 1,020 + 18 | 1,038.00 |
| Employee FSZN (1%) | 3,000 × 0.01 | 30.00 |
| PIT (13%, no deduction) | 3,000 × 0.13 | 390.00 |
| Net pay | 3,000 − 30 − 390 | 2,580.00 |

### Test suite

**Test 1:** Employee gross BYN 3,000, 2025, non-HTP. → Employer FSZN = 34% × 3,000 = **BYN 1,020.00** (840 + 180). Belgosstrakh = **BYN 18.00**. Employer total = **BYN 1,038.00**.

**Test 2:** Same employee, employee-side. → Employee FSZN = 1% × 3,000 = **BYN 30.00**; PIT = 13% × 3,000 = **BYN 390.00**; net pay = **BYN 2,580.00**.

**Test 3:** HTP employer, gross BYN 6,000, HTP base ~BYN 2,000. → Employer FSZN = 34% × 2,000 = **BYN 680.00**; employee FSZN = 1% × 2,000 = **BYN 20.00**; PIT still on full gross = 13% × 6,000 = **BYN 780.00**.

**Test 4:** Executive, 2025 annual income BYN 260,000. → PIT = (220,000 × 13%) + (40,000 × 25%) = 28,600 + 10,000 = **BYN 38,600.00**. 25% band reconciled on annual return.

**Test 5:** 2026 earner, annual income BYN 700,000. → PIT = (350,000 × 13%) + (250,000 × 25%) + (100,000 × 30%) = 45,500 + 62,500 + 30,000 = **BYN 138,000.00**. [2026 threshold year is a RESEARCH GAP — see Rule 6.]

**Test 6:** IP, low income, 2025 floor. → FSZN base = 12 × 726 = BYN 8,712; FSZN = 35% × 8,712 = **BYN 3,049.20** (pension 29% = 2,526.48 + social 6% = 522.72).

**Test 7:** Employer FSZN debit on statement = BYN 1,020.00, non-HTP. → Implied gross base = 1,020 ÷ 0.34 = **BYN 3,000** (reverse-engineering check, Section 9).

**Test 8:** Belgosstrakh debit = BYN 18.00. → Implied payroll base = 18 ÷ 0.006 = **BYN 3,000** (cross-check vs FSZN-derived base).

### Prohibitions

- **NEVER apply the HTP FSZN base reduction without documented HTP residency** — NEVER apply the HTP FSZN base reduction without documented HTP residency.  _(skill prose)_
- **NEVER quote a precise Belgosstrakh rate above the 0.6% base without the specific risk-class tariff certificate** — NEVER quote a precise Belgosstrakh rate above the 0.6% base without the specific risk-class tariff certificate.  _(skill prose)_
- **NEVER withhold the 25%/30% PIT through payroll** — NEVER withhold the 25%/30% PIT through payroll — the increased-rate portion is reconciled on the annual return.  _(skill prose)_
- **NEVER state the 2026 thresholds as settled without reviewer confirmation** — NEVER state the 2026 BYN 350,000 / 600,000 thresholds as settled without the reviewer confirming the application year (RESEARCH GAP).  _(skill prose)_
- **NEVER apply the FSZN ceiling or HTP base without verifying the current Belstat average wage** — NEVER apply the FSZN ceiling or HTP base without verifying the current Belstat average wage (RESEARCH GAP).  _(skill prose)_
- **NEVER tell a self-employed/IP they owe FSZN below the 12-minimum-wage floor** — NEVER tell a self-employed/IP they owe FSZN below the 12-minimum-wage floor — the floor applies.  _(skill prose)_
- **NEVER conflate FSZN with PIT with Belgosstrakh** — NEVER conflate FSZN (social) with PIT (tax) with Belgosstrakh (accident insurance) — they are three separate obligations.  _(skill prose)_
- **NEVER confuse outgoing contribution debits with incoming pension/benefit credits** — NEVER confuse outgoing contribution debits with incoming pension/benefit credits.  _(skill prose)_
- **NEVER present any Belarus figure as definitive** — NEVER present any Belarus figure as definitive — confidence is MEDIUM and Big-4 coverage is absent; label estimates and direct to ssf.gov.by / nalog.gov.by.  _(skill prose)_
- **NEVER advise on sanctions-affected payment mechanics** — NEVER advise on sanctions-affected payment mechanics — statutory rates only.  _(skill prose)_

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
