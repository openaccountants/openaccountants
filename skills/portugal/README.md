---
jurisdiction: PT
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
partial: {}
---

# Portugal: tax pack

Calendar tax year for individuals; companies use the calendar year unless they adopt another period. Authority: the Autoridade Tributária e Aduaneira (AT), through the Portal das Finanças; social security through the Segurança Social. Euro. Individuals pay IRS, companies pay IRC (19% for periods starting in 2026, falling to 17% from 2028) with the derrama estadual and municipal surcharges; VAT (IVA) under EU rules.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | pt-irs-employees-investment (employees, pensioners, capital income, rent and capital gains, tax year 2026); pt-income-tax (self-employed, Category B, tax year 2026); portugal-crypto-tax (crypto gains, rewards, mining and the exit charge on leaving, tax year 2026) | checked against the law |
| IT-CORP, corporate income tax | pt-corporate-tax (tax year 2026: 19% for periods starting in 2026, 15% SME and 12.5% startup rate on the first EUR 50,000, derrama municipal up to 1.5% and derrama estadual 3%/5%/9%, autonomous taxation, losses at 65% (75% for 2020-2021 losses), interest limit, participation exemption, payments on account, Modelo 22 and IES, fines and 7.221% late interest, SIFIDE II and RFAI; Madeira and Azores 13.3% and 10.5%, CINM 5%; regional surcharges not covered) | checked against the law |
| VAT | portugal-vat-return (tax year 2026: mainland, Azores and Madeira rates, art. 53 exemption EUR 15,000, monthly or quarterly returns, deadlines, refunds, penalties) | sourced from the law |
| SC, social contributions | pt-social-contributions (tax year 2026: self-employed 21.4% and 25.2%, relevant income 70%/20%, quarterly declaration, EUR 20 minimum, first 12 months, 4 x IAS and 12 x IAS on the 2026 IAS of EUR 537.13, contracting entities 10%/7%, employee 11% and employer 23.75%, MOE, deadlines, fines and interest); the payroll run inside portugal-payroll (tax year 2026) | checked against the law |
| PR, payroll withholding | portugal-payroll (tax year 2026: mainland, Azores and Madeira withholding tables, November 2026 cut, subsidies and twelfths, meal allowance, IRS Jovem, DMR and Social Security deadlines) | checked against the law |
| TP, transfer pricing | pt-transfer-pricing | checked against the law |
| XB, cross-border | pt-cross-border (residence, non-residents, exit tax, outbound withholding, tax year 2026); pt-foreign-source-treaties (foreign income of residents, foreign tax credit, tax year 2026); pt-nhr-ifici (tax year 2026: IFICI entry test and the seven activity routes, 15 January registration, 20% on qualifying A and B income, foreign-income exemption, 35% on listed low-tax jurisdictions, the NHR transitional group and 10% pensions, IRS Jovem bar, penalties) | checked against the law |

The coverage report counts a domain as present when a skill's slug matches it, and counts a domain listed under `partial` as missing. It does not check tax year. Gaps: none listed.

Other skills in this folder (bookkeeping, e-invoicing, financial statements, formation, tax optimisation, return assembly) belong to the accounting milestone and are not counted here.

## Official sources

- Portal das Finanças, tax codes (CIRC, CIRS, CIVA, RGIT, LGT): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/ (read 2026-10-22)
- Diário da República: https://diariodarepublica.pt (read 2026-10-22)
- Segurança Social: https://www.seg-social.pt
