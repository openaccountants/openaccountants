---
name: tunisia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Tunisia VAT (TVA) return. Three rates -- 19%/13%/7%. Unique suspension regime (not zero-rating). Droit de consommation interaction. Withholding TVA 25%. ALWAYS read before handling Tunisia TVA work.
version: 2.0
---

# Tunisia VAT (TVA) Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Tunisia |
| Standard rate | 19% |
| Intermediate rate | 13% (hotels/tourism, construction materials, legal/accounting) |
| Reduced rate | 7% (basic foodstuffs, pharmaceuticals, agricultural equipment, IT, low-voltage electricity) |
| Suspension regime | Distinct from zero-rating (exporters with attestation) |
| Filing portal | https://www.impots.finances.gov.tn |
| Authority | Direction Generale des Impots (DGI) |
| Currency | TND |
| Filing frequency | Monthly (>= TND 1M) or Quarterly |
| Deadline | 15th paper / 28th electronic of following month |
| Registration | TND 100K goods / 50K services |
| Withholding TVA | 25% of TVA amount |
| Primary legislation | Code de la TVA (as amended) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from BIAT (Banque Internationale Arabe de Tunisie), BNA (Banque Nationale Agricole), Amen Bank, STB, BT, ATB, or any Tunisian bank.

**R-TN-1 -- Offshore company.** Message: "Offshore entities have specific regime. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| BIAT | EXCLUDE | Exempt financial |
| BNA, BANQUE NATIONALE AGRICOLE | EXCLUDE | Same |
| AMEN BANK, STB | EXCLUDE | Same |
| BT, ATB | EXCLUDE | Same |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA | |
| CNSS, CNRPS | EXCLUDE | Social security |
| STEG | Domestic (7% low-voltage / 19% commercial) | Electricity |
| SONEDE | Domestic 7% or 19% | Water |
| TUNISIE TELECOM, OOREDOO TN, ORANGE TN | Domestic 19% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 19% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Hotel at 13%

Hotel room TND 200/night. TVA at 13%. Output TVA = TND 26.

### Example 2 -- Product subject to droit de consommation

Cosmetics CIF TND 100K. DC at 25% = TND 25K. TVA base = TND 125K. TVA at 19% = TND 23,750.

### Example 3 -- Withholding TVA

Ministry pays supplier. Invoice TND 50K + TVA 9.5K. Withholding 25% of 9.5K = TND 2,375. Supplier claims credit Line 24.

---

## Section 5 -- Classification rules

19% standard. 13% intermediate (hotels/tourism, certain construction, legal/accounting). 7% reduced (basic foodstuffs, pharmaceuticals, agricultural equipment, IT, buses for employee transport, low-voltage domestic electricity). 2025 Finance Law: real estate developers tiered (7% <= TND 400K, 19% > TND 400K).

Suspension regime: NOT zero-rating. Exporters (>= 80% export) with attestation de suspension buy without TVA. Supplier must verify attestation.

Exempt: financial, education, medical, bread/cereals.

---

## Section 6 -- TVA return form

Output: Lines 1-13 (19% sales, 13% sales, 7% sales, suspension, exempt, exports, total, TVA 19%, TVA 13%, TVA 7%, autoliquidation, adjustments, total brute).

Input: Lines 14-21 (goods for resale, materials, services, capital goods, imports, autoliquidation input, exclusions, total deductible).

Net: Lines 22-25 (due, credit reporte, retenue a la source, payable/credit).

---

## Section 7 -- Reverse charge and droit de consommation

Reverse charge: non-resident services. Self-assess at applicable rate (usually 19%). Net zero. Code TVA Art. 19.

Droit de consommation: excise on specific goods. TVA is calculated on price INCLUDING DC. DC is part of TVA base.

---

## Section 8 -- Deductibility and blocked input

Blocked (Code TVA Art. 10-12): vehicles < 9 seats, staff accommodation, entertainment/gifts, fuel for blocked vehicles, personal use, invoices without matricule fiscal.

Prorata: includes suspension turnover in numerator. Annual recalculation.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly 15th (paper) / 28th (electronic). Quarterly for small. Late filing: 1%/month (min TND 50). Late payment: 0.75%/month.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Autoliquidation 19%. Net zero.
**EC2 -- Exporter with suspension.** Sales under suspension. Input fully recoverable.
**EC3 -- Hotel 13%.** Not 19%.
**EC4 -- Pharmaceuticals 7%.**
**EC5 -- DC + TVA.** TVA on price INCLUDING DC.
**EC6 -- Withholding TVA.** 25% of TVA. Supplier claims credit.
**EC7 -- Suspension certificate purchase.** Invoice without TVA. Verify attestation.
**EC8 -- Mixed supply prorata.** Include suspension in numerator.

**Test 1** -- TND 100K sale. TVA TND 19K (19%).
**Test 2** -- Hotel TND 50K. TVA TND 6.5K (13%).
**Test 3** -- Pharmacy TND 30K. TVA TND 2.1K (7%).
**Test 4** -- French services TND 20K. Output 3.8K, input 3.8K. Net zero.
**Test 5** -- Export TND 500K. Zero.
**Test 6** -- Vehicle blocked. TND 50K + 9.5K TVA. Input = 0.

Out of scope: IS 15%, PAYE 0%-35%, CNSS/CNRPS.

### Prohibitions

- NEVER confuse suspension with exemption
- NEVER apply wrong rate -- three rates exist
- NEVER forget DC in TVA base
- NEVER issue suspension invoice without verifying attestation
- NEVER accept invoices without matricule fiscal
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
