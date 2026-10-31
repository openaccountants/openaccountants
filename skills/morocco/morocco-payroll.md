---
name: morocco-payroll
description: Morocco — Payroll for a Self-Employed Person Who Hires Employees (IR salarial / CNSS / AMO / TFP)
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco Payroll

## Morocco — Payroll for a Self-Employed Person Who Hires Employees (IR salarial / CNSS / AMO / TFP)

A self-employed person in Morocco — whether an **auto-entrepreneur**, a registered **travailleur non-salarié (TNS)**, or the manager of a small structure — who **hires even one employee** becomes an **employer (employeur)** with three monthly payroll obligations:

1. **IR salarial** — the **impôt sur le revenu** on salaries, withheld at source (**retenue à la source**) and paid to the **Direction Générale des Impôts (DGI)**.
2. **CNSS contributions** — social-security contributions to the **Caisse Nationale de Sécurité Sociale**, split between **employer (part patronale)** and **employee (part salariale)**, including **AMO** (Assurance Maladie Obligatoire) and the **taxe de formation professionnelle (TFP)**.
3. **The bulletin de paie** — a compliant payslip for each employee each month.

This is **fundamentally different** from the contributor's *own* self-employed cover (TNS / auto-entrepreneur AMO and retraite — see `ma-social-contributions`). As an employer you compute **percentages on each employee's real salary** with a **ceiling**, not a forfaitaire SMIG-indexed base.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (IR salarial, CNSS, AMO, TFP, SMIG, bulletin de paie, Damancom, SIMPL) and explain them in the user's chosen language.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Topic | Payroll for an employer (IR salarial withholding + CNSS/AMO/TFP) |
| Authority | **DGI** (Direction Générale des Impôts, tax.gov.ma) **+ CNSS** (cnss.ma) |
| Currency | **MAD** (dirham marocain, DH) |
| Tax year | 2026 (Loi de Finances 2026) |
| IR scale | Progressive **0% → 37%**; 0% on first **MAD 40,000/year** (≈ MAD 3,333.33/month) |
| Frais professionnels | **35%** if gross ≤ MAD 6,500/month (cap MAD 2,500/mo) — **25%** if > MAD 6,500/month (cap MAD 2,916.67/mo) *(verify monthly thresholds vs annual MAD 78,000)* |
| Family deduction | **MAD 50/month per dependent**, max **MAD 300/month** (6 dependents) |
| CNSS ceiling | **MAD 6,000/month** gross for short-term + long-term branches |
| CNSS + AMO + TFP — employer | **≈ 21.09%** total *(verify)* |
| CNSS + AMO — employee | **≈ 6.74%** total *(verify)* |
| TFP | **1.60% employer**, uncapped (taxe de formation professionnelle, collected by CNSS) |
| Declaration — CNSS | **Damancom** (DNS / BDS), filed + paid by the **10th** of the following month |
| Declaration — IR | **SIMPL-IR** (DGI portal), withheld IR paid by DGI deadline (typically by the end of the following month) *(verify exact date)* |
| Quality tier | **Research-verified — pending sign-off by a Moroccan expert-comptable** |
| Version | 1.0 |

**Conservative defaults** (apply when the user has not specified otherwise):
- Treat the worker as an **employee (salarié)** — and therefore subject to payroll — whenever there is **subordination** (fixed hours, direction, integration into the business). When in doubt, default to **employee** treatment, which is the safer classification and avoids requalification penalties. See §6.
- Apply the **25% frais professionnels rate** only when the employee's gross clearly exceeds the threshold; otherwise apply **35%**. Never exceed the monthly caps.
- Apply CNSS short/long-term branches on **min(gross, MAD 6,000)**; apply **AMO and TFP on full uncapped gross**.
- If a benefit-in-kind, bonus, or allowance may be **CNSS-assiette** or **IR-imposable**, treat it as **included** unless a clear exemption is identified, then flag it to **verify**.
- Round each employee's monthly IR to the dirham as the DGI does, and reconcile to the annual scale at year-end.
- All figures below are **2026** values to be **verified** against the current CNSS circular and the Loi de Finances 2026 before filing.

## 2. IR Salarial — Computation

IR salarial is computed **monthly** on the employee's **revenu net imposable (RNI)** — the gross salary minus the deductible items — then the progressive scale is applied and the **déductions pour charges de famille** are subtracted.

### Step-by-step (monthly)

- **IR salarial computation steps** — 1. **Salaire brut global (SBG)** = base salary + taxable allowances + benefits in kind + taxable bonuses. 2. **Salaire brut imposable (SBI)** = SBG − legally exempt elements (e.g. certain reimbursements of professional expenses, exempt indemnités) *(verify each item)*. 3. Deduct, in order, from SBI: - **Frais professionnels (FP)** — a standard professional-expense allowance: **35%** of SBI if monthly gross ≤ **MAD 6,500** (cap **MAD 2,500/month**), or **25%** if monthly gross > **MAD 6,500** (cap **MAD 2,916.67/month**). *(Verify: some sources express the rate change against an annual MAD 78,000 gross threshold — confirm the exact monthly cut-off in force for 2026.)* - **CNSS + AMO employee contributions** (the part salariale — see §3) — deductible. - **Employee retirement / insurance** (CIMR, mutuelle, life insurance) within legal limits, if any *(verify caps)*. 4. The result is the **revenu net imposable (RNI)**. 5. Apply the **monthly IR scale** (below) and subtract the **somme à déduire**. 6. Subtract **déductions pour charges de famille**: **MAD 50/month per dependent** (non-working spouse + children under 27, or any age if disabled), capped at **MAD 300/month** (6 dependents). 7. The result is the **IR net to withhold** (retenue à la source).

### IR scale — monthly (RNI, 2026)

**IR scale — monthly (RNI, 2026)**

| RNI / month (MAD) | Rate | Somme à déduire (MAD/month) |
| --- | --- | --- |
| 0 – 3,333.33 | 0% | 0 |
| 3,333.34 – 5,000 | 10% | 333.33 |
| 5,000.01 – 6,666.67 | 20% | 833.33 |
| 6,666.68 – 8,333.33 | 30% | 1,500.00 |
| 8,333.34 – 15,000 | 34% | 1,833.33 |
| Over 15,000 | 37% | 2,283.33 |

### IR scale — annual (RNI, 2026) — for reconciliation

**IR scale — annual (RNI, 2026) — for reconciliation**

| RNI / year (MAD) | Rate | Somme à déduire (MAD/year) |
| --- | --- | --- |
| 0 – 40,000 | 0% | 0 |
| 40,001 – 60,000 | 10% | 4,000 |
| 60,001 – 80,000 | 20% | 10,000 |
| 80,001 – 100,000 | 30% | 18,000 |
| 100,001 – 180,000 | 34% | 22,000 |
| Over 180,000 | 37% | 27,400 |

- **IR net formula** — IR brut = (RNI × rate) − somme à déduire; IR net = IR brut − charges de famille

The 2026 scale is **unchanged from the 2025 reform** (which raised the exempt threshold from MAD 30,000 to MAD 40,000 and cut the top marginal rate to 37%). *(Verify no further amendment in the Loi de Finances 2026.)*

## 3. CNSS / AMO / TFP — Rates & Ceiling

CNSS contributions are split between **employer (part patronale)** and **employee (part salariale)**. Some branches are **capped** at a gross of **MAD 6,000/month**; others apply to the **full uncapped salary**.

**CNSS/AMO/TFP rate table**

| Branch (FR / native) | Employer | Employee | Base / ceiling |
| --- | --- | --- | --- |
| **Allocations familiales** (family allowances) | 6.40% | — | Full salary, **no cap** |
| **Prestations sociales court terme** (short-term: sickness, maternity) | 1.05% | 0.52% | Capped at **MAD 6,000/mo** |
| **Prestations sociales long terme** (long-term: retirement, invalidity, survivors) | 7.93% | 3.96% | Capped at **MAD 6,000/mo** |
| **AMO** (Assurance Maladie Obligatoire — health) | 4.11% | 2.26% | Full salary, **no cap** |
| **TFP** — taxe de formation professionnelle | 1.60% | — | Full salary, **no cap** |
| **Total** | **≈ 21.09%** | **≈ 6.74%** | — |

*(Verify all rates against the current CNSS circular. The AMO employer 4.11% is commonly reported as 2.26% AMO de base + 1.85% AMO Solidarité/Tadamoun — confirm the split and whether the contributor's payroll software itemises them separately.)*

### Key mechanics

- **CNSS ceiling mechanics** — - **The ceiling only bites on the two "prestations sociales" branches.** For an employee earning **above MAD 6,000/month**, the short- and long-term contributions are frozen at the MAD 6,000 base, so the **effective CNSS rate falls** as salary rises — but **AMO and TFP keep growing** because they are uncapped. - **Maximum capped employee CNSS** (short + long term) = (0.52% + 3.96%) × 6,000 = **4.48% × 6,000 = MAD 268.80/month**. *(Verify.)* - **AMO has no ceiling** — it is **2.26% employee / 4.11% employer** on the full gross. - **The employee never pays family allowances or TFP** — those are **employer-only**. - **TFP is collected by the CNSS** alongside the social contributions (it funds the OFPPT vocational-training system) even though it is technically a tax, not a benefit. - **The employer remits both halves** — the employer withholds the employee part from net pay and adds its own part, paying the total to CNSS via Damancom.

## 4. Declarations & Calendar

A Moroccan employer runs **two parallel monthly filings** — one to CNSS, one to DGI.

### CNSS — via Damancom

- **CNSS filing rules** — - **Damancom** is the CNSS télédéclaration portal (since 2025, access is via the **Mon e-ID** national digital identity). Filing is **mandatory online**. - The employer files the **DNS — Déclaration Nominative des Salaires** (nominative salary declaration: each employee, days worked, salary) each month. - CNSS issues the **BDS — Bordereau de Déclaration des Salaires** (the computed contributions slip) around the **22nd** of the month. - **Two modes:** **EFI** (manual online entry, suited to very small employers) and **EDI** (file upload from payroll software). - **Deadline:** declaration **and** payment by the **10th of the following month** (e.g. March 2026 contributions are due by **10 April 2026**). - **Late surcharge** (since April 2025): **3% for the first month**, then **0.5% per additional month** *(verify current penalty regime)*.

### IR salarial — via SIMPL-IR (DGI)

- **SIMPL-IR filing rules** — - The withheld IR is declared and paid on the DGI's **SIMPL** portal (Service des Impôts en Ligne) under **SIMPL-IR**. - **Monthly payment** of the retenue à la source is the default; **quarterly** payment may apply to certain small employers *(verify eligibility and the exact monthly payment deadline — commonly by the end of the following month)*. - **Annual return:** the employer files the **déclaration des traitements et salaires** (annual recap of all salaries paid and IR withheld, historically model 9421 / now filed via SIMPL) by **end of February / 1 March** of the following year *(verify the current form and date in force for the 2026 reporting cycle)*.

### Registration

- **Registration requirements** — Before the first payroll, the employer must be **affiliated with CNSS** (numéro d'affiliation) and have each employee **immatriculé** (numéro d'immatriculation CNSS), and be registered with the **DGI** for IR salarial. *(Verify the affiliation procedure for an auto-entrepreneur / TNS who becomes an employer.)*

## 5. Worked Examples (Payslips)

All figures are **illustrative 2026** computations to **verify** before filing. Single employee, no CIMR/mutuelle, dependents as stated.

### Example A — SMIG-level employee, 2 dependents

- **Salaire brut imposable (SBI):** MAD 4,000/month. Dependents: 2.
- **CNSS employee** (capped base = min(4,000, 6,000) = 4,000): short+long term = 4.48% × 4,000 = **MAD 179.20**.
- **AMO employee** (uncapped): 2.26% × 4,000 = **MAD 90.40**.
- **Total employee social** = 179.20 + 90.40 = **MAD 269.60** (deductible for IR).
- **Frais professionnels** (gross ≤ 6,500 → 35%, cap 2,500): 35% × 4,000 = **MAD 1,400** (under cap).
- **RNI** = 4,000 − 1,400 − 269.60 = **MAD 2,330.40**.
- RNI ≤ 3,333.33 → **0% bracket → IR brut = 0**.
- **IR net = MAD 0** (the family deduction does not create a refund).
- **Employer CNSS+AMO+TFP** ≈ : capped branches (1.05% + 7.93%) × 4,000 = 8.98% × 4,000 = 359.20; family allowances 6.40% × 4,000 = 256.00; AMO 4.11% × 4,000 = 164.40; TFP 1.60% × 4,000 = 64.00 → **employer total ≈ MAD 843.60**.
- **Net pay to employee** = 4,000 − 269.60 − 0 = **MAD 3,730.40**.

### Example B — Mid-level employee, 3 dependents

- **SBI:** MAD 8,000/month. Dependents: 3.
- **CNSS employee** — capped branches on **6,000**: 4.48% × 6,000 = **MAD 268.80**.
- **AMO employee** (uncapped, on 8,000): 2.26% × 8,000 = **MAD 180.80**.
- **Total employee social** = 268.80 + 180.80 = **MAD 449.60**.
- **Frais professionnels** (gross > 6,500 → 25%, cap 2,916.67): 25% × 8,000 = 2,000 (under cap) = **MAD 2,000**.
- **RNI** = 8,000 − 2,000 − 449.60 = **MAD 5,550.40**.
- RNI in 5,000.01–6,666.67 → **20%, somme à déduire 833.33**: IR brut = (5,550.40 × 20%) − 833.33 = 1,110.08 − 833.33 = **MAD 276.75**.
- **Charges de famille:** 3 × 50 = **MAD 150**.
- **IR net** = 276.75 − 150 = **MAD 126.75** (≈ **MAD 127** rounded).
- **Net pay** = 8,000 − 449.60 − 127 = **MAD 7,423.40**.

### Example C — Higher earner, 1 dependent (ceiling effect)

- **SBI:** MAD 18,000/month. Dependents: 1.
- **CNSS employee** — capped branches on **6,000**: **MAD 268.80**.
- **AMO employee** (uncapped, on 18,000): 2.26% × 18,000 = **MAD 406.80**.
- **Total employee social** = 268.80 + 406.80 = **MAD 675.60**.
- **Frais professionnels** (25%, cap 2,916.67): 25% × 18,000 = 4,500 → **capped at MAD 2,916.67**.
- **RNI** = 18,000 − 2,916.67 − 675.60 = **MAD 14,407.73**.
- RNI in 8,333.34–15,000 → **34%, somme à déduire 1,833.33**: IR brut = (14,407.73 × 34%) − 1,833.33 = 4,898.63 − 1,833.33 = **MAD 3,065.30**.
- **Charges de famille:** 1 × 50 = **MAD 50**.
- **IR net** = 3,065.30 − 50 = **MAD 3,015.30** (≈ **MAD 3,015**).
- **Net pay** = 18,000 − 675.60 − 3,015 = **MAD 14,309.40**.
- Note the ceiling effect: the capped CNSS stays at MAD 268.80 while AMO and the IR keep climbing — the marginal cost of a raise here is mostly **IR + uncapped AMO**.

## 6. Tier 2 — Employee vs Independent, Bulletin de Paie, Edge Cases

### Employee (salarié) vs independent (TNS / prestataire)

- **Classification rule** — Payroll obligations apply **only to employees**. The distinction turns on **subordination juridique** (legal subordination), not on the label of the contract.

**Employee vs independent indicators table**

| Indicator | Points to **employee** | Points to **independent** |
| --- | --- | --- |
| Direction & control | Employer sets hours, methods, place | Worker organises own work |
| Integration | Part of the business's organisation | Provides a service from outside |
| Exclusivity / continuity | Ongoing, exclusive | Project-based, multiple clients |
| Tools & risk | Employer provides tools, bears risk | Worker bears own commercial risk |
| Remuneration | Fixed monthly salary | Invoices, facture, often with VAT |

- **Faux indépendant risk** — A genuine **independent** (auto-entrepreneur, TNS, or company) invoices the contributor and handles **their own** CNSS-TNS / AMO and IR — see `ma-social-contributions` and `morocco-professional-income-tax`. **Disguising an employee as an independent** ("faux indépendant") risks **requalification**, back-contributions, IR, and penalties. **Default to employee treatment when subordination is present.**

### Bulletin de paie — required contents

- **Bulletin de paie required contents** — Each employee must receive a monthly **bulletin de paie** (payslip). It must show, at minimum *(verify against the Code du travail and current practice)*: - Employer identity, **CNSS affiliation number**, ICE; employee identity and **CNSS immatriculation number**. - Pay period, days/hours worked, position. - **Salaire de base**, allowances, overtime (heures supplémentaires), benefits in kind. - **Salaire brut global** and **salaire brut imposable**. - Each **CNSS / AMO employee deduction** line and the **IR retenu**. - **Net à payer** (net pay) and payment method/date. - The **employer's contributions** are often shown for transparency though they are not deducted from the employee. Payslips and payroll registers must be **retained** (the **livre de paie** / payroll records) for the statutory period *(verify retention duration)*.

### Edge cases & flags

- **Edge cases and flags** — - **Benefits in kind (avantages en nature)** — housing, car, etc. — are generally both **CNSS-assiette and IR-imposable** at their assessed value *(verify valuation rules)*. - **Indemnités** — some indemnities (de déplacement, de panier, de représentation) are **exempt within limits**; excess is taxable. *(Verify each ceiling.)* - **Overtime (heures supplémentaires)** — taxable and CNSS-able; computed on the legal premium rates. - **13th month / primes** — taxable; spread or taxed in the month paid per DGI rules *(verify)*. - **CIMR / mutuelle** — optional complementary pension/health; employee contributions may be IR-deductible within limits *(verify)*. - **Apprentices / stagiaires** — special regimes may reduce or exempt contributions *(verify eligibility)*. - **First hire by a TNS/auto-entrepreneur** — confirm whether the contributor's own régime restricts hiring (an auto-entrepreneur's eligibility can be affected by employing staff) — **flag and verify** before onboarding.

## 7. Reference + Test Suite

### Reference checklist (each month)

- **Monthly reference checklist** — 1. Build each employee's **salaire brut imposable**. 2. Compute **employee CNSS** on min(gross, 6,000) + **AMO** on full gross. 3. Deduct **frais professionnels** (35%/25%, respect caps) and **employee social** to get **RNI**. 4. Apply the **monthly IR scale**, subtract **charges de famille** → **IR net**. 5. Compute **employer CNSS + AMO + TFP** (≈ 21.09%). 6. Produce the **bulletin de paie**; confirm **net à payer**. 7. File the **DNS on Damancom** and pay CNSS by the **10th**. 8. Pay the **IR retenu via SIMPL-IR** by the DGI deadline. 9. Year-end: file the **déclaration annuelle des traitements et salaires** and reconcile to the **annual IR scale**.

### Test suite (self-checks before delivering a result)

- [ ] Did I apply the **MAD 6,000 ceiling** to short/long-term CNSS only, and **AMO + TFP on full gross**? (Capped CNSS employee max = MAD 268.80.)
- [ ] Did I use the correct **frais professionnels** rate (35% vs 25%) and **cap**?
- [ ] Did I deduct **employee CNSS/AMO** before applying the IR scale?
- [ ] Did I apply the right **monthly bracket** and **somme à déduire**, then subtract **charges de famille** (MAD 50 × dependents, max 300)?
- [ ] Did I keep **family allowances (6.40%) and TFP (1.60%) employer-only**?
- [ ] Did I confirm the worker is an **employee** (subordination) and not a disguised independent?
- [ ] Did I flag every **benefit-in-kind / indemnity / bonus** for IR + CNSS treatment?
- [ ] Did I mark all rates and dates **"verify"** against the current CNSS circular, SIMPL/DGI guidance, and the Loi de Finances 2026?

### Sources (to re-verify before filing)

- **DGI** — tax.gov.ma (Code Général des Impôts; IR salarial; SIMPL-IR).
- **CNSS** — cnss.ma (contribution rates, ceiling, Damancom, DNS/BDS, penalties).
- **Loi de Finances 2026** (Morocco) — confirms IR scale continuity.
- **PwC Worldwide Tax Summaries — Morocco** (individual taxes; social security).
- Moroccan payroll practitioners (cross-checked: Upsilon Consulting, ClicPaie, Humantal, Sahl Compta) — used for corroboration only; primary sources govern.

## PROHIBITIONS

- **Prohibited actions** — - **Do NOT** file or pay on the user's behalf, or submit anything to Damancom, SIMPL, CNSS, or the DGI. Produce computations and draft payslips only. - **Do NOT** present any rate, ceiling, bracket, or deadline as final without the **"verify"** caveat — these are research-verified, not officially signed off. - **Do NOT** advise classifying a genuine employee as an independent ("faux indépendant") to avoid CNSS/IR. When subordination exists, the worker is an employee. - **Do NOT** omit the **AMO uncapped** treatment or apply the MAD 6,000 ceiling to AMO or TFP. - **Do NOT** handle **company corporate payroll for IS-liable entities, multi-CNES / expatriate regimes, conventions of non-double taxation, severance/indemnité de licenciement taxation, CIMR optimisation, or labour-law disputes** — these are out of scope; refer to a Moroccan **expert-comptable** and, for labour law, a specialist. - **Do NOT** advise on the contributor's **own** TNS/auto-entrepreneur social cover here — route to `ma-social-contributions`. - **Do NOT** proceed if the contributor's own régime may prohibit or restrict hiring — flag and stop until verified.

## Disclaimer

This skill is **research-verified** against public CNSS, DGI, Loi de Finances 2026, and reputable Moroccan payroll-practitioner sources as of **May 2026**, but it has **not yet been signed off by a Moroccan expert-comptable**. Rates, ceilings, brackets, forms, and deadlines change and must be **independently verified** against the current CNSS circular and DGI guidance before any payroll is run, declared, or paid. It is general information, **not** tax, accounting, or legal advice, and creates no engagement. A qualified Moroccan **expert-comptable** (and, for employment matters, a labour-law adviser) must review every payroll before filing. Provided by **openaccountants.com** under its open-source tax-skills project.

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
