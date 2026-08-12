---
name: cameroon-social-contributions
description: Use this skill whenever asked about Cameroon (CM) social security contributions (CNPS), payroll-linked levies, or personal income tax on salaries. Trigger on phrases like "CNPS contributions", "Cameroon social security", "how much CNPS do I pay", "pension vieillesse", "prestations familiales", "risques professionnels", "Cameroon payroll tax", "Crédit Foncier CFC", "Fonds National de l'Emploi FNE", "Cameroon PIT", "IRPP Cameroun", "centimes additionnels communaux CAC", "Cameroon PAYE", "Cameroon expat 183 days", or any question about Cameroon employer/employee contribution computation. Also trigger when classifying bank statement transactions that relate to CNPS debits, DGI/impôts payments, CFC or FNE remittances from Afriland, SGBC, BICEC, Ecobank, UBA Cameroon, or other Cameroonian banks. This skill covers CNPS pension/family/occupational-risk rates, the XAF 750,000 monthly ceiling, CFC and FNE payroll levies, the 10%/15%/25%/35% PIT scale (and the 11%/16.5%/27.5%/38.5% effective rates with the 10% CAC surcharge), local council/audiovisual levies, monthly remittance deadlines, registration, penalties, bank statement classification, and edge cases. ALWAYS read this skill before touching any Cameroon payroll or contribution work.
version: 0.1
jurisdiction: CM
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Nkinyam Courage Ndasi
review_status: current
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon Social Security Contributions (CNPS) & Payroll

## Cameroon Social Security Contributions (CNPS) & Payroll Skill v0.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Nkinyam Courage Ndasi** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### cameroon-social-contributions

- **Employee pension rate (vieillesse-invalidité-décès)** — 4.20%  _(CLEISS cotisations)_
- **Employer pension rate (vieillesse-invalidité-décès)** — 4.20%  _(CLEISS cotisations)_
- **Employer family allowances rate – general regime (prestations familiales)** — 7.00%  _(CLEISS)_
- **Employee family allowances rate** — 0%  _(CLEISS)_
- **Employer occupational risk rate – class 1 (minimum)** — 1.75%  _(CLEISS)_
- **Employer occupational risk rate – class 2 (mid)** — 2.50%  _(CLEISS)_
- **Employer occupational risk rate – class 3 (maximum)** — 5.00%  _(CLEISS)_
- **Employee occupational risk rate** — 0%  _(CLEISS)_
- **Total CNPS employer rate – minimum risk (1.75%)** — 12.95%  _(CLEISS; PwC)_
- **Total CNPS employer rate – mid risk (2.50%)** — 13.70%  _(CLEISS; PwC)_
- **Total CNPS employer rate – maximum risk (5.00%)** — 16.20%  _(CLEISS)_
- **Total employee social rate (CNPS only)** — 4.20%  _(CLEISS cotisations)_
- **Employer family allowances rate – agricultural regime** — 5.65%  _(CLEISS)_
- **Employer family allowances rate – private-education regime** — 3.70%  _(CLEISS)_
- **Voluntary insured (self-insured) pension contribution rate** — 8.40% of declared income  _(CLEISS)_
- **CNPS pension and family allowances contribution ceiling – monthly** — XAF 750,000/month  _(CLEISS)_
- **CNPS pension and family allowances contribution ceiling – annual** — XAF 9,000,000/year  _(CLEISS)_
- **Occupational-risk (risques professionnels) contribution base** — Full salary, no ceiling  _(CLEISS)_
- **Crédit Foncier du Cameroun (CFC) – employee rate** — 1.0% of taxable salary  _(PwC Other taxes)_
- **Crédit Foncier du Cameroun (CFC) – employer rate** — 1.5% of taxable salary  _(PwC Other taxes)_
- **Fonds National de l'Emploi (FNE) – employer rate** — 1.0% of taxable salary  _(PwC Other taxes)_
- **Fonds National de l'Emploi (FNE) – employee rate** — 0%  _(PwC Other taxes)_
- **Total employee social rate (CNPS pension + CFC)** — 5.20%  _(Computed)_
- **Total employer payroll levy rate (CNPS min risk + CFC + FNE)** — 15.45%  _(Computed)_
- **CNPS employee pension deduction from PIT base** — 4.20% of gross salary (capped at XAF 750,000/mo base)  _(MINFI / PwC)_
- **Monthly PAYE + CNPS remittance deadline** — 15th of the month following the salary month  _(MINFI / PwC)_
- **Tax year end** — 31 December  _(MINFI)_
- **Record retention period** — 10 years  _(PwC)_
- **Day-count threshold for tax domicile in Cameroon (foreign nationals)** — > 183 days in a calendar year  _(PwC)_
- **Tax consequence of exceeding 183-day threshold** — Tax-domiciled; taxed on worldwide income  _(PwC)_
- **Employee CNPS formula** — min(gross_salary, 750,000) × 4.20%  _(CLEISS)_
- **Employer CNPS formula** — min(gross, 750,000) × 4.20% + min(gross, 750,000) × FAM% + gross × RISK%  _(CLEISS; PwC)_
- **PIT taxable base formula** — gross − (gross × 4.20% CNPS) − (gross × 30% abatement) − XAF 500,000 standard deduction; round down to nearest 1,000  _(MINFI / PwC)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Cameroon |
| Currency | Central African CFA franc (XAF / FCFA) -- XAF only |
| Tax Authority | Direction Générale des Impôts (DGI), under MINFI |
| Social Security Authority | Caisse Nationale de Prévoyance Sociale (CNPS) |
| Primary Social Legislation | CNPS regime (pension, family allowances, occupational risks) [CLEISS regime page] |
| Primary Tax Legislation | Code Général des Impôts (CGI) / General Tax Code [MINFI] |
| Employee social rate | 4.20% (pension branch only) [CLEISS cotisations] |
| Employer social rate (CNPS) | 12.95%–15.20% depending on risk class [CLEISS; PwC] |
| Contribution ceiling (pension + family) | XAF 750,000/month (XAF 9,000,000/year) [CLEISS] |
| Occupational-risk base | Full salary, no ceiling [CLEISS] |
| Housing fund (CFC) | Employee 1.0% / Employer 1.5% of taxable salary [PwC Other taxes] |
| Employment fund (FNE) | Employer 1.0% of taxable salary [PwC Other taxes] |
| PIT base scale | 10% / 15% / 25% / 35% [MINFI] |
| PIT effective (incl. 10% CAC) | 11% / 16.5% / 27.5% / 38.5% [PwC] |
| PIT exemption threshold | Salaries ≥ XAF 62,000/month are taxed at source [MINFI] |
| Payment frequency | Monthly (PAYE + CNPS) |
| Monthly deadline | 15th of the month following the salary month [MINFI; PwC] |
| Minimum wage (SMIG, non-agricultural) | XAF 60,000/month [CLEISS; widely cited 2025/2026] |
| Tax year | Calendar year ending 31 December |
| Validated by | Verified by Nkinyam Courage Ndasi (3472800) on 2026-06-21 |
| Validation date | Verified by Nkinyam Courage Ndasi (3472800) on 2026-06-21 |

**CNPS branch overview (2025)**  _(CLEISS)_

| Branch | Employee | Employer | Ceiling |
| --- | --- | --- | --- |
| Old-age / invalidity / death pension (vieillesse-invalidité-décès) | 4.20% | 4.20% | XAF 750,000/mo [CLEISS] |
| Family allowances (prestations familiales), general regime | 0% | 7.00% | XAF 750,000/mo [CLEISS] |
| Occupational risks (risques professionnels) | 0% | 1.75% / 2.50% / 5.00% by risk class | full salary [CLEISS] |
| **CNPS totals (min risk 1.75%)** | **4.20%** | **12.95%** | mixed |
| **CNPS totals (max risk 5.00%)** | **4.20%** | **16.20%** | mixed |

*Arithmetic check (employer, min risk): 7.00 + 4.20 + 1.75 = 12.95%. (max risk): 7.00 + 4.20 + 5.00 = 16.20%.*

> Note: research notes cite an employer band of "~12.95%–15.20%". The 15.20% figure appears to combine 7% + 4.2% + 2.5% (mid risk) + 1.5% CFC, mixing CNPS and the housing fund. Computed CNPS-only employer totals are 12.95% (min), 13.70% (mid 2.50%), 16.20% (max 5.00%). [RESEARCH GAP — reviewer to confirm the exact employer band and how the 15.20% headline is composed.]

**Family-allowance rate variants (replace the 7.00% general regime) [CLEISS]**  _(CLEISS)_

| Regime | Family-allowance employer rate |
| --- | --- |
| General | 7.00% |
| Agricultural workers | 5.65% |
| Private-education staff | 3.70% |

**Other mandatory payroll levies (not CNPS)**  _(PwC Other taxes)_

| Levy | Employee | Employer | Source |
| --- | --- | --- | --- |
| Housing fund — Crédit Foncier du Cameroun (CFC) | 1.0% | 1.5% | PwC Other taxes |
| National Employment Fund (FNE) | 0% | 1.0% | PwC Other taxes |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown risk class | Apply minimum 1.75% occupational-risk rate; flag for reviewer |
| Unknown regime (general vs agricultural vs education) | Assume general regime (7% family allowance) |
| Salary above ceiling, ceiling treatment unclear | Cap pension + family base at XAF 750,000/mo; apply risk on full salary [CLEISS] |
| Unknown whether worker is salaried | Treat as salaried; do not apply minimum-tax/turnover rules |
| Unknown CAC applicability | Apply the 10% CAC surcharge (effective rates) and flag |
| Ambiguous DGI vs CNPS debit | Classify per reference; if unclear, flag for reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly taxable salary and whether the worker is salaried (employee) vs self-employed/voluntary insured. Without gross salary, STOP. Do not compute contributions.

**Recommended** -- the enterprise's CNPS occupational-risk classification (1.75% / 2.50% / 5.00%), the applicable family-allowance regime (general / agricultural / private-education), and the employee's CNPS registration status.

**Ideal** -- the employer's CNPS DIPE / récapitulatif, monthly DGI payroll returns, bank statements showing CNPS, DGI, CFC and FNE remittances, and residence/days-present information for any foreign national.

### Refusal catalogue

- **R-CM-SOC-1 -- Gross salary unknown** — Trigger: gross monthly taxable salary not provided. Message: "Gross monthly taxable salary is mandatory. CNPS and PIT both depend on it (with a XAF 750,000/month ceiling on the pension and family branches). Cannot proceed without it."
- **R-CM-SOC-2 -- Occupational-risk class unknown for a precise employer figure** — Trigger: a precise employer total is requested but the enterprise risk classification (1.75% / 2.50% / 5.00%) is unknown. Message: "Employer occupational-risk rate depends on the enterprise's CNPS risk classification. I will use the minimum 1.75% as a conservative default and flag it; the exact rate must be confirmed against the CNPS notification before filing."
- **R-CM-SOC-3 -- Self-employed / voluntary insured** — Trigger: the person is a voluntary/self-insured contributor rather than a salaried employee. Message: "Voluntary insured persons contribute 8.40% of declared income to the pension branch [CLEISS], but declared-income rules and eligibility require CNPS confirmation. Escalate to a Cameroon-qualified accountant."  _(CLEISS)_
- **R-CM-SOC-4 -- Penalty / arrears quantification** — Trigger: client has unpaid CNPS or PIT and asks for the arrears figure. Message: "Late payment carries a 10% penalty plus 1.5%/month interest (interest capped at 50% of principal) per secondary summaries [RESEARCH GAP — not verified against the CGI text]. Do not quantify arrears without official DGI/CNPS statements. Escalate to a Cameroon-qualified accountant."
- **R-CM-SOC-5 -- Expatriate residence determination** — Trigger: a foreign national's tax status is in question. Message: "A foreign national present > 183 days in a calendar year is tax-domiciled in Cameroon and taxed on worldwide income [PwC]. Day counts and treaty relief must be confirmed by a qualified accountant before applying payroll taxes."  _(PwC)_

## Section 3 -- Payment pattern library

Deterministic pre-classifier for bank statement transactions related to Cameroon payroll, social security, and tax. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference as it appears in the statement. CNPS, CFC, FNE, and PIT remittances are statutory obligations -- EXCLUDE them from any business revenue/expense or VAT (TVA) supply classification.

### 3.1 CNPS social security debits

**CNPS social security debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNPS, CAISSE NATIONALE DE PREVOYANCE | EXCLUDE -- CNPS remittance | Monthly social contributions |
| PREVOYANCE SOCIALE, COTISATION CNPS | EXCLUDE -- CNPS remittance | Same |
| PENSION, VIEILLESSE, INVALIDITE | EXCLUDE -- CNPS pension branch | Pension contribution |
| PRESTATIONS FAMILIALES, ALLOCATIONS FAMILIALES | EXCLUDE -- CNPS family branch | Family allowances |
| RISQUES PROFESSIONNELS, ACCIDENT TRAVAIL | EXCLUDE -- CNPS risk branch | Occupational risk |

### 3.2 DGI / income-tax and PAYE debits (NOT CNPS)

**DGI/PAYE debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, IMPOTS, DIRECTION GENERALE DES IMPOTS | EXCLUDE -- tax remittance, not CNPS | PIT/IRPP and other taxes |
| IRPP, IR SALAIRES, PRECOMPTE | EXCLUDE -- PIT withholding | PAYE on salaries |
| TVA, TAXE VALEUR AJOUTEE | EXCLUDE -- VAT remittance | Not a contribution |
| CAC, CENTIMES ADDITIONNELS | EXCLUDE -- council surcharge on PIT | Part of PIT effective rate |

### 3.3 Other mandatory payroll levies

**Other mandatory payroll levies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CFC, CREDIT FONCIER | EXCLUDE -- housing fund levy | 1% employee / 1.5% employer |
| FNE, FONDS NATIONAL EMPLOI | EXCLUDE -- employment fund levy | 1% employer |
| TAXE COMMUNALE, TAXE DEVELOPPEMENT LOCAL | EXCLUDE -- local council tax | Banded, up to XAF 2,520/mo |
| RAV, REDEVANCE AUDIOVISUELLE, CRTV | EXCLUDE -- audiovisual royalty | Banded, max XAF 13,000 |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE -- payroll expense | Net pay to employee; not a contribution |
| SALAIRE, PAIE (incoming) | EXCLUDE -- employment income received | Not a contribution |

### 3.5 Benefits received (not contributions)

**Benefits received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION CNPS, RENTE, PENSION VIEILLESSE (credit) | EXCLUDE -- pension income received | Benefit, not a contribution paid |
| ALLOCATION FAMILIALE (credit) | EXCLUDE -- family benefit received | Not a contribution |

## Section 4 -- Worked examples

Bank statement classifications and computations for a hypothetical Cameroonian employer (general regime, minimum 1.75% risk class) and its salaried staff. All figures in XAF.

### Example 1 -- Employee earning below the ceiling (XAF 300,000/mo)

**Input line:**
`15.02.2025 ; CNPS COTISATION JANVIER ; DEBIT ; PENSION SALARIE ; -12 600 ; XAF`

**Reasoning:**
Salary XAF 300,000 < XAF 750,000 ceiling, so the full salary is the pension/family base. Employee pension = 300,000 × 4.20% = **XAF 12,600**. The debit matches "CNPS COTISATION" (pattern 3.1). This is the employee pension share withheld and remitted.

Employer side (same month, same employee):
- Pension 4.20% × 300,000 = 12,600
- Family 7.00% × 300,000 = 21,000
- Risk 1.75% × 300,000 = 5,250
- CNPS employer subtotal = **XAF 38,850** (= 12.95% × 300,000) ✓
- CFC employer 1.5% × 300,000 = 4,500; FNE 1.0% × 300,000 = 3,000
- CFC employee 1.0% × 300,000 = 3,000

**Classification:** EXCLUDE from VAT/revenue -- CNPS statutory remittance.

### Example 2 -- Employee above the ceiling (XAF 1,200,000/mo)

**Input line:**
`15.04.2025 ; CNPS PREVOYANCE SOCIALE ; DEBIT ; PENSION PLAFONNE ; -31 500 ; XAF`

**Reasoning:**
Salary XAF 1,200,000 > XAF 750,000 ceiling. Pension and family branches are capped at the ceiling; the occupational-risk branch uses the full salary (no ceiling) [CLEISS].
- Employee pension = 750,000 × 4.20% = **XAF 31,500** (capped). ✓ matches the debit.
- Employer pension = 750,000 × 4.20% = 31,500
- Employer family = 750,000 × 7.00% = 52,500
- Employer risk = 1,200,000 × 1.75% = 21,000 (full salary)
- CNPS employer subtotal = 31,500 + 52,500 + 21,000 = **XAF 105,000**

**Classification:** EXCLUDE -- CNPS remittance (ceiling applied to pension/family, full salary for risk).

### Example 3 -- PIT (IRPP) withholding, not CNPS

**Input line:**
`15.03.2025 ; DGI IMPOTS IRPP SALAIRES ; DEBIT ; PRECOMPTE FEVRIER ; -45 000 ; XAF`

**Reasoning:**
Matches "DGI IMPOTS IRPP" (pattern 3.2). This is PIT withheld on salaries (PAYE), remitted to the DGI -- NOT a CNPS contribution. Exclude from VAT/revenue. Do not classify as social security.

**Classification:** EXCLUDE -- PIT (IRPP) remittance to DGI. NOT CNPS.

### Example 4 -- CFC housing-fund and FNE levies

**Input line:**
`15.05.2025 ; CREDIT FONCIER CFC + FNE ; DEBIT ; AVRIL 2025 ; -9 000 ; XAF`

**Reasoning:**
Matches "CREDIT FONCIER CFC" and "FNE" (pattern 3.3). For an employee on XAF 300,000:
- CFC employer 1.5% × 300,000 = 4,500
- FNE employer 1.0% × 300,000 = 3,000
- (CFC employee 1.0% × 300,000 = 3,000 is withheld separately, not in this XAF 9,000 employer remittance: 4,500 + 3,000 = 7,500; with the employee CFC 1,500 share rounding, see note.)

[RESEARCH GAP — reviewer to confirm whether CFC employee and employer shares are remitted together or separately on local returns; example amounts illustrate rate application only.]

**Classification:** EXCLUDE -- statutory payroll levies (housing fund + employment fund).

### Example 5 -- PIT computation on a XAF 500,000/mo salary (annualised)

**Reasoning (PIT base, per MINFI/PwC standard payroll computation):**
Gross annual salary = 500,000 × 12 = XAF 6,000,000.
- Less 4.20% CNPS employee (pension) deductible. Pension base capped at 750,000/mo > 500,000, so full salary: 6,000,000 × 4.20% = 252,000.
- Less 30% professional-expense abatement on salary [PwC]: 6,000,000 × 30% = 1,800,000.
- Less standard deduction XAF 500,000 [MINFI].

Net taxable income = 6,000,000 − 252,000 − 1,800,000 − 500,000 = **XAF 3,448,000**, rounded down to nearest thousand = XAF 3,448,000.

Apply base scale (10/15/25/35):
- 0 – 2,000,000 @ 10% = 200,000
- 2,000,001 – 3,000,000 @ 15% = 150,000 (cumulative 350,000)
- 3,000,001 – 3,448,000 @ 25% = 448,000 × 25% = 112,000

Base PIT = 200,000 + 150,000 + 112,000 = **XAF 462,000**.
With 10% CAC surcharge: 462,000 × 1.10 = **XAF 508,200** annual PIT (effective).

*Cross-check via effective rates (11/16.5/27.5): 2,000,000×11% = 220,000; 1,000,000×16.5% = 165,000; 448,000×27.5% = 123,200; total = 508,200. ✓*

**Classification:** Computation only -- PIT withheld monthly and remitted to DGI by the 15th of the following month.

### Example 6 -- Salary below the PIT exemption threshold

**Input line:**
`28.02.2025 ; VIREMENT SALAIRE ; DEBIT ; PAIE FEVRIER ; -55 000 ; XAF`

**Reasoning:**
Gross salary XAF 55,000/month < XAF 62,000/month exemption threshold [MINFI], so no PIT is deducted at source. CNPS pension (4.20% × 55,000 = XAF 2,310 employee) and employer branches still apply -- the exemption is PIT-only, not a contribution exemption. Note XAF 55,000 is below the XAF 60,000 SMIG; flag the underpayment for reviewer.

**Classification:** EXCLUDE -- net salary payment. No PIT; CNPS still due. Flag sub-SMIG wage.

## Section 5 -- Tier 1 rules

Apply exactly as written when data is clear and inputs are available.

### Rule 1 -- CNPS employee contribution

- **Employee CNPS formula** — Employee CNPS = min(gross_salary, 750,000) × 4.20%   [pension branch only]  _(CLEISS)_
- **Employee contribution scope** — Employees contribute to the pension branch only; family allowances and occupational risks are employer-borne  _(CLEISS)_

### Rule 2 -- CNPS employer contribution

- **Employer CNPS formula** — Employer CNPS = min(gross, 750,000) × 4.20%   (pension) + min(gross, 750,000) × FAM%     (family: 7.00% general / 5.65% agric / 3.70% educ) + gross × RISK%                   (risk: 1.75% / 2.50% / 5.00%, no ceiling)  _(CLEISS; PwC)_
- **General-regime minimum-risk employer total** — 12.95% (mixed base)  _(CLEISS; PwC)_

### Rule 3 -- The XAF 750,000/month ceiling

- **Ceiling rule** — Pension and family branches are capped at XAF 750,000/month (XAF 9,000,000/year). The occupational-risk branch is assessed on the full salary with no ceiling.  _(CLEISS)_

### Rule 4 -- CFC and FNE levies

- **CFC and FNE levy rule** — CFC (housing fund): employee 1.0% + employer 1.5% of taxable salary. FNE (employment fund): employer 1.0% of taxable salary. [RESEARCH GAP — reviewer to confirm whether the CFC/FNE base is itself capped; PwC states "taxable salary" without a stated cap.]  _(PwC Other taxes)_

### Rule 5 -- PIT scale (base vs effective)

Base statutory scale (MINFI): 10% / 15% / 25% / 35%. PwC effective rates include the 10% CAC surcharge: 11% / 16.5% / 27.5% / 38.5% (base × 1.10).

**PIT scale table**

| Net income (XAF) | Base rate | Effective (incl. CAC) | Cumulative base tax at top of band |
| --- | --- | --- | --- |
| 0 – 2,000,000 | 10% | 11% | 200,000 |
| 2,000,001 – 3,000,000 | 15% | 16.5% | 350,000 |
| 3,000,001 – 5,000,000 | 25% | 27.5% | 850,000 |
| Over 5,000,000 | 35% | 38.5% | — |

*Cumulative check: 2,000,000×10% = 200,000; +1,000,000×15% = 150,000 → 350,000; +2,000,000×25% = 500,000 → 850,000. ✓*

### Rule 6 -- PIT taxable base

- **PIT taxable base formula** — Net salary base = gross − 4.20% CNPS employee − 30% professional-expense abatement − XAF 500,000 standard deduction; round down to the nearest XAF 1,000  _(MINFI; PwC)_

### Rule 7 -- PIT exemption floor

- **PIT exemption floor rule** — Only salaries ≥ XAF 62,000/month are subject to PIT deduction at source; below this, exempt from PIT (not from CNPS)  _(MINFI)_

### Rule 8 -- Local payroll levies

- **Local development tax (taxe communale)** — up to XAF 2,520/month, banded, on salaries exceeding XAF 500,000  _(PwC)_
- **Audiovisual royalty (RAV/CRTV)** — banded, maximum XAF 13,000, for gross salaries above XAF 1,000,000  _(PwC)_

### Rule 9 -- Monthly remittance

- **Monthly remittance rule** — PIT and CNPS for a salary month are remitted (and the monthly return filed) by the 15th of the following month  _(MINFI; PwC)_

### Rule 10 -- Registration

- **Registration rule** — Employers must register with CNPS and obtain an employer number; employees are registered as *assurés obligatoires*. Registration is mandatory from the first employee — no de-minimis headcount threshold found. [RESEARCH GAP — no numeric registration threshold confirmed.]  _(CNPS)_

### Rule 11 -- Voluntary insured persons

- **Voluntary insured contribution rule** — Voluntary/self-insured contributors pay 8.40% of declared income to the pension branch. This is outside standard salaried payroll — see Refusal R-CM-SOC-3.  _(CLEISS)_

### Rule 12 -- Non-salary income rates

- **Non-salary income rates rule** — Income from stocks and shares is taxed at an overall 16.5%; other (non-salary) activity income at 33%. These are out of scope for the salaried-payroll path but noted for classification.  _(PwC)_

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Occupational-risk classification

- **T2-1** — Trigger: the enterprise risk rate (1.75% / 2.50% / 5.00%) is not on file. Issue: employer total swings materially with the risk class. Action: apply 1.75% as a conservative default; flag for reviewer to confirm against the CNPS notification.

### T2-2 -- Special family-allowance regime

- **T2-2** — Trigger: employer is agricultural or a private-education establishment. Issue: family-allowance rate is 5.65% (agric) or 3.70% (educ), not 7% [CLEISS]. Action: flag; confirm the regime before computing employer cost.  _(CLEISS)_

### T2-3 -- CAC surcharge applicability

- **T2-3** — Trigger: uncertainty whether the 10% CAC applies to a given PIT computation. Issue: the CAC mechanism is reconciled from MINFI base rates vs PwC effective rates, not stated verbatim on a single official page [RESEARCH GAP]. Action: apply the effective (11/16.5/27.5/38.5) rates by default; flag for reviewer to confirm CAC treatment.

### T2-4 -- Expatriate / 183-day residence

- **T2-4** — Trigger: a foreign national whose day count is near 183. Issue: > 183 days → tax-domiciled, worldwide-income taxation [PwC]. Action: flag; confirm residence and treaty relief with a qualified accountant.  _(PwC)_

### T2-5 -- Salary above the ceiling

- **T2-5** — Trigger: salary > XAF 750,000/month. Issue: pension/family capped at the ceiling; risk on full salary. Some EOR guides incorrectly cap all branches [RESEARCH GAP — CLEISS treated as authoritative]. Action: apply CLEISS treatment (full salary for risk); flag if a source disagrees.

### T2-6 -- Arrears / penalties

- **T2-6** — Trigger: unpaid CNPS or PIT. Issue: 10% penalty + 1.5%/month interest (capped at 50% of principal); filing penalties 10%/month capped at 30%; understatement 30%/100%/150% [secondary sources only — RESEARCH GAP]. Action: do not quantify without official statements. Escalate to a qualified accountant.

### T2-7 -- Sub-SMIG wages

- **T2-7** — Trigger: gross salary < XAF 60,000/month (non-agricultural). Issue: below the headline SMIG [CLEISS; widely cited]. Action: flag the underpayment; confirm the current decree (SMIG confirmed to 2023, cited as current — [RESEARCH GAP]).  _(CLEISS)_

## Section 7 -- Excel working paper template

```
CAMEROON PAYROLL / CNPS COMPUTATION -- WORKING PAPER
Client/Employer: [name]            CNPS employer no: [____]
Tax Year: [year]                   Prepared: [date]

INPUT DATA
  Employee name:                   [____]
  Gross monthly salary (XAF):      [____]
  Risk class (1.75/2.50/5.00%):    [____]
  Family regime (gen/agric/educ):  [____]
  Resident / >183 days:            [YES/NO]

CONTRIBUTION BASES
  Pension/family base (min(gross,750,000)):  XAF [____]
  Risk base (full gross):                    XAF [____]

EMPLOYEE CONTRIBUTIONS
  Pension 4.20% × capped base:     XAF [____]
  CFC 1.00% × taxable salary:      XAF [____]
  Employee total:                  XAF [____]

EMPLOYER CONTRIBUTIONS
  Pension 4.20% × capped base:     XAF [____]
  Family [7.00/5.65/3.70]% × capped base: XAF [____]
  Risk [1.75/2.50/5.00]% × full salary:   XAF [____]
  CFC 1.50% × taxable salary:      XAF [____]
  FNE 1.00% × taxable salary:      XAF [____]
  Employer total:                  XAF [____]

PIT (IRPP) COMPUTATION (if gross ≥ 62,000/mo)
  Annual gross:                    XAF [____]
  Less CNPS 4.20% (deductible):    XAF [____]
  Less 30% professional abatement: XAF [____]
  Less standard deduction 500,000: XAF [____]
  Net taxable (round down 1,000):  XAF [____]
  Base PIT (10/15/25/35 scale):    XAF [____]
  + 10% CAC surcharge:             XAF [____]
  PIT effective (annual):          XAF [____]
  PIT per month:                   XAF [____]

LOCAL LEVIES (banded)
  Taxe communale (≤2,520/mo):      XAF [____]
  RAV/CRTV (≤13,000):              XAF [____]

REMITTANCE
  Due by 15th of following month.

REVIEWER FLAGS / DEFAULTS APPLIED
  [List Tier 2 flags + RESEARCH GAPs here]
```

## Section 8 -- Bank statement reading guide

### How payroll debits appear on Cameroonian bank statements

Common banks: Afriland First Bank, SGBC (Société Générale Cameroun), BICEC, Ecobank Cameroun, UBA Cameroun, Commercial Bank of Cameroon.

**CNPS remittances:**
- Description: "CNPS", "CAISSE NATIONALE DE PREVOYANCE", "COTISATION CNPS", "PREVOYANCE SOCIALE"
- Timing: monthly, around or before the 15th of the following month
- Amount: employee 4.20% (pension) + employer branches; large employers remit a consolidated figure

**DGI / tax remittances:**
- Description: "DGI", "IMPOTS", "IRPP", "PRECOMPTE", "TVA"
- Timing: monthly, by the 15th
- These are tax, NOT CNPS — do not classify as social security

**CFC / FNE levies:**
- Description: "CREDIT FONCIER", "CFC", "FNE", "FONDS NATIONAL EMPLOI"

**Key identification tips:**
1. CNPS/DGI/CFC/FNE debits are outgoing (DEBIT), never credits.
2. They recur monthly with amounts proportional to the payroll.
3. Do not confuse CNPS (social security) with DGI/IRPP (income tax) — both are statutory but separate.
4. Inbound CNPS credits are benefits received (pension, family allowance), not contributions paid.
5. Amounts are in XAF (FCFA); no decimal sub-unit is used in practice.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for CNPS debits** — identify outgoing payments matching Section 3.1.
2. **Separate CNPS from DGI/CFC/FNE** — use the reference text per Sections 3.2–3.3.
3. **Reverse-engineer the salary base where possible:**
   - Employee pension debit ÷ 4.20% ≈ capped salary base (max XAF 750,000).
   - If the implied base hits XAF 750,000 exactly, salary is at or above the ceiling.
4. **Flag for reviewer:** "Contribution classification derived from bank statement amounts only. Risk class, family regime, and residence status have not been verified. Reviewer must confirm before filing CNPS/DGI returns."

## Section 10 -- Reference material

**Section 10 heading**

### Contribution summary (2025, general regime)

**Contribution summary (2025, general regime)**  _(CLEISS / PwC / computed)_

| Item | Employee | Employer (min risk) | Base | Source |
| --- | --- | --- | --- | --- |
| Pension | 4.20% | 4.20% | min(gross, 750,000) | CLEISS |
| Family allowances | 0% | 7.00% | min(gross, 750,000) | CLEISS |
| Occupational risks | 0% | 1.75% / 2.50% / 5.00% | full gross | CLEISS |
| CFC (housing) | 1.00% | 1.50% | taxable salary | PwC |
| FNE (employment) | 0% | 1.00% | taxable salary | PwC |
| **Social total (min risk)** | **5.20%** | **15.45%** | mixed | computed |

*Arithmetic check: employee 4.20 + 1.00 (CFC) = 5.20%. Employer 4.20 + 7.00 + 1.75 + 1.50 + 1.00 = 15.45%.* ✓

### PIT scale (2025)

**PIT scale (2025)**  _(MINFI / PwC)_

| Net income (XAF) | Base rate | Effective (incl. 10% CAC) | Source |
| --- | --- | --- | --- |
| 0 – 2,000,000 | 10% | 11% | MINFI / PwC |
| 2,000,001 – 3,000,000 | 15% | 16.5% | MINFI / PwC |
| 3,000,001 – 5,000,000 | 25% | 27.5% | MINFI / PwC |
| Over 5,000,000 | 35% | 38.5% | MINFI / PwC |

- **PIT deductions** — PIT deductions: 4.20% CNPS, 30% professional abatement, XAF 500,000 standard deduction.  _(MINFI/PwC)_
- **PIT exemption threshold** — Exemption: salaries < XAF 62,000/mo  _(MINFI)_
- **Other income rates** — Stocks/shares income 16.5%; other activity income 33%  _(PwC)_

### Thresholds and figures

**Thresholds and figures**  _(CLEISS / MINFI / PwC)_

| Item | Value | Source |
| --- | --- | --- |
| Pension/family ceiling | XAF 750,000/mo (9,000,000/yr) | CLEISS |
| PIT exemption floor | XAF 62,000/mo | MINFI |
| Standard deduction | XAF 500,000 | MINFI |
| Professional abatement | 30% | PwC |
| SMIG (non-agricultural) | XAF 60,000/mo | CLEISS (confirmed 2023, cited current) |
| SMIG (agricultural) | XAF 45,000/mo | CLEISS |
| Taxe communale max | XAF 2,520/mo (salary > 500,000) | PwC |
| RAV/CRTV max | XAF 13,000 (gross > 1,000,000) | PwC |
| Voluntary insured rate | 8.40% of declared income | CLEISS |
| Record retention | 10 years | PwC |

### Filing deadlines

**Filing deadlines**  _(MINFI / PwC)_

| Filing | Deadline | Source |
| --- | --- | --- |
| Monthly PAYE + CNPS | 15th of following month | MINFI / PwC |
| Employer annual income summary (DIPE / récapitulatif) | 15 March | PwC |
| Annual individual declaration — public/semi-public & seniors | 31 July | PwC |
| Annual individual declaration — private under Large Taxpayers' Unit | 30 September | PwC |
| Annual individual declaration — other individuals | 31 October | PwC |
| Annual adjustment — Large Taxpayers' Unit | 15 March | PwC |
| Annual adjustment — Medium & Specialized Tax Centres | 15 April | PwC |
| Annual adjustment — Divisional Tax Centres | 15 May | PwC |

### Penalties

[RESEARCH GAP — from secondary summaries (TaxesForExpats, Lloyds Bank Trade, Hallelaw 2025), not verified against the CGI text or PwC. Internally consistent; verify before relying on exact figures.]

**Penalties**

| Breach | Penalty |
| --- | --- |
| Late payment | 10% + 1.5%/month interest (interest capped at 50% of principal) |
| Failure to file / late declaration | 10%/month, capped at 30% |
| Insufficient declaration (good faith) | 30% |
| Bad faith | 100% |
| Fraud | 150% |

### Residence / expat

- **183-day residence test** — Foreign national present > 183 days in a calendar year → tax-domiciled  _(PwC)_
- **Worldwide income taxation** — Persons fiscally domiciled in Cameroon are, in principle, taxed on worldwide income  _(PwC)_

### Test suite

**Test 1:** Salary XAF 300,000/mo, general regime, min risk. → Employee pension 300,000 × 4.20% = **XAF 12,600**. Employer CNPS 300,000 × 12.95% = **XAF 38,850**.

**Test 2:** Salary XAF 750,000/mo (exactly the ceiling), min risk. → Employee pension 750,000 × 4.20% = **XAF 31,500**. Employer CNPS = 750,000 × 12.95% = **XAF 97,125** (all branches on 750,000 since risk base = full salary = ceiling here).

**Test 3:** Salary XAF 1,200,000/mo, min risk. → Employee pension capped: 750,000 × 4.20% = **XAF 31,500**. Employer = pension 31,500 + family 52,500 + risk (1,200,000 × 1.75% = 21,000) = **XAF 105,000**.

**Test 4:** Salary XAF 55,000/mo. → Below XAF 62,000 PIT floor → **no PIT**. CNPS pension employee 55,000 × 4.20% = **XAF 2,310** still due. Below SMIG — flag.

**Test 5:** Annual salary XAF 6,000,000 PIT base. → Net taxable = 6,000,000 − 252,000 − 1,800,000 − 500,000 = **XAF 3,448,000**. Base PIT = 200,000 + 150,000 + (448,000 × 25% = 112,000) = **XAF 462,000**. Effective (incl. CAC) = **XAF 508,200**.

**Test 6:** Net taxable income XAF 5,000,000 (top of 25% band). → Base PIT = 850,000. Effective = 850,000 × 1.10 = **XAF 935,000**.

**Test 7:** Net taxable income XAF 8,000,000. → Base = 850,000 + (3,000,000 × 35% = 1,050,000) = **XAF 1,900,000**. Effective = 1,900,000 × 1.10 = **XAF 2,090,000**.

**Test 8:** Agricultural employer, salary XAF 400,000/mo, min risk. → Employer = pension 16,800 + family (400,000 × 5.65% = 22,600) + risk (400,000 × 1.75% = 7,000) = **XAF 46,400**.

### Prohibitions

- **Never compute without gross salary** — NEVER compute contributions without the gross monthly salary.
- **Never apply ceiling to occupational risk** — NEVER apply the XAF 750,000 ceiling to the occupational-risk branch — risk is on full salary  _(CLEISS)_
- **Never omit family-allowance branch** — NEVER omit the employer family-allowance branch (7% general) — it is the largest single employer cost.
- **Never conflate CNPS and DGI/IRPP** — NEVER conflate CNPS (social security) with DGI/IRPP (income tax) — separate obligations, separate authorities.
- **Never apply PIT below floor / never treat as CNPS exemption** — NEVER apply PIT below the XAF 62,000/month floor; but NEVER treat that floor as a CNPS exemption.
- **Never quote penalty figures as definitive** — NEVER quote penalty figures as definitive — they are unverified secondary sources [RESEARCH GAP].
- **Never assume 7% family rate for agricultural/education** — NEVER assume the 7% family rate for agricultural or private-education employers.
- **Never present figures as definitive** — NEVER present contribution or PIT figures as definitive — label as estimated and direct the client to official CNPS/DGI statements.
- **Never quantify arrears/penalties without official statements** — NEVER quantify arrears or penalties without official statements — escalate to a Cameroon-qualified accountant.
- **Never assume non-residence without confirming 183-day count** — NEVER assume a foreign national is non-resident without confirming the 183-day count.

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
