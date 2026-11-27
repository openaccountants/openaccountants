---
name: il-estimated-tax
description: Work out a full-year Illinois individual's 2026 estimated income tax on Form IL-1040-ES. Covers the more-than-$1,000 test after withholding and credits, the four payment dates, the distinction between the full-tax worksheet and 90% current-year or 100% qualifying prior-year penalty protection, withholding timing, annualization, farmer and nursing-home exceptions, and installment penalties. Trigger on "Illinois estimated tax", "IL-1040-ES", "IL-2210", or "Illinois quarterly payments". Obtain the tax base and eligible credits through il-income-tax; preserve the separately dated 2025 regression cases.
version: "2.1"
jurisdiction: US-IL
category: state-tax
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Illinois estimated income tax for individuals, tax year 2026

> **General reference only.** Built from the law; not yet approved. This Guide has not been reviewed for a particular taxpayer's facts. Obtain qualified professional review before filing or paying. US Circular 230, 31 CFR §10.37: this general illustration does not establish a tax position for a particular taxpayer.

An individual generally must make estimated payments if expected 2026 Illinois tax exceeds **$1,000 after withholding and allowed credits**. The full-tax worksheet and the amount protecting against an installment penalty are different calculations. Illinois uses **90% of current-year tax or 100% of qualifying prior-year tax**, without a high-income 110% uplift, and credits payments and withholding against each installment. [35 ILCS 5/803(b), 804(c), (f), (g)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000)

## Scope and who this is for

Full-year resident individuals, including sole proprietors and disregarded single-member LLC owners, using IL-1040-ES. This Guide covers estimates, their timing and installment penalties. It does not turn Schedule C profit directly into Illinois base income.

| Original topic | Destination |
| --- | --- |
| Federal AGI, Schedule M additions/subtractions, bonus depreciation and Illinois base income | `il-income-tax`; obtain a checked computation before using worksheet line 1 |
| Exemption entitlement and credits, including property tax, K-12, EITC, child tax, other-state and PTE credits | `il-income-tax`; obtain the eligible amounts, rather than treating a listed credit as automatic |
| Federal estimated tax and its separate safe-harbour rules | `us-quarterly-estimated-tax` |
| Corporation/PTE estimates, pass-through withholding obligations, composite/entity returns | `il-pprt`; do not use individual vouchers for entity returns |
| Employer withholding | `il-payroll` |
| Nonresident/part-year allocation, audit adjustments, abatement and interest | Explicit holds under “When to refuse or refer” below |

## Ask the client first

Obtain filing status, residence, actual Illinois base-income computation, eligible exemptions and credits; the filed 2025 return and whether it covered 12 months; 2026 withholding by type and date; income received by period; all estimates and any overpayment election/payment dates; and farmer/nursing-home facts. Retrieve available records before asking. Missing withholding, a prior-year return or an overpayment election is an unresolved input: do not silently substitute zero or invent eligibility.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or condition | Official source |
| --- | --- | --- |
| Individual estimated-tax threshold | More than $1,000 after withholding and credits; exactly $1,000 does not trigger estimates | [803(a), (b)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000) |
| Worksheet tax rate | 4.95% of net income | [2026 IL-1040-ES, line 4](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf) |
| Basic exemption amount, subject to entitlement | $2,925 in 2026; $2,850 in 2025, not the former $2,625 | [FY 2026-15, personal exemption](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html) |
| Exemption income cliff | No exemption if AGI exceeds $500,000 on a joint federal return or $250,000 otherwise; dependency and allocation rules also apply | [204(a), (b), (g)](https://my.ilga.gov/legislation/ilcs/fulltext?DocName=003500050K204) |
| Ordinary required installment | 25% of the required annual payment before installment payment/withholding credits | [804(c)(1)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000) |
| Required annual payment | Lesser of 90% current-year tax and 100% prior-year tax, if the prior return was filed, showed a tax liability and covered 12 months | [804(c)(1)(B)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000) |
| Annualized cumulative percentages | 22.5%, 45%, 67.5%, 90% | [804(c)(2)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000) |
| Late estimated-payment penalty | 2% of the late amount paid within 30 days; 10% of the amount paid later | [735/3-3(b-25)(1)](https://www.ilga.gov/documents/legislation/ilcs/documents/003507350K3-3.htm) |

The basic amount is not an unconditional allowance per person. Section 204(b) denies it to a dependent whose Illinois base income exceeds that amount; 204(a) applies the Illinois allocation fraction. Section 204(d) adds $1,000 for the taxpayer's qualifying age-65 or blindness condition; a spouse on a separate return also needs no gross income and must not be another taxpayer's dependent. Establish entitlement through the income-tax computation. [204](https://my.ilga.gov/legislation/ilcs/fulltext?DocName=003500050K204)

### Full-tax worksheet

Use the **2026** IL-1040-ES worksheet, not a prior-year return's line mapping:

1. Line 1: checked Illinois base income. Line 2: eligible total exemption. Line 3: line 1 minus line 2. Line 4: line 3 multiplied by 4.95%.
2. Line 5: applicable medical-cannabis and gaming-licensee asset-sale surcharges. Line 6: lines 4 plus 5. A surcharge case requires a checked surcharge computation.
3. Line 7: expected Illinois withholding and pass-through withholding. Line 8: allowed credits for property tax, volunteer emergency workers, other-state income tax, K-12 education, EITC, child tax, PTE tax and Schedule 1299-C. Line 9: lines 7 plus 8.
4. Line 10: line 6 minus line 9. At $1,000 or less, stop. Above $1,000, line 11 divides line 10 by four and rounds to whole dollars. This budgets the full estimated tax, rather than automatically calculating the minimum protected amount.
5. If income changes, refigure the worksheet and use its Amended Estimated Tax Worksheet, which accounts for installments already due and payments already made. Do not simply divide the revised tax by four and ignore earlier shortfalls.

Source: [2026 IL-1040-ES, worksheet and amended worksheet](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf).

### Penalty protection and payment credits

Under 804(c)(1), calculate the lesser of 90% current-year tax and 100% qualifying prior-year tax. The prior-year alternative requires a filed return showing liability for a 12-month year; it is unavailable merely because an amount called “last year's tax” was supplied. Illinois has no high-income 110% substitution. Planning uses projected current tax, but the current-year protection ultimately uses the tax shown on the return (or actual tax if no return is filed), not a lower forecast. Section 804(f) defines tax for this purpose by reference to Article 2 tax less section 601(b)(3) and (4) credits. IDOR's IL-2210 mechanism additionally sets out the allowed tax credits before its 90% calculation; withholding is a payment afterward, not a deduction before multiplying by 90%. [804(c), (f), (g)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000), [available 2025 IL-2210, Step 2](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-2210.pdf).

Apply a quarter of the required annual amount to each due date, then credit withholding and timely estimates, carrying forward earlier excesses. Wage withholding is normally deemed paid one-quarter on each date; actual withholding dates may be established instead. Timely pass-through withholding has its own deemed date: the last day of the entity's taxable year, not automatically one-quarter per date. [804(g)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000).

An elected 2025 overpayment can reduce installments until used. The 2026 ES form requires the election by the prior return's extended due date for first-installment treatment; otherwise it counts when elected. The available IL-2210 instructions add that a portion originating in payments made after the prior return's original due date counts on its actual payment date. Do not treat every carryforward as paid on 15 April. [2026 ES](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf), [IL-2210 instructions, Step 4 line 20](https://tax.illinois.gov/forms/incometax/currentyear/individual/il-2210-instr.html).

For uneven income, 804(c)(2) permits a lower annualized installment. Annualize net income before the standard exemption for the completed months before the installment month: multiply by 12 and divide by those months, then deduct the applicable annual exemption. Apply the cumulative percentage and subtract earlier **required** installments. A reduction must be recaptured in later installments to the extent not already recaptured. Do not use the percentage alone as a payment formula or declare an early installment penalty-free without the full calculation. [804(c)(2)(A), (B), (D)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000).

The currently read IL-2210 and instructions are **2025** documents. They illustrate the credit/payment mechanism, not verified 2026 return line numbers. A final 2026 IL-2210 submission, annualized outcome or unusual-credit calculation is a non-usable hold pending that year's form check. Check this point with one of our partner accountants.

### Exceptions and boundaries

| Facts | Treatment |
| --- | --- |
| Farming gross income at least two-thirds of total estimated gross income for the year | Farmer excluded from the estimated-payment requirement, 803(a), (e) |
| Age 65 or older and permanent nursing-home residence | 806 exempts the installment penalty; “nursing home” is a licensed skilled/intermediate long-term-care facility under the Acts listed there. IDOR's ES form says estimates are not required |
| No requirement to file an Illinois return for 2025 | No 2026 estimated-tax underpayment penalty under 804(d). Being a new resident alone is not the test |
| Individual had no 2025 tax liability and that year covered 12 months | No 2026 estimated-tax underpayment penalty under 804(d); a short zero-liability year does not establish this exception |
| 2025 return covered fewer than 12 months | No 100% prior-year alternative; calculate the current-year route unless another exception applies |
| Joint estimates but separate final returns | If eligible for federal joint treatment, estimated payments may be allocated to either spouse or divided as elected, 803(c); different filing statuses also require proper prior-tax allocation |
| Fiscal-year or short-year taxpayer | 803(g) shifts the months; short years require the regulations under 803(f), 804(i). A specific short-year outcome is held below |

Source: [803, 804 and 806](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000), [IL-2210 instructions, differing filing statuses](https://tax.illinois.gov/forms/incometax/currentyear/individual/il-2210-instr.html).

### Filing and payment

Calendar-year 2026 installments are due **15 April, 15 June and 15 September 2026, and 15 January 2027**. The whole estimate may be paid on the first date. A weekend/holiday due date moves to the next business day. [2026 ES](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf), [Publication 105](https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html).

Pay from a bank account through MyTax Illinois using the IL-PIN, by card with a provider fee, or by EFT under Form EFT-1. Electronic payments need no paper voucher. For check/money-order payments, complete the voucher and print the Social Security number(s), tax year and “IL-1040-ES” on the payment; mail both to the voucher address and record the payment. Entity filers including IL-1041, IL-1065, IL-1120, IL-1120-ST and IL-990-T do not use this voucher. [2026 ES](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf).

### Penalties and interest

The late estimated-payment penalty applies to each installment's shortfall, not the whole annual tax or an annual interest rate. For returns due on or after 1 January 2024, 735/3-3(b-25)(1) charges **2%** on the late amount paid within 30 days and **10%** on the amount paid later. Partial payments require separate payment-date treatment. IDOR applies payments to the earliest unpaid due date unless instructed otherwise. [804(a), (b)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000), [735/3-3](https://www.ilga.gov/documents/legislation/ilcs/documents/003507350K3-3.htm), [Publication 105](https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html).

Final-return unpaid-tax penalties and interest are separate from this installment calculation. This Guide does not supply an interest rate or a complete annual-return penalty. Check this point with one of our partner accountants.

## Worked cases

### Case 1: full-tax worksheet, 2026

A single full-year resident has **checked Illinois base income $100,000**, one eligible $2,925 exemption, no surcharges, withholding or credits. This is a stipulated base-income input, not a conclusion from $100,000 Schedule C profit. Net income is $97,075; tax to cents is $4,805.21. It exceeds $1,000. The worksheet's full-tax budget is $1,201 per installment after whole-dollar rounding; it is not the final balance or a claim to have found the minimum protected payment. [2026 ES](https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf), [2026 exemption](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html).

```oa-check
name: Illinois full-tax worksheet 2026
inputs:
  base_income: 100000
  exemption: 2925
  withholding_and_credits: 0
steps:
  - net_income: base_income - exemption
  - tax: round(net_income * 0.0495, 2)
  - estimated_tax: tax - withholding_and_credits
  - installment: round(estimated_tax / 4, 0)
expected:
  net_income: 97075
  tax: 4805.21
  estimated_tax: 4805.21
  installment: 1201
```

### Case 2: prior-year protection, 2026

Retain the consultant's 2026 tax **$8,000**, filed 12-month 2025 return showing tax **$5,000**, with no withholding, credits, earlier excesses or exceptions. Compare $7,200 with $5,000: the protected annual amount is $5,000, or **$1,250 per due date**. The remaining tax is $3,000, payable by the return's original payment deadline; the installment safe harbour does not forgive it. If precisely the first $1,250 shortfall is paid 20 days late, the other installments are timely and no relief applies, the installment penalty is **$25**. [804(c)](https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000), [735/3-3(b-25)(1)](https://www.ilga.gov/documents/legislation/ilcs/documents/003507350K3-3.htm), [601(a)](https://www.ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=16200000&SeqStart=15400000).

```oa-check
name: Illinois qualifying prior-year protection and isolated late payment 2026
inputs:
  tax_2026: 8000
  tax_2025: 5000
steps:
  - current_test: tax_2026 * 0.90
  - prior_test: tax_2025 * 1.00
  - required_annual: min(current_test, prior_test)
  - installment: required_annual * 0.25
  - balance_with_return: tax_2026 - required_annual
  - late_penalty_20_days: installment * 0.02
expected:
  current_test: 7200
  required_annual: 5000
  installment: 1250
  balance_with_return: 3000
  late_penalty_20_days: 25
```

### Historical 2025 cases: preserved inputs, non-usable outcomes

These are the original 2025 regression inputs, not 2026 cases. The 2025 calendar-year dates were 15 April, 16 June (15 June was Sunday), 15 September 2025 and 15 January 2026, derived from 803(d) and Publication 105's business-day rule. Their former payment recommendations are withdrawn pending the base, eligibility and prior-year facts below. Arithmetic alone does not clear a tax result. Check this point with one of our partner accountants.

| Original case | Preserved inputs and arithmetic check | Hold |
| --- | --- | --- |
| 1, single full-year freelancer | Schedule C net $100,000; no withholding/other credits. At the later corrected 2025 exemption $2,850: ($100,000 - $2,850) × 4.95% = $4,808.93; divided by four = $1,202.23 before whole-dollar rounding | Schedule C profit is not established Illinois base income; confirm that base and exemption before using this as a payment result. Check this point with one of our partner accountants. |
| 2, part-year freelancer | Stated Illinois taxable income $8,000, withholding $0; $8,000 × 4.95% = $396 | Allocation and exemption facts were never established; $396 is arithmetic, not a cleared part-year liability. Check this point with one of our partner accountants. |
| 3, prior-year route | Current 2025 estimated tax $6,000; prior 2024 tax $4,000. min($5,400, $4,000) = $4,000; divided by four = $1,000 | Confirm tax definitions, credits/withholding and filed 12-month prior return showing liability. Check this point with one of our partner accountants. |
| 4, joint with wages | Combined income $150,000; spouse W-2 withholding $3,200. At the corrected joint exemption $5,700: tax arithmetic $7,142.85; less withholding $3,942.85; divided by four $985.71 | Confirm Illinois base, both exemption entitlements and whether this is a full-tax budget or minimum protection; withholding must not be reduced by 90%. Check this point with one of our partner accountants. |
| 5, property credit | Original label “IL taxable income $80,000”; property tax paid $6,000. Original base-style arithmetic with $2,850 exemption: tax $3,818.93; assumed 5% credit $300; net $3,518.93; divided by four $879.73 | “Taxable income” and base income were conflated. Property-credit eligibility and income cutoff must be checked; the $300 is a historical assumed credit, not an allowance granted here. Check this point with one of our partner accountants. |

The even older $2,625/$5,250 exemptions and $500 threshold are superseded, not alternative 2025 constants. With those obsolete inputs, case 4 arithmetic was ($150,000 - $5,250) × 4.95% = **$7,165.13**, not $7,170.23; less $3,200 is $3,965.13 and divided by four is $991.28. None is a usable 2025 payment result. The 2025 exemption amount is $2,850, with two basic allowances totaling $5,700 only when eligible. [FY 2026-15](https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html).

## When to refuse or refer

Each hold below preserves a topic but supplies no usable tax conclusion:

- Part-year/nonresident Schedule NR allocation, composite returns, audit-adjusted estimates or penalty abatement: Check this point with one of our partner accountants.
- A short tax year, a final 2026 annualized/IL-2210 result, an unusual credit, a surcharge or an overpayment whose payment/election timing cannot be established: Check this point with one of our partner accountants.
- Bonus-depreciation add-back, Schedule M line mapping, EITC/child-credit eligibility and property-credit eligibility have not been proven by this estimates Guide; obtain a checked `il-income-tax` result before using them. Check this point with one of our partner accountants.
- Annual-return late-payment penalties, interest rates and interest periods: Check this point with one of our partner accountants.

## Sources

| Official source and operative sections | URL | Read on |
| --- | --- | --- |
| Read for IITA Article 8: 803(a)-(h), 804(a)-(i), 806; threshold, tax definition, installments, annualization, payment timing and exceptions | https://ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=18800000&SeqStart=18300000 | 2026-11-27 |
| Read for IITA 204(a)-(g), exemption eligibility, dependency, allocation, age/blindness and income cliff | https://my.ilga.gov/legislation/ilcs/fulltext?DocName=003500050K204 | 2026-11-27 |
| Read for Uniform Penalty and Interest Act 3-3(b-25)(1), current estimated-payment penalty | https://www.ilga.gov/documents/legislation/ilcs/documents/003507350K3-3.htm | 2026-11-27 |
| Read for IITA 601(a), tax payment by original return deadline | https://www.ilga.gov/legislation/ILCS/details?ActID=577&ActName=Illinois+Income+Tax+Act.&ChapAct=35+ILCS+5/&Chapter=REVENUE&ChapterID=8&MajorTopic=GOVERNMENT&Print=True&SeqEnd=16200000&SeqStart=15400000 | 2026-11-27 |
| Read for 2026 IL-1040-ES, R-09/26: worksheet, amended worksheet, dates, credit election and payment instructions | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-1040-es.pdf | 2026-11-27 |
| Read for FY 2026-15: 2025 and 2026 basic exemption amounts | https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html | 2026-11-27 |
| Read for Publication 105, December 2025: business-day convention and payment application | https://tax.illinois.gov/research/publications/pubs/illinois-estimated-payments-requirements-for-individuals-and-businesses.html | 2026-11-27 |
| Read for available 2025 IL-2210 and instructions: Step 2 credits/payment separation; Step 4 carryforward timing. Not a 2026 line-number verification | https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/individual/il-2210.pdf ; https://tax.illinois.gov/forms/incometax/currentyear/individual/il-2210-instr.html | 2026-11-27 |

Not yet confirmed: none asserted as usable. The specifically identified holds above require partner-accountant resolution before use. The official 204 and 3-3 text was read in the search service's expanded official-page text after direct page loads failed; URL access alone was not treated as a read.
