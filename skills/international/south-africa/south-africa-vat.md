---
name: south-africa-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a South Africa VAT return (VAT201), classify transactions for South African VAT purposes, or advise on VAT registration and filing in South Africa. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "input tax South Africa", "output tax South Africa", "South African Revenue Service VAT", or any SA VAT request. ALWAYS read this skill before touching any South Africa VAT work.
version: 2.0
jurisdiction: ZA
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# South Africa VAT (VAT201) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | South Africa (Republic of South Africa) |
| Tax | VAT (Value-Added Tax) |
| Currency | ZAR (South African Rand / R) |
| Tax year | Tax period (bi-monthly for most; monthly for large vendors; quarterly/annual for small) |
| Standard rate | 15% |
| Zero rate | 0% (exports; basic foodstuffs; international transport; certain farming inputs; petrol/diesel; residential accommodation on long-term letting by developers; certain financial instruments) |
| Exempt | Financial services (lending, insurance), residential rental, public transport by road/rail |
| Registration threshold | ZAR 1,000,000 per 12-month period |
| Tax authority | SARS (South African Revenue Service) |
| Return form | VAT201 (eFiling) |
| Filing portal | SARS eFiling (https://efiling.sars.gov.za) |
| Filing frequencies | Monthly (>ZAR 30M/year); Bi-monthly (most vendors); Quarterly/Semi-annual/Annual (approved small vendors) |
| Filing deadline | Last business day of month following tax period (eFiling); 25th for paper (not recommended) |
| Tax invoice | VAT-compliant invoice — required for input tax |
| VAT number | Format: 4xxxxxxxx (10 digits starting with 4) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a South African CA(SA) or registered tax practitioner |
| Skill version | 2.0 |

### Key VAT201 fields

| Field | Meaning |
|---|---|
| Field 1 | Standard-rated supplies (output tax base at 15%) |
| Field 1A | Output tax at 15% (Field 1 × 15/115) |
| Field 2 | Zero-rated supplies |
| Field 3 | Exempt supplies |
| Field 4 | Total supplies (1+2+3) |
| Field 5 | Total output tax (Field 1A) |
| Field 10 | Input tax — standard-rated purchases |
| Field 11 | Input tax — imported goods/services |
| Field 12 | Total input tax (10+11) |
| Field 13 | Net VAT payable/refundable (5−12) |
| Field 14 | VAT refund requested (if 12 > 5) |
| Field 15 | VAT payable (if 5 > 12) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% standard |
| Unknown counterparty country | Domestic South Africa |
| Unknown export qualification | 15% until export evidence confirmed |
| Unknown business-use % (vehicle, entertainment) | 0% input tax |
| Unknown whether tax invoice compliant | No input tax |
| Unknown whether zero-rated or exempt | Treat as taxable 15% |
| Unknown B2B vs B2C for cross-border | 15% if consumed in South Africa |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | ZAR 50,000 |
| HIGH tax delta on single default | ZAR 7,500 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | ZAR 30,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the tax period in CSV, PDF, or pasted text. VAT registration number (starting with 4).

**Recommended** — tax invoices for all input tax claims above ZAR 5,000, sales invoices for all output, prior period excess credit (Field 14).

**Ideal** — complete creditors/debtors ledger, import VAT certificates (SAD500), asset register, prior VAT201 return.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input tax credits require a valid VAT tax invoice per Section 20 of the VAT Act. All credits are provisional pending invoice verification."

### Refusal catalogue

**R-ZA-1 — Non-VAT-registered vendor.** "Only registered vendors can charge VAT and claim input tax. Confirm VAT registration before proceeding."

**R-ZA-2 — Partial exemption / apportionment.** "If the vendor makes both taxable and exempt supplies, input tax must be apportioned under Section 17(1) of the VAT Act. The apportionment ratio changes annually — out of scope without full-year data. Escalate to a CA(SA)."

**R-ZA-3 — Capital goods scheme (Section 18A).** "Adjustments to input tax on capital goods where use changes between taxable and non-taxable purposes require specialist computation. Out of scope."

**R-ZA-4 — Financial services (Section 2).** "Financial services have complex VAT treatment. Banks, insurers, and financial institutions require specialist handling. Out of scope."

**R-ZA-5 — Property transactions.** "Property development, sale of commercial property, and option-to-tax elections are highly fact-sensitive. Escalate to specialist."

---

## Section 3 — Supplier pattern library

### 3.1 South African banks — fees (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ABSA BANK, ABSA GROUP | EXCLUDE (fee lines) | Financial service — VAT exempt |
| STANDARD BANK, STANBIC | EXCLUDE (fee lines) | Same |
| FIRSTRAND, FNB, FIRST NATIONAL BANK | EXCLUDE (fee lines) | Same |
| NEDBANK | EXCLUDE (fee lines) | Same |
| CAPITEC BANK | EXCLUDE (fee lines) | Same |
| INVESTEC | EXCLUDE (fee lines) | Same |
| AFRICAN BANK | EXCLUDE (fee lines) | Same |
| BANK CHARGES, SERVICE FEE, INTEREST | EXCLUDE | Bank fee/interest — exempt |

### 3.2 South African government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SARS, SOUTH AFRICAN REVENUE SERVICE | EXCLUDE | Tax payment |
| UIF, UNEMPLOYMENT INSURANCE FUND | EXCLUDE | Statutory contribution |
| WORKMEN'S COMP, COIDA | EXCLUDE | Compensation fund |
| MUNICIPALITY, LOCAL AUTHORITY (rates) | EXCLUDE | Rates and taxes — outside VAT scope |
| ROAD ACCIDENT FUND, RAF | EXCLUDE | Statutory levy |

### 3.3 South African utilities (taxable at 15%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| ESKOM | Input 15% | 15% | National electricity — taxable |
| CITY POWER (Johannesburg) | Input 15% | 15% | Municipal electricity — taxable |
| CAPE TOWN ELECTRICITY | Input 15% | 15% | Municipal electricity — taxable |
| RAND WATER, RAND WATER BOARD | Input 15% | 15% | Water — taxable |
| CITY OF CAPE TOWN WATER | Input 15% | 15% | Water — taxable |
| VODACOM | Input 15% | 15% | Mobile/internet — taxable |
| MTN SOUTH AFRICA | Input 15% | 15% | Mobile — taxable |
| CELL C | Input 15% | 15% | Mobile — taxable |
| TELKOM SA | Input 15% | 15% | Fixed-line/internet — taxable |
| RAIN NETWORK | Input 15% | 15% | Internet — taxable |
| AFRIHOST | Input 15% | 15% | Internet — taxable |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| SOUTH AFRICAN AIRWAYS, SAA | Check route | 0%/15% | International 0%; domestic 15% |
| FLYSAFAIR | Input 15% | 15% | Domestic airline — 15% |
| AIRLINK | Check route | 0%/15% | International 0%; domestic 15% |
| KULULA.COM | Input 15% | 15% | Domestic — 15% |
| UBER SOUTH AFRICA | Input 15% | 15% | Ride-hailing — taxable |
| BOLT SOUTH AFRICA | Input 15% | 15% | Ride-hailing — taxable |
| DHL SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| FEDEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| DAWN WING | Input 15% | 15% | Courier — taxable |
| THE COURIER GUY, TCG | Input 15% | 15% | Courier — taxable |
| ARAMEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| CHECKERS, SHOPRITE | Input 15%/0% | Mixed | Basic zero-rated food items; non-food 15% |
| PICK N PAY, PNP | Input 15%/0% | Mixed | Same — zero-rate basic foodstuffs |
| WOOLWORTHS FOOD | Input 15%/0% | Mixed | Food hall: basic items 0%; prepared/luxury food 15% |
| SPAR | Input 15%/0% | Mixed | Same |
| FOOD LOVERS MARKET | Input 15%/0% | Mixed | Same |
| CLICKS | Input 15% | 15% | Health/beauty retail — 15% |
| DIS-CHEM | Input 15% (OTC)/0% (prescription exemption) | Mixed | Prescription meds exempt; others 15% |
| MCDONALD'S SA, STEERS, NANDO'S | Input 15% | 15% | Fast food/restaurant — 15% (no zero-rate for prepared food) |

**Note on zero-rated basic foodstuffs:** Brown bread, maize meal, mielie rice, dried mealies, dried beans, lentils, pilchards/sardines in tins, milk, eggs, fruits and vegetables, vegetable oil, edible legumes. These are zero-rated under Schedule 2 of the VAT Act.

### 3.6 SaaS — international suppliers (reverse charge / imported services)

Under VAT Act Section 7(1)(c), imported services from abroad are subject to VAT if the recipient is a non-vendor or partially exempt vendor. For fully taxable vendors, VAT on imported services can be claimed back as input tax in the same period — net effect zero.

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | Imported services — self-assess 15% | Output and input in same period (net zero for fully taxable) |
| MICROSOFT (365, Azure) | Imported services — self-assess 15% | Same |
| META, FACEBOOK ADS | Imported services — self-assess 15% | Same |
| ZOOM, SLACK | Imported services — self-assess 15% | Same |
| NOTION, OPENAI, ANTHROPIC | Imported services — self-assess 15% | Same |
| AWS | Imported services — self-assess 15% | Same |
| XERO (if billed from NZ) | Imported services — self-assess 15% | Same |
| SAGE (if billed from UK) | Imported services — self-assess 15% | Same |

### 3.7 Local SaaS and professional tools (15%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| XERO (South Africa entity) | Input 15% | 15% | Accounting software |
| SAGE SOUTH AFRICA | Input 15% | 15% | Accounting/payroll |
| PASTEL, SAGE PASTEL | Input 15% | 15% | South African accounting |
| QUICKBOOKS SOUTH AFRICA | Input 15% | 15% | Accounting SaaS |

### 3.8 Payment processors (exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| PAYFAST (transaction fees) | EXCLUDE | Financial service — exempt |
| YOCO (transaction fees) | EXCLUDE | Payment processing — exempt |
| PEACH PAYMENTS (fees) | EXCLUDE | Same |
| STRIPE (fees) | EXCLUDE | Same |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN ACCOUNT TRANSFER, INTER-ACCOUNT | EXCLUDE | Internal movement |
| LOAN, BOND REPAYMENT | EXCLUDE | Loan principal |
| SALARY, WAGES, PAYROLL | EXCLUDE | Outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| MUNICIPAL RATES, PROPERTY RATES | EXCLUDE | Local government levy — not a supply |
| ATM, CASH WITHDRAWAL | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Johannesburg-based IT consultant. Format: FNB (First National Bank) account statement.

### Example 1 — Domestic B2B revenue (15%)

**Input line:**
`15 Apr 2025  CREDIT  ABC TECHNOLOGY (PTY) LTD  INV-2025-041  R 115,000.00  R 500,000.00`

**Reasoning:**
Incoming R 115,000 from a SA company for IT consulting. Standard 15% VAT. Gross R 115,000 includes VAT. Net = R 100,000 (taxable supply) + R 15,000 output tax. A VAT-compliant tax invoice must be issued per Section 20 of the VAT Act. Report on VAT201 Field 1.

**Classification:** Output tax 15% — R 15,000. Net supply: R 100,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22 Apr 2025  CREDIT  ACME CORP USA  USD 5,000 (R 92,500)  R 592,500.00`

**Reasoning:**
USD receipt from a US company for IT consulting services exported from South Africa. Zero-rated under Schedule 1 of the VAT Act if the services are physically performed in SA but consumed outside SA. Evidence: contract showing foreign client, payment in foreign currency. Report R 92,500 on Field 2 (zero-rated). Output tax: R 0.

**Classification:** Zero-rated export — R 92,500. Output tax: R 0.

### Example 3 — Electricity (15%, input credit)

**Input line:**
`10 Apr 2025  DEBIT  ESKOM HOLDINGS SOC  April electricity  -R 11,500.00  R 388,500.00`

**Reasoning:**
Eskom electricity bill. Taxable at 15%. Gross R 11,500. Net = R 10,000 + R 1,500 input tax. Eskom issues VAT-compliant tax invoices — input credit of R 1,500 claimable. Report on Field 10.

**Classification:** Input tax 15% — R 1,500. Net expense: R 10,000.

### Example 4 — Zero-rated food (basic foodstuffs)

**Input line:**
`12 Apr 2025  DEBIT  PICK N PAY  Groceries (business kitchen)  -R 800.00  R 387,700.00`

**Reasoning:**
Grocery purchase. If itemised receipt shows basic foodstuffs only (brown bread, eggs, fresh vegetables, etc.) — zero-rated under Schedule 2 of the VAT Act. No input tax on zero-rated items (the input tax rate is 0%). If mixed grocery (some 15% non-food items), split the purchase. Without itemised receipt: conservative default is 15% on full amount.

**Classification:** Zero-rated (if basic foodstuffs only) — R 0 input tax. Conservative default: 15% on R 800 = R 104 input tax / (R 695.65 net + R 104 VAT = R 800 gross). Flag: obtain itemised receipt.

### Example 5 — Imported service — self-assess (Google Ads)

**Input line:**
`08 Apr 2025  DEBIT  GOOGLE IRELAND LIMITED  Google Ads April  -R 10,000.00  R 377,700.00`

**Reasoning:**
Google Ads billed from Ireland. This is an "imported service" under Section 7(1)(c) of the VAT Act. The South African VAT-registered vendor must self-assess 15% VAT. Self-assessed output: R 10,000 × 15% = R 1,500 (add to Field 5). For a fully taxable vendor, simultaneously claim same as input tax R 1,500 (Field 10/11). Net effect: zero. Must be disclosed in the VAT201.

**Classification:** Imported service — self-assess output R 1,500; input R 1,500. Net: R 0 for fully taxable vendor.

### Example 6 — Residential rent (exempt, no input tax)

**Input line:**
`01 Apr 2025  DEBIT  CITY PROP MANAGEMENT  April office rent  -R 23,000.00  R 354,700.00`

**Reasoning:**
Monthly rent. If this is for a commercial office space where the landlord has opted to charge VAT and issues a VAT invoice showing 15%, then input tax of R 3,000 is claimable (gross R 23,000 / 1.15 × 15%). If the landlord has NOT opted to charge VAT (which is common for smaller landlords), then the rent is exempt and no input tax is available. Default: ask for the landlord's VAT invoice.

**Classification:** Tier 2 — ask. If VAT invoice received from landlord: Input 15% — R 3,000. If no VAT invoice: EXEMPT — no input tax.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 15%

Default rate for all taxable supplies. Legislation: VAT Act No. 89 of 1991, Section 7(1)(a).

### 5.2 Zero rate 0%

Exports of goods and qualifying services; basic foodstuffs (Schedule 2); illuminating paraffin; petrol and diesel (specific provisions); certain agricultural inputs; prescription medicines; qualifying accommodation. Evidence required for export zero-rating. Legislation: VAT Act Section 11; Schedule 2.

### 5.3 Exempt supplies

Financial services (Section 2); residential rental; public road and rail transport. No output tax charged; no input tax claimable on costs. Legislation: VAT Act Section 12.

### 5.4 Tax invoice requirements (Section 20)

For supplies above ZAR 50: full tax invoice required with supplier name/address/VAT number, invoice number, date, buyer name/address/VAT number (if VAT-registered), description, net amount, VAT rate, VAT amount, total. For supplies ZAR 50 and below: abridged invoice acceptable.

### 5.5 Imported services

Services supplied by a non-resident to a South African recipient are subject to VAT under Section 7(1)(c). Fully taxable vendors self-assess (output = input; net zero). Partially exempt or non-vendor recipients cannot recover and face a cost. Legislation: VAT Act Section 7(1)(c).

### 5.6 Anti-avoidance — entertainment

Input tax on entertainment, accommodation, and food/beverages is BLOCKED under Section 17(2)(a) UNLESS the vendor is in the business of providing entertainment (hotels, restaurants, conference venues). "Entertainment" includes meals, beverages, social functions.

### 5.7 Motor vehicles

Input tax on motor cars (as defined — passenger vehicles) is BLOCKED under Section 17(2)(c). Exception: if the vendor trades in motor cars or provides transport services as their primary business. Bakkies (utes/pickups) used exclusively for business: may qualify.

### 5.8 Filing deadlines

| Category | Period | Due date |
|---|---|---|
| Monthly vendor (>ZAR 30M/year) | Monthly | Last business day of following month |
| Bi-monthly vendor (most) | Every 2 months | Last business day of following month |
| Small vendor (approved) | Quarterly/semi-annual/annual | As approved by SARS |

### 5.9 Penalties

| Offence | Penalty |
|---|---|
| Late return | ZAR 100–ZAR 16,000 per month late |
| Late payment | 10% of tax due + interest at prescribed rate |
| Understatement | 10%–200% of shortfall depending on intent |
| Fraud | Criminal prosecution |

---

## Section 6 — Tier 2 catalogue

### 6.1 Entertainment — is vendor in the hospitality trade?

**What it shows:** Restaurant, entertainment, or accommodation expense.
**What's missing:** Whether the vendor's primary business is hospitality/entertainment (unblocks the input).
**Conservative default:** BLOCKED — no input tax.
**Question to ask:** "Is this entertainment expense directly related to the provision of entertainment to customers (e.g., you are a restaurant, hotel, or conference venue)? If not, the input tax is blocked."

### 6.2 Motor vehicle — is it a "motor car" as defined?

**What it shows:** Vehicle purchase, lease, or maintenance.
**What's missing:** Whether the vehicle is a "motor car" (blocked) or a qualifying vehicle.
**Conservative default:** BLOCKED — no input tax.
**Question to ask:** "Is this a passenger vehicle (sedan, SUV, hatchback) used for business? If yes: blocked. Is it a bakkie/van used exclusively for business goods transport? If exclusively business use: may be unblocked."

### 6.3 Rent — has landlord opted to charge VAT?

**What it shows:** Monthly rent payment.
**What's missing:** Whether the landlord is VAT-registered and has charged VAT on the invoice.
**Conservative default:** No input tax (treat as exempt until VAT invoice confirmed).
**Question to ask:** "Does your landlord issue a VAT tax invoice for the rent showing their VAT number and 15% VAT? If not, no input credit is available."

### 6.4 Zero-rated basic food vs. standard-rated food

**What it shows:** Supermarket purchase.
**What's missing:** Itemised receipt showing which items are basic (zero-rated) vs. standard (15%).
**Conservative default:** 15% on full amount.
**Question to ask:** "Do you have an itemised till slip? Items like brown bread, eggs, fresh vegetables, milk are zero-rated; packaged snacks, prepared food, non-food items are 15%."

### 6.5 Imported services — partial exemption interaction

**What it shows:** Payment for foreign digital services.
**What's missing:** Whether the vendor has any exempt income that blocks full input tax recovery on imported services.
**Conservative default:** Self-assess output and input at 15% (net zero for fully taxable).
**Question to ask:** "Does the business have any exempt income (residential rent, financial services)? If yes, the imported services input tax recovery may be limited."

---

## Section 7 — Excel working paper template

```
SOUTH AFRICA VAT201 WORKING PAPER
Tax Period: ____________  VAT Registration No.: ____________

A. OUTPUT TAX
  A1. Standard-rated supplies at 15% (net)     ___________
  A2. Output tax 15% (A1 × 15/115 of gross OR A1 × 15%)  ___
  A3. Zero-rated supplies (net)                ___________
  A4. Exempt supplies (net)                    ___________
  A5. Imported services self-assessed output   ___________
  A6. Total output tax (A2 + A5)               ___________

B. INPUT TAX
  B1. Standard-rated purchases (net)           ___________
  B2. Input tax at 15% (B1 × 15/115)           ___________
  B3. Import VAT (SAD500)                      ___________
  B4. Imported services input (self-assessed)  ___________
  B5. Blocked input (entertainment, motor cars) ___________
  B6. Net input tax (B2+B3+B4 − B5)            ___________

C. NET VAT
  C1. Net VAT (A6 − B6)                         ___________
  C2. Prior period credit                       ___________
  C3. Net payable / (refund) (C1 − C2)          ___________

REVIEWER FLAGS:
  [ ] Tax invoices (Section 20) confirmed for all input claims?
  [ ] Entertainment and motor car inputs correctly blocked?
  [ ] Export evidence held for zero-rated supplies?
  [ ] Imported services self-assessed (output = input)?
  [ ] Basic foodstuffs correctly zero-rated?
  [ ] Rent — landlord VAT invoice confirmed?
```

---

## Section 8 — Bank statement reading guide

### Common South African bank statement formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| FNB | Date, Description, Debit, Credit, Balance | DD Mon YYYY | ZAR with 2 decimals |
| Standard Bank | Date, Narrative, Debit, Credit, Balance | DD MMM YYYY | ZAR |
| ABSA | Date, Description, Amount, Balance | DD/MM/YYYY | ZAR |
| Nedbank | Date, Details, Debit, Credit, Balance | DD/MM/YYYY | ZAR |
| Capitec | Date, Description, Debit, Credit, Balance | YYYY-MM-DD | ZAR |

### Key South African banking terms

| Term | Meaning | Classification hint |
|---|---|---|
| CREDIT | Incoming funds | Potential revenue |
| DEBIT | Outgoing payment | Potential expense |
| ATM WITHDRAWAL | Cash withdrawal | Tier 2 — ask |
| BANK CHARGES | Bank fee | Exempt |
| INTEREST EARNED | Interest received | Exempt |
| BALANCE | Running balance | Ignore |
| SALARY / WAGES | Payroll | Out of VAT scope |
| EFT / EFT DEBIT | Electronic fund transfer | Check direction |

---

## Section 9 — Onboarding fallback

```
SOUTH AFRICA VAT ONBOARDING — MINIMUM QUESTIONS
1. VAT registration number (10 digits starting with 4)?
2. Tax period covered by this bank statement?
3. Filing frequency: monthly, bi-monthly, or other?
4. Do you have any exports (zero-rated)? Evidence held?
5. Do you have exempt income (financial services, residential rent)?
6. Does the business provide entertainment as its primary service?
   (Determines whether entertainment input tax is blocked)
7. Are any vehicles used exclusively for business goods transport?
8. Imported services (Google, Microsoft, etc.) — confirm for self-assessment
9. Prior period credit/refund amount to carry forward?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| VAT Act | Value-Added Tax Act No. 89 of 1991 |
| Standard rate | Section 7(1)(a) |
| Zero rate | Section 11; Schedule 2 |
| Exemptions | Section 12 |
| Input tax | Section 16 |
| Blocked input — entertainment | Section 17(2)(a) |
| Blocked input — motor cars | Section 17(2)(c) |
| Tax invoice | Section 20 |
| Imported services | Section 7(1)(c) |
| Penalties | Tax Administration Act No. 28 of 2011 |

### Known gaps

- Partial exemption (Section 17(1)) apportionment — escalate
- Property option to tax — escalate
- Financial services VAT — escalate
- Capital goods adjustments (Section 18A) — escalate

### Self-check

- [ ] All tax invoices Section 20 compliant
- [ ] Entertainment and motor car inputs blocked
- [ ] Export zero-rating supported by evidence
- [ ] Imported services self-assessed
- [ ] Basic foodstuffs correctly split from 15% items
- [ ] Prior period credit carried forward

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial |
| 2.0 | April 2026 | v2.0 rewrite: pattern library, worked examples, no inline tier tags |

---

## Prohibitions

- NEVER allow input tax on entertainment expenses unless vendor's primary business is hospitality
- NEVER allow input tax on motor cars (passenger vehicles) used for mixed purposes
- NEVER zero-rate exports without evidence (customs documents, foreign payment records)
- NEVER allow input tax from a non-VAT-registered supplier
- NEVER self-assess imported services without recording both output and input in the same period
- NEVER present calculations as definitive — direct to a CA(SA) or registered tax practitioner

---

## Disclaimer

This skill and its outputs are for informational purposes only and do not constitute advice. All outputs must be reviewed by a qualified professional before filing. The most up-to-date version is maintained at openaccountants.com.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
