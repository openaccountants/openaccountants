---
name: fr-cross-border
description: "France cross-border income tax for individuals, tax year 2026: residence tests (CGI art. 4 A, 4 B), non-residents with French income (the 20%/30% minimum rate of art. 197 A and the average-rate option), withholding on salaries (art. 182 A) and on fees and royalties (art. 182 B), the levy on property gains (art. 244 bis A), social levies for non-residents (17.2%, 18.6%, or 7.5% when covered by another EU scheme), the impatriate regime (art. 155 B), treaty credits, A1 postings and penalties. Trigger on: non-résident France, impatrié, article 155 B, prime d'impatriation, taux minimum 20 %, taux moyen, retenue à la source 182 A, 244 bis A, prélèvement de solidarité 7,5 %, crédit d'impôt conventionnel. Out of scope: leaving France and exit tax (leaving-france-exit-tax), company outbound withholding and CFC (fr-corporate-tax), the resident computation (fr-personal-income-tax)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fr-cross-border"
  jurisdiction: "FR"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# France: cross-border individuals (non-residents, impatriates, treaty relief) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not file, pay or take a tax position on it without review by a qualified professional in France.

**Tax year.** This skill covers income of 2026, declared in spring 2027, and French-source payments made during 2026. The Code général des impôts (CGI) and Code de la sécurité sociale (CSS) articles were read on Légifrance on 23 October 2026, in the version in force that day. The income tax scale used below is the one in CGI art. 197 as amended by the 2026 finance law (loi n° 2026-103 du 19 février 2026, art. 4). That law applies it to the tax due for 2025 and the following years (art. 4, II, A), so it is the scale for 2026 income unless the 2027 finance law changes it. The 2027 finance law did not exist on 23 October 2026. Use the art. 197 scale in force when the 2026 return is computed.

**Sibling skills.** Leaving France, the exit tax (art. 167 bis), IFI and succession reach are in `leaving-france-exit-tax`. Outbound withholding paid by companies on dividends, interest and royalties, branch tax and CFC rules are in `fr-corporate-tax`. The resident computation (household shares, décote, reductions and credits, the 10% salary deduction) is in `fr-personal-income-tax`. Rental income rules (micro-foncier, régime réel, LMNP) are in `fr-rental-income`. Securities gains and the flat tax for residents are in `fr-capital-gains`. Payroll contributions on an impatriate's pay are in `france-payroll`. This skill does not repeat them.

## Who this applies to

**Residence (CGI art. 4 A and 4 B).** A person with a tax domicile in France is taxed on worldwide income. A person whose tax domicile is outside France is taxed only on French-source income (art. 4 A). A person has a French tax domicile if any one of these is true (art. 4 B, 1):

- **a. Foyer or main stay.** Their home (foyer) or the place of their main stay is in France.
- **b. Professional activity.** They carry on a professional activity in France, employed or not, unless they show it is only accessory. Directors of companies with their seat in France and annual turnover above EUR 250 million are treated as working mainly in France unless they prove otherwise. Turnover of controlled companies (Code de commerce art. L. 233-16) is added.
- **c. Centre of economic interests.** The centre of their economic interests is in France.

One test is enough. A treaty overrides them: a person who meets a French test but is not a resident of France under a double tax treaty is not French-domiciled (art. 4 B, 1, last paragraph). French State and local-government agents posted abroad who pay no personal tax on all their income there stay French-domiciled (art. 4 B, 2).

**Who this skill is for.**

- Non-residents with French-source income: French salaries, fees, royalties, rents, property gains, gains on large stakes in French companies.
- People arriving to work in France who may use the impatriate regime (art. 155 B).
- French residents with foreign income who need the treaty credit mechanics.

**What counts as French-source income (art. 164 B).** Income from property in France; income from French securities and capital placed in France; income from businesses in France; income from activities, employed or self-employed, carried on in France; gains on French property and on shares of property-rich companies; gains on shares of French companies where the seller's stake falls under art. 164 B, I, f; payments for artistic or sporting services supplied or used in France. Where the payer is domiciled or established in France, pensions, royalties and payments for services of any kind supplied or used in France are also French-source (art. 164 B, II).

**How the base is computed (art. 164 A).** French-source income of a non-resident is computed under the same rules as for residents, but no charge deductible from global income can be deducted.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Income tax scale, per share: 0% to EUR 11,600; 11% to EUR 29,579; 30% to EUR 84,577; 41% to EUR 181,917; 45% above | as listed | Tax due for 2025 and later years, until amended | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636 |
| Non-resident minimum rate, up to the top of the second band (EUR 29,579) | 20% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985917 |
| Non-resident minimum rate, above that limit | 30% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985917 |
| Minimum rates for income sourced in the overseas departments | 14.4% and 20% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985917 |
| Salary and pension withholding for non-residents (art. 182 A), annual tariff: 0% to EUR 17,275 | 0% | From 1 Jul 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628 |
| Same, from EUR 17,275 to EUR 50,112 | 12% | From 1 Jul 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628 |
| Same, above EUR 50,112 | 20% | From 1 Jul 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628 |
| Same, overseas departments | 8% and 14.4% | From 1 Jul 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628 |
| Withholding on fees, royalties and services paid to a non-resident without a permanent base (art. 182 B) | art. 219 standard rate (25%, see `fr-corporate-tax`) | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 |
| Art. 182 B, sporting services | 15% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 |
| Art. 182 B, cost allowance for EU or EEA companies | 10% of the gross amount | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 |
| Art. 182 B and 182 A bis, payments other than salaries to a person in a non-cooperative state (unless the payer proves the payments are genuine and not located there for tax reasons) | 75%, final and not refundable | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 |
| Artists' withholding (art. 182 A bis), after a 10% allowance | 15% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042907688 |
| Levy on French property gains, individuals (art. 244 bis A) | 19% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806274 |
| Same, companies | art. 219 standard rate | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806274 |
| Holding-period allowance on property gains (income tax) | 6% a year from year 6 to 21; 4% for year 22 | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047970756 |
| Surtax on taxable property gains above EUR 50,000 (art. 1609 nonies G), also due by non-residents; not on building land | 2% to 6% of the whole gain, with smoothing | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806252 |
| Levy on gains from stakes above 25% in a French company (art. 244 bis B), individuals | 12.8% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051200525 |
| Flat income tax rate on investment income (art. 200 A) | 12.8% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896 |
| Impatriate: optional flat exemption of pay instead of the actual premium | 30% of pay | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985788 |
| Impatriate: exemption of qualifying foreign passive income | 50% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985788 |
| Impatriate: caps on the pay exemption | 50% of total pay, or foreign-days part limited to 20% of taxable pay | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985788 |
| Impatriate: duration | Until 31 Dec of the 8th year after the start; not French-domiciled in the 5 prior calendar years | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985788 |
| CSG on revenus fonciers (unfurnished rents) and on property gains (CSS art. L136-8, IV) | 9.2% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623 |
| CSG on other patrimony income, including furnished letting income (CSS art. L136-8, I, 2°) | 10.6% | Income of 2025 onward (patrimony contribution, art. L136-6); payments from 1 Jan 2026 (investment income taxed at source, art. L136-7) | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053226452 |
| CRDS | 0.5% | 2026 | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000190291 |
| Solidarity levy (prélèvement de solidarité, CGI art. 235 ter) | 7.5% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037949145 |
| Total social levies: unfurnished rents and property gains / other patrimony income | 17.2% / 18.6% | 2026 | Sum of the three rows above |
| Holding-period allowance on property gains for the social levies | 1.65% a year from year 6 to 21; 1.60% for year 22; 9% a year from year 23 (exempt after 30 years) | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053584839 |
| Person covered for health by a scheme under Regulation 883/2004 (EU, EEA, Switzerland) and not by a French scheme | 7.5% only (no CSG or CRDS) | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218166 |
| Late filing surcharge (art. 1728) | 10%; 40% after formal notice; 80% for hidden activity | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 |
| Inaccuracy surcharge (art. 1729) | 40% deliberate; 80% abuse of law or fraud | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 |
| Late payment interest (art. 1727) | 0.20% a month | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |
| A1 posting within the EU | Home scheme kept if the posting is expected to last 24 months or less | 2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731 |

## The taxable base

**Non-residents: the minimum rate and the average-rate option (art. 197 A).**

1. Compute each French-source income under the resident rules, with no deduction from global income (art. 164 A). Rents follow `fr-rental-income`; salaries follow `fr-personal-income-tax`.
2. Apply the scale with the household shares (art. 197, I, 1 and 2 only). The décote (art. 197, I, 4) is not among the rules art. 197 A applies.
3. The tax cannot be lower than 20% of net taxable income up to EUR 29,579 plus 30% of the part above (14.4% and 20% for income from the overseas departments).
4. **Average-rate option.** If the person shows that the French tax rate on their total French and foreign income would be lower than these minimums, that rate applies to the French income. Compute the French tax on worldwide income under French rules, divide by worldwide income, and apply the result to French-source income. Residents of an EU state, or of a state with an administrative-assistance or recovery-assistance convention, may attach a sworn statement while they gather the proof. For this worldwide-rate computation only, maintenance payments (art. 156, II, 2°) are deductible, if they are taxable in France in the hands of the recipient and the deduction does not reduce the tax due in the state of residence (art. 197 A, b).
5. Withholding under art. 182 A, 182 A bis and 182 B is set against this tax (art. 182 A, V; art. 182 A bis, IV; art. 182 B, II). For art. 182 B withholding, art. 182 B, II adds that any excess is refunded on request. The art. 182 B and 182 A bis rates of 75% are final and not refundable.

**Salaries and pensions of non-residents (art. 182 A).** The French payer withholds on the net amount (computed under income tax rules, without the real-expenses option). Use the annual tariff in the table. Divide the band limits by 4, 12, 52 or 312 for quarterly, monthly, weekly or daily pay. These amounts are outside the general withholding scheme (prélèvement à la source): art. 204 D excludes income subject to art. 182 A, 182 A bis, 182 A ter and 182 B. The withholding is not final: it is credited against the art. 197 A tax on the annual return.

**Fees, royalties and services (art. 182 B).** A payer carrying on an activity in France withholds on gross payments to a person with no permanent professional base in France for: professional services of the kind in art. 92 done in France; royalties for inventions, copyright and industrial property; services of any kind supplied or used in France; sporting services. A treaty often removes or lowers this withholding. Companies paying abroad: see `fr-corporate-tax`.

**Property gains of non-residents (art. 244 bis A).** The gain is computed under the resident rules of art. 150 U to 150 VE, including the holding-period allowance (6% a year from year 6 to year 21, then 4% for year 22, so no income tax after 22 years). Individuals pay 19%. The art. 1609 nonies G surtax applies when the taxable gain exceeds EUR 50,000 (not on building land). The former main home is exempt if sold by 31 December of the year after the move abroad, to an EU state or a state with both assistance conventions, and not let or lent in between. A person who used the art. 150 U, II, 2° exemption cannot use this one, and the reverse. The levy discharges the income tax on that gain.

**Large stakes (art. 244 bis B).** Gains on shares of a French company subject to corporate tax, where the seller's family group held more than 25% of the profits at any time in the last five years, bear a 12.8% levy for individuals (75% in a non-cooperative state, whatever the stake). The levy discharges the income tax. An individual may claim back, by a formal claim, the part of the levy above the extra art. 197 A tax that the gain would cause if added to their other French income of the year (art. 244 bis B, second paragraph).

**Social levies on non-residents.** A non-resident pays social levies only on income from French real property (CSS art. L136-6, I bis, which refers to CGI art. 164 B, I, a) and on French property gains taxed under art. 244 bis A (CSS art. L136-7, I bis). French dividends, interest and gains on securities of a non-resident bear no social levies: art. L136-6, I and art. L136-7, I reach only persons domiciled in France (confirmed by service-public.gouv.fr, page F2329, checked 30 June 2026). For 2026:

- Unfurnished rents (revenus fonciers): CSG 9.2% (CSS art. L136-8, IV, 1°), CRDS 0.5%, solidarity levy 7.5%. Total 17.2%.
- Furnished letting income (location meublée non professionnelle): it is not in the 9.2% list of art. L136-8, IV, so CSG is 10.6%. Total 18.6%.
- Property gains: total 17.2% (service-public.gouv.fr, page F2329). The social levies use their own holding-period allowance (CSS art. L136-7, VI, 2): 1.65% a year from year 6 to 21, 1.60% for year 22 and 9% a year from year 23, so the gain is free of social levies after 30 years, against 22 years for income tax.
- A person covered for health insurance under Regulation (EC) 883/2004 (another EU or EEA state, or Switzerland), and not by a French compulsory scheme, owes no CSG or CRDS (CSS art. L136-6, I ter; art. L136-7, I ter). The 7.5% solidarity levy still applies, because CGI art. 235 ter excludes the I ter relief.

The 10.6% rate (LFSS 2026, loi n° 2025-1403, art. 12) applies to the patrimony contribution of art. L136-6 from the taxation of 2025 income, and to investment income taxed at source under art. L136-7 from 1 January 2026 (art. 12, II).

**The impatriate regime (art. 155 B).** It applies to employees and certain company officers called from abroad to work in a company established in France for a limited period. Conditions:

- Not French tax-domiciled in the five calendar years before the year they took up the post.
- French-domiciled under art. 4 B, 1, a or b (home or main stay, or main professional activity).
- The regime runs until 31 December of the eighth calendar year after the year they took up the post. It survives a change of job inside the same company or a group company in France (control under Code de commerce art. L. 233-3).

The reliefs:

1. **The premium.** The parts of pay directly linked to the move abroad (the impatriation premium) are exempt. Alternatively, on option, 30% of pay is exempt instead.
2. **Comparable pay.** If the taxed part of pay is lower than the pay for similar duties in the company (or in similar French companies), the difference is added back.
3. **Foreign workdays.** The part of pay for work done abroad, in the direct and exclusive interest of the employer, is also exempt.
4. **Caps.** On the employee's option, either the exempt total (premium plus foreign workdays) is limited to 50% of total pay, or the foreign-workdays part is limited to 20% of the taxable pay that results from step 1.
5. **Passive income.** For the same period, 50% of the following foreign income is exempt: investment income paid by a person established in a state whose treaty with France has an administrative-assistance clause; royalties of art. 92, 2, 2° and 3° from such a payer; gains on securities whose custodian (or issuing company) is in such a state. Losses on those securities count for 50%.
6. **Social levies.** CSS art. L136-6, I, 4° makes the income exempted under art. 155 B, II subject to the patrimony contribution. The levies are due on the full amount, not on the taxed half.
7. An impatriate cannot also use art. 81 A (the expatriate exemption).

## Deadlines and filing

- **Non-resident return.** Non-residents file the same annual return (form 2042 and its annexes) as residents. Check the date for non-residents in `fr-personal-income-tax`. The non-resident tax office is the service des impôts des particuliers non-résidents (SIP des non-résidents). Contact (service-public.gouv.fr, page F2329): telephone +33 1 72 95 20 42, Monday to Friday 9:00 to 16:00; secure messaging in the online personal account; post to 10 rue du Centre, TSA 10010, 93465 Noisy-le-Grand Cedex. The SIP des non-résidents sends the social levies notice between August and September.
- **Average-rate option.** Claimed on the return, with proof of worldwide income, or a sworn statement for residents of the states named in art. 197 A, a.
- **Property gains (art. 244 bis A).** The levy is paid when the deed is registered, or within a month of the sale if there is no registration. An accredited tax representative in France is responsible for it. No representative is needed if the seller lives in an EU state, or in an EEA state that has both an administrative-assistance and a recovery-assistance convention with France (art. 244 bis A, IV bis, last paragraph). A seller living elsewhere, the UK included, appoints one.
- **Withholding by payers.** The French employer applies art. 182 A on each payment. The payer of fees or royalties applies art. 182 B. Both are then credited against the non-resident's annual tax.
- **Impatriate.** The regime is claimed through the employer's pay reporting and on the employee's annual return. The 50% passive income exemption is claimed on the return.
- **A1.** An employee posted within the EU applies for an A1 certificate in the sending state. The worker stays on the home scheme if the posting is expected to last 24 months or less and the worker is not replacing another posted person (Regulation 883/2004, art. 12, 1).

## Penalties and interest

- **Late filing (art. 1728).** 10% of the tax if there was no formal notice, or if the return is filed within 30 days of a formal notice. 40% if it is not filed within 30 days of the formal notice. 80% where a hidden activity is found.
- **Inaccuracies or omissions (art. 1729).** 40% for a deliberate breach. 80% for abuse of law (reduced to 40% if the person was neither the main initiator nor the main beneficiary). 80% for fraudulent manoeuvres or a hidden part of a price.
- **Late payment interest (art. 1727).** 0.20% a month.
- **Social levies not paid within 45 days of assessment.** A 10% surcharge under CGI art. 1730 (CSS art. L136-6, III).
- For the audit procedure and appeals, use `fr-tax-audit`.

## Cross-border points

- **Treaty first.** Check the treaty before the domestic rule. A treaty can move residence (art. 4 B, 1, last paragraph), remove or reduce withholding under art. 182 B and art. 244 bis A ("sous réserve des conventions internationales"), and decides which state may tax.
- **Two treaty credit methods.** French treaties usually remove double tax for a French resident with a foreign tax credit set against French tax. The France-United Kingdom treaty (signed 19 June 2008, art. 24) shows both methods:
  - **Credit equal to the French tax.** For most income taxable in the UK (salaries, rents, business profits), the income is included in the French computation, and the credit equals the French tax on that income. This works like an exemption that keeps the income in the rate. The person must be subject to UK tax on it.
  - **Credit equal to the foreign tax.** For dividends (art. 11), some gains (art. 14), directors' fees (art. 15, 3), artists and sportsmen (art. 16), certain pensions (art. 17, 1 and 2) and art. 23, 3 income, the credit is the UK tax actually borne, capped at the French tax on that income.
  - **The French tax on the income.** For income taxed at a flat rate, it is the net income times that rate. For income taxed on the scale, it is the net income times the average rate (French tax on total net income divided by that income).
- **No double use of the payroll scheme.** Foreign income that gets a credit equal to the French tax is outside the prélèvement à la source (art. 204 D).
- **Pay rate.** The individual withholding rate is calculated net of treaty credits on the income concerned (art. 204 H, I, 1).
- **Social security.** In the EU, EEA and Switzerland, Regulation 883/2004 decides which state's contributions are due. One state's scheme applies at a time. A posted worker keeps the home scheme for up to 24 months with an A1. A person covered by another EU state's scheme owes only the 7.5% solidarity levy on French patrimony income (see The taxable base).
- **Leaving France.** Departure-year rules, the exit tax and the former main home are in `leaving-france-exit-tax`. The former-home exemption for non-residents is in art. 244 bis A, I, 1 (see The taxable base).

## Worked examples

### Example 1: a UK resident letting a Paris flat, minimum rate against the average-rate option

A single person lives in the UK and is not French-domiciled. They let an unfurnished flat in Paris. For 2026 the net rental income under the régime réel (form 2044, see `fr-rental-income`) is EUR 12,000. They have no other French income. Their worldwide income, measured under French rules, is EUR 50,000 (the EUR 12,000 plus UK salary). One household share. The scale used is the art. 197 scale read on 23 October 2026; replace it with the scale for income of 2026 once enacted.

- Scale on the French income alone: 11% of (12,000 minus 11,600) = EUR 44. The minimum rate gives 20% of 12,000 = EUR 2,400. The tax is the higher, EUR 2,400.
- Average-rate option: French tax on EUR 50,000 is EUR 1,977.69 (11% band) plus 30% of (50,000 minus 29,579), which is EUR 8,103.99. The average rate is 8,103.99 / 50,000 = 16.208%. Applied to EUR 12,000 that is EUR 1,944.96. It is lower than EUR 2,400, so the option saves EUR 455.04 if the person can prove the worldwide income.
- Social levies on rents: 17.2% of EUR 12,000 = EUR 2,064 if not covered by an EU scheme under Regulation 883/2004. If the person is covered under that Regulation and not by a French scheme, only the 7.5% levy is due: EUR 900. Whether UK cover qualifies after Brexit is not confirmed (see Sources).
- Treaty: rents from French property may be taxed in France (France-UK treaty, art. 6). Relief for the French tax is given in the UK, not covered here.

```oa-check
name: UK resident, Paris rent EUR 12,000, minimum rate vs average-rate option (2026)
inputs:
  french_income: 12000
  worldwide_income: 50000
  band1_top: 11600
  band2_top: 29579
  band3_top: 84577
steps:
  - scale_french: max(min(french_income, band2_top) - band1_top, 0) * 0.11 + max(min(french_income, band3_top) - band2_top, 0) * 0.30
  - minimum_tax: min(french_income, band2_top) * 0.20 + max(french_income - band2_top, 0) * 0.30
  - tax_minimum_rule: max(scale_french, minimum_tax)
  - scale_world: max(min(worldwide_income, band2_top) - band1_top, 0) * 0.11 + max(min(worldwide_income, band3_top) - band2_top, 0) * 0.30
  - tax_average_option: round(french_income * scale_world / worldwide_income, 2)
  - tax_due: min(tax_minimum_rule, tax_average_option)
  - saving: tax_minimum_rule - tax_due
  - levies_full: french_income * 0.172
  - levies_eu_covered: french_income * 0.075
expected:
  scale_french: 44.00
  minimum_tax: 2400.00
  tax_minimum_rule: 2400.00
  scale_world: 8103.99
  tax_average_option: 1944.96
  tax_due: 1944.96
  saving: 455.04
  levies_full: 2064.00
  levies_eu_covered: 900.00
```

### Example 2: an impatriate with a premium, an add-back and foreign dividends

An engineer arrives from abroad in 2026 to work for a French company. They were not French-domiciled in 2021 to 2025, and are French-domiciled from arrival (home and main activity). Their 2026 pay is EUR 150,000: EUR 120,000 salary plus a EUR 30,000 impatriation premium written into the contract. The company pays EUR 125,000 for similar duties. 10% of their working days are abroad, in the employer's direct and exclusive interest. They receive EUR 10,000 of dividends from a company in a state whose treaty with France has an administrative-assistance clause; no foreign tax was withheld. They opt for the flat 12.8% on investment income and are affiliated to the French social security scheme.

- Taxed pay after the premium: 150,000 minus 30,000 = 120,000. This is EUR 5,000 below comparable pay, so EUR 5,000 is added back. The exempt premium is EUR 25,000 and taxable pay under step 1 is EUR 125,000.
- Foreign workdays: 10% of 125,000 = EUR 12,500 exempt.
- Caps: total exempt EUR 37,500 is below 50% of total pay (EUR 75,000). The foreign-days part (EUR 12,500) is below 20% of taxable pay (EUR 25,000). Neither cap reduces the exemption.
- Taxable pay: 150,000 minus 37,500 = EUR 112,500, before the 10% salary deduction and the scale (`fr-personal-income-tax`).
- Dividends: 50% exempt, so EUR 5,000 is taxed at 12.8% = EUR 640. Social levies apply to the full EUR 10,000 at 18.6% = EUR 1,860 (CSS art. L136-6, I, 4°).
- The regime runs to 31 December 2034 (the eighth calendar year after 2026).

```oa-check
name: Impatriate art. 155 B, pay EUR 150,000 with premium, add-back, foreign days and dividends (2026)
inputs:
  total_pay: 150000
  premium: 30000
  comparable_pay: 125000
  foreign_dividends: 10000
  start_year: 2026
steps:
  - taxable_before_addback: total_pay - premium
  - addback: max(comparable_pay - taxable_before_addback, 0)
  - premium_exempt: premium - addback
  - taxable_step1: taxable_before_addback + addback
  - foreign_days_exempt: taxable_step1 * 10 / 100
  - cap_50: total_pay * 0.5
  - cap_20_foreign: taxable_step1 * 0.2
  - exempt_total: min(premium_exempt + min(foreign_days_exempt, cap_20_foreign), cap_50)
  - taxable_pay: total_pay - exempt_total
  - dividends_taxed: foreign_dividends * 0.5
  - dividend_tax: dividends_taxed * 0.128
  - dividend_levies: foreign_dividends * 0.186
  - last_year: start_year + 8
expected:
  addback: 5000.00
  premium_exempt: 25000.00
  taxable_step1: 125000.00
  foreign_days_exempt: 12500.00
  exempt_total: 37500.00
  taxable_pay: 112500.00
  dividends_taxed: 5000.00
  dividend_tax: 640.00
  dividend_levies: 1860.00
  last_year: 2034
```

## Ask the client first

1. Where is your home, where does your family live, where do you mainly work, and where are most of your assets and income? Did you live in France at any time in the last five years? This settles art. 4 B, the treaty tie-breaker and art. 155 B eligibility.
2. Which country's social security covers you for health, and do you hold an A1 or an equivalent certificate? This decides 7.5% against 17.2% or 18.6%. Is any French flat let furnished or unfurnished? This decides 17.2% against 18.6%.
3. Your total worldwide income for the year, with proof. If the average rate is below 20%, the option lowers the French tax.
4. For an impatriate: the contract (premium written in or not), the start date, the pay for similar duties, and a log of days worked abroad.
5. Every French-source payment and any French withholding already suffered (salary under art. 182 A, fees under art. 182 B, a property sale under art. 244 bis A).
6. Your country of residence, so the right treaty and its credit method can be applied.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 4 A (worldwide or French-source scope) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006302200 | 2026-10-23 |
| CGI art. 4 B (tax domicile tests) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051202565 | 2026-10-23 |
| CGI art. 155 B (impatriates) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985788 | 2026-10-23 |
| CGI art. 164 A (non-resident base) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006308201 | 2026-10-23 |
| CGI art. 164 B (French-source income) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031815417 | 2026-10-23 |
| CGI art. 182 A (salary withholding for non-residents) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373628 | 2026-10-23 |
| CGI art. 182 A bis (artists) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042907688 | 2026-10-23 |
| CGI art. 182 B (fees, royalties, services) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 | 2026-10-23 |
| CGI art. 197 (scale) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053542636 | 2026-10-23 |
| CGI art. 197 A (minimum rate, average-rate option) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037985917 | 2026-10-23 |
| CGI art. 200 A (12.8% flat rate) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896 | 2026-10-23 |
| CGI art. 204 D (income outside the prélèvement à la source) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373571 | 2026-10-23 |
| CGI art. 204 H (withholding rate net of treaty credits) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373568 | 2026-10-23 |
| CGI art. 150 VC (holding-period allowance) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047970756 | 2026-10-23 |
| CGI art. 235 ter (7.5% solidarity levy) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037949145 | 2026-10-23 |
| CGI art. 244 bis A (property gains of non-residents) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806274 | 2026-10-23 |
| CGI art. 244 bis B (large stakes) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051200525 | 2026-10-23 |
| CGI art. 1609 nonies G (surtax on property gains) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806252 | 2026-10-23 |
| CGI art. 1727 (late payment interest) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 | 2026-10-23 |
| CGI art. 1728 (late filing) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 | 2026-10-23 |
| CGI art. 1729 (inaccuracies) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 | 2026-10-23 |
| CSS art. L136-6 (patrimony contribution; I bis non-residents; I ter EU cover) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218166 | 2026-10-23 |
| CSS art. L136-7 (investment income and property gains; I bis non-residents; VI, 2 social-levy holding allowance) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053584839 | 2026-10-23 |
| CSS art. L136-8 (CSG rates, version in force from 27 June 2026; the note there about 2026 income concerns IV bis, added by loi n° 2026-534, art. 65, not the 10.6% rate) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623 | 2026-10-23 |
| LFSS 2026 (loi n° 2025-1403), art. 12 (10.6% CSG and its start dates, II) | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053226452 | 2026-10-23 |
| CGI art. 219 (25% standard rate used by art. 182 B and 244 bis A) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 | 2026-10-23 |
| service-public.gouv.fr F2329 (social levies on patrimony income; non-residents; SIP des non-résidents contact; checked 30 June 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 | 2026-10-23 |
| Ordonnance n° 96-50, art. 19 (CRDS 0.5%) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000190291 | 2026-10-23 |
| France-UK tax treaty of 19 June 2008, arts. 6 and 24 (décret n° 2010-20) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000021645398 | 2026-10-23 |
| Regulation (EC) 883/2004, art. 12 (postings) | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731 | 2026-10-23 |

Not yet confirmed: impots.gouv.fr and BOFiP were in maintenance on 23 October 2026, so these items were not read. (1) Whether a person covered by the UK scheme after Brexit gets the CSG and CRDS relief of CSS art. L136-6, I ter (that article names only Regulation 883/2004; service-public.gouv.fr F2329 names only the EEA and Switzerland). (2) Whether the art. 155 B, I, 3 caps are compulsory with a choice between them, or apply only on option (the article's wording says "sur option"; BOFiP BOI-RSA-GEO-40-10 not read). (3) The 2026 filing dates for non-residents. (4) Whether the 2027 finance law will change the art. 197 scale for 2026 income. (5) Whether the excess of art. 182 A and 182 A bis withholding over the art. 197 A tax is refunded: unlike art. 182 B, II, those articles provide only that the withholding is set against the tax.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fr-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fr-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
