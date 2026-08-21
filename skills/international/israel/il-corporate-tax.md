---
name: il-corporate-tax
description: Use this skill when advising on Israeli corporate tax strategy, profit extraction methods, or controlling shareholder (בעל שליטה) tax planning. Trigger on phrases like "corporate tax Israel", "dividend vs salary Israel", "baal shlita", "בעל שליטה", "halokat dividendim", "חלוקת דיבידנדים", "shareholder loan Israel", "halvaat baalim", "הלוואת בעלים", "Section 3 tet", "סעיף 3 ט", "dmei nihul", "דמי ניהול", "management fees Israel", "chevra me'atim", "חברה מעטים", or any Israeli corporate tax extraction query. ALWAYS read this skill before advising on Israeli corporate profit extraction.
version: 1.0
jurisdiction: IL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Corporate Tax

## Israel Corporate Tax Strategy Skill v1.0

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Corporate tax, profit extraction methods for controlling shareholders |
| Currency | NIS (Israeli New Shekel — ₪) |
| Corporate tax rate | 23% flat on taxable profits |
| Dividend tax — controlling shareholder (10%+) | 30% |
| Dividend tax — non-controlling | 25% |
| Section 3(tet) deemed interest rate (2026) | 6.53% |
| Section 3(yod) rate (CPI-linked loans, 2026) | 4.9% |
| Surtax threshold | NIS 721,560 (frozen 2025–2027) |
| Credit point value | NIS 2,904/year (frozen 2025–2027) |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed רואה חשבון or יועץ מס |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown shareholder percentage | Treat as controlling shareholder (30% dividend tax) |
| Unknown Section 3(tet) rate | Use current year published rate |
| Unknown whether salary is below minimum | Flag minimum salary requirement for controlling shareholders |
| Unknown company type | Treat as closely held (Chevra Me'atim) |

## Section 2 — Extraction methods overview

Israeli company owners (Baalei Shlita — בעלי שליטה) have four main methods to extract value:

**Extraction methods overview table**

| Method | Corporate tax | Personal tax | Bituach Leumi | Key advantage |
| --- | --- | --- | --- | --- |
| **Salary (Maskoret — משכורת)** | 0% (deductible expense) | Progressive rates (10%–50%) | Employee + Employer NI | Tax credit points, pension deductions, NI ceiling |
| **Dividend (Dividend — דיבידנד)** | 23% (on profit first) | 30% (controlling shareholder) | None | No NI, simple, no employer cost beyond profit |
| **Shareholder loan (Halvaat Baalim — הלוואת בעלים)** | 0% (no immediate tax) | Section 3(tet) deemed interest | None | Defers real tax, keeps cash flexible |
| **Management fees (Dmei Nihul — דמי ניהול)** | 0% (deductible) | Income tax as business income + VAT 18% | Self-employed NI rates | Can deduct business expenses against fees |

### Combined effective tax rates (2026, controlling shareholder above surtax threshold)

**Combined effective tax rates table**

| Method | Effective rate (approximate) |
| --- | --- |
| Salary (top bracket) | ~55–60% (50% income tax + employer NI) |
| Dividend | 46.1% (up to ~52% with surtax) |
| Shareholder loan | 6.53% annual deemed interest (not a real extraction) |
| Management fees | ~50–55% + 18% VAT on gross |

## Section 3 — Dividend distribution (Halokat Dividendim — חלוקת דיבידנדים)

### 3.1 Tax calculation for controlling shareholder (10%+ holding)

- **Dividend tax calculation for controlling shareholder** — Company pre-tax profit:             P Corporate tax (23%):                P × 0.23 Distributable profit:               P × 0.77 Dividend withholding tax (30%):     P × 0.77 × 0.30 = P × 0.231 Net to shareholder:                 P × 0.77 × 0.70 = P × 0.539 Effective total tax rate:           46.1%  _(Section 3.1)_

### 3.2 Surtax impact (Mas Yesafim — מס יסף)

- **Surtax impact on dividends above threshold** — If total annual income (including dividend) exceeds NIS 721,560: 3% surtax on excess (Section 121B); Additional 2% on non-labor income above threshold (effective 2025+); Total additional: 5% on dividend portion above threshold; Effective rate climbs to ~49.95% on portion above threshold  _(Section 121B)_

### 3.3 When dividend is optimal

- **When dividend is optimal** — Shareholder's salary already maximizes lower tax brackets; Amount is large enough that salary would push into 47%+ bracket; Company has sufficient retained earnings (Arvei Rvaachim — ערכי רווחים); No Bituach Leumi advantage left (salary already above NI ceiling)

### 3.4 When dividend is suboptimal

- **When dividend is suboptimal** — Shareholder draws no or low salary (wasting lower brackets and credit points); Amount is moderate (under ~NIS 200,000) and salary brackets not fully utilized; Company needs the cash for operations (dividend is irreversible)

## Section 4 — Salary extraction (Maskoret — משכורת)

### 4.1 Income tax brackets (2026)

**Income tax brackets (2026)**

| Annual income (NIS) | Rate |
| --- | --- |
| Up to 84,120 | 10% |
| 84,121 – 120,720 | 14% |
| 120,721 – 228,000 | 20% |
| 228,001 – 301,200 | 31% |
| 301,201 – 560,280 | 35% |
| 560,281 – 721,560 | 47% |
| Above 721,560 | 50% (47% + 3% surtax) |

### 4.2 Bituach Leumi for controlling shareholder employees (2026)

**Bituach Leumi for controlling shareholder employees (2026)**

| Income range | Employee NI | Employee health | Employer NI |
| --- | --- | --- | --- |
| Up to NIS 7,703/month | 0.4% | 3.1% | 4.46% |
| NIS 7,703 – NIS 51,910/month | 7.0% | 5.0% | 7.38% |
| Above NIS 51,910/month | 0% (ceiling) | 0% (ceiling) | 0% (ceiling) |

- **NI rate difference from regular employees** — Controlling shareholder NI rates (4.46%/7.38% employer) differ slightly from regular employees (4.51%/7.60%).

### 4.3 Salary advantages

- **Salary advantages** — Pension contributions (Hafrashat Pensia — הפרשת פנסיה) are tax-deductible up to ceiling; Keren Hishtalmut contributions (up to ceiling) are employer-deductible, tax-free to employee; Tax credit points reduce effective rate on first brackets; NI contributions build social security entitlements

### 4.4 Optimal salary level

- **Optimal salary level** — The sweet spot is often drawing enough salary to utilize the lower tax brackets (up to ~NIS 228,000/year at 20% marginal rate) and maximize pension/Keren Hishtalmut deductions, then extracting additional amounts as dividends.

### 4.5 Minimum salary requirement

- **Minimum salary requirement** — The Tax Authority expects controlling shareholders to draw a reasonable salary (~NIS 6,500+/month) before distributing dividends.

## Section 5 — Shareholder loan (Halvaat Baalim — הלוואת בעלים)

### 5.1 Section 3(tet) rules (2026)

- **Section 3(tet) applicability** — When a company lends money to a shareholder at below-market interest, Section 3(tet) rules apply.

**Section 3(tet) rules table (2026)**

| Rule | Detail |
| --- | --- |
| Deemed interest rate (2026) | 6.53% per year |
| Treatment for controlling shareholders | Deemed interest classified as salary income, taxed at marginal rates |
| Reporting obligation | Company must report deemed interest on Form 126 |
| Section 3(yod) rate | 4.9% (for CPI-linked loans between related parties) |

### 5.2 Reclassification risks

**Reclassification risks table**

| Risk factor | Detail |
| --- | --- |
| Loan not repaid within reasonable time | ITA may reclassify as dividend (30% tax + penalties) |
| Loan used for personal expenses | Strengthens reclassification risk |
| No repayment schedule | Red flag for ITA |
| Company has retained earnings | Increases risk of deemed-dividend reclassification |

### 5.3 Worked example

- **Worked example — shareholder loan deemed interest** — Loan amount:                NIS 500,000 Annual deemed interest:     NIS 500,000 × 6.53% = NIS 32,650 Tax on deemed interest:     NIS 32,650 × 47% (marginal rate) = NIS 15,346 Net annual cost:            NIS 15,346 (3.07% of loan)  _(Section 5.3)_

Compare with dividend on the same NIS 500,000: tax of ~NIS 230,500 (46.1%). The loan defers this but accumulates cost annually.

### 5.4 When shareholder loan makes sense

- **When shareholder loan makes sense** — Short-term cash need (under 12 months) with clear repayment plan; Bridge financing until dividend declaration is approved; Company has a formal loan agreement with interest and repayment terms

### 5.5 When to avoid shareholder loans

- **When to avoid shareholder loans** — Long-term extraction need (accumulates deemed interest annually); Company has distributable retained earnings; No documented loan agreement or repayment schedule

## Section 6 — Management fees (Dmei Nihul — דמי ניהול)

### 6.1 How it works

- **Management fees mechanism** — 1. Shareholder (or their management company) invoices the company for management services 2. Company deducts the fee as a business expense (no corporate tax) 3. Fee is subject to income tax as business income + VAT (18%) 4. If through a personal Osek Murshe: subject to self-employed NI rates

### 6.2 Self-employed NI rates (2026)

**Self-employed NI rates (2026)**

| Income range | NI rate | Health rate | Total |
| --- | --- | --- | --- |
| Up to NIS 7,703/month | 2.87% | 3.1% | 5.97% |
| NIS 7,703 – NIS 51,910/month | 12.83% | 5.0% | 17.83% |

- **NI deductibility** — 52% of the NI amount is tax-deductible.

### 6.3 Requirements and risks

- **Management fees requirements and risks** — Transfer pricing rules apply (Section 85A) — fees must reflect arm's length market rates; ITA may challenge "excessive" management fees as disguised dividends; Must issue Heshbonit Mas (tax invoice); Requires maintaining a separate business entity with bookkeeping; Properly documented service agreements required  _(Section 85A)_

## Section 7 — Strategy comparison

### 7.1 Decision matrix

**Decision matrix table**

| Factor | Salary | Dividend | Loan | Management fees |
| --- | --- | --- | --- | --- |
| Total effective tax rate | 10%–60% | 46.1%–52% | 6.53% deemed/year | Variable + 18% VAT |
| Bituach Leumi | Yes (capped) | No | No | Yes (higher rates) |
| Corporate tax deductible | Yes | No | N/A | Yes |
| Pension benefits | Yes | No | No | Self-funded |
| Reversible | No | No | Yes (repay loan) | No |
| ITA scrutiny | Low | Low | High | Medium |
| Timing flexibility | Monthly | Board resolution | Immediate | Per invoice |

### 7.2 Common optimal combinations

**Common optimal combinations table**

| Scenario | Recommended approach |
| --- | --- |
| Small extraction (under NIS 200,000) | Salary up to the 20% bracket to maximize credit points and pension |
| Medium extraction (NIS 200,000 – 500,000) | Salary to optimize brackets + dividend for the remainder |
| Large extraction (NIS 500,000+) | Salary at optimal level + dividend; potentially short-term loan bridge |
| One-time tax assessment | Short-term shareholder loan with 12-month repayment, funded by planned dividend |

## Section 8 — Closely held companies (Chevra Me'atim — חברה מעטים)

- **Closely held company annual tax on undistributed profits** — A closely held company is subject to a 2% annual tax on accumulated undistributed profits unless at least 6% of accumulated profits are distributed as dividends. This rule creates pressure to distribute regularly rather than accumulating profits indefinitely within the company.

## Section 9 — Compliance checklist

**Compliance checklist table**

| Requirement | Check |
| --- | --- |
| Company has a CPA (Roe Cheshbon — רואה חשבון) | All strategies require professional filing |
| Board resolution for dividends | Required before distribution, must be documented |
| Loan agreement for shareholder loans | Written agreement with interest rate, repayment schedule, and signatures |
| Minimum salary for controlling shareholder | ITA expects ~NIS 6,500+/month before dividends |
| Withholding tax on dividends | Company must withhold 30% and deposit with ITA by the 15th of the following month |
| Form 856 reporting | Payments to shareholders must be reported |
| Section 3(tet) reporting | Deemed interest must be reported on Form 126 |
| Transfer pricing for management fees | Fees must reflect market rates |
| VAT invoice for management fees | Must issue Heshbonit Mas |
| Surtax reporting | Include all income sources when calculating surtax threshold |

## Section 10 — Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Israeli Tax Authority | https://www.gov.il/he/departments/israel_tax_authority |
| Income Tax Ordinance | https://www.nevo.co.il/law/70264 |
| Bituach Leumi — contribution rates | https://www.btl.gov.il/Insurance/National%20Insurance/Pages/default.aspx |
| Kol Zchut — income tax brackets | https://www.kolzchut.org.il/he/מדרגות_מס_הכנסה |

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
