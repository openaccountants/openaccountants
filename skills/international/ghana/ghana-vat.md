---
name: ghana-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Ghana VAT return. VAT 15% + NHIL 2.5% + GETFund 2.5% = 20% effective. Act 1151 effective 1 Jan 2026 recouples levies. Flat rate scheme abolished. Withholding VAT at 7%. ALWAYS read before handling Ghana VAT work.
version: 2.0
---

# Ghana VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Ghana |
| VAT | 15% |
| NHIL | 2.5% |
| GETFund | 2.5% |
| Effective total | 20% |
| COVID-19 HRL | ABOLISHED |
| Flat Rate Scheme | ABOLISHED (Act 1151) |
| Zero rate | 0% (exports, Free Zones supplies) |
| Filing portal | https://taxpayersportal.ghana.gov.gh |
| Authority | Ghana Revenue Authority (GRA) |
| Currency | GHS (Ghana Cedi) |
| Filing frequency | Monthly |
| Deadline | Last working day of following month |
| Registration | GHS 750,000 (goods); all service providers regardless |
| Withholding VAT | 7% of VAT amount |
| Primary legislation | VAT Act 2025 (Act 1151) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

**Key change under Act 1151:** NHIL and GETFund recoupled -- now recoverable as input. COVID HRL abolished. Flat rate abolished.

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from GCB (Ghana Commercial Bank), Ecobank Ghana, Stanbic GH, Standard Chartered GH, Fidelity Bank GH, or any Ghanaian bank.

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| GCB, GHANA COMMERCIAL BANK | EXCLUDE | Exempt financial |
| ECOBANK GH, ECOBANK GHANA | EXCLUDE | Same |
| STANBIC GH, STANDARD CHARTERED GH | EXCLUDE | Same |
| FIDELITY BANK GH | EXCLUDE | Same |
| GRA, GHANA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| SSNIT | EXCLUDE | Social security |
| ECG, VRA | Domestic 20% | Electricity |
| GHANA WATER | Domestic 20% | Water |
| MTN GH, VODAFONE GH, AIRTEL-TIGO | Domestic 20% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 20% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale with levies

GHS 10,000 net. VAT GHS 1,500 + NHIL GHS 250 + GETFund GHS 250 = total GHS 2,000 (20%).

### Example 2 -- Withholding VAT

Government ministry pays supplier. Invoice GHS 20K + VAT 3K + NHIL 500 + GETFund 500 = GHS 24K. Withholding = 7% of GHS 3K = GHS 210. Supplier receives GHS 23,790. Claims GHS 210 credit (Box 20).

---

## Section 5 -- Classification rules

15% VAT + 2.5% NHIL + 2.5% GETFund on same base. Under Act 1151, all three recoverable as input. 0% exports, Free Zones. Exempt: financial (margin-based), residential rental, medical, education, unprocessed foodstuffs, agricultural inputs, petroleum (separate levies).

---

## Section 6 -- VAT return form

Output: Boxes 1-8 (standard, zero-rated, exempt, total, output VAT, NHIL, GETFund, total output).

Input: Boxes 10-15 (local purchases, imports, total input VAT 15%, capital goods, overheads, resale).

Net: Boxes 16-21 (net VAT, net NHIL, net GETFund, credit b/f, withholding credits, net payable).

---

## Section 7 -- Reverse charge and withholding VAT

Reverse charge: non-resident services. Self-assess VAT 15% + NHIL 2.5% + GETFund 2.5%. Under Act 1151, all recoverable. Net zero.

Withholding VAT: designated agents withhold 7% of VAT amount (NOT total invoice). Agent only withholds on VAT, NOT NHIL/GETFund. Supplier claims credit Box 20.

---

## Section 8 -- Deductibility and blocked input

Blocked (s.42): entertainment, motor vehicles (unless exclusively for transport for reward), club subscriptions, personal use.

Under Act 1151: NHIL and GETFund on inputs ARE recoverable.

Partial exemption: s.41(5). GRA approval required.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly. Last working day of following month. Withholding remittance: 15th. Late filing: GHS 500/month. Late payment: 125% of BoG rate monthly.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge all three components. Net zero under Act 1151.
**EC2 -- Former flat rate business.** Now standard 15% + levies.
**EC3 -- Withholding VAT.** 7% of VAT only, not NHIL/GETFund.
**EC4 -- Cocoa export.** Zero-rated. All input recoverable. Refund after 3 months.
**EC5 -- Free Zone supply.** Zero-rated with valid permit.
**EC6 -- Bad debt.** 12 months + write-off + recovery efforts.
**EC7 -- Motor vehicle.** Blocked unless transport for reward.

**Test 1** -- GHS 10K sale. VAT 1.5K, NHIL 250, GETFund 250. Total 2K.
**Test 2** -- Local purchase GHS 2K + VAT 300 + NHIL 50 + GETFund 50. All recoverable under Act 1151.
**Test 3** -- UK services GHS 5K. Self-assess 750+125+125. Claim all. Net zero.
**Test 4** -- Export GHS 50K. Zero-rated.
**Test 5** -- Flat rate transition. Now standard regime.
**Test 6** -- Govt pays GHS 20K + VAT 3K. Withholding 7% of 3K = 210.
**Test 7** -- Entertainment. All blocked.

Out of scope: CIT 25%, PAYE progressive, SSNIT 13.5%+5.5%, CST 9%.

### Prohibitions

- NEVER apply flat rate scheme -- abolished under Act 1151
- NEVER ignore withholding VAT credits
- NEVER withhold on NHIL/GETFund -- only on VAT component
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
