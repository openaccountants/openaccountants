---
name: nicaragua-iva
description: "Use this skill for Nicaragua value added tax (Impuesto al Valor Agregado, IVA) in 2026. It gives the 15% rate shown separately on the invoice, the exempt goods of Ley 822 art. 127 as reformed by Ley 987 (books and school material, medicines, unprocessed listed farm products, basic foods such as rice, eggs, tortilla, simple bread, milk and listed meats, LPG up to 25 pounds, fuels bearing IECC and IEFOMAV, used goods, real estate), the exempt services of art. 136 (human medical care, internal transport, education, public water, banking and interest), the rule that exemptions need a franchise letter at the time of sale, and the monthly declaration through the DGI VET. Trigger phrases include IVA Nicaragua, 15% IVA, exenciones IVA, franquicia, DGI VET and declaracion mensual."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nicaragua-iva"
  jurisdiction: "NI"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nicaragua value added tax (IVA), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Nicaragua.

## Who this applies to

Persons who sell goods, provide services or import in Nicaragua and are registered with the DGI in the general regime, under Title III of the Ley de Concertacion Tributaria (Ley 822) as reformed by Ley 987 of 2019.

Refusal catalogue:
- **R-NI-1 Cuota fija.** Small traders in the cuota fija regime pay a fixed monthly amount and do not file IVA returns.
- **R-NI-2 Free zones.** Zona franca entities have their own exemptions; refer.
- **R-NI-3 Cooperatives and exoneration holders.** Special treatment; refer.
- **R-NI-4 ISC goods** (drinks, tobacco): import base rules of art. 130; refer.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Rate unknown | 15% |
| Customer claims exemption but shows no franchise letter at the time of sale | Charge 15%; the customer claims a refund from DGI (DGI FAQ) |
| Purchase without a valid invoice | No credit |
| Business use of a vehicle or phone unknown | No credit |

## Rates, bands and thresholds

| Item | Rate or rule | Condition | Source |
| --- | --- | --- | --- |
| General rate | 15% | Shown expressly and separately on the invoice | DGI FAQ, Determinacion del IVA: https://www.dgi.gob.ni/FAQ/determinacion_del_iva.htm |
| IVA and income tax | IVA is not income for IR and not part of its base | LCT art. 114 | same |
| Sale to an exempt customer without franchise | 15% charged; customer seeks refund | If DGI finds no support, the seller pays as jointly liable | same |
| Exempt goods (art. 127) | Exempt, by ministerial lists | 18 numbered groups | La Gaceta 41 of 28 Feb 2019, Ley 987 (copy at MEM): https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf |
| LPG (art. 127.11) | Exempt | Butane, propane or mix, containers up to 25 pounds | same |
| Exempt imports (art. 131.1) | Exempt | Goods whose local sale is exempt, except used goods | same |
| Exempt services (art. 136) | Exempt | Listed services | same |

## The base

**Exempt goods (art. 127, Ley 987):** books, magazines, school and scientific materials and their inputs; medicines, vaccines, prostheses, glucose testing, clinical oxygen, reagents, wheelchairs and their inputs; medical, surgical, dental and diagnostic equipment; unprocessed rice, maize, wheat, black and red beans, tomato, onion, sweet pepper, cabbage, potato, banana, plantain, sorghum, soya, sugar cane and palm kernel; rice of 80/20 quality or lower, soya and palm oil, salt, sulphited cane sugar and ground coffee up to 115 grams; eggs, maize tortilla, pinol, wheat flour, simple and traditional sweet bread, yeast for it, maize and soya flour; modified, infant and whole milk and artisan cheese; live animals (not pets or pedigree horses); fresh fish; listed cuts of beef, pork and chicken (not fillets, loins and other special cuts); LPG up to 25 pounds; crude oil and fuels that bore IECC and IEFOMAV; used movable goods; transfer of real estate; free port purchases; sales at qualifying fairs; currency, lottery, shares and securities; solar panels, deep-cycle solar batteries and energy-saving lamps.

**Exempt services (art. 136):** human medical and dental care (not cosmetic); farm and compulsory motor insurance premiums; non-profit sports events; religious events; internal air, land, lake, river and sea transport; freight for export; education by educational entities; electricity for irrigation; public water; banking and microfinance services; interest including finance leases; and further items in the article not read in full.

**Credit:** IVA paid on purchases for taxed activity is credited against IVA charged; the credit and proportionality rules (Ley 822 arts. 112 onward) were not read in this pass.

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Monthly IVA declaration (form 110) | Not confirmed in this pass (the old file said the 15th of the following month) | DGI VET |
| Retained IVA | With the monthly declaration of recaudos y anticipos | DGI VET |
| Nil declarations | Required even with no activity | DGI VET |

## Penalties and interest

Codigo Tributario: fines in unidades de multa, closure and loss of benefits (art. 124); 110 to 130 units for late books (art. 127.4). See Not yet confirmed for surcharges.

## Cross-border points

Imports pay IVA at customs on the art. 130 base unless exempt (art. 131). Exports: zero rating and credit refunds were not confirmed in this pass. Services from abroad: not confirmed.

## Two worked examples that recompute

### Example 1: hardware store, October 2026

Taxed sales C$1,000,000 (IVA C$150,000), IVA on purchases with valid invoices C$90,000. IVA payable C$60,000.

```oa-check
name: NI 2026 IVA monthly position
inputs:
  sales: 1000000
  input_iva: 90000
steps:
  - output_iva: sales * 0.15
  - payable: output_iva - input_iva
expected:
  output_iva: 150000
  payable: 60000
```

### Example 2: furniture dealer, used or new (decision)

Selling C$100,000 of used furniture is exempt (art. 127.13): no IVA. The same sale of new furniture carries C$15,000 of IVA. A dealer selling both must separate the two on its invoices and books, because the exemption follows the goods, not the dealer.

```oa-check
name: NI 2026 used goods exempt
inputs:
  sale: 100000
steps:
  - iva_used: 0
  - iva_new: sale * 0.15
  - difference: iva_new - iva_used
expected:
  iva_new: 15000
  difference: 15000
```

## Ask the client first

1. Regime: general or cuota fija? Any franchise, free zone or cooperative status?
2. What is sold, item by item, and which items are on the art. 127 lists?
3. Customers holding exemption franchises, and whether letters were shown at the sale.
4. Purchases with valid invoices and their use.
5. Imports and exports in the month.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI FAQ, Determinacion del IVA: 15% rate, separate statement, exempt customers, art. 114 | https://www.dgi.gob.ni/FAQ/determinacion_del_iva.htm | 2026-11-14 |
| Read for DGI FAQ, Impuesto al Valor Agregado: form 110 and the end of autotraslacion (Ley 891) | https://www.dgi.gob.ni/FAQ/impuesto_al_valor_agregado_iva.htm | 2026-11-14 |
| Read for Ley 987 (La Gaceta 41, 28 Feb 2019): reformed arts. 127, 130, 131 and 136 | https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf | 2026-11-14 |
| Read for DGI FAQ, Infracciones, sanciones y delitos: CTr arts. 124 and 127 | https://www.dgi.gob.ni/FAQ/infracciones__sanciones_y_deli.htm | 2026-11-14 |

Not yet confirmed: the monthly IVA due date; zero rating of exports and refund of credits; credit and proportionality rules (arts. 112 onward); IVA on services from non-residents; IVA retention by agents; surcharges and the value of the unidad de multa; the full art. 136 list.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nicaragua-iva` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nicaragua-iva. If neither is available, confirm every figure against the official source pages cited above before relying on it.
