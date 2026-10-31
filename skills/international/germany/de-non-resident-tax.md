---
name: de-non-resident-tax
description: "Use this skill when a person or company that does not live in Germany has German income, or when a German resident needs credit for foreign tax. Tax year 2026. Covers unlimited vs limited liability (§ 1 EStG, §§ 8, 9 AO), the § 1(3) option (90% or EUR 12,348 test), § 1a EU/EEA splitting, German-source income under § 49 EStG, how a non-resident is assessed (§ 50: Grundfreibetrag added back, no splitting), wage tax for non-resident employees, § 50a withholding (15%, 30% on supervisory board fees), § 50c exemption and refund at the BZSt, Kapitalertragsteuer on dividends, and the § 34c and § 32d(5) foreign tax credits. Trigger on: beschränkte Steuerpflicht, non-resident Germany, § 1 Abs. 3 EStG, § 50a, Abzugsteuer, Kapitalertragsteuer Erstattung, Anrechnung ausländischer Steuer. Out of scope: rental computation (de-rental-income), resident employees (de-employee-income-tax), payroll mechanics (de-payroll), corporate tax (de-corporate-tax), exit tax (leaving-germany-exit-tax), Swiss commuters (germany-to-switzerland-cross-border-tax)."
version: 0.3
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-29
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany: non-residents with German income, and foreign tax credits, tax year 2026

This skill decides whether a person is taxed in Germany on worldwide income or only on German income, then works out how the German income is taxed: by assessment, by wage tax, or by a flat withholding. It also covers the reverse case: a German resident with foreign income who wants credit for the foreign tax.

See also, and do not repeat here:

- **de-employee-income-tax**: the 2026 tariff, Werbungskosten and special expenses for a resident employee. The tariff formula there is the one used below.
- **de-rental-income**: how to compute the rental result (AfA, Werbungskosten, Anlage V). A non-resident landlord computes it the same way.
- **de-capital-gains**: the flat tax on investment income, the Sparer-Pauschbetrag and the loss pots.
- **de-payroll**: running wage tax for an employee, including tax class I.
- **de-corporate-tax**: corporate tax at 15%, also for the German permanent establishment of a foreign company.
- **leaving-germany-exit-tax**: shareholders who move out, and extended limited liability after a move to a low-tax country (§ 2 AStG).
- **germany-to-switzerland-cross-border-tax**: Swiss commuters and moves to Switzerland.
- **de-treaty-withholding-rates**: treaty withholding rates by country, § 43b, § 50g and § 50d(3).

## Who this applies to

**Unlimited liability (§ 1(1) EStG).** A person with a residence (Wohnsitz) or habitual abode (gewöhnlicher Aufenthalt) in Germany is taxed on worldwide income.

- **Residence (§ 8 AO):** a home the person keeps and uses, in circumstances showing they will keep and use it. A flat kept available in Germany is enough, even if the person spends most of the year abroad.
- **Habitual abode (§ 9 AO):** staying in a way that shows the stay is not just temporary. A continuous stay of more than six months always counts, from the first day; short breaks are ignored. The six-month rule does not apply to a purely private stay (visit, holiday, cure) of up to one year (§ 9 sentence 3 AO).
- **German state employees abroad (§ 1(2) EStG):** German nationals paid from a German public purse, taxed abroad only like non-residents, stay fully liable.

**Limited liability (§ 1(4) EStG).** A person with neither residence nor habitual abode in Germany is taxed only on German-source income listed in § 49 EStG.

**The § 1(3) option.** A non-resident can apply to be treated as fully liable for their German income if, in the calendar year, either:

- at least 90% of their total income is subject to German income tax, or
- the income not subject to German tax is no more than the Grundfreibetrag, EUR 12,348 for 2026. The amount is cut to ¾, ½ or ¼ for residents of lower-cost countries (BMF country groups; Austria and most of Western Europe are in group 1, full amount).

German income that a tax treaty limits to a reduced rate (for example dividends) counts as not subject to German tax for the test (§ 1(3) sentence 3). The foreign income must be shown by a certificate from the foreign tax authority (§ 1(3) sentence 5). § 50a withholding still applies (§ 1(3) sentence 6).

**§ 1a EStG, EU/EEA nationals.** An EU or EEA national who is fully liable under § 1(1) or treated so under § 1(3) can have a spouse who lives in another EU/EEA state treated as fully liable, so the couple gets joint assessment and splitting. For the § 1(3) test the income of both spouses counts and the Grundfreibetrag is doubled to EUR 24,696 (§ 1a(1) no. 2). A non-EU/EEA national under § 1(3) gets the Grundfreibetrag but not splitting.

**Companies.** A company with neither its seat nor its place of management in Germany has limited corporate tax liability on its German income (§ 2 no. 1 KStG). Income settled by withholding is final unless it belongs to a German business (§ 32(1) KStG). A German permanent establishment is assessed at the 15% corporate rate (§ 23 KStG; see de-corporate-tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Grundfreibetrag (basic allowance) | EUR 12,348 | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 2026 tariff, zone 3 (taxable EUR 17,800 to 69,878) | (173.10 × z + 2,397) × z + 1,034.87, z = (taxable − 17,799) / 10,000; full tariff in de-employee-income-tax | 2026 | Same |
| Non-resident assessment | Tariff applied to taxable income plus EUR 12,348; for German employment income the add-back is only the part of EUR 12,348 above that income (net of allowed deductions) | 2026 | https://www.gesetze-im-internet.de/estg/__50.html (§ 50(1) sentence 2) |
| § 1(3) test | German-taxed income at least 90% of total, or non-German income at most EUR 12,348 (scaled by country group) | 2026 | https://www.gesetze-im-internet.de/estg/__1.html |
| § 1a test for a couple | Both spouses' income; non-German income at most EUR 24,696 | 2026 | https://www.gesetze-im-internet.de/estg/__1a.html |
| Country groups (Ländergruppen) | Group 1 full amount, group 2 ¾, group 3 ½, group 4 ¼ | From 2025, until replaced | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-12-02-beruecks-auslaendischer-verhaeltnisse.pdf |
| § 50a withholding: artists, athletes, entertainers, royalties | 15% of gross receipts | 2026 | https://www.gesetze-im-internet.de/estg/__50a.html (§ 50a(2)) |
| § 50a withholding: supervisory board fees | 30% of gross receipts | 2026 | Same |
| § 50a, net basis for eligible EU/EEA creditors | Only § 50a(1) nos. 1, 2 and 4, not royalties under no. 3: 30% for individuals, 15% for eligible companies, on net receipts after proven directly related costs | 2026 | Same, § 50a(3) |
| § 50a small performances | No withholding if receipts per performance are no more than EUR 250 | 2026 | Same, § 50a(2) sentence 3 |
| § 50a ordered by the tax office | 25% of gross (15% for companies) | 2026 | Same, § 50a(7) |
| Solidarity surcharge on § 50a and Kapitalertragsteuer | 5.5% of the tax withheld | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html (§ 3(1) nos. 5, 6) and __4.html |
| Kapitalertragsteuer on dividends | 25% plus 5.5% surcharge (26.375% in total) | 2026 | https://www.gesetze-im-internet.de/estg/__43a.html; BZSt page in Sources |
| Refund for a foreign company with limited corporate tax liability | Two fifths of the Kapitalertragsteuer withheld; further treaty or directive claims are not affected | 2026 | https://www.gesetze-im-internet.de/estg/__44a.html (§ 44a(9)) |
| § 50c exemption for small royalties | Payer need not withhold where a treaty bars German tax and royalties from that payer in the year stay at or below EUR 10,000 | 2026 | https://www.gesetze-im-internet.de/estg/__50c.html (§ 50c(2) no. 2) |
| § 50c refund deadline | Four years from the end of the year of receipt; not before one year after the tax was paid, nor before any longer treaty period | 2026 | Same, § 50c(3) sentence 2 |
| Flat tax on a resident's capital income | 25%, less foreign tax capped at 25% of each item and at the German tax on it | 2026 | https://www.gesetze-im-internet.de/estg/__32d.html (§ 32d(1), (5)) |
| Solidarity surcharge threshold, assessment | None while income tax is at most EUR 20,350 (EUR 40,700 joint); always 5.5% on § 32d(3) and (4) tax | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__3.html |

## The taxable base

### Step 1: is the income German-source? (§ 49 EStG)

The common cases:

| Income | German-source when | § 49(1) |
|---|---|---|
| Business profits | There is a permanent establishment or a permanent representative in Germany | no. 2(a) |
| Artists, athletes, entertainers | The performance takes place or is exploited in Germany, whoever receives the money | no. 2(d), 3, 9 |
| Sale of shares in a company | The conditions of § 17 apply and the company has its seat or management in Germany; or the property-company branch applies: at some time in the 365 days before disposal, more than 50% of the share value rested directly or indirectly on German immovable property and the shares were attributable to the seller at that time. For that percentage, use the active business assets at the book values that would have applied at that time, rather than market values. The separate statutory restructuring branch and treaty override must also be tested where relevant. | no. 2(e)(aa)–(cc) |
| Self-employed work | Performed or exploited in Germany, or a fixed base in Germany | no. 3 |
| Employment | Work done in Germany; or pay from a German public purse; or pay as managing director (Geschäftsführer), Prokurist or board member of a company managed in Germany | no. 4(a), (b), (c) |
| Dividends | The paying company has its seat or management in Germany | no. 5(a) |
| Rent | Domestic location, domestic registration or exploitation in a German permanent establishment or other facility, within the property/right categories in no. 6. For other rights whose only domestic link is registration in a German public book or register, no. 6 excludes the income if the rental is between parties not related under § 1(2) AStG, or applicable treaty provisions, taking account of the Act's treaty-application rules, oppose taxation. An actual domestic location or exploitation link must be tested separately. | no. 6 |
| Sale of German land | Privately held: inside the ten-year period of § 23 EStG (no. 8). Held in a business, or by a foreign company: always, with no time limit (no. 2(f)) | no. 8, no. 2(f) |
| German pensions | Paid by a German statutory pension fund, insurer or pension scheme | no. 7 |

For business rental or disposal of other rights under § 49(1) no. 2(f), apply its corresponding registry-only exception: where registration is the sole domestic source link, income is excluded if the parties are not related under § 1(2) AStG, or the applicable treaty, with the Act's treaty-application rules, opposes taxation. This does not exempt German land or override a different domestic source link. A property-company separator: German real-estate active book assets of EUR 40 and other active book assets of EUR 60 fail the strict more-than-50% test even if the property's market value is EUR 90. Book assets of EUR 60 and EUR 40 pass that percentage test only if the seller-attribution and relevant-time conditions also hold; the separate § 17 and treaty tests still apply.

Ordinary interest from a German bank account or a listed bond is not on the list (§ 49(1) no. 5(c) covers only loans secured on German land and certain profit-participation rights, and no. 5(d) only over-the-counter coupon payments), so a non-resident is not taxed on it.

### Step 2: is the tax settled by withholding? (§ 50(2) EStG)

For a person remaining subject to limited liability, income subject to wage tax, Kapitalertragsteuer or § 50a withholding is generally settled by that withholding. Test all the exceptions in § 50(2) sentence 2 before treating it as final:

- income of a German business (permanent establishment);
- German employment income under § 49(1) no. 4 where a § 39a(4) allowance was entered and annual pay exceeds the Grundfreibetrag plus the employee and special-expense lump sums (no. 4(a)); an application under § 46(2) no. 8 (no. 4(b)); or the § 46(2) nos. 2, 5 and 5a cases (no. 4(c));
- employment applications connected with extraordinary income under § 34(1) and (2) nos. 2 and 4 (no. 4(d)), or an application for a foreign-tax credit under § 50d(7) sentence 2 (no. 4(e)); these have their own gates, rather than no. 4(b)'s nationality/residence restriction;
- income under § 50a(1) nos. 1, 2 and 4 on application (no. 5; assessed by the BZSt);
- a later finding that the conditions for full liability under § 1(2), § 1(3) or § 1a were not met (no. 2), or the mixed-year case under § 2(7) sentence 3 (no. 3);
- the specified life-insurance capital income under § 49(1) no. 5 sentence 1(a), to which § 20(1) no. 6 sentence 2 applies, on application (no. 6).

The EU/EEA nationality and residence restriction in § 50(2) sentence 7 applies to no. 4(b) and no. 5. Sentence 8 additionally extends no. 4(b) to the specified EU/EEA nationals resident in Switzerland and Swiss nationals resident in the EU or Switzerland. It is not a general restriction on no. 4(d), no. 4(e) or no. 6. For no. 4 employment cases use the competent employer's Betriebsstättenfinanzamt under sentences 3–6; for no. 6 use the debtor's income-tax office under sentence 10. The referred special-tariff, insurance and credit computations are not supplied by this assessment-gate list. A person actually qualifying for full liability under § 1(3) or § 1a follows that full-liability route instead.

Income with no withholding, such as rent, a German business or a sale of German land, is always assessed.

### Step 3: the assessment of a non-resident (§ 50(1) EStG)

1. **Income.** Compute each type as for a resident. Business expenses and Werbungskosten count only if they relate to the German income.
2. **No personal deductions.** Special expenses, the EUR 36 lump sum, single-parent relief, child allowances, extraordinary burdens and § 35a credits do not apply (§ 50(1) sentence 4). There is no splitting. Exception under § 50(1a): mandatory contributions to a professional pension institution can qualify where membership arises from the admission required for the German professional practice. It covers EU/EEA nationals resident in the EU/EEA or Switzerland, and Swiss nationals resident in the EU or Switzerland. Contributions must directly relate to German income under § 49(1) no. 2 or 3 from that admitted practice; the deduction follows German qualifying income divided by the total positive German and foreign income from that practice. It is excluded to the extent already deducted in the residence state or exceeding the German qualifying income.
3. **Employees are the exception.** For employment income under § 49(1) no. 4, pension and health insurance contributions and the EUR 36 lump sum are allowed, for the period of the German employment and up to that employment income (§ 50(1) sentence 5). The employee lump sum (EUR 1,230, § 9a) is a Werbungskosten lump sum and applies anyway; it and the EUR 36 are cut pro rata for part-year work (§ 50(1) sentence 6).
4. **Grundfreibetrag added back.** Apply the tariff to taxable income plus EUR 12,348. For employment income, add only the part of EUR 12,348 above the employment income less allowed deductions. In effect a non-resident employee keeps the allowance on wages; a landlord or business owner does not.
5. **Solidarity surcharge.** Establish the assessment base under § 3 SolzG; it is not automatically the unadjusted income-tax amount. For an ordinary single assessment with no § 32d(3) or (4) tax component, it is zero when that base is at most EUR 20,350. Above that threshold, take the smaller of 5.5% of the base and 11.9% of the excess over EUR 20,350, dropping fractions of a cent (§§ 3(3), 4 SolzG). A stipulated base of EUR 20,400 gives min(EUR 1,122, EUR 5.95) = EUR 5.95. The separate § 32d(3)/(4) component and the withholding branches retain their own 5.5% treatment and do not receive this ordinary threshold/cap.

### Step 4: the § 1(3) assessment instead

The person is taxed as a resident on their German income: Grundfreibetrag, special expenses, the EUR 36 lump sum and the resident deductions apply. Income that is not subject to German tax is left out of the base but raises the rate (progression, § 32b(1) no. 5 EStG): the tax rate is found on taxable income plus that foreign income, then applied to taxable income alone. Splitting needs § 1a. Foreign capital income is a special case: § 2(5b) EStG keeps capital income under § 32d(1) out of "income" wherever the law refers to it, and whether foreign interest or dividends of a § 1(3) applicant count in the 90% test and in the progression is not settled here (see Not yet confirmed).

### Wage tax for non-resident employees

- Non-resident employees are in tax class I (§ 38b(1) no. 1(b) EStG), unless treated as fully liable under § 1(3) or § 1a.
- The employer's Betriebsstättenfinanzamt (the tax office for the place of business), not a residence office, sets and changes their wage tax data and issues the tax ID (§ 39(2) sentence 2 and § 39(3) EStG).
- A § 1(3) or § 1a employee with wage tax data set this way must file (§ 46(2) no. 7(b) EStG). An employee who wants § 1(3) treatment only in the assessment applies with a return (§ 46(2) no. 9), at the employer's Betriebsstättenfinanzamt.

### § 50a withholding (artists, athletes, royalties, supervisory boards)

- The German payer withholds when the payment is made: 15% of gross, 30% for supervisory board fees, plus 5.5% surcharge on the tax. Travel and hotel costs the payer refunds count as receipts only above actual cost and the per diem lump sums.
- For § 50a(1) nos. 1, 2 and 4 only, the payer may deduct directly related costs proved in a form the BZSt can check or paid by the payer, then withhold 30% for an EU/EEA national resident in the EU/EEA, or 15% for a company meeting § 32(4) KStG. This net route does not apply to royalties under § 50a(1) no. 3 (§ 50a(3)).
- The payer files the withholding return with the BZSt by the 10th of the month after each calendar quarter and pays it over (§ 50a(5)). It must file even when nothing is withheld. The payer is liable for tax not withheld; the creditor can also be pursued.
- On request the payer issues a certificate of the tax withheld (§ 50a(5) sentence 7). The creditor needs it for a refund.

### Treaty relief: exemption and refund (§ 50c EStG)

- The payer withholds in full even when a treaty limits German tax, unless the creditor holds an exemption certificate (Freistellungsbescheinigung) from the BZSt (§ 50c(1), (2)). For dividends, a treaty exemption certificate is given only to a company holding at least 10% of a German company.
- Small royalties: where a treaty bars German tax and the year's royalties from that payer stay at or below EUR 10,000, the payer need not withhold (§ 50c(2) no. 2), but must still file the withholding return.
- Refund: the creditor applies to the BZSt, electronically, within four years from the end of the year of receipt, with a residence certificate from their own tax authority and the payer's tax certificate (§ 50c(3), (5)). The BZSt warns that refunds can take more than 20 months.
- Companies: § 50d(3) denies relief to the stated extent where both conditions hold: participating or constitutionally benefited persons would not have the entitlement if they earned the income directly, and the income source has no substantial connection with the entity's economic activity. Merely receiving or passing on the income, or activity through a business operation not adequately equipped for its purpose, is not economic activity for this test. The denial does not apply to the extent the entity proves that obtaining a tax advantage was not one of the main purposes of its interposition, or where its main class of shares is substantially and regularly traded on a recognised exchange. § 42 AO remains applicable. Lack of other economic activity alone does not displace an established statutory rebuttal; neither rebuttal nor listing creates an entitlement without the other relief conditions.

### Kapitalertragsteuer on dividends to non-residents

The German company withholds 25% plus 5.5% surcharge, 26.375% in all, whoever the shareholder is. For a non-resident shareholder without a German business, that settles the German tax. The excess over the treaty rate is reclaimed from the BZSt under § 50c(3). Example: a treaty limit of 15% gives a refund of 26.375% − 15% = 11.375% of the gross dividend. For a capital-income creditor that is a corporation subject to limited liability within § 2 no. 1 KStG, § 44a(9) provides a refund of two fifths of the Kapitalertragsteuer actually withheld and remitted. This incorporates the application/procedure in § 50c(3) and (5) and the anti-abuse test and exceptions in § 50d(3); it is not an unconditional refund for every foreign company. Further statutory or treaty relief claims remain separate. The treaty rate itself depends on the treaty; see de-treaty-withholding-rates for the rates by country.

### Foreign tax credit for residents (§ 34c and § 32d(5) EStG)

Which rule applies depends on the income:

- **Capital income under the flat tax (§ 32d(1)), such as foreign dividends and interest of a private investor.** § 34c does not apply (§ 34c(1) sentence 1, second half). The foreign tax is credited under § 32d(5): at most 25% of each item, and at most the German tax on the capital income. The flat tax is then (e − 4q) / 4 without church tax, where e is the capital income after the Sparer-Pauschbetrag and q the creditable foreign tax (§ 32d(1) sentence 4). Income that had no German Kapitalertragsteuer, for example through a foreign broker, is declared in the return (§ 32d(3)).
- **Other foreign income taxed at the tariff (for example foreign rent, foreign business income).** § 34c(1) applies where no treaty exists; where a treaty provides for a credit, § 34c(6) applies the same method. Capital income assessed under the § 32d(6) Günstigerprüfung instead keeps the § 32d(5) credit, capped at the additional tariff tax on that capital income (§ 32d(6) sentence 2). For income within § 34c, the foreign tax is credited up to the German tax on that income:

  credit cap = German tariff tax × foreign income from that country / taxable income (sentence 2: the average rate on the whole taxable income, applied to the foreign income).

  Foreign tax above the cap is lost. Only tax that was set, paid and reduced by any refund due abroad counts. Instead of the credit the taxpayer can deduct the foreign tax from the income (§ 34c(2)).
- **Income a treaty exempts in Germany** (often foreign employment income or foreign rent): no credit, but it raises the rate under § 32b(1) no. 3. Exception: rent from property in another EU/EEA state, and profits of an EU/EEA permanent establishment that fails the active-business test of § 2a(2), do not raise the rate (§ 32b(1) sentence 2).

What counts as foreign income is set out in § 34d EStG.

## Deadlines and filing

| Step | Rule |
|---|---|
| Who files | A non-resident with German income not settled by withholding (rent, a German business, sale of German land), or who applies for an assessment (§ 1(3), refunds of wage tax, § 50a net assessment). Return under § 25(3) EStG |
| Competent tax office | For a non-resident: the office where the German assets are, or the most valuable part; failing that, where the activity is mainly carried on (§ 19(2) AO). Employees under § 1(3) or § 50(2) no. 4: the employer's Betriebsstättenfinanzamt (§ 46(2) nos. 7, 9; § 50(2) sentences 3 to 6 EStG). § 50a net assessments: the BZSt (§ 50(2) sentence 9) |
| Pensions from Germany | A non-resident whose only German income is pensions under § 49(1) nos. 7 and 10: Finanzamt Neubrandenburg, also where such a person applies under § 1(3) (§ 19(6) AO; § 1 EStZustV) |
| Own return, 2026 | 31 July 2027, a Saturday, so Monday 2 August 2027 (§ 149(2), § 108(3) AO) |
| With a tax adviser, 2026 | 29 February 2028 (§ 149(3) AO) |
| § 50a withholding return (payer) | By the 10th of the month after each calendar quarter, to the BZSt (§ 50a(5)) |
| § 50c refund | Four years from the end of the year the payment was received (§ 50c(3)) |
| Electronic filing | Compulsory where there is business or self-employed income (§ 25(4) EStG) |

## Penalties and interest

- **Late filing surcharge (§ 152 AO).** 0.25% per started month of the tax less prepayments and withholding, at least EUR 25 per month, at most EUR 25,000. It is compulsory if the return is not filed within 14 months after the end of the year (for 2026: by 29 February 2028), unless an extension was granted, the tax is nil or negative, or the tax does not exceed prepayments and withholding (§ 152(2), (3) AO).
- **Interest (§ 233a, § 238 AO).** 0.15% per full month (1.8% a year) on the balance, from 15 months after year end: from 1 April 2028 for 2026.
- **Late payment (§ 240 AO).** 1% per started month on the overdue tax rounded down to EUR 50.
- **§ 50a payer.** The payer is liable for tax it did not withhold or pay over (§ 50a(5) sentence 5). The creditor can also be pursued.

## Cross-border points

- **Treaties override.** A treaty can take away Germany's right to tax (for example employment income under the 183-day rule) or cap it (dividends, royalties). Withholding still happens first; relief is by exemption certificate or refund (§ 50c).
- **Moving in or out during the year.** A person who is fully liable for part of the year is assessed once; foreign income of the non-resident months raises the rate (§ 2(7), § 32b(1) no. 2 EStG). Not set out further here.
- **Leaving with shares.** See leaving-germany-exit-tax, including extended limited liability under § 2 AStG after a move to a low-tax country.
- **VAT.** A non-resident letting German property or performing in Germany may also have German VAT duties. Not covered here; see germany-vat-return.
- **Church tax.** Not dealt with here; it is set by state law.

## Worked examples

### Example 1: Austrian resident with a German rental flat

Anna lives in Vienna and has no home in Germany. Her German flat produces a rental result of EUR 24,000 for 2026, computed as in de-rental-income. Her only other income is a rental result of EUR 2,000 from a garage she lets in Vienna. (Invented case.)

**Limited liability (default).** No personal deductions, no EUR 36 lump sum. Taxable income EUR 24,000. The tariff is applied to 24,000 + 12,348 = 36,348. z = (36,348 − 17,799) / 10,000 = 1.8549. Tax = (173.10 × 1.8549 + 2,397) × 1.8549 + 1,034.87 = 6,076.65, rounded down EUR 6,076. Below EUR 20,350, so no surcharge.

**§ 1(3) option.** German income is 24,000 / 26,000 = 92.3% of her total, and the Austrian income is under EUR 12,348 (Austria is in country group 1), so both tests pass. She needs a certificate from the Austrian tax office for the EUR 2,000. Taxable income 24,000 − 36 = EUR 23,964. The Austrian rent is not subject to German tax, so it raises the rate (§ 32b(1) no. 5; the EU/EEA rent exception in § 32b(1) sentence 2 covers only no. 3): tax on 23,964 + 2,000 = 25,964 is EUR 3,107, a rate of 11.9666%. Tax = 23,964 × 11.9666% = EUR 2,867. The option saves EUR 3,209.

The tax office rounds the progression rate; the example keeps it unrounded, which can move the result by one euro. If Anna also had large Austrian income (say a salary of EUR 40,000), she would fail both tests and stay on the limited-liability figure.

```oa-check
name: DE non-resident landlord 2026, limited liability vs § 1(3) option
inputs:
  rent_result: 24000
  foreign_rent: 2000
  grundfreibetrag: 12348
steps:
  - base_limited: rent_result + grundfreibetrag
  - z1: (base_limited - 17799) / 10000
  - tax_limited: floor((173.10 * z1 + 2397) * z1 + 1034.87)
  - german_share: rent_result / (rent_result + foreign_rent)
  - taxable_opt: rent_result - 36
  - prog_base: taxable_opt + foreign_rent
  - z2: (prog_base - 17799) / 10000
  - tax_prog_base: floor((173.10 * z2 + 2397) * z2 + 1034.87)
  - rate: tax_prog_base / prog_base
  - tax_option: floor(taxable_opt * rate)
  - saving: tax_limited - tax_option
expected:
  base_limited: 36348
  tax_limited: 6076
  german_share: 0.9231
  tax_prog_base: 3107
  tax_option: 2867
  saving: 3209
tolerance: 0.01
```

### Example 2: German resident with foreign dividends taxed 15% abroad

Jan lives in Munich. In 2026 he receives EUR 10,000 of dividends from a foreign company through a foreign broker. The source country withheld 15% (EUR 1,500), its treaty rate. He has no other capital income and is not a church member. (Invented case.)

**Which regime.** These are private capital income under § 32d(1) EStG, so § 34c does not apply (§ 34c(1) sentence 1, second half, and § 34c(6) sentence 2). The credit is under § 32d(5). Because no German bank withheld, he declares the dividends in the return (§ 32d(3)).

- Capital income after the Sparer-Pauschbetrag of EUR 1,000 (see de-capital-gains): e = EUR 9,000.
- German tax before credit: 25% × 9,000 = EUR 2,250.
- Cap 1: 25% of the dividend, EUR 2,500. Cap 2: the German tax on the capital income, EUR 2,250. The EUR 1,500 paid is under both, so q = EUR 1,500 is credited in full.
- Flat tax: (9,000 − 4 × 1,500) / 4 = EUR 750.
- Solidarity surcharge: 5.5% × 750 = EUR 41.25. The EUR 20,350 threshold does not apply to § 32d(3) tax.
- Total German tax on the dividends: EUR 791.25.

If he had chosen the tariff under § 32d(6), § 32d(5) still governs the credit, applied to the additional tariff tax on the capital income. The foreign tax must first be reduced by any source-country refund entitlement. If 30% (EUR 3,000) were withheld but the same treaty limits source tax to 15%, only EUR 1,500 is creditable in this case and EUR 1,500 is reclaimed from the source country; the German tax cap does not turn treaty-refundable tax into a German credit. In a separate no-refund-entitlement case with EUR 3,000 of eligible foreign tax, the German cap would limit credit to EUR 2,250 and EUR 750 would remain uncredited.

```oa-check
name: DE resident, EUR 10,000 foreign dividends, 15% foreign tax, § 32d(5) credit
inputs:
  dividends: 10000
  foreign_rate: 0.15
  sparer_pauschbetrag: 1000
steps:
  - foreign_tax: dividends * foreign_rate
  - e: dividends - sparer_pauschbetrag
  - german_tax_before: e * 0.25
  - q: min(foreign_tax, dividends * 0.25, german_tax_before)
  - flat_tax: (e - 4 * q) / 4
  - soli: flat_tax * 0.055
  - total: flat_tax + soli
expected:
  foreign_tax: 1500
  german_tax_before: 2250
  q: 1500
  flat_tax: 750
  soli: 41.25
  total: 791.25
```

For comparison, the § 34c cap for income taxed at the tariff is German tariff tax × foreign income / taxable income. With taxable income of EUR 60,000 including EUR 10,000 of foreign rent, tariff tax T, the cap is T × 10,000 / 60,000.

## Ask the client first

1. Where do you live, and do you keep any home in Germany you can use? Did you stay in Germany more than six months in a row? This decides full or limited liability.
2. What German income do you have (wages for work done in Germany, rent, a business, director or board fees, performances, royalties, dividends), and was tax withheld from it?
3. What is your total income from all countries for 2026? This decides the § 1(3) test.
4. Your nationality, and where your spouse lives. EU/EEA nationals may get splitting under § 1a.
5. Which country taxes you as a resident, and do you have its residence certificate? Treaty refunds and the § 1(3) option need one.
6. For a resident with foreign income: what type of income, which country, how much tax was paid, and was any of it refundable there?
7. For the relevant non-resident branch: any later failed full-liability status, mixed residence year, extraordinary employment income or special credit/insurance application; any registry-only right and related-party/treaty facts; for a property-company share, dated active-asset book values and seller attribution during the 365-day window; for entity relief, its statutory population, owners/beneficiaries, source-to-activity connection and actual rebuttal or listed-share evidence.

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 1 (liability, § 1(3) option) | https://www.gesetze-im-internet.de/estg/__1.html | 2026-10-23 |
| EStG § 2 (§ 2(5b) capital income) | https://www.gesetze-im-internet.de/estg/__2.html | 2026-10-23 |
| EStG § 1a (EU/EEA spouses) | https://www.gesetze-im-internet.de/estg/__1a.html | 2026-10-23 |
| EStG § 25 (return, electronic filing) | https://www.gesetze-im-internet.de/estg/__25.html | 2026-10-23 |
| EStG § 32a (2026 tariff, EUR 12,348) | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-10-23 |
| EStG § 32b (progression) | https://www.gesetze-im-internet.de/estg/__32b.html | 2026-10-23 |
| EStG § 32d (flat tax, foreign tax credit) | https://www.gesetze-im-internet.de/estg/__32d.html | 2026-10-23 |
| EStG § 34c (foreign tax credit) | https://www.gesetze-im-internet.de/estg/__34c.html | 2026-10-23 |
| EStG § 34d (foreign income) | https://www.gesetze-im-internet.de/estg/__34d.html | 2026-10-23 |
| EStG § 38b (tax class I) | https://www.gesetze-im-internet.de/estg/__38b.html | 2026-10-23 |
| EStG § 39 (wage tax data for non-residents) | https://www.gesetze-im-internet.de/estg/__39.html | 2026-10-23 |
| EStG § 43a (Kapitalertragsteuer 25%) | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-10-23 |
| EStG § 44a (two-fifths refund) | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-10-23 |
| EStG § 46 (employee assessments) | https://www.gesetze-im-internet.de/estg/__46.html | 2026-10-23 |
| EStG § 49 (German-source income) | https://www.gesetze-im-internet.de/estg/__49.html | 2026-10-23 |
| EStG § 50 (assessment of non-residents) | https://www.gesetze-im-internet.de/estg/__50.html | 2026-10-23 |
| EStG § 50a (withholding) | https://www.gesetze-im-internet.de/estg/__50a.html | 2026-10-23 |
| EStG § 50c (exemption and refund) | https://www.gesetze-im-internet.de/estg/__50c.html | 2026-10-23 |
| EStG § 50d (treaty shopping) | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-10-23 |
| AO §§ 8, 9 (residence, habitual abode) | https://www.gesetze-im-internet.de/ao_1977/__8.html | 2026-10-23 |
| AO § 19 (competent tax office) | https://www.gesetze-im-internet.de/ao_1977/__19.html | 2026-10-23 |
| EStZustV § 1 (Finanzamt Neubrandenburg for non-resident pensioners) | https://www.gesetze-im-internet.de/estzustv/__1.html | 2026-10-23 |
| AO §§ 108, 149, 152, 233a, 238, 240 | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-23 |
| KStG § 2 (limited corporate liability) | https://www.gesetze-im-internet.de/kstg_1977/__2.html | 2026-10-23 |
| KStG § 23 (15% to 2027) | https://www.gesetze-im-internet.de/kstg_1977/__23.html | 2026-10-23 |
| KStG § 32 (withholding final) | https://www.gesetze-im-internet.de/kstg_1977/__32.html | 2026-10-23 |
| SolzG §§ 3, 4 | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-23 |
| BMF letter of 2 December 2025, country groups from 2025 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-12-02-beruecks-auslaendischer-verhaeltnisse.pdf | 2026-10-23 |
| BZSt, Kapitalertragsteuerentlastung (26.375%, processing time) | https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/kapitalertragsteuerentlastung_node.html | 2026-10-23 |
| BZSt, Abzugsteuern nach § 50a EStG | https://www.bzst.de/DE/Unternehmen/Abzugsteuern/abzugsteuern_node.html | 2026-10-23 |
| SolzG §§ 3(1)–(3), 4, assessment base, threshold and sliding cap; actual selected operative reads | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-10-29 |
| EStG §§ 49(1) nos. 2(e), 2(f), 6; 50(2); 44a(9); 50d(3), selected source/assessment/refund conditions actually read | https://www.gesetze-im-internet.de/estg/__49.html | 2026-10-29 |

Not yet confirmed: whether the BMF has issued a country-group list for 2026 (the 2 December 2025 letter applies from 2025 and no later one was found); how the tax office rounds the progression rate; whether foreign capital income of a § 1(3) applicant counts in the 90% test and in the progression, given § 2(5b) EStG; whether the § 50c(3) refund of dividend tax down to the treaty rate includes the solidarity surcharge (the example assumes it does); church tax for non-residents (state law).

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
