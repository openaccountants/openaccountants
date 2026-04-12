---
name: lebanon-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Lebanon VAT return. Trigger on phrases like "Lebanon VAT", "TVA Lebanon", "MOF Lebanon". Lebanon imposes VAT at 11% under Law 379/2001 (12% Cabinet-approved Feb 2026, pending Parliament). WARNING -- ongoing economic crisis affects enforcement and exchange rates. ALWAYS read this skill before handling any Lebanon VAT work.
version: 2.0
---

# Lebanon VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Lebanon |
| Standard rate | 11% (single rate; 12% Cabinet-approved Feb 2026, pending Parliament) |
| Zero rate | 0% (exports, international transport) |
| Exempt | Financial/banking, insurance, medical, education, residential rental, public transport, unprocessed agricultural, books |
| Filing portal | https://www.finance.gov.lb |
| Authority | Ministry of Finance (MOF) |
| Currency | LBP (Lebanese Pound) |
| Filing frequency | Quarterly |
| Deadline | 20th of month following quarter end |
| Registration threshold | LBP 100,000,000 (effectively negligible due to currency crisis) |
| Primary legislation | Law No. 379 of 2001; Decree 7336/2002 |
| CRITICAL WARNING | Economic crisis since 2019 -- exchange rates, enforcement, refunds all affected |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Bank Audi, Blom Bank, Byblos Bank, BankMed, Fransabank, or any Lebanese bank.

**Refusal catalogue:**

**R-LB-1 -- Exchange rate determination.** Trigger: foreign currency transactions without confirmed MOF rate guidance. Message: "Multiple exchange rates exist. MOF guidance on applicable rate must be confirmed by practitioner before VAT calculations."

**R-LB-2 -- Crisis-era enforcement.** Trigger: questions about current MOF operational status. Message: "Verify current MOF enforcement position with local practitioner."

---

## Section 3 -- Supplier pattern library

### 3.1 Lebanese banks (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANK AUDI, AUDI | EXCLUDE | Exempt financial service |
| BLOM BANK, BLOM | EXCLUDE | Same |
| BYBLOS BANK | EXCLUDE | Same |
| BANKMED, FRANSABANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS, DOUANE | Check for import VAT | VAT recoverable |
| NSSF, CNSS | EXCLUDE | Social security |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EDL, ELECTRICITE DU LIBAN | Domestic 11% | Electricity |
| OGERO, ALFA, TOUCH | Domestic 11% | Telecoms |

### 3.4 SaaS

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, AWS | Reverse charge 11% | Non-resident; exchange rate critical |
| ZOOM, SLACK, NOTION | Reverse charge 11% | Same |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

Company sells goods LBP 10,000,000 net. Output VAT = LBP 1,100,000 (11%). Total = LBP 11,100,000.

### Example 2 -- Foreign currency reverse charge

UK law firm invoices USD 10,000. Reverse charge at 11% on LBP equivalent. Exchange rate: flag for practitioner -- conversion rate is critical during crisis.

---

## Section 5 -- Classification rules

### 5.1 Standard rate 11%

Single rate. No reduced rates. If 12% enacted by Parliament, update accordingly.

### 5.2 Zero-rated

Exports, international transport, duty-free zone supplies (conditions).

### 5.3 Exempt

Financial/banking, insurance, medical, education, residential rental, public transport, unprocessed agricultural, books/newspapers, gold (investment grade).

---

## Section 6 -- VAT return form structure

| Section | Description |
|---|---|
| A. Output VAT | 11% on domestic taxable supplies |
| B. Zero-rated | Exports |
| C. Exempt | Exempt revenue |
| D. Total supplies | A+B+C |
| E. Input VAT domestic | 11% on local purchases |
| F. Input VAT imports | Customs VAT |
| G. Total input | E+F |
| H. Net VAT | A minus G |
| Credit brought forward | Prior period |

---

## Section 7 -- Reverse charge and imports

Services from non-resident: self-assess at 11%. Claim input if taxable. Net zero. Exchange rate: must confirm with practitioner.

Import of goods: VAT at 11% on CIF plus customs plus excise. Collected by Lebanese Customs.

---

## Section 8 -- Deductibility and blocked input

Blocked: entertainment/hospitality, personal-use items, passenger vehicles (unless transport/rental), purchases for exempt supplies, gifts (above thresholds), tobacco/alcohol (personal), club memberships.

Partial exemption: turnover-based apportionment. Annual adjustment required.

---

## Section 9 -- Filing, deadlines, and penalties

| Quarter | Deadline |
|---|---|
| Q1 (Jan-Mar) | 20 April |
| Q2 (Apr-Jun) | 20 July |
| Q3 (Jul-Sep) | 20 October |
| Q4 (Oct-Dec) | 20 January |

| Violation | Penalty |
|---|---|
| Late filing | LBP 50,000/day (pre-crisis; may be negligible) |
| Late payment | 1.5% per month |
| Failure to register | Backdated assessment + penalties |

Note: penalty amounts may be effectively negligible due to devaluation.

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- Foreign currency invoicing.** Flag for practitioner. Multiple rates exist.

**EC2 -- Refund delays.** Cash refunds from MOF may not be obtainable. Carry forward.

**EC3 -- Export proof.** Zero-rated only with customs declaration, bill of lading, proof of delivery.

**EC4 -- Banking services exempt.** Input VAT on purchases for exempt banking not recoverable.

**EC5 -- Restaurant (blocked for buyer).** Entertainment blocked for input recovery.

**EC6 -- Construction/real estate.** First sale may be taxable. Escalate.

### Test suite

**Test 1 -- Standard sale.** LBP 10M net. Expected: output LBP 1.1M (11%).

**Test 2 -- Export.** USD 5,000 to France. Expected: 0%. Input recoverable.

**Test 3 -- Reverse charge.** UK firm USD 10,000. Expected: 11% self-assessed. Exchange rate: flag.

**Test 4 -- Exempt.** Bank interest LBP 500M. Expected: no output. Input LBP 2.2M not recoverable.

**Test 5 -- Import.** Turkish goods CIF LBP 100M + duty LBP 5M. Expected: VAT base LBP 105M, VAT LBP 11.55M.

**Test 6 -- Blocked entertainment.** Dinner LBP 5M + VAT LBP 550K. Expected: input = 0.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format -- include note about economic crisis verification]
```

### Out of scope -- direct tax

- Corporate income tax: 17%
- Personal income tax: progressive 2%-25%
- Social security (NSSF): employer and employee contributions

### Prohibitions

- NEVER apply any rate other than 11% (until 12% enacted)
- NEVER allow input recovery on exempt supplies
- NEVER use exchange rate without practitioner confirmation
- NEVER assume pre-crisis rules apply unchanged
- NEVER assume MOF systems operational without confirming
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
