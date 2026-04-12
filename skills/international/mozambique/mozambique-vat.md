---
name: mozambique-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mozambique VAT (IVA) return. Standard rate 16%, reduced 5%. ISPC simplified regime for small taxpayers. Portuguese-language terminology. ALWAYS read before handling Mozambique IVA work.
version: 2.0
---

# Mozambique VAT (IVA) Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Mozambique |
| Standard rate | 16% |
| Reduced rate | 5% (private health, education, vocational training) |
| Zero rate | 0% (exports) |
| ISPC (simplified) | 3% of turnover (below MZN 2,500,000) |
| Filing portal | https://efatura.at.gov.mz |
| Authority | Autoridade Tributaria de Mocambique (AT) |
| Currency | MZN (Metical) |
| Filing frequency | Monthly (large) or Quarterly (standard) |
| Deadline | Last working day of following month/quarter |
| Registration threshold | MZN 2,500,000 |
| Primary legislation | CIVA, Law 32/2007 as amended |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from BCI (Banco Comercial e de Investimentos), Millennium bim, Standard Bank MZ, BCI Fomento, Absa MZ, or any Mozambican bank.

**R-MZ-1 -- Megaproject.** Trigger: LNG, Sasol, mining concessions. Message: "Megaproject fiscal regimes are negotiated individually. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| BCI, BANCO COMERCIAL | EXCLUDE | Exempt financial |
| MILLENNIUM BIM | EXCLUDE | Same |
| STANDARD BANK MZ | EXCLUDE | Same |
| AT, AUTORIDADE TRIBUTARIA | EXCLUDE | Tax payment |
| ALFANDEGAS, CUSTOMS | Check for import IVA | |
| INSS | EXCLUDE | Social security |
| EDM, ELECTRICIDADE | Domestic 16% | Electricity |
| FIPAG | Domestic 16% | Water |
| VODACOM MZ, TMCEL, MOVITEL | Domestic 16% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidacao 16% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

MZN 1,000,000 net. IVA = MZN 160,000 (16%).

### Example 2 -- ISPC taxpayer

Small retailer under ISPC. Quarterly sales MZN 400,000. ISPC = 3% = MZN 12,000. No input recovery.

---

## Section 5 -- Classification rules

16% standard. 5% reduced (private health/education). 0% exports. Exempt: basic foodstuffs, financial, medical (public), education (public), residential rental, public transport, agricultural inputs.

ISPC: 3% of gross turnover for businesses below MZN 2,500,000. No IVA charged, no input recovery.

---

## Section 6 -- IVA return form

Output: Lines 1-8 (16% sales, exempt, exports, total, IVA liquidado, autoliquidacao, adjustments, total).

Input: Lines 9-14 (local, imports, autoliquidacao input, capital goods, exclusions, total deductible).

Net: Lines 15-17 (net, credit transitado, payable/credit).

---

## Section 7 -- Reverse charge (autoliquidacao)

Non-resident services: self-assess 16%. Net zero. CIVA Art. 23.

---

## Section 8 -- Deductibility and blocked input

Blocked (CIVA Art. 20-22): vehicles < 9 seats, entertainment, personal use, fuel for blocked vehicles, invoices without NUIT.

Prorata: CIVA Art. 19.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly or quarterly. Last working day of following month. Late filing: MZN 5K-50K. Late payment: 2%/month.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Autoliquidacao 16%. Net zero.
**EC2 -- Prawn export.** Zero-rated. Input recoverable.
**EC3 -- Motor vehicle blocked.**
**EC4 -- ISPC boundary.** Exceeds MZN 2.5M: must register for IVA.
**EC5 -- Megaproject (LNG).** Escalate.
**EC6 -- Basic foodstuffs exempt.** Rice/bread exempt. No output, no input recovery.

**Test 1** -- MZN 1M sale. IVA MZN 160K.
**Test 2** -- MZN 500K purchase + IVA 80K. Recoverable.
**Test 3** -- SA services MZN 3M. Output 480K, input 480K. Net zero.
**Test 4** -- Export MZN 50M. Zero-rated.
**Test 5** -- Entertainment. Blocked.
**Test 6** -- ISPC quarterly MZN 400K. ISPC = MZN 12K.

Out of scope: IRPC 32%, IRPS progressive 10%-32%, INSS employer 4% + employee 3%.

### Prohibitions

- NEVER confuse IVA with ISPC
- NEVER allow ISPC taxpayers to charge IVA
- NEVER apply standard rules to megaprojects without verification
- NEVER accept invoices without NUIT
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
