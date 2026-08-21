---
name: luxembourg-social-contributions
description: Use this skill whenever asked about Luxembourg social security contributions (cotisations sociales) for employees, employers, or the self-employed (independants). Trigger on phrases like "how much social security in Luxembourg", "CCSS contributions", "Luxembourg payroll deductions", "pension contribution Luxembourg 2026", "assurance dependance", "dependency insurance", "Mutualite des employeurs", "accident insurance Luxembourg", "CNS health contribution", "CNAP pension", "social parameters 2026", "contribution ceiling 5x SSM", "declaration d'entree", "decompte CCSS", or any question about Luxembourg social-security obligations for a payroll, employer registration, or self-employed client. Also trigger when classifying bank statement transactions that relate to CCSS debits, social-security direct debits, or government contribution payments from BCEE, BGL BNP Paribas, Banque de Luxembourg, Spuerkeess, or other Luxembourg banks. This skill covers the 2026 contribution rates (including the pension reform of 18 Dec 2025), employee/employer/self-employed splits, the SSM floor and 5x-SSM ceiling, the dependency abatement, registration and wage-declaration forms, payment deadlines, penalties, and bank statement classification patterns. Personal income tax (PIT) is administered separately by the ACD and is documented here only for context. ALWAYS read this skill before touching any Luxembourg social-contribution work.
version: 0.1
jurisdiction: LU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg Social Security Contributions (Cotisations Sociales)

## Luxembourg Social Security Contributions (Cotisations Sociales) Skill v0.1

**Tier 2 — research-verified.** Figures are corroborated from multiple authoritative sources (CCSS/IGSS social-parameter notices, FEDIL, PwC Worldwide Tax Summaries, CLEISS, Orbitax, Securex, salary.lu) and the Ministry of Health and Social Security pension-reform page. Several primary CCSS/IGSS/MDE/AAA rate-notice pages returned HTTP 403 on direct fetch, so the exact official "avis aux employeurs" rate-notice values should be confirmed on the official PDF before filing. Where a figure is uncertain or period-dependent it is marked **[RESEARCH GAP — reviewer to confirm]**.

## Section 1 -- Quick reference

Read this whole section before computing or classifying anything.

**Section 1 quick reference field table**

| Field | Value |
| --- | --- |
| Country | Luxembourg (Grand Duchy of Luxembourg) |
| Primary legislation | Code de la securite sociale (CSS); long-term care under CSS Book V |
| 2026 change | Loi du 18 decembre 2025 portant reforme de l'assurance pension (Bill 8634), in force 1 Jan 2026: pension contribution raised from 8.00% to 8.50% per party (taxsummaries.pwc.com / m3s.gouvernement.lu) |
| Collection body | Centre commun de la securite sociale (CCSS) -- single collector for all branches; https://ccss.public.lu (CCSS) |
| Oversight | Inspection generale de la securite sociale (IGSS) |
| Branch funds | CNS (health), CNAP (pension), AAA (accident), MDE (employer mutual) |
| Personal income tax authority | Administration des contributions directes (ACD) -- separate; PIT not in the SSC base (PwC) |
| Currency | EUR only |
| Pension rate (each side), 2026 | 8.50% (was 8.00% in 2025) -- fedil.lu / taxsummaries.pwc.com |
| Health rate on ordinary cash salary (each side) | 3.05% (2.80% in-kind + 0.25% cash surcharge) -- fedil.lu / cleiss.fr |
| Dependency (long-term care) | 1.40%, employee only, no ceiling -- taxsummaries.pwc.com |
| Family benefits | 1.70%, employer only, **PUBLIC-sector employers ONLY** (private sector 0%, state-funded) -- cleiss.fr / fedil.lu |
| Occupational health | 0.14%, employer only -- fedil.lu |
| Accident insurance | 0.65% base (2026, was 0.70% in 2025) x bonus-malus factor, employer only -- orbitax.com / fedil.lu |
| Mutualite des employeurs (MDE) | 2026: approx 0.23%-2.66% by absenteeism class, employer only -- pixie.lu |
| Contribution ceiling (5x SSM), in force 1 Jan 2026 | EUR 13,518.68/month (index 968.04, set 1 May 2025) -- fedil.lu / igss.gouvernement.lu |
| Contribution ceiling, from 1 June 2026 | EUR 13,856.65/month (index 992.24) -- salary.lu |
| Contribution floor (SSM), in force 1 Jan 2026 | EUR 2,703.74/month (unqualified) -- fedil.lu |
| Payment | Employer remits both shares to CCSS; consolidated monthly invoice (decompte) -- ccss.public.lu |
| Validated by | Pending -- requires sign-off by a Luxembourg payroll/tax professional |
| Validation date | Pending |

**Branch overview (2026)**  _(cleiss.fr; fedil.lu; taxsummaries.pwc.com; pixie.lu)_

| Branch (fund) | Employee | Employer | Total | Ceiling applies? |
| --- | --- | --- | --- | --- |
| Health/sickness -- in-kind (CNS) | 2.80% | 2.80% | 5.60% | Yes (5x SSM) |
| Health/sickness -- cash surcharge (CNS) | 0.25% | 0.25% | 0.50% | Yes (5x SSM) |
| Pension (CNAP) | 8.50% | 8.50% | 17.00% | Yes (5x SSM) |
| Dependency / long-term care (CNS) | 1.40% | 0% | 1.40% | **No ceiling** |
| Family benefits (CNS/State) | 0% | 1.70% (**public sector only**; private 0%) | 1.70% (public) / 0% (private) | Yes (5x SSM) |
| Occupational health (State service) | 0% | 0.14% | 0.14% | Yes (5x SSM) |
| Accident (AAA) | 0% | 0.65% x factor | 0.65% x factor | Yes (5x SSM) |
| Mutualite des employeurs (MDE) | 0% | approx 0.23%-2.66% | approx 0.23%-2.66% | Yes (5x SSM) |

*Sources: cleiss.fr; fedil.lu; taxsummaries.pwc.com; pixie.lu. The State separately funds an additional 8.50% pension share (m3s.gouvernement.lu); it is not withheld from pay. Family benefits (1.70%) are levied only on PUBLIC-sector employers; in the private sector they are state-funded and the employer pays 0% (cleiss.fr / fedil.lu).*

Health in-kind 2.80 + 2.80 = 5.60 ✓. Cash surcharge 0.25 + 0.25 = 0.50 ✓. Pension 8.50 + 8.50 = 17.00 ✓. Each total row equals the exact sum of its employee and employer columns (family benefits total is 1.70% for public-sector employers and 0% for private-sector employers).

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Accident bonus-malus factor unknown | Assume 1.0 (neutral); effective accident rate = 0.65% (orbitax.com / fedil.lu) |
| MDE class unknown | Do NOT default a rate -- flag for reviewer (2026 spread approx 0.23%-2.66% is too wide) (pixie.lu) |
| Family benefits 1.70% | Apply ONLY for PUBLIC-sector employers; private-sector payroll = 0% (state-funded) (cleiss.fr / fedil.lu) |
| Health rate on ambiguous remuneration | Use 3.05% each side for ordinary periodic cash; 2.80% for pure benefits-in-kind/bonuses (cleiss.fr) |
| Period within 2026 unknown | Default to the index-968.04 parameters in force at 1 Jan 2026; flag if pay date is on/after 1 June 2026 (fedil.lu / salary.lu) |
| Employment status unknown | Ask -- self-employed pay BOTH shares; do not assume employee-only split (cleiss.fr) |
| Dependency abatement period unknown | Use EUR 675.94/month but recompute as 1/4 of the prevailing SSM for the period (fedil.lu) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- gross monthly remuneration, employment status (employee / employer view / self-employed), whether the employer is public or private sector (for the 1.70% family-benefits contribution), and the pay period (to pick the correct index and ceiling). Without the pay period you cannot choose between the index-968.04 set in force at 1 Jan 2026 and the 1 June 2026 indexed set; flag if unknown.

**Recommended** -- whether remuneration is ordinary periodic cash (3.05% health) or benefits-in-kind/bonus (2.80% health); the employer's accident bonus-malus factor; the employer's MDE absenteeism class; and whether the employee is a resident (dependency base can include certain net portfolio income / capital gains for residents).

**Ideal** -- the CCSS consolidated monthly invoice (decompte), the official "avis aux employeurs" rate notice for the period, payroll slips, and the AAA/MDE annual rate notices for the firm.

### Refusal catalogue

- **R-LU-SSC-1 -- MDE class unknown** — Trigger: employer cost requested but the Mutualite des employeurs absenteeism class is not known. Message: "The MDE employer-mutual rate ranges roughly 0.23% to 2.66% (2026) by absenteeism class (pixie.lu). The spread is too wide to default. Provide the firm's MDE class/rate notice before I quantify employer cost."  _(pixie.lu)_
- **R-LU-SSC-2 -- Accident bonus-malus unknown for a precise figure** — Trigger: a precise employer accident contribution is requested. Message: "Accident insurance is the 0.65% (2026) base rate multiplied by the firm's bonus-malus factor (0.85 / 1.0 / 1.1 / 1.3 / 1.5). I will assume 1.0 (neutral) unless the AAA notice says otherwise; flag the assumption to the reviewer."  _(orbitax.com / fedil.lu)_
- **R-LU-SSC-3 -- Contribution arrears / penalties** — Trigger: client has unpaid CCSS contributions from prior periods. Message: "Late contributions accrue default interest of 0.6% per full calendar month (guichet.public.lu). Do not quantify arrears without the CCSS statement. Escalate to a Luxembourg payroll professional."  _(guichet.public.lu)_
- **R-LU-SSC-4 -- Cross-border / posted workers and A1 coverage** — Trigger: worker is a frontalier, posted worker, or has multi-state activity. Message: "Which State's social security applies (and A1 certificate handling) is governed by EU coordination rules and is outside this skill's scope. Escalate to a cross-border specialist."
- **R-LU-SSC-5 -- Personal income tax computation** — Trigger: client asks to compute Luxembourg PIT. Message: "Personal income tax is administered separately by the ACD (progressive 0%-42% over 23 brackets plus a 7%/9% employment-fund solidarity surcharge) and is NOT part of the social-security base. This skill covers contributions only; use the Luxembourg income-tax skill for PIT."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. CCSS contribution payments always EXCLUDE from any VAT return; the employee share is a withholding (not a separate business supply) and the employer share is a payroll on-cost, not a deductible VAT input.

### 3.1 CCSS contribution debits (employer remittance, both shares)

**CCSS contribution debits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CCSS, CENTRE COMMUN | EXCLUDE -- social security remittance | Consolidated monthly decompte |
| CENTRE COMMUN DE LA SECURITE SOCIALE | EXCLUDE -- social security | Full name |
| SECURITE SOCIALE, SECU SOCIALE | EXCLUDE -- social security | Generic reference |
| COTISATIONS SOCIALES, COTISATION CCSS | EXCLUDE -- social security | French-language reference |
| DECOMPTE CCSS | EXCLUDE -- social security | Monthly invoice settlement |

### 3.2 CCSS debits appearing on specific Luxembourg banks

**CCSS debits by bank table**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| BCEE / Spuerkeess | "CCSS" or "CENTRE COMMUN SEC SOC" | EXCLUDE -- social security |
| BGL BNP Paribas | "CCSS DECOMPTE" or "COTISATIONS SOCIALES" | EXCLUDE -- social security |
| Banque de Luxembourg | "SECURITE SOCIALE" or "CCSS" | EXCLUDE -- social security |
| Banque Internationale a Luxembourg (BIL) | "CCSS" or "COTISATION SOCIALE" | EXCLUDE -- social security |
| Revolut / Wise | Rare -- CCSS debits typically come from a local SEPA account | If present, EXCLUDE -- social security |

### 3.3 Income tax payments (NOT social security -- do not confuse)

**Income tax payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACD, ADMINISTRATION DES CONTRIBUTIONS | EXCLUDE -- income tax, not SSC | Direct-tax authority |
| RETENUE D'IMPOT, IMPOT SUR TRAITEMENTS | EXCLUDE -- wage tax (withheld PIT) | Not a social contribution |
| IMPOT DE SOLIDARITE, FONDS POUR L'EMPLOI | EXCLUDE -- employment-fund surcharge | PIT surcharge, not SSC |

### 3.4 Salary and payroll (exclude from SSC classification)

**Salary and payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, TRAITEMENT, REMUNERATION (outgoing) | EXCLUDE -- payroll expense | Net wage to employee, not the SSC remittance |
| SALAIRE, PAIE (incoming) | EXCLUDE -- employment income received | Not an SSC payment |

### 3.5 Benefits received (not contributions)

**Benefits received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNAP, PENSION, RENTE | EXCLUDE -- pension income received | Not a contribution paid |
| CNS, REMBOURSEMENT, INDEMNITE PECUNIAIRE | EXCLUDE -- health reimbursement / sick-pay reimbursement received | Inbound; not a contribution |
| MDE, MUTUALITE -- inbound credit | EXCLUDE -- continued-pay reimbursement received | MDE reimburses the employer; not a contribution paid |
| CAISSE D'ALLOCATIONS, ALLOCATION FAMILIALE | EXCLUDE -- family benefit received | Not a contribution |

## Section 4 -- Worked examples

Six bank statement / payroll classifications for a hypothetical Luxembourg-resident employee and the employing company. All figures use the index-968.04 parameters in force at 1 Jan 2026 unless stated. The employer is assumed **private sector** (family benefits = 0%); accident bonus-malus is assumed 1.0 and MDE is assumed Class 1 (0.23%, 2026), both flagged. Health is taken at 3.05% each side (ordinary periodic cash salary).

### Example 1 -- Standard employee deduction, gross EUR 5,000/month (below ceiling)

**Input line:**
`30.01.2026 ; SALAIRE JANVIER ; CREDIT ; NET DE COTISATIONS ; +4,361.96 ; EUR`

**Reasoning:**
Gross EUR 5,000 is below the ceiling of EUR 13,518.68 in force at 1 Jan 2026 (fedil.lu), so the full gross is the base for capped branches.
- Health 3.05% = 5,000.00 x 0.0305 = EUR 152.50 (fedil.lu)
- Pension 8.50% = 5,000.00 x 0.085 = EUR 425.00 (fedil.lu / taxsummaries.pwc.com)
- Dependency 1.40% on (5,000.00 - 675.94 abatement) = 4,324.06 x 0.014 = EUR 60.54 (taxsummaries.pwc.com)

Total employee SSC = 152.50 + 425.00 + 60.54 = **EUR 638.04**. Net of SSC (before PIT) = 5,000.00 - 638.04 = **EUR 4,361.96**. The credit line reconciles to the cent (PIT is withheld separately by the ACD and is not modelled here).

**Classification:** EXCLUDE from VAT. The net salary credit is employment income; the EUR 638.04 employee SSC is a withholding remitted to CCSS, not a separate expense.

### Example 2 -- Employer's CCSS remittance for the same employee

**Input line:**
`05.03.2026 ; CCSS DECOMPTE ; DEBIT ; COTISATIONS JANVIER ; -1,266.54 ; EUR`

**Reasoning:**
For the EUR 5,000 employee above, the employer share (private-sector employer, accident factor 1.0, MDE Class 1 assumed):
- Health 3.05% = EUR 152.50 (fedil.lu)
- Pension 8.50% = EUR 425.00 (fedil.lu / taxsummaries.pwc.com)
- Occupational health 0.14% = 5,000 x 0.0014 = EUR 7.00 (fedil.lu)
- Accident 0.65% x 1.0 = 5,000 x 0.0065 = EUR 32.50 (orbitax.com / fedil.lu)
- MDE 0.23% (2026 Class 1 assumed) = 5,000 x 0.0023 = EUR 11.50 (pixie.lu) **[RESEARCH GAP — reviewer to confirm the exact 2026 per-class MDE rate against the official MDE notice]**
- Family benefits 1.70% = EUR 0.00 (private-sector employer; state-funded) (cleiss.fr / fedil.lu)

Employer share = 152.50 + 425.00 + 7.00 + 32.50 + 11.50 = EUR 628.50. The CCSS decompte is consolidated and collects BOTH shares (ccss.public.lu): employee 638.04 + employer 628.50 = **EUR 1,266.54**. Reconciles to the cent.

**Classification:** EXCLUDE from VAT. Employer share = payroll on-cost (deductible business expense); employee share = the withholding being remitted. No VAT input.

### Example 3 -- High earner above the ceiling, gross EUR 15,000/month

**Input line:**
`30.01.2026 ; SALAIRE DIRECTION ; CREDIT ; NET DE COTISATIONS ; +13,238.05 ; EUR`

**Reasoning:**
Gross EUR 15,000 exceeds the ceiling EUR 13,518.68 in force at 1 Jan 2026, so capped branches use the ceiling; dependency uses uncapped income.
- Health 3.05% on 13,518.68 = EUR 412.32 (fedil.lu)
- Pension 8.50% on 13,518.68 = EUR 1,149.09 (fedil.lu / taxsummaries.pwc.com)
- Dependency 1.40% on (15,000.00 - 675.94) = 14,324.06 x 0.014 = EUR 200.54 -- **no ceiling** (taxsummaries.pwc.com)

Total employee SSC = 412.32 + 1,149.09 + 200.54 = **EUR 1,761.95**. Net of SSC = 15,000.00 - 1,761.95 = **EUR 13,238.05**. Reconciles to the cent. Note the dependency base (14,324.06) exceeds the contribution ceiling because dependency has no ceiling.

**Classification:** EXCLUDE from VAT. Demonstrates the ceiling on health/pension and the absence of a ceiling on dependency.

### Example 4 -- ACD wage-tax debit (NOT social security)

**Input line:**
`10.02.2026 ; ADMINISTRATION DES CONTRIBUTIONS ; DEBIT ; RETENUE IMPOT JANVIER ; -2,100.00 ; EUR`

**Reasoning:**
Matches "ADMINISTRATION DES CONTRIBUTIONS" (pattern 3.3). This is the withheld wage tax (retenue d'impot sur traitements) remitted to the ACD, plus the employment-fund solidarity surcharge -- NOT a social contribution. Do not classify as SSC. Income tax sits outside the social-security base (taxsummaries.pwc.com).

**Classification:** EXCLUDE from VAT. Income-tax remittance, NOT social security.

### Example 5 -- Self-employed (independant) provisional contribution, first year

**Input line:**
`05.04.2026 ; CCSS ; DEBIT ; COTISATION INDEPENDANT AVRIL ; -670.53 ; EUR`

**Reasoning:**
A first-year self-employed person is provisionally based on the SSM (cleiss.fr). The self-employed pay BOTH shares. On the SSM EUR 2,703.74/month (in force 1 Jan 2026, fedil.lu):
- Pension 17.00% (8.50% + 8.50%) = 2,703.74 x 0.17 = EUR 459.64 (cleiss.fr / fedil.lu)
- Health 6.10% (in-kind 5.60% + cash 0.50%, both shares) = 2,703.74 x 0.061 = EUR 164.93 (cleiss.fr) **[RESEARCH GAP — whether the 0.50% cash surcharge applies to the independant depends on benefit entitlement; reviewer to confirm]**
- Dependency 1.40% on (2,703.74 - 675.94) = 2,027.80 x 0.014 = EUR 28.39 (taxsummaries.pwc.com)
- Accident 0.65% x 1.0 = 2,703.74 x 0.0065 = EUR 17.57 (orbitax.com / cleiss.fr)

Monthly total = 459.64 + 164.93 + 28.39 + 17.57 = **EUR 670.53**. The State adds a further 8.50% to the self-employed pension (cleiss.fr); that is not debited from the contributor. Reconcile against the CCSS provisional assessment.

**Classification:** EXCLUDE from VAT. Self-employed CCSS contribution -- a personal statutory obligation, not a business supply.

### Example 6 -- Benefits-in-kind / bonus (health at 2.80%, not 3.05%)

**Input line:**
`20.12.2026 ; PRIME DE FIN D'ANNEE ; CREDIT ; BONUS NON-PERIODIQUE ; +3,000.00 ; EUR`

**Reasoning:**
A non-periodic bonus is treated as benefits/non-periodic remuneration: the 0.25% cash-benefit surcharge does NOT apply, so health is 2.80% (not 3.05%) on this component (cleiss.fr). Assume the year-to-date base is below the ceiling. (Note: from 1 June 2026 the index-992.24 parameters apply; this December 2026 example still uses the post-1-June ceiling of EUR 13,856.65 for the cap test, but the EUR 3,000 bonus is below either ceiling.)
- Health 2.80% = 3,000.00 x 0.028 = EUR 84.00
- Pension 8.50% = 3,000.00 x 0.085 = EUR 255.00 (fedil.lu / taxsummaries.pwc.com)
- Dependency 1.40% = 3,000.00 x 0.014 = EUR 42.00, subject to the abatement note below (taxsummaries.pwc.com)

Employee SSC on the bonus (health + pension) = 84.00 + 255.00 = **EUR 339.00**, plus dependency of up to EUR 42.00. **[RESEARCH GAP — reviewer to confirm whether the monthly dependency abatement (EUR 692.83 from 1 June 2026) is consumed once per month across all components; if already used on regular salary it is not applied again here.]**

**Classification:** EXCLUDE from VAT. Demonstrates the 2.80% (not 3.05%) health rate on non-periodic remuneration.

## Section 5 -- Tier 1 rules

These rules apply when the pay period, gross remuneration, and remuneration type are clear. Apply exactly as written.

### Rule 1 -- Contribution formula (employee, ordinary cash salary)

- **employee_SSC formula** — employee_SSC = health_3.05% x min(gross, ceiling) + pension_8.50% x min(gross, ceiling) + dependency_1.40% x max(0, gross - 675.94)   // dependency has NO ceiling Health 3.05% = 2.80% in-kind + 0.25% cash surcharge (fedil.lu); pension 8.50% (fedil.lu / taxsummaries.pwc.com); dependency 1.40% with the EUR 675.94/month abatement and no ceiling (taxsummaries.pwc.com).  _(fedil.lu / taxsummaries.pwc.com)_

### Rule 2 -- Contribution formula (employer)

- **employer_SSC formula** — employer_SSC = health_3.05% x min(gross, ceiling) + pension_8.50% x min(gross, ceiling) + occupational_0.14% x min(gross, ceiling) + accident_0.65% x bonus_malus x min(gross, ceiling) + MDE_class_rate x min(gross, ceiling) + family_1.70% x min(gross, ceiling)   // PUBLIC-SECTOR EMPLOYERS ONLY; private sector = 0% Employer pays NO dependency contribution (employee-only). Family benefits (1.70%) apply ONLY to public-sector employers; in the private sector they are state-funded and the employer pays 0%. Sources: fedil.lu; cleiss.fr; pixie.lu.  _(fedil.lu; cleiss.fr; pixie.lu)_

### Rule 3 -- The pension rate is 8.50% each side in 2026 (was 8.00% in 2025)

- **Pension rate 2026** — Combined employee + employer = 17.00% in 2026 (was 16.00% in 2025), plus an 8.50% State share (total 25.50%, was 24.00%). Effective 1 Jan 2026 under the loi du 18 decembre 2025 portant reforme de l'assurance pension (Bill 8634), scheduled to hold through 2032.  _(taxsummaries.pwc.com / m3s.gouvernement.lu / orbitax.com)_

### Rule 4 -- Health is 3.05% on cash salary, 2.80% on benefits/bonuses

- **Health rate by remuneration type** — The 0.25% cash-benefit surcharge applies only to periodic cash remuneration. Pure benefits-in-kind and non-periodic bonuses take 2.80%.  _(fedil.lu / cleiss.fr)_

### Rule 5 -- Dependency insurance: 1.40%, employee only, no ceiling, with abatement

- **Dependency insurance rule** — Levied on professional income (and, for residents, certain net portfolio income/capital gains) reduced by EUR 675.94/month (= 1/4 of the SSM; the official notice rounds 2,703.74 / 4 to EUR 675.93 -- a 1-cent difference; reconcile to the value on the prevailing CCSS notice). No employer share and NO upper ceiling. The abatement rises with each SSM indexation.  _(taxsummaries.pwc.com)_

### Rule 6 -- The 5x-SSM ceiling caps all branches except dependency

- **Ceiling applies to which branches** — The ceiling applies to health, pension, family benefits, occupational health, accident and MDE; it does NOT apply to dependency.  _(fedil.lu)_

**5x SSM ceiling table**

| Effective | Ceiling (5x SSM) | Index | Source |
| --- | --- | --- | --- |
| In force at 1 Jan 2026 (index set 1 May 2025) | EUR 13,518.68/month (approx EUR 162,224/year) | 968.04 | fedil.lu / igss.gouvernement.lu |
| From 1 June 2026 | EUR 13,856.65/month (EUR 166,279.80/year) | 992.24 | salary.lu |

### Rule 7 -- The SSM is the contribution floor

**SSM floor table**

| Effective | SSM unqualified (age 18+) | SSM qualified (+20%) | Source |
| --- | --- | --- | --- |
| In force at 1 Jan 2026 (index set 1 May 2025) | EUR 2,703.74/month | EUR 3,244.48/month | fedil.lu |
| From 1 June 2026 | EUR 2,771.33/month | EUR 3,325.59/month | salary.lu |

- **SSM floor application** — The SSM is the floor for health, pension and accident.  _(fedil.lu)_

### Rule 8 -- Accident insurance = 0.65% base x bonus-malus

- **Accident insurance rule** — Base rate 0.65% for 2026 (was 0.70% in 2024-2025), employer only, multiplied by the firm's bonus-malus factor of 0.85 / 1.0 / 1.1 / 1.3 / 1.5 set on the prior accident record (reference period 1 Apr Y-2 to 31 Mar Y-1).  _(orbitax.com / fedil.lu)_

### Rule 9 -- Mutualite des employeurs (MDE): class-based, employer only

- **MDE rule** — Reimburses continued pay during employee sickness. Employer-only, assigned to one of 4 absenteeism classes; 2026 rates are approximately Class 1 = 0.23%, Class 2 = 0.95%, Class 3 = 1.56%, Class 4 = 2.66%. **[RESEARCH GAP — confirm exact 2026 per-class percentages against the official MDE/CCSS rate notice.]**  _(pixie.lu)_

### Rule 10 -- Self-employed pay BOTH shares

- **Self-employed contributions** — Pension 17% total in 2026, health 5.60% in-kind + 0.50% cash, dependency 1.40%, accident 0.65% x factor. SSM is the floor and 5x SSM the ceiling; CCSS provisionally bases the first year on the SSM. The State adds 8.50% to the self-employed pension.  _(cleiss.fr)_

### Rule 11 -- Collection and payment

- **Collection and payment rule** — The employer withholds the employee share and remits BOTH shares to the CCSS, which issues a consolidated monthly invoice (decompte) covering all branches.  _(ccss.public.lu)_

### Rule 12 -- Registration and declaration deadlines

**Registration and declaration deadlines table**

| Obligation | Deadline | Channel | Source |
| --- | --- | --- | --- |
| Employer operating declaration (immatriculation) | Within 8 days of first employee's start | CCSS | ccss.public.lu |
| Entry declaration (declaration d'entree / DPE) | Within 8 days of hiring | SECUline (DECAFF) / MyGuichet.lu | ccss.public.lu |
| Exit declaration (declaration de sortie) | Within 8 days of the event | SECUline / MyGuichet.lu | guichet.public.lu |
| Monthly wage declaration (declaration de salaires) | By the 24th of the month after the salary period (electronic via SECUline) | SECUline | ccss.public.lu |
| Pay the monthly CCSS invoice (decompte) | Within 10 days of the statement date (statement issued approx 2 months after the invoiced month) | CCSS | guichet.public.lu |

### Rule 13 -- Personal income tax is separate from SSC

- **PIT separation rule** — PIT is administered by the ACD (progressive 0%-42% over 23 brackets, plus a 7%/9% employment-fund solidarity surcharge); it is not part of the social-security contribution base. Do not mix PIT into the contribution computation.  _(taxsummaries.pwc.com)_

## Section 6 -- Tier 2 catalogue

When data is ambiguous or circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Pay date straddling the 1 June 2026 indexation

**Trigger:** The salary period or pay date is near 1 June 2026 and it is unclear which index applies.

**Issue:** From 1 June 2026 the SSM, ceiling (EUR 13,856.65) and the dependency abatement all change (salary.lu). Using the wrong parameter set mis-states both employee and employer contributions for high earners and the abatement.

**Action:** Confirm the exact period; apply the index-968.04 set (in force at 1 Jan 2026) before 1 June, the index-992.24 values on/after.

### T2-2 -- MDE class and accident bonus-malus unknown

**Trigger:** Employer cost requested without the firm's MDE class or AAA bonus-malus factor.

**Issue:** MDE spans approx 0.23%-2.66% in 2026 (pixie.lu) and accident is 0.65% x {0.85 / 1.0 / 1.1 / 1.3 / 1.5} (orbitax.com / fedil.lu). Both materially affect employer cost.

**Action:** Use accident factor 1.0 only as a flagged assumption; do NOT default an MDE rate -- request the AAA/MDE notices.

### T2-3 -- Public vs private sector (family benefits)

**Trigger:** Employer cost requested without knowing whether the employer is public or private sector.

**Issue:** The 1.70% family-benefits contribution applies ONLY to public-sector employers; in the private sector it is state-funded and the employer pays 0% (cleiss.fr / fedil.lu). Defaulting to "include" overstates private-sector employer cost.

**Action:** Default to private sector (0% family benefits) and flag; confirm public-sector status before adding 1.70%.

### T2-4 -- Resident dependency base beyond salary

**Trigger:** Resident client with portfolio income or capital gains.

**Issue:** For residents the dependency base can include certain net portfolio income and capital gains, not just professional income (taxsummaries.pwc.com). This is outside ordinary payroll.

**Action:** Flag for reviewer; the dependency base may exceed wages.

### T2-5 -- Self-employed health split and first-year provisional base

**Trigger:** Self-employed contribution requested.

**Issue:** Whether the 0.50% cash-benefit surcharge applies to an independant depends on benefit entitlement; first-year contributions are provisional on the SSM and later re-assessed (cleiss.fr).

**Action:** Flag for reviewer; reconcile against the CCSS provisional and final assessments.

### T2-6 -- Contribution arrears and default interest

**Trigger:** Unpaid CCSS contributions from prior periods.

**Issue:** Default interest accrues at 0.6% per full calendar month from the 1st day of the 1st month after the due date (guichet.public.lu); separately, late entry/exit declarations attract a fine.

**Action:** Do not quantify arrears without the CCSS statement. Escalate.

### T2-7 -- Cross-border / posted workers (A1)

**Trigger:** Frontalier, posted worker, or multi-state activity.

**Issue:** Applicable legislation and A1 certificates are governed by EU coordination rules.

**Action:** Escalate to a cross-border specialist; do not assume Luxembourg coverage.

## Section 7 -- Excel working paper template

When producing a Luxembourg SSC computation, structure the working paper as follows:

```
LUXEMBOURG SOCIAL CONTRIBUTIONS -- WORKING PAPER
Client: [name]
Pay period: [month / year]              Index applied: [968.04 / 992.24]
Prepared: [date]

INPUT DATA
  Employment status:               [Employee / Employer view / Self-employed]
  Employer sector:                 [Private / Public]   (family benefits public sector only)
  Gross remuneration (month):      EUR [____]
  Remuneration type:               [Ordinary cash / Benefits-in-kind / Bonus]
  Resident?                        [YES/NO]
  Accident bonus-malus factor:     [0.85 / 1.0 / 1.1 / 1.3 / 1.5]   (default 1.0, FLAG)
  MDE absenteeism class / rate:    [Class __ / ____%]   (FLAG if unknown)

PARAMETERS (pick by period)
  Ceiling (5x SSM):                EUR [13,518.68 (1 Jan) / 13,856.65 (1 Jun)]
  SSM floor (unqualified):         EUR [2,703.74 (1 Jan) / 2,771.33 (1 Jun)]
  Dependency abatement (1/4 SSM):  EUR [675.94 -> recompute for period]

EMPLOYEE SHARE
  Capped base (min(gross,ceiling)):  EUR [____]
  Health (3.05% cash / 2.80% BIK):   EUR [____]
  Pension (8.50%):                   EUR [____]
  Dependency (1.40% x (gross-abat)): EUR [____]   (NO ceiling)
  Employee SSC total:                EUR [____]
  Net of SSC (before PIT):           EUR [____]

EMPLOYER SHARE
  Health (3.05%):                    EUR [____]
  Pension (8.50%):                   EUR [____]
  Occupational health (0.14%):       EUR [____]
  Accident (0.65% x factor):         EUR [____]
  MDE (class rate):                  EUR [____]
  Family benefits (1.70%):           EUR [____]   (PUBLIC sector only; private = 0)
  Employer SSC total:                EUR [____]

CCSS DECOMPTE
  Total remitted (employee+employer): EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags + RESEARCH GAP markers]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their cost impact]
```

## Section 8 -- Bank statement reading guide

### How CCSS contribution debits appear on Luxembourg bank statements

**BCEE / Spuerkeess (Banque et Caisse d'Epargne de l'Etat):**
- Description: "CCSS", "CENTRE COMMUN SEC SOC", "COTISATIONS SOCIALES"
- Timing: monthly, after the CCSS decompte is issued (statement approx 2 months after the invoiced month; payable within 10 days of the statement)
- Amount: combined employee + employer share for all branches

**BGL BNP Paribas:**
- Description: "CCSS DECOMPTE" or "COTISATIONS SOCIALES"
- Timing: same monthly cycle

**Banque de Luxembourg / BIL:**
- Description: "SECURITE SOCIALE", "CCSS", "COTISATION SOCIALE"
- Timing: same monthly cycle

**Key identification tips:**
1. CCSS contribution remittances are outgoing (DEBIT). Inbound CNAP/CNS/MDE credits are benefits or reimbursements, NOT contributions.
2. The decompte is consolidated -- a single CCSS debit covers ALL branches (health, pension, dependency, family, occupational, accident, MDE); do not expect separate lines per branch.
3. Do not confuse CCSS debits with ACD debits ("ADMINISTRATION DES CONTRIBUTIONS", "RETENUE D'IMPOT") -- those are income tax, not social security.
4. The employer's debit collects BOTH the withheld employee share and the employer share.
5. Irregular CCSS lump sums may include arrears + 0.6%/month default interest -- flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no payroll detail:

1. **Scan for CCSS debits** -- identify all outgoing payments matching Section 3 patterns.
2. **Separate CCSS from ACD** -- exclude any "ADMINISTRATION DES CONTRIBUTIONS" / "RETENUE D'IMPOT" lines (those are income tax, not SSC).
3. **Do not split branches from a single decompte** -- the consolidated invoice cannot be decomposed into branch shares from the bank line alone; request the CCSS decompte detail.
4. **Estimate the headline split only with a flag:**
   - Approx combined (employer + employee) burden roughly 24%-27% of gross (private sector, before MDE/accident spread); employee share = component sum 8.50% + 3.05% + 1.40% = 12.95% on ordinary cash salary before the dependency abatement effect. (cleiss.fr / fedil.lu)
5. **Flag for reviewer:** "SSC figures derived from bank statement amounts only. Pay period/index, employer sector, accident bonus-malus, and MDE class have not been verified. A reviewer must confirm against the CCSS decompte before relying on these figures."

## Section 10 -- Reference material

### Branch rate table (2026, with 2025 comparatives)

**Branch rate table (2026, with 2025 comparatives)**

placeholder

**Branch rate table (2026, with 2025 comparatives)**  _(cleiss.fr / fedil.lu / taxsummaries.pwc.com / orbitax.com / pixie.lu)_

| Branch | 2026 employee | 2026 employer | 2025 employee | 2025 employer | Source |
| --- | --- | --- | --- | --- | --- |
| Health -- in-kind | 2.80% | 2.80% | 2.80% | 2.80% | cleiss.fr |
| Health -- cash surcharge | 0.25% | 0.25% | 0.25% | 0.25% | fedil.lu |
| Pension | 8.50% | 8.50% | 8.00% | 8.00% | fedil.lu / taxsummaries.pwc.com |
| Dependency | 1.40% | 0% | 1.40% | 0% | taxsummaries.pwc.com |
| Family benefits (public sector only) | 0% | 1.70% (public) / 0% (private) | 0% | 1.70% (public) / 0% (private) | cleiss.fr / fedil.lu |
| Occupational health | 0% | 0.14% | 0% | 0.14% | fedil.lu |
| Accident (base, pre-factor) | 0% | 0.65% | 0% | 0.70% | orbitax.com / fedil.lu |
| MDE (class-dependent) | 0% | approx 0.23%-2.66% | 0% | approx 0.07%-2.64% | pixie.lu |

### Thresholds (with provenance)

**Thresholds (with provenance)**  _(fedil.lu / igss.gouvernement.lu / salary.lu / taxsummaries.pwc.com / orbitax.com)_

| Item | Value | Source |
| --- | --- | --- |
| Ceiling (5x SSM), in force 1 Jan 2026 | EUR 13,518.68/month (approx EUR 162,224/year), index 968.04 (set 1 May 2025) | fedil.lu / igss.gouvernement.lu |
| Ceiling (5x SSM), from 1 June 2026 | EUR 13,856.65/month (EUR 166,279.80/year), index 992.24 | salary.lu |
| SSM unqualified, in force 1 Jan 2026 | EUR 2,703.74/month | fedil.lu |
| SSM qualified (+20%), in force 1 Jan 2026 | EUR 3,244.48/month | fedil.lu |
| SSM unqualified, from 1 June 2026 | EUR 2,771.33/month | salary.lu |
| SSM qualified (+20%), from 1 June 2026 | EUR 3,325.59/month | salary.lu |
| Dependency abatement (in force 1 Jan 2026) | EUR 675.94/month (1/4 SSM; official notice rounds to EUR 675.93); recompute per period | fedil.lu / taxsummaries.pwc.com |
| 2025 baseline (1 Jan 2025) | SSM EUR 2,637.79/month, ceiling EUR 13,188.96/month (index 944.43) | orbitax.com |

Arithmetic check: 5 x 2,703.74 = 13,518.70 (the official ceiling EUR 13,518.68 differs by rounding at the index; use the cited official figure). 5 x 2,771.33 = 13,856.65 ✓. Abatement 2,703.74 / 4 = 675.935 ≈ 675.94 (official notice rounds to 675.93). From 1 June 2026: 2,771.33 / 4 = 692.83.

### Approximate total burden (2026)

**Approximate total burden (2026)**  _(fedil.lu / cleiss.fr / pixie.lu)_

| View | Approx burden | Source |
| --- | --- | --- |
| Employee, ordinary cash salary | component sum 8.50% + 3.05% + 1.40% = 12.95% (the 1.40% dependency portion is on a different, post-abatement, uncapped base, so the effective headline is slightly lower) | fedil.lu / cleiss.fr |
| Employer (private sector) | approx 11.7%-14.3% (pension 8.50% + health 3.05% + occupational 0.14% + accident 0.65% x factor + MDE 0.23%-2.66%; family benefits 0% in private sector) | fedil.lu / pixie.lu |
| Combined (employer + employee, private sector) | roughly 24%-27% of gross | fedil.lu |

### Forms

**Forms**  _(ccss.public.lu / guichet.public.lu)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Declaration d'entree (DPE) | Register a new employee's start | Within 8 days of hiring | ccss.public.lu |
| Declaration de sortie | Notify end of employment | Within 8 days of the event | guichet.public.lu |
| Immatriculation employeur | Register as an employer | Within 8 days of first employee's start | ccss.public.lu |
| Declaration de salaires | Declare wages/contribution bases | By the 24th of the month after the salary period (SECUline) | ccss.public.lu |
| Paiement du decompte | Settle the monthly CCSS invoice | Within 10 days of the statement date | guichet.public.lu |

### Penalties

**Penalties**  _(guichet.public.lu)_

| Penalty | Amount | Source |
| --- | --- | --- |
| Late entry/exit declaration | EUR 50 per month of delay, capped at EUR 2,500 (after a 30-day tolerance beyond the 8-day deadline) | guichet.public.lu |
| Late payment of contributions | Default interest 0.6% per full calendar month, from the 1st day of the 1st month after the due date | guichet.public.lu |

### Test suite

Test 1: Employee, gross EUR 5,000/month, in force 1 Jan 2026, ordinary cash. -> Health 152.50 + pension 425.00 + dependency 60.54 = employee SSC EUR 638.04; net of SSC EUR 4,361.96. (5,000 x 0.0305 = 152.50; 5,000 x 0.085 = 425.00; (5,000 - 675.94) x 0.014 = 60.54.)

Test 2: Employer share for Test 1 (private sector, factor 1.0, MDE Class 1 = 0.23%). -> 152.50 + 425.00 + 7.00 + 32.50 + 11.50 = employer SSC EUR 628.50. CCSS decompte total = 638.04 + 628.50 = EUR 1,266.54. (MDE rate flagged; family benefits 0% in private sector.)

Test 3: Employee, gross EUR 15,000/month, in force 1 Jan 2026 (above ceiling). -> Health 412.32 + pension 1,149.09 + dependency 200.54 = EUR 1,761.95; net EUR 13,238.05. (Capped base 13,518.68 for health/pension; dependency base 14,324.06 uncapped.)

Test 4: Bonus EUR 3,000 (non-periodic), employee. -> Health at 2.80% = 84.00; pension 8.50% = 255.00. Health + pension = EUR 339.00; dependency up to 42.00 depends on whether the monthly abatement was already consumed [RESEARCH GAP].

Test 5: Self-employed, first year, provisional on SSM EUR 2,703.74, in force 1 Jan 2026. -> Pension 17% = 459.64; health 6.10% = 164.93 (flagged); dependency 1.40% on (2,703.74 - 675.94) = 28.39; accident 0.65% = 17.57. Total = EUR 670.53.

Test 6: Pay period from 1 June 2026, ceiling test, gross EUR 14,000. -> Capped base = ceiling EUR 13,856.65; pension 8.50% = 1,177.82; health 3.05% = 422.63; dependency on (14,000 - 692.83 abatement) = 13,307.17 x 0.014 = 186.30 uncapped. (5 x 2,771.33 = 13,856.65 ✓; abatement = 2,771.33 / 4 = 692.83 for this period.)

Test 7: ACD debit "RETENUE D'IMPOT". -> NOT social security; income tax remittance; exclude from SSC.

Test 8: Inbound "CNAP PENSION" credit. -> Pension income RECEIVED, not a contribution; do not classify as SSC.

### Prohibitions

- **2026/2025 pension rate mismatch prohibition** — NEVER use the 2025 pension rate (8.00%) for a 2026 period -- it rose to 8.50% each side under the loi du 18 decembre 2025; equally, NEVER apply the 2026 rate (8.50%) to a 2025 period.  _(loi du 18 decembre 2025)_
- **Dependency ceiling prohibition** — NEVER apply the 5x-SSM ceiling to the dependency contribution -- dependency has NO ceiling.  _(Prohibitions section)_
- **Employer dependency share prohibition** — NEVER charge an employer share of dependency -- it is employee-only.  _(Prohibitions section)_
- **Private-sector family benefits prohibition** — NEVER charge a private-sector employer the 1.70% family-benefits contribution -- it is public-sector only (state-funded in the private sector).  _(Prohibitions section)_
- **MDE default rate prohibition** — NEVER default an MDE rate when the class is unknown -- the 2026 spread (0.23%-2.66%) is too wide; flag instead.  _(Prohibitions section)_
- **Health rate on bonus prohibition** — NEVER use 3.05% health on a pure bonus/benefit-in-kind -- the 0.25% cash surcharge applies only to periodic cash; use 2.80%.  _(Prohibitions section)_
- **Index parameter mixing prohibition** — NEVER mix the index-968.04 (in force 1 Jan 2026) and the 1 June 2026 (index 992.24) parameter sets within one period.  _(Prohibitions section)_
- **PIT/SSC base separation prohibition** — NEVER fold personal income tax into the social-security base -- the ACD administers PIT separately.  _(Prohibitions section)_
- **Arrears quantification prohibition** — NEVER quantify contribution arrears without the CCSS statement -- default interest at 0.6%/month accrues.  _(Prohibitions section)_
- **Definitiveness disclaimer** — NEVER present these figures as definitive -- this is a Tier 2 research-verified skill; the official CCSS "avis aux employeurs" rate notice must be confirmed before filing.  _(Prohibitions section)_
- **Research gap prohibition** — NEVER ignore a RESEARCH GAP marker -- each must be resolved by a reviewer before relying on the affected figure.  _(Prohibitions section)_

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
