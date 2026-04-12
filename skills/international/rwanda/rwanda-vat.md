---
name: rwanda-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Rwanda VAT return. Standard rate 18%. Mandatory EBM (Electronic Billing Machine). No EBM = no input recovery. EAC member. ALWAYS read before handling Rwanda VAT work.
version: 2.0
---

# Rwanda VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Rwanda |
| Standard rate | 18% |
| Zero rate | 0% (exports, diplomatic, SEZ) |
| Filing portal | https://efiling.rra.gov.rw |
| Authority | Rwanda Revenue Authority (RRA) |
| Currency | RWF |
| Filing frequency | Monthly (standard); Quarterly (< RWF 200M turnover) |
| Deadline | 15th of following month |
| Registration | RWF 20,000,000 annual turnover |
| EBM | MANDATORY -- no EBM receipt = no input recovery |
| Primary legislation | Law 049/2023 as amended by Law 009/2025 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Key 2025 changes (Law 009/2025):** Mobile phones, ICT equipment, fuel, fee-based financial services, local road transport now taxable from July 2025.

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from BK (Bank of Kigali), I&M Bank Rwanda, Equity Bank RW, BPR, Access Bank RW, or any Rwandan bank.

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| BK, BANK OF KIGALI | EXCLUDE | Exempt financial |
| I&M RWANDA, I&M BANK RW | EXCLUDE | Same |
| EQUITY BANK RW, BPR | EXCLUDE | Same |
| RRA, RWANDA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| RSSB | EXCLUDE | Social security |
| REG, EUCL | Domestic 18% | Electricity |
| WASAC | Domestic 18% | Water |
| MTN RW, AIRTEL RW | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Purchase without EBM

VAT-registered supplier provides services but issues handwritten invoice without EBM. Input VAT NOT recoverable regardless of supplier's registration status.

### Example 2 -- Export of tea

Exporter ships tea to Mombasa. Zero-rated. Input VAT fully recoverable. Must have export documentation.

---

## Section 5 -- Classification rules

18% standard. 0% exports, diplomatic, SEZ. Exempt: unprocessed agricultural, financial (margin-based; fee-based now taxable from July 2025), medical, education, residential rental, public transport (road transport of goods now taxable from July 2025), books/newspapers, water/electricity (domestic), funeral.

EBM: mandatory for all VAT-registered. No EBM = no input claim.

---

## Section 6 -- VAT return form

Output: A1-A7 (standard, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: B1-B9 (local with EBM, imports, imported services, input local, input imports, input imported services, total input, adjustments, allowable input).

Net: C1-C3 (net, credit b/f, net payable).

---

## Section 7 -- Reverse charge

Non-resident services: self-assess 18%. Net zero. Law 049/2023 Art. 13.

EAC: no intra-community mechanism.

---

## Section 8 -- Deductibility and blocked input

Blocked (Art. 17): entertainment, vehicles < 10 seats (unless taxi/hire), clubs, personal use, purchases without EBM receipt.

Partial exemption: Art. 16(3). RRA approval.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly 15th (quarterly for small). Late filing: 20% + RWF 100K minimum. Late payment: 1.5%/month. Non-EBM: 100% of unreported tax.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 18%. Net zero.
**EC2 -- Non-EBM invoice.** Input NOT recoverable.
**EC3 -- Tea export.** Zero-rated.
**EC4 -- EAC import (Kenya).** VAT at customs. Recoverable.
**EC5 -- Motor vehicle blocked.**
**EC6 -- SEZ supply.** May be zero-rated. Verify certificate.
**EC7 -- Credit note.** Adjust A6.
**EC8 -- Deemed supply cessation.** 18% on market value.

**Test 1** -- RWF 5M sale. Output 900K.
**Test 2** -- EBM receipt RWF 1M + 180K VAT. Recoverable.
**Test 3** -- Handwritten receipt RWF 500K + 90K VAT. Input = 0.
**Test 4** -- Indian IT RWF 3M. Output 540K, input 540K.
**Test 5** -- Mineral export RWF 50M. Zero-rated.
**Test 6** -- Entertainment. Blocked.
**Test 7** -- Hospital services RWF 10M. Exempt. Input not recoverable.
**Test 8** -- Tanzania import RWF 8M. Customs VAT 1.44M. Recoverable.

Out of scope: CIT 30%, PAYE 0%-30%, RSSB 5%+3% pension, 0.3% maternity.

### Prohibitions

- NEVER allow input recovery without EBM receipt
- NEVER treat EAC as intra-community
- NEVER accept non-EBM invoices
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
