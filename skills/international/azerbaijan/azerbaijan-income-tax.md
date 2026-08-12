---
name: azerbaijan-income-tax
description: Use this skill whenever asked about Azerbaijan personal income tax for individuals, employees, and self-employed individual entrepreneurs. Trigger on phrases like "how much income tax do I pay in Azerbaijan", "Azerbaijan payroll tax", "DSMF social insurance", "simplified tax regime", "individual entrepreneur tax", "private non-oil sector holiday", "oil and gas sector tax", "annual income tax return Azerbaijan", "AZN withholding", "compulsory medical insurance", "unemployment insurance contribution", "taxes.gov.az", or any question about computing, withholding, or filing personal income tax in the Republic of Azerbaijan. Also trigger when classifying AZN bank-statement lines for an individual entrepreneur, computing payroll deductions, or advising on the 2025 holiday regime versus the 2026 progressive reform. This skill covers personal income tax brackets (private non-oil, oil/gas/public, 2026 reform), DSMF/UIC/medical contributions, the simplified-tax regime, micro-entrepreneur exemptions, filing deadlines, and penalties. ALWAYS read this skill before touching any Azerbaijan income tax work.
version: 0.1
jurisdiction: AZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Income Tax -- Individuals & Self-Employed

## Azerbaijan Income Tax -- Individuals & Self-Employed Skill v0.1

> **CONFIDENCE: MEDIUM.** Several figures rely on Big-4 (PwC) and reputable local-firm summaries rather than direct extraction from the Azeri-language Tax Code, and the figures span a major regime change at 1 January 2026 (the 7-year private non-oil holiday expired 31 December 2025). Items marked **[RESEARCH GAP — reviewer to confirm]** must be reconfirmed against the official portal at [taxes.gov.az](https://www.taxes.gov.az/en) before any return is filed.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Azerbaijan |
| Tax | Personal income tax (gəlir vergisi) on individuals + individual entrepreneurs |
| Currency | AZN only (Azerbaijani manat) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Tax Code of the Republic of Azerbaijan (Income Tax of Individuals chapter; exemptions Article 102; financial sanctions Article 58; late-payment interest Article 59) |
| Supporting legislation | Law on Social Insurance; Law on Unemployment Insurance; Law on Medical Insurance |
| Tax authority | State Tax Service under the Ministry of Economy (Dövlət Vergi Xidməti) |
| Social security body | State Social Protection Fund (DSMF/SSPF), Ministry of Labour and Social Protection of Population |
| Filing portal | taxes.gov.az |
| Filing deadline | 31 March of the following year (annual return) [PwC] |
| Validated by | Pending — requires sign-off by an Azerbaijani tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Personal Income Tax Brackets — 2025 (current tax year)

**Private non-oil/non-gas sector employees — 7-year holiday (1 Jan 2019 – 31 Dec 2025) [PwC]**  _(PwC)_

| Monthly income (AZN) | Rate | Cumulative tax at top |
| --- | --- | --- |
| 0 -- 8,000 | 0% | AZN 0 |
| above 8,000 | 14% of the amount exceeding 8,000 | — |

*Example: AZN 10,000/month → 14% × (10,000 − 8,000) = AZN 280.*

**Oil/gas sector and government/public sector employees (also the standard rate after the holiday ends) [PwC]**  _(PwC)_

| Monthly income (AZN) | Rate | Cumulative tax at top |
| --- | --- | --- |
| 0 -- 2,500 | 14% | AZN 350 |
| above 2,500 | AZN 350 + 25% of the amount exceeding 2,500 | — |

*Example: AZN 4,000/month → 350 + 25% × (4,000 − 2,500) = 350 + 375 = AZN 725.*

### Personal Income Tax Brackets — 2026 (CONFIRMED REFORM)

**Private non-oil/non-gas sector employees — NEW progressive regime, effective 1 Jan 2026 [Mercans]**  _(Mercans)_

| Monthly income (AZN) | Rate | Cumulative tax at top |
| --- | --- | --- |
| 0 -- 2,500 | 3% | AZN 75 |
| 2,501 -- 8,000 | 10% | AZN 625 |
| above 8,000 | 14% of the amount exceeding 8,000 | — |

*The lowest band rises to 5% in 2027 and 7% from 2028.* [Mercans]
*Example: AZN 5,000/month → (3% × 2,500) + (10% × 2,500) = 75 + 250 = AZN 325.*

> **2026 transition note.** From 1 Jan 2026 the holiday ends; **no income is fully exempt** for private non-oil employees. Apply the 3%/10%/14% schedule above. The interaction of the new progressive regime with the AZN 200/month personal exemption (Section 1, below) is **[RESEARCH GAP — reviewer to confirm]** against the published 2026 Tax Code text.

### Self-Employed / Individual Entrepreneur Regimes — 2025

**Self-Employed / Individual Entrepreneur Regimes — 2025**  _(ExpertSM)_

| Regime | Rate | Notes |
| --- | --- | --- |
| General regime (entrepreneurial profit) | 20% on net taxable profit [ExpertSM] | Plus VAT if turnover exceeds AZN 200,000 |
| Simplified tax regime | 2% of gross revenue/turnover [ExpertSM] | Replaces PIT, profit tax, VAT, asset tax. **[RESEARCH GAP — reviewer to confirm]** — older sources cite 4% Baku / 2% regions; confirm current split with the State Tax Service |

### Personal Exemptions and Payroll Reference (2025)

**Personal Exemptions and Payroll Reference (2025)**  _(PwC/APA/GRATA)_

| Item | Value | Source |
| --- | --- | --- |
| Minimum monthly wage | AZN 400/month (from 1 Jan 2025; unchanged into 2026) | APA |
| Personal monthly exemption (oil/gas & public sector, primary workplace, monthly income below AZN 2,500) | AZN 200/month (AZN 2,400/year where annual income below AZN 30,000) | GRATA |
| Withholding method | Employers withhold income tax + social/medical/unemployment at source (PAYE-style); withheld income tax transferred same day as payment | PwC |
| VAT standard rate | 18% | PwC |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Sector unknown for an employee | Treat as **private non-oil/non-gas** (dominant case) but FLAG: oil/gas/public faces the 14%/25% schedule and 22% employer DSMF |
| Tax year unknown | Confirm year. 2025 = holiday regime; 2026 = progressive regime. STOP if not confirmed |
| Simplified vs general regime unknown | Confirm with client; do not assume |
| Simplified tax rate unknown | 2% of gross turnover; flag for Baku 4% verification |
| Self-employed social-insurance % unknown | STOP — activity/region-dependent and not published in secondary sources **[RESEARCH GAP — reviewer to confirm]** |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) the tax year, (b) employment sector (private non-oil / oil-gas / public), or (c) self-employment regime (general 20% / simplified 2%).

**Recommended** -- payroll registers, DSMF / medical / unemployment contribution records, prior-year annual return, VAT registration status, monthly gross wage breakdown.

**Ideal** -- complete income and expenditure account for the entrepreneur, asset register, quarterly advance-payment confirmations, employment income details, and confirmation of micro-entrepreneur exemption eligibility.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without supporting records = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify the sector/regime, that all deductions are supported, and that the correct tax year's rates were applied."

### Refusal Catalogue

- **R-AZ-1** — "Azerbaijan changed its personal income tax regime on 1 January 2026, and the rate depends on whether the employee is private non-oil, oil/gas, or public sector. This skill cannot compute tax without the tax year AND the sector. Please confirm before proceeding."  _(R-AZ-1 -- Tax year / sector unknown)_
- **R-AZ-2** — "Self-employed / individual-entrepreneur social-insurance percentages are activity- and region-dependent and are not published in authoritative secondary sources. [RESEARCH GAP — reviewer to confirm.] Escalate to an Azerbaijani tax professional for the exact rate."  _(R-AZ-2 -- Self-employed social insurance)_
- **R-AZ-3** — "This skill covers individuals and individual entrepreneurs only. Legal entities pay 20% corporate profit tax and file separately. Escalate to an Azerbaijani tax professional."  _(R-AZ-3 -- Companies and partnerships)_
- **R-AZ-4** — "Non-residents are taxed only on Azerbaijan-source income and withholding rates differ (dividends 5%, interest 10%, rent/royalties 14%, non-resident no-PE income generally 10%). Treaty analysis is out of scope. Escalate to an Azerbaijani tax professional."  _(R-AZ-4 -- Non-resident / cross-border income)_
- **R-AZ-5** — "Client has outstanding tax arrears or is subject to State Tax Service enforcement. Late-payment interest accrues at 0.1%/day and an understatement sanction of 50% of the underreported tax may apply (Article 58). Do not advise. Escalate immediately."  _(R-AZ-5 -- Arrears / enforcement)_
- **R-AZ-6** — "This skill covers personal income tax only. For Azerbaijan VAT (standard rate 18%, registration at AZN 200,000), use a dedicated VAT skill."  _(R-AZ-6 -- VAT return requested)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Azerbaijani and English terms are both listed). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + KÖÇÜRMƏ (transfer), ÖDƏNİŞ (payment), DAXİLOLMA | Gross revenue | Business income | If VAT-registered, extract net (excl. 18% VAT) |
| QONORAR (fee), XİDMƏT HAQQI (service fee), KONSULTASİYA | Gross revenue | Business income | Professional/service fees |
| STRIPE PAYOUT, PAYPAL, WISE, PAYONEER | Gross revenue | Business income | Platform payout — match to underlying invoices |
| UPWORK, FIVERR, FREELANCE | Gross revenue | Business income | Net of platform commission |
| ƏMƏK HAQQI (salary), MAAŞ (wage), EMPLOYER [name] | Employment income | Employment income | Subject to PAYE withholding — NOT entrepreneurial income |
| İCARƏ (rent received), KİRAYƏ | Rental income | Rental income | Rent/royalty WHT 14% may apply [PwC] |
| FAİZ (interest received) | Investment income | Interest income | Interest WHT 10% [PwC] |
| DİVİDEND | Investment income | Investment income | Dividend WHT 5% [PwC] |
| VERGİ QAYTARILMASI (tax refund) | EXCLUDE | Not income | Refund of prior-year tax |

### 3.2 Expense Patterns (Debits) -- Deductible (General-regime entrepreneur)

**3.2 Expense Patterns (Debits) -- Deductible (General-regime entrepreneur)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFİS İCARƏSİ (office rent), OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| MÜHASİB (accountant), AUDİT, BOOKKEEP | Accountancy fees | Deductible |  |
| VƏKİL (lawyer), HÜQUQ (legal) | Legal fees | Deductible | Must be business-related |
| OFİS LƏVAZİMATI (office supplies), STATIONERY | Office supplies | Deductible |  |
| REKLAM (advertising), GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| TƏLİM (training), KURS (course), SEMİNAR | Training | Deductible | Must relate to current business |
| BANK HAQQI (bank fee), KOMİSSİYA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, AWS, CLOUD | IT infrastructure | Deductible | Capitalise if a long-lived asset |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**3.3 Expense Patterns (Debits) -- SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| Perpetual software licence (long-lived) | Capital item | Depreciate | Asset, not period expense |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| AZƏRİŞIQ (electricity), AZƏRSU (water) | Electricity/water | T2 if home office | 100% if dedicated office; proportional if home |
| AZTELEKOM, BAKCELL, NAR, AZERCELL (broadband) | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, ƏLAQƏ (communications) | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AZAL, AZERBAIJAN AIRLINES, TURKISH AIRLINES, PEGASUS | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAXI | Local transport | Deductible if business purpose |  |
| BENZİN (petrol), YANACAQ (fuel), SOCAR PETROL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKİNG (parking) | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORAN (restaurant), NAHAR (lunch), QONAQLIQ (entertainment) | Entertainment | NOT deductible | Private/entertainment |
| MARKET, SUPERMARKET, BAZARSTORE, ARAZ MARKET | Personal/groceries | NOT deductible | Private living costs |
| CƏRİMƏ (fine), PENALTY | Fines/penalties | NOT deductible | Public policy |
| VERGİ ÖDƏNİŞİ (tax payment), GƏLİR VERGİSİ | Tax payments | NOT deductible | Income tax cannot reduce income |
| ŞƏXSİ (personal), CASH ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate)

**3.7 Expense Patterns (Debits) -- Capital Items (depreciate)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, KOMPÜTER, MACBOOK, DESKTOP | Computer hardware | Capitalise & depreciate | Depreciation rates per Tax Code **[RESEARCH GAP — reviewer to confirm exact %]** |
| PRINTER, SCANNER | Office equipment | Capitalise & depreciate | **[RESEARCH GAP — reviewer to confirm exact %]** |
| MEBEL (furniture), MASA (desk), STUL (chair) | Furniture/fittings | Capitalise & depreciate | **[RESEARCH GAP — reviewer to confirm exact %]** |
| AVTOMOBİL (vehicle) | Motor vehicle | Capitalise & depreciate | Business % only |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DAXİLİ KÖÇÜRMƏ (internal transfer), OWN ACCOUNT | EXCLUDE | Own-account transfer |
| KREDİT ÖDƏNİŞİ (loan repayment), BORC | EXCLUDE | Loan principal movement |
| DSMF, SOSİAL SIĞORTA (social insurance) | Contribution payment | Withheld/contributed — see Section 5; not a Box 2 trade expense |
| TİBBİ SIĞORTA (medical insurance), İŞSİZLİK SIĞORTASI (unemployment) | Contribution payment | Statutory contribution — see Section 5 |
| ƏDV ÖDƏNİŞİ (VAT payment) | EXCLUDE | VAT liability payment, not expense |
| AVANS VERGİ (advance tax instalment) | Credit against liability | Quarterly advance — credit, not expense |

### 3.9 Azerbaijani Banks -- Statement Format Reference

**3.9 Azerbaijani Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Kapital Bank | KÖÇÜRMƏ, ÖDƏNİŞ, KOMİSSİYA | PDF/CSV; date format DD.MM.YYYY |
| PASHA Bank | TRANSFER, PAYMENT, FEE | PDF/CSV; counterparty in description |
| ABB (International Bank of Azerbaijan) | KÖÇÜRMƏ, DAXİLOLMA, HAQQI | PDF; AZN and FX accounts |
| Bank Respublika | ÖDƏNİŞ, İCARƏ, MAAŞ | PDF/CSV |
| Unibank / Leobank | PAYMENT, CARD, TRANSFER | CSV; clean counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- Private Non-Oil Employee, 2025 (Holiday Regime)

**Input line:**
`15.02.2025 ; KAPITAL BANK ; ƏMƏK HAQQI ; TECH STUDIO LLC FEB MAAŞ ; +6,000.00 ; AZN`

**Reasoning:**
Private non-oil/non-gas employee, monthly gross AZN 6,000, 2025 holiday regime. Income up to AZN 8,000 is taxed at **0%** [PwC]. Income tax = AZN 0. (Social/medical/unemployment contributions still apply — see Example 5.)

**Classification:** Monthly income tax = AZN 0 (holiday band).

### Example 2 -- Private Non-Oil Employee Above the Holiday Ceiling, 2025

**Input line:**
`28.02.2025 ; PASHA BANK ; MAAŞ ; FINTECH AZ LLC ; +10,000.00 ; AZN`

**Reasoning:**
Monthly gross AZN 10,000, private non-oil, 2025. First AZN 8,000 at 0%; excess taxed at 14% [PwC]. Tax = 14% × (10,000 − 8,000) = 14% × 2,000 = **AZN 280**.

**Classification:** Monthly income tax = AZN 280.

### Example 3 -- Oil/Gas Sector Employee, 2025

**Input line:**
`28.02.2025 ; ABB ; ƏMƏK HAQQI ; SOCAR DOWNSTREAM ; +4,000.00 ; AZN`

**Reasoning:**
Oil/gas sector employee, monthly gross AZN 4,000, 2025. Schedule: 14% up to AZN 2,500, then AZN 350 + 25% on the excess [PwC]. Tax = 350 + 25% × (4,000 − 2,500) = 350 + 375 = **AZN 725**. Employer DSMF on this sector is 22% of gross.

**Classification:** Monthly income tax = AZN 725.

### Example 4 -- Private Non-Oil Employee, 2026 (Progressive Reform)

**Input line:**
`31.01.2026 ; UNIBANK ; MAAŞ ; DESIGN HOUSE LLC ; +5,000.00 ; AZN`

**Reasoning:**
From 1 Jan 2026 the holiday is gone; the progressive schedule applies [Mercans]: 3% on the first AZN 2,500, then 10% on AZN 2,501–8,000. Tax = (3% × 2,500) + (10% × (5,000 − 2,500)) = 75 + 250 = **AZN 325**.

**Classification:** Monthly income tax = AZN 325.

### Example 5 -- DSMF Social Insurance, Private Non-Oil Employee, 2025

**Input line (gross wage):**
`AZN 6,000 monthly gross — private non-oil sector employee`

**Reasoning (employee DSMF):**
2025 private non-oil employee DSMF = 3% on the first AZN 200, then AZN 6 + 10% on the portion above AZN 200 [PwC]. Compute: 3% × 200 = AZN 6 (the stated AZN 6 base reconciles); plus 10% × (6,000 − 200) = 10% × 5,800 = AZN 580. Employee DSMF = 6 + 580 = **AZN 586**.

> **[RESEARCH GAP — reviewer to confirm]** The PwC employer formula is stated as "2% on first AZN 200; **AZN 44** + 15% on the portion above AZN 200." Arithmetically, 2% × AZN 200 = AZN 4, not AZN 44, so the AZN 44 base does not reconcile to a 2% rate on the first AZN 200. Confirm the correct employer base figure with the State Tax Service before relying on it. Using the formula as published: employer DSMF on AZN 6,000 = 44 + 15% × 5,800 = 44 + 870 = **AZN 914** (per source, base unverified).

**Classification:** Employee DSMF = AZN 586 (verified); employer DSMF = AZN 914 per published formula (base flagged).

### Example 6 -- Individual Entrepreneur on the Simplified Regime, 2025

**Input line:**
`10.03.2025 ; LEOBANK ; XİDMƏT HAQQI ; CLIENT ABC ; +12,000.00 ; AZN`

**Reasoning:**
Individual entrepreneur under the simplified tax regime (annual turnover not exceeding AZN 200,000, not VAT-registered). Tax = 2% of gross turnover [ExpertSM/Deel]. On this AZN 12,000 receipt: 2% × 12,000 = **AZN 240**. The simplified tax replaces PIT, profit tax, VAT and asset tax.

> **[RESEARCH GAP — reviewer to confirm]** If the entrepreneur operates in Baku, older sources cite a 4% rate. Confirm the current statutory rate split with the State Tax Service before applying 2%.

**Classification:** Simplified tax = AZN 240 on this receipt.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residence and Scope

- **Residence and scope** — Residents are taxed on worldwide income; non-residents are taxed only on Azerbaijan-source income [PwC]. Confirm residence before computing.  _(Tax Code of the Republic of Azerbaijan; PwC)_

### 5.2 Personal Income Tax — 2025 by Sector

**5.2 Personal Income Tax — 2025 by Sector**  _(PwC)_

| Sector | Schedule (monthly) | Source |
| --- | --- | --- |
| Private non-oil/non-gas (holiday) | 0% up to AZN 8,000; 14% on the excess | PwC |
| Oil/gas + government/public | 14% up to AZN 2,500; AZN 350 + 25% on the excess | PwC |

The 7-year holiday ran 1 Jan 2019 – 31 Dec 2025 for private non-oil/non-gas employees [PwC].

### 5.3 Personal Income Tax — 2026 Reform (private non-oil)

- **2026 reform schedule** — From 1 Jan 2026 [Mercans]: 3% up to AZN 2,500; 10% on AZN 2,501–8,000; 14% above AZN 8,000. The lowest band rises to 5% in 2027 and 7% from 2028.  _(Mercans)_

### 5.4 Social Insurance (DSMF) — 2025

**5.4 Social Insurance (DSMF) — 2025**  _(PwC)_

| Party / sector | Rate | Source |
| --- | --- | --- |
| Employee — private non-oil | 3% on first AZN 200; AZN 6 + 10% above AZN 200 | PwC |
| Employer — private non-oil | 2% on first AZN 200; AZN 44 + 15% above AZN 200 **[base flagged — see Example 5]** | PwC |
| Employee — oil/gas & government | 3% of gross monthly salary | PwC |
| Employer — oil/gas & government | 22% of gross monthly salary | PwC |

- **2026 reform DSMF change** — **2026 reform:** the combined DSMF rate on the wage portion **above AZN 8,000** (private non-oil) drops from 25% to **21% (10% employee + 11% employer)**; the portion up to AZN 8,000 is unchanged [Mercans]. Self-check: 10% + 11% = 21% (combined column reconciles).  _(Mercans)_

### 5.5 Unemployment Insurance Contribution (UIC) — 2025

**5.5 Unemployment Insurance Contribution (UIC) — 2025**  _(PwC)_

| Party | Rate | Source |
| --- | --- | --- |
| Employee | 0.5% of gross salary | PwC |
| Employer | 0.5% of gross salary | PwC |
| **Combined** | **1.0%** | PwC |

Self-check: 0.5% + 0.5% = 1.0% (combined reconciles).

### 5.6 Compulsory Medical Insurance — 2025

**5.6 Compulsory Medical Insurance — 2025**  _(PwC)_

| Income band | Employee | Employer | Source |
| --- | --- | --- | --- |
| Up to AZN 8,000 | 2% | 2% | PwC |
| Above AZN 8,000 | AZN 160 + 0.5% on the excess | AZN 160 + 0.5% on the excess | PwC |

Self-check: at exactly AZN 8,000, 2% × 8,000 = AZN 160 — so the AZN 160 base reconciles to the cap of the lower band for each party.

### 5.7 Self-Employed / Individual Entrepreneur

**5.7 Self-Employed / Individual Entrepreneur**  _(ExpertSM/Deel)_

| Regime | Rate | Notes |
| --- | --- | --- |
| General | 20% on net taxable profit [ExpertSM] | Plus VAT if turnover > AZN 200,000 |
| Simplified | 2% of gross turnover [ExpertSM/Deel] | Eligibility: turnover ≤ AZN 200,000 and not VAT-registered; replaces PIT, profit tax, VAT, asset tax |

- **Self-employed social insurance research gap** — **Self-employed social insurance** is activity- and region-dependent (minimum-wage-based multiples apply); exact percentages were not found in authoritative secondary sources **[RESEARCH GAP — reviewer to confirm]** [PwC].  _(PwC)_

### 5.8 Withholding Tax on Non-Employment Income

**5.8 Withholding Tax on Non-Employment Income**  _(PwC)_

| Income type | Rate | Source |
| --- | --- | --- |
| Dividends | 5% | PwC |
| Interest | 10% | PwC |
| Rent / royalties | 14% | PwC |
| Non-resident, no-PE income (general) | 10% | PwC |
| Non-resident leasing / insurance | 4% | PwC |
| Non-resident telecom / transport | 6% | PwC |

### 5.9 VAT Interaction

**5.9 VAT Interaction**  _(PwC/ExpertSM/Deel)_

| Scenario | Income Tax Treatment | Source |
| --- | --- | --- |
| Standard VAT rate | 18% | PwC |
| Mandatory VAT registration | Taxable turnover > AZN 200,000 in any 12 consecutive months (or single transaction over the threshold) | PwC |
| VAT collected on sales (VAT-registered) | NOT income — exclude | — |
| Simplified-regime entrepreneur | Cannot be VAT-registered; VAT does not apply | ExpertSM/Deel |

### 5.10 Exemptions

**5.10 Exemptions**  _(GRATA/PwC/Caspian Legal Center)_

| Exemption | Detail | Source |
| --- | --- | --- |
| Personal monthly exemption (oil/gas & public, primary workplace) | AZN 200/month where monthly income below AZN 2,500 (AZN 2,400/year where annual income below AZN 30,000) | GRATA |
| Private non-oil employees (2025) | Were under the 0% holiday band rather than the AZN 200 exemption | PwC |
| Micro-entrepreneur 75% income exemption | See Section 6.1 | Caspian Legal Center |

### 5.11 Filing and Payment

**5.11 Filing and Payment**  _(PwC)_

| Item | Detail | Source |
| --- | --- | --- |
| Annual income tax return | Due **31 March** of the following year (3-month extension possible if tax already paid) | PwC |
| Who must file | Residents with income not taxed at source or foreign income; non-residents with Azeri-source income not subject to withholding; individual entrepreneurs | PwC |
| Quarterly advance payments (independent entrepreneurs) | No later than the **15th** of the month following each quarter; final payment by 31 March | PwC |
| Cessation declaration | Within **30 days** of stopping business activity | PwC |
| Withheld income tax | Transferred **same day** as the income payment | PwC |

### 5.12 Penalties

**5.12 Penalties**  _(Grant Thornton/Caspian Legal Center)_

| Item | Rate / amount | Source |
| --- | --- | --- |
| Late-payment interest | 0.1% per day on the unpaid tax (statutory cap on accrual period — **[RESEARCH GAP — reviewer to confirm cap, commonly cited as one year]**) | Grant Thornton |
| Understatement / underreporting (Article 58 financial sanction) | 50% of the understated/underreported tax | Caspian Legal Center |
| Transfer-pricing reporting violation | AZN 6,000 (increased from AZN 2,000 in 2025) | Caspian Legal Center |
| Business facility registration / signage failure | AZN 40 (micro-business/non-profit); AZN 400 (other taxpayers) | Caspian Legal Center |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Micro-Entrepreneur 75% Income Exemption

- **Micro-entrepreneur 75% exemption** — **Source:** Caspian Legal Center (2025 Tax Code) - Self-employed individuals in listed services (software, design, translation, advertising, research, education, legal/audit/accounting, journalism, courier, tourist guidance, service exports) with **annual income up to AZN 45,000** get **75% of income exempt**, provided such activity is at least **50% of total annual income**. - **Conservative default:** do not apply the exemption until eligibility (activity type, the 50% test, and the AZN 45,000 ceiling) is confirmed. - **Flag for reviewer:** confirm activity is on the listed-services schedule and that the 50% and AZN 45,000 conditions are met for the year.  _(Caspian Legal Center (2025 Tax Code))_

### 6.2 Simplified vs General Regime Choice

- **Simplified vs general regime choice** — - Simplified (2% of turnover) requires turnover ≤ AZN 200,000 and no VAT registration; certain activities are excluded. - General regime (20% of net profit) allows expense deductions but adds VAT obligations above AZN 200,000. - **Flag for reviewer:** confirm the entrepreneur's activity is eligible for simplified tax and that the rate (2% vs a possible Baku rate) is correct **[RESEARCH GAP — reviewer to confirm]**.

### 6.3 Home Office Deduction (general-regime entrepreneur)

- **Home office deduction** — - Apportion utilities/rent by the dedicated business-use proportion of the home. - A dual-use room does not qualify. - **Conservative default:** 0% until the arrangement is confirmed.

### 6.4 Motor Vehicle Business Use

- **Motor vehicle business use** — - Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. - Requires a mileage log. - **Conservative default:** 0% business use until a log is provided.

### 6.5 Phone / Internet Mixed Use

- **Phone/internet mixed use** — - Business-use portion only; client must provide a reasonable estimate. - **Conservative default:** 0% until the business percentage is confirmed.

### 6.6 Depreciation of Capital Assets

- **Depreciation of capital assets** — - Capital assets must be depreciated rather than expensed in full. - **The exact Tax Code depreciation rates by asset class are [RESEARCH GAP — reviewer to confirm]** — do not state a rate without confirmation. - **Flag for reviewer:** confirm the applicable depreciation method and rate per the Tax Code.

### 6.7 2025/2026 Regime Boundary

- **2025/2026 regime boundary** — - Wages paid in December 2025 vs January 2026 fall under different regimes (holiday vs progressive). - **Flag for reviewer:** confirm the period of each payment and apply the correct year's schedule.

## Section 7 -- Excel Working Paper Template

```
AZERBAIJAN INCOME TAX -- WORKING PAPER
Tax Year: 2025 / 2026  (CIRCLE ONE -- rates differ)
Client: ___________________________
Type: Employee / Individual Entrepreneur (General) / Individual Entrepreneur (Simplified)
Sector (if employee): Private non-oil / Oil-gas / Public

== PART A: EMPLOYEE PAYROLL (per month) ==
  A1. Gross monthly wage (AZN)                    ___________
  A2. Income tax (apply correct schedule)         ___________
        2025 private non-oil: 0% to 8,000; 14% excess
        2025 oil/gas+public:  14% to 2,500; 350 + 25% excess
        2026 private non-oil: 3% / 10% / 14%
  A3. Employee DSMF                               ___________
  A4. Employee UIC (0.5%)                          ___________
  A5. Employee medical (2% up to 8,000)            ___________
  A6. Net pay (A1 - A2 - A3 - A4 - A5)            ___________

  Employer cost (informational):
  A7. Employer DSMF                               ___________
  A8. Employer UIC (0.5%)                          ___________
  A9. Employer medical (2% up to 8,000)            ___________

== PART B: INDIVIDUAL ENTREPRENEUR -- SIMPLIFIED ==
  B1. Gross turnover (AZN)                         ___________
  B2. Simplified tax (2% of B1)                    ___________
       [Verify Baku rate before applying]

== PART C: INDIVIDUAL ENTREPRENEUR -- GENERAL ==
  C1. Gross business income                        ___________
  C2. Less: allowable expenses                     ___________
  C3. Less: depreciation [confirm rates]           ___________
  C4. Net taxable profit (C1 - C2 - C3)            ___________
  C5. Micro-entrepreneur 75% exemption (if eligible) ________
  C6. Taxable base after exemption                 ___________
  C7. Income tax (20% of C6)                       ___________

== PART D: WITHHOLDING ON OTHER INCOME ==
  D1. Dividends x 5%                               ___________
  D2. Interest x 10%                               ___________
  D3. Rent/royalties x 14%                         ___________

REVIEWER FLAGS:
  [ ] Tax year confirmed (2025 vs 2026)?
  [ ] Sector / regime confirmed?
  [ ] Employer DSMF base figure verified (AZN 44 reconciliation)?
  [ ] Simplified rate confirmed (2% vs Baku 4%)?
  [ ] Self-employed social-insurance % obtained from authority?
  [ ] Micro-entrepreneur 75% exemption eligibility confirmed?
  [ ] Depreciation rates confirmed against Tax Code?
  [ ] Home office / vehicle / phone business % documented?
```

## Section 8 -- Bank Statement Reading Guide

### Azerbaijani Bank Statement Formats

**Azerbaijani Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Kapital Bank | PDF, CSV | Tarix (date), Təsvir (description), Məbləğ (amount), Qalıq (balance) | Most common; description holds counterparty + reference |
| PASHA Bank | PDF, CSV | Date, Description, Debit, Credit, Balance | Corporate-friendly exports |
| ABB (IBA) | PDF | Tarix, Əməliyyat (operation), Məbləğ | AZN and FX accounts |
| Bank Respublika | PDF, CSV | Tarix, Təsvir, Məbləğ |  |
| Unibank / Leobank | CSV | Date, Counterparty, Amount, Currency | Clean digital exports |

### Key Azerbaijani Banking / Tax Terms

**Key Azerbaijani Banking / Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| KÖÇÜRMƏ | Transfer | Check direction for income/expense |
| ÖDƏNİŞ | Payment | Expense — check counterparty |
| DAXİLOLMA | Incoming / receipt | Potential income |
| ƏMƏK HAQQI / MAAŞ | Salary / wage | Employment income (PAYE) |
| QONORAR | Fee / honorarium | Business income |
| İCARƏ / KİRAYƏ | Rent | Rental income / rent expense |
| FAİZ | Interest | Interest income (WHT 10%) |
| DİVİDEND | Dividend | Investment income (WHT 5%) |
| KOMİSSİYA / HAQQI | Commission / charge | Bank charge (deductible) |
| DSMF | Social insurance fund | Statutory contribution |
| ƏDV | VAT | VAT liability movement — exclude |
| CƏRİMƏ | Fine | Not deductible |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items and all **[RESEARCH GAP]** items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- AZERBAIJAN INCOME TAX
1. Tax year being computed: 2025 or 2026? (rates differ materially)
2. Are you an employee, or an individual entrepreneur?
3. If employee: which sector — private non-oil, oil/gas, or government/public?
4. If entrepreneur: general regime (20% of profit) or simplified (2% of turnover)?
5. Annual turnover — is it at or below AZN 200,000?
6. Are you VAT-registered (taxable turnover over AZN 200,000)?
7. Do you qualify for the micro-entrepreneur 75% exemption (listed service,
   annual income up to AZN 45,000, that activity at least 50% of income)?
8. Any other income (rent, interest, dividends, foreign income)?
9. Any capital assets purchased during the year?
10. Confirmation of DSMF / medical / unemployment contributions paid.
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| Income tax of individuals | Tax Code of the Republic of Azerbaijan, Income Tax chapter |
| Exemptions | Tax Code, Article 102 |
| Financial sanctions (understatement) | Tax Code, Article 58 |
| Late-payment interest | Tax Code, Article 59 |
| Social insurance | Law on Social Insurance (DSMF/SSPF) |
| Unemployment insurance | Law on Unemployment Insurance |
| Medical insurance | Law on Medical Insurance |
| Tax authority | State Tax Service under the Ministry of Economy — taxes.gov.az |

### Key Thresholds (all sourced)

**Key Thresholds (all sourced)**

| Threshold | Value | Source |
| --- | --- | --- |
| VAT mandatory registration | AZN 200,000 taxable turnover in any 12 consecutive months (or single transaction over it) | PwC |
| Simplified-regime eligibility (turnover) | Annual turnover ≤ AZN 200,000 and not VAT-registered | Deel |
| Tax holiday income ceiling (private non-oil, 2025) | Monthly wage up to AZN 8,000 at 0% | PwC |
| Micro-entrepreneur 75% exemption ceiling | Annual income up to AZN 45,000 | Caspian Legal Center |
| Minimum monthly wage | AZN 400/month (from 1 Jan 2025) | APA |
| Medical insurance band split | AZN 8,000/month | PwC |

### 2025 vs 2026 — At a Glance

**2025 vs 2026 — At a Glance**

| Item | 2025 | 2026 |
| --- | --- | --- |
| Private non-oil PIT | 0% to 8,000; 14% excess [PwC] | 3% / 10% / 14% [Mercans] |
| Lowest band trajectory | n/a (holiday) | 3% (2026) → 5% (2027) → 7% (2028) [Mercans] |
| Combined DSMF above AZN 8,000 (private non-oil) | 25% | 21% (10% EE + 11% ER) [Mercans] |
| Minimum monthly wage | AZN 400 [APA] | AZN 400 (unchanged) [APA] |

### Test Suite

**Test 1 -- Private non-oil employee, 2025, under ceiling.**
Input: Private non-oil, monthly gross AZN 6,000, 2025.
Expected: Income tax = AZN 0 (0% holiday band, income ≤ 8,000).

**Test 2 -- Private non-oil employee, 2025, above ceiling.**
Input: Private non-oil, monthly gross AZN 10,000, 2025.
Expected: 14% × (10,000 − 8,000) = AZN 280.

**Test 3 -- Oil/gas employee, 2025.**
Input: Oil/gas, monthly gross AZN 4,000, 2025.
Expected: 350 + 25% × (4,000 − 2,500) = 350 + 375 = AZN 725.

**Test 4 -- Private non-oil employee, 2026, progressive.**
Input: Private non-oil, monthly gross AZN 5,000, 2026.
Expected: (3% × 2,500) + (10% × 2,500) = 75 + 250 = AZN 325.

**Test 5 -- Employee DSMF, private non-oil, 2025.**
Input: Monthly gross AZN 6,000.
Expected: 3% × 200 + 10% × 5,800 = 6 + 580 = AZN 586 (employee). Employer = AZN 914 per published formula but the AZN 44 base is FLAGGED for confirmation.

**Test 6 -- UIC combined.**
Input: Monthly gross AZN 3,000.
Expected: employee 0.5% × 3,000 = AZN 15; employer 0.5% × 3,000 = AZN 15; combined AZN 30 (1.0%).

**Test 7 -- Medical insurance, income above band.**
Input: Monthly gross AZN 10,000.
Expected (each of employee and employer): AZN 160 + 0.5% × (10,000 − 8,000) = 160 + 10 = AZN 170.

**Test 8 -- Simplified-regime entrepreneur.**
Input: Gross turnover receipt AZN 12,000, simplified regime.
Expected: 2% × 12,000 = AZN 240 (verify Baku rate before applying).

**Test 9 -- General-regime entrepreneur.**
Input: Net taxable profit AZN 50,000, no micro-entrepreneur exemption.
Expected: 20% × 50,000 = AZN 10,000.

**Test 10 -- Regime boundary.**
Input: Private non-oil wage AZN 7,000, December 2025 vs January 2026.
Expected: Dec 2025 = AZN 0 (holiday); Jan 2026 = (3% × 2,500) + (10% × (7,000 − 2,500)) = 75 + 450 = AZN 525.

## PROHIBITIONS

- NEVER apply a rate schedule without knowing BOTH the tax year (2025 vs 2026) AND the sector/regime
- NEVER apply the 2025 holiday (0% to AZN 8,000) to income earned in 2026 or later
- NEVER assume a self-employed social-insurance percentage — it is activity/region-dependent and flagged as a research gap
- NEVER state a capital-asset depreciation rate without confirming it against the Tax Code
- NEVER apply the AZN 200/month personal exemption to private non-oil employees in 2025 (they were under the holiday, not the exemption)
- NEVER apply the micro-entrepreneur 75% exemption without confirming the listed-service, 50%, and AZN 45,000 conditions
- NEVER treat the simplified 2% rate as final for a Baku-based entrepreneur without verifying the rate split
- NEVER include VAT collected on sales as income
- NEVER allow fines, penalties, or income tax itself as a deduction
- NEVER present tax calculations as definitive — always label as estimated and route through the deterministic engine

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
