---
name: algeria-social-contributions
description: Use this skill whenever asked about Algeria social security / social insurance contributions (CNAS for salaried employees, CASNOS for self-employed/non-salaried) and the interaction with Algerian personal income tax (IRG). Trigger on phrases like "how much CNAS do I pay", "Algeria payroll contributions", "employer social security Algeria", "CNAS employee deduction", "CASNOS self-employed contribution", "G50 declaration", "DAS annual salary declaration", "IRG on salary", "Algerian minimum wage SNMG", "social security Algeria calculation", or any question about Algerian payroll, contribution or IRG obligations. Also trigger when classifying bank statement transactions that relate to CNAS/CASNOS debits, G50 tax payments, or DGI/Trésor payments from BNA, BEA, CPA, BADR, or other Algerian banks. This skill covers CNAS 26%/9% branch rates, the CASNOS 15% self-employed regime, the SNMG floor, IRG progressive brackets, G50/DAS filing and deadlines, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Algerian contribution or payroll work.
version: 0.1
jurisdiction: DZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Algeria Social Security / Social Insurance Contributions (CNAS / CASNOS)

## Algeria Social Security / Social Insurance Contributions (CNAS / CASNOS) Skill v0.1

> **Tier 2 (research-verified) skill.** Branch rates rely on CLEISS (authoritative French bilateral social-security source), corroborated by PwC Worldwide Tax Summaries and a 2025 Algerian payroll source. Primary Algerian authorities (CNAS, CASNOS, DGI/Ministère des Finances) were not directly fetched. Every figure carries an inline source or a `[RESEARCH GAP — reviewer to confirm]` marker. A warranted Algerian accountant must sign off before filing.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Algeria (People's Democratic Republic of Algeria) |
| Currency | Algerian Dinar (DZD) only |
| Salaried contribution authority | CNAS (Caisse Nationale des Assurances Sociales des travailleurs salariés) |
| Self-employed contribution authority | CASNOS (Caisse Nationale de Sécurité Sociale des Non-Salariés) |
| Tax authority (IRG/IBS) | DGI — Direction Générale des Impôts, Ministère des Finances (mfdgi.gov.dz) |
| Consolidated rate publisher | CLEISS (cleiss.fr) |
| Salaried total contribution | 35% of gross — 26% employer + 9% employee (CLEISS / PwC) |
| Self-employed (CASNOS) rate | 15% of declared annual income (7.5% insurance + 7.5% retirement) (CLEISS) |
| Minimum wage (SNMG) 2024–2025 | 20,000 DZD/month (CLEISS) |
| Minimum wage (SNMG) from 1 Jan 2026 | 24,000 DZD/month (+20%) (Radio Algérie / North Africa Post) |
| Personal income tax | IRG — progressive 0%–35% (PwC, FL 2022 schedule still current) |
| Salaried monthly IRG exemption | salaries ≤ 30,000 DZD/month effectively exempt (corroborated; see Section 10) |
| CNAS earnings ceiling | No general ceiling for salaried CNAS (CLEISS / PwC) |
| Salaried filing | G50 (tax, incl. IRG withheld) monthly by 20th; CNAS DAC monthly within first 10 days; DAS annual before 31 Jan |
| Validated by | Pending — requires sign-off by a warranted Algerian accountant |
| Validation date | Pending |

**Contribution regime overview**

| Regime | Who | Headline rate |
| --- | --- | --- |
| CNAS (salaried) | Employees and their employers | 26% employer + 9% employee = 35% of gross (CLEISS / PwC) |
| CASNOS (non-salaried) | Self-employed, professionals, traders | 15% of declared annual income (CLEISS) |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employment status (salaried vs self-employed) | STOP — CNAS and CASNOS regimes differ entirely; ask before computing |
| Salaried base unknown | Apply the SNMG floor (20,000 DZD/month for 2024–2025) as the minimum base |
| Self-employed declared income unknown | Apply the CASNOS floor (216,000 DZD/year) (CLEISS) |
| Tax year not stated | Assume 2025 (current research year); confirm SNMG/bracket year before filing |
| Unknown whether a DZD debit is CNAS or IRG/G50 | Classify by counterparty (CNAS vs Trésor/DGI); flag for reviewer if unclear |
| Construction/public-works/hydraulics sector add-on uncertain | Flag — an extra 0.375% unemployment add-on may apply (CLEISS) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- employment status (salaried vs non-salaried/self-employed) and gross monthly salary (CNAS) or declared annual income (CASNOS). Without employment status, STOP — the two regimes are not interchangeable.

**Recommended** -- the tax year, the employer's sector (construction/public works/hydraulics carries an add-on), and for IRG: residency status and any other Algeria-source income.

**Ideal** -- CNAS DAC declarations, G50 declarations, DAS annual salary declaration, payslips showing the 9% employee deduction and IRG withheld, and bank statements showing CNAS/CASNOS and Trésor/DGI debits.

### Refusal catalogue

- **R-DZ-SC-1** — Employment status unknown. Trigger: not stated whether the client is salaried (CNAS) or self-employed (CASNOS). Message: "Employment status is mandatory. Salaried workers contribute 35% via CNAS (26% employer / 9% employee, no ceiling); self-employed contribute 15% via CASNOS within an income band. These regimes are not interchangeable. Cannot proceed without this information."
- **R-DZ-SC-2** — Contribution arrears / penalties. Trigger: client has unpaid CNAS contributions from prior periods. Message: "Late CNAS contributions attract a 10% penalty plus 3% per month of delay (majoration de retard) and can trigger legal proceedings (CLEISS / Algerian payroll sources). Do not quantify arrears without a CNAS statement. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-3** — Sector add-ons and exemptions. Trigger: client is in construction, public works, hydraulics, or claims a reduced-rate scheme (e.g. ANSEJ/ANADE start-up exemptions). Message: "An additional 0.375% unemployment-branch contribution applies in construction/public works/hydraulics, and start-up/youth-employment schemes may carry temporary exemptions. These require case-specific confirmation. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-4** — Non-resident / expat payroll. Trigger: client is a non-resident, on a bilateral social-security agreement, or seconded into/out of Algeria. Message: "Bilateral social-security agreements and secondment relief are outside the scope of this skill. Non-residents are taxed only on Algeria-source professional income (PwC). Escalate to a warranted Algerian accountant."
- **R-DZ-SC-5** — IRG/tax penalty quantification. Trigger: request to quantify statutory IRG late-payment penalties. Message: "Specific statutory IRG late-payment penalty percentages are not confirmed from a primary authority in this skill `[RESEARCH GAP — reviewer to confirm against the Code des Impôts Directs, mfdgi.gov.dz]`. Do not estimate. Escalate to a warranted Algerian accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Algerian contributions and payroll tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statements may be in French or Arabic. Contribution and IRG payments always EXCLUDE from any VAT (TVA) return — they are statutory payroll/personal obligations, not business supplies.

### 3.1 CNAS salaried contribution debits

**CNAS salaried contribution debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNAS | EXCLUDE -- social contribution | Monthly DAC payment of the combined 35% (26% employer + 9% employee) |
| CAISSE NATIONALE ASSURANCES SOCIALES | EXCLUDE -- social contribution | Full CNAS name |
| COTISATION CNAS, COTISATIONS SOCIALES | EXCLUDE -- social contribution | "Contribution" reference |
| DAC, DECLARATION CNAS | EXCLUDE -- social contribution | DAC = the monthly CNAS declaration/payment |
| الضمان الاجتماعي (social security) | EXCLUDE -- social contribution | Arabic-language reference |

### 3.2 CASNOS self-employed contribution debits

**CASNOS self-employed contribution debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CASNOS | EXCLUDE -- self-employed contribution | 15% of declared annual income |
| CAISSE NON-SALARIES, NON SALARIES | EXCLUDE -- self-employed contribution | Full/abbreviated CASNOS reference |
| COTISATION CASNOS | EXCLUDE -- self-employed contribution | Contribution reference |

### 3.3 IRG / income tax payments (NOT a social contribution)

**IRG / income tax payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| G50, G-50, G 50 | EXCLUDE -- payroll tax (IRG withheld) | Monthly combined tax declaration, due 20th |
| IRG, IMPOT REVENU GLOBAL | EXCLUDE -- income tax | Not a CNAS/CASNOS contribution |
| TRESOR, RECETTE DES IMPOTS | EXCLUDE -- tax payment to the Treasury | DGI/Trésor counterparty |
| DGI, DIRECTION DES IMPOTS | EXCLUDE -- tax payment | Tax authority |
| IBS, IMPOT BENEFICES SOCIETES | EXCLUDE -- corporate tax | Company-level, not payroll contribution |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE -- payroll expense | Net wage transfer, not a CNAS payment |
| SALAIRE (incoming) | EXCLUDE -- employment income received | Not a contribution |
| الراتب (salary) | EXCLUDE -- payroll/salary | Arabic-language reference |

### 3.5 Benefits received (not contributions paid)

**Benefits received**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION CNR, RETRAITE | EXCLUDE -- pension income received | CNR pays pensions; not a contribution |
| ALLOCATION CHOMAGE, CNAC | EXCLUDE -- unemployment benefit received | Inbound benefit, not a contribution |
| ALLOCATIONS FAMILIALES | EXCLUDE -- family benefit received | Outside the contribution base entirely |

## Section 4 -- Worked examples

Six bank statement classifications from a hypothetical Algerian small employer and a self-employed professional. All amounts in DZD. Currency and figures per CLEISS / PwC research; SNMG 20,000 DZD/month (2024–2025).

### Example 1 -- Monthly CNAS contribution debit (BNA)

**Input line:**
`10.02.2025 ; CNAS COTISATION 01/2025 ; DEBIT ; DAC JANVIER ; -28,000.00 ; DZD`

**Reasoning:**
Matches "CNAS COTISATION" (pattern 3.1). This is the monthly DAC payment for January 2025. For a single SNMG-floor employee (base 20,000 DZD/month), total contribution = 35% × 20,000 × 4 employees ≈ 28,000 — or one employee at a higher base. Check headcount and base; the combined 35% (26% employer + 9% employee) is remitted together. Exclude from TVA. The employer 26% is a deductible payroll cost; the employee 9% was deducted from the worker's gross.

**Classification:** EXCLUDE from TVA -- CNAS social contribution.

### Example 2 -- Employee 9% deduction verification (single SNMG worker)

**Input line:**
`28.02.2025 ; VIREMENT SALAIRE FEVRIER ; DEBIT ; PAIE EMPLOYE ; -18,200.00 ; DZD`

**Reasoning:**
Matches "VIREMENT SALAIRE" (pattern 3.4) — a net wage transfer, not a contribution. Reconciliation: gross SNMG 20,000 DZD. Employee CNAS 9% = 20,000 × 0.09 = 1,800.00. IRG: monthly salary 20,000 ≤ 30,000 exemption threshold, so IRG ≈ 0 (see Section 10). Net = 20,000 − 1,800 − 0 = 18,200.00 DZD. The figure reconciles. This is payroll expense, not the employer's contribution remittance.

**Classification:** EXCLUDE from TVA -- net payroll expense. NOT a CNAS contribution remittance.

### Example 3 -- G50 / IRG payment to the Treasury (NOT a contribution)

**Input line:**
`19.02.2025 ; RECETTE DES IMPOTS G50 ; DEBIT ; IRG SALAIRES 01/2025 ; -9,072.00 ; DZD`

**Reasoning:**
Matches "RECETTE DES IMPOTS" / "G50" (pattern 3.3). This is the monthly G50 remittance of IRG withheld from salaries, due by the 20th of the following month (Rivermate). It is a tax payment to the DGI/Trésor, NOT a CNAS/CASNOS social contribution. Do not classify as social security. Exclude from TVA.

**Classification:** EXCLUDE from TVA -- payroll income tax (IRG via G50). NOT a contribution.

### Example 4 -- CASNOS self-employed annual contribution (CPA bank)

**Input line:**
`15.03.2025 ; CASNOS COTISATION 2025 ; DEBIT ; NON SALARIE ; -90,000.00 ; DZD`

**Reasoning:**
Matches "CASNOS COTISATION" (pattern 3.2). 15% of declared annual income (CLEISS). 90,000 / 0.15 = 600,000 DZD declared annual income, which sits inside the CASNOS band (floor 216,000 → ceiling 4,320,000). Split is 7.5% social insurance (45,000) + 7.5% retirement (45,000). Inside the band, so neither floor nor ceiling bites. Exclude from TVA.

**Classification:** EXCLUDE from TVA -- CASNOS self-employed contribution.

### Example 5 -- CASNOS contribution at the floor (low declared income)

**Input line:**
`20.03.2025 ; CASNOS ; DEBIT ; COTISATION MINIMALE ; -32,400.00 ; DZD`

**Reasoning:**
Matches "CASNOS" (pattern 3.2). The CASNOS base is floored at 216,000 DZD/year (CLEISS). 15% × 216,000 = 32,400.00 DZD — the minimum annual CASNOS contribution. Any declared income below 216,000 is contributed on the 216,000 floor, not the lower actual figure. Exclude from TVA.

**Classification:** EXCLUDE from TVA -- CASNOS minimum contribution (floored at 216,000 DZD base).

### Example 6 -- Ambiguous CNAS debit (possible arrears + penalty)

**Input line:**
`05.04.2025 ; CNAS REGULARISATION ; DEBIT ; MAJORATION DE RETARD ; -41,500.00 ; DZD`

**Reasoning:**
Matches "CNAS" (pattern 3.1) but the reference "MAJORATION DE RETARD" signals a late-payment surcharge. Late CNAS contributions carry a 10% penalty plus 3% per month of delay (almawarid). The amount mixes contribution principal with penalty, which cannot be separated without a CNAS statement. The penalty portion is not a normal deductible contribution. Flag for reviewer.

**Classification:** EXCLUDE from TVA. Flag for reviewer -- request a CNAS statement to split contribution principal from the 10% + 3%/month penalty.

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Salaried CNAS formula

- **CNAS formula** — CNAS_total = gross_salary x 35% CNAS_employer = gross_salary x 26% CNAS_employee = gross_salary x 9%  _(Headline 26% employer / 9% employee / 35% total (CLEISS / PwC). The employer remits both shares monthly. No general earnings ceiling applies (CLEISS / PwC).)_

### Rule 2 -- CNAS branch breakdown (effective 1 Jan 2024)

**CNAS branch breakdown**  _(https://www.cleiss.fr/docs/cotisations/algerie.html)_

| Branch | Employer | Employee | Other | Total |
| --- | --- | --- | --- | --- |
| Social insurance (illness, maternity, disability, death) | 11.5% | 1.5% | — | 13% |
| Work accidents & occupational illness | 1.25% | — | — | 1.25% |
| Retirement | 11% | 6.75% | 0.50% (FNPOS housing fund) | 18.25% |
| Early retirement | 0.25% | 0.25% | — | 0.5% |
| Unemployment insurance | 1% | 0.5% | — | 1.5% |
| **TOTAL** | **25% (+0.50% FNPOS)** | **9%** | **0.50%** | **34.5%** |

- **Reconciliation of headline vs itemised rates** — The headline 26% employer is the commonly-cited figure including the 0.50% FNPOS and minor sector add-ons; CLEISS itemises pure employer branches at 25% + 0.50% FNPOS = 25.5% (PwC / CLEISS reconciliation). Employer column 11.5 + 1.25 + 11 + 0.25 + 1 = 25.0%; employee column 1.5 + 0 + 6.75 + 0.25 + 0.5 = 9.0%; grand total 34.5% (35% with rounding/sector add-ons).  _(https://www.cleiss.fr/docs/cotisations/algerie.html)_

### Rule 3 -- Construction / public works / hydraulics add-on

- **Sector add-on (unemployment branch)** — 0.375% (Applies in construction, public works, and hydraulics sectors, added to employer side where applicable; otherwise omit.)  _(CLEISS)_

### Rule 4 -- Contribution base (salaried)

- **Contribution base definition** — The base is all gross salary elements, excluding family benefits, expense reimbursements, departure/severance bonuses, and certain hardship allowances (CLEISS). The SNMG minimum wage (20,000 DZD/month in 2024–2025; 24,000 DZD/month from 1 Jan 2026) effectively floors the base. No general ceiling (CLEISS / PwC).  _(CLEISS / PwC)_

### Rule 5 -- Employee 9% is deductible for IRG

- **Employee 9% CNAS deductibility** — The employee's 9% CNAS deduction is subtracted from gross salary to arrive at the IRG taxable base (CLEISS). Compute IRG on (gross − employee social contribution).  _(CLEISS)_

### Rule 6 -- Self-employed CASNOS formula

- **CASNOS formula** — CASNOS = clamp(declared_annual_income, 216,000, 4,320,000) x 15%  _(https://www.cleiss.fr/docs/cotisations/algerie.html)_
- **CASNOS composition and bounds** — 15% = 7.5% social insurance + 7.5% retirement (CLEISS). Floor base 216,000 DZD/year (min contribution 32,400); ceiling base 4,320,000 DZD/year (max contribution 648,000).  _(https://www.cleiss.fr/docs/cotisations/algerie.html)_

### Rule 7 -- IRG progressive brackets (annual)

**IRG progressive brackets (annual)**  _(https://taxsummaries.pwc.com/algeria/individual/taxes-on-personal-income)_

| Annual taxable income (DZD) | Marginal rate | Tax at top of band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| ≤ 240,000 | 0% | 0 | 0 |
| 240,001 – 480,000 | 23% | 55,200 | 55,200 |
| 480,001 – 960,000 | 27% | 129,600 | 184,800 |
| 960,001 – 1,920,000 | 30% | 288,000 | 472,800 |
| 1,920,001 – 3,840,000 | 33% | 633,600 | 1,106,400 |
| > 3,840,000 | 35% | — | — |

- **Cumulative check** — Progressive 0%–35% on annual taxable income (PwC, FL 2022 schedule still current per PwC last reviewed 14 July 2025). Cumulative check: 0 → +55,200 → +129,600 = 184,800 → +288,000 = 472,800 → +633,600 = 1,106,400.  _(https://taxsummaries.pwc.com/algeria/individual/taxes-on-personal-income)_

### Rule 8 -- Monthly salary IRG exemption

- **Salaried monthly IRG exemption threshold** — 30,000 DZD/month (Salaries not exceeding this amount are effectively exempt from IRG (search result; corroborates the 240,000 annual threshold plus salary-relief mechanics). For salaried workers, apply payroll-specific relief; do not apply the raw annual table without confirming the salary-withholding schedule `[RESEARCH GAP — confirm the exact salaried IRG withholding/abatement table against the DGI / Code des Impôts Directs, mfdgi.gov.dz]`.)  _(search result (corroborated))_

### Rule 9 -- Filing schedule

**Filing schedule**

| Obligation | Frequency | Deadline | Source |
| --- | --- | --- | --- |
| G50 (tax, incl. IRG salaries withheld) | Monthly | 20th of month following salary payment | Rivermate |
| CNAS contribution declaration/payment (DAC) | Monthly | Within first 10 days of following month | almawarid |
| DAS (Déclaration Annuelle des Salaires) | Annual | Before 31 January following year | almawarid |
| Annual income tax return | Annual | ~30 April following the tax year | Rivermate |

- **CNAS deadline note** — The CNAS 10-day deadline (almawarid) is the social-security-specific one; the 20th is the G50 tax deadline. Some EOR guides cite the 20th for CNAS too `[RESEARCH GAP — confirm exact CNAS monthly deadline against cnas.dz]`.  _(almawarid)_

### Rule 10 -- Universal mandatory affiliation

- **Mandatory affiliation** — All salaried workers must be affiliated to CNAS, and all non-salaried/self-employed to CASNOS, from the first day of activity. There is no income threshold for affiliation — coverage is universal and mandatory (CLEISS).  _(CLEISS)_

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Salaried vs self-employed boundary (mixed activity)

- **T2-1** — Trigger: Client draws a salary and also earns self-employed/professional income. Issue: Salaried income falls under CNAS (35%); self-employed income under CASNOS (15%). Both regimes can apply simultaneously on different income streams. Action: Flag for reviewer. Split the income streams and confirm dual affiliation before computing.

### T2-2 -- Sector-specific add-on (construction / public works / hydraulics)

- **T2-2** — Trigger: Employer operates in construction, public works, or hydraulics. Issue: An extra 0.375% unemployment-branch contribution applies (CLEISS). It is easy to omit. Action: Flag for reviewer. Confirm the sector classification and add the 0.375% to the employer side.  _(CLEISS)_

### T2-3 -- Rate-source reconciliation (26% vs 25.5%)

- **T2-3** — Trigger: A contribution figure does not reconcile to a clean 26% employer. Issue: CLEISS itemises pure employer branches at 25% + 0.50% FNPOS = 25.5%, while PwC and Algerian summaries cite a headline 26% (rounding/sector add-ons). A second 2025 source (almawarid) allocates branches slightly differently (Health-Maternity 12.5%/1.5%; Retirement 10.5%/6.75%) but reaches the same ~26%/9% totals. Action: Flag for reviewer where the exact branch split matters (e.g. branch-level reconciliation). Use 26%/9%/35% as the headline.

### T2-4 -- CNAS / CASNOS arrears and penalties

- **T2-4** — Trigger: Client has unpaid contributions from prior periods. Issue: Late CNAS contributions attract 10% + 3% per month of delay and can trigger legal proceedings (almawarid). Principal and penalty cannot be separated without a CNAS statement. Action: Do not quantify arrears. Escalate to a warranted Algerian accountant.  _(almawarid)_

### T2-5 -- Salaried IRG withholding vs annual table

- **T2-5** — Trigger: Need to compute IRG actually withheld from a salary. Issue: The 30,000 DZD/month exemption and salary-specific abatements differ from a naive application of the annual 0%–35% table. The exact salaried withholding schedule is not confirmed from a primary authority. Action: Flag for reviewer. Confirm against the DGI / Code des Impôts Directs `[RESEARCH GAP — reviewer to confirm]` before relying on a computed net-pay figure.

### T2-6 -- 2026 SNMG change and Finance Law 2025 floors

- **T2-6** — Trigger: Computation spans into 2026, or involves the lump-sum/minimum tax regime. Issue: SNMG rises to 24,000 DZD/month from 1 Jan 2026 (Radio Algérie / North Africa Post). Finance Law 2025 reportedly raised the minimum lump-sum tax (IFU/FRT) floor to DZD 30,000 from DZD 10,000 effective 1 Jan 2026 `[RESEARCH GAP — verify exact wording at https://taxsummaries.pwc.com/algeria/individual/significant-developments]`. Action: Flag for reviewer. Confirm which year's SNMG and tax floors apply.  _(Radio Algérie / North Africa Post)_

## Section 7 -- Excel working paper template

When producing a contribution / payroll computation, structure the working paper as follows:

```
ALGERIA CONTRIBUTION & IRG COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [year]                          Currency: DZD
Prepared: [date]

INPUT DATA
  Employment status:             [Salaried (CNAS) / Self-employed (CASNOS)]
  Sector:                        [Standard / Construction-PublicWorks-Hydraulics]
  Gross monthly salary (CNAS):   DZD [____]
  Declared annual income (CASNOS): DZD [____]
  Residency:                     [Resident / Non-resident]

CNAS COMPUTATION (salaried)
  Gross monthly base:            DZD [____]   (floored at SNMG: 20,000 [2024-25] / 24,000 [2026])
  Employer 26%:                  DZD [____]
  Employee 9%:                   DZD [____]
  Sector add-on 0.375% (if any): DZD [____]
  Total 35%:                     DZD [____]

CASNOS COMPUTATION (self-employed)
  Declared income (clamped 216,000 - 4,320,000): DZD [____]
  Contribution 15%:              DZD [____]
    of which 7.5% insurance:     DZD [____]
    of which 7.5% retirement:    DZD [____]

IRG COMPUTATION
  Gross salary (annual):         DZD [____]
  Less employee CNAS 9%:         DZD [____]
  IRG taxable base:              DZD [____]
  IRG (per Section 5 Rule 7/8):  DZD [____]   [confirm salaried withholding schedule]
  Net pay:                       DZD [____]

FILING
  G50 (IRG) due:                 20th of following month
  CNAS DAC due:                  within 10 days of following month
  DAS (annual salaries) due:     before 31 January

REVIEWER FLAGS
  [List any Tier 2 flags and RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contribution and tax debits appear on Algerian bank statements

Statements from Algerian banks (BNA — Banque Nationale d'Algérie; BEA — Banque Extérieure d'Algérie; CPA — Crédit Populaire d'Algérie; BADR; BDL) are typically in French, sometimes Arabic. Amounts are in DZD with no decimal subunit in common use (the centime is largely nominal).

**CNAS (salaried contributions):**
- Description: "CNAS", "COTISATION CNAS", "DAC", "CAISSE NATIONALE ASSURANCES SOCIALES"
- Timing: Monthly, around the first 10 days for the prior month
- Amount: ~35% of total gross payroll (combined employer 26% + employee 9%)

**CASNOS (self-employed contributions):**
- Description: "CASNOS", "COTISATION CASNOS", "NON SALARIE"
- Timing: Typically annual (15% of declared annual income)
- Amount: 15% of declared income, within the 216,000–4,320,000 base band

**G50 / IRG (income tax to the Treasury):**
- Description: "G50", "RECETTE DES IMPOTS", "TRESOR", "IRG SALAIRES", "DGI"
- Timing: Monthly by the 20th
- Counterparty: DGI / Trésor, NOT CNAS/CASNOS

**Key identification tips:**
1. Contribution debits are always outgoing (DEBIT), never credits — inbound CNR/CNAC credits are benefits received, not contributions.
2. CNAS debits recur monthly; CASNOS typically annual.
3. Counterparty distinguishes regime: CNAS/CASNOS = social contribution; Trésor/DGI/G50 = income tax.
4. A "MAJORATION DE RETARD" or "REGULARISATION" reference signals penalties/arrears — flag for reviewer.
5. Family benefits (ALLOCATIONS FAMILIALES) are outside the contribution base entirely.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Determine the regime** -- look for CNAS (salaried) vs CASNOS (self-employed) debit counterparties.
2. **Scan for contribution debits** -- identify all outgoing payments matching Section 3 patterns.
3. **Reverse-engineer the base:**
   - CNAS monthly debit ÷ 0.35 ≈ total gross monthly payroll base.
   - CASNOS debit ÷ 0.15 ≈ declared annual income (then check it sits within 216,000–4,320,000).
   - If a CASNOS debit ≈ 32,400, the floor (216,000 base) is in play.
4. **Separate tax from contributions** -- G50/Trésor/DGI debits are IRG (income tax), not social contributions.
5. **Flag for reviewer:** "Regime and base derived from bank statement amounts only. Employment status, sector, and declared income have not been independently verified. Salaried IRG withholding and any sector add-on require confirmation before filing."

## Section 10 -- Reference material

### Contribution rate summary

**Contribution rate summary**

| Regime | Employer | Employee | Total | Base / band | Source |
| --- | --- | --- | --- | --- | --- |
| CNAS (salaried) | 26% | 9% | 35% | gross salary, SNMG floor, no general ceiling | CLEISS / PwC |
| CNAS branch total (itemised) | 25% + 0.50% FNPOS | 9% | 34.5% | as above | CLEISS |
| Construction/PW/hydraulics add-on | +0.375% | — | +0.375% | unemployment branch | CLEISS |
| CASNOS (self-employed) | — | 15% | 15% | 216,000 – 4,320,000 DZD/yr declared income | CLEISS |

### Minimum wage (SNMG)

**Minimum wage (SNMG)**

| Period | SNMG (monthly) | Source |
| --- | --- | --- |
| 2024–2025 | 20,000 DZD | CLEISS |
| From 1 Jan 2026 | 24,000 DZD (+20%) | Radio Algérie / North Africa Post |

### IRG annual brackets (PwC, FL 2022 schedule current)

**IRG annual brackets**

| Annual taxable income (DZD) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| ≤ 240,000 | 0% | 0 |
| 240,001 – 480,000 | 23% | 55,200 |
| 480,001 – 960,000 | 27% | 184,800 |
| 960,001 – 1,920,000 | 30% | 472,800 |
| 1,920,001 – 3,840,000 | 33% | 1,106,400 |
| > 3,840,000 | 35% | — |

- **Other personal taxes and residency rules** — Monthly salary IRG exemption: salaries ≤ 30,000 DZD/month effectively exempt (search result). Other personal taxes: capital gains 15% residents / 20% non-residents; dividends 15%; interest 10% (PwC). Residents taxed on worldwide income; non-residents only on Algeria-source professional income (PwC).  _(https://taxsummaries.pwc.com/algeria/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/algeria/individual/other-taxes)_

### Corporate income tax (IBS) — context only

**Corporate income tax (IBS) rates**

| Activity | IBS rate | Source |
| --- | --- | --- |
| Manufacturing / production | 19% | PwC |
| Building, public works, hydraulics, tourism/thermal | 23% | PwC |
| Other (services / trade) | 26% | PwC |
| Minimum CIT on nil returns | DZD 10,000 | PwC |
| Reduced rate on reinvested manufacturing profits | 10% | PwC |

- **Finance Law 2025 minimum lump-sum tax floor** — Finance Law 2025 reportedly raised the minimum lump-sum tax (IFU/FRT) floor to DZD 30,000 from DZD 10,000 effective 1 Jan 2026 `[RESEARCH GAP — reviewer to confirm]`.  _(https://taxsummaries.pwc.com/algeria/corporate/taxes-on-corporate-income)_

### Penalties

**Penalties table**

| Penalty | Rate / consequence | Source |
| --- | --- | --- |
| Late CNAS contributions | 10% penalty + 3% per month of delay (majoration de retard) | almawarid |
| Late CNAS declaration | Possible legal proceedings (poursuites) | almawarid |
| IRG late payment | Penalties + interest + potential audit; exact statutory % `[RESEARCH GAP — reviewer to confirm against Code des Impôts Directs]` | (not in consulted authorities) |

### Worked IRG reconciliation (illustrative — confirm salaried schedule before use)

Annual gross 960,000 DZD (80,000/month). Employee CNAS 9% = 86,400. IRG annual-table base = 960,000 − 86,400 = 873,600.
IRG on 873,600 = 0 (first 240,000) + 23% × (480,000 − 240,000) = 55,200 + 27% × (873,600 − 480,000) = 27% × 393,600 = 106,272 → **total IRG 161,472**.
Annual net = 960,000 − 86,400 − 161,472 = **712,128 DZD**. (Illustrative on the annual table; the salaried monthly withholding schedule may differ — see Rule 8 / T2-5.)

### Test suite

**Test 1:** Salaried, gross 20,000 DZD/month (SNMG floor). -> Employer 26% = 5,200; Employee 9% = 1,800; Total 35% = 7,000. IRG ≈ 0 (≤ 30,000/month exemption). Net pay = 20,000 − 1,800 = 18,200.

**Test 2:** Salaried, gross 100,000 DZD/month. -> Employer 26% = 26,000; Employee 9% = 9,000; Total 35% = 35,000. (Branch check: employer 25% + 0.50% FNPOS reconciles to 25.5%; headline 26%.)

**Test 3:** CASNOS, declared income 600,000 DZD/yr. -> 15% × 600,000 = 90,000 (45,000 insurance + 45,000 retirement). Inside band 216,000–4,320,000.

**Test 4:** CASNOS, declared income 100,000 DZD/yr (below floor). -> floored at 216,000; 15% × 216,000 = 32,400 minimum.

**Test 5:** CASNOS, declared income 6,000,000 DZD/yr (above ceiling). -> capped at 4,320,000; 15% × 4,320,000 = 648,000 maximum.

**Test 6:** Salaried, annual gross 960,000 DZD, resident. -> Employee CNAS 9% = 86,400; IRG annual-table base 873,600; IRG = 161,472; net = 712,128. (Illustrative — confirm salaried withholding schedule.)

**Test 7:** Construction-sector salaried, gross 50,000 DZD/month. -> Standard employer 26% = 13,000 PLUS 0.375% add-on = 187.50, employer total 13,187.50; employee 9% = 4,500.

**Test 8:** CNAS monthly debit observed = 7,000 DZD, single employee. -> 7,000 / 0.35 = 20,000 implied gross base (SNMG floor). Reconciles.

### Prohibitions

- NEVER compute contributions without first establishing whether the client is salaried (CNAS) or self-employed (CASNOS) — the regimes differ entirely.
- NEVER apply a general earnings ceiling to salaried CNAS — none is reported (CLEISS / PwC).
- NEVER omit the 0.375% sector add-on for construction/public works/hydraulics without confirming the sector.
- NEVER apply the raw annual IRG table as if it were the salaried monthly withholding without confirming the schedule — flag the `[RESEARCH GAP]`.
- NEVER tell a self-employed client they owe contributions below the CASNOS floor — the 216,000 DZD base (32,400 DZD min) always applies.
- NEVER conflate CNAS/CASNOS (social contribution) with G50/IRG (income tax) — they go to different authorities.
- NEVER quantify contribution or tax arrears/penalties without an official CNAS or DGI statement — escalate.
- NEVER state a statutory IRG late-payment penalty percentage — it is unconfirmed `[RESEARCH GAP — reviewer to confirm]`.
- NEVER mix tax years' SNMG figures — 20,000 DZD applies through 2025; 24,000 DZD from 1 Jan 2026.
- NEVER present figures as definitive — this is a Tier 2 skill pending warranted-accountant sign-off.

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
