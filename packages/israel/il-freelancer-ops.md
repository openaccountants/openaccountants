---
name: il-freelancer-ops
description: Use this skill when advising Israeli freelancers (עצמאים) on business operations, tax deadlines, threshold monitoring, invoice requirements, and accountant package preparation. Trigger on phrases like "osek patur threshold", "freelancer Israel taxes", "עוסק פטור", "עוסק מורשה", "עסק זעיר", "esek za'ir", "mkdamot", "מקדמות", "havila l'roe cheshbon", "bituach leumi self-employed", "ביטוח לאומי עצמאי", "freelancer deadlines Israel", or any Israel freelancer operations query. ALWAYS read this skill before advising on Israeli freelancer tax operations.
version: 1.0
jurisdiction: IL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Freelancer Ops

## Israel Freelancer Operations Skill v1.0

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Freelancer tax operations, deadlines, threshold monitoring |
| Currency | NIS (Israeli New Shekel — ₪) |
| Business types | Osek Murshe (עוסק מורשה), Osek Patur (עוסק פטור), Esek Za'ir (עסק זעיר) |
| VAT rate | 18% (effective January 2025) |
| Osek Patur threshold (2025) | NIS 120,000 annual turnover |
| Osek Patur threshold (2026) | NIS 122,833 annual turnover (CPI-indexed) |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים בישראל) |
| Filing portal | Shaam Online — https://www.misim.gov.il |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed רואה חשבון or יועץ מס |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown business type | Treat as Osek Murshe (higher obligations) |
| Unknown VAT filing frequency | Bi-monthly |
| Revenue near threshold | Alert at 70% — do not wait until exceeded |
| Unknown whether invoice requires allocation number | Include allocation number |
| Unknown pension deposit status | Assume no deposit made — flag Dec 31 deadline |

## Section 2 — Freelancer business types

### 2.1 Osek Murshe (עוסק מורשה) — Authorized dealer

**Osek Murshe attributes**

| Attribute | Detail |
| --- | --- |
| Registration | Registered for VAT at ITA |
| VAT obligation | Must charge 18% VAT on all invoices |
| Invoice type | Heshbonit Mas (חשבונית מס — tax invoice) |
| Input VAT | Can deduct input VAT (Mas Tsumos — מס תשומות) on business expenses |
| VAT filing | Bi-monthly (turnover < NIS 1.5M) or monthly (turnover > NIS 1.5M) |
| Annual return | Form 1301 (דוח שנתי) required |
| Advance payments | Mkdamot (מקדמות) — bi-monthly income tax advances |

### 2.2 Osek Patur (עוסק פטור) — Exempt dealer

**Osek Patur attributes**

| Attribute | Detail |
| --- | --- |
| Eligibility | Annual turnover below threshold (NIS 120,000 for 2025; NIS 122,833 for 2026) |
| VAT obligation | Does NOT charge VAT |
| Invoice type | Kabala (קבלה — receipt) only |
| Input VAT | Cannot deduct input VAT on purchases |
| VAT filing | No periodic VAT returns; annual turnover declaration by January 31 |
| Annual return | Form 1301 still required for income tax |
| Threshold monitoring | Must convert to Osek Murshe if threshold exceeded mid-year |

### 2.3 Esek Za'ir (עסק זעיר) — Micro business

Introduced in 2024 under Income Tax Ordinance Section 17א.

**Esek Za'ir attributes**

| Attribute | Detail |
| --- | --- |
| Eligibility | Under the Osek Patur revenue threshold |
| Key benefit | 30% normative expense deduction — no receipts needed |
| Reporting | Simplified; exempt from annual income tax report in most cases |
| Restriction | Cannot be a former employee of the invoiced client |
| Restriction | No more than 25% of annual revenue from a single related party |
| Threshold | Shared with Osek Patur (NIS 122,833 for 2026, CPI-indexed) |

## Section 3 — Invoice requirements

### 3.1 General rules

- **Invoice numbering** — Invoice numbering must be sequential with no gaps
- **Osek number requirement** — All invoices must include the freelancer's Osek number (מספר עוסק — 9-digit taxpayer ID)
- **Osek Murshe invoice requirement** — Osek Murshe: must issue Heshbonit Mas (tax invoice) showing VAT separately
- **Osek Patur invoice requirement** — Osek Patur: issues Kabala (receipt) only — must NOT show VAT

### 3.2 Allocation numbers (Mispar Haktzaa — מספר הקצאה)

- **Allocation number requirement** — From 2026, Osek Murshe must obtain an allocation number from the Tax Authority system for tax invoices

**Allocation number thresholds**

| Effective date | Invoice threshold (before VAT) |
| --- | --- |
| January 2026 | NIS 10,000 |
| June 2026 | NIS 5,000 |

- **Missing allocation number consequence** — Without an allocation number, the recipient cannot deduct input VAT. Flag any issued invoice above the threshold that is missing an allocation number.

## Section 4 — Tax deadline calendar

### 4.1 Periodic deadlines

**Periodic deadlines table**

| Deadline | Frequency | Date | Details |
| --- | --- | --- | --- |
| VAT filing (Osek Murshe, bi-monthly) | Bi-monthly | 15th of the month after the period | Mar 15, May 15, Jul 15, Sep 15, Nov 15, Jan 15 |
| VAT filing (monthly filers) | Monthly | 15th of each month | For businesses exceeding the monthly threshold |
| Detailed VAT report (Doch Meforat, report 874) | Monthly | 23rd of the following month | Required for annual turnover > NIS 500,000; forces monthly filing |
| Bituach Leumi advances | Monthly | 15th of each month | National Insurance advance payments |
| Mkdamot (income tax advances) — monthly filers | Monthly | 15th of the month after the period | Per Tax Authority assessment letter |
| Mkdamot — bi-monthly filers | Bi-monthly | 19th of the month after the period | Per Tax Authority assessment letter |

### 4.2 Annual deadlines

**Annual deadlines table**

| Deadline | Date | Details |
| --- | --- | --- |
| Osek Patur annual turnover declaration | January 31 | Report previous year's turnover to VAT office |
| Annual income tax report (Form 1301) — paper | May 31 | For tax year 2025 filed in 2026 |
| Annual income tax report (Form 1301) — online | June 30 | Online filing mandatory for most filers |
| Annual income tax report — CPA extension | July 31 or later | Via CPA association quota arrangement |
| Self-employed pension deposit deadline | December 31 | Last day to deposit for that tax year's benefits |

- **Shabbat/holiday deadline shift** — If a deadline falls on Shabbat (Saturday), it moves to Sunday. If it falls on a Jewish holiday (Chag), check the ITA website for adjusted dates.

### 4.3 Pension contribution deadlines (December 31)

- **Missed deadline consequence** — Missing December 31 forfeits both tax benefits for the entire year
- **Section 45א — 35% tax credit (Zikui) — credit basis** — Credit on contributions up to 5.5% of business income
- **Section 45א 2026 cap** — approximately NIS 11,640 + NIS 1,164 NIS
- **Section 47 — Income deduction (Nikui) — deduction basis** — Deduction of up to 11% of qualifying income
- **Section 47 2026 qualifying-income ceiling** — NIS 232,800; max deposit approximately NIS 25,608 NIS
- **Mandatory self-employed pension contribution 2026 rates** — 4.45% on income up to half the average wage; 12.55% above it
- **Average wage 2026** — NIS 13,769/month NIS/month
- **Mandatory pension nature** — This is a legal obligation, not just a tax benefit

## Section 5 — Osek Patur threshold monitoring

### 5.1 Alert levels

- **Tracking approach** — Track cumulative annual revenue against the Osek Patur threshold

**Alert levels table**

| Alert level | Revenue (2026) | Action |
| --- | --- | --- |
| Informational (70%) | ~NIS 86,000 | "You've reached 70% of the annual threshold. Consider planning for potential transition." |
| Warning (85%) | ~NIS 104,400 | "Approaching threshold. Review implications of converting to Osek Murshe." |
| Urgent (95%) | ~NIS 116,700 | "Very close to threshold. Conversion may be required soon." |

### 5.2 Transition implications

- **Transition steps** — When the threshold is exceeded, the freelancer must: 1. Register as Osek Murshe at the local Tax Authority office (Misrad Mas Hachnasa — משרד מס הכנסה) 2. Begin charging VAT (18%) on all invoices 3. Switch to issuing Heshbonit Mas (tax invoices) instead of Kabala (receipts) 4. Register for the allocation number system (for invoices above the threshold) 5. Begin filing periodic VAT returns 6. Start tracking input VAT on business expenses for deductions 7. Notify clients of new invoicing format 8. Bituach Leumi payments may increase

### 5.3 Esek Za'ir alternative

- **Esek Za'ir alternative** — If income is expected to stay near the threshold, the Esek Za'ir track offers a 30% normative expense deduction and simplified reporting but shares the same revenue ceiling as Osek Patur. It does not defer the obligation to convert to Osek Murshe if the threshold is exceeded.

## Section 6 — Bituach Leumi (National Insurance) for self-employed

### 6.1 Contribution rates (2026)

**Contribution rates table**

| Income range | NI rate | Health rate | Total |
| --- | --- | --- | --- |
| Up to NIS 7,703/month | 2.87% | 3.10% | 5.97% |
| NIS 7,703 – NIS 51,910/month | 12.83% | 5.00% | 17.83% |

- **Minimum monthly advance** — NIS 187 NIS/month
- **Maximum monthly advance** — NIS 7,850 NIS/month
- **Minimum income floor** — NIS 2,065/month NIS/month
- **Direct-debit extension** — Direct-debit payers (הוראת קבע) get an automatic extension to the 22nd
- **NI tax deductibility** — 52% of the NI amount is tax-deductible for income tax purposes

## Section 7 — Accountant package (Havila L'Roe Cheshbon — חבילה לרואה חשבון)

### 7.1 Package contents

- **Package contents list** — 1. **Issued invoices** — all invoices/receipts issued during the period, sorted by date 2. **Received invoices/receipts** — all expense documents (business purchases, subscriptions, equipment) 3. **Bank statement summary** — transaction list matched to invoices where possible 4. **Utility bills** — electricity, telecoms, water, organized by provider 5. **Revenue summary** — running annual total with monthly breakdown 6. **Cover sheet** — summary page with key figures

### 7.2 Cover sheet fields

**Cover sheet fields table**

| Field | Description |
| --- | --- |
| Period covered | Month / quarter / year |
| Total revenue (Bruto — ברוטו) | Gross income for the period |
| Total expenses | All deductible business expenses |
| Net income (Neto — נטו) | Revenue minus expenses |
| VAT collected | For Osek Murshe only |
| VAT paid on expenses (Mas Tsumos) | For Osek Murshe only |
| Net VAT payable/refundable | Output VAT minus Input VAT |
| Running annual revenue total | Year-to-date cumulative |
| Invoice count | Number of invoices issued and received |

### 7.3 Folder structure

- **Folder structure** — Organize by period: - `YYYY-MM/invoices-issued/` - `YYYY-MM/invoices-received/` - `YYYY-MM/utility-bills/` - `YYYY-MM/bank-statements/` - Cover sheet at the root of each period folder

## Section 8 — Invoice aging tracker

- **Tracking approach** — Track all issued invoices by payment status:

**Invoice aging tracker table**

| Bucket | Age | Recommended action |
| --- | --- | --- |
| Current | 0–29 days | Monitor, no action needed |
| 30-day | 30–59 days | Friendly reminder to client |
| 60-day | 60–89 days | Formal follow-up with invoice copy and payment details |
| 90+ day | 90+ days | Alert for escalation consideration |

- **Partial payments tracking** — Track partial payments and maintain running totals: total outstanding, total overdue, by client.

## Section 9 — Worked examples

### Example 1 — Osek Patur approaching threshold

**Scenario:** Freelance web developer, Osek Patur, has earned NIS 95,000 by September with 3 months remaining.

**Working:**
- Average monthly income: NIS 95,000 ÷ 9 = ~NIS 10,556
- Projected annual total: NIS 10,556 × 12 = ~NIS 126,667
- 2025 threshold: NIS 120,000
- Status: projected to exceed threshold by ~NIS 6,667

**Action:** Alert at 85% level. Prepare transition checklist. Recommend consulting accountant before crossing the threshold.

### Example 2 — Pension contribution deadline

**Scenario:** Self-employed consultant, annual business income NIS 300,000. December 15, no pension deposits yet.

**Working:**
- Section 45א credit: 35% on up to 5.5% of NIS 300,000 = NIS 16,500 eligible → NIS 5,775 tax credit
- Section 47 deduction: up to 11% of NIS 300,000 = NIS 33,000 deductible (marginal benefit depends on tax bracket)
- Mandatory contribution: 4.45% on income up to half the average wage + 12.55% above it
- Deadline: December 31 — missing it forfeits both benefits for the entire year

**Action:** Urgent alert. Deposit to pension fund, Kupat Gemel, or insurance policy before December 31.

## Section 10 — Common errors and red flags

**Common errors and red flags table**

| Error | Why it matters |
| --- | --- |
| Confusing Osek Murshe with Osek Patur | Different VAT obligations, invoice types, and filing requirements |
| Skipping zero-revenue VAT returns | Osek Murshe must file bi-monthly returns even with no revenue; missing reports trigger penalties |
| Gap in invoice numbering | Violates Tax Authority requirements; sequential numbering is mandatory |
| Missing allocation number on invoices > NIS 10,000 | From 2026, recipient loses input VAT deduction |
| Wrong annual report deadline | Form 1301 is due May 31 (paper) / June 30 (online) — not April 30 |
| Confusing Section 45א credit with mandatory pension | They are separate: 45א/47 are voluntary tax benefits; mandatory contribution is a legal floor |
| Using Bituach Leumi based on monthly actual revenue | BL advances are based on projected annual income, not actual monthly revenue |

## Section 11 — Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Tax Authority — Form 1301 / annual report | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals |
| Tax Authority — allocation numbers | https://www.gov.il/he/service/request-assignment-number-for-tax-invoice |
| Kol Zchut — Osek Patur | https://www.kolzchut.org.il/he/עוסק_פטור |
| Kol Zchut — Esek Za'ir | https://www.kolzchut.org.il/he/עסק_זעיר |
| Kol Zchut — Section 45א pension credit | https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_בגין_הפרשות_לביטוח_פנסיוני |
| Bituach Leumi — self-employed rates | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| ITA filing portal (Shaam Online) | https://www.misim.gov.il |

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional — such as a רואה חשבון (Ro'eh Cheshbon — CPA) or יועץ מס (Yo'etz Mas — tax advisor) licensed in Israel — before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
