---
name: senegal-payroll
description: "Senegal payroll for employees, tax year 2026. Gross to net and employer cost for Senegal-based staff. IRPP salary withholding (30 percent abatement capped at XOF 900,000, the art. 173 scale, the art. 174 family reduction by parts, the 43 percent cap), TRIMF, the 3 percent CFCE employer tax, monthly remittance by the 15th, the January salary statement, penalties. Trigger on Senegal payroll, paie Senegal, retenue a la source, IRPP, TRIMF, CFCE, parts fiscales, bulletin de paie, form F4, gross to net Senegal. IPRES, CSS and IPM contributions are in senegal-social-contributions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/senegal-payroll"
  jurisdiction: "SN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Senegal Payroll Skill v1.0

## Scope

Salary withholding and employer payroll tax for employees paid in Senegal, tax year 2026 (calendar year, XOF). It covers:

- IRPP withheld at source on pay including benefits in kind and bonuses (CGI arts. 181, 183, 184);
- TRIMF, the fixed local tax on salaries and pensions (arts. 275 to 282);
- CFCE, the 3% employer flat contribution (arts. 263 to 269);
- remittance, the annual salary statement, refunds and penalties.

Senegal does levy income tax on salaries: never treat it as a no-income-tax country. The social contributions (IPRES pensions, CSS family allowances and work injury, IPM health cover) are owned by [senegal-social-contributions](senegal-social-contributions.md); their rates are not restated here. Out of scope: non-resident treaty questions, specific allowances whose taxability needs a ruling, and filing in the client's name.

## Ask the client first

1. Gross monthly pay in XOF, and whether benefits in kind and bonuses are included.
2. Family situation: single, married, divorced or widowed; number of dependent children; whether the spouse has taxable income (parts and TRIMF).
3. Tax residence of the employee (non-residents: at most 1.5 parts; TRIMF only for residents).
4. The employer's tax regime (real normal, real simplified or CGU) and the monthly withholding total (decides monthly or quarterly remittance).
5. Whether the employer has a CFCE exemption (new company, 50 new jobs, approved investment, mining or petroleum phase).

Without the gross pay, stop: nothing can be computed.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Employment abatement | 30% of gross employment income, capped at XOF 900,000 a year; not for pensions and life annuities (arts. 168 b, 182) | 2026 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| IRPP band 1 | 0% on 0 to 630,000 (art. 173) | 2026 | same |
| IRPP band 2 | 20% on 630,001 to 1,500,000 | 2026 | same |
| IRPP band 3 | 30% on 1,500,001 to 4,000,000 | 2026 | same |
| IRPP band 4 | 35% on 4,000,001 to 8,000,000 | 2026 | same |
| IRPP band 5 | 37% on 8,000,001 to 13,500,000 | 2026 | same |
| IRPP band 6 | 40% on 13,500,001 to 50,000,000 | 2026 | same |
| IRPP band 7 | 43% above 50,000,000 | 2026 | same |
| Cap on the tax | IRPP may not exceed 43% of taxable income (art. 174) | 2026 | same |
| Family reduction, 1 part | 0% | 2026 | same |
| Family reduction, 1.5 parts | 10%, minimum 100,000, maximum 300,000 (art. 174) | 2026 | same |
| Family reduction, 2 parts | 15%, minimum 200,000, maximum 650,000 | 2026 | same |
| Family reduction, 2.5 parts | 20%, minimum 300,000, maximum 1,100,000 | 2026 | same |
| Family reduction, 3 parts | 25%, minimum 400,000, maximum 1,650,000 | 2026 | same |
| Family reduction, 3.5 parts | 30%, minimum 500,000, maximum 2,030,000 | 2026 | same |
| Family reduction, 4 parts | 35%, minimum 600,000, maximum 2,490,000 | 2026 | same |
| Family reduction, 4.5 parts | 40%, minimum 700,000, maximum 2,755,000 | 2026 | same |
| Family reduction, 5 parts | 45%, minimum 800,000, maximum 3,180,000 | 2026 | same |
| TRIMF, gross 0 to 599,999 | XOF 900 a year (art. 282) | 2026 | same |
| TRIMF, gross 600,000 to 999,999 | XOF 3,600 a year | 2026 | same |
| TRIMF, gross 1,000,000 to 1,999,999 | XOF 4,800 a year | 2026 | same |
| TRIMF, gross 2,000,000 to 6,999,999 | XOF 12,000 a year | 2026 | same |
| TRIMF, gross 7,000,000 to 11,999,999 | XOF 18,000 a year | 2026 | same |
| TRIMF, gross 12,000,000 and over | XOF 36,000 a year | 2026 | same |
| CFCE | 3% of gross payroll, employer only, no ceiling (arts. 263, 266, 267) | 2026 | same |
| Remittance | First 15 days of the next month; real simplified and CGU employers quarterly, first 15 days of January, April, July and October (arts. 185, 268) | 2026 | same |
| Late payment interest | 5% of the unpaid amount, plus 0.5% for each further month or part-month (art. 665) | 2026 | same |
| General fine | XOF 200,000 for a breach with no specific fine (art. 667) | 2026 | same |
| Penalty, failure to declare or pay | 25% of the tax (art. 671 I) | 2026 | same |
| Penalty, tax withheld and not paid over or bad faith | 50% of the tax (art. 671 III) | 2026 | same |
| Penalty, repeat breach or undeclared activity | 100% of the tax (art. 671 IV) | 2026 | same |

The 25% band some French payroll sources show is not in art. 173: the band from 1,500,001 to 4,000,000 is 30%.

### Step 1: IRPP withholding

1. Gross pay plus benefits in kind for the year (or the month times 12).
2. Less the 30% abatement, capped at XOF 900,000 a year (75,000 a month). The abatement stands in for compulsory pension contributions and job costs: never deduct the employee's IPRES or IPM shares on top of it (arts. 168, 182).
3. Other art. 168 deductions, taken first where they apply: the 10% or 20% special abatement for State agents in diplomatic posts; mileage allowances up to XOF 50,000 a month, or 100,000 for sales representatives doing at least 500 km a week (Arrete 12911 of 31 July 2013, printed under art. 168).
4. Round down to the thousand francs and apply the bands to the whole income (art. 173). Cumulative tax at the top of each band: 174,000 at 1,500,000; 924,000 at 4,000,000; 2,324,000 at 8,000,000; 4,359,000 at 13,500,000; 18,959,000 at 50,000,000.
5. Take the family reduction from the tax: rate for the parts, kept between the minimum and the maximum (art. 174). Income is never divided by parts.
6. Cap the tax at 43% of taxable income (art. 174).
7. Monthly withholding: the annual tax divided by 12 (our working method; the articles read give no monthly formula, see Not yet confirmed). Regularise at the last pay of the year.

There is no minimum IRPP. The 900 to 36,000 table is TRIMF (art. 282), a separate tax added on top. Never compute IRPP as the higher of the scale tax and that table.

### Step 2: parts

| Situation | Parts |
|---|---|
| Single, divorced or widowed, no dependent child | 1 |
| Married, no dependent child | 1.5 |
| Single or divorced, 1 dependent child | 1.5 |
| Married or widowed, 1 dependent child | 2 |
| Each further dependent child | +0.5 |
| Only one spouse has taxable income | +0.5 (art. 174.3) |

Maximum 5 parts in all cases (art. 174.4). Non-residents: maximum 1.5 parts (art. 176). Each child gives a half part to each parent with income (art. 174.2). A single person with no dependent child gets 1.5 parts if a child has died, on a 40% war or accident pension, or after adopting (art. 175). A married employee who does not give the employer the spouse's details loses the extra half part (art. 191, point 8).

### Step 3: TRIMF

A fixed annual tax on salaries and pensions, withheld by the employer with the salary withholding (arts. 181, 183.3, 275). Due by anyone resident in Senegal receiving salary or pension (art. 275). Technical assistance staff of a foreign State or international body, and pensioners paid from abroad, are outside it (art. 277); the art. 271 points 1 to 7 exemptions also apply (art. 278), such as blind people and people with a 50% work-accident or war disability.

- The band is read directly from gross income with benefits, before the abatement (art. 282). Amounts are per year.
- Spouse: the employee is taxed for himself or herself and for a spouse without income (art. 276). Our reading: charge the band amount twice if the spouse has no income, once if the spouse has income (see Not yet confirmed).
- The employer regularises at the last payment of the year (art. 281); over-withheld TRIMF is reclaimed before 1 April of the next year.

### Step 4: CFCE

3% of all salaries, paid leave, bonuses, allowances and benefits in money or kind; expense reimbursements and family benefits are left out (arts. 266, 267). Employer only (art. 263). There is no expatriate rate: art. 267 sets one rate, and art. 265 reaches pay of people domiciled abroad on the same terms. Exemptions: the State, local authorities, foreign or international public bodies; art. 253 companies; 3 years for 50 new stable jobs; 3 years for new companies outside the large-enterprise service; the approved investment regime; mining and petroleum phases (arts. 263, 264). Paid on the same conditions and dates as salary withholding (art. 268).

### Step 5: social contributions

Add the employee and employer IPRES, CSS and IPM amounts from [senegal-social-contributions](senegal-social-contributions.md). Net pay = gross less IRPP, TRIMF and the employee social shares. Employer cost = gross plus CFCE and the employer social shares.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Non-resident employee paid by a Senegal employer | Withholding still applies (art. 183); at most 1.5 parts (art. 176); no TRIMF (art. 275); treaty questions to an expert-comptable |
| Employee leaving Senegal for good | Employer regularises the year's tax and gives a certificate stamped by the tax office, or owes the balance (art. 187) |
| Employer did not withhold, or too little | Employer pays the missing amount, recovers it from staff, and bears the art. 671 penalty, which cannot be recovered (art. 188) |
| Pensions and life annuities | No 30% abatement (art. 168 b) |
| Request for a 6% expatriate CFCE | Refuse: CFCE is 3% (art. 267) |
| Request for a 1,800,000 abatement cap | Refuse: the cap is 900,000 (art. 182) |

### Defaults when a fact is missing

| Unknown | Default | Why |
|---|---|---|
| Family situation or parts | 1 part (single, no dependants) | Highest IRPP; never grant unevidenced parts |
| Spouse income, for TRIMF | Charge the band amount twice until the spouse's income is evidenced | Art. 276 covers a spouse without income |
| Residence | Resident only if confirmed; otherwise flag | Non-resident rules differ |
| Unclassified bank narration | Ask; do not guess | Institutions vary |

### Bank statement narrations

| Narration | Classification |
|---|---|
| `SALAIRE`, `PAIE`, `VIREMENT SALAIRE`, `NET A PAYER` | Net salary payment |
| `ACOMPTE`, `AVANCE SUR SALAIRE` | Salary advance (recoverable, not income) |
| `PRIME`, `BONUS`, `GRATIFICATION` | Bonus, taxable through IRPP and TRIMF at source |
| `INDEMNITE TRANSPORT`, `INDEMNITE` | Allowance, check taxability (arts. 166, 167) |
| `RAPPEL SALAIRE` | Back pay |
| `DGID`, `IMPOTS`, `RETENUE SOURCE`, `IR RETENUE`, `F4` | IRPP and TRIMF withholding paid to the DGID |
| `CFCE` | Employer flat contribution (3%) |
| `IPRES`, `RETRAITE`, `CSS`, `PRESTATIONS FAMILIALES`, `ACCIDENT TRAVAIL`, `IPM`, `PREVOYANCE MALADIE` | Social contributions: see [senegal-social-contributions](senegal-social-contributions.md) |
| `VIREMENT SALAIRES`, `MASSE SALARIALE` | Net wages paid out |

Terms: salaire brut (gross), net a payer (net pay), retenue a la source (withholding), bulletin de paie (payslip), parts and reduction pour charges de famille (family reduction on the tax), cadre (executive), masse salariale (wage bill).

### Working paper columns (one row per employee, XOF)

Gross; benefits in kind; total gross; abatement `MIN(0.30*gross*12, 900000)/12`; monthly IRPP base; parts; IRPP (bands on base times 12, less the art. 174 reduction, capped at 43%, divided by 12); TRIMF (art. 282 lookup on gross times 12, doubled for a spouse without income, divided by 12); employee social shares (from the social contributions skill); net pay; CFCE `0.03*gross`; employer social shares; total employer cost. Add a row summing IRPP, TRIMF and CFCE for the monthly declaration.

## Worked cases

All in XOF, 1 part unless stated. Monthly figures divide the annual tax by 12.

**Example A, 200,000 a month, single.** Gross 2,400,000; abatement 720,000 (under the cap); base 1,680,000; IRPP 174,000 + 180,000 x 30% = 228,000 a year (19,000 a month). TRIMF 12,000 a year (band 2,000,000 to 6,999,999). CFCE 6,000 a month.

**Example D, low pay of 64,300 a month, single.** Gross 771,600; abatement 231,480; base rounded down to 540,000, inside the 0% band: no IRPP. TRIMF is still due: 3,600 a year (band 600,000 to 999,999). CFCE 1,929 a month.

**Case 1, 500,000 a month, single (Example B).** Gross 6,000,000; abatement 1,800,000 capped at 900,000; base 5,100,000; IRPP 924,000 + 1,100,000 x 35% = 1,309,000 a year, 109,083.33 a month. TRIMF 12,000 a year. CFCE 15,000 a month.

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

**Case 2, a decision: does the spouse's income change the withholding? (Example C).** A cadre on 1,000,000 a month, married, 2 children. Gross 12,000,000; abatement capped at 900,000; base 11,100,000; tax from the bands 2,324,000 + 3,100,000 x 37% = 3,471,000.

- Spouse has income: 2.5 parts, reduction 20% x 3,471,000 = 694,200 (inside 300,000 to 1,100,000); IRPP 2,776,800 a year (231,400 a month); TRIMF 36,000 once.
- Spouse has no income: 3 parts, reduction 25% x 3,471,000 = 867,750 (inside 400,000 to 1,650,000); IRPP 2,603,250 a year; TRIMF 72,000 (charged for the spouse too, art. 276).

The spouse's income is the figure that decides: get it in writing before granting the half part. Both results are below 43% of 11,100,000.

```oa-check
name: Payroll example C, 1,000,000 a month, spouse with and without income
inputs:
  gross: 12000000
steps:
  - abatement: min(gross * 0.30, 900000)
  - base: gross - abatement
  - bands: 2324000 + (base - 8000000) * 0.37
  - reduction: min(max(bands * 0.20, 300000), 1100000)
  - tax: bands - reduction
  - monthly: tax / 12
  - reduction_3: min(max(bands * 0.25, 400000), 1650000)
  - tax_3: bands - reduction_3
expected:
  tax: 2776800.00
  monthly: 231400.00
  tax_3: 2603250.00
```

## When to refuse or refer

| Trigger | Response |
|---|---|
| No gross pay | Refuse to compute |
| Parts claimed without evidence | Default to 1 part; maximum 5 (art. 174) |
| Request for a 6% expatriate CFCE | Refuse: 3% (art. 267) |
| Treaty relief for a non-resident | Refer to a Senegal expert-comptable |
| Exact IPRES, CSS or IPM figures | See the social contributions skill; those rates are not yet confirmed from an official source |
| Output to be treated as filed advice | Refuse: estimate only, needs sign-off by a Senegal expert-comptable |

Never divide income by parts; never treat TRIMF as monthly; never apply an IRPP floor; never present a computation as final.

## Filing and payment

| Item | Detail | Source |
|---|---|---|
| Monthly withholding (IRPP, TRIMF, CFCE) | First 15 days of the next month, with the art. 186 declaration (called form F4 in practice; the CGI does not use the name); quarterly for real simplified and CGU employers | CGI arts. 185, 186, 268 |
| Annual salary statement | During January, Etat 1024 and annexes; one more month on request for firms with 300 or more staff or several sites | CGI art. 191; DGID calendar of annual filings |
| December withholding | Paid within the time for the art. 191 statement | CGI art. 186 |
| Employee's own annual return | Before 1 May; compulsory for an employee with several employers, with non-salary income not taxed finally, or where withholding was omitted (arts. 60, 196); otherwise only on request (art. 197) | CGI |
| Refund of over-withheld IRPP | Claim before 1 April of the next year | CGI art. 187 |
| Pay records | Keep to the end of the 11th following year | CGI art. 184 |

Penalties: see the rates table (arts. 665, 667, 671); a repeat offence doubles fines and penalties (art. 671 VII).

## Completion checklist

- Gross, benefits and parts evidenced; spouse income known.
- Abatement capped at 900,000; no extra social deduction.
- Bands, reduction, 43% cap applied; TRIMF added on top.
- CFCE at 3% unless an exemption is documented.
- Social contributions added from the social contributions skill.
- Remittance date set (monthly or quarterly); January statement diarised.
- Output labelled as an estimate for review.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): read arts. 60, 165 to 199 (abatement, scale, parts, withholding, remittance), 263 to 269 (CFCE), 275 to 282 (TRIMF table) and 665 to 671 (interest and penalties) in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-14 |
| DGID calendar of annual filings: read the salary statement (Etat 1024, art. 191) entry | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-14 |
| DGID, Lois et reglements: read the rates table (income tax scale, CFCE 3%) for 2026 | https://www.dgid.sn/loi-reglement | 2026-11-14 |

Not yet confirmed: whether art. 276 means the TRIMF band amount is charged twice for a spouse without income (the article says the employee is taxed "pour lui-meme et son conjoint ne disposant pas de revenus"; a Senegal accountant must confirm); dividing the annual tax by 12 is our working method for monthly withholding, the articles read give no monthly formula; SMIG of XOF 371 an hour and SMAG of XOF 237 an hour since 1 July 2023 (the decrees were not read and the only source seen was a foreign liaison body); the text of Loi 2025-17 was not opened. IPRES, CSS and IPM rates are listed in the social contributions skill.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `senegal-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/senegal-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
