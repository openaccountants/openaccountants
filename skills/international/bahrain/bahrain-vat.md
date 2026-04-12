---
name: bahrain-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Bahrain VAT return for any client. Trigger on phrases like "prepare VAT return", "Bahrain VAT", "NBR return", "file VAT Bahrain", or any request involving Bahrain VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Bahrain VAT classification rules, return box mappings, deductibility rules, reverse charge treatment, GCC transitional provisions, and filing deadlines. Bahrain applies VAT at 10% under Decree-Law No. 48 of 2018, administered by the National Bureau for Revenue (NBR). ALWAYS read this skill before touching any Bahrain VAT-related work.
version: 2.0
---

# Bahrain VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Kingdom of Bahrain |
| Standard rate | 10% (increased from 5% on 1 January 2022) |
| Reduced rates | None |
| Zero rate | 0% (exports, international transport, oil/gas, new buildings for residential use, specified foodstuffs, healthcare, education) |
| Exempt supplies | Financial services (margin-based), bare land, local passenger transport, residential rental |
| Return form | NBR VAT Return (electronic, via NBR portal) |
| Filing portal | https://www.nbr.gov.bh |
| Authority | National Bureau for Revenue (NBR) |
| Currency | BHD (Bahraini Dinar) |
| Filing frequency | Monthly (turnover > BHD 3,000,000); Quarterly (all others) |
| Deadline | Last day of month following period end |
| Mandatory registration | BHD 37,500 annual taxable supplies |
| Voluntary registration | BHD 18,750 annual taxable supplies |
| Primary legislation | Decree-Law No. 48 of 2018; Resolution No. 12 of 2018 (Executive Regulations); Resolution No. 33 of 2021 (rate increase) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending -- requires validation by licensed Bahrain tax advisor |
| Validation date | Pending |
| Last research update | April 2026 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Bahrain |
| Unknown B2B vs B2C for GCC customer | B2C, charge 10% |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the period in CSV, PDF, or pasted text covering the full period. Acceptable from NBB, BBK, Ahli United, BisB, SICO, Al Baraka, Ithmaar, or any other Bahraini or international bank.

**Recommended** -- sales invoices (especially for zero-rated and GCC supplies), purchase invoices for any input VAT claim above BHD 50, the client's VAT registration number.

**Ideal** -- complete invoice register, prior period VAT return, reconciliation of credit brought forward.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement at all, hard stop. If bank statement only without invoices, proceed but record: "This return was produced from bank statement alone. Reviewer must verify input VAT claims are supported by compliant tax invoices."

### Refusal catalogue

**R-BH-1 -- VAT group intra-group supplies.** Trigger: client is part of a VAT group. Message: "Intra-group supplies within a Bahrain VAT group are outside the scope of VAT. This skill does not handle VAT group consolidation. Escalate to licensed tax advisor."

**R-BH-2 -- Oil and gas sector.** Trigger: client operates in upstream oil/gas. Message: "Oil and gas operations have specific zero-rating rules under Article 68. Escalate to specialist tax advisor."

**R-BH-3 -- Partial exemption complex.** Trigger: client makes both taxable and exempt supplies with no agreed pro-rata. Message: "Partial exemption requires an NBR-agreed apportionment method. Escalate to licensed tax advisor."

---

## Section 3 -- Supplier pattern library

Match by case-insensitive substring on counterparty name. If none match, fall through to Section 5.

### 3.1 Bahraini banks (fees: exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| NBB, NATIONAL BANK OF BAHRAIN | EXCLUDE for bank charges/fees | Margin-based financial service, exempt |
| BBK, BANK OF BAHRAIN AND KUWAIT | EXCLUDE for bank charges/fees | Same |
| AHLI UNITED, AUB | EXCLUDE for bank charges/fees | Same |
| BISB, AL SALAM BANK | EXCLUDE for bank charges/fees | Same |
| AL BARAKA, ITHMAAR | EXCLUDE for bank charges/fees | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Financial transaction, out of scope |

### 3.2 Government and regulatory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| NBR, NATIONAL BUREAU FOR REVENUE | EXCLUDE | Tax payment |
| LMRA, LABOUR MARKET | EXCLUDE | Government levy |
| SIO, SOCIAL INSURANCE | EXCLUDE | Social insurance contribution |
| MOIC, MINISTRY OF INDUSTRY | EXCLUDE | Government fee |
| CUSTOMS, BAHRAIN CUSTOMS | Check for import VAT | Customs duty exclude; import VAT recoverable |
| TAMKEEN | EXCLUDE | Government support |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EWA, ELECTRICITY AND WATER | Domestic 10% | Standard-rated utility |
| BATELCO, STC BAHRAIN, ZAIN BAHRAIN | Domestic 10% | Telecoms, standard-rated |

### 3.4 SaaS and digital services

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Typically non-GCC | Reverse charge 10% | Non-resident digital service |
| AWS, AMAZON WEB SERVICES | Non-GCC or GCC entity -- check | Reverse charge 10% | Verify billing entity |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | US entities | Reverse charge 10% | Non-resident |

### 3.5 Insurance (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SOLIDARITY, AXA BAHRAIN, GIG BAHRAIN | EXCLUDE | Life insurance exempt; general insurance at 10% -- check policy type |

### 3.6 Payroll and transfers (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, PAYROLL | EXCLUDE | Employment cost, out of scope |
| GOSI, SOCIAL INSURANCE ORGANIZATION | EXCLUDE | Social insurance |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Out of scope |

---

## Section 4 -- Worked examples

### Example 1 -- Reverse charge on non-resident SaaS

**Input line:** `05.01.2026 ; NOTION LABS INC ; DEBIT ; Monthly plan ; USD 16.00 ; BHD 6.03`

**Reasoning:** Notion Labs Inc is a US entity. No VAT on invoice. Non-resident supplying services to Bahrain. Reverse charge at 10%. Both output and input reported. Net effect zero for fully taxable business.

**Output:**

| Date | Counterparty | Net | VAT | Rate | Output box | Input box |
|---|---|---|---|---|---|---|
| 05.01.2026 | NOTION LABS INC | 6.03 | 0.60 | 10% | Imported services output | Imported services input |

### Example 2 -- Standard domestic sale

**Input line:** `10.01.2026 ; AL JAZEERA TRADING ; CREDIT ; Invoice 2026-001 ; +5,000.00 ; BHD`

**Reasoning:** Domestic sale to Bahraini customer. Standard rate 10%. Output VAT = BHD 500.

**Output:**

| Date | Counterparty | Net | VAT | Rate | Box |
|---|---|---|---|---|---|
| 10.01.2026 | AL JAZEERA TRADING | 5,000.00 | 500.00 | 10% | Standard rated sales |

### Example 3 -- Entertainment (blocked)

**Input line:** `15.01.2026 ; GULF HOTEL BAHRAIN ; DEBIT ; Client dinner ; -250.00 ; BHD`

**Reasoning:** Entertainment expense. Input VAT blocked under Ministerial Order No. 14/2019. No recovery.

**Output:**

| Date | Counterparty | Gross | Net | VAT recovery | Note |
|---|---|---|---|---|---|
| 15.01.2026 | GULF HOTEL BAHRAIN | 250.00 | 250.00 | 0 | Blocked: entertainment |

---

## Section 5 -- Classification rules

### 5.1 Standard rate 10%

Default rate for all taxable supplies not specifically zero-rated or exempt. Applies to most goods and services supplied in Bahrain.

Legislation: Decree-Law No. 48/2018, Article 56.

### 5.2 Zero-rated supplies (0%, input VAT recoverable)

- Exports of goods outside Bahrain (with proof)
- Exports of services to non-GCC recipients
- International transport of goods and passengers
- First supply of new residential buildings (within 3 years of completion)
- Specified foodstuffs (basic necessities list per NBR)
- Healthcare services (by licensed providers)
- Education services (by licensed institutions)
- Oil and gas sector supplies (Article 68)
- Supplies to qualifying free zones

Legislation: Decree-Law No. 48/2018, Articles 59-68.

### 5.3 Exempt supplies (no VAT, no input recovery)

- Financial services (margin-based: interest, forex spreads)
- Bare land
- Local passenger transport
- Residential rental
- Life insurance

Legislation: Decree-Law No. 48/2018, Articles 64-68.

### 5.4 GCC transitional rules

- Supplies to VAT-registered businesses in implementing states (SA, UAE, OM): standard-rated in Bahrain at 10%
- Supplies to non-implementing states (KW, QA): treated as exports (zero-rated) for goods; services follow place-of-supply rules
- Imports from GCC implementing states: reverse charge applies

Legislation: GCC Unified VAT Agreement; Decree-Law No. 48/2018.

---

## Section 6 -- VAT return form structure

### Output section

| Box | Description | Mapping |
|---|---|---|
| 1 | Standard rated sales (10%) | Domestic taxable supplies |
| 2 | Sales to GCC registered customers | Intra-GCC taxable |
| 3 | Zero-rated domestic sales | Healthcare, education, new buildings, foodstuffs |
| 4 | Zero-rated exports | Exports outside Bahrain/GCC |
| 5 | Exempt sales | Financial, land, residential rental |
| 6 | Total sales | Sum |
| 7 | Output VAT on standard rated | 10% of Box 1+2 |
| 8 | Adjustments to output | Credit notes |
| 9 | VAT on imports (goods) | Customs VAT |
| 10 | VAT on imports (services) | Reverse charge output |
| 11 | Total output VAT | 7+8+9+10 |

### Input section

| Box | Description | Mapping |
|---|---|---|
| 12 | Standard rated purchases | Local purchases with VAT |
| 13 | Imports (goods) | From customs entries |
| 14 | Imports (services) | Reverse charge input |
| 15 | Total input VAT | Sum of allowable input |
| 16 | Adjustments | Blocked items, apportionment |
| 17 | Allowable input VAT | 15 minus 16 |

### Net calculation

| Box | Description | Formula |
|---|---|---|
| 18 | Net VAT | 11 minus 17 |
| 19 | Credit brought forward | Prior period |
| 20 | Net payable / (refundable) | 18 minus 19 |

---

## Section 7 -- Reverse charge and imports

### Reverse charge on imported services

When a Bahrain VAT-registered person receives services from a non-resident not registered in Bahrain:
1. Self-assess output VAT at 10% (Box 10)
2. Claim input VAT at 10% (Box 14) if for taxable supplies
3. Net effect zero for fully taxable businesses

Legislation: Decree-Law No. 48/2018, Article 34.

### Import of goods

- VAT at 10% on CIF value plus customs duty
- Collected by Bahrain Customs at point of entry
- Recoverable as input VAT if goods are for taxable supplies

### GCC imports

- Goods from GCC implementing states: reverse charge mechanism
- Goods from non-implementing states: treated as third-country imports

---

## Section 8 -- Deductibility and blocked input

### Blocked input tax

Legislation: Ministerial Order No. 14/2019.

- Motor vehicles for personal transport (unless taxi, car hire, driving instruction, or dealer stock)
- Entertainment, hospitality, and recreation
- Personal-use goods and services
- Club memberships (recreational)
- Purchases without valid tax invoice

### Partial exemption

If business makes both taxable and exempt supplies, input VAT on common costs must be apportioned.

`Recovery % = Taxable Supplies / Total Supplies * 100`

Reviewer must confirm method with NBR.

---

## Section 9 -- Filing, deadlines, and penalties

| Obligation | Period | Deadline |
|---|---|---|
| VAT return (monthly) | Monthly | Last day of month following period |
| VAT return (quarterly) | Quarterly | Last day of month following quarter |
| Payment | Same as return | Same deadline |

### Penalties

| Violation | Penalty |
|---|---|
| Late filing | BHD 500 minimum; 5% of unpaid tax for each month |
| Late payment | 5% of unpaid tax per month |
| Failure to register | BHD 5,000 to BHD 10,000 |
| Incorrect return | BHD 1,000 to BHD 5,000 |
| Tax evasion | BHD 10,000 minimum + imprisonment |

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- SaaS from US provider.** Company subscribes to AWS. No VAT on invoice. Resolution: reverse charge at 10%. Output Box 10, input Box 14. Net zero.

**EC2 -- Export of goods.** Bahraini manufacturer ships goods to Oman. Resolution: zero-rated export (Box 4). Input VAT fully recoverable.

**EC3 -- Motor vehicle (blocked).** Company buys sedan for director. Resolution: input VAT blocked. Full cost including irrecoverable VAT.

**EC4 -- GCC supply to non-implementing state.** Sale of goods to Qatar. Resolution: treated as export, zero-rated for goods.

**EC5 -- New residential building.** Developer sells newly built apartment within 3 years. Resolution: zero-rated (first supply of new residential property). Input VAT recoverable.

**EC6 -- Financial services (exempt).** Bank earns interest income. Resolution: exempt supply. No output VAT. Related input VAT not recoverable.

**EC7 -- Mixed supply.** Company provides both taxable consulting and exempt financial advisory. Resolution: partial exemption applies. Reviewer must confirm apportionment.

**EC8 -- Credit note.** Supplier issues credit note for returned goods. Resolution: reduce output VAT in period issued. Buyer adjusts input VAT.

### Test suite

**Test 1 -- Standard sale.** Input: company sells goods BHD 10,000 net. Expected: output VAT = BHD 1,000 (10%).

**Test 2 -- Local purchase.** Input: company buys supplies BHD 5,000 + BHD 500 VAT. Expected: input VAT BHD 500 recoverable.

**Test 3 -- Reverse charge.** Input: company receives IT services from UK firm, BHD 2,000, no VAT. Expected: output VAT BHD 200, input VAT BHD 200. Net zero.

**Test 4 -- Export.** Input: exporter ships goods BHD 50,000. Expected: zero-rated. No output VAT. Input recoverable.

**Test 5 -- Blocked entertainment.** Input: client dinner BHD 300 + BHD 30 VAT. Expected: input VAT = 0 (blocked).

**Test 6 -- Exempt supply.** Input: bank earns interest BHD 100,000. Expected: exempt. No VAT. Related input not recoverable.

### Reviewer escalation protocol

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list treatments]
Recommended: [which and why]
Action Required: Licensed Bahrain tax advisor must confirm.
```

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [outside scope]
Action Required: Do not classify. Refer to licensed tax advisor.
```

### Out of scope -- direct tax

- Corporate Income Tax: 0% (no CIT in Bahrain)
- Personal Income Tax: None
- Social insurance (GOSI): employer 12%, employee 7% (Bahraini); employer 3%, employee 1% (non-Bahraini)
- Excise tax: tobacco 100%, energy drinks 100%, carbonated drinks 50%

### Prohibitions

- NEVER apply any rate other than 10%, 0%, or exempt
- NEVER allow input VAT recovery on blocked categories
- NEVER ignore reverse charge on services from non-residents
- NEVER treat non-implementing GCC states (Kuwait, Qatar) as implementing states
- NEVER compute any number -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER accept invoices without valid VAT registration number for input claims

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
