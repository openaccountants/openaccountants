---
name: ma-social-contributions
description: Use this skill whenever asked about Morocco social contributions for the self-employed — the CNSS scheme for travailleurs non-salariés (TNS), the mandatory AMO health-insurance generalisation, and the dedicated social cover for auto-entrepreneurs. Trigger on phrases like "CNSS auto-entrepreneur", "AMO Maroc", "social security Morocco self-employed", "TNS Maroc", "cotisation CNSS indépendant", "couverture sociale travailleur non salarié", "تغطية صحية للعمل الحر", "CNSS Maroc cotisation", "retraite TNS Maroc", "AMO travailleur non salarié". Covers the profession-by-profession TNS rollout, the forfaitaire (SMIG-indexed) contribution base, AMO and retraite rates and minimums, registration and quarterly payment, and the contrast with employee CNSS (employer/employee split, salary ceiling) for those who hire. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-auto-entrepreneur and ma-cpu, which bundle their own social-cover components.
version: 1.0
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Social Contributions

## Morocco — Social Contributions for the Self-Employed (CNSS / AMO / Retraite TNS)

Morocco is in the middle of a multi-year **généralisation de la protection sociale**
(social-protection roll-out, Loi-cadre n° 09-21). The headline goal is to bring every
worker — salaried and **non-salaried (travailleurs non-salariés, TNS)** — into the
**Caisse Nationale de Sécurité Sociale (CNSS)** for **mandatory health insurance
(Assurance Maladie Obligatoire, AMO)** and a **basic pension (retraite de base)**.

For the self-employed this happens **profession by profession**: each socioprofessional
category is brought in by its own **décret** that fixes a **forfaitaire (flat) income
base** for that category. Auto-entrepreneurs have a **dedicated, turnover-linked**
variant. Anyone who **hires staff** also has the ordinary **employer/employee CNSS**
obligations, which work very differently (percentages on real salary, with a ceiling).

This skill replies in the user's language. Moroccan users mix English, French, and
Darija — keep the native terms (CNSS, AMO, TNS, retraite, SMIG, DGI) and explain them
in the user's chosen language.

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Topic | Social contributions for the self-employed — CNSS / AMO / retraite |
| Authority | **CNSS** (Caisse Nationale de Sécurité Sociale) — cnss.ma |
| Currency | **MAD** (dirham marocain, DH) |
| Legal framework | **Loi-cadre n° 09-21** (généralisation); **Loi n° 98-15** (AMO base TNS); **Loi n° 99-15** (retraite TNS); category décrets |
| TNS — AMO rate (active) | **6.37%** of the forfaitaire base *(verify current value)* |
| TNS — AMO rate (pensioners) | **4.52%** of total base pensions *(verify)* |
| TNS — retraite (pension) rate | **10%** of the forfaitaire base *(verify)* |
| TNS — contribution base | **Forfaitaire**, indexed to **SMIG**, **1.75× to 2.75× SMIG** by category *(verify)* |
| SMIG (reference) | **16.29 MAD/hour ≈ MAD 3,111.39/month** (Jan 2024 figure) *(verify current SMIG)* |
| Auto-entrepreneur base | **50% of turnover (services)** / **20% of turnover (commercial)** *(verify)* |
| Auto-entrepreneur minimum | **~MAD 300 / quarter (≈ MAD 1,200/year)**, even at zero turnover; annual range cited **MAD 1,200–14,400** *(verify)* |
| Employee CNSS (total) | **~27.83%** of gross — employer **~21.09%** / employee **~6.74%** *(verify)* |
| Employee CNSS ceiling | **MAD 6,000 / month** for capped (short/long-term) branches *(verify)* |
| Uncapped employee branches | AMO, allocations familiales, taxe de formation professionnelle (whole salary) *(verify)* |
| Filing & payment (TNS / AE) | **Quarterly**, online via cnss.ma / ae.gov.ma *(verify exact dates)* |
| Filing & payment (employer) | **Monthly** DAMANCOM teledeclaration *(verify)* |
| Cross-references | `ma-auto-entrepreneur`, `ma-cpu`, `ma-income-tax`, `morocco-vat` |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan expert-comptable** |
| Version | 1.0 |
| Last research update | May 2026 |

### Conservative defaults

When data is missing or ambiguous, the agent applies the **conservative default** and
flags it for the reviewer:

- **Profession not yet confirmed as "rolled out"** → assume affiliation **is now
  mandatory** (the roll-out is broad by 2026) and tell the user to confirm their
  category's **décret** and effective date on cnss.ma.
- **Category / forfaitaire base unknown** → do **not** guess the bracket; quote the
  rate formula and send the user to the **category décret** for the exact base.
- **Activity mix unknown (auto-entrepreneur)** → treat as **services (50% base)**, the
  higher base, until commercial (20%) is confirmed.
- **Zero / low turnover** → assume the **minimum contribution still applies** (no
  exoneration for "no income").
- **Has any staff** → assume **employer CNSS registration and monthly DAMANCOM** are
  due, separate from the owner's own TNS cover.
- **2026 figures** → every rate, base multiple, ceiling, and minimum carries "verify
  current value"; check the **Loi de Finances 2026**, the relevant **décret**, and
  **cnss.ma** before finalising any number.

## 2. Who Contributes

Three distinct populations, three different mechanics. Identify which one the user is in
**before** computing anything — they do not mix the same way.

### 2a. Travailleurs non-salariés (TNS) — by profession

The **TNS** regime covers self-employed people who are **not** auto-entrepreneurs and
**not** employees: independent professionals, regulated/liberal professions, and
own-account traders/artisans with accounts. They are brought in **category by
category**, each by a **décret** that fixes a **forfaitaire income** for that group.

Categories already brought in (illustrative, **non-exhaustive** — confirm each on
cnss.ma):

- **CPU** payers (Contribution Professionnelle Unique) — the largest cohort → see
  `ma-cpu`, which **bundles** its own AMO/social component.
- **Commerçants et artisans** keeping accounts (tenant une comptabilité).
- **Health professions:** médecins (doctors), pharmaciens, dentistes (chirurgiens-
  dentistes), sages-femmes, kinésithérapeutes, infirmiers, opticiens.
- **Legal / court professions:** notaires, adouls, avocats, huissiers, experts-
  comptables (each by its own décret / ordre).
- **Architects, engineers, and other ordres professionnels** as their décrets land.

> Each profession's **forfaitaire base** is set in **its own décret**. The agent must
> not transplant one category's base onto another.

### 2b. Auto-entrepreneurs — dedicated cover

Auto-entrepreneurs have a **dedicated, simplified** social cover: affiliation is
**automatic** on RNAE registration, and the contribution is **linked to declared
turnover** rather than a fixed category forfait (see §3 and `ma-auto-entrepreneur`).

### 2c. Employees and those who hire (ordinary CNSS)

If a self-employed person **hires staff**, they become an **employer** with the
**ordinary CNSS** obligations: percentage contributions on **real salary**, split
**employer / employee**, with a **ceiling** on some branches. This is **separate** from
the owner's own TNS/AE cover and is handled below in §3c.

## 3. Base, Rates & Minimums

### 3a. TNS (regulated/independent professions)

- **Forfaitaire base and opting up** — Contributions are computed on a **forfaitaire (flat) base** set by the worker's **category décret**, indexed to the **SMIG**, in a band of roughly **1.75× to 2.75× SMIG**. A TNS may, on registration, **opt for a higher base** than the category default, and may **change the base once a year** (request filed ~60 days before it takes effect) *(verify)*.  _((verify))_

**TNS regime rates and bases**

| Regime | Rate (active) | Base |
| --- | --- | --- |
| **AMO** (health) | **6.37%** *(verify)* | Forfaitaire base (1.75×–2.75× SMIG) |
| **Retraite** (pension) | **10%** *(verify)* | Same forfaitaire base |
| **AMO** (pensioners) | **4.52%** of base pensions *(verify)* | Pension, precompted by the payer |

- **Monthly TNS contribution formula** — Monthly TNS contribution = forfaitaire base × (AMO rate + retraite rate) ≈ base × (6.37% + 10%)        (verify both rates)  _((verify))_

> The AMO and retraite are **distinct regimes** with distinct décrets; retraite
> enrolment timing has been **phased** after AMO for some categories. Confirm whether
> the user's category is in **both** AMO and retraite yet.

### 3b. Auto-entrepreneurs

- **Auto-entrepreneur base — services** — ≈ 50% of collected turnover *(verify)* % (services (prestations))  _((verify))_
- **Auto-entrepreneur base — commercial/industrial/artisanal** — ≈ 20% of collected turnover *(verify)* % (commercial / industrial / artisanal)  _((verify))_
- **Auto-entrepreneur base derivation and brackets** — The auto-entrepreneur base is derived **from turnover**, not from a category forfait. The CNSS applies the TNS rates (AMO + retraite) to that derived base, and the result is **collected quarterly with the tax** via the AE portal. The scheme is commonly described through **fixed brackets (tranches) T1–T8**, each with a set quarterly amount.  _((verify the current bracket table))_
- **Minimum contribution at zero turnover** — ~MAD 300/quarter (≈ MAD 1,200/year) MAD (applies even at zero turnover)  _((verify))_
- **Annual contribution range** — MAD 1,200 to ~14,400 depending on turnover MAD  _((verify the current bracket table))_
- **AMO waiting period for auto-entrepreneurs** — AMO benefits start after a 3-month stage (waiting period) from the first contribution *(verify)*.  _((verify))_

> **Default:** when the exact bracket amount is unknown, quote the **~MAD 300/quarter**
> floor and send the user to **cnss.ma / ae.gov.ma** for their bracket. Do **not**
> invent a T1–T8 amount. See `ma-auto-entrepreneur` for the full AE picture.

### 3c. Employee CNSS (employer / employee split) — for those who hire

- **Employee CNSS total split** — Ordinary employee social charges in 2026 total roughly **27.83%** of gross salary, split **employer ~21.09% / employee ~6.74%** *(verify)*. Critically, **some branches are capped** and **some are not**.  _((verify))_

**Employee CNSS branches — capped vs uncapped**

| Branch | Capped at MAD 6,000/month? | Notes *(all rates verify)* |
| --- | --- | --- |
| Prestations sociales (short + long term, incl. base pension) | **Yes** — capped | Employee ~4.48%; employer ~8.98% on the capped salary |
| AMO (health) | **No** — whole salary | Employee ~2.26%; employer ~2.26% base + AMO Solidarité ~1.85% |
| Allocations familiales (family allowances) | **No** — whole salary | Employer ~6.40% |
| Taxe de formation professionnelle (TFP) | **No** — whole salary | Employer ~1.60% |

- **Ceiling application scope** — > The **MAD 6,000/month ceiling** applies **only** to the capped (prestations > sociales) branch. AMO, family allowances, and TFP are computed on the **full** > salary. This is the central contrast with the self-employed: the **TNS base is a > SMIG-indexed forfait**, whereas the **employee base is real salary, partly capped**.  _((verify))_

## 4. Registration & Payment

### TNS / regulated professions

- **TNS registration and payment steps** — 1. Affiliate with **CNSS** under the décret for your **category** (some ordres professionnels coordinate this). 2. CNSS assigns the **forfaitaire base**; you may **opt up** to a higher base. 3. **Declare and pay quarterly**, online via **cnss.ma** *(verify portal/dates)*.  _((verify portal/dates))_

### Auto-entrepreneurs

- **Auto-entrepreneur registration and payment steps** — 1. Registration in the **RNAE** (rn.ae.gov.ma, Poste Maroc / Al Barid Bank) **automatically** triggers CNSS affiliation. 2. Social contribution is **collected quarterly alongside the impôt libératoire** via the AE portal — including **nil (néant)** quarters. 3. AMO benefits begin after the **3-month stage**.

### Employers (those who hire)

- **Employer registration and payment steps** — 1. Register the **business** as an employer with CNSS and obtain the **affiliation number**. 2. **Declare and pay monthly** via **DAMANCOM** (teledeclaration), withholding the employee share from payroll *(verify deadline — typically before the end of the month following the period)*.  _((verify deadline))_

## 4. Registration & Payment

> A self-employed person who hires staff has **two** distinct CNSS relationships: their
> **own** TNS/AE cover **and** the **employer** obligation for staff. Keep them separate.

## 5. Worked Examples

> All figures use the 2026 rates/bases flagged "verify". Recompute with the confirmed
> category décret values and current SMIG before relying on them.

### Example 1 — TNS regulated professional (forfaitaire base)

Dr. Amine is a self-employed doctor (TNS). His category décret sets a forfaitaire base
of, say, **2× SMIG ≈ MAD 6,223/month** *(verify the exact category base)*.

- **AMO** = 6,223 × 6.37% ≈ **MAD 396/month** *(verify rate)*.
- **Retraite** = 6,223 × 10% ≈ **MAD 622/month** *(verify rate)*.
- **Total ≈ MAD 1,018/month**, paid **quarterly** (≈ MAD 3,055/quarter).
- Flag: confirm the **exact forfaitaire base** in the medical-profession décret — the
  2× SMIG used here is **illustrative**.

### Example 2 — Auto-entrepreneur, services (turnover-linked)

Sara is an auto-entrepreneur web developer (services). Quarterly collected turnover
**MAD 60,000**.

- Social base ≈ **50% × 60,000 = MAD 30,000** for the quarter *(verify the 50%)*.
- CNSS applies the AMO + retraite rates to that base, **placing her in a T1–T8 bracket**
  — quote the **bracket amount from cnss.ma / ae.gov.ma**, not a computed guess.
- Even a **zero-turnover** quarter still owes the **~MAD 300 minimum** *(verify)*.
- Cross-reference `ma-auto-entrepreneur` for the parallel **impôt libératoire** (1% for
  services) collected at the same time.

### Example 3 — Self-employed person who hires one employee (employer split)

Khadija runs a CPU micro-business (own TNS cover via `ma-cpu`) and hires **one
assistant** at **MAD 8,000/month** gross.

- For the assistant, the **capped branch** uses **MAD 6,000** (the ceiling), the
  **uncapped branches** use the **full MAD 8,000**:
  - Employee prestations sociales ≈ 6,000 × 4.48% ≈ **MAD 269** *(verify)*.
  - Employee AMO ≈ 8,000 × 2.26% ≈ **MAD 181** *(verify)* → withheld from pay.
  - Employer prestations ≈ 6,000 × 8.98% ≈ **MAD 539**; employer family allowances
    ≈ 8,000 × 6.40% ≈ **MAD 512**; employer AMO + TFP on full salary *(verify all
    rates)*.
- Khadija files this **monthly via DAMANCOM**. Her **own** social cover stays under the
  **CPU/TNS** track — it is **not** part of the employee computation.

## 6. Tier 2 — Reviewer Judgement Required

Escalate to the **Moroccan expert-comptable** reviewer when:

- The user's **profession's roll-out status** or **effective date** is uncertain (is
  the category in AMO yet? in retraite yet?).
- The **exact forfaitaire base** for the category must be read off a specific décret.
- A TNS wants to **opt up** to a higher base, or change the base, and needs the pension
  trade-off modelled.
- The user **hires staff** — full employer payroll/CNSS setup, DAMANCOM, and the
  capped/uncapped branch allocation (see `payroll`-type work).
- **Auto-entrepreneur ceiling breach** or exit (re-route via `ma-auto-entrepreneur` /
  `ma-cpu` / `ma-income-tax`), including how social cover changes on exit.
- **Cross-border / detachement** (a TNS working abroad, or a foreign self-employed
  person in Morocco) and CNSS social-security agreements.
- **Arrears, benefit eligibility, or the 3-month AMO stage / pension vesting** (3,240
  days) disputes.
- Any number where the agent had to fall back to a **"verify"** value or an
  **illustrative** base.

The agent must **never** present these as settled; it presents the computation, the
assumptions, and the open items for the reviewer to sign off.

## 7. Reference + Test Suite

### Legal & source references

- **Legal & source references list** — - **Loi-cadre n° 09-21** relative à la protection sociale (généralisation roadmap). - **Loi n° 98-15** — régime AMO de base for the **non-salariés (TNS)**. - **Loi n° 99-15** — régime de **pension (retraite)** for the non-salariés. - **Category décrets** — fix the **forfaitaire base** per socioprofessional group (CPU payers, commerçants/artisans, médecins, pharmaciens, dentistes, notaires, adouls, avocats, architects, etc.). **Verify each on cnss.ma.** - **Décret n° 2.21.477 (2021)** — mandatory CNSS/AMO for **auto-entrepreneurs**. - **Loi de Finances 2026** — confirm current rates, SMIG, ceiling, and minimums. - Authority: **CNSS** — cnss.ma (TNS portal, DAMANCOM for employers). Tax interaction: **DGI** — tax.gov.ma. AE register: **RNAE** — rn.ae.gov.ma. - Secondary corroboration: PwC Worldwide Tax Summaries (Morocco), CLEISS (cotisations Maroc), Moroccan accounting practices (figures cross-checked May 2026).  _(Loi-cadre n° 09-21; Loi n° 98-15; Loi n° 99-15; Décret n° 2.21.477 (2021); Loi de Finances 2026)_

### Short test suite

1. **Q:** TNS doctor, category base = 2× SMIG. **A:** AMO 6.37% + retraite 10% on the
   **category forfaitaire base** *(verify base and rates)*; paid quarterly.
2. **Q:** Auto-entrepreneur, services, zero turnover this quarter. **A:** Still owes the
   **~MAD 300 minimum** *(verify)*; AMO benefits only after the 3-month stage.
3. **Q:** Auto-entrepreneur, commercial. **A:** Base ≈ **20% of turnover** *(verify)*;
   bracket amount from cnss.ma — do **not** compute a guess.
4. **Q:** Employee paid MAD 10,000/month — what's capped? **A:** Only the **prestations
   sociales** branch is capped at **MAD 6,000**; **AMO, family allowances, TFP** apply to
   the **full** salary *(verify rates)*.
5. **Q:** Which rate split for employees? **A:** Total ≈ **27.83%**, employer ≈ 21.09% /
   employee ≈ 6.74% *(verify)*.
6. **Q:** Is a freelance graphic designer's profession "rolled out" yet? **A:** Default
   to **mandatory**; confirm the **category décret** and effective date on cnss.ma —
   escalate (Tier 2).
7. **Q:** Self-employed CPU payer hires staff. **A:** Two relationships — own **CPU/TNS**
   cover (`ma-cpu`) **plus** ordinary **employer CNSS** via **DAMANCOM** for the staff.

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** transplant one category's **forfaitaire base** onto another — each TNS category has its **own décret base**. - **Do NOT** invent auto-entrepreneur **T1–T8 bracket** amounts — quote the **~MAD 300 minimum** floor and send the user to cnss.ma / ae.gov.ma. - **Do NOT** apply the **MAD 6,000 ceiling** to AMO, family allowances, or the training tax — the ceiling is **only** for the capped prestations-sociales branch. - **Do NOT** conflate **TNS / auto-entrepreneur** self-cover with the **employer/employee** computation — a person who hires has **both**, computed separately. - **Do NOT** assume "no income → no contribution" — a **minimum** applies regardless. - **Do NOT** state any rate, base multiple, ceiling, SMIG, or minimum as final without the **"verify current value"** caveat against the **Loi de Finances 2026** and the relevant **décret**. - **Do NOT** advise on **employee payroll mechanics, IR withholding, TVA, or company forms** under this skill — route to the relevant skill (`ma-income-tax`, `morocco-vat`, etc.). - **Do NOT** confirm a profession's **roll-out / effective date** without checking cnss.ma — escalate if uncertain. - **Do NOT** issue any filing or computation as final without **Moroccan expert-comptable** sign-off.

## Disclaimer

This skill is **research-verified** against public sources (CNSS / cnss.ma including the
official TNS and AMO rate pages, the généralisation framework laws, PwC Worldwide Tax
Summaries, CLEISS, and reporting on the Loi de Finances 2025/2026) as of **May 2026**.
It is **YMYL** content and is **pending sign-off by a Moroccan expert-comptable**. The
social-protection roll-out is **ongoing and category-specific**; rates, the SMIG, the
forfaitaire bases, ceilings, brackets, and effective dates change with each décret and
each Loi de Finances and must be **re-verified** before use. Nothing here substitutes
for advice from a licensed Moroccan expert-comptable or the CNSS. Part of
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
