---
name: il-corporate-tax
description: "Use this skill when advising on Israeli corporate tax strategy, profit extraction methods, or controlling shareholder (בעל שליטה) tax planning. Trigger on phrases like \"corporate tax Israel\", \"dividend vs salary Israel\", \"baal shlita\", \"בעל שליטה\", \"halokat dividendim\", \"חלוקת דיבידנדים\", \"shareholder loan Israel\", \"halvaat baalim\", \"הלוואת בעלים\", \"Section 3 tet\", \"סעיף 3 ט\", \"dmei nihul\", \"דמי ניהול\", \"management fees Israel\", \"chevra me'atim\", \"חברה מעטים\", or any Israeli corporate tax extraction query. ALWAYS read this skill before advising on Israeli corporate profit extraction."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-corporate-tax"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-03"
---

# IL Corporate Tax

## Israel Corporate Tax Strategy Skill v1.1

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1: Quick reference

**Quick reference table**

| Field | Value | Source |
| --- | --- | --- |
| Country | Israel (מדינת ישראל) | |
| Scope | Corporate tax, profit extraction methods for controlling shareholders | |
| Currency | NIS (Israeli New Shekel: ₪) | |
| Corporate tax rate | unverified: 23% flat on taxable profits | unverified |
| Dividend tax: controlling shareholder (10%+) | 30% (the Authority lists dividend rates for 2026 as 25% and 30%); unverified: that 30% is the rate for a 10%+ holder | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.118) |
| Dividend tax: non-controlling | 25% (same list) | same |
| Section 3(tet) interest rate (2026) | 6.53% (s.3(i) interest rate in the 2026 booklet); the s.3(i) loan ceiling linked to CPI rise is NIS 8,640 a year | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.15) |
| Section 3(yod) rate (CPI-linked loans, 2026) | unverified: 4.9% | unverified |
| Surtax threshold | NIS 721,560 a year for 2026 (unverified: frozen 2025 to 2027) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.11) |
| Credit point value | NIS 242 a month, NIS 2,904 a year, for 2026 (unverified: frozen 2025 to 2027) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.12) |
| Tax authority | Israel Tax Authority (ITA: רשות המיסים) |
| Contributor | Open Accountants Community |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown shareholder percentage | Treat as controlling shareholder (30% dividend tax) |
| Unknown Section 3(tet) rate | Use current year published rate |
| Unknown whether salary is below minimum | unverified: flag minimum salary requirement for controlling shareholders |
| Unknown company type | Treat as closely held (Chevra Me'atim) (unverified consequences, see Section 8) |

## Section 2: Extraction methods overview

Israeli company owners (Baalei Shlita: בעלי שליטה) have four main methods to extract value:

**Extraction methods overview table**

| Method | Corporate tax | Personal tax | Bituach Leumi | Key advantage |
| --- | --- | --- | --- | --- |
| **Salary (Maskoret: משכורת)** | 0% (deductible expense) | Progressive rates (10%–50%) | Employee + Employer NI | Tax credit points, pension deductions, NI ceiling |
| **Dividend (Dividend: דיבידנד)** | 23% (on profit first) | 30% (controlling shareholder) | None | No NI, simple, no employer cost beyond profit |
| **Shareholder loan (Halvaat Baalim: הלוואת בעלים)** | 0% (no immediate tax) | Section 3(tet) deemed interest | None | Defers real tax, keeps cash flexible |
| **Management fees (Dmei Nihul: דמי ניהול)** | 0% (deductible) | Income tax as business income + VAT 18% | Self-employed NI rates | Can deduct business expenses against fees |

### Combined effective tax rates (2026, controlling shareholder above surtax threshold)

**Combined effective tax rates table**

| Method | Effective rate (approximate) |
| --- | --- |
| Salary (top bracket) | ~55–60% (50% income tax + employer NI) |
| Dividend | 46.1% (up to ~52% with surtax) |
| Shareholder loan | 6.53% annual deemed interest (not a real extraction) |
| Management fees | ~50–55% + 18% VAT on gross |

## Section 3: Dividend distribution (Halokat Dividendim: חלוקת דיבידנדים)

### 3.1 Tax calculation for controlling shareholder (10%+ holding)

- **Dividend tax calculation for controlling shareholder**: Company pre-tax profit:             P Corporate tax (23%):                P × 0.23 Distributable profit:               P × 0.77 Dividend withholding tax (30%):     P × 0.77 × 0.30 = P × 0.231 Net to shareholder:                 P × 0.77 × 0.70 = P × 0.539 Effective total tax rate:           46.1%  _(Section 3.1)_

### 3.2 Surtax impact (Mas Yesafim: מס יסף)

- **Surtax impact on dividends above threshold** (2026 booklet p.11, s.121B): 3% on the part of total taxable income above NIS 721,560; plus 2% on taxable income from capital sources above that amount. These are two bases: work out each one; do not apply a flat 5% to the whole dividend once total income passes the threshold. unverified: that a dividend counts as capital-source income for the 2% charge, and the ~49.95% effective rate  _(Section 121B)_

### 3.3 When dividend is optimal

- **When dividend is optimal**: Shareholder's salary already maximizes lower tax brackets; Amount is large enough that salary would push into 47%+ bracket; Company has sufficient retained earnings (Arvei Rvaachim: ערכי רווחים); No Bituach Leumi advantage left (salary already above NI ceiling)

### 3.4 When dividend is suboptimal

- **When dividend is suboptimal**: Shareholder draws no or low salary (wasting lower brackets and credit points); Amount is moderate (under ~NIS 200,000) and salary brackets not fully utilized; Company needs the cash for operations (dividend is irreversible)

## Section 4: Salary extraction (Maskoret: משכורת)

### 4.1 Income tax brackets (2026)

**Income tax brackets (2026)**

Income from personal exertion (salary is), 2026:

| Annual income (NIS) | Rate | Source |
| --- | --- | --- |
| Up to 84,120 | 10% | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.10) |
| 84,121 – 120,720 | 14% | same |
| 120,721 – 228,000 | 20% | same |
| 228,001 – 301,200 | 31% | same |
| 301,201 – 560,280 | 35% | same |
| 560,281 – 721,560 | 47% | same |
| Above 721,560 | 50% (47% + 3% surtax) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.11) |

### 4.2 Bituach Leumi for controlling shareholder employees (2026)

**Bituach Leumi for controlling shareholder employees (2026)**

Column 2 of the National Insurance employee table: a controlling shareholder in a closely held company (holds at least 10% of the shares or the right to appoint a director), aged 18 and under retirement age.

| Income range | Employee total (NI plus health) | Share of health in total | Employer NI | Source |
| --- | --- | --- | --- | --- |
| Up to NIS 7,703/month (from 01.01.2026) | 4.25% | 3.23% | 4.46% | https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx |
| NIS 7,703 – NIS 51,910/month (from 01.01.2026) | 11.96% | 5.17% | 7.38% | same |
| Above NIS 51,910/month | 0% (ceiling) | 0% (ceiling) | 0% (ceiling) | same |

- **NI rate difference from regular employees**: Controlling shareholder employer rates (4.46%/7.38%) differ slightly from an ordinary resident employee in column 1 (4.51%/7.60%) (National Insurance employee page).

### 4.3 Salary advantages

- **Salary advantages**: Pension contributions (Hafrashat Pensia: הפרשת פנסיה) are tax-deductible up to ceiling; Keren Hishtalmut contributions (up to ceiling) are employer-deductible, tax-free to employee; Tax credit points reduce effective rate on first brackets; NI contributions build social security entitlements

### 4.4 Optimal salary level

- **Optimal salary level**: The sweet spot is often drawing enough salary to utilize the lower tax brackets (up to ~NIS 228,000/year at 20% marginal rate) and maximize pension/Keren Hishtalmut deductions, then extracting additional amounts as dividends.

### 4.5 Minimum salary requirement

- **Minimum salary requirement**: unverified: the Tax Authority expects controlling shareholders to draw a reasonable salary (~NIS 6,500+/month) before distributing dividends.

## Section 5: Shareholder loan (Halvaat Baalim: הלוואת בעלים)

### 5.1 Section 3(tet) rules (2026)

- **Section 3(tet) applicability**: When a company lends money to a shareholder at below-market interest, Section 3(tet) rules apply.

**Section 3(tet) rules table (2026)**

| Rule | Detail | Source |
| --- | --- | --- |
| Interest rate under s.3(i) (2026) | 6.53% per year | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf (p.15) |
| Treatment for controlling shareholders | unverified: deemed interest classified as salary income, taxed at marginal rates | unverified |
| Reporting obligation | unverified: company must report deemed interest on Form 126 | unverified |
| Section 3(yod) rate | unverified: 4.9% (for CPI-linked loans between related parties) | unverified |

The 6.53% is the prescribed s.3(i) interest rate. It is not a tax on the loan principal and not a safe harbour against the Authority treating the withdrawal as a dividend or salary; see 5.2.

### 5.2 Reclassification risks

**Reclassification risks table**

unverified: every row of this table.

| Risk factor | Detail |
| --- | --- |
| Loan not repaid within reasonable time | ITA may reclassify as dividend (30% tax + penalties) |
| Loan used for personal expenses | Strengthens reclassification risk |
| No repayment schedule | Red flag for ITA |
| Company has retained earnings | Increases risk of deemed-dividend reclassification |

### 5.3 Worked example

- **Worked example: shareholder loan deemed interest** (the 6.53% is from the 2026 booklet; unverified: the 47% marginal treatment): Loan amount:                NIS 500,000 Annual deemed interest:     NIS 500,000 × 6.53% = NIS 32,650 Tax on deemed interest:     NIS 32,650 × 47% (marginal rate) = NIS 15,346 Net annual cost:            NIS 15,346 (3.07% of loan)  _(Section 5.3)_

Compare with dividend on the same NIS 500,000: tax of ~NIS 230,500 (46.1%). The loan defers this but accumulates cost annually.

### 5.4 When shareholder loan makes sense

- **When shareholder loan makes sense**: Short-term cash need (under 12 months) with clear repayment plan; Bridge financing until dividend declaration is approved; Company has a formal loan agreement with interest and repayment terms

### 5.5 When to avoid shareholder loans

- **When to avoid shareholder loans**: Long-term extraction need (accumulates deemed interest annually); Company has distributable retained earnings; No documented loan agreement or repayment schedule

## Section 6: Management fees (Dmei Nihul: דמי ניהול)

### 6.1 How it works

- **Management fees mechanism**: 1. Shareholder (or their management company) invoices the company for management services 2. Company deducts the fee as a business expense (no corporate tax) 3. Fee is subject to income tax as business income + VAT (18%) 4. If through a personal Osek Murshe: subject to self-employed NI rates

### 6.2 Self-employed NI rates (2026)

**Self-employed NI rates (2026)**

Self-employed aged 18 and under retirement age.

| Income range | NI rate | Health rate | Total | Source |
| --- | --- | --- | --- | --- |
| Up to NIS 7,703/month (from 01.01.2026) | 4.47% | 3.23% | 7.70% | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx |
| NIS 7,703 – NIS 51,910/month | 12.83% | 5.17% | 18.00% | same |

- **NI deductibility**: unverified: 52% of the NI amount is tax-deductible.

### 6.3 Requirements and risks

- **Management fees requirements and risks**: Transfer pricing rules apply (Section 85A): fees must reflect arm's length market rates; ITA may challenge "excessive" management fees as disguised dividends; Must issue Heshbonit Mas (tax invoice); Requires maintaining a separate business entity with bookkeeping; Properly documented service agreements required  _(Section 85A)_

## Section 7: Strategy comparison

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

## Section 8: Closely held companies (Chevra Me'atim: חברה מעטים)

- **Closely held company annual tax on undistributed profits**: unverified (the provision was not opened): A closely held company is subject to a 2% annual tax on accumulated undistributed profits unless at least 6% of accumulated profits are distributed as dividends. This rule creates pressure to distribute regularly rather than accumulating profits indefinitely within the company.

## Section 9: Compliance checklist

**Compliance checklist table**

| Requirement | Check |
| --- | --- |
| Company has a CPA (Roe Cheshbon: רואה חשבון) | All strategies require professional filing |
| Board resolution for dividends | Required before distribution, must be documented |
| Loan agreement for shareholder loans | Written agreement with interest rate, repayment schedule, and signatures |
| Minimum salary for controlling shareholder | unverified: ITA expects ~NIS 6,500+/month before dividends |
| Withholding tax on dividends | unverified: company must withhold 30% and deposit with ITA by the 15th of the following month |
| Form 856 reporting | Payments to shareholders must be reported |
| Section 3(tet) reporting | Deemed interest must be reported on Form 126 |
| Transfer pricing for management fees | Fees must reflect market rates |
| VAT invoice for management fees | Must issue Heshbonit Mas |
| Surtax reporting | Include all income sources when calculating surtax threshold |

## Section 10: Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Israeli Tax Authority | https://www.gov.il/he/departments/israel_tax_authority |
| Income Tax Ordinance | https://www.nevo.co.il/law/70264 |
| Bituach Leumi: contribution rates | https://www.btl.gov.il/Insurance/National%20Insurance/Pages/default.aspx |
| Kol Zchut: income tax brackets | https://www.kolzchut.org.il/he/מדרגות_מס_הכנסה |

## Recomputed checks (2026)

```oa-check
name: Dividend from NIS 100,000 profit, 10% holder
inputs:
  p: 100000
steps:
  - c: p*0.23
  - d: (p-c)*0.30
  - t: c+d
expected:
  t: 46100
```

```oa-check
name: Deemed interest, NIS 500,000 loan (2026)
inputs:
  l: 500000
steps:
  - i: l*0.0653
expected:
  i: 32650
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Israel Tax Authority, salary-deduction booklet from January 2026 (updated April 2026), read p.10 (2026 bands), p.11 (s.121B surtax), p.12 (credit point), p.15 (s.3(i) interest rate 6.53%, s.3(i) ceiling NIS 8,640) | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-03 |
| Israel Tax Authority, "Know your rights and duties" guide, tax year 2025 (published July 2026), read PDF p.118 (special-rate income for tax year 2026: dividend 25%, 30%) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-03 |
| National Insurance, employee rates page, read the NIS 7,703 band and NIS 51,910 ceiling from 01.01.2026 and the column 1 and column 2 (controlling shareholder) working-age rates | https://www.btl.gov.il/Insurance/Rates/Pages/%D7%9C%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D%20%D7%A9%D7%9B%D7%99%D7%A8%D7%99%D7%9D.aspx | 2026-11-03 |
| National Insurance, self-employed rates page, read the working-age table from 01.01.2026 | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/Self_Employed/Pages/rates.aspx | 2026-11-03 |

Not yet confirmed: the 23% corporate rate (and so the 46.1% combined figure and the first worked check); which holder takes the 30% dividend rate (the guide lists 25% and 30% without saying); the s.3(yod) 4.9% rate; the treatment of s.3(i) interest as salary, its Form 126 reporting and the reclassification risks; closely held company 2% tax and the 6% distribution condition; NIS 6,500 salary expectation; the split of controlling shareholder employee contributions between National Insurance and health (the page gives totals); 52% deductibility; dividend withholding and its deposit date; whether a dividend is capital-source income for the 2% surtax; the effective-rate tables in Sections 2 and 7.

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional: such as a רואה חשבון (Ro'eh Cheshbon: CPA) or יועץ מס (Yo'etz Mas: tax advisor) licensed in Israel: before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
