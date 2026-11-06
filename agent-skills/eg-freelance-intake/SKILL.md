---
name: eg-freelance-intake
description: "ALWAYS USE THIS SKILL when a user asks for help with their Egyptian taxes AND mentions freelancing, self-employment, sole proprietorship, professional practice, or a small business in Egypt. Trigger on phrases like \"help me with my Egyptian taxes\", \"I'm a freelancer in Egypt\", \"prepare my income tax return\", \"I have a small business in Cairo\", \"أنا أعمل لحسابي الخاص\" (I am self-employed), \"ضريبة الدخل\" (income tax), \"منشأة صغيرة\" (small enterprise), \"إقرار ضريبي\" (tax return), \"أنا فريلانسر\" (I'm a freelancer), \"نظام الضرائب المبسط\" (simplified tax regime), or any similar phrasing where the user is an Egypt-resident self-employed individual. REQUIRED entry point for the Egypt self-employed workflow; downstream skills (eg-income-tax, eg-sme-tax, eg-social-insurance, egypt-vat, eg-return-assembly) depend on it. Egypt-resident self-employed only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eg-freelance-intake"
  jurisdiction: "EG"
  tax_year: "2026"
  last_updated: "2026-07-13"
---

# EG Freelance Intake

## Egypt Self-Employed Intake Orchestrator v0.1

## What this file is

- **Purpose of this skill** — This is the intake orchestrator for an Egypt-resident self-employed person — a sole proprietor (منشأة فردية), an independent professional (مهنة حرة / مهنة غير تجارية), or a small business owner. It establishes the facts and routes the case to the correct tax regime. It computes nothing.
- **Two parallel tracks for the self-employed** — Egypt runs two parallel tracks for the self-employed: (1) The simplified SME regime (نظام الضرائب المبسط للمنشآت الصغيرة) under Law No. 6 of 2025, effective 1 March 2025, for businesses whose annual turnover (حجم الأعمال) does not exceed EGP 20 million. Tax is a small percentage of turnover, not net profit, plus lighter bookkeeping, quarterly VAT filing, and audit deferral. → routes to eg-sme-tax. (2) The general income-tax system (الضريبة على الدخل) under the Income Tax Law (Law No. 91 of 2005, as amended by Law No. 175 of 2023). Progressive brackets apply to net profit (صافي الربح). This is the default for anyone above EGP 20m or who does not opt into / qualify for the simplified regime. → routes to eg-income-tax.  _(Law No. 6 of 2025; Income Tax Law No. 91 of 2005, as amended by Law No. 175 of 2023)_
- **Simplified SME regime effective date** — 1 March 2025  _(Law No. 6 of 2025)_
- **Simplified SME regime turnover ceiling** — 20,000,000 EGP  _(Law No. 6 of 2025)_

This skill's only job: collect facts, parse uploaded documents, confirm with the user, and hand a clean intake package to eg-return-assembly. It never produces tax figures.

Language. Write English prose, keep native Arabic terms where they aid precision (shown in parentheses on first use). Always reply in the language the user writes in — if they message in Arabic, answer in Arabic.

## Design principles (upload-first)

1. Upload-first. After a short scope sweep, the user dumps everything they have. Claude infers as much as possible before asking anything.
2. Inference, then confirm. Parse every document, build a picture, then show one compact summary for correction.
3. Gap-filling only. Ask the user only about what is missing, ambiguous, or needs confirmation.
4. Computes nothing. Routing and fact-gathering only. All numbers come from downstream content skills and are reviewed by a qualified Egyptian accountant (محاسب قانوني).
5. Do not narrate phases. Never say "Step 1," "now the inference phase," etc. Just do the work.
6. Do not re-ask. If the scope sweep established the activity is professional, do not later ask the activity type. Track what is known.
7. Do not ask about what the documents already show. If the bank statement shows the turnover, confirm it; do not ask for it.

## Step 1 — Refusal and routing sweep

Establish the load-bearing facts up front. These determine scope and the regime split. Batch them; do not walk through one at a time.

- **1. Residency** — Is the person an Egyptian tax resident (مقيم) for 2026? Resident → continue. Non-resident → stop. Non-residents are taxed only on Egypt-source income under different rules. Refer to an Egyptian accountant who handles non-resident filings.
- **Non-resident stop condition** — Non-resident → stop. Non-residents are taxed only on Egypt-source income under different rules. Refer to an Egyptian accountant who handles non-resident filings.
- **2. Legal form** — Sole proprietor / professional individual, or a company (شركة)? Individual sole proprietor or independent professional → continue. Company — joint-stock (شركة مساهمة), LLC (شركة ذات مسؤولية محدودة), or partnership — → escalate / stop. Companies file corporate tax under separate rules; this workflow is for individuals only. Refer to an accountant handling corporate returns.
- **Company escalate/stop condition** — Company (joint-stock, LLC, or partnership) → escalate / stop. Companies file corporate tax under separate rules; this workflow is for individuals only. Refer to an accountant handling corporate returns.
- **3. Activity type** — Commercial or industrial (نشاط تجاري أو صناعي), versus professional / non-commercial (مهنة حرة / غير تجارية, e.g. consultant, designer, doctor, lawyer, software developer)? Both are in scope. Record it — it affects expense rules and classification downstream. Mixed activity → record both.
- **4. Annual turnover vs the EGP 20m simplified threshold** — ≤ EGP 20 million → eligible for the simplified SME regime (Law No. 6 of 2025). Flag that opting in is an election; confirm the user's intent. → candidate for eg-sme-tax. > EGP 20 million → general income-tax system, progressive brackets on net profit. → eg-income-tax. Not sure → ask for the rough range; the dividing line is EGP 20m. EGP  _(Law No. 6 of 2025)_
- **5. VAT registration vs the EGP 500k threshold** — Mandatory VAT registration (التسجيل بضريبة القيمة المضافة) is triggered when taxable turnover exceeds EGP 500,000 in any 12 months (VAT Law No. 67 of 2016). Already VAT-registered → record the registration number. → egypt-vat in play. Taxable turnover > EGP 500k but not registered → flag: likely a mandatory-registration obligation; reviewer must confirm. Below EGP 500k and not registered → note; voluntary registration may still apply. EGP  _(VAT Law No. 67 of 2016)_
- **6. Employees** — Does the person employ anyone (موظفين)? Yes → triggers payroll withholding (ضريبة كسب العمل) and employer/employee social insurance (التأمينات الاجتماعية). → eg-social-insurance (and payroll handling). No → still record the person's own social insurance position as a self-employed/self-occupied contributor.
- **7. E-invoicing / e-receipt status** — Is the person registered on the ETA e-invoicing or e-receipt system (الفاتورة الإلكترونية / الإيصال الإلكتروني)? The ETA mandate applies to all VAT-registered taxpayers (B2B e-invoicing) and to listed taxpayers for B2C e-receipts. Record registration status; flag if VAT-registered but not yet on the e-invoicing system.

Any single answer that puts the case out of scope (non-resident, company) is a blocking question — resolve it before moving on.

## Step 2 — Collect (the upload)

Once scope is confirmed, ask for everything at once. One message, no preamble. Adapt the list to what was established in Step 1.

Typical items to request:

- Bank statements for 2026 (business and personal accounts) — to reconstruct turnover and expenses.
- Invoices issued and received (فواتير) — and ETA e-invoice / e-receipt data exported from the e-invoicing portal if registered.
- Records of professional/business expenses and asset purchases (for capital allowances under the general regime).
- VAT records — returns filed, VAT registration certificate (شهادة التسجيل), input/output VAT data (if registered).
- Social insurance records (التأمينات الاجتماعية) — own contributions and any payroll for employees.
- Prior-year tax return (الإقرار الضريبي للعام السابق) and any ETA correspondence.
- Tax card / registration data (البطاقة الضريبية) and tax file number.
- Withholding certificates for tax withheld at source by clients, if any.

Tell the user not to organise anything — Claude will identify each file. Wait for the dump; do not ask other questions while waiting. If the user uploads a partial set and says that's all they have, proceed to inference and request specific missing items during gap-filling.

## Step 3 — Infer and confirm

When documents arrive, parse each one and build an internal picture:

- Bank statements → total inflows (candidate turnover / حجم الأعمال), recurring client payments, outflows for expenses, VAT and tax payments, social insurance payments, equipment purchases.
- Invoices / ETA e-invoice data → reconcile issued invoices against deposits; confirm turnover; check VAT charged; confirm whether turnover crosses the EGP 500k VAT line or the EGP 20m simplified line.
- VAT returns → periods filed, output vs input VAT, any gaps.
- Prior-year return → prior regime used, prior turnover/net profit, carried-forward items.
- Social insurance records → contribution status for the individual and any employees.

Then show one compact summary for the user to correct: identity and legal form, residency, activity type, estimated annual turnover, VAT status, employee status, e-invoicing status, the regime each fact points to, and any flags (e.g. "turnover near the EGP 20m line — confirm which side"; "taxable turnover above EGP 500k but no VAT registration found"). Invite a plain "ok" or corrections. Do not show raw extraction; show the picture.

During gap-filling, ask with ask_user_input_v0 where possible, and only about what the documents cannot show — for example the election into the simplified regime (it is optional for eligible businesses), the professional-vs-commercial split for mixed activity, or the business-use percentage of mixed personal/business expenses. Flag every judgment call for the reviewer.

## Step 4 — Hand off (routing map)

Once facts are confirmed, route and hand the structured intake package to eg-return-assembly. Routing logic:

**Routing map**

| Established facts | Route to |
| --- | --- |
| Resident individual, turnover ≤ EGP 20m, opts into simplified regime | `eg-sme-tax` |
| Resident individual, turnover > EGP 20m (or not eligible / declines simplified) | `eg-income-tax` |
| Taxable turnover > EGP 500k, or already VAT-registered | `egypt-vat` |
| Has employees, or own self-employed contributions to record | `eg-social-insurance` |
| Non-resident | **Stop** — refer to a specialist in non-resident filings |
| Company (شركة) of any form | **Escalate / stop** — corporate tax, out of scope for this workflow |

- **Mutual exclusivity and convergence of paths** — The simplified-regime and general-system paths are mutually exclusive for the income-tax computation: a case goes to either eg-sme-tax or eg-income-tax, never both. VAT (egypt-vat) and social insurance (eg-social-insurance) run in addition whenever their triggers are met, regardless of which income path applies. All paths converge on eg-return-assembly, which assembles the package and prepares it for accountant review.

State the route plainly to the user, confirm the reviewer step, and hand off. Example:

> Confirmed: resident sole proprietor, professional activity, turnover about EGP 6m, VAT-registered, no employees. You're eligible for the simplified SME regime and you've elected to use it. I'll prepare the simplified-tax package plus your VAT reconciliation, then assemble everything for review by a qualified Egyptian accountant before anything is filed with the ETA. Starting now.

## Disclaimer

This skill performs orchestration and routing only. It establishes facts and directs the case to the correct Egyptian tax regime; it computes no tax figures itself. All figures, classifications, and filing positions produced by the downstream skills must be reviewed and signed off by a qualified Egyptian accountant (محاسب قانوني) before filing with the Egyptian Tax Authority (ETA / مصلحة الضرائب المصرية) or acting upon them. Thresholds and rules cited (the EGP 20 million simplified-regime threshold under Law No. 6 of 2025, the EGP 500,000 VAT registration threshold under VAT Law No. 67 of 2016, and the general income-tax brackets under Law No. 91 of 2005 as amended by Law No. 175 of 2023) should be re-verified against current ETA guidance at the time of filing.

## Step 4 — Hand off (routing map)

0. **Route resident individual under simplified turnover threshold who opts in** — Route to eg-sme-tax
0. **Route resident individual above threshold or declining simplified regime** — Route to eg-income-tax
0. **Route VAT-relevant cases** — Route to egypt-vat
0. **Route social insurance cases** — Route to eg-social-insurance
0. **Stop for non-resident** — Stop — refer to a specialist in non-resident filings
0. **Escalate/stop for company** — Escalate / stop — corporate tax, out of scope for this workflow
0. **Converge and assemble package** — Hand off structured intake package to eg-return-assembly

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eg-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eg-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
