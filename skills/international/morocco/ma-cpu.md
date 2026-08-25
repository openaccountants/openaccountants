---
name: ma-cpu
description: Use this skill whenever asked about Morocco's Contribution Professionnelle Unique (CPU) — the single-tax regime that replaced the régime forfaitaire (régime du bénéfice forfaitaire) for small self-employed people and professionals who are not on the auto-entrepreneur status. Trigger on phrases like "CPU Maroc", "Contribution Professionnelle Unique", "régime forfaitaire Maroc", "contribution professionnelle unique calcul", "droit complémentaire AMO CPU", "coefficient bénéfice CPU", "المساهمة المهنية الموحدة", "CPU vs auto-entrepreneur Maroc". Covers eligibility and turnover ceilings, the CPU computation (turnover × profession coefficient → 10% liberatory IR), the effective minimum, the mandatory complementary health contribution (droit complémentaire) banded by profit for AMO, and the filing & payment calendar. Reply in the user's language (English, French, or Moroccan Arabic / Darija) and keep the native terms (CPU, IR, DGI, AMO, CNSS). Cross-reference ma-auto-entrepreneur (simpler, lower ceilings) and ma-income-tax (RNR/RNS) as alternatives.
version: 1.0
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Cpu

## Morocco — Contribution Professionnelle Unique (CPU)

The **Contribution Professionnelle Unique (CPU)** — *المساهمة المهنية الموحدة* —
is Morocco's single-tax regime for small individual taxpayers whose professional
income was historically determined under the **régime du bénéfice forfaitaire**
(the flat-rate profit regime). The forfaitaire regime was **abrogated from 1
January 2021** and replaced by the CPU, instituted by **Article 6 of the Loi de
Finances n° 65.20** for budget year 2020.

The CPU bundles, into a **single payment**, the taxes that a small professional
used to pay separately:

- the **impôt sur le revenu (IR)** on professional income, plus
- the **taxe professionnelle (TP)** and **taxe de services communaux (TSC)** —
  both now **permanently exonerated** for CPU taxpayers (Loi 07-20 amending Loi
  47-06 on local taxation), plus
- a **droit complémentaire** (complementary duty) that funds social protection,
  in the first instance **mandatory basic health insurance (AMO)**.

CPU sits **between** the two other self-employed routes:

- **`ma-auto-entrepreneur`** — simpler, lower ceilings, a flat 0.5%/1% liberatory
  IR on collected turnover. Use when the taxpayer qualifies and is below the AE
  ceilings.
- **`ma-income-tax`** (RNR — *résultat net réel* / RNS — *résultat net
  simplifié*) — real-accounting regimes, mandatory above the CPU ceilings or by
  option. Use when the CPU ceilings are breached or real-expense deduction is
  beneficial.

This skill replies in the user's language. Moroccan users mix English, French,
and Darija — keep the native terms (CPU, IR, DGI, AMO, CNSS, droit
complémentaire) and explain them in the user's chosen language.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Regime | Contribution Professionnelle Unique (CPU) — replaced the régime forfaitaire from 2021 |
| Currency | MAD (dirham marocain, DH) |
| Turnover ceiling — commercial / industrial / artisanal | **MAD 2,000,000 / year (VAT included)** *(verify current value)* |
| Turnover ceiling — services / liberal professions | **MAD 500,000 / year (VAT included)** *(verify current value)* |
| Tax base | **Turnover × profession coefficient** (coefficient per the table annexed to **Art. 40-I CGI**) |
| Liberatory IR rate (1st component) | **10%** of the base → CPU IR = turnover × coefficient × 10% *(verify current value)* |
| 2nd component | **Droit complémentaire** (AMO health cover), banded by the annual CPU IR amount — **MAD 1,200 → 14,400 / year** (8 bands) *(verify table)* |
| Effective minimum | No Art. 144 cotisation minimale applies to CPU; the practical floor is the **lowest droit complémentaire band = MAD 1,200 / year** *(verify)* |
| Plus-values / indemnités (cession / cessation) | **20% liberatory IR** on the net gain *(verify rate)* |
| Annual CA declaration & payment | **Before 1 April** of the year following the year the turnover was earned |
| Payment options | **Annual** (before 1 April) **or quarterly** (4 acomptes of 25%, before end of months 3, 6, 9, 12 of the following year) |
| Existence declaration (new taxpayer) | Within **30 days** of starting activity |
| Authority | **Direction Générale des Impôts (DGI)** — tax.gov.ma |
| Portal | **SIMPL-CPU** on tax.gov.ma (declaration is **pre-filled** by the DGI) |
| Social cover | **AMO** via the droit complémentaire; CNSS-administered scheme |
| Primary legislation | LF 65.20 (2020); CGI Art. **40, 41, 43, 44, 73-II, 82 quater, 173-I**; Loi 07-20 (TP/TSC exemption) |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Version | 1.0 |

### Conservative defaults

- **Activity not stated** → default to the **services / liberal** branch and the
  **MAD 500,000** ceiling (the lower, stricter limit), and flag for confirmation.
- **Coefficient not known with certainty** → do **not** guess; state the
  computation as `turnover × coefficient × 10%`, leave the coefficient as a
  *verify-from-the-Art. 40-I CGI annex* placeholder, and escalate to Tier 2.
- **Multiple activities** → compute **each** activity separately with its own
  coefficient, then sum (CGI Art. 40 — `D = Σ (CAᵢ × coefficientᵢ)`).
- **Any rate / ceiling / band** → present with the **"verify against Loi de
  Finances 2026 and the DGI"** caveat; never as final.
- **AMO adhesion** → the droit complémentaire is **due once the taxpayer is
  affiliated** to basic AMO; treat affiliation as mandatory under the regime.

## 2. Eligibility & Ceilings

### Who is in scope

- **Scope of CPU applicability** — CPU applies to **individuals (personnes physiques)** with professional income who fall into one of these groups: taxpayers whose professional income **was determined under the old régime du bénéfice forfaitaire** before the 2021 reform (they roll into CPU automatically — **no formality required**, the prior forfaitaire declaration stands); taxpayers **starting** a professional activity who opt for CPU; taxpayers previously on **RNR / RNS** whose turnover has fallen **below the CPU ceiling** and who opt back into CPU.  _(CGI Art. 41; LF 65.20)_

### Turnover ceilings (VAT included)

**Turnover ceilings (VAT included)**

| Activity branch | Annual ceiling (TTC) |
| --- | --- |
| Commercial, industrial, artisanal | **MAD 2,000,000** *(verify)* |
| Services (prestations de services) and non-excluded liberal professions | **MAD 500,000** *(verify)* |

### Breach rule

- **Ceiling breach exit rule** — If a ceiling is exceeded for **two consecutive years**, the **RNR (résultat net réel)** regime applies from **1 January of the year following those two years**. A single year over the limit does **not** by itself force the exit — but flag it and watch the second year.

### Exclusions

- **Excluded activities** — Professions, activities, and services listed in **décret n° 2-08-124 (28 May 2009)** are **excluded from CPU regardless of turnover**. These are broadly the regulated/liberal professions (the same families typically excluded from the auto-entrepreneur regime). If the activity is one of these, route to **`ma-income-tax`**. When unsure whether an activity is excluded, **default to excluded** and escalate.  _(Décret n° 2-08-124 (28 May 2009))_

### Option mechanics & deadlines

- **Option mechanics and deadlines** — **New taxpayers** opting for CPU: send a registered request (or hand-deliver against receipt) to the inspecteur des impôts — **option at start of activity**: before **1 April** of the year following the start year; **option in the course of activity** (e.g. coming from RNR/RNS): within the deadline for filing the prior year's global income declaration, i.e. before **1 May** of the current year; the option takes effect **the following year**. The option stays valid **as long as** turnover has not exceeded the ceiling for two consecutive years.

## 3. Computation

- **CPU total formula** — CPU = IR component + Droit complémentaire = (Turnover × profession coefficient × 10%) + droit complémentaire (from table)

### 3.1 IR component (1ère composante)

- **IR component formula** — Taxable base   = Turnover (CA) × profession coefficient   ← coefficient per Art. 40-I CGI annex IR component   = Taxable base × 10%   (taux libératoire — flat liberatory rate) = CA × coefficient × 10%
- **Important points on IR component** — The **10% liberatory rate** is applied **directly** to the coefficient-adjusted base. The ordinary progressive **IR scale is NOT applied** to CPU income — the CPU's 10% replaces it. *(The progressive scale below is given only for context and for routing comparisons against `ma-income-tax`.)* **Mobile-payment turnover** (paiement mobile) for years **2020–2024** is **excluded** from the base (CGI Art. 247 ter incentive). Confirm whether any equivalent incentive continues for 2026. **Multiple activities** with different coefficients → compute each separately and sum.  _(CGI Art. 247 ter)_
- **Alimentation générale (general food retail)** — **8%**  _(**Confirmed** (DGI CPU guide example))_
- **Coiffeur (men's hairdresser)** — **40%**  _(**Confirmed** (DGI CPU guide example))_
- **Other commerce / services / artisanat / liberal** — **per the Art. 40-I CGI annex**  _(*Must be read from the annex — do not guess*)_
- **Do not invent coefficients** — Do **not** invent coefficients for any other activity. Read the exact value from the **annex to the CGI (Art. 40-I)** or the DGI's coefficient table.  _(Art. 40-I CGI)_

### Context only — ordinary IR progressive scale (2026)

**Ordinary IR progressive scale (2026) — context only, not applied to CPU**

| Annual taxable income (MAD) | Rate |
| --- | --- |
| 0 – 40,000 | **0% (exempt)** |
| 40,001 – 60,000 | 10% |
| 60,001 – 80,000 | 20% |
| 80,001 – 100,000 | 30% |
| 100,001 – 180,000 | 34% |
| Over 180,000 | **37%** |

This scale governs **RNR/RNS** taxpayers, **not** CPU. Use it only to compare routes or to model what happens if the taxpayer exits CPU.

*(2025 IR reform: exempt band raised to MAD 40,000, top rate cut to 37% — verify against Loi de Finances 2026.)*

### 3.2 Minimum

- **No cotisation minimale for CPU** — There is **no Article 144 cotisation minimale** for CPU taxpayers — the 0.25% (or 0.15%) minimum-contribution floor, raised to **MAD 3,000** for 2026, applies to **RNR/RNS and corporate (IS)** taxpayers, **not** to CPU. Under CPU the **effective floor** is the **lowest droit complémentaire band, MAD 1,200 / year**, which is payable once the taxpayer is affiliated to AMO even when the IR component is tiny. Do not apply the MAD 3,000 CM to a CPU return.  _(CGI Art. 144)_

### 3.3 Droit complémentaire (2ème composante — AMO health cover)

- **Droit complémentaire mechanics** — The **annual IR component** (1ère composante) determines, by band, the **droit complémentaire** payable for **AMO** (basic mandatory health insurance). It is due once the taxpayer adheres to the AMO scheme.

**Droit complémentaire bands table**  _(Source: DGI CPU practical guide table. Verify the bands and amounts against the current Loi de Finances / DGI publication.)_

| Annual IR component band (MAD) | Quarterly droit (MAD) | Annual droit (MAD) |
| --- | --- | --- |
| Less than 500 | 300 | **1,200** |
| 500 – 1,000 | 390 | **1,560** |
| 1,001 – 2,500 | 570 | **2,280** |
| 2,501 – 5,000 | 720 | **2,880** |
| 5,001 – 10,000 | 1,050 | **4,200** |
| 10,001 – 25,000 | 1,500 | **6,000** |
| 25,001 – 50,000 | 2,250 | **9,000** |
| Over 50,000 | 3,600 | **14,400** |

- **Pro-ration on part-year period** — The droit complémentaire is **pro-rated** when the period is shorter than a full year (e.g. on a mid-year cessation — see Example 3): annualize the IR component to find the band, then apply the months/12 fraction to the annual droit.

## 4. Filing & Payment Calendar

**Filing & Payment Calendar table**

| Obligation | Deadline | Form / channel |
| --- | --- | --- |
| **Existence declaration** (new taxpayer) | Within **30 days** of starting activity | Imprimé-modèle DGI; registered letter or against receipt |
| **Annual turnover (CA) declaration** | **Before 1 April** of the year following the year the turnover was earned | **SIMPL-CPU** on tax.gov.ma (pre-filled) — model **ADP150B**; paper accepted |
| **Annual payment** option | Spontaneous payment **before 1 April** (with the declaration) | Bordereau-avis **RSP150B**; télépaiement via SIMPL |
| **Quarterly payment** option | **4 acomptes of 25%** of the CPU due, before the end of **months 3, 6, 9 and 12** of the following year | Bordereau-avis **RSP150B** per quarter |
| **Plus-values / indemnités** declaration (cession / cessation) | Within **45 days** of the cession / cessation | Model **ADP160B**, bordereau **RSP160B** (CGI Art. 82 quater-II) |
| Transfer of fiscal domicile | Within **30 days** of the change | Imprimé-modèle DGI |
| Departure from Morocco | At least **30 days before** departure | — |
| Death | Within **3 months** of death | Heirs file |

- **All CPU taxpayers must file** — **All** CPU taxpayers must file the CA declaration, **including** those whose IR in principal is **below MAD 5,000** — the old exemption from filing (former Art. 86-4°) was abrogated by LF 2021.  _(Former CGI Art. 86-4° (abrogated by LF 2021))_
- **Declaration pre-filled by DGI** — The declaration is **pre-filled** by the DGI in SIMPL-CPU based on the regime's computation rules; the taxpayer chooses the annual or quarterly payment option and (where applicable) supplies the AMO affiliation number and date.
- **Late filing / late payment penalties** — **Late filing / late payment** (CGI Art. 184 / 208): typically a **penalty of 10%** (reduced to 5% if the delay ≤ 30 days), plus a **5%** surcharge for the first month of late payment and **0.5%** per additional month or fraction. *(Verify current rates.)*  _(CGI Art. 184 / 208)_

## 5. Worked Examples

> All figures illustrative; coefficients and bands must be verified against the
Art. 40-I CGI annex and the current DGI droit-complémentaire table.

### Example 1 — General food shop (alimentation générale)

- Turnover (CA): **MAD 375,000**; coefficient (alimentation générale): **8%**.
- IR component = `375,000 × 8% × 10%` = **MAD 3,000**.
- The MAD 3,000 IR falls in the **2,501–5,000** band → droit complémentaire =
  **MAD 2,880 / year**.
- **Total CPU = 3,000 + 2,880 = MAD 5,880 / year** (payable once AMO-affiliated).
- This mirrors the DGI's transitional example, where the same MAD 3,000 equalled
  the old IR + TP combined.

### Example 2 — New men's hairdresser (coiffeur), first year

- Turnover (CA): **MAD 60,000**; coefficient (coiffeur): **40%**.
- IR component = `60,000 × 40% × 10%` = **MAD 2,400**.
- The MAD 2,400 IR falls in the **1,001–2,500** band → droit complémentaire =
  **MAD 2,280 / year**.
- **Total CPU = 2,400 + 2,280 = MAD 4,680 / year**.

### Example 3 — Mid-year cessation with plus-value

- A carpenter (menuisier), AMO-affiliated, **ceases on 30 June** and **sells the
  business for MAD 180,000**, realizing a **net gain of MAD 100,000**. He earned
  **MAD 90,000** turnover in the first half; assume coefficient **12%** *(verify
  from the annex)*.
- **CPU on the half-year turnover:** `90,000 × 12% × 10%` = **MAD 1,080**.
- **Droit complémentaire (pro-rated):** annualize the IR — `1,080 × (12/6) = 2,160`
  → falls in the **1,001–2,500** band → annual droit **MAD 2,280**; pro-rate to 6
  months: `2,280 × 6/12 =` **MAD 1,140**.
- CPU to pay = `1,080 + 1,140 =` **MAD 2,220**.
- **Plus-value:** `100,000 × 20% =` **MAD 20,000** (separate 20% liberatory IR;
  declared on **ADP160B** within **45 days**).

### Example 4 — Ceiling breach (routing, not a CPU number)

- A trader's turnover is **MAD 2,300,000** (commercial) for a second consecutive
  year. The **MAD 2,000,000** ceiling is breached two years running → **RNR
  applies from 1 January** of the next year. Do **not** compute CPU; route to
  **`ma-income-tax`** and flag VAT (TVA) registration implications (see
  `morocco-vat`).

## 6. Tier 2 — Reviewer Judgement Required

Escalate to the **Moroccan expert-comptable** reviewer when:

- The **profession coefficient** is anything other than the confirmed values
  (alimentation 8%, coiffeur 40%) — the exact Art. 40-I annex value must be read
  and verified.
- **Borderline excluded activity** (possible décret 2-08-124 / regulated
  profession) — eligibility call; default to excluded.
- **Ceiling breach** in the current or prior year — exit timing (one vs two
  consecutive years), RNR/RNS routing, and **TVA** registration.
- **Multiple activities** straddling both ceilings or mixing coefficients.
- **Mobile-payment turnover** treatment (the 2020–2024 exclusion) and whether any
  equivalent incentive applies in 2026.
- **AMO affiliation** status / arrears — whether the droit complémentaire is yet
  payable, and the pro-rata on a part-year.
- **Plus-values / cessation** computations (depreciation recapture, indemnités).
- Any number where the agent had to fall back to a "verify" value.

The agent must **never** present these as settled; it presents the computation,
the assumptions, and the open items for the reviewer to sign off.

## 7. Reference

### Legal references (Code Général des Impôts and related)

- **CGI Art. 40-I** — determination of the CPU professional income (turnover × profession coefficient); **annexed coefficient table** by activity.  _(CGI Art. 40-I)_
- **CGI Art. 41** — conditions of application of the CPU regime.  _(CGI Art. 41)_
- **CGI Art. 43 / 44** — turnover ceilings and the base.  _(CGI Art. 43 / 44)_
- **CGI Art. 73-II** — the **10% liberatory rate** (IR component) and the **20%** rate on plus-values / indemnités; **Art. 73-II-B-6°** — the droit complémentaire.  _(CGI Art. 73-II)_
- **CGI Art. 82 quater** — declaration of turnover and of plus-values/indemnités under the CPU.  _(CGI Art. 82 quater)_
- **CGI Art. 173-I** — spontaneous payment (bordereau-avis de versement).  _(CGI Art. 173-I)_
- **CGI Art. 184 / 208** — late-filing and late-payment penalties.  _(CGI Art. 184 / 208)_
- **CGI Art. 247 ter** — exclusion of 2020–2024 mobile-payment turnover from the base.  _(CGI Art. 247 ter)_
- **Loi de Finances n° 65.20 (2020), Art. 6** — institution of the CPU; abrogation of the régime du bénéfice forfaitaire from 1 January 2021.  _(LF n° 65.20 (2020), Art. 6)_
- **Loi 07-20 amending Loi 47-06** — permanent exemption from **taxe professionnelle (TP)** and **taxe de services communaux (TSC)** for CPU taxpayers.  _(Loi 07-20 amending Loi 47-06)_
- **Décret n° 2-08-124 (28 May 2009)** — list of activities/professions excluded from CPU.  _(Décret n° 2-08-124 (28 May 2009))_
- **Loi de Finances 2026 (LF n° 50-25) and Note Circulaire DGI n° 737** — confirm current ceilings, the 10% rate, the coefficient annex, and the droit complémentaire bands.  _(LF n° 50-25 / Note Circulaire DGI n° 737)_

Authority: **Direction Générale des Impôts (DGI)** — tax.gov.ma (portal
**SIMPL-CPU**). Social: **AMO / CNSS** — cnss.ma.

Official forms: **ADP150B** (CA declaration), **RSP150B** (payment bordereau),
**ADP160B / RSP160B** (plus-values & indemnités).

### Short test suite

1. **Q:** Alimentation générale, CA MAD 375,000, coefficient 8%. **A:** IR =
   375,000 × 8% × 10% = **MAD 3,000**; droit complémentaire band 2,501–5,000 =
   **MAD 2,880**; total **MAD 5,880**.
2. **Q:** Coiffeur, CA MAD 60,000, coefficient 40%. **A:** IR = 60,000 × 40% ×
   10% = **MAD 2,400**; droit band 1,001–2,500 = **MAD 2,280**; total **MAD
   4,680**.
3. **Q:** Services freelancer, CA MAD 700,000. **A:** **Ceiling breached**
   (>500,000 for services) — flag; if breached two years running route to
   **`ma-income-tax`** (RNR).
4. **Q:** Activity branch not stated. **A:** Default to **services / MAD 500,000
   ceiling**; do not assume a coefficient — escalate.
5. **Q:** Coefficient for "atelier de soudure" not known. **A:** Do **not** guess;
   state `CA × coefficient × 10%`, read coefficient from the **Art. 40-I annex**,
   Tier 2.
6. **Q:** Doctor / lawyer wants CPU. **A:** **Excluded** (décret 2-08-124 /
   regulated profession) — route to **`ma-income-tax`**.
7. **Q:** Does the MAD 3,000 cotisation minimale apply? **A:** **No** — Art. 144
   CM does not apply to CPU; the practical floor is the **MAD 1,200** droit
   complémentaire band.
8. **Q:** Sold the business, net gain MAD 100,000. **A:** **20% liberatory** =
   **MAD 20,000**; declare on **ADP160B** within **45 days**.

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** apply the **ordinary progressive IR scale** to CPU income — the CPU IR component is the **flat 10% liberatory** rate on the coefficient-adjusted base. - **Do NOT** invent a **profession coefficient** — only `alimentation générale = 8%` and `coiffeur = 40%` are confirmed here; every other value must be read from the **Art. 40-I CGI annex**. - **Do NOT** apply the **Art. 144 cotisation minimale (MAD 3,000)** to a CPU taxpayer — it does not apply to CPU. - **Do NOT** confirm eligibility for a **regulated / liberal profession** or any activity on **décret 2-08-124** — default to **excluded**, route to `ma-income-tax`. - **Do NOT** keep computing CPU once a **ceiling** is breached for two consecutive years — route to **`ma-income-tax`** (RNR) and flag TVA. - **Do NOT** omit the **droit complémentaire** — the CPU is IR component **plus** the AMO duty; remember to **pro-rate** it on a part-year. - **Do NOT** deduct **business expenses** — the CPU base is **turnover × the profession coefficient**, not real net profit. - **Do NOT** state any rate, ceiling, coefficient, or band as final without the **"verify against Loi de Finances 2026 and the DGI"** caveat. - **Do NOT** advise on **TVA**, employees / payroll, or company forms (SARL/SA) under this skill — route to the relevant skill. - **Do NOT** issue a return as filed without **expert-comptable** sign-off.

## Disclaimer

This skill is **research-verified** against public sources — the **DGI**
(tax.gov.ma), the official **DGI "Guide pratique relatif à l'application du régime
de la CPU"**, **PwC Worldwide Tax Summaries** (Morocco), and reporting on the
**Loi de Finances 2025/2026** — as of **May 2026**. It is **YMYL** content and is
**pending sign-off by a Moroccan accountant (expert-comptable)**. Coefficients,
rates, ceilings, droit-complémentaire bands, and deadlines change with each Loi de
Finances and must be **re-verified** before use. Nothing here is a substitute for
advice from a licensed Moroccan expert-comptable or the DGI. Part of
**openaccountants.com** — open-source tax skills for the self-employed.

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
