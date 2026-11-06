---
name: na-transfer-pricing
description: "Namibia transfer pricing, 2026: s.95A arm's length rule, connected persons and the 30% tax EBITDA interest cap. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/na-transfer-pricing"
  jurisdiction: "NA"
  tax_year: "2026"
  last_updated: "2026-11-01"
---

# Namibia Transfer Pricing v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

## Who this applies to

Connected persons in an international transaction: resident with non-resident; two non-residents through a Namibian permanent establishment; two residents through a foreign permanent establishment, or where a treaty takes one out of Namibian tax (s.95A(1), [Act](https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf); [NamRA](https://www.namra.org.na/investors-info-pack/page/transfer-pricing-301019/)). Connected includes a non-company holding at least 20% of a company, group companies and control in fact. Banks and registered insurers are outside the interest cap (s.95A(7)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Interest cap | Net interest expense over 30% of tax EBITDA not deductible | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.95A(3)) |
| Cap exemption | Net interest expense not exceeding N$3,000,000 | 2026 | same |
| Carry forward | 5 years; 10 for mining, petroleum, green hydrogen | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.95A(5)) |

## The base

Where the price differs from the arm's length price the Minister may adjust (s.95A(2)). The cap also covers third-party debt guaranteed by a connected person (s.95A(4)). Tax EBITDA is taxable income before net interest, tax, tax depreciation and amortisation.

## Deadlines and filing

The adjustment flows through the [company return](na-corporate-income-tax.md).

## Penalties and interest

An adjustment produces a shortfall: see the company skill, s.66.

## Cross-border points

Withholding on the same payments: [cross-border skill](na-cross-border.md).

## Two worked examples that recompute

Example 1. Net interest N$10m, EBITDA N$20m. Cap N$6m, N$4m disallowed and carried forward.

```oa-check
name: Cap
inputs:
  n: 10000000
  e: 20000000
steps:
  - cap: e * 0.30
  - dis: n - cap
expected:
  dis: 4000000.00
```

Example 2. A decision: reduce debt? Net interest N$2.5m is within N$3m, so no cap applies; at N$3.5m on EBITDA of N$10m, N$500,000 is lost.

```oa-check
name: Over the limit
inputs:
  n: 3500000
  e: 10000000
steps:
  - dis: max(0, n - e * 0.30)
expected:
  dis: 500000.00
```

## Ask the client first

1. Connected parties and where?
2. Transactions and amounts?
3. Net interest and tax EBITDA?
4. Guarantees by connected parties?
5. Bank, insurer, mining, petroleum, green hydrogen?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: s.95A) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| NamRA transfer pricing (read: whole page) | https://www.namra.org.na/investors-info-pack/page/transfer-pricing-301019/ | 2026-11-01 |

Not yet confirmed: Practice note and documentation requirements; penalties specific to transfer pricing; methods.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-01. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `na-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/na-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
