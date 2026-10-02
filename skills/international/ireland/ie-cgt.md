---
name: ie-cgt
description: ALWAYS read this skill before touching any Irish Capital Gains Tax work. Trigger on phrases like "Ireland CGT", "33% capital gains Ireland", "PPR exemption Ireland", "Entrepreneur Relief Ireland", "CG50 clearance", "Irish Capital Gains Tax", "Form CG1", "preliminary CGT Ireland", "Retirement Relief Ireland", "Section 597AA", "Section 598", "Section 599", "Revenue Online Service CGT", "ROS CGT", "Irish share disposal tax", "Euronext Dublin share sale CGT", "Irish property gain", "non-resident CGT Ireland", "Irish-situs CGT", "crypto CGT Ireland", or any question about computing, filing, or reporting capital gains on Irish chargeable assets. Scope covers CGT computation for chargeable assets (real property, shares, business assets, crypto, intangibles), the Principal Private Residence relief, Entrepreneur Relief (Section 597AA), Retirement Relief (Sections 598/599), the annual exemption, the CG50 clearance regime for high-value land disposals, loss relief, and the preliminary-CGT / final-return mechanics under Form CG1 via ROS. ALWAYS read this skill before producing any Irish CGT figure.
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland Capital Gains Tax (CGT) for individuals

This Guide is a source-cited draft by the OpenAccountants team. No accountant has reviewed it. It sets out how to compute, pay and report Irish Capital Gains Tax on a disposal by an individual: the chargeable gain, the personal exemption, the rates, the main reliefs, losses, share identification, the CG50A clearance and the payment and return dates. Figures are for tax year 2026. The Irish tax year is the calendar year. Every figure below sits in a table that names the Revenue page it comes from. Check the Revenue pages for any change announced after 2 October 2026.

## Section 1: Quick reference

**Section 1: Quick reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Ireland |
| Tax | Capital Gains Tax (CGT) |
| Currency | EUR |
| Tax year | 1 January to 31 December (calendar year) |
| Primary legislation | Taxes Consolidation Act 1997 (Revenue cites, among others, sections 546, 552, 556, 573, 597AA, 598, 599, 601, 603A, 604 and 980) |
| Standard rate | 33% for most gains (see the "How to calculate CGT" table) |
| Revised Entrepreneur Relief rate | 10% on gains from chargeable business assets, up to a lifetime limit of gains (see the Entrepreneur Relief table) |
| Personal exemption | EUR 1,270 of gains each tax year, per individual, not transferable to a spouse or civil partner |
| Tax authority | Office of the Revenue Commissioners ("Revenue") |
| Returns | Form CG1 (paper), Form 12 (paper), Form 11 or Form 1, depending on who files (see Section 6.1) |
| Payment | By disposal date: 1 January to 30 November pays by 15 December of the same year; 1 December to 31 December pays by 31 January of the next year |
| Status | Source-cited draft by the OpenAccountants team. No accountant has reviewed it |
| Guide version | 2.0 |

### Figures by official source

**How to calculate CGT (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx |
| Rate for most gains, disposals on or after 6 December 2012 | 33% | "The rate of CGT is 33% for most gains." |
| Gains from foreign life policies and foreign investment products | 40% | "40% for gains from foreign life policies and foreign investment products." |
| Gains from venture capital funds, individuals and partnerships | 15% | "15% for gains from venture capital funds for individuals and partnerships." |
| Gains from venture capital funds, companies | 12.5% | "12.5% for gains from venture capital funds for companies." |
| Historic rate, disposals 7 December 2011 to 5 December 2012 | 30% | "5 December 2012 30%" |
| Historic rate, disposals 8 April 2009 to 6 December 2011 | 25% | "6 December 2011 25%" |
| Historic rate, disposals 15 October 2008 to 7 April 2009 | 22% | "7 April 2009 22%" |
| Historic rate, disposals up to and including 14 October 2008 | 20% | "Up to, and including, 14 October 2008 20%" |

**What is exempt from CGT (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx |
| Personal exemption, each tax year, after losses | EUR 1,270 | "Each tax year, the first €1,270 of your gain or gains (after deducting losses) are exempt from CGT." |
| Moveable property such as furniture: exempt where the gain does not exceed | EUR 2,540 | "moveable property (such as furniture), where the gain does not exceed €2,540" |

**Revised Entrepreneur Relief (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx |
| Rate on gains from chargeable business assets | 10% | "This relief gives a CGT rate of 10% on gains from the disposal of chargeable business assets." |
| Rate for disposals 1 January to 31 December 2016 | 20% | "The rate is 20% for disposals from 1 January to 31 December 2016." |
| Lifetime limit, gains arising 1 January 2016 to 31 December 2025 | EUR 1,000,000 | "You can claim the relief on the first €1,000,000 of gains arising between 1 January 2016 and 31 December 2025." |
| Lifetime limit, gains arising on or after 1 January 2026 | EUR 1,500,000 | "For gains arising on or after 1 January 2026, the lifetime limit increases to €1,500,000." |
| Shares: minimum holding of the ordinary shares, for a continuous three years | 5% | "you must have owned at least 5% of the ordinary shares for a continuous period of three years." |
| Director or employee: minimum share of time in a managerial or technical capacity | 50% | "spent no less than 50% of your time in the service of the company" |
| Group: subsidiaries of the holding company that must each operate a qualifying business | 51% | "It must hold shares in other companies, all of which are its 51% subsidiaries." |

**Disposal of a business or farm (Retirement Relief) (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx |
| Transfer to a child on or after 1 January 2025, owner aged 55 to 69: relief restricted to | EUR 10 million | "between 55 and 69, the relief is restricted to €10 million" |
| Transfer to a child on or after 1 January 2025, owner aged 70 or older: relief restricted to | EUR 3 million | "70 or older, the relief is restricted to €3 million." |
| Disposal outside the family on or after 1 January 2025, owner aged 55 to 69: lifetime threshold for full relief | EUR 750,000 | "€750,000 for disposals made: from 1 January 2014 to 31 December 2024 (inclusive) and you are between 55 and 65 or on, or after, 1 January 2025 and you are between 55 and 69." |
| Disposal outside the family on or after 1 January 2025, owner aged at least 70: lifetime threshold for full relief | EUR 500,000 | "€500,000 for disposals made from 1 January 2014 to 31 December 2024 (inclusive) and you are at least 66 or on, or after, 1 January 2025 and you are at least 70 years old." |

**Transfer of a site from a parent to a child (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx |
| Maximum value of the site (the site must also be one acre or less) | EUR 500,000 | "be one acre or less and have a value of €500,000 or less." |

**Tax and Duty Manual Part 42-03-01, section 980 (Revenue)**

| Item | Figure | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf |
| Purchaser deducts this share of the consideration if no certificate is produced | 15% | "the purchaser is required to deduct 15% from the consideration and remit that amount to Revenue." |
| Section 980 applies where the consideration for a specified asset exceeds | EUR 500,000 | "where the consideration exceeds €500,000, or €1,000,000 if the asset disposed of is a house." |
| Threshold where the asset is a house | EUR 1,000,000 | "where the consideration exceeds €500,000, or €1,000,000 if the asset disposed of is a house." "A house includes an apartment for the purpose of the definition." |

### CGT rate at a glance

**CGT rate at a glance table**

| Asset class or scenario | Rate or treatment | Notes |
| --- | --- | --- |
| Most chargeable gains (land, buildings, shares, crypto-assets, goodwill and other intangibles) | 33% | Rate since 6 December 2012. Revenue's crypto-asset manual lists crypto-assets among the assets on which CGT arises ([Tax and Duty Manual Part 02-01-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf)) |
| Qualifying gains under Revised Entrepreneur Relief | 10% | Up to the lifetime limit for the period the gain arises in (see the Entrepreneur Relief table). Gains above the limit go at 33% |
| Foreign life policies and foreign investment products | 40% | Out of scope of this Guide. Refer |
| Venture capital funds | 15% (individuals and partnerships) or 12.5% (companies) | Out of scope of this Guide. Refer |
| Principal Private Residence, owned and fully occupied as the main home throughout ownership | Exempt | Restricted where not fully occupied, partly used for business, or sold with development value (Section 4.1) |
| Specified asset sold for more than EUR 500,000 (EUR 1,000,000 for a house or apartment) with no CG50A | Purchaser deducts 15% | The vendor reclaims it using Form CG50B (Section 4.7) |
| Non-resident disposing of Irish land, buildings, minerals, continental shelf rights, certain unquoted shares, or assets of a trade carried on in Ireland | 33% | Section 3.1 |

## Ask the client first

- When was the contract signed, and was it a written contract? The time of disposal is usually the contract date, and it decides both the payment date and the tax year ([pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
- Are you resident in Ireland, and what is the asset and where is it? A non-resident pays Irish CGT only on the assets listed in Section 3.1 ([CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx)).
- How did you acquire the asset, when, and for how much? A gift or inheritance, or a purchase before 6 April 1974, changes the base cost to market value, and costs paid up to 31 December 2002 can be indexed ([how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx), [indexation](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/inflation-relief.aspx)).
- Who is the buyer or recipient? A spouse or civil partner, a child, or an unconnected third party each lead to a different rule ([exemptions](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx), [Retirement Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx)).
- If it is your home: which months did you live in it, was any part used for a business, was it let, and does the price include development value ([PPR Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx))?
- If it is a business or shares in your company: your age at the disposal, how long you have owned the assets and worked in the business, your shareholding, and every earlier claim to Entrepreneur Relief or Retirement Relief ([Entrepreneur Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx), [Retirement Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx)).

## The method, step by step

1. **Fix the disposal and its date.** A sale, gift, exchange, or receipt of compensation or insurance money for an asset is a disposal. Under a written contract the time of disposal is usually the contract date. The date puts the disposal in a tax year and in a payment period. [CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx) and [pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)
2. **Check the person is chargeable on this asset.** A non-resident individual is chargeable only on the assets listed in Section 3.1. A company normally includes its gains in Corporation Tax, except gains on development land, which go to CGT. Refer companies. [CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx)
3. **Remove exempt disposals.** Betting, lottery wins, prize bonds, government stocks, certain life assurance policies, animals, private motor cars and moveable property where the gain does not exceed the amount in the "What is exempt" table are exempt. A transfer to a spouse or civil partner is usually exempt, with the exceptions in Section 3.5. There is generally no CGT on an asset transferred on death. [What is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx)
4. **Compute the chargeable gain on each disposal.** Proceeds (or market value where Section 3.5 requires it) less the purchase price and allowable expenses: enhancement expenditure, and fees such as solicitor's and auctioneer's fees on acquisition and disposal. For costs paid up to 31 December 2002, apply the indexation multiplier for the year the cost was paid (Section 4.4). For shares, identify the shares sold under Section 3.7. [How to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx) (Taxes Consolidation Act 1997, section 552)
5. **Apply reliefs that remove or reduce the gain.** Principal Private Residence Relief (section 604), Retirement Relief (sections 598 and 599), the site to a child relief (section 603A), each as set out in Section 4. [CGT reliefs](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/index.aspx)
6. **Add the year's gains and deduct allowable losses.** Deduct current-year losses, then losses brought forward. Development land losses and gains have their own ring-fence (Section 3.6). [If you make a loss](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx) (section 546)
7. **Deduct the personal exemption.** An individual deducts the EUR 1,270 personal exemption from the year's gains after losses. It is per individual, whether resident or non-resident, and cannot be transferred to a spouse or civil partner, or used by a company or trust. [What is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx) (section 601)
8. **Apply the rate.** 33% for most gains. 10% on qualifying gains under Revised Entrepreneur Relief, up to the lifetime limit for the period the gain arises in; the excess goes at 33%. Other rates in the "How to calculate CGT" table are out of scope. A credit for foreign CGT paid may be claimed on the return. [How to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx) and [Entrepreneur Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx) (section 597AA)
9. **Check the CG50A clearance before completion.** On a sale of a specified asset for more than EUR 500,000 (more than EUR 1,000,000 for a house or apartment), the vendor needs a CG50A or the purchaser deducts 15% (Section 4.7). [CG50A](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx) and [Tax and Duty Manual Part 42-03-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf)
10. **Pay by the date for the disposal's period, then file.** Disposals 1 January to 30 November: pay by 15 December of the same year. Disposals 1 December to 31 December: pay by 31 January of the next year. File the return on or before 31 October of the year after the disposal, even if no tax is due because of reliefs or losses (Section 6). [Pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing Irish CGT.** Obtain:
  1. Identity and residence: name, PPSN or tax reference, and whether the person is resident in Ireland.
  2. Asset: its type (land, buildings, shares, business asset, crypto-asset, intangible, moveable property) and where it is.
  3. Acquisition: date, price or market value, and the incidental costs (solicitor, auctioneer), with documents. For an inherited asset, the market value at the date of death.
  4. Disposal: contract date, gross proceeds, and the incidental costs of disposal.
  5. Recipient: spouse or civil partner, child, other relative, or unconnected buyer; whether it was a gift or a sale below value to help the buyer.
  6. For a home: the full timeline of occupation, any letting, any business use, the land area, and whether the price includes development value.
  7. For Entrepreneur Relief: the shareholding, ownership dates, the role and time spent in the company, the trading activity of the company and its group, and earlier qualifying gains since 1 January 2016.
  8. For Retirement Relief: age at the disposal, ownership and working periods, whether the recipient is a child (as defined in Section 4.3), and earlier disposals that count towards the lifetime thresholds.
  9. For shares: every purchase and sale date and quantity, including purchases in the four weeks before a sale and repurchases in the four weeks after.
  10. For costs paid up to 31 December 2002: the year each cost was paid, for the indexation multiplier.
  11. Losses brought forward, and for married couples or civil partners whether they are jointly assessed.
  12. For a specified asset sold for more than the section 980 threshold: whether a CG50A has been obtained.

### Refusal catalogue

**Refusal catalogue table**

| Trigger | Reason |
| --- | --- |
| Acquisition cost unknown or undocumented | Cannot compute the chargeable gain. Do not estimate |
| Asset acquired by gift or inheritance with no market value evidence | Base cost is market value; obtain a valuation first ([how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx)) |
| Resident but not domiciled in Ireland, with gains on foreign assets | The remittance rules are not covered by this Guide. Refer |
| Disposal of a partnership interest | Not covered. Refer |
| Trust or estate disposals (Form 1) | Not covered. Refer |
| Foreign life policies, foreign investment products, venture capital funds | Different rates and regimes. Refer |
| Company reorganisations, mergers, reconstructions, share-for-share exchanges | Not covered. Refer |
| Cross-border disposal where a double tax treaty or a foreign tax credit may apply | Treaty analysis needed. Refer |
| Development land | Separate loss ring-fence and indexation rules. Refer |
| Home claimed as PPR but let, partly used for business, more than one acre, or sold with development value | Apportionment required. Prepare it, then refer for sign-off |
| Entrepreneur Relief claimed without evidence of the ownership and working periods | Cannot confirm section 597AA eligibility |
| Retirement Relief where earlier disposals may have used the lifetime threshold | Aggregate the earlier disposals first |
| Specified asset sold for more than the section 980 threshold with no CG50A | Confirm the 15% deduction before completion |

## Section 3: Chargeable persons, chargeable assets, computation

### 3.1 Chargeable persons

- **Chargeable persons.** CGT is payable by the person making the disposal. Irish resident individuals are generally subject to CGT on gains arising on the disposal of assets ([Tax and Duty Manual Part 02-01-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf)). A non-resident individual pays CGT on gains on: land, buildings and minerals in Ireland; exploration or exploitation rights in the Irish continental shelf; unquoted shares deriving the greater part of their value from land, buildings or minerals in Ireland or from exploitation rights in the Irish continental shelf; and assets used for the purpose of a trade carried on in Ireland. A company normally includes its capital gains in its profits for Corporation Tax; a company's gain on development land is charged to CGT instead. Source: [CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx).

### 3.2 Chargeable assets

- **Chargeable assets.** CGT is due on gains from the sale, gift or exchange of assets such as land (including development land), buildings, shares in Irish-resident or non-resident companies, goodwill, patents and copyright, currency other than Irish currency, assets of a trade, foreign life insurance policies and offshore funds, and capital payments in certain situations. Antiques, paintings and jewellery can also be chargeable. Compensation and insurance money for damage, destruction or loss of an asset may be a disposal; where the money is used to repair or replace the asset, the person may claim to defer the CGT (the claim is not automatic). Crypto-assets are listed by Revenue among the assets on which CGT arises. A jointly owned asset is taxed on the owner's share of the gain. Sources: [what do you pay CGT on](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx), [Tax and Duty Manual Part 02-01-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf).
- **Exempt.** Betting, lottery wins, prize bonds, sweepstakes, bonuses under the National Instalments Savings Scheme, government stocks, certain life assurance policies, animals and private motor cars. Section 603 of the Taxes Consolidation Act 1997 as enacted provides that no chargeable gain accrues on tangible movable property that is a wasting asset, except an asset used solely for a trade or profession on which capital allowances were or could have been claimed ([section 603 as enacted](https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html)). And moveable property (such as furniture) where the gain does not exceed EUR 2,540. Source: [what is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx). Revenue's page states this test as the gain. Section 602 of the Taxes Consolidation Act 1997 as enacted states it as the amount or value of the consideration for the disposal, and excludes a wasting asset ([section 602 as enacted](https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html); the enacted text prints the 1997 amount in punts and does not prove the current figure). Where the sale price is above the figure in the table, refer.

### 3.3 Computation formula

- **Chargeable gain computation formula.** Chargeable gain = proceeds (or market value) less the purchase price (or market value at acquisition) less allowable expenses. Where indexation applies, each cost paid up to 31 December 2002 is multiplied by the multiplier for the year it was paid. Annual computation, per [how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx):
  1. Compute the chargeable gain on each disposal in the tax year.
  2. Add the gains together and deduct allowable losses.
  3. Deduct the personal exemption of EUR 1,270 (individuals only) and any other exemptions or reliefs.
  4. Multiply the taxable gain by the rate: 33%, or 10% on the part that qualifies for Revised Entrepreneur Relief.

### 3.4 Allowable deductions (section 552)

- **Allowable deductions.** The purchase price; money spent that adds value to the asset (enhancement expenditure); and costs such as solicitor's or auctioneer's fees paid when acquiring and disposing of the asset. Source: [how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx). Routine repairs that do not add value are not enhancement expenditure; treat them as not deductible (Section 7).

### 3.5 Market value, spouses and death

- **When market value replaces the price.** Use market value where the asset was a gift to someone other than a spouse or civil partner; where it was sold for less than its worth to help the buyer; where it was inherited and is now being disposed of; or where it was bought before 6 April 1974. Source: [how to calculate](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx).
- **Spouses and civil partners.** A gain on a transfer between spouses or civil partners is usually exempt, including divorced spouses and separated or former civil partners. The exemption does not apply to: trading stock of the transferor's business; a transfer to a spouse or civil partner who is non-resident and not liable to CGT; or a transfer to a former spouse or civil partner that is not covered by a court order. Source: [what is exempt](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx).
- **Inherited assets.** In general there is no CGT on an asset transferred on death. A person who inherits an asset is treated as owning it from the date of death, at a cost equal to the market value at that date. A personal representative who sells during the administration period may owe CGT. Source: [CGT overview](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx).

### 3.6 Capital losses (section 546)

- **Capital losses treatment.** An allowable loss is deducted from chargeable gains of the same tax year, subject to certain exceptions. Losses that cannot be used are carried forward against the next available gains in later years. Losses cannot be set against gains of earlier years, except losses made in the year of death, which can be deducted from the deceased's gains for the previous three years. A development land loss can be deducted from any chargeable gain, but a gain on development land can be reduced only by development land losses. Source: [if you make a loss](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx).
- **Spouses and civil partners.** Where a couple is jointly assessed for CGT, one partner's allowable losses are automatically set against the other's chargeable gains, unless the partner applies to keep their own loss on or before 1 April of the following year. Source: [if you make a loss](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx).

### 3.7 Shares: which shares were sold

- **Share identification.** Where only some shares of a holding are sold, the oldest shares are treated as sold first (first in, first out). Where shares are sold within four weeks of a purchase, the shares sold are treated as those bought in the four weeks before (last in, first out); any excess over those purchases follows first in, first out. Where shares are sold and repurchased within four weeks, a loss on the sale can only be set against a gain on a later disposal of the repurchased shares. Source: [selling or disposing of shares](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/selling-or-disposing-of-shares.aspx).

## Section 4: Reliefs: PPR, Entrepreneur Relief, Retirement Relief, indexation, losses

### 4.1 Principal Private Residence (PPR) relief (section 604)

- **PPR relief, full exemption and restrictions.** A house or apartment owned and occupied as the only or main residence is exempt from CGT if, for the entire period of ownership, the owner lived in it as the main residence AND used all of it as the home. The exemption also covers land up to one acre (0.405 hectares) around the house, not counting the site of the house. The last 12 months of ownership count as occupation. Source: [PPR Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx).
  - **Part business use.** Relief applies only to the part used as the home. Rent a Room Relief does not affect a claim for full exemption.
  - **Not always lived in.** Relief applies only to the time the owner lived in the property, plus the last 12 months. Revenue's example apportions the gain by the years of qualifying occupation (including the last 12 months) over the whole period of ownership; Example B below uses months in the same way.
  - **Absences treated as living there.** Only these: the employer required the owner to live elsewhere (up to a four-year maximum); the owner had a job all of whose duties were performed outside the State; or the property stayed unoccupied while the owner was receiving care in a hospital, nursing home or convalescent home, or was resident in a fee-paying retirement home.
  - **Development value.** Relief applies only to the value without development value; Revenue computes a notional gain on current use value first. Refer these cases.

### 4.2 Revised Entrepreneur Relief (section 597AA)

- **Entrepreneur Relief rate and conditions.** The rate on gains from chargeable business assets is 10% instead of 33%, up to a lifetime limit of gains. The limit is EUR 1,000,000 for gains arising from 1 January 2016 to 31 December 2025, and EUR 1,500,000 for gains arising on or after 1 January 2026. To test the limit, add together all earlier gains on qualifying disposals made on or after 1 January 2016. Gains above the limit are charged at 33%. Source: [Revised Entrepreneur Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx).
  - **Qualifying assets.** Shares held by an individual in a trading company or in a holding company of a qualifying group, OR assets owned by a sole trader and used in their trade.
  - **Qualifying business.** Any business other than holding securities or other assets as investments, holding development land, or developing or letting land. Where the business is in a group, every 51% subsidiary must operate a qualifying business; a dormant company or a non-trading subsidiary in the group stops the relief.
  - **Ownership.** The business assets must have been owned for a continuous three years within the five years immediately before the disposal. For shares, the individual must have owned at least 5% of the ordinary shares for a continuous three years, which can be at any time before the disposal.
  - **Work.** Where the business is operated by a company, the individual must have been a director or employee who spent no less than 50% of their time in the service of the company (or group companies) in a managerial or technical capacity, for a continuous three years within the five years immediately before the disposal.
  - **Excluded disposals.** Shares, securities or other assets held as investments; development land; assets on which no chargeable gain would arise; assets personally owned outside the company even if the company uses them; goodwill disposed of to a connected company; and shares where the individual remains connected with the company after the disposal. For the last two, the relief may still apply if the disposal is for genuine commercial reasons and not for tax avoidance.

### 4.3 Retirement Relief (sections 598 and 599)

- **Retirement Relief conditions and strands.** The owner does not need to retire. The relief is available to an individual aged 55 or older disposing of any part of their business or farming assets. Someone younger than 55 can qualify only if ALL of these hold: they cannot continue the business or farm because of ill health (with medical evidence), they reach 55 within 12 months of the disposal, and every other condition is met. Source: [Retirement Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx).
  - **Ownership and work periods.** Qualifying assets include chargeable business assets (other than tangible movable property) owned for at least 10 years ending on the date of disposal, and shares in the individual's family company held for at least 10 years ending with the disposal where the individual has been a working director for at least 10 years, of which at least 5 years as a full-time working director. Farm land has its own letting conditions. Source: [Tax and Duty Manual Part 19-06-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-06-03.pdf).
  - **Who is a "child".** A son or daughter, stepchild or child of a civil partner, an adopted child, a child of a deceased child, a niece or nephew who has worked full time in the business or farm for at least five years up to the disposal, or a foster child maintained for at least five years before age 18 (with testimony of more than one witness).
  - **Transfer to a child (section 599), on or after 1 January 2025.** Aged 55 to 69: relief is restricted to EUR 10 million. Aged 70 or older: relief is restricted to EUR 3 million. The value transferred to a child is aggregated across transfers (Revenue's example aggregates two transfers to the same son). For transfers from 1 January 2014 to 31 December 2024 the split was at 66, with EUR 3 million for those aged 66 or older.
  - **Clawback and deferral (child).** If the child disposes of the asset within six years, the relief is clawed back: the child pays the CGT on the parent's disposal as well as on their own. Where a transfer to a child on or after 1 January 2025 by someone aged 55 or older exceeds the EUR 10 million limit, the parent may defer the CGT on the excess by claiming deferral on the return for the year of transfer. The deferred CGT crystallises if the child disposes of the assets within 12 years of the transfer.
  - **Disposal outside the family (section 598), on or after 1 January 2025.** Full relief where the market value at the time of disposal does not exceed EUR 750,000 (aged 55 to 69) or EUR 500,000 (aged at least 70). These are lifetime limits: earlier disposals of the business or farm count. Above the threshold, marginal relief may limit the CGT to half the difference between the sale price or market value and the threshold. For disposals from 1 January 2014 to 31 December 2024 the age split was at 66.

### 4.4 Indexation relief (section 556)

- **Indexation relief mechanics.** Indexation applies only to costs paid up to 31 December 2002, while the person owned the asset. Each such cost (the purchase price or market value on acquisition, acquisition costs, enhancement costs) is multiplied by the multiplier for the year it was paid. Costs paid in 2003 or later are not indexed. For a date before 6 April 1974, use the multiplier for 1974/5. For development land, only the current use value at acquisition is indexed; the development value is allowable but not indexed. Source: [Indexation Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/inflation-relief.aspx). Take the multipliers from Revenue's published CGT multiplier table.

### 4.5 Losses

- **Losses treatment detail.** See Section 3.6 for same-year use, carry-forward, the year-of-death carry-back, the development land ring-fence and spouse transfers, and Section 3.7 for the four-week repurchase restriction on shares. A loss with no gains in the same year does not need to go on that year's return; deduct it on the return for the next year with a chargeable gain. Source: [if you make a loss](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx).

### 4.6 Other reliefs in scope

- **Other reliefs list.**
  - Personal exemption: EUR 1,270 per individual per tax year, not transferable to a spouse or civil partner (Section 3.3).
  - Spouses and civil partners: transfers usually exempt, with the exceptions in Section 3.5.
  - Site to a child (section 603A): no CGT on a transfer of land to a child to build the child's only or main residence, where the land is one acre or less AND worth EUR 500,000 or less. A transfer includes a joint transfer by the parent and their spouse or civil partner to the child. The child may have to pay the CGT if they dispose of the land without building a house on it, or without living in the house as their only or main residence for at least three years; this clawback does not apply to a disposal to the child's spouse or civil partner. Source: [site to a child](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx).
  - Exempt assets: Section 3.2.

### 4.7 CG50A clearance (section 980)

- **CG50A withholding mechanics.** Section 980 applies where the consideration for a specified asset exceeds EUR 500,000, or EUR 1,000,000 if the asset is a house or apartment. A house includes an apartment. The specified assets are: land in the State; minerals in the State and related rights; exploration or exploitation rights in the Continental Shelf; shares (other than shares quoted on a stock exchange) deriving their value or the greater part of it from those assets; shares received in exchange for such shares; and goodwill of a trade carried on in the State. Source: [Tax and Duty Manual Part 42-03-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf).
  - To get a CG50A the vendor must meet at least one of these: be resident in Ireland, OR have paid the CGT on the disposal (if it is due). Apply online in myAccount or ROS through the Capital Gains Clearance (eCG50) facility; a paper Form CG50 is still accepted from people who cannot apply online.
  - Without a CG50A, the purchaser must withhold 15% of the purchase price and gives the vendor a Form CG50B, which lets the vendor reclaim the amount from Revenue later.
  - Source: [CG50A](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx).

## Section 5: Worked examples

All amounts in these examples are hypothetical and in EUR. The rates and exemption come from the tables in Section 1.

### Example A: Disposal of shares listed on Euronext Dublin

Facts (hypothetical). Mr Ó Briain, an Irish resident individual, sells 5,000 shares in an Irish listed company on 12 May 2026. He bought 3,000 in June 2018 for 18,000 and 2,000 in February 2021 for 22,000. Proceeds after broker commission are 75,000. He has no other disposals in 2026, no purchases in the four weeks before the sale, and no losses brought forward. First in, first out identifies the 3,000 June 2018 shares first, then the 2,000 February 2021 shares ([selling shares](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/selling-or-disposing-of-shares.aspx)). No indexation (costs paid after 2002). The disposal is in the initial period, so he pays by 15 December 2026 and files by 31 October 2027.

**Example A computation table**

| Line item | Amount (hypothetical, EUR) |
| --- | --- |
| Disposal proceeds | 75,000 |
| Less: cost of 3,000 shares (June 2018) | (18,000) |
| Less: cost of 2,000 shares (February 2021) | (22,000) |
| **Chargeable gain** | **35,000** |
| Less: personal exemption | (1,270) |
| **Taxable gain** | **33,730** |
| CGT at 33% | **11,130.90** |

### Example B: Sale of a former home that was later let (PPR partial)

Facts (hypothetical). Ms Ní Mhurchú bought a house in Galway in January 2012 for 300,000 including purchase costs. She lived in it as her only home until December 2021 (120 months). From January 2022 she let it and lived elsewhere by choice, with no absence that Revenue treats as living there. She signed the sale contract in December 2026 for 520,000, with 8,000 of sale costs. Ownership is 180 months. Qualifying months are 120 of occupation plus the last 12 months of ownership, so 132 of 180 are exempt and 48 of 180 are chargeable ([PPR Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx)). The contract date is in December, the later period, so she pays by 31 January 2027 and files by 31 October 2027. The price is below the section 980 threshold for a house, so no CG50A is needed.

**Example B computation table**

| Line item | Amount (hypothetical, EUR) |
| --- | --- |
| Disposal proceeds | 520,000 |
| Less: incidental costs of disposal | (8,000) |
| Less: purchase price and costs | (300,000) |
| **Total gain** | **212,000** |
| Chargeable part (212,000 × 48 ÷ 180) | 56,533.33 |
| Less: personal exemption | (1,270) |
| **Taxable gain** | **55,263.33** |
| CGT at 33% | **18,236.90** |

### Example C: Entrepreneur disposal of trading company shares in 2026

Facts (hypothetical). Ms de Paor founded an Irish trading company in 2018 and has held all of its ordinary shares since then. She has worked full time as a director throughout, and the company has no subsidiaries. On 1 October 2026 she sells all the shares to an unrelated buyer for 2,010,000, keeps no connection with the company, and has made no earlier qualifying disposals. Her cost was 10,000. The gain arises in 2026, so the lifetime limit is the 2026 figure in the Entrepreneur Relief table ([Revised Entrepreneur Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx)). The shares are unquoted; section 980 catches them only if they derive the greater part of their value from Irish land, minerals or Continental Shelf rights, so confirm what the company owns before completion.

**Example C computation table**

| Line item | Amount (hypothetical, EUR) |
| --- | --- |
| Disposal proceeds | 2,010,000 |
| Less: acquisition cost | (10,000) |
| **Chargeable gain** | **2,000,000** |
| Qualifying part, within the 2026 lifetime limit | 1,500,000 |
| CGT at 10% on the qualifying part | **150,000** |
| Excess over the lifetime limit | 500,000 |
| Less: personal exemption, set against the excess | (1,270) |
| Excess after exemption | 498,730 |
| CGT at 33% on the excess | **164,580.90** |
| **Total CGT** | **314,580.90** |

The Revenue page does not say which part of the gain the personal exemption reduces. This Guide's choice, not Revenue's: this example sets it against the part taxed at 33%. Confirm with the adopting accountant.

### Example D: Retirement Relief, sale outside the family with marginal relief

Facts (hypothetical). Mr Ó Sé, aged 60, has owned and run his business for more than 10 years. In March 2026 he sells it to an unrelated buyer for its market value of 900,000. His cost was 200,000 and he has made no earlier disposals of the business. The market value exceeds the threshold for his age in the Retirement Relief table, so full relief is not available, but marginal relief may limit the CGT to half the excess over the threshold ([Retirement Relief](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx)).

**Example D computation table**

| Line item | Amount (hypothetical, EUR) |
| --- | --- |
| Chargeable gain (900,000 less 200,000) | 700,000 |
| Less: personal exemption | (1,270) |
| CGT at 33% without relief | 230,580.90 |
| Marginal relief limit: half of (900,000 less 750,000) | **75,000** |
| **CGT due (the lower amount)** | **75,000** |

## Section 6: Filing and payment

### 6.1 Returns

- **Return form usage and filing deadline.** File the CGT return on or before 31 October of the year that follows the date of disposal, even if no tax is due because of reliefs or allowable losses. For 2026 disposals that is 31 October 2027. The return depends on the person ([pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)):
  - Form CG1: for someone who does not usually submit annual tax returns or use the online Form 12. It is available only on paper.
  - Form 12 (paper): for a PAYE taxpayer who must submit a tax return. CGT cannot be reported on the online eForm 12.
  - Form 11: for someone self-employed or with income not taxed under PAYE. File it on ROS.
  - Form 1 for a trust or estate, and Form CT1 for a company. Out of scope.
  - The return shows the assets disposed of, the amount received, reliefs claimed, losses brought forward, the chargeable gain or loss, the taxable gain and rate, and the CGT already paid.
- **ROS extension.** Revenue eBrief 034/26 extends the ROS date to 18 November 2026 for 2025 Form 11 returns, for the income tax balance for 2025 and preliminary tax for 2026, and for certain CAT returns. It does not mention CGT. The extension applies only where both the return and the payment go through ROS. Do not move a CGT payment date on the strength of it. [eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)

### 6.2 Payment dates by disposal date

- **Two payment periods.** For disposals made 1 January to 30 November (the initial period), pay the CGT by 15 December of the same year. For disposals made 1 December to 31 December (the later period), pay by 31 January of the next year. The tax is paid before the return is filed; the return then shows the amount already paid. A late payment incurs interest and a late return incurs a penalty. Source: [pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx).

### 6.3 Registration and payment channels

- **ROS and myAccount.** Someone not registered for CGT must register (in myAccount or ROS, using the tax registration number or PPSN) and pay online through ROS or myAccount. Someone exempt from mandatory e-filing can instead email the Collector-General's Payment Accounting section or send payment with CGT Payslip A (initial period) or CGT Payslip B (later period). Source: [pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx).

### 6.4 CG50A mechanics

- **CG50A process detail.** See Section 4.7. Apply through the eCG50 facility in myAccount or ROS before completion. If no CG50A is produced, the purchaser withholds 15% and issues Form CG50B; the vendor reclaims the amount from Revenue. Source: [CG50A](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx).

### 6.5 Records

- **Record keeping.** Keep the purchase and sale contracts, valuations, broker notes, cost invoices, CG50A or CG50B documents, and for a PPR claim the evidence of the dates of occupation for the whole period of ownership. This Guide does not state a retention period; confirm it with the adopting accountant.

## Section 7: Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition cost | STOP. Cannot compute the gain |
| Acquired by gift or inheritance with no market valuation | Obtain a market valuation; if none is available, STOP |
| Home let for part of the ownership | Treat the let months as not qualifying unless an absence in Section 4.1 covers them |
| Land around the home over one acre | Restrict PPR to one acre and refer the apportionment |
| Unclear whether Entrepreneur Relief ownership, holding or working-time conditions are met | Assume not met; use 33% |
| Unknown earlier Entrepreneur Relief or Retirement Relief claims | Assume the limit is partly used; request the history before claiming |
| Indexation year unclear for a cost paid before 2003 | Use Revenue's multiplier table for the year of payment; if the year is unknown, STOP |
| Unknown whether the buyer is connected or paid full value | Use market value and refer |
| Repair or enhancement expenditure unclear | Treat as a repair, not deductible |
| Crypto-asset or share disposals with many lots | Identify shares first in, first out with the four-week rule in Section 3.7; for crypto-assets, document the lot trail and refer the identification method |
| Specified asset sold above the section 980 threshold with no CG50A | Assume the buyer withholds 15%; advise the vendor to apply for a CG50A at once |
| Disposal near the 30 November or 31 December boundary | Confirm the contract date; err toward the earlier payment date |
| Non-resident disposing of an asset in Ireland | Check it is on the Section 3.1 list; if it is not, flag for review rather than assume no charge |
| Possible treaty relief or foreign CGT credit | STOP. Refer |
| Transfer to a spouse or civil partner who is non-resident | The exemption does not apply if they are not liable to CGT; refer |
| Loss on a disposal to a connected person | Refer before using the loss |
| Moveable property sold for more than the chattels figure in the table while the gain is below it | Refer. Revenue's page and the statute state the test differently |

## When to refuse or refer

- Refuse to compute without documented acquisition cost and disposal date.
- Refer: companies, trusts and estates; partnerships; development land; foreign life policies, foreign investment products and venture capital funds; company reorganisations and share exchanges; treaty claims and foreign CGT credits; resident individuals not domiciled in Ireland with foreign gains.
- Refer: PPR claims with development value, business use, letting, or more than one acre, after preparing the apportionment.
- Refer: Retirement Relief deferral claims on transfers to a child above the EUR 10 million limit, and any clawback computation.
- Refer: property acquired between 7 December 2011 and 31 December 2014 (Revenue lists a separate relief for it, not covered here), Farm Restructuring Relief, and compensation or insurance deferral claims ([CGT reliefs](https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/index.aspx)).
- Refer: anything where the client's facts do not match the conditions above word for word.

## Sources

All sources are official Revenue pages, read on 2 October 2026.

1. CGT overview: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/index.aspx
2. What do you pay CGT on: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-do-you-pay-cgt-on.aspx
3. What is exempt from CGT: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx
4. How to calculate CGT: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx
5. When and how do you pay and file CGT: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx
6. If you make a loss: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/if-you-make-a-loss.aspx
7. Selling or disposing of shares: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/selling-or-disposing-of-shares.aspx
8. CGT Clearance Certificate (CG50A): https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/cgt-clearance-certificate-cg50a.aspx
9. CGT reliefs overview: https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/index.aspx
10. Principal Private Residence (PPR) Relief: https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/principal-private-residence-ppr-relief.aspx
11. Revised Entrepreneur Relief: https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/revised-entrepreneur-relief.aspx
12. Disposal of a business or farm (Retirement Relief): https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/disposal-of-a-business-or-farm.aspx
13. Indexation Relief: https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/inflation-relief.aspx
14. Transfer of a site from a parent to a child: https://www.revenue.ie/en/gains-gifts-and-inheritance/cgt-reliefs/transfer-of-a-site-from-a-parent-to-a-child.aspx
15. Tax and Duty Manual Part 19-06-03 (Retirement Relief): https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-19/19-06-03.pdf
16. Tax and Duty Manual Part 42-03-01 (section 980): https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-03-01.pdf
17. Tax and Duty Manual Part 02-01-03 (crypto-assets): https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-02/02-01-03.pdf
18. Revenue eBrief 034/26 (ROS pay and file extension 2026): https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx
19. Section 602 of the Taxes Consolidation Act 1997, as enacted (chattels): https://www.irishstatutebook.ie/eli/1997/act/39/section/602/enacted/en/html
20. Section 603 of the Taxes Consolidation Act 1997, as enacted (wasting assets): https://www.irishstatutebook.ie/eli/1997/act/39/section/603/enacted/en/html

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
