---
name: algeria-payroll
description: "Use this skill whenever asked about Algeria payroll processing for employed persons. Trigger on phrases like 'Algeria payroll', 'IRG Traitements et Salaires', 'IRG withholding Algeria', 'retenue à la source Algérie', 'CNAS deduction', 'cotisation sociale Algérie', 'G50 declaration', 'DAS CNAS', 'bordereau CNAS', 'salaire net Algérie', 'PAYE Algeria', 'net salary Algeria', 'SNMG', 'salaire minimum Algérie', 'abattement 40% salaire', 'employer social security Algeria', 'gross to net Algeria', 'barème IRG', or any question about computing employee pay, income-tax withholding, or social-security contributions for Algeria-based employees. This skill covers IRG (income tax) withholding by the employer, CNAS social security (employee 9% + employer 26%), the branch-by-branch contribution breakdown, the 40% salary abattement, the SNMG minimum wage, and filing obligations to the DGI (G50) and CNAS (monthly + annual DAS). ALWAYS read this skill before processing any Algeria payroll."
version: 0.2
jurisdiction: DZ
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

# Algeria Payroll v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). Amounts in Algerian dinars (DA or DZD). Primary authority: Direction Generale des Impots (DGI).

## Who this applies to

Employers running monthly payroll for staff in Algeria. Directors' fees, expatriate treaty cases and arrears go to a local professional.

## Rates, bands and thresholds

| Annual taxable income (DA) | Rate | Tax year | Official URL |
|---|---|---|---|
| Up to 240,000 | 0% | 2026 | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| 240,001 to 480,000 | 23% | 2026 | same |
| 480,001 to 960,000 | 27% | 2026 | same |
| 960,001 to 1,920,000 | 30% | 2026 | same |
| 1,920,001 to 3,840,000 | 33% | 2026 | same |
| Over 3,840,000 | 35% | 2026 | same |

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Salary exemption | Up to 30,000 DA a month: no IRG | CIDTA arts. 5 and 68 | 2026 | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| Abatement | 40% of the tax, minimum 1,000, maximum 1,500 DA a month | Taken off the tax, not the income | 2026 | same |
| Second abatement, 30,001 to 35,000 DA | IRG = first-abatement IRG x 137/51 - 27,925/8 | Ordinary employees | 2026 | same |
| Second abatement, disabled workers and pensioners, 30,001 to 42,500 DA | IRG = first-abatement IRG x 93/61 - 81,213/41 | Disabled workers and retirees | 2026 | same |
| Non-monthly bonuses, arrears | 10% | Treated as a separate monthly payment | 2026 | same |
| Occasional teaching, research, invigilation | 10% final | Vacataire work on top of a main job | 2026 | same |
| Other occasional intellectual work | 15% final | CIDTA art. 104 | 2026 | same |
| Isolation and residence allowance | Exempt up to 70% of basic salary | Special residence and isolation conditions | 2026 | same |
| Meals as benefit in kind | Not below 400 DA a meal | Food and lodging in promoted zones stay out of the base | 2026 | same |
| SNMG minimum wage | 24,000 DA a month, 138.46 DA an hour | 40 hours a week, 173.33 hours a month; Decree 26-01 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf |

| Branch | Employer | Employee | Other | Tax year | Official URL |
|---|---|---|---|---|---|
| Social insurance | 11.5% | 1.5% | none | 2024 edition | https://www.cleiss.fr/docs/cotisations/algerie.html |
| Work accidents | 1.25% | none | none | 2024 edition | same |
| Retirement | 11% | 6.75% | 0.5% FNPOS | 2024 edition | same |
| Early retirement | 0.25% | 0.25% | none | 2024 edition | same |
| Unemployment | 1% | 0.5% | none | 2024 edition | same |
| Total | 25% | 9% | 0.5% | 2024 edition | same |
| Construction, public works, hydraulics add-on | 0.375% | 0.375% | CACOBATPH | 2024 edition | same |


## The base

Order of calculation (https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires): (1) gross pay with benefits in kind; (2) less employee social share 9%; (3) test the exemption; (4) apply the bands to monthly taxable income, annual bands divided by 12; (5) take the 40% abatement off the tax, minimum 1,000, maximum 1,500 DA; (6) apply the second abatement in its band. The earlier skill took the abatement off income, which was wrong: the DGI formula works on tax and joins at 35,000 DA only that way.

Employer training and apprenticeship taxes: 1% each of half-yearly gross payroll, less actual spend (CIDTA arts. 196 bis to quinquies, LF 2026 arts. 18 to 20, https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf).

### Carried from the earlier version, not checked against the law

Patterns, defaults and refusal rules kept so no work is lost. Any figure here is unverified unless it also appears in the tables above; the tables win.

**Conservative Defaults**

| Unknown | Conservative default | Why |
| -- | -- | -- |
| unverified: Tax year | Default to **2025** scale (FL 2022, still current) | Skill tax_year is 2025; no 2026 scale published |
| unverified: Sector (construction add-on) | Assume **no** CACOBATPH 0.375% add-on unless told construction | Avoids over-stating; flag if sector unknown |
| unverified: Whether gross ≤ 30,000 DA | Apply the **full IRG exemption** strictly at/below 30,000 DA | Statutory exemption |
| unverified: Abattement amount | Apply 40% floored 1,000 / capped 1,500 DA/month | Statutory bounds |
| unverified: CNAS base below SNMG | Floor the contribution base at the **SNMG** (20,000 DA for 2025) | Contributions cannot be below SNMG |
| CNAS ceiling | **None**: compute on full gross (uncapped) | General salaried regime is uncapped |
| Currency | Algerian Dinar (DZD) | Wages are paid in Dinars |
| unverified: Headline CNAS split | **26% employer / 9% employee / 35% total** | Operative figure per unverified note/unverified note |

When an input is missing or ambiguous, apply the conservative assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

#### Required inputs before computing payroll

- **Required inputs**: 1. Monthly gross salary in DZD (and whether it is the ordinary/fixed base). 2. Tax/fiscal year (defaults to 2025 scale). 3. Sector (to decide the CACOBATPH 0.375% construction add-on). 4. Whether the salary is at or below the SNMG floor (20,000 DA for 2025 / 24,000 DA for 2026). 5. Any non-ordinary pay components (bonuses, primes, indemnités) and their treatment.

#### Refusal catalogue: DO NOT compute, refuse and request input

**Refusal catalogue**

| Situation | Action |
| -- | -- |
| No gross salary provided | REFUSE: request monthly salary in DZD |
| Salary stated in EUR/USD with no DZD conversion and no rate | REFUSE: request DZD figure |
| Request to omit IRG withholding or CNAS to "save money" | REFUSE: these are statutory; escalate to accountant |
| Salary below the SNMG offered as the contribution base | REFUSE: base cannot fall below the SNMG |
| unverified: Request to ignore the 30,000 DA monthly IRG exemption | REFUSE: statutory exemption; flag |
| Self-employed / non-salarié income mixed in | REFUSE payroll path: non-salariés have a separate CNAS band and IRG treatment |
| Definitive "this is your exact tax" assertion requested | REFUSE: outputs are estimates pending accountant sign-off |


Classify bank-statement lines deterministically. Match case-insensitively; longest / most-specific pattern wins.

#### Salary credits (money arriving in an employee account)

**Salary credits**

| Pattern (regex-ish, case-insensitive) | Classification |
| -- | -- |
| `SALAIRE`, `VIR.* SALAIRE`, `PAIE`, `VIREMENT SALAIRE` | Net salary payment |
| `ACOMPTE`, `AVANCE SUR SALAIRE` | Salary advance (not net pay; clears against salary) |
| `PRIME`, `INDEMNITE`, `IFSP`, `IEP` | Allowance / bonus component |
| `RAPPEL`, `RAPPEL SALAIRE` | Back-pay / arrears |
| `REMBOURSEMENT CNAS`, `IJ CNAS` | CNAS reimbursement / daily indemnity: not ordinary salary |

#### Employer debits (money leaving the employer account)

**Employer debits**

| Pattern | Classification |
| -- | -- |
| unverified: `IRG`, `G50`, `RETENUE SOURCE`, `VERSEMENT IRG` | IRG withholding remitted to DGI (liability settlement) |
| `CNAS`, `COTISATION CNAS`, `SECURITE SOCIALE` | CNAS contribution (employer + employee portions) |
| unverified: `CACOBATPH` | Construction sector leave / bad-weather fund (0.375% each) |
| `DAS`, `DECLARATION ANNUELLE` | Annual salary declaration filing (CNAS) |
| `VIREMENT PAIE`, `SALAIRES`, `NOMINATIVE PAIE` | Net wages disbursed to employees |

**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| -- | -- |
| Exact ordering of abattement vs. CNAS deduction in the IRG base | Not cleanly confirmed against DGI text |
| unverified: Interaction of the 30,000 DA exemption with the abattement floor | Mechanic not fully documented |
| unverified: Whether the FL 2022 scale still applies for the period in question | No 2025/2026 replacement published; verify currency |
| unverified: Exact IRG (G50) late-payment penalty percentages | Not confirmed from a primary DGI source |
| unverified: Precise date of the annual DGI salary recap (~30 April) | Secondary source only |
| CACOBATPH applicability for a given employer | Sector-specific |
| Treatment of specific primes / indemnités (taxable vs exempt) | Component-specific, needs ruling |
| unverified: Headline 26% vs CLEISS 25.5% employer reconciliation | Two presentations of the same regime |


**Excel Working Paper Template**

| Col | Header | Formula / source |
| -- | -- | -- |
| A | Employee name | input |
| B | Gross monthly salary (DZD) | input |
| unverified: C | Employee CNAS 9% | `=B*0.09` |
| D | Salary after CNAS | `=B-C` |
| unverified: E | Abattement | `=MIN(MAX(D*0.40,1000),1500)` |
| unverified: F | Monthly IRG base | `=MAX(0, D-E)` |
| unverified: G | Annual IRG base | `=F*12` |
| unverified: H | IRG annual | nested IF on G using subtract constants (55,200 / 74,400 / 103,200 / 160,800 / 237,600) |
| unverified: I | IRG monthly (pre-exemption) | `=H/12` |
| unverified: J | IRG monthly (final) | `=IF(B<=30000, 0, I)` |
| K | Net pay | `=B-C-J` |
| unverified: L | Employer CNAS 26% | `=B*0.26` |
| unverified: M | CACOBATPH (construction only) | `=IF(construction, B*0.375%*2, 0)` |
| unverified: N | Total employer cost | `=B+L+IF(construction, B*0.375%, 0)` |

- **IRG formula for column H**: =IF(G<=240000,0, IF(G<=480000, G*0.23-55200, IF(G<=960000, G*0.27-74400, IF(G<=1920000, G*0.30-103200, IF(G<=3840000, G*0.33-160800, G*0.35-237600)))))  _(Section 11 formulas)_

Suggested layout (one row per employee per month):

**Terminology Reading Guide**

| French / Arabic-transliterated term | English / meaning |
| -- | -- |
| Salaire / Paie | Salary / payroll run |
| IRG (Impôt sur le Revenu Global) | Personal income tax |
| Traitements et Salaires | Wages and salaries (the salary category of IRG) |
| Retenue à la source | Withholding at source |
| unverified: Abattement | Deduction / allowance (here, the 40% professional-expense deduction) |
| CNAS | National Social Insurance Fund |
| Cotisation | Contribution (social security) |
| unverified: G50 (bordereau) | Monthly tax/contribution declaration slip |
| DAS (Déclaration Annuelle des Salaires) | Annual salary declaration (CNAS) |
| SNMG | Guaranteed national minimum wage |
| Prime / Indemnité | Bonus / allowance |
| Acompte / Avance | Advance on salary |
| CACOBATPH | Construction-sector leave / bad-weather fund |
| unverified: FNPOS | Social-housing fund (0.5% pension-branch component) |
| Allocation chômage | Unemployment allowance |
| DGI | Directorate-General of Taxes |


- **Onboarding fallback steps**: If the engagement lacks key data: 1. No prior payroll register (livre de paie) available → request the last 3 months of payslips, G50 declarations, and CNAS bordereaux to back-solve the rates actually applied. 2. Unknown sector → default CACOBATPH off, FLAG; confirm before the first remittance. 3. Salary near the SNMG → confirm the contribution base is floored at the SNMG (20,000 DA for 2025 / 24,000 DA for 2026), never below. 4. Year ambiguity → default to the 2025 (FL 2022) scale; verify whether any new finance law has replaced it for periods after the research date. 5. Mixed self-employed income → route non-salarié income to a separate treatment; the non-salariés CNAS band (216,000-4,320,000 DZD/year, CLEISS) and IRG treatment differ.  _(CLEISS)_

## Deadlines and filing

How to file and pay the monthly G50 (real regime):
1. Log in to Jibaya'tic if your tax centre uses it, or take the paper Serie G n° 50 to the tax receiver for your head office or main establishment (https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee).
2. Enter the month's taxable sales and output TVA, input TVA, and salary IRG withheld. Box numbers are unverified, so copy them from the form itself.
3. Attach the supplier statement Code TCA art. 29 requires for input TVA (https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee).
4. File within the first 20 days of the month after the period. Payment need not be on the same day as filing, but must fall inside the same time limit.
5. Keep the stamped copy or online acknowledgement as proof. E-payment delayed up to 10 days through no fault of the taxpayer or bank carries no penalty.

| Obligation | Form | Deadline | Official URL |
|---|---|---|---|
| IRG, real regime | G n° 50 | First 20 days of next month | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| IRG, IFU employers | G n° 50 ter | 20 of month after quarter | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu |
| Annual statement | G n° 29, with NIN | 30 April | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| Training and apprenticeship taxes | Special declaration, even if nil | 20 of month after each half-year (art. 196 sexies, LF 2026 art. 21) | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| Cessation | G n° 29 | 10 days | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| Payslips | Keep to fourth following year; show "retenue IRG: neant" where nil | Art. 75 | same |


## Penalties and interest

| Failure | Result | Official URL |
|---|---|---|
| No G n° 50 or payment | 10%, 25% after a month's notice (art. 134-2) | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| No G n° 29 | 5% of annual payroll | same |
| CNAS lateness | unverified | unverified |


## Cross-border points

Staff paid by an employer without an Algerian tax home compute and pay IRG themselves. Pensions to people abroad use the monthly scale (https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires).

## Two worked examples that recompute

**Example 1, simple.** Gross 120,000 DA gives IRG 22,660 and net 86,540.

```oa-check
name: Employee, gross 120,000 DA a month
inputs:
  gross: 120000
steps:
  - cnas: gross * 0.09
  - base: gross - cnas
  - annual: base * 12
  - tax_year: (min(annual,480000)-240000)*0.23 + (min(annual,960000)-480000)*0.27 + (annual-960000)*0.30
  - before: tax_year / 12
  - abate: clamp(before * 0.40, 1000, 1500)
  - irg: before - abate
  - net: gross - cnas - irg
expected:
  irg: 22660.00
  net: 86540.00
```

**Example 2, edge.** Gross 37,000 DA falls in the second abatement band: taxable 33,670 DA; IRG 1,576.92 DA.

```oa-check
name: Employee, gross 37,000 DA a month, second abatement band
inputs:
  gross: 37000
steps:
  - cnas: gross * 0.09
  - base: gross - cnas
  - before: (base * 12 - 240000) * 0.23 / 12
  - abate: clamp(before * 0.40, 1000, 1500)
  - first: before - abate
  - irg: first * 137 / 51 - 27925 / 8
expected:
  irg: 1576.92
```

## Ask the client first

1. Monthly gross and benefits in kind?
2. Disabled or retired?
3. Sector, for the construction add-on?
4. Real regime or IFU employer?
5. Any non-monthly bonus?

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi de finances pour 2026, JO n° 88 of 31 Dec 2025 (read: fiscal articles 5 to 29, 53 to 60); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf | 2026-11-01 |
| Presidential Decree 26-01 of 7 Jan 2026, JO 2026 n° 1 (read: arts. 1 and 2); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf | 2026-11-01 |
| DGI, IRG traitements et salaires, archived copy of 1 Sep 2026 (page cites LF 2026); read for the rates and steps cited | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires | 2026-11-01 |
| DGI, IFU regime page, archived copy of 19 Feb 2025; dated 24 Oct 2023, so LF 2025 overrides it; read for the rates and steps cited | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu | 2026-11-01 |
| CLEISS (French public body), Algeria contributions at 1 Jan 2024; 2024 is the latest edition; read for the rates and steps cited | https://www.cleiss.fr/docs/cotisations/algerie.html | 2026-11-01 |
| DGI notice extending G50 and TFP/TA, archived copy of 8 Oct 2026; read for the rates and steps cited | https://web.archive.org/web/20261008093610/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-delais-g50-taxeformation-taxe-apprentissage | 2026-11-01 |

mfdgi.gov.dz and cnas.dz refused every direct and Chrome connection on 2026-11-01; DGI pages are Internet Archive copies, marked as such.

Not yet confirmed: 26% employer and 35% total headline figures, since CLEISS shows 25% plus 0.5% FNPOS, 34.5% total; whether branch rates changed after 1 Jan 2024; CNAS monthly deadline, DAS date and CNAS late penalties (cnas.dz would not open); old skill figures of 15% plus 2% a month for CNAS lateness; whether the 30,000 DA gate is tested on gross or on taxable pay; salary band handling for part-year staff; dependent and spouse reductions.

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
