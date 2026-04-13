---
name: oman-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Oman VAT return for any client. Trigger on phrases like "prepare VAT return", "Oman VAT", "OTA return", or any request involving Oman VAT filing. Oman applies VAT at 5% under Royal Decree No. 121/2020, administered by the Oman Tax Authority (OTA). ALWAYS read this skill before touching any Oman VAT-related work.
version: 2.0
---

# Oman VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Sultanate of Oman |
| Standard rate | 5% |
| Zero rate | 0% (exports, international transport, oil/gas exploration, healthcare, education, specified foodstuffs, first supply of residential property) |
| Exempt supplies | Financial services (margin-based), bare land, local passenger transport, residential rental |
| Return form | OTA VAT Return (electronic) |
| Filing portal | https://www.taxoman.gov.om |
| Authority | Oman Tax Authority (OTA) |
| Currency | OMR (Omani Rial) |
| Filing frequency | Monthly or Quarterly (assigned by OTA) |
| Deadline | Last day of month following period end |
| Mandatory registration | OMR 38,500 annual taxable supplies |
| Voluntary registration | OMR 19,250 annual taxable supplies or expenditure |
| Primary legislation | Royal Decree No. 121/2020; Ministerial Decision No. 53/2021 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 5% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Oman |
| Unknown blocked-input status | Blocked |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the period. Acceptable from Bank Muscat, NBO, Bank Dhofar, Sohar International, OAB, Alizz Islamic, or any other bank.

**Recommended** -- sales invoices, purchase invoices for input claims above OMR 20, client VAT registration number.

**Ideal** -- complete invoice register, prior period return, credit brought forward reconciliation.

### Refusal catalogue

**R-OM-1 -- VAT group.** Trigger: client is part of a VAT group. Message: "VAT group consolidation is outside this skill. Escalate to licensed tax advisor."

**R-OM-2 -- Free zone / SEZ.** Trigger: client operates in designated free zone. Message: "Free zone and SEZ entities have specific VAT treatment. Escalate to specialist."

**R-OM-3 -- Partial exemption.** Trigger: mixed taxable and exempt supplies without agreed method. Message: "Partial exemption requires OTA-agreed apportionment. Escalate."

---

## Section 3 -- Supplier pattern library

### 3.1 Omani banks (fees: exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANK MUSCAT, BANKMUSCAT | EXCLUDE | Margin-based financial service |
| NBO, NATIONAL BANK OF OMAN | EXCLUDE | Same |
| BANK DHOFAR | EXCLUDE | Same |
| SOHAR INTERNATIONAL, SOHAR BANK | EXCLUDE | Same |
| OAB, OMAN ARAB BANK | EXCLUDE | Same |
| ALIZZ ISLAMIC | EXCLUDE | Same |
| INTEREST, LOAN REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government and regulatory

| Pattern | Treatment | Notes |
|---|---|---|
| OTA, OMAN TAX AUTHORITY | EXCLUDE | Tax payment |
| CUSTOMS, ROYAL OMAN POLICE | EXCLUDE | Government levy (check for import VAT separately) |
| PASI, PUBLIC AUTHORITY FOR SOCIAL INSURANCE | EXCLUDE | Social insurance |
| MINISTRY | EXCLUDE | Government fee |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| NAMA, MAZOON, MUSCAT ELECTRICITY | Domestic 5% | Electricity |
| OMANTEL, OOREDOO OMAN | Domestic 5% | Telecoms |
| HAYA WATER | Domestic 5% | Water/wastewater |

### 3.4 SaaS and digital services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 5% | Non-resident digital |
| AWS, ZOOM, SLACK, NOTION | Reverse charge 5% | Non-resident |
| ANTHROPIC, OPENAI, GITHUB, FIGMA | Reverse charge 5% | Non-resident |

### 3.5 Payroll and transfers

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Out of scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| DIVIDEND | EXCLUDE | Out of scope |

---

## Section 4 -- Worked examples

### Example 1 -- Non-resident SaaS reverse charge

**Input:** `03.01.2026 ; ZOOM VIDEO COMMUNICATIONS ; DEBIT ; Monthly ; USD 14.99 ; OMR 5.77`

Zoom is US entity. No VAT on invoice. Reverse charge at 5%. Output and input both reported. Net zero.

### Example 2 -- Standard domestic sale

**Input:** `10.01.2026 ; MUSCAT TRADING CO ; CREDIT ; Invoice 001 ; +2,000.00 ; OMR`

Domestic sale. Standard rate 5%. Output VAT = OMR 100.

### Example 3 -- Blocked motor vehicle

**Input:** `20.01.2026 ; TOYOTA OMAN ; DEBIT ; Sedan purchase ; -8,000.00 ; OMR`

Motor vehicle < 9 seats for personal transport. Input VAT blocked.

---

## Section 5 -- Classification rules

### 5.1 Standard rate 5%

Default rate for all taxable supplies. Legislation: Royal Decree 121/2020, Art. 41.

### 5.2 Zero-rated supplies (0%, input recoverable)

- Exports of goods outside Oman
- International transport
- First supply of residential property (within 3 years)
- Healthcare and education (licensed providers)
- Specified basic foodstuffs
- Oil and gas exploration/production
- Financial services for explicit fees to non-residents
- Supplies to designated free zones

Legislation: Royal Decree 121/2020, Art. 42-46.

### 5.3 Exempt supplies

- Financial services (margin-based)
- Bare land
- Local passenger transport
- Residential rental
- Life insurance

Legislation: Royal Decree 121/2020, Art. 47-50.

### 5.4 GCC transitional rules

Same framework as Bahrain. Qatar and Kuwait treated as non-GCC (non-implementing).

---

## Section 6 -- VAT return form structure

### Output section

| Box | Description |
|---|---|
| 1 | Standard rated supplies (5%) |
| 2 | Zero-rated supplies |
| 3 | Exempt supplies |
| 4 | Total supplies |
| 5 | Output VAT on standard rated |
| 6 | Output VAT on imports of goods (customs) |
| 7 | Output VAT on imports of services (reverse charge) |
| 8 | Adjustments |
| 9 | Total output VAT |

### Input section

| Box | Description |
|---|---|
| 10 | Input VAT on local purchases |
| 11 | Input VAT on imports |
| 12 | Input VAT on imported services (reverse charge) |
| 13 | Capital goods input VAT |
| 14 | Adjustments (blocked, apportionment) |
| 15 | Total allowable input VAT |

### Net calculation

| Box | Description |
|---|---|
| 16 | Net VAT (9 minus 15) |
| 17 | Credit brought forward |
| 18 | Net payable / (refundable) |

---

## Section 7 -- Reverse charge and imports

When a VAT-registered person receives services from a non-resident not registered in Oman:
1. Self-assess output VAT at 5%
2. Claim input VAT at 5% if for taxable supplies
3. Net zero for fully taxable businesses

Import of goods: VAT at 5% on CIF plus customs duty. Collected by Oman Customs. Recoverable if for taxable supplies.

Legislation: Royal Decree 121/2020, Art. 36.

---

## Section 8 -- Deductibility and blocked input

Blocked categories (Ministerial Decision No. 54/2021):
- Motor vehicles < 9 seats (unless taxi/hire/dealer)
- Entertainment and hospitality
- Personal-use items
- Club memberships (recreational)
- Purchases without valid tax invoice

Partial exemption: turnover-based apportionment, OTA approval required.

---

## Section 9 -- Filing, deadlines, and penalties

| Obligation | Deadline |
|---|---|
| VAT return | Last day of month following period |
| Payment | Same |

| Violation | Penalty |
|---|---|
| Late filing | OMR 25 per day (max OMR 2,500) |
| Late payment | 1% per month on unpaid amount |
| Failure to register | OMR 5,000 |
| Tax evasion | Fines and imprisonment |

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- SaaS reverse charge.** Reverse charge at 5%. Net zero.

**EC2 -- Export of goods.** Zero-rated. Input recoverable.

**EC3 -- Motor vehicle blocked.** No input recovery.

**EC4 -- GCC supply to Qatar.** Treated as export for goods (zero-rated).

**EC5 -- Healthcare supply.** Zero-rated if by licensed provider.

**EC6 -- Residential property first sale.** Zero-rated within 3 years of completion.

**EC7 -- Free zone supply.** May be zero-rated. Verify certificate.

**EC8 -- Credit note.** Adjust output VAT in period issued.

### Test suite

**Test 1 -- Standard sale.** Input: OMR 10,000 net. Expected: output VAT = OMR 500 (5%).

**Test 2 -- Local purchase.** Input: OMR 5,000 + OMR 250 VAT. Expected: input VAT OMR 250 recoverable.

**Test 3 -- Reverse charge.** Input: UK services OMR 3,000. Expected: output OMR 150, input OMR 150. Net zero.

**Test 4 -- Export.** Input: goods OMR 50,000. Expected: zero-rated. Input recoverable.

**Test 5 -- Blocked.** Input: entertainment OMR 500 + OMR 25 VAT. Expected: input = 0.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate Income Tax: 15% (standard)
- Personal Income Tax: None
- Social insurance (PASI): employer 11.5%, employee 7%
- Excise tax: tobacco 100%, energy drinks 100%, carbonated 50%, alcohol 100%, pork 100%

### Prohibitions

- NEVER apply any rate other than 5%, 0%, or exempt
- NEVER allow input recovery on blocked categories
- NEVER ignore reverse charge on non-resident services
- NEVER treat Kuwait/Qatar as GCC implementing states
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit brought forward

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
