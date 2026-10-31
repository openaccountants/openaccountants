---
name: ma-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with their Moroccan taxes AND mentions freelancing, self-employment, auto-entrepreneur, or sole proprietorship in Morocco. Trigger on "help with my Morocco taxes", "I'm an auto-entrepreneur", "I'm self-employed in Morocco", etc. REQUIRED entry point for the Morocco self-employed workflow; downstream skills (ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax, ma-social-contributions, morocco-vat, ma-return-assembly) depend on it. Morocco-resident sole proprietors only.
version: 0.1
jurisdiction: MA
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: orchestrator
---

# Morocco Self-Employed Intake Skill v0.1 (ma-freelance-intake)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

The intake orchestrator for a Morocco-resident self-employed person (travailleur indépendant / auto-entrepreneur). Every downstream Morocco content skill — `ma-auto-entrepreneur`, `ma-cpu`, `morocco-professional-income-tax`, `ma-social-contributions`, `morocco-vat` — and the assembly orchestrator `ma-return-assembly` depend on this skill running first to produce a structured intake package.

This skill **computes nothing**. Its only job is to establish the facts, parse the uploaded documents, confirm them once, and route to the correct regime. Morocco's self-employed landscape spans three income-tax (IR / impôt sur le revenu) paths plus social and VAT layers, and the routing decision drives everything downstream, so getting the routing right is the whole point of this file.

Reply to the user in their own language. If they write in French, answer in French; if in English, answer in English. Embed the native French terms (auto-entrepreneur, contribution professionnelle unique / CPU, régime du résultat net réel / RNR, régime du résultat net simplifié / RNS, registre du commerce / RC, identifiant commun de l'entreprise / ICE, taxe sur la valeur ajoutée / TVA, CNSS, AMO) so the user recognises exactly which regime and form is meant.

---

## Design principles (upload-first)

Upload-first, inference-then-confirm:
1. **Compact refusal/routing sweep** — a few interactive questions, ~30 seconds, to establish activity type, turnover band, residency, and VAT exposure.
2. **Upload-first** — the user dumps everything they have (bank statements, RC/ICE registration, prior IR declarations, auto-entrepreneur attestations).
3. **Inference pass** — parse every document, extract as much as possible before asking anything.
4. **Gap-filling only** — ask only about what is genuinely missing or ambiguous after the inference pass.
5. **Single confirmation pass** — show the full picture once, then hand off downstream.

Do not narrate phases ("now I am inferring…"). Do not re-ask anything already visible in the uploaded documents. Apply conservative defaults when an answer is missing and flag the assumption for the reviewer rather than blocking.

---

## Step 1 — Refusal / routing sweep (route to the right regime)

Establish, fast and in this order:

1. **Sole proprietor or company?**
   - **Personne physique** (auto-entrepreneur or other individual sole proprietor) → continue in this workflow.
   - **Société (SARL, SA, etc.)** → **out of scope. Escalate** to a qualified Moroccan expert-comptable. This workflow covers individuals taxed under IR only, not corporate tax (impôt sur les sociétés / IS).

2. **Activity type** — this drives every turnover threshold below:
   - **Commerciale, industrielle ou artisanale** (selling goods, manufacturing, craft) — the higher-threshold track.
   - **Prestations de services / profession libérale** (consulting, IT, design, professional services) — the lower-threshold track.
   - A mixed activity takes the lower (services) threshold for the services portion; flag mixed activity for the reviewer.

3. **Annual turnover (chiffre d'affaires) vs the thresholds** — the central routing question:
   - **Auto-entrepreneur:** up to **500,000 MAD** commercial/industrial/artisanal, or **200,000 MAD** services. Simplest regime; flat tax on turnover (1% commercial, 2% services) paid via the national auto-entrepreneur platform. → routes to `ma-auto-entrepreneur`.
   - **CPU (contribution professionnelle unique) / RNS:** above the auto-entrepreneur band and up to **2,000,000 MAD** commercial/industrial/artisanal, or **500,000 MAD** services. → routes to `ma-cpu` (CPU) or `morocco-professional-income-tax` (RNS net profit), depending on the elected option.
   - **RNR (régime du résultat net réel):** above the CPU/RNS turnover ceilings, or where the taxpayer elects to be taxed on actual net profit. → routes to `morocco-professional-income-tax`.
   - If the user does not know their regime, infer it: an auto-entrepreneur attestation ⇒ auto-entrepreneur; turnover inside the CPU band with no full books ⇒ CPU/RNS; turnover above the ceilings or full accounting records ⇒ RNR.

4. **Moroccan tax resident for the year?** Resident if the habitual home (foyer permanent d'habitation), centre of economic interests, or 183+ days in Morocco in the 365-day period.
   - Non-residents are taxed only on Moroccan-source income and cannot use these regimes the same way → flag prominently and **escalate** if non-resident; do not silently assume residency.

5. **VAT (TVA) exposure?**
   - Auto-entrepreneurs are outside the TVA regime on their flat-tax turnover.
   - Service providers and commercial activities above the TVA registration thresholds charge TVA (standard rate 20%, with reduced rates for certain activities). If the user is registered for TVA or appears to exceed the threshold, → engage `morocco-vat`.
   - Where TVA status is unclear, infer from invoices (TVA shown ⇒ registered) and the prior IR declaration; confirm before routing.

Conservative defaults if unanswered: auto-entrepreneur where an attestation exists and turnover is within band; otherwise CPU within the CPU band; RNR above the ceilings; Moroccan resident; no TVA unless an invoice or registration says otherwise. Always flag each default for the reviewer.

---

## Step 2 — Collect

Ask the user to upload (whatever they have — partial is fine):
- **Bank statements** for all accounts (MAD and any FX) for the full year — to reconcile against declared turnover and catch unrecorded receipts.
- **RC / ICE registration documents** (registre du commerce, identifiant commun de l'entreprise) and any **auto-entrepreneur attestation / carte** — confirms activity type, registration status, and regime.
- **Prior-year IR declaration** and any CPU or auto-entrepreneur payment receipts — anchors the regime and the prior turnover figure.
- **Invoices issued** (factures) and expense records — to establish turnover, activity type, and whether TVA is being charged.
- **CNSS / AMO** registration and contribution history — for the social-contributions hand-off.

## Step 3 — Infer & confirm

- Determine **activity type and regime** from the documents if not stated (auto-entrepreneur attestation ⇒ auto-entrepreneur; CPU receipts ⇒ CPU; full books / over-ceiling turnover ⇒ RNR).
- Total the **chiffre d'affaires** from invoices and bank receipts; check it against the relevant band (500k/200k auto-entrepreneur; 2,000,000/500,000 CPU/RNS) and flag if the user is approaching or has breached a ceiling.
- Separate genuine business turnover from internal transfers, loan movements, and personal funds in the bank data.
- Convert any **FX receipts to MAD** at the Bank Al-Maghrib rate on the date of receipt.
- Check **TVA exposure** against the registration thresholds and the prior declaration.
- Confirm **CNSS / AMO** registration status (mandatory social cover for the self-employed — for the reviewer to compute, not this skill).
- Present one consolidated summary: activity type, regime, residency, turnover vs thresholds, TVA status, social-contributions status. Get a single confirmation.

## Step 4 — Hand off (the routing map)

Produce a structured intake package and route based on the confirmed regime:

- **Auto-entrepreneur** (within 500k/200k band): `ma-auto-entrepreneur` (flat tax on turnover) **+** `ma-social-contributions` (CNSS/AMO) → `ma-return-assembly`. No TVA on the flat-tax turnover.
- **CPU / RNS** (CPU band, up to 2,000,000/500,000): `ma-cpu` (CPU) or `morocco-professional-income-tax` (RNS net profit, per the elected option) **+** `ma-social-contributions` **+** `morocco-vat` if TVA-registered → `ma-return-assembly`.
- **RNR** (above the ceilings or by election): `morocco-professional-income-tax` (RNR net profit, full books) **+** `ma-social-contributions` **+** `morocco-vat` (TVA by default for activities above the threshold) → `ma-return-assembly`.
- **Ceiling breach mid-year:** flag prominently; the taxpayer moves up a regime (auto-entrepreneur → CPU/RNS, or CPU/RNS → RNR) and the reviewer determines the effective date. Route accordingly.
- **Société, non-resident, or other complexity (IS, multi-activity, foreign establishment):** stop and escalate to a qualified Moroccan expert-comptable.

Always pass forward: activity type, regime, residency status, annual turnover figure, TVA determination, CNSS/AMO status, and every assumption made under a conservative default.

---

## Disclaimer

This skill orchestrates intake only and computes no tax. It establishes facts and routes to downstream skills. All figures, regime determinations, and downstream outputs must be reviewed and signed off by a qualified Moroccan expert-comptable before anything is filed with the Direction Générale des Impôts (DGI). The most up-to-date version is maintained at [openaccountants.com](https://www.openaccountants.com).
