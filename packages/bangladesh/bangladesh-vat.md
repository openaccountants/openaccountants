---
name: bangladesh-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Bangladesh VAT return (Mushak-9.1) or turnover tax return for any client. Trigger on phrases like "prepare VAT return", "Bangladesh VAT", "Mushak", "BIN registration", "NBR filing", or any request involving Bangladesh VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers standard VAT-registered (Article 10 equivalent) and turnover tax filers. Complex multi-establishment structures, bond/export processing zones, and supplementary duty computations are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Bangladesh VAT work.
version: 2.0
---

# Bangladesh VAT Return Skill (Mushak-9.1) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in vat-workflow-base Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | Bangladesh (People's Republic of Bangladesh) |
| Standard rate | 15% |
| Reduced rates | 5%, 7.5%, 10% (specified goods/services via SRO) |
| Turnover tax | 4% (BDT 50 lakh–3 crore turnover); 3% (BDT 30–50 lakh) |
| Zero rate | 0% (exports, deemed exports, supplies to diplomats) |
| Return form | Mushak-9.1 (monthly VAT return); Turnover Tax return (quarterly) |
| Filing portal | https://vat.gov.bd (Mushak Online Portal) |
| Authority | National Board of Revenue (NBR) |
| Currency | BDT (Bangladeshi Taka) |
| Filing frequencies | Monthly (VAT registered); Quarterly (turnover tax) |
| Deadline | Within 15 days after end of period |
| Companion skill (Tier 1, workflow) | vat-workflow-base v0.1 or later — MUST be loaded |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | Pending |

**Key Mushak-9.1 sections (the fields you will use most):**

| Part | Meaning |
|---|---|
| Part 1 | Entity information (BIN, name, period) |
| Part 2 | Output tax on local sales (standard + reduced rates) |
| Part 3 | Output tax on exports (zero-rated) |
| Part 4 | Exempt supplies |
| Part 5 | Total output tax (derived: sum of Part 2) |
| Part 6 | Input tax on local purchases (from Mushak-6.1) |
| Part 7 | Input tax on imports (from Bill of Entry) |
| Part 8 | Total input tax credit (derived: Part 6 + Part 7) |
| Part 9 | Net tax payable or credit carried forward (Part 5 minus Part 8) |
| Part 10 | Supplementary Duty (if applicable) |
| Part 11 | Interest / penalty (if late) |
| Part 12 | Total payable (derived: Parts 9 + 10 + 11) |

**Conservative defaults — Bangladesh-specific values:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Bangladesh |
| Unknown registration type | VAT registered (standard) |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | BDT 500,000 |
| HIGH tax-delta on a single conservative default | BDT 30,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | BDT 1,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Bangladeshi bank: Dutch-Bangla Bank, BRAC Bank, Eastern Bank, City Bank, Standard Chartered BD, HSBC BD, Islami Bank, or any other.

**Recommended** — sales invoices (Mushak-11) for the period, purchase invoices with supplier BIN, the client's BIN in writing (13 digits).

**Ideal** — complete Mushak-6.1 (purchase register), Mushak-6.2 (sales register), prior period Mushak-9.1, reconciliation of excess credit brought forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This Mushak-9.1 was produced from bank statement alone. The reviewer must verify that input VAT claims are supported by compliant Mushak-11 invoices bearing supplier BIN and that all classifications match supporting documents."

### Bangladesh-specific refusal catalogue

**R-BD-1 — Turnover tax client attempting to claim input VAT.** Trigger: client is turnover tax registered (annual turnover BDT 30 lakh to BDT 3 crore). Message: "Turnover tax payers pay a flat 3%/4% on turnover and cannot recover input VAT. This skill can prepare the turnover tax return but cannot calculate input VAT recovery for a turnover tax client."

**R-BD-2 — Export Processing Zone (EPZ) entity.** Trigger: client operates in an EPZ or Special Economic Zone. Message: "EPZ/SEZ entities have special VAT rules outside the standard Mushak-9.1 framework. Please escalate to a qualified chartered accountant familiar with EPZ obligations."

**R-BD-3 — Multi-establishment with separate BINs.** Trigger: client has multiple business units each with a separate BIN. Message: "Each BIN files a separate Mushak-9.1 with inter-establishment transfers on Mushak-6.4. This requires consolidation analysis beyond this skill. Please use a qualified practitioner."

**R-BD-4 — Supplementary Duty computation.** Trigger: client manufactures or imports goods subject to Supplementary Duty (tobacco, alcohol, vehicles, SIM cards). Message: "Supplementary Duty rates vary widely (7.5%–500%) and SD is calculated before VAT. This requires specialist product-level analysis. Please escalate to a qualified chartered accountant."

**R-BD-5 — Withholding VAT agent obligations.** Trigger: client is a designated VDS withholding agent (government entity, bank, NGO, listed company). Message: "VDS withholding obligations require tracking of Mushak-6.10 certificates and deposit schedules. Out of scope for standard return preparation. Please use a qualified practitioner."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Bangladeshi banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DUTCH-BANGLA, DUTCH BANGLA, DBBL | EXCLUDE for bank charges/fees | Financial service, exempt |
| BRAC BANK, BRAC BNK | EXCLUDE for bank charges/fees | Same |
| EASTERN BANK, EBL | EXCLUDE for bank charges/fees | Same |
| CITY BANK, ISLAMI BANK, AB BANK | EXCLUDE for bank charges/fees | Same |
| STANDARD CHARTERED BD, HSBC BD | EXCLUDE for bank charges/fees | Same |
| UCBL, PRIME BANK, MUTUAL TRUST | EXCLUDE for bank charges/fees | Same |
| INTEREST, MUNAFA, PROFIT | EXCLUDE | Interest income/expense, out of scope |
| LOAN, REPAYMENT | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| NBR, NATIONAL BOARD OF REVENUE | EXCLUDE | Tax payment, not a supply |
| VAT DEPARTMENT, MUSHAK | EXCLUDE | VAT payment |
| CUSTOMS, SHULKO | EXCLUDE | Customs duty (but import VAT on Bill of Entry is claimable) |
| BIDA, BOI, RJSC | EXCLUDE | Regulatory/licence fees |
| RAJUK, CDA, KDA | EXCLUDE | Development authority fees |
| INCOME TAX, TAX DEDUCTED | EXCLUDE | Income tax payment |

### 3.3 Utilities

| Pattern | Treatment | Return section | Notes |
|---|---|---|---|
| DESCO, DPDC, BPDB, NESCO, BREB | Domestic 15% | Part 6 | Electricity — overhead |
| TITAS GAS, BAKHRABAD GAS, JALALABAD GAS | Domestic 15% | Part 6 | Gas utility |
| WASA, DHAKA WASA, CHITTAGONG WASA | Domestic 15% | Part 6 | Water supply |
| GRAMEENPHONE, GP, ROBI, BANGLALINK, TELETALK | Domestic 15% | Part 6 | Telecoms — overhead (note: 15% SD also applies to mobile services) |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SADHARAN BIMA, JIBAN BIMA | EXCLUDE | Government insurance, exempt |
| GREEN DELTA, PRAGATI, PIONEER | EXCLUDE | Insurance premium, exempt |
| METLIFE BD, GUARDIAN LIFE | EXCLUDE | Same |

### 3.5 Digital payments and mobile financial services

| Pattern | Treatment | Notes |
|---|---|---|
| BKASH, B-KASH | EXCLUDE for transaction fees | Financial service, exempt |
| NAGAD | EXCLUDE for transaction fees | Same |
| ROCKET, DBBL MOBILE | EXCLUDE for transaction fees | Same |
| UPAY, SURE CASH | EXCLUDE for transaction fees | Same |

### 3.6 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, BETON, WAGES | EXCLUDE | Wages — outside VAT scope |
| PROVIDENT FUND, PF | EXCLUDE | Employee benefit, out of scope |
| GRATUITY | EXCLUDE | Employee benefit |

### 3.7 SaaS and international digital services (reverse charge)

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE, GOOGLE ADS | Google (US/IE entity) | Self-assess 15% | Non-resident digital service |
| MICROSOFT, AZURE, OFFICE 365 | Microsoft (US/IE) | Self-assess 15% | Same |
| META, FACEBOOK ADS | Meta (US/IE) | Self-assess 15% | Same |
| AMAZON AWS, AWS | Amazon (US/LU) | Self-assess 15% | Same |
| ZOOM, SLACK, DROPBOX | US entities | Self-assess 15% | Same |
| CANVA, FIGMA, NOTION | Non-resident | Self-assess 15% | Same |

### 3.8 Professional services (Bangladesh)

| Pattern | Treatment | Return section | Notes |
|---|---|---|---|
| CA FIRM, AUDIT, CHARTERED ACCOUNTANT | Domestic 15% | Part 6 | Deductible if business purpose |
| ADVOCATE, LAWYER, BARRISTER | Domestic 15% | Part 6 | Legal services |
| CONSULTANT, ENGINEERING | Domestic 15% | Part 6 | Professional overhead |

### 3.9 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT, BHARA, OFFICE RENT | Domestic 15% if commercial with VAT invoice | Part 6 |
| HOUSE RENT, RESIDENTIAL | EXCLUDE | Residential lease, exempt |

### 3.10 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL, ACCOUNT TRANSFER | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Out of scope |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |
| DIRECTOR FEE, PROPRIETOR DRAWING | EXCLUDE | Out of scope |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Dhaka-based self-employed IT consultant.

### Example 1 — Standard domestic sale at 15%

**Input line:**
`05.04.2026 ; ABC TECHNOLOGIES LTD ; CREDIT ; Invoice BD-2026-041 IT consultancy ; BDT 115,000`

**Reasoning:**
Domestic sale of IT consulting services to a BDT-paying local company. Standard 15% applies. The gross amount includes VAT. Net = BDT 100,000, VAT = BDT 15,000. Report in Mushak-9.1 Part 2. Mushak-11 tax invoice must be issued.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | ABC TECHNOLOGIES LTD | +115,000 | +100,000 | 15,000 | 15% | Part 2 (output) | N | — |

### Example 2 — Local purchase with input tax credit

**Input line:**
`10.04.2026 ; COMPUTER SOURCE BD ; DEBIT ; Office supplies ; BDT -23,000`

**Reasoning:**
Purchase from a local VAT-registered supplier. Assuming valid Mushak-11 held with supplier BIN. Net = BDT 20,000, VAT = BDT 3,000 at 15%. Input VAT claimable in Part 6.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | COMPUTER SOURCE BD | -23,000 | -20,000 | 3,000 | 15% | Part 6 (input) | N | — |

### Example 3 — Export, zero-rated

**Input line:**
`15.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice BD-EXP-018 Software development ; BDT 350,000`

**Reasoning:**
Export of IT services. Zero-rated under VAT & SD Act 2012 Section 24. Report in Mushak-9.1 Part 3 at 0%. Input VAT on related purchases is fully recoverable. Bank realization certificate required within 6 months.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | STUDIO KREBS GMBH | +350,000 | +350,000 | 0 | 0% | Part 3 (export) | N | — |

### Example 4 — Non-resident digital service (reverse charge)

**Input line:**
`18.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Workspace April ; BDT -2,800`

**Reasoning:**
Service from non-resident. No VAT on invoice. Client must self-assess VAT at 15% under reverse charge (Section 18(3)). Self-assessed output = BDT 420. If used for taxable supplies, input credit of BDT 420 also claimable. Net effect zero for fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | GOOGLE IRELAND LIMITED | -2,800 | -2,800 | 420 | 15% | Part 2 (output) + Part 6 (input) | N | — |

### Example 5 — Blocked input: passenger vehicle

**Input line:**
`22.04.2026 ; TOYOTA BANGLADESH ; DEBIT ; Lease payment Corolla ; BDT -85,000`

**Reasoning:**
Passenger vehicle lease. Input VAT blocked under VAT & SD Act 2012 Section 49 — personal consumption / passenger vehicle unless transport business. IT consultant does not qualify. Full block, zero recovery.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | TOYOTA BANGLADESH | -85,000 | -85,000 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Bank charges, excluded

**Input line:**
`30.04.2026 ; DUTCH-BANGLA BANK ; DEBIT ; Monthly maintenance fee ; BDT -500`

**Reasoning:**
Bank charges are exempt financial services. No VAT. Exclude from VAT return entirely.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Return section | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | DUTCH-BANGLA BANK | -500 | — | — | — | — | N | "Exempt financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (VAT & SD Act 2012, Section 15)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales go to Mushak-9.1 Part 2. Purchases go to Part 6.

### 5.2 Reduced rates (Third Schedule, various SROs)

5%, 7.5%, or 10% on specified goods/services as gazetted via Statutory Regulatory Orders. Each reduced rate has its own line in Part 2. Check current SRO schedule before classifying.

### 5.3 Zero rate (Section 24-25)

Exports of goods (with customs documentation), deemed exports (EPZ supplies), supplies to diplomats, international transport. Report in Part 3. Input VAT on related purchases fully recoverable.

### 5.4 Exempt supplies (First Schedule)

Agricultural products, certain food items, education, health services, land transport, financial services. Report in Part 4. No output VAT, no input VAT recovery on related costs.

### 5.5 Input tax credit — eligibility (Section 45-52)

Purchase must be used for making taxable supplies. Valid Mushak-11 with supplier BIN required. Claim within 3 return periods from invoice date.

### 5.6 Input tax credit — apportionment

If business makes both taxable and exempt supplies: creditable input = total input x (taxable supplies / total supplies). Annual adjustment required. Flag for reviewer.

### 5.7 Blocked input VAT (Section 49)

Zero VAT recovery regardless of other rules: personal consumption, passenger vehicles (unless transport business), entertainment (unless documented promotion), purchases without valid Mushak-11, purchases from unregistered suppliers, goods lost/stolen/destroyed (unless insured), free samples (unless documented promotional). Check blocked status FIRST before applying any recovery.

### 5.8 Imports

VAT at 15% on (assessable value + customs duty). Paid at customs. Input credit claimable in Part 7 if goods used for taxable supplies.

### 5.9 Reverse charge on imported services (Section 18(3))

Non-resident service provider with no BIN: client self-assesses 15% output VAT. Input credit claimable if used for taxable supplies. Net effect zero for fully taxable client.

### 5.10 Capital goods

Full credit in period of acquisition if used entirely for taxable supplies. If mixed use (taxable and exempt), apportionment applies — flag for reviewer.

### 5.11 Credit notes (Section 57)

Supplier reduces output VAT in period of credit note. Buyer reverses input VAT. Both update Mushak-6.1/6.2. Register in Mushak-6.2.1.

### 5.12 Time of supply (Section 14)

VAT chargeable at the earlier of: invoice date, payment receipt, or delivery. Advance payments trigger VAT at receipt.

### 5.13 Turnover tax (simplified)

Turnover tax payers file quarterly. Rate: 4% (BDT 50 lakh–3 crore) or 3% (BDT 30–50 lakh). No input credit. No reverse charge. Report total turnover and flat-rate tax only.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

Pattern: petrol station, CNG, Padma Oil, Jamuna Oil. Why insufficient: vehicle type unknown. If passenger car, blocked. If commercial vehicle for business, deductible. Default: 0% recovery. Question: "Is this for a commercial vehicle used exclusively for business?"

### 6.2 Entertainment and meals

Pattern: restaurant, hotel dining, catering. Why insufficient: entertainment blocked unless documented business promotion. Default: block. Question: "Was this documented promotional entertainment with supporting records?"

### 6.3 Ambiguous SaaS billing entities

Pattern: Google, Microsoft, Meta, Amazon where legal entity not visible. Why insufficient: same brand can bill from various entities. Default: self-assess 15% reverse charge. Question: "Could you check the invoice for the legal entity name and country?"

### 6.4 Round-number incoming transfers

Pattern: large round credit from owner-matching name. Default: exclude as proprietor injection. Question: "Is this a customer payment, your own capital injection, or a loan?"

### 6.5 Incoming transfers from individuals

Pattern: incoming from private-looking counterparties. Default: domestic sale at 15% (Part 2). Question: "Was this a sale? If so, what goods/services?"

### 6.6 Cash withdrawals

Pattern: ATM, cash withdrawal. Default: exclude as proprietor drawing. Question: "What was the cash used for?"

### 6.7 Mixed-use phone and internet

Pattern: Grameenphone, Robi, Banglalink personal lines. Default: 0% recovery if mixed use. Question: "Is this a dedicated business line or personal/mixed?"

### 6.8 Rent payments

Pattern: monthly rent to landlord. Default: no input credit (no invoice assumed). Question: "Does the landlord issue a Mushak-11 with their BIN?"

### 6.9 Outgoing transfers to individuals

Pattern: outgoing to private names. Default: exclude as drawings/wages. Question: "Was this a contractor payment with invoice, wages, or personal transfer?"

### 6.10 Import-related payments

Pattern: LC, shipping, freight forwarder. Why insufficient: need Bill of Entry to determine VAT paid at customs. Default: exclude until Bill of Entry provided. Question: "Please provide the customs Bill of Entry showing VAT paid."

---

## Section 7 — Excel working paper template (Bangladesh-specific)

The base specification is in vat-workflow-base Section 3. This section provides the Bangladesh-specific overlay.

### Sheet "Transactions"

Columns A-L per the base. Column H ("Return section") accepts: Part 2, Part 3, Part 4, Part 6, Part 7, or blank for excluded transactions. For reverse-charge transactions, enter "Part 2 + Part 6" in column H.

### Sheet "Return Summary"

One row per Mushak-9.1 part:

```
| Part 2  | Output tax on local sales      | =SUMIFS(Transactions!F:F, Transactions!H:H, "Part 2") |
| Part 3  | Export sales (zero-rated)       | =SUMIFS(Transactions!E:E, Transactions!H:H, "Part 3") |
| Part 4  | Exempt supplies                | =SUMIFS(Transactions!E:E, Transactions!H:H, "Part 4") |
| Part 5  | Total output tax               | =Return_Summary!C[Part2_row] |
| Part 6  | Input tax local purchases      | =SUMIFS(Transactions!F:F, Transactions!H:H, "Part 6") |
| Part 7  | Input tax imports              | =SUMIFS(Transactions!F:F, Transactions!H:H, "Part 7") |
| Part 8  | Total input tax credit         | =C[Part6_row]+C[Part7_row] |
| Part 9  | Net tax payable                | =C[Part5_row]-C[Part8_row] |
| Part 12 | Total payable                  | =MAX(C[Part9_row],0) |
```

### Sheet "Return Form"

Final Mushak-9.1-ready figures. If Part 8 > Part 5, excess credit carried forward (no refund claim via this skill).

---

## Section 8 — Bank statement reading guide

Follow the universal exclusion rules in vat-workflow-base Step 6, plus these Bangladesh-specific patterns.

**CSV format conventions.** Dutch-Bangla and BRAC Bank exports typically use comma delimiters with DD/MM/YYYY dates. Common columns: Date, Description, Debit, Credit, Balance.

**Bengali/Bangla language variants.** Some descriptions may appear in Bangla script. Treat transliterated equivalents the same as English.

**Internal transfers and exclusions.** Own-account transfers between client's DBBL, BRAC, bKash accounts. Always exclude.

**Proprietor draws.** Self-employed sole proprietors cannot pay themselves wages. Any transfer to personal account is a drawing. Exclude.

**bKash/Nagad transactions.** Mobile financial service transactions appear as "BKASH", "NAGAD". Transaction fees are exempt. The underlying payment may be a sale or purchase — classify based on counterparty, not the payment method.

**Foreign currency transactions.** Convert to BDT at the transaction date rate. Use Bangladesh Bank reference rate.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
Inference: sole trader names match account holder; company names end in "Ltd", "Limited", "Pvt Ltd". Fallback: "Are you a sole proprietor, partnership, or company?"

### 9.2 Registration type
Inference: if asking for Mushak-9.1, VAT registered. If turnover below BDT 3 crore, may be turnover tax. Fallback: "Are you VAT registered (BIN holder, 15%) or turnover tax (3-4%)?"

### 9.3 BIN
Inference: 13-digit BIN may appear in payment descriptions. Fallback: "What is your 13-digit BIN?"

### 9.4 Filing period
Inference: first and last transaction dates. Monthly for VAT registered. Fallback: "Which month does this cover?"

### 9.5 Industry
Inference: counterparty mix, sales descriptions. Fallback: "What does the business do?"

### 9.6 Exempt supplies
Inference: presence of medical/educational/financial income. Fallback: "Do you make any VAT-exempt sales?" If yes and significant, apportionment required.

### 9.7 Exports
Inference: foreign currency incoming, foreign counterparties. Fallback: "Do you export goods or services?"

### 9.8 Credit brought forward
Not inferable. Always ask: "Do you have excess credit from the prior period?"

---

## Section 10 — Reference material

### Sources

1. Value Added Tax and Supplementary Duty Act 2012 — Sections 2, 5, 14, 15, 18, 24, 25, 45-52, 57, 107, 109-130
2. VAT & SD Rules 2016 — Rules 40-47, Mushak form series
3. NBR Statutory Regulatory Orders (SROs) for reduced rates and exemptions
4. NBR Mushak Online Portal — https://vat.gov.bd

### Known gaps

1. Supplier pattern library covers major Bangladeshi banks and utilities but not every local vendor. Add patterns as they emerge.
2. Supplementary Duty computation is refused (R-BD-4) — a future version should add SD for common categories.
3. SRO-based reduced rates change frequently. Verify current SRO schedule before each filing period.
4. Multi-establishment (separate BIN) consolidation is refused (R-BD-3).
5. Worked examples are for a hypothetical IT consultant in Dhaka. Sector-specific examples (garments, pharmaceuticals) should be added in v2.1.

### Change log

- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure. Supplier pattern library added (Section 3). Worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template specification added (Section 7). Bank statement reading guide added (Section 8). Onboarding moved to fallback role (Section 9).
- v1.1: Previous monolithic version with full Mushak form mappings and test suite.

### Self-check

1. Quick reference at top with return sections and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 10 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 13 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 10 items).
6. Excel template specification: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 8 items).
8. All 5 Bangladesh-specific refusals present: yes (Section 2).
9. Reference material at bottom: yes (Section 10).
10. Blocked input VAT explicit: yes (Section 5.7 + Example 5).

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
