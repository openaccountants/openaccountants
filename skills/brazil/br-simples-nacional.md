---
name: br-simples-nacional
description: >
  Use this Guide for Brazilian microenterprises, small companies and individual
  microentrepreneurs that need to establish Simples Nacional or SIMEI eligibility and
  calculate calendar-2026 DAS. It covers the five annex tables, effective-rate formula,
  activity segregation, factor R, cash-versus-accrual revenue, export ceilings, state
  sublimits, ordinary and cargo MEI limits, fixed contributions, excess revenue and the
  declarations and evidence needed for review. Trigger phrases include Simples Nacional,
  MEI, DAS, PGDAS-D, DEFIS, DASN-SIMEI, anexos and fator R. It distinguishes 2026
  treatment from enacted future MEI changes and the separate 2027 regular IBS/CBS
  election. Load br-indirect-tax for ordinary local tax calculations and brazil-vat for
  federal consumption taxes and the reform transition.
version: 3.2
jurisdiction: BR
tax_year: 2026
last_updated: 2026-11-26
source_checked: 2026-11-26
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
depends_on:
  - income-tax-workflow-base
---

# Brazil Simples Nacional and MEI v3.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Calendar **2026** calculations for a verified Simples Nacional or SIMEI optant. ME/EPP size alone does not establish an election. Obtain the CNPJ, opening date, ownership and domicile, actual activities/contracts, Consulta Optantes result, earned/received revenue by month and domestic/export destination, payroll, debts, registrations and notices before computing. Do not infer eligibility or an annex from a bank credit or missing records. [LC123 arts.3,16–18-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

Use [br-indirect-tax](br-indirect-tax.md) for ordinary local taxes outside DAS and [brazil-vat](brazil-vat.md) for general consumption-tax reform. The examples and annex tables here remain **2026**; do not roll them into 2027, whose revenue recognition, history and allocation rules change.

## Rates, bands and thresholds

Amounts are BRL. Size ceilings, annual exclusion tests and RBT12 rate bands are different tests. The nominal rate alone is not the monthly effective rate.

| Item | 2026 amount and conditions | Official source |
|---|---|---|
| ME / EPP | ME: annual gross revenue ≤360,000; EPP: >360,000 and ≤4,800,000. Registered legal form and exclusions still apply. Opening-year limits are proportional to months of activity, including fractions | [LC123 art.3 I–II,§§2,4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Exports | Additional qualifying goods/services export ceiling of4,800,000, separately from domestic revenue; apply proportional startup limits to each | [LC123 art.3§14](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| ICMS/ISS sublimit |3,600,000 in every state and DF in2026; separate domestic/export and excess/startup timing tests apply | [CGSN54/2025 official notice](https://www8.receita.fazenda.gov.br/SimplesNacional/Noticias/NoticiaCompleta.aspx?id=94c10cc2-7eb5-4ef0-bfb2-5479e72caff8); [LC123 arts.19–20](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Ordinary MEI |81,000 annual; startup6,750 per opening-to-year-end month, counting fractions. Actual permitted occupation, election and other conditions are necessary | [LC123 art.18-A§§1–4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Cargo MEI |251,600 annual; startup20,966.67 per counted month; only the exclusive qualifying autonomous-cargo occupation route | [LC123 art.18-F](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [DASN§4.3.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |
| Ordinary MEI own contribution |5% of2026 minimum wage1,621 =81.05, before applicable fixed local components and benefit adjustment | [Lei8212 art.21§2IIa](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [Decree12797 art.1](https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html) |
| Cargo MEI own contribution |12% ×1,621 =194.52, plus applicable fixed local components, with exclusive-occupation conditions | [LC123 art.18-FIII](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [Decree12797 art.1](https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html) |
| Fixed local components / ordinary DAS-MEI |1 ICMS if liable and/or5 ISS if liable: ordinary totals82.05,86.05 or87.05. Components and destination follow AnnexXI and CNPJ CNAE/address at the first DAS generation for the entry month or first month of the year; later activity/address changes affect the next year's DAS | [CGSN140 art.101§1](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278); [PGMEI§1.3.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf) |
| Factor R |For covered services only: FS12/RBT12r ≥0.28 →III; below0.28 →V. Equality belongs inIII; it is not an election | [LC123 art.18§§5-J–5-M](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [PGDAS§8.2.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf) |

### Annex I

| RBT12 in BRL | Nominal rate | Deduction in BRL | Official source |
|---|---|---|---|
| 1 a Faixa Até 180.000,00 | 4,00% | 0 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 2 a Faixa De 180.000,01 a 360.000,00 | 7,30% | 5.940,00 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 3 a Faixa De 360.000,01 a 720.000,00 | 9,50% | 13.860,00 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 4 a Faixa De 720.000,01 a 1.800.000,00 | 10,70% | 22.500,00 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 5 a Faixa De 1.800.000,01 a 3.600.000,00 | 14,30% | 87.300,00 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 6 a Faixa De 3.600.000,01 a 4.800.000,00 | 19,00% | 378.000,00 | [LC123 Annex I](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

### Annex II

| RBT12 in BRL | Nominal rate | Deduction in BRL | Official source |
|---|---|---|---|
| 1 a Faixa Até 180.000,00 | 4,50% | 0 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 2 a Faixa De 180.000,01 a 360.000,00 | 7,80% | 5.940,00 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 3 a Faixa De 360.000,01 a 720.000,00 | 10,00% | 13.860,00 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 4 a Faixa De 720.000,01 a 1.800.000,00 | 11,20% | 22.500,00 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 5 a Faixa De 1.800.000,01 a 3.600.000,00 | 14,70% | 85.500,00 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 6 a Faixa De 3.600.000,01 a 4.800.000,00 | 30,00% | 720.000,00 | [LC123 Annex II](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

### Annex III

| RBT12 in BRL | Nominal rate | Deduction in BRL | Official source |
|---|---|---|---|
| 1 a Faixa Até 180.000,00 | 6,00% | 0 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 2 a Faixa De 180.000,01 a 360.000,00 | 11,20% | 9.360,00 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 3 a Faixa De 360.000,01 a 720.000,00 | 13,50% | 17.640,00 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 4 a Faixa De 720.000,01 a 1.800.000,00 | 16,00% | 35.640,00 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 5 a Faixa De 1.800.000,01 a 3.600.000,00 | 21,00% | 125.640,00 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 6 a Faixa De 3.600.000,01 a 4.800.000,00 | 33,00% | 648.000,00 | [LC123 Annex III](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

### Annex IV

| RBT12 in BRL | Nominal rate | Deduction in BRL | Official source |
|---|---|---|---|
| 1 a Faixa Até 180.000,00 | 4,50% | 0 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 2 a Faixa De 180.000,01 a 360.000,00 | 9,00% | 8.100,00 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 3 a Faixa De 360.000,01 a 720.000,00 | 10,20% | 12.420,00 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 4 a Faixa De 720.000,01 a 1.800.000,00 | 14,00% | 39.780,00 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 5 a Faixa De 1.800.000,01 a 3.600.000,00 | 22,00% | 183.780,00 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 6 a Faixa De 3.600.000,01 a 4.800.000,00 | 33,00% | 828.000,00 | [LC123 Annex IV](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

### Annex V

| RBT12 in BRL | Nominal rate | Deduction in BRL | Official source |
|---|---|---|---|
| 1 a Faixa Até 180.000,00 | 15,50% | 0 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 2 a Faixa De 180.000,01 a 360.000,00 | 18,00% | 4.500,00 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 3 a Faixa De 360.000,01 a 720.000,00 | 19,50% | 9.900,00 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 4 a Faixa De 720.000,01 a 1.800.000,00 | 20,50% | 17.100,00 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 5 a Faixa De 1.800.000,01 a 3.600.000,00 | 23,00% | 62.100,00 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| 6 a Faixa De 3.600.000,01 a 4.800.000,00 | 30,50% | 540.000,00 | [LC123 Annex V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |


### Later MEI changes

LC238/2026 provides an ordinary ceiling of140,000 and startup11,666.67 per counted month from1January2028; its2027 transition amounts are110,000 and9,166.67. **Expansion for2027–2029 is conditional on recognition of the revenue waiver in the relevant annual budget law.** Do not use an expanded ceiling without that evidence. Its two-employee allowance (minimum wage or professional floor) takes effect1January2027, not in2026. [LC238 arts.1–3,10](https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-238-21-outubro-2026-800071-publicacaooriginal-181678-pl.html). For remission/renegotiation of a particular debt: Check this point with one of our partner accountants.

## The base

### Eligibility before annex selection

Check the complete [LC123 art.3§§4–6 and art.17](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html). Structural bars include another legal entity holding capital, a Brazilian branch of an overseas-headquartered entity, a foreign branch and a share corporation. Other ownership is conditional: a common individual owner of a favored business triggers the global-revenue test; participation in a non-favored company requires **more than10%** plus excess global revenue; administration of another for-profit entity also uses the global-revenue test. Art.3§5 excludes specified cooperative, purchasing, consortium and similar collective-interest participations from the particular IV/VII bars. These are not blanket exemptions from all exclusions.

Foreign-domiciled owners/partners, public-entity capital, debts whose enforceability is not suspended and missing/irregular required tax registration are separate exclusions. Personal service, subordination and habituality **together** trigger the disguised-employment bar. For restricted finance/factoring, energy, vehicles/fuel, wholesale/production, transport, property development/letting or labour-supply activities and their exceptions: Check this point with one of our partner accountants. Do not declare eligibility from a generic sector name. [LC123 arts.3§4XI,17](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

For **2026 MEI**, confirm SIMEI election, only one establishment, no participation in another enterprise as holder/partner/administrator, and at most one employee paid the minimum wage or professional floor. A replacement during that employee's lawful absence is allowed until the absence ends. The statutory startup legal form is excluded; a newly opened ordinary business is not thereby barred. Match every actual occupation to [AnnexXI](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Anexo_XI.pdf), including CNAE and ISS/ICMS flags. A generic IT label or relabelled software consultancy proves no permitted occupation. [LC123 arts.18-A,18-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

**Benefit months:** the PGMEI adjustment covers maternity, sickness or imprisonment benefit as an individual contributor for the **entire calendar month**, first through last day. Own-INSS is zero for that eligible month; fixed ICMS/ISS remains and accumulates until the10 collection minimum. A partial month does not remove the contribution. Retain benefit dates and check automatic debit against the actual assessment. [PGMEI§§4.2,4.7](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf).

### Annex and revenue

Use the actual supply and statutory activity: resale is AnnexI; own industrial production isII. AnnexIII includes its specified education/training, repairs and accounting services. AnnexIV includes construction/engineering works and subcontracts, landscaping/interior decoration, surveillance/cleaning/conservation and legal services. Covered professional services use the factor-R test forIII/V; CNAE alone does not decide. **Commercial importers and establishments equated to industrial establishments can useII rather thanI.** [LC123 art.18§§4,5-B–5-M](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [PGDAS§8.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

AnnexIV employer CPP remains outside DAS; other ordinary annexes include CPP subject to statutory exceptions. Work out the actual payroll liability separately:20% of an assumed payroll is not a complete employer computation. [LC123 arts.13VI,18§5-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

1. Reconcile gross sales, service prices, operations on others' account and other main-activity revenue; exclude cancelled sales and unconditional discounts. Identify PIX/loan/capital/own-transfer movements and gross sales behind net marketplace settlements. Returns belong in the prescribed return-period adjustment, with a cash-basis deduction limited to the amount actually refunded. [LC123 art.3§1](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [CGSN140 art.17](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278).
2. For a continuing2026 company, RBT12 is earned revenue in the12months immediately before the PA. A startup opted from opening uses opening-month revenue×12, then the average of prior activity months×12 for the next11months; ordinary history applies from month13. A company entering in January after opening also uses that proportional history until month13. Domestic/export rate histories remain separate. **Only for the effective-rate calculation**, substitute1 when RBT12 is zero. [CGSN140 arts.21–23](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278).
3. In2026, the irrevocable annual cash option changes the monthly base to receipts; earned revenue still governs limits and rates. Keep receivable records and compulsory inclusions on closing, returning to accrual, exclusion or local impediment; outstanding installments must otherwise enter by the last month of the following calendar year. **The December2026 transition overrides continued deferral:** include all outstanding amounts for supplies made through31December2026, including installments not yet due. Later receipt is not taxed again; subsequent return/cancellation/unwinding adjusts the original PA. From1January2027 accrual is mandatory; no November2026 cash election is required for2027. [CGSN140 arts.19–20](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278); [CGSN196 art.1, art.144-C; art.8](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694); [CGSN190 art.1, art.16](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/152832); [PGDAS§5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
4. **Effective rate=(RBT12×nominal−deduction)/RBT12.** Apply it to each segregated monthly base with the actual tax allocations. In2026 ISS is capped at5%, excess allocated proportionately to the same-band federal taxes. Sixth-band local-tax percentages can instead use the fifth-band formula before local impediment takes effect. The total annex rate is not an ISS rate or an input credit. [CGSN140 arts.21–24](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278); [LC123 art.23](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).
5. Separate activity, domestic/export, ISS location/retention, ST/monophase, immunity and supported relief. Removing one component does not remove revenue from the other components; a substituted trader differs from the substituting seller. Fixed local taxation requires its own law. Imports, specified ICMS, retained/imported ISS, AnnexIV CPP and other art.13§1 items remain outside DAS. Retain a tax-by-tax reconciliation and separate payment proof. [LC123 arts.13§1,18§4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [PGDAS§§6.5–6.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf). For disputed local relief, suspension, disaster extension or special substitution: Check this point with one of our partner accountants.

### Factor R

FS12 includes eligible paid remuneration, paid pró-labore and the prescribed thirteenth salary, plus employer CPP and FGTS actually collected; exclude rent and profit distributions. Use the remuneration reported in GFIP/eSocial/DCTFWeb; employee INSS withheld is not automatically employer CPP. RBT12r includes earned domestic **and** export revenue even for a cash monthly base. [LC123 art.18§24](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [PGDAS§8.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

The2026 zero rules are0.01 where FS12 is zero (including zero revenue), and0.28 with positive FS12/zero revenue. Opening month uses current paid payroll/revenue; before13months use the prescribed accumulated prior months. Truncate to two decimals without rounding; exactly0.28 selectsIII. Missing payroll is not zero payroll. **For PA11/2026 and12/2026, report FS12 for all Simples activities, irrespective of annex.** [PGDAS§§8.2.1–8.2.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

### Excess and local sublimit

| Event | Effective treatment | Official source |
|---|---|---|
| Continuing ME/EPP, excess ≤20% / >20% |Following calendar year / following month respectively | [LC123 art.3§§9,9-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Startup exceeds proportional ceiling |Retroactive to opening; ≤20% excess instead takes effect following year | [LC123 art.3§§10,12](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Local sublimit exceeded |Continuing: >20% next month, ≤20% following year. Startup: proportional sublimit300,000 per counted month; >20% retroactive to opening, ≤20% following year. Local impediment need not end federal Simples | [LC123 arts.3§§11,13,19–20](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [CGSN140 art.12](https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278) |
| MEI excess ≤20% / >20% |SIMEI exit next1January / retroactive1January of excess year (opening for startup). Notify by last business day of following month. Within20%, the excess is assessed under the ordinary annex rules and paid on the January payment due date without additions; >20% requires recalculation under ordinary Simples if still eligible | [LC123 art.18-A§§7–10](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [DASN§§4.7–4.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |

Exactly20% belongs in the ≤20% route. Test domestic/export ceilings separately and distinguish prior/current years. A SIMEI exit alone does not end Simples. If MEI revenue later crosses >20% after an earlier ≤20% notice, give a new notice by the last business day of the following month and correct the retroactive periods. [LC123 art.18-A§9](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

### 2026 / 2027 consumption-tax boundary

Simples operations are excluded from2026 IBS/CBS test-rate collection; legacy DAS remains due. For electronic-document start dates, exceptions and current layouts: Check this point with one of our partner accountants. [LC214 art.348IIIc](https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.html).

From2027, eligible Simples ME/EPP can retain IBS/CBS within DAS or elect regular IBS/CBS while keeping the remaining Simples treatment. LC123 art.13§§9–11 governs that election. Normal semester elections are the preceding September for January and March for July; a regular-regime refund in the current or preceding calendar year prevents exit. Full-DAS suppliers have no own regular IBS/CBS input credit; a regular buyer's credit is limited to the IBS/CBS effectively due through Simples, subject to LC214 arts.47–48. This does not extend automatically to SIMEI supplies; for a MEI buyer-credit exception: Check this point with one of our partner accountants. [LC214 arts.41§5,47§9,517](https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.html); [CGSN196 art.2, art.58§§7–8, effective1January2027](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694).

For first-semester2027 the exceptional windows were Simples entry/return1September–15October2026, regularisation by30October; regular IBS/CBS election1September–30October2026; irreversible cancellation3November–20December2026. These are distinct choices; existing eligible Simples optants need no fresh application merely to remain. Read the actual receipt and effective date. For a new-company/MAT screen or disputed option: Check this point with one of our partner accountants. [CGIBS30September2026 notice](https://cgibs.gov.br/embora-os-periodos-sejam-parecidos-tratam-de-escolhas-diferentes-por-isso-e-importante-entender-cada-situacao); [regular-option manual§§2–4](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf).

Compare actual input/output taxes, customer credits, prices, recovery timing, compliance costs and remaining DAS. Keep both workpapers conditional where inputs are missing; B2B/B2C alone proves no saving.

## Deadlines and filing

| Obligation | Deadline / scope | Official source |
|---|---|---|
| Monthly PGDAS-D / DAS |20th following month; payment shifts to next banking business day without bank service. Match any actual extension | [PGDAS§6.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf); [FAQ6.4,6.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf) |
|2026 DEFIS |31March2027, expressly preserved in PGDAS-D2018 by art.144-F. Earlier normal years:31March following year; historical special events in first4months: endJune, otherwise endfollowing month; no weekend/holiday shift under that framework | [CGSN196 art.1, art.144-F](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694); [PGDAS§9.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf) |
|2027 onward annual data |Once January–March within PGDAS-D, including inactive entities; special-event data in event-month PGDAS-D, also for exclusion. Keep2026's separate transition duty distinct | [CGSN190 art.1, art.38-B](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/152832); [CGSN196 art.2, art.38-B§2-A; art.8](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694) |
| DASN-SIMEI |Last day of May following year (2026:31May2027). Extinction in first4months: endJune; otherwise endfollowing month | [DASN§2.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |

**Monthly ME/EPP:** in the [Simples Portal](https://www8.receita.fazenda.gov.br/SimplesNacional/Default.aspx), use authorised CNPJ representation → **Cálculo e Declaração → PGDAS-D e DEFIS**. Confirm the actual2026 recognition regime; choose **Declaração Mensal → Declarar/Retificar**, PA/year, earned domestic/export revenue and receipts for cash optants. Zero revenue still requires the declaration. Supply FS12 as above. Choose each establishment's activities, segregated bases and ISS municipality; support any judicial suspension with the actual process. Check **Resumo da Declaração – Valor Devido por Tributo → Transmitir**, save declaration/receipt, then **Gerar DAS** and keep separate payment proof. **Débitos → Consultar/Gerar DAS** may be needed for already-declared debts and prior amortisations/offsets/transfers. [PGDAS§§3,5–6,8.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

**DEFIS for applicable periods, including2026:** **DEFIS → Acessar DEFIS**, year, Original/Retificadora, actual normal/special status/date. Complete missing monthly returns, enter economic/fiscal, establishment, owner and inactivity data; no sales alone does not prove no patrimonial movement. **Salvar Dados → Verificar Pendências → Transmitir → Gravar Recibo/Imprimir**. For an incorrectly declared special event blocking subsequent periods: Check this point with one of our partner accountants. [PGDAS§§9.2–9.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf); [2026 transition art.144-F](https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694).

**MEI:** **PGMEI → Emitir Guia de Pagamento (DAS)**, CNPJ/year/PA → **Apurar/Gerar DAS → Imprimir/Visualizar PDF**; check assessment and pay with separate proof. Payment is monthly even without revenue, including opening/closing months. For **Serviços Públicos → DASN SIMEI**, choose year, original/rectifying and normal/extinction status; complete missing prior returns and PGMEI assessments. Enter commerce/industry and service revenues plus employee answer, check total/assessed/paid amounts and excess, transmit and retain receipt. Keep excess DAS and MAED/DARF distinct; annual transmission is no proof of monthly payment. [PGMEI§§1–4.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf); [DASN§§2–4.9](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf).

**Regular IBS/CBS election record:** authorised CNPJ representation → **Opção pelo regime regular de IBS e CBS** (or consumption portal's **Escolher Regime de Apuração IBS/CBS**) → inspect entity, **Solicitar Opção**, acknowledgement/confirmation, result PDF and history/effective date. Cancel only with authority in the applicable window and save the receipt. These are documented labels, not a tested live submission. [option manual§§3–4](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf).

## Penalties and interest

PGDAS-D: late/omitted information carries2% per calendar month/fraction from the day after the original deadline, cap20%, minimum50 per reference month, even if tax was paid; incorrect/omitted information:20 per group of10. Subject to the minimum, penalties reduce **to half** for filing before an official procedure or **to75%** for filing in the intimation period; the FAQ requires payment within30days after notification. Technically nonconforming filings are treated as unfiled with a10-day replacement notice. The older manual's April-next-year clock is superseded by the statute. [LC123 art.38-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [FAQ6.5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf).

DASN-SIMEI:2% per month/fraction, cap20%, minimum50, with the applicable notice/reductions; retain its separate MAED/DARF. [DASN§4.9](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf). For DEFIS sanctions across the repeal/2026-return transition: Check this point with one of our partner accountants. Use the current authorised debt document for actual late-DAS charges rather than assuming a single all-in rate.

## Cross-border points

Foreign domicile/structures remain eligibility checks even for Brazilian-only sales. Domestic/export limits and rate histories are separate. A service export needs a foreign resident/domiciled recipient and payment representing an inflow of foreign exchange; it does not qualify when the result occurs in Brazil. A foreign bank receipt alone proves neither export nor exemption. Export segregation removes only the prescribed components and retains the others. Imports require separate outside-DAS analysis. [LC123 arts.3§§14–15,13§1,17II,18§§12–14](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [PGDAS§§1.5,6.5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

## Two worked examples that recompute

### Ordinary AnnexI commerce

A continuing eligible optant has prior12-month earned revenue500,000 and current ordinary resale revenue45,000, with no ST, monophase, export, relief, local sublimit effect or other segregated revenue. AnnexI's third band supplies9.5% and13,860. Effective rate=(47,500−13,860)/500,000=6.728%; monthly DAS=3,027.60. This is a total-DAS example, not the buyer's separately deductible tax credit. [LC123art.18,AnnexI](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

```oa-check
name: Simples Annex I ordinary commerce
inputs:
  rbt12: 500000
  monthly_revenue: 45000
  nominal: 0.095
  deduction: 13860
steps:
  - effective: (rbt12 * nominal - deduction) / rbt12
  - das: monthly_revenue * effective
expected:
  effective: 0.06728
  das: 3027.60
```

### Covered consultancy: actual payroll selects III or V

A continuing eligible company performs a professional consultancy actually subject to factorR. Earned RBT12r400,000 and current ordinary service base30,000 are otherwise unchanged. If paid eligible FS12 is130,000, ratio0.325 satisfies the threshold, so AnnexIII gives9.09% and2,727monthly. If supported FS12 were100,000, ratio0.25 fails, so AnnexV gives17.025% and5,107.50monthly. The DAS difference is2,380.50, before considering any actual payroll cost or other taxes. A missing payroll file does not authorise the lower-payroll assumption. This works both factual routes; it is not permission to choose an annex or manufacture remuneration. [LC123art.18§§5-J,5-K,24; AnnexesIII,V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

```oa-check
name: Factor R consultancy both factual routes
inputs:
  rbt12: 400000
  revenue: 30000
  payroll_high: 130000
  payroll_low: 100000
  iii_nominal: 0.135
  iii_deduction: 17640
  v_nominal: 0.195
  v_deduction: 9900
steps:
  - factor_high: payroll_high / rbt12
  - factor_low: payroll_low / rbt12
  - iii_effective: (rbt12 * iii_nominal - iii_deduction) / rbt12
  - v_effective: (rbt12 * v_nominal - v_deduction) / rbt12
  - das_iii: revenue * iii_effective
  - das_v: revenue * v_effective
  - difference: das_v - das_iii
expected:
  factor_high: 0.325
  factor_low: 0.25
  iii_effective: 0.0909
  v_effective: 0.17025
  das_iii: 2727
  das_v: 5107.50
  difference: 2380.50
```

The former two other worked topics remain: an **eligible, verified AnnexXI service occupation**, liable only for fixedISS and without the full-month benefit adjustment, pays1,621×5%+5=86.05 monthly in2026; a generic “IT services MEI” does not establish eligibility. A full-year ordinary MEI with90,000earned revenue exceeds81,000by9,000, or11.111…%, below the20% boundary97,200. Its SIMEI exit is next1January with communication and prescribed excess assessment, not immediate retroactive exit. A startup or a different eligibility failure changes that answer. [LC123arts.18-A,18-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [Lei8212art.21](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [DASN manual §4.7–4.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf).

```oa-check
name: Eligible ordinary service MEI fixed 2026 DAS
inputs:
  monthly_minimum_wage: 1621
  own_social_rate: 0.05
  fixed_iss: 5
steps:
  - own_social: monthly_minimum_wage * own_social_rate
  - fixed_das: own_social + fixed_iss
expected:
  own_social: 81.05
  fixed_das: 86.05
```

```oa-check
name: Full-year ordinary MEI excess within twenty percent
inputs:
  full_year_limit: 81000
  annual_revenue: 90000
  excess_margin: 0.20
steps:
  - excess: annual_revenue - full_year_limit
  - excess_percent: excess / full_year_limit * 100
  - twenty_percent_boundary: full_year_limit * (1 + excess_margin)
expected:
  excess: 9000
  excess_percent: 11.111111111
  twenty_percent_boundary: 97200
```


## Ask the client first

Obtain identity/election/ownership and notices; earned/received domestic/export histories; actual contracts and permitted occupation; paid payroll/pro-labore/CPP/FGTS; benefit dates; debt/registration evidence; filed returns, receipts and payments; and the2027 option record. Retain reconciliations, annex/factor-R calculations, ceilings/effective dates and outside-DAS liabilities. Inspect supplied Banco do Brasil, Caixa, Itaú, Bradesco, Santander, Nubank, Inter and C6 CSV/PDF/OFX formats; bank names, PIX, fiscal-document and tax labels are search clues. Continue supported work and mark missing-input outcomes conditional.

## Sources

Read dates below distinguish completed22November evidence reused for unchanged2026 rules from the26November targeted operative reads. They do not certify another writer's11November source-read date or a live filing.

| Source / operative scope read | Official URL | Read on |
|---|---|---|
| LC123: arts.3,13,16–18-C,18-F,19–20,38–38-B and2026 AnnexI–V; no claim of whole-act read | https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html |2026-11-22|
| LC238: operative arts.1–10, later ceiling commencement/budget condition; individual remission referred | https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-238-21-outubro-2026-800071-publicacaooriginal-181678-pl.html |2026-11-22|
| Decree12797: complete arts.1–2,2026 wage | https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html |2026-11-22|
| Lei8212: art.21 contribution; not a complete payroll read | https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html |2026-11-22|
| CGSN54/2025: full substantive2026 sublimit notice | https://www8.receita.fazenda.gov.br/SimplesNacional/Noticias/NoticiaCompleta.aspx?id=94c10cc2-7eb5-4ef0-bfb2-5479e72caff8 |2026-11-22|
| PGDAS-D manual13November2026:2026 revenue/filing/DEFIS/factor-R text;§§5,8.2.2 re-read26November; screenshots not tested | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf |2026-11-22;2026-11-26|
| FAQ9October2026:6.4–6.12; statute/newer operative resolutions control conflicts | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf |2026-11-22|
| DASN-SIMEI: complete extracted ordinary/excess/penalty text; no screenshot/live-screen test | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf |2026-11-22|
| AnnexXI: table framework and cargo rows; actual client occupation requires matching | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Anexo_XI.pdf |2026-11-22|
| PGMEI: ordinary assessment, benefit and payment text;§1.3.1 annual lock re-read26November | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf |2026-11-22;2026-11-26|
| CGSN140: targeted arts.2–3,15–24,97-A,101§1 and144-C–F, multivigente future annotations separated | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278 |2026-11-26|
| CGSN190: arts.16,38-B,144-D–E amendments and repeal/effective clauses, as amended by196; not whole-act clearance | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/152832 |2026-11-26|
| CGSN195: complete operative text,2027 electronic-document amendment; no general document-exception clearance | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154194 |2026-11-26|
| CGSN196: complete operative body including144-C,144-F,credit boundaries and commencement; attached2027 schedules not read or used | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/154694 |2026-11-26|
| LC214 official Camara consolidation: arts.41,47,348,517,544; not whole-act read | https://www2.camara.leg.br/legin/fed/leicom/2025/leicomplementar-214-16-janeiro-2025-796905-normaatualizada-pl.html |2026-11-22|
| CGIBS30September2026 notice: operative first-semester option dates | https://cgibs.gov.br/embora-os-periodos-sejam-parecidos-tratam-de-escolhas-diferentes-por-isso-e-importante-entender-cada-situacao |2026-11-22|
| Regular-option manual7October2026: complete extracted14-page text; no live election/MAT test | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf |2026-11-22|

Not yet confirmed: actual taxpayer eligibility/occupation, disputed sector/local exceptions or relief, disaster extensions, later MAT screens, full electronic-document exceptions, individual MEI debt relief, budget satisfaction for expanded MEI ceilings, SIMEI buyer-credit exceptions and DEFIS penalty treatment across the transition. For each such unresolved application: Check this point with one of our partner accountants. No unverified amount or individual result is authorised by the examples.
