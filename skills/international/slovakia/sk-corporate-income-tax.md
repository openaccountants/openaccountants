---
name: sk-corporate-income-tax
description: "Slovak corporate income tax (daň z príjmov právnických osôb) for tax year 2026 under Act No. 595/2003 Coll. as amended, including Act No. 261/2025 Coll. Covers the three rates set by taxable revenue (10% up to EUR 100,000, 24% above EUR 5,000,000, 21% otherwise), the minimum tax with its new EUR 11,520 band for revenue above EUR 5,000,000, the tax base from accounting profit, paid-basis expenses, unrecoverable VAT, depreciation groups 0 to 6, the 5-year loss carry-forward with the 50% cap, the two interest limits (25% EBITDA for related-party loans and 30% above EUR 3,000,000 net interest), dividends, advances, the DPPO return and extensions, and penalties. Trigger on: Slovakia corporate tax, DPPO, s.r.o. tax, 10% rate Slovakia, minimálna daň, daňová licencia, preddavky na daň. Out of scope: individuals (slovakia-pit), payroll (sk-payroll-social), VAT (slovakia-vat-return), company set-up (sk-company-formation)."
jurisdiction: SK
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovak corporate income tax (DPPO): 2026 rates, minimum tax, losses and filing

The law is the Income Tax Act, Act No. 595/2003 Coll. (zákon o dani z príjmov). This skill reads the consolidated version in force from 1 January 2026 on slov-lex.sk, which includes the consolidation package Act No. 261/2025 Coll. Penalties and interest come from the Tax Procedure Code, Act No. 563/2009 Coll. (daňový poriadok). The Financial Administration (Finančná správa) runs the return and the portal at financnasprava.sk. Figures are for the 2026 tax period: the calendar year 2026, or a fiscal year (hospodársky rok) that ends in 2026 or 2027. Where a rule applies only to periods that start on or after 1 January 2026, the skill says so.

## Who this applies to

- **Slovak-resident legal persons**: a company with its seat or place of effective management in Slovakia (§ 2(d) second point). Typical clients: s.r.o., a.s., cooperatives. They are taxed on worldwide income.
- **Non-resident legal persons** with Slovak-source income (§ 16), in particular a permanent establishment in Slovakia. A registered permanent establishment files a DPPO return like a resident. Slovak income with no permanent establishment is mostly taxed by withholding (§ 43); see "Cross-border points".
- **Non-profit bodies** (§ 12(3)) are taxed only on part of their income. Not covered here.

Not covered here, refer to a specialist: banks, insurers and leasing companies (special interest and reserve rules); companies in liquidation or bankruptcy (special tax periods in § 41); the special 54% base for banks on card-payment fees to gaming accounts (§ 51eb, new from 2026); the Pillar Two top-up tax under Act No. 507/2023 Coll. (scope check only: multinational and large domestic groups); controlled foreign companies; hybrid mismatches; mergers and divisions; the R&D super-deduction (§ 30c) and the investment deduction (§ 30e) beyond a pointer; transfer pricing documentation.

Related skills: an overview in [sk-tax-overview](sk-tax-overview.md); individuals in [slovakia-pit](slovakia-pit.md); employer contributions in [sk-payroll-social](sk-payroll-social.md); VAT in [slovakia-vat-return](slovakia-vat-return.md); setting up a company in [sk-company-formation](sk-company-formation.md).

## Rates, bands and thresholds

"Taxable revenue" below is zdaniteľné príjmy (výnosy): the company's taxable income in the revenue sense, before expenses. It is not the tax base. The rate band is chosen by revenue, then the single rate applies to the whole tax base after losses. There is no slicing: a company with EUR 100,001 of taxable revenue pays 21% on all of its base.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| CIT rate, taxable revenue up to EUR 100,000 (§ 15(b)(1a)) | 10% of the base after losses | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| CIT rate, taxable revenue above EUR 100,000 and up to EUR 5,000,000 (§ 15(b)(1b)) | 21% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| CIT rate, taxable revenue above EUR 5,000,000 (§ 15(b)(1c)) | 24% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Exit tax special base (§ 17f, rate in § 15(b)(3)) | 21% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Dividends received from a non-cooperating state, special base (§ 51e(4), rate in § 15(b)(2)) | 35% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Yield on Slovak, EU or EEA state bonds and treasury bills, special base (§ 51ea, rate in § 15(b)(4)) | 13% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, taxable revenue up to EUR 50,000 (§ 46b(2)(a)) | EUR 340 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 50,000 up to EUR 250,000 (§ 46b(2)(b)) | EUR 960 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 250,000 up to EUR 500,000 (§ 46b(2)(c)) | EUR 1,920 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 500,000 up to EUR 5,000,000 (§ 46b(2)(d)) | EUR 3,840 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Minimum tax, above EUR 5,000,000 (§ 46b(2)(e), new: Act No. 261/2025, periods starting on or after 1 January 2026) | EUR 11,520 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2025/261/20260101.html |
| Micro-taxpayer (mikrodaňovník): taxable revenue up to EUR 60,000 (§ 2(w)) | Full loss offset, no 50% cap | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Loss carry-forward (§ 30) | 5 periods; capped at 50% of the base unless a micro-taxpayer | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Related-party interest limit (§ 21a) | Interest above 25% of EBITDA (profit before tax plus depreciation plus interest expense) is not deductible | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Interest limitation rule (§ 17k) | Net interest above EUR 3,000,000 added back to the extent it exceeds 30% of tax EBITDA | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Depreciable tangible movable asset (§ 22(2)(a)) | Entry price above EUR 1,700 and useful life over one year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Advances, prior-year tax above EUR 16,600 (§ 42(1)) | Monthly, 1/12 of prior-year tax | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Advances, prior-year tax above EUR 5,000 up to EUR 16,600 (§ 42(2)) | Quarterly, 1/4 of prior-year tax | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| No advances, prior-year tax up to EUR 5,000 (§ 42(3)(a)) | None, unless the tax office orders them | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Withholding tax, standard (§ 43(1)(b)) | 19% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Withholding tax, payee in a non-cooperating state (§ 43(1)(c)) | 35% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html |
| Late payment interest (Tax Procedure Code § 156(2)) | 4 times the ECB main rate a year, at least 15% a year, for at most 4 years. At the ECB main refinancing rate of 2.65% (from 16 September 2026) the 15% floor applies | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html |

## The taxable base

**Start from accounting profit.** A company that keeps double-entry books starts from the profit or loss in its statutory accounts (Slovak GAAP or IFRS), then adds back and deducts the items the Act lists (§ 17). The result, less tax losses, is the base the rate applies to.

**Common add-backs.**
- Expenses that are not tax expenses under § 21, such as representation (entertainment) costs, and fines and penalties imposed by public bodies.
- Expenses deductible only when paid (§ 17(19)). Among them: rent and royalties; marketing and market studies; commissions; legal and advisory services under CPA codes 69.1, 69.2, 70.1 and 70.22; contractual penalties and late payment interest owed by the company; payments to a person in a non-cooperating state once withholding duties are met. If they are booked in 2026 and paid in 2027, they come into the 2027 base.
- From 1 January 2026, VAT that a VAT payer has no right to deduct is not a tax expense, and on tangible assets it is not part of the entry price (§ 52zzzk, inserted by Act No. 261/2025). If the split between business and non-business use of the asset later changes, that VAT is not taken into the base either. Check this for any VAT-registered client with exempt supplies or blocked input VAT.
- Accounting depreciation above tax depreciation.
- Interest caught by § 21a or § 17k (see below).

**Common deductions.** Income not subject to tax, such as most dividends (§ 12(7)(c), below); tax depreciation above accounting depreciation; the R&D super-deduction (§ 30c: 100% of R&D costs, plus 100% of the increase in the two-year average of R&D costs over the average of the two prior periods) and the investment deduction (§ 30e) where the conditions are met.

**Depreciation (§ 26 and § 27).** Tangible assets go into one of seven groups. Straight-line annual depreciation (§ 27) is entry price divided by the period. In the first year only the months from the month the asset is put into use count. Assets in groups 2 and 3 may instead be depreciated by the accelerated method (§ 28); the method is chosen per new asset and cannot be changed (§ 26(3)). A micro-taxpayer may depreciate assets placed in use in a micro-taxpayer period in groups 0 to 4 in any amount it chooses within the group period, except cars with an entry price of EUR 48,000 or more (§ 26(12)).

| Group | Period | Annual straight-line share |
|---|---|---|
| 0 | 2 years | 1/2 |
| 1 | 4 years | 1/4 |
| 2 | 6 years | 1/6 |
| 3 | 8 years | 1/8 |
| 4 | 12 years | 1/12 |
| 5 | 20 years | 1/20 |
| 6 | 40 years | 1/40 |

Assets that fit no group in Annex 1 go into group 2 (§ 26(2)). § 26(14) as amended from 1 January 2026 (building depreciation over at least half the group 6 period) applies first to the period whose return is filed after 31 December 2025. Annex 1 as amended from that date applies first to technical improvements put into use, and repairs booked, in that period. Where the group, period or annual rate changes, the change is also made for assets already being depreciated, but depreciation already claimed is not reopened (§ 52zzzf). Check the asset's group against the 2026 Annex 1 before carrying last year's register forward.

**Interest: two separate limits.**
- **§ 21a (thin capitalisation).** Interest and related costs on loans from a related person (závislá osoba) are not deductible to the extent they exceed 25% of EBITDA. EBITDA here is accounting profit before tax plus the depreciation and interest expense in it. Banks, insurers and leasing companies are out. § 21a does not apply where the company has already added back interest under § 17k.
- **§ 17k (ATAD rule).** If net interest expense is above EUR 3,000,000, the excess over 30% of the tax base (increased by net interest and tax depreciation) is added back. Most owner-managed companies never reach the EUR 3,000,000 floor.

**Tax losses (§ 30).** A tax loss is deducted over at most the five periods right after the loss year. The yearly deduction is capped at 50% of the base, unless the company is a micro-taxpayer in the year it deducts. Then the full base can be absorbed. A micro-taxpayer is a company with taxable revenue up to EUR 60,000 that has no controlled transaction with a related person, is not in bankruptcy, liquidation or a payment plan, and has a full 12-month period (§ 2(w)). Note the two thresholds differ: EUR 60,000 for the loss rule, EUR 100,000 for the 10% rate. Unused loss falls away after the fifth period and on entry into liquidation or bankruptcy.

**Dividends received.** A dividend paid out of a company's profit is not subject to tax in the hands of a Slovak company, to the extent it was not a tax expense of the payer (§ 12(7)(c)). The exception: dividends from a company resident in a non-cooperating state go into a special base taxed at 35% (§ 51e(4) and § 15(b)(2)). The Ministry of Finance publishes a list of cooperating states (states with a tax treaty or an information exchange agreement with Slovakia, less those on the EU list of non-cooperative jurisdictions at 1 January and those with no or a zero corporate tax). A state that is not on that list is a non-cooperating state (§ 2(x)). Use the list valid from 1 January 2026.

**Minimum tax (§ 46b).** A company pays the minimum tax for its revenue band (table above) if its tax after reliefs and foreign tax credit is lower than that figure, or if it has a tax loss. A shorter period is pro-rated by months (§ 46b(6)). It is halved for a company whose staff are at least 20% disabled employees (§ 46b(3)). It does not apply to:
- a company filing for the first time, for the period in which it was set up (unless it is a successor of a company dissolved without liquidation);
- non-profit taxpayers under § 12(3) and (4);
- a company running a sheltered workshop;
- the special periods in liquidation or bankruptcy;
- a land community (pozemkové spoločenstvo) with only its own activities and taxable revenue up to EUR 10,000;
- a company from the period in which it receives notice of proceedings to dissolve it;
- a registered social enterprise (§ 46b(7)).

The excess of minimum tax over the computed tax can be credited against tax in the next three periods. Only the part of that later tax above the minimum tax can absorb it (§ 46b(5)). The credit is lost on dissolution without liquidation, liquidation or bankruptcy (§ 46b(8)).

## Deadlines and filing

- **Return.** The DPPO return is due within three calendar months after the end of the tax period: 31 March 2027 for calendar 2026 (§ 49(2)). Tax is payable by the same date.
- **Extension by notice.** A notice filed with the tax office before the deadline moves it by up to three whole calendar months, to 30 June 2027 for calendar 2026. The new date is the end of the month the company names. If the company has foreign-source income, the move is up to six months, to 30 September 2027 (§ 49(3)(a) and (b)). Tax is due on the new date. Companies in liquidation or bankruptcy apply instead, at least 15 days before the deadline (§ 49(3)(c)).
- **Form.** On 23 October 2026 the Financial Administration's return page names form MF/012187/2025-721, with filing notes for periods whose deadline falls after 31 December 2025. It has 15 pages and at least five annexes even when blank. Before filing the 2026 return, check that page for a newer form.
- **Electronic filing.** A legal person entered in the commercial register, and any VAT payer, must file electronically (Tax Procedure Code § 14(1)(a)). Some annexes may be sent in other ways, but the VII-part annex and the § 13a, § 13b, § 30ca and § 30e annexes form part of the return.
- **Minimum tax** is payable by the return deadline (§ 46b(4)).
- **Advances in 2026 (§ 42).** The tax that sets them (§ 42(6)) is the tax on the base after losses, at the § 15 rate shown in the previous period's return, less reliefs under the Act. It is the computed tax, not the minimum tax. Based on the 2025 tax:
  - above EUR 16,600: monthly, 1/12 of that tax, by the end of each month;
  - above EUR 5,000 up to EUR 16,600: quarterly, 1/4, by the end of each calendar quarter (or quarter of the fiscal year);
  - up to EUR 5,000: none, unless the tax office orders them.
  Until the deadline for the 2025 return, advances follow the last known tax, from the 2024 return (§ 42(7)). A company formed during the year (other than by merger or division) pays no advances in its first period (§ 42(4)). A company filing its first return pays no advances until that return is due, then makes up the advances that fell due by the end of the following month (§ 42(8)).
- **Financial transaction tax.** Separate from CIT, Act No. 279/2024 Coll. taxes financial transactions. Its § 6 rates from 1 January 2026: 0.4%, at most EUR 40 per transaction; 0.8% on cash withdrawals; EUR 2 per payment card. This skill does not cover it beyond this pointer.

## Penalties and interest

From the Tax Procedure Code, Act No. 563/2009 Coll. (version in force from 1 September 2026):

- **Late return (§ 155(1)(a)).** A fine of EUR 100 to EUR 30,000. If the tax office has sent a notice and the return still does not arrive in the time it sets, up to EUR 60,000 (§ 155(1)(b)). A tax office does not impose a fine within a range for the first breach (§ 155(4)).
- **Tax understated in a return and raised by the tax office (§ 155(1)(f)).** 3 times the ECB main refinancing rate a year on the extra tax, at least 10% a year (§ 155(5)). The rate used is the one on the day the assessment is delivered (§ 155(7)). It runs daily from the day after the filing deadline, at least 1% of the extra tax and at most the extra tax (§ 155(2)). Paying the assessed amount within 15 days of delivery cuts the fine to two thirds (§ 155(17)).
- **Correction by a supplementary return (§ 155(1)(g)).** The ECB rate a year on the increase, at least 3% a year. If the supplementary return follows the start of a tax audit: twice the ECB rate, at least 7% a year (§ 155(1)(h) and (5)).
- **Late payment interest (§ 156(2)).** 4 times the ECB main rate in force on the day the arrears arise, at least 15% a year, daily, for at most four years. It applies to late tax and late advances; on a late advance it runs at most to the return deadline (§ 156(4)).
- **At the current ECB rate.** The ECB main refinancing rate is 2.65% from 16 September 2026. 3 times is 7.95%, 2 times 5.3%, 1 times 2.65% and 4 times 10.6%, so all four floors apply: 10%, 7%, 3% and 15% a year.

## Cross-border points

- **Withholding on payments abroad (§ 43).** Tax is withheld at 19% on Slovak-source income of a non-resident without a registered permanent establishment, such as royalties, interest and certain services. The rate is 35% where the payee is in a non-cooperating state. A treaty or the EU Interest and Royalties Directive can reduce or remove it. For the detailed rules see [sk-cross-border](sk-cross-border.md).
- **Dividends paid abroad.** A dividend paid by a Slovak company to a company is not subject to tax (§ 12(7)(c)). The exception is a recipient company that is a taxpayer of a non-cooperating state (§ 12(7)(c)(1)). That dividend is withheld under § 43(2) (§ 16(1)(e) point 9) at 35% (§ 43(1)(c)).
- **Exit tax (§ 17f).** Moving assets, the seat or the business abroad creates a special base taxed at 21%.
- **Permanent establishments.** The § 21a and § 17k limits and the rate bands apply to a non-resident's Slovak permanent establishment as they do to a resident company.
- **Pillar Two.** Act No. 507/2023 Coll. on top-up tax applies to Slovak members of a multinational or large domestic group whose ultimate parent's consolidated accounts show annual revenue of at least EUR 750,000,000 in at least two of the four preceding periods (§ 3(1)(a)). Those groups also need a top-up tax computation. Not covered here.

## Worked examples

### Example 1: small s.r.o., 10% rate, minimum tax check

Alfa s.r.o. has a calendar 2026 year. Its taxable revenue is EUR 90,000 and its accounting profit is EUR 20,000. It booked EUR 1,500 of representation costs, which are not tax expenses. It has a 2023 tax loss of EUR 4,000 still unused. It has no related-party transactions.

- Base before losses: EUR 20,000 plus EUR 1,500 is EUR 21,500.
- Revenue of EUR 90,000 is above EUR 60,000, so Alfa is not a micro-taxpayer. The loss deduction is capped at 50% of EUR 21,500, EUR 10,750. The whole EUR 4,000 fits.
- Base after losses: EUR 17,500.
- Revenue is not above EUR 100,000, so the rate is 10%: tax EUR 1,750.
- Minimum tax for revenue above EUR 50,000 up to EUR 250,000 is EUR 960. EUR 1,750 is higher, so Alfa pays EUR 1,750 by 31 March 2027.
- 2026 tax is not above EUR 5,000, so there are no advances in 2027.
- The edge: with revenue of EUR 100,500 instead, the rate on the same base would be 21%, tax EUR 3,675. EUR 500 of extra revenue costs EUR 1,925 of tax.

```oa-check
name: Alfa s.r.o., revenue EUR 90,000, profit EUR 20,000, loss EUR 4,000 (2026)
inputs:
  revenue: 90000
  profit: 20000
  addbacks: 1500
  loss_bf: 4000
  min_tax_band: 960
steps:
  - base_before_loss: profit + addbacks
  - loss_cap: base_before_loss * 0.50
  - loss_used: min(loss_bf, loss_cap)
  - base_after_loss: base_before_loss - loss_used
  - tax_10: base_after_loss * 0.10
  - tax_payable: max(tax_10, min_tax_band)
  - tax_if_21: base_after_loss * 0.21
  - cliff_cost: tax_if_21 - tax_10
expected:
  base_before_loss: 21500.00
  loss_cap: 10750.00
  loss_used: 4000.00
  base_after_loss: 17500.00
  tax_10: 1750.00
  tax_payable: 1750.00
  tax_if_21: 3675.00
  cliff_cost: 1925.00
```

### Example 2: large company at 24%, loss cap and advances

Beta a.s. has a calendar 2026 year with taxable revenue of EUR 6,200,000. Its tax base before losses is EUR 300,000. It has EUR 400,000 of tax losses from 2024 and 2025.

- Not a micro-taxpayer, so the loss deduction is capped at 50% of EUR 300,000, EUR 150,000. EUR 250,000 of loss carries forward, within the five-year window.
- Base after losses: EUR 150,000.
- Revenue is above EUR 5,000,000, so the rate is 24%: tax EUR 36,000.
- Minimum tax for revenue above EUR 5,000,000 is EUR 11,520. EUR 36,000 is higher, so it does not bite. Had Beta made a tax loss in 2026, it would still pay EUR 11,520. It could then credit that amount against the part of its 2027 to 2029 tax above the minimum tax.
- The § 42(6) tax for 2026 is EUR 36,000 (base after losses at 24%, no reliefs). It is above EUR 16,600, so once the 2026 return is due (31 March 2027, or the extended date) Beta pays monthly advances of EUR 3,000 (1/12 of EUR 36,000). Until then its 2027 advances follow its 2025 tax (§ 42(7)).

```oa-check
name: Beta a.s., revenue EUR 6,200,000, base EUR 300,000, losses EUR 400,000 (2026)
inputs:
  base_before_loss: 300000
  loss_bf: 400000
  min_tax_band: 11520
steps:
  - loss_cap: base_before_loss * 0.50
  - loss_used: min(loss_bf, loss_cap)
  - loss_cf: loss_bf - loss_used
  - base_after_loss: base_before_loss - loss_used
  - tax_24: base_after_loss * 0.24
  - tax_payable: max(tax_24, min_tax_band)
  - monthly_advance: tax_payable / 12
expected:
  loss_cap: 150000.00
  loss_used: 150000.00
  loss_cf: 250000.00
  base_after_loss: 150000.00
  tax_24: 36000.00
  tax_payable: 36000.00
  monthly_advance: 3000.00
```

## Ask the client first

1. Taxable revenue for the period. It sets the rate band (EUR 100,000 and EUR 5,000,000), the minimum tax band, and micro-taxpayer status (EUR 60,000).
2. The tax period: calendar or fiscal year, and whether it is the company's first period (no minimum tax, no advances).
3. Any transaction with a related person in the period. It removes micro-taxpayer status and brings in § 21a for related-party interest.
4. Unused tax losses by year, and any minimum tax paid in 2023 to 2025 still to be credited.
5. Unpaid year-end items in the § 17(19) list (rent, royalties, advisory and legal fees, penalties), and whether the company recovers its input VAT in full.
6. Foreign income or payments to non-residents, and whether any counterparty is in a non-cooperating state.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 595/2003 Coll. on income tax, consolidated version in force 1 January to 30 December 2026 (§ 2(w), § 2(x), § 12(7), § 15, § 16(1)(e), § 17(19), § 17k, § 21, § 21a, § 22, § 26, § 27, § 30, § 30c, § 42, § 43, § 46b, § 49, § 51e, § 51ea, § 51eb, § 52zzzf, § 52zzzj, § 52zzzk) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 595/2003 Coll., version in force from 1 December 2025 (2025 minimum tax bands, for comparison) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20251201.html | 2026-10-23 |
| Act No. 595/2003 Coll., version in force 31 December 2026 (changes affect individuals only) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20261231.html | 2026-10-23 |
| Act No. 261/2025 Coll. on consolidation of public finances (new § 46b(2), § 51eb, § 52zzzj, § 52zzzk) | https://static.slov-lex.sk/static/SK/ZZ/2025/261/20260101.html | 2026-10-23 |
| Act No. 563/2009 Coll. Tax Procedure Code, version in force from 1 September 2026 (§ 14, § 154, § 155, § 156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 279/2024 Coll. on financial transaction tax, version in force from 1 January 2026 (§ 6) | https://static.slov-lex.sk/static/SK/ZZ/2024/279/20260101.html | 2026-10-23 |
| Ministry of Finance, list of cooperating states under § 2(x), valid from 1 January 2026 | https://www.mfsr.sk/files/archiv/39/Zoznam-spolupracujucich-statov-podla-2-pism-x-zakona-c-595_2003-Z-z_1.1.2026.pdf | 2026-10-23 |
| Act No. 507/2023 Coll. on top-up tax, version in force from 31 December 2025 (§ 3(1)) | https://static.slov-lex.sk/static/SK/ZZ/2023/507/20251231.html | 2026-10-23 |
| European Central Bank, key interest rates (main refinancing rate 2.65% from 16 September 2026) | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-23 |
| Financial Administration, legal persons' income tax return | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-prijmov/pravnicke-osoby/danove-priznanie-dan-prijem-po | 2026-10-23 |

Not yet confirmed: the full 2026 Annex 1 asset classification after the 1 January 2026 changes (Annex 1 is a separate download on slov-lex and was not read; only the group periods in § 26(1) were read); whether the Ministry issues a new DPPO form for 2026 periods (the return page on 23 October 2026 still names MF/012187/2025-721).
