---
name: senegal-payroll
description: Use this skill whenever asked about Senegal payroll processing for employed persons. Trigger on phrases like "Senegal payroll", "Sénégal paie", "IRPP Senegal", "retenue à la source Senegal", "TRIMF", "IPRES contribution", "CSS Senegal", "prestations familiales", "CFCE", "IPM health Senegal", "quotient familial Senegal" (Senegal has a reduction, not a quotient), "parts fiscales", "net salary Senegal", "salaire net Sénégal", "PAYE Senegal", "employer social charges Senegal", "SMIG Senegal", "minimum wage Senegal", "form F4 Senegal", "gross to net Senegal", "bulletin de paie", or any question about computing employee pay, income tax withholding, or social contributions for Senegal-based employees. Senegal DOES levy personal income tax (IRPP) on salaries plus a fixed local salary tax (TRIMF). This skill covers progressive IRPP withholding with the family reduction on the tax (CGI art. 174), TRIMF, IPRES pensions, CSS family allowances and work-injury, IPM health cover, the employer payroll tax (CFCE), minimum wage, filing obligations, and penalties. ALWAYS read this skill before processing any Senegal payroll.
version: 0.2
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal Payroll Skill v0.2 (Tier 2: research-verified, pending accountant sign-off)

## Senegal Payroll Skill v0.2 (Tier 2: research-verified, pending accountant sign-off)

> Senegal is **not** a no-income-tax jurisdiction. Salaries bear progressive personal income tax (IRPP) withheld at source, a separate fixed local salary tax (TRIMF), mandatory social contributions (IPRES, CSS, IPM), and an employer-only payroll tax (CFCE). All five must be handled together.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Senegal (République du Sénégal) |
| Currency | West African CFA franc — XOF / FCFA only |
| Standard pay frequency | Monthly (mensuel) |
| Tax year | Calendar year (1 January: 31 December) |
| Income tax system | IRPP: progressive bands on the whole income (CGI art. 173), then a family reduction on the tax by parts (art. 174), withheld at source (arts. 181, 183) |
| Fixed local salary tax | TRIMF (Taxe Représentative de l'Impôt du Minimum Fiscal): CGI arts. 275 to 282 |
| Tax authority | Direction Générale des Impôts et des Domaines (DGID) |
| Pension body | IPRES (Institution de Prévoyance Retraite du Sénégal) |
| Family allowance / work injury body | Caisse de Sécurité Sociale (CSS) |
| Health body | IPM (Institution de Prévoyance Maladie) — employer-level institution |
| Employer payroll tax | CFCE — Contribution Forfaitaire à la Charge de l'Employeur, 3% of payroll |
| Monthly remittance | First 15 days of the following month, with the art. 186 declaration (CGI art. 185); quarterly for real simplified and CGU employers. F4 is the practitioner name for the form; the CGI does not use it |
| Validated by | Pending — requires sign-off by a Senegalese chartered accountant (expert-comptable) |
| Skill version | 0.2 |

## Section 2 — Income Tax Withholding (IRPP)

The employer withholds IRPP at source when paying gross remuneration, including benefits in kind and bonuses (CGI arts. 181, 183, 184). The bands apply to the whole taxable income, not per part. Parts only set the family reduction taken off the tax (art. 174).

Order of the calculation:

1. Gross pay plus benefits in kind.
2. Less the 30% abatement, capped at 900,000 a year.
3. Round down to the thousand and apply the bands (art. 173).
4. Take the family reduction from the tax (art. 174).
5. Cap the tax at 43% of taxable income (art. 174).
6. TRIMF is separate and on top.

### 2.1 Professional / employment deduction

- **Abatement**: 30% of gross employment income, covering compulsory pension contributions and job costs  _(CGI arts. 168 b and 182)_
- **Annual cap on the abatement**: 900,000 XOF/year (= 75,000 XOF/month)  _(CGI arts. 168 b and 182)_
- **Application order**: The abatement is applied to gross employment income before the bands. It does not apply to pensions and life annuities.
- **Social contributions are not a separate deduction**: The abatement stands in for compulsory pension contributions. Art. 168 lists no other deduction for employee social contributions, so IPRES and IPM employee shares are never taken off the IRPP base on top of it.
- **Other deductions in art. 168**: The 10% or 20% special abatement for State agents in diplomatic posts, taken first; and mileage allowances up to 50,000 XOF a month, or 100,000 XOF for sales representatives doing at least 500 km a week (Arrêté 12911 of 31 July 2013, printed under art. 168).

### 2.2 Progressive IRPP scale (annual taxable income, XOF)

**Progressive IRPP scale**  _(Source: CGI art. 173. https://www.dgid.sn/storage/docs/CGI-2025.pdf)_

| Annual taxable income (XOF) | Marginal rate | Cumulative tax at top of band (XOF) |
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

The 25% band that some French payroll sources show is not in art. 173. The band from 1,500,001 to 4,000,000 is 30%.

### 2.3 Family reduction (réduction pour charges de famille)

Income is not split into parts. The tax from the bands is reduced by the rate for the employee's parts, within a minimum and a maximum (CGI art. 174).

| Parts | Rate | Minimum (XOF) | Maximum (XOF) |
| --- | --- | --- | --- |
| 1 | 0% | 0 | 0 |
| 1.5 | 10% | 100,000 | 300,000 |
| 2 | 15% | 200,000 | 650,000 |
| 2.5 | 20% | 300,000 | 1,100,000 |
| 3 | 25% | 400,000 | 1,650,000 |
| 3.5 | 30% | 500,000 | 2,030,000 |
| 4 | 35% | 600,000 | 2,490,000 |
| 4.5 | 40% | 700,000 | 2,755,000 |
| 5 | 45% | 800,000 | 3,180,000 |

| Situation | Parts |
| --- | --- |
| Single, divorced or widowed, no dependent child | 1 |
| Married, no dependent child | 1.5 |
| Single or divorced, 1 dependent child | 1.5 |
| Married or widowed, 1 dependent child | 2 |
| Each further dependent child | +0.5 |
| Only one spouse has taxable income | +0.5 (art. 174.3) |

The maximum is 5 parts in all cases (art. 174.4). Non-residents: maximum 1.5 parts (art. 176). Each child gives a half part to each parent with income (art. 174.2). Single people with no dependent child get 1.5 parts if a child has died, on a 40% war or accident pension, or after adopting (art. 175). A married employee who does not give the employer the spouse's details loses the extra half part (art. 191, point 8).

### 2.4 No minimum income tax

The old "MPIT floor" does not exist as a floor on IRPP. Arts. 173 and 174 set no minimum. The 900 to 36,000 table is the TRIMF table of art. 282, a separate tax added on top of IRPP, whatever the IRPP. Never compute IRPP as the higher of the scale tax and that table.

## Section 3 — TRIMF (Taxe Représentative de l'Impôt du Minimum Fiscal)

A separate fixed **annual** tax on salaries and pensions, withheld at source by the employer and paid with the salary withholding (CGI arts. 181, 183.3, 275). It funds local authorities. It is due by anyone resident in Senegal receiving salary or pension (art. 275). Technical assistance staff of a foreign State or international body, and pensioners paid from abroad, are outside it (art. 277).

**TRIMF annual table (art. 282)**

| Gross annual income, with benefits (XOF) | TRIMF per year (XOF) |
| --- | --- |
| 0 to 599,999 | 900 |
| 600,000 to 999,999 | 3,600 |
| 1,000,000 to 1,999,999 | 4,800 |
| 2,000,000 to 6,999,999 | 12,000 |
| 7,000,000 to 11,999,999 | 18,000 |
| 12,000,000 and over | 36,000 |

The band is read directly from gross income, before the abatement. Amounts are per year, not per month.

**Spouse:** the employee is taxed at the rate for his or her band for himself or herself and for a spouse without income (art. 276). If the spouse has no income, charge the band amount twice. If the spouse has income, charge it once.

The employer regularises at the last payment of the year, on the year's salary with benefits (art. 281). Over-withheld TRIMF is reclaimed before 1 April of the next year (art. 281).

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
| Rate | 3% (art. 267) | CGI |
| Base | All salaries, paid leave, bonuses, allowances and benefits in money or kind; excludes expense reimbursements and family benefits (art. 266) | CGI |
| Exemptions | State, local authorities, foreign or international public bodies; art. 253 companies; 3 years for 50 new stable jobs; 3 years for new companies outside the large-enterprise service; approved investment regime; mining and petroleum phases (arts. 263, 264) | CGI |
| Party | Employer only | CGI art. 263 |
| Monthly payment deadline | Same conditions and dates as salary withholding (art. 268, so art. 185) | CGI |
| Annual statement | January, with the art. 191 salary statement (art. 269 extends employer obligations to CFCE) | CGI |

Contribution Forfaitaire à la Charge de l'Employeur — an employer-only payroll tax.

There is no expatriate rate. Art. 267 sets one rate of 3%; art. 265 reaches pay of people domiciled abroad on the same terms.

Source: CGI arts. 263 to 269, https://www.dgid.sn/storage/docs/CGI-2025.pdf.

## Section 8 — Conservative Defaults

**Conservative defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Family situation / parts | Treat as **1 part (single, no dependants)** | Highest IRPP: never grant unevidenced parts. Maximum is 5 (art. 174) |
| Cadre vs non-cadre | Treat as **non-cadre** (Régime Général only) | Do not assume the complementary executive scheme applies without confirmation |
| Work-injury risk class | Use the **highest cited rate, 5%** | Avoids understating employer cost — confirm actual class with CSS |
| IPM rate | Flag as **[RESEARCH GAP]**, do not compute a number | Rate is IPM-specific; refuse a definitive figure |
| Spouse income for TRIMF | Charge the band amount twice until the spouse's income is evidenced | Art. 276: covers a spouse without income |
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
| Family parts asserted but not evidenced | Default to 1 part rather than grant unevidenced relief; maximum is 5 (art. 174) |
| User asks for an exact IPM deduction | IPM-specific; refuse without the IPM's own schedule |
| User asks to apply a 6% "expat CFCE" | Art. 267 has one rate; CFCE is 3% |
| Non-resident employee | Withholding still applies where the employer is in Senegal (art. 183), maximum 1.5 parts (art. 176); treaty questions go to an expert-comptable |
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

All figures in XOF. IRPP computed on gross less the capped abatement, rounded down to the thousand, 1 part unless stated. Monthly figures divide the annual tax by 12. Employee social contributions are not deducted again (art. 182).

### Example A — Junior employee, 200,000/month, single, non-cadre

**Example A steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 200,000 × 12 | 2,400,000 |
| Abatement | 30% × 2,400,000 = 720,000 (< 900,000 cap) | 720,000 |
| IRPP base | 2,400,000 − 720,000 | 1,680,000 |
| IRPP (1 part) | band 1,500,001–4,000,000 @30%: 174,000 + (1,680,000 − 1,500,000) × 30% = 174,000 + 54,000 | **228,000/yr (19,000/mo)** |
| IPRES employee (Régime Général) | base 200,000 < 432,000 ceiling → 5.6% × 200,000 | 11,200/mo |
| IPRES employer | 8.4% × 200,000 | 16,800/mo |
| CSS family allow. (employer) | 7% × 63,000 (base capped at ceiling) | 4,410/mo |
| CSS work-injury (employer, default 5%) | 5% × 63,000 | 3,150/mo |
| CFCE (employer) | 3% × 200,000 | 6,000/mo |
| TRIMF | Gross 2,400,000 is in the 2,000,000–6,999,999 band | 12,000/yr (1,000/mo) |
| IPM | Fund-specific; take it from the IPM schedule | flag |

Arithmetic check: 174,000 + 54,000 = 228,000 ✓; 228,000 / 12 = 19,000 ✓.

### Example B — Mid employee, 500,000/month, single, non-cadre

**Example B steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 500,000 × 12 | 6,000,000 |
| Abatement | 30% × 6,000,000 = 1,800,000, capped at 900,000 | 900,000 |
| IRPP base | 6,000,000 − 900,000 | 5,100,000 |
| IRPP (1 part) | band 4,000,001–8,000,000 @35%: 924,000 + (5,100,000 − 4,000,000) × 35% = 924,000 + 385,000 | **1,309,000/yr (109,083/mo)** |
| TRIMF | Gross 6,000,000 is in the 2,000,000–6,999,999 band | 12,000/yr (1,000/mo) |
| IPRES employee | salary 500,000 > 432,000 ceiling → 5.6% × 432,000 | 24,192/mo |
| IPRES employer | 8.4% × 432,000 | 36,288/mo |
| CSS family allow. (employer) | 7% × 63,000 | 4,410/mo |
| CSS work-injury (employer, default 5%) | 5% × 63,000 | 3,150/mo |
| CFCE (employer) | 3% × 500,000 | 15,000/mo |

Arithmetic check: 924,000 + 385,000 = 1,309,000 ✓; 1,309,000 / 12 = 109,083.33 ✓.

```oa-check
name: Payroll example B, 500,000 a month, 1 part
inputs:
  gross: 6000000
steps:
  - abatement: min(gross * 0.30, 900000)
  - base: gross - abatement
  - tax: 174000 + (4000000 - 1500000) * 0.30 + (base - 4000000) * 0.35
  - monthly: tax / 12
expected:
  tax: 1309000.00
  monthly: 109083.33
```

### Example C: Cadre, 1,000,000/month, married, 2 children, spouse has income

**Example C steps**

| Step | Computation | Result |
| --- | --- | --- |
| Gross annual | 1,000,000 × 12 | 12,000,000 |
| Abatement | 30% × 12,000,000 = 3,600,000, capped at 900,000 | 900,000 |
| IRPP base | 12,000,000 − 900,000 | 11,100,000 |
| Tax from the bands | 2,324,000 + (11,100,000 − 8,000,000) × 37% = 2,324,000 + 1,147,000 | 3,471,000 |
| Parts | Married with 2 children; spouse has income, so no extra half part | 2.5 |
| Family reduction | 20% × 3,471,000 = 694,200, between 300,000 and 1,100,000 | 694,200 |
| IRPP due | 3,471,000 − 694,200; below 43% of 11,100,000 | **2,776,800/yr (231,400/mo)** |
| TRIMF | Gross 12,000,000 is in the top band; spouse has income, so once | 36,000/yr (3,000/mo) |
| IPRES general employee | 5.6% × 432,000 (ceiling) | 24,192/mo |
| IPRES cadre employee | 2.4% × 1,000,000 (< 1,296,000 ceiling) | 24,000/mo |
| IPRES cadre employer | 3.6% × 1,000,000 | 36,000/mo |
| CFCE (employer) | 3% × 1,000,000 | 30,000/mo |

If the spouse had no income, parts would be 3: reduction 25% × 3,471,000 = 867,750, IRPP 2,603,250, and TRIMF 72,000 (art. 276).

```oa-check
name: Payroll example C, 1,000,000 a month, 2.5 parts
inputs:
  gross: 12000000
steps:
  - abatement: min(gross * 0.30, 900000)
  - base: gross - abatement
  - bands: 2324000 + (base - 8000000) * 0.37
  - reduction: min(max(bands * 0.20, 300000), 1100000)
  - tax: bands - reduction
  - monthly: tax / 12
expected:
  tax: 2776800.00
  monthly: 231400.00
```

### Example D — Minimum-wage employee (SMIG), single, non-cadre

**Example D steps**

| Step | Computation | Result |
| --- | --- | --- |
| SMIG hourly | 371 FCFA/hr since 1 July 2023 (CLEISS) | 371/hr |
| Monthly (173.33 hrs) | 371 × 173.33 ≈ | ~64,300/mo |
| Gross annual | ~64,300 × 12 | ~771,600 |
| Abatement | 30% × 771,600 | 231,480 |
| IRPP base | 771,600 − 231,480 | 540,120 |
| IRPP (1 part) | Rounded to 540,000 ≤ 630,000 → 0% band | **0 IRPP** |
| TRIMF | Gross 771,600 is in the 600,000–999,999 band | 3,600/yr (300/mo) |
| IPRES employee | 5.6% × 64,300 (< 432,000) | 3,601/mo |
| CFCE (employer) | 3% × 64,300 | 1,929/mo |

Arithmetic check: 540,000 < 630,000 → 0% ✓. TRIMF is due even though IRPP is nil.

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

- **1. Tax year**: Tax year is the calendar year.
- **2. IRPP withholding scope**: IRPP is withheld at source on remuneration including benefits in kind and bonuses.  _(CGI arts. 181, 183)_
- **3. Abatement rule**: The abatement is 30% of gross employment income, capped at 900,000 XOF/year (75,000/month). It replaces any deduction for compulsory pension contributions.  _(CGI arts. 168, 182)_
- **4. IPRES Régime Général** — IPRES Régime Général: employee 5.6% + employer 8.4% = 14.0%, monthly ceiling 432,000 XOF.  _(PwC; CLEISS)_
- **5. IPRES Régime Complémentaire des Cadres** — IPRES Régime Complémentaire des Cadres: employee 2.4% + employer 3.6% = 6.0%, monthly ceiling 1,296,000 XOF.  _(PwC; CLEISS)_
- **6. CSS family allowances** — CSS family allowances: 7% employer-only, ceiling 63,000 XOF/month.  _(PwC; CLEISS)_
- **7. CSS work-injury** — CSS work-injury: 1%/3%/5% by risk class, employer-only, ceiling 63,000 XOF/month.  _(PwC; CLEISS)_
- **8. CFCE rate**: CFCE: 3% of total gross payroll, employer-only.  _(CGI arts. 263, 266, 267)_
- **9. Remittance deadline**: Withholding (IRPP + TRIMF + CFCE) is paid in the first 15 days of the following month. Real simplified and CGU employers, and employers with monthly withholding of at most 20,000, pay in the first 15 days of January, April, July and October.  _(CGI arts. 185, 268)_
- **10. TRIMF rule**: TRIMF: 900 to 36,000 XOF a year by gross income, added to IRPP, doubled for a spouse without income.  _(CGI arts. 276, 282)_

## Section 13 — Tier 2 Catalogue (requires reviewer judgement)

1. The specific IPM's rate, base and caps for a given employer. [RESEARCH GAP]
2. The employer's CSS work-injury risk class (1%/3%/5%).
3. Current official SMIG/SMAG decree figures. [RESEARCH GAP]
4. Taxability of specific allowances and benefits in kind under the CGI (arts. 166, 167).
5. Evidence for each part claimed, including spouse income.

## Section 14 — Excel Working Paper Template

Suggested columns for a monthly payroll working paper (one row per employee). All amounts XOF.

**Working paper columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name / matricule | input |
| B | Gross monthly remuneration | input |
| C | Benefits in kind | input |
| D | Total gross (B + C) | `=B+C` |
| E | Abatement | `=MIN(0.30*D*12,900000)/12` (annual cap) |
| F | Monthly IRPP base | `=D-E` (no further deduction for social contributions) |
| G | Parts | input (default 1) |
| H | IRPP ÷ 12 | bands on `F*12`, less art. 174 reduction for G, capped at 43% |
| I | TRIMF | art. 282 lookup on `D*12`, doubled for a spouse without income, ÷ 12 |
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
| `Parts` / `Réduction pour charges de famille` | Parts / family reduction on the tax |
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
| Tax year | Calendar year | CGI |
| Employer withholding (IRPP + TRIMF + CFCE) | First 15 days of the following month, with the art. 186 declaration (form **F4** in practice); quarterly as in rule 9 | CGI arts. 185, 186, 268 |
| Annual salary statement | During January, Etat 1024; one more month on request for firms with 300+ staff or several sites | CGI art. 191; https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf |
| December withholding | Paid within the time for the art. 191 statement | CGI art. 186 |
| Individual annual income tax return | Before 1 May. Compulsory for an employee with several employers, or with non-salary income not taxed finally, or where withholding was omitted (arts. 60, 196). Otherwise only on request (art. 197) | CGI |
| Refund of over-withheld IRPP | Claim before 1 April of the next year | CGI art. 187 |
| Pay records | Keep to the end of the 11th following year | CGI art. 184 |

Source: https://www.dgid.sn/storage/docs/CGI-2025.pdf.

## Section 18 — Penalties and Interest

**Penalties and interest table**  _(CGI, https://www.dgid.sn/storage/docs/CGI-2025.pdf)_

| Trigger | Penalty / interest | Source |
| --- | --- | --- |
| Any breach with no specific fine, including a late return | 200,000 XOF; per document where documents are missing | Art. 667 |
| Spontaneous late payment of withholding | 5% interest on the amount due, plus 0.5% per further month or part-month | Arts. 189, 665 |
| Failure to declare or pay | 25% of the tax | Art. 671 I |
| Tax withheld and not paid over, bad faith, or assessment ex officio | 50% of the tax | Art. 671 III |
| Repeat breach or undeclared activity | 100% of the tax | Art. 671 IV |
| Employer did not withhold, or too little | Pays the missing amount personally, recovers it from staff, and bears the art. 671 penalty, which cannot be recovered | Art. 188 |

## Section 19 — Minimum Wage (SMIG / SMAG)

**SMIG / SMAG table**

| Item | Value | Source |
| --- | --- | --- |
| SMIG (non-agricultural) | 371 FCFA gross/hour since 1 July 2023 (40-hour legal week) ≈ 64,300 FCFA/month at 173.33 hrs | CLEISS, 2026 table [decree not read] |
| SMAG (agricultural) | 237 FCFA gross/hour since 1 July 2023 | CLEISS, 2026 table [decree not read] |

An older figure of 52,500 FCFA/month (303.49 FCFA/hour) is widely repeated but predates the 2023 increase. Use 371 FCFA/hour.

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
- **Example B IRPP**: 1,309,000/yr on base 5,100,000. Check: 924,000 + 1,100,000 × 35% = 1,309,000. ✓
- **Example C IRPP**: 2,776,800/yr, 2.5 parts. Check: 3,471,000 − 20% × 3,471,000 = 2,776,800. ✓
- **Example D**: base 540,000 ≤ 630,000 → 0% IRPP; TRIMF 3,600. ✓
- **Example E employer cost (excl. IPM)** — 558,848. Check: 500,000 + 36,288 + 4,410 + 3,150 + 15,000. ✓
- **IPRES employee cap @500,000 salary** — 24,192/mo. Check: 5.6% × 432,000 (ceiling). ✓

## PROHIBITIONS

- **No no-income-tax treatment** — NEVER treat Senegal as a no-income-tax jurisdiction — IRPP and TRIMF both apply to salaries.
- **Family parts default**: NEVER grant family parts that are not evidenced; default to 1 part. NEVER divide income by parts: art. 174 is a reduction on the tax.
- **Abatement cap**: NEVER use a 1,800,000 cap; art. 182 says 900,000. NEVER deduct employee social contributions on top of the abatement.
- **No IRPP floor**: NEVER apply an MPIT floor to IRPP; the table is TRIMF, added on top.
- **TRIMF table**: NEVER treat TRIMF as monthly; art. 282 gives annual amounts.
- **Expatriate CFCE ban**: NEVER apply a 6% "expatriate CFCE"; CFCE is 3% (art. 267).
- **Ceiling application requirement** — NEVER compute IPRES, CSS or IPM without applying the correct monthly ceiling (432,000 / 1,296,000 / 63,000 / 250,000).
- **Employer-only branches inclusion** — NEVER forget the employer-only CFCE (3%) and CSS branches in the total cost of employment.
- **IPM deduction schedule requirement** — NEVER compute a definitive IPM deduction without the specific IPM's schedule.
- **Remittance deadline**: NEVER miss the art. 185 deadline: penalties and interest apply.
- **Non-definitive presentation requirement** — NEVER present payroll computations as definitive — always label as estimated, flag every [RESEARCH GAP], and direct to a Senegalese expert-comptable.

## Sources checked for the 1 November 2026 fix

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): arts. 60, 165 to 199, 263 to 269, 275 to 282, 665 to 671 read in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-01 |
| CLEISS, Senegal contributions at 1 January 2026: table and notes read | https://www.cleiss.fr/docs/cotisations/senegal.html | 2026-11-01 |

Not yet confirmed: IPRES, CSS and IPM rates rest on CLEISS and PwC, because ipres.sn and secusociale.sn did not open; SMIG and SMAG decrees not read; dividing the annual tax by 12 is our working method for monthly withholding, the articles read give no monthly formula; the text of Loi 2025-17 was not opened; the cadre base (old text charges 6% on pay up to 1,296,000, while CLEISS says the base lies between 432,000 and 1,296,000).

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
