---
name: uk-corporation-tax
description: "UK corporation tax for companies resident in the UK and for non-resident companies trading in the UK through a permanent establishment. Covers the 25% main rate, the 19% small profits rate and marginal relief between GBP 50,000 and GBP 250,000 (limits shared by associated companies and cut for short periods), financial years running from 1 April, the taxable base, capital allowances, trade losses and the GBP 5m deductions allowance, 75% group relief, the dividend exemption and substantial shareholding exemption, corporate interest restriction, CT600 filing with iXBRL accounts, payment 9 months and 1 day after the period end, quarterly instalments for large and very large companies, and penalties. Financial year 2026. Trigger on: UK corporation tax, CT600, marginal relief, small profits rate, associated companies, quarterly instalment payments, group relief, SSE, corporate interest restriction. Out of scope: R&D relief (gb-tax-relief-under-the-merged-scheme), transfer pricing (uk-transf"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-corporation-tax"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# UK corporation tax: rates, marginal relief, CT600, losses and payment dates (financial year 2026)

Corporation tax is charged by financial year. A financial year runs from 1 April to 31 March and is named after the calendar year in which it starts, so financial year 2026 runs from 1 April 2026 to 31 March 2027. A company's accounting period that straddles 31 March is split between the two financial years on a time basis when the rates differ. For financial years 2023 to 2027 the rates, limits and fraction are the same, so current periods need no split.

The law is mainly the Corporation Tax Act 2009 (CTA 2009), the Corporation Tax Act 2010 (CTA 2010), the Taxation (International and Other Provisions) Act 2010 (TIOPA 2010), the Taxation of Chargeable Gains Act 1992 (TCGA 1992), Schedule 18 to the Finance Act 1998 (returns and penalties) and the yearly Finance Acts. HMRC's own guidance is on gov.uk and in the HMRC internal manuals.

## Who this applies to

- **UK resident companies.** A company incorporated in the UK is UK resident for corporation tax ([CTA 2009 s14](https://www.legislation.gov.uk/ukpga/2009/4/section/14)). A company incorporated abroad can also be UK resident if its central management and control is in the UK. A UK resident company is charged on all its profits wherever they arise, subject to an election to exempt the profits of foreign permanent establishments ([CTA 2009 s5(1)](https://www.legislation.gov.uk/ukpga/2009/4/section/5)).
- **Non-resident companies.** A non-UK resident company is within corporation tax only if it trades in the UK through a permanent establishment, deals in or develops UK land, carries on a UK property business, or has other UK property income ([CTA 2009 s5(2)](https://www.legislation.gov.uk/ukpga/2009/4/section/5)). A permanent establishment is charged on the profits attributable to it ([CTA 2009 s5(3) and s19](https://www.legislation.gov.uk/ukpga/2009/4/section/5)).
- **Also within corporation tax:** clubs, societies, co-operatives and other unincorporated associations, and the UK property income of non-resident companies.
- **Out of scope of this skill:** partnerships and LLPs (their members are taxed instead), sole traders, oil and gas ring fence profits (separate rates), banks and insurers' special regimes, REITs, investment trusts and authorised funds (unit trusts and OEICs pay 20%), tonnage tax, and charities' exemptions.
- **Non-UK resident companies** cannot use the small profits rate or marginal relief, because both require the company to be UK resident in the period. A UK permanent establishment of a foreign company therefore pays the 25% main rate on all its profits ([CTA 2010 s18A(1)(a)](https://www.legislation.gov.uk/ukpga/2010/4/section/18A), [s18B(1)(a)](https://www.legislation.gov.uk/ukpga/2010/4/section/18B); [HMRC marginal relief guidance](https://www.gov.uk/guidance/corporation-tax-marginal-relief)).
- **Close investment-holding companies** cannot use the small profits rate or marginal relief and pay the main rate on all profits ([CTA 2010 s18A(1)(b)](https://www.legislation.gov.uk/ukpga/2010/4/section/18A), [s18B(1)(b)](https://www.legislation.gov.uk/ukpga/2010/4/section/18B)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Main rate (profits over the upper limit) | 25% | FY2026 (1 Apr 2026 to 31 Mar 2027); same for FY2023 to FY2025 | [Finance Act 2025 s13](https://www.legislation.gov.uk/ukpga/2025/8/section/13); [HMRC rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) |
| Small profits rate (profits at or below the lower limit) | 19% | FY2026 | [Finance Act 2025 s14](https://www.legislation.gov.uk/ukpga/2025/8/section/14) |
| Lower limit | £50,000 | FY2026 | [CTA 2010 s18D](https://www.legislation.gov.uk/ukpga/2010/4/section/18D) |
| Upper limit | £250,000 | FY2026 | [CTA 2010 s18D](https://www.legislation.gov.uk/ukpga/2010/4/section/18D) |
| Standard marginal relief fraction | 3/200 | FY2026 | [Finance Act 2025 s14](https://www.legislation.gov.uk/ukpga/2025/8/section/14) |
| Main rate, small profits rate and fraction, next year | 25%, 19% and 3/200 (limits unchanged at £50,000 and £250,000) | FY2027 (1 Apr 2027 to 31 Mar 2028) | [Finance Act 2026 s11](https://www.legislation.gov.uk/ukpga/2026/11/section/11); [Finance Act 2026 s12](https://www.legislation.gov.uk/ukpga/2026/11/section/12); [CTA 2010 s18D](https://www.legislation.gov.uk/ukpga/2010/4/section/18D) |
| Marginal relief formula | F x (U - A) x N / A | all years from FY2023 | [CTA 2010 s18B](https://www.legislation.gov.uk/ukpga/2010/4/section/18B); [HMRC CTM03925](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03925) |
| Associated companies | both limits divided by (1 + number of associated companies) | FY2026 | [HMRC marginal relief guidance](https://www.gov.uk/guidance/corporation-tax-marginal-relief) |
| Short accounting period | both limits reduced in proportion | FY2026 | [CTA 2010 s18D](https://www.legislation.gov.uk/ukpga/2010/4/section/18D) |
| Unit trusts and OEICs | 20% | FY2026 | [HMRC rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) |
| Ring fence profits (oil and gas) | 30% main, 19% small, fraction 11/400 | FY2026 | [HMRC rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) |
| Loss deductions allowance (company not in a group) | £5,000,000 a year, cut for short periods | FY2026 | [CTA 2010 s269ZW](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZW) |
| Loss deductions allowance (group) | one £5,000,000 shared across the group | FY2026 | [CTA 2010 s269ZR](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZR) |
| Profits above the deductions allowance that brought-forward losses can cover | 50% | FY2026 | [CTA 2010 s269ZB](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZB); [s269ZD](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZD) |
| Corporate interest restriction de minimis | £2,000,000 net interest a year for the worldwide group | FY2026 | [TIOPA 2010 s392](https://www.legislation.gov.uk/ukpga/2010/8/section/392) |
| Corporate interest restriction fixed ratio | 30% of tax-EBITDA (lower of that and the fixed ratio debt cap) | FY2026 | [TIOPA 2010 s397](https://www.legislation.gov.uk/ukpga/2010/8/section/397) |
| Annual Investment Allowance | £1,000,000 | since 1 Jan 2019 | [gov.uk AIA](https://www.gov.uk/capital-allowances/annual-investment-allowance) |
| Full expensing (new main rate plant, companies only) | 100% first-year allowance | expenditure from 1 Apr 2023 | [CAA 2001 s45S](https://www.legislation.gov.uk/ukpga/2001/2/section/45S); [HMRC CA23174AA](https://www.gov.uk/hmrc-internal-manuals/capital-allowances-manual/ca23174aa) |
| Special rate plant first-year allowance (companies) | 50% | expenditure from 1 Apr 2023 | [HMRC CA23174AA](https://www.gov.uk/hmrc-internal-manuals/capital-allowances-manual/ca23174aa) |
| New first-year allowance (new main rate plant, includes some leased plant) | 40% | expenditure from 1 Jan 2026 | [Finance Act 2026 s29 (new CAA 2001 s45U)](https://www.legislation.gov.uk/ukpga/2026/11/section/29) |
| Main pool writing-down allowance | 14% (was 18%); hybrid rate for a period spanning 1 Apr 2026 | periods from 1 Apr 2026 | [Finance Act 2026 s28](https://www.legislation.gov.uk/ukpga/2026/11/section/28) |
| Large company (quarterly instalments) | profits over £1.5m, shared by associated companies | FY2026 | [HMRC instalments guidance](https://www.gov.uk/guidance/corporation-tax-paying-in-instalments) |
| Very large company (earlier instalments) | profits over £20m; for periods beginning on or after 1 Apr 2023 divided by (1 + number of associated companies) | periods from 1 Apr 2019 | [SI 2017/1072](https://www.legislation.gov.uk/uksi/2017/1072/made); [HMRC very large company guidance](https://www.gov.uk/guidance/pay-corporation-tax-if-youre-a-very-large-company) |
| Pillar Two | Multinational top-up tax and domestic top-up tax at a 15% minimum rate for groups with revenue over EUR 750m in two of the four prior periods; in force for periods beginning on or after 31 Dec 2023 (UTPR from 31 Dec 2024) | in force | [HMRC MTT01100](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt01100); [HMRC MTT01010](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt01010) |

There is no local or regional tax on company profits in the UK and no minimum tax for ordinary companies outside Pillar Two.

**How marginal relief works.** Work out tax on taxable total profits (N) at the 25% main rate. Then deduct marginal relief: 3/200 x (upper limit - augmented profits) x (taxable total profits / augmented profits). Augmented profits (A) are taxable total profits plus exempt distributions received, other than distributions from a 51% subsidiary or a company of which the recipient is a 51% subsidiary ([CTA 2010 s18L](https://www.legislation.gov.uk/ukpga/2010/4/section/18L)). Between the limits the effective marginal rate on each extra pound is 26.5%. If augmented profits are at or below the lower limit, the whole of taxable total profits is taxed at 19%.

**Associated companies.** Two companies are associated if one controls the other or both are under the control of the same person or persons. Rights held by a participator's associates (such as relatives) are counted only where there is substantial commercial interdependence between the companies; rights the participators hold themselves always count ([HMRC CTM03950](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03950)). HMRC's example: a company with 3 other associated companies divides the limits by 4, giving a lower limit of £12,500 and an upper limit of £62,500 ([HMRC marginal relief guidance](https://www.gov.uk/guidance/corporation-tax-marginal-relief)).

**Next year.** Finance Act 2026 charges corporation tax for financial year 2027 (1 April 2027 to 31 March 2028) at a 25% main rate ([s11](https://www.legislation.gov.uk/ukpga/2026/11/section/11)), with a 19% standard small profits rate and a 3/200 standard marginal relief fraction ([s12](https://www.legislation.gov.uk/ukpga/2026/11/section/12)). The £50,000 and £250,000 limits are fixed in CTA 2010 s18D and did not change, so an accounting period straddling 31 March 2027 needs no split.

## The taxable base

Start with the profit before tax in the accounts (UK GAAP or IFRS) and adjust it into taxable total profits.

1. **Trading profit.** Add back expenses not incurred wholly and exclusively for the trade, depreciation and amortisation of plant (capital allowances replace it), client entertaining, fines and penalties, general provisions, and capital items charged to profit and loss. Deduct income taxed elsewhere in the computation (for example property income or exempt dividends).
2. **Capital allowances.** Plant and machinery goes through the Annual Investment Allowance (£1m), full expensing (100% on new, unused main rate plant bought by a company), the 50% special rate allowance, the new 40% first-year allowance from 1 January 2026, or the main pool at 14% (from 1 April 2026) and the special rate pool. Disposals of fully expensed assets give a balancing charge.
3. **Loan relationships and intangibles.** Interest and other finance costs follow the accounts under the loan relationship rules in CTA 2009 Parts 5 and 6. Intangible fixed assets created or acquired from 1 April 2002 follow CTA 2009 Part 8.
4. **Other income and gains.** Add UK property business profits, non-trading loan relationship credits and chargeable gains. Companies still get indexation allowance on gains, frozen at December 2017 ([HMRC rates and allowances](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax)).
5. **Dividends received are mostly exempt.** For a small company, a dividend is exempt if the payer is resident in the UK or a qualifying territory and the other conditions in [CTA 2009 s931B](https://www.legislation.gov.uk/ukpga/2009/4/section/931B) are met. For other companies a dividend is exempt if it falls into an exempt class in [CTA 2009 ss931E to 931Q](https://www.legislation.gov.uk/ukpga/2009/4/part/9A/chapter/3), which include distributions from controlled companies, on non-redeemable ordinary shares and on portfolio holdings of less than 10%. Exempt dividends still count in augmented profits for marginal relief unless they come from a 51% group company.
6. **Substantial shareholding exemption (SSE).** A gain on selling shares is not a chargeable gain where the investing company held at least 10% of the ordinary share capital for a continuous 12 months beginning not more than six years before the sale, and the company sold is a trading company or the holding company of a trading group ([TCGA 1992 Sch 7AC paras 1, 7, 8 and 19](https://www.legislation.gov.uk/ukpga/1992/12/schedule/7AC)).
7. **Corporate interest restriction.** A worldwide group whose net interest expense in the UK is £2m a year or less is not restricted. Above that, net interest deductions are capped at the interest capacity, broadly 30% of tax-EBITDA under the fixed ratio method, or the group ratio if elected ([TIOPA 2010 s392](https://www.legislation.gov.uk/ukpga/2010/8/section/392), [s397](https://www.legislation.gov.uk/ukpga/2010/8/section/397)). Groups over the de minimis file an interest restriction return.
8. **Trade losses.**
   - **Current year and carry back.** A trade loss can be set against total profits of the same period and, if the claim requires, the previous 12 months ([CTA 2010 s37](https://www.legislation.gov.uk/ukpga/2010/4/section/37)). The claim must be made within two years after the end of the loss-making period.
   - **Carry forward.** Losses arising from 1 April 2017 that are not used can be carried forward and set against total profits of later periods, on a claim made within two years after the end of the later period, provided the trade continues ([CTA 2010 s45A](https://www.legislation.gov.uk/ukpga/2010/4/section/45A)).
   - **Restriction for large profits.** Brought-forward losses can cover profits up to the deductions allowance (£5m a year for a single company or group) plus 50% of profits above it ([CTA 2010 s269ZB](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZB) for losses set against trading profits, [s269ZD](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZD) for post-2017 losses set against total profits, [s269ZW](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZW)). A group nominates a company to allocate its single £5m allowance ([s269ZR](https://www.legislation.gov.uk/ukpga/2010/4/section/269ZR)).
9. **Group relief.** Two companies are in the same group if one is a 75% subsidiary of the other or both are 75% subsidiaries of a third company ([CTA 2010 s152](https://www.legislation.gov.uk/ukpga/2010/4/section/152)). Current-year losses and other amounts can be surrendered between UK-related group members: UK residents and non-residents within corporation tax, such as through a UK permanent establishment ([HMRC CTM80150](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm80150)). Carried-forward losses from 1 April 2017 can also be group relieved, subject to the same deductions allowance.

## Deadlines and filing

| Step | Deadline | Source |
|---|---|---|
| Tell HMRC the company is within corporation tax | within 3 months after the start of its first accounting period | [Finance Act 2004 s55](https://www.legislation.gov.uk/ukpga/2004/12/section/55) |
| Pay corporation tax (not large) | 9 months and 1 day after the end of the accounting period | [gov.uk Pay Corporation Tax](https://www.gov.uk/pay-corporation-tax) |
| Large company (profits over £1.5m, under £20m) | four equal instalments: 6 months 13 days after the start of the period, then every 3 months, the last 3 months 14 days after the period ends (months 7, 10, 13 and 16 of a 12-month period) | [HMRC instalments guidance](https://www.gov.uk/guidance/corporation-tax-paying-in-instalments) |
| Very large company (profits over £20m, divided among associated companies) | four instalments on the 14th day of months 3, 6, 9 and 12 of the period | [HMRC CTM92805](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm92805); [HMRC very large company guidance](https://www.gov.uk/guidance/pay-corporation-tax-if-youre-a-very-large-company) |
| File the Company Tax Return (CT600) | 12 months after the end of the accounting period | [gov.uk Company Tax Returns](https://www.gov.uk/company-tax-returns) |

- **Large company exceptions.** No instalments are needed if the total liability is under £10,000. Nor are they needed if profits are no more than £10m and either the company did not exist (or had no accounting period) in the previous 12 months, or for any period ending in the previous 12 months its annual rate of profit was no more than £1.5m or its tax no more than £10,000 ([HMRC instalments guidance](https://www.gov.uk/guidance/corporation-tax-paying-in-instalments)). There is no such first-period grace for very large companies, though the £10,000 liability exception still applies to them ([HMRC very large company guidance](https://www.gov.uk/guidance/pay-corporation-tax-if-youre-a-very-large-company)).
- **The return.** The return is form CT600; the current version is "Company Tax Return CT600 (2026) Version 3" ([gov.uk CT600](https://www.gov.uk/government/publications/corporation-tax-company-tax-return-ct600-2015-version-3)). It must be filed online, and the accounts and tax computations must be in iXBRL format ([HMRC COM60040](https://www.gov.uk/hmrc-internal-manuals/cotax-manual/com60040)). HMRC's free 'File your accounts and Company Tax Return' service closed on 31 March 2026; from 1 April 2026 returns are filed through commercial software, and a paper CT600 is allowed only with a reasonable excuse or when filing in Welsh ([gov.uk closure guidance](https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return)).
- **Accounting periods.** An accounting period for corporation tax cannot exceed 12 months. A company with a longer period of accounts files two returns: the first 12 months, then the rest.
- **Companies House** accounts are a separate filing with separate deadlines. See uk-financial-statements.

## Penalties and interest

| Failure | Penalty or rate | Source |
|---|---|---|
| Return late, filing date on or after 1 April 2026 | £200 flat; £400 if more than 3 months late | [FA 1998 Sch 18 para 17(2)](https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/17); [Finance Act 2026 s265](https://www.legislation.gov.uk/ukpga/2026/11/section/265) |
| Third return in a row late, filing date on or after 1 April 2026 | £1,000 flat; £2,000 if more than 3 months late | [FA 1998 Sch 18 para 17(3)](https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/17); [Finance Act 2026 s265](https://www.legislation.gov.uk/ukpga/2026/11/section/265) |
| Return late, filing date before 1 April 2026 | £100 flat; £200 if more than 3 months late; third in a row £500 and £1,000 | [Finance Act 2026 s265](https://www.legislation.gov.uk/ukpga/2026/11/section/265) (the amounts it replaced) |
| Return not filed within 18 months of the period end | extra 10% of unpaid tax; 20% if filed more than 2 years after the period end | [FA 1998 Sch 18 para 18](https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/18) |
| Inaccurate return | up to 30% (careless), 70% (deliberate) or 100% (deliberate and concealed) of the potential lost revenue for a domestic (category 1) inaccuracy, reduced for disclosure; higher maximums for offshore categories 2 and 3 | [FA 2007 Sch 24 para 4](https://www.legislation.gov.uk/ukpga/2007/11/schedule/24/paragraph/4) |
| Late payment interest | Bank of England base rate plus 4% (from 6 April 2025); 7.75% from 9 January 2026 | [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates) |
| Underpaid quarterly instalments | 6.25% from 29 December 2025 | [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates) |
| Repayment interest | base rate minus 1%, minimum 0.5%; 2.75% from 9 January 2026 | [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates) |

The doubled flat penalties apply to returns whose filing date is 1 April 2026 or later, which for a company on the normal 12-month filing date means accounting periods ending on or after 1 April 2025; earlier returns keep £100, £200, £500 and £1,000 ([Finance Act 2026 s265(2)](https://www.legislation.gov.uk/ukpga/2026/11/section/265)). HMRC may now change these amounts by regulations (new para 17(5)). The HMRC interest page was last updated on 23 December 2025, and the Bank of England's Bank Rate has stayed at 3.75% since 18 December 2025 ([Bank of England Bank Rate history](https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp)), so the rates above were current when read; they move with Bank Rate, so check on the day you compute. There is no separate fixed late payment penalty for corporation tax; interest runs from the due date. HMRC estimates the tax (a determination) if the return is 6 months late ([gov.uk late filing penalties](https://www.gov.uk/company-tax-returns/penalties-for-late-filing)).

## Cross-border points

- **Dividends paid.** A UK company does not withhold tax on ordinary dividends it pays, to residents or non-residents. HMRC's manual states that UK dividend income remains non-taxable for most non-UK residents ([HMRC SAIM5120](https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim5120)). REIT property income distributions have their own rules and are out of scope.
- **Interest paid.** A company paying yearly interest arising in the UK must deduct income tax ([ITA 2007 s874](https://www.legislation.gov.uk/ukpga/2007/3/section/874)). For payments in 2026-27 the rate is the basic rate, 20% ([Finance Act 2026 s2](https://www.legislation.gov.uk/ukpga/2026/11/section/2)). From 2027-28 s874(2) refers to the savings basic rate instead ([Finance Act 2026 Sch 1 para 29](https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/29)), which is 22% for 2027-28 ([Finance Act 2026 s5](https://www.legislation.gov.uk/ukpga/2026/11/section/5)), so interest paid on or after 6 April 2027 has 22% deducted. Exceptions (payments to UK companies, quoted Eurobonds, and others in ITA 2007 ss875 to 888E) and treaty relief can remove or reduce it.
- **Royalties paid.** Basic rate income tax (20% in 2026-27; these sections were not moved to the savings rate) is deducted from UK patent royalties ([ITA 2007 s903](https://www.legislation.gov.uk/ukpga/2007/3/section/903)) and from royalties for intellectual property where the owner's usual place of abode is outside the UK ([ITA 2007 s906](https://www.legislation.gov.uk/ukpga/2007/3/section/906)). Treaties can reduce this.
- **No EU directives.** The UK left the EU, so the Parent-Subsidiary and Interest and Royalties Directives no longer apply. Relief now comes from domestic law and the treaty network.
- **Controlled foreign companies.** TIOPA 2010 Part 9A can charge a UK company on profits of a foreign company it controls with others, where those profits pass through the CFC charge gateway and no entity-level exemption applies (exempt period, excluded territories, low profits, low profit margin, tax exemption) ([HMRC INTM190000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm190000)). Check this whenever a UK company owns a low-taxed foreign subsidiary.
- **Foreign branches.** A UK company can elect to exempt the profits of all its foreign permanent establishments ([CTA 2009 s5(1)](https://www.legislation.gov.uk/ukpga/2009/4/section/5)).
- **Exit tax.** A company that stops being UK resident is treated as selling and buying back its assets at market value just before it leaves ([TCGA 1992 s185](https://www.legislation.gov.uk/ukpga/1992/12/section/185)). A company moving to a relevant EEA state can apply, within 9 months after the period end, for an exit charge payment plan spreading the tax over six equal annual instalments ([TMA 1970 Sch 3ZB](https://www.legislation.gov.uk/ukpga/1970/9/schedule/3ZB)).
- **Transfer pricing** between related parties is in uk-transfer-pricing.

## Worked examples

### Example 1: a simple trading company

Brightwell Joinery Ltd has no associated companies and no dividend income. Its accounts run for the year 1 April 2026 to 31 March 2027, which falls wholly in financial year 2026. Profit before tax is £180,000. The accounts charge £22,000 of depreciation and £3,000 of client entertaining. In the year it bought a new CNC machine for £30,000, which qualifies for full expensing.

Taxable trading profit is 180,000 + 22,000 + 3,000 - 30,000 = £175,000. That is between the £50,000 and £250,000 limits, so marginal relief applies. Tax at the main rate is 175,000 x 25% = £43,750. Marginal relief is 3/200 x (250,000 - 175,000) x 175,000 / 175,000 = £1,125. Corporation tax payable is £42,625. It is not a large company, so the tax is due on 1 January 2028 (9 months and 1 day after 31 March 2027) and the CT600 is due by 31 March 2028.

```oa-check
name: Single company, taxable profit GBP 175,000, FY2026, no associated companies
inputs:
  accounts_profit: 180000
  depreciation: 22000
  entertaining: 3000
  full_expensing: 30000
  main_rate: 25
  lower_limit: 50000
  upper_limit: 250000
steps:
  - fraction: 3 / 200
  - ttp: accounts_profit + depreciation + entertaining - full_expensing
  - augmented: ttp
  - tax_main: pct(ttp, main_rate)
  - marginal_relief: fraction * (upper_limit - augmented) * ttp / augmented
  - ct: tax_main - marginal_relief
expected:
  ttp: 175000
  tax_main: 43750
  marginal_relief: 1125
  ct: 42625
```

### Example 2: losses brought forward, one associated company and an exempt dividend

Harrow Lane Trading Ltd is controlled by the same individual who controls one other trading company, so it has one associated company. The limits are divided by 2: lower limit £25,000, upper limit £125,000. Its year runs 1 April 2026 to 31 March 2027. Adjusted trading profit is £140,000. It has £60,000 of trade losses brought forward from the year to 31 March 2026. It also received a £10,000 dividend on a 4% holding in an unrelated UK company, which is exempt as a portfolio holding but counts in augmented profits.

The loss is well under the £5m deductions allowance, so all of it can be used: taxable total profits are 140,000 - 60,000 = £80,000. Augmented profits are 80,000 + 10,000 = £90,000, which is between the reduced limits. Tax at the main rate is 80,000 x 25% = £20,000. Marginal relief is 3/200 x (125,000 - 90,000) x 80,000 / 90,000 = £466.67. Corporation tax payable is £19,533.33. Without the associated company, augmented profits of £90,000 would sit further below the £250,000 upper limit and the relief would be larger; the association costs this company tax.

```oa-check
name: Losses brought forward, one associated company, exempt portfolio dividend, FY2026
inputs:
  trading_profit: 140000
  losses_bf: 60000
  exempt_dividend: 10000
  associated: 1
  deductions_allowance: 5000000
  main_rate: 25
steps:
  - fraction: 3 / 200
  - lower_limit: 50000 / (1 + associated)
  - upper_limit: 250000 / (1 + associated)
  - loss_cap: min(trading_profit, deductions_allowance) + pct(max(trading_profit - deductions_allowance, 0), 50)
  - loss_used: min(losses_bf, loss_cap)
  - ttp: trading_profit - loss_used
  - augmented: ttp + exempt_dividend
  - tax_main: pct(ttp, main_rate)
  - marginal_relief: round(fraction * (upper_limit - augmented) * ttp / augmented, 2)
  - ct: tax_main - marginal_relief
expected:
  lower_limit: 25000
  upper_limit: 125000
  loss_used: 60000
  ttp: 80000
  augmented: 90000
  tax_main: 20000
  marginal_relief: 466.67
  ct: 19533.33
```

## Ask the client first

1. **Associated companies.** Who controls the company, and what other companies do they (and, where there is commercial interdependence, their relatives) control? This sets the limits and the instalment thresholds.
2. **Accounting period dates.** Does the period run 12 months, is it short, or does the set of accounts run longer than 12 months (two returns)?
3. **Losses and group.** Are there trade losses brought forward, from before or after 1 April 2017, and is the company in a 75% group that can surrender or claim losses?
4. **Dividends and share sales.** Did it receive dividends or sell shares in the period, and what percentage holdings were involved (marginal relief, SSE)?
5. **Size.** Were augmented profits over £1.5m (shared by associated companies) this year or last year? That decides quarterly instalments.
6. **Foreign links.** Is it UK incorporated, or managed from abroad; does it have foreign branches or subsidiaries, or pay interest or royalties abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| HMRC: rates and allowances, Corporation Tax | https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax | 2026-10-22 |
| gov.uk: Corporation Tax rates | https://www.gov.uk/corporation-tax-rates | 2026-10-22 |
| HMRC: Marginal Relief guidance | https://www.gov.uk/guidance/corporation-tax-marginal-relief | 2026-10-22 |
| HMRC manual CTM03925 (marginal relief formula and example) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03925 | 2026-10-22 |
| HMRC manual CTM03910 (rates, limits, fractions FY2023 to FY2025) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03910 | 2026-10-22 |
| HMRC manual CTM03950 (associated companies) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03950 | 2026-10-22 |
| Finance Act 2025 s13 (charge and main rate FY2026) | https://www.legislation.gov.uk/ukpga/2025/8/section/13 | 2026-10-22 |
| Finance Act 2025 s14 (small profits rate and fraction FY2026) | https://www.legislation.gov.uk/ukpga/2025/8/section/14 | 2026-10-22 |
| Finance Act 2026 contents | https://www.legislation.gov.uk/ukpga/2026/11/contents | 2026-10-22 |
| Finance Act 2026 s11 (charge and main rate FY2027) | https://www.legislation.gov.uk/ukpga/2026/11/section/11 | 2026-10-22 |
| Finance Act 2026 s12 (small profits rate and fraction FY2027) | https://www.legislation.gov.uk/ukpga/2026/11/section/12 | 2026-10-22 |
| Finance Act 2026 s2 (basic rate 2026-27) | https://www.legislation.gov.uk/ukpga/2026/11/section/2 | 2026-10-22 |
| Finance Act 2026 s5 (savings basic rate 22% for 2027-28) | https://www.legislation.gov.uk/ukpga/2026/11/section/5 | 2026-10-22 |
| Finance Act 2026 Sch 1 para 29 (ITA 2007 s874(2) moved to the savings basic rate) | https://www.legislation.gov.uk/ukpga/2026/11/schedule/1/paragraph/29 | 2026-10-22 |
| Finance Act 2026 s28 (writing-down allowance 14%) | https://www.legislation.gov.uk/ukpga/2026/11/section/28 | 2026-10-22 |
| Finance Act 2026 s29 (40% first-year allowance) | https://www.legislation.gov.uk/ukpga/2026/11/section/29 | 2026-10-22 |
| Finance Act 2026 s265 (late filing penalty commencement) | https://www.legislation.gov.uk/ukpga/2026/11/section/265 | 2026-10-22 |
| CTA 2009 s5 (territorial scope) | https://www.legislation.gov.uk/ukpga/2009/4/section/5 | 2026-10-22 |
| CTA 2009 s14 (UK incorporated companies resident) | https://www.legislation.gov.uk/ukpga/2009/4/section/14 | 2026-10-22 |
| CTA 2009 s931A and s931B (dividend exemption) | https://www.legislation.gov.uk/ukpga/2009/4/section/931B | 2026-10-22 |
| CTA 2009 Part 9A Chapter 3 (exempt classes) | https://www.legislation.gov.uk/ukpga/2009/4/part/9A/chapter/3 | 2026-10-22 |
| CTA 2010 s18A (small profits rate: UK resident, not a close investment-holding company) | https://www.legislation.gov.uk/ukpga/2010/4/section/18A | 2026-10-22 |
| CTA 2010 s18B, s18D, s18L (marginal relief) | https://www.legislation.gov.uk/ukpga/2010/4/section/18B | 2026-10-22 |
| CTA 2010 s37 (current year and carry back) | https://www.legislation.gov.uk/ukpga/2010/4/section/37 | 2026-10-22 |
| CTA 2010 s45A (carry forward) | https://www.legislation.gov.uk/ukpga/2010/4/section/45A | 2026-10-22 |
| CTA 2010 s152 (75% group) | https://www.legislation.gov.uk/ukpga/2010/4/section/152 | 2026-10-22 |
| CTA 2010 s269ZB, s269ZR, s269ZW (loss restriction, deductions allowance) | https://www.legislation.gov.uk/ukpga/2010/4/section/269ZW | 2026-10-22 |
| CTA 2010 s269ZD (restriction on deductions from total profits) | https://www.legislation.gov.uk/ukpga/2010/4/section/269ZD | 2026-10-22 |
| HMRC manual CTM80150 (group relief: who can claim) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm80150 | 2026-10-22 |
| TIOPA 2010 s392 and s397 (corporate interest restriction) | https://www.legislation.gov.uk/ukpga/2010/8/section/392 | 2026-10-22 |
| TCGA 1992 Sch 7AC (substantial shareholding exemption) | https://www.legislation.gov.uk/ukpga/1992/12/schedule/7AC | 2026-10-22 |
| TCGA 1992 s185 (company ceasing to be resident) | https://www.legislation.gov.uk/ukpga/1992/12/section/185 | 2026-10-22 |
| TMA 1970 Sch 3ZB (exit charge payment plans) | https://www.legislation.gov.uk/ukpga/1970/9/schedule/3ZB | 2026-10-22 |
| CAA 2001 s45S (full expensing) | https://www.legislation.gov.uk/ukpga/2001/2/section/45S | 2026-10-22 |
| HMRC manual CA23174AA (full expensing 100%, special rate 50%) | https://www.gov.uk/hmrc-internal-manuals/capital-allowances-manual/ca23174aa | 2026-10-22 |
| gov.uk: Annual Investment Allowance | https://www.gov.uk/capital-allowances/annual-investment-allowance | 2026-10-22 |
| Finance Act 2004 s55 (notice of chargeability) | https://www.legislation.gov.uk/ukpga/2004/12/section/55 | 2026-10-22 |
| gov.uk: Pay Corporation Tax | https://www.gov.uk/pay-corporation-tax | 2026-10-22 |
| HMRC: paying Corporation Tax in instalments | https://www.gov.uk/guidance/corporation-tax-paying-in-instalments | 2026-10-22 |
| HMRC manual CTM92805 (very large company instalment dates) | https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm92805 | 2026-10-22 |
| HMRC: paying Corporation Tax as a very large company | https://www.gov.uk/guidance/pay-corporation-tax-if-youre-a-very-large-company | 2026-10-22 |
| SI 2017/1072 (very large companies) | https://www.legislation.gov.uk/uksi/2017/1072/made | 2026-10-22 |
| gov.uk: Company Tax Returns | https://www.gov.uk/company-tax-returns | 2026-10-22 |
| gov.uk: CT600 (2026) Version 3 | https://www.gov.uk/government/publications/corporation-tax-company-tax-return-ct600-2015-version-3 | 2026-10-22 |
| HMRC manual COM60040 (online filing, iXBRL) | https://www.gov.uk/hmrc-internal-manuals/cotax-manual/com60040 | 2026-10-22 |
| gov.uk: closure of HMRC's free CT filing service on 31 March 2026 | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return | 2026-10-22 |
| gov.uk: late filing penalties | https://www.gov.uk/company-tax-returns/penalties-for-late-filing | 2026-10-22 |
| FA 1998 Sch 18 paras 17 and 18 (late filing penalties) | https://www.legislation.gov.uk/ukpga/1998/36/schedule/18/paragraph/17 | 2026-10-22 |
| FA 2007 Sch 24 para 4 (inaccuracy penalties) | https://www.legislation.gov.uk/ukpga/2007/11/schedule/24/paragraph/4 | 2026-10-22 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-22 |
| Bank of England: Bank Rate history | https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp | 2026-10-22 |
| ITA 2007 s874, s903, s906 (deduction from interest and royalties) | https://www.legislation.gov.uk/ukpga/2007/3/section/874 | 2026-10-22 |
| gov.uk: Income Tax rates (basic rate 2026-27) | https://www.gov.uk/income-tax-rates | 2026-10-22 |
| HMRC manual SAIM5120 (dividends received by non-residents) | https://www.gov.uk/hmrc-internal-manuals/savings-and-investment-manual/saim5120 | 2026-10-22 |
| HMRC manual INTM190000 (controlled foreign companies) | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm190000 | 2026-10-22 |
| HMRC manuals MTT01100 and MTT01010 (Pillar Two) | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt01100 | 2026-10-22 |

Not yet confirmed: whether a tax treaty's non-discrimination article lets a UK permanent establishment of a non-resident company use the small profits rate or marginal relief despite CTA 2010 ss18A and 18B.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-corporation-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-corporation-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
