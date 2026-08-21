---
name: senegal-payroll
description: Use this skill whenever asked about Senegal payroll processing for employed persons. Trigger on phrases like "Senegal payroll", "Sénégal paie", "IRPP Senegal", "retenue à la source Senegal", "TRIMF", "IPRES contribution", "CSS Senegal", "prestations familiales", "CFCE", "IPM health Senegal", "quotient familial Senegal", "parts fiscales", "net salary Senegal", "salaire net Sénégal", "PAYE Senegal", "employer social charges Senegal", "SMIG Senegal", "minimum wage Senegal", "form F4 Senegal", "gross to net Senegal", "bulletin de paie", or any question about computing employee pay, income tax withholding, or social contributions for Senegal-based employees. Senegal DOES levy personal income tax (IRPP) on salaries plus a fixed local salary tax (TRIMF). This skill covers progressive IRPP withholding with family-quotient splitting, TRIMF, IPRES pensions, CSS family allowances and work-injury, IPM health cover, the employer payroll tax (CFCE), minimum wage, filing obligations, and penalties. ALWAYS read this skill before processing any Senegal payroll.
version: 0.1
jurisdiction: SN
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Senegal Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

> Senegal is **not** a no-income-tax jurisdiction. Salaries bear progressive personal income tax (IRPP) withheld at source, a separate fixed local salary tax (TRIMF), mandatory social contributions (IPRES, CSS, IPM), and an employer-only payroll tax (CFCE). All five must be handled together.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Senegal (République du Sénégal) |
| Currency | West African CFA franc — XOF / FCFA only |
| Standard pay frequency | Monthly (mensuel) |
| Tax year | Calendar year (1 January — 31 December) — PwC, Senegal Tax Administration |
| Income tax system | IRPP — progressive, withheld at source (retenue à la source) with family-quotient (parts) splitting — CGI Art. 173 |
| Fixed local salary tax | TRIMF (Taxe Représentative de l'Impôt du Minimum Fiscal) — CGI |
| Tax authority | Direction Générale des Impôts et des Domaines (DGID) |
| Pension body | IPRES (Institution de Prévoyance Retraite du Sénégal) |
| Family allowance / work injury body | Caisse de Sécurité Sociale (CSS) |
| Health body | IPM (Institution de Prévoyance Maladie) — employer-level institution |
| Employer payroll tax | CFCE — Contribution Forfaitaire à la Charge de l'Employeur, 3% of payroll |
| Monthly remittance form | F4 (practitioner-cited) — declared/remitted before the 15th of the following month |
| Validated by | Pending — requires sign-off by a Senegalese chartered accountant (expert-comptable) |
| Skill version | 0.1 |

## Section 2 — Income Tax Withholding (IRPP)

The employer withholds IRPP monthly at source on gross remuneration (including fringe benefits and bonuses). The annual schedule is progressive and is applied **per family part** under the quotient-familial (income-splitting) mechanism.

### 2.1 Professional / employment deduction

- **Professional (employment) deduction** — 30% of gross employment income  _(Multiple payroll guides; confirm CGI)_
- **Annual cap on the deduction** — 1,800,000 XOF/year (= 150,000 XOF/month)  _(Rivermate Senegal tax guide — confirm CGI)_
- **Application order** — The deduction is applied to gross employment income before the progressive scale.

[RESEARCH GAP — reviewer to confirm] Whether mandatory social contributions (IPRES employee share, IPM employee share) are also deductible from the IRPP base, and the exact ordering of deductions, must be confirmed against CGI Art. 173 and the salary-withholding rules. The worked examples below compute IRPP on (gross − professional deduction) only, and flag this gap.

### 2.2 Progressive IRPP scale (annual taxable income, per part, XOF)

**Progressive IRPP scale**  _(Source: PwC Tax Summaries — Senegal, Taxes on personal income (last reviewed 31 March 2026). https://taxsummaries.pwc.com/senegal/individual/taxes-on-personal-income)_

| Annual taxable income per part (XOF) | Marginal rate | Cumulative tax at top of band (XOF) |
| --- | --- | --- |
| 0 – 630,000 | 0% | 0 |
| 630,001 – 1,500,000 | 20% | 174,000 |
| 1,500,001 – 4,000,000 | 30% | 924,000 |
| 4,000,001 – 8,000,000 | 35% | 2,324,000 |
| 8,000,001 – 13,500,000 | 37% | 4,359,000 |
| 13,500,001 – 50,000,000 | 40% | 18,959,000 |
| 50,000,001 + | 43% | — |

**Cumulative-tax arithmetic check (recomputed):**
- 630,000 → 0
- 1,500,000 → 0 + (1,500,000 − 630,000) × 20% = 174,000 ✓
- 4,000,000 → 174,000 + (4,000,000 − 1,500,000) × 30% = 174,000 + 750,000 = 924,000 ✓
- 8,000,000 → 924,000 + (8,000,000 − 4,000,000) × 35% = 924,000 + 1,400,000 = 2,324,000 ✓
- 13,500,000 → 2,324,000 + (13,500,000 − 8,000,000) × 37% = 2,324,000 + 2,035,000 = 4,359,000 ✓
- 50,000,000 → 4,359,000 + (50,000,000 − 13,500,000) × 40% = 4,359,000 + 14,600,000 = 18,959,000 ✓

> [RESEARCH GAP — reviewer to confirm] Secondary French payroll sources render the middle of the scale as a 25% band (1,500,001–4,000,000) plus a 30% band (4,000,001–8,000,000) — a 6-rate scale topping at 40%/43%. PwC merges these into a single 30% band on 1,500,001–4,000,000 (used above). The authoritative arbiter is the CGI Art. 173. Confirm the middle bands against the CGI text (official PDF via eRegulations: https://senegal.eregulations.org/media/t-code-general-impots[1].pdf) before publishing computations that fall in the 1.5M–8M range.

### 2.3 Family quotient (quotient familial / parts)

**Family quotient**  _(Source: PwC Tax Summaries — Senegal (confirms the splitting mechanism). https://taxsummaries.pwc.com/senegal/individual/taxes-on-personal-income)_

| Situation | Parts (standard pattern) |
| --- | --- |
| Single, no dependants | 1 |
| Married | 1.5 |
| Each dependent child | +0.5 |

Income is split into "parts" by family situation; each part is taxed through the progressive scale, then recombined (income splitting). Standard pattern:

> [RESEARCH GAP — reviewer to confirm] The exact part counts and the statutory maximum number of parts must be taken from the CGI. The pattern above is the commonly reported one; do not finalise part counts (especially the cap) without CGI confirmation.

### 2.4 Minimum Personal Income Tax (MPIT) floor

**MPIT floor**  _(Source: PwC Tax Summaries — Senegal. https://taxsummaries.pwc.com/senegal/individual/taxes-on-personal-income)_

| Annual income | MPIT floor (XOF) |
| --- | --- |
| Under 600,000 | 900 |
| ≥ 12,000,000 | 36,000 |

A floor applies to the IRPP computed above.

> [RESEARCH GAP — reviewer to confirm] The intermediate MPIT bands between 900 XOF and 36,000 XOF were not obtainable verbatim from an authoritative page; pull the full MPIT scale from the CGI.

## Section 3 — TRIMF (Taxe Représentative de l'Impôt du Minimum Fiscal)

A separate fixed monthly local salary tax, withheld at source by the employer and remitted to DGID. It is distinct from IRPP and from the MPIT floor; it funds local communities. Due by every individual resident in Senegal receiving salary or pension.

**TRIMF summary**

| Item | Value | Source |
| --- | --- | --- |
| Range | From 900 FCFA/month (lowest incomes) to 36,000 FCFA/month (highest), by gross-income bracket | UFE / payroll-practitioner summaries |
| Parts | 1 part employee + 1 part non-working spouse (bracket amount × parts) | Payroll-practitioner summary (La Paie Sénégalaise) |
| Mechanism | Withheld at source, remitted to DGID with the monthly salary withholding | Payroll-practitioner summary |

> [RESEARCH GAP — reviewer to confirm] The exact TRIMF bracket-by-bracket schedule (income band → fixed amount) is set in the CGI and was not obtainable verbatim from an authoritative page. Pull the full band table from the CGI text before publishing precise per-employee TRIMF amounts. The worked examples below use only the documented 900-floor / 36,000-cap endpoints and flag any intermediate value as a gap.

## Section 4 — Social Contributions — IPRES (Pensions)

Both PwC and CLEISS (the French official social-security liaison body) agree; the CLEISS table is effective 1 January 2026.

### 4.1 Régime Général (all employees)

**Régime Général**  _(PwC Tax Summaries — Senegal, Other taxes (https://taxsummaries.pwc.com/senegal/corporate/other-taxes) · CLEISS (https://www.cleiss.fr/docs/cotisations/senegal.html))_

| Party | Rate | Monthly ceiling (XOF) |
| --- | --- | --- |
| Employee | 5.6% | 432,000 |
| Employer | 8.4% | 432,000 |
| **Total** | **14.0%** | 432,000 |

Check: 5.6% + 8.4% = 14.0% ✓. Annual ceiling ≈ 432,000 × 12 = 5,184,000 XOF.

### 4.2 Régime Complémentaire des Cadres (executives / cadres only)

**Régime Complémentaire des Cadres**  _(PwC Tax Summaries — Senegal, Other taxes (https://taxsummaries.pwc.com/senegal/corporate/other-taxes) · CLEISS (https://www.cleiss.fr/docs/cotisations/senegal.html))_

| Party | Rate | Monthly ceiling (XOF) |
| --- | --- | --- |
| Employee | 2.4% | 1,296,000 |
| Employer | 3.6% | 1,296,000 |
| **Total** | **6.0%** | 1,296,000 |

Check: 2.4% + 3.6% = 6.0% ✓.

## Section 5 — Social Contributions — CSS (Family Allowances + Work Injury) — Employer Only

**CSS branches**  _(PwC (https://taxsummaries.pwc.com/senegal/corporate/other-taxes) · CLEISS (https://www.cleiss.fr/docs/cotisations/senegal.html))_

| Branch | Rate | Party | Monthly ceiling (XOF) | Source |
| --- | --- | --- | --- | --- |
| Family allowances (prestations familiales) | 7% | Employer only | 63,000 | PwC; CLEISS |
| Work injury / occupational disease (accidents du travail / maladies professionnelles) | 1%, 3% or 5% (by risk class) | Employer only | 63,000 | PwC; CLEISS |

- **Common ceiling and risk class** — Both CSS branches are capped at the same 63,000 XOF/month base. The work-injury rate depends on the employer's assessed risk class — confirm the specific rate with CSS for the employer in question.  _(PwC; CLEISS)_

## Section 6 — Health — IPM (Institution de Prévoyance Maladie)

**IPM contribution details**

| Item | Value | Source |
| --- | --- | --- |
| Total contribution (PwC "employment medical coverage") | 6% total, split equally employer/employee (3% / 3%) | PwC |
| Contribution base | Between 60,000 and 250,000 XOF/month | PwC |
| Branch rate range (CLEISS) | Between 2% and 7.5% | CLEISS |
| Ceiling (CLEISS) | 250,000 XOF/month | CLEISS |
| Practitioner-cited caps | Employer up to ~30,000 XOF/month; employee ~10,000 XOF/month (varies by IPM) | Practitioner guides |

Mandatory employer-sponsored health cover via an IPM.

Check: 3% employer + 3% employee = 6.0% total ✓ (PwC split).

> [RESEARCH GAP — reviewer to confirm] PwC (6% on a 60,000–250,000 base) and CLEISS (2%–7.5%, 250,000 ceiling) describe the same branch differently. The exact rate, base and caps are set by the specific IPM the employer is affiliated to. Confirm the IPM's own rules before computing IPM deductions for a given employer.

Sources: PwC (https://taxsummaries.pwc.com/senegal/corporate/other-taxes) · CLEISS (https://www.cleiss.fr/docs/cotisations/senegal.html).

## Section 7 — CFCE (Employer Payroll Tax)

**CFCE details**

| Item | Value | Source |
| --- | --- | --- |
| Rate | 3% of total gross payroll (salaries, indemnities, emoluments, benefits in kind) | Sénégal Services / DGID; PwC |
| Party | Employer only | Sénégal Services / DGID |
| Monthly payment deadline | By the 15th of the following month (same return/conditions as salary withholding) | Sénégal Services / DGID |
| Annual summary declaration | Before 31 December each year | Sénégal Services / DGID démarche |

Contribution Forfaitaire à la Charge de l'Employeur — an employer-only payroll tax.

> [RESEARCH GAP — reviewer to confirm] An "expatriate differential" (3% local vs 6% expatriate CFCE) is sometimes cited but could not be confirmed from any authoritative source. Treat CFCE as a flat 3% for all employees unless the CGI states otherwise; do not publish a 6% expat figure without CGI confirmation.

Sources: Sénégal Services (https://senegalservices.sn/demarche/sacquitter-de-limposition-a-la-contribution-forfaitaire-a-la-charge-des-employeurs-cfce) · PwC (https://taxsummaries.pwc.com/senegal/corporate/other-taxes). (The official DGID CFCE page could not be fetched due to a TLS certificate error; corroborated via the government Sénégal Services mirror.)

## Section 8 — Conservative Defaults

**Conservative defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Family situation / parts | Treat as **1 part (single, no dependants)** | Higher effective IRPP — never grant unverified parts. CGI part cap unconfirmed [RESEARCH GAP] |
| Cadre vs non-cadre | Treat as **non-cadre** (Régime Général only) | Do not assume the complementary executive scheme applies without confirmation |
| Work-injury risk class | Use the **highest cited rate, 5%** | Avoids understating employer cost — confirm actual class with CSS |
| IPM rate | Flag as **[RESEARCH GAP]**, do not compute a number | Rate is IPM-specific; refuse a definitive figure |
| Deductibility of social contributions from IRPP base | Compute IRPP on (gross − professional deduction) only; flag the gap | Ordering unconfirmed [RESEARCH GAP] |
| IRPP middle bands (25%/30% question) | Use PwC merged 30% band; flag any 1.5M–8M result | PwC is the cited source; CGI confirmation pending |
| TRIMF amount | Use 900 floor / 36,000 cap endpoints only; flag intermediate values | Full band table unconfirmed [RESEARCH GAP] |
| Residency | Treat as **resident** only if confirmed; otherwise flag | Non-resident withholding rules are out of scope here |

When inputs are missing or ambiguous, use these defaults and flag them clearly to the user. Defaults are deliberately cautious (tend to overstate tax/contributions or refuse rather than understate).

Always present payroll outputs as estimated, label every gap, and direct the user to a Senegalese expert-comptable.

### 9.1 Required inputs (refuse to compute net pay without these)

1. Gross monthly remuneration in XOF (and whether benefits in kind / bonuses are included).
2. Pay period and pay frequency (monthly assumed).
3. Family situation: single / married; number of dependent children (for parts and TRIMF spouse part).
4. Whether the employee is a cadre (executive) — determines the complementary IPRES scheme.
5. The employer's CSS work-injury risk class (1%, 3% or 5%).
6. The employer's IPM affiliation and that IPM's rate/base/caps.
7. Tax residency status of the employee.

### 9.2 Refusal Catalogue — refuse and explain when:

**Refusal Catalogue**

| Trigger | Refuse because |
| --- | --- |
| No gross salary figure given | Cannot compute any withholding or contribution |
| Family parts asserted but not evidenced | Parts cap unconfirmed [RESEARCH GAP]; default to 1 part rather than grant unverified relief |
| Result falls in the 1,500,001–8,000,000 per-part band | Middle-band rate (25% vs 30%) unconfirmed against CGI — produce a range and refuse a single definitive number |
| User asks for an exact TRIMF amount on a mid-range income | Full TRIMF band table unconfirmed [RESEARCH GAP] |
| User asks for an exact IPM deduction | IPM-specific; refuse without the IPM's own schedule |
| User asks to apply a 6% "expat CFCE" | Unconfirmed; refuse and treat CFCE as flat 3% |
| Non-resident employee | Out of scope; direct to non-resident withholding rules and an expert-comptable |
| Request to treat the output as final/filed advice | This is a Tier-2 unverified estimate; require accountant sign-off |

## Section 10 — Transaction / Payment Pattern Library (Deterministic)

Deterministic mapping of bank-statement narrations to ledger treatment. Match case-insensitively; XOF amounts only.

### 10.1 Salary credits (employee-side, for reconciliation)

**Salary credits**

| Narration pattern | Classification |
| --- | --- |
| `SALAIRE`, `PAIE`, `VIREMENT SALAIRE`, `NET A PAYER` | Net salary payment |
| `ACOMPTE`, `AVANCE SUR SALAIRE` | Salary advance (recoverable, not income) |
| `PRIME`, `BONUS`, `GRATIFICATION` | Bonus (taxable; subject to IRPP/TRIMF at source) |
| `INDEMNITE TRANSPORT`, `INDEMNITE` | Allowance (check taxability per CGI) |
| `RAPPEL SALAIRE` | Back-pay / arrears |

### 10.2 Employer debits (payroll run and remittances)

**Employer debits**

| Narration pattern | Classification |
| --- | --- |
| `DGID`, `IMPOTS`, `RETENUE SOURCE`, `IR RETENUE`, `F4` | IRPP + TRIMF withholding remitted to DGID |
| `CFCE` | Employer payroll tax (3%) to DGID |
| `IPRES`, `RETRAITE` | IPRES pension contribution (employee + employer) |
| `CSS`, `SECURITE SOCIALE`, `PRESTATIONS FAMILIALES`, `ACCIDENT TRAVAIL` | CSS family-allowance / work-injury (employer only) |
| `IPM`, `PREVOYANCE MALADIE` | IPM health contribution (employer + employee) |
| `VIREMENT SALAIRES`, `PAIE`, `MASSE SALARIALE` | Net wages disbursed to employees |

> Narration strings above are the most common Senegalese banking/payroll terms; institutions vary. Treat any unmatched narration as unclassified and ask the user rather than guessing.

## Section 11 — Worked Examples

All figures in XOF. IRPP computed on (gross − professional deduction), 1 part unless stated, per the Conservative Defaults and the [RESEARCH GAP] on social-contribution deductibility. Endpoints recomputed end-to-end.

### Example A — Junior employee, 200,000/month, single, non-cadre

**Example A steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 200,000 × 12 | 2,400,000 |
| Professional deduction | 30% × 2,400,000 = 720,000 (< 1,800,000 cap) | 720,000 |
| IRPP base | 2,400,000 − 720,000 | 1,680,000 |
| IRPP (1 part) | band 1,500,001–4,000,000 @30%: 174,000 + (1,680,000 − 1,500,000) × 30% = 174,000 + 54,000 | **228,000/yr (19,000/mo)** |
| IPRES employee (Régime Général) | base 200,000 < 432,000 ceiling → 5.6% × 200,000 | 11,200/mo |
| IPRES employer | 8.4% × 200,000 | 16,800/mo |
| CSS family allow. (employer) | 7% × 63,000 (base capped at ceiling) | 4,410/mo |
| CSS work-injury (employer, default 5%) | 5% × 63,000 | 3,150/mo |
| CFCE (employer) | 3% × 200,000 | 6,000/mo |
| TRIMF | [RESEARCH GAP — exact band amount] | flag |
| IPM | [RESEARCH GAP — IPM-specific] | flag |

Arithmetic check: 174,000 + 54,000 = 228,000 ✓; 228,000 / 12 = 19,000 ✓.

### Example B — Mid employee, 500,000/month, single, non-cadre

**Example B steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 500,000 × 12 | 6,000,000 |
| Professional deduction | 30% × 6,000,000 = 1,800,000 (= cap) | 1,800,000 |
| IRPP base | 6,000,000 − 1,800,000 | 4,200,000 |
| IRPP (1 part) | band 4,000,001–8,000,000 @35%: 924,000 + (4,200,000 − 4,000,000) × 35% = 924,000 + 70,000 | **994,000/yr (82,833/mo)** |
| IPRES employee | salary 500,000 > 432,000 ceiling → 5.6% × 432,000 | 24,192/mo |
| IPRES employer | 8.4% × 432,000 | 36,288/mo |
| CSS family allow. (employer) | 7% × 63,000 | 4,410/mo |
| CSS work-injury (employer, default 5%) | 5% × 63,000 | 3,150/mo |
| CFCE (employer) | 3% × 500,000 | 15,000/mo |

Arithmetic check: 924,000 + 70,000 = 994,000 ✓; 994,000 / 12 = 82,833.33 ✓ (round per DGID rules).

> Note: this result spans the 4M+ band, but the IRPP base (4,200,000) sits just above the 4,000,000 boundary. The 1,500,001–4,000,000 portion uses the PwC merged 30% rate — flag the 25%/30% [RESEARCH GAP] to the user.

### Example C — Cadre, 1,000,000/month, married + 2 children, non-cadre vs cadre schemes

**Example C steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 1,000,000 × 12 | 12,000,000 |
| Professional deduction | 30% × 12,000,000 = 3,600,000, capped at 1,800,000 | 1,800,000 |
| IRPP base (total) | 12,000,000 − 1,800,000 | 10,200,000 |
| Parts | married 1.5 + (2 × 0.5) | 2.5 parts [RESEARCH GAP — part cap] |
| Income per part | 10,200,000 / 2.5 | 4,080,000 |
| IRPP per part | band 4,000,001–8,000,000 @35%: 924,000 + (4,080,000 − 4,000,000) × 35% = 924,000 + 28,000 | 952,000 |
| IRPP total | 952,000 × 2.5 | **2,380,000/yr (198,333/mo)** |
| IPRES general employee | 5.6% × 432,000 (ceiling) | 24,192/mo |
| IPRES cadre employee | 2.4% × 1,000,000 (< 1,296,000 ceiling) | 24,000/mo |
| IPRES cadre employer | 3.6% × 1,000,000 | 36,000/mo |
| CFCE (employer) | 3% × 1,000,000 | 30,000/mo |

Arithmetic check: 924,000 + 28,000 = 952,000 ✓; 952,000 × 2.5 = 2,380,000 ✓; 2,380,000 / 12 = 198,333.33 ✓.

### Example D — Minimum-wage employee (SMIG), single, non-cadre

**Example D steps**

| Step | Computation | Result |
| --- | --- | --- |
| SMIG hourly | 371 FCFA/hr (since 1 July 2023) [confirm decree — RESEARCH GAP] | 371/hr |
| Monthly (173.33 hrs) | 371 × 173.33 ≈ | ~64,300/mo |
| Gross annual | ~64,300 × 12 | ~771,600 |
| Professional deduction | 30% × 771,600 | 231,480 |
| IRPP base | 771,600 − 231,480 | 540,120 |
| IRPP (1 part) | 540,120 ≤ 630,000 → 0% band | **0 IRPP** |
| MPIT floor | income < 600,000 → 900/yr | 900/yr |
| IPRES employee | 5.6% × 64,300 (< 432,000) | 3,601/mo |
| CFCE (employer) | 3% × 64,300 | 1,929/mo |

Arithmetic check: 540,120 < 630,000 → 0% ✓. MPIT floor 900 applies since computed IRPP (0) is below it.

### Example E — Employer total cost-of-employment snapshot (Example B employee)

**Example E cost snapshot**

| Cost component (monthly) | Amount |
| --- | --- |
| Gross salary | 500,000 |
| IPRES employer (8.4% × 432,000) | 36,288 |
| CSS family allowance (7% × 63,000) | 4,410 |
| CSS work-injury (5% × 63,000, default) | 3,150 |
| CFCE (3% × 500,000) | 15,000 |
| IPM employer | [RESEARCH GAP] |
| **Total employer cost (excl. IPM)** | **558,848** |

Arithmetic check: 500,000 + 36,288 + 4,410 + 3,150 + 15,000 = 558,848 ✓.

## Section 12 — Tier 1 Rules (deterministic, no judgement)

- **1. Tax year** — Tax year is the calendar year.  _(PwC, Senegal Tax Administration)_
- **2. IRPP withholding scope** — IRPP is withheld at source on gross remuneration including benefits in kind and bonuses.  _(PwC)_
- **3. Professional deduction rule** — The professional deduction is 30% of gross employment income, capped at 1,800,000 XOF/year (150,000/month).  _(Rivermate (confirm CGI))_
- **4. IPRES Régime Général** — IPRES Régime Général: employee 5.6% + employer 8.4% = 14.0%, monthly ceiling 432,000 XOF.  _(PwC; CLEISS)_
- **5. IPRES Régime Complémentaire des Cadres** — IPRES Régime Complémentaire des Cadres: employee 2.4% + employer 3.6% = 6.0%, monthly ceiling 1,296,000 XOF.  _(PwC; CLEISS)_
- **6. CSS family allowances** — CSS family allowances: 7% employer-only, ceiling 63,000 XOF/month.  _(PwC; CLEISS)_
- **7. CSS work-injury** — CSS work-injury: 1%/3%/5% by risk class, employer-only, ceiling 63,000 XOF/month.  _(PwC; CLEISS)_
- **8. CFCE rate** — CFCE: 3% of total gross payroll, employer-only.  _(Sénégal Services / DGID; PwC)_
- **9. Monthly remittance deadline** — Monthly withholding (IRPP + TRIMF + CFCE) is declared and remitted before the 15th of the following month.  _(Sénégal Services / DGID)_
- **10. MPIT floor rule** — MPIT floor: 900 XOF (income < 600,000) up to 36,000 XOF (income ≥ 12,000,000).  _(PwC)_

## Section 13 — Tier 2 Catalogue (requires reviewer judgement)

1. Exact IRPP middle bands (25%/30% split vs PwC merged 30%) — CGI Art. 173. [RESEARCH GAP]
2. Exact TRIMF bracket-by-bracket schedule. [RESEARCH GAP]
3. Family-quotient part counts and the statutory maximum number of parts. [RESEARCH GAP]
4. Whether IRPP base is net of social contributions and the deduction ordering. [RESEARCH GAP]
5. Whether CFCE has any expatriate-specific rate (6% claim unconfirmed). [RESEARCH GAP]
6. The specific IPM's rate, base and caps for a given employer. [RESEARCH GAP]
7. The employer's CSS work-injury risk class (1%/3%/5%).
8. Current official SMIG/SMAG decree figures. [RESEARCH GAP]
9. Taxability of specific allowances and benefits in kind under the CGI.

## Section 14 — Excel Working Paper Template

Suggested columns for a monthly payroll working paper (one row per employee). All amounts XOF.

**Working paper columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name / matricule | input |
| B | Gross monthly remuneration | input |
| C | Benefits in kind | input |
| D | Total gross (B + C) | `=B+C` |
| E | Professional deduction | `=MIN(0.30*D*12,1800000)/12` (annualised cap) |
| F | Monthly IRPP base | `=D-E` (flag social-contribution deductibility gap) |
| G | Parts | input (default 1) |
| H | IRPP (annual scale per part × parts) ÷ 12 | scale function on `F*12/G` |
| I | TRIMF | TRIMF band lookup [RESEARCH GAP] |
| J | IPRES employee (5.6%, base MIN(D,432000)) | `=0.056*MIN(D,432000)` |
| K | IPRES cadre employee (2.4%, base MIN(D,1296000)) | `=0.024*MIN(D,1296000)` if cadre |
| L | IPM employee | [RESEARCH GAP] |
| M | Net pay | `=D-H-I-J-K-L` |
| N | IPRES employer (8.4%) | `=0.084*MIN(D,432000)` |
| O | CSS family (7%, base MIN(D,63000)) | `=0.07*MIN(D,63000)` |
| P | CSS work-injury (rate × MIN(D,63000)) | `=rate*MIN(D,63000)` |
| Q | CFCE (3%) | `=0.03*D` |
| R | IPM employer | [RESEARCH GAP] |
| S | Total employer cost | `=D+N+O+P+Q+R` |

Add a reconciliation row summing columns H, I (DGID remittance), J+N (IPRES), O+P (CSS), Q (CFCE) for the F4 / monthly declaration.

## Section 15 — Bank Statement / Terminology Reading Guide

**Terminology guide**

| French / Wolof-influenced term | English meaning |
| --- | --- |
| `Salaire brut` | Gross salary |
| `Salaire net` / `Net à payer` | Net pay |
| `Retenue à la source` | Withholding at source (IRPP + TRIMF) |
| `Bulletin de paie` | Payslip |
| `Quotient familial` / `Parts` | Family quotient / parts |
| `Cadre` | Executive / managerial employee |
| `Cotisations sociales` | Social contributions |
| `Prestations familiales` | Family allowances (CSS) |
| `Accident du travail` | Work injury (CSS) |
| `Acompte` / `Avance` | Advance on salary |
| `Indemnité` | Allowance / indemnity |
| `Masse salariale` | Total payroll / wage bill |
| `DGID` | Tax authority |
| `IPRES` / `CSS` / `IPM` | Pension / social security / health bodies |

## Section 16 — Onboarding Fallback

When onboarding a new Senegal payroll client and information is incomplete:

1. Request the latest bulletins de paie and the employer's IPRES, CSS and IPM affiliation numbers.
2. Confirm each employee's family situation (for parts and TRIMF spouse part) and cadre status.
3. Obtain the employer's CSS work-injury risk class in writing from CSS.
4. Obtain the IPM's contribution schedule (rate, base, caps).
5. Until confirmed, apply the Conservative Defaults (Section 8) and label every output as an estimate with flagged [RESEARCH GAP] items.
6. Do not file or finalise any return — produce a working paper for the expert-comptable to review and sign off.

## Section 17 — Filing, Remittance and Forms

**Filing and remittance schedule**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year | PwC |
| Monthly employer withholding (IRPP + TRIMF + CFCE) | Declared/remitted before the 15th of the following month; declaration form **F4** (practitioner-cited) | PwC; Sénégal Services / DGID |
| Annual salary summary declaration | Early in the following year (commonly cited ~1 March); CFCE annual recap before 31 December | Practitioner sources; Sénégal Services [RESEARCH GAP on exact form/date] |
| Individual annual income tax return | Before 1 May of each year for prior-year income; pure-PAYE employees may be exempt | PwC, Senegal Tax Administration |

Sources: PwC Tax Administration (https://taxsummaries.pwc.com/senegal/individual/tax-administration) · DGID IR simulator (http://www.impotsetdomaines.gouv.sn/fr/simulateur/ir).

## Section 18 — Penalties and Interest

**Penalties and interest table**  _(PwC Tax Summaries — Senegal, Tax administration (https://taxsummaries.pwc.com/senegal/corporate/tax-administration))_

| Trigger | Penalty / interest | Source |
| --- | --- | --- |
| Late filing of a return | 200,000 XOF per return | PwC |
| Spontaneous late payment | 5% interest on the amount due, plus 0.5% per month (or part-month) of delay | PwC |
| Assessed via audit — WHT and VAT | 50% penalty | PwC |
| Assessed via audit — other taxes | 25% penalty | PwC |

## Section 19 — Minimum Wage (SMIG / SMAG)

**SMIG / SMAG table**

| Item | Value | Source |
| --- | --- | --- |
| SMIG (non-agricultural) | 371 FCFA gross/hour since 1 July 2023 (40-hour legal week) ≈ 64,300 FCFA/month at 173.33 hrs | africapaierh; Rivermate [RESEARCH GAP — confirm decree] |
| SMAG (agricultural) | Separate, lower rate set for the agricultural sector | Ministry of Labour [RESEARCH GAP — confirm current amount] |

> [RESEARCH GAP — reviewer to confirm] An older figure of 52,500 FCFA/month (303.49 FCFA/hour) is widely repeated but predates the 2023 increase. Use the 371 FCFA/hour (post-July-2023) figure, and verify it against an official decree from the Ministry of Labour before publishing.

## Section 20 — Reference Material and Test Suite

### 20.1 Reference anchors

- PwC Tax Summaries — Senegal (individual + corporate). https://taxsummaries.pwc.com/senegal
- CLEISS — Senegal social-security contributions, effective 01/01/2026. https://www.cleiss.fr/docs/cotisations/senegal.html
- DGID — impotsetdomaines.gouv.sn (CFCE page, IR simulator).
- CGI (Code Général des Impôts), official PDF via eRegulations. https://senegal.eregulations.org/media/t-code-general-impots[1].pdf
- Sénégal Services — CFCE démarche. https://senegalservices.sn

### 20.2 Test Suite (recompute each before relying on the skill)

- **IRPP cumulative @4,000,000/part** — 924,000. Check: 174,000 + (4,000,000 − 1,500,000) × 30% = 174,000 + 750,000 = 924,000. ✓
- **IRPP cumulative @8,000,000/part** — 2,324,000. Check: 924,000 + 4,000,000 × 35% = 2,324,000. ✓
- **IRPP cumulative @13,500,000/part** — 4,359,000. Check: 2,324,000 + 5,500,000 × 37% = 4,359,000. ✓
- **IRPP cumulative @50,000,000/part** — 18,959,000. Check: 4,359,000 + 36,500,000 × 40% = 18,959,000. ✓
- **IPRES Régime Général total** — 14.0%. Check: 5.6 + 8.4. ✓
- **IPRES Cadres total** — 6.0%. Check: 2.4 + 3.6. ✓
- **Example A IRPP** — 228,000/yr (19,000/mo) on base 1,680,000. Check: 174,000 + 180,000 × 30% = 228,000. ✓
- **Example B IRPP** — 994,000/yr on base 4,200,000. Check: 924,000 + 200,000 × 35% = 994,000. ✓
- **Example C IRPP** — 2,380,000/yr, 2.5 parts, per-part base 4,080,000. Check: (924,000 + 80,000 × 35%) × 2.5 = 952,000 × 2.5 = 2,380,000. ✓
- **Example D** — base 540,120 ≤ 630,000 → 0% IRPP, MPIT floor 900. ✓
- **Example E employer cost (excl. IPM)** — 558,848. Check: 500,000 + 36,288 + 4,410 + 3,150 + 15,000. ✓
- **IPRES employee cap @500,000 salary** — 24,192/mo. Check: 5.6% × 432,000 (ceiling). ✓

## PROHIBITIONS

- **No no-income-tax treatment** — NEVER treat Senegal as a no-income-tax jurisdiction — IRPP and TRIMF both apply to salaries.
- **Family parts default** — NEVER grant family parts that are not evidenced; default to 1 part and flag the CGI part-cap gap.
- **IRPP middle-band gap flag** — NEVER publish a single definitive IRPP figure for a per-part base in the 1,500,001–8,000,000 range without flagging the 25%/30% middle-band [RESEARCH GAP].
- **TRIMF mid-range invention ban** — NEVER invent a TRIMF amount for a mid-range income — the full band table is unconfirmed.
- **Expatriate CFCE ban** — NEVER apply a 6% "expatriate CFCE" — unconfirmed; CFCE is flat 3% absent CGI proof.
- **Ceiling application requirement** — NEVER compute IPRES, CSS or IPM without applying the correct monthly ceiling (432,000 / 1,296,000 / 63,000 / 250,000).
- **Employer-only branches inclusion** — NEVER forget the employer-only CFCE (3%) and CSS branches in the total cost of employment.
- **IPM deduction schedule requirement** — NEVER compute a definitive IPM deduction without the specific IPM's schedule.
- **Remittance deadline** — NEVER miss the 15th-of-following-month remittance deadline — penalties (200,000 XOF/return + interest) apply.
- **Non-definitive presentation requirement** — NEVER present payroll computations as definitive — always label as estimated, flag every [RESEARCH GAP], and direct to a Senegalese expert-comptable.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. This is a **Tier-2, research-verified draft pending sign-off by a licensed Senegalese accountant (expert-comptable)**; several figures are flagged [RESEARCH GAP — reviewer to confirm] and must be checked against the Code Général des Impôts and current decrees. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before implementation.

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
