---
name: croatia-income-tax
description: "Use this skill for Croatian personal income tax (porez na dohodak) for the 2026 tax year (calendar year). It covers residence, the two annual rates set by each town or municipality inside the legal ranges (lower rate up to EUR 60,000 of base, higher rate above), the default 20% / 30%, the EUR 600 monthly personal allowance and the dependant and disability coefficients, employment income and monthly withholding, the youth and returnee reliefs, self-employed income from books (obrt, free professions), the lump-sum paušalni obrt and its seven 2026 bands, final taxes on interest, dividends and capital gains (12%), rent (12%), property disposals (24%), the annual return, deadlines and fines. Trigger on: porez na dohodak, osobni odbitak, paušalni obrt, PO-SD, DOH, JOPPD, Croatian salary tax, Zagreb tax rate, dividend tax Croatia. Out of scope: hr-cross-border (treaties, non-resident withholding), croatia-payroll and croatia-social-contributions, croatia-vat-return, hr-corporate-income-tax, hr-transfer-pricing, croatia-tax-optimization."
jurisdiction: HR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Croatia: personal income tax (2026)

This skill covers personal income tax in Croatia for 2026. The law is the Income Tax Act (Zakon o porezu na dohodak, "ZPD"), Narodne novine 115/16, 106/18, 121/19, 32/20, 138/20, 151/22, 114/23 and 152/24. The Tax Administration (Porezna uprava) keeps a consolidated text in force from 1 January 2025. The authority is the Tax Administration of the Ministry of Finance. The currency is the euro. The tax year is the calendar year (art. 7).

Detail lives in the sibling skills. Read [hr-cross-border](hr-cross-border.md) for residence tie-breakers, non-residents, treaty forms and withholding on payments abroad, [hr-corporate-income-tax](hr-corporate-income-tax.md) for companies and for an obrt that opts into profit tax, and [hr-transfer-pricing](hr-transfer-pricing.md) for related-party pricing. Read [croatia-payroll](croatia-payroll.md) for the full gross-to-net and the JOPPD report, [croatia-social-contributions](croatia-social-contributions.md) for contributions and [croatia-vat-return](croatia-vat-return.md) for VAT; those three still carry 2025 figures.

**What changed for 2026.** The Act itself did not change for 2026. The last amendment, NN 152/2024, took effect on 1 January 2025. It raised the basic allowance from EUR 560 to EUR 600 a month, moved the band limit from EUR 50,400 to EUR 60,000 a year (EUR 5,000 a month for withholding), narrowed the local rate ranges, added the five-year relief for returning emigrants, and tightened the rules on property sales and rent. What does change in 2026:

- **Local rate decisions.** Each town or municipality sets its own two rates. The Tax Administration's 2026 table shows, for example, Zagreb 23% / 33%, Split 21.5% / 32% and Rijeka 20% / 25% (Rijeka's decision NN 149/25 applies from 1 January 2026). Of 556 local units, 543 kept the same lower rate as in 2025.
- **Contribution bases** (NN 150/2025): the paušalni obrt base is EUR 797.20 a month; the maximum monthly base is EUR 11,958.00.
- **Income Tax Ordinance** amended by NN 157/2025 from 1 January 2026, mainly for students working through student services and for JOPPD codes.

## Who this applies to

- **Residents** are individuals with a domicile (prebivalište) or habitual residence (uobičajeno boravište) in Croatia, and Croatian civil servants paid by the state while abroad (art. 3). Residents are taxed on worldwide income (art. 6(1)).
- **Habitual residence** means staying in a place in circumstances showing the stay is not just temporary. A continuous or connected stay of at least 183 days in one or two calendar years counts; short breaks of up to one year do not matter (Tax Administration, habitual residence page).
- **Non-residents** are taxed only on Croatian-source income (art. 4, art. 6(2)).
- **Sources of income** are five: employment (salary and pension), self-employment, property and property rights, capital, and other income (art. 5).
- **Annual or final.** Employment, self-employment and other income not treated as final are added up and taxed at the annual rates (art. 13, art. 18). Property, capital and some other income are taxed separately as final income at flat rates, with no personal allowance and no annual return (art. 12(4), art. 55).
- **Out of scope here:** individuals who opt into profit tax for their business (art. 36), and companies.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Band limit for the annual rates | lower rate on base up to EUR 60,000; higher rate on the part above | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19) |
| Band limit for monthly withholding on salary | lower rate on monthly base up to EUR 5,000; higher rate above | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 24(3)) |
| Local rate range, municipality (općina) | lower 15% to 20%; higher 25% to 30% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19.a(2)) |
| Local rate range, town (grad) | lower 15% to 21%; higher 25% to 31% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19.a(2)) |
| Local rate range, large town or county seat | lower 15% to 22%; higher 25% to 32% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19.a(2)) |
| Local rate range, City of Zagreb | lower 15% to 23%; higher 25% to 33% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19.a(2)) |
| Default rates where a local unit made no decision | 20% and 30% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 19.a(5)) |
| Rates in force for 2026: Zagreb; Split; Rijeka | 23% / 33%; 21.5% / 32%; 20% / 25% | 2026 | https://porezna-uprava.gov.hr/UserDocsImages/Portal_porezne_konkurentnosti/Odluke_JLS/Porezne%20stope%20godi%C5%A1njeg%20poreza%20na%20dohodak/Tablica%20poreznih%20stopa%20godi%C5%A1njeg%20poreza%20na%20dohodak%20za%202026%20godinu.xlsx |
| Basic personal allowance | EUR 600 a month (EUR 7,200 a year) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 14(1)) |
| Dependent close family member; 1st child; 2nd child; 3rd child | 0.5 (EUR 300); 0.5 (EUR 300); 0.7 (EUR 420); 1.0 (EUR 600) a month | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 14(3)) |
| 4th to 9th child | 1.4 (EUR 840); 1.9 (EUR 1,140); 2.5 (EUR 1,500); 3.2 (EUR 1,920); 4.0 (EUR 2,400); 4.9 (EUR 2,940) a month; each further child 1.1 more than the previous one | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 14(3)) |
| Disability: partial; 100% or care allowance | 0.3 (EUR 180); 1.0 (EUR 600) a month, per person | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 14(3)) |
| Dependant income limit | 6 x basic allowance a year (EUR 3,600) | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 17(1)) |
| Youth relief on salary | up to 25: 100% of the lower-rate tax on salary; 26 to 30: 50% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 46(2)) |
| Returning emigrant relief on salary | 100% of the tax on salary for 5 years | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 46(3) to (5)) |
| Assisted areas (group I) and Vukovar; pensions | 50% cut in tax on salary or pension | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 24(5), art. 46(1)) |
| Interest; dividends and profit shares; capital gains on financial assets | 12% final | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 70(1), (4), (17), (19)) |
| Capital gains exemption | financial assets sold more than 2 years after acquisition | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 67(8)) |
| Share awards and options to employees and board members | 24% final | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 70(18)) |
| Hidden profit distributions (withdrawals) | 36% final | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 70(2)) |
| Rent of real estate and movables | 12% on rent less a flat 30% for expenses | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 57(1), art. 62(1)) |
| Royalties for property rights | 24% withheld on the gross fee | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 62(2)) |
| Sale of real estate within 2 years, or more than 3 of the same kind in 5 years | 24% on the gain | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 58(2), (3), art. 62(3), (4)) |
| Tourist letting by private individuals | annual lump sum per bed set by the local unit: category I EUR 100 to 300; II EUR 70 to 200; III EUR 30 to 150; IV and 0 EUR 20 to 100 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 57(4)) |
| Unexplained assets | 36%, increased by 100% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 78) |
| Paušalni obrt: entry limit | receipts not above the VAT registration limit, EUR 60,000 | 2026 | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 |
| Paušalni obrt: tax | 12% of the band base, paid quarterly | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 (art. 82(5), (6)) |
| Paušalni obrt bands (receipts: base; annual tax) | up to 11,300: 1,695; 203.40. 11,300.01 to 15,300: 2,295; 275.40. 15,300.01 to 19,900: 2,985; 358.20. 19,900.01 to 30,600: 4,590; 550.80. 30,600.01 to 40,000: 6,000; 720.00. 40,000.01 to 50,000: 7,500; 900.00. 50,000.01 to 60,000: 9,000; 1,080.00 (EUR) | 2026 | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 |
| Paušalni obrt: cut for Vukovar, assisted areas and group I islands | 25% of the lump-sum tax | 2026 | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 |
| Paušalni obrt: monthly contribution base | EUR 797.20 | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html (art. 7) |
| Contribution bases: obrt on books; free profession on books | EUR 1,295.45; EUR 2,192.30 a month | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html (art. 6) |
| Maximum monthly contribution base | EUR 11,958.00 | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html (art. 4) |
| Low-salary pension base cut | gross up to EUR 700: base cut by EUR 300; EUR 700.01 to 1,300: cut by 0.5 x (1,300 - gross) | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html (Contributions Act art. 21.a) |

## The taxable base

### Annual income (art. 13 to 19)

The annual base is employment income plus self-employment income plus other income that is not final, minus the personal allowance (art. 18(1)). Tax is the lower rate on the base up to EUR 60,000 and the higher rate above (art. 19). The rates are those of the local unit where the taxpayer has a domicile or habitual residence (art. 1(2), art. 19.a). For rent and tourist letting, the place where the property is decides which local unit gets the tax (art. 1(3)).

**Personal allowance.** EUR 600 for every month of the tax year, plus the dependant and disability parts (art. 14). In the annual assessment a taxpayer can also add mandatory health contributions paid privately, and gifts for listed public purposes up to 2% of receipts (art. 15). A dependant whose own income is over 6 x EUR 600 (EUR 3,600) in the year does not count (art. 17(1)). If two people support the same dependant, the allowance is split equally unless they agree otherwise (art. 17(5)).

### Employment (art. 20 to 27)

- Employment income is all receipts from the employer in cash or in kind, minus the employee's mandatory contributions (art. 20, 21, 23). For a usual employee these are pension contributions of 15% (pillar I) and 5% (pillar II), 20% in all; the 16.5% health contribution is paid by the employer on top and is not deducted from the employee (rates as on the Tax Administration's paušalni page; detail in [croatia-social-contributions](croatia-social-contributions.md)).
- The employer withholds an advance on each payment. The monthly base is gross pay minus contributions minus the monthly allowance on the tax card, taxed at the local lower rate up to EUR 5,000 a month and the higher rate above (art. 24(2), (3)).
- The advance is halved for pensioners and for people living in group I assisted areas and Vukovar (art. 24(5)).
- Employees up to 25 have the lower-rate tax on their salary cut by 100%; those aged 26 to 30 by 50%. The relief covers the whole year in which the age is reached (art. 46(2), (8)).
- Croatian citizens who lived abroad without a break for at least two years and come back (and were not posted abroad by a Croatian employer) have the tax on their salary cut by 100% for five years, from 1 January of the year they qualify (art. 46(3) to (5)). It replaces the youth and assisted-area reliefs (art. 46(9)).

### Self-employment on books (art. 28 to 38)

- Covers obrt and similar trades, free professions (doctors, lawyers, architects, consultants and others), agriculture and forestry over EUR 10,685 of receipts or in VAT, and small electricity production (art. 28, 29).
- Income is business receipts minus business expenses, on a cash basis (art. 11(3), art. 30). Contributions paid are deductible (art. 32(6)).
- Not deductible: 50% of entertainment, 50% of car costs where no benefit in kind is taxed (insurance is fully deductible), and anything not directly linked to the business (art. 33).
- Assets over EUR 665 with a life over one year go into the fixed asset list and are written off at the profit tax rates (art. 35).
- Extra deductions: salaries of new hires for one year (three years for workers with a disability), education aid, and R&D (art. 18(2), art. 44, art. 45).
- A loss is carried forward against the same kind of income for five years (art. 38).
- An obrt can opt to pay profit tax instead; the choice binds for three years (art. 36). It must switch if receipts in the previous year were over EUR 1,000,000 (Profit Tax Act art. 2(4)).

### Paušalni obrt (art. 82)

- A trade (not a free profession) that is not in VAT and has receipts not above the VAT registration limit (EUR 60,000) can pay a lump sum instead of keeping books (art. 82(1); Tax Administration paušalni page).
- The base is fixed by the band the year's receipts fall in, not by actual profit. Tax is 12% of the band base (art. 82(6)), paid quarterly by the last day of each quarter.
- The paušalist keeps only a sales book (KPR) and files the PO-SD report within 15 days after the year ends, paying any balance the same day (art. 82(4), (6)).
- If receipts pass the VAT limit during a month, the lump sum applies to the end of that month; then the trader moves to books (art. 82(9), (10)).
- Contributions for a paušalist insured on that basis are on EUR 797.20 a month for 2026: EUR 119.58 pillar I, EUR 39.86 pillar II and EUR 131.54 health a month (Tax Administration paušalni page).

### Other income not treated as final (art. 39, 40)

Board fees, author fees, fees to consultants, agents, translators and similar, and other unlisted payments. Author, journalist, artist and sportsperson income gets a flat 30% expense deduction (art. 39(5)). The payer withholds an advance at the lower local rate with no allowance (art. 40(1)). The income then goes into the annual assessment.

### Final income (art. 55 to 78)

No allowance and no annual return (art. 55(2), (3)).

- **Rent:** 30% flat expenses, 12% tax on the rest, paid monthly by assessment (art. 57(1), art. 62(1)). Handing property to anyone other than close family without a lease counts as letting (art. 62(9), (10)). If the landlord is in VAT, or its receipts pass the VAT limit, rent is taxed as self-employment instead (art. 61).
- **Tourist letting** by private individuals with a hospitality approval: a yearly lump sum per bed or camp unit, set by the local unit inside the legal range. The defaults where no decision was made are EUR 200, 135, 90 and 60 by category (art. 57(4), (7), art. 82(2), (5)).
- **Sale of real estate:** the gain is the price minus cost uplifted by producer prices, minus documented investment and sale costs (art. 58(1)). It is not taxed after two years of ownership, unless more than three properties of the same kind are sold within five years. A home used by the owner or dependants, sales within close family, and inherited property are exempt (art. 58(2) to (6)). Tax is 24% (art. 62(3), (4)).
- **Interest:** 12% withheld (art. 70(1)). Bank interest of up to 0.5% a year, interest on bonds and on Croatian government securities, and life and voluntary pension yields are not taxed (art. 65(2)).
- **Dividends and profit shares:** 12% withheld (art. 70(19)).
- **Capital gains on financial assets:** 12% on gains minus losses of the same year (art. 67(11), art. 70(4)). Gains on assets sold more than two years after acquisition, and transfers in close family or by inheritance, are not taxed (art. 67(8)). FIFO applies (art. 70(5)). The holder pays by the end of February for the previous year, or has a broker or the depository SKDD compute it (art. 70(4), (7), (8), (14)). Gains on non-listed company shares are taxed by assessment at 12%, and the sale must be reported within eight days (art. 70(17)).
- **Share awards and employee options:** 24% withheld (art. 68, art. 70(18)).

## Deadlines and filing

- **Registration:** report the start of a business, letting or income from abroad within 8 days (art. 83(1), art. 87(4)). A lease must reach the tax office within 8 days unless a notary sent it (art. 62(7), (8)).
- **Withholding on salary:** on each payment, under the rules in force on the payment day (art. 24(1)), reported on the JOPPD form (art. 27). The employer does a year-end recalculation in December where the year's pay was uneven (art. 47).
- **Annual return (DOH):** compulsory for the self-employed on books and for seafarers in international shipping (art. 48). It is filed by the end of February for the previous year (art. 50(2)). For 2025 the Tax Administration set the last day as 2 March 2026. For 2026 the end of February 2027 falls on a Sunday.
- **Self-employed tax due:** the balance on the return is due on the last day for filing (art. 46(12)). Monthly advances for the next period are one twelfth of the year's tax, paid by the last day of each month (art. 37(5)). A new business pays no advances until its first return (art. 37(4)).
- **Employees and other income (special procedure):** the Tax Administration assesses on its own and sends a provisional decision by 30 June (art. 51, art. 54(2)). Claims for dependants, disability, health contributions, gifts or foreign tax go on form ZPP-DOH by the end of February (art. 53(1)). Objections run to 31 July (art. 54(3)). A balance due is paid within 15 days of the objection deadline (art. 54(9)).
- **Paušalni obrt:** quarterly tax by the last day of each quarter; PO-SD by 15 January 2027 for 2026 (art. 82(5), (6); Tax Administration paušalni page).
- **Capital gains:** self-assessed and paid by the end of February 2027 for 2026 (art. 70(4), (14)).
- **Foreign income:** a resident who earns directly from abroad pays the advance within 30 days (art. 81(1)), or, if tax is paid abroad during the year, reports by 31 January (art. 81(3), (4)).

## Penalties and interest

From the Income Tax Act. Fines are set within these ranges.

- **Self-employed person, in connection with the business:** EUR 660 to 6,630 for not paying the return tax or assessed tax on time, not registering a business or letting, or not filing a lease (art. 92(1)).
- **Other individual:** EUR 260 to 2,650 for the same breaches, for unpaid capital gains tax, or for unpaid tax on a foreign pension (art. 92(2)).
- **Payers (companies):** EUR 1,320 to 6,630 for not paying or underpaying withheld tax, not reporting payments, or not paying into a bank account (art. 91(1)); the responsible person EUR 260 to 1,320 (art. 91(4)). A self-employed payer: EUR 660 to 3,980 (art. 91(2)).
- **No return filed, or wrong data:** the tax is set by estimate (art. 48(4), art. 82(7)).
- **Unexplained assets:** 36% plus 100% (art. 78).
- **Late payment interest** runs under the General Tax Act (art. 90 of the Income Tax Act). The rate is not in this skill.

## Cross-border points

- **Non-residents** get the EUR 600 allowance only for the months they have Croatian income (art. 16(1)). An EU or EEA resident whose Croatian income is at least 90% of worldwide income, and is exempt at home, gets the full family allowance in the annual assessment (art. 16(3)).
- **Treaties come first** over the Act (art. 80(1)). Foreign tax is credited per item of income, on a certificate from the foreign authority, and only if it was charged as the treaty allows (art. 80(2) to (4)). The credit is claimed in the return or on the ZPP-DOH, with the certificate by 30 November (art. 53(4), (5), art. 81(4)).
- **Foreign income is taken as the source state computed it**, less contributions not allowed there (art. 80.a).
- **Digital nomads.** Pay from a foreign employer received under the digital nomad status is exempt (art. 9(1)(26)).
- **Moving in or out.** The tax year is cut to the period of residence when someone becomes or stops being resident; allowances count in full months in the taxpayer's favour (art. 7(2), (3)).
- **Foreign performers** paid through a foreign company: the Croatian payer withholds profit tax on the company's fee instead (art. 6(3)).
- Treaty relief forms, permanent establishments and withholding on payments to non-residents are in [hr-cross-border](hr-cross-border.md). Social security for posted workers and A1 certificates is in [croatia-social-contributions](croatia-social-contributions.md).

## Worked examples

### Example 1: employee in Zagreb with two children

An employee in Zagreb earns EUR 3,000 gross a month for all of 2026. She is 35 and supports two children with no income of their own. Her pension contributions are 20%, so EUR 600, and her income is EUR 2,400. Her allowance is EUR 600 plus EUR 300 for the first child and EUR 420 for the second, EUR 1,320 in all (art. 14). The monthly base is EUR 1,080. That is under the EUR 5,000 monthly limit, so all of it is taxed at Zagreb's lower rate of 23%. Withholding is EUR 248.40 a month and net pay is EUR 2,151.60. Over the year the base is EUR 12,960 and the tax EUR 2,980.80, so the year-end assessment changes nothing. At EUR 3,000 the low-salary pension cut (gross up to EUR 1,300) does not apply.

```oa-check
name: HR employee in Zagreb, two children, gross 3,000 a month (2026)
inputs:
  gross: 3000
  allowance_basic: 600
  child1: 300
  child2: 420
  rate_lower: 23
steps:
  - pension: pct(gross, 20)
  - income: gross - pension
  - allowance: allowance_basic + child1 + child2
  - base: max(income - allowance, 0)
  - tax_month: pct(base, rate_lower)
  - net_month: gross - pension - tax_month
  - tax_year: tax_month * 12
expected:
  pension: 600.00
  income: 2400.00
  allowance: 1320.00
  base: 1080.00
  tax_month: 248.40
  net_month: 2151.60
  tax_year: 2980.80
```

### Example 2: obrt on books in Split, base over EUR 60,000

A sole trader in Split keeps books. In 2026 his business receipts are EUR 140,000 and his deductible expenses, including the contributions he paid, are EUR 65,000. He has no dependants and lives in Split all year. His income is EUR 75,000. After the EUR 7,200 annual allowance the base is EUR 67,800. The first EUR 60,000 is taxed at Split's lower rate of 21.5% (EUR 12,900). The other EUR 7,800 is taxed at Split's higher rate of 32% (EUR 2,496). Tax is EUR 15,396, due with the DOH return by the end of February 2027, less any advances already paid for 2026. From the month after the filing deadline he pays monthly advances of one twelfth, EUR 1,283 (art. 37(5)). He cannot be a paušalist: his receipts are over EUR 60,000.

```oa-check
name: HR obrt on books in Split, base above EUR 60,000 (2026)
inputs:
  receipts: 140000
  expenses: 65000
  allowance_year: 7200
  band_limit: 60000
steps:
  - income: receipts - expenses
  - base: income - allowance_year
  - tax_lower: pct(min(base, band_limit), 21.5)
  - tax_higher: pct(max(base - band_limit, 0), 32)
  - tax: tax_lower + tax_higher
  - advance_month: tax / 12
expected:
  income: 75000.00
  base: 67800.00
  tax_lower: 12900.00
  tax_higher: 2496.00
  tax: 15396.00
  advance_month: 1283.00
```

## Ask the client first

1. Where is your domicile or habitual residence (town or municipality), and were you in Croatia for 183 days or more? The local unit sets your two rates.
2. What kinds of income do you have in 2026: salary, a trade or free profession, rent, tourist letting, interest, dividends, share sales, income from abroad?
3. Who do you support, and what is each person's own income for the year? Is there a disability decision?
4. How old are you, and did you return to Croatia after living abroad for two years or more?
5. For a business: obrt or free profession, books or paušal, in VAT or not, and what are the expected receipts?
6. For a sale of property or shares: when was it bought, for how much, and how many similar properties have you sold in the last five years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dohodak, consolidated text NN 115/16 to 152/24, in force from 1 Jan 2025 (Tax Administration register) (art. 1 to 7, 9, 11 to 19.a, 20 to 50, 51 to 70, 75 to 82, 91, 92) | https://porezna-uprava.gov.hr/hr_propisi/_layouts/in2.vuk.sp.propisi.intranet/propisi.aspx#id=pro1623 | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o porezu na dohodak, NN 152/2024 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o porezu na dohodak, NN 114/2023 (12% rates on capital and rent) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1609.html | 2026-10-23 |
| Zakon o porezu na dobit, consolidated text in force from 1 Jan 2026 (art. 2(4)) | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 | 2026-10-23 |
| Pravilnik o izmjenama i dopunama Pravilnika o porezu na dohodak, NN 157/2025, in force 1 Jan 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_157_2365.html | 2026-10-23 |
| Naredba o iznosima osnovica za obračun doprinosa za obvezna osiguranja za 2026. godinu, NN 150/2025 | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html | 2026-10-23 |
| Zakon o izmjenama i dopunama Zakona o doprinosima, NN 114/2023 (art. 21.a, low-salary pension base cut) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1611.html | 2026-10-23 |
| Tax Administration, Porez na dohodak (rates, list of regulations) | https://porezna-uprava.gov.hr/hr/porez-na-dohodak-3939/3939 | 2026-10-23 |
| Tax Administration, Porezne stope godišnjeg poreza na dohodak, with the 2026 table of local rates | https://porezna-uprava.gov.hr/hr/porezne-stope-godisnjeg-poreza-na-dohodak/4764 | 2026-10-23 |
| Tax Administration, Obrtnici paušalisti (2026 bands and contributions) | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 | 2026-10-23 |
| Tax Administration, Uobičajeno boravište za porezne svrhe | https://porezna-uprava.gov.hr/hr/uobicajeno-boraviste-za-porezne-svrhe/4142 | 2026-10-23 |
| Tax Administration, Godišnji obračun poreza na dohodak (DOH and ZPP-DOH dates for 2025) | https://porezna-uprava.gov.hr/hr/godisnji-obracun-poreza-na-dohodak/3957 | 2026-10-23 |
| Tax Administration, Primatelj kamata (12% on interest) | https://porezna-uprava.gov.hr/hr/primatelj-kamata/4471 | 2026-10-23 |

Not yet confirmed: the exact last filing day the Tax Administration will set for 2026 DOH returns (28 February 2027 is a Sunday); the late payment interest rate under the General Tax Act for 2026; the consolidated text of the Paušalni Ordinance (NN 1/20 to 16/25), read here only through the Tax Administration's 2026 band table; the tourist letting lump sum each local unit set for 2026; the employee contribution rates (15% and 5%) were read on the Tax Administration's paušalni page, not in the consolidated Contributions Act.
