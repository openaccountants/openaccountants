---
name: slovenia-income-tax
description: "Slovenian personal income tax (dohodnina) for tax year 2026 under ZDoh-2 as amended to ZINR (Uradni list RS 40/25). Covers residents and non-residents, the five-band scale (16%, 26%, 33%, 39%, 50%) with the 2026 indexed bands, the general allowance of EUR 5,551.93 and its taper for total income up to EUR 17,766.18, dependants and other allowances, capital income at 25% with 20% and 15% after 5 and 10 years and exemption after 15, rent at 25% with 10% standard costs, sole proprietors (s.p.) on normed expenses at 20% (pointer), the informative calculation (informativni izračun) and its 15-day objection, advance tax and fines. Trigger on: dohodnina, informativni izračun, ugovor, splošna olajšava, Doh-KDVP, Doh-Div, rent tax Slovenia. Out of scope: si-cross-border (7% new-resident relief, non-residents), slovenia-payroll, slovenia-social-contributions, si-corporate-income-tax, slovenia-tax-optimization."
version: 0.3
jurisdiction: SI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia: personal income tax (dohodnina) 2026 v0.3

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from the Personal Income Tax Act (ZDoh-2) and the Tax Procedure Act (ZDavP-2) as consolidated on pisrs.si, the amending act ZDoh-2AB (Uradni list RS 104/24), and the Financial Administration (FURS) notice of the 2026 scale and allowances, all read on 24 October 2026. It prepares working papers; it is not authority to file or pay.

Related skills in this pack:

- Residence, non-residents, treaties and the 7% relief for new residents under 40: [si-cross-border](si-cross-border.md).
- Monthly withholding (akontacija) by the employer and the REK forms: [slovenia-payroll](slovenia-payroll.md).
- Contribution rates for employees and the self-employed: [slovenia-social-contributions](slovenia-social-contributions.md).
- Companies: [si-corporate-income-tax](si-corporate-income-tax.md). Planning, including the s.p. against d.o.o. choice: [slovenia-tax-optimization](slovenia-tax-optimization.md).

## Who this applies to

- **Residents** pay dohodnina on worldwide income. Residence (registered permanent residence, habitual abode, centre of interests, more than 183 days) is in ZDoh-2 arts. 6 and 7 and is worked through in [si-cross-border](si-cross-border.md).
- **Non-residents** pay only on Slovenian-source income. A resident of another EU or EEA state can claim the resident allowances (arts. 111 to 114 and 117) if Slovenian employment, business, royalty and other income is at least 90% of their total taxable income for the year (ZDoh-2 art. 116, as amended for tax years from 2025).
- **Part-year residents** (the year someone arrives or leaves) get the allowances and the band amounts pro rata to the period of residence (ZDoh-2 art. 121).
- **Three tax tracks.** Most income goes into one annual base taxed on the scale: employment, business income on actual expenses, basic farming, royalties and other income (ZDoh-2 arts. 109 and 119). Three kinds of income stay out of the annual base and are taxed at flat, final rates (ZDoh-2 art. 131.a):
  1. capital income (interest, dividends, capital gains, and individual investment account income);
  2. business income of a sole proprietor (s.p.) who uses normed expenses;
  3. rental income.

## Rates, bands and thresholds

The band amounts and allowances are indexed each year by a ministerial rule if the budget implementation act provides for it (ZDoh-2 arts. 118 and 122(2) and (3)). For 2026 they are set by the Pravilnik o določitvi usklajenih zneskov olajšav, enačbe za določitev olajšave in lestvice za odmero dohodnine za leto 2026 (Uradni list RS 104/25), as published by FURS on 15 December 2025.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Band 1: net annual base up to EUR 9,721.43 | 16% | 2026 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Letna_odmera_dohodnine/Opis/Lestvica_za_leto_2026.docx |
| Band 2: EUR 9,721.43 to 28,592.44 | EUR 1,555.43 + 26% over 9,721.43 | 2026 | same FURS notice |
| Band 3: EUR 28,592.44 to 57,184.88 | EUR 6,461.89 + 33% over 28,592.44 | 2026 | same FURS notice |
| Band 4: EUR 57,184.88 to 82,346.23 | EUR 15,897.40 + 39% over 57,184.88 | 2026 | same FURS notice |
| Band 5: over EUR 82,346.23 | EUR 25,710.33 + 50% over 82,346.23 | 2026 | same FURS notice |
| Monthly scale for the main employer: band limits | EUR 810.12 / 2,382.70 / 4,765.41 / 6,862.19 | 2026 | same FURS notice; ZDoh-2 art. 127(2) |
| General allowance (splošna olajšava) | EUR 5,551.93 | 2026 | same FURS notice; ZDoh-2 art. 111(1) |
| Extra general allowance where total income is up to EUR 17,766.18 | 20,832.39 minus 1.17259 times total income, added to the EUR 5,551.93 | 2026 | same FURS notice; ZDoh-2 art. 111(3) |
| First dependent child | EUR 2,995.83 | 2026 | same FURS notice; ZDoh-2 art. 114 |
| Second / third / fourth / fifth child | EUR 3,256.77 / 5,432.02 / 7,607.27 / 9,782.51 | 2026 | same FURS notice |
| Each further child | previous child's amount plus EUR 2,175.25 | 2026 | same FURS notice |
| Child needing special care | EUR 10,856.24 | 2026 | same FURS notice |
| Other dependent family member | EUR 2,995.83 | 2026 | same FURS notice |
| Disabled person with 100% impairment and a right to care | EUR 20,196.38 | 2026 | same FURS notice; ZDoh-2 art. 112(1) |
| Age 70 or over; 10-year volunteer rescuer | EUR 1,665.58 | 2026 | same FURS notice; ZDoh-2 art. 112(8) |
| Pupil or student, on student work through an authorised agency, up to age 26 | EUR 3,886.35 | 2026 | same FURS notice; ZDoh-2 art. 113(3) |
| Employee up to and including the year they turn 29 | EUR 1,443.50 a year, pro rata per full month employed | 2026 | same FURS notice; ZDoh-2 art. 113(6) |
| Voluntary supplementary pension premium | up to 24% of employee pension contributions (5.844% of a pension), max EUR 3,224.18 | 2026 | same FURS notice; ZDoh-2 art. 117 |
| Pension credit | 13.5% of the pension, off the tax | 2026 | ZDoh-2 art. 112(3), https://pisrs.si/pregledPredpisa?id=ZAKO4697 |
| New residents under 40 | 7% of salary off the tax, up to 5 years | tax years from 2025 | ZDoh-2 art. 113.a; see [si-cross-border](si-cross-border.md) |
| Interest, dividends, capital gains | 25%, final | 2026 | ZDoh-2 art. 132(1) |
| Capital gains after 5 / 10 years held | 20% / 15% | 2026 | ZDoh-2 art. 132(2) |
| Capital gains after 15 years held | exempt | 2026 | ZDoh-2 art. 96(1) |
| Interest on EU bank deposits and Slovenian retail bonds issued 2024 to 2026 | first EUR 1,000 a year exempt | 2026 | ZDoh-2 art. 133 |
| Individual investment account (INR) payout | 15%, final; exempt for a payout made at least 15 years after opening (or after the last payout) | from 5 March 2026 | ZDoh-2 arts. 104.b and 132(3); ZINR art. 45 |
| Rent | 25% final, on rent less 10% standard costs | 2026 | ZDoh-2 arts. 77 and 135.č |
| Royalties | 10% standard costs; 25% advance tax | 2026 | ZDoh-2 arts. 79 and 130 |
| s.p. on normed expenses | 20% final | 2026 | ZDoh-2 art. 135.a |
| Normed expenses, full-time self-insured s.p. | 80% of revenue up to EUR 60,000; none on revenue above | from 2025 | ZDoh-2 art. 59(1) |
| Normed expenses, other s.p. | 80% up to EUR 12,500; 40% from 12,500 to 30,000; none above | from 2025 | ZDoh-2 art. 59(2) |
| Entry test for normed expenses | prior-year revenue up to EUR 30,000, or EUR 60,000 if full-time self-insured for 9 months | from 2025 | ZDoh-2 art. 48(3) |
| Advance tax at a secondary employer; contract work | 25% | 2026 | ZDoh-2 art. 127(6) and (10) |

## The taxable base

**The annual base.** Add up the year's employment, business (actual expenses), basic farming, royalty and other income, each net of its own deductions. Take off the allowances. The result is the net annual base, taxed on the 2026 scale (ZDoh-2 art. 119). Tax withheld or paid in advance during the year is credited (art. 123).

**Employment.** The base is gross employment income less the employee's compulsory social contributions (ZDoh-2 art. 41(1)). These include the 1% long-term care contribution and the flat monthly compulsory health contribution (OZP: EUR 37.17 a month in January and February 2026, EUR 39.36 from March, so EUR 467.94 for a full year 2026), both compulsory social security contributions the employee must pay (ZPSV art. 1; ZZVZZ art. 48; ZDOsk-1 arts. 51(2) and 56.a(1)). Contribution rates are in [slovenia-social-contributions](slovenia-social-contributions.md).

**The general allowance and its taper.** Every resident gets EUR 5,551.93 in 2026, unless another resident claims them as a dependant (art. 111(1)). If total income is up to EUR 17,766.18, the resident also gets 20,832.39 minus 1.17259 times total income. The extra amount falls to nil at EUR 17,766.18 (art. 111(3) and the 2026 FURS notice). Total income means employment, business (but not s.p. income on normed expenses), basic farming, royalty and other income, leaving out exempt income. The law counts the income itself, not the base after contributions (arts. 37 and 111(3)). Business income counts as profit before contributions (art. 111(4)).

**Dependants.** A child counts up to 18. A child up to 26 still counts while in education, not employed, not in business and with own income below the dependant allowance (student work, scholarships and family pension do not count as own income). A spouse who is not employed, not in business and has own income below the dependant allowance can also count, and so can parents registered at the same permanent address with income below that allowance (ZDoh-2 art. 115(1), (3) and (9)). Only one parent takes the full amount for a child. The other gets any difference, and the amount is split pro rata if the parents do not agree (art. 114(10) and (11)). Only the months the child was actually supported count (art. 114(9)).

**Capital gains.** These are taxed at a separate rate and never enter the annual base (art. 131.a).

- **Base.** The gain is disposal value less acquisition value. If positive, deduct standard costs: the lower of 1% of cost plus 1% of proceeds, or the gain itself (ZDoh-2 art. 97(1)). Cost includes improvements to real estate and the inheritance, gift or transfer tax paid on acquisition (art. 98).
- **Rate by holding period.** 25% up to 5 years, 20% after 5 years, 15% after 10 years, and exempt after 15 years (arts. 132(2) and 96(1)).
- **Other exemptions.** A home lived in and registered as the permanent residence for the last three years is exempt, and so is the sale of debt securities (art. 96(2)).
- **Losses.** Losses net against gains of the same year only. The one exception is a loss on shares held before a bonus issue from company funds, which can be carried forward (art. 97(3)). A loss on an exempt disposal does not count (art. 96(3)). A loss is blocked if the same securities are bought back within 30 days, or bought by a family member or a 25% related company (art. 97(2) to (5)).
- **Mixed holding periods.** When gains of different holding periods remain after losses, the net gain is split pro rata between them (art. 97(4)).

**Dividends and interest.** Taxed at 25% final (art. 132(1)). A Slovenian payer of dividends withholds the tax within five days of payment (ZDavP-2 art. 325(4)). Interest on deposits at Slovenian and other EU banks, and on Slovenian government retail bonds issued in 2024 to 2026, is not withheld. FURS assesses it on the resident's return (ZDavP-2 art. 325(7)). That interest is exempt up to EUR 1,000 a year in total (ZDoh-2 art. 133), and no return is needed if the total is EUR 1,000 or less (ZDavP-2 art. 326(2)). Interest on other Slovenian government securities and on listed Slovenian corporate bonds is also assessed on a return, not withheld (ZDavP-2 art. 325(8)).

**Individual investment account (INR).** This account came in with ZINR (Uradni list RS 40/25, published 4 June 2025). ZINR came into force the next day and applies nine months later, so from 5 March 2026 (ZINR art. 45). Only the return is taxed, and only when it is paid out: the payout up to the account value less deposits (ZDoh-2 art. 104.c). The rate is 15% final (art. 132(3)), withheld by the INR provider within five days of the payout (ZDavP-2 art. 325(12)). The first payout made at least 15 years after the account was opened, with no payout before it, is exempt; so is a payout made at least 15 years after the previous one (ZDoh-2 art. 104.b).

**Rent.** The base is rent less 10% standard costs. The landlord can instead claim the actual upkeep costs they paid, with invoices (ZDoh-2 art. 77(1) and (2)). Farm or forest land has no cost deduction. Subletting is taxed on the sublet rent less the rent paid. The tax is 25% final (art. 135.č). Rent and capital income stay out of the annual base (art. 131.a); there is no election to add them in.

**Sole proprietor (s.p.).** Business profit is revenue less expenses under corporate tax rules (ZDoh-2 art. 48(1) and (2)).

- **Actual expenses.** The profit joins the annual base and is taxed on the scale.
- **Normed expenses.** The s.p. can elect normed expenses instead if prior-year revenue was up to EUR 30,000, or up to EUR 60,000 with full-time self-employment insurance for at least nine months (art. 48(3), amended by ZDoh-2AB from 2025). A new business can elect for its first year, and also for its second year if it started in the last six months of the first (art. 48(4)). The new business elects within eight days of registration (ZDavP-2 art. 308(2)).
- **Forced exit for 2026.** An s.p. must use actual expenses and keep full books for 2026 if its 2025 revenue exceeded EUR 60,000 (full-time self-insured for nine months in 2025) or EUR 30,000 (otherwise) (ZDoh-2AB art. 23(b)). The deduction is set by art. 59 (see the table above). The remaining profit is taxed at 20% final (art. 135.a).
- **Pointer only.** This skill does not cover business expenses, depreciation, reliefs or the s.p. against d.o.o. choice. Use [slovenia-tax-optimization](slovenia-tax-optimization.md) and [si-corporate-income-tax](si-corporate-income-tax.md), whose base rules ZDoh-2 art. 48(2) borrows.

**Changes for 2025 and 2026.**

- **ZDoh-2AB (Uradni list RS 104/24), from tax year 2025** (ZDoh-2AB art. 27(1)):
  - lowered the normed-expense entry threshold from EUR 50,000 to 30,000, and for farm households from EUR 100,000 to 60,000 (art. 48);
  - rewrote the normed-expense scale (art. 59);
  - added the 7% relief for new residents (art. 113.a);
  - raised the dependant amounts (art. 114, indexed for 2025 under ZDoh-2AB art. 26);
  - dropped the extra proof test for EU and EEA non-residents (art. 116).
- **ZDoh-2AB, from tax year 2026:** it deletes art. 42(1), the special base for public servants and officials posted abroad, who were taxed only on the pay they would have received for the same work in Slovenia (ZDoh-2AB arts. 7 and 27(1); old text in the ZDoh-2 consolidated text NPB33).
- **ZINR (Uradni list RS 40/25):** added the INR regime, applying from 5 March 2026 (ZINR art. 45).

The PISRS register lists no amendment to ZDoh-2 after ZINR as of 24 October 2026.

**Foreign tax credit.** A resident deducts foreign tax on foreign income, up to the lower of the foreign tax actually paid and the Slovenian tax on that income. Under a treaty, the credit is capped at the treaty rate. Unused credit is lost (ZDoh-2 arts. 136, 137 and 140). Details are in [si-cross-border](si-cross-border.md).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Send FURS data for allowances (dependants) so the informative calculation includes them | by 15 February 2027 for 2026 | ZDavP-2 art. 270(2) |
| Return for interest, dividends and rent not taxed at source (for example a foreign payer, or a private tenant), and for capital gains on securities | by 28 February 2027 for 2026 | ZDavP-2 arts. 325(5) and 326(1) |
| Capital gain on real estate | return within 15 days of the sale | ZDavP-2 art. 326(3) |
| Claim actual rent costs where the tenant withheld tax | by 28 February 2027 | ZDavP-2 art. 329.a(1) |
| FURS decision on the 28 February returns | by 30 April | ZDavP-2 art. 330(2) |
| s.p. annual tax return (davčni obračun) | by 31 March 2027 for 2026; balance due within 30 days of that date | ZDavP-2 arts. 297(2) and 301 |
| s.p. election of normed expenses | by 31 March of the year concerned | ZDavP-2 art. 308 |
| FURS sends the informative calculation (informativni izračun) | by 31 May 2027 | ZDavP-2 art. 267(3) |
| Objection (ugovor) to the informative calculation | within 15 days of delivery, with a corrected calculation | ZDavP-2 art. 267(4) and (5) |
| No informative calculation received by 15 June | file a return (napoved) by 31 July 2027 | ZDavP-2 art. 267(6) |
| Leaving Slovenia before 31 July | return for the resident period by the date of departure | ZDavP-2 art. 269(2) |
| EU or EEA non-resident claiming resident allowances | return by 31 July of the second year after the tax year (31 July 2028 for 2026) | ZDavP-2 arts. 269(1) and 270(3) |
| FURS decision after an objection or return | by 31 October | ZDavP-2 art. 276 |
| Paying an assessment | within 30 days of delivery of the decision | ZDavP-2 art. 66 |

**The informative calculation.** FURS prepares it from the data it holds. If the resident does not object within 15 days of delivery, it becomes their return and then the assessment decision, and the right of appeal is treated as waived (ZDavP-2 art. 267(3)). To claim foreign tax credits or treaty exemptions, the resident must claim them in the objection or the return (art. 273(1) and art. 274(1)). A treaty credit can also be claimed on appeal (art. 273(5)). Dependants can be added in the objection (art. 271(1)). A difference of EUR 2 or less is not collected (art. 277).

**Advance tax (akontacija) during the year.**

- **Main employer.** The employer withholds on the monthly scale, applying one twelfth of the allowances (ZDoh-2 art. 127(2) and (3)).
- **Secondary employer and contract work.** These withhold 25% with no allowances (art. 127(6) and (10)).
- **Withholding payers.** A payer pays the tax withheld within five days of paying the income (ZDavP-2 art. 283(1)).
- **s.p. advance tax.** The s.p. pays advance tax equal to the last year's tax. It is paid monthly if over EUR 400, otherwise quarterly. Each instalment falls due on the last day of its period and must be paid within 20 days (ZDavP-2 art. 298(1), (3) and (4)). The s.p. can ask FURS to change the amount at least 30 days before an instalment falls due (art. 299).

Returns are filed on eDavki.

## Penalties and interest

| Breach | Fine or charge | Source |
|---|---|---|
| Individual: return not filed on time or in the set way (including the 31 July return and the capital income returns) | EUR 250 to 400 | ZDavP-2 art. 394 |
| Individual: false, wrong or incomplete data in a return | EUR 400 to 5,000 | ZDavP-2 art. 395 |
| s.p.: tax return not filed, filed late, or wrong; books not kept | EUR 800 to 10,000 | ZDavP-2 art. 397(1) |
| Tax found in an audit | interest at 7% a year from the due date to the decision | ZDavP-2 art. 95 |
| Late payment | default interest at the ECB main refinancing rate plus 8 points, reset each half-year: 10.15% for January to June 2026 (ECB rate 2.15%) and 10.40% for July to December 2026 | ZDavP-2 art. 96(1); ZPOMZO-1 art. 2; minister's notice, Uradni list RS 1124/2026 |

There is no fine for a late return if the tax is paid under a voluntary disclosure (samoprijava, ZDavP-2 art. 63). There is no fine for wrong data if the return is corrected under art. 64 (ZDavP-2 art. 396).

## Cross-border points

- **Residence and part-year rules** are in [si-cross-border](si-cross-border.md). In the year of arrival or departure, the allowances and the bands are pro rata to the resident period (ZDoh-2 art. 121).
- **Foreign income of a resident** goes into the informative calculation only if FURS has the data. The resident must add it, and claim the foreign tax credit, in the objection or a return. Foreign dividends, interest and rent go on the 28 February return (ZDavP-2 arts. 273, 326 and 328).
- **EU and EEA non-residents** with at least 90% of their taxable income from Slovenia can claim resident allowances by filing a return (ZDoh-2 art. 116; ZDavP-2 arts. 269(1) and 270(3)).
- **New residents under 40** with a salary of at least twice the average salary get 7% of salary off their tax for up to five years (ZDoh-2 art. 113.a). The conditions are in [si-cross-border](si-cross-border.md).
- **Non-residents selling Slovenian securities** file within 15 days of the sale, or for all sales of the year by 28 February (ZDavP-2 art. 326(4)).

## Worked examples

**Example 1: employee with a flat let to a private tenant (2026).** A resident employee earns gross salary of EUR 36,000. Employee contributions are 23.1% of gross (15.5% pension, 6.36% health, 0.14% unemployment, 0.1% parental, 1% long-term care), so EUR 8,316. The example leaves out the OZP to keep the figures simple; on a full year it also reduces the employment base, by EUR 467.94. There are no dependants. The employee also lets a flat to a private individual for EUR 12,000 a year. A private tenant is not a withholding payer, so the landlord files a rent return by 28 February 2027.

- The employment base is 36,000 less 8,316 = EUR 27,684.
- Total income is over EUR 17,766.18, so only the general allowance of EUR 5,551.93 applies.
- The net annual base is EUR 22,132.07. It falls in band 2: 1,555.43 + 26% of (22,132.07 less 9,721.43) = EUR 4,782.20.
- The monthly withholding by the main employer is credited against this in the informative calculation.
- The rent is outside the annual base. The base is 12,000 less 10% standard costs = EUR 10,800. Tax at 25% is EUR 2,700.

```oa-check
name: Slovenian employee with rental income, 2026 scale
inputs:
  gross_salary: 36000
  employee_contributions: 8316
  general_allowance: 5551.93
  rent: 12000
steps:
  - employment_base: gross_salary - employee_contributions
  - net_base: employment_base - general_allowance
  - annual_tax: 1555.43 + (net_base - 9721.43) * 0.26
  - rent_base: rent * 0.90
  - rent_tax: rent_base * 0.25
expected:
  employment_base: 27684
  net_base: 22132.07
  annual_tax: 4782.20
  rent_base: 10800
  rent_tax: 2700
```

**Example 2: low earner with a child and a share sale (2026).** A resident employee earns gross salary of EUR 17,000. Employee contributions at 23.1% are EUR 3,927. As in Example 1 the OZP is left out; on a full year it also reduces the employment base, by EUR 467.94. They support one child all year and claim the child. They also sell shares bought 7 years ago for EUR 20,000, for EUR 30,000.

- Total income of EUR 17,000 is under the EUR 17,766.18 limit, so the extra general allowance applies: 20,832.39 less 1.17259 times 17,000 = EUR 898.36. The total general allowance is 5,551.93 + 898.36 = EUR 6,450.29.
- The employment base is EUR 13,073. Less the general allowance and the first-child allowance of EUR 2,995.83, the net base is EUR 3,626.88.
- All of it is in band 1 at 16%, so the tax is EUR 580.30.
- The gain is EUR 10,000. The standard costs are the lower of 1% of 20,000 plus 1% of 30,000 (EUR 500) and the gain, so EUR 500, leaving a base of EUR 9,500.
- After 5 but under 10 years of holding the rate is 20%, so the tax on the gain is EUR 1,900. It is reported on the capital gains return by 28 February 2027.

```oa-check
name: Slovenian low earner with child and 7-year share gain, 2026
inputs:
  gross_salary: 17000
  employee_contributions: 3927
  general_allowance: 5551.93
  child_allowance: 2995.83
  cost: 20000
  proceeds: 30000
steps:
  - extra_allowance: max(20832.39 - 1.17259 * gross_salary, 0)
  - total_general: general_allowance + extra_allowance
  - employment_base: gross_salary - employee_contributions
  - net_base: max(employment_base - total_general - child_allowance, 0)
  - annual_tax: min(net_base, 9721.43) * 0.16
  - gain: proceeds - cost
  - standard_costs: min(cost * 0.01 + proceeds * 0.01, gain)
  - gain_base: gain - standard_costs
  - gain_tax: gain_base * 0.20
expected:
  extra_allowance: 898.36
  total_general: 6450.29
  employment_base: 13073
  net_base: 3626.88
  annual_tax: 580.30
  gain_base: 9500
  gain_tax: 1900
```

## Ask the client first

1. Were you a Slovenian resident for the whole of 2026? If you arrived or left, on what dates, and were you under 40 when you started work here?
2. What income did you have, by type? That means salary (main or secondary employer), contract work, s.p. business (actual or normed expenses), rent, dividends, interest, share or property sales, and any income from abroad.
3. Who do you support, and for which months? Does the other parent claim any of the children?
4. For each sale of shares or property: the purchase date and cost, the sale date and price, and whether you lived in the property.
5. Has FURS delivered your informative calculation, and on what date? The 15-day objection period runs from delivery.
6. Did you pay tax abroad on any income? Do you have the foreign tax certificates?

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Act (ZDoh-2), unofficial consolidated text NPB36 up to ZINR (Uradni list RS 40/25): arts. 37, 41, 42, 46 to 48, 59, 77 to 80, 96 to 98, 104.a to 104.c, 111 to 123, 127, 128, 130 to 140 | https://pisrs.si/pregledPredpisa?id=ZAKO4697 | 2026-10-24 |
| PISRS register entry for ZDoh-2 (amendment list, last entry 40/25 ZINR) | https://pisrs.si/api/rezultat/zbirka/id/ZAKO4697 | 2026-10-24 |
| ZDoh-2AB, Uradni list RS 104/24 (amendments; arts. 23, 26 and 27 on transition and start dates) | https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2024-01-3309 | 2026-10-24 |
| FURS, notice of the 2026 income tax scale and allowances (15 December 2025, under the Pravilnik in Uradni list RS 104/25) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Dohodnina/Letna_odmera_dohodnine/Opis/Lestvica_za_leto_2026.docx | 2026-10-24 |
| FURS, annual income tax assessment page | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/letna_odmera_dohodnine/ | 2026-10-24 |
| ZDoh-2, unofficial consolidated text NPB33 (up to ZORZFS, before ZDoh-2AB): old art. 42(1) | https://pisrs.si/api/datoteke/integracije/9340577 (NPB 33 version in the PISRS register for ZAKO4697) | 2026-10-24 |
| Individual Investment Accounts Act (ZINR), Uradni list RS 40/25: art. 45 (entry into force and start of application) | https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-1572 | 2026-10-24 |
| Prescribed Default Interest Rate Act (ZPOMZO-1): art. 2 | https://pisrs.si/pregledPredpisa?id=ZAKO3695 | 2026-10-24 |
| Minister of Finance, rate of default interest from 1 July 2026 (10.40%), Uradni list RS 1124/2026 | https://pisrs.si/api/uradni-list/objava/u20261124.pdf | 2026-10-24 |
| ECB key interest rates (main refinancing rate 2.15% from 11 June 2025, 2.40% from 17 June 2026) | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-24 |
| Social Security Contributions Act (ZPSV) art. 1 and arts. 8 to 13 rates, and Long-Term Care Act (ZDOsk-1) arts. 51(2), 56 and 56.a(1), for the example contribution rates and their deduction | https://pisrs.si/pregledPredpisa?id=ZAKO984 and https://pisrs.si/pregledPredpisa?id=ZAKO8819 | 2026-10-24 |
| Health Care and Health Insurance Act (ZZVZZ) art. 48 (OZP), and FURS self-employed contribution tables SZ 1/2026 and SZ 3/2026 for the OZP of EUR 37.17 and EUR 39.36 | https://pisrs.si/pregledPredpisa?id=ZAKO213 and https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost/ | 2026-10-24 |
| Tax Procedure Act (ZDavP-2), unofficial consolidated text up to ZDavP-2P (Uradni list RS 100/25) and decision U-I-148/25: arts. 63, 64, 66, 95, 96, 267 to 277, 283, 297 to 301, 308, 325 to 330, 394 to 397 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-24 |

Not yet confirmed: FURS practice on whether "total income" for the allowance taper is gross pay (the reading used here, from arts. 37 and 111(3) and the FURS monthly table, which uses gross pay). The eDavki form codes Doh-KDVP and Doh-Div, which are FURS names and are not in the statute. The 2027 indexation, not yet published.

> Contributed by Michael Cutajar.

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
