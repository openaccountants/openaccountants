---
name: lu-cross-border
description: "Luxembourg cross-border tax for individuals for tax year 2026: tax residence (fiscal domicile or habitual stay, with the six-month rule in § 14 StAnpG); non-residents taxed only on Luxembourg-source income (art. 156 LIR) and their tax classes (art. 157bis); the option to be taxed like a resident (art. 157ter: 90% of world income or under EUR 13,000 of foreign income, with up to 50 treaty-exempt working days counted); frontier workers from France, Belgium and Germany and the 34-day treaty thresholds; social security under Reg. 883/2004 (25%) and the telework framework agreement (under 50%); the impatriate regime (art. 115 no. 13b: 50% of pay exempt, capped at EUR 400,000, for up to eight years); outbound withholding; leaving Luxembourg. Trigger on: frontalier, télétravail 34 jours, non-résident Luxembourg, assimilation 157ter, impatrié, expat regime Luxembourg, moving to or leaving Luxembourg. Out of scope: luxembourg-income-tax, luxembourg-payroll, luxembourg-social-contributions, lu-c"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lu-cross-border"
  jurisdiction: "LU"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Luxembourg cross-border tax for individuals: residence, non-residents, frontier workers and impatriates (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Luxembourg.

What matters for 2026:

- **The scale did not change.** The LIR text in force on 1 January 2026 still carries the scale set by the law of 20 December 2024 (art. 118), first applied for 2025. Rates run from 0% up to 42%.
- **France: 34 days, confirmed by a new circular.** Circular L.G. – Conv. D.I. n° 61 of 24 June 2026 replaces the 2020 circular. It sets out how the 34-day threshold works for French residents from 2023 onwards, including the proration for part-time and part-year contracts.
- **Impatriate regime.** Art. 115 no. 13b, in its version from tax year 2025, exempts 50% of the total gross pay of a qualifying impatriate, on pay up to EUR 400,000. People who used the pre-2025 regime stay on it unless they choose the new one.

This skill sets out who is taxed where and on what. For the tax computation (scale, tax credits, deductions) use `luxembourg-income-tax`. For wage withholding cards use `luxembourg-payroll`. For contribution rates use `luxembourg-social-contributions`. For company residence, the company exit charge and dividend withholding exemptions use `lu-corporate-tax`.

## Who this applies to

**Resident individuals (art. 2 LIR).** A person is a resident taxpayer if they have their fiscal domicile or their habitual stay in Luxembourg. Residents are taxed on worldwide income.

- **Fiscal domicile (§ 13 StAnpG):** where the person has a dwelling in circumstances showing they will keep and use it.
- **Habitual stay (§ 14(1) StAnpG):** where the person stays in circumstances showing the stay is not merely temporary. Unlimited tax liability always arises when the stay in Luxembourg lasts **more than six months**, and it then also covers the first six months.
- The ACD adds that a person whose centre of vital interests is abroad is, in principle, a non-resident whatever their address, and that a residence permit does not by itself make someone tax resident.
- A treaty tie-breaker (usually art. 4 of the treaty) decides between two residences.

**Non-resident individuals (arts. 2 and 156 LIR).** A person with neither domicile nor habitual stay in Luxembourg is taxed only on Luxembourg-source income listed in art. 156. For most clients that means:

- employment income for work done in Luxembourg, or paid by a Luxembourg public body (art. 156 no. 4);
- pensions from a former Luxembourg job or paid by a Luxembourg fund (no. 5);
- business and professional profits from a Luxembourg permanent establishment or activity (nos. 1 and 3);
- rent from Luxembourg property (no. 7);
- dividends from Luxembourg companies (no. 6), usually settled by the 15% withholding;
- gains on Luxembourg property, and gains on a substantial shareholding (more than 10%, art. 100) in a Luxembourg company if sold within six months of purchase, or if the seller was resident for more than 15 years and left less than five years before the sale (no. 8). Shares in a corporate investment fund, a SICAR or an SPF are excluded (no. 8c).

**Part-year residents (art. 6(3)).** Income of the resident period and of the non-resident period are taxed separately.

**Frontier workers.** Residents of France, Belgium or Germany who work for a Luxembourg employer. They are non-residents taxed in Luxembourg on pay for days worked in Luxembourg, plus days covered by the treaty threshold (see below).

**Impatriates.** Employees seconded to, or hired from abroad by, a Luxembourg company who become Luxembourg residents (art. 115 no. 13b).

Out of scope: companies (see `lu-corporate-tax`), cross-border VAT (`luxembourg-vat-return`), public-sector pay under art. 18 or 19 of the treaties beyond a mention, and inheritance tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Residence by habitual stay | stay in Luxembourg of more than 6 months; liability then covers the first 6 months too | current | [§ 14(1) StAnpG, Legilux](https://legilux.public.lu/eli/etat/leg/loi/1934/10/16/n2/jo) |
| Income tax scale | 0% up to EUR 13,230, then 8% rising to 42% above EUR 234,870 (23 bands); taxable income rounded down to a multiple of EUR 50 | 2025 and 2026 | [LIR arts. 118 and 126](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Employment fund surcharge on income tax | 7%; 9% above adjusted taxable income of EUR 150,000 (classes 1 and 1a) or EUR 300,000 (class 2) | since 2013 | [ACD, Fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html) |
| Tax class of a married non-resident | class 1, unless both spouses ask for the 157ter rate on the withholding card | current | LIR art. 157bis(2) and (3) |
| Minimum rate on a non-resident's Luxembourg income other than employment and pensions | 15% (7.5% on certain extraordinary income) | current | LIR arts. 157(5) and 157bis(6) |
| Option to be taxed like a resident | at least 90% of world income taxable in Luxembourg, or foreign net income under EUR 13,000; treaty-exempt pay for up to 50 working days counts as Luxembourg income | current | LIR art. 157ter(1) and (2) |
| Belgian residents: extra assimilation route | more than 50% of the household's professional income taxable in Luxembourg | current | [ACD, Assimilation](https://impotsdirects.public.lu/fr/az/a/assimil.html) (Belgium treaty art. 24 § 4a) |
| Telework threshold, French residents | 34 days a year, prorated for part-time and part-year contracts | from 2023 | [Circular L.G. – Conv. D.I. n° 61 of 24 June 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-du-directeur-des-contributions-lg-conv-di-n-61-du-24-juin-2026.pdf) |
| Telework threshold, German residents | 34 days a year, not prorated; activity under 30 minutes in a place is ignored | from 2024 | [Circular L.G. – Conv. D.I. n° 71 of 18 March 2024](https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lg-conv-di-71-du-18-mars-2024.pdf) |
| Telework threshold, Belgian residents | 34 days a year, not prorated (24 days before 2022) | from 2022 | [ACD note, Belgium tolerance threshold](https://impotsdirects.public.lu/dam-assets/fr/conventions/conv/seuil-de-tolerance-b-03-2023.pdf) |
| Social security: substantial activity in the residence state | 25% of working time | current | [Guichet.lu, telework](https://guichet.public.lu/fr/citoyens/travail/conditions-travail/teletravail/teletravail.html) |
| Social security: telework framework agreement | telework from 25% to under 50% of working time, in the residence state only; A1 for up to 3 years | from 1 July 2023 | [CCSS, Accord-cadre sur le télétravail](https://ccss.public.lu/fr/employeurs/secteur-prive/activite-etranger/accord-teletravail.html) |
| Impatriate exemption | 50% of total gross annual pay, applied to pay up to EUR 400,000 (so at most EUR 200,000 exempt); the part of pay above EUR 400,000 is fully taxable | from 2025 | LIR art. 115 no. 13b |
| Impatriate minimum fixed pay | EUR 75,000 gross a year | from 2025 | LIR art. 115 no. 13b, condition 4 |
| Impatriate duration | the year of starting work plus up to 8 following tax years | from 2025 | LIR art. 115 no. 13b |
| Withholding on dividends | 15% of gross; 17.65% of net if the payer bears it | current | [LIR arts. 146 and 148](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf); exemptions in `lu-corporate-tax` |
| Withholding on directors' fees (tantièmes) | 20% of gross; 25% of the net paid if the payer bears it | current | LIR art. 152, Title 2(3) |
| Withholding on non-resident artists and professional sportspeople | 10% of receipts; 11.11% if the payer bears it | current | LIR art. 152, Title 1(2) |
| Withholding on ordinary interest and royalties paid abroad | none under domestic law | current | LIR art. 146 (see `lu-corporate-tax`) |
| Late filing surcharge | up to 10% of the tax | current | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Late payment interest | 0.6% a month | current | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |

## The taxable base

**Non-residents (arts. 156 to 157bis).**

1. Only income in art. 156 is taxed. Expenses count only if they have a direct economic link to that income (art. 157(1)).
2. Most special expenses are not deductible for a non-resident (art. 157(2)). Insurance and pension contributions under art. 110 nos. 1 to 3 remain deductible against income in art. 156 nos. 1 to 5, as does the EUR 480 lump sum of art. 113 for those with professional income.
3. **Wage withholding is final** for a non-resident employee (art. 157(3)), unless an assessment applies. A non-resident employed in Luxembourg continuously for at least nine months of the year falls under the same assessment triggers as a resident employee in art. 153(1) no. 1 (art. 157(4)); that alone does not force an assessment. An assessment also follows when the person asks for the 157ter option or the 157bis(3) rate. Once professional income is assessed, the assessment covers all the person's art. 156 income (art. 157bis(7)).
4. **Tax class (art. 157bis).** A married non-resident with professional income is put in class 1 (157bis(2)). If both spouses ask, the withholding card shows the rate they would have under 157ter, and an assessment then becomes compulsory (157bis(3)). Unmarried non-residents get class 1 or 1a under art. 119. Widowed, divorced or separated people in the cases of art. 119 no. 3 b and c get class 2 (157bis(4)). Child reductions and the extraordinary-charges allowance for children also apply (157bis(5)).
5. **Minimum 15% rate.** On Luxembourg income other than employment and pensions (for example rent from a Luxembourg flat), the rate cannot be below 15% (157bis(6)). The cap in 157bis(6a) limits the result.

**The 157ter option.** A non-resident can ask to be taxed at the rate that would apply if they were resident and taxed on world income. The tax still falls only on the Luxembourg income; foreign income only sets the rate (exemption with progression). It is open if either:

- at least **90%** of the person's world income (Luxembourg and foreign) is taxable in Luxembourg; or
- the person's net income not taxable in Luxembourg is **under EUR 13,000**.

For the 90% test, employment income that a treaty gives to another state counts as Luxembourg income, but only up to the pay for **50 working days** (157ter(2)). This is what lets a frontier worker who passes the 34-day threshold still opt. Married couples are taxed jointly on the Luxembourg income (class 2) unless they ask for individual taxation by 31 December of the following year. For a married couple it is enough that one spouse meets the 90% test or the EUR 13,000 test. The request is made on page 3 of the Form 100 return ("Assimilation du non-résident au résident"). The person must prove foreign income with documents (157ter(4)). Choosing it brings a compulsory assessment (157ter(3)).

**Frontier workers: which days are taxed where.** The general treaty rule (art. 14 France and Germany, art. 15 Belgium) is that pay is taxed where the work is physically done. Each treaty adds a tolerance: if the worker works in the residence state and/or a third state for no more than **34 days** in the year, all the pay stays taxable in Luxembourg.

- **France (protocol point 3, avenant of 7 November 2022; circular n° 61 of 24 June 2026).** Any day or part-day of work in France or a third state counts as a full day, and so do training days. Holidays, weekly rest days, public holidays when not required to work, sick days and force majeure do not count. The 34 days are prorated for part-time contracts (75% part-time gives 25 days) and for part-year contracts (start on 1 July gives 17 days), rounded down.
- **Germany (art. 14(1a), protocol of 6 July 2023, from 1 January 2024; circular n° 71).** 34 days, not prorated for part-time or part-year work. A day counts only if the person worked at least 30 minutes in that place. Paid on-call days at home count.
- **Belgium (art. 15 and final protocol para. 8, avenant of 31 August 2021, from 1 January 2022; ACD note).** 34 days, not prorated. Any part-day counts as a full day.

**Above the threshold.** If the count goes over 34, the tolerance is lost from day one. The residence state taxes the pay for every day worked there (and, under the French circular, for days in a third state, unless the third state's treaty gives it the right). Luxembourg keeps the pay for days worked in Luxembourg. The split is by working days; the French circular splits a half-day in each country 50/50, and the German agreement splits by minutes where the data exists. Sick pay and maternity pay paid under social security law are taxed by the state that pays them, not under the employment article.

**Impatriates (art. 115 no. 13b).** 50% of total gross annual pay is exempt. Benefits in kind and cash benefits already exempt under other numbers of art. 115 are left out of the base. The exemption applies to pay up to EUR 400,000; pay above that gets no exemption. All conditions must be met:

1. The person is resident in Luxembourg (domicile or habitual stay).
2. In the 5 tax years before starting work in Luxembourg, the person was not domiciled in Luxembourg, did not live within 150 km of the Luxembourg border, and was not taxed in Luxembourg on professional income.
3. At least 75% of working time is spent on the job that qualifies.
4. Fixed gross pay is at least EUR 75,000 a year.
5. The person does not replace a non-impatriate employee.
6. Secondees: at least five years in the group or five years of specialist experience; an employment link with the sending company; a right to return; and a secondment contract between the two companies.
7. Direct hires: deep specialisation in the sector. The hiring company must be a Luxembourg company or a company in another EEA state. Agency workers do not qualify.
8. Impatriates are no more than 30% of the Luxembourg company's staff. This does not apply to companies less than ten years old on 1 January.

The exemption runs for the assignment, up to the end of the eighth tax year after the year the person started work in Luxembourg. It stops as soon as a condition fails. The employer sends the ACD a list of beneficiaries by 31 January each year. A person on the pre-2025 regime stays on it unless they expressly choose the new version; that choice is irrevocable.

**Leaving Luxembourg.** Luxembourg has no exit tax on an individual's private assets. Two rules still reach a leaver:

- **Business assets (art. 38(1)(c)).** A sole trader or professional who moves their domicile or habitual stay abroad is treated as selling their business assets at estimated realisation value, except assets that stay attached to a Luxembourg permanent establishment at book value.
- **Substantial shareholdings (art. 156 no. 8b).** A gain on a holding of more than 10% in a Luxembourg company, made by someone who was resident for more than 15 years and left less than five years before the sale, is Luxembourg-source income. Most treaties give gains on shares to the residence state, so check the treaty first.

For a company moving its seat abroad, see `lu-corporate-tax` (art. 172 and art. 38).

## Deadlines and filing

- **Income tax return (Form 100):** by 31 December of the year after the tax year, for residents and non-residents alike ([ACD, délais de dépôt](https://impotsdirects.public.lu/fr/az/d/delais/depot.html)). For 2026 income: 31 December 2027.
- **157ter or 157bis(3) option:** made on the Form 100. A married couple's request to be taxed individually is due by 31 December of the year after the tax year (157ter(1)).
- **Withholding card rate:** a married non-resident couple can ask for the 157ter rate on the withholding card during the year (157bis(3)); this commits them to an assessment.
- **Impatriate list:** the employer files the list of impatriates with the ACD by 31 January each year (art. 115 no. 13b).
- **Telework declaration for social security:** the employer must declare cross-border telework to the CCSS through SECUline (procedure DEMDET) or the paper form. From 1 July 2024 a declaration can go back only three months. Any change (move, new percentage, new activity) needs a new declaration ([CCSS](https://ccss.public.lu/fr/employeurs/secteur-prive/activite-etranger/accord-teletravail.html)).
- **Proof of days:** the frontier worker carries the burden of proof. The French circular lists accepted evidence: employment contract or employer statement, timesheets, travel tickets, hotel bills, signed attendance lists, mission orders.

## Penalties and interest

The ACD rules apply to individuals in the same way as to companies ([ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html)):

- **Late filing:** a surcharge of up to 10% of the tax, set by the tax office.
- **Failure to file:** a penalty payment (astreinte) after a final deadline, and an estimated assessment (taxation d'office).
- **Late payment:** interest at 0.6% a month from the end of the month after the assessment notice is received. It also runs on the late filing surcharge and on unpaid advance payments.
- **Agreed payment plan:** 0.1% or 0.2% a month; a missed instalment brings back the full 0.6% rate.

## Cross-border points

- **Treaties.** Luxembourg's treaties follow the OECD model. The three frontier-worker treaties are France (20 March 2018, applicable from 2020), Germany (23 April 2012, amended by the protocol of 6 July 2023) and Belgium (17 September 1970, as amended). The list of treaties and their texts is on the [ACD treaty page](https://impotsdirects.public.lu/fr/conventions/luxembourg.html).
- **Public sector pay.** Pay from a Luxembourg public body falls under the government service article (art. 18 France and Germany, art. 19 Belgium), not the employment article. For a French resident with French but not Luxembourg nationality, the 34-day tolerance also applies to that pay from 2023 (circular n° 61). German residents in the Luxembourg public service also get the 34-day tolerance from 2024 (circular n° 71).
- **Social security is a separate test.** Tax days and social security percentages are counted under different rules. Under Reg. (EC) 883/2004, an employee who does at least 25% of their work in the residence state is insured there. The framework agreement (art. 16(1) of the regulation) keeps Luxembourg insurance for telework from 25% to under 50%, if all of these hold: employee (not self-employed), telework only in the residence state, no other usual activity outside Luxembourg, a link to the employer's IT system, and both states signed. France, Belgium and Germany signed with effect from 1 July 2023 ([Belgian social security, list of signatories](https://socialsecurity.belgium.be/fr/activites-internationales/teletravail-transfrontalier-dans-lue)). The CCSS issues an A1 for up to three years. Paid holidays are not working time for this test; sick days are.
- **Outbound withholding.** Dividends 15% (exemptions under art. 147 for qualifying parent companies; see `lu-corporate-tax`); directors' fees 20%; non-resident artists and sportspeople 10%; no withholding on ordinary interest or royalties. For a non-resident individual, withholding on dividends is final unless the dividend belongs to a Luxembourg business (art. 157(3)). A treaty can cut the rate; the treaty rate table is on the [ACD withholding page](https://impotsdirects.public.lu/fr/conventions/tx_ret.html).
- **Joint taxation with a non-resident spouse (art. 3 d).** A resident and a non-resident spouse can ask to be taxed jointly if the resident spouse earns at least 90% of the household's professional income in Luxembourg.

## Worked examples

### Example 1: French frontier worker, EUR 70,000, 40 days working from home in France

Facts: a single French resident works full time for a Luxembourg company all year 2026. Salary EUR 70,000. She works 220 days: 180 in Luxembourg and 40 at home in France. No days in third states. Her only income is the salary.

1. **Threshold test.** 40 days in France is above the 34-day limit for a full-time, full-year contract. The tolerance is lost from day one.
2. **Split.** Luxembourg taxes the pay for 180 days; France taxes the pay for 40 days. 70,000 x 180 / 220 = EUR 57,272.73 is taxed in Luxembourg; 70,000 x 40 / 220 = EUR 12,727.27 in France.
3. **157ter option.** She has no foreign income other than the French-taxed salary. For the 90% test, the 40 treaty-exempt days count as Luxembourg income because they are within the 50-day cap. Her ratio is 100%, so she can ask to be taxed like a resident. Without the option she stays in class 1 (art. 157bis(4)); her withholding is final unless her taxable income passes the art. 153(1) no. 1 assessment limit, which applies to her because she works in Luxembourg all year (art. 157(4)).
4. **Social security.** 40 / 220 = 18.18% of her working time is in France, below 25%. She stays insured in Luxembourg only, on the whole salary. The framework agreement is not needed.
5. **Payroll.** The employer has to split the withholding (the ACD intermittent or daily-scale method); see `luxembourg-payroll`. The French return reports the 40 days' pay; France gives the relief under its own rules (outside this skill).

```oa-check
name: French frontier worker, EUR 70,000, 180 Luxembourg days and 40 French days (2026)
inputs:
  salary: 70000
  days_total: 220
  days_lu: 180
  days_fr: 40
  threshold_fr: 34
  cap_157ter_days: 50
steps:
  - days_over_threshold: max(days_fr - threshold_fr, 0)
  - pay_taxed_in_lu: round(salary * days_lu / days_total, 2)
  - pay_taxed_in_fr: round(salary * days_fr / days_total, 2)
  - pay_counted_as_lu_for_157ter: pay_taxed_in_lu + round(salary * min(days_fr, cap_157ter_days) / days_total, 2)
  - share_157ter: round(pay_counted_as_lu_for_157ter / salary, 4)
  - share_of_time_in_france: round(days_fr / days_total, 4)
expected:
  days_over_threshold: 6
  pay_taxed_in_lu: 57272.73
  pay_taxed_in_fr: 12727.27
  pay_counted_as_lu_for_157ter: 70000.00
  share_157ter: 1.0000
  share_of_time_in_france: 0.1818
```

Edge cases: had she worked 30 days in France, all EUR 70,000 would stay taxable in Luxembourg. Had she started on 1 July, her threshold would be 17 days (34 x 6/12). A German resident with the same days would also lose the tolerance (34 days, not prorated), but a German part-year worker keeps the full 34 days.

### Example 2: impatriate hired from abroad on EUR 150,000

Facts: an engineer living in Spain is hired directly by a Luxembourg company and starts work on 1 January 2026. Fixed gross pay EUR 150,000. He moves to Luxembourg, is single with no children (class 1), and meets all the conditions of art. 115 no. 13b (no Luxembourg tax or home within 150 km of the border in 2021 to 2025, deep specialisation, impatriates under 30% of staff).

1. **Exempt part.** 50% of EUR 150,000 = EUR 75,000 (pay is below the EUR 400,000 cap).
2. **Taxable pay.** EUR 75,000.
3. **Tax on the scale (class 1, art. 118).** Up to EUR 54,090 the bands give EUR 8,859.60. The 39% band then applies to EUR 75,000 - 54,090 = 20,910, giving EUR 8,154.90. Total EUR 17,014.50.
4. **Employment fund surcharge.** 7% (adjusted taxable income not above EUR 150,000) = EUR 1,191.02. Total EUR 18,205.52.
5. **Without the regime**, the scale on EUR 150,000 gives EUR 46,590.00, plus 7% = EUR 49,851.30. The regime saves EUR 31,645.78.
6. **Period.** The exemption can run from 2026 to the end of 2034 (the year of starting work plus eight tax years), while the conditions hold.

The figures apply the scale to the taxable pay before employee social contributions, the expense lump sums and the tax credits. Those reduce the tax; take them from `luxembourg-payroll` and `luxembourg-income-tax`.

```oa-check
name: Impatriate, gross pay EUR 150,000, class 1, 2026 scale
inputs:
  gross_pay: 150000
  exemption_rate: 0.5
  exemption_cap: 400000
  surcharge_rate: 0.07
steps:
  - exempt_part: min(gross_pay, exemption_cap) * exemption_rate
  - taxable_pay: gross_pay - exempt_part
  - tax_to_54090: 2205 * (0.08 + 0.09 + 0.10 + 0.11 + 0.12) + 2295 * (0.14 + 0.16 + 0.18 + 0.20 + 0.22 + 0.24 + 0.26 + 0.28 + 0.30 + 0.32 + 0.34 + 0.36 + 0.38)
  - tax_scale: tax_to_54090 + (min(taxable_pay, 117450) - 54090) * 0.39
  - surcharge: round(tax_scale * surcharge_rate, 2)
  - total_tax: tax_scale + surcharge
  - tax_scale_without_regime: tax_to_54090 + (117450 - 54090) * 0.39 + (min(gross_pay, 176160) - 117450) * 0.40
  - total_without_regime: tax_scale_without_regime + round(tax_scale_without_regime * surcharge_rate, 2)
  - saving: total_without_regime - total_tax
expected:
  exempt_part: 75000
  taxable_pay: 75000
  tax_to_54090: 8859.60
  tax_scale: 17014.50
  surcharge: 1191.02
  total_tax: 18205.52
  tax_scale_without_regime: 46590.00
  total_without_regime: 49851.30
  saving: 31645.78
```

## Ask the client first

1. **Where do you live, and since when?** Where is your family home, and how many days do you spend in Luxembourg? (Residence and part-year split.)
2. **Frontier workers: how many days did you work outside Luxembourg in the year, in which countries, and why** (telework, training, missions)? Part-time or part-year contract? Any sick days or on-call days at home?
3. **What other income do you and your spouse or partner have, and where is it taxed?** (157ter 90% test and EUR 13,000 test; Belgian 50% household test.)
4. **Married or in a registered partnership?** Do you want joint or individual taxation?
5. **Impatriates: how were you recruited (secondment or direct hire), what is your fixed pay, where did you live and work in the last five years, and how many impatriates does the employer have?**
6. **Leaving: do you run a business or hold more than 10% of a Luxembourg company, and how long were you resident?**

## Sources

| Source | URL | Read on |
|---|---|---|
| LIR, consolidated text in force at 1 January 2026 (ACD, updated 8 May 2026): arts. 2, 3, 6, 38, 100, 113, 115 no. 13b, 118 to 121, 126, 146, 148, 152, 156, 157, 157bis, 157ter | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-10-23 |
| Steueranpassungsgesetz of 16 October 1934, §§ 13 and 14, Legilux | https://legilux.public.lu/eli/etat/leg/loi/1934/10/16/n2/jo | 2026-10-23 |
| ACD, Résident / non-résident | https://impotsdirects.public.lu/fr/az/r/resid_nonresid.html | 2026-10-23 |
| ACD, Séjour habituel | https://impotsdirects.public.lu/fr/az/s/sejour.html | 2026-10-23 |
| ACD, Assimilation fiscale des contribuables non résidents | https://impotsdirects.public.lu/fr/az/a/assimil.html | 2026-10-23 |
| ACD, Fonds pour l'emploi | https://impotsdirects.public.lu/fr/az/f/fond_empl.html | 2026-10-23 |
| ACD, treaties in force (France, Belgium, Germany entries) | https://impotsdirects.public.lu/fr/conventions/luxembourg.html | 2026-10-23 |
| Circular L.G. – Conv. D.I. n° 61 of 24 June 2026, France, 34 days (scanned; read by OCR) | https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-du-directeur-des-contributions-lg-conv-di-n-61-du-24-juin-2026.pdf | 2026-10-23 |
| Avenant to the France-Luxembourg treaty of 7 November 2022 (29 to 34 days) | https://impotsdirects.public.lu/dam-assets/fr/conventions/conv/avenant-a-la-convention-lu-fr-34-jours-et-fonction-publique-signe-7-novembre-2022.pdf | 2026-10-23 |
| Circular L.G. – Conv. D.I. n° 71 of 18 March 2024, Germany protocol of 6 July 2023 | https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lg-conv-di-71-du-18-mars-2024.pdf | 2026-10-23 |
| ACD note, Belgium tolerance threshold (34 days) | https://impotsdirects.public.lu/dam-assets/fr/conventions/conv/seuil-de-tolerance-b-03-2023.pdf | 2026-10-23 |
| ACD, Télétravail (withholding methods) | https://impotsdirects.public.lu/fr/az/t/teletravail.html | 2026-10-23 |
| CCSS, Accord-cadre sur le télétravail | https://ccss.public.lu/fr/employeurs/secteur-prive/activite-etranger/accord-teletravail.html | 2026-10-23 |
| Belgian federal social security, signatories of the telework framework agreement | https://socialsecurity.belgium.be/fr/activites-internationales/teletravail-transfrontalier-dans-lue | 2026-10-23 |
| Guichet.lu, Opter pour le télétravail (25% rule) | https://guichet.public.lu/fr/citoyens/travail/conditions-travail/teletravail/teletravail.html | 2026-10-23 |
| ACD, late filing surcharge, penalty payment and late interest | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-10-23 |
| ACD, filing deadlines | https://impotsdirects.public.lu/fr/az/d/delais/depot.html | 2026-10-23 |
| ACD, treaty withholding rates |https://impotsdirects.public.lu/fr/conventions/tx_ret.html | 2026-10-23 |
| ACD, laws passed in 2025 and 2026 | https://impotsdirects.public.lu/fr/legislation/legi26.html | 2026-10-23 |

Not yet confirmed: the text of the France and Belgium treaties themselves (the skill relies on the ACD circulars and notes, and the Belgian note dates from March 2023; no later Belgian change was listed on the ACD treaty page); whether France and Luxembourg agreed new conditions from 2025 under art. 3 of the 2022 avenant (the June 2026 circular still applies 34 days and no new avenant is listed); the text of the telework framework agreement itself and whether it was renewed or changed (read through the CCSS page and the Belgian signatory list); the deferral of the art. 38 charge for individuals moving within the EEA (no instalment rule was found in the LIR text read).

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lu-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lu-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
