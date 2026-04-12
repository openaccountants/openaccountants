---
name: cameroon-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Cameroon VAT (TVA) return. Trigger on phrases like "TVA Cameroun", "DGI return", "declaration TVA". Cameroon applies TVA at 17.5% plus CAC municipal surcharge (10% of TVA = effective 19.25%). ALWAYS read this skill before touching any Cameroon VAT work.
version: 2.0
---

# Cameroon VAT (TVA) Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Cameroon |
| Standard TVA rate | 17.5% |
| CAC (municipal surcharge) | 10% of TVA amount (effective 1.75% of base) |
| Effective total rate | 19.25% |
| Reduced rate | 10% (social housing, 2026 Finance Law) |
| Zero rate | 0% (exports, international transport) |
| Filing portal | https://fiscalis.minfi.cm |
| Authority | Direction Generale des Impots (DGI) |
| Currency | FCFA (XAF) |
| Filing frequency | Monthly (regime reel); Quarterly (simplifie) |
| Deadline | 15th of following month |
| Registration threshold | FCFA 100M (regime reel); FCFA 50-100M (simplifie) |
| Primary legislation | Code General des Impots, Titre III |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Afriland First Bank, BICEC, Societe Generale Cameroun, Ecobank Cameroun, UBA Cameroun, or any Cameroonian bank.

**Refusal catalogue:**

**R-CM-1 -- Free zone.** Trigger: Douala Free Zone enterprise. Message: "Free zone VAT exemptions require specific decree. Escalate."

**R-CM-2 -- Oil/gas/mining.** Message: "Sector-specific conventions. Escalate."

---

## Section 3 -- Supplier pattern library

### 3.1 Cameroonian banks (fees: exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AFRILAND FIRST BANK, AFRILAND | EXCLUDE | Exempt financial service |
| BICEC | EXCLUDE | Same |
| SGC, SOCIETE GENERALE CAMEROUN | EXCLUDE | Same |
| ECOBANK CAMEROUN | EXCLUDE | Same |
| UBA CAMEROUN | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE | Tax payment |
| DOUANE, CUSTOMS | Check for import TVA | Duty exclude; TVA+CAC recoverable |
| CNPS | EXCLUDE | Social security |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| ENEO, SONATREL | Domestic 19.25% | Electricity |
| CAMWATER, CDE | Domestic 19.25% | Water |
| MTN CAMEROUN, ORANGE CAMEROUN | Domestic 19.25% | Telecoms |

### 3.4 SaaS

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, AWS | Autoliquidation 19.25% (TVA + CAC) | Both TVA and CAC must be self-assessed |
| ZOOM, SLACK, NOTION | Autoliquidation 19.25% | Same |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale with CAC

Taxable base FCFA 1,000,000. TVA = 17.5% x 1,000,000 = FCFA 175,000. CAC = 10% x 175,000 = FCFA 17,500. Total tax = FCFA 192,500 (effective 19.25%).

### Example 2 -- Reverse charge (autoliquidation)

French IT services FCFA 8,000,000. Self-assess TVA FCFA 1,400,000 + CAC FCFA 140,000. Claim input FCFA 1,540,000. Net zero.

---

## Section 5 -- Classification rules

### 5.1 Standard rate 19.25% (17.5% TVA + 10% CAC surcharge)

CAC is 10% of TVA amount, NOT of taxable base. Both always blocked or allowed together.

### 5.2 Reduced rate 10% (social housing, 2026 Finance Law)

### 5.3 Zero-rated

Exports, international transport, diplomatic supplies.

### 5.4 Exempt

Basic foodstuffs, financial services, medical/pharmaceutical, education, residential rental, agricultural inputs, petroleum products (subject to excise).

---

## Section 6 -- VAT return form structure

### Output: A1-A10

A1 (standard sales), A2 (exempt), A3 (exports), A4 (total), A5 (TVA collectee 17.5%), A6 (CAC 10% of A5), A7 (autoliquidation TVA), A8 (CAC autoliquidation), A9 (adjustments), A10 (total TVA+CAC brute).

### Input: B1-B8

B1 (local TVA), B2 (local CAC), B3 (import TVA), B4 (import CAC), B5 (capital goods TVA+CAC), B6 (autoliquidation input), B7 (exclusions), B8 (total deductible).

### Net: C1-C3

C1 = A10-B8. C2 = credit reporte. C3 = payable or carry forward.

---

## Section 7 -- Reverse charge (autoliquidation)

Services from non-resident: self-assess TVA 17.5% + CAC 10% of TVA. Both must be self-assessed. Claim input if taxable. Net zero.

Legislation: CGI, Art. 135.

---

## Section 8 -- Deductibility and blocked input

Blocked (CGI Art. 144-147): vehicles < 9 seats (unless taxi), staff accommodation, entertainment/gifts, fuel for blocked vehicles, personal use, invoices without NIU.

TVA and CAC always blocked or allowed together.

Partial exemption (prorata): CGI Art. 143. DGI approval required.

---

## Section 9 -- Filing, deadlines, and penalties

| Regime | Period | Deadline |
|---|---|---|
| Regime reel | Monthly | 15th of following month |
| Simplifie | Quarterly | 15th of month following quarter |

| Violation | Penalty |
|---|---|
| Late filing | 30% surcharge |
| Late payment | 1.5% per month |
| Failure to register | 100% of tax due |

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- US SaaS.** Autoliquidation. TVA 17.5% + CAC. Net zero.

**EC2 -- Timber export.** Zero-rated. Input TVA+CAC recoverable.

**EC3 -- Motor vehicle blocked.** Both TVA and CAC blocked.

**EC4 -- CEMAC import (Gabon).** TVA+CAC at Cameroon customs. No intra-community mechanism.

**EC5 -- Excise + TVA.** TVA calculated on price INCLUDING excise duty.

**EC6 -- Bad debt relief.** Court judgment required. Reviewer flag.

### Test suite

**Test 1 -- Standard sale.** FCFA 10M. Expected: TVA FCFA 1.75M, CAC FCFA 175K, total FCFA 1.925M.

**Test 2 -- Local purchase.** FCFA 5M + TVA 875K + CAC 87.5K. Expected: both recoverable.

**Test 3 -- Reverse charge.** French services FCFA 8M. Expected: output TVA 1.4M + CAC 140K. Input 1.54M. Net zero.

**Test 4 -- Export.** Cocoa FCFA 200M. Expected: zero-rated. Input recoverable.

**Test 5 -- Blocked entertainment.** FCFA 3M + TVA 525K + CAC 52.5K. Expected: both blocked. Cost FCFA 3.577M.

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Out of scope -- direct tax

- Corporate IS: 33% (including 10% surcharge)
- PAYE (IRPP): progressive 10%-35%
- CNPS: family 7%, work injury 1.75%-5%

### Prohibitions

- NEVER separate TVA recovery from CAC -- always together
- NEVER confuse zero-rated with exempt
- NEVER treat CEMAC as intra-community
- NEVER accept invoices without NIU
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit reporte

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
