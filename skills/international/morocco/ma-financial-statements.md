---
name: ma-financial-statements
description: "Use this skill whenever asked about financial statements, statutory accounts, or financial reporting obligations for self-employed people and small businesses in Morocco — who has to prepare formal accounts and who does not, the CGNC framework, the components of the états de synthèse (Bilan, CPC, ESG, Tableau de financement, ETIC), the normal vs simplified model, when IFRS applies, how accounts are filed with the DGI and deposited at the commercial court (dépôt légal), and when a statutory auditor (commissaire aux comptes) is required. Trigger on phrases like \"Morocco financial statements\", \"états de synthèse\", \"bilan CPC Maroc\", \"do I file accounts Morocco\", \"comptes annuels Maroc\", \"CGNC états de synthèse\", \"tableau de financement\", \"ETIC\", \"commissaire aux comptes Maroc\", \"dépôt des comptes Maroc\", \"القوائم المالية المغرب\", \"الميزانية المغرب\". Frame for a self-employed reader: auto-entrepreneur and CPU taxpayers do NOT prepare formal financial statements (they keep simple registers — cross-ref ma-bookkeeping); résultat net réel (RNR) taxpayers and companies prepare the full états de synthèse under the CGNC, and résultat net simplifié (RNS) prepares a reduced set. Reply in the user's language (English, French, or Moroccan Arabic / Darija). Cross-reference ma-bookkeeping, ma-income-tax, ma-cpu, and ma-auto-entrepreneur."
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

# MA Financial Statements

## Morocco — Financial Statements & Financial Reporting (États de Synthèse)

This skill tells an AI agent **who has to prepare formal financial statements** in Morocco, **what those statements are**, and **how they are filed** — organised by tax regime and legal form. It does **not** compute the tax (that is `ma-income-tax`, `ma-cpu`, `ma-auto-entrepreneur`) and it does **not** govern the underlying books and invoices (that is `ma-bookkeeping`). It governs the **output** of the accounting system: the **états de synthèse** under the **Code Général de Normalisation Comptable (CGNC)**.

The central message for a self-employed reader:

- **Auto-entrepreneur (AE)** and **Contribution Professionnelle Unique (CPU)** taxpayers do **NOT** prepare formal financial statements. They keep **simple registers** (registre des recettes / registre des recettes et des achats — see `ma-bookkeeping`). No bilan, no CPC.
- **Résultat Net Réel (RNR)** taxpayers and **companies (SARL, SA, etc.)** prepare the **full états de synthèse** under the CGNC.
- **Résultat Net Simplifié (RNS)** prepares a **reduced set** of statements.

This skill replies in the user's language. Moroccan users mix English, French, and Darija — keep the native terms (CGNC, états de synthèse, bilan, CPC, ESG, tableau de financement, ETIC, commissaire aux comptes, dépôt légal, DGI) and explain them in the user's chosen language.

## 1. Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Morocco (MA) |
| Scope | Financial statements / financial reporting obligations by regime and legal form |
| Currency | MAD (dirham marocain, DH) |
| Authority | **Direction Générale des Impôts (DGI)** — tax.gov.ma (filing with the tax return); **greffe du tribunal de commerce** (dépôt légal) |
| Standards | **CGNC** (Code Général de Normalisation Comptable) for statutory/individual accounts; **IFRS** for banks/insurers and (optionally) listed groups — consolidated accounts only |
| Accounting law | **Loi 9-88** on accounting obligations of traders (dahir 25 Dec 1992); **Code de Commerce** |
| Who prepares full états de synthèse | **RNR** taxpayers + **companies** (SARL, SA, SNC, SCS…) |
| Who prepares a reduced set | **RNS** taxpayers (simplified presentation) *(verify the exact reduced set)* |
| Who prepares NONE | **Auto-entrepreneur** and **CPU** — registers only (see `ma-bookkeeping`) |
| États de synthèse — modèle normal | **5 components**: **Bilan**, **CPC**, **ESG**, **Tableau de financement (TF)**, **ETIC** — for turnover ≥ **MAD 10,000,000** *(verify threshold)* |
| États de synthèse — modèle simplifié | **Reduced set** (Bilan + CPC at minimum; ESG dropped) — for turnover < **MAD 10,000,000** *(verify exact components — sources disagree)* |
| Filing with DGI | États de synthèse **attached to the annual IS/IR return** via **SIMPL** (SIMPL-IS / SIMPL-IR), filed electronically |
| IS return deadline | Within **3 months** of financial year-end (e.g. **31 March** for a calendar-year close) *(verify)* |
| Dépôt légal (commercial court) | Companies deposit états de synthèse at the **greffe du tribunal de commerce** within **30 days** of approval by the assemblée générale, now via electronic platform *(verify)* |
| Audit (commissaire aux comptes) | **Mandatory for all SA**; **SARL and others when turnover > MAD 50,000,000 (HT)** *(verify)* |
| Non-dépôt penalty | Fine reported at **MAD 10,000–50,000** for failure to deposit at the court *(verify amount and article)* |
| Contributor | Open Accountants Community |
| Quality tier | **Research-verified — pending sign-off by a Moroccan accountant (expert-comptable)** |
| Version | 1.0 |
| Last research update | May 2026 |

### Conservative defaults

When the regime, legal form, turnover, or threshold is missing or ambiguous, the agent applies the **conservative default** and flags it for the reviewer:

- **Regime/form unknown** → assume the taxpayer **must prepare full états de synthèse under the CGNC** until AE/CPU status is confirmed; never tell someone they are exempt from accounts without confirming the regime.
- **AE/CPU confirmed** → confirm they prepare **no formal financial statements** (registers only) and route the books question to `ma-bookkeeping`.
- **Turnover near the MAD 10,000,000 line** → assume the **modèle normal (5 statements)** applies, not the simplified model.
- **Turnover near the MAD 50,000,000 line** (non-SA) → assume a **commissaire aux comptes is required** and warn the user to engage one.
- **Any figure marked *(verify)*** → present as provisional; the reviewer confirms against the current CGNC / CGI / Loi de Finances 2026 / Code de Commerce before relying on it.

## 2. Who Prepares What

Match the taxpayer to a row first. The obligation scales sharply with regime and legal form.

**Who Prepares What**

| Taxpayer | Formal financial statements? | What they produce | Frame |
| --- | --- | --- | --- |
| **Auto-entrepreneur (AE)** | **No** | Register of receipts only (see `ma-bookkeeping`) | Tax is libératoire on collected turnover; no bilan, no CPC |
| **CPU** | **No** | Register of receipts **and** purchases + vouchers | Exempt from CGNC états de synthèse |
| **RNS (résultat net simplifié)** | **Reduced** | Simplified états de synthèse | Full bookkeeping foundation, abbreviated statements |
| **RNR (résultat net réel)** | **Yes — full** | Complete états de synthèse (CGNC) | Same obligation as a company on the reporting side |
| **Company (SARL, SA, …)** | **Yes — full** | Complete états de synthèse (CGNC); IFRS if bank/insurer/listed group | Plus dépôt légal and possibly audit |

### 2.1 What changes as a self-employed person grows

This is the core narrative for the reader:

1. **Start as auto-entrepreneur** → keep a **register of receipts**. You do **not** prepare or file any financial statements. Your tax is computed on collected turnover (see `ma-auto-entrepreneur`).
2. **CPU** → keep a **register of receipts and purchases**. Still **no** formal financial statements.
3. **Move to RNR** (by option, or because the turnover ceiling was exceeded for two consecutive years — verify in `ma-income-tax` / `ma-cpu`) → you now prepare the **full états de synthèse under the CGNC** every year and attach them to your **IR return** via SIMPL-IR. This is a large step up in obligation.
4. **Incorporate (e.g. SARL)** → the company prepares **full états de synthèse**, attaches them to the **IS return** via SIMPL-IS, **deposits** them at the **greffe du tribunal de commerce** (dépôt légal), and appoints a **commissaire aux comptes** if it is an SA or if turnover exceeds **MAD 50,000,000 HT**.

> The agent must not let the reader assume incorporation is "the same as freelancing with a logo". Incorporation brings **published accounts, dépôt légal, and possible statutory audit** — all absent for AE/CPU.

## 3. The États de Synthèse (CGNC Components)

The **CGNC** (Code Général de Normalisation Comptable) is Morocco's accounting framework. It offers **two models** depending on size; the components below are the **modèle normal** set.

The five états de synthèse form **an inseparable whole** (un tout indissociable):

### 3.1 Bilan (balance sheet)

- **Bilan** — The **patrimonial situation** at the closing date: **actif** (assets) on one side, **passif** (equity + liabilities) on the other. Structured by the CGNC masses: **actif immobilisé / actif circulant / trésorerie** and **financement permanent / passif circulant / trésorerie passif**.  _(CGNC)_

### 3.2 CPC — Compte de Produits et Charges (income statement)

- **CPC** — The **profit-and-loss** statement: **produits** (revenues) and **charges** (expenses) for the period, split into **exploitation** (operating), **financier** (financial), and **non courant** (non-recurring). Produces the **résultat net** (net result) of the year.  _(CGNC)_

### 3.3 ESG — État des Soldes de Gestion (statement of management balances)

- **ESG** — Two cascading tables showing the **formation of the net result** (via the intermediate management balances — soldes intermédiaires de gestion) and the **capacité d'autofinancement (CAF)** — self-financing capacity. **Required in the modèle normal**; typically **dropped in the modèle simplifié**.  _(CGNC)_

### 3.4 Tableau de financement (TF) — financing statement

- **Tableau de financement (TF)** — Shows the **variation of resources and uses** over the year (emplois et ressources), i.e. how the business financed its investments and how working capital moved.  _(CGNC)_

### 3.5 ETIC — État des Informations Complémentaires (notes)

- **ETIC** — The **explanatory notes** that make the bilan and CPC understandable: accounting methods, detail of fixed assets and depreciation, debt maturity tables, provisions, commitments, and other disclosures required by the CGNC.  _(CGNC)_

### 3.6 Modèle normal vs modèle simplifié

**Modèle normal vs modèle simplifié**

|  | Modèle normal | Modèle simplifié |
| --- | --- | --- |
| Turnover trigger | **≥ MAD 10,000,000** *(verify)* | **< MAD 10,000,000** *(verify)* |
| Bilan | Yes | Yes |
| CPC | Yes | Yes |
| ESG | **Yes** | **No** (dropped) |
| Tableau de financement | Yes | *(verify — sources disagree whether it is required)* |
| ETIC | Yes (full) | Yes (abbreviated) *(verify)* |

> **Caution:** public secondary sources **disagree** on the exact component list of the **modèle simplifié** (some describe two statements, others four). The agent must present the simplified set as **to be confirmed** against the CGNC text and a Moroccan expert-comptable. The reliably distinguishing fact is that the **ESG is not required** in the simplified model.

### 3.7 IFRS — when it applies

- **Banks and credit institutions — mandatory IFRS** — mandatory IFRS for consolidated accounts, from periods beginning Jan 2008  _(Bank Al-Maghrib Circular 56/G/2007)_
- **Insurance and reinsurance companies** — IFRS required for their financial statements (reported from December 2022) *(verify scope)*
- **Listed groups (AMMC-regulated)** — an irrevocable option to use IFRS or local GAAP for consolidated accounts; most use IFRS in practice  _(AMMC)_

Morocco's **statutory / individual accounts are always prepared under the CGNC**. **IFRS** applies only to **consolidated accounts** of specific entities:

A **self-employed person or an ordinary SARL does not use IFRS** — they use the **CGNC**. Do not tell a freelancer or a small company to prepare IFRS statements.

## 4. Audit / Commissaire aux Comptes

- **Commissaire aux comptes (CAC)** — A **commissaire aux comptes (CAC)** is the **statutory auditor**, appointed to certify that the états de synthèse are **régulières et sincères**. This is distinct from the **expert-comptable** who prepares/reviews the accounts.
- **Société Anonyme (SA)** — always requires at least one commissaire aux comptes, regardless of turnover  _(Loi 17-95 (verify))_
- **SARL and other commercial companies — CAC threshold** — MAD 50,000,000 (HT) MAD (turnover at close of financial year exceeds this amount triggers mandatory CAC *(verify)*)  _(Loi 5-96 (verify))_
- **CAC on request** — a CAC may also be required by the company statutes, or at the request of partners holding a defined minority stake (reported as ≥ 1/10 of the capital for SARL) *(verify the exact percentage)*

When the appointment is **mandatory** *(verify against Loi 17-95 on SA and Loi 5-96 on SARL/others, as amended)*:

Other points:

- The mandate is typically **3 financial years**, renewable *(verify)*.
- The CAC must be enrolled with the **Ordre des Experts-Comptables**.
- **Auto-entrepreneur, CPU, RNS, and RNR individuals are not subject to statutory audit** — the CAC regime is a **company-law** obligation, not a personal-income-tax one. (RNR/RNS taxpayers may still engage an expert-comptable voluntarily.)

> The agent must not tell a sole proprietor (any regime) that they need a commissaire aux comptes. It applies to companies meeting the form/threshold tests above.

## 5. Worked Examples

### Example 1 — Freelance developer, auto-entrepreneur

- Activity: software services; turnover collected ≈ MAD 200,000/year.
- **Financial statements?** **None.** She keeps a **register of receipts** only (see `ma-bookkeeping`). No bilan, no CPC, no CGNC états de synthèse, no dépôt légal, no commissaire aux comptes.
- **Filing:** declares collected turnover under the AE channel (see `ma-auto-entrepreneur`); no financial statements are attached.
- Agent output: confirms **no formal accounts**, routes the records question to `ma-bookkeeping`, and flags that **if she moves to RNR or incorporates**, full états de synthèse under the CGNC begin.

### Example 2 — IT consultant who moved to RNR, then asks about incorporating

- Activity: consultancy; exceeded the service ceiling for two consecutive years, now taxed under **RNR**; turnover ≈ MAD 3,000,000.
- **As RNR (individual):** must prepare **full états de synthèse under the CGNC** (Bilan, CPC, ESG, TF, ETIC — modèle simplifié components likely apply below MAD 10,000,000, **verify**) and **attach them to the IR return** via **SIMPL-IR**. He may engage an **expert-comptable**, but a **commissaire aux comptes is not required** for an individual.
- **If he incorporates as a SARL:** the company prepares the **full états de synthèse**, attaches them to the **IS return** (SIMPL-IS), and performs **dépôt légal** at the greffe within **30 days** of the AG approval. A **CAC is not yet required** at MAD 3,000,000 turnover (below the MAD 50,000,000 line and not an SA) *(verify)*.
- Agent output: distinguishes **RNR-individual** vs **SARL** obligations, flags the modèle normal/simplifié threshold, and notes the **dépôt légal** that incorporation adds.

## 6. Reference + Test Suite

### Legal & source references

- **CGNC** — Code Général de Normalisation Comptable (the accounting framework and the five états de synthèse: Bilan, CPC, ESG, Tableau de financement, ETIC).
- **Loi 9-88** on the accounting obligations of traders (dahir 25 Dec 1992) — makes CGNC-compliant accounting mandatory.
- **Code de Commerce** — commercial books and obligations.
- **Loi 17-95** on the Société Anonyme — commissaire aux comptes for SA; dépôt légal.
- **Loi 5-96** on the SARL/SNC/SCS — CAC threshold (turnover > MAD 50,000,000 HT) and dépôt légal *(verify article/amendments)*.
- **CGI** (Code Général des Impôts) — états de synthèse attached to the IS/IR return; IS filing within 3 months of close; SIMPL teleservices *(verify articles)*.
- **Bank Al-Maghrib Circular 56/G/2007** — IFRS for banks' consolidated accounts.
- **AMMC** — listed-group consolidated-accounts IFRS option.
- **Loi de Finances 2026** — current-year confirmation of deadlines/thresholds.
- Secondary commentary (PwC Morocco, Upsilon Consulting, Deloitte LF 2026, IFRS Foundation jurisdiction profile) used for cross-checking — **not** primary authority.

### Short test suite

1. *"I'm an auto-entrepreneur — do I file financial statements?"* → **No**; register of receipts only (see `ma-bookkeeping`). No bilan/CPC.
2. *"CPU — do I prepare a bilan?"* → **No**; register of receipts and purchases only; exempt from CGNC états de synthèse.
3. *"What are the états de synthèse?"* → under the CGNC modèle normal, **five**: **Bilan, CPC, ESG, Tableau de financement, ETIC** (an inseparable whole).
4. *"Normal vs simplified model?"* → **modèle normal (5 statements)** at turnover ≥ **MAD 10,000,000**; **modèle simplifié** below, with the **ESG dropped** (exact reduced set to verify).
5. *"Do I use IFRS?"* → only **banks/insurers (mandatory)** and **listed groups (optional)** for **consolidated** accounts; an ordinary self-employed person or SARL uses the **CGNC**.
6. *"Where do I file my company accounts?"* → **attached to the IS/IR return** via **SIMPL**, and **deposited at the greffe du tribunal de commerce** (dépôt légal, ~30 days after AG approval).
7. *"Do I need a commissaire aux comptes?"* → **all SA**; **SARL/others when turnover > MAD 50,000,000 HT**; **never** for an AE/CPU/RNS/RNR individual.

## PROHIBITIONS

- **Do NOT** tell an **auto-entrepreneur** or **CPU** taxpayer they must prepare a bilan, a CPC, or any CGNC états de synthèse — they keep **registers only** (`ma-bookkeeping`).
- **Do NOT** tell an **RNR** taxpayer or a **company** they may skip the full états de synthèse under the CGNC.
- **Do NOT** state the **modèle simplifié** component list as settled — sources disagree; present it as **to verify**, anchoring only on "ESG is dropped".
- **Do NOT** tell a self-employed person or an ordinary SARL to prepare **IFRS** statements — IFRS is for banks/insurers/listed groups' **consolidated** accounts.
- **Do NOT** tell any **sole proprietor** (AE/CPU/RNS/RNR) they need a **commissaire aux comptes** — that is a company-law obligation (SA, or turnover > MAD 50M HT).
- **Do NOT** state firm thresholds, deadlines, or penalty amounts as settled — present items marked *(verify)* as provisional pending reviewer confirmation against the current CGNC / CGI / Code de Commerce / Loi de Finances 2026.
- **Do NOT** compute the tax itself here — defer to `ma-income-tax`, `ma-cpu`, `ma-auto-entrepreneur`; defer the books/invoices to `ma-bookkeeping`.
- **Do NOT** replace a licensed Moroccan **expert-comptable / commissaire aux comptes**.

## Disclaimer

This skill is **research-verified** from public sources (the CGNC, the CGI, the Code de Commerce, Loi 17-95 and Loi 5-96, Bank Al-Maghrib and AMMC materials, the IFRS Foundation jurisdiction profile, the DGI / tax.gov.ma, the Loi de Finances 2026, and reputable professional commentary) and is **pending sign-off by a licensed Moroccan expert-comptable**. It is general information, **not** accounting or tax advice, and does not create a professional engagement. Component lists (especially the **modèle simplifié**), thresholds, deadlines, penalty amounts, and audit triggers change with each Loi de Finances and with amendments to company law — every item marked *(verify)* must be confirmed against current texts before reliance. Always have a licensed Moroccan **expert-comptable** or the **DGI** review before filing or relying on this output. Part of **openaccountants.com** — open-source tax skills for the self-employed.

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
