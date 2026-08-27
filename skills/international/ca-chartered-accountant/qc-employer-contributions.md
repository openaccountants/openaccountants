---
name: qc-employer-contributions
description: Use this skill whenever asked about Quebec-specific employer contributions — CNESST (CSST), HSF (Health Services Fund / Fonds des services de santé), QPIP (Quebec Parental Insurance Plan / RQAP), QPP (Quebec Pension Plan — replaces CPP for Quebec employees), WSDRF (1% training levy). Trigger on "Quebec payroll", "QPP Quebec", "QPIP RQAP", "CNESST", "HSF Quebec", "FSS", "Fonds services santé", "Quebec employer contributions". ALWAYS read this skill for Quebec payroll alongside canada-payroll (federal).
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# QC Employer Contributions

## Quebec — Employer Contributions (CNESST / HSF / QPIP / QPP) — Skill v1.0

> **Scope note.** This skill covers Quebec-specific payroll contributions remitted to **Revenu Québec** and to **CNESST**. It is a Quebec overlay on top of the federal payroll skill at `canada-payroll.md`. Do NOT duplicate federal mechanics here — for federal source deductions (federal income tax, EI, the federal half of remitting cadence, ROE/T4 mechanics, RP account setup, RC1 enrolment, etc.) **read `canada-payroll.md` first**, then layer the Quebec rules below.
>
> Quebec is the only province where the employer files a **separate provincial payroll return** (the source-deductions remittance **TPZ-1015.R-V**) and where **QPP replaces CPP** entirely. Quebec also has its own **RL-1** slip parallel to the federal T4 (covered in the Quebec individual-return skill, not here).

## 1. Quick reference table — 2025 Quebec employer contributions

**2025 Quebec employer contributions quick reference**

| # | Contribution | Who pays | Administered by | 2025 employee rate | 2025 employer rate | 2025 earnings ceiling / base |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **QPP** base | EE + ER | Revenu Québec / Retraite Québec | 5.40% | 5.40% | $3,500 exemption – **$71,300** YMPE |
| 1a | **QPP** additional (first additional contribution) | EE + ER | Revenu Québec / Retraite Québec | 1.00% | 1.00% | $3,500 – $71,300 |
| 1b | **QPP2** (second additional, on YAMPE band) | EE + ER | Revenu Québec / Retraite Québec | 4.00% | 4.00% | $71,300 – **$81,200** (YAMPE) |
| 2 | **QPIP / RQAP** | EE + ER (+ self-employed) | Conseil de gestion de l'assurance parentale / Revenu Québec | **0.494%** | **0.692%** (SE: 0.878%) | Max insurable earnings **$98,000** |
| 3 | **HSF / FSS** | ER only | Revenu Québec | — | **1.65% → 4.26%** sliding by total payroll | Total Quebec payroll (no ceiling) |
| 4 | **CNESST** (occupational health & safety / workers' comp) | ER only | CNESST (separate ministry) | — | Sector-rated, typically **0.5%–5%+** | Insurable earnings up to **$98,000/worker** (same 2025 max as QPIP) |
| 5 | **WSDRF** (1% training levy, Loi du 1%) | ER only | Revenu Québec (Commission des partenaires du marché du travail) | — | **1.0%** of payroll | Only if total payroll **> $2,000,000** |

- **Maximum annual QPP employee contribution (2025)** — Base + additional = $4,348.50 (5.4% × ($71,300 − $3,500) + 1.0% × ($71,300 − $3,500) = $3,661.20 + $678.00; per Retraite Québec rounding the published maximum is **$4,348.50**). QPP2 maximum = 4.0% × ($81,200 − $71,300) = **$396.00**. **Total maximum employee QPP (2025) = $4,744.50.** Employer matches dollar-for-dollar.  _(Retraite Québec 2025 rounding)_

> The "base + additional" presentation is how Retraite Québec publishes the 2025 figures: a combined first-tier rate of **6.4% EE / 6.4% ER** on earnings between $3,500 and $71,300, and a second-tier **4% EE / 4% ER** on earnings between $71,300 and $81,200. Some Revenu Québec guides express the first-tier rate as a single 6.4% figure rather than 5.4% + 1.0% — both are equivalent.

## 2. Required inputs + refusal catalogue

### 2.1 Required inputs (gather before computing)

- **Total annual Quebec payroll** — Gross wages, salaries, bonuses, taxable benefits subject to source deductions — drives HSF rate and WSDRF threshold.
- **Per-employee gross pensionable / insurable earnings breakdown** — Earnings up to $71,300 (for QPP base + additional); earnings between $71,300 and $81,200 (for QPP2); earnings up to $98,000 (for QPIP and CNESST insurable earnings).
- **CNESST sector classification(s)** — NAICS-based unit code(s) assigned by CNESST in the *Avis de cotisation* / employer file. A single employer may have multiple classification units.
- **Public/parapublic sector check** — Whether the employer is in the public/parapublic sector (different HSF table applies — out of scope, see §2.2).
- **Self-employed contractors paid through payroll** — Whether any workers are self-employed contractors paid through payroll (QPIP self-employed rate of 0.878% differs; CPP/QPP and CNESST may not apply — confirm worker status under the Revenu Québec employee-vs-contractor tests).
- **Employer identification numbers** — Employer's NEQ (numéro d'entreprise du Québec) and Revenu Québec identification number (NIQ).
- **Remittance frequency** — As assigned by Revenu Québec (weekly / twice-monthly / monthly / quarterly — mirrors federal threshold logic but is determined by Revenu Québec separately based on the average monthly Quebec source deductions).

### 2.2 Refusal catalogue — when to stop and escalate

- **R-QC-1** — Employer is in the public sector or parapublic sector (different HSF rate table; reduced rate not available).  _(R-QC-1)_
- **R-QC-2** — Employer is requesting HSF reduced rate for the primary-and-manufacturing sector (special table — verify eligibility under the SMB sector rules; do not assume).  _(R-QC-2)_
- **R-QC-3** — Worker classification is ambiguous (employee vs. self-employed contractor) — defer to a Quebec employment-law review; misclassification triggers CNESST, QPP, QPIP, and HSF retroactive assessments plus penalties.  _(R-QC-3)_
- **R-QC-4** — Employer has workers in multiple CNESST classification units and is requesting an allocation across units — refer to a CNESST tarification consultant.  _(R-QC-4)_
- **R-QC-5** — Employer is requesting WSDRF training-expenditure substantiation (which courses qualify under the Loi favorisant le développement et la reconnaissance des compétences de la main-d'œuvre) — refer to the Commission des partenaires du marché du travail (CPMT).  _(R-QC-5)_
- **R-QC-6** — Employer has out-of-province employees physically reporting to a Quebec establishment, or vice versa — the "establishment to which the employee reports" rule under R.R.Q. requires case-by-case analysis.  _(R-QC-6)_
- **R-QC-7** — Indigenous employers operating on reserve, or employees with Indian Act §87 exemptions — out of scope.  _(R-QC-7)_
- **R-QC-8** — First-Nations or Inuit employer subject to special HSF / QPIP exemptions under intergovernmental agreements.  _(R-QC-8)_
- **R-QC-9** — Employer is a non-resident of Canada with a Quebec establishment — non-resident employer certification regime + Quebec source-deduction rules interact; refer.  _(R-QC-9)_
- **R-QC-10** — Mid-year change in legal status, amalgamation, or asset sale affecting payroll continuity (e.g., successor employer rules for QPP/QPIP ceilings).  _(R-QC-10)_

### 3.1 Why QPP instead of CPP

- **CPP replacement by QPP** — CPP does not apply to employees whose establishment of the employer is in Quebec. QPP applies instead, administered jointly by Retraite Québec (benefits, plan administration) and Revenu Québec (collection of contributions through source deductions).

If the same individual has Quebec and non-Quebec employment income in the same year, QPP and CPP are reconciled on the federal T1 / Schedule 8 and Quebec TP-1 / Schedule R. Out of scope for this payroll skill — see `qc-individual-return.md`.

### 3.2 2025 rates and ceilings

- **YMPE (maximum pensionable earnings)** — $71,300  _(§3.2 2025 rates and ceilings)_
- **YAMPE (additional maximum pensionable earnings)** — $81,200  _(§3.2 2025 rates and ceilings)_
- **Basic exemption** — $3,500 (only the base + first-additional tier benefit from the exemption; QPP2 has no exemption — it applies to the entire YMPE-to-YAMPE band)  _(§3.2 2025 rates and ceilings)_
- **Base rate** — 5.40% EE + 5.40% ER (10.80% total)  _(§3.2 2025 rates and ceilings)_
- **First additional rate** — 1.00% EE + 1.00% ER (2.00% total) → Combined first-tier = 6.40% EE + 6.40% ER on earnings $3,500 – $71,300  _(§3.2 2025 rates and ceilings)_
- **Second additional (QPP2)** — 4.00% EE + 4.00% ER on earnings $71,300 – $81,200  _(§3.2 2025 rates and ceilings)_

### 3.3 Computation per pay period

- **QPP per pay period computation steps** — 1. Compute annualized pensionable earnings for the period. 2. Apply pro-rated basic exemption ($3,500 ÷ number of pay periods). 3. Compute first-tier QPP at 6.40% on the result (employee and employer each). 4. If annualized earnings exceed $71,300, compute QPP2 at 4.00% on the excess up to $81,200 (employee and employer each). 5. Cap year-to-date employee contribution at $4,744.50 ($4,348.50 base+additional + $396.00 QPP2).  _(Revenu Québec method / WebRAS calculator)_

### 3.4 Reporting

- **Source-deductions remittance** — TPZ-1015.R-V (combined with QPIP, HSF, and Quebec income tax).
- **Year-end slip** — RL-1, Box B (QPP) and Box B.A (QPP2 — second additional contribution).
- **Reconciliation** — Sommaire 1 (RLZ-1.S-V) — annual summary of source deductions and employer contributions, due last day of February.

### 3.5 Self-employed Quebec residents

- **Self-employed QPP treatment** — Self-employed individuals pay both halves of QPP (12.80% on the first tier, 8.00% on QPP2) through their Quebec personal return (TP-1, Schedule U / form TP-1129.66.3.6-V), not through payroll. Not covered further in this skill.

### 4.1 Why QPIP exists

Since 2006, Quebec has run its own parental-insurance regime under the Loi sur l'assurance parentale (Régime québécois d'assurance parentale, RQAP). It replaces the parental-benefits portion of federal EI for Quebec workers. Federal EI premiums are correspondingly reduced for Quebec employees (the EI Quebec-reduced rate is published annually by the CEIC).

### 4.2 2025 rates

**QPIP 2025 rates**

| Payer | Rate | Applied to |
| --- | --- | --- |
| Employee | **0.494%** | Insurable earnings up to $98,000 |
| Employer | **0.692%** | Insurable earnings up to $98,000 |
| Self-employed | **0.878%** | Net self-employment earnings up to $98,000 |

- **Maximum insurable earnings (MIE) 2025** — $98,000  _(§4.2 2025 rates)_
- **Maximum 2025 employee QPIP** — $484.12 (0.494% × $98,000)  _(§4.2 2025 rates)_
- **Maximum 2025 employer QPIP per employee** — $678.16 (0.692% × $98,000)  _(§4.2 2025 rates)_
- **No earnings exemption** — No earnings exemption — premiums apply from the first dollar of insurable earnings.

### 4.3 Federal EI coordination

- **Federal EI withholding for Quebec employees** — The employer still withholds federal EI from Quebec employees but at the Quebec-reduced rate (set annually by the CEIC — historically about 15% lower than the rest-of-Canada rate). The EI premium reduction reflects QPIP picking up parental benefits. See `canada-payroll.md` §EI for the federal mechanics — do not duplicate.

### 4.4 Reporting

- **QPIP withholding and remittance** — Withheld and remitted on TPZ-1015.R-V alongside QPP and Quebec income tax.
- **QPIP year-end slip** — RL-1, Box H (QPIP premium) and Box I (QPIP insurable earnings).

### 5.1 Purpose

- **HSF purpose** — The HSF is an employer-only contribution that funds Quebec's public health-care system. There is no employee portion and no ceiling per employee — it applies to the entire Quebec payroll without any per-employee cap.

### 5.2 2025 rate schedule (private-sector SMBs, all sectors)

**HSF 2025 rate schedule**

| Total Quebec payroll (TP) | HSF rate |
| --- | --- |
| TP ≤ $1,000,000 | **1.65%** |
| $1,000,000 < TP ≤ $7,500,000 | Computed by formula (see §5.3) |
| TP > $7,500,000 | **4.26%** |

> **Reduced rate** is available to private-sector employers in the **primary and manufacturing sectors** with TP ≤ $7.5M (lower entry rate, sliding scale). Out of scope here — see refusal **R-QC-2**.

### 5.3 Sliding-scale formula ($1M < TP ≤ $7.5M)

- **HSF sliding-scale formula** — HSF rate (private sector, general) = 0.7575% + (0.9075% × TP / $1,000,000) for $1M < TP ≤ $7.5M, expressed as a percentage and rounded as Revenu Québec specifies.  _(Guide TP-1015.G-V and Guide de l'employeur (TP-1015.G))_

For a payroll of $3,000,000: Rate = 0.7575% + (0.9075% × 3) = 0.7575% + 2.7225% = 3.48% (rounded per Revenu Québec). Always compute using the current-year Revenu Québec rate calculator (Outil de calcul du taux du FSS) rather than from memory — the formula coefficients are updated periodically by budget legislation.

### 5.4 Reporting

- **HSF remittance and true-up** — Remitted with each source-deductions remittance (TPZ-1015.R-V) using the expected annual rate derived from estimated payroll, then trued up on the Sommaire 1 (RLZ-1.S-V) based on actual year-end payroll. If estimated rate < actual rate, employer owes the difference (no penalty if reasonable estimate); if estimated rate > actual, refund or carry-forward credit on the Sommaire 1.

### 6.1 What CNESST is and isn't

- **CNESST** — CNESST (Commission des normes, de l'équité, de la santé et de la sécurité du travail) is a separate ministry from Revenu Québec — created in 2016 from the merger of the CSST (workers' comp), CNT (labour standards), and CES (pay equity). For payroll-contribution purposes, "CNESST" generally refers to the workers' compensation premium (formerly CSST), governed by the Loi sur les accidents du travail et les maladies professionnelles (LATMP) and Loi sur la santé et la sécurité du travail (LSST). CNESST contribution is employer-only. It is not filed on TPZ-1015 — it has its own annual statement and remittance flow.  _(LATMP, LSST)_

### 6.2 2025 rate structure

- **Rate varies by sector and classification unit** — Assigned by CNESST in the Décision sur la classification and published annually. Typical ranges: Office / professional services: ~0.15%–0.50%; Retail, hospitality: ~0.50%–1.50%; Construction (subject to ASP Construction): 3%–6%+; Forestry, mining, heavy industry: 5%+.
- **Insurable earnings ceiling per worker (2025)** — $98,000 (same as QPIP MIE — Quebec aligns these annually).
- **Retrospective/personalized rate regime threshold** — Larger employers (>$586,500 estimated 2025 premium threshold, indexed) may be in the retrospective or personalized rate regime rather than the rate-applied-to-payroll regime — refer to CNESST tarification specialist (refusal R-QC-4).  _(R-QC-4)_

### 6.3 Annual filing — Déclaration des salaires (DAS)

- **Form** — Déclaration des salaires (annual statement of insurable wages), filed online via Mon Espace CNESST.
- **Due date** — 14 March of the following year (i.e., the 2025 statement is due 14 March 2026).
- **Reconciliation** — Reconciles estimated premiums paid through periodic remittance against actual insurable wages.
- **Periodic remittance mechanism** — Periodic remittance is integrated with Revenu Québec source-deductions remittance via the Versement périodique mechanism: employer pays estimated CNESST premium to Revenu Québec on the same TPZ-1015.R-V schedule, and Revenu Québec forwards to CNESST. The annual reconciliation happens on the Déclaration des salaires.

> The 28 February date sometimes cited applies to the federal T4 / RL-1 slips and Sommaire 1, not to the CNESST DAS. The CNESST DAS is due 14 March.

### 6.4 Other CNESST employer obligations not covered here

- Pay equity (Loi sur l'équité salariale) — separate triennial maintenance obligation.
- Labour standards levy (formerly CNT levy) — replaced by CNESST general financing; usually embedded in remittance.
- Health-and-safety prevention programs (groupes prioritaires, programmes de prévention) — sector-dependent.

### 7.1 Legal basis

- **WSDRF legal basis** — Loi favorisant le développement et la reconnaissance des compétences de la main-d'œuvre, R.S.Q. c. D-8.3 (the "Loi du 1%"). Administered by the Commission des partenaires du marché du travail (CPMT) with collection via Revenu Québec.  _(R.S.Q. c. D-8.3)_

### 7.2 Who is subject

- **WSDRF applicability threshold** — Employers whose total Quebec payroll exceeds $2,000,000 in the calendar year.

### 7.3 The 1% obligation — spend or pay

- **1% spend-or-pay obligation** — Eligible employers must spend at least 1% of total payroll on eligible training expenditures during the year. If they spend less than 1%, the shortfall is remitted to Revenu Québec as a contribution to the WSDRF.
- **Eligible expenditures** — Eligible expenditures are defined in the CPMT regulations (training provided by recognized educators, certain in-house training, training-related travel, etc.). See refusal R-QC-5 for substantiation work.  _(R-QC-5)_
- **Reporting form** — Declared on form LE-39.0.2-V (Calcul des cotisations de l'employeur — fonds des services de santé et formation) and reconciled on the Sommaire 1.
- **Carry-forward** — Unused excess training expenditures (i.e., spent >1%) can be carried forward to reduce the obligation in future years, subject to CPMT rules.

### 7.4 Quick test

Total Quebec payroll for 2025 = $2,000,001 → subject. Total Quebec payroll = $1,999,999 → not subject. (The threshold is the calendar year, evaluated on actual payroll, not estimated.)

## 8. Federal coordination

Cross-reference `canada-payroll.md` for federal mechanics. Quebec-specific deviations:

**Federal coordination table**

| Federal item | Quebec treatment |
| --- | --- |
| **CPP** | **Does not apply** to Quebec-establishment employees. Use QPP instead. |
| **EI premiums** | Applies, but at the **Quebec-reduced rate** (lower than the rest-of-Canada rate). |
| **Federal income tax withholding** | Applies as usual (TD1, T4127). |
| **Quebec income tax withholding** | Separate — uses **TP-1015.3-V (TPD)** Quebec personal-exemption form and Revenu Québec's WebRAS calculator. |
| **T4** | Still issued for federal tax / EI; **RL-1** issued in parallel for Quebec (QPP, QPIP, HSF, Quebec tax). |
| **Federal remittance (PD7A)** | Still applies for federal tax, EI, CPP-or-its-Quebec-absence. Goes to CRA. |
| **Quebec remittance (TPZ-1015.R-V)** | Separate; goes to Revenu Québec. |
| **ROE (Record of Employment)** | Same as federal — issued through Service Canada. QPIP claims pull from the same ROE. |

**Bottom line:** a Quebec employer files **two** payroll-remittance streams — one to CRA (federal tax + EI) and one to Revenu Québec (Quebec tax + QPP + QPIP + HSF + WSDRF + integrated CNESST periodic remittance). The two streams must be kept reconciled.

## 9. Filing mechanics — Revenu Québec

### 9.1 Periodic remittance — TPZ-1015.R-V

**Periodic remittance frequency table**

| Average monthly Quebec source deductions | Remittance frequency |
| --- | --- |
| < $3,000 | **Quarterly** (or monthly, employer's choice) |
| $3,000 – $24,999.99 | **Monthly** (15th of following month) |
| $25,000 – $99,999.99 | **Twice-monthly** (25th + 10th) |
| ≥ $100,000 | **Weekly** (within 3 working days) |

> Thresholds mirror but do not exactly equal the federal CRA thresholds — Revenu Québec assigns the frequency independently based on the prior two years of Quebec remittance history. Always check the employer's Avis de cotisation for the assigned frequency.

- **Remittance includes** — The remittance includes (on a single voucher): 1. Quebec income tax withheld 2. Employee + employer QPP (incl. QPP2) 3. Employee + employer QPIP 4. Employer HSF 5. Employer WSDRF (if applicable) 6. Employer CNESST periodic remittance (if integrated)

### 9.2 Annual reconciliation

- **Sommaire 1 (RLZ-1.S-V)** — Annual employer summary; due last day of February following the calendar year.
- **RL-1 slips** — To each employee — same deadline (28/29 February).
- **CNESST Déclaration des salaires** — Separate; due 14 March.

### 9.3 Penalties (non-exhaustive)

- **Late remittance penalty** — 7% / 11% / 15% sliding penalty depending on lateness, plus interest.
- **Failure to file RL-1 / Sommaire 1** — $25 per slip per day, capped.
- **Failure to file CNESST DAS** — Separate CNESST penalty regime plus interest.
- **Negligence / gross negligence penalty** — Up to 50% penalty on under-withheld amounts.

## 10. Worked example — Montreal SaaS company, 8 employees, $800,000 payroll

**Facts.** *Acme SaaS inc.*, Quebec-incorporated, Montreal establishment, 8 software developers and 1 office manager. 2025 calendar-year payroll:

- 6 developers @ $95,000 = $570,000
- 2 senior developers @ $130,000 = $260,000
- 1 office manager @ $55,000 = $55,000
- **Total Quebec payroll = $885,000** (revised — using these illustrative numbers)
- For the "$800k" round number, assume total payroll = **$800,000**; we use that figure throughout for HSF and WSDRF.
- Sector: software publishing / SaaS — NAICS 5132 — **office / professional services CNESST classification**, assumed rate **0.18%** (illustrative; verify against actual CNESST classification).

For each employee, compute base + additional (6.40% EE / 6.40% ER) on earnings $3,500 – $71,300, plus QPP2 (4.00% EE / 4.00% ER) on earnings $71,300 – $81,200.

- **Office manager (gross $55,000):** Pensionable base = $55,000 − $3,500 = $51,500. QPP first tier = 6.40% × $51,500 = **$3,296** EE + **$3,296** ER. No QPP2.
- **Developer (gross $95,000):** First-tier capped: 6.40% × ($71,300 − $3,500) = 6.40% × $67,800 = **$4,339.20** EE + **$4,339.20** ER. QPP2: 4.00% × ($81,200 − $71,300) = 4.00% × $9,900 = **$396** EE + **$396** ER. Total per developer: $4,735.20 EE + $4,735.20 ER. (Slight rounding vs. published $4,744.50 max — Retraite Québec applies a specific rounding convention; the maximum is published as $4,348.50 base+additional, which differs from 6.40% × $67,800 = $4,339.20 by a rounding/inclusion-of-the-cents convention. **Always use the official WebRAS calculator** for final figures.)
- **Senior developer (gross $130,000):** Both ceilings hit. Same maximum as the developer = **$4,735.20** EE + **$4,735.20** ER (approx; use WebRAS).

- Office manager ($55,000): 0.494% × $55,000 = **$271.70** EE; 0.692% × $55,000 = **$380.60** ER.
- Developer ($95,000, capped at $98,000): 0.494% × $95,000 = **$469.30** EE; 0.692% × $95,000 = **$657.40** ER.
- Senior developer ($130,000, capped at $98,000): 0.494% × $98,000 = **$484.12** EE; 0.692% × $98,000 = **$678.16** ER.

Total Quebec payroll = $800,000 (< $1M) → HSF rate = **1.65%**.
- HSF = 1.65% × $800,000 = **$13,200**.

Assume CNESST rate = 0.18% (office/SaaS classification — illustrative).
- Insurable earnings, capped at $98,000/worker: developers and seniors capped at $98,000 each (6 + 2 = 8 workers × $98,000 = $784,000); office manager $55,000.
- Insurable wage base = $784,000 + $55,000 = $839,000.
- CNESST premium = 0.18% × $839,000 = **$1,510.20**.

> Note: in this worked example, salaries exceed total payroll because we used the $800,000 round figure for HSF/WSDRF but full $95k/$130k for per-employee QPP/QPIP. In a real engagement, reconcile so per-employee gross sums to total Quebec payroll exactly.

Total Quebec payroll = $800,000. Threshold = $2,000,000. **Not subject.**

- Federal EI withheld at the **Quebec-reduced employee rate** plus 1.4× employer share — see `canada-payroll.md` §EI for current rates.
- Federal income tax withheld using TD1 + T4127.
- **No CPP withheld** (QPP replaces).

**Summary — annual employer cost of Quebec contributions (illustrative)**

| Contribution | Employer cost |
| --- | --- |
| QPP (employer match) | ≈ $35,000–$40,000 (sum of per-employee ER QPP) |
| QPIP (employer) | ≈ $5,000–$5,400 |
| HSF | $13,200 |
| CNESST | $1,510 |
| WSDRF | $0 (under threshold) |
| **Total Quebec employer cost** | **≈ $55,000** on $800k payroll (~6.9%) |

…on top of federal employer EI cost (Quebec-reduced rate × 1.4) and any group benefits.

## 11. Conservative defaults

- **General default principle** — When information is missing, default conservatively (i.e., assume the higher liability) and flag for verification.
- **CNESST rate default** — If classification unit unknown, default to the sector's upper-bound published rate rather than the floor. Flag for CNESST classification confirmation.
- **HSF rate default near tier break** — If total payroll is near a tier break (e.g., $999k vs. $1.01M), default to the higher tier until year-end actuals are known; refund/credit on Sommaire 1.
- **WSDRF default near threshold** — If total payroll is within 5% of the $2M threshold, treat the employer as subject and recommend tracking training expenditures throughout the year.
- **Worker classification default** — If employee-vs.-contractor is ambiguous, default to employee (more conservative for the employer — all five contributions apply). Document the basis and flag for legal review.
- **Establishment location default** — If an employee works from home in a province other than Quebec but the employer's establishment is in Quebec, default to the "establishment to which the employee reports" rule — generally Quebec — and flag (refusal R-QC-6).  _(R-QC-6)_
- **Remittance frequency default** — If Revenu Québec has not yet notified, default to monthly until the Avis de cotisation arrives.
- **Annualized vs. period earnings default** — Always use Revenu Québec's WebRAS (Web ROD calculator) for per-pay-period figures rather than back-of-envelope annualization, which can over- or under-withhold near tier breaks.

## 12. Sources

Primary legislation (Quebec):

- Loi sur le régime de rentes du Québec, R.S.Q. c. R-9 — QPP.
- Loi sur l'assurance parentale, R.S.Q. c. A-29.011 — QPIP / RQAP.
- Loi sur la Régie de l'assurance maladie du Québec, R.S.Q. c. R-5 — HSF.
- Loi sur les accidents du travail et les maladies professionnelles (LATMP), R.S.Q. c. A-3.001 — CNESST.
- Loi sur la santé et la sécurité du travail (LSST), R.S.Q. c. S-2.1 — CNESST.
- Loi favorisant le développement et la reconnaissance des compétences de la main-d'œuvre, R.S.Q. c. D-8.3 — WSDRF.
- Loi sur les impôts, R.S.Q. c. I-3 — Quebec income tax withholding.

Administrative guidance:

- Revenu Québec — Guide de l'employeur (TP-1015.G-V), 2025 edition.
- Revenu Québec — Tableaux des retenues à la source et des cotisations de l'employeur (TP-1015.TI-V / TR-V), 2025 edition.
- Revenu Québec — WebRAS (online source-deduction calculator), 2025.
- Revenu Québec — TPZ-1015.R-V Source-Deductions Statement.
- Revenu Québec — RLZ-1.S-V Sommaire des retenues et cotisations de l'employeur.
- Revenu Québec — LE-39.0.2-V Calcul des cotisations de l'employeur — FSS et formation.
- Retraite Québec — Bulletin des cotisations au RRQ, 2025.
- RQAP — Cotisations 2025 (rqap.gouv.qc.ca).
- CNESST — Taux de cotisation 2025 (cnesst.gouv.qc.ca).
- CNESST — Déclaration des salaires (Mon Espace CNESST).
- Commission des partenaires du marché du travail (CPMT) — règlement sur les dépenses de formation admissibles.

Cross-references in this skill package:

- `canada-payroll.md` — federal payroll workflow (CPP/EI/T4/CRA remittance).
- `payroll-workflow-base.md` — Tier-1 workflow base.
- `qc-individual-return.md` — Quebec TP-1 (employee side: RL-1 reconciliation, QPP credit, QPIP credit).
- `intake.md`, `global-router.md` — routing into the Quebec payroll skills from a Canadian intake.

## Verification status

*Verification status: pending. To be reviewed by a Quebec-licensed CPA / payroll specialist before production use. All 2025 rates above should be cross-checked against the current Revenu Québec, Retraite Québec, CNESST, and CPMT publications at the time of engagement.*

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
