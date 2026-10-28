---
name: gi-corporate-tax
description: >
  Prepare a corporate tax working paper for accounting periods wholly after 1 July 2024, checked in 2026. This draft covers income categories, expense adjustments, capital allowances, trade losses, cessation stock valuation, accounting periods, payments and filing controls. It includes UK treaty permanent-establishment and profit-attribution rules; Pillar Two, specialised exemptions and other treaty corridors remain outside the completed draft scope. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.19"
verified_by: pending
sources:
  - url: "https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force"
    title: "UK–Gibraltar agreement: Articles 3–5, 7–9, 21 and 28–29"
    as_of: "2026-10-28"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf"
    title: "Income Tax Act 2010, 23 March 2026 consolidation"
    as_of: "2026-10-28"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf"
    title: "Rates of Tax Rules 1989, rule 6, 1 July 2024 consolidation"
    as_of: "2026-10-28"
  - url: "https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Guidance%20Notes%20for%20Companies,%2008-2025.pdf"
    title: "Income Tax Office Guidance Notes for Companies, August 2025"
    as_of: "2026-10-22"
  - url: "https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate"
    title: "Income Tax Office corporate filing, payments and penalty guidance"
    as_of: "2026-10-28"
  - url: "https://www.gibraltar.gov.gi/new/sites/default/files/1/01/guidance_on_business_entertainment_expenditure.pdf"
    title: "Income Tax Office business entertainment guidance; undated, limitations noted in body"
    as_of: "2026-10-28"
  - url: "https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Schedule%2010%20Table%20-%20Payments%20on%20Account%20-%202022%20to%202033.pdf"
    title: "Income Tax Office allocation table 2022–2033; stale rate footer, not rate authority"
    as_of: "2026-10-28"
  - url: "https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls"
    title: "ITO published CT4 workbook: instructions, fields and declaration; current operational limit retained"
    as_of: "2026-10-28"
  - url: "https://www.gibraltar.gov.gi/contacts/income-tax-office-76"
    title: "ITO contact page: Corporate Tax Section, CT1/CT2 and general-query routes"
    as_of: "2026-10-28"
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gibraltar corporate tax and filing v0.19

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Who this applies to

### Scope

Prepare a corporate tax working paper for accounting periods wholly after 1 July 2024, checked in 2026. This draft covers income categories, expense adjustments, capital allowances, trade losses, cessation stock valuation, accounting periods, payments and filing controls. It includes UK treaty permanent-establishment and profit-attribution rules; Pillar Two, specialised exemptions and other treaty corridors remain outside the completed draft scope.

Earlier source reads and completed corporate reviews date from 22 October 2026. The 28 October continuation supplies a complete writer quote ledger, actual CT4 and published return-contact procedures, and the ordinary rented-premises/non-annual approved-fund rules. Current independent acceptance is pending; earlier completed reviews retain their exact scopes. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

### Company residence and the source of profits

Section 74 defines an ordinarily resident company by **management and control in Gibraltar**, or management and control exercised outside Gibraltar by persons ordinarily resident in Gibraltar. It adds a control rule for investment companies, including power through shares, votes or constitutional documents to secure that affairs follow the resident controller's wishes. “Investment company” here concerns a company whose income mainly falls outside trade, business or employment profits. Do not replace these tests with place of incorporation alone. Collect the decision-making history, directors' and controllers' residence, constitutional powers and actual conduct; no single meeting or registered address settles the factual analysis. [Section 74, company residence and investment-company definitions](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Residence and source answer different questions. Section 11(1) charges the specified Schedule 1 income accruing in or derived from Gibraltar. Section 11(2)'s additional charge on specified foreign income of ordinarily resident persons expressly excludes companies. That does not create an exemption for every foreign receipt of a company: apply the statutory source definition and the interest, royalty and movable-property deeming rules below. [Section 11(1)–(2); Schedule 1, Table C](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Under section 74, source is determined by the location of the activities giving rise to profits. The definition also deems those activities to take place in Gibraltar where the underlying income-producing activity requires licensing and regulation under Gibraltar law, or falls within the specified lawful passporting branch/permanent-establishment case. A foreign customer, overseas payment account or contract signature abroad is therefore not by itself a non-chargeability test. For example, a Gibraltar team supplying services to an overseas customer must analyse its profit-producing work rather than classify the invoice as exempt because the customer is abroad. [Section 74, definition of accrued in and derived from](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The licensing deeming rule has an express exception for a Gibraltar company's overseas branch or permanent establishment, to the extent of activities conducted outside Gibraltar. This disapplies that deeming limb for the stated activities; it is not a blanket exemption for all overseas receipts or proof that a foreign establishment exists. Keep the establishment evidence and attributable activities separate from Gibraltar work. [Section 74, same definition, paragraph (c)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For a non-ordinarily-resident company trading through a Gibraltar branch or agency, section 11(4) measures chargeable profits by trading income through or from it and, insofar as chargeable, property/right income connected with assets used or held by or for it. Treaty residence, permanent-establishment thresholds, dual-residence resolution and profit attribution need the applicable agreement and facts; this domestic-law section does not resolve them. [Section 11(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

## Rates, bands and thresholds

| Item | Amount or condition | Period | Official source |
|---|---|---|---|
| Ordinary company rate | 15% | Periods wholly after 1 July 2024 | [Rates Rules, rule 6(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf) |
| Utility / dominant-position abuse categories | 20%; apply the distinct statutory conditions | 2026 | [Rates Rules, rule 6(2)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf) |
| Inter-company interest exclusion | Less than £100,000 per annum; connected borrowers aggregated | 2026; shortened-period computation remains open | [Schedule 1, Table C, Class 1A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |
| First-year plant / computer deductions | £30,000 / £50,000; qualifying expenditure conditions apply | Ordinary 2026 periods | [Schedule 3, paragraph 8](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |
| Ordinary company pool rate | 15%; separate 20% taxpayer categories remain below | Twelve-month 2026 period | [Schedule 3, paragraph 9(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |
| Small residual pool | Less than £1,000; equality does not qualify | 2026 | [Schedule 3, paragraph 9(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |
| Tax-return audited-account threshold | At least £1,750,000 assessable income; shorter periods use monthly proportion | Twelve-month period; exact conditions below | [Income Tax Act, section 30(1)(b)–(cb)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |

### Charge and rates

Apply the source-of-profit analysis under section 11 and Schedule 1, not a blanket worldwide or tax-free-offshore assumption. The standard company rate is 15% from 1 July 2024. The higher rate is 20% for the statutory utility/dominant-position categories. Mixed activities require classification before rates are assigned. Rule 6(3) requires the Commissioner's opinion that the company has abused its dominant market position; market dominance alone is not the complete statutory condition. [Rates of Tax Rules, rule 6](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf). [ITO, Guidance Notes for Companies, August 2025, pp2–3](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Guidance%20Notes%20for%20Companies,%2008-2025.pdf); [Income Tax Act](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

## The base

### Interest, royalties and overseas movable-property income

Do not treat an overseas payer as sufficient evidence of non-chargeable income. Schedule 1 Table C Class 1A covers loan/advance interest between companies and deems it Gibraltar-source where the recipient company is registered in Gibraltar. The exclusion applies where interest from any one company is **less than £100,000 per annum**. For this threshold, interest from companies connected with each other under Schedule 4 paragraph 9 is aggregated. The rule does not require the borrower and lender themselves to be connected before inter-company interest can fall within Class 1A. [Schedule 1, Table C, Class 1A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The amount is a threshold, not a £100,000 deduction. On a twelve-month case with all other conditions satisfied, £99,999 falls below it; **£100,000 does not**. If two connected borrower companies owe £60,000 and £45,000, their £105,000 aggregate fails the less-than threshold: do not test each in isolation or tax only the £5,000 excess. These examples classify gross income before allowable expenses and other applicable provisions. For shortened periods or unusual accrual arrangements, resolve the “per annum” computation before using these examples. [Class 1A(a)–(b)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Interest already constituting a trading receipt under Schedule 3 paragraph 15 and taxed accordingly is excluded from the separate Class 1A charge. Reconcile the two provisions so that the same receipt is not counted twice. Do not infer a blanket interest exemption merely because Class 1A's threshold is not reached. [Class 1A(b)(ii)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For accounting periods **beginning on or after 1 February 2024**, paragraph 15 covers interest and similar amounts for the specified non-individual businesses: public money lending (including holding out as such), the specified deposit-taking funds/investments, permitted insurance business and permitted distributed-ledger storage/transmission of another's value. It deems the covered amounts trading income accruing in and derived from Gibraltar. Identify the activity and permission; the rule does not apply to every company merely because it earns interest. [Schedule 3, paragraph 15(1), (2), (6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

“Similar amounts” includes the specified lending-linked instruments and derivatives, discounts, and qualifying virtual-asset lending or proof-of-stake arrangements. Paragraph 15(1B) also addresses assets held for others and facilitation producing a share of value. Read these inclusions together with the paragraph 15(2) business conditions. They do not establish that every crypto receipt is taxed, or that a company outside paragraph 15 is exempt under all other provisions. Token valuation, timing, trading classification and permission analysis require separate work. [Paragraph 15(1A)–(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Paragraph 15(3) restricts the deduction of interest expense incurred to generate interest not taxable under subparagraph (2). Its interaction with income charged separately under Class 1A needs case-specific review; do not automatically deduct funding costs whenever inter-company interest crosses the threshold. Paragraphs 15(4)–(5) can attribute income back to a chargeable transferor after a connected-person transfer of income-producing assets, unless evidence satisfies the Commissioner that tax avoidance was not a main purpose. Paragraph 15 also applies subject to section 18 on partnerships. [Paragraph 15(3)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Royalties:** Table C Class 3A covers royalties received or receivable by a company and deems them Gibraltar-source where the recipient is registered in Gibraltar. Class 3A contains no equivalent £100,000 interest threshold. Obtain the licence, rights granted, accrual calculation and recipient registration evidence; treaty relief and receipt classification must be assessed separately. [Schedule 1, Table C, Class 3A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Overseas movable-property rents:** Class 3B separately covers non-trading rental income from movable property outside Gibraltar received or receivable by a company, deeming it Gibraltar-source when that company is registered in Gibraltar. This is not a rule for every overseas real-estate receipt. Document the asset, location and trading/non-trading classification before applying it. [Schedule 1, Table C, Class 3B](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### From accounting profit to deductible expenses

Schedule 3 paragraph 1 starts with profits under the permitted accounting standards, subject to statutory adjustments, and excludes capital gains and capital losses from that measure. Establish whether a receipt is genuinely capital; a ledger label does not settle a trading-property or other classification. Pre-trading expenditure incurred with a view to carrying on the business is treated as incurred on its first trading day for the relevant profit or capital-allowance computation. That timing rule does not make every start-up expense deductible. [Schedule 3, paragraph 1](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The general expense test is money wholly and exclusively expended to produce the trade's income, subject to the specified exclusions. Reconcile the ledger to a tax-adjustment schedule and retain the invoice, business purpose, period and legal treatment. Key exclusions include accounting depreciation, capital withdrawals and improvements, recoverable insurance/indemnity amounts, tax under this Act or tax eligible for section 37 relief, and contributions to unapproved employee pension/provident funds. Assess statutory capital allowances separately instead of deducting book depreciation. [Paragraph 2(1)(d)–(f), (i), (k), (m)–(n)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Interest needs its own checks: paragraph 2(1)(j) excludes interest to a non-resident to the extent it exceeds a reasonable commercial rate, while paragraph 2(1)(l) restricts borrowing outside the stated income-producing business or acquisition purposes. Apply the [connected-party interest restrictions](gi-connected-party-pricing-and-interest.md) as well; passing one provision does not establish deductibility under all others. [Paragraph 2(1)(j), (l)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Where income is partly chargeable and partly non-chargeable, paragraph 2(2)(a) requires pro-rata apportionment of deductions between them. For a simple established allocation of 75% to chargeable income, £12,000 of otherwise allowable shared expense gives £9,000 against chargeable income. This example assumes the income classification and allocation basis have been verified; do not use turnover mechanically where the facts require a different analysis. [Paragraph 2(2)(a)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For the defined apportioned branch head-office expenses, paragraph 2(1)(p) excludes the amount exceeding **5% of the Gibraltar branch's gross income**. If the relevant expense is £40,000 and branch gross income is £500,000, the ceiling is £25,000 and £15,000 is disallowed under that restriction, before other conditions. This is not a deduction of 5% without expenditure and is separate from connected-company expense restrictions. [Paragraph 2(1)(p)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

#### Rented domestic premises used to produce income

Where Schedule 3 paragraph 2(1)(a) applies to a dwelling-house or domestic office, identify the part used to produce the trade or profession’s income. The deduction for those premises must not exceed **two-thirds of the rent bona fide paid**, unless the greater-sum exception is justified on the particular circumstances specified in the paragraph. The cap is not an automatic deduction: an unsupported or private amount does not qualify merely because it is below two-thirds. This rule does not create a deduction for imputed rent where no rent was paid. [Schedule 3, paragraph 2(1)(a), printed page 159](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Conditional illustration:** assume £18,000 of relevant bona fide rent was paid and a separate supported analysis establishes £9,000 as the income-producing rent amount. The ordinary two-thirds cap is £12,000, so the amount within both those tests is £9,000. If the otherwise eligible amount instead is £14,400 and no greater-sum exception is relied on, the cap leaves £12,000. These are assumed inputs, not a prescribed business-use percentage, a final tax assessment or a conclusion about the recipient’s tax or employee benefits. The [supplementary rent control](../../research/gibraltar-2026/corporate-completion-2026-10-28/rent-control.md) checks only that arithmetic.

#### Non-annual employer contributions to an approved fund

Schedule 3 paragraph 4 addresses an employer contribution to an approved employee provident, pension or other fund **which is not an ordinary annual contribution**. It is deducted in the year paid or spread over the period the Commissioner decides is proper. Do not invent a default spreading period or replace the paid-year condition with an unsupported book accrual. Retain the fund approval, contribution character, payment evidence and any Commissioner decision supporting the spreading treatment. This rule does not itself establish an employee exemption or another fund’s approval. [Schedule 3, paragraphs 2(1)(n) and 4, printed pages 161 and 163](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Bad debts, entertainment and gifts

Paragraph 2(1)(g) permits the specified bad debts, qualifying released debts and doubtful debts to the extent estimated bad for the period. Retain debtor-specific support, the recoverable amount and any relevant arrangement or compromise. The provision does not establish that a general accounting provision qualifies in full. Amounts recovered on previously deducted debts and the specified sale, assignment or capitalisation proceeds must be brought into profits under paragraph 3; avoid both omission and double counting if already recognised in the accounts. [Paragraphs 2(1)(g), 3(a)–(c)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Business entertainment, including hospitality and incidental costs, is generally disallowed under paragraph 2(1)(o). Bona fide staff provision is outside its entertainment definition unless incidental to provision for others. The provision also contains an ordinary-course supplier exception and a separate client-entertainment exception requiring Gazette guidelines and the Commissioner's satisfaction that the claimant's benefit is merely incidental. The ITO interpretation and evidence requirements are summarised below; the specific Gazette publication has not been identified, so its formal publication requirement remains unverified. Do not approve client hospitality merely because a client attended. The latter exception also has a statutory exclusion following refused claims in three of the preceding ten years, lasting the specified five-year period. [Paragraph 2(1)(o)(i)–(ii), (iv)–(vi)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The ITO's published entertainment guidance covers existing and prospective clients and business introducers, with acceptance depending on the facts and the Commissioner's satisfaction. It calls for documentary support and a detailed record identifying the expense's purpose and staff involved; insufficient evidence leads to refusal. Prepare an event record linking the invoice to attendees, business purpose and the claimant's incidental benefit. Those practical fields support the statutory test; they do not guarantee approval. [ITO entertainment guidance, printed pages 1 and 3](https://www.gibraltar.gov.gi/new/sites/default/files/1/01/guidance_on_business_entertainment_expenditure.pdf).

The guidance also says promotional branding must appear on the **gift itself**, not only its wrapping. For staff events, it suggests asking whether the employer would have funded the event if only employees attended when assessing incidental entertainment. Treat this as an administrative aid, not a substitute for the Act, and check employee benefit taxation separately. The PDF remains linked from the [ITO downloads page](https://www.gibraltar.gov.gi/income-tax-office/downloads-ito), but contains no verified current revision date. [ITO guidance, printed pages 3–4](https://www.gibraltar.gov.gi/new/sites/default/files/1/01/guidance_on_business_entertainment_expenditure.pdf).

The gift restriction has an exception for an article carrying a conspicuous advertisement for the donor, excluding food, drink, tobacco and goods-exchange tokens/vouchers, where qualifying articles to the **same recipient in the period cost no more than £100 in total**. Two eligible branded articles costing £60 and £40 meet that cost boundary; adding another £1 article takes the total outside this exception. It is not an automatic £100 deduction from an over-limit gift total. The general business-purpose test still applies. [Paragraph 2(1)(o)(iii)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Example tax bridge: start with £100,000 accounting profit after £10,000 book depreciation and £2,000 client entertainment that does not qualify for an exception. Add back both amounts and deduct £8,000 of independently established capital allowances: **£104,000** before losses and other adjustments. This example assumes no other differences; it does not turn a partial reconciliation into a complete tax computation. [Paragraph 2(1)(k), (o) and Part II](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Capital allowances: equipment purchases and pools

For ordinary 2026 periods, Schedule 3 paragraph 8 provides first-year deductions for qualifying expenditure up to **£30,000 for plant and machinery** and **£50,000 for computer equipment**. These are expenditure deductions, not tax credits. The expenditure must meet the wholly-and-exclusively income-producing condition and the ownership requirement, subject to the specified user and eventual-ownership contract provisions. Keep invoice, acquisition date, business purpose and ownership/contract evidence. Do not assume a separate cap for each invoice. The enhanced amounts for periods ending between 1 July 2021 and 30 June 2023 are historical and do not apply simply because an asset is still in use in 2026. [Schedule 3, paragraph 8](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Plant and machinery includes fixtures and fittings. Ordinary passenger cars are excluded from that paragraph's definition unless they meet the stated goods-carrying, unsuitable-for-private-use or public-hire/carriage exceptions. Computer equipment includes peripherals and software. Motor vehicles are separately addressed in the pool provisions, so exclusion from the first-year plant definition does not itself settle every vehicle allowance. Mixed-use vehicles and the special electric-vehicle provisions need separate review; this Guide does not treat all cars or all software expenditure as automatically qualifying. [Paragraphs 8(1)(c), 8(2)(c), 9(2)(c), 9(11)–(11B)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Build the paragraph 9 pool from qualifying current additions **after subtracting first-year deductions**, plus the eligible brought-forward pool, less the statutory disposal values. Do not deduct the same cost both in full and again through the pool. For a twelve-month period, the ordinary company pool rate is **15%**; paragraph 9(3)(a) instead provides **20%** for non-companies and companies chargeable under Schedule 6. The temporary 25%/30% rates apply only to the specified periods ending from 1 July 2021 to 30 June 2023. Identify the taxpayer category before choosing the rate. [Paragraph 9(1)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Example: assume an ordinary company has a twelve-month 2026 period, no opening pool, no disposals and £40,000 of qualifying plant expenditure. A £30,000 first-year deduction leaves £10,000 in the pool. The 15% pool allowance is £1,500, giving total deductions of £31,500 and a £8,500 closing pool. For £60,000 of qualifying computer equipment on the same assumptions, the £50,000 first-year deduction and £1,500 pool allowance leave £8,500. These are separate alternative examples, not a combined claim. [Paragraphs 8–9](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For a period shorter than twelve months, paragraph 9(4) time-apportions the **pool allowance**. A six-month period with an otherwise eligible £10,000 pool therefore gives £10,000 × 15% × 6/12 = £750. This does not assert a corresponding reduction to the paragraph 8 first-year limits. Paragraph 9(7) allows the full residual pool if it is **less than £1,000**. On a normal twelve-month calculation, £999 qualifies for full deduction; exactly £1,000 does not qualify under that rule and instead gives £150 at the ordinary company pool rate, assuming no other provision applies. [Paragraph 9(4), (7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Disposals and special capital-allowance cases

Paragraph 9(2)(e) covers assets sold, ceasing to exist, moved wholly outside the trade, or affected by permanent trade discontinuance. Its value rule uses sale proceeds; where these are not at arm's length, it substitutes **net book value at disposal**. Do not silently replace that statutory wording with market value or tax written-down value. For a continuing ordinary company with £20,000 of pool/additions before disposal and £5,000 of established arm's-length proceeds, the resulting £15,000 pool gives a £2,250 allowance over twelve months, subject to the other rules. [Paragraph 9(2)(e), (3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Do not apply that simple example to every exit. Paragraph 9(5) provides a full remaining-pool allowance on permanent discontinuance; paragraph 9(6) contains a separate restriction where the qualifying-expenditure balance is below disposed-asset value; and paragraph 9(12) excludes assets purchased and disposed of in the same period from subparagraph (2). No automatic balancing charge, same-period deduction or value for destruction/private transfer is established by this Guide. Obtain a reviewed computation for those cases. [Paragraph 9(5)–(6), (12)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Paragraph 14A contains a separate start-up provision referring to capital allowances against first-year tax liability, with no duplicate claim and exclusions where the Commissioner identifies the specified connected prior business or artificial arrangement. Its application and interaction with ordinary deductions require separate review; do not turn the equipment deductions above into a pound-for-pound credit. Building rules are addressed below; extended accounting periods and special assets are outside these equipment examples. [Paragraphs 8(5), 9(8), 14–14A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Buildings: separate eligibility and historical schemes

Schedule 3 paragraph 6 permits the Commissioner to allow **4% per annum of cost excluding land** for wear and tear of a hotel, mill, factory or other qualifying similar premises used in the owner's trade, business, profession or vocation. “Mill, factory and other similar premises” has a specific manufacturing/process and powered-machinery definition in paragraph 6(6). An ordinary office does not qualify merely because it is a business asset. If the trader is not the owner, paragraph 6(2) permits allocation to either or apportionment between them; do not give both parties a full deduction. [Paragraph 6(1)–(3), (6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Example: assume qualifying premises cost £900,000, supported evidence allocates £250,000 to land, and the full-year deduction is allowed. The building cost is £650,000 and 4% gives **£26,000**. Retain the land allocation and the allowance history. Paragraph 6(4) prohibits a deduction exceeding written-down value: if only £20,000 remains, the £26,000 claim is not permitted. Do not automatically substitute a final £20,000 deduction without confirming the applicable treatment. [Paragraph 6(1), (4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For disposal of an industrial building, paragraph 6(5) provides a deduction for written-down value less amounts realised or expected on sale or recoverable under insurance/indemnity, and no deduction if recoveries exceed written-down value. With established written-down value of £100,000 and total qualifying recoveries of £70,000, the difference is **£30,000**; recoveries of £110,000 do not produce a deduction under that paragraph. This is not a conclusion about all other tax consequences of disposal. [Paragraph 6(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The broader **1% real-property allowance** in paragraph 6A is expressly limited to accounting periods or assessment years ending **1 July 2021 to 30 June 2023** and excludes a person qualifying under paragraph 6. Do not apply it to a 2026 period because the provision remains printed in the consolidated Act. Its disposal and historical-claim implications need separate review. [Paragraph 6A(1), (5)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Two construction schemes also have closed commencement windows:

| Provision | Commissioner-approved qualifying project | Construction commencement window |
|---|---|---|
| Paragraph 12A | Wholly and exclusively offices for business use | 1 July 2013 to 31 March 2015 |
| Paragraph 12B | High-value accommodation | 1 July 2014 to 31 December 2015 |

Both provide 30% of qualifying construction costs in the first period following completion and 10% in each of the second through eighth periods. A completion certificate must accompany the claim. The developer can elect the deduction for itself, the occupier, or a 50:50 split. Costs exclude land but include the specified planning/design, foundations/services, demolition and installed-building fittings. A 2026 construction start does not satisfy either window; a qualifying historical start needs its completion date and claim history checked rather than being rejected solely because the claim is later. [Paragraphs 12A–12B](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For £1,000,000 of established qualifying construction costs, the statutory sequence is £300,000 then seven deductions of £100,000, totalling £1,000,000. Under a valid 50:50 election, each claimant's first-period share is £150,000. Paragraphs 12A(6) and 12B(6) expressly allow these deductions in addition to other applicable relief for the same expenditure; retain separate legal grounds rather than extending that exception to ordinary equipment claims. Project approval, elections, implementing rules and any unresolved definition of high-value accommodation require verification for a live claim. [Paragraphs 12A(2)–(8), 12B(2)–(8)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Trading stock when a trade ends

Section 21 supplies a separate valuation rule when a trade or business is discontinued. Use the **amount realised or value of consideration** if the stock is sold/transferred for valuable consideration to a person carrying on, or intending to carry on, a trade or business in Gibraltar **and** its cost can be deducted by that purchaser in computing the relevant assessable income/profits. Both conditions matter. A purchaser's Gibraltar address alone does not establish them. [Section 21(1)(a)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For other stock, use what it would have realised on an **open-market sale at discontinuance**. Do not automatically use historic cost, accounting carrying value, zero because it was given away, or the actual price of a transaction that does not meet paragraph (a). Establish the cessation date and a supportable valuation as at that date. This rule determines the stock value for the cessation profit computation; it does not itself quantify the whole taxable profit. [Section 21(1)(b)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The statutory stock definition extends beyond finished retail goods. It includes real or personal property ordinarily sold in the trade, items that would be sold when mature or complete, and materials used in manufacture, preparation or construction. It also includes services, articles or materials treated as professional work in progress. Identify the business's actual stock/WIP rather than applying the rule only to warehouse goods. [Section 21(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Example 1: qualifying purchaser.** Assume a discontinued trade transfers its stock for £25,000 cash and non-cash consideration independently valued at £5,000. The buyer intends to carry on the relevant Gibraltar trade and the stock cost is deductible in the buyer's taxable computation. Section 21(1)(a)'s value is **£30,000**. A £40,000 open-market estimate is not substituted merely because it is higher, though other applicable anti-avoidance/connected-party rules must still be checked. These facts and consideration values are assumed, not statutory safe harbours.

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.

**Example 2: other stock.** Assume the paragraph (a) buyer/deductibility conditions are not met. Supported open-market values at cessation are £18,000 for finished goods and £12,000 for qualifying unfinished stock. The section 21(1)(b) total is **£30,000**, even if the actual disposal proceeds are £20,000. The £10,000 difference is a valuation reconciliation, not automatically the final taxable gain or tax bill; reconcile it to the accounts without counting a receipt twice.

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.

Recommended working papers: cessation date and stock/WIP inventory; buyer's trade and deductible-cost evidence where paragraph (a) is used; contract and cash/non-cash consideration; market valuation where paragraph (b) applies; and the bridge to the cessation accounts. Keep stock valuation separate from capital-allowance disposals and transferred-loss eligibility. Interactions with connected-party provisions, actual valuation disputes and return-field mechanics remain case-specific review work. [Sections 20A–21; Schedule 3 Part II](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Trade losses: eligibility and continuity

Section 20(1) provides for losses to be set against assessable profits or gains of subsequent periods, subject to its restrictions. Establish the **tax loss**, rather than copying an accounting deficit. A loss is excluded if the corresponding profit would not have been taxable under the Act, and the same loss cannot be used twice. At the claim date, the loss must relate to a period for which an assessment could then be made if the loss had been a profit. Do not treat an old ledger balance as proof that a loss remains claimable. [Section 20(1), (2), (4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Maintain a roll-forward by originating period: established tax loss, prior utilisation, current claim and balance. For a company outside the designated-person restriction, assume £80,000 of eligible unused losses and £50,000 of otherwise assessable profits, with all continuity and claim conditions satisfied. Set off £50,000, leaving zero on that profit component and £30,000 of unused losses. A separate £10,000 loss from an activity whose profits would not be taxable is not added to the eligible pool. These assumptions must be proved in an actual claim. [Section 20(1)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

A company loses the specified relief where, within any three-year period, there is **both** a change of ownership and a major change in the nature or conduct of its trade. The trade change can precede, follow or coincide with the ownership change. The restriction concerns losses in a basis period beginning before the ownership change set against profits of a basis period ending after it. Ownership means a change in effective control through direct or indirect voting-share ownership together with changed beneficial ownership. Record the control history and changes in customers, activities and operating model; the last items are evidence prompts, not statutory tests of a major change. [Section 20(3), (5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Designated persons: 50% loss limit and exceptions

For accounting periods ending **on or after 31 July 2024**, section 20(6) limits a designated person's loss set-off to **50% of the Schedule 3 measure of profits or gains**. Section 20(7) covers persons carrying on regulated activities within section 5 of the Financial Services Act 2019, activities licensable under section 3(1) of the Gambling Act, and their connected persons. A company outside the regulated industry can therefore still fall within the rule through connection. Check the statutory activity definitions and [connected-person rules](gi-connected-party-pricing-and-interest.md) before classifying it. [Section 20(6)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Example: assume a designated company has a Schedule 3 profit measure of £100,000 and £80,000 of eligible carried-forward losses, all outside the protected periods below, with no insolvency exception. The cap is £50,000; set off £50,000, leaving £50,000 of profits before other applicable adjustments and £30,000 of unused losses. At exactly £50,000 of eligible losses the entire pool fits the cap. This calculation does not establish the company's status or eligibility. [Section 20(6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.


The restriction does not apply to losses incurred in periods ending **from 1 July 2021 through 30 June 2023**. Designated persons must use these losses before losses from other periods. Identify the loss period's **end date**: a period ending 30 June 2023 falls within the window; one ending 1 July 2023 does not. Section 20(8) separately excludes the specified designated companies subject to insolvency proceedings. Neither exception removes the other loss eligibility conditions. [Section 20(8)–(10)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Mixed protected and restricted losses: statutory working-paper interpretation

The complete interpretation, assumptions and executable mixed-pool example are preserved together in section 7 below.

### Losses transferred in a group restructure

Section 20A permits corresponding unrelieved trade losses to be available against the recipient entity's future profits when the trade or business transfers to a separate entity as part of a group restructure. The provision includes reorganisations, takeovers, mergers and sales of a trade or business. It is not a general permission to pool losses between companies merely because they share an owner. The transferred business must have been taxable had it made profits. [Section 20A(1), (2), (6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Only the proportion attributable to the transferred part is available, measured by **income attributable to each share of the trade**. For example, if eligible unrelieved losses are £100,000 and a supported income-based allocation attributes 40% to the transferred part, the potential transferred pool is £40,000, subject to the remaining conditions. A 40% asset-value share alone does not establish that result. [Section 20A(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

No set-off is given under section 20A(1) if, within the specified three-year period from transfer, there is both a change in ultimate company ownership and a major change in the nature or conduct of the trade. The effective-control and beneficial-ownership definition appears in subsection (5). Retain the transfer agreement, income allocation, loss history and post-transfer ownership/trade monitoring. Interaction with section 20 restrictions, evidence required for a claim and any advance clearance needs case-specific review. [Section 20A(3)–(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Computation and examples

1. Reconcile accounts to a profit bridge: accounting profit, non-chargeable items, disallowances, capital allowances and separately supported reliefs.
2. Map each adjustment to the Act and retain the ledger transaction behind it. Unsupported deductions remain review questions.
3. Separate ordinary and higher-rate profit streams. Check connected-party dealings and interest restrictions independently.
4. Compute current liability, subtract period-matched payments and reconcile the residual to CT1.
5. Keep company-registry accounts, corporation-tax filing and payroll reporting as separate calendar events.



The instalment example in section 4 also recomputes under its stated, verified basis-liability assumptions:

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.

## Deadlines and filing

### Establish the tax accounting periods

Section 16 starts a company's tax accounting period when it is first registered in Gibraltar or when the preceding accounting period ends. It normally ends at the earlier of twelve months from its beginning and the company's accounting date. Do not automatically use trading commencement as the first tax-period start, or assume a long set of financial statements creates one equally long tax period. Retain the registration evidence, accounting-date history and prior assessments. [Section 16(1)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For example, a company first registered on 1 July 2025 with accounts to 31 December 2025 has an initial six-month period on those assumptions. Its normal nine-month return/payment rule points to 30 September 2026. Keep the six-month period length when applying provisions that expressly time-apportion thresholds or allowances; do not halve every statutory amount merely because the period is short. [Sections 16(2)–(3), 29 and 39(1)(b)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Winding up ends an accounting period and begins another at its commencement, subject to section 16(1)–(3). Thereafter periods end at twelve-month intervals, with the last ending on completion of winding up. Cessation of sales is not the same event as commencement or completion of winding up. Where period boundaries are uncertain, subsection (5) permits a Commissioner assessment for a period no longer than twelve months, subject to revision on further facts or an appeal revealing the proper periods. [Section 16(4)–(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For accounts exceeding twelve months, subsection (6) requires time apportionment on the basis that profits accrued evenly. Its wording identifies an initial period ending on the company's accounting date and a subsequent period comprising the remaining twelve months. **Do not substitute a standard first-twelve-months-plus-remainder convention without confirming the applicable boundaries.** Obtain the determined periods and reconcile allocated profits to the accounts. If a confirmed allocation divides £180,000 evenly over eighteen months into six- and twelve-month periods, the amounts are £60,000 and £120,000; this arithmetic does not determine which dates apply. Subsection (7) gives the Commissioner discretion over profit allocation if an accounting-date delay beyond twelve months was effected to reduce tax. [Section 16(6)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Filing requirements

A company must file if it is **registered in Gibraltar or has assessable income** under the Act. A Gibraltar branch with assessable income files for the branch's income. The registration limb means that zero assessable income is not itself a filing exemption for a registered company. The obligation continues even if the Commissioner has not sent a return form. [Sections 29(1)–(2), 30(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Section 29(3) gives the normal deadline of nine months after the month containing the accounting-period end. **For an extended accounting period**, section 29(4) instead expressly measures the return deadline from the end of the month containing the extended period's end. Thus an extended set of accounts ending 30 June 2026 points to 31 March 2027 for that return rule. Keep the component tax computations and payment obligations separately checked; this return provision does not by itself postpone instalments or establish every payment deadline. [Section 29(3)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Section 30 requires the prescribed form and specified accompanying information, plus payment in accordance with the return computation, subject to its stated exceptions. For the below-threshold independent-report route, accounts must be signed for the board by two directors, or the sole director if there is only one. An unsigned accounts file, omitted required report or omitted attachment cannot be treated as a complete filing merely because a CT1 was submitted. Keep the signed submission set and proof of receipt; current submission-channel acceptance must be confirmed before filing. [Section 30(1)(a), (ca), (d)–(g)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For an ordinary accounting period, the complete CT1 and balancing payment are due nine months after the end of the month containing the accounting-period end. The return includes accounts, a tax computation where assessable income exists, and a PAYE reconciliation where required for a non-June year-end. Instalments are due on 28 February and 30 September; allocate them to the correct accounting period using Schedule 10. Ceasing trade does not itself end returns. [ITO corporate guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

For a twelve-month accounting period, current section 30(1)(b) requires audited accounts where assessable income is **at least £1,750,000**; paragraph (bb) requires accounts and an independent accountant's report below that amount. Shorter periods use the monthly proportion: six months gives £875,000, with equality on the audited side. The report issuer must satisfy the approval, independence and practising-certificate requirements in paragraph (cb). This tax-return attachment rule does not itself establish company-law audit exemption. [Income Tax Act, section 30, consolidation dated 23 March 2026](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf); [company accounts and reporting Guide](gi-company-accounts-and-reporting.md).

### Current published CT1/CT2 contact route

The ITO’s current contact page lists **corporate.returns@gibraltar.gov.gi** specifically for company tax returns **CT1 and CT2**, separately from its corporate-query and certificate contacts. Use the complete signed return/attachment set described above and retain submission and receipt evidence. The page identifies a published route; this Guide has not tested a live filing, individual attachment acceptance or an alternative portal. The CT1/CT2 label is not authority to send CT4 to that mailbox. [ITO contact page, Corporate Tax Section](https://www.gibraltar.gov.gi/contacts/income-tax-office-76).

### Payments on account and balancing payment

Keep three fields separate: the **basis period** used to calculate an instalment, the **payment due date**, and the **accounting period receiving the credit**. Section 39(4) requires payments by **28 February and 30 September**. Each is 50% of the tax payable for the relevant basis period determined using Schedule 10. The basis period is not automatically the most recently completed accounts: its due-and-payable date must precede the first instalment date as prescribed by the table. [Section 39(4)(a)–(d) and Schedule 10](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The ITO publishes a 2022–2033 allocation table, but its footer still states **10%**. That is not the current standard company rate. Do not use that footer as rate authority or silently apply it to a 2026 computation. Check the basis liability, applicable rate provisions and any period spanning a rate change against the Act and the company's tax record. The table also has irregular month-end dates in certain rows; resolve any affected row before relying on it. [ITO allocation table](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Schedule%2010%20Table%20-%20Payments%20on%20Account%20-%202022%20to%202033.pdf); [current company rate guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

For a verified basis-period liability of **£20,000**, with no reduction or adjustment required, each instalment is **£10,000**. If the final tax for the credited accounting period is £26,000, the balance is £6,000. If final tax is £18,000, the £2,000 excess is repayable under section 39(4)(e); obtain the account reconciliation rather than automatically crediting another period. The normal company balance date is nine months after the end of the month containing the period end. Section 39(9) separately gives **60 days after the assessment date** for an assessment under section 33(1)(b); do not apply the normal balance date to every additional assessment. [Section 39(1)(b), (4)(e), (9)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For a changed accounting date, section 39(4)(f) retains the previous-date basis until an accounting period under the Act has been made up to the new date. An extended basis period within paragraph (g) is apportioned to an equivalent twelve months; a basis period shorter than twelve months is grossed up by time under paragraph (h). Example: a six-month basis liability of £6,000 annualises to £12,000, giving £6,000 per 50% instalment, before any other applicable adjustment. Keep the original period, time calculation and statutory basis in the working paper. [Section 39(4)(f)–(h)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Applying to reduce instalments

If required payments on account will exceed the current period's liability, section 39(5) permits an application for full or partial discharge. The Commissioner decides whether to discharge or reduce the obligation under subsection (6); an internal forecast is not itself that decision. The ITO identifies **Form CT4** and says it is not valid for an accounting period that has already ended. Prepare the expected tax computation and supporting forecast, retain the application and decision, and update the payment schedule. The published form’s fields, calculation and postal instructions are set out below. A particular claim’s receipt and the Commissioner’s decision require their own evidence. [Section 39(5)–(6)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf); [ITO CT4 guidance and download](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

Payments on account are themselves subject to late-payment surcharge. If an amount omitted following a discharge application is later found payable, section 39(7) treats the relevant shortfall as due on the original instalment date for surcharge purposes. Do not describe an approved reduction as protection against surcharge if the estimate proves insufficient. [Section 39(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Complete the published CT4 working paper

Use the workbook currently linked from the ITO corporate page, and prepare the claim before the payment-on-account due date. The ITO says CT4 is invalid for a period already ended. The workbook asks for the taxpayer reference, incorporation number, company name, contact telephone and registered-office address; identify the accounting period and select either a lower-liability claim or a no-tax-due claim. Record the stated reason: lower trading profits, lower other significant income, more tax deducted at source, more non-chargeable income, or a specified other reason. A box describing non-chargeable income is not a statutory exemption: establish its current legal treatment separately. [Published CT4, company information and claim fields, rows 11–38 and 49–97](https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls); [current ITO CT4 guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

Estimate the **whole period’s expected corporation-tax liability** reasonably from the information now available. Enter **half that estimate as each reduced payment on account**, not half the reduction from the previous liability. Retain the forecast computation and its assumptions. Section 39(6) still requires the Commissioner’s discharge/reduction decision; completion or delivery of the form does not itself grant the reduction. [CT4 instructions, rows 30–32 and 94–102](https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls); [section 39(5)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Conditional forecast illustration:** assume the verified original basis liability is £24,000, giving two £12,000 payments before reduction, and the properly computed current-period forecast is £10,000. CT4’s requested amount is **£5,000 per payment**, totalling £10,000; the aggregate proposed reduction is £14,000. If the Commissioner grants those amounts and the final period liability is later £14,000, £4,000 remains to reconcile before any surcharge calculation. This does not establish the Schedule 10 allocation, approval, original due dates or surcharge allocation. The [supplementary controls](../../research/gibraltar-2026/corporate-completion-2026-10-28/ct4-controls.md) recompute these assumed amounts, including a zero-estimate request; a zero estimate is not an automatic discharge.

The declaration requires signature, date, signatory name and designation. The form says a photocopied signature is unacceptable; except where a liquidator or administrator is appointed, the signer must be authorised for the company. It also calls for an adviser/representative’s details when signing for the company. Preserve the signed claim, evidence of authority and actual decision. [CT4 declaration, rows 102–118](https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls).

**Published submission instructions:** the workbook currently linked by the ITO instructs postal delivery to the Income Tax Office at St. Jago’s Stone Block, 331 Main Street, Gibraltar. Its file metadata records a March 2015 save date and it names F C Carreras as Commissioner; the current ITO page nevertheless expressly links this form for reduction claims. An old file-save date is not a stated legal expiry. Follow the published instructions, retain delivery/receipt evidence and obtain the actual reduction decision; this Guide does not claim a live filing was tested or a particular claim accepted. The ITO contact page lists **corporate.enquiries@gibraltar.gov.gi** for general corporate queries; it does not label that address a CT4 filing channel. Do not substitute it for the workbook’s route or treat a query as an accepted claim. [Published CT4 instructions, row 36](https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls); [ITO Corporate Tax Section](https://www.gibraltar.gov.gi/contacts/income-tax-office-76).

## Penalties and interest

### Failure and boundary checks

Section 64 charges **10% of unpaid tax on the day immediately after its due date**. If tax and that surcharge remain unpaid within 90 days from when the first surcharge becomes payable, a further **20% of the tax and surcharge still unpaid** becomes due. A fully unpaid £1,000 becomes £1,100, then £1,320. If the confirmed combined balance at the second trigger is £600 after intervening payments, the additional surcharge is £120, not £220; reconcile actual allocations before calculating it. These are payment surcharges, separate from return penalties. An appeal or collection postponement does not automatically remove them: section 36(10) retains the original due date for ultimately payable tax. [Sections 36(10), 39(7), 64](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf); [assessment appeals Guide](gi-income-tax-assessment-appeals.md).

For current company return failures, section 65(3) provides these **additional** penalties, using Schedule 9 Companies Act size classification:

| Company classification | Initial failure | Continuing after three months from filing date | Continuing after six months from filing date | Total if all three arise |
|---|---:|---:|---:|---:|
| Micro or small | £100 | £450 | £750 | £1,300 |
| Medium | £750 | £1,250 | £2,000 | £4,000 |
| Large | £1,500 | £3,500 | £5,000 | £10,000 |

The later amounts are added, not substituted. Establish the classification using the [accounts and reporting Guide](gi-company-accounts-and-reporting.md) and Schedule 9; do not classify size solely by tax payable. The ITO states that this company penalty schedule applies from **1 January 2025**. Historical defaults need the applicable earlier provisions. Section 65(4) gives the Commissioner power to set aside penalties where a reasonable excuse existed throughout the statutory default period; relief is not automatic. Keep evidence covering the whole period, not just the filing day. [Section 65(3)–(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf); [ITO filing-penalty guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate).

**Open scope:** remaining deductibility rules, building-claim procedures and special-case capital allowances, administrative confirmation of the mixed-pool loss interpretation and restructuring interactions, connected-party adjustments, minimum tax, all filing exemptions, and registry reporting must be completed before calling corporate coverage comprehensive.

## Cross-border points

### UK treaty: permanent establishments and business profits

Apply this section only after establishing entitlement under the UK–Gibraltar agreement, its effective period and Article 4 residence. For dual-resident companies, authority agreement is required for relief except to the extent authorities otherwise agree; incorporation alone is not the treaty tie-breaker. See [UK treaty entitlement](gi-uk-investment-income-treaty.md). Article 7(1) generally allocates enterprise profits exclusively to its territory unless it conducts business through a permanent establishment in the other territory, which can then tax attributable profits. Items separately dealt with elsewhere in the agreement retain their own rules under Article 7(4); absence of a PE is not a universal exemption for property income or investment payments. [Articles 4 and 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force).

### Fixed places and projects

Article 5(1) defines a PE as a fixed business location through which the enterprise conducts all or part of its business. Paragraph (2) lists management places, branches, offices, factories, workshops and natural-resource extraction locations. Paragraph (3) sets a **more-than-twelve-month** duration for a building site or construction/installation project. Exactly twelve months does not pass that project-duration limb. It is not a twelve-month grace period for every office, agent or other business activity. Verify project start, completion, interruptions and any aggregation issue before drawing a conclusion; the text alone does not settle every project-timing fact. [Article 5(1)–(3)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

### Activity exclusions and combined operations

Article 5(4) contains specific exclusions for facilities/stock used solely for storage, display or delivery of the enterprise's goods, stock solely for processing by another enterprise, and fixed places solely for purchasing goods or collecting information. Its separate residual-activity exclusion requires preparatory or auxiliary character; a combination of listed activities must be preparatory or auxiliary overall. Do not rewrite these different limbs into a single assumed test. Establish what the location actually does. [Article 5(4)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

Paragraph (5) withdraws paragraph (4)'s exclusion where the same or a closely related enterprise operates at that or another place in the same territory, the activities are complementary parts of a cohesive business operation, and either the relevant place is a PE or the combined activities are not preparatory or auxiliary. A separately incorporated warehouse and sales operation therefore require a combined factual analysis, not automatic exemption merely because one location stores goods. [Article 5(5)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

For this rule, paragraph (6) includes factual control or common control, and in any event specified **more-than-50%** direct/indirect beneficial ownership. For companies it refers to aggregate vote and share value or beneficial equity interest. Exactly 50% does not trigger that numerical route, but factual control can still establish close relationship. The test is not the same as a universal 51% share-count requirement. [Article 5(6)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

**Ownership example:** assume one equal-right class, no indirect holdings and 1,000 total shares. Holdings of 500 give 50%; 510 give 51%. The second passes the stated numerical limb; the first still needs the factual-control inquiry. Even established close relationship does not itself prove the remaining paragraph (5) conditions or a PE.

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.

### Contracting agents and subsidiaries

Under Article 5(7), a person acting for the enterprise who has and habitually exercises authority to conclude contracts on its behalf can create a deemed PE, subject to the independent-agent and limited-activity exceptions in the text. Examine actual authority and conduct; a job title or unsigned internal policy is not conclusive. Paragraph (8) protects an independent broker, commission agent or other independent agent acting in the ordinary course of its business. Paragraph (9) says control of one company by another does not **of itself** make either a PE of the other. It does not disapply the fixed-place, agency or combined-operation tests. [Article 5(7)–(9)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment).

### Attribute profits rather than taxing all sales

Article 7(2) uses a hypothetical separate and independent enterprise undertaking comparable activities under comparable conditions. Consider functions, assets and risks through the PE and elsewhere, including internal dealings. Do not allocate all customer revenue to the PE merely because customers are located there, or select a profit percentage without evidence. Keep a reconciled functional analysis and accounts supporting revenue, expense and internal-dealing allocations. Article 7(3) requires an appropriate other-territory tax adjustment to eliminate double taxation of qualifying adjusted profits, with authority consultation where necessary. [Article 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-7-business-profits).

Article 9 concerns separate associated enterprises, including direct/indirect participation in management, control or capital and common participation. Where non-independent commercial/financial conditions suppress profits, the article permits inclusion of profits that would otherwise have accrued; its corresponding-adjustment provision is conditional on those being independent-party profits. It does not automatically accept every foreign adjustment. Use [connected-party rules](gi-connected-party-pricing-and-interest.md) and the [MAP route](gi-income-tax-assessment-appeals.md#treaty-map-a-separate-submission-and-collection-decision) for the relevant domestic and dispute questions. [Article 9](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-9-associated-enterprises).

### Shipping and offshore overrides

Article 8 allocates profits from international-traffic ship/aircraft operations exclusively to the enterprise's territory. Bareboat rentals and container activities are included only when incidental to those operations; participation in pools, joint businesses and international operating agencies is also covered. Verify the Article 3 definition of international traffic and actual operations. [Articles 3(1)(h), 8](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force).

Article 21 takes priority for defined offshore exploration/exploitation activities. Paragraph (3) deems a PE, subject to paragraphs (4)–(5). The paragraph (4) exception is **not exceeding 30 days in aggregate in any twelve-month period beginning or ending in the fiscal year concerned**. Associated enterprises' substantially similar offshore activities are aggregated, excluding simultaneous activity. Its association definition is participation in management, control or capital or common participation; do not import Article 5(6)'s numerical route as its sole test. Paragraph (5) separately allocates specified offshore supply/personnel transportation and towing/anchor-handling profits exclusively to residence. [Article 21(1)–(5)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-21-miscellaneous-rules-applicable-to-certain-offshore-activities).

**Offshore example:** assume enterprise A performs 28 counted days, an associated enterprise performs 12 substantially similar days, and 10 of those days coincide with A's activity. Within the relevant window, the aggregate is **28 + 12 − 10 = 30 days**. One further non-overlapping day gives 31 and fails that paragraph (4) exception. This does not resolve paragraph (5), other PE rules, domestic charge or the distinct employee rules in the [employment treaty Guide](gi-uk-employment-pensions-treaty.md).

The [original executable control and assumptions](../../research/gibraltar-2026/corporate-completion-2026-10-28/preserved-corporate-controls.md) are preserved in supplementary research; the method and numerical explanation here remain unchanged.

This section establishes treaty rules, not a case-specific PE clearance, home-office ruling or profit-allocation approval. Current registration/return treatment for a particular non-resident enterprise, project-timing interpretations, valuation and internal-dealing evidence, other corridors and Article 28 anti-abuse application remain subject to further source and professional review.

For the separately sourced corporate residence-transfer exit base and conditional deferral, use the [foreign-tax-relief Guide](gi-foreign-tax-relief.md). Its retained-PE, scope, definition and payment limits remain explicit; stock cessation and capital-allowance adjustments above are separate methods.

## Two worked examples that recompute

### Example 1: ordinary liability and matched payments

For **already established** ordinary taxable profit of £100,000, tax is **£15,000**. If £10,000 was paid on account for that period, the residual is **£5,000**. An accounting period ending 30 June 2026 ordinarily produces a 31 March 2027 return/balance date; retain any applicable official extension. Zero accounting profit does not prove zero taxable profit.

```oa-check
name: Ordinary company liability and period-matched payment
inputs:
  established_taxable_profit: 100000
  ordinary_rate: 0.15
  payments_for_period: 10000
steps:
  - current_tax: established_taxable_profit * ordinary_rate
  - residual: current_tax - payments_for_period
expected:
  current_tax: 15000
  residual: 5000
```

### Example 2: mixed protected and restricted loss pools

**Interpretation, not published Commissioner guidance:** section 20(6) measures the 50% cap by profits computed under Schedule 3. Subsection (9) excludes protected-period losses from that restriction, and subsection (10) requires their use first. Read together, these provisions support keeping the cap at **50% of the original Schedule 3 profit measure**, while limiting the subsequent restricted-loss claim to the profits remaining after protected losses. They do not expressly direct a second calculation of 50% on that smaller remainder. This is the Guide's reasoned statutory reading; no official mixed-pool worked example or case-specific ruling has been verified. [Section 20(1), (6), (9)–(11); Schedule 3](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

For a reviewable working paper, let **P** be the positive Schedule 3 profit measure, **A** eligible unused protected losses and **B** eligible unused restricted losses. On that reading, protected losses used are `min(A, P)`, the cap is `0.5 × P`, and restricted losses used are the smallest of B, the cap and the remaining profit. Keep unused amounts in their respective pools. Assume all general eligibility and continuity conditions hold, no insolvency exception applies and no applicable regulations change the treatment. This illustration does not determine a taxpayer's designated status or the eligibility of a loss.

With P = £100,000, A = £40,000 and B = £80,000, use £40,000 protected losses first and £50,000 restricted losses next. The remaining profit component is **£10,000**, with £30,000 restricted losses unused. If A instead equals £70,000, only **£30,000** of restricted losses can be used, despite the £50,000 cap; remaining profit is zero and £50,000 restricted losses remain. If protected losses equal or exceed P, restricted losses are not used. These are loss-set-off examples, not final tax assessments.

```oa-check
name: Mixed loss pools using the original Schedule 3 cap interpretation
inputs:
  schedule3_profit: 100000
  protected_pool: 40000
  larger_protected_pool: 70000
  restricted_pool: 80000
steps:
  - cap: schedule3_profit * 0.5
  - protected_used: min(protected_pool, schedule3_profit)
  - restricted_used: min(restricted_pool, cap, schedule3_profit - protected_used)
  - residual_profit: schedule3_profit - protected_used - restricted_used
  - restricted_left: restricted_pool - restricted_used
  - larger_protected_used: min(larger_protected_pool, schedule3_profit)
  - second_restricted_used: min(restricted_pool, cap, schedule3_profit - larger_protected_used)
  - second_residual_profit: schedule3_profit - larger_protected_used - second_restricted_used
  - second_restricted_left: restricted_pool - second_restricted_used
expected:
  cap: 50000
  restricted_used: 50000
  residual_profit: 10000
  restricted_left: 30000
  second_restricted_used: 30000
  second_residual_profit: 0
  second_restricted_left: 50000
```

Section 20(11) permits regulations changing the percentage, designations and treatment of reliefs. Before filing, verify applicable regulations and obtain review of this interpretation for the actual claim. Retain the Schedule 3 computation, separate loss-period roll-forwards, protected-first ordering and the reason for the selected cap base. The arithmetic test checks the stated reading; it does not prove administrative acceptance. [Section 20(10)–(11)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

## Ask the client first

1. Where are management/control and profit-producing activities actually exercised, and what licensing or foreign-PE facts apply?
2. What are the tax accounting periods, income categories, assessable income and company-size evidence?
3. Which ledger adjustments, expenditure eligibility and capital-allowance pools are supported by source documents?
4. What loss periods, ownership/trade changes and designated-person or protected-pool facts apply?
5. Which verified basis liability, period-matched payments, current forecast and Commissioner decisions determine the CT4 request?
6. What signed return/attachment set, filing dates, submission evidence and unresolved interpretations need review?

### Self-checks and output

- Retain the relevant source version, the applicable period and the facts establishing scope.
- Reconcile every input to the client's records; keep estimates separate from actual amounts.
- Recompute the example and boundary cases before applying the method.
- Record exclusions and unresolved points explicitly. Do not convert a missing source into an exemption.
- Deliver a calculation, evidence list, filing calendar and reviewer questions. Record the exact revision reviewed.

## Sources

The following links collect the sources already cited above. Their applicable versions, statutory locators and unresolved limitations remain as stated in the body; this list is not a new source verification.

- [Rates of Tax Rules, rule 6](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf)
- [ITO, Guidance Notes for Companies, August 2025, pp2–3](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Guidance%20Notes%20for%20Companies,%2008-2025.pdf)
- [Income Tax Act](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf)
- [Articles 4 and 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force)
- [Article 5(1)–(3)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-5-permanent-establishment)
- [Article 7](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-7-business-profits)
- [Article 9](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-9-associated-enterprises)
- [Article 21(1)–(5)](https://www.gov.uk/government/publications/gibraltar-tax-treaties/2019-uk-gibraltar-double-taxation-agreement-in-force#article-21-miscellaneous-rules-applicable-to-certain-offshore-activities)
- [ITO corporate guidance](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate)
- [ITO entertainment guidance, printed pages 1 and 3](https://www.gibraltar.gov.gi/new/sites/default/files/1/01/guidance_on_business_entertainment_expenditure.pdf)
- [ITO downloads page](https://www.gibraltar.gov.gi/income-tax-office/downloads-ito)
- [ITO allocation table](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Corporate/Schedule%2010%20Table%20-%20Payments%20on%20Account%20-%202022%20to%202033.pdf)

Earlier source reads are preserved at 22 October 2026. The Act, corporate Rates Rules, cited UK treaty articles, entertainment guidance, allocation table and current ITO corporate/contact/CT4 material were read for the 28 October writer ledger; the August 2025 company-guidance PDF retains its earlier read scope. The dated research records retain statutory locators and source limitations. Inclusion of the allocation table or undated entertainment guidance does not remove the specific limitations noted above. The arithmetic blocks verify only the stated examples; they do not settle the mixed-loss cap interpretation or establish taxpayer eligibility.

### 28 October corporate procedure continuation

| Official source | Actual new scope read | Read on |
|---|---|---|
| [Income Tax Act, section 39](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) | Complete company payments-on-account and reduction provisions, subsections (4)–(9), printed pages 100–101 | 2026-10-28 |
| [Published CT4 workbook](https://www.gibraltar.gov.gi/new/sites/default/files/HMGoG_Documents/CT4%20-%20Claim%20to%20reduce%20payments%20on%20account%20for%20an%20accounting%20period.xls) | All populated cells, instructions, company/claim fields and declaration; read locally without modifying or executing the workbook | 2026-10-28 |
| [ITO corporate page](https://www.gibraltar.gov.gi/income-tax-office/businesses-and-corporations/corporate) | Current CT4 link, expired-period restriction and surcharge warning | 2026-10-28 |
| [ITO contact page](https://www.gibraltar.gov.gi/contacts/income-tax-office-76) | Corporate Tax Section: CT1/CT2 returns and general-query contacts | 2026-10-28 |

The [complete writer rule ledger and old-topics map](../../research/gibraltar-2026/corporate-completion-2026-10-28/ledgers/gi-corporate-tax.md) cover the inherited and new rules with exact primary-source quotes, dates and full original-paragraph destinations. This local v0.19 continuation has not received independent acceptance; the earlier full/delta reviews cover their recorded predecessors.

Not yet confirmed: section 16(6) extended-period boundaries; the Schedule 10 table’s specific anomalous dates; Schedule 3 paragraph 9(6) disposal wording and the paragraph 2(1)(o) Gazette-guideline identity; other capital-allowance/claim interactions and administrative confirmation of the labelled mixed-loss reading described above. The new published CT1/CT2 contact does not establish a tested filing or a CT4 route.

### Disclaimer

General tax and accounting reference material only. These drafts have not been professionally attested. A qualified professional in the relevant jurisdiction must check the facts, current law, elections and deadlines before anyone files, pays or acts on an output.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
