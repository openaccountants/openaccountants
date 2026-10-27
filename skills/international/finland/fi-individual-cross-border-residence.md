---
name: fi-individual-cross-border-residence
description: >
  Determine Finnish individual residence, Finnish-source income and ordinary international double-tax relief for 2026. Covers arrival, departure, the Finnish-citizen three-year presumption, treaty residence, nonresident wage and investment taxation, progressive assessment, pensions, property income, foreign employment and the six-month exemption. Establish the actual source and treaty treatment before calculating withholding or relief. Includes net-income foreign-tax-credit limits, oldest-first five-year carryovers, progression exemption, source-tax refunds and filing routes. Trigger on moving to Finland, leaving Finland, tax residence, foreign wages, foreign pension, Finnish rent, source-tax card, nonresident dividends or foreign-tax credit. Social insurance and corporate permanent establishments use separate skills.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.5
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland individual cross-border residence v0.5

## Who this applies to

Use for an individual arriving in Finland, departing, living in several countries or receiving foreign/Finnish-source income across a border in 2026. First decide **domestic residence by period**, then treaty residence and each income article, then the tax calculation and collection route. Domestic residents are liable on worldwide income; nonresidents on Finnish-source income, subject to treaty restrictions. Domestic resident and treaty resident are distinct conclusions. [Income Tax Act 1535/1992 §§9–13][law].

The [individual income-tax skill](fi-income-tax.md) computes ordinary earned/capital income, pensions, rent, gains, sole-trade allocations, deductions and credits. This skill selects which income enters that computation and how foreign tax is relieved. Diplomatic/international-organisation service, seafarers, artists, sportspeople, foreign-key-employee elections and special fund arrangements need their separate statutory conditions. Do not use ordinary wage rules to decide those regimes. [Income Tax Act §§9–13,77][law]; [Nonresident Tax Act 627/1978 §§3–7,13][source-law].

## Rates, bands and thresholds

| Item | 2026 rule | Official source |
|---|---|---|
| Domestic presence route | Continuous stay **over 6 months**, temporary absences do not interrupt; main home is an independent route | ITA §11 [text][law] |
| Finnish citizen departure | Departure year plus next 3 tax years presumed resident unless substantial ties shown absent | ITA §11 [text][law] |
| Ordinary nonresident wage/trade income | 35% source tax, unless treaty or progressive route applies | Nonresident Act §7(1)(1) [text][source-law] |
| Source-tax wage deduction | EUR 510/month or EUR 17/day for shorter period, capped at income; requires source-tax card and statutory income eligibility | Nonresident Act §6 [text][source-law] |
| Nonresident natural-person dividend, taxable interest and royalty | 30% domestic source rate; unknown nominee dividend 35%; treaty/card can change outcome | Nonresident Act §§3,7 [text][source-law] |
| Net capital income under assessment | 30% through EUR 30,000, 34% above; distinguish gross source-tax route | Nonresident Act §15 [text][source-law] |
| Nonresident municipal rate under ordinary assessment | 7.60%; regional/church/health conditions separately | Nonresident Act §13a; [Vero 2026 municipal decision][municipal] |
| Foreign employment exemption | At least 6 months continuous work-caused stay; average at most 6 Finland days per full work month, maximum 60 days taken in advance | ITA §77 [text][law] |
| Unused credit | Next 5 tax years, same source/category, oldest before current-year tax | Relief Act 1552/1995 §5 [text][relief-law] |

## The base

### Residence and the period covered

Build a dated chronology of homes available, actual presence/absences, work, family and citizenship. Registration is evidence, not the statutory residence test. An arrival for exactly six months does not satisfy the **over-six-month** route, but a main home in Finland can still do so. A stay can cross tax years; do not replace it by a universal 183-day count. For a foreign citizen leaving, check retained home and continued presence before ending residence. For a Finnish citizen leaving in 2026, the presumption ordinarily includes 2027–2029; an earlier nonresident claim needs evidence of substantial ties ending. Work abroad temporarily while a home/family/business remains in Finland does not itself rebut the presumption. Special state-service rules in §11(2)–(3) survive the ordinary window. [ITA §§9,11][law].

Claim the actual effective period with supporting residence certificate, deed/lease, family and work records, travel log and Finnish ties. Vero distinguishes ties broken on departure from ties broken later, for which nonresidence generally starts at the next year's beginning. Use the tax return/MyTax or Form 50A claim route. [Vero residence guidance §§3.2,6.1][residence].

If both states regard the person as resident, read the **actual treaty**, applying its permanent-home, vital-interests, habitual-abode, citizenship and competent-authority sequence where provided. Preserve the treaty/article and supporting facts. Do not treat the residence certificate alone as a substitute for that analysis or invent a treaty rate. [Vero treaty-residence guidance §5][residence].

### Finnish-source income of a nonresident

Map each receipt under ITA §10, including Finnish real-property/apartment rent, Finnish business activity, public-employer wages, private employment performed exclusively/mainly in Finland for a Finnish employer, Finnish board fees, leased-worker income, Finnish pensions, dividends and royalties. A board fee can be Finnish-source regardless of where the meeting is held; an ordinary private wage needs the statutory employer/workplace conditions. Then apply the treaty income article. The domestic source list is not exhaustive. [ITA §§10,13][law].

For ordinary wages within source taxation, include cash and taxable benefits, excluding only qualifying tax-free travel reimbursements. Apply the EUR 510/month or EUR 17/day reduction only under the source-tax card and §6 conditions, capped at the qualifying income, then 35%. The deduction is not a second annual income-tax expense allowance. Social contributions are separate. A director's fee in ITA §10(4a) does not qualify for the §6 reduction. [Nonresident Act §§4,6–7][source-law].

For ordinary dividends, taxable interest or royalties received by an individual, apply the gross 30% domestic rate, subject to a proven treaty ceiling/card. Qualifying interest on deposits, bonds and other ordinary loans not equivalent to capital investment is exempt for nonresidents under ITA §9(2); a domestic-source label does not override that exemption. A nominee-listed dividend without recipient information bears 35% at payer level. For an EEA resident's dividend, §13(1)(3) permits assessment on request when the information-exchange conditions and inability to credit the Finnish source tax in the residence state are established by its authority's certificate. This is a conditional relief route, not an automatic dividend exemption. [ITA §9(2)][law]; [Nonresident Act §§3,7,13][source-law].

Pensions, Finnish net rent, property gains and other §13 assessed income follow annual assessment rather than a blanket 35% wage source tax. Deduct the applicable income-production costs and losses, then apply earned/capital computation in the [individual skill](fi-income-tax.md). Domestic property-rich share gains under ITA §10(10a) include a more-than-50% direct/indirect Finnish property test on disposal or within the preceding 365 days, excluding the specified publicly listed interests; treaty scope still needs its own article. [ITA §10][law]; [Nonresident Act §§13–15][source-law].

### Progressive wage option

An individual resident in the EEA or a jurisdiction with the required administrative-assistance/information-exchange agreement, or holding the specified researcher permit, can request §13(1)(6) assessment of qualifying earned income instead of source tax. Obtain the nonresident progressive tax card or advance decision; an election applies to all that year's qualifying §13(1)(6) income, not only the most favourable payment. Include foreign wages, pensions and social benefits within §14 in the rate calculation, after statutory net-income deductions, and tax only the Finnish-taxable share through the statutory progression deduction. If the EEA/researcher and **75% Finnish net-earned-income** test is met with residence-state income certification, the specified foreign income is left out of that rate calculation. Compute state tax, the 7.60% municipal rate and applicable church/health components with the income-tax and payroll skills; do not apply a withholding percentage as final assessment. [Nonresident Act §§13–16][source-law]; [Vero nonresident guidance §10][nonresident].

### Resident foreign wages: six-month exemption

Under ITA §77, the stay abroad must be caused by work and last continuously at least six months. The work state must have the treaty's primary right to tax where a treaty applies. The rule excludes Finnish public-employer/Business Finland pay and Finnish ship/aircraft work; employment-share benefits have their specific §77(2) conditions. Finland visits must average no more than six days per full work month, with no more than 60 days anticipated before earning them; the employee must return to continue the same foreign work. Unexpected compelling events outside employee/employer control have the statutory interruption/early-end exceptions. Count arrival/departure and visit days under the actual timeline, and allocate compensation to work performed abroad; Finnish work does not become foreign merely because paid by a foreign employer. [ITA §77][law].

Exempt wages still require reporting and separate insurance/insurance-salary analysis. A six-month wage exemption is not automatic exemption from Finnish social contributions. If the wage fails §77, include the taxable amount and use the treaty credit/exemption method below. [ITA §77][law]; [payroll](fi-employer-payroll.md), [social contributions](fi-yel-social.md).

### Compute foreign-tax relief

For credit-method income, establish the eligible paid foreign income tax for the same receipt/period and any treaty ceiling. A foreign tax levied contrary to the treaty is not cured by an unlimited Finnish credit. Compute Finnish taxable **net** foreign income using Finnish income-production costs/interest and the applicable source/category. The cap is the corresponding Finnish tax multiplied by foreign net taxable income / total net taxable income in that source/category; prepare the calculation separately by relevant tax. Negative/zero taxable capacity cannot create a cash credit. For capital income, apply the actual 30/34% band calculation to total income before deriving the cap. Do not use foreign gross receipts in the numerator while using net total income in the denominator. [Relief Act §§1–4][relief-law].

Use eligible confirmed carryovers still within their next-five-year window, oldest first, up to this year's cap; then current-year eligible tax in the remaining cap. Preserve unused current tax as a new vintage. The limitation is source/category based, not a separate cap invented for every country. Maintain country-level evidence to establish treaty eligibility, then combine only the statutory basket. Notify Vero if foreign tax changes. [Relief Act §§4–5,8–9][relief-law].

Where the treaty uses exemption with progression for an individual, include the net exempt receipt in the appropriate source/category's rate calculation, then deduct the portion of tax corresponding to exempt net income / total net income. Income-related expenses/interest cannot create a loss beyond the exempt foreign income. This is different from treating the income as never reported. Use 2026 wording: the amendments referring to ITA §9b under Act 325/2026 start in **2027**. [Relief Act §6 and commencement][relief-law].

## Deadlines and filing

Report worldwide income for resident periods and Finnish-taxable income for nonresident periods on the relevant pre-completed return or business return, correcting omissions by the date on that taxpayer's return. Declare foreign tax and the credit/exemption claim even if the tax card or advances anticipated relief. Use the [prepayment skill](fi-prepayments.md) where wages/income have no sufficient Finnish withholding. [Relief Act §8][relief-law]; [Nonresident Act §16][source-law].

A nonresident leased worker under §16a whose payer does not withhold and whose treaty permits Finnish taxation must request advances by the end of the month following work commencement. The 2026 amendment also addresses the specified leased-worker wage on a Finnish vessel. Do not apply a generic six-month exemption from this collection duty. [Nonresident Act §16a][source-law].

Give the payer the source/progressive card and recipient/residence evidence before payment. If source tax was excessive, the payer can correct within the payment year where applicable; otherwise request Vero refund with the payment, identity/residence and treaty evidence. Ordinary refund applications under §11 are within three years after the end of the calendar year of withholding. A source-tax refund is distinct from amending annual assessment. Retain both-country assessments, currency conversions and carryover vintages. [Nonresident Act §§10–11,13,16][source-law].

## Penalties and interest

A late leased-worker advance request can bring a tax increase up to **EUR 2,000** under §16a, considering seriousness/repetition. The recipient's annual assessment and deficient reporting follow Assessment Procedure Act §§32–33: use the sanctions and annual interest calculation in the [individual income-tax skill](fi-income-tax.md). A payer's missing source withholding or reporting is a separate liability under Nonresident Act §§8–10, not an automatic penalty of the recipient. Ordinary overdue-tax interest accruing in 2026 is 9.5%; relief interest accruing in 2026 is 4.5%; do not assume 2027 rates. [Nonresident Act §§8–11,16a][source-law]; [prepayments](fi-prepayments.md).

## Cross-border points

Keep four conclusions separate: domestic residence, treaty residence, source/treaty allocation for each income and insurance coverage. A1/certificate and social-security agreement evidence govern the insurance route; a treaty income-tax exemption alone does not. Foreign tax credits require actual tax type, payment, period and treaty compatibility. A Finnish property purchase also creates separate transfer/annual property-tax questions. [ITA §§9–13][law]; [Relief Act §§1–5][relief-law]; [Nonresident Act §§13–16][source-law].

## Two worked examples that recompute

### 1. Ordinary nonresident wages with source-tax card

Assume one full month's EUR 3,000 cash wage, no benefits, Finnish taxing right, no progressive election and a source-tax card allowing the monthly deduction. Taxable source base EUR 2,490 at 35% gives EUR 871.50 tax. Cash after source tax EUR 2,128.50 is **before** any separate insurance contributions.

```oa-check
name: Finland nonresident wage source deduction
inputs:
  wage: 3000
  authorised_monthly_deduction: 510
  rate: 0.35
steps:
  source_base: max(0, wage - authorised_monthly_deduction)
  source_tax: source_base * rate
  cash_before_insurance: wage - source_tax
expected:
  source_base: 2490
  source_tax: 871.5
  cash_before_insurance: 2128.5
```

### 2. Capital-income credit cap and oldest-first use

Assume domestic net capital income EUR 12,000 and foreign net capital income EUR 8,000, all ordinary taxable income, no credits/losses, eligible current foreign tax EUR 2,600 and valid same-category prior credit EUR 400. Total income EUR 20,000 gives Finnish capital tax EUR 6,000; the foreign cap is EUR 2,400. Use the prior EUR 400 first, then EUR 2,000 current credit, leaving EUR 600 current unused. Finnish tax after credit is EUR 3,600. Inputs assume treaty eligibility and valid vintage.

```oa-check
name: Finland capital foreign tax credit net limitation
inputs:
  domestic_net: 12000
  foreign_net: 8000
  finnish_rate: 0.30
  valid_prior_credit: 400
  current_foreign_tax: 2600
steps:
  total_net: domestic_net + foreign_net
  finnish_tax: total_net * finnish_rate
  foreign_limit: finnish_tax * foreign_net / total_net
  prior_used: min(valid_prior_credit, foreign_limit)
  current_used: min(current_foreign_tax, foreign_limit - prior_used)
  current_unused: current_foreign_tax - current_used
  finnish_tax_after_credit: finnish_tax - prior_used - current_used
expected:
  total_net: 20000
  finnish_tax: 6000
  foreign_limit: 2400
  prior_used: 400
  current_used: 2000
  current_unused: 600
  finnish_tax_after_credit: 3600
```

## Ask the client first

- What citizenships, homes, family/work ties and dated travel records apply?
- What residence period is claimed, and what foreign residence certificate/decision exists?
- Which income, payer, work location and property facts determine source and treaty article?
- What tax cards, Finnish advances/withholding and return deadlines already exist?
- Which paid foreign taxes, attributable expenses and unused credit vintages are evidenced?
- What A1/social-security coverage and foreign-employment work/visit records exist?

## Sources

| Official source | Provisions read | Read date |
|---|---|---|
| [Income Tax Act 1535/1992][law] | §§9–13,77: residence, source and foreign wages | 2026-10-26 |
| [Nonresident Tax Act 627/1978][source-law] | §§3–16a: rates, cards, assessment, refund and leased workers | 2026-10-26 |
| [Relief Act 1552/1995][relief-law] | §§1–6,8–9; distinguish future 325/2026 wording | 2026-10-26 |
| [Vero residence guidance][residence] | Residence effective periods, evidence and treaty sequence | 2026-10-26 |
| [Vero nonresident guidance][nonresident] | Income categories and assessment routes | 2026-10-26 |
| [Vero 2026 municipal decision][municipal] | Nonresident municipal percentage | 2026-10-26 |

Not yet confirmed: country-specific treaty rates and unusual special-service/election regimes. Establish those from the actual treaty and special statute for the case; no universal treaty outcome is asserted.

[law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[source-law]: https://www.finlex.fi/fi/lainsaadanto/1978/627
[relief-law]: https://www.finlex.fi/fi/lainsaadanto/1995/1552
[residence]: https://www.vero.fi/en/detailed-guidance/guidance/48999/tax-residency-nonresidency-and-residency-in-accordance-with-a-tax-treaty--natural-persons4/
[nonresident]: https://www.vero.fi/en/detailed-guidance/guidance/334489/taxation-of-income-received-by-nonresidents-natural-persons/
[municipal]: https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47465/kuntien-ja-seurakuntien-tuloveroprosentit-vuonna-2026/
