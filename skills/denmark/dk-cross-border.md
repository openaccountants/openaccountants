---
name: dk-cross-border
description: "Danish cross-border tax for individuals and companies, income year 2026. Covers full tax liability (dwelling in Denmark, the 6-month stay rule, the 3-month and 180-day holiday rule), limited tax liability of non-residents on Danish wages, board fees, permanent establishments, property, dividends and royalties, the researcher and key-employee scheme (forskerskatteordningen: 27% plus 8% AM-bidrag for up to 84 months, minimum salary DKK 65,400 a month in 2026), cross-border commuters (grænsegængere, 75% rule), withholding on dividends (27%, 15%, 44%) and royalties (22%) and the refund claim, foreign tax credit and the ligningsloven § 33 A exemption, and exit tax on shares (fraflytningsbeskatning, DKK 100,000 threshold, deferral). Trigger on: moving to or from Denmark, Danish tax residence, begrænset skattepligt, forskerordning, grænsegænger, udbytteskat refund, fraflytningsskat, fast driftssted. Out of scope: rate tables for residents (dk-income-tax), share income in general (dk-capital-gains), company exit tax and corporate withholding detail (dk-corporate-tax), VAT (denmark-vat-return)."
version: 0.2
jurisdiction: DK
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark: cross-border tax (residence, non-residents, withholding, exit) v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's or company's facts, elections, deadlines or filings. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Denmark.

Tax year: income year 2026 (calendar year for individuals). Currency: Danish kroner (DKK). Authority: Skattestyrelsen (skat.dk). Main statutes: Kildeskatteloven (KSL), Ligningsloven (LL), Aktieavancebeskatningsloven (ABL), Selskabsskatteloven (SEL), Skattekontrolloven (SKL). The KSL consolidation of May 2024 has since been amended; the changes that matter here are lov nr. 1691 of 30 December 2024, § 6 (researcher-scheme pay base, from income year 2026), lov nr. 1694 of 30 December 2024, § 4 (refund interest, § 69 B) and lov nr. 1648 of 16 December 2025, § 20 (§ 48 renumbered from 1 January 2026). No amending law since May 2024 changes KSL §§ 1, 2, 5 A-5 D, 7-10, 48 B or 48 F. Indexed amounts are taken from Skatte- og Vækstministeriet's 2026 rate tables.

See also: dk-income-tax (resident rates, allowances, self-employed), dk-capital-gains (share income for residents), dk-corporate-tax (company tax, outbound withholding detail, company exit tax), denmark-vat-return (VAT).

## Who this applies to

**Full tax liability (KSL § 1).** A person is fully liable on worldwide income if they:
- have a dwelling (bopæl) in Denmark (§ 1, stk. 1, nr. 1). Liability starts only when the person also takes up residence; a short holiday stay does not count (KSL § 7, stk. 1). Skattestyrelsen applies this as: a person with a Danish home can stay up to 3 consecutive months, or 180 days in any 12-month period, without becoming fully liable, if the stay is holiday-like and involves no work;
- stay in Denmark for at least 6 months without a dwelling, counting short trips abroad for holidays (§ 1, stk. 1, nr. 2). Liability then runs from the start of the stay (KSL § 8, stk. 1). Tourists and students who stay taxable at home only become liable after more than 365 days within 2 years (§ 8, stk. 2);
- are Danish public servants posted abroad, and certain seafarers (§ 1, stk. 1, nr. 3-4).

A person fully liable under § 1 but resident in another state under a tax treaty can only deduct expenses tied to income Denmark may tax under the treaty (KSL § 1, stk. 2).

**Limited tax liability (KSL § 2).** A person not covered by § 1 is taxed only on listed Danish income, including:
- pay for work done in Denmark, plus severance and non-compete pay linked to Danish work (§ 2, stk. 1, nr. 1). Pay from an employer with no Danish base is outside this unless the person is in Denmark for more than 183 days in a 12-month period (§ 2, stk. 14, nr. 2);
- board fees (nr. 2); hired-out labour working as an integrated part of a Danish business (nr. 3), taxed at a gross 30% (KSL § 48 B) unless the person elects ordinary taxation by 1 May of the following year (§ 2, stk. 10);
- business carried on through a permanent establishment in Denmark (nr. 4); Danish real property and gains on it (nr. 5);
- dividends from Danish companies (nr. 6), royalties (nr. 8), and Danish pensions and social benefits (nr. 9-12).

Interest received by a non-resident individual is not on the § 2 list, so it is not taxed in Denmark unless it belongs to a Danish permanent establishment.

**Companies.** A company is resident if registered in Denmark or managed from Denmark (SEL § 1, stk. 6). A foreign company is taxed on a Danish permanent establishment, Danish property, and by withholding on dividends, interest on controlled debt and royalties (SEL § 2, stk. 1). Company exit tax and the corporate withholding detail are in dk-corporate-tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Labour market contribution (AM-bidrag), full and limited liability | 8% | 2026 | https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability |
| Researcher and key-employee scheme, gross tax | 27% of cash pay, plus AM-bidrag | 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Researcher scheme, minimum monthly pay (before AM-bidrag, plus ATP) | DKK 65,400 (DKK 78,000 in 2025; DKK 67,300 for 2027): base DKK 47,600 at 2010 level, indexed under Personskatteloven § 20 | 2026 | KSL § 48 E, stk. 3, nr. 3, as amended by lov nr. 1691 of 30 December 2024, § 6, nr. 1 (effect from income year 2026, § 9, stk. 5); https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Researcher scheme, maximum period | 84 months in total | 2026 | KSL § 48 F, stk. 2; https://info.skat.dk/data.aspx?oid=1977284 |
| Researcher scheme, look-back: no Danish tax liability in prior | 10 years | 2026 | KSL § 48 E, stk. 3, nr. 1; https://info.skat.dk/data.aspx?oid=1977286 |
| Hired-out labour, gross tax | 30% | 2026 | KSL § 48 B; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Cross-border commuter, minimum share of income taxable in Denmark | 75% | 2026 | KSL § 5 A; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Dividend withholding by the paying company | 27% | 2026 | KSL § 65; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Final dividend tax, non-resident individual | 27%; 15% if under 10% held and the home state exchanges information; 44% on main-shareholder shares held from a ligningsloven § 5 H state | 2026 | KSL § 2, stk. 11; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Royalty withholding | 22% | 2026 | KSL §§ 2, stk. 12, and 65 C; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Interest on controlled debt to foreign related companies | 22% | 2026 | KSL § 65 D; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Withholding rate where no tax card exists | 55% | 2026 | KSL § 48, stk. 9 (stk. 8 until 31 December 2025; renumbered by lov nr. 1648 of 16 December 2025, § 20); https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven |
| Share income tax (used for exit tax on shares) | 27% up to DKK 79,400; 42% above | 2026 | Personskatteloven § 8 a; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven |
| Exit tax on shares, minimum holding value | DKK 100,000 market value | 2026 | ABL § 38, stk. 2; https://www.retsinformation.dk/eli/lta/2026/849 |
| Exit tax on shares, prior Danish liability needed | at least 7 of the last 10 years | 2026 | ABL § 38, stk. 3; https://www.retsinformation.dk/eli/lta/2026/849 |
| Dividend tax refund, limitation period | 5 years from withholding | 2026 | https://skat.dk/en-us/businesses/companies-and-foundations/companies-and-foundations/declaring-and-paying-dividends-and-dividend-tax/claiming-refund-of-danish-dividend-tax |
| § 33 A exemption, minimum stay abroad; maximum days in Denmark | 6 months; 42 days | 2026 | LL § 33 A, stk. 1; https://www.retsinformation.dk/eli/lta/2025/1500 |
| Late filing skattetillæg (persons covered by SKL § 5) | DKK 400 a day, at most DKK 10,000; DKK 200 a day, at most DKK 5,000 if taxable income is below the top-tax threshold | 2026 | SKL § 73, stk. 1-2, as amended by lov nr. 16 of 14 January 2025; https://www.retsinformation.dk/eli/lta/2025/16 |
| Voluntary payment after year end: day-to-day interest; residual tax: percentage surcharge | 3.7%; 5.7% for income year 2025. The income year 2026 rates are published in December 2026 | 2025 | KSL § 59, stk. 1, and § 61, stk. 2; SKM2025.716.SKTST, https://info.skat.dk/data.aspx?oid=2460000 |
| Lapsed exit-tax deferral: monthly rate under Opkrævningsloven § 7, stk. 2 | 0.1% a month, plus 0.4 percentage points per started month | 2026 | ABL § 39, stk. 4; SKM2025.720.SKTST, https://info.skat.dk/data.aspx?oid=2459995 |

## The taxable base

**Arrival year.** In the first year of full liability, income is scaled to a full year so the progressive bands work, and the full-year tax is then reduced to the part-year share (Skattestyrelsen, tax liability page). Assets brought into Danish tax on arrival take market value at arrival as their cost (KSL § 9, stk. 1); depreciable assets follow § 9, stk. 2.

**Non-resident employees.** The base is Danish-source pay under KSL § 2, less only expenses tied to that income (§ 2, stk. 9). A person working in Denmark for less than a full year can tick box 69 in the limited-liability return to have income converted to a full year and get the personal allowance; otherwise no personal allowance is used (Skattestyrelsen, tax liability page).

**Cross-border commuters (grænsegængere, KSL §§ 5 A-5 D).** If at least 75% of the person's total income (worldwide, measured under Danish rules) is wages or business income Denmark may tax, they can elect commuter treatment. They then get the deductions a resident gets for personal and family items: own-home interest net of rental value, private interest, deductible pension and unemployment fund payments, gifts, maintenance and compulsory foreign social contributions (§ 5 B). Tax is calculated like a resident's (§ 5 C), and a spouse living at the same address is treated as fully liable for the calculation, using the spouse's total income (§ 5 C, stk. 2). The election is made in the return and can be changed until 30 June in the second year after the income year (§ 5 D).

**Researcher and key-employee scheme (KSL §§ 48 E-48 F).** An employee who becomes liable under § 1 or § 2, stk. 1, nr. 1, working for a Danish-taxable employer, can elect a gross tax of 27% on cash pay (plus 8% AM-bidrag). Conditions:
- no Danish liability under § 1 or the listed parts of § 2 in the 10 years before the employment (§ 48 E, stk. 3, nr. 1). Earlier periods under the scheme itself are ignored (§ 48 F, stk. 2);
- no stake in the management, control or significant influence over the employer in the last 5 years (§ 48 E, stk. 3, nr. 2);
- a contract guaranteeing an average monthly cash pay of at least DKK 65,400 in 2026 before AM-bidrag, plus ATP (§ 48 E, stk. 3, nr. 3: base DKK 47,600 at 2010 level from income year 2026, lowered from DKK 59,500 by lov nr. 1691/2024). Bonuses only count if the right to a fixed amount arises during the year under the contract; a year-end top-up does not cure a shortfall. Employer pension contributions with bortseelsesret do not count (Den juridiske vejledning C.F.6.1.4). Researchers approved by a public research institution or Danmarks Frie Forskningsfond are exempt from the pay test (§ 48 E, stk. 4);
- the scheme does not apply to a treaty-resident employee who works abroad with taxing rights moving away for more than 30 working days in the calendar year (§ 48 E, stk. 2).

The 27% applies with no deductions, and the scheme pay is kept out of taxable income (§ 48 F, stk. 1). Losses (other than business losses) cannot be carried forward in scheme years (§ 48 F, stk. 5), and § 33 A relief is not available on scheme pay (§ 48 F, stk. 7). The scheme runs for up to 84 months in total, split over any number of periods (§ 48 F, stk. 2). Maternity and parental leave do not break the pay test but do not extend the 84 months (C.F.6.1.4).

**Foreign tax relief for residents.**
- **Credit (LL § 33).** Foreign tax on foreign-source income is credited against Danish state and municipal tax on that income. The credit cannot exceed the Danish tax that falls proportionally on the foreign income (§ 33, stk. 1), and under a treaty it cannot exceed the tax the other state is entitled to under the treaty (§ 33, stk. 2).
- **Employment abroad (LL § 33 A).** A fully liable person who earns wages during a stay abroad of at least 6 months, with breaks in Denmark of no more than 42 days in total (holidays or work tied to the stay), gets the Danish tax on that pay reduced in full (§ 33 A, stk. 1). Where a treaty gives Denmark the taxing right, the reduction is half (§ 33 A, stk. 3). Pay for work done in Denmark is excluded, and Danish state employees receiving certain allowances are excluded (§ 33 A, stk. 2).
- **Treaty exemption.** Where a treaty uses exemption with progression, the treaty article governs; read the specific treaty.

**Exit tax on shares (ABL §§ 38-40).** When Danish taxing rights end (ending § 1 liability, or becoming treaty-resident abroad) for reasons other than death, gains and losses on shares are treated as realised at market value on the exit date (§ 38, stk. 1). This applies only if the person holds shares worth DKK 100,000 or more in total at exit (§ 38, stk. 2), and was Danish-liable on share gains for at least 7 of the last 10 years (§ 38, stk. 3). Shares acquired from a spouse who meets the 7-year test, or by succession, are caught regardless. The net gain is share income taxed at 27% and 42% (Personskatteloven § 8 a). Losses on shares at exit can only offset exit gains (§ 38, stk. 4).

**Exit tax on other assets.** Other assets that leave Danish taxation are treated as sold at market value on departure (KSL § 10, stk. 1). This does not cover shares (ABL § 38), receivables and debt (Kursgevinstloven § 37) or employee options and warrants (LL § 28), which have their own rules (KSL § 10, stk. 3). Deferral for tax on LL § 28 options is in KSL § 73 E.

**Permanent establishment.** For both individuals (KSL § 2, stk. 3-8) and companies (SEL § 2, stk. 2-4), a PE exists where business is carried on through a fixed place of business in Denmark. A building, construction or installation project is a PE from the first day. A place used only for preparatory or auxiliary activity is not a PE unless it forms part of a wider set of complementary functions in Denmark. A dependent agent who habitually concludes contracts, or plays the principal role in concluding them, creates a PE; an independent agent acting in the ordinary course of its business does not. Profit is attributed on an arm's length basis as if the PE were a separate enterprise (KSL § 2, stk. 8), unless the relevant treaty article says otherwise.

## Deadlines and filing

- **Return for individuals.** People who receive an annual assessment (årsopgørelse) must correct it by 1 May of the following year (SKL § 10, stk. 1). People expected to file a full return, including most with foreign income or limited liability, and the self-employed, file by **1 July 2027** for income year 2026 (SKL §§ 10, stk. 2, and 11). Limited-liability taxpayers use TastSelv or form 04.009 with supplement 04.031.
- **Elections.** Commuter treatment is chosen in the return and can be changed until 30 June 2028 for 2026 (KSL § 5 D). Ordinary taxation instead of the 30% hired-out labour tax must be chosen by 1 May 2027 (KSL § 2, stk. 10). The researcher scheme is applied through the employer's withholding from the start of the employment.
- **Dividend tax by the paying company.** Due as soon as the dividend is declared, and paid by the company's deadline for A-tax in the following month (KSL § 66, stk. 1).
- **Dividend tax refund.** Claim online within 5 years of withholding (a treaty can set a different period), one shareholder per claim and up to 20 distributions. Attach a residence certificate certified by the home tax authority (for individuals form 02.050), the dividend advice, account and custody statements and any power of attorney (form 02.043). Skattestyrelsen pays interest if processing exceeds six months (KSL § 69 B). Claims filed before 1 January 2026 and not yet decided have had expected processing extended by 18 months. Skattestyrelsen applied a 3-year limit from 2016; after the Supreme Court held in June 2026 that the limit is 5 years, it is reopening, by the end of 2026 and without a request, claims rejected on the 3-year limit for dividend tax withheld after 11 June 2021 (skat.dk refund page).
- **Exit tax.** The tax is computed in the return for the year of departure. To keep deferral, the return and a holdings list (beholdningsoversigt) must be filed on time (ABL § 39, stk. 2), and a return must be filed every year while a deferred balance exists, by 1 July with the current address (ABL § 39 A, stk. 11). Amounts that fall due are paid by 20 September of the following year (§ 39 A, stk. 12).

## Penalties and interest

- **Late return (persons covered by SKL § 5, mainly the self-employed).** Skattetillæg of DKK 400 a day, capped at DKK 10,000; DKK 200 a day, capped at DKK 5,000, where taxable income is below the top-tax threshold (SKL § 73, stk. 1-2, as amended by lov nr. 16/2025). Skattestyrelsen can also assess income on an estimated basis (SKL § 74).
- **Residual tax.** Residual tax (restskat) at the annual assessment carries a percentage surcharge: 5.7% for income year 2025 (KSL § 61, stk. 2). Paying extra preliminary tax by 1 July of the following year avoids it and costs only day-to-day interest: 3.7% for income year 2025 (KSL § 59, stk. 1). Both rates are set in SKM2025.716.SKTST; the income year 2026 rates are published in December 2026.
- **Exit tax deferral lost.** If the return and holdings list are late, deferral lapses and the tax is due as if no deferral had been given, with interest at the Opkrævningsloven § 7, stk. 2 rate (0.1% a month for 2026, SKM2025.720.SKTST) plus 0.4 percentage points per started month (ABL § 39, stk. 4). Skattestyrelsen can overlook a late filing (§ 39, stk. 5). A late annual return during deferral makes the whole balance due (§ 39 A, stk. 11).
- **Researcher scheme under-withholding.** Tax withheld too low is set against any refund; too high is set against residual tax (KSL § 48 F, stk. 8).

## Cross-border points

**Withholding on dividends to non-residents.** The company withholds 27% (KSL § 65). A non-resident individual's final tax is 27%, reduced to 15% where they hold under 10% and their state exchanges tax information with Denmark (KSL § 2, stk. 11). Outside the EU the under-10% test includes related parties. A treaty can reduce it further. The excess is reclaimed from Skattestyrelsen. The rate is 44% on main-shareholder shares where the beneficial owner is resident in a state on the ligningsloven § 5 H, stk. 2 list. Corporate shareholders: see dk-corporate-tax.

**Royalties and interest.** Royalties paid abroad carry 22% withholding (KSL § 65 C) unless a treaty or the Interest and Royalties Directive reduces it. Interest paid to non-resident individuals is not taxed. Interest on controlled debt paid to foreign related companies carries 22% (KSL § 65 D); detail in dk-corporate-tax.

**Treaty tie-breaker.** A person fully liable under § 1 may still be resident elsewhere under a treaty. Becoming treaty-resident abroad counts as exit for share exit tax (ABL § 38, stk. 1) and for other assets (KSL § 10, stk. 1).

**Deferral of share exit tax (ABL §§ 39-39 B).** Deferral is available on request. Moving to a country outside the Nordic mutual assistance convention (7 December 1989) and outside Council Directive 2010/24/EU also needs adequate security (bank guarantee, listed securities or similar) (§ 39, stk. 3). The deferred balance falls due as shares are sold (gain computed on the exit-date cost basis, with credit for foreign tax under LL § 33), as dividends are received, on other value-reducing distributions, on loans from the company, and on death (§ 39 A, stk. 2-9). A later fall in value reduces the balance. The balance lapses once all shares on the list are sold, unless unused losses remain (§ 39 A, stk. 10). If the person moves back to Denmark, the market value on return is reduced and the remaining balance lapses (§ 39 B).

**Company exit.** A company that stops being resident, or moves assets out of Danish taxation, is taxed on market value with an optional five-year deferral for EU/EEA moves (SEL § 5, stk. 7; §§ 26-27). See dk-corporate-tax.

## Worked examples

**Example 1: key employee under the researcher scheme, income year 2026.** Ana moves from Spain to Copenhagen on 1 January 2026 to work for a Danish A/S. She has never been liable to Danish tax and owns no shares in the employer. Her contract pays DKK 80,000 a month in cash, above the DKK 65,400 minimum, so she elects the scheme. Annual cash pay is DKK 960,000. AM-bidrag at 8% is DKK 76,800. The 27% scheme tax is charged on pay after AM-bidrag, DKK 883,200, giving DKK 238,464. Total Danish tax on the pay is DKK 315,264, an effective 32.84%. She gets no deductions against this pay, and the scheme can run for up to 84 months.

```oa-check
name: Example 1, researcher and key-employee scheme, DKK 80,000 a month (2026)
inputs:
  monthly_pay: 80000
  months: 12
  minimum_monthly_pay: 65400
  am_rate: 0.08
  scheme_rate: 0.27
steps:
  - qualifies_margin: monthly_pay - minimum_monthly_pay
  - annual_pay: monthly_pay * months
  - am_bidrag: annual_pay * am_rate
  - scheme_base: annual_pay - am_bidrag
  - scheme_tax: scheme_base * scheme_rate
  - total_tax: am_bidrag + scheme_tax
  - effective_rate_pct: total_tax / annual_pay * 100
expected:
  qualifies_margin: 14600
  annual_pay: 960000
  am_bidrag: 76800
  scheme_base: 883200
  scheme_tax: 238464
  total_tax: 315264
  effective_rate_pct: 32.84
```

**Example 2: exit tax on shares when leaving Denmark, 2026.** Lars, single, has been fully liable in Denmark for 12 years. He moves to Portugal on 1 December 2026 and gives up his Danish home. At departure he owns unlisted shares worth DKK 2,000,000 (cost DKK 400,000) and listed shares worth DKK 50,000 (cost DKK 30,000). His holdings total DKK 2,050,000, over the DKK 100,000 threshold, and he meets the 7-in-10-year test, so ABL § 38 applies. The deemed gain is DKK 1,600,000 + DKK 20,000 = DKK 1,620,000. He has no other share income in 2026. Tax at 27% on the first DKK 79,400 is DKK 21,438, and at 42% on the remaining DKK 1,540,600 is DKK 647,052, a total of DKK 668,490. Portugal is covered by Directive 2010/24/EU, so he can defer without security if he files the 2026 return and holdings list by 1 July 2027 and files every year after. Had he moved to a country outside the Nordic convention and the Directive, deferral would need security for the DKK 668,490.

```oa-check
name: Example 2, share exit tax on departure (2026 share income bands)
inputs:
  unlisted_value: 2000000
  unlisted_cost: 400000
  listed_value: 50000
  listed_cost: 30000
  threshold: 100000
  band_limit: 79400
steps:
  - holding_value: unlisted_value + listed_value
  - over_threshold: holding_value - threshold
  - deemed_gain: (unlisted_value - unlisted_cost) + (listed_value - listed_cost)
  - tax_low: min(deemed_gain, band_limit) * 0.27
  - tax_high: max(deemed_gain - band_limit, 0) * 0.42
  - exit_tax: tax_low + tax_high
expected:
  holding_value: 2050000
  over_threshold: 1950000
  deemed_gain: 1620000
  tax_low: 21438
  tax_high: 647052
  exit_tax: 668490
```

## Ask the client first

1. **Dates and homes.** When did they arrive or leave, do they keep a dwelling in Denmark, and how many days were spent in Denmark in any 12-month period? This decides full or limited liability and the start or end date.
2. **Treaty residence.** Where is their family, permanent home and centre of vital interests? A treaty tie-breaker can make them resident abroad even while § 1 applies.
3. **Previous Danish liability.** Have they been liable to Danish tax at any time in the last 10 years? This decides the researcher scheme and the 7-in-10 test for share exit tax.
4. **Employment terms.** Contract cash pay per month, who bears the cost, any ownership in the employer, and expected workdays outside Denmark. This decides the scheme and § 33 A.
5. **Income mix.** For a non-resident, what share of total worldwide income is Danish wages or business income? At 75% or more, commuter treatment is open.
6. **Shareholdings at exit.** Market value and cost of every share holding at departure, and the destination country. This decides whether exit tax applies and whether deferral needs security.

## Sources

| Source | URL | Read on |
|---|---|---|
| Kildeskatteloven, LBK nr. 460 of 3 May 2024, §§ 1, 2, 5 A-5 D, 7-10, 48 B, 48 E-48 F, 65-66, 73 E | https://www.retsinformation.dk/eli/lta/2024/460 | 2026-10-23 |
| Ligningsloven, LBK nr. 1500 of 24 November 2025, §§ 33 and 33 A | https://www.retsinformation.dk/eli/lta/2025/1500 | 2026-10-23 |
| Aktieavancebeskatningsloven, LBK nr. 849 of 21 September 2026, §§ 38-40 | https://www.retsinformation.dk/eli/lta/2026/849 | 2026-10-23 |
| Selskabsskatteloven, LBK nr. 279 of 13 March 2025, §§ 1, stk. 6, and 2, stk. 2-4 | https://www.retsinformation.dk/eli/lta/2025/279 | 2026-10-23 |
| Skattekontrolloven, LBK nr. 12 of 8 January 2024, §§ 10, 11, 73, 74 | https://www.retsinformation.dk/eli/lta/2024/12 | 2026-10-23 |
| Lov nr. 16 of 14 January 2025 (SKL § 73 amounts doubled) | https://www.retsinformation.dk/eli/lta/2025/16 | 2026-10-23 |
| Lov nr. 1691 of 30 December 2024, § 6, nr. 1 (KSL § 48 E pay base DKK 47,600) and § 9, stk. 5 (effect from income year 2026) | https://www.retsinformation.dk/eli/lta/2024/1691 | 2026-10-23 |
| Lov nr. 1648 of 16 December 2025, § 20 (KSL § 48 renumbered from 1 January 2026) | https://www.retsinformation.dk/eli/lta/2025/1648 | 2026-10-23 |
| Skattestyrelsen, SKM2025.720.SKTST, Opkrævningsloven § 7, stk. 2 rate for 2026 | https://info.skat.dk/data.aspx?oid=2459995 | 2026-10-23 |
| Skatte- og Vækstministeriet, rates in Kildeskatteloven 2026 and 2027 (page dated 14 September 2026) | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven | 2026-10-23 |
| Skatte- og Vækstministeriet, rates in Personskatteloven 2026 | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/personskatteloven | 2026-10-23 |
| Den juridiske vejledning 2026-2, C.F.6 Forskerskatteordningen | https://info.skat.dk/data.aspx?oid=1977257 | 2026-10-23 |
| Den juridiske vejledning 2026-2, C.F.6.1.1 personkreds and period | https://info.skat.dk/data.aspx?oid=1977284 | 2026-10-23 |
| Den juridiske vejledning 2026-2, C.F.6.1.3 prior tax liability | https://info.skat.dk/data.aspx?oid=1977286 | 2026-10-23 |
| Den juridiske vejledning 2026-2, C.F.6.1.4 minimum pay | https://info.skat.dk/data.aspx?oid=1977289 | 2026-10-23 |
| Skattestyrelsen, Tax liability (full and limited, commuters, box 69) | https://skat.dk/en-us/individuals/taxation-in-denmark/tax-liability | 2026-10-23 |
| Skattestyrelsen, Claiming refund of Danish dividend tax | https://skat.dk/en-us/businesses/companies-and-foundations/companies-and-foundations/declaring-and-paying-dividends-and-dividend-tax/claiming-refund-of-danish-dividend-tax | 2026-10-23 |
| Skattestyrelsen, SKM2025.716.SKTST, interest rates on residual tax for income year 2025 | https://info.skat.dk/data.aspx?oid=2460000 | 2026-10-23 |

Not yet confirmed: the income year 2026 day-to-day interest and residual-tax surcharge rates (Skattestyrelsen publishes them in December 2026; the 2025 rates are shown); country-by-country treaty rates for dividends and royalties; any 2026 amendment to Ligningsloven §§ 33 and 33 A after the November 2025 consolidation.

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
