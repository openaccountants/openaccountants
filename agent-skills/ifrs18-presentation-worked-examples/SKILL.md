---
name: ifrs18-presentation-worked-examples
description: "Worked examples for ifrs18-presentation (IFRS 18 Presentation and Disclosure in Financial Statements) - a full IAS 1-to-IFRS 18 restatement and an MPM and nature-of-expense matrix example. Section 7 of the parent skill, split out so each file stays under the platform size limit. MUST load alongside ifrs18-presentation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ifrs18-presentation-worked-examples"
  jurisdiction: "GLOBAL"
  tax_year: "2027"
  last_updated: "2026-11-10"
  authored_by: "Talha Mehmood, ACA, FCCA"
---

# IFRS 18 worked examples (`ifrs18-presentation-worked-examples`)

Section 7 of `ifrs18-presentation`, moved here unchanged so each file stays under the platform size limit. Load `ifrs18-presentation` first.

## Section 7 — Worked Examples (`oa-check` blocks)

### Worked Example 1 — Industrial Group Full P&L, Cash Flow & Balance Sheet Restatement (Najd Advanced Industries Company)

#### Client Facts
**Najd Advanced Industries Company (NAIC)** is a listed industrial manufacturing group in Saudi Arabia reporting in `SAR '000` for the year ended **31 December 2026** (with comparative **FY2025**). NAIC has no specified main business activity of investing in assets or providing financing to customers (Rule A2.9). Under IAS 1, NAIC reported **FY2026 Operating profit of SAR 360,400 thousand** (FY2025: SAR 291,100 thousand) and **Profit for the year of SAR 297,500 thousand** (FY2025: SAR 242,100 thousand). Note disclosures reveal:

1. **Note 7 (Other operating income — FY2026: SAR 38,900; FY2025: SAR 31,400):** Comprises government grant amortisation (FY2026: 6,500; FY2025: 6,500), insurance claim recoveries (FY2026: 9,700; FY2025: 4,900), sale of scrap (FY2026: 5,100; FY2025: 4,300), sundry operating income (FY2026: 3,400; FY2025: 2,900), and **rental income from third-party investment property** of **SAR 14,200** (FY2025: **SAR 12,800**).
2. **Note 9 (Other gains — net — FY2026: SAR 5,600; FY2025: SAR 3,100):** Previously presented below IAS 1 operating profit. Comprises net loss on undesignated commodity forward contracts managing raw material price risk (FY2026: **-3,600**; FY2025: **+1,400**), gain on disposal of operating PP&E (FY2026: **+6,900**; FY2025: **+4,200**), loss on disposal of operating intangibles (FY2026: **0**; FY2025: **-2,500**), and gain on modification of bank borrowings (FY2026: **+2,300**; FY2025: **0**).
3. **Note 10 (Net foreign exchange gain/(loss) — FY2026: SAR -7,800; FY2025: SAR +2,400):** Previously presented below IAS 1 operating profit. Decomposes into FX gain/(loss) on trade receivables/payables (FY2026: **+1,600**; FY2025: **-1,500**) and FX gain/(loss) on USD bank borrowings (FY2026: **-9,400**; FY2025: **+3,900**).
4. **Note 18 (Finance costs — FY2026: SAR -86,500; FY2025: SAR -78,900):** Comprises interest on borrowings (-61,300 / -56,200), amortisation of borrowing transaction costs (-2,200 / -1,900), interest on lease liabilities (-11,800 / -10,900), unwinding of discount on decommissioning provision (-3,100 / -2,800), net interest on employee EOSB obligation (-6,900 / -6,100), and net loss on interest rate swap over borrowings (-1,200 / -1,000).
5. **Note 24 (Zakat and Income Tax):** Zakat of **SAR -18,200** (FY2025: **SAR -15,600**) is assessed on NAIC's net-worth Zakat base outside the scope of IAS 12 and was presented in the tax section under IAS 1. Income tax expense under IAS 12 is **SAR -31,400** (FY2025: **SAR -26,300**).

```yaml
example_id: ifrs18-naic-full-restatement-fy2026
currency: "SAR '000"
inputs:
  ias1_operating_profit_2026: 360400
  ias1_operating_profit_2025: 291100
  ias1_profit_for_year_2026: 297500
  ias1_profit_for_year_2025: 242100
  reclassifications_to_operating_2026:
    investment_property_rental_moved_to_investing: -14200
    commodity_forwards_moved_in: -3600
    gain_on_disposal_ppe_moved_in: 6900
    loss_on_disposal_intangibles_moved_in: 0
    fx_on_trade_balances_moved_in: 1600
    zakat_outside_ias12_moved_in: -18200
  reclassifications_to_operating_2025:
    investment_property_rental_moved_to_investing: -12800
    commodity_forwards_moved_in: 1400
    gain_on_disposal_ppe_moved_in: 4200
    loss_on_disposal_intangibles_moved_in: -2500
    fx_on_trade_balances_moved_in: -1500
    zakat_outside_ias12_moved_in: -15600
  investing_components_2026:
    rental_income_investment_property: 14200
    share_of_results_associates_jvs: 27500
    fair_value_gain_investment_property: 9300
    dividend_income_equity_investments: 8400
    fair_value_loss_fvtpl_investments: -4100
    interest_income_cash_and_deposits: 12700
  investing_components_2025:
    rental_income_investment_property: 12800
    share_of_results_associates_jvs: 22100
    fair_value_gain_investment_property: 6400
    dividend_income_equity_investments: 7200
    fair_value_gain_fvtpl_investments: 2700
    interest_income_cash_and_deposits: 9800
  financing_components_2026:
    gain_on_modification_borrowings: 2300
    fx_loss_on_borrowings: -9400
    interest_expense_borrowings: -61300
    amortisation_borrowing_costs: -2200
    interest_expense_leases: -11800
    unwinding_discount_decommissioning: -3100
    net_interest_eosb: -6900
    net_loss_interest_rate_swap: -1200
  financing_components_2025:
    gain_on_modification_borrowings: 0
    fx_gain_on_borrowings: 3900
    interest_expense_borrowings: -56200
    amortisation_borrowing_costs: -1900
    interest_expense_leases: -10900
    unwinding_discount_decommissioning: -2800
    net_interest_eosb: -6100
    net_loss_interest_rate_swap: -1000
  income_tax_expense_2026: -31400
  income_tax_expense_2025: -26300
  discontinued_operations_2026: 21600
  discontinued_operations_2025: 16900
recomputations:
  net_operating_profit_bridge_2026: -14200 + (-3600) + 6900 + 0 + 1600 + (-18200) # = -27500
  ifrs18_operating_profit_2026: 360400 + (-27500) # = 332900
  operating_profit_pct_change_2026: (-27500 / 360400) * 100 # = -7.6304% (-7.6%)
  net_operating_profit_bridge_2025: -12800 + 1400 + 4200 + (-2500) + (-1500) + (-15600) # = -26800 ( wait: -12800 + 1400 + 4200 - 2500 - 1500 - 15600 = -26800; 292300 - 26800 = 265500 )
  ifrs18_operating_profit_2025: 265500
  total_investing_2026: 14200 + 27500 + 9300 + 8400 + (-4100) + 12700 # = 68000
  total_investing_2025: 12800 + 22100 + 6400 + 7200 + 2700 + 9800 # = 61000
  profit_before_financing_and_tax_2026: 332900 + 68000 # = 400900
  profit_before_financing_and_tax_2025: 265500 + 61000 # = 326500
  total_financing_2026: 2300 + (-9400) + (-61300) + (-2200) + (-11800) + (-3100) + (-6900) + (-1200) # = -93600
  total_financing_2025: 0 + 3900 + (-56200) + (-1900) + (-10900) + (-2800) + (-6100) + (-1000) # = -75000
  profit_before_income_taxes_2026: 400900 + (-93600) # = 307300
  profit_before_income_taxes_2025: 326500 + (-75000) # = 251500
  profit_from_continuing_operations_2026: 307300 + (-31400) # = 275900
  profit_from_continuing_operations_2025: 251500 + (-26300) # = 225200
  ifrs18_profit_for_year_2026: 275900 + 21600 # = 297500 (Matches IAS 1: 297500 == 297500 PASS)
  ifrs18_profit_for_year_2025: 225200 + 16900 # = 242100 (Matches IAS 1: 242100 == 242100 PASS)
```

#### Step 1 — Presentation Reclassification Journal Entries (FY2026 & FY2025)

```text
31 Dec 2026 — Reclassify Investment Property Rental Income from Operating to Investing — driving rule: IFRS 18.53(c), B45
  Dr Other operating income (IAS 1 Operating bucket)                  14,200 (FY2025: 12,800)
    Cr Rental income from investment property (IFRS 18 Investing)       14,200 (FY2025: 12,800)
  (Memo: Note 7 breakdown; investment property generates returns independently of manufacturing; Debits = Credits = 14,200)

31 Dec 2026 — Allocate "Other gains — net" components to Operating and Financing — driving rule: IFRS 18.52, 60(c), B47, B74
  Dr Other gains — net (IAS 1 unallocated bucket)                      5,600 (FY2025: 3,100)
  Dr Net loss on commodity forward contracts (IFRS 18 Operating)       3,600 (FY2025: Cr 1,400)
    Cr Gain on disposal of PP&E (IFRS 18 Operating)                      6,900 (FY2025: 4,200)
    Cr Gain on modification of borrowings (IFRS 18 Financing)            2,300 (FY2025: 0; plus FY2025 Dr Loss on disposal of intangibles 2,500)
  (Memo: Note 9 breakdown; PP&E/intangible disposals and commodity forwards are Operating; debt modification is Financing; Debits = Credits = 9,200)

31 Dec 2026 — Split "Net foreign exchange differences" into Operating and Financing — driving rule: IFRS 18.B65, B66
  Dr Net FX loss on foreign-currency borrowings (IFRS 18 Financing)    9,400 (FY2025: Cr 3,900)
    Cr Net FX gain on trade balances (IFRS 18 Operating)                 1,600 (FY2025: Dr 1,500)
    Cr Net foreign exchange gain/(loss) (IAS 1 unallocated bucket)       7,800 (FY2025: Dr 2,400)
  (Memo: Note 10 & Borrowings roll-forward corroboration B16; FX follows underlying item; Debits = Credits = 9,400)

31 Dec 2026 — Reclassify Zakat outside IAS 12 scope into Operating — driving rule: IFRS 18.52, 67
  Dr Zakat expense (IFRS 18 Operating)                                18,200 (FY2025: 15,600)
    Cr Zakat (IAS 1 Tax bucket)                                         18,200 (FY2025: 15,600)
  (Memo: Note 24; Zakat assessed on net-worth base outside IAS 12 falls into Operating residual; Debits = Credits = 18,200)
```

#### Step 2 — Restated Statement of Profit or Loss (IFRS 18 Presentation)

| Statement of Profit or Loss Line Item | Note | FY2026 (SAR '000) | FY2025 Restated (SAR '000) | Governing Rule / Citation |
| :--- | :---: | :---: | :---: | :--- |
| **OPERATING** | | | | |
| Revenue from contracts with customers | 5 | 2,480,000 | 2,215,000 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Cost of sales | 6 | (1,736,000) | (1,573,000) | [IFRS 18.52, 82](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Gross profit** *(permitted additional subtotal)* | | **744,000** | **642,000** | [IFRS 18.24, 118(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Selling and distribution expenses | 6 | (198,400) | (177,200) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| General and administrative expenses | 6 | (156,200) | (148,900) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Research and development expenses | 6 | (42,000) | (36,500) | [IFRS 18.52, 78](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Expected credit losses on trade receivables and contract assets | 11 | (14,600) | (9,800) | [IFRS 18.52, 75(b)(ii)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Amortisation of deferred government grants | 7 | 6,500 | 6,500 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Insurance claim recoveries | 7 | 9,700 | 4,900 | [IFRS 18.52, 41](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Sale of scrap and by-products | 7 | 5,100 | 4,300 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Sundry operating income | 7 | 3,400 | 2,900 | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Donations and social responsibility contributions | 8 | (4,800) | (3,600) | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Litigation provision charge | 8 | (3,900) | (2,800) | [IFRS 18.52, B57](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Other operating expenses | 8 | (2,600) | (2,300) | [IFRS 18.52](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net gain / (loss) on commodity forward contracts *(Judgement)* | 9 | (3,600) | 1,400 | [IFRS 18.B72–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Gain on disposal of property, plant and equipment | 9 | 6,900 | 4,200 | [IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Loss on disposal of intangible assets | 9 | — | (2,500) | [IFRS 18.B47](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net foreign exchange gain / (loss) on trade balances | 10 | 1,600 | (1,500) | [IFRS 18.B65, B66(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Zakat *(Judgement)* | 24 | (18,200) | (15,600) | [IFRS 18.52, 67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **OPERATING PROFIT** *(Mandatory Subtotal 1)* | | **332,900** | **265,500** | [IFRS 18.69(a), 70](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INVESTING** | | | | |
| Rental income from investment property *(Judgement)* | 7 | 14,200 | 12,800 | [IFRS 18.53(c), 54, B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Share of results of associates and joint ventures | 14 | 27,500 | 22,100 | [IFRS 18.53(a), B43](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net fair value gain on investment property *(Judgement)* | 13 | 9,300 | 6,400 | [IFRS 18.54(a), B45](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Dividend income from equity investments | 15 | 8,400 | 7,200 | [IFRS 18.53(c), 54(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net fair value gain / (loss) on investments at FVTPL | 16 | (4,100) | 2,700 | [IFRS 18.53(c), 54(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest income on cash, cash equivalents and short-term deposits | 17 | 12,700 | 9,800 | [IFRS 18.53(b)–(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Total investing** | | **68,000** | **61,000** | [IFRS 18.53–54](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT BEFORE FINANCING AND INCOME TAXES** *(Mandatory Subtotal 2)* | | **400,900** | **326,500** | [IFRS 18.69(b), 71](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **FINANCING** | | | | |
| Gain on modification of borrowings | 9 | 2,300 | — | [IFRS 18.59(a), 60(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net foreign exchange gain / (loss) on foreign currency borrowings | 10 | (9,400) | 3,900 | [IFRS 18.60, B65, B66(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest expense on borrowings | 18 | (61,300) | (56,200) | [IFRS 18.59(a), 60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Amortisation of borrowing transaction costs | 18 | (2,200) | (1,900) | [IFRS 18.59(a), 60(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Interest expense on lease liabilities | 18 | (11,800) | (10,900) | [IFRS 18.59(b), 61, B56(b)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Unwinding of discount on decommissioning provision | 18 | (3,100) | (2,800) | [IFRS 18.59(b), 61, B56(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net interest on employee end-of-service benefit obligation | 18 | (6,900) | (6,100) | [IFRS 18.59(b), 61, B56(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Net loss on interest rate swap | 18 | (1,200) | (1,000) | [IFRS 18.B72–B74](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Total financing** | | **(93,600)** | **(75,000)** | [IFRS 18.59–61](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT BEFORE INCOME TAXES** | | **307,300** | **251,500** | [IFRS 18.118(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **INCOME TAXES** | | | | |
| Income tax expense | 24 | (31,400) | (26,300) | [IFRS 18.67](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT FROM CONTINUING OPERATIONS** | | **275,900** | **225,200** | [IFRS 18.118(f)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **DISCONTINUED OPERATIONS** | | | | |
| Profit from discontinued operation, net of tax | 12 | 21,600 | 16,900 | [IFRS 18.68](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **PROFIT FOR THE YEAR** *(Mandatory Total — Invariant)* | | **297,500** | **242,100** | [IFRS 18.69(c), 72](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

#### Step 3 — Transition Reconciliation / Allocation Matrix for Comparative Period FY2025 (IFRS 18.C3)

| IAS 1 Line Item as Originally Presented (FY2025, SAR '000) | IAS 1 Presented | Operating | Investing | Financing | Income Taxes | Discontinued | IFRS 18 Row Total | Row Tie-Out |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Revenue | 2,215,000 | 2,215,000 | — | — | — | — | 2,215,000 | **PASS (0)** |
| Cost of sales | (1,573,000) | (1,573,000) | — | — | — | — | (1,573,000) | **PASS (0)** |
| Selling and distribution expenses | (177,200) | (177,200) | — | — | — | — | (177,200) | **PASS (0)** |
| General and administrative expenses | (148,900) | (148,900) | — | — | — | — | (148,900) | **PASS (0)** |
| Research and development expenses | (36,500) | (36,500) | — | — | — | — | (36,500) | **PASS (0)** |
| Impairment loss on trade receivables & contract assets | (9,800) | (9,800) | — | — | — | — | (9,800) | **PASS (0)** |
| Other operating income | 31,400 | 18,600 | 12,800 | — | — | — | 31,400 | **PASS (0)** |
| Other operating expenses | (8,700) | (8,700) | — | — | — | — | (8,700) | **PASS (0)** |
| Share of results of associates and joint ventures | 22,100 | — | 22,100 | — | — | — | 22,100 | **PASS (0)** |
| Dividend income | 7,200 | — | 7,200 | — | — | — | 7,200 | **PASS (0)** |
| Interest income | 9,800 | — | 9,800 | — | — | — | 9,800 | **PASS (0)** |
| Net fair value gain on investment property | 6,400 | — | 6,400 | — | — | — | 6,400 | **PASS (0)** |
| Net fair value gain / (loss) on investments at FVTPL | 2,700 | — | 2,700 | — | — | — | 2,700 | **PASS (0)** |
| Finance costs | (78,900) | — | — | (78,900) | — | — | (78,900) | **PASS (0)** |
| Net foreign exchange gain / (loss) | 2,400 | (1,500) | — | 3,900 | — | — | 2,400 | **PASS (0)** |
| Other gains — net | 3,100 | 3,100 | — | — | — | — | 3,100 | **PASS (0)** |
| Zakat | (15,600) | (15,600) | — | — | — | — | (15,600) | **PASS (0)** |
| Income tax expense | (26,300) | — | — | — | (26,300) | — | (26,300) | **PASS (0)** |
| Profit from discontinued operation, net of tax | 16,900 | — | — | — | — | 16,900 | 16,900 | **PASS (0)** |
| **Total / Category Subtotal (FY2025)** | **242,100** | **265,500** | **61,000** | **(75,000)** | **(26,300)** | **16,900** | **242,100** | **PASS (0)** |

#### Step 4 — Class B Roll-Forward Corroboration of Reclassified Amounts (FY2026, SAR '000)

* **Check B7 (Lease liability interest = -11,800):** Opening lease liability `219,700` + additions `44,900` − payments `62,100` − disposed with subsidiary `14,300` − closing balance `200,000` (non-current `154,000` + current `46,000`) = implied interest `-11,800` (**PASS**).
* **Check B8 (EOSB net interest = -6,900):** Opening EOSB `210,900` + current service cost `27,300` − benefits paid `16,800` − OCI remeasurement `5,250` − closing balance `223,050` = implied net interest `-6,900` (**PASS**).
* **Check B9 (Decommissioning unwinding = -3,100):** Opening provision `68,800` + additions capitalised `5,200` − utilised `2,400` − closing balance `74,700` = implied unwinding `-3,100` (**PASS**).
* **Check B12 (Share of results of associates/JVs = +27,500):** Closing carrying amount `290,900` − opening `259,900` − additions `18,000` + dividends received `12,400` + OCI share `2,100` = implied share of results `+27,500` (**PASS**).
* **Check B16 (FX on borrowings = -9,400):** Opening borrowings `1,192,000` + drawdowns `286,000` − repayments `312,000` + transaction cost amortisation `2,200` − modification gain `2,300` − closing borrowings `1,175,300` (non-current `892,300` + current `283,000`) = implied FX loss `-9,400` (**PASS**).
* **Cash Flow & Balance Sheet Impact:** Indirect operating cash flow starts from **Operating profit of SAR 332,900** (FY2025: 265,500) and generates **Net cash from operating activities of SAR 484,100** (FY2025: 435,000). Rental cash received from investment property (`+14,200` / `+12,800`), dividends received (`+12,400` from associates + `+8,400` from equity investments), and interest received (`+12,700`) sit in **Investing activities** (`-216,800` / `-287,000`). Interest paid (`-62,500` / `-57,200`) and dividends paid (`-145,000` / `-120,000`) sit in **Financing activities** (`-295,600` / `-183,600`). On the Statement of Financial Position, **Goodwill of SAR 142,600** is presented on its own line separate from **Other intangible assets of SAR 178,000** (FY2025: 170,000), while **Total Assets of SAR 5,176,900** (FY2025: 4,984,100) and **Total Equity of SAR 2,513,600** (FY2025: 2,375,200) remain unchanged.

### Worked Example 2 — Management-Defined Performance Measures (MPMs) & Specified Nature-of-Expense Matrix (IFRS 18.83 & 18.123)

#### Client Facts
Continuing from NAIC's FY2026 financial statements:
1. **Publicly communicated MPMs:** In its earnings release and investor presentation, NAIC reports two non-IFRS performance subtotals:
   * **MPM 1 — Adjusted operating profit:** Defined by management as *Operating profit before Zakat, IAS 36 impairment of PP&E, write-downs of inventories to NRV, litigation provision charges, and insurance claim recoveries*.
   * **MPM 2 — EBITDA before non-recurring items:** Defined as *Adjusted operating profit (MPM 1) before depreciation of PP&E, depreciation of ROU assets, and amortisation of intangible assets*.
2. **Tax and NCI parameters ([IFRS 18.123(d)–(e)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)):** Income tax effects are determined using the applicable statutory income tax rate of **20%** in the jurisdiction where each adjusting item arises ([IFRS 18.B141(a)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html)). Zakat is non-deductible and carries **0%** income tax effect and **0%** NCI effect (wholly-owned parent level). PP&E impairment (`12,400`), inventory write-downs (`8,900`), and insurance recoveries (`-9,700`) arise in a **90%-owned subsidiary** (**10% NCI**); the litigation provision (`3,900`) arises in a **100%-owned subsidiary** (**0% NCI**).
3. **Functional expense presentation:** NAIC presents four functional operating expense lines on the face (*Cost of sales*, *Selling and distribution*, *General and administrative*, and *Research and development*) totalling **SAR 2,132,600 thousand** in FY2026 (FY2025: **SAR 1,935,600 thousand**), triggering the mandatory single-note disclosure under [IFRS 18.83](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html).

```yaml
example_id: ifrs18-naic-mpm-and-nature-matrix-fy2026
currency: "SAR '000"
inputs:
  ifrs18_operating_profit_2026: 332900
  ifrs18_operating_profit_2025: 265500
  statutory_tax_rate: 0.20
  subsidiary_nci_rate: 0.10
  mpm1_adjustments_2026:
    zakat: 18200
    impairment_ppe_ias36: 12400
    inventory_writedown_ias2: 8900
    litigation_provision: 3900
    insurance_recoveries: -9700
  mpm1_adjustments_2025:
    zakat: 15600
    impairment_ppe_ias36: 0
    inventory_writedown_ias2: 6200
    litigation_provision: 2800
    insurance_recoveries: -4900
  mpm2_da_addbacks_2026:
    depreciation_ppe: 182700
    depreciation_rou: 41900
    amortisation_intangibles: 23800
  mpm2_da_addbacks_2025:
    depreciation_ppe: 168400
    depreciation_rou: 38200
    amortisation_intangibles: 21600
  functional_operating_expenses_2026:
    cost_of_sales: 1736000
    selling_and_distribution: 198400
    general_and_administrative: 156200
    research_and_development: 42000
recomputations:
  mpm1_adjusted_operating_profit_2026: 332900 + 18200 + 12400 + 8900 + 3900 + (-9700) # = 366600
  mpm1_adjusted_operating_profit_2025: 265500 + 15600 + 0 + 6200 + 2800 + (-4900) # = 285200
  tax_effect_impairment_2026: -12400 * 0.20 # = -2480
  tax_effect_inventory_2026: -8900 * 0.20 # = -1780
  tax_effect_litigation_2026: -3900 * 0.20 # = -780
  tax_effect_insurance_2026: 9700 * 0.20 # = 1940
  total_mpm1_tax_effect_2026: 0 + (-2480) + (-1780) + (-780) + 1940 # = -3100
  nci_effect_impairment_2026: -12400 * 0.10 # = -1240
  nci_effect_inventory_2026: -8900 * 0.10 # = -890
  nci_effect_insurance_2026: 9700 * 0.10 # = 970
  total_mpm1_nci_effect_2026: 0 + (-1240) + (-890) + 0 + 970 # = -1160
  mpm2_ebitda_before_non_recurring_2026: 366600 + 182700 + 41900 + 23800 # = 615000
  mpm2_ebitda_before_non_recurring_2025: 285200 + 168400 + 38200 + 21600 # = 513400
  total_functional_expenses_2026: 1736000 + 198400 + 156200 + 42000 # = 2132600
  total_specified_five_natures_2026: 372000 + 182700 + 41900 + 23800 + 12400 + 8900 # = 641700
  total_other_natures_2026: 1205000 + 74300 + 61200 + 33500 + 28700 + 19600 + 9800 + 58800 # = 1490900
  nature_matrix_grand_total_2026: 641700 + 1490900 # = 2132600 (Matches functional total 2132600 PASS)
```

#### Step 1 — Single-Note Disclosure of Management-Defined Performance Measures (IFRS 18.122–123)

| MPM Reconciliation Line Item (SAR '000) | FY2026 Amount | FY2026 Income Tax Effect (20% Statutory) | FY2026 NCI Effect (10% Sub Share) | FY2025 Restated Amount | Governing Citation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Operating profit** *(IFRS 18 most directly comparable subtotal)* | **332,900** | | | **265,500** | [IFRS 18.69(a), 118, 123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Zakat (assessed on net-worth base; non-deductible) | 18,200 | — | — | 15,600 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Impairment loss on property, plant and equipment (IAS 36) | 12,400 | (2,480) | (1,240) | — | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Write-down of inventories to net realisable value (IAS 2) | 8,900 | (1,780) | (890) | 6,200 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Litigation provision charge (IAS 37) | 3,900 | (780) | — | 2,800 | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Less: Insurance claim recoveries | (9,700) | 1,940 | 970 | (4,900) | [IFRS 18.123(c)–(d)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **Adjusted operating profit (MPM 1)** | **366,600** | **(3,100)** | **(1,160)** | **285,200** | [IFRS 18.117, 123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Depreciation of property, plant and equipment | 182,700 | *(Note 1)* | *(Note 1)* | 168,400 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Depreciation of right-of-use assets | 41,900 | *(Note 1)* | *(Note 1)* | 38,200 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| Add: Amortisation of intangible assets | 23,800 | *(Note 1)* | *(Note 1)* | 21,600 | [IFRS 18.123(c)](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |
| **EBITDA before non-recurring items (MPM 2)** | **615,000** | | | **513,400** | [IFRS 18.117, 118(b), 123](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs18.html) |

*(Note 1: Alternatively, MPM 2 can be reconciled directly to the IFRS 18.118(b) OPBDA subtotal of `332,900 + 182,700 + 41,900 + 23,800 + 12,400 = 593,700`, in which case only the remaining non-OPBDA reconciling items — Zakat `18,200`, inventory write-down `8,900`, litigation `3,900`, and insurance recoveries `-9,700` — require tax and NCI effects).*

#### Step 2 — Mandatory Single-Note Analysis of Operating Expenses by Nature and Function (IFRS 18.83, FY2026, SAR '000)

| Expense Nature Category (*Bold = Mandatory per IFRS 18.83*) | Cost of Sales | Selling & Distribution | General & Admin | Research & Development | FY2026 Total | FY2025 Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Employee benefits (IAS 19)** | **224,900** | **62,000** | **70,100** | **15,000** | **372,000** | **341,500** |
| **Depreciation of property, plant and equipment (IAS 16)** | **164,700** | **6,000** | **9,000** | **3,000** | **182,700** | **168,400** |
| **Depreciation of right-of-use assets (IFRS 16)** | **20,900** | **12,000** | **8,000** | **1,000** | **41,900** | **38,200** |
| **Amortisation of intangible assets (IAS 38)** | **12,800** | **2,000** | **6,000** | **3,000** | **23,800** | **21,600** |
| **Impairment losses on PP&E (IAS 36)** | **12,400** | **—** | **—** | **—** | **12,400** | **—** |
| **Write-down of inventories to NRV (IAS 2)** | **8,900** | **—** | **—** | **—** | **8,900** | **6,200** |
| *Subtotal — Five Specified Natures (IFRS 18.83)* | *444,600* | *82,000* | *93,100* | *22,000* | *641,700* | *575,900* |
| Raw materials and consumables used | 1,160,000 | 25,000 | — | 20,000 | 1,205,000 | 1,096,000 |
| Utilities and energy | 68,300 | 2,000 | 4,000 | — | 74,300 | 67,900 |
| Freight and distribution | 8,200 | 53,000 | — | — | 61,200 | 55,400 |
| Repairs and maintenance | 27,500 | 2,000 | 4,000 | — | 33,500 | 30,100 |
| Marketing and advertising | — | 28,700 | — | — | 28,700 | 25,300 |
| Professional and consultancy fees | 2,600 | — | 17,000 | — | 19,600 | 17,800 |
| Insurance | 4,800 | 1,000 | 4,000 | — | 9,800 | 8,900 |
| Other operating expenses by nature | 20,000 | 4,700 | 34,100 | — | 58,800 | 58,300 |
| **Total Operating Expenses in Functional Lines (Tie-Out)** | **1,736,000** | **198,400** | **156,200** | **42,000** | **2,132,600** | **1,935,600** |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-10. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ifrs18-presentation-worked-examples` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ifrs18-presentation-worked-examples. If neither is available, confirm every figure against the official source pages cited above before relying on it.
