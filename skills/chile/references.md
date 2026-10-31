---
name: chile-references
jurisdiction: CL
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Chile — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## LibreDTE/libredte-lib-core

- Repository: [LibreDTE/libredte-lib-core](https://github.com/LibreDTE/libredte-lib-core)
- License: AGPL-3.0
- Language: PHP
- Stars: 216
- Scope: Core PHP library for Chilean electronic invoicing (DTE) via SII. Contains authoritative SII classification codes for document types (`tipos_documento.php`), additional taxes and withholdings (`impuestos_adicionales_retenciones.php`), customs codes, payment methods, and commune data. The tax rate constants include IVA retention rates by product category (ganado 8%, trigo 4%, arroz 10%, etc.), excise taxes on alcohol (licores 31.5%, vinos 20.5%, cervezas 20.5%), beverages (analcohólicas 10%, azucaradas 18%), and full DTE document type mappings (factura afecta 33, boleta 39, nota de crédito 61, exportación 110, etc.).
- Integration: Same license (AGPL-3.0). SII tax codes, withholding rates, and document type classifications directly incorporated into `chile-iva.md`.

## LibreDTE/libredte-app-community

- Repository: [LibreDTE/libredte-app-community](https://github.com/LibreDTE/libredte-app-community)
- License: AGPL-3.0
- Language: PHP
- Stars: 38
- Scope: Community edition web application for Chilean electronic invoicing. Built on `libredte-lib-core`. Provides a full SII-integrated invoicing workflow including Formulario 29 generation, libro de compras/ventas, and DTE management.
- Integration: Same license. Reference implementation for SII workflow and validation rules.

## grblasquiz/hacecuentas

- Repository: [grblasquiz/hacecuentas](https://github.com/grblasquiz/hacecuentas)
- License: check
- Language: TypeScript/JSON
- Scope: Chilean net salary calculator (Calculadora de Sueldo Líquido Chile 2026). Contains Impuesto Único de Segunda Categoría (IUSC) progressive brackets in UTM (same 0%–40% structure as IGC in UTA), AFP commission rates for all seven AFPs (Uno 0.49%, Modelo 0.58%, PlanVital 1.16%, Habitat 1.27%, Capital 1.44%, Cuprum 1.44%, ProVida 1.45%), Fonasa/Isapre health deduction rules, and Seguro de Cesantía rates. Data sourced from SII and Superintendencia de Pensiones.
- Integration: Cross-validation source for IUSC brackets and AFP rates incorporated into `cl-income-tax.md`.

## efeoncepro/greenhouse-eo

- Repository: [efeoncepro/greenhouse-eo](https://github.com/efeoncepro/greenhouse-eo)
- License: check
- Language: Markdown
- Scope: Chilean payroll compliance audit reference. Contains detailed Chile payroll law documentation including IUSC tax table formulas, AFP/pension contribution rules (10% mandatory + commission), Seguro de Cesantía rates by contract type (indefinido: worker 0.6% / employer 2.4%; plazo fijo: worker 0% / employer 3%), gratificación legal calculations, and boleta de honorarios retention rate (15.25% for 2026). Cites SII, Dirección del Trabajo, Superintendencia de Pensiones, AFC, and PREVIRED as primary sources.
- Integration: Cross-validation source for withholding rates and payroll deduction rules.

## rcaurasma/nuam-node-react

- Repository: [rcaurasma/nuam-node-react](https://github.com/rcaurasma/nuam-node-react)
- License: check
- Language: JavaScript
- Scope: Implementation of SII Declaraciones Juradas 1922/1949 factor definitions. Contains factor labels for IDPC credits (generated pre/post 2017), RAP register, ISFUT, and dividend distribution classifications used in Operación Renta.
- Integration: Reference for DJ factor definitions relevant to corporate/dividend income tax reporting.

## UBIOBIO-OpenSource/remusystem

- Repository: [UBIOBIO-OpenSource/remusystem](https://github.com/UBIOBIO-OpenSource/remusystem)
- License: check
- Language: Java
- Stars: 1
- Scope: Open-source payroll system (sistema de remuneraciones) built to Chilean labor legislation. Contains Impuesto Único de Segunda Categoría computation logic.
- Integration: Reference implementation for Chilean payroll tax computation.

## nicsoto/ArriendoFacil

- Repository: [nicsoto/ArriendoFacil](https://github.com/nicsoto/ArriendoFacil)
- License: check
- Language: JavaScript
- Scope: Chilean rental property management tool with tax summary features. Implements DFL-2 exemption logic (first 2 qualifying properties exempt from rental income tax), Impuesto Global Complementario references for rental income, and Formulario 22 integration guidance.
- Integration: Reference for Chilean rental income tax treatment and DFL-2 rules.

## MilkoYunusic/Stock-Options-RSU

- Repository: [MilkoYunusic/Stock-Options-RSU](https://github.com/MilkoYunusic/Stock-Options-RSU)
- License: check
- Language: HTML
- Scope: Chilean tax guide for stock options and RSU compensation. Covers IGC treatment of exercise/vesting gains, DJ 1929 employer reporting obligations, and non-resident employer scenarios.
- Integration: Reference for stock compensation income tax treatment under Chilean law.

---

## Authoritative Government Sources

| Source | URL | Data Used |
|---|---|---|
| SII (Servicio de Impuestos Internos) | https://www.sii.cl | IGC/IUSC brackets, UTA/UTM values, DTE rules, Formulario 22/29 |
| SII — IUSC tables | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/ | Monthly withholding tax brackets |
| SII — UTA/UTM values | https://www.sii.cl/valores_702/utm_uta_702.html | Tax unit values for bracket computation |
| Superintendencia de Pensiones | https://www.spensiones.cl | AFP commission rates, pension contribution rules |
| Dirección del Trabajo | https://www.dt.gob.cl | Labor law, gratificación, employment contracts |
| AFC Chile | https://www.afc.cl | Seguro de Cesantía funding and rates |
| PREVIRED | https://www.previred.com | Previsional indicators, cotización tracking |
| Superintendencia de Salud | https://www.supersalud.gob.cl | Fonasa/Isapre health contribution rules |
