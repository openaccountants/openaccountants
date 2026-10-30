---
name: ie-prsi-class-s
description: "Irish PRSI Class S for the self-employed, tax year 2026, under the Social Welfare Consolidation Act 2005 as revised to 1 October 2026. Covers who pays (sole traders, partners, proprietary directors with 50% or more, people living on rent or investment income, councillors), the 4.2% rate to 30 September 2026 and 4.35% from 1 October 2026, the blended 4.2375% rate for 2026 self-assessed income and 4.125% for 2025 income, the EUR 5,000 income floor, the EUR 650 minimum, the EUR 310 no-return flat rate, payment through Form 11 and preliminary tax, directors under PAYE, the benefits Class S covers, voluntary contributions, and the late filing surcharge and 0.0219% daily interest. Trigger on 'Class S', 'PRSI self-employed', 'PRSI on rental income', 'director PRSI', 'how much PRSI do I pay'. Out of scope: employee PRSI (ie-payroll), USC (ie-usc), Class K and cross-border cases (ie-prsi-cross-border), income tax on the Form 11 (ie-income-tax-form11)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ie-prsi-class-s"
  jurisdiction: "IE"
  tax_year: "2026"
  last_updated: "2026-10-24"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Ireland PRSI Class S for the self-employed

Pay Related Social Insurance (PRSI) at Class S is the social insurance contribution of self-employed people in Ireland. The Department of Social Protection (DSP) owns the contribution; Revenue collects it with income tax and USC through self-assessment, or through payroll for proprietary directors. The contribution year is the calendar year. Section numbers are the Social Welfare Consolidation Act 2005 (SWCA) unless another act is named. The Law Reform Commission revised text read for this skill is updated to 1 October 2026 and already prints the 4.35% rate.

See also: `ie-payroll` (employee and employer PRSI, Class A), `ie-usc` (Universal Social Charge), `ie-prsi-cross-border` (Class K, A1 certificates, EU and bilateral rules), `ie-income-tax-form11` (the Form 11 return), `ie-preliminary-tax` (preliminary tax rules in depth).

## Who this applies to

- **Self-employed contributors.** Every person aged over 16 and under pensionable age (66) who has reckonable income or reckonable emoluments is a self-employed contributor, whether or not they are also an employee (s.20(1)(a)(i)). A person born on or after 1 January 1958 who has reached 66 but is under 70 and has not been awarded the State Pension (Contributory) stays in Class S (s.20(1)(a)(ii)). Revenue: the change applied from 1 January 2024 and does not reach someone already getting the State Pension (Contributory) or born before 1 January 1958 ([Revenue, do you need to pay PRSI](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)).
- **Who that covers in practice.** Sole traders, farmers, professionals, contractors and sub-contractors, partners; people whose only income is investments, rents or maintenance payments; employees who are also self-employed (Class S on top of their employee class); councillors on their local authority pay ([DSP SW74 leaflet](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)). A spouse or civil partner who takes part in the business is a Class S payer ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/); Sch. 1 Pt. 3 para. 1(ii)).
- **Proprietary directors.** From 1 July 2013 a director who owns or controls 50% or more of the shares, directly or indirectly (for example through a holding company), is self-employed and pays Class S. Below 50%, DSP decides case by case under the Code of Practice on determining employment status ([DSP, PRSI and family employment](https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/)). A Class S director pays through PAYE (s.21(1)(c), s.23(3)); if the directorship is the only self-employed income, the director does not register as self-employed ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); [SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)). The director must check that the right PRSI was deducted and paid over ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)).
- **Excepted, so no Class S** (Sch. 1 Pt. 3):
  - a prescribed relative who helps in the business but is not a partner, spouse or civil partner (para. 1). DSP lists son, daughter, parent, brother or sister; confirm doubtful cases with DSP Scope Section ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf));
  - a person on pre-retirement allowance (para. 2);
  - a person whose total reckonable income, emoluments and earnings, before capital allowances, is below EUR 5,000 (para. 3; S.I. 312 of 1996 art. 92);
  - an employee or occupational pensioner whose other income has no reckonable emoluments and no trade, profession or partnership income (para. 4). That income may be Class K: see `ie-prsi-cross-border`;
  - a person in the employments in arts. 81 to 84 of S.I. 312 of 1996 (para. 5). Modified-rate public servants (Classes B, C, D) with self-employed income pay Class K on it instead ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf));
  - a person not resident or not ordinarily resident whose income has no trade, profession or partnership income (para. 6). DSP applies this to non-resident directors and non-residents with only unearned income ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
- **Share fishers** classed as self-employed may add an optional Class P contribution on top of Class S. This skill does not compute Class P ([DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Class S rate on reckonable income or emoluments, 1 January to 30 September 2026 | 4.2% | 2026 | SWCA s.21(1)(a), (c); SW (Misc. Provisions) Act 2024 s.3(2), Table items 9-10, col. 5: https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf |
| Class S rate from 1 October 2026 | 4.35% | 2026 | SWCA s.21(1)(a), (c) as revised: https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html ; 2024 Act s.3(3), col. 6 |
| Class S rate, 1 January to 30 September 2025 / from 1 October 2025 | 4.1% / 4.2% | 2025 | 2024 Act s.3(1), (2), cols. 4-5: https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf |
| Enacted future steps: from 1 October 2027 / from 1 October 2028 | 4.5% / 4.7% | 2027-2028 | 2024 Act s.3(4), (5), cols. 7-8: https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf |
| Blended rate for 2026 self-assessed income: ((4.2 x 9) + (4.35 x 3)) / 12 | 4.2375% | 2026 | SWCA s.38BA (2024 Act s.9); DSP: https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| Blended rate for 2025 self-assessed income: ((4.1 x 9) + (4.2 x 3)) / 12 | 4.125% | 2025 | SWCA s.38BA; DSP: https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ ; Revenue TDM 38-01-04J para. 10.2: https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-38/38-01-04J.pdf |
| Minimum annual contribution (reckonable income, emoluments, or both together) | EUR 650 | 2026 | SWCA s.21(1)(a), (c), (f); 2024 Act s.5: https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html |
| Income floor: below this, no Class S (total before capital allowances) | under EUR 5,000 | 2026 | SWCA Sch. 1 Pt. 3 para. 3; S.I. 312 of 1996 art. 92 as amended by S.I. 684 of 2010 art. 6: https://www.irishstatutebook.ie/eli/2010/si/684/made/en/print |
| Flat contribution where Revenue says no return is needed | EUR 310 | 2026 | SWCA s.21(1)(b): https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html |
| Contribution linked to childcare services relief (TCA s.216C) | EUR 650 | 2026 | SWCA s.21(1)(ea): https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html |
| Voluntary contribution, last paid at Class S | EUR 650 a year | 2026 | SWCA s.26(1) (2024 Act s.6); SW14: https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Payroll subclasses for Class S directors: S0 weekly pay up to EUR 500, S1 over EUR 500 | same rate for both: 4.2%, then 4.35% from 1 Oct 2026 | 2026 | DSP: https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| Proprietary director shareholding for Class S | 50% or more | 2026 | DSP: https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/ |
| Upper earnings limit | none (the rate applies to all reckonable income) | 2026 | SWCA s.21(1)(a): https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html |
| Preliminary tax: lowest of 90% of current year, 100% of previous year, 105% of pre-preceding year (direct debit only) | 90% / 100% / 105% | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Late filing surcharge: within two months / after two months | 5% capped at EUR 12,695 / 10% capped at EUR 63,485 | 2026 | TCA s.1084; https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |
| Interest on late income tax, which includes Class S (s.23(4)) | 0.0219% a day | 2026 | TCA s.1080; https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |

**Why there is a blended rate.** When a Class S rate changes during a contribution year, s.38BA sets one rate for the year: (A x C + B x D) / 12, where A and B are the two rates and C and D the months (including part months) each applied. The rate rose on 1 October in both 2025 and 2026, so C is 9 and D is 3. The DSP page prints the results: 4.125% for 2025 income and 4.2375% for 2026 income. Revenue applies the same method on the return: its manual for the 2025 ROS Form 11 sets "PRSI rate of 4.125% on all classes, Form 11" (TDM 38-01-04J para. 10.2), and the 2024 manual set the 2024 blend of 4.025% (TDM 38-01-04I). Revenue's public page "Do you need to pay PRSI?" prints only the two period rates; on a Form 11 use the blended rate.

**Directors under PAYE use the period rate.** Section 38BA does not apply to emoluments taxed under PAYE (TCA Part 42 Chapter 4; s.38BA(2)). A Class S director's payroll deducts 4.2% on pay to 30 September 2026 and 4.35% after.

## The taxable base

- **Reckonable income** is the aggregate income from all sources for the contribution year, as estimated under the Income Tax Acts, after capital allowances. It leaves out reckonable earnings and reckonable emoluments, which carry their own charge (s.2(1)). Revenue: "Your PRSI is calculated on your gross income once any capital allowances have been deducted" ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)).
- **Income that is exempt from income tax still counts.** Reckonable income is computed without regard to TCA ss.140, 195, 216C, 216F, 231, 232 and 233 (s.2(1)). Income exempt under, for example, the artists' exemption (s.195) is still subject to Class S.
- **No joint assessment.** The TCA Part 44 Chapter 1 joint assessment rules are disregarded (s.2(1)), so each spouse or civil partner's Class S is worked out on their own income. Where joint assessment applies for income tax, the contributions are collected from the assessable spouse or nominated civil partner, but the amount owed by each is unchanged (s.23(5), (5A)).
- **What DSP lists as included:** benefit in kind; trade or profession income; interest, annuities and foreign investment income; Irish rent; income taxed at source such as bank interest and maintenance payments; share dividends and ARF dividends; certain taxable employment income such as a director's ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)). Revenue adds rental income and legally enforceable maintenance payments ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)).
- **What DSP lists as excluded:** capital allowances; social welfare payments; SOLAS training payments and HSE Mobility Allowance taxed under PAYE; pensions taxed under PAYE; income continuance payments taxed under PAYE; redundancy and termination payments taxed under PAYE; early AVC withdrawals taxed under PAYE; retirement lump sums above the EUR 200,000 lifetime tax-free limit; certain early encashments of private pensions by public servants who were once self-employed; gains on certain foreign life policies and offshore funds; certain chargeable excesses on a Benefit Crystallisation Event ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).
- **The floor is a cliff, not an allowance.** Below EUR 5,000 of total income (before capital allowances) there is no Class S. At EUR 5,000 or more, Class S is due on all reckonable income, with the EUR 650 minimum. At exactly EUR 5,000 the minimum applies.
- **The minimum.** The charge is the greater of the rate times income and EUR 650 (s.21(1)(a)). A director who has both reckonable income and reckonable emoluments pays only one EUR 650 minimum, not two (s.21(1)(f)).
- **Tax credits do not reduce Class S.** Class S on reckonable income is charged as if it were income tax, but the Income Tax Acts' provisions granting an allowance, deduction or relief do not apply to it (s.23(4)).
- **No pro-rating.** The floor and the minimum are annual. The law read has no rule to reduce them for a person who starts or stops mid-year.
- **Benefits it buys.** Class S counts for these schemes only: State Pension (Contributory), Bereaved Partner's (Contributory) Pension, Guardian's Payment (Contributory), Invalidity Pension, Maternity, Adoptive, Paternity and Parent's Benefit, Carer's Benefit, Treatment Benefit, Jobseeker's Benefit (Self-Employed) and bereavement grant (s.21(1)(e)). DSP's list adds Benefit Payment for 65 Year Olds and Partial Capacity Benefit ([DSP Class S rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/)).
- **Full payment or nothing.** A full year of contributions (one for each week) is credited only when the full amount due is paid. A part payment earns no contributions for that year (s.21(1)(d); [DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)). This matters most for the State Pension.
- **Voluntary contributions.** A person who leaves compulsory insurance (for example income falls under EUR 5,000) and is under 66, or 66 to 70 without a State Pension (Contributory) award, may pay voluntary contributions: EUR 650 a year for someone last at Class S. Apply within 60 months from the end of the contribution year in which a contribution was last paid or credited ([SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)). They keep cover only for the pensions the person had when last paying compulsory PRSI ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).

## Deadlines and filing

- **Registration.** Self-employed people register with Revenue for income tax and PRSI (eRegistration or Form TR1). Anyone whose taxable non-PAYE income exceeds EUR 5,000, or gross non-PAYE income exceeds EUR 30,000, must register for self-assessment ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). This is a separate test from the Class S floor (EUR 5,000 or over, before capital allowances).
- **One sum with income tax.** Class S on reckonable income is assessed, charged and paid as if it were income tax, in one aggregated sum with the income tax for the same year (s.23(4)). It goes on the Form 11 and is paid with income tax and USC.
- **Preliminary tax.** Preliminary tax is the estimate of income tax, PRSI and USC for the year, due by 31 October of that year. It must be at least the lowest of 90% of this year's tax, 100% of last year's, or 105% of the year before last (direct debit only; not if that year's tax was nil). In the first year of self-assessment, the 100% option is normally nil ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- **Return and balance.** By 31 October 2026: pay 2026 preliminary tax, file the 2025 Form 11 and pay the 2025 balance. If the person both pays and files through ROS, the date is Wednesday 18 November 2026; if only one is done through ROS, it stays 31 October ([Revenue pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx); [eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)). The 2026 Form 11 (Class S at 4.2375%) is due by 31 October 2027.
- **Which rate on which return.** The 2025 Form 11 filed in 2026 uses 4.125%. The 2026 Form 11 and the current-year option for 2026 preliminary tax use 4.2375%. Never apply the two period rates separately on an annual return.
- **Directors under PAYE.** The company deducts Class S on each payment and reports it on the payroll submission on or before pay day; see `ie-payroll` for submission and payment dates.
- **No-return cases.** A person with income of EUR 5,000 or more whom Revenue has excused from making returns pays EUR 310 for the year direct to DSP (s.21(1)(b); [DSP Operational Guidelines](https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/)).

## Penalties and interest

Because Class S is charged as part of the income tax sum, the Income Tax Acts' collection, surcharge and interest rules apply to it (s.23(4)).

| Event | Consequence | Source |
|---|---|---|
| Form 11 filed within two months after the due date | Surcharge of 5% of the tax due, capped at EUR 12,695 | TCA s.1084; [Revenue pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |
| Form 11 filed more than two months late | Surcharge of 10%, capped at EUR 63,485 | same |
| LPT obligations not met | 10% surcharge on the final liability, even if income tax is paid and filed on time | same |
| Late payment | Interest of 0.0219% for each day or part of a day | TCA s.1080; [Revenue interest guidelines](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf) |
| Preliminary tax below the lowest of the three tests | Interest charged | [Revenue preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx) |
| Class S not paid in full | No contributions credited for the year until the full amount is paid | s.21(1)(d) |
| Director's Class S under-deducted by the company | Collected as PAYE the employer should have remitted; payroll interest and penalties apply (see `ie-payroll`) | s.23(3) |

## Cross-border points

- **Non-residents.** A person not resident or not ordinarily resident whose income has no trade, profession or partnership income is excepted (Sch. 1 Pt. 3 para. 6). A non-resident with an Irish trade is not excepted by that paragraph; the EU and bilateral rules below still decide which country insures them.
- **Which country insures.** For work in more than one EU or EEA state, the UK or Switzerland, or a country with a bilateral agreement, which country's social insurance applies follows EU Regulation 883/2004, the A1 certificate or the agreement. Use `ie-prsi-cross-border`; do not apply Class S until that question is settled.
- **Foreign income.** Foreign investment income, including foreign property income, is part of the Class S base for a person who is in Class S ([SW74](https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf)).

## Worked examples

### Example 1: sole trader, 2026 income, Form 11

Aoife, aged 45, is a sole trader. Her 2026 trading profit is EUR 84,000, she claims EUR 6,000 of capital allowances, and she has EUR 2,000 of Irish rental profit (rent less allowable expenses, as computed for income tax). Reckonable income is 84,000 - 6,000 + 2,000 = EUR 80,000. That is above the EUR 5,000 floor. For 2026 income on a Form 11 the rate is the blended rate: ((4.2 x 9) + (4.35 x 3)) / 12 = 4.2375%. Class S is 80,000 x 4.2375% = EUR 3,390.00, which is above the EUR 650 minimum. It is paid with her income tax and USC: preliminary tax by 31 October 2026, and the 2026 balance with the 2026 Form 11 by 31 October 2027.

```oa-check
name: Sole trader, 2026 reckonable income EUR 80,000, blended rate
inputs:
  trading_profit: 84000
  capital_allowances: 6000
  irish_rental_profit: 2000
steps:
  - reckonable: trading_profit - capital_allowances + irish_rental_profit
  - rate_2026: (4.2 * 9 + 4.35 * 3) / 12
  - by_rate: reckonable * rate_2026 / 100
  - class_s: max(by_rate, 650)
expected:
  reckonable: 80000
  rate_2026: 4.2375
  class_s: 3390.00
```

### Example 2: first-year trader on the minimum, 2025 return filed late

Ciarán started trading in 2025. His 2025 reckonable income is EUR 14,000. This is his first self-assessment year, so no 2025 preliminary tax was due (100% of a nil prior year). The 2025 rate is the blended 4.125%: 14,000 x 4.125% = EUR 577.50, below the minimum, so Class S is EUR 650. He files the 2025 Form 11 on paper and pays on 30 November 2026, 30 days after 31 October (the ROS date of 18 November does not apply). The return is within two months of the due date, so the surcharge is 5%. On the Class S part alone: surcharge 650 x 5% = EUR 32.50, and interest 650 x 0.0219% x 30 = EUR 4.27. The same surcharge and interest also apply to any income tax and USC in the same return. Once the full EUR 650 is paid, his 2025 contributions are credited.

```oa-check
name: First-year trader, 2025 income EUR 14,000, minimum applies, filed and paid 30 days late
inputs:
  reckonable: 14000
  days_late: 30
steps:
  - rate_2025: (4.1 * 9 + 4.2 * 3) / 12
  - by_rate: reckonable * rate_2025 / 100
  - class_s: max(by_rate, 650)
  - surcharge: class_s * 5 / 100
  - interest: round(class_s * 0.0219 / 100 * days_late, 2)
expected:
  rate_2025: 4.125
  by_rate: 577.50
  class_s: 650.00
  surcharge: 32.50
  interest: 4.27
```

## Ask the client first

1. Which year's income are we working on (2025 return or 2026), and is PRSI paid through Form 11 or deducted through payroll as a director?
2. Your date of birth, and have you been awarded the State Pension (Contributory)?
3. If you are a director: what share of the company do you own or control, directly or through another company?
4. Are you also an employee or a modified-rate public servant, and is your other income from a trade or profession, or only rent, dividends or other unearned income?
5. Total income for the year before capital allowances, and the capital allowances claimed.
6. Are you resident in Ireland, and do you work in any other country?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Welfare Consolidation Act 2005, revised to 1 October 2026: s.2(1) reckonable income, s.20, s.21, s.23, s.26, s.38BA, Sch. 1 Pt. 3 | https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html | 2026-10-24 |
| Social Welfare (Miscellaneous Provisions) Act 2024 (No. 24 of 2024), s.3 and Table, s.5, s.6, s.9 (new s.38BA) | https://www.irishstatutebook.ie/pdf/2024/en.act.2024.0024.pdf | 2026-10-24 |
| Social Welfare and Automatic Enrolment Retirement Savings System (Amendment) Act 2025 (No. 19 of 2025), the Budget 2026 social welfare act: no change to Class S | https://www.irishstatutebook.ie/eli/2025/act/19/enacted/en/html | 2026-10-24 |
| S.I. No. 684 of 2010, art. 6 (EUR 5,000 floor in art. 92 of S.I. 312 of 1996) | https://www.irishstatutebook.ie/eli/2010/si/684/made/en/print | 2026-10-24 |
| DSP, PRSI Class S rates (updated 20 January 2026) | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ | 2026-10-24 |
| DSP, SW14 PRSI Contribution Rates and User Guide, January 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf | 2026-10-24 |
| DSP, SW74 A Guide to PRSI for the Self-Employed, January 2025 (used for who pays and what counts, not for rates) | https://assets.gov.ie/38671/0aa2cf3d831a4076b1b6208e1287d9f9.pdf | 2026-10-24 |
| DSP, Operational Guidelines: PRSI for the Self-Employed (updated 6 January 2026) | https://www.gov.ie/en/department-of-social-protection/publications/operational-guidelines-prsi-for-the-self-employed/ | 2026-10-24 |
| DSP, PRSI and family employment (updated 15 April 2025) | https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/ | 2026-10-24 |
| Revenue, do you need to pay PRSI? | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx | 2026-10-24 |
| Revenue, who should register for income tax self-assessment? | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx | 2026-10-24 |
| Revenue, what is preliminary tax? | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-10-24 |
| Revenue, pay and file (deadlines, late filing surcharge) | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-10-24 |
| Revenue, eBrief No. 034/26 (ROS extension to 18 November 2026) | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-24 |
| Revenue, TDM 38-01-04J, Income tax return form 2025, ROS Form 11, para. 10.2 (Form 11 PRSI rate 4.125% for 2025) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-38/38-01-04J.pdf | 2026-10-24 |
| Revenue, Guidelines for charging interest on late payment (updated May 2025) | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-24 |

Not yet confirmed: (1) whether Class S is deductible in computing taxable income for income tax (no source read says so either way); (2) whether pension contribution relief reduces reckonable income; (3) how the EUR 650 minimum is collected for a director whose only Class S is through PAYE and whose pay gives less than EUR 650; (4) the part-year treatment for someone awarded the State Pension (Contributory) between 66 and 70 during the year; (5) how a mid-year start or finish is treated beyond the annual floor and minimum (the law read has no pro-rating rule); (6) the full list of "prescribed relatives" in art. 94 of S.I. 312 of 1996 (taken from the DSP leaflet, not the regulation); (7) whether interest also runs on the late filing surcharge; (8) the text of arts. 81 to 84 of S.I. 312 of 1996 (para. 5 exceptions), not read; (9) the Social Welfare Bill for Budget 2027 was not enacted on 24 October 2026 and was not read.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ie-prsi-class-s` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ie-prsi-class-s. If neither is available, confirm every figure against the official source pages cited above before relying on it.
