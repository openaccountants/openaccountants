---
name: lebanon-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Lebanon VAT return. Trigger on phrases like "Lebanon VAT", "TVA Lebanon", "MOF Lebanon". Lebanon imposes VAT at 11% under Law 379/2001 (12% Cabinet-approved Feb 2026, pending Parliament). WARNING -- ongoing economic crisis affects enforcement and exchange rates. ALWAYS read this skill before handling any Lebanon VAT work.
version: 2.0
jurisdiction: LB
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lebanon VAT

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
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

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Bank Audi, Blom Bank, Byblos Bank, BankMed, Fransabank, or any Lebanese bank.

- **R-LB-1 -- Exchange rate determination** — Trigger: foreign currency transactions without confirmed MOF rate guidance. Message: "Multiple exchange rates exist. MOF guidance on applicable rate must be confirmed by practitioner before VAT calculations."  _(R-LB-1)_
- **R-LB-2 -- Crisis-era enforcement** — Trigger: questions about current MOF operational status. Message: "Verify current MOF enforcement position with local practitioner."  _(R-LB-2)_

## Section 3 -- Supplier pattern library

### 3.1 Lebanese banks (exempt -- exclude)

**Lebanese banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BANK AUDI, AUDI | EXCLUDE | Exempt financial service |
| BLOM BANK, BLOM | EXCLUDE | Same |
| BYBLOS BANK | EXCLUDE | Same |
| BANKMED, FRANSABANK | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS, DOUANE | Check for import VAT | VAT recoverable |
| NSSF, CNSS | EXCLUDE | Social security |

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EDL, ELECTRICITE DU LIBAN | Domestic 11% | Electricity |
| OGERO, ALFA, TOUCH | Domestic 11% | Telecoms |

### 3.4 SaaS

**SaaS pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, AWS | Reverse charge 11% | Non-resident; exchange rate critical |
| ZOOM, SLACK, NOTION | Reverse charge 11% | Same |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

Company sells goods LBP 10,000,000 net. Output VAT = LBP 1,100,000 (11%). Total = LBP 11,100,000.

### Example 2 -- Foreign currency reverse charge

UK law firm invoices USD 10,000. Reverse charge at 11% on LBP equivalent. Exchange rate: flag for practitioner -- conversion rate is critical during crisis.

## Section 5 -- Classification rules

### 5.1 Standard rate 11%

- **Standard rate** — 11% (Single rate. No reduced rates. If 12% enacted by Parliament, update accordingly.)

### 5.2 Zero-rated

- **Zero-rated supplies** — Exports, international transport, duty-free zone supplies (conditions).

### 5.3 Exempt

- **Exempt supplies** — Financial/banking, insurance, medical, education, residential rental, public transport, unprocessed agricultural, books/newspapers, gold (investment grade).

## Section 6 -- VAT return form structure

**VAT return form structure**

| Section | Description |
| --- | --- |
| A. Output VAT | 11% on domestic taxable supplies |
| B. Zero-rated | Exports |
| C. Exempt | Exempt revenue |
| D. Total supplies | A+B+C |
| E. Input VAT domestic | 11% on local purchases |
| F. Input VAT imports | Customs VAT |
| G. Total input | E+F |
| H. Net VAT | A minus G |
| Credit brought forward | Prior period |

## Section 7 -- Reverse charge and imports

- **Reverse charge on services from non-resident** — Services from non-resident: self-assess at 11%. Claim input if taxable. Net zero. Exchange rate: must confirm with practitioner.
- **Import of goods VAT** — Import of goods: VAT at 11% on CIF plus customs plus excise. Collected by Lebanese Customs.

## Section 8 -- Deductibility and blocked input

- **Blocked input items** — Blocked: entertainment/hospitality, personal-use items, passenger vehicles (unless transport/rental), purchases for exempt supplies, gifts (above thresholds), tobacco/alcohol (personal), club memberships.
- **Partial exemption** — Partial exemption: turnover-based apportionment. Annual adjustment required.

## Section 9 -- Filing, deadlines, and penalties

**Quarterly filing deadlines**

| Quarter | Deadline |
| --- | --- |
| Q1 (Jan-Mar) | 20 April |
| Q2 (Apr-Jun) | 20 July |
| Q3 (Jul-Sep) | 20 October |
| Q4 (Oct-Dec) | 20 January |

**Penalties table**

| Violation | Penalty |
| --- | --- |
| Late filing | LBP 50,000/day (pre-crisis; may be negligible) |
| Late payment | 1.5% per month |
| Failure to register | Backdated assessment + penalties |

Note: penalty amounts may be effectively negligible due to devaluation.

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

Flag for practitioner. Multiple rates exist.

Cash refunds from MOF may not be obtainable. Carry forward.

Zero-rated only with customs declaration, bill of lading, proof of delivery.

Input VAT on purchases for exempt banking not recoverable.

Entertainment blocked for input recovery.

First sale may be taxable. Escalate.

### Test suite

LBP 10M net. Expected: output LBP 1.1M (11%).

USD 5,000 to France. Expected: 0%. Input recoverable.

UK firm USD 10,000. Expected: 11% self-assessed. Exchange rate: flag.

Bank interest LBP 500M. Expected: no output. Input LBP 2.2M not recoverable.

Turkish goods CIF LBP 100M + duty LBP 5M. Expected: VAT base LBP 105M, VAT LBP 11.55M.

Dinner LBP 5M + VAT LBP 550K. Expected: input = 0.

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

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
