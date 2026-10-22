---
name: be-corporate-tax
description: "Belgian corporate income tax (vennootschapsbelasting / impôt des sociétés) for income year 2026 (assessment year 2027): companies resident in Belgium and Belgian permanent establishments of foreign companies (belasting niet-inwoners). Covers the 25% rate and the 20% small-company rate on the first EUR 100,000 with the 2026 director pay test (EUR 51,000), the 20% cap on flat-rate benefits in kind, the taxable base, the dividends received deduction, the capital gains exemption on shares, the 70% basket rule above EUR 1m, loss carry-forward, the group contribution, the interest limit, advance payments and the 6.75% increase, Biztax filing, penalties, 30% withholding and the parent-subsidiary exemption. Trigger on: vennootschapsbelasting, VenB, impôt des sociétés, ISoc, verlaagd tarief, bedrijfsleidersbezoldiging, DBI, RDT, korf, groepsbijdrage, voorafbetalingen, Biztax, roerende voorheffing. Out of scope: be-income-tax, be-capital-gains, belgium-payroll, be-vat-return, belgium-financial-statements."
jurisdiction: BE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Belgian corporate income tax (vennootschapsbelasting): income year 2026

> **General reference only.** This skill is a source-cited draft. No accountant has reviewed it. Do not rely on it to file, pay or take a tax position without review by a qualified Belgian tax adviser (belastingadviseur / conseiller fiscal).

Belgium names a tax year after the year in which the tax is assessed. Profit of a financial year that closes in 2026 is taxed in **assessment year (aanslagjaar) 2027**. This skill uses the Income Tax Code (WIB 92) text that FisconetPlus publishes as "WIB 92 - Inkomsten 2026", which is the text for assessment year 2027 ([FisconetPlus, WIB 92 income 2026](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2ebbd3f4-ca47-41f5-8f17-2a243befae75)). Article numbers below are WIB 92 unless stated otherwise.

**What changed for 2026, plainly.** The law of 15 July 2026 reforming personal income tax (Belgisch Staatsblad 29 July 2026) also changed corporate tax from assessment year 2027:

- the director pay needed for the 20% small-company rate is now a base of EUR 25,000, indexed each year; the indexed figure for assessment year 2027 is **EUR 51,000** (it was EUR 45,000 for assessment year 2026);
- a company loses the 20% rate if flat-rate benefits in kind given to its directors exceed 20% of their total pay;
- a separate 7.5% tax applies to the excess part of flat-rate benefits in kind given to employees.

Sources: [law of 15 July 2026, articles 76 to 88](https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2026-07-29&lg_txt=n&caller=sum&s_editie=1&2026005724=2&numac_search=2026005724&view_numac=); [art. 215 as consolidated for income 2026](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1). The programme law of 18 July 2025 had already tightened the dividends received deduction (see "The taxable base"). The law of 6 April 2026 introducing a tax on capital gains on financial assets is aimed at individuals; the income-2026 FisconetPlus text of art. 192 (capital gains exemption on shares) and art. 215 (rates) shows no amendment by it. See `be-capital-gains` for individuals.

## Who this applies to

- **Resident companies (vennootschapsbelasting).** A domestic company (binnenlandse vennootschap) is any company that has its principal establishment or its seat of management or administration in Belgium and is not excluded from corporate tax ([art. 2, § 1, 5°, b)](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2bfeec21-7e5f-4828-a283-cb99c56d41a1); [art. 179](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c3eb061b-8d91-426f-9712-823d3e40b341)). It is taxed on its worldwide profit, including distributed profit. A foreign-law company run from Belgium is resident; FOD Financiën does not open its tax file automatically and it must contact its tax office ([FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte)).
- **Foreign companies (belasting niet-inwoners/vennootschappen).** A foreign company without its principal establishment or seat of management in Belgium pays non-resident tax on Belgian income, mainly the profit of a Belgian establishment ([art. 227, 2°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1cc34fb6-e0a7-4839-97c3-ee2a1255c792)). The same rates apply, and for the 20% rate and the director pay test only the Belgian establishment's profit counts ([art. 246, 1°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2081260d-9fbe-401c-9a84-554b9d0188ba)). A treaty may narrow what counts as an establishment.
- **Out of scope here:**
  - Non-profit bodies and entities in sectors excluded by art. 181 and 182 pay legal-persons tax (rechtspersonenbelasting), not corporate tax ([FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte)).
  - Investment companies, regulated real estate companies and pension funds taxed under art. 185bis, tonnage-tax shipping companies and diamond traders have special regimes. Refer.
  - Sole traders and self-employed individuals: use `be-income-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Standard rate | 25% | Income 2026 (AY 2027); since AY 2021 | [art. 215, first paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1); [FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte) |
| Small-company rate | 20% on the first EUR 100,000 of taxable income; 25% above | Income 2026 | [art. 215, second paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1) |
| Director pay test for the 20% rate | At least one director must receive pay charged to the year's result of at least EUR 51,000 (indexed amount; base EUR 25,000), or at least equal to the company's taxable income if that is lower. Applies from the fifth taxable period after incorporation | Income 2026 (AY 2027) | [art. 215, third paragraph, 4°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1); [law of 15 July 2026, art. 80 and 88](https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2026-07-29&lg_txt=n&caller=sum&s_editie=1&2026005724=2&numac_search=2026005724&view_numac=) |
| Same test, previous year | EUR 45,000 or taxable income if lower | Income 2025 (AY 2026) | [FOD Financiën, notes to the AY 2026 return (PDF), p. 49](https://financien.belgium.be/sites/default/files/downloads/121-aangifte-venb-toelichting-2026.pdf) |
| Benefits-in-kind cap for the 20% rate | Reduced rate lost if flat-rate benefits in kind to directors exceed 20% of total director pay for the period | Income 2026 | [art. 215, third paragraph, 5°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1); [art. 2, § 1, 25°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2bfeec21-7e5f-4828-a283-cb99c56d41a1) |
| Separate tax on excess employee benefits in kind | 7.5% of the part above 20% of total employee pay | Income 2026 | [art. 219septies](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/613136be-62d7-41d5-a4ec-be3a2d339c91) |
| Other exclusions from the 20% rate | Company holds shares worth more than 50% of its paid-up capital (holdings of 75% or more ignored); 50% or more of its shares held by other companies; certain investment and real estate companies | Income 2026 | [art. 215, third paragraph, 1°, 2°, 6°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1) |
| Basket rule (korf) on carried-forward deductions | EUR 1,000,000 plus 70% of the remaining profit above EUR 1,000,000 | Income 2026; this text applies to periods starting on or after 1 January 2024 | [art. 207, fifth paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586) |
| Interest limitation | Net borrowing cost deductible up to the higher of EUR 3,000,000 or 30% of tax EBITDA | Income 2026 | [art. 198/1, § 3](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c0ee50c4-7f17-4e52-ac4e-56b5791eaa8d) |
| Dividends received deduction (DBI / RDT) | 100% of qualifying dividends deducted (holding of at least 10% or acquisition value of at least EUR 2,500,000, held one year) | Income 2026 | [art. 202](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db2358eb-2747-49c6-93a8-462927e4fc8f) |
| Innovation income deduction | 85% of qualifying net innovation income | Income 2026 | [art. 205/1, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0e0ea26c-f373-4711-87eb-7ef8dc073313) |
| Investment deduction (assets from 1 January 2025) | Basic 10% (small companies; 20% for digital assets); thematic 40% (small) or 30% (others); technology 13.5% or spread 20.5% | Income 2026 | [FOD Financiën, investeringsaftrek](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/belastingvoordelen/investeringsaftrek) |
| Increase for insufficient advance payments | 6.75% of the tax, reduced by 9.00% / 7.50% / 6.00% / 4.50% of each of the four advance payments | Income 2026 (AY 2027) | [FOD Financiën, voorafbetalingen](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorafbetalingen); [art. 218](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4497a4fa-744a-4885-a3d0-3c93ffc7e029) |
| Withholding tax (roerende voorheffing) on dividends, interest, royalties | 30% standard rate | 2026 | [art. 269, § 1, 1°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac); [FOD Financiën, roerende voorheffing](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorheffingen/roerende-voorheffing) |
| Late payment interest | 4% a year, per month started; not charged under EUR 5 a month | Current per FOD Financiën | [FOD Financiën, betaling](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling); [art. 414](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5) |
| Local or trade tax on company profit | None. Belgium has no municipal surcharge on corporate tax; the surcharge in `be-income-tax` is for individuals | 2026 | [art. 215](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1) sets the only rates |
| Pillar Two | Minimum rate 15%. Applies to Belgian entities of multinational or large domestic groups with annual consolidated revenue of EUR 750,000,000 or more in at least two of the four preceding reporting years. Law of 19 December 2023, in force 31 December 2023; this skill does not compute top-up tax | 2026 | [law of 19 December 2023, art. 3, 15° and art. 5, § 1](https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2023-12-28&lg_txt=n&caller=sum&s_editie=1&2023048529=1&numac_search=2023048529&view_numac=); [art. 207, ministerial notice quoted in the FisconetPlus text](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586) |

**Who is a small company.** "Small" means small under art. 1:24, §§ 1 to 6, of the Companies and Associations Code (WVV), or meeting the same criteria where that article does not apply ([notes to the AY 2026 return, definitions](https://financien.belgium.be/sites/default/files/downloads/121-aangifte-venb-toelichting-2026.pdf)). Read the client's WVV classification; do not guess it from turnover alone.

**The director pay test, worked out.** The test is per company, not per director: one director must receive at least EUR 51,000 charged to the 2026 result. If the best-paid director gets less than EUR 51,000, the 20% rate still applies when that pay is at least equal to the company's taxable income. Young companies are exempt for their first four taxable periods. Then the new benefits-in-kind cap is a separate condition: a company whose flat-rate benefits in kind to directors (for example a company car) are worth more than 20% of the total pay it gives its directors in the period still loses the 20% rate, even if the EUR 51,000 test is met ([art. 2, § 1, 25°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2bfeec21-7e5f-4828-a283-cb99c56d41a1)).

## The taxable base

The taxable base is the accounting profit in the annual accounts, adjusted by tax corrections, then reduced by exempt amounts and deductions ([FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte)).

1. **Start** from the accounting result before tax, including reserved profit and distributed profit.
2. **Add back disallowed expenses (verworpen uitgaven).** Example: fines, including administrative fines, are not deductible ([art. 53, 6°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/69b77d81-d360-48f5-a66c-fa9eee78daca)). Excess flat-rate benefits in kind are dealt with through the 20% rate test (directors) and the 7.5% separate tax (employees), not as an add-back in this skill.
3. **Interest limitation.** Net borrowing costs above the higher of EUR 3m or 30% of tax EBITDA are not deductible in the year. Interest between Belgian group companies is left out of the calculation, as are loans concluded before 17 June 2016 and not fundamentally changed ([art. 198/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c0ee50c4-7f17-4e52-ac4e-56b5791eaa8d)).
4. **Depreciation.** Assets are written off under the general depreciation rules of WIB 92. This skill does not cover rates per asset class.
5. **Take out exempt items and deductions, in the legal order** ([art. 206/5 and art. 207](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586)). First-order deductions come off the current profit without limit: the year's dividends received deduction, patent income deduction (old regime), the year's innovation income deduction, the investment deduction, and the group contribution.
6. **Dividends received deduction (DBI / RDT).** Qualifying dividends are deducted in full. On the date of payment the company must hold at least 10% of the payer's capital, or a holding with an acquisition value of at least EUR 2,500,000; the shares must be held in full ownership for at least one year; and the payer must meet the subject-to-tax conditions in art. 203 ([art. 202, § 2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db2358eb-2747-49c6-93a8-462927e4fc8f)). **New from AY 2026 (programme law of 18 July 2025):** for a company that is not small, the EUR 2,500,000 route only works if the holding is booked as financial fixed assets. An unused current-year deduction carries forward.
7. **Capital gains on shares** are fully exempt when the dividends on those shares would qualify for the dividends received deduction under art. 202 and 203 ([art. 192, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/34540b66-dab5-4f78-aec7-b578676a0112)). Earlier write-downs on the shares are taxed back first.
8. **Innovation income deduction**: 85% of qualifying innovation income, with carry-forward of the unused part ([art. 205/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0e0ea26c-f373-4711-87eb-7ef8dc073313)). **Investment deduction**: see the rates table; it comes after the innovation income deduction and before the group contribution among the first-order items, only against the Belgian profit left at that point ([art. 207, second paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586)), and the unused part carries forward with no time limit ([FOD Financiën, investeringsaftrek](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/belastingvoordelen/investeringsaftrek)).
9. **Group contribution (groepsbijdrage).** A loss-making company can take over profit from a linked profitable company. Link: a direct 90% capital holding either way, or both 90% held by the same company, continuously for five years from 1 January of the fourth year before the assessment year. A foreign party must be in the European Economic Area. The profitable company deducts the amount, the loss company reports it as profit, and the profitable company pays it a fee equal to the tax saved; the agreement (275 CTIG) is attached to the return. Excluded if either party is: a company that makes real property available to its directors or their spouse or children, an art. 185bis company, a tonnage-tax shipping company, a registered diamond trader, a company taxed on a flat-rate basis under art. 342, §§ 2 and 4, or (for a foreign party) a company on a special tax regime in its home state ([art. 205/5, § 2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/41995537-9114-4410-947f-98213373fffb)).
10. **Second-order deductions and the basket (korf).** Carried-forward dividends received deduction, carried-forward innovation deduction, tax losses brought forward and the old notional interest deduction come next. Together they are capped at **EUR 1,000,000 plus 70% of the profit above EUR 1,000,000** remaining after the first-order deductions ([art. 207, fifth paragraph](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586)). The capped-off part is not lost; it carries forward. A small company is exempt from the cap on its losses for its first four taxable periods (art. 207, sixth paragraph). The investment deduction carried forward is outside the basket.
11. **Losses.** Tax losses carry forward with no time limit ([art. 206, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ad34622a-3c3f-4aab-901f-6ec38172ee20)). There is no general carry-back; the only carry-back is for farm crop damage from bad weather recognised by a region (art. 206, § 4). Losses are cut proportionally after tax-neutral mergers and contributions (art. 206, § 2), and lost on a change of control not justified by legitimate financial or economic needs (art. 207, eighth paragraph).
12. **Group taxation.** Belgium has no fiscal unity. The group contribution in step 9 is the only way to use another company's profit or loss.

## Deadlines and filing

- **Return.** One corporate tax return (aangifte in de vennootschapsbelasting / déclaration à l'impôt des sociétés) per financial year, filed electronically through **Biztax**, also reachable through MyMinfin. Paper is allowed only with a yearly signed statement that the company or its agent lacks the IT means ([FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte); [Biztax](https://financien.belgium.be/nl/E-services/biztax)). Foreign companies file the non-resident companies return (BNI/ven) through the same channel.
- **Filing deadline.** The legal rule is the last day of the seventh month after the financial year closes; a weekend or holiday moves it to the next working day ([FOD Financiën, filing deadlines](https://financien.belgium.be/nl/E-services/biztax/indieningstermijnen-aangiften)). For AY 2026 (year-ends 31 December 2025 to 28 February 2026) the administration set 30 September 2026, then extended it to **15 October 2026** ([Biztax news, 25 September 2026](https://financien.belgium.be/nl/E-services/biztax)). The AY 2027 dates for a 31 December 2026 year-end were not yet published on 22 October 2026.
- **Advance payments (voorafbetalingen).** No legal duty to prepay, but a company that does not prepay enough pays the increase. For a calendar-year company and AY 2027, payments must reach the advance payments account by **10 April 2026, 10 July 2026, 12 October 2026 and 21 December 2026** ([FOD Financiën, voorafbetalingen](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorafbetalingen)). A payment that arrives late counts for the next quarter. Non-calendar years have their own dates. FOD Financiën suggests prepaying 102% of the expected tax less credits, split in four.
- **The increase (vermeerdering).** Base = tax on the year's income less creditable withholdings and credits. Increase = base x 6.75%, less 9.00% of VA1, 7.50% of VA2, 6.00% of VA3 and 4.50% of VA4. For companies the base rate used is never below 3% (6.75% = 2.25 x 3%), the 90% cap and the 106% uplift used for individuals do not apply, and companies never get a bonus for overpaying ([art. 218, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4497a4fa-744a-4885-a3d0-3c93ffc7e029); [FOD Financiën, voorafbetalingen](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorafbetalingen)). A small company owes no increase for its first three financial years ([art. 218, § 2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4497a4fa-744a-4885-a3d0-3c93ffc7e029)).
- **Change from 2027 income.** The law of 15 July 2026 makes the first-quarter window for individuals start on 21 February (art. 65). For companies, art. 72 sets a different window: a payment made from 21 December of the second year before the assessment year up to 10 April of the year before is multiplied by 3, the first-quarter factor. For a calendar 2027 company (AY 2028) that is 21 December 2026 to 10 April 2027. Both rules apply to advance payments for AY 2028 and later, not to 2026 ([law of 15 July 2026, art. 65, 72 and 73](https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2026-07-29&lg_txt=n&caller=sum&s_editie=1&2026005724=2&numac_search=2026005724&view_numac=)). Check the FOD Financiën page for the AY 2028 rates when published.
- **Final payment.** Tax not covered by prepayments and withholdings is assessed; the assessment notice must be paid within two months of being sent ([art. 413](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09b8ca93-c681-40df-9a8f-c5a947e063ae)), online through MyMinfin or by transfer to BE42 6792 0000 0054 with the structured reference ([FOD Financiën, betaling](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling)).
- **Withholding on distributions.** Withholding tax on dividends the company pays is declared (form 273A) and paid within 15 days of attribution or payment ([FOD Financiën, roerende voorheffing](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorheffingen/roerende-voorheffing)).

## Penalties and interest

- **Late, missing or wrong return: tax increase.** 10% to 200% of the tax on the income not declared or declared late, on a scale set by royal decree according to the nature and seriousness of the offence. No increase for a first offence in good faith. The increase only applies when the undeclared or late income reaches EUR 2,500, and tax plus increase cannot exceed the undeclared income ([art. 444](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0)).
- **Administrative fines.** EUR 50 to EUR 1,250 per breach of the Code, on a scale set by royal decree ([art. 445, § 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f)).
- **Late return, other effects.** The administration may assess ex officio (the company must then prove its figures) and has a longer period to reassess, in principle four years from 1 January of the assessment year for 31 December year-ends ([FOD Financiën, corporate tax return page](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte)).
- **Late payment interest.** Charged per calendar month on the unpaid amount rounded down to EUR 10, from the first day of the month after the due date; not charged when below EUR 5 a month ([art. 414](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5)). The rate follows the law of 5 May 1865 (art. 2, § 2/1); FOD Financiën gives it as 4% a year, unchanged since 1 January 2018 ([FOD Financiën, betaling](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling)).
- **Insufficient advance payments.** The 6.75% increase in "Deadlines and filing" is the sanction; it is not deductible.

## Cross-border points

- **Withholding on outbound dividends.** Standard rate 30% ([art. 269, § 1, 1°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac)). **Parent-subsidiary exemption:** no withholding on dividends paid by a Belgian subsidiary to a parent in another EU member state, or in a treaty state with exchange of information, if the parent holds at least 10% of the capital for an uninterrupted period of at least one year, has a legal form listed in the Directive 2011/96/EU annex (or a similar treaty-state form), is tax resident there and is subject to corporate tax without a special regime ([KB/WIB 92, art. 106, § 5 and § 6bis](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f160145d-45d4-435d-a65a-0e0914843b1d)). The same 10% and one-year test exempts dividends between Belgian companies (art. 106, § 6). A holding below 10% but with an acquisition value of at least EUR 2,500,000, held one year, can also be exempt for EEA or treaty-state parents when the withholding could not otherwise be credited or refunded; since 29 July 2025 a parent that is not small must book it as financial fixed assets ([art. 264/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4e011ee5-67f1-4e29-b5fe-109d60a93df2)).
- **Interest and royalties paid abroad.** Domestic withholding is 30% (art. 269, § 1, 1°). Treaties and the exemptions in the royal decree implementing WIB 92 can reduce or remove it; check the treaty and the payer's exemption file for each payment. Reduced rates for liquidation reserve dividends (5%, 6.5%, 9.8% or 20%) are in art. 269, § 1, 8°.
- **EU directives.** Parent-Subsidiary Directive: above. Anti-Tax Avoidance Directive: interest limitation (art. 198/1), CFC rules (art. 185/2), exit taxation (art. 185/1). Pillar Two: law of 19 December 2023.
- **CFC rules.** Belgium taxes the undistributed profit of a controlled foreign company, or of a foreign establishment of the company, when (1) the company with associated entities holds the majority of votes, at least 50% of the capital or a right to at least 50% of the profit, and (2) the foreign entity pays no income tax, or less than half the Belgian tax it would pay if it were Belgian. Low taxation is presumed for entities in the EU list of non-cooperative jurisdictions or the Belgian low-tax list. How much profit is included is set by § 2 ([art. 185/2](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/8784f2e1-6561-49f7-80aa-70c63994da21)).
- **Exit tax on companies.** Moving the principal establishment or seat of management abroad is treated as a liquidation, so hidden gains and reserves are taxed ([art. 210, § 1, 4°](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a3d38979-9797-4133-b830-bf716b9625de)). Transferring assets from Belgium to a foreign establishment whose profit is treaty-exempt also creates taxable profit ([art. 185/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5b1d6308-dd8a-48c3-a795-b9b84247c2d5)). For moves to another EU or EEA state with recovery assistance, the company can choose to pay one fifth at once and the rest in equal instalments over the next four years ([art. 413/1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501)).
- **Transfer pricing.** The arm's length rule (art. 185, § 2), abnormal advantages and the 275 MF / LF / CBC documentation are in `be-transfer-pricing`.

## Worked examples

### Example 1: trading NV, not a small company, profit EUR 800,000

A distribution NV, calendar financial year 2026, is not small under art. 1:24 WVV. Its profit before tax in the accounts is EUR 795,000, after a EUR 5,000 administrative fine was expensed. No dividends received, no losses brought forward, net interest well under EUR 3m. It made four equal advance payments of EUR 50,000 by the 2026 dates.

1. Add back the fine (art. 53, 6°): taxable income 795,000 + 5,000 = EUR 800,000.
2. Not small, so the 25% rate applies to the whole amount: EUR 200,000.
3. Increase for insufficient prepayments: 200,000 x 6.75% = EUR 13,500. Prepayment benefit: 50,000 x 9% + 50,000 x 7.5% + 50,000 x 6% + 50,000 x 4.5% = EUR 13,500. Net increase: nil. Four equal quarters covering the full tax always cancel the increase, because the four percentages average 6.75%.
4. Balance on assessment: 200,000 - 200,000 = nil.

```oa-check
name: Belgian NV, not small, taxable income EUR 800,000, income 2026 (AY 2027)
inputs:
  profit_before_tax: 795000
  fine: 5000
  va1: 50000
  va2: 50000
  va3: 50000
  va4: 50000
steps:
  - taxable: profit_before_tax + fine
  - tax: taxable * 0.25
  - increase_gross: tax * 0.0675
  - prepay_benefit: va1 * 0.09 + va2 * 0.075 + va3 * 0.06 + va4 * 0.045
  - increase: max(0, increase_gross - prepay_benefit)
  - prepaid: va1 + va2 + va3 + va4
  - balance_due: tax + increase - prepaid
expected:
  taxable: 800000
  tax: 200000
  increase_gross: 13500
  prepay_benefit: 13500
  increase: 0
  balance_due: 0
```

### Example 2: small BV, losses brought forward, the EUR 51,000 director pay test, late prepayments

A BV in its sixth financial year (calendar 2026) is small under art. 1:24 WVV. Its shares are held by two individuals; it holds no shares in other companies. Its taxable profit for 2026 before using losses is EUR 180,000. It has EUR 50,000 of tax losses brought forward. Its only director is paid EUR 60,000 charged to the 2026 result, with no benefits in kind. It made advance payments of EUR 10,000 in October and EUR 10,000 in December 2026 only.

1. **Losses and the basket.** The cap is EUR 1,000,000 plus 70% of profit above EUR 1,000,000. Profit is below EUR 1m, so all EUR 50,000 of losses can be used. Taxable income: EUR 130,000.
2. **20% rate test.** Small company, not 50% owned by companies, past its first four periods, director pay EUR 60,000 at least EUR 51,000, no benefits in kind over 20%. The reduced rate applies: 100,000 x 20% = EUR 20,000, plus 30,000 x 25% = EUR 7,500. Tax: EUR 27,500.
3. **The edge case.** Had the director been paid EUR 45,000, enough for AY 2026, the test would fail for 2026 income: EUR 45,000 is below EUR 51,000 and below taxable income of EUR 130,000. All income would be taxed at 25%, EUR 32,500, which is EUR 5,000 more.
4. **Increase.** 27,500 x 6.75% = EUR 1,856.25. Benefit: 10,000 x 6% + 10,000 x 4.5% = EUR 1,050. Increase: EUR 806.25. The company is past its first three financial years, so the start-up exemption does not apply.
5. **Balance on assessment:** 27,500 + 806.25 - 20,000 = EUR 8,306.25, payable within two months of the assessment notice.

```oa-check
name: Small Belgian BV, EUR 50,000 losses, director pay test, VA3 and VA4 only, income 2026
inputs:
  profit_before_losses: 180000
  losses_bf: 50000
  director_pay: 60000
  low_director_pay: 45000
  pay_threshold: 51000
  va3: 10000
  va4: 10000
steps:
  - basket_cap: 1000000 + max(profit_before_losses - 1000000, 0) * 0.70
  - loss_used: min(losses_bf, profit_before_losses, basket_cap)
  - taxable: profit_before_losses - loss_used
  - tax: min(taxable, 100000) * 0.20 + max(taxable - 100000, 0) * 0.25
  - tax_if_test_failed: taxable * 0.25
  - extra_if_test_failed: tax_if_test_failed - tax
  - increase_gross: tax * 0.0675
  - prepay_benefit: va3 * 0.06 + va4 * 0.045
  - increase: max(0, increase_gross - prepay_benefit)
  - balance_due: tax + increase - va3 - va4
expected:
  loss_used: 50000
  taxable: 130000
  tax: 27500
  tax_if_test_failed: 32500
  extra_if_test_failed: 5000
  increase_gross: 1856.25
  prepay_benefit: 1050
  increase: 806.25
  balance_due: 8306.25
```

## Ask the client first

1. **Is the company small under art. 1:24 WVV, and in which taxable period since incorporation is it?** This decides the 20% rate, the start-up exemptions from the increase (first three financial years) and from the director pay test (first four periods), and the basket exemption for losses.
2. **What did each director receive in 2026, charged to the 2026 result, and how much of it was flat-rate benefits in kind?** At least one director needs EUR 51,000 (or at least the taxable income), and benefits in kind above 20% of director pay cost the 20% rate.
3. **Who owns the company, and what shares does it hold?** 50% or more held by companies, or a share portfolio worth more than 50% of paid-up capital, excludes the 20% rate. Size, date and booking of each holding decide the dividends received deduction and the capital gains exemption.
4. **What advance payments were made, on which dates, and what is the financial year?** The increase depends on the quarter each payment arrived in.
5. **Are there losses, carried-forward deductions or a change of control?** The basket rule applies above EUR 1m, and an unjustified change of control wipes out carried-forward losses.
6. **Is there a 90% group company, a foreign establishment, or a foreign subsidiary in a low-tax country?** Group contribution, treaty exemption and CFC rules may apply.

## Sources

| Source | URL | Read on 2026-10-22 |
|---|---|---|
| Law of 15 July 2026 reforming personal income tax, Belgisch Staatsblad 29 July 2026 (numac 2026005724), titles 12 and 14 | https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2026-07-29&lg_txt=n&caller=sum&s_editie=1&2026005724=2&numac_search=2026005724&view_numac= | 2026-10-22 |
| Law of 19 December 2023 introducing a minimum tax for multinational and large domestic groups, Belgisch Staatsblad 28 December 2023 (numac 2023048529), art. 3 and 5 | https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2023-12-28&lg_txt=n&caller=sum&s_editie=1&2023048529=1&numac_search=2023048529&view_numac= | 2026-10-22 |
| FisconetPlus, WIB 92 income 2026 (table of contents) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2ebbd3f4-ca47-41f5-8f17-2a243befae75 | 2026-10-22 |
| WIB 92 art. 2 (definitions; excess benefits in kind) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2bfeec21-7e5f-4828-a283-cb99c56d41a1 | 2026-10-22 |
| WIB 92 art. 53 (non-deductible expenses) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/69b77d81-d360-48f5-a66c-fa9eee78daca | 2026-10-22 |
| WIB 92 art. 179 (who pays corporate tax) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c3eb061b-8d91-426f-9712-823d3e40b341 | 2026-10-22 |
| WIB 92 art. 185/1 (exit on asset transfer) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5b1d6308-dd8a-48c3-a795-b9b84247c2d5 | 2026-10-22 |
| WIB 92 art. 185/2 (CFC) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/8784f2e1-6561-49f7-80aa-70c63994da21 | 2026-10-22 |
| WIB 92 art. 192 (capital gains on shares) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/34540b66-dab5-4f78-aec7-b578676a0112 | 2026-10-22 |
| WIB 92 art. 198/1 (interest limitation) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c0ee50c4-7f17-4e52-ac4e-56b5791eaa8d | 2026-10-22 |
| WIB 92 art. 202 (dividends received deduction) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db2358eb-2747-49c6-93a8-462927e4fc8f | 2026-10-22 |
| WIB 92 art. 205/1 (innovation income deduction) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0e0ea26c-f373-4711-87eb-7ef8dc073313 | 2026-10-22 |
| WIB 92 art. 205/5 (group contribution) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/41995537-9114-4410-947f-98213373fffb | 2026-10-22 |
| WIB 92 art. 206 (losses) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ad34622a-3c3f-4aab-901f-6ec38172ee20 | 2026-10-22 |
| WIB 92 art. 207 (order of deductions, basket) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c5cbf033-a4dc-40d9-8848-4ed87bbb5586 | 2026-10-22 |
| WIB 92 art. 210 (deemed liquidation, seat moved abroad) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a3d38979-9797-4133-b830-bf716b9625de | 2026-10-22 |
| WIB 92 art. 215 (rates, small-company rate, director pay test) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1 | 2026-10-22 |
| WIB 92 art. 218 (increase for insufficient prepayments) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4497a4fa-744a-4885-a3d0-3c93ffc7e029 | 2026-10-22 |
| WIB 92 art. 219septies (7.5% separate tax) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/613136be-62d7-41d5-a4ec-be3a2d339c91 | 2026-10-22 |
| WIB 92 art. 227 (non-resident taxpayers) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/1cc34fb6-e0a7-4839-97c3-ee2a1255c792 | 2026-10-22 |
| WIB 92 art. 246 (non-resident company rates) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2081260d-9fbe-401c-9a84-554b9d0188ba | 2026-10-22 |
| WIB 92 art. 264/1 (withholding exemption, holdings under 10%) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4e011ee5-67f1-4e29-b5fe-109d60a93df2 | 2026-10-22 |
| WIB 92 art. 269 (withholding tax rates) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac | 2026-10-22 |
| WIB 92 art. 413 (payment within two months) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09b8ca93-c681-40df-9a8f-c5a947e063ae | 2026-10-22 |
| WIB 92 art. 413/1 (exit tax instalments) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501 | 2026-10-22 |
| WIB 92 art. 414 (late payment interest) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5 | 2026-10-22 |
| WIB 92 art. 444 (tax increases) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-22 |
| WIB 92 art. 445 (administrative fines) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f | 2026-10-22 |
| KB/WIB 92 art. 106 (dividend withholding exemptions, parent-subsidiary) | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f160145d-45d4-435d-a65a-0e0914843b1d | 2026-10-22 |
| FOD Financiën, aangifte in de vennootschapsbelasting (rate, base, Biztax, late filing) | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/aangifte | 2026-10-22 |
| FOD Financiën, toelichting bij de aangifte VenB, aanslagjaar 2026 (PDF) | https://financien.belgium.be/sites/default/files/downloads/121-aangifte-venb-toelichting-2026.pdf | 2026-10-22 |
| FOD Financiën, voorafbetalingen (AY 2027 dates and rates) | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorafbetalingen | 2026-10-22 |
| FOD Financiën, indieningstermijnen aangiften | https://financien.belgium.be/nl/E-services/biztax/indieningstermijnen-aangiften | 2026-10-22 |
| FOD Financiën, Biztax (news on the AY 2026 deadline) | https://financien.belgium.be/nl/E-services/biztax | 2026-10-22 |
| FOD Financiën, vennootschapsbelasting betalen (late payment interest) | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling | 2026-10-22 |
| FOD Financiën, roerende voorheffing | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/voorheffingen/roerende-voorheffing | 2026-10-22 |
| FOD Financiën, investeringsaftrek | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/belastingvoordelen/investeringsaftrek | 2026-10-22 |

Not yet confirmed: the Biztax filing deadline for AY 2027 (31 December 2026 year-ends), not published on 22 October 2026; the exact periods to which the earlier temporary 40% basket share applied (the 70% text in force for 2026 was confirmed, the 40% history was not); the size thresholds of art. 1:24 WVV (the FOD Financiën advance payments page shows EUR 9,000,000 turnover and EUR 4,500,000 balance sheet, which may be out of date, so this skill does not rely on them); and the AY 2028 advance payment percentages that follow from the law of 15 July 2026.
