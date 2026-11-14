---
name: panama-itbms
description: >
  Use this skill for Panama's goods and services tax (Impuesto de Transferencia de
  Bienes Muebles y Servicios, ITBMS) in 2026. It gives the 7% general rate, 10% on
  alcoholic drinks and on lodging, 15% on tobacco, the exemptions DGI lists (medicines,
  basic school supplies, uniforms, textbooks, food, farm products, electricity and
  water, medical and laboratory services), the B/.36,000 annual turnover at which a
  business must charge ITBMS, input credit, the 50% ITBMS credit against income tax for
  non-contributors, retention agents, the monthly return in the first 15 days and DGI
  fines. Trigger phrases include ITBMS Panama, impuesto de transferencia, 7% ITBMS,
  certificado de no contribuyente, formulario 430 and agente de retencion ITBMS.
version: "1.0"
jurisdiction: PA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Panama ITBMS (goods and services tax), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Panamanian accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Panama.

## Who this applies to

Businesses and professionals selling goods or services in Panama whose annual turnover exceeds B/.36,000 (or whose activity requires it), plus retention agents. Amounts are in balboas (B/.), at par with the US dollar. The authority is the Direccion General de Ingresos (DGI) of the Ministerio de Economia y Finanzas; returns are filed in e-Tax 2.0.

Below B/.36,000 a business does not charge ITBMS and can obtain a Certificado de No Contribuyente so that retention agents do not retain on its sales. Taxpayers in arrears or who have not filed cannot get any certificate.

Refer: free zones (Colon Free Zone and others; trade between zone companies is exempt), SEM and Panama Pacifico, the selective consumption tax (ISC) on drinks and tobacco, real estate (ITBI), imports beyond the basic rule, and any audit.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Rate unknown | 7% |
| Turnover near B/.36,000 | Register and charge once the year's turnover exceeds it |
| Purchase without a valid fiscal invoice naming the buyer and RUC | No credit |
| Payment to a foreign provider with no Panama branch | Retain the ITBMS as agent |

## Rates, bands and thresholds

| Item | Rate or amount | Condition | Source |
| --- | --- | --- | --- |
| General rate | 7% | From 1 July 2010 (Ley 8 de 2010 art. 76); includes restaurants with prepared food | DGI, Generalidades del ITBMS: https://dgi.mef.gob.pa/itbms/Generalidades.php |
| Alcoholic drinks (import, wholesale, retail) | 10% | | same |
| Lodging in all forms | 10% | | same |
| Tobacco products | 15% | | same |
| Turnover above which ITBMS must be charged | B/.36,000 a year | Goods and services | DGI, ITBMS: https://dgi.mef.gob.pa/itbms/Itbms.php |
| Return and payment | First 15 days of the following month | Monthly | DGI, Generalidades del ITBMS: https://dgi.mef.gob.pa/itbms/Generalidades.php |
| Late return fine | B/.10.00 | | DGI FAQ, ITBMS: https://dgi.mef.gob.pa/Preguntas/Itbms.php |
| Amended return after 90 days | B/.100 (individuals), B/.500 (companies) | One amendment a period, within 12 months | same |
| Fines for companies | B/.500 to B/.5,000 for repeat breaches | Plus possible closure | DGI, Generalidades del ITBMS: https://dgi.mef.gob.pa/itbms/Generalidades.php |
| Defrauding ITBMS | 5 to 10 times the tax defrauded, or 1 month to 1 year arrest | | same |
| ITBMS of non-contributors credited against income tax | 50% of ITBMS on purchases, up to 10% of the income tax | Codigo Fiscal art. 701 l) | same |
| Retention agents: large buyers | Annual purchases of B/.5,000,000 or more | DE 84 of 2005 art. 19 | DGI FAQ, ITBMS: https://dgi.mef.gob.pa/Preguntas/Itbms.php |

## The base

- **Taxed:** transfer of movable goods and provision of services in Panama, and imports. Exports are not charged ITBMS (DGI FAQ).
- **Not charged (DGI list):** medicines, basic school supplies, uniforms, textbooks, food, farm products, public services (electricity, water), medical services and laboratories. Fondas and fast-food restaurants do not charge ITBMS on that food.
- **Credit:** a registered contributor credits the ITBMS on purchases and services inherent to its activity against ITBMS charged; it may not use it against income tax. ITBMS shown on the purchases report cannot exceed 15% of the purchase.
- **Non-contributors:** ITBMS paid is a cost; 50% of ITBMS on documented purchases (with the buyer's name and RUC) may be credited against income tax, capped at 10% of the tax; self-employed filers deduct ITBMS inherent to the activity as an expense and credit only the rest.
- **Retention:** agents (state entities, payers of foreign suppliers without a Panama establishment, large buyers with purchases of B/.5,000,000 or more, card processors) retain ITBMS; the supplier enters retentions on line 52 of form 430. No retention if the supplier shows a Certificado de No Contribuyente.
- **Free zones:** trade between companies inside a free zone is exempt.

The ITBMS account is a current liability (Tesoro Nacional ITBMS) for contributors and a cost for non-contributors.

## Deadlines and filing

| Obligation | Deadline | Form |
| --- | --- | --- |
| ITBMS return and payment | First 15 days of the following month | Form 430, e-Tax 2.0 |
| ITBMS retention return | First 15 days of the month | e-Tax 2.0 |
| Purchases report | With the monthly figures; must match the return | Informe de Compras |

## Penalties and interest

Late return: B/.10. Amended return more than 90 days (three months) after the original: B/.100 individuals, B/.500 companies. Company breaches B/.500 to B/.5,000 if repeated, plus possible administrative closure. Fraud: 5 to 10 times the tax or 1 month to 1 year of arrest, split equally with accomplices.

## Cross-border points

Exports are not charged. Imports pay ITBMS at customs (form 433 for import ITBMS). A Panamanian payer of a foreign supplier without a Panama establishment retains the ITBMS; a company paying professional fees abroad becomes a retention agent for 100% of the tax.

## Two worked examples that recompute

### Example 1: small hotel with a bar, March 2026

Room revenue B/.20,000 (10%: B/.2,000), bar drinks B/.5,000 (10%: B/.500), restaurant food B/.10,000 (7%: B/.700). ITBMS on purchases with valid invoices B/.1,200. Payable B/.2,000 by 15 April 2026.

```oa-check
name: PA 2026 ITBMS hotel, three rates
inputs:
  rooms: 20000
  drinks: 5000
  food: 10000
  input_itbms: 1200
steps:
  - output: rooms * 0.10 + drinks * 0.10 + food * 0.07
  - payable: output - input_itbms
expected:
  output: 3200
  payable: 2000
```

### Example 2: freelance designer, charge ITBMS or not (decision)

A designer billing B/.30,000 a year is below B/.36,000: no ITBMS charged, and a Certificado de No Contribuyente stops retentions; ITBMS on purchases is a cost. At B/.40,000 the designer must charge 7%, B/.2,800 a year, file monthly, and credit input ITBMS. The figure that decides it is B/.36,000 of annual turnover.

```oa-check
name: PA 2026 ITBMS registration threshold
inputs:
  turnover_a: 30000
  turnover_b: 40000
  threshold: 36000
steps:
  - itbms_a: turnover_a * 0.07 * min(max(turnover_a - threshold, 0), 1)
  - itbms_b: turnover_b * 0.07 * min(max(turnover_b - threshold, 0), 1)
expected:
  itbms_a: 0
  itbms_b: 2800
```

## Ask the client first

1. Annual turnover, and whether it passed B/.36,000.
2. What is sold: general goods, food (restaurant or fast food), alcohol, tobacco, lodging, exempt items?
3. Customers: state entities, large buyers or card payments that retain ITBMS?
4. Purchases with valid fiscal invoices naming the buyer and RUC.
5. Payments to foreign suppliers, imports, exports, free zone status.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI, ITBMS page: 7%, B/.36,000 threshold, 10% and 15% rates, items not charged | https://dgi.mef.gob.pa/itbms/Itbms.php | 2026-11-14 |
| Read for DGI, Generalidades del ITBMS: Ley 8 de 2010 art. 76 rate, rate table, 50% credit against income tax, filing in the first 15 days, fines, retention rules, free zones | https://dgi.mef.gob.pa/itbms/Generalidades.php | 2026-11-14 |
| Read for DGI FAQ, ITBMS: retention return, certificates, amendments, late fine B/.10, obligation above B/.36,000, line 52 of form 430, exports, retention agents | https://dgi.mef.gob.pa/Preguntas/Itbms.php | 2026-11-14 |

Not yet confirmed: the full legal list of exempt goods and services (Codigo Fiscal art. 1057-V not read; the DGI summary list is used); the retention percentages applied by agents (50% or 100% by case); ITBMS on digital services from abroad; the box layout of form 430 beyond line 52; late payment surcharge and interest.
