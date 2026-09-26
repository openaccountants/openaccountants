---
name: au-working-holiday-makers
description: >
  Use this skill for any Australian working holiday maker (WHM) tax question for
  holders of subclass 417 Working Holiday or 462 Work and Holiday visas and their
  employers: employer registration, Schedule 15 withholding and the $45,000
  threshold, unregistered employer rates, no-TFN withholding, STP income type
  and tax treatment codes, superannuation guarantee, the departing Australia
  superannuation payment (DASP) and its 65% tax, residency, the
  non-discrimination article countries after Addy, and whether a return is
  needed. Trigger on "backpacker tax", "working holiday maker",
  "417 visa tax", "462 visa tax", "WHM employer registration", "Schedule 15",
  "DASP", "backpacker super refund". Covers 2026-27.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 income year (1 July 2026 to 30 June 2027)"
last_updated: 2026-09-27
review_status: pending_review
depends_on:
  - australia-payroll
  - au-super-guarantee
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Working Holiday Makers

## Australia Working Holiday Makers v1.0

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| Who is a WHM | A holder of a subclass 417 Working Holiday or 462 Work and Holiday visa, or an associated bridging visa while a further 417 or 462 application is decided |
| Registered employer withholding | 15% on the first $45,000 paid to the worker in the income year, then 30% to $135,000, 37% to $190,000 and 45% above |
| Unregistered employer withholding | Foreign resident rates: 30% from the first dollar to $135,000 |
| No TFN | 45% of every payment, ignoring cents |
| Tax on assessment | 15% to $45,000; $6,750 plus 30% to $135,000; $33,750 plus 37% to $190,000; $54,100 plus 45% above |
| Tax-free threshold, offsets, Medicare levy adjustments | None for WHM withholding |
| Superannuation guarantee | 12% of ordinary time earnings, with choice of fund |
| Departing Australia superannuation payment | Taxed at 65% for a WHM, claimed after leaving Australia, not included in a tax return |
| Lodgment | No return needed where the only income is WHM salary or wages under $45,001 |
| STP reporting | Income type WHM with the country of nationality; tax treatment code H with R, U or F |
| Tax authority | Australian Taxation Office |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The employer workflow

**Step 1. Register before the first payment.**
An employer of a 417 or 462 visa holder must be registered for PAYG withholding and then register
as an employer of working holiday makers. Penalties apply for failing to register. See Section 4.

**Step 2. Check the visa.**
Confirm work rights and the visa subclass through Visa Entitlement Verification Online (VEVO).

**Step 3. Take a TFN declaration.**
The worker declares that they are a working holiday maker. Withhold at WHM rates even if they do
not, provided the visa is a 417 or 462.

**Step 4. Withhold under Schedule 15.**
Track total payments to each worker for the income year and move up the rate scale as the
cumulative total passes each threshold. See Section 3.

**Step 5. Pay superannuation.**
Superannuation guarantee applies as for any employee. See Section 6.

**Step 6. Report through STP.**
Income type WHM with the worker's country of nationality, or payment type code H on a payment
summary. See Section 5.

**Step 7. Handle changes.**
A worker who moves to another visa stops being a WHM from that date; withhold under the ordinary
tables and report a second income type from then.

## Section 3 - Withholding and tax rates for 2026-27

**Working holiday maker income tax rates and Schedule 15 coefficients**

| Taxable income | Tax on this income | Withholding coefficient (a) |
| --- | --- | --- |
| $0 to $45,000 | 15 cents for each $1 | 0.15 |
| $45,001 to $135,000 | $6,750 plus 30 cents for each $1 over $45,000 | 0.30 |
| $135,001 to $190,000 | $33,750 plus 37 cents for each $1 over $135,000 | 0.37 |
| $190,001 and over | $54,100 plus 45 cents for each $1 over $190,000 | 0.45 |

- **Registered employers** — Withhold a flat 15% from the first dollar up to $45,000 of total payments to the worker in the income year, then apply the next coefficient to whole pays once the cumulative total has passed each threshold. In the ATO's example a worker whose payments passed $45,000 in April is withheld at 30% on the whole of May's pay. The formula is withholding equals the coefficient multiplied by the pay ignoring cents, rounded to the nearest dollar.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **All payments** — Schedule 15 covers every payment to a WHM: salary and wages, allowances, the taxable component of an employment termination payment, unused leave, return to work payments, back payments, commissions, bonuses and payments to actors and entertainers. Do not use Schedule 7 or Schedule 11 for a WHM.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **Unregistered employers** — An employer that has not registered must withhold at foreign resident rates, which start at 30% from the first dollar up to $135,000, and may be penalised for not registering.  _([ATO, Employer registration for working holiday makers](https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/registration-obligations-for-businesses/work-out-which-registrations-you-need/taxation-registrations/employer-registration-for-working-holiday-makers))_
- **No TFN** — Withhold 45% of every payment, ignoring cents, where the worker has not quoted a TFN, claimed an exemption or advised that they have applied for one; a worker who has applied has 28 days to provide it.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **No adjustments** — A WHM cannot claim the tax-free threshold, tax offsets or Medicare levy adjustments through withholding, cannot have a study and training support loan debt and cannot receive lump sum B payments. Ignore any offset or Medicare claim on the declaration.  _([ATO, Schedule 15](https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers))_
- **Variations** — Only a PAYG withholding variation notice from the ATO changes the rate, for example for a resident WHM from a non-discrimination article country. See Section 7.  _([ATO, Employers of working holiday makers](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/hiring-a-new-worker/employers-of-working-holiday-makers))_
- **Income tax rates** — The 2025-26 and 2026-27 scales are identical. Earlier years used $37,000 and $120,000 thresholds and a 32.5% second rate, so a prior-year return must use the table for that year.  _([ATO, Tax rates: working holiday maker](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-working-holiday-makers))_

## Section 4 - Employer registration

- **Who must register** — Any employer who employs, or plans to employ, a 417 or 462 visa holder, before making the first payment. The business must already be registered for PAYG withholding.  _([ATO, Employer registration for working holiday makers](https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/registration-obligations-for-businesses/work-out-which-registrations-you-need/taxation-registrations/employer-registration-for-working-holiday-makers))_
- **How** — Online through the ATO's Working Holiday Maker Employer Registration Form, through a registered tax or BAS agent, or by phone as an authorised business contact. A PAYG withholding branch can be registered with the branch application form.  _([ATO, Employer registration for working holiday makers](https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/registration-obligations-for-businesses/work-out-which-registrations-you-need/taxation-registrations/employer-registration-for-working-holiday-makers))_
- **Check and cancel** — The registration shows on the Australian Business Register, and can be cancelled by phoning the ATO business line on 13 28 66.  _([ATO, Employer registration for working holiday makers](https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/registration-obligations-for-businesses/work-out-which-registrations-you-need/taxation-registrations/employer-registration-for-working-holiday-makers))_
- **Contractors** — A WHM who is an employee on the facts must be taxed under Schedule 15 even if they quote an ABN; treating an employee as a contractor attracts penalties.  _([ATO, Employers of working holiday makers](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/hiring-a-new-worker/employers-of-working-holiday-makers))_

## Section 5 - Reporting

- **STP Phase 2** — Report the income type WHM and the worker's home country, which is the country of nationality on the visa. The tax treatment code starts with H, followed by R for a registered employer, U for an unregistered employer or F where no TFN declaration was provided, with no study loan or Medicare levy variation characters.  _([ATO, How to report employment and tax information through STP Phase 2](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines/how-to-report-employment-and-tax-information-through-stp-phase-2))_
- **Payment summaries** — An employer not reporting through STP gives every WHM a payment summary showing all payments in the gross section with H in the gross payment type box, and two payment summaries where the worker changed visa during the year.  _([ATO, Employers of working holiday makers](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/hiring-a-new-worker/employers-of-working-holiday-makers))_
- **Income statement** — The worker sees year-to-date income, tax withheld and super in ATO online services through myGov, and uses it to decide whether to lodge.  _([ATO, Working holiday makers](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/working-holiday-makers))_

## Section 6 - Superannuation and the departing Australia superannuation payment

- **Super guarantee** — A WHM is entitled to super like any other employee, at 12% of ordinary time earnings, and must be offered a choice of fund.  _([ATO, Super guarantee](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee))_
- **DASP eligibility** — After leaving Australia a former temporary resident can claim their super as a departing Australia superannuation payment once the visa has ceased and no other active visa is held, unless they are an Australian or New Zealand citizen or a permanent resident. Applications are made online free of charge and can be started before departure; a paper application to a fund may attract a fee and, above $5,000, a certification of immigration status from Home Affairs.  _([ATO, Departing Australia superannuation payment (DASP)](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/temporary-residents-and-superannuation/departing-australia-superannuation-payment-dasp))_
- **DASP tax** — A final withholding applies when the payment is made: nil on the tax-free component and 65% on the taxable component where the fund holds contributions made while the person held a 417 or 462 visa or an associated bridging visa. The 65% rate then applies to the whole payment, including super earned on another visa. The ordinary rates are 35% on a taxed element and 45% on an untaxed element.  _([ATO, Departing Australia superannuation payment (DASP)](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/temporary-residents-and-superannuation/departing-australia-superannuation-payment-dasp))_
- **Not assessable** — A DASP is not included in a tax return. The fund or the ATO issues a DASP payment summary within 14 days, with an H indicator where the WHM rate applied, and pays within about 28 days of a complete application.  _([ATO, Departing Australia superannuation payment (DASP)](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/temporary-residents-and-superannuation/departing-australia-superannuation-payment-dasp))_
- **Unclaimed super** — Six months after the person leaves with a ceased visa, the fund transfers the balance to the ATO as unclaimed super, which can still be claimed as a DASP.  _([ATO, Departing Australia superannuation payment (DASP)](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/temporary-residents-and-superannuation/departing-australia-superannuation-payment-dasp))_

## Section 7 - Residency and the non-discrimination article countries

- **Most WHMs are foreign residents** — The Commissioner's long-standing view is that a person who comes to Australia for a holiday and works to fund it is a visitor, not a resident, whatever the length of stay. Residency can start when the purpose changes, for example on committing to employer sponsorship or applying for a permanent visa.  _([ATO, Australian residency if you're on a working holiday or visit](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/australian-residency-if-you-re-on-a-working-holiday-or-visit))_
- **Factors** — Purpose of the stay, living arrangements, community ties, location of assets and family ties in Australia are weighed together, against arrangements to return home, study or employment to go back to and continuing connections abroad.  _([TR 2023/1 Income tax: residency tests for individuals](https://www.ato.gov.au/law/view/document?DocID=TXR/TR20231/NAT/ATO/00001))_
- **The Addy decision** — A WHM who is both an Australian resident for tax purposes and a national of an eligible non-discrimination article country is taxed on the lower of the WHM basis and the basis that applies to a resident Australian national. The eligible countries are Chile, Finland, Germany, Israel (from 2020-21), Japan, Norway, Turkey and the United Kingdom; Iceland's treaty excludes WHM rates from its article.  _([ATO, Taxation of Australian resident WHMs from NDA countries](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/taxation-of-australian-resident-whms-from-nda-countries))_
- **What changes for an eligible resident** — Employers keep withholding at 15%. The worker lodges a return as a resident, including foreign-sourced income where Australia has taxing rights, and receives the resident rates, the low income tax offset and a Medicare levy liability if that produces less tax. A PAYG variation is available only after a prior year assessment as a resident or a private ruling.  _([ATO, Taxation of Australian resident WHMs from NDA countries](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/taxation-of-australian-resident-whms-from-nda-countries))_
- **Employers are unaffected** — The decision changes nothing for employers unless the ATO issues a variation notice.  _([ATO, Employers of working holiday makers](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/hiring-a-new-worker/employers-of-working-holiday-makers))_

## Section 8 - The worker's tax return

- **When no return is needed** — A WHM whose only income was salary or wages earned as a WHM, totalling less than $45,001, does not need to lodge a return or a non-lodgment advice.  _([ATO, Working holiday makers](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/working-holiday-makers))_
- **When to lodge** — Lodge to claim deductions, where income passed $45,000 and withholding fell short, where an unregistered employer withheld 30%, or as an eligible NDA-country resident. The return asks for WHM net income and nationality in the adjustments section.  _([ATO, Taxation of Australian resident WHMs from NDA countries](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/taxation-of-australian-resident-whms-from-nda-countries))_
- **Medicare levy** — A foreign resident for the full year claims a full exemption from the Medicare levy, exemption category 2, and a part-year foreign resident claims it for that period if there are no dependants outside an exemption category.  _([ATO, Foreign residents Medicare levy exemption](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-exemption/foreign-residents-medicare-levy-exemption))_
- **Leaving early** — A worker leaving Australia permanently before 30 June can lodge the return early.  _([ATO, Working holiday makers](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/working-holiday-makers))_
- **TFN** — Apply online once the visa is granted; without a TFN the 45% rate applies to every payment.  _([ATO, Working holiday makers](https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/working-holiday-makers))_

## Section 9 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Worker | Lena, 417 visa, national of Spain, foreign resident for the whole of 2026-27, TFN quoted |
| Employer | One registered WHM employer for the full year, paying $4,333.33 monthly ($52,000 for the year) |
| Super | Superannuation guarantee at 12% |

**Facts.** All figures are synthetic.

**Step 1, monthly withholding.** Each pay is $4,333 ignoring cents. Until the cumulative total
passes $45,000 the coefficient is 0.15.

```
Months 1 to 10   4,333 x 0.15 = 649.95, rounded to           650 each
Cumulative payments after month 10                        43,333
Month 11         prior total below 45,001, still 0.15        650
Cumulative payments after month 11                        47,667
Month 12         prior total above 45,000, so 0.30         1,300
Total withheld for the year                                8,450
```

**Step 2, tax on assessment.**

```
Tax on the first 45,000 at 15%                             6,750
Tax on the next 7,000 at 30%                               2,100
Tax payable                                                8,850
Less tax withheld                                          8,450
Shortfall to pay on lodgment                                 400
```

Lena must lodge a return because her income passed $45,000 and the withholding scale lags the
assessment scale. She claims the foreign resident Medicare levy exemption for the full year.

**Step 3, superannuation and the DASP.**

```
Super guarantee 52,000 x 12%                               6,240
DASP tax at 65% on the taxable component                   4,056
Net DASP paid after Lena leaves Australia                  2,184
```

**Step 4, if the employer were unregistered.** Withholding would have been 30% of every pay,
$15,600 for the year, and Lena would lodge to recover the $6,750 excess. The employer would also
face a penalty for failing to register.

**Step 5, if Lena were German and became a resident.** As a national of an eligible NDA country
who had become an Australian resident, she could lodge as a resident and pay the lower of the WHM
tax and the resident calculation, which for $52,000 of Australian income is resident rates on the
amount above the tax-free threshold plus the Medicare levy, less the low income tax offset.

## Section 10 - Common errors

- Employing a 417 or 462 visa holder without registering, then withholding 15% anyway.
- Applying the 15% rate to a worker on any other visa, or continuing it after the worker moves to a sponsored or permanent visa.
- Resetting the $45,000 cumulative total when the worker changes jobs; each employer tracks its own payments, which is why a multi-employer worker often has a shortfall on assessment.
- Using Schedule 7 or Schedule 11 for a WHM's leave or termination payments.
- Allowing the tax-free threshold, offsets or a Medicare levy reduction through withholding.
- Reporting WHM income under the salary and wages income type, or without the country of nationality.
- Skipping super guarantee, or advising the worker that the DASP is taxed at the ordinary 35% rate.
- Including the DASP in a tax return.
- Treating a long stay, a lease or a steady job as proof of residency, or the reverse.
- Advising an NDA-country worker to lodge as a resident without evidence that residency actually changed.

## Section 11 - Self-checks

- [ ] The employer's WHM registration is visible on the Australian Business Register.
- [ ] The visa subclass has been verified on VEVO and the TFN declaration is on file.
- [ ] Cumulative payments per worker are tracked so the rate moves at $45,000, $135,000 and $190,000.
- [ ] Every payment type, including leave and termination amounts, runs through Schedule 15.
- [ ] STP reports income type WHM, the country of nationality and an H tax treatment code.
- [ ] Super guarantee is paid at 12% with a choice of fund offered.
- [ ] The worker knows the DASP is claimed after departure and taxed at 65%.
- [ ] Residency has been assessed on purpose and behaviour, not on days alone.
- [ ] NDA-country status and residency are both established before lodging as a resident.
- [ ] The Medicare levy exemption is claimed for the foreign resident period.

## Section 12 - Sources

- Income Tax Rates Act 1986, Part III (working holiday maker income); Taxation Administration Act 1953, Schedule 1, section 12-35; Superannuation Guarantee (Administration) Act 1992; Superannuation (Departing Australia Superannuation Payments Tax) Act 2007.
- ATO, Schedule 15 tax table for working holiday makers (from 1 July 2026), https://www.ato.gov.au/tax-rates-and-codes/schedule-15-tax-table-for-working-holiday-makers
- ATO, Tax rates: working holiday maker, https://www.ato.gov.au/tax-rates-and-codes/tax-rates-working-holiday-makers
- ATO, Employers of working holiday makers, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/engaging-a-worker/hiring-a-new-worker/employers-of-working-holiday-makers
- ATO, Employer registration for working holiday makers, https://www.ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/registration-obligations-for-businesses/work-out-which-registrations-you-need/taxation-registrations/employer-registration-for-working-holiday-makers
- ATO, Working holiday makers, https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/working-holiday-makers
- ATO, Taxation of Australian resident WHMs from NDA countries, https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/taxation-of-australian-resident-whms-from-nda-countries
- ATO, Australian residency if you're on a working holiday or visit, https://www.ato.gov.au/individuals-and-families/coming-to-australia-or-going-overseas/coming-to-australia/australian-residency-if-you-re-on-a-working-holiday-or-visit
- ATO, TR 2023/1 Income tax: residency tests for individuals, https://www.ato.gov.au/law/view/document?DocID=TXR/TR20231/NAT/ATO/00001
- ATO, Departing Australia superannuation payment (DASP), https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/temporary-residents-and-superannuation/departing-australia-superannuation-payment-dasp
- ATO, Super guarantee, https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee
- ATO, How to report employment and tax information through STP Phase 2, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines/how-to-report-employment-and-tax-information-through-stp-phase-2
- ATO, STP Phase 2 income types, https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines/reporting-the-amounts-you-have-paid/income-types
- ATO, Foreign residents Medicare levy exemption, https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-exemption/foreign-residents-medicare-levy-exemption

Sources were checked on 27 September 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before relying on it for withholding, registration or a return. Residency and the non-discrimination article position depend on the worker's facts.

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
