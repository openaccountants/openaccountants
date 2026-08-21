---
name: sweden-bookkeeping
description: Use this skill whenever asked about Swedish bookkeeping, chart of accounts, BAS kontoplan, financial statements, or accounting standards in Sweden. Trigger on phrases like "Swedish bookkeeping", "bokföring Sverige", "BAS kontoplan", "kontoplan", "årsredovisning", "K2", "K3", "BFL", "ÅRL", "resultaträkning", "balansräkning", "enskild firma bokföring", "årsbokslut", "Bokföringsnämnden", "BFN", "avskrivning", "förenklat årsbokslut", or any question about recording transactions, financial reporting, or accounting standards for Swedish entities.
version: 1.0
jurisdiction: SE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Sweden (Konungariket Sverige) |
| Currency | SEK (Swedish Krona) |
| Financial year | Flexible; calendar year most common. Split year allowed for non-AB entities. |
| Accounting standards | K2 (BFNAR 2016:10) for smaller companies; K3 (BFNAR 2012:1) for larger/default; K1 for simplified annual accounts |
| Standard chart of accounts | BAS-kontoplanen (voluntary but used by >95% of businesses) |
| Governing body | BFN (Bokföringsnämnden -- Swedish Accounting Standards Board) |
| Key legislation | BFL (Bokföringslagen 1999:1078); ÅRL (Årsredovisningslagen 1995:1554) |
| Filing obligation | Bolagsverket (Swedish Companies Registration Office) -- within 7 months of year-end for AB |
| Tax authority | Skatteverket (Swedish Tax Agency) |
| Archival requirement | 7 years (bokföringslagen ch. 7) |

## Section 2 -- Standard Chart of Accounts (BAS-kontoplanen)

The BAS chart is a four-digit decimal classification system aligned with ÅRL income statement and balance sheet formats. Classes 1-8 cover financial accounting.

### Class 1 -- Tillgångar (Assets)

**Class 1 -- Tillgångar (Assets)**

| Code | Account | Description |
| --- | --- | --- |
| 1010 | Utvecklingsutgifter | Development expenditure (K3 only) |
| 1020 | Koncessioner | Concessions |
| 1030 | Patent | Patents |
| 1050 | Goodwill | Goodwill |
| 1110 | Byggnader | Buildings |
| 1120 | Förbättringsutgifter (annans fastighet) | Improvements to leased property |
| 1130 | Mark | Land |
| 1210 | Maskiner och inventarier | Machinery and equipment |
| 1220 | Inventarier och verktyg | Tools and fixtures |
| 1230 | Datorer | Computers |
| 1240 | Bilar och andra transportmedel | Vehicles |
| 1250 | Kontorsinventarier | Office furniture |
| 1290 | Övriga materiella anläggningstillgångar | Other tangible fixed assets |
| 1310 | Aktier i dotterföretag | Shares in subsidiaries |
| 1380 | Andra långfristiga fordringar | Other long-term receivables |
| 1400 | Varulager | Inventory (goods for resale) |
| 1410 | Lager av råvaror | Raw materials |
| 1420 | Lager av varor under tillverkning | Work in progress |
| 1460 | Lager av handelsvaror | Trading goods |
| 1510 | Kundfordringar | Trade receivables |
| 1610 | Fordringar hos anställda | Receivables from employees |
| 1630 | Skattefordringar | Tax receivables |
| 1710 | Förutbetalda hyreskostnader | Prepaid rent |
| 1790 | Övriga förutbetalda kostnader | Other prepaid expenses |
| 1910 | Kassa | Cash |
| 1920 | PlusGiro | PlusGiro account |
| 1930 | Företagskonto/checkkonto | Business bank account |
| 1940 | Övriga bankkonton | Other bank accounts |

### Class 2 -- Eget Kapital och Skulder (Equity and Liabilities)

**Class 2 -- Eget Kapital och Skulder (Equity and Liabilities)**

| Code | Account | Description |
| --- | --- | --- |
| 2010 | Eget kapital (enskild firma) | Owner's equity (sole trader) |
| 2013 | Privata uttag | Owner's drawings |
| 2018 | Egna insättningar | Owner's contributions |
| 2020-2040 | Eget kapital delägare 2-4 | Partner equity (handelsbolag) |
| 2081 | Aktiekapital | Share capital (AB) |
| 2085 | Uppskrivningsfond | Revaluation reserve |
| 2086 | Reservfond | Legal reserve |
| 2091 | Balanserad vinst/förlust | Retained earnings |
| 2099 | Årets resultat | Current year result |
| 2110-2139 | Periodiseringsfonder | Tax allocation reserves |
| 2150 | Ackumulerade överavskrivningar | Accumulated excess depreciation |
| 2310 | Banklån (långfristiga) | Long-term bank loans |
| 2350 | Andra skulder till kreditinstitut | Other credit institution debts |
| 2390 | Övriga långfristiga skulder | Other long-term liabilities |
| 2440 | Leverantörsskulder | Trade payables (suppliers) |
| 2510 | Skatteskulder | Tax liabilities |
| 2610 | Utgående moms (25%) | Output VAT 25% |
| 2620 | Utgående moms (12%) | Output VAT 12% |
| 2630 | Utgående moms (6%) | Output VAT 6% |
| 2640 | Ingående moms | Input VAT (deductible) |
| 2650 | Redovisning av moms | VAT settlement account |
| 2710 | Personalens källskatt | Employee tax withheld (PAYE) |
| 2730 | Lagstadgade sociala avgifter | Statutory social charges payable |
| 2731 | Avräkning arbetsgivaravgifter | Employer contributions settlement |
| 2790 | Övriga kortfristiga skulder | Other current liabilities |
| 2900 | Upplupna kostnader | Accrued expenses |
| 2910 | Upplupna löner | Accrued wages |
| 2920 | Upplupna semesterlöner | Accrued holiday pay |
| 2940 | Upplupna sociala avgifter | Accrued social contributions |
| 2990 | Övriga upplupna kostnader | Other accrued expenses |

### Class 3 -- Rörelseintäkter (Operating Revenue)

**Class 3 -- Rörelseintäkter (Operating Revenue)**

| Code | Account | Description |
| --- | --- | --- |
| 3010 | Försäljning varor (25% moms) | Sales of goods (25% VAT) |
| 3040 | Försäljning varor (12% moms) | Sales of goods (12% VAT) |
| 3050 | Försäljning varor (6% moms) | Sales of goods (6% VAT) |
| 3100 | Försäljning tjänster (25% moms) | Sales of services (25% VAT) |
| 3200 | Försäljning tjänster momsfri | Sales of services (VAT-exempt) |
| 3300 | EU-intäkter | EU intra-community sales |
| 3400 | Exportintäkter | Export revenue |
| 3900 | Övriga rörelseintäkter | Other operating income |

### Class 4 -- Kostnader för varor/material (COGS)

**Class 4 -- Kostnader för varor/material (COGS)**

| Code | Account | Description |
| --- | --- | --- |
| 4010 | Inköp av varor (inom Sverige) | Purchases of goods (domestic) |
| 4100 | Inköp av råvaror | Raw material purchases |
| 4500 | Övriga inköp av varor/material | Other purchases |
| 4600 | Legoarbete och underentreprenader | Subcontract work |
| 4900 | Förändring av varulager | Inventory change |

### Class 5 -- Övriga Externa Kostnader (Other External Expenses)

**Class 5 -- Övriga Externa Kostnader (Other External Expenses)**

| Code | Account | Description |
| --- | --- | --- |
| 5010 | Lokalhyra | Premises rent |
| 5020 | El för belysning | Electricity |
| 5060 | Städning och renhållning | Cleaning |
| 5090 | Övriga lokalkostnader | Other premises costs |
| 5100 | Fastighetskostnader | Property expenses (owned premises) |
| 5200 | Hyra av anläggningstillgångar | Leased assets |
| 5210 | Hyra av maskiner | Machine leases |
| 5250 | Hyra av datorer | Computer leases |
| 5300-5399 | Energikostnader | Energy costs (heating, fuel) |
| 5400 | Förbrukningsinventarier | Consumable equipment (< SEK 25,000) |
| 5410 | Förbruknings­material | Consumable materials |
| 5420 | Programvaror (avskrivning/abonnemang) | Software (subscription/depreciation) |
| 5500 | Reparation och underhåll | Repairs and maintenance |
| 5600 | Transportkostnader | Transport/freight |
| 5610 | Frakter | Freight costs |
| 5700 | Frakter och transporter (utgående) | Outbound freight |
| 5800 | Resekostnader | Travel expenses |
| 5810 | Biljetter | Tickets (flights, trains) |
| 5820 | Hyrbil | Car rental |
| 5830 | Kost och logi | Meals and accommodation |
| 5900 | Reklam och PR | Advertising and PR |
| 5910 | Annonsering | Advertising |
| 5930 | Reklamtrycksaker | Printed materials |
| 6000 | Övriga försäljningskostnader | Other selling costs |
| 6100 | Kontorsmaterial | Office supplies |
| 6200 | Tele och post | Telecoms and postage |
| 6210 | Telekommunikation | Telephone/internet |
| 6230 | Datakommunikation | Data services |
| 6300 | Företagsförsäkringar | Business insurance |
| 6400 | Förvaltningskostnader | Administration costs |
| 6500 | Övriga externa tjänster | Other external services |
| 6530 | Redovisningstjänster | Accounting services |
| 6540 | IT-tjänster | IT services |
| 6550 | Konsultarvode | Consulting fees |
| 6570 | Bankkostnader | Bank charges |
| 6900 | Övriga externa kostnader | Other miscellaneous external costs |

### Class 7 -- Personalkostnader m.m. (Staff Costs etc.)

**Class 7 -- Personalkostnader m.m. (Staff Costs etc.)**

| Code | Account | Description |
| --- | --- | --- |
| 7010 | Löner till kollektivanställda | Wages -- collectively agreed |
| 7210 | Löner till tjänstemän | Salaries -- employees |
| 7220 | Löner till företagsledare | Directors' salaries |
| 7310 | Kontanta extraförmåner | Cash fringe benefits |
| 7380 | Kostnader för förmåner | Benefit costs |
| 7410 | Pensionsförsäkringspremier | Pension insurance premiums |
| 7510 | Arbetsgivaravgifter | Employer social contributions (31.42%) |
| 7570 | Egenavgifter | Self-employed social contributions |
| 7610 | Utbildning | Training costs |
| 7690 | Övriga personalkostnader | Other staff costs |
| 7820 | Avskrivningar maskiner/inventarier | Depreciation machinery/equipment |
| 7830 | Avskrivningar byggnader | Depreciation buildings |
| 7840 | Avskrivningar bilar | Depreciation vehicles |

### Class 8 -- Finansiella poster, Skatt, Resultat (Financial Items, Tax, Result)

**Class 8 -- Finansiella poster, Skatt, Resultat (Financial Items, Tax, Result)**

| Code | Account | Description |
| --- | --- | --- |
| 8310 | Ränteintäkter | Interest income |
| 8410 | Räntekostnader | Interest expense |
| 8420 | Räntekostnader banklån | Interest on bank loans |
| 8490 | Övriga finansiella kostnader | Other financial costs |
| 8910 | Skatt på årets resultat | Current year income tax |
| 8990 | Resultat | Net profit/loss |

## Section 3 -- Revenue Recognition

### Cash vs Accrual Basis

**Cash vs Accrual Basis**

| Entity Type | Basis | Notes |
| --- | --- | --- |
| AB (Aktiebolag) | Accrual (mandatory) | BFL/ÅRL require accrual basis |
| Enskild firma (sole trader) | Accrual | BFL requires current recording; may use simplified annual accounts |
| Handelsbolag (partnership) | Accrual | Same as AB |
| K1 entity (simplified) | Cash-like | Förenklat årsbokslut allows near-cash treatment |

### Key Rules

- **Revenue recognition timing** — Revenue recognised when performance obligation is satisfied (goods: delivery; services: over time or at completion)
- **K2 recognition** — K2: simpler recognition -- revenue at point of invoicing for most service companies; construction contracts on completion
- **K3 recognition** — K3: percentage-of-completion required for long-term contracts where outcome can be estimated
- **Subscription income** — Subscription income: recognised over the period of service

### Förenklat Årsbokslut (K1 -- Simplified Annual Accounts)

- **Turnover threshold for K1 availability** — SEK 3,000,000 SEK (Net turnover limit for sole traders (enskild firma))
- **Revenue recognition** — Revenue recognised at invoice date (near-cash basis)
- **Accruals threshold for recurring items** — SEK 5,000 SEK (No accruals required for recurring items below this amount)
- **Inventory valuation** — Simplified inventory valuation

## Section 4 -- Expense Classification

### Deductible Operating Expenses

**Deductible Operating Expenses**

| Category | BAS Code | Deductibility |
| --- | --- | --- |
| Premises rent | 5010 | 100% deductible |
| Electricity/utilities | 5020 | 100% deductible |
| Accounting services | 6530 | 100% deductible |
| Insurance (business) | 6300 | 100% deductible |
| Advertising | 5900 | 100% deductible |
| Office supplies | 6100 | 100% deductible |
| Telecoms (business) | 6210 | 100% deductible |
| Bank charges | 6570 | 100% deductible |
| Software subscriptions | 5420 | 100% deductible |
| Travel (business) | 5800 | 100% deductible |
| Training/education | 7610 | 100% deductible |
| Repairs and maintenance | 5500 | 100% deductible |

### Limited/Non-Deductible Expenses

**Limited/Non-Deductible Expenses**

| Category | Limitation |
| --- | --- |
| Representation (extern) -- food/drink | Deductible up to SEK 350/person (excl. VAT) for income tax; VAT deduction limited to SEK 300/person |
| Internal representation | Deductible up to SEK 600/person for 2 events/year |
| Gifts to clients | Deductible if < SEK 300 (excl. VAT) per gift |
| Fines and penalties (böter) | 0% -- never deductible |
| Personal expenses | 0% -- never deductible |
| Income tax | 0% -- never deductible |
| Private portion of mixed assets | Must be excluded (förmånsbeskattning) |

### Vehicle (Bil) Rules

- **Company car private-use** — Company car private-use: taxed as benefit-in-kind (bilförmån) on employee; deductible for company
- **Sole trader vehicle log** — Sole trader: log required for business km; private km not deductible
- **Mileage allowance** — 25 SEK/km (Mileage allowance (if using private car for business): SEK 25/km (tax-free for employment; for self-employed: actual costs))

## Section 5 -- Asset vs Expense Thresholds

### Capitalization Rules

**Capitalization Rules**

| Rule | Detail |
| --- | --- |
| Low-value asset threshold (K2/tax) | SEK 25,000 (excl. VAT) -- items below may be expensed directly (account 5400) |
| Grouping | Items forming a unit may be grouped and capitalised together even if individual cost < threshold |
| K3 component approach | Required to separate significant components with different useful lives |
| K2 simplified | No component approach; entire asset depreciated as one unit |

### Depreciation Methods

**Depreciation Methods**

| Framework | Method | Notes |
| --- | --- | --- |
| K2 | Straight-line only | No other method permitted |
| K3 | Straight-line, diminishing balance, or units-of-production | Must reflect consumption pattern |
| Tax (Räkenskapsenlig) | 30% declining balance (main rule) or 20% straight-line (5-year rule) | See below |
| Tax (Restvärdesavskrivning) | 25% declining balance | Alternative without book-tax alignment |

### Tax Depreciation -- Machinery and Equipment (Inventarier)

**Tax Depreciation -- Machinery and Equipment (Inventarier)**

| Method | Rate | Notes |
| --- | --- | --- |
| Huvudregeln (30% rule) | 30% of net book value per year | Declining balance; never fully written off |
| Kompletteringsregeln (20% rule) | 20% of acquisition cost per year | Straight-line; fully written off in 5 years |
| Immediate write-off | 100% (if < SEK 25,000 excl. VAT) | Or if expected useful life ≤ 3 years |

### Tax Depreciation -- Buildings

**Tax Depreciation -- Buildings**

| Building Type | Annual Rate |
| --- | --- |
| Industrial buildings | 4% |
| Commercial buildings | 2% |
| Office buildings | 2% |
| Residential buildings (rental) | 2% |
| Warehouse/logistics | 4% |
| Light structures (barracks, sheds) | 5% |

### Tax Depreciation -- Land Improvements

- **Land improvements depreciation rate** — 5 % per year (Rate: 5% per year of acquisition cost)

### Överavskrivningar (Excess Depreciation)

- **Excess depreciation treatment** — The difference between tax depreciation (typically higher via 30% rule) and book depreciation (straight-line per plan) is recorded in account 2150 (accumulated excess depreciation) as an untaxed reserve (obeskattad reserv).

## Section 6 -- P&L Format (Resultaträkning)

Sweden uses the "kostnadsslagsindelning" (by nature) format as standard per ÅRL. BAS is aligned to this.

### Format (Kostnadsslagsindelad -- By Nature)

```
Nettoomsättning (Net turnover)                                 xxx
Förändring av varulager (Change in inventory)                  xxx
Aktiverat arbete för egen räkning                              xxx
Övriga rörelseintäkter (Other operating income)                xxx
                                                            -------
Summa rörelseintäkter                                          xxx

Råvaror och förnödenheter (Raw materials/consumables)         (xxx)
Övriga externa kostnader (Other external expenses)            (xxx)
Personalkostnader (Staff costs)                               (xxx)
Avskrivningar (Depreciation)                                  (xxx)
Nedskrivningar (Impairment)                                   (xxx)
Övriga rörelsekostnader (Other operating expenses)            (xxx)
                                                            -------
Rörelseresultat (Operating profit/loss)                        xxx

Finansiella intäkter (Financial income)                        xxx
Finansiella kostnader (Financial costs)                       (xxx)
                                                            -------
Resultat efter finansiella poster                              xxx

Bokslutsdispositioner (Appropriations)*                       (xxx)
  - Förändring periodiseringsfond                             (xxx)
  - Förändring överavskrivningar                              (xxx)
                                                            -------
Resultat före skatt (Profit before tax)                        xxx

Skatt på årets resultat (Income tax)                          (xxx)
                                                            -------
Årets resultat (Net profit/loss)                               xxx
```

*Bokslutsdispositioner (appropriations) are a uniquely Swedish feature -- transfers to/from untaxed reserves.

## Section 7 -- Balance Sheet Format (Balansräkning)

Sweden uses the vertical format per ÅRL.

### Format

```
TILLGÅNGAR (Assets)

Anläggningstillgångar (Fixed assets)
  Immateriella anläggningstillgångar
    Goodwill                                                  xxx
    Patent och licenser                                       xxx
  Materiella anläggningstillgångar
    Byggnader och mark                                        xxx
    Maskiner och inventarier                                  xxx
  Finansiella anläggningstillgångar
    Aktier i dotterföretag                                    xxx
    Långfristiga fordringar                                   xxx
                                                           -------
  Summa anläggningstillgångar                                  xxx

Omsättningstillgångar (Current assets)
  Varulager                                                   xxx
  Kundfordringar                                              xxx
  Övriga fordringar                                           xxx
  Förutbetalda kostnader                                      xxx
  Kassa och bank                                              xxx
                                                           -------
  Summa omsättningstillgångar                                  xxx

SUMMA TILLGÅNGAR                                               xxx
                                                           =======

EGET KAPITAL OCH SKULDER (Equity and Liabilities)

Eget kapital (Equity)
  Aktiekapital                                                xxx
  Uppskrivningsfond                                           xxx
  Reservfond                                                  xxx
  Balanserat resultat                                         xxx
  Årets resultat                                              xxx
                                                           -------
  Summa eget kapital                                           xxx

Obeskattade reserver (Untaxed reserves)*
  Periodiseringsfonder                                        xxx
  Ackumulerade överavskrivningar                              xxx
                                                           -------
  Summa obeskattade reserver                                   xxx

Avsättningar (Provisions)                                     xxx

Långfristiga skulder (Long-term liabilities)
  Skulder till kreditinstitut                                 xxx
                                                           -------
  Summa långfristiga skulder                                   xxx

Kortfristiga skulder (Current liabilities)
  Leverantörsskulder                                          xxx
  Skatteskulder                                               xxx
  Övriga skulder                                              xxx
  Upplupna kostnader                                          xxx
                                                           -------
  Summa kortfristiga skulder                                   xxx

SUMMA EGET KAPITAL OCH SKULDER                                 xxx
                                                           =======
```

*Obeskattade reserver (untaxed reserves) is unique to Swedish accounting -- the portion deferred from taxation (78.4% equity, 21.6% deferred tax at current rate).

## Section 8 -- Bank Reconciliation Patterns

### Swedish Bank Statement Formats

**Swedish Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Swedbank | CSV, SIE | Datum, Text, Belopp, Saldo |
| SEB | CSV, SIE | Bokföringsdag, Text, Belopp, Saldo |
| Nordea | CSV | Datum, Transaktion, Belopp, Saldo |
| Handelsbanken | CSV | Datum, Text/Referens, Belopp, Disponibelt saldo |
| Danske Bank | CSV | Date, Description, Amount, Balance |
| Länsförsäkringar | CSV | Datum, Text, Belopp |

### SIE Format

- **SIE** — SIE (Standard Import/Export) is the Swedish standard for transferring accounting data between systems. SIE4 files contain complete bookkeeping data and can be imported by all Swedish accounting software (Fortnox, Visma, Björn Lundén, etc.).

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Classification |
| --- | --- |
| BG (Bankgiro), PG (Plusgiro) | Transfer (check direction) |
| AUTOGIRO | Direct debit (recurring expense) |
| SWISH | Mobile payment (check direction) |
| SKATTEVERKET, SKATTEKONTO | Tax payment |
| ARBETSGIVARAVG | Employer contribution payment |
| KORTKÖP, KORTTRANSAKTION | Card purchase (expense) |
| INSÄTTNING | Deposit (potential income or transfer) |
| LÖN, LÖNEUTBETALNING | Salary payment |
| HYRA, LOKALHYRA | Rent payment |
| RÄNTA | Interest (check debit/credit) |
| AVGIFT, SERVICEAVGIFT | Bank/service charges |
| FAKTURA, FAKT NR | Invoice payment (check context) |

## Section 9 -- Micro-Entity / Small Business Simplifications

### Size Categories (ÅRL Chapter 1, Section 3)

- **Smaller company definition** — A company is a "smaller company" (mindre företag) if it does NOT exceed more than one of the listed thresholds for two consecutive financial years. All others are "larger companies" (större företag).  _(ÅRL Chapter 1, Section 3)_

**Size Categories (ÅRL Chapter 1, Section 3)**  _(ÅRL Chapter 1, Section 3)_

| Criterion | Threshold |
| --- | --- |
| Average employees | 50 |
| Balance sheet total | SEK 40,000,000 |
| Net turnover | SEK 80,000,000 |

### K-Regulation Hierarchy

**K-Regulation Hierarchy**

| Category | Regulation | Who Can Use |
| --- | --- | --- |
| K1 | BFNAR 2006:1 (enskild firma) / 2010:1 (ideell) | Sole traders with turnover ≤ SEK 3M; simplified annual accounts |
| K2 | BFNAR 2016:10 | Smaller companies (AB, HB, EF) that choose simplification |
| K3 | BFNAR 2012:1 | Default for all companies preparing årsredovisning; mandatory for larger companies |
| K4 | RFR 2 (IFRS-based) | Listed companies and groups with consolidated reporting |

### K1 Simplifications (Förenklat Årsbokslut)

- **No accruals for small recurring items** — No accruals needed for recurring items < SEK 5,000
- **Revenue at invoice date** — Revenue at invoice date
- **Inventory simplified valuation** — Inventory: simplified valuation (latest purchase price × quantity)
- **Fixed asset immediate write-off threshold** — SEK 25,000 SEK (Fixed assets: immediate write-off if < SEK 25,000 (half a prisbasbelopp))
- **No formal balance sheet filing** — No formal balance sheet filing (only part of tax return NE)

### K2 Simplifications

- **Straight-line depreciation only** — Straight-line depreciation only
- **No component approach** — No component approach for assets
- **No revaluation of assets** — No revaluation of assets
- **Limited disclosures** — Limited disclosures in notes
- **No deferred tax** — No deferred tax in balance sheet
- **Intangible assets capitalisation** — Intangible assets: only acquired intangibles may be capitalised (no internally generated)
- **Accrual threshold for expenses** — SEK 7,000 SEK (Accrual threshold for expenses (from 2025 K2 update))

## Section 10 -- Interaction with Tax Skills

### Income Tax (Inkomstskatt)

- **Corporate tax rate (bolagsskatt)** — 20.6 % (For AB: corporate tax rate 20.6% (bolagsskatt))
- **Taxable income basis** — Taxable income starts from accounting result + tax adjustments
- **Key adjustments** — Key adjustments: excess depreciation (överavskrivning), allocation to periodiseringsfond (tax allocation reserve -- defer up to 25% of profit for 6 years)
- **Sole trader taxation** — For sole traders: progressive income tax on business profit (after social contributions)
- **Egenavgifter rate** — approximately 28.97 % (Egenavgifter (self-employed social contributions): approximately 28.97% of profit)
- **Schablonavdrag home office deduction** — SEK 2,000/year SEK/year (Schablonavdrag (standard deduction) available for home office: SEK 2,000/year)
- **Cross-reference** — Use the se-income-tax skill for detailed computation

### VAT (Moms)

- **VAT accounts** — VAT accounts: 2610-2650 in BAS
- **Standard and reduced VAT rates** — 25% standard; 12% (food, hotels); 6% (books, newspapers, public transport) (Standard rate: 25%; Reduced: 12% (food, hotels); 6% (books, newspapers, public transport))
- **VAT filing frequency** — Monthly filing if turnover > SEK 40M; quarterly if > SEK 1M; annual if ≤ SEK 1M
- **Cross-reference** — Use the sweden-vat-return skill for filing details

### Employer Contributions (Arbetsgivaravgifter)

- **Employer contributions rate** — 31.42 % (Rate: 31.42% of gross salary (2025))
- **Declaration and payment** — Declared and paid monthly to Skatteverket via arbetsgivardeklaration
- **Accounts used** — Recorded in accounts 7510/2731
- **Reduced contributions** — Reduced contributions for employees born 1938-2006 (different rules apply)
- **Cross-reference** — Use the se-social-contributions skill for details

### Periodiseringsfond (Tax Allocation Reserve)

- **Deferral limit** — Companies may defer up to 25% of taxable profit to a tax allocation reserve
- **Reversal period** — Must be reversed within 6 years (FIFO)
- **Accounting treatment** — Recorded as obeskattad reserv in accounts 2120-2139
- **Eligible entities** — Available for AB, enskild firma, and handelsbolag
- **Enskild firma interest charge** — Enskild firma: standard interest charge (schablonintäkt) on fund balance

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
