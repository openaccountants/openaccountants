---
name: eg-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with their Egyptian taxes AND mentions freelancing, self-employment, sole proprietorship, professional practice, or a small business in Egypt. Trigger on phrases like "help me with my Egyptian taxes", "I'm a freelancer in Egypt", "prepare my income tax return", "I have a small business in Cairo", "أنا أعمل لحسابي الخاص" (I am self-employed), "ضريبة الدخل" (income tax), "منشأة صغيرة" (small enterprise), "إقرار ضريبي" (tax return), "أنا فريلانسر" (I'm a freelancer), "نظام الضرائب المبسط" (simplified tax regime), or any similar phrasing where the user is an Egypt-resident self-employed individual. REQUIRED entry point for the Egypt self-employed workflow; downstream skills (eg-income-tax, eg-sme-tax, eg-social-insurance, egypt-vat, eg-return-assembly) depend on it. Egypt-resident self-employed only.
version: 0.3
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-17
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# EG Freelance Intake v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Egypt self-employed intake router, tax year 2026, law as read on 16 November 2026. It takes an Egypt-resident sole proprietor (منشأة فردية), independent professional (مهنة حرة / مهنة غير تجارية) or small business owner from first message to a confirmed set of facts, and routes the case. It computes no tax. All numbers come from the content skills it routes to and are reviewed by a qualified Egyptian accountant (محاسب قانوني) before anything is filed with the Egyptian Tax Authority (ETA, مصلحة الضرائب المصرية).

Reply in the language the user writes in: Arabic in, Arabic out. Write English prose otherwise and keep native Arabic terms in brackets on first use where they help.

**Key figures that decide the route.** Each is owned by the skill in the Owner skill column; this table only routes.

| Item | Figure | Conditions | Tax year | Owner skill | Official URL |
|---|---|---|---|---|---|
| Turnover regime ceiling | EGP 20,000,000 a year (in words on the page) | Law 6 of 2025 art. 1: the project asks to use the law, professional activities included, registered or not; in force from 1 March 2025 (art. 16) | 2026 | `eg-sme-tax` | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Consultancy exclusion | 90% or more of annual turnover from consulting for one or two persons | Law 6 art. 4(1); the Minister of Finance may except activities | 2026 | `eg-sme-tax` | same |
| One-time overshoot | Up to 20% above EGP 20,000,000, once in the five years from the request (in words on the page for the ceiling) | Law 6 art. 10 last para.; a larger or second overshoot ends the regime from the following year | 2026 | `eg-sme-tax` | same |
| VAT registration limit | EGP 500,000 of taxable and exempt sales (in words on the page) | VAT Law 67 of 2016 art. 16; apply within 30 days of reaching it; the Minister may change the limit by decision | 2026 | `egypt-vat` | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |

## Scope

- **In:** an individual who is an Egyptian tax resident for 2026 and carries on a commercial, industrial, craft or professional activity alone: sole traders, freelancers, consultants, designers, doctors, lawyers, software developers.
- **Out, stop and refer:** non-residents (taxed only on income realised in Egypt: see `eg-income-tax`, Law 91 art. 6), and companies of every form (joint-stock شركة مساهمة, limited liability شركة ذات مسؤولية محدودة, partnerships). Companies go to `eg-corporate-tax` and `eg-financial-statements`.
- **Two parallel income tax tracks** for the self-employed, mutually exclusive for any one year:
  1. **Turnover regime** (نظام الضرائب المبسط), Law 6 of 2025, in force 1 March 2025: tax is a percentage of turnover (حجم الأعمال), with lighter records (art. 13), quarterly VAT returns (art. 12) and examination of returns only after five years from the request (art. 12). Route: `eg-sme-tax`.
  2. **General system** (الضريبة على الدخل), Income Tax Law 91 of 2005 as amended (the band table in force is art. 8 as replaced by Law 7 of 2024): progressive bands on net profit (صافي الربح). It applies to everyone above EGP 20,000,000 and to anyone who has not asked for, or cannot use, the turnover regime. Route: `eg-income-tax`.
- VAT (`egypt-vat`) and social insurance (`eg-social-insurance`) run alongside whichever income track applies. All paths end in `eg-return-assembly`.

## Ask the client first

Batch these in one message. Any answer that puts the case out of scope (non-resident, company) is blocking: settle it before anything else.

1. **Residence for 2026.** Resident (مقيم)? Resident: continue. Non-resident: stop and refer to an Egyptian accountant who handles non-resident filings.
2. **Legal form.** Individual sole proprietor or independent professional: continue. Company of any form, partnerships included: stop and refer to an accountant handling company returns.
3. **Activity.** Commercial or industrial (نشاط تجاري أو صناعي), or professional, non-commercial (مهنة حرة / غير تجارية)? Both are in scope. Record it, and record both for mixed activity: it changes expense rules downstream.
4. **Turnover and regime.** Rough annual turnover. Up to EGP 20,000,000: has the client filed the request form 10/1 طلبات, and on what date, or was the business under the small-enterprise tax rules of Law 152 of 2020 (moved across without a request, per the ETA Services Guide)? If consulting, what share of turnover comes from the top one or two clients?
5. **VAT.** VAT-registered? Registration number. If not, total taxable and exempt sales in the year, and whether the client imports for trade, exports or acts as a distribution agent (these must register whatever the turnover). Below the limit and not registered: note it; voluntary registration may still suit the client (`egypt-vat`).
6. **Staff.** Any employees (موظفين)? Yes: payroll tax (ضريبة كسب العمل) and employer and employee social insurance (التأمينات الاجتماعية). No: still record the client's own social insurance as a business owner.
7. **E-invoice and e-receipt.** Registered on the ETA e-invoice (الفاتورة الإلكترونية) or e-receipt (الإيصال الإلكتروني) system? Named in an ETA phase decision? Joining under those phase decisions and actually issuing the documents is a condition of the turnover regime (Law 6 art. 3).

## The method, step by step

### Working principles (upload first)

1. Upload first. After the short scope sweep above, the user sends everything they have. Infer as much as possible before asking anything.
2. Infer, then confirm. Parse every document, build a picture, then show one compact summary for correction.
3. Fill gaps only. Ask only about what is missing, ambiguous or needs confirmation.
4. Compute nothing. Routing and fact-gathering only. All numbers come from the downstream content skills and are reviewed by a qualified Egyptian accountant.
5. Do not narrate phases. Never say "Step 1" or "now the inference phase". Do the work.
6. Do not re-ask. If the sweep settled that the activity is professional, do not ask the activity type again. Track what is known.
7. Do not ask what the documents already show. If the bank statement shows the turnover, confirm it; do not ask for it.

### Step 1. Scope sweep

Ask the seven questions under "Ask the client first", batched. Resolve any blocking answer first.

### Step 2. Collect (the upload)

Once scope is confirmed, ask for everything at once, in one message with no preamble, adapted to Step 1:

- bank statements for 2026, business and personal accounts, to rebuild turnover and expenses;
- invoices issued and received (فواتير), and the e-invoice or e-receipt data exported from the ETA systems if registered;
- records of business or professional expenses and asset purchases (they support depreciation under the general system);
- VAT records: returns filed, the VAT registration certificate (شهادة التسجيل), output and input VAT data;
- social insurance records: own contributions and any payroll;
- the prior-year return (الإقرار الضريبي للعام السابق) and any ETA correspondence;
- the tax card (البطاقة الضريبية) and tax registration number;
- certificates for tax withheld by clients, if any. A project in the turnover regime is outside the withholding and advance payment systems in both directions (Law 6 art. 11).

Tell the user not to organise anything: each file will be identified. Wait for the upload and do not ask other questions meanwhile. If the user sends a partial set and says that is all, go on to Step 3 and ask for specific missing items while filling gaps.

### Step 3. Infer and confirm

Parse each document:

- bank statements: total inflows (candidate turnover), recurring client payments, outflows for expenses, VAT and tax payments, social insurance payments, equipment purchases;
- invoices and e-invoice data: reconcile issued invoices to deposits, confirm turnover and VAT charged, and test turnover against the EGP 500,000 VAT limit and the EGP 20,000,000 turnover regime ceiling in the key figures table;
- VAT returns: periods filed, output against input, gaps;
- prior-year return: regime used, prior turnover or net profit, items carried forward;
- social insurance records: status of the client and any employees.

Then show one compact summary for correction: identity and legal form, residence, activity, estimated annual turnover, VAT status, staff, e-invoice status, the route each fact points to, and flags such as "turnover near the EGP 20,000,000 line, confirm which side" or "sales above EGP 500,000 but no VAT registration found". Invite a plain "ok" or corrections. Show the picture, not raw extraction.

While filling gaps, ask with a structured question tool where one is available (such as `ask_user_input_v0`), and only about what the documents cannot show: whether the form 10/1 request was filed, the professional against commercial split of mixed activity, the business share of mixed personal and business costs. Flag every judgement call for the reviewer.

### Step 4. Route and hand off

| Established facts | Route to |
|---|---|
| Resident individual, turnover up to EGP 20,000,000, form 10/1 filed (or moved from Law 152/2020), not excluded by the 90% consultancy test | `eg-sme-tax` |
| Resident individual above EGP 20,000,000 outside the one-time overshoot, or no request filed, or excluded | `eg-income-tax` |
| Taxable and exempt sales reach EGP 500,000, already VAT-registered, or importer, exporter or distribution agent | `egypt-vat` |
| Employees, or the client's own contributions to record | `eg-social-insurance` (and `eg-payroll` for staff) |
| Non-resident | Stop: refer to a specialist in non-resident filings |
| Company of any form | Stop: company tax, out of scope for this workflow |

The two income tracks are mutually exclusive for the year: a case goes to `eg-sme-tax` or to `eg-income-tax`, never both. VAT and social insurance run in addition whenever their triggers are met. All paths converge on `eg-return-assembly`, which assembles the package for accountant review.

State the route plainly, confirm the review step and hand off. Example:

> Confirmed: resident sole proprietor, professional activity, turnover about EGP 6m, VAT-registered, no employees, request form 10/1 filed. You are in the turnover regime. I will prepare the turnover tax package and your quarterly VAT reconciliation, then assemble everything for review by a qualified Egyptian accountant before anything is filed with the ETA.

## Worked cases

**Case 1. Developer, turnover EGP 6,000,000, request filed, VAT-registered.** Turnover is EGP 14,000,000 under the ceiling, so the turnover regime is open if the 90% consultancy test is passed. Sales are EGP 5,500,000 above the VAT limit, so VAT applies. Route: `eg-sme-tax` plus `egypt-vat`, then `eg-return-assembly`. Had turnover been EGP 23,000,000 in the first breach, the one-time overshoot (up to EGP 24,000,000, computed as 120% of the ceiling) would keep the case in `eg-sme-tax` at the top band; EGP 25,000,000 would move it to `eg-income-tax` from the following year.

```oa-check
name: Routing tests for a developer with turnover EGP 6m
inputs:
  turnover: 6000000
  ceiling: 20000000
  vat_limit: 500000
steps:
  - headroom_to_ceiling: ceiling - turnover
  - excess_over_vat_limit: turnover - vat_limit
  - overshoot_cap: ceiling * 1.2
expected:
  headroom_to_ceiling: 14000000.00
  excess_over_vat_limit: 5500000.00
  overshoot_cap: 24000000.00
```

## When to refuse or refer

- Non-resident, or a company of any form: stop and refer (Scope).
- The client wants turnover split across relatives or new entities to stay under EGP 20,000,000 or the VAT limit: refuse. Law 6 art. 4(2) excludes a project that enters by splitting an activity without economic reason.
- The client asks to suppress or hide sales: refuse and offer the lawful routes.
- Open ETA examination, dispute, unfiled years or a settlement question: refer to a qualified Egyptian accountant (the dispute and settlement windows are in `eg-tax-optimization`).
- Never present a route or any downstream figure as a filed return or a professional sign-off.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 6 of 2025, arts. 1 to 16, whole text (text layer read) | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-16 |
| VAT Law 67 of 2016, art. 16 (page image read) | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf | 2026-11-16 |
| Law 7 of 2024, arts. 1 and 2: replaced Income Tax Law art. 8 band table (text layer read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-16 |
| MoF Decision 420 of 2025, arts. 1 to 4: forms 10/1 and 11/1 طلبات, form 20 إقرارات (page images read) | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-16 |
| ETA Services Guide, 2nd edition, service 1/1 (registration) and section 18/2 (Law 6), read in part | https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf | 2026-11-16 |

Not yet confirmed: the reported cut of the VAT registration limit to EGP 250,000 (attributed to a 2025 resolution numbered 281); VAT Law art. 16 reads EGP 500,000 and the ETA list of VAT laws and decisions read on 2026-11-16 holds no such decision, so `egypt-vat` keeps 500,000 and the claim stays held. The current e-invoice and e-receipt phase decisions and whether a given client is named in them (the old text said every VAT-registered taxpayer is in the B2B e-invoice mandate; no phase decision was read). The direct move of Law 152/2020 enterprises rests on the ETA Services Guide, not on a statute read here. How partnerships and their partners are taxed: this workflow refers every partnership out.
