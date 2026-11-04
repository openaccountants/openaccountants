---
name: pt-irs-employees-investment
description: "Portuguese personal income tax (IRS) for tax year 2026 for residents who earn a salary (Category A), a pension (Category H), investment income (Category E dividends and interest), rent (Category F) or capital gains on shares and property (Category G). Covers the 2026 IRS bands of CIRS art. 68 as set by the 2026 State Budget (Lei 73-A/2025), the solidarity surcharge, the specific deduction for employees and pensioners, deductions from the tax (dependants, general family expenses, health, education, rent, invoice VAT), IRS Jovem, the 28% and 25% special rates and the option to aggregate, the reduced rates for long residential leases, the 50% inclusion of property gains and main-home reinvestment, joint or separate filing, the Modelo 3 return and IRS automatico, late filing fines and interest. Trigger on: 'IRS Portugal employee', 'Modelo 3 2026', 'Anexo A', 'Anexo E', 'Anexo F', 'Anexo G', 'englobamento', 'rendas IRS 25%', 'mais-valias imoveis 50%', 'deducoes a coleta', 'IRS Jovem 2026', "
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pt-irs-employees-investment"
  jurisdiction: "PT"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Portugal: IRS for employees, pensioners and investment income (tax year 2026)

This skill computes the annual IRS of a Portuguese resident individual whose income is salary, pension, dividends and interest, rent or capital gains. It is the annual return (Modelo 3), filed between 1 April and 30 June 2027 for income earned in 2026.

Sibling skills, which this one links to and does not repeat:

- `pt-income-tax`: self-employed income (Category B, Anexo B), the simplified regime coefficients. Tax year 2026.
- `portugal-payroll`: monthly withholding on salaries and social security (TSU). Its frontmatter says tax year 2025, though it carries some 2026 figures.
- `pt-foreign-source-treaties`: foreign income of residents, the foreign tax credit and Anexo J.
- `pt-nhr-ifici`: the old non-habitual resident regime and IFICI (20% flat rate). Check this first: a person under either regime is taxed differently and cannot use IRS Jovem.
- `portugal-crypto-tax`: crypto gains and income.

The law is the Código do IRS (CIRS). The Tax Authority (Autoridade Tributária e Aduaneira, AT) publishes the consolidated text, article by article, on the Portal das Finanças. Every figure below was read there, or in the 2026 State Budget law in the Diário da República, on 2026-10-22.

## Who this applies to

**Residents.** A person is resident for a year if, in that year, they spent more than 183 days in Portugal in any 12-month period starting or ending in the year, or had a home there on any day of that period in conditions that suggest they intend to keep it as their habitual residence (CIRS art. 16(1)). A day of presence is any day that includes an overnight stay (art. 16(2)). Residents are taxed on worldwide income.

**Part-year residents.** Residence starts on the first day of presence and ends on the last day of presence (art. 16(3) and (4)), with two exceptions that make a leaver resident for the whole year (art. 16(14) and (16)). Arrival and departure cases belong to cross-border work; this skill assumes a full-year resident.

**Non-residents** with Portuguese salary, pension or rent are taxed at flat rates by withholding or by autonomous rates (art. 71(4), art. 72(6)) and get none of the deductions from the tax (art. 78(5)). They are out of scope here.

**Income categories in scope:** A (employment), H (pensions), E (capital: dividends, interest), F (property: rent), G (capital gains, other than crypto). Category B (self-employed) is in `pt-income-tax`.

**The household.** Married couples and civil partners are taxed separately by default. They may opt for joint taxation each year, and both must make the option in the return (art. 59(2)). Under separate taxation each spouse declares their own income plus 50% of the dependants' income (art. 59(1)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRS band 1: taxable income up to EUR 8,342 | 12.50% (average 12.500%) | 2026 | CIRS art. 68(1), wording of Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Band 2: over 8,342 to 12,587 | 15.70% (average 13.579%) | 2026 | same |
| Band 3: over 12,587 to 17,838 | 21.20% (average 15.823%) | 2026 | same |
| Band 4: over 17,838 to 23,089 | 24.10% (average 17.705%) | 2026 | same |
| Band 5: over 23,089 to 29,397 | 31.10% (average 20.579%) | 2026 | same |
| Band 6: over 29,397 to 43,090 | 34.90% (average 25.130%) | 2026 | same |
| Band 7: over 43,090 to 46,566 | 43.10% (average 26.472%) | 2026 | same |
| Band 8: over 46,566 to 86,634 | 44.60% (average 34.856%) | 2026 | same |
| Band 9: over 86,634 | 48.00% | 2026 | same |
| Solidarity surcharge | 2.5% on taxable income over EUR 80,000 up to 250,000; 5% over 250,000 | 2026 | CIRS art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx |
| IAS (social support index) | EUR 537.13 | 2026 | Portaria 480-A/2025/1, art. 2 and 4: https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 |
| Specific deduction, Category A | 8.54 x IAS = EUR 4,587.09, or the employee's compulsory social security if higher | 2026 | CIRS art. 25(1)(a) and (2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx |
| Specific deduction, Category H | Same EUR 4,587.09 per pensioner; plus compulsory contributions above that amount | 2026 | CIRS art. 53(1), (2), (4): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx |
| Minimum existence reference value | Higher of EUR 12,880 and 1.5 x 14 x IAS (EUR 11,279.73), so EUR 12,880 | 2026 | CIRS art. 70(1), wording of Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx |
| Dividends and interest from Portuguese payers | 28% final withholding; residents may opt to aggregate | 2026 | CIRS art. 71(1) and (9): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx |
| Capital income not withheld (for example foreign interest) | 28% autonomous rate | 2026 | CIRS art. 72(1)(d): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx |
| Dividends of PT or qualifying EU/EEA companies, if aggregated | Only 50% included | 2026 | CIRS art. 40-A(1), (2), (4): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs40a.aspx |
| Rent from residential leases | 25% autonomous rate | 2026 | CIRS art. 72(2) |
| Residential lease 5 to under 10 years | 25% less 10 points = 15% (a further 2 points off per renewal, up to 10 points) | 2026 | CIRS art. 72(3) |
| Residential lease 10 to under 20 years | 25% less 15 points = 10% | 2026 | CIRS art. 72(4) |
| Residential lease 20 years or more | 25% less 20 points = 5% | 2026 | CIRS art. 72(5) |
| Long-lease reductions, leases signed from 1 January 2024 | No reduction if the monthly rent is more than 50% above the general rent limits of Portaria 176/2019 for the property type and municipality; a further 5 points off on a new lease whose rent is at least 5% below the previous lease on the same property | 2026 | CIRS art. 72(23) and (24) |
| Other rent (shops, offices) | 28% autonomous rate | 2026 | CIRS art. 72(1)(e) |
| Net gains on shares and securities | 28% autonomous rate | 2026 | CIRS art. 72(1)(c) |
| Listed securities and open funds held over 2 years | 10% (2 to 5 years), 20% (5 to 8 years), 30% (8 years or more) of the gain excluded | 2026 | CIRS art. 43(5), wording of Lei 31/2024: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx |
| Short-term securities gains, compulsory aggregation | Held under 365 days and taxable income (including the gain) at or above EUR 86,634 | 2026 | CIRS art. 72(14) |
| Property gains | 50% of the net gain included, then aggregated at the band rates | 2026 | CIRS art. 43(2)(b) |
| Gains on shares of unlisted micro and small companies | 50% of the net gain included, then taxed at the 28% autonomous rate unless the resident opts to aggregate | 2026 | CIRS art. 43(3), art. 72(1)(c) and (13) |
| Return filing exemption for low salary or pension | Total EUR 8,500 or less with no withholding | 2026 | CIRS art. 58(1)(b): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs58.aspx |

The 2026 bands are lower than the 2025 bands. The 2026 State Budget (Lei 73-A/2025, art. 71) rewrote the art. 68 table: bands 2 to 5 were cut (for example band 2 went from 16.00% to 15.70%) and every band limit was raised. The law came into force on 1 January 2026.

Pillar Two and other company-level measures do not apply to individuals.

## The taxable base

**Step 1: gross income by category.** Category A is all pay for work, including the holiday and Christmas subsidies and taxable benefits in kind. Category H is pensions.

**Step 2: specific deductions.**

- Category A: EUR 4,587.09 per earner (8.54 x IAS, art. 25(1)(a)), capped at the gross. If the employee's compulsory social security and statutory health subsystem contributions are higher, deduct them instead (art. 25(2)). Union dues up to 1% of the gross are added at 200% (art. 25(1)(c)). The deduction can rise to 75% of 12 x IAS for professional body fees the employee pays (art. 25(4)).
- Category H: the whole pension if it is EUR 4,587.09 or less; otherwise EUR 4,587.09, plus compulsory contributions above that amount (art. 53).
- Category F: actual costs of the property paid in the year, such as IMI, condominium charges and repairs. Finance costs, depreciation, furniture and appliances are not deductible (art. 41(1)). Repair costs in the 24 months before the first letting count (art. 41(7)).
- Category G: the difference between the sale value and the acquisition value (art. 10(4)(a)). The costs that may be added to the acquisition value are in art. 51, which was not read for this skill.

**Step 3: autonomous rate or aggregation.** Categories A, H and property gains are always aggregated (englobamento). Rent, capital income and securities gains are taxed at their autonomous or final rates (art. 71 and 72) unless the resident opts to aggregate them (art. 71(9), art. 72(13)). If the person aggregates one item of a category, every item of that category must be aggregated (art. 22(5)). Aggregation pays when the person's marginal band rate is below the autonomous rate. Worked example 2 shows the test.

**Step 4: IRS Jovem.** A taxpayer aged 35 or under who is not a dependant can exempt part of their Category A and B income for the first 10 years of earning income, by opting in the return (CIRS art. 12-B(1); the 2020 to 2021 regime was the old art. 2-B, now replaced). The exemption is 100% in year 1, 75% in years 2 to 4, 50% in years 5 to 7 and 25% in years 8 to 10, capped each year at 55 x IAS = EUR 29,542.15 of exempt income (art. 12-B(5)). Years with no Category A or B income do not count (art. 12-B(3)(b)). The exempt part is still counted to find the rate on the rest (art. 12-B(4), art. 22(4)). People who have had NHR or IFICI, opted for the returning-resident regime of art. 12-A, or have unpaid tax cannot use it (art. 12-B(9)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx

**Step 5: minimum existence.** A taxpayer whose gross income comes mainly from employment, pensions or the professional activities in the table of Portaria 1011/2001 (except code 15) gets an amount (abatimento) taken off taxable income (art. 70(2)). The reference value is EUR 12,880 (art. 70(1)). If gross income is at or below the reference value, the amount is the reference value less the specific deductions and less the general expenses cap divided by the first band rate (250 / 12.5% = EUR 2,000). Above it, the amount tapers by the formulas in art. 70(2)(b) and (c) and (3). The amount is never negative and never more than gross income less specific deductions (art. 70(2)(d)). It does not apply to anyone in the household when total gross income exceeds 2.2 x 14 x IAS (EUR 16,543.60) times the number of taxpayers, or when income taxed at the final rates and not aggregated exceeds 14 x IAS (EUR 7,519.82) times the number of taxpayers (art. 70(4)). Gross income here includes exempt income, such as the IRS Jovem part (art. 70(5)(a)). AT publishes the simplified formulas for each year in the first quarter of the next year (art. 70(6)).

**Step 6: tax by band.** Apply the art. 68 table to taxable income. AT computes the tax by taking the upper limit of the highest band fully used at that band's average rate (column B), plus the excess at the next band's normal rate (column A) (art. 68(2)). The result can differ by a cent from adding the bands one by one. Under joint taxation, divide taxable income by two, apply the table and multiply by two (art. 69). Then add the solidarity surcharge on taxable income over EUR 80,000 (art. 68-A).

**Step 7: deductions from the tax (deduções à coleta).** These reduce the tax, not the income, and only residents get them (art. 78(5)). Expense-based deductions count only if the invoice carries the taxpayer's tax number (NIF) and the seller reported it to AT (e-fatura) (art. 78(6)). In the order of art. 78(1):

| Deduction | Amount | Source |
|---|---|---|
| Each dependant | EUR 600; EUR 300 each for shared custody with alternating residence | art. 78-A(1) |
| Dependant aged 3 or under at 31 December | plus EUR 126 | art. 78-A(2)(a) |
| Second and later dependant aged 6 or under | plus EUR 300 (not added to the EUR 126) | art. 78-A(3) and (4) |
| Ascendant living with the taxpayer, income not above the minimum pension | EUR 525 (EUR 635 if there is only one) | art. 78-A(1)(c), (2)(b) |
| General family expenses | 35% of invoices, up to EUR 250 per taxpayer; single parent 45%, up to EUR 335 | art. 78-B(1) and (9) |
| Health | 15% of health costs, up to EUR 1,000 for the household | art. 78-C(1) |
| Education and training | 30% of costs, up to EUR 800 for the household (raised by up to EUR 300 for rent of a student living over 50 km from home, max EUR 400 of that rent) | art. 78-D(1) and (11) |
| Rent of the taxpayer's permanent home | 15% of rent paid; for 2026 the cap is EUR 900 | art. 78-E(1)(a) and (10); Decreto-Lei 97/2026, art. 15(1), as reproduced by AT |
| Mortgage interest on the home, contracts up to 31 December 2011 only | 15%, up to EUR 296 (up to EUR 450 for low incomes) | art. 78-E(1)(b) and (5) |
| VAT on invoices from car and motorbike repair, restaurants and hotels, hairdressers and vets, and from 2026 bookshops, performing arts, theatres and venues, libraries, museums and monuments; public transport tickets and passes; newspaper and magazine subscriptions; gyms and sports clubs | 15% of the VAT (100% for public transport and periodical subscriptions, 35% for veterinary medicines, 30% for gyms and sports clubs), up to EUR 250 for the household | art. 78-F(1), (3), (6), (7), (8); points g) to l) added by Lei 73-A/2025 |

**Overall cap.** The deductions for health, education, housing, alimony, invoice VAT, care homes, tax benefits and domestic work (art. 78(1)(c) to (h), (k) and (m)) together cannot exceed a cap per household (art. 78(7)). The dependants and general family expenses deductions sit outside it. The cap is:

- no cap if taxable income is EUR 8,342 or less;
- EUR 1,000 + EUR 1,500 x (80,000 - taxable income) / (80,000 - 8,342) for taxable income between EUR 8,342 and EUR 80,000;
- EUR 1,000 above EUR 80,000.

For three or more dependants the cap rises by 5% per dependant (art. 78(8)). Under joint taxation the cap uses taxable income after the divisor of two (art. 78(7)).

Separate taxation halves the household-based limits for each spouse (art. 78(14)).

**Step 8: credits.** Deduct withholding and payments on account (art. 78(2)). Only these give a refund if they exceed the tax (art. 78(3)).

**Losses.** Carry-forward of net securities losses and rental losses is governed by CIRS art. 55, which was not read for this skill. This skill does not compute loss carry-forwards; read art. 55 for the case.

**Property gains and the main home.** A gain on the sale of the taxpayer's own permanent home is excluded if the sale proceeds (less the loan repaid) are reinvested in another permanent home in Portugal or the EU/EEA between 24 months before and 36 months after the sale, the intention is declared in the return for the year of sale, and the home sold was the tax domicile for the 12 months before (art. 10(5)). A partial reinvestment excludes a proportional part of the gain (art. 10(12)). The relief is lost if the new home is not used as the household's home within 12 months, or if the household's tax domicile is not fixed there (art. 10(6)(a) and (e)). For sales from 1 January 2026 to 31 December 2029, Decreto-Lei 97/2026 added a second exclusion: gains on the sale of any home are excluded if reinvested within the same window in Portuguese homes let for housing at a rent within the legal caps, with a lease signed within 6 months and kept for at least 36 months in the first 5 years, and the new property not sold within 5 years (art. 10(7) to (9)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Household composition and shared-expense percentages for the IRS automatico | By end of February 2027 | CIRS art. 58-A(6), art. 78(11) |
| AT shows the e-fatura deduction totals | By 15 March 2027; complaints by 31 March 2027 | CIRS art. 78-B(6) and (7) |
| Modelo 3 return for 2026 income | 1 April to 30 June 2027, online only, whether or not 30 June is a working day | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| Foreign tax credit not yet known | Deadline extended to 31 December 2027, if AT is told within the normal period | CIRS art. 60(3) and (4) |
| Payment of the balance due | By 31 August 2027 when AT issues the assessment in the normal period (art. 77(a)); by 31 December 2027 when it is issued in the art. 77(c) period | CIRS art. 97(1)(a) and (c): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx |
| Correction of a filed return | Within 30 days of a fact that changes the income declared | CIRS art. 60(2) |

**The return.** Modelo 3 with the annexes the income needs: Anexo A (employment and pensions), E (capital income, only if aggregating or not withheld), F (rent), G (capital gains), H (tax benefits and deductions), J (foreign income, see `pt-foreign-source-treaties`), L (NHR or IFICI, see `pt-nhr-ifici`).

**IRS automatico.** For taxpayers in the group set by regulation, AT prepares a provisional return and assessment from the data it holds (art. 58-A(1)). The taxpayer can confirm it, and it then counts as filed (art. 58-A(2)). If they neither confirm nor file by 30 June, it becomes final on that date; married couples are then taxed separately (art. 58-A(3) and (4)(b)). Anyone whose real situation differs from the draft must file a normal return (art. 58-A(9)). The draft does not cover anyone who must report assets held in a listed low-tax jurisdiction under art. 57(7) (property, vehicles, bank or securities accounts, shares, fund units, bonds, loans, insurance contracts, or assets held through partnerships or trusts there) (art. 58-A(12)).

**Who need not file.** A person whose only income is taxed at the art. 71 final rates and who does not aggregate it, or whose salary and pensions total EUR 8,500 or less with no withholding (art. 58(1)). The exemption does not apply to anyone who opts for joint taxation, has income in kind, or holds assets in a listed low-tax jurisdiction that must be reported under art. 57(7) (art. 58(3)(a), (c) and (e)). Art. 57(7) does not mention crypto assets.

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 (RGIT art. 116(1)). Not applicable when the person was exempt from filing under CIRS art. 58 (RGIT art. 116(3)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Waiver of the fine:** no fine if the person has had no tax conviction and no waiver or reduced fine in the previous five years (RGIT art. 29(1)), or if there was no loss of revenue and the failure is put right (RGIT art. 29(2)). A late return always counts as a loss of revenue if tax was not paid on time (art. 29(3)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit29.aspx
- **Compensatory interest (juros compensatórios):** due when the taxpayer's fault delays the assessment, counted day by day from the filing deadline. A late return always counts as a delay. Rate: the legal interest rate under art. 559(1) of the Civil Code (LGT art. 35(1), (3), (6), (10)), which Portaria 291/2003 sets at 4% a year. Capped at 180 days for an error shown in the return (LGT art. 35(7)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx
- **Late payment interest (juros de mora):** due from the payment deadline until payment, at the rate set for debts to the State (LGT art. 44(1) to (3)). The IGCP fixes that rate each year: 7.221% from 1 January 2026 (Aviso 18/2026/2). A balance for 2026 income falls due in 2027, so the 2027 rate applies; it is published around January 2027. Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx
- **Long-lease rent rates lost:** if a lease that got the reduced rate ends early through the landlord's fault, the reduction is lost from the start of the lease and the difference is paid with compensatory interest (CIRS art. 72(20)).

## Cross-border points

- **Foreign income of a resident** is taxed in Portugal with a credit for foreign tax (art. 81). Use `pt-foreign-source-treaties`.
- **Foreign dividends and interest** not withheld in Portugal pay the 28% autonomous rate (art. 72(1)(d)), or 35% if the payer is in a listed low-tax jurisdiction (art. 72(18)(a)).
- **Non-residents** with Portuguese salary or pensions suffer 25% final withholding (art. 71(4)(a) and (c)); Portuguese rent of a non-resident is taxed at 25% or 28% (art. 72(1)(e) and (2)). EU/EEA residents may elect to be taxed at the resident band rates on their worldwide income (art. 72(15) and (16)).
- **Exit:** loss of residence is treated as a sale of crypto assets at market value (art. 10(25), art. 43(12)). The rule dates from Lei 24-D/2022; Decreto-Lei 97/2026 only renumbered it (it was art. 10(22)). For shares there is no general exit charge in the CIRS text read; see `portugal-crypto-tax` for crypto.
- **NHR and IFICI:** check status first; see `pt-nhr-ifici`. Such taxpayers cannot use IRS Jovem (art. 12-B(9)).
- **Deductions from the tax:** residents only (art. 78(5)).

## Worked examples

### Example 1: single employee, EUR 30,000 gross salary, no dependants

Ana is single, resident all year, aged 40, with no dependants. Her 2026 gross salary is EUR 30,000 (14 payments). Her employee social security at 11% is EUR 3,300. She has e-fatura invoices for general expenses well above EUR 714.29, and EUR 600 of health costs. She has no other income.

1. Specific deduction: social security (EUR 3,300) is below 8.54 x IAS (EUR 4,587.09), so she deducts EUR 4,587.09.
2. Taxable income: 30,000 - 4,587.09 = EUR 25,412.91. The minimum existence rule does not apply: her gross is over EUR 16,543.60.
3. Tax by band (art. 68(2) method): EUR 25,412.91 is in band 5. Tax = 23,089 x 17.705% + (25,412.91 - 23,089) x 31.10% = 4,087.91 + 722.74 = EUR 4,810.64.
4. Deductions from the tax: general family expenses EUR 250 (the maximum). Health 15% x 600 = EUR 90. The overall cap for health and the other capped items is 1,000 + 1,500 x (80,000 - 25,412.91) / (80,000 - 8,342) = EUR 2,142.66, so the EUR 90 is allowed in full.
5. Tax after deductions: 4,810.64 - 250 - 90 = EUR 4,470.64. Her monthly withholding is then credited against this.

```oa-check
name: PT single employee, gross EUR 30,000, 2026 bands
inputs:
  gross: 30000
  ias: 537.13
  ss_rate: 0.11
  band4_top: 23089
  band4_avg: 0.17705
  band5_rate: 0.311
  general_expenses_cap: 250
  health_spend: 600
  health_rate: 0.15
steps:
  - ss: gross * ss_rate
  - specific_deduction: round(max(8.54 * ias, ss), 2)
  - taxable: gross - specific_deduction
  - tax: round(band4_top * band4_avg + (taxable - band4_top) * band5_rate, 2)
  - health: health_spend * health_rate
  - cap: round(1000 + 1500 * (80000 - taxable) / (80000 - 8342), 2)
  - capped_items: min(health, cap)
  - net_tax: tax - general_expenses_cap - capped_items
expected:
  specific_deduction: 4587.09
  taxable: 25412.91
  tax: 4810.64
  cap: 2142.66
  net_tax: 4470.64
```

### Example 2: employee with residential rent, 25% autonomous rate or aggregation

Rui is single and resident. His 2026 gross salary is EUR 18,000 (social security EUR 1,980). He lets a flat under a residential lease of 2 years for EUR 9,000 in the year and paid EUR 1,000 of IMI and condominium charges. His net Category F income is 9,000 - 1,000 = EUR 8,000. The lease is under 5 years, so no reduced rate applies.

1. Salary: specific deduction EUR 4,587.09 (above his EUR 1,980 social security). Category A taxable income = 18,000 - 4,587.09 = EUR 13,412.91.
2. Option A, autonomous rate: tax on salary = 12,587 x 13.579% + (13,412.91 - 12,587) x 21.20% = 1,709.19 + 175.09 = EUR 1,884.28. Rent at 25% x 8,000 = EUR 2,000. Total EUR 3,884.28.
3. Option B, aggregation (art. 72(13)): taxable income = 13,412.91 + 8,000 = EUR 21,412.91, in band 4. Tax = 17,838 x 15.823% + (21,412.91 - 17,838) x 24.10% = 2,822.51 + 861.55 = EUR 3,684.06.
4. Aggregation saves EUR 200.22, because his top band rate on the rent (21.20% to 24.10%) is below 25%. With a 10-year lease (10% rate, art. 72(4)) the autonomous rate would win.
5. Check two side effects before choosing. Aggregation raises taxable income, which lowers the overall cap on deductions from the tax (step 7 above). And all of his Category F income must be aggregated, not only this flat (art. 22(5)). Deductions from the tax are left out of the comparison here because they are the same in both options unless the cap bites.

```oa-check
name: PT employee with EUR 8,000 net residential rent, autonomous 25% vs aggregation, 2026 bands
inputs:
  gross_salary: 18000
  specific_deduction: 4587.09
  rent_gross: 9000
  rent_costs: 1000
  rent_rate: 0.25
steps:
  - cat_a: gross_salary - specific_deduction
  - cat_f: rent_gross - rent_costs
  - tax_salary_only: round(12587 * 0.13579 + (cat_a - 12587) * 0.212, 2)
  - tax_rent_autonomous: cat_f * rent_rate
  - option_a: tax_salary_only + tax_rent_autonomous
  - aggregated: cat_a + cat_f
  - option_b: round(17838 * 0.15823 + (aggregated - 17838) * 0.241, 2)
  - saving: option_a - option_b
expected:
  cat_a: 13412.91
  tax_salary_only: 1884.28
  option_a: 3884.28
  aggregated: 21412.91
  option_b: 3684.06
  saving: 200.22
```

## Ask the client first

1. Were you resident in Portugal for all of 2026, and have you ever been registered under NHR or IFICI? (Changes the rates, the deductions and IRS Jovem.)
2. Are you married or in a civil partnership, and how many dependants do you have, with their ages? (Joint or separate, the dependant deductions and the cap.)
3. Your age, and in which year did you first earn employment or self-employed income after your studies? (IRS Jovem year and percentage.)
4. For each let property: is the lease residential, when was it signed, how long is it, and is it registered on the Portal das Finanças? (25%, 28% or the 15%, 10% or 5% long-lease rates.)
5. Did you sell shares, funds or property in 2026: dates bought and sold, prices, and for a home sale, do you intend to reinvest? (Category G: 28%, holding-period exclusions, 50% inclusion, reinvestment.)
6. Do you have any foreign income or foreign accounts? (Anexo J and `pt-foreign-source-treaties`.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 68, IRS bands (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-22 |
| CIRS art. 68-A, solidarity surcharge | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-22 |
| CIRS art. 69, joint taxation divisor | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs69.aspx | 2026-10-22 |
| CIRS art. 70, minimum existence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx | 2026-10-22 |
| CIRS art. 10, capital gains and reinvestment (wording of Decreto-Lei 97/2026) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs10.aspx | 2026-10-22 |
| CIRS art. 12-B, IRS Jovem | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-22 |
| CIRS art. 16, residence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx | 2026-10-22 |
| CIRS art. 22, aggregation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-22 |
| CIRS art. 25, Category A specific deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-22 |
| CIRS art. 40-A, 50% of dividends on aggregation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs40a.aspx | 2026-10-22 |
| CIRS art. 41, Category F deductions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs41.aspx | 2026-10-22 |
| CIRS art. 43, capital gains inclusion | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs43.aspx | 2026-10-22 |
| CIRS art. 53, Category H specific deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx | 2026-10-22 |
| CIRS art. 58 and 58-A, filing exemption and IRS automatico | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs58a.aspx | 2026-10-22 |
| CIRS art. 57(7), assets in listed low-tax jurisdictions to report in the return | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs57.aspx | 2026-10-23 |
| CIRS art. 59, married couples | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs59.aspx | 2026-10-22 |
| CIRS art. 60, filing period | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-22 |
| CIRS art. 71, final withholding rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-22 |
| CIRS art. 72, special rates (rent, gains, capital) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-22 |
| CIRS art. 78 and 78-A to 78-F, deductions from the tax | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78.aspx | 2026-10-22 |
| CIRS art. 78, cap formula (image on the AT page) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/PublishingImages/irs78_Lei_12_2022.PNG | 2026-10-22 |
| CIRS art. 97, payment | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx | 2026-10-22 |
| Lei 73-A/2025, 2026 State Budget (art. 71 amends CIRS art. 68, 70, 78-F; in force 1 January 2026) | https://files.diariodarepublica.pt/1s/2025/12/25002/0000200271.pdf | 2026-10-22 |
| RGIT art. 116 and 29, fines | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx | 2026-10-22 |
| LGT art. 35 and 44, interest | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-22 |
| Portaria 480-A/2025/1, IAS 2026 = EUR 537.13 (art. 2), from 1 January 2026 (art. 4) | https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 | 2026-10-23 |
| Aviso 18/2026/2 (IGCP), late payment interest 7.221% from 1 January 2026 | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-23 |
| Portaria 291/2003, legal interest rate 4% (AT copy) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria_291_de_8_de_abril_de_2003_serie_i_b.pdf | 2026-10-23 |
| CIRS art. 78-A to 78-F, deductions from the tax (one page per article) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78e.aspx | 2026-10-23 |

Not yet confirmed:

- That no portaria has replaced Portaria 291/2003 (4% legal interest). The AT copy of the portaria was read; its current status was not checked on the Diário da República.
- The late payment interest rate for 2027, which applies to a 2026 balance paid late. The IGCP had not published it on 2026-10-23.
- Juros indemnizatórios (interest AT pays on overpaid tax, LGT art. 43). The AT page did not load, so the rate is not given.
- How the 2026 rent deduction cap of EUR 900 (Decreto-Lei 97/2026, art. 15(1)) interacts with the higher limits for low incomes in art. 78-E(4), which Lei 36/2024 phases in at 75% for 2026. Use EUR 900 unless taxable income is low, and check AT's simulator for a low-income tenant.
- The loss carry-forward periods of CIRS art. 55 were not read today.
- CIRS art. 68(2) still refers to EUR 8,059 (the 2025 first band limit) after the 2026 change to the table. AT's method in practice uses the band limits of the current table, as in the examples; this is a drafting leftover in the law, not confirmed by AT guidance.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pt-irs-employees-investment` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pt-irs-employees-investment. If neither is available, confirm every figure against the official source pages cited above before relying on it.
