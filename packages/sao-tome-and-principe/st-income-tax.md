---
name: st-income-tax
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It covers IRS categories A to D, residence (more than 180 days, a home on 31 December, centre of interests), the 2009 annual band table, monthly withholding, 15% withholding on Category B fees and final 15% withholding on capital income, prizes and non-residents, the Db 25,000 lottery exemption, the cash limit, filing in February or by 30 April, payment by 30 September, and the held 30% band and IERS history. It says plainly which figures come from official texts and which remain held. Trigger phrases: Sao Tome personal income tax, IRS Sao Tome, STP tax return, Direccao dos Impostos, dobras, imposto sobre o rendimento de pessoas singulares. It is general reference for working papers, not for filing without review by a qualified professional in the country."
jurisdiction: ST
tax_year: 2026
last_updated: 2026-11-16
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
category: international
tier: 2
domain: income-tax
---

# Sao Tome and Principe Personal Income Tax v0.3

> **Sourced from the law, in part.** Tax year 2026. The IRS code was read in its 2009 republication on the Ministry of Finance legacy site. Later amendments, the 2024 Budget changes and the published 2026 Budget Law were not read on an official host, so the current band table is held: see `Not yet confirmed:` under Sources. No accountant has signed this version.

## Who this applies to

Individuals with income in four categories ([IRS code art. 1](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf)):

- **Category A:** employment income, pensions and life annuities.
- **Category B:** business and professional income.
- **Category C:** capital income.
- **Category D:** capital gains and other increases in wealth, including lottery, raffle, totoloto, bingo and other prizes (art. 20(2) as amended by Law 11/2009).

Income in cash or in kind is taxed, in any currency, even if it comes from unlawful acts (art. 1(3)). The code is Law 17/2008, first amended and republished by Law 11/2009 of 8 October 2009, in force on publication (Law 11/2009 art. 5).

**Residents** pay on worldwide income; **non-residents** only on income obtained in STP (art. 35). A person is resident for a year if, in that year, any of these applies (art. 36(1)):

- stayed in STP more than 180 days, in a row or not;
- had a home in STP on 31 December that suggests the intention to keep it as a permanent residence;
- has the main centre or base of professional or business activity or economic interests in STP;
- holds a public post abroad for STP;
- on 31 December is crew of a ship or aircraft serving an entity resident or managed in STP.

The older skill gave the day test as 183 days; the code says more than 180 days.

**Groups for Category B.** Group 1 keeps organised accounts and Group 2 keeps simplified books, by the IRC code's rules (arts. 112, 113 and [company tax](st-corporate-income-tax.md)). Agriculture: 50% of income from an exclusively agricultural and livestock activity is exempt, after losses (art. 10.ºA, added by Law 11/2009).

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Annual band table, Categories A, B and D after aggregation | Up to Dbs. 11.700.000,00 0%; 10% to Dbs. 50.000.000,00 less Dbs. 881.250,00; 13% to Dbs. 100.000.000,00 less Dbs. 1.380.000,00; 15% to Dbs. 150.000.000,00 less Dbs. 1.875.000,00; 20% to Dbs. 240.000.000,00 less Dbs. 5.625.000,00; 25% above, less Dbs. 9.000.000,00. Printed in dobras before the re-denomination | 2009 text, in force from 8 Oct 2009; 2026 status held | [Law 11/2009 art. 1, amending art. 66](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| Monthly withholding table, Category A | From Dbs. 975.001,00 8%; from Dbs. 4.167.001,00 11%; from Dbs. 8.333.001,00 13%; from Dbs. 12.500.001,00 18%; above Dbs. 20.000.000,00 23%. Printed in dobras before the re-denomination | 2009 text; 2026 status held | [Law 11/2009 art. 1, amending art. 68](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| Withholding on Category B fees | 15% of gross Category B income from STP paid to residents by entities that keep or must keep organised accounts; a payment on account of the final tax | 2009 text | [IRS code arts. 68 and 91 (republished numbering)](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| Final (liberatory) withholding | 15% of gross amount, final: capital income from STP not in Category B; Category D gains from STP not in Category B; other STP income of non-residents without a permanent establishment there | 2009 text | [IRS code art. 69](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| Lottery prizes, Category D | National totoloto prizes of Dbs. 25.000,00 or less are exempt | 2025 Law; same text in the 2026 Bill, art. 8 approved 11 Feb 2026 | [2025 Budget Law art. 8(18)](https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf); [2026 Budget Bill art. 8(18)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |
| Cash limit | Taxpayers with organised accounts may not pay or receive Dbs. 10.000,00 or more in cash; split payments for one deal are added together; the excess cash expense is not deductible | 2025 Law; art. 9 of the 2026 Bill approved unchanged 11 Feb 2026 | [2025 Budget Law art. 9](https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf); [2026 debate](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Personal and family deduction from tax | 10% of the annual minimum wage per taxpayer; 15% with one dependant, 20% with two, 25% with three or more; raised to 35% for 60% or more permanent invalidity | 2009 text; minimum wage for 2026 not read | [Law 11/2009 art. 1, amending art. 75](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |
| Health and education deductions from tax | 10% of qualifying health spending (taxpayer, household, ascendants and first-degree collaterals) and of education and training spending, each up to Dbs. 1.000.000,00 | 2009 text | [Law 11/2009 art. 1, amending arts. 77 and 78](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf) |

Article numbers: a row that says "amending" uses the numbering of Law 11/2009 art. 1; every other reference uses the numbering of the code as republished in the same Gazette (Law 11/2009 art. 4(2) renumbered arts. 67 to 134). The band table is printed with these "parcela a abater" (amount to deduct) values; they do not make the bands continuous. Apply them as printed and flag the result for review.

## The base

- **Aggregation.** Categories A, B and D are aggregated and taxed with the art. 66 table (art. 66(1)). Category D net gains are aggregated only if a resident opts to declare them, and that option obliges the person to declare all income (art. 70).
- **Employer withholding.** Employers withhold on employment income and pensions (art. 89). Where Category A comes from one payer only, that payer withholds at the art. 66 rates and deducts 1/12 of the personal deduction each month (art. 90 as amended); if that changes, the employee must tell the employer, who then uses the monthly table (art. 90(2)).
- **Withholding by others.** Entities with organised accounts, public bodies, international organisations and NGOs withhold on Category B, C and D income and on STP income of non-residents without a permanent establishment (art. 91).
- **Deductions from tax** apply in this order: personal and family situation, international double taxation, health, education and training, housing costs; then payments on account and amounts withheld. Only the last two are refundable (art. 73). Deductions under art. 73(1) are for residents only (art. 73(4)).
- **Company car.** An employer-provided car is taxed at 0.50% of its customs or purchase value per month of use (Law 11/2009 art. 1, amending art. 43(3)).
- **Category B expenses.** Pay to the owner and household members working in the business is not deductible; costs of an own car used in the business are capped at 3% of booked income (art. 49(4) and (5) as amended).

**Held: the 30% band and the special tax IERS.** The 2024 Budget text (Assembly Diario II no. 25 of 22 Dec 2023, art. 8(11) and (12)) added a band of 30% for income of Db 420,000 or more less Db 45,048, and a special tax (IERS) of 20% on monthly disposable income above Db 50,000. In the debate of 11 February 2026 the Minister said the IERS was dropped in 2025, that a Constitutional Court ruling returned the 2024 measures to their earlier base, and that the government "decided to keep" the 30% rate. The 2025 Budget Law read has no IERS and no band change. The ruling and any law restoring the 30% band were not read, so do not use it. For the record, the older skill's two worked cases on that band were: income of Db 500,000 gives tax of Db 104,952 (500,000 x 30% less 45,048), and income of exactly Db 420,000 ("equal or above") gives Db 80,952. Whether Db 420,000 is annual or monthly was never stated in the Budget text.

## Deadlines and filing

| Step | When | Where and how |
|---|---|---|
| Start of Category B activity | Declare 15 days before starting (art. 109(1)(a)) | Direccao dos Impostos or the Principe delegation, by tax domicile (art. 110); electronic filing allowed where authorised |
| Annual return, Category A and or D (if the net Category D option is taken) | During February of the following year (art. 109(1)(b)) | Same; IRS Modelo 1 with the annex for each category ([Ministry forms folder](https://ministerio.financas.st/phocadownload/Imposto/espaco_contribuinte/Minutas_Formularios/IRS/IRS%20Modelo1.pdf)) |
| Annual return and accounting and tax information return, Category B Group 1 | By 30 April of the following year (art. 109(1)(c)) | Same, with the IRC documents for the group (art. 109(2)) |
| Annual return, Category B Group 2 with simplified books | During February of the following year (art. 109(1)(d)) | Same |
| Changes, cessation, change of group | Within 30 days (art. 109(1)(e) to (g)) | Same |
| Tax withheld by payers | By the 10th of the month after deduction (art. 88(3)) | Places of collection by tax domicile (art. 88(2)) |
| Payments on account, Category B | Three, by the last day of June, September and December; together 75% of the prior basis (art. 92) | Direccao dos Impostos |
| Balance of IRS with compensatory interest | By 30 September of the following year (art. 87(1)) | Direccao dos Impostos |
| Refund of overpaid tax | By the end of the third month after 30 September (art. 86) | Credit note; interest at the compensatory rate if late |
| Statements to employees | By 20 January (payers' duties, the article before art. 117) | Payer to each employee |
| Return of non-resident withholding | By the last working day of June (same article, no. 2) | Payer to the tax administration |

The older skill gave 31 March as the filing date; the code gives February or 30 April as above. The Direccao dos Impostos fixes taxable income by 31 August (art. 72).

## Penalties and interest

Late assessment caused by the taxpayer carries compensatory interest, daily, at the Central Bank reference rate plus three percentage points a year ([General Tax Code art. 38](https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N6_2007_Lei_Que_Aprova_Codigo_Geral_Tributario.pdf)). Late payment carries default interest at 1/6 of the reference rate a month (art. 54). Refund delays caused by the administration earn indemnity interest at the compensatory rate (IRS art. 86(2)). No collection or refund is made below 1/12 of the monthly minimum wage (IRS art. 85). Fine amounts were not read.

## Cross-border points

- Non-residents without a permanent establishment suffer final 15% withholding on STP income (art. 69(1)(c)); with a permanent establishment they file like residents (art. 108).
- Foreign tax: residents deduct international double taxation from the tax (art. 73(1)(b)).
- A resident leaving STP for more than six months, and non-residents with STP income, must appoint a resident tax representative (art. 123).
- A Cabo Verde tax treaty went to the Assembly in 2021 as Resolution Bill 44/XI/5.a/2021; whether it is in force, and all treaty rates, are not confirmed. For company withholding see [corporate income tax](st-corporate-income-tax.md).

## Two worked examples that recompute

**Example 1, lottery prize above the exemption.** A resident wins a national totoloto prize of Db 30,000. The exemption covers only prizes of Db 25,000 or less, so the whole prize is Category D income. The payer withholds the final 15% under art. 69(1)(b) unless the winner opts to aggregate (art. 70), which forces a full declaration.

```oa-check
name: Totoloto prize above Db 25,000
inputs:
  prize: 30000
  exempt_limit: 25000
  final_rate: 0.15
steps:
  - taxable_flag: min(1, max(0, prize - exempt_limit))
  - tax: prize * final_rate * taxable_flag
expected:
  taxable_flag: 1
  tax: 4500
```

**Example 2, decision: resident or non-resident consultant, edge case.** A foreign consultant invoices a company with organised accounts Db 200,000 for services in STP. If the consultant stayed 181 days (more than 180), they are resident: the company withholds 15% on account under art. 68 and the consultant files an annual return, where the final tax may differ. At 180 days, with no home or centre of interests in STP, they are non-resident: the same 15% is final under art. 69(1)(c), and no return is needed for that income.

```oa-check
name: Category B fee withholding
inputs:
  fee: 200000
  rate: 0.15
  days: 181
steps:
  - resident: min(1, max(0, days - 180))
  - withheld: fee * rate
  - net_paid: fee - withheld
expected:
  resident: 1
  withheld: 30000
  net_paid: 170000
```

## Ask the client first

- Days in STP in the year, home on 31 December, and centre of interests
- Income by category A to D, and who paid it
- One employer or several (it changes the withholding table)
- Whether organised accounts are kept (Group 1 or Group 2)
- Dependants and any invalidity of 60% or more
- Foreign tax paid

## Sources

| Source | URL | Read on |
|---|---|---|
| IRS Law 11/2009 (Gazette no. 68, 8 Oct 2009): amending arts. 1 to 5, and republished code arts. 1, 20, 35 to 37, 66, 68 to 75, 85 to 92, 108 to 117, 123 read; art. 66 table checked on the rendered page | https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N11_2009_Codigo_Imposto_Sobre_Rendimento_Pessoas_Singulares_IRS.pdf | 2026-11-16 |
| IRS Modelo 1 return form (Ministry forms folder; form only, no instructions) | https://ministerio.financas.st/phocadownload/Imposto/espaco_contribuinte/Minutas_Formularios/IRS/IRS%20Modelo1.pdf | 2026-11-16 |
| General Tax Code, Law 6/2007, arts. 38, 53 and 54 read | https://ministerio.financas.st/phocadownload/Imposto/legislacao/Lei_N6_2007_Lei_Que_Aprova_Codigo_Geral_Tributario.pdf | 2026-11-16 |
| 2025 Budget Law 2/2025 (Gazette no. 23, 16 May 2025), arts. 8 and 9 read (copy fetched 2026-11-15, sha256 fdcb13cc) | https://ministerio.financas.st/phocadownload/Orcamento/oge/A-2025/Aprovado/lei%20oge2025.pdf | 2026-11-16 |
| 2026 Budget Bill 51/XII/7.a/2025, arts. 8 and 9 read (copy fetched 2026-11-15, sha256 85eb8384) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf | 2026-11-16 |
| Assembly debate of 11 Feb 2026 on the Budget, art. 8 and 9 amendments and votes, pp. 315 to 321 read (copy fetched 2026-11-15, sha256 4a161493) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf | 2026-11-16 |
| 2024 Budget text in Assembly Diario II no. 25 of 22 Dec 2023, art. 8(10) to (13) read (copy fetched 2026-11-15, sha256 101a27e2) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf | 2026-11-16 |
| Budget execution report Q3 2025, tax laws summary (pp. 384 to 385 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies; it is cited as the Assembly's own record. The newer Finance Ministry site (financas.gov.st) answered 403 on 2026-11-16.

Not yet confirmed: amendments to the IRS code after Law 11/2009; whether the 2009 band and withholding tables still apply in 2026 and their value in current dobras (re-denomination rule not re-read); the 30% band (Db 420,000, less Db 45,048) and its status after the Constitutional Court ruling; the published 2026 Budget Law (Law 3/2026) on an official host; any 2026 decree amending the IRS code under the budget power; the 2026 minimum wage used for the personal deduction; fine amounts; treaties, including the Cabo Verde treaty.
