---
name: kz-freelance-intake
description: "ALWAYS USE THIS SKILL when a user asks for help with their Kazakhstan taxes AND mentions freelancing, self-employment, ИП, or sole proprietorship in Kazakhstan. Trigger on \"help with my Kazakhstan taxes\", \"I'm an ИП\", \"I'm self-employed in Kazakhstan\", etc. REQUIRED entry point for the Kazakhstan self-employed workflow; downstream skills (kz-simplified-regime, kz-income-tax, kz-social-contributions, kazakhstan-vat, kz-return-assembly) depend on it. Kazakhstan-resident sole proprietors only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-freelance-intake"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-06-12"
---

# Kazakhstan Self-Employed Intake Skill v0.1 (kz-freelance-intake)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is

The intake orchestrator for a Kazakhstan-resident self-employed person — an individual entrepreneur (ИП / жеке кәсіпкер). Every downstream Kazakhstan content skill — `kz-simplified-regime`, `kz-income-tax`, `kz-social-contributions`, `kazakhstan-vat` — and the assembly orchestrator `kz-return-assembly` depend on this skill running first to produce a structured intake package.

This skill **computes nothing**. Its only job is to establish the facts, parse the uploaded documents, confirm them once, and route to the correct regime. Kazakhstan's self-employed landscape has several tax paths (special vs general) and the routing decision drives everything downstream, so getting the routing right is the whole point of this file.

Reply to the user in their own language. If they write in Russian or Kazakh, answer in that language; if in English, answer in English. Embed the native terms (ИП / жеке кәсіпкер, ТОО, упрощённая декларация / оңайлатылған декларация, общеустановленный режим / жалпыға бірдей режим, розничный налог / бөлшек салық, патент / патент, НДС / ҚҚС, ИПН / ЖТС, социальные платежи / әлеуметтік төлемдер) so the user recognises exactly which regime and form is meant.

---

## Design principles (upload-first)

Upload-first, inference-then-confirm:
1. **Compact refusal/routing sweep** — a few interactive questions, ~30 seconds, to establish form of business, regime, residency, turnover vs the special-regime ceilings, and VAT (НДС/ҚҚС) exposure.
2. **Upload-first** — the user dumps everything they have (Kaspi/Halyk bank statements, ИП registration, prior declarations).
3. **Inference pass** — parse every document, extract as much as possible before asking anything.
4. **Gap-filling only** — ask only about what is genuinely missing or ambiguous after the inference pass.
5. **Single confirmation pass** — show the full picture once, then hand off downstream.

Do not narrate phases ("now I am inferring…"). Do not re-ask anything already visible in the uploaded documents. Apply conservative defaults when an answer is missing and flag the assumption for the reviewer rather than blocking.

---

## Step 1 — Refusal / routing sweep (route to the right regime)

Establish, fast and in this order:

1. **ИП (жеке кәсіпкер) or ТОО?**
   - **ИП (individual entrepreneur)** → continue in this workflow.
   - **ТОО (a legal entity / juridical person)** → **out of scope. Escalate** to a qualified Kazakhstan accountant. This workflow covers individuals only, not corporate income tax (КПН / КТС).

2. **Which tax regime are you on?** This is the central routing question:
   - **Упрощённая декларация (оңайлатылған декларация)** — the most common special regime for small ИП. A flat 3% on turnover (split between ИПН and социальный налог), filed half-yearly on form 910.00. → routes to `kz-simplified-regime`.
   - **Розничный налог (бөлшек салық)** — a special reduced-rate regime for qualifying retail/service activity serving end consumers. → routes to `kz-simplified-regime` (retail-tax branch).
   - **Патент (патент)** — the simplest path for a solo ИП with no employees and limited turnover; tax prepaid on form 911.00. → routes to `kz-simplified-regime` (patent branch).
   - **Общеустановленный режим (жалпыға бірдей режим)** — ИПН on net income (income minus deductible expenses) filed on form 220.00, plus НДС if registered. Default for an ИП who never elected a special regime, or who exceeded a special-regime ceiling. → routes to `kz-income-tax`.
   - If the user does not know their regime, infer it from the documents (a 910.00 ⇒ упрощёнка; a 911.00 / patent receipt ⇒ патент; a 220.00 ⇒ общеустановленный; the registration extract often states the elected regime).

3. **Kazakhstan tax resident for the year (183+ days in KZ, or centre of vital interests)?**
   - Non-residents have materially different ИПН treatment and cannot use the special regimes the same way → flag prominently and **escalate** if non-resident; do not silently assume residency.

4. **Does annual turnover exceed the special-regime ceilings or the VAT registration threshold?**
   - The special regimes (упрощёнка, розничный налог, патент) each have their own turnover ceiling expressed in МРП (монтхly calculation index) over the tax period; if the ИП breaches the applicable ceiling, they fall out of the special regime and onto общеустановленный режим. The reviewer confirms the exact 2026 МРП-denominated ceiling for the elected regime — do not hardcode it here.
   - **VAT (НДС / ҚҚС) registration threshold — note the 2026 change:** the new Tax Code effective 1 January 2026 **lowered the mandatory VAT registration threshold**. Once cumulative annual turnover crosses the 2026 threshold, the ИП must register for НДС and an obligation arises. Have the reviewer apply the precise 2026 МРП figure; flag any ИП approaching or over it. → engage `kazakhstan-vat`.

5. **VAT (НДС / ҚҚС) status — already registered?**
   - If the ИП is **already VAT-registered** (voluntarily or by threshold breach), engage `kazakhstan-vat` regardless of regime.
   - Note: an ИП on the simplified declaration that crosses the VAT threshold must register even while staying on упрощёнка for income-tax purposes — VAT and income-tax regime are separate determinations.

Conservative defaults if unanswered: ИП on упрощённая декларация (3%, form 910.00); Kazakhstan resident; turnover under the special-regime ceiling and under the VAT threshold; not VAT-registered. Always flag each default for the reviewer.

---

## Step 2 — Collect

Ask the user to upload (whatever they have — partial is fine):
- **Bank statements** for all accounts — typically **Kaspi** and **Halyk** (Kaspi Business / Halyk Bank), RUB/USD/EUR plus KZT — for the full year, to reconcile against declared turnover and catch unreported receipts.
- **ИП registration extract** (свидетельство / уведомление о регистрации ИП, talon) — confirms the elected regime, ОКЭД activity codes, and employee status.
- **Prior-year declarations** — form 910.00 (упрощёнка), 911.00 (патент), 220.00 (общеустановленный), and any 300.00 НДС returns — plus **социальные платежи** payment history (ОПВ pension, СО social contributions, ВОСМС medical, социальный налог).
- Any **patent / розничный налог** documents if the user mentions them — these change the routing branch; flag for the reviewer.

## Step 3 — Infer & confirm

- Determine **regime** from the documents if not stated (910.00 ⇒ упрощёнка; 911.00 ⇒ патент; 220.00 ⇒ общеустановленный; registration extract often states it).
- Total **turnover (оборот)** from the bank data and run it against the applicable special-regime ceiling **and** the 2026 VAT registration threshold; flag if the user is approaching or has breached either.
- Separate genuine business turnover from internal transfers, loan movements, and personal funds in the Kaspi/Halyk data.
- Convert any **FX receipts to KZT** at the National Bank (НБ РК / ҚРҰБ) rate on the date of receipt.
- Check **VAT (НДС/ҚҚС) status** — already registered, or turnover over the 2026 threshold requiring registration.
- Note **социальные платежи** status for the ИП (ОПВ, СО, ВОСМС, and социальный налог where applicable) — for the reviewer to compute, not this skill.
- Present one consolidated summary: form of business, regime, residency, turnover vs ceiling + VAT threshold, VAT status, contributions status. Get a single confirmation.

## Step 4 — Hand off (the routing map)

Produce a structured intake package and route based on the confirmed regime:

- **ИП on упрощённая декларация / розничный налог / патент:** `kz-simplified-regime` (correct branch) **+** `kz-social-contributions` (ОПВ + СО + ВОСМС + социальный налог) **+** `kazakhstan-vat` if VAT-registered or over the 2026 threshold → `kz-return-assembly`.
- **ИП on общеустановленный режим:** `kz-income-tax` (ИПН on net income, form 220.00) **+** `kz-social-contributions` **+** `kazakhstan-vat` if registered or over threshold → `kz-return-assembly`.
- **Ceiling breach mid-period:** route turnover up to the breach to the special-regime skill, and post-breach turnover to `kz-income-tax`; engage `kazakhstan-vat` from the registration date; flag prominently.
- **ТОО, non-resident, or other complexity:** stop and escalate to a qualified Kazakhstan accountant.

Always pass forward: form of business, regime, residency status, annual turnover figure, VAT determination (incl. the 2026 threshold check), социальные платежи status, and every assumption made under a conservative default.

---

## Disclaimer

This skill orchestrates intake only and computes no tax. It establishes facts and routes to downstream skills. All figures, regime determinations, and downstream outputs must be reviewed and signed off by a qualified Kazakhstan accountant (бухгалтер / салық кеңесшісі) before anything is filed with the State Revenue Committee (КГД / МКД). The most up-to-date version is maintained at [openaccountants.com](https://www.openaccountants.com).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-06-12. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
