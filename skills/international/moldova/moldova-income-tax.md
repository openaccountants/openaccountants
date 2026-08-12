---
name: moldova-income-tax
description: Use this skill whenever asked about Moldova (Republic of Moldova) personal income tax for self-employed individuals and individuals. Trigger on phrases like "how much tax do I pay in Moldova", "impozit pe venit", "CET18", "Declaratia persoanei fizice", "flat 12% tax", "income tax return Moldova", "deductible expenses", "personal exemption / scutire personala", "CAS / BASS social insurance", "CNAM / CAM health insurance", "fixed annual contribution", "self-employed tax Moldova", "freelancer tax Moldova", "IT Park 7%", "independent retail 1%", or any question about filing or computing personal income tax for a resident individual or sole proprietor in Moldova. Also trigger when preparing or reviewing a CET18 return, computing the monthly payroll PIT base, or advising on social (CAS) and health (CNAM) contributions. This skill covers the flat 12% PIT, reduced 7% farming rate, final withholding rates (dividends, royalties, winnings), personal/dependent exemptions, employer/employee CAS and CNAM, fixed annual contributions for the self-employed, the CET18 return, penalties, and interaction with VAT and the IT Park regime. ALWAYS read this skill before touching any Moldova income tax work.
version: 0.1
jurisdiction: MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova (Republic of Moldova) Income Tax -- Self-Employed and Individuals

## Moldova (Republic of Moldova) Income Tax -- Self-Employed and Individuals Skill v0.1

> **Tier 2 (research-verified).** Figures below were assembled from PwC Worldwide Tax Summaries, the Moldovan State Social Insurance Budget Law for 2025, and corroborating Moldovan secondary sources. They have NOT yet been signed off by a warranted Moldovan accountant. Treat every output as a draft for professional review. See the caveats in Section 10.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Moldova (Republic of Moldova) |
| Tax | Personal Income Tax (Impozit pe venit) |
| Currency | MDL (Moldovan leu) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Tax Code of the Republic of Moldova (Codul Fiscal, Law No. 1163/1997), Title II -- Income Tax |
| Supporting legislation | Law No. 489/1999 (public social insurance system); Law No. 1593/2002 (mandatory health insurance contributions); Law on the State Social Insurance Budget for 2025; Law on Mandatory Health Insurance Funds for 2025; Law No. 228 of 10 July 2025 (new simplified independent-activity regime, effective 1 Jan 2026 -- NOT 2025) |
| Tax authority | Serviciul Fiscal de Stat (State Tax Service, SFS) -- sfs.md [PwC Moldova] |
| Social-insurance administrator | Casa Națională de Asigurări Sociale (CNAS) -- cnas.gov.md [PwC Moldova] |
| Health-insurance administrator | Compania Națională de Asigurări în Medicină (CNAM) -- cnam.md [PwC Moldova] |
| Filing portal | SFS e-services (sfs.md) |
| Annual return | CET18 -- Declarația persoanei fizice cu privire la impozitul pe venit |
| Filing & payment deadline | 30 April of the year following the reporting year [PwC Moldova Individual -- Tax administration] |
| Validated by | Pending -- requires sign-off by a warranted Moldovan accountant |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rates (2025)

- **Flat tax framing** — Moldova levies a flat personal income tax, not progressive brackets.  _([PwC Moldova Individual -- Taxes on personal income])_

**Tax Rates (2025) table**

| Income type | Rate | Notes |
| --- | --- | --- |
| Resident individual -- employment, professional & entrepreneurial income, capital gains, other taxable income | 12% | Flat rate, no brackets [PwC Moldova] |
| Farming / agricultural enterprises -- entrepreneurial income | 7% | Reduced rate [PwC Moldova] |
| Dividends (general) -- final withholding | 6% | Withheld at source [PwC Moldova] |
| Royalties -- final withholding | 12% | Withheld at source [PwC Moldova] |
| Gambling / lottery / sports-bet winnings -- final withholding | 18% | On the amount exceeding MDL 297 [PwC Moldova] |
| Independent retail-sale individuals (Chapter 10² regime, in force through 2025) | 1% | 1% of declared income, not less than MDL 3,000/year [PwC Moldova] |

- **No progressive band** — Moldova has no separate progressive band -- the 12% applies from the first taxable leu, after exemptions are deducted.

### Personal & Dependent Exemptions (2025)

- **Availability condition** — Available only to residents whose annual taxable income does not exceed MDL 360,000.  _([PwC Moldova Individual -- Deductions; salarii.md])_

**Personal & Dependent Exemptions (2025) table**

| Exemption | Annual (MDL) | Monthly (MDL) | Source |
| --- | --- | --- | --- |
| Personal exemption (standard) | 29,700 | 2,475 | [PwC; salarii.md] |
| Personal exemption (increased / major) | 34,620 | 2,885 | [PwC; salarii.md] |
| Spouse (major) exemption -- transferable if spouse has no income | 21,780 | 1,815 | [PwC Moldova Individual -- Deductions] |
| Dependent exemption (per dependent) | 9,900 | 825 | [PwC; salarii.md] |
| Dependent with severe childhood disability | 21,780 | 1,815 | [PwC Moldova Individual -- Deductions] |

Arithmetic check: 2,475 × 12 = 29,700; 2,885 × 12 = 34,620; 825 × 12 = 9,900; 1,815 × 12 = 21,780. ✓

### Thresholds (2025)

**Thresholds (2025) table**

| Threshold | Amount (MDL) | Notes | Source |
| --- | --- | --- | --- |
| Personal-exemption income ceiling | 360,000 | Exemptions only if annual taxable income ≤ this | [PwC; salarii.md] |
| Mandatory VAT registration | 1,200,000 | Turnover over last 12 consecutive months (2025; raised to 1.5m from 1 Jan 2026, 1.7m from 1 Mar 2026) | [KPMG TaxNewsFlash; PwC] |
| Independent-retail minimum tax | 3,000 | 1% tax but not less than this per year | [PwC Moldova] |
| Minimum monthly wage | 5,500 | 169 hrs/month, approx MDL 32.54/hr; from 1 Jan 2025 (rises to 6,300 from 1 Jan 2026) | [Government of Moldova; WageIndicator] |
| Average monthly forecast salary | 16,100 | Used for benefit ceilings, IT-Park minimum, fine bases (rises to 17,400 for 2026) | [Government of Moldova (gov.md)] |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP -- do not apply resident rules to a non-resident |
| Unknown annual taxable income vs MDL 360,000 ceiling | Assume ceiling exceeded -> NO personal exemption (conservative) |
| Unknown whether self-employed is in justice sector | General fixed CAS (MDL 20,518), flag for reviewer |
| Unknown whether individual is employed (CNAM via payroll) or pays fixed CNAM | Assume fixed annual CNAM (MDL 12,636), flag for reviewer |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown regime (general 12% vs IT Park vs independent retail 1%) | General 12% regime |
| Unknown farming status | Standard 12% (not the 7% farming rate) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (1) tax residency, (2) regime (general self-employed / employee / IT Park / independent retail), and (3) whether health insurance is paid via payroll (9%) or as the fixed annual premium.

**Recommended** -- all sales invoices, purchase invoices/receipts, CNAS/CNAM contribution payment records, prior-year CET18 or tax assessment, VAT registration status, dependent/spouse exemption documentation.

**Ideal** -- complete income and expenditure account, asset register, exemption certificates lodged with the employer (cerere de scutiri), proof of fixed-contribution payments, employment income statements (if mixed employed + self-employed).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This CET18 was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that each is incurred in the production of income under the Tax Code."

### Refusal Catalogue

- **R-MD-1** — Residency determines whether the flat 12% resident rules and exemptions apply. This skill cannot compute tax without knowing whether the client is a Moldovan tax resident. Please confirm before proceeding.
- **R-MD-2** — Annual taxable income near or above MDL 360,000 removes the personal exemption [PwC]. Confirm exact income and exemption entitlement with a reviewer before claiming any exemption.  _([PwC])_
- **R-MD-3** — This skill covers resident individuals and sole proprietors only. Legal entities (SRL, SA) file corporate income tax. Escalate to a warranted Moldovan accountant.
- **R-MD-4** — Non-resident and foreign-citizen taxation has different rules and a 3-day filing trigger on ceasing activity [PwC]. Out of scope. Escalate to a warranted accountant.  _([PwC])_
- **R-MD-5** — Capital-gains computations require specialised analysis under the Tax Code. Escalate to a warranted accountant.
- **R-MD-6** — IT Park residents pay a single 7% tax on turnover that already bundles PIT, CAS and CNAM [PwC]. Do not run the general 12% computation. Use the IT-Park regime and escalate to a reviewer.  _([PwC])_
- **R-MD-7** — Law No. 228/2025 introduces a new simplified freelancer regime (15% up to MDL 1,200,000, 35% above) effective 1 January 2026. It does NOT apply to tax year 2025. For 2025, the legacy rules in this skill apply [EY Tax Alert Moldova, 1 Sep 2025].  _([EY Tax Alert Moldova, 1 Sep 2025])_
- **R-MD-8** — Tax-evasion fines run 80%-100% of the evaded amount and late-payment interest accrues daily [PwC]. Do not advise. Escalate to a warranted accountant immediately.  _([PwC])_
- **R-MD-9** — This skill covers personal income tax (CET18) only. For Moldova VAT, use the dedicated Moldova VAT skill.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Moldovan statements mix Romanian and Russian terms. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | CET18 Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, PLATA, INCASARE, ПЛАТЕЖ | Business income | Entrepreneurial/professional income | If VAT-registered, extract net (excl. 20% VAT) |
| ONORARIU, SERVICII, CONSULTANTA, HONORARIUM | Business income | Professional fees -- typical for self-employed |  |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout -- match to underlying invoices |  |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Business income | Platform payout -- verify against invoices |  |
| WISE PAYOUT, WISE TRANSFER, PAYONEER | Business income | International platform payout |  |
| UPWORK, FIVERR, FREELANCE | Business income | Freelance platform -- net of platform commission |  |
| SALARIU, SALARY, ЗАРПЛАТА, EMPLOYER [name] | Employment income | Employment income (PIT/CAS/CNAM already withheld) | NOT self-employment; usually already taxed at source |
| CHIRIE PRIMITA, RENT RECEIVED, АРЕНДА | Rental income | Other income -- not self-employment |  |
| DOBANDA, INTEREST, ПРОЦЕНТЫ | Investment income | Interest income |  |
| DIVIDEND, DIVIDENDE | Investment income -- final WHT 6% | Dividends | 6% withheld at source -- generally final [PwC] |
| ROYALTY, REDEVENTA | Royalty income -- final WHT 12% | Royalties | 12% withheld at source [PwC] |
| CASTIG LOTERIE, WINNINGS, ВЫИГРЫШ | Winnings -- final WHT 18% | Gambling/lottery/sports | 18% on amount exceeding MDL 297 [PwC] |
| RESTITUIRE SFS, TAX REFUND | EXCLUDE | Not income | Tax refund from prior year |
| GRANT, SUBVENTIE | Check nature | Capital grants EXCLUDE; revenue grants = business income |  |

### 3.2 Expense Patterns (Debits) -- Fully Deductible (business income & expenditure)

**Fully deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| CHIRIE BIROU, OFFICE RENT, АРЕНДА ОФИСА | Office rent | Deductible | Dedicated business premises |
| ASIGURARE PROFESIONALA, PI INSURANCE | Professional insurance | Deductible |  |
| CONTABIL, AUDIT, BOOKKEEP, ACCOUNTANT | Accountancy fees | Deductible |  |
| AVOCAT, LAWYER, JURIST, NOTAR (business) | Legal/notary fees | Deductible | Must be business-related |
| RECHIZITE, OFFICE SUPPLIES, PAPETARIE | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, PUBLICITATE | Marketing/advertising | Deductible |  |
| INSTRUIRE, TRAINING, CURS, SEMINAR, CONFERINTA | Training | Deductible | Must relate to current business |
| COMISION BANCAR, BANK FEE, SPEZE BANCARE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, COMISION PROCESARE | Payment processing fees | Deductible |  |
| POSTA, POSTA MOLDOVEI (business) | Postage | Deductible | Business correspondence |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible (capitalise if large/long-life) | See Tier 2 on capitalisation |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| Perpetual software licence (large value) | Capital item | Capitalise / depreciate | Flag for reviewer -- depreciation per Tax Code Art. 26-27 [RESEARCH GAP -- reviewer to confirm exact depreciation method] |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities expense patterns table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ENERGOCOM, PREMIER ENERGY, GAZ, APA-CANAL | Electricity/gas/water | T2 if home office | 100% if dedicated office; proportional if home |
| MOLDTELECOM, ORANGE, MOLDCELL, STARNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, TELEFON | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR MOLDOVA, WIZZ AIR, TAROM, FLYONE | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, UBER, YANGO, TAXI | Local transport | Deductible if business purpose |  |
| BENZINA, COMBUSTIBIL, PETROM, ROMPETROL, FUEL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARCARE, PARKING | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT deductible expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, CINA, PRANZ, ENTERTAINMENT | Entertainment | Generally NOT deductible | Flag any client-hospitality claim for reviewer |
| PERSONAL, ALIMENTE, SUPERMARKET, LINELLA, KAUFLAND, NR1 | Personal expenses | NOT deductible | Private living costs |
| AMENDA, PENALITATE, FINE, ШТРАФ | Fines/penalties | NOT deductible | Public policy |
| IMPOZIT VENIT, INCOME TAX, PLATA SFS (PIT) | Tax payments | NOT deductible | Income tax cannot reduce income |
| PRELEVARE, DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items

**Capital items expense patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, CALCULATOR | Computer hardware | Capitalise / depreciate | Tax Code depreciation [RESEARCH GAP -- confirm rate/method] |
| IMPRIMANTA, SCANNER, PRINTER | Office equipment | Capitalise / depreciate | [RESEARCH GAP -- confirm rate] |
| MOBILIER, BIROU, SCAUN, FURNITURE | Furniture/fittings | Capitalise / depreciate | [RESEARCH GAP -- confirm rate] |
| AUTO, MASINA, VEHICLE (business) | Motor vehicle | Capitalise / depreciate, business % only | [RESEARCH GAP -- confirm rate] |

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER INTERN, CONT PROPRIU, OWN ACCOUNT | EXCLUDE | Own-account transfer |
| RAMBURSARE CREDIT, LOAN REPAYMENT, CREDIT | EXCLUDE | Loan principal movement |
| CAS, BASS, CNAS, SOCIAL INSURANCE | Contribution payment | Deductible from PIT base (see Section 5) -- not a business expense |
| CNAM, CAM, ASIGURARE MEDICALA | Health contribution payment | Deductible from PIT base (see Section 5) -- not a business expense |
| PLATA TVA, VAT PAYMENT, SFS TVA | EXCLUDE | VAT liability payment, not expense |

### 3.9 Moldovan Banks -- Statement Format Reference

**Moldovan Banks Statement Format Reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Moldova Agroindbank (MAIB) | TRANSFER, PLATA, INCASARE, COMISION | PDF/CSV; date format DD.MM.YYYY |
| Moldindconbank (MICB) | PLATA, TRANSFER, RETRAGERE | PDF/CSV; counterparty in description |
| Victoriabank | PLATA, TRANSFER, COMISION | PDF; Romanian-language descriptions |
| OTP Bank Moldova | PLATA, TRANSFER, CARD | PDF/CSV |
| Revolut / Wise (foreign) | PAYMENT, TRANSFER, CARD PAYMENT | CSV; multi-currency -- convert to MDL at the correct rate |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (VAT-registered freelancer)

**Input line:**
`15.03.2025 ; MAIB INCASARE ; SC EXEMPLU SRL ; PLATA FACT 2025-007 ; +12,000.00 ; MDL`

**Reasoning:**
Client payment for services. Freelancer is VAT-registered (standard 20% VAT), so MDL 12,000 includes VAT. Net = 12,000 / 1.20 = MDL 10,000 (business income). VAT MDL 2,000 is a liability to SFS, excluded from income.

**Classification:** Business income = MDL 10,000. VAT MDL 2,000 excluded. (If NOT VAT-registered, the full MDL 12,000 is business income.)

### Example 2 -- SaaS Subscription (Fully Deductible)

**Input line:**
`01.04.2025 ; MICB CARD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -540.00 ; MDL`

**Reasoning:**
Monthly SaaS subscription, recurring, used in producing income. Fully deductible as an operating expense.

**Classification:** Deductible business expense = MDL 540.00.

### Example 3 -- Employee Monthly Payroll (Net Pay)

**Input:** Employee, gross monthly salary MDL 16,100, standard personal exemption (MDL 2,475/month), no dependents, private sector.

**Reasoning (Tax Code Title II; buhgalter.md; playroll):**
1. Employee CAS 6%: 16,100 × 0.06 = MDL 966.00
2. Employee CNAM 9%: 16,100 × 0.09 = MDL 1,449.00
3. PIT taxable base = gross − CAS − CNAM − exemption = 16,100 − 966.00 − 1,449.00 − 2,475.00 = MDL 11,210.00
4. PIT 12%: 11,210.00 × 0.12 = MDL 1,345.20
5. Net pay = gross − CAS − CNAM − PIT = 16,100 − 966.00 − 1,449.00 − 1,345.20 = **MDL 12,339.80**

Employer also pays CAS 24% on top: 16,100 × 0.24 = MDL 3,864.00 (employer cost, not deducted from the employee).

**Classification:** PIT withheld MDL 1,345.20; net pay MDL 12,339.80; employer CAS MDL 3,864.00.

### Example 4 -- General Self-Employed Annual Computation

**Input:** Resident sole proprietor, general regime (not IT Park, not justice sector, no employees), net business income MDL 300,000, not VAT-registered, single, no dependents, NOT employed elsewhere. Annual income exceeds MDL 360,000 ceiling? No -- but it does NOT exceed it, so the personal exemption is available. (300,000 ≤ 360,000.)

**Reasoning:**
1. PIT base = net business income − personal exemption = 300,000 − 29,700 = MDL 270,300
2. PIT 12%: 270,300 × 0.12 = MDL 32,436.00
3. Fixed annual CAS (individual insurance contract, general): MDL 20,518 [State Social Insurance Budget Law 2025]
4. Fixed annual CNAM (fixed-sum premium): MDL 12,636 [IPN; logos-pres]
5. Total annual liability = 32,436.00 + 20,518 + 12,636 = **MDL 65,590.00**

**Classification:** PIT MDL 32,436.00; CAS MDL 20,518; CNAM MDL 12,636.

> Note: whether the personal exemption is deductible against entrepreneurial income (as opposed to employment income) for a sole proprietor should be confirmed by a reviewer. [RESEARCH GAP -- reviewer to confirm exemption applicability to entrepreneurial income.] If unavailable, PIT = 300,000 × 0.12 = MDL 36,000.00 and total = MDL 69,154.00.

### Example 5 -- Dividend Receipt (Final Withholding)

**Input line:**
`20.06.2025 ; VICTORIABANK ; SC EXEMPLU SRL ; DIVIDENDE 2024 ; +47,000.00 ; MDL`

**Reasoning:**
Dividends suffer a 6% final withholding tax at source [PwC]. If MDL 47,000 is the net amount received, the gross was 47,000 / 0.94 = MDL 50,000 and the 6% tax (MDL 3,000) was already withheld. No further PIT is due; this is generally final.

**Classification:** Investment income, final WHT 6% already settled. Exclude from the 12% PIT base. Flag to reviewer whether amount shown is gross or net.

### Example 6 -- Fixed Contribution Payment (CAS)

**Input line:**
`31.03.2025 ; MAIB PLATA ; CNAS BASS ; CONTRIBUTIE FIXA 2025 ; -20,518.00 ; MDL`

**Reasoning:**
Annual fixed CAS for a self-employed individual under an individual insurance contract, general regime [State Social Insurance Budget Law 2025]. This is a contribution payment, not a business expense; it is tracked separately and reduces the PIT base only to the extent the statute allows (employee CAS/CNAM are deductible; for fixed contributions, confirm with reviewer).

**Classification:** CAS fixed contribution MDL 20,518. [RESEARCH GAP -- reviewer to confirm deductibility of fixed CAS against the PIT base.]

### Example 7 -- Internal Transfer (Exclude)

**Input line:**
`15.05.2025 ; MAIB TRANSFER ; CONT PROPRIU ECONOMII ; ; -25,000.00 ; MDL`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Flat 12% Rate

- **Flat 12% rate rule** — Resident individuals pay a flat 12% on employment, professional and entrepreneurial income, capital gains, and other taxable income -- there are no progressive brackets in 2025. Farming/agricultural enterprises are taxed at a reduced 7% on entrepreneurial income.  _(Tax Code, Title II [PwC Moldova Individual -- Taxes on personal income; PwC])_

### 5.2 The Monthly Payroll PIT Base

- **Monthly PIT base formula** — Monthly PIT base = gross salary − employee CAS (6%) − employee CNAM (9%) − applicable monthly personal/dependent exemptions. The 12% rate is applied to that base. PIT is withheld and remitted by the employer by the 25th of the following month.  _(Tax Code, Title II; administrative practice [buhgalter.md; playroll])_

### 5.3 Personal and Dependent Exemptions

- **Standard personal exemption** — MDL 29,700/year (MDL 2,475/month)  _([PwC; salarii.md])_
- **Increased/major personal exemption** — MDL 34,620/year (MDL 2,885/month) for qualifying persons  _([PwC; salarii.md])_
- **Spouse (major) exemption** — MDL 21,780/year, transferable if the spouse has no income  _([PwC])_
- **Dependent exemption** — MDL 9,900/year per dependent (MDL 21,780/year for a dependent with a severe childhood disability)  _([PwC; salarii.md])_
- **Exemption ceiling** — All exemptions are available only if annual taxable income does not exceed MDL 360,000  _([PwC; salarii.md])_

### 5.4 Deductibility of Contributions from the PIT Base

- **Deductibility of employee CAS/CNAM** — Both employee CAS (6%) and employee CNAM (9%) are deductible when computing the PIT taxable base. This is what makes the Example 3 base lower than gross.  _([PwC Moldova Individual -- Deductions])_

### 5.5 Social Insurance (CAS / BASS)

**Social Insurance (CAS / BASS) table**  _(Law No. 489/1999; State Social Insurance Budget Law for 2025)_

| Payer | Rate / amount | Base | Notes |
| --- | --- | --- | --- |
| Employer (private sector, standard) | 24% | Gross remuneration, meal tickets, other | No salary ceiling; 32% for special working conditions [PwC] |
| Employee | 6% | Gross salary | Withheld by employer; deductible from PIT base [buhgalter.md; rivermate; playroll] |
| Self-employed (individual insurance contract, general) | MDL 20,518/year (fixed) | -- | Annual fixed amount, 2025 [State Social Insurance Budget Law 2025] |
| Self-employed (justice sector -- lawyers, notaries, bailiffs, forensic experts, mediators, authorised administrators) | MDL 27,772/year (fixed) | -- | Annual fixed amount, 2025 [State Social Insurance Budget Law 2025] |

- **Agriculture CAS split** — Agriculture: 24% total (18% employer-paid + 6% from the state budget)  _([PwC])_

### 5.6 Health Insurance (CNAM / CAM)

**Health Insurance (CNAM / CAM) table**  _(Law No. 1593/2002; Mandatory Health Insurance Funds Law for 2025)_

| Payer | Rate / amount | Base | Notes |
| --- | --- | --- | --- |
| Employee | 9% | Wages and other remuneration | Fully employee-borne; employers do NOT pay a separate percentage, only withhold and remit; deductible from PIT base [PwC; playroll; salarii.md] |
| Individual paying fixed sum (notaries, lawyers, bailiffs, family doctors in private practice, etc.) | MDL 12,636/year (fixed) | -- | Fixed annual premium, 2025 (unchanged into 2026) [IPN; logos-pres] |

> Some EOR guides report an employer health split of 4.5% / 4.5%. This is OUTDATED -- since 2021 Moldova's CNAM on salaries is a single 9% employee-borne contribution with no separate employer percentage [confirmed by PwC and playroll].

### 5.7 Contribution & Payroll Totals (Standard Private-Sector Employee)

**Contribution & Payroll Totals table**

| Component | Employee | Employer | Total |
| --- | --- | --- | --- |
| Social insurance (CAS / BASS) | 6% | 24% | 30% |
| Health insurance (CNAM / CAM) | 9% | 0% | 9% |
| **Total contributions** | **15%** | **24%** | **39%** |

Arithmetic check -- employee column: 6 + 9 = 15. ✓ Employer column: 24 + 0 = 24. ✓ Total column: 30 + 9 = 39, and 15 + 24 = 39. ✓ (PIT of 12% is additional and is borne by the employee on the post-contribution, post-exemption base.)

### 5.8 Final Withholding Taxes

**Final Withholding Taxes table**

| Income | Rate | Source |
| --- | --- | --- |
| Dividends (general) | 6% | [PwC] |
| Royalties | 12% | [PwC] |
| Gambling / lottery / sports winnings (on amount exceeding MDL 297) | 18% | [PwC] |

- **Withholding finality** — These are withheld at source and are generally final -- exclude from the 12% PIT base.

### 5.9 Independent Retail-Sale Regime (Chapter 10², 2025 only)

- **Independent retail-sale regime** — Individuals doing independent retail sales (not legal entities) are taxed at 1% of declared income, not less than MDL 3,000 per year. In force during 2025; superseded by Law No. 228/2025 from 1 Jan 2026.  _([PwC])_

### 5.10 IT Park (MITP) Single Tax

- **IT Park single tax** — Residents of the Moldova Innovation Technology Park pay a single 7% tax on turnover (excl. VAT), covering corporate income tax, employee PIT, social and health contributions, and most local/real-estate/road taxes -- but not less than a per-employee minimum equal to 30% of the average monthly forecast salary. Eligibility requires 70%+ of revenue from qualifying IT activities. If a client is an IT-Park resident, do NOT run the general 12% computation (Refusal R-MD-6).  _([PwC; deschidecompanie.md])_

### 5.11 Filing & Payment

**Filing & Payment table**

| Item | Detail | Source |
| --- | --- | --- |
| Annual return | CET18 -- Declarația persoanei fizice cu privire la impozitul pe venit | [PwC; logos-pres] |
| Filing deadline | 30 April of the year following the reporting year (e.g., 30 April 2026 for 2025) | [PwC; logos-pres] |
| PIT settlement | Same deadline -- 30 April of the following year | [PwC] |
| Payroll PIT/CAS/CNAM remittance | By the 25th of the month following payment | [playroll] |
| Foreign-citizen return | Within 3 days of ending activity in Moldova | [PwC] |

### 5.12 Penalties

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Late filing / failure to file | MDL 500 to MDL 1,000 per return, capped at MDL 10,000 total | [PwC Corporate -- Tax administration] |
| Understatement (incorrect return reducing tax/CAS/CNAM) | 20% to 30% of the under-declared amount | [PwC] |
| Diminishing taxable income (deferred-payment beneficiaries, 2023-2025 profit) | 12% to 15% of undeclared/diminished income | [PwC; intelcont] |
| Tax evasion | 80% to 100% of the evaded amount (plus criminal sanctions where evasion exceeds 50 average forecast salaries) | [PwC] |
| Late-payment interest (majorare de întârziere) | NBM short-term policy rate rounded up + 5 percentage points; set at 9% per annum for 2025; accrues daily | [PwC; intelcont; Orbitax] |

> The 0.0301%/day figure on PwC's individual page reflects a later/2026 rate, not the 2025 9% p.a. figure [caveat].

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total floor area), and apply it to rent, electricity, gas, water, internet.
- A dual-use room does NOT qualify.
- **Conservative default:** 0% until the reviewer confirms the room arrangement.
- **Flag for reviewer:** confirm floor-area basis and that the workspace is genuinely dedicated. [RESEARCH GAP -- confirm Tax Code basis for home-office apportionment for sole proprietors.]

### 6.2 Motor Vehicle Business Use

- Only the business-use percentage of fuel, insurance, maintenance and depreciation is deductible.
- Client must maintain a mileage log.
- **Conservative default:** 0% business use until a mileage log is provided.
- **Flag for reviewer:** confirm the business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only; client must provide a reasonable estimate.
- **Conservative default:** 0% deduction until the business percentage is confirmed.

### 6.4 Depreciation / Capital Allowances

- Capital assets must be depreciated rather than expensed.
- The exact depreciation methods, asset categories and rates under the Tax Code (Art. 26-27 and Government regulation) are **[RESEARCH GAP -- reviewer to confirm rates, categories and method for 2025]**. Do not invent rates.
- **Flag for reviewer** on every capitalised asset.

### 6.5 Personal Exemption Entitlement

- Exemptions vanish above MDL 360,000 annual taxable income, and the application of the personal exemption to entrepreneurial (as opposed to employment) income for sole proprietors should be confirmed.
- **Flag for reviewer:** confirm exemption entitlement and the precise income definition used for the ceiling test.

### 6.6 Deductibility of Self-Employed Fixed Contributions

- Employee CAS (6%) and CNAM (9%) are explicitly deductible from the PIT base [PwC]. Whether the fixed annual CAS (MDL 20,518) and fixed CNAM (MDL 12,636) reduce a self-employed person's PIT base is **[RESEARCH GAP -- reviewer to confirm]**.

### 6.7 Bad Debt Write-Off

- Deductible only if income was previously declared, recovery steps were taken, and the debt is genuinely irrecoverable. Flag all three conditions for the reviewer.

## Section 7 -- Excel Working Paper Template

```
MOLDOVA PERSONAL INCOME TAX -- CET18 WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Regime: General self-employed / Employee / IT Park / Independent retail
Annual taxable income <= MDL 360,000 (exemption available)? Yes / No

A. BUSINESS / EMPLOYMENT INCOME
  A1. Client/professional income (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, Wise, etc.)           ___________
  A3. Employment income (PIT usually withheld at source)      ___________
  A4. Other income (rental, etc.)                             ___________
  A5. TOTAL income                                            ___________

B. ALLOWABLE BUSINESS EXPENSES
  B1. Office rent                                             ___________
  B2. Professional insurance                                  ___________
  B3. Accountancy / legal / notary fees                       ___________
  B4. Office supplies                                         ___________
  B5. Software subscriptions                                  ___________
  B6. Marketing / advertising                                 ___________
  B7. Bank / payment processing fees                          ___________
  B8. Training                                                ___________
  B9. Travel (business)                                       ___________
  B10. Telecoms (business %)                                  ___________
  B11. Home office (% of utilities/rent)                      ___________
  B12. Vehicle expenses (business %)                          ___________
  B13. Depreciation (per Tax Code -- reviewer to confirm)     ___________
  B14. TOTAL expenses                                         ___________

C. NET BUSINESS INCOME (A1+A2 - B14)                          ___________

D. CONTRIBUTIONS DEDUCTIBLE FROM PIT BASE
  D1. Employee CAS 6% (if employed)                           ___________
  D2. Employee CNAM 9% (if employed)                          ___________
  D3. TOTAL deductible contributions                          ___________

E. EXEMPTIONS (only if income <= MDL 360,000)
  E1. Personal exemption (29,700 / 34,620)                    ___________
  E2. Spouse exemption (21,780, if applicable)                ___________
  E3. Dependent exemptions (9,900 x n / 21,780 disabled)      ___________
  E4. TOTAL exemptions                                        ___________

F. PIT TAXABLE BASE (C + A3 + A4 - D3 - E4)                   ___________

G. PIT AT 12% (7% if farming)                                 ___________

H. SEPARATE SELF-EMPLOYED CONTRIBUTIONS (not via payroll)
  H1. Fixed annual CAS (20,518 general / 27,772 justice)      ___________
  H2. Fixed annual CNAM (12,636)                              ___________

I. FINAL WITHHELD ITEMS (informational -- already settled)
  I1. Dividends (6% WHT)                                      ___________
  I2. Royalties (12% WHT)                                     ___________
  I3. Winnings (18% WHT on amount > MDL 297)                  ___________

J. TOTAL ANNUAL LIABILITY (G + H1 + H2 - any PIT withheld)    ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Annual income vs MDL 360,000 ceiling confirmed?
  [ ] Regime confirmed (general / IT Park / independent retail)?
  [ ] Justice-sector status confirmed (CAS 20,518 vs 27,772)?
  [ ] Health insurance route confirmed (9% payroll vs 12,636 fixed)?
  [ ] Exemption applicability to entrepreneurial income confirmed?
  [ ] Depreciation rates/methods confirmed against Tax Code?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Final-withheld items excluded from the 12% base?
```

## Section 8 -- Bank Statement Reading Guide

### Moldovan Bank Statement Formats

**Moldovan Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Moldova Agroindbank (MAIB) | PDF, CSV | Data, Descriere, Debit, Credit, Sold | Most common; description contains counterparty + reference; DD.MM.YYYY |
| Moldindconbank (MICB) | PDF, CSV | Data, Detalii, Suma, Sold | Counterparty in details field |
| Victoriabank | PDF | Data, Descriere, Retragere, Incasare, Sold | Romanian-language descriptions |
| OTP Bank Moldova | PDF, CSV | Data, Descriere, Suma, Sold |  |
| Revolut / Wise (foreign) | CSV | Date, Counterparty, Amount, Currency, Reference | Multi-currency -- convert to MDL |

### Key Moldovan / Romanian Banking Terms

**Key Moldovan / Romanian Banking Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFER / TRANSFERIRE | Transfer | Check direction for income/expense |
| PLATA | Payment | Outgoing payment -- check counterparty |
| INCASARE | Receipt / collection | Potential income |
| RETRAGERE | Withdrawal | Cash withdrawal -- ask what it was for |
| COMISION / SPEZE | Fee / charges | Deductible (business account) |
| DOBANDA | Interest | Interest income or bank charge |
| DEBIT DIRECT | Direct debit | Regular expense (utility, subscription) |
| SALARIU | Salary | Employment income (usually taxed at source) |
| IMPOZIT | Tax | Tax payment -- not deductible |
| CHIRIE | Rent | Office rent (expense) or rent received (income) |
| CONT PROPRIU | Own account | Internal transfer -- exclude |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- MOLDOVA PERSONAL INCOME TAX
1. Are you a Moldovan tax resident?
2. What is your regime: general self-employed, employee, IT Park resident, or independent retail?
3. Is your annual taxable income at or below MDL 360,000 (so exemptions apply)?
4. Are you in the justice sector (lawyer, notary, bailiff, mediator, forensic expert, authorised administrator)?
5. How do you pay health insurance: 9% through payroll, or the MDL 12,636 fixed annual premium?
6. Are you VAT-registered (turnover over MDL 1.2m in the last 12 months)?
7. Marital status and number of dependents? Does your spouse have income?
8. Home office: dedicated room? If yes, what % of floor area?
9. Vehicle: business use %? Do you keep a mileage log?
10. Phone/internet: business use %?
11. Did you receive any dividends (6%), royalties (12%), or winnings (18%) already taxed at source?
12. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References table**

| Topic | Reference |
| --- | --- |
| Personal income tax (flat 12%) | Tax Code (Codul Fiscal, Law No. 1163/1997), Title II |
| Exemptions & deductions | Tax Code, Title II [PwC Moldova Individual -- Deductions] |
| Social insurance (CAS/BASS) | Law No. 489/1999; State Social Insurance Budget Law for 2025 |
| Health insurance (CNAM/CAM) | Law No. 1593/2002; Mandatory Health Insurance Funds Law for 2025 |
| Independent-activity regime (from 2026) | Law No. 228 of 10 July 2025 (NOT 2025) |
| Annual return | CET18 -- Declarația persoanei fizice cu privire la impozitul pe venit |
| Tax authority | Serviciul Fiscal de Stat (SFS), sfs.md |
| Social administrator | CNAS, cnas.gov.md |
| Health administrator | CNAM, cnam.md |

### Caveats (read before relying on figures)

- PwC Worldwide Tax Summaries pages were last reviewed 14 January 2026 and now display 2026 figures; the 2025 exemption amounts (MDL 29,700 / 34,620 / 21,780 / 9,900), which are unchanged into 2026, were independently confirmed against 2025-specific Moldovan sources (salarii.md, buhgalter.md).
- The exact 2025 fixed annual CAS amounts (general MDL 20,518; justice MDL 27,772) come from the State Social Insurance Budget Law for 2025 reported via secondary aggregators (cis-legislation, WebSearch); the primary cis-legislation page could not be fetched directly. **The official CNAS / sfs.md figures should be confirmed before publishing.** [RESEARCH GAP -- reviewer to confirm exact 2025 fixed-contribution MDL digits.]
- The MDL 12,636 fixed annual CNAM premium for 2025 is confirmed unchanged into 2026 [IPN; logos-pres].
- The 4.5% / 4.5% employer health split seen in some EOR guides is OUTDATED -- CNAM on salaries is a single 9% employee-borne contribution.
- The late-payment interest rate is set annually (NBM rate +5pp = 9% p.a. for 2025). The 0.0301%/day figure on PwC's individual page reflects a later period.
- The 1% independent-retail regime and the old independent-activity regime are superseded by Law No. 228/2025 effective 1 Jan 2026 -- for 2025 the legacy rules apply.
- **Recommend a verified accountant confirm the exact 2025 fixed-contribution MDL figures, the depreciation rates, and the personal-exemption income ceiling against the SFS Tax Code and the 2025 social-insurance budget law before relying on them.**

### Test Suite

**Test 1 -- Standard private-sector employee, monthly payroll.**
Input: Gross MDL 16,100/month, standard personal exemption MDL 2,475, no dependents.
Expected: Employee CAS = MDL 966.00; CNAM = MDL 1,449.00; PIT base = 16,100 − 966 − 1,449 − 2,475 = MDL 11,210.00; PIT 12% = MDL 1,345.20; net pay = MDL 12,339.80; employer CAS 24% = MDL 3,864.00.

**Test 2 -- General self-employed, exemption available.**
Input: Net business income MDL 300,000 (≤ 360,000 ceiling), single, no dependents, general regime, exemption applies.
Expected: PIT base = 300,000 − 29,700 = MDL 270,300; PIT 12% = MDL 32,436.00; fixed CAS MDL 20,518; fixed CNAM MDL 12,636; total = MDL 65,590.00.

**Test 3 -- General self-employed, NO exemption (income over ceiling).**
Input: Net business income MDL 500,000 (> 360,000), general regime.
Expected: No personal exemption. PIT 12% = 500,000 × 0.12 = MDL 60,000.00; fixed CAS MDL 20,518; fixed CNAM MDL 12,636; total = MDL 93,154.00.

**Test 4 -- Farming enterprise (reduced rate).**
Input: Entrepreneurial income of a farming enterprise MDL 200,000, 7% rate.
Expected: PIT = 200,000 × 0.07 = MDL 14,000.00.

**Test 5 -- Justice-sector self-employed contributions.**
Input: Notary, general 12% PIT on net income MDL 400,000 (no exemption, over ceiling).
Expected: PIT 12% = MDL 48,000.00; fixed CAS MDL 27,772 (justice); fixed CNAM MDL 12,636; total = MDL 88,408.00.

**Test 6 -- Dividend final withholding.**
Input: Net dividend received MDL 47,000 (6% WHT already taken).
Expected: Gross = 47,000 / 0.94 = MDL 50,000.00; WHT 6% = MDL 3,000.00; no further PIT; exclude from 12% base.

**Test 7 -- VAT-registered freelancer client payment.**
Input: Client payment MDL 12,000 incl. 20% VAT.
Expected: Net business income = 12,000 / 1.20 = MDL 10,000.00; VAT MDL 2,000 excluded.

**Test 8 -- Independent retail minimum tax.**
Input: Independent retail individual, declared income MDL 200,000 (Chapter 10², 2025).
Expected: 1% = 200,000 × 0.01 = MDL 2,000.00; but not less than MDL 3,000 -> tax = MDL 3,000.00.

## PROHIBITIONS

- **Confirm residency before applying resident rules** — NEVER apply resident rules without confirming Moldovan tax residency
- **Personal exemption income limit** — NEVER claim a personal exemption when annual taxable income exceeds MDL 360,000 MDL
- **Flat PIT rate, no progressive brackets** — NEVER apply progressive brackets -- Moldova PIT is a flat 12% (7% farming) in 2025
- **IT-Park resident taxation** — NEVER run the general 12% computation for an IT-Park resident (single 7% turnover tax instead)
- **Law 228/2025 freelancer regime effective date** — NEVER apply the Law 228/2025 freelancer regime (15%/35%) to tax year 2025 -- it begins 1 Jan 2026
- **CNAM contribution structure** — NEVER add a separate employer health-insurance percentage -- CNAM is a single 9% employee-borne contribution
- **VAT exclusion from business income** — NEVER include VAT collected on sales in business income for a VAT-registered client
- **Exclude final-withheld income from PIT base** — NEVER include final-withheld dividends/royalties/winnings in the 12% PIT base
- **Depreciation rates research gap** — NEVER invent depreciation rates -- they are a RESEARCH GAP pending reviewer confirmation
- **Non-deductible items** — NEVER allow income tax, fines, drawings, or personal expenses as deductions
- **Estimates require sign-off** — NEVER present tax calculations as definitive -- always label as estimated and pending accountant sign-off

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
