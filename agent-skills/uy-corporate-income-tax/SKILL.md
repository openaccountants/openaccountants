---
name: uy-corporate-income-tax
description: "Uruguay corporate income tax (IRAE, Impuesto a las Rentas de las Actividades Económicas) for tax year 2026 under Título 4 of the Texto Ordenado 2023 as amended by Ley 20.446, and its regulation Decreto 150/007. Covers who pays (companies, SAS, permanent establishments, trusts, sole traders with business income), the 25% rate, Uruguayan source and the 2026 rules on indirect share transfers, the base and its deduction rules (the proportional deduction for payments taxed at lower rates, the 150% deductions, non-deductible items), five-year indexed losses, the fictitious-profit regime and the UI 4,000,000 accounting threshold, the UI 305,000 small-business exemption, the option for independent professionals, monthly advances and the 2026 minimum monthly payments (Decreto 310/025), the annual return in the fourth month, IRNR rates on dividends and other payments to non-residents, and the 15% domestic minimum top-up for EUR 750 million groups. Trigger on: IRAE 2026, impuesto a la renta empre"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uy-corporate-income-tax"
  jurisdiction: "UY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Uruguay: corporate income tax (IRAE) for 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes the IRAE of a business for a fiscal year in 2026. It links to the other Uruguay skills and does not repeat them:

- [uruguay-income-tax](uruguay-income-tax.md): IRPF, including the 7% tax on dividends that individuals receive from IRAE-taxed profits.
- [uruguay-iva](uruguay-iva.md): VAT.
- [uruguay-payroll](uruguay-payroll.md) and [uruguay-social-contributions](uruguay-social-contributions.md): employer obligations.

**Which text of the law.** Título 4 (IRAE) of the Texto Ordenado 2023 approved by Decreto 101/024, as consolidated by IMPO with the changes of Ley 20.446 of 16 December 2025 (Diario Oficial 8 January 2026). The regulation is Decreto 150/007, whose article references still use the older numbering of the Título (for example "literal E) del artículo 52" is today's art. 66 E). Non-resident rates come from Título 8 (IRNR); the minimum top-up tax from Título 21. Thresholds in UI (Unidad Indexada) are converted at the quotation the rule names, usually at the year-end close.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Rate | 25% of the renta neta fiscal (T4 art. 23) |
| Fiscal year | The company's financial year if it keeps sufficient accounts; otherwise the calendar year (art. 17) |
| Losses | Carried forward up to 5 years, indexed by IPC (art. 32 F) |
| Return and balance | By the fourth month after the year-end (Res. DGI 1478/007, num. 9) |
| Minimum monthly payment 2026 | UYU 6,840 to UYU 19,240 depending on last year's income (Decreto 310/025) |
| Dividends paid to individuals or non-residents | 7% (IRPF or IRNR) |

## Who this applies to

- **Taxed on any income, whatever the factors used** (T4 art. 12 A): sociedades anónimas and en comandita por acciones; other commercial companies under Ley 16.060 and SAS (Ley 19.820); agrarian associations and companies; permanent establishments of non-residents; State commercial and industrial entities; closed credit funds and open investment funds investing only in non-resident securities; trusts other than guarantee trusts; de facto and civil companies, except those formed only by resident individuals (art. 12 A 8).
- **Taxed on business income** (art. 12 B): any business combining capital and labour in industrial, commercial or service activity, and farming. Income of university-qualified professionals and similar listed occupations is not business income while labour is the predominant factor; it stays in IRPF unless the person opts or is required to move (art. 14).
- **Assimilated income** (art. 13): sales of land lots from subdivisions of more than 25 lots, and more than two property sales a year above the stated value, with exceptions for property held ten years or more.
- **Residence** (art. 3): entities incorporated under Uruguayan law; foreign entities that move their domicile to Uruguay. Under Ley 20.446 an entity that ceases to be resident must close its fiscal year at that date (art. 17).
- **Permanent establishment** (art. 4): a fixed place of business, including construction or installation works lasting more than three months and services through staff for more than six months in any twelve-month period, plus dependent agents. Auxiliary and preparatory activities are excluded.
- **Out of scope.** Large-scale mining (the IRAE additional, arts. 124 to 135), farming under IMEBA, free-zone users, promoted-investment exemptions under Ley 16.906, and the detailed transfer-pricing rules (arts. 46 to 58).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| IRAE rate on renta neta fiscal | 25% | 2026 | https://www.impo.com.uy/bases/todgi-2023/4-2024 (T4 art. 23) |
| Losses of earlier years | Deductible for 5 years after the year of the loss, indexed by IPC (fiscal years from 1 January 2016), oldest first | 2026 | same, art. 32 F |
| Payment taxed for the recipient in IRPF Categoría I or in IRNR (for example rent paid to an individual, interest to a non-resident) | Deductible in the proportion 12% / 25% (48%); 100% if the IRNR 25% rate applies | 2026 | same, art. 31 |
| Payment taxed abroad at an effective rate of 25% or more | 100% deductible; a lower effective rate gives a proportional deduction | 2026 | same, art. 31 |
| Training in priority areas, quality certification, lab accreditation and other listed expenses | Deductible at 150% of the real amount | 2026 | same, art. 34 |
| Employment promotion | Extra deduction of 50% of the lowest of three measures of wage-bill growth | 2026 | same, art. 34 H |
| Contributions to employees' voluntary pension savings (AFAP) | Deductible up to the employee's compulsory individual-savings contribution, at most UI 15,000 a year per employee | 2026 | same, art. 33 C |
| Food donations under Ley 20.177 | Up to the lower of 2% of gross income and 5% of the previous year's taxed net income | 2026 | same, art. 33 N |
| Inflation adjustment | Only in a year when IPC rose more than 100% over the 36 months before the close | 2026 | same, art. 38 |
| Small business exemption (art. 66 E) | Exempt while yearly income does not exceed UI 305,000 (UI at the start of the fiscal year) | 2026 | https://www.impo.com.uy/bases/decretos/150-2007 (Decreto 150/007 art. 122) |
| Sufficient accounting required for SA, PE, State entities, funds and trusts | Always | 2026 | same, art. 168 a); T4 art. 111 |
| Sufficient accounting required for other companies, sole traders, SAS and IRPF taxpayers who opted in | When last year's income exceeded UI 4,000,000 (UI at the year-end close) | 2026 | same, Decreto 150/007 art. 168 b), c) |
| Independent professional income: compulsory move from IRPF to IRAE | When fees in the year exceed UI 4,000,000; IRAE from the first month of the next year | 2026 | same, Decreto 150/007 art. 7 |
| Fictitious profit, businesses not obliged to keep sufficient accounts, fiscal years from 2023: income up to UI 1,000,000 / over 1,000,000 to 2,000,000 / over 2,000,000 to 3,000,000 / over 3,000,000 | 12% / 14% / 48% / 60% of each tranche, minus admitted owners' salaries | 2026 | same, Decreto 150/007 art. 64 |
| Fictitious profit, IRPF labour income taxed in IRAE by option: up to UI 2,000,000 / over 2,000,000 to 3,000,000 / over 3,000,000 | 48% / 60% / 72% | 2026 | same, Decreto 150/007 art. 64 |
| Minimum monthly payment, last year's income up to 1.5 times the art. 66 E limit | UYU 6,840 | 2026 | https://www.impo.com.uy/bases/decretos/310-2025 (art. 2) |
| Over 1.5 up to 3 times / over 3 up to 6 times / over 6 up to 12 times / over 12 up to 24 times / over 24 times | UYU 7,740 / 8,460 / 11,360 / 15,390 / 19,240 | 2026 | same, art. 2 |
| International transport (Uruguay to abroad) | Uruguayan-source net income fixed at 10% of gross fares and freight | 2026 | https://www.impo.com.uy/bases/todgi-2023/4-2024 (art. 60 A) |
| Digital intermediation services | 100% Uruguayan source if both parties are in Uruguay; 50% if one is abroad | 2026 | same, art. 60 E |
| IRNR on dividends paid by IRAE taxpayers to non-residents | 7% | 2026 | https://www.impo.com.uy/bases/todgi-2023/8-2024 (T8 art. 18 B) |
| IRNR on income of residents of low or no-tax jurisdictions (except IRAE dividends) | 25% | 2026 | same, art. 18 B |
| IRNR, other income (royalties, services, most interest) | 12%; reduced rates on local deposits and listed debt as in IRPF | 2026 | same, art. 18 |
| Domestic minimum top-up tax (IMCD) | Charged when the group's effective rate in Uruguay is below 15%; groups with consolidated revenue of EUR 750,000,000 or more in at least 2 of the 4 previous years | 2026 | https://www.impo.com.uy/bases/todgi2023/101-2024/3_T21 (T21 arts. 2, 3) |

## The base

- **Gross income** (T4 art. 24): the total product of the year's operations, accrued.
- **Deductible expenses** (art. 30): accrued in the year, necessary to obtain and keep taxed income, and documented. An expense is deductible only if it is taxed income for the other party in IRAE, IRPF, IRNR or an effective foreign income tax. Wages are deductible only if the social-security contributions on them were paid.
- **Proportional deduction** (art. 31): where the recipient is taxed in IRPF Categoría I or IRNR at 12%, only 12/25 of the expense is deductible; for foreign recipients the ratio of the effective foreign rate to 25%.
- **Other deductions** (arts. 32, 33): casualty and theft losses not covered by insurance, bad debts, depreciation, amortisation of intangibles with a real investment and identified seller, earlier losses (5 years), and the listed exceptions such as salaries exempt from IRPF by the mínimo no imponible, taxes other than IRAE and Impuesto al Patrimonio, and donations to public bodies.
- **Not deductible** (art. 35): owners' personal expenses, illegal losses, tax penalties, profit withdrawals, IRAE itself, Impuesto al Patrimonio, goodwill amortisation, the minimum top-up tax, professional fees not paid by the means Ley 19.210 requires, and freight not paid electronically. Expenses that produce untaxed income are disallowed in proportion.
- **Financial expenses** (art. 36): deducted only through the ratio of average assets producing taxed income to average total assets at fiscal values.
- **Uruguayan source** (art. 16): activities, assets or rights used in Uruguay. From 2026 the sale of shares in a non-resident entity is Uruguayan-source when, at any time in the previous 365 days, more than 50% of its assets were in Uruguay, or Uruguayan assets exceeded UI 31,500,000 and more than 50% of them changed hands; the Uruguayan share follows the asset ratio. Intra-group restructurings with 95% common ownership kept for two years are excluded.
- **Order of the computation:** accounting profit, add back non-deductible items and the disallowed part of proportional expenses, subtract extra 50% deductions and exempt income, subtract indexed losses, multiply by 25%, subtract advances paid for the year (the minimum monthly payments are credited first; an excess of those over the tax gives no credit, Decreto 150/007 art. 164).

## Deadlines and filing

| Step | What and where | Source |
|---|---|---|
| Annual return | Form 1050 (IRAE, ICOSA and Impuesto al Patrimonio) for CEDE, NO CEDE and large taxpayers, through the DGI PADI application, filed even without activity | [DGI, form 1050](https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/documentos/publicaciones/Charla%20externa%20formulario%201050.pdf) |
| Due date of return and balance | Within the fourth month after the fiscal year-end, on the date of the general deadline table (Res. DGI 1478/007, num. 9). A calendar 2026 year: April 2027 | [DGI, vencimientos](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-pagos-cuenta-saldos-declaraciones-juradas) |
| Advances (anticipos) | Monthly: last year's ratio of IRAE to taxed gross income times this month's income, minus the minimum monthly payment. Not due in the first year of activity. Taxpayers may file a provisional return instead if the advances would exceed the year's tax (Decreto 150/007 arts. 165, 166) | [Decreto 150/007](https://www.impo.com.uy/bases/decretos/150-2007) |
| Quarterly advances | Where payable quarterly, in the fifth, eighth and eleventh months of the year and the second month of the next | [DGI, vencimientos](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-pagos-cuenta-saldos-declaraciones-juradas) |
| Minimum monthly payment | Every month from the first month with taxed income, at the 2026 amount for last year's income band; new businesses use the lowest band (Decreto 150/007 arts. 170, 172) | [Decreto 310/025](https://www.impo.com.uy/bases/decretos/310-2025) |
| Payment | Boleto 2908 through Servicios en Línea, then Abitab, Red Pagos or online banking | DGI, vencimientos |
| Cessation | A sale or closure of the business ends the fiscal year and needs a return (T4 art. 112) | T4 art. 112 |

## Penalties and interest

- **Late payment** of the balance or of advances: fine of 5% (within 5 working days), 10% (up to 90 days) or 20% (after that), plus a monthly surcharge set by the Executive (Código Tributario art. 94). Paying less than the advances due without a justified provisional return is mora on the shortfall (Decreto 150/007 art. 166).
- **Late filing:** UYU 910 per return in 2026 (Res. DGI 97/026).
- **Joint liability:** partners of personal companies and directors are jointly liable for the tax and the mora (T4 art. 119).

## Cross-border points

- **Withholding by IRAE taxpayers** on Uruguayan-source payments to non-residents at the IRNR rates in the table (T4 art. 113). Dividends paid out of untaxed income are exempt; dividends from listed shares are exempt (T8 art. 19 C).
- **Permanent establishments** compute all Uruguayan income of the foreign entity, except PEs created by construction or services, which compute only the income connected with them (art. 21). They must appoint a resident representative (art. 22).
- **Foreign tax credit** for multinational group entities on income under art. 16 numerals 6 and 7, capped at the Uruguayan tax on that income (art. 118).
- **Transfer pricing** applies to transactions with related parties and low-tax jurisdictions (arts. 46 to 58); a separate skill should cover it.

## Two worked examples that recompute

### Example 1: SA with a proportional expense and a loss carried forward

Delta SA has a calendar 2026 year and keeps full accounts. Its accounting profit is UYU 10,000,000. That profit is after UYU 200,000 of DGI fines, UYU 600,000 of office rent paid to a resident individual (taxed for her in IRPF Categoría I), and UYU 400,000 of approved priority-area staff training. It has an indexed loss of UYU 1,500,000 from 2023. It paid UYU 1,600,000 of advances (including the minimum monthly payments) for 2026.

Add back the fines (not deductible): UYU 200,000. Only 12/25 of the rent is deductible, UYU 288,000, so add back UYU 312,000. The training counts at 150%, so subtract the extra UYU 200,000. Subtract the 2023 loss, still within five years. The renta neta fiscal is 10,000,000 + 200,000 + 312,000 - 200,000 - 1,500,000 = UYU 8,812,000, and IRAE is UYU 2,203,000. After advances, UYU 603,000 is due with form 1050 in April 2027.

```oa-check
name: UY IRAE 2026, SA with proportional rent deduction and loss
inputs:
  book_profit: 10000000
  fines: 200000
  rent_to_individual: 600000
  training: 400000
  loss_2023: 1500000
  advances: 1600000
steps:
  - rent_deductible: rent_to_individual * 0.12 / 0.25
  - rent_addback: rent_to_individual - rent_deductible
  - training_extra: training * 0.5
  - taxable: book_profit + fines + rent_addback - training_extra - loss_2023
  - irae: taxable * 0.25
  - balance: irae - advances
expected:
  rent_deductible: 288000
  rent_addback: 312000
  training_extra: 200000
  taxable: 8812000
  irae: 2203000
  balance: 603000
```

### Example 2: should an independent architect move from IRPF to IRAE?

Sofía is a resident architect billing UYU 1,800,000 in 2026, with no staff, under UI 2,000,000 and under the UI 4,000,000 compulsory limit. She paid UYU 250,000 of pension contributions. Her real expenses are about UYU 900,000.

Staying in IRPF: renta computable is 70% of fees, UYU 1,260,000 (the 30% flat deduction). Tax on the scale is 86,486.40 to 180 BPC plus 24% of the excess over UYU 1,235,520, so UYU 92,361.60. Her nominal income is above 180 BPC, so the deduction credit is 8% of 250,000 = UYU 20,000. IRPF: UYU 72,361.60.

Opting into IRAE with fictitious profit: 48% of fees is UYU 864,000, at 25% UYU 216,000. With real accounts instead: (1,800,000 - 900,000) at 25% = UYU 225,000. Both are before the admitted notional owner's salary (art. 32 G) and before the 7% IRPF on profits she withdraws.

The decision: at this income she stays in IRPF, which costs about UYU 144,000 less. The IRAE option starts to pay only where the IRPF marginal rates (31% and 36%) apply to a large part of the income and real expenses are high; above UI 4,000,000 of fees IRAE is compulsory anyway. Once she opts, she must stay in IRAE for the minimum number of years the regulation sets (art. 14).

```oa-check
name: UY 2026, independent professional, IRPF vs IRAE option
inputs:
  bpc: 6864
  fees: 1800000
  contributions: 250000
  real_expenses: 900000
steps:
  - renta: fees * 0.70
  - tax_to_180: (120 * bpc - 84 * bpc) * 0.10 + (180 * bpc - 120 * bpc) * 0.15
  - irpf_scale: tax_to_180 + (renta - 180 * bpc) * 0.24
  - credit: contributions * 0.08
  - irpf: irpf_scale - credit
  - irae_ficto: fees * 0.48 * 0.25
  - irae_real: (fees - real_expenses) * 0.25
  - saving_irpf: irae_ficto - irpf
expected:
  renta: 1260000
  tax_to_180: 86486.40
  irpf_scale: 92361.60
  credit: 20000
  irpf: 72361.60
  irae_ficto: 216000
  irae_real: 225000
  saving_irpf: 143638.40
```

## Ask the client first

1. Legal form (SA, SRL, SAS, sole trader, PE, trust, de facto company) and the fiscal year-end.
2. Last year's income in pesos and in UI: it decides the small-business exemption, sufficient accounting or fictitious profit, and the 2026 minimum-payment band.
3. Who receives the main expenses: individuals in IRPF Categoría I, non-residents (and their country and effective rate), or IRAE taxpayers.
4. Losses of the last five years, with their year of origin and IPC indexation.
5. Advances and minimum payments already made for the year, and any provisional return.
6. Foreign shareholders, related parties abroad, a group with consolidated revenue of EUR 750 million or more, any free-zone or promoted-investment status.

## Sources

| Source | URL | Read on |
|---|---|---|
| Texto Ordenado 2023, Título 4 IRAE, IMPO consolidated text with Ley 20.446: arts. 1 to 40, 59, 60, 110 to 123 read | https://www.impo.com.uy/bases/todgi-2023/4-2024 | 2026-11-11 |
| Decreto 150/007 (IRAE regulation), arts. 7, 64, 122, 123 bis, 164 to 177 read | https://www.impo.com.uy/bases/decretos/150-2007 | 2026-11-11 |
| Decreto 310/025, art. 2: 2026 minimum monthly payments | https://www.impo.com.uy/bases/decretos/310-2025 | 2026-11-11 |
| Texto Ordenado 2023, Título 8 IRNR, arts. 18 and 19 read | https://www.impo.com.uy/bases/todgi-2023/8-2024 | 2026-11-11 |
| Texto Ordenado 2023, Título 21 IMCD, arts. 1 to 6 read | https://www.impo.com.uy/bases/todgi2023/101-2024/3_T21 | 2026-11-11 |
| DGI, vencimientos de pagos a cuenta, saldos y declaraciones juradas (guide and PDF), read for the fourth-month rule and quarterly advances | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-pagos-cuenta-saldos-declaraciones-juradas | 2026-11-11 |
| DGI, form 1050 presentation, read for who files and the deadline | https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/documentos/publicaciones/Charla%20externa%20formulario%201050.pdf | 2026-11-11 |
| Código Tributario, art. 94 (mora) | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 | 2026-11-11 |
| Resolución DGI 97/026, numeral 1 read for the late-return fine | https://www.impo.com.uy/bases/resoluciones-dgi/97-2026 | 2026-11-11 |
| Decreto 11/026, art. 1: BPC 2026 (for the IRPF side of Example 2) | https://www.impo.com.uy/bases/decretos/11-2026 | 2026-11-11 |

Not yet confirmed: the notional "trading" regime (3% of gross) carried by the old file, which was not found in Decreto 150/007 as read; the IMCD start date and its computation rules (Título 21 arts. 7 onward and Decreto 206/026 not read); the monthly recargo rate for 2026; the 2026 UI quotation used to convert the UI thresholds; the minimum years an IRAE option binds; the notional owner's salary amounts under art. 32 G; whether the fictitious-profit 48% / 60% / 72% professional scale applies by tranche; the exact April 2027 day in the deadline table; IRNR rates on interest by instrument for non-residents beyond the table; the reduced rates and exemptions for promoted investment, free zones and software; Monotributo (BPS) as the alternative for very small businesses, which the old file mentioned without figures.

> Contributed by OpenAccountants.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uy-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uy-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
