---
name: ma-auto-entrepreneur
description: Use this skill whenever asked about Morocco's auto-entrepreneur regime — the simplified turnover-based tax and social-cover status for freelancers and micro-businesses. Trigger on phrases like "auto-entrepreneur Maroc", "Morocco freelancer tax", "régime auto-entrepreneur", "micro business Morocco tax", "RNAE", "statut auto-entrepreneur", "تاجر ذاتي", "freelance Maroc impôt". Covers turnover ceilings, the 0.5%/1% liberatory IR, the single-client 80,000 MAD anti-disguised-salary withholding, dedicated CNSS/AMO cover, registration via the RNAE (Poste Maroc / ae.gov.ma), excluded regulated professions, and exit on ceiling breach. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-cpu and ma-income-tax for alternatives.
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

# MA Auto Entrepreneur

## Morocco — Auto-Entrepreneur Regime (Statut de l'Auto-Entrepreneur)

The **auto-entrepreneur** (AE) status is Morocco's flagship simplified regime for freelancers, sole traders, and micro-businesses. It replaces ordinary income-tax accounting with a single **impôt libératoire** computed as a flat percentage of **turnover actually collected** (chiffre d'affaires encaissé), bundles a dedicated social-cover scheme (**CNSS / AMO**), and is administered through the national register **RNAE** (Registre National de l'Auto-Entrepreneur). It is governed by **Loi n° 114-13** and Articles **42 bis, 42 ter, 43, 44-II and 73-III** of the **Code Général des Impôts (CGI)**.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (auto-entrepreneur, IR, CNSS, AMO, DGI, RNAE) and explain them in the user's chosen language.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Regime | Auto-entrepreneur (statut de l'auto-entrepreneur) — impôt libératoire on turnover |
| Currency | MAD (dirham marocain, DH) |
| Turnover ceiling — commercial / industrial / artisanal | **MAD 500,000 / year** *(verify current value)* |
| Turnover ceiling — services (prestations de services) | **MAD 200,000 / year** *(verify current value)* |
| IR rate — commercial / industrial / artisanal | **0.5% of collected turnover** *(verify current value)* |
| IR rate — services | **1% of collected turnover** *(verify current value)* |
| Single-client anti-disguised-salary rule | Amounts > **MAD 80,000 / year** from one client (services) → client withholds **30%** at source on the excess, liberatory *(verify rate)* |
| Tax base | Turnover **collected**, no deduction of expenses |
| Authority | **Direction Générale des Impôts (DGI)** — tax.gov.ma |
| Register / portal | **RNAE** via Poste Maroc / Al Barid Bank — `rn.ae.gov.ma` (a.k.a. ae.gov.ma) |
| Social cover | Dedicated **CNSS / AMO** scheme, mandatory since décret 2.21.477 (2021) |
| Filing & payment | **Quarterly**, online, including nil (néant) declarations |
| Primary legislation | Loi 114-13; CGI Art. 42 bis, 42 ter, 43, 44-II, 73-III |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Version | 1.0 |
| Last research update | May 2026 |

### Conservative defaults

When data is missing or ambiguous, the agent applies the **conservative default** and flags it for the reviewer:

- **Activity mix unknown** → treat the activity as **services (1%)**, the higher rate, until the user confirms it is commercial/industrial/artisanal (0.5%).
- **Turnover near a ceiling** → assume the ceiling is **breached** and warn about exit consequences rather than assume continued eligibility.
- **Single-client revenue near MAD 80,000** → assume the **30% withholding** on the excess applies, and tell the user to confirm with the paying client.
- **Eligibility uncertain (possible regulated profession)** → assume the activity is **excluded** and route to `ma-cpu` / `ma-income-tax` until confirmed.
- **2026 figures** → all rates and ceilings carry "verify current value"; check the **Loi de Finances 2026** and the DGI before finalising any number.

## 2. Eligibility & Excluded Activities

### Who can opt in

- **Eligibility criteria** — Resident **physical persons** (individuals) carrying on an **industrial, commercial, artisanal, or service** activity on their own account. Annual turnover within the ceilings above. Registered in the **RNAE** and holding the AE card. A person may combine activities (e.g. commerce + services) **provided each branch stays under its own ceiling** and **neither branch exceeds its limit** — see §3 for the combined-activity test.  _(Loi 114-13)_

### Excluded activities (professions réglementées and others)

- **Excluded activities** — The AE status is **not available** to **regulated/liberal professions** and a list of other activities, including (non-exhaustive — confirm against the regulatory list): - **Liberal professions:** lawyers (avocats), notaries (notaires), doctors and health professionals (médecins, dentistes, pharmaciens), chartered accountants / experts-comptables, architects, engineers in regulated practice, court officers (huissiers, adouls), etc. - **Financial / insurance** intermediation. - **Real-estate development** (promotion immobilière). - **Regulated transport** operators. - Activities subject to **special licensing or excise** (e.g. tobacco, alcohol). > **Default rule:** if there is *any* doubt that the activity is a regulated profession, treat it as **excluded** and route the user to `ma-cpu` (Contribution Professionnelle Unique) or `ma-income-tax` (régime du résultat net simplifié / réel). Do **not** assert eligibility for a borderline profession.

## 3. Rates & Computation

### Turnover bands and liberatory IR

**Turnover bands and liberatory IR**

| Activity | Annual ceiling | IR rate on collected turnover |
| --- | --- | --- |
| Commercial / industrial / artisanal | MAD 500,000 *(verify)* | **0.5%** *(verify)* |
| Services (prestations de services) | MAD 200,000 *(verify)* | **1%** *(verify)* |

- **Libératoire tax treatment** — Tax is a flat percentage of **turnover actually collected** during the period — **no expense deduction**. The tax is **libératoire**: it discharges the AE's income tax on that activity, so AE turnover is **not** re-entered on the progressive IR scale and **no annual global IR return** is filed for the AE activity.
- **IR libératoire formula** — IR libératoire = turnover collected in the quarter × rate (0.5% or 1%)

> Some sources reference a small **supplementary/professional duty** layered on top of the base rate in certain brackets. Treat any add-on as **"verify current value against the DGI auto-entrepreneur guide / Loi de Finances 2026"** before using it in a computation.

### Combined activities

- **Combined activities rule** — If a user runs both a commercial and a service branch, apply **each rate to its own turnover** and check **each branch against its own ceiling**. Breaching **either** ceiling triggers the exit rule in §5.

### The single-client > MAD 80,000 rule (anti-salary-disguise)

- **Single-client >80,000 withholding rule** — To stop employers re-labelling employees as auto-entrepreneurs, the law caps how much an AE may bill **one single client**: - For **services**, when annual revenue from **one client** exceeds **MAD 80,000**, the **excess above 80,000** is **not** taxed at the 1% liberatory rate. - Instead the **paying client withholds tax at source at 30%** *(verify rate — historically 30%, per CGI Art. 73)* on the excess, and this withholding is **liberatory** for that excess.  _(CGI Art. 73)_
- **Single-client withholding formula** — Taxed at 1% liberatory   = min(client revenue, 80,000) Subject to 30% withholding = max(client revenue − 80,000, 0) 30% withholding (by client) = max(client revenue − 80,000, 0) × 30%   (verify rate)

> Practical effect: an AE doing essentially full-time work for **one** company gets pushed toward an employee-like 30% rate on the excess. If a user's revenue is concentrated in one client, flag both the **tax** consequence and the **labour-law risk** of disguised employment (requalification en contrat de travail).

## 4. Social Cover (CNSS / AMO for Auto-Entrepreneurs)

Since **décret n° 2.21.477 (2021)** and the généralisation of **AMO** (Assurance Maladie Obligatoire) to non-salaried workers (**TNS**), CNSS affiliation is **mandatory** for every auto-entrepreneur.

### What it covers

- **CNSS/AMO coverage** — - **AMO** — mandatory health insurance: medical costs, hospitalisation, medicines, for the AE, spouse, and children. - **Basic retirement** (retraite de base). - **Daily allowances** for maternity / temporary incapacity, subject to contribution conditions.  _(décret n° 2.21.477 (2021))_

### How contributions are computed

- **CNSS contribution computation** — Contributions are **forfaitaires** (flat-rate by bracket), **based on declared turnover**, and **collected quarterly alongside the tax** through the AE portal. - The CNSS scheme uses **fixed brackets T1 to T8**; declared (annualised) turnover places the AE in a bracket, each with a **set contribution amount** *(verify the current T1–T8 amounts on cnss.ma / ae.gov.ma — not consistently published)*. - A **minimum** contribution applies even with **zero turnover** — historically **~MAD 300 / quarter (≈ MAD 1,200 / year)** *(verify current value)*. - Commonly cited bases: services ≈ **50% of turnover**, commercial ≈ **20% of turnover** used to set the bracket *(verify — methodology varies by source)*. > **Default:** when the exact bracket amount is unknown, quote the **minimum ~MAD 300/quarter** floor and tell the user the precise figure must be read off the **CNSS / ae.gov.ma** bracket table for their declared turnover. Do **not** invent a T1–T8 amount.

## 5. Registration & Filing / Payment Calendar

### Registration (RNAE)

- **RNAE registration steps** — 1. Apply on **`rn.ae.gov.ma`** (the RNAE portal, run by **Poste Maroc / Al Barid Bank**) or at a **Barid Bank** branch. 2. Provide CIN (national ID), activity, and address; registration is **free**. 3. Processing typically **7–15 days**; you receive the **auto-entrepreneur card** and a tax identifier. 4. CNSS affiliation is created alongside registration.

### Filing & payment (quarterly)

**Quarterly filing/payment calendar**

| Quarter | Period | Declare & pay by *(verify exact dates each year)* |
| --- | --- | --- |
| Q1 | Jan–Mar | end of **April** |
| Q2 | Apr–Jun | end of **July** |
| Q3 | Jul–Sep | end of **October** |
| Q4 | Oct–Dec | end of **January** (following year) |

- **Filing/payment rules** — Declaration and payment are **quarterly**, **online**, and **nil declarations (déclaration néant) are still required** when there is no turnover. Payment is online (carte bancaire, virement, réseaux agréés). The **CNSS contribution is collected at the same time** as the tax. > Missing a declaration (including a nil one) or a payment risks penalties and, ultimately, **radiation** from the RNAE. Confirm exact deadlines for 2026 on ae.gov.ma.

## 6. Worked Examples

> All figures use the 2026 rates/ceilings flagged "verify". Recompute with confirmed values before relying on them.

### Example 1 — Service freelancer, multiple clients

Sara is a freelance web developer (services). 2026 collected turnover **MAD 150,000**, spread across 5 clients (largest single client MAD 45,000).

- Within the services ceiling (200,000). Eligible.
- No client exceeds 80,000 → no 30% withholding.
- **IR = 150,000 × 1% = MAD 1,500** for the year.
- Plus CNSS quarterly contributions per her turnover bracket *(verify amount)*.

### Example 2 — Services with one dominant client (>80k rule)

Youssef does design work; 2026 turnover **MAD 120,000**, of which **MAD 100,000 from a single agency** and MAD 20,000 from others.

- Within ceiling (200,000). Eligible.
- Single client = 100,000 > 80,000 → excess = **20,000**.
  - First 80,000 from that client + the 20,000 from other clients = **100,000 at 1%** → **MAD 1,000**.
  - Excess **20,000 × 30% = MAD 6,000** withheld at source by the agency *(verify rate)*, liberatory on that slice.
- **Total tax ≈ MAD 7,000.** Flag the disguised-employment risk given the concentration.

### Example 3 — Commercial activity at the lower rate

Khadija resells handmade goods (commercial/artisanal). 2026 collected turnover **MAD 400,000**.

- Within commercial ceiling (500,000). Eligible.
- **IR = 400,000 × 0.5% = MAD 2,000** for the year.
- Plus CNSS quarterly contributions per bracket *(verify)*.

### Example 4 — Ceiling breach → exit

Omar (services) collects **MAD 230,000** in 2026, exceeding the 200,000 services ceiling.

- One year over is **tolerated**; the AE is generally **radiated only if the ceiling is exceeded two consecutive years** *(verify the current grace rule)*.
- On exit, Omar moves to **`ma-cpu` (CPU)** or the **`ma-income-tax`** régimes (résultat net simplifié / réel) and ordinary IR/TVA obligations may begin.
- Action: model the post-exit position with `ma-cpu` and `ma-income-tax` and advise on TVA registration thresholds.

## 7. Tier 2 — Reviewer Judgement Required

Escalate to the **Moroccan expert-comptable** reviewer when:

- **Single-client concentration** suggests **disguised employment** (labour-law requalification risk beyond the 30% tax point).
- **Ceiling breach** in the current or prior year — exit mechanics, CPU vs net-income routing, and TVA registration.
- **Borderline excluded activity** (possible regulated profession) — eligibility call.
- **Combined activities** straddling both ceilings.
- **CNSS bracket / AMO** entitlement disputes or arrears.
- **VAT (TVA)** interaction — AE turnover is generally outside ordinary TVA, but confirm against the TVA thresholds (see `morocco-vat`) if activity is borderline.
- Any client-specific number where the agent had to fall back to a "verify" value.

The agent must **never** present these as settled; it presents the computation, the assumptions, and the open items for the reviewer to sign off.

## 8. Reference

### Legal references

- **Legal references** — - **Loi n° 114-13** relative au statut de l'auto-entrepreneur (19 February 2015). - **Code Général des Impôts (CGI)** — Art. **42 bis, 42 ter** (regime & conditions), **43, 44-II** (turnover ceilings / base), **73-III** (rates, including the single-client withholding). - **Décret n° 2.21.477 (2021)** — mandatory CNSS / AMO affiliation for auto-entrepreneurs (généralisation AMO to TNS). - **Loi de Finances 2026** — confirm current rates, ceilings, and any add-on duty; **2025 IR reform context:** the ordinary IR scale was reformed (exempt band raised to **MAD 40,000**, top rate reduced to **37%**), which is the fallback regime if an AE exits. - Authority: **Direction Générale des Impôts (DGI)** — tax.gov.ma. Register: **RNAE** — rn.ae.gov.ma (Poste Maroc / Al Barid Bank). Social: **CNSS** — cnss.ma.  _(Loi n° 114-13; CGI Art. 42 bis, 42 ter, 43, 44-II, 73-III; Décret n° 2.21.477 (2021); Loi de Finances 2026)_

### Short test suite

1. **Q:** Service freelancer, MAD 90,000 turnover, no client over 80k. **A:** IR = 90,000 × 1% = **MAD 900**; within ceiling; CNSS per bracket.
2. **Q:** Commercial AE, MAD 600,000 turnover. **A:** **Ceiling breached** (>500,000) — flag exit, route to `ma-cpu` / `ma-income-tax`.
3. **Q:** Services AE, single client pays MAD 130,000. **A:** 80,000 at 1% (MAD 800); **50,000 × 30% = MAD 15,000** withheld by client *(verify rate)*; flag disguised-employment risk.
4. **Q:** Doctor wants AE status. **A:** **Excluded** (regulated profession) — route to `ma-income-tax`.
5. **Q:** Zero turnover this quarter. **A:** Still file a **déclaration néant**; **minimum CNSS** (~MAD 300/quarter, verify) still due.
6. **Q:** Activity mix not stated. **A:** Default to **services / 1%** and the 200,000 ceiling until confirmed.

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** confirm eligibility for any **regulated/liberal profession** (lawyer, doctor, notary, expert-comptable, architect, etc.) — default to **excluded**. - **Do NOT** apply the AE liberatory rates to turnover **above a ceiling** — once breached, the regime no longer applies; route to `ma-cpu` / `ma-income-tax`. - **Do NOT** ignore the **single-client > MAD 80,000** rule for services — apply the 30% withholding on the excess *(verify rate)* and flag disguised-employment risk. - **Do NOT** deduct business expenses — the base is **turnover collected**, gross. - **Do NOT** invent CNSS **T1–T8** bracket amounts — quote the minimum floor and send the user to cnss.ma / ae.gov.ma for the exact figure. - **Do NOT** state any rate, ceiling, or deadline as final without the **"verify current value"** caveat against the **Loi de Finances 2026** and the DGI. - **Do NOT** advise on **TVA**, employees/payroll, multi-state, or company forms (SARL/SA) under this skill — route to the relevant skill. - **Do NOT** issue a return as filed without **expert-comptable** sign-off.

## Disclaimer

This skill is **research-verified** against public sources (DGI / tax.gov.ma, the auto-entrepreneur portal ae.gov.ma, PwC Worldwide Tax Summaries, and reporting on the Loi de Finances 2025/2026) as of **May 2026**. It is **YMYL** content and is **pending sign-off by a Moroccan accountant (expert-comptable)**. Rates, ceilings, CNSS bracket amounts, and deadlines change with each Loi de Finances and must be **re-verified** before use. Nothing here is a substitute for advice from a licensed Moroccan expert-comptable or the DGI. Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
