---
name: es-income-tax
description: "Use this Guide for 2026 Spanish resident personal income tax in the fifteen common-territory autonomous communities. It computes ordinary employment and self-employment income, general and savings bases, loss offsets, state and regional scales, separate personal and family minima, the employment-income reduction, the 2026 low-pay credit, prepayments and the annual balance. Trigger phrases include IRPF, Modelo 100, autónomo tax, estimación directa, salary income, base del ahorro, mínimo personal, cuota autonómica and regional tax bands. Obtain residence, community, family facts, income schedules and certificates before computing. Regional credits require a separate eligibility schedule; the country README records unfinished coverage. Foral systems, Ceuta/Melilla territorial relief, special incoming-worker elections and módulos calculations need their own verified treatment. No community, method or business-use percentage is assumed."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/es-income-tax"
  jurisdiction: "ES"
  tax_year: "2026"
  last_updated: "2026-10-28"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Spain resident personal income tax (IRPF) v2.3

Calculate resident IRPF from classified income, then apply the state and community scales with their separate personal and family minima. This Guide covers income earned in **calendar year 2026**, returned in 2027 under the campaign rules published for that return. It is sourced from the law; independent whole-pack review is pending and no accountant has signed off this revision.

> **General reference only.** Prepare a computation and evidence schedule for a qualified Spanish reviewer. The country pack remains partial while its regional-credit and territorial gaps are reconciled. A calculation using only the state half is not the taxpayer's full IRPF liability.

## Who this applies to

Use the ordinary resident regime for individuals in the fifteen autonomous communities whose scales appear below. [Ley 35/2006 (LIRPF), arts. 8–9](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a9) taxes resident individuals on worldwide income. Residence follows **more than 183 days** in Spain in the calendar year, counting the statutory sporadic absences, **or** the Spanish main centre/base of activities or economic interests. There is a rebuttable spouse/minor-child family presumption. Exactly 183 days does not meet the day limb but does not settle the other limbs. A Spanish address, nationality or bank account alone does not establish the answer.

Determine the autonomous community under [art. 72](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a72): most days, then the defined main-interest test if days cannot decide, then last declared residence. Apply its anti-avoidance and residence-change rules. Do not select whichever community gives the lowest tax. Establish family unit and individual/joint filing under arts. 82–84 before calculating allowances or reductions.

Navarra and the three Basque foral territories use [their territorial IRPF Guide](es-foral-income-tax.md); they are outside these fifteen common-territory tables. Ceuta/Melilla have separate territorial calculations, including the 2026 Ceuta changes. Non-residents follow IRNR; special incoming-worker elections follow art. 93. An arrival or departure does not create an assumed ordinary split-year return: settle domestic and treaty residence and any exit charge first.

## Rates, bands and thresholds

### State general scale and the two savings halves

The following general scale is **only the state half**, from [LIRPF art. 63](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63). Add the actual community computation, not an assumed duplicate of it.

| General taxable base band, EUR | State marginal rate | Tax year | Official source |
|---|---|---|---|
| 0–12,450 | 9.5% | 2026 | [LIRPF art. 63.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |
| 12,450–20,200 | 12% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |
| 20,200–35,200 | 15% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |
| 35,200–60,000 | 18.5% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |
| 60,000–300,000 | 22.5% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |
| Above 300,000 | 24.5% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a63) |

The published state cumulative taxes at EUR 12,450 / 20,200 / 35,200 / 60,000 / 300,000 are **EUR 1,182.75 / 2,112.75 / 4,362.75 / 8,950.75 / 62,950.75**, respectively (art. 63.1). Use the applicable cumulative amount plus the excess times that band's rate.

| Savings taxable base band, EUR | State half | Regional half | Derived combined rate | Tax year | Source |
|---|---|---|---|---|---|
| 0–6,000 | 9.5% | 9.5% | 19% | 2026 | [LIRPF arts. 66.1, 76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |
| 6,000–50,000 | 10.5% | 10.5% | 21% | 2026 | [Same provisions](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| 50,000–200,000 | 11.5% | 11.5% | 23% | 2026 | [Same provisions](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| 200,000–300,000 | 13.5% | 13.5% | 27% | 2026 | [Same provisions](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| Above 300,000 | 15% | 15% | 30% | 2026 | [Same provisions](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |

The marginal rates are applied only within each band. A withholding scale is not a substitute for these annual tax scales. The state and regional savings **rates** coincide, but the personal/family minimum allocated to each computation can differ.

### Cataluña: regional general scale

Artículo 611-1. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 12500.00 | 9.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 12500.00 | 1187.50 | 9500.00 | 12.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 22000.00 | 2375.00 | 11000.00 | 16.00% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 33000.00 | 4135.00 | 20000.00 | 19.00% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 53000.00 | 7935.00 | 37000.00 | 21.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 90000.00 | 15890.00 | 30000.00 | 23.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 120000.00 | 22940.00 | 55000.00 | 24.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |
| 175000.00 | 36415.00 | No upper limit | 25.50% | 2026 | [Statute, Artículo 611-1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951#a6) |

### Galicia: regional general scale

Artículo 4. Escala autonómica o complementaria del impuesto sobre la renta de las personas físicas. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 12985.35 | 9.00% | 2026 | [Statute, Artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4) |
| 12985.35 | 1168.68 | 8083.25 | 11.65% | 2026 | [Statute, Artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4) |
| 21068.60 | 2110.38 | 14131.40 | 14.90% | 2026 | [Statute, Artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4) |
| 35200.00 | 4215.96 | 24800.00 | 18.40% | 2026 | [Statute, Artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4) |
| 60000.00 | 8779.16 | No upper limit | 22.50% | 2026 | [Statute, Artículo 4](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4) |

### Andalucía: regional general scale

Artículo 23. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 13000.00 | 9.50% | 2026 | [Statute, Artículo 23](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-5) |
| 13000.00 | 1235.00 | 8100.00 | 12.00% | 2026 | [Statute, Artículo 23](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-5) |
| 21100.00 | 2207.00 | 14100.00 | 15.00% | 2026 | [Statute, Artículo 23](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-5) |
| 35200.00 | 4322.00 | 24800.00 | 18.50% | 2026 | [Statute, Artículo 23](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-5) |
| 60000.00 | 8910.00 | No upper limit | 22.50% | 2026 | [Statute, Artículo 23](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-5) |

### Principado de Asturias: regional general scale

Artículo 2. Escala autonómica aplicable a la base liquidable general. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0.00 | 12450.00 | 9.00% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 12450.00 | 1120.50 | 5257.20 | 12.00% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 17707.20 | 1751.36 | 15300.00 | 14.00% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 33007.20 | 3893.36 | 20400.00 | 19.20% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 53407.20 | 7810.16 | 16592.80 | 21.50% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 70000.00 | 11377.62 | 20000.00 | 22.50% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 90000.00 | 15877.62 | 85000.00 | 25.00% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |
| 175000.00 | 37127.62 | No upper limit | 26.00% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2) |

### Cantabria: regional general scale

Artículo 1. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 13000.00 | 8.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |
| 13000.00 | 1105.00 | 8000.00 | 11.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |
| 21000.00 | 1985.00 | 14200.00 | 14.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |
| 35200.00 | 4044.00 | 24800.00 | 18.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |
| 60000.00 | 8508.00 | 30000.00 | 22.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |
| 90000.00 | 15258.00 | No upper limit | 24.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028#a1) |

### La Rioja: regional general scale

Artículo 31. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 12450.00 | 8.00% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 12450.00 | 996.00 | 7750.00 | 10.60% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 20200.00 | 1817.50 | 15000.00 | 13.60% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 35200.00 | 3857.50 | 4800.00 | 17.80% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 40000.00 | 4711.90 | 10000.00 | 18.30% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 50000.00 | 6541.90 | 10000.00 | 19.00% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 60000.00 | 8441.90 | 60000.00 | 24.50% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |
| 120000.00 | 23141.90 | No upper limit | 27.00% | 2026 | [Statute, Artículo 31](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-3) |

### Región de Murcia: regional general scale

Artículo 2. Tarifa autonómica. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 12450.00 | 9.50% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542#a2) |
| 12450.00 | 1182.75 | 7750.00 | 11.20% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542#a2) |
| 20200.00 | 2050.75 | 13800.00 | 13.30% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542#a2) |
| 34000.00 | 3886.15 | 26000.00 | 17.90% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542#a2) |
| 60000.00 | 8540.15 | No upper limit | 22.50% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542#a2) |

### Comunitat Valenciana: regional general scale

Artículo 2. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 12000 | 8.8% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 12000 | 1056 | 10000 | 11.7% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 22000 | 2226 | 10000 | 14.6% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 32000 | 3686 | 10000 | 17% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 42000 | 5386 | 10000 | 19.4% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 52000 | 7326 | 10000 | 21.9% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 62000 | 9516 | 10000 | 24.4% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 72000 | 11956 | 28000 | 26.1% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 100000 | 19264 | 50000 | 27.35% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 150000 | 32939 | 50000 | 28.35% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |
| 200000 | 47114 | No upper limit | 29.35% | 2026 | [Statute, Artículo 2](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2) |

### Aragón: regional general scale

Artículo 110-1. Escala autonómica del impuesto. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 13072.50 | 9.50% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 13072.50 | 1241.89 | 8137.50 | 12.00% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 21210.00 | 2218.39 | 15750.00 | 15.00% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 36960.00 | 4580.89 | 15540.00 | 18.50% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 52500.00 | 7455.79 | 7500.00 | 20.50% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 60000.00 | 8993.29 | 20000.00 | 23.00% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 80000.00 | 13593.29 | 10000.00 | 24.00% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 90000.00 | 15993.29 | 40000.00 | 25.00% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |
| 130000.00 | 25993.29 | No upper limit | 25.50% | 2026 | [Statute, Artículo 110-1](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006#a1) |

### Castilla-La Mancha: regional general scale

Artículo 13 bis. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 12450.00 | 9.50% | 2026 | [Statute, Artículo 13 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a13bis) |
| 12450.00 | 1182.75 | 7750.00 | 12.00% | 2026 | [Statute, Artículo 13 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a13bis) |
| 20200.00 | 2112.75 | 15000.00 | 15.00% | 2026 | [Statute, Artículo 13 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a13bis) |
| 35200.00 | 4362.75 | 24800.00 | 18.50% | 2026 | [Statute, Artículo 13 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a13bis) |
| 60000.00 | 8950.75 | No upper limit | 22.50% | 2026 | [Statute, Artículo 13 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368#a13bis) |

### Canarias: regional general scale

Artículo 18 bis. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 13748.00 | 9.00% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 13748.00 | 1237.32 | 5674.00 | 11.50% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 19422.00 | 1889.83 | 16502.00 | 14.00% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 35924.00 | 4200.11 | 21642.00 | 18.50% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 57566.00 | 8203.88 | 35702.00 | 23.50% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 93268.00 | 16593.85 | 30477.00 | 25.00% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |
| 123745.00 | 24213.1 | No upper limit | 26.00% | 2026 | [Statute, Artículo 18 bis](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a18bis) |

### Extremadura: regional general scale

Artículo 1. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 12450.00 | 7.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 12450.00 | 964.88 | 7750.00 | 9.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 20200.00 | 1720.50 | 4000.00 | 16.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 24200.00 | 2360.50 | 11000.00 | 17.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 35200.00 | 4285.50 | 24800.00 | 21.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 60000.00 | 9493.50 | 20200.00 | 23.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 80200.00 | 14240.50 | 19000.00 | 24.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 99200.00 | 18800.50 | 21000.00 | 24.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |
| 120200.00 | 23945.50 | No upper limit | 25.00% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159#a1) |

### Illes Balears: regional general scale

Artículo 1. Escala autonómica del impuesto aplicable a la base liquidable general. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 10000 | 9% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 10000 | 900 | 8000 | 11.25% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 18000 | 1800 | 12000 | 14.25% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 30000 | 3510 | 18000 | 17.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 48000 | 6660 | 22000 | 19% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 70000 | 10840 | 20000 | 21.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 90000 | 15190 | 30000 | 22.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 120000 | 22015 | 55000 | 23.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |
| 175000 | 35077.50 | No upper limit | 24.75% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a1) |

### Madrid: regional general scale

Artículo 1. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0 | 0 | 13362.22 | 8.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) |
| 13362.22 | 1135.79 | 5642.41 | 10.70% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) |
| 19004.63 | 1739.53 | 16421.05 | 12.80% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) |
| 35425.68 | 3841.42 | 21894.72 | 17.40% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) |
| 57320.40 | 7651.10 | No upper limit | 20.50% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a1) |

### Castilla y León: regional general scale

Artículo 1. Escala autonómica. All amounts are EUR; the width is the amount in the next band, not its absolute upper boundary.

| Base from | Tax at that base | Next band width | Marginal rate | Tax year | Official source |
|---|---|---|---|---|---|
| 0.00 | 0.00 | 12450.00 | 9.0% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254#a1) |
| 12450.00 | 1120.5 | 7750.00 | 12.0% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254#a1) |
| 20200.00 | 2050.5 | 15000.00 | 14.0% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254#a1) |
| 35200.00 | 4150.5 | 18207.20 | 18.5% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254#a1) |
| 53407.20 | 7518.83 | No upper limit | 21.5% | 2026 | [Statute, Artículo 1](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254#a1) |

### Other ordinary computation thresholds

| Item | Amount or test | Tax year | Source |
|---|---|---|---|
| Ordinary employment other-expense allowance | EUR 2,000, limited by the specified remaining employment income | 2026 | [LIRPF art. 19.2.f](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a19) |
| Employment reduction eligibility | Statutory net employment income below EUR 19,747.50 and other non-exempt income no more than EUR 6,500 | 2026 | [LIRPF art. 20](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a20) |
| 2026 low-pay credit eligibility | Qualifying gross employment income below EUR 20,048.45 and other non-exempt income no more than EUR 6,500 | 2026 | [LIRPF DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-15) |
| Simplified direct assessment | Prior-year combined activity turnover no more than EUR 600,000, with annualisation and method conditions | 2026 | [RD 439/2007 (RIRPF) art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a28) |
| Simplified provisions/hard-to-justify expense | Ordinarily 5%; qualifying 2026 Ceuta activity 10%. Annual combined cap EUR 2,000 | 2026 | [RIRPF art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a30) |
| General direct-assessment instalment rate | 20% of year-to-date net activity income, before the prescribed credits/adjustments | 2026 | [RIRPF art. 110](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a110) |
| Professional invoice withholding | Normally 15%; eligible start year and next two years 7%, subject to written notice and prior-activity conditions | 2026 | [RIRPF art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a95) |
| Professional instalment exemption | At least 70% of the activity's previous-year income subject to withholding; use the covered period for a start-year test | 2026 | [RIRPF art. 109](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a109) |

## The base

### 1. Classify and reconcile all income

Reconcile certificates, invoices, asset schedules, foreign income, bank gross amounts and tax prepayments. Salary, pensions and other art. 17 income are employment; a genuine organised business/profession is an activity under art. 27. Net property rents, savings income and disposal gains each need their own category computation. Use the rental, capital-gains and crypto siblings only after checking their tax year and source status. Bank transfers between owned accounts are not new taxable income merely because they appear as a credit; a processor's net payout does not remove its gross revenue or separately recorded fee. Withholding and instalments are prepayments, not deductible activity expenses.

Build the **general base** under arts. 45 and 48 and the **savings base** under arts. 46 and 49. In the savings base, net investment income and disposal gains/losses are separate baskets. A negative basket can offset at most **25%** of the other positive basket; carry the remaining eligible loss for **four following years**, preserving its source year and using the statutory maximum available each year. General-base non-disposal losses have their own art. 48 25% and four-year rules. Do not net a share-sale loss directly against salary. Wash-sale, exempt and other loss-denial rules still apply before a loss reaches either basket.

### 2. Compute ordinary employee income

### Foreign-work salary exemption: ordinary resident employee

Apply **LIRPF7(p) and RIRPF6 before calculating taxable employee income**. Establish ordinary IRPF residence and the competent common territory first. This is employment actually performed outside Spain for a non-Spanish-resident enterprise/entity or an overseas permanent establishment. A foreign payer or customer alone does not exempt work performed from Spain. A Spanish employer can pay the salary: identify the foreign recipient/beneficiary of the actual services. For a related recipient, substantiate an intragroup service producing or capable of producing an advantage or utility to that recipient under current LIS18.5; group membership or a trip alone does not establish that benefit. This worksheet covers an ordinary employee; it does not establish a director's, international-official's or other special-status claimant's entitlement. [LIRPF7(p)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764); [RIRPF6/9A3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820); [LIS18.5](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328).

The work territory must apply an income tax identical or analogous to IRPF and satisfy the noncooperative-jurisdiction condition. The comparable-tax condition is deemed satisfied where Spain has a double-tax treaty containing an information-exchange clause; actual foreign withholding is not itself a prerequisite to this exemption. Without that treaty, substantiate the analogous tax and the jurisdiction's status. Read the applicable-period list, not merely the newest displayed list: current OrderHFP/115/2023 includes dated2026 amendments whose application to taxes with a tax period depends on when that period begins. The statutory references to tax havens are read through Ley36/2006 DA10's noncooperative-jurisdiction definition. [OrderHFP/115/2023 current list and effect notes](https://www.boe.es/buscar/act.php?id=BOE-A-2023-3508); [Ley36/2006 DA10](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20843); [AEAT2025 foreign-work method](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c02-irpf-cuestiones-generales/sujecion-irpf-aspectos-materiales/delimitacion-negativa-hecho-imponible-rentas-sujetas/rentas-exentas-articulo-7-ley-irpf/rendimientos-trabajo-percibidos-trabajos-efectivamente-realizados.html).

Keep a schedule for **each employment relationship/payer j**: `N_j` is non-specific remuneration actually earned in that relationship in the tax year, excluding the separately identified foreign-service remuneration `S_j`; `D_j` is the number of qualifying days abroad in that relationship; and `T_j` is its calendar-day duration in that tax year. For a relationship lasting all2026 use **365**, not working days. For a shorter relationship use its actual duration, not365. Calculate separately for each payer in whose relationship the qualifying assignment occurred; do not import salary or unemployment benefits from unrelated non-assignment payers. This is the TEAC19July2024 RG00/08685/2023 correction expressly incorporated in AEAT's2025 manual, applied here against the unchanged current statutory/regulatory method. Include evidenced outbound/return travel days for the qualifying assignment, as the manual explains; a private holiday abroad or remote work in Spain is not automatically a qualifying service day. [TEAC19July2024, operative unified criterion](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00/08685/2023/00/0/1); [AEAT2025 foreign-work method](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c02-irpf-cuestiones-generales/sujecion-irpf-aspectos-materiales/delimitacion-negativa-hecho-imponible-rentas-sujetas/rentas-exentas-articulo-7-ley-irpf/rendimientos-trabajo-percibidos-trabajos-efectivamente-realizados.html).

`eligible_foreign_salary = sum(S_j + N_j × D_j/T_j)` across qualifying relationships; `exempt_7p = min(60,100, eligible_foreign_salary)` for the taxpayer's **whole year**, not60,100 per payer, country or trip. Specific remuneration is added once and is not multiplied by the day fraction again. The annual cap is not itself prorated to assignment days. Reconcile `taxable_gross_employment = total_otherwise_taxable_gross_employment − exempt_7p`, retaining salary from Spain, ineligible assignments and the excess over the annual cap. Then apply the ordinary employee-expense/reduction rules below to the nonexempt computation; this formula does not independently establish an expense allocation or another exemption. It does not turn7(p) income into exempt-with-progression income merely because it is foreign. [LIRPF7(p)](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764); [RIRPF6/9A3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820); [TEAC19July2024, operative unified criterion](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00/08685/2023/00/0/1).

For a fully evidenced2026 full-year relationship, nonspecific salary36,500, specific foreign premium2,000 and45 qualifying foreign days produce `2,000 + 36,500 ×45/365 = 6,500` exempt; taxable gross is32,000 out of38,500 before employee expenses. A184-day relationship paying18,400 nonspecific salary and3,000 specific remuneration, with46 qualifying days, produces `3,000 + 18,400 ×46/184 = 7,600` exempt and13,800 taxable gross. Using365 in that second denominator would incorrectly produce5,318.90. For two qualifying successive payers,27,300 over273days/39foreigndays and18,400 over92days/36foreigndays produce3,900 +7,200 =11,100 exempt, subject to the one shared cap. A third payer with no qualifying assignment contributes no amount to that exemption calculation. These are declared-input salary controls, not residence or final-quota determinations. [TEAC19July2024, operative unified criterion](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00/08685/2023/00/0/1); [RIRPF6/9A3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820).

For employees assigned abroad,7(p) is **incompatible with the RIRPF9.A.3(b) expatriate-excess regime regardless of amount**; the taxpayer can select the excess regime instead. Do not apply both to the same year's assignment computation. Separately qualifying ordinary travel/subsistence reimbursements under9.A.3(a) remain a different exemption, subject to their own evidence/limits; remove them from the salary worksheet rather than exempt them twice. Under art80, foreign-tax relief concerns income remaining included and taxed in Spain: identify foreign tax actually attributable to that residual taxable foreign income and cap it by the Spanish effective-rate charge on its corresponding taxable foreign base. Do not credit tax on the7(p)-exempt slice again, claim a credit solely because the foreign country charged something, or use gross salary as the Spanish taxable-base ceiling. If all the foreign salary is exempt, its Spanish art80 ceiling is zero. If80,000 of otherwise taxable foreign salary is wholly eligible,7(p) exempts60,100 and19,900 remains gross taxable; a separately evidenced1,990 foreign tax on the residual and4,975 Spanish art80 ceiling gives1,990 credit, not a credit for the tax on all80,000. Reconcile treaty limits and actual expense/base allocation before fixing that ceiling. [RIRPF6/9A3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820); [LIRPF80](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764); [AEAT2025 foreign-work method](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c02-irpf-cuestiones-generales/sujecion-irpf-aspectos-materiales/delimitacion-negativa-hecho-imponible-rentas-sujetas/rentas-exentas-articulo-7-ley-irpf/rendimientos-trabajo-percibidos-trabajos-efectivamente-realizados.html).

[LIRPF arts. 17–20](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a19) start with gross cash and taxable benefits, after any verified exemption or qualifying irregular-income treatment. Deduct actual employee Social Security, eligible passive-rights/orphan contributions, eligible union/mandatory-professional dues and employment-litigation costs; the last have a **EUR 300** annual ceiling. The separate art. 19.2.f allowance is **EUR 2,000**, with the statutory cap. Qualifying employment-related relocation adds **EUR 2,000** in the move year and next year; qualifying active-worker disability adds **EUR 3,500**, or **EUR 7,750** in the specified higher-need/disability cases. Obtain the evidence rather than granting every supplement to every employee.

For **art. 20**, define `R` as gross employment income less **art. 19.2.a–e expenses only**. Do **not** subtract the art. 19.2.f EUR 2,000 allowance before testing the reduction:

| Statutory R, EUR, with other-income condition met | Employment reduction | Tax year | Source |
|---|---|---|---|
| R ≤ 14,852 | EUR 7,302 | 2026 | [LIRPF art. 20.a](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a20) |
| 14,852 < R ≤ 17,673.52 | 7,302 − 1.75 × (R − 14,852) | 2026 | [LIRPF art. 20.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a20) |
| 17,673.52 < R < 19,747.50 | 2,364.34 − 1.14 × (R − 17,673.52) | 2026 | [LIRPF art. 20.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a20) |

The reduction is unavailable if other non-exempt income exceeds **EUR 6,500**. Apply it without making the resulting employment amount negative. Keep its eligibility R separate from the actual employment amount after all allowed art. 19 expenses.

The **2026 low-pay credit in DA 61** is a tax-credit step, not a replacement employment deduction. For qualifying wages from actual employment/statutory service, define `G` as the article's **gross** employment amount. If G ≤ **EUR 17,094**, the nominal credit is **EUR 590.89**. For 17,094 < G < **20,048.45**, it is `590.89 − 0.2 × (G − 17,094)`. Other non-exempt income must not exceed **EUR 6,500**. Cap it at the stated proportion of state-plus-regional gross tax attributable to that net employment income. Deduct it at the DA 61.2 position after art. 80 foreign-tax relief; it is not automatically refundable beyond tax. The 2026 thresholds differ from the earlier 2025 rule ([DA 61, as amended from 1 January 2026](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-15)).

### 3. Compute self-employment income under the actual method

Confirm normal, simplified or objective assessment. For simplified direct assessment, prior-year combined activity turnover must not exceed **EUR 600,000**, annualised where the prior activity lasted less than a year, with the art. 28 conditions and art. 29 election/exclusion rules. Do not assume simplified assessment when the method is unknown. Objective-assessment módulos have their own activity-specific computation and annual order; they are not obtained by applying 5% to accounting profit. The [instalment Guide](es-estimated-tax.md#objective-method-entry-limits-ordinary-text-and-the-published-2026-route) supplies the published 2026 AEAT entry limits and preserved election routes after non-convalidation, with the lower statutory baseline and remaining legal-reconciliation boundary. Check eligibility before using a module worksheet; the actual activity-specific computation remains separate.

Under [LIRPF arts. 28–30](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30), reconcile gross activity income, evidenced deductible business expenses and tax depreciation. Deduct the taxpayer's eligible own social contributions. Include costs on the correct tax basis: recoverable input VAT is excluded, while irrecoverable VAT is not erased merely because the taxpayer is registered. Taxes paid as IRPF prepayments, loan principal and owner drawings are not ordinary activity expenses.

| Special direct-assessment expense | Rule | Tax year | Source |
|---|---|---|---|
| Main-home supplies | Normally 30% × separately evidenced business floor-area fraction × qualifying supplies; a higher or lower substantiated percentage replaces that default | 2026 | [LIRPF art. 30.2.5.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30) |
| Taxpayer's own working meals | Business purpose, restaurant/hospitality establishment and electronic payment; actual cost within the applicable daily limit | 2026 | [LIRPF art. 30.2.5.c](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30) |
| Meal daily limits, without overnight / with qualifying overnight | Spain EUR 26.67 / EUR 53.34; abroad EUR 48.08 / EUR 91.35 | 2026 | [RIRPF art. 9.A.3.a, read with LIRPF art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a9) |
| Eligible health insurance | EUR 500 per covered taxpayer/spouse/cohabiting child under 25, or EUR 1,500 for a covered person with disability | 2026 | [LIRPF art. 30.2.5.a](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a30) |

Asset business use follows [RIRPF art. 22](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a22). Partial allocation requires a part capable of separate independent use; an indivisible asset is not automatically deductible in a chosen private/business percentage. The incidental-private-use rule excludes ordinary passenger vehicles, with the specific goods-transport, paid passenger transport, driving instruction, commercial-agent and hire exceptions. **Do not import a VAT 50% vehicle presumption into IRPF.** Obtain the asset and use evidence before deducting it.

For simplified assessment, the official linear depreciation table uses maximum rate/maximum years of: buildings **3%/68**; installations, furniture and other tangible assets **10%/20**; machinery **12%/18**; transport **16%/14**; information equipment and software **26%/10**; tools **30%/8**; specified livestock **16%/14**; horses/non-citrus fruit trees **8%/25**; citrus/vines **4%/50**; olive groves **2%/100**. Apply date and qualifying ERD depreciation provisions where relevant. Source: [RIRPF art. 30.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a30), [AEAT official simplified table](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html). Normal direct assessment uses its applicable corporate-tax depreciation rules instead; do not swap the tables silently.

In simplified assessment, deduct `min(2,000, 5% × positive qualifying net income before this item)` for provisions and hard-to-justify expenses **together**, not EUR 2,000 for each. It is incompatible with the elected art. 32.2.1/RIRPF art. 26.1 reduction. In 2026, eligible Ceuta activity instead has **10%**, while the EUR 2,000 cap remains; DA 64 has its own instalment-effective-date rule. This does not extend the special rate to every Melilla or mainland taxpayer ([RIRPF art. 30](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a30); [LIRPF DA 64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18)).

Test the separate [art. 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a32) reductions rather than assuming none. The qualifying single-unrelated-client/economically-dependent route starts with **EUR 2,000**. Its conditions include direct assessment, one unrelated client or a qualifying TRADE relationship with an unrelated dependent client, deductible expenses no more than **30% of gross declared income**, required formal obligations, no employment income apart from the permitted up-to-**EUR 4,000** unemployment/art. 17.2.a benefit exception, at least **70%** of income withheld, and no income-attribution-entity activity. It is incompatible with the simplified provisions/5% item. Subject to other non-exempt income no more than **EUR 6,500**, the additional reduction is **EUR 6,498** where eligible net activity income is at most **EUR 14,047.50**, then `6,498 − 1.14 × (net activity income − 14,047.50)` up to **EUR 19,747.50**. Qualifying active disability adds **EUR 3,500**, or **EUR 7,750** in the stated higher-need cases. Do not make net income negative. Where that route does not apply, art. 32.2.3 gives **EUR 1,620** at non-exempt income up to **EUR 8,000**, tapering by **0.405** per euro above EUR 8,000 to **EUR 12,000**, with the **EUR 3,700** combined employment-reduction cap. A qualifying new activity can reduce eligible positive net income by **20%** in the first positive year and next year, on no more than **EUR 100,000**; the prior-activity and former-employer-income exclusions must hold. Do not equate first registration with eligibility.

### 4. Build taxable bases and family schedules

After category netting, apply the statutory base reductions in their prescribed order, without manufacturing a negative base. The ordinary pension-reduction limit is the lower of **30%** of eligible net employment/activity income and **EUR 1,500**. Employer-linked and qualifying self-employed employment-plan additions have distinct **EUR 8,500/EUR 4,250** conditions and interaction; the specified incremental combined ceiling is EUR 8,500. Carry qualifying unused reduction under the **five-year** rule, not every excess contribution automatically ([LIRPF arts. 50–52](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52)).

Joint family filing is an actual election under arts. 82–84. The married-couple family reduction is **EUR 3,400**; the eligible other family-unit reduction is **EUR 2,150**, unavailable where the taxpayer cohabits with the other parent as art. 84 specifies. Apply first against the general base, then the permitted savings remainder. The basic taxpayer minimum is not multiplied by the number of adults in a joint return; age/disability and descendant rules are separate.

**State minimum amounts.** Determine eligibility under arts. 57–61 before summing amounts:

| Component | Annual amount, EUR | Tax year | Official source |
|---|---|---|---|
| Taxpayer | 5,550; add 1,150 when over 65, then another 1,400 when over 75 | 2026 | [LIRPF art. 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a57) |
| Eligible descendants, in order | 2,400 / 2,700 / 4,000 / 4,500 for fourth and each later | 2026 | [LIRPF art. 58](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a58) |
| Eligible descendant under three | Add 2,800; adoption/foster placement has its own three-period rule | 2026 | [LIRPF art. 58.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a58) |
| Eligible ascendant | 1,150; add 1,400 over 75 | 2026 | [LIRPF art. 59](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a59) |
| Qualifying disability of taxpayer/eligible relative | 3,000, or 9,000 from 65% disability; add 3,000 qualifying assistance amount | 2026 | [LIRPF art. 60](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a60) |

Descendants normally must be under **25**, or disabled at any age, and meet cohabitation/dependency and income conditions. The relative's non-exempt annual income must not exceed **EUR 8,000**; their own IRPF return with income **over EUR 1,800** can deny the minimum. Apply shared entitlement, closer-degree, tax-accrual-date, death and ascendant-half-period cohabitation rules in art. 61. Exactly EUR 8,000 is not above that limit. Qualifying disability ordinarily requires at least **33%**, with the statutory pension/recognition rules in art. 60.3. It is not inferred from a medical expense.

**Regional minima replace only the regional amounts.** The following personal amounts are **total personal minima** at ages ≤65 / over65 / over75, not amounts all added together. Descendant columns give first/second/third/fourth-and-later, plus the separate under-three addition. Ascendant and disability conditions continue to apply.

| Region or profile | Personal totals, EUR | Descendants and under-three addition, EUR | Ascendant base and over75 addition, EUR | Disability ordinary / at least65% / assistance, EUR | 2026 official rule |
|---|---|---|---|---|---|
| State profile; Cataluña, Cantabria, Murcia, Aragón, Castilla-La Mancha, Extremadura and Castilla y León | 5,550 / 6,700 / 8,100 | 2,400 / 2,700 / 4,000 / 4,500; +2,800 | 1,150; +1,400 | 3,000 / 9,000 / +3,000 | [LIRPF arts. 56–61](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a56); regional statutes listed in Sources |
| Galicia | 5,789 / 6,988 / 8,448 | 2,503 / 2,816 / 4,172 / 4,694; +2,920 | 1,199; +1,460 | 3,129 / 9,387 / +3,129 | [D.Leg. 1/2011 art. 4 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161#a4-2) |
| Andalucía | 5,790 / 6,990 / 8,450 | 2,510 / 2,820 / 4,170 / 4,700; +2,920 | 1,200; +1,460 | 3,130 / 9,390 / +3,130 | [Ley 5/2021 art. 23 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915#a2-12) |
| Asturias | 6,105 / 7,370 / 8,910 | 2,640 / 2,970 / 4,400 / 4,950; +3,080 | 1,265; +1,540 | 3,300 / 9,900 / +3,300 | [D.Leg. 2/2014 arts. 2 bis–2 quinquies](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945#a2-2) |
| Comunitat Valenciana | 6,105 / 7,370 / 8,910 | 2,640 / 2,970 / 4,400 / 4,950; +3,080 | 1,265; +1,540 | 3,300 / 9,900 / +3,300 | [Ley 13/1997 art. 2 bis](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202#a2-2) |
| Canarias | 5,606 / 6,768 / 8,182 | 2,424 / 2,727 / 4,040 / 4,545; +2,828 | 1,162; +1,414 | 3,030 / 9,090 / +3,030 | [D.Leg. 1/2009 art. 18 quater](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008#a1-11) |
| Illes Balears | 5,550 / 7,370 / 8,910 | 2,400 / 2,970 / 4,400 / 4,950; +2,800 | 1,265; +1,540 | 3,300 / 9,900 / +3,300 | [D.Leg. 1/2014 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925#a2) |
| Madrid | 5,956.65 / 7,190.91 / 8,693.49 | 2,575.85 / 2,897.83 / 4,400 / 4,950; +3,005.16 | 1,234.26; +1,502.58 | 3,219.81 / 9,659.44 / +3,219.81 | [D.Leg. 1/2010 arts. 2–2 quater](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068#a2) |
| La Rioja | State personal, descendant and ascendant profile | State ordinary descendant profile | State profile | **Disabled descendants only:** 3,300 / 9,900; assistance remains +3,000. Other disability minima stay at state amounts | [Ley 10/2017 art. 31 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750#a3-12) |

For Illes Balears, the enhanced over65 personal minimum is **1.10 × (5,550 + 1,150) = 7,370**; it is not 5,550 plus only an enhanced age increment. The under65 personal minimum, first-child amount and under-three addition are not all increased by 10%. La Rioja's disability-descendant increase does not increase the assistance amount. A general “use state minima in every community” rule is incorrect.

### Pension reductions: employer and self-employed increments

Under [LIRPF arts. 51–52](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52), first classify each paid/imputed contribution by instrument, payer and beneficiary. A deductible alternative-mutual contribution already used as an activity expense cannot also reduce the general base. The ordinary reduction is subject to both available general base and the lower of **30% of individual net employment/activity income** and the applicable annual monetary ceiling. The **1,500** ordinary ceiling is shared across eligible instruments, not repeated for each plan.

The **8,500 employer-linked increment** requires actual employer contributions or qualifying employee contributions to the **same** employment instrument. For annual employer contribution `E`, the employee contribution eligible for that increment is no more than:

| Employer contribution E | Employee amount eligible for the increment | Tax year | Official source |
|---|---|---|---|
| E at most 500 | 2.5 × E | 2026 | [LIRPF art. 52.1.b.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52) |
| E from 500.01 to 1,500 | 1,250 + 0.25 × (E − 500) | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52) |
| E above 1,500 | E | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52) |
| Gross employment income from that contributing employer above 60,000 | E, overriding the enhanced multipliers | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52) |

Employer amounts resulting from an employee's own decision count as **employee contributions**, so salary sacrifice cannot manufacture the employer multiplier. Employee amounts outside the increment's conditions can only use ordinary capacity if otherwise eligible. Track actual employer and employee totals; the increment is an upper limit, not an automatic extra deduction.

The **4,250 self-employed increment** is confined to the statutory sectoral/simplified employment plans joined through the activity and the specified own-promoter employment plans, mutual arrangements, business social-prevision plans or collective-dependency insurance. An ordinary personal pension plan does not become a qualifying self-employed employment plan because its holder is an autónomo. Combined use of the employer and self-employed increments cannot exceed **8,500**; the ordinary 1,500 sits outside that combined increment. Employer-paid collective-dependency premiums have their separate additional **5,000** limit. Apply the applicable income/base limits and instrument conditions before granting any reduction ([art. 52.1](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a52)).

Keep oldest eligible carry first under the regulatory ordering and expiry rules. Article 52.2 permits **five following years** for contributions not reduced because of insufficient base or the percentage limit, including qualifying imputed employer amounts; it does **not** cure contributions exceeding the legal contribution ceiling. Claim and identify the carry in the prescribed return. For contributions to an eligible spouse's plan, the additional art. 51.7 limit is **1,000**, only where the spouse's net employment/activity income is **below 8,000**, including nil; exactly 8,000 fails that gateway. It is not a transfer of unused ordinary pension capacity.

The disability-plan route under [art. 53](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a53) is distinct: eligible disability/relationship conditions, own contributions at most **24,250**, qualifying other contributor at most **10,000**, and combined **24,250 per beneficiary**. Give the beneficiary's own contributions priority and prorate the remaining permitted amount across other contributors. Its insufficient-base carry is **five years**. A protected-property contribution under [art. 54](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a54) instead has **10,000 per contributor**, combined **24,250**, proportional sharing and **four-year** carry for excess/insufficient-base amounts; apply older balances first. The beneficiary's own contribution and business-affected assets do not qualify. A disposal in the contribution year or following **four years** can trigger the specified contributor/beneficiary recapture with interest, subject to the statutory death exception. Do not interchange the two regimes' carry periods.

### 5. Apply each scale to its own base and minimum

For the ordinary case without special annuity or exempt-income progression rules, define `S(x)` as the state general-scale tax on non-negative x, `A(x)` as the selected community scale, and `H(x)` as one savings-half scale. Use the statutory cumulative quota plus excess × marginal rate at the applicable band.

- State general tax: `S(Bg) − S(min(Bg, Ms))`.
- Regional general tax: `A(Bg) − A(min(Bg, Ma))`.
- State savings tax: `H(Bs) − H(min(Bs, max(0, Ms − Bg)))`.
- Regional savings tax: `H(Bs) − H(min(Bs, max(0, Ma − Bg)))`.

Here Bg/Bs are the relevant general/savings taxable bases and Ms/Ma are the independently computed state/regional personal-family minima. A minimum is **not** deducted from income at the taxpayer's highest marginal rate. Carry its unused part to savings only as art. 56.2 allows. Keep state and regional liabilities separate for their credit limits; annuities under arts. 64/75, exempt-income progression and special elections require their own computations.

Apply eligible state and regional tax credits with their own conditions and available-tax limits. Use [es-irpf-deductions](es-irpf-deductions.md) for national startup subscriptions, donations, legacy home/rental relief, reinvestment, energy/EV/self-consumption credits and the fifteen regional catalogues. Keep state-only, shared national and regional quota credits separate; calculate maternity/childcare and large-family/disability credits at their refundable differential positions, adding back actual advance receipts. That Guide supplies the monthly entitlement, contribution and expense limits, cession and home-grandfathering calculations; its pending list and the country README identify remaining interactions. Do not claim an unreconciled 2025 regional amount as a 2026 credit. Compute the art. 80 foreign-tax credit and the DA 61 credit in their proper order, then the statutory differential and eligible refundable-family-credit adjustments. Credit documented withholding and instalments. A negative balance from excess eligible prepayments is a refund, not a negative marginal tax rate.

The national habitual-home rental credit in current art. 68.6 is deducted entirely from the state half under art. 67.1.a. RDL 29/2026 makes that amendment effective on 8 October 2026; it is distinct from regional rental relief and the old DT 15 rental transition. Use the verified formula and property-ownership test in [es-irpf-deductions](es-irpf-deductions.md), and do not stack the old national transition for the same home and period ([RDL 29/2026 art. 6.Segundo.Tres–Cuatro/Trece](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823)).

### Child-support annuities and exempt income with progression

For [arts. 64 and 75](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a64), establish child support within art. 7.k, actually paid under its qualifying judicial or legally recognised agreement route, **no entitlement to the descendant minimum for that child**, and qualifying annual support `C` **below** general taxable base `Bg`. Voluntary transfers do not establish eligibility. Do not deduct child support from the base under the spouse-maintenance rule in art. 55.

Using the state/regional scales `S/A` defined above and the independently established minima `Ms/Ma`, calculate:

- State general quota: `max(0, S(C) + S(Bg − C) − S(min(Bg, Ms + 1,980)))`.
- Regional general quota: `max(0, A(C) + A(Bg − C) − A(min(Bg, Ma + 1,980)))`.

The **1,980** increases the minimum used for this tax calculation; it is not a cash credit or another expense. Preserve the separate savings calculation and the statutory art. 56 allocation of personal/family minima. The special split requires `C < Bg`; do not extend it to equality or negative remaining base, or claim both the same child's descendant minimum and this split. Record support for multiple children separately before aggregating the qualifying payments.

Only income actually **exempt with progression** under the applicable treaty/statute enters [DA 20](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#davigesima). Classify it as general or savings by its nature. For general exempt income `Eg`, form `Tg = Bg + Eg`; calculate the state and regional ordinary scale quotas on Tg, less each scale's tax on the applicable minimum allocated to that enlarged general base. Divide each resulting quota by Tg, retain the independently computed average rate and apply it to **Bg alone**. Do not directly tax Eg or use the taxpayer's marginal band as the average rate. If Tg is zero, there is no general rate to divide by. Allocate any minimum not absorbed by the enlarged general base to savings under the statutory rules.

For savings exempt income `Es`, similarly use `Ts = Bs + Es` for each half's savings scale and subtract the tax on that half's applicable residual minimum, then apply its average percentage to **Bs alone**. Keep each half separate and do not use exempt general income to increase the savings rate or vice versa. The [AEAT general-progression workpaper](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/rentas-exentas-progresividad/tratamiento-liquidatorio-rentas-exentas-progresividad-big.html) demonstrates the enlarged-base/average-rate order under unchanged DA 20. Its printed regional rate of 9.23% for 2,475/26,800 differs from ordinary rounding to 9.24%; DA 20 itself supplies no decimal convention. Retain precision in the legal computation and reconcile the displayed rate and final cents to the approved return engine; the final 2026 engine is not yet available. The combined worksheet below supplies the simultaneous support-annuity/progression sequence.

### Simultaneous child support and exempt income with progression

Apply both methods in one worksheet. First establish the arts.64/75 conditions above, including qualifying support `C < Bg` using the actual general liquidable base, not the artificially enlarged rate-setting base. For legally established general exempt-with-progression income `Eg`, set `Tg=Bg+Eg`. The full-minimum formulas below cover the branch where the **actual** general BL absorbs the augmented minimum in each half: `Bg >= Ms + 1,980` and `Bg >= Ma + 1,980`. The official worksheet establishes this condition before using the full augmented minima. In that branch, apply each half's general scale separately to `C` and `Tg−C`, subtract that half's scale tax on its full augmented minimum, and stop at zero:

- `QE_aug = max(0,S(C)+S(Tg−C)−S(Ms+1980))`.
- `QA_aug = max(0,A(C)+A(Tg−C)−A(Ma+1980))`.
- IfTg>0, `rE=100×QE_aug/Tg` and `rA=100×QA_aug/Tg`; apply those separate general average percentages to **Bg alone**. Keep the statutory two-decimal expression and the rate-display reservation above; do not invent a rounding rule from this worksheet.

If either actual-base absorption condition fails, this worksheet does not establish the general/savings allocation for that half. Determine it under art. 56 together with arts. 64/75 and DA 20 before calculating the affected rate or savings tax. Do not treat `min(Tg,M+1980)` alone as a verified allocation rule, or carry the special 1,980 increment into savings. This scope limit does not mean the annuity relief fails; its eligibility remains the separate `C < Bg` test.

This order preserves the annuity split while including exempt income only for rate-setting. It does not compute two competing final taxes and select the lower one, deduct support as an expense, or apply an average rate to the exempt amount. Continue the separate savings calculation, using the actual personal/family-minimum allocation under art.56 and DA20; the special1,980 annuity increment is not a new minimum carried to savings. If the actualC<Bg condition fails, use the ordinary progression method without the annuity split. The official combined worksheet expressly uses theactualBg eligibility test and theC / (Bg+Eg−C) split. Its2025 figures are a method reference; use the actual2026 regional scale/minimum in this Guide. [AEAT combined worksheet](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/supuestos-especiales-concurrencia-rentas.html); [LIRPF arts.56/63–64/74–75/DA20](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a64).

Control using2026 State and city-complementary scales: age40, minimum5,550 in each half, Bg23,000, verifiedEg3,000, qualifyingC1,800, no other minimum or savings facts. Tg26,000. For each half, scale tax onC is171, onTg−C24,200 is2,712.75, and on7,530 is715.35. Enlarged split quota is2,168.40; average rate is exactly8.34%; actual general quota is1,918.20 per half,3,836.40 combined **before credits**. The exact rate deliberately avoids the unresolved display/truncation boundary. City-source eligibility and territorial credits are tested separately below; residence alone does not establish a60% deduction on every receipt. [LIRPF arts.63–65/DA32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65).

### Ceuta and Melilla: scale, source and tax-credit calculation

These cities use the separate **art. 65 complementary scale** through [DA 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#datrigesimasegunda), alongside the state general scale. Do not choose Andalucía's scale from geographical proximity. The complementary schedule is:

| Base from, EUR | Cumulative quota, EUR | Marginal rate on excess | Tax year | Official source |
|---|---|---|---|---|
| 0 | 0 | 9.5% | 2026 | [LIRPF art. 65/DA 32](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65) |
| 12,450 | 1,182.75 | 12% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65) |
| 20,200 | 2,112.75 | 15% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65) |
| 35,200 | 4,362.75 | 18.5% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65) |
| 60,000 | 8,950.75 | 22.5% | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65) |

The state scale's extra over-300,000 band does not create an extra city complementary band. Use the state-law personal/family minima and the appropriate savings halves; then apply the qualifying territorial credit ([LIRPF arts. 63/65/66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a65)).

Under [art. 68.4](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a68), an actual city resident can deduct **60%** of gross state-plus-complementary tax attributable to qualifying city-source income included in the taxable bases. A Spanish IRPF taxpayer living elsewhere has a narrower route: **exclude employment, gains on movable goods and local bank deposits**, and exclude investment-fund income unless all fund assets meet the local-investment condition. This is residence in the city, not merely residence somewhere in Spain. Neither a payer's address nor a local bank account turns all worldwide income into qualifying city-source income.

Qualifying sources are work actually performed locally, including the specified unemployment/pension benefits under [RIRPF art. 58.1.a](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a58); local immovable-property rents/imputations and disposal gains; business/professional activities genuinely completed locally; qualifying local movable-property gains, invested loan/bond returns, effectively located/used leased movables/businesses/mines, and local financial-institution deposits. Company distributions require art. 68.4.3.h's actual operating, residence/object or three-year/external-operation conditions and identifiable reserves under RIRPF art. 58.2. Mere purchases, transport or isolated production stages do not close the required local commercial cycle. Fishing/shipping use the incorporated LIS art. 33 rules.

Build a source ledger **after** the relevant category expense, loss-netting and base-reduction rules. For a habitual **city resident**, let `Qg/Qs` be combined gross state-plus-complementary tax on the general/savings base **after minimum relief**, `Bg/Bs` the corresponding positive taxable bases, and `Cg/Cs` the portions of those bases attributable to eligible city-source income. For the ordinary mixed-source case calculate:

`territorial_credit = 0.60 × (Qg × Cg/Bg + Qs × Cs/Bs)`.

Treat a zero base/basket as zero rather than divide by zero. Do not use gross wages instead of the eligible taxable-base portion or apply the general average rate to savings income. Each source portion must be substantiated and cannot exceed its positive basket. The credit cannot exceed **60% of total gross tax**. Allocate the total credit **50% state/50% complementary** under arts. 67/77, respecting each half's non-negative liquid-tax limit; it is a shared quota credit, not refundable maternity relief. For the narrower art. 68.4.2 route of an IRPF taxpayer **resident outside the cities**, build Qg/Qs from the actual state and regional quotas, using that taxpayer’s actual regional scale and minimum; allocate the credit to the actual state/regional halves under arts. 67/77. A Madrid resident with qualifying Ceuta-property income therefore retains Madrid’s scale/minimum, rather than adopting the city complementary scale. DA 32 restricts that complementary scale to habitual city residents. AEAT's [official mixed-source workpaper](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c16-deducciones-generales-cuota/deduccion-rentas-obtenidas-ceuta-melilla/ejemplo-deduccion-rentas-obtenidas-ceuta-melilla.html) supplies this proportional method under the unchanged provision. Its final complementary subtraction contains a typographical result: use the actual subtraction, not the printed result.

After **three complete years** of habitual/effective city residence, the qualifying extension starts only in tax periods beginning **after** that three-year period ends. At least **one third of net wealth**, valued under wealth-tax rules, must be locally situated. Eligible outside-city income is capped at the net local returns and gains/losses. Test the actual period, wealth ratio, net-income cap and general/savings attribution before extending the credit; do not simply exempt all foreign income or apply the first-year resident rule to worldwide income ([art. 68.4.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a68)).

A distinct **2026 Ceuta-only activity rule** in [DA 64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18) increases the simplified-assessment provisions/hard-to-justify percentage to **10%**, for Ceuta activity income qualifying for art. 68.4. Keep the ordinary **2,000** overall allowance cap and other RIRPF art. 30 conditions; the amendment changes the percentage, not every condition. The annual rule applies to 2026. Its separate **10% módulos net-yield reduction** requires the actual qualifying activity worksheet; it is not a second 10% charge against profit already reduced under the other method. For instalments the new reductions apply only where the filing window begins **more than one month after 3 September 2026**: the ordinary October window began on 1 October, so the ordinary first affected quarterly window is **January 2027 for Q4 2026**. Do not recompute all earlier payments automatically. This Ceuta-specific enhancement does not extend to Melilla or La Palma.

For **2026 La Palma residents**, [DA 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-8) applies the resident limbs of art. 68.4 with the island substituted for the cities, on the same residence/source/extended-residence conditions. Its annual entitlement is separate from the **10 September 2026** withholding/instalment commencement and permitted payer regularisation timing. Apply the actual territorial status and retain that dated distinction; a Canary Islands address outside La Palma is insufficient.

## Deadlines and filing

| Obligation | Rule | Tax year | Source |
|---|---|---|---|
| Ordinary employee filing threshold | Generally gross employment income up to EUR 22,000, only within the exclusive-source and other conditions of art. 96 | 2026 | [LIRPF art. 96.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Reduced employment filing threshold | EUR 15,876 for the specified multiple-payer, maintenance, non-withholding-payer or fixed-rate cases; the multiple-payer exception uses EUR 1,500 from second/later payers under the current article | 2026 | [LIRPF art. 96.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Other exclusive-source filing limits | EUR 1,600 for the stated withheld investment/gain basket; EUR 1,000 for the specified imputed-property/Treasury-bill/public-aid basket; separate EUR 1,000 total-income and below-EUR-500 loss rule | 2026 | [LIRPF art. 96.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Self-employed annual filing | RETA or the specified self-employed sea-worker registration at any point in the year requires filing regardless of those ordinary income limits | 2026 | [LIRPF art. 96.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Annual return | Modelo 100 in the campaign prescribed for 2026 income, filed in 2027; use that year's published form/window and payment rules | 2026 income | [LIRPF art. 96.5–96.6](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a96) |
| Direct-assessment instalments | Modelo 130: first 20 days of April, July and October; first 30 days of January following the year, with non-working-day adjustments | 2026 | [RIRPF arts. 109–111](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a111) |
| Corrections | Use the approved autoliquidación rectificativa route and its specified exceptions, not an automatic old “supplementary versus refund request” split | Current rule | [RIRPF art. 67 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a6-2) |

The ordinary filing exceptions are conditional combinations of income sources, not universal tax-free allowances. Check art. 96.4 mandatory cases, and any additional special filing duty, before concluding no return is required. A taxpayer can need to file to obtain an eligible refund even when below an ordinary compulsory-filing threshold.

For Modelo 130, compute the prescribed year-to-date amount, less earlier relevant instalments and withholding, then the applicable statutory adjustments; the detailed sibling is [es-estimated-tax](es-estimated-tax.md). The 70% professional exemption concerns an actual qualifying activity and the correct reference period. Do not grant it to every trading business. Invoice withholding is taken on gross professional fees, not on profit or VAT. The 7% start rule requires no professional activity in the preceding year and written communication to the payer (RIRPF art. 95). Confirm whether the customer is an obliged withholder. VAT returns are separate and do not have an identical fourth-quarter deadline merely because both are quarterly.

## Penalties and interest

| Event | Statutory consequence | Tax year | Source |
|---|---|---|---|
| Voluntary late filing with tax due, no prior request, within 12 months | 1% plus 1% for each complete month late; art. 27 excludes the corresponding penalty and pre-filing interest | 2026 | [LGT art. 27.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| That filing after 12 months | 15% plus interest from after the 12-month period until filing | 2026 | [Same article](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| All required prompt-payment conditions met | 25% reduction of the art. 27 surcharge | 2026 | [LGT art. 27.5](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) |
| Late ordinary return without economic loss | EUR 200, halved without prior request under the article's conditions | 2026 | [LGT arts. 198.1–198.2](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198) |
| Underpayment offence | Minor 50%, serious 50–100%, very serious 100–150%, after classification and statutory reductions | 2026 | [LGT arts. 188, 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) |
| Executive collection | 5% / 10% / 20% according to payment timing and enforcement stage; ordinary enforcement also carries applicable interest | 2026 | [LGT art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28) |
| Default interest | Rate for each delay segment; AEAT documents 4.0625% under the continued budget for 2026 until a replacement rate takes effect | 2026 | [LGT art. 26](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a26); [AEAT 2026 interest rule](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) |

Classify the actual conduct, unpaid amount, prior request and timing. Art. 191 concealment, false-document, accounting and withheld-tax rules prevent assigning every error the minor rate. Payment reductions have conditions; they are not automatic discounts. A return correction does not cancel interest or a late surcharge merely by changing its label.

## Cross-border points

For an ordinary resident employee physically assigned abroad, calculate the [foreign-work salary exemption](#foreign-work-salary-exemption-ordinary-resident-employee) before the residual foreign-tax credit. A treaty exemption,7(p) and an expatriate-excess election are distinct routes. Use the own-territory foreign-assignment method in [foral IRPF](es-foral-income-tax.md#foreign-assignment-employment-local-exemptions), rather than importing State7(p), where a foral system is competent.

Ordinary residents include worldwide income in its correct general or savings category. A foreign bank's absence of Spanish withholding is not an exemption. Under [LIRPF art. 80](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a80), the foreign-tax credit is the lower of qualifying foreign tax actually paid and the Spanish effective-rate amount on the corresponding taxable foreign base. Separate general and savings effective rates as the article requires; a corporate participation or PE exemption is not imported into individual IRPF.

Check domestic/treaty residence, work location, foreign withholding, foreign-property income, special incoming-worker elections under art. 93 and potential share-exit rules under art. 95 bis. Treaty relief depends on the actual treaty and facts; do not insert a guessed rate. The [non-resident Guide](es-non-resident-income-tax-irnr-and.md) handles ordinary IRNR after residence is settled. Arrival/departure and foral cases remain separately identified in the country README.

The 2026 Ceuta simplified-expense change is **10%**, not a new mainland allowance; [DA 64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18) uses its own effective date for instalments. Art. 68.4 territorial relief and associated withholding rules require territorial income and residence conditions, not merely a Ceuta/Melilla billing address.

## Two worked examples that recompute

### Example 1: an employee's reduction and 2026 low-pay credit

Assume a 40-year-old individual Madrid resident with no relatives giving minima, no other income, no joint return and no other credits. Hypothetical certified gross wages are **EUR 18,000**, deductible employee contributions **EUR 1,150**, and withholding **EUR 600**. The contribution is an input from the certificate, not a payroll rate inferred from this example.

Art. 20's reference income is **EUR 16,850**, before the separate EUR 2,000 allowance. Its reduction is `7,302 − 1.75 × (16,850 − 14,852) = 3,805.50`. The taxable general base is **EUR 11,044.50**. State and Madrid tax use their respective minima of **EUR 5,550** and **EUR 5,956.65**. Rounding each half's computed liability to cents gives **EUR 521.98** and **EUR 432.47**. The 2026 DA 61 credit is `590.89 − 0.2 × (18,000 − 17,094) = 409.69`, below the attributable-tax cap. Tax after this credit is **EUR 544.76**, leaving a **EUR 55.24 refund** against EUR 600 withholding.

```oa-check
name: Madrid employee with distinct net-income reduction and gross-pay credit
inputs:
  gross_wages: 18000
  employee_contributions: 1150
  other_expense_allowance: 2000
  state_minimum: 5550
  madrid_minimum: 5956.65
  withholding: 600
steps:
  employment_reduction_reference: gross_wages - employee_contributions
  employment_reduction: 7302 - 1.75 * (employment_reduction_reference - 14852)
  general_taxable_base: max(0, employment_reduction_reference - other_expense_allowance - employment_reduction)
  state_tax: round((general_taxable_base - state_minimum) * 0.095, 2)
  madrid_tax: round((general_taxable_base - madrid_minimum) * 0.085, 2)
  low_pay_credit: min(state_tax + madrid_tax, 590.89 - 0.2 * (gross_wages - 17094))
  final_tax: state_tax + madrid_tax - low_pay_credit
  refund: withholding - final_tax
expected:
  employment_reduction_reference: 16850
  employment_reduction: 3805.50
  general_taxable_base: 11044.50
  state_tax: 521.98
  madrid_tax: 432.47
  low_pay_credit: 409.69
  final_tax: 544.76
  refund: 55.24
```

### Example 2: established professional, two bases and a capped loss offset

Assume a 40-year-old individual Madrid resident, established simplified-assessment professional with multiple unrelated clients, no qualifying art. 32 reduction, family minima, pension reductions or tax credits. Gross fees are **EUR 60,000** and accepted business expenses, including own contributions and depreciation but before the simplified allowance, are **EUR 20,000**. Prior-year method conditions are met. The 5% item is **EUR 2,000**, so the general base is **EUR 38,000**. Clients withheld **EUR 9,000**; the prior-year professional-withholding exemption from Modelo 130 applies.

The taxpayer also has **EUR 10,000** foreign-bank interest with no withholding/foreign tax and an eligible current-year **EUR 4,000** disposal loss, with no loss-denial rule. Art. 49 permits only **EUR 2,500** cross-basket offset, leaving savings base **EUR 7,500** and **EUR 1,500** loss carried forward. General tax is **EUR 4,353.50 state plus EUR 3,783.04 Madrid**. Savings tax is **EUR 1,455** across its two halves. Total tax is **EUR 9,591.54**, leaving **EUR 591.54 payable** after professional withholding. A full EUR 4,000 offset against interest would be wrong.

```oa-check
name: Madrid professional with simplified expense cap and savings loss limitation
inputs:
  gross_fees: 60000
  accepted_business_expenses: 20000
  simplified_rate: 0.05
  simplified_cap: 2000
  state_minimum: 5550
  madrid_minimum: 5956.65
  interest_income: 10000
  eligible_disposal_loss: 4000
  professional_withholding: 9000
steps:
  profit_before_simplified_item: gross_fees - accepted_business_expenses
  simplified_item: min(simplified_cap, profit_before_simplified_item * simplified_rate)
  general_base: profit_before_simplified_item - simplified_item
  state_general_tax: round(4362.75 + (general_base - 35200) * 0.185 - state_minimum * 0.095, 2)
  madrid_general_tax: round(3841.42 + (general_base - 35425.68) * 0.174 - madrid_minimum * 0.085, 2)
  allowed_savings_offset: min(eligible_disposal_loss, interest_income * 0.25)
  savings_base: interest_income - allowed_savings_offset
  loss_carried_forward: eligible_disposal_loss - allowed_savings_offset
  savings_tax: round(min(savings_base, 6000) * 0.19 + max(0, savings_base - 6000) * 0.21, 2)
  total_tax: state_general_tax + madrid_general_tax + savings_tax
  balance_payable: total_tax - professional_withholding
expected:
  simplified_item: 2000
  general_base: 38000
  state_general_tax: 4353.50
  madrid_general_tax: 3783.04
  allowed_savings_offset: 2500
  savings_base: 7500
  loss_carried_forward: 1500
  savings_tax: 1455
  total_tax: 9591.54
  balance_payable: 591.54
```

## Ask the client first

1. What are the calendar-year residence days, economic/family ties, arrival/departure facts, treaty residence and actual autonomous community or foral territory?
2. Which employment, activity, property, investment and disposal income exists worldwide, with certificates, expenses, assets, losses and foreign taxes by source year?
3. What activity method, prior-year combined turnover, start/cessation history, client relationships and withholding history apply?
4. What age, family-unit election, eligible relatives' ages/income/returns, cohabitation and certified disability facts determine each minimum or credit?
5. Which pension contributions, support payments, regional-credit expenses and prior carryforwards have evidence and applicable limits?
6. What withholding/instalments were actually paid, which returns/corrections exist, and has any authority issued a request or assessment?

For a foreign assignment within question2, obtain each employment contract and its in-year duration, payer salary/premium split, travel/service calendar, foreign-beneficiary work evidence, comparable-tax/treaty and jurisdiction-status evidence, election record and foreign-tax allocation certificate.

## Sources

| Official source | Provisions/use | Read on |
|---|---|---|
| [Ley 35/2006, current consolidated IRPF law](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 8–9, 17–20, 28–32, 45–52, 56–63, 66, 72–76, 80, 82–84, 93, 95 bis, 96; DA 61/64: ordinary computation, residence, allowances, filing and dated 2026 rules | 2026-10-25 |
| [RD 439/2007, IRPF regulations](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 9, 22, 28–30, 67 bis, 95, 109–111: activity treatment, depreciation, correction and payments | 2026-10-25 |
| [AEAT simplified depreciation table](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/3-impuesto-sobre-renta-personas-fisicas/3_5-estimacion-directa-simplificada/3_5_4-tabla-amortizacion-simplificada.html) | Official activity manual updated 30 April 2026; each retained rate/maximal period checked | 2026-10-25 |
| [Cataluña: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2024-6951) | Artículo 611-1. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Galicia: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2011-18161) | Artículo 4. Escala autonómica o complementaria del impuesto sobre la renta de las personas físicas. Regional minima and credit provisions where used | 2026-10-25 |
| [Andalucía: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2021-17915) | Artículo 23. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Principado de Asturias: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2015-945) | Artículo 2. Escala autonómica aplicable a la base liquidable general. Regional minima and credit provisions where used | 2026-10-25 |
| [Cantabria: current regional statute](https://www.boe.es/buscar/act.php?id=BOCT-c-2008-90028) | Artículo 1. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. Regional minima and credit provisions where used | 2026-10-25 |
| [La Rioja: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2017-13750) | Artículo 31. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Región de Murcia: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2011-10542) | Artículo 2. Tarifa autonómica. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. Regional minima and credit provisions where used | 2026-10-25 |
| [Comunitat Valenciana: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-1998-8202) | Artículo 2. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Aragón: current regional statute](https://www.boe.es/buscar/act.php?id=BOA-d-2005-90006) | Artículo 110-1. Escala autonómica del impuesto. Regional minima and credit provisions where used | 2026-10-25 |
| [Castilla-La Mancha: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2014-1368) | Artículo 13 bis. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. Regional minima and credit provisions where used | 2026-10-25 |
| [Canarias: current regional statute](https://www.boe.es/buscar/act.php?id=BOC-j-2009-90008) | Artículo 18 bis. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Extremadura: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2018-8159) | Artículo 1. Escala autonómica del Impuesto sobre la Renta de las Personas Físicas. Regional minima and credit provisions where used | 2026-10-25 |
| [Illes Balears: current regional statute](https://www.boe.es/buscar/act.php?id=BOE-A-2014-6925) | Artículo 1. Escala autonómica del impuesto aplicable a la base liquidable general. Regional minima and credit provisions where used | 2026-10-25 |
| [Madrid: current regional statute](https://www.boe.es/buscar/act.php?id=BOCM-m-2010-90068) | Artículo 1. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Castilla y León: current regional statute](https://www.boe.es/buscar/act.php?id=BOCL-h-2013-90254) | Artículo 1. Escala autonómica. Regional minima and credit provisions where used | 2026-10-25 |
| [Hacienda, 2026 regional tax compilation](https://www.hacienda.gob.es/sgfal/financiacionterritorial/autonomica/capitulo-iv-tributacion-autonomica-2026.pdf) | Updated 23 September 2026; discovery/cross-check of all fifteen regional scales and minima. The actual regional statutes control | 2026-10-25 |
| [RDL 29/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) | Art. 6.Segundo.Tres–Cuatro/Trece and final provision 11: national rental credit effective 8 October 2026, allocation to the state half and DT 15 exclusion | 2026-10-25 |
| [Ley 58/2003, General Tax Law](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Arts. 26–28, 188, 191, 198: interest, surcharges and penalties | 2026-10-25 |
| [AEAT interest rule for the 2025 return filed in 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html) | Explicit continued-budget 2026 interest rate; not a relabelling of 2025 income as 2026 | 2026-10-25 |
| [LIRPF arts. 51–54/64–65/68/75 and DA 20/32/57/64](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764), [RIRPF arts. 51/58](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Pension matching/carries, child maintenance, exempt progression and city/island entitlement and computations; articles reread with their effective dates | 2026-10-27 |
| [AEAT progression worksheet](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/rentas-exentas-progresividad/tratamiento-liquidatorio-rentas-exentas-progresividad-big.html), [Ceuta/Melilla worksheet](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c16-deducciones-generales-cuota/deduccion-rentas-obtenidas-ceuta-melilla/ejemplo-deduccion-rentas-obtenidas-ceuta-melilla.html) | Unchanged statutory computation order; printed arithmetic discrepancies identified rather than copied | 2026-10-27 |
| [AEAT simultaneous annuity/progression worksheet](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c15-calculo-impuesto-determinacion-cuotas-integras/especialidades-determinacion-cuota-integra-estatal-autonomica/supuestos-especiales-concurrencia-rentas.html) | Actual-base annuity eligibility, augmented-base split, separate half quotas/average rates and application to taxable base;2025 source read against unchanged2026 statutory method |2026-10-27 |
| [Current LIRPF7(p)/80](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Entire selected foreign-work exemption and foreign-tax-credit provisions |2026-10-28 |
| [Current RIRPF6/9A3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Entire6, selected9A3(a)/(b): specific/nonspecific remuneration, cap and incompatible excess option |2026-10-28 |
| [AEAT2025 full foreign-work page](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c02-irpf-cuestiones-generales/sujecion-irpf-aspectos-materiales/delimitacion-negativa-hecho-imponible-rentas-sujetas/rentas-exentas-articulo-7-ley-irpf/rendimientos-trabajo-percibidos-trabajos-efectivamente-realizados.html) | Complete relevant page, including day count, TEAC denominator correction, incompatibility and example;2025 manual is not relabelled as2026 income |2026-10-28 |
| [TEAC19July2024 RG00/08685/2023](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00/08685/2023/00/0/1) | Unified criterion and selected operative reasoning: full-year versus actual relationship duration and payer-specific computation |2026-10-28 |
| [Current LIS18.5](https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328) | Selected intragroup-service advantage/utility rule |2026-10-28 |
| [Ley36/2006 DA10](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20843) | Noncooperative-jurisdiction reference bridge |2026-10-28 |
| [OrderHFP/115/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-3508) | Current list and dated application notes; apply the tax-period-specific version |2026-10-28 |

**Source discrepancies resolved by statute.** Hacienda's PDF prints Madrid's EUR 21,894.72 band width with a malformed decimal; Madrid art. 1 gives the correct amount. Its Canarias first cumulative quota is EUR 1,237.30, while current art. 18 bis gives **EUR 1,237.32**. The statutory amounts are used here. La Rioja art. 31 bis also preserves the ordinary assistance amount while increasing only the specified disabled-descendant minimum. The 2027 Valencian scale printed alongside the 2026 table is not used for 2026.

Not yet confirmed in this revision: specific interactions within the fifteen 2026 common-territory regional-credit catalogues in es-irpf-deductions; the specifically outstanding foral methods recorded in [foral IRPF Sources](es-foral-income-tax.md#sources); the three-year Ceuta/Melilla extension’s detailed cross-basket attribution where decisive; final average-rate display/truncation and any minimum-spillover allocation in a fact pattern not resolved by the stated art.56/DA20 method; módulos activity computations and case-specific election/return corrections beyond the published 2026 AEAT entry/election route supplied in es-estimated-tax; the final 2026-return schema, campaign dates and payment-option details for filing in 2027; special elections and treaty/exit computations outside the ordinary examples. These remain visible country-pack work. Independent whole-pack review is pending.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-28. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `es-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/es-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
