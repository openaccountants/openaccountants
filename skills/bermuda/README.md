---
jurisdiction: BM
applicable: [IT-CORP, SC, PR, TP, XB]
not_applicable:
  IT-IND: "Bermuda has no personal income tax; employment income bears the payroll tax employee portion (bm-payroll-social)"
  VAT: "Bermuda has no VAT, GST or general sales tax; indirect tax is customs import duty (bermuda-tax)"
covered_by:
  IT-CORP: bm-corporate-income-tax
  SC: bm-payroll-social
  PR: bm-payroll-social
  TP: bm-corporate-income-tax
  XB: bermuda-tax
partial: {}
---

# Bermuda: tax pack

Bermuda has no personal income tax, no capital gains tax, no VAT or sales tax and no withholding tax. It charges payroll tax (employer and employee portions, tax year 1 April to 31 March), social insurance (contribution year from the first Monday of August), customs import duty, stamp duty and land tax. Since fiscal years beginning on or after 1 January 2025, Bermuda constituent entities of multinational groups with EUR 750 million revenue pay 15% corporate income tax, administered by the Corporate Income Tax Agency (CITA). Amounts are BMD, at par with the US dollar.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | not applicable, see above | |
| IT-CORP, corporate income tax | [bm-corporate-income-tax](bm-corporate-income-tax.md) | checked against the law |
| VAT / GST | not applicable; customs duty in [bermuda-tax](bermuda-tax.md) | |
| SC, social contributions | [bm-payroll-social](bm-payroll-social.md) | checked against the law |
| PR, payroll withholding | [bm-payroll-social](bm-payroll-social.md) | checked against the law |
| TP, transfer pricing | [bm-corporate-income-tax](bm-corporate-income-tax.md) (CIT Act s.37, in-scope groups only) | checked against the law |
| XB, cross-border | [bermuda-tax](bermuda-tax.md) | checked against the law |

## Other skills

- [Bermuda tax](bermuda-tax.md): start here; customs duty, stamp duty, land tax and routing.
- [Company formation](bm-company-formation.md).

## Official sources

Read on 2026-11-14: Office of the Tax Commissioner pages at gov.bm (payroll tax 2026-27, stamp duty, land tax), the Department of Social Insurance contribution calendar 2026-27, the Bermuda Customs Tariff 2026, the Corporate Income Tax Act 2023 and CITA deadlines at cita.bm, and the gov.bm limited companies page. Each skill lists its pages.
