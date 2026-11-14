---
name: ni-tax-overview
description: "Use this skill for a first map of the Nicaragua tax system in 2026 and to route a question to the right Nicaragua skill. It names the authority (DGI), the calendar fiscal period, the headline figures with their official sources (employment income scale exempt to C$100,000 then 15% to 30%; business income 30% or the pago minimo definitivo of 1%, 2% or 3%; IVA 15%; capital income and gains 15%; non-residents 20%; tax havens 30%; INSS 7% employee and 21.5% or 22.50% employer), the main deadlines and which skill owns each job. Trigger phrases include impuestos Nicaragua, DGI, Ley 822, Ley de Concertacion Tributaria and what taxes apply in Nicaragua."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ni-tax-overview"
  jurisdiction: "NI"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nicaragua tax overview, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. "NI" here is Nicaragua.

## Who this applies to

Anyone starting a Nicaragua question. The tax authority is the Direccion General de Ingresos (DGI); filing is through its Ventanilla Electronica Tributaria (VET). The main law is the Ley de Concertacion Tributaria (Ley 822 of 2012), reformed by Ley 987 of 2019. Currency: cordoba (C$). The fiscal period is the calendar year; DGI may authorise a special 12-month period for business income (art. 50).

| Job | Skill |
| --- | --- |
| Employment income (rentas del trabajo) | [nicaragua-income-tax](nicaragua-income-tax.md) |
| Business income, PMD, annual return | [ni-corporate-income-tax](ni-corporate-income-tax.md) |
| IVA | [nicaragua-iva](nicaragua-iva.md) |
| Employer retention | [nicaragua-payroll](nicaragua-payroll.md) |
| INSS | [nicaragua-social-contributions](nicaragua-social-contributions.md) |
| Setting up a business | [ni-company-formation](ni-company-formation.md) |

## Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Employment income scale | Exempt to C$100,000; 15%, 20%, 25%, 30% above C$500,000 | DGI FAQ, Periodo fiscal y tarifa del impuesto: https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm |
| Business income | 30% (gross income above C$12,000,000) | DGI FAQ, Liquidacion del impuesto: https://www.dgi.gob.ni/FAQ/liquidacion_del_impuesto.htm |
| Pago minimo definitivo | 3% large, 2% principal, 1% other taxpayers | La Gaceta 41 of 28 Feb 2019, Ley 987 (copy at MEM): https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf |
| Capital income and gains | 15% (10% on loans from investment-grade international banks) | same |
| Non-residents, economic activities and employment | 20% definitive | same |
| Payments to tax havens | 30% definitive | same |
| IVA | 15% | DGI FAQ, Determinacion del IVA: https://www.dgi.gob.ni/FAQ/determinacion_del_iva.htm |
| INSS integral regime | Employee 7.0%; employer 21.5% or 22.50% | INSS, Regimenes de afiliacion: https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion |

## The base

IR has three baskets: employment income (art. 23 scale), business income (30% or PMD, whichever is higher) and capital income and gains (15% definitive, kept separate except for financial institutions). IVA is charged on sales, services and imports at 15% with long exemption lists (arts. 127 and 136). Other taxes not covered: ISC, IECC fuel tax, IEFOMAV road fund tax, municipal taxes and stamp tax.

## Deadlines and filing

| Return | Deadline |
| --- | --- |
| Annual business income return | Last day of the second month after the period: 28 February 2027 |
| Employee annual return (when required) | Within 90 days after 31 December |
| Monthly advances and retentions | 15th of the following month, nil returns required |

## Penalties and interest

Codigo Tributario (Ley 562) art. 124 sanctions: fines in unidades de multa, closure, loss of benefits.

## Cross-border points

Territorial basis: income from Nicaraguan sources. Definitive retentions to non-residents: 20% general, 15% capital income, 3% insurance, transport and international telecoms, 1.5% reinsurance, 30% to tax havens. No tax treaty was confirmed in this pass.

## Two worked examples that recompute

### Example 1: dividend of C$1,000,000 to a shareholder

15% definitive retention (art. 87.2; DGI code 514/524): C$150,000 retained, C$850,000 paid.

```oa-check
name: NI 2026 dividend retention
inputs:
  dividend: 1000000
steps:
  - retention: dividend * 0.15
  - net: dividend - retention
expected:
  retention: 150000
  net: 850000
```

### Example 2: service from a foreign provider in a tax haven or not (decision)

A Nicaraguan company pays C$500,000 for consulting by a non-resident. If the provider is not in a tax haven, 20% definitive retention: C$100,000. If it is resident in a tax haven, 30%: C$150,000. Check the provider's residence before contracting; the C$50,000 difference is a real cost if the provider grosses up.

```oa-check
name: NI 2026 non-resident service, tax haven or not
inputs:
  fee: 500000
steps:
  - retention_general: fee * 0.20
  - retention_haven: fee * 0.30
  - difference: retention_haven - retention_general
expected:
  retention_general: 100000
  retention_haven: 150000
  difference: 50000
```

## Ask the client first

1. Individual or company; resident or not?
2. Income type: employment, business, capital?
3. DGI classification and regime (general, cuota fija, large or principal taxpayer).
4. Employees and INSS registration.
5. Payments abroad.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI FAQ, Periodo fiscal y tarifa del impuesto: art. 23 scale | https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm | 2026-11-14 |
| Read for DGI FAQ, Liquidacion del impuesto: 30% rate, C$12,000,000 threshold, period | https://www.dgi.gob.ni/FAQ/liquidacion_del_impuesto.htm | 2026-11-14 |
| Read for Ley 987 (La Gaceta 41, 28 Feb 2019): arts. 24, 49, 53, 61, 69, 87, 127, 136 | https://www.mem.gob.ni/wp-content/uploads/2023/08/2019.02.28-Ley-987-Reforma-a-Ley-822-G-41.pdf | 2026-11-14 |
| Read for DGI FAQ, Determinacion del IVA: 15% | https://www.dgi.gob.ni/FAQ/determinacion_del_iva.htm | 2026-11-14 |
| Read for INSS, Regimenes de afiliacion | https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion | 2026-11-14 |
| Read for DGI catalogue of retention codes and rates, Aviso 005-01-2024 | https://www.dgi.gob.ni/pdfNoticia/3175 | 2026-11-14 |

Not yet confirmed: tax treaties; municipal taxes; any tax reform after Ley 987 of 2019.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ni-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ni-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
