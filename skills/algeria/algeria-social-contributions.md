---
name: algeria-social-contributions
description: "Use this skill whenever asked about Algeria social security / social insurance contributions (CNAS for salaried employees, CASNOS for self-employed/non-salaried) and the interaction with Algerian personal income tax (IRG). Trigger on phrases like 'how much CNAS do I pay', 'Algeria payroll contributions', 'employer social security Algeria', 'CNAS employee deduction', 'CASNOS self-employed contribution', 'G50 declaration', 'DAS annual salary declaration', 'IRG on salary', 'Algerian minimum wage SNMG', 'social security Algeria calculation', or any question about Algerian payroll, contribution or IRG obligations. Also trigger when classifying bank statement transactions that relate to CNAS/CASNOS debits, G50 tax payments, or DGI/Trésor payments from BNA, BEA, CPA, BADR, or other Algerian banks. This skill covers CNAS 26%/9% branch rates, the CASNOS 15% self-employed regime, the SNMG floor, IRG progressive brackets, G50/DAS filing and deadlines, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Algerian contribution or payroll work."
version: 0.2
jurisdiction: DZ
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

# Algeria Social Contributions (CNAS and CASNOS) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). Amounts in Algerian dinars (DA or DZD). Primary authority: Direction Generale des Impots (DGI).

## Who this applies to

Salaried workers and employers (CNAS) and non-salaried workers (CASNOS). Affiliation is compulsory whatever the income. Arrears cases and start-up reductions go to a local professional.

## Rates, bands and thresholds

| Branch | Employer | Employee | Other | Tax year | Official URL |
|---|---|---|---|---|---|
| Social insurance | 11.5% | 1.5% | none | 2024 edition | https://www.cleiss.fr/docs/cotisations/algerie.html |
| Work accidents | 1.25% | none | none | 2024 edition | same |
| Retirement | 11% | 6.75% | 0.5% FNPOS | 2024 edition | same |
| Early retirement | 0.25% | 0.25% | none | 2024 edition | same |
| Unemployment | 1% | 0.5% | none | 2024 edition | same |
| Total | 25% | 9% | 0.5% | 2024 edition | same |
| Construction, public works, hydraulics add-on | 0.375% | 0.375% | CACOBATPH | 2024 edition | same |

| CASNOS item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Rate | 15% of annual base | 7.5% insurance, 7.5% retirement | 2026 | https://casnos.dz/ |
| Minimum contribution | SNMG x 12 x 15% = 43,200 DA | Base 288,000 DA, from SNMG 24,000 DA | 2026 | https://casnos.dz/ |
| Maximum contribution | SNMG x 12 x 15% x 20 = 864,000 DA | Base 5,760,000 DA | 2026 | same |
| SNMG | 24,000 DA a month | Decree 26-01 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf |


## The base

CNAS base: all salary items except family benefits, expense refunds, leaving bonuses and special living-condition allowances (https://www.cleiss.fr/docs/cotisations/algerie.html). CASNOS base: taxable annual income, or turnover if none (https://www.cleiss.fr/docs/cotisations/algerie.html).

### Carried from the earlier version, not checked against the law

Patterns, defaults and refusal rules kept so no work is lost. Any figure here is unverified unless it also appears in the tables above; the tables win.

#### Required inputs

**Minimum viable**: employment status (salaried vs non-salaried/self-employed) and gross monthly salary (CNAS) or declared annual income (CASNOS). Without employment status, STOP: the two regimes are not interchangeable.

**Recommended**: the tax year, the employer's sector (construction/public works/hydraulics carries an add-on), and for IRG: residency status and any other Algeria-source income.

**Ideal**: CNAS DAC declarations, G50 declarations, DAS annual salary declaration, payslips showing the 9% employee deduction and IRG withheld, and bank statements showing CNAS/CASNOS and Trésor/DGI debits.

#### Refusal catalogue

- **R-DZ-SC-1**: Employment status unknown. Trigger: not stated whether the client is salaried (CNAS) or self-employed (CASNOS). Message: "Employment status is mandatory. Salaried workers contribute 35% via CNAS (26% employer / 9% employee, no ceiling); self-employed contribute 15% via CASNOS within an income band. These regimes are not interchangeable. Cannot proceed without this information."
- **R-DZ-SC-2**: Contribution arrears / penalties. Trigger: client has unpaid CNAS contributions from prior periods. Message: "Late CNAS contributions attract a 10% penalty plus 3% per month of delay (majoration de retard) and can trigger legal proceedings (CLEISS / Algerian payroll sources). Do not quantify arrears without a CNAS statement. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-3**: Sector add-ons and exemptions. Trigger: client is in construction, public works, hydraulics, or claims a reduced-rate scheme (e.g. ANSEJ/ANADE start-up exemptions). Message: "An additional 0.375% unemployment-branch contribution applies in construction/public works/hydraulics, and start-up/youth-employment schemes may carry temporary exemptions. These require case-specific confirmation. Escalate to a warranted Algerian accountant."
- **R-DZ-SC-4**: Non-resident / expat payroll. Trigger: client is a non-resident, on a bilateral social-security agreement, or seconded into/out of Algeria. Message: "Bilateral social-security agreements and secondment relief are outside the scope of this skill. Non-residents are taxed only on Algeria-source professional income (unverified note). Escalate to a warranted Algerian accountant."
- **R-DZ-SC-5**: IRG/tax penalty quantification. Trigger: request to quantify statutory IRG late-payment penalties. Message: "Specific statutory IRG late-payment penalty percentages are not confirmed from a primary authority in this skill (unverified). Do not estimate. Escalate to a warranted Algerian accountant."


This is the deterministic pre-classifier for bank statement transactions related to Algerian contributions and payroll tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statements may be in French or Arabic. Contribution and IRG payments always EXCLUDE from any VAT (TVA) return: they are statutory payroll/personal obligations, not business supplies.

#### 3.1 CNAS salaried contribution debits

**CNAS salaried contribution debits**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: CNAS | EXCLUDE: social contribution | Monthly DAC payment of the combined 35% (26% employer + 9% employee) |
| CAISSE NATIONALE ASSURANCES SOCIALES | EXCLUDE: social contribution | Full CNAS name |
| COTISATION CNAS, COTISATIONS SOCIALES | EXCLUDE: social contribution | "Contribution" reference |
| DAC, DECLARATION CNAS | EXCLUDE: social contribution | DAC = the monthly CNAS declaration/payment |
| الضمان الاجتماعي (social security) | EXCLUDE: social contribution | Arabic-language reference |

#### 3.2 CASNOS self-employed contribution debits

**CASNOS self-employed contribution debits**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: CASNOS | EXCLUDE: self-employed contribution | 15% of declared annual income |
| CAISSE NON-SALARIES, NON SALARIES | EXCLUDE: self-employed contribution | Full/abbreviated CASNOS reference |
| COTISATION CASNOS | EXCLUDE: self-employed contribution | Contribution reference |

#### 3.3 IRG / income tax payments (NOT a social contribution)

**IRG / income tax payments**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: G50, G-50, G 50 | EXCLUDE: payroll tax (IRG withheld) | Monthly combined tax declaration, due 20th |
| IRG, IMPOT REVENU GLOBAL | EXCLUDE: income tax | Not a CNAS/CASNOS contribution |
| TRESOR, RECETTE DES IMPOTS | EXCLUDE: tax payment to the Treasury | DGI/Trésor counterparty |
| DGI, DIRECTION DES IMPOTS | EXCLUDE: tax payment | Tax authority |
| IBS, IMPOT BENEFICES SOCIETES | EXCLUDE: corporate tax | Company-level, not payroll contribution |

#### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| SALAIRE, PAIE, VIREMENT SALAIRE (outgoing) | EXCLUDE: payroll expense | Net wage transfer, not a CNAS payment |
| SALAIRE (incoming) | EXCLUDE: employment income received | Not a contribution |
| الراتب (salary) | EXCLUDE: payroll/salary | Arabic-language reference |

#### 3.5 Benefits received (not contributions paid)

**Benefits received**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| PENSION CNR, RETRAITE | EXCLUDE: pension income received | CNR pays pensions; not a contribution |
| ALLOCATION CHOMAGE, CNAC | EXCLUDE: unemployment benefit received | Inbound benefit, not a contribution |
| ALLOCATIONS FAMILIALES | EXCLUDE: family benefit received | Outside the contribution base entirely |

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

#### T2-1: Salaried vs self-employed boundary (mixed activity)

- **T2-1**: Trigger: Client draws a salary and also earns self-employed/professional income. Issue: Salaried income falls under CNAS (35%); self-employed income under CASNOS (15%). Both regimes can apply simultaneously on different income streams. Action: Flag for reviewer. Split the income streams and confirm dual affiliation before computing.

#### T2-2: Sector-specific add-on (construction / public works / hydraulics)

- **T2-2**: Trigger: Employer operates in construction, public works, or hydraulics. Issue: An extra 0.375% unemployment-branch contribution applies (CLEISS). It is easy to omit. Action: Flag for reviewer. Confirm the sector classification and add the 0.375% to the employer side.  _(CLEISS)_

#### T2-3: Rate-source reconciliation (26% vs 25.5%)

- **T2-3**: Trigger: A contribution figure does not reconcile to a clean 26% employer. Issue: CLEISS itemises pure employer branches at 25% + 0.50% FNPOS = 25.5%, while unverified note and Algerian summaries cite a headline 26% (rounding/sector add-ons). A second 2025 source (unverified note) allocates branches slightly differently (Health-Maternity 12.5%/1.5%; Retirement 10.5%/6.75%) but reaches the same ~26%/9% totals. Action: Flag for reviewer where the exact branch split matters (e.g. branch-level reconciliation). Use 26%/9%/35% as the headline.

#### T2-4: CNAS / CASNOS arrears and penalties

- **T2-4**: Trigger: Client has unpaid contributions from prior periods. Issue: Late CNAS contributions attract 10% + 3% per month of delay and can trigger legal proceedings (unverified note). Principal and penalty cannot be separated without a CNAS statement. Action: Do not quantify arrears. Escalate to a warranted Algerian accountant.  _(unverified note)_

#### T2-5: Salaried IRG withholding vs annual table

- **T2-5**: Trigger: Need to compute IRG actually withheld from a salary. Issue: The 30,000 DZD/month exemption and salary-specific abatements differ from a naive application of the annual 0%-35% table. The exact salaried withholding schedule is not confirmed from a primary authority. Action: Flag for reviewer. Confirm against the DGI / Code des Impôts Directs (unverified) before relying on a computed net-pay figure.

#### T2-6: 2026 SNMG change and Finance Law 2025 floors

- **T2-6**: Trigger: Computation spans into 2026, or involves the lump-sum/minimum tax regime. Issue: SNMG rises to 24,000 DZD/month from 1 Jan 2026 (unverified note / unverified note). Finance Law 2025 reportedly raised the minimum lump-sum tax (IFU/FRT) floor to DZD 30,000 from DZD 10,000 effective 1 Jan 2026 (unverified). Action: Flag for reviewer. Confirm which year's SNMG and tax floors apply.  _(unverified note / unverified note)_


When producing a contribution / payroll computation, structure the working paper as follows:

```
ALGERIA CONTRIBUTION & IRG COMPUTATION: WORKING PAPER
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
  [List any Tier 2 flags and (unverified)

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Deadlines and filing

| Obligation | Deadline | Official URL |
|---|---|---|
| CASNOS base declaration | 1 March | https://casnos.dz/ |
| CASNOS payment, non-farm | Before 30 June | same |
| CASNOS payment, farm | 30 September | same |
| CNAS monthly and annual | unverified: 10 days and 31 January in the old skill | unverified |

How to pay CASNOS: (1) declare your base at your CASNOS office by 1 March; (2) compute 15% within the floor and cap; (3) pay at your antenne before 30 June. If you miss the declaration, the amount is set provisionally on last year's base, plus 5% for each extra month.

## Penalties and interest

CASNOS: late base declaration, last year's base increased 5% a month (https://casnos.dz/). CNAS late penalties are unverified; the old skills disagree (10% plus 3% a month against 15% plus 2%).

## Cross-border points

A French posted worker or treaty case needs the bilateral agreement, which is out of scope. Refer it.

## Two worked examples that recompute

**Example 1, simple.** Salary 80,000 DA: employee 7,200 DA, employer 20,000 DA, FNPOS 400 DA.

```oa-check
name: CNAS on 80,000 DA
inputs:
  gross: 80000
steps:
  - employee: gross * 0.09
  - employer: gross * 0.25
  - fnpos: gross * 0.005
expected:
  employee: 7200.00
  employer: 20000.00
  fnpos: 400.00
```

**Example 2, edge.** Self-employed income 200,000 DA is below the 288,000 DA floor, so CASNOS is 43,200 DA, not 30,000.

```oa-check
name: CASNOS floor 2026
inputs:
  income: 200000
  snmg: 24000
steps:
  - base: clamp(income, snmg * 12, snmg * 12 * 20)
  - due: base * 0.15
expected:
  due: 43200.00
```

## Ask the client first

1. Salaried or self-employed?
2. Sector, for the construction add-on?
3. Declared annual income?
4. Farm or non-farm?
5. Any arrears?

## Sources

| Source | URL | Read on |
|---|---|---|
| Presidential Decree 26-01 of 7 Jan 2026, JO 2026 n° 1 (read: arts. 1 and 2); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf | 2026-11-01 |
| CASNOS site, contribution FAQ and assiette text in the page bundle; read for the rates and steps cited | https://casnos.dz/ | 2026-11-01 |
| CLEISS (French public body), Algeria contributions at 1 Jan 2024; 2024 is the latest edition; read for the rates and steps cited | https://www.cleiss.fr/docs/cotisations/algerie.html | 2026-11-01 |

mfdgi.gov.dz and cnas.dz refused every direct and Chrome connection on 2026-11-01; DGI pages are Internet Archive copies, marked as such.

Not yet confirmed: 26% employer and 35% total headline figures, since CLEISS shows 25% plus 0.5% FNPOS, 34.5% total; whether branch rates changed after 1 Jan 2024; CNAS monthly deadline, DAS or DAC dates and CNAS late penalties, because cnas.dz would not open and has no readable archive; CASNOS late penalty; the CASNOS site still prints 216,000 and 4,320,000 DA, computed on the old SNMG, so the 2026 amounts below come from its formula with the new SNMG and need CASNOS confirmation.

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
