---
name: latvia-income-tax
description: Use this skill whenever asked about Latvia personal income tax (iedzīvotāju ienākuma nodoklis, IIN) for employees, self-employed / economic-activity individuals, pensioners, or capital-income recipients. Trigger on phrases like "how much income tax do I pay in Latvia", "Latvia PIT rate", "gada ienākumu deklarācija", "annual income declaration", "non-taxable minimum", "neapliekamais minimums", "VSAOI", "social contributions Latvia", "solidarity tax", "solidaritātes nodoklis", "micro-enterprise tax", "mikrouzņēmuma nodoklis", "MET", "economic activity registration", "capital gains Latvia", "dividend tax Latvia", "self-employed Latvia tax", "EDS", or any question about filing or computing Latvian personal income tax. Also trigger when preparing or reviewing a Latvian annual income declaration (form GID), a capital-gains return (GD/GDz), or a monthly payroll computation, computing the fixed non-taxable minimum and allowances, or advising on VSAOI / solidarity tax interaction. This skill covers the 25.5% / 33% progressive PIT, the +3% high-income surtax, the fixed non-taxable minimum and allowances, VSAOI rates and bases, the solidarity tax, the micro-enterprise tax regime, capital-income tax, penalties, and the interaction with VAT and social insurance. ALWAYS read this skill before touching any Latvian income tax work.
version: 0.1
jurisdiction: LV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia Personal Income Tax

## Latvia Personal Income Tax -- Skill v0.1

> **Tier 2 (research-verified).** Figures are sourced to VID, VSAA, the Ministry of Finance (FM), the Cabinet of Ministers, and Big-4 / Orbitax secondary guides, and are mutually consistent. They have **not** yet been signed off by a Latvian-qualified tax adviser. Items marked **[RESEARCH GAP — reviewer to confirm]** require human confirmation before filing.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Latvia (Republic of Latvia / Latvijas Republika) |
| Tax | Personal Income Tax -- iedzīvotāju ienākuma nodoklis (IIN) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Law "On Personal Income Tax" (Likums "Par iedzīvotāju ienākuma nodokli") |
| Supporting legislation | Law "On State Social Insurance" (VSAOI); Micro-Enterprise Tax Law (Mikrouzņēmumu nodokļa likums); Law "On Taxes and Fees" (administration, interest, penalties) |
| Tax authority | Valsts ieņēmumu dienests (VID / State Revenue Service) |
| Social insurance agency | Valsts sociālās apdrošināšanas aģentūra (VSAA) |
| Policy ministry | Finanšu ministrija (Ministry of Finance / FM) |
| Filing portal | EDS -- Electronic Declaration System (eds.vid.gov.lv) |
| Annual return deadline | 1 March -- 1 June of the following year; 1 April -- 1 July if annual income exceeds EUR 105,300 (PwC) |
| Validated by | Pending — requires sign-off by a Latvian-qualified tax adviser |
| Validation date | Pending |
| Skill version | 0.1 |

### PIT Rate Brackets (2025 -- annual reconciliation)

**PIT Rate Brackets (2025 -- annual reconciliation)**  _(VID, https://www.vid.gov.lv/en/personal-income-tax-rates)_

| Annual income (EUR) | Rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 105,300 | 25.5% | EUR 26,851.50 |
| 105,300 -- 200,000 | 33% | EUR 58,102.50 |
| 200,000+ | 33% + 3% surtax | -- |

- **PIT withholding mechanics** — PIT is progressive at annual reconciliation. Monthly payroll is withheld at the flat 25.5%; the 33% and +3% bands are settled through the annual income declaration.  _(VID, https://www.vid.gov.lv/en/personal-income-tax-rates)_
- **PIT rate up to EUR 105,300** — 25.5% (on annual income up to EUR 105,300)  _(VID, https://www.vid.gov.lv/en/personal-income-tax-rates)_
- **PIT rate above EUR 105,300** — 33% (on the portion of annual income above EUR 105,300)  _(PwC, https://taxsummaries.pwc.com/latvia/individual/taxes-on-personal-income)_
- **High-income surtax** — An additional +3% surtax on the portion of total annual income exceeding EUR 200,000, on top of the 33% rate. PwC notes this first applies via the 2026 tax return (i.e. on 2025 income reconciled in 2026). [RESEARCH GAP — reviewer to confirm] the exact first-application year for payroll vs annual reconciliation.  _(VID)_
- **Cumulative-tax check** — at EUR 105,300 → 105,300 × 25.5% = 26,851.50. At EUR 200,000 → 26,851.50 + (200,000 − 105,300) × 33% = 26,851.50 + 94,700 × 33% = 26,851.50 + 31,251.00 = 58,102.50.
- **No separate personal allowance band** — Latvia has no separate tax-free "personal allowance" band — the fixed non-taxable minimum (below) is deducted from the PIT base instead.

### Non-Taxable Minimum and Allowances (2025)

**Non-Taxable Minimum and Allowances (2025)**  _(FM, https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances)_

| Item | 2025 amount | Source |
| --- | --- | --- |
| Fixed non-taxable minimum (all employees) | EUR 510/month (EUR 6,120/year) | FM, https://www.fm.gov.lv/en/changes-taxation-and-finances-2025 |
| Pensioner non-taxable minimum | EUR 1,000/month (EUR 12,000/year) | FM, https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances |
| Dependant allowance (per dependant) | EUR 250/month (EUR 3,000/year) | FM, non-taxable-minimum-and-tax-allowances |
| Disability allowance -- Group I/II | EUR 154/month (EUR 1,848/year) | FM, non-taxable-minimum-and-tax-allowances |
| Disability allowance -- Group III | EUR 120/month (EUR 1,440/year) | FM, non-taxable-minimum-and-tax-allowances |
| Politically-repressed persons | EUR 154/month | FM, non-taxable-minimum-and-tax-allowances |

- **2025 vs 2026 caution** — The former differentiated (income-dependent) allowance was abolished from 2025; the fixed EUR 510/month applies uniformly for 2025 (FM "Changes from 2025"). The FM allowances page (updated Jan 2026) shows EUR 550/month — that is the 2026 figure (progression: 510 in 2025 → 550 in 2026 → 570 in 2027). Use EUR 510 for the 2025 tax year.  _(FM)_

### Social Insurance (VSAOI) -- 2025

**VSAOI standard**  _(VSAA, https://www.vsaa.gov.lv/en/contributions-0)_

| Class | Rate | Base / ceiling | Source |
| --- | --- | --- | --- |
| Employee VSAOI (standard) | 10.50% | Gross up to EUR 105,300/year | VSAA, https://www.vsaa.gov.lv/en/contributions-0 |
| Employer VSAOI (standard) | 23.59% | Gross up to EUR 105,300/year | VSAA, contributions-0 |
| **Total VSAOI (standard)** | **34.09%** | Gross up to EUR 105,300/year | VSAA, contributions-0 |

- **Total check (standard)** — 10.50% + 23.59% = 34.09% ✓

**VSAOI pension-age reduced**  _(PwC, .../individual/other-taxes)_

| Class | Rate | Base / ceiling | Source |
| --- | --- | --- | --- |
| Employee VSAOI (pension-age reduced) | 9.25% | Up to EUR 105,300/year | PwC, .../individual/other-taxes |
| Employer VSAOI (pension-age reduced) | 20.77% | Up to EUR 105,300/year | PwC, other-taxes |
| **Total VSAOI (pension-age reduced)** | **30.02%** | Up to EUR 105,300/year | PwC, other-taxes |

- **Total check (reduced)** — 9.25% + 20.77% = 30.02% ✓

### Capital Income (2025)

**Capital Income (2025)**  _(PwC, taxes-on-personal-income)_

| Income type | Rate | Note | Source |
| --- | --- | --- | --- |
| Dividends | 25.5% | Exempt from PIT if already subject to Latvian CIT | PwC, taxes-on-personal-income |
| Interest | 25.5% | Flat | PwC |
| Capital gains | 25.5% | Flat (increased from 20% in 2024) | PwC |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- do not compute without confirming Latvian tax residency |
| Unknown marital/dependant status | No dependant allowance applied (EUR 0) |
| Unknown whether wage-tax book lodged with employer | Non-taxable minimum NOT auto-applied at payroll |
| Unknown income level vs cap | Assume below EUR 105,300 (25.5% only); flag if approaching cap |
| Unknown self-employed monthly income vs EUR 700 | Treat as below EUR 700 (10% pension contribution on actual income) |
| Unknown whether dividend was CIT-charged | Treat dividend as taxable at 25.5% |
| Unknown capital-gains quarterly total | Assume > EUR 1,000 (quarterly filing) and flag |
| Unknown VAT-registration / turnover | Assume below EUR 50,000; flag if approaching |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — bank statement for the full tax year (CSV, PDF, or pasted text), plus confirmation of Latvian tax residency, source of income (employment / economic activity / capital / pension), and whether a wage-tax book (algas nodokļa grāmatiņa) is lodged with the employer.

Recommended -- payslips / employer VSAOI records, economic-activity income & expense records, capital transaction records (purchase cost and disposal proceeds), prior-year annual declaration (GID), dependant / disability / pensioner status.

Ideal -- complete income and expenditure account, asset register, VSAOI payment confirmations, EDS pre-filled data export, and confirmation of any solidarity-tax exposure.

- **Refusal if minimum missing** — Refusal if minimum is missing -- SOFT WARN. No bank statement at all = hard stop. Bank statement without supporting documents = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify residency, that economic-activity expenses are supported, that the non-taxable minimum / allowances are correctly applied, and that the correct progressive band has been used at annual reconciliation."

### Refusal Catalogue

- **R-LV-1 -- Residency unknown** — "Latvian PIT depends on tax residency. This skill cannot compute tax without confirming whether the individual is a Latvian tax resident, a non-resident, or dual-resident. Please confirm before proceeding."
- **R-LV-2 -- Companies / partnerships** — "This skill covers individuals (employees, self-employed / economic-activity persons, capital-income recipients). Companies pay corporate income tax (UIN); partnerships and group structures file separately. Escalate to a Latvian-qualified adviser."
- **R-LV-3 -- Non-resident / cross-border income** — "Non-resident taxation, double-tax-treaty relief, and posted-worker rules have different rules. Out of scope. Escalate to a Latvian-qualified adviser."
- **R-LV-4 -- Complex capital / property disposals** — "Real-estate disposals, inherited assets, and structured capital transactions require specialised analysis (including the 25.5% capital-gains rate and quarterly reporting interaction). Escalate to a Latvian-qualified adviser."
- **R-LV-5 -- Solidarity-tax / high-income reconciliation** — "Income above the EUR 105,300 social-insurance cap triggers solidarity tax (effective 25%, recalculated with refund the following year) and may cross the 33% / +3% PIT bands. This needs reviewer judgement. Escalate before advising."
- **R-LV-6 -- Arrears / enforcement** — "Client has outstanding tax arrears or is subject to VID enforcement. Late-payment interest (0.05%/day, capped at 40% of principal) and understatement penalties (20%/30%) apply. Do not advise. Escalate immediately."
- **R-LV-7 -- VAT return requested** — "This skill covers personal income tax only. For Latvian VAT, use the latvia-vat-return skill. For payroll mechanics, use latvia-payroll; for VSAOI detail, latvia-social-contributions."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the statement. Latvian statements frequently use Latvian-language terms (shown in the patterns). If multiple patterns match, use the most specific.

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Classification | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + PĀRSKAITĪJUMS, MAKSĀJUMS, RĒĶINS, INVOICE | Economic-activity income | Business/self-employment income | If VAT-registered, extract net (excl. 21% VAT) |
| HONORĀRS, PAKALPOJUMI, KONSULTĀCIJAS, FEES | Economic-activity income | Professional fees | Typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Economic-activity income | Platform payout | Match to underlying invoices |
| PAYPAL PAYOUT, WISE PAYOUT, REVOLUT PAYOUT | Economic-activity income | Platform payout | Verify business vs personal account |
| UPWORK, FIVERR, TOPTAL | Economic-activity income | Freelance platform | Net of platform commission |
| ALGA, DARBA SAMAKSA, SALARY, EMPLOYER [name] | Employment income | Employment income (payroll) | PIT 25.5% + VSAOI 10.50% normally already withheld |
| PENSIJA, PENSION, VSAA PENSIJA | Pension income | Pension | Pensioner non-taxable minimum may apply |
| ĪRE, RENT RECEIVED | Rental income | Other income | Report on annual declaration |
| PROCENTI, INTERESSI, INTEREST | Capital income | Interest -- 25.5% | Capital income |
| DIVIDENDE, DIVIDEND | Capital income | Dividend -- 25.5% (exempt if Latvian CIT paid) | Confirm CIT status |
| VID ATMAKSA, TAX REFUND, NODOKĻU ATMAKSA | EXCLUDE | Not income | Prior-year refund |
| PABALSTS, GRANT, VALSTS ATBALSTS | Check nature | Capital grants EXCLUDE; revenue grants = income | Confirm grant type |

### 3.2 Expense Patterns (Debits) -- Economic-Activity, Fully Deductible

- **Deduction scope note** — Deductions apply only to economic-activity (self-employed) income computed on the general regime. Employees cannot deduct work expenses against employment income. Micro-enterprise tax payers cannot deduct expenses (the 25% MET is on turnover).

**3.2 Expense Patterns (Debits) -- Economic-Activity, Fully Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BIROJA ĪRE, OFFICE RENT, KIRI | Office rent | Deductible | Dedicated business premises |
| PROFESIONĀLĀ APDROŠINĀŠANA, PI INSURANCE | Professional insurance | Deductible |  |
| GRĀMATVEDIS, AUDITORS, BOOKKEEP, ACCOUNTANT | Accountancy fees | Deductible |  |
| JURISTS, ADVOKĀTS, LAWYER, LEGAL (business) | Legal fees | Deductible | Must be business-related |
| KANCELEJAS PRECES, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MĀRKETINGS, GOOGLE ADS, META ADS, REKLĀMA | Marketing/advertising | Deductible |  |
| APMĀCĪBA, KURSI, TRAINING, SEMINAR | Training/CPD | Deductible | Must relate to current activity |
| BANKAS KOMISIJA, BANK FEE, SWEDBANK CHARGE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, KOMISIJA | Payment processing fees | Deductible |  |
| DOMĒNS, HOSTING, AWS, CLOUDFLARE | IT infrastructure | Deductible | Capital if substantial -- see 3.7 |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**3.3 Expense Patterns (Debits) -- SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| PERPETUAL LICENCE (substantial) | Capital item | Capitalise / depreciate | Confirm useful life **[RESEARCH GAP — reviewer to confirm depreciation rate]** |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| LATVENERGO, ELEKTRUM, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| ŪDENS, GĀZE, WATER, GAS | Water/gas | T2 if home office | Apportion |
| TET, BITE, LMT, TELE2, BROADBAND | Telecoms/broadband | T2 | Business portion only; default 0% if mixed |
| MOBILAIS, MOBILE | Phone | T2 | Business portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIRBALTIC, RYANAIR, WIZZ AIR, FLIGHT | Flights | Deductible if business travel | Must be wholly business |
| HOTEL, VIESNĪCA, BOOKING.COM | Accommodation | Deductible if business travel |  |
| BOLT, UBER, TAKSOMETRS, TAXI | Local transport | Deductible if business purpose |  |
| DEGVIELA, FUEL, CIRCLE K, NESTE | Vehicle fuel | T2 -- business % only | Requires mileage log |
| STĀVVIETA, PARKING | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTORĀNS, RESTAURANT, PUSDIENAS, ENTERTAINMENT | Entertainment / personal meals | NOT deductible | Personal living cost |
| PĀRTIKA, RIMI, MAXIMA, LIDL, GROCERIES | Personal expenses | NOT deductible | Private living costs |
| SODS, FINE, PENALTY, NOKAVĒJUMA NAUDA | Fines/penalties | NOT deductible | Public policy |
| IIN, INCOME TAX, NODOKĻU MAKSĀJUMS | Tax payments | NOT deductible | PIT cannot reduce income |
| PERSONĪGAIS, DRAWINGS, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items

**3.7 Expense Patterns (Debits) -- Capital Items**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KLĒPJDATORS, LAPTOP, MACBOOK, DATORS | Computer hardware | Capitalise / depreciate | **[RESEARCH GAP — reviewer to confirm depreciation rate for economic-activity assets]** |
| PRINTERIS, SCANNER, OFFICE EQUIPMENT | Office equipment | Capitalise / depreciate | As above |
| MĒBELES, FURNITURE, GALDS, KRĒSLS | Furniture/fittings | Capitalise / depreciate | As above |
| AUTO, CAR, TRANSPORTLĪDZEKLIS (business) | Motor vehicle | Capitalise; business % only | As above |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IEKŠĒJAIS PĀRSKAITĪJUMS, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| AIZDEVUMA ATMAKSA, LOAN REPAYMENT (principal) | EXCLUDE | Loan principal movement |
| VSAOI, SOCIĀLĀS IEMAKSAS, SOCIAL CONTRIBUTIONS | Social-insurance payment | Not a PIT deduction line; tracked separately |
| PVN, VAT PAYMENT, VID PVN | EXCLUDE | VAT liability payment, not expense |
| AVANSA NODOKLIS, ADVANCE/PROVISIONAL TAX | Credit against PIT liability | Not an expense |

### 3.9 Latvian Banks -- Statement Format Reference

**3.9 Latvian Banks -- Statement Format Reference**

| Bank | Common patterns | Notes |
| --- | --- | --- |
| Swedbank | PĀRSKAITĪJUMS, KARTE, KOMISIJA, MAKSĀJUMS | PDF/CSV; date format DD.MM.YYYY |
| SEB banka | PĀRSKAITĪJUMS, TIEŠAIS DEBETS, KARTES MAKSĀJUMS | PDF/CSV |
| Citadele | MAKSĀJUMS, KOMISIJA, KARTE | PDF; CSV export available |
| Luminor | TRANSFER, CARD, FEE | PDF/CSV |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency -- use EUR amounts |

## Section 4 -- Worked Examples

All examples use the 2025 figures: PIT 25.5%, fixed non-taxable minimum EUR 510/month, employee VSAOI 10.50% (employee mandatory social contributions reduce the PIT base under the PIT-law withholding method — confirm with reviewer for edge cases).

### Example 1 -- Monthly Payroll (employee, wage-tax book lodged)

**Input line:**
`15.01.2025 ; SWEDBANK PĀRSKAITĪJUMS ; SIA OZOLS ; ALGA JANVĀRIS ; +1,463.60 ; EUR`

**Scenario:** Gross salary EUR 2,000/month, single, no dependants, wage-tax book lodged so the EUR 510/month non-taxable minimum is applied at source.

**Reasoning:**
- Employee VSAOI: 2,000 × 10.50% = **EUR 210.00**
- Non-taxable minimum: **EUR 510.00**
- PIT base: 2,000 − 210 − 510 = **EUR 1,280.00**
- PIT at 25.5%: 1,280 × 0.255 = **EUR 326.40**
- Net pay: 2,000 − 210 − 326.40 = **EUR 1,463.60**
- Employer VSAOI: 2,000 × 23.59% = **EUR 471.80**; total employer cost = 2,000 + 471.80 = **EUR 2,471.80**

**Classification:** Net employment credit EUR 1,463.60 (Section 3.1 ALGA). The 33%/+3% bands are NOT applied at payroll — only at annual reconciliation.

### Example 2 -- Self-Employed Fee Received (general regime)

**Input line:**
`12.03.2025 ; SEB PĀRSKAITĪJUMS ; SIA BĒRZS ; RĒĶINS NR.2025-014 ; +5,000.00 ; EUR`

**Reasoning:** Payment for services under registered economic activity. If not VAT-registered, full EUR 5,000 is economic-activity income. If VAT-registered (21%), extract the net. Net economic-activity profit (income − allowable expenses) is taxed at 25.5%; VSAOI is payable separately (see Example 3).

**Classification:** Economic-activity income EUR 5,000 (net of VAT if registered).

### Example 3 -- Self-Employed VSAOI Payment

**Input line:**
`05.04.2025 ; SWEDBANK MAKSĀJUMS ; VALSTS KASE VSAOI ; PAŠNODARBINĀTAIS Q1 ; -652.47 ; EUR`

**Reasoning:** Self-employed VSAOI is 31.07% (29.36% if pension-age) on a freely-chosen object at/above the minimum base where monthly income is EUR 700 or more (VID). This is a social-insurance payment, tracked separately — it is not a Section 3.2 expense line. Example: object EUR 700/month × 3 months = 2,100 × 31.07% = **EUR 652.47**.

**Classification:** VSAOI payment (Section 3.8). Not a PIT deduction line.

### Example 4 -- Dividend Already Subject to CIT

**Input line:**
`20.05.2025 ; CITADELE ; SIA PRIEDE ; DIVIDENDE 2024 ; +5,000.00 ; EUR`

**Reasoning:** Dividend from a Latvian company that has already paid corporate income tax (CIT/UIN) on the underlying profit is **exempt** from PIT (PwC). If the distribution had NOT borne Latvian CIT, the 25.5% capital-income rate would apply.

**Classification:** Capital income EUR 5,000 — **PIT EUR 0.00** (CIT already paid). Confirm CIT status with reviewer.

### Example 5 -- Capital Gain on Share Sale (quarterly threshold)

**Input line:**
`18.06.2025 ; SEB ; BROKER PĀRDOŠANA ; AKCIJAS ; +8,000.00 ; EUR`

**Reasoning:** Shares acquired for EUR 5,000, sold for EUR 8,000. Capital gain = 8,000 − 5,000 = **EUR 3,000**. Capital-gains PIT at 25.5% = 3,000 × 0.255 = **EUR 765.00**. Because the quarterly gain exceeds EUR 1,000, a capital-gains return (GD/GDz) must be filed **quarterly**, by the 15th of the month following the quarter (PwC).

**Classification:** Capital gain EUR 3,000; PIT EUR 765.00; quarterly capital-gains return required.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`30.05.2025 ; SWEDBANK PĀRSKAITĪJUMS ; PAŠA KONTS - KRĀJUMI ; ; -2,000.00 ; EUR`

**Reasoning:** Transfer between the taxpayer's own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Progressive PIT at Annual Reconciliation

- **Progressive PIT at Annual Reconciliation** — Legislation: Law "On Personal Income Tax". For 2025: 25.5% on annual income up to EUR 105,300; 33% on the portion above EUR 105,300; an additional 3% surtax on the portion above EUR 200,000 (VID, https://www.vid.gov.lv/en/personal-income-tax-rates). Monthly payroll PIT is withheld at the flat 25.5%; the 33% and +3% are settled through the annual income declaration. The +3% surtax: VID lists it as a 2025 rate, PwC notes first application via 2026 returns — [RESEARCH GAP — reviewer to confirm].  _(VID, https://www.vid.gov.lv/en/personal-income-tax-rates)_

### 5.2 Non-Taxable Minimum and Allowances

- **Non-Taxable Minimum and Allowances** — The fixed non-taxable minimum for 2025 is EUR 510/month (EUR 6,120/year), applied uniformly to all employees (FM, https://www.fm.gov.lv/en/changes-taxation-and-finances-2025). It is applied at payroll only if a wage-tax book (algas nodokļa grāmatiņa) is lodged with the employer. Pensioners: EUR 1,000/month. Dependant allowance: EUR 250/month per dependant. Disability: Group I/II EUR 154/month; Group III EUR 120/month; politically-repressed EUR 154/month (FM, https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances).  _(FM, https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances)_

### 5.3 PIT Base Computation (employment)

- **PIT base and PIT calc** — PIT base = gross salary − employee mandatory social contributions (VSAOI) − applicable non-taxable minimum − allowances. PIT (payroll) = PIT base × 25.5%.

> The deductibility of employee VSAOI from the PIT base follows the standard Latvian withholding method (consistent with VID payroll guidance and Baltic practice). Confirm the precise interaction with reviewer for non-standard cases.

### 5.4 Capital Income

- **Capital Income** — Dividends, interest, and capital gains are taxed at a flat 25.5% for 2025 (increased from 20% in 2024). Dividends already subject to Latvian CIT are exempt from PIT (PwC, https://taxsummaries.pwc.com/latvia/individual/taxes-on-personal-income).  _(PwC, https://taxsummaries.pwc.com/latvia/individual/taxes-on-personal-income)_

### 5.5 Mandatory Social Insurance (VSAOI)

**Mandatory Social Insurance (VSAOI)**  _(VSAA, https://www.vsaa.gov.lv/en/contributions-0)_

| Payer | Standard rate | Pension-age reduced |
| --- | --- | --- |
| Employee | 10.50% | 9.25% |
| Employer | 23.59% | 20.77% |
| **Total** | **34.09%** | **30.02%** |

- **Base and healthcare earmark** — On gross income up to the maximum base of EUR 105,300/year. The employee 10.50% includes 1 percentage point earmarked for healthcare (VSAA, https://www.vsaa.gov.lv/en/contributions-0; PwC for the reduced rate). Totals check: 10.50 + 23.59 = 34.09; 9.25 + 20.77 = 30.02.  _(VSAA, https://www.vsaa.gov.lv/en/contributions-0)_

### 5.6 Self-Employed VSAOI

- **Self-Employed VSAOI** — 31.07% (29.36% if pension-age) on a freely-chosen object at/above the minimum base where monthly income is EUR 700 or more. Where monthly income is below EUR 700, a 10% contribution to state pension insurance is payable on the actual income (VID, https://www.vid.gov.lv/en/self-employed-persons-individual-entrepreneurs). The interaction between the freely-chosen object, the EUR 740 minimum object, and the 10% low-income contribution is nuanced — [RESEARCH GAP — reviewer to confirm against current VSAA self-employed guidance].  _(VID, https://www.vid.gov.lv/en/self-employed-persons-individual-entrepreneurs)_

### 5.7 Solidarity Tax

- **Solidarity Tax** — Applies to income above the EUR 105,300 social-insurance cap. Charged at 34.09% during the year and recalculated to an effective 25%, with the over-collected amount above 25% refunded to the employer by 1 September of the following year (Grant Thornton, https://www.grantthornton.lv/en/insights/key-tax-rates-in-latvia-2025/). It replaces uncapped social contributions for high earners.  _(Grant Thornton, https://www.grantthornton.lv/en/insights/key-tax-rates-in-latvia-2025/)_

### 5.8 Minimum Wage and Minimum Contributions

- **Minimum Wage and Minimum Contributions** — Minimum monthly wage is EUR 740 from 1 January 2025 (was EUR 700 in 2024) (Cabinet of Ministers, https://www.mk.gov.lv/en/article/national-minimum-wage-amount-740-euros-next-year). The minimum social-insurance object = minimum wage; minimum quarterly base = 3 × minimum wage = EUR 2,220 for 2025 (VSAA). If an employee's wage is below the minimum, the employer must top up contributions to the minimum base.  _(Cabinet of Ministers, https://www.mk.gov.lv/en/article/national-minimum-wage-amount-740-euros-next-year)_

### 5.9 Micro-Enterprise Tax (MET)

- **Micro-Enterprise Tax (MET)** — A single combined payment (covering VSAOI + the owner's PIT) at 25% of turnover (VID, https://www.vid.gov.lv/en/microenterprise-tax). Available only where turnover stays within the VAT-registration threshold (EUR 50,000); minimum MET is EUR 50 if no/low turnover. An older tiered 25%/40% structure (40% above EUR 25,000 turnover) appeared in pre-2024 rules — [RESEARCH GAP — reviewer to confirm no turnover-tier rate applies for 2025 against the current Micro-Enterprise Tax Law text].  _(VID, https://www.vid.gov.lv/en/microenterprise-tax)_

### 5.10 Registration Thresholds

**5.10 Registration Thresholds**

| Threshold | Amount | Source |
| --- | --- | --- |
| Economic-activity registration with VID | EUR 3,000/year | VID, self-employed-persons-individual-entrepreneurs |
| Mandatory VAT registration | EUR 50,000 taxable supplies / 12 months | VID, self-employed-persons-individual-entrepreneurs |
| Social-insurance maximum base | EUR 105,300/year | FM, changes-taxation-and-finances-2025 |
| High-income surtax threshold | EUR 200,000/year | VID, personal-income-tax-rates |
| Capital-gains quarterly reporting | EUR 1,000/quarter | PwC, tax-administration |

### 5.11 Filing Deadlines and Penalties

**5.11 Filing Deadlines and Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| Annual declaration (GID) | 1 March -- 1 June following year; 1 April -- 1 July if income > EUR 105,300 | PwC, tax-administration |
| Refund-only claims | Within 3 years | PwC |
| Capital-gains return (GD/GDz) | Quarterly by 15th of following month if quarterly gains > EUR 1,000; else annually by 15 January | PwC |
| Self-employed reports | Annual by 17 January; quarterly by the 17th | VID, self-employed |
| Late-payment interest | 0.05%/day, capped when it reaches 40% of principal overdue | Orbitax |
| Understatement penalty | 20% if understatement ≤ 15% of correct liability; 30% if > 15% | Orbitax |
| Self-employed minimum payment | EUR 50 minimum if economic-activity income below minimum wage / zero | PwC, tax-administration |

> From 1 January 2026 late-payment interest is calculated twice monthly (on the 1st and 15th) rather than daily — the 0.05%/day rule stated is the 2025 basis (Orbitax).

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (economic activity)

- **Home Office (economic activity)** — Apportion rent, electricity, water, internet, maintenance by the business-use proportion of the home. Must be a genuinely dedicated workspace. Conservative default: 0% deduction until reviewer confirms arrangement.

### 6.2 Motor Vehicle Business Use

- **Motor Vehicle Business Use** — Only the documented business-use percentage of fuel, insurance, and maintenance is deductible against economic-activity income. Mileage log required. Conservative default: 0% business use until mileage log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone / Internet Mixed Use** — Business-use portion only. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Capital Asset Depreciation (economic activity)

- **Capital Asset Depreciation (economic activity)** — Business assets are capitalised and depreciated for economic-activity income rather than expensed in full. [RESEARCH GAP — reviewer to confirm the applicable depreciation rates / method for individual economic-activity assets under the current PIT law.] Flag for reviewer: confirm rate, useful life, and start year.

### 6.5 Dividend CIT Status

- **Dividend CIT Status** — A dividend is PIT-exempt only if the underlying profit bore Latvian CIT. Flag for reviewer to confirm CIT status, especially for foreign-source dividends.

### 6.6 Solidarity-Tax Reconciliation (high earners)

- **Solidarity-Tax Reconciliation (high earners)** — Income above EUR 105,300 triggers solidarity tax (effective 25%); the over-collection is refunded the following year. Combined with the 33% / +3% PIT bands, this needs end-to-end reconciliation. Flag for reviewer.

### 6.7 Regime Choice (general vs micro-enterprise)

- **Regime Choice (general vs micro-enterprise)** — General regime: 25.5% PIT on net profit + 31.07% VSAOI. MET: flat 25% of turnover, no expense deductions, capped at EUR 50,000 turnover. Flag for reviewer to confirm the more favourable / eligible regime.

## Section 7 -- Excel Working Paper Template

```
LATVIA PERSONAL INCOME TAX -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Latvian resident / Non-resident
Status: Employee / Self-employed (general) / Micro-enterprise / Pensioner
Wage-tax book lodged with employer? Yes / No
Dependants: ____   Disability group: ____   Pensioner: Yes / No

A. EMPLOYMENT INCOME (annual)
  A1. Gross salary                               ___________
  A2. Less: employee VSAOI (10.50% / 9.25%)      ___________
  A3. Less: non-taxable minimum (510/mo if book) ___________
  A4. Less: dependant allowance (250/mo each)    ___________
  A5. Less: disability/pensioner allowance       ___________
  A6. PIT base (A1 - A2 - A3 - A4 - A5)          ___________

B. ECONOMIC-ACTIVITY INCOME (general regime)
  B1. Gross economic-activity income (net of VAT)___________
  B2. Less: allowable expenses                   ___________
  B3. Less: capital allowances [reviewer rate]   ___________
  B4. Net economic-activity profit               ___________

C. CAPITAL INCOME
  C1. Interest (25.5%)                           ___________
  C2. Dividends taxable (25.5%; 0 if CIT-paid)   ___________
  C3. Capital gains (25.5%)                      ___________

D. PIT COMPUTATION (annual reconciliation)
  D1. Total annual income (A6 + B4 + C totals)   ___________
  D2. Portion <= 105,300 @ 25.5%                 ___________
  D3. Portion 105,300-200,000 @ 33%              ___________
  D4. Portion > 200,000 @ 33% + 3% surtax        ___________
  D5. Total PIT (D2 + D3 + D4)                   ___________
  D6. Less: PIT already withheld at payroll      ___________
  D7. PIT due / refund (D5 - D6)                 ___________

E. SOCIAL INSURANCE (informational)
  E1. Employee VSAOI                             ___________
  E2. Employer VSAOI / self-employed VSAOI       ___________
  E3. Solidarity tax exposure (>105,300)?        ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Wage-tax book / non-taxable minimum correct?
  [ ] Dependant / disability / pensioner allowances confirmed?
  [ ] Correct progressive band(s) applied at reconciliation?
  [ ] +3% surtax first-application year confirmed?
  [ ] Dividend CIT status confirmed?
  [ ] Capital-gains quarterly vs annual filing confirmed?
  [ ] Self-employed VSAOI object / 10% low-income rule confirmed?
  [ ] Solidarity tax reconciled (if income > 105,300)?
  [ ] Capital-asset depreciation rates confirmed?
  [ ] Regime choice (general vs MET) confirmed?
```

## Section 8 -- Bank Statement Reading Guide

### Latvian Bank Statement Formats

**Latvian Bank Statement Formats**

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| Swedbank | PDF, CSV | Datums, Apraksts, Debets, Kredīts, Atlikums | Most common; date DD.MM.YYYY |
| SEB banka | PDF, CSV | Datums, Detaļas, Summa, Atlikums | Counterparty in details field |
| Citadele | PDF, CSV | Datums, Maksājuma mērķis, Summa | Clear payment-purpose field |
| Luminor | PDF, CSV | Date, Description, Amount, Balance |  |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency |
| Wise Business | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency; convert to EUR |

### Key Latvian Banking and Tax Terms

**Key Latvian Banking and Tax Terms**

| Term | English | Classification hint |
| --- | --- | --- |
| PĀRSKAITĪJUMS | Transfer | Check direction for income/expense |
| MAKSĀJUMS | Payment | Expense -- check counterparty |
| TIEŠAIS DEBETS | Direct debit | Regular expense (utility, subscription) |
| KARTE / KARTES MAKSĀJUMS | Card payment | Expense -- check merchant |
| KOMISIJA | Bank charges / commission | Deductible (economic activity) |
| ALGA / DARBA SAMAKSA | Salary / wages | Employment income |
| HONORĀRS | Fee / honorarium | Economic-activity income |
| PROCENTI | Interest | Capital income (or bank charge) |
| DIVIDENDE | Dividend | Capital income (check CIT status) |
| PENSIJA | Pension | Pension income |
| ĪRE | Rent | Rental income or office-rent expense |
| VSAOI / SOCIĀLĀS IEMAKSAS | Social insurance contributions | Tracked separately |
| PVN | VAT | Exclude (liability payment) |
| NOKAVĒJUMA NAUDA | Late-payment interest | Not deductible |

## Section 9 -- Onboarding Fallback

0. **Classify transactions** — Classify all transactions using the pattern library (Section 3).
0. **Mark Tier 2 items pending** — Mark all Tier 2 items as "PENDING -- reviewer must confirm".
0. **Apply conservative defaults** — Apply conservative defaults (Section 1).
0. **Generate working paper** — Generate the working paper (Section 7) with clear flags.
0. **Present onboarding questions** — Present the following questions to the client.

```
ONBOARDING QUESTIONS -- LATVIA PERSONAL INCOME TAX
1. Are you a Latvian tax resident?
2. What are your income sources: employment, economic activity (self-employed),
   capital income (dividends/interest/gains), pension?
3. Is a wage-tax book (algas nodokļa grāmatiņa) lodged with your employer?
4. How many dependants? Any disability group (I/II/III) or politically-repressed status?
5. Are you a pensioner (state old-age pension)?
6. If self-employed: is your monthly income at/above EUR 700? General regime or
   micro-enterprise tax?
7. Did any annual income exceed EUR 105,300? Exceed EUR 200,000?
8. Capital gains: did quarterly gains exceed EUR 1,000?
9. For dividends received: had the company already paid Latvian CIT?
10. Are you VAT-registered (turnover over EUR 50,000)?
```

### Key Legislation and Authority References

**Key Legislation and Authority References**

| Topic | Reference |
| --- | --- |
| PIT rates and bands | Law "On Personal Income Tax"; VID, https://www.vid.gov.lv/en/personal-income-tax-rates |
| Non-taxable minimum and allowances | FM, https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances |
| 2025 tax changes | FM, https://www.fm.gov.lv/en/changes-taxation-and-finances-2025 |
| Social insurance (VSAOI) | Law "On State Social Insurance"; VSAA, https://www.vsaa.gov.lv/en/contributions-0 |
| Self-employed / economic activity | VID, https://www.vid.gov.lv/en/self-employed-persons-individual-entrepreneurs |
| Micro-enterprise tax | Micro-Enterprise Tax Law; VID, https://www.vid.gov.lv/en/microenterprise-tax |
| Minimum wage | Cabinet of Ministers, https://www.mk.gov.lv/en/article/national-minimum-wage-amount-740-euros-next-year |
| Interest and penalties | Law "On Taxes and Fees"; Orbitax country chapter |
| Tax administration / deadlines | PwC, https://taxsummaries.pwc.com/latvia/individual/tax-administration |

### Authoritative Sources

**Authoritative Sources**

| Title | Publisher | URL |
| --- | --- | --- |
| Personal Income Tax rates | VID (State Revenue Service) | https://www.vid.gov.lv/en/personal-income-tax-rates |
| On contributions (VSAOI) | VSAA | https://www.vsaa.gov.lv/en/contributions-0 |
| Self-employed persons | VID | https://www.vid.gov.lv/en/self-employed-persons-individual-entrepreneurs |
| Microenterprise Tax | VID | https://www.vid.gov.lv/en/microenterprise-tax |
| Changes in taxation 2025 | Ministry of Finance | https://www.fm.gov.lv/en/changes-taxation-and-finances-2025 |
| Non-taxable minimum and allowances | Ministry of Finance | https://www.fm.gov.lv/en/non-taxable-minimum-and-tax-allowances |
| National minimum wage 740 euros | Cabinet of Ministers | https://www.mk.gov.lv/en/article/national-minimum-wage-amount-740-euros-next-year |
| Taxes on personal income | PwC | https://taxsummaries.pwc.com/latvia/individual/taxes-on-personal-income |
| Other taxes | PwC | https://taxsummaries.pwc.com/latvia/individual/other-taxes |
| Tax administration | PwC | https://taxsummaries.pwc.com/latvia/individual/tax-administration |
| Key Tax changes 2025 | Grant Thornton Latvia | https://www.grantthornton.lv/en/insights/key-tax-rates-in-latvia-2025/ |
| Interest and Penalties | Orbitax | https://orbitax.com/taxhub/countrychapters/LV/Latvia/e5f4c7d16b644b02bdb68eb4bbc3ab94/Interest-and-Penalties-580 |

### Test Suite

Input: Employment income EUR 30,000/year, single, no dependants, wage-tax book lodged.
Expected: Annual EE VSAOI 30,000 × 10.50% = EUR 3,150.00; non-taxable minimum 510 × 12 = EUR 6,120.00; PIT base = 30,000 − 3,150 − 6,120 = EUR 20,730.00; PIT 25.5% = 20,730 × 0.255 = **EUR 5,286.15**.

Input: Taxable income (post-allowance) EUR 150,000.
Expected: 105,300 × 25.5% = 26,851.50; (150,000 − 105,300) × 33% = 44,700 × 33% = 14,751.00; total PIT = **EUR 41,602.50**.

Input: Total annual income EUR 250,000.
Expected: 105,300 × 25.5% = 26,851.50; (250,000 − 105,300) × 33% = 144,700 × 33% = 47,751.00; +3% surtax on (250,000 − 200,000) = 50,000 × 3% = 1,500.00; total = **EUR 76,102.50**. (Confirm +3% first-application year — see RESEARCH GAP in 5.1.)

Input: Self-employed, monthly income EUR 500.
Expected: 10% pension contribution on actual income = 500 × 10% = **EUR 50.00/month**; plus 25.5% PIT on net economic-activity profit. (Not the full 31.07% VSAOI.)

Input: Quarterly capital gain EUR 1,500 (proceeds 8,000, cost 6,500).
Expected: Gain 1,500; PIT 25.5% = 1,500 × 0.255 = **EUR 382.50**; quarterly capital-gains return required (gain > EUR 1,000).

Input: EUR 5,000 dividend from a Latvian company that paid CIT.
Expected: **PIT EUR 0.00** (exempt). If no Latvian CIT had been paid: 5,000 × 25.5% = EUR 1,275.00.

Input: Gross salary EUR 1,500/month, employee at state old-age-pension age.
Expected: EE VSAOI 1,500 × 9.25% = EUR 138.75; ER VSAOI 1,500 × 20.77% = EUR 311.55; total 1,500 × 30.02% = **EUR 450.30**.

Input: Annual income EUR 130,000 (above the EUR 105,300 social-insurance cap).
Expected: Income above EUR 105,300 = EUR 24,700 subject to solidarity tax; charged at 34.09% during the year and recalculated to an effective 25%, with the over-collection refunded to the employer by 1 September of the following year. Escalate (R-LV-5).

## PROHIBITIONS

- NEVER compute Latvian PIT without confirming tax residency
- NEVER apply the 33% or +3% bands at monthly payroll -- payroll is flat 25.5%, the higher bands settle at annual reconciliation
- NEVER use EUR 550 as the 2025 non-taxable minimum -- that is the 2026 figure; 2025 is EUR 510/month
- NEVER auto-apply the non-taxable minimum at payroll unless a wage-tax book is lodged
- NEVER tax a Latvian-CIT-bearing dividend at 25.5% -- it is PIT-exempt
- NEVER deduct employee work expenses against employment income -- deductions apply to economic-activity income only
- NEVER treat the micro-enterprise 25% as allowing expense deductions -- it is on turnover
- NEVER ignore the EUR 105,300 social-insurance cap or the solidarity-tax interaction for high earners
- NEVER state a numeric rate/threshold/deadline without an inline citation or a [RESEARCH GAP] marker
- NEVER present tax calculations as definitive -- always label as estimated, Tier-2, pending professional sign-off

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
