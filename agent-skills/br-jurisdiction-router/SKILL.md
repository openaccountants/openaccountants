---
name: br-jurisdiction-router
description: "Identify the relevant Brazilian taxing authority and regional rule before loading a computation or filing Guide for calendar 2026. Distinguishes federal taxes, state and Federal District taxes, municipal taxes, shared IBS administration, statistical macroregions, development-agency territories, free trade areas and the establishment relevant to regional payroll. Use for Brazil state tax, município, UF, Brasília, Distrito Federal, Northeast incentives, Manaus, multistate sales, municipal services and regional payroll. Produces the smallest necessary set of national and local owners, with separate location facts for each taxable event. It carries no substitute rate table and does not infer that every local product, property or incentive regime has been researched."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/br-jurisdiction-router"
  jurisdiction: "BR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Brazil: choose the authority, territory and regional Guide v0.1

**Built from the law. Not yet approved.** Brazil's country name alone does not select the local rule. Identify the event and its legally relevant locations, then load the national method and the applicable local profile. This Guide selects owners; it does not calculate a tax or authorise filing.

**Required inputs:** the actual transaction or employment/property event and its date; taxpayer/entity and tax regime; establishments and their UF/municipality; origin, delivery/use or performance locations where relevant; product/service/activity classification; and any claimed territorial/project authorisation. Ask only for a missing fact that can change this particular answer. One question does not require an entire client-intake exercise.

## The method, step by step

### 1. Separate the meanings of “region”

The Constitution's autonomous political units are the Union, states, Federal District and municipalities. IBGE's North, Northeast, Southeast, South and Centre-West are geographic macroregions. They are not another autonomous taxing government. An incentive's legally defined territory, a state, a municipality, an establishment and a macroregion are different fields in the workpaper ([Constitution art. 18](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html); [IBGE Grande Região definition and delimitation](https://www.ibge.gov.br/apps/quadrogeografico/pdf/qg_2024_010_GrandReg.pdf)).

Use the official [IBGE current UF data](https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome) to identify the UF code and geographic grouping. The following is a geographic index, not a table of tax jurisdictions with common rates:

| Geographic macroregion | States and Federal District in the official grouping |
|---|---|
| North / Norte | Acre AC; Amapá AP; Amazonas AM; Pará PA; Rondônia RO; Roraima RR; Tocantins TO |
| Northeast / Nordeste | Alagoas AL; Bahia BA; Ceará CE; Maranhão MA; Paraíba PB; Pernambuco PE; Piauí PI; Rio Grande do Norte RN; Sergipe SE |
| Southeast / Sudeste | Espírito Santo ES; Minas Gerais MG; Rio de Janeiro RJ; São Paulo SP |
| South / Sul | Paraná PR; Rio Grande do Sul RS; Santa Catarina SC |
| Centre-West / Centro-Oeste | Distrito Federal DF; Goiás GO; Mato Grosso MT; Mato Grosso do Sul MS |

Do not treat “Amazonas”, “Amazônia”, “Manaus”, “SUDAM area” and “a SUFRAMA free trade area” as interchangeable. Do not assume “SUDENE area” is exactly the IBGE Northeast. The [regional-incentive owner](br-regional-incentives.md) identifies the relevant law, territory, enterprise, approved project, operation and date. Constitution art. 43 authorises regional development measures subject to law; it does not award a benefit to everyone within a geographic macroregion ([art. 43](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html)).

### 2. Identify the taxing power and the job

This is a constitutional allocation and routing table. The owning Guide must still establish the actual taxable event, taxpayer, place, date, exemption, rate and procedure under operative law. A constitutional power to create a tax does not prove that a specific charge or rate applies.

| Question or event | Authority and owner to load | Boundary to retain |
|---|---|---|
| Individual income or company profit | Federal income-tax power under Constitution art. 153 III. [IRPF](br-income-tax.md), [monthly income tax](br-estimated-tax.md), [rental variants](br-carn-monthly-income-tax-rental-income.md), or [IRPJ/CSLL](brazil-corporate-tax.md) for the actual job. The contributions have their own constitutional/statutory basis | An address in a different state does not itself create a different state's IRPF bracket. Regional incentives require a separate eligibility decision. https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html |
| Goods, interstate/intermunicipal transport or communications | States/DF under art. 155 II. [ICMS/ISS/IPI national method](br-indirect-tax.md), then [state profiles](br-state-tax-profiles.md) for the actual UF/product/route | Keep internal, interstate, destination differential, FCP, substitution tax and exemptions separate. A geographic grouping can appear in a statutory route test without creating one common internal rate. Same constitutional URL as above |
| A listed service outside the ICMS allocation | Municipal taxing power under art. 156 III, with the DF exception below. [National classification/place method](br-indirect-tax.md), then [municipal profile and procedure](br-municipal-taxes.md) | Select the exact service and statutory place rule. Neither the customer's address nor the provider's preferred invoice portal alone establishes the taxing municipality. Same constitutional URL as above |
| A gift or inheritance | States/DF under art. 155 I and §1. [State profiles](br-state-tax-profiles.md) for the competent authority and evidence route | Do not substitute an ordinary ICMS rate or an income-tax capital-gains computation. Local ITCMD rates, base, exemptions, progressive treatment and foreign-event rules require their own operative provisions. Same constitutional URL as above |
| Vehicle ownership | States/DF under art. 155 III. [State profiles](br-state-tax-profiles.md) and the actual state's IPVA law/assessment | Vehicle type, relevant ownership facts, exemptions and annual procedure require their own check. A sales invoice's ICMS does not settle IPVA. Same constitutional URL as above |
| Urban property or an onerous property transfer | Municipal allocation under art. 156 I-II, with DF exception below. [Municipal property-tax branches](br-municipal-taxes.md) | Keep IPTU, ITBI and a gift/inheritance's ITCMD separate. Do not substitute the market price, registry cost or a capital-gain tax for the local tax's own base. Same constitutional URL as above |
| Rural land, imports, industrial products or financial operations | Relevant federal powers in art. 153. [Indirect-tax method](br-indirect-tax.md), [cross-border owner](brazil-cross-border-tax.md) or another actual specialist owner as appropriate | No complete rural-land return, customs valuation or every IOF branch is certified merely by identifying the federal power. Same constitutional URL as above |
| Consumption-tax transition, CBS/IBS | [Federal/dual-VAT owner](brazil-vat.md) plus [fiscal-document owner](brazil-einvoice.md). Constitution arts. 156-A and 156-B distinguish shared IBS competence and integrated administration | A national legal framework does not justify erasing the destination, entity-specific rate or transition date. Do not apply an eventual end-state system to an earlier period. Same constitutional URL as above |
| Employee salary and payroll | [Regional wage-floor selection](br-regional-payroll.md), then [national payroll](brazil-payroll.md) | Labour territory and collective-agreement coverage are separate from customer location and tax residence. The salary-input supplement does not approve the national payroll owner's later draft |
| Own-account social contributions or small-business unified regime | [INSS owner](br-inss.md) or [Simples/MEI owner](br-simples-nacional.md) | Do not apply an employee's regional wage-floor selection as an own-account contribution base, or assume every local duty disappears under the unified regime |
| Regional investment or shipment relief | [Regional-incentive owner](br-regional-incentives.md), coordinated with corporate/indirect/dual-VAT owners | Separate agency territory, project approval, enterprise/tax regime, qualifying income or goods, registration, shipment/internment evidence and the period in force |

### 3. Handle the Federal District explicitly

The Constitution prohibits dividing the DF into municipalities and attributes state and municipal legislative powers to it. Brasília is the federal capital. Do not create a fictitious “Prefeitura de Brasília” filing authority or treat an administrative region inside the DF as an autonomous municipality ([Constitution arts. 18 §1 and 32 caput/§1](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html)).

For a DF event, record DF as the federative unit and establish the relevant DF tax administration and statute through the [state](br-state-tax-profiles.md) and [municipal-equivalent](br-municipal-taxes.md) owners. A national dataset's locality label or an administrative-region name is a lookup key, not proof that municipal taxing power has been delegated to a new autonomous municipality.

### 4. Keep a separate location decision for each event

Use an event-by-event record instead of one global “client region” field:

| Event | Facts to place in the record before the owning Guide applies its law |
|---|---|
| A goods supply | Dispatch establishment, origin UF, actual delivery/destination, purchaser's relevant status, purpose, product classification and regime |
| A service | Actual provider establishment, service-list item, performance/use and customer facts relevant to the statutory place and retention test |
| A property transaction | Property location/classification, instrument, transfer type, parties, values and any capital contribution, immunity or judicial issue |
| An inheritance/gift | Asset types/locations, donor/deceased and beneficiary facts, relevant domiciles, succession/gift date and foreign connections |
| A payroll item | Establishment of assignment, employee duties/category, actual work or remote arrangement, applicable collective instrument, period, contract and public-contract conditions where relevant |
| A territorial benefit | Exact site/municipality, applicable statutory territory, project/activity/product, authorisation, qualifying operation/income, evidence and effective period |

These are research inputs, not substitute statutory place tests. One business can need federal, state, municipal, labour and incentive determinations using different location facts in the same month.

### 5. Reconcile sources and route the actual unsupported component

Open the current official statute/regulation and the relevant administrative procedure. Retain the portion read and date, and check commencement, replacement provisions, product/service definitions, exceptions and judicial decisions. A national government dataset or an official comparative table can assist identification while its reported amount remains stale or conditional. Do not label a value “confirmed” merely because its host is official.

Where a platform dataset and the law disagree, record both with their dates; identify the provision, specific activity, period and conditions that explain the difference. Distinguish a genuine change from a different service code, a benefit, an expired record, a missing value or a portal default. A blank dataset field is not an exemption or a zero rate. The [municipal owner](br-municipal-taxes.md) preserves this evidence distinction; the [state owner](br-state-tax-profiles.md) does the same for interstate lookup tables and current state law.

Load only the owners required by this question. For example, an establishment in São Paulo selling goods to a purchaser in another state does not establish that every operation uses a São Paulo internal rate. A provider in one city serving a customer elsewhere requires the actual service-place and retention test. A company operating in Manaus requires both the ordinary tax owners and proof of any particular incentive. These are routing traces, not completed tax calculations.

### 6. Produce a usable handoff

Return the identified event, period, entity/regime, UF and municipality or DF, the legally relevant location facts, owning Guide(s), actual source/date, applicability conclusion and remaining evidence. Identify a quoted local rate as provisional until the owner checks all its conditions. Preserve separate subtotals/results for supported components while isolating the unresolved one.

Do not describe a state profile, a capital-city example, a national NFS-e dataset or the existence of this router as proof that every Brazilian state/product, municipality/service, property or territorial-benefit computation is complete. Each owner retains its actual limits and `Not yet confirmed:` line. The pack README's partial entries remain until the underlying ordinary gaps close.

## When to refuse or refer

Do not certify the dependent local computation where the actual event, territory, classification, effective provision or necessary authorisation cannot be established. Continue independent supported components and state precisely which missing fact or primary source prevents the remaining result.

Refer a genuine competence dispute, conflicting assessment or court-order interpretation to an appropriately qualified professional with the official texts and the taxpayer's evidence. Refer an unsupported specialist regime to its actual source work. A geographic label or a missing profile is not itself a reason to abandon all ordinary computations.

This is a new routing job. It grants no filing/payment/election authority and no accountant approval. Keep an existing named approval bound to the text and version actually approved.

## Sources

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| Constitution, read for arts. 18, 32, 43, 145, 149, 153, 155, 156, 156-A and 156-B: federative structure, tax allocations, regional measures and integrated IBS administration | https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html | 2026-11-11 |
| IBGE current UF JSON, read for all UF names/codes and their macroregion membership; no municipal-rate or entitlement claim | https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome | 2026-11-11 |
| IBGE Grande Região reference, read for definition, non-autonomous status and geographic delimitation; historical municipality totals are not used as current counts | https://www.ibge.gov.br/apps/quadrogeografico/pdf/qg_2024_010_GrandReg.pdf | 2026-11-11 |

Not yet confirmed: no independent tax rates, deadlines or filing permissions are established by this router. The actual client's local/product/service/property classification, applicable judicial effect, territorial project authorisation and unresolved owner-level computations require the owning Guide and current official text. This routing coverage does not close any ordinary gap solely by adding a link or listing a jurisdiction.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `br-jurisdiction-router` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/br-jurisdiction-router. If neither is available, confirm every figure against the official source pages cited above before relying on it.
