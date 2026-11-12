---
name: cl-tax-overview
description: >
  Chile tax overview and routing for income year 2026, ordinarily reported in AT 2027. Establishes taxpayer,
  residence and source, calendar versus commercial and tax year, indexed UTM/UTA/UF distinctions, ordinary
  IGC top band, actual transitional company rate and VAT orientation. Directs income tax, corporate tax,
  VAT, payroll, independent contributions, transfer pricing, cross-border and formation work to the owning
  current Guides. Trigger on Chile tax overview, impuestos Chile, tax residency, UTA, UTM, Operación Renta,
  which Chile tax Guide and company versus personal tax. Includes a recomputing published-unit example;
  excludes complete return preparation, all bracket computations, special sectors and unverified treaty facts.
jurisdiction: CL
category: orchestrator
tax_year: 2026
tax_year_notes: "calendar 2026 income, ordinarily AT 2027"
last_updated: 2026-11-11
version: 0.1
type: router
tier: 2
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Chile tax overview and Guide routing, income year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Establish the income year, taxpayer, residence/domicile, income type and company regime before choosing a return. This overview routes ordinary Chilean 2026 work to its owning Guide. It carries a small orientation table, not a substitute tax computation. Calendar 2026 income is normally reported in Operación Renta AT 2027; an AT 2026 return generally concerns earlier income. Monthly VAT and payroll are separate obligations.

Chile's SII administers internal taxes and TGR handles the tax-collection role identified in the Código Tributario. The principal figures use Chilean pesos (CLP); UTM, UTA and UF are different indexed units. A bare number such as “40%” or “27%” is not an effective tax burden for every person. Source versions and transitional commencement matter: the current LIR article can already display an ultimate amended rate while a transitory provision supplies the rate for 2026 income.

## Ask the client first

1. Income/payment year and the actual return period, including any June commercial year-end or cessation.
2. Individual, company or permanent establishment; residence, domicile, entry/departure dates and foreign income.
3. Salary, honorarios, business profit, rent, gains, dividends, imports or other income/transaction type.
4. Company regime and elections, ownership and distribution history; do not infer Pro Pyme from the entity name.
5. VAT status, sales/purchases, document type, employees and independent-worker contributions.
6. SII registration, RUT, earlier filings, unpaid periods and notices already received.

## Rates, bands and thresholds

| Orientation item | Figure and conditions | Period | Official source |
|---|---|---|---|
| Calendar year and tax year | Calendar year is the twelve months ending 31 December; año tributario is the year tax or its first instalment is payable. Commercial years can differ under the statutory definition | 2026 income / ordinarily AT 2027 | [LIR art. 2 Nos. 7-9](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368) |
| General income-tax residence rule | Domiciled/resident persons: worldwide income; non-residents: Chilean-source income, subject to the law's exceptions. A foreigner establishing domicile/residence is Chilean-source-only during the first three years from entry, with possible Regional Director extension in qualifying cases | 2026 | [LIR art. 3](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368): “durante los tres primeros años contados desde su ingreso a Chile” |
| Statutory residence day test | More than 183 days, continuous or not, in any twelve-month period; domicile is a separate test, and absence alone need not end it | 2026 | [Código Tributario art. 8 No. 8](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6374); [LIR art. 4](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368) |
| Ordinary Global Complementario top marginal band | 40% on the portion above 310 UTA, not a flat rate on all income. Special art. 52 bis rules and corporate-credit effects require their own analysis | 2026 income | [LIR art. 52](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368): “exceda de 310 unidades tributarias anuales, 40%” |
| Ordinary art. 14 A company IDPC orientation | 27% for commercial-year 2026 income under the transitory rule; this is not the Pro Pyme, transparent or art. 14 G answer | 2026 income | [Ley 21.850 art. 6 transitorio](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1229250): “durante el año comercial 2026, 27%” |
| General VAT | 19% of the taxable base for transactions subject to Title II; exemptions, territorial rules, reverse-charge/withholding and special schemes must be tested separately | 2026 | [DL 825 art. 14](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6369): “una tasa de 19%” |
| UTA conversion | Last-commercial-month UTM × twelve, or the number of months in the relevant commercial year under art. 8 No. 10. Penalty UTA has its own application-date rule | 2026 | [Código Tributario art. 8 No. 10](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6374) |
| Published December 2026 UTM and UTA | CLP 72,802 UTM; CLP 873,624 UTA in SII's published 2026 table. Use the unit/date required by the particular rule, not an unrelated monthly UTA | December 2026, table read 11 November | [SII 2026 table, December row](https://www.sii.cl/valores_y_fechas/utm/utm2026.htm) |
| Ordinary annual income return timing | April in relation to preceding calendar/commercial-year income; art. 69 has June-balance, cessation, sporadic-income and other exceptions. Actual AT 2027 opening/payment/refund dates are a separate calendar | Ordinarily April 2027 for 2026 income | [LIR art. 69](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368): “presentadas en el mes de abril” |
| Ordinary monthly VAT declaration/payment rule | By the 12th of the next month under art. 64, with applicable electronic extensions and calendar rules checked in the VAT Guide; do not promise every electronic filer the 20th | 2026 monthly periods | [DL 825 art. 64](https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6369) |

The old overview's 150-UTA ordinary top-band threshold is corrected: the current ordinary art. 52 says 310 UTA. Article 52 bis contains a separate scale for specified public authorities; its 150-UTA entry must not replace the ordinary table. Likewise, the current article 20 displays 23% after Ley 21.850's amendment, but that law's sixth transitory article expressly supplies 27% for 2026, followed by later-year stages. Read both the amended text and its commencement provisions. Pro Pyme is governed separately, including Ley 21.755 art. 25; load the corporate Guide before quoting a rate to a small company.

## The method, step by step

1. **Pin down the job and period.** Separate a computation of 2026 income from a return submitted during 2026. Use LIR art. 2's calendar/commercial/tax-year distinctions. Ask for a real notice or return period when the label is ambiguous. A VAT period, employment month and annual IGC period do not become the same job because the same RUT appears on them.
2. **Establish residence and source first.** Load [cl-cross-border](cl-cross-border.md) for a move, foreign-source income, an overseas payee, treaty, foreign tax credit or permanent establishment. Count actual days and examine domicile and the foreigner's initial-period exception. A client abroad does not alone prove that a Chilean worker's income is exempt; a foreign passport does not alone establish non-residence.
3. **Route individual income.** Load [cl-income-tax](cl-income-tax.md) for salaries, honorarios, rent, gains, IGC, deductions, credits and the annual F22. Keep gross revenue, taxable base, indexed brackets, withholding and final liability separate. A marginal rate is applied only within its relevant band. Distinguish PPM and creditable advance withholding from final or sole withholding taxes; do not assume a withholding equals the final liability.
4. **Route company and shareholder work.** Load [cl-corporate-income-tax](cl-corporate-income-tax.md) for IDPC regime eligibility, base, losses, depreciation, PPM, annual returns and owner distributions. Identify the actual art. 14 regime and the income year before applying transition rates. Corporate tax and owner IGC/Additional Tax can interact through credits; do not add headline rates without the credit/restitution computation.
5. **Route transaction tax.** Load [cl-vat-return](cl-vat-return.md) for VAT scope, exemptions, debit/credit, documents, F29 and the applicable electronic filing/payment deadline. Use the current standard owner, rather than the duplicate legacy `chile-iva.md`. Do not infer that the presence of VAT on a supplier invoice makes the whole amount deductible input credit.
6. **Route people and contributions.** Load [cl-payroll](cl-payroll.md) for employed workers, withholding and employer/employee charges. Load [cl-social-contributions](cl-social-contributions.md) for independent honorarios, annual pension/health/insurance payments and total/partial coverage conditions. A boleta withholding is not proof of employee status. Future annual contribution parameters must retain their explicit unconfirmed/hypothetical labels.
7. **Route structure and related-party dealings.** Use [cl-company-formation](cl-company-formation.md) for legal form, registry/RUT and the separate activity-start handoff. Use [cl-transfer-pricing](cl-transfer-pricing.md) for controlled transactions and documentation; the general corporate Guide does not supply a complete TP study. Record the handoff and unresolved facts instead of inventing an answer from this overview.
8. **Complete the filing handoff.** Return the selected Guide(s), period, taxpayer classification, source provisions, required documents and unresolved elections. Obtain the current SII calendar and portal instructions from the owning Guide before a real filing. The overview does not reproduce every form field or certify that a return was submitted. Retain actual acknowledgements and payment evidence separately.

## Worked orientation example

For an ordinary twelve-month commercial year ending December 2026, SII publishes December UTM CLP 72,802 and UTA CLP 873,624. The ordinary 310-UTA start of the 40% marginal band is therefore CLP 270,823,440. An assumed taxable amount one peso higher has one peso in that top slice; this is not its total IGC, which also needs lower bands and credits. The same year's corporate and VAT rates are not added to that marginal rate. Load the appropriate individual computation rather than calculate total tax from this router.

```oa-check
name: CL 2026 published UTA and ordinary top-band orientation
inputs:
  december_utm: 72802
  top_band_uta: 310
steps:
  - december_uta: december_utm * 12
  - top_band_pesos: december_uta * top_band_uta
  - taxable_illustration: top_band_pesos + 1
  - top_slice: max(0, taxable_illustration - top_band_pesos)
expected:
  december_uta: 873624
  top_band_pesos: 270823440
  top_slice: 1
```

## When to refuse or refer

Refer an incomplete residence/source analysis, conflicting corporate elections, unavailable source text, a regulated/sector regime, a treaty entitlement not established, a notice dispute or a filing with missing documents to the relevant specialist workflow. Do not resolve those questions with this orientation table. A Guide's source check is separate from professional approval of a taxpayer's actual position.

UF is used for contribution ceilings and other specified purposes; it is not UTM or UTA. Fetch the exact UF date specified by the owning rule. Published December UTM/UTA does not establish the daily UF of 31 December. Similarly, the ordinary annual April rule does not establish every special filing date or an AT 2027 electronic extension. The old uncertain 2025 UTA comparison is replaced by the correct 2026 conversion and dated SII row, not carried into a new year's computation.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| LIR DL 824, current JSON metadata (version 1 November to 31 December 2026), arts. 2-4,20,52,52 bis,69; transition read separately | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6368 | 2026-11-11 |
| Código Tributario DL 830, current JSON arts. 8 Nos. 3,4,8,10, indexed units and residence; art. 68 registration handoff | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6374 | 2026-11-11 |
| DL 825, current JSON arts. 3,14,64, VAT orientation and filing rule | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=6369 | 2026-11-11 |
| Ley 21.850, current JSON art. 8 and sixth transitory article, actual income-year rate stages and art. 14 G exception | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1229250 | 2026-11-11 |
| Ley 21.755 art. 25, separate Pro Pyme transitory regime identified for corporate handoff | https://nuevo.leychile.cl/servicios/Navegar/get_norma_json?idNorma=1214890 | 2026-11-11 |
| SII UTM/UTA 2026, full monthly table and December row, UTA definition | https://www.sii.cl/valores_y_fechas/utm/utm2026.htm | 2026-11-11 |

Not yet confirmed: the complete AT 2027 filing/payment/refund calendar and fields, any case-specific electronic F29 extension not established here, the actual daily UF needed at a future valuation date, and specialist sector/treaty/election facts. They are not inferred from a general rate or prior year's filing date. This is a router; all detailed tax bases, credits, instalments, penalties and return fields require the linked owning Guide and applicable source.
