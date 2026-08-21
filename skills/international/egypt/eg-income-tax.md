---
name: eg-income-tax
description: Use this skill whenever asked about Egyptian personal income tax for resident individuals, sole proprietors, freelancers, or professionals — to compute, review, or explain it. Trigger on phrases like "Egypt income tax", "ضريبة الدخل", "Egyptian tax brackets", "sole proprietor tax Egypt", "freelancer tax Egypt", "professional income tax Egypt", "إقرار ضريبة الدخل", or any request to prepare or check an Egyptian individual income tax return. ALWAYS read this skill before touching any Egypt personal income tax work.
version: 1.0
jurisdiction: EG
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Income Tax

## Egypt Personal Income Tax (ضريبة الدخل) Skill v1.0

This skill covers Egyptian personal income tax (ضريبة الدخل على الأشخاص الطبيعيين) for **resident individuals**, **sole proprietors (منشأة فردية)**, and **professionals / non-commercial activity (مهن حرة)**. The AI must reply in the user's language (English or Arabic / Egyptian Arabic) and may use the native tax terms shown throughout.

> **Currency note:** all figures are in Egyptian Pounds (EGP / ج.م).
> **YMYL — verify before relying.** Egyptian brackets and exemptions changed in 2024 and 2025. Where this skill says "verify current value," re-confirm against the Egyptian Tax Authority (ETA — eta.gov.eg), PwC Worldwide Tax Summaries (taxsummaries.pwc.com/egypt) or a Big-4 alert before filing.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Egypt (جمهورية مصر العربية) |
| Tax | Personal Income Tax (ضريبة الدخل على الأشخاص الطبيعيين) |
| Currency | EGP (Egyptian Pound — ج.م) |
| Tax year | Calendar year (1 January – 31 December) for individuals |
| Legislation | Income Tax Law No. 91 of 2005 (as amended) — including the 2024 bracket reset and Laws No. 5, 6 and 7 of 2025 |
| Tax authority | Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية) |
| Portal | eta.gov.eg |
| Filing deadline | **31 March** of the year following the tax year (individuals / sole proprietors) |
| Top marginal rate | 27.5% on income over EGP 1,200,000 |
| Annual personal exemption | EGP 20,000 (raised from EGP 15,000 effective 21 Feb 2024) — *verify current value* |
| Simplified SME alternative | Law No. 6 of 2025 turnover-based regime for businesses up to EGP 20m — see `eg-sme-tax` |
| Contributor | Open Accountants Community |
| Quality tier | Research-verified — pending sign-off by a qualified Egyptian accountant (محاسب قانوني) |
| Skill version | 1.0 |

### Progressive tax brackets — tax year 2026

**Progressive tax brackets — TY2026**

| Band (taxable income, EGP) | Rate | Native |
| --- | --- | --- |
| 0 – 40,000 | 0% | معفى |
| 40,001 – 55,000 | 10% |  |
| 55,001 – 70,000 | 15% |  |
| 70,001 – 200,000 | 20% |  |
| 200,001 – 400,000 | 22.5% |  |
| 400,001 – 1,200,000 | 25% |  |
| Over 1,200,000 | 27.5% | الشريحة العليا |

- **Rates apply basis** — Rates apply to annual taxable income after deducting the personal exemption and allowable deductions. Tax is computed band-by-band (marginal), subject to the high-earner bracket-elimination rule below.
- **High-earner bracket-elimination rule (مهم)** — Egypt does not grant the lower bands to high earners. As total annual taxable income rises past defined thresholds, the 0% band (and then successively higher bands) is withdrawn, so the highest earners are taxed across the upper bands only. The 0% first band is available only to residents whose annual income does not exceed EGP 1,200,000. The exact step thresholds at which each lower band is removed must be verified against the current ETA schedule before filing. When the precise schedule is unknown, compute the straightforward marginal result AND flag that the bracket-elimination adjustment may increase tax — defer the final number to a qualified Egyptian accountant.

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown whether an expense is deductible | Treat as **non-deductible** until documentary support (e-invoice/receipt) is confirmed |
| Unknown whether high-earner bracket-elimination applies | Compute marginal tax AND warn it may be higher; do not finalise |
| Unknown personal exemption for the year | Use EGP 20,000 and label "verify current value" |
| Unknown residency | Treat as **non-resident** (Egyptian-source income only) until residency confirmed |
| Unknown whether SME regime is better | Compute normal regime; cross-ref `eg-sme-tax` for comparison |
| Mixed personal/business expense | Disallow the personal portion |

## Section 2 — Required inputs & refusal catalogue

### Required inputs

- **Residency status** — Resident if present in Egypt > 183 days in a 12-month period, or Egypt is the centre of vital/commercial interests, or an Egyptian working abroad whose income is paid by an Egyptian treasury. Residents are taxed on worldwide income for activities managed/realised in Egypt; non-residents on Egyptian-source income only.
- **Activity category** — employment (مرتبات وأجور), commercial & industrial activity (نشاط تجاري وصناعي), or non-commercial / professional activity (مهن غير تجارية). Each has its own income-determination rules but feeds the same progressive scale.
- **Gross receipts / revenue** — Gross receipts / revenue for the tax year, with supporting documents.
- **Business expenses** — Business expenses with e-invoices / receipts (electronic invoicing is the ETA standard).
- **Insurance & pension contributions** — Insurance & pension contributions (for the capped deduction).
- **Withholding tax already suffered** — Withholding tax already suffered (advance payments / WHT certificates) to credit against the final liability.
- **Tax year and SME election** — Tax year and whether the SME alternative regime has been elected.

### Refusal catalogue (R-EG-n)

- **R-EG-1** — Do not produce a final filing figure without the residency status confirmed.  _(R-EG-1)_
- **R-EG-2** — Do not deduct an expense lacking documentary support (e-invoice/receipt). Disallow it.  _(R-EG-2)_
- **R-EG-3** — Do not finalise tax for income > EGP 1,200,000, or where bracket-elimination may apply, without a qualified Egyptian accountant confirming the band schedule.  _(R-EG-3)_
- **R-EG-4** — Refuse to advise on tax evasion, under-declaration of receipts, or fictitious expenses.  _(R-EG-4)_
- **R-EG-5** — Do not apply the simplified SME (turnover-based) regime here; route to `eg-sme-tax` and confirm eligibility (turnover ≤ EGP 20m and election made).  _(R-EG-5)_
- **R-EG-6** — Do not advise on corporate income tax (companies) — this skill is individuals only.  _(R-EG-6)_
- **R-EG-7** — Do not give a binding figure where the current-year bracket/exemption values cannot be verified; provide the formula and flag "verify current value."  _(R-EG-7)_
- **R-EG-8** — Do not net foreign tax credits or apply tax treaties without explicit treaty confirmation; flag for professional review.  _(R-EG-8)_

## Section 3 — Transaction Pattern Library

Bank/ledger keywords (Arabic + English) to classify line items. Match on substrings; when ambiguous, apply the conservative default.

### Income (دخل / إيرادات)

**Income keyword table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| إيراد / مبيعات / تحصيل | revenue / sales / receipt | Business income (commercial/industrial) |
| أتعاب / استشارات | fees / consulting | Professional (non-commercial) income |
| تحويل وارد / إيداع عميل | incoming transfer / client deposit | Income — confirm it is trading receipt |
| مرتب / راتب | salary / payroll | Employment income (separate computation) |
| إيجار مستحق | rent received | Real-estate revenue (separate category) |
| فوائد / عوائد | interest / yield | Investment income — usually WHT/final; exclude from business profit |

### Deductible expenses (مصروفات قابلة للخصم)

**Deductible expenses table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| إيجار مكتب / محل | office / shop rent | Deductible if business-use |
| رواتب الموظفين | staff wages | Deductible |
| كهرباء / مياه / إنترنت | utilities / internet | Deductible (business portion) |
| مشتريات / بضاعة | purchases / stock | Cost of goods sold |
| إهلاك أصول | depreciation | Deductible per law schedules |
| تأمينات اجتماعية | social insurance | Deductible employer/owner contributions |
| دعاية وإعلان | advertising | Deductible if documented |
| صيانة | maintenance | Deductible |

### Non-deductible / disallowed (غير قابل للخصم)

**Non-deductible table**

| Keyword (AR) | Keyword (EN) | Treatment |
| --- | --- | --- |
| مصاريف شخصية / سحب شخصي | personal / owner drawings | **Non-deductible** |
| غرامات / جزاءات | fines / penalties | **Non-deductible** |
| ضريبة الدخل | income tax paid | **Non-deductible** |
| مصروف بدون فاتورة | expense without invoice | **Non-deductible** (no support) |
| توزيعات أرباح موزعة | distributed profits/dividends | Not an expense |

### Exclusions (مستبعد من الربح)

**Exclusions table**

| Item (AR) | Item (EN) | Treatment |
| --- | --- | --- |
| إيرادات معفاة | exempt income | Exclude from taxable base |
| دخل خاضع لخصم نهائي | income under final WHT | Exclude from progressive base (already taxed) |
| رأس مال / قروض واردة | capital injection / loan in | Not income |

## Section 4 — Worked examples

All figures illustrative; verify the live bracket/exemption schedule before filing.

### Example 1 — Freelance developer, low income

Net professional profit EGP 90,000. Personal exemption EGP 20,000 → taxable EGP 70,000.
- 0–40,000 @ 0% = 0
- 40,000–55,000 @ 10% = 1,500
- 55,000–70,000 @ 15% = 2,250
- **Tax = EGP 3,750.**

### Example 2 — Sole proprietor shop (commercial activity)

Gross receipts EGP 600,000; documented deductible expenses EGP 250,000 → net profit EGP 350,000. Exemption EGP 20,000 → taxable EGP 330,000.
- 0–40,000 @ 0% = 0
- 40,000–55,000 @ 10% = 1,500
- 55,000–70,000 @ 15% = 2,250
- 70,000–200,000 @ 20% = 26,000
- 200,000–330,000 @ 22.5% = 29,250
- **Tax = EGP 59,000.**

### Example 3 — Professional with capped insurance deduction

Net profit EGP 250,000; life/health/pension premiums EGP 18,000. Deduction capped at the lower of 15% of net revenue or EGP 10,000 → deduct EGP 10,000. Personal exemption EGP 20,000. Taxable = 250,000 − 10,000 − 20,000 = EGP 220,000.
- 0–40,000 @ 0% = 0
- 40,000–55,000 @ 10% = 1,500
- 55,000–70,000 @ 15% = 2,250
- 70,000–200,000 @ 20% = 26,000
- 200,000–220,000 @ 22.5% = 4,500
- **Tax = EGP 34,250.**

### Example 4 — High earner (top band + elimination flag)

Net taxable income EGP 1,500,000.
- Marginal computation: 0 + 1,500 + 2,250 + 26,000 + 45,000 (200k–400k @22.5%) + 200,000 (400k–1.2m @25%) + 82,500 (300k @27.5%) = **EGP 357,250 marginal.**
- **⚠ Flag (R-EG-3):** income exceeds EGP 1,200,000, so the 0% band (and possibly lower bands) is **eliminated**, raising the actual tax above the marginal figure. Defer the final number to a qualified Egyptian accountant and verify the current band-elimination schedule.

### Example 5 — Normal vs SME comparison

Trading turnover EGP 4,000,000; net profit after expenses EGP 700,000.
- Normal regime (progressive on net profit) — compute and flag the high-earner elimination rule.
- SME regime (Law No. 6 of 2025): turnover ≤ EGP 20m → tax ≈ **1% of turnover** (EGP 3m–10m band) = EGP 40,000, subject to eligibility and election.
- Present both; route the SME path to `eg-sme-tax`. The taxpayer may benefit materially from the SME regime here — recommend professional confirmation.

### Example 6 — Non-resident, Egyptian-source fee

Non-resident consultant earns EGP 100,000 of Egyptian-source professional fees. Taxed on Egyptian-source income only; personal exemption generally available to residents — **verify exemption availability for non-residents** and check WHT/treaty position (R-EG-8). Flag for professional review.

## Section 5 — Tier 1 rules (law refs) + Tier 2

### Tier 1 — settled rules with citations

- **T1-1** — Tax base is annual net profit for both commercial/industrial and non-commercial (professional) activity.  _(Income Tax Law No. 91 of 2005, as amended)_
- **T1-2** — Progressive scale 0% / 10% / 15% / 20% / 22.5% / 25% / 27.5%, top band over EGP 1,200,000 (current schedule per ETA / PwC, TY2026). *Verify current value.*  _(T1-2)_
- **T1-3** — Annual personal exemption EGP 20,000 (raised from EGP 15,000 effective 21 Feb 2024). *Verify current value.*  _(T1-3)_
- **T1-4** — 0% first band available only to residents with annual income ≤ EGP 1,200,000; high-earner bracket-elimination applies above that — *verify the step schedule.*  _(T1-4)_
- **T1-5** — Insurance/pension premiums + private fund contributions deductible up to the lower of 15% of net revenue or EGP 10,000.  _(T1-5)_
- **T1-6** — Deductible expenses must be connected to the activity and supported by electronic invoices/receipts; personal expenses, fines, and income tax itself are non-deductible.  _(T1-6)_
- **T1-7** — Business losses carry forward up to 5 years (restrictions on >50% ownership/activity change).  _(T1-7)_
- **T1-8** — Annual return filing deadline 31 March following the tax year for individuals.  _(T1-8)_
- **T1-9** — Simplified turnover-based SME regime for businesses with annual turnover ≤ EGP 20m introduced by Law No. 6 of 2025 (rates ~0.4%–1.5% of turnover by band) — handled in `eg-sme-tax`.  _(T1-9, Law No. 6 of 2025)_
- **T1-10** — 2025 procedural package (Laws No. 5 & 7 of 2025): settlement/amnesty windows and a cap that delay interest/additional tax cannot exceed 100% of principal tax — relevant to penalties, not the base computation.  _(T1-10, Laws No. 5 & 7 of 2025)_

### Tier 2 — judgement / ambiguity (resolve conservatively, flag for reviewer)

- **T2-1** — Allocating mixed personal/business expenses — disallow personal share.  _(T2-1)_
- **T2-2** — Depreciation rates and asset categories — apply law schedules; flag if uncertain.  _(T2-2)_
- **T2-3** — Treatment of foreign-source income for residents and treaty relief — flag (R-EG-8).  _(T2-3)_
- **T2-4** — Whether a receipt is a trading receipt vs capital/loan — default to caution.  _(T2-4)_
- **T2-5** — Exact high-earner band-elimination thresholds — verify; do not finalise.  _(T2-5)_

## Section 6 — Excel working paper template

**Excel working paper columns**

| Col | Header (EN) | Header (AR) |
| --- | --- | --- |
| A | Date | التاريخ |
| B | Description | البيان |
| C | Counterparty | الطرف الآخر |
| D | Category (income/expense/non-deductible/exclusion) | التصنيف |
| E | Amount EGP | المبلغ |
| F | Document ref (e-invoice no.) | رقم الفاتورة الإلكترونية |
| G | Deductible? (Y/N) | قابل للخصم؟ |
| H | Note / disallowance reason | ملاحظات |

- **Summary block formula** — Gross receipts (إجمالي الإيرادات)            = SUM(income) Less deductible expenses (المصروفات)         = SUM(deductible) Net profit (صافي الربح)                      = receipts − expenses Less insurance/pension (capped)              = MIN(15% net revenue, 10,000) Less personal exemption (الإعفاء الشخصي)     = 20,000   [verify] Taxable income (الوعاء الضريبي)              = net profit − deductions Tax (band-by-band)                           = progressive calc ⚠ apply high-earner band-elimination if income > 1,200,000 Less WHT / advance payments                  = credits Tax payable / refundable (المستحق)           = tax − credits

Build the progressive calc as a stepped formula per band; keep each band on its own row so a reviewer can audit it.

## Section 7 — Bank Statement Reading Guide

Egyptian statements (كشف حساب) appear in Arabic, English, or both. Common formats:

- **National Bank of Egypt — البنك الأهلي المصري (NBE):** Arabic-first; debit = مدين, credit = دائن. Look for مبيعات / تحصيل (income) and سحب / مدفوعات (payments).
- **Banque Misr — بنك مصر:** bilingual; transfers labelled تحويل (transfer), إيداع (deposit), سحب (withdrawal).
- **Commercial International Bank — CIB (البنك التجاري الدولي):** often English-first with Arabic memo lines; POS/merchant settlements show as "POS Settlement" or تسوية نقاط بيع → business income.

### Key Arabic banking terms

**Key Arabic banking terms table**

| Arabic | English |
| --- | --- |
| كشف حساب | bank statement |
| رصيد | balance |
| مدين | debit |
| دائن | credit |
| إيداع | deposit |
| سحب | withdrawal |
| تحويل | transfer |
| تحصيل | collection / receipt |
| مرتجع | refund / return |
| رسوم بنكية | bank charges (deductible business expense) |
| فائدة دائنة | interest earned (investment income — exclude from business profit) |
| نقاط البيع | point of sale (POS) |

Reconcile statement receipts to declared revenue; unexplained deposits should be queried, not assumed taxable or non-taxable (apply R-EG-1/R-EG-2 discipline).

## Section 8 — Onboarding fallback, references & test suite

### Onboarding fallback

If required inputs are missing, ask (in the user's language): residency status, activity category, the tax year, gross receipts, documented expenses, insurance/pension contributions, and any WHT suffered. Do not guess — apply conservative defaults and flag.

### References (verify before filing)

- Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية): eta.gov.eg
- PwC Worldwide Tax Summaries — Egypt: taxsummaries.pwc.com/egypt
- Income Tax Law No. 91 of 2005 (as amended); 2024 bracket reset; Laws No. 5, 6, 7 of 2025
- Big-4 / major-firm 2025–2026 tax alerts (PwC, KPMG, EY, Deloitte, Andersen, Matouk Bassiouny)

### Test suite

1. Net profit EGP 70,000 → tax EGP 3,750. ✓ (Example 1)
2. Net profit EGP 350,000 (commercial) → tax EGP 59,000. ✓ (Example 2)
3. Insurance premium EGP 18,000 → deduction capped at EGP 10,000. ✓ (Example 3)
4. Income EGP 1,500,000 → must flag bracket-elimination (R-EG-3). ✓ (Example 4)
5. Expense without invoice → non-deductible (R-EG-2). ✓
6. Turnover ≤ EGP 20m → offer SME comparison and route to `eg-sme-tax`. ✓ (Example 5)
7. Non-resident Egyptian-source fee → tax Egyptian-source only, flag exemption/treaty. ✓ (Example 6)
8. Filing deadline = 31 March of the following year. ✓

## PROHIBITIONS

- Do NOT advise on, enable, or overlook tax evasion, under-declaration of receipts, fictitious or undocumented expenses, or concealment of income.
- Do NOT finalise a tax figure when current-year brackets/exemption cannot be verified — give the formula and flag "verify current value."
- Do NOT finalise tax for income over EGP 1,200,000 or where the high-earner bracket-elimination rule may apply, without qualified Egyptian accountant review.
- Do NOT deduct expenses without documentary support (e-invoice/receipt).
- Do NOT apply the SME turnover-based regime here — route to `eg-sme-tax`.
- Do NOT handle corporate income tax — this skill is individuals only.
- Do NOT apply tax treaties or foreign tax credits without explicit confirmation.
- Do NOT present output as a filed return or as professional sign-off.

## Disclaimer

This skill is **research-verified** open-source content from the Open Accountants Community and is **pending sign-off by a qualified Egyptian accountant (محاسب قانوني)**. It is provided for informational and workflow purposes only and does not constitute tax, legal, or accounting advice. Egyptian tax law (Income Tax Law No. 91 of 2005 as amended, and the 2024–2025 amendments) changes frequently; brackets, the personal exemption, and the high-earner band-elimination schedule must be re-verified against the Egyptian Tax Authority (eta.gov.eg) and a reputable source before any return is filed. Always have an Egypt-licensed professional review and sign off. Learn more at openaccountants.com.

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
