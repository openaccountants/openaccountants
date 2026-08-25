---
name: netherlands-bookkeeping
description: Use this skill whenever asked about Dutch bookkeeping, chart of accounts, financial statements, RGS mapping, jaarrekening preparation, balance sheet or P&L format in the Netherlands. Trigger on phrases like "Dutch bookkeeping", "boekhouding", "grootboekrekening", "jaarrekening", "RGS", "chart of accounts Netherlands", "balans", "winst- en verliesrekening", "micro-entity Netherlands", "BW2 Title 9", "Dutch GAAP", "RJ guidelines", "small company accounts NL", "annual accounts Netherlands", or any question about recording transactions, financial reporting, or accounting standards for Dutch entities.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Currency | EUR |
| Financial year | Flexible (most common: 1 January -- 31 December) |
| Accounting standards | Dutch GAAP (BW2 Title 9); RJ Guidelines (Raad voor de Jaarverslaggeving) |
| Standard chart of accounts | RGS (Referentie GrootboekSchema) -- voluntary reference standard |
| Governing body | Raad voor de Jaarverslaggeving (RJ); Belastingdienst (tax) |
| Key legislation | Burgerlijk Wetboek Boek 2, Titel 9 (BW2 Title 9) |
| Filing obligation | KVK (Kamer van Koophandel) -- within 12 months of year-end |
| Tax authority | Belastingdienst |
| Reporting format | SBR/XBRL for KVK and Belastingdienst filings |

## Section 2 -- Standard Chart of Accounts (RGS-Based)

The RGS (Referentie GrootboekSchema) is not mandatory but is the de facto Dutch standard used by most accounting software. Below is a practical mapping for small/micro entities.

### Assets (Class 0-1)

**Assets (Class 0-1)**

| Code | Account | Description |
| --- | --- | --- |
| 0100 | Immateriële vaste activa | Intangible fixed assets |
| 0110 | Goodwill | Goodwill |
| 0120 | Software | Software licences |
| 0200 | Materiële vaste activa | Tangible fixed assets |
| 0210 | Gebouwen | Buildings |
| 0220 | Machines en installaties | Machinery and installations |
| 0230 | Inventaris | Furniture and fittings |
| 0240 | Computers | Computer hardware |
| 0250 | Vervoermiddelen | Vehicles |
| 0900 | Cum. afschrijvingen | Accumulated depreciation |
| 1100 | Debiteuren | Trade receivables |
| 1200 | Overige vorderingen | Other receivables |
| 1300 | Voorraad | Inventory |
| 1500 | Vooruitbetaalde kosten | Prepaid expenses |
| 1800 | Kruisposten | Inter-account transfers |
| 1900 | Bank | Bank accounts |
| 1910 | Kas | Cash |

### Liabilities (Class 2)

**Liabilities (Class 2)**

| Code | Account | Description |
| --- | --- | --- |
| 2000 | Crediteuren | Trade payables |
| 2100 | Belastingen en premies | Taxes and social premiums payable |
| 2110 | Omzetbelasting (BTW) | VAT payable |
| 2120 | Loonheffingen | Payroll taxes payable |
| 2200 | Overige schulden | Other payables |
| 2300 | Leningen langlopend | Long-term loans |
| 2400 | Voorzieningen | Provisions |

### Equity (Class 0/3)

**Equity (Class 0/3)**

| Code | Account | Description |
| --- | --- | --- |
| 0500 | Eigen vermogen | Equity |
| 0510 | Aandelenkapitaal | Share capital (BV) |
| 0520 | Agioreserve | Share premium |
| 0530 | Overige reserves | Other reserves |
| 0590 | Resultaat lopend jaar | Current year result |
| 0595 | Privé (eenmanszaak) | Owner's drawings (sole trader) |

### Revenue (Class 8)

**Revenue (Class 8)**

| Code | Account | Description |
| --- | --- | --- |
| 8000 | Netto-omzet | Net turnover |
| 8010 | Omzet diensten | Revenue from services |
| 8020 | Omzet handel | Revenue from goods |
| 8100 | Overige bedrijfsopbrengsten | Other operating income |

### Cost of Goods Sold (Class 7)

**Cost of Goods Sold (Class 7)**

| Code | Account | Description |
| --- | --- | --- |
| 7000 | Inkoopwaarde omzet | Cost of goods sold |
| 7010 | Inkopen | Purchases |
| 7020 | Voorraadmutatie | Inventory change |

### Operating Expenses (Class 4-6)

**Operating Expenses (Class 4-6)**

| Code | Account | Description |
| --- | --- | --- |
| 4000 | Personeelskosten | Staff costs |
| 4010 | Lonen en salarissen | Wages and salaries |
| 4020 | Sociale lasten | Social security contributions |
| 4030 | Pensioenlasten | Pension costs |
| 4100 | Afschrijvingen | Depreciation |
| 4200 | Huisvestingskosten | Premises costs |
| 4210 | Huur | Rent |
| 4220 | Gas, water, elektra | Utilities |
| 4300 | Verkoopkosten | Selling expenses |
| 4310 | Reclame en marketing | Advertising and marketing |
| 4400 | Autokosten | Vehicle costs |
| 4500 | Kantoorkosten | Office costs |
| 4510 | Telefoon en internet | Telecoms |
| 4520 | Kantoorbenodigdheden | Office supplies |
| 4530 | Software abonnementen | Software subscriptions |
| 4600 | Algemene kosten | General costs |
| 4610 | Accountantskosten | Accountancy fees |
| 4620 | Advieskosten | Advisory/legal fees |
| 4630 | Bankkosten | Bank charges |
| 4640 | Verzekeringen | Insurance |
| 4650 | Contributies en abonnementen | Subscriptions |

### Other Income/Expenses (Class 8/9)

**Other Income/Expenses (Class 8/9)**

| Code | Account | Description |
| --- | --- | --- |
| 8200 | Financiële baten | Financial income (interest received) |
| 8300 | Financiële lasten | Financial expenses (interest paid) |
| 8400 | Buitengewone baten | Extraordinary income |
| 8500 | Buitengewone lasten | Extraordinary expenses |

### Tax (Class 9)

**Tax (Class 9)**

| Code | Account | Description |
| --- | --- | --- |
| 9000 | Vennootschapsbelasting | Corporate income tax |
| 9010 | Latente belastingen | Deferred taxes |

### Cash vs Accrual Basis

**Cash vs Accrual Basis**

| Entity Type | Basis | Notes |
| --- | --- | --- |
| BV / NV (legal entity) | Accrual (verplicht) | BW2 Title 9 requires accrual basis |
| Eenmanszaak / VOF (sole trader / partnership) | Accrual or Cash | Tax law allows "kasstelsel" for certain small traders; most use accrual |
| ZZP (freelancer) | Accrual | Recommended; required if VAT-registered on standard scheme |

### Key Rules

- **Revenue recognition timing** — Revenue recognised when goods/services delivered and collectability is reasonably assured (RJ 270)  _(RJ 270)_
- **Construction contracts method** — Construction contracts: percentage-of-completion method preferred (RJ 221)  _(RJ 221)_
- **Long-term service contracts** — Long-term service contracts: revenue allocated over the period of service delivery
- **Goed koopmansgebruik** — For IB (inkomstenbelasting) purposes, "goed koopmansgebruik" (sound business practice) governs timing

### Thresholds

- **Cash/accrual switching threshold** — No statutory threshold for switching between cash/accrual for sole traders
- **KOR (Kleineondernemersregeling) turnover threshold** — EUR 20,000/year EUR (exempts from VAT filing but requires standard bookkeeping)

### Deductible Operating Expenses

**Deductible Operating Expenses**

| Category | Nominal Code | Deductibility |
| --- | --- | --- |
| Office rent | 4210 | 100% deductible |
| Utilities (business premises) | 4220 | 100% deductible |
| Accountancy fees | 4610 | 100% deductible |
| Software subscriptions | 4530 | 100% deductible |
| Professional insurance | 4640 | 100% deductible |
| Marketing/advertising | 4310 | 100% deductible |
| Travel (business) | 4400 | 100% deductible if wholly business |
| Training/education | 4600 | 100% deductible if business-related |
| Bank charges | 4630 | 100% deductible |
| Phone/internet (business %) | 4510 | Business portion only |

### Limited/Non-Deductible Expenses (Fiscal)

**Limited/Non-Deductible Expenses (Fiscal)**

| Category | Limitation |
| --- | --- |
| Business meals/entertainment | 80% deductible (20% non-deductible add-back) |
| Gifts to clients | 80% deductible if > EUR 15/gift |
| Fines and penalties | 0% -- never deductible |
| Personal expenses | 0% -- never deductible |
| Income tax / VPB | 0% -- never deductible |
| Private use of business assets | Add-back required (bijtelling for cars) |

### Car (Auto) Special Rules

- **Company car private-use addition (bijtelling) standard** — 22% % of catalogue value (standard)
- **Company car private-use addition (bijtelling) zero-emission** — 16% % of catalogue value (zero-emission vehicles)
- **Kilometre allowance for business use of private car** — EUR 0.23 EUR/km (2025)

### Capitalization Rules

**Capitalization Rules**

| Rule | Threshold | Notes |
| --- | --- | --- |
| Tax depreciation maximum rate | 20% per year on cost | Minimum 5-year useful life |
| Goodwill maximum rate | 10% per year | Minimum 10-year amortization |
| Low-value asset expensing | No statutory threshold | Practice: items < EUR 450 often expensed directly |
| Real estate floor (bodemwaarde) | WOZ-value | Cannot depreciate below WOZ-value for tax |
| Buildings (beleggingspand) | Max 100% WOZ-value | Investment property: cannot depreciate below 100% WOZ |
| Buildings (own use) | Max 50% WOZ-value | Own-use property: floor is 50% of WOZ-value |

### Depreciation Methods and Rates

**Depreciation Methods and Rates**

| Asset Type | Method | Common Tax Rate |
| --- | --- | --- |
| Buildings (own use) | Straight-line | 2-3% (floor: 50% WOZ) |
| Buildings (investment) | Straight-line | 2-3% (floor: 100% WOZ) |
| Machinery and equipment | Straight-line | 10-20% |
| Office furniture/fittings | Straight-line | 20% |
| Computer hardware | Straight-line | 20% (max allowed) |
| Software | Straight-line | 20% |
| Vehicles | Straight-line | 20% |
| Goodwill | Straight-line | 10% |

### Small-Scale Investment Deduction (KIA)

- **KIA deduction** — For investments between EUR 2,801 and EUR 393,252 (2025), an additional percentage deduction (up to 28%) of the investment amount is available on top of regular depreciation.

## Section 6 -- P&L Format (Winst- en Verliesrekening)

Dutch law prescribes the income statement classified by nature of expense (categoriale model) or by function (functionele model). Small entities typically use nature-of-expense.

### Format (Categoriale Model -- by Nature)

Netto-omzet (Net turnover)                                    xxx
Wijziging voorraad (Change in inventory)                      xxx
Overige bedrijfsopbrengsten (Other operating income)          xxx
                                                           -------
Totale bedrijfsopbrengsten                                    xxx

Grondstof-/hulpmateriaalkosten (Raw materials)               (xxx)
Personeelskosten (Staff costs)                               (xxx)
Afschrijvingen (Depreciation/amortisation)                   (xxx)
Overige bedrijfskosten (Other operating expenses)            (xxx)
                                                           -------
Totale bedrijfslasten                                        (xxx)

Bedrijfsresultaat (Operating profit)                          xxx

Financiële baten (Financial income)                           xxx
Financiële lasten (Financial expenses)                       (xxx)
                                                           -------
Resultaat voor belastingen (Profit before tax)                 xxx

Belastingen (Tax)                                            (xxx)
                                                           -------
Resultaat na belastingen (Net profit)                          xxx

## Section 7 -- Balance Sheet Format (Balans)

Dutch law prescribes a vertical (staffelvorm) balance sheet format. Small entities file an abbreviated version.

### Format

ACTIVA (Assets)

Vaste activa (Fixed assets)
  Immateriële vaste activa                                    xxx
  Materiële vaste activa                                      xxx
  Financiële vaste activa                                     xxx
                                                           -------
  Totaal vaste activa                                         xxx

Vlottende activa (Current assets)
  Voorraden                                                   xxx
  Vorderingen                                                 xxx
  Liquide middelen                                            xxx
                                                           -------
  Totaal vlottende activa                                     xxx

TOTAAL ACTIVA                                                 xxx
                                                           =======

PASSIVA (Equity and Liabilities)

Eigen vermogen (Equity)
  Aandelenkapitaal                                            xxx
  Reserves                                                    xxx
  Onverdeeld resultaat                                        xxx
                                                           -------
  Totaal eigen vermogen                                       xxx

Voorzieningen (Provisions)                                    xxx

Langlopende schulden (Long-term liabilities)                  xxx

Kortlopende schulden (Current liabilities)                    xxx
                                                           -------
TOTAAL PASSIVA                                                xxx
                                                           =======

### Dutch Bank Statement Formats

**Dutch Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| ING | CSV, MT940 | Date, Name/Description, Account, Counter-account, Amount, Balance |
| ABN AMRO | CSV, MT940 | Transaction date, Amount, Description, Counter-party IBAN |
| Rabobank | CSV, MT940, CAMT.053 | Date, Counter-party name, IBAN, Amount, Description |
| SNS/RegioBank | CSV | Date, Description, Debit, Credit, Balance |
| Bunq | CSV | Date, Amount, Account, Counterparty, Description |
| Knab | CSV | Date, Amount, Name, Description, IBAN |

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Classification |
| --- | --- |
| SEPA Overboeking, Betaling aan | Outgoing payment (expense or transfer) |
| SEPA Incasso, Automatische incasso | Direct debit (recurring expense) |
| iDEAL betaling | Incoming payment from customer |
| Tikkie | Small payment (check direction) |
| BELASTINGDIENST, BTW, LH | Tax payment (exclude from P&L) |
| KVK, Kamer van Koophandel | Business registration fee |
| PENSIOENFONDS | Pension contribution |
| Pinbetaling, Geldautomaat | Card/ATM (check nature) |

### Size Categories (from 1 January 2024)

**Size Categories (from 1 January 2024)**

| Category | Balance Sheet Total | Net Turnover | Employees |
| --- | --- | --- | --- |
| Micro | ≤ EUR 450,000 | ≤ EUR 900,000 | < 10 |
| Small (Klein) | ≤ EUR 7,500,000 | ≤ EUR 15,000,000 | < 50 |
| Medium (Middelgroot) | ≤ EUR 25,000,000 | ≤ EUR 50,000,000 | < 250 |

- **Two of three criteria rule** — Must meet at least 2 of 3 criteria on two consecutive balance sheet dates.

### Simplifications by Category

**Simplifications by Category**

| Simplification | Micro | Small |
| --- | --- | --- |
| P&L required in filing | No | No |
| Management report (bestuursverslag) | Not required | Not required |
| Statutory audit | Not required | Not required |
| Consolidated accounts | Not required | Not required |
| Notes (toelichting) | Very limited | Limited |
| Use tax accounting principles | Allowed (Art. 2:396 lid 6) | Allowed |
| File abbreviated balance sheet only | Yes | Yes (with limited notes) |
| Cash flow statement | Not required | Not required |

### Sole Trader (Eenmanszaak) / ZZP

- **No formal annual accounts obligation** — No formal annual accounts obligation under BW2 Title 9  _(BW2 Title 9)_
- **Record retention obligation** — Must maintain adequate records for tax (bewaarplicht: 7 years)
- **Annual income tax return** — Annual income tax return (aangifte IB) with balance sheet and P&L
- **VAT return frequency** — VAT return quarterly (or monthly for larger traders)
- **Small Businesses Scheme (KOR) turnover threshold** — EUR 20,000 EUR (full VAT exemption)

## Section 10 -- Interaction with Tax Skills

### Income Tax (IB/VPB)

- **Jaarrekening as basis for tax return** — The jaarrekening (annual accounts) forms the basis for the tax return
- **Fiscal adjustments outside accounts** — Fiscal adjustments are made outside the accounts (e.g., entertainment 20% add-back, KIA deduction, MKB profit exemption)
- **Fiscal accounting principles for micro/small entities** — Micro/small entities may use fiscal accounting principles for their jaarrekening, eliminating most differences
- **Zelfstandigenaftrek** — EUR 3,750 EUR (2025)
- **Startersaftrek** — EUR 2,123 EUR
- **MKB-winstvrijstelling** — 13.31% % of profit

### VAT (BTW)

- **VAT recording** — VAT is recorded in account 2110 (payable) and cleared via the BTW-aangifte
- **Input VAT tracking** — Input VAT (voorbelasting) is tracked separately and offset against output VAT
- **Private-use correction** — Private-use correction (privégebruik correctie) due in final period
- **Cross-reference for BTW filing** — Use the netherlands-vat-return skill for BTW filing details

### Payroll Tax (Loonheffingen)

- **Loonheffingen composition** — Loonheffingen includes wage tax + social insurance premiums
- **Recording until remitted** — Recorded in account 2120 until remitted to Belastingdienst
- **Cross-reference for payroll calculation** — Use the nl-payroll-tax skill for detailed calculation

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
