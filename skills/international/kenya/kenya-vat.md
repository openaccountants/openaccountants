---
name: kenya-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Kenya VAT return (VAT-3), classify transactions for Kenyan VAT purposes, or advise on VAT registration and filing in Kenya. Trigger on phrases like "Kenya VAT", "KRA VAT", "VAT-3 Kenya", "input tax Kenya", "output tax Kenya", "Kenya Revenue Authority VAT", or any Kenya VAT request. ALWAYS read this skill before touching any Kenya VAT work.
version: 2.0
jurisdiction: KE
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Kenya VAT (VAT-3) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Kenya (Republic of Kenya) |
| Tax | VAT (Value Added Tax) |
| Currency | KES (Kenyan Shilling / Ksh) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 16% |
| Zero rate | 0% (exports; certain agricultural inputs; medicines; specified goods under Second Schedule) |
| Exempt | Financial services, education, medical services, agricultural products (raw), passenger transport |
| Registration threshold | KES 5,000,000 per year |
| Tax authority | KRA (Kenya Revenue Authority) |
| Return form | VAT-3 (monthly) |
| Filing portal | iTax (https://itax.kra.go.ke) |
| Filing deadline | 20th of the month following the tax period |
| Tax invoice | ETR (Electronic Tax Register) receipt or e-Invoice required |
| PIN | Personal Identification Number — tax registration |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Kenyan CPA(K) or tax practitioner |
| Skill version | 2.0 |

### Key VAT-3 return fields

| Field | Meaning |
|---|---|
| Section A | Standard-rated sales at 16% |
| Section B | Zero-rated sales |
| Section C | Exempt sales |
| Section D | Total output tax |
| Section E | Standard-rated purchases (input tax) |
| Section F | Zero-rated purchases |
| Section G | Total input tax |
| Section H | Net VAT payable (D − G) |
| Section I | Excess credit c/f or refund |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 16% standard |
| Unknown counterparty country | Domestic Kenya |
| Unknown export qualification | 16% until evidence confirmed |
| Unknown business-use % | 0% input tax |
| Unknown ETR/e-Invoice availability | No input credit |
| Unknown whether exempt or taxable | Taxable at 16% |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | KES 500,000 |
| HIGH tax delta on single default | KES 80,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net VAT position | KES 200,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. KRA PIN (tax PIN).

**Recommended** — ETR receipts or e-invoices for all purchases, sales invoices issued, prior period excess credit.

**Ideal** — complete purchase/sales register from iTax, import entry documents (IDF/Entry), asset register.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input tax requires ETR receipts or compliant e-invoices. All credits provisional pending verification."

### Refusal catalogue

**R-KE-1 — Non-registered vendor.** "Only KRA VAT-registered taxpayers (above KES 5M threshold) can charge and recover VAT. Confirm registration."

**R-KE-2 — Partial exemption.** "Businesses with both taxable and exempt supplies must apportion input tax. Out of scope without full-year data."

**R-KE-3 — Withholding VAT (WHT-VAT).** "Government agencies withhold 6% (or 100%) of VAT on payments. Track WHT-VAT certificates — escalate if significant."

**R-KE-4 — Digital marketplace suppliers.** "Non-resident digital service providers must register for Kenyan VAT. Complex cross-border treatment — escalate for non-resident client situations."

---

## Section 3 — Supplier pattern library

### 3.1 Kenyan banks — fees (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KENYA COMMERCIAL BANK, KCB | EXCLUDE (fees) | Financial service — exempt |
| EQUITY BANK, EQUITY GROUP | EXCLUDE (fees) | Same |
| COOPERATIVE BANK, CO-OP BANK | EXCLUDE (fees) | Same |
| ABSA BANK KENYA | EXCLUDE (fees) | Same |
| STANDARD CHARTERED KENYA | EXCLUDE (fees) | Same |
| NCBA BANK, NCBA GROUP | EXCLUDE (fees) | Same |
| I&M BANK | EXCLUDE (fees) | Same |
| DIAMOND TRUST BANK, DTB | EXCLUDE (fees) | Same |
| MPESA, M-PESA (SAFARICOM) | EXCLUDE (fees) | Mobile money — financial service |
| AIRTEL MONEY | EXCLUDE (fees) | Same |
| BANK CHARGES, INTEREST | EXCLUDE | Bank fee/interest — exempt |

### 3.2 Kenyan government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KENYA REVENUE AUTHORITY, KRA | EXCLUDE | Tax payment |
| NATIONAL SOCIAL SECURITY FUND, NSSF | EXCLUDE | Social insurance |
| NATIONAL HOSPITAL INSURANCE FUND, NHIF | EXCLUDE | Health insurance |
| NITA, NATIONAL INDUSTRIAL TRAINING | EXCLUDE | Statutory levy |
| NTSA, NATIONAL TRANSPORT AND SAFETY | EXCLUDE | Regulatory fee |

### 3.3 Kenyan utilities (taxable at 16%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| KENYA POWER, KPLC | Input 16% | 16% | Electricity — taxable |
| NAIROBI CITY WATER, NCWSC | Input 16% | 16% | Water — taxable |
| SAFARICOM (data/voice) | Input 16% | 16% | Telecom — taxable |
| AIRTEL KENYA | Input 16% | 16% | Mobile — taxable |
| TELKOM KENYA, TELKOM | Input 16% | 16% | Telecom — taxable |
| ZUKU FIBER, WANANCHI GROUP | Input 16% | 16% | Internet — taxable |
| LIQUID TELECOM KENYA | Input 16% | 16% | Internet — taxable |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| KENYA AIRWAYS, KQ | Check route | 0%/16% | International 0%; domestic 16% |
| JAMBOJET | Input 16% | 16% | Domestic — 16% |
| AFRICAAIRWAYS | Check route | 0%/16% | Check |
| UBER KENYA | Input 16% | 16% | Ride-hailing — taxable |
| BOLT KENYA | Input 16% | 16% | Ride-hailing — taxable |
| LITTLE CAB | Input 16% | 16% | Ride-hailing — taxable |
| DHL KENYA | Input 16% | 16% | Courier — taxable |
| FEDEX KENYA | Input 16% | 16% | Courier — taxable |
| G4S KENYA, WELLS FARGO (courier) | Input 16% | 16% | Security/courier — taxable |
| POSTA KENYA (parcel) | Input 16% | 16% | Parcel — taxable |
| POSTA KENYA (stamps) | EXEMPT | 0% | Universal stamps — exempt |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| NAKUMATT, NAIVAS SUPERMARKET | Input 16%/0% | Mixed | Non-food 16%; basic food may be zero-rated |
| QUICKMART SUPERMARKET | Input 16%/0% | Mixed | Same |
| CARREFOUR KENYA | Input 16%/0% | Mixed | Same |
| CHANDARANA FOODPLUS | Input 16%/0% | Mixed | Supermarket — split |
| TUSKYS SUPERMARKET | Input 16%/0% | Mixed | Same |
| KWAL, DEL MONTE KENYA (packaged food) | Input 16% | 16% | Processed food — 16% |
| UNGA LIMITED (maize flour) | Input 0% | 0% | Basic staple — zero-rated |

### 3.6 SaaS — international suppliers

Foreign digital service providers must register with KRA if providing services to Kenyan consumers/businesses.

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE (Workspace, Ads) | Reverse charge 16% | Self-assess if not KRA-registered |
| MICROSOFT (365, Azure) | Reverse charge 16% | Same |
| META, FACEBOOK ADS | Reverse charge 16% | Same |
| ZOOM, SLACK, NOTION | Reverse charge 16% | Same |
| AWS | Reverse charge 16% | Same |

### 3.7 Payment processors (exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| MPESA TRANSACTION FEE | EXCLUDE | Financial service — exempt |
| PESAPAL (fees) | EXCLUDE | Payment gateway — exempt |
| STRIPE (fees) | EXCLUDE | Same |
| PAYPAL (fees) | EXCLUDE | Same |

### 3.8 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Internal movement |
| LOAN, REPAYMENT | EXCLUDE | Loan principal |
| SALARY, PAYROLL | EXCLUDE | Outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| ATM, CASH WITHDRAWAL | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Nairobi-based IT consultant. Format: KCB Bank statement.

### Example 1 — Domestic B2B revenue (16%)

**Input line:**
`15/04/2025  Credit  SAFARICOM PLC  Invoice KE-2025-041  Ksh 1,160,000  Ksh 5,000,000`

**Reasoning:**
Incoming Ksh 1,160,000 from Safaricom for IT consulting. Standard 16%. Gross 1,160,000 includes VAT. Net = Ksh 1,000,000 + Ksh 160,000 output VAT. Issue ETR receipt or e-invoice; report on VAT-3 Section A.

**Classification:** Output tax 16% — Ksh 160,000. Net: Ksh 1,000,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22/04/2025  Credit  ACME CORP USA  Consulting USD 5,000 (Ksh 645,000)  Ksh 5,645,000`

**Reasoning:**
USD from foreign client for services. Zero-rated if services exported outside Kenya. Evidence: contract, FX payment. Report Ksh 645,000 on Section B. Output tax: Ksh 0.

**Classification:** Zero-rated — Ksh 645,000. Output tax: Ksh 0.

### Example 3 — Electricity (16%)

**Input line:**
`10/04/2025  Debit  KENYA POWER  April bill  -Ksh 11,600  Ksh 4,988,400`

**Reasoning:**
Kenya Power electricity. 16% VAT. Gross Ksh 11,600. Net = Ksh 10,000 + Ksh 1,600 input tax. ETR receipt from KPLC — input credit Ksh 1,600.

**Classification:** Input tax 16% — Ksh 1,600. Net: Ksh 10,000.

### Example 4 — M-Pesa transaction fee (exempt)

**Input line:**
`08/04/2025  Debit  SAFARICOM M-PESA  Transaction fees  -Ksh 232  Ksh 4,988,168`

**Reasoning:**
M-Pesa transaction fee. Mobile money is a financial service — exempt from VAT. No input tax. EXCLUDE from VAT-3.

**Classification:** EXEMPT — no input tax.

### Example 5 — International SaaS (reverse charge)

**Input line:**
`05/04/2025  Debit  GOOGLE IRELAND  Workspace April  -Ksh 3,480  Ksh 4,984,688`

**Reasoning:**
Google Workspace. If Google is not KRA-registered for digital services, the Kenyan business must self-assess 16% VAT. Ksh 3,480 net; self-assessed VAT = Ksh 557. Both output and input in same period for fully taxable business.

**Classification:** Reverse charge — self-assess Ksh 557 output and input. Net: Ksh 0.

### Example 6 — Domestic courier (16%)

**Input line:**
`12/04/2025  Debit  DHL KENYA  Shipping invoice  -Ksh 5,800  Ksh 4,978,888`

**Reasoning:**
DHL courier. 16% VAT. Gross Ksh 5,800. Net = Ksh 5,000 + Ksh 800 input tax. DHL Kenya issues ETR receipts — input credit Ksh 800.

**Classification:** Input tax 16% — Ksh 800. Net: Ksh 5,000.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 16%

Default rate for all taxable supplies. Legislation: VAT Act 2013 (No. 35 of 2013) Section 5.

### 5.2 Zero rate

Second Schedule goods and services: exports, certain agricultural inputs (fertilizers, seeds), medicines, textbooks, ambulance services. Legislation: VAT Act 2013 Second Schedule.

### 5.3 Exempt supplies

First Schedule: financial services, education, medical/health services, raw agricultural products sold by farmers, passenger transport. Legislation: VAT Act 2013 First Schedule.

### 5.4 ETR / e-Invoice requirement

Electronic Tax Register (ETR) receipts required for retail; e-invoices via iTax for B2B. Input tax credit requires a compliant ETR or e-invoice from a KRA VAT-registered supplier.

### 5.5 Withholding VAT

Government departments and designated agents withhold 6% VAT on payments to suppliers; 100% on payments to foreign entities not registered in Kenya. Track withholding tax certificates (WHT-VAT form).

### 5.6 Filing deadlines

| Obligation | Due date |
|---|---|
| VAT-3 return | 20th of following month |
| VAT payment | 20th of following month |
| Late penalty | 5% of unpaid tax + 1% per month interest |

---

## Section 6 — Tier 2 catalogue

### 6.1 Withholding VAT from government clients

**What it shows:** Payment from government that appears less than invoiced.
**What's missing:** WHT-VAT certificate amount.
**Conservative default:** Record full output tax on invoice; offset WHT-VAT certificate.
**Question to ask:** "Do you have the WHT-VAT withholding certificate from the government agency?"

### 6.2 Export service qualification

**What it shows:** Revenue from a foreign client.
**What's missing:** Evidence services were exported.
**Conservative default:** 16%.
**Question to ask:** "Foreign client contract + FX payment evidence available?"

### 6.3 Zero-rated vs. exempt food items

**What it shows:** Grocery or agricultural purchase.
**What's missing:** Whether the specific items are zero-rated (Second Schedule) or simply out of scope.
**Conservative default:** 16% on all.
**Question to ask:** "What exactly was purchased? Itemised receipt available?"

### 6.4 International SaaS — KRA registration status

**What it shows:** Payment to foreign digital provider.
**What's missing:** Whether provider is KRA-registered.
**Conservative default:** Self-assess 16% reverse charge.
**Question to ask:** "Does the foreign provider's invoice show a KRA PIN? If yes, treat as standard. If no, self-assess."

---

## Section 7 — Excel working paper template

```
KENYA VAT-3 WORKING PAPER
Period: ____________  PIN: ____________

A. OUTPUT TAX
  A1. Standard-rated sales 16% (net)           ___________
  A2. Output tax (A1 × 16%)                    ___________
  A3. Zero-rated exports                       ___________
  A4. Exempt sales                             ___________
  A5. Reverse charge output self-assessed      ___________

B. INPUT TAX
  B1. Standard-rated purchases 16% (net)       ___________
  B2. Input tax (B1 × 16%)                     ___________
  B3. Import input tax                         ___________
  B4. Reverse charge input self-assessed       ___________
  B5. Total input (B2+B3+B4)                  ___________
  B6. WHT-VAT credits                          ___________

C. NET VAT
  C1. Net (A2 − B5)                            ___________
  C2. WHT-VAT credits (B6)                     ___________
  C3. Prior credit                             ___________
  C4. Net payable (C1−C2−C3)                   ___________

REVIEWER FLAGS:
  [ ] ETR/e-invoices confirmed?
  [ ] Export evidence held?
  [ ] WHT-VAT certificates collected?
  [ ] Reverse charge self-assessed?
```

---

## Section 8 — Bank statement reading guide

### Common Kenyan bank formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| KCB | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | KES |
| Equity Bank | Date, Narrative, Withdrawal, Deposit, Balance | DD/MM/YYYY | KES |
| Co-op Bank | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | KES |
| ABSA Kenya | Date, Description, Amount, Balance | DD/MM/YYYY | KES |

### Key Kenyan banking terms

| Term | Meaning | Hint |
|---|---|---|
| Credit / Deposit | Incoming | Potential revenue |
| Debit / Withdrawal | Outgoing | Potential expense |
| M-PESA | Mobile money | Check if fee or transfer |
| Bank Charges | Fee | Exempt |
| Interest | Interest | Exempt |
| Balance | Balance | Ignore |

---

## Section 9 — Onboarding fallback

```
KENYA VAT ONBOARDING — MINIMUM QUESTIONS
1. KRA PIN (Personal Identification Number)?
2. VAT registration number?
3. Month covered by this bank statement?
4. Export sales (zero-rated)? Evidence held?
5. Government clients who withhold VAT? WHT-VAT certificates?
6. International SaaS subscriptions — self-assess reverse charge?
7. Prior period excess credit carried forward?
```

---

## Section 10 — Reference material

| Topic | Reference |
|---|---|
| VAT Act | VAT Act 2013 (No. 35 of 2013) |
| Standard rate | Section 5 |
| Zero rate | Second Schedule |
| Exemptions | First Schedule |
| Withholding VAT | Section 17 |
| ETR requirement | Section 27 |
| Penalties | Section 53 |

### Known gaps

- Partial exemption apportionment — escalate
- WHT-VAT reconciliation for large government contracts — specialist
- Digital marketplace complex cross-border — escalate
- Property/land transactions — escalate

### Self-check

- [ ] ETR/e-invoices held for all input credits
- [ ] Export evidence confirmed
- [ ] WHT-VAT certificates collected from government clients
- [ ] Reverse charge self-assessed for foreign digital services
- [ ] Prior credit carried forward correctly

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial |
| 2.0 | April 2026 | v2.0 rewrite |

---

## Prohibitions

- NEVER claim input credit without ETR receipt or compliant e-invoice
- NEVER zero-rate exports without customs documentation or FX evidence
- NEVER ignore WHT-VAT from government clients
- NEVER present calculations as definitive — direct to CPA(K)

---

## Disclaimer

This skill is for informational purposes only. All outputs must be reviewed by a qualified professional. Updated version at openaccountants.com.
