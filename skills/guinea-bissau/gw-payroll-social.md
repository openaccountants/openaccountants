---
name: gw-payroll-social
description: "Guinea-Bissau payroll for tax year 2026: Imposto Profissional withholding, the DECIRF return, stamp duty, democracy tax and social security."
jurisdiction: GW
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guinea-Bissau Payroll and Social Contributions (2026)

**Status of the 2026 budget text.** The Ministry of Finance publishes a document called OGE 2026, dated December 2025 (https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195). Its law number and date are blank (`Lei n.º ____/202`), and we could not confirm a vote, promulgation or Boletim Oficial publication. Each rule below marked "2026 budget text" applies only if that law is in force. Confirm that with the DGCI before relying on it.

## Who this applies to

Any employer or other payer of work income, even occasional (Código do Imposto Profissional, arts 5, 18). The social security body is named INPS in older skills and INSS in other documents; we could not open an official site for it.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Official URL |
|---|---|---|---|
| Imposto Profissional withheld | [Band table](gw-income-tax.md) on gross pay | 2026 | https://kontaktu.mef.gw/legislation |
| Employee social security, as computed by DECIRF field 06 | 8% of gross | 2026 | https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf |
| Stamp duty on pay, DECIRF field 11 | 0.3% of gross | 2026 | same |
| Late DECIRF fine | FCFA 100,000 to 3,000,000 | 2026 | same |
| Employer social security | unverified: 14% in the old skill, no official text opened | 2026 | unverified |
| Work accident cover | unverified: old skill's 2% to 10% has no official source | 2026 | unverified |
| Earnings ceiling | unverified: old skill says none | 2026 | unverified |
| Democracy tax, 2026 budget text art. 12 | FCFA 500 to 20,000 by band | 2026 | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 |

Democracy tax table in the 2026 budget text, for employees and the self-employed, including informal workers, read as monthly pay bands (the text does not state the period): up to 41,667: 500; to 83,333: 1,000; to 208,333: 2,000; to 300,000: 4,000; to 400,500: 6,000; to 750,000: 10,000; to 1,100,000: 15,000; to 1,500,000: 17,000; above: 20,000. It is collected with the Imposto Profissional (art. 12(4)). Under-18s not working and people unable to work are exempt. The DECIRF already carries an Imposto de Democracia under Lei 1/2021 art. 14; its previous table was not read.

## The base

Tax is charged on gross pay and on benefits in cash or kind (art. 1). See [income tax](gw-income-tax.md) for what is excluded. Field 07 of DECIRF Anexo A separates pay and holiday pay, the 13th month, and other allowances.

## Deadlines and filing

| Step | Deadline | Basis |
|---|---|---|
| Keep an individual record per worker, no more than 30 days behind | Always | arts 5, 6 |
| DECIRF and payment | 10th of the next month | DECIRF para. 9; art. 29 |
| Annual map and individual slips | 31 January | art. 7 |

How to file the DECIRF, on Kontaktu: open Quadro 01 (taxpayer) and Quadro 02 (period, type). In Anexo A, enter each worker's NIF (field 03), and income (field 05); fields 06, 08, 10 and 11 fill in. A worker with no NIF is rejected, so obtain one from the DGCI first. Quadro 03 then shows field 04 Imposto Profissional, 05 democracy tax, 06 stamp duty. Sign in Quadros 04 and 05, submit, and pay. We did not confirm how social security itself is paid; the DECIRF only computes the employee share.

## Penalties and interest

Late or missing DECIRF: FCFA 100,000 to 3,000,000, on top of late-payment penalties (Lei 8/2020 art. 8). Late annual map or missing records: FCFA 50,000 to 300,000 (art. 37). Under the 2026 budget text, the withholder alone answers for tax withheld and not paid over (Lei Geral Tributária art. 24).

## Cross-border points

Foreign staff are taxed on work done here, and residents abroad on income made available by a resident company (art. 3). Staff of embassies and international organisations can be exempt (art. 4).

## Two worked examples that recompute

Employee on FCFA 250,000: tax 17,083, social security 20,000, stamp 750. Net 212,167, before any democracy tax.

```oa-check
name: Monthly payroll, FCFA 250,000
inputs:
  gross: 250000
steps:
  - tax: gross * 0.10 - 7917
  - ss: gross * 0.08
  - stamp: gross * 0.003
  - net: gross - tax - ss - stamp
expected:
  net: 212167
```

Decision: is the 2026 democracy tax withheld? At FCFA 250,000 the table gives 4,000, so net falls to 208,167. Run the payroll both ways only after the DGCI confirms the budget text.

```oa-check
name: Net with the 2026 democracy tax
inputs:
  net_before: 212167
  idpc: 4000
steps:
  - net: net_before - idpc
expected:
  net: 208167
```

## Ask the client first

1. How many workers, and are any foreign?
2. Gross pay and benefits for each?
3. Does each worker have a NIF?
4. Is the employer registered on Kontaktu?
5. Is the employer registered with social security?

## Sources

| Source | URL | Read on |
|---|---|---|
| Código do Imposto Profissional (consolidated text on the DGCI Kontaktu legislation page; only the sections for this skill were read) | https://kontaktu.mef.gw/legislation | 2026-11-01 |
| DECIRF instructions, Instrução de Serviço 20/DGCI/2021, Quadro 03 and Anexo A | https://kontaktu.mef.gw/api/public_files/BAo5g30BVxKCKoELsx7W.pdf | 2026-11-01 |
| OGE 2026, Lei do Orçamento, arts 6 to 17 (draft-form text, law number blank; the tax chapter only was read) | https://www.mef.gw/publicacoes/orcamento-geral-do-estado/2026-oge2026/viewdocument/195 | 2026-11-01 |

Not yet confirmed: employer social security rate (14% appears in an ILO summary and vendor pages, no official text opened; Law 4/2007 not found on an official site); work accident rates; earnings ceiling; social security due date and form (the old 15th of month is unsourced; the tax date is the 10th); quarterly statements in the old skill (no official source, dropped from the body); whether the 2026 budget text is in force; the pay period of the democracy tax table.

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
