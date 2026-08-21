---
name: ma-formation
description: Use this skill whenever asked about registering or forming a business in Morocco as a self-employed person — choosing and obtaining a legal status, the identifiers every business needs, and the tax regime picked at registration. Trigger on phrases like "register auto-entrepreneur Morocco", "créer auto-entrepreneur", "comment s'inscrire auto-entrepreneur Maroc", "ICE Maroc", "obtenir un IF", "Registre de Commerce Maroc", "start business Morocco", "créer une SARL Maroc", "patente / taxe professionnelle", "كيفاش نسجل مقاول ذاتي", "تسجيل شركة المغرب". Covers RNAE auto-entrepreneur registration (ae.gov.ma / Poste Maroc), obtaining the ICE, the IF (Identifiant Fiscal) from the DGI, the RC (Registre de Commerce), the taxe professionnelle (ex-patente) and its new-business exemption, regulated professions, choosing the regime (auto-entrepreneur vs CPU vs RNR/RNS), VAT registration, and forming a SARL / SARL-AU via the CRI / OMPIC, with timing and cost. Reply in the user's language (English, French, or Moroccan Arabic / Darija) and keep the native terms. Cross-reference ma-auto-entrepreneur, ma-cpu, ma-income-tax, and morocco-vat for the downstream tax detail.
version: 1.0
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Formation

## Morocco — Business Formation & Registration for the Self-Employed

This skill walks a self-employed person through **starting and registering** a business in Morocco: which legal status to adopt (**auto-entrepreneur**, a sole trader under **CPU / RNR / RNS**, or a one-person company **SARL-AU**), and which identifiers and tax registrations follow. The four identifiers that recur across every Moroccan business are:

- **ICE** — *Identifiant Commun de l'Entreprise* — a 15-digit universal business ID used by all administrations (DGI, CNSS, OMPIC, customs).
- **IF** — *Identifiant Fiscal* — the tax identifier issued by the **DGI**.
- **RC** — *Registre de Commerce* — commercial-register number (commerçants only).
- **TP** — *taxe professionnelle*, the local business tax formerly called the **patente**.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (auto-entrepreneur, ICE, IF, RC, patente, CRI, OMPIC, DGI, CNSS) and explain them in the chosen language. It is a **formation / registration** skill; for ongoing tax computation route to `ma-auto-entrepreneur`, `ma-cpu`, `ma-income-tax`, `morocco-vat`, and `ma-social-contributions`.

## 1. Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Topic | Business formation & registration for the self-employed |
| Currency | **MAD** (dirham marocain, DH) |
| Authority — tax | **Direction Générale des Impôts (DGI)** — tax.gov.ma |
| Authority — companies / IP | **OMPIC** (ompic.ma) via the **CRI** (regional one-stop window) |
| Authority — auto-entrepreneur | **RNAE** — Registre National de l'Auto-Entrepreneur, via Poste Maroc / Al Barid Bank — `rn.ae.gov.ma` (a.k.a. ae.gov.ma) |
| Authority — social | **CNSS** (cnss.ma) |
| ICE | 15 digits; auto-attributed by **OMPIC** (companies) or **DGI** (individuals); recoverable at `ice.gov.ma` *(verify)* |
| RNAE registration cost | **Free** (no fee) *(verify)* |
| RNAE AE-number issuance | ~**24–72 h** after the dossier is filed at Poste Maroc / Al Barid Bank *(verify)* |
| AE turnover ceiling — commercial / industrial / artisanal | **MAD 500,000 / year** *(verify)* |
| AE turnover ceiling — services | **MAD 200,000 / year** *(verify)* |
| Taxe professionnelle — new-business exemption | **5 years** from start of activity, automatic *(verify)* |
| Taxe professionnelle — rate band | ~**10%–30%** of rental value of premises/assets, after the 5-year window *(verify)* |
| VAT (TVA) franchise / threshold — commercial-industrial-artisanal | **MAD 500,000** turnover *(verify CGI Art. 91)* |
| VAT (TVA) franchise / threshold — services | **MAD 200,000** turnover *(verify)* |
| VAT status of companies (SARL/SA) | **Subject to VAT from creation** regardless of turnover *(verify)* |
| SARL / SARL-AU minimum capital | **No legal minimum** since Loi 24-10 (often MAD 10,000–50,000 in practice) *(verify)* |
| SARL capital blocking | ≤ MAD 100,000 → no blocking; > MAD 100,000 → deposit ≥ 1/4 in a blocked account *(verify)* |
| SARL formation cost | ~**MAD 5,000–15,000** excl. capital (notary/legal fees vary) *(verify)* |
| SARL formation timing (CRI guichet unique) | ~**10–15 working days** *(verify)* |
| Primary legislation | Loi 114-13 (AE); Loi 15-95 Code de Commerce (RC); Loi 47-06 / 07-20 (local taxes, TP); Loi 5-96 & 24-10 (SARL); CGI; Loi de Finances 2026 |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Version | 1.0 |
| Last research update | May 2026 |

### Conservative defaults

When data is missing or ambiguous, apply the **conservative default** and flag it for the reviewer:

- **Activity type unknown** → ask whether the activity is **commercial** (commerçant → needs **RC**) or a **prestation de services / profession libérale** (often no RC, but still needs **IF + ICE + TP**).
- **Profession possibly regulated** → assume it **needs prior authorisation / ordre professionnel** and is **excluded** from auto-entrepreneur until proven otherwise.
- **Regime not chosen** → do **not** auto-select; lay out auto-entrepreneur vs CPU vs RNR/RNS and route the tax detail to the dedicated skill.
- **Near a ceiling** (AE/CPU/VAT) → assume the ceiling **is or will be breached** and warn about the consequences (exit, VAT registration).
- **Any rate, threshold, fee, or deadline** → present as *indicative* and append **"verify against the Loi de Finances 2026 and the DGI / OMPIC"**.

## 2. Registering as an Auto-Entrepreneur (statut de l'auto-entrepreneur)

The **auto-entrepreneur (AE)** status (Loi 114-13) is the lightest path for an individual freelancer or micro-trader. Registration is through the **RNAE** (Registre National de l'Auto-Entrepreneur), operated by **Poste Maroc / Al Barid Bank** on the portal **`rn.ae.gov.ma`** (commonly written **ae.gov.ma**).

**Who can use it.** A physical person whose annual turnover stays under **MAD 500,000** (commercial/industrial/artisanal) or **MAD 200,000** (services), and whose activity is **not on the excluded list** of regulated/liberal professions *(verify list)*.

**Steps.**

1. **Create an account** on `rn.ae.gov.ma` (CIN/national-ID based).
2. **Fill the online form** — identity, activity (with its code), and the commune/address. Takes ~15–30 minutes.
3. **Upload / prepare documents** — typically CIN, a photo, and proof of address *(verify the current checklist on the portal)*.
4. **File the dossier physically** at a **Poste Maroc / Al Barid Bank** branch (or sometimes a CRI) to validate it.
5. **Receive the AE registration number** (carte d'auto-entrepreneur) — usually within **24–72 hours** *(verify)*. **Registration is free** *(verify)*.
6. **Automatic CNSS affiliation** — since 2021, RNAE registration triggers affiliation to the CNSS non-salarié (AMO) scheme. See `ma-social-contributions`.

**What you get.** An AE number that doubles as your business identity; you obtain an **ICE** and an **IF** in the process (the AE is in the DGI system). You generally do **not** need a full **RC** registration as an auto-entrepreneur *(verify for commercial activities)*.

**Tax under AE.** Liberatory IR on **collected** turnover — **0.5%** (commercial/industrial/artisanal) or **1%** (services). Full detail and the single-client anti-disguised-salary rule live in **`ma-auto-entrepreneur`**.

> Route all AE tax computation, ceiling-breach handling, and the 80,000-MAD single-client withholding to **`ma-auto-entrepreneur`** — this skill only covers the *registration*.

- **AE liberatory IR rate — commercial/industrial/artisanal** — 0.5% percent of collected turnover  _(ma-auto-entrepreneur)_
- **AE liberatory IR rate — services** — 1% percent of collected turnover  _(ma-auto-entrepreneur)_

## 3. ICE / IF / RC / Taxe Professionnelle

These are the core identifiers and the first local tax. For a **company**, the CRI one-stop window produces them together; for an **individual**, they come from the DGI (and the RC tribunal where the activity is commercial).

### 3.1 ICE — Identifiant Commun de l'Entreprise

- **ICE** — A **15-digit** universal ID (9 entity digits + 4 establishment digits + 2 control digits) used by **all** administrations. Mandatory on invoices. - **New company** → ICE is **attributed by OMPIC** when you request the *certificat négatif* (name reservation). - **New individual / sole trader** → **DGI** attributes the ICE and prints it on the **bulletin IF / TP**. - **Existing business** without an ICE → recover/generate it at **`ice.gov.ma`** using your IF, RC, or CNSS number; a PDF certificate is produced *(verify)*.

### 3.2 IF — Identifiant Fiscal

- **IF** — The tax identifier issued by the **DGI** (Direction Générale des Impôts). Obtained at registration with the DGI tax office of the activity's location, or automatically through the **CRI** for a company. Required for IR/IS, VAT, and to invoice.

### 3.3 RC — Registre de Commerce

- **RC** — The **commercial register**, kept by the **Tribunal de Commerce**, governed by the **Code de Commerce (Loi 15-95)**. - **Required for commerçants** (commercial/industrial activities). Many pure **prestataires de services / professions libérales** and **auto-entrepreneurs** do **not** register in the RC *(verify per activity)*. - Two forms: **RC analytique** (the local court's number) and the **RC central** kept by **OMPIC**.  _(Loi 15-95)_

### 3.4 Taxe professionnelle (ex-patente)

- **Taxe professionnelle (TP)** — The **taxe professionnelle (TP)** — historically the **patente** — is a **local tax** on those carrying on a profession/business (Loi 47-06 on local taxation). - **Base:** the **rental value** of premises and business fixed assets; **rate band ~10%–30%** *(verify)*. - **New-business exemption:** **5 years** of full exemption from the start of activity, applied **automatically** *(verify)* — a key reason new businesses owe little local tax at the outset. - Paid alongside the **taxe de services communaux (TSC)**. - Note: **CPU** taxpayers and (effectively) **auto-entrepreneurs** are **exempt / outside** the TP under their own regimes — see Section 4 and `ma-cpu`.  _(Loi 47-06)_

## 4. Choosing the Regime at Registration + VAT

The status you register under determines which **income-tax regime** applies. Lay out the options; do **not** auto-pick.

### 4.1 The four routes

**The four routes table**

| Route | Who | Tax base | Note |
| --- | --- | --- | --- |
| **Auto-entrepreneur** | Individual under the AE ceilings, non-excluded activity | **0.5% / 1%** liberatory on **collected** turnover | Lightest; CNSS bundled. → `ma-auto-entrepreneur` |
| **CPU** (Contribution Professionnelle Unique) | Individual, turnover ≤ **MAD 500,000** (comm./ind./artisanal) or ≤ **200,000** (services), not on excluded list | **10%** on **turnover × profession coefficient** + droit complémentaire | Replaces forfait; **exempt from TP & TSC**. → `ma-cpu` |
| **RNR** (Résultat Net Réel) | Higher turnover or by election | **Net profit**, progressive IR scale | Full accounting. → `ma-income-tax` |
| **RNS** (Résultat Net Simplifié) | Mid-range turnover | Simplified net profit, progressive IR | → `ma-income-tax` |

**Decision pointers.**
- Very small, expense-light freelancing → **auto-entrepreneur** is usually simplest.
- Small trade/craft with a known profession coefficient → compare **CPU**.
- Significant expenses, or activity excluded from AE/CPU, or above ceilings → **RNR / RNS**.
- A **regulated / liberal profession** (doctor, lawyer, architect, notaire, accountant, etc.) is generally **excluded from AE and CPU** and needs its **ordre professionnel / authorisation** — route to `ma-income-tax`.

### 4.2 Regulated professions & authorisations

- **Regulated professions default** — Before registering, confirm the activity does not require **prior authorisation** or membership of an **ordre / syndicat professionnel** (e.g. health, legal, accounting, engineering, transport, food handling). If it might, **default to "needs authorisation"** and flag it — the legal status cannot be finalised until the profession's own licence is obtained.

### 4.3 VAT (TVA) registration

- **VAT registration rules** — - **Auto-entrepreneurs / CPU** small operators are typically **outside VAT** under the franchise thresholds — **MAD 500,000** (comm./ind./artisanal) / **MAD 200,000** (services) of turnover *(verify CGI)*. - **Above the threshold**, or for **companies (SARL/SA) from creation**, VAT applies — standard rate **20%**, with reduced rates (e.g. 10%, 0% on exports) *(verify the 2026 rate convergence)*. - VAT registration is part of the DGI/IF process; declarations are **monthly** or **quarterly** via **SIMPL-TVA**. Detail lives in **`morocco-vat`**.  _(verify CGI)_

## 5. SARL / SARL-AU Overview (CRI / OMPIC)

A self-employed person who wants **limited liability** or to scale beyond the individual regimes usually forms a **SARL** (multi-partner) or **SARL-AU** / **SARL-associé unique** (one-person LLC, the Moroccan EURL). Companies are formed through the **CRI guichet unique** (regional one-stop window) with **OMPIC**.

**Typical steps (CRI single window).**

1. **Certificat négatif** — reserve the company name with **OMPIC** (small fee, ~MAD 230) *(verify)*. The **ICE** is attributed here.
2. **Draft the statuts** (articles of association); notarised or under private signature.
3. **Deposit capital** — **no legal minimum** since Loi 24-10; if capital **> MAD 100,000**, block **≥ 1/4** in a bank account in the company-in-formation's name *(verify)*.
4. **Register at the CRI** — RC registration (Tribunal de Commerce), IF (DGI), TP, and CNSS affiliation are processed together.
5. **Legal publications** — Bulletin Officiel + a journal d'annonces légales *(fees vary)*.

**Indicative cost & timing.** ~**MAD 5,000–15,000** excluding capital; ~**10–15 working days** via the CRI one-stop window *(verify — varies by region and adviser)*.

**Tax of a SARL/SARL-AU.** A company is generally subject to **corporate income tax (IS)**, not the individual IR regimes, and is **VAT-registered from creation**. That shifts the engagement out of the self-employed individual scope — flag that company taxation (IS) is **outside this skill set** and needs an **expert-comptable**.

## 6. Worked Examples

### Example 1 — Freelance graphic designer, Casablanca

- **Facts:** Individual, services, expects ~MAD 120,000/year, no employees, no shop.
- **Status:** Eligible for **auto-entrepreneur** (under the 200,000 services ceiling; design is not a regulated profession — *verify*).
- **Steps:** Register on **`rn.ae.gov.ma`** → file dossier at Poste Maroc → AE number in ~24–72 h (free). Obtains **ICE + IF** via the RNAE/DGI; CNSS affiliation automatic.
- **Tax:** **1%** liberatory IR on collected turnover (→ `ma-auto-entrepreneur`).
- **VAT:** **Below MAD 200,000** → outside VAT *(verify)*.
- **TP:** Effectively outside the patente under the AE regime.
- **Flag:** Confirm the activity is not on the AE excluded list; verify all figures against the Loi de Finances 2026.

### Example 2 — Two partners opening an e-commerce trading company

- **Facts:** Two associés, expected turnover ~MAD 1,500,000, want limited liability.
- **Status:** **SARL** via the **CRI guichet unique**.
- **Steps:** Certificat négatif at OMPIC (ICE attributed) → statuts → no minimum capital but plan working capital → RC + IF + TP + CNSS at the CRI → legal publications. ~10–15 working days; ~MAD 5,000–15,000 excl. capital *(verify)*.
- **Tax:** Corporate **IS** + **VAT from creation** (turnover well above 500,000) → **outside this skill** — route to an expert-comptable and `morocco-vat`.
- **TP:** **5-year new-business exemption** applies automatically, then the ~10%–30% band on rental value *(verify)*.
- **Flag:** Company taxation is out of scope here; confirm all costs/timing with the CRI and an expert-comptable.

## 7. Reference + Test Suite

### Sources

- **Loi n° 114-13** — statut de l'auto-entrepreneur; **RNAE** portal `rn.ae.gov.ma` (Poste Maroc / Al Barid Bank).
- **OMPIC** (ompic.ma) — *certificat négatif*, ICE attribution for companies, RC central. **`ice.gov.ma`** — ICE recovery platform.
- **Code de Commerce (Loi 15-95)** — Registre de Commerce.
- **Loi 47-06** (and **Loi 07-20**) — fiscalité locale: **taxe professionnelle** (ex-patente), **TSC**, and the **5-year** new-business TP exemption.
- **Loi 5-96** (sociétés) and **Loi 24-10** — SARL / SARL-AU, removal of minimum capital; **CRI** guichet unique.
- **CGI** — IR regimes (AE / CPU / RNR / RNS), **VAT thresholds & rates**.
- **Loi de Finances 2026** and **Note Circulaire DGI** — current ceilings, rates, thresholds, and the VAT-rate convergence.
- Cross-references: **PwC Worldwide Tax Summaries (Morocco)**, **Baker Tilly Morocco** (CPU), **mcinet.gov.ma** (self-employment).
- Authorities: **DGI** (tax.gov.ma / SIMPL), **OMPIC**, **CRI**, **CNSS**.

### Short test suite

1. **Q:** Web freelancer, services, CA ~MAD 90,000, wants the simplest setup. **A:** **Auto-entrepreneur** via `rn.ae.gov.ma` (free, ~24–72 h); ICE+IF obtained; outside VAT; → `ma-auto-entrepreneur`.
2. **Q:** "What is the ICE and how many digits?" **A:** *Identifiant Commun de l'Entreprise*, **15 digits**, universal across administrations; from **OMPIC** (companies) or **DGI** (individuals); recover at `ice.gov.ma`.
3. **Q:** Pure services provider — do they need an RC? **A:** **Often no** — RC is for **commerçants**; services/professions libérales usually skip RC but still need **IF + ICE + TP** *(verify per activity)*.
4. **Q:** "How long is the patente exemption for a new business?" **A:** **5 years** from start of activity, automatic (taxe professionnelle) *(verify)*.
5. **Q:** Lawyer wants to register as auto-entrepreneur. **A:** **Excluded** (regulated/liberal profession needs the ordre); route to `ma-income-tax`.
6. **Q:** SARL minimum capital? **A:** **No legal minimum** since Loi 24-10; blocking only if capital **> MAD 100,000** *(verify)*.
7. **Q:** Activity commercial vs services unknown. **A:** **Ask** — it changes RC requirement, the AE/CPU ceiling (500k vs 200k), and the VAT threshold.
8. **Q:** Trader expects CA MAD 1.2M. **A:** Over AE/CPU ceilings → **RNR/RNS** (or SARL); **VAT applies** — route to `ma-income-tax` + `morocco-vat`.

## PROHIBITIONS

- **Prohibitions list** — - **Do NOT** auto-select a **legal status or tax regime** — present auto-entrepreneur vs CPU vs RNR/RNS vs SARL and let the user choose; the choice drives RC, VAT, and TP outcomes. - **Do NOT** confirm a **regulated / liberal profession** as eligible for auto-entrepreneur or CPU — **default to excluded / needs authorisation** and route to `ma-income-tax`. - **Do NOT** state any **fee, ceiling, threshold, rate, or processing time** as final — they change with the Loi de Finances and by region; append **"verify against the Loi de Finances 2026 and the DGI / OMPIC / CRI"**. - **Do NOT** assume a **services** provider needs an **RC** — RC is for **commerçants**; verify per activity. - **Do NOT** claim a business is **outside VAT** without checking the activity-type threshold (500,000 vs 200,000) — and remember **companies are VAT-liable from creation**. - **Do NOT** invent the **AE/CPU excluded-professions list** or a **profession coefficient** — read them from the official RNAE list / CGI annex. - **Do NOT** compute **corporate tax (IS)** or full company tax under this skill — flag it as out of scope and route to an expert-comptable. - **Do NOT** provide **AE / CPU / VAT / income-tax computation** here — route to `ma-auto-entrepreneur`, `ma-cpu`, `morocco-vat`, `ma-income-tax`, and `ma-social-contributions`. - **Do NOT** treat this skill's output as a **filed registration** — final registration and any tax position require **Moroccan expert-comptable** sign-off.

## Disclaimer

This skill is **research-verified** against public sources — the **DGI** (tax.gov.ma), **OMPIC** (ompic.ma) and `ice.gov.ma`, the **RNAE** portal (`rn.ae.gov.ma` / Poste Maroc), **CRI** guidance, **PwC Worldwide Tax Summaries** (Morocco), and reporting on the **Loi de Finances 2025/2026** — as of **May 2026**. It is **YMYL** content and is **pending sign-off by a Moroccan accountant (expert-comptable)**. Registration procedures, identifiers, fees, ceilings, rates, exemptions, and deadlines change with each Loi de Finances and by region and must be **re-verified** before use. Nothing here is a substitute for advice from a licensed Moroccan expert-comptable, the DGI, OMPIC, or your CRI. Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
