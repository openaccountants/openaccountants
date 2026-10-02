---
name: ie-prsi-class-s
description: Use this skill whenever asked about Irish PRSI Class S contributions for self-employed individuals. Trigger on phrases like "PRSI self-employed", "Class S contributions", "how much PRSI do I pay", "PRSI calculation Ireland", "self-employed social insurance Ireland", "PRSI threshold", or any question about PRSI obligations for a self-employed client in Ireland. This skill covers Class S rates, minimum contribution, income threshold, payment schedule, interaction with income tax, and edge cases. ALWAYS read this skill before touching any Irish PRSI Class S work.
version: 2.0
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland PRSI Class S for the self-employed

This Guide covers Pay Related Social Insurance (PRSI) at Class S in Ireland: who pays it, on what income, at which rate, and how it is paid through self-assessment or payroll. Figures are for tax year 2026. The Irish tax year is the calendar year. The Class S rate changed on 1 October 2026, so the rate you use depends on HOW the person pays (self-assessment or payroll) and WHICH year's income you are working on. The tables below say which rate applies to whom.

## Section 1: Quick reference

### Department of Social Protection, PRSI Class S Rates page (last updated 20 January 2026)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| Rate for 2026 self-employed income returned through Revenue self-assessment (the "blended" rate) | 4.2375% | "for 2026 income the rate will be 4.2375% or min payment of €650" |
| Minimum annual Class S contribution | EUR 650 | "the minimum annual contribution for Class S is €650" |
| Rate for 2025 self-employed income returned through self-assessment (the 2025 Form 11 filed in 2026). NOT the 2026 rate. | 4.125% | "a blended or proportionate rate of 4.125% or a minimum payment of €650 will apply on their self-employed 2025 annual income" |

### Department of Social Protection, SW14 PRSI Contribution Rates and User Guide, January 2026

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Class S period rate, 1 January to 30 September 2026 | 4.2% | "pay Class S PRSI at the rate of 4.2% until 30 September 2026 (4.35% from 1 October 2026)" |
| Class S period rate, from 1 October 2026 | 4.35% | "pay Class S PRSI at the rate of 4.2% until 30 September 2026 (4.35% from 1 October 2026)" |
| Annual income at which Class S starts (this amount or more) | EUR 5,000 | "Self-employed contributors with annual income of €5,000 or over pay Class S PRSI" |
| Voluntary contribution for a person who last paid compulsory PRSI at Class S (flat amount per contribution year) | EUR 650 | "There is a flat rate of €650 for persons who last paid PRSI at Class S" |

**Which rate applies to whom (2026):**

| Who | Income | Rate to use |
| --- | --- | --- |
| Self-employed person who returns PRSI through Revenue self-assessment (Form 11) | 2026 income (Form 11 for 2026, filed in 2027) | The blended 2026 rate in the Class S Rates table above, or the minimum, whichever is greater. Do not apply the two period rates separately. |
| Same person | 2025 income (Form 11 for 2025, due in 2026) | The 2025 blended rate in the Class S Rates table above, or the minimum, whichever is greater. |
| Self-employed company director whose PRSI is collected under PAYE | Pay in each week of 2026 | The period rate for the week. SW14 prints Class S as weekly pay bands with one rate per period ("Up to €500 S0 All 4.20% ... More than €500 S1 All 4.20%" to 30 September 2026; both subclasses 4.35% from 1 October 2026) and says "Self-employed company directors pay their PRSI under the PAYE system". The blended rate is printed only "For those returning PRSI through the Revenue self-assessed system". The director must check the deduction: DSP says it is "the responsibility of each company director to ensure that the correct amount of PRSI has been deducted and remitted to the Revenue Commissioners" ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)). |
| Anyone estimating 2026 preliminary tax on the current-year option | 2026 income | The 2026 blended rate, because preliminary tax is an estimate of the 2026 self-assessed liability. |

| Field | Value |
| --- | --- |
| Country | Ireland |
| Authority | Department of Social Protection (DSP) sets the class and rate; Revenue collects Class S through self-assessment or PAYE |
| Primary legislation | Social Welfare Consolidation Act 2005, as amended, Chapter 3 of Part II (self-employed contributors) and Part III of the First Schedule (excluded persons); Social Welfare (Consolidated Contributions and Insurability) Regulations 1996, S.I. 312 of 1996, Chapter 2 of Part II ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)) |
| Upper earnings limit | None. SW14 charges Class S "on all reckonable income". |
| Payment method | Self-assessment (Form 11) with income tax and USC; PAYE for self-employed company directors |
| Currency | EUR only |

## Section 2: Who pays Class S, and who does not

### DSP leaflet, A Guide to PRSI for the Self-Employed (January 2025)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf |
| Who pays | (no figure) | "People whose only income is from investments, rents or maintenance payments" |
| Employees with self-employment | (no figure) | "Employees who are also self-employed pay Class S PRSI in addition to their PRSI contribution as an employee" |
| Employees with only unearned other income | (no figure) | "People insured as employees whose only other income is unearned such as share dividend payments or rent. They may be liable for PRSI contributions at Class K on this income" |

This leaflet is dated January 2025 and prints 2025 rates. Use it only for WHO pays and WHAT income counts, never for a rate. The rates are in the Section 1 tables.

1. **Who pays.** Self-employed people pay Class S if their annual income is at or above the threshold in the SW14 table above (EUR 5,000 or over, not "more than"). The leaflet lists farmers, professionals, contractors and sub-contractors, people in business on their own or in partnership, people whose ONLY income is investments, rents or maintenance payments, employees who are ALSO self-employed (Class S in addition to their employee class), and councillors on their local authority emoluments ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
2. **Who does not pay Class S** ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)):
   - prescribed relatives (son, daughter, parent, brother or sister) who help in the business but are not partners (spouses and civil partners are not excluded relatives: the [DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/) list "spouses or civil partners of self-employed contributors who participate in the business" as Class S payers);
   - people whose total income from self-employment (earned and unearned) and employment is below the threshold;
   - people Revenue classes as non-resident who hold solely unearned income, and non-resident directors of Irish companies;
   - employees whose ONLY other income is unearned (dividends, rent): they may pay Class K on it, not Class S;
   - people under pensionable age with an occupational pension whose only other income is unearned: Class K, not Class S;
   - public servants paying PRSI at Class B, C or D (modified rate contributors, for example civil and public servants recruited before 6 April 1995) who are also self-employed: Class K on that income ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/); [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
3. **Age.** Class S is paid from age 16 up to pension age, currently 66. A person born on or after 1 January 1958 who is aged 66 to 70 and has NOT been awarded the State Pension (Contributory) still pays ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)). Revenue says the change applies from 1 January 2024 and does not apply to a person already getting the State Pension (Contributory), or who was 66 by 1 January 2024 (born before 1 January 1958) ([Revenue PRSI page](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)). So turning 66 does NOT end Class S for everyone.

### DSP, PRSI and Family Employment (last updated 15 April 2025)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/ |
| Proprietary director shareholding at which Class S applies (this share or more, directly or indirectly) | 50% | "proprietary directors who own or control 50% or more of the shareholding of a company, either directly or indirectly e.g., through a holding company, are classified as self-employed" |

4. **Company directors.** Since 1 July 2013 a proprietary director who owns or controls the share in the table above OR MORE, directly or indirectly (for example through a holding company), is self-employed and pays Class S. Below that share, DSP decides case by case; it is NOT automatically Class A and NOT automatically Class S ([DSP family employment page](https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/)). A self-employed company director pays PRSI under the PAYE system, not through a separate Class S registration, where the directorship is the only self-employed income ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); [DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).

## Section 3: What income counts

5. **Income included.** Class S is paid on total income: benefit in kind, trade or profession income, interest, annuities and foreign investment income, Irish rent, income taxed at source (bank interest, maintenance payments), share dividends and ARF dividends, and certain taxable employment income such as a company director's ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)). Revenue: "Your PRSI is calculated on your gross income once any capital allowances have been deducted", and you must also pay PRSI on rental income or legally enforceable maintenance payments ([Revenue PRSI page](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)).
6. **Income excluded.** Capital allowances; social welfare payments; pensions taxed under PAYE; redundancy and termination payments taxed under PAYE; SOLAS training payments and HSE Mobility Allowance taxed under PAYE; income continuance payments taxed under PAYE; early AVC withdrawals taxed under PAYE; certain retirement lump sums above the lifetime tax-free limit; certain foreign life policy and offshore fund gains; and certain chargeable excesses on a Benefit Crystallisation Event ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
7. **No cap.** There is no upper earnings limit: SW14 charges Class S on all reckonable income.

## The method, step by step

1. **Fix the income year and the payment route.** Ask whether you are working on 2026 income or 2025 income, and whether PRSI is returned through Form 11 self-assessment or deducted under PAYE as a self-employed director. This decides the rate (see "Which rate applies to whom" in Section 1, [DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)).
2. **Check the class.** Confirm the person is self-employed, or a proprietary director at or above the shareholding in the family employment table, or has only investment, rent or maintenance income. If the person is an employee whose only other income is unearned, or a modified-rate public servant, stop: that is Class K, not this Guide ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
3. **Check age.** Under 16: no Class S. 66 to 70: Class S still applies if born on or after 1 January 1958 and not awarded the State Pension (Contributory) ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); [Revenue PRSI page](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)).
4. **Work out reckonable income.** Gross income after capital allowances, including the income types listed in Section 3 and leaving out the excluded items ([Revenue PRSI page](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx); [DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
5. **Apply the annual test.** If annual income is below the SW14 threshold, no Class S is due (consider a voluntary contribution, Section 6). If it is at or above the threshold, Class S is due on ALL of it, not on the excess ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
6. **Compute.** Self-assessed: Class S = the greater of (reckonable income x the blended rate for that income year) and the minimum in the Class S Rates table ([DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)). Payroll-collected director: the employer deducts at the period rate for each week (SW14 table).
7. **Pay with the self-assessment.** Class S is paid to Revenue with income tax and USC: preliminary tax for the year by 31 October of that year, and the Form 11 return and balance for the previous year by the same date ([Revenue pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx); [Revenue preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). See Section 5 for the ROS extension.

~~~
Self-assessed Class S for an income year:
  if reckonable_income < annual threshold      -> Class S = 0
  else Class S = max(reckonable_income x blended_rate_for_that_year, minimum)
Use the 2026 blended rate for 2026 income and the 2025 blended rate for 2025 income.
Never apply the two period rates of one year separately on a Form 11.
~~~

## Section 4: Worked examples (hypothetical amounts)

All incomes below are hypothetical, chosen to show the method. Rates and the minimum come from the Section 1 tables.

| Case | Hypothetical facts | Result |
| --- | --- | --- |
| A, ordinary, 2026 | Sole trader, aged 45, reckonable 2026 income EUR 80,000, Form 11 | EUR 80,000 x 4.2375% = EUR 3,390.00. This is above the minimum, so EUR 3,390.00 is due. [DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/) |
| B, minimum, 2026 | Self-employed, 2026 reckonable income EUR 12,000, Form 11 | EUR 12,000 x 4.2375% = EUR 508.50. That is below the minimum, so EUR 650 is due. [DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/) |
| C, below threshold | Self-employed, total annual income EUR 4,800, no employment | Below the annual threshold: no Class S. Consider whether a voluntary contribution makes sense. [SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf) |
| D, 2025 income filed in 2026 | Sole trader, 2025 reckonable income EUR 50,000, 2025 Form 11 | EUR 50,000 x 4.125% = EUR 2,062.50, using the 2025 blended rate, not the 2026 rate. [DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/) |

## Section 5: Payment schedule and registration

### Revenue, Who should register for Income Tax self-assessment?

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx |
| Taxable non-PAYE income above which you MUST register for self-assessment | EUR 5,000 | "your taxable non-PAYE income exceeds €5,000 or your gross non-PAYE income exceeds €30,000" |
| Gross non-PAYE income above which you MUST register (either test is enough) | EUR 30,000 | "your taxable non-PAYE income exceeds €5,000 or your gross non-PAYE income exceeds €30,000" |

The registration test (more than the amounts above, either test) is a different rule from the Class S income test (EUR 5,000 or over). Same digits, two rules. Self-employed people register using eRegistration or Form TR1 parts A and B ([Revenue registration page](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). A person whose only self-employed income is a company directorship does not register as self-employed, because tax and PRSI are collected under PAYE ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).

### Revenue, What is preliminary tax?

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Preliminary tax safe harbour, current year | 90% | "90% of the tax due for that tax year" |
| Preliminary tax safe harbour, previous year | 100% | "100% of the tax due for the immediately previous tax year" |
| Preliminary tax safe harbour, pre-preceding year, direct debit only, not if that year's tax was nil | 105% | "105% of the tax due for the tax year preceding the immediately previous tax year" |

Preliminary tax is the estimate of income tax, PRSI and USC for the year. It must equal or exceed the LOWEST of the three options in the table above, and it is due by 31 October of the tax year ([Revenue preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).

| Event | Deadline | Source |
| --- | --- | --- |
| 2026 preliminary tax (income tax, PRSI and USC) | 31 October 2026 | [Revenue preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx) |
| 2025 Form 11 return and 2025 balance | 31 October 2026 | [Revenue pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |
| ROS extension, only if BOTH paying and filing through ROS (2025 return, 2025 balance, 2026 preliminary tax) | Wednesday 18 November 2026 | [Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx) |
| 2026 Form 11 return and 2026 balance (Class S at the 2026 blended rate) | 31 October 2027; any 2027 ROS extension is not yet announced | [Revenue pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |

If only one of paying or filing is done through ROS, the extension does not apply and the date stays 31 October 2026 ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).

### DSP, Operational Guidelines: PRSI for the Self-Employed (last updated 6 January 2026)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/ |
| Share of the year's income tax and PRSI charged that must be paid before the year's 52 Class S contributions are awarded | 100% | "When the full amount (100%) of income tax and PRSI charged has been paid, an annual complement of 52 Class S contributions are awarded. Where less than the full amount due has been paid, no contributions are awarded." |
| Flat-rate Class S contribution paid direct to DSP by a person with income of EUR 5,000 or more whom Revenue excused from making returns (No Net Liability case) | EUR 310 | "Persons whose annual income is €5,000 or more, who have been deemed to have no tax liability by the Revenue Commissioners and who are subsequently excused from making annual returns by the Inspector of Taxes, are required to pay a flat rate of €310 direct to this department" |

A part payment earns no contributions for the year: DSP awards the 52 Class S contributions only when the full amount in the table above has been paid ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)).

## Section 6: Voluntary contributions and benefits

- **Voluntary contributions.** A person no longer covered by compulsory PRSI (for example they stopped self-employment, or income fell below the threshold), who is under pension age, or aged 66 to 70 without an award of the State Pension (Contributory), may opt to pay voluntary contributions if they meet the conditions. For a person who last paid at Class S it is the flat amount in the SW14 table above. Apply within 60 months from the end of the contribution year in which a contribution was last paid or credited ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)). Voluntary contributions cover only the pensions the person was covered for when last paying compulsory PRSI ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)). Confirm the contribution record with DSP before advising.
- **Benefits Class S covers** ([DSP Class S Rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)): Adoptive Benefit, Benefit Payment for 65 Year Olds, Carer's Benefit, Guardian's Payment (Contributory), Invalidity Pension, Jobseeker's Benefit for the Self-Employed, Maternity Benefit, Parent's Benefit, Partial Capacity Benefit, Paternity Benefit, State Pension (Contributory), Treatment Benefit, and Bereaved Partner's (Contributory) Pension. The leaflet adds: "Class S PRSI does not provide cover for any other schemes or benefits" ([DSP leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
- **Share fishermen and fisherwomen** classed as self-employed may pay an optional Class P contribution on top of Class S ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)). This Guide does not compute Class P.

## Section 7: Interaction with USC and income tax

- PRSI, USC and income tax are three separate charges. Revenue collects all three together through preliminary tax and the Form 11 balance ([Revenue preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- The pages read for this Guide do not say whether Class S is deductible in computing taxable income, or whether income tax credits reduce PRSI. Do not state either as fact; ask the accountant.

## Section 8: Edge case registry

### EC1: income exactly at the threshold
Situation: total annual income equals the SW14 threshold. Resolution: Class S applies, because the test is "or over". The calculated amount is below the minimum, so the minimum in the Class S Rates table is due.

### EC2: income just below the threshold
Situation: total annual income is below the SW14 threshold. Resolution: no Class S. Consider a voluntary contribution (Section 6).

### EC3: mid-year start
Situation: self-employment started in July 2026. Resolution: the pages state an ANNUAL income test and do not mention pro-rating. Apply the test to the income for the year as the page words it, and flag the point to the accountant.

### EC4: proprietary director paid salary only
Situation: director owns or controls the Class S shareholding in the family employment table or more. Resolution: Class S, not Class A, collected under PAYE by the company at the period rate for each week. Below that share, DSP decides case by case: refer.

### EC5: client turning 66 in 2026
Situation: client reaches 66 during 2026. Resolution: if born on or after 1 January 1958 and not awarded the State Pension (Contributory), Class S continues to age 70. If they are awarded the State Pension (Contributory), refer for the treatment of the rest of the year; the pages read do not set out a part-year rule for Class S.

### EC6: rental income only
Situation: client has rental income and no trade or employment. Resolution: people whose only income is rents pay Class S, subject to the annual test. If the client is ALSO an employee and the rent is the only other income, it is Class K, not Class S.

### EC7: which rate for which year
Situation: client asks which rate applies. Resolution: 2025 Form 11 uses the 2025 blended rate; 2026 Form 11 uses the 2026 blended rate. Do not apply the period rates separately on an annual return.

## Ask the client first

- Which year's income are we working on, 2025 or 2026, and is PRSI paid through Form 11 or deducted under PAYE as a company director?
- What is your date of birth, and have you been awarded the State Pension (Contributory)?
- Are you also an employee? If so, is your other income from a trade or profession (Class S), or only rent, dividends or other unearned income (likely Class K)?
- If you are a company director, what share of the company do you own or control, directly or through another company?
- What is your gross self-employed and other income for the year, and what capital allowances do you claim?
- Are you a public servant paying a modified PRSI class, or a share fisherman or fisherwoman?
- Has the full income tax and PRSI bill for the year been paid, or only part of it?

## When to refuse or refer

- **Cross-border.** The client works or lives in another EU or EEA state, or in a country with a social security agreement with Ireland. Which state collects social insurance is outside this Guide: refer.
- **Director below the Class S shareholding.** Classification is case by case: refer to DSP Scope Section or the accountant.
- **Class K cases.** Employees whose only other income is unearned, occupational pensioners under pension age with only unearned other income, modified-rate public servants, public office holders: refer.
- **Aged 66 to 70 with a pension award during the year**, or any doubt about State Pension (Contributory) status: refer.
- **Told by Revenue no return is needed** but income is at or above the threshold: a flat-rate contribution is paid direct to DSP (amount in the Operational Guidelines table, Section 5). Confirm with DSP: refer.
- **Class P** for share fishermen and fisherwomen: refer.
- **Tax year not known:** stop. Do not compute PRSI.

### Reviewer escalation templates

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

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
~~~

## Sources

- DSP, PRSI Class S Rates: https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/
- DSP, SW14 PRSI Contribution Rates and User Guide, January 2026: https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf
- DSP, A Guide to PRSI for the Self-Employed, January 2025: https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf
- DSP, PRSI and Family Employment: https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/
- DSP, Operational Guidelines: PRSI for the Self-Employed (last updated 6 January 2026): https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/
- Revenue, Do you need to pay PRSI?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx
- Revenue, Who should register for Income Tax self-assessment?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx
- Revenue, What is preliminary tax?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx
- Revenue, Pay and file system: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx
- Revenue, eBrief No. 034/26: https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants website. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
