---
name: ie-usc
description: "Ireland's Universal Social Charge (USC) for tax year 2026, for employees, pensioners, the self-employed and investors. Covers the 2026 bands (0.5% on the first EUR 12,012, 2% on the next EUR 16,688, 3% on the next EUR 41,344, 8% on the balance), the EUR 13,000 exemption cliff, the reduced rates for people aged 70 or over and full medical card holders with income of EUR 60,000 or less, the 3% surcharge on non-PAYE income over EUR 100,000, exempt income such as social welfare payments and DIRT-paid interest, capital allowances and losses, spouses and maintenance, cumulative deduction through payroll, payment with preliminary tax and Form 11, and the late filing surcharge and interest. Trigger on 'USC', 'universal social charge', 'USC rates 2026', 'USC surcharge', 'USC medical card', 'USC exemption'. Out of scope: running a payroll (ie-payroll), income tax (ie-income-tax-form11), PRSI (ie-prsi-class-s), residence (ie-cross-border)."
version: 2.1
jurisdiction: IE
category: international
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland Universal Social Charge (USC), tax year 2026

> **Source-cited draft.** Drafted from Part 18D of the Taxes Consolidation Act 1997 (sections 531AL to 531AAF) as amended by Finance Act 2025 s.2, read in Revenue's Notes for Guidance (Finance Act 2025 edition) and checked against the enacted text of Finance Act 2011 s.3 and Finance Act 2012 s.3, the Universal Social Charge Regulations 2018 (S.I. No. 510 of 2018), Revenue's Tax and Duty Manual Part 18D-00-01 and Revenue's USC pages, all read on 2026-10-24. No accountant has reviewed it.

Authority: the Revenue Commissioners. The tax year is the calendar year. Currency: euro. Section numbers are TCA 1997 unless another act is named. USC is a tax on income, but it is not "income tax" within the Tax Acts: it is a separate charge under Part 18D (Tax and Duty Manual 18D-00-01, para 2).

See also: `ie-payroll` (running a payroll, the RPN, emergency basis), `ie-income-tax-form11` (the self-employed return), `ie-preliminary-tax` (preliminary tax rules), `ie-paye-rental-nonresident` (PAYE workers with side income, non-residents), `ie-prsi-class-s` (PRSI), `ie-cross-border` (residence).

## Who this applies to

- **Every individual** whose aggregate income for the year is more than EUR 13,000 (s.531AM(2)). Each person is charged on their own income. Spouses and civil partners are charged separately and cannot share bands (s.531AS(1), s.531AT(1)).
- **Aggregate income** is "relevant emoluments" (all income within the PAYE system, s.531AM(1)(a)) plus "relevant income" (all other income, s.531AM(1)(b)): salary, taxable benefits, occupational pensions, self-employed profit, rental profit, dividends and share option gains ([Revenue, USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx)).
- **Not in:** payments under the Social Welfare Acts and similar payments by other bodies, Irish or foreign (s.531AM(1)(a)(I)), and the exempt income listed in "The taxable base" below.
- **Non-residents:** USC is not payable on the employment income of a non-resident that is attributable to duties performed wholly outside Ireland, where there is no Irish income tax charge on it (Tax and Duty Manual 18D-00-01, para 16.1). Arrears or a bonus paid after a person leaves, for work done while resident, is PAYE income liable to USC in the year it is paid (para 16.2).
- **Who collects it:** the employer or pension provider for PAYE income (s.531AO); the individual through self-assessment for other income (s.531AS), or by assessment if they are not a chargeable person (s.531AT).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard band 1 (s.531AN, Table Part 1) | 0.5% on the first EUR 12,012 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Standard band 2 | 2% on the next EUR 16,688 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Standard band 3 | 3% on the next EUR 41,344 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Balance | 8% on the remainder (above EUR 70,044) | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Exemption: no USC if aggregate income does not exceed (s.531AM(2)); above it, USC on the full income | EUR 13,000 | 2026 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf |
| Reduced rates, aged 70 or over, aggregate income EUR 60,000 or less (s.531AN, Table Part 2) | 0.5% on the first EUR 12,012, 2% on the balance | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx |
| Reduced rate, full medical card holder under 70, aggregate income EUR 60,000 or less (s.531AN(3)) | Standard bands up to EUR 28,700, then 2% at most on the excess (same result as the reduced rates) | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Medical card reduced rate ends (s.531AN(4), "2028" substituted by FA 2025 s.2(1)(b)) | From the 2028 year of assessment | 2026, 2027 apply | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| Surcharge on relevant (non-PAYE) income over EUR 100,000 (s.531AN(2)) | 3% on the excess, so 11% in total on it | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx |
| Encashed private pension rights ring-fenced under s.787TA (s.531AN(3A)) | 2% on the full amount, not counted for the surcharge | 2026 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf |
| Bank bonuses from State-supported institutions (s.531AAD) | 45% on the full bonus; standard rates if bonuses are EUR 20,000 or less in the year | 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx |
| Property relief surcharge (s.531AAE(1), (3), inserted by Finance Act 2012 s.3) | Extra 5% of the part of aggregate income sheltered by specified property reliefs used in the year; only where aggregate income is EUR 100,000 or more | 2026 | https://www.irishstatutebook.ie/eli/2012/act/9/section/3/enacted/en/html |
| Emergency basis (no RPN), USC Regulations 2018 reg. 19 | 8% on all pay, no cut-off | 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf |
| Week 53 pay day (31 December, or 30/31 December in a leap year) (s.531AN(5) to (8)) | Bands, the EUR 60,000 limit and the EUR 13,000 exemption rise by 1/52 (weekly) or 1/26 (fortnightly), capped at the pay that day; not where pay days were changed | 2026 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf |

**How the exemption works.** It is a cliff, not an allowance. At EUR 13,000 or less: no USC. Above: USC on every euro from the first. The statute says "does not exceed", so income of exactly EUR 13,000 is exempt (s.531AM(2)). Revenue's exempt payments page says income "less than the exemption limit"; the statute governs. USC deducted from someone under the limit is repaid on a claim (s.531AW(2)).

**How the reduced rates work.** Two tests, both needed: (a) aged 70 or over, or holds a full medical card (including a Health Amendment Act card), and (b) aggregate income EUR 60,000 or less. Above EUR 60,000 the standard rates apply to all income, not just the excess ([Revenue, reduced rates](https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx)). They apply for the whole year if the person reaches 70 in the year or holds a full medical card at any time in the year. A medical card holder must tell Revenue. A GP Visit Card, Drugs Payment Scheme Card, Long-Term Illness Scheme Card or European Health Insurance Card does not qualify. A person who gets an Irish medical card under EU rules is still subject to the EUR 60,000 limit; frontier workers without a full Irish medical card pay up to 8% (Tax and Duty Manual 18D-00-01, para 13).

**How the non-PAYE surcharge works.** The test is relevant income only: income outside the PAYE system (self-employed profit, rental, investment income). PAYE salary does not count toward the EUR 100,000, and share option gains are not relevant income for this test (s.531AN(2A)). The 3% applies only to the part of relevant income above EUR 100,000. A large salary with modest side income pays no surcharge.

**Two rules share EUR 100,000. Keep them apart.** The non-PAYE surcharge tests relevant income, applies when it is MORE than EUR 100,000, and is charged on the excess. The property relief surcharge tests aggregate income (all income for USC, PAYE included), applies when it is EUR 100,000 OR MORE (a "specified individual", s.531AAE(1)), and is charged on the income sheltered by the reliefs.

**How the property relief surcharge works.** The specified property reliefs are the area-based capital allowances, writing down and balancing allowances on buildings and the other property-based accelerated allowances, and Section 23-type relief under s.372AP, including amounts carried forward (s.531AAE(1)). Only the part of a relief to which full effect is given in the year counts as used (s.531AAE(2)). The surcharge is 5% of that part of aggregate income against which the reliefs were used, on top of the ordinary USC (s.531AAE(3)). Property reliefs are treated as used before other High Earners Restriction reliefs (s.531AAE(4)(b)). Revenue's Notes for Guidance example (s.531AAE(3)): aggregate income EUR 150,000, EUR 50,000 of property relief used, surcharge EUR 2,500. The surcharge is computed on the reliefs claimed before the High Earners Restriction: with aggregate income EUR 150,000 and EUR 160,000 of property relief available, the surcharge is EUR 7,500 (5% of 150,000), not 5% of the restricted EUR 80,000 (Tax and Duty Manual 18D-00-01, para 18.3, Example A). Residential owner-occupier relief is outside it (para 18.1). Refer cases where the High Earners Restriction also applies.

**Revenue's own 2026 examples (use them as tests).**

| Person | Income | USC 2026 | Source |
|---|---|---|---|
| Jacob, 32, self-employed | EUR 25,000 | EUR 319.82 | https://www.revenue.ie/en/jobs-and-pensions/usc/calculating-usc.aspx |
| Sadhbh, 45 | EUR 50,000 | EUR 1,032.82 | same |
| Donnchadh, 55, full medical card, told Revenue | EUR 50,000 | EUR 819.82 | same |
| Cian, 75, over the EUR 60,000 limit | EUR 75,000 | EUR 2,030.62 | same |
| Emma | EUR 65,000 | EUR 1,482.82 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf |
| John, full medical card | EUR 55,000 | EUR 919.82 | same |
| Sinead: EUR 40,000 PAYE salary plus EUR 110,000 non-PAYE investment income | EUR 150,000 | EUR 8,330.62 | same |
| James and Claire, spouses, charged separately | EUR 30,000 and EUR 90,000 | EUR 432.82 and EUR 3,230.62 | https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx |

The Manual also shows EUR 12,500 (no USC) against EUR 13,500 (USC on the full amount). At 2026 rates, EUR 13,500 gives 60.06 + 2% of 1,488 = EUR 89.82 (our arithmetic).

## The taxable base

**Start from gross income.** USC is charged on gross income, including notional pay, after relief for certain trading losses and capital allowances, but before pension contributions (Tax and Duty Manual 18D-00-01, para 1). Income tax deductions and reliefs generally do not apply.

**Deducted before USC (s.531AM(1)(b)(vi) and (vii), s.531AU):**
- Trading or professional losses carried forward under s.382, to the extent actually used in the year against profits of the same trade. Other losses are not deductible.
- Capital allowances actually used in the year by a person carrying on the trade or profession: wear and tear on plant and machinery (s.284), industrial buildings (s.272), farm buildings (s.658) and farm pollution control (s.659), including amounts carried forward. Not deductible for lessors of plant, machinery or buildings, or for partners who are not active in the trade (s.409A). Lessors and passive investors pay USC on income before capital allowances.
- A legally enforceable maintenance payment to a separated spouse, civil partner or qualifying cohabitant, if there is no joint assessment (s.531AM(1)(b)(v) to (vb)).

**Not deducted:** employee pension contributions and permanent health insurance deducted from pay ("There is no relief from USC for employee pension contributions"), the initial market value of shares in an approved profit sharing scheme, approved share option gains, the SARP exempt amount (s.531AM(1)(a)(i) to (v)), donations to approved bodies, sports bodies and governing bodies, double rent allowance and lessor deductions under s.372AP and s.372AU (s.531AM(1)(b)(II)). Income exempt from income tax under s.140, 141, 142, 143, 195 (artists), 232, 234 and 664 is still charged to USC (s.531AM(1)(b)(I)). Income tax credits never reduce USC (s.531AX(2)).

**Exempt from USC:**
- Department of Social Protection payments and similar payments made by other bodies, including social welfare payments from another country, Community Employment, VTOS and Youthreach (s.531AM(1)(a)(I); [Revenue, exempt payments](https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx)).
- Deposit interest subject to DIRT, credit union dividends, EU and non-EU deposit interest, and income from certain foreign life policies, investment undertakings and offshore funds (s.531AM(1)(b)(iii)).
- Employer contributions to a PRSA, a PEPP or the auto-enrolment scheme (MyFutureFund) (s.531AM(1)(a)(VI) to (VIII)).
- Termination payments within the basic and increased exemptions and Standard Capital Superannuation Relief (s.531AM(1)(a)(IV)). Statutory redundancy under the Redundancy Payments Act 1967 is exempt. Ex-gratia payments above the statutory amount are exempt from income tax and USC within the limits; the basic exemption is EUR 10,160 plus EUR 765 for each full year of service, and the lifetime tax-exempt limit on ex-gratia payments is EUR 200,000 ([Revenue, basic exemption](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/lump-sum-payments/basic-exemption.aspx); Tax and Duty Manual 18D-00-01, para 14). USC applies to the part above the limits. The increased exemption and Standard Capital Superannuation Benefit are not set out here (Tax and Duty Manual Part 05-05-19).
- Pre-retirement access to AVCs (s.531AM(1)(a)(V)), income gifted to the Minister for Finance under s.483, and pay covered by a PAYE exclusion order (s.531AM(1)(a)(II), (III)).
- Foreign employment income that gets Transborder Workers' Relief under s.825A (s.531AM(1)(b)(iv)).
- The early childcare supplement, some employer benefits such as travel passes and Cycle to Work, childcare services relief income, Rent-a-room relief income and scholarships ([Revenue, exempt payments](https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx); full list in Tax and Duty Manual 18D-00-01, para 12).

Exempt payments are outside "aggregate income", so they do not count toward the EUR 13,000 test or the EUR 60,000 limit (s.531AM(1), (2)).

**Spouses, civil partners and maintenance.** Bands are not transferable. Where a couple is jointly assessed, the assessment on the assessable spouse or nominated civil partner may include the other's USC (s.531AV), but each USC charge is computed separately. Maintenance ([Revenue, spouses page](https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx)):
- Legally enforceable, not jointly assessed: the payer is exempt on the part of income paid as maintenance; the recipient pays USC on the part for themselves and not on the part for children.
- Separated but jointly assessed: the payer gets no exemption; the recipient is exempt.
- Voluntary: the payer pays USC on it; the recipient is exempt.
- To get the exemption during the year, contact Revenue, which writes to the employer; otherwise claim at year end on Form 12 or Form 11.

**Interaction with other charges.** USC is separate from income tax and PRSI and cannot reduce any other liability (s.531AX(1)). Compute each charge separately and add the euro amounts, never the rates.

## Deadlines and filing

| Who | What and when | Source |
|---|---|---|
| Employer or pension provider | Deducts USC on each pay day on the cumulative basis using the cut-off points on the Revenue Payroll Notification (RPN): cumulative USC to date (cumulative pay against the yearly cut-offs times periods so far over 52, 26 or 12) less USC already deducted. If cumulative USC falls, the employer refunds the difference (USC Regulations 2018, reg. 14). No RPN: 8% on all pay (reg. 19) | https://www.irishstatutebook.ie/eli/2018/si/510/made/en/html |
| Employer | Payroll submission on or before pay day; monthly USC return by the 14th of the following month; a Revenue statement not corrected is deemed the return (s.531AOA). Running payroll in detail: `ie-payroll` | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf |
| Unpaid USC of a PAYE worker | Revenue can collect it in the next year through the employer as notional pay, by adjusting credits or bands, or by assessment (s.531AY) | same |
| Self-employed and other chargeable persons | USC is due and payable as income tax is: with preliminary tax by 31 October 2026 for 2026, and the balance with the 2026 Form 11 by 31 October 2027 (s.531AS; Tax and Duty Manual 18D-00-01, para 5.2). USC can be in one assessment with income tax, even if no income tax is due (s.531AS(3), (4)) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf |
| ROS extension, 2026 | For the 2025 Form 11 balance and 2026 preliminary tax, the date is Wednesday 18 November 2026 only if the person both pays and files through ROS; if only one is done on ROS, 31 October 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| Preliminary tax | Covers income tax, PRSI and USC; the 90% / 100% / 105% tests are in `ie-preliminary-tax` | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| PAYE-only worker owed a refund (for example maintenance, or income of EUR 13,000 or less) | Claim on Form 12 in myAccount (s.531AW) | https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx |

## Penalties and interest

Part 47 of the TCA (penalties, offences, interest and other sanctions) applies to USC as it applies to income tax (s.531AAA(e); Tax and Duty Manual 18D-00-01, para 3).

| Item | Amount | Source |
|---|---|---|
| Late self-assessment return filed less than two months after the filing date | Surcharge of 5% of the tax due, up to EUR 12,695 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |
| Late return filed more than two months after the filing date | Surcharge of 10% of the tax due, up to EUR 63,485 | same |
| Late payment of income tax (and so USC) by an individual, s.1080 | 0.0219% a day | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |
| Late payment by an employer of Income Tax, PRSI, USC and LPT deducted, s.991 | 0.0274% a day | same |
| Local Property Tax not up to date | Revenue says a 10% surcharge may be added to the final liability even if income tax is filed and paid on time | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |

The surcharge follows the return, not the payment: a late Form 11 is surcharged even if the tax was paid on time. Employer fixed penalties for payroll failures are in `ie-payroll`.

## Cross-border points

- **Non-resident employees** working wholly outside Ireland with no Irish income tax charge: no USC on that income; Revenue can issue a PAYE exclusion order (Tax and Duty Manual 18D-00-01, para 16.1). Split-year leavers: arrears or a bonus paid after leaving is liable in the year paid (para 16.2).
- **Transborder Workers' Relief (s.825A):** USC does not apply to the foreign employment income covered by the relief (s.531AM(1)(b)(iv); Manual para 12.3).
- **Foreign social welfare** is exempt, like DSP payments ([Revenue, exempt payments](https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx)).
- **Foreign deposit interest** (EU and non-EU) is outside relevant income (s.531AM(1)(b)(iii)).
- **Posted and frontier workers and EU medical cards:** a person who qualifies for an Irish medical card under EU rules gets the reduced rate only if income is EUR 60,000 or less; frontier workers (including from Northern Ireland) without a full Irish medical card pay the standard rates (Manual para 13). Refer these cases.
- **Treaties:** where a treaty applies to "identical or substantially similar taxes" imposed later, Revenue has told the treaty partner that USC is substantially similar to income tax and is covered, including the relieving provisions (Tax and Duty Manual 18D-00-01, para 13.2). Check the treaty text for that clause. Treaty relief is in `ie-foreign-tax-and-withholding`.

## Worked examples

### Example 1: sole trader with capital allowances and a pension contribution

A sole trader aged 40, single, no medical card, has 2026 trading profit of EUR 60,000 before capital allowances. She claims EUR 4,000 wear and tear on plant and machinery she uses in the trade, and pays EUR 5,000 into a personal pension. She has no other income.

The capital allowances are deductible for USC because she actively carries on the trade (s.531AM(1)(b)(vii)). The pension contribution is not. Income for USC = 60,000 − 4,000 = EUR 56,000. That is above EUR 13,000, so USC is due on all of it, and her non-PAYE income is below EUR 100,000, so no surcharge. USC = 0.5% × 12,012 (60.06) + 2% × 16,688 (333.76) + 3% × (56,000 − 28,700 = 27,300) (819.00) = EUR 1,212.82. She pays it with preliminary tax by 31 October 2026 and settles any balance on the 2026 Form 11.

```oa-check
name: Sole trader, profit EUR 60,000, capital allowances EUR 4,000, pension EUR 5,000 (2026)
inputs:
  profit: 60000
  capital_allowances: 4000
  pension: 5000
steps:
  - usc_income: profit - capital_allowances
  - band1: 12012 * 0.005
  - band2: 16688 * 0.02
  - band3: (min(usc_income, 70044) - 28700) * 0.03
  - band4: max(usc_income - 70044, 0) * 0.08
  - usc: band1 + band2 + band3 + band4
expected:
  usc_income: 56000
  usc: 1212.82
```

### Example 2: aged 72, over the reduced rate limit, with a large rental profit

A man aged 72 has, in 2026: a PAYE salary of EUR 30,000 from his company, the State Pension (Contributory) of EUR 15,000, and rental profit of EUR 125,000 after allowable expenses. He claims EUR 5,000 of capital allowances on the furnishings for income tax.

The State Pension is a DSP payment, so it is exempt and left out of aggregate income. As a lessor he cannot deduct the capital allowances for USC (s.531AM(1)(b)(vii)). Aggregate income = 30,000 + 125,000 = EUR 155,000. He is over 70, but income is above EUR 60,000, so standard rates apply to all of it. USC = 60.06 + 333.76 + 3% × 41,344 (1,240.32) + 8% × (155,000 − 70,044 = 84,956) (6,796.48) = EUR 8,430.62. His non-PAYE income is EUR 125,000, which is over EUR 100,000, so the 3% surcharge applies to the EUR 25,000 excess: EUR 750.00. His salary does not count toward that test. Total USC = EUR 9,180.62. The company deducts USC from his salary through payroll; the rest is paid through self-assessment.

```oa-check
name: Aged 72, salary EUR 30,000, State Pension EUR 15,000, rental profit EUR 125,000 (2026)
inputs:
  salary: 30000
  state_pension: 15000
  rental_profit: 125000
  capital_allowances: 5000
steps:
  - aggregate: salary + rental_profit
  - band1: 12012 * 0.005
  - band2: 16688 * 0.02
  - band3: 41344 * 0.03
  - band4: (aggregate - 70044) * 0.08
  - standard: band1 + band2 + band3 + band4
  - surcharge: max(rental_profit - 100000, 0) * 0.03
  - usc: standard + surcharge
expected:
  aggregate: 155000
  standard: 8430.62
  surcharge: 750.00
  usc: 9180.62
```

## Ask the client first

1. Your 2026 income split into PAYE pay or pension, self-employed profit, rental profit and investment income. (The EUR 13,000 cliff, the bands and the non-PAYE surcharge all turn on it.)
2. Any social welfare payments, DIRT-paid interest, redundancy or other exempt income? (Taken out of the charge and the tests.)
3. Will you be 70 or over at any point in 2026, or did you hold a full medical card (not a GP visit card) at any time in 2026, and has Revenue been told? (Reduced rates, if income is EUR 60,000 or less.)
4. Do you actively carry on the trade, or are you a lessor or a passive partner? Any trading losses carried forward? (Capital allowances and losses before USC.)
5. Do you claim property-based capital allowances or Section 23 relief, and how much of it is used in 2026? Did you get a bonus from a State-supported bank? (Property relief surcharge at 5%; the 45% rate.)
6. Do you pay or receive maintenance, is it legally enforceable, and are you jointly assessed? Do you work or live outside Ireland? (Maintenance exemption; non-resident and EU cases.)

Refer to a qualified practitioner: property relief surcharge cases where the High Earners Restriction also applies, bank bonuses, Week 53 cases where the result depends on the band increase, ex-gratia redundancy above the statutory amount, posted and frontier workers, EU medical card claims, and any tax year other than 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2025 (No. 18 of 2025) s.2: amends s.531AN (2026 bands, EUR 28,700, medical card end 2028) | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html | 2026-10-24 |
| Revenue, Notes for Guidance TCA 1997 Part 18D, Finance Act 2025 edition (s.531AL to 531AAF) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf | 2026-10-24 |
| Finance Act 2011 (No. 6 of 2011) s.3: inserts Part 18D, including s.531AM(2) ("does not exceed") | https://www.irishstatutebook.ie/eli/2011/act/6/section/3/enacted/en/html | 2026-10-24 |
| Finance Act 2012 (No. 9 of 2012) s.3: inserts s.531AAE (property relief surcharge) | https://www.irishstatutebook.ie/eli/2012/act/9/section/3/enacted/en/html | 2026-10-24 |
| Revenue, Basic exemption (termination payments) | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/lump-sum-payments/basic-exemption.aspx | 2026-10-24 |
| Universal Social Charge Regulations 2018 (S.I. No. 510 of 2018), regs. 14 and 19 | https://www.irishstatutebook.ie/eli/2018/si/510/made/en/html | 2026-10-24 |
| Revenue, Tax and Duty Manual Part 18D-00-01 Universal Social Charge (last reviewed January 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf | 2026-10-24 |
| Revenue, USC overview | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx | 2026-10-24 |
| Revenue, Standard rates and thresholds of USC | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx | 2026-10-24 |
| Revenue, Reduced rates of USC | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx | 2026-10-24 |
| Revenue, Other rates of USC | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx | 2026-10-24 |
| Revenue, Payments and income exempt from USC | https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx | 2026-10-24 |
| Revenue, Calculating your USC | https://www.revenue.ie/en/jobs-and-pensions/usc/calculating-usc.aspx | 2026-10-24 |
| Revenue, USC between spouses, civil partners and on maintenance payments | https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx | 2026-10-24 |
| Revenue, How USC affects redundancy payments | https://www.revenue.ie/en/jobs-and-pensions/usc/redundancy-payments.aspx | 2026-10-24 |
| Revenue, Cumulative basis | https://www.revenue.ie/en/employing-people/paying-an-employee/methods-of-calculating-tax/cumulative-basis.aspx | 2026-10-24 |
| Revenue, Emergency Basis of Tax and USC Deduction 2026 | https://www.revenue.ie/en/jobs-and-pensions/documents/emergency-rates.pdf | 2026-10-24 |
| Revenue, Preliminary tax | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-10-24 |
| Revenue, Pay and file system (late filing surcharge) | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-10-24 |
| Revenue, eBrief 034/26 (ROS extension to 18 November 2026) | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-24 |
| Revenue, Tax and Duty Manual, Guidelines for charging interest on late payment (updated May 2025) | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-24 |

Not yet confirmed: (1) the consolidated text of Part 18D: the Law Reform Commission's Revised Acts do not include the Taxes Consolidation Act 1997 (revisedacts.lawreform.ie returns 404 for it, and it is not in the alphabetical list, checked 2026-10-24), so section wording is taken from Revenue's Notes for Guidance (Finance Act 2025 edition), checked against the enacted Finance Act 2011 s.3, Finance Act 2012 s.3 and Finance Act 2025 s.2; later amendments between 2011 and 2024 were not read in their enacting acts; (2) that the s.1084 late filing surcharge is computed on USC as part of "tax due": it follows from s.531AAA(e) applying Part 47, but no Revenue page read says so in terms; (3) the increased exemption and Standard Capital Superannuation Benefit figures for termination payments (Tax and Duty Manual Part 05-05-19, not read here); (4) Budget 2027 and Finance Bill 2026 changes to USC for 2027 were not read.

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
