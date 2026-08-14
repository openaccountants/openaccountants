---
name: ua-return-assembly
description: "Final orchestrator that assembles the complete Ukrainian ФОП (FOP) filing package for a Ukraine-resident sole proprietor: consumes the Ukraine content-skill outputs and produces one unified reviewer package with the correct declaration, schedules, filing-and-payment calendar, and pre-filing checklist. Computes nothing itself."
version: 0.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - ua-freelance-intake
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UA Return Assembly

## Ukraine FOP Return-Assembly Orchestrator v0.1

## 1. What this file is

This is the capstone skill for the Ukraine self-employed (ФОП / FOP) workflow. It runs **last**, after intake and after the content skills have produced their numbers.

It **computes nothing**. Its job is to:

- pick the correct declaration based on the regime,
- gather every content-skill output into one reviewer package,
- lay out the filing-and-payment calendar by group,
- describe submission via the Електронний кабінет with a КЕП, and
- run the final pre-filing checklist.

All tax figures come from the content skills. This orchestrator only sequences, reconciles, and packages. Every number is provisional until a qualified Ukrainian accountant reviews and signs off.

Do not re-interrogate scope that `ua-freelance-intake` already validated (ФОП vs ТОВ, simplified vs general, group, VAT status, residency). Trust the intake package; cross-check specific numbers during reconciliation only.

## 2. Inputs required

**The structured intake package** from `ua-freelance-intake`:
- ФОП status confirmed; regime (simplified single tax vs general system); group (1, 2, or 3) if simplified; VAT registration status; confirmed Ukrainian tax residency for the year.
- КВЕД activity codes; bank-statement-derived income (FX converted to UAH at the NBU rate on the date of receipt); flags for barred activities or approach to the group income cap.

**Per-skill outputs** (whichever apply to the regime):
- `ua-single-tax` — single-tax liability and the 1% military levy where applicable; group, period, and rate (Group 1/2 fixed; Group 3 percentage 3% VAT-registered / 5% non-VAT).
- `ua-income-tax` — general-system net taxable income, 18% PIT and 5% military levy (general-system FOPs only).
- `ua-social-contributions` — ЄСВ (unified social contribution) "for self," by quarter, at 22% of the contribution base with the monthly minimum, plus any exemption (pensioner, disability, employed elsewhere as primary job, mobilised).
- `ukraine-vat` — VAT return box values and net VAT payable/refundable (registered FOPs only).

If a required output is missing, halt and route back to the relevant content skill before assembling.

## 3. Decision tree — which declaration, which schedules

```
Is the FOP on the SIMPLIFIED system (single tax)?
│
├── YES → Декларація платника єдиного податку
│         (single-tax payer declaration, MoF Order No. 578)
│         │
│         ├── Group 1 or 2 → ANNUAL declaration
│         │     + Додаток 1 (ЄСВ "for self") where ЄСВ was paid
│         │     + monthly single tax & military levy paid by the 20th
│         │
│         └── Group 3 → QUARTERLY declaration (cumulative within the year)
│               + Додаток 1 (ЄСВ "for self")
│               + ukraine-vat return separately if VAT-registered (3% rate)
│
└── NO (GENERAL system) → Декларація про майновий стан і доходи
          (property-status-and-income declaration) — ANNUAL
          + the FOP business-income section (18% PIT + 5% military levy)
          + ЄСВ "for self" reported via the quarterly combined report (see §4)
          + ukraine-vat return separately if VAT-registered
```

Notes:
- The single-tax declaration and the property-and-income declaration are **mutually exclusive** for the period — a FOP is on exactly one regime.
- ЄСВ "for self" is now reconciled through the **quarterly combined report** (об'єднана звітність з ЄСВ, ПДФО та військовим збором). For simplified FOPs, ЄСВ "for self" continues to be declared via Додаток 1 to the single-tax declaration; the combined report covers ЄСВ/PIT/military-levy where the FOP has **employees** or pays individuals.
- VAT is always its own return on its own monthly cycle; it is never folded into the income or single-tax declaration.

## 4. Filing & payment calendar (tax year 2026)

**Filing & payment calendar (tax year 2026)**

Standard rule: if a deadline falls on a weekend or public holiday, it moves to the next working day. Dates below already reflect 2026 weekend shifts where confirmed.

**Filing & payment calendar table**  _(MoF Order No. 578; tax.gov.ua)_

| Obligation | Group 1 & 2 (simplified) | Group 3 (simplified) | General system |
| --- | --- | --- | --- |
| **Single-tax / income declaration — filing** | Annual: by **2 Mar 2026** (for 2025; 1 Mar is Sunday) | Quarterly, within 40 days of quarter-end: Q1 by **11 May 2026**, Q2 by **10 Aug 2026**, Q3 by **9 Nov 2026**, Q4/annual by **9 Feb 2027** | Annual property-and-income declaration: by **1 May 2026** (for 2025) |
| **Single tax — payment** | **Monthly**, by the **20th** of each month (advance payment) | **Quarterly**, within 10 days of the filing deadline: Q1 by ~20 May, Q2 by ~20 Aug, Q3 by ~19 Nov, Q4 by ~19 Feb 2027 | n/a (pays PIT instead) |
| **PIT (18%)** | n/a | n/a | Final settlement by **10 May 2026** (10 days after filing); advance instalments during the year |
| **Military levy** | Built into the single-tax regime; paid monthly with single tax (by the 20th) | 1% of income, paid quarterly within 10 days of the filing deadline | 5% of net income, settled with PIT by **10 May 2026** |
| **ЄСВ (unified social contribution, "for self")** | **Quarterly**, by the 20th of the month after the quarter: Q1 by **20 Apr 2026**, Q2 by **20 Jul 2026**, Q3 by **19 Oct 2026**, Q4 by **19 Jan 2027** | Same quarterly schedule as Group 1&2 | Same quarterly schedule |
| **VAT return (if registered)** | Monthly: within **20 days** after the reporting month | Same — monthly within 20 days | Same — monthly within 20 days |
| **VAT payment (if registered)** | Within **10 days** after the return filing deadline (~30th of the following month) | Same | Same |

**2026 reporting change — abolition of the separate monthly report:** From 1 January 2026 the separate **monthly** ЄСВ / PIT / military-levy calculation (Податковий розрахунок) is abolished for FOPs and self-employed persons. It is replaced by a **quarterly combined report** (об'єднана звітність), first due for Q1 2026 within 40 calendar days of quarter-end (i.e. by ~10–11 May 2026). The report is one quarterly form that still breaks the figures out month-by-month inside it. The monthly cycle remains only for legal entities. Confirm the FOP files the combined report only where it has employees / pays individuals; a FOP with no employees declares ЄСВ "for self" through the declaration's Додаток 1.

> The exact ЄСВ minimum, single-tax fixed amounts, and military-levy figures for 2026 come from the content skills, not this orchestrator. Do not hard-code them here.

## 5. Submission — Електронний кабінет + КЕП

All FOP declarations and reports are filed **electronically** through the State Tax Service's **Електронний кабінет** (cabinet.tax.gov.ua) — or an accredited e-reporting provider (Вчасно, M.E.Doc, Соната, Taxer, etc.).

Process:
1. **Authenticate** to the Електронний кабінет with a **КЕП** (кваліфікований електронний підпис — qualified electronic signature). The КЕП identifies the FOP and is mandatory for signing.
2. Open **«Ведення звітності»** (reporting), select the correct form for the period:
   - Декларація платника єдиного податку (single-tax payer declaration) — simplified FOPs; or
   - Декларація про майновий стан і доходи (property-and-income declaration) — general-system FOPs; plus
   - the **об'єднана звітність** (quarterly combined report) if there are employees; and
   - the VAT return (Податкова декларація з ПДВ) if registered.
3. Attach the relevant додатки (e.g. **Додаток 1** for ЄСВ "for self").
4. **Sign with the КЕП** and submit.
5. Wait for **two receipts (квитанції)**:
   - **Квитанція №1** — confirms delivery to the tax authority's receiving system.
   - **Квитанція №2** — the acceptance receipt. The report is **officially filed only when Квитанція №2 reads «Прийнято» (Accepted).**
6. Pay the liabilities by the payment deadlines in §4 (filing and payment are separate dates).

Store both квитанції with the package as proof of filing. A missing or rejected Квитанція №2 means the report is **not** filed — resolve the rejection reason and resubmit before the deadline.

## 6. Final pre-filing checklist

- [ ] Regime confirmed from the intake package: simplified (group 1/2/3) **or** general system — exactly one.
- [ ] Correct declaration selected per §3 (single-tax payer declaration vs property-and-income declaration).
- [ ] All applicable content-skill outputs present: `ua-single-tax` **or** `ua-income-tax`; `ua-social-contributions`; `ukraine-vat` if registered.
- [ ] FX income converted to UAH at the NBU rate on the date of receipt; total income reconciles to bank statements.
- [ ] No barred activity (excisable goods, FX exchange, financial services, gambling, mineral extraction) and the group income cap not breached.
- [ ] ЄСВ "for self" computed for every quarter, with any exemption (pensioner, disability, employed-elsewhere, mobilised) documented.
- [ ] Додаток 1 (ЄСВ) attached where ЄСВ was paid.
- [ ] Single tax + military levy reconciled to the regime and group.
- [ ] If employees/payments to individuals: quarterly **combined report** prepared (not the abolished monthly form).
- [ ] VAT return box values reconciled to turnover; net VAT payable/refundable agreed (registered FOPs).
- [ ] Filing and payment dates from §4 mapped to a concrete action list with amounts.
- [ ] КЕП valid and not expired; access to the Електронний кабінет confirmed.
- [ ] Two receipts captured after submission; **Квитанція №2 = «Прийнято»** for every report.
- [ ] Qualified Ukrainian accountant has reviewed and signed off **before** filing.

## 7. Reference Material

**Declarations & forms**
- Декларація платника єдиного податку (single-tax payer declaration) — MoF Order No. 578; annual for Groups 1&2, quarterly cumulative for Group 3; Додаток 1 = ЄСВ "for self".
- Декларація про майновий стан і доходи (property-status-and-income declaration) — general-system FOPs and individuals; updated form per MoF order effective 06.02.2026.
- Об'єднана звітність з ЄСВ, ПДФО та військовим збором — quarterly combined report (replaces the abolished monthly Податковий розрахунок from 1 Jan 2026); for FOPs with employees / payments to individuals.
- Податкова декларація з ПДВ — monthly VAT return for registered FOPs.

**Key 2026 deadlines (verify each against tax.gov.ua before filing)**
- Group 1&2 single-tax declaration (2025): by **2 Mar 2026**.
- Group 3 single-tax declaration: quarterly within 40 days — Q1 **11 May 2026**, Q2 **10 Aug 2026**, Q3 **9 Nov 2026**, Q4 **9 Feb 2027**.
- General-system property-and-income declaration (2025): by **1 May 2026**; PIT + military levy settled by **10 May 2026**.
- ЄСВ "for self" (quarterly): Q1 **20 Apr 2026**, Q2 **20 Jul 2026**, Q3 **19 Oct 2026**, Q4 **19 Jan 2027**.
- Single tax: Group 1&2 monthly by the **20th**; Group 3 quarterly within 10 days of the filing deadline.
- VAT: file within **20 days** of month-end, pay within a further **10 days** (registered only).

**Submission**
- Електронний кабінет — cabinet.tax.gov.ua; sign with **КЕП**; report filed only on **Квитанція №2 «Прийнято»**.

**Authority**
- State Tax Service of Ukraine — tax.gov.ua / dps.gov.ua.

*Figures, rates, and minimum-base amounts are owned by the content skills, not this orchestrator. Deadlines shift to the next working day on weekends/holidays — re-verify each year.*

## Disclaimer

This skill performs **orchestration only**: it selects the correct declaration, sequences the content skills, builds the calendar, and packages the result. It computes no tax. Every figure, schedule, and return assembled here is **provisional** and must be reviewed and signed off by a **qualified Ukrainian accountant or auditor** before it is filed with the State Tax Service. Deadlines and form references reflect rules as understood for tax year 2026 and must be re-verified against tax.gov.ua / dps.gov.ua at filing time. The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## 2. Inputs required

0. **Intake package input** — Consume structured intake package
0. **Single tax skill invocation** — Consume single-tax liability output
0. **Income tax skill invocation** — Consume general-system PIT/military levy output
0. **Social contributions skill invocation** — Consume ЄСВ output by quarter
0. **VAT skill invocation** — Consume VAT return box values and net VAT payable/refundable

## 3. Decision tree — which declaration, which schedules

0. **Select declaration** — Select correct declaration and schedules per decision tree

## 4. Filing & payment calendar (tax year 2026)

0. **Build calendar** — Lay out filing-and-payment calendar by group

## 5. Submission — Електронний кабінет + КЕП

0. **Submission guidance** — Describe submission via Електронний кабінет with КЕП

## 6. Final pre-filing checklist

0. **Run checklist** — Run final pre-filing checklist

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
