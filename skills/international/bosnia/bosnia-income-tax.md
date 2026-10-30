---
name: bosnia-income-tax
description: "Bosnia and Herzegovina personal income tax (porez na dohodak) for tax year 2026, set separately by the Federation of BiH (FBiH), Republika Srpska (RS) and Brčko District (BD). Covers residence in each, the flat rates (FBiH 10%, RS 8% on salary, 10% on business income, 13% on capital and other income, BD 10%), personal allowances (FBiH 300 KM a month plus dependant factors, RS 12,000 KM a year, BD 14,400 KM a year), self-employment, the RS 2% small-entrepreneur tax and FBiH flat-rate amounts, rent, interest and property gains, annual returns and fines. Trigger on: porez na dohodak, lični odbitak, porezna kartica, GPD-1051, mali preduzetnik, paušal, godišnja poreska prijava, Bosnia income tax. Out of scope: monthly payroll (bosnia-payroll), contribution rates and bases (bosnia-social-contributions), VAT (bosnia-vat), companies (ba-corporate-income-tax)."
version: 0.2
jurisdiction: BA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina: personal income tax (2026)

> **Not reviewed by an accountant.** Figures come from the three income tax laws and their 2026 implementing texts, read on the official sites of the FBiH Tax Administration (pufbih.ba), the RS Tax Administration (poreskaupravars.org) and the Brčko District Assembly (skupstinabd.ba) on 30 October 2026. It prepares working papers; it is not authority to file or pay.

There is no state-level income tax in Bosnia and Herzegovina. Each of the three tax jurisdictions has its own law, rates, allowances, forms and tax administration. Find out which one applies before computing anything. VAT is the only general tax levied at state level (see [bosnia-vat](bosnia-vat.md)).

| | FBiH | RS | Brčko District |
|---|---|---|---|
| Law | Zakon o porezu na dohodak (Sl. novine FBiH 10/08, 9/10, 44/11, 7/13, 65/13) and Pravilnik o primjeni (consolidated to 12/26) | Zakon o porezu na dohodak (Sl. glasnik RS 60/15, amended to 114/25) | Zakon o porezu na dohodak (Sl. glasnik BD 60/10, amended to 5/25) |
| Authority | Porezna uprava FBiH | Poreska uprava RS | Porezna uprava, Direkcija za finansije BD |

Related skills in this pack:

- Monthly salary withholding, forms and the employer side: [bosnia-payroll](bosnia-payroll.md).
- Contribution rates and bases, including the self-employed: [bosnia-social-contributions](bosnia-social-contributions.md).
- VAT: [bosnia-vat](bosnia-vat.md). Companies: [ba-corporate-income-tax](ba-corporate-income-tax.md). Overview: [ba-tax-overview](ba-tax-overview.md). Planning: [bosnia-tax-optimization](bosnia-tax-optimization.md).

## Who this applies to

**FBiH (Law art. 2).** A resident is a person who has a domicile (prebivalište) in the Federation, or who stays there 183 days or more in a tax period, or who has an FBiH domicile and is paid from the federal or state budget for work outside the Federation. Residents are taxed on income from inside and outside the Federation. A person domiciled in RS or Brčko who works for an employer with its seat in the Federation is also treated as an FBiH resident for that salary (art. 2(4)). Non-residents (no domicile, fewer than 183 days) are taxed on FBiH-source employment income, business income through a permanent place of business, and income from property, rights and capital in the Federation. Foreign diplomats and OHR employees are out of scope (art. 3).

**RS (Law art. 6).** A resident has a domicile in RS, or stays 183 days or more in any 12-month period that starts or ends in the tax year, or has a permanent home and centre of vital interests in RS. The centre of vital interests can rest on, among others, property worth over 300,000 KM, a company stake over 100,000 KM, marriage to a citizen, a work permit or study. Residents are taxed on income from RS, the other entity, Brčko and abroad; non-residents only on RS-source income.

**Brčko District (Law art. 2 and 3).** Same tests as FBiH: domicile in the District, or 183 days in a tax period. A person domiciled in either entity who is employed by an employer seated in the District is treated as a District resident for that salary (art. 3(1)(e)), with the basic allowance (art. 25(22)).

**Kinds of income.** FBiH and Brčko tax income from employment, self-employment, property and property rights, capital investment, and prizes and games of chance (FBiH art. 4). RS taxes personal income (salary), self-employment, author and industrial property rights, capital, capital gains, foreign-source income and other income (RS art. 3).

**Not income in FBiH (art. 5):** dividends and profit shares, a resident's pension, child allowance, inheritances and gifts taxed under other laws, proceeds from selling assets used privately, insurance pay-outs used to repair property, and employee benefits up to the rulebook limits. **Not taxed in FBiH (art. 6):** among others, interest on bank savings and accounts and on government bonds, scholarships up to 75% of the average net salary, and student cooperative income up to four average monthly salaries a year.

## Rates, bands and thresholds

All amounts are in convertible marks (KM, BAM). There are no progressive bands in any of the three systems.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| FBiH income tax rate | 10% | 2026 | [FBiH Law art. 9](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf) |
| FBiH basic personal allowance | 3,600 KM a year (300 KM a month) | 2026 | [FBiH Law art. 24(1); Rulebook art. 21(6)](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf) |
| FBiH dependant factors (monthly) | spouse 0.5 (150 KM); 1st child 0.5 (150 KM); 2nd child 0.7 (210 KM); 3rd and each further child 0.9 (270 KM); other dependant 0.3 (90 KM); disability 0.3 (90 KM) | 2026 | [FBiH Law art. 24(2); Rulebook art. 21(6)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| FBiH dependant income limit | dependant's own income not above 3,600 KM a year | 2026 | FBiH Law art. 24(3) |
| FBiH short work, final tax | 10% with no allowance, work up to 10 days or 80 hours a month paid up to 250 KM | 2026 | FBiH Law art. 27(6) |
| FBiH rental, normed costs | 30% of rent; 50% for rooms and flats let to tourists who pay tourist tax | 2026 | FBiH Law art. 20(8) |
| FBiH occasional activity and author fees, normed costs | 20% of income (occasional); 30% or actual (author fees) | 2026 | FBiH Law art. 15(7) and (8) |
| FBiH flat-rate (paušal) tax, main occupation | 70, 30, 50, 80 or 70 KM a month by activity; half for a secondary occupation | 2026 | [FBiH Rulebook art. 53](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| FBiH prizes and games of chance | 10% final on each prize over 100 KM | 2026 | FBiH Law art. 23 and 34 |
| RS rate on personal income (salary) | 8% | 2026 | [RS Tax Administration notice, February 2026](https://poreskaupravars.org/izmjene-u-podnosenju-obrasca-1002-od-01-01-2026-godine-3/) |
| RS rate on self-employment income | 10% | 2026 | [RS Law art. 4(2) as amended by 119/21](https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20doprinosima.pdf) |
| RS rate on author rights, capital, capital gains and other income | 13% | 2026 | RS Law art. 4(3) as amended by 119/21 |
| RS basic personal allowance | 12,000 KM a year (1,000 KM a month) | 2026 | RS Law art. 10(3)(1) as amended by 119/21 |
| RS dependant allowance | 1,800 KM a year per dependant | 2026 | [RS Law art. 10(3)(2) as amended by 49/21](https://poreskaupravars.org/wp-content/uploads/2021/06/Zakon-o-izmjenama-Zakona-oa-porezu-na-dohodak-.pdf) |
| RS dependant income limit | 3,000 KM a year | 2026 | [RS Law art. 10(8) as amended by 66/18](https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-izmjenama-dopunama-Zakona-o-porezu-na-dohodak-SLGL-66_18.pdf) |
| RS voluntary pension and life insurance | each deductible up to 1,200 KM a year | 2026 | RS Law art. 10(1) as amended by 66/18 |
| RS tax-free part of salary for jobs needing no qualification or 3-year secondary school | 50 KM a month (net) | from 1 Jan 2026 | [RS Law art. 8(2)(13), added by 114/25](https://poreskaupravars.org/wp-content/uploads/2025/12/Dohodak.pdf) |
| RS small entrepreneur tax | 2% of total revenue | 2026 | [RS Law art. 23(1)](https://www.poreskaupravars.org/dokumenti/zakoni/zakonoporezunadohodak6015.pdf) |
| RS small entrepreneur minimum annual tax | 1,200 KM; 600 KM if revenue is not above 50,000 KM | 2026 | [RS Law art. 23(2) and 23a, by 110/24](https://poreskaupravars.org/wp-content/uploads/2025/01/Scan29012025.pdf) |
| RS small entrepreneur ceiling | revenue up to 100,000 KM, not VAT-registered, at most 3 workers | 2026 | RS Law art. 21 as replaced by 110/24 |
| RS small farmer tax | 0 KM up to 12,000 KM revenue; 200 KM up to 25,000; 400 KM up to 50,000 | 2026 | [RS Law art. 27b, added by 112/23](https://poreskaupravars.org/wp-content/uploads/2023/12/Scan26122023.pdf) |
| RS seasonal and temporary work | 9 KM tax per day of engagement | from 1 Jan 2026 | RS Law art. 52a, added by 114/25 |
| RS non-resident occasional services | 10% withholding on the gross fee, final | 2026 | RS Law art. 61a, added by 110/24 |
| Brčko income tax rate | 10% | 2026 | [BD Law art. 10](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf) |
| Brčko basic personal allowance | 14,400 KM a year (1,200 KM a month) | from 1 Aug 2022 | [BD Law art. 25(1) as amended by 21/22](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf) |
| Brčko life insurance with savings element | up to 1,800 KM a year added to the allowance | from 1 Aug 2022 | BD Law art. 25(8) as amended by 21/22 |
| Brčko meal allowance not taxed | up to 10 KM per working day | from 1 Jan 2023 | [BD Law art. 11(2)(c)(6) as amended by 45/22](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/05B45-22%20Zakon%20o%20izmjeni%20Zakona%20o%20porezu%20na%20dohodak.pdf) |
| Late payment interest | FBiH 0.04% a day; RS 0.03% a day; Brčko 0.03% a day | 2026 | [FBiH interest law art. 2](https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf); [RS ZPP art. 60](https://poreskaupravars.org/wp-content/uploads/2026/05/Zakon-o-poreskom-postupku-78-20.pdf); [BD ZPU art. 68](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf) |

## The taxable base

### Federation of BiH

**Employment (arts. 10, 11, 24, 27).** Income is the gross salary plus benefits in kind (car or other assets for private use, free or cheap housing, food, goods and services, interest-free or cheap loans, personal costs paid by the employer, debts paid or forgiven). Mandatory employee contributions for pension, health and unemployment are deducted (art. 11). The personal allowance from the employee's tax card (porezna kartica, PK-1002) is deducted monthly; without a card, no allowance is given (art. 27(3) and (4)). Tax is 10% of what is left. Gifts for holidays or company jubilees up to 30% of the average monthly salary published for the Federation, in total for the year, statutory severance and certain hardship payments are not income (art. 10(4); Rulebook art. 20(20)). Details of the employer side are in [bosnia-payroll](bosnia-payroll.md).

**Self-employment (arts. 12 to 19).** Crafts, agriculture and forestry (only if VAT-registered), liberal professions (doctors, lawyers, notaries, auditors, tax advisers, accountants, engineers, architects, translators and similar) and other independent activities. Profit is business income less business expenses paid in the year, on a cash basis, from the prescribed books (income and expense book KPR-1041, turnover book KP-1042, fixed-asset list, receivables and payables). Rules on expenses:

- Deductible: costs wholly and directly connected with the activity, including professional fees, staff meals up to the official limit, car costs for the business, contributions paid for staff and for oneself, training, interest on business loans and travel costs (art. 15(1) and (5)).
- Capped by the previous year's revenue: advertising 3%, entertainment 1%, sponsorship 1%, donations 0.5% (art. 15(6)).
- Not deductible: the income tax itself, fines and penalty interest, costs with no documents, costs not linked to the income, related-party costs above market value, and donations to political parties (art. 15(9)).
- Depreciation at the rates set by the Minister; assets under 1,000 KM and computer hardware and software can be written off in the year of purchase (art. 16).
- A tax loss is carried forward for five years (art. 26).
- A self-employed person whose only income is from the activity and who employs people with special needs or a disability over 50% for at least 10 months cuts the tax by 10% per such employee, up to 50% of the tax (art. 35(3)).

**Flat-rate tax (paušal, art. 31; Rulebook art. 52 and 53).** A craftsperson who is not VAT-registered can ask to pay a fixed monthly amount instead of keeping full books: 70 KM for home crafts without staff, 30 KM for old and traditional crafts, 50 KM for passenger transport with one vehicle, 80 KM for freight with one vehicle up to 8 tonnes, 70 KM for street retail. Half these amounts apply to a secondary occupation. The amount is due by the 15th of the next month. Card-free sales to companies carry an extra 10% final withholding on each payment. The Tax Administration ends the flat rate if income grows past the level the flat rate assumes or the person becomes VAT-liable.

**Property (arts. 20 and 32).** Rent from real estate and movable property: either actual costs or 30% normed costs, and the method chosen must be kept for this year and the next five. Rooms and flats let to tourists who pay tourist tax: 50% normed costs, and 10% tax on each collection is final. Sale of real estate: market value less cost uplifted by the industrial producer price index; no tax on the taxpayer's own home or on property held more than three years. Each gain is taxed separately at 10% and is final.

**Property rights and capital (arts. 21, 22, 32, 33).** Temporary licensing of author or industrial rights: 20% normed costs, payer withholds 10%, final. Interest on loans: 10% withholding, final, no allowance. Dividends are not income (art. 5).

**Allowances in the annual return (art. 24(7) and (8)).** Residents can add medical costs not covered by insurance, donations or the employer, and interest on a housing loan for buying or building a suitable flat. These are given only in the annual return.

### Republika Srpska

**Personal income (salary).** The base is gross personal income (art. 13 as amended by 119/21). Contributions are **not** deducted from the tax base. The monthly allowance of 1,000 KM (1/12 of 12,000) is deducted by the payer who holds the tax card (arts. 58(2) and 62). Dependants (spouse, children, parents with income up to 3,000 KM a year) add 1,800 KM a year each, and interest on a loan for the first home is deductible; both through the tax card (art. 10 as amended). The RS Tax Administration's 2026 example: gross 1,800 KM less the 50 KM tax-free part gives a contribution base of 1,750 KM; contributions 31% are 542.50 KM; the tax base is 1,750 less the 1,000 KM allowance, 750 KM; tax at 8% is 60 KM; net pay 1,197.50 KM. Meals in the employer's canteen or from a caterer are tax-free up to 0.75% of the previous year's average net salary a day (art. 8(2)(11) as amended by 56/22).

**Self-employment (art. 14 as replaced by 110/24).** Entrepreneurial activities are all business activities except the independent professions. Independent professions (samostalna zanimanja) are lawyers, notaries, health workers, vets, tour guides, engineers, architects, researchers, scientists, inventors, insolvency administrators, interpreters, experts, journalists, artists, athletes and brokers; accounting, bookkeeping, audit, tax and business consulting; advertising and market research. Profit is taxed at 10%. Advances are paid monthly by the 10th, based on the last annual return; a new business files an estimate within 30 days (art. 25a, added by 119/21).

**Small entrepreneur (arts. 21 to 25).** An entrepreneur (not an independent profession) can opt for a 2% tax on total revenue if, for the whole year: at most three workers; revenue (with related persons in the same activity) not above 100,000 KM and not VAT-registered; no joint activity; no outside investors. The minimum annual tax is 1,200 KM, or 600 KM if revenue is not above 50,000 KM. The choice is notified by 31 January of the year, or within 30 days of starting. Tax is paid on monthly revenue by the 10th of the next month with a monthly return, and it is final.

**Small farmer (arts. 27a to 27v).** A registered farm holder with revenue up to 50,000 KM can opt for a fixed annual tax (table above). Statement by 28 February, decision by 30 April, payment by 30 June.

**Capital, capital gains, author rights, other income.** 13% (art. 4(3)). Exempt income listed in art. 8 now has to be reported too (art. 61b, added by 114/25).

### Brčko District

The base follows the FBiH model: gross salary less employee contributions less the monthly allowance (arts. 11, 12, 28). The basic allowance is 1,200 KM a month. It rises by 50% of the basic allowance for a dependent spouse and for dependent children up to age 27, and by 10% for each 20% of certified disability (art. 25(4) and (5)). Life insurance with a savings element (up to 1,800 KM a year), interest on a first-home loan and children's tuition fees are added in the annual return (art. 25(8) to (17)). Meals up to 10 KM a working day and holiday gifts up to 30% of the average District net salary once a year are not taxed (art. 11). Self-employment, flat-rate tax, rent and capital follow rules close to FBiH; the District has its own flat-rate rulebook (art. 32(4)).

## Deadlines and filing

| What | FBiH | RS | Brčko |
|---|---|---|---|
| Salary withholding paid | same day as the salary or the first day after (Law art. 27(1)) | at the moment of payment (Law art. 61(1)) | same day or the first day after (Law art. 28(2)) |
| Monthly withholding report | MIP-1023 by the 15th for the previous month (Law art. 28(2); Rulebook) | Form 1002 by the 10th for the previous month (Law art. 61(4)) | monthly return (Law art. 38a) |
| Self-employed advances | 1/12 of last year's tax each month (art. 29) | monthly by the 10th (art. 25a) | 1/12 of last year's tax (art. 30) |
| Annual return | GPD-1051 by 31 March (art. 36(1)) | by 31 March (art. 60(3)) | by the end of February (art. 38(1)) |
| Joint activity return | by the end of February (art. 36(1)) | | |
| Employee's annual pay certificate | by the end of February (art. 28(3)) | after year-end (art. 61(2)) | |
| Start of activity, renting or foreign income | notify within 8 days (art. 38) | small entrepreneur option by 31 January or within 30 days of starting (art. 25) | notify within 8 days (art. 39) |
| Tax due with the annual return | paid in full by the filing deadline (art. 35(6)) | | paid by the filing deadline (art. 37(7)) |

**Who must file an annual return.** In FBiH and Brčko: anyone with income from more than one source, salary from two or more employers, income received directly from abroad, or other income for which the law requires a return. An employee with one employer and no other income does not file. People whose only income was taxed by final withholding (short work, tourist lets, property and rights sales, interest, prizes) do not file (FBiH art. 36(3) to (5); BD art. 38(3) to (5)). An FBiH employee may still file to claim the extra allowances. In RS an employee taxed at source with no other income does not file (art. 60(4)); small-entrepreneur revenue stays out of the annual return (art. 60(2)).

**Refunds.** FBiH: overpaid tax is set against other debts first; any refund is made within 90 days of the filing deadline (art. 35(7) and (8)).

## Penalties and interest

**FBiH (Zakon o Poreznoj upravi, arts. 84, 85, 87; interest law art. 2).**

- Return not filed: legal person 2,000 to 20,000 KM (responsible person 500 to 3,000 KM); individual 300 to 3,000 KM. For each return the Tax Administration has to prepare itself: 500 to 50,000 KM.
- Tax under-declared: 10% of the actual liability; if the declared tax is below 50% of the actual tax, a further 50% of the difference.
- Withholding report not filed: 200 KM per failure, up to 50,000 KM.
- Late payment interest: 0.04% for each day.

**RS (Zakon o poreskom postupku 78/20, arts. 60, 112, 113, 115; PIT Law art. 70b).**

- Return not filed or filed late: legal person 2,000 to 6,000 KM (responsible person 1,000 to 3,000 KM); entrepreneur 1,000 to 3,000 KM; individual 500 to 1,500 KM.
- Tax neither declared nor paid, found in an audit: 30% of the amount, up to 200,000 KM.
- Payer who does not withhold and pay tax: a fine equal to the tax that should have been withheld; responsible person 1,000 to 3,000 KM.
- Late payment interest: 0.03% a day.

**Brčko (Zakon o Poreznoj upravi 11/20, arts. 68 and 76).**

- Return not filed in the form, place or time required: legal person 1,000 to 5,000 KM; responsible person and entrepreneur 200 to 1,000 KM; individual 100 to 300 KM.
- Late payment interest: 0.03% a day, never more than the unpaid tax itself.

## Cross-border points

- **Between the entities.** Each jurisdiction taxes its residents on income from the other entity and Brčko too, and credits the tax paid there, capped at its own tax on that income, on certified documents only (FBiH art. 25; RS art. 67; BD art. 26). The FBiH and Brčko rules that treat an employee by the employer's seat (FBiH art. 2(4), BD art. 3(1)(e)) mean salary is normally taxed where the employer sits.
- **Foreign income.** Residents are taxed on worldwide income with a credit for foreign tax, capped the same way. Treaties for the avoidance of double taxation take priority (FBiH art. 35(5); BD art. 37(6)). An FBiH employee paid directly from abroad self-assesses the monthly advance within five days of receipt (FBiH art. 27(10)); in RS within seven days (RS art. 66).
- **Non-residents.** FBiH: occasional performers, artists and similar pay 10% withholding on the gross fee, final (art. 30(1)). RS: occasional services by non-residents carry 10% withholding on the gross fee, final, unless a treaty gives less (art. 61a). Losses of a foreign branch are not deductible (FBiH art. 26(3)).
- **Treaty rates and residence certificates** are not covered here. See [ba-tax-overview](ba-tax-overview.md).

## Worked examples

### Example 1: FBiH employee with one child, monthly salary 2,500 KM (2026)

An employee of a Sarajevo company earns gross 2,500 KM a month. The tax card shows factor 1.5: the basic allowance (1.0) and one dependent child (0.5). Employee contributions are 31% of gross (17% pension, 12.5% health, 1.5% unemployment; see bosnia-social-contributions).

- Contributions: 2,500 × 31% = 775 KM.
- Income after contributions: 2,500 − 775 = 1,725 KM.
- Allowance: 300 × 1.5 = 450 KM.
- Tax base: 1,725 − 450 = 1,275 KM. Tax at 10%: 127.50 KM.
- Net pay: 2,500 − 775 − 127.50 = 1,597.50 KM.

With one employer and no other income, the employee does not need to file GPD-1051 for 2026.

```oa-check
name: FBiH employee, gross 2500 KM, factor 1.5 (2026)
inputs:
  gross: 2500
  contribution_rate: 0.31
  basic_allowance: 300
  factor: 1.5
steps:
  - contributions: gross * contribution_rate
  - after_contributions: gross - contributions
  - allowance: basic_allowance * factor
  - tax_base: max(after_contributions - allowance, 0)
  - tax: tax_base * 0.10
  - net: gross - contributions - tax
expected:
  contributions: 775.00
  tax_base: 1275.00
  tax: 127.50
  net: 1597.50
```

### Example 2: RS small entrepreneur below the minimum tax (2026)

A hairdresser in Banja Luka runs a registered business with one worker, is not VAT-registered, and chose small-entrepreneur status by 31 January 2026. Revenue for 2026 is 24,000 KM.

- 2% of revenue: 24,000 × 2% = 480 KM.
- Revenue is not above 50,000 KM, so the minimum annual tax is 600 KM (art. 23a), not 1,200 KM.
- The annual tax is the higher figure: 600 KM. The monthly 2% payments made by the 10th of each month count towards it.

If revenue had been 70,000 KM, the tax would be 1,400 KM (2%), above the 1,200 KM minimum.

```oa-check
name: RS small entrepreneur, revenue 24000 KM (2026)
inputs:
  revenue: 24000
  rate: 0.02
  minimum_low: 600
steps:
  - tax_at_rate: revenue * rate
  - annual_tax: max(tax_at_rate, minimum_low)
expected:
  tax_at_rate: 480.00
  annual_tax: 600.00
```

## Ask the client first

1. Where is the person domiciled, where do they work, and where is the employer's seat (FBiH, RS or Brčko)? This picks the law.
2. Do they have a tax card filed with the employer, and which dependants are on it?
3. What income besides one salary: self-employment, rent, tourist lets, property sales, interest on private loans, income from abroad or from the other entity?
4. If self-employed: which activity (craft, liberal profession, independent profession), books or flat rate, VAT-registered or not, how many workers, and the revenue for the year?
5. Any foreign or other-entity tax paid, with certified proof?
6. Any housing-loan interest, medical costs (FBiH), life insurance or tuition fees (Brčko) to claim in the annual return?

## Sources

| Source | URL | Read on |
|---|---|---|
| FBiH Zakon o porezu na dohodak (consolidated, 10/08 to 65/13), arts. 2 to 38, 45 | https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf | 2026-10-30 |
| FBiH Pravilnik o primjeni Zakona o porezu na dohodak (consolidated to 12/26), arts. 20, 21, 29, 52, 53 | https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf | 2026-10-30 |
| FBiH Zakon o Poreznoj upravi (consolidated to 44/22), arts. 84 to 87 | https://www.pufbih.ba/v1/public/upload/zakoni/a0e37-zakon-o-poreznoj-upravi-fbih-preciscen-tekst-novi-22.pdf | 2026-10-30 |
| FBiH Zakon o visini stope zatezne kamate na javne prihode (consolidated to 77/25), art. 2 | https://pufbih.ba/v1/public/upload/zakoni/1%20Zakon%20o%20visini%20stope%20zatezne%20kamate%20na%20javne%20prihode%20-%20PRECISCEN%20TEKST.pdf | 2026-10-30 |
| FBiH Tax Administration, list of regulations (API) | https://pufbih.ba/propisi-zakoni | 2026-10-30 |
| RS Zakon o porezu na dohodak 60/15 (gazette text), arts. 3 to 6, 21 to 25, 58 to 67 | https://www.poreskaupravars.org/dokumenti/zakoni/zakonoporezunadohodak6015.pdf | 2026-10-30 |
| RS amendment 66/18 (art. 10 allowances, arts. 70a to 70c fines) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-izmjenama-dopunama-Zakona-o-porezu-na-dohodak-SLGL-66_18.pdf | 2026-10-30 |
| RS amendment 49/21 (art. 10 dependants 1,800 KM) | https://poreskaupravars.org/wp-content/uploads/2021/06/Zakon-o-izmjenama-Zakona-oa-porezu-na-dohodak-.pdf | 2026-10-30 |
| RS Službeni glasnik 119/21 page with PIT and contributions amendments (art. 4 rates, art. 10 allowance 12,000 KM, art. 13 base) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20doprinosima.pdf | 2026-10-30 |
| RS amendment 56/22 (meal allowance) | https://poreskaupravars.org/wp-content/uploads/2022/06/Zakon-o-izmjenama-i-dopunama-Zakona-o-doprinosima-i-porezu-na-dohodak-.pdf | 2026-10-30 |
| RS amendment 112/23 (small farmer) | https://poreskaupravars.org/wp-content/uploads/2023/12/Scan26122023.pdf | 2026-10-30 |
| RS amendment 110/24 (self-employment definitions, small entrepreneur, non-resident withholding) | https://poreskaupravars.org/wp-content/uploads/2025/01/Scan29012025.pdf | 2026-10-30 |
| RS amendment 114/25 (50 KM tax-free part, seasonal work, reporting exempt income) | https://poreskaupravars.org/wp-content/uploads/2025/12/Dohodak.pdf | 2026-10-30 |
| RS Tax Administration, changes to Form 1002 from 1 January 2026 (worked example) | https://poreskaupravars.org/izmjene-u-podnosenju-obrasca-1002-od-01-01-2026-godine-3/ | 2026-10-30 |
| RS Zakon o poreskom postupku 78/20, arts. 60, 112 to 115 (amended by 37/22, which does not touch these articles) | https://poreskaupravars.org/wp-content/uploads/2026/05/Zakon-o-poreskom-postupku-78-20.pdf | 2026-10-30 |
| Brčko Zakon o porezu na dohodak, unofficial consolidated text (60/10, 14/17, 24/20) | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf | 2026-10-30 |
| Brčko amendments 21/22, 45/22 and 5/25 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf | 2026-10-30 |
| Brčko Zakon o Poreznoj upravi 11/20, arts. 68 and 76 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20Poreznoj%20upravi%20Brc--ko%20Distrikta%20BiH/011B11-20%20Zakon%20%20o%20poreznoj%20upravi%20Brcko%20distrikta%20BiH.pdf | 2026-10-30 |

Not yet confirmed: the wording of RS Law art. 4(1) after 119/21 (the 8% salary rate is taken from the RS Tax Administration's 2026 worked example, not from the article text, which was not on the scanned page); how the RS small-entrepreneur minimum tax is topped up during or after the year; the FBiH capital-gains rules for shares and securities (FMF general opinion 2025 not read); RS capital gains computation and holding-period rules after 2015; the Brčko flat-rate (paušal) amounts and Brčko monthly return form; FBiH accelerated depreciation rules; treaty withholding rates; whether any FBiH Law amendment after 65/13 exists (the Tax Administration's list of 12 October 2026 shows none).

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
