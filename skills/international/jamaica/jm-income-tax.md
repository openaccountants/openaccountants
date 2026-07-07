---
name: jamaica-income-tax
description: Use this skill whenever asked about Jamaica personal income tax for self-employed individuals or employees with additional income. Trigger on phrases like "how much tax do I pay in Jamaica", "S04 return", "IT01 return", "chargeable income", "tax-free threshold", "NIS contributions", "NHT contributions", "Education Tax", "HEART levy", "PAYE Jamaica", "self-employed tax Jamaica", "TAJ filing", "statutory deductions Jamaica", or any question about filing or computing income tax for a self-employed person or an employee with other income sources in Jamaica. Also trigger when computing payroll deductions, quarterly estimated tax (S04A), NIS ceiling, NHT contributions, Education Tax, or capital allowances for a Jamaican taxpayer. This skill covers income tax rates and brackets, the tax-free threshold (including the April 2025 mid-year increase), statutory contributions (NIS, NHT, Education Tax, HEART), allowable deductions, capital allowances, filing forms and deadlines, penalties, and GCT registration requirements for small businesses. ALWAYS read this skill before touching any Jamaica income tax work.
jurisdiction: JM
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# jamaica-income-tax

## Section 1 -- Quick Reference

**Section 1 Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Jamaica |
| Tax | Personal Income Tax (PIT) |
| Currency | JMD (Jamaican Dollars) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (Jamaica) |
| Supporting legislation | National Insurance Scheme Act; National Housing Trust Act; Education Tax Act; HEART Trust/NSTA Act; Tax Administration Jamaica Act |
| Tax authority | Tax Administration Jamaica (TAJ) |
| Filing portal | TAJ e-Portal — https://www.jamaicatax.gov.jm |
| Filing deadline (self-employed annual) | 15 March of the following year (S04) |
| Quarterly estimated tax deadline | 15 March, 15 June, 15 September, 15 December (S04A) |
| Validated by | Pending — requires sign-off by a qualified Jamaican tax practitioner or CPA |
| Validation date | Pending |
| Skill version | 0.1 |

### Income Tax Rate Brackets (2025)

**Income Tax Rate Brackets (2025)**  _(Source: PwC Worldwide Tax Summaries — Jamaica Individual (reviewed 31 Dec 2025); https://taxsummaries.pwc.com/jamaica/individual/taxes-on-personal-income)_

| Band | Annual Chargeable Income Above Threshold | Rate |
| --- | --- | --- |
| Lower band | Up to JMD 6,000,000 | 25% |
| Higher band | Above JMD 6,000,000 | 30% |

- **Non-residents tax rate** — Non-residents: taxed at a flat 25% from the first dollar, with no tax-free threshold available.  _(Source: PwC Jamaica Individual.)_
- **Basis of taxation** — Residents (domiciled in Jamaica) are taxed on worldwide income. Non-residents are taxed on Jamaica-source income only.  _(Source: PwC Jamaica Individual.)_

Jamaica uses a two-band progressive structure applied to chargeable income ABOVE the tax-free threshold. The threshold itself is tax-free.

### Tax-Free Threshold (2025) — Mid-Year Adjusted

**Tax-Free Threshold (2025) table**  _(Source: Orbitax citing TAJ Technical Advisory #042025/01/IT-TA; https://orbitax.com/news/country/article/Jamaica-Explains-Increase-in-A-59152. Official advisory PDF: https://www.jamaicatax.gov.jm/documents/10194/52231399/Technical_Advisory_Threshold+_042025.pdf/c4adbf81-8ddd-9a1b-9e8b-8bdc431162df)_

| Period | Annual Threshold | Monthly Equivalent | Weekly Equivalent |
| --- | --- | --- | --- |
| 1 Jan 2025 -- 31 Mar 2025 | JMD 1,700,088 | JMD 141,674 | JMD 32,694 |
| 1 Apr 2025 -- 31 Dec 2025 | JMD 1,799,376 | JMD 149,948 | JMD 34,603 |
| **Full-year 2025 blended effective threshold** | **JMD 1,774,554** | -- | -- |

- **Blended threshold derivation** — (3/12 x JMD 1,700,088) + (9/12 x JMD 1,799,376) = JMD 425,022 + JMD 1,349,532 = JMD 1,774,554  _(Source: Orbitax citing TAJ Technical Advisory #042025/01/IT-TA)_

**Upcoming confirmed increases (2025/26 budget)**  _(Source: JIS; https://jis.gov.jm/increase-in-income-tax-threshold-now-in-effect/)_

| Effective Date | Annual Threshold | Full-Year Blended |
| --- | --- | --- |
| 1 Apr 2026 | JMD 1,902,360 | JMD 1,876,614 |
| 1 Apr 2027 | JMD 2,003,496 | [RESEARCH GAP — reviewer to confirm blended] |

### Additional Exemptions on Top of the Threshold

**Additional Exemptions table**  _(Source: JIS; https://jis.gov.jm/increase-in-income-tax-threshold-now-in-effect/ and https://jis.gov.jm/taj-develops-technical-advisory-for-revised-income-tax-threshold-and-pension-exemptions/)_

| Category | Additional Annual Exemption |
| --- | --- |
| Pensioner (from approved superannuation scheme, any age) | JMD 250,040 |
| Golden Ager (aged 65 or over) | JMD 250,040 |
| Pensioner AND aged 65+ (both) | JMD 500,080 combined additional |

Example for 2025: a pensioner aged 65+ has total tax-free income = JMD 1,774,554 + JMD 500,080 = JMD 2,274,634.

### Statutory Contribution Rates — 2025

**A. National Insurance Scheme (NIS)**  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes. Ceiling raised to JMD 5,000,000 by Cabinet in 2022; remained at JMD 5,000,000 through 2025.)_

| Contributor | Rate | Annual Insurable Earnings Ceiling | Maximum Annual Contribution |
| --- | --- | --- | --- |
| Employee | 3% | JMD 5,000,000 | JMD 150,000 |
| Employer | 3% | JMD 5,000,000 | JMD 150,000 |
| Self-employed | 6% | JMD 5,000,000 | JMD 300,000 |

- **NIS deductibility** — NIS contributions are income-tax deductible for the contributor.  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes)_

**B. National Housing Trust (NHT)**  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes. NHT official site: https://www.nht.gov.jm/self-employed-contributions)_

| Contributor | Rate | Annual Earnings Ceiling |
| --- | --- | --- |
| Employee | 2% | None — all gross emoluments |
| Employer | 3% | None — all gross emoluments |
| Self-employed | 3% | None — applied to net statutory income after allowable expenses |

- **NHT refund rule** — Employee contributions accumulate in an individual account and are refundable after 7 years of contributions (or at age 65) if no mortgage is drawn. Employer contributions are non-refundable. Expatriates may claim a refund of employee NHT on permanent departure.  _(NHT official site: https://www.nht.gov.jm/self-employed-contributions)_

**C. Education Tax**  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes. Dawgen Global compliance guide: https://www.dawgen.global/payroll-and-statutory-deductions-paye-nis-nht-education-tax-and-heart-every-employers-complete-compliance-guide/)_

| Contributor | Rate | Annual Earnings Ceiling |
| --- | --- | --- |
| Employee | 2.25% | None |
| Employer | 3.5% | None |
| Self-employed | 2.25% | None |

- **Education Tax base and no threshold exemption** — Calculated on statutory income AFTER deduction of NIS contributions (and approved superannuation). There is NO earnings ceiling. Education Tax has NO threshold exemption — employees who fall below the income tax threshold still pay Education Tax on ALL earnings. This is a frequent compliance error.  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes)_

**D. HEART Trust/NSTA Levy**  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes)_

| Contributor | Rate | Applies When |
| --- | --- | --- |
| Employee | 0% (none) | n/a |
| Employer | 3% | Employer has 3 or more employees |

- **HEART levy application** — Employer-only levy on total gross payroll. No earnings ceiling. Tax-deductible for the employer. Applies from the first dollar of payroll once the employer has 3 or more employees. Note: one secondary source cited a monthly payroll threshold of approximately JMD 292,300 (2026 figure) in addition to the employee-count test — [RESEARCH GAP — reviewer to confirm from current HEART Trust/NSTA Act].  _(Source: PwC Jamaica Other Taxes; https://taxsummaries.pwc.com/jamaica/individual/other-taxes)_

### Summary: Total Statutory Contribution Rates (2025)

**Employee on-cost**

| Contribution | Employee Rate | Ceiling |
| --- | --- | --- |
| NIS | 3% | JMD 5,000,000 p.a. |
| NHT | 2% | None |
| Education Tax | 2.25% | None (on income net of NIS) |
| **Total employee deductions** | **~7.25%** (blended; NIS ceiling applies) | — |

**Employer on-cost**

| Contribution | Employer Rate | Ceiling |
| --- | --- | --- |
| NIS | 3% | JMD 5,000,000 p.a. |
| NHT | 3% | None |
| Education Tax | 3.5% | None |
| HEART (3+ employees) | 3% | None |
| **Total employer on-cost** | **~12.5%** | — |

**Self-employed total**

| Contribution | Self-Employed Rate | Ceiling |
| --- | --- | --- |
| NIS | 6% | JMD 5,000,000 p.a. |
| NHT | 3% | None |
| Education Tax | 2.25% | None (on income net of NIS) |
| **Total self-employed statutory** | **~11.25%** (blended; NIS ceiling applies) | — |

Note: The totals are approximate because the NIS ceiling means effective rates fall as income rises above JMD 5,000,000.

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP — do not apply threshold until residency confirmed |
| Unknown pensioner / Golden Ager status | Do not apply additional exemptions |
| Unknown business-use % (vehicle, home office, phone) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether NHT contributions are current | Do not assume deductibility of arrears |
| Unknown GCT registration status | Ask if annual turnover approaches JMD 15,000,000 |
| Dividend income — unknown withholding applied | Treat as 15% WHT already deducted (final for ordinary dividends) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of residency status (resident or non-resident) and income source (employed, self-employed, or both).
- **Recommended inputs** — All sales invoices, purchase invoices/receipts, NIS/NHT/Education Tax payment records, prior year S04 or tax assessment, quarterly S04A payment confirmations, capital allowances schedule (Schedule 2).
- **Ideal inputs** — Complete Profit & Loss Account and Balance Sheet, asset register, all statutory payment receipts, evidence of approved superannuation contributions, any GCT return filed for the year.
- **Refusal if minimum is missing** — SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This S04 working paper was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-JM-1** — Residency status unknown. "Residency determines whether the tax-free threshold applies and whether worldwide income is in scope. This skill cannot compute tax without confirming residency. Please confirm before proceeding."
- **R-JM-2** — Company or partnership structure. "This skill covers sole traders and individuals only. Companies file a corporate income tax return; partnerships file separately. Escalate to a qualified Jamaican tax practitioner."
- **R-JM-3** — Non-resident income from outside Jamaica. "Non-residents are taxed only on Jamaica-source income. Cross-border income sourcing is complex. Escalate to a qualified practitioner."
- **R-JM-4** — Estate or trust income. "Estate and trust taxation is outside the scope of this skill. Escalate to a qualified practitioner."
- **R-JM-5** — Arrears / TAJ enforcement. "Client has outstanding tax arrears or is subject to TAJ enforcement. The 33.33% per annum interest rate on late payments is severe. Do not advise further. Escalate to a qualified practitioner immediately."
- **R-JM-6** — GCT return requested. "This skill covers income tax only (S04, IT01). For Jamaica General Consumption Tax, use the jamaica-gct skill."
- **R-JM-7** — Transfer tax or stamp duty on property. "Transfer tax (1.5% on estate; 15% on real estate transfers) is a transactional tax outside this skill. Escalate to a qualified practitioner."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | S04 Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED, WIRE | Gross business income | Business income — include in revenue | If GCT-registered (above JMD 15M threshold), extract net (excl. 15% GCT) |
| INVOICE, PROFESSIONAL FEES, CONSULTANCY, SERVICES | Gross business income | Business income | Typical for self-employed professionals |
| STRIPE PAYOUT, STRIPE TRANSFER | Gross business income | Business income — platform payout | Match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Gross business income | Business income — platform payout |  |
| WISE PAYOUT, WISE TRANSFER | Gross business income | Business income — international payout | Use JMD equivalent at date of receipt |
| UPWORK, FIVERR, TOPTAL, FREELANCER | Gross business income | Business income — net of platform commission | Gross up if commission separately charged |
| SALARY, WAGES, EMOLUMENTS, EMPLOYER [name] | Employment income | NOT self-employment — separate schedule | PAYE withholding should have applied |
| RENT RECEIVED, RENTAL PAYMENT FROM | Rental income | Rental income — include in total income | Not self-employment |
| INTEREST, BANK INTEREST | Interest income | 25% WHT likely already deducted at source | Include gross; credit WHT |
| DIVIDEND, DIV PAYMENT | Dividend income | 15% WHT ordinary dividend (final if applied) | Preference dividends at 25%/30% |
| TAJ REFUND, TAX REFUND | EXCLUDE | Prior year refund — not income |  |
| GRANT, GOVERNMENT GRANT, MSME GRANT | Check nature | Revenue grant = income; capital grant = exclude | Ask client |

### 3.2 Expense Patterns (Debits) -- Fully Deductible Business Expenses

**Fully Deductible Business Expenses table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, LEASE [commercial address] | Office rent | Deductible — wholly and exclusively incurred | Dedicated business premises only |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, CPA, BOOKKEEPER, TAX PRACTITIONER | Accountancy fees | Deductible |  |
| LAWYER, ATTORNEY, LEGAL, NOTARY (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing / advertising | Deductible |  |
| TRAINING, COURSE, SEMINAR, CONFERENCE, CPD | Training | Deductible | Must relate to current business |
| PROFESSIONAL BODY, SUBSCRIPTION, MEMBERSHIP (professional) | Professional subscriptions | Deductible |  |
| BANK CHARGE, MAINTENANCE FEE, SERVICE CHARGE | Bank charges | Deductible — business account only |  |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible if recurring subscription or under capital threshold |  |
| POSTAGE, COURIER, DELIVERY (business) | Postage / delivery | Deductible |  |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible — operating expense | Recurring subscription |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| SOFTWARE LICENCE (perpetual, significant cost) | Capital item | Capitalise — use capital allowances schedule | Recurring vs perpetual distinction; flag for reviewer |

### 3.4 Expense Patterns (Debits) -- Utilities (Apportionment Required)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| JPS, JAMAICA PUBLIC SERVICE, ELECTRICITY | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| NWC, NATIONAL WATER COMMISSION, WATER | Water | T2 if home office |  |
| FLOW, DIGICEL, LIME, INTERNET, BROADBAND | Telecoms | T2 | Business use portion only; default 0% if mixed |
| DIGICEL MOBILE, FLOW MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| CARIBBEAN AIRLINES, JETBLUE, AMERICAN AIRLINES | Flights | Deductible if wholly business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB, RESORT | Accommodation | Deductible if wholly business travel |  |
| UBER, KNUTSFORD EXPRESS, TAXI, TRANSPORT | Local transport | Deductible if business purpose |  |
| PETROL, FUEL, GAS STATION, RUBIS, TOTAL | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARKING | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINING, LUNCH, DINNER, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Not wholly and exclusively business |
| PERSONAL, GROCERIES, SUPERMARKET | Personal expenses | NOT deductible |  |
| FINE, PENALTY, TRAFFIC TICKET | Fines / penalties | NOT deductible | Public policy |
| TAJ PAYMENT, INCOME TAX PAYMENT, TAX PAYMENT | Income tax | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal use) | Drawings | NOT deductible | Not a business expense |
| DONATION (over 5% of chargeable income) | Excess charitable donation | NOT deductible | Capped at 5% of taxable income |

- **Note on charitable donations** — Deductible up to 5% of taxable income for approved charitable organisations. Excess is blocked.

### 3.7 Expense Patterns (Debits) -- Capital Items (Schedule 2)

**Capital Items table**  _(Source: PwC Jamaica Deductions; https://taxsummaries.pwc.com/jamaica/individual/deductions)_

| Pattern | Asset Class | Initial Allowance | Annual Rate | Notes |
| --- | --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP, SERVER | Data processing equipment | 25% | 20% | Schedule 2 |
| PRINTER, SCANNER, COPIER, PHOTOCOPIER | Plant & machinery (office) | 25% | 12.5% | Schedule 2 |
| FURNITURE, DESK, CHAIR, FILING CABINET | [RESEARCH GAP — reviewer to confirm specific rate] | — | — | Flag for reviewer |
| VEHICLE, CAR, TRUCK (trade/PSV) | Trade vehicles | 0% initial | 20% | Business use % only; private motor vehicle cost capped at USD 35,000 |
| PRIVATE VEHICLE (personal use partly business) | Private motor vehicle | 0% initial | 12.5% | Cost cap USD 35,000; business % only |
| INDUSTRIAL BUILDING (concrete) | Industrial building | 20% (standard) | 4%--12.5% | Enhanced: 30% Year 1 / 25% Year 2 for spend in 2025--2026 |
| AIR CONDITIONING, AC UNIT | Plant & machinery | 25% | 12.5% |  |

**Enhanced (accelerated) capital allowances 2025-2026**  _(Source: EY Tax Alert; https://globaltaxnews.ey.com/news/2025-0742-jamaica-proposes-accelerated-capital-allowances-for-certain-expenditures-and-reduced-dividend-withholding-tax-rates)_

| Asset Class | Year 1 | Year 2 | Subsequent Years |
| --- | --- | --- | --- |
| Industrial buildings (concrete) | 30% initial + annual | 25% | 5.5%/year until written off |
| Non-industrial buildings (concrete) | 12% initial + annual | 8% | 5%/year |
| Machinery (production/manufacturing) | 40% initial | 25%/year | Until written off |
| Data processing equipment | 40% initial | 33.33%/year | Until written off |

### 3.8 Statutory Contributions (Separate Lines — Not Business Expenses)

**Statutory Contributions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NIS, NATIONAL INSURANCE, NIS CONTRIBUTION | Deductible from income for IT purposes | Deducted before computing chargeable income; NOT a business expense in P&L |
| NHT, NATIONAL HOUSING TRUST | NOT deductible from income for IT purposes | Contributions accumulate in NHT account — not a tax deduction |
| EDUCATION TAX | NOT separately deductible from IT base | Employer's Education Tax is a business expense; employee and self-employed Ed Tax is not deductible |
| HEART LEVY | Employer only — deductible as business expense |  |
| QUARTERLY ESTIMATED TAX, S04A PAYMENT | Credit against annual liability | Not an expense — credit on annual return |
| PAYE WITHHELD | Credit against annual liability | Not an expense |

### 3.9 Jamaican Banks -- Statement Format Reference

**Bank Statement Format Reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| NCB (National Commercial Bank) | TRANSFER, PAYMENT, DD, WITHDRAWAL, DEPOSIT | Most common; description includes counterparty + reference |
| Scotiabank Jamaica | TRF, PAYMENT, CARD, DD, CREDIT | PDF/CSV; date in DD/MM/YYYY |
| JMMB Bank | TRANSFER, PAYMENT | Growing consumer and business bank |
| Sagicor Bank Jamaica | PAYMENT, TRANSFER, DEBIT |  |
| Wise (USD/foreign currency) | TRANSFER, CONVERSION, FEE | Multi-currency — use JMD equivalent at transfer date |
| PayPal / Stripe (USD) | PAYOUT | Convert to JMD at Bank of Jamaica rate on date of receipt |

## Section 4 -- Worked Examples

### Example 1 -- Employee Below Threshold (All Income Within Tax-Free Band)

**Scenario:** Employee, resident, annual gross salary JMD 1,500,000.

**Bank statement line:**
`15/01/2025 ; NCB CREDIT ; EMPLOYER ABC LTD ; MONTHLY SALARY JAN ; +125,000.00 ; JMD`

**Computation (annual):**
- Gross salary: JMD 1,500,000
- NIS (employee): JMD 1,500,000 x 3% = JMD 45,000 (ceiling JMD 5,000,000 not triggered)
- NHT (employee): JMD 1,500,000 x 2% = JMD 30,000
- Education Tax base: JMD 1,500,000 - JMD 45,000 = JMD 1,455,000; Ed Tax = JMD 1,455,000 x 2.25% = JMD 32,737.50
- Chargeable income for IT: JMD 1,500,000 - JMD 45,000 (NIS deductible) - JMD 1,774,554 (threshold) = negative — threshold exceeds income
- Income tax: JMD 0 (income below threshold)
- **Net take-home:** JMD 1,500,000 - JMD 45,000 - JMD 30,000 - JMD 32,737.50 = **JMD 1,392,262.50**
- Note: Education Tax of JMD 32,737.50 still applies despite income being below the IT threshold — common compliance point.

**Classification:** Statutory deductions apply; IT = nil.

### Example 2 -- Employee Above Threshold, Single Band

**Scenario:** Employee, resident, annual gross salary JMD 2,400,000.

**Computation (annual):**
- Gross salary: JMD 2,400,000
- NIS (employee): JMD 2,400,000 x 3% = JMD 72,000
- NHT (employee): JMD 2,400,000 x 2% = JMD 48,000
- Education Tax base: JMD 2,400,000 - JMD 72,000 = JMD 2,328,000; Ed Tax = JMD 2,328,000 x 2.25% = JMD 52,380
- Chargeable income for IT: JMD 2,400,000 - JMD 72,000 (NIS) - JMD 1,774,554 (threshold) = JMD 553,446
- Income tax: JMD 553,446 x 25% = JMD 138,361.50 (entirely in lower band; JMD 553,446 < JMD 6,000,000)
- **Net take-home:** JMD 2,400,000 - JMD 72,000 - JMD 48,000 - JMD 52,380 - JMD 138,361.50 = **JMD 2,089,258.50**

**Classification:** 25% lower band; all standard contributions apply.

### Example 3 -- Self-Employed, Lower Band

**Scenario:** Sole trader, resident, gross business income JMD 3,500,000, allowable business expenses JMD 400,000 (excluding NIS/NHT/Ed Tax).

**Computation (annual):**
- Gross business income: JMD 3,500,000
- Less: allowable business expenses: JMD 400,000
- Statutory income before contributions: JMD 3,100,000
- NIS (self-employed): JMD 3,500,000 x 6% = JMD 210,000 (ceiling not triggered; JMD 3,500,000 < JMD 5,000,000)
- NHT (self-employed): JMD 3,100,000 (net statutory income after expenses) x 3% = JMD 93,000 [RESEARCH GAP — reviewer to confirm NHT base is net statutory income or gross; PwC cites 3% on emoluments; NHT site cites net statutory income for self-employed]
- Education Tax base: JMD 3,500,000 - JMD 210,000 (NIS) = JMD 3,290,000; Ed Tax = JMD 3,290,000 x 2.25% = JMD 74,025
- Chargeable income for IT: JMD 3,500,000 - JMD 400,000 (business expenses) - JMD 210,000 (NIS deductible) - JMD 1,774,554 (threshold) = JMD 1,115,446
- Income tax: JMD 1,115,446 x 25% = JMD 278,861.50 (entirely in lower band)
- **Total statutory payments:** JMD 210,000 + JMD 93,000 + JMD 74,025 + JMD 278,861.50 = JMD 655,886.50
- **Net retained:** JMD 3,500,000 - JMD 400,000 (expenses) - JMD 655,886.50 = **JMD 2,444,113.50**

**Classification:** Lower band; all self-employed contributions apply.

### Example 4 -- Self-Employed, Spanning Both Bands

**Scenario:** Sole trader, resident, gross business income JMD 9,000,000, allowable expenses JMD 500,000.

**Computation (annual):**
- Gross business income: JMD 9,000,000
- Less: allowable business expenses: JMD 500,000
- NIS (self-employed): ceiling applies; JMD 5,000,000 x 6% = JMD 300,000 (maximum)
- Ed Tax base: JMD 9,000,000 - JMD 300,000 = JMD 8,700,000; Ed Tax = JMD 8,700,000 x 2.25% = JMD 195,750
- NHT (self-employed): [RESEARCH GAP — base to be confirmed] approximately JMD 8,500,000 x 3% = JMD 255,000 (illustrative)
- Chargeable income for IT: JMD 9,000,000 - JMD 500,000 (business expenses) - JMD 300,000 (NIS) - JMD 1,774,554 (threshold) = JMD 6,425,446
- IT on lower band (JMD 6,000,000 x 25%): JMD 1,500,000
- IT on upper band (JMD 6,425,446 - JMD 6,000,000 = JMD 425,446 x 30%): JMD 127,633.80
- Total income tax: JMD 1,500,000 + JMD 127,633.80 = **JMD 1,627,633.80**

**Classification:** Spans both bands; upper 30% rate applies to JMD 425,446.

### Example 5 -- Laptop Purchase (Capital Item, Not Immediate Expense)

**Bank statement line:**
`10/06/2025 ; NCB CARD ; BEST BUY ELECTRONICS KINGSTON ; MACBOOK PRO ; -180,000.00 ; JMD`

**Reasoning:**
Capital asset — data processing equipment. Depreciated at 20% per annum straight-line (standard rate) or 40% initial allowance + 33.33%/year under the enhanced 2025--2026 accelerated allowances. Using standard rates: JMD 180,000 x 20% = JMD 36,000 capital allowance in year of purchase. Do NOT put the full JMD 180,000 in deductible expenses.

Under accelerated allowance (for qualifying expenditure 1 Jan 2025 -- 31 Dec 2026): Year 1 allowance = 40% initial = JMD 72,000 (plus standard 20% on remaining JMD 108,000 = JMD 21,600); flag for reviewer to confirm qualification.

**Classification:** Schedule 2 (capital allowances) — standard annual allowance JMD 36,000. NOT a P&L expense.

### Example 6 -- Internal Transfer (Exclude)

**Bank statement line:**
`20/03/2025 ; NCB TRANSFER ; OWN SAVINGS ACCOUNT ; PERSONAL SAVINGS ; -500,000.00 ; JMD`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely from S04 computation.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly and Exclusively Test

- **Wholly and exclusively test** — An expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned. The apportionment method must be reasonable and documented.  _(Source: Income Tax Act (Jamaica), deductions provisions; PwC Jamaica Deductions — https://taxsummaries.pwc.com/jamaica/individual/deductions)_

### 5.2 Self-Employed — Computation of Chargeable Income

- **Chargeable income formula** — Chargeable income = Gross business income LESS: Wholly and exclusively incurred business expenses LESS: NIS contributions (deductible) LESS: Approved superannuation / pension contributions LESS: Interest on capital employed in earning income LESS: Charitable donations (capped at 5% of taxable income to approved organisations) LESS: Tax-free threshold (JMD 1,774,554 blended for 2025) = Taxable income to which 25%/30% rates are applied  _(Source: PwC Jamaica Deductions.)_
- **NHT and Ed Tax not deductible for self-employed IT base** — NHT and Education Tax are NOT deductible from the income tax base for self-employed persons (NIS is deductible; NHT and Ed Tax are not).  _(Source: PwC Jamaica Deductions.)_

### 5.3 Loss Carry-Forward

- **Loss carry-forward restriction** — Losses are restricted to 50% of chargeable income in the carry-forward year. Exceptions: new businesses (first 5 years) or businesses with turnover under JMD 15,000,000. A sole trader cannot use the threshold to create or enlarge a loss carry-forward.  _(Source: PwC Jamaica Deductions.)_

### 5.4 Capital Allowances (Standard Rates — Straight-Line)

**Standard Rates table**  _(Source: EY Tax Alert 2025-0742.)_

| Asset Class | Initial Allowance | Annual Rate |
| --- | --- | --- |
| Industrial buildings (concrete) | 20% | 4%--12.5% |
| Non-industrial buildings | 0% | 4% |
| Plant & machinery (production) | 25% | 12.5% |
| Data processing equipment | 25% | 20% |
| Trade / PSV vehicles | 0% | 20% |
| Private motor vehicles (cost capped at USD 35,000) | 0% | 12.5% |

- **Enhanced rates cross reference** — Enhanced (accelerated) rates available for qualifying expenditure 1 Jan 2025 -- 31 Dec 2026 — see Section 3.7 and Section 6.4.  _(Source: EY Tax Alert 2025-0742.)_

### 5.5 Non-Deductible Expenses

**Non-Deductible Expenses table**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Not wholly and exclusively for business |
| Personal living expenses | Private |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income cannot reduce income |
| NHT contributions (self-employed) | Not deductible for IT purposes |
| Capital expenditure | Must go through Schedule 2 capital allowances |
| Drawings / personal withdrawals | Not an expense |
| Charitable donations exceeding 5% of taxable income | Capped |

### 5.6 Income Types and Tax Treatment

**Income Types table**  _(Source: PwC Jamaica Income Determination — https://taxsummaries.pwc.com/jamaica/individual/income-determination)_

| Income Type | Tax Treatment |
| --- | --- |
| Business profits (sole trader) | 25% / 30% progressive, after threshold |
| Employment income | PAYE withholding; threshold applied by employer |
| Rental income | Included in total income on return |
| Interest (from banks/financial institutions) | 25% WHT deducted at source — credit on return |
| Ordinary dividends | 15% WHT — final (not included in IT01 if WHT applied) |
| Preference dividends | Included in return at 25%/30% |
| Capital gains | NONE — Jamaica has no capital gains tax on individuals |

### 5.7 Withholding Taxes on Passive Income

**Withholding Taxes table**  _(Source: PwC Jamaica Significant Developments — https://taxsummaries.pwc.com/jamaica/individual/significant-developments; EY Tax Alert 2025-0742.)_

| Payment Type | Resident Rate | Non-Resident Rate |
| --- | --- | --- |
| Ordinary dividends | 15% (final WHT) | 15% (from 1 Apr 2025; previously 25%) |
| Preference dividends | 25% / 30% progressive | 25% / 30% |
| Interest (banks/financial) | 25% (credit against IT) | 25% |

- **Non-resident dividend WHT reduction** — Non-resident dividend WHT reduced from 25% to 15% effective 1 April 2025.  _(Source: PwC Jamaica Significant Developments — https://taxsummaries.pwc.com/jamaica/individual/significant-developments; EY Tax Alert 2025-0742.)_

### 5.8 Benefits in Kind (Employment)

- **Company car deemed benefit** — Company cars attract a deemed benefit: Benefit value: JMD 30,000 to JMD 140,000 per year depending on cost, age, and usage. Included in employment income and subject to PAYE. [RESEARCH GAP — reviewer to confirm exact tiered scale from current TAJ guidelines]  _(Source: PwC Jamaica Income Determination.)_

### 5.9 GCT Registration Threshold

- **GCT registration threshold** — Self-employed persons providing taxable goods or services must register for General Consumption Tax (GCT — Jamaica's VAT equivalent) if annual turnover meets or exceeds JMD 15,000,000 (increased from JMD 10,000,000, effective 1 April 2025). Registration required within 21 days of crossing the threshold. GCT rate: 15% standard. GCT returns and payment due by 25th of each month.  _(Source: JIS — https://jis.gov.jm/gct-exemption-threshold-for-msmes-increased-to-15-million/; VATupdate — https://www.vatupdate.com/2025/03/13/jamaica-raises-gct-registration-threshold-in-2025-26-budget/)_

For GCT computation details, use the jamaica-gct skill.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction method** — Calculate the proportion of home used exclusively for business (dedicated room as a percentage of total rooms or floor area). Apply that percentage to rent, electricity, water, internet, and maintenance costs. A dual-use room (kitchen table, living room) does NOT qualify. Conservative default: 0% deduction until reviewer confirms room arrangement and business exclusivity. Flag for reviewer: Confirm room count, floor area basis, and that the workspace is genuinely dedicated and used exclusively for business.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use rules** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must maintain a mileage log (business trips vs total mileage). For private motor vehicles, the cost is capped at USD 35,000 for capital allowance purposes. Conservative default: 0% business use until mileage log provided. Flag for reviewer: Confirm business percentage is documented, vehicle classification (trade vs private), and USD 35,000 cost cap compliance.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rule** — Business-use portion only. Client must provide a reasonable estimate of business vs personal use. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Accelerated Capital Allowances (2025--2026)

- **Accelerated capital allowances qualification** — For qualifying capital expenditure between 1 January 2025 and 31 December 2026, enhanced rates apply (see Section 3.7). The asset and expenditure must qualify under the budget measure. Flag for reviewer to confirm qualification before applying enhanced rates.

### 6.5 Approved Superannuation Contributions

- **Approved superannuation contributions rule** — Contributions to an approved superannuation/pension scheme are deductible. The scheme must be approved by the relevant authority. Flag for reviewer: Confirm the scheme is TAJ-approved before deducting.

### 6.6 Bad Debt Write-Off

- **Bad debt write-off conditions** — Deductible only if: (1) the income was previously declared as business income, (2) all reasonable recovery steps have been taken, and (3) the debt is genuinely irrecoverable. Flag for reviewer: Confirm all three conditions before deducting.

### 6.7 Charitable Donations

- **Charitable donations cap** — Deductible up to 5% of taxable income for approved charitable organisations. Excess is not deductible. Flag for reviewer: Confirm the organisation is approved; confirm cap calculation.

### 6.8 NHT Base for Self-Employed

- **NHT base uncertainty** — PwC cites NHT at 3% for self-employed on emoluments; the NHT official site references "net statutory income." The exact base (gross income, net of expenses, or net of NIS) for self-employed NHT computations requires confirmation. [RESEARCH GAP — reviewer to confirm NHT base for self-employed from current NHT Act provisions.]

## Section 7 -- Excel Working Paper Template

```
JAMAICA INCOME TAX — S04 WORKING PAPER
Tax Year: 2025 (1 January -- 31 December 2025)
Client: ___________________________
Status: Self-Employed / Employee with other income
Residency: Resident / Non-Resident
Pensioner (approved scheme)? Yes / No
Golden Ager (65+)? Yes / No

A. GROSS INCOME
  A1. Business income (gross revenue)               ___________
  A2. Employment income                             ___________
  A3. Rental income                                 ___________
  A4. Interest income (gross, before 25% WHT)       ___________
  A5. Dividend income (ordinary, gross if WHT)      ___________
  A6. Other income                                  ___________
  A7. TOTAL GROSS INCOME                            ___________

B. ALLOWABLE BUSINESS DEDUCTIONS (P&L)
  B1. Office rent                                   ___________
  B2. Professional insurance                        ___________
  B3. Accountancy / legal fees                      ___________
  B4. Office supplies / stationery                  ___________
  B5. Software subscriptions                        ___________
  B6. Marketing / advertising                       ___________
  B7. Bank charges / payment processing fees        ___________
  B8. Training / CPD / professional subscriptions   ___________
  B9. Travel (flights, hotels, transport)           ___________
  B10. Telecoms (business % of phone/internet)      ___________
  B11. Home office (% of utilities/rent)            ___________
  B12. Vehicle expenses (business % only)           ___________
  B13. Other allowable expenses                     ___________
  B14. TOTAL BUSINESS DEDUCTIONS                    ___________

C. NET BUSINESS INCOME (A1 - B14)                  ___________

D. FURTHER DEDUCTIONS FROM CHARGEABLE INCOME
  D1. NIS contributions (deductible)                ___________
  D2. Approved superannuation contributions         ___________
  D3. Capital allowances (Schedule 2)               ___________
  D4. Charitable donations (max 5% of taxable)      ___________
  D5. TOTAL FURTHER DEDUCTIONS                      ___________

E. INCOME BEFORE THRESHOLD (C + A2:A6 - D5)        ___________

F. TAX-FREE THRESHOLD (2025 blended)               (1,774,554)
   Additional: Pensioner exemption                 (250,040) if applicable
   Additional: Golden Ager exemption               (250,040) if applicable

G. CHARGEABLE INCOME (E - F)                        ___________

H. INCOME TAX COMPUTATION
  H1. Lower band: up to JMD 6,000,000 x 25%        ___________
  H2. Upper band: excess above JMD 6,000,000 x 30% ___________
  H3. TOTAL INCOME TAX LIABILITY                    ___________

I. STATUTORY CONTRIBUTIONS (for self-employed)
  I1. NIS: min(gross income x 6%, JMD 300,000)     ___________
  I2. NHT: net statutory income x 3%               ___________
  I3. Education Tax: (gross - NIS) x 2.25%         ___________
  I4. TOTAL STATUTORY CONTRIBUTIONS                 ___________

J. CREDITS
  J1. PAYE withheld during year                    ___________
  J2. WHT on interest (25%)                        ___________
  J3. WHT on dividends (15%)                       ___________
  J4. Quarterly estimated tax paid (S04A x4)       ___________
  J5. TOTAL CREDITS                                ___________

K. TAX DUE / REFUND (H3 - J5)                      ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] Pensioner / Golden Ager status confirmed?
  [ ] All NIS, NHT, Education Tax payment records obtained?
  [ ] GCT registration status checked (turnover vs JMD 15M threshold)?
  [ ] All T2 items (home office, vehicle, phone) flagged for review?
  [ ] Entertainment expenses excluded?
  [ ] Capital items in Schedule 2 (not P&L)?
  [ ] Charitable donation cap verified (max 5%)?
  [ ] Loss carry-forward restriction applied if applicable?
  [ ] Accelerated capital allowances eligibility confirmed for 2025--2026 spend?
  [ ] NHT base for self-employed confirmed with reviewer?
```

## Section 8 -- Bank Statement Reading Guide

### Jamaican Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| NCB (National Commercial Bank) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description contains counterparty + reference |
| Scotiabank Jamaica | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant name |
| JMMB Bank | PDF | Date, Particulars, Withdrawals, Deposits | Shorter descriptions |
| Sagicor Bank Jamaica | PDF | Date, Description, Amount |  |
| Wise (multi-currency) | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency — use JMD equivalent at date |
| PayPal / Stripe | CSV/Dashboard | Date, Counterparty, Amount, Currency | Convert to JMD at Bank of Jamaica rate on date of receipt |

### Key Jamaican Banking and Tax Terms

**Key Terms table**

| Term | English / Context | Classification Hint |
| --- | --- | --- |
| TRANSFER / TRF | Bank transfer | Check direction; income or expense |
| DD / DIRECT DEBIT | Direct debit | Regular expense (utility, subscription) |
| SO / STANDING ORDER | Standing order | Regular expense (rent) |
| CARD / CARD PAYMENT | Debit/credit card | Expense — check merchant |
| CREDIT | Deposit / inbound | Potential income |
| CHARGES / BANK CHARGES | Bank service charges | Deductible (business account) |
| EMOLUMENTS | Employment income | PAYE income |
| STATUTORY DEDUCTIONS | NIS + NHT + Ed Tax | Payroll contributions |
| GCT | General Consumption Tax | VAT equivalent; exclude from income if GCT-registered |
| TAJ | Tax Administration Jamaica | Tax authority — tax payments / refunds |
| S04 / S04A | Self-employed tax return forms | Annual / quarterly |
| TRN | Taxpayer Registration Number | 9-digit ID required for all filers |
| KNUTSFORD | Knutsford Express (intercity bus) | Deductible travel if business purpose |
| JPS | Jamaica Public Service (electricity) | Utility — T2 apportionment |
| NWC | National Water Commission | Utility — T2 apportionment |
| RUBIS / TOTAL / GAS STATION | Fuel / petrol | Vehicle expense — T2 business % |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING — reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS — JAMAICA INCOME TAX (S04)

1. Residency status: are you a Jamaican tax resident for 2025?
2. Income type: are you self-employed, employed, or both?
3. Pensioner: do you receive income from a TAJ-approved superannuation/pension scheme?
4. Golden Ager: are you aged 65 or over?
5. NIS: what is your total NIS contribution paid in 2025? Do you have payment receipts?
6. NHT: what is your total NHT contribution paid in 2025?
7. Education Tax: has your employer deducted Education Tax, or do you pay it yourself?
8. Quarterly estimated tax: have you made any S04A payments during 2025? Total amount?
9. PAYE: has income tax been withheld at source by your employer? Total withheld?
10. Home office: do you use a dedicated room exclusively for business? What % of floor area?
11. Vehicle: do you use a vehicle for business? Business use %? Do you have a mileage log?
12. Phone/internet: what % of usage is for business?
13. GCT: is your annual turnover at or above JMD 15,000,000? Are you GCT-registered?
14. Capital assets: did you purchase any significant assets (equipment, vehicles) in 2025?
15. Superannuation: do you contribute to a TAJ-approved pension scheme? Amount?
16. Other income: any rental income, interest, or dividends received?
17. TRN: do you have your 9-digit Taxpayer Registration Number?
```

### Key Legislation and Authority References

**Key Legislation and Authority References**  _(Income Tax Act (Jamaica))_

| Topic | Reference |
| --- | --- |
| Income tax rates and threshold | Income Tax Act (Jamaica) |
| April 2025 threshold increase | TAJ Technical Advisory #042025/01/IT-TA |
| Allowable deductions | Income Tax Act — deductions provisions |
| Capital allowances | Income Tax Act — Schedule 2 |
| NIS | National Insurance Scheme Act; https://mlss.gov.jm/departments/national-insurance-scheme/ |
| NHT | National Housing Trust Act; https://www.nht.gov.jm/self-employed-contributions |
| Education Tax | Education Tax Act |
| HEART levy | HEART Trust/NSTA Act |
| Filing deadlines | Tax Administration Jamaica Act |
| Penalties and interest | Tax Administration Jamaica Act |
| PwC summary (authoritative secondary) | https://taxsummaries.pwc.com/jamaica/individual/taxes-on-personal-income |
| EY capital allowances / WHT alert | https://globaltaxnews.ey.com/news/2025-0742-jamaica-proposes-accelerated-capital-allowances-for-certain-expenditures-and-reduced-dividend-withholding-tax-rates |
| TAJ e-Portal | https://www.jamaicatax.gov.jm |
| JIS threshold announcement | https://jis.gov.jm/increase-in-income-tax-threshold-now-in-effect/ |
| JIS minimum wage (June 2025) | https://jis.gov.jm/minimum-wage-moves-to-16000-june-1/ |
| JIS GCT threshold increase | https://jis.gov.jm/gct-exemption-threshold-for-msmes-increased-to-15-million/ |

### Filing Forms Summary

**Filing Forms Summary**  _(Tax Administration Jamaica Act)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| S04 | Self-employed annual return (year ended 31 Dec) | 15 March of following year |
| S04A | Quarterly declaration of estimated income and contributions | 15 March, 15 June, 15 Sept, 15 Dec |
| IT01 | Individual return for employees with additional income sources | 15 March of following year |
| IT05 | PAYE / pensioner return (reclaim excess withholding) | 15 March of following year |
| S01 | Employer monthly statutory remittance | 14th of each month |
| IT06 | Employer annual PAYE return | 14 January of following year |

All returns must be filed electronically via the TAJ e-Portal. Source: TAJ Portal — https://www.jamaicatax.gov.jm/self-employed-statutory; JIS filing season — https://jis.gov.jm/taj-launches-2025-tax-filing-season/

### Penalties and Interest

**Penalties and Interest**  _(Tax Administration Jamaica Act)_

| Offence | Penalty |
| --- | --- |
| Late filing of return | JMD 5,000 per month (or part month) per form from day after due date |
| Late payment — interest | 33.33% per annum from day after due date until payment |
| TAJ-issued assessment (audit) | Up to 50% additional penalty on assessed tax |
| Statute of limitations — assessment | 6 years |
| Statute of limitations — refund claim | 6 years |

Notes: Filing on time eliminates the JMD 5,000/month filing penalty even if payment cannot be made immediately. Extensions require written permission from the Commissioner General. [RESEARCH GAP — reviewer to confirm the 33.33% p.a. interest rate from current legislation; PwC has cited 16.62% p.a. in some editions — discrepancy may reflect different provisions or an update. Source: PwC Jamaica Tax Administration — https://taxsummaries.pwc.com/jamaica/individual/tax-administration]

### Minimum Wage (Reference Only — Not a Tax Rate)

Effective 1 June 2025: JMD 16,000 per 40-hour week (JMD 400/hour). This is relevant for payroll compliance, not for computing income tax rates. Source: JIS — https://jis.gov.jm/minimum-wage-moves-to-16000-june-1/

### Key 2025/2026 Budget Changes (Summary)

1. IT threshold raised to JMD 1,799,376 (April 2025); planned JMD 1,902,360 (April 2026)
2. GCT registration threshold raised from JMD 10,000,000 to JMD 15,000,000 (April 2025)
3. Non-resident ordinary dividend WHT reduced from 25% to 15% (April 2025)
4. Enhanced / accelerated capital allowances on qualifying plant and buildings (2025--2026)
5. Residential electricity GCT reduced from 15% to 7% (May 2025) — GCT, not income tax
6. Minimum wage raised to JMD 16,000/week (June 2025)

Source: EY; KPMG budget review; JIS; Ministry of Finance Revenue Measures 2025/2026 — https://www.mof.gov.jm/wp-content/uploads/Revenue-Measures-2025-2026.pdf

### Test Suite

Input: Resident employee, annual gross salary JMD 1,500,000, no other income, not a pensioner or Golden Ager.
Expected: NIS = JMD 45,000; NHT = JMD 30,000; Ed Tax base = JMD 1,455,000; Ed Tax = JMD 32,737.50; chargeable income for IT = JMD 0 (income below JMD 1,774,554 threshold); IT = JMD 0; net take-home = JMD 1,392,262.50.

Input: Resident employee, annual gross salary JMD 2,400,000, no other income.
Expected: NIS = JMD 72,000; NHT = JMD 48,000; Ed Tax base = JMD 2,328,000; Ed Tax = JMD 52,380; chargeable income = JMD 553,446 (= JMD 2,400,000 - JMD 72,000 - JMD 1,774,554); IT = JMD 138,361.50 (25%); net take-home = JMD 2,089,258.50.

Input: Resident sole trader, gross income JMD 9,000,000, allowable expenses JMD 500,000, no approved pension.
Expected: NIS = JMD 300,000 (ceiling); Ed Tax base = JMD 8,700,000; Ed Tax = JMD 195,750; chargeable income = JMD 6,425,446 (= JMD 9,000,000 - JMD 500,000 - JMD 300,000 - JMD 1,774,554); IT lower band = JMD 1,500,000 (25% x JMD 6,000,000); IT upper band = JMD 127,633.80 (30% x JMD 425,446); total IT = JMD 1,627,633.80.

Input: Resident, aged 67, receives pension from approved scheme, annual pension JMD 1,800,000, no other income.
Expected: Total exemption = JMD 1,774,554 + JMD 250,040 (pensioner) + JMD 250,040 (Golden Ager) = JMD 2,274,634; chargeable income = JMD 1,800,000 - JMD 2,274,634 = negative; IT = JMD 0. NIS = JMD 1,800,000 x 3% = JMD 54,000 [RESEARCH GAP — reviewer to confirm whether NIS applies to pension income from approved scheme].

Input: Self-employed, includes JMD 150,000 client entertainment in claimed deductions.
Expected: Remove JMD 150,000 from deductions. Not deductible. No apportionment.

Input: Laptop JMD 180,000 claimed as immediate business expense.
Expected: Remove from P&L deductions. Capital allowance (standard rate 20%) = JMD 36,000 in Schedule 2. Accelerated rate (40% initial for 2025 qualifying spend) = JMD 72,000 — flag for reviewer to confirm qualification.

Input: Non-resident, Jamaica-source business income JMD 2,000,000, no expenses.
Expected: No threshold applies; chargeable income = JMD 2,000,000; IT = JMD 2,000,000 x 25% = JMD 500,000.

Input: Employee, annual gross salary JMD 1,200,000.
Expected: IT = JMD 0 (below threshold); Ed Tax still applies: base = JMD 1,200,000 - NIS; NIS = JMD 1,200,000 x 3% = JMD 36,000; Ed Tax base = JMD 1,164,000; Ed Tax = JMD 1,164,000 x 2.25% = JMD 26,190. Education Tax does NOT have a threshold exemption.

## PROHIBITIONS

- **Non-resident threshold prohibition** — NEVER apply the tax-free threshold to a non-resident — non-residents pay 25% from the first dollar  _(PROHIBITIONS)_
- **Education Tax threshold prohibition** — NEVER omit Education Tax for employees below the income tax threshold — Education Tax has no threshold exemption  _(PROHIBITIONS)_
- **NHT not deductible from IT base** — NEVER deduct NHT contributions from the income tax base — NHT is not income-tax deductible  _(PROHIBITIONS)_
- **Income tax payments not deductible** — NEVER treat income tax payments as a deductible business expense  _(PROHIBITIONS)_
- **Entertainment not deductible** — NEVER allow entertainment expenses as deductible — no partial deduction, no apportionment  _(PROHIBITIONS)_
- **Capital items not immediate expense** — NEVER allow a capital item as an immediate P&L expense — it must go through Schedule 2 capital allowances  _(PROHIBITIONS)_
- **Fines not deductible** — NEVER allow fines or penalties as deductible  _(PROHIBITIONS)_
- **Charitable donation cap** — NEVER allow charitable donations above 5% of taxable income  _(PROHIBITIONS)_
- **Higher band threshold rule** — NEVER apply the higher 30% rate to income below JMD 6,000,000 above threshold  _(PROHIBITIONS)_
- **Estimation disclosure requirement** — NEVER present tax calculations as definitive — always label as estimated and flag for reviewer sign-off  _(PROHIBITIONS)_
- **GCT exclusion from income** — NEVER use GCT collected from customers as income — if GCT-registered, extract net amount only  _(PROHIBITIONS)_
- **TRN registration check** — NEVER skip the TRN registration check — every individual earning income in Jamaica must have a TRN  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
