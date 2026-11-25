---
name: nz-acc-levies
description: "Use this skill whenever asked about New Zealand ACC levies for self-employed individuals. Trigger on phrases like \"ACC levy\", \"earner levy\", \"work levy\", \"CoverPlus\", \"CoverPlus Extra\", \"accident compensation\", \"ACC invoice\", \"classification unit\", or any question about ACC obligations for sole traders in New Zealand. Covers earner levy, work levy by classification unit (CU), CoverPlus/CoverPlus Extra, maximum liable earnings, and payment schedules. ALWAYS read this skill before touching any NZ ACC work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nz-acc-levies"
  jurisdiction: "NZ"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# ACC levies in New Zealand: employees, the self-employed and employers

How Accident Compensation Corporation (ACC) levies work in New Zealand: the Earners' levy deducted through PAYE, the Earners' levy and Work levy that ACC invoices to the self-employed, the Work levy employers pay for their staff, the Working Safer levy, classification by business industry classification (BIC) code, CoverPlus and CoverPlus Extra, and the invoice cycle.

Figures are for the levy year 1 April 2026 to 31 March 2027 (tax year 2026-27; Inland Revenue calls it the tax year ending 31 March 2027). Each rate below names its own levy year. A short section covers the 2025-26 returns being filed now.

Inland Revenue (IRD) publishes the PAYE rates, which include GST. ACC applies the statutory levy rates before GST to invoiced earnings. Use the regulations and the ACC invoice for the client's classification unit and any adjustments.

Companion Skills: income tax on the business itself is in `nz-income-tax-ir3` (and `nz-provisional-tax`); GST registration and input tax are in `nz-gst-return`.

## Scope

In scope:

- Employees: the Earners' levy that the employer deducts as part of PAYE ([IR335 Employer's guide](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf), page 18).
- The self-employed: sole traders, contractors paid schedular payments, partners with active partnership income, and owners who play an active part in a look-through company (LTC). ACC invoices them directly for their levies ([IR3G 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf), PDF pages 15, 26, 35 and 60; [IRD, ACC levies for a look-through company](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company)).
- Employers, including close companies that pay shareholder-employees without PAYE.
- Private domestic workers and other IR56 taxpayers who deduct their own PAYE.

Out of scope: ACC claims, weekly compensation, rehabilitation, levy disputes and reviews. See "When to refuse or refer".

### The three levies at a glance

| Levy | What it covers | Who pays | Where the rate comes from |
| --- | --- | --- | --- |
| Earners' levy | Injuries outside work (IR335 page 18: "to cover the cost of non-work-related injuries") | Employees through PAYE; the self-employed on their ACC invoice; close companies on shareholder-employee pay with no PAYE | IRD rates page (below) (https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates) |
| Work levy | Injuries at work | Employers, for their employees, and self-employed people | Use the rate for the applicable classification unit in [Work Account Levies Regulations 2025, Schedule 2](https://www.legislation.govt.nz/regulation/public/2025/0017/12.0/contents.html) and check the ACC invoice |
| Working Safer levy | Funds WorkSafe New Zealand | Businesses and the self-employed | Flat rate of 8 cents per NZD 100 before GST ([Rates of Funding Levy regulations](https://www.legislation.govt.nz/regulation/public/2016/0020/8.0/DLM6725448.html)). Check the earnings or compensation base on the invoice |

Source for the self-employed list: IRD, "I am coming to work or study in New Zealand": "In addition to the Earners' levy that people getting salary or wages pay, you'll also pay the: Work levy Working Safer levy" ([IRD](https://www.ird.govt.nz/situations/work-or-study-in-new-zealand)).

## Ask the client first

- Are you an employee, a sole trader, a contractor paid schedular payments, a partner, an LTC owner (active or passive), a shareholder-employee, an employer, or a mix of these?
- Which levy year is the question about? A self-employed person's ACC invoice is based on the income tax return, so it usually relates to an earlier year than the one the invoice arrives in.
- Can you send your latest ACC invoice? It shows your classification unit, the Work levy and Working Safer levy rates, and any discount or loading. Without it no Work levy figure can be given.
- What were the liable earnings in the most recent income tax return (IR3), and is the BIC code on that return right for your main activity?
- Are you on CoverPlus (the default) or CoverPlus Extra, and at what agreed level of cover? (**check** with ACC)
- For employees: pay frequency, and whether any payment is a lump sum, redundancy, retiring payment or employee share scheme benefit.
- Do you have more than one source of liable income, or shareholder-employee pay from two or more companies?
- Are you GST-registered?

## The method, step by step

1. **Place the person.** Employee only: the Earners' levy is already inside PAYE and the employer pays the Work levy; there is no ACC invoice to the employee (IR335 page 18: "PAYE includes ACC earners' levy already, so no extra calculations are needed"). Self-employed, contractor on schedular payments, partner with active income, or active LTC owner: ACC invoices the person directly. Passive LTC investor: no ACC levies on that LTC income ([IRD LTC page](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company)).
2. **Pick the levy year and its row.** Use the row of the IRD table for the year the earnings relate to. Do not use the 2027-28 row for 2026-27, and do not use last year's row for this year ([IRD rates page](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates)).
3. **Find liable earnings.** For the self-employed, ACC takes income from the IR3: question 11A (gross earnings with PAYE deducted and earnings not liable for the earners' levy), 12 (schedular payments), 17 (foreign employment and foreign services income only), 18 (active partnership income), 19 (LTC active income), 20 (shareholder-employee salary with no tax deducted), 24 (self-employed income), 27 (other income) and 29 (other expenses) ([IR3G 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf), PDF page 60). IRD passes this to ACC under an information-sharing agreement that "Enables ACC to assess levies" ([IRD, information sharing with ACC](https://www.ird.govt.nz/about-us/information-sharing/mous/acc)).
4. **Apply the maximum and minimum.** Use the annual maximum and apply any PAYE exceptions below. The ordinary self-employed minimum applies if the person averaged more than 30 hours per week across their work, including employee hours. Use actual liable income at 30 hours or less. Regulation 6(4) reduces the self-employed Earners' levy minimum base by earnings as an employee. Check the separate calculation for purchased weekly compensation.
5. **Calculate the Earners' levy.** Use the published GST-inclusive rate for PAYE. When estimating the 2026-27 ACC invoice for standard CoverPlus, multiply the taxable base by the statutory 1.52% rate before GST and apply GST at 15%. Check combined income adjustments and the actual invoice.
6. **Identify Work and Working Safer levies.** For Work levy use the applicable classification unit and any Experience Rating adjustment. ACC discontinued the No Claims Discount from 1 April 2026. The separate Working Safer levy has a flat rate. An incorrect BIC code can affect the Work levy (IR3G 2026, PDF page 8).
7. **Label the total an estimate** until the ACC invoice arrives, and state which levy year each figure belongs to.
8. **For an employer's payroll**, confirm the earners' levy is deducted only from the payments IR335 lists, only up to the per-pay maximum, and that lump sums follow the lump-sum rule (see the boundary table).
9. **Record the deduction.** ACC levies paid for self-employment and as an employer, and any interest charged, go in the business expenses (Box 9 of the IR3B) ([IR3B July 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3b/ir3b-2026.pdf)).

## Figures, with their levy years

### Earners' levy rate and maximum ([IRD, ACC earners' levy rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates))

The table gives Inland Revenue's GST-inclusive PAYE rates and corresponding maximum amounts. Schedule the employer's withholding using the per-pay rules below. For self-employed invoices, calculate the levy at the statutory GST-exclusive rate before adding GST.

| Levy year | Rate (includes GST) | Maximum liable earnings | Maximum levy payable | Use | Source |
| --- | --- | --- | --- | --- | --- |
| 1 April 2026 to 31 March 2027 | $1.75 per $100 (1.75%) | $156,641 | $2,741.22 | **This skill's year** | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| 1 April 2025 to 31 March 2026 | $1.67 per $100 (1.67%) | $152,790 | $2,551.59 | Returns being filed now for 2025-26 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| 1 April 2027 to 31 March 2028 | $1.83 per $100 (1.83%) | $160,244 | $2,932.47 | Next year only. Never for 2026-27 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |

The ordinary statutory rates before GST are NZD 1.45, NZD 1.52 and NZD 1.59 per NZD 100 for 2025-26, 2026-27 and 2027-28 respectively. Check regulation 7 for purchased weekly compensation. [Earners' Levy Regulations 2025, regulations 4–8](https://www.legislation.govt.nz/regulation/public/2025/0018/latest/LMS1019194.html)

### Maximum and minimum for the self-employed, 2026-27 ([IRD Payroll calculations and business rules specification, 1 April 2026 to 31 March 2027](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf))

| What | 2026-27 | Source wording |
| --- | --- | --- |
| Maximum liable earnings, employees and private domestic workers (Work and Earners' Accounts) | $156,641 | Row "Employees and private domestic workers ... (Work and Earners' Accounts)": 2025/26 $152,790, 2026/27 $156,641 (https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf) |
| Maximum liable earnings, self-employed people (Work and Earners' Accounts) | $156,641 | same table (https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf) |
| Minimum liable earnings on which self-employed people pay the Work and Earners' levies | $50,501 | "To increase the minimum liable earnings that self-employed people pay Work and Earners' levies on to $50,501 in 2026/27" (https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf) |

For standard cover the 2026-27 minimum applies when average weekly work across all jobs exceeds 30 hours. When the person worked 30 hours or less on average, ACC uses actual liable income. For 2025-26 the equivalent full-time minimum is NZD 49,365. [Earners' Levy Regulations 2025, regulation 6](https://www.legislation.govt.nz/regulation/public/2025/0018/latest/LMS1019199.html) · [Work Account Levies Regulations 2025, regulation 7](https://www.legislation.govt.nz/regulation/public/2025/0017/latest/LMS1019593.html)

### Earners' levy through PAYE, 2026-27 ([IR335 Employer's guide, September 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf))

| What | Tax year ending 31 March 2027 | Source |
| --- | --- | --- |
| Earners' levy rate, already inside PAYE | 1.75% | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Maximum earnings per weekly pay | $3,012 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Maximum earnings per fortnightly pay | $6,024 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Maximum earnings per 4-weekly pay | $12,048 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Maximum earnings per monthly pay | $13,053 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Non-notified rate (ND tax code), includes the earners' levy | 46.75% | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |

IR335 page 18: the maximum does not apply to PAYE on regular secondary income, casual agricultural employee payments, election day workers' earnings, or earnings where the non-notified rate is used.

### Work levy and Working Safer levy

The 2026-27 Work Account levy rates are in Schedule 2 of the Work Account Levies Regulations. Select the client's classification unit and check invoice adjustments. The Working Safer rate is 8 cents per NZD 100 before GST. [Work Account Levies Regulations 2025, Schedule 2](https://www.legislation.govt.nz/regulation/public/2025/0017/12.0/contents.html) · [Rates of Funding Levy regulations](https://www.legislation.govt.nz/regulation/public/2016/0020/8.0/DLM6725448.html)

## Boundaries and exceptions

### Which payments carry the Earners' levy through PAYE ([IR335 page 18](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf))

| Deduct the earners' levy from | Do not deduct the earners' levy from | Source |
| --- | --- | --- |
| Salary and wages | Schedular payments | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Overtime pay | Retirement payments | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Backpay and holiday pay | Redundancy payments | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Long-service leave pay | Employee share scheme benefits | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Bonuses or gratuities | Jury fees | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Taxable allowances | Witness fees | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Shareholder-employee salaries with PAYE deductions | Taxable and non-taxable pensions | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Salaries to partners in a partnership | Tax-free allowances | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Salaries to working owners of a look-through company | Shareholder-employee salaries with no PAYE deductions (ACC invoices the company instead) | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |

Read the two columns separately. The PDF's flattened text runs them together, which is how an earlier version of this skill came to say that LTC working owners' salaries are excluded. They are in the "deduct" column.

Lump sums (IR335, pages 39–42): exclude the levy for genuine redundancy or retirement payments and employee share scheme benefits. For main employment follow the annualised income plus extra pay test against NZD 156,641. For secondary employment, include the low threshold for the employee's tax code. IR335 provides a split calculation when annualised income plus that low threshold is below NZD 156,642 and the total including the lump sum exceeds NZD 156,641. Include the levy on the portion of the lump sum up to the ceiling and exclude it on the remainder. A purported redundancy or retiring payment requires the employment to end.

### Who pays what, by situation ([IR3G 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf))

| Situation | Treatment | Source |
| --- | --- | --- |
| Employee only | Earners' levy inside PAYE. Employer pays the Work levy. No ACC invoice to the employee | IR335 page 18 |
| Contractor on schedular payments | No earners' levy deducted by the payer ("this is the worker's responsibility, not yours"). ACC invoices the contractor for levies on schedular payments | IR335 schedular payments section; IR3G PDF page 15 |
| Sole trader | "Income from self-employment is liable for ACC levies which ACC will invoice you for" | IR3G PDF page 35 |
| Partner | Active partnership income is liable and invoiced by ACC; salary paid to a working partner has the earners' levy deducted through PAYE only if it is paid under a binding written contract of service signed by all the partners, the contract states the amount payable, and the partner personally and actively performs the services | IR3G PDF page 26; IR335 pages 18 and 56 |
| LTC owner, passive investor | No ACC levies on LTC income, including LTC income received as beneficiary income through a trustee owner | IRD LTC page |
| LTC owner, active | Self-employed for ACC; ACC invoices the owner directly | IRD LTC page |
| LTC working owner paid salary or wages | Earners' levy deducted as part of PAYE. IR335 page 61 treats the payment as salary or wages only if the owner is employed under a written contract of employment. The LTC is invoiced by ACC for levies on salary or wages paid to employees | IRD LTC page; IR335 page 61 |
| Close company, shareholder-employee paid with no PAYE | ACC invoices the company for the earners' levy on that remuneration, based on the shareholder-employee remuneration declared in the company's IR4 | IR335 page 18; IR3G PDF page 29 |
| Employee and self-employed (mixed income) | "you have to pay ACC levies on both sources of income, up to the maximum. ACC will invoice you for the amount you'll have to pay" | IR3G PDF page 61 |
| Shareholder-employee pay from two or more companies | A refund from ACC may be due if the combined total is over the maximum ($152,790 for 2025-26 returns) | IR3G PDF page 61 |
| Private domestic worker or other IR56 taxpayer | Earners' levy is included in their own PAYE. ACC can invoice a private domestic worker for the Work levy. Other IR56 taxpayers, such as NZ-based employees of overseas employers, may be outside the Work levy | IR3G PDF page 61, ACC calculating your levies |
| Loss, or earnings below the minimum | Apply the minimum when the self-employed person averages more than 30 work hours per week across all jobs. Check the employee earnings offset and the separate rule for purchased compensation | Earners' Levy Regulations 2025 regulations 6–7, Work Account Levies Regulations 2025 regulation 7 |
| BIC code missing or wrong | ACC selects a code; the levy rate may be wrong. Fix the code in myIR or on the next return | IR3G PDF page 8; [IRD, updating a client's BIC code](https://www.ird.govt.nz/roles/tax-agents/updating-client-bic-code) |

### CoverPlus and CoverPlus Extra

Check the policy details against ACC's CoverPlus or CoverPlus Extra terms.

| Point | What to confirm with ACC |
| --- | --- |
| CoverPlus | The default cover for the self-employed; levies based on liable earnings from the tax return and the classification unit |
| CoverPlus Extra | An agreed level of cover chosen instead of CoverPlus; levies based on the agreed cover, not on actual earnings. Review the agreed level each year, because it can end up above or below actual earnings |
| Weekly compensation | How much ACC pays if the person cannot work, and on what income it is based |

### GST

- Inland Revenue's payroll rates include GST. The regulatory rates for the ACC invoice are GST-exclusive.
- A GST-registered business may claim qualifying GST on its ACC levies in its GST return. Check the taxable activity, use and taxable supply information. For the income-tax deduction, exclude the GST claimed. See `nz-gst-return` for input tax generally.

## Worked cases

The payroll cases use Inland Revenue's GST-inclusive PAYE rate of 1.75%. The standard self-employed invoice cases use the statutory 2026-27 rate of 1.52% before GST, the NZD 156,641 cap and the NZD 50,501 minimum where it applies. The invoice results are estimates of the Earners' levy component.

### Case 1: sole trader below the maximum ([IRD rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates))

A self-employed web designer has liable earnings of $90,000 for 2026-27, on CoverPlus.

- Earners' levy: $90,000 x 1.52% = $1,368.00 before GST, or $1,573.20 including GST.
- Check the Work levy by classification unit and the Working Safer levy separately on the ACC invoice.
- Timing: ACC invoices from the IR3, and IRD says "ACC will begin invoicing self-employed levies from September" (IR3G 2026, PDF page 60).

```oa-check
name: Earners' levy below the maximum
inputs:
  earnings: 90000
  rate: 0.0152
  gst: 0.15
  cap: 156641
steps:
  - levy: min(earnings, cap) * rate * (1 + gst)
expected:
  levy: 1573.20
```

### Case 2: high earner above the maximum ([IRD rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates))

A consultant has liable self-employed earnings of $200,000 for 2026-27.

- Liable earnings are capped at $156,641, for both the Earners' levy and the Work levy.
- Earners' levy invoice estimate: $156,641 x 1.52% x 1.15 = $2,738.08 including GST.

```oa-check
name: Earners' levy above the maximum
inputs:
  earnings: 200000
  rate: 0.0152
  gst: 0.15
  cap: 156641
steps:
  - levy: min(earnings, cap) * rate * (1 + gst)
expected:
  levy: 2738.08
```

### Case 3: self-employed with a loss ([IRD payroll specification](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf))

A sole trader working more than 30 hours per week on average records a loss for 2026-27. The sole trader has no earnings as an employee and has standard CoverPlus.

- IR3G: a loss or earnings below the minimum still attract ACC levies, "calculated at the minimum level".
- Earners' levy on the $50,501 minimum: $50,501 x 1.52% x 1.15 = $882.76 including GST.
- The minimum does not apply if the person averaged 30 hours or less across all work during the tax year.

### Case 4: employee paid weekly above the per-pay maximum ([IR335](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf))

An employee on a main tax code earns $3,500 in a weekly pay in 2026-27.

- The earners' levy is inside PAYE; it applies only up to $3,012 per weekly pay.
- Earners' levy portion of that week's PAYE: $3,012 x 1.75% = $52.71. The employee gets no ACC invoice; the employer pays the Work levy.

### Case 5: employee with a side business (mixed income) ([IR3G 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf))

A client earns $120,000 of salary with PAYE and $60,000 of self-employed income in 2026-27.

- Earners' levy already inside PAYE on the salary: $120,000 x 1.75% = $2,100.00.
- Use $156,641 − $120,000 = $36,641 as the remaining liable earnings under the combined cap, assuming ACC allocates the salary first.
- Invoiced Earners' levy component on that base: $36,641 x 1.52% x 1.15 = $640.48 including GST. The estimated PAYE and invoice components total $2,740.48. Check any Multiple Employer Adjustment and the separate Work levy assessment with ACC.

### Case 6: LTC working owner

An LTC owner works in the business, is paid a salary under a written employment contract, and also receives an LTC active income allocation.

- Salary: PAYE including the earners' levy is deducted (IR335 page 18 "deduct" column; IR335 page 61 for the written contract). ACC invoices the LTC for levies on salary or wages paid to employees.
- Active LTC income: the owner is self-employed for ACC and ACC invoices the owner directly ([IRD LTC page](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company)).
- A passive co-owner pays no ACC levies on LTC income.

## When to refuse or refer

- A request for a specific industry's Work levy or Working Safer levy rate without the client's ACC invoice: do not state a rate. Point to the invoice or ACC.
- ACC claims, weekly compensation, rehabilitation or personal service rehabilitation payments: outside this skill. Refer to ACC. (For how ACC personal service rehabilitation payments are taxed, see the IR3G.)
- A disputed levy, classification unit or invoice, or a request for reassessment: refer to ACC's Business Service Centre (phone 0800 222 776, as printed in IR3G 2026) and to a New Zealand chartered accountant.
- CoverPlus Extra: whether to take it and at what level of cover. ACC-only product; refer.
- Several entities or activities that may fall in different classification units: refer; the choice of BIC code for the main activity decides the rate.
- Refer complex GST apportionment, evidence or eligibility questions.
- Shareholder-employee refunds for pay from two or more companies over the maximum: ACC process; refer to ACC.
- Income tax on the business: see `nz-income-tax-ir3` and `nz-provisional-tax`. GST generally: see `nz-gst-return`.

## Filing and payment

- **Employees and employers.** The employer deducts PAYE, including the earners' levy where applicable, and files employment information under payday filing. Remit the deductions by Inland Revenue's separate payment dates. Earnings not liable for the levy (for example employee share scheme benefits) go in the corresponding field of the employment information.
- **Self-employed.** There is no separate ACC return. The person files the IR3 with the correct BIC code; IRD passes the income and BIC code to ACC; ACC sends an invoice. IRD: "Once ACC gets your information from us, they'll send you an invoice for your levies" ([IRD](https://www.ird.govt.nz/situations/work-or-study-in-new-zealand)). ACC begins invoicing self-employed levies from September (IR3G 2026, PDF page 60).
- **First year in business.** Because the invoice follows the income tax return, a new business usually receives its first ACC invoice only after its first IR3 is filed. Tell the client to set money aside. Any interim or first-year arrangement is **check** with ACC.
- **Employers' invoices.** ACC generally invoices around July. It can charge a provisional levy for the current year and adjust the prior year's levy when actual payroll is available. Update employer details through MyACC for Business or form ACC4618 where applicable.
- **CoverPlus Extra invoices.** ACC invoices after you accept the offer, or in April if you start the levy year on the policy. Pay by the due date whilst a review or reassessment is pending.
- **Payment and late payment.** Pay by the due date on the ACC invoice. Payment methods, instalment plans and late-payment penalties are set by ACC: **check** on the invoice.
- **Deduction.** ACC levies paid for self-employment and as an employer, and any interest charged, are claimed in Box 9 of the IR3B ([IR3B July 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3b/ir3b-2026.pdf)). The earners' levy inside an employee's PAYE is part of their tax deducted, not a business expense.

## 2025-26 returns being filed now ([IRD rates table](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates))

For the year 1 April 2025 to 31 March 2026 (IR3G 2026 and the [IRD rates table](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates)):

| What | 2025-26 | Source |
| --- | --- | --- |
| Earners' levy rate (includes GST) | 1.67% | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Maximum liable earnings | $152,790 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Maximum levy payable | $2,551.59 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |

An employee amending the tax deducted on an IR3 works out the earners' levy with the IR3G worksheet: liable salary and wages, capped at $152,790, multiplied by 1.67%. Self-employed invoices are worked out from IR3 income, so an invoice issued from September 2026 may use 2025-26 income. Check which levy year and which rates each invoice line uses (**check** on the invoice).

## Completion checklist ([IRD rates table](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates))

- [ ] Status placed: employee, self-employed, partner, LTC owner (active or passive), shareholder-employee, employer, IR56, or mixed.
- [ ] Levy year stated for every figure, and the matching row of the IRD table used (2026-27: 1.75%, $156,641).
- [ ] Liable earnings taken from the right IR3 questions; maximum applied; self-employed minimum ($50,501 for 2026-27) considered, including the full-time condition (**check**).
- [ ] Use the GST-inclusive PAYE rate for withholding and the statutory rate plus GST for standard self-employed invoice estimates.
- [ ] Payroll: only "deduct" column payments carry the earners' levy; per-pay maximum and lump-sum rule applied.
- [ ] BIC code checked on the return.
- [ ] Work levy, Working Safer levy, discounts and CoverPlus or CoverPlus Extra read from the ACC invoice, not estimated from memory.
- [ ] ACC levies paid (and interest) recorded in Box 9 of the IR3B.
- [ ] Every ACC-only point marked **check** and confirmed with ACC or on the invoice.
- [ ] Totals labelled estimates; referrals made where "When to refuse or refer" applies.

## Sources

- IRD, ACC earners' levy rates: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates (read for the 2025-26, 2026-27 and 2027-28 earners' levy rates, maximum liable earnings and maximum levy, on 2026-11-14)
- Earners' Levy Regulations 2025, regulations 4–8 for statutory rates, thresholds and GST: https://www.legislation.govt.nz/regulation/public/2025/0018/latest/LMS1019194.html (read 2026-11-22)
- Work Account Levies Regulations 2025, regulations 5–7 and Schedule 2: https://www.legislation.govt.nz/regulation/public/2025/0017/latest/LMS1019593.html (read 2026-11-22)
- Health and Safety at Work (Rates of Funding Levy) Regulations 2016: https://www.legislation.govt.nz/regulation/public/2016/0020/8.0/DLM6725448.html (read 2026-11-22)
- ACC, calculating your levies, hours worked, limits, multiple employers and IR56: https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies (read 2026-11-22)
- ACC, Experience Rating and end of No Claims Discount: https://www.acc.co.nz/for-business/your-work-levy-and-experience-rating/understanding-the-experience-rating-programme (read 2026-11-22)
- ACC, levy invoicing for employers and self-employed: https://www.acc.co.nz/for-business/understanding-levies-if-you-work-or-own-a-business (read 2026-11-22)
- ACC, CoverPlus Extra invoicing and terms: https://www.acc.co.nz/for-business/understanding-your-cover-options/optional-cover-coverplus-extra-cpx (read 2026-11-22)
- ACC, employer invoice timing: https://www.acc.co.nz/for-business/manage-your-business-online/online-business-account (read 2026-11-22)
- ACC, employer changes and form ACC4618: https://www.acc.co.nz/for-business/update-your-business-details/change-my-details (read 2026-11-22)
- IRD Smart Business, ACC GST input tax, page 52: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir320/ir320.pdf?modified=20251014030747 (read 2026-11-22)
- IRD, payment dates for employer deductions: https://www.ird.govt.nz/employing-staff/payday-filing/paying-deductions-to-inland-revenue (read 2026-11-22)
- IRD, Employer's guide IR335 (September 2026): https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf (read 2026-11-14 for the PAYE earners' levy rate, per-pay maximums, the ND rate and which payments carry the levy (page 18))
- IRD, Payroll calculations and business rules specification, 1 April 2026 to 31 March 2027: https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf (read 2026-11-14 for the 2026-27 maximum liable earnings ($156,641) and the self-employed minimum ($50,501))
- IRD, Individual income tax return guide IR3G 2026: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf (read for who pays which levy by situation and the return treatment, on 2026-11-14)
- IRD, IR3B Schedule of business income (July 2026): https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3b/ir3b-2026.pdf (read for where self-employed income for the levy is reported, on 2026-11-14)
- IRD, ACC levies for a look-through company: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company (read for ACC levies for LTC working owners, on 2026-11-14)
- IRD, I am coming to work or study in New Zealand: https://www.ird.govt.nz/situations/work-or-study-in-new-zealand (read for the arrival position for new workers, on 2026-11-14)
- IRD, Updating a client's BIC code: https://www.ird.govt.nz/roles/tax-agents/updating-client-bic-code (read for BIC codes and how they feed the Work levy, on 2026-11-14)
- IRD, Information sharing with ACC: https://www.ird.govt.nz/about-us/information-sharing/mous/acc (read for what IRD shares with ACC for levy invoicing, on 2026-11-14)

Not yet confirmed: the superseded March 2025 Inland Revenue news link returns 404. Verify invoice-specific classification, adjustments, cover and due date from the current ACC records.

This skill is general information, not tax advice. Confirm ACC-only points with ACC and have a New Zealand chartered accountant review the position before acting.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nz-acc-levies` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nz-acc-levies. If neither is available, confirm every figure against the official source pages cited above before relying on it.
