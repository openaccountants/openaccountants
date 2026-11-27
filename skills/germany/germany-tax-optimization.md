---
name: germany-tax-optimization
description: Use this skill whenever asked about reducing tax in Germany, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for self-employed individuals in Germany. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "Steuern sparen", "Steueroptimierung", "Steuerlast senken". ALWAYS read this skill before advising on any German tax optimization strategy.
version: 2.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Tax planning for the self-employed in Germany (Steueroptimierung)

## Scope

Use this Guide for German self-employed tax planning for 2026. Compare eligible options using taxable income and the actual tariff; a deduction is not the same as a cash saving. The examples preserve their stated inputs and years. They do not determine a real client's liability. Bookkeeping: `germany-bookkeeping`; payroll: `de-payroll`; VAT: `germany-vat-return`; trade tax: `de-trade-tax`; formation: `germany-formation`; property: `de-rental-income`.

## Ask the client first

- Establish residence, legal form, trade or profession, EÜR or balance sheet, expected profit and withdrawals, losses and other income.
- Establish the spouses' assessment eligibility, each person's taxable income and relevant special tariffs; a wedding date alone is insufficient.
- Obtain actual asset costs, purchase dates, independent usability, private use, planned investments and existing investment deductions.
- Obtain prior/current VAT turnover, start date, waiver/permission records, invoices and the actual supplies.
- Obtain pension/provider certificates, employer contributions, special cap reductions, Riester eligibility and prior relevant insured income, child-allowance allocation and health-cover facts.

## The method, step by step

1. Fix the facts and compute taxable income before choosing an option. Do not use profit or turnover as a substitute for taxable income.
2. Compare the eligible assessment routes using the tariff below. Wage-tax classes concern payroll withholding; use `de-payroll` for that question.
3. Check each asset and investment deduction separately, including its deadline and subsequent add-back. Compare timing, financing and later withdrawals before recommending a purchase or contribution.
4. Test VAT independently of EÜR income-tax timing. Do not infer entitlement from a bank entry or merchant name.
5. Record the non-tax reasons and resolve the referrals below before recommending an arrangement.

## Rates, bands and thresholds

The ordinary 2026 tariff uses taxable income rounded down to whole euros. Round the resulting tax down to whole euros. Special tariffs and progression adjustments require separate treatment. [EStG § 32a(1)](https://www.gesetze-im-internet.de/estg/__32a.html).

| Single taxable income x in EUR | Ordinary income tax in EUR | Official source |
| --- | --- | --- |
| Up to 12,348 | 0 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 12,349–17,799 | (914.51 × y + 1,400) × y; y is one ten-thousandth of x less 12,348 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 17,800–69,878 | (173.10 × z + 2,397) × z + 1,034.87; z is one ten-thousandth of x less 17,799 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 69,879–277,825 | 0.42 × x − 11,135.63 | https://www.gesetze-im-internet.de/estg/__32a.html |
| From 277,826 | 0.45 × x − 19,470.38 | https://www.gesetze-im-internet.de/estg/__32a.html |

## Income splitting and structuring

Spouses can elect individual or joint assessment if both meet the specified unlimited-tax-liability conditions and do not live permanently apart, with those conditions present at the beginning of or arising during the year. Either spouse choosing individual assessment means individual assessment; joint election requires both. The return records the election; an absent or ineffective election defaults to joint assessment. The spouse rules also apply to registered civil partners. Changes after final assessment have separate statutory conditions: do not assume a free retrospective choice. [EStG §§ 26](https://www.gesetze-im-internet.de/estg/__26.html), [2(8)](https://www.gesetze-im-internet.de/estg/__2.html).

Joint assessment combines income; ordinary splitting tax is twice the § 32a(1) tax on half the joint taxable income, subject to the special-tariff reservations. Compare both routes; unequal incomes alone do not establish a client's saving. [EStG §§ 26b](https://www.gesetze-im-internet.de/estg/__26b.html), [32a(5)](https://www.gesetze-im-internet.de/estg/__32a.html).

## Deductions and capital allowances

Business-caused expenditure is the starting point under [EStG § 4(4)](https://www.gesetze-im-internet.de/estg/__4.html). Household/living costs are excluded subject to the specific personal-relief exceptions in [§ 12](https://www.gesetze-im-internet.de/estg/__12.html). For courses, books, journals, work equipment, telephone, internet, chamber/professional dues and business insurance, establish the actual business connection and the applicable deduction/depreciation rules. No undocumented telephone percentage or universal immediate equipment deduction is given here. Mixed use, education, moving and restricted expenses require the referrals below.

| Option | Eligibility and limit for 2026 | Official source |
| --- | --- | --- |
| Home-working day allowance | EUR 6 per calendar day, at most EUR 1,260 across all business/professional activity. Ordinarily work predominantly at home and do not visit an outside first workplace that day. If permanently no other workplace is available, the allowance can also apply on days worked elsewhere/at the first workplace. Excluded to the extent the specified double-household accommodation deduction is available or a home-office-room deduction is taken. | https://www.gesetze-im-internet.de/estg/__4.html |
| GWG immediate deduction | Election for an independently usable, depreciable movable fixed asset costing no more than EUR 800 after excluding VAT contained in the price. Deduct in the acquisition/manufacture/contribution or business-opening year. Technically coordinated components usable only with other fixed assets fail independent usability even if transferable to another such arrangement. Above EUR 250, record date and cost/value separately unless already evident from the books. The pool election below takes precedence for its assets. Eligibility excludes contained VAT; the actual deductible cost excludes VAT only to the extent recoverable under § 9b(1). | https://www.gesetze-im-internet.de/estg/__6.html ; https://www.gesetze-im-internet.de/estg/__9b.html |
| Annual asset pool | Alternative for qualifying independently usable depreciable movable fixed assets costing more than EUR 250 and no more than EUR 1,000 after excluding contained VAT. Release one fifth in the formation year and each of the next four years; disposal does not reduce the pool. Apply uniformly to all qualifying assets acquired/manufactured/contributed in that year. Independently usable assets no more than EUR 250 can be expensed immediately. | https://www.gesetze-im-internet.de/estg/__6.html |
| Investment deduction (IAB) | Up to 50% of expected cost of a future depreciable movable fixed asset. Profit computed under § 4 or § 5, excluding IAB deductions AND § 7g(2) add-backs, must not exceed EUR 200,000. Asset must be rented out or used exclusively/almost exclusively in the business's German establishment until the end of the business year following acquisition/manufacture. Electronically transmit the prescribed totals; hardship permission requires equivalent submitted particulars. It may create/increase a loss. Partnership/common-property and special-business-asset deductions must follow their actual § 7g(7) investment attribution. | https://www.gesetze-im-internet.de/estg/__7g.html |
| Separate aggregate IAB cap | Unadded/unreversed deductions claimed in the deduction business year and the three preceding business years must total no more than EUR 200,000 per business. This is distinct from the profit test; it is not an automatic deduction of that amount. | https://www.gesetze-im-internet.de/estg/__7g.html |
| IAB acquisition and reversal | On acquisition, add back up to 50% of actual cost, no more than the available deduction; an optional cost reduction no greater than that add-back reduces all depreciation/GWG/pool bases. For deductions claimed after finality of the first assessment, the asset must still be unacquired when the deduction is claimed. Reverse unused deductions in their original year if not added back by the end of the third following business year; early reversal is possible. Failure of the subsequent use condition reverses the acquisition adjustments. Final assessments can be amended; § 233a(2a)'s later interest start does not apply to these reversals. | https://www.gesetze-im-internet.de/estg/__7g.html |
| Special depreciation | For depreciable movable fixed assets acquired/manufactured after 31 December 2023, up to 40% in total over the acquisition year and four following years, alongside § 7(1)/(2) depreciation. Prior business year's profit must meet the § 7g profit test; qualifying rental or exclusive/almost exclusive business use must persist in acquisition and following business year, or reversal applies. Cost reduction above reduces the base. Earlier assets and other depreciation selectors are referred below. | https://www.gesetze-im-internet.de/estg/__7g.html ; https://www.gesetze-im-internet.de/estg/__52.html |

For EÜR timing, receipts generally belong to the year received and expenses to the year paid; merely changing an invoice date does not establish either. Asset rules still apply. Regularly recurring items received/paid a short time around year-end belong to their economic year; resolve their exact timing before using a year-end strategy. Prepaid use rights over more than five years are spread over the covered period, subject to the market-standard Damnum/Disagio exception; balance-sheet profit rules are unaffected. This is not the VAT timing rule. [EStG §§ 11](https://www.gesetze-im-internet.de/estg/__11.html), [4(3)](https://www.gesetze-im-internet.de/estg/__4.html).

## Investment and retirement

For domestic pension deductions, establish actual paid qualifying contributions, refunds/subsidies, provider eligibility and absence of a disqualifying connection with tax-free income. Statutory pension, farmers' fund and professional funds providing comparable benefits share the § 10 pension regime. A Basisrente contract must meet the actual § 10(1) no. 2(b) conditions and certification requirement; the ordinary post-2011 retirement contract pays a lifelong monthly own-life annuity no earlier than age 62, with only permitted supplementary survivor/disability cover and limited payout exceptions. Rights must be non-inheritable, non-transferable, non-pledgeable, non-saleable and non-capitalisable. Pre-2012 contracts have the statutory age-60 exception. Do not infer qualification from a product name. [EStG § 10(1), (2), (2a), (6)](https://www.gesetze-im-internet.de/estg/__10.html).

| Item | Conditions and computation | Official source |
| --- | --- | --- |
| Shared pension deduction cap | 2026: EUR 30,826 single; EUR 61,652 jointly assessed (computed from the EUR 124,800 miners' pension ceiling × 24.7%, rounded up, and doubled). 100% from 2023, within the shared cap. Add qualifying tax-free employer pension contributions before capping, then subtract that employer amount. Apply the § 10(3) special cap reduction for specified pension-entitlement groups; specified Minijob employer amounts are added/subtracted only on application. Refunds/subsidies affect the actual eligible aggregate. | https://www.gesetze-im-internet.de/estg/__10.html ; https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html ; https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html |
| Riester special-expense comparison | For the ordinary domestic compulsory-statutory-pension-insurance branch, eligible contributions plus entitled allowance enter the comparison up to EUR 2,100 yearly. Voluntary contributions alone do not establish this eligibility. If deduction is better, add the allowance entitlement back to the resulting tariff tax; otherwise no special deduction. Product qualification, other eligibility populations and indirect-spouse cases need separate review. | https://www.gesetze-im-internet.de/estg/__10a.html |
| Riester own-payment minimum | For an isolated directly eligible claimant without an indirectly eligible spouse: max(EUR 60, min(4% of prior-year relevant statutory insured income, EUR 2,100) − entitled basic/child allowances). Use actual relevant insured income, not profit/turnover. Below the minimum, reduce the allowance in the ratio of paid qualifying contribution to minimum. At/above minimum, full entitlement. Special income categories/cases in § 86(2)–(5) are referred. | https://www.gesetze-im-internet.de/estg/__86.html ; https://www.gesetze-im-internet.de/estg/__10a.html |
| Riester basic allowance | EUR 175 yearly for an eligible claimant. Directly eligible under-25s at contribution-year start receive a one-off EUR 200 increase for the first eligible post-2007 contribution year for which an allowance is requested. The examples below are age 30. | https://www.gesetze-im-internet.de/estg/__84.html |
| Riester child allowance | EUR 185 per qualifying child, or EUR 300 if born after 2007. Requires assessed Kindergeld; complete recovery for the year removes entitlement. Multiple recipients: allocation to the first entitlement period's assessed recipient. For eligible non-separated EU/EEA-resident married different-sex parents, allocation is to the mother unless both request the father; corresponding same-sex married/civil-partner parents use the Kindergeld-assessed parent unless both request the other. The request cannot be withdrawn for an elapsed contribution year. Child count alone is insufficient. | https://www.gesetze-im-internet.de/estg/__85.html |
| Saver's allowance | For § 20 private capital income: EUR 1,000 single or EUR 2,000 jointly assessed, instead of actual expenses; no more than income after § 20(6) loss netting. Allocate half to each spouse, transferring the unused part to the other when the first spouse's capital income is below EUR 1,000. Business-held investments require separate classification. | https://www.gesetze-im-internet.de/estg/__20.html |

**Pension arithmetic preserved (2026).** Employee RV EUR 9,000 + qualifying tax-free employer RV EUR 9,000 + eligible Basisrente EUR 15,000 = EUR 33,000. Assuming no special cap reduction or other adjustment, min(33,000, 30,826) − 9,000 = EUR 21,826 deductible, rather than the employee's whole EUR 24,000. An isolated self-payer has no invented employer offset. Apply the actual eligibility conditions above.

**Earlier pension-cap illustration (labelled 2026 in the original).** The former EUR 29,344 single / EUR 58,688 joint cap and EUR 12,325 saving are withdrawn as 2026 conclusions. Its assumed-rate product is 29,344 × 42% = EUR 12,324.48, not proof of a current deduction or tax saving. Use the actual shared 2026 cap above; Check this point with one of our partner accountants for the case-specific outcome.

**Riester arithmetic preserved (2026).** Directly eligible age-30 claimant, no children or indirectly eligible spouse, relevant prior insured income EUR 20,000: minimum max(60, min(800, 2,100) − 175) = EUR 625. Paying EUR 312.50 gives EUR 175 × 312.50 / 625 = EUR 87.50 allowance. At EUR 100,000 relevant income the minimum is EUR 1,925. The EUR 60 floor still applies at low income. These are allowance/contribution calculations, not a net tax-saving promise.

On application, § 32d(6) compares taxation of all relevant capital income at the tariff with the separate regime, including surcharges. The request must cover all capital income for that year, and both spouses' capital income on joint assessment. A marginal rate comparison alone is insufficient. [EStG § 32d(6)](https://www.gesetze-im-internet.de/estg/__32d.html).

## VAT planning

| Option | Actual gates before using it | Official source |
| --- | --- | --- |
| Domestic small-business exemption | For an eligible German/§ 1(3)-territory-established supplier's § 1(1) no. 1 supplies: § 19 turnover no more than EUR 25,000 in the preceding year AND no more than EUR 100,000 in the current year; this is actual turnover, not an estimate safe harbour. The whole crossing supply loses exemption. A start-up uses EUR 25,000 in the start year, with the whole crossing supply taxable. Use receipts-based turnover: exclude § 4 no. 8(i), no. 9(b) and nos. 11–29 exempt supplies; exclude § 4 nos. 8(a)–(h), 9(a) and 10 only if ancillary; exclude fixed-asset disposals. No related input deduction for § 19 exempt supplies. Intra-EU new-vehicle supplies and foreign schemes need separate treatment. Office requests and specified foreign-purchase/recipient liabilities can still cause filing duties. | https://www.gesetze-im-internet.de/ustg_1980/__19.html ; https://www.gesetze-im-internet.de/ustg_1980/__15.html ; https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-muster-USt-erklaerung-2026.pdf?__blob=publicationFile&v=5 |
| Waiver of that exemption | Irrevocable declaration by the last day of February of the second year after the period; effective from that period's start and binding for at least five calendar years. Later revocation operates from the beginning of a subsequent calendar year. Compare actual input/output VAT and customers before electing. | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Permitted cash VAT (Ist) | Tax office permission on application: prior § 19(2) turnover no more than EUR 800,000, or actual § 148 AO bookkeeping release, or to the extent supplies arise from a qualifying § 18(1) no. 1 profession. This Guide covers those business branches. A partial bookkeeping release without meeting the turnover branch limits permission to the released businesses. Switching methods must neither omit nor double-tax supplies. EÜR does not itself prove VAT permission. | https://www.gesetze-im-internet.de/ustg_1980/__20.html |
| Ordinary input VAT timing | For a completed business supply, legally owed VAT and possession of the required § 14/14a invoice are needed; payment is not a general condition. An advance before performance requires both invoice and payment. Apply exemption, mixed-use, expense-prohibition, entertainment and other restrictions separately; this row does not establish unrestricted deduction. | https://www.gesetze-im-internet.de/ustg_1980/__15.html |

## Deadlines, interest and red lines

For a mandatory ordinary calendar-year 2026 return, the unadvised deadline is 2 August 2027 (31 July is Saturday), subject to an actual applicable holiday or valid individual extension. A qualifying adviser-prepared mandatory return is ordinarily due 29 February 2028; an earlier tax-office call can apply. Farming/non-calendar-year and voluntary employee returns require separate treatment. [AO §§ 149](https://www.gesetze-im-internet.de/ao_1977/__149.html), [108(3)](https://www.gesetze-im-internet.de/ao_1977/__108.html).

Ordinary § 233a assessment interest for 2026 starts 1 April 2028, not on the advance-payment due date; it does not apply to assessment of advances/withholding. The § 238(1a) rate is 0.15% per full month, equivalent to 1.8% a year, on the difference rounded down to the next EUR 50. Refund interest is capped at the amount refunded and starts no earlier than payment. Farming and retrospective-event/loss cases have different start rules; apply the specific IAB reversal rule above. Other interest and late-payment/late-filing surcharges are separate: use the referral below. [AO §§ 233a](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [238](https://www.gesetze-im-internet.de/ao_1977/__238.html).

Under § 42 AO, an inappropriate legal arrangement producing a legally unintended tax advantage compared with an appropriate arrangement is abuse unless the taxpayer demonstrates non-tax reasons material in the overall circumstances. A specific anti-avoidance statute determines its own consequences first; otherwise tax follows the appropriate arrangement. Tax saving by itself is not the complete statutory test. [AO § 42](https://www.gesetze-im-internet.de/ao_1977/__42.html).

## Worked cases

Use the ordinary tariff above only on stipulated taxable income, with no special tariffs, progression adjustments, surcharge or church tax. Earlier numbers are preserved for correction; none is a certified client result.

**Original Example 1, splitting (2026): EUR 80,000 sole-trader income and spouse EUR 0.** The old EUR 21,787 / EUR 14,996 / EUR 6,791 saving is withdrawn. Profit alone does not fix taxable income or joint eligibility. If the stated EUR 80,000 is instead stipulated to be taxable income and the couple meets the joint conditions, single tax is floor(0.42 × 80,000 − 11,135.63) = EUR 22,464; joint tax is twice tax on EUR 40,000 = EUR 14,418; difference EUR 8,046. Choose joint assessment for that stipulated ordinary comparison. For the original profit-only facts: Check this point with one of our partner accountants.

**Original Example 2, Rürup (2026): single, EUR 70,000 profit, EUR 15,000 contribution.** Original arithmetic: 70,000 − 15,000 = EUR 55,000; 15,000 × 42% = EUR 6,300. Profit is not taxable income and a constant rate does not prove that saving. Under the explicit isolated-self-payer, eligible-contract/no-other-cap-use/no-special-reduction assumption, if EUR 70,000 is taxable income before the deduction, the ordinary tariff falls from EUR 18,264 to EUR 12,347, a EUR 5,917 difference. Actual deductibility, locked capital and future pension taxation/product suitability remain to be assessed. For the original unstated facts: Check this point with one of our partner accountants.

**Original Example 3, vehicle IAB/special depreciation (Year 0/Year 1, dates unspecified): EUR 40,000 planned cost.** Preserve the old inputs: IAB EUR 20,000; special depreciation EUR 8,000 at 20%; ordinary depreciation EUR 3,200 at the stated 16% on a reduced EUR 20,000 base; stated six-year life; total EUR 31,200, 78%, and EUR 13,104 at 42%. Arithmetic checks: 20,000 + 8,000 + 3,200 = 31,200; 31,200 / 40,000 = 78%; 31,200 × 42% = 13,104. But 1/6 is not 16%, the special-depreciation base must also reflect the elected IAB cost reduction, and the original purchase year, profit, use and depreciation selector are missing. An elected full IAB cost reduction leaves EUR 20,000 for depreciation, not an unchanged EUR 40,000 special-depreciation base. Do not use the old deduction/saving. Check this point with one of our partner accountants.

**Original Example 4, laptop (2026): EUR 799.** Under the explicitly qualifying independently usable depreciable movable-business-asset, fully business-used, VAT-exclusive-cost and no-pool assumptions, immediate deduction is EUR 799. The old EUR 336 saving is rounding of 799 × 42% = EUR 335.58. The old three-year illustration used EUR 266 and EUR 112 saving: 266 × 42% = EUR 111.72, while 799/3 = EUR 266.333…; it neither proves a three-year useful life nor purchase-year proration. No taxable-income interval is given. Keep the deduction conditional and do not treat those saving/life figures as usable conclusions. Check this point with one of our partner accountants.

**Original Example 5, home working (2026): 210 days.** If all days meet the allowance conditions, min(210 × EUR 6, EUR 1,260) = EUR 1,260. Old assumed-rate products are EUR 529.20 at 42% (old rounded EUR 529) and EUR 302.40 at 24% (old rounded EUR 302). Taxable income and the affected tariff interval are missing, so these products are not an established saving. Check this point with one of our partner accountants.

**Current Case 1, assessment choice (2026): EUR 60,000 taxable income, spouse EUR 0.** On the stipulated ordinary-tax/eligible-joint facts, single tax is EUR 14,233 and joint tax EUR 8,434; difference EUR 5,799. Choose joint assessment for this comparison. A spouse with progression income or losses requires a fresh comparison.

**Current Case 2, IAB (2026/2027): freelancer profit EUR 80,000 in 2026, machine EUR 30,000 in 2027.** Profit is stipulated as the statutory profit-test amount. If the asset, German rental/use, existing-deduction capacity, filing and timing conditions above are met, a full 50% deduction is EUR 15,000 in 2026. Electing the full EUR 15,000 acquisition add-back and cost reduction in 2027 leaves EUR 15,000 for depreciation. The original “worthwhile if the current marginal rate is at least next year's” conclusion is withdrawn: rates alone omit later depreciation, financing and actual use. Check this point with one of our partner accountants. The decision whether to claim remains held.

```oa-check
name: DE 2026 ordinary splitting, original and current income inputs
inputs:
  old_income: 80000
  income: 60000
steps:
  - old_single: floor(0.42 * old_income - 11135.63)
  - z_old_half: (old_income / 2 - 17799) / 10000
  - old_joint: 2 * floor((173.10 * z_old_half + 2397) * z_old_half + 1034.87)
  - old_difference: old_single - old_joint
  - z_single: (income - 17799) / 10000
  - tax_single: floor((173.10 * z_single + 2397) * z_single + 1034.87)
  - z_half: (income / 2 - 17799) / 10000
  - tax_joint: 2 * floor((173.10 * z_half + 2397) * z_half + 1034.87)
  - difference: tax_single - tax_joint
expected:
  old_single: 22464
  old_joint: 14418
  old_difference: 8046
  tax_single: 14233
  tax_joint: 8434
  difference: 5799
```

```oa-check
name: DE 2026 conditional investment deduction, not a recommendation
inputs:
  expected_cost: 30000
  profit: 80000
  profit_limit: 200000
steps:
  - deduction: pct(expected_cost, 50) * min(floor(profit_limit / profit), 1)
  - base_for_depreciation: expected_cost - deduction
expected:
  deduction: 15000.00
  base_for_depreciation: 15000.00
```

## When to refuse or refer

Each point below is a non-usable hold on the case-specific outcome, not a deduction or planning recommendation. **Check this point with one of our partner accountants.**

- Annual planning calendar: VAT return period/start-up rules and deadline extensions; income/trade-tax prepayments and reductions; recurring-item year-end attribution; late filing/payment, deferral, enforcement, disclosure and criminal tax questions. Build the client's calendar from actual obligations and notices, not the former generic month table. Check this point with one of our partner accountants.
- Solidarity surcharge: actual base, exemptions and mitigation, including a company versus an individual. Check this point with one of our partner accountants.
- Church tax: membership, state rate, base, mixed-faith arrangements and interaction with capital tax. Check this point with one of our partner accountants.
- Legal form: sole trader versus GmbH/UG/GmbH & Co. KG, corporate salary versus withdrawals, retained versus distributed profit, loss ownership, accounts and formation costs. No incorporation-profit threshold or combined tax rate is asserted. Check this point with one of our partner accountants.
- Trade tax: trade versus liberal profession, allowance, base rate, municipal multiplier and § 35 credit caps; 2026 versus later minimum-multiplier rules. Check this point with one of our partner accountants.
- Retained-profit election under § 34a: eligible accounts/partner share, applications, withdrawals and subsequent taxation. Check this point with one of our partner accountants.
- Dividend taxation: private versus business holding, flat-tax exceptions, partial-income option, costs, election/revocation and hidden distributions; owner loans, rent and pension promises. Check this point with one of our partner accountants.
- Corporate-tax option under § 1a KStG: eligible entity, application timing, initial irrevocability, separate later Rückoption and conversion consequences. Check this point with one of our partner accountants.
- Family employment: actual contract, pay/performance, arm's-length assessment and social-insurance status; no invented universal written-contract or own-bank-account court holding. Check this point with one of our partner accountants.
- Dedicated home-office room: centre-of-activity, actual costs versus annual flat amount, monthly reduction, records and interaction with the day allowance; no unsupported new-2026 court-documentation rule. Check this point with one of our partner accountants.
- Commuting: home/business-premises classification, full one-way kilometres, attendance, cap/car exception, business-car adjustments and special transport/disability situations. Check this point with one of our partner accountants.
- Business travel and relocation: private-car mileage versus business-asset costs; domestic/foreign meal allowances, overnight/trip duration, repeated-site limits and meal reductions; moving eligibility and evidence. Check this point with one of our partner accountants.
- Double household: own household, financial participation, work causation, location and accommodation/travel limits. Check this point with one of our partner accountants.
- Education and mixed expenses: first training versus later professional development, private/business allocation, business gifts/entertainment, separate records and restrictions. Do not infer entitlement solely from a course, merchant or expense label. Check this point with one of our partner accountants.
- Childcare and other private training expenses: eligible child/household, age/disability, excluded activities, payment evidence and individual limits. Check this point with one of our partner accountants.
- Donations: recipient eligibility, qualifying payments, evidence, caps and carry-forward. Check this point with one of our partner accountants.
- Household-service/craftsman relief: eligible household, expense/base, payment evidence and individual credit limits; no general percentage benefit is asserted. Check this point with one of our partner accountants.
- Other asset methods: useful lives, computer one-year treatment, ordinary/declining-balance/special depreciation windows, pre-2024 special depreciation, electric-vehicle accelerated depreciation, and company-car private use/list-price/logbook/commuting or electric/hybrid reductions. Do not substitute ordering/payment for acquisition or infer a method from price alone. Check this point with one of our partner accountants.
- Losses: intra-year restrictions, income-tax carry-back order/waiver/caps, carry-forward year-specific percentage, trade-tax separate carry-forward, limited partners, interest barrier and farming/forestry. Check this point with one of our partner accountants.
- Deferral models and hobby losses: § 15b initial-phase model/capital tests, loss-ring-fencing and profit intention; a tax motive or repeated loss alone is not a complete determination. Check this point with one of our partner accountants.
- Social insurance: compulsory, voluntary or application-based pension membership, one-client work versus employment status, professional funds, branch-specific ceilings and actual contributions. Do not equate one client with false self-employment. Check this point with one of our partner accountants.
- Health/care cover and pension/investment products: actual qualifying contributions and deduction adjustments, statutory versus private cover, pension payout taxation, Riester special populations/product certification, VWL eligibility and later investment/exit consequences. No product ranking or assumed lower retirement rate. Check this point with one of our partner accountants.
- Cross-border and exit: foreign spouse, home, income, customer, staff, company/assets, treaties, foreign credits, controlled foreign companies, transfer pricing, reverse-charge/place-of-supply and intra-EU reporting. Use `germany-transfer-pricing` and `de-capital-gains` for routing, with the actual facts. Check this point with one of our partner accountants.
- Property, succession and disposal: property companies, land/building split, building life, private sales/transfer tax, inheritance/gifts/business succession, sale/closure allowances, share sales and conversion holding periods. Check this point with one of our partner accountants.

## Sources

Existing exact source reads below are reused for unchanged 2026 conditions; genuinely new dependencies were read on 27 November. A statute's reservation is not an assumption that its conditions are met.

| Official source and operative passage read | Read date |
| --- | --- |
| EStG § 32a(1),(5), complete 2026 tariff and splitting: https://www.gesetze-im-internet.de/estg/__32a.html | 2026-11-26, reused |
| EStG §§ 26,26b,2(8), joint conditions/election/combination/civil partners: https://www.gesetze-im-internet.de/estg/__26.html ; https://www.gesetze-im-internet.de/estg/__26b.html ; https://www.gesetze-im-internet.de/estg/__2.html | 2026-11-26, reused |
| EStG § 4(3),(4),(5) no. 6c, EÜR/assets, business expense and full day-allowance conditions: https://www.gesetze-im-internet.de/estg/__4.html ; private-cost exclusion § 12: https://www.gesetze-im-internet.de/estg/__12.html | 2026-11-27 |
| EStG § 6(2),(2a), independent use, record duty and annual-pool election, and § 9b(1) recoverable input VAT/cost: https://www.gesetze-im-internet.de/estg/__6.html ; https://www.gesetze-im-internet.de/estg/__9b.html | 2026-11-27 |
| EStG § 7g(1)–(7), complete eligibility, limits, attribution, add-back and reversal; § 52(16) acquisition-date application: https://www.gesetze-im-internet.de/estg/__7g.html ; https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| EStG § 11, receipt/payment, recurring items, use prepayments and balance-sheet reservation: https://www.gesetze-im-internet.de/estg/__11.html | 2026-11-27 |
| EStG § 10(1),(2),(2a),(3),(4b),(6), pension qualification/provider/certification, adjustments and cap: https://www.gesetze-im-internet.de/estg/__10.html | 2026-11-27 |
| 2026 pension cap calculation inputs, § 4 ceiling and 2026 contribution-rate notice: https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html ; https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-11-26, reused |
| EStG § 10a(1),(2),(3), eligibility and comparison; § 86(1)–(5), actual minimum/payment ratio: https://www.gesetze-im-internet.de/estg/__10a.html ; https://www.gesetze-im-internet.de/estg/__86.html | 2026-11-27 |
| EStG §§ 84,85, basic/young-claimant/child entitlement and allocation: https://www.gesetze-im-internet.de/estg/__84.html ; https://www.gesetze-im-internet.de/estg/__85.html | 2026-11-27 |
| EStG § 20(9), saver allowance/allocation/limit; § 32d(6), full capital-income comparison: https://www.gesetze-im-internet.de/estg/__20.html ; https://www.gesetze-im-internet.de/estg/__32d.html | 2026-11-27 |
| UStG § 19, domestic exemption/turnover/waiver; § 15, exempt-use deduction exclusion; 2026 annual-return instructions, whole crossing supply/start-up: https://www.gesetze-im-internet.de/ustg_1980/__19.html ; https://www.gesetze-im-internet.de/ustg_1980/__15.html ; https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-muster-USt-erklaerung-2026.pdf?__blob=publicationFile&v=5 | 2026-11-26, reused |
| UStG § 20, all ordinary-business permission branches, partial-release and transition conditions: https://www.gesetze-im-internet.de/ustg_1980/__20.html | 2026-11-27 |
| UStG § 15(1) no. 1, ordinary/advance invoice timing: https://www.gesetze-im-internet.de/ustg_1980/__15.html | 2026-11-26, reused |
| AO §§ 149(1)–(4),108(3), filing/deadline rules, plus transitional scope in EGAO Art. 97 § 36: https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html ; https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26, reused |
| AO §§ 233a(1)–(3),238(1),(1a),(2), assessment-interest scope/start/refund/full-month/base rules: https://www.gesetze-im-internet.de/ao_1977/__233a.html ; https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-26, reused |
| AO § 42, entire specific-rule/abuse/non-tax-reason test: https://www.gesetze-im-internet.de/ao_1977/__42.html | 2026-11-27 |

Not yet confirmed: case-specific conclusions under the referral topics, original profit-only tax outcomes, vehicle dates/use/depreciation, laptop tax-saving interval and actual private-use classification. These are explicitly non-usable holds above.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Wirtschaftsprüfer) before filing or acting upon.

> Contributed by OpenAccountants.
