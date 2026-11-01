---
jurisdiction: SJ
applicable: [IT-IND, IT-CORP, SC, PR, TP, XB]
not_applicable:
  VAT: "Merverdiavgiftsloven s 1-2(2) places Svalbard outside the Norwegian VAT area (lovdata.no/dokument/NL/lov/2009-06-19-58, read 2026-10-31). Purchases made in mainland Norway are a separate question."
covered_by:
  IT-CORP: sj-svalbard-company-income-tax
  XB: sj-svalbard-tax-residence
partial:
  IT-IND: "no individual income tax skill; the slug match comes from the company skill, and sj-svalbard-payroll-tax covers salary tax only"
  XB: "individual residence, temporary work and departure only; companies, mainland departure and treaties are not covered"
---

# Svalbard: tax pack

Svalbard has its own tax act (Svalbard Tax Act) and tax rates set by annual Storting decision. This pack covers Svalbard only, not Jan Mayen.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | (missing) | |
| IT-CORP, corporate income tax | sj-svalbard-company-income-tax | sourced from the law |
| VAT | not applicable, see above | |
| SC, social contributions | (missing) | |
| PR, payroll withholding | sj-svalbard-payroll-tax | sourced from the law |
| TP, transfer pricing | (missing) | |
| XB, cross-border | sj-svalbard-tax-residence | sourced from the law, partial |

## Official sources

- Merverdiavgiftsloven: https://lovdata.no/dokument/NL/lov/2009-06-19-58 (read 2026-10-31)
- Skatteetaten, tax rates on Svalbard: https://www.skatteetaten.no/en/rates/tax-rates-on-svalbard (read 2026-10-31)

Each skill lists its own sources with the date last read.
