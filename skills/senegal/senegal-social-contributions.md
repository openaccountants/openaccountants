---
name: senegal-social-contributions
description: Use this skill whenever asked about Senegal social security / social insurance contributions and employer payroll taxes for employees, directors, or expatriate staff. Trigger on phrases like "how much IPRES do I pay", "Senegal social security", "CSS contribution", "IPM health insurance", "CFCE payroll tax", "Senegal payroll deductions", "IPRES cadre scheme", "retenue IRPP", "cotisation sociale Sénégal", "Senegal employer charges", or any question about Senegalese payroll contribution obligations. Also trigger when classifying bank statement transactions that relate to IPRES, CSS, IPM, CFCE, or DGID/Trésor Public payroll debits from CBAO, SGBS, Ecobank, BICIS, or other Senegalese banks. Also trigger when preparing the monthly PAYE (retenue à la source) and the annual recapitulative payroll returns. This skill covers IPRES (general + cadre), CSS (family allowances + work injury), IPM health insurance, CFCE employer payroll tax, the IRPP progressive scale, the art. 174 family reduction, TRIMF, contribution ceilings, payment/filing schedule, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Senegal payroll or social-contribution work.
version: 0.2
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal Social Security & Payroll Contributions

## Senegal Social Security & Payroll Contributions Skill v0.2

> **Currency:** West African CFA franc — **XOF** (written CFA / FCFA). All figures below are in XOF.
> **Senegal levies personal income tax (IRPP).** The "no income tax" special case does **not** apply.
> **Authority:** tax rules come from the CGI (January 2025 edition, on dgid.sn). Social contribution rates come from PwC Worldwide Tax Summaries (reviewed 31 March 2026) and CLEISS (table at 1 January 2026), because the IPRES and CSS sites did not open.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Republic of Senegal
- **Primary Legislation** — Code Général des Impôts (CGI); Code de la Sécurité Sociale; Code du Travail
- **Income tax** — IRPP — Impôt sur le Revenu des Personnes Physiques
- **Pension institution** — IPRES — Institution de Prévoyance Retraite du Sénégal
- **Family/work-injury institution** — CSS — Caisse de Sécurité Sociale
- **Health institution** — IPM — Institution de Prévoyance Maladie (employer-level fund)
- **Employer payroll tax** — CFCE — Contribution Forfaitaire à la Charge de l'Employeur (3%)
- **Tax authority** — DGID — Direction Générale des Impôts et des Domaines; collection via Trésor Public
- **Rate publisher (research basis)** — PwC Worldwide Tax Summaries — Senegal (reviewed 31 Mar 2026)
- **PAYE frequency** — Monthly withholding (retenue à la source) on gross remuneration
- **Currency** — XOF (CFA franc) only
- **Validated by** — Pending — requires sign-off by a Senegalese chartered accountant (expert-comptable / OHADA)
- **Validation date** — Pending

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Senegal |
| Primary Legislation | Code Général des Impôts (CGI); Code de la Sécurité Sociale; Code du Travail |
| Income tax | IRPP — Impôt sur le Revenu des Personnes Physiques |
| Pension institution | IPRES — Institution de Prévoyance Retraite du Sénégal |
| Family/work-injury institution | CSS — Caisse de Sécurité Sociale |
| Health institution | IPM — Institution de Prévoyance Maladie (employer-level fund) |
| Employer payroll tax | CFCE — Contribution Forfaitaire à la Charge de l'Employeur (3%) |
| Tax authority | DGID — Direction Générale des Impôts et des Domaines; collection via Trésor Public |
| Rate publisher (research basis) | PwC Worldwide Tax Summaries — Senegal (reviewed 31 Mar 2026) |
| PAYE frequency | Monthly withholding (retenue à la source) on gross remuneration |
| Currency | XOF (CFA franc) only |
| Validated by | Pending — requires sign-off by a Senegalese chartered accountant (expert-comptable / OHADA) |
| Validation date | Pending |

**Contribution overview (employer + employee shares)**  _(PwC (other-taxes / corporate), reviewed 31 Mar 2026)_

| Scheme | Employer | Employee | Total | Monthly base ceiling | Source |
| --- | --- | --- | --- | --- | --- |
| IPRES — General (Régime Général) | 8.4% | 5.6% | 14% | 432,000 | PwC (other-taxes), reviewed 31 Mar 2026 |
| IPRES — Cadre (Régime Complémentaire des Cadres) | 3.6% | 2.4% | 6% | 1,296,000 | PwC (other-taxes), reviewed 31 Mar 2026 |
| CSS — Family allowances (prestations familiales) | 7% | 0% | 7% | 63,000 | PwC (corporate/other-taxes), reviewed 31 Mar 2026 |
| CSS — Work injury (accidents du travail) | 1% / 3% / 5% | 0% | 1–5% | 63,000 | PwC (corporate/other-taxes), reviewed 31 Mar 2026 |
| IPM — Health insurance | 3% | 3% | 6% | 60,000–250,000 | PwC (corporate/other-taxes), reviewed 31 Mar 2026 — see gap note |
| CFCE — Employer payroll tax | 3% | 0% | 3% | No ceiling (full payroll) | PwC (corporate/other-taxes), reviewed 31 Mar 2026 |

> **Arithmetic check:** IPRES General 8.4 + 5.6 = 14% ✓. IPRES Cadre 3.6 + 2.4 = 6% ✓. IPM 3 + 3 = 6% ✓. CSS and CFCE are 100% employer-borne ✓.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether employee is a "cadre" (executive) | Assume NON-cadre — apply IPRES General only; flag for reviewer |
| Unknown CSS work-injury risk category | Apply 5% (highest) as conservative; flag — actual rate is set by CSS on registration |
| Unknown gross above a scheme ceiling | Apply the ceiling base, not the full gross, for that scheme |
| Unknown IPM rate/fund | Apply 3% employer + 3% employee on base capped at 250,000; mark [RESEARCH GAP] |
| Unknown number of parts | Compute on 1 part (single, no children): no family reduction, highest IRPP; flag for reviewer |
| Unknown whether DGID/Trésor debit is IRPP or social | Classify as statutory payroll obligation; flag for reviewer to split |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — monthly gross remuneration (XOF) and whether the employee is a **cadre** (executive/manager) or non-cadre. Without gross remuneration, STOP.

**Recommended**: CSS work-injury risk category (1%/3%/5%), number of parts (marital status + dependent children), and which IPM fund the employer has joined.

**Ideal** — the employer's IPRES/CSS/IPM registration certificates (showing the exact assigned rates), prior payroll journals, and bank statements showing the monthly contribution debits.

### Refusal catalogue

- **R-SN-SOC-1 -- Cadre vs non-cadre status unknown** — The IPRES complementary cadre scheme (extra 6%, employer 3.6% / employee 2.4%) applies only to executives/managers. Cannot finalise IPRES without confirming cadre status. Defaulting to non-cadre (General only) and flagging for reviewer. (Trigger: not stated whether the employee is a cadre.)
- **R-SN-SOC-2 -- CSS work-injury rate** — The CSS accidents-du-travail rate (1%, 3%, or 5%) is set by the Caisse de Sécurité Sociale per risk category on the employer's registration. Do not assume a rate; obtain the CSS registration certificate. Defaulting to 5% conservatively and flagging. (Trigger: work-injury rate not provided.)
- **R-SN-SOC-3 -- IPM rate/ceiling ambiguity** — [RESEARCH GAP — reviewer to confirm] PwC's individual and corporate pages describe IPM differently (2%–7.5% each vs 6% split 3%/3%) and the precise rate/ceiling depends on the specific IPM fund the employer joined. Do not present IPM as definitive — confirm against the actual IPM scheme. (Trigger: IPM computation requested.)
- **R-SN-SOC-4 -- Family parts**: Parts give a reduction on the tax (CGI art. 174), not a division of income; maximum 5 parts. Without evidence of family situation, compute on 1 part and flag. (Trigger: IRPP requested with dependants.)
- **R-SN-SOC-5 -- Arrears / back-contributions** — Late social-contribution and IRPP regularisation carries 5% interest plus 0.5% per month of delay (PwC). Do not quantify arrears without the institution's statement. Escalate to a Senegalese expert-comptable. (Trigger: unpaid prior-period contributions.)

## Section 3 -- Payment pattern library

Deterministic pre-classifier for Senegalese bank statement transactions related to payroll/social contributions. Match by case-insensitive substring on the counterparty/reference as it appears in the statement. These are statutory payroll obligations — **EXCLUDE** them from any VAT (TVA) return and never treat them as a business supply.

### 3.1 Pension contributions (IPRES)

**Pension contributions (IPRES) patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IPRES, INST PREVOYANCE RETRAITE | EXCLUDE — pension contribution | General + cadre combined remittance |
| RETRAITE, COTISATION RETRAITE | EXCLUDE — pension contribution | French-language reference |
| REGIME GENERAL, REGIME CADRES | EXCLUDE — pension contribution | Explicit scheme reference |

### 3.2 Social security — family allowances & work injury (CSS)

**CSS patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CSS, CAISSE DE SECURITE SOCIALE | EXCLUDE — CSS contribution | Family allowances + work injury |
| PRESTATIONS FAMILIALES, ALLOC FAMILIALES | EXCLUDE — CSS family branch | Employer-only |
| ACCIDENT TRAVAIL, ACCIDENTS DU TRAVAIL | EXCLUDE — CSS work-injury branch | Employer-only |

### 3.3 Health insurance (IPM)

**IPM patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IPM, INST PREVOYANCE MALADIE | EXCLUDE — health contribution | Employer + employee share |
| MALADIE, COTISATION MALADIE | EXCLUDE — health contribution | French-language reference |

### 3.4 Employer payroll tax & income tax to DGID / Trésor

**CFCE / IRPP / DGID / TVA patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CFCE, CONTRIBUTION FORFAITAIRE | EXCLUDE — employer payroll tax (3%) | Employer-only, no ceiling |
| TRIMF, RETENUE TRIMF | EXCLUDE: fixed tax withheld with IRPP | Art. 282 annual table |
| IRPP, RETENUE A LA SOURCE, RAS | EXCLUDE — PAYE income tax withheld | Not a social contribution |
| DGID, IMPOTS, TRESOR PUBLIC | EXCLUDE — tax remittance | Could be IRPP and/or CFCE — flag to split |
| TVA, TAXE VALEUR AJOUTEE | EXCLUDE — VAT, not payroll | Separate obligation |

### 3.5 Salary & pension received (not contributions)

**Salary/pension received patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, NET A PAYER (outgoing) | EXCLUDE — payroll expense | Net wage to employee, not a contribution |
| SALAIRE, PAIE (incoming) | EXCLUDE — employment income received | Not a contribution |
| PENSION IPRES, PENSION RETRAITE (incoming) | EXCLUDE — pension income received | Benefit received, not a contribution paid |

## Section 4 -- Worked examples

Bank statement classifications and computations for a hypothetical Dakar-based services company and its staff. All amounts XOF. PwC figures (reviewed 31 Mar 2026) underlie every rate.

### Example 1 -- Non-cadre at the IPRES general ceiling (CBAO)

**Input line:**
`30.06.2026 ; IPRES COTISATION RETRAITE ; DEBIT ; REGIME GENERAL JUIN ; -60,480 ; XOF`

**Reasoning:**
Employee monthly gross 500,000 but the IPRES General base is **capped at 432,000**. IPRES General total 14% × 432,000 = 60,480 (employer 8.4% × 432,000 = 36,288; employee 5.6% × 432,000 = 24,192; 36,288 + 24,192 = 60,480 ✓). Non-cadre, so no complementary scheme. Matches pattern 3.1.

**Classification:** EXCLUDE — IPRES pension contribution. Statutory; not a VAT-bearing supply.

### Example 2 -- Cadre executive, both IPRES schemes (SGBS)

**Input line:**
`30.06.2026 ; IPRES REGIME CADRES ; DEBIT ; COMPLEMENTAIRE JUIN ; -77,760 ; XOF`

**Reasoning:**
Cadre with gross 1,296,000 (at the cadre ceiling). Complementary cadre scheme total 6% × 1,296,000 = 77,760 (employer 3.6% × 1,296,000 = 46,656; employee 2.4% × 1,296,000 = 31,104; 46,656 + 31,104 = 77,760 ✓). This is **in addition** to the General scheme (14% on base capped at 432,000 = 60,480, billed separately). Matches pattern 3.1.

**Classification:** EXCLUDE — IPRES cadre complementary contribution.

### Example 3 -- CSS employer remittance (Ecobank)

**Input line:**
`15.07.2026 ; CSS CAISSE SECURITE SOCIALE ; DEBIT ; PRESTATIONS+AT JUIN ; -5,040 ; XOF`

**Reasoning:**
CSS base is capped at 63,000/month. Family allowances 7% × 63,000 = 4,410. Work injury (assume 1% risk category) 1% × 63,000 = 630. Total 4,410 + 630 = 5,040 ✓. 100% employer-borne. Matches pattern 3.2.

**Classification:** EXCLUDE — CSS contribution (employer cost). Flag work-injury category for reviewer confirmation.

### Example 4 -- IPM health contribution (BICIS)

**Input line:**
`30.06.2026 ; IPM COTISATION MALADIE ; DEBIT ; JUIN ; -15,000 ; XOF`

**Reasoning:**
[RESEARCH GAP — reviewer to confirm] Using PwC corporate-page figures: IPM 6% total split 3% employer / 3% employee on a base capped at 250,000. For an employee at/above the 250,000 ceiling: 6% × 250,000 = 15,000 (employer 3% × 250,000 = 7,500; employee 3% × 250,000 = 7,500; 7,500 + 7,500 = 15,000 ✓). Matches pattern 3.3. PwC's individual page describes IPM differently (2%–7.5% each) — do not finalise without confirming the fund's actual rate.

**Classification:** EXCLUDE — IPM health contribution. Flag IPM rate/ceiling for reviewer.

### Example 5 -- CFCE employer payroll tax (CBAO)

**Input line:**
`30.06.2026 ; CFCE CONTRIBUTION FORFAITAIRE ; DEBIT ; PAIE JUIN ; -150,000 ; XOF`

**Reasoning:**
CFCE is 3% of **total gross payroll with no ceiling** (PwC, employer-only). Monthly payroll 5,000,000 → 3% × 5,000,000 = 150,000 ✓. Matches pattern 3.4. Employer-only; never deducted from the employee.

**Classification:** EXCLUDE — CFCE employer payroll tax. Deductible business cost; not VAT-bearing.

### Example 6 -- DGID PAYE / IRPP withholding remittance (SGBS)

**Input line:**
`15.07.2026 ; DGID TRESOR PUBLIC ; DEBIT ; RAS IRPP JUIN ; -52,000 ; XOF`

**Reasoning:**
"DGID TRESOR PUBLIC" + "RAS IRPP" matches pattern 3.4. This is **monthly PAYE income tax withheld** from employees and remitted, NOT a social contribution. If the reference also bundled CFCE, request the payroll journal to split IRPP from CFCE. Do not classify as IPRES/CSS/IPM.

**Classification:** EXCLUDE — IRPP (PAYE) remittance to DGID. NOT a social contribution. Flag to split if CFCE is bundled.

### Example 7 -- IRPP annual liability computation (1 part)

**Input:** Annual taxable income 3,000,000; single, no dependants, 1 part. Gross income 3,750,000.

**Reasoning (CGI arts. 173, 174, 282):**
- 0–630,000 @ 0% = 0
- 630,001–1,500,000 @ 20% × 870,000 = 174,000
- 1,500,001–3,000,000 @ 30% × 1,500,000 = 450,000
- **Total IRPP = 0 + 174,000 + 450,000 = 624,000** ✓

1 part gives no reduction. TRIMF on gross 3,750,000 is 12,000 and is added on top; it is not a floor. With 2 parts, the reduction is 15% × 624,000 = 93,600, below the 200,000 minimum, so the minimum decides and IRPP is 424,000.

```oa-check
name: IRPP on 3,000,000, 2 parts, minimum reduction decides
inputs:
  base: 3000000
steps:
  - bands: 174000 + (base - 1500000) * 0.30
  - reduction: min(max(bands * 0.15, 200000), 650000)
  - tax: bands - reduction
expected:
  bands: 624000.00
  tax: 424000.00
```

**Classification:** IRPP due = 624,000 at 1 part, plus TRIMF 12,000.

## Section 5 -- Tier 1 rules

Apply exactly as written when inputs are clear.

### Rule 1 -- IPRES General applies to all employees

- **IPRES General rule** — IPRES General = 14% total (employer 8.4% / employee 5.6%) on monthly base capped at 432,000. Per-employee contribution = 14% × min(gross, 432,000).  _(PwC, reviewed 31 Mar 2026)_

### Rule 2 -- IPRES Cadre is ADDITIONAL and only for executives

- **IPRES Cadre rule** — The complementary cadre scheme = 6% total (employer 3.6% / employee 2.4%) on base capped at 1,296,000, due in addition to the General scheme, only for cadres (managers/executives). Non-cadres: General only.

### Rule 3 -- CSS is 100% employer-borne, base capped at 63,000

- **CSS rule** — Family allowances = 7%. Work injury = 1%, 3%, or 5% per CSS-assigned risk category. Both on base capped at 63,000/month. Never deduct CSS from the employee.  _(PwC)_

### Rule 4 -- IPM health insurance [RESEARCH GAP]

- **IPM rule** — [RESEARCH GAP — reviewer to confirm] Per PwC corporate page: 6% total split 3% employer / 3% employee on base 60,000–250,000. PwC individual page gives 2%–7.5% each. Fund-specific. Do not present as definitive.

### Rule 5 -- CFCE has NO ceiling

- **CFCE rule** — CFCE = 3% of total gross payroll, employer-only, no ceiling — applies to full payroll. It is an employer payroll tax, not a withholding from the employee.  _(PwC)_

### Rule 6 -- IRPP is progressive on whole income, then reduced for family parts

- **IRPP progressivity rule**: Tax is computed on the whole taxable income on the scale below. Income is not divided by parts. The tax is then reduced by the rate for the employee's parts, within a minimum and maximum, and capped at 43% of taxable income. Default to 1 part if parts are unknown.  _(CGI arts. 173, 174)_
- **Employment base rule**: Taxable pay is gross pay less a 30% abatement capped at 900,000 a year. The abatement stands in for compulsory pension contributions, so IPRES and other employee contributions are never deducted on top.  _(CGI arts. 168, 182)_

**IRPP annual scale**  _(CGI art. 173)_

| Annual taxable income (XOF) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 – 630,000 | 0% | 0 |
| 630,001 – 1,500,000 | 20% | 174,000 |
| 1,500,001 – 4,000,000 | 30% | 924,000 |
| 4,000,001 – 8,000,000 | 35% | 2,324,000 |
| 8,000,001 – 13,500,000 | 37% | 4,359,000 |
| 13,500,001 – 50,000,000 | 40% | 18,959,000 |
| Over 50,000,000 | 43% | — |

> **Cumulative check:** 174,000 + 30%×2,500,000 = 924,000 ✓; + 35%×4,000,000 = 2,324,000 ✓; + 37%×5,500,000 = 4,359,000 ✓; + 40%×36,500,000 = 18,959,000 ✓.

### Rule 7 -- TRIMF is separate; there is no minimum income tax

- **TRIMF rule**: The old "MPIT floor" is wrong. Arts. 173 and 174 set no minimum IRPP, and no higher-of test applies. The table below is TRIMF, a separate annual tax read from gross income and added on top of IRPP. It is doubled for a spouse without income (art. 276).  _(CGI arts. 275, 276, 282)_

**TRIMF annual table**  _(CGI art. 282)_

| Gross annual income (XOF) | TRIMF per year (XOF) |
| --- | --- |
| 0 – 599,999 | 900 |
| 600,000 – 999,999 | 3,600 |
| 1,000,000 – 1,999,999 | 4,800 |
| 2,000,000 – 6,999,999 | 12,000 |
| 7,000,000 – 11,999,999 | 18,000 |
| 12,000,000+ | 36,000 |

### Rule 8 -- PAYE is monthly

- **PAYE frequency rule**: Employers withhold IRPP and the employee shares of social contributions monthly on gross remuneration (including fringe benefits and bonuses) and remit to DGID/Trésor and the institutions. Salary withholding is paid in the first 15 days of the next month, or quarterly for real simplified and CGU employers and where monthly withholding is at most 20,000.  _(CGI art. 185)_

### Rule 9 -- Ceilings cap the BASE, not the contribution

- **Ceiling application rule** — Apply each scheme's monthly base ceiling before multiplying by the rate. A high salary does not raise IPRES/CSS/IPM contributions above the capped base; CFCE alone has no ceiling.

### Rule 10 -- Minimum wage (SMIG) for sanity-checks only

- **SMIG rule**: SMIG (general, non-agricultural) = 371 FCFA gross/hour since 1 July 2023; 237 FCFA/hour for agricultural work. CSS contributions are never on less than the SMIG. The old 150,000/month and 303.49/hour figures do not agree with this table. Decree not read.  _(CLEISS, table at 1 January 2026)_

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Cadre classification borderline

- **Cadre classification borderline** — Trigger: Employee's role could be cadre or non-cadre (e.g., senior technician, team lead). Issue: Cadre status adds the 6% complementary scheme. Misclassification under- or over-states IPRES. Action: Flag for reviewer; confirm against the collective agreement (convention collective) and IPRES registration.

### T2-2 -- CSS work-injury risk category

- **CSS work-injury risk category** — Trigger: Work-injury rate not on the CSS certificate. Issue: Rate is 1%, 3%, or 5% by activity risk; defaulting to 5% over-states cost. Action: Obtain the CSS registration; flag for reviewer.

### T2-3 -- IPM fund and rate

- **IPM fund and rate** — Trigger: IPM computation needed but fund unknown. [RESEARCH GAP] Issue: PwC individual vs corporate pages disagree (2–7.5% each vs 6% split 3/3); fund-specific. Action: Confirm the employer's actual IPM scheme rate/ceiling before finalising. Flag.

### T2-4 -- Family parts evidence

- **Family parts evidence**: Trigger: Employee has a spouse and/or dependent children. Issue: Parts schedule and the 5-part maximum are fixed by CGI art. 174; a spouse with no income adds a half part, and the employee loses it if the spouse's details are not given (art. 191). Action: Obtain evidence before applying parts above 1.

### T2-5 -- Expatriate / seconded staff

- **Expatriate / seconded staff** — Trigger: Foreign national or secondee. Issue: Totalisation agreements, residence, and which schemes apply may differ; PwC general rates may not capture exemptions. Action: Flag for reviewer; confirm residence and any social-security agreement.

### T2-6 -- Arrears / late regularisation

- **Arrears / late regularisation** — Trigger: Unpaid prior-period IRPP or contributions. Issue: 5% interest + 0.5%/month of delay (PwC). Penalties compound. Action: Do not estimate; obtain institution statements; escalate to an expert-comptable.  _(PwC)_

## Section 7 -- Excel working paper template

```
SENEGAL PAYROLL CONTRIBUTIONS -- WORKING PAPER
Employer: [name]            Employee: [name]
Month/Tax Year: [period]    Prepared: [date]

INPUT DATA
  Monthly gross remuneration:    XOF [____]
  Cadre (executive)?             [YES/NO]
  CSS work-injury risk rate:     [1% / 3% / 5%]  (from CSS cert)
  IPM fund / rate:               [____]  [RESEARCH GAP if unknown]
  Family parts:                  [____]  (default 1; flag if >1)
  Gross annual income:           XOF [____]
  Spouse without income?         [YES/NO]

SOCIAL CONTRIBUTIONS (apply ceilings to base BEFORE rate)
  IPRES General base (min gross,432,000): XOF [____]
    Employer 8.4%:               XOF [____]
    Employee 5.6%:               XOF [____]
  IPRES Cadre base (if cadre, min gross,1,296,000): XOF [____]
    Employer 3.6%:               XOF [____]
    Employee 2.4%:               XOF [____]
  CSS base (min gross, 63,000):  XOF [____]
    Family allowances 7% (emp.): XOF [____]
    Work injury [1/3/5]% (emp.): XOF [____]
  IPM base (min gross, 250,000): XOF [____]   [RESEARCH GAP]
    Employer 3%:                 XOF [____]
    Employee 3%:                 XOF [____]
  CFCE 3% of full gross (no cap, employer): XOF [____]

INCOME TAX (IRPP)
  Gross less abatement (30%, cap 900,000): XOF [____]
  Tax from the bands:            XOF [____]
  Family reduction (art. 174):   XOF [____]
  IRPP due (max 43% of taxable): XOF [____]
  TRIMF (art. 282, x2 if spouse without income): XOF [____]
  Monthly PAYE (retenue):        XOF [____]

TOTALS
  Total employee deductions:     XOF [____]
  Total employer cost:           XOF [____]
  Net pay to employee:           XOF [____]

REVIEWER FLAGS / RESEARCH GAPS
  [List here]
```

## Section 8 -- Bank statement reading guide

### How contribution debits appear on Senegalese bank statements

**CBAO / Attijariwafa, SGBS (Société Générale), Ecobank, BICIS, UBA, Bank of Africa:**
- References are usually in **French**: "IPRES", "COTISATION RETRAITE", "CSS", "CAISSE DE SECURITE SOCIALE", "IPM", "MALADIE", "CFCE", "DGID", "TRESOR PUBLIC", "RAS IRPP".
- Contribution debits are **outgoing (DEBIT)**, typically monthly, around mid-month for the prior month's payroll.
- IPRES, CSS, IPM are remitted to the **institutions**; IRPP (RAS) and CFCE go to **DGID / Trésor Public**.

**Key identification tips:**
1. Social contributions recur monthly with amounts tied to capped bases (IPRES base ≤ 432,000; cadre ≤ 1,296,000; CSS ≤ 63,000; IPM base ≤ 250,000) — CFCE alone scales with full payroll.
2. A debit to "DGID"/"TRESOR PUBLIC" may bundle IRPP and CFCE — request the payroll journal to split.
3. Do not confuse outbound IPRES contributions with inbound "PENSION IPRES" credits (benefits received).
4. TVA (VAT) debits are a separate obligation — never fold into payroll contributions.
5. Irregular lump sums referencing "REGULARISATION" or "ARRIERE" may include 0.5%/month + 5% interest — flag for reviewer.

## Section 9 -- Onboarding fallback

If only a bank statement is provided and no payroll detail:

1. **Scan for contribution debits** — identify outgoing payments matching Section 3 patterns (IPRES, CSS, IPM, CFCE, DGID/RAS).
2. **Group by institution** — IPRES (pension), CSS (family + injury), IPM (health), DGID (IRPP/CFCE).
3. **Reverse-check the bases:**
   - IPRES General debit ÷ 14% ⇒ implied base (capped at 432,000).
   - CSS debit ÷ (7% + injury%) ⇒ implied base (capped at 63,000).
   - CFCE debit ÷ 3% ⇒ implied total gross payroll (no cap).
4. **Flag for reviewer:** "Contribution classification derived from bank amounts only. Cadre status, CSS work-injury category, IPM fund/rate, and family parts are unverified. Reviewer must confirm before filing PAYE or the annual recapitulative returns."

## Section 10 -- Reference material

### Contribution quick-calc at common bases (2026, PwC reviewed 31 Mar 2026)

**Contribution quick-calc at common bases**  _(PwC reviewed 31 Mar 2026)_

| Scheme | Base used | Employer | Employee | Total |
| --- | --- | --- | --- | --- |
| IPRES General | 432,000 (ceiling) | 36,288 | 24,192 | 60,480 |
| IPRES Cadre | 1,296,000 (ceiling) | 46,656 | 31,104 | 77,760 |
| CSS family (7%) | 63,000 (ceiling) | 4,410 | 0 | 4,410 |
| CSS work injury (3%) | 63,000 (ceiling) | 1,890 | 0 | 1,890 |
| IPM (6%) [RESEARCH GAP] | 250,000 (ceiling) | 7,500 | 7,500 | 15,000 |
| CFCE (3%) | 1,000,000 payroll | 30,000 | 0 | 30,000 |

> **Check:** 8.4%×432,000=36,288; 5.6%×432,000=24,192; sum 60,480 ✓. 3.6%×1,296,000=46,656; 2.4%×1,296,000=31,104; sum 77,760 ✓. 7%×63,000=4,410 ✓. 3%×63,000=1,890 ✓. 3%×250,000=7,500 each, 15,000 ✓. 3%×1,000,000=30,000 ✓.

### Filing, forms & deadlines (PwC tax-administration pages, reviewed 31 Mar 2026)

**Filing, forms & deadlines**  _(PwC tax-administration pages, reviewed 31 Mar 2026)_

| Obligation | Deadline | Source |
| --- | --- | --- |
| Salary withholding (IRPP + TRIMF) and CFCE | First 15 days of the next month, or quarterly as in Rule 8 | CGI arts. 185, 268 |
| Employee social shares | Remitted to the institutions | PwC individual/tax-administration |
| Individual IRPP annual return | Before 1 May; compulsory for employees with several employers or other income (arts. 60, 196) | CGI |
| Annual salary statement | During January (art. 191) | CGI |
| Annual recapitulative return on service payments | 31 January | PwC corporate/tax-administration |
| Annual recapitulative return on rent payments | 31 January | PwC corporate/tax-administration |
| CIT return (context) | 30 April | PwC corporate/tax-administration |
| CIT instalments (context) | 15 Feb, 30 Apr, 15 Jun | PwC corporate/tax-administration |

### Penalties (PwC corporate/tax-administration, reviewed 31 Mar 2026)

**Penalties**  _(PwC corporate/tax-administration, reviewed 31 Mar 2026)_

| Penalty | Amount/rate |
| --- | --- |
| Late filing | XOF 200,000 (art. 667) |
| Late payment (spontaneous regularisation) | 5% interest + 0.5% per further month or part (art. 665) |
| Tax withheld or collected and not paid over | 50% (art. 671 III) |
| Failure to declare or pay | 25% (art. 671 I) |

### Test suite

**Test 1:** Non-cadre, gross 500,000 → IPRES General base capped 432,000. Total 14% × 432,000 = **60,480** (employer 36,288 / employee 24,192). ✓

**Test 2:** Cadre, gross 1,296,000 → cadre scheme 6% × 1,296,000 = **77,760** (employer 46,656 / employee 31,104), **plus** General 14% × 432,000 = 60,480 (billed separately). ✓

**Test 3:** CSS, gross 200,000, work-injury 1% → base capped 63,000. Family 7% × 63,000 = 4,410; injury 1% × 63,000 = 630; total **5,040** (employer-only). ✓

**Test 4:** CFCE, monthly payroll 5,000,000 → 3% × 5,000,000 = **150,000** (employer-only, no ceiling). ✓

**Test 5:** IPM [RESEARCH GAP], gross 300,000 → base capped 250,000. 6% × 250,000 = **15,000** (employer 7,500 / employee 7,500). Flag fund-specific rate. ✓

**Test 6:** IRPP, annual taxable 3,000,000, 1 part → 0 + 20%×870,000 + 30%×1,500,000 = 174,000 + 450,000 = **624,000**. TRIMF is added separately. ✓

**Test 7:** IRPP, annual taxable 500,000, 1 part → **0** (0% band). Gross 714,285 → TRIMF **3,600**, separate. ✓

**Test 8:** IRPP, annual taxable 8,000,000, 1 part → cumulative at 8,000,000 = **2,324,000** (per Rule 6 table). ✓

### Prohibitions

- NEVER apply the IPRES cadre complementary scheme to a non-cadre, or omit it for a confirmed cadre.
- NEVER deduct CSS or CFCE from the employee — both are 100% employer-borne.
- NEVER apply a scheme's rate to gross above its capped base (IPRES 432,000 / cadre 1,296,000 / CSS 63,000 / IPM 250,000).
- NEVER apply a ceiling to CFCE — it has none; it is 3% of full payroll.
- NEVER present IPM rate/ceiling as definitive — it is a flagged [RESEARCH GAP]; confirm the fund.
- NEVER divide income by parts; art. 174 is a reduction on the tax. NEVER apply parts above 1 without evidence, or above 5.
- NEVER deduct employee contributions from the IRPP base on top of the 30% abatement (art. 182).
- NEVER apply a minimum IRPP floor; the 900 to 36,000 table is TRIMF, added on top.
- NEVER treat a DGID/Trésor "RAS IRPP" debit as a social contribution — it is PAYE income tax.
- NEVER quote SMIG as the decree: the figure comes from the CLEISS table.
- NEVER estimate arrears/penalties without the institution's statement — escalate to an expert-comptable.
- NEVER present any figure as definitive — label as estimated, cite PwC, and direct to a Senegalese chartered accountant.

## Sources checked for the 1 November 2026 fix

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): arts. 60, 168, 173 to 199, 263 to 269, 275 to 282, 665 to 671 read in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-01 |
| CLEISS, Senegal contributions at 1 January 2026: table and notes read | https://www.cleiss.fr/docs/cotisations/senegal.html | 2026-11-01 |

Not yet confirmed: IPRES, CSS and IPM rates rest on CLEISS and PwC, because ipres.sn and secusociale.sn did not open; the health contribution includes a 2% AMO levy per CLEISS, and the split inside each IPM is not read; the cadre base (old text charges 6% on pay up to 1,296,000, while CLEISS says the base lies between 432,000 and 1,296,000); SMIG decree not read; filing dates for IPRES and CSS returns not read.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, expert-comptable, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
