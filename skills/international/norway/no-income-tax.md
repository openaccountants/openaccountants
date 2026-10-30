---
name: no-income-tax
description: "Use this skill for Norwegian personal income tax for income year 2026 (the calendar year, filed in 2027). It covers who is taxed in Norway, the 22% tax on ordinary income (18.5% in Finnmark and seven Nord-Troms municipalities), the five-step bracket tax (trinnskatt) on personal income, the national insurance contribution as it sits on the same base, the NOK 114,540 personal allowance, the 46% and 40% minimum deductions, the pension tax credit, the low-income limitation, the selected-youth work deduction, sole proprietors (enkeltpersonforetak) and calculated personal income, depreciation, wealth tax, returns, advance tax, enforcement fines and additional tax. Trigger on: Norwegian tax, skattemelding, trinnskatt, alminnelig inntekt, personinntekt, personfradrag, minstefradrag, enkeltpersonforetak, ENK, formuesskatt, forskuddsskatt, restskatt. Out of scope: no-social-contributions (contribution detail), no-employer-payroll, no-capital-gains (shares, shareholder model), no-individual-residence (residence and exit), no-corporate-income-tax, no-vat-return, no-transfer-pricing."
version: 2.1
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-10-30
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway: personal income tax (income year 2026)

This skill covers personal income tax in Norway for income year 2026. The 2026 return is filed in spring 2027. A return filed in 2026 is for 2025 and needs 2025 figures. The main law is the Tax Act (skatteloven, lov 1999-03-26-14). The rates and amounts for the year are in the Storting's tax decision for 2026 (Stortingets skattevedtak, FOR-2025-12-18-2747, amended 19 June 2026). Returns, penalties and corrections follow the Tax Administration Act (skatteforvaltningsloven) and its regulation. Payment and interest follow the Tax Payment Act (skattebetalingsloven). The authority is Skatteetaten. Amounts are in Norwegian kroner (NOK).

Norway taxes individuals on two bases. Ordinary income (alminnelig inntekt) is net income after deductions and is taxed at a flat 22%. Personal income (personinntekt) is gross pay, pensions and calculated business income, with no deductions; bracket tax and the national insurance contribution fall on it. Keep the two bases apart in every calculation.

Detail lives in the sibling skills. Read [no-social-contributions](no-social-contributions.md) for the national insurance contribution and employer contributions, [no-employer-payroll](no-employer-payroll.md) for withholding on wages, [no-capital-gains](no-capital-gains.md) for shares, dividends and the shield deduction, [no-individual-residence](no-individual-residence.md) for residence, emigration and exit tax, [no-corporate-income-tax](no-corporate-income-tax.md) for companies and [no-vat-return](no-vat-return.md) for VAT.

## Who this applies to

- **Residents.** A person resident in Norway is taxed on all wealth and income in Norway and abroad (skatteloven § 2-1 first and ninth paragraphs).
- **Day tests.** A person who stays in Norway for more than 183 days in any 12-month period, or more than 270 days in any 36-month period, is resident, but only from the income year in which the stay passes that count (§ 2-1 second paragraph). Detail and the emigration tests are in [no-individual-residence](no-individual-residence.md).
- **Leaving Norway.** Residence ends for a year only if the person shows they did not stay in Norway for periods over 61 days in that year and that they and close relatives did not have a home in Norway. A person resident for at least ten years stays resident until the end of the third income year after moving, subject to the same tests each year (§ 2-1 third paragraph).
- **Wealth tax residence.** The duty to pay wealth tax depends on living in Norway on 31 December of the year before the assessment year (§ 2-1 seventh paragraph).
- **Non-residents.** A non-resident is taxed only on the Norwegian items listed in § 2-3, such as work done in Norway and business carried on here. A short-stay foreign worker can choose the flat PAYE scheme (kildeskatt på lønn, Tax Act chapter 20); see Cross-border points.
- **Sole proprietors.** An owner of an enkeltpersonforetak (ENK) is taxed personally. Business profit is ordinary income, and a calculated personal income (beregnet personinntekt) carries bracket tax and the contribution (§§ 12-2 g and 12-10 to 12-13).
- **Out of scope here.** Companies (AS, ASA), partnerships taxed at partner level, petroleum tax, Svalbard tax, shipping tonnage tax and the special rules for fishermen, farmers and seamen. They use other rules and are flagged, not computed.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax on ordinary income, individuals | 22% (common tax 8.25% + county 2.40% + municipal 11.35%, maximum rates) | 2026 | ssv. §§ 3-2, 3-8; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Tax on ordinary income, Finnmark and Karlsøy, Kvænangen, Kåfjord, Lyngen, Nordreisa, Skjervøy, Storfjord | 18.5% (common tax 4.75%) | 2026 | ssv. § 3-2; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Bracket tax step 1 | 1.7% of personal income above NOK 226,100 | 2026 | ssv. § 3-1; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 |
| Bracket tax step 2 | 4.0% above NOK 318,300 | 2026 | ssv. § 3-1 |
| Bracket tax step 3 | 13.7% above NOK 725,050 | 2026 | ssv. § 3-1 |
| Bracket tax step 4 | 16.8% above NOK 980,100 | 2026 | ssv. § 3-1 |
| Bracket tax step 5 | 17.8% above NOK 1,467,200 | 2026 | ssv. § 3-1 |
| National insurance contribution: pay | 7.6% | 2026 | Stortingsvedtak om avgifter til folketrygden 2026 § 7; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 |
| National insurance contribution: business income | 10.8% | 2026 | same decision § 8 |
| National insurance contribution: pensions, and anyone under 17 or over 69 | 5.1% | 2026 | same decision § 6 |
| Contribution lower limit and phase-in | Nothing due up to NOK 99,650; never more than 25% of income above NOK 99,650 | 2026 | folketrygdloven § 23-3 fourth paragraph; https://lovdata.no/lov/1997-02-28-19/§23-3 |
| Personal allowance (personfradrag), class 1 | NOK 114,540 | 2026 | ssv. § 6-3 |
| Minimum deduction on pay | 46% of pay, at most NOK 95,700 | 2026 | skatteloven § 6-32 first paragraph a; ssv. § 6-1 |
| Minimum deduction on pensions | 40% of pensions, at most NOK 75,400 (pay and pension together capped at NOK 95,700) | 2026 | skatteloven § 6-32 first paragraph b and d; ssv. § 6-1 |
| Special deduction, Finnmark and seven Nord-Troms municipalities | NOK 45,000 (not for bracket tax or contribution) | 2026 | skatteloven § 15-5 |
| Tax credit for pensioners | Up to NOK 39,100; reduced by 19.1% of pension income above NOK 294,200 and 6% above NOK 437,100 | 2026 | ssv. § 6-5 (amended 19 June 2026); skatteloven § 16-1 third paragraph |
| Low-income limitation for pensioners | No tax below NOK 163,750 (single) or NOK 151,350 (each spouse); above that, tax capped at 55% of the excess | 2026 | ssv. § 6-4; skatteloven § 17-1 |
| Selected-youth work deduction (trial) | NOK 125,000, reduced by 40% of eligible income above NOK 345,000 | 2026 | ssv. § 6-6; skatteloven § 6-86 |
| Parental childcare deduction | NOK 15,000 for one child, plus NOK 10,000 for each further child | 2026 | ssv. § 6-2 |
| Exemption card limit (frikort) | NOK 100,000 | 2026 | Skatteetaten, Forskuddsutskrivingen 2026; https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ |
| PAYE scheme for foreign workers | 25% (22.5% under 17 or over 69; 17.4% if not a member of national insurance); only up to NOK 725,050 of pay | 2026 | ssv. § 3-9; Forskuddsutskrivingen 2026 |
| Wealth tax, state | 0.65% of net wealth above NOK 1,900,000; 0.75% above NOK 21,500,000 (spouses: NOK 3,800,000 and NOK 43,000,000) | 2026 | ssv. § 2-1 |
| Wealth tax, municipal | Up to 0.35% of net wealth above NOK 1,900,000 | 2026 | ssv. § 2-3 |
| Wealth valuation, primary home | 25% of estimated market value; 70% of the part above NOK 14,000,000 | 2026 | skatteloven § 4-10 second paragraph |
| Wealth valuation, shares | 80% of value | 2026 | skatteloven § 4-12 |
| Direct expensing of an asset | Cost below NOK 30,000 or life under three years | 2026 | skatteloven § 14-40 |
| Bank-payment rule for deductions | A cost paid other than through a bank is deductible only if the payment is under NOK 10,000 | 2026 | skatteloven § 6-51 |
| Upward adjustment factor on share income | 1.72 | 2026 | Forskuddsutskrivingen 2026 (skatteloven § 10-31 first paragraph) |
| Late-payment interest | 12% from 1 January 2026; 12.25% from 1 July 2026 | 2026 | skattebetalingsloven § 11-1; https://www.skatteetaten.no/satser/forsinkelsesrenter/ |
| Court fee (basis of enforcement fines) | NOK 1,345 | 2026 | Skatteetaten, enforcement fines; https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/enforcement-fines/ |

The 22% is the sum of maximum rates. A county or municipality may set a lower rate, but the maximum applies unless it does (ssv. § 3-8 second paragraph).

## The taxable base

### Ordinary income for an employee or pensioner

1. Start with taxable pay, benefits in kind, pensions, interest, rent and other income. Shares and dividends follow the shareholder model in [no-capital-gains](no-capital-gains.md); dividends and gains above the shield are multiplied by 1.72 for 2026 before the 22% applies.
2. Deduct the minimum deduction (minstefradrag) unless actual costs of earning the pay are higher (§ 6-30). It is 46% of pay up to NOK 95,700 and 40% of pensions up to NOK 75,400. Someone with both gets the sum, capped at NOK 95,700 (§ 6-32). There is no minimum deduction on business income, except a childminder's fee in their own home (§ 6-31 first paragraph d).
3. Deduct interest on debt (§ 6-40), union dues, gifts to approved organisations, the parental childcare deduction and other specific deductions.
4. Deduct usable losses carried forward.
5. Deduct the personal allowance of NOK 114,540 (§ 15-4). In Finnmark and the seven Nord-Troms municipalities, also deduct NOK 45,000 (§ 15-5). The tax is 22% (18.5% there) of what is left, never below zero.

The personal allowance is cut to whole or started months of residence for a part-year resident (§ 15-4 fifth paragraph). The upper limit of the minimum deduction is cut the same way (§ 6-32 fourth paragraph).

### Personal income, bracket tax and the contribution

Personal income (§ 12-2) is pay and benefits, pensions, work assessment allowance and disability benefit, and calculated personal income from a sole proprietorship. No deduction reduces it: not the personal allowance, not interest, not losses. Bracket tax is charged step by step on total personal income (ssv. § 3-1). For a part-year resident the step limits are cut to whole or started months of residence (ssv. § 3-1 second paragraph).

The national insurance contribution is a percentage of the same personal income. Pay carries 7.6%, business income 10.8%, pensions and people under 17 or over 69 carry 5.1% (folketrygdloven § 23-3; 2026 decision §§ 6 to 8). Childminding in one's own home and fishing businesses that pay product tax carry the middle rate instead of the high rate (§ 23-3 second paragraph no. 2 c and d). Nothing is due up to NOK 99,650 of total personal income, and the total can never exceed 25% of income above NOK 99,650. Apply that limit once across all categories. The full method is in [no-social-contributions](no-social-contributions.md).

### Sole proprietors (enkeltpersonforetak)

**Is it a business?** Business needs profit potential, enough duration and extent, and work on the owner's own account and risk. A registration or a payment-platform label does not decide it. Occasional independent work can be employment-type income instead. Passive investments can be capital income.

**Business profit.** Taxable revenue includes earned sales, fees, commissions, royalties, grants and benefits in kind. Recognise credit sales in the year they are earned. Record sales without output VAT where charged. Reconcile customer sales, refunds, platform fees and payouts; a bank payout is not turnover. Separate loans, transfers and owner drawings. Owner withdrawals of goods or services are taxed at market value.

Deduct business costs with an invoice, a business purpose and a business-or-private split. Exclude private consumption and tax payments. A cost is deductible only if it was paid through a bank or a licensed payment provider, unless the total payment is under NOK 10,000. Several payments for the same delivery, service or contract count as one (§ 6-51). An amount refused under this rule cannot go into the asset's depreciation base either.

**Common costs.**

| Item | Treatment |
|---|---|
| Home office in an owned home or housing cooperative unit | Standard deduction NOK 2,240 for 2026, not reduced for part-year use; or actual costs with a supported split. The room must be used for the business. No deduction for rent paid to yourself. |
| Phone and internet (electronic communication) | Deduct the business costs, then add back private use. The private add-back is at most NOK 4,392 a year (field 6998 in the business specification) and never more than the costs. |
| Client meals at a restaurant outside the workplace | Deductible only within a ceiling of NOK 592 per person for 2026. Above the ceiling, none of the meal is deductible. Spirits make the whole meal non-deductible. Other entertainment, gifts to business contacts and trips are not deductible. |
| Training | Keeping up a qualification already used to earn income can be deductible. Getting a new qualification or degree normally is not. |
| Fines and additional tax | Not deductible, even when incurred in the business. |

**Vehicles.** A car counts as a business vehicle (yrkesbil) if business driving is at least 6,000 km a year, or more than half its total use; take a three-year view (Skatte-ABC B-5-3.3). Keep a trip log. A car below those tests is a private car even if it is used somewhat in the business; for business driving in a private car under 6,000 km the 2026 rate is NOK 3.50 per km (2026 rates regulation). For a business vehicle, deduct actual costs and depreciation and add back private use. Under the standard car-benefit rule the 2026 benefit is 30% of the list price as new up to NOK 370,300 and 20% of the excess. Use 75% of the list price if the car was more than three years old on 1 January, or if documented business driving exceeds 40,000 km in the year; use 56.25% if both apply (Skatteetaten, bilsatser firmabil). Private use of a car outside the standard rules is valued at NOK 3.40 per km (2026 rates regulation).

**Depreciation.** An asset with a cost of NOK 30,000 or more and a life of at least three years must go into a declining-balance group. An asset under NOK 30,000 or with a life under three years can be expensed or depreciated (§ 14-40). Use tax groups, not book depreciation (§ 14-43):

| Group | Assets | Maximum rate |
|---|---|---:|
| a | Office machines | 30% |
| b | Acquired goodwill | 20% |
| c | Lorries, buses, vans, taxis, vehicles for disabled transport | 24% |
| d | Passenger cars, tractors, machinery, tools, instruments, furniture | 20% |
| e | Ships, vessels, rigs | 14% |
| f | Aircraft, helicopters | 12% |
| g | Power transmission and distribution plant | 5% |
| h | Buildings and plant, hotels, restaurants | 4% |
| i | Commercial buildings | 2% |
| j | Fixed technical installations in buildings | 10% |

Groups a to d are pooled; each asset in e to i has its own balance; j is pooled per building (§ 14-41). On a sale in groups a to d and j, the price not taken to income reduces the balance (§ 14-44). A negative balance in a, c, d or j is taken to income at least at the group's rate (§ 14-46). Gains and losses on groups e to i go to a gain and loss account; at least 20% of a positive balance is taken to income and up to 20% of a negative balance is deducted each year (§ 14-45). A balance under NOK 30,000 is cleared in full that year (§ 14-47).

**Calculated personal income (§§ 12-10 to 12-13).** Start with ordinary business income before losses carried forward (§ 12-11 first paragraph). Add back actual capital costs and losses, except losses on customer receivables and interest on financial-institution debt up to the shield base. Deduct actual capital income such as interest, dividends and gains on financial assets, but not income on customer receivables. Then deduct the shield deduction: the shield base times the shield rate (§ 12-12). The shield base is the average of opening and closing values of business assets (fixed assets of NOK 30,000 or more, stock, customer receivables and acquired intangibles), less debt to financial institutions, supplier credit and customer prepayments. The Ministry sets the maximum shield rate for each year (§ 12-12 third paragraph). A negative result cannot be set against other personal income. It is carried forward against later positive results from the same business, and the right is lost to the extent the owner does not use it in the first year possible (§ 12-13).

**Small businesses.** An owner whose total operating revenue is NOK 50,000 or less need not file the business specification (næringsspesifikasjon), unless an exception applies, for example VAT registration, accounting duty, more than one business or a spouse split. Without the personal income report, personal income equals business income and a negative result cannot be carried forward (skatteforvaltningsforskriften § 8-2-1).

**Losses.** An ordinary business loss reduces other ordinary income. An unused ordinary loss is carried forward. Keep it separate from negative calculated personal income.

### Credits and limits

- **Pension tax credit (§ 16-1).** A person on a national insurance retirement pension or AFP gets a credit of up to NOK 39,100 against income tax and the contribution. It falls by 19.1% of pension income above NOK 294,200 and by 6% above NOK 437,100. It is cut for graded pension, AFP reduced for earnings and months without pension.
- **Low-income limitation (§ 17-1).** For a pensioner, no income tax or contribution is due when ordinary income (plus 1.5% of net wealth above NOK 200,000 for a single person, excluding the primary home) is no more than NOK 163,750 (single) or NOK 151,350 (each spouse). Above that, the listed taxes cannot exceed 55% of the excess. A person who qualifies for both the credit and the limitation gets the lower tax (§ 16-1 fourth paragraph).
- **Selected-youth work deduction (§ 6-86).** A trial from 2026 for 8% of people born 1991 to 2006 who were registered as taxable to Norway on 31 October 2025, drawn at random by Skatteetaten. The deduction is NOK 125,000, reduced by 40% of eligible income (pay, calculated personal income and partner pay) above NOK 345,000, so it reaches zero at NOK 657,500. It cannot exceed the income, cannot create or increase a loss and lasts five income years. It is cut by months for part-year residents. It is not given to anyone on the PAYE scheme or the foreign-worker standard deduction. Being in the age group is not enough; check the person was drawn.

### Wealth tax

Net wealth is valued at 1 January of the assessment year. Main valuation rules: primary home 25% of estimated market value and 70% of the part above NOK 14,000,000 (§ 4-10); secondary home 100%; listed and unlisted shares 80% (§ 4-12). The state rate is 0.65% above NOK 1,900,000 and 0.75% above NOK 21,500,000; the municipal rate is up to 0.35% above NOK 1,900,000 (ssv. §§ 2-1 and 2-3). The combined rate is therefore 1.0%, and 1.1% above NOK 21,500,000. Spouses taxed together have double thresholds. Debt is reduced in proportion where assets carry a valuation discount (§ 4-19).

## Deadlines and filing

| Step | When | Source |
|---|---|---|
| Tax return, employees and pensioners | End of April 2027 for income year 2026 | skatteforvaltningsforskriften § 8-2-3 first paragraph b |
| Tax return, ENK owners | End of May 2027 | § 8-2-3 first paragraph a |
| Spouses with different deadlines | Both may use the later one | § 8-2-3 second paragraph |
| Extension | Apply before the deadline; an accountant can get extensions for a smaller share of named clients, at most to 30 June | § 8-2-5 |
| Pre-filled return | An employee or pensioner whose pre-filled return is right need not submit; the pre-filled data then count as filed | skatteforvaltningsloven § 8-2 fourth paragraph |
| Advance tax (forskuddsskatt), individuals | Four equal instalments, 15 March, 15 June, 15 September, 15 December of the income year; under NOK 2,000 all falls due on 15 June | skattebetalingsloven § 10-20 |
| Extra advance tax | Pay by 31 May of the following year to avoid the interest charge on residual tax | skattebetalingsloven § 11-5 first paragraph |
| Residual tax (restskatt) | Three weeks after the assessment is sent, but not before 20 August; NOK 1,000 or more is split into two instalments five weeks apart | skattebetalingsloven § 10-21 |
| Correcting your own return | Up to three years after the filing deadline | skatteforvaltningsloven § 9-4 second paragraph |
| Tax office reopening | Five years after the end of the income year; ten years with aggravated additional tax | skatteforvaltningsloven § 12-6 |

The return covers wealth on 1 January of the assessment year and income of the previous calendar year (§ 8-2-2). A sole proprietor files the personal return with the business information and the business specification. Skatteetaten's page for sole proprietors says a deadline on a Saturday or Sunday is met by the next working day. Employees pay through withholding on the tax card; see [no-employer-payroll](no-employer-payroll.md). Self-employed people and people with income that has no withholding pay advance tax. Update the tax card when expected profit changes; Skatteetaten lets you change it online until 15 December. If an instalment is not paid, the later instalments fall due at once (§ 10-20 fourth paragraph).

Keep accounting records: the annual accounts, specifications and documentation of entries for five years after the year end; agreements and material correspondence for three years and six months (bokføringsloven § 13).

## Penalties and interest

- **Enforcement fine (tvangsmulkt).** If a return or other required information is not given by the deadline, Skatteetaten can set a daily fine. It is half a court fee per day (skatteforvaltningsforskriften § 14-1-1), capped at 50 court fees (skatteforvaltningsloven § 14-1 second paragraph). With the 2026 court fee of NOK 1,345 that is NOK 672.50 a day and at most NOK 67,250.
- **Additional tax (tilleggsskatt).** 20% of the tax advantage that was or could have been gained from wrong or missing information; 10% where the information was also reported by an employer or other third party (§ 14-5). Aggravated additional tax adds 20% or 40% for intent or gross negligence, so 40% or 60% in total (§ 14-6).
- **No additional tax** on correct pre-filled information, obvious typing or calculation errors, a voluntary correction not prompted by a control, an amount under NOK 1,000, or after death (§ 14-4). An enforcement fine already paid is deducted from additional tax for failing to file (§ 14-5 fifth paragraph). Additional tax can be appealed within six weeks (Skatteetaten, additional tax).
- **Late-payment interest.** Charged from the due date until payment (skattebetalingsloven § 11-1). The rate is 12% from 1 January 2026 and 12.25% from 1 July 2026.
- **Interest on residual tax.** Residual tax carries an interest charge from 1 July of the income year to the first due date, at the rate under § 11-6 reduced by 22%. No charge arises on residual tax paid by 31 May of the assessment year (§ 11-5). Interest also runs on tax increased by a change decision or the taxpayer's own correction (§ 11-2).

## Cross-border points

- **Residence and exit tax.** Residence day counts, the ten-year tail, the treaty tie-breaker and the exit tax on shares are in [no-individual-residence](no-individual-residence.md).
- **PAYE scheme (kildeskatt på lønn).** A foreign worker on a short stay with limited tax liability can be taxed at a flat 25% of gross pay with no deductions (skatteloven §§ 20-1 and 20-2; ssv. § 3-9). The rate is 22.5% under 17 or over 69 and 17.4% if the worker is not a member of national insurance. The scheme closes once pay exceeds NOK 725,050 (§ 20-3), and the ordinary rules then apply to all the pay. It is voluntary. A person only on the scheme need not file a return (skatteforvaltningsloven § 8-2 fifth paragraph).
- **Non-residents on ordinary rules.** The personal allowance is given to a resident and to someone taxable for work done in Norway (§ 15-4 fourth paragraph), cut by months. A non-resident taxable only on board fees and similar gets a minimum deduction of at most NOK 4,000 (§ 6-32 fourth paragraph).
- **Work abroad.** A resident working abroad for at least 12 continuous months can ask to have the tax on that foreign pay reduced, with short visits home limited to six days a month on average (§ 2-1 tenth paragraph). It does not apply where a treaty gives Norway sole taxing rights.
- **Pensioners in the EEA.** A non-resident pensioner in another EEA state taxed in Norway on almost all ordinary income can claim the pension credit and the low-income limitation (§§ 16-1 fifth and 17-1 fifth paragraphs).
- **Membership of national insurance** decides whether the contribution is due, not tax residence. See [no-social-contributions](no-social-contributions.md).

## Worked examples

Both examples assume a full-year resident in a municipality with the maximum rates, outside Finnmark and Nord-Troms, aged 17 to 69, a member of national insurance, not drawn for the youth deduction and with no other income or deductions. Amounts are unrounded working-paper figures; the official assessment rounds.

### Example 1: employee on NOK 700,000

An employee earns NOK 700,000 in 2026. The minimum deduction is 46% of pay, which is NOK 322,000, capped at NOK 95,700. Ordinary income is NOK 604,300. After the NOK 114,540 personal allowance the base is NOK 489,760, and tax at 22% is NOK 107,747.20. Bracket tax is on the full NOK 700,000: 1.7% of NOK 92,200 (NOK 226,100 to 318,300) is NOK 1,567.40, and 4.0% of NOK 381,700 (NOK 318,300 to 700,000) is NOK 15,268.00, together NOK 16,835.40. The contribution is 7.6% of NOK 700,000, NOK 53,200; the 25% limit (NOK 150,087.50) does not bite. Total tax before withholding is NOK 177,782.60.

```oa-check
name: NO employee, pay NOK 700,000 (2026)
inputs:
  pay: 700000
  min_rate: 46
  min_cap: 95700
  allowance: 114540
steps:
  - min_deduction: min(pct(pay, min_rate), min_cap)
  - ordinary_income: pay - min_deduction
  - base: max(ordinary_income - allowance, 0)
  - tax_ordinary: pct(base, 22)
  - step1: pct(min(pay, 318300) - 226100, 1.7)
  - step2: pct(min(pay, 725050) - 318300, 4.0)
  - bracket_tax: step1 + step2
  - contribution_rate: pct(pay, 7.6)
  - contribution_cap: pct(pay - 99650, 25)
  - contribution: min(contribution_rate, contribution_cap)
  - total: tax_ordinary + bracket_tax + contribution
expected:
  min_deduction: 95700.00
  ordinary_income: 604300.00
  base: 489760.00
  tax_ordinary: 107747.20
  bracket_tax: 16835.40
  contribution: 53200.00
  total: 177782.60
```

### Example 2: sole proprietor with a side job

An ENK owner has business profit of NOK 450,000 and pay of NOK 60,000 from a part-time job. The business has a documented zero shield base and no capital items, so calculated personal income equals the profit, NOK 450,000. The minimum deduction applies only to the pay: 46% of NOK 60,000 is NOK 27,600. There is none on the business profit. Ordinary income is NOK 482,400, the base after the personal allowance is NOK 367,860 and tax at 22% is NOK 80,929.20. Personal income is NOK 510,000. Bracket tax is NOK 1,567.40 on step 1 plus 4.0% of NOK 191,700 (NOK 7,668.00) on step 2, together NOK 9,235.40. The contribution is 7.6% of the pay (NOK 4,560) plus 10.8% of the business income (NOK 48,600), NOK 53,160; one 25% limit on NOK 510,000 (NOK 102,587.50) does not bite. Total tax is NOK 143,324.60, paid through withholding on the pay and four advance tax instalments.

```oa-check
name: NO sole proprietor NOK 450,000 plus pay NOK 60,000 (2026)
inputs:
  business: 450000
  pay: 60000
  allowance: 114540
steps:
  - min_deduction: min(pct(pay, 46), 95700)
  - ordinary_income: business + pay - min_deduction
  - base: max(ordinary_income - allowance, 0)
  - tax_ordinary: pct(base, 22)
  - personal_income: business + pay
  - step1: pct(min(personal_income, 318300) - 226100, 1.7)
  - step2: pct(min(personal_income, 725050) - 318300, 4.0)
  - bracket_tax: step1 + step2
  - contribution_rates: pct(pay, 7.6) + pct(business, 10.8)
  - contribution_cap: pct(personal_income - 99650, 25)
  - contribution: min(contribution_rates, contribution_cap)
  - total: tax_ordinary + bracket_tax + contribution
expected:
  min_deduction: 27600.00
  ordinary_income: 482400.00
  base: 367860.00
  tax_ordinary: 80929.20
  bracket_tax: 9235.40
  contribution: 53160.00
  total: 143324.60
```

## Ask the client first

- Were you resident in Norway for all of 2026, and where did you live on 1 January 2026 (municipality, and whether it is in Finnmark or the seven Nord-Troms municipalities)?
- What income did you have: pay, pension, business profit, rent, interest, dividends or share sales? Are you a member of Norwegian national insurance?
- If you run an ENK: what are revenue, costs, assets, debts and stock at the start and end of the year, and do you have any losses or negative personal income carried forward?
- What is your date of birth, and did Skatteetaten tell you that you were drawn for the youth work deduction?
- Do you receive a retirement pension or AFP, and from what month?
- What net wealth did you have on 1 January 2027 (home, second home, shares, bank, debt)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Stortingets skattevedtak for inntektsåret 2026, FOR-2025-12-18-2747, amended 19 June 2026 (§§ 2-1, 2-3, 3-1, 3-2, 3-8, 3-9, 6-1 to 6-6) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | 2026-10-30 |
| Stortingsvedtak om fastsetting av avgifter mv. til folketrygden for 2026, FOR-2025-12-18-2748 (§§ 6 to 8) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 | 2026-10-30 |
| Skatteloven, lov 1999-03-26-14 (§§ 2-1, 2-3, 4-10, 4-12, 6-30 to 6-32, 6-51, 6-86, 12-2, 12-10 to 12-13, 14-40 to 14-47, 15-4, 15-5, 16-1, 17-1, 20-1 to 20-3) | https://lovdata.no/lov/1999-03-26-14 | 2026-10-30 |
| Folketrygdloven, lov 1997-02-28-19 (§ 23-3) | https://lovdata.no/lov/1997-02-28-19/§23-3 | 2026-10-30 |
| Skatteforvaltningsloven, lov 2016-05-27-14 (§§ 8-2, 9-4, 12-6, 14-1, 14-4 to 14-6) | https://lovdata.no/lov/2016-05-27-14 | 2026-10-30 |
| Skatteforvaltningsforskriften, FOR-2016-11-23-1360 (§§ 8-2-1 to 8-2-5, 14-1-1) | https://lovdata.no/forskrift/2016-11-23-1360 | 2026-10-30 |
| Skattebetalingsloven, lov 2005-06-17-67 (§§ 10-20, 10-21, 11-1, 11-2, 11-5) | https://lovdata.no/lov/2005-06-17-67 | 2026-10-30 |
| Bokføringsloven, lov 2004-11-19-73 (§ 13) | https://lovdata.no/lov/2004-11-19-73/§13 | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Forskrift om satser mv. til bruk for forskudd og skattefastsetting for 2026, FOR-2025-11-07-2216 (NOK 3.50 and NOK 3.40 per km) | https://lovdata.no/dokument/SF/forskrift/2025-11-07-2216 | 2026-10-30 |
| Skatteetaten, Home office standard deduction 2026 | https://www.skatteetaten.no/en/rates/home-office-standard-deduction/?year=2026 | 2026-10-30 |
| Skatteetaten, Telefon og internett (ENK) | https://www.skatteetaten.no/bedrift-og-organisasjon/skatt/skattemelding-naringsdrivende/fradrag/eiendeler-utstyr-eiendom/telefon-og-internett/ | 2026-10-30 |
| Skatteetaten, Skatte-ABC R-13 Representasjon (2026 meal ceiling) | https://www.skatteetaten.no/en/rettskilder/type/handboker/skatte-abc/gjeldende/r-13-representasjon/R-13.008/R-13.009/ | 2026-10-30 |
| Skatteetaten, Skatte-ABC B-5-3.3 Yrkesbil | https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/b-5-bil--fradrag-for-bilkostnader/B-5.007/B-5.010/ | 2026-10-30 |
| Skatteetaten, Bilsatser firmabil 2026 | https://www.skatteetaten.no/satser/bilsatser---firmabil/ | 2026-10-30 |
| Skatteetaten, Tax return for sole proprietorships | https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/ | 2026-10-30 |
| Skatteetaten, Advance tax | https://www.skatteetaten.no/en/person/taxes/tax-deduction-card-and-advance-tax/advance-tax/ | 2026-10-30 |
| Skatteetaten, Enforcement fines | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/enforcement-fines/ | 2026-10-30 |
| Skatteetaten, Additional tax | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/additional-tax/ | 2026-10-30 |
| Skatteetaten, Forsinkelsesrenter | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-10-30 |
| Skatteetaten, Formuesskatt satser 2026 | https://www.skatteetaten.no/satser/formuesskatt/ | 2026-10-30 |

Not yet confirmed: that a sole proprietor using the NOK 3.50 kilometre rate may deduct no other costs of that car, and how an owner chooses between the standard benefit and the per-km valuation for a business vehicle (Skatte-ABC B-7, not read); the maximum shield rate for sole proprietors for 2026 (set after the year ends; § 12-12 third paragraph); the conditions for the home-office standard deduction on the share of the home and rental income (at least 50% of rental value, or rent up to NOK 20,000), which the 2026 page did not state; the van rules (class-two van list-price cut of 50% capped at NOK 150,000) and the 75% cost cap on the car benefit for sole proprietors, both in the previous version of this skill; the rate in skattebetalingsloven § 11-6 used for the residual-tax interest charge in 2026; whether the 19 June 2026 amendments to the pension credit (NOK 39,100, 19.1%) apply to the whole of income year 2026 in Skatteetaten's assessment, as the amended decision reads.

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
