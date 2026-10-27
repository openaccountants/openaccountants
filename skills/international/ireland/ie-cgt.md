---
name: ie-cgt
description: "Irish Capital Gains Tax (CGT) for individuals, tax year 2026. Covers the standard rate of 33% for disposals up to 6 October 2026 and 31% from 7 October 2026 (Financial Resolution No. 3 and section 36 of the Finance (No. 2) Bill 2026, provisional until enacted), development land at 33%, the EUR 1,270 annual exemption, the computation and allowable costs, share identification, losses, Principal Private Residence relief, Revised Entrepreneur Relief at 10% (lifetime limit EUR 1,500,000 for gains from 1 January 2026), Retirement Relief, the site to a child relief, indexation, the CG50A clearance and 15% withholding, payment by 15 December or 31 January, returns on Form 11, Form 12 or CG1 by 31 October, surcharges and interest. Triggers: Ireland CGT, 31% capital gains, CG50, Entrepreneur Relief, Form CG1. Out of scope: companies (ie-corporation-tax), gifts and inheritances on the recipient side (ie-cat), remittance basis (ie-non-dom), treaty credits (ie-foreign-tax-and-withholding)."
version: 2.2
jurisdiction: IE
category: international
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland Capital Gains Tax (CGT) for individuals, 2026

Built by Michael Cutajar and the OpenAccountants team. Checked against the law: not signed off by an accountant. This skill sets out how an individual computes, pays and reports Irish CGT on a disposal in tax year 2026 (the calendar year). The law is Part 19 and related parts of the Taxes Consolidation Act 1997 (TCA), as amended by later Finance Acts, including Finance Act 2025. The standard rate fell from 33% to 31% for disposals on or after 7 October 2026. That cut is provisional until the Finance (No. 2) Bill 2026 becomes law (see "The 31% rate" below).

## Who this applies to

- **Irish resident individuals** are generally chargeable on gains on the disposal of assets ([Tax and Duty Manual Part 02-01-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf)). CGT is paid by the person making the disposal.
- **Non-resident individuals** pay CGT only on gains on: land, buildings and minerals in Ireland; exploration or exploitation rights in the Irish continental shelf; unquoted shares deriving the greater part of their value from those assets; and assets used for a trade carried on in Ireland ([CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx)).
- **Companies** normally include their gains in Corporation Tax; a company's gain on development land is charged to CGT instead. Out of scope here: use `ie-corporation-tax`.
- **What is a disposal.** A sale, gift, exchange, or receipt of compensation or insurance money for an asset. Under a written contract the time of disposal is usually the contract date. The date fixes the tax year, the payment period and the rate ([pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
- **Chargeable assets** include land (including development land), buildings, shares in Irish or foreign companies, goodwill, patents and copyright, foreign currency, assets of a trade, foreign life policies and offshore funds, and capital payments in certain cases. Antiques, paintings and jewellery can be chargeable. Revenue lists crypto-assets among the assets on which CGT arises. A jointly owned asset is taxed on the owner's share of the gain ([what do you pay CGT on](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx), [TDM 02-01-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf)).
- **Exempt:** betting, lottery wins, prize bonds, sweepstakes, National Instalments Savings Scheme bonuses, government stocks, certain life assurance policies, animals, private motor cars, and moveable property such as furniture where the gain does not exceed EUR 2,540 ([what is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx)). Section 603 TCA as enacted gives no chargeable gain on tangible movable wasting assets, except those used solely in a trade or profession on which capital allowances were or could have been claimed ([s.603 as enacted](https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html)). Revenue states the chattels test as the gain; section 602 as enacted states it as the consideration and excludes wasting assets ([s.602 as enacted](https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html)). Where the sale price is above EUR 2,540 but the gain is below it, refer.
- **Spouses and civil partners.** A transfer between them is usually exempt, including divorced spouses and separated or former civil partners. Not exempt: trading stock of the transferor's business; a transfer to a spouse or civil partner who is non-resident and not liable to CGT; a transfer to a former spouse or civil partner not covered by a court order ([what is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx)).
- **Death.** In general there is no CGT on an asset passing on death. The heir owns it from the date of death at market value at that date. A personal representative who sells during administration may owe CGT ([CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx)). The recipient's tax on the gift or inheritance is CAT: see `ie-cat`.
- **Refer, out of scope:** trusts and estates (Form 1); partnerships; development land; foreign life policies, foreign investment products and venture capital funds; company reorganisations, mergers and share-for-share exchanges; resident individuals not domiciled in Ireland with foreign gains (`ie-non-dom`); property bought between 7 December 2011 and 31 December 2014 (Revenue lists a separate relief), Farm Restructuring Relief, and compensation or insurance deferral claims ([CGT reliefs](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/index.aspx)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate, most gains, disposals 6 December 2012 to 6 October 2026 | 33% | 2026 | https://www.irishstatutebook.ie/eli/2013/act/8/section/43/enacted/en/html |
| Standard rate, most gains, disposals on or after 7 October 2026 (provisional) | 31% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx ; https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf |
| Development land (s.649A, not cut) | 33% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx |
| Foreign life policies and foreign investment products (out of scope) | 40% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx |
| Venture capital funds: individuals and partnerships / companies (out of scope) | 15% / 12.5% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx |
| Historic standard rates: to 14 Oct 2008; 15 Oct 2008 to 7 Apr 2009; 8 Apr 2009 to 6 Dec 2011; 7 Dec 2011 to 5 Dec 2012 | 20%; 22%; 25%; 30% | historic | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx |
| Personal exemption, per individual per year, after losses, not transferable | EUR 1,270 | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx |
| Moveable property exempt where the gain does not exceed | EUR 2,540 | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx |
| Revised Entrepreneur Relief rate (s.597AA); 20% for 2016 disposals | 10% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx |
| Entrepreneur Relief lifetime limit, gains 1 Jan 2016 to 31 Dec 2025 | EUR 1,000,000 | to 2025 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx |
| Entrepreneur Relief lifetime limit, gains on or after 1 January 2026 | EUR 1,500,000 | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx |
| Entrepreneur Relief: minimum ordinary shareholding for 3 continuous years; minimum working time; group subsidiaries | 5%; 50%; 51% | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx |
| Retirement Relief, transfer to a child from 1 Jan 2025: aged 55 to 69 / 70 or older | EUR 10 million / EUR 3 million | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx |
| Retirement Relief, disposal outside the family from 1 Jan 2025, lifetime: aged 55 to 69 / 70 or older | EUR 750,000 / EUR 500,000 | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx |
| Site from parent to child (s.603A): maximum value; maximum area | EUR 500,000; one acre | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx |
| PPR: land around the home covered, excluding the site of the house | one acre (0.405 ha) | 2026 | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx |
| Section 980 (CG50A) threshold: specified asset / house or apartment | EUR 500,000 / EUR 1,000,000 | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf |
| Purchaser withholding without a CG50A | 15% of the consideration | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf |
| Late filing surcharge (s.1084, "tax" includes CGT) | 5%, max EUR 12,695, within 2 months; 10%, max EUR 63,485, after | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Interest on late CGT (s.1080) | 0.0219% a day | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |

### The 31% rate from 7 October 2026: provisional

- **What changed.** Financial Resolution No. 3, agreed by Dáil Éireann on 6 October 2026, substitutes "31 per cent" for "33 per cent" in section 28(3) TCA for disposals made on or after 7 October 2026 ([Dáil record, 6 October 2026](https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml)). Section 36 of the Finance (No. 2) Bill 2026 (Bill 98 of 2026) makes the same change: "(2) Subsection (1) applies to disposals of assets made on or after 7 October 2026" ([Bill 98, as initiated](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf)). Revenue's pages already give 31% ([how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx)).
- **Status on 26 October 2026.** The Oireachtas page shows the Bill has completed Dáil First Stage; it is not law ([Bill 98 of 2026](https://www.oireachtas.ie/en/bills/bill/2026/98/)).
- **Why it applies now.** The resolution has statutory effect under the Provisional Collection of Taxes Act 1927, which covers CGT ([Finance Act 2010 s.160](https://www.irishstatutebook.ie/2010/en/act/pub/0005/sec0160.html)).
- **When it would lapse.** On the first of: the Bill not read a second time within 84 days after the resolution (or within five sitting days after a recess covering days 82 to 84); the Dáil rejecting the provision; an Act with the provision coming into operation; or four months from 7 October 2026 ([Finance Act 1974 s.85](https://www.irishstatutebook.ie/1974/en/act/pub/0027/sec0085.html), [Appropriation Act 1991 s.2](https://www.irishstatutebook.ie/1991/en/act/pub/0032/print.html)). A dissolution period is left out of the counts ([Finance Act 1992 s.250](https://www.irishstatutebook.ie/1992/en/act/pub/0009/sec0250.html)).
- **What to do.** Compute disposals on or after 7 October 2026 at 31%. If the resolution lapses, they go back to 33%. Before 7 February 2027, check that the Finance (No. 2) Act 2026 is in force and still says 31%.
- **What it does not change.** Development land stays at 33% (s.649A(1)(b), set by Finance Act 2013 s.43; Bill 98 does not amend s.649A). The 10%, 40%, 15% and 12.5% rates, the EUR 1,270 exemption and the payment dates are unchanged.

## The taxable base

**Annual computation** ([how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx)):

1. For each disposal: proceeds (or market value) less the purchase price (or market value at acquisition) less allowable expenses (s.552). Allowable: the price, enhancement expenditure that adds value, and costs such as solicitor's and auctioneer's fees on acquisition and disposal. Routine repairs are not enhancement; treat unclear spending as a repair.
2. Apply reliefs that remove or reduce the gain (PPR, Retirement Relief, site to a child).
3. Add the year's gains and deduct allowable losses: current-year losses first, then losses brought forward.
4. Deduct the EUR 1,270 exemption. It is per individual, resident or not, cannot pass to a spouse or civil partner, and is not available to a company or trust. Where gains are taxed at two or more rates, it goes against the gains at the highest rate first (s.601(3), [s.601](https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html)). No exemption is given where Retirement Relief under s.598 or s.599 is allowed (s.601(5); [TDM 19-07-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-07-01.pdf)).
5. Apply the rate for each disposal's date. If a year has disposals on both sides of 7 October 2026, keep two groups; the exemption comes off the 33% group first.

**Market value replaces the price** where the asset was a gift to someone other than a spouse or civil partner, sold below value to help the buyer, inherited, or bought before 6 April 1974 ([how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx)). If no valuation exists, stop.

**Indexation (s.556).** Only costs paid up to 31 December 2002 are indexed, each by the multiplier for the year paid (1974/5 multiplier for dates before 6 April 1974). Costs from 2003 are not indexed. For development land only current use value at acquisition is indexed. Use Revenue's multiplier table ([Indexation Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/inflation-relief.aspx)). If the year of a pre-2003 cost is unknown, stop.

**Shares: which shares were sold.** Oldest first (FIFO). Shares sold within four weeks of a purchase are matched with the shares bought in those four weeks (LIFO), then FIFO for any excess. Where shares are sold and bought back within four weeks, a loss on the sale can only be used against a gain on the repurchased shares ([selling shares](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/selling-or-disposing-of-shares.aspx)). For crypto-assets with many lots, document the lot trail and refer the identification method.

**Losses (s.546).** Set against gains of the same year, then carried forward to the next available gains. No carry-back, except losses in the year of death, which go against the deceased's gains of the previous three years. A development land loss can be used against any gain; a development land gain can be reduced only by development land losses. A jointly assessed couple's losses are set against the other's gains unless the partner applies by 1 April of the following year to keep them. A loss with no gains that year can be claimed on the return for the next year with a gain ([if you make a loss](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx)). Refer a loss on a disposal to a connected person.

**Principal Private Residence relief (s.604).** Full exemption where, for the whole ownership, the owner lived in the house or apartment as the main residence and used all of it as the home, with up to one acre of land. The last 12 months of ownership always count. Part business use: relief only on the home part (Rent a Room Relief does not affect full exemption). Not always lived in: relief for the months of occupation plus the last 12, apportioned over ownership. Absences treated as occupation: employer required living elsewhere (four years maximum); a job with all duties outside the State; or the home empty while the owner was in hospital, a nursing or convalescent home, or a fee-paying retirement home. Development value: relief only on the value without it; refer ([PPR Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx)). Illustration (hypothetical): bought 2012 for 300,000, lived in for 120 months, then let; sold December 2026 for 520,000 less 8,000 costs; ownership 180 months. Gain 212,000; chargeable part 48/180 = 56,533.33; less 1,270 = 55,263.33; at 31% = 17,131.63, payable by 31 January 2027.

**Revised Entrepreneur Relief (s.597AA).** 10% on gains from chargeable business assets up to the lifetime limit (EUR 1,000,000 for gains 2016 to 2025; EUR 1,500,000 for gains from 1 January 2026, with earlier 2016 to 2025 gains counted up to EUR 1,000,000; s.597AA(4A) to (4C), inserted by [Finance Act 2025 s.51](https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0051.html)). The excess goes at the standard rate for the disposal date ([Revised Entrepreneur Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx)). Conditions:
- Assets: shares in a trading company or holding company of a qualifying group, or a sole trader's trade assets.
- Business: not holding investments, holding development land, or developing or letting land. Every 51% subsidiary must operate a qualifying business; a dormant or non-trading subsidiary stops the relief.
- Ownership: three continuous years within the five years before the disposal; for shares, at least 5% of the ordinary shares for three continuous years at any time before.
- Work: a director or employee spending at least 50% of their time in a managerial or technical capacity for three continuous years within the five years before.
- Excluded: investment assets, development land, assets owned personally outside the company, goodwill sold to a connected company, and shares where the seller stays connected with the company (the last two can still qualify for genuine commercial reasons). Where conditions are unclear, assume not met.

**Retirement Relief (s.598, s.599).** No need to retire. Age 55 or over, or younger only on ill health with medical evidence, reaching 55 within 12 months, and all other conditions met ([Retirement Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx)). Assets: chargeable business assets (not tangible movable property) owned for 10 years to the disposal; family company shares held 10 years by a working director of 10 years, 5 of them full time; farm land has its own letting rules ([TDM 19-06-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-06-03.pdf)).
- To a child (s.599): relief restricted to EUR 10 million (55 to 69) or EUR 3 million (70 or older), aggregated across transfers. A child includes a stepchild or civil partner's child, an adopted child, a deceased child's child, a niece or nephew who worked full time in the business for five years, and a foster child maintained for five years before 18. Clawback if the child disposes within six years. Above EUR 10 million the parent may claim deferral on the return; it crystallises if the child disposes within 12 years. Refer deferral and clawback.
- Outside the family (s.598): full relief where market value does not exceed EUR 750,000 (55 to 69) or EUR 500,000 (70 or older), lifetime. Above that, marginal relief limits the CGT to half the excess over the threshold. For 2014 to 2024 disposals the age split was 66. Illustration (hypothetical): aged 60, sold March 2026 for 900,000, cost 200,000. Without relief: (700,000 less 1,270) at 33% = 230,910.90. Marginal limit: half of 150,000 = 75,000, so CGT is 75,000, with no EUR 1,270 exemption (s.601(5)).

**Site to a child (s.603A).** No CGT on land to a child to build their only or main home, where the site is one acre or less and worth EUR 500,000 or less, including a joint transfer by both parents. The child pays the CGT if they dispose of the land without building, or without living in the house for three years (not on a disposal to their spouse or civil partner) ([site to a child](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx)).

**Compensation or insurance** for damage or loss can be a disposal; where the money repairs or replaces the asset, a deferral claim is possible but not automatic. Refer.

## Deadlines and filing

- **Pay first.** Disposals 1 January to 30 November 2026 (initial period): pay by **15 December 2026**. Disposals 1 to 31 December 2026 (later period): pay by **31 January 2027** ([pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)). Near a boundary, confirm the contract date and err toward the earlier date.
- **Then file** by **31 October 2027** for 2026 disposals, even if no tax is due because of reliefs or losses. The return shows assets disposed of, proceeds, reliefs, losses brought forward, the gain or loss, the taxable gain and rate, and the CGT already paid.
- **Which return.** Form CG1 (paper only) for someone who does not usually file returns; paper Form 12 for a PAYE taxpayer who must file (CGT cannot go on the online eForm 12); Form 11 on ROS for the self-employed or those with non-PAYE income (see `ie-income-tax-form11`, Panel L); Form 1 for trusts and estates and CT1 for companies are out of scope.
- **ROS extension.** eBrief 034/26 extends the ROS date to 18 November 2026 for 2025 Form 11 returns and income tax payments; it does not mention CGT. Do not move a CGT payment date on the strength of it ([eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).
- **Registration and payment.** Someone not registered for CGT registers in myAccount or ROS (tax reference or PPSN) and pays online. Someone exempt from e-filing can email the Collector-General's Payment Accounting section or pay with CGT Payslip A (initial period) or B (later period).
- **CG50A clearance (s.980).** Applies where the consideration for a specified asset exceeds EUR 500,000, or EUR 1,000,000 for a house or apartment. Specified assets: land and minerals in the State and related rights; continental shelf rights; unquoted shares deriving their value or most of it from those; shares received in exchange for such shares; and goodwill of a trade in the State ([TDM 42-03-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf)). The vendor gets a CG50A if resident in Ireland or if the CGT due has been paid; apply through eCG50 in myAccount or ROS (paper CG50 for those who cannot apply online). Without it the purchaser withholds 15% and gives the vendor Form CG50B, which the vendor uses to reclaim ([CG50A](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx)). Apply before completion.
- **Records.** Keep contracts, valuations, broker notes, cost invoices, CG50A or CG50B documents, and for PPR the occupation evidence for the whole ownership. This skill does not state a retention period.

## Penalties and interest

- **Late payment interest (s.1080).** CGT paid after the 15 December or 31 January date carries interest at 0.0219% for each day or part of a day ([TDM, interest on late payment](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)). Revenue's pay and file page: "A late payment will incur an interest charge. A late Return will incur a penalty."
- **Late filing surcharge (s.1084).** In s.1084 "tax" is income tax, corporation tax or capital gains tax ([Notes for Guidance, TCA Part 47, Finance Act 2025 edition](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part47.pdf)). The surcharge is a percentage of the total tax for the year: 5% (max EUR 12,695) if filed within two months after the return date, 10% (max EUR 63,485) after that ([Revenue Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). For a 2026 disposal: on time by 31 October 2027; 5% to 31 December 2027; 10% after.
- **Incorrect returns.** A deliberately or carelessly incorrect return is treated as late unless corrected by the return date; penalties under s.1077E or s.1077F replace the surcharge where the return was on time (Notes for Guidance, Part 47).
- **No CG50A.** Not a penalty, but 15% of the price is withheld until reclaimed.

## Cross-border points

- **Non-residents** are chargeable only on the Irish assets listed in "Who this applies to". If an asset is not on that list, flag for review rather than assume no charge. The EUR 1,270 exemption applies to non-resident individuals too.
- **CG50A for non-residents.** A non-resident vendor of a specified asset above the s.980 threshold gets a CG50A only by paying the CGT due; otherwise the purchaser withholds 15%.
- **Transfer to a non-resident spouse** who is not liable to CGT is not exempt. Refer.
- **Foreign CGT paid** can be credited on the return where a treaty or unilateral relief applies; treaty analysis is in `ie-foreign-tax-and-withholding` and `ie-cross-border`. Refer.
- **Resident but not domiciled** with gains on foreign assets: remittance rules, see `ie-non-dom`. Refer.
- **Foreign life policies and offshore funds** have their own rates and regimes. Refer.

## Worked examples

**Example 1. Listed shares sold in May 2026 (33%, simple).** Mr Ó Briain, Irish resident, sells 5,000 shares in an Irish listed company on 12 May 2026 for 75,000 after commission. He bought 3,000 in June 2018 for 18,000 and 2,000 in February 2021 for 22,000. No other disposals, no purchases in the four weeks before, no losses. FIFO uses the 2018 shares, then the 2021 shares; together they are the whole sale. No indexation (costs after 2002). The disposal is before 7 October 2026, so 33%. Gain 35,000, less 1,270, taxable 33,730, CGT 11,130.90. Pay by 15 December 2026; file by 31 October 2027 (Form 11 if he is a chargeable person, otherwise Form 12 or CG1). If he paid on 15 January 2027, interest for 31 days would be 11,130.90 x 0.0219% x 31.

```oa-check
name: Listed shares sold 12 May 2026, FIFO, 33% rate
inputs:
  proceeds: 75000
  cost_2018: 18000
  cost_2021: 22000
  exemption: 1270
  rate: 33
  late_days: 31
  daily_interest_bp: 219
steps:
  - gain: proceeds - cost_2018 - cost_2021
  - taxable: max(gain - exemption, 0)
  - cgt: taxable * rate / 100
  - interest_if_late: round(cgt * daily_interest_bp / 1000000 * late_days, 2)
expected:
  gain: 35000
  taxable: 33730
  cgt: 11130.90
  interest_if_late: 75.57
```

**Example 2. Founder sells her trading company on 2 November 2026 (Entrepreneur Relief over the limit, 31% on the excess).** Ms de Paor founded an Irish trading company in 2018 and has held all its ordinary shares and worked full time as a director since. The company has no subsidiaries and no Irish land. On 2 November 2026 she sells all the shares to an unrelated buyer for 2,010,000, keeps no connection, and has no earlier qualifying gains. Cost 10,000. Gain 2,000,000. The gain arises in 2026, so the lifetime limit is 1,500,000 at 10%: 150,000. The excess of 500,000 is taxed at the standard rate for the disposal date. The disposal is after 7 October 2026, so 31%. The EUR 1,270 exemption goes against the higher-rate part first (s.601(3)): 498,730 at 31% = 154,606.30. Total 304,606.30. The disposal is in the initial period, so she pays by 15 December 2026. If the 31% rate lapsed, the excess would be at 33%: 164,580.90, total 314,580.90. The shares are unquoted but do not derive their value from Irish land, so s.980 does not apply.

```oa-check
name: Entrepreneur Relief, gain EUR 2,000,000, disposal 2 Nov 2026, excess at 31% (33% fallback)
inputs:
  proceeds: 2010000
  cost: 10000
  er_limit: 1500000
  er_rate: 10
  exemption: 1270
  rate_new: 31
  rate_old: 33
steps:
  - gain: proceeds - cost
  - qualifying: min(gain, er_limit)
  - cgt_er: qualifying * er_rate / 100
  - excess: gain - qualifying
  - excess_taxable: max(excess - exemption, 0)
  - cgt_excess: excess_taxable * rate_new / 100
  - total_cgt: cgt_er + cgt_excess
  - total_if_33: cgt_er + excess_taxable * rate_old / 100
expected:
  gain: 2000000
  qualifying: 1500000
  cgt_er: 150000
  excess: 500000
  excess_taxable: 498730
  cgt_excess: 154606.30
  total_cgt: 304606.30
  total_if_33: 314580.90
```

## Ask the client first

1. When was the contract signed, and was it written? (Tax year, payment date, and 33% or 31%. If the date cannot be shown to be on or after 7 October 2026, use 33%.)
2. Are you resident in Ireland, and what is the asset and where is it? (Non-residents pay only on the listed Irish assets.)
3. How, when and for how much did you acquire it, and do you have the documents? (Gift, inheritance or pre-1974 means market value; costs to 2002 are indexed. No cost evidence, no computation.)
4. Who is the buyer or recipient: spouse or civil partner, child, connected person, or unconnected buyer?
5. If it is your home: which months did you live in it, was it let or used for business, how much land, any development value?
6. If it is a business or company shares: your age, shareholding, ownership and working periods, group structure, and every earlier Entrepreneur Relief or Retirement Relief claim. Also any losses brought forward, and whether a CG50A is needed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue, How to calculate CGT (31% from 7 Oct 2026, 33% development land, other rates, EUR 1,270) | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx | 2026-10-26 |
| Revenue, When and how do you pay and file CGT | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx | 2026-10-26 |
| Revenue, Revised Entrepreneur Relief | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx | 2026-10-26 |
| Finance Act 2025 s.51 (s.597AA(4) to (4C), EUR 1,500,000 limit) | https://www.irishstatutebook.ie/2025/en/act/pub/0018/sec0051.html | 2026-10-27 |
| Oireachtas, Finance (No. 2) Bill 2026 (Bill 98), stage page | https://www.oireachtas.ie/en/bills/bill/2026/98/ | 2026-10-26 |
| Finance (No. 2) Bill 2026, as initiated, s.36 | https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf | 2026-10-24 |
| Revenue TDM, Guidelines for charging interest on late payment (CGT 0.0219% a day) | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-24 |
| Revenue, Notes for Guidance TCA Part 47, Finance Act 2025 edition (s.1080, s.1084) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part47.pdf | 2026-10-24 |
| Revenue, Guide to completing 2025 returns (surcharge 5% / 10%, Panel L) | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf | 2026-10-24 |
| Dáil Éireann debate, 6 October 2026, Financial Resolution No. 3 | https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml | 2026-10-23 |
| Finance Act 2010 s.160; Finance Act 1974 s.85; Appropriation Act 1991 s.2; Finance Act 1992 s.250 (provisional collection) | https://www.irishstatutebook.ie/2010/en/act/pub/0005/sec0160.html ; https://www.irishstatutebook.ie/1974/en/act/pub/0027/sec0085.html ; https://www.irishstatutebook.ie/1991/en/act/pub/0032/print.html ; https://www.irishstatutebook.ie/1992/en/act/pub/0009/sec0250.html | 2026-10-23 |
| Finance Act 2013 s.43 (33%; development land s.649A) | https://www.irishstatutebook.ie/eli/2013/act/8/section/43/enacted/en/html | 2026-10-23 |
| TCA 1997 s.601 as enacted; TDM 19-07-01 | https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-07-01.pdf | 2026-10-23 |
| TCA 1997 s.602 and s.603 as enacted | https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html ; https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html | 2026-10-02 |
| Revenue, CGT overview | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx | 2026-10-02 |
| Revenue, What do you pay CGT on | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx | 2026-10-02 |
| Revenue, What is exempt from CGT | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx | 2026-10-02 |
| Revenue, If you make a loss | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx | 2026-10-02 |
| Revenue, Selling or disposing of shares | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/selling-or-disposing-of-shares.aspx | 2026-10-02 |
| Revenue, CG50A clearance certificate | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx | 2026-10-02 |
| Revenue, CGT reliefs overview | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/index.aspx | 2026-10-02 |
| Revenue, PPR Relief | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx | 2026-10-02 |
| Revenue, Retirement Relief (disposal of a business or farm) | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx | 2026-10-02 |
| Revenue, Indexation Relief | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/inflation-relief.aspx | 2026-10-02 |
| Revenue, Site from a parent to a child | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx | 2026-10-02 |
| Revenue TDM 19-06-03 (Retirement Relief) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-06-03.pdf | 2026-10-02 |
| Revenue TDM 42-03-01 (section 980) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf | 2026-10-02 |
| Revenue TDM 02-01-03 (crypto-assets) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf | 2026-10-02 |
| Revenue eBrief 034/26 (ROS extension 2026) | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-02 |

Not yet confirmed: (1) whether the Finance (No. 2) Act 2026 is enacted with the 31% rate unchanged (Bill 98 had completed only Dáil First Stage on 26 October 2026); (2) s.601(3) and (5) were read as enacted, with no official consolidated TCA text to confirm later Finance Acts changed only the amount (Revenue TDM 19-07-01 confirms EUR 1,270 and subsection (5)); (3) the s.1084 surcharge figures come from Revenue's Form 11 guide and Notes for Guidance; no Revenue page was found applying them to a stand-alone Form CG1; (4) Revenue's rate table prints the 33% start date as 6 December 2021, read as a misprint of 6 December 2012 (Finance Act 2013 s.43); (5) the CGT indexation multipliers are not reproduced here; (6) no record retention period is stated.

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
