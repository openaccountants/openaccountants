---
name: gw-income-tax
description: "Guinea-Bissau tax on individuals for tax year 2026: Imposto Profissional bands, self-employed rates, annual return and payments, from the official code."
jurisdiction: GW
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea-Bissau Personal Income Tax (2026)

Guinea-Bissau has no single personal income tax and no IRPS statute. Income is taxed by source: Imposto Profissional on work, Imposto de Capitais on investment income, Contribuição Predial Urbana on urban property. Earlier versions of this skill called the tax IRPS; the DGCI publishes no such code.

**Status of the 2026 budget text.** The Ministry of Finance publishes a document called OGE 2026, dated December 2025 (https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195). Its law number and date are blank (`Lei n.º ____/202`), and we could not confirm a vote, promulgation or Boletim Oficial publication. Each rule below marked "2026 budget text" applies only if that law is in force. Confirm that with the DGCI before relying on it.

## Who this applies to

Anyone earning work income in Guinea-Bissau, resident there or not, for work done there. People living abroad are also caught when a resident company makes the income available (Código do Imposto Profissional, art. 3). Exempt: foreign staff of diplomatic and consular missions, where reciprocity exists, and foreign staff of international organisations (art. 4). Pensions up to FCFA 200,000 a month, invalidity pensions, sick pay, dismissal compensation set under labour law, and travel costs and daily allowances within limits are not work income (art. 2).

## Rates, bands and thresholds

Currency is the CFA franc (XOF, FCFA). Tax = gross income in the band x rate, less the deduction on that row (art. 27(3)).

| Item | Rate or amount | Parcela to deduct | Tax year | Official URL |
|---|---|---|---|---|
| Employee, monthly income to 41,667 | 1% | 0 | 2026 | https://kontaktu.mef.gw/legislation |
| Employee, 41,668 to 83,333 | 6% | 2,083 | 2026 | same |
| Employee, 83,334 to 208,333 | 8% | 3,750 | 2026 | same |
| Employee, 208,334 to 300,000 | 10% | 7,917 | 2026 | same |
| Employee, 300,001 to 400,500 | 12% | 13,917 | 2026 | same |
| Employee, 400,501 to 750,000 | 14% | 37,947 | 2026 | same |
| Employee, 750,001 to 1,100,000 | 16% | 52,947 | 2026 | same |
| Employee, 1,100,001 to 1,500,000 | 18% | 74,947 | 2026 | same |
| Employee, above 1,500,000 | 20% | 104,947 | 2026 | same |
| Self-employed and author's rights, monthly to 183,333 | 10% | 0 | 2026 | same |
| Self-employed, 183,334 to 833,333 | 20% | 18,333 | 2026 | same |
| Self-employed, above 833,333 | 25% | 60,000 | 2026 | same |
| Occasional income of residents | 10% | none | 2026 | same |
| Interest on deposits and placements under one year | 15% | none | 2026 | same |
| Other investment income, including dividends and capital gains | 15% | none | 2026 | same |
| Bonds and Treasury paper maturing in under two years | 10% | none | 2026 | same |

Reading note: the published 14% row deduction of 37,947 makes tax fall by about 16,000 when income crosses 400,500. The other rows join up. Apply the table as published and ask the DGCI on a case near that line.

The code sets an annual column too (art. 27(1)); the top annual band starts above FCFA 18,000,000.

## The base

Work income covers pay in cash or kind, bonuses and benefits (art. 1). The DGCI withholding instructions compute the tax on gross pay ("valor bruto pago x taxa"), so do not subtract social security unless the DGCI confirms it.

Self-employed people deduct costs indispensable to the activity: staff, finance leases, third-party services, utilities, consumables, professional dues, training, travel, insurance, and social contributions (art. 13). Vehicle costs count at 50%. Travel is capped at 10% of gross income, and training plus other costs at 10% together.

2026 budget text (art. 13): benefits count as pay above FCFA 65,000 for family allowances and FCFA 50,000 for meal allowances, and the listed benefits may not exceed 15% of gross monthly income. The current code cap is 30%. New art. 27-A adds autonomous rates: undocumented spending 15%, representation 12%, fuel vouchers 10%, daily allowances 5%, amounts owed to non-residents 10%.

## Deadlines and filing

| Step | Who | Deadline | Basis |
|---|---|---|---|
| Registration declaration | Self-employed | Before starting | art. 10-A |
| Annual return, modelo 1 | Self-employed with art. 11 income | 28 February, tax due the same day | arts 11, 30 |
| Payments on account, each 25% of the last assessed tax | Self-employed | March, June, September, December | art. 31-A |
| Withholding on employees | Employer, on the DECIRF | 10th of the next month | [DECIRF instructions](https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf) para. 9 |

How to file the annual return: go to the Repartição de Finanças for your home area, hand in modelo 1 with the receipts, compute the tax on the form, deduct tax withheld and payments on account, and pay that day. If the tax is not paid at that moment, the return counts as not filed (art. 30(2)). The kontaktu.mef.gw portal is the DGCI's filing system for its electronic returns.

## Penalties and interest

Late or missing declarations: FCFA 50,000 to 300,000. Refusal to show records: FCFA 100,000 to 300,000. Any other breach: FCFA 25,000 to 100,000 (art. 37). Tax debts prescribe in eight years (Lei Geral Tributária, art. 45). The right to assess lapses after four years from the start of the following year (art. 82).

## Cross-border points

Non-residents pay on work done in the country or income made available by a resident company (art. 3). Non-resident businesses under the six-month regime are in [corporate income tax](gw-corporate-income-tax.md). The payroll side is in [payroll](gw-payroll-social.md).

## Two worked examples that recompute

Employee on FCFA 250,000 a month: 250,000 x 10% less 7,917 = 17,083.

```oa-check
name: Employee, FCFA 250,000 a month
inputs:
  gross: 250000
steps:
  - tax: gross * 0.10 - 7917
expected:
  tax: 17083
```

Decision: the same FCFA 250,000 earned as employment or as self-employment, before costs. Self-employed: 250,000 x 20% less 18,333 = 31,667, which is 14,584 more. Self-employment wins only if deductible costs cut the income enough, and the costs need documents.

```oa-check
name: Employee or self-employed at FCFA 250,000
inputs:
  gross: 250000
steps:
  - employee: gross * 0.10 - 7917
  - self: gross * 0.20 - 18333
  - gap: self - employee
expected:
  gap: 14584
```

## Ask the client first

1. Employee, self-employed, or occasional income?
2. Where is the work done, and who pays?
3. Monthly gross, including benefits in kind?
4. For the self-employed, which costs are documented?
5. Is the pay near FCFA 400,500 a month?
6. Is any pension or exempt status involved?

## Sources

| Source | URL | Read on |
|---|---|---|
| Código do Imposto Profissional, Decreto 23/83, consolidated to 31 Jan 2021 (consolidated text on the DGCI Kontaktu legislation page; only the sections for this skill were read) | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| Código do Imposto de Capitais, Decreto 8/84, art. 22 rates (consolidated text on the DGCI Kontaktu legislation page; only the sections for this skill were read) | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| Lei Geral Tributária, Lei 3/2022, arts 45, 82 (consolidated text on the DGCI Kontaktu legislation page; only the sections for this skill were read) | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| DECIRF filing instructions, Instrução de Serviço 20/DGCI/2021, paras 9-10 and Anexo A | https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf | 2026-11-01 |
| OGE 2026, Lei do Orçamento, arts 6 to 17 (draft-form text, law number blank; the tax chapter only was read) | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 | 2026-11-01 |

Not yet confirmed: whether the 2026 budget text is in force; whether social security reduces the Imposto Profissional base (the old skill said yes on a payroll vendor's word, DGCI instructions show gross); the Imposto Complementar on top of the separate taxes (a DGCI 2025 talk mentions an overlay tax; code not found on the portal); residence tests (the 183-day rule in the old skill has no official source; art. 3 turns on where work is done); the old claim of a 31 March annual return is replaced by the code's 28 February; the old 0% first-band note has no official support.

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
