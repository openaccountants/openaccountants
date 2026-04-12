---
name: qatar-tax
description: Use this skill whenever asked about Qatar indirect tax or VAT status. Qatar does NOT have VAT/GST as of April 2026. This skill documents the current tax landscape and expected future VAT under the GCC Unified VAT Agreement. ALWAYS read before advising on Qatar tax.
version: 2.0
---

# Qatar Tax Status Skill v2.0 (No VAT/GST)

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | State of Qatar |
| VAT/GST status | NOT IMPLEMENTED as of April 2026 |
| Expected VAT rate | 5% (per GCC Agreement, but Qatar may choose differently) |
| Corporate income tax | 10% on non-Qatari share of profits |
| Excise tax | Tobacco 100%, energy drinks 100%, carbonated 50% |
| Authority | General Tax Authority (GTA) |
| Portal | https://www.gta.gov.qa |
| Currency | QAR |
| Primary legislation | Law No. 24/2018 (Income Tax); GCC VAT Agreement (not implemented) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from QNB, Commercial Bank, Doha Bank, Al Khaliji, Masraf Al Rayan, or any Qatari bank.

---

## Section 3 -- Supplier pattern library

### 3.1 Qatari banks

| Pattern | Treatment | Notes |
|---|---|---|
| QNB, QATAR NATIONAL BANK | EXCLUDE | No VAT system |
| COMMERCIAL BANK, CBQ | EXCLUDE | Same |
| DOHA BANK, MASRAF AL RAYAN | EXCLUDE | Same |

### 3.2 Government

| Pattern | Treatment | Notes |
|---|---|---|
| GTA, GENERAL TAX AUTHORITY | EXCLUDE | Tax payment |
| CUSTOMS | Customs duty only | No VAT at border |

Note: no VAT patterns needed -- Qatar has no VAT system.

---

## Section 4 -- Worked examples

### Example 1 -- Client asks about Qatar VAT

"Does Qatar have VAT?" -- No. Qatar has not implemented VAT. No VAT return, registration, or collection required.

### Example 2 -- Purchase from UAE supplier

Qatar company buys goods from UAE. UAE supplier charges 5% UAE VAT. The UAE VAT is an irrecoverable cost to the Qatar company. No mechanism to recover it in Qatar.

---

## Section 5 -- Classification rules

### 5.1 No VAT

No VAT registration, returns, invoicing, reverse charge, or input recovery exists in Qatar.

### 5.2 Corporate income tax

10% flat on non-Qatari-owned share of profits. Qatari/GCC-owned share exempt. Oil/gas: up to 35%.

### 5.3 Excise tax

Tobacco 100%, energy drinks 100%, carbonated 50%, special purpose goods 100%. Monthly return to GTA.

### 5.4 Customs duties

Standard 5% CIF. GCC-origin goods exempt. Free zones may exempt.

---

## Section 6 -- No VAT return form

No VAT return exists. CIT return filed within 4 months of fiscal year end.

---

## Section 7 -- No reverse charge

No VAT system means no reverse charge mechanism.

---

## Section 8 -- No input deductibility

No input VAT recovery mechanism. Foreign VAT paid (e.g., UAE 5%, Saudi 15%) is irrecoverable cost.

---

## Section 9 -- Cross-border implications

Qatar businesses bear irrecoverable foreign VAT from GCC implementing states. No mechanism to recover. Non-implementing states (Qatar, Kuwait) treated as non-GCC by implementing states.

When VAT arrives: include change-of-law clauses in long-term contracts.

---

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- "Do I need to charge VAT?"** No. Issue invoices without VAT.

**EC2 -- UAE invoice with 5% VAT.** Irrecoverable cost.

**EC3 -- Export to Saudi Arabia.** No Qatar VAT. Saudi customer accounts for import VAT under Saudi rules.

**EC4 -- VAT grouping.** No VAT group possible in Qatar.

**EC5 -- Long-term contract.** Prudent to include VAT change-of-law clause.

**EC6 -- Digital services.** No Qatar VAT on digital services.

**EC7 -- Withholding tax.** 5% WHT on payments to non-residents for services in Qatar. This is CIT, NOT VAT.

**EC8 -- Excise vs VAT.** Energy drink tax is excise, NOT VAT.

**EC9 -- Free zone entity.** CIT exemptions for up to 20 years. No VAT. Excise still applies.

### Test suite

**Test 1 -- Domestic sale.** QAR 50,000 consulting. Expected: no VAT. Invoice without VAT line.

**Test 2 -- UAE purchase.** AED 10,000 + AED 500 UAE VAT. Expected: total cost AED 10,500. UAE VAT irrecoverable.

**Test 3 -- Export to Oman.** QAR 100,000. Expected: no Qatar VAT. Oman handles import VAT.

**Test 4 -- Non-resident WHT.** UK consultant QAR 30,000 services in Qatar. Expected: 5% WHT = QAR 1,500. This is CIT, not VAT.

**Test 5 -- Excise.** 1,000 cases energy drinks CIF QAR 20,000. Expected: excise QAR 20,000 (100%), customs QAR 1,000 (5%).

### Escalation protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

### Prohibitions

- NEVER state Qatar has VAT -- it does not
- NEVER advise charging VAT on Qatar invoices
- NEVER advise filing VAT returns in Qatar
- NEVER advise registering for VAT in Qatar
- NEVER confuse excise tax with VAT
- NEVER advise foreign VAT is recoverable in Qatar
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
