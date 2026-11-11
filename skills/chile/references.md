---
name: chile-references
jurisdiction: CL
category: orchestrator
tax_year: 2026
last_updated: 2026-11-11
version: 1.1
type: router
description: >
  Chile source-routing catalog for 2026 tax and payroll research. Directs income tax, company tax,
  VAT/DTE, payroll, independent contributions and corporate declarations to the owning Guides and
  original SII, pension, labour, health and current LeyChile sources. Retains the legacy project links
  solely as optional engineering references, with their former topic labels separated from verified law.
  Trigger on Chile tax sources, SII reference, DTE format, Formulario 29, F22, DJ, AFP source,
  payroll reference and open-source Chile accounting projects. Contains no duplicated operative tax
  rates or filing deadlines. Excludes code licensing approval, validation of third-party calculations,
  unverified project integration and complete specialist DFL-2 or equity-compensation advice.
tier: 2
domain: income-tax
---

# Chile: primary tax sources and optional engineering references, 2026 v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Use the owning Chile Guide and the actual official original for a tax figure. This catalog helps locate those sources; a third-party application's constants, stars, claimed tax compliance or source links do not independently establish the law. The legacy project identities remain below so engineering research is not lost. Their old tax numbers are not carried into a second operative rate table.

## Ask the client first

1. Which income/payment year, return period or dated contribution month is being researched?
2. Is the job legal research, a tax calculation, a filing or implementation of a technical document format?
3. Which taxpayer, income category, regime and document/return are involved?
4. Is there an actual source provision, current official table, project commit or failure to reproduce?
5. Does the question require specialist DFL-2, equity-compensation, customs, industry withholding or corporate-register treatment?
6. If code will be reused, which exact version, files and licence govern the proposed use?

## The method, step by step

1. **Load the owner first.** Use [cl-tax-overview](cl-tax-overview.md) for intake/routing; [cl-income-tax](cl-income-tax.md) for individual tax and F22; [cl-corporate-income-tax](cl-corporate-income-tax.md) for company profit, distributions and records; [cl-vat-return](cl-vat-return.md) for IVA/F29/DTE; [cl-payroll](cl-payroll.md) for employee pay; [cl-social-contributions](cl-social-contributions.md) for independent contributions. Read each owner's scope and unconfirmed items. A link does not mean every specialist topic is fully covered.
2. **Choose the right original.** Use the dated SII table or instruction for the applicable period and the law/version in force. For LeyChile use the current JSON route, read metadata and all nested article text, and check transitory commencement. Do not rely on an export that silently supplies a future version or stops halfway through an article. [cl-cross-border](cl-cross-border.md), [cl-transfer-pricing](cl-transfer-pricing.md) and [cl-company-formation](cl-company-formation.md) own those separate workflows.
3. **Keep legal, technical and operator evidence distinct.** SII technical DTE specifications describe a document format; they do not establish every tax rate in an implementation. SP is the pension regulator; AFC is the unemployment-insurance scheme operator. PREVIRED is an operational payment provider, not a government tax-law source. Use the competent regulator and actual law for the rule, then the current operator workflow for payment evidence.
4. **Retain a research record.** Record the precise official URL, act/article or table, period/version, short exact original-language words and date read. Check neighboring exceptions and effective dates. A project file can help identify a question, but replace its asserted tax authority with the primary text before calculating.
5. **Bound the answer.** Return the selected owner/source, the question it actually answers and unresolved specialist facts. Do not describe this catalog as a completed tax calculation, successful filing, code audit or licence clearance. Obtain actual acknowledgements and case-specific professional review through the owning workflow.

## Optional engineering references retained from the earlier catalog

These are repository-author sources for project identity only. They are not tax-law authorities or proof that the software currently implements the listed legacy research topics correctly. No popularity, language, licence-compatibility, reuse permission or integration assertion is made. Open the actual project revision and licence before considering reuse; the former blanket statement that all projects have compatible open-source licences was unsupported and must not be used.

| Repository-author link | Legacy research topics retained and their destination |
|---|---|
| [LibreDTE/libredte-lib-core](https://github.com/LibreDTE/libredte-lib-core) | DTE type mappings, additional tax/withholding classifications, customs codes, payment methods and communes: begin with the official SII DTE route and VAT owner. Product-specific IVA withholding (ganado, trigo, arroz), alcohol/beverage excise (liquors, wine, beer, non-alcoholic and sugary beverages) and customs classifications require their current original instruments; a library constant is not confirmation. |
| [LibreDTE/libredte-app-community](https://github.com/LibreDTE/libredte-app-community) | DTE management, F29 and purchase/sales records: route to SII and the VAT owner. Any dependency on the core library, workflow completeness and actual integration must be checked in the selected project version. |
| [grblasquiz/hacecuentas](https://github.com/grblasquiz/hacecuentas) | Net salary, IUSC, AFP, health and unemployment deductions: official SII/SP/health routes and payroll owner. The earlier AFP commission constants are not reused as current rates. IUSC monthly and IGC annual unit treatment must be checked in their own tables. |
| [efeoncepro/greenhouse-eo](https://github.com/efeoncepro/greenhouse-eo) | Payroll audit, pension, unemployment by contract, gratificación and honorarios: official SP/DT/SII sources and owning payroll/contribution Guides. This project must not be assumed open source or compatible merely because its repository is readable. |
| [rcaurasma/nuam-node-react](https://github.com/rcaurasma/nuam-node-react) | Corporate DJ 1922/1949 factor labels, subject to the actual filer and AT instructions, credit vintages, RAP, ISFUT and distribution classifications: use the actual SII form/instructions for the relevant AT and corporate owner. Detailed special-register treatment remains a source-required specialist question. |
| [UBIOBIO-OpenSource/remusystem](https://github.com/UBIOBIO-OpenSource/remusystem) | Salary/payroll implementation and IUSC computation: current SII monthly table and payroll owner. No software output is certified by its project name or this link. |
| [nicsoto/ArriendoFacil](https://github.com/nicsoto/ArriendoFacil) | Rental income, DFL-2 and F22: individual owner for ordinary income; DFL-2 property eligibility, acquisition/ownership restrictions and exemption limits require a full current specialist source check. The earlier simplified property-count assertion is not an operative rule here. |
| [MilkoYunusic/Stock-Options-RSU](https://github.com/MilkoYunusic/Stock-Options-RSU) | Options/RSU exercise or vesting, IGC, foreign employers and DJ reporting: individual/cross-border owners for their stated portions and a specialist source check for equity awards. The earlier association of DJ 1929 with all employer equity reporting is not confirmed; choose the actual form from SII's instructions. |

The earlier “incorporated into” and “cross-validation” statements do not establish that any current Guide or software passed an integration audit. The duplicate legacy `chile-iva.md` is not the current VAT owner. All former tax topics above retain a destination or explicit source-required boundary; none should be inferred from an unverified code constant.

## When to refuse or refer

Refer source text that is unavailable, truncated or not yet in force; conflicting effective dates; a software output with no reproducible source/version; specialist DFL-2, equity, excise/customs or corporate-register questions not established by the owning Guide; and proposed reuse without the actual licence. Do not replace any missing legal check with a repository's stars, marketing claim or a prior-year table.

AFC remains an operator route at https://www.afc.cl. PREVIRED remains a private operational provider at https://www.previred.com; direct access was blocked during this check, so no current operator screen or payment acceptance is certified. Their appearance here does not put them in the government-source table or make a private indicator an official legal rule.

## Sources

The catalog identifies the portions actually read on 11 November 2026. A technical title or catalog entry is not a claim that every linked instruction or field was audited. Dated annual pages concern their named tax year; they do not establish a future year's calendar.

| Primary source / route and portion read | What to use it for and limits | Official URL | Read on |
|---|---|---|---|
| SII monthly IUSC tables, 2026 page, read for the scope in the next column | Monthly salary-table source, choose the actual month; use the payroll/income owner for the computation | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm | 2026-11-11 |
| SII UTM/UTA 2026 table, read for the scope in the next column | Dated indexed units; UTM, UTA and daily UF are distinct, use the rule's required unit/date | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |
| SII DTE format document, title and contents only | Technical format orientation; this older specification alone does not prove a current schema, code/rate list or accepted production workflow | https://www.sii.cl/factura_electronica/factura_mercado/formato_dte.pdf | 2026-11-11 |
| SII F29 FAQ, read for the scope in the next column | Monthly-tax form identity and route, not a blanket deadline for every taxpayer | https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_1060.htm | 2026-11-11 |
| SII boletas de honorarios portal, read for the scope in the next column | Official independent-receipt/withholding starting point; detailed conditions stay in the owners | https://www.sii.cl/destacados/boletas_honorarios/ | 2026-11-11 |
| SII AT 2026 declaraciones juradas catalog, read for the scope in the next column | Actual form/instruction lookup for its named AT, including corporate reporting; not the unconfirmed AT 2027 calendar | https://www.sii.cl/ayudas/ayudas_por_servicios/2120-formularios_y_plazos_2026-2171.html | 2026-11-11 |
| SP AFP system, read for the scope in the next column | Pension/AFP source route; never substitute a salary application's commission constants | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9897.html | 2026-11-11 |
| SP employer contribution information, read for the scope in the next column | Employer obligations and current stage, read with the effective law and payroll owner | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10906.html | 2026-11-11 |
| SP independent workers, read for the scope in the next column | Annual versus monthly contribution distinctions and independent-worker workflow | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9913.html | 2026-11-11 |
| SP 2026 contribution ceiling publication, read for the scope in the next column | Dated ceiling source; actual January and later-month treatment belongs in the contribution owner | https://www.spensiones.cl/portal/institucional/594/w3-article-16921.html | 2026-11-11 |
| SP Seguro de Cesantía, read for the scope in the next column | Regulator's unemployment-insurance route, distinguished from AFC's operator workflow | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9894.html | 2026-11-11 |
| Dirección del Trabajo, read for the scope in the next column | Official labour-law/employment route | https://www.dt.gob.cl/portal/1626/w3-channel.html | 2026-11-11 |
| DT gratificación topic, read for the scope in the next column | Starting point for legal profit-sharing questions; actual statutory conditions belong in payroll | https://dt.gob.cl/portal/1628/w3-propertyvalue-22107.html | 2026-11-11 |
| Superintendencia de Salud, read for the scope in the next column | Official health-regulator route; old supersalud root redirects to this host | https://www.superdesalud.gob.cl/ | 2026-11-11 |
| LeyChile current LIR JSON | Current statute/version route, used with its transitory law, not a future export | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368 | 2026-11-11 |


Not yet confirmed: project-version-specific features, licences and compatibility, any claimed incorporation into existing Guides, current code/production-schema completeness, sector withholding/excise/customs classifications, detailed RAP/ISFUT and DJ factor rules, specialist DFL-2 and equity-award treatment, and operator screens not actually read. Tax figures and deadlines must come from the current owner and primary original, not this catalog.
