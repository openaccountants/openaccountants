---
name: jamaica-gct
description: Use this skill whenever asked to prepare, review, or classify transactions for a Jamaica GCT (General Consumption Tax) return (Form GCT-R) for any client. Trigger on phrases like "prepare GCT return", "Jamaica VAT", "GCT return", "TAJ filing", or any request involving Jamaica consumption tax filing. This skill covers standard GCT-registered businesses only. Free-zone entities and approved farmer/manufacturer schemes are in the refusal catalogue. ALWAYS read this skill before touching any Jamaica GCT work.
version: 2.0
---

# Jamaica GCT Return Skill (Form GCT-R) v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Jamaica |
| Standard rate | 15% |
| Special rate | 25% (telephone services and handsets) |
| Zero rate | Exports, international transport, supplies to diplomats, certain agricultural inputs, supplies to free-zone entities |
| Exempt supplies | Unprocessed agricultural produce, basic food items (flour, rice, cornmeal, chicken backs/necks), medical/dental services, education, financial services (interest, life insurance), residential rental, public transport, water/electricity (domestic thresholds), petroleum (subject to SCT) |
| Return form | GCT-R |
| Filing portal | https://www.jamaicatax.gov.jm |
| Authority | Tax Administration Jamaica (TAJ) |
| Currency | JMD (Jamaican Dollar) |
| Filing frequency | Monthly (standard); bi-monthly (approved small taxpayers) |
| Deadline | 25th of month following period |
| Registration threshold | JMD 15,000,000 annual taxable supplies |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires sign-off by licensed ICATT accountant |
| Validation date | Pending |

**Key GCT-R lines:**

| Line | Meaning |
|---|---|
| 1 | Taxable supplies at 15% (net) |
| 2 | GCT on taxable supplies (output) |
| 3 | Zero-rated supplies |
| 4 | Exempt supplies |
| 5 | Total supplies |
| 6 | GCT on imports (customs C78) |
| 7 | Total output tax (2+6) |
| 8 | Input GCT on local purchases |
| 9 | Input GCT on imports (C78) |
| 10 | Total input tax (8+9) |
| 11 | Adjustments (blocked/apportioned) |
| 12 | Net input tax claimable (10-11) |
| 13 | Net GCT payable/refundable (7-12) |
| 14 | Credit brought forward |
| 15 | Net amount payable/refundable (13-14) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% |
| Unknown GCT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Jamaica |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | JMD 500,000 |
| HIGH tax-delta on a single conservative default | JMD 50,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 |
| LOW absolute net GCT position | JMD 1,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: NCB, Scotiabank Jamaica, JMMB, Sagicor Bank, First Global Bank, CIBC FirstCaribbean, or any other.

**Recommended** — tax invoices, customs entries (C78), withholding certificates.

**Ideal** — complete sales and purchase records, prior GCT-R, credit balance reconciliation.

### Refusal catalogue

**R-JM-1 — Below registration threshold.** *Trigger:* turnover below JMD 15,000,000 and not voluntarily registered. *Message:* "Below mandatory GCT registration threshold."

**R-JM-2 — Free-zone entity.** *Trigger:* client operates in a Special Economic Zone. *Message:* "Free-zone benefits require valid licence. Escalate."

**R-JM-3 — Approved farmer/manufacturer.** *Trigger:* client claims approved status. *Message:* "Confirm TAJ approved status before applying GCT relief."

**R-JM-4 — Partial exemption.** *Trigger:* mixed taxable/exempt. *Message:* "Apportionment required. Flag for reviewer."

**R-JM-5 — Tourism sector concessions.** *Trigger:* hotel/tourism operator claiming special treatment. *Message:* "Tourism sector has multiple overlapping levies. Flag for reviewer."

---

## Section 3 — Supplier pattern library

### 3.1 Banks (fees taxable, interest exempt)
| Pattern | Treatment | Notes |
|---|---|---|
| NCB, NATIONAL COMMERCIAL BANK | 15% for fees; EXCLUDE for interest | |
| SCOTIABANK, JMMB, SAGICOR BANK | Same | |
| FIRST GLOBAL, CIBC FIRSTCARIBBEAN | Same | |

### 3.2 Government (exclude)
| Pattern | Treatment | Notes |
|---|---|---|
| TAJ, TAX ADMINISTRATION JAMAICA | EXCLUDE | Tax payment |
| NIS, NHT, EDUCATION TAX | EXCLUDE | Statutory deductions |
| CUSTOMS, JAMAICA CUSTOMS | EXCLUDE for duty; check GCT on imports |

### 3.3 Utilities
| Pattern | Treatment | Notes |
|---|---|---|
| JPS, JAMAICA PUBLIC SERVICE | Domestic 15% (commercial) | Electricity |
| NWC, NATIONAL WATER COMMISSION | Exempt (domestic threshold) or 15% | Check threshold |
| FLOW, DIGICEL | 25% (telephone) or 15% (internet) | Telephone at 25%; internet at 15% |

### 3.4 Insurance
| Pattern | Treatment | Notes |
|---|---|---|
| SAGICOR LIFE, GUARDIAN LIFE | EXCLUDE | Life insurance exempt |
| GENERAL INSURANCE, ADVANTAGE GENERAL | Domestic 15% | General insurance taxable |

### 3.5 SaaS non-resident (reverse charge)
| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Reverse charge 15% | Self-assess output/input |
| ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI | Reverse charge 15% | Same |

### 3.6 Food and entertainment (blocked)
| Pattern | Treatment | Notes |
|---|---|---|
| HI-LO, LOSHUSAN, MEGAMART, PRICESMART | Default BLOCK | Personal provisioning |
| RESTAURANT | Default BLOCK | Entertainment |

### 3.7 Fuel
| Pattern | Treatment | Notes |
|---|---|---|
| PETCOM, SHELL, TOTAL | No GCT (subject to SCT) | Petroleum |

### 3.8 Internal transfers
| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL | EXCLUDE | |
| SALARY, WAGES, PAYE | EXCLUDE | |

---

## Section 4 — Worked examples

### Example 1 — Non-resident reverse charge (CARICOM consulting)
**Input:** `TRINIDAD CONSULTING LTD ; DEBIT ; JMD 310,000`
**Treatment:** Reverse charge 15%. Output = JMD 46,500. Input = JMD 46,500. Net zero.

### Example 2 — Standard domestic sale
**Input:** `ABC JAMAICA LTD ; CREDIT ; JMD 575,000`
**Treatment:** Net = 500,000. GCT = 75,000. Line 1/2.

### Example 3 — Entertainment, blocked
**Input:** `RESTAURANT CHEZ MARIE ; DEBIT ; JMD 23,000`
**Treatment:** GCT of JMD 3,000 blocked. No input credit.

### Example 4 — Export
**Input:** `US BUYER INC ; CREDIT ; JMD 500,000`
**Treatment:** Line 3. Zero-rated. Full input credit.

### Example 5 — Motor car, blocked
**Input:** `AUTOMOTORS JA LTD ; DEBIT ; sedan ; JMD 5,000,000`
**Treatment:** GCT JMD 750,000 blocked. No input credit.

### Example 6 — Telephone service at 25%
**Input:** `DIGICEL ; DEBIT ; phone service ; JMD 12,500`
**Treatment:** Net = 10,000. GCT = 2,500 at 25%. Input credit allowed if business line.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15%
Default for all taxable supplies. Sales Line 1/2. Purchases Line 8.

### 5.2 Telephone rate 25%
Telephone services and handsets. Sales at 25%.

### 5.3 Zero-rated
Exports, international transport, diplomatic supplies, approved agricultural inputs, free-zone supplies.

### 5.4 Exempt (Second Schedule)
Basic food items, medical/dental, education, financial interest, life insurance, residential rental, public transport, domestic water/electricity, petroleum.

### 5.5 Reverse charge (Section 4A)
Services from non-residents. Self-assess 15%.

### 5.6 Blocked input GCT (Section 16(2), 17)
Entertainment, motor cars, club subscriptions, personal use, exempt supply costs.

### 5.7 Customs GCT
GCT paid at customs on imports. Line 6 (output), Line 9 (input).

### 5.8 Withholding GCT (Section 19A)
Designated agents withhold two-thirds of GCT (effectively 10% of GCT-exclusive value).

### 5.9 Tax invoice (Section 20)
Must show: "Tax Invoice", supplier TRN, customer TRN (B2B > JMD 10,000), GCT amount.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Tourism sector
*Default:* flag. *Question:* "Confirm applicable concessions with TAJ."

### 6.2 Approved farmer/manufacturer
*Default:* flag. *Question:* "Confirm TAJ approved status."

### 6.3 Mixed supplies apportionment
*Default:* flag. *Question:* "Confirm taxable/exempt ratio."

### 6.4 Motor vehicle exception
*Default:* blocked. *Question:* "Is this a taxi, rental car, driving school vehicle, or goods transport vehicle?"

### 6.5 Digital services from non-residents
*Default:* flag. *Question:* "Confirm registration obligations for non-resident digital suppliers."

---

## Section 7 — Excel working paper template
Standard layout. Column H accepts GCT-R line numbers.
```
Line 7 = Total output GCT
Line 12 = Net input GCT
Line 13 = 7 - 12
Line 15 = 13 - 14
```

---

## Section 8 — Bank statement reading guide
**Format:** NCB/Scotiabank CSV, DD/MM/YYYY, JMD. **Language:** English.
**Internal transfers:** "Own account transfer". Exclude. **Fuel:** No GCT (SCT instead).

---

## Section 9 — Onboarding fallback

### 9.1 Registration status
*Inference:* if filing GCT-R, registered. *Fallback:* "Are you GCT-registered?"

### 9.2 TRN
*Fallback:* "What is your 9-digit TRN?"

### 9.3 Filing period
*Inference:* from statement. *Fallback:* "Monthly or bi-monthly? Which period?"

### 9.4 Credit brought forward
Always ask: "Excess credit from prior period? (Line 14)"

---

## Section 10 — Reference material

### Sources
1. General Consumption Tax Act, 1991 (as amended) — Sections 2-4A, 8, 16-21, 25, 28, 30, 31
2. GCT Regulations; First Schedule (zero-rated); Second Schedule (exempt)
3. Special Economic Zones Act, 2016

### Change log
- **v2.0 (April 2026):** Full rewrite to 10-section architecture.
- **v1.1/v1.0:** Initial skill.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
