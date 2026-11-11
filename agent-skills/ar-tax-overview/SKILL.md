---
name: ar-tax-overview
description: "Route an Argentina tax question for fiscal year 2026 to the correct Guide. Use for Ganancias, IVA, Monotributo, payroll, autonomos, corporate tax, residence, foreign payments, transfer pricing, company formation and Bienes Personales screening. Establish taxpayer, residence, activity, period and province before selecting a computation. This overview carries no independent rates or filing-calendar table: load the owning Guide and its dated official sources. Provincial/municipal taxes and personal-assets computations require additional current official sources. The output is a routing and missing-evidence checklist for professional review."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-tax-overview"
  jurisdiction: "AR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Argentina: tax overview 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

**Quick answer:** select the taxpayer and tax job first, then load its current Guide. Argentina has national, provincial and municipal obligations; a federal return does not settle the other layers. Work in Argentine pesos (ARS) and retain original-currency evidence where relevant. This is a Tier 2 source-cited routing draft without professional approval.

1. Obtain CUIT, individual/entity form, residence and movement history, activity, fiscal opening/closing dates, transaction/payment dates and each province/municipality of operation. LIG arts. 1 and 24 distinguish resident worldwide income, non-resident Argentine-source income, the individual's calendar year and business attribution to the relevant annual commercial period. Do not assume every company uses the calendar year or that every foreign payer creates foreign-source income.
2. For a small individual business, load [Monotributo](ar-monotributo.md) to test eligibility before choosing the general regime. Its period-specific category table owns the indexed small-business limits. A company's legal form alone is not a substitute for classification.
3. For general-regime individual income, load [individual income tax](argentina-income-tax.md). It owns personal rates, bands, allowances, income categories, credits and filing. For employee withholding, load [payroll](argentina-payroll.md); ordinary monthly, annual and final parameters differ. Do not copy a payroll table into an annual self-employed computation.
4. For a company's income-tax base, indexed corporate bands, loss/inflation reconciliation, advances or annual return, load [corporate income tax](ar-corporate-income-tax.md). Its opening-year scale and separate F.713/PUB obligations replace the old overview's approximate filing-month/June-extension assertion.
5. For transaction classification, output/input IVA and imported-service issues, load [IVA computation](argentina-iva.md); for the monthly return, load [IVA filing](ar-vat-return.md). The owning Guides distinguish ordinary, reduced and increased treatment, exemptions and exports. Monotributo thresholds belong to its own Guide, not an invented general IVA registration threshold.
6. For personal autonomous or employer/employee social contributions, load [social contributions](ar-social-contributions.md). A personal autonomous payment does not settle employer obligations. Payroll income-tax withholding is a separate computation.
7. Resolve residence, source, permanent establishment, outbound beneficiary withholding, treaty documentation and foreign-tax-credit screening with [cross-border](argentina-cross-border.md). Add [transfer pricing](argentina-transfer-pricing.md) for related parties or statutory non-cooperative/low-tax cases; taxpayer fiscal opening determines the applicable documentation regime.
8. For SA/SRL/SAS and foreign-entity registration, load [company formation](ar-company-formation.md). Separate registry, national tax, provincial and employer registrations. For Ingresos Brutos/municipal charges, identify the actual jurisdictions and obtain their current codes, activity classifications and applicable interjurisdictional rules; no nationwide approximate rate range is supplied.
9. Screen personal-assets exposure separately. ARCA's Bienes Personales overview identifies an annual asset tax with domestic and, depending on the case, foreign assets. This pack does not supply its current minimum, rates, valuation, REIBP effects or substitute-taxpayer calculation. Stop that computation and obtain its current primary texts rather than importing income-tax residence or assuming every asset is taxable.
10. National administration is ARCA, created by Decreto 953/2024 arts. 1-2 following AFIP's dissolution. Legacy forms/URLs can still say AFIP; match the current rule and period, not the logo. Hand off the chosen Guides, actual facts, source-period dates and unresolved items. A Guide's tax year is not professional approval.

## When to refuse or refer

Refer missing province/municipality, disputed residence, special industry/promotion/gaming, reorganisations, complex financial instruments, provincial pension funds, assets-tax/REIBP and unsupported historic periods to the appropriate current official material and qualified professional. These are scope boundaries, not exemptions. Do not give a filing-ready answer while the controlling taxpayer, period, source or transaction classification is missing.

The old overview's personal/corporate/IVA rate topics are retained through the owning Guides above, avoiding competing rate tables. Its approximate provincial range and general annual-extension statement were not established from primary text and are not repeated as facts. Tax thresholds change under different mechanisms; do not assume every tax is indexed in the same month or by the same index.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for residence/source and individual/business period attribution: LIG arts. 1, 24, 53, 73; quotation: "Los no residentes tributan exclusivamente" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for authority succession: Decreto 953/2024 arts. 1-2; quotation: "Créase la AGENCIA DE RECAUDACIÓN Y CONTROL ADUANERO" | https://www.argentina.gob.ar/normativa/nacional/decreto-953-2024-405666/texto | 2026-11-11 |
| Read for assets-tax screening only, opening definition; quotation: "bienes situados en el país y en el exterior"; no threshold or rate is used | https://www.arca.gob.ar/gananciasYBienes/bienes-personales/default.asp | 2026-11-11 |

Not yet confirmed: current provincial/municipal rates and procedures; complete Bienes Personales/REIBP and substitute-taxpayer rules; the old unsupported nationwide provincial rate range and blanket June extension. Use the owning Guide's current official source for every rate, deadline and computation; this router establishes none independently.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
