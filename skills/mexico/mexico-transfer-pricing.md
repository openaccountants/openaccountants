---
name: mexico-transfer-pricing
description: Use this skill whenever asked about Mexico transfer pricing rules, documentation requirements, or precios de transferencia compliance. Trigger on phrases like "transfer pricing Mexico", "Mexican TP documentation", "precios de transferencia Mexico", "master file Mexico", "local file Mexico", "CbCR Mexico", "APA Mexico", "SAT transfer pricing", "maquiladora safe harbor", "Article 76 LISR", or any question about intercompany pricing for Mexican entities.
version: 1.2
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-14
type: situation-rules
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico Transfer Pricing

## Who this applies to

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Mexico (United Mexican States) |
| Tax authority | Servicio de Administración Tributaria (SAT) |
| Key TP legislation | Articles 76, 76-A, 179-184, Income Tax Law (Ley del ISR -- LISR); Fiscal Code (CFF) Art. 34-A (APA) |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | MXN |
| Documentation language | Spanish (Local File); Master File in Spanish or English |
| TP documentation types | Four types: TP Report, Local File, Master File, CbCR |
| Skill version | 1.0 |

## Rates, bands and thresholds

| Threshold | Amount | Source |
| --- | --- | --- |
| CbCR: prior-year consolidated accounting revenues | Equal to or above MXN 12,000,000,000 (fixed; LIF modification possible only by Congress) | [LISR Art. 76-A fr. III item 6, DOF 18-11-2015 ("doce mil millones de pesos")](https://dof.gob.mx/nota_detalle.php?codigo=5415878&fecha=18/11/2015) |
| Master/local informative returns: large-taxpayer classes | Art. 32-H fr. I class: accumulated income equal to or above MXN 1,103,204,520.00 (updated through DOF 28-12-2025) | [CFF Art. 32-H fr. I amount, RMF 2026 Anexo 5, DOF 28-12-2025 ("$1,103,204,520.00")](https://dof.gob.mx/nota_detalle.php?codigo=5777219&fecha=28/12/2025); LISR Art. 76-A first paragraph |
| TP documentation exemption (business) | Prior-year income up to MXN 13,000,000.00 | [LISR Art. 76 fr. IX, DOF 11-12-2013 ("no hayan excedido de $13 '000,000.00")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |
| TP documentation exemption (professional services) | Prior-year service income up to MXN 3,000,000.00 | [LISR Art. 76 fr. IX, DOF 11-12-2013 ("no hubiesen excedido en dicho ejercicio de $3 '000,000.00")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |
| Maquiladora safe harbour | Greater of 6.9% of total assets or 6.5% of total costs and expenses | [LISR Art. 182 frs. I and II, DOF 11-12-2013 ("El 6.9%", "El 6.5%")](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |

## The taxable base

### 3.1 Definition

- **Arm's length principle** -- Transactions between related parties must be valued as if they were carried out between independent parties in comparable operations. The arm's length principle applies.  _(Article 179 LISR)_

### 3.2 Accepted Methods (Article 180 LISR)

**3.2 Accepted Methods (Article 180 LISR)**  _(Article 180 LISR)_

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |
| Residual Profit Split | Yes |

### 3.3 Preferred Method

- **Preferred method** -- CUP is preferred by SAT where applicable. Discounted cash flow method accepted for transactions involving intangibles under certain conditions.

### 3.4 Range

- **Range application** -- Interquartile range applied; adjustment to median if result outside range.

## Deadlines and filing

**Section 4 -- Filing Obligations**

| Obligation | Detail |
| --- | --- |
| TP Report | Maintain; available on SAT audit request |
| Local File | Annual electronic filing (May 15) |
| Master File | Annual electronic filing (December 31) |
| CbCR | Annual electronic filing (December 31) |
| Annual tax return (Declaración Anual) | Includes informative obligations on related-party transactions |
| Informative multiple return | Related-party transaction information in annual return |

### Deadline table

| Item | Deadline |
| --- | --- |
| Local File | May 15 of the following fiscal year |
| Master File | December 31 of the following fiscal year |
| CbCR | December 31 of the following fiscal year |
| TP Report preparation | By time of annual tax return filing (March 31 for legal entities) |
| Annual tax return | March 31 of the following fiscal year |
| Maquiladora informative return | June of the following fiscal year |

## Penalties and interest

**Section 6 -- Penalties**

| Offence | Penalty |
| --- | --- |
| Late/incomplete Art. 76-A informative returns (infraction: CFF Art. 81 fr. XL; fine: CFF Art. 82 fr. XXXVII, amounts updated by RMF and compiled in the consolidated CFF text, actualizada DOF 28-12-2025) | MXN 226,000.00 -- MXN 321,770.00 (2026) |
| Failure to file Local File / Master File | Same CFF Art. 81 fr. XL infraction / Art. 82 fr. XXXVII fine range (Art. 76-A returns) |
| SAT TP adjustment -- tax omission | 55-75% of the omitted contributions (CFF Art. 76; Art. 64 repealed) |
| Late payment surcharge (recargos) | Annual variable rate under CFF Art. 22, applied to the updated amount |
| Inflation adjustment | Contributions updated under CFF Art. 65 |
| Non-compliance with maquiladora safe harbor | Deemed permanent establishment of foreign principal |

## Cross-border points

- The master file and CbCR exist only because the counterparty group is multinational (LISR Art. 76-A); purely domestic related-party flows carry the Art. 76 fr. IX documentation and the Art. 76 fr. X informative return (15 May).
- CbCR data feeds SAT risk-based audit selection; exchange with the foreign parent's authority depends on the competent-authority framework (CRMA) -- procedure not read in an archived source.
- TP disputes on cross-border flows can go to the Mutual Agreement Procedure under Mexico's treaties (treaty texts not archived).

## Worked examples

### Worked example 1: CbCR threshold test

A Mexican multinational group reports consolidated accounting revenues of MXN 12,500,000,000 for FY2025. The statutory trigger is revenues equal to or above MXN 12,000,000,000, so the CbCR is due by 31 December 2026.

```oa-check
name: cbcr threshold test
inputs:
  ingresos_consolidados: 12500000000
  umbral: 12000000000
steps:
  - excedente: ingresos_consolidados - umbral
expected:
  excedente: 500000000
```

### Worked example 2: TP documentation exemption test

A professional-services individual earned MXN 2,800,000 of service income in the prior year. The Art. 76 fr. IX exemption ceiling for service income is MXN 3,000,000, so the full TP study is not required (the Art. 179 exceptions still must be checked).

```oa-check
name: tp documentation exemption headroom
inputs:
  techo_servicios: 3000000
  ingresos_servicios: 2800000
steps:
  - margen: techo_servicios - ingresos_servicios
expected:
  margen: 200000
```

## Ask the client first

1. Which entities sit in Mexico and which related parties are abroad (residence drives Art. 76-A applicability)?
2. Prior-year consolidated accounting revenues (CbCR trigger) and each entity's accumulated income (Art. 32-H classes and the Art. 76 fr. IX exemption).
3. What related-party flows exist by type (goods, services, intangibles, financing) and are comparables already on file?
4. Is the entity a maquiladora under Art. 181 (safe-harbour election and the June informative return)?

## Section 2 -- Documentation Requirements

### 2.1 TP Report (Estudio de Precios de Transferencia)

**2.1 TP Report (Estudio de Precios de Transferencia)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for taxpayers with related-party transactions (general obligation under Art. 76 LISR) |
| Threshold | All entities with controlled transactions must have TP study available. Exemption (LISR Art. 76 fr. IX final paragraph): business taxpayers whose prior-year income did not exceed MXN 13,000,000.00, and professional-services taxpayers whose prior-year income from services did not exceed MXN 3,000,000.00, are not obliged to keep this documentation (exceptions: the Art. 179 penultimate-paragraph case and contractors/assignatarios) |
| Content | Functions/assets/risks, method selection, comparables, arm's length analysis |
| Language | Spanish |
| Filing | Not filed; maintained and available on SAT request |

### 2.2 Local File (Archivo Local)

**2.2 Local File (Archivo Local)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for taxpayers referenced in CFF Art. 32-H frs. I, II, III, IV and VI with related-party transactions (LISR Art. 76-A first paragraph); for the large-taxpayer class of Art. 32-H fr. I the threshold is accumulated income equal to or above MXN 1,103,204,520.00 (amount updated by the RMF through DOF 28-12-2025; re-indexed each January under CFF Art. 32-H) |
| Format | Per BEPS Action 13 / OECD standards with Mexico-specific content |
| Language | Spanish |
| Filing deadline | May 15 of the following fiscal year |
| Filing method | Electronic submission to SAT |

### 2.3 Master File (Archivo Maestro)

**2.3 Master File (Archivo Maestro)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for entities meeting the income threshold (same as Local File) |
| Format | OECD Annex I to Chapter V |
| Language | Spanish or English |
| Filing deadline | December 31 of the following fiscal year |
| Filing method | Electronic submission |

### 2.4 Country-by-Country Report (CbCR)

**2.4 Country-by-Country Report (CbCR)**

| Item | Detail |
| --- | --- |
| Threshold | Multinational group with consolidated accounting revenues equal to or above MXN 12,000 million in the prior year (LISR Art. 76-A fr. III item 6). The amount is fixed in the statute and modifiable only by Congress through the Ley de Ingresos de la Federacion (LIF 2025 contains no modification); it is not inflation-indexed. The EUR 750m OECD figure is a comparator only, with no Mexican primary source |
| Filing deadline | December 31 of the following fiscal year |
| Content | Per OECD Annex III |
| Filing method | Electronic |

### 2.5 Important Distinction

- **Distinction between TP Report and Local File** -- Mexico distinguishes between: 1. TP Report (all entities with related-party transactions) -- general support file. 2. Local File (large entities over threshold) -- OECD BEPS Action 13 format, filed with SAT. Both must be prepared; the Local File is more detailed and includes some Master File content.

## Section 7 -- Advance Pricing Agreements (APA)

**Section 7 -- Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes (general APA under Art. 34-A CFF) |
| Types | Unilateral (primarily); bilateral available |
| Governing legislation | Article 34-A, Fiscal Code (CFF) |
| Application | To SAT with proposed methodology |
| Duration | Up to 5 years (year of request + 1 prior + up to 3 forward) |
| Fees | No formal fee |
| Processing time | Variable; historically lengthy |
| Maquiladora APA | ELIMINATED from 2022 reform; no longer available from FY2025 |

### Important: Maquiladora APA Elimination

- **Maquiladora APA elimination** -- From 2025, maquiladoras can NO longer request APAs. The sole mechanism available is the safe harbour (Article 182 LISR).  _(Article 182 LISR)_

## Section 8 -- Safe Harbours

### 8.1 Maquiladora Safe Harbour (Article 182 LISR)

**8.1 Maquiladora Safe Harbour (Article 182 LISR)**  _(Article 182 LISR)_

| Item | Detail |
| --- | --- |
| Applicable to | Maquiladora companies operating under Art. 181 LISR |
| Calculation | Taxable profit = GREATER of: 6.5% of total costs/expenses (including foreign-sourced) OR 6.9% of total assets (including foreign-owned assets) |
| Mandatory from 2025 | Only mechanism available (APA option eliminated) |
| Consequence of non-compliance | Foreign principal deemed to have a Permanent Establishment in Mexico |
| Annual informative return | Required in June of following year |

### 8.2 General Transactions

- **No safe harbour for general transactions** -- No safe harbour for non-maquiladora related-party transactions. All must be at arm's length with supporting documentation.

## Section 9 -- Recent Developments

**Section 9 -- Recent Developments**

| Date | Development |
| --- | --- |
| 2025 | Maquiladora APA option expired (last APAs covered 2021-2024); safe harbour now mandatory |
| 2024 | Updated indexed thresholds for documentation obligations |
| 2022 | Tax reform eliminated maquiladora APA from Article 182 LISR |
| 2025 | Pillar Two under discussion; no legislation enacted yet |
| Ongoing | SAT increasing TP audit activity, especially on maquiladoras and digital services |
| Ongoing | Focus on substance requirements for intercompany transactions |
| May 2026 | First Local File filing deadline for FY2025 (May 15, 2026) |

## Section 10 -- Interaction with Other Skills

**Section 10 -- Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| mexico-corporate-tax (ISR) | TP adjustments directly affect income tax (ISR) base |
| mexico-bookkeeping | TP documentation relies on Mexican accounting standards (NIF) |
| mexico-vat (IVA) | TP adjustments may affect customs valuation and IVA |
| Maquiladora regime | Safe harbour is the sole TP mechanism for maquiladoras from 2025 |
| Customs valuation | Related-party import pricing must be consistent with TP positions |
| CbCR | SAT uses CbCR for risk-based audit selection |
| Double tax treaties | Mexico's DTA network provides MAP for TP disputes |

## Sources

| Source | URL | Read on |
|---|---|---|
| DOF 18-11-2015, LISR reform decree, read for Art. 76-A fr. III item 6 (CbCR trigger of twelve thousand million pesos) | https://dof.gob.mx/nota_detalle.php?codigo=5415878&fecha=18/11/2015 | 2026-11-14 |
| DOF 11-12-2013, decree issuing the LISR, second part, read for Art. 76 fr. IX (MXN 13,000,000 and 3,000,000 documentation exemptions) and Art. 182 (6.9% of assets, 6.5% of costs) | https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013 | 2026-11-14 |
| DOF 28-12-2025, RMF 2026 Anexos 4, 5, 6, 8, 15 and 25, read for Anexo 5 (CFF Art. 32-H fr. I amount MXN 1,103,204,520.00) | https://dof.gob.mx/nota_detalle.php?codigo=5777219&fecha=28/12/2025 | 2026-11-14 |
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 76 frs. IX and X, 76-A, 179, 180, 181, 182 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-29 |
| Código Fiscal de la Federación, consolidated (Cámara de Diputados, last reform DOF 09-04-2026), Arts. 22, 32-H, 34-A, 65, 76, 81 fr. XL, 82 fr. XXXVII (multa $226,000.00 a $321,770.00, actualizada DOF 28-12-2025) | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-10-31 |
| SAT, Resolución Miscelánea Fiscal 2025, Anexo 5 (2025 fine amounts for CFF infractions; item XXXVII: MXN 199,630.00 to MXN 284,220.00 for CFF Art. 81 fr. XL -- superseded for 2026 by the amounts compiled in the consolidated CFF text) | http://omawww.sat.gob.mx/normatividad_RMF_RGCE/Paginas/documentos2025/rmf/anexos/Anexo5_RMF2025-30122024.pdf | 2026-11-02 |

Not yet confirmed: the June deadline for the maquiladora informative return (LISR Art. 32-A second paragraph not read in full); APA duration and scope details (CFF Art. 34-A read only at the heading level); interquartile-range and median-adjustment mechanics (not stated in the LISR text read; OECD practice); the "May 2026 first Local File deadline" and other Section 9 developments (news items, no archived primary source); Pillar Two status in Mexico.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
