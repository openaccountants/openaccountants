---
name: ca-estimated-tax-540es
description: >-
  California individual estimated income tax for tax year 2026, Form 540-ES: payment requirement, 90% current-year and 100%/110% prior-year routes, the current-year high-income restriction, 30%/40%/0%/30% installments, withholding and overpayment credits, payment methods, annualization, farmers and fishermen, and FTB 5805 penalty analysis. Preserves the historical 2025 cases separately. Trigger on "California estimated tax", "540-ES", "CA quarterly payments", "California safe harbor", "FTB 5805" and "California estimated payment due dates". Federal estimates use us-quarterly-estimated-tax.
version: "1.1"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# California estimated tax for individuals (Form 540-ES), tax year 2026

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer first.** For ordinary calendar-year individuals, test the **$500** expected balance (**$250** married/RDP filing separately) after withholding and credits, then compute the applicable **90% current-year / 100% or 110% prior-year** amount. California uses **30% / 40% / 0% / 30%**, with 2026 payments due **April 15, June 15, September 15 (no regular installment), and January 15, 2027**. Check the exceptions below before using the prior-year route. [FTB 2026 instructions, General Information and B–D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).

## Scope

Compute California individual estimated payments from an already established California tax figure, including sole proprietors and owners of disregarded single-member LLCs. Residents, part-year residents and nonresidents use the applicable worksheet; source-income computations outside the established inputs remain held below. For taxable years beginning on or after January 1, 2026, R&TC 19136 does not apply to a nonresident electing a group return under section 18537: do not run that election through this ordinary individual schedule. [R&TC 19136(f), (j)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.).

Load `us-tax-workflow-base` for the wider job. Obtain tax inputs from `ca-income-tax` / `ca-540-individual-return`; send the payment schedule, receipts and any unresolved penalty computation to `us-ca-return-assembly`. Federal estimates belong to `us-quarterly-estimated-tax`, and the cross-state comparison to `us-state-estimated-tax-safe-harbors-matrix`. Fiduciary estimates (541-ES), corporate estimates (100-ES), LLC annual tax and fee (3522 / 3536; `ca-smllc-form-568` / `ca-llc-fee-and-tax`), and PTE elective payments (`ca-pte-elective-tax`) require their own work. These references define routing, not conclusions about those taxes.

Current operative guidance below is for **2026**. The separately labelled **2025 historical cases** retain their original years and inputs; never turn those amounts into 2026 tax rates or liability figures.

## Ask the client first

Collect the filed 2025 return and its period, California AGI and tax, filing status, any overpayment elected forward, expected 2026 AGI and tax, and California withholding (wages, pensions and any supported 592-B/593 credits). Obtain dated estimate receipts, actual withholding dates if using them, and the income dates for annualization. Ask about residency changes, group-return elections, farming/fishing gross income, military domicile, disaster relief, retirement/disability and joint payments later claimed separately. These are required inputs; an unknown prior-year AGI is **not** an assumed 110% figure.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure and operative conditions | Official source |
| --- | --- | --- |
| General payment test | Expected 2026 tax after withholding and credits is at least $500 ($250 married/RDP filing separately), and withholding/credits are below the applicable smaller percentage amount; higher-income and farmer rules modify that amount | [2026 540-ES B–C](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Current-year route | 90% of 2026 tax; qualifying farmers/fishermen use 66 2/3% instead | [2026 worksheet 19a](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Ordinary prior-year route | 100% of 2025 tax including AMT; filed return must cover a full 12 months; check the independent no-liability exception first | [2026 540-ES B](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [IRC 6654(d)(1)(B), incorporated by R&TC 19136(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Higher prior-year AGI | Substitute 110% if 2025 California AGI is more than $150,000 ($75,000 married/RDP filing separately); this uplift does not apply to farmers/fishermen | [2026 540-ES C](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Current-year high income | At 2026 California AGI equal to or greater than $1,000,000 ($500,000 married/RDP filing separately), the prior-year percentage route is unavailable; use the current-year route, subject to the independent no-penalty exceptions | [R&TC 19136.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.3); [2026 540-ES C](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Small tax / prior-year protection | No estimated-tax addition if the preceding year's relevant tax less credits, or the estimated current-year relevant tax less credits, is less than $500 ($250 separate). This is not permission to subtract estimated payments from the tax test | [R&TC 19136(c)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.); [2025 FTB 5805, Important box, historical application](https://www.ftb.ca.gov/forms/2025/2025-5805.pdf) |
| Mandatory electronic payment | Triggered by an estimate/extension payment exceeding $20,000 or an original return showing total liability over $80,000; subsequent payments of any amount/type/year must be electronic. The triggering first payment need not be electronic | [2026 540-ES General Information](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Electronic-payment noncompliance | 1% penalty for individuals required to e-pay who do not do so | [2026 540-ES General Information](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| 2026 estimate-penalty rate | 7% for January–June and July–December 2026; apply only to days the installment is unpaid | [FTB rate table](https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html) |
| Following rate period | 7% for January 1–June 30, 2027; no assumption that an old rate continues | [FTB September 2026, Adjusted Interest Rates](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/09.html) |
| Historical 2025 penalty only | 8% April 15–June 30, 2025; 7% July 1, 2025–April 15, 2026 | [2025 FTB 5805 K](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |

### Computation and credits

1. **Establish 2026 tax.** Complete the 2026 California Estimated Tax Worksheet, lines 1–18. Residents begin with California AGI; nonresidents/part-year residents begin with total AGI from all sources and use the source-income/proration steps at lines 5–8. Line 18 adds lines 14–17, not less than zero: include deferred-installment interest, AMT and Behavioral Health Services Tax. Section D's latter tax worksheet applies 1% to taxable income (California-source taxable income for nonresidents) above $1,000,000. Tax preparation itself belongs to the income-tax Guides. The planning worksheet refers to the 2025 tax table; it is not a final 2026 return tax table. [2026 worksheet, lines 1–18 and D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).
2. **Check independent exceptions.** A nonresident or new resident in 2026 who had no California tax liability in 2025 need not make estimates. Do not infer “no liability” merely from “no return filed.” Apply the small-tax protection above before treating a high-AGI taxpayer as penalized. [2026 540-ES B](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [R&TC 19136(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.).
3. **Compute the annual amount at line 19.** Line 19a is 90% of line 18 (farmer exception above). For ordinary filers, line 19b uses 2025 Form 540 lines 48 + 61 + 62, or 540NR lines 63 + 71 + 72; line 19c uses 2025 Form 540 line 17 or 540NR line 32. Use the smaller eligible current/prior amount, applying the AGI rules above. No filed full-year prior return means no ordinary prior-year route. For a penalty computation, do not blindly reuse these three-line planning sums: the 2025 FTB 5805 instructions add any IRC 453A interest and exclude lump-sum/accumulation-distribution tax. A 2026 return-specific reconciliation is held pending final instructions below. [2026 worksheet 19a–f](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [2025 FTB 5805, Part II lines 1 and 5](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
4. **Deduct withholding and credit forward.** Line 20 is expected California withholding, including pensions/annuities; line 21 subtracts it from the annual amount. Reduce the balance by a 2025 overpayment elected toward 2026, without counting it twice. The worksheet says no payment is needed at this time if line 21 is below $500 ($250 separate); that planning instruction is not an independent blanket exemption from the final underpayment test. Record the credit's application and reconcile dated payments at penalty time. [2026 worksheet 20–21 and E](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).
5. **Allocate ordinary installments.** Line 22 applies 30% / 40% / 0% / 30% to the remaining worksheet balance. For penalty analysis, California also allocates annual withholding in those proportions by default, **not four equal parts**: R&TC 19136(e)(2) replaces “an equal part” in IRC 6654(g)(1) with the applicable installment percentage. If actual withholding dates/amounts are established, use them; the historical 2025 procedure is FTB 5805 Part I question 3. An early overpayment carries to later installments; later payments first clear the oldest unpaid installment and cannot erase the penalty already accrued. [2026 worksheet 22](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [R&TC 19136(e)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.); [2025 FTB 5805 Worksheet II](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
6. **Pay and retain evidence.** Use [FTB Web Pay](https://www.ftb.ca.gov/pay/) (schedule up to one year ahead), supported software EFW, or credit card with a fee. Do not mail 540-ES with those electronic payments. If paper payment is permitted, use the payment form for the correct date; put name/address/SSN or ITIN and amount on it, and SSN/ITIN plus “2026 Form 540-ES” on a U.S.-dollar check drawn on a U.S. financial institution, payable to Franchise Tax Board. Mail with the form to Franchise Tax Board, PO Box 942867, Sacramento, CA 94267-0008. Retain dates, confirmation numbers and credit amounts; check receipts in MyFTB. A 2025 balance is not a 2026 estimate: use FTB 3519 as directed in section A. [2026 540-ES A, E–F and payment record](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).
7. **Test underpayment separately.** Compare each required installment with amounts timely credited, applying the oldest-first rule. For each unpaid portion, compute the applicable annual rate × unpaid amount × days unpaid / 365 for these non-leap years, stopping at payment or the ordinary return due date, whichever comes first. Split at rate changes; this estimate-penalty computation does not compound daily merely because ordinary tax-interest news describes compounded interest. The 2025 regular method is Worksheet II of FTB 5805. Current-year return-box and final form computations remain held below. [R&TC 19136(a)–(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.); [IRC 6654(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm); [2025 FTB 5805 Worksheet II](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).

### Filing calendar and alternatives

| Installment / alternative | When and amount | Official source |
| --- | --- | --- |
| First 2026 installment | April 15, 2026: 30% | [2026 540-ES General Information, D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Second | June 15, 2026: 40% | [2026 540-ES General Information, D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Third | September 15, 2026: 0% regular installment; a payment can still cure earlier shortages | [2026 540-ES General Information, D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [2025 FTB 5805 Payment Application](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |
| Fourth | January 15, 2027: 30% | [2026 540-ES General Information, D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Early return instead of fourth payment | File the 2026 return and pay its entire balance by January 31, 2027 as printed in the instructions; that Sunday rolls to February 1, 2027 under the holiday rule. This removes only the fourth-installment penalty | [2026 540-ES D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [Government Code 6700(a)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=6700); [6706](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=6706) |
| Fiscal-year schedule | Fifteenth day of months 4, 6, 9 and month 1 of the following fiscal year; next business day for weekend/legal holiday. The ordinary third installment remains zero | [2026 540-ES D and General Information](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Qualifying farmers/fishermen | At least two-thirds of 2025 or 2026 gross income from farming/fishing: pay all estimated tax by January 15, 2027, or file/pay total 2026 tax by March 1, 2027 | [2026 540-ES D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |

**Annualization.** For uneven income, section D permits the annualization schedule in the **2025** FTB 5805 for planning 2026 payments; do not relabel the historical form as a final 2026 filing form. It uses cumulative January–March, January–May, January–August and January–December income, including the relevant partnership/S-corporation items. Use the method for all payment dates once selected. It compares the annualized amount with the regular installment plus recapture of earlier reductions; California's statutory cumulative annualized percentages are 27% / 63% / 63% / 90%, not federal percentages. A zero regular third installment does not justify deleting the annualization column. A disputed-timing or final 2026 annualized computation is a non-usable hold below. [2026 540-ES D](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html); [2025 FTB 5805 Part III](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html); [R&TC 19136.1(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.1).

**Farmers/fishermen.** Use the smaller eligible 66 2/3% current-year or 100% prior-year amount; the 110% uplift does not apply. The current-year $1,000,000/$500,000 restriction still removes the prior-year route, so test it separately. Use the farmer-specific 5805F process, not the ordinary installment calculation. [IRC 6654(i), as incorporated by R&TC 19136](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm); [2026 540-ES C–D and worksheet 19a](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).

## Boundary and exception table

| Boundary | Treatment | Official source |
| --- | --- | --- |
| 2025 California AGI exactly $150,000 ($75,000 separate) | Not “more than”; ordinary prior-year percentage remains 100%, if otherwise eligible | [2026 540-ES C](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| 2026 California AGI exactly $1,000,000 ($500,000 separate) | Prior-year percentage route unavailable; independent small-tax/no-liability protection is still tested | [R&TC 19136.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.3); [19136(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.) |
| Joint estimates followed by separate returns | Either spouse/RDP may claim all or each may claim part. Notify FTB before filing for division: provide the written divorce agreement/court settlement or allocation statement with both notarized signatures, following section B | [2026 540-ES B](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Military servicemember not domiciled in California | Exclude military pay from the estimate. Do not extend that automatically to the nonmilitary spouse's pay; refer the spouse/domicile determination below | [2026 540-ES B](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Backup withholding already suffered | Include supported California withholding credits; the 7% backup rate applies to statutory reportable payments, not every 1099. Interest/dividends and ordinary financial-institution loan-fund releases are excluded from that backup rule | [R&TC 18664(a)–(c)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18664); [2025 FTB 5805 Part II line 3 and Worksheet II](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |

**Law-change protection.** R&TC 19136(g)(1)(A) prevents the estimated-tax addition to the extent an underpayment was created or increased by a law chaptered during and operative for that same taxable year. Determine the affected amount rather than treating every shortage as penalized. [R&TC 19136(g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.).

**Missing inputs.** Never invent the prior AGI, filed-return period, current AGI, tax or credit amount. Produce conditional schedules only, explicitly labelled with their assumptions. For unproved withholding timing, use the statutory installment allocation; use actual dates only with evidence. If a possible current-year high-income threshold cannot be resolved, do not present the prior-year route as a confirmed payment obligation.

## Worked cases

### Case 1: ordinary installments, 2026

Original inputs: single; 2025 tax $8,000, California AGI $140,000; expected 2026 tax $12,000; expected withholding $1,000. Assume a filed full-year 2025 return, no credit forward, no exception or actual-date withholding election. Current route = $10,800; prior route = $8,000; annual amount = $8,000; less withholding gives $7,000. Pay $2,100 / $2,800 / $0 / $2,100 on the four dates above. [2026 worksheet 19–22](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).

```oa-check
name: CA 2026 540-ES installments, prior-year route at 100%
inputs:
  tax_2025: 8000
  tax_2026: 12000
  withholding: 1000
steps:
  - current: tax_2026 * 0.9
  - prior: tax_2025 * 1
  - required: min(current, prior)
  - balance: required - withholding
  - q1: balance * 0.3
  - q2: balance * 0.4
  - q3: balance * 0
  - q4: balance * 0.3
expected:
  required: 8000
  balance: 7000
  q1: 2100
  q2: 2800
  q3: 0
  q4: 2100
```

### Case 2: higher-earner decision, 2026

Original inputs: single; 2025 tax $30,000 on California AGI $300,000; expected 2026 tax $45,000. Assume eligible full-year prior return, no withholding/credit forward and no independent exception. Prior route = $33,000; current route = $40,500. Below $1,000,000 current AGI, use $33,000. At the original alternative $1,200,000 current AGI, use $40,500, an increase of $7,500. Under the regular method, cumulative payment by June 15 is $28,350 rather than $23,100: $5,250 extra. A late sale does not automatically excuse an earlier shortage; assess annualization on the actual income dates. [2026 540-ES C, worksheet 19–22](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html).

```oa-check
name: CA 2026 required annual payment, 110% route against the $1,000,000 rule
inputs:
  tax_2025: 30000
  tax_2026: 45000
steps:
  - current: tax_2026 * 0.9
  - prior_110: tax_2025 * 1.1
  - required_low: min(current, prior_110)
  - required_high: current
  - extra: required_high - required_low
  - by_june_extra: extra * 0.7
expected:
  current: 40500
  prior_110: 33000
  required_low: 33000
  required_high: 40500
  extra: 7500
  by_june_extra: 5250
```

### Historical 2025 cases: original inputs retained

These are regression examples for the earlier 2025 Guide, not current-year figures. Unless the case says otherwise, ordinary percentage examples assume a filed full-year 2024 return, prior California AGI within the ordinary threshold, current AGI below the current-year restriction, no withholding or credit forward and no independent exception. The 2025 ordinary due dates are April 15, **June 16** (June 15 was Sunday), September 15 and January 15, 2026. [2025 540-ES B–D](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).

- **Original §6.3, basic computation:** 2024 tax $10,000; expected 2025 tax $12,000. Smaller of $10,800 and $10,000 is $10,000; installments $3,000 / $4,000 / $0 / $3,000. [2025 worksheet 19–22](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **EC-ES-1, equal quarters:** required annual $20,000; paid $5,000 April 15, $5,000 June 16, $5,000 September 15 and $5,000 January 15, 2026. Required $6,000 / $8,000 / $0 / $6,000. April shortage $1,000 is cured by the June payment; only $4,000 of June's payment then meets June's installment, leaving $4,000 unpaid until September. September cures it and leaves $1,000 for January; January is fully covered. The earliest historical version specified **June 15** payment: preserve that alternative as an early payment which cures April one day sooner; June's due date is still June 16. Do not retain the old false January-shortage conclusion or charge the April shortage until September. [2025 FTB 5805, Payment Application](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
- **EC-ES-2, new resident:** moved January 1, 2025; no 2024 return and, as the case stipulates, no 2024 California tax; expected 2025 tax $15,000. No estimates required under the new-resident exception; the liability remains payable with the 2025 return. “No return” alone would not establish the exception. [2025 540-ES B](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **EC-ES-3, late income:** $30,000 earned in Q1–Q3, $120,000 contract received in November; 2025 tax $18,000; prior tax $5,000. Under the stated ordinary assumptions, smaller of $16,200 and $5,000 is $5,000. Timely $1,500 / $2,000 / $0 / $1,500 satisfies that route; balance $13,000 due April 15, 2026. Annualization is an alternative requiring the actual cumulative income/credit data, not a result inferred from the November receipt alone. [2025 540-ES C–D](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html); [R&TC 18566](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18566).
- **EC-ES-4, wages plus side business:** 2025 tax $15,000; annual California withholding $12,000; prior tax unspecified. If the $13,500 current route controls, default withholding is $3,600 / $4,800 / $0 / $3,600 and estimates are $450 / $600 / $0 / $450. A lower eligible prior route can reduce them; if withholding covers that route, no estimates. Four equal $3,000 withholding credits were wrong. [2025 FTB 5805 Worksheet II](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
- **EC-ES-5, farmer:** 70% gross income from farming; 2025 tax $8,000; prior tax not supplied. Meets the gross-income test, assuming the 70% refers to 2024 or 2025. Pay the eligible required amount by January 15, 2026, or file/full-pay by **March 2, 2026** (March 1 was Sunday). The current-route fraction is 66 2/3%, not 100% of the $8,000 liability; the smaller eligible prior-year amount still needs its missing input. [2025 540-ES D](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html); [IRC 6654(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).
- **EC-ES-6, disaster:** home in a Governor-declared county, FTB announces extensions; the original example suggested April 15 moving to October 15 without a named notice or year. **Non-usable hold:** neither that date nor a penalty waiver is established for this taxpayer. Check this point with one of our partner accountants.
- **EC-ES-7, early overpayment:** required annual $10,000; paid $5,000 April 15 and $5,000 June 16; none September/January. Required $3,000 / $4,000 / $0 / $3,000; carry $2,000 after April, $3,000 after June, covering January. No installment shortage. The earliest historical June **15** payment variant also satisfies the June 16 due date. [2025 FTB 5805 Worksheet II lines 3–9](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
- **EC-ES-8, separate spouses:** A's tax $20,000, B's $3,000. Test each spouse under the separate-return rules; B's expected balance threshold is $250, not $500. Prior tax, AGI, withholding and allocation facts are absent, so neither spouse's dollar schedule is determined. **Non-usable hold** for those missing facts and joint-credit allocation: Check this point with one of our partner accountants. [2025 540-ES B–C](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **ES-1:** prior tax $8,000; 2025 tax $10,000; no withholding. Smaller of $9,000 and $8,000 is $8,000; $2,400 / $3,200 / $0 / $2,400. [2025 worksheet 19–22](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **ES-2, equal-quarter test:** annual $12,000; $3,000 each April 15, June 16, September 15 and January 15, 2026. Required $3,600 / $4,800 / $0 / $3,600. April shortage $600 cured in June; June then short $2,400, cured in September; carry $600 covers January with its $3,000 payment. Original June **15** variant cures April one day earlier. No January shortage. [2025 FTB 5805, Payment Application](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
- **ES-3:** 2025 tax $16,000; prior tax $14,000; W-2 withholding $14,000. Annual amount $14,000 versus $14,400 current. Default withholding $4,200 / $5,600 / $0 / $4,200 covers it exactly: no estimates, correcting the old equal-withholding result. [2025 FTB 5805 Worksheet II](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).
- **ES-4:** new California resident, no 2024 California tax, 2025 tax $20,000, no withholding. No estimates required under the new-resident exception, rather than the old $18,000 estimated schedule. The $20,000 liability remains. [2025 540-ES B](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **ES-5:** prior tax $6,000, 2025 tax $25,000; paid $1,800 / $2,400 / $0 / $1,800. Smaller of $22,500 and $6,000 is $6,000; timely payments satisfy the route; $19,000 remains payable with the return. [2025 540-ES B–D](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).
- **ES-6, separate agencies:** original stipulated federal annual payment $16,000 and California annual $10,000. Given the original federal $4,000 installments (to be confirmed in the federal Guide), California is $3,000 / $4,000 / $0 / $3,000. The action-list totals are $7,000 / $8,000 / $4,000 / $7,000 on April 15, June 16, September 15, 2025 and January 15, 2026, **paid separately** to IRS and FTB. The earliest historical calendar showed June 15 instead: an early Sunday payment remains timely for the June 16 due date. These totals are not instructions to remit one combined payment. [2025 540-ES General Information, D–F](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html).

## When to refuse or refer

Each item below is a **non-usable hold** for the indicated determination, not a numerical default:

- Disaster postponement or relief: county, event, affected taxpayer and operative FTB notice must be established. A declaration alone does not prove a particular extended date. Check this point with one of our partner accountants.
- Penalty waiver: casualty/disaster/unusual circumstances require the equity-and-good-conscience test; retirement after age 62 or disability in the current/preceding year requires reasonable cause and no willful neglect. Eligibility is not automatic approval; a 2026 waiver application and final return-box instructions are held. Check this point with one of our partner accountants. [IRC 6654(e)(3), incorporated by R&TC 19136](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).
- Final 2026 FTB 5805/5805F filing, line numbers, final annualization and special IRC 453A/lump-sum/trust tax reconciliation: final instructions were not established by this source read. The draft-form catalogue warns against reliance on drafts. Do not copy 2025 Form 540 line 113, 540NR line 123 or FTB 5805 Part I/II boxes into a claimed final 2026 filing instruction. Check this point with one of our partner accountants. [FTB draft-form warning](https://www.ftb.ca.gov/forms/draft-tax-forms.html).
- Part-year/nonresident source-income inputs beyond the established worksheet, a nonresident group-return election, military spouse/domicile, fiduciary work and disputed large-gain/pass-through timing require the appropriate specialist facts and forms. Check this point with one of our partner accountants.

For **historical 2025** FTB 5805, FTB ordinarily bills the penalty; pay within 15 days to avoid additional interest. A “Yes” answer in Part I requires completing/attaching the form. Annualization requires sides 3–4 and the return box (540 line 113 / 540NR line 123); a waiver requires Part I question 1, the computation without waiver, the requested amount and supporting explanation. These are historical instructions, not confirmation of 2026 boxes. [2025 FTB 5805 B–D](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html).

## Completion checklist

- [ ] Establish tax, credits, filing status, return period and residency; resolve independent exceptions before the ordinary percentage routes.
- [ ] Apply California AGI boundaries, withholding and credit-forward without double counting.
- [ ] Produce the dated California schedule and separate federal payment list; retain receipts and MyFTB reconciliation.
- [ ] Test each installment, actual-date withholding if supported, oldest-first payment application, annualization and any relief hold.
- [ ] Give `us-ca-return-assembly` the schedule, receipts, assumptions and explicit holds; never mark an unresolved filing/waiver determination complete.

**Circular 230 §10.37.** This general reference does not determine a taxpayer's facts, filing position or waiver eligibility; a practitioner must assess the applicable law and facts before using it as written tax advice.

## Sources

| Official source | What was actually read | Read on |
| --- | --- | --- |
| [2026 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) | General Information; A–G; worksheet 1–22 and payment record, including the planning-year references | 2026-11-27 |
| [2026 540-ES vouchers](https://www.ftb.ca.gov/forms/2026/2026-540-es.pdf) | Forms 1–4: printed taxable year, payment dates, separate balance/payment instructions and mailing address | 2026-11-27 |
| [2025 540-ES instructions](https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.html) | B–G and worksheet 19–22, solely for retained 2025 case outcomes and actual weekend-adjusted dates | 2026-11-27 |
| [2025 FTB 5805 instructions](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) | General Information B–K; Part II lines 1, 3, 5; Part III cumulative periods and recapture; Worksheet II credit allocation, oldest-first rule and daily penalty formula | 2026-11-27 |
| [2025 FTB 5805](https://www.ftb.ca.gov/forms/2025/2025-5805.pdf) | Side 1 Important box/Part I, Side 2 required annual amount and withholding; historical form only | 2026-11-27 |
| [R&TC 19136](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.) | Entire section (a)–(j), especially incorporation, small-tax exception, withholding substitution and effective-2026 group-return exclusion; read in browser | 2026-11-27 |
| [R&TC 19136.1](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.1) | Entire section; post-2010 installment and annualization percentages; read in browser | 2026-11-27 |
| [R&TC 19136.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.3) | Entire section; current-year AGI restriction and operative date; read in browser | 2026-11-27 |
| [IRC 6654](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) | (b), (d)–(i): prior return period, high income, annualization/recapture, waivers, withholding, early return and farmers; application checked against California's overriding modifications | 2026-11-27 |
| [FTB rate table](https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html) | Estimate-penalty current and previous periods through December 2026 | 2026-11-27 |
| [FTB September 2026 Tax News](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/2026/09.html) | Adjusted Interest Rates for January–June 2027, linked to estimate-penalty rates | 2026-11-27 |
| [R&TC 18566](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18566) | Calendar/fiscal return due dates; read in browser | 2026-11-27 |
| [R&TC 18664](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18664) | Entire section: backup reportable payments, exclusions, rate, coordination; read in browser | 2026-11-27 |
| [Government Code 6700](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=6700) and [6706](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=6706) | Sunday as holiday and next-business-day performance; whole sections read in browser | 2026-11-27 |
| [FTB draft forms](https://www.ftb.ca.gov/forms/draft-tax-forms.html) | Warning against reliance and catalogue entries for the 2026 underpayment forms; no draft instructions relied upon | 2026-11-27 |

Not yet confirmed: final 2026 underpayment-form instructions and return boxes, taxpayer-specific disaster notices/waivers, disputed annualization, nonresident/source-income and military-spouse determinations, and missing inputs in the historical spouse/farmer cases. These remain the explicit non-usable holds above: Check this point with one of our partner accountants.
