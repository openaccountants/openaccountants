---
name: uk-rental-sa105
description: Use this skill whenever asked about UK property income or rental income for individuals. Trigger on phrases like "SA105", "rental income UK", "property income", "buy-to-let", "letting income", "landlord tax UK", "rent-a-room", "mortgage interest relief", "Section 24", "property allowance", "non-resident landlord scheme", "NRLS", "furnished holiday let", "FHL abolished", "FHL abolition", "repairs deduction", "letting agent fees", "property expenses", "UK property pages", "April 2026 property tax", "property income hike", "MTD ITSA landlord", or any question about computing, filing, or reporting UK property income on a Self Assessment tax return. Covers SA105 form structure, allowable expenses, mortgage interest restriction, Rent-a-Room relief, property income allowance, non-resident landlord scheme, the abolition of FHL rules, and the April 2026 property income rate change announced at Autumn Budget 2025. ALWAYS read this skill before touching any UK rental income work.
version: 1.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - uk-income-tax-sa100
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK property income on the SA105 pages

Tax year 2026/27 (6 April 2026 to 5 April 2027) is the year in force. Returns being filed now are for tax year 2025/26, on the SA105 form HMRC labels "2026". Where a rule changed between those years, both are shown.

## Scope and who this is for

Individuals who let UK land or property and report it on the SA105 "UK property" pages of the SA100 return, or in Making Tax Digital for Income Tax (MTD) software. Covered: profit (cash basis, expenses, capital), the property allowance, Rent-a-Room, the residential finance cost restriction, replacement of domestic items, the end of furnished holiday lettings (FHL), joint ownership and Form 17, losses, the Non-resident Landlord Scheme (NRLS), MTD, the 2025/26 box map, filing and payment.

Out of scope: companies, partnership and trust returns, overseas property (the "Foreign" pages), Capital Gains Tax on a sale, Stamp Duty Land Tax. Rates shown are for England and Northern Ireland; "Income tax bands are different if you live in Scotland" ([Income Tax rates](https://www.gov.uk/income-tax-rates)).

## Ask the client first

- Where do you live, and have you been outside the UK for 6 months or more? (NRLS.)
- Which properties do you let, and are any overseas? (UK and overseas are separate businesses.)
- Is any letting a room in your own only or main home? (Rent-a-Room.)
- Do you own any property jointly? With whom, in what shares, and was a Form 17 sent?
- What were gross rents and other receipts, before expenses and agent's fees?
- Do you pay interest on a loan used for the letting? Residential or commercial property?
- Did you replace furniture or appliances, or do building work (repair or improvement)?
- Was any property an FHL in 2024/25 or earlier? Any capital allowance pools or FHL losses left?
- Any losses or unused residential finance costs brought forward (last year's boxes 43 and 45)?
- Any letting to family or friends below market rent?
- Did HMRC write to you about MTD? What was your self-employment plus property income before expenses on your 2024/25 and 2025/26 returns?
- Is any rent from your employer, your spouse's employer, or a company or partnership you or someone connected to you controls or belongs to?

## The method, step by step

1. **Who is taxed, in what shares.** The person "receiving or entitled to the profits" is taxed ([PIM1030](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim1030)). Spouses and civil partners are taxed 50/50 on joint property unless a valid Form 17 is in force.
2. **One UK business.** All UK lettings, including former FHLs, are added together; overseas lettings are kept separate ([working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income)).
3. **Accounting basis.** Cash basis is the default at receipts of £150,000 or less; otherwise traditional accounting (box 20.2) ([PIM1092](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim1092)).
4. **Rent-a-Room first** for a room in the main home: full exemption, exempt amount (box 37), or normal profit.
5. **Property allowance or expenses.** Never both, never with Rent-a-Room on the same income, never with the finance cost tax reducer.
6. **Sort costs:** expenses (boxes 24 to 29), private use (box 30), capital allowances (boxes 31 to 35), domestic items (box 36), residential finance costs (box 44), non-residential finance costs (box 26).
7. **Profit or loss** on HMRC's working sheet (box 38 or 41); use losses brought forward (box 39); carry the rest forward (box 43).
8. **Finance cost tax reduction:** 20% of the lowest of finance costs (with any brought forward), property profits after losses, and adjusted total income above the Personal Allowance. Carry the unused part forward (box 45 next year) ([how it is worked out](https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies)).
9. **Rate year.** 2025/26 and 2026/27 use the ordinary rates; separate property rates start in 2027/28.
10. **Reporting route and deadlines:** SA105 for 2025/26; MTD for 2026/27 if 2024/25 qualifying income was over £50,000; NRLS tax in box 21. File and pay on time ([MTD](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)).

## Rates, allowances and thresholds by year

### Income Tax rates on property income ([Finance Act 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [s.7](https://www.legislation.gov.uk/ukpga/2026/11/section/7); [Income Tax rates](https://www.gov.uk/income-tax-rates))

| Item | 2025/26 | 2026/27 (current year) | 2027/28 (enacted) |
| --- | --- | --- | --- |
| Personal Allowance | £12,570 | £12,570 | Not covered here |
| Basic rate | £12,571 to £50,270 at 20% | £12,571 to £50,270 at 20% | Property basic rate 22% |
| Higher rate | £50,271 to £125,140 at 40% | £50,271 to £125,140 at 40% | Property higher rate 42% |
| Additional rate | Over £125,140 at 45% | Over £125,140 at 45% | Property additional rate 47% |
| Finance cost tax reduction | 20% | 20% | 22% (announced) |

- For 2026/27, Finance Act 2026 s.2 sets "the basic rate is 20%". There is no separate property rate that year.
- s.7 sets the 2027/28 property rates for England, Wales and Northern Ireland; devolved powers are still to be commenced ([policy paper](https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income)).
- From 2027/28 general reliefs and the Personal Allowance are set against other income first, and "Finance cost relief will be provided at the separate property basic rate (22%)" ([HM Treasury explainer](https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-dividend-income/changes-to-tax-rates-for-property-savings-dividend-income)).
- Taper: the Personal Allowance "goes down by £1 for every £2" of adjusted net income above £100,000, reaching zero at £125,140 ([Income Tax rates](https://www.gov.uk/income-tax-rates)).

### Allowances and thresholds ([property allowance](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income); [Rent-a-Room HS223](https://www.gov.uk/government/publications/rent-a-room-for-traders-hs223-self-assessment-helpsheet/hs223-rent-a-room-scheme-2026); [SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf))

| Item | Figure | Years |
| --- | --- | --- |
| Property allowance | £1,000 a year | Each tax year from 6 April 2017, including 2025/26 and 2026/27 |
| Rent-a-Room limit | £7,500 (£3,750 if someone else also gets letting income from the same property) | 2025/26 (HS223 2026); HMRC's current guidance gives the same figure |
| Cash basis ceiling | Receipts £150,000 or less | 2017/18 onwards |
| Consolidated expenses (one figure in box 29) | Property income before expenses below £90,000 | 2025/26 return |
| Loss set against total income (capital allowances or agricultural losses only) | Relief capped at the greater of £50,000 or 25% of adjusted total income | 2025/26 return |

### Mileage for landlords ([PIM2220](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim2220))

Unincorporated landlords may use fixed mileage rates instead of actual running costs and capital allowances, but not if capital allowances were already claimed on the vehicle. Cars and goods vehicles: 55p a mile for the first 10,000 business miles and 25p after that for 2026/27; 45p and 25p up to and including 2025/26. Motorcycles 24p. Only journeys wholly and exclusively for the letting business count.

## The rules in detail

### Cash basis or traditional accounting ([PIM1092](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim1092))

- Cash basis (money in and out in the tax year) is the default for individuals and partnerships with receipts of £150,000 or less.
- Traditional accounting (GAAP) is required for companies, LLPs, trustees and partnerships with a non-individual member, and where receipts exceed £150,000 (reduced pro rata for a part year). It is also required where business premises renovation allowance was claimed and a balancing event in the tax year gives rise to a balancing adjustment (Condition D). A client can also elect for it, within one year of the filing date, by ticking box 20.2.
- Spouses or civil partners letting jointly and taxed 50/50 must use the same basis. This condition does not apply if a Form 17 declaration is in force.
- On the cash basis, no property loss can be set against general income.
- Under traditional accounting, rent is taxed in the year it is earned. Rent paid in advance for a later year is excluded ([PIM1101](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim1101)).

### Property allowance ([tax-free allowances](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income); [renting out: paying tax](https://www.gov.uk/renting-out-a-property/paying-tax))

- **£1,000 or less:** gross property income of up to £1,000 (UK and foreign added together) is exempt and need not be reported.
- **Above £1,000:** the client uses either the allowance or actual expenses, not both. The allowance deducts up to £1,000, cannot create a loss, and allows no other expenses or allowances. The total claimed across all property businesses cannot exceed £1,000. Joint owners each get £1,000 against their own share of gross rents.
- **Barred** in any year with property income from a company the client or a connected person owns or controls, from a partnership where either is a partner, or from the client's or spouse's employer.
- **Also barred** if the client claims the residential finance cost tax reducer, and on Rent-a-Room income.
- **Telling HMRC:** gross property income over £1,000 up to £2,500 means contact HMRC. A return is needed above £2,500 after allowable expenses or £10,000 before them. New clients register by 5 October after the tax year.

### Allowable expenses and capital ([working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income); [SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf))

The test is "wholly and exclusively for the purposes of renting out the property", and not capital. For a cost that is partly private, deduct only the business part (box 30 on the return).

| Cost | Treatment | SA105 box (2025/26) |
| --- | --- | --- |
| Head-lease rent, business and water rates, Council Tax, buildings, contents and rent-loss insurance, ground rent | Allowable if the landlord pays | 24 |
| Repairs: redecorating between tenants, damp, roof, replacing a broken-down boiler | Allowable | 25 |
| Interest and loan costs on non-residential lets | Allowable in full | 26 |
| Agent's fees, accountant's fees, legal fees for lets of a year or less or renewing a lease under 50 years | Allowable | 27 |
| Services to tenants, including gardeners' and cleaners' wages | Allowable | 28 |
| Phone, stationery, advertising, business travel, bad debts (traditional accounting only) | Allowable | 29 |
| Legal costs of a first letting for more than a year; buying, selling or improving property | Capital, not allowable | none |
| Residential mortgage interest and other residential finance costs | Tax reduction only | 44 |
| Mortgage capital repayments | Not allowable ("only the interest element") | none |

- Where insurance or a kept tenancy deposit pays for repairs, claim only the excess.
- HMRC lists "Council Tax while the property is vacant but available for letting" as deductible ([NRLS guidance](https://www.gov.uk/government/publications/non-resident-landord-guidance-notes-for-letting-agents-and-tenants-non-resident-landlords-scheme-guidance-notes/what-the-non-resident-landlords-scheme-is)).
- Uncommercial lets, such as to a relative at a reduced rent: expenses are capped at that property's rent. No loss arises.
- No Annual Investment Allowance is available for equipment for use in a dwelling-house.
- **Repair or improvement:** a repair "restores an asset to its original condition". The nearest modern equivalent is still a repair, "such as replacing a single-glazed window with a double-glazed window". An extension, a new security system, a higher-specification kitchen, or making a run-down property fit to let are capital.

### Residential finance cost restriction ([how it is worked out](https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies); [working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income))

- **Who:** individuals (UK resident) letting residential property in the UK or overseas; non-UK resident individuals letting UK residential property; partners; trustees and beneficiaries liable to Income Tax on residential profits. Companies are not affected.
- **What:** interest on mortgages, loans (including for furnishings) and overdrafts; alternative finance returns; arrangement and incidental fees; discounts, premiums and disguised interest. A mixed residential and commercial loan is apportioned.
- **The reduction:** since 2020/21, 0% of these costs is deductible and 100% goes to a tax reduction at the basic rate (20% for 2025/26 and 2026/27). It is 20% of the lowest of (a) finance costs not deducted plus any brought forward, (b) property profits after losses brought forward, and (c) adjusted total income (excluding savings and dividend income) above the Personal Allowance.
- It "can't be used to create a tax refund". Where (b) or (c) is the lowest, the unused costs carry forward (box 45 next year).
- Claiming it bars the property allowance.

### Replacement of domestic items relief ([working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income))

- **Covers:** movable furniture, furnishings, appliances and kitchenware in any let dwelling-house, furnished or not.
- **Conditions:** it replaces an old item, which is no longer available to the tenant; the new item is for the tenant's exclusive use; the cost would otherwise be capital; and no capital allowances were claimed on it.
- **Not available** for a first purchase, or for a room let in the client's own home.
- **Amount:** new item cost plus incidental buying or disposal costs, minus anything received for the old item. For an improvement, only the cost of an equivalent item counts. A reasonable modern equivalent, such as a more efficient fridge, is not an improvement. Box 36.

### Rent-a-Room relief ([HS223 2026](https://www.gov.uk/government/publications/rent-a-room-for-traders-hs223-self-assessment-helpsheet/hs223-rent-a-room-scheme-2026); [the Rent a Room Scheme](https://www.gov.uk/rent-room-in-your-home/the-rent-a-room-scheme))

- **Who:** owner-occupiers and tenants letting furnished accommodation in their only or main home.
- **Excluded:** accommodation that is not part of the main home, is unfurnished, is used as an office or business, or is let while the client lives abroad; homes converted into separate flats.
- **Limit for 2025/26:** £7,500, or £3,750 if someone else receives letting income from the same property. There is no part-year reduction.
- **Gross receipts** include rent before expenses, payments for meals and services such as cleaning or laundry, and balancing charges.
- **Receipts not more than the limit:** exempt automatically. Tick box 4 if this is the only letting income.
- **Receipts above the limit:** Method A taxes actual profit (the default). Method B taxes receipts minus the limit, with no expenses. For Method B, receipts go in box 20 and the exempt amount in box 37.
- **Time limit:** to opt out, or to start or stop Method B, tell HMRC within one year of 31 January after the tax year (31 January 2028 for 2025/26). HMRC's own worked example in HS223 says 31 January 2027 for the tax year ending 5 April 2026, so to be safe the client should act by 31 January 2027.
- **Losses:** exempt receipts and Method B cannot create a loss.

### Furnished holiday lettings: abolished from 6 April 2025 ([FHL policy paper](https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/abolition-of-the-furnished-holiday-lettings-tax-regime); [clarification](https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/clarification-on-abolition-of-the-furnished-holiday-lettings-tax-regime); [renting out: paying tax](https://www.gov.uk/renting-out-a-property/paying-tax))

Up to 2024/25 an FHL had to be available to let for at least 210 days, actually let for at least 105 days, have long lets (31 or more days in a row) of no more than 155 days in total, and be let at market rent. From 6 April 2025 for Income Tax and CGT (1 April 2025 for Corporation Tax):

| Area | Treatment from 2025/26 |
| --- | --- |
| Income | Part of the UK property business (overseas business for EEA lets); SA105 boxes 5 to 19 no longer used |
| Finance costs | Restricted, with the 20% tax reduction |
| Capital allowances | No new claims; replacement of domestic items relief instead. Pools that held expenditure by 5 April 2025 keep writing-down allowances until used up or a small-pool claim is made |
| FHL losses | Become losses of the ongoing UK or overseas property business (box 39) |
| CGT reliefs | Rollover, gift and Business Asset Disposal Relief end. BADR may still apply to a disposal within the normal 3-year period after an FHL business ceased before 6 April 2025. For a contract on or after 6 March 2024 with disposal on or after 6 April 2025, relief needs the anti-forestalling statement |
| Pensions | No longer relevant UK earnings; abolition is not a cessation |

### Jointly owned property and Form 17 ([ITA 2007 s.837](https://www.legislation.gov.uk/ukpga/2007/3/section/837); [Form 17](https://www.gov.uk/government/publications/income-tax-declaration-of-beneficial-interests-in-joint-property-and-income-17); [TSEM9852](https://www.gov.uk/hmrc-internal-manuals/trusts-settlements-and-estates-manual/tsem9852))

- **Not spouses or civil partners:** each owner is taxed on their share of the property, unless the owners agree a different split. The tax share must be the share actually agreed ([FHL clarification](https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/clarification-on-abolition-of-the-furnished-holiday-lettings-tax-regime)).
- **Spouses and civil partners living together:** taxed 50/50, whatever the shares, unless a valid Form 17 is in force.
- **Form 17 conditions:** they must hold the income in unequal shares (or one holds all of it), matching their shares in the property. It is not possible for beneficial joint tenants ([TSEM9850](https://www.gov.uk/hmrc-internal-manuals/trusts-settlements-and-estates-manual/tsem9850)). Both sign, with evidence such as a declaration of trust.
- **60-day rule:** the declaration only has effect if HMRC receives notice within 60 days beginning with its date. It applies only to income arising on or after that date. It covers only the listed assets and lasts until their interests change or they stop living together.
- **On SA105:** tick box 3 and enter only the client's share. If only a net share is notified, put income in box 20 or a loss in box 29.

### Losses ([PIM4210](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim4210); [SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf))

- A loss is carried forward automatically against the first profits of the same property business, indefinitely (box 39 used, box 43 carried forward).
- Only the capital-allowance part (boxes 32 to 35 minus box 31) or agricultural part can go against total income (box 42). This is capped at the greater of £50,000 or 25% of adjusted total income, and is not available on the cash basis.
- UK, overseas and partnership lettings are separate businesses for losses.
- Losses are lost on cessation. They may be usable if the same business restarts within 3 years, depending on the facts ([working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income)).

### Non-resident Landlord Scheme ([NRLS guidance notes](https://www.gov.uk/government/publications/non-resident-landord-guidance-notes-for-letting-agents-and-tenants-non-resident-landlords-scheme-guidance-notes/what-the-non-resident-landlords-scheme-is); [paying tax on rent to landlords abroad](https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad); [NRL1](https://www.gov.uk/guidance/apply-as-an-individual-to-receive-uk-rental-income-without-uk-tax-deducted))

- **Who:** landlords whose usual place of abode is outside the UK; for individuals, HMRC normally treats an absence of 6 months or more as meaning that. A UK resident can still be in the scheme. If only one spouse lives abroad, only their share is covered.
- **Who deducts:** letting agents, always, whatever the rent. Tenants paying the landlord directly deduct only if the rent is over £100 a week, unless HMRC says otherwise.
- **How much:** rent for the quarter minus deductible expenses paid, times the basic rate of Income Tax. Non-deductible payments to third parties, such as loan repayments, stay in.
- **When:** quarters end 30 June, 30 September, 31 December and 31 March, with payment within 30 days. By 5 July each year, form NRLY goes to HMRC and to the landlord, and certificate NRL6 goes to the landlord.
- **Gross payment:** apply on NRL1 (NRL2 companies, NRL3 trustees). HMRC approves if UK tax affairs are up to date, there were never UK tax obligations, or no UK liability is expected.
- **On SA105:** gross rents go in box 20 and the tax deducted in box 21.
- **Rate change:** the withholding rate is to move to the property basic rate by secondary legislation for 2027/28 ([policy paper](https://www.gov.uk/government/publications/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income/income-tax-changes-to-tax-rates-for-property-savings-and-dividend-income)). Check the regulations before applying 22%.

### Making Tax Digital for Income Tax ([when you need it](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax); [qualifying income](https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax); [quarterly updates](https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates))

| Qualifying income over | Measured on the return for | Must use MTD from |
| --- | --- | --- |
| £50,000 | 2024/25 | 6 April 2026 |
| £30,000 | 2025/26 | 6 April 2027 |
| £20,000 | 2026/27 | 6 April 2028 |

- **Once in MTD, there are three obligations:** (1) keep digital records in compatible software; (2) send quarterly updates from that software (dates below); (3) submit the year-end tax return through that software by 31 January following the end of the tax year ([submit your tax return](https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/submit-your-tax-return)). All quarterly updates must be sent before the return can be submitted. Quarterly updates are summaries, not tax returns.
- **Exempt clients:** a client can be exempt, for example if digitally excluded. An exempt client does not use MTD but must still report income and gains in a normal Self Assessment return.
- **Qualifying income** is self-employment plus property income before expenses. Employment, partnership shares, dividends and pensions are excluded. Joint owners count their share.
- **Quarterly updates** (standard periods to 5 July, 5 October, 5 January, 5 April) are due 7 August, 7 November, 7 February and 7 May. They are cumulative from 6 April.
- **Penalty points:** HMRC will not apply points for late quarterly updates in 2026/27. Penalty points will still apply for late tax returns for this tax year. From 2027/28, 4 points bring a £200 penalty.
- HMRC writes to those over a threshold, but the client must check even without a letter.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Landlord with residential mortgage interest wants the property allowance | Cannot use the allowance while claiming the finance cost tax reducer | [Property allowance](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| Rent-a-Room receipts exactly at the limit | "not more than" the limit: exempt | [HS223 2026](https://www.gov.uk/government/publications/rent-a-room-for-traders-hs223-self-assessment-helpsheet/hs223-rent-a-room-scheme-2026) |
| Self-contained flat in a converted house | Not Rent-a-Room | [Rent a Room Scheme](https://www.gov.uk/rent-room-in-your-home/the-rent-a-room-scheme) |
| Cash basis receipts exactly £150,000 | Cash basis still available ("£150,000 or less"); above it, traditional accounting | [PIM1092](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim1092) |
| Single to double glazing on replacement | Repair (nearest modern equivalent) | [Working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income) |
| Sofa (£400 like-for-like) replaced with a sofa bed (£550) | Relief £400; no relief for the extra £150 (HMRC example) | [Working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income) |
| Commercial property loan interest | Deductible in full (box 26), not restricted | [SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf) |
| Spouses own 90/10 as tenants in common, no Form 17 | Taxed 50/50 | [TSEM9846](https://www.gov.uk/hmrc-internal-manuals/trusts-settlements-and-estates-manual/tsem9846) |
| Spouses own as beneficial joint tenants | No Form 17 possible; 50/50 | [TSEM9850](https://www.gov.uk/hmrc-internal-manuals/trusts-settlements-and-estates-manual/tsem9850) |
| Form 17 received on day 61 | No effect; make a new declaration and send it in time | [ITA 2007 s.837](https://www.legislation.gov.uk/ukpga/2007/3/section/837) |
| Tenant pays an overseas landlord exactly £100 a week, no agent | Tenant need not operate NRLS unless HMRC says so (the rule bites "over £100 a week") | [Paying tax on rent to landlords abroad](https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad) |
| MTD qualifying income exactly £50,000 for 2024/25 | Not over the threshold, so not required from April 2026 | [MTD: when you need it](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax) |

## Worked cases

### Case A: finance costs above profit, carried forward ([HMRC case study, Example 4](https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies))

HMRC's own example, using the same 20% reduction that applies in 2025/26 and 2026/27. Year 1: rents £20,000, repairs and other non-finance costs £7,000, mortgage interest £15,000.

- Property profit = £20,000 − £7,000 = £13,000 (interest is not deducted).
- Tax reduction = 20% of the lowest of £15,000 (finance costs), £13,000 (profits) and adjusted total income: £13,000 × 20% = £2,600.
- Unused finance costs carried forward: £15,000 − £13,000 = £2,000 (SA105 box 45 next year).
- Year 2: profits £22,000, interest £15,000 plus £2,000 brought forward = £17,000. Reduction £17,000 × 20% = £3,400.

The example's tax bands are old-year figures; the reduction mechanics are unchanged.

### Case B: Rent-a-Room above the limit, 2025/26 ([HS223 2026](https://www.gov.uk/government/publications/rent-a-room-for-traders-hs223-self-assessment-helpsheet/hs223-rent-a-room-scheme-2026))

Chris lets a room in his home: rent £10,400 plus £200 for heating and light, so gross receipts are £10,600. His expenses are £9,000.

- Method A (actual profit): £10,600 − £9,000 = £1,600 taxable.
- Method B (receipts over the limit): £10,600 − £7,500 = £3,100 taxable.
- Method A is better and is HMRC's default. If Chris had elected Method B earlier, the statutory deadline to revoke it is 31 January 2028 for 2025/26, but HMRC's HS223 example says 31 January 2027, so he should act by 31 January 2027 to be safe. On SA105 he enters receipts in box 20 and expenses in the expense boxes, and leaves box 37 blank.

### Case C: property allowance or expenses, 2026/27 ([property allowance](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income))

Gross rent from a garage let to a neighbour: £2,400. Expenses: £300. No mortgage, no connected-party income.

- With the allowance: £2,400 − £1,000 = £1,400 taxable.
- With expenses: £2,400 − £300 = £2,100 taxable.
- Use the allowance. Gross income is over £1,000 but not over £2,500, so a client outside Self Assessment contacts HMRC rather than registering.

### Case D: higher-rate landlord, England, 2026/27 ([Income Tax rates](https://www.gov.uk/income-tax-rates); [Finance Act 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2); [finance cost case studies](https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies))

Salary £45,000. One buy-to-let: rents £20,000, allowable non-finance expenses £4,000, mortgage interest £9,000. No other income. Illustrative only.

- Property profit: £20,000 − £4,000 = £16,000.
- Total income: £45,000 + £16,000 = £61,000. Taxable after the £12,570 Personal Allowance: £48,430.
- Basic rate band width: £50,270 − £12,570 = £37,700. Tax: £37,700 × 20% = £7,540.
- Higher rate: £48,430 − £37,700 = £10,730. Tax: £10,730 × 40% = £4,292.
- Tax before the reduction: £7,540 + £4,292 = £11,832.
- Reduction: 20% of the lowest of £9,000, £16,000 and £48,430 = £1,800.
- Liability: £11,832 − £1,800 = £10,032 (before PAYE already paid).
- The property allowance is not available here, because the finance cost reducer is claimed. The rents alone are £20,000, below the April 2026 and April 2027 MTD thresholds, so MTD is not required on these figures.

### Case E: spouses, unequal ownership ([ITA 2007 s.837](https://www.legislation.gov.uk/ukpga/2007/3/section/837); [TSEM9848](https://www.gov.uk/hmrc-internal-manuals/trusts-settlements-and-estates-manual/tsem9848))

A married couple own a let flat as tenants in common, 75 and 25 by a declaration of trust, and the income follows those shares. They sign Form 17 on 1 September 2026 and HMRC receives it on 20 September 2026, inside 60 days. Income up to 31 August 2026 is split 50/50. Income from 1 September 2026 is split 75/25. Each ticks box 3 and enters only their own share. If HMRC had received the form after the 60 days, the declaration would have no effect and a fresh one would be needed.

### Case F: tenant operating the NRLS ([paying tax on rent to landlords abroad](https://www.gov.uk/guidance/paying-tax-on-rent-to-landlords-abroad))

HMRC's example: Julie paid £1,500 for the quarter: £200 for plumbing repairs (a deductible expense), £100 to pay off the landlord's loan, and £1,200 to the landlord. Tax is due on £1,300 at the basic rate of 20%, so £260 is due to HMRC within 30 days of the quarter end. The landlord claims the £260 in box 21 of SA105.

## When to refuse or refer

- Refer if the client's usual place of abode or UK residence is unclear.
- Refer property held by a company, LLP, trust or partnership.
- Refer a letting that may be a trade (guest house, serviced accommodation); it belongs on the self-employment pages.
- Refer a sale or gift of a former FHL, especially where BADR, rollover or gift relief is claimed after 6 April 2025, or a contract dated on or after 6 March 2024.
- Refer if a Form 17 is proposed but the couple own as joint tenants, or cannot evidence unequal beneficial interests.
- Refer Scottish or Welsh taxpayers for rate bands, and check whether devolved property rates apply from 2027/28.
- Refuse to deduct residential mortgage interest as an expense, to claim the property allowance alongside expenses or the finance cost reducer, or to claim domestic items relief for a first purchase.
- Refuse to present 2027/28 property rates as applying to 2026/27 income.
- Refer undisclosed past rental income to HMRC's Let Property Campaign.

## Filing and payment

### Deadlines for the 2025/26 return ([Self Assessment deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account))

- Register by 5 October 2026 if the client has not sent a return before, or did not need to send one for 2024/25.
- Paper return: HMRC must receive it by 11:59pm on 31 October 2026. Online return: by 11:59pm on 31 January 2027. Online by 30 December 2026 if the client wants a balance collected through their tax code.
- Pay the 2025/26 balance by 31 January 2027. Payments on account, each half of last year's tax, are due 31 January and 31 July. They are not needed if last year's tax was less than £1,000, or more than 80% was collected at source.
- Keep records for at least 5 years after the 31 January filing deadline ([working out rental income](https://www.gov.uk/guidance/income-tax-when-you-rent-out-a-property-working-out-your-rental-income)).

### Penalties ([Self Assessment penalties](https://www.gov.uk/self-assessment-tax-returns/penalties))

- Late return: £100 at once; after 3 months £10 a day up to £900; after 6 months and again after 12 months, 5% of the tax due or £300, whichever is greater.
- Late payment: 5% of unpaid tax at 30 days, 6 months and 12 months, plus interest.
- Late registration can bring a failure-to-notify penalty.

### SA105 box map for 2025/26 returns ([SA105 2026 form](https://assets.publishing.service.gov.uk/media/69cd19d6eafd66b876458ba9/SA105_2026_v0.1.pdf); [SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf))

| Box | What goes in it |
| --- | --- |
| 1, 2 | Number of properties let; X if all property income ceased in 2025/26 with none expected in 2026/27 |
| 3 | X if any property is let jointly (enter only your share) |
| 4 | X if claiming Rent-a-Room with rents of £7,500 or less (£3,750 if shared) |
| 5 to 19 | No longer in use (former FHL section) |
| 20, 20.1, 20.2 | Total rents and other income (non-residents: gross, before NRLS tax); property income allowance; X if traditional accounting |
| 21 | Tax taken off income in box 20 (NRLS only) |
| 22, 23 | Lease premiums (income part, leases up to 50 years); reverse premiums and inducements |
| 24 to 29 | Rent, rates, insurance, ground rents (24); repairs (25); non-residential finance costs (26); legal, management, professional fees (27); services and wages (28); other expenses (29), or all expenses as one figure in 29 if income before expenses is below £90,000 |
| 30, 31 | Private use adjustment; balancing charges |
| 32 to 35 | Annual Investment Allowance (32); Structures and Buildings Allowance (33); electric charge-points (33.1); Freeport and Investment Zones SBA (33.2); zero-emission cars (34.1; box 34 not used); all other capital allowances (35) |
| 36 | Costs of replacing domestic items (residential lettings only) |
| 37 | Rent-a-Room exempt amount |
| 38 to 40 | Adjusted profit (working sheet); loss brought forward used this year; taxable profit (38 minus 39) |
| 41 to 43 | Adjusted loss; loss set against 2025/26 total income (unusual); loss to carry forward |
| 44, 45 | Residential property finance costs; unused residential finance costs brought forward |

The working sheet adds boxes 20, 22, 23, 30 and 31, then subtracts boxes 24 to 29, 32 to 35, 36, 37 and 20.1. A property allowance claim leaves boxes 24 to 30 and 32 to 36 empty. HMRC has not yet published the 2026/27 SA105; clients in MTD for 2026/27 report through compatible software.

## Completion checklist ([SA105 notes 2026](https://assets.publishing.service.gov.uk/media/69cbb66fa60a12ca3913c62a/UK_property_notes.pdf); [Finance Act 2026 s.2](https://www.legislation.gov.uk/ukpga/2026/11/section/2))

- [ ] Residence and usual place of abode confirmed; NRLS credit in box 21 if relevant.
- [ ] Ownership shares confirmed; Form 17 validity checked (unequal beneficial interests, within 60 days, effect only from its date).
- [ ] All UK lettings, including former FHLs, in one business; overseas lettings excluded.
- [ ] Accounting basis confirmed (cash basis at £150,000 or less unless opted out in box 20.2).
- [ ] Rent-a-Room and property allowance compared with expenses; allowance not used with the finance cost reducer.
- [ ] Each cost tested for revenue or capital; mileage at the right year's rate.
- [ ] Finance costs: residential in box 44, unused brought forward in box 45, non-residential in box 26.
- [ ] Domestic items relief conditions met (replacement, old item removed, no capital allowances).
- [ ] Losses brought forward applied (box 39) and carried forward (box 43).
- [ ] FHL pools and losses from 2024/25 or earlier carried into the UK business.
- [ ] 2026/27 computations use 20/40/45 and a 20% reduction. 2027/28 projections use 22/42/47 and 22%, labelled as future.
- [ ] MTD position checked for April 2026, April 2027 and April 2028.
- [ ] Return filed and balance and payments on account paid by the deadlines.

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
