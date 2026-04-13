---
name: mauritius-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mauritius VAT return. Standard rate 15%. Tourist refund scheme. Freeport treatment. GBL interactions. ALWAYS read before handling Mauritius VAT work.
version: 2.0
---

# Mauritius VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Mauritius |
| Standard rate | 15% |
| Zero rate | 0% (exports, basic foodstuffs, domestic electricity first 75 kWh, freeport supplies) |
| Filing portal | https://www.mra.mu |
| Authority | Mauritius Revenue Authority (MRA) |
| Currency | MUR |
| Filing frequency | Quarterly (standard); Monthly (large taxpayers) |
| Deadline | Last day of month following quarter (quarterly); 20th (monthly) |
| Registration | MUR 6,000,000 annual turnover |
| Tourist refund | MUR 2,300 minimum per invoice |
| Primary legislation | VAT Act 1998 (Act No. 2 of 1998) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from MCB (Mauritius Commercial Bank), SBM (State Bank of Mauritius), Absa Mauritius, AfrAsia Bank, Bank One, or any Mauritian bank.

**R-MU-1 -- GBL company.** Trigger: Global Business Licence. Message: "GBL companies have specific VAT treatment. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| MCB, MAURITIUS COMMERCIAL BANK | EXCLUDE | Exempt financial |
| SBM, STATE BANK OF MAURITIUS | EXCLUDE | Same |
| ABSA MU, AFRASIA | EXCLUDE | Same |
| BANK ONE | EXCLUDE | Same |
| MRA, MAURITIUS REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| NPF, NSF, CSG | EXCLUDE | Social contributions |
| CEB | Domestic 15% | Electricity |
| CWA | Domestic 15% | Water |
| MAURITIUS TELECOM, EMTEL, MTML | Domestic 15% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 15% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

MUR 1,000,000 net. Output VAT = MUR 150,000 (15%).

### Example 2 -- Tourist refund

Tourist purchases goods MUR 5,000. Issues Tax-Free Shopping receipt. Tourist claims refund at airport.

---

## Section 5 -- Classification rules

15% standard. 0% exports, basic foodstuffs (rice, flour, bread, cooking gas), domestic electricity (first 75 kWh), freeport supplies. Exempt: financial, medical, education, residential rental, public transport, postal, residential property sales (subsequent).

Tourist refund: minimum MUR 2,300 per invoice. Claimed at airport.

---

## Section 6 -- VAT return form

Output: Boxes 1-7 (standard, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: Boxes 8-14 (local purchases, imports, input local, input imports, capital goods, adjustments, net input).

Net: Boxes 15-17 (net, credit b/f, net payable).

---

## Section 7 -- Reverse charge

Non-resident services: self-assess 15%. Net zero. VAT Act s.7A.

---

## Section 8 -- Deductibility and blocked input

Blocked (s.21): vehicles < 9 seats (unless taxi/hire/driving instruction/dealer), entertainment, clubs, personal use, invoices without VAT number.

Partial exemption: s.20. MRA may approve alternative methods.

---

## Section 9 -- Filing, deadlines, and penalties

Quarterly: last day of month following quarter. Monthly (large): 20th. Late filing: MUR 5,000/month. Late payment: 2%/month.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 15%. Net zero.
**EC2 -- IT export.** Zero-rated. Input recoverable.
**EC3 -- Motor vehicle blocked.**
**EC4 -- Freeport supply.** Zero-rated with certificate. Verify.
**EC5 -- GBL company.** Escalate.
**EC6 -- Basic foodstuffs.** Rice/flour zero-rated.
**EC7 -- Bad debt.** 6+ months, written off.
**EC8 -- Residential first sale.** Standard-rated by developer. Subsequent exempt.

**Test 1** -- MUR 1M sale. Output 150K.
**Test 2** -- MUR 500K purchase + 75K VAT. Recoverable.
**Test 3** -- UK consulting MUR 2M. Output 300K, input 300K.
**Test 4** -- Textiles export MUR 10M. Zero-rated.
**Test 5** -- Entertainment. Blocked.
**Test 6** -- Bank interest MUR 50M. Exempt. Input not recoverable.

Out of scope: CIT 15%, PAYE progressive, NPF/NSF, CSG 3%+1.5%/3%.

### Prohibitions

- NEVER confuse tourist refund with standard refund
- NEVER allow recovery on blocked categories
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
