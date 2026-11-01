---
name: st-payroll-social
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It covers INSS employer and employee rates, the conflict between the 6% and 4% in the official text and the reported 7% and 5%, the minimum contributory wage, the UCSS, monthly declarations by the 10th, self-employed schemes of 10% and 14%, and interest. It says plainly which figures come from official texts and which remain unverified because the Finance Ministry site could not be opened. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto. It is general reference for working papers, not for filing without review by a qualified professional in the country."
jurisdiction: ST
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.2
category: international
---

# Sao Tome and Principe Payroll and Social Contributions v0.2

> **Sourced from the law, in part.** Tax year 2026. The Finance Ministry site refused access on 1 November 2026, so the tax codes themselves were not read. Rows marked unverified carry older figures that no official page has confirmed. No accountant has signed this version and it has had no independent review yet.

## Who this applies to

Every employer with staff, including public bodies, embassies, religious bodies and NGOs ([INSS](https://inss.gov.st/trabalhador-outrem.html)), and self-employed people ([INSS](https://inss.gov.st/independente.html)). Members of company organs, partners and managers go on the monthly declaration ([INSS](https://inss.gov.st/Decla-rend.html)).

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Employee rate | 4% in the official text | 2026 text; see next row | [REPSO art. 101(3)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf); [INSS page](https://inss.gov.st/trabalhador-outrem.html) |
| Employer rate | 6% in the official text | 2026 text; see next row | [REPSO art. 101(3)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf) |
| Rates under Decree-Law 1/2025 | unverified: a law firm alert reports 7% employer and 5% employee from 1 January 2025, with 6% and 4% kept for some entities. The decree was not read | 2026 | unverified |
| Self-employed | 10% compulsory scheme; 14% wider scheme, on a chosen conventional pay | 2026 | [REPSO art. 131(1)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf); [INSS page](https://inss.gov.st/independente.html) |
| Self-employed pay bands | 1, 3, 5 or 7 UCSS and upwards | 2026 | [REPSO art. 131(2)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf) |
| UCSS | Db 1,000 for minimum pensions, minimum contributory wage, minimum sickness benefit, certificates; Db 800 for all else | 2026 if not since changed | [Joint Order 35/2023 art. 1](https://inss.gov.st/assets/Leis/Despacho_n_35_2023.pdf) |
| Minimum contributory wage | Legal minimum wage; if none or below 1 UCSS, 1 UCSS | 2026 | [REPSO art. 99](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf) |
| Payroll income tax | Employer withholding: older point, unverified. See [income tax](st-income-tax.md) | 2026 | unverified |

## The base

Contribution equals the rates times the contribution base ([REPSO art. 97](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf)). Older question on a cap: no ceiling appears in the articles read; the rest of the text was not checked for one. Old note that INSS excludes health care: unverified. Sickness benefit is a contributory benefit under the wider self-employed scheme.

Self-employed on 10%: old age, invalidity, survivors. On 14%: those plus sickness, parenthood, funeral ([INSS page](https://inss.gov.st/independente.html)).

## Deadlines and filing

Register the employer and each worker. Send the declaration through the INSS portal or by electronic means, and proof of payment, by the 10th of the next month. January 2024 was due 10 February 2024 ([INSS](https://inss.gov.st/Decla-rend.html)). If the 10th is not a working day, pay earlier ([REPSO art. 105](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf)). The old skill said the 15th; the law says the 10th.

## Penalties and interest

Late interest runs daily at j/30, where j is the monthly rate for tax debts, never below 1%, and doubles once the delay passes 180 days ([REPSO art. 106](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf)). Missing declarations can be estimated by adding at least 25% to the latest pay (art. 100).

## Cross-border points

Social security conventions are out of scope and unverified here.

## Two worked examples that recompute

**Example 1.** Salary of Db 10,000 at the rates in the official text. If the 2025 rates apply, use 7% and 5%.

```oa-check
name: Employee on official text rates
inputs:
  salary: 10000
steps:
  - employee: salary * 0.04
  - employer: salary * 0.06
  - total: employee + employer
expected:
  employee: 400
  employer: 600
  total: 1000
```

**Example 2, decision: 10% or 14%.** Self-employed person on 3 UCSS at Db 800 (the Order keeps Db 800 for cases it does not list; confirm with INSS).

```oa-check
name: Self-employed scheme
inputs:
  ucss: 800
steps:
  - pay: ucss * 3
  - basic: pay * 0.10
  - wider: pay * 0.14
  - extra: wider - basic
expected:
  pay: 2400
  basic: 240
  wider: 336
  extra: 96
```

## Ask the client first

- Employer or self-employed
- Whether INSS authorised the older rate
- Gross pay and benefits
- Scheme and band if self-employed
- Months not yet declared

## Sources

| Source | URL | Read on |
|---|---|---|
| Decree-Law 19/2022 consolidated text, arts. 97 to 105, 131 | https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf | 2026-11-01 |
| Joint Order 35/2023, UCSS value | https://inss.gov.st/assets/Leis/Despacho_n_35_2023.pdf | 2026-11-01 |
| INSS employed workers page | https://inss.gov.st/trabalhador-outrem.html | 2026-11-01 |
| INSS self-employed page | https://inss.gov.st/independente.html | 2026-11-01 |
| INSS monthly declaration page | https://inss.gov.st/Decla-rend.html | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies. The Ministry of Finance site (financas.gov.st) answered 403 by fetch and in a browser tab on 2026-11-01 and was not read.

Not yet confirmed: Text of Decree-Law 1/2025 and current rates; 2026 legal minimum wage; UCSS after 2023; any wage ceiling; wage withholding table; portal steps beyond the pages cited.

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
