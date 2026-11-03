---
name: cv-payroll-social
description: "Payroll and social contributions for Cape Verde (tax year 2026): INPS rates 16% and 8.5%, REMPE 8%, FOS and DPR by the 15th. Built from INPS, DNRE and Boletim Oficial pages."
jurisdiction: CV
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cape Verde Payroll and Social Contributions v0.2

## Who this applies to

Employers, employees and the self-employed in Cape Verde. The Instituto Nacional de Previdencia Social (INPS) runs social security; DNRE takes withheld income tax.

## Rates, bands and thresholds

Basis for 2026: the law is the State Budget 2026 (Lei 69/X/2025, in force 1 January 2026), the DNRE Calendario Fiscal 2026 and the base code as published. No consolidated code was found, and Lei 116/IX/2021 could not be opened, so a row resting on original code text carries that limit. The Amending Budget of 13 August 2026 changed no tax rate we could find.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Employer | 16% | 2026 | https://inps.cv/obrigacoes/ |
| Employee | 8.5% | 2026 | same |
| Total, employed | 24.5% | 2026 | same |
| Self-employed | 19.5% | 2026 | same |
| Domestic service | 15% employer, 8% worker, 23% total | 2026 | same |
| REMPE | 8%, worker | 2026 | same |
| IRPS withholding | See [income tax](cv-income-tax.md) | 2026 | https://boe.incv.cv/Bulletins/Download/1952 |

## The base

Contributions are computed on pay declared on the FOS (Folhas de Ordenados e Salarios). The TEU replaces the employer contribution in REMPE, not worker registration. Employers must register within 15 days of starting and notify new workers within 15 days of their start.

## Deadlines and filing

INPS: monthly FOS, and payment by the 15th of the next month; if the 15th is a Saturday, Sunday or holiday, the next working day. Payment needs the Documento de Cobranca generated on the INPS Portal. DNRE: DPR and withheld tax by the 15th.

### How to run a month

1. Log in to the INPS Portal and submit the FOS (online or XML).
2. Generate the Documento de Cobranca.
3. Pay at a bank, Portal (Vinti4), ATM, Home Banking, QR Code, POS, FOS Express or Televinti4.
4. Submit the DPR with the salaries annex on Porton di Nos Ilha and pay the withheld IRPS.

## Penalties and interest

Unpaid contributions bring late-payment interest and a fine for each month. Four consecutive months of FOS without payment is grave non-compliance (INPS). The Calendario Fiscal says late or missing returns and unpaid tax are infractions under the Regime Juridico das Infracoes Tributarias Nao Aduaneiras, with fines and late-payment interest. That regime could not be opened, so no amount is given here.

## Cross-border points

Non-resident employee withholding is 20% in the DPR table (code A.4). Social security treaties: not read.

## Two worked examples that recompute

Case 1: gross CVE 100,000: employer 16,000, employee 8,500, total 24,500.

```oa-check
name: INPS on 100,000
inputs:
  g: 100000
steps:
  - er: g * 0.16
  - ee: g * 0.085
  - total: er + ee
expected:
  er: 16000.00
  ee: 8500.00
  total: 24500.00
```

Case 2, REMPE or normal regime: same pay, REMPE removes employer cost and the worker pays 8%: employer saves 16,000 and the worker 500.

```oa-check
name: REMPE payroll
inputs:
  g: 100000
steps:
  - saving_er: g * 0.16
  - saving_ee: g * 0.085 - g * 0.08
expected:
  saving_er: 16000.00
  saving_ee: 500.00
```


## Ask the client first

- Regime: normal, REMPE, domestic or self-employed?
- Gross pay and any extras?
- New workers this month?
- Non-resident staff?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 69/X/2025, State Budget 2026, BO I 133 sup. 1, 31 Dec 2025: arts 29, 30, 32, 84, 99, 100 and Anexo I read | https://boe.incv.cv/Bulletins/DownloadAct?id=89137 | 2026-11-01 |
| Lei 1/XI/2026, Amending Budget 2026, BO I 90, 13 Aug 2026: searched for tax-rate changes, none found | https://boe.incv.cv/Bulletins/DownloadAct?id=112975 | 2026-11-01 |
| Lei 78/VIII/2014, Codigo do IRPS, BO I 81, 31 Dec 2014 (original text): arts 21, 45 to 53, 57, 70 to 74 read | https://boe.incv.cv/Bulletins/Download/1952 | 2026-11-01 |
| INPS, Obrigacoes: all read | https://inps.cv/obrigacoes/ | 2026-11-01 |
| INPS, Pagamento: all read | https://inps.cv/pagamento-2/ | 2026-11-01 |
| INPS, Inscricao: all read | https://inps.cv/inscricao/ | 2026-11-01 |
| INPS, Contribuicoes: all read | https://inps.cv/contribuicoes/ | 2026-11-01 |
| DNRE, DPR FAQ v6: category table and Category A answers read | https://www.mf.gov.cv/documents/54571/273413/DPR%20%E2%80%93%20Perguntas%20Frequentes_FAQ_Vers%C3%A3o%206.pdf | 2026-11-01 |
| DNRE, Calendario Fiscal 2026, updated 11 Jun 2026: all months read | https://www.mf.gov.cv/documents/54571/0/Calendario_Fiscal_2026_PEC_Vers%C3%A3o_Atualizado_110626.pdf/7f524ec2-1b35-2f33-8936-42e8b752516e?version=1.0&t=1781260657225 | 2026-11-01 |

Not yet confirmed: Lei 116/IX/2021 and every other amendment not listed in Sources; penalty amounts; interest rate. A contribution ceiling (the old skill said none generally applies); INPS law article numbers for the rates; national minimum wage for 2026; fine amounts.

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
