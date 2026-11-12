---
name: br-simples-nacional
description: "Use this Guide for Brazilian microenterprises, small companies and individual microentrepreneurs that need to establish Simples Nacional or SIMEI eligibility and calculate calendar-2026 DAS. It covers the five annex tables, effective-rate formula, activity segregation, factor R, cash-versus-accrual revenue, export ceilings, state sublimits, ordinary and cargo MEI limits, fixed contributions, excess revenue and the declarations and evidence needed for review. Trigger phrases include Simples Nacional, MEI, DAS, PGDAS-D, DEFIS, DASN-SIMEI, anexos and fator R. It distinguishes 2026 treatment from enacted future MEI changes and the separate 2027 regular IBS/CBS election. Load br-indirect-tax for ordinary local tax calculations and brazil-vat for federal consumption taxes and the reform transition."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/br-simples-nacional"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil Simples Nacional and MEI v3.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Start with the actual taxpayer, activities and election record. ME/EPP size status does not itself prove a Simples election; SIMEI is a further fixed-payment system for an eligible individual microentrepreneur. A company carrying out a non-eligible activity or with a prohibited ownership structure cannot select an annex to cure that bar. Obtain the actual CNPJ, registered activities and Consulta Optantes result, then apply LC123arts.3,16–18-A. [LC123](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

Before computing, obtain: opening date and prior/current-year revenue separated between domestic and exports; each establishment's earned and received monthly revenue; actual contracts/CNAEs and fiscal qualifications; ownership/domicile/debt/registration facts; paid payroll and contributions; election/exit notices and returns. These facts control eligibility, timing, rate and segregation. Do not default an unknown business to ME, an unknown activity to Annex V, missing payroll to a low factor R or missing revenue to a top band. [LC123arts.3,17–18; official PGDAS-D manual §§1.5,5–6](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html), [manual](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

This Guide owns the Simples/MEI figures. [br-indirect-tax](br-indirect-tax.md) owns ordinary ICMS/ISS/IPI outside DAS. [brazil-vat](brazil-vat.md) owns PIS/Cofins and the general CBS/IBS transition. This is a source-based draft at tier2; no prior accountant's approval is carried into this replacement.

## Rates, bands and thresholds

Amounts are in BRL. For the annex tables below, the first boundary is inclusive and every subsequent band starts at the stated .01. The nominal rate alone is not the monthly effective rate. Apply the formula and segregation in The base; sixth-band local-tax limitations can change the total charged through DAS. [LC123art.18 and AnnexesI–V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

| Item | Rule for calendar2026 and conditions | Official source |
|---|---|---|
| Microempresa | Annual gross revenue at most360,000; registered forms and art.3 exclusions still apply | [LC123art.3I,§4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Empresa de Pequeno Porte | Annual gross revenue above360,000 and at most4,800,000; a startup uses the proportional limit | [LC123art.3II,§2](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Separate export ceiling | Up to an additional4,800,000 for qualifying goods/services exports, separately from the domestic ceiling; not a single combined4,800,000 test | [LC123art.3§14](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Startup ME/EPP ceiling | Apply1/12 of the relevant annual limit for each month from opening to year-end, counting a fraction as a full month; exclusion timing differs for excess up to20% | [LC123art.3§§2,10–14](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| ICMS/ISS sublimit | 3,600,000 in all states and DF for2026; apply the distinct excess/startup timing before removing local taxes from DAS | [RFB PortariaCGSN54/2025 notice](https://www8.receita.fazenda.gov.br/SimplesNacional/Noticias/NoticiaCompleta.aspx?id=94c10cc2-7eb5-4ef0-bfb2-5479e72caff8); [LC123arts.19–20](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Factor R | Listed services use AnnexIII at ratio at least28%; otherwise AnnexV. It is not an election and does not apply to every service | [LC123art.18§§5-J,5-K,24](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Ordinary MEI ceiling | 81,000 annual; startup6,750 per opening-to-year-end month, including fractions. Positive occupation and other eligibility tests apply | [LC123art.18-A§§1–4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Cargo MEI ceiling | 251,600 annual or startup20,966.67 per counted month, for the exclusive qualifying cargo occupation route; not a higher limit for every MEI with a van | [LC123art.18-F](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [DASN manual §4.3.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |
|2026 minimum wage | 1,621 from1January2026; used below for MEI's own contribution | [Decree12797/2025art.1](https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html) |
| Ordinary MEI social contribution |5% of the minimum, giving81.05 monthly, plus1 ICMS and/or5 ISS if liable to the respective tax | [Lei8212art.21§2IIa](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [LC123art.18-A§3V](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Cargo MEI social contribution |12% of the minimum, giving194.52, plus the applicable fixed local tax. The exclusive occupation conditions remain necessary | [LC123art.18-FIII](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Ordinary monthly DAS-MEI | Commerce/industry82.05; services86.05; both87.05 when both local components apply. Other taxes outside the fixed system remain separate; an eligible full-calendar-month benefit can remove the own-INSS component under the rule below | [LC123art.18-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [Lei8212art.21](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html); [Decree12797](https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html) |

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

### Enacted later MEI changes, not the 2026 computation

LC238/2026 was enacted on21October2026. Its general ordinary-MEI ceiling becomes140,000, with11,666.67 startup monthly proportional amount, from1January2028. A transitional2027 ceiling is110,000, with9,166.67 startup monthly amount. The revenue-limit expansion for2027–2029 depends on the budget-law conditions in art.3; do not promise the expanded limit before checking them for that year. The change allowing two employees and other non-ceiling changes starts1January2027, subject to their own conditions. The remission/renegotiation chapter is not an unconditional cancellation of every DAS debt. None changes the 2026 ceiling, employee rule or payment computation above. [LC238arts.2–3,5–10](https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-238-21-outubro-2026-800071-publicacaooriginal-181678-pl.html).

## The base

### Eligibility and activity classification

Apply the complete LC123art.3§4 and art.17 bars and their exceptions. Important ordinary checks are:

| Situation | Treatment and condition | Official source |
|---|---|---|
| Another legal entity holds capital; foreign-headquartered branch; company has overseas branch; share corporation | Art.3§4 contains separate structural bars. Corporate participations and the specified cooperative/association exceptions require the full tests | [LC123art.3§§4–6](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Individual owner also owns/administers another business | Apply the particular participation percentage and global-revenue conditions; do not reject every second ownership automatically | [LC123art.3§4III–V,§5](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Owner/partner domiciled abroad; public-entity capital; enforceable tax/social debts; missing/irregular required registration | Distinct art.17 bars. Suspended enforceability is relevant for the debt test; prove regularisation rather than assume a bank payment cured it | [LC123art.17II,III,V,XVI](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Financial/factoring/credit, energy, specified vehicles/fuel, wholesale/production restrictions, property development/own-property letting and labour supply | Apply the actual statutory bar and its exceptions. Particular passenger transport and small alcoholic-drink producers have defined exceptions; AnnexIV activities need §1 and art.18§5-C together | [LC123arts.3§4VIII,17I,VI–XV,§§1,5;18§5-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Employment disguised as supplier | Personal service, subordination and habituality together are an art.3§4XI exclusion; a CNPJ or invoice alone does not establish independence | [LC123art.3§4XI](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

For MEI, also establish optant status, only one establishment, no participation in another enterprise as holder/partner/administrator, and ordinarily at most one employee receiving the minimum wage or professional floor under the2026 rule. LC123art.18-C§2 permits a substitute employee, including a fixed-term hire, during the sole employee’s legal absence until the absence conditions cease; this is the statutory replacement exception, not a second permanent position. The statutory startup form is excluded by LC123art.18-A§4V. This legal-form exclusion does not mean every newly opened ordinary business is barred: an otherwise eligible new MEI uses the proportional opening-year limit. Eligibility is a **positive occupation test** against AnnexXI, not the old blanket phrase “all unregulated professions” or generic “IT services”. The current official occupation PDF lists the actual occupation, CNAE and ISS/ICMS flags. Confirm all actual activities against it; a software consultant is not made eligible by calling the work computer maintenance. [LC123arts.18-A,18-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [DASN manual §1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf); [official AnnexXI](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Anexo_XI.pdf).

**MEI benefit adjustment.** Under the PGMEI manual, mark **Benefício INSS** only for salary-maternity, sickness or imprisonment benefit as an individual contributor covering the entire calendar month, from first to last day. For that eligible month own-INSS is zero; applicable fixed ICMS/ISS remains and is accumulated into later assessments until the10minimum for collection is reached. A partial month does not remove the whole contribution. Retain the benefit period and actual assessment, and coordinate an authorised automatic debit to avoid duplicate/manual payment. [PGMEI manual §§4.2,4.7](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf).

Use the contract and service actually performed to select the annex; CNAE is evidence, not a licence to ignore the statutory activity. AnnexI covers resale, II industrialised goods. AnnexIII includes its expressly listed services, including specified education/training, repairs, accounting offices and other statutory categories. AnnexIV includes construction/engineering works and subcontracts, landscaping/interior decoration, surveillance/cleaning/conservation and legal services. Factor-R professional activities under art.18§5-I, §5-D and related rules need the payroll test to choose III/V; do not send lawyers to V or all maintenance/health/IT work to a single generic annex. [LC123art.18§§4,5-B–5-M](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§8.1–8.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

AnnexIV excludes CPP from DAS, with the employer contribution collected under the otherwise applicable law. Do not treat “20% of payroll” as every employer's complete liability: actual contribution base, RAT, employee deductions, other applicable rules and any lawful replacement regime need separate payroll work. Other ordinary annexes include CPP within the annex allocation, subject to the actual exceptions. [LC123arts.13VI,18§5-C](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [Lei8212art.22](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html).

### Revenue, effective rate and segregation

1. Reconcile gross revenue from underlying supplies, fiscal documents, marketplace reports and earned/received records. Sale value, service price and the result of operations on another's account are treated under the statutory revenue definition; exclude cancelled sales and unconditional discounts, with returns handled in the proper period. A PIX credit can be a sale, capital, loan or transfer. Identify it before inclusion. Marketplace settlement after fees is not automatically the gross sale amount. [LC123art.3§1](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§1.5,6](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
2. Keep separate running domestic/export annual-limit totals, prior-year totals, and prior12-month earned revenue for rate calculation. For a continuing company use RBT12, the12months before the assessment month. For a startup opted from opening, annualised RBT12 in the first month is that month’s earned revenue×12; in the next11months it is the average earned revenue of prior activity months×12; from month13 use the ordinary rolling history. A business entering the January after opening follows the latter proportional rule until month13. Domestic and export revenue are separately used for their rate/base calculations under art.3§15, while both are combined for factorR. The calendar-year limit test and rate annualisation are different calculations. If RBT12 is zero, the manual uses1 for the effective-rate formula, avoiding division by zero. [LC123art.18§§1–3](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§1.5,6,8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf); [FAQ5.3–5.4,5.24](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf).
3. Under the annual irrevocable cash option, received revenue is the monthly base, but earned revenue still controls rates and limits. Record both; an unpaid invoice does not disappear from the eligibility/annex-band history. Preserve the actual chosen regime. [LC123art.18§3](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
4. Select the annex and its RBT12 band, then compute **effective rate=(RBT12×nominal rate−deduction)/RBT12**. Apply it to the appropriate monthly segregated base and statutory allocation adjustments. Multiple activities share the relevant company domestic/export revenue history but are computed in their actual categories. Apply the effective tax-allocation percentages, cap the ISS component at the statutory5% and transfer the excess proportionately to the same-band federal components; the annex’s total rate is not the ISS rate. No input-cost deduction is allowed merely because the supplier charged tax. [LC123art.18§§1-A,4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).
5. Segregate domestic/export resale, industrial sales, service categories, ISS location/retention, monophase or substitution, immunity and supported local reductions. A substituted trader's revenue qualification differs from the substituting seller's own ICMS operation. Removing the substituted/monophase tax component does not remove that revenue from every other tax's base. Fixed ICMS/ISS requires an applicable local rule, not a free field election. [LC123art.18§4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§6.5–6.6](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
6. Reconcile final DAS by tax and establishment with prior balances, supported suspension/assessment qualifications and payments. Imports, specified ST/advance/interstate ICMS, retained/imported ISS, AnnexIV CPP and other art.13§1 items may remain outside DAS. “Unified” does not mean every conceivable tax is included. [LC123art.13§1](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

### Factor R, including startups and zero months

For covered services only, use **FS12/RBT12r**. FS12 is remuneration paid in the relevant prior12months plus qualifying CPP/FGTS actually collected, including paid pró-labore and the prescribed thirteenth salary; rents and distributed profits are excluded. Do not add all INSS deductions as employer CPP. The denominator includes earned domestic and export revenue in the relevant period even where the monthly DAS uses cash receipts. Reconcile reported payroll and actual payment/contribution evidence. [LC123art.18§§5-K,24](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§1.5,8.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

The manual's zero/startup rules matter: no payroll and no revenue gives0.01; no payroll with positive revenue also gives0.01; positive payroll with zero revenue gives0.28. In the opening month use that month's paid payroll and revenue; for fewer than13months of activity use the actual accumulated prior months prescribed by §8.2.1 rather than invent12full months. Express the ratio to two decimal places without rounding for the threshold test, as the manual requires. A ratio exactly0.28 belongs in III. Obtain the underlying figures before deciding. [manual §8.2.1pp75–77](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

### Excess revenue and local sublimit timing

| Event | Effective treatment | Official source |
|---|---|---|
| Continuing ME/EPP exceeds annual ceiling by at most20% | General exclusion effective following calendar year; exactly20% belongs here | [LC123art.3§9-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Continuing ME/EPP exceeds by more than20% | General exclusion from following month; do not label every first over-limit sale an immediate annual exit | [LC123art.3§9](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Startup exceeds proportional ceiling | Ordinarily retroactive to opening, except excess at most20% gives following-year effect | [LC123art.3§§10,12](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| Local sublimit exceeded | Local impediment follows its own art.20 rules: ordinarily following month; at most20% excess following year. Startup retroactivity and its20% exception have separate conditions | [LC123arts.3§§11,13,20§§1,1-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |
| MEI exceeds ordinary/proportional ceiling by at most20% | SIMEI exit from following1January, prescribed excess-payment and communication duties still apply | [LC123art.18-A§7IIIa/IVa,§§8,10](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [DASN manual §4.7–4.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |
| MEI exceeds by more than20% | Retroactive SIMEI exit to1January of the excess year, or opening for startup; compute ordinary Simples if still eligible, rather than only a fixed top-up | [LC123art.18-A§7IIIb/IVb](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html) |

Above the local sublimit, federal Simples can continue while local taxes leave DAS from the proper effective date. Check separate export totals, prior/current year, sixth-band allocations and all establishments before recomputing. A SIMEI exit is not automatically an exit from Simples Nacional. If an initial MEI excess notification was for at most20% and revenue later crosses more than20% in the same year, a new notification is required by the last business day of the month following that later crossing; its earlier retroactive effective date must be applied. Keep both communication receipts and effective dates, and correct the periods actually affected. [LC123arts.18-A§9,19–20](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

### 2026 transition and the separate 2027 IBS/CBS decision

Simples operations are excluded from the2026 test-rate collection under LC214art.348IIIc. This is not a general waiver of legacy DAS. The new electronic-document schedule has its own Simples start from1January2027 under JointAct4. Use [brazil-vat](brazil-vat.md) for general grace, waiver, correction and current document phases, rather than the old statement “all penalties suspended for3months”. [LC214art.348](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm); [JointAct4art.1§1](https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf).

From2027, a Simples business can keep IBS/CBS within DAS or elect the regular regime for those taxes while preserving the remaining Simples treatment. The election provision is **LC123art.13§§9–11**, inserted by LC214art.517 and amended by LC227; art.21-A concerns CADIN, not this election. Elections apply to semesters beginning January/July, normally elected the preceding September/March. A refund under the regular regime can restrict exit under LC214art.41§5; include that lock in the decision. Full-DAS sellers do not take their own regular IBS/CBS input credits, but a regular buyer can credit the IBS/CBS amount due through Simples, subject to the law. “No transferable credit at all” is therefore wrong. [LC214arts.41,47§9,517,544](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm).

For the first2027 semester the actual exceptional timetable was: Simples entry/return1September–15October2026, pending issues regularised by30October; regular IBS/CBS election1September–30October2026; irreversible cancellation3November–20December2026. These are distinct choices. Existing Simples optants need not reapply merely to remain. As of11November2026, the October windows have passed; do not tell a continuing company to make a fresh ordinary election now. New-company/MAT cases follow their actual current route. [CGIBS30September2026 notice](https://cgibs.gov.br/embora-os-periodos-sejam-parecidos-tratam-de-escolhas-diferentes-por-isso-e-importante-entender-cada-situacao); [regular-option manual §§2–4](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf).

Compare both methods using actual taxed inputs, expected output bases/rates for the effective period, customers' legally available credits and agreed prices, recovery timing, compliance costs and the remaining DAS. B2B/B2C labels alone do not prove a saving, and an estimated future standard rate cannot complete a binding2027 comparison. State which figures remain unknown and prepare both workpapers for review. This is a decision method, not a recommendation to elect automatically.

## Deadlines and filing

| Obligation | Ordinary deadline and boundary | Official source |
|---|---|---|
| Monthly PGDAS-D and DAS |20th of following month; payment moves to next banking business day if no bank service. Check published disaster/other extensions for the actual place/period | [official manual §§1.4,6.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf); [FAQ6.4,6.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf) |
| DEFIS |31March of following year; normal calendar2026 due31March2027. Special merger/split/incorporation/extinction: endJune for first-four-month events, otherwise endfollowing month. Ordinary date does not move for weekend/holiday | [FAQ6.10](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf); [manual §9.1](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf) |
| DASN-SIMEI |Last day of May following year; calendar2026 ordinarily31May2027. Extinction special: endJune for first-four-month events, otherwise endfollowing month | [DASN manual §2.2](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |
| MEI excess communication |Last business day of month after excess, with effective date determined by the20%/startup tests above | [DASN manual §4.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf) |

**ME/EPP monthly route.** Open the [Portal do Simples Nacional](https://www8.receita.fazenda.gov.br/SimplesNacional/Default.aspx), use its authorised Simples service access or e-CAC/gov.br with the correct CNPJ representation, then **Cálculo e Declaração → PGDAS-D e DEFIS**. Follow the current access controls; the cited2025 manual's screen labels are guidance, not a claim that login screens were tested live. [manual §3](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

1. Confirm **Regime de Apuração → Optar/Consultar** for the correct year, preserving the annual irrevocable cash/accrual record. The manual specifies the November computation for an existing optant's following-year choice and distinct opening-month/November/December cases. [§5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
2. Choose **Declaração Mensal → Declarar/Retificar**, enter month/year and whole-company earned revenue separated domestic/export. Cash optants also enter received revenue. Complete a zero-revenue month with zero; inactivity does not remove the monthly duty. [§§6.1,6.4](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
3. For each establishment select actual **Atividades** and enter segregated activity revenue. Use the correct ISS municipality and supported qualifications for ST/monophase, retention, suspension, immunity or local relief. A court suspension requires its actual process, not an unchecked reason code. [§§6.5–6.6](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).
4. Check **Resumo da Declaração no Simples Nacional – Valor Devido por Tributo**, then **Transmitir**. Save **Imprimir Recibo** and the submitted declaration. **Gerar DAS** for that PA, continue/check summary, save the PDF and pay through the authorised facility. Keep proof of payment separately. Previously declared outstanding debts may need **Débitos → Consultar/Gerar DAS** so partial payments, offsets and transfers are recognised. [§§6.7–6.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

**Annual DEFIS.** In the same application use **DEFIS → Acessar DEFIS**; choose year and Original/Retificadora, with normal/special event and date only when applicable. Complete missing monthly declarations first. Enter company and establishment economic/fiscal data, owner income and the actual inactivity answer; zero revenue is not itself proof of no patrimonial movement. Use **Salvar Dados → Verificar Pendências → Transmitir → Gravar Recibo/Imprimir**. Correct a false special-event declaration through the manual's actual rectification route because it can block subsequent periods. No annual tax payment is proved merely by transmitting DEFIS. [manual §§9.2–9.8](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

**MEI.** Use the Portal's **PGMEI → Emitir Guia de Pagamento (DAS)**, enter CNPJ/year, select PA, choose **Apurar/Gerar DAS → Imprimir/Visualizar PDF**, check the amount/date and pay with separate proof. It remains monthly even without revenue and includes the opening and closing month. Use **Serviços Públicos → DASN SIMEI – Declaração Anual para o MEI** for the annual return. Enter CNPJ, year and original/rectifying normal/special status; complete missing prior returns and PGMEI assessments. Enter **Receita de comércio e indústria**, **Receita de prestação de serviços** and employee answer. Check automatically totalled gross revenue, assessed/paid monthly amounts and any excess; choose **Transmitir**, retain receipt and any excess DAS or MAED/DARF. A DASN is a declaration, not a monthly payment channel. The cargo case also checks exclusive occupations and the compatible contribution. [DASN manual §§2–4.9](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf); [PGMEI manual](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf).

**First-semester2027 regular IBS/CBS record.** For an existing optant, the published manual routes from the Portal's **Opção pelo regime regular de IBS e CBS** or the [consumption portal](https://consumo.tributos.gov.br/) **Escolher Regime de Apuração IBS/CBS**. Use authorised gov.br representation of the CNPJ, verify the displayed entity, **Solicitar Opção**, acknowledge and confirm, then save result PDF and history/effective date. New companies use MAT's actual route; the October manual says later MAT instructions were still to follow, so do not invent those screens. During the published cancellation window, inspect the actual option card/history, cancel only if authorised and retain the receipt; cancellation is irreversible for that semester. [regular-option manual §§3–4](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf).

## Penalties and interest

Monthly PGDAS-D late/omitted information is subject to LC123art.38-A:2% per calendar month or fraction from the day after the original filing deadline, capped at20% of the declared taxes even if paid; minimum50 per reference month. Incorrect/omitted information has20 per group of10. Subject to the statutory minimum, penalties reduce to half before an official procedure or to75% when filed within an intimation's deadline. A technically nonconforming declaration can be treated as not filed, with the prescribed10-day replacement notice. The2025 PGDAS manual's old “April of next year” starting clock is outdated; the current statute and October2026FAQ6.5 control. [LC123art.38-A](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [FAQ6.5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf).

DASN-SIMEI lateness generates the applicable MAED notice/DARF, ordinarily2% per month/fraction capped20%, with50minimum; use the notice and legally applicable reductions rather than assuming the DAS balance contains the filing penalty. The manual separates assessment, late-payment charges and notice. The current October2026FAQ6.12 confirms a DEFIS late penalty from calendar2026, notified through Caixa Postal rather than automatically launched; the older manual’s “no fine” statement is obsolete. The precise current art.97-A amounts/reductions remain unconfirmed because its operative consolidated text was inaccessible. Likewise calculate late DAS interest/charges through the actual current authorised debt document, not an invented all-in rate. [DASN manual §4.9](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf); [LC123arts.21§3,38–38-B](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html).

## Cross-border points

Owner domicile and foreign structures can defeat eligibility even when sales are entirely Brazilian. Domestic/export ceilings are separate; service exports require the actual foreign recipient/payment/result conditions, not simply a foreign currency bank credit. Segregation may remove particular export-tax components while preserving other DAS taxes and the appropriate rate history. Foreign goods/services imports and their outside-DAS taxes require separate analysis under art.13§1. [LC123arts.3§14,13,17II,18§4](https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html); [manual §§1.5,6.5](https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf).

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

- What are the CNPJ, legal/ownership structure, owner domicile, opening date, establishments, actual election status and notified effective dates?
- What were earned domestic/export revenues by month for the prior/current years and prior12months, received amounts, cancellations/returns and underlying marketplace/invoice records?
- Which actual goods/services and contracts/CNAEs establish the annex or exact permitted MEI occupation, with local location, ST, monophase, retention and export evidence?
- What paid payroll, pró-labore, thirteenth salary, actual CPP and FGTS support factorR, and were employee/MEI conditions met?
- What PGDAS-D/PGMEI, DEFIS/DASN, DTE notices, debt/registration regularisation, declarations and payments already exist, and what2027 option/cancellation receipt governs?

Preserve a workpaper with identification/election, earned/received and domestic/export revenue reconciliations, annex lines, factorR numerator/denominator, current/prior-year ceiling tests and effective dates, DAS components, outside-DAS liabilities, prior payments, declarations/receipts and reviewer flags. Banco do Brasil, Caixa, Itaú, Bradesco, Santander, Nubank, Inter and C6 names and supplied CSV/PDF/OFX columns must be inspected rather than assumed compatible. Bank names, PIX, NF-e, NFS-e, marketplace, own-transfer, DAS, DAS-MEI, DASN, INSS and “ICMS/ISS fora Simples” descriptors are search clues; classify from the evidence. If an input is absent, continue supported ordinary work and mark that calculation conditional. Escalate the actual disputed eligibility, occupation, exclusion or special local rule with its documents; do not reject all ordinary reform questions or invent a default.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| LC123 current consolidation: arts.3,13,16–18-F,19–20,23–26,38–38-B and all2026 AnnexesI–V; later-effect amendments distinguished | https://www2.camara.leg.br/legin/fed/leicom/2006/leicomplementar-123-14-dezembro-2006-548099-normaatualizada-pl.html |2026-11-11|
| LC238 arts.2–10 complete act:2027/2028 commencement, budget conditions, employees and remission scope read | https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-238-21-outubro-2026-800071-publicacaooriginal-181678-pl.html |2026-11-11|
| Decree12797 art.1 complete act:2026minimum wage read | https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12797-23-dezembro-2025-798569-publicacaooriginal-177587-pe.html |2026-11-11|
| Lei8212: arts.21–22, ordinary MEI contribution and separate employer-base conditions read | https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html |2026-11-11|
| PortariaCGSN54 official2026sublimit notice, read for all-state2026amount | https://www8.receita.fazenda.gov.br/SimplesNacional/Noticias/NoticiaCompleta.aspx?id=94c10cc2-7eb5-4ef0-bfb2-5479e72caff8 |2026-11-11|
| PGDAS-D/DEFIS manual17June2025:§§1.4–1.5,3,5–6,8–8.2,9selected workflow pp82–86,89–91,100–102 read; its obsolete MAED clock and DEFIS no-penalty statement not adopted | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGDAS-D_2018_V4.pdf |2026-11-11|
| CGSN FAQ partially updated9October2026: eligibility/limits,5.3–5.4,5.24,6.4–6.12,7.5note2 read; reform section warns incomplete, old election timetable displaced by current notice/manual | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/PerguntaoSN.pdf |2026-11-11|
| DASN-SIMEI manualSeptember2024: definitions, all ordinary filing/excess/late-declaration workflow§§1–4.9 read; historical limits separated | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual_DASN-SIMEI.pdf |2026-11-11|
| Official AnnexXI occupation PDF: read for table framework and occupation/CNAE/ISS/ICMS columns read; actual taxpayer occupation must be matched | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Anexo_XI.pdf |2026-11-11|
| PGMEI manual19November2025:§§1–4.2 and4.7 ordinary assessment/payment and full-month benefit adjustment read; no live portal access claimed | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_PGMEI_2018.pdf |2026-11-11|
| LC214 current with LC227:arts.41,47–48,348,517,544 read, credit/semester/effective-date conditions | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm |2026-11-11|
| JointAct4 art.1 complete signed act: Simples document start and exceptions read | https://cgibs.gov.br/upload/arquivos/202607/31091735-20260730-16h30-ato-conjunto-rfb-cgibs-na-c2-ba-4-260731-090909.pdf |2026-11-11|
| CGIBS30September2026 whole notice read for first-semester2027 option deadlines | https://cgibs.gov.br/embora-os-periodos-sejam-parecidos-tratam-de-escolhas-diferentes-por-isso-e-importante-entender-cada-situacao |2026-11-11|
| Regular IBS/CBS option manual7October2026 complete14pages read: access, representation, choice, receipt, history/cancellation and then-incomplete later MAT instructions | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/Manual%20op%C3%A7%C3%A3o%20regime%20regular%20IBS%20e%20CBS%20no%20Simples%20Nacional.pdf |2026-11-11|

Not yet confirmed: the current complete CGSN140 consolidated act and the original CGSN194/195 instruments could not be read through the legacy/SPA route or normal-browser fallback. No unsupported statement that every unregulated activity qualifies for MEI, or generic IT consultancy qualifies, is adopted. The taxpayer's exact AnnexXI occupation and full current electronic-document exceptions, precise current post-reform DEFIS penalty amounts/reductions, event-specific local relief/substitution rules, disaster extensions and any updated post-October MAT screens need their actual current instrument. Later MEI expansion still needs the budget condition for the relevant year. No live return was prepared, transmitted or accepted by this Guide.

Visit [OpenAccountants](https://openaccountants.com) to browse Guides, sign in, request professional review and follow updates. Check the version, date and approval displayed there; this draft does not claim to be the platform’s current verified version.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `br-simples-nacional` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/br-simples-nacional. If neither is available, confirm every figure against the official source pages cited above before relying on it.
