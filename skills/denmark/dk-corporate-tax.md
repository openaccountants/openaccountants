---
name: dk-corporate-tax
description: "Danish corporate income tax (selskabsskat) for companies resident in Denmark (A/S, ApS and other limited companies) and for permanent establishments of foreign companies, income year 2026. Covers the 22% rate (Selskabsskatteloven § 17) and the higher rate for financial companies, the taxable base, participation exemption for subsidiary and group shares, loss carry-forward with the DKK 21,830,700 limit and the 60% rule, mandatory national joint taxation (sambeskatning) and the administration company, the interest limitation rules, acontoskat in March and November, the restskattetillæg, the oplysningsskema deadline, exit tax and withholding on outbound dividends, interest and royalties. Trigger on: Danish corporate tax, selskabsskat, ApS tax, acontoskat, sambeskatning, underskudsfremførsel, rentefradragsbegrænsning, udbytteskat, Denmark 22%. Out of scope: individuals and the self-employed (dk-income-tax), shareholders' share income (dk-capital-gains), VAT (denmark-vat-return), payroll, transfer pricing documentation, tonnage tax, hydrocarbon tax and foundations."
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

# Denmark: corporate income tax (selskabsskat) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts, elections, deadlines or filings. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Denmark.

Tax year: income year 2026 (indkomståret 2026). Most companies use the calendar year. A company with a different financial year (forskudt indkomstår) is taxed for the income year that the financial year "replaces" (Selskabsskatteloven § 29 A, stk. 1). Currency: Danish kroner (DKK). Authority: Skattestyrelsen (skat.dk). Statute: Selskabsskatteloven, LBK nr. 279 of 13 March 2025, as later amended (see Sources).

See also: dk-income-tax (individuals and the self-employed), dk-capital-gains (individual share gains), denmark-vat-return (VAT).

## Who this applies to

**Resident companies.** Selskabsskatteloven (SEL) § 1, stk. 1 taxes companies resident in Denmark on their worldwide income, subject to the territorial rule for foreign permanent establishments and real property (SEL § 8). The main entities are registered aktieselskaber (A/S) and anpartsselskaber (ApS) (§ 1, stk. 1, nr. 1) and other companies where no participant has personal liability and profit is shared by capital (§ 1, stk. 1, nr. 2). A company in § 1, stk. 1, nr. 2-6 is resident if it is registered in Denmark or has its place of management (ledelsens sæde) here (§ 1, stk. 6).

**Foreign companies with Danish income.** SEL § 2 makes a foreign company taxable in Denmark when it:
- carries on business through a permanent establishment (fast driftssted) here (§ 2, stk. 1, litra a). Building, construction or installation work is a permanent establishment from day one (§ 2, stk. 2). Profit is attributed on an arm's length basis (§ 2, stk. 7);
- earns income from Danish real property (litra b);
- receives Danish dividends, interest on controlled debt, or royalties (litra c, d, g). These are taxed by withholding; see Cross-border points.

**Transparent entities.** Partnerships (I/S, K/S) are not taxed under SEL; the partners are. SEL § 2 C can reclassify a transparent entity or branch as a taxable company where more than 50% is held by related parties in states that treat it as non-transparent (hybrid mismatch rule; amended by lov nr. 750 of 20 June 2025).

**Out of scope here:** cooperatives taxed at 14.3% (SEL § 19), foundations (fondsbeskatningsloven), investment companies and investment institutions, tonnage-taxed shipping and hydrocarbon income. Hydrocarbon income under kulbrinteskatteloven § 4 carries a 3 percentage point additional corporate tax (SEL § 17, stk. 1, 2. pkt.).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax (selskabsskat) | 22% of taxable income | 2026 | SEL § 17, stk. 1; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven |
| Financial companies (banks, mortgage credit, insurers, investment firms and others listed in § 17 A, stk. 3) | Taxable income multiplied by 26/22, so an effective 26% | 2026 | SEL § 17 A; svmn.dk table (above) |
| Taxable income rounded down | To the nearest DKK 100 before tax is computed | 2026 | SEL § 22; https://www.retsinformation.dk/eli/lta/2025/279 |
| Local or trade tax on profit | None. 14.24% of the corporate tax collected is passed to the municipalities, but the company pays only the 22% | 2026 | SEL § 23, stk. 1; svmn.dk table |
| Loss carry-forward: full offset up to | DKK 21,830,700 (2010 base DKK 15.9m, indexed) | 2026 | SEL § 12, stk. 2; svmn.dk table |
| Loss carry-forward: offset above that amount | 60% of income above DKK 21,830,700 | 2026 | SEL § 12, stk. 2; svmn.dk table |
| Thin capitalisation (§ 11) | Applies only if controlled debt exceeds DKK 10m; debt to equity 4:1 | 2026 | SEL § 11; https://www.retsinformation.dk/eli/lta/2025/279 |
| Asset test (§ 11 B): net financing expenses not restricted below | DKK 21.3m | 2026 | SEL § 11 B, stk. 1; svmn.dk table |
| Standard rate for the § 11 B asset test | 4.2% | 2026 | SEL § 11 B, stk. 2; svmn.dk table |
| EBITDA rule (§ 11 C): cap on net borrowing costs | 30% of taxable EBITDA; costs up to DKK 22,313,400 always deductible | 2026 | SEL § 11 C, stk. 1-2; svmn.dk table |
| Acontoskat (on-account tax), ordinary | 50% of the average of the last three years' tax, in two equal instalments; amounts in whole DKK 1,000; not charged below DKK 2,000 | 2026 | SEL § 29 A, stk. 2; svmn.dk table |
| Restskattetillæg (surcharge on residual tax) | 6.6% for income year 2025. The 2026 rate is published by 15 December 2026 and is capped at 10% | 2025 (2026 not yet set) | SEL § 29 B, stk. 10 and 12; https://info.skat.dk/data.aspx?oid=2459998 |
| Credit (godtgørelse) on overpaid tax | 2.8% for income year 2025 (cap 5%) | 2025 (2026 not yet set) | SEL § 29 B, stk. 8; https://info.skat.dk/data.aspx?oid=2459998 |
| Surcharge on voluntary acontoskat paid after 20 March and by 20 November | 0.7% for 2025 | 2025 (2026 not yet set) | SEL § 29 B, stk. 9; https://info.skat.dk/data.aspx?oid=2459998 |
| Surcharge on voluntary acontoskat paid after 20 November and by 1 February | 1.3% for 2025 | 2025 (2026 not yet set) | SEL § 29 B, stk. 11; https://info.skat.dk/data.aspx?oid=2459998 |
| Tax depreciation, plant and machinery (driftsmidler) | Up to 25% a year on the declining pool balance | 2026 | Afskrivningsloven § 5; https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/afskrivningsloven |
| Small assets written off at once (småaktiver) | Cost up to DKK 36,000 | 2026 | Afskrivningsloven § 6; svmn.dk afskrivningsloven table |
| Buildings and installations | Up to 3% a year straight line (4% if acquired before 1 January 2023) | 2026 | Afskrivningsloven § 17, stk. 1; svmn.dk afskrivningsloven table |
| Late filing skattetillæg (oplysningsskema) | DKK 400 per day, at most DKK 10,000 | 2026 | Skattekontrolloven § 73, stk. 1, as amended by lov nr. 16 of 14 January 2025; https://www.retsinformation.dk/eli/lta/2025/16 |
| Late payment interest (Opkrævningsloven § 7) | Basis rate 0.1% plus 0.85 percentage points, so 0.95% a month, calculated daily | 2026 | Opkrævningsloven § 7, stk. 1, as amended by lov nr. 1694 of 30 December 2024; https://info.skat.dk/data.aspx?oid=2459995 |
| Pillar Two | In force: 15% global minimum tax for groups with revenue of at least EUR 750m in two of the four prior years (minimumsbeskatningsloven) | 2026 | https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe |

There is no reduced small-company rate and no separate minimum tax outside Pillar Two.

## The taxable base

**Starting point.** Taxable income is computed under the general income tax rules (statsskatteloven, ligningsloven and the special acts) starting from the accounting result. The main adjustments:

- **Add back** accounting depreciation and impairment; then **deduct** tax depreciation under afskrivningsloven (25% declining balance for plant, 3% straight line for most buildings, immediate write-off for small assets).
- **Add back** costs that are not deductible under the general rules, such as corporate tax itself. Interest and surcharges on corporate tax payable under SEL §§ 29 B and 30 are neither taxable nor deductible (§ 29 B, stk. 13; § 30).
- **Interest limitation**, applied in this order:
  1. **Thin capitalisation (SEL § 11).** If controlled debt (from related parties) exceeds DKK 10m and debt to equity exceeds 4:1, interest and losses on the excess controlled debt are not deductible.
  2. **Asset test (SEL § 11 B).** Net financing expenses above DKK 21.3m are deductible only up to the tax value of qualifying assets times the standard rate (4.2% for 2026). Amounts restricted here are lost, except certain net capital losses on receivables, which are carried forward.
  3. **EBITDA rule (SEL § 11 C).** Exceeding borrowing costs may reduce taxable income before interest and depreciation by at most 30%. Costs up to DKK 22,313,400 are always deductible. Restricted costs carry forward without time limit; unused interest capacity carries forward for 5 years (§ 11 C, stk. 4-5). For jointly taxed companies the thresholds apply once for the group.

**Participation exemption on dividends (SEL § 13, stk. 1).**
- Dividends on **subsidiary shares** (datterselskabsaktier: at least 10% of the share capital, Aktieavancebeskatningsloven (ABL) § 4 A) and **group shares** (koncernselskabsaktier: companies that are or can be jointly taxed, ABL § 4 B) are exempt (§ 13, stk. 1, nr. 2). Not exempt to the extent the paying company deducted the distribution.
- Dividends on **tax-free portfolio shares** (unlisted, under 10%, ABL § 4 C) are exempt for distributions from 1 January 2025 (§ 13, stk. 1, nr. 3, inserted by lov nr. 1691 of 30 December 2024). The exemption does not cover a dividend the paying company deducted, or shares covered by ABL §§ 17 or 19 A; those dividends are taxable at 22%. The former rule that taxed 70% of these dividends was repealed by the same law (lov nr. 1691/2024 § 1, nr. 10, which rewrote § 13, stk. 2).
- Dividends on **listed portfolio shares** (under 10%) are fully taxable at 22%.

**Participation exemption on gains (ABL § 8).** Gains and losses on subsidiary shares, group shares and tax-free portfolio shares are ignored. Gains and losses on other shares (taxable portfolio shares, mainly listed holdings under 10%) are taxable (ABL § 9), and for companies they are generally computed on the mark-to-market basis, year-end value less opening value (lagerprincippet, ABL § 23, stk. 5). Unlisted taxable shares may be put on the realisation basis instead (§ 23, stk. 6).

**Losses (SEL § 12).** A tax loss carries forward without time limit. In each later year the loss offsets income in full up to DKK 21,830,700 (2026) and then 60% of the income above that amount. There is **no carry-back**. Remaining losses must be reported digitally each year; late reporting costs a DKK 5,000 surcharge (SEL § 35). Losses can be reduced or lost on a change of ownership or on a debt settlement (SEL §§ 12 A-12 D); check these when control changes.

**Joint taxation (sambeskatning, SEL § 31).** National joint taxation is **mandatory** for all Danish companies and Danish permanent establishments in the same group. A group exists where one company has controlling influence (bestemmende indflydelse) over another, normally more than 50% of the votes (SEL § 31 C). The rules:
- Each company computes its own taxable income; the group income is the sum (§ 31, stk. 2).
- Each profitable company first uses its own pre-joint-taxation losses, then its own losses from within the joint taxation, then current-year losses of other group companies, then other companies' carried-forward joint-taxation losses (§ 31, stk. 2).
- The DKK 21,830,700 / 60% limit applies once for the whole group (§ 31, stk. 3).
- The ultimate Danish parent is the **administration company** (administrationsselskab). It files for the group and pays all of the group's corporate tax and acontoskat (§ 31, stk. 6; § 29 A, stk. 3). If there is no Danish parent, one of the Danish sister companies is designated.
- **International joint taxation** (SEL § 31 A) is optional. It brings in all foreign group companies and permanent establishments and binds the group for 10 years. It is not covered here.

## Deadlines and filing

**The return.** The tax return is the oplysningsskema for selskaber (still often called the selvangivelse). It is filed in TastSelv Selskabsskat (DIAS) through TastSelv Erhverv. The deadline is **6 months after the end of the income year** (Skattekontrolloven § 12, stk. 1). For an income year ending between 1 and 31 March, the deadline is 1 September of the same year (§ 12, stk. 2). A calendar-year company files its 2026 return by **30 June 2027**. A deadline falling on a weekend or holiday moves to 09:00 on the next working day (§ 13). The oplysningsskema for income year 2025 was due 30 June 2026 per skat.dk.

**Acontoskat (on-account tax), SEL § 29 A.** Companies pay their expected tax during the income year.
- Ordinary acontoskat is 50% of the average tax of the last three income years, in two equal instalments. Last payment dates: **20 March** and **20 November** of the income year (§ 29 A, stk. 5).
- A company can pay voluntary extra acontoskat by 20 March, by 20 November, and a third time by **1 February** of the following year (§ 29 A, stk. 6). The amount must be declared in TastSelv Erhverv before it is paid.
- A company in its first two taxable years has no ordinary acontoskat but may pay voluntary amounts on the same dates (§ 29 A, stk. 4).
- In a joint taxation group only the administration company pays acontoskat, for the whole group (§ 29 A, stk. 3).
- A company can ask Skattestyrelsen to lower its ordinary acontoskat if income is expected to fall materially (§ 29 C).

**Final tax.** Skattestyrelsen issues the annual assessment (årsopgørelse) in October of the year after the income year. Residual tax (restskat) plus the restskattetillæg falls due on **1 November** of that year, and payment by **20 November** is on time (SEL § 30, stk. 1 and 4). Overpaid tax is refunded with the godtgørelse within 2 bank days after 20 November (§ 29 B, stk. 5).

**Who must pay on account.** Companies whose first income year began after 28 January 1992 are in the acontoskat scheme. Older companies pay on 1 November of the following year, unless their taxable income two years earlier was DKK 10m or more, or they are an ApS with paid-in capital under DKK 200,000; then they must pay on account too (SEL § 30 A, stk. 1).

## Penalties and interest

- **Late filing.** A company that files the oplysningsskema late pays a **skattetillæg of DKK 400 per day**, up to **DKK 10,000** (Skattekontrolloven § 73, stk. 1, as amended by lov nr. 16 of 14 January 2025, § 2, nr. 1, in force 15 January 2025). The amount is per company, including each late company in a joint taxation group. The consolidated act LBK nr. 12 of 8 January 2024 predates that law and still prints the old DKK 200 and DKK 5,000; do not use those figures. Skattestyrelsen's guidance (Den juridiske vejledning 2026-2, A.C.2.1.4.3.1) confirms the doubled rates from 15 January 2025. From 1 January 2026 the skattetillæg for a company is collected through the tax account (opkrævningsloven § 16, nr. 10, inserted by lov nr. 1783/2025). Skattestyrelsen may also assess the income by estimate (§ 74).
- **Late loss reporting.** DKK 5,000 if remaining losses are not reported on time (SEL § 35).
- **Residual tax surcharge.** Residual tax carries the restskattetillæg (6.6% for income year 2025; the 2026 rate is set by 15 December 2026). The rate is the Nationalbank overdraft rate for non-financial companies (January to September), less 22%, times 480/360, plus 2 percentage points, capped at 10% (SEL § 29 B, stk. 10). Voluntary acontoskat paid by 20 March earns a small credit; later voluntary payments carry a smaller surcharge (0.7% or 1.3% for 2025), so paying early is cheaper.
- **Late payment interest.** Tax paid after the last on-time payment date carries interest under Opkrævningsloven § 7, stk. 1: a monthly basis rate plus a fixed addition, calculated daily and not deductible. The addition is **0.85 percentage points**: lov nr. 1694 of 30 December 2024, § 1, nr. 6, changed "0,7" to "0,85" in § 7, stk. 1. The consolidated act LBK nr. 1040 of 13 September 2024 predates that law and still prints 0.7; do not use it. The basis rate for 2026 is **0.1%** (SKM2025.720.SKTST), so the 2026 rate is 0.95% a month. The Ministry's rate table gives the addition as 0.7% for 2025 and 0.85% for 2026.
- **2026 change for late filers.** Before 2026, a company that filed late paid monthly interest under Opkrævningsloven § 7 on its residual tax from 1 November until the bill was issued (old SEL § 30, stk. 1, 2. pkt.). Lov nr. 1783 of 29 December 2025, § 3, nr. 1, repealed that rule from 1 January 2026: a late filer's residual tax now falls due on the same date as everyone else's (1 November, on time by 20 November), and tax paid after that carries Opkrævningsloven § 7 interest (lov nr. 1783/2025, § 6, stk. 7).

## Cross-border points

**Withholding on outbound dividends.**
- A Danish company withholds **27%** on dividends (Kildeskatteloven (KSL) § 65, stk. 1). Dividends paid to Danish companies, foundations and similar may be paid with **22%** withheld (KSL § 65, stk. 6, 1. pkt.). No dividend tax is withheld on dividends exempt for a Danish company as tax-free portfolio shares (KSL § 65, stk. 6, 2. pkt., as amended by lov nr. 1691/2024, § 6, nr. 3; this replaced the former 15.4% rate).
- A foreign corporate shareholder's Danish tax on the dividend is **22%** (SEL § 2, stk. 1, litra c; § 2, stk. 8). It falls to **15%** for holdings under 10% where the shareholder's state exchanges tax information with Denmark, and to **0%** on tax-free portfolio shares (unlisted, under 10%) for dividends distributed from 1 January 2025 (SEL § 2, stk. 8, 4. pkt., as amended by lov nr. 1691 of 30 December 2024). The 15% and 0% rates require that the beneficial owner does not control the paying company, unless the owner is resident in the EU or a tax treaty reduces the tax (§ 2, stk. 8). It rises to **44%** on subsidiary or group shares held by an owner in a state on the ligningsloven § 5 H list. Any excess withheld above the final rate (or the treaty rate) is reclaimed from Skattestyrelsen.
- **Subsidiary shares:** no Danish tax and no withholding where the parent holds at least 10% and tax must be waived or reduced under the Parent-Subsidiary Directive (2011/96/EU) or a tax treaty with the parent's state (SEL § 2, stk. 1, litra c, 4. pkt.; KSL § 65, stk. 4). The same applies to group shares held by an EU/EEA company where the Directive or treaty would have applied.

**Interest.** Interest on controlled debt paid to a foreign related company is taxed at **22%** by withholding (SEL § 2, stk. 1, litra d; KSL § 65 D). There is no tax where the Interest and Royalties Directive (2003/49/EC) or a treaty reduces or waives it (with a one-year association test), or in several other cases listed in litra d, for example where the recipient's foreign tax on the interest is at least three quarters of the Danish tax. Interest paid to unrelated lenders is not taxed.

**Royalties.** Royalties paid abroad carry **22%** withholding (KSL § 65 C; SEL § 2, stk. 1, litra g). The rate is waived under the Interest and Royalties Directive for associated companies held together for at least one year, and may be reduced by a treaty.

**CFC rules (SEL § 32).** A Danish company that controls a subsidiary (more than 50% of the votes) includes the subsidiary's income in its own taxable income when the subsidiary's CFC income (mainly financial and passive income) is more than one third of its total taxable income. There is no low-tax test. Tax paid by the subsidiary is credited. The rule does not apply where the group has chosen international joint taxation.

**Exit tax (SEL § 5, stk. 7; §§ 26-27).** When a company stops being tax resident in Denmark, or becomes resident elsewhere under a treaty, its assets and liabilities that leave Danish taxation are treated as sold at market value on the date of the move. An internal transfer of assets from Denmark to a foreign head office or branch, after which they leave Danish taxation, is treated as a sale at market value to a group company (SEL § 8, stk. 4, 3. pkt.). For moves to the EU or EEA (with recovery assistance), the company can choose a deferral (henstand), paid in five equal yearly instalments, with interest of 1 percentage point over the Nationalbank discount rate, at least 3% a year (§ 27, stk. 2 and 7). The election is made in the timely return for the year of the move (§ 26, stk. 2). Any balance still deferred falls due if the assets are sold or moved outside the EU/EEA.

**Transfer pricing.** Transactions with related parties must be at arm's length, with reporting and documentation under Skattekontrolloven §§ 37-40. See dk-transfer-pricing.

## Worked examples

**Example 1: a simple trading company, income year 2026.** Nordlys ApS is a calendar-year trading company with no group. Its accounting profit before tax is DKK 2,412,345. The accounts charge DKK 300,000 of depreciation; tax depreciation on the plant pool (opening balance DKK 1,000,000 at 25%) is DKK 250,000. The profit includes a DKK 200,000 dividend from a 40%-owned Danish subsidiary, which is exempt (subsidiary shares, SEL § 13, stk. 1, nr. 2). Taxable income is DKK 2,412,345 + 300,000 − 250,000 − 200,000 = DKK 2,262,345, rounded down to DKK 2,262,300 (SEL § 22). Tax at 22% is DKK 497,706. The company's tax for the last three years was DKK 420,000, DKK 460,000 and DKK 500,000, so ordinary acontoskat is 50% of the DKK 460,000 average = DKK 230,000, paid as DKK 115,000 by 20 March 2026 and DKK 115,000 by 20 November 2026. Residual tax of DKK 267,706 is due by 20 November 2027, plus the restskattetillæg at the 2026 rate, which will be published by 15 December 2026. The oplysningsskema is due 30 June 2027.

```oa-check
name: Example 1, Danish trading ApS, income year 2026
inputs:
  accounting_profit: 2412345
  book_depreciation: 300000
  tax_depreciation: 250000
  exempt_dividend: 200000
  tax_year1: 420000
  tax_year2: 460000
  tax_year3: 500000
steps:
  - taxable_before_rounding: accounting_profit + book_depreciation - tax_depreciation - exempt_dividend
  - taxable_income: floor(taxable_before_rounding / 100) * 100
  - corporate_tax: taxable_income * 0.22
  - ordinary_aconto: (tax_year1 + tax_year2 + tax_year3) / 3 * 0.50
  - instalment: ordinary_aconto / 2
  - residual_tax: corporate_tax - ordinary_aconto
expected:
  taxable_before_rounding: 2262345
  taxable_income: 2262300
  corporate_tax: 497706
  ordinary_aconto: 230000
  instalment: 115000
  residual_tax: 267706
```

**Example 2: losses brought forward and the 60% rule, income year 2026.** Vestkyst A/S has taxable income of DKK 40,000,000 in 2026 before using losses, and DKK 35,000,000 of tax losses brought forward. It is not in a group. Under SEL § 12, stk. 2 the loss first offsets income in full up to DKK 21,830,700. The income above that is DKK 18,169,300, and the remaining loss of DKK 13,169,300 can offset only 60% of it, which is DKK 10,901,580. Total loss used is DKK 32,732,280. Taxable income is DKK 7,267,720, rounded down to DKK 7,267,700, and tax at 22% is DKK 1,598,894. DKK 2,267,720 of loss carries forward to 2027. Without the 60% rule the whole DKK 35,000,000 loss would have been used and the tax would have been DKK 1,100,000, so the rule brings DKK 498,894 of tax forward into 2026.

```oa-check
name: Example 2, loss carry-forward with the DKK 21,830,700 limit and the 60% rule (2026)
inputs:
  income_before_losses: 40000000
  losses_brought_forward: 35000000
  full_offset_limit: 21830700
steps:
  - full_offset: min(losses_brought_forward, min(income_before_losses, full_offset_limit))
  - loss_remaining: losses_brought_forward - full_offset
  - income_above_limit: max(income_before_losses - full_offset_limit, 0)
  - partial_offset: min(loss_remaining, income_above_limit * 0.60)
  - loss_used: full_offset + partial_offset
  - taxable_before_rounding: income_before_losses - loss_used
  - taxable_income: floor(taxable_before_rounding / 100) * 100
  - corporate_tax: taxable_income * 0.22
  - loss_carried_forward: losses_brought_forward - loss_used
  - tax_without_limit: floor((income_before_losses - losses_brought_forward) / 100) * 100 * 0.22
  - tax_brought_forward_by_rule: corporate_tax - tax_without_limit
expected:
  full_offset: 21830700
  partial_offset: 10901580
  loss_used: 32732280
  taxable_income: 7267700
  corporate_tax: 1598894
  loss_carried_forward: 2267720
  tax_without_limit: 1100000
  tax_brought_forward_by_rule: 498894
```

## Ask the client first

1. **Group structure.** Who owns the company and what does it own, with voting percentages? Any Danish group company means mandatory joint taxation and an administration company; foreign group companies matter for CFC, interest withholding and the option of international joint taxation.
2. **Income year and age.** Calendar year or a different financial year (forskudt indkomstår)? When was the company formed? This fixes the filing deadline and whether ordinary acontoskat applies.
3. **Losses and ownership changes.** How much loss is carried forward, from which years, and has there been a change of control or a debt settlement that could cut it?
4. **Shareholdings.** For each share it owns: percentage held, listed or unlisted. This decides whether dividends and gains are exempt or taxable, and on what basis.
5. **Financing.** Related-party debt, total net interest and the tax value of assets. Needed for the §§ 11, 11 B and 11 C tests and for withholding on interest paid abroad.
6. **Sector.** Is it a bank, insurer, investment firm, payment or e-money institution or another financial company listed in SEL § 17 A? Then the effective rate is 26%.

## Sources

| Source | URL | Read on |
|---|---|---|
| Selskabsskatteloven, LBK nr. 279 of 13 March 2025 (in force; the printout lists later amendments by lov nr. 562/2025, 750/2025, 1755/2025, 1783/2025 and 763/2026) | https://www.retsinformation.dk/eli/lta/2025/279 | 2026-10-22 |
| Lov nr. 1783 of 29 December 2025 (amends SEL § 30 and Opkrævningsloven § 16 from 1 January 2026) | https://www.retsinformation.dk/eli/lta/2025/1783 | 2026-10-22 |
| Lov nr. 750 of 20 June 2025 (amends SEL § 2 C and § 31 A) | https://www.retsinformation.dk/eli/lta/2025/750 | 2026-10-22 |
| Lov nr. 763 of 8 September 2026 (amends SEL §§ 24 and 30; no rate changes) | https://www.retsinformation.dk/eli/lta/2026/763 | 2026-10-22 |
| Skattekontrolloven, LBK nr. 12 of 8 January 2024 (§§ 12-14 filing deadline; § 73 late filing, as amended) | https://www.retsinformation.dk/eli/lta/2024/12 | 2026-10-22 |
| Lov nr. 16 of 14 January 2025, § 2, nr. 1 (SKL § 73, stk. 1: DKK 200 to 400 a day, cap DKK 5,000 to 10,000, in force 15 January 2025) | https://www.retsinformation.dk/eli/lta/2025/16 | 2026-10-22 |
| Aktieavancebeskatningsloven, LBK nr. 849 of 21 September 2026 (§§ 4 A-4 C, 8, 9, 23) | https://www.retsinformation.dk/eli/lta/2026/849 | 2026-10-22 |
| Kildeskatteloven, LBK nr. 460 of 3 May 2024, as amended by lov nr. 1691/2024 (§§ 65, 65 C, 65 D) | https://www.retsinformation.dk/eli/lta/2024/460 | 2026-10-22 |
| Opkrævningsloven, LBK nr. 1040 of 13 September 2024 (§ 7 interest, as amended) | https://www.retsinformation.dk/eli/lta/2024/1040 | 2026-10-22 |
| Lov nr. 1694 of 30 December 2024, § 1, nr. 6 (Opkrævningsloven § 7, stk. 1: addition 0.7 to 0.85 percentage points) | https://www.retsinformation.dk/eli/lta/2024/1694 | 2026-10-22 |
| Lov nr. 1691 of 30 December 2024 (SEL § 13, stk. 1, nr. 3 and § 2, stk. 8; KSL § 65, stk. 6; § 12, stk. 2 base DKK 15.9m) | https://www.retsinformation.dk/eli/lta/2024/1691 | 2026-10-22 |
| Skattestyrelsen: basis rate under Opkrævningsloven § 7, stk. 2, for 2026 (SKM2025.720.SKTST) | https://info.skat.dk/data.aspx?oid=2459995 | 2026-10-22 |
| Minimumsbeskatningsloven, LBK nr. 1089 of 2 September 2025 | https://www.retsinformation.dk/eli/lta/2025/1089 | 2026-10-22 |
| Skatte- og Vækstministeriet: rates and thresholds in Selskabsskatteloven, 2026 and 2027 (page dated 2 September 2026) | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/selskabsskatteloven | 2026-10-22 |
| Skatte- og Vækstministeriet: rates in Kildeskatteloven, 2026 and 2027 (page dated 14 September 2026) | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/kildeskatteloven | 2026-10-22 |
| Skatte- og Vækstministeriet: rates in Opkrævningsloven, 2025 and 2026 (page dated 17 March 2026) | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/opkraevningsloven | 2026-10-22 |
| Skatte- og Vækstministeriet: rates in Afskrivningsloven, 2026 and 2027 (page dated 27 August 2026) | https://svmn.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/afskrivningsloven | 2026-10-22 |
| Skattestyrelsen: rates under SEL § 29 B, stk. 8-11 for 2025 (SKM2025.718.SKTST) | https://info.skat.dk/data.aspx?oid=2459998 | 2026-10-22 |
| Skattestyrelsen, Den juridiske vejledning A.C.2.1.4.3.1: skattetillæg under SKL § 73 | https://info.skat.dk/data.aspx?oid=2284578 | 2026-10-22 |
| skat.dk: paying acontoskat and corporate tax | https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/betal-acontoskat-og-selskabsskat | 2026-10-22 |
| skat.dk: tax return for companies and foundations (deadline, late filing, TastSelv) | https://skat.dk/en-us/businesses/companies-and-foundations/companies-and-foundations/tax-return-for-companies-and-foundations | 2026-10-22 |
| skat.dk: oplysningsskema 2025 deadlines | https://skat.dk/erhverv/oplys-aarets-resultat | 2026-10-22 |
| skat.dk: global minimum tax for large groups (GloBE) | https://skat.dk/erhverv/selskaber-fonde-og-foreninger/selskaber-og-fonde/global-minimumsskat-for-store-koncerner-globe | 2026-10-22 |

Not yet confirmed: the 2026 restskattetillæg, godtgørelse and voluntary acontoskat surcharge rates (Skattestyrelsen publishes them by 15 December 2026; the 2025 rates are shown above); the effective dates of the individual Pillar Two charging rules (income inclusion rule, undertaxed profits rule, Danish top-up tax); the R&D enhanced deduction percentages for 2026; the commencement order the Minister issued under lov nr. 1694/2024, § 18, stk. 2, for the 0.85-point addition (the Ministry table and Den juridiske vejledning apply 0.85 for 2026, but the order itself was not located).

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
