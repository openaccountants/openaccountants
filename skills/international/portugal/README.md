---
jurisdiction: PT
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
partial:
  VAT: "pt-vat-return still carries the 2025 rules and is not yet a pointer to portugal-vat-return; its body can only change once its last_updated can advance past 2026-10-23"
---

# Portugal: tax pack

Calendar tax year for individuals; companies use the calendar year unless they adopt another period. Authority: the Autoridade Tributária e Aduaneira (AT), through the Portal das Finanças; social security through the Segurança Social. Euro. Individuals pay IRS, companies pay IRC (19% for periods starting in 2026, falling to 17% from 2028) with the derrama estadual and municipal surcharges; VAT (IVA) under EU rules.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | pt-irs-employees-investment (employees, pensioners, capital income, rent and capital gains, tax year 2026); pt-income-tax (self-employed, Category B, tax year 2026); portugal-crypto-tax (crypto gains, rewards, mining and the exit charge on leaving, tax year 2026) | source-cited draft |
| IT-CORP, corporate income tax | pt-corporate-tax | source-cited draft |
| VAT | portugal-vat-return (tax year 2026: mainland, Azores and Madeira rates, art. 53 exemption EUR 15,000, monthly or quarterly returns, deadlines, refunds, penalties); pt-vat-return is the older 2025 version, to be turned into a pointer | source-cited draft |
| SC, social contributions | pt-social-contributions (self-employed, tax year 2026); employee and employer rates inside portugal-payroll (tax year 2026) | source-cited draft |
| PR, payroll withholding | portugal-payroll (tax year 2026) | source-cited draft |
| TP, transfer pricing | pt-transfer-pricing | source-cited draft |
| XB, cross-border | pt-cross-border (residence, non-residents, exit tax, outbound withholding, tax year 2026); pt-foreign-source-treaties (foreign income of residents, foreign tax credit, tax year 2026); pt-nhr-ifici | source-cited draft |

The coverage report counts a domain as present when a skill's slug matches it, and counts a domain listed under `partial` as missing. It does not check tax year. Gaps: none listed.

Other skills in this folder (bookkeeping, e-invoicing, financial statements, formation, tax optimisation, return assembly) belong to the accounting milestone and are not counted here.

## Official sources

- Portal das Finanças, tax codes (CIRC, CIRS, CIVA, RGIT, LGT): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/ (read 2026-10-22)
- Diário da República: https://diariodarepublica.pt (read 2026-10-22)
- Segurança Social: https://www.seg-social.pt
