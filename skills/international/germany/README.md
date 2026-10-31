---
jurisdiction: DE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  XB: leaving-germany-exit-tax
partial: {}
---

# Germany: tax pack

Calendar tax year. Authorities: the Bundeszentralamt für Steuern and the local Finanzamt; foreign businesses have a designated Finanzamt by country. Euro. Income tax with a solidarity surcharge and optional church tax; corporate tax at 15% plus trade tax set by each municipality; VAT at 19% (7% reduced), EU rules apply; social contributions split between employer and employee with annual ceilings.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | de-employee-income-tax, de-self-employed-income-tax, de-einkommensteuer-freelancer (2026 deep-tax shape: Freiberufler or trade, EÜR and Anlage EÜR/S/G, home office EUR 1,260 and EUR 6 day rate, GWG and 30% declining balance, § 7g, EUR 12,348 Grundfreibetrag and 2026 tariff, splitting, surcharge, church tax, § 10 caps, § 10d losses, § 37 prepayments, § 35 credit, § 149 deadlines, § 152 surcharge), de-capital-gains (2026 deep-tax shape: 25% flat tax, surcharge and church-tax formula, EUR 1,000/2,000 allowance, share and general loss pots, loss certificates, funds and the Vorabpauschale, § 17 partial-income method, § 23 one-year and ten-year rules and the EUR 1,000 Freigrenze, Günstigerprüfung, Anlage KAP), de-rental-income (2026 deep-tax shape: § 21 income, Werbungskosten, AfA 2%/2.5%/3%, § 7(5a) 5% declining balance, § 7b, the 15% three-year rule and § 82b, cheap lets at 50%/66%, holiday lets, losses, § 23 ten-year rule, Anlage V, deadlines and surcharges), de-estimated-tax (2026 deep-tax shape: § 37 prepayments, four dates, EUR 400/100 minimums, EUR 600 small-deductions rule, adjustment window, solidarity surcharge and church tax on prepayments, year-end balance, 1% surcharge, 1.8% interest); partners and the year of moving in or out in de-partners-and-part-year; non-residents in de-non-resident-tax | Source-cited draft; see scope limits below |
| IT-CORP, corporate income tax | de-corporate-tax; trade tax (Gewerbesteuer) for companies, partnerships and sole traders in de-trade-tax (2026: liability, § 8 add-backs, § 9 reductions, EUR 24,500 allowance, 3.5% base rate, 200% multiplier floor, § 35 EStG credit, § 10a losses, apportionment, prepayments, penalties) | Source-cited draft |
| VAT | germany-vat-return (2026 rates incl. 7% on restaurant food, filing rhythm, advance returns and 2026 box numbers, extension and special prepayment, § 13b, recapitulative statement, e-invoice dates, surcharges and interest); de-vat-annual-and-special-schemes (annual return, § 19 small businesses and the EU scheme, § 20 cash basis, extension and special prepayment, partial exemption, § 15a, § 13b, OSS, penalties, e-invoicing dates) | Source-cited draft; see scope limits below |
| SC, social contributions | de-social-contributions (2026 deep-tax shape: voluntary health minimum base EUR 1,318.33 and ceiling EUR 5,812.50, 14.0%/14.6% plus 2.9% average additional rate, care 3.6% with surcharge and child reductions, § 2 SGB VI compulsory pension groups, 18.6%, start phase and income bases, exemptions, KSK and the 4.9% levy, accident and unemployment on application, status procedure, due dates, surcharges, tax deduction; employee summary points to de-payroll) | Source-cited draft; see scope limits below |
| PR, payroll withholding | de-payroll (2026 deep-tax shape: wage tax classes I to VI through the 2026 PAP, Vorsorgepauschale, surcharge and church tax, 2026 contribution rates and ceilings, Minijob EUR 603 and Midijob band, Aktivrente, Lohnsteuer-Anmeldung, contribution due dates, DEÜV, payslip, minimum wage, tax-free surcharges, sick and maternity pay, penalties, cross-border withholding); de-payroll-benefits (2026: benefits in kind and the EUR 50 limit, company cars with the 1%, 0.03% and quarter or half list-price rules and the EUR 60,000, 70,000 and 100,000 caps, list-price rounding, logbook, 2026 meal and lodging values, § 37b 30% and § 40 flat taxes, tax-free items, employer pensions with the 8% and 4% limits, § 100 subsidy and salary sacrifice, managing directors and the § 7a status procedure); germany-payroll (older full-cycle version, overlaps de-payroll) | Source-cited draft; see scope limits below |
| TP, transfer pricing | germany-transfer-pricing | Source-cited draft; see scope limits below |
| XB, cross-border | de-non-resident-tax, leaving-germany-exit-tax, de-treaty-withholding-rates (German withholding on dividends, interest and royalties paid abroad; treaty rates for 12 partners; § 50c, § 43b, § 50g, § 50d(3)), germany-to-switzerland-cross-border-tax (2026, with the art. 15a commuter rules), de-uk-employer-first-hire | Source-cited draft; see scope limits below |

## Scope of this national core pack

The methods listed above are supplied for the stated 2026 scope. The following narrow branches remain outside this batch and require their own facts, source confirmation or specialist treatment. They are not assertions of zero tax, an exemption or a completed calculation for those facts. This map uses the repository's completion rule: `partial` is reserved for omitted coverage most clients need, rather than every unresolved local or conditional branch. The underlying Guide limitations remain in place.

| Recorded item | Named scope limit | Handling |
| --- | --- | --- |
| DE-M01 | State/church-specific church-tax selection, caps and rounding, including flat-rate and non-resident cases | Obtain the actual applicable state/church rules; the national conditional examples do not establish every local result. |
| DE-M02 | Foreign social contributions on salary before arrival or after departure in the specific moving-year case | Separate deduction determination; do not infer a zero deduction from the unresolved treatment. |
| DE-M03 | Foreign capital income in the section 1(3) eligibility and progression intersection | Refer that specific applicant computation; preserve the supplied qualified non-capital cases. |
| DE-M04 | Repeated travel to a rental property as a first place of activity; depreciation in the disposal month | Check those facts separately; the supplied ordinary rental and depreciation methods remain conditional on their stated scope. |
| DE-M05 | Whole-euro VAT return transcription, VAT calendar-year gift aggregation and particular entertainment-receipt formalities | Follow the actual current form and evidence requirements; an income-tax test does not establish a different VAT rule. |
| DE-M06 | Exact OSS weekend deadline treatment for the recorded quarter | Retain the supplied early operational filing/payment route; the later local draft correction is not part of these frozen reviewed bytes. |
| DE-M07 | Particular startup pension, non-statutory-insured spouse income and owner accident-insurance expense interactions | Determine the actual scheme and taxpayer-specific treatment before computing the excluded branch. |
| DE-M08 | Saxony Midijob care-contribution allocation | Separate local worksheet required; do not substitute the outside-Saxony algorithm. The unpublished follow-up remains separate. |
| DE-M09 | Support-fund/direct-promise employer pensions and particular collective-agreement or actual-saving top-up conditions | Refer the actual arrangement; the listed ordinary pension routes retain their stated conditions. |
| DE-M10 | SME documentation relief applied to the distinct audit transaction-matrix obligation | Do not infer an audit handover exemption from threshold arithmetic alone. |
| DE-M11 | Particular Swiss commuter return-count, leave/sickness, home-office and CHF-to-EUR conversion questions | Preserve the limited corridor examples; obtain the actual treaty/application and conversion determination for those facts. |

These are source-cited drafts. The completed independent review and the unchanged Guide hashes are recorded in each Guide's ledger. This batch carries no accountant attestation. Accounting/workflow material outside the reviewed 25-Guide population is not newly accepted by this packaging change.

## Official sources

- Einkommensteuergesetz (EStG): https://www.gesetze-im-internet.de/estg/
- Körperschaftsteuergesetz (KStG): https://www.gesetze-im-internet.de/kstg_1977/
- Umsatzsteuergesetz (UStG): https://www.gesetze-im-internet.de/ustg_1980/
- Gewerbesteuergesetz (GewStG): https://www.gesetze-im-internet.de/gewstg/
- Bundeszentralamt für Steuern: https://www.bzst.de
