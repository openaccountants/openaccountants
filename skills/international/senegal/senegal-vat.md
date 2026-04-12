---
name: senegal-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Senegal VAT (TVA) return. Standard rate 18%, reduced 10% (tourism). WAEMU member. Precompte TVA mechanism. ALWAYS read before handling Senegal VAT work.
version: 2.0
---

# Senegal VAT (TVA) Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Senegal |
| Standard rate | 18% |
| Reduced rate | 10% (tourism accommodation/catering) |
| Zero rate | 0% (exports) |
| Filing portal | https://eservices.dgid.sn |
| Authority | DGID (Direction Generale des Impots et des Domaines) |
| Currency | FCFA (XOF) |
| Filing frequency | Monthly (reel normal); Quarterly (simplifie) |
| Deadline | 15th of following month |
| Registration | FCFA 100M goods / 50M services |
| Primary legislation | CGI, Livre II -- TVA |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CBAO, SGBS (Societe Generale Banques au Senegal), Ecobank SN, BOA SN, BIS, BNDE, or any Senegalese bank.

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| CBAO | EXCLUDE | Exempt financial |
| SGBS, SOCIETE GENERALE SN | EXCLUDE | Same |
| ECOBANK SN, BOA SN | EXCLUDE | Same |
| DGID | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA | |
| CSS, IPRES | EXCLUDE | Social charges |
| SENELEC | Domestic 18% | Electricity |
| SDE, SEN'EAU | Domestic 18% | Water |
| ORANGE SN, FREE SN, EXPRESSO | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 18% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

FCFA 10M net. TVA = FCFA 1.8M (18%).

### Example 2 -- Precompte TVA

Government entity pays supplier. Precompte withheld. Supplier claims credit on Line III.3.

---

## Section 5 -- Classification rules

18% standard. 10% reduced (tourism). 0% exports. Exempt: basic foodstuffs, financial, medical, education, residential rental, agricultural inputs, petroleum (specific taxes).

---

## Section 6 -- VAT return form

Output: I.1-I.8 (18% sales, exempt, exports, total, TVA collectee, autoliquidation, adjustments, total brute).

Input: II.1-II.6 (local, imports, autoliquidation input, capital goods, adjustments, total deductible).

Net: III.1-III.4 (net, credit reporte, precompte, payable/credit).

---

## Section 7 -- Reverse charge

Non-resident services: self-assess 18%. Net zero if fully taxable. CGI Art. 364.

---

## Section 8 -- Deductibility and blocked input

Blocked (CGI Art. 376-379): vehicles < 9 seats, staff accommodation, entertainment, fuel for blocked vehicles, personal use, invoices without NINEA.

Prorata: CGI Art. 375. Capital goods: 20yr immovable, 5yr movable.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly 15th. Quarterly for simplifie. Late filing: 50% surcharge (min FCFA 200K). Late payment: 1%/month.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Autoliquidation 18%. Net zero.
**EC2 -- Groundnut export.** Zero-rated. Input recoverable.
**EC3 -- Motor vehicle blocked.**
**EC4 -- WAEMU import (CI).** VAT 18% at Senegalese customs.
**EC5 -- Precompte.** Government withholds. Supplier claims credit.
**EC6 -- Capital goods adjustment.** 20yr immovable.

**Test 1** -- FCFA 10M sale. TVA FCFA 1.8M.
**Test 2** -- Equipment FCFA 5M + TVA 900K. Recoverable.
**Test 3** -- French consulting FCFA 8M. Output 1.44M, input 1.44M. Net zero.
**Test 4** -- Fish export FCFA 50M. Zero-rated.
**Test 5** -- Entertainment. Blocked.

Out of scope: IS 30%, PAYE progressive, IPRES/CSS.

### Prohibitions

- NEVER confuse zero-rated with exempt
- NEVER treat WAEMU as intra-community
- NEVER accept invoices without NINEA
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
