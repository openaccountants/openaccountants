---
name: ca-estimated-tax-540es
description: "California estimated income tax for individuals for tax year 2026 on Form 540-ES. Who must pay (expected tax of $500 or more, $250 married/RDP filing separately), the required annual payment (smaller of 90% of 2026 tax or 100% of 2025 tax, 110% if 2025 California AGI was over $150,000, and no prior-year route at 2026 California AGI of $1,000,000 or more), the uneven 30% / 40% / 0% / 30% installments due April 15, June 15, September 15 (nothing due) and January 15, 2027, early filing in place of the fourth installment, annualization, farmers and fishermen, mandatory e-pay, and the form FTB 5805 underpayment penalty and waivers. Trigger on \"California estimated tax\", \"540-ES\", \"CA quarterly payments\", \"California safe harbor\", \"FTB 5805\", \"California estimated payment due dates\". Federal estimates are in us-quarterly-estimated-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ca-estimated-tax-540es"
  jurisdiction: "US-CA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# California estimated tax for individuals (Form 540-ES), tax year 2026

> **Source-cited draft.** Built from the 2026 Instructions for Form 540-ES and the 2026 Form 540-ES payment forms, the 2025 form FTB 5805 instructions and R&TC 19136.3, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, pay California estimated tax if you expect to owe at least **$500** ($250 married/RDP filing separately) after withholding and credits. The required annual payment is the smaller of **90%** of the 2026 tax or **100%** of the 2025 tax (including AMT); use **110%** of the 2025 tax if 2025 California AGI was over **$150,000** ($75,000 separate), and the prior-year route is gone if 2026 California AGI is **$1,000,000** or more ($500,000 separate). Pay it unevenly: **30%** by April 15, 2026, **40%** by June 15, 2026, **nothing** for September 15, 2026, and **30%** by January 15, 2027.

## Scope and who this is for

In scope: individuals (residents, part-year residents and nonresidents) paying 2026 California personal income tax estimates on Form 540-ES, and the form FTB 5805 underpayment penalty on the 2026 return. Out of scope: fiduciaries (Form 541-ES), the LLC fee estimate on form FTB 3536 (`ca-llc-fee-and-tax`), pass-through entity elective tax prepayments (`ca-pte-elective-tax`), and federal estimates (`us-quarterly-estimated-tax`; the cross-state view is in `us-state-estimated-tax-safe-harbors-matrix`). The tax itself is figured with `ca-income-tax` and `ca-540-individual-return`.

## Ask the client first

1. **The 2025 California return**: total tax (Form 540 lines 48, 61 and 62), California AGI (line 17), and any 2025 overpayment applied to 2026. These set the prior-year route and the 110% test.
2. **Expected 2026 California AGI and tax**, and whether 2026 California AGI may reach $1,000,000 ($500,000 separate).
3. **California withholding for 2026** (W-2 box 17, pensions, Form 592-B or 593 withholding). Withholding counts as paid evenly on the due dates unless shown otherwise.
4. **Filing status for 2026** (the $250 and $75,000 and $500,000 separate-return figures).
5. **Uneven income in the year** (a large sale or a fourth-quarter contract): the annualization option.
6. **New to California in 2026, or farming or fishing income of two-thirds or more of gross income**: the exceptions.

## The method, step by step

1. **Estimate 2026 tax** on the 2026 California Estimated Tax Worksheet (line 1 AGI, line 2 deduction, line 4 tax, line 6a exemption credits, lines 11 to 17 credits, AMT and the Behavioral Health Services Tax). Line 18 is the 2026 estimated tax.
2. **Test whether estimates are required.** Required if the expected 2026 tax after withholding and credits is at least $500 ($250 separate) and withholding and credits will be less than the smaller of 90% of 2026 tax or 100% of 2025 tax. No estimates are needed by a nonresident or new resident of 2026 who had no California tax liability in 2025.
3. **Fix the required annual payment** (worksheet line 19):
   - line 19a: 90% of line 18;
   - line 19b: 2025 tax (2025 Form 540 lines 48 + 61 + 62);
   - if 2025 California AGI (line 19c) is not more than $150,000 ($75,000 separate), take the smaller of 19a and 19b;
   - if it is more, take the smaller of 19a and 110% of 19b;
   - if 2026 California AGI is $1,000,000 or more ($500,000 separate), use 19a.
4. **Subtract expected withholding** (line 20) to get line 21. If line 21 is under $500 ($250 separate), no payment is needed now.
5. **Split into installments** (line 22): 30% of line 21 for the first and fourth payments, 40% for the second, nothing for the third.
6. **Pay**: Web Pay at ftb.ca.gov/pay (can be scheduled up to a year ahead), electronic funds withdrawal through software, credit card (fee), or check with the dated Form 540-ES payment form to Franchise Tax Board, PO Box 942867, Sacramento CA 94267-0008. Write the SSN or ITIN and "2026 Form 540-ES" on the check.
7. **On the 2026 return**, test the payments on form FTB 5805 and report any penalty on Form 540 line 113.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Estimates required | Expected tax of at least $500 ($250 married/RDP filing separately) after withholding and credits | And withholding and credits below the smaller of 90% of 2026 tax or 100% of 2025 tax | [2026 Form 540-ES instructions, section B](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Current-year route | 90% of the 2026 tax | Farmers and fishermen 66 2/3% | same, worksheet line 19a |
| Prior-year route | 100% of the 2025 tax including AMT | 2025 California AGI not more than $150,000 ($75,000 separate) | same, section C |
| Prior-year route, higher income | 110% of the 2025 tax | 2025 California AGI more than $150,000 ($75,000 separate); not farmers or fishermen | same, section C |
| No prior-year route | Estimate must be based on 2026 tax | 2026 California AGI equal to or greater than $1,000,000 ($500,000 separate) | same, section C; [R&TC 19136.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.3) |
| First installment | 30% of the required annual payment, by April 15, 2026 | Calendar-year filers | [2026 Form 540-ES instructions, sections D and General Information](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Second installment | 40%, by June 15, 2026 | same | same |
| Third installment | No installment due (September 15, 2026) | same | same |
| Fourth installment | 30%, by January 15, 2027 | Not needed if the 2026 return is filed by January 31, 2027 and the balance paid | same |
| Fiscal year filers | 15th day of the 4th, 6th and 9th months and the 1st month of the next fiscal year | Weekend or holiday moves to the next business day | same |
| Mandatory e-pay | All payments electronic once an estimate or extension payment exceeds $20,000 or an original return shows total tax over $80,000 | 1% noncompliance penalty otherwise | same |
| Penalty rate, 2025 computation period | 8% from April 15, 2025 to June 30, 2025; 7% from July 1, 2025 to April 15, 2026 | FTB 5805; the 2026 period rates are set by the FTB each half year | [2025 FTB 5805 instructions](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |
| No penalty | Prior-year tax less credits under $500 ($250 separate) | FTB 5805 | same |

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| 2025 California AGI exactly $150,000 | Not "more than" $150,000: the 100% prior-year route applies | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| 2026 California AGI exactly $1,000,000 | "Equal to or greater than": no prior-year route | same |
| Client pays four equal quarters, copying the federal pattern | Q1 and Q2 are short of 30% and 40% (25% and 50% cumulative against 30% and 70%), so a penalty can run on Q2 even though the year's total is right | same, section D |
| New California resident in 2026 with no 2025 California liability | No estimates required | same, section B |
| Two-thirds or more of 2025 or 2026 gross income from farming or fishing | Pay all estimated tax by January 15, 2027, or file and pay in full by March 1, 2027 (form FTB 5805F) | same, section D |
| Income arrives mostly late in the year | Annualize on form FTB 5805 (sides 3 and 4) and tick Form 540 line 113 | [2025 FTB 5805 instructions](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |
| Withholding covers most of the tax | Withholding is treated as paid evenly on the due dates; an uneven-withholding election is made on FTB 5805 Part I question 3 | same |
| Overpaid Q1 and Q2 | The excess carries to later installments; nothing is due for Q3 in any case | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Joint estimates, then separate returns | Either spouse may claim all, or the FTB divides them on a written request (notarized or under a divorce agreement) sent before filing | same, section B |
| Nonresident military servicemember | Leave military pay out of the estimate (FTB Pub. 1032) | same |
| Federally declared disaster | The FTB may postpone due dates; check the FTB postponement notice for the county before charging a penalty | same (booklet reference) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| 2025 California AGI unknown | Assume over $150,000 and use 110% until the 2025 return is seen |
| 2026 AGI could reach $1,000,000 | Use 90% of 2026 tax; do not rely on the prior-year route |
| Withholding timing unknown | Treat as paid evenly on the four due dates |

## Worked cases

### Case 1: ordinary installments (computation)

A single client's 2025 California tax was $8,000 on California AGI of $140,000. Expected 2026 tax is $12,000 and expected 2026 withholding is $1,000. 90% of 2026 tax is $10,800; the prior-year figure is $8,000 at 100% (AGI not over $150,000). The required annual payment is $8,000, less $1,000 withholding: $7,000 to pay. Installments: $2,100 by April 15, 2026, $2,800 by June 15, 2026, nothing in September, $2,100 by January 15, 2027.

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

### Case 2: which route is open to a higher earner (decision)

A single client's 2025 California tax was $30,000 on California AGI of $300,000, so the prior-year route needs 110%: $33,000. Expected 2026 tax is $45,000, so 90% is $40,500. If 2026 California AGI stays under $1,000,000 the client pays the smaller amount, $33,000. If a 2026 sale lifts California AGI to $1,200,000, the prior-year route is closed and the client must pay $40,500: $7,500 more, of which 30% and 40% should already be in by June 15.

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

## When to refuse or refer

- Refer a request for a penalty waiver on casualty, disaster or unusual-circumstance grounds, or for a client who retired after age 62 or became disabled in 2025 or 2026 with reasonable cause: the waiver is requested on FTB 5805 Part I and is the FTB's decision.
- Refer fiduciary estimates (Form 541-ES) and part-year or nonresident estimates that need Schedule CA (540NR) source figures beyond the worksheet lines.
- Refer an annualized computation with large capital gains or pass-through income where the timing of income is disputed.
- Do not apply the federal four-equal-payments pattern to California.

## Filing and payment

| Step | When | Source |
| --- | --- | --- |
| First 2026 payment (30%) | April 15, 2026 | [2026 Form 540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es.pdf) |
| Second 2026 payment (40%) | June 15, 2026 | same |
| Third 2026 payment (none required) | September 15, 2026 | same |
| Fourth 2026 payment (30%) | January 15, 2027, or file and pay in full by January 31, 2027 | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Check estimated payments received | MyFTB at ftb.ca.gov | same |
| Underpayment penalty | Form FTB 5805 with the 2026 return, Form 540 line 113; or the FTB bills it, payable within 15 days | [2025 FTB 5805 instructions](https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html) |
| A 2025 balance due | Not on Form 540-ES: use form FTB 3519 | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |

## Completion checklist

- [ ] 2025 tax (lines 48 + 61 + 62) and 2025 California AGI taken from the filed 2025 return.
- [ ] $150,000 test (110%) and $1,000,000 test (no prior-year route) applied with the right filing-status figures.
- [ ] Withholding and any 2025 overpayment applied deducted.
- [ ] Installments set at 30%, 40%, nothing, 30%, not four equal parts.
- [ ] Payment method chosen; e-pay rule checked ($20,000 payment, $80,000 return).
- [ ] Federal estimates kept separate (`us-quarterly-estimated-tax`).
- [ ] FTB 5805 run on the 2026 return; annualization or waiver documented if used.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 Instructions for Form 540-ES (FTB). Read for General Information (30/40/0/30, mandatory e-pay), sections B, C, D (dates, early filing, annualization, farmers, fiscal year), F, G and the worksheet lines 1 to 22. | https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf | 2026-11-13 |
| 2026 Form 540-ES payment forms. Read for the dates printed on forms 1 to 4 and the mailing address. | https://www.ftb.ca.gov/forms/2026/2026-540-es.pdf | 2026-11-13 |
| 2025 Instructions for form FTB 5805. Read for the waiver (section C), annualization (section D), the 2025 penalty rates (8% and 7%), the under-$500 prior-year rule and withholding timing. | https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html | 2026-11-13 |
| R&TC 19136.3 (California Legislative Information, through Firecrawl). Read for (a), no prior-year clause at AGI of $1 million ($500,000 separate). | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.3 | 2026-11-13 |

Not yet confirmed: the 2026 form FTB 5805 and its penalty rates for the 2026 computation period (the 2025 instructions say the FTB sets the July to December 2026 and January to June 2027 rates in March and September 2026; the FTB interest rate page did not return the figures when read); the R&TC sections behind the 30/40/0/30 split and the $150,000 rule were not opened, and the FTB instructions are cited instead.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ca-estimated-tax-540es` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ca-estimated-tax-540es. If neither is available, confirm every figure against the official source pages cited above before relying on it.
