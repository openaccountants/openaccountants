---
name: ma-return-assembly
description: >
  Use this skill to assemble and sequence the complete Moroccan tax filing package for a self-employed person once the regime, income, social and VAT figures are known. Trigger on "assemble my Morocco return", "what do I file in Morocco", "Morocco filing package", "déclaration Maroc". Consumes ma-auto-entrepreneur/ma-cpu/morocco-professional-income-tax, ma-social-contributions, morocco-vat. Computes nothing itself.
version: 0.1
jurisdiction: MA
tax_year: 2026
tier: 2
last_updated: 2026-10-31
category: orchestrator
depends_on:
  - ma-freelance-intake
---

# Morocco Return Assembly — Filing Package Orchestrator (assemblage de la déclaration marocaine)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

This is the **final orchestrator** for a Morocco-resident self-employed person (travailleur indépendant / auto-entrepreneur). It **assembles and sequences** the filing package — it **computes nothing**. Every figure originates upstream; this file decides *which declaration applies for the confirmed regime*, *what attaches*, *when each filing and payment is due*, and *how to submit through the SIMPL teleservice*.

The tax authority is the **Direction Générale des Impôts (DGI)**, which operates the **SIMPL** online portal (simpl.tax.gov.ma). Social cover runs through the **Caisse Nationale de Sécurité Sociale (CNSS)** and the **Assurance Maladie Obligatoire (AMO)**. Auto-entrepreneur flat-tax turnover is declared through the dedicated national auto-entrepreneur platform (Barid Cash / rc-auto.gov.ma) rather than SIMPL.

Reply in the user's language (French or English). Native French terms appear throughout so the package reads naturally for a Moroccan reviewer.

> This file assumes `ma-freelance-intake` has already run and the regime is **confirmed**. If the regime is still open, route back to intake before assembling.

---

## Inputs consumed

Collect these from the upstream skills before assembling. Do not re-interrogate anything the intake already settled.

| Input | Source skill | Used for |
|---|---|---|
| Residency, activity type (commerciale/artisanale vs services/profession libérale), confirmed regime | `ma-freelance-intake` | Routing the declaration |
| Annual turnover (chiffre d'affaires) in MAD | intake / regime skill | Band checks, ceiling-breach flag |
| ICE, RC number, identifiant fiscal (IF) | intake | All DGI / SIMPL filings |
| Flat-tax turnover figure (1% commercial / 2% services) | `ma-auto-entrepreneur` | Auto-entrepreneur quarterly declaration |
| CPU liability figure | `ma-cpu` | CPU annual declaration |
| Net profit (résultat net) under RNR or RNS | `morocco-professional-income-tax` | IR déclaration du revenu global |
| TVA output/input position, declaration frequency | `morocco-vat` | TVA returns (if registered) |
| CNSS / AMO registration status and contribution figures | `ma-social-contributions` | CNSS filing |
| SIMPL / platform credentials | intake | Submission |

If a content skill did not run or returned no validated output, **note the gap in the reviewer brief and continue** with available data rather than halting.

---

## Which declaration by regime

Pick exactly one income-tax track per the regime confirmed at intake. Never file two income-tax declarations for the same activity.

### Auto-entrepreneur (within 500,000 MAD commercial / 200,000 MAD services)
- **Declaration:** the **auto-entrepreneur turnover declaration**, filed **quarterly** on the national auto-entrepreneur platform (not SIMPL). Flat tax on declared turnover (1% commercial/industriel/artisanal, 2% services); the figure comes from `ma-auto-entrepreneur`.
- **TVA:** none on the flat-tax turnover — auto-entrepreneurs sit outside the TVA regime.
- **Social:** CNSS/AMO via `ma-social-contributions`.
- A **nil quarter is still declared** — file zero, do not skip.

### CPU — contribution professionnelle unique (CPU band, up to 2,000,000 MAD commercial / 500,000 MAD services)
- **Declaration:** the **CPU annual declaration**, filed via SIMPL. The CPU bundles IR plus the professional levy into a single annual figure produced by `ma-cpu`.
- **TVA:** TVA return(s) via `morocco-vat` **if registered** (CPU does not by itself remove TVA obligations).
- **Social:** CNSS/AMO via `ma-social-contributions`.

### RNR / RNS — résultat net réel / résultat net simplifié (above the ceilings, or by election)
- **Declaration:** the **IR déclaration annuelle du revenu global**, filed via SIMPL, reporting the **résultat net** (full books under RNR; simplified books under RNS) from `morocco-professional-income-tax`.
- **TVA:** TVA return(s) via `morocco-vat` — TVA applies by default for activities above the registration threshold.
- **Social:** CNSS/AMO via `ma-social-contributions`.

> **Ceiling breach mid-year** — flag prominently. The taxpayer moves up a regime (auto-entrepreneur → CPU/RNS → RNR); the reviewer sets the effective date and which declaration covers which period. Do not silently apply a single regime to the whole year.

---

## Filing & payment calendar

All SIMPL filings are electronic; payment is electronic (télépaiement) at filing. Auto-entrepreneur turnover is filed on its own platform. Dates below are the standard 2026 expectations — **confirm each against the DGI before filing**, as deadlines shift.

| Filing | Regime | Frequency | Deadline | Source skill |
|---|---|---|---|---|
| Auto-entrepreneur turnover declaration | Auto-entrepreneur | **Quarterly** | Within the **month following** each quarter-end | `ma-auto-entrepreneur` |
| CPU annual declaration | CPU | Annual | Per the CPU calendar (typically **by 1 March** of the following year) — confirm | `ma-cpu` |
| IR déclaration du revenu global | RNR / RNS | Annual | **By ~1 May** of the year following the tax year (résultat net) | `morocco-professional-income-tax` |
| TVA declaration — monthly | TVA-registered (larger turnover) | **Monthly** | By the **20th** of the following month (télédéclaration) | `morocco-vat` |
| TVA declaration — quarterly | TVA-registered (smaller turnover) | **Quarterly** | By the **20th** of the month following the quarter | `morocco-vat` |
| CNSS / AMO contributions | All regimes | Per CNSS schedule | Per CNSS rules — confirm cadence | `ma-social-contributions` |

> **TVA frequency** is set by turnover, not by income-tax regime — `morocco-vat` decides monthly vs quarterly. Do not infer it here.

> **IR deadline flag.** The résultat net IR déclaration du revenu global is generally due by **1 May**; the precise 2026 date and any electronic-filing extension must be confirmed on the DGI portal before relying on it.

---

## SIMPL submission

1. **Account / platform.** For CPU and IR (RNR/RNS), log in to **SIMPL** (simpl.tax.gov.ma) using the identifiant fiscal (IF) and SIMPL credentials. For **auto-entrepreneur**, use the national auto-entrepreneur platform instead — these are separate systems.
2. **Select the correct form** — one income-tax declaration only (auto-entrepreneur turnover *or* CPU *or* IR revenu global), plus the TVA return at the frequency `morocco-vat` set, if registered.
3. **Attach schedules** — accounts / P&L (états de synthèse where required under RNR), TVA reconciliation, and supporting workpapers from the content skills.
4. **Télépaiement** — settle the tax due electronically at filing through the portal's payment channels.
5. **Capture confirmation** — save the SIMPL (or platform) acknowledgment / accusé de réception for the file. A return is not filed until acknowledgment is received.

---

## Pre-filing checklist

- [ ] Intake (`ma-freelance-intake`) complete; residency, activity type, and regime confirmed.
- [ ] Regime decided and **exactly one** income-tax declaration selected (auto-entrepreneur / CPU / IR — never two).
- [ ] Turnover checked against the band; any ceiling breach flagged with effective date for the reviewer.
- [ ] Income figures reconciled: TVA turnover ↔ income-tax turnover/net (flag any mismatch).
- [ ] TVA returns prepared at the correct frequency (monthly vs quarterly per `morocco-vat`), or confirmed not registered.
- [ ] CNSS / AMO registration current and contributions reconciled.
- [ ] Deadlines mapped to dates (calendar above); IR ~1 May and TVA 20th-of-month dates confirmed on DGI.
- [ ] Correct portal selected (SIMPL for CPU/IR; auto-entrepreneur platform for flat tax); credentials working.
- [ ] Télépaiement method ready; expected tax-due figure available from content skills.
- [ ] All open flags (deadlines, ceiling breach, data gaps, conservative defaults) listed in the reviewer brief.
- [ ] Package routed for **qualified Moroccan expert-comptable** sign-off before any submission.

---

## Disclaimer

This skill performs **orchestration and assembly only** — it computes no tax figure. All amounts originate from the Morocco content skills (`ma-freelance-intake`, `ma-auto-entrepreneur`, `ma-cpu`, `morocco-professional-income-tax`, `ma-social-contributions`, `morocco-vat`) and **must be reviewed and signed off by a qualified Moroccan expert-comptable** before anything is filed with the DGI, CNSS, or the auto-entrepreneur platform. Deadlines, forms, thresholds, and regime rules change; verify every flagged item against the DGI (simpl.tax.gov.ma) at filing time. Nothing here is tax, legal, or financial advice.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
