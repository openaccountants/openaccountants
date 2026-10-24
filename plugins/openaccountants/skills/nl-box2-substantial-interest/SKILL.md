---
name: nl-box2-substantial-interest
description: "Dutch box 2 (aanmerkelijk belang) for tax year 2026: income tax on a resident individual's substantial interest of 5% or more in a company. Covers who has a substantial interest (the 5% test with a fiscal partner, the family pull-in rule or meetrekregeling), regular benefits such as dividends, disposal benefits from a sale and deemed disposals (emigration, death, liquidation, falling below 5%), the acquisition price, the 2026 rates of 24.5% up to EUR 68,843 and 31% above, splitting box 2 income between fiscal partners, loss relief and the loss tax credit, the EUR 500,000 excessive borrowing rule, roll-overs and payment deferral, and the combined burden with corporate tax. Trigger on: box 2, aanmerkelijk belang, DGA dividend, verkoop aandelen bv, excessief lenen, ab-verlies. Out of scope: box 1 and box 3 (nl-income-tax), DGA salary (nl-payroll-tax), the BV's own tax (nl-corporate-tax), emigration detail (nl-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-box2-substantial-interest"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Netherlands: box 2, income from a substantial interest (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from wetten.overheid.nl or belastingdienst.nl, read on 22 October 2026. It prepares working papers; it is not authority to file or pay.

Box 2 taxes what an individual gets out of a company in which they hold a substantial interest (aanmerkelijk belang): dividends, sale gains and deemed sale gains. The law is chapter 4 of the Wet inkomstenbelasting 2001 (Wet IB 2001), with the rate in art. 2.12. This skill links rather than repeats:

- Box 1, box 3, credits and the rest of the return: [nl-income-tax](nl-income-tax.md), [nl-deductions](nl-deductions.md).
- The DGA's salary (gebruikelijk loon) and payroll: [nl-payroll-tax](nl-payroll-tax.md); national insurance and Zvw: [nl-social-contributions](nl-social-contributions.md).
- The BV's own corporate tax, the participation exemption and fiscal unity: [nl-corporate-tax](nl-corporate-tax.md).
- Emigration, the protective assessment and non-residents: [nl-cross-border](nl-cross-border.md).
- Whether to incorporate or how to take money out: [netherlands-tax-optimization](netherlands-tax-optimization.md).

## Who this applies to

**The 5% test.** A person has a substantial interest if they, alone or together with their fiscal partner, directly or indirectly hold at least 5% of the issued capital of a company, rights to acquire 5% of the issued capital, profit-sharing certificates for 5% of the annual profit or of the liquidation proceeds, or 5% of the votes in a cooperative (Wet IB 2001 art. 4.6). The company can be Dutch or foreign: a bv, nv, Ltd or AG all count ([Belastingdienst, Wanneer hebt u een aanmerkelijk belang?](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/wanneer_hebt_u_een_aanmerkelijk_belang/)).

- **Per class of shares.** Holding 5% of one class of shares is enough, even if the person holds less than 5% of the whole capital (art. 4.7).
- **Bought-back shares** not yet cancelled are left out of the capital when testing the 5% (art. 4.8).
- **Usufruct and options.** A person entitled only to the benefits of shares is treated as a shareholder (art. 4.3). A call option on shares counts as the shares (art. 4.4). Units in an open fund for joint account count as shares (art. 4.5).
- **Pull-along (meesleepregeling).** Once a person has a substantial interest in a company, all their other shares and profit certificates in that company belong to it too (art. 4.9).
- **Family pull-in (meetrekregeling).** Shares a person holds in a company where they do not reach 5%, but where their partner, or a blood relative or in-law in the direct line of them or their partner (parents, children, grandchildren), does hold a substantial interest, also form a substantial interest for that person (art. 4.10).
- **Deemed substantial interest (fictief aanmerkelijk belang).** Shares stay in box 2 after a roll-over under arts. 3.65, 4.17 to 4.17c, 4.40 or 4.41, even though the holding is now below 5% (art. 4.11).
- **Minor children.** Parents report the box 2 income of their minor children up to the day the child turns 18 ([Belastingdienst, Fiscale informatie 2026, ch. 14.3](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aanmerkelijk_belang)).

**Residents** are taxed on box 2 income from Dutch and foreign companies. **Non-residents** are taxed only on box 2 income from a company established in the Netherlands; a company incorporated under Dutch law always counts as established in the Netherlands for this purpose (art. 4.35; Fiscale informatie 2026, ch. 14.1). Non-resident detail sits in [nl-cross-border](nl-cross-border.md).

**Not box 2:**
- Salary from the company is box 1 wages, not a regular benefit ([Belastingdienst, Inkomsten uit aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/inkomsten_uit_aanmerkelijk_belang/)).
- Interest the person receives on a loan to their own company is box 1 income from making assets available (terbeschikkingstelling), not box 2 (same page).
- Shares held in a sole trader's business are business assets in box 1. Bringing them into the business is itself a deemed disposal (art. 4.16(1)(f)).
- A holding below 5% that no rule above pulls in is a box 3 asset ([nl-income-tax](nl-income-tax.md)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Box 2 rate, first band | 24.5% of taxable box 2 income up to €68,843 | 2026 | [Wet IB 2001 art. 2.12](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Box 2 rate, second band | €16,866 plus 31% of the excess over €68,843 | 2026 | same; [Belastingdienst, Box 2](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/) |
| Box 2 band, earlier years | €67,804 (2025), €67,000 (2024, when the top rate was 33%) | 2025, 2024 | [Belastingdienst, Box 2](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/) |
| Fiscal partners | The band is per person. Partners who are partners for the whole year, or who choose to be treated as partners for the whole year, split their joint box 2 income in any ratio that totals 100%, so each can use their own €68,843 band | 2026 | Wet IB 2001 art. 2.17(2), (5)(b), (7); [Fiscale informatie 2026, ch. 14.3.1](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aanmerkelijk_belang) |
| Substantial interest threshold | 5% of issued capital, a class of shares, profit rights or votes | 2026 | Wet IB 2001 arts. 4.6, 4.7 |
| Excessive borrowing threshold | Debts to own companies above €500,000 at 31 December are a deemed regular benefit; the threshold rises by amounts already taxed | 2026 | Wet IB 2001 arts. 4.13(1)(f), 4.14a; [Belastingdienst, Excessief lenen](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/bijzondere_situaties/geld_lenen_van_uw_bv/excessief-lenen-van-bv-beperkt) |
| Deemed return on low-taxed investment companies | 6% a year of the value at 1 January, less actual regular benefits, at least nil | 2026 | Wet IB 2001 arts. 4.13(1)(a), 4.14(1) |
| Loss carry-back and carry-forward | Back 1 year, forward 6 years (losses from 2018 or earlier: 9 years forward) | 2026 | Wet IB 2001 art. 4.49(1); [Belastingdienst, Verlies uit aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/) |
| Loss tax credit after the interest ends | 24.5% of the unrelieved box 2 loss (the first-band rate in art. 2.12), set against box 1 tax and national insurance contributions | 2026 | Wet IB 2001 arts. 4.53(2), 2.11a(2); [Belastingdienst, Verlies omzetten in belastingkorting](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/verlies_omzetten_in_belastingkorting) |
| Usual salary (gebruikelijk loon) reference | At least the highest of the most comparable job, the best-paid employee, and €58,000 (€56,000 in 2025 and 2024) | 2026 | [Belastingdienst, Loon en aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/) |
| Dutch dividend tax | 15% withheld by the company, credited against income tax | 2026 | [Wet op de dividendbelasting 1965 art. 5](https://wetten.overheid.nl/BWBR0002515); Wet IB 2001 art. 9.2 |
| Corporate tax on the company's profit (for the combined burden) | 19% up to €200,000; €38,000 plus 25.8% above | 2026 | [Wet Vpb 1969 art. 22](https://wetten.overheid.nl/BWBR0002672/2026-01-01) |

**Combined burden in 2026.** Profit earned in a BV and paid out as a dividend is taxed twice. At the low rates: 19% corporate tax, then 24.5% box 2 on the remaining 81%, is 38.845% in total. At the high rates: 25.8% corporate tax, then 31% on the remaining 74.2%, is 48.802%. The box 1 top rate for 2026 is in [nl-income-tax](nl-income-tax.md); compare like with like before advising on salary against dividend.

## The taxable base

Taxable box 2 income is box 2 income less box 2 losses carried over (art. 4.1). Box 2 income is the total of (a) regular benefits less deductible costs and (b) disposal benefits, less any personal deductions left after box 1 and box 3 (art. 4.12).

**1. Regular benefits (reguliere voordelen), art. 4.13.**
- Dividends and other profit distributions, gross: before costs and before dividend tax (Fiscale informatie 2026, ch. 14.4).
- A repayment of paid-in capital is a regular benefit, except to the extent it does not exceed the acquisition price of those shares and the shareholders' meeting decided on it beforehand with a matching cut in nominal value by amendment of the articles (art. 4.13(1)(b)). The amount not taxed reduces the acquisition price (art. 4.33).
- A 6% deemed return on shares in an exempt investment institution (vbi) or a foreign company mainly holding investments, unless it is subject to a real profit tax by Dutch standards (arts. 4.13(1)(a), 4.14(1) and (8)).
- **Excessive borrowing (Wet excessief lenen), arts. 4.13(1)(f) and 4.14a.** In 2026 the threshold is €500,000. All debts of the person and their fiscal partner, together, to companies in which the person has a substantial interest, measured at nominal value on 31 December, count. The part above the threshold is a deemed regular benefit taxed in box 2. Own-home debts are left out only where the company holds a mortgage right on the home; that condition does not apply to an own-home debt that already existed on 31 December 2022 (art. 4.14a(6); transitional rule in art. 10a.23; [Belastingdienst, Excessief lenen](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/bijzondere_situaties/geld_lenen_van_uw_bv/excessief-lenen-van-bv-beperkt)). Claims the person has on the company are not netted off. Debts of a child or parent (a blood relative or in-law in the direct line of the person or their partner) who has no substantial interest in that company also count, to the extent they exceed that relative's own €500,000 (art. 4.14b(1) and (2)). The threshold rises by amounts taxed in earlier years (art. 4.14a(2)). A repayment gives a negative deemed benefit, at most the amount taxed before (art. 4.14a(1)(b)), and the Belastingdienst lowers the threshold by the repayment, but not below €500,000 (same Belastingdienst page). The loan itself continues: the company keeps charging interest on the whole loan, and no dividend tax is withheld on the taxed part (same Belastingdienst page). Someone who moves to the Netherlands starts with a threshold equal to their debts at that time, at least €500,000 (art. 4.14c).
- **Deductible costs** are the costs of acquiring, collecting and keeping the regular benefits, to the extent they are not more than usual: for example interest on a loan taken to buy the shares, and bank custody fees. Dividend tax withheld is not a cost; it is a credit (art. 4.15; Fiscale informatie 2026, ch. 14.4.2).
- **Timing.** A regular benefit is taxed when it is received, set off, made available, starts to bear interest, or becomes due and collectable (art. 4.43). Declaring a dividend and crediting the shareholder's current account is enough.

**2. Disposal benefits (vervreemdingsvoordelen), arts. 4.16 to 4.34.**
- Gain = transfer price less acquisition price (art. 4.19). The transfer price is the price received less the seller's costs (art. 4.20). On a part disposal, a proportional part of the acquisition price is used (art. 4.19(1)).
- **Deemed disposals** (art. 4.16(1)) include: a buy-back of shares; payment of liquidation distributions; transfer of the company's assets under universal title (merger, demerger); transfer on death or under matrimonial property law; bringing the shares into a business; the substantial interest ceasing to exist; ceasing to be a Dutch resident other than by death, including becoming treaty-resident elsewhere; granting a call option; and the shares starting to give the 6% deemed return because the company became an exempt investment institution or a low-taxed foreign investment company (art. 4.16(1)(k)).
- **Market value.** If there is no consideration, or the deal is not at arm's length (a gift, an exchange, a sale to family at a low price), market value is used as the transfer price and as the acquirer's acquisition price (art. 4.22).
- **Liquidation.** A liquidation distribution is a disposal benefit to the extent it exceeds the acquisition price; the rest reduces the acquisition price. Acquisition price still left when liquidation is complete is a disposal loss, taken in the year liquidation is completed (arts. 4.34, 4.46(6)).
- **No loss while keeping the business.** A loss is not taken if the person keeps, directly or indirectly, all or almost all of their interest in the company's activities; it is added to the acquisition price of what they keep (art. 4.24).

**3. Acquisition price (verkrijgingsprijs), arts. 4.21 to 4.25.**
- The price paid plus the buyer's costs, such as notary costs (art. 4.21(1); Fiscale informatie 2026, ch. 14.5.2).
- Shares of the same class with different prices are averaged (art. 4.21(2)).
- If shares become part of a substantial interest after they were acquired (for example the person reaches 5% later), the acquisition price is the market value at that time (art. 4.23).
- On moving to the Netherlands, the acquisition price is stepped up to market value on arrival, unless the person lived here before or was already taxed as a non-resident on that interest (art. 4.25).
- After a roll-over (gift, inheritance, matrimonial property, share merger), the acquirer takes over the old acquisition price (arts. 4.39 to 4.39c, 4.42).
- After a contribution of a business to a BV under art. 3.65, the acquisition price can be negative (art. 4.21(4)).

**4. Roll-overs (doorschuiving), on request.**
- **Inheritance and gift of a business company.** If the company runs a business, the transfer is not a disposal for the part of the price that relates to business assets. Main conditions: the acquirer is a Dutch resident and does not hold the shares in a business of their own, the shares were not part of a substantial interest only through the family pull-in rule, a legacy is transferred within two years of the death, and, for a gift, the acquirer is 21 or older; preference shares have extra conditions (arts. 4.17a(1) and (3), 4.17c(1) and (3)). The acquirer takes over the acquisition price (arts. 4.39a, 4.39c). Investment assets in the company are not covered. Arts. 4.17a and 4.17c carry amendments that have no commencement date yet: check the version in force on the date of the transfer.
- **Matrimonial property** and division of a community within two years of a divorce (art. 4.17), unless the parties choose to settle now (art. 4.38).
- **Dropping below 5%** while keeping the shares: the deemed disposal can be skipped on request, and the shares stay in box 2 as a deemed substantial interest (arts. 4.40, 4.11).
- **Share-for-share exchange (aandelenfusie), legal merger and demerger:** the gain is not taxed on request; the new shares take over the old acquisition price. Any cash top-up is taxed (arts. 4.41, 4.42).

**5. Splitting between fiscal partners.** Box 2 income before personal deductions is joint income for partners who have the same fiscal partner for the whole calendar year. They choose the split each year in the return, any ratio that totals 100%; without a choice it is half each. They also choose, separately, how to split the Dutch dividend tax withheld; without a choice that is half each too. The splits can be changed until the assessments are final (art. 2.17(2) to (5)). Partners for only part of the year can choose to be treated as partners for the whole year and then split; this choice is not available where one of them emigrated or immigrated in the year and is not a qualifying non-resident (art. 2.17(7)). Without that choice, each reports their own benefits.

**6. Losses.**
- A negative box 2 income is a box 2 loss (art. 4.47). It is set off against box 2 income of the year before, then the next 6 years, oldest first (art. 4.49(1) and (3)). Losses from 2018 or earlier can be carried forward 9 years ([Belastingdienst, Verlies uit aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/)).
- The inspector fixes the loss in an objectionable decision, together with the assessment for the loss year (art. 4.50). For a faster carry-back, the person can ask in writing, after filing the loss-year return, for a provisional loss set-off. The assessment for the earlier year must be final, and at most 80% of the loss is set off provisionally (same page; art. 4.51(5)).
- **Loss tax credit.** If the person and their partner had no substantial interest in the calendar year and in the year before, an unrelieved box 2 loss can be converted on request into a credit of 24.5% of the loss. The credit reduces box 1 tax and national insurance contributions for that year and the following 7 years, but no later than the 9th year after the loss year (arts. 4.53(4), 2.11a). The Belastingdienst only accepts the request from the second year after the year in which the substantial interest ended, and only after the loss has been fixed in a final assessment ([Verlies omzetten in belastingkorting](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/verlies_omzetten_in_belastingkorting)).

**7. The DGA's salary.** A substantial-interest holder who works for their company must take a usual salary in box 1: at least the highest of the most comparable job, the best-paid employee in the company or a connected company, and €58,000 in 2026. A lower amount is allowed if the person shows that comparable work is normally paid less. If the usual salary for all their companies together is €5,000 or less and they can show it, the actual salary is reported ([Belastingdienst, Loon en aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/)). Profit taken as dividend instead of salary is taxed in box 2. Run the salary through payroll: see [nl-payroll-tax](nl-payroll-tax.md). The salary-against-dividend choice: see [netherlands-tax-optimization](netherlands-tax-optimization.md).

## Deadlines and filing

- **Return.** Box 2 income goes in the annual income tax return (aangifte inkomstenbelasting), filed online through Mijn Belastingdienst, in the section for substantial interest. The Belastingdienst computes the box 2 tax ([Box 2](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/)). The filing deadline is the date in the invitation letter. The Belastingdienst says this is usually 1 May of the following year, and an extension moves that date ([Tot wanneer kan ik een voorlopige aanslag aanvragen of wijzigen?](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/tot-wanneer-voorlopige-aanslag-aanvragen-wijzigen)).
- **Dividend tax.** Report the gross dividend as a regular benefit, and the 15% Dutch dividend tax withheld under tax to be credited ([Inkomsten uit aanmerkelijk belang](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/inkomsten_uit_aanmerkelijk_belang/)).
- **Excessive borrowing.** The deemed benefit is measured on 31 December and reported in that year's return (arts. 4.14a(4), 4.43(3)).
- **Preliminary assessment (voorlopige aanslag).** A large 2026 dividend or sale gain can be paid in monthly instalments during the year through a preliminary assessment. The 2026 form has been available since 1 December 2025 in Mijn Belastingdienst. It can be requested or changed until the return deadline, and not after the return has been filed ([Vanaf wanneer](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/vanaf-wanneer-een-voorlopige-aanslag-aanvragen-of-wijzigen); [Tot wanneer](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/tot-wanneer-voorlopige-aanslag-aanvragen-wijzigen)).
- **Payment.** The final assessment states its payment date. The [invorderingsrente page](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente) gives a legal payment term of 6 weeks for an income tax assessment.
- **Requests that need a letter.** The loss tax credit (art. 4.53), a provisional loss set-off (art. 4.51(5)), the roll-overs (arts. 4.17a, 4.17c, 4.40, 4.41) and payment deferral are requests, not automatic.

**Payment deferral for a sale on credit (art. 25(9) Invorderingswet 1990).** If the shares are sold to an individual, or to a BV wholly owned by one individual in the EU or EEA, and the buyer leaves the price owing, the seller can ask for deferral of the income tax on the disposal for up to 10 years, with sufficient security. Conditions: the shares sold are at least 5% of the issued capital, and the company's assets are not mainly investments. The tax is paid in 10 equal yearly instalments. The first falls due 6 weeks after the assessment date, then one each year. Deferral is only given if the tax on the disposal is more than €3,350. The deferred amount is cut by half of the repayments on the price, and by half of the regular benefits from the shares, to the extent either exceeds twice that year's instalment in a calendar year; it is also cut for shares the buyer disposes of. The seller must tell the receiver at once (Uitvoeringsregeling Invorderingswet 1990, art. 3(2) to (6)). Collection interest runs on instalments paid after the assessment's payment date, even with deferral ([Invorderingsrente](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente)). A similar 10-year deferral exists where the company transfers shares in a subsidiary below market value at the shareholder's request (art. 25(11) Invorderingswet; art. 3a of the regulation). A share-for-share exchange needs no deferral, because the roll-over in art. 4.41 applies.

## Penalties and interest

- **Late or missing return:** administrative penalty of up to €6,709 (AWR art. 67a).
- **Intentional failure to file, or an incorrect or incomplete return filed on purpose:** penalty of up to 100% of the tax not levied as a result. Where losses were used, the base is the tax without those losses (AWR art. 67d). Under-assessment through intent or gross negligence found on a later additional assessment: up to 100% (AWR art. 67e).
- **Tax interest (belastingrente):** 5% from 1 January 2026, charged when an assessment cannot be set on time ([Overzicht percentages belastingrente](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente)). A preliminary assessment requested in time for a large box 2 income is the practical way to limit it.
- **Collection interest (invorderingsrente):** 4.3% from 1 January 2026 on late payment, including during deferral or instalments ([Invorderingsrente](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente)). Interest on a protective assessment for emigration does not run during the deferral: see [nl-cross-border](nl-cross-border.md).

## Cross-border points

- **Emigration** is a deemed disposal at market value (art. 4.16(1)(h)); the tax goes into a protective assessment with deferral. Full treatment, including the 2026 worked example: [nl-cross-border](nl-cross-border.md).
- **Short stay (passanten), art. 4.18.** No emigration charge applies to a substantial interest in a foreign company if the person leaves within 8 years of moving to the Netherlands and has lived here for no more than 10 years in total in the last 25 years.
- **Arrival.** Acquisition price steps up to market value on immigration (art. 4.25). The excessive borrowing threshold starts at the debts on arrival, at least €500,000 (art. 4.14c).
- **Non-residents** are taxed on box 2 income from a company established in the Netherlands only (Fiscale informatie 2026, ch. 14.1; art. 4.35). Check the treaty with the country of residence: it can cap the Dutch charge on dividends and gains.
- **Foreign companies.** Dividends and gains from a foreign company are box 2 income for a resident. Relief for foreign withholding tax runs through the Besluit voorkoming dubbele belasting 2001 or the treaty; foreign tax that is relieved is not a deductible cost (art. 4.15(4)(b)). Shares in a low-taxed foreign investment company give the 6% deemed return (art. 4.14).
- **Dividend tax** at 15% applies to a Dutch company's dividend, including one paid to a non-resident shareholder; the rate under a treaty and the company-level rules are in [nl-cross-border](nl-cross-border.md).

## Worked examples

### Example 1: a DGA takes a €150,000 dividend from his BV in 2026

He owns 100% of a trading BV and takes his usual salary through payroll. In 2026 the BV pays him a dividend of €150,000. It withholds 15% dividend tax, so he receives €127,500 in cash.

**Alone (no fiscal partner).**
1. Regular benefit: €150,000 gross (art. 4.13; Fiscale informatie 2026, ch. 14.4). No deductible costs.
2. Box 2 tax: €16,866 on the first €68,843, plus 31% × (€150,000 − €68,843) = €25,158.67. Total €42,024.67.
3. Dividend tax withheld, €22,500, is credited. Still to pay on the assessment: €19,524.67.

**With a fiscal partner for the whole of 2026.**
4. The dividend is joint income. They choose a 50/50 split in their returns (art. 2.17), so each reports €75,000.
5. Each pays €16,866 + 31% × (€75,000 − €68,843) = €18,774.67. Together €37,549.34, saving €4,475.33 against the single case. Any split that puts both partners above €68,843 gives the same total. They also choose how to split the €22,500 dividend tax credit; without a choice it is €11,250 each (art. 2.17(2), (3)).

**The company side.** Assume the BV's 2026 taxable profit is exactly what is needed to pay this dividend after corporate tax, and stays under €200,000: profit €185,185.19 (€150,000 ÷ 0.81), corporate tax at 19% €35,185.19. Corporate tax plus his box 2 tax (alone) is €77,209.86. Measured against the profit before corporate tax, that is 41.69%. The dividend tax is not an extra cost: it is a prepayment of the box 2 tax.

```oa-check
name: DGA dividend EUR 150,000, alone and with a fiscal partner (2026 box 2)
inputs:
  dividend: 150000
  band: 68843
  band_tax: 16866
  low_rate: 0.245
  high_rate: 0.31
  dividend_tax_rate: 0.15
  cit_low_rate: 0.19
steps:
  - box2_alone: band_tax + max(dividend - band, 0) * high_rate
  - dividend_tax: dividend * dividend_tax_rate
  - payable_alone: box2_alone - dividend_tax
  - share_each: dividend / 2
  - box2_each: band_tax + max(share_each - band, 0) * high_rate
  - box2_couple: box2_each * 2
  - saving: box2_alone - box2_couple
  - pre_tax_profit: round(dividend / (1 - cit_low_rate), 2)
  - cit: round(pre_tax_profit * cit_low_rate, 2)
  - combined: cit + box2_alone
  - combined_rate: round(combined / pre_tax_profit, 4)
expected:
  box2_alone: 42024.67
  dividend_tax: 22500
  payable_alone: 19524.67
  box2_each: 18774.67
  box2_couple: 37549.34
  saving: 4475.33
  pre_tax_profit: 185185.19
  cit: 35185.19
  combined: 77209.86
  combined_rate: 0.4169
```

### Example 2: selling a 30% stake in 2026, with a box 2 loss brought forward

She bought 30% of an operating BV in 2019 for €240,000 and paid €2,000 in notary and adviser costs. In 2026 she sells the whole stake to an unrelated buyer for €600,000 in cash and pays €12,000 in selling costs. Her 2023 return shows a box 2 loss of €40,000 from the liquidation of another company. That loss was fixed by a decision with the 2023 assessment and has not been used yet. She has no fiscal partner.

1. Acquisition price: €240,000 + €2,000 = €242,000 (art. 4.21(1)).
2. Transfer price: €600,000 − €12,000 = €588,000 (art. 4.20).
3. Disposal benefit: €588,000 − €242,000 = €346,000 (art. 4.19).
4. The 2023 loss is first carried back to 2022 and then forward to 2024 up to 2029 (art. 4.49(1)). She had no box 2 income in 2022, 2024 or 2025, so all €40,000 is set off in 2026. Box 2 has no cap on the loss set off in a year, so the whole loss is used against the gain. Taxable box 2 income: €306,000.
5. Box 2 tax: €16,866 + 31% × (€306,000 − €68,843) = €90,384.67. Without the loss it would be €102,784.67; the loss saves €12,400, which is 31% of €40,000.
6. She has no substantial interest left after the sale. Had the sale produced a loss instead, she could have asked for the loss tax credit at 24.5% once the interest had been gone for the calendar year and the year before (art. 4.53). If the buyer had left part of the price owing, she could have asked for deferral under art. 25(9) Invorderingswet.

```oa-check
name: Sale of a 30% stake with a EUR 40,000 box 2 loss brought forward (2026)
inputs:
  price: 600000
  selling_costs: 12000
  purchase_price: 240000
  purchase_costs: 2000
  loss_brought_forward: 40000
  band: 68843
  band_tax: 16866
  high_rate: 0.31
steps:
  - acquisition_price: purchase_price + purchase_costs
  - transfer_price: price - selling_costs
  - gain: transfer_price - acquisition_price
  - taxable: max(gain - loss_brought_forward, 0)
  - box2_tax: band_tax + max(taxable - band, 0) * high_rate
  - box2_tax_no_loss: band_tax + max(gain - band, 0) * high_rate
  - loss_saving: box2_tax_no_loss - box2_tax
expected:
  acquisition_price: 242000
  transfer_price: 588000
  gain: 346000
  taxable: 306000
  box2_tax: 90384.67
  box2_tax_no_loss: 102784.67
  loss_saving: 12400
```

## Ask the client first

1. Who holds what: the percentage of each class of shares, options and profit certificates held by the client, their fiscal partner and their parents, children or grandchildren in the same company. This decides whether box 2 applies at all (arts. 4.6 to 4.10).
2. Did the client have the same fiscal partner for the whole of 2026? Only then can box 2 income be split (art. 2.17(5)).
3. For a sale or deemed disposal: the original price and costs, any later step-ups (immigration, reaching 5%, inheritance or gift roll-overs), and the price and costs on sale. Was the price paid in cash, in shares or left owing?
4. All debts of the client, their partner and their children or parents to the client's companies at 31 December 2026, with any mortgage right the company holds on an own home and the debts that existed on 31 December 2022.
5. Box 2 losses from earlier years, with the decisions that fixed them. Box 2 income of 2025, for a carry-back.
6. Does the client work for the company, and what salary does payroll pay? A dividend cannot replace the usual salary.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, arts. 2.11a, 2.12, 2.14, 2.17, 4.1 to 4.53, 9.2, 10a.23 (versions valid 1 January 2026 and 21 February 2026) | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-22 |
| Wet op de dividendbelasting 1965, art. 5 (version valid from 1 January 2025, still in force) | https://wetten.overheid.nl/BWBR0002515 | 2026-10-22 |
| Wet op de vennootschapsbelasting 1969, art. 22 (version valid 1 January 2026) | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-10-22 |
| Invorderingswet 1990, art. 25(9) to (11) (version valid 1 January 2026) | https://wetten.overheid.nl/BWBR0004770/2026-01-01 | 2026-10-22 |
| Uitvoeringsregeling Invorderingswet 1990, arts. 3 and 3a (version valid 1 January 2026) | https://wetten.overheid.nl/BWBR0004766/2026-01-01 | 2026-10-22 |
| Algemene wet inzake rijksbelastingen, arts. 67a, 67d, 67e (version valid 1 January 2026) | https://wetten.overheid.nl/BWBR0002320/2026-01-01 | 2026-10-22 |
| Belastingdienst, Fiscale informatie 2026, ch. 14 Aanmerkelijk belang | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/aanmerkelijk_belang | 2026-10-22 |
| Belastingdienst, Box 2: uitleg en tarieven | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_2/ | 2026-10-22 |
| Belastingdienst, Wanneer hebt u een aanmerkelijk belang? | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/wanneer_hebt_u_een_aanmerkelijk_belang/ | 2026-10-22 |
| Belastingdienst, Inkomsten uit aanmerkelijk belang | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/inkomsten_uit_aanmerkelijk_belang/ | 2026-10-22 |
| Belastingdienst, Verlies uit aanmerkelijk belang | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/ | 2026-10-22 |
| Belastingdienst, Verlies omzetten in belastingkorting | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/verlies_uit_aanmerkelijk_belang/verlies_omzetten_in_belastingkorting | 2026-10-22 |
| Belastingdienst, Loon en aanmerkelijk belang | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/ | 2026-10-22 |
| Belastingdienst, Excessief lenen van bv beperkt vanaf 2023 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/bijzondere_situaties/geld_lenen_van_uw_bv/excessief-lenen-van-bv-beperkt | 2026-10-22 |
| Belastingdienst, Vanaf wanneer kan ik een voorlopige aanslag aanvragen of wijzigen? | https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/vanaf-wanneer-een-voorlopige-aanslag-aanvragen-of-wijzigen | 2026-10-22 |
| Belastingdienst, Tot wanneer kan ik een voorlopige aanslag aanvragen of wijzigen? | https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/tot-wanneer-voorlopige-aanslag-aanvragen-wijzigen | 2026-10-22 |
| Belastingdienst, Overzicht percentages belastingrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-22 |
| Belastingdienst, Invorderingsrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente | 2026-10-22 |

Not yet confirmed: the exact filing deadline for the 2026 income tax return (the pages read say "usually 1 May" and point to the invitation letter); how far art. 25(9) Invorderingswet deferral reaches when only part of the price is left owing. The Wet IB 2001 version read is valid from 1 January to 20 February 2026; the version in force from 21 February 2026 was compared for arts. 2.12, 4.6, 4.14a, 4.49 and 4.53 and has the same text, apart from a notice of amendments to arts. 2.12 and 4.53 that have no commencement date yet.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-box2-substantial-interest` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-box2-substantial-interest. If neither is available, confirm every figure against the official source pages cited above before relying on it.
