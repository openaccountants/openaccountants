---
name: gw-tax-overview
description: "Guinea-Bissau tax system for 2026: which taxes exist, headline rates, deadlines and the DGCI portal, from the official codes."
jurisdiction: GW
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea-Bissau Tax Overview (2026)

**Status of the 2026 budget text.** The Ministry of Finance publishes a document called OGE 2026, dated December 2025 (https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195). Its law number and date are blank (`Lei n.º ____/202`), and we could not confirm a vote, promulgation or Boletim Oficial publication. Each rule below marked "2026 budget text" applies only if that law is in force. Confirm that with the DGCI before relying on it.

## Tax system at a glance

Guinea-Bissau is in UEMOA and ECOWAS and uses the CFA franc (XOF). The tax year is the calendar year (Contribuição Industrial code art. 23: "o ano económico coincide com o ano civil"). The authority is the Direcção-Geral das Contribuições e Impostos (DGCI) in the Ministry of Finance, and returns run through [Kontaktu](https://kontaktu.mef.gw). Income is taxed by source, not under one income tax.

| Tax | Headline | Skill | Official URL |
|---|---|---|---|
| Imposto Profissional | Employees 1% to 20%; self-employed 10% to 25% | [Income tax](gw-income-tax.md) | https://kontaktu.mef.gw/legislation |
| Contribuição Industrial | 25%; minimum 1% of turnover; derrama 2% | [Corporate tax](gw-corporate-income-tax.md) | same |
| Imposto de Capitais | 5%, 10% or 15% | [Corporate tax](gw-corporate-income-tax.md) | same |
| IVA | 19%, 10%, 0%; simplified 5% | [VAT](gw-vat-gst.md) | same |
| Excise | Lei 6/2022 | none yet | same |
| Contribuição Predial Urbana | Urban property; has its own code | none yet | same |
| Employee social security | 8% in the DGCI return | [Payroll](gw-payroll-social.md) | https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf |

Every taxpayer gets a número de identificação fiscal, used on all returns and invoices (Lei Geral Tributária). The general limits are four years to assess (art. 82) and eight years for debts to prescribe (art. 45).

## Main deadlines

| Item | Date |
|---|---|
| Withholding return (DECIRF) | 10th of next month |
| IVA, normal regime | 15th of next month |
| Employer annual map | 31 January |
| Self-employed return | 28 February |
| Company return | April |

## Worked checks

Company with profit FCFA 10,000,000 and turnover FCFA 200,000,000: 25% is 2,500,000, the 1% minimum is 2,000,000, so 2,500,000 is due, plus 200,000 derrama.

```oa-check
name: Headline company tax
inputs:
  profit: 10000000
  turnover: 200000000
steps:
  - ci: max(profit * 0.25, turnover * 0.01)
  - total: ci + profit * 0.02
expected:
  total: 2700000
```

Price of FCFA 1,190,000 including 19% IVA: 1,190,000 / 119 x 100 = 1,000,000 before tax.

```oa-check
name: IVA out of an inclusive price
inputs:
  price: 1190000
steps:
  - base: price / 119 * 100
expected:
  base: 1000000
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated codes, DGCI Kontaktu legislation page | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| DECIRF instructions | https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf | 2026-11-01 |
| OGE 2026, tax chapter | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 | 2026-11-01 |

Not yet confirmed: whether the 2026 budget text is in force; the Imposto Complementar. The old skill's top "IRPS" 20% and 31 March filing date are replaced by the official codes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
