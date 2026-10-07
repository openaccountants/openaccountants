---
name: cyprus-income-tax
description: Use this skill whenever asked about Cyprus personal income tax for self-employed individuals or employees. Trigger on phrases like "how much tax do I pay in Cyprus", "TD1", "IR1", "income tax return Cyprus", "allowable deductions", "Social Insurance", "GHS", "GESY", "provisional tax", "temporary tax", "chargeable income", "non-dom", "Special Defence Contribution", "SDC", "50% expat exemption", "183-day rule", "60-day rule", "self-employed tax Cyprus", or any question about filing or computing income tax for a self-employed individual or employee in Cyprus. Also trigger when preparing or reviewing a TD1/IR1 return, computing deductible expenses, advising on provisional (temporary) tax instalments, or assessing tax residency under the 183-day or 60-day rule. This skill covers PIT rate bands (2025 and the 2026 reform), Social Insurance and GHS/GESY contributions, employer-only funds, the 1/5 deductions cap, expat exemptions, SDC for domiciled residents, penalties, and interaction with VAT and social insurance. ALWAYS read this skill before touching any Cyprus income tax work.
version: 0.1
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-02
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus Income Tax for Individuals and the Self-Employed

This Guide covers Cyprus personal income tax for resident individuals: employees, the self-employed, landlords and pensioners. Figures are for tax year 2026. The 2026 tax reform (Law 244(I)/2025 and the amending laws passed with it) applies from tax year 2026 and changes the bands, the filing duty, the personal deductions, the Special Defence Contribution (SDC) on rent and dividends, and the accounts and deadline rules for the self-employed. For tax year 2025 and earlier, use the official 2025 return guide, not this Guide.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Tax | Personal income tax (Φόρος Εισοδήματος) |
| Currency | EUR only |
| Tax year | Calendar year (1 January to 31 December) |
| Primary legislation | Income Tax Law N.118(I)/2002, as amended (from 2026 by Law 244(I)/2025) |
| Supporting legislation | Special Defence Contribution Law N.117(I)/2002; Assessment and Collection of Taxes Law (amended by Law 243(I)/2025) |
| Tax authority | Cyprus Tax Department (Τμήμα Φορολογίας), Ministry of Finance |
| Filing portal | Tax For All (TFA) only, from tax year 2026; TAXISnet was used for tax years 2017 to 2025 |
| Return for tax year 2026 | Filed during 2027; deadline in the deadlines table in Section 5.12 |

### Tax Rate Brackets: tax year 2026 (2026 reform)

The scale applies to chargeable income (taxable income after exemptions and deductions), per person. Cyprus taxes spouses separately. The 0% band is the tax-free amount; there is no separate personal allowance.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| 0% band: chargeable income up to | EUR 22,000 | "0% από €0 μέχρι €22.000" |
| Rate on that band | 0% | "0% από €0 μέχρι €22.000" |
| 20% band: from | EUR 22,001 | "20% από €22.001 μέχρι €32.000" |
| 20% band: to | EUR 32,000 | "20% από €22.001 μέχρι €32.000" |
| Rate on that band | 20% | "20% από €22.001 μέχρι €32.000" |
| 25% band: from | EUR 32,001 | "25% από €32.001 μέχρι €42.000" |
| 25% band: to | EUR 42,000 | "25% από €32.001 μέχρι €42.000" |
| Rate on that band | 25% | "25% από €32.001 μέχρι €42.000" |
| 30% band: from | EUR 42,001 | "30% από €42.001 μέχρι €72.000" |
| 30% band: to | EUR 72,000 | "30% από €42.001 μέχρι €72.000" |
| Rate on that band | 30% | "30% από €42.001 μέχρι €72.000" |
| 35% band: from | EUR 72,001 | "35% από €72.001 και άνω" |
| Top rate, on everything from that amount up | 35% | "35% από €72.001 και άνω" |
| Tax-free amount up to tax year 2025 (not for 2026) | EUR 19,500 | "έχει αυξηθεί από €19.500 σε €22.000 με εφαρμογή από το φορολογικό έτος 2026" |

The Tax Department's return page prints the cumulative tax at the top of each 2026 band:

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/ |
| Cumulative tax at the top of the 20% band | EUR 2,000 | "32.000 20% 2.000 2.000" |
| Cumulative tax at the top of the 25% band | EUR 4,500 | "42.000 25% 2.500 4.500" |
| Cumulative tax at the top of the 30% band | EUR 13,500 | "72.000 30% 9.000 13.500" |
| Deadline for the tax year 2025 return (extended by decree; not the 2026 deadline) | 31 October 2026 | "For the current year (tax year 2025) the deadline for submitting a tax return is October 31, 2026" |

Above the top of the 30% band, tax is the cumulative figure for the 30% band plus the top rate on the excess. The page writes it as "(Income-72.000)*35%+13.500".

### Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Unknown tax year | Ask. Use this Guide only for tax year 2026 income; send tax year 2025 work to the 2025 return guide |
| Unknown residency | Treat as resident only if the 183-day rule or the 60-day rule is met (Section 5.2); otherwise STOP and confirm |
| Unknown domicile status | Treat as Cyprus-domiciled (SDC applies). Non-dom status is a fact that needs evidence (Section 5.8) |
| Unknown business-use share (vehicle, phone, home) | No deduction |
| Unknown expense category | Not deductible |
| Unknown self-employed insurable income | Refer to the Social Insurance Services category table; do not assert an amount |
| Unknown VAT registration | Treat as registered if taxable supplies passed the registration threshold in Section 5.10 |
| Unknown whether expense is entertainment or private | Not deductible |
| Unknown family income for the new personal deductions | Do not grant the child, housing or green deductions (Section 5.6) |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable: bank statement for the full tax year in CSV, PDF or pasted text, plus confirmation of (1) Cyprus tax residency (183-day or 60-day rule), (2) domicile status (domiciled or non-dom, which decides SDC), (3) employment status (employee under PAYE, self-employed, or both), and (4) age at 31 December of the tax year (it decides the filing duty, Section 5.12).

Recommended: all sales invoices, purchase invoices and receipts, Social Insurance and GHS payment records, the prior year return or assessment, VAT registration status, occupational category (for self-employed Social Insurance), and, for the new personal deductions, the gross income of the spouse or partner and the number of dependent children.

Ideal: complete income and expenditure account, asset register with capital allowances schedule, provisional (temporary) tax payment confirmations, employer emoluments certificates, reviewed or audited accounts where the turnover thresholds in Section 5.12 require them, and evidence for any exemption claim (Section 5.7).

Refusal if minimum is missing: SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This return was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met, and must confirm residency and domicile status."

### Refusal Catalogue

- **R-CY-1**: Residency unknown. "Cyprus tax residents are taxed on worldwide income; non-residents only on Cyprus-source income. This Guide cannot proceed without confirming residency under the 183-day rule or the 60-day rule. Please confirm before proceeding."
- **R-CY-2**: Companies and partnerships. "This Guide covers individuals and sole-trader self-employed only. Companies (corporate income tax, whose rate changed from tax year 2026) and partnerships file separate returns. Escalate to a Cyprus-licensed accountant."
- **R-CY-3**: Non-resident and dual-resident income. "Non-resident and dual-resident taxation, and double-tax-treaty relief, have different rules. Out of scope. Escalate to a Cyprus-licensed accountant."
- **R-CY-4**: Capital gains and property disposals. "Cyprus Capital Gains Tax on disposals of immovable property situated in Cyprus (and related shares) is a separate tax. Out of scope. Escalate to a Cyprus-licensed accountant."
- **R-CY-5**: Arrears and enforcement. "Client has outstanding tax or Social Insurance arrears or is subject to Tax Department or Social Insurance Services enforcement. From 2026 the Tax Department may also seal business premises for repeated non-filing or large debts. Do not advise. Escalate to a Cyprus-licensed accountant immediately."
- **R-CY-6**: VAT return requested. "This Guide covers personal income tax only. For Cyprus VAT, use the `cyprus-vat-return` Guide."
- **R-CY-7**: Non-dom and SDC structuring. "Non-domicile status and Special Defence Contribution planning require confirmation of the 17-of-20-year deemed-domicile test and the individual's domicile of origin. Use the `cy-non-dom` Guide and flag for a Cyprus-licensed accountant; do not assert non-dom status without evidence."
- **R-CY-8**: Crypto-asset disposals, approved share option plans, AIF carried interest. "These are taxed at special rates under their own rules (Section 5.3). Flag for a Cyprus-licensed accountant."

## Section 3: Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to the rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Greek and transliterated terms are included because Cyprus statements often appear in Greek or mixed Greek and English. If multiple patterns match, use the most specific. If none match, fall through to Section 5.

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, EMBASMA, PAYMENT | Self-employment income | Business income | If VAT-registered, extract the net amount (excluding VAT at the rate in Section 5.10) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, AMOIVI | Self-employment income | Business income | Professional fees, typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Self-employment income | Business income | Platform payout; match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Self-employment income | Business income | Platform payout; verify against invoices |
| WISE PAYOUT, REVOLUT PAYOUT | Self-employment income | Business income | Check if business or personal |
| UPWORK, FIVERR, TOPTAL | Self-employment income | Business income | Freelance platform; net of commission |
| MISTHOS, SALARY, PAYROLL, EMPLOYER [name] | Employment income (PAYE) | Employment income | NOT self-employment; emoluments under PAYE |
| ENOIKIO, RENT RECEIVED | Rental income | Rental income | Income tax and GHS; no SDC on rent from 2026 (Section 5.3) |
| TOKOS, INTEREST RECEIVED | Investment income | EXEMPT from income tax | SDC if resident and domiciled; GHS (Section 5.8) |
| MERISMA, DIVIDEND | Investment income | EXEMPT from income tax | SDC if resident and domiciled; GHS (Section 5.8) |
| TAX REFUND, EPISTROFI FOROU | EXCLUDE | Not income | Tax refund from prior year |
| GOVERNMENT GRANT, EPIDOMA | Check nature | Capital grants EXCLUDE; revenue grants = income | Confirm grant nature |

### 3.2 Expense Patterns (Debits): Fully Deductible (Self-Employment)

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, ENOIKIO GRAFEIOU | Office rent | Deductible | Dedicated business premises. From 1 July 2026 rent must be paid by bank transfer, card or other electronic means (Section 5.3) |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, LOGISTIS | Accountancy and audit fees | Deductible |  |
| LAWYER, LEGAL, DIKIGOROS (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing and advertising | Deductible |  |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training | Deductible | Must relate to current business |
| PROFESSIONAL BODY, ICPAC SUBSCRIPTION | Professional subscriptions | Deductible |  |
| BANK CHARGE, MAINTENANCE FEE, SPEXODA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS | IT infrastructure | Deductible | If capital, use capital allowances |

### 3.3 Expense Patterns (Debits): SaaS and Software

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT, M365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| SOFTWARE LICENCE (perpetual, high value) | Capital item | Capital allowance | Capitalise per wear-and-tear schedule |

### 3.4 Expense Patterns (Debits): Utilities (may need apportionment)

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EAC, AHK, ELECTRICITY, ILEKTRISMOS | Electricity | T2 if home office | Full if dedicated office; proportional if home |
| WATER BOARD, YDREFSI | Water | T2 if home office | Proportional if home |
| CYTA, PRIMETEL, EPIC, CABLENET | Telecoms and broadband | T2 | Business use portion only; no deduction if mixed and unconfirmed |

### 3.5 Expense Patterns (Debits): Travel

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RYANAIR, WIZZ AIR, AEGEAN, CYPRUS AIRWAYS, EASYJET | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| BOLT, TAXI, UBER | Local transport | Deductible if business purpose |  |
| FUEL, PETROLINA, EKO, PETROL | Vehicle fuel | T2: business share only | Requires mileage log |
| PARKING | Parking | T2: business share only |  |

### 3.6 Expense Patterns (Debits): NOT Deductible

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible by default | Private or non-business; flag if a documented business purpose exists |
| PERSONAL, GROCERIES, SUPERMARKET, ALPHAMEGA, LIDL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, PROSTIMO, PARKING FINE | Fines and penalties | NOT deductible | Public policy |
| INCOME TAX, FOROS, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits): Capital Items (Capital Allowances)

| Pattern | Category | Annual Rate | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | See 5.4 [RESEARCH GAP: reviewer to confirm the wear-and-tear rate] | Capital allowance, not expense |
| PRINTER, SCANNER, COPIER | Office equipment | See 5.4 [RESEARCH GAP: reviewer to confirm] | Capital allowance |
| FURNITURE, DESK, CHAIR | Furniture and fittings | See 5.4 [RESEARCH GAP: reviewer to confirm] | Capital allowance |
| VEHICLE, CAR (business) | Motor vehicle | See 5.4 [RESEARCH GAP: reviewer to confirm] | Business share only |

### 3.8 Exclusions, Social Insurance, and Tax Credits (Neither Income nor Expense)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| SOCIAL INSURANCE, KOINONIKES ASFALISEIS | Deduction within the one-fifth cap | Deductible against income, NOT a business expense (Section 5.6) |
| GHS, GESY, GENIKO SYSTIMA YGEIAS | Deduction within the one-fifth cap | Deductible against income (Section 5.6) |
| VAT PAYMENT, FPA | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, TEMPORARY TAX, PROSORINI FORO | Credit against final liability | Not an expense |

### 3.9 Cyprus Banks: Statement Format Reference

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Cyprus | EMBASMA, METAFORA, CHREOSI, KARTA | PDF or CSV; often Greek and English; date DD/MM/YYYY |
| Hellenic Bank | PAYMENT, TRANSFER, DD, FEE | PDF or CSV; counterparty in description |
| Eurobank Cyprus | TRANSFER, DIRECT DEBIT, CHARGE | PDF; private and business |
| Astrobank / Alpha Bank Cyprus | METAFORA, PLIROMI, SPEXODA | PDF; mixed-language descriptions |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency; use EUR amounts |

## Section 4: Worked Examples

Amounts in the bank lines below are hypothetical.

### Example 1: Client Payment (VAT-registered self-employed)

Input line:
`15/03/2026 ; BANK OF CYPRUS EMBASMA ; ANDREOU TRADING LTD ; PLIROMI INV-2026-003 ; +1,190.00 ; EUR`

Reasoning: client payment for services. The self-employed person is VAT-registered, so the receipt includes VAT at the standard rate in Section 5.10. The net amount is business income. The VAT part is a liability to the Tax Department and is excluded from income.

Classification: self-employment income = the net amount. VAT excluded.

### Example 2: SaaS Subscription (Fully Deductible)

Input line:
`01/04/2026 ; HELLENIC BANK DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR`

Reasoning: monthly SaaS subscription, recurring, wholly business. Deductible as an operating expense. For a VAT-registered person, the amount net of recoverable input VAT is the expense.

Classification: deductible expense (net of recoverable VAT where registered).

### Example 3: Entertainment (Private)

Input line:
`22/04/2026 ; BANK OF CYPRUS KARTA ; OPSO RESTAURANT ; CLIENT DINNER ; -85.00 ; EUR`

Reasoning: client meals are treated as private by default and fail the wholly-and-exclusively test unless a business purpose is documented. Flag for the reviewer if a documented business-entertainment policy exists.

Classification: NOT deductible by default.

### Example 4: Social Insurance and GHS Payment (Self-Employed)

Input line:
`10/01/2026 ; BANK OF CYPRUS DD ; SOCIAL INSURANCE SERVICES ; Q4 CONTRIBUTION ; -2,490.00 ; EUR`

Reasoning: self-employed Social Insurance and GHS contributions are deducted from income within the one-fifth cap (Section 5.6), NOT as a business operating expense. Record separately.

Classification: contribution deduction (within the one-fifth cap), not a business expense.

### Example 5: Tax on chargeable income (hypothetical, tax year 2026)

Input: Cyprus resident self-employed person; chargeable income after all deductions of EUR 50,000 (hypothetical).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| Hypothetical chargeable income | EUR 50,000 | Hypothetical; bands from the table in Section 1 |
| Tax: the 20% band in full, the 25% band in full, then the 30% rate on the part above EUR 42,000 | EUR 6,900 | Our arithmetic; case A in the test suite |

The 0% band carries no tax. The result matches the return page's cumulative figure at the top of the 25% band plus the 30% rate on the excess.

### Example 6: Foreign Pension Income (special mode, hypothetical)

Input line:
`05/02/2026 ; EUROBANK CYPRUS EMBASMA ; UK PENSION PROVIDER ; MONTHLY PENSION ; +1,500.00 ; EUR`

Reasoning: a pension for services rendered abroad may be taxed at the special rate in Section 5.3 on the amount above the annual threshold there, OR at the normal scale. The election is made each year.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf |
| Hypothetical annual foreign pension | EUR 18,000 | Hypothetical |
| Special-mode tax on that pension: the special rate on the amount above the threshold | EUR 650 | Our arithmetic; case D in the test suite |

Classification: flag for reviewer to confirm the annual election. Present both methods and compare with the normal scale.

## Section 5: Rules

### 5.1 The Wholly and Exclusively Test

- **Wholly and exclusively test**: an expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned on a reasonable, documented basis. [Legacy rule, kept; no saved official page was found that prints the wording, so treat it as the working standard and confirm with the reviewer.]

### 5.2 Residency and Scope of Charge

Source: the Tax Department page https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/ and the reform presentation https://www.gov.cy/media/sites/167/2026/05/%CE%A6%CE%BF%CF%81%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CE%BA%CE%AE-%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-2026-%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AC-%CF%80%CF%81%CF%8C%CF%83%CF%89%CF%80%CE%B1-11.05.2026.pdf

- **Worldwide or source**: Cyprus tax residents are taxed on worldwide income; non-residents only on income arising in Cyprus.
- **183-day rule**: an individual is resident for a tax year if they stay in Cyprus for one or more periods exceeding 183 days in total in that year. More than 183 days, not 183 exactly.
- **60-day rule**: an individual who does not meet the 183-day rule is resident if ALL of these hold in the tax year: (a) at least 60 days in Cyprus; AND (b) does not reside for more than 183 days in any other single country; AND (c) carries on a business in Cyprus, and/or is employed in Cyprus (not necessarily by a Cypriot employer), and/or holds an office in a Cyprus tax resident company; AND (d) keeps a permanent home in Cyprus, owned or rented. If the business, employment or office ends during the year, the person is not resident for that year under this rule; the reform presentation says the condition must hold until 31 December of the tax year.
- **2026 change to the 60-day rule**: the reform removed the condition that the person must not be tax resident in another country. Being tax resident elsewhere no longer blocks the 60-day rule; the 183-days-in-another-country test in (b) still applies.

### 5.3 Income Determination

| Income type | Income tax treatment (tax year 2026) |
| --- | --- |
| Employment emoluments | Taxable at the scale; PAYE withheld by the employer |
| Self-employment profit | Taxable at the scale |
| Dividends | NOT taxable for income tax; SDC if resident and domiciled (Section 5.8); GHS |
| Interest | NOT taxable for income tax (the 2026 law exempts all interest income of individuals); SDC if resident and domiciled (Section 5.8); GHS |
| Rental income | Taxable at the scale, with the flat expenses deduction for buildings in the TD59A table (Section 5.6) plus capital allowances and interest. SDC on rent is abolished from 1 January 2026. GHS still applies |
| Pension for services rendered abroad | Normal scale, OR the special rate on the amount above the annual threshold in the table below (yearly election) |
| Gains on disposal of crypto-assets (new article 20E, from 2026) | Special rate in the table below; crypto losses set off only against crypto gains of the same year, with no carry forward; mined crypto is taxed normally |
| Benefit from approved employee share option or share award plans (new article 20D) | Special rate in the table below, taxed separately and not added to other income |
| AIF carried interest and UCITS performance fees (articles 20b and 20c) | Optional special rate with a minimum tax, elected each year (TD59A table, Section 5.6) |
| Gains on disposal of shares and other titles | Not settled on any saved official page. The Income Tax Law presentation names article 8(22) (an exemption subsection) only for its change from 1 January 2031, under which redeeming a unit or share in a collective investment scheme "ΔΕΝ συνιστά διάθεση τίτλου (εδάφιο (22))". Do not assert an exemption or a charge; refer |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf |
| Special rate on a foreign-services pension, on the amount above the threshold | 5% | "συντελεστή ύψους 5%, από €3.420 σε €5.000" |
| Annual threshold from 2026 | EUR 5,000 | "συντελεστή ύψους 5%, από €3.420 σε €5.000" |
| Threshold up to tax year 2025 (not for 2026) | EUR 3,420 | "συντελεστή ύψους 5%, από €3.420 σε €5.000" |
| Special rate on crypto-asset disposal gains | 8% | "Τα κέρδος υπόκεινται σε φορολογία με συντελεστή ύψους 8%" |
| Special rate on approved share option or share award benefits | 8% | "υπόκειται σε φορολογία με συντελεστή ύψους 8%, και δεν προστίθεται σε οποιοδήποτε άλλο εισόδημα" |
| Cap on share option benefits taxed at the special rate, per rolling ten years | EUR 1,000,000 | "του ενός εκατομμυρίου ευρώ (€1.000.000)" |
| Deduction for donations to approved cultural institutions, only to the extent it creates no loss | EUR 50,000 | "μέχρι €50.000 αναφορικά με δωρεές/συνεισφορές σε πολιτιστικά ιδρύματα" |

Rent and GHS from 2026 (FAQs, https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf): income tax on rent is paid through provisional tax in two instalments, on 31 July and 31 December of the tax year. A tenant that is a legal person (a company) must still withhold GHS from the rent. Where no GHS was withheld, the landlord pays it by self-assessment in two instalments on the same dates. From 1 July 2026, rent for property in Cyprus may be collected only by bank transfer, debit or credit card, or another recognised electronic means; cash and cheques are not allowed.

### 5.4 Capital Allowances (Wear and Tear)

- **Capital allowances treatment**: capital items are relieved through wear-and-tear (capital) allowances, not as outright deductions.

[RESEARCH GAP: reviewer to confirm] The wear-and-tear percentages by asset class (computers, plant and machinery, motor vehicles, furniture, commercial buildings) were not found on any saved Tax Department page and must be taken from the Income Tax Law or Tax Department guidance before any capital-allowance figure is asserted.

### 5.5 Social Insurance and GHS (GESY)

Social Insurance rates (Social Insurance Services rules as printed on the government business portal):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/ |
| Employee share on insurable earnings | 8.8% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| Employer share on the employee's insurable earnings | 8.8% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| State share | 5.2% | "proportion of 8.8%, 8.8% and 5.2%, respectively" |
| Self-employed person's own share on insurable income | 16.6% | "21.8% on their insurable income; 16.6% of which is paid by the self-employed" |
| Self-employed rate including the state share | 21.8% | "21.8% on their insurable income; 16.6% of which is paid by the self-employed" |
| Employer-only Redundancy Fund | 1.2% | "employers must contribute 1.2% to the Redundancy Fund" |
| Employer-only Human Resources Development Fund | 0.5% | "0.5% to the Human Resources Development Fund" |
| Employer-only Social Cohesion Fund | 2% | "2% to the Social Cohesion Fund for their employees" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sisweb.mlsi.gov.cy/anotato2025/ |
| Maximum insurable earnings, monthly-paid employees, from 1 January 2026 | EUR 5,742 | "€5.742 από 1/1/2026" |
| Maximum insurable earnings, weekly-paid employees, from 5 January 2026 | EUR 1,325 | "€1.325 από 5/1/2026" |

GHS (General Healthcare System) contributions:

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| GHS the employer withholds from employees' emoluments (tax year 2026 form) | 2.65% | "you must withhold 2.65% G.H.S." |
| Annual income above which GHS withholding stops | EUR 180,000 | "exceeds the amount of €180.000, stop withholding" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf |
| GHS rate on self-employed income (2025 return guide; no 2026 page found) | 4% | "for all income and periods throughout the year except for self- employed taxpayers" |

- **GHS on other income**: the 2025 return guide charges GHS on all income at the employee rate in the TD59A table except self-employed income, and only on income up to the annual cap in that table, with incomes added together in a set order. No 2026 page restates this; confirm with the reviewer.
- **Self-employed Social Insurance basis**: contributions are paid on insurable income. The minimum insurable income per occupational category is set by Social Insurance Services and was not found on any readable allowed page. Do not assert a self-employed Social Insurance amount; use the `cyprus-social-contributions` Guide and refer.
- **Employer GHS share and the Central Holiday Fund**: no readable allowed page prints the 2026 rates. See the `cyprus-payroll` Guide and refer.

### 5.6 Deductions (TD59A, the one-fifth cap and the new 2026 personal deductions)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| Flat expenses deduction for let buildings, as a share of gross rents of buildings only | 20% | "twenty per cent (20%) of the gross rents of building only is allowed as a deduction" |
| Life and disability insurance premiums: limit as a share of the capital sum insured | 7% | "must not exceed 7% of the capital sum insured" |
| Medical fund contributions: limit as a share of gross income | 2% | "maximum 2% of gross income per circular 3/30.5.24" |
| Home insurance for natural disasters: cap per tax year | EUR 500 | "Home Insurance for natural disasters (up to €500)" |
| Housing deduction: rent of the main residence or interest on a serviced main-residence loan, per spouse, civil partner or single person | EUR 2,000 | "a deduction of a) up to €2.000, under conditions, is granted to each spouse, civil partner or single person for interest on a serviced housing loan" |
| Green deduction: energy upgrade of the main residence or an electric vehicle, per spouse, civil partner or single person | EUR 1,000 | "b) up to €1.000, under conditions, to each spouse or civil partner or single person for capital expenditure" |
| Optional special rate for AIF carried interest and UCITS performance fees | 8% | "special tax rate of 8% with a minimum tax of €10.000 for AIF carried interest" |
| Minimum tax under that special rate | EUR 10,000 | "special tax rate of 8% with a minimum tax of €10.000 for AIF carried interest" |

**The one-fifth cap.** The total of the year's contributions for life insurance, approved medical funds, GHS, pension schemes, pension and provident funds and Social Insurance must not exceed one fifth of taxable income, measured as one fifth of the intermediary calculation (line B6 of form TD59A). Line B6 is income less union subscriptions, the first-employment exemption, home insurance, rental deductions and other deductions. Life and disability premiums from 1 January 2026 count inside the cap and are each limited to the share of the sum insured in the table above. The home insurance deduction reduces the income on which the cap is measured and does not count inside the cap.

**New personal deductions from 2026** (FAQs, https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf |
| First dependent child, per parent | EUR 1,000 | "€1.000 για το πρώτο εξαρτώμενο τέκνο, • €1.250 για το δεύτερο" |
| Second dependent child | EUR 1,250 | "€1.250 για το δεύτερο εξαρτώμενο τέκνο, • €1.500 για το τρίτο" |
| Third and each further dependent child | EUR 1,500 | "€1.500 για το τρίτο και κάθε επιπρόσθετο εξαρτώμενο τέκνο" |
| Family income ceiling: no children, or one or two children | EUR 100,000 | "€100.000 για οικογένειες χωρίς τέκνα ή με ένα (1) ή δύο (2) τέκνα" |
| Family income ceiling: three or four children | EUR 150,000 | "€150.000 για οικογένειες με τρία (3) ή τέσσερα (4) τέκνα" |
| Family income ceiling: five or more children | EUR 200,000 | "€200.000 για οικογένειες με πέντε (5) ή περισσότερα τέκνα" |
| Single person's income ceiling | EUR 40,000 | "το συνολικό του μεικτό εισόδημα δεν υπερβαίνει τις €40.000" |

Rules for these deductions, all from the FAQs above:
- They cover dependent children, rent or serviced housing-loan interest for the main residence in Cyprus, and capital spending on an energy upgrade of the main residence or an electric vehicle.
- They depend on the income criteria. The total GROSS family income (all members, all sources in Cyprus or abroad) must NOT EXCEED the ceiling for the family's number of children. It is a cliff: one euro over the ceiling and the deduction is lost in full, not tapered. Income of children in full-time education from work, child benefit and student grants are left out of family income.
- Spouses, civil partners, and partners without a civil partnership who have children together must each consent, in their own return, to share their tax data so the family income can be checked. The returns of both (or of the single person) must be filed on time. A late return loses the deductions.
- The child amounts are doubled for single-parent families (TD59A note 12).
- Housing: the cap in the TD59A table applies to interest and rent TOGETHER in a year, not to each. If the amount paid is lower, the actual amount is given. A restructured loan counts as serviced if instalments are paid without fail up to 31 December of the tax year.
- These deductions are given ON TOP of the one-fifth cap: they do not reduce the income on which the cap is measured and do not count inside it.
- Employees claim them on form TD59A through the employer, stating only the final amount per category, and again in the 2026 return.

### 5.7 Exemptions for people taking up work in Cyprus

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf |
| Article 8(21B) exemption on Cyprus employment remuneration or Cyprus business profits | 25% | "can claim an income tax exemption of 25% on- a. his/her remuneration" |
| Gross earnings that must be exceeded in the year (and in the first 12 months) | EUR 30,000 | "has gross earnings exceeding €30.000 in the relevant year" |
| Maximum exemption per tax year | EUR 25,000 | "The exemption cannot exceed €25.000 in a tax year" |

**Article 8(21B), 25% (new; employment or self-employment started from 1 January 2025 to 31 December 2030).** A Cyprus tax resident who meets ALL of these conditions: (a) was NOT Cyprus tax resident in the seven years before the year the Cyprus employment or business began (2019 to 2025); AND (b) WAS Cyprus tax resident in some year before those seven years; AND (c) earned more than the earnings figure in the table above in the first 12 months; AND (d) began the employment or self-employment in the window above; AND (e) at the start either holds a university degree recognised in Cyprus and worked full time abroad for a foreign employer for at least 36 of the 84 months before, OR worked full time abroad for a foreign employer for at least 84 months. It is granted for seven consecutive tax years starting with the year of commencement, but only in a year when Cyprus earnings exceed the earnings figure (a cliff: at or below it, no exemption that year) and the person is Cyprus tax resident (except the first year). The exemption is capped per year at the maximum in the table above. Source: https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf

**Articles 8(23) and 8(23A), 50%.** The minimum pay figures are in the TD59A table below. Conditions from the Tax Department's explanatory table https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf
- 8(23A) as enacted by Law 121(I)/2022, for employment started from 1 January 2022 to 29 June 2023 only: 50% of remuneration from the FIRST employment in Cyprus, where remuneration exceeds the 8(23A) minimum in the TD59A table below, for 17 years or until that first employment ends, whichever is earlier. The person must not have been Cyprus tax resident for at least 10 years before the year the first employment began.
- 8(23A) as amended by Law 51(I)/2023, available for employment started from 1 January 2022 and the ONLY limb for employment started on or after 30 June 2023 (so every 2024, 2025 and 2026 starter): 50% of remuneration from employment in Cyprus, where remuneration exceeds the same minimum, for 17 years. Here "first employment in Cyprus" means starting Cyprus employment, with a resident or a non-resident employer, after 15 consecutive tax years with no employment in Cyprus, and the person must not have been Cyprus tax resident for at least 15 years before the year that employment began. A person who qualified under the 2022 wording before Law 51(I)/2023 keeps the exemption on the old conditions (table note 3).
- Old 8(23), employment started 1 January 2012 to 25 July 2022: 50% of remuneration from any employment in Cyprus, where remuneration exceeds the old minimum in the TD59A table below, for 10 years, for a person not resident in 3 of the last 5 years. Transitional rules move some 2016 to 2021 starters into 8(23A); refer those cases.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf |
| First employment: exemption as a share of emoluments | 20% | "20% of your emoluments from any employment with a maximum of €8.550" |
| Maximum 20% exemption per tax year | EUR 8,550 | "20% of your emoluments from any employment with a maximum of €8.550" |
| Old 50% exemption (circular 2017/4): salary must exceed | EUR 100,000 | "your salary exceeds €100.000 in the tax year according to circular 2017/4" |
| 50% exemption under circulars 2022/10 and 2024/04: salary must exceed | EUR 55,000 | "your salary exceeds €55.000 in the tax year according to circular 2022/10" |
| 50% exemption, as a share of emoluments | 50% | "50% of your emoluments from any employment provided that your salary exceeds €55.000" |

**Articles 8(21) and 8(21A), 20%.** Conditions from the Tax Department's explanatory table https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf
- 8(21A), employment starting between 26 July 2022 and 31 December 2027: for a person who, for the 3 consecutive years immediately before the first employment in Cyprus, was employed OUTSIDE Cyprus by an employer NOT resident in Cyprus. 20% of remuneration from the first employment, capped per year as in the table above, no minimum pay, for 7 years starting from the year AFTER the year the first employment began, or until that first employment ends, whichever is earlier.
- Old 8(21), employment up to 25 July 2022: for a person not resident in the year before employment began; any employment; 5 years from the year after commencement.
- Both are granted whether or not the person becomes Cyprus tax resident after starting work.

**Only one first-employment exemption per claim.** Form TD59A lets an employee deduct "either" the 20% exemption "or" one of the two 50% exemptions. No saved page states how 8(21B) interacts with the others; refer any person who may qualify for two.

### 5.8 Special Defence Contribution (SDC)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf |
| SDC on dividends received by individuals, for dividends out of profits of 2026 onward | 5% | "Άτομα σε ποσοστό 5% (μείωση από το 17%)" |
| SDC on a dividend paid out of profits of 2025 or earlier, even if received later | 17% | "σε ποσοστό 17% επί του (α) και ➢ σε ποσοστό 5% επί του (β)" |
| SDC on interest received or credited | 17% | "αναφορικά με τόκο που λαμβάνει ή πιστώνεται, σε 17%" |
| Reduced SDC on interest from government savings certificates and development bonds, and listed corporate or public-body bonds | 3% | "σε ποσοστό τρία τοις εκατό (3%)" |

- **Who pays**: only individuals who are Cyprus tax resident AND domiciled in Cyprus. A non-domiciled resident, or a non-resident, pays no SDC on dividends, interest or rent. Source: https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/
- **Deemed domicile**: whatever the domicile of origin, a person resident in Cyprus for at least 17 out of the last 20 years immediately before the tax year is treated as domiciled for SDC. A person with a Cypriot domicile of origin can be non-domiciled only under the narrow exceptions on the same page. Use the `cy-non-dom` Guide.
- **Rent**: SDC on rental income was charged up to and including tax year 2025 and is abolished from 1 January 2026. Do not charge SDC on 2026 rents.
- **Which dividend rate**: the rate follows the year of the PROFITS the dividend is paid from, not the year it is received. A 2027 dividend out of 2025 profits bears the older rate in the table above.
- **Deposit interest refund (2025 rule; confirm for 2026)**: the 2025 return guide refunds SDC withheld on deposit interest where total income including the interest does not exceed the amount in the table below. The guide does not print the refund formula, and no 2026 page restates the rule. Refer before relying on it.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf |
| Total income ceiling for the SDC refund on deposit interest (tax year 2025 guide) | EUR 12,000 | "does not exceed €12.000. Column 1 T.I.C." |

### 5.9 Non-Deductible Expenses

| Expense | Reason |
| --- | --- |
| Entertainment and private meals | Not wholly-and-exclusively business |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Relieved via capital allowances, not as an expense |
| Drawings and personal withdrawals | Not an expense |

### 5.10 VAT Interaction

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/ |
| Standard VAT rate | 19% | "Κανονικός συντελεστής (19%)" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/ |
| Compulsory registration: taxable supplies in the 12 months to the end of any month have exceeded | EUR 15,600 | "έχει υπερβεί τις €15.600" |

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income; exclude from gross |
| Input VAT recovered (registered) | NOT an expense; exclude from costs |
| Input VAT blocked or non-deductible | IS a cost; include in the expense |
| Not VAT-registered (below the registration threshold) | All VAT paid on purchases is a cost (gross) |
| Foreign VAT (non-reclaimable) | IS a cost; full gross |

### 5.11 Provisional (Temporary) Tax

Source: the Tax Department deadline calendar https://www.gov.cy/mof-tax/prothesmies/ and the FAQs https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf

| Item | Detail |
| --- | --- |
| Who | Individuals with income other than employment (self-employment, rent and other sources); also employees with income from other sources. Employees with only PAYE income do not pay provisional tax |
| Instalments | Provisional tax computation submitted and the first of two instalments paid by 31 July, the second by 31 December, of the tax year itself |
| Form | Temporary declaration code 0200 through the Tax portal by the end of July (TD59A note 3) |
| Income starting after 30 June (from 2026) | A person who starts earning non-employment income after 30 June files the provisional tax declaration and pays ONE instalment by 31 December of that year (Law 243(I)/2025; collection presentation in Section 5.12) |
| Final balance | Paid by self-assessment by the return deadline in Section 5.12 |
| Underestimation | The additional tax for underestimating provisional tax is not printed on any saved page; refer |

Trap: the official calendar labels the July and December 2026 provisional tax rows "for 2025". Read them as the 2026 instalments only after checking with the reviewer.

### 5.12 Filing Duty, Deadlines, Accounts and Interest

**Who must file from tax year 2026.** A return is required from (a) any person with gross income (before any exemption or deduction) within article 5 of the Income Tax Law: business, employment, dividends, interest, pension, rents, royalties, property, sale of crypto-assets and similar; OR (b) any Cyprus tax resident who, by 31 December of the tax year, has completed their 25th year of age but not their 71st, whatever their income, even with no income. A resident with no gross income who is under 25 or has completed their 71st year by 31 December does not have to file. A non-resident files if they have income arising in Cyprus. The old income threshold for filing (the tax-free amount up to 2025) no longer applies. The Council of Ministers may exempt categories by decree. Sources: https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf and https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%9D%CF%8C%CE%BC%CE%BF%CE%B9-%CE%A0%CE%92%CE%95-%CE%95%CE%B9%CF%83%CF%80%CF%81%CE%AC%CE%BE%CE%B5%CF%89%CF%82-%CE%A7%CE%B1%CF%81%CF%84%CE%BF%CF%83%CE%AE%CE%BC%CF%89%CE%BD.pdf |
| Turnover up to which an individual in business need not prepare accounts, from tax year 2026 | EUR 120,000 | "από €70.000 σε €120.000 για την υποχρέωση ετοιμασίας λογαριασμών από φυσικά πρόσωπα" |
| Turnover threshold up to tax year 2025 (not for 2026) | EUR 70,000 | "από €70.000 σε €120.000 για την υποχρέωση ετοιμασίας λογαριασμών από φυσικά πρόσωπα" |
| Reviewed (not audited) accounts band: turnover from EUR 120,001 and below EUR 200,000 (the page prints "<"; edge unconfirmed) | EUR 200,000 | "€120.001 < €200.000 και €500.000 Επισκόπηση λογαριασμών" |
| Reviewed accounts band: total assets up to | EUR 500,000 | "€120.001 < €200.000 και €500.000 Επισκόπηση λογαριασμών" |
| Interest rate on overdue tax from 1 January 2026 | 3.5% | "(από 1/1/2026 είναι 3,5%)" |

**Accounts.** From tax year 2026 an individual in business whose turnover does not exceed (or for at least two consecutive years ceases to exceed) the first figure above need not prepare accounts. Above it, reviewed accounts are allowed within the turnover and total-assets limits above; otherwise audited accounts are required. The presentation's table is garbled in the saved copy; confirm the exact band edges with the reviewer.

**Deadlines** (Assessment and Collection of Taxes Law article 5(1A) as amended; collection presentation above; FAQs):

| Who | Return and self-assessment payment for tax year 2026 |
| --- | --- |
| Individuals not required to prepare reviewed or audited accounts (employees, pensioners, landlords, smaller self-employed) | 31 July 2027 (FAQs: "Η προθεσμία υποβολής είναι μέχρι την 31η Ιουλίου 2027") |
| Individuals required to prepare reviewed or audited accounts | 31 January of the second year after the tax year (for tax year 2026, 31 January 2028), replacing 31 March of that year |
| Employers' annual return of employees | 31 March of the year after the tax year, with no three-month extension |

- **Interest**: from tax year 2026, interest on tax due after an assessment runs from 1 August of the year after the tax year for individuals without accounts, and from 1 February of the second year for those with accounts. The rate is in the table above. If the Tax Department extends the filing deadline by public announcement, interest runs from the end of the extended deadline, and a return and self-assessment filed within the extension carry no late-filing or late-payment charge.
- **Late filing and late payment charges**: the 2026 amounts appear only as an image in the official presentation and are not readable. Refer; do not quote an amount.
- **Records**: keep documents supporting the return for 6 years from the later of the filing deadline and the actual filing date; a revised return restarts the period.

## Section 6: Edge Cases

### 6.1 Home Office Deduction

**Legislation:** Income Tax Law N.118(I)/2002.

- Calculate the proportion of the home used for business (dedicated rooms as a share of total rooms or floor area).
- Apply that share to rent or mortgage interest, electricity, water, internet, maintenance.
- Must be a genuinely dedicated workspace; a dual-use room does NOT qualify.

**Conservative default:** no deduction until the reviewer confirms the room arrangement.
**Flag for reviewer:** confirm room count, floor-area basis, and dedicated use.

### 6.2 Motor Vehicle Business Use

- Only the business-use share of fuel, insurance, maintenance and capital allowance is deductible.
- Client must keep a mileage log (business and total).

**Conservative default:** no business use until a mileage log is provided.
**Flag for reviewer:** confirm the business share is documented and reasonable, and confirm the wear-and-tear rate (see the 5.4 research gap).

### 6.3 Phone and Internet Mixed Use

- Business-use portion only; client must provide a reasonable estimate.

**Conservative default:** no deduction until the business share is confirmed.

### 6.4 Non-Dom Status and SDC

- Non-dom status removes SDC on dividends and interest (and, up to tax year 2025, on rent), but requires confirmation of domicile of origin and the 17-of-20-year deemed-domicile test.
- **Flag for reviewer:** do NOT assert non-dom status without evidence; the conservative default treats the individual as domiciled (SDC applies). For the optional lump-sum extension for deemed-domiciled people, use the `cy-non-dom` Guide.

### 6.5 Exemption Eligibility

- The 25%, 50% and 20% exemptions have strict prior-residence, prior-employment, date and pay conditions (Section 5.7). Form TD59A allows only one of the 20% and 50% exemptions.
- **Flag for reviewer:** confirm prior-residence history, foreign employment history, the remuneration threshold and the first-employment date.

### 6.6 Foreign Pension Election

- Special rate above the annual threshold, or normal scale; yearly election (Section 5.3).
- **Flag for reviewer:** confirm which election is beneficial.

### 6.7 Bad Debt Write-Off

- Deductible only if (1) income was previously declared, (2) all reasonable recovery steps were taken, (3) the debt is genuinely irrecoverable. [Legacy rule; no saved page states it.]
- **Flag for reviewer** to confirm all three conditions.

### 6.8 Self-Employed Insurable Income Category

- Social Insurance is computed on insurable income for the occupational category.
- **Flag for reviewer:** confirm the occupational category and the official minimum from the Social Insurance Services table.

### 6.9 New Personal Deductions at the Family Income Ceiling

- The ceiling is on gross family income, including the partner's income and foreign income. One euro over and all child, housing and green deductions are lost (Section 5.6).
- **Flag for reviewer:** confirm both partners' gross income, their consent in the return, and that both returns were filed on time.

## Section 7: Working Paper Template

~~~
CYPRUS INCOME TAX: INDIVIDUAL RETURN WORKING PAPER
Tax Year: 2026 (filed through Tax For All)
Client: ___________________________
Residency: Resident (183-day / 60-day) / Non-resident
Domicile: Domiciled / Non-dom
Age at 31 December: ______ (filing duty, Section 5.12)

A. SELF-EMPLOYMENT GROSS INCOME
  A1. Client payments (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)      ___________
  A3. Other business income                         ___________
  A4. TOTAL gross self-employment income            ___________
  (Turnover check: accounts, review or audit, Section 5.12)

B. ALLOWABLE BUSINESS DEDUCTIONS
  B1. Office rent                                   ___________
  B2. Professional insurance                        ___________
  B3. Accountancy / legal fees                      ___________
  B4. Office supplies / stationery                  ___________
  B5. Software subscriptions                        ___________
  B6. Marketing / advertising                       ___________
  B7. Bank charges / payment processing fees        ___________
  B8. Training / professional subs                  ___________
  B9. Travel (flights, hotels, transport)           ___________
  B10. Telecoms (business share of phone/internet)  ___________
  B11. Home office (share of utilities/rent)        ___________
  B12. Vehicle expenses (business share)            ___________
  B13. Capital allowances (wear and tear)           ___________
  B14. Other allowable expenses                     ___________
  B15. TOTAL business deductions                    ___________

C. NET PROFIT (A4 - B15)                            ___________

D. OTHER INCOME
  D1. Employment income (PAYE emoluments)           ___________
  D2. Rental income less flat buildings deduction,
      capital allowances and interest               ___________
  D3. Foreign pension (if normal scale elected)     ___________
  D4. TOTAL other taxable income                    ___________
  (Dividends and interest: not taxable for income tax; SDC and GHS only)
  (Crypto gains, share option benefits, foreign pension in special mode:
   taxed separately at their special rates, Section 5.3)

E. EXEMPTIONS AND FIRST DEDUCTIONS
  E1. Exemption 8(21B) / 8(23A) / 8(21A) (one only)  ___________
  E2. Union and professional subscriptions          ___________
  E3. Home insurance (natural disasters, capped)    ___________
  E4. Other deductions                              ___________
  E5. INTERMEDIARY INCOME (C + D4 - E1 to E4)       ___________

F. ONE-FIFTH CAP
  F1. Social Insurance                              ___________
  F2. GHS                                           ___________
  F3. Life / disability premiums (capped per policy)___________
  F4. Pension, provident and medical funds          ___________
  F5. SUBTOTAL (F1 to F4)                           ___________
  F6. Cap = E5 / 5                                  ___________
  F7. Allowed = MIN(F5, F6)                         ___________

G. NEW PERSONAL DEDUCTIONS (outside the cap; income criteria)
  G1. Dependent children                            ___________
  G2. Rent or housing-loan interest (one cap)       ___________
  G3. Energy upgrade / electric vehicle             ___________
  G4. TOTAL (0 if family income over the ceiling)   ___________

H. CHARGEABLE INCOME (E5 - F7 - G4)                  ___________

I. TAX (2026 scale, Section 1)
  I1. Tax on chargeable income                      ___________
  I2. Special-rate taxes (Section 5.3)              ___________
  I3. Less: PAYE withheld                           ___________
  I4. Less: provisional tax paid                    ___________
  I5. Less: foreign tax credit (if any)             ___________
  I6. Tax due / refund                              ___________

J. SDC (only if resident AND domiciled)
  J1. Dividends from 2026+ profits                  ___________
  J2. Dividends from 2025-or-earlier profits        ___________
  J3. Interest (general rate or reduced bond rate)  ___________
  J4. Rent: none from 2026

REVIEWER FLAGS:
  [ ] Residency confirmed (183-day / 60-day)?
  [ ] Domicile / non-dom status confirmed?
  [ ] Filing duty confirmed (income or age)?
  [ ] Accounts / review / audit position confirmed (turnover)?
  [ ] VAT registration status confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business share confirmed with mileage log?
  [ ] One-fifth cap applied correctly?
  [ ] Family income criteria and partner consent confirmed?
  [ ] Capital allowance rates confirmed (RESEARCH GAP)?
  [ ] Self-employed insurable income category confirmed?
  [ ] Exemption eligibility confirmed?
  [ ] Tax year 2026 scale used (not 2025)?
~~~

### Cyprus Bank Statement Formats

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Cyprus | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; Greek and English; description has counterparty and reference |
| Hellenic Bank | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| Eurobank Cyprus | PDF | Date, Particulars, Withdrawals, Deposits | Private and business |
| Astrobank | PDF | Date, Description, Amount, Balance | Mixed-language descriptions |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency possible |
| Wise Business | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency; conversion fees on a separate line |

### Key Cypriot and Greek Banking Terms

| Term (Greek or transliterated) | English | Classification Hint |
| --- | --- | --- |
| METAFORA / EMBASMA | Transfer or remittance | Check direction for income or expense |
| AMESI CHREOSI / DD | Direct debit | Regular expense (utility, subscription) |
| PAGIA ENTOLI / SO | Standing order | Regular expense (rent, loan) |
| KARTA / CARD | Card payment | Expense; check merchant |
| KATATHESI / DEPOSIT | Deposit | Potential income |
| SPEXODA / CHARGES | Bank charges | Deductible business expense |
| TOKOS / INTERESSI | Interest | Interest income (not taxable for income tax; SDC if domiciled) or bank charge |
| MISTHOS | Salary | Employment income (PAYE) |
| ENOIKIO | Rent | Rental income or office-rent expense |
| FPA | VAT | VAT liability or credit; exclude from income and expense |

## Section 9: Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING: reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

~~~
ONBOARDING QUESTIONS (CYPRUS INCOME TAX):
1. Residency: were you in Cyprus more than 183 days in 2026?
   If not, do you meet the 60-day rule (at least 60 days, not more than 183 days
   in any other single country, Cyprus business, job or directorship held to
   31 December, and a Cyprus home)?
2. Domicile: are you Cyprus-domiciled, or do you claim non-dom status?
3. Age at 31 December 2026 (filing duty)?
4. Employment status: employee under PAYE, self-employed, or both?
5. Business turnover and total assets (accounts, review or audit)?
6. VAT registration: did taxable supplies pass the registration threshold?
7. Occupational category (self-employed Social Insurance)?
8. Home office: dedicated room or shared space? If dedicated, what share of floor area?
9. Vehicle: business use share, and do you keep a mileage log?
10. Phone and internet: business use share?
11. Social Insurance and GHS: total amounts paid in the tax year?
12. Provisional (temporary) tax: total amount paid in the tax year?
13. Other income: employment, rental, dividends (from which year's profits), interest,
    foreign pension, crypto, share options?
14. Family: dependent children, gross income of spouse or partner, rent or
    housing-loan interest, energy upgrade or electric vehicle spending?
15. When and how did you start work in Cyprus (25%, 50% or 20% exemption)?
~~~

### Key Legislation and Authority References

| Topic | Reference |
| --- | --- |
| Income tax rates, exemptions and deductions | Income Tax Law N.118(I)/2002, as amended (Law 244(I)/2025 from 1 January 2026) |
| Special Defence Contribution | Special Defence Contribution Law N.117(I)/2002, as amended |
| Returns, deadlines, accounts, interest, penalties | Assessment and Collection of Taxes Law, as amended (Law 243(I)/2025) |
| Tax authority | Cyprus Tax Department (Τμήμα Φορολογίας), Ministry of Finance |
| Social insurance authority | Social Insurance Services, Ministry of Labour and Social Insurance |
| Filing portal | Tax For All (TFA) from tax year 2026 |

### Key Thresholds (each carries a source)

Every threshold sits in the sourced table of its section. This index points to them.

| Threshold | Where |
| --- | --- |
| Tax-free amount and bands | Section 1, FAQs table |
| Residency: 183-day and 60-day rules | Section 5.2 |
| Deemed domicile for SDC | Section 5.8 |
| Social Insurance maximum insurable earnings | Section 5.5, Social Insurance Services table |
| GHS annual income cap | Section 5.5, TD59A table |
| Family and single income ceilings for the new personal deductions | Section 5.6, FAQs table |
| Exemption pay thresholds | Section 5.7 |
| VAT compulsory registration | Section 5.10 |
| Accounts, review and audit turnover thresholds | Section 5.12 |

### 2026 New Deductions (apply only from tax year 2026)

The child, housing and green deductions (with income criteria), the home insurance deduction, the disability insurance deduction and the cultural donations deduction are set out with their limits in Sections 5.3 and 5.6.

### Cited Sources

All sources are listed under "Sources" at the end of this Guide. Every source is an official Cyprus government page.

### Test Suite

Amounts in these tests are hypothetical unless stated.

- Test A (ordinary): resident, chargeable income as in Example 5 (tax year 2026). Expected: the tax in the Example 5 table.
- Test B (boundary): chargeable income equal to the top of the 0% band in Section 1. Expected: no tax. One euro more is taxed at the 20% band rate.
- Test C (exclusion): resident but non-domiciled; dividends only. Expected: no income tax (dividends are not taxable for income tax) and no SDC (non-dom). GHS may still apply (Section 5.5).
- Test D (special mode): foreign pension as in Example 6, special mode elected. Expected: the tax in the Example 6 table.
- Test E (cap): a person who meets every article 8(21B) condition and whose 25% exemption would exceed the yearly maximum in Section 5.7. Expected: the exemption is limited to that maximum.
- Test F (cliff): family with two children and gross family income one euro above the ceiling for that family size. Expected: no child, housing or green deduction at all.
- Test G (rent): resident domiciled landlord, 2026 rents. Expected: income tax at the scale after the flat buildings deduction; GHS; no SDC.

## The method, step by step

1. **Confirm the year and the law.** Tax year 2026 follows Income Tax Law N.118(I)/2002 as amended by Law 244(I)/2025, in force from 1 January 2026 (FAQs: https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf).
2. **Decide residency** under the 183-day or 60-day rule, and domicile for SDC (Tax Department page: https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/).
3. **Decide the filing duty** from income and age (Assessment and Collection of Taxes Law article 5, Tax Department return page: https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/).
4. **Classify the year's income** (Section 3 and Section 5.3). Separate income taxed at special rates (crypto, share options, AIF carried interest, foreign pension in special mode) and income not taxable (dividends, interest), using the TD59A form notes (https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf).
5. **Compute self-employed profit** and check turnover against the accounts thresholds (collection presentation, Section 5.12).
6. **Apply exemptions** (Section 5.7): 8(21B), 8(23A) or 8(21A), one first-employment exemption only (form TD59A note 7).
7. **Apply deductions in the TD59A order** (https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf): subscriptions, home insurance, rental deductions, other deductions, then the one-fifth cap on contributions and premiums, then the new personal deductions if the family income criteria are met (FAQs).
8. **Apply the 2026 scale** to chargeable income (Section 1), and add the special-rate taxes.
9. **Compute SDC** for resident domiciled individuals on dividends and interest only (SDC presentation: https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf), and GHS on income not already withheld (TD59A).
10. **Credit PAYE and provisional tax**, then file through Tax For All by the deadline in Section 5.12 and pay the self-assessment (deadline calendar: https://www.gov.cy/mof-tax/prothesmies/).

## Ask the client first

- How many days were you in Cyprus in 2026, how many in any other single country, and did you have a Cyprus business, job or directorship and a Cyprus home until 31 December? (Residency, Section 5.2.)
- Where were you born and where is your permanent home, and in how many of the last 20 years were you Cyprus tax resident? (Domicile and SDC, Section 5.8.)
- When did you start your current job or business in Cyprus, where did you live and work in the years before, and what is your annual pay? (Exemptions, Section 5.7.)
- What was the gross income of everyone in your family for 2026, how many dependent children do you have, and will your spouse or partner consent in their return? (New personal deductions, Section 5.6.)
- What was your business turnover and total assets? (Accounts and the deadline, Section 5.12.)
- Did you have crypto disposals, share options, foreign pensions, dividends from pre-2026 profits, or rental income? (Special rates and SDC, Sections 5.3 and 5.8.)

## When to refuse or refer

- Residency or domicile cannot be confirmed (R-CY-1, R-CY-7).
- Companies, partnerships, capital gains on Cyprus property, non-resident or treaty cases (R-CY-2 to R-CY-4).
- Arrears, enforcement, or a request to estimate late filing or late payment charges: the 2026 amounts are not readable on any allowed page (R-CY-5).
- Underestimation of provisional tax: the additional tax rule is not printed on any saved page.
- Anyone who may qualify for two exemptions, or who started work in Cyprus between 2016 and 2021 (transitional 8(23A) rules).
- Crypto-asset gains, approved share option plans, AIF carried interest (R-CY-8).
- Share or other title disposals (article 8(22) not printed on any saved page).
- Self-employed Social Insurance amounts and capital allowance rates (research gaps).
- Family income near a deduction ceiling, or a partner who will not consent.

## PROHIBITIONS

- NEVER apply the Cyprus scale without first confirming tax residency
- NEVER assert non-dom status (and the SDC exemption) without evidence; default to domiciled
- NEVER apply the 2026 scale or deductions to tax year 2025 income, or the 2025 scale to 2026
- NEVER treat dividends or interest as taxable for income tax; they bear SDC (if domiciled) and GHS only
- NEVER charge SDC on rent for tax year 2026
- NEVER assert a self-employed Social Insurance figure without the official occupational-category table
- NEVER assert a capital-allowance rate; it is a research gap until confirmed
- NEVER allow entertainment or private expenses as deductions by default
- NEVER allow income tax itself, fines or penalties as a deduction
- NEVER include VAT collected on sales in business income for a VAT-registered person
- NEVER exceed the one-fifth cap on contributions and premiums
- NEVER grant the child, housing or green deductions without checking gross family income against the ceiling
- NEVER present tax calculations as definitive; label them as estimates pending reviewer sign-off

## Sources

- Tax Department, Tax Reform 2026 hub: https://www.gov.cy/mof-tax/en/documents/forologiki-metarrythmisi-2026/
- FAQs for individuals, version 11 May 2026: https://www.gov.cy/media/sites/167/2026/05/FAQs-110526.pdf
- Form TD59A 2026 (English): https://www.gov.cy/media/sites/167/2026/02/IR59_2026_English__.pdf
- Individual Income Tax Return page: https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/
- Tax Residency and Domicile page: https://www.gov.cy/mof-tax/en/documents/tax-residency-domicility/
- Presentation, Tax Reform 2026 for individuals (11 May 2026): https://www.gov.cy/media/sites/167/2026/05/%CE%A6%CE%BF%CF%81%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CE%BA%CE%AE-%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-2026-%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AC-%CF%80%CF%81%CF%8C%CF%83%CF%89%CF%80%CE%B1-11.05.2026.pdf
- Presentation, Income Tax Law amendments: https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%A6%CF%8C%CF%81%CE%BF%CF%82-%CE%95%CE%B9%CF%83%CE%BF%CE%B4%CE%AE%CE%BC%CE%B1%CF%84%CE%BF%CF%82.pdf
- Presentation, Assessment and Collection of Taxes Law amendments: https://www.gov.cy/media/sites/167/2026/03/2026-%CE%A6%CE%BF%CF%81%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-%CE%9D%CF%8C%CE%BC%CE%BF%CE%B9-%CE%A0%CE%92%CE%95-%CE%95%CE%B9%CF%83%CF%80%CF%81%CE%AC%CE%BE%CE%B5%CF%89%CF%82-%CE%A7%CE%B1%CF%81%CF%84%CE%BF%CF%83%CE%AE%CE%BC%CF%89%CE%BD.pdf
- Presentation, Special Defence Contribution and Capital Gains: https://www.gov.cy/media/sites/167/2026/03/EEA-%CE%A6%CE%9A%CE%9A-%CE%9C%CE%95%CE%A4%CE%91%CE%A1%CE%A1%CE%A5%CE%98%CE%9C%CE%99%CE%A3%CE%97-06032026.pdf
- Article 8(21B) exemption leaflet: https://www.gov.cy/media/sites/167/2026/06/Article-8-21B-of-the-Income-Tax-Law-N.118-I-2002.pdf
- Explanatory table, articles 8(23) and 8(23A): https://www.gov.cy/media/sites/167/2026/06/%CE%A0%CE%AF%CE%BD%CE%B1%CE%BA%CE%B1%CF%82-%CE%B1%CF%80%CE%B1%CE%BB%CE%BB%CE%B1%CE%B3%CF%8E%CE%BD-823-%CE%BA%CE%B1%CE%B9-823%CE%91.pdf
- Explanatory table, articles 8(21) and 8(21A): https://www.gov.cy/media/sites/167/2026/01/implementation-of-sections-21-and-21A-of-article-8-24072023.pdf
- Return completion guide 2025: https://www.gov.cy/media/sites/167/2026/06/Guide-for-completion-of-tax-return-2025.pdf
- Tax Department deadline calendar: https://www.gov.cy/mof-tax/prothesmies/
- VAT rates: https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/
- VAT registration obligation: https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/
- Social Insurance rates (government business portal): https://www.businessincyprus.gov.cy/social-insurance-registration-and-contributions/
- Social Insurance maximum insurable earnings 2026: https://sisweb.mlsi.gov.cy/anotato2025/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
