---
name: eg-return-assembly
description: Use this skill as the final orchestrator that assembles the complete Egyptian filing package for an Egypt-resident self-employed person. It computes nothing itself — it sequences and stitches together the Egypt content skills into one reviewer-ready filing package (income tax return, VAT returns, social insurance, e-invoicing precondition, ETA submission). Trigger on phrases like "file my Egyptian tax return", "submit income tax return Egypt", "ETA filing", "assemble my Egypt return", "قدّم الإقرار الضريبي", "إقرار ضريبة الدخل مصر".
version: 0.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - eg-freelance-intake
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Return Assembly

## Egypt Return Assembly — Filing Package Orchestrator (تجميع الإقرار الضريبي المصري)

## 1. What this file is

This is the **final orchestrator (المُجمِّع النهائي)** for an Egypt-resident self-employed person (مهني / صاحب نشاط تجاري). It **assembles the filing package** — it does **not compute** any figure. Every number comes from the upstream content skills; this file decides *which return applies*, *what schedules attach*, *when each filing is due*, and *how to submit through the ETA portal*.

The Egyptian Tax Authority (**ETA — مصلحة الضرائب المصرية**, eta.gov.eg) is the single authority for income tax and VAT. The National Organisation for Social Insurance (**NOSI — الهيئة القومية للتأمينات الاجتماعية**) handles social insurance.

AI replies in the **user's language** (Arabic or English). Native Arabic terms appear throughout so the package reads naturally for an Egyptian reviewer.

> **Precondition (شرط مسبق):** e-invoicing / e-receipt compliance. See Section 3. Without it, the simplified regime is unavailable and input VAT credit can be disallowed.

## 2. Inputs required

Collect these from `eg-freelance-intake` before assembling. Do not re-interrogate scope the intake already settled.

**Inputs required table**  _(eg-freelance-intake)_

| Input | Source skill | Used for |
| --- | --- | --- |
| Residency confirmation, activity type (professional vs commercial) | `eg-freelance-intake` | Routing the return |
| Annual turnover (إجمالي الأعمال) in EGP | `eg-freelance-intake` / `egypt-vat` | Simplified vs general decision; VAT registration |
| ETA Tax Registration Number (رقم التسجيل الضريبي) | intake | All ETA filings |
| National ID (الرقم القومي) | intake | ETA portal account |
| Net profit on commercial/professional activity | `eg-income-tax` | General return |
| Turnover-based liability figures | `eg-sme-tax` | Simplified return |
| VAT output/input position, e-invoice UUIDs | `egypt-vat` | VAT return(s) |
| Social insurance contribution wage & status | `eg-social-insurance` | NOSI filing |
| e-invoice / e-receipt registration status | `egypt-vat` / intake | Precondition gate |
| ETA portal credentials, digital signature (token) | intake | Submission |

- **Missing content skill output handling** — If a content skill did not run or returned no validated output, note the gap in the reviewer brief and continue with available data rather than halting.  _(Section 2, Egypt Return Assembly)_

## 3. Decision tree — which return applies

```
START
  │
  ├─ Is e-invoice + e-receipt compliance in place?
  │     NO  ─► Simplified regime UNAVAILABLE. Flag precondition failure.
  │           Default to GENERAL return. Note remediation in reviewer brief.
  │     YES ─► continue
  │
  ├─ Annual turnover ≤ EGP 20,000,000 AND a formal election
  │   to join Law No. 6 of 2025 was filed (and 5-yr lock-in accepted)?
  │
  ├── YES ─► SIMPLIFIED REGIME (نظام مبسّط — Law No. 6 of 2025)
  │            • Return: simplified turnover-based annual income tax return
  │              (separate form from the standard return — via eg-sme-tax)
  │            • VAT: QUARTERLY return (if VAT-registered) — within one
  │              month after each quarter (via egypt-vat)
  │            • Liability is turnover-based; eg-sme-tax holds the bands.
  │              (Do not restate rates here.)
  │
  └── NO  ─► GENERAL REGIME (النظام العام)
               • Return: standard annual individual income tax return
                 — net profit on commercial/professional activity
                 (via eg-income-tax)
               • Filed by 31 March (individuals) following the tax year
               • VAT: MONTHLY return (if VAT-registered) — via egypt-vat
               • Attach activity P&L / accounts as schedules

ALWAYS (both branches):
   • Social insurance filing/registration with NOSI (via eg-social-insurance)
   • e-invoicing / e-receipt running and reconciled
```

### Routing notes

- **Simplified regime is an election** — The simplified regime is an election, not automatic. Eligibility is turnover ≤ EGP 20m, but the taxpayer must have formally requested it and accepted the ~5-year lock-in. If no election exists, use the general return.  _(Section 3, Egypt Return Assembly, Routing notes)_
- **VAT registration independent of income-tax regime** — VAT registration is independent of the income-tax regime. Confirm registration status from `egypt-vat` (the registration threshold tightened in 2026 — verify the current threshold in `egypt-vat`; do not hard-code it here).  _(Section 3, Egypt Return Assembly, Routing notes)_
- **Professional vs commercial activity** — Professional vs commercial: both file the general individual return when not in the simplified regime; `eg-income-tax` handles the distinction.  _(Section 3, Egypt Return Assembly, Routing notes)_

## 4. Filing & payment calendar

All filings are electronic via the ETA portal; payment is electronic at the time of filing. e-invoicing/e-receipt compliance is a precondition running underneath the whole calendar.

**Filing & payment calendar table**  _(Section 4, Egypt Return Assembly)_

| Filing | Regime | Frequency | Deadline | Source skill |
| --- | --- | --- | --- | --- |
| Individual income tax return (الإقرار السنوي) | General | Annual | **31 March** following the tax year (individuals) | `eg-income-tax` |
| Simplified turnover-based return | Simplified (Law 6/2025) | Annual | Per the Unified Tax Procedures Law due date — **verify on ETA** | `eg-sme-tax` |
| VAT return (إقرار ض.ق.م) | General | **Monthly** | By the end of the following month *(see note)* | `egypt-vat` |
| VAT return | Simplified | **Quarterly** | Within **one month** after each quarter | `egypt-vat` |
| Social insurance (تأمينات اجتماعية) | Both | Per NOSI schedule (typically monthly) | Per NOSI rules — confirm | `eg-social-insurance` |
| e-invoice / e-receipt reporting | Both (precondition) | Real-time | Same day the document is issued | `egypt-vat` |

> **VAT deadline — flag (uncertainty).** Sources disagree. The ETA-practice and the `egypt-vat` skill state **end of the following month**. VAT Law No. 67 of 2016 / PwC describe a statutory window of **two months after the tax period, with the April return due by 15 June**. Use the **earlier (end of following month)** conservatively and **confirm the exact monthly deadline with the reviewer / on eta.gov.eg** before filing.

> **Simplified-return due date — flag.** The simplified annual return uses the due date in the Unified Tax Procedures Law and a separate form; the precise 2026 calendar date was **not verifiable** at time of writing — confirm on ETA.

## 5. Submission (ETA portal & digital signature)

0. **Account login** — Account — log in to the ETA online portal (eta.gov.eg) using the National ID (الرقم القومي) or the Tax Registration Number (رقم التسجيل الضريبي). Electronic filing is mandatory for these taxpayers.
0. **Select the correct form** — Select the correct form — general individual return or the simplified turnover-based return (do not file both); plus the VAT return at the correct frequency for the chosen regime.
0. **Attach schedules** — Attach schedules — activity accounts / P&L, VAT reconciliation, and any supporting workpapers produced by the content skills.
0. **Digital signature** — Digital signature (التوقيع الإلكتروني) — sign with the ETA-recognised electronic signature / token where required. Confirm the signing certificate is valid and not expired before submission.
0. **Pay electronically** — Pay electronically — settle the tax due at the time of filing through the portal's payment channels.
0. **Capture confirmation** — Capture confirmation — save the ETA submission reference / acknowledgment for the file. Do not consider a return filed until acknowledgment is received.

## 6. Final pre-filing checklist

- [ ] Intake (`eg-freelance-intake`) complete; residency & activity type confirmed.
- [ ] **e-invoice + e-receipt** compliance verified (precondition gate passed).
- [ ] Regime decided via Section 3 (general vs simplified) and election status
      confirmed for simplified.
- [ ] Correct income-tax form selected (general return *or* simplified return —
      never both).
- [ ] Income figures reconciled: VAT turnover ↔ income-tax gross/net (flag any
      mismatch for the reviewer).
- [ ] VAT returns prepared at the correct frequency (monthly = general /
      quarterly = simplified) and all e-invoice UUIDs present.
- [ ] Social insurance (NOSI) registration current and contributions reconciled.
- [ ] Deadlines mapped to dates (Section 4); VAT monthly deadline confirmed.
- [ ] Digital signature certificate valid; ETA portal credentials working.
- [ ] Payment method ready; expected tax due figure available from content skills.
- [ ] All open flags (VAT deadline, simplified due date, any data gaps) listed in
      the reviewer brief.
- [ ] Package routed for **qualified Egyptian accountant (محاسب قانوني)** sign-off
      before any submission.

## 7. Reference (forms, deadlines, sources)

**Reference table**  _(Section 7, Egypt Return Assembly)_

| Item | Reference / value | Status |
| --- | --- | --- |
| Individual income tax return deadline | **31 March** following the tax year | Verified (ETA / PwC) |
| Sole proprietorship / partnership deadline | 30 April (where applicable) | Verified (secondary) |
| Simplified regime | Law No. 6 of 2025 (turnover ≤ EGP 20m; separate form; ~5-yr lock-in) | Verified (EY / law firms) |
| Simplified VAT frequency | Quarterly, within 1 month after quarter | Verified (Law 6/2025 commentary) |
| General VAT frequency | Monthly | Verified |
| General VAT deadline | End of following month **vs** 2-month statutory window (April → 15 June) | **Conflicting — confirm** |
| VAT Law | No. 67 of 2016 + Executive Regulations | Verified |
| Social insurance | Law No. 148 of 2019 (NOSI) | Verified |
| e-invoicing / e-receipt | ETA mandate; precondition for simplified regime; same-day reporting | Verified |
| ETA portal | https://www.eta.gov.eg ; e-invoice: https://invoicing.eta.gov.eg | Verified |

**Could not verify / flag for reviewer:**
- Exact monthly VAT deadline (end of following month vs two-month statutory rule).
- Exact 2026 calendar due date and form code for the simplified turnover-based
  return.
- Current 2026 VAT registration threshold (defer to `egypt-vat`; reportedly
  lowered in 2026 — confirm).
- Whether digital signature is mandatory for *every* individual return or only
  certain filings — confirm with the reviewer / ETA.

## Disclaimer

This skill performs **orchestration and assembly only** — it computes no tax figures. All amounts originate from the Egypt content skills (`eg-freelance-intake`, `eg-income-tax`, `eg-sme-tax`, `egypt-vat`, `eg-social-insurance`) and **must be reviewed and signed off by a qualified Egyptian accountant (محاسب قانوني)** before anything is filed with the ETA or NOSI. Deadlines, forms, thresholds, and the simplified-regime election rules change frequently; verify every flagged item against eta.gov.eg at filing time. Nothing here is tax, legal, or financial advice.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
