---
name: jordan-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Jordan General Sales Tax (GST) return for any client. Trigger on phrases like "Jordan GST", "Jordan VAT", "ISTD return", or any request involving Jordanian indirect tax. Jordan imposes GST at 16% under Law No. 6 of 1994, administered by ISTD. Multiple special rates exist (4%, 5%, 8%, 10%). ALWAYS read this skill before handling any Jordan GST work.
version: 2.0
---

# Jordan GST Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Jordan (Hashemite Kingdom) |
| Standard rate | 16% |
| Special rates | 4% (telecoms), 5% (certain services), 8% (certain goods), 10% (certain goods/services) |
| Zero rate | 0% (exports, specified basic foodstuffs) |
| Exempt supplies | Financial services, medical, education, residential rental, unprocessed agricultural |
| Filing portal | https://www.istd.gov.jo |
| Authority | Income and Sales Tax Department (ISTD) |
| Currency | JOD (Jordanian Dinar) |
| Filing frequency | Monthly (turnover > JOD 1M); Bi-monthly (others) |
| Deadline | End of month following period |
| Mandatory registration | JOD 75,000 (goods), JOD 30,000 (services) |
| Primary legislation | General Sales Tax Law No. 6 of 1994 (as amended) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 16% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Jordan |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the period. Acceptable from Arab Bank, Housing Bank, Jordan Ahli Bank, Cairo Amman, Bank al Etihad, or any other Jordanian bank.

**Recommended** -- sales invoices (Arabic required), purchase invoices for input claims.

### Refusal catalogue

**R-JO-1 -- Free zone complex.** Trigger: Aqaba Special Economic Zone operations. Message: "ASEZA has specific GST rules. Escalate to licensed practitioner."

**R-JO-2 -- Special Sales Tax.** Trigger: alcohol, tobacco, fuel subject to SST. Message: "SST is separate from GST and computed first. Escalate for combined computation."

---

## Section 3 -- Supplier pattern library

### 3.1 Jordanian banks (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ARAB BANK | EXCLUDE | Financial service, exempt |
| HOUSING BANK, ISKAN BANK | EXCLUDE | Same |
| JORDAN AHLI, CAIRO AMMAN | EXCLUDE | Same |
| BANK AL ETIHAD, CAPITAL BANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| ISTD, INCOME AND SALES TAX | EXCLUDE | Tax payment |
| CUSTOMS, JORDAN CUSTOMS | Check for import GST | Duty exclude; GST recoverable |
| SSC, SOCIAL SECURITY CORPORATION | EXCLUDE | Social contribution |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| JEPCO, EDCO, IDECO | Domestic 16% | Electricity |
| MIYAHUNA, WAJ | Domestic 16% | Water |
| ZAIN JORDAN, ORANGE JORDAN, UMNIAH | Domestic 4% | Telecoms at special rate |

### 3.4 SaaS

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE | Reverse charge 16% | Non-resident service |
| AWS, ZOOM, SLACK | Reverse charge 16% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Reverse charge on US SaaS

**Input:** `05.01.2026 ; SALESFORCE INC ; DEBIT ; Monthly CRM ; USD 200 ; JOD 142`

US entity. No GST. Reverse charge at 16%. Output and input both reported. Net zero.

### Example 2 -- Telecoms at 4%

**Input:** `10.01.2026 ; ZAIN JORDAN ; DEBIT ; Mobile plan ; -50.00 ; JOD`

Telecoms services at special 4% rate, not 16%.

---

## Section 5 -- Classification rules

### 5.1 Standard rate 16%

Default for all taxable supplies unless specifically listed at another rate.

### 5.2 Special rates

4% telecoms (domestic), 5% certain services, 8% certain goods, 10% certain goods/services. Rate determined by ISTD schedules.

### 5.3 Zero-rated (0%, input recoverable)

Exports, international transport, basic foodstuffs (bread, rice, sugar, milk per Cabinet decision), goods to free zones (conditions).

### 5.4 Exempt (no GST, no recovery)

Financial services, medical, education, residential rental (unfurnished), unprocessed agricultural, government-to-government, charitable (conditions).

---

## Section 6 -- GST return form structure

### Output section

| Section | Description |
|---|---|
| Output GST at 16% | Standard-rated supplies |
| Output GST at special rates | 4%, 5%, 8%, 10% separately |
| Zero-rated | Exports and zero-rated supplies |
| Exempt | Exempt supplies |

### Input section

| Section | Description |
|---|---|
| Input GST on domestic purchases | Recoverable if taxable |
| Input GST on imports | Customs GST |
| Input GST adjustments | Blocked, apportionment |

### Net

Output GST minus allowable input GST. Credit brought forward from prior period.

---

## Section 7 -- Reverse charge and imports

Services from non-resident: self-assess at 16%. Claim input if for taxable supplies. Net zero.

Import of goods: GST on CIF plus customs duties. Collected by Jordan Customs. Recoverable if for taxable supplies.

Legislation: GST Law No. 6/1994, reverse charge provisions.

---

## Section 8 -- Deductibility and blocked input

Blocked:
- Entertainment and hospitality
- Motor vehicles for personal use
- Non-business goods/services
- Purchases related to exempt supplies
- Gifts/donations (above limits)

Partial exemption: turnover-based apportionment. ISTD approval required.

---

## Section 9 -- Filing, deadlines, and penalties

| Category | Period | Deadline |
|---|---|---|
| Large taxpayers (> JOD 1M) | Monthly | End of following month |
| Others | Bi-monthly | End of month following bi-monthly period |

Bi-monthly periods: Jan-Feb (due 31 Mar), Mar-Apr (31 May), May-Jun (31 Jul), Jul-Aug (30 Sep), Sep-Oct (30 Nov), Nov-Dec (31 Jan).

| Violation | Penalty |
|---|---|
| Late filing | JOD 100-500 per return |
| Late payment | 4% first week; 1% per week after |
| Tax evasion | Fines and imprisonment |

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- Foreign SaaS.** Reverse charge at 16%. Net zero.

**EC2 -- Export of goods.** Zero-rated. Input recoverable.

**EC3 -- Telecom at 4%.** Not 16%.

**EC4 -- Free zone to domestic.** GST applies when goods leave free zone.

**EC5 -- Credit note.** Reduces output GST in period issued.

**EC6 -- Exempt financial services.** No output GST. Input not recoverable.

**EC7 -- Import of goods.** GST on CIF + duty. Recoverable.

### Test suite

**Test 1 -- Standard sale.** JOD 1,000 net. Expected: output GST JOD 160 (16%).

**Test 2 -- Export.** JOD 5,000 goods. Expected: 0% GST. Input recoverable.

**Test 3 -- Reverse charge.** UK consulting JOD 1,420. Expected: output JOD 227.20, input JOD 227.20.

**Test 4 -- Telecoms.** JOD 50,000 services. Expected: GST JOD 2,000 (4%).

**Test 5 -- Exempt supply.** Bank financial services JOD 100,000. Expected: no output GST. Input JOD 3,200 not recoverable.

**Test 6 -- Import.** Electronics CIF JOD 10,000 + duty JOD 1,000. Expected: GST base JOD 11,000, GST JOD 1,760.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate income tax: 20% standard; banks 35%; telecoms 24%; mining 30%
- Personal income tax: progressive 5%-30%
- Social security: employer 14.25%, employee 7.5%

### Prohibitions

- NEVER apply a rate other than 0%, 4%, 5%, 8%, 10%, 16%
- NEVER allow input recovery on exempt supplies
- NEVER ignore reverse charge on non-resident services
- NEVER treat imports as zero-rated
- NEVER issue invoices without Arabic text
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without confirming correct period (monthly vs bi-monthly)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
