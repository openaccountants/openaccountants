---
name: pl-cross-border
description: "Polish cross-border personal income tax (PIT) for tax year 2026. Covers individual residence (centre of vital interests or over 183 days, PIT Act art. 3), non-residents and Polish-source income (art. 3 ust. 2a-2b), the return relief for people moving to Poland (ulga na powrót, art. 21 ust. 1 pkt 152: four years, PLN 85,528 a year), withholding on payments to non-resident individuals (20% on fees, royalties and advisory services, 19% on dividends and interest, art. 29 and 30a), certificates of residence, IFT-1R and PIT-8AR, exemption with progression and credit (art. 27 ust. 8-9a), the abolition relief (art. 27g, PLN 1,360 cap), and individual exit tax (art. 30da-30df: 19% or 3% above PLN 4,000,000, PIT-NZ). Trigger on: moving to Poland, leaving Poland, non-resident, ulga na powrót, ulga abolicyjna, certyfikat rezydencji, IFT-1R, PIT-NZ, exit tax Poland. Out of scope: companies (pl-cit-corporate-tax), transfer pricing (pl-transfer-pricing), sole-trader computation (pl-income-tax), investment income (pl-capital-gains), ZUS (pl-zus-contributions)."
jurisdiction: PL
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Poland: cross-border tax for individuals (2026) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Poland.

**Which text of the law.** Article numbers are those of the PIT Act (ustawa z dnia 26 lipca 1991 r. o podatku dochodowym od osób fizycznych), consolidated text Dz.U. 2026 poz. 592, as amended by Dz.U. 2026 poz. 779, 846, 1079, 1098 and 1123. The Sejm's unified text, dated 2026-09-16 and read on 2026-10-23, includes all of these. Tax year: the calendar year. Currency: Polish złoty (PLN).

**Sibling skills. Link, do not repeat.**
- Companies: residence, withholding on payments by and to companies, the PLN 2,000,000 pay-and-refund rule, CFC and company exit tax: [pl-cit-corporate-tax](pl-cit-corporate-tax.md).
- Related-party pricing: [pl-transfer-pricing](pl-transfer-pricing.md).
- Sole traders (scale, flat 19%, ryczałt): [pl-income-tax](pl-income-tax.md). Investment income and the PIT-38: [pl-capital-gains](pl-capital-gains.md).
- Social contributions: [pl-zus-contributions](pl-zus-contributions.md). VAT on cross-border supplies: [pl-vat-return](pl-vat-return.md).

## Who this applies to

**Residents (art. 3 ust. 1 and 1a).** A person with a place of residence (miejsce zamieszkania) in Poland is taxed on worldwide income. A person has a place of residence in Poland if either:
1. their centre of personal or economic interests (centre of vital interests) is in Poland; or
2. they stay in Poland for more than 183 days in the tax year.

Either test is enough. Both are read subject to tax treaties (art. 4a), so a person resident in both countries under domestic law is placed by the treaty tie-breaker.

**Residence can change during the year.** The Ministry of Finance treats the year as split: up to the day of the change the person is taxed in Poland on worldwide income, and from the next day only on Polish-source income. The 183-day test counts days of physical presence in the calendar year, and any part of a day in Poland, including the day of arrival or departure, counts as a day ([MF tax explanations of 29 April 2021 on tax residence, sections 2.2 and 2.3](https://eureka.mf.gov.pl/informacje/podglad/482416)).

**Non-residents (art. 3 ust. 2a and 2b).** A person with no place of residence in Poland is taxed only on income earned in Poland. That includes, in particular, income from:
- work done in Poland under an employment or similar relationship, wherever the salary is paid;
- activity performed personally in Poland, wherever the fee is paid;
- a business carried on in Poland, including through a Polish permanent establishment;
- Polish real estate, and shares in companies at least 50% of whose assets are Polish real estate (real-estate-rich companies);
- securities admitted to trading on the Polish regulated market;
- payments made by Polish residents, companies and other entities, wherever the contract was signed or performed, where they are payments of the kind listed in art. 29 ust. 1 (art. 3 ust. 2b pkt 7 and ust. 2d);
- unrealised gains taxed by exit tax (art. 30da).

**Arriving.** A person who becomes resident may claim the return relief (ulga na powrót) for four years if they meet the conditions below.

**Leaving.** A person who stops being resident may owe exit tax on unrealised gains if the assets they take with them are worth more than PLN 4,000,000 (art. 30da and 30db).

**Out of scope.** Companies, partnerships taxed as companies, and family foundations: see [pl-cit-corporate-tax](pl-cit-corporate-tax.md). Diplomats are exempt on foreign income under art. 3 ust. 3. Social security coordination (which country's ZUS applies) is not covered; refer it.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Residence test | Centre of vital interests in Poland, or more than 183 days in Poland in the tax year | 2026 | [PIT Act art. 3 ust. 1a](https://api.sejm.gov.pl/eli/acts/DU/2026/592/text/U/D20260592Lj.pdf) |
| Tax scale (residents, and non-residents on scale income) | 12% minus PLN 3,600 up to PLN 120,000; PLN 10,800 plus 32% of the excess above PLN 120,000 | 2026 | PIT Act art. 27 ust. 1 |
| Return relief (ulga na powrót) | Exempt revenue up to PLN 85,528 a year, for four consecutive tax years starting with the year of the move or the next year | 2026 | PIT Act art. 21 ust. 1 pkt 152; [podatki.gov.pl, ulga na powrót](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-na-powrot-pit) |
| Shared cap with the young-person, 4+ family and working-senior reliefs | PLN 85,528 a year in total across art. 21 ust. 1 pkt 148 and 152-154 | 2026 | PIT Act art. 21 ust. 44 |
| Employee standard costs, one employer | PLN 250 a month, PLN 3,000 a year | 2026 | PIT Act art. 22 ust. 2 pkt 1 |
| Withholding on non-residents: personal-activity fees under art. 13 pkt 2 and 6-9 (arts, sport and teaching; board and supervisory seats; mandate and specific-task contracts; management contracts), royalties, know-how, equipment rental, interest outside art. 30a | 20% of revenue | 2026 | PIT Act art. 29 ust. 1 pkt 1 |
| Withholding on non-residents: advisory, accounting, market research, legal, advertising, management and control, data processing, recruitment, guarantees and similar services | 20% of revenue | 2026 | PIT Act art. 29 ust. 1 pkt 5 |
| Withholding on non-residents: entertainment and sports performers | 20% of revenue | 2026 | PIT Act art. 29 ust. 1 pkt 2 |
| Flat tax on dividends, interest on loans, bank deposits and securities | 19% | 2026 | PIT Act art. 30a ust. 1 pkt 1-4 |
| Payments to a related non-resident above PLN 2,000,000 in the payer's tax year (art. 29 ust. 1 pkt 1 and art. 30a ust. 1 pkt 1-5a) | Domestic rate withheld on the excess, ignoring treaty relief, unless the payer files a statement or holds an opinion | 2026 | PIT Act art. 41 ust. 12-15 |
| Validity of a certificate of residence with no stated period | 12 months from the date of issue | 2026 | PIT Act art. 41 ust. 9a |
| Abolition relief (ulga abolicyjna) cap | PLN 1,360, except for employment and certain service income earned outside the land territory of any state | 2026 | PIT Act art. 27g ust. 2 and 5; [podatki.gov.pl, ulga abolicyjna](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-abolicyjna-pit) |
| Exit tax threshold | Applies only if the market value of the assets moved exceeds PLN 4,000,000 (one limit for both spouses together) | 2026 | PIT Act art. 30db |
| Exit tax rate | 19% where the asset has a tax value; 3% where no tax value is set | 2026 | PIT Act art. 30da ust. 1 |
| Exit tax instalments | Up to 5 years, on application, for a move to an EU/EEA state with a recovery-assistance agreement | 2026 | PIT Act art. 30de |
| Employee social contributions withheld by the employer | Pension 9.76% (half of 19.52%), disability 1.5%, sickness 2.45%: 13.71% in total | 2026 | [Social Insurance System Act art. 16 and 22](https://api.sejm.gov.pl/eli/acts/DU/2026/199/text/U/D20260199Lj.pdf) |
| Annual cap on the pension and disability contribution base | PLN 282,600 | 2026 | [MRPiPS notice, M.P. 2025 poz. 1206](https://api.sejm.gov.pl/eli/acts/MP/2025/1206/text.pdf) |
| Late payment interest | 10.50% a year (200% of the NBP lombard rate of 4.25% plus 2 points, floor 8%) | from 5 March 2026 | Tax Ordinance art. 56 § 1; [MF notice, M.P. 2026 poz. 269](https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf); [NBP base rates](https://static.nbp.pl/dane/stopy/stopy_procentowe.xml) |

## The taxable base

**Return relief: who qualifies (art. 21 ust. 1 pkt 152 and ust. 43).** All of these must be met:
1. The person moved their place of residence to Poland after 31 December 2021 ([act of 29 October 2021, Dz.U. 2021 poz. 2105, art. 53](https://api.sejm.gov.pl/eli/acts/DU/2021/2105/text.pdf)) and, as a result, is a Polish resident.
2. They had no place of residence in Poland in the three calendar years before the year of the move, nor in that year up to the day before the move.
3. They hold Polish citizenship, a Karta Polaka, or citizenship of another EU/EEA state or Switzerland; or they lived without a break during that period in the EU/EEA, Switzerland, Australia, Chile, Israel, Japan, Canada, Mexico, New Zealand, South Korea, the UK or the USA; or they lived in Poland for at least five calendar years before that period.
4. They hold a certificate of residence or other evidence of their foreign tax residence for the period that matters.
5. They have not used the relief before.

**Return relief: what it covers.** Revenue from employment, mandate and specific-task contracts under art. 13 pkt 8 (with a business, with a property owner or manager for services to that property, or with an estate enterprise), maternity benefit, and business income taxed on the scale, at 19% flat, under IP Box or under the ryczałt on recorded revenue. Management contracts are not covered ([podatki.gov.pl](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-na-powrot-pit)). Revenue taxed at a flat rate under the PIT Act, or already exempt, does not count towards the PLN 85,528 (art. 21 ust. 39).

**How the relief works.**
- It exempts revenue, not income. Revenue is exempted in date order from the start of the year until the cap is used ([podatki.gov.pl](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-na-powrot-pit)).
- Employee standard costs stay deductible against the taxable part: the rule that costs of exempt revenue are not deductible (art. 23 ust. 1 pkt 31) does not apply to this relief (art. 23 ust. 10). Employment and art. 13 pkt 8 costs are capped at the taxable part of the revenue from that source (art. 22 ust. 3b).
- Social contributions whose base is the exempt revenue cannot be deducted (art. 26 ust. 1 pkt 2, closing words). Only the contributions on the taxable part are deducted.
- An employer applies the relief during the year only on the employee's signed statement, with the start and end year, or on a PIT-2 (part G). It then applies from the next month at the latest (art. 31a ust. 8-9). If it was not applied during the year, the person claims it in the annual return.

**Non-residents with Polish employment.** Salary for work done in Poland is Polish-source (art. 3 ust. 2b pkt 1). The employer withholds advances on the scale as for a resident; the treaty article on employment decides whether Poland may tax it. That payroll computation belongs in the PR domain, which has no skill yet.

**Non-residents with Polish fees, royalties and investment income.** The payer withholds a final flat tax on revenue, with no deduction for costs: 20% under art. 29 ust. 1, 19% under art. 30a ust. 1. A treaty rate or exemption applies only if the payer holds the recipient's certificate of residence (art. 29 ust. 2; art. 30a ust. 2). The payer must take due care when checking the conditions for a reduced rate or exemption, scaled to its size and to any relationship with the recipient (art. 41 ust. 4aa).

**EU/EEA residents can elect the scale (art. 29 ust. 4-5).** A non-resident with a certificate of residence from an EU/EEA state or Switzerland can ask, in an annual return, to have art. 29 ust. 1 revenue taxed on the scale. The 20% withheld is then treated as an advance. This works only where the treaty allows Poland to obtain tax information from that state.

**Residents with foreign income: two methods.**
- **Exemption with progression (art. 27 ust. 8).** Where a treaty exempts the foreign income, add it to the Polish income, compute the tax on the total on the scale, find the average rate, and apply that rate to the Polish income only.
- **Credit (art. 27 ust. 9 and 9a).** Where the treaty uses the credit method, or there is no treaty, add the foreign income and deduct the foreign tax paid. The deduction cannot exceed the Polish tax attributable to the foreign income.
- **Abolition relief (art. 27g).** A resident taxed under the credit method on foreign employment, personal-activity or business income (or certain copyright income) deducts the difference between the credit-method tax and the tax the exemption-with-progression method would give. The deduction is capped at PLN 1,360 (art. 27g ust. 2), except for work outside the land territory of any state (art. 27g ust. 5). It is not available for income from listed tax havens (art. 27g ust. 3). Claim it on PIT/O with the PIT-36, PIT-36L or PIT-28 ([podatki.gov.pl](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-abolicyjna-pit)).

**Exit tax (art. 30da).** On a change of residence that ends Poland's right to tax a gain, the excess of market value over tax value of the assets is taxed. For assets not used in a business, only "personal assets" are caught: partnership interests, shares, securities, derivatives and fund units. They are caught only if the person was resident in Poland for at least five of the ten years before the change (art. 30da ust. 3). Assets that stay attached to a Polish permanent establishment are not caught (art. 30da ust. 5). A person who becomes resident again within 5 years of the end of the year of departure can claim the tax back (art. 30df ust. 2).

## Deadlines and filing

| What | Who | Deadline | Source |
|---|---|---|---|
| Annual PIT return (PIT-37, PIT-36, PIT-36L, PIT-28) | Resident or non-resident taxpayer | 15 February to 30 April 2027 for 2026 | PIT Act art. 45 ust. 1 |
| Return relief shown in the return | Taxpayer | Part D of PIT-37, PIT-36 or PIT-36L; part C of PIT-28 | [podatki.gov.pl, ulga na powrót](https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-na-powrot-pit) |
| Payment of tax withheld from non-residents | Payer (company or business) | By the 20th of the month after the month of withholding | PIT Act art. 42 ust. 1 |
| PIT-8AR annual return of flat-rate tax withheld (filed electronically, art. 45ba; so is the IFT-1R) | Payer | End of January 2027 | PIT Act art. 42 ust. 1a; [podatki.gov.pl, PIT forms](https://www.podatki.gov.pl/podatki-firmowe/pit/formularze-pit) |
| IFT-1R information on income of a non-resident individual | Payer, to the taxpayer and to the tax office for foreign persons; also where a treaty means nothing was withheld | End of February 2027; within 14 days of the taxpayer's written request | PIT Act art. 42 ust. 2 pkt 2, 4 and 6 |
| PIT-11 for revenue covered by the return relief | Employer | With the usual PIT-11 | PIT Act art. 42 ust. 5 |
| PIT-NZ exit tax return and payment | Taxpayer | By the 7th of the month after the month in which the assets moved pass PLN 4,000,000 | PIT Act art. 30da ust. 14; [podatki.gov.pl, PIT forms](https://www.podatki.gov.pl/podatki-firmowe/pit/formularze-pit) |

## Penalties and interest

**Late payment interest (Tax Ordinance art. 56).** Unpaid tax carries interest at 200% of the NBP lombard rate plus 2 points, with a floor of 8%. From 5 March 2026 that is 10.50% a year ([M.P. 2026 poz. 269](https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf)). The lombard rate was still 4.25% on 2026-10-23 ([NBP](https://static.nbp.pl/dane/stopy/stopy_procentowe.xml)).

**Payer liability (Tax Ordinance art. 30 § 1 and 3).** A payer that fails to withhold, or withholds but does not pay over, is liable for the tax with all its assets. If a certificate of residence went out of date because the taxpayer moved and did not supply a new one, the taxpayer bears that liability instead (PIT Act art. 41 ust. 9b-9c).

**Return relief claimed wrongly.** Where the employer under-withheld because it applied the employee's statement, the usual protection of employees from the employer's under-withholding is switched off (PIT Act art. 31a ust. 10, disapplying Tax Ordinance art. 26a § 2), so the tax office can hold the employee liable for the tax (Tax Ordinance art. 30 § 5). The statement is made under criminal liability for false statements (art. 31a ust. 9).

**Tax withheld wrongly.** A taxpayer who disputes the tax a payer withheld can apply to the tax office for a declaration of overpayment (Tax Ordinance art. 75 § 1).

Fiscal Penal Code offences (non-filing, false returns, payer failures) are summarised in [pl-cit-corporate-tax](pl-cit-corporate-tax.md); refer those cases to a Polish tax adviser.

## Cross-border points

- **Certificates of residence.** A certificate with no period of validity is accepted for 12 months from issue (art. 41 ust. 9a). A copy is enough unless it raises reasonable doubt (art. 41 ust. 9e). If the person changes residence within the 12 months, they must supply a new certificate at once (art. 41 ust. 9b).
- **Treaty example: Germany.** Under the Poland-Germany treaty, income of a German resident from independent professional or other self-employed activity is taxable only in Germany, unless the person has a fixed base regularly available in Poland. If they do, Poland may tax only the income attributable to it ([Treaty art. 14(1), Dz.U. 2005 nr 12 poz. 90](https://api.sejm.gov.pl/eli/acts/DU/2005/90/text.pdf)). Each treaty must be read on its own; this skill does not list treaty rates.
- **Pay-and-refund for related parties.** Above PLN 2,000,000 a year to the same related non-resident individual, art. 41 ust. 12 applies in PIT the same way art. 26(2e) applies in CIT. See [pl-cit-corporate-tax](pl-cit-corporate-tax.md) for the statement and opinion routes.
- **Payments by and to companies.** Withholding when the recipient is a company, CFC rules and company exit tax are in [pl-cit-corporate-tax](pl-cit-corporate-tax.md). Related-party documentation is in [pl-transfer-pricing](pl-transfer-pricing.md).
- **Social security.** The return relief does not reduce ZUS. Which country's social security applies to a cross-border worker is decided by EU coordination rules or a bilateral agreement, not by the PIT Act.

## Worked examples

### Example 1: a returning Pole uses the return relief in 2026

Facts (invented): Anna, a Polish citizen, lived and worked in Ireland from 2019. She held Irish tax residence certificates for 2022 to 2025. She moved back to Warsaw on 15 September 2025 and chose to start the relief on 1 January 2026, so her relief years are 2026 to 2029. In 2026 she works for one Polish employer for the full year at PLN 12,500 a month, PLN 150,000 in total. She has no other income. She gave her employer the statement in December 2025. Social contributions are withheld at 13.71%; her base stays below the PLN 282,600 cap.

Walk-through:
1. Exempt revenue: the first PLN 85,528 of 2026 salary (January to June in full, and PLN 10,528 of July).
2. Taxable revenue: 150,000 - 85,528 = 64,472.
3. Standard costs: 250 x 12 = 3,000. These stay deductible because art. 23 ust. 10 switches off the rule against costs of exempt revenue, and they are below the cap of the taxable revenue of 64,472 (art. 22 ust. 3b).
4. Social contributions withheld for the year: 150,000 x 13.71% = 20,565. Only those on the taxable revenue are deductible: 64,472 x 13.71% = 8,839.11.
5. Tax base: 64,472 - 3,000 - 8,839.11 = 52,632.89, rounded to PLN 52,633 (Tax Ordinance art. 63).
6. Tax on the scale: 52,633 x 12% - 3,600 = 2,715.96, rounded to PLN 2,716.
7. Without the relief: base 150,000 - 3,000 - 20,565 = 126,435. Tax 10,800 + (126,435 - 120,000) x 32% = 12,859.20, rounded to PLN 12,859.
8. The relief saves PLN 10,143 of PIT in 2026. The 9% health contribution is not deductible under the scale and is not affected.

```oa-check
name: Anna, 2026, return relief on PLN 150,000 salary
inputs:
  salary: 150000
  relief_cap: 85528
  monthly_costs: 250
  months: 12
  scale_threshold: 120000
  reducing_amount: 3600
  tax_at_threshold: 10800
steps:
  - exempt: min(salary, relief_cap)
  - taxable_revenue: salary - exempt
  - costs: monthly_costs * months
  - zus_total: salary * 0.1371
  - zus_deductible: taxable_revenue * 0.1371
  - base: round(taxable_revenue - costs - zus_deductible)
  - tax: max(round(base * 0.12 - reducing_amount), 0)
  - base_no_relief: round(salary - costs - zus_total)
  - tax_no_relief: round(tax_at_threshold + (base_no_relief - scale_threshold) * 0.32)
  - saving: tax_no_relief - tax
expected:
  exempt: 85528
  taxable_revenue: 64472
  zus_total: 20565
  zus_deductible: 8839.11
  base: 52633
  tax: 2716
  base_no_relief: 126435
  tax_no_relief: 12859
  saving: 10143
```

### Example 2: a German consultant paid PLN 50,000 by a Polish company

Facts (invented): Jonas lives in Berlin and is a German tax resident. He runs a one-person advisory business there. In May 2026 a Polish sp. z o.o. pays him PLN 50,000 for management advice. He spent eight days in Poland on the job and has no office or other fixed base in Poland. He is not related to the company.

Walk-through:
1. The fee is Polish-source: it is paid by a Polish company (art. 3 ust. 2b pkt 7) and is an advisory service listed in art. 29 ust. 1 pkt 5.
2. **No certificate of residence.** The company must withhold 20% of revenue, with no costs: 50,000 x 20% = 10,000. Jonas receives 40,000. The company pays the 10,000 to its tax office by 22 June 2026, reports it on the PIT-8AR by 1 February 2027 and sends Jonas and the tax office for foreign persons an IFT-1R by 1 March 2027. Each statutory day (20 June, 31 January, 28 February) falls on a weekend, so the deadline moves to the next working day (Tax Ordinance art. 12 § 5).
3. **With a German certificate of residence**, held by the company before payment and checked with due care: under art. 14(1) of the Poland-Germany treaty, the fee is taxable only in Germany because Jonas has no fixed base in Poland. The company withholds nothing and pays Jonas 50,000. It still sends the IFT-1R (art. 42 ust. 6).
4. If the company withheld 10,000 because the certificate arrived late, Jonas can apply to the Polish tax office for a declaration of overpayment (Tax Ordinance art. 75 § 1).

```oa-check
name: Jonas, 2026, PLN 50,000 advisory fee with and without a certificate of residence
inputs:
  fee: 50000
  treaty_rate_percent: 0
steps:
  - wht_domestic: fee * 0.20
  - net_domestic: fee - wht_domestic
  - wht_treaty: fee * treaty_rate_percent / 100
  - net_treaty: fee - wht_treaty
  - cost_of_missing_certificate: wht_domestic - wht_treaty
expected:
  wht_domestic: 10000
  net_domestic: 40000
  wht_treaty: 0
  net_treaty: 50000
  cost_of_missing_certificate: 10000
```

## Ask the client first

1. **Residence history.** Where did the person live, with what home, family and work ties, in each of the last four years? What is the exact date of the move? Do they hold certificates of residence for those years?
2. **Return relief start year.** Has the relief been used before, in whole or in part? Will it start in the year of the move or the next year? Has the employer received the statement?
3. **Other reliefs.** Does the person also use the young-person, 4+ family or working-senior relief? The PLN 85,528 cap is shared.
4. **Type of income.** For each Polish payment to a non-resident: is it a salary, a fee for personal activity, an advisory service, a royalty, a dividend or interest? Is the payer related to the recipient? Where is the work physically done, and is there an office or fixed base in Poland?
5. **Leaving Poland.** Market value and tax value of shares, partnership interests, securities and fund units held on the day before departure. Was the person resident in Poland for five of the last ten years? Where are they moving to?
6. **Foreign income of a resident.** Which country, which treaty article, which method (exemption with progression or credit), and how much foreign tax was paid?

## Sources

| Source | URL | Read on |
|---|---|---|
| PIT Act, consolidated text Dz.U. 2026 poz. 592, ELI record (later amendments 779, 846, 1079) | https://api.sejm.gov.pl/eli/acts/DU/2026/592 | 2026-10-23 |
| PIT Act, Sejm unified text incl. Dz.U. 2026 poz. 592, 779, 846, 1079, 1098, 1123 (arts. 3, 4a, 13, 21 ust. 1 pkt 152 and ust. 39, 43, 44, 22 ust. 2 and 3b, 23 ust. 1 pkt 31 and ust. 10, 26, 27, 27g, 29, 30a, 30da-30df, 31a, 41, 42, 45, 45ba) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text/U/D20260592Lj.pdf | 2026-10-23 |
| Social Insurance System Act, Sejm unified text of Dz.U. 2026 poz. 199 (arts. 16, 22) | https://api.sejm.gov.pl/eli/acts/DU/2026/199/text/U/D20260199Lj.pdf | 2026-10-23 |
| MRPiPS notice on the 2026 annual contribution cap, M.P. 2025 poz. 1206 | https://api.sejm.gov.pl/eli/acts/MP/2025/1206/text.pdf | 2026-10-23 |
| Tax Ordinance, Sejm unified text of Dz.U. 2026 poz. 622 (arts. 12, 26a, 30, 56, 63, 75) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text/U/D20260622Lj.pdf | 2026-10-23 |
| MF notice on late payment interest, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-23 |
| NBP base rates (lombard 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe.xml | 2026-10-23 |
| Poland-Germany double tax treaty, Dz.U. 2005 nr 12 poz. 90 (art. 14) | https://api.sejm.gov.pl/eli/acts/DU/2005/90/text.pdf | 2026-10-23 |
| Act of 29 October 2021 amending the PIT Act (Polski Ład), Dz.U. 2021 poz. 2105, art. 53 (return relief only for moves after 31 December 2021) | https://api.sejm.gov.pl/eli/acts/DU/2021/2105/text.pdf | 2026-10-23 |
| Ministry of Finance tax explanations of 29 April 2021 on tax residence of individuals (sections 2.2 and 2.3), in the MF Eureka system | https://eureka.mf.gov.pl/informacje/podglad/482416 | 2026-10-23 |
| podatki.gov.pl, ulga na powrót (updated 6 October 2026) | https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-na-powrot-pit | 2026-10-23 |
| podatki.gov.pl, ulga abolicyjna (updated 13 October 2026) | https://www.podatki.gov.pl/ulgi-i-odliczenia/ulga-abolicyjna-pit | 2026-10-23 |
| podatki.gov.pl, deduction of social contributions (contributions on exempt revenue not deductible) | https://www.podatki.gov.pl/ulgi-i-odliczenia/odliczenie-skladek-na-ubezpieczenie-spoleczne-pit | 2026-10-23 |
| podatki.gov.pl, PIT forms for businesses (PIT-NZ (2), PIT-8AR (14), IFT-1R (18)) | https://www.podatki.gov.pl/podatki-firmowe/pit/formularze-pit | 2026-10-23 |

The ISAP pages (isap.sejm.gov.pl) serve a browser check to scripted requests, so the law texts were read from the Sejm's own ELI service (api.sejm.gov.pl), which serves the same documents.

Not yet confirmed: whether, in the year of arrival, a person who passes 183 days is resident for the whole year or only from arrival (the MF explanations give a split-year example only for departure under the centre-of-interests test); how an employer spreads standard costs over months in which all salary is exempt when it computes monthly advances (the annual tax in Example 1 does not depend on it); treaty rates for countries other than Germany.
