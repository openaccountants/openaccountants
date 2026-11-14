---
name: el-salvador-income-tax
description: "Use this skill for El Salvador personal income tax (Impuesto sobre la Renta, ISR) of domiciled individuals and self-employed professionals for tax year 2026. It gives the art. 37 table as reformed by Decreto Legislativo 293 of 30 April 2025 (exempt to USD 6,600, then 10%, 20% and 30% with fixed amounts of USD 212.12, 720.00 and 3,462.86), the 30% rate for non-domiciled individuals, the USD 1,600 fixed deduction for salary earners up to USD 9,100, the USD 800 medical and USD 800 school deductions, the 10% retention on services (Codigo Tributario art. 156), 10% capital gains, 5% on profits distributed, the USD 60,000 filing rule for salary earners and the four-month return deadline. Trigger phrases include renta El Salvador, F-11, declaracion de renta, retencion 10% honorarios, tabla articulo 37 and Ministerio de Hacienda DGII."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/el-salvador-income-tax"
  jurisdiction: "SV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# El Salvador personal income tax (ISR), tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Salvadoran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in El Salvador.

## Who this applies to

Individuals with income obtained in El Salvador (LISR art. 16) for the calendar year 2026, mainly domiciled salary earners with other income and self-employed professionals. The authority is the Ministerio de Hacienda, Direccion General de Impuestos Internos (DGII). The currency is the US dollar.

Refer, do not compute: non-domiciled persons beyond the flat 30% (treaty and source questions), trusts and estates, special regimes (free zones, international services, tech incentives), capital gains on assets held 12 months or less with complex basis, and any DGII audit. Companies: corporate tax is not in this pack yet (LISR art. 41 rate shown below for reference). VAT: [el-salvador-iva](el-salvador-iva.md). Payroll retention: [el-salvador-payroll](el-salvador-payroll.md).

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Domicile unknown | Stop; non-domiciled pay 30% flat (art. 37) |
| Salary only, up to USD 9,100, fully withheld | No return needed; the USD 1,600 fixed deduction is inside the retention (art. 29.7) |
| Medical or school spending without receipts | No art. 33 deduction |
| Self-employed AFP or ISSS | Treat as voluntary unless the client shows affiliation |
| Business use share of a car or phone unknown | Not deductible |
| Payer retained 10% on fees | A credit against the annual tax, not a final tax |

## Rates, bands and thresholds

**Art. 37 table, domiciled individuals, estates and trusts (annual renta neta o imponible, USD), as reformed by Decreto Legislativo 293 of 30 April 2025 (Diario Oficial 79, tomo 447, 30 April 2025), in force eight days after publication.** Applies to tax year 2026.

| Band | From | To | Rate on excess | Over | Plus fixed amount | Source |
| --- | --- | --- | --- | --- | --- | --- |
| I | 0.01 | 6,600.00 | Exempt | | | Asamblea Legislativa, Decreto 293: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/E198E77D-2027-47AA-A8F6-1D70E2F46431.pdf |
| II | 6,600.01 | 9,142.86 | 10% | 6,600.00 | 212.12 | same |
| III | 9,142.87 | 22,857.14 | 20% | 9,142.86 | 720.00 | same |
| IV | 22,857.15 | and above | 30% | 22,857.14 | 3,462.86 | same |

The fixed amount of USD 212.12 starts at USD 6,600.01: the reform moved the exempt ceiling up from USD 4,064 but kept the old fixed amount, so the tax jumps at that point. Keep income just below USD 6,600 in mind.

**Other figures.**

| Item | Amount or rate | Condition | Source |
| --- | --- | --- | --- |
| Non-domiciled individuals, estates and trusts (art. 37) | 30% of renta neta | No table | Asamblea Legislativa, LISR consolidated (D.L. 134): https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf |
| Fixed deduction for salary earners (art. 29.7) | USD 1,600 | Salary only, up to USD 9,100 a year; no proof needed; built into retention | same |
| Medical and hospital costs (art. 33 a) | Up to USD 800 a year | Paid in El Salvador to domiciled licensed professionals, for the taxpayer and close family | same |
| School fees (art. 33 b) | Up to USD 800 a year | Children up to 25 or own studies, at authorised schools | same |
| Salary earners who need not file (art. 38) | Fully withheld salary only | Must file if salary exceeds USD 60,000, or retention does not match the table | same |
| Aguinaldo exempt (art. 4.16) | Up to two monthly minimum wages of commerce and services | Excess is taxed | same |
| Capital gains (art. 42) | 10% of the net gain | Asset held more than 12 months; otherwise added to ordinary income | same |
| Profits distributed to shareholders (art. 72) | 5% final retention | Domiciled or not | same |
| Companies (art. 41), for reference | 30%; 25% if taxable income is USD 150,000 or less | Legal persons | same |
| Non-domiciled artistic and sports groups (art. 40) | 5% of gross per event | | same |
| Retention on services by individuals without employment (CT art. 156) | 10% of the sums paid | Advance of ISR, whatever the amount | Asamblea Legislativa, Codigo Tributario consolidated (D.L. 230): https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf |
| Advance payments of business owners (pago a cuenta, CT art. 151) | 1.75% of monthly gross income | Individuals owning mercantile businesses; 0.3% for listed distributors and passenger transport; within 10 working days after the month | same |

## The base

1. **Income obtained in El Salvador (art. 16):** from goods located, activities carried out or capital invested in the country, and services rendered there.
2. **Salary earners:** the employer retains monthly on the Decreto Ejecutivo 10 tables (see the payroll skill). Up to USD 9,100 of salary, the USD 1,600 deduction and social security contributions are inside the retention and no return is filed.
3. **Self-employed and mixed income:** gross income less the costs and expenses of producing it (art. 29), less the art. 33 deductions (USD 800 medical, USD 800 school). The art. 29.7 USD 1,600 does not apply to them (art. 33).
4. **Exclusions:** income that bore a final retention (5% profits, 20% to non-domiciled) is left out (art. 37). Capital gains over 12 months use the 10% rate separately.
5. **Apply the table**, then credit the 10% service retentions and any pago a cuenta.

Non-deductible (art. 29-A, examples): personal and family living costs, the tax itself, fines, surcharges and interest.

## Deadlines and filing

| Obligation | Deadline | Form or channel |
| --- | --- | --- |
| Annual ISR return (LISR art. 48) | Within four months of year end: by 30 April 2027 for 2026 | DGII form (F-11), Ministerio de Hacienda online services |
| Payment | With the return (CT art. 150) | Banks or online |
| Pago a cuenta (business owners) | Within 10 working days after each month | DGII form |
| Retentions by payers | Monthly | DGII form (F-14) |

## Penalties and interest

| Default | Fine | Source |
| --- | --- | --- |
| Return not filed (CT art. 238 a) | 40% of the tax determined, at least one monthly minimum wage | Codigo Tributario |
| Return late (art. 238 b) | 5% of the tax if up to one month late, 10% up to two, 15% up to three, 20% beyond; at least two minimum wages; one minimum wage if no tax due | same |
| Pago a cuenta not paid (art. 247 a) | 75% of the amount not paid | same |
| Pago a cuenta paid late (art. 247 b) | 50% of the amount paid late | same |
| Retained tax not remitted (art. 246 a) | Equal to the amount not paid | same |
| Tax not retained (art. 246 b) | 75% of the amount not retained | same |

Late payment interest was not confirmed in this pass.

## Cross-border points

Payments to non-domiciled persons for income obtained in El Salvador bear a final 20% retention (CT art. 158), including services from abroad used in El Salvador and royalties; 5% for international transport and for licensed foreign insurers (art. 158 a and b); 25% to persons in tax havens (art. 158-A). Non-domiciled individuals taxed by assessment pay 30%. Profits paid to non-domiciled shareholders bear 5% (LISR arts. 72, 73).

## Two worked examples that recompute

### Example 1: self-employed architect, 2026

Fees USD 30,000, documented costs USD 8,000, medical USD 800 and school USD 800 (both at the cap). Renta imponible USD 20,400, band III. Tax USD 2,971.43. Clients retained 10% (USD 3,000), so the return shows a refund of USD 28.57.

```oa-check
name: SV 2026 self-employed, art. 37 band III and 10% retention
inputs:
  fees: 30000
  costs: 8000
  medical: 800
  school: 800
steps:
  - net: fees - costs - medical - school
  - tax: round(720 + (net - 9142.86) * 0.20, 2)
  - retained: fees * 0.10
  - refund: round(retained - tax, 2)
expected:
  net: 20400
  tax: 2971.43
  retained: 3000
  refund: 28.57
```

### Example 2: does the USD 800 medical deduction matter (decision)

A part-time consultant has net income of USD 6,900 before art. 33 deductions. Without the medical deduction the tax is USD 212.12 + 10% of USD 300 = USD 242.12. With USD 800 of receipted medical costs the base falls to USD 6,100, inside the exempt band: tax nil. Because of the jump at USD 6,600.01, the receipts are worth USD 242.12, more than 30% of what was spent.

```oa-check
name: SV 2026 the step at USD 6,600
inputs:
  net_before: 6900
  medical: 800
steps:
  - tax_without: round(212.12 + (net_before - 6600) * 0.10, 2)
  - net_with: net_before - medical
  - tax_with: 0
  - saving: tax_without - tax_with
expected:
  tax_without: 242.12
  net_with: 6100
  saving: 242.12
```

## Ask the client first

1. Domiciled in El Salvador in 2026? If not, 30% flat or 20% retention applies.
2. Salary only (one employer or several), or also fees, a business, rents, profits or gains?
3. Total salary for the year: up to USD 9,100, up to USD 60,000, or more?
4. Fees received and the 10% retained by each payer (retention certificates).
5. Medical and school receipts paid in El Salvador.
6. Any asset sold, with purchase date and cost.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Decreto Legislativo 293 (30 April 2025), art. 1 (new art. 37 table) and art. 3 (in force) | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/E198E77D-2027-47AA-A8F6-1D70E2F46431.pdf | 2026-11-14 |
| Read for LISR consolidated text (Asamblea Legislativa indice legislativo, to D.L. 900 of 2023), arts. 4.16, 16, 29, 29-A, 33, 34 to 42, 48, 72 to 74 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf | 2026-11-14 |
| Read for Codigo Tributario consolidated text, arts. 150, 151, 155, 156, 158, 158-A, 238, 246, 247 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf | 2026-11-14 |
| Read for the Asamblea record of Decreto 293: date, Diario Oficial 79, tomo 447 | https://www.asamblea.gob.sv/leyes-y-decretos/view/6220 | 2026-11-14 |

Not yet confirmed: late payment interest rate; the 2024 reform on foreign-source income (not in the consolidated text read); whether an annual retention table for 2026 differs from Decreto Ejecutivo 10; form numbers (F-11, F-14) on the current DGII portal; any LISR amendment after D.L. 900 of 2023 other than Decreto 293; corporate tax details beyond the art. 41 rate.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `el-salvador-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/el-salvador-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
