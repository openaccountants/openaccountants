---
name: ru-return-assembly
description: Use this skill as the final orchestrator that assembles the complete Russian filing package for a Russia-resident self-employed person (самозанятый, ИП). It runs last, after the Russia content skills, and produces the ready-to-file set of declarations, payment notifications (уведомления), and the ЕНП/ЕНС reconciliation. It computes nothing of its own — every figure comes from the upstream content skills and is signed off by a qualified Russian accountant. Trigger on phrases like "file my Russian tax return", "submit УСН declaration", "сдать декларацию по УСН", "3-НДФЛ filing", "подать 3-НДФЛ", "ЕНП payment", "уплатить ЕНП", "assemble my Russian filing package", or any request to finalise and submit a Russia self-employed return. Russia-resident self-employed only.
version: 0.1
jurisdiction: RU
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - ru-freelance-intake
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RU Return Assembly

## 1. What this file is

This is the **final orchestrator** of the Russia self-employed workflow. It runs **last**, after `ru-freelance-intake` has routed the case and after the relevant content skills (`ru-self-employed-npd`, `ru-usn`, `ru-income-tax`, `ru-social-contributions`, `russia-vat`) have produced their computed outputs.

Its single job is to **assemble the filing package**: pick the right declaration for the regime, attach the required schedules, lay out the payment-and-submission calendar, build the unified-tax-account (ЕНП/ЕНС) picture with its notifications (уведомления об исчисленных суммах), and run a final pre-filing checklist before anything goes to the ФНС.

This skill **computes nothing**. It does not calculate tax, contributions, or НДС. Every monetary figure it lays out is produced upstream and reviewed by a qualified Russian accountant. If a figure is missing, it stops and points back to the content skill that owns it — it never invents a number.

Reply to the user in their own language. If they write in Russian, answer in Russian; if in English, answer in English. Keep the native Russian terms (декларация по УСН, 3-НДФЛ, ЕНП, ЕНС, уведомление, личный кабинет, страховые взносы, НДС, КУДиР) inline so the user recognises exactly which form, account, or deadline is meant.

## 2. Inputs required

This skill consumes the structured outputs of the upstream skills. Before assembling, confirm you have:

- **Confirmed routing** from `ru-freelance-intake`: form of business (самозанятый / ИП), regime (НПД / УСН / ОСНО), Russian tax-residency status, annual income vs the НПД cap, and the НДС determination.
- **The computed tax figure** from the regime content skill:
  - НПД → confirmation from `ru-self-employed-npd` that tax is auto-calculated in «Мой налог» (no declaration to assemble).
  - УСН → annual tax and quarterly advance amounts from `ru-usn` (object «доходы» 6% or «доходы минус расходы» 15%; reduced regional rate if any).
  - ОСНО → НДФЛ figures from `ru-income-tax`.
- **Страховые взносы** figures from `ru-social-contributions` for an ИП (фиксированные взносы plus the 1%-over-300,000 ₽ amount).
- **НДС** figures and the quarterly decomposition from `russia-vat`, where НДС applies.
- **Supporting records**: КУДиР (книга учёта доходов и расходов) for УСН/ОСНО, bank reconciliation, prior-year filings, and the ЕНС balance / saldo if known.
- **Submission credentials status**: access to the ФНС личный кабинет (ЛК ИП / ЛК ФЛ) or an ЭДО operator, and a valid electronic signature (УКЭП / КЭП) where required.

If any required input is absent, do not assemble — name the missing item and the content skill that owns it, and stop.

## 3. Decision tree by regime

Determine which return(s) apply from the **confirmed regime**. Do not re-derive the regime here; trust the intake routing.

### НПД — самозанятый (физлицо or ИП on НПД)

- **НПД filing and payment rules** — No tax return at all. Налог на профессиональный доход is calculated automatically inside the «Мой налог» app from the чеки (receipts) the user records. The ФНС posts the amount due to the app, typically by the 12th of the following month. Payment: monthly, by the 28th of the following month (via «Мой налог», autopay, or ЕНП). No уведомление is needed because the ФНС already knows the amount. No страховые взносы are mandatory on НПД (pension contributions are voluntary). No НДС. Assembly output for НПД is therefore a payment-and-confirmation package: confirm чеки are complete and reconciled to bank receipts, confirm the running annual total stays under the 2,400,000 ₽ cap, and produce the monthly payment schedule. → no declaration.  _(ru-return-assembly skill text, section 3 НПД)_
- **НПД annual income cap** — 2,400,000 ₽  _(ru-return-assembly skill text, section 3 НПД)_

### УСН — ИП on упрощённая система

- **УСН annual return requirements** — Annual return: декларация по УСН (КНД 1152017). Attach the regime-appropriate sections (для «доходы»: разделы 1.1 and 2.1.1, plus 2.1.2 if a trade levy applies; для «доходы минус расходы»: разделы 1.2 and 2.2). Note: the ФНС approved an updated УСН form for 2026 (приказ ФНС от 26.11.2025 № ЕД-7-3/1017@) — confirm the current form before filing. (Form-number / effective-date detail to be confirmed against nalog.gov.ru at filing time.)  _(приказ ФНС от 26.11.2025 № ЕД-7-3/1017@)_
- **КУДиР maintenance for УСН** — КУДиР is maintained but not filed; keep it on hand for any ФНС request.  _(ru-return-assembly skill text, section 3 УСН)_
- **Quarterly advances for УСН** — Advance payments are due during the year via ЕНП, each preceded by an уведомление об исчисленных суммах so the ФНС can allocate the ЕНП to the right tax (see calendar in Section 4).  _(ru-return-assembly skill text, section 3 УСН)_
- **Страховые взносы for УСН** — Engage ru-social-contributions — fixed contributions plus 1% over 300,000 ₽. The «доходы» tax can be reduced by paid contributions; ensure the upstream computation already reflected this.  _(ru-return-assembly skill text, section 3 УСН)_
- **НДС threshold for УСН ИП from 2026** — 20,000,000 ₽ (If 2025 income exceeded this threshold (or the threshold is crossed during 2026), НДС applies → add the quarterly декларация по НДС from russia-vat. From 2026, an ИП on УСН is not automatically НДС-exempt.)  _(ru-return-assembly skill text, section 3 УСН)_

### ОСНО — ИП (or individual) on общая система

- **ОСНО annual return requirements** — Annual return: 3-НДФЛ (декларация по форме 3-НДФЛ, КНД 1151020), reporting business income net of professional deductions (профессиональный вычет). (Confirm the current 3-НДФЛ form revision at filing time.)  _(КНД 1151020)_
- **НДФЛ payment schedule for ОСНО** — The annual balance is paid by 15 July; advance НДФЛ payments are made during the year (by the 28th of the month after each quarter), each with an уведомление.  _(ru-return-assembly skill text, section 3 ОСНО)_
- **НДС for ОСНО** — Charged by default → quarterly декларация по НДС from russia-vat, filed electronically only.  _(ru-return-assembly skill text, section 3 ОСНО)_
- **Страховые взносы and КУДиР for ОСНО** — Страховые взносы: engage ru-social-contributions (fixed + 1% over 300k). Supporting book: КУДиР for ОСНО is maintained, not filed.  _(ru-return-assembly skill text, section 3 ОСНО)_
- **Stop-and-escalate from the tree** — ООО / corporate налог на прибыль, non-resident status, ПСН (патент) complexity, or a mid-year НПД cap breach that splits income across regimes — hand to a qualified Russian accountant rather than assembling a package automatically.  _(ru-return-assembly skill text, section 3 stop-and-escalate note)_

## 4. Filing & payment calendar (tax year 2026)

All tax payments for ИП flow through the единый налоговый платёж (ЕНП) into the единый налоговый счёт (ЕНС); the ФНС then offsets the balance against each obligation. Where a payment has no corresponding declaration on the same date (e.g. УСН advances, fixed contributions), an уведомление об исчисленных суммах (КНД 1110355) must precede it so the ЕНП is allocated correctly. Statutory deadlines that fall on a weekend shift to the next working day; the 2026 shifts are reflected below — verify each against nalog.gov.ru before filing.

**Filing & payment calendar (tax year 2026)**  _(ru-return-assembly skill text, section 4 calendar table)_

| Obligation | НПД (самозанятый) | ИП on УСН | ИП on ОСНО |
| --- | --- | --- | --- |
| **Annual declaration** | None — auto-calc in «Мой налог» | Декларация по УСН — by **25 Apr** (→ **28 Apr 2026**, as 25 Apr is Saturday) | **3-НДФЛ** — by **30 Apr 2026** |
| **Main tax payment** | Monthly via app/ЕНП, by **28th** of following month | Annual tax via ЕНП after the declaration; quarterly advances during the year | НДФЛ annual balance by **15 Jul 2026**; advances by 28th after each quarter |
| **Advance уведомления** | Not applicable | I кв → **27 Apr**, полугодие → **27 Jul**, 9 мес → **26 Oct 2026** | НДФЛ advance уведомления by the 25th preceding each 28th payment |
| **Страховые взносы — fixed** | Voluntary only | Fixed amount via ЕНП by **28 Dec 2026** | Fixed amount via ЕНП by **28 Dec 2026** |
| **Страховые взносы — 1% over 300k** | Not applicable | By **1 Jul 2027** (for 2026 income) | By **1 Jul 2027** (for 2026 income) |
| **НДС (if applicable)** | Never | If 2026 income > 20M ₽: quarterly декларация by 25th (→ **27 Apr / 27 Jul / 26 Oct 2026**, weekend shifts); pay in thirds by the 28th | Quarterly декларация by 25th (same 2026 shifts); pay in thirds by the 28th, **electronic filing only** |

**ЕНП mechanic:** money paid as ЕНП sits on the ЕНС and is distributed by the ФНС to specific taxes/contributions. The **уведомление** is what tells the ФНС how to split it when no declaration carries that information yet. Missing or late уведомления are a common cause of mis-allocation and pени — treat them as first-class deliverables, not afterthoughts.

Do not restate detailed **rates or amounts** here; those belong to the content skills (`ru-usn`, `ru-income-tax`, `ru-social-contributions`, `russia-vat`).

## 5. Submission

**Channel — ФНС личный кабинет:**
- ИП file the декларация по УСН / 3-НДФЛ and НДС returns through the **личный кабинет ИП** on nalog.gov.ru, or through an **ЭДО operator** (Контур, СБИС, Такском и т.д.).
- Самозанятые do everything inside **«Мой налог»** — no личный кабинет filing is needed because there is no declaration.

- **Electronic signature requirement** — Declarations filed through the личный кабинет ИП or an operator require a valid усиленная квалифицированная электронная подпись (УКЭП / КЭП). The декларация по НДС is electronic-only and cannot be filed on paper. Confirm the signature is valid and not expired before the deadline.  _(ru-return-assembly skill text, section 5 Submission)_
- **ЕНП payment & уведомления process** — Pay tax/contributions as a single ЕНП transfer to the ЕНС (or use the pre-filled payment in the личный кабинет / банк). Submit the уведомление об исчисленных суммах (КНД 1110355) for each obligation that has no same-date declaration — УСН advances, fixed страховые взносы, НДФЛ advances — by the working day before the payment date. After payment, check the ЕНС saldo in the личный кабинет to confirm the balance is positive/zero and that the ФНС allocated the ЕНП as intended.  _(КНД 1110355)_
- **Confirmation of filing** — Capture the ФНС acceptance receipt (квитанция о приёме) for every filed declaration and the ЕНС allocation, and keep them with the file.  _(ru-return-assembly skill text, section 5 Submission)_

## 6. Final pre-filing checklist

Run every applicable item before submitting. Do not file if any item fails.

- [ ] **Regime confirmed** by `ru-freelance-intake`; the correct declaration (or none, for НПД) is selected.
- [ ] **All upstream figures present** — tax (`ru-usn` / `ru-income-tax` / `ru-self-employed-npd`), страховые взносы (`ru-social-contributions`), НДС (`russia-vat`) — and **reviewer-signed-off**. No invented numbers.
- [ ] **Income reconciled** to bank statements; FX receipts converted at the ЦБ РФ rate on the date of receipt.
- [ ] **НПД only:** all чеки recorded in «Мой налог»; running annual total **under 2,400,000 ₽**; monthly payment schedule produced.
- [ ] **УСН only:** correct object («доходы» / «доходы минус расходы») and the matching разделы; **current 2026 form** confirmed; КУДиР complete; tax reduction for paid contributions reflected upstream.
- [ ] **ОСНО only:** 3-НДФЛ professional deductions supported; НДФЛ advances reconciled; КУДиР complete.
- [ ] **НДС (if applicable):** quarterly decomposition from `russia-vat` matches the declaration; filed electronically.
- [ ] **Страховые взносы:** fixed amount scheduled for **28 Dec 2026**; 1%-over-300k scheduled for **1 Jul 2027**.
- [ ] **Уведомления** prepared and timed for every ЕНП payment lacking a same-date declaration (КНД 1110355).
- [ ] **Electronic signature (УКЭП)** valid and unexpired; access to личный кабинет / ЭДО operator confirmed.
- [ ] **Deadlines re-verified** against nalog.gov.ru, including 2026 weekend shifts.
- [ ] **ЕНС saldo** checked after payment; ФНС acceptance receipts archived.
- [ ] **Escalation triggers** (ООО, non-resident, ПСН, mid-year cap breach) ruled out or escalated to a qualified Russian accountant.

## 7. Reference (form names & key 2026 deadlines)

Verify all of the following against nalog.gov.ru (ФНС) before filing; weekend shifts and form revisions change year to year.

- **НПД filing form** — No declaration — налог auto-calculated in «Мой налог»; ФНС notifies the amount by ~the 12th, payment by the 28th of the following month.  _(ru-return-assembly skill text, section 7 Returns/forms)_
- **УСН declaration form** — декларация по УСН, КНД 1152017 (object-specific разделы 1.1/2.1.1 or 1.2/2.2). Updated 2026 form per приказ ФНС от 26.11.2025 № ЕД-7-3/1017@ (form/effective-date to be confirmed at filing).  _(КНД 1152017; приказ ФНС от 26.11.2025 № ЕД-7-3/1017@)_
- **ОСНО declaration form** — 3-НДФЛ, КНД 1151020 (revision to be confirmed at filing).  _(КНД 1151020)_
- **НДС declaration form** — декларация по НДС, quarterly, electronic only.  _(ru-return-assembly skill text, section 7 Returns/forms)_
- **Уведомление об исчисленных суммах form** — КНД 1110355 (ЕНП allocation).  _(КНД 1110355)_
- **КУДиР requirement** — Maintained for УСН/ОСНО, not filed.  _(ru-return-assembly skill text, section 7 Returns/forms)_
- **УСН declaration deadline (ИП)** — 25 Apr → 28 Apr 2026 (25 Apr is Saturday)  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **УСН advance уведомления deadlines** — 27 Apr / 27 Jul / 26 Oct 2026  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **3-НДФЛ declaration and payment deadlines** — declaration: 30 Apr 2026; НДФЛ payment: 15 Jul 2026  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **НДС quarterly declaration deadlines (2026 shifts)** — 27 Apr / 27 Jul / 26 Oct 2026 (and 25 Jan 2027 for Q4 2026)  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **Страховые взносы deadlines** — fixed: 28 Dec 2026; 1% over 300,000 ₽: 1 Jul 2027  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **ЕНП tax payments deadline** — generally tied to the 28th of the month  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_
- **НПД tax payment deadline** — monthly by the 28th of the following month  _(ru-return-assembly skill text, section 7 Key 2026 deadlines)_

## Disclaimer

This skill performs **orchestration and assembly only** and computes no tax, contributions, or НДС. It selects the correct declaration, lays out the filing and ЕНП/ЕНС payment calendar, and runs the pre-filing checklist; every monetary figure originates from the upstream content skills. **All figures, regime determinations, form revisions, and deadlines must be reviewed and signed off by a qualified Russian accountant (бухгалтер / налоговый консультант) and verified against nalog.gov.ru (ФНС) before anything is filed.** The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## 4. Filing & payment calendar (tax year 2026)

****Annual declaration****  _(**3-НДФЛ** — by **30 Apr 2026**)_

None — auto-calc in «Мой налог»

****Main tax payment****  _(НДФЛ annual balance by **15 Jul 2026**; advances by 28th after each quarter)_

Monthly via app/ЕНП, by **28th** of following month

****Advance уведомления****  _(НДФЛ advance уведомления by the 25th preceding each 28th payment)_

Not applicable

****Страховые взносы — fixed****  _(Fixed amount via ЕНП by **28 Dec 2026**)_

Voluntary only

****Страховые взносы — 1% over 300k****  _(By **1 Jul 2027** (for 2026 income))_

Not applicable

****НДС (if applicable)****  _(Quarterly декларация by 25th (same 2026 shifts); pay in thirds by the 28th, **electronic filing only**)_

Never

## Workflow orchestration sequence

0. **Step 1: Intake routing** — Confirm routing from ru-freelance-intake before assembling the filing package.
0. **Step 2: НПД figures** — Consume confirmation from ru-self-employed-npd that tax is auto-calculated.
0. **Step 3: УСН figures** — Consume annual tax and quarterly advance amounts from ru-usn.
0. **Step 4: ОСНО figures** — Consume НДФЛ figures from ru-income-tax.
0. **Step 5: Social contributions** — Consume страховые взносы figures from ru-social-contributions for an ИП.
0. **Step 6: VAT figures** — Consume НДС figures and quarterly decomposition from russia-vat.
0. **Step 7: Assemble filing package** — Assemble the declarations, payment calendar, and ЕНП/ЕНС reconciliation using all upstream figures.
0. **Step 8: Pre-filing checklist** — Run the final pre-filing checklist and escalate to a qualified Russian accountant if any item fails.

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
