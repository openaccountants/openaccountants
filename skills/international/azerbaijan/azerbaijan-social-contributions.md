---
name: azerbaijan-social-contributions
description: Use this skill whenever asked about Azerbaijan employer/employee social contributions, payroll taxes, or salary withholding. Trigger on phrases like "Azerbaijan social insurance", "SSPF contributions", "DSMF", "how much social security do I pay in Azerbaijan", "Azerbaijan payroll tax", "mandatory health insurance Azerbaijan", "unemployment insurance Azerbaijan", "AZN salary net pay", "Azerbaijan income tax withholding", "non-oil/gas grace period", "PIT exemption AZN 8000", "what changes on 1 January 2026 in Azerbaijan", or any question about Azerbaijan employment-income contributions, the State Social Protection Fund, or the State Tax Service unified monthly declaration. Also trigger when classifying bank-statement transactions that relate to SSPF/DSMF debits, State Tax Service (taxes.gov.az) payments, mandatory health insurance, or salary payments in AZN from Azerbaijani banks (Kapital Bank, PASHA Bank, ABB / International Bank of Azerbaijan). This skill covers the two-track regime (non-oil/gas private sector grace period vs oil/gas & government standard rates), the 2025 social insurance / health / unemployment schedules, the confirmed 1 Jan 2026 changes, personal income tax withholding, filing forms, deadlines, penalties, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Azerbaijan payroll or social-contribution work.
version: 0.1
jurisdiction: AZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Social Contributions & Payroll Withholding

## Azerbaijan Social Contributions & Payroll Withholding Skill v0.1

> **Tier 2 (research-verified) skill. Confidence: medium.** Figures are corroborated primarily via PwC Worldwide Tax Summaries and a Mercans statutory alert; official authority sites (taxes.gov.az, dsmf.gov.az) are largely in Azerbaijani. A native-language review of the source laws is recommended before this skill is promoted to verified (Q1) status. Every figure below carries an inline citation or a `[RESEARCH GAP — reviewer to confirm]` marker.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Azerbaijan (Republic of Azerbaijan)
- **Currency** — AZN (Azerbaijani manat) — AZN only
- **Primary Legislation** — Law "On Social Insurance"; Law "On Medical Insurance"; Law "On Unemployment Insurance"; Tax Code of the Republic of Azerbaijan
- **Social fund authority** — State Social Protection Fund (SSPF / DSMF)
- **Health insurance authority** — State Agency on Mandatory Health Insurance
- **Tax / collection authority** — State Tax Service under the Ministry of Economy (taxes.gov.az)
- **Filing channel** — Unified monthly declaration on the State Tax Service e-portal (taxes.gov.az / e-gov.az)  _(PwC tax administration; e-gov.az)_
- **Has personal income tax?** — **Yes** — PIT is withheld at source by the employer  _(PwC)_
- **Two-track regime** — (a) non-oil/gas private sector under a 7-year grace period (1 Jan 2019 – 31 Dec 2025); (b) oil/gas & government (state) sectors at standard rates  _(PwC)_
- **Contribution ceiling** — **None** — social insurance and health insurance apply to full uncapped gross salary  _(PwC)_
- **Minimum monthly wage (2025)** — AZN 400/month, effective 1 Jan 2025 (Presidential Decree 23 Dec 2024; previously AZN 345)  _(APA / Presidential Decree)_
- **Monthly filing deadline** — 20th of the following month; withheld PIT remitted on the day income is paid  _(PwC; e-gov.az)_
- **Annual PIT return** — 31 March of the following year (3-month extension possible if tax paid on time)  _(PwC)_
- **Default tax year for this skill** — 2025 (grace-period figures); 2026 figures shown as forward-looking
- **Verified by** — Pending — requires sign-off by an Azerbaijan-qualified tax professional
- **Validation date** — Pending

**Two-track regime — this determines BOTH income tax and social insurance figures.** Always establish the sector before computing.

**Two-track regime table**  _(PwC)_

| Track | Who | Source |
| --- | --- | --- |
| Non-oil/gas private sector | Private employers outside the oil-and-gas sector (the most common case) | PwC |
| Oil/gas & government (state) sectors | Oil-and-gas industry employers and government/state-budget employers | PwC |

**2025 contribution overview (non-oil/gas private sector — the default)**  _(PwC)_

| Contribution | Employee | Employer | Combined | Source |
| --- | --- | --- | --- | --- |
| Social insurance (SSPF), first AZN 200 | 3% (= AZN 6) | 22% (= AZN 44) | 25% (= AZN 50) | PwC |
| Social insurance (SSPF), amount above AZN 200 | 10% of excess | 15% of excess | 25% of excess | PwC |
| Unemployment insurance | 0.5% | 0.5% | 1.0% | PwC |
| Mandatory medical insurance, up to AZN 8,000 | 2% | 2% | 4% | PwC |
| Mandatory medical insurance, excess above AZN 8,000 | 0.5% of excess (+ AZN 160 base) | 0.5% of excess (+ AZN 160 base) | 1.0% of excess (+ AZN 320 base) | PwC |

> Arithmetic check (first AZN 200 block): employee AZN 6 + employer AZN 44 = AZN 50 combined ✓. Marginal rates above AZN 200: employee 10% + employer 15% = 25% combined ✓. Medical up-to-8,000: 2% + 2% = 4% ✓.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown sector | Treat as **non-oil/gas private sector** (most common; grace-period rates) |
| Unknown period / year boundary | For periods on/after 1 Jan 2026 apply the new progressive PIT, reduced above-8,000 SSPF and reduced above-2,500 health insurance; otherwise use 2025 grace-period figures |
| Unknown ceiling | **No ceiling** — compute on full uncapped gross |
| Unknown PIT residency / foreign-source income | Assume employer withholding only on Azerbaijan-source employment income; flag annual-return obligations for reviewer |
| Diplomat / PSA expatriate status claimed | STOP — different rules apply; escalate to reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — Minimum viable — gross monthly salary (AZN), the **sector** (non-oil/gas private vs oil/gas & government), and the **pay period / year** (2025 vs 2026). Without the sector you cannot select the correct PIT and SSPF schedule; without the period you cannot tell whether the 2026 changes apply.
- **Recommended** — Recommended — whether the employee is a foreign national (and if so whether diplomatic status or a Production Sharing Agreement applies), and whether the employer is benefitting from the state subsidy of private-sector social insurance.
- **Ideal** — Ideal — the employer's filed unified monthly declarations, bank statements showing salary debits and SSPF / State Tax Service / health-insurance payments, and the prior-year annual PIT return if any.

### Refusal catalogue

- **R-AZ-SC-1 — Sector unknown** — Trigger: employer sector (non-oil/gas private vs oil/gas & government) not provided. Message: "The sector is mandatory. Azerbaijan operates a two-track regime: non-oil/gas private-sector employees are under a 7-year grace period (different PIT and social-insurance schedules) through 31 Dec 2025, while oil/gas and government employees pay standard rates. I cannot select the correct schedule without the sector."  _(PwC)_
- **R-AZ-SC-2 — Diplomatic or PSA expatriate** — Trigger: employee has diplomatic status or works under a Production Sharing Agreement (PSA). Message: "Diplomatic staff and expatriates working under Production Sharing Agreements are exempt from the standard social-insurance rates. These cases are out of scope for this skill — escalate to a qualified Azerbaijan tax professional."  _(PwC)_
- **R-AZ-SC-3 — Penalty / arrears quantification** — Trigger: client asks for an exact penalty or interest figure on late or underreported contributions. Message: "Exact penalty and interest figures (the cited ~0.1%/day interest capped around one year, and the ~10% understatement fine) come from secondary payroll guides, not the Tax Code text — they must be confirmed against the current Tax Code of Azerbaijan. Do not quantify; flag for reviewer."  _(RemotePeople — secondary)_
- **R-AZ-SC-4 — State subsidy reliance** — Trigger: client wants to rely on the state subsidy of private-sector social-insurance contributions to reduce a quoted figure. Message: "The state subsidy (reported as 100% of private-sector mandatory social insurance through 31 Dec 2025, dropping to 80% for 2026–2028) is from a secondary summary; the underlying presidential/government decree must be verified before relying on it. Escalate to a reviewer."  _(Multiplier — secondary; RESEARCH GAP — reviewer to confirm decree)_
- **R-AZ-SC-5 — Self-employed / independent entrepreneur** — Trigger: the individual is a self-employed entrepreneur, not an employee. Message: "This skill computes employer/employee payroll contributions and salary withholding. Independent entrepreneurs file quarterly advance PIT (due the 15th of the month after each quarter, final settlement 31 March) and have a distinct social-insurance basis — flag for reviewer."  _(PwC)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to Azerbaijan payroll and social contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Social-insurance, health-insurance, unemployment and PIT remittances are statutory payroll obligations — they are EXCLUDED from any VAT/turnover-tax classification and are not business supplies.

### 3.1 State Social Protection Fund (SSPF / DSMF) debits

**3.1 State Social Protection Fund (SSPF / DSMF) debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DSMF, DSMF.GOV.AZ | EXCLUDE — social insurance | State Social Protection Fund |
| SSPF, SOCIAL PROTECTION FUND | EXCLUDE — social insurance | English rendering |
| SOSIAL MÜDAFIƏ, SOSIAL SIĞORTA | EXCLUDE — social insurance | Azerbaijani: "social protection / social insurance" |
| MƏCBURI DÖVLƏT SOSIAL SIĞORTA | EXCLUDE — social insurance | "Mandatory state social insurance" |

### 3.2 State Tax Service (PIT withholding & combined remittances)

**3.2 State Tax Service table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VERGILƏR, TAXES.GOV.AZ | EXCLUDE — tax/contribution remittance | State Tax Service e-portal |
| STATE TAX SERVICE, VERGI XIDMƏTI | EXCLUDE — PIT/payroll remittance | Unified monthly declaration |
| GƏLIR VERGISI, INCOME TAX | EXCLUDE — PIT withholding | Personal income tax at source |

### 3.3 Mandatory health & unemployment insurance

**3.3 Mandatory health & unemployment insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TIBBI SIĞORTA, MEDICAL INSURANCE | EXCLUDE — mandatory health insurance | State Agency on Mandatory Health Insurance |
| ICBARI TIBBI SIĞORTA | EXCLUDE — mandatory health insurance | "Compulsory medical insurance" |
| IŞSIZLIKDƏN SIĞORTA, UNEMPLOYMENT | EXCLUDE — unemployment insurance | 0.5% + 0.5% |

### 3.4 Salary and payroll (exclude from contribution classification)

**3.4 Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ƏMƏK HAQQI, MAAŞ, SALARY (outgoing) | EXCLUDE — payroll expense | Wage payment, not a contribution |
| MAAŞ, SALARY (incoming) | EXCLUDE — employment income received | Not a contribution |

### 3.5 Benefits received (not contributions)

**3.5 Benefits received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSIYA, PENSION | EXCLUDE — pension income received | Benefit, not a contribution paid |
| MÜAVINƏT, ALLOWANCE / BENEFIT | EXCLUDE — social benefit received | Not a contribution |

## Section 4 -- Worked examples

Six payroll classifications/computations for a hypothetical Baku-based employee. All amounts in AZN. Default sector is non-oil/gas private unless stated.

### Example 1 -- Standard private-sector salary, 2025 (below all break points)

**Input line:**
`31.03.2025 ; ƏMƏK HAQQI MART ; CREDIT ; SALARY MAR ; +1,764.00 ; AZN`

**Facts:** Gross AZN 2,000/month, non-oil/gas private sector, 2025.

**Reasoning (2025 non-oil/gas):**
- SSPF employee: AZN 6 + 10% × (2,000 − 200) = 6 + 180 = **AZN 186** [PwC]
- Unemployment employee: 0.5% × 2,000 = **AZN 10** [PwC]
- Medical employee: 2% × 2,000 = **AZN 40** (below AZN 8,000) [PwC]
- PIT: 0% up to AZN 8,000 → **AZN 0** [PwC]
- Net pay = 2,000 − 186 − 10 − 40 − 0 = **AZN 1,764.00** ✓ (matches the credit line)

Employer cost on top of gross: SSPF AZN 44 + 15% × 1,800 = 44 + 270 = AZN 314; unemployment AZN 10; medical AZN 40 → employer add-on = **AZN 364**.

**Classification:** Salary credit EXCLUDE from VAT. Net AZN 1,764.00.

### Example 2 -- Private-sector salary, 2025 (above AZN 8,000 PIT/medical break)

**Facts:** Gross AZN 10,000/month, non-oil/gas private sector, 2025.

**Reasoning (2025 non-oil/gas):**
- SSPF employee: 6 + 10% × (10,000 − 200) = 6 + 980 = **AZN 986** [PwC]
- Unemployment employee: 0.5% × 10,000 = **AZN 50** [PwC]
- Medical employee: 2% × 8,000 + 0.5% × (10,000 − 8,000) = 160 + 10 = **AZN 170** [PwC]
- PIT: 14% × (10,000 − 8,000) = **AZN 280** [PwC]
- Net pay = 10,000 − 986 − 50 − 170 − 280 = **AZN 8,514.00**

Employer SSPF: 44 + 15% × 9,800 = 44 + 1,470 = **AZN 1,514**; employer unemployment AZN 50; employer medical AZN 170.

**Classification:** EXCLUDE from VAT. Net AZN 8,514.00; total employer-side contributions (employee + employer) remitted via the unified monthly declaration.

### Example 3 -- Same salary, 2026 changes applied (above AZN 8,000)

**Facts:** Gross AZN 10,000/month, non-oil/gas private sector, **2026**.

**Reasoning (2026 non-oil/gas):**
- SSPF employee (above 8,000): AZN 786 + 10% × (10,000 − 8,000) = 786 + 200 = **AZN 986** [PwC corporate page]
- Unemployment employee: 0.5% × 10,000 = **AZN 50** [PwC]
- Medical employee (non-state, above 2,500): 2% × 2,500 + 0.5% × (10,000 − 2,500) = 50 + 37.50 = **AZN 87.50** [PwC corporate page]
- PIT (progressive): 3% × 2,500 + 10% × (8,000 − 2,500) + 14% × (10,000 − 8,000) = 75 + 550 + 280 = **AZN 905** [Mercans]
- Net pay = 10,000 − 986 − 50 − 87.50 − 905 = **AZN 7,971.50**

Employer SSPF (above 8,000): AZN 1,214 + 11% × 2,000 = 1,214 + 220 = **AZN 1,434** [PwC corporate page].

**Note:** Above AZN 8,000 the combined SSPF rate falls from 25% to 21% (10% employee + 11% employer) from 1 Jan 2026 [PwC]. Above AZN 2,500 the combined medical rate falls from 4% to 1% (0.5% + 0.5%) [PwC].

**Classification:** EXCLUDE from VAT. Net AZN 7,971.50.

### Example 4 -- Oil/gas or government employee, 2025 (standard rates)

**Facts:** Gross AZN 3,000/month, government (state) sector, 2025.

**Reasoning (standard rates):**
- SSPF employee: 3% × 3,000 = **AZN 90** [PwC]
- Unemployment employee: 0.5% × 3,000 = **AZN 15** [PwC]
- Medical employee: 2% × 3,000 = **AZN 60** (below AZN 8,000) [PwC]
- PIT (oil/gas & government): 14% × 2,500 + 25% × (3,000 − 2,500) = 350 + 125 = **AZN 475** [PwC]
- Net pay = 3,000 − 90 − 15 − 60 − 475 = **AZN 2,360.00**

Employer SSPF: 22% × 3,000 = **AZN 660**; employer unemployment AZN 15; employer medical AZN 60.

**Classification:** EXCLUDE from VAT. Net AZN 2,360.00. Note the standard 3%/22% SSPF (combined 25%) and the AZN 2,500 PIT break — these differ sharply from the private-sector grace-period figures.

### Example 5 -- SSPF debit on a bank statement (employer remittance)

**Input line:**
`20.04.2025 ; DSMF MƏCBURI SOSIAL SIĞORTA ; DEBIT ; MART 2025 ; -500.00 ; AZN`

**Reasoning:**
Matches "DSMF" / "MƏCBURI SOSIAL SIĞORTA" (patterns 3.1). This is the March-2025 mandatory state social-insurance remittance to the SSPF, paid on the 20th of the following month [e-gov.az; PwC]. It is a statutory payroll obligation, not a business supply.

**Classification:** EXCLUDE from VAT/turnover-tax. Record as social-insurance liability settlement.

### Example 6 -- Ambiguous State Tax Service debit (combined remittance or interest)

**Input line:**
`20.05.2025 ; VERGILƏR TAXES.GOV.AZ ; DEBIT ; ƏLAVƏ ÖDƏNIŞ ; -1,820.00 ; AZN`

**Reasoning:**
Matches "VERGILƏR / TAXES.GOV.AZ" (pattern 3.2) but the reference "ƏLAVƏ ÖDƏNIŞ" ("additional payment") and the irregular amount suggest it may bundle PIT, contributions and possibly late-payment interest (cited at ~0.1%/day, capped around one year — secondary source) [RemotePeople — secondary]. Cannot split principal from interest without the unified declaration.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request the unified monthly declaration to split PIT, SSPF, unemployment, health insurance and any interest/penalty. `[RESEARCH GAP — reviewer to confirm exact interest figure against the Tax Code.]`

## Section 5 -- Tier 1 rules

These rules apply when bank-statement data is clear and all required inputs (gross salary, sector, period) are available. Apply exactly as written.

### Rule 1 -- Establish the track first

- **Rule 1** — Azerbaijan operates a two-track regime: (a) non-oil/gas private sector under a 7-year grace period (1 Jan 2019 – 31 Dec 2025), and (b) oil/gas & government (state) sectors at standard rates. The track determines BOTH income tax and social insurance.  _(PwC)_

### Rule 2 -- 2025 social insurance (SSPF), non-oil/gas private sector

- **2025 SSPF formula** — Employee SSPF: gross <= 200:  3% x gross gross >  200:  6 + 10% x (gross - 200) Employer SSPF: gross <= 200:  22% x gross gross >  200:  44 + 15% x (gross - 200)  _(PwC)_

### Rule 3 -- Standard social insurance (oil/gas & government, and post-grace-period)

- **Rule 3** — Employee 3%, employer 22% — combined 25% — on full gross, no break point. This is also the rate that applies once the 7-year non-oil/gas grace regime ends.  _(PwC)_

### Rule 4 -- 2026 social insurance change (non-oil/gas private sector)

- **2026 SSPF formula above 8000** — From 1 Jan 2026, for wages above AZN 8,000 the combined SSPF rate drops from 25% to 21%: Employee SSPF (above 8,000):  786   + 10% x (gross - 8,000) Employer SSPF (above 8,000):  1,214 + 11% x (gross - 8,000) Below AZN 8,000 the marginal structure is unchanged (employee 6 + 10% above 200; employer 44 + 15% above 200).  _(PwC corporate page)_

### Rule 5 -- Unemployment insurance

- **Unemployment insurance rate** — 0.5% employee + 0.5% employer on gross salary (combined 1.0%), in force since 1 Jan 2018; unchanged for 2025/2026.  _(PwC)_

### Rule 6 -- Mandatory medical (health) insurance, 2025

- **2025 medical insurance rate** — 2% each (employee + employer) on income up to AZN 8,000; on the excess above AZN 8,000, AZN 160 + 0.5% each. In force since 1 Jan 2021.  _(PwC)_

### Rule 7 -- Mandatory medical insurance change, 2026 (non-state sector)

- **2026 medical insurance rate** — From 1 Jan 2026: 2% each up to AZN 2,500; on the excess above AZN 2,500, AZN 50 + 0.5% each — combined above-threshold rate falls from 4% to 1%. Oil/gas & government sectors keep the AZN 8,000 break (2% each up to 8,000; AZN 160 + 0.5% each above).  _(PwC corporate page)_

### Rule 8 -- No contribution ceiling

- **No ceiling rule** — Social insurance and health insurance have NO upper ceiling — contributions apply to the full gross salary. Do not impose a cap.  _(PwC)_

### Rule 9 -- Personal income tax (PIT) by track

- **PIT formula by track** — 2025 non-oil/gas private:   0% up to 8,000;  14% on excess above 8,000 2025 oil/gas & government:  14% up to 2,500; 350 + 25% on excess above 2,500 2026 non-oil/gas private:   3% up to 2,500; 10% on 2,501-8,000; 14% above 8,000 The 2026 bottom rate of 3% is scheduled to rise to 5% in 2027 and 7% from 2028.  _(PwC; Mercans)_

### Rule 10 -- Withholding & filing mechanics

- **Withholding and filing mechanics** — The employer withholds PIT at source; withheld PIT is remitted on the day income is paid to employees. A single unified monthly declaration on the State Tax Service e-portal covers PIT withholding, SSPF social insurance, unemployment insurance and mandatory health insurance, due by the **20th of the following month**.  _(PwC tax administration; e-gov.az)_

### Rule 11 -- Minimum monthly wage

- **Minimum monthly wage** — AZN 400/month effective 1 Jan 2025 (Presidential Decree 23 Dec 2024; previously AZN 345 since 1 Jan 2023). There is no statutory contribution floor, but the minimum wage is the practical employment floor.  _(APA / Presidential Decree; PwC)_

### Rule 12 -- Foreign employees

- **Foreign employees rule** — Foreign employees are subject to the same social-insurance rates, EXCEPT those with diplomatic status and expatriates working under Production Sharing Agreements (PSAs), who are exempt.  _(PwC)_

## Section 6 -- Tier 2 catalogue

When data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Year-boundary period straddling 1 Jan 2026

- **T2-1** — **Trigger:** Pay period spans late 2025 into 2026, or arrears relate to a pre-2026 period paid in 2026. **Issue:** The 2025 grace-period figures and the 2026 changes differ for PIT, above-8,000 SSPF and above-2,500 health insurance. The correct schedule depends on the period the salary relates to, not the payment date. **Action:** Flag for reviewer. Confirm the legal effective date and the period to which the salary relates.

### T2-2 -- End of the 7-year grace period

- **T2-2** — **Trigger:** Non-oil/gas private-sector employer for 2026+ where the grace regime (through 31 Dec 2025) has ended. **Issue:** The 7-year non-oil/gas grace period runs 1 Jan 2019 – 31 Dec 2025. Whether the standard 3%/22% SSPF and the standard PIT apply from 2026, or the new 2026 progressive schedule applies, depends on which transitional rule governs. The research data shows a new progressive PIT and reduced above-threshold contribution rates from 2026 for the non-oil/gas private sector. [PwC; Mercans] **Action:** Flag for reviewer. `[RESEARCH GAP — reviewer to confirm the 2026 transitional rule against the Tax Code amendments.]`

### T2-3 -- State subsidy of private-sector social insurance

- **T2-3** — **Trigger:** Employer wants to net off the state subsidy. **Issue:** A state subsidy reportedly covered 100% of private-sector mandatory social-insurance contributions from 1 Jan 2023 to 31 Dec 2025, reducing to 80% for 2026–2028 — but this is from a secondary summary, not the decree text. [Multiplier — secondary] **Action:** Flag for reviewer. Do not net the subsidy without the underlying decree. `[RESEARCH GAP — reviewer to confirm decree.]`

### T2-4 -- First-AZN-200 employer rate discrepancy

- **T2-4** — **Trigger:** Computing the 2025 employer SSPF on the first AZN 200. **Issue:** PwC's individual page in one rendering shows the lower-tier employer rate as 2% on the first AZN 200, while the corporate page and the prevailing market figure is 22% on the first AZN 200 (AZN 44). This skill uses **22% / AZN 44**, consistent with the standard 22% employer rate and the corporate page. [PwC corporate page] **Action:** Reviewers should confirm the first-AZN-200 employer figure against the Law "On Social Insurance." `[RESEARCH GAP — reviewer to confirm.]`

### T2-5 -- Mixed oil/gas and non-oil/gas employment

- **T2-5** — **Trigger:** Employee works partly in an oil/gas entity and partly in a non-oil/gas entity, or the employer's sector classification is disputed. **Issue:** The track determines PIT and SSPF; misclassification swings the figures materially (e.g. 0% vs 14% PIT below AZN 8,000). **Action:** Flag for reviewer to confirm the employer's sector registration.

### T2-6 -- Penalties and late-payment interest

- **T2-6** — **Trigger:** Client asks for the cost of late or incorrect filing. **Issue:** Secondary guides cite ~0.1%/day interest (capped around one year) and a ~10% understatement fine, but these are not from the Tax Code text. [RemotePeople — secondary] **Action:** Do not quantify. Escalate to a reviewer. `[RESEARCH GAP — reviewer to confirm against the Tax Code of Azerbaijan.]`

## Section 7 -- Excel working paper template

When producing an Azerbaijan payroll computation, structure the working paper as follows:

```
AZERBAIJAN PAYROLL & SOCIAL CONTRIBUTIONS -- WORKING PAPER
Client/Employee: [name]
Tax Year / Period:  [2025 / 2026 / month]
Prepared:           [date]

INPUT DATA
  Gross monthly salary (AZN):   [____]
  Sector:  [Non-oil/gas private / Oil-gas / Government]
  Period on/after 1 Jan 2026:   [YES/NO]
  Foreign national:             [YES/NO]
  Diplomatic / PSA status:      [YES/NO -> if YES, STOP & escalate]

EMPLOYEE DEDUCTIONS
  SSPF social insurance:        AZN [____]
  Unemployment insurance:       AZN [____]   (0.5% x gross)
  Mandatory health insurance:   AZN [____]
  Personal income tax (PIT):    AZN [____]
  Total employee deductions:    AZN [____]
  NET PAY:                      AZN [____]   (gross - total deductions)

EMPLOYER CONTRIBUTIONS (on top of gross)
  SSPF social insurance:        AZN [____]
  Unemployment insurance:       AZN [____]   (0.5% x gross)
  Mandatory health insurance:   AZN [____]
  Total employer cost add-on:   AZN [____]
  TOTAL COST OF EMPLOYMENT:     AZN [____]   (gross + employer add-on)

FILING
  Unified monthly declaration due:  20th of following month
  PIT remitted:                     day income is paid

REVIEWER FLAGS
  [List any Tier 2 flags / RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How payroll & contribution flows appear on Azerbaijani bank statements

**Kapital Bank / PASHA Bank / ABB (International Bank of Azerbaijan):**
- Salary credit: "ƏMƏK HAQQI" / "MAAŞ" / "SALARY" (incoming to employee account)
- SSPF remittance: "DSMF" / "MƏCBURI SOSIAL SIĞORTA" / "SOSIAL MÜDAFIƏ FONDU" (outgoing, employer)
- Tax/PIT remittance: "VERGILƏR" / "TAXES.GOV.AZ" / "GƏLIR VERGISI" (outgoing, employer)
- Health insurance: "ICBARI TIBBI SIĞORTA" / "MEDICAL INSURANCE" (outgoing)
- Unemployment: "IŞSIZLIKDƏN SIĞORTA" (outgoing)

**Timing tips:**
1. Contribution and PIT remittances cluster around the **20th of the month** (the unified declaration deadline) [e-gov.az; PwC].
2. PIT may be remitted on the salary-payment day, separate from the 20th-of-month declaration [PwC].
3. Contribution debits are always outgoing (employer side); salary credits are incoming (employee side).
4. There is no contribution ceiling, so high-salary months produce proportionally larger debits (with the marginal-rate breaks at AZN 200, AZN 2,500 and AZN 8,000) [PwC].
5. Irregular lump sums referencing "ƏLAVƏ ÖDƏNIŞ" (additional payment) may include interest/penalties — flag for reviewer.

### Azerbaijani / English glossary

**Azerbaijani / English glossary table**

| Azerbaijani | English |
| --- | --- |
| ƏmƏk haqqı / maaş | Salary / wage |
| MƏcburi dövlƏt sosial sığorta | Mandatory state social insurance (SSPF) |
| DSMF | State Social Protection Fund (SSPF) |
| Gəlir vergisi | Income tax (PIT) |
| Icbari tibbi sığorta | Compulsory medical insurance |
| Işsizlikdən sığorta | Unemployment insurance |
| Vergilər | Taxes |
| Pensiya | Pension |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for outgoing remittances** matching Section 3 patterns (DSMF, VERGILƏR, tibbi sığorta, işsizlikdən sığorta).
2. **Identify the salary base** from incoming "MAAŞ / ƏMƏK HAQQI" credits, or back out gross from the deductions if only net is visible.
3. **Establish the sector** — you cannot select PIT/SSPF schedules without it. If unknown, default to non-oil/gas private and flag.
4. **Establish the period** — apply 2025 grace-period figures by default; apply 2026 changes only for periods on/after 1 Jan 2026.
5. **Flag for reviewer:** "Computation derived from bank-statement amounts only. Sector, period, and foreign/diplomatic status have not been independently verified. A reviewer must confirm before filing the unified monthly declaration."

### Thresholds (break points)

**Thresholds (break points)**  _(PwC; APA / Presidential Decree)_

| Threshold | Meaning | Source |
| --- | --- | --- |
| AZN 200/month | Social-insurance break point: lower marginal rates on first AZN 200 (3% employee / 22% employer), higher above | PwC |
| AZN 2,500/month | Oil/gas & government PIT break (14% below; AZN 350 + 25% above); and the 2026 non-state health-insurance break | PwC |
| AZN 8,000/month | Key break point — 2025 non-oil/gas PIT (0% below, 14% above) and social/health-insurance tiering | PwC |
| AZN 400/month | Statutory minimum monthly wage (2025) | APA / Presidential Decree |

### Rate summary (combined employee + employer, on full uncapped gross)

**Rate summary (combined employee + employer, on full uncapped gross)**  _(PwC)_

| Item | 2025 non-oil/gas private | 2025 oil/gas & government | 2026 non-oil/gas private | Source |
| --- | --- | --- | --- | --- |
| SSPF, first AZN 200 | 25% (6 + 44) | 25% (flat 3% + 22%) | 25% (6 + 44) | PwC |
| SSPF, AZN 200–8,000 | 25% (10% + 15%) | 25% | 25% (10% + 15%) | PwC |
| SSPF, above AZN 8,000 | 25% (10% + 15%) | 25% | 21% (10% + 11%) | PwC |
| Unemployment | 1.0% (0.5% + 0.5%) | 1.0% | 1.0% | PwC |
| Medical, up to break | 4% (2% + 2%) up to 8,000 | 4% up to 8,000 | 4% up to 2,500 | PwC |
| Medical, above break | 1.0% (0.5% + 0.5%) above 8,000 | 1.0% above 8,000 | 1.0% above 2,500 | PwC |

### Personal income tax brackets

**Personal income tax brackets**  _(PwC; Mercans)_

| Regime | Bracket 1 | Bracket 2 | Bracket 3 | Source |
| --- | --- | --- | --- | --- |
| 2025 non-oil/gas private | up to 8,000: 0% | above 8,000: 14% of excess | — | PwC |
| 2025 oil/gas & government | up to 2,500: 14% | above 2,500: 350 + 25% of excess | — | PwC |
| 2026 non-oil/gas private | up to 2,500: 3% | 2,501–8,000: 10% | above 8,000: 14% | Mercans |

### Personal income tax brackets

Cumulative-tax check (2026, AZN 8,000): 3% × 2,500 + 10% × 5,500 = 75 + 550 = AZN 625 at the AZN 8,000 ceiling; the third bracket adds 14% of any excess above AZN 8,000 ✓. Oil/gas 2025 at AZN 2,500: 14% × 2,500 = AZN 350, matching the "AZN 350 +" base of the second bracket ✓.

### Forms

**Forms**  _(PwC; e-gov.az)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Unified monthly payroll/withholding declaration (State Tax Service e-portal) | Reports PIT withheld plus SSPF social insurance, unemployment and mandatory health insurance | 20th of the following month | PwC; e-gov.az |
| Annual personal income tax return | Residents with untaxed/foreign-source income; non-residents with non-withheld AZ-source income | 31 March of the following year (3-month extension possible if tax paid on time) | PwC |
| Quarterly advance payments (independent entrepreneurs) | Estimated PIT for self-employed/entrepreneurs | 15th of the month after each quarter; final settlement 31 March | PwC |

### Penalties

**Penalties**  _(RemotePeople — secondary)_

| Type | Amount | Source |
| --- | --- | --- |
| Late payment of taxes/contributions (interest) | ~0.1% per day on overdue amounts, accruing up to ~one year `[RESEARCH GAP — confirm against Tax Code]` | RemotePeople — secondary |
| Underreporting / understatement / late or incorrect filing | Administrative fines; secondary guides cite up to ~10% plus daily interest `[RESEARCH GAP — confirm against Tax Code]` | RemotePeople — secondary |

### Test suite

**Test 1:** Gross AZN 2,000, non-oil/gas private, 2025. → Employee SSPF 186, unemployment 10, medical 40, PIT 0. Net = **AZN 1,764.00**.

**Test 2:** Gross AZN 10,000, non-oil/gas private, 2025. → Employee SSPF 986, unemployment 50, medical 170, PIT 280. Net = **AZN 8,514.00**.

**Test 3:** Gross AZN 10,000, non-oil/gas private, 2026. → Employee SSPF 986, unemployment 50, medical 87.50, PIT 905. Net = **AZN 7,971.50**.

**Test 4:** Gross AZN 3,000, government sector, 2025. → Employee SSPF 90 (3%), unemployment 15, medical 60, PIT 475 (350 + 25% × 500). Net = **AZN 2,360.00**.

**Test 5:** Gross AZN 200, non-oil/gas private, 2025. → Employee SSPF 6 (3% × 200), unemployment 1, medical 4, PIT 0. Net = **AZN 189.00**.

**Test 6:** Gross AZN 8,000, non-oil/gas private, 2025. → Employee SSPF 6 + 10% × 7,800 = 786; unemployment 40; medical 2% × 8,000 = 160; PIT 0 (at the AZN 8,000 ceiling, still 0%). Net = 8,000 − 786 − 40 − 160 − 0 = **AZN 7,014.00**.

**Test 7:** Gross AZN 8,000, non-oil/gas private, 2026. → Employee SSPF 786 (at ceiling); unemployment 40; medical 2% × 2,500 + 0.5% × 5,500 = 50 + 27.50 = 77.50; PIT 3% × 2,500 + 10% × 5,500 = 75 + 550 = 625. Net = 8,000 − 786 − 40 − 77.50 − 625 = **AZN 6,471.50**.

- **Test 8** — STOP. Exempt from standard social-insurance rates; escalate to reviewer (R-AZ-SC-2).  _(R-AZ-SC-2)_

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
