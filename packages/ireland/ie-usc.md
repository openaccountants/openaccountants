---
name: ie-usc
description: Use this skill whenever asked about Ireland's Universal Social Charge (USC) for self-employed individuals or any taxpayer. Trigger on phrases like "USC calculation", "universal social charge", "USC rates Ireland", "USC bands", "USC surcharge", "USC self-employed", "USC medical card", "USC exemption", or any question about USC obligations. This skill covers standard rates and bands, the self-employed surcharge, exemptions, reduced rates for medical card holders and over-70s, and edge cases. ALWAYS read this skill before touching any Irish USC work.
version: 2.0
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland Universal Social Charge (USC)

This Guide works out the Universal Social Charge (USC) for an individual in Ireland: the exemption test, the standard rate bands, the reduced rates for people aged 70 or over and full medical card holders, the surcharge on non-PAYE income, and how USC is paid. Figures are for tax year 2026. The Irish tax year is the calendar year. Every figure below comes from a Revenue page or the Revenue Tax and Duty Manual on USC, linked in the table that holds it.

## Section 1: Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Ireland |
| Authority | Revenue Commissioners |
| Law | Part 18D of the Taxes Consolidation Act 1997 (sections 531AL to 531AAF), per the Revenue Tax and Duty Manual Part 18D-00-01 |
| Who pays | Each individual, on their own income. Spouses and civil partners are charged separately and cannot transfer bands |
| Exemption test | A cliff, not an allowance: see Section 3 |
| How it is paid | Employees: deducted by the employer or pension provider. Self-employed: with preliminary tax and the balance on the Form 11 |
| Currency | EUR |

**2026 standard rates and bands.** Revenue prints each band as a WIDTH ("Next"), not as a cumulative ceiling. Apply the bands in order to total income.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx |
| Band 1: the first part of income | EUR 12,012 | "First" |
| Rate on band 1 | 0.5% | "Standard rates and thresholds of USC for 2026" |
| Band 2: the next part of income (a width) | EUR 16,688 | "Next" |
| Rate on band 2 | 2% | "Threshold for 2026" |
| Band 3: the next part of income (a width) | EUR 41,344 | "Next" |
| Rate on band 3 | 3% | "Threshold for 2026" |
| Rate on the balance above band 3 | 8% | "Balance" |

## Section 2: Required inputs and refusal catalogue

### Required inputs

Before computing any USC figure, get these facts. If the tax year is unknown, stop: the bands change from year to year (compare the 2025 and 2026 rows on the standard rates page linked in Section 1).

1. The tax year.
2. Total income for USC, built as Section 3 describes: employment income, taxable benefits, self-employed profit, rental income, share option gains and dividends, after deducting capital allowances only where the person actively carries on the trade, for plant, machinery and certain buildings, and with no deduction for employee pension contributions.
3. Which parts of that income are exempt payments (Department of Social Protection payments and similar payments, DIRT-paid interest, the other exempt items in Section 3).
4. Age on 31 December of the tax year: does the person reach 70 in the year?
5. Did the person hold a FULL medical card (not a GP visit card) at any time in the year, and have they told Revenue?
6. How much of the income is non-PAYE income (self-employed, rental, investment)?
7. Any income sheltered by property or area-based incentive reliefs (for example Section 23 relief)?
8. Any bonus from a bank that received State support?

### Refusal catalogue

- **R-IE-USC-1: Cross-border USC treatment.** Trigger: a non-resident, a frontier worker, a person with foreign employment income under Transborder Workers Relief, or a person covered by another EU state's social security scheme who claims a medical card under EU rules. Message: "Cross-border USC treatment depends on facts this Guide does not cover. Refer to a qualified practitioner." The Tax and Duty Manual (Section 3 table) treats these cases in its own chapters.
- **R-IE-USC-2: Property relief surcharge.** Trigger: income sheltered by property or area-based incentive reliefs, especially with the High Earners Restriction. Message: "The property relief surcharge needs the relief ordering rules in the Tax and Duty Manual. Refer."
- **R-IE-USC-3: Bank bonuses.** Trigger: a bonus from a State-supported bank. Refer.

### Prohibitions

- Never compute USC without confirming the tax year.
- Never apply USC when total income does not exceed the exemption limit in Section 3. Never charge USC only on the excess above it: above the limit, USC is due on the FULL income.
- Never apply reduced rates unless BOTH tests in Section 4 are met: (aged 70 or over OR a full medical card holder) AND income at or below the reduced rate income limit.
- Never apply reduced rates to part of the income of someone above the reduced rate income limit. Above that limit, standard rates apply to ALL income.
- Never apply the non-PAYE surcharge to PAYE income, or to total income above the surcharge threshold. It applies only to the non-PAYE income that exceeds the threshold.
- Never confuse the two rules that use the same threshold figure in Section 4: the non-PAYE surcharge and the property relief surcharge.
- Never conflate USC with income tax or PRSI. They are separate charges.
- Never reduce USC by income tax credits. A person with no income tax to pay because of credits can still owe USC (Tax and Duty Manual, Section 3 table).
- Never pool USC bands between spouses or civil partners.

## Section 3: Exemption test

**Exemption test and what counts as income.** Law: section 531AM of the Taxes Consolidation Act 1997.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx |
| Exemption limit for 2026: if total income exceeds it, USC is due on the full income | EUR 13,000 | "you pay USC on your full income" |

The test is a cliff. If total income for the year does NOT exceed the limit in the table above, no USC is due. If it exceeds the limit by any amount, USC is charged on the whole income, from the first euro, at the Section 1 rates. Income exactly at the limit is exempt: the Tax and Duty Manual says the exemption applies "Where an individual’s total income for a year does not exceed" the limit. (Revenue's exempt payments page says income "less than the exemption limit" is exempt; the statute wording in the Manual governs, see the Sources section.)

What counts (Revenue USC overview page, linked above): "employment income taxable employer benefits self-employed income rental income share option gains and dividend income". A person actively carrying on a trade deducts standard-rate capital allowances for plant and machinery and certain buildings before USC. The Manual: "Any capital allowances due to persons that do not actively carry on a trade are not deductible. Therefore, lessors and other passive investors, such as non-active partners in a partnership trade, must pay USC on gross income before the deduction of capital allowances." Accelerated allowances are not deductible, apart from farm buildings. Losses: "Losses, other than those arising from the carrying on of a trade or profession, are not deductible before USC is charged." (Manual, Sections 7 and 8). "There is no relief from USC for employee pension contributions."

**Payments and income that are not charged to USC.**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx |
| Exemption limit for 2026 (same figure as the table above) | EUR 13,000 | "The exemption limit for 2026 is" |

Not charged to USC, per that page: payments from the Department of Social Protection (DSP); payments similar to DSP payments made by another body (for example the Community Employment Scheme, VTOS, Youthreach, and social welfare payments from another country); income on which DIRT has already been paid; the early childcare supplement; some employer benefits such as travel passes and Cycle to Work; income under childcare services relief; income under Rent-a-room relief; scholarship income; pre-retirement access to AVCs; and statutory redundancy payments under the Redundancy Payments Act 1967. Ex-gratia redundancy above the statutory amount is exempt only up to limits set elsewhere, so refer (Revenue, How USC affects redundancy payments). The full list is in Section 12 of the Tax and Duty Manual.

Do DSP payments count toward the exemption test? No Revenue page we read says they do. The Manual defines the income liable to USC as "relevant emoluments" plus "relevant income"; relevant emoluments "do not include" payments under the Social Welfare Acts, and relevant income leaves out deposit interest. Treat DSP payments and DIRT-paid deposit interest as outside both the charge and the test. If the answer turns on this point, refer (Section 9).

## Section 4: Standard bands, surcharge, and reduced rates

### Self-employed surcharge (non-PAYE income)

**Other rates of USC.**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx |
| Surcharge on non-PAYE income | 3% | "if your non-PAYE income is more than" |
| Non-PAYE income threshold for the surcharge (MORE than this, per year) | EUR 100,000 | "a year" |
| Rate on the full amount of certain bank bonuses | 45% | "applies to the full amount of certain bank bonuses" |
| Bank bonuses at or below this in a year: standard rates apply | EUR 20,000 | "or less in a year, the standard rates of USC apply" |
| Property relief surcharge on taxable income sheltered by property or area-based reliefs | 5% | "sheltered" |
| Property relief surcharge does not apply if gross income is LESS than | EUR 100,000 | "does not apply if your gross income is less than" |

**How the non-PAYE surcharge works.** It applies to the individual whose NON-PAYE income (self-employed profit, rental, investment income) is more than the threshold in the table above. PAYE salary does not count toward that threshold. The surcharge is charged only on the part of the non-PAYE income that exceeds the threshold, on top of the band rate. Total income above the threshold is not enough: someone with a large salary and modest self-employed profit pays no surcharge.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf |
| Rate that applies to the non-PAYE income above the surcharge threshold (band rate plus surcharge) | 11% | "applies to the non-PAYE income that exceeds" |
| Worked example (Revenue): gross income | EUR 150,000 | "Sinead has annual gross income of" |
| of which PAYE salary | EUR 40,000 | "PAYE salary" |
| of which non-PAYE investment income | EUR 110,000 | "non-PAYE investment income" |
| non-PAYE income above the threshold, charged the surcharge | EUR 10,000 | "The amount of non-PAYE income that exceeds" |
| USC for 2026 | EUR 8,330.62 | "Sinead’s USC liability for 2026 is therefore" |
| Reduced rates: the most a qualifying person pays | 2% | "only pay USC at a maximum rate of" |

**Two rules share the same threshold figure. Keep them apart.**
- Non-PAYE surcharge: test = NON-PAYE income; direction = MORE than the threshold; charged on the excess only.
- Property relief surcharge: test = gross (aggregate) income; it does not apply if that income is LESS than the threshold, so it can apply at exactly the threshold; charged on the part of taxable income sheltered by the specified property reliefs, whatever its size. The Manual adds: "There is no upper income limit." Refer (R-IE-USC-2).

### Formula (2026)

Apply this per person. Use the band widths and rates in Section 1; do not use cumulative ceilings from memory.

~~~
1. If total income for USC does not exceed the Section 3 exemption limit: USC = 0. Stop.
2. If the person qualifies for reduced rates (all tests below): band 1 at the band 1 rate,
   then ALL the rest at the reduced balance rate. Go to step 5.
3. Otherwise standard rates: band 1 at the band 1 rate, the next band 2 width at the band 2
   rate, the next band 3 width at the band 3 rate, the balance at the balance rate.
4. Non-PAYE surcharge: if non-PAYE income is more than the surcharge threshold, add the
   surcharge rate on (non-PAYE income minus the threshold).
5. Add any property relief surcharge or bank bonus charge only after referral.
~~~

### Reduced rates (medical card / aged 70+)

**Reduced rates of USC.**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx |
| Income limit for reduced rates (income at or below this) | EUR 60,000 | "Reduced rates of USC will apply if your income is" |
| Reduced rate on the first part of income | 0.5% | "The reduced rates for 2026 are" |
| First part of income at the reduced first rate | EUR 12,012 | "on the first" |
| Reduced rate on the balance | 2% | "on the balance" |

The reduced rates apply only when BOTH conditions are met:
- Condition one: the person is aged 70 or older, OR holds a FULL medical card (not a GP visit card).
- Condition two, which must ALSO be met: income for the year is at or below the income limit in the table above.

If income is more than the limit, the reduced rates are lost on ALL income, not just the excess. Revenue says that above the limit "the standard rates of USC apply. You cannot avail of the reduced rates." This is a cliff.

Timing. The reduced rates apply for the whole year when the person reaches 70 in the year, or holds a full medical card "at any time during the year". A medical card holder must contact Revenue to get the reduced rate. Other cards do not qualify: the Manual names the GP Visit Card, the Drugs Payment Scheme Card, the Long-Term Illness Scheme Card and the European Health Insurance Card.

End date. For full medical card holders aged under 70, the reduced rate "shall cease to have effect from the 2028 year of assessment onwards" (Manual, Section 4.1). It applies for 2026 and 2027. The age 70 route has no end date in the Manual.

## Section 5: USC and other charges interaction

| Question | Answer |
| --- | --- |
| Is USC part of PRSI? | No. PRSI is a separate charge, not covered by this Guide |
| Do income tax credits reduce USC? | No. The Manual: a person with no income tax liability because of tax credits, losses or capital allowances "may still have a liability to USC" |
| Are pension contributions deducted before USC? | No for employee contributions. Employer PRSA and PEPP contributions are exempt from USC (Manual, Section 11) |
| Are capital allowances deducted before USC? | Yes, for a person actively carrying on the trade; not for lessors and passive investors (Manual, Section 7) |
| Does USC apply to DSP payments? | No (Section 3) |
| Does USC apply to deposit interest that has had DIRT deducted? | No (Section 3) |
| Spouses and civil partners | Each is charged individually. "USC rate thresholds are non-transferable between spouses or civil partners" (spouses page in the Sources section) |
| Legally enforceable maintenance paid by a separated spouse | Legally enforceable maintenance paid by a separated spouse or civil partner who is NOT jointly assessed: the payer is exempt on the part of income paid as maintenance; the recipient pays USC on the part for themselves but not on the part for children. Separated couples who are jointly assessed for income tax: the payer gets no exemption and pays USC on the maintenance; the recipient is exempt. Voluntary maintenance: the payer pays USC on it and the recipient is exempt (spouses page) |

## Section 6: Payment schedule

**Payment.**

| Payment method | Detail |
| --- | --- |
| PAYE employees and pensioners | The employer or pension provider deducts USC from pay, under the Universal Social Charge Regulations 2018 (Manual, Section 5.1) |
| Self-employed | Pay USC with preliminary tax by 31 October of the tax year, and any balance by 31 October of the following year (Manual, Section 5.2). Preliminary tax covers income tax, PRSI and USC (Revenue preliminary tax page) |
| Pay and file through ROS in 2026 | For the 2025 Form 11 balance and 2026 preliminary tax, the date is extended to Wednesday 18 November 2026, but only if the person BOTH pays AND files through ROS. If only one is done through ROS, the date stays 31 October 2026 (Revenue eBrief 034/26) |

## Section 7: Total marginal burden context

The live version of this Guide showed combined income tax, PRSI and USC rates. Those combined rates are not printed on any Revenue page and the PRSI rate it used was out of date, so they are removed. Work out income tax, PRSI and USC separately and add the euro amounts, never the rates. The only combined rate Revenue prints for USC is the rate on non-PAYE income above the surcharge threshold, in the Section 4 table.

## Section 8: Edge case registry

Worked amounts below come from Revenue's own examples (pages linked in the tables) unless marked hypothetical.

**Revenue examples, 2026.**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/jobs-and-pensions/usc/calculating-usc.aspx |
| Jacob, aged 32, self-employed: income | EUR 25,000 | "is self-employed and earns" |
| Jacob: USC | EUR 319.82 | "Total" |
| Sadhbh, aged 45: income | EUR 50,000 | "Sadhbh, aged 45, earns" |
| Sadhbh: USC | EUR 1,032.82 | "Total" |
| Donnchadh, aged 55, full medical card, has told Revenue: USC on the same income as Sadhbh | EUR 819.82 | "Total" |
| Cian, aged 75: income above the reduced rate limit | EUR 75,000 | "who earns" |
| Cian: USC at standard rates | EUR 2,030.62 | "Total" |

### EC1: Income exactly at the exemption limit

Total income equals the Section 3 limit. Exempt: the Manual's test is "does not exceed".

### EC2: Income just above the exemption limit (hypothetical)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf |
| Manual example: gross income below the limit, no USC | EUR 12,500 | "no USC applies" |
| Manual example: gross income above the limit, USC on the full amount | EUR 13,500 | "USC applies to the full" |
| Hypothetical USC on that amount at 2026 standard rates (our arithmetic: band 1, then the rest at the band 2 rate) | EUR 89.82 | Case B in the test suite |

### EC3: Medical card holder or person aged 70+ just above the reduced rate limit

Standard rates apply to ALL income. Cian in the Revenue examples table is aged 75 and pays standard rates on the whole of his income.

### EC4: Mixed PAYE and non-PAYE income, surcharge test

Test the surcharge on non-PAYE income only. In the Revenue Sinead example (Section 4), only the non-PAYE income above the threshold carries the surcharge; her PAYE salary does not. A person whose non-PAYE income is at or below the threshold pays no surcharge however large their salary.

### EC5: DSP payments alongside other income

DSP payments are not charged to USC. Leave them out of the charge, and (Section 3) out of the exemption test. Refer if the outcome depends on the test.

### EC6: DIRT-paid deposit interest

Not charged to USC. Leave it out.

### EC7: Week 53 pay day

When PAYE pay is paid on 31 December (or 30 or 31 December in a leap year), the bands, the reduced rate income limit and the exemption limit are increased by 1/52 for weekly pay or 1/26 for fortnightly pay, restricted to the actual PAYE income on that day, and not where pay days were changed to gain the wider bands (Manual, Section 4.2). Refer if it matters.

## Section 9: Reviewer escalation protocol

When a situation requires reviewer judgement:

~~~
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified practitioner must confirm before advising client.
~~~

When a situation is outside the scope of this Guide:

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside the scope of this Guide]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
~~~

## Section 10: Test suite

Use the Revenue examples in Section 8 and Section 4 as the tests. Each must reproduce exactly.

- Test 1 (ordinary): Sadhbh. Standard rates on income above band 2. Expected USC: the Sadhbh value in the Revenue examples table.
- Test 2 (exempt): income in the Manual example below the limit (EC2 table). Expected: no USC.
- Test 3 (cliff, hypothetical): income in the Manual example above the limit (EC2 table). Expected: the hypothetical USC in the EC2 table, charged on the full income.
- Test 4 (reduced rates): Donnchadh. Full medical card, told Revenue, income at or below the limit. Expected: the Donnchadh value.
- Test 5 (reduced rates lost): Cian. Aged 75 but income above the limit. Expected: the Cian value at standard rates.
- Test 6 (surcharge, mixed income): Sinead. Expected: the Sinead value in the Section 4 table, with the surcharge on the non-PAYE excess only.

## The method, step by step

1. Fix the tax year and confirm it is 2026. Use the 2026 bands on the [standard rates page](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx).
2. Build total income for USC under section 531AM of the Taxes Consolidation Act 1997: include the income types on the [Revenue USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx), deduct capital allowances only where the person actively carries on the trade, for plant, machinery and certain buildings, do not deduct employee pension contributions.
3. Remove exempt payments and income listed on the [exempt payments page](https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx) and in Section 12 of the [Tax and Duty Manual Part 18D-00-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf).
4. Apply the exemption cliff in Section 3 ([Revenue USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx)). At or below the limit: no USC. Above: USC on the full income.
5. Test reduced rates on the [reduced rates page](https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx): (aged 70 or over in the year OR full medical card at any time in the year) AND income at or below the limit. For a medical card holder under 70, confirm the year is 2027 or earlier ([Manual](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf), Section 4.1).
6. Apply the bands in order: reduced rates if step 5 passed, otherwise the standard band widths and rates ([standard rates page](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)).
7. If non-PAYE income is more than the surcharge threshold, add the surcharge on the non-PAYE excess only ([other rates page](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx); [Manual](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf), Section 4.3).
8. Check for property-relief-sheltered income and bank bonuses ([other rates page](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx)). If present, refer.
9. Compute each spouse or civil partner separately ([spouses page](https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx)).
10. Payment: PAYE income through the employer; self-employed with [preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx) by 31 October and the balance on the Form 11, or by the later ROS date in [eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx) if paying AND filing through ROS.

## Ask the client first

- What is your total income for the year, split into PAYE pay, self-employed profit, rental income and investment income? (Exemption cliff, bands, and the non-PAYE surcharge all turn on it.)
- Did you receive any social welfare payments, DIRT-paid interest or other exempt income? (Removed from the charge.)
- Will you be 70 or over at any point this year, or did you hold a full medical card (not a GP visit card) at any time this year, and has Revenue been told? (Reduced rates.)
- Do you claim any property-based capital allowances or Section 23 relief, or carry forward losses from them? (Property relief surcharge.)
- Do you pay maintenance to, or receive it from, a separated spouse or civil partner, and is it legally enforceable, and are you still jointly assessed? (Maintenance exemption.)
- Are you an active trader or a passive investor or lessor? (Capital allowances before USC.)
- Do you pay and file through ROS? (Payment date.)

## When to refuse or refer

- Non-residents, frontier workers, Transborder Workers Relief, and EU social security cases (R-IE-USC-1).
- Any income sheltered by property or area-based reliefs, especially with the High Earners Restriction (R-IE-USC-2).
- Bonuses from a State-supported bank (R-IE-USC-3).
- A Week 53 pay day where the result depends on the band increase (EC7).
- A result that turns on whether DSP payments count toward the exemption test (Section 3).
- A tax year other than 2026. Budget 2027 is due in October 2026 and will change figures for 2027 only.
- Ex-gratia redundancy payments (limits are outside this Guide).

## Sources

- Revenue, Universal Social Charge overview: https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx
- Revenue, Standard rates and thresholds of USC: https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx
- Revenue, Reduced rates of USC: https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx
- Revenue, Other rates of USC: https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx
- Revenue, Payments and income exempt from USC: https://www.revenue.ie/en/jobs-and-pensions/usc/exempt-payments-income.aspx
- Revenue, Calculating your USC: https://www.revenue.ie/en/jobs-and-pensions/usc/calculating-usc.aspx
- Revenue, USC between spouses, civil partners and on maintenance payments: https://www.revenue.ie/en/jobs-and-pensions/usc/married-couples-civil-partners.aspx
- Revenue, Tax and Duty Manual Part 18D-00-01 Universal Social Charge (last reviewed January 2026): https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-18d/18D-00-01.pdf
- Revenue, Preliminary tax: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx
- Revenue, eBrief 034/26: https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx
- Revenue, How USC affects redundancy payments: https://www.revenue.ie/en/jobs-and-pensions/usc/redundancy-payments.aspx

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
