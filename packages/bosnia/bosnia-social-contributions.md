---
name: bosnia-social-contributions
description: "Use this skill whenever asked about Bosnia and Herzegovina (BiH) payroll social security contributions, salary taxes, or personal income tax withholding. Trigger on phrases like \"how much social contributions in Bosnia\", \"BiH payroll\", \"Federation of BiH contributions\", \"Republika Srpska contributions\", \"doprinosi\", \"MIO/PIO\", \"PIO/MIO\", \"Brcko District payroll\", \"BiH net to gross\", \"gross to net salary Bosnia\", \"FBiH employer contributions 5%\", \"RS 32.8% contributions\", \"BiH personal income tax\", \"porez na dohodak\", \"BAM salary tax\", \"do I pay social security in Bosnia\", or any question about computing Bosnian payroll deductions, employer on-costs, or PIT withholding. CRITICAL: Bosnia and Herzegovina has NO single nationwide payroll/social-security system — contributions and PIT are set and collected at ENTITY level (Federation of BiH, Republika Srpska, Brcko District) with materially different rates and bases. ALWAYS branch on entity before computing. Also trigger when classifying bank-statement transactions that relate to payroll-tax payments to Porezna uprava FBiH, Poreska uprava RS, entity pension/health funds, or UINO (VAT). ALWAYS read this skill before touching any BiH social-contributions or payroll work."
version: 0.1
jurisdiction: BA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina Social Security Contributions & Payroll

## Bosnia and Herzegovina Social Security Contributions & Payroll Skill v0.1

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

> **STOP — entity branch first.** Bosnia and Herzegovina is a federal state with THREE separate payroll/PIT regimes. You CANNOT compute anything until you know which entity applies: **Federation of BiH (FBiH)**, **Republika Srpska (RS)**, or **Brcko District (BD)**. Only VAT is unified nationally.

**Quick reference fields**  _(authority and legislation per the research brief; PwC Worldwide Tax Summaries (https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes); UINO (https://www.uino.gov.ba/portal/en/news/the-threshold-for-entering-the-vat-system-has-been-increased-to-bam-100-000/).)_

| Field | Value |
| --- | --- |
| Country | Bosnia and Herzegovina (BiH) |
| ISO code | BA |
| Currency | Convertible Mark (BAM / KM) only |
| Tax year | 2025 |
| FBiH legislation | Law on Contributions of FBiH (Zakon o doprinosima FBiH), as amended by the Law published in the Official Gazette of FBiH on 7 May 2025, applicable from 1 July 2025; Law on Personal Income Tax of FBiH (flat 10%) |
| RS legislation | Law on Contributions of RS (Zakon o doprinosima RS); Law on Personal Income Tax of RS (flat 8%) |
| BD legislation | Law on Personal Income Tax of Brcko District (flat 10%) |
| National (VAT) legislation | Law on Value Added Tax of BiH (Official Gazette of BiH no. 80/23) |
| FBiH authority | Tax Administration of FBiH (Porezna uprava FBiH, www.pufbih.ba) + entity pension fund (FZ MIO/PIO), health fund, employment service |
| RS authority | Tax Administration of Republika Srpska (Poreska uprava RS, www.poreskaupravars.org) |
| BD authority | Brcko District Tax Administration |
| VAT authority (national) | Indirect Taxation Authority (Uprava za indirektno oporezivanje / UINO, www.uino.gov.ba) |
| Contribution base | Gross salary (all entities). FBiH disaster + water charges are on NET salary |
| Withholding | PAYE-style: employer calculates and withholds both contributions and PIT at source each salary payment |
| Validated by | Pending — requires sign-off by a BiH-licensed tax advisor / certified accountant |
| Validation date | Pending |

**Headline rate overview (per entity)**  _(PwC (https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes and .../taxes-on-personal-income); FBiH employer cut per Orbitax (https://orbitax.com/news/archive.php/Federation-of-Bosnia-and-Herze-58893) and Unija (https://unija.com/en/amendments-to-the-law-on-contibutions-in-the-fbih/).)_

| Item | FBiH | RS | BD |
| --- | --- | --- | --- |
| Employee social contributions (on gross) | 31.0% | 32.8% | 12.0% health + pension fund election |
| Employer social contributions (on gross) | 5.0% (from 1 Jul 2025) | 0% (none) | per elected pension fund |
| FBiH-only extra employer charges (on NET) | 0.5% disaster + 0.5% water | n/a | n/a |
| Personal income tax (flat) | 10% | 8% | 10% |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown entity | STOP -- do not compute. Ask which entity (FBiH / RS / BD) applies based on place of work/residence |
| Entity known but pay-period date unknown (FBiH) | STOP -- FBiH employer rates changed on 1 Jul 2025; confirm pay date before computing |
| Pay date on/after 1 Jul 2025 (FBiH employer) | Apply reduced employer rates totalling 5.0% |
| Pay date before 1 Jul 2025 (FBiH employer) | Apply old employer rates totalling 10.5% |
| Unknown personal allowance / dependants (FBiH PIT) | Apply basic allowance only; flag dependants for reviewer |
| RS personal allowance / deduction unknown | [RESEARCH GAP — reviewer to confirm RS personal deduction] |
| Contribution base ambiguous | Use gross salary; FBiH disaster + water charges on net salary only |
| BD pension fund election unknown | STOP -- ask whether the individual elected the RS or FBiH pension fund |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- (1) the **entity** (FBiH / RS / BD), (2) **gross monthly salary in BAM**, and (3) for FBiH, the **pay-period date** (to pick the correct employer rate set). Without the entity, STOP.

**Recommended** -- residency/place of work confirming the entity; number of dependants and disability status (FBiH PIT personal allowance); for BD, the elected pension fund (RS or FBiH).

**Ideal** -- prior payslips, the employer's monthly salary/tax specification, and the entity tax-administration registration confirming fund membership.

### Refusal catalogue

- **R-BA-SSC-1 -- Entity unknown** — Trigger: the applicable entity (FBiH / RS / BD) is not provided. Message: "Bosnia and Herzegovina has three separate payroll regimes with materially different contribution and PIT rates. The entity (Federation of BiH, Republika Srpska, or Brcko District) is mandatory before any computation. Cannot proceed without it."
- **R-BA-SSC-2 -- FBiH pay-period date unknown** — Trigger: FBiH payroll where the pay date in 2025 is not given. Message: "FBiH employer contribution rates fell from 10.5% to 5.0% effective 1 July 2025. 2025 payrolls straddle two rate sets. Confirm the pay-period date before computing employer on-costs."
- **R-BA-SSC-3 -- Contribution minimum/maximum base** — Trigger: salary is near the minimum wage or unusually high and a contribution floor/ceiling may bite. Message: "A minimum contribution base (linked to the minimum/average wage) applies; any annual ceiling was not pinned to a primary figure. [RESEARCH GAP — reviewer to confirm the applicable floor/ceiling with the entity tax administration] before relying on the computation."
- **R-BA-SSC-4 -- RS small-entrepreneur / FBiH self-employment specifics** — Trigger: client is a sole trader / small entrepreneur rather than an employee. Message: "Self-employed and small-entrepreneur regimes (e.g. RS 2% on annual revenue) differ from employee payroll. Escalate to a BiH-licensed advisor; this skill computes employee payroll."
- **R-BA-SSC-5 -- Cross-entity or expat arrangements** — Trigger: worker is posted across entities, is a non-resident, or has dual fund membership. Message: "Cross-entity postings, non-resident workers, and totalisation/treaty questions require case-specific confirmation. Escalate to a BiH-licensed advisor."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to BiH payroll taxes and contributions. When a transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty/reference. Contribution and PIT payments always EXCLUDE from any VAT return — they are statutory payroll obligations, not taxable supplies.

### 3.1 FBiH payroll-tax / contribution payments

**3.1 FBiH payroll-tax / contribution payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| POREZNA UPRAVA FBIH, PU FBIH, PUFBIH | EXCLUDE -- payroll tax/contribution remittance | FBiH Tax Administration |
| DOPRINOSI, DOPRINOS | EXCLUDE -- social contributions | "Contributions" in local language |
| MIO, PIO, MIO/PIO, FZ MIO | EXCLUDE -- pension/disability contribution | FBiH pension fund |
| ZDRAVSTVENO, ZZO | EXCLUDE -- health insurance contribution | Health fund |
| NEZAPOSLENOST, ZAPOSLJAVANJE | EXCLUDE -- unemployment contribution | Employment service |
| POREZ NA DOHODAK | EXCLUDE -- personal income tax (not a contribution) | PIT withholding |

### 3.2 Republika Srpska payroll-tax / contribution payments

**3.2 Republika Srpska payroll-tax / contribution payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PORESKA UPRAVA RS, PU RS | EXCLUDE -- payroll tax/contribution remittance | RS Tax Administration |
| DOPRINOSI RS, DOPRINOS | EXCLUDE -- social contributions | RS unified contribution |
| PIO RS, FOND PIO | EXCLUDE -- pension/disability contribution | RS pension fund |
| ZDRAVSTVO RS, FOND ZDRAVSTVA | EXCLUDE -- health insurance contribution | RS health fund |
| DJECIJA ZASTITA, DJEČJA ZAŠTITA | EXCLUDE -- child protection contribution | RS-specific |

### 3.3 Brcko District payroll payments

**3.3 Brcko District payroll payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BRCKO DISTRIKT, BD POREZ | EXCLUDE -- BD payroll tax | Brcko District Tax Administration |
| ZDRAVSTVO BD | EXCLUDE -- BD health contribution | 12.0% health on gross |

### 3.4 National VAT payments (NOT payroll — do not confuse)

**3.4 National VAT payments (NOT payroll — do not confuse)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UINO, UPRAVA ZA INDIREKTNO OPOREZIVANJE | EXCLUDE -- VAT/indirect tax | National authority, not payroll |
| PDV, PDV PRIJAVA | EXCLUDE -- VAT | "PDV" = VAT |

### 3.5 Salary and payroll movements (exclude from contribution classification)

**3.5 Salary and payroll movements (exclude from contribution classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLATA, PLAĆA, NETO PLATA (outgoing) | EXCLUDE -- payroll/wage expense | Net salary disbursement, not a contribution |
| PLATA, PLAĆA (incoming) | EXCLUDE -- employment income received | Not a contribution payment |
| PENZIJA, PENZIJSKO (incoming) | EXCLUDE -- pension income received | Benefit received, not a contribution |

## Section 4 -- Worked examples

Five bank-statement / payslip classifications for hypothetical BiH employees, in BAM. **All figures recomputed below.**

### Example 1 -- FBiH employee, gross BAM 2,000, pay date Aug 2025 (post-1-Jul-2025 employer rates)

**Input line:**
`31.08.2025 ; POREZNA UPRAVA FBIH ; DEBIT ; DOPRINOSI + POREZ 08/2025 ; -758.00 ; BAM`

**Reasoning (gross BAM 2,000, single, basic FBiH allowance BAM 1,000/month):**
- Employee contributions = 2,000 x 31.0% = **BAM 620.00** (pension 17.0% = 340.00 + health 12.5% = 250.00 + unemployment 1.5% = 30.00; 340 + 250 + 30 = 620 ✓)
- PIT base = gross − employee contributions − personal allowance = 2,000 − 620 − 1,000 = **BAM 380.00**
- PIT (10%) = 380.00 x 10% = **BAM 38.00**
- Employee deductions total remitted (contributions + PIT) = 620.00 + 38.00 = **BAM 658.00**
- Net pay to employee = 2,000 − 620 − 38 = **BAM 1,342.00**
- Employer social contributions (post-1-Jul-2025) = 2,000 x 5.0% = **BAM 100.00** (pension 2.5% = 50.00 + health 2.0% = 40.00 + unemployment 0.5% = 10.00; 50 + 40 + 10 = 100 ✓)
- FBiH net-based charges: disaster 0.5% x 1,342.00 = **BAM 6.71**; water 0.5% x 1,342.00 = **BAM 6.71**
- The combined remittance shown (BAM 758.00) = employee deductions 658.00 + employer social 100.00 = **758.00 ✓** (the 0.5% + 0.5% net charges of 13.42 are typically remitted separately to FBiH funds).

**Classification:** EXCLUDE from VAT -- FBiH payroll remittance (contributions + PIT). Record net pay BAM 1,342.00 as payroll expense; employer on-cost BAM 100.00 + BAM 13.42 net charges as employer payroll cost.

### Example 2 -- FBiH employee, gross BAM 2,000, pay date May 2025 (PRE-1-Jul-2025 employer rates)

**Input line:**
`31.05.2025 ; PU FBIH ; DEBIT ; DOPRINOSI POSLODAVAC 05/2025 ; -210.00 ; BAM`

**Reasoning:**
- Same employee side as Example 1 (employee 620.00, PIT 38.00, net 1,342.00).
- Employer social contributions PRE-1-Jul-2025 = 2,000 x 10.5% = **BAM 210.00** (pension 6.0% = 120.00 + health 4.0% = 80.00 + unemployment 0.5% = 10.00; 120 + 80 + 10 = 210 ✓).
- The reference is the employer-side remittance only (BAM 210.00). Demonstrates the effective-date branch: same gross, employer cost is BAM 210.00 before 1 Jul vs BAM 100.00 from 1 Jul.

**Classification:** EXCLUDE from VAT -- FBiH employer contribution remittance (old rate set). Confirm pay-period date drives the rate.

### Example 3 -- Republika Srpska employee, gross BAM 2,000

**Input line:**
`10.06.2025 ; PORESKA UPRAVA RS ; DEBIT ; DOPRINOSI 05/2025 ; -656.00 ; BAM`

**Reasoning (RS):**
- Employee contributions = 2,000 x 32.8% = **BAM 656.00** (pension 18.5% = 370.00 + health 12.0% = 240.00 + unemployment 0.6% = 12.00 + child protection 1.7% = 34.00; 370 + 240 + 12 + 34 = 656 ✓)
- RS has NO employer-side social contributions.
- RS PIT (flat 8%) base = gross − contributions − personal deduction. RS personal deduction figure is **[RESEARCH GAP — reviewer to confirm RS personal deduction]**. If, for illustration only, no deduction were applied: PIT = (2,000 − 656) x 8% = 1,344 x 8% = BAM 107.52. DO NOT rely on this PIT figure until the RS personal deduction is confirmed.
- The DOPRINOSI line of BAM 656.00 (contributions only) reconciles to the 32.8% rate. ✓

**Classification:** EXCLUDE from VAT -- RS contribution remittance. PIT figure flagged pending RS personal deduction.

### Example 4 -- Brcko District employee, gross BAM 2,000, elected RS pension fund

**Input line:**
`12.06.2025 ; BRCKO DISTRIKT ; DEBIT ; ZDRAVSTVO + PIO 05/2025 ; -... ; BAM`

**Reasoning (BD):**
- BD health insurance = 2,000 x 12.0% = **BAM 240.00** (on gross).
- Pension: the individual elects to pay into either the RS or FBiH pension fund. If RS fund elected, the RS pension rate (18.5%) applies = 2,000 x 18.5% = **BAM 370.00**. If FBiH fund elected, the FBiH employee pension rate (17.0%) applies = 2,000 x 17.0% = **BAM 340.00**.
- Other BD contribution components (unemployment, etc.) and the BD PIT personal allowance were not pinned to a primary figure: **[RESEARCH GAP — reviewer to confirm full BD contribution stack and personal allowance]**.
- BD PIT is flat 10% on the post-deduction base; do NOT apply FBiH disaster/water charges in BD.

**Classification:** EXCLUDE from VAT -- BD payroll remittance. STOP and confirm the elected pension fund before finalising.

### Example 5 -- National VAT remittance (NOT payroll -- do not confuse)

**Input line:**
`10.07.2025 ; UINO ; DEBIT ; PDV 06/2025 ; -1,700.00 ; BAM`

**Reasoning:**
- Matches "UINO" / "PDV" (pattern 3.4). This is a VAT remittance to the national Indirect Taxation Authority, NOT a payroll contribution or PIT. VAT is a single 17% standard rate. Do not classify as social security.

**Classification:** EXCLUDE from VAT return as a payroll item -- this IS the VAT payment itself. NOT a contribution; do not record in payroll computations.

## Section 5 -- Tier 1 rules

These rules apply when the entity is known, inputs are complete, and (for FBiH) the pay-period date is known. Apply exactly as written. All rates from PwC unless noted.

### Rule 1 -- Branch on entity FIRST

- **Branch on entity first** — There is no nationwide payroll/social-security system. Determine FBiH / RS / BD before any calculation.  _(Research brief; PwC.)_

### Rule 2 -- FBiH employee contributions = 31.0% of gross

- **FBiH employee contributions** — 31.0% percent (Pension/disability (MIO/PIO) 17.0% + health 12.5% + unemployment 1.5%, all on gross salary)  _(PwC: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes)_

### Rule 3 -- FBiH employer contributions = 5.0% from 1 Jul 2025 (was 10.5%)

- **FBiH employer contributions** — 5.0% from 1 July 2025 (pension 2.5% + health 2.0% + unemployment 0.5%); 10.5% before 1 July 2025 (pension 6.0% + health 4.0% + unemployment 0.5%) percent  _(Orbitax: https://orbitax.com/news/archive.php/Federation-of-Bosnia-and-Herze-58893; Unija: https://unija.com/en/amendments-to-the-law-on-contibutions-in-the-fbih/)_

### Rule 4 -- FBiH extra employer charges are on NET salary

- **FBiH extra employer charges on net salary** — Protection from natural/other disasters 0.5% + water protection charge 0.5%, both levied on net salary. Do NOT apply these in RS or BD.  _(PwC: .../individual/other-taxes)_

### Rule 5 -- RS employee contributions = 32.8% of gross; no employer contributions

- **RS employee contributions** — 32.8% percent (Pension/disability 18.5% + health 12.0% + unemployment 0.6% + child protection 1.7%. No employer-side social contributions in RS.)  _(PwC: .../individual/other-taxes)_

### Rule 6 -- Brcko District = 12.0% health on gross + pension fund election

- **BD contribution rule** — BD: 12.0% health insurance on gross; for pension the individual elects to pay into either the RS or FBiH pension fund (use that fund's pension rate).  _(PwC: .../individual/other-taxes)_

### Rule 7 -- Personal income tax is flat and entity-specific

- **Personal income tax by entity** — FBiH 10%, RS 8%, Brcko District 10% percent  _(PwC: .../individual/taxes-on-personal-income)_

### Rule 8 -- FBiH PIT base

- **FBiH PIT base formula** — FBiH PIT base = gross salary − employee social contributions − personal allowance. PIT is withheld monthly by the employer at salary payment.  _(PwC; Rivermate: https://rivermate.com/guides/bosnia-and-herzegovina/taxes)_

### Rule 9 -- FBiH basic personal allowance (licni odbitak) = BAM 1,000/month for 2025

- **FBiH basic personal allowance** — BAM 1,000/month for 2025 (with additional allowances for dependent family members and disability. Secondary source — [RESEARCH GAP — reviewer to confirm exact 2025 figure and dependant/disability coefficients against the FBiH Law on Personal Income Tax / Porezna uprava FBiH])  _(Rivermate)_

### Rule 10 -- Gross salary is the contribution base in all entities

- **Contribution base rule** — All social contributions in FBiH, RS and BD use gross salary as the base. Only the FBiH disaster/water charges use net salary.  _(PwC: .../individual/other-taxes)_

### Rule 11 -- PAYE-style withholding

- **PAYE-style withholding rule** — The employer is the income payer / withholding agent and calculates and withholds both contributions and PIT at source with each salary payment.  _(PwC tax administration)_

### Rule 12 -- Monthly reporting and payment deadlines

**Monthly reporting and payment deadlines**  _(PwC tax administration: https://taxsummaries.pwc.com/Bosnia-and-Herzegovina/Individual/Tax-administration; UINO.)_

| Item | Entity | Deadline |
| --- | --- | --- |
| Contributions + PIT payment | FBiH | With salary payment, no later than the end of the following month |
| Salary/tax specification | FBiH | On the payment day, no later than one day after payment |
| Salary-tax specification | RS | By the 10th day of the following month |
| VAT return (PDV prijava) | National (UINO) | By the 10th day of the month following the period |

### Rule 13 -- Annual PIT return deadlines

- **Annual PIT return deadlines** — FBiH and RS annual PIT returns due 31 March of the following year; Brcko District annual return due 28 February (not required if all PIT settled via monthly withholding).  _(PwC tax administration.)_

### Rule 14 -- Minimum wage 2025 (drives minimum contribution base)

- **Minimum wage 2025** — FBiH: BAM 1,000/month net (raised from BAM 620 from 1 Jan 2025). RS: tiered by education — BAM 900 net (BAM 1,344.26 gross) basic; BAM 950 net (1,426.23 gross) for 3-yr secondary; BAM 1,000 net (1,508.20 gross) for 4-yr secondary; BAM 1,300 net (2,000 gross) for higher education.  _(WageIndicator: https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2025/minimum-wage-updated-in-the-federation-of-bosnia-and-herzegovina-from-01-january-2025-may-02-2025; WageIndicator: https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2025/minimum-wage-updated-in-republika-srpska-bosnia-and-herzegovina-from-01-january-2025-may-04-2025)_

### Rule 15 -- VAT is national, flat 17%, threshold BAM 100,000

- **VAT national flat rate and threshold** — Corporate income tax is flat 10% nationwide; VAT is a single standard rate of 17% with no reduced rate, administered by UINO. Mandatory VAT registration once taxable supplies exceed (or are likely to exceed) BAM 100,000/year (raised from BAM 50,000 effective 2 Dec 2023).  _(Mondaq tax card 2026: https://www.mondaq.com/withholding-tax/1747486/bosnia-herzegovina-tax-card-2026; PwC corporate other taxes; UINO.)_

## Section 6 -- Tier 2 catalogue

When the entity is known but circumstances are ambiguous, flag these for reviewer confirmation rather than computing automatically.

### T2-1 -- FBiH payroll straddling 1 July 2025

- **T2-1** — Trigger: FBiH payroll covering a period that spans or sits near 1 July 2025. Issue: Employer rate fell from 10.5% to 5.0% on 1 July 2025. The applicable rate depends on the pay-period date, not the work month in some interpretations. Action: Flag for reviewer. Confirm exact pay date and the entity's transition guidance.

### T2-2 -- Minimum / maximum contribution base

- **T2-2** — Trigger: Salary at or below the entity minimum wage, or unusually high. Issue: A minimum contribution base (linked to the minimum/average wage) applies; any annual ceiling was not pinned to a primary figure. Action: [RESEARCH GAP — reviewer to confirm floor/ceiling with the entity tax administration] before computing.

### T2-3 -- FBiH dependant / disability allowances

- **T2-3** — Trigger: Client claims allowances for dependent family members or disability. Issue: The basic BAM 1,000/month allowance is from a secondary source; dependant/disability coefficients were not pinned. Action: Flag for reviewer; confirm against the FBiH Law on Personal Income Tax.

### T2-4 -- RS personal deduction for PIT

- **T2-4** — Trigger: Computing RS PIT (8%) net of any personal deduction. Issue: The RS personal deduction figure was not captured from a primary source. Action: [RESEARCH GAP — reviewer to confirm RS personal deduction]; do not finalise RS PIT without it.

### T2-5 -- Brcko District full contribution stack

- **T2-5** — Trigger: BD payroll beyond health + elected pension. Issue: Only 12.0% health on gross and the pension-fund election are pinned; other BD components and the BD personal allowance were not. Action: [RESEARCH GAP — reviewer to confirm full BD contribution stack and personal allowance].

### T2-6 -- Self-employed / small-entrepreneur regimes

- **T2-6** — Trigger: Sole trader, freelancer, or RS small entrepreneur (2% on annual revenue). Issue: These regimes differ from employee payroll and are outside this skill's compute core. Action: Escalate to a BiH-licensed advisor.

## Section 7 -- Excel working paper template

When producing a BiH payroll computation, structure the working paper as follows:

```
BiH PAYROLL / SSC COMPUTATION -- WORKING PAPER
Client: [name]
Entity: [FBiH / RS / BD]            <-- MUST be set before computing
Tax Year: 2025
Pay-period date: [____]            <-- FBiH: drives employer rate set
Prepared: [date]

INPUT DATA
  Gross monthly salary (BAM):       [____]
  Personal allowance (BAM):         [FBiH 1,000 / RS gap / BD gap]
  Dependants / disability:          [____]
  Pay date on/after 1 Jul 2025:     [YES/NO]   (FBiH only)
  BD elected pension fund:          [RS / FBiH]  (BD only)

EMPLOYEE CONTRIBUTIONS (on gross)
  FBiH:  pension 17.0% + health 12.5% + unemployment 1.5% = 31.0%
  RS:    pension 18.5% + health 12.0% + unemploy 0.6% + child 1.7% = 32.8%
  BD:    health 12.0% + elected pension (RS 18.5% or FBiH 17.0%)
  Employee contributions (BAM):     [____]

EMPLOYER CONTRIBUTIONS (on gross)
  FBiH (from 1 Jul 2025): 2.5% + 2.0% + 0.5% = 5.0%
  FBiH (before 1 Jul 2025): 6.0% + 4.0% + 0.5% = 10.5%
  RS:    none
  Employer contributions (BAM):     [____]

FBiH NET-BASED CHARGES (employer)
  Net salary (BAM):                 [____]
  Disaster 0.5% + Water 0.5%:       [____]

PERSONAL INCOME TAX
  PIT base = gross − employee contributions − personal allowance (FBiH)
  PIT rate: FBiH 10% / RS 8% / BD 10%
  PIT (BAM):                        [____]

RESULTS
  Net pay to employee (BAM):        [____]
  Total employer cost (BAM):        [____]

REVIEWER FLAGS / RESEARCH GAPS
  [List any Tier 2 flags and [RESEARCH GAP] markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How BiH payroll-tax payments appear on bank statements

**Language note:** BiH uses Bosnian/Croatian/Serbian. Key terms: *doprinosi* = contributions; *porez na dohodak* = personal income tax; *plata/plaća* = salary; *neto/bruto* = net/gross; *PDV* = VAT; *MIO/PIO* = pension and disability insurance; *zdravstveno* = health; *nezaposlenost* = unemployment; *dječja zaštita* = child protection.

**Federation of BiH (FBiH):**
- Counterparty: "POREZNA UPRAVA FBIH" / "PU FBIH" / entity funds (FZ MIO/PIO, ZZO)
- References: "DOPRINOSI", "POREZ NA DOHODAK", a month code (e.g. "08/2025")
- Timing: monthly, with or just after salary payment

**Republika Srpska (RS):**
- Counterparty: "PORESKA UPRAVA RS" / "PU RS" / RS funds
- References: "DOPRINOSI", "DJECIJA ZASTITA"
- Timing: monthly; specification by the 10th of the following month

**Brcko District (BD):**
- Counterparty: "BRCKO DISTRIKT" / BD Tax Administration
- References: health + elected pension fund

**National VAT (UINO):**
- Counterparty: "UINO" / "UPRAVA ZA INDIREKTNO OPOREZIVANJE"
- Reference: "PDV"; due by the 10th of the following month — this is NOT a payroll item

**Key identification tips:**
1. Contribution/PIT debits are outgoing and recur monthly with consistent amounts unless salary changed.
2. Employer-side FBiH on-cost changes at 1 Jul 2025 (10.5% → 5.0%) — a step-down in the employer remittance mid-2025 is expected, not an error.
3. Do not confuse UINO/PDV (VAT) debits with payroll contributions.
4. RS has no employer-side social contribution remittance — only the employee 32.8% appears.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Identify the entity** -- counterparty name (POREZNA UPRAVA FBIH vs PORESKA UPRAVA RS vs BRCKO DISTRIKT) reveals it. If none present, STOP and ask.
2. **Scan for payroll-tax debits** -- match Section 3 patterns; separate contributions (doprinosi) from PIT (porez na dohodak) and VAT (PDV / UINO).
3. **Reverse-engineer the gross** (entity-specific):
   - FBiH: employee contributions ÷ 31.0% ≈ gross.
   - RS: employee contributions ÷ 32.8% ≈ gross.
   - BD: health ÷ 12.0% ≈ gross (then confirm pension fund election).
4. **Check the FBiH employer step-down** -- if employer remittance drops mid-2025, it likely reflects the 1 Jul 2025 cut.
5. **Flag for reviewer:** "Entity and gross derived from bank-statement amounts only. Personal allowance, minimum/maximum contribution base, and (FBiH) pay-date rate set have not been independently verified. Reviewer must confirm before relying on the computation."

## Section 10 -- Reference material

### Contribution rate tables (recomputed; totals verified)

**FBiH — employee (on gross)**  _(PwC .../individual/other-taxes)_

| Component | Rate | Source |
| --- | --- | --- |
| Pension / disability (MIO/PIO) | 17.0% | PwC .../individual/other-taxes |
| Health insurance | 12.5% | PwC .../individual/other-taxes |
| Unemployment insurance | 1.5% | PwC .../individual/other-taxes |
| **Total employee** | **31.0%** | 17.0 + 12.5 + 1.5 = 31.0 ✓ |

**FBiH — employer (on gross)**  _(Orbitax; Unija)_

| Component | From 1 Jul 2025 | Before 1 Jul 2025 | Source |
| --- | --- | --- | --- |
| Pension / disability | 2.5% | 6.0% | Orbitax; Unija |
| Health insurance | 2.0% | 4.0% | Orbitax; Unija |
| Unemployment insurance | 0.5% | 0.5% | Orbitax; Unija |
| **Total employer** | **5.0%** | **10.5%** | 2.5+2.0+0.5=5.0 ✓ ; 6.0+4.0+0.5=10.5 ✓ |

**FBiH — additional employer charges (on NET salary)**  _(PwC .../individual/other-taxes)_

| Component | Rate | Source |
| --- | --- | --- |
| Protection from natural/other disasters | 0.5% | PwC .../individual/other-taxes |
| Water protection charge | 0.5% | PwC .../individual/other-taxes |

**RS — employee (on gross); no employer-side contributions**  _(PwC .../individual/other-taxes)_

| Component | Rate | Source |
| --- | --- | --- |
| Pension / disability | 18.5% | PwC .../individual/other-taxes |
| Health insurance | 12.0% | PwC .../individual/other-taxes |
| Unemployment insurance | 0.6% | PwC .../individual/other-taxes |
| Child protection | 1.7% | PwC .../individual/other-taxes |
| **Total employee** | **32.8%** | 18.5+12.0+0.6+1.7=32.8 ✓ |

**Brcko District — employee (on gross)**  _(PwC .../individual/other-taxes)_

| Component | Rate | Source |
| --- | --- | --- |
| Health insurance | 12.0% | PwC .../individual/other-taxes |
| Pension | elected fund: RS 18.5% or FBiH 17.0% | PwC .../individual/other-taxes |
| Other components / allowance | [RESEARCH GAP — reviewer to confirm] | — |

### PIT, CIT and VAT (recomputed)

**PIT, CIT and VAT table**  _(PwC .../individual/taxes-on-personal-income; Mondaq tax card 2026; PwC corporate other taxes)_

| Tax | Jurisdiction | Rate / structure | Source |
| --- | --- | --- | --- |
| Personal income tax | FBiH | 10% flat | PwC .../individual/taxes-on-personal-income |
| Personal income tax | RS | 8% flat (small entrepreneurs 2% on annual revenue) | PwC .../individual/taxes-on-personal-income |
| Personal income tax | Brcko District | 10% flat | PwC .../individual/taxes-on-personal-income |
| Corporate income tax | BiH (nationwide) | 10% flat | Mondaq tax card 2026 |
| VAT | BiH (nationwide) | 17% single standard rate, no reduced rate | PwC corporate other taxes |

### Thresholds

**Thresholds table**  _(UINO; PwC; Rivermate)_

| Threshold | Amount | Detail | Source |
| --- | --- | --- | --- |
| VAT registration (national) | BAM 100,000 | Mandatory once taxable supplies exceed/likely exceed BAM 100,000/yr; raised from BAM 50,000 on 2 Dec 2023 | UINO: https://www.uino.gov.ba/portal/en/news/the-threshold-for-entering-the-vat-system-has-been-increased-to-bam-100-000/ |
| RS small-entrepreneur regime | 2% PIT on annual revenue | Alternative simplified PIT in RS | PwC .../individual/taxes-on-personal-income |
| FBiH basic personal allowance | BAM 1,000/month (2025) | Plus dependant/disability allowances | Rivermate (secondary); [RESEARCH GAP — confirm against FBiH PIT Law] |

### Filing & payment deadlines

**Filing & payment deadlines table**  _(PwC tax administration; UINO)_

| Form / item | Jurisdiction | Deadline | Source |
| --- | --- | --- | --- |
| Annual PIT return | FBiH | 31 March (following year) | PwC tax administration |
| Annual PIT return | RS | 31 March (following year) | PwC tax administration |
| Annual PIT return | Brcko District | 28 February (not required if all PIT settled via monthly withholding) | PwC tax administration |
| Monthly salary/tax specification | FBiH | On payment day, no later than one day after payment | PwC tax administration |
| Monthly contributions + PIT payment | FBiH | With salary payment, no later than end of following month | PwC tax administration |
| Monthly salary-tax specification | RS | By the 10th of the following month | PwC tax administration |
| VAT return (PDV prijava) | National (UINO) | By the 10th of the month following the period | UINO |

### Filing & payment deadlines

> **Form numbers note:** specific FBiH/RS form numbers (e.g. FBiH GIP/MIP/PMIP, RS forms) were not captured from authoritative sources — **[RESEARCH GAP — reviewer to confirm form numbers with the entity tax administrations]**.

### Penalties (VAT — national)

**Penalties (VAT — national) table**  _(PwC corporate other taxes)_

| Penalty | Rate / Amount | Source |
| --- | --- | --- |
| Failure to calculate/pay VAT | 50% of the VAT amount, minimum BAM 100 | PwC corporate other taxes |
| Failure to submit VAT declaration on time | BAM 300 | PwC corporate other taxes |

### Penalties (VAT — national)

> Payroll-contribution and PIT late-payment penalties at entity level were not pinned to a primary figure — **[RESEARCH GAP — reviewer to confirm entity-level payroll penalties]**.

### Test suite

**Test 1 -- FBiH, gross BAM 2,000, post-1-Jul-2025, single, allowance BAM 1,000.**
Employee contributions = 2,000 x 31.0% = **620.00**. PIT base = 2,000 − 620 − 1,000 = **380.00**. PIT = 380 x 10% = **38.00**. Net pay = 2,000 − 620 − 38 = **1,342.00**. Employer social = 2,000 x 5.0% = **100.00**. Disaster+water = 1,342 x 1.0% = **13.42**. Total employer cost = 2,000 + 100 + 13.42 = **2,113.42**.

**Test 2 -- FBiH, gross BAM 2,000, PRE-1-Jul-2025.**
Employee side identical to Test 1 (net 1,342.00). Employer social = 2,000 x 10.5% = **210.00**. Disaster+water = 1,342 x 1.0% = **13.42**. Total employer cost = 2,000 + 210 + 13.42 = **2,223.42**.

**Test 3 -- RS, gross BAM 2,000.**
Employee contributions = 2,000 x 32.8% = **656.00** (370.00 + 240.00 + 12.00 + 34.00). No employer contributions. PIT (8%) requires the RS personal deduction → **[RESEARCH GAP — reviewer to confirm RS personal deduction]**; illustrative-only with no deduction = (2,000 − 656) x 8% = 1,344 x 8% = **107.52** (do not rely).

**Test 4 -- BD, gross BAM 2,000, RS pension fund elected.**
Health = 2,000 x 12.0% = **240.00**. Pension (RS rate) = 2,000 x 18.5% = **370.00**. Remaining BD components + PIT allowance → **[RESEARCH GAP — reviewer to confirm]**.

**Test 5 -- BD, gross BAM 2,000, FBiH pension fund elected.**
Health = 2,000 x 12.0% = **240.00**. Pension (FBiH rate) = 2,000 x 17.0% = **340.00**. Remaining BD components + PIT allowance → **[RESEARCH GAP — reviewer to confirm]**.

**Test 6 -- FBiH, gross BAM 3,000, post-1-Jul-2025, single, allowance BAM 1,000.**
Employee contributions = 3,000 x 31.0% = **930.00**. PIT base = 3,000 − 930 − 1,000 = **1,070.00**. PIT = 1,070 x 10% = **107.00**. Net pay = 3,000 − 930 − 107 = **1,963.00**. Employer social = 3,000 x 5.0% = **150.00**. Disaster+water = 1,963 x 1.0% = **19.63**. Total employer cost = 3,000 + 150 + 19.63 = **3,169.63**.

**Test 7 -- VAT registration check.**
Taxable supplies BAM 120,000/yr → exceeds BAM 100,000 → mandatory VAT registration with UINO; VAT charged at 17%.

**Test 8 -- Entity unknown.**
Gross BAM 2,000, entity not stated → STOP. Refuse under R-BA-SSC-1; ask for the entity.

### Prohibitions

- NEVER compute BiH payroll without first establishing the entity (FBiH / RS / BD).
- NEVER apply one entity's rates to another — FBiH (31.0% / 5.0%), RS (32.8% / 0%), and BD (12.0% + elected pension) are not interchangeable.
- NEVER apply the FBiH employer rate without confirming the pay-period date (10.5% before 1 Jul 2025; 5.0% from 1 Jul 2025).
- NEVER apply FBiH disaster (0.5%) or water (0.5%) net-salary charges in RS or BD.
- NEVER add employer-side social contributions in RS — there are none.
- NEVER finalise RS or BD PIT without confirming the personal deduction/allowance (flagged research gaps).
- NEVER rely on the FBiH BAM 1,000 personal allowance, minimum/maximum contribution base, or entity form numbers without reviewer confirmation — they are secondary or unpinned.
- NEVER confuse UINO/PDV (national VAT) debits with entity payroll contributions.
- NEVER present BiH payroll figures as definitive — label as estimated and direct the client to the relevant entity tax administration.
- NEVER advise on self-employed, small-entrepreneur, cross-entity or expat arrangements with this skill — escalate to a BiH-licensed advisor.

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
