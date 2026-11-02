---
name: at-corporate-income-tax
description: "Austrian corporate income tax (Körperschaftsteuer, KöSt) for tax year 2026: GmbH, AG, FlexCo and foreign companies with Austrian income. Covers liability (seat or management), the 23% rate (KStG § 22(1)) and the enacted 24% on income above EUR 1,000,000 for financial years starting after 31 December 2027, the minimum tax (EUR 500 a year for a GmbH, EUR 3,500 for an AG), the 75% loss offset limit (§ 8(4) Z 2), the participation exemption and international participations (§§ 10 and 10a), group taxation (§ 9), the interest limit (§ 12a), the clearing-account rule from 2027 (§ 8(2a)), KESt on distributions (27.5%, or 23% to a company), filing deadlines, quarterly prepayments, late-filing surcharge and Anspruchszinsen. Trigger on: Körperschaftsteuer, KöSt, Mindestkörperschaftsteuer, Verlustvortrag GmbH, Schachtelbeteiligung, Gruppenbesteuerung, Zinsschranke, Austrian company tax. Out of scope: at-transfer-pricing, at-cross-border, at-vat-return, at-income-tax, at-company-formation."
version: 1.2
jurisdiction: AT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austria corporate income tax (Körperschaftsteuer): tax year 2026

Source-cited draft: not reviewed by an accountant, not for filing.

This skill covers how Austria taxes companies: who is liable, the rate, the minimum tax, the taxable base (losses, the participation exemption, the interest limit, group taxation), the return, prepayments, surcharges and interest, and the tax on dividends a company pays or receives. All statute text was read on RIS (the federal legal information system) on 23 October 2026, in the version in force on that day unless a row says otherwise. Tax year 2026 means the calendar year 2026, or a financial year that ends in 2026.

What is new for 2026: nothing in the 23% rate, the minimum tax or the loss limit. The interim tax of a private foundation rises from 23% to 27.5% from calendar year 2026 (KStG § 22(2)). Already enacted by the Budgetbegleitgesetz 2027-2028 (BGBl. I Nr. 62/2026), for later years only: the clearing-account rule in KStG § 8(2a), from financial years ending in 2027 (§ 26c Z 101), and a 24% rate on income above EUR 1,000,000, from financial years starting after 31 December 2027 (§ 22(1) and § 26c Z 102). Neither applies to 2026.

Related skills: `at-transfer-pricing` (arm's length prices with related companies, hidden distributions, master file and local file), `at-cross-border` (residence, exit tax, withholding on payments abroad under § 99 EStG), `at-income-tax` (the shareholder's own income tax), `at-company-formation` (choosing and founding the company), `at-vat-return`. This skill does not repeat them.

## Who this applies to

- **Unlimited liability.** A body with its management (Geschäftsleitung) or its seat (Sitz, § 27 BAO) in Austria is taxed on all its Austrian and foreign income (KStG § 1(2)). One of the two is enough. Bodies are domestic private-law legal persons and comparable foreign entities, commercial operations of public bodies (Betriebe gewerblicher Art), and associations, institutions, foundations and other funds without legal personality.
- **Limited liability.** A body with neither management nor seat in Austria is taxed only on certain Austrian income (KStG § 1(3) Z 1). See `at-cross-border` for what counts as Austrian income.
- **All income is business income** for a company that must keep accounts because of its legal form (GmbH, AG, FlexCo), for cooperatives that must keep accounts, and for comparable foreign bodies with unlimited liability (KStG § 7(3)).
- **Partnerships are not KöSt taxpayers.** An OG or KG is transparent; its partners pay income tax or KöSt on their share. See `at-income-tax`.
- **Private foundations** (Privatstiftungen) have their own interim tax: 27.5% from 2026 on income under § 13(3) and (4) (KStG § 22(2)). Not covered further here.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| KöSt rate on income (unlimited and limited taxpayers) | 23% | Calendar years from 2024 (24% in 2023) | KStG § 22(1): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=22 |
| KöSt rate, enacted for later years | 23% up to EUR 1,000,000 of income; 24% on the part above EUR 1,000,000. Applies to unlimited taxpayers and to limited taxpayers under § 1(3) Z 1; limited taxpayers under § 1(3) Z 2 and 3 stay at 23% (§ 22(1a)). Foreign income exempt in Austria is left out when testing the EUR 1,000,000 | Financial years starting after 31 December 2027; for a tax group, the group parent's financial years starting after that date | KStG § 22(1) as amended by BGBl. I Nr. 62/2026, § 26c Z 102 lit. a and b: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=26c |
| Surcharge where the company does not name the recipient of a payment on request | 25% of the amount, on top of KöSt | 2026 | KStG § 22(3) |
| Minimum tax (Austrian companies with share capital and comparable foreign companies with unlimited liability) | 5% of one quarter of the legal minimum share capital, for each full calendar quarter of unlimited liability | 2026 | KStG § 24(4) Z 1: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=24 |
| Legal minimum share capital of a GmbH | EUR 10,000 (since BGBl. I Nr. 179/2023) | 2026 | GmbHG § 6(1): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001720&Paragraf=6 |
| Minimum tax of a GmbH | EUR 125 a quarter, EUR 500 a year | 2026 | KStG § 24(4) Z 1 with GmbHG § 6(1) |
| Legal minimum share capital of an AG | EUR 70,000 | 2026 | AktG § 7: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002070&Paragraf=7 |
| Minimum tax of an AG | EUR 875 a quarter, EUR 3,500 a year | 2026 | KStG § 24(4) Z 1 with AktG § 7 |
| Minimum tax of a foreign company with no legal minimum capital, or one below the GmbH minimum | As for a GmbH: EUR 500 a year | 2026 | KStG § 24(4) Z 1, second sentence |
| Minimum tax of banks and insurers in company form | EUR 1,363 a quarter | 2026 | KStG § 24(4) Z 2 |
| Loss offset limit for carried-forward losses | 75% of the total income (Gesamtbetrag der Einkünfte) | 2026 | KStG § 8(4) Z 2 lit. a: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=8 |
| International participation (internationale Schachtelbeteiligung) | At least one tenth of the capital, held without a break for at least one year | 2026 | KStG § 10(2): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=10 |
| Switch-over to credit (Methodenwechsel): low taxation | Effective foreign tax below 15% | 2026 | KStG § 10a(3) and (7): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=10a |
| Switch-over: portfolio holdings it also reaches | At least 5% (dividends under § 10(1) Z 5 or 6) | 2026 | KStG § 10a(7) |
| Group taxation: financial link | More than 50% of the capital and of the voting rights, for the whole financial year of the member | 2026 | KStG § 9(4) and (5): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=9 |
| Group taxation: minimum life | Three financial years of twelve months each | 2026 | KStG § 9(10) |
| Group taxation: foreign members' losses counted | Up to 75% of the sum of the own incomes of all Austrian members and the group parent | 2026 | KStG § 9(6) Z 6 |
| Interest limit (Zinsschranke) | Net interest expense deductible up to 30% of tax EBITDA; at least EUR 3,000,000 a year in any case | 2026 | KStG § 12a(1): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=12a |
| Interest limit: equity ratio escape | Full deduction if the company's equity ratio is at least the group's, or up to 2 points below it | 2026 | KStG § 12a(5) |
| Interest limit: carryforwards | Unused interest: carried forward on application, no time limit stated. Unused EBITDA capacity: five following years | 2026 | KStG § 12a(6) |
| Clearing-account receivable against an individual shareholder, not settled at the balance sheet date | Treated as an open distribution to the extent it exceeds EUR 50,000 | Financial years ending in 2027 onwards (not 2026) | KStG § 8(2a) as amended by BGBl. I Nr. 62/2026, § 26c Z 101 |
| KESt on a distribution, general rate | 27.5% | 2026 | EStG § 27a(1) Z 2: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27a |
| KESt the payer may withhold when the recipient is a company (§ 1(1) KStG) | 23% | Income received from 2024 | EStG § 93(1a): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=93 |
| No KESt on dividends to a company holding at least 10% | Exempt at source; for an EU parent (Annex 2 EStG) only after one year without a break | 2026 | EStG § 94 Z 2: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=94 |
| Combined burden on profit paid out to an individual shareholder | 44.175% (23% + 27.5% x 77%) | 2026 | Arithmetic from KStG § 22(1) and EStG § 27a(1) Z 2 |
| Prepayments | One quarter each on 15 February, 15 May, 15 August and 15 November | 2026 | EStG § 45(2) with KStG § 24(3) Z 1: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=45 |
| Prepayment uplift on the last assessed tax | +4% for the first year after the assessed year, +5% for each further year | 2026 | EStG § 45(1) |
| Late-filing surcharge (Verspätungszuschlag) | Up to 10% of the tax assessed; not set below EUR 50 | 2026 | BAO § 135: https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=135 |
| Interest on assessed differences (Anspruchszinsen) | 2% a year above the base rate (Basiszinssatz), from 1 October of the following year, for at most 48 months; not set below EUR 50 | 2026 | BAO § 205(1) and (2): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=205 |
| Base rate (Basiszinssatz), so the Anspruchszinsen rate | 2.03% from 16 September 2026, so 4.03%; 1.53% from 11 June 2025 to 15 September 2026, so 3.53%. The rate moves with the ECB main refinancing rate: check it on the day | 2026 | OeNB, Basis- und Referenzzinssätze: https://www.oenb.at/isawebstat/stabfrage/createReport?lang=DE&report=2.1 |
| Late-payment surcharges (Säumniszuschläge) | 2%, then 1% and 1% more after three and six months of enforceability; not set below EUR 50 | 2026 | BAO § 217(2), (3) and (10): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=217 |

## The taxable base

1. **Start from the accounts.** For a GmbH, AG or FlexCo all income is business income (KStG § 7(3)). The profit is taken from the UGB accounts and adjusted under the EStG and KStG.
2. **Distributions do not reduce income.** Income is the same whether it is kept, paid out openly or paid out as a hidden distribution (KStG § 8(2)). A price that favours a shareholder is added back; the method is in `at-transfer-pricing`.
3. **Clearing accounts, from 2027.** For financial years ending in 2027 or later, a receivable on the clearing account (Verrechnungskonto) against an individual shareholder, or a person close to the shareholder, must be settled by the balance sheet date. Indirect holdings count. Turning it into a written loan at arm's length (written agreement, interest paid as it runs, a duty to repay) also counts as settling it. If it is not settled, the amount above EUR 50,000 is treated as openly distributed and received on the day after the resolution to prepare the accounts (§ 222(1) UGB), and at the latest "nach fünf Monaten" (KStG § 8(2a); § 26c Z 101). The five months are the period § 222(1) UGB gives for preparing the accounts, which runs from the balance sheet date: for a 31 December 2027 year-end, the deemed distribution falls on 31 May 2028 at the latest (Budget Committee report, 561 d.B. XXVIII. GP, on § 8(2a)). The EUR 50,000 threshold applies whatever the size of the holding. That brings in KESt at 27.5% (see `at-transfer-pricing` for the gross-up when the company bears it). It does not apply to 2026 year-ends.
4. **Exempt participation income (§ 10(1)).** Exempt are:
   - Z 1 to 4: profit shares of every kind from Austrian companies and cooperatives (shares, profit participation rights, participation capital). The law sets no minimum holding.
   - Z 5: the same from a foreign company that meets the conditions of Annex 2 EStG (the EU Parent-Subsidiary Directive 2011/96/EU), if Z 7 does not apply.
   - Z 6: the same from a foreign company comparable to an Austrian company, resident in a state with comprehensive administrative assistance with Austria, if Z 7 does not apply.
   - Z 7: profit shares of every kind from an international participation.
5. **International participation (§ 10(2) and (3)).** A company that holds, in the form of capital shares, at least one tenth of a foreign company comparable to an Austrian company (or of an EU company under Annex 2 EStG), without a break for at least one year, has an international participation. The one-year period does not restart for shares from a capital increase that does not raise the percentage. On top of the dividend exemption, gains, losses and other value changes on the holding are tax-neutral. The company can opt, in the return for the year it acquires the holding, to make value changes taxable; the option can be made up or withdrawn only within one month of filing, by correcting the return (§ 10(3) Z 1 and 2). Actual and final losses on liquidation or insolvency of the subsidiary stay deductible, reduced by tax-free dividends of the last five years.
6. **What the exemption does not cover.**
   - **Deductible dividends (§ 10(4)).** Profit shares under § 10(1) Z 5 to 7 are taxable to the extent the foreign company could deduct them.
   - **Switch-over (§ 10a(7)).** For an international participation, and for a holding of at least 5% whose dividends fall under § 10(1) Z 5 or 6, the exemption and the tax neutrality are replaced by taxation with credit of the foreign tax if the foreign company is low-taxed (effective foreign tax below 15%, § 10a(3)) and its business focus is earning passive income (interest, royalties, taxable dividends and share gains, financial leasing, banking and insurance, low-value re-invoicing, § 10a(2)). Controlled foreign company rules (Hinzurechnungsbesteuerung) under § 10a(1) Z 1 and (4) apply where the low-taxed company's passive income is more than one third of its income, the Austrian company (with associated enterprises) holds more than 50% of the votes or capital or is entitled to more than 50% of the profits, and the foreign company carries on no substantial economic activity (staff, equipment, assets, premises); the Austrian company must prove the substance. The foreign tax is credited on application (§ 10a(9)).
   - **Note.** In earlier law the switch-over sat in § 10(4) and (5). In the version in force today § 10(4) is the deductible-dividend rule above and there is no § 10(5); the switch-over is § 10a.
7. **Losses.** A loss that cannot be used in the year is carried forward under § 18(6) EStG and deducted in later years as a special expense, but only up to 75% of the total income of the year. What cannot be deducted moves to the following years under the same limit (KStG § 8(4) Z 2 lit. a). No time limit appears in the law. The 75% limit does not apply to the extent the total income contains gains from a debt waiver (including restructuring gains under § 23a), gains in years affected by insolvency proceedings, gains on the sale or closure of a business, part of a business or a partnership share, liquidation gains under § 19, amounts recaptured under § 9(6) Z 7 KStG or § 2(8) Z 4 EStG, or amounts under § 6 Z 6 EStG (except those under § 6 Z 6 lit. a last sentence) (lit. b). Losses are lost where the company's identity changes through a substantial change of its organisational and economic structure together with a substantial paid change of shareholders (Mantelkauf), unless done to restructure the company and keep a substantial part of the jobs. Losses stay deductible to the extent hidden reserves are realised for tax by the end of the financial year of the change (lit. c).
8. **Interest limit (§ 12a).** Net interest expense (interest expense over taxable interest income, including all payments for raising debt) is deductible only up to 30% of tax EBITDA (total income before § 12a, with tax depreciation and write-ups and the net interest expense added back), but always up to EUR 3,000,000 a year. A standalone company is outside the rule: one that is not fully consolidated in group accounts, has no associated enterprise under § 10a(4) Z 2 and has no foreign permanent establishment (§ 12a(2)). A fully consolidated company can deduct everything if its equity ratio is at least the group's or no more than 2 points below it (§ 12a(5)). Unused interest is carried forward on application; unused EBITDA capacity is carried forward, also on application, for five years (§ 12a(6)).
9. **Group taxation (§ 9).** Austrian companies and cooperatives under § 7(3), plus comparable foreign companies resident in the EU or in a state with comprehensive administrative assistance that are linked only to Austrian members or the group parent, can be members (§ 9(2)). The financial link is more than 50% of the capital and of the votes, directly, through a partnership or through other members, held for the whole financial year of the member (§ 9(4) and (5)). The income of each Austrian member is added to the member or parent above it. A foreign member brings in only its losses, worked out under Austrian rules and capped at the loss under foreign law, and only up to 75% of the sum of the own incomes of all Austrian members and the parent; the rest is carried forward by the parent (§ 9(6) Z 6). Foreign losses are added back as profit when they are, or could be, offset against foreign profits, and in full when the foreign member leaves the group (§ 9(6) Z 7). The group must last three twelve-month financial years; a member that leaves earlier is taxed as if it had never joined (§ 9(10)).
10. **Minimum tax.** It is payable in loss years too. In a later year, the minimum tax paid above the actual KöSt is credited like a prepayment, but only to the extent that year's actual KöSt exceeds that year's minimum tax (KStG § 24(4) Z 4). If the legal form changes during a quarter, the form at the start of the quarter counts (§ 24(4) Z 1).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| KöSt return for 2026 (K 1 for companies that keep accounts, K 2 for other unlimited taxpayers, K 3 for limited taxpayers) | 30 April 2027 on paper; 30 June 2027 if filed electronically. A company with unlimited liability must file electronically unless it lacks the technical means | BAO § 134(1); KStG § 24(3) Z 1 |
| Extension in a single case | On a reasoned application; if refused, at least one more week | BAO § 134(2) |
| Return filed by a tax adviser under the quota system (Quotenregelung) | At the latest 31 March 2028 for tax year 2026; §§ 134 and 135 BAO do not apply while this time is used. The tax office can extend this to 30 June 2028 for all returns still due from one adviser (§ 134a(3)). The share of returns each adviser must file by set earlier dates is fixed by BMF regulation (§ 134a(5) Z 3) | BAO § 134a(1), (3) and (5): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=134a |
| Prepayments for 2026 | 15 February, 15 May, 15 August and 15 November 2026, a quarter each, based on the last assessed KöSt plus the uplift. The minimum tax is due for each full calendar quarter of unlimited liability in any case | EStG § 45(1) and (2); KStG § 24(3) Z 1 and (4) Z 1 |
| Change of the prepayment for the current year | The tax office cannot change it after 30 September unless the company applied by 30 September | EStG § 45(3) |
| Balance after the assessment notice | Within one month of the notice, where the tax was assessed later than one month before it fell due | BAO § 210(4): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=210 |
| Voluntary payment on account to avoid Anspruchszinsen | Any time, and more than once (Anzahlung) | BAO § 205(3) |
| Tax group application (form G 4) | Signed by the legal representatives of the parent and every Austrian member before the end of the financial year for which it is to take effect; filed with the parent's tax office within one calendar month of the last signature | KStG § 9(8) |
| KESt on a dividend paid | Withheld when the dividend is paid; paid over within one week (see `at-transfer-pricing` for § 96 EStG) | EStG §§ 93, 95, 96 |

## Penalties and interest

- **Late filing.** If the return is late and the delay is not excusable, the tax office can add up to 10% of the tax assessed. Amounts under EUR 50 are not set (BAO § 135). The surcharge does not apply where the adviser's quota deadline under § 134a is used.
- **Late payment.** 2% of tax not paid by the due date; 1% more if still unpaid three months after it became enforceable, and another 1% three months after that. Surcharges under EUR 50 are not set (BAO § 217(2), (3) and (10)).
- **Anspruchszinsen.** A difference between the assessed KöSt and the prepayments carries interest at 2% a year above the base rate (4.03% from 16 September 2026), from 1 October of the year after the tax year (for 2026, from 1 October 2027) until the notice, for at most 48 months. Amounts under EUR 50 are not set (BAO § 205(1) and (2)). A payment on account under § 205(3) reduces it.
- **Unnamed recipients.** 25% surcharge on payments whose recipient the company will not name on request (KStG § 22(3)).
- **Late-payment and interest rules on cross-border items** (withholding under § 99 EStG) are in `at-cross-border`.

## Cross-border points

- **Dividends paid to a company abroad.** KESt is 27.5%, or 23% where the payer uses § 93(1a) EStG for a company recipient. No KESt is withheld where the recipient is an EU company meeting Annex 2 EStG, holding at least 10% directly or indirectly, and the holding has lasted without a break for at least one year (EStG § 94 Z 2). For a domestic company shareholder the 10% test applies with no holding period. The minister can require withholding in abuse cases and on hidden distributions by regulation (§ 94 Z 2, last sentence); the regulation and the refund route are in `at-transfer-pricing`. Treaty relief and refunds are in `at-cross-border`.
- **Dividends received from abroad.** See the exemptions in "The taxable base", steps 4 to 6. A holding under 10%, or held for less than a year, can still be exempt under § 10(1) Z 5 or 6, but without tax-neutral gains and losses.
- **Foreign group members.** Only first-tier foreign companies, resident in the EU or a state with comprehensive administrative assistance, linked only to Austrian members (KStG § 9(2)). Losses only, capped as above.
- **Transfer pricing.** Prices with related companies abroad must be at arm's length (§ 6 Z 6 EStG and treaty Article 9). The method, documentation and adjustments are in `at-transfer-pricing`.
- **Residence of the company and exit tax.** Moving the seat or management abroad, and taxing a non-resident's Austrian income, are in `at-cross-border`.
- **Payments abroad.** Withholding at 20% or 27.5% on royalties, consulting fees and similar payments to foreign businesses under § 99 EStG is in `at-cross-border`.
- **Global minimum tax.** The Mindestbesteuerungsgesetz (BGBl. I Nr. 183/2023) for groups with revenue of EUR 750 million or more is outside this skill. § 10a(3) KStG counts a qualified domestic top-up tax paid abroad when it tests low taxation.

## Worked examples

### Example 1: GmbH with EUR 400,000 profit and a EUR 500,000 loss carried forward (tax year 2026)

Gamma GmbH has a 2026 profit for tax purposes of EUR 400,000. It has no other income, so its total income (Gesamtbetrag der Einkünfte) is EUR 400,000. It carries forward EUR 500,000 of losses from earlier years, worked out from proper books. None of its 2026 income is of a kind listed in § 8(4) Z 2 lit. b (no restructuring gain, no sale of a business, no liquidation), and there has been no change of shareholders.

The loss deduction is capped at 75% of total income: 400,000 x 75% = EUR 300,000. Taxable income is 400,000 - 300,000 = EUR 100,000. KöSt at 23% is EUR 23,000. That is above the GmbH minimum tax of EUR 500, so the minimum tax does not bite. EUR 200,000 of losses move to 2027 under the same 75% limit. Prepayments made for 2026 are credited against the EUR 23,000, and any balance is due one month after the notice. If the balance is assessed after 1 October 2027, Anspruchszinsen run from that date.

```oa-check
name: Gamma GmbH, 2026, profit EUR 400,000 with EUR 500,000 loss carried forward
inputs:
  total_income: 400000
  loss_brought_forward: 500000
  loss_limit_pct: 75
  kost_rate_pct: 23
  minimum_tax_gmbh: 500
steps:
  - loss_cap: total_income * loss_limit_pct / 100
  - loss_used: min(loss_brought_forward, loss_cap)
  - taxable_income: total_income - loss_used
  - kost: taxable_income * kost_rate_pct / 100
  - tax_payable: max(kost, minimum_tax_gmbh)
  - loss_carried_to_2027: loss_brought_forward - loss_used
expected:
  loss_cap: 300000
  loss_used: 300000
  taxable_income: 100000
  kost: 23000
  tax_payable: 23000
  loss_carried_to_2027: 200000
```

### Example 2: dividend from a 15% EU subsidiary held for 18 months (tax year 2026)

Delta GmbH, an Austrian company, has held 15% of an operating company resident in another EU member state for 18 months, without a break. In 2026 it receives a dividend of EUR 120,000. The subsidiary is comparable to an Austrian company and could not deduct the dividend in its own state. It runs a trading business, so its business focus is not passive income.

15% is at least one tenth and 18 months is more than one year, so the holding is an international participation (KStG § 10(2)). The dividend is exempt under § 10(1) Z 7. Austrian KöSt on it is nil. A later gain or loss on selling the shares is tax-neutral too, unless Delta opted in the return for the year it acquired the holding to make value changes taxable (§ 10(3)).

The exemption would fall away to the extent the subsidiary could deduct the dividend (§ 10(4)): the full EUR 120,000 would then be taxed at 23%, which is EUR 27,600. If instead the subsidiary were low-taxed (below 15% effective) and mainly earned passive income, the switch-over in § 10a(7) would apply: the dividend becomes taxable with credit of the foreign tax.

```oa-check
name: Delta GmbH, 2026, dividend from 15% EU subsidiary held 18 months
inputs:
  dividend: 120000
  holding_pct: 15
  months_held: 18
  min_holding_pct: 10
  min_months: 12
  kost_rate_pct: 23
steps:
  - holding_test_margin: holding_pct - min_holding_pct
  - period_test_margin: months_held - min_months
  - exempt_amount: dividend
  - taxable_dividend: dividend - exempt_amount
  - kost_on_dividend: taxable_dividend * kost_rate_pct / 100
  - kost_if_deductible_abroad: dividend * kost_rate_pct / 100
expected:
  holding_test_margin: 5
  period_test_margin: 6
  exempt_amount: 120000
  taxable_dividend: 0
  kost_on_dividend: 0
  kost_if_deductible_abroad: 27600
```

## Ask the client first

- Is it a GmbH, FlexCo, AG or another body, where are its seat and its real management, and does its financial year end on 31 December? This decides liability, the minimum tax and which year the 2027 and 2028 changes first hit.
- What losses are carried forward, from which years, and has the shareholding or the business changed? This decides the 75% offset and the Mantelkauf test.
- For each holding in another company: country, percentage, date acquired, whether the option under § 10(3) was made, and how the subsidiary is taxed and what it earns. This decides the exemption and the switch-over.
- Is the company in a tax group, or could it form one (more than 50% of capital and votes for a full year)? Was a G 4 application filed?
- Is the company part of consolidated group accounts, and what is its net interest expense? This decides the interest limit.
- Does an individual shareholder owe the company money on a clearing account, and how much? From 2027 year-ends, more than EUR 50,000 unsettled at the balance sheet date is a distribution.

## Sources

| Source | URL | Read on |
|---|---|---|
| Körperschaftsteuergesetz 1988 (KStG) § 1 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=1 | 2026-10-23 |
| KStG § 7 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=7 | 2026-10-23 |
| KStG § 8 (current version; § 8(2a) is in it from 30 July 2026 and applies from financial years ending in 2027) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=8 | 2026-10-23 |
| KStG § 9 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=9 | 2026-10-23 |
| KStG § 10 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=10 | 2026-10-23 |
| KStG § 10a | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=10a | 2026-10-23 |
| KStG § 12a | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=12a | 2026-10-23 |
| KStG § 22 (current, and the version from 1 January 2028) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=22 | 2026-10-23 |
| KStG § 24 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=24 | 2026-10-23 |
| KStG § 26c (Z 101 and 102, BGBl. I Nr. 62/2026) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=26c | 2026-10-23 |
| GmbH-Gesetz § 6 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001720&Paragraf=6 | 2026-10-23 |
| Aktiengesetz § 7 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002070&Paragraf=7 | 2026-10-23 |
| Einkommensteuergesetz 1988 (EStG) § 27a | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27a | 2026-10-23 |
| EStG § 45 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=45 | 2026-10-23 |
| EStG § 93 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=93 | 2026-10-23 |
| EStG § 94 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=94 | 2026-10-23 |
| Bundesabgabenordnung (BAO) § 134 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=134 | 2026-10-23 |
| BAO § 134a | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=134a | 2026-10-23 |
| BAO § 135 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=135 | 2026-10-23 |
| BAO § 205 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=205 | 2026-10-23 |
| BAO § 210 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=210 | 2026-10-23 |
| BAO § 217 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=217 | 2026-10-23 |
| Unternehmensgesetzbuch (UGB) § 222 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702&Paragraf=222 | 2026-10-23 |
| Budget Committee report on the Budgetbegleitgesetz 2027-2028 (561 d.B. XXVIII. GP), notes on § 8(2a) and § 22(1) KStG | https://www.parlament.gv.at/dokument/XXVIII/I/561/fname_1768090.pdf | 2026-10-23 |
| OeNB, Basis- und Referenzzinssätze | https://www.oenb.at/isawebstat/stabfrage/createReport?lang=DE&report=2.1 | 2026-10-23 |
| BMF form catalogue (K 3, G 4) | https://service.bmf.gv.at/service/anwend/formulare/show_mast.asp?s=g4 | 2026-10-23 |

Not yet confirmed: the percentages and dates in the BMF quota regulation under § 134a(5) BAO; how KESt withheld on a domestic dividend to a company holding under 10% is credited or refunded in the assessment; the minimum tax of an SE (Article 4 of Regulation (EC) No 2157/2001 was not read); the KStR 2013 guidance on §§ 9, 10, 10a and 12a, which was not read for this refresh.

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
