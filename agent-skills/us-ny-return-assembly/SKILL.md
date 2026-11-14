---
name: us-ny-return-assembly
description: "Final step of the New York freelancer workflow for tax year 2026. Runs the federal and New York skills in order for a full-year New York resident sole proprietor or single-member LLC, checks that the figures agree across Form 1040, Form IT-201 and IT-225, Form NYC-202 and Form IT-219, the MCTMT lines and the estimated tax schedules, and produces the reviewer brief, the working paper and the client's action list with 2027 dates. Carries no rates of its own; every figure is in the skill that owns it. Trigger after us-ny-freelance-intake hands off, or on \"assemble my New York return\", \"NY return package\", \"reviewer brief New York\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-ny-return-assembly"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New York freelancer return assembly, tax year 2026

> **Source-cited draft.** Routing and cross-checks built from the 2025 Form IT-201, IT-225 and IT-219 instructions, the 2026 Form IT-2105 instructions and the 2025 Form NYC-202 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Run the skills in the order below, then check the links between returns: federal AGI is the starting point of Form IT-201; any UBT or MCTMT deducted on Schedule C is added back on Form IT-225 (codes A-201 and A-214); the UBT on Form NYC-202 feeds the IT-219 credit on Form IT-201 line 53, capped at the city tax; estimated payments for each tax are matched to the right return. Then write the reviewer brief and the client's action list. This skill states no tax figures.

## Scope and who this is for

In scope: the complete 2026 federal and New York filing package for a full-year New York State resident (including New York City and Yonkers residents) who is a sole proprietor or a single-member LLC disregarded for federal tax: Form 1040, Form IT-201 with IT-225 and IT-219, and Form NYC-202 or NYC-202S where the UBT applies.

Out of scope: anything `us-ny-freelance-intake` refused (part-year or nonresident returns, partnerships, corporations, multi-state income, open audits). If such a fact appears in the documents now, stop (see "When to refuse or refer").

## Ask the client first

Intake has already collected the facts. Ask again only where a fact is missing or the documents contradict each other:

1. Any income, entity or move that intake did not record.
2. Whether any UBT or MCTMT was deducted on the federal Schedule C.
3. Where the business is carried on, if any work was done outside New York City or outside the MCTD.
4. Whether the client wants the 2027 estimates on the prior-year or the current-year route.

## The method, step by step

### How this workflow runs

- Produce the full package; do not ask how deep to go, which deliverables to prioritize, or whether to continue between skills.
- Do not re-check scope that intake already checked.
- Self-checks are targets, not blockers: if one fails, flag it for the reviewer and continue.
- Where a choice is needed, pick the most defensible path and record it under "Positions taken" in the reviewer brief.

### Order of skills

1. `us-sole-prop-bookkeeping`
2. `us-schedule-c-and-se-computation`
3. `us-self-employed-retirement`
4. `us-self-employed-health-insurance`
5. `us-qbi-deduction`
6. `us-federal-return-assembly`
7. `us-quarterly-estimated-tax`
8. `us-1099-nec-issuance` (if contractors were paid)
9. `ny-it-201-resident-return`
10. `nyc-ubt` (if the business is carried on in New York City)
11. `ny-estimated-tax`
12. `ny-mctmt` (if self-employment earnings are allocated to the MCTD)
13. `ny-llc-filing-fee-it-204-ll` (single-member LLC)
14. This skill: cross-checks and output

If an upstream skill did not run, name it and stop until it does (R-NYA-1).

### Cross-checks: federal

- Schedule C net profit to Schedule 1 line 3; Schedule SE tax to Schedule 2 line 4; half of SE tax, SE retirement and SE health insurance to Schedule 1 (lines 15, 16 and 17); the QBI deduction to Form 1040 line 13; total tax and total payments tie to the federal assembly working paper.
- Form 2210 run if federal estimates fell short.

### Cross-checks: New York State (Form IT-201)

- Lines 1 to 19 equal the finished federal return, ending at federal AGI ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **No QBI add-back.** New York starts from federal AGI, and the section 199A deduction is taken after AGI, so it never reaches Form IT-201. The older version of this skill told the preparer to add the QBI deduction back with code A-201; that was wrong. A-201 is the add-back of income taxes and unincorporated business taxes deducted in computing federal AGI ([IT-225-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf)).
- UBT deducted on Schedule C: added back with A-201. MCTMT deducted federally: added back with A-214.
- Bonus depreciation, section 168(n) property and R&E expenditures: the Notice N-26-1 codes (A-209 and S-213; A-225, S-221 and S-222) as set out in `ny-it-201-resident-return`. The older version gave codes A-110, S-103, S-106 and S-110; use the codes in the current IT-225 instructions.
- Interest on US government obligations is a line 28 subtraction; other states' municipal bond interest is a line 20 addition.
- Standard or itemized deduction chosen for New York on its own merits (New York allows a different choice from the federal one) and taxable income on line 38.
- Tax on line 39 from the table, the rate schedule or the recapture worksheet, with the 2026 rates.
- New York City residents: city tax on lines 47 and 47a, household credit, IT-219 UBT credit on line 53 (via Form IT-201-ATT line 8), school tax credits, city earned income credit.
- MCTMT on lines 54a and 54b where a zone's earnings are over the threshold for the year; Yonkers surcharge on line 55.
- Payments: withholding, IT-2105 estimates and any IT-370 extension payment, then the refund or balance due; Form IT-2105.9 if estimates fell short.

### Cross-checks: New York City UBT (Form NYC-202 or NYC-202S)

- Schedule B starts from the same Schedule C net profit as the federal return; income taxes and UBT deducted federally are added back on Schedule B line 9.
- Schedule A: allowance for services, the exemption, the 4% tax, the business tax credit, the UBT on line 19, other credits, estimated payments on line 22 ([NYC-202 instructions (2025)](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf)). The figures are in `nyc-ubt`.
- The UBT carried to Form IT-219 equals Form NYC-202 line 21 (or NYC-202S line 8), and the IT-219 credit does not exceed the city tax less the city household credit ([IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
- The older version said the UBT is not deductible on Schedule C and that the IT-219 credit equals the full UBT; both were wrong. The UBT is deducted federally and added back for New York, and the IT-219 credit is a percentage of the UBT that falls as city income rises.

### Cross-checks: MCTMT

- The base is net earnings from self-employment allocated to each zone, tested per person and per zone. Self-employed individuals report the MCTMT on Form IT-201 lines 54a to 54e, not on a separate return; the older version pointed to Form MTA-6, which is not the individual's form ([IT-201-I (2025), lines 54a to 54e](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).

### Cross-checks: estimated tax

- Federal 2026 payments matched to the federal safe harbour (`us-quarterly-estimated-tax`).
- New York 2026 payments (Form IT-2105) matched to the required annual payment (`ny-estimated-tax`); UBT estimates (Form NYC-5UBTI) kept apart from IT-2105 payments (`nyc-ubt`).
- 2027 estimates set up for federal, New York State (including MCTMT) and New York City UBT.

### The documents to produce

1. Executive summary: filing status, income, federal tax, New York State tax, New York City tax, UBT, MCTMT, total liability, refund or balance due.
2. Federal Form 1040 working paper, line by line, with Schedules C, SE, 1, 2 and 3, Form 8995 or 8995-A, and Form 2210 if needed.
3. Federal 2027 estimated tax schedule (Form 1040-ES).
4. Form IT-201 working paper, line by line, with IT-225, IT-219 and IT-201-ATT where they apply.
5. Form NYC-202 or NYC-202S working paper (if the UBT applies).
6. New York 2027 estimated tax schedule (Form IT-2105) and Form IT-2105.9 if needed.
7. The 1099-NEC batch, if contractors were paid.
8. The reviewer brief and the client's action list (below).

Output files: a master workbook (sheets for each form above), `reviewer_brief.md` and `taxpayer_action_list.md` with dates, amounts and payment links.

### Reviewer brief: structure

```markdown
# Return package: [client] - tax year 2026

## Executive summary
- Filing status; residence (New York City, Yonkers or rest of state); business type
- Federal total tax; New York State tax; New York City tax; UBT; MCTMT
- Total 2026 liability; total payments; refund or balance due

## Federal return
## New York State return (IT-201)
- Federal AGI; additions (by IT-225 code); subtractions; New York AGI
- Deduction (standard or itemized); taxable income; tax and method used
- City tax; IT-219 credit; household credits; net state and city tax; payments; balance
## New York City UBT (if it applies)
- Business income; allowance for services; exemption; tax; business tax credit; UBT; estimates; balance
## MCTMT (if it applies)
- Earnings by zone; tax by zone
## Cross-jurisdiction reconciliation
- Federal AGI equals IT-201 line 19
- UBT and MCTMT add-backs match the Schedule C deductions
- IT-219 credit within the city tax
- Each estimated payment applied to the right return
## Reviewer attention flags
## Positions taken (with citations)
## Planning notes for 2027
- PTET, NYC UBT estimates, estimated tax coordination, S corporation question (`us-s-corp-election-decision`)
```

### Client action list: structure

```markdown
## Action list

### By 15 April 2027
1. Review and sign the return package
2. Pay the federal balance (EFTPS or IRS Direct Pay)
3. Pay the New York balance (Tax Department Online Services)
4. Pay the New York City UBT balance (NYC e-Services), if any
5. Pay the first 2027 installment of federal, New York (IT-2105) and UBT (NYC-5UBTI) estimates
6. File Form IT-370, Form NYC-EXT and federal Form 4868 if more time is needed (each extends filing only; NYC needs its own form)

### By 15 June 2027, 15 September 2027 and 15 January 2028
1. Pay the 2027 federal, New York and UBT installments

### All year
1. Get a W-9 from each new contractor before paying them
2. Keep receipts for business expenses
3. Watch income against the UBT and MCTMT thresholds
4. Revisit the S corporation question with `us-s-corp-election-decision`
```

Due dates for 2027 are those that apply when each date falls on a weekday; confirm them against the 2027 Form 1040-ES, IT-2105 and NYC-5UBTI when published.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NYA-1 | An upstream skill did not run | Name it and stop until it runs |
| R-NYA-2 | Income from another state appears that intake did not record | Stop: multi-state allocation and the IT-112-R credit need a professional |
| R-NYA-3 | Business carried on both inside and outside New York City | Flag: UBT business allocation is referred (`nyc-ubt`) |
| R-NYA-4 | K-1 income from a partnership or S corporation appears | Stop and refer |
| R-NYA-5 | The LLC elected PTET, or the client asks about it | Use `ny-pte-tax-ptet`; refer the election |
| R-NYA-6 | A move into or out of New York State or New York City appears | Stop: part-year return (`ny-residency-leaving-new-york`) |

### Known gaps

1. The PTET election is not automated; it is an entity election made by its own deadline.
2. UBT allocation for work inside and outside New York City needs reviewer judgment.
3. The New York depreciation modifications need asset-by-asset records (Form IT-398).
4. The New York City school tax credit is claimed on Form IT-201 line 69 itself, at the amounts in `ny-it-201-resident-return`; the older version gave amounts twice the published ones and a separate form, which was wrong.
5. The New York State and New York City earned income credits are checked in `ny-it-201-resident-return`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IT-201-I (2025). Read for lines 1 to 19, 20 to 31, 38, 39, 47 to 55 and the payment lines. | https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf | 2026-11-13 |
| IT-225-I (2025). Read for codes A-201, A-214, A-209 and S-213. | https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf | 2026-11-06 |
| IT-219-I (2025). Read for the source of the UBT figure and the credit limit. | https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf | 2026-11-13 |
| IT-2105-I (2026). Read for the MCTMT on Form IT-201 and estimated MCTMT. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| Instructions for Form NYC-202 (2025). Read for Schedule A and Schedule B. | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form IT-201, IT-225, IT-219 and NYC-202 and their instructions are not published, so the line numbers are those of the 2025 forms (2025-2026 filing cycle); the 2027 installment dates in the action list are not yet published.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-ny-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-ny-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
