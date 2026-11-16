---
name: costa-rica-tax-optimization
description: "Use this skill when someone asks how to lawfully reduce income tax in Costa Rica in 2026. It works the main levers to the figure that decides them: operating in one's own name on the lucrative activity table (not subject to CRC 6,244,000) or through a small company on the 5% to 20% table (gross income up to CRC 119,174,000), the cliff when a company's gross income passes CRC 119,174,000, claiming the family credits, and the red lines (territorial source rules, simplified regime eligibility, substance). Trigger phrases include reduce tax Costa Rica, planificacion fiscal, persona fisica o sociedad, PYME tramos and regimen simplificado."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/costa-rica-tax-optimization"
  jurisdiction: "CR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Costa Rica tax planning levers, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Costa Rican adviser. Aggressive positions are never advised; every suggestion needs review by a qualified professional in Costa Rica.

## Who this applies to

Self-employed individuals and owner-managed businesses in Costa Rica choosing how to structure income in 2026. The tables are owned by [costa-rica-income-tax](costa-rica-income-tax.md); this skill compares options.

Red lines: Costa Rica taxes Costa Rican-source income, so only genuinely foreign-source income is outside scope, and relabelling local income is not planning; the Regimen de Tributacion Simplificada needs its eligibility limits checked before electing; any structure needs real substance.

## Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Lucrative activity, not subject | Up to CRC 6,244,000 of renta neta | Hacienda, Tramos del impuesto sobre la renta 2026: https://www.hacienda.go.cr/docs/TramosRenta2026.pdf |
| Lucrative activity, top rate | 25% above CRC 20,872,000 | same |
| Small legal person table | 5% to CRC 5,621,000, 10% to 8,433,000, 15% to 11,243,000, 20% above | same |
| Gross income ceiling for the small table | CRC 119,174,000 | same |
| Family credits, annual | CRC 20,520 per child, CRC 31,080 spouse | same |

## The base

Individuals: renta neta of the activity on the annual table, less credits. Small companies: renta neta on the 5% to 20% table if the period's gross income is not above CRC 119,174,000; otherwise the general corporate rate (see Not yet confirmed). Profit taken out of a company bears a further tax on distribution, not computed here.

## Deadlines and filing

Annual returns (forms 101 and 102) in TRIBU-CR by mid-March of the following year (16 March 2026 for period 2025, Hacienda CP-11-2026).

## Penalties and interest

Late filing: half a salario base (CRC 231,100); late payment 1% a month up to 20% (Hacienda 2026 summary). Misreporting source or splitting a business artificially exposes the taxpayer to adjustments and fines.

## Cross-border points

Territorial basis: income from Costa Rican sources. Confirm the source of any foreign client income before excluding it; payments abroad bear the remittance tax (not covered).

## Two worked examples that recompute

### Example 1: own name or small company at CRC 15,000,000

Individual: CRC 1,438,450. Small company: CRC 1,735,150 before distribution tax. The individual route is CRC 296,700 cheaper at this level.

```oa-check
name: CR 2026 individual against small company
inputs:
  net: 15000000
steps:
  - individual: (8329000 - 6244000) * 0.10 + (10414000 - 8329000) * 0.15 + (net - 10414000) * 0.20
  - company: 5621000 * 0.05 + (8433000 - 5621000) * 0.10 + (11243000 - 8433000) * 0.15 + (net - 11243000) * 0.20
  - difference: company - individual
expected:
  individual: 1438450
  company: 1735150
  difference: 296700
```

### Example 2: the CRC 119,174,000 gross income cliff

A company with renta neta CRC 20,000,000 pays CRC 2,735,150 on the small table while its gross income stays at or below CRC 119,174,000. One colón more of gross income moves the whole renta neta to the general 30% rate (Ley 7092 art. 15 a)): CRC 6,000,000 on the same CRC 20,000,000, CRC 3,264,850 more (derived). There is no blended computation. Watch gross income near the ceiling; do not split the business artificially to stay under it.

```oa-check
name: CR 2026 small company table at renta neta 20 million
inputs:
  net: 20000000
steps:
  - small_table: 5621000 * 0.05 + (8433000 - 5621000) * 0.10 + (11243000 - 8433000) * 0.15 + (net - 11243000) * 0.20
  - effective_rate: round(small_table / net, 4)
expected:
  small_table: 2735150
  effective_rate: 0.1368
```

## Ask the client first

1. Expected renta neta and gross income for the year.
2. Individual or company today, and how much profit will be taken out.
3. Spouse and children who qualify for credits.
4. Clients abroad and where the work is done.
5. Interest in the simplified regime (purchases, staff, premises).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Hacienda, Tramos del impuesto sobre la renta 2026: lucrative activity and small legal person tables, credits | https://www.hacienda.go.cr/docs/TramosRenta2026.pdf | 2026-11-14 |
| Read for Hacienda notice CP-11-2026: forms and the 16 March 2026 deadline | https://www.hacienda.go.cr/docs/CP11-2026.pdf | 2026-11-14 |
| Read for Hacienda, Infracciones y sanciones administrativas mas relevantes (2026) | https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf | 2026-11-14 |

The general corporate rate is 30% of renta neta for a legal person whose renta bruta exceeds CRC 119,174,000 (Ley 7092 art. 15 a), https://sinalevi.go.cr/ResultadosNormativa/Informacion?param1=10969&param2=148972&param3=1, read 2026-11-14); the company method is in [costa-rica-corporate-income-tax](costa-rica-corporate-income-tax.md).

Not yet confirmed: the tax on distributed profits (15% in the old file); the Regimen de Tributacion Simplificada limits (the old file gave purchases up to about CRC 85,969,200, at most 5 employees, one establishment, assets up to 350 base salaries); PYME reliefs; the old file's "exempt up to about CRC 10,104,000" was wrong for 2026 (the 2026 not-subject amount is CRC 6,244,000).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `costa-rica-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/costa-rica-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
