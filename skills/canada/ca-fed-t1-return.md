---
name: ca-fed-t1-return
description: Use this skill whenever asked about a Canadian federal T1 General individual income tax return for a self-employed sole proprietor. Trigger on phrases like "T1 return", "personal tax Canada", "federal tax brackets", "basic personal amount", "CPP self-employed", "CPP2", "self-employment tax Canada", "net income", "taxable income", "federal tax calculation", "non-refundable credits", "instalment payments", or any question about computing federal tax for a self-employed individual in Canada. ALWAYS read this skill before touching any T1 return work.
version: 2.2
jurisdiction: CA
tax_year: 2025
tax_year_notes: This Guide intentionally computes the 2025 T1 filed in 2026; original 2026 cross-references are separately labelled and never substituted.
type: computation
last_updated: 2026-11-27
source_checked: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# Canadian federal T1 return - self-employed, 2025

## Scope

Federal return assembly for a full-year Canadian-resident sole proprietor, in CAD. Use the 2025 T1 **Step 5** for federal tax; the old Schedule 1 references are obsolete. Provincial tax is a separate calculation. Do not use the examples as a complete filing balance or silently substitute 2026 rates.

Historical attribution, retained without renewing approval:
Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Contributor: Open Accountants Community.

| Historical attribution field | Original record |
| --- | --- |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |

## Ask the client first

Obtain legal identity and SIN for filing, date of birth, marital status, December 31 province/territory, business permanent establishments, all T-slips and other income, T2125 net business/professional/commission income, RRSP receipts and actual deduction limit, other deduction/credit evidence, withholding, instalments, prior assessments, CPP/QPP deductions and elections, disability/retirement periods and EI agreement dates. Do not invent missing amounts: an illustrative zero deduction must be labelled as an assumption. An unknown province, RRSP entitlement, CPP status or EI agreement blocks the affected final computation.

Bank statement classification and business expenses belong to `ca-fed-t2125`; reconcile its result to supporting records before return assembly. A sole proprietor is the scope; the historical reference to an LLC is not an entity-classification conclusion. Partnerships, corporations and entity classification: Check this point with one of our partner accountants.

## The method, step by step

### Income and return flow

Use the actual [2025 T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), not a copied prior-year line list:

1. Assemble income at line 15000. Employment is line 10100/10400; OAS is **11300**, other pensions/superannuation **11500**; taxable Canadian dividends 12000, interest 12100; business/professional/commission net income 13500/13700/13900. Farming/fishing and their special rules require separate review.
2. Deduct allowable amounts, including RRSP at 20800, self-employed CPP at 22200 and enhanced employee CPP at **22215**; reach net income before adjustments 23400, then subtract any social benefits repayment 23500 to reach net income 23600. Do not describe 23400 as net business income or 22215 as self-employed CPP2.
3. Apply the permitted Step 4 deductions and zero floor to taxable income 26000; do not deduct business costs or CPP twice.
4. Compute federal tax on 26000, then credits and Step 5 Part C adjustments through net federal tax 42000. Amount 35000 is **total federal non-refundable credits**, not federal tax. The basic federal tax line is 42900.
5. Complete Step 6: include self-employed CPP 42100, EI 42120, applicable social-benefit repayment and provincial tax; then use the actual return's total credits/payments to determine refund/balance. Withholding is 43700, instalments 47600. Do not subtract separately paid GST/HST credits or CCB as T1 payments.

RRSP: $32,490 is the **2025 annual dollar limit**, not everyone's available deduction. The deduction limit includes unused room plus the positive excess of min(18% of **2024 earned income**, $32,490) over the prior-year pension adjustment and prescribed amount, plus pension adjustment reversal, less net past-service pension adjustment. Confirm receipts, eligibility, unused contributions, employer PRPP contributions and the actual CRA limit before claiming a deduction. Uncertain earned-income, spousal/transfer/age or contribution timing cases: Check this point with one of our partner accountants. [ITA 146(1), (5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html); [2025 limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html).

Other income/deductions from the historical line matrix remain intake items, not automatic claims: rental, capital gains, EI benefits, workers' compensation/social assistance; RPP, pension splitting, union/professional dues, childcare, disability supports, ABIL, moving, support, carrying charges, employment expenses and clergy residence; Armed Forces/security-option deductions, other-payments deductions, partnership/non-capital/net-capital losses, capital-gains and northern-residents deductions. Eligibility, allocation, losses and carryovers: Check this point with one of our partner accountants.

### Federal Tax Brackets (2025)

Apply each rate to the portion of **taxable** income in the band, including cents; no gaps at whole-dollar boundaries. The final column gives the formula using CRA's rounded base amounts.

| Taxable income T (CAD) | Marginal rate | Federal tax before credits | Source |
| --- | --- | --- | --- |
| T at most $57,375 | 14.5% | T × 14.5% | [2025 T1 p5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| $57,375 < T at most $114,750 | 20.5% | $8,319.38 + (T − $57,375) × 20.5% | same |
| $114,750 < T at most $177,882 | 26% | $20,081.25 + (T − $114,750) × 26% | same |
| $177,882 < T at most $253,414 | 29% | $36,495.57 + (T − $177,882) × 29% | same |
| T above $253,414 | 33% | $58,399.85 + (T − $253,414) × 33% | same |

The 2025 full-year first rate is 14.5%; do not prorate by when income was earned. [S.C. 2026 c.2 s2(1), (3), (4)](https://laws-lois.justice.gc.ca/eng/annualstatutes/2026_2/page-1.html) supplies the operative 2025 rule; the current consolidated ITA instead prints the later 14% rate. Thresholds are indexed under [ITA 117.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html).

### Basic Personal Amount (2025)

For the full-year resident in scope, use net income **23600**, not taxable income, for this table. The end points overlap only at the same resulting amount.

| Net Income | BPA |
| --- | --- |
| $177,882 or less | $16,129 |
| $177,882 -- $253,414 | Graduated reduction |
| $253,414+ | $14,538 |

Between the two thresholds: BPA = $16,129 - $1,591 x (net income - $177,882) / $75,532. Flag if net income between $177,882 and $253,414. Outside them use the capped amounts, not an unbounded clawback. The BPA enters line 30000; its ordinary 2025 credit is BPA × 14.5%. [ITA 118(1), (1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [2025 Federal Worksheet p3](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).

### CPP Self-Employed (2025)

The following short formula is only for **12 contributory months, pensionable self-employment earnings only**, no Quebec earnings/QPP, no employment contributions, no disability/election/exemption or other adjustment, and no retirement-benefit-start proration. All examples using it assume age 18–64 throughout 2025 and those conditions. Complete Schedule 8 Parts 1–2 first; age, disability, election and death can change the months and ceilings. Age 65–69 is not automatically optional: an election requires a CPP/QPP retirement pension. Special coverage, partial-year or election cases: Check this point with one of our partner accountants. [CPP Act 10](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-10.html), [13](https://laws-lois.justice.gc.ca/eng/acts/C-8/section-13.html); [2025 Schedule 8 pp1–3](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

For net pensionable earnings E, let B = max(0, min(E, 71,300) − 3,500) and A = max(0, min(E, 81,200) − 71,300).

| Component | Self-employed contribution | Full-year maximum | Source |
| --- | --- | --- | --- |
| Base CPP | B × 9.9% | $6,712.20 | [2025 Schedule 8 pp3,6–7](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) |
| First additional CPP | B × 2% | $1,356.00 | same |
| Base plus first additional (computed) | B × 11.9% | $8,068.20 | same |
| Second additional CPP (CPP2) | A × 8% | $792.00 | same |

YMPE is $71,300, YAMPE $81,200 and basic exemption $3,500. The $792 above is **CPP2**, not QPP2. Rates for an employee alone are 5.95% and 4%, half the combined self-employed rates. [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

Half of base CPP plus all first and second additional (CPP2) contributions are deductible (line 22200); the other half of base CPP is a non-refundable credit (line 31000).

At the full-year maxima this gives deduction $3,356.10 + $1,356 + $792 = **$5,504.10**, base credit amount **$3,356.10**, payable **$8,860.20** at 42100. Do not credit half the enhanced contributions. [ITA 60(e)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html), [118.7](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.7.html); Schedule 8 Part 4.

For employment plus business income use **Part 3 then Part 5** of Schedule 8. Do not apply two full exemptions or deduct the employee contribution from the self-employed maximum as if the rates were identical. Quebec-resident/QPP or cross-province CPP/QPP cases need their applicable schedule/RC381, not this shortcut: Check this point with one of our partner accountants.

### EI self-employment and other credits

- **EI rate (2025) -- $1.64/$100** outside Quebec; maximum earnings $65,700 and premium $1,077.48. Quebec rate is $1.31/$100 (not $1.30), maximum $860.67. These rates apply through an EI self-employment agreement for an eligible Canadian citizen/permanent resident, not automatically to every sole proprietor. Under EI Act 152.21 the premium base is the lesser of self-employed earnings and the annual insurable ceiling **less employment insurable earnings**; it is not a second full annual maximum. Premiums apply to the agreement-entry year regardless of entry date. Use Schedule 13; no employer 1.4× addition to this self-employment premium. [EI Act 152.02](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-152.02.html), [152.21](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-152.21.html); [2025 authority announcement](https://www.canada.ca/en/employment-social-development/news/2024/09/canada-employment-insurance-commission-confirms-2025-employment-insurance-premium-rate.html).
- EI under this scheme concerns special benefits, not an entitlement to regular unemployment benefits. Twelve months after agreement is only one eligibility condition; continuing agreement, interruption of earnings and qualifying earnings also matter. Benefit types (maternity, parental, sickness, compassionate care, family caregiver), Quebec/QPIP coordination and termination/opt-out: Check this point with one of our partner accountants. [EI Act 152.07](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/section-152.07.html).
- Self-employed EI premiums enter credit amount 31217 and payable 42120. Ordinary credit rate is 14.5% under [ITA 118.7](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.7.html); use [2025 T1 Step 5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).
- Canada employment amount 31260 is min($1,471, eligible employment income) for 2025; business profits do not generate it, but genuine employment income can qualify even if the person also has a business. [ITA 118(10)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html) controls over CRA's overbroad “not self-employed” summary.
- Canadian taxable-corporation dividends, eligible: taxable amount is cash × 1.38 and federal dividend tax credit 15.0198% of taxable amount; other-than-eligible: cash × 1.15 and 9.0301%. Use slip taxable amounts/credits where supplied; do not gross up twice. Foreign dividends do not get this credit. These rates cover both original 2025/2026 references. These shortcuts exclude capital-gain dividends, mortgage investment corporation distributions, dividend-rental arrangements, attribution/TOSI and unclear designation. Check this point with one of our partner accountants. [ITA 82](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html), [121](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-121.html); [CRA T5 Guide, boxes 11/12/25/26](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4015/t5-guide-return-investment-income.html); [Federal Worksheet pp1,8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).
- Compute ordinary credit amounts at 14.5%, then add the separately calculated donations/gifts credit and **top-up credit 34990**. For 2025 the top-up is max(0, line 33800 + Schedule 9 line 22 − $8,319.38) × 3.45%, using the Federal Worksheet. Non-refundable credits cannot themselves create a refund. [ITA 118(11)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [2025 Worksheet p7](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).
- Medical costs (including the historical 3%/dollar-threshold shorthand), charitable gifts (first-$200 and higher-rate bands), age, spouse/dependant/caregiver, disability/T2201, tuition/transfers and home accessibility credits: **no usable eligibility or amount conclusion here**. Use the actual 2025 forms and supporting evidence; Check this point with one of our partner accountants. Do not revive the old unqualified or prior-year credit table.

The old next-year cross references remain separate from 2025 computation: **2026** second federal band $58,523.01–$117,045 at 20.5%, and Canada employment amount ceiling $1,501. They must not enter a 2025 calculation. [CRA indexed 2026 table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html).

### Filing, payment and instalments

For 2025, ordinary self-employed filing is **June 15, 2026**, also applying to the qualifying spouse/partner. The extension does not apply where the business expenditures were primarily tax-shelter investment costs. Payment remains **April 30, 2026**; unpaid tax bears prescribed-rate compound daily interest from **May 1, 2026**. [ITA 150(1)(d)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html); [CRA 2025 dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html); [interest](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html).

Ordinary late-return penalty: 5% of tax unpaid when filing was due plus 1% per **complete** late month, at most 12. The repeated-failure rule needs **both** a demand to file for this year and a penalty payable for any of the three preceding years before the failure; then 10% plus 2% per complete month, at most 20. Do not treat “second late return” alone as sufficient. [ITA 162(1)–(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html).

Ordinary instalments: net tax owing must exceed $3,000 ($1,800 for Quebec residence at year-end) in **2025 and either 2024 or 2023**. Net tax owing uses the statutory credits/withholding adjustments and, outside Quebec, includes the collected provincial income tax; it is not simply the federal balance on a return. Farming/fishing as chief income source uses a different test and calendar: Check this point with one of our partner accountants. [ITA 156.1(1)–(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html).

The ordinary quarterly dates are March 15, June 15, September 15 and December 15; the next business day applies if a due date is a weekend or CRA-recognized public holiday. For 2025 the first two dates become **March 17 and June 16**. CRA's no-calculation reminder, prior-year and current-year methods are alternatives; instalment amounts also account for CPP payable and voluntary EI, so do not blindly divide federal tax by four. Late/insufficient instalments can attract interest; use actual reminders, payments, applicable rates and the statutory calculation before quantifying it. Instalment-interest/penalty calculations: Check this point with one of our partner accountants. [ITA 156](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html); [CRA options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html); [due-date convention](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

## Worked cases

All five tests keep their original 2025 inputs. Calculations are rounded half up to cents and use the stated full-year CPP assumptions. For tests 1–3 assume no other deductions/credits, no refundable benefits, no AMT/TOSI or other federal adjustments; the RRSP inputs are assumed **allowable**, not inferred from income. Federal subtotals exclude provincial tax and payments; they are not final balances. The low-income test does not decide Canada workers benefit eligibility.

### Test 1 - Standard self-employed (current Example 1)

Net business income **$85,000**, RRSP **$10,000**, no other income, no dependants, **Ontario**, no EI. CPP $8,860.20; deduction $5,504.10; net/taxable income $69,495.90. Federal tax before credits $10,804.16; BPA credit $2,338.71, CPP credit $486.63; federal tax **$7,978.82**. Federal tax plus CPP **$16,839.02**, before provincial tax/payments.

```oa-check
name: Original 2025 test 1 - Ontario profit 85000
inputs:
  profit: 85000
  rrsp: 10000
steps:
  base: (71300 - 3500) * 0.099
  first: (71300 - 3500) * 0.02
  second: (81200 - 71300) * 0.08
  cpp: base + first + second
  deduction: base / 2 + first + second
  taxable: profit - rrsp - deduction
  gross_tax: round(8319.38 + (taxable - 57375) * 0.205, 2)
  bpa_credit: round(16129 * 0.145, 2)
  cpp_credit: round(base / 2 * 0.145, 2)
  federal: gross_tax - bpa_credit - cpp_credit
  subtotal: federal + cpp
expected:
  cpp: 8860.20
  deduction: 5504.10
  taxable: 69495.90
  gross_tax: 10804.16
  federal: 7978.82
  subtotal: 16839.02
```

### Test 2 - Low income (current Example 2)

Net business income **$14,000**, no other income, no RRSP. CPP $1,249.50, deduction $729.75; net/taxable income $13,270.25. Pre-credit tax $1,924.19; BPA/CPP credits exceed it, so federal tax **$0**, CPP still **$1,249.50**. Province and refundable-credit facts remain unprovided.

```oa-check
name: Original 2025 test 2 - profit 14000
inputs:
  profit: 14000
steps:
  base: (profit - 3500) * 0.099
  first: (profit - 3500) * 0.02
  deduction: base / 2 + first
  taxable: profit - deduction
  gross_tax: round(taxable * 0.145, 2)
  federal: max(0, gross_tax - round(16129 * 0.145, 2) - round(base / 2 * 0.145, 2))
  cpp: base + first
expected:
  deduction: 729.75
  taxable: 13270.25
  gross_tax: 1924.19
  federal: 0
  cpp: 1249.50
```

### Test 3 - High income (current Example 3)

Net business income **$300,000**, RRSP **$32,490**, no other income. The original “max” means the annual dollar limit, not an established personal maximum. Assuming the input is allowable, CPP $8,860.20, deduction $5,504.10, net/taxable income **$262,005.90**; pre-credit tax $61,235.18; BPA $14,538/credit $2,108.01, CPP credit $486.63; federal tax **$58,640.54**. No donations were supplied: the old extra donation-rate conclusion is not part of this test.

```oa-check
name: Original 2025 test 3 - profit 300000
inputs:
  profit: 300000
  rrsp: 32490
steps:
  base: 67800 * 0.099
  deduction: base / 2 + 67800 * 0.02 + 9900 * 0.08
  taxable: profit - rrsp - deduction
  gross_tax: round(58399.85 + (taxable - 253414) * 0.33, 2)
  federal: gross_tax - round(14538 * 0.145, 2) - round(base / 2 * 0.145, 2)
expected:
  deduction: 5504.10
  taxable: 262005.90
  gross_tax: 61235.18
  federal: 58640.54
```

### Test 4 - Employment/CPP overlap, restored historical test

Employment **$55,000**, employee CPP **$3,064.25** (5.95% on $51,500), business **$30,000**. Assume all employment is pensionable with correct full-year deductions, no CPP2 through employment and no other Schedule 8 adjustments. Remaining first-ceiling earnings $16,300: self-employed CPP $1,939.70 plus CPP2 $792 = **$2,731.70**, not another full maximum. Self-employed base credit amount $806.85 and deduction $1,924.85. Use Schedule 8 Part 5 for the real return, including employee deductions/credits; no complete tax balance is calculated.

```oa-check
name: Original 2025 test 4 - mixed earnings
inputs:
  employment: 55000
  business: 30000
steps:
  employee_cpp: (employment - 3500) * 0.0595
  remaining: min(business, 71300 - employment)
  base: remaining * 0.099
  first: remaining * 0.02
  second: min(max(0, employment + business - 71300), 9900) * 0.08
  payable: base + first + second
  deduction: base / 2 + first + second
expected:
  employee_cpp: 3064.25
  payable: 2731.70
  deduction: 1924.85
```

### Test 5 - Late filing, restored historical test

Original **$8,000 balance**, **three complete months late**, filing **September 30 instead of June 15**. For the 2025 return those filing dates are in **2026**. Assuming the $8,000 remained unpaid at filing due date and the ordinary (not repeated-failure) penalty applies, $8,000 × (5% + 3 × 1%) = **$640**. Interest on unpaid tax starts May 1, 2026; no interest amount is inferred from these inputs.

```oa-check
name: Original 2025 test 5 - ordinary late return
inputs:
  unpaid: 8000
  complete_months: 3
steps:
  penalty: unpaid * (0.05 + min(complete_months, 12) * 0.01)
expected:
  penalty: 640
```

### Historical edge cases EC1–EC10

- **EC1:** Employment pensionable earnings **$50,000**, CPP already withheld; self-employed profit unspecified. Use Schedule 8 Parts 3/5; no payable can be computed without the remaining inputs.
- **EC2:** Age **72** throughout 2025: no CPP contributory months (including CPP2). Under-18 and age-transition/election cases need the applicable months, not the full-year shortcut.
- **EC3:** Net income **$210,000**: BPA **$15,452.46**, ordinary BPA credit **$2,240.61**. Compute before rounding; the old $15,453/$2,241 figures were premature rounding.
- **EC4:** Business loss **−$15,000**, employment **$60,000**: assuming a genuine deductible business loss and no limitation, income subtotal **$45,000 before other deductions/adjustments**; no positive self-employed CPP base. Do not call that subtotal final net income without employee CPP and other deductions. Loss characterization, restricted losses and historical 3-year/20-year carryback/carryforward statement: Check this point with one of our partner accountants.
- **EC5:** No instalments, prior-year tax owing **$12,000**, current balance **$15,000**. These descriptions alone do not establish statutory net tax owing or CPP/EI instalment bases. Hold the old “four $3,000 payments plus interest” conclusion; reminders, dates and rates are missing. Check this point with one of our partner accountants.
- **EC6:** New EI opt-in followed by an immediate sickness claim: the 12-month agreement condition is not met. Other benefit/termination/refund outcomes are not decided. Check this point with one of our partner accountants.
- **EC7:** Quick Method GST/HST difference/benefit **$1,200**: preserve the input; do not automatically put it on the old line 8290 or add it again to an already adjusted T2125 result. Its reconciliation/income treatment is held. Check this point with one of our partner accountants.
- **EC8:** Maximum RRSP contribution question: use actual room and receipts and the 2025/2024 limit mechanics above. The old “business income minus employer-half CPP” earned-income shortcut is withdrawn. Check this point with one of our partner accountants.
- **EC9:** Pensionable business income **$78,000**, full-year CPP assumptions: CPP $8,068.20 + CPP2 $536 = **$8,604.20**; deduction **$5,248.10**, base credit amount **$3,356.10**. Do not split the total in half.
- **EC10:** Filed **September 30, 2026**, refund due, no tax unpaid when filing was due: the ordinary s162(1) late-return penalty is **$0**. Other filing obligations/penalties and refund-interest commencement are not inferred. Check this point with one of our partner accountants.

```oa-check
name: Original 2025 edges - BPA 210000 and CPP2 78000
inputs:
  income: 210000
  earnings: 78000
steps:
  bpa: round(16129 - 1591 * (income - 177882) / 75532, 2)
  bpa_credit: round(bpa * 0.145, 2)
  base: 67800 * 0.099
  first: 67800 * 0.02
  second: (earnings - 71300) * 0.08
  cpp: base + first + second
  deduction: base / 2 + first + second
expected:
  bpa: 15452.46
  bpa_credit: 2240.61
  second: 536
  cpp: 8604.20
  deduction: 5248.10
```

## When to refuse or refer

Retain these refusal identifiers:
- **R-CA-T1-1:** Non-resident or part-year resident return: Check this point with one of our partner accountants.
- **R-CA-T1-2:** Deceased or bankruptcy return: Check this point with one of our partner accountants.
- **R-CA-T1-3:** Trust income allocation: Check this point with one of our partner accountants.
- **R-CA-T1-4:** Provincial/territorial tax, surtaxes and credits: Check this point with one of our partner accountants.

## Working paper and reviewer brief

Record the source document and tax year next to each input. Keep total income, net income, taxable income, pre-credit federal tax, each credit, CPP deduction/credit/payable, EI and provincial computation separate. Use Step 6's actual credit list, including any refundable credits, before a filing balance. Required review flags: province/residence, CPP months/elections and T4 overlap, RRSP entitlement, BPA phase-out, other credits/top-up, instalments/interest and April 30 payment. Escalation brief: facts, missing evidence, affected result, proposed treatment and accountant decision. Label results estimated until professional review.

## Sources

Operative sources are linked beside each rule: 2025 T1/Worksheet/Schedule 8; ITA 3, 60(e), 117–118/118.7, 146, 150, 156/156.1 and 162; CPP Act 10/13; EI Act 152.07/152.21. Preserve T2125's [home-office restriction under ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html): the qualifying workspace deduction cannot create or increase that business's loss; eligibility and carryforward application require review. Check this point with one of our partner accountants.

Not yet confirmed: No unresolved proposition is offered as usable law. Specialist eligibility, carryovers, benefit and interest outcomes expressly held above require partner-accountant review.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner) before filing or acting upon.
