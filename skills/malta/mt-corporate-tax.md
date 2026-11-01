---
name: mt-corporate-tax
description: "Malta corporate income tax for basis year 2026 (year of assessment 2027): companies resident in Malta and Malta permanent establishments of foreign companies. Covers the 35% company rate, the full imputation system and the five tax accounts, shareholder refunds (six-sevenths, five-sevenths, two-thirds, full), the elective 15% final tax without imputation (LN 188 of 2025), the taxable base, loss carry-forward, group loss relief (51%) and fiscal units (95%), notional interest deduction, provisional tax, the company return and its deadline, interest and additional tax, outbound withholding, and Pillar Two status. Trigger on: Malta corporate tax, Malta company tax rate, 35% Malta, six-sevenths refund, Malta tax accounts, Malta fiscal unit, Malta group relief, Malta provisional tax company, Malta 15% final tax election. Out of scope: participation exemption detail (mt-holding-company-participation-exemption), company residence, CFC and exit tax (mt-company-residence-and-substance), transfer pricing (malta-transfer-pricing), individuals (malta-income-tax)."
version: 0.2
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta corporate income tax: 35%, imputation, refunds and filing (basis year 2026)

Malta taxes a company on the profits of its basis year in the following year of assessment. A company with a 31 December 2026 year end is taxed for year of assessment 2027. The company pays tax at 35%. When it pays a dividend, the shareholder can claim back most of that tax. The company's profits are sorted into five tax accounts, and the account decides whether a refund is available. Statute quotes are from the consolidated texts on legislation.mt, read on 22 October 2026.

See also: `mt-holding-company-participation-exemption` (participating holdings, the exemption, refund detail, the untaxed account), `mt-company-residence-and-substance` (residence, CFC, interest limitation, exit tax), `malta-transfer-pricing`, `selling-a-company-in-malta`, `mt-capital-gains`.

## Who this applies to

- **Companies resident in Malta.** Under article 2(1) of the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf), a company incorporated in Malta is resident in Malta, and a company incorporated abroad is resident if its management and control is exercised in Malta. The detail, and the domicile and remittance-basis points for a foreign-incorporated company managed in Malta, are in `mt-company-residence-and-substance`. The MTCA [Corporate Tax page](https://mtca.gov.mt/business-tax/corporate/corporate_tax) says Maltese companies are taxed "on their worldwide income and capital gains".
- **Foreign companies with a Malta business.** The same MTCA page says foreign companies "carrying out business activities in Malta are liable to tax on income arising in Malta". A permanent establishment in Malta is taxed at the same 35% on that income.
- **Others charged at the company rate.** Article 56(6) also charges a "body corporate established by law" and an undertaking dealt with as a separate body of persons under article 30(7)(d). Partnerships that elect to be treated as companies under article 27 of the [Income Tax Management Act, Cap. 372](https://legislation.mt/eli/cap/372/eng/pdf) are taxed as companies.
- **Out of scope here.** Individuals and the self-employed (`malta-income-tax`), partnerships that have not elected, trusts and foundations (`mt-foundations-and-trusts`), and sector regimes (insurance, shipping, funds, securitisation vehicles). Article 56(13) is not the company rate: it is the 35% rate for "Contractor" income under article 23 and the 10% withholding on payments to sub-contractors.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Company rate, art. 56(6) Cap. 123 | 35% ("thirty-five cents (0.35) on every euro") | YA 2027 (basis 2026) | https://legislation.mt/eli/cap/123/eng/pdf |
| Elective final tax without imputation, reg. 3(1)(b) S.L. 123.217 | 15%, final, no shareholder refund; stays for at least 5 years of assessment | Income of the fiscal year before YA 2025 and later | https://legislation.mt/eli/sl/123.217/eng/pdf |
| Shareholder refund, Maltese taxed account or foreign income account, art. 48(4A)(a) Cap. 372 | six-sevenths of the tax | Current | https://legislation.mt/eli/cap/372/eng/pdf |
| Refund where profits are passive interest or royalties, or dividends from a holding failing the art. 12(1)(u) conditions | five-sevenths | Current | https://legislation.mt/eli/cap/372/eng/pdf |
| Refund on foreign income account profits, art. 48(4)(a); in practice the route left where the company claimed double tax relief, because proviso (ii) to art. 48(4A)(a) then bars the six-sevenths refund | two-thirds | Current | https://legislation.mt/eli/cap/372/eng/pdf |
| Refund on foreign income account profits from a participating holding, art. 48(4)(b) | all of the Malta tax paid, subject to the anti-abuse conditions in the proviso to art. 48(4)(b) for holdings acquired on or after 1 January 2007 (and, from 1 January 2011, earlier holdings) | Current | https://legislation.mt/eli/cap/372/eng/pdf |
| Tax deducted from an untaxed dividend paid to a "recipient", art. 62(1) Cap. 123 | 15% | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Group loss relief: "fifty-one per cent subsidiary", art. 16 Cap. 123 | more than 50% of shares, votes, profits and assets on a winding up | Current | https://legislation.mt/eli/cap/123/eng/pdf |
| Fiscal unit: "ninety-five per cent (95%) subsidiary", rule 2 S.L. 123.189 | at least 95% of any two of votes, profits, assets on a winding up | From YA 2020 | https://legislation.mt/eli/sl/123.189/eng/pdf |
| Notional interest deduction: reference rate, rule 2 S.L. 123.176 | 20-year Malta Government Stock yield plus 5% | From YA 2018 | https://legislation.mt/eli/sl/123.176/eng/pdf |
| Notional interest deduction cap, rule 4(2)(a) | 90% of chargeable income; excess carried forward | From YA 2018 | https://legislation.mt/eli/sl/123.176/eng/pdf |
| Interest limitation, reg. 4 S.L. 123.187 | 30% of EBITDA, or EUR 3,000,000 in any case; full deduction for a standalone entity (reg. 4(3)(b)) | From 1 Jan 2019 | https://legislation.mt/eli/sl/123.187/eng/pdf |
| Research, development and innovation deduction, art. 14(1)(ha) Cap. 123 (Act III of 2026) | 175% of the expenditure; applies "from such date as may be provided by the Minister" by Gazette notice | Marked "Applicable from the year of assessment 2027" | https://legislation.mt/eli/cap/123/eng/pdf |
| Provisional tax instalments, rule 5 S.L. 372.18 | 20%, 30%, 50% of the benchmark | Each basis period | https://legislation.mt/eli/sl/372.18/eng/pdf |
| Interest on late tax, art. 44(2A) Cap. 372 and S.L. 372.28 | 0.6% per month or part, capped at the tax | Tax payable on or after 31 Aug 2022 | https://legislation.mt/eli/sl/372.28/eng/pdf |
| Pillar Two, S.L. 123.212 | Article 50 deferral elected: IIR and UTPR not applied for up to six fiscal years from 31 Dec 2023; EUR 750m group revenue in at least two of the four preceding fiscal years (reg. 2(2)) | 2024 to about 2029 | https://legislation.mt/eli/sl/123.212/eng/pdf |

No separate local, municipal or trade tax on company profit, and no company minimum tax, appears in the Income Tax Acts read today.

### What changed in the 2025 and 2026 budget laws

1. **The elective 15% final tax** (Final Income Tax Without Imputation Regulations, S.L. 123.217, Legal Notice 188 of 2025, in force 2 September 2025). An "entity" (a company, a body treated as a company, or a trust using article 27D(1)) may pay 15% on its chargeable income "in lieu of the rate determined in article 56(6)". The tax is final: it cannot be credited or refunded to anyone (reg. 3(4)(b)), and the profits go to the final tax account (reg. 3(4)(c)). It cannot be lower than the 35% tax "reduced by the amount of refund claimed or claimable in terms of article 48(4) or (4A)" by all the shareholders on those profits, "and applying the provisions of article 43(6) of the Act, where applicable" (reg. 3(4)(a)). Read the floor with care. Because the elected profits go to the final tax account, no article 48 refund can ever actually be claimed on them, so "claimable" can only sensibly mean the refunds the shareholders would have been entitled to under the normal system; MTCA has not published guidance confirming this. On that reading the floor is 5% for Malta trading profit with six-sevenths shareholders, 10% for passive interest or royalties (five-sevenths), and 35% for profits that would have gone to the immovable property account (no refund), so the election gives nothing on those profits. The regulation does not say whether a shareholder that is not registered for refunds counts as able to claim one. Article 43(6), which deems a Malta-resident individual registered for refunds to receive the company's net profits as a dividend, is pulled into the floor calculation "where applicable"; how it changes the floor is not explained in the regulations. It applies from the year of assessment in which the election is made; the entity cannot notify a return to the normal system before the end of five years from the start of the first year of assessment under the election, and a return to the normal system then holds for at least five consecutive years of assessment (reg. 3(3)). The MTCA notice says the election is "binding on the taxpayer for a period of five (5) consecutive Years of Assessment". Excluded: dividends from another Malta company not paid from its final tax account, and income already taxed at a final rate. The MTCA [notice of 27 March 2026](https://mtca.gov.mt/news-results-page/2026/03/27/election-for-final-income-tax-without-imputation) says the election is made "through the income tax return, by completing the relevant questions therein", by the online filing deadline. Reg. 3(2)(a) allows the election for income of "the fiscal year preceding the year of assessment 2025 and subsequent years", so it is available for basis year 2026 (year of assessment 2027). A further point is unsettled: whether losses brought forward and group relief can reduce income taxed at 15% (article 14(1)(g) bars setting a loss against "income which stands to be allocated to the final tax account", and reg. 3(4)(c) reallocates the elected profits there). Ask MTCA before relying on either reading. When it beats the refund route is worked through in `mt-holding-company-participation-exemption`.
2. **The 175% R&D deduction** (article 14(1)(ha), added by Act III of 2026). The text is in the Act and marked applicable from year of assessment 2027 (basis year 2026). It only starts on a date the Minister sets by Gazette notice, and the activities and conditions are to be set by rules. I did not find that notice or those rules. Until they exist, use the existing article 14(1)(h) deduction for scientific research at 100%.
3. **The refund fractions are unchanged.** The amendment list printed against article 48 of Cap. 372 ends with Act XII of 2023; no 2025 or 2026 Act is listed against it, and the fractions in the consolidated text are six-sevenths, five-sevenths, two-thirds and full refund.
4. **Pillar Two.** Legal Notice 48 of 2026 amended regulation 11 of S.L. 123.212 (the filing entity rules). The deferral itself is unchanged.
5. **New article 22B of Cap. 123** (Act IX of 2025) lets the Minister make regulations for an elective tax "higher than that established" on the profits of Malta entities. No regulations under it were found; it does not change the 35% rate.

## The taxable base

**From accounting profit to chargeable income.** The MTCA [Income Tax page](https://mtca.gov.mt/business-tax/corporate/Income_Tax) says chargeable income "is based on the accounting profits before tax for the basis period as adjusted for tax purposes". In practice:

- Add back accounting depreciation. Deduct tax wear and tear allowances on plant and machinery (art. 14(1)(f)) and industrial buildings (S.L. 123.173).
- Deduct expenses incurred in producing the income (art. 14(1)), including rent, repairs, promotion and market research (art. 14(1)(l)), and capital spending on intellectual property spread over at least three years, or deducted in one year subject to prescribed conditions (art. 14(1)(m)).
- Bad debts are deductible only when "proved to the satisfaction of the Commissioner to have become bad" in the year (art. 14(1)(d)). A general provision is added back. Recoveries are taxed when received.
- Scientific research expenditure is deductible under art. 14(1)(h); capital research spending is spread over six years.
- Leave out exempt income: participation exemption dividends and gains (art. 12(1)(u), see `mt-holding-company-participation-exemption`).
- Transfer pricing adjustments: `malta-transfer-pricing`.

**Notional interest deduction.** Under the [Notional Interest Deduction Rules, S.L. 123.176](https://legislation.mt/eli/sl/123.176/eng/pdf) (Legal Notice 37 of 2018, in force from YA 2018), a Malta-resident company or partnership, or a Malta permanent establishment, may deduct deemed interest on its risk capital (share capital, share premium, positive retained earnings, interest-free loans and other equity). The rate is the 20-year Malta Government Stock yield plus 5%. The deduction is optional, needs approval of all shareholders, and only reduces profits going to the foreign income account or Maltese taxed account. It is capped at 90% of chargeable income, with the excess carried forward. Risk capital invested where income would be exempt is excluded. Each shareholder is deemed to receive interest income equal to its share of the deduction (rule 5).

**Interest limitation.** Exceeding borrowing costs are deductible up to 30% of tax EBITDA, or up to EUR 3,000,000 in any case (reg. 4, [S.L. 123.187](https://legislation.mt/eli/sl/123.187/eng/pdf)). Detail in `mt-company-residence-and-substance`.

**The five tax accounts (art. 2(1) Cap. 123).** Every Malta company sorts its distributable profits into:

| Account | What goes in, in plain terms | Shareholder refund on distribution |
|---|---|---|
| Final tax account | Profits taxed at a final rate (for example the 15% election, property transfer final tax). Filled first. | None. No further tax on the dividend (art. 68(1)(c)) |
| Immovable property account | Profits from Malta immovable property that are not in the final tax account | None (art. 48(4A) covers only the Maltese taxed account and foreign income account) |
| Foreign income account | Taxable foreign income: participating holding income or gains declared and taxed, other foreign investment income, dividends from another company's foreign income account | six-sevenths; five-sevenths for passive interest or royalties; two-thirds if double tax relief was claimed; all of it for participating holdings |
| Maltese taxed account | Other taxed profits, for example Malta trading profit | six-sevenths; five-sevenths for passive interest or royalties |
| Untaxed account | What is left: profits that bore no Malta tax | No refund. 15% deducted when paid to a "recipient" (art. 62) |

Tax on profits allocated to the foreign income account is not payable before the earlier of the dividend date or 18 months after the end of the accounting period (art. 42(9) Cap. 372).

**How the refund works.** The company pays 35%. It pays a dividend and issues a dividend certificate. A shareholder registered for refunds claims within four years (art. 48(5)). The refund is capped at the tax the company actually paid. So on Malta trading profit taken out fully as a dividend, Malta tax ends at 35% x (1 - 6/7) = 5% of the profit. Where a company pays a dividend from foreign income account or Maltese taxed account profits, any tax not yet paid on those profits is due as Advance Company Income Tax within 60 days of the end of the month after the dividend (art. 42B Cap. 372). Malta-resident individual shareholders need care. A resident individual registered for refunds (or beneficially entitled to the profits of a registered person) is deemed under article 43(6) of Cap. 123 to receive the company's net profits as a dividend on the first day of the next accounting period, unless they were distributed to him in the period they were earned. Separately, article 12(1)(c)(iii) of Cap. 123 exempts taxed-account dividends to higher-income individuals, and such exempt dividends fall under the refund bar in the proviso to article 48(1) of Cap. 372 (see `mt-holding-company-participation-exemption`).

**Losses.** A trading loss of the basis year is set against other income and capital gains of that year. What is left is "carried forward and set off against what would otherwise have been the total income for subsequent years in succession" (art. 14(1)(g)). There is no time limit and no carry-back. A loss cannot be set against income going to the final tax account, and a loss from activities whose profit would go to that account is not usable. A foreign loss that would not have been taxable if profitable and kept abroad is not deductible. Loss transfer on a merger or division needs the Commissioner's permission.

**Group loss relief (arts. 16 to 22 Cap. 123).** Two companies resident in Malta, and not resident anywhere else, are a group if one is the 51% subsidiary of the other or both are 51% subsidiaries of a third Malta company. 51% means more than 50% of ordinary shares and votes, profits available for distribution, and assets on a winding up. The surrendering company's current-year loss may be set against the claimant's total income for the same year if:

- both were in the group throughout the year;
- in the loss year both had accounting periods starting and ending on the same dates (newly incorporated or wound-up companies have a relief in art. 18(2));
- the loss is matched by account: a loss that would have gone to the immovable property account or Maltese taxed account is set against the claimant's income for those accounts; a foreign income account loss only against foreign income account income (art. 18(1)(c) and (d));
- the claim includes the surrendering company's consent and is made by the later of the claimant's tax return date and 12 months after the end of the accounting period (art. 21).

A surrendered loss that exceeds the claimant's income is carried forward by the claimant as its own (art. 18(1)(b)). Only losses of the current year can be surrendered, not losses brought forward.

**Fiscal units (S.L. 123.189, Legal Notice 110 of 2019).** A parent company and its 95% subsidiaries with the same accounting dates may elect to form a fiscal unit from YA 2020. The parent ("principal taxpayer") must be a company registered in Malta. It files one return for the unit, intra-unit transactions are ignored, and the subsidiaries' tax duties are suspended. Rule 6(2) reads: where article 48(4) or (4A) "would have applied to a shareholder of a company that forms part of a fiscal unit upon a receipt of a dividend from such company and such shareholder is specifically empowered to consolidate its results pursuant to Maltese law", the unit's chargeable income is "fully subject to tax" at 35% less the rate found by dividing "the total amounts claimable by all members of the fiscal unit and, or persons entitled to receive distributions from the principal taxpayer" under article 48(4)/(4A) by the unit's chargeable income. Rule 6(3) then switches off the article 48 refund "in respect of profits relative to which sub-rule (2) are claimed". The refund is in effect given at company level, without a dividend; on Malta trading profit with six-sevenths shareholders the unit's rate works out at 5%. The rule does not define "specifically empowered to consolidate its results"; check MTCA's fiscal unit guidelines before computing the rate. The distributable profits of transparent subsidiaries go to the untaxed account (rule 8(1)). Anti-abuse (rule 13): if the tax payable by the principal taxpayer after refunds is lower than 95% of what all the companies would have paid separately after refunds, the shareholders of the principal taxpayer are deemed to receive an advance equal to the shortfall divided by 35%; it is treated as an untaxed dividend on the tax return date, with tax deducted at 35% where paid to a "recipient". The election takes effect from the year of assessment in which it is made, or the next if made after the subsidiary's return date. A non-100% subsidiary needs minority shareholder approval.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Basis period | The accounting year ending in the year before the year of assessment; a company may get permission for a non-December year end (art. 11(2) Cap. 123) | Cap. 123 |
| Company return and self-assessment | The later of the last day of the 9th month after year end and 31 March of the year of assessment (rule 2(c)(i) S.L. 372.16). 31 December 2026 year end: 30 September 2027 | https://legislation.mt/eli/sl/372.16/eng/pdf |
| Tax payment ("tax settlement date") | Same day as the return date (rule 5(b) S.L. 372.16) | same |
| Provisional tax | 30 April, 31 August and 21 December falling in the basis period: at least 20%, then a further 30%, then a further 50% of the benchmark (rules 4 and 5) | https://legislation.mt/eli/sl/372.18/eng/pdf |
| Advance Company Income Tax | Within 60 days of the end of the month after a dividend from the foreign income account or Maltese taxed account (art. 42B) | Cap. 372 |
| Group relief claim | Later of the tax return date and 12 months after the accounting period end (art. 21) | Cap. 123 |
| Refund claim by shareholder | Within four years of eligibility (art. 48(5)) | Cap. 372 |

- **Return.** Filed as the MTCA e-Return, "an application in the form of a spreadsheet through which the Tax Practitioner submits the Income Tax Return and Financial Statements" ([MTCA IRD Services Online](https://mtca.gov.mt/business-tax/corporate/irdservicesonline)). Only a registered tax practitioner can file a company return, after the company authorises them on form MTCA02 ([MTCA Income Tax page](https://mtca.gov.mt/business-tax/corporate/Income_Tax)). A Malta company files its financial statements with the return (art. 10(4) Cap. 372). The TIFD spreadsheet is on the MTCA [corporate downloads](https://mtca.gov.mt/business-tax/corporate/downloads) page.
- **E-filing extensions.** MTCA usually extends the online filing date, but "These extensions apply only to the electronic filing of tax returns, and not to tax payments" ([notice of 13 January 2026](https://mtca.gov.mt/home/2026/01/13/electronic-filing-extension-of-corporate-income-tax-returns-for-2026)). For 31 December 2025 year ends the online date was 27 November 2026 against a statutory date of 30 September 2026. The table for 2026 year ends had not been published when this was read.
- **Provisional tax benchmark.** The tax shown in the last self-assessment due before the calendar year in which the first instalment falls, with provisional tax added back (rules 2 and 6 S.L. 372.18). A company in its first year of assessment has a nil benchmark; in its second, the first year's computation is used (rule 8). A company expecting lower tax may reduce instalments by filing the PT reduction form (rule 10).

## Penalties and interest

| Default | Charge | Source |
|---|---|---|
| Late company return (person other than an individual), Table B | EUR 50 within 6 months; EUR 200 (6 to 12 months); EUR 400 (12 to 18); EUR 600 (18 to 24); EUR 800 (24 to 36); EUR 1,000 (36 to 48); EUR 1,200 (48 to 60); EUR 1,500 after 60 months | Schedule, item 3, Cap. 123 |
| Omission from a return | 1.5% per month of the "endangered tax"; fully remitted if corrected by a further return within 12 months of the return date before an enquiry notice, otherwise 0.1% per month if corrected before the notice; 0.75% per month if corrected after the enquiry notice but before an assessment; capped at sixty times the monthly rate | Schedule, items 5 to 7, Cap. 123 |
| Late payment of tax | Interest of 0.6% per month or part, from the tax settlement date, capped at the tax | Art. 44(2A) Cap. 372; rule 2 S.L. 372.28 |
| Late provisional tax | Additional tax of 0.6% per month or part (periods from 1 June 2022); reduced by 90% on the part above the tax in the self-assessment; stops after the tax settlement date | Rule 14 S.L. 372.18 |
| Wrong refund claim | Penalty equal to the refund claimed | Art. 48(10) Cap. 372 |

The Commissioner may remit late-return additional tax for "reasonable excuse"; lack of funds or reliance on an adviser is not one (Schedule item 4). Interest may be remitted under the [Remission of Interest Rules, S.L. 372.26](https://legislation.mt/eli/sl/372.26/eng/pdf). The printed PT reduction form still says "1%"; rule 14 as amended sets 0.6%.

## Cross-border points

- **Dividends paid abroad.** Malta does not withhold tax on dividends paid to non-residents. Tax is deducted only from untaxed account dividends paid to a "recipient" (art. 61 and 62 Cap. 123), and a non-resident is a recipient only if owned and controlled by, or acting for, an individual ordinarily resident and domiciled in Malta. A non-recipient is not charged on an untaxed dividend (art. 66). Dividends from taxed accounts bear no further tax for non-residents (art. 68(1)). A non-resident shareholder registered for refunds can claim the article 48 refunds.
- **Interest and royalties paid abroad.** Article 12(1)(c)(i) exempts interest, discount, premium and royalties "accruing to or derived by any person not resident in Malta", unless they are effectively connected with a Malta permanent establishment of that person. The proviso requires the beneficial owner to be non-resident and not owned and controlled by, or acting for, individuals ordinarily resident and domiciled in Malta. So there is no domestic withholding on these payments in the ordinary case.
- **EU directives.** The participation exemption carries the Parent-Subsidiary Directive anti-hybrid rule: profits that benefit from the directive's withholding exemption are exempt only to the extent the subsidiary cannot deduct them (art. 12(1)(u) Cap. 123). The ATAD rules (interest limitation, exit tax, CFC, hybrids) are in S.L. 123.187.
- **CFC rules.** Regulation 7 of [S.L. 123.187](https://legislation.mt/eli/sl/123.187/eng/pdf) can attribute undistributed income of a low-taxed controlled foreign company to the Malta parent. Thresholds and carve-outs are in `mt-company-residence-and-substance`.
- **Exit tax.** Regulation 5 of S.L. 123.187 taxes the market-value gain when a company moves assets or its tax residence out of Malta, from 1 January 2020. See `mt-company-residence-and-substance`.
- **Pillar Two.** Malta transposed the EU directive in S.L. 123.212 but elected the Article 50 deferral. For up to six consecutive fiscal years from 31 December 2023 the regulations apply only Chapters I, VIII, IX and X of the directive (reg. 2(1)), the Malta UTPR percentage is deemed zero, and a Malta parent nominates a filing entity in another state (reg. 11). Groups with EUR 750 million revenue still have information duties. No Malta top-up tax is charged during the deferral on that wording, and Malta has no domestic top-up tax. The deferral does not stop other countries' IIR or UTPR from picking up top-up tax on a low-taxed Malta entity; the effective rate after shareholder refunds (often about 5%) is what those rules look at.

## Worked examples

All companies and figures are invented. Rates are from the tables above.

### Example 1: a Malta trading company, profits paid out to a foreign parent

Harbour Trading Ltd is incorporated in Malta, calendar year end, basis year 2026 (YA 2027). Its accounts show profit before tax of EUR 250,000. It booked depreciation of EUR 30,000; tax wear and tear allowances are EUR 24,000. It also booked a general provision for doubtful debts of EUR 5,000, which is not a deduction under art. 14(1)(d). All profit is Malta trading profit, so it goes to the Maltese taxed account.

Chargeable income is 250,000 + 30,000 - 24,000 + 5,000 = EUR 261,000. Tax at 35% is EUR 91,350.

Its YA 2025 self-assessment (basis year 2024, the last return due before 1 January 2026) showed tax of EUR 80,000, so provisional tax in 2026 is EUR 16,000 on 30 April, EUR 24,000 on 31 August and EUR 40,000 on 21 December. The balance of EUR 11,350 is due with the return on 30 September 2027.

Harbour pays all its 2026 profit as a dividend to its sole shareholder, a German company not owned or controlled by anyone ordinarily resident and domiciled in Malta, and registered for refunds. The shareholder claims six-sevenths of the tax: EUR 78,300. Malta tax left is EUR 13,050, which is 5% of chargeable income. No tax is withheld on the dividend.

```oa-check
name: Malta trading company, basis year 2026, six-sevenths refund
inputs:
  profit_before_tax: 250000
  depreciation_booked: 30000
  wear_and_tear: 24000
  general_provision: 5000
  pt_benchmark: 80000
steps:
  - chargeable: profit_before_tax + depreciation_booked - wear_and_tear + general_provision
  - tax: chargeable * 0.35
  - pt_april: pt_benchmark * 0.20
  - pt_august: pt_benchmark * 0.30
  - pt_december: pt_benchmark * 0.50
  - balance_due: tax - pt_april - pt_august - pt_december
  - refund_fraction: 6 / 7
  - refund: tax * refund_fraction
  - malta_tax_after_refund: tax - refund
  - effective_rate_pct: malta_tax_after_refund / chargeable * 100
expected:
  chargeable: 261000
  tax: 91350
  pt_april: 16000
  pt_august: 24000
  pt_december: 40000
  balance_due: 11350
  refund: 78300
  malta_tax_after_refund: 13050
  effective_rate_pct: 5.00
```

### Example 2: losses brought forward and group relief, and the 15% election compared

Gozo Logistics Ltd has chargeable income of EUR 300,000 for basis year 2026, all for its Maltese taxed account, before losses. It has its own unrelieved trading losses brought forward of EUR 80,000. Its sister company, Gozo Fleet Ltd, made a 2026 trading loss of EUR 60,000 that would have gone to its Maltese taxed account. A Malta parent owns 100% of both; both are resident only in Malta, were in the group all year, and have 31 December year ends. Fleet consents and Gozo Logistics claims the whole loss by 30 September 2027.

Chargeable income is 300,000 - 80,000 - 60,000 = EUR 160,000. Tax at 35% is EUR 56,000. If the profits are paid out and six-sevenths is claimed, Malta tax left is EUR 8,000.

Compare the 15% final tax election for the same year: 15% x 160,000 = EUR 24,000, final and not refundable. The floor in reg. 3(4)(a) is the 35% tax less refunds claimable (EUR 8,000), so the 15% tax stands at EUR 24,000. On profits paid out to a shareholder that is registered for and will claim the six-sevenths refund, the election costs EUR 16,000 more. The election wins where the refund route does not deliver 5% in practice: profits kept in the company (no refund is paid until a dividend is paid, so retained profits carry 35%), or shareholders who would not claim refunds, such as many Malta-resident individual owners, for whom the 35% imputation tax is otherwise the final cost and an FTA dividend bears no further tax (art. 68(1)(c)). This example also assumes losses and group relief reduce the income taxed at 15%; that is not settled (see above). Run the floor on the client's own shareholders before advising (see `mt-holding-company-participation-exemption`).

```oa-check
name: Losses brought forward plus group relief, and the 15% election compared
inputs:
  chargeable_before_losses: 300000
  own_losses_bf: 80000
  group_loss_surrendered: 60000
steps:
  - own_used: min(own_losses_bf, chargeable_before_losses)
  - group_used: min(group_loss_surrendered, chargeable_before_losses - own_used)
  - chargeable: chargeable_before_losses - own_used - group_used
  - losses_carried_forward: own_losses_bf - own_used
  - tax: chargeable * 0.35
  - refund_fraction: 6 / 7
  - refund_route_net: tax - tax * refund_fraction
  - elective_tax: chargeable * 0.15
  - elective_payable: max(elective_tax, refund_route_net)
  - election_extra_cost: elective_payable - refund_route_net
expected:
  chargeable: 160000
  losses_carried_forward: 0
  tax: 56000
  refund_route_net: 8000
  elective_payable: 24000
  election_extra_cost: 16000
```

## Ask the client first

1. Who are the shareholders, where are they resident and domiciled, are any companies or trusts, and are they registered for refunds? This decides refunds, "recipient" status and withholding on untaxed dividends.
2. What are the sources of income: Malta trading, Malta property, foreign income, passive interest or royalties, participating holdings? This decides the tax account and the refund fraction.
3. Will the profits be paid out soon or kept? This decides between the refund route and the 15% final tax election, which locks in for five years.
4. Is the company in a group: who owns at least 51% or 95%, which companies are resident only in Malta, and do accounting dates match? This decides group relief and a fiscal unit.
5. What losses are brought forward, in which account would they have fallen, and what did the last self-assessment show (the provisional tax benchmark)?
6. Is the company part of a group with consolidated revenue of EUR 750 million or more? This brings in the Pillar Two filing duties.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123 (arts. 2, 11, 12, 14, 16 to 22B, 43(6), 56, 61 to 68, Schedule) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-10-22 |
| Income Tax Management Act, Cap. 372 (arts. 10, 42, 42B, 44, 48) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-10-22 |
| Final Income Tax Without Imputation Regulations, S.L. 123.217 (LN 188 of 2025) | https://legislation.mt/eli/sl/123.217/eng/pdf | 2026-10-22 |
| Consolidated Group (Income Tax) Rules, S.L. 123.189 (LN 110 of 2019) | https://legislation.mt/eli/sl/123.189/eng/pdf | 2026-10-22 |
| Notional Interest Deduction Rules, S.L. 123.176 (LN 37 of 2018) | https://legislation.mt/eli/sl/123.176/eng/pdf | 2026-10-22 |
| EU Anti-Tax Avoidance Directives Implementation Regulations, S.L. 123.187 | https://legislation.mt/eli/sl/123.187/eng/pdf | 2026-10-22 |
| EU Global Minimum Level of Taxation Regulations, S.L. 123.212 | https://legislation.mt/eli/sl/123.212/eng/pdf | 2026-10-22 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16 | https://legislation.mt/eli/sl/372.16/eng/pdf | 2026-10-22 |
| Payment of Provisional Tax (P.T.) Rules, S.L. 372.18 | https://legislation.mt/eli/sl/372.18/eng/pdf | 2026-10-22 |
| Income Tax (Rate of Interest) Rules, S.L. 372.28 | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-10-22 |
| Remission of Interest Rules, S.L. 372.26 (title only) | https://legislation.mt/eli/sl/372.26/eng/pdf | 2026-10-22 |
| MTCA: Corporate Tax | https://mtca.gov.mt/business-tax/corporate/corporate_tax | 2026-10-22 |
| MTCA: Income Tax (company return cycle) | https://mtca.gov.mt/business-tax/corporate/Income_Tax | 2026-10-22 |
| MTCA: Electronic filing extension of corporate income tax returns for 2026 | https://mtca.gov.mt/home/2026/01/13/electronic-filing-extension-of-corporate-income-tax-returns-for-2026 | 2026-10-22 |
| MTCA: Election for Final Income Tax Without Imputation (27 March 2026) | https://mtca.gov.mt/news-results-page/2026/03/27/election-for-final-income-tax-without-imputation | 2026-10-22 |
| MTCA: IRD Services Online for tax practitioners | https://mtca.gov.mt/business-tax/corporate/irdservicesonline | 2026-10-22 |
| MTCA: Corporate downloads | https://mtca.gov.mt/business-tax/corporate/downloads | 2026-10-22 |

MTCA pages sit behind a bot check; they were read in a browser.

Not yet confirmed: whether the Gazette notice and rules that start the 175% deduction in art. 14(1)(ha) have been issued; the names and numbers of the return attachments (TRA forms) in the YA 2027 e-Return; MTCA's online filing extension dates for 2026 year ends; whether losses brought forward and group relief reduce income taxed under the 15% election; how the reg. 3(4)(a) floor treats shareholders not registered for refunds and Malta-resident individuals under article 43(6); the meaning of "specifically empowered to consolidate its results" in rule 6(2) S.L. 123.189; any regulations under article 22B Cap. 123; wear and tear rates under the Deductions (Wear and Tear) Rules (not read for this skill).

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
