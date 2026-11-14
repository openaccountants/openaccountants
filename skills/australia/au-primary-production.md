---
name: au-primary-production
description: >
  Use this skill to prepare Australian primary production workpapers for 2026-27
  for individuals, partners and trust beneficiaries carrying on a farming,
  fishing or forestry business: whether a business of primary production is
  carried on (TR 97/11), income averaging under Division 392, farm management
  deposits under Division 393, livestock trading stock values, natural increase
  cost elections and forced disposal or death elections (Subdivision 385-E), and
  the special depreciation rules for water facilities, fencing, fodder storage,
  horticultural plants and landcare. Trigger on "primary producer", "farm
  management deposit", "FMD", "income averaging", "natural increase", "forced
  disposal of livestock" or "drought".
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27 (law and figures read 2 November 2026)"
tier: 2
last_updated: 2026-11-02
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australian Primary Production v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide prepares the primary production workpapers that sit behind an income tax return: a business indicator matrix, a primary and non-primary production income split for each owner, a farm management deposit (FMD) register, income averaging inputs and an estimate, a livestock reconciliation in head and dollars, forced disposal or death elections, and the classification of primary production depreciating assets. It loads on top of `workflow-base`, whose reviewer brief, intake and self-check rules apply. Law and figures are as read on 2 November 2026 for the 2026-27 income year (1 July 2026 to 30 June 2027).

It covers individuals carrying on a primary production business in Australia, alone, as partners, or as trust beneficiaries treated as carrying on the trust's business. Companies and trustees appear only where they make an election for the business (Subdivision 385-E) or cannot use a concession. It does not cover:

- The business schedule and its P8 primary and non-primary production labels, and the small business simplified trading stock threshold: `au-sole-trader-schedule`.
- Partnership and trust returns and distributions: `au-partnerships` and `au-trust-distributions`.
- Non-commercial losses under Division 35, including the primary production exception: `au-deductions-offsets` and `au-partnerships`.
- General depreciation (Division 40 decline in value, the instant asset write-off, small business pooling) and Division 43 capital works: `au-deductions-offsets`. This guide holds only the primary production rules in Subdivisions 40-F and 40-G and the small business choice for them.
- Individual tax rates, the return assembly and amendments: `au-rates-2026-27`, `au-individual-return` and `au-amending-individual-income-tax-return-period`.
- Capital gains on farm land, water entitlements and carbon sequestration rights, and the small business CGT concessions: `au-capital-gains` and `au-small-business-cgt`.
- Fuel tax credits: `au-fuel-tax-credits`. GST: `australia-gst` and `au-gst-bas`. PAYG instalments, including the 2-instalment option for primary producers: `au-payg-instalments`.
- State land tax and duty concessions for primary production land: `au-land-tax` and `au-stamp-duty`.
- Australian carbon credit units, forestry managed investment schemes, carbon sink forests and the horse industry rulings: refer (R-AU-PP-3, R-AU-PP-5).

**The reviewer is the customer of this output.** The ATO calculates the averaging result on assessment; every averaging figure here is a labelled estimate, not a return figure. An authorised human decides positions, signs and lodges.

## Ask the client first

1. The income year, the entity, and each owner's interest (individual, partner or trust beneficiary) with the share of income for each.
2. A description of each activity with business evidence: plans, scale, sales records, registrations, history of profit and loss, and time spent.
3. Primary production and non-primary production income and deductions for each owner, reconciled to the business schedule or the partnership or trust return.
4. Basic taxable income for up to the 4 prior income years, the averaging history, and any choice not to average or to restart averaging, with its date.
5. FMD statements from every provider: each deposit's date and amount, repayments, transfers, consolidations, interest paid and any loan offset arrangement.
6. Evidence for any FMD repayment within 12 months: rainfall records for the land, a disaster recovery grant letter, or evidence of death, bankruptcy or ceasing the business.
7. A livestock reconciliation by class: opening head and value, purchases, natural increase, sales, deaths, rations and private use, and closing head; last year's closing value and basis for each class.
8. Forced disposal or death circumstances (compulsory acquisition, tick eradication lease, fire, drought or flood, disease destruction, contamination notice) with documents, proceeds, compensation and replacement intentions.
9. Capital expenditure records for water facilities, fencing, fodder storage, horticultural plants and landcare works: date incurred, cost, use, whether owner or lessee, and any small business entity choice already made.

## The method, step by step

### Step 1: Is a business of primary production carried on?

A primary production business is a business of cultivating or propagating plants, fungi or their products; maintaining animals for sale or for their bodily produce, including natural increase; manufacturing dairy produce from raw material you produced; fishing and related operations; pearling; planting or tending trees intended to be felled; felling trees; or 'transporting trees, or parts of trees, that you felled in a plantation or forest to the place: (i) where they are first to be milled or processed; or (ii) from which they are to be transported to the place where they are first to be milled or processed' ([ITAA 1997 s 995-1, 'primary production business', paras (a) to (h)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1)).

Whether the activity is a business is decided by weighing the indicators in [TR 97/11 para 13](https://www.ato.gov.au/law/view/document?docid=TXR/TR9711/NAT/ATO/00001): significant commercial purpose or character; more than an intention to engage in business; a purpose and prospect of profit; repetition and regularity; similarity to the ordinary trade; businesslike planning and organisation; size, scale and permanency; and whether the activity is better described as a hobby, recreation or sport. No one indicator decides it (para 15), and other employment does not stop a primary production activity being a business (para 14). Prepare the matrix; the reviewer decides (R-AU-PP-1).

Route an individual's loss to `au-deductions-offsets` for Division 35 before any of Steps 3 to 5 rely on it, and the business schedule to `au-sole-trader-schedule`, `au-partnerships` or `au-trust-distributions`.

### Step 2: Split income and deductions for each owner

Build each income measure from its own source; do not reuse one total:

- **Basic taxable income** is taxable income excluding certain superannuation and employment termination amounts and any net capital gain, less any above-average special professional income; nil if negative ([s 392-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-15)).
- **Taxable primary production income** is assessable primary production income less primary production deductions, floored at nil ([s 392-80](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-80)). Assessable primary production income is basic assessable income derived from carrying on a primary production business, plus certain carbon unit amounts (s 392-80(2); R-AU-PP-3). Take partnership and trust shares from `au-partnerships` and `au-trust-distributions`.
- **Taxable non-primary production income** is the rest of basic assessable income less the other deductions, floored at nil ([s 392-85](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-85)).
- FMD interest is assessable but is not primary production income, and government income support and disaster payments are not primary production income ([ATO, Farm management deposits scheme](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/primary-producers/managing-varying-income/farm-management-deposits-scheme); [ATO, Income averaging](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/primary-producers/managing-varying-income/tax-averaging)).

### Step 3: Farm management deposits (Division 393)

Keep one register line for each deposit: owner, provider, date, amount, deductible and non-deductible parts, repayments, transfers and interest.

**Deduction.** The owner can deduct a deposit for the year it is made if all of these hold ([s 393-5(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-5)):

1. The owner is an individual carrying on a primary production business in Australia when the deposit is made. Partners and certain trust beneficiaries are treated as individuals carrying on the business ([s 393-25(2) to (6)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-25)). Companies and other entities cannot hold an FMD, and deposits cannot be joint (ATO FMD page; [s 393-35 item 2](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-35)).
2. If the business stops later in the year, it restarts within 120 days.
3. The owner's taxable non-primary production income for the year is not more than $100,000.
4. The owner does not die or become bankrupt in the year.

The year's FMD deductions cannot exceed the owner's taxable primary production income, applied in deposit order ([s 393-5(2), (3)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-5)). That income is measured before the FMD deduction itself: in the example to s 393-10(1), taxable primary production income of $50,000 makes a $120,000 deposit 'only partly deductible', and the unrecouped deduction is $50,000. Whether the FMD deduction is then a primary production deduction (s 392-80(3)) or a non-primary production deduction (s 392-85(3)) changes averaging and the $100,000 test; the sections read do not settle it, so the reviewer decides (Needs Input).

**Account conditions** ([s 393-35](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-35)): a deposit of $1,000 or more (item 4); a trustee may deposit only for a beneficiary under a legal disability who is presently entitled (item 3); no encumbrance (item 7); interest not reinvested as an FMD with the provider without first being paid to the depositor (item 9); no single deposit, and no total of all the owner's FMDs, above $800,000 (item 10); repayment on death, bankruptcy or ceasing the business without restarting within 120 days (item 11); repayments of $1,000 or more unless the whole deposit is repaid (item 12); no provider fees deducted (item 14). From 2016-17 a provider may reduce interest on a loan relating to the owner's or partnership's primary production business ([s 393-37](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-37)). The ATO says that under such an offset the FMD interest is not assessable and the interest saved is not deductible, if the FMD is linked to the loan, the business is run as a sole trader or partnership, and the loan relates wholly to the primary production business (ATO FMD page).

**Repayments.** A repayment is assessable to the extent the deposit's unrecouped deduction exceeds what remains after the repayment, so non-deductible amounts come out first ([s 393-10(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-10)). Repayments count as assessable primary production income in averaging (ATO FMD page). Death, bankruptcy or ceasing the business makes the deposit taxable when it becomes repayable, not when paid ([s 393-10(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-10)). Reinvesting with the same provider, extending the term or a requested transfer is not a repayment or a new deposit ([s 393-15](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-15)).

**The 12-month rule.** Any part repaid before the last day of the 12 months after the deposit day is taken never to have been an FMD, and a deposit reduced below $1,000 in that time is taken never to have been one ([s 393-40(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-40)). The exceptions, each with its own evidence:

- **Severe rainfall deficiency** ([s 393-40(3), (3AA)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-40)): the owner's business is one of paras (a), (b), (c) or (f) of the definition (plants, animals, dairy, tree planting), and rainfall on land where it is carried on was within the lowest 5% for that land on Bureau of Meteorology records for the most recent 6 consecutive months before the repayment for which records are publicly available at the time of the repayment, with the business carried on there and the amount held in the FMD for that period. The current regulations prescribe no different deficiency or period ([Income Tax Assessment (1997 Act) Regulations 2021, compilation 16, 27 June 2026](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html): Division 393 holds only ss 393-20.01, 393-20.02 and 393-40.01). The test is the rainfall record, not a drought declaration.
- **Natural disaster** ([s 393-40(3A)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-40); Regulations 2021 s 393-40.01): Category C recovery assistance as a primary producer recovery grant under the Disaster Recovery Funding Arrangements 2018, first provided during the 12-month period, with the repayment made after it was first provided.
- **Death, bankruptcy or ceasing the business** ([s 393-40(5)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-40)).

After a drought or disaster repayment, a later deposit by the owner in the same income year is not an FMD ([s 393-40(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-40)). An exception repayment is still assessable. Without an exception, a deduction claimed for the earlier year falls away: route the amendment to `au-amending-individual-income-tax-return-period`. Keep each claimed exception `UNVERIFIED` until its evidence is on file. Never instruct a provider (R-AU-PP-2).

### Step 4: Income averaging (Division 392)

**Eligibility** ([s 392-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-10)): an individual who has carried on a primary production business in Australia for 2 or more income years in a row ending with the current year, where for at least one of those years basic taxable income was less than or equal to the next year's. Averaging can continue after the business stops while income from it, or another primary production business, continues (s 392-10(2)). Trust beneficiaries presently entitled to income of a trust carrying on the business are taken to carry it on; below $1,040 of trust income, only if the Commissioner is satisfied the interest was not acquired or granted wholly or primarily to obtain averaging ([s 392-20(2)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-20)). Averaging does not start until the first year basic taxable income is at least the previous year's, so the first adjustment is an offset or nil ([ATO, Income averaging](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/primary-producers/managing-varying-income/tax-averaging)).

**Calculation** (estimate only; the ATO computes it on assessment):

1. Years averaged: the current year and the 4 previous years if Division 392 has applied for at least 4 years in a row, including the current year; otherwise those years and the year before them ([s 392-40](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-40)).
2. Average income: the sum of basic taxable income for those years divided by their number, rounded down to whole dollars ([s 392-45](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-45)).
3. Comparison rate: income tax on average income at the current year's basic rates, divided by average income ([ss 392-50, 392-55](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-55)). Basic rates are the resident rates in Schedule 7 Part I of the Income Tax Rates Act 1986, or Part II for non-residents, ignoring Medicare levy, rebates and credits ([s 392-35(4), (5)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-35)). The 2026-27 resident scale is in `au-rates-2026-27`, read again for this guide at the [ATO resident tax rates page](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents) (updated 13 August 2026).
4. Gross averaging amount: the difference between tax on basic taxable income at the comparison rate and at basic rates ([s 392-70](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-70)). Comparison-rate tax below basic-rate tax gives a tax offset; above gives extra income tax ([s 392-35(2), (3)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-35)).
5. Averaging adjustment: gross averaging amount x averaging component / basic taxable income ([s 392-75](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-75)).

**Averaging component** ([s 392-90](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-90)):

| Taxable non-primary production income | Taxable primary production income above nil | Taxable primary production income nil |
|---|---|---|
| Nil | Basic taxable income | Nil |
| Above nil, not over $5,000 | Basic taxable income | Basic taxable income |
| Over $5,000, not over $10,000 | Taxable primary production income plus the shade-out amount | The shade-out amount |
| $10,000 or more | Taxable primary production income | Nil |

The shade-out amount is $10,000 less taxable non-primary production income when taxable primary production income is above nil (s 392-90(2)). When it is nil, the shade-out amount is $10,000 less taxable non-primary production income less (primary production deductions less assessable primary production income), floored at nil (s 392-90(3), formula image in the ATO legal database).

**Choices.** An individual can choose in writing, by the time the return is lodged unless the Commissioner allows later, not to average for that year and the next 9 years; the choice cannot be revoked or overlap an earlier one ([s 392-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-25)). Where basic taxable income for a year is permanently reduced below two-thirds of average income because of retirement or another cause, the individual can choose, in writing by lodgment, that averaging not apply for that year; later years are then assessed as if no primary production business had been carried on before it ([s 392-95(1) to (1B)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-95)). Both are the client's decisions with the reviewer.

### Step 5: Livestock and other trading stock

1. Reconcile head by class to movement records (opening, purchases, natural increase, sales, deaths, rations and private use, closing).
2. Opening value must equal last year's closing value. Value each class, or each animal, at cost, market selling value or replacement value; the basis can change from year to year ([ATO, Information for primary producers 2026, Valuing livestock](https://www.ato.gov.au/law/view/document?docid=SAV/PP)). A small business entity may choose the simplified trading stock rules: route the threshold to `au-sole-trader-schedule`.
3. **Natural increase.** The cost of an animal acquired by natural increase is, at the taxpayer's election, its actual cost or the cost the regulations prescribe for its class ([s 70-55(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/70-55)); make the election by the time the return for the year of acquisition is lodged, unless the Commissioner allows later (s 70-55(3)). A horse bred from a paid insemination service costs at least the attributable service fee (s 70-55(2)). Prescribed costs ([Regulations 2021 s 70-55.01](https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html), compilation 16):

| Class of live stock | Prescribed cost per animal |
|---|---|
| Cattle | $20.00 |
| Deer | $20.00 |
| Emus | $8.00 |
| Goats | $4.00 |
| Horses | $20.00 |
| Pigs | $12.00 |
| Poultry | $0.35 |
| Sheep | $4.00 |

   A class not in the table (for example alpacas or ostriches) has no prescribed cost; the ATO guide says to contact the ATO to confirm the cost (R-AU-PP-5).
4. **Rations and private use.** Account for stock taken for the owner's or family's use, including livestock slaughtered for personal consumption or employees' rations, as if disposed of at cost ([ATO, Information for primary producers 2026](https://www.ato.gov.au/law/view/document?docid=SAV/PP)). The ATO's annual determination of values for goods taken from stock was not read for 2026-27 (Needs Input if a value from it is used).
5. **Forced disposal or death of livestock (Subdivision 385-E).** An election is available where livestock held as assets of a primary production business in Australia are disposed of or die because land is compulsorily acquired or resumed, a State or Territory leases land for cattle tick eradication, pasture or fodder is destroyed by fire, drought or flood and the proceeds will be used mainly to buy replacement stock or maintain breeding stock, livestock are compulsorily destroyed for disease control or die of such a disease, or an official contamination notice is received ([s 385-100(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-100)). Proceeds are defined in s 385-100(2).
   - Tax profit: proceeds less the purchase cost of livestock bought during the year and the opening trading stock value of the rest ([s 385-105(3)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-105)).
   - **Spread** ([s 385-105(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-105)): proceeds less tax profit, plus 20% of the tax profit, in the disposal year; 20% in each of the next 4 years.
   - **Defer** ([s 385-110](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-110)), available only if the proceeds will be used mainly to buy replacement livestock or maintain breeding stock to replace them (s 385-110(2)): proceeds less tax profit in the disposal year; the purchase price of each replacement animal bought in that year or the next 5 years is treated as reduced by the tax profit for the species divided by the number of that species disposed of or dead, but not so as to take unused tax profit below nil ([s 385-120](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-120)); amounts chosen for replacement animals bred are assessable ([s 385-115](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-115)); any unused tax profit is assessable in the fifth year after the disposal year. Bovine tuberculosis cases run over 10 years ([s 385-125](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-125)).
   - Related elections: an insurance recovery for lost livestock or fire-damaged trees can be spread 20% a year over 5 years (Subdivision 385-F, [s 385-130](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-130)), and profit on an early second wool clip forced by fire, drought or flood can be deferred to the next year (Subdivision 385-G, [s 385-135](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-135)).
   - Rules for all 3 kinds of election (Subdivision 385-H): only the partnership or trustee can elect for a business it carries on ([s 385-145](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-145)); elect before lodging the return for the last year the amount would otherwise be assessable, unless the Commissioner allows more time ([s 385-150](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-150)); a disentitling event after an election brings the remaining amount to tax ([s 385-160](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-160)); amounts included are primary production income ([s 385-155](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-155)).

   The taxpayer decides whether to elect, with the reviewer.

### Step 6: Primary production depreciating assets

Classify each item before it reaches the general schedule in `au-deductions-offsets`.

| Asset | Meaning | Deduction | Source |
|---|---|---|---|
| Water facility (dam, tank, bore, pipe, pump, windmill, irrigation channel, and things reasonably incidental such as a culvert) | [s 40-520(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-520) | Whole capital cost in the year incurred, for expenditure from 7:30 pm AEST on 12 May 2015 | [s 40-540](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-540); ATO guide |
| Fencing asset (a fence, or a capital repair, alteration, addition or extension to one) | s 40-520(4) | Whole capital cost in the year incurred, for expenditure from 7:30 pm AEST on 12 May 2015; stockyards, pens and portable fences are excluded (s 40-555(7)) and the ATO says the earlier rules for fences apply to them | [s 40-551](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-551); ATO guide |
| Fodder storage asset (silo, tank, bin, shed, above-ground bunker for fodder) | s 40-520(3) | Whole cost in the year incurred where incurred on or after 19 August 2018, or incurred earlier and first used or installed ready for use on or after that date; otherwise, for expenditure from 7:30 pm AEST on 12 May 2015 to 18 August 2018, a third a year over 3 years | [s 40-548](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-548); ATO guide |
| Horticultural plant (a live plant or fungus cultivated or propagated for its products or parts) | s 40-520(2) | Effective life under 3 years: all establishment cost when it starts to decline in value; otherwise the write-off rates below | [s 40-545](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-545) |
| Landcare operation (land class fencing under an approved plan, fencing out animals from degraded land, levees, salinity drainage, pest and weed eradication, other works against land degradation) | [s 40-630](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-630); list from ATO guide | Capital cost in the year incurred, for land used for primary production or for a rural land business other than mining or quarrying; reduced by a reasonable amount for later other use (s 40-630(1), (3)) | s 40-630; ATO guide |

Conditions: water facility, fencing and fodder storage expenditure must be incurred primarily and principally for a primary production business conducted on land in Australia ([s 40-525](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-525)), and the deduction is reduced for any period the asset is not wholly used in that business or for a taxable purpose ([s 40-515(4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-515)). A lessee can claim; a partnership cannot, so the cost is allocated to the partners ([ATO, Information for primary producers 2026, Depreciating assets](https://www.ato.gov.au/law/view/document?docid=SAV/PP)). A second-hand water facility, fodder storage asset or fence attracts no deduction if anyone has deducted or can deduct earlier expenditure on it, and a fence deducted as a landcare operation cannot also be deducted as a fencing asset ([s 40-555(1), (4) to (6)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-555)).

Horticultural plant write-off rates, applied to establishment expenditure x write-off days / 365, where write-off days are days of commercial horticulture use or readiness inside the time limit ([s 40-545(2), (3)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-545)):

| Effective life | Annual write-off rate | Use counted for at most |
|---|---|---|
| 3 to fewer than 5 years | 40% | 2 years and 183 days |
| 5 to fewer than 6 2/3 years | 27% | 3 years and 257 days |
| 6 2/3 to fewer than 10 years | 20% | 5 years |
| 10 to fewer than 13 years | 17% | 5 years and 323 days |
| 13 to fewer than 30 years | 13% | 7 years and 253 days |
| 30 years or more | 7% | 14 years and 105 days |

**Small business entities** may choose, for each such asset, Subdivision 40-F or 40-G treatment or the simplified depreciation rules ([s 328-175(3), (4)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/328-175)); once made for an asset the choice cannot be changed (s 328-175(4)), and horticultural plants cannot use the simplified rules (s 328-175(5)). The ATO guide says capital expenditure on connecting mains electricity or installing a phone line can be deductible over 10 years under separate rules; route those, with every general depreciating asset, to `au-deductions-offsets`.

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Business status unclear | Prepare the TR 97/11 matrix; mark every concession that needs a business as conditional |
| Taxable non-primary production income near $100,000 and not final | Hold the FMD deduction as conditional until the year's income is known |
| FMD repaid within 12 months, exception evidence missing | Treat the repaid part as never an FMD; flag the earlier deduction for amendment |
| Unknown deductible part of an FMD | Treat repayments as assessable only after non-deductible amounts, using provider and return records; flag if neither exists |
| Prior years' basic taxable income missing | No averaging estimate; Needs Input |
| Natural increase election not recorded | Use actual cost only if records support it; otherwise Needs Input before lodgment |
| Livestock class valuation basis not recorded for last year | Opening value equals last year's closing value as lodged; do not revalue |
| Forced disposal circumstance undocumented | No election in the workpaper; list the evidence needed |
| Asset could be a water facility, fence or landcare item | Record the facts against each meaning; claim under one provision only |

## Worked cases

All facts are hypothetical and set in 2026-27 unless stated.

### Case A: FMD deduction limit and a later repayment

Ella, a grazier, has taxable primary production income of $60,000 and taxable non-primary production income of $40,000 in 2026-27. She already holds $650,000 in FMDs, deposits $50,000 on 1 October 2026 and $30,000 on 1 May 2027. Both deposits pass the eligibility tests, but deductions are capped at taxable primary production income in deposit order, so $20,000 of the May deposit is not deductible. In September 2028, more than 12 months after the May deposit, she withdraws $25,000 of it; $5,000 is assessable in 2028-29 (s 393-10).

```oa-check
name: AU 2026-27 FMD deduction limit and later repayment assessability
inputs:
  taxable_pp_income: 60000
  taxable_non_pp_income: 40000
  non_pp_income_limit: 100000
  deposit_oct_2026: 50000
  deposit_may_2027: 30000
  balance_before: 650000
  holding_limit: 800000
  repayment_of_may_deposit: 25000
steps:
  - non_pp_headroom: non_pp_income_limit - taxable_non_pp_income
  - deductible_oct: min(deposit_oct_2026, taxable_pp_income)
  - deductible_may: min(deposit_may_2027, taxable_pp_income - deductible_oct)
  - non_deductible_may: deposit_may_2027 - deductible_may
  - holding_headroom_after: holding_limit - (balance_before + deposit_oct_2026 + deposit_may_2027)
  - remaining_after_repayment: deposit_may_2027 - repayment_of_may_deposit
  - assessable_on_repayment: max(deductible_may - remaining_after_repayment, 0)
expected:
  non_pp_headroom: 60000
  deductible_oct: 50000
  deductible_may: 10000
  non_deductible_may: 20000
  holding_headroom_after: 70000
  remaining_after_repayment: 5000
  assessable_on_repayment: 5000
```

### Case B: averaging estimate with a shade-out amount

Tom, a resident wheat grower, has been in averaging for well over 4 years. Basic taxable income: 2022-23 $30,000; 2023-24 $40,000; 2024-25 $35,000; 2025-26 $50,000; 2026-27 $95,000, made up of $87,000 taxable primary production income and $8,000 taxable non-primary production income. Tax at basic rates uses the 2026-27 resident scale: 15% from $18,200 to $45,000 and 30% from $45,000 to $135,000 ([ATO resident tax rates](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents)). The estimate is an offset of $7,993.14; the assessment figure governs.

```oa-check
name: AU 2026-27 income averaging offset with a non-primary production shade-out
inputs:
  bti_2022_23: 30000
  bti_2023_24: 40000
  bti_2024_25: 35000
  bti_2025_26: 50000
  bti_2026_27: 95000
  taxable_pp_income: 87000
  taxable_non_pp_income: 8000
steps:
  - average_income: floor((bti_2022_23 + bti_2023_24 + bti_2024_25 + bti_2025_26 + bti_2026_27) / 5)
  - tax_on_average: pct(clamp(average_income - 18200, 0, 26800), 15) + pct(clamp(average_income - 45000, 0, 90000), 30)
  - comparison_rate: tax_on_average / average_income
  - tax_at_comparison_rate: bti_2026_27 * comparison_rate
  - tax_at_basic_rates: pct(clamp(bti_2026_27 - 18200, 0, 26800), 15) + pct(clamp(bti_2026_27 - 45000, 0, 90000), 30)
  - gross_averaging_amount: tax_at_basic_rates - tax_at_comparison_rate
  - shade_out_amount: 10000 - taxable_non_pp_income
  - averaging_component: taxable_pp_income + shade_out_amount
  - averaging_offset: round(gross_averaging_amount * averaging_component / bti_2026_27, 2)
expected:
  average_income: 50000
  tax_on_average: 5520
  comparison_rate: 0.1104
  tax_at_comparison_rate: 10488
  tax_at_basic_rates: 19020
  gross_averaging_amount: 8532
  shade_out_amount: 2000
  averaging_component: 89000
  averaging_offset: 7993.14
```

### Case C: drought sale of cattle, spread or defer

In 2026-27 drought destroys a grazier's pasture and she sells 400 head of cattle for $300,000, intending to use the proceeds mainly to restock. Of those cattle, 50 were bought during the year for $60,000; the other 350 had an opening trading stock value of $70,000. The tax profit is $170,000. If she elects to spread, $164,000 is assessable in 2026-27 and $34,000 in each of the next 4 years. If she elects to defer and buys 200 replacement cattle at $1,200 each in 2027-28, each is treated as costing $775, leaving $85,000 of unused tax profit to be used or assessed by 2031-32.

```oa-check
name: AU 2026-27 forced disposal of livestock tax profit spread and defer
inputs:
  proceeds: 300000
  purchases_in_year_cost: 60000
  opening_value_rest: 70000
  head_disposed: 400
  replacement_head: 200
  replacement_price_each: 1200
steps:
  - tax_profit: proceeds - purchases_in_year_cost - opening_value_rest
  - spread_disposal_year: proceeds - tax_profit + pct(tax_profit, 20)
  - spread_each_later_year: pct(tax_profit, 20)
  - defer_disposal_year: proceeds - tax_profit
  - reduction_per_head: tax_profit / head_disposed
  - reduced_cost_each: replacement_price_each - reduction_per_head
  - unused_tax_profit: tax_profit - replacement_head * reduction_per_head
expected:
  tax_profit: 170000
  spread_disposal_year: 164000
  spread_each_later_year: 34000
  defer_disposal_year: 130000
  reduction_per_head: 425
  reduced_cost_each: 775
  unused_tax_profit: 85000
```

### Case D: a new orchard block in its first part-year

A grower spends $40,000 establishing a block of trees with a stipulated effective life of 12 years. The block can first be used for commercial horticulture on 1 January 2027, giving 181 write-off days in 2026-27. The 17% rate applies.

```oa-check
name: AU 2026-27 horticultural plant first part-year write-off
inputs:
  establishment_expenditure: 40000
  write_off_rate_percent: 17
  write_off_days: 181
  days_basis: 365
steps:
  - full_year_deduction: pct(establishment_expenditure, write_off_rate_percent)
  - deduction_2026_27: round(full_year_deduction * write_off_days / days_basis, 2)
expected:
  full_year_deduction: 6800
  deduction_2026_27: 3372.05
```

### Further positions

- **Case E: a partner with off-farm wages.** A partner in a farming partnership earns wages and plans an FMD deposit before 30 June 2027. Her taxable non-primary production income includes the wages less related deductions; her taxable primary production income is her partnership share. Keep the deduction conditional until both are known for the year, and confirm the $100,000 test is met on the final figures.
- **Case F: early withdrawal without an exception.** A deposit made on 1 August 2026 is half withdrawn on 1 March 2027 to buy feed. No rainfall or disaster evidence is supplied. The withdrawn half is taken never to have been an FMD, so it is not deductible for 2026-27; if the return has already claimed it, route the amendment. If Bureau of Meteorology records public on 1 March 2027 show rainfall within the lowest 5% for the land over the most recent 6 consecutive months they cover, the exception can be reconsidered.
- **Case G: natural increase.** A cattle breeder records 150 calves born in 2026-27 and elects the prescribed cost. If the class is valued at cost at year end, each calf carries $20; the alternative is market selling value or replacement value for that class or animal. The election must be on file by lodgment.
- **Case H: a small trust beneficiary.** A beneficiary is presently entitled to $900 of a farming trust's income. Below $1,040 she is treated as carrying on the trust's business for averaging only if the Commissioner is satisfied the interest was not acquired or granted wholly or primarily to obtain averaging; flag for the reviewer rather than assuming averaging applies.
- **Case I: a new dam partly used for the house.** A farmer builds a dam in October 2026, 80% used for stock water and 20% for the homestead garden. The cost is deductible in 2026-27 as a water facility, reduced for the part of the decline in value attributable to use that is not wholly for the business or a taxable purpose; the reviewer settles the apportionment.

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement in this guide is unresolved, and return Needs Input or refer it for qualified review.

**Topical refusals**

- **R-AU-PP-1, business status.** *Trigger:* the work depends on whether a primary production activity is a business. *Message:* "Whether this activity is a business of primary production is decided by weighing the TR 97/11 indicators; no single indicator decides it. The matrix is prepared; the reviewer decides."
- **R-AU-PP-2, FMD planning and providers.** *Trigger:* a request to time a deposit or withdrawal, or to instruct an FMD provider. *Message:* "Deposit and withdrawal timing is planning advice, and providers act only on the owner's instructions. The register and the tax effect of each option are prepared for the reviewer and the owner to decide."
- **R-AU-PP-3, carbon and forestry schemes.** *Trigger:* Australian carbon credit units, carbon sink forests, forestry managed investment schemes or carbon sequestration rights. *Message:* "These regimes are outside this guide. Refer to a practitioner who handles them; CGT on sequestration rights routes to au-capital-gains."
- **R-AU-PP-4, capital gains on farm assets.** *Trigger:* sale of farm land, water entitlements or the business. *Message:* "Capital gains and the small business concessions are handled in au-capital-gains and au-small-business-cgt."
- **R-AU-PP-5, unusual livestock.** *Trigger:* horse breeding stock valuation options (TR 2008/2) or a class with no prescribed natural increase cost. *Message:* "This class needs a cost or valuation basis this guide does not carry. Obtain actual cost records or ATO confirmation before valuing it."
- **R-AU-PP-6, companies and trusts seeking individual concessions.** *Trigger:* a company or trustee seeks an FMD or averaging, or a fixed trust with no income or a chosen beneficiary arrangement is involved (ss 392-20(3) and (4), 393-25(5) and (6)). *Message:* "FMDs and averaging belong to individuals. The trust beneficiary rules for this structure need specialist review."
- **R-AU-PP-7, grants and disaster payments.** *Trigger:* a government grant, subsidy or disaster payment whose tax status is unclear. *Message:* "Grant treatment depends on the payment's terms (TR 2006/3). Assemble the documents; the reviewer decides whether it is assessable, exempt or non-assessable non-exempt."

**Reviewer attention thresholds (guide policy, not law)**

- An FMD deposit where taxable non-primary production income is within $10,000 of $100,000, or deductions are within $5,000 of taxable primary production income.
- An owner's total FMD balance within $25,000 of $800,000.
- Any FMD repayment within 12 months of the deposit.
- Every FMD deduction: its classification as a primary production or non-primary production deduction.
- A forced disposal or death tax profit above $50,000, and any election under Subdivision 385-E, 385-F or 385-G.
- An averaging estimate that shows extra income tax, or differs from the assessment by more than $1,000.
- A change of valuation basis for a livestock class, or closing livestock value moving by more than 25% with stable head counts.

**Prohibitions**

- Never state a threshold, prescribed cost, write-off rate or tax rate from memory.
- Never treat a drought declaration as the FMD rainfall test, or a supplied exception as met before its evidence is on file.
- Never present an averaging estimate as the return or assessment figure.
- Never make or revoke an averaging choice, a natural increase election or a Subdivision 385-E, 385-F or 385-G election for the client.

## Completion checklist

- [ ] TR 97/11 matrix complete for each activity, with the reviewer's decision recorded.
- [ ] Basic taxable income, taxable primary production income and taxable non-primary production income built separately for each owner and reconciled to the business schedule.
- [ ] FMD register agrees to provider statements; each deposit tested against s 393-5 and s 393-35; each repayment tested under s 393-10 and s 393-40, with exception evidence listed.
- [ ] Averaging inputs cover the right years under s 392-40; any choice under s 392-25 or s 392-95 is evidenced; the estimate is labelled as such.
- [ ] Livestock head counts agree to movement records, values to the trading stock schedule, and opening values to last year's closing values.
- [ ] Natural increase elections and Subdivision 385-E, 385-F and 385-G elections are documented with the person and date that made them.
- [ ] Each primary production asset is classified under one provision, with the expenditure date, use, owner or lessee status and any small business choice.
- [ ] Every figure cites its source and read date; Needs Input items list the evidence needed, owner, status and next action.
- [ ] Reviewer brief additions: the business status decision, FMD exposure to amendment, averaging estimate caveat, elections made or pending, and each refusal raised.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITAA 1997 s 995-1, definition of primary production business (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/995-1 | 2026-11-02 |
| TR 97/11, paras 11 to 18 | https://www.ato.gov.au/law/view/document?docid=TXR/TR9711/NAT/ATO/00001 | 2026-11-02 |
| ITAA 1997 ss 392-5, 392-10, 392-15, 392-20, 392-25, 392-35, 392-40, 392-45, 392-50, 392-55, 392-65, 392-70, 392-75, 392-80, 392-85, 392-90, 392-95 (the s 392-90(3) formula is the image https://www.ato.gov.au/law/view/sgif/cch-leg2/graphic_24388258_20260409t173133-191.gif) | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/392-10 (and the matching docid for each section) | 2026-11-02 |
| ITAA 1997 ss 393-5, 393-10, 393-15, 393-25, 393-35, 393-37, 393-40 | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/393-5 (and the matching docid for each section) | 2026-11-02 |
| ITAA 1997 s 70-55 and ss 385-95 to 385-160 | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/385-100 (and the matching docid for each section) | 2026-11-02 |
| ITAA 1997 ss 40-515, 40-520, 40-525, 40-540, 40-545, 40-548, 40-551, 40-555, 40-630 and 328-175 | https://www.ato.gov.au/law/view/document?docid=PAC/19970038/40-515 (and the matching docid for each section) | 2026-11-02 |
| Income Tax Assessment (1997 Act) Regulations 2021, compilation 16 (27 June 2026), ss 70-55.01 and 393-40.01, and the Division 393 contents | https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| ATO, Farm management deposits scheme (updated 22 August 2025) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/primary-producers/managing-varying-income/farm-management-deposits-scheme | 2026-11-02 |
| ATO, Income averaging (updated 22 August 2025) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/primary-producers/managing-varying-income/tax-averaging | 2026-11-02 |
| ATO, Information for primary producers 2026 (2026 edition, whose year references are to 2025-26; used for principles only): depreciating assets, valuing livestock, natural increase, abnormal receipts, small business concessions | https://www.ato.gov.au/law/view/document?docid=SAV/PP | 2026-11-02 |
| ATO, Tax rates - Australian residents, 2026-27 table (updated 13 August 2026) | https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents | 2026-11-02 |

Named but not read for this guide: TR 2006/3, TR 2008/2, the ATO determination of values for goods taken from stock for 2026-27, s 40-635 (the landcare list above comes from the ATO guide) and ss 393-16, 393-17 and 393-27. Read each before relying on a position that turns on it.

Method adapted by its author from the `au-primary-production` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Topic chosen from the public Ask Nagaris skill list (names only); no Nagaris text was used.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
