---
name: philippines-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Philippines VAT return (BIR Form 2550M/2550Q), classify transactions for Philippine VAT purposes, or advise on VAT registration and filing in the Philippines. Trigger on phrases like "Philippines VAT", "BIR Form 2550", "input VAT Philippines", "output VAT Philippines", "VAT-registered Philippines", "percentage tax Philippines", or any Philippines VAT request. ALWAYS read this skill before touching any Philippines VAT work.
version: 2.0
jurisdiction: PH
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Philippines VAT Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Philippines (Republika ng Pilipinas) |
| Tax | Value Added Tax (VAT) |
| Currency | PHP (Philippine Peso / ₱) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 12% |
| Zero rate | 0% (exports; services to non-residents; PEZA/BOI-registered enterprises; international transport) |
| Exempt | Agricultural products (unprocessed), educational services, medical/hospital services, housing below threshold (PHP 3.199M), financial services (some), life insurance premiums, importation of basic necessities |
| Registration threshold | PHP 3,000,000 per year in gross sales/receipts |
| Non-VAT (percentage tax) | 3% on gross receipts for non-VAT-registered (< PHP 3M); quarterly Form 2551Q |
| Tax authority | Bureau of Internal Revenue (BIR) |
| Monthly return | BIR Form 2550M (due: 20th of following month) |
| Quarterly return | BIR Form 2550Q (due: 25th of month following quarter end) |
| Filing portal | EFPS (Electronic Filing and Payment System) — https://efps.bir.gov.ph |
| Tax invoice | Official Receipt (OR) or Sales Invoice — BIR-registered |
| TIN | Tax Identification Number (9 or 12 digits) |
| RDO | Revenue District Office — taxpayer's registered district |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Philippine CPA or tax practitioner |
| Skill version | 2.0 |

### Key Form 2550M/Q lines

| Line | Meaning |
|---|---|
| Part I-A | Sales/receipts at 12% (net of VAT) |
| Part I-B | Zero-rated sales |
| Part I-C | Exempt sales |
| Part II | Output VAT at 12% |
| Part III | Input VAT from domestic purchases |
| Part IV | Input VAT from importation |
| Part V | Net input VAT available |
| Part VI | VAT payable (Part II − Part V) |
| Part VII | Tax credits/excess credit |
| Part VIII | Net VAT still due |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 12% standard |
| Unknown counterparty country | Domestic Philippines |
| Unknown export/zero-rate qualification | 12% until evidence confirmed |
| Unknown business-use % (vehicle, phone) | 0% input VAT |
| Unknown whether Official Receipt compliant | No input credit |
| Unknown B2B vs B2C for digital services | 12% domestic |
| Unknown PEZA status | Not zero-rated until certificate confirmed |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | PHP 500,000 |
| HIGH tax delta on single default | PHP 60,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | PHP 200,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. TIN and confirmation of VAT registration (Certificate of Registration — COR, BIR Form 2303).

**Recommended** — Official Receipts (ORs) or Sales Invoices for all output VAT, supplier ORs/invoices for all input VAT claimed, prior period excess credit.

**Ideal** — complete sales/purchase journal, import entries, prior quarterly return, EFPS filing confirmation.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input VAT credits require BIR-registered Official Receipts (OR) or Sales Invoices from VAT-registered suppliers. All credits are provisional pending receipt verification."

### Refusal catalogue

**R-PH-1 — Non-VAT (percentage tax) taxpayer.** "Businesses below the PHP 3M threshold pay percentage tax (3% of gross receipts) via Form 2551Q, not VAT. They cannot register ORs for VAT and cannot recover input VAT. This skill covers VAT-registered businesses only."

**R-PH-2 — PEZA/BOI zero-rating complex structures.** "PEZA-registered enterprises have specific zero-rating rules for sales within the ecozone. If the client sells to a PEZA entity and claims zero-rating, verify the PEZA certificate — if complex, escalate to a Philippine CPA."

**R-PH-3 — Partial exemption with mixed supplies.** "If the business makes both taxable and exempt supplies and cannot directly attribute input VAT, an allocation is required. Out of scope without the annual ratio — escalate."

**R-PH-4 — Withholding VAT (Final Withholding VAT).** "Certain transactions (e.g., payments by government, non-residents) are subject to final withholding VAT. If significant government contracts exist, track separately — escalate to a CPA."

**R-PH-5 — Digital service providers (non-residents).** "Non-resident digital service providers with Philippine consumption must register for VAT under the Digital Economy Taxation Act. Out of scope for domestic filers."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Philippine banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BDO UNIBANK, BANCO DE ORO | EXCLUDE (fee lines) | Financial service — VAT exempt |
| BANK OF THE PHILIPPINE ISLANDS, BPI | EXCLUDE (fee lines) | Same |
| METROBANK, METROPOLITAN BANK | EXCLUDE (fee lines) | Same |
| UNIONBANK OF THE PHILIPPINES | EXCLUDE (fee lines) | Same |
| SECURITY BANK | EXCLUDE (fee lines) | Same |
| LANDBANK OF THE PHILIPPINES, LBP | EXCLUDE (fee lines) | Same |
| PHILIPPINE NATIONAL BANK, PNB | EXCLUDE (fee lines) | Same |
| CHINA BANKING, CHINABANK | EXCLUDE (fee lines) | Same |
| RCBC, RIZAL COMMERCIAL BANKING | EXCLUDE (fee lines) | Same |
| GCASH, G-XCHANGE (GXI) | EXCLUDE (fee lines) | E-wallet — financial service |
| MAYA, PAYMAYA | EXCLUDE (fee lines) | E-wallet — financial service |
| SEABANK | EXCLUDE (fee lines) | Digital bank — financial service |
| SERVICE CHARGE, BANK FEE, INTEREST | EXCLUDE | Bank charges/interest — exempt |

### 3.2 Philippine government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BUREAU OF INTERNAL REVENUE, BIR | EXCLUDE | Tax payment |
| BUREAU OF CUSTOMS, BOC | EXCLUDE | Customs duty |
| SOCIAL SECURITY SYSTEM, SSS | EXCLUDE | Social insurance |
| PHILHEALTH | EXCLUDE | Health insurance |
| PAG-IBIG, HDMF | EXCLUDE | Housing fund |
| SEC PHILIPPINES | EXCLUDE | Regulatory fee |
| LGU, BARANGAY, CITY HALL | EXCLUDE | Local government fee |

### 3.3 Philippine utilities (taxable at 12%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| MERALCO, MANILA ELECTRIC | Input 12% | 12% | Electricity (Metro Manila) — taxable |
| CEPALCO (Cagayan de Oro electric) | Input 12% | 12% | Electricity — taxable |
| VECO (Visayas Electric) | Input 12% | 12% | Electricity — taxable |
| MANILA WATER | Input 12% | 12% | Water (East Zone) — taxable |
| MAYNILAD WATER SERVICES | Input 12% | 12% | Water (West Zone) — taxable |
| PLDT, PHILIPPINE LONG DISTANCE | Input 12% | 12% | Telecom/internet — taxable |
| GLOBE TELECOM | Input 12% | 12% | Mobile/internet — taxable |
| SMART COMMUNICATIONS, SMART | Input 12% | 12% | Mobile — taxable |
| DITO TELECOMMUNITY | Input 12% | 12% | Mobile — taxable |
| CONVERGE ICT | Input 12% | 12% | Internet — taxable |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| PHILIPPINE AIRLINES, PAL | Check route | 0%/12% | International 0%; domestic 12% |
| CEBU PACIFIC | Check route | 0%/12% | International 0%; domestic 12% |
| AIRASIA PHILIPPINES | Check route | 0%/12% | International 0%; domestic 12% |
| PHILIPPINE NATIONAL RAILWAYS, PNR | Input 12% | 12% | Rail — taxable |
| LRT, MRT (Metro Rail Transit) | Input 12% | 12% | Mass transit — taxable |
| GRAB PHILIPPINES | Input 12% | 12% | Ride-hailing — taxable |
| ANGKAS | Input 12% | 12% | Motorcycle taxi — taxable |
| LBC EXPRESS | Input 12% | 12% | Courier — taxable |
| JRS EXPRESS | Input 12% | 12% | Courier — taxable |
| DHL PHILIPPINES | Input 12% | 12% | Courier — taxable |
| FEDEX PHILIPPINES | Input 12% | 12% | Courier — taxable |
| 2GO EXPRESS | Input 12% | 12% | Courier — taxable |
| NINJA VAN PHILIPPINES | Input 12% | 12% | Courier — taxable |
| J&T EXPRESS PHILIPPINES | Input 12% | 12% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| SM SUPERMARKET, SM MARKETS | Input 12% | 12% | Supermarket — 12% on non-exempt items |
| ROBINSONS SUPERMARKET | Input 12% | 12% | Supermarket — 12% |
| PUREGOLD | Input 12% | 12% | Supermarket — 12% |
| S&R MEMBERSHIP SHOPPING | Input 12% | 12% | Warehouse club — 12% |
| MERCURY DRUG | Input 12% (medicine) / EXEMPT (prescription) | Mixed | Prescription medicines exempt; OTC/non-medicine 12% |
| WATSONS PHILIPPINES | Input 12% | 12% | Health/beauty retail — 12% |
| 7-ELEVEN PHILIPPINES | Input 12% | 12% | Convenience store — 12% |
| JOLLIBEE (eat-in) | Input 12% | 12% | Restaurant — 12% (food not exempt when eaten in) |
| MCDONALD'S PHILIPPINES | Input 12% | 12% | Restaurant — 12% |

### 3.6 SaaS — international suppliers (note: PH now has digital VAT)

Under the Digital Economy Taxation Act (R.A. 11976, signed 2024), non-resident digital service providers must register for Philippine VAT. For B2B PKP buyers: input credit claimable if the foreign supplier charges and remits 12% VAT.

| Pattern | Status | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | Should be registered | Input 12% if charged | Check if Google charges PH VAT on invoice |
| MICROSOFT (365, Azure) | Should be registered | Input 12% if charged | Same |
| META, FACEBOOK ADS | Should be registered | Input 12% if charged | Same |
| NETFLIX | Registered | 12% on subscription | Consumer-facing |
| ZOOM | Check | Input 12% if charged | Verify registration |
| SLACK | Check | Input 12% if charged | Verify |
| NOTION, OPENAI, ANTHROPIC | Check | Flag for verification | Verify PH registration status |
| AWS | Check | Input 12% if charged | Verify |

### 3.7 Payment processors (exempt fees)

| Pattern | Treatment | Notes |
|---|---|---|
| PAYPAL (transaction fees) | EXCLUDE | Financial service — VAT exempt |
| STRIPE (transaction fees) | EXCLUDE | Same |
| GCASH (transaction fees) | EXCLUDE | Same |
| PAYMONGO (fees) | EXCLUDE | Payment gateway — exempt |
| DRAGONPAY (fees) | EXCLUDE | Same |

### 3.8 Professional services (VAT-registered)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| CPA FIRM, ACCOUNTING FIRM | Input 12% | 12% | Professional services — taxable |
| LAW FIRM, ATTY, ATTORNEY | Input 12% | 12% | Legal services — taxable |
| NOTARY PUBLIC | Input 12% | 12% | Notarial services — taxable |
| ADVERTISING AGENCY | Input 12% | 12% | Marketing — taxable |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTER-ACCOUNT TRANSFER, OWN ACCOUNT | EXCLUDE | Internal movement |
| LOAN PROCEEDS, LOAN REPAYMENT | EXCLUDE | Loan principal — out of scope |
| SALARY, PAYROLL | EXCLUDE | Wages — outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| SECURITY DEPOSIT, ADVANCE DEPOSIT | Tier 2 — check | May trigger VAT if applied to taxable supply |
| ATM WITHDRAWAL, CASH WITHDRAWAL | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Manila-based IT consultant. Format: BDO Unibank transaction history.

### Example 1 — Domestic B2B revenue (12%)

**Input line:**
`04/15/2025  CREDIT  ABC TECH SOLUTIONS INC  REF INV-2025-041  PHP 1,120,000.00  PHP 5,000,000.00`

**Reasoning:**
Incoming PHP 1,120,000 from a Philippine company for IT consulting. Standard 12% VAT. Gross PHP 1,120,000 includes VAT. Net = PHP 1,000,000 (taxable base) + PHP 120,000 output VAT. A BIR-registered Official Receipt or Service Invoice must be issued. Report on Form 2550M Part I-A.

**Classification:** Output VAT 12% — PHP 120,000. Net sales: PHP 1,000,000.

### Example 2 — Zero-rated export service

**Input line:**
`04/22/2025  CREDIT  ACME CORPORATION USA  USD 10,000 (PHP 560,000.00)  PHP 5,560,000.00`

**Reasoning:**
USD receipt from a US company for IT consulting services rendered to a non-resident. Zero-rated if: (1) service rendered in the Philippines; (2) paid by a non-resident in foreign currency; (3) proceeds inwardly remitted through Philippine banking. Report PHP 560,000 on Form 2550M Part I-B (zero-rated). Output VAT: PHP 0. Confirm: inward remittance documentation held.

**Classification:** Zero-rated — PHP 560,000. Output VAT: PHP 0.

### Example 3 — Utility expense (12%, input credit)

**Input line:**
`04/10/2025  DEBIT  MERALCO  April 2025 Electric Bill  -PHP 11,200.00  PHP 4,988,800.00`

**Reasoning:**
MERALCO electricity bill. Taxable at 12%. Gross PHP 11,200 includes VAT. Net = PHP 10,000 + PHP 1,200 input VAT. MERALCO issues BIR-registered ORs — input credit of PHP 1,200 claimable. Report on Form 2550M Part III.

**Classification:** Input VAT 12% — PHP 1,200. Net expense: PHP 10,000.

### Example 4 — International airline (domestic route, 12%)

**Input line:**
`04/08/2025  DEBIT  CEBU PACIFIC AIR  Manila-Cebu ticket  -PHP 4,480.00  PHP 4,984,320.00`

**Reasoning:**
Domestic flight (Manila to Cebu) on Cebu Pacific. Domestic air transport is taxable at 12%. Gross PHP 4,480. Net = PHP 4,000 + PHP 480 input VAT. Cebu Pacific issues VAT ORs for domestic tickets — input credit of PHP 480 claimable if OR is BIR-registered.

**Classification:** Input VAT 12% — PHP 480. Net expense: PHP 4,000.

### Example 5 — Exempt supply received (SSS contribution)

**Input line:**
`04/25/2025  DEBIT  SOCIAL SECURITY SYSTEM  SSS April 2025  -PHP 4,500.00  PHP 4,979,820.00`

**Reasoning:**
SSS employer contribution. Government social insurance — EXCLUDE from VAT return entirely. Not a supply of goods or services. No input VAT. This is a payroll-related obligation, not a business expense generating input credit.

**Classification:** EXCLUDE — outside VAT scope. Statutory employer obligation.

### Example 6 — Restaurant (12%, no block in Philippines)

**Input line:**
`04/12/2025  DEBIT  JOLLIBEE FOODS CORP  Client lunch  -PHP 1,120.00  PHP 4,978,700.00`

**Reasoning:**
Client lunch at Jollibee. In the Philippines, there is no absolute block on entertainment/meals input VAT (unlike Malta). Restaurant meals are taxable at 12%. If a BIR-registered OR is obtained, input VAT of PHP 120 is claimable (PHP 1,120 gross / 1.12 = PHP 1,000 net + PHP 120 VAT). However, BIR scrutinises entertainment claims — ensure business purpose is documented. If no OR: no credit.

**Classification:** Input VAT 12% — PHP 120 (if OR held). Net expense: PHP 1,000. Flag: confirm BIR-registered OR from Jollibee.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 12%

Default rate for all taxable supplies of goods and services. Legislation: National Internal Revenue Code (NIRC) Section 106 (goods) and Section 108 (services).

### 5.2 Zero rate — exports and qualifying supplies

Zero-rated: export of goods; services rendered to non-residents paid in foreign currency (with inward remittance); services to PEZA-registered entities within ecozones; services to BOI-registered enterprises (specific cases); international transport of passengers and cargo. Evidence: export documentation; inward remittance records; PEZA certificate. Legislation: NIRC Sections 106(A)(2) and 108(B).

### 5.3 Exempt supplies

Agricultural products in original state; educational services; medical/hospital services; literary/musical compositions; housing below PHP 3,199,200 (BIR threshold); lease of residential unit below PHP 15,000/month; life insurance premiums; common carriers below threshold; importation of basic necessities. Legislation: NIRC Sections 109.

### 5.4 Official Receipt (OR) / Sales Invoice requirements

BIR-registered ORs or Sales Invoices are required for input credit. Must contain: TIN of seller and buyer, BIR-registered serial number, date, description, net amount, VAT rate, VAT amount. Electronic invoices allowed via EFPS-registered providers.

### 5.5 Input VAT limitations

Input VAT is not creditable for: entertainment/representation expenses (limited — see Section 6.1); motor vehicles not used exclusively for business; purchases from non-VAT-registered suppliers; purchases without valid ORs.

### 5.6 Transitional input VAT

Beginning inventory VAT credit available upon VAT registration (2% of inventory value or actual input VAT on goods for sale, whichever is higher).

### 5.7 Filing deadlines

| Return | Period | Due date |
|---|---|---|
| Form 2550M (monthly) | Monthly | 20th of following month |
| Form 2550Q (quarterly) | Quarterly | 25th of month following quarter |
| Payment | Same as filing | Same deadline |

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late filing | PHP 1,000 per return + 25% surcharge |
| Late payment | 12% interest per annum on unpaid tax |
| Failure to issue OR | 50% surcharge on transaction + compromise penalty |
| Fraud/falsification | 50% surcharge + criminal liability |

---

## Section 6 — Tier 2 catalogue

### 6.1 Entertainment expense input VAT limit

**What it shows:** Restaurant, hotel, or entertainment expense claimed as business entertainment.
**What's missing:** Whether BIR-registered OR held and whether expense is within the entertainment deduction limit.
**Conservative default:** No input credit (treat as personal if OR not confirmed).
**Question to ask:** "Is there a BIR-registered OR for this entertainment expense? Is this within the 0.5% of net sales / 1% of net revenue entertainment ceiling?"

### 6.2 Zero-rating for services to non-residents

**What it shows:** Revenue from a foreign client.
**What's missing:** Whether payment was received in foreign currency with inward remittance through a Philippine bank.
**Conservative default:** 12% standard rate.
**Question to ask:** "Was payment received in USD/foreign currency? Was it remitted through a Philippine bank (with bank credit advice)? Is the client a non-resident foreign company?"

### 6.3 PEZA zero-rating

**What it shows:** Sale to a company that may be PEZA-registered.
**What's missing:** PEZA registration certificate and whether the supply is within the ecozone.
**Conservative default:** 12% — do not zero-rate without certificate.
**Question to ask:** "Can the buyer provide their PEZA Certificate of Registration and authority to zero-rate?"

### 6.4 Digital services — foreign provider VAT status

**What it shows:** Payment to a foreign tech/SaaS company.
**What's missing:** Whether the foreign provider has registered for Philippine VAT (post-Digital Economy Act 2024) and whether they are charging 12% VAT on invoices.
**Conservative default:** No input credit until confirmed.
**Question to ask:** "Does the invoice from this foreign provider show Philippine VAT (12%) charged? If not, no input credit is available."

### 6.5 Motor vehicle expenses

**What it shows:** Vehicle purchase, lease, fuel, or maintenance.
**What's missing:** Whether vehicle is used exclusively for business.
**Conservative default:** 0% input credit.
**Question to ask:** "Is this vehicle registered in the company name and used exclusively for business? Personal-use vehicles and mixed-use vehicles have limited input VAT recovery."

---

## Section 7 — Excel working paper template

```
PHILIPPINES VAT WORKING PAPER
Period: ____________  TIN: ____________  RDO: ____________

A. OUTPUT VAT
  A1. Taxable sales at 12% (net)               ___________
  A2. Output VAT at 12% (A1 × 12%)             ___________
  A3. Zero-rated sales (exports/non-resident)  ___________
  A4. Exempt sales (net)                        ___________

B. INPUT VAT
  B1. Domestic purchases — 12% (net)           ___________
  B2. Input VAT at 12% (B1 × 12%)              ___________
  B3. Importation input VAT                    ___________
  B4. Total input VAT (B2+B3)                  ___________
  B5. Disallowed input (blocked items)         ___________
  B6. Net input VAT (B4 − B5)                  ___________

C. NET VAT PAYABLE
  C1. Net VAT (A2 − B6)                         ___________
  C2. Excess credit from prior period           ___________
  C3. Tax credits (e.g., CWT, advance payments) ___________
  C4. Net payable / (refund) (C1−C2−C3)         ___________

REVIEWER FLAGS:
  [ ] BIR-registered ORs/invoices confirmed for all input credits?
  [ ] Inward remittance documentation for zero-rated services?
  [ ] PEZA certificates confirmed for zero-rated sales to ecozone?
  [ ] Digital service provider VAT registration confirmed?
  [ ] Motor vehicle input VAT blocked where applicable?
  [ ] Entertainment ceiling calculated?
```

---

## Section 8 — Bank statement reading guide

### Common Philippine bank statement formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| BDO | Date, Reference, Description, Debit, Credit, Balance | MM/DD/YYYY | PHP with 2 decimals |
| BPI | Date, Transaction Reference, Description, Withdrawal, Deposit, Balance | MM/DD/YYYY | PHP |
| Metrobank | Date, Description, Debit, Credit, Balance | MM/DD/YYYY | PHP |
| UnionBank | Date, Description, Debit, Credit, Available Balance | MM/DD/YYYY | PHP |
| Landbank | Posting Date, Description, Debit, Credit, Running Balance | MM/DD/YYYY | PHP |

### Key Philippine banking terms

| Term | Meaning | Classification hint |
|---|---|---|
| CREDIT / DEPOSIT | Incoming funds | Potential revenue |
| DEBIT / WITHDRAWAL | Outgoing payment | Potential expense |
| INWARD REMITTANCE | Foreign currency receipt | Potential zero-rated export |
| SERVICE CHARGE | Bank fee | Exempt |
| INTEREST | Bank interest | Exempt |
| BALANCE | Running balance | Ignore |
| ATM WITHDRAWAL | Cash withdrawal | Tier 2 — ask |
| PAYROLL DEBIT | Salary payment | Out of VAT scope |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
PHILIPPINES VAT ONBOARDING — MINIMUM QUESTIONS
1. TIN (Tax Identification Number) and RDO (Revenue District Office)?
2. Certificate of Registration (BIR Form 2303) — VAT registered? What is the effective date?
3. Filing basis: monthly (2550M) or monthly + quarterly (2550Q)?
4. Do you have any exports or services to non-resident clients?
   If yes: was payment received in foreign currency with inward remittance?
5. Do you have any PEZA-registered customers?
6. Motor vehicle expenses — are vehicles exclusively for business?
7. Any international SaaS subscriptions? Do those invoices show 12% Philippine VAT?
8. Prior period excess input VAT credit carried forward?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| VAT on goods | NIRC Section 106 |
| VAT on services | NIRC Section 108 |
| Zero-rated sales | NIRC Sections 106(A)(2), 108(B) |
| Exempt transactions | NIRC Section 109 |
| Input VAT | NIRC Section 110 |
| Official Receipts | NIRC Section 237 |
| Registration threshold | NIRC Section 109(BB) (PHP 3M) |
| Digital economy VAT | R.A. 11976 (Digital Economy Taxation Act, 2024) |
| Penalties | NIRC Sections 248–249 |

### Known gaps

- PEZA zero-rating complex structures — escalate to CPA
- Final withholding VAT on government transactions — track separately
- Percentage tax (non-VAT registered) — separate Form 2551Q; different skill
- Import VAT (Bureau of Customs process) — coordinate with customs broker
- Digital Economy VAT implementation — verify BIR RMC for latest guidance

### Self-check before filing

- [ ] BIR-registered ORs/invoices held for all input VAT claimed
- [ ] Inward remittance documentation for all zero-rated services
- [ ] PEZA certificates on file for any PEZA zero-rated sales
- [ ] Digital service VAT registration confirmed for foreign suppliers
- [ ] Prior period excess credit correctly applied
- [ ] Entertainment input VAT within the BIR ceiling

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, Digital Economy Act note, no inline tier tags |

---

## Prohibitions

- NEVER claim input VAT from a supplier who is not BIR VAT-registered
- NEVER zero-rate services to non-residents without inward remittance documentation
- NEVER zero-rate PEZA sales without the buyer's PEZA certificate
- NEVER claim input VAT from foreign SaaS providers without confirming Philippine VAT registration
- NEVER apply 12% to exempt supplies (unprocessed agriculture, medical, education, etc.)
- NEVER present calculations as definitive — direct to a Philippine CPA or BIR-accredited tax practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.
