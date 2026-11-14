---
name: us-federal-return-assembly
description: "Router for assembling a US freelancer's 2026 federal Form 1040 package (sole proprietor or single-member LLC on Schedule C). Sets which skills to load and in what order (bookkeeping, Schedule C and SE tax, retirement, self-employed health insurance, premium tax credit, Schedule 1-A, QBI, tax and credits, estimated tax and Form 2210), why retirement must come before the health insurance limit, the tie-out checks between Schedule C, Schedule SE, Schedules 1, 1-A, 2 and 3, Forms 7206, 8995 and 8962, and the reviewer package. Carries no rates of its own; every figure lives in the skill it routes to. Trigger on \"prepare my federal return\", \"put the 1040 together\", \"freelancer tax return\", \"what order do I do the schedules\", \"return package for review\". Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-federal-return-assembly"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US federal return assembly for a Schedule C freelancer, tax year 2026

> **Source-cited draft.** Built from the 2026 Schedule C, Form 7206, Schedule 1 and Form 1040 as printed for 2025, IRS Publication 560 and IRS Publication 974, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Do the return in this order: books, then Schedule C, then Schedule SE, then the retirement deduction, then the self-employed health insurance deduction (its limit needs the retirement figure), then the premium tax credit if there was Marketplace cover, then the rest of Schedule 1 and AGI, then the standard or itemized deduction, Schedule 1-A, the QBI deduction, the tax, Schedule 2 and credits, payments and the estimated tax penalty. Then run the tie-outs below. Every figure comes from the skill named at that step.

## Scope and who this is for

For whoever prepares or reviews a 2026 Form 1040 for a US freelancer: a sole proprietor, or a single-member LLC disregarded for federal tax that reports on Schedule C, with or without wages, investment income or a spouse's income. The 2026 return is due 15 April 2027.

Out of scope: S corporations, partnerships and multi-member LLCs, rental (Schedule E) and K-1 income, foreign income and accounts, nonresidents and dual-status filers, amended returns and IRS notices (see the refusal list). For a California resident's state return, `ca-540-individual-return`.

## Ask the client first

- Filing status, and dates of birth of the taxpayer and spouse. Can anyone claim the taxpayer as a dependant?
- A valid social security number for everyone on the return (needed for the Schedule 1-A deductions); a married person must file jointly to claim them.
- Every source of self-employment income: more than one Schedule C, or a partnership, changes Form 7206 and QBI.
- Every Form 1099-NEC, 1099-MISC and 1099-K, to reconcile to the books. Income is reportable whether or not a form arrived.
- Every Form W-2 with box 12 codes (wage base, employer plan eligibility, tips and overtime boxes).
- Health cover by month: who was covered, who paid, Marketplace cover with advance premium tax credit (Form 1095-A), and any month anyone was eligible for a subsidized employer plan.
- The retirement plan type, the date it was set up, and the amounts and dates contributed.
- 2026 estimated payments (dates and amounts), any 2025 overpayment applied, and the 2025 total tax and AGI.
- Capital gains, dividends, rental income, K-1s, foreign income or accounts and digital assets.
- State of residence for 2026, for the state handoff.

## The method, step by step

| Step | Do this | Skill to load | Lands on (2025 line numbers) |
| --- | --- | --- | --- |
| 1 | Close the books: reconcile receipts to deposits and every 1099; exclude transfers, loans and personal items | `us-sole-prop-bookkeeping`, `us-1099-k-and-payment-processors` | Schedule C lines 1 to 27b |
| 2 | Finish Schedule C, including depreciation and the home office | `us-schedule-c-and-se-computation`, `us-section-179-and-bonus-depreciation` | Schedule C line 31 |
| 3 | Schedule SE and Form 8959 | `us-schedule-c-and-se-computation` | Schedule 2 line 4; Schedule 1 line 15 |
| 4 | Retirement deduction: base is net profit less the deductible half of SE tax, not less health insurance | `us-self-employed-retirement` | Schedule 1 line 16 |
| 5 | Health insurance deduction: limit is net profit less the deductible half less step 4 | `us-self-employed-health-insurance` | Form 7206 line 14; Schedule 1 line 17 |
| 6 | Marketplace cover only: resolve the premium tax credit and step 5 together (Pub. 974), Form 8962 | `us-premium-tax-credit-8962` | Schedule 2 line 1a or Schedule 3 line 9 |
| 7 | Rest of Schedule 1 (HSA, IRA, student loan interest), then AGI | `us-federal-income-tax-return-1040` | Form 1040 lines 10, 11a |
| 8 | Standard or itemized deduction, with the SALT cap | `us-federal-income-tax-return-1040` | line 12e |
| 9 | Schedule 1-A: tips, overtime, car loan interest, senior deduction | `us-federal-income-tax-return-1040` | line 13b |
| 10 | QBI deduction on income before QBI = line 11a − 12e − 13b | `us-qbi-deduction` | line 13a |
| 11 | Capital gains and qualified dividends, if any | `us-capital-gains` | Schedule D; line 7a |
| 12 | Tax, Schedule 2 Part I, credits (child tax credit, education, foreign tax) | `us-federal-income-tax-return-1040`, `us-child-tax-credit-and-eitc`, `us-education-credits-8863`, `us-foreign-tax-credit-1116` | lines 16 to 24 |
| 13 | Payments and the estimated tax penalty (Form 2210 only if a Part II box applies); next year's vouchers | `us-quarterly-estimated-tax` | lines 25d, 26, 33, 38 |
| 14 | Tie-outs below, then the package: return, recomputing working paper, reviewer note of every judgment call | this skill | |

**Why step 4 before step 5.** Form 7206 line 9 subtracts the Schedule 1 line 16 retirement deduction for the same business, while the Pub. 560 worksheet for the retirement deduction never subtracts health insurance. Doing them in this order has no loop. The only true loop in the return is step 5 with step 6 (Marketplace cover). Sources: [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf), [Pub. 560](https://www.irs.gov/pub/irs-pdf/p560.pdf), [Pub. 974](https://www.irs.gov/publications/p974).

### Tie-out checks before sign-off

Line numbers are from the 2025 forms; check them against the 2026 forms when issued.

- Schedule C line 31 = Schedule SE line 2 (one business, no farm or partnership income).
- Schedule SE line 12 = Schedule 2 line 4, and Schedule SE line 13 = Schedule 1 line 15.
- Form 7206 line 14 (or the worksheet) = Schedule 1 line 17; Form 7206 line 9 = the line 16 amount for the same business.
- Schedule 1 line 26 = lines 11 to 23 plus 25 = Form 1040 line 10.
- Form 1040 line 9 = 1z + 2b + 3b + 4b + 5b + 6b + 7a + 8; line 11a = 9 − 10; line 11b = 11a.
- Form 8995 line 11 (or 8995-A line 33) = line 11a − 12e − 13b; the QBI deduction = line 13a.
- Schedule 1-A line 38 = line 13b; line 14 = 12e + 13a + 13b; line 15 = 11b − 14, not below zero.
- Schedule 2 line 21 = line 23; line 24 = 22 + 23.
- Line 33 = 25d + 26 + 32; line 26 agrees with the IRS online account payment record.
- Form 8962: excess advance credit = Schedule 2 line 1a; net credit = Schedule 3 line 9.
- Only one of line 34 and line 37 is positive, equal to the difference between lines 33 and 24.
- Every 1099 is traced to a Schedule C line or an explained exclusion.

### Worked case: the order error

A single developer has 2026 net profit of USD 120,000, no wages, and contributes USD 15,000 to a SEP. Deductible half of SE tax: USD 120,000 x 92.35% x 15.3% / 2 = USD 8,477.73 (all under the wage base). The correct Form 7206 limit is USD 120,000 − USD 8,477.73 − USD 15,000 = USD 96,522.27. A preparer who does health insurance before the SEP gets USD 111,522.27, USD 15,000 too high; with premiums between those two amounts the deduction would be overstated.

```oa-check
name: Retirement before the health insurance limit (2026)
inputs:
  net_profit: 120000
  sep: 15000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - limit_right_order: net_profit - half_se - sep
  - limit_wrong_order: net_profit - half_se
  - overstatement: limit_wrong_order - limit_right_order
expected:
  half_se: 8477.73
  limit_right_order: 96522.27
  limit_wrong_order: 111522.27
  overstatement: 15000
```

## When to refuse or refer

- An S corporation, partnership or multi-member LLC; a Schedule C loss with at-risk, passive activity or excess business loss questions.
- Rental income, K-1s, material capital gains or digital asset disposals beyond simple Schedule D reporting (`us-capital-gains`).
- Foreign income, Form 2555, FBAR or Form 8938 (`us-fbar-and-fatca-8938`), a nonresident or dual-status filer (`us-form-1040-nr-nonresident-return`).
- A specified service business above the QBI threshold, aggregation, or the wage and property limits (Form 8995-A schedules).
- Marketplace cover where the Pub. 974 computation does not converge, or household income is near the edge of eligibility.
- Tips in an occupation not clearly on the IRS list, overtime not shown on a W-2 or 1099, or tips earned in a possible specified service business.
- A tie-out that fails and cannot be explained from the documents.
- Amended returns (`us-amended-return-form-1040-including-capital`), unfiled years, IRS notices or collection.
- Any figure that cannot be traced to a source document or an official IRS page: flag it, never guess.

## Filing and payment

The 2026 return is due **15 April 2027**; Form 4868 by that date extends filing to 15 October 2027 but not payment. Deadlines, payment routes and penalties are in `us-federal-income-tax-return-1040`; the 2027 estimated tax schedule is in `us-quarterly-estimated-tax`. Hand the state preparer federal AGI, taxable income, the QBI deduction, depreciation detail, and the health insurance and retirement amounts.

## Completion checklist

- Intake recorded, including health cover by month and SSN status.
- Schedule C reconciled to the bank and every 1099.
- Schedule SE, then retirement, then health insurance (then Form 8962 if Marketplace), in that order.
- Schedule 1-A tested person by person.
- QBI computed from line 11a − 12e − 13b on the right form.
- Every tie-out passes or is explained in the reviewer note.
- Safe harbour tested; Form 2210 only if a Part II box applies.
- Filing, extension and payment confirmed; 2027 estimates scheduled; state handoff prepared.
- A credentialed preparer reviews and signs.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Form 7206 (2025). Read for line 9 (retirement deduction subtracted) and line 14 to Schedule 1. | https://www.irs.gov/pub/irs-pdf/f7206.pdf | 2026-11-13 |
| IRS Publication 560 (2025). Read for the Deduction Worksheet for Self-Employed, which subtracts only the deductible half of SE tax. | https://www.irs.gov/pub/irs-pdf/p560.pdf | 2026-11-13 |
| IRS Publication 974. Read for the simplified and iterative methods for the premium tax credit with the self-employed health insurance deduction. | https://www.irs.gov/publications/p974 | 2026-11-13 |
| Schedule 1 (Form 1040) 2025. Read for lines 10 to 26. | https://www.irs.gov/pub/irs-pdf/f1040s1.pdf | 2026-11-13 |
| Schedule 2 (Form 1040) 2025. Read for lines 1a, 4, 11, 12 and 21. | https://www.irs.gov/pub/irs-pdf/f1040s2.pdf | 2026-11-13 |
| Schedule 3 (Form 1040) 2025. Read for line 9, the net premium tax credit. | https://www.irs.gov/pub/irs-pdf/f1040s3.pdf | 2026-11-13 |
| Form 1040 (2025). Read for lines 1z to 38 used in the tie-outs. | https://www.irs.gov/pub/irs-pdf/f1040.pdf | 2026-11-13 |
| Schedule C (Form 1040) 2026. Read for line 31. | https://www.irs.gov/pub/irs-pdf/f1040sc.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form 1040 and Schedules 1, 1-A, 2 and 3 were not published when read, so every line number above is from the 2025 forms and must be checked against the 2026 forms; Publication 974 was not re-read line by line for 2026.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-federal-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-federal-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
