---
name: eg-return-assembly
description: Use this skill as the final orchestrator that assembles the complete Egyptian filing package for an Egypt-resident self-employed person. It computes nothing itself; it sequences and stitches together the Egypt content skills into one reviewer-ready filing package (income tax return, VAT returns, social insurance, e-invoicing precondition, ETA submission). Trigger on phrases like "file my Egyptian tax return", "submit income tax return Egypt", "ETA filing", "assemble my Egypt return", "قدّم الإقرار الضريبي", "إقرار ضريبة الدخل مصر".
version: 0.2
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - eg-freelance-intake
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
---

# EG Return Assembly v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Egypt return assembly (تجميع الإقرار الضريبي المصري), tax year 2026, law as read on 16 November 2026. This is the final orchestrator (المُجمِّع النهائي) for an Egypt-resident self-employed person (مهني / صاحب نشاط تجاري). It assembles the filing package and computes no figure: every number comes from the content skills. It decides which return applies, what attaches, when each filing is due and how it is submitted. Reply in the user's language, Arabic or English, and keep native Arabic terms so the package reads naturally for an Egyptian reviewer.

Authorities: the Egyptian Tax Authority (ETA, مصلحة الضرائب المصرية, eta.gov.eg) for income tax, VAT and payroll tax; the National Organization for Social Insurance (NOSI, الهيئة القومية للتأمين الاجتماعي) for contributions.

**Answer first.** For tax year 2026 an individual files the annual income tax return between 1 January and 31 March 2027 (before 1 April), on the general return or, in the turnover regime, on form 20 إقرارات. VAT is monthly on the general system and quarterly in the turnover regime, each within the month after the period. Joining the ETA e-invoice or e-receipt system under its phase decisions is a condition of the turnover regime.

## Scope

- **In:** a resident individual, sole proprietor or professional, whose facts `eg-freelance-intake` has confirmed. Both income tracks: the general system (`eg-income-tax`) and the turnover regime under Law 6 of 2025 (`eg-sme-tax`); VAT under VAT Law 67 of 2016 and its executive regulations (`egypt-vat`); payroll (`eg-payroll`) and social insurance under Law 148 of 2019 (`eg-social-insurance`); records (`eg-bookkeeping`).
- **Out:** companies (`eg-corporate-tax`, `eg-financial-statements`), non-residents, partnerships, and any computation (the content skills own every figure).

## Ask the client first

Take these from `eg-freelance-intake`; do not re-ask what the intake settled.

| Input | Source skill | Used for |
|---|---|---|
| Residence, activity type (professional or commercial) | `eg-freelance-intake` | Routing the return |
| Annual turnover (إجمالي الأعمال / حجم الأعمال) in EGP | `eg-freelance-intake`, `egypt-vat` | Turnover regime or general system; VAT registration |
| ETA tax registration number (رقم التسجيل الضريبي) | intake | Every ETA filing |
| National ID (الرقم القومي) | intake | ETA system account |
| Net profit of the commercial or professional activity | `eg-income-tax` | General return |
| Turnover tax figures | `eg-sme-tax` | Form 20 return |
| VAT output and input, e-invoice identifiers | `egypt-vat` | VAT returns |
| Contribution wage and status | `eg-social-insurance` | NOSI payments |
| Staff pay and tax withheld | `eg-payroll` | Payroll returns |
| E-invoice or e-receipt registration status | `eg-bookkeeping`, intake | Turnover regime condition |
| ETA system user name and password; accountant registered on the system | intake | Submission |

If a content skill did not run or returned no validated output, record the gap in the reviewer brief and continue with the data available rather than halting.

## The method, step by step

### Step 1. Decide which income return applies

```
START
  |
  +- Turnover up to EGP 20,000,000 AND (request form 10/1 filed,
  |  or business moved over from Law 152 of 2020) AND not excluded
  |  (90% consultancy test, improper splitting)?
  |
  +-- YES -> TURNOVER REGIME (Law 6 of 2025)
  |           - Condition: returns on time, and joined to the ETA
  |             e-systems, e-invoice or e-receipt, under the phase
  |             decisions, with documents actually issued (art. 3).
  |             If the condition fails, flag it for the reviewer.
  |           - Income: annual return on form 20 إقرارات (via eg-sme-tax)
  |           - VAT, if registered: QUARTERLY, within the month after
  |             the quarter, with payment (via egypt-vat)
  |           - Payroll: annual settlement return only, with payment
  |
  +-- NO  -> GENERAL SYSTEM (النظام العام)
              - Income: annual individual return with every table
                of the form, net profit of the activity (via eg-income-tax)
              - VAT, if registered: MONTHLY, within the month after
                the month (via egypt-vat)
              - Payroll, if staff: quarterly returns and the January
                annual settlement (via eg-payroll)

ALWAYS (both branches):
   - Social insurance with NOSI (via eg-social-insurance)
   - E-invoice or e-receipt documents issued and reconciled
```

Routing notes:

- The turnover regime is an election, not automatic: Law 6 art. 1 covers projects that ask for it. The request is form 10/1 طلبات (MoF Decision 420 of 2025 art. 1). Leaving is possible only after five years from the day after the request (Law 6 art. 5), on form 11/1 طلبات. Without a request, and unless the business moved over from Law 152 of 2020, use the general return.
- VAT registration does not depend on the income regime. Take registration status and the limit from `egypt-vat`; do not hard-code them here.
- Professional and commercial activity both use the individual return on the general system; `eg-income-tax` handles the difference.

### Step 2. Map the filing and payment calendar

All returns go through the ETA electronic system. E-invoice and e-receipt compliance runs underneath the whole calendar.

| Filing | Track | Frequency | Deadline (tax year 2026) | Source |
|---|---|---|---|---|
| Individual income tax return (الإقرار السنوي) with all tables | General | Annual | Before 1 April 2027; a return missing tables does not count as filed | Law 206 of 2020 art. 31(c): https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Turnover regime return, form 20 إقرارات | Turnover regime | Annual | Same dates as the general return: 1 January to 31 March 2027 for an individual | Law 6 art. 12: https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf; MoF 420 art. 2: https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf |
| VAT return (إقرار ض.ق.م) | General | Monthly, even with no sales | Within the month after the month | Law 206 art. 31(a): https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| VAT return | Turnover regime | Quarterly | Within the month after the quarter, with payment | Law 6 art. 12: https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Payroll tax, quarterly return | General, with staff | Quarterly | In January, April, July and October | Law 206 art. 31(b): https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Payroll tax, annual settlement | Both, with staff | Annual | During January; in the turnover regime this is the only payroll return, with payment | Law 206 art. 31(b); Law 6 art. 12: https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Social insurance (تأمينات اجتماعية) | Both | Monthly | Due date and grace period in `eg-social-insurance` | Law 148 of 2019 art. 121, as read in `eg-social-insurance` |
| E-invoice and e-receipt documents | Both | As issued | Timing rules in `eg-bookkeeping` | ETA e-invoice and e-receipt rules, as read in `eg-bookkeeping` |

A first return counts as notice of starting the activity, and a return is still due for a period in which the taxpayer is exempt (Law 206 art. 31). No annual return is needed where income is only salary, or only real estate income within the exempt band, or only those two within that band (same article).

### Step 3. Assemble the package

1. Intake summary from `eg-freelance-intake`, with the route and its facts.
2. Income: the general return workpapers from `eg-income-tax` (receipts, deductible costs, depreciation, net profit, bands, credits), or the turnover figure and band from `eg-sme-tax` for form 20.
3. VAT: one reconciliation per period from `egypt-vat`, with every e-invoice identifier. Input VAT on purchases needs the supplier's e-invoice, or the credit can be disallowed (`eg-bookkeeping`).
4. Payroll and social insurance schedules, if there are staff.
5. A reconciliation of VAT turnover to income tax turnover; flag every difference for the reviewer.
6. The reviewer brief: open flags, data gaps, judgement calls.

### Step 4. Submit through the ETA system

1. **Log in.** Merged tax offices use the ETA electronic tax system; offices not yet merged use https://eservice.incometax.gov.eg/etax (ETA Services Guide, section 18/2). The ETA front offices help with registering on the portal, registering the accountant and the agent on the system to approve the return, and uploading returns (Services Guide, service 2/1).
2. **Pick the form.** General return or form 20, never both, plus the VAT return at the frequency of the track.
3. **Complete every table.** A return without all its tables and data is not counted as filed on time (Law 206 art. 31(c)).
4. **Attach schedules.** Activity accounts or profit and loss, the VAT reconciliation, and supporting workpapers.
5. **Have the registered accountant approve the return** on the system where the client uses one (Services Guide, service 2/1).
6. **Pay.** Payment runs through a payment claim (مطالبة) linked to the ETA system, by card (Services Guide, service 2/1). For VAT, `egypt-vat` sets out paying by claim number after filing.
7. **Keep the confirmation.** Save the submission reference. A return is not treated as filed until the system acknowledges it.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| Turnover regime request never filed | General return; Law 6 covers only projects that ask | Law 6 art. 1 |
| Business was under Law 152 of 2020 small-enterprise tax | Moved to Law 6 without a request | ETA Services Guide 18/2 |
| Consultant with 90% or more of turnover from one or two persons | Outside Law 6; general return | Law 6 art. 4(1) |
| Not joined to the e-systems under the phase decisions, or late returns | Breaks the Law 6 art. 3 conditions; flag for the reviewer before using form 20 | Law 6 art. 3 |
| Sole proprietor asks for a 30 April date | No: a natural person files before 1 April; before 1 May (or within four months of the year end) is for legal persons | Law 206 art. 31(c) |
| Return filed without all tables | Not counted for the deadline | Law 206 art. 31(c) |
| Late return or payment | Fines in `eg-income-tax` (Law 206 arts. 69, 70); late returns also break the Law 6 art. 3 condition | Law 206; Law 6 |

## Worked cases

**Case 1. Turnover regime developer, first VAT quarter of 2026.** A developer in the turnover regime has turnover of EGP 1,200,000 for 2026. The band from `eg-sme-tax` is 0.5%, so form 20 shows EGP 6,000, due by 31 March 2027. In the first quarter of 2026 the developer made taxable sales of EGP 300,000 at the 14% rate from `egypt-vat`, and holds e-invoices for EGP 7,000 of input VAT. Output is EGP 42,000 and the quarterly return, due with payment by 30 April 2026, shows EGP 35,000.

```oa-check
name: Turnover regime developer, annual return and first VAT quarter
inputs:
  turnover: 1200000
  band_rate: 0.005
  q1_taxable_sales: 300000
  vat_rate: 0.14
  q1_input_vat: 7000
steps:
  - form_20_tax: turnover * band_rate
  - q1_output_vat: q1_taxable_sales * vat_rate
  - q1_vat_payable: q1_output_vat - q1_input_vat
expected:
  form_20_tax: 6000.00
  q1_output_vat: 42000.00
  q1_vat_payable: 35000.00
```

On the general system the same developer would file the individual return by 31 March 2027 and twelve monthly VAT returns.

## When to refuse or refer

- Refuse to file both the general return and form 20 for the same year.
- Refuse to present the package as filed, or as a professional sign-off. Route it for sign-off by a qualified Egyptian accountant (محاسب قانوني) before any submission to the ETA or NOSI.
- Refer companies, partnerships, non-residents, free zone projects and any open examination, dispute or settlement (see `eg-tax-optimization` for the dispute committees).
- Refer where a content skill returned no validated output for a figure the return needs.

## Filing and payment

Returns and payments go through the ETA electronic system (Step 4). Turnover regime VAT is paid with the quarterly return (Law 6 art. 12). On the general system, VAT is paid after the return through the claim the system issues (`egypt-vat`). Social insurance is paid to NOSI as set out in `eg-social-insurance`.

## Completion checklist

- [ ] Intake from `eg-freelance-intake` complete; residence and activity confirmed.
- [ ] E-invoice or e-receipt status checked against the ETA phase decisions (Law 6 art. 3 condition for the turnover regime).
- [ ] Track decided under Step 1, with the form 10/1 request date (or the Law 152 move) recorded for the turnover regime.
- [ ] One income tax form only: the general return or form 20.
- [ ] VAT turnover reconciled to income tax turnover; differences flagged.
- [ ] VAT returns at the right frequency (monthly general, quarterly turnover regime) with all e-invoice identifiers.
- [ ] Payroll returns and NOSI contributions reconciled, if there are staff.
- [ ] Deadlines mapped to dates from Step 2.
- [ ] Every table of the return form completed.
- [ ] ETA system access working; accountant registered to approve the return where used.
- [ ] Payment route ready; tax due taken from the content skills.
- [ ] Every open flag listed in the reviewer brief.
- [ ] Package routed for sign-off by a qualified Egyptian accountant before submission.

## Sources

| Source | URL | Read on |
|---|---|---|
| Unified Tax Procedures Law 206 of 2020, arts. 25 to 28, 31, 38, 68 to 71 (page images and OCR read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-16 |
| Law 6 of 2025, arts. 1 to 16, whole text | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-16 |
| MoF Decision 420 of 2025, arts. 1 to 4 (page images read) | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-16 |
| ETA Services Guide, 2nd edition, services 1/1, 2/1 and section 18/2, read in part | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-16 |
| ETA list of VAT laws and decisions, list page read | https://eta.gov.eg/ar/content/qwanyn-aldrybt-ly-alqymt-almdaft | 2026-11-16 |

Not yet confirmed: whether an electronic signature or token is required on every individual return or only on some filings (the Services Guide describes accountant approval on the system, not a signature rule). Whether electronic filing is compulsory for every individual taxpayer by a rule other than the e-system practice described here. The same-day reporting rule for e-invoices and e-receipts in the earlier version (timing rules sit in `eg-bookkeeping`). The e-invoice portal address invoicing.eta.gov.eg in the earlier version (not opened). The VAT limit reportedly cut to EGP 250,000 (held in `egypt-vat`). How partnerships and their partners file.
