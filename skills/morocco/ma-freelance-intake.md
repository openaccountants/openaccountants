---
name: ma-freelance-intake
description: Use this skill first when a user asks for help with Moroccan taxes and mentions freelancing, self-employment, auto-entrepreneur or sole proprietorship in Morocco, tax year 2026. Trigger on "help with my Morocco taxes", "I am an auto-entrepreneur", "I am self-employed in Morocco", "travailleur independant Maroc". Required entry point for the Morocco self-employed workflow, it establishes the facts and routes to ma-auto-entrepreneur, ma-cpu, morocco-professional-income-tax, ma-social-contributions, morocco-vat and ma-return-assembly using the 2026 CGI regime limits. Morocco-resident sole proprietors only.
version: 1.0
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-14
type: router
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# Morocco self-employed intake and routing, tax year 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

The intake orchestrator for a Morocco-resident self-employed person (travailleur indépendant / auto-entrepreneur). Every downstream Morocco content skill (`ma-auto-entrepreneur`, `ma-cpu`, `morocco-professional-income-tax`, `ma-social-contributions`, `morocco-vat`) and the assembly orchestrator `ma-return-assembly` depend on this skill running first to produce a structured intake package.

This skill **computes nothing**. Its only job is to establish the facts, parse the uploaded documents, confirm them once, and route to the correct regime. Morocco's self-employed landscape spans three income-tax (IR / impôt sur le revenu) paths plus social and VAT layers, and the routing decision drives everything downstream, so getting the routing right is the whole point of this file.

Reply to the user in their own language. If they write in French, answer in French; if in English, answer in English. Embed the native French terms (auto-entrepreneur, contribution professionnelle unique / CPU, régime du résultat net réel / RNR, régime du résultat net simplifié / RNS, registre du commerce / RC, identifiant commun de l'entreprise / ICE, taxe sur la valeur ajoutée / TVA, CNSS, AMO) so the user recognises exactly which regime and form is meant.


## Ask the client first

The five facts that decide the route: sole proprietor or company; activity type (commercial, industrial or craft, or services); turnover collected in 2026 and in the two years before; tax residence in 2026; VAT registration or invoices showing VAT. Then the design below.

### Design principles (upload-first)

Upload-first, inference-then-confirm:
1. **Compact refusal/routing sweep** ,  a few interactive questions, ~30 seconds, to establish activity type, turnover band, residency, and VAT exposure.
2. **Upload-first** ,  the user dumps everything they have (bank statements, RC/ICE registration, prior IR declarations, auto-entrepreneur attestations).
3. **Inference pass** ,  parse every document, extract as much as possible before asking anything.
4. **Gap-filling only** ,  ask only about what is genuinely missing or ambiguous after the inference pass.
5. **Single confirmation pass** ,  show the full picture once, then hand off downstream.

Do not narrate phases ("now I am inferring…"). Do not re-ask anything already visible in the uploaded documents. Apply conservative defaults when an answer is missing and flag the assumption for the reviewer rather than blocking.


## The method, step by step

### Rates, bands and thresholds

The regime limits that drive the routing. Each regime skill owns the detail; these are here only to route.

| Item | Limit or rate | Conditions | Year | Source URL |
|---|---|---|---|---|
| Auto-entrepreneur limit, commercial, industrial, craft | MAD 500,000 turnover collected a year | Art. 42 ter-II-A. Also needs social security membership (42 ter-II-B) | 2026 | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 |
| Auto-entrepreneur limit, services | MAD 200,000 turnover collected a year | Art. 42 ter-II-A | 2026 | same |
| Auto-entrepreneur IR, commercial, industrial, craft | 0.5% of turnover collected | Art. 73-III | 2026 | same |
| Auto-entrepreneur IR, services | 1% of turnover collected | Art. 73-III. Services above MAD 80,000 from one client: the client withholds on the excess (see ma-auto-entrepreneur) | 2026 | same |
| CPU limit, commercial, industrial, craft | MAD 2,000,000 a year | Art. 41-II-A. Needs AMO membership (41-II-B) | 2026 | same |
| CPU limit, services | MAD 500,000 a year | Art. 41-II-A | 2026 | same |
| RNS limit, commercial, industrial, craft, fishing | MAD 2,000,000 a year, excluding VAT | Art. 39. Exit after two consecutive years over | 2026 | same |
| RNS limit, services | MAD 500,000 a year, excluding VAT | Art. 39 | 2026 | same |
| Tax residence, days test | More than 183 days in any 365-day period | Art. 23. Also a permanent home or centre of economic interests in Morocco | 2026 | same |

### Step 1: refusal and routing sweep

Establish, fast and in this order:

1. **Sole proprietor or company?**
   - **Personne physique** (auto-entrepreneur or other individual sole proprietor) to continue in this workflow.
   - **Société (SARL, SA, etc.)** to **out of scope. Escalate** to a qualified Moroccan expert-comptable. This workflow covers individuals taxed under IR only, not corporate tax (impôt sur les sociétés / IS).

2. **Activity type** ,  this drives every turnover threshold below:
   - **Commerciale, industrielle ou artisanale** (selling goods, manufacturing, craft) ,  the higher-threshold track.
   - **Prestations de services / profession libérale** (consulting, IT, design, professional services) ,  the lower-threshold track.
   - A mixed activity takes the lower (services) threshold for the services portion; flag mixed activity for the reviewer.

3. **Annual turnover (chiffre d'affaires) vs the thresholds** ,  the central routing question:
   - **Auto-entrepreneur:** up to **500,000 MAD** commercial/industrial/artisanal, or **200,000 MAD** services. Simplest regime; flat IR on turnover collected (0.5% commercial, industrial or craft, 1% services, Art. 73-III), paid through the national auto-entrepreneur platform. to routes to `ma-auto-entrepreneur`.
   - **CPU (contribution professionnelle unique) or RNS:** above the auto-entrepreneur band (or by choice) and up to **2,000,000 MAD** commercial/industrial/artisanal, or **500,000 MAD** services. to routes to `ma-cpu` (CPU) or `morocco-professional-income-tax` (RNS net profit), depending on the elected option.
   - **RNR (régime du résultat net réel):** above the CPU/RNS turnover ceilings, or where the taxpayer elects to be taxed on actual net profit. to routes to `morocco-professional-income-tax`.
   - If the user does not know their regime, infer it: an auto-entrepreneur attestation means auto-entrepreneur; turnover inside the CPU band with no full books means CPU/RNS; turnover above the ceilings or full accounting records means RNR.

4. **Moroccan tax resident for the year?** Resident if the permanent home (foyer permanent d'habitation) or centre of economic interests is in Morocco, or the stay exceeds 183 days in any 365-day period (Art. 23).
   - Non-residents are taxed only on Moroccan-source income and cannot use these regimes the same way to flag prominently and **escalate** if non-resident; do not silently assume residency.

5. **VAT (TVA) exposure?**
   - Auto-entrepreneurs are outside the TVA regime on their flat-tax turnover.
   - Service providers and commercial activities liable to TVA charge it (standard rate 20%, reduced 10%, Art. 99; the small-business exemption is in `morocco-vat`). If the user is registered for TVA or appears to exceed the threshold, to engage `morocco-vat`.
   - Where TVA status is unclear, infer from invoices (TVA shown means registered) and the prior IR declaration; confirm before routing.

Conservative defaults if unanswered: auto-entrepreneur where an attestation exists and turnover is within band; otherwise CPU within the CPU band; RNR above the ceilings; Moroccan resident; no TVA unless an invoice or registration says otherwise. Always flag each default for the reviewer.


### Step 2: collect

Ask the user to upload (whatever they have ,  partial is fine):
- **Bank statements** (only if the user offers them; do not insist) for all accounts (MAD and any FX) for the full year ,  to reconcile against declared turnover and catch unrecorded receipts.
- **RC / ICE registration documents** (registre du commerce, identifiant commun de l'entreprise) and any **auto-entrepreneur attestation / carte** ,  confirms activity type, registration status, and regime.
- **Prior-year IR declaration** and any CPU or auto-entrepreneur payment receipts ,  anchors the regime and the prior turnover figure.
- **Invoices issued** (factures) and expense records ,  to establish turnover, activity type, and whether TVA is being charged.
- **CNSS / AMO** registration and contribution history ,  for the social-contributions hand-off.

### Step 3: infer and confirm

- Determine **activity type and regime** from the documents if not stated (auto-entrepreneur attestation means auto-entrepreneur; CPU receipts means CPU; full books / over-ceiling turnover means RNR).
- Total the **chiffre d'affaires** from invoices and bank receipts; check it against the relevant band (500k/200k auto-entrepreneur; 2,000,000/500,000 CPU/RNS) and flag if the user is approaching or has breached a ceiling.
- Separate genuine business turnover from internal transfers, loan movements, and personal funds in the bank data.
- Convert any **FX receipts to MAD** at the Bank Al-Maghrib rate on the date of receipt.
- Check **TVA exposure** against the registration thresholds and the prior declaration.
- Confirm **CNSS / AMO** registration status (mandatory social cover for the self-employed ,  for the reviewer to compute, not this skill).
- Present one consolidated summary: activity type, regime, residency, turnover vs thresholds, TVA status, social-contributions status. Get a single confirmation.

### Step 4: hand off (the routing map)

Produce a structured intake package and route based on the confirmed regime:

- **Auto-entrepreneur** (within 500k/200k band): `ma-auto-entrepreneur` (flat tax on turnover) **+** `ma-social-contributions` (CNSS/AMO) to `ma-return-assembly`. No TVA on the flat-tax turnover.
- **CPU / RNS** (CPU band, up to 2,000,000/500,000): `ma-cpu` (CPU) or `morocco-professional-income-tax` (RNS net profit, per the elected option) **+** `ma-social-contributions` **+** `morocco-vat` if TVA-registered to `ma-return-assembly`.
- **RNR** (above the ceilings or by election): `morocco-professional-income-tax` (RNR net profit, full books) **+** `ma-social-contributions` **+** `morocco-vat` (TVA by default for activities above the threshold) to `ma-return-assembly`.
- **Ceiling breach mid-year:** flag prominently; the taxpayer moves up a regime (auto-entrepreneur to CPU/RNS, or CPU/RNS to RNR) and the reviewer determines the effective date. Route accordingly.
- **Société, non-resident, or other complexity (IS, multi-activity, foreign establishment):** stop and escalate to a qualified Moroccan expert-comptable.

Always pass forward: activity type, regime, residency status, annual turnover figure, TVA determination, CNSS/AMO status, and every assumption made under a conservative default.


## Worked cases

**Case: a web designer, services, turnover collected MAD 180,000 in 2026, resident, no VAT invoices, AE attestation on file.** Services limit MAD 200,000, so the auto-entrepreneur route holds with MAD 20,000 of headroom. Flat IR at 1%: MAD 1,800 (computed in `ma-auto-entrepreneur`, which also checks the one-client MAD 80,000 rule). Route: `ma-auto-entrepreneur` plus `ma-social-contributions`, then `ma-return-assembly`. Flag that "web design" sits close to "IT service providers", which are excluded from CPU, so if turnover passes the limit the next route is RNS or RNR, not CPU.

```oa-check
name: Web designer on the auto-entrepreneur route
inputs:
  turnover: 180000
  services_limit: 200000
  rate: 0.01
steps:
  - headroom: services_limit - turnover
  - flat_ir: turnover * rate
expected:
  headroom: 20000
  flat_ir: 1800
```

## When to refuse or refer

- A company (SARL, SA and others): out of scope, escalate to a Moroccan expert-comptable. This workflow covers individuals taxed under IR only, not corporate tax (IS).
- A non-resident: flag and escalate; do not assume residency.
- Multi-activity mixes across limits, a foreign establishment, or a mid-year ceiling breach where the effective date is unclear: escalate.
- This skill computes nothing and files nothing. All figures, regime findings and downstream outputs are reviewed and signed off by a qualified Moroccan expert-comptable before anything is filed with the DGI.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code Général des Impôts 2026, DGI, French edition. Read for Art. 23 residence (183 days), Art. 39 RNS limits, Art. 41-II CPU limits, Art. 42 ter auto-entrepreneur limits, Art. 73-III auto-entrepreneur rates (0.5% and 1%) and Art. 99 VAT rates | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-14 |

Not yet confirmed: none.
