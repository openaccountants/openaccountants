---
name: morocco-income-tax
description: Morocco — Personal Income Tax on Professional Income (Impôt sur le Revenu / IR)
jurisdiction: MA
domain: income-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# morocco-income-tax

## Morocco — Personal Income Tax on Professional Income (Impôt sur le Revenu / IR)

Morocco's **Impôt sur le Revenu (IR)** is the personal income tax levied on individuals. This skill covers **professional / business income** (revenus professionnels) taxed on **net profit** under the two general accounting systems:

- **Régime du Résultat Net Réel (RNR)** — the real net-income system (full accounting), the default for individuals carrying on a business.
- **Régime du Résultat Net Simplifié (RNS)** — the simplified net-income system available below the turnover ceilings, with lighter books but no provisions and no carry-forward of losses.

Both compute IR on **net taxable profit** (résultat net fiscal) run through the progressive IR scale, subject to a **cotisation minimale (CM)** floor on turnover. For the simplified **turnover-based** alternatives — the **auto-entrepreneur** liberatory tax and the **Contribution Professionnelle Unique (CPU)** — see `ma-auto-entrepreneur` and `ma-cpu`.

This skill is governed by the **Code Général des Impôts (CGI)** and administered by the **Direction Générale des Impôts (DGI)**. It replies in the user's language — Moroccan users mix English, French, and Darija — and keeps native terms (IR, résultat net, cotisation minimale, DGI, RNR, RNS, acomptes) explained in context.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Tax | Impôt sur le Revenu (IR) — professional income on net profit |
| Systems covered | Résultat Net Réel (RNR) and Résultat Net Simplifié (RNS) |
| Currency | MAD (dirham marocain, DH) |
| Exempt threshold | Net taxable income up to **MAD 40,000 / year** *(2025 reform)* |
| Top marginal rate | **37%** above MAD 180,000 *(2025 reform; was 38%)* |
| Cotisation minimale — standard rate | **0.25% of turnover (HT)** + other operating/financial income *(verify)* |
| Cotisation minimale — reduced (regulated-margin goods) | **0.15%** *(verify)* |
| Cotisation minimale — liberal professions | **4%** *(reduced from 6%; verify)* |
| Cotisation minimale — minimum floor (IR) | **MAD 1,500 / year** *(verify)* |
| CM exemption for new businesses | First **3 financial years** of activity *(verify)* |
| Annual return | **Déclaration du revenu global** via **SIMPL-IR**, by **1 May** of year N+1 *(verify date each year)* |
| Advance payments | **Acomptes** / cotisation minimale paid in-year; final IR settled on filing *(verify mechanics)* |
| Authority | **Direction Générale des Impôts (DGI)** — tax.gov.ma |
| Portal | **SIMPL-IR** — télédéclaration & télépaiement (irpart.tax.gov.ma) |
| Primary legislation | Code Général des Impôts (CGI); Loi de Finances 2025 & 2026 |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan expert-comptable** |
| Version | 1.0 |
| Last research update | May 2026 |

### Progressive IR scale (barème annuel) — 2025 reform, in force 2026

**Progressive IR scale (barème annuel) — 2025 reform, in force 2026**

| Annual net taxable income (MAD) | Rate | Somme à déduire (MAD) *(verify)* |
| --- | --- | --- |
| 0 – 40,000 | **0% (exonéré)** | 0 |
| 40,001 – 60,000 | **10%** | 4,000 |
| 60,001 – 80,000 | **20%** | 10,000 |
| 80,001 – 100,000 | **30%** | 18,000 |
| 100,001 – 180,000 | **34%** | 22,000 |
| Above 180,000 | **37%** | 27,400 |

- **Fast formula (quick method)** — IR brut = (net taxable income × rate of its bracket) − somme à déduire IR net  = IR brut − family deductions (charges de famille) − tax credits
- **Family deduction (déduction pour charges de famille)** — MAD 500 per dependent / year, maximum MAD 3,000 (up to 6 dependents) *(verify — the Loi de Finances 2026 was reported to revalue this; confirm the current per-head amount and cap)*. Dependents = spouse and children (children under 27 / without age limit if disabled).  _(verify)_

The progressive scale applies to the taxpayer's **revenu global** (all IR categories combined). Professional net profit is one component, added to any salary, rental, or other income before the scale is applied.

### Conservative defaults

- **System unknown** — Assume RNR (full accounting, fewer reliefs lost) unless the user confirms RNS eligibility and election.
- **Deductibility of an expense uncertain** — Treat it as non-deductible until substantiated (invoice + business purpose); add it back to net profit.
- **Turnover near an RNS ceiling** — Assume the ceiling is breached and warn of the move to RNR.
- **Cotisation minimale vs scale IR** — Compute both; the IR due is the higher of (scale IR) and (cotisation minimale), subject to the MAD 1,500 floor and the new-business exemption.
- **2026 figures** — All rates, the somme-à-déduire column, the family deduction, and deadlines carry "verify"; check the Loi de Finances 2026 and the DGI before finalising any number.

### Required inputs

1. **Activity & system** — nature of the business; whether RNR or RNS (and whether an RNS election was filed and is still valid).
2. **Annual turnover (HT)** — chiffre d'affaires hors taxe, plus other operating income, financial income, and subsidies (the cotisation-minimale base).
3. **Net accounting result** — revenue minus expenses per the books, with the detail needed to test deductibility and apply fiscal reintegrations/déductions.
4. **Other IR income** — salary, rental, capital income (to build the revenu global; the scale applies to the total).
5. **Family situation** — number of dependents for charges de famille.
6. **Start date of activity** — to test the 3-year CM exemption.
7. **Acomptes / CM already paid** in the year, and any withholdings at source.

### Refusal catalogue

- **R-MA-1** — Corporate income tax (IS). Companies (SARL, SA, etc.) are taxed under IS, not IR. Refuse and route to a Morocco corporate-tax skill.  _(R-MA-1)_
- **R-MA-2** — Auto-entrepreneur / CPU. Turnover-based liberatory regimes are out of scope; route to `ma-auto-entrepreneur` / `ma-cpu`.  _(R-MA-2)_
- **R-MA-3** — VAT (TVA). TVA computation and returns are out of scope; route to `morocco-vat`.  _(R-MA-3)_
- **R-MA-4** — Salary-only taxpayers. Pure payroll IR (retenue à la source on salaire) without professional income is a different workflow; flag and limit to the professional component.  _(R-MA-4)_
- **R-MA-5** — Agricultural income special regimes, real-estate capital gains (TPI), and financial-product withholdings beyond the revenu-global mention → reviewer only.  _(R-MA-5)_
- **R-MA-6** — Non-residents / treaty relief. Residence determination and double-tax treaty application require the expert-comptable.  _(R-MA-6)_
- **R-MA-7** — Filing as agent. Never submit a SIMPL-IR return as filed; produce a draft for expert-comptable sign-off.  _(R-MA-7)_

## 3. Transaction Pattern Library

Classify bank-statement lines and ledger entries. Keywords appear in **French**, **Moroccan Arabic / Darija (transliterated + script)**, and **English**.

### Income (revenu professionnel — taxable)

**Income (revenu professionnel — taxable)**

| Pattern (FR / AR / EN) | Treatment |
| --- | --- |
| `VIREMENT RECU`, `VRMT`, `ENCAISSEMENT`, `REGLEMENT CLIENT`, `FACTURE` | Business receipt → turnover |
| `CHEQUE REMIS`, `REMISE CHEQUE`, `versement espèces` | Receipt → turnover (confirm source) |
| `تحويل وارد` (tahwil warid), `أداء زبون` (client payment), `فاتورة` (fatura) | Client payment → turnover |
| `produits financiers`, `intérêts créditeurs`, `فوائد` | Financial income → in CM base |
| `subvention`, `don reçu`, `إعانة` | Subsidy/grant → in CM base (and often taxable) |

### Deductible expenses (charges déductibles)

**Deductible expenses (charges déductibles)**

| Pattern (FR / AR / EN) | Treatment |
| --- | --- |
| `LOYER`, `bail`, `كراء` (kira) | Rent of business premises → deductible |
| `SALAIRES`, `paie`, `أجور` | Staff wages → deductible (with CNSS) |
| `CNSS`, `AMO`, `cotisations sociales` | Social charges → deductible |
| `ACHAT`, `fournisseur`, `marchandises`, `مشتريات` | Purchases / stock → deductible (COGS) |
| `ELECTRICITE`, `EAU`, `LYDEC`, `REDAL`, `ONEE`, `كهرباء` | Utilities (business share) → deductible |
| `TELEPHONE`, `INTERNET`, `IAM`, `INWI`, `ORANGE` | Telecom (business share) → deductible |
| `ASSURANCE`, `تأمين` | Business insurance → deductible |
| `HONORAIRES`, `comptable`, `avocat`, `أتعاب` | Professional fees → deductible |
| `CARBURANT`, `GASOIL`, `AFRIQUIA`, `SHELL`, `وقود` | Fuel (business use) → deductible (substantiate) |
| `AMORTISSEMENT`, `dotation` | Depreciation of fixed assets → deductible per CGI rates |
| `INTERETS EMPRUNT`, `crédit`, `قرض` | Loan interest (business) → deductible |

### Non-deductible (charges non déductibles — reintegrate)

**Non-deductible (charges non déductibles — reintegrate)**

| Pattern (FR / AR / EN) | Treatment |
| --- | --- |
| `AMENDE`, `PENALITE`, `majoration`, `غرامة` | Fines & penalties → **non-deductible** |
| `IR`, `acompte IR`, `cotisation minimale` | The IR itself / CM → **non-deductible** |
| `cadeaux` over the unit cap, `dons` non-qualifying | Excess gifts / non-qualifying donations → non-deductible |
| Cash expense > regulatory threshold (paiement espèces) | Portion over the cash-payment limit → **non-deductible** *(verify current threshold per CGI)* |
| `frais sans justificatif`, no invoice | Unsupported expense → non-deductible (§6001-style substantiation) |

### Likely personal (exclusions — not business)

**Likely personal (exclusions — not business)**

| Pattern (FR / AR / EN) | Treatment |
| --- | --- |
| `RETRAIT GAB`, `retrait DAB`, `سحب` (cash withdrawal) | Personal unless proven business |
| `MARJANE`, `CARREFOUR`, `ACIMA`, groceries, `سوق` | Personal household → exclude |
| `transfert famille`, `virement personnel`, `تحويل عائلي` | Personal transfer → exclude |
| `restaurant`, `café`, clothing, `ملابس` | Personal unless a substantiated business meal/representation |
| `scolarité`, `école`, school fees | Personal → exclude |

- **Likely-personal default** — Apply a likely-personal default: mixed-use and undocumented private-looking spend is excluded from business expenses until the user substantiates a business purpose.

## 4. Worked Examples

All figures use the 2025-reform scale and 2026 "verify" rates. Recompute with confirmed values. IR uses the quick formula: `(income × rate) − somme à déduire`.

### Example 1 — Small RNS service business, below exemption

Amine (RNS, services) has 2025 turnover **MAD 120,000** and net profit **MAD 35,000**. No other income; single, no dependents.

- Net taxable income MAD 35,000 → **first bracket (0%)** → **scale IR = 0**.
- **Cotisation minimale:** 120,000 × 0.25% = **MAD 300**, raised to the **MAD 1,500 floor** *(verify)* — **unless** he is still within the **3-year new-business CM exemption**, in which case CM = 0.
- **IR due = higher of (0, CM).** If exempt period applies → **MAD 0**; otherwise **MAD 1,500** (the floor). Flag the exemption-period question.

### Example 2 — RNR profit in the middle brackets

Fatima (RNR, commerce) nets **MAD 150,000** profit; turnover **MAD 900,000**; 2 dependents.

- Scale IR: 150,000 falls in the **34%** bracket → `(150,000 × 34%) − 22,000 = 51,000 − 22,000 = ` **MAD 29,000** (IR brut).
- Family deduction: 2 × 500 = **MAD 1,000** → IR net = **MAD 28,000** *(verify per-head amount)*.
- Cotisation minimale: 900,000 × 0.25% = **MAD 2,250**, above the 1,500 floor.
- **IR due = higher of (28,000, 2,250) = MAD 28,000.** CM is absorbed.

### Example 3 — Loss year, cotisation minimale bites

Karim (RNR) makes a **loss**; turnover **MAD 1,200,000**.

- Scale IR on professional income = **0** (no profit).
- Cotisation minimale: 1,200,000 × 0.25% = **MAD 3,000** (above floor).
- **IR due = MAD 3,000** (CM), unless within the 3-year exemption → 0.
- RNR/RNS deficit: attach the **état explicatif** of the loss; RNS **cannot carry the loss forward**, RNR generally can (verify carry-forward window).

### Example 4 — Liberal profession (higher CM rate)

Nadia, an architect (profession libérale, RNR), nets **MAD 90,000**; fees turnover **MAD 600,000**.

- Scale IR: 90,000 in the **30%** bracket → `(90,000 × 30%) − 18,000 = 27,000 − 18,000 = ` **MAD 9,000**.
- Cotisation minimale for **liberal professions at 4%** *(verify)*: 600,000 × 4% = **MAD 24,000** — **higher than** the scale IR.
- **IR due = higher of (9,000, 24,000) = MAD 24,000.** Flag the 4% CM rate explicitly; it dominates and is a common surprise.

### Example 5 — Combined revenu global

Hassan has professional net profit **MAD 70,000** (RNS) **plus** salary net of **MAD 50,000** already withheld at source.

- **Revenu global** = 70,000 + 50,000 = **MAD 120,000** → scale: `(120,000 × 34%) − 22,000 = 40,800 − 22,000 = ` **MAD 18,800** total IR on the global income.
- **Credit the salary withholding** (retenue à la source) already paid; the professional CM on turnover applies to the professional slice only.
- Net IR payable on filing = total scale IR − salary withholding − acomptes/CM credited. Reviewer to reconcile the withholding certificate.

## 5. Tier 1 Rules (deterministic — Code Général des Impôts)

These the agent applies directly, always with the "verify against current CGI / LF 2026" caveat:

- **Scope of IR professional income** — Revenus professionnels; RNR / RNS definitions and turnover ceilings.  _(CGI Art. 30–33)_
- **Net result determination** — Produits imposables and charges déductibles; deductibility requires the expense be incurred for the business, recorded, and supported.  _(CGI Art. 8, 9 & 10)_
- **RNS ceilings *(verify current values)*** — RNS available where turnover (HT) does not exceed: MAD 2,000,000 for commercial / industrial / artisanal, and MAD 500,000 for services and liberal professions. Exceeding for 2 consecutive years → mandatory move to RNR.  _(verify current values)_
- **Progressive scale (barème de l'IR)** — 0% to 37%, exempt band MAD 40,000 (2025 reform). Use the somme-à-déduire quick method in §1.  _(CGI Art. 73)_
- **Family deductions** — Déductions pour charges de famille: MAD 500/dependent, cap MAD 3,000 *(verify revaluation in LF 2026)*.  _(CGI Art. 74)_
- **Cotisation minimale (CM)** — Base = turnover HT + other operating income + financial income + subsidies; 0.25% standard, 0.15% regulated-margin goods, 4% liberal professions; minimum MAD 1,500 for IR; 3-year new-business exemption. IR due = higher of scale IR and CM.  _(CGI Art. 144)_
- **Non-deductible charges** — Fines/penalties, the IR/CM itself, the over-cap portion of cash payments above the regulatory threshold, and unsupported expenses are reintegrated to the result *(verify the cash-payment threshold)*.
- **Filing** — Déclaration du revenu global; télédéclaration and télépaiement via SIMPL-IR: annual return by 1 May of year N+1 *(verify each year)*; loss/nil years require an état explicatif.  _(CGI Art. 82 & 173)_
- **Advance payments (acomptes)** — The CM and any in-year acomptes/withholdings are paid during the year and credited against final IR on filing *(verify the exact acompte calendar applicable to IR professional income)*.

## 6. Tier 2 — Reviewer Judgement Required

Escalate to the **Moroccan expert-comptable** when:

- **System choice / election** — RNR vs RNS eligibility, the validity and timing of an RNS option, or a forced switch on ceiling breach.
- **Deductibility calls** — depreciation rates and policies, provisions (RNS cannot provision), mixed business/personal assets, related-party charges, the cash-payment non-deductibility threshold.
- **Loss treatment** — carry-forward eligibility and window under RNR; the état explicatif for nil/deficit results.
- **Revenu global assembly** — combining professional income with salary, rental, and capital income, and crediting withholdings at source.
- **Cotisation minimale edge cases** — the 4% liberal-profession rate, the 0.15% reduced rate, the new-business exemption window, and CM vs scale interaction.
- **Family deduction** — current per-head amount/cap after LF 2026; dependent eligibility (age, disability, students).
- **Any number where the agent fell back to a "verify" value.**

The agent presents the computation, the assumptions, and the open items — never as a settled, file-ready result.

## 7. Excel Template

**Excel Template**

| Cell / Row | Label | Formula / Input |
| --- | --- | --- |
| B1 | Turnover HT (CA) | input |
| B2 | Other operating + financial income + subsidies | input |
| B3 | **CM base** | `=B1+B2` |
| B4 | Deductible expenses (total) | input (from pattern library) |
| B5 | Reintegrations (non-deductible add-backs) | input |
| B6 | **Net professional result** | `=B1+B2-B4+B5` |
| B7 | Other revenu global (salary, rental, …) | input |
| B8 | **Net taxable income (revenu global)** | `=MAX(B6,0)+B7` |
| B9 | Bracket rate | lookup on B8 vs §1 scale |
| B10 | Somme à déduire | lookup on B8 vs §1 scale |
| B11 | **IR brut (scale)** | `=B8*B9-B10` |
| B12 | Dependents | input |
| B13 | Family deduction | `=MIN(B12*500,3000)` *(verify)* |
| B14 | **IR net (scale)** | `=MAX(B11-B13,0)` |
| B15 | CM rate | 0.25% / 0.15% / 4% (select) |
| B16 | CM raw | `=B3*B15` |
| B17 | **Cotisation minimale** | `=IF(new_business_exempt,0,MAX(B16,1500))` *(verify floor)* |
| B18 | **IR due (before credits)** | `=MAX(B14,B17)` |
| B19 | Acomptes / CM paid / withholdings | input |
| B20 | **Net IR payable on filing** | `=MAX(B18-B19,0)` |

The lookup in B9/B10 must use the §1 scale table. Keep the somme-à-déduire column flagged "verify" until reconciled with the current CGI Art. 73 text.

## 8. Bank Statement Guide

Morocco's main retail banks; statement layouts and label conventions:

### Attijariwafa Bank

- Labels often abbreviated: `VIR`, `VRST`, `RET GAB`, `PRLV`, `COM` (commissions).
- Client receipts: `VIREMENT RECU` / `VRT EN VOTRE FAVEUR`. Card acquiring (TPE): `REMISE TPE` / `VERSEMENT MONETIQUE` → turnover.
- Bank charges `COMMISSION` / `FRAIS TENUE DE COMPTE` → deductible business cost if the account is professional.

### BMCE / Bank of Africa

- `VIREMENT EN VOTRE FAVEUR`, `MISE A DISPOSITION`, `VRST ESPECES` → receipts.
- `PRELEVEMENT` (PRLV) for recurring suppliers/utilities → expense (classify by counterparty: ONEE/Lydec = utilities; IAM/Inwi/Orange = telecom).
- Loan lines `ECHEANCE CREDIT` → split principal (non-deductible) vs interest (deductible).

### Banque Populaire (BCP / BP régionales)

- `VERSEMENT`, `REMISE CHEQUE`, `VIREMENT RECU` → receipts.
- `CHABI` / mobile-wallet credits → confirm whether business receipts.
- `AGIOS`, `COMMISSIONS`, `INTERETS DEBITEURS` → finance cost (deductible if business); `INTERETS CREDITEURS` → financial income (in CM base).

- **Mixed account risk default** — Across all banks: a mixed personal/professional account is the biggest risk. Default private-looking lines (`RET GAB`, supermarkets, family transfers, school fees) to excluded and ask the user to confirm any business reclassification.

## 9. Onboarding

To use this skill, gather from the user:

1. **Are you an individual** running a business (not a company/IS)? If a company → refuse (R-MA-1).
2. **Which system** — RNR or RNS? If unsure, default to **RNR** and flag.
3. **Turnover (HT)** and **net accounting result** for the year, plus a **bank statement / ledger export** for classification.
4. **Activity type** — is it a **profession libérale**? (drives the 4% CM rate.)
5. **Other income** (salary, rental) and **dependents**.
6. **Start date** of the activity (3-year CM exemption test).
7. **Acomptes / CM / withholdings** already paid.

Then: classify transactions (§3), build the net result, run the scale (§1), test the cotisation minimale (§5.6), and present a **draft** for the expert-comptable.

### Legal & source references

- **Code Général des Impôts (CGI)** — Art. **30–33** (revenus professionnels, RNR / RNS), **8–10** (produits & charges), **73** (barème IR), **74** (charges de famille), **144** (cotisation minimale), **82 & 173** (déclaration / paiement).
- **Loi de Finances 2025** — IR reform: exempt band raised to **MAD 40,000**, top rate reduced to **37%**, brackets widened.
- **Loi de Finances 2026** — confirm carry-over of the scale and any revaluation of the family deduction and CM parameters.
- **DGI** — tax.gov.ma; **SIMPL-IR** télédéclaration — irpart.tax.gov.ma.
- **PwC Worldwide Tax Summaries — Morocco** — taxsummaries.pwc.com/morocco.

### Short test suite

1. **Q:** RNS, profit MAD 30,000, no other income. **A:** Scale IR **0** (under 40,000); CM = max(turnover × 0.25%, 1,500) unless within 3-year exemption.
2. **Q:** RNR, profit MAD 150,000, 2 dependents. **A:** `(150,000×34%)−22,000 = 29,000`, less family 1,000 = **MAD 28,000** (CM absorbed). *(verify per-head.)*
3. **Q:** RNR loss, turnover MAD 1.2M. **A:** Scale IR 0; **CM = MAD 3,000**; attach état explicatif; RNS cannot carry loss forward.
4. **Q:** Architect (libérale), turnover MAD 600k, profit MAD 90k. **A:** Scale IR MAD 9,000 vs **CM 4% = MAD 24,000** → IR due **MAD 24,000**.
5. **Q:** When is the annual return due? **A:** Déclaration du revenu global via **SIMPL-IR by 1 May** of year N+1 *(verify)*.
6. **Q:** Company (SARL) asks for IR. **A:** **Refuse (R-MA-1)** — that is **IS**.
7. **Q:** Freelancer on turnover-based tax. **A:** Route to `ma-auto-entrepreneur` / `ma-cpu` (R-MA-2).

## PROHIBITIONS

- **Do NOT** apply IR to a **company** — corporations pay **IS** (R-MA-1).
- **Do NOT** handle **auto-entrepreneur / CPU** turnover-based tax here — route to `ma-auto-entrepreneur` / `ma-cpu` (R-MA-2).
- **Do NOT** ignore the **cotisation minimale**: IR due = **higher** of scale IR and CM (floor MAD 1,500, 4% for liberal professions), subject to the 3-year exemption.
- **Do NOT** deduct **fines, penalties, the IR/CM itself, over-threshold cash payments, or unsupported expenses** — reintegrate them.
- **Do NOT** allow **RNS** to provision or carry losses forward — those are RNR-only features (verify carry-forward window).
- **Do NOT** state any **rate, somme-à-déduire, family deduction, ceiling, or deadline** as final without the **"verify current value"** caveat against the **Loi de Finances 2026** and the DGI.
- **Do NOT** advise on **TVA, IS, salary-only payroll IR, capital gains (TPI), treaties, or non-resident status** under this skill — route appropriately.
- **Do NOT** submit a **SIMPL-IR** return as filed without **expert-comptable** sign-off (R-MA-7).

## Disclaimer

This skill is **research-verified** against public sources (DGI / tax.gov.ma, the SIMPL-IR portal, PwC Worldwide Tax Summaries, and reporting on the Loi de Finances 2025/2026) as of **May 2026**. It is **YMYL** content and is **pending sign-off by a Moroccan accountant (expert-comptable)**. The progressive scale, the somme-à-déduire amounts, the family deduction, the cotisation minimale rates and floor, RNS ceilings, and filing deadlines change with each Loi de Finances and must be **re-verified** before use. Nothing here is a substitute for advice from a licensed Moroccan expert-comptable or the DGI. Part of **openaccountants.com** — open-source tax skills for the self-employed.
