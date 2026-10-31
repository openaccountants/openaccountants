---
jurisdiction: AZ
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: azerbaijan-income-tax
  IT-CORP: az-corporate-income-tax
  VAT: azerbaijan-vat
  SC: azerbaijan-social-contributions
  PR: azerbaijan-payroll
  TP: azerbaijan-transfer-pricing
  XB: azerbaijan-cross-border
partial:
  IT-IND: "Land/building disposal and fixed-receipt trade calculations, and full bank-deposit exemption conditions remain incomplete."
  SC: "Informal-worker medical-category commencement and implementing charge remain unconfirmed."
  PR: "Non-employment director or corporate-office fees require further classification and calculation."
  TP: "Full CbCR parent, surrogate and local-filing exceptions and exchange-failure triggers remain incomplete."
  XB: "Full CFC inclusion, preferential-jurisdiction payment interactions/list and migration/exit asset calculations remain incomplete."
---

# Azerbaijan: tax pack

The State Tax Service administers the Tax Code. Ordinary income/profit tax uses the calendar year, VAT uses calendar months and payroll combines monthly payment obligations with quarterly reporting. Amounts are Azerbaijani manat (AZN) unless stated otherwise. This pack was rebuilt from current primary sources on 24 October 2026 and independently re-checked against them on 31 October 2026. Every tax domain applies; every skill is tier 2, checked against the law, with no accountant sign-off. Presence of a file is not complete coverage or professional review.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND | [azerbaijan-income-tax](azerbaijan-income-tax.md) | checked against the law; partial |
| IT-CORP | [az-corporate-income-tax](az-corporate-income-tax.md) | checked against the law |
| VAT | [azerbaijan-vat](azerbaijan-vat.md) | checked against the law; partial |
| SC | [azerbaijan-social-contributions](azerbaijan-social-contributions.md) | checked against the law; partial |
| PR | [azerbaijan-payroll](azerbaijan-payroll.md) | checked against the law; partial |
| TP | [azerbaijan-transfer-pricing](azerbaijan-transfer-pricing.md) | checked against the law; partial |
| XB | [azerbaijan-cross-border](azerbaijan-cross-border.md) | checked against the law; partial |

[az-tax-overview](az-tax-overview.md) routes questions to those skills. Ordinary computations include business profit and losses, depreciation, simplified turnover eligibility, employment gross-to-net, employee/employer contributions, entrepreneur contributions, VAT input allocation, TP adjustments, non-resident gross-up and PE remittance tax. Each tax skill has two recomputing examples. The partial notes identify actual missing computations, not zeros or exemptions.

PSA/pipeline and special-zone regimes, territorial/park/investment incentives, contribution-subsidy claims, specialist VAT margin schemes and country-by-country treaty rates are outside the implemented ordinary regime. Those specialist exclusions do not by themselves make a domain partial. The substantive core gaps above do.

## Official sources

Read on 31 October 2026: [current Tax Code](https://e-qanun.az/frameworks/46/f_46948.html), [Social Insurance Law](https://frameworks.e-qanun.az/3/f_3813.html), [Medical Insurance Law](https://frameworks.e-qanun.az/0/f_80.html), [Unemployment Insurance Law](https://frameworks.e-qanun.az/36/f_36310.html), [current registered TP Rules](https://frameworks.e-qanun.az/35/f_35074.html), [Cabinet size criteria](https://e-qanun.az/framework/41048), [sector criteria](https://www.taxes.gov.az/az/post/321), [DTA administration Rules](https://www.taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasi-haqqinda-beynelxalq-muqavilelerin-inzibatciligi-qaydalari) and [official treaty register](https://taxes.gov.az/az/page/ikiqat-vergitutmanin-aradan-qaldirilmasina-dair-beynelxalq-sazisler). Each skill names the actual articles and read dates. The consolidated Code includes future amendments: 2027 rules are not applied to 2026. Law 413-VIIQD's leasing changes take effect on 25 December 2026; the VAT and cross-border skills give both periods.

## Review and adjacent material

The research/review receipts are in `docs/research/2026-10-24-azerbaijan-*`. Separate AI source review does not constitute accountant sign-off. No `tier: 1`, named reviewer or professional approval has been added. Issue #380 stays open.

`az-company-formation.md` and `azerbaijan-tax-optimization.md` remain unchanged accounting-milestone material. Their old prospective salary statements, mixed simplified-tax descriptions and unsupported timings/figures have been recorded in the research receipt for a separate correction PR. They are not evidence for the current tax computations.
