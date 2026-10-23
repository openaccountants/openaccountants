---
name: portugal-vat-return
description: "Portuguese VAT (IVA) for tax year 2026: who must charge it, the mainland rates of 23%, 13% and 6%, the Azores (16%, 9%, 4%) and Madeira (22%, 12%, 4%) rates, the art. 53 small-business exemption at EUR 15,000 with its 25% margin, the EU small-business scheme (EUR 100,000), monthly or quarterly periodic returns (EUR 650,000 test), return due on the 20th and payment on the 25th of the second month after the period (20 and 25 September for June and Q2), refunds after 12 months or above EUR 3,000, blocked input VAT, the domestic reverse charge on construction, late interest (7.221% in 2026) and RGIT fines. Trigger on: Portuguese VAT, IVA, declaração periódica, regime de isenção artigo 53, IVA trimestral mensal, autoliquidação, reembolso de IVA, coima IVA, Açores Madeira IVA. Out of scope: invoicing software, ATCUD and SAF-T (portugal-einvoice), bookkeeping (portugal-bookkeeping), income tax (pt-income-tax), corporate tax (pt-corporate-tax)."
version: 2.1
jurisdiction: PT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
  - eu-vat-directive
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal VAT (IVA): rates, thresholds, returns and penalties, tax year 2026 v2.1

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Portugal.

**What this skill does.** It sets out the law layer of Portuguese VAT for 2026: who is in, the rates on the mainland and in the autonomous regions, the small-business exemption, return frequency, deadlines, refunds and penalties. Figures come from the VAT Code (Código do IVA, "CIVA"), the General Tax Law ("LGT") and the General Regime for Tax Offences ("RGIT"), read on the Portal das Finanças, from AT circulars and from the Diário da República.

**Sibling skills.** [pt-vat-return](pt-vat-return.md) is a pointer to this file. [portugal-einvoice](portugal-einvoice.md) covers certified invoicing software, ATCUD and SAF-T. [portugal-bookkeeping](portugal-bookkeeping.md), [pt-income-tax](pt-income-tax.md) and [pt-corporate-tax](pt-corporate-tax.md) cover the rest. Load `vat-workflow-base` and `eu-vat-directive` alongside.

## Who this applies to

- **Taxable persons.** Anyone who independently carries on an activity of producing, trading or providing services, including liberal professions, and anyone who carries out a single taxable operation linked to such an activity (CIVA art. 2).
- **Small-business exemption (regime especial de isenção, art. 53).** A taxable person with its seat or domicile in Portugal is exempt if it does not carry out exports or related activities and its annual turnover in Portugal in the previous calendar year did not exceed EUR 15,000. A business starting up uses its estimate for the current year (art. 53(1) and (5)). An exempt business charges no VAT and cannot deduct input VAT (art. 53(3)). The scheme does not apply to a single taxable operation or to intra-EU supplies of new means of transport (art. 53(6)).
- **Losing the exemption (art. 58).** The exemption ends: from 1 January of the next year if turnover in the year exceeded EUR 15,000; at once if turnover in the current year exceeds EUR 15,000 by more than 25% (that is, above EUR 18,750); or when another condition stops being met (art. 58(2) and (4)). The business then files a change declaration (art. 32) within 15 working days of the year-end or of the moment it crossed the 25% margin (art. 58(5)).
- **Moving into the exemption.** A business in the normal regime that meets the conditions files a change declaration (art. 32) to apply it (art. 54(1)).
- **EU small-business scheme.** A business established in another EU state can use the Portuguese exemption if its EU turnover is at most EUR 100,000, it has notified its home state, and it holds a number with the suffix "EX" (art. 53(2)). A Portuguese business can use another state's exemption under art. 58-A. Rules in force since 2025 (Decree-Law 35/2025).
- **Out of scope here.** The small retailers' scheme (art. 60 onwards), margin schemes, VAT groups, travel agents, farmers' flat-rate scheme and import VAT deferral. Refer them.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate, mainland | 23% | 2026 | CIVA art. 18(1)(c), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx |
| Intermediate rate, mainland (List II: for example restaurant and catering services, excluding alcoholic drinks and soft drinks; certain tinned fish) | 13% | 2026 | CIVA art. 18(1)(b) and List II, https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx |
| Reduced rate, mainland (List I: for example basic foods, books, medicines, hotel accommodation, certain housing construction) | 6% | 2026 | CIVA art. 18(1)(a) and List I, https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx |
| Azores: reduced / intermediate / standard | 4% / 9% / 16% | 2026 | AT Ofício Circulado 25045/2024, https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_25045_2024.pdf |
| Madeira: reduced (since 1 October 2024) / intermediate / standard | 4% / 12% / 22% | 2026 | AT Ofício Circulado 25045/2024, https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_25045_2024.pdf |
| Construction or renovation of homes for owner-occupation sale or housing rent within set price limits (List I item 2.42), operations started 25 September 2025 to 31 December 2029, VAT due from 1 January 2026 | 6% | 2026 | List I item 2.42, Decree-Law 97/2026, https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx |
| Small-business exemption: previous-year turnover in Portugal | EUR 15,000 | 2026 | CIVA art. 53(1), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx |
| Exemption ends at once when current-year turnover exceeds the limit by more than | 25% (above EUR 18,750) | 2026 | CIVA art. 58(2)(b), (4)(b), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva58.aspx |
| EU small-business scheme: EU-wide turnover cap | EUR 100,000 | 2026 | CIVA art. 53(2)(a), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx |
| Monthly periodic return: previous-year turnover at least | EUR 650,000 | 2026 | CIVA art. 41(1)(a), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx |
| Refund: credit still outstanding after 12 months above | EUR 250 | 2026 | CIVA art. 22(5), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva22.aspx |
| Refund before 12 months: credit above | EUR 3,000 | 2026 | CIVA art. 22(6), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva22.aspx |
| AT may require a guarantee for refunds above | EUR 30,000 | 2026 | CIVA art. 22(7), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva22.aspx |
| Input VAT on diesel, LPG, natural gas and biofuels for ordinary vehicles | 50% deductible | 2026 | CIVA art. 21(1)(b), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva21.aspx |
| Late payment interest (juros de mora) on debts to the State, from 1 January 2026 | 7.221% a year | 2026 | IGCP Aviso 18/2026/2, https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 |
| Fine for a late or missing return | EUR 150 to EUR 3,750 | 2026 | RGIT art. 116(1), https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx |

## The taxable base

- **What is taxed.** Supplies of goods and services in Portugal, intra-EU acquisitions and imports. The base is the consideration excluding VAT.
- **Where a supply takes place inside Portugal matters.** Supplies treated as made in the Azores or Madeira take the regional rates (art. 18(3)).
- **Exempt supplies.** Art. 9 lists the exemptions without deduction (for example health, education, most financial services and letting of property). A business with mixed supplies apportions input VAT.
- **Customer pays the VAT (autoliquidação).** The Portuguese business customer self-assesses VAT on: services bought from suppliers not established in Portugal under the general rule (art. 2(1)(e)); construction work, including renovation, repair, maintenance and demolition, done under contract or subcontract for a customer with a right to deduct (art. 2(1)(j)); Annex E goods such as scrap (art. 2(1)(i)); emission rights (art. 2(1)(l)); and cork, wood, pine cones and pine nuts in shell (art. 2(1)(m)).
- **Input VAT.** Deductible on goods and services bought for taxable operations with a valid invoice (art. 19-20). Not deductible (art. 21(1)): buying, leasing, using or repairing passenger cars, pleasure boats, aircraft and motorcycles; fuel for ordinary vehicles, except that 50% of the VAT on diesel, LPG, natural gas and biofuels is deductible; business travel and tolls; accommodation, food, drink, tobacco and reception costs. Exceptions are in art. 21(2).
- **Credits.** An excess of deductible VAT is carried forward to later periods (art. 22(4)). Refunds are covered under Deadlines and filing.

## Deadlines and filing

- **Frequency.** Monthly if turnover in the previous calendar year was EUR 650,000 or more; quarterly if below (art. 41(1)). A quarterly business may opt for monthly returns: on registration, or by a change declaration filed in January, with effect from 1 January (art. 41(2)-(4)). A quarterly business that reached EUR 650,000 files a change declaration in January and moves to monthly from 1 January of that year (art. 41(5)). A part-year turnover is annualised (art. 41(7)).
- **Return due dates.** The periodic return is filed electronically by the 20th of the second month after the month or quarter (art. 41(1)). The June return (monthly filers) and the Q2 return (quarterly filers) are due by 20 September (art. 41(10)).
- **Payment due dates.** The VAT is paid by the 25th of the second month after the month or quarter (art. 27(1)). For June and Q2, by 25 September (art. 27(10)).
- **2026 dates for a quarterly filer.** Q1 2026: return by 20 May 2026, payment by 25 May 2026. Q2: 20 and 25 September 2026. Q3: 20 and 25 November 2026. Q4: 20 and 25 February 2027.
- **Return when nothing happened.** The periodic return is still due for a period with no taxable operations (art. 29(2)).
- **Refunds.** A refund can be asked once a credit above EUR 250 has persisted for 12 months; earlier if the credit exceeds EUR 3,000, or on ceasing activity or moving to a scheme without returns, if at least EUR 25 (art. 22(5)-(6)). AT pays by the end of the second month after the request, or within 30 days for businesses on the monthly refund register; after that, the business can ask for compensatory interest (art. 22(8)). Registration on the monthly refund register is requested by the end of November of the previous year (art. 22(14)).
- **Invoicing and SAF-T.** Invoices must be issued through certified software and their data reported to AT. See [portugal-einvoice](portugal-einvoice.md).

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Late payment interest (juros de mora) | 7.221% a year from 1 January 2026, from the payment deadline until payment | LGT art. 44; CIVA art. 96; IGCP Aviso 18/2026/2 |
| Compensatory interest (juros compensatórios) | At the legal interest rate (Civil Code art. 559(1)), counted daily from the filing deadline when the taxpayer's fault delays assessment. A late return always counts as a delay. Capped at 180 days for an error shown in the return | LGT art. 35 |
| VAT charged but not paid over, up to 90 days or longer if not a crime | Fine between the unpaid tax and twice that amount | RGIT art. 114(1) |
| Same, through negligence | Fine between 15% and half of the unpaid tax | RGIT art. 114(2) |
| Late or missing periodic return | Fine of EUR 150 to EUR 3,750 | RGIT art. 116(1) |
| Waiver of the fine | No fine if, in the previous five years, there was no conviction and no waiver or reduced fine; or if the failure caused no loss of revenue and was put right. Unpaid tax always counts as a loss | RGIT art. 29 |
| Payment short of the declared amount | AT issues a debt certificate for the difference and starts enforcement | CIVA art. 27(6) |

## Cross-border points

- **Services bought from abroad.** The Portuguese business customer self-assesses VAT on services taxable in Portugal under the general rule and bought from a supplier not established in Portugal, and deducts it in the same return if entitled (art. 2(1)(e), 19(1)(c)).
- **Services sold to EU businesses** under the general rule are taxed in the customer's state; they go on the return and on the recapitulative statement.
- **Intra-EU supplies of goods** to VAT-registered customers are exempt with deduction; intra-EU acquisitions are self-assessed.
- **Regional rates.** A mainland business supplying in the Azores or Madeira applies the regional rate where the operation is treated as made there (art. 18(3)).
- **Non-established businesses** may use the Portuguese small-business exemption only through the EU scheme (art. 53(2)). Those that had used the old exemption lost it from 1 July 2025 (Decree-Law 35/2025, art. 10).
- **Sales to EU consumers** at a distance and e-services above the EU-wide threshold are taxed in the customer's state, usually through the one-stop shop. See `eu-vat-directive`.

## Worked examples

**Example 1: quarterly return, Q3 2026, mainland.** A Lisbon Lda. with 2025 turnover of EUR 300,000 files quarterly. In July to September 2026 it invoices EUR 40,000 of services at 23%. It buys EUR 12,000 of goods and services at 23%, EUR 1,000 net of diesel at 23%, a EUR 300 net client lunch at 13% and EUR 600 net of passenger-car leasing at 23%. Output VAT is 9,200. Input VAT on general purchases is 2,760. The diesel VAT is 230, of which 50% is deductible: 115. The lunch VAT (39) and the car leasing VAT (138) are not deductible. VAT payable is 6,325. The return is due by 20 November 2026 and the payment by 25 November 2026. Paid one month late, late interest at 7.221% is about EUR 38.06.

```oa-check
name: Portugal quarterly periodic return Q3 2026 with blocked and 50% input VAT
inputs:
  sales_net: 40000
  purchases_net: 12000
  diesel_net: 1000
  lunch_net: 300
  car_lease_net: 600
steps:
  - output_vat: sales_net * 0.23
  - input_general: purchases_net * 0.23
  - diesel_deductible: diesel_net * 0.23 * 0.50
  - lunch_deductible: lunch_net * 0.13 * 0
  - car_lease_deductible: car_lease_net * 0.23 * 0
  - deductible: input_general + diesel_deductible + lunch_deductible + car_lease_deductible
  - payable: output_vat - deductible
  - interest_one_month: payable * 0.07221 / 12
expected:
  output_vat: 9200
  deductible: 2875
  payable: 6325
  interest_one_month: 38.06
```

**Example 2: a freelancer crosses the 25% margin.** A designer in Porto is under the art. 53 exemption for 2026, having billed EUR 14,000 in 2025. By 31 October 2026 she has billed EUR 18,000. That is above EUR 15,000 but within the 25% margin (EUR 18,750), so she stays exempt for now. In November she bills EUR 1,500, taking the year to EUR 19,500, 30% over the limit. The exemption ends at that moment (art. 58(4)(b)). She files a change declaration within 15 working days and charges 23% from then. On EUR 2,000 of December invoices she charges EUR 460. Even had she stayed within the margin, her 2026 turnover above EUR 15,000 would have ended the exemption from 1 January 2027 (art. 58(4)(a)).

```oa-check
name: Portugal art. 53 exemption, crossing the 25% margin in 2026
inputs:
  billed_to_october: 18000
  november_invoice: 1500
  limit: 15000
  december_net: 2000
steps:
  - margin_ceiling: limit * 1.25
  - year_to_november: billed_to_october + november_invoice
  - excess_pct: (year_to_november - limit) / limit * 100
  - over_ceiling: year_to_november - margin_ceiling
  - vat_december: december_net * 0.23
expected:
  margin_ceiling: 18750
  year_to_november: 19500
  excess_pct: 30
  over_ceiling: 750
  vat_december: 460
```

## Ask the client first

- What was your turnover in Portugal in 2025, and what will it be in 2026? Do you export? (Decides the EUR 15,000 exemption and the 25% margin.)
- Was your 2025 turnover EUR 650,000 or more, and have you opted for monthly returns? (Decides monthly or quarterly.)
- Where are your operations treated as made: mainland, Azores or Madeira? (Decides the rate.)
- Do you make exempt supplies such as letting, health, education or financial services? (Decides apportionment.)
- Do you have passenger cars, fuel, travel, meals or hospitality costs? (Decides blocked and 50% input VAT.)
- Do you buy construction work, services from abroad or scrap? (Decides self-assessment.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIVA art. 2 (taxable persons, self-assessment) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva2.aspx | 2026-10-23 |
| CIVA art. 18 (rates) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx | 2026-10-23 |
| CIVA Lists I and II | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/c-iva-listas.aspx | 2026-10-23 |
| CIVA art. 19 and 21 (deduction and exclusions) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva21.aspx | 2026-10-23 |
| CIVA art. 22 (credits and refunds) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva22.aspx | 2026-10-23 |
| CIVA art. 27 (payment deadlines) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva27.aspx | 2026-10-23 |
| CIVA art. 41 (periodic return deadlines and frequency) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva41.aspx | 2026-10-23 |
| CIVA art. 53 (small-business exemption, with Decree-Law 35/2025 transitional rules) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-23 |
| CIVA art. 54 and 58 (entering and leaving the exemption) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva58.aspx | 2026-10-23 |
| AT Ofício Circulado 25045/2024 (rates in the Azores and Madeira) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Oficio_circulado_25045_2024.pdf | 2026-10-23 |
| CIVA art. 29 (obligations, nil returns) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva29.aspx | 2026-10-23 |
| LGT art. 35 and 44 (interest) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx | 2026-10-23 |
| IGCP Aviso 18/2026/2 (late interest 7.221% for 2026) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-23 |
| RGIT art. 29, 114 and 116 (fines) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx | 2026-10-23 |

Not yet confirmed: whether the Azores or Madeira regional budgets changed their rates after the AT circular of 6 December 2024 (none found in the sources read); whether the supply that takes turnover past the 25% margin is itself taxed or only later supplies; how deadlines falling on a weekend or holiday move (20 September 2026 is a Sunday); the deadline for reporting invoice data to AT (left to portugal-einvoice); the maximum fine limits that cap RGIT art. 114; the return-form changes made by Portaria 298/2026/1 (published 16 July 2026, mostly for periods from 1 July 2027) are not described here.
