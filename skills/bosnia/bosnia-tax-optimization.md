---
name: bosnia-tax-optimization
description: Use this skill whenever asked about reducing tax in Bosnia and Herzegovina, tax planning, or legal strategies to minimise tax for a self-employed person or small company, tax year 2026. Trigger on phrases like "reduce tax Bosnia", "flat 10% tax Bosnia", "small entrepreneur 2%", "FBiH vs RS tax", "sole proprietor vs doo Bosnia", "0% dividend Bosnia", "save tax Bosnia", "tax planning Bosnia". This skill covers the flat income tax (FBiH 10%, RS 8% on salary, Brčko 10%) and the monthly allowances, the RS small-entrepreneur 2%-of-revenue option, the FBiH-vs-RS choice for salaries and contributions, the 10% profit tax with no income tax on dividends to FBiH, RS and Brčko residents, and the disguised-employment red line. ALWAYS read this skill before advising on any Bosnia and Herzegovina tax optimisation. The detailed computations are out of scope and sit in bosnia-income-tax, bosnia-payroll, bosnia-social-contributions and ba-corporate-income-tax.
version: 0.3
jurisdiction: BA
tax_year: 2026
last_updated: 2026-11-15
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Bosnia and Herzegovina Tax Optimization v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This decision skill produces a tax-planning comparison and review brief for **tax year 2026** in Bosnia and Herzegovina: the Federation of BiH (FBiH), Republika Srpska (RS), and Brčko District (BD). Amounts are in KM, also identified as BAM or convertible marks. It compares eligible sole-proprietor regimes, employment costs where the jurisdiction genuinely follows the facts, and lawful company extraction. It does not prepare an election, payslip, return or dividend resolution.

The headline levers remain ordinary flat income/profit tax, the RS small-entrepreneur revenue basis, the restricted FBiH flat-rate option and individual dividend exclusions. A lower headline rate does not establish a cheaper or legally available arrangement. Contributions, the annual tax floor, recipient type, genuine business/employment facts and overdue liabilities can decide the answer.

Load `bosnia-income-tax.md`, `bosnia-payroll.md`, `bosnia-social-contributions.md`, `ba-corporate-income-tax.md`, `bosnia-vat.md` and `ba-cross-border.md` for their separate computations. This skill preserves the earlier requirement to reconcile sibling figures, but **the operative statute controls a contradiction**. Do not copy a conflicting sibling assertion into usable advice. None of those passing siblings is newly verified or amended by this rewrite.

### Quick reference

| Decision | 2026 starting point | Condition and official source |
|---|---|---|
| RS salary versus ordinary business income | Salary 8%; ordinary self-employment 10% | Different bases; [119/21 art 1, PIT 4(1)–(2)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip) |
| RS small entrepreneur | 2% of total revenue; annual minimum 1,200, or 600 where annual revenue is not above 50,000 | All-year cumulative eligibility, no real-expense deduction from revenue; [PIT 23(1)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [110/24 arts 2–4, PIT 21/23/23a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip) |
| FBiH salary | 10% after paid employee contributions; basic monthly allowance 300 derived from 3,600 annual | Resident eligibility and tax card; [PIT 9/11/24/27](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf) |
| RS salary base | Gross less applicable allowance; 1,000 monthly derived from 12,000 annual | Full-time basic allowance; part-time/multiple-payer adjustment; contributions not deducted from PIT base; [66/18 art 2, PIT 10](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porez%20dohodak_la.zip); [119/21 arts 2/4/5](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip) |
| BD salary | 10% after paid mandatory employee contributions; resident allowance 1,200 monthly | No BD contribution computation supplied here; [PIT 10/12](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf); [21/22 art 2, PIT 25(1)](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf) |
| FBiH ordinary contributions | Employee 31% and employer 5%, both derived sums | Employer reduction applies from 1 July 2025; special bases/categories and other levies separate; [Contributions 10, consolidated 33/25](https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf) |
| RS ordinary contributions | 31% derived, withheld from gross base | 18.5% pension + 10.2% health + 0.6% unemployment + 1.7% child protection; [Contributions 22/24](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20doprinosima_la.zip); [112/19 art 2](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20Zak%20doprinosima_la.zip); [119/21 art 3](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20doprinosima_la.zip) |
| Ordinary company profit tax | 10% in FBiH, RS and BD | Applied to statutory taxable profit; [CIT 31](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 36](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip); [CIT 20](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf) |
| Resident individual dividend extraction | FBiH/BD: not income; RS: PIT exemption | Genuine dividend, recipient facts and reporting still checked; [PIT 5(1)(1)](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [PIT 6(a)](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf); [original PIT 8(3)(13)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [105/19 art 1](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porezu%20na%20dohodak_la.zip); [112/23 art 2](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zakon_o_dop_zakona_o_porezu_na_dohodak_hp_la.zip); [PIT 61b](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip) |
| VAT | 17%; compulsory registration threshold 100,000 | Statutory taxable/zero-rated turnover and related controlled persons; not a universal cash-receipts test; [VAT 23/57](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf); [80/23 art 1](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf) |

**Who stands behind it:** tier 2; no licensed Bosnian tax adviser has approved this version. Sources below identify what was actually read on 15 November 2026. Calculations are working papers for professional review.

## Ask the client first

1. Where do the individual and employer actually reside, work, register and maintain their business presence? Obtain the employment contract, business registration and any cross-entity working facts.
2. Is the activity an entrepreneurial business, independent profession, employment, supplementary occupation or a company? Obtain the actual activity classification and evidence of control, clients and business risk.
3. What are annual revenue, taxable profit, real deductible expenses, related-person revenue, VAT status, staff count, joint activity and outside investment for the whole year?
4. For salary, obtain gross contractual pay, hours/full-time status, tax card, dependants, job qualification, tax-free components and applicable contribution category/minimum base. Do not assume the old comparison is a real payslip.
5. For a dividend, identify whether the recipient is an individual or legal person, residence, beneficial entitlement, distributable profit, the company's tax/contribution/wage liabilities and any treaty evidence.
6. Is a regime election already effective, and what changes are proposed? Obtain approvals, prior returns and tax/contribution balances before computing an achievable saving.

## The method, step by step

### Classify the facts before comparing rates

Choose the actual jurisdiction and income category, then construct a comparison using the same revenue, time period and genuine business/employment facts. FBiH PIT 2(4) specifically treats an RS/BD-resident individual earning employment income from an employer seated in FBiH as resident for that law. RS PIT 64 assigns payment by the relevant residence, activity registration or property/source rule. Neither provision makes a nominal registered address a free tax-rate election. [[FBiH PIT 2](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [RS PIT 64](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip)]

**AUDIT FLASH POINT**: a single-client proprietor under employer-like direction may have employment-classification risk. Do not invent an automatic statutory client-count safe harbour or say that a single client proves independence. FBiH PIT 10 includes remuneration for work performed under the employer's instructions; RS PIT 14 distinguishes entrepreneurial and independent professional activity. Keep employment and dividend extraction genuine. [[PIT 10](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [110/24 art 1, PIT 14](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

### Compare the RS small-entrepreneur and ordinary bases

First test **all-year cumulative** eligibility under PIT 21 as replaced by 110/24. The person must carry on entrepreneurial activity within PIT 14(2); employ no more than 3 workers; have annual revenue not above 100,000 and not be VAT-registered; have no joint activity; and have no other person investing in that activity. The revenue test aggregates the entrepreneur and related persons carrying on the same activity. The specified related family includes spouse/partner, children/adopted children, parents/adopters, and siblings living in the same household. Do not split one activity across those persons to assume a fresh threshold. [[110/24 art 2, PIT 21](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

Independent professions within PIT 14(3) are excluded. Preserve the full category: lawyers, notaries, health workers, veterinarians, tourist guides, engineers, architects, researchers, scientists, inventors, bankruptcy administrators, interpreters, experts, journalists, artists, athletes and brokers; accounting, bookkeeping, auditing, tax/business/management consulting; and advertising/market research. Actual classification matters; a generic registration label does not override the activity. [[110/24 art 1, PIT 14](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

For an eligible person with an effective election, calculate annual small-entrepreneur income tax as the larger of **2% of total revenue** and the applicable annual minimum: **600 if revenue is not above 50,000**, otherwise **1,200**. Expenses do not reduce the revenue base. Contributions and other obligations are separate. The normal route applies **10% to statutory net income**, starting with revenue less qualifying paid business expenses, not an unchecked accounting-profit figure. [[PIT 15/17/23](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [PIT 4(2)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip); [PIT 23(2)/23a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

The original shortcut said that 2% wins when profit exceeds 20% of revenue. Preserve the comparison, but apply it only when the minimum is not binding and the ordinary taxable base equals the profit used. Otherwise compute both tax amounts. The original example remains: **revenue 60,000 gives 2%×60,000=1,200**, equal to the 1,200 minimum for revenue above 50,000. Normal tax is also 1,200 on profit 12,000; higher taxable profit makes the 2% route cheaper on income tax alone. The floor counterexample under Worked cases prevents using 20% as a blanket decision rule.

VAT registration also removes the non-VAT qualification, including a voluntary registration. The VAT statute tests taxable and creditable exempt turnover in the preceding year or likely to exceed the threshold, with controlled-related-person aggregation. Do not wait for cash revenue above the threshold while ignoring the statutory forecast or linked persons. [[VAT 57/58](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf); [80/23 art 1](https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf); [PIT 21](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

### Compare FBiH flat-rate and net-income taxation

FBiH PIT 31 permits paušal only for qualifying self-employment outside VAT, subject to the Minister's criteria and an effective authority decision. Current Rulebook 52 covers homecraft alone without employees; traditional/old crafts alone or with at most 2 employees; qualifying transport with 1 vehicle up to 8 tonnes; and qualifying individual retail by personal work outside a shop without employees. The homecraft/traditional-craft routes require application and proof; the transport/retail routes have the authority's decision on its records. Do not assume every freelancer can elect. [[PIT 31](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [Rulebook 52](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf)]

| Qualifying FBiH activity | Monthly paušal, 2026 | Official source |
|---|---|---|
| Homecraft alone, no employees | 70 | [Rulebook 53(1)(a)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Traditional/old crafts | 30 | [Rulebook 53(1)(b)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Passenger transport with qualifying single vehicle | 50 | [Rulebook 53(1)(c)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Freight transport, single vehicle up to 8 tonnes | 80 | [Rulebook 53(1)(d)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Individual retailer outside shop by personal work | 70 | [Rulebook 53(1)(e)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Supplementary occupation with qualifying decision | 50% of corresponding amount | [Rulebook 53(2)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| Occasional cashless receipts from legal persons | Additional 10% withholding on each qualifying receipt | Not absorbed into monthly paušal; [Rulebook 53(5)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |

The rulebook's temporary half reduction ending 31 December 2022 is historical and unusable for 2026. Compare the actual authorised flat amount plus any required receipt withholding and separate contributions with ordinary 10% taxable net-income treatment. Conditions changing during the year can end paušal; do not preserve the flat amount after eligibility is lost. [[Rulebook 53/54](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf); [PIT 9/31](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf)]

### Compare genuine salary arrangements

FBiH ordinary salary PIT starts with taxable remuneration, deducts paid mandatory employee contributions, then applies eligible personal allowances under the tax-card rules before 10%. The 300 basic monthly allowance is derived from 3,600 annual. RS ordinary salary PIT uses gross remuneration less eligible allowances at 8%; the old contribution expense deduction was deleted by 119/21. The 1,000 basic monthly allowance is derived from 12,000 annual and is for full-time employment, prorated for part-time/multiple-payer facts. [[PIT 9/11/24/27](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [PIT 10/58](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porez%20dohodak_la.zip); [PIT 4/10/12/13](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip)]

For the ordinary contribution categories, FBiH employee 31% and employer 5% are derived from the component rates in Contributions 10; employer 5% applies from 1 July 2025. RS 31% is derived from 18.5% pension, 10.2% health, 0.6% unemployment and 1.7% child protection and is withheld from the base. Do not treat these as the full set of every possible employer levy or a substitute for special bases. [[Contributions 10](https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf); [Contributions 22/24](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20doprinosima_la.zip); [112/19 art 2](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20Zak%20doprinosima_la.zip); [119/21 art 3](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20doprinosima_la.zip)]

RS 2026 has a further 50 KM net monthly salary exemption for the statutory job categories. The exact statute refers to jobs requiring no education level and jobs requiring **“najmanje stečeno srednje obrazovanje u trajanju od tri godine”**. Do not silently replace that wording with a broader or narrower education rule. Establish the applicable job and reporting classification before using relief; the original salary illustration assumes no tax-free parts. The applicable ordinary contribution exemption follows Contributions 21; special bases can produce a different result. Detailed job-code/form mechanics remain with the payroll workflow and require its current source confirmation. [[114/25 art 2, PIT 8(2)(13)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip); [Contributions 21, with 112/19 deletion of former paragraph 2](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20doprinosima_la.zip)]

BD taxes salary at 10% after deductible paid employee contributions and allows qualifying residents 1,200 monthly under 21/22. This skill gives no BD salary illustration because the applicable contribution/insurance category is not established here. Likewise, entity-specific self-employed contributions remain a separate computation: **income-tax savings are not total-cost savings**. [[PIT 10/12](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf); [PIT 25(1)](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf)]

### Check company extraction separately

Ordinary company taxable profit is taxed at 10% in each jurisdiction. A genuine dividend/profit share to a resident individual is not income under FBiH PIT 5(1)(1) or BD PIT 6(a); RS PIT 8(4)(14) exempts it after the renumbering chain. This is different from a corporate participation exemption or a foreign-recipient withholding rule. The earlier statement that 10% is the whole tax on distributed profit is usable only as narrow arithmetic with ordinary taxable profit, a qualifying resident individual, lawful distribution and no separate charge. It is not a universal effective-tax guarantee. RS 2026 PIT 61b requires reporting exempt income; exemption does not mean no declaration. [[CIT 31](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 36](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip); [CIT 20](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf); [PIT 5](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [PIT 6](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf); [original PIT 8](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [105/19 art 1](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porezu%20na%20dohodak_la.zip); [112/23 art 2](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zakon_o_dop_zakona_o_porezu_na_dohodak_hp_la.zip); [PIT 61b](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip)]

| Foreign dividend recipient: corporate-tax withholding regime | Domestic treatment before treaty relief | Condition and official source |
|---|---|---|
| FBiH nonresident legal person within CIT withholding scope | 5% of gross dividend | Do not apply a corporate-tax rule automatically to a foreign individual; [CIT 38(1)/(6)/(7)](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf) |
| RS foreign legal person | 10% unless applicable treaty | The old 5% exception was deleted; [CIT 44/45](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip); [1/17 art 15](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dobit_la.zip) |
| BD foreign legal person | Dividend income excluded from withholding | Distinguish branch-profit and other exceptions; [CIT 28/29(2)(d)](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf) |

The original “foreign owner” comparison is therefore retained with its recipient-type boundary. Do not infer any particular treaty rate or individual-owner tax from it. Obtain the actual residence/beneficial-entitlement documents and use `ba-cross-border.md` and the applicable treaty before payment. RS statutory treaty evidence includes the prescribed residence/document conditions; 114/25 removes automatic submission of retained evidence, not the duty to have it. [[CIT 52 as replaced](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dobit_la.zip); [114/25 art 16](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dobit.zip)]

**No distribution while in arrears:** FBiH CIT 55(1) prohibits profit distributions where direct-tax/contribution obligations **or employment-income obligations** remain unpaid on the payment date. RS CIT 54 prohibits dividend/profit-share payments while due tax liabilities remain unpaid. Preserve the original salary-versus-dividend decision, but check distributable profit, genuine remuneration and these payment restrictions first. [[CIT 55](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 54](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip)]

## Boundary and exception table

| Trigger | Required treatment | Source |
|---|---|---|
| Related family carrying on same RS activity | Aggregate revenue for small-entrepreneur entry; do not fabricate independent thresholds | [PIT 21(2)–(3)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip) |
| Small-business annual floor binds | Compute both tax amounts; derived 20% margin shortcut alone cannot decide | [PIT 23](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [PIT 23a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip) |
| VAT registration or independent profession | Do not use RS small-entrepreneur route despite a favourable numerical comparison | [PIT 14/21](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip) |
| FBiH flat-rate receipts from legal persons by bank | Check additional 10% withholding, rather than treating flat payment as entire tax | [Rulebook 53(5)](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf) |
| RS job qualification may attract salary relief | Establish statutory job and actual insurance base; do not mechanically use the no-relief fixture | [PIT 8(2)(13)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip); [Contributions 21](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20doprinosima_la.zip) |
| Genuine cross-entity work/seat/registration facts | Determine jurisdiction before comparing; address-only region shopping is refused | [PIT 2](https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf); [PIT 64](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip) |
| Foreign individual dividend recipient | Do not apply corporate-recipient withholding table automatically; confirm individual/treaty treatment first | [CIT 38](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 44/45](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip); [CIT 28/29](https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf) |
| Unpaid distribution-blocking liabilities | Stop proposed payment until lawful clearance | [CIT 55](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 54](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip) |

## Worked cases

### Original salary comparison, retained in full

The complete earlier raw illustration and executable block follow unchanged. They model ordinary full-time salary with the stated absence of tax-free parts, not a conclusion about any actual person's eligibility. For 2026, determine qualification-dependent relief, minimum/special contribution bases and tax-card/residence facts before applying it. Employer “cost” in this illustration means gross pay plus the stated employer contributions only; other employer levies are outside this comparison. The two calculated net-pay figures differ by 28 and the contribution-only employer outlays by 100, both derived from the fixture.

**Illustration: gross salary KM 2,000 a month, single employee with no dependants, no tax-free parts**

FBiH: employee contributions 31% are KM 620. The tax base is 2,000 - 620 - 300 = KM 1,080, and tax at 10% is KM 108. Net pay is KM 1,272. The employer adds 5%, KM 100, so the cost is KM 2,100.

RS: contributions 31% are KM 620. The tax base is 2,000 - 1,000 = KM 1,000, and tax at 8% is KM 80. Net pay is KM 1,300. The employer pays no contributions on top, so the cost is KM 2,000.

```oa-check
name: Gross KM 2,000 salary, FBiH vs RS, 2026
inputs:
  gross: 2000
  fbih_allowance: 300
  rs_allowance: 1000
steps:
  - fbih_contrib: gross * 0.31
  - fbih_base: gross - fbih_contrib - fbih_allowance
  - fbih_tax: fbih_base * 0.10
  - fbih_net: gross - fbih_contrib - fbih_tax
  - fbih_employer_cost: gross + gross * 0.05
  - rs_contrib: gross * 0.31
  - rs_base: gross - rs_allowance
  - rs_tax: rs_base * 0.08
  - rs_net: gross - rs_contrib - rs_tax
  - rs_employer_cost: gross
expected:
  fbih_contrib: 620
  fbih_base: 1080
  fbih_tax: 108
  fbih_net: 1272
  fbih_employer_cost: 2100
  rs_contrib: 620
  rs_base: 1000
  rs_tax: 80
  rs_net: 1300
  rs_employer_cost: 2000
```

The minimum contribution bases, tax-free parts and dependant allowances change these numbers. Use `bosnia-payroll.md` for a real payslip.

### Decision: same revenue, taxable profit at and above the crossover

Assume an eligible full-year RS entrepreneur with an effective election, no related-person complication, no VAT registration and the same separate contribution costs under either comparison. Revenue 60,000 means 2% tax 1,200, equal to the 1,200 floor. Ordinary tax on taxable profit 12,000 is 1,200, so there is no income-tax saving. At taxable profit 18,000, ordinary tax 1800 exceeds small-business tax 1,200 by 600. This preserves the original 60,000/12,000/1,200 comparison and makes its deciding assumption explicit. [[PIT 23](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [PIT 4(2)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip); [PIT 23(2)/23a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

```oa-check
name: RS regime decision at and above the crossover
inputs:
  revenue: 60000
  profit_at_crossover: 12000
  higher_profit: 18000
  annual_floor: 1200
steps:
  small_tax: max(revenue * 0.02, annual_floor)
  ordinary_at_crossover: profit_at_crossover * 0.10
  ordinary_higher_profit: higher_profit * 0.10
  saving_at_crossover: ordinary_at_crossover - small_tax
  saving_higher_profit: ordinary_higher_profit - small_tax
expected:
  small_tax: 1200
  ordinary_at_crossover: 1200
  ordinary_higher_profit: 1800
  saving_at_crossover: 0
  saving_higher_profit: 600
```

### Decision: annual minimum overturns the headline margin rule

Keep the same eligibility assumptions, but revenue 24,000 and taxable profit 5000. Profit is 20.833333% of revenue, derived and rounded here, yet 2% of revenue is only 480. The 600 annual minimum raises small-business tax to 600; ordinary 10% tax is 500. The ordinary route saves 100 on income tax alone. This is why the annual floor must be applied before recommending a regime. Contributions, election feasibility and actual deductible expenses remain separate. [[PIT 23](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [PIT 4(2)](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip); [PIT 23a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip)]

```oa-check
name: RS annual minimum reverses the margin shortcut
inputs:
  revenue: 24000
  taxable_profit: 5000
  annual_floor: 600
steps:
  revenue_tax: revenue * 0.02
  small_tax: max(revenue_tax, annual_floor)
  ordinary_tax: taxable_profit * 0.10
  ordinary_saving: small_tax - ordinary_tax
  margin_percent: taxable_profit / revenue * 100
expected:
  revenue_tax: 480
  small_tax: 600
  ordinary_tax: 500
  ordinary_saving: 100
  margin_percent: 20.833333
```

## When to refuse or refer

- **Prohibition 1:** never combine the RS revenue regime with a deduction for real expenses from that revenue base. Use the alternative ordinary basis only where lawfully available.
- **Prohibition 2:** never recommend RS/FBiH registration purely for a rate without genuine presence and the correct jurisdictional facts. **AUDIT FLASH POINT**.
- **Prohibition 3:** never present single-client work as safe self-employment. Refer control, direction and economic-substance issues before comparing tax.
- **Prohibition 4:** reconcile `bosnia-income-tax.md`, `bosnia-social-contributions.md`, `bosnia-payroll.md` and `ba-corporate-income-tax.md`; preserve their ordinary 31% RS employee withholding and 5% FBiH employer contribution context where applicable, but resolve any conflict from the operative law rather than giving a sibling automatic priority.
- **Prohibition 5:** never present held items as confirmed or the comparison as definitive advice. Route the working papers to a licensed Bosnian tax adviser.
- Refuse the RS small regime for excluded independent professions or failed all-year entry tests, and stop any proposed dividend barred by arrears.
- Refer unknown BD insurance rates, self-employed contribution amounts, treaty/foreign-individual outcomes, and unconfirmed current election or filing mechanics. Do not invent a penalty, portal field, deadline extension or tax-free salary classification to finish a comparison.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Bosnia and Herzegovina) before acting upon.

## Filing and payment

This planning skill does not itself establish that an election has been accepted. Obtain the authority decision/status first; a numerically cheaper outcome is not a valid election. RS PIT 24 requires payment on monthly revenue by the 10th of the next month; PIT 24a requires the monthly return by the same 10th. The ordinary self-employment advance under 25a is also monthly by the 10th of the following month. If eligibility is lost/revoked, establish the ordinary annual liability and credit prior tax under 26. Actual election/withdrawal filing forms, evidence and portal steps remain held until current operational instructions are confirmed. The statutory monthly rules above are sourced separately. [[PIT 24/26](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip); [PIT 24a/25a](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip)]

For authorised FBiH paušal, monthly payment is due by the 15th of the next month; occasional bank receipts from legal persons have their separate withholding rule. Keep the authority approval and receipt records. [[Rulebook 52/53](https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf)]

RS 2026 exempt-income reporting must be checked even where dividend PIT is exempt. Foreign corporate dividend withholding/treaty evidence and corporate payment restrictions are separate from personal PIT. Route actual returns and payments through the relevant income, payroll, corporate or cross-border skill after checking their current sources. No specific penalty or interest figure is asserted here; the current tax-procedure provisions must be sourced before quantifying a late-payment or reclassification exposure. [[PIT 61b](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip); [CIT 52](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dobit_la.zip); [114/25 art 16](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dobit.zip); [CIT 55](https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf); [CIT 54](https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip)]

## Completion checklist

- Trace every input to the contract, registration, tax card, bookkeeping and prior authority decisions.
- Identify jurisdiction, actual activity, all-year eligibility and relevant related persons before calculating.
- Apply each revenue floor, real taxable-profit adjustment, VAT interaction, contribution base and salary exemption independently.
- Recompute both options; show income tax and separate contribution/other employer costs without calling a partial comparison a total saving.
- Preserve the complete historical fixture and distinguish its assumptions from the actual client's facts.
- Check recipient type, genuine dividend, reporting and distribution-blocking liabilities before proposing extraction.
- Reconcile any sibling contradiction to the current statute, document remaining gaps and obtain qualified professional review before action.

## Sources

The following operative provisions and neighboring conditions were actually read on 2026-11-15. Parliament adopted-law attachments recover RS originals where direct tax-authority PDFs failed; a file named “Prijedlog” is used only where its actual text/index establish the adopted law. No search snippet or merely successful download is treated as reading. The old 119/21 income-tax source linked a contributions document; the correct income-tax original is now separately cited.

| Source and read scope | URL | Read on |
|---|---|---|
| FPIT: Read for arts. 1–5, 9–12, 18–20, 24, 26–27, 31 and neighbors; authority unofficial consolidation to 65/13. | https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf | 2026-11-15 |
| FCON: Read for arts. 1–5, 10, 10a, 10b, 11 and neighbors; authority unofficial consolidation through 33/25, commencement footnote 1 July 2025. | https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf | 2026-11-15 |
| FCIT: Read for arts. 1–6, 31–32, 38 and 55–56. Authority direct PDF and earlier capture hashes identical; art. 5(2) defines a nonresident legal person. | https://www.pufbih.ba/v1/public/upload/zakoni/9080b-zakon-o-porezu-na-dobit-precisceni.pdf | 2026-11-15 |
| FRULE: Read for complete current rulebook arts. 52–54 and neighbors; eligibility, approval, amounts, supplement and ended 2022 reduction distinguished. | https://pufbih.ba/v1/public/upload/zakoni/16_02_2026teksta%20Pravilnika%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak_12_26/16_02_2026_PRECISCENI%20Pravilnik%20o%20primjeni%20Zakona%20o%20porezu%20na%20dohodak%2012-26.pdf | 2026-11-15 |
| RPIT: Read for arts. 1–10, 14–27, 58–64 and 73–74. Adopted index attachment filename says Prijedlog; actual body ZAKON signed 16 July 2015, effective 1 September 2015. Superseding amendments read separately. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog_zakona_o_porezu_na_dohodak_0.zip | 2026-11-15 |
| RPIT 18: Read for complete arts. 1–7; replaces art. 10, including full-time/proportional and tax-card conditions, and art. 58(2). | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porez%20dohodak_la.zip | 2026-11-15 |
| RPIT 19: Read for complete arts. 1–4; adds art. 8(1), renumbers former art. 8(3) as art. 8(4). | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porezu%20na%20dohodak_la.zip | 2026-11-15 |
| RPIT 20: Read for complete arts. 1–6; dividend point 13 retained, capital-gain amendments separate. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Prijedlog%20zakona%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak%20latinica_la.zip | 2026-11-15 |
| RPIT 21: Read for complete arts. 1–9: salary rate 8%, business rate 10%, allowance 12,000, gross base, deleted contribution deduction, filing by the 10th. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dohodak_la.zip | 2026-11-15 |
| RPIT 23: Read for complete arts. 1–8; dividend point 13 renumbered as 14; small farmer separate regime, not generic small entrepreneur. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zakon_o_dop_zakona_o_porezu_na_dohodak_hp_la.zip | 2026-11-15 |
| RPIT 24: Read for complete arts. 1–7: PIT arts. 14, 21, 23 and 23a, related-family aggregation; the 2025 transition is distinct. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_porezu_na_dohodak_hp_la.zip | 2026-11-15 |
| RPIT 25: Read for complete arts. 1–10: 2026 salary exemption of 50 net for specified jobs, exempt-income reporting and seasonal rules; 8% and 10% rates unchanged. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dohodak_1.zip | 2026-11-15 |
| RCON: Read for arts. 1–3, 9–11, 16–24 and neighbors; gross base, payer/withholding, original rates. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20doprinosima_la.zip | 2026-11-15 |
| RCON 19: Read for complete arts. 1–3; unemployment rate 0.8% to 0.6%, effective 1 January 2020. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20Zak%20doprinosima_la.zip | 2026-11-15 |
| RCON 21: Read for complete arts. 1–5; health rate 12% to 10.2%, transition for wages earned earlier, effective 1 January 2022. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20doprinosima_la.zip | 2026-11-15 |
| RCON 22: Read for complete arts. 1–3; seconded workers' base in art. 16a, no change to the ordinary art. 22 rates. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20doprinosima%2C%20hp_la.zip | 2026-11-15 |
| RCON 22 B: Read for complete arts. 1–4; large-family benefit recipients in art. 16b, no change to the ordinary art. 22 rates. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zak%20o%20dopunama%20Zakona%20o%20doprinosima_la.zip | 2026-11-15 |
| RCON 23: Read for complete arts. 1–3; special categories in arts. 13 and 14, no change to the ordinary art. 22 rates. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zakon_o_dopunama_zakona_o_doprinosima_hp_la.zip | 2026-11-15 |
| RCON 25: Read for complete arts. 1–5; entrepreneur minimum base 70%, seasonal art. 16v, effective 1 January 2026; no change to the art. 22 rates. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20doprinosima.zip | 2026-11-15 |
| RCIT: Read for arts. 36–39, 44–47, 53–56 and neighbors; the 2015 original art. 44(2) 5% rate was superseded by 1/17. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon_o_porezu_na_dobit_8.zip | 2026-11-15 |
| RCIT 17: Read for amending arts. 12–22; art. 15 deletes art. 44(2), art. 16 amends art. 45, art. 19 covers treaty evidence. Full relevant operative neighbors. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20izmj%20i%20dop%20Zakona%20o%20porezu%20na%20dobit_la.zip | 2026-11-15 |
| RCIT 25: Read for complete arts. 1–18; the 2026 changes neither alter the art. 36 or 44 rates nor repeal the art. 54 prohibition; art. 52 document retention kept but automatic submission removed. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/la/Zak%20o%20izmj%20i%20dop%20Zak%20o%20porezu%20na%20dobit.zip | 2026-11-15 |
| BPIT: Read for arts. 2–12, 25 and neighbors. Unofficial consolidation stops at 24/20; 21/22 read separately. | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf | 2026-11-15 |
| BPIT 22: Read for complete amending arts. 1–4, including 1 August 2022 application. | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf | 2026-11-15 |
| BCIT: Read for arts. 20–21 and 28–31; the separate 38/22 amendment read in full, with no relevant rate or dividend change. | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf | 2026-11-15 |
| VAT: Read for arts. 23 and 57–58, full operative clauses and neighbors; original 50,000 threshold superseded by 80/23. | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-1-Zakon_o_PDV-b.pdf | 2026-11-15 |
| VAT 23: Read for complete 80/23 arts. 1–2; publication 24 November 2023, eighth-day commencement. | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf | 2026-11-15 |
| RPIT21A: Read for complete arts. 1–2; allowance 6,000 to 8,400 as an intermediate stage, then 12,000 under 119/21. Dependant amount separate. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20izmj%20Zakona%20o%20porezu%20na%20dohodak_la.zip | 2026-11-15 |
| RPIT22: Read for complete arts. 1–2; changes the prepared-food employee exemption, no change to arts. 4, 10 or 21–26. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat%20Zakon%20o%20izmj%20Zakona%20o%20porezu%20na%20dohodak%2C%20hp_la.zip | 2026-11-15 |
| RCON21A: Read for complete arts. 1–2; adds art. 10a ordinary minimum gross salary floor and part-time/multiple-payer rule. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zakon%20o%20dop%20Zakona%20o%20doprinosima_la.zip | 2026-11-15 |
| RCON24: Read for complete arts. 1–5; entrepreneur, profession, pension and supplementary classifications; art. 11 minimum of 80% scheduled but superseded by 114/25; art. 21 special pension exception. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zak_o_doprinosima_hp_la.zip | 2026-11-15 |
| RCIT19: Read for complete arts. 1–11; art. 37 special tax year, art. 46 interest investment wording; no change to arts. 36, 44 or 54. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/Zak%20izmj%20dop%20Zak%20porezu%20na%20dobit_la.zip | 2026-11-15 |
| RCIT24: Read for complete adopted Latin amending arts. 1–2. Changes art. 46 only, no change to arts. 36, 44 or 54. The earlier Ministry-hosted Cyrillic Gazette 48/24, physical p. 2, was read separately and is legally the same; retained as corroboration outside the PR. | https://www.narodnaskupstinars.net/sites/default/files/upload/dokumenti/akti/usvojeni_zakoni/lat_zakon_o_izmj_i_dop_zakona_o_porezu_na_dobit_hp_la.zip | 2026-11-15 |
| BCIT22: Read for complete arts. 1–4; art. 8 donations, art. 39a production condition, art. 43 implementation; no change to arts. 20 or 29. | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/06B38-22%20Zakon%20o%20izmjeni%20i%20dopunama%20Zakona%20o%20porezu%20na%20dobit.pdf | 2026-11-15 |
| RPITERR: Read for the entire PIT erratum and neighboring introduction, visually read from the rendered PDF, physical p. 1 / printed p. 45. Bad-font text unusable; manual exact quote retained. Changes only the art. 65 cross-reference from 64 to 59, not the art. 8 dividend point, rates or bases. | https://poreskaupravars.org/wp-content/uploads/2026/05/Ispravka-Zakona-o-porezu-na-dohodak-05-16.pdf | 2026-11-15 |

Not yet confirmed: BD contribution/insurance rates for the actual worker, so no BD salary illustration; entity-specific self-employed contribution cash amounts and applicable minimum/statistical bases, left to a separately sourced contribution computation; current operational RS election/withdrawal and annual-form mechanics; exact foreign-individual/treaty outcomes; full employer levies outside ordinary contributions; actual job/qualification eligibility and current operational steps for RS salary relief; current tax-procedure penalties/interest. These items are unusable pending operative confirmation. The earlier statutory 8% RS salary gap is closed by the 119/21 original; FBiH flat-rate eligibility is now sourced to current Rulebook 52 rather than silently omitted. The earlier blanket 20% margin shortcut, blanket foreign-owner withholding and unconditional 10% whole-tax conclusion are expressly qualified above.
