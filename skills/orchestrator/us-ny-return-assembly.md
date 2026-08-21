---
name: us-ny-return-assembly
description: Final orchestrator skill that assembles the complete federal and New York State filing package for New York resident sole proprietors and single-member LLCs disregarded for federal tax. Consumes outputs from all federal content skills (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC) and all New York content skills (IT-201 individual return, NYC UBT Form NYC-202 where applicable, NY estimated tax IT-2105, MCTMT) to produce a single unified reviewer package. Handles reconciliation between federal AGI and NY AGI adjustments, NY itemized vs standard deduction election, NYC income tax surcharge, NYC UBT credit against personal income tax, and MCTMT computation. New York full-year residents only.
version: 1.0
jurisdiction: US-NY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Ny Return Assembly

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

- Do NOT ask "how deep do you want me to go" or "do you want the full package." Produce it.
- Do NOT announce token counts or tool calls.
- Do NOT ask which deliverables to prioritize. Produce all deliverables listed in Section 6.
- Do NOT re-validate scope that intake already validated.
- Do NOT pause between content skills to check in.
- Self-checks are targets, not blockers. If one fails, flag it for reviewer and continue.
- If you feel the urge to ask "how should I proceed," pick the most defensible path and flag the decision in the reviewer brief.

## Section 1 — Scope

Produces the complete federal + New York filing package for:
- Full-year New York State residents (including NYC residents)
- Sole proprietors or single-member LLCs disregarded for federal tax
- Tax year 2025
- Filing Form 1040 (federal), IT-201 (NY State), NYC-202 (NYC UBT, if applicable)

## Section 2 — Execution order

0. **Step 1** — us-sole-prop-bookkeeping
0. **Step 2** — us-schedule-c-and-se-computation
0. **Step 3** — us-self-employed-retirement
0. **Step 4** — us-self-employed-health-insurance
0. **Step 5** — us-qbi-deduction
0. **Step 6** — us-federal-return-assembly
0. **Step 7** — us-quarterly-estimated-tax
0. **Step 8** — us-1099-nec-issuance
0. **Step 9** — ny-it-201-individual-return
0. **Step 10** — nyc-ubt-form-202
0. **Step 11** — ny-estimated-tax-it-2105
0. **Step 12** — ny-mctmt
0. **Step 13** — THIS SKILL — final assembly and verification

### Federal internal consistency

- **Schedule C net profit flow** — Schedule C net profit → Schedule 1 Line 3 → Form 1040 Line 8
- **Schedule SE tax flow** — Schedule SE tax → Schedule 2 Line 4 → Form 1040 Line 23
- **Half of SE tax flow** — Half of SE tax → Schedule 1 Line 15 → Form 1040 Line 10
- **SE retirement flow** — SE retirement → Schedule 1 Line 16 → Form 1040 Line 10
- **SE health insurance flow** — SE health insurance → Schedule 1 Line 17 → Form 1040 Line 10
- **QBI deduction flow** — QBI deduction → Form 1040 Line 13
- **Total tax flow** — Total tax → Form 1040 Line 24
- **Form 2210 penalty** — Form 2210 penalty (if applicable)
- **Total payments flow** — Total payments → Form 1040 Line 33

### New York internal consistency

- **Federal AGI starting point** — Federal AGI → IT-201 Line 19 (starting point)
- **NY additions** — NY additions (IT-201 Lines 20-23): interest income on non-NY state/local bonds, QBI deduction add-back (NY does not allow QBI deduction)
- **NY subtractions** — NY subtractions (IT-201 Lines 24-32): interest on US government obligations, NY state/local pension exclusion
- **NY AGI flow** — NY AGI → IT-201 Line 33
- **NY standard deduction** — $8,000 single / $16,050 MFJ vs NY itemized deduction (IT-201 Line 34-35)  _(IT-201 Line 34-35)_
- **NY itemized deduction limitation threshold** — 50% limitation on charitable contributions and other adjustments if NY AGI > $525,000
- **NY taxable income flow** — NY taxable income → IT-201 Line 38
- **NY tax computation** — NY tax → IT-201 Line 39 (from tax computation worksheet or tax table)
- **NYC resident tax flow** — NYC resident tax → IT-201 Lines 47-51 (if NYC resident)
- **NYC UBT credit flow** — NYC UBT credit → IT-201 Line 51 (partial credit against NYC personal income tax)
- **NY household credit** — NY household credit → IT-201 Line 40 (if income below threshold)
- **Total NY tax flow** — Total NY tax → IT-201 Line 62
- **NY estimated tax payments flow** — NY estimated tax payments → IT-201 Line 67
- **NY refund or balance due flow** — NY refund or balance due → IT-201 Line 78 or 80

### NYC UBT consistency (if applicable)

- **Gross income from NYC business flow** — Gross income from NYC business → Form NYC-202 Line 1
- **NYC UBT deductions flow** — NYC UBT deductions → Form NYC-202 Lines 2-12
- **NYC UBT taxable income flow** — NYC UBT taxable income → Form NYC-202 Line 13
- **NYC UBT exemption calculation** — $95,000, phaseout $95K-$150K USD  _(Form NYC-202 Line 14-16)_
- **UBT tax rate** — 4% (of taxable income after exemption)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **UBT credits available** — UBT credits available → NYC-202 Line 18+
- **UBT estimated payments** — UBT estimated payments → NYC-202 Schedule F
- **UBT balance due or refund** — UBT balance due or refund

### Federal-NY coordination

- **Federal AGI as NY starting point** — Federal AGI used correctly as NY starting point
- **QBI add-back for NY** — QBI deduction properly added back for NY (NY does not conform to §199A)
- **Filing status consistency** — Filing status consistent
- **Dependents consistency** — Dependents consistent
- **NY itemized deductions basis** — NY itemized deductions use federal Schedule A as starting point but apply NY modifications: - State/local tax deduction: included for NY purposes (no $10,000 SALT cap at state level) - College tuition deduction (IT-201 Line 30): up to $10,000 per student  _(IT-201 Line 30)_
- **Depreciation conformity** — NY generally conforms to federal MACRS but has modifications for bonus depreciation (NY decoupled from 100% bonus; add-back required, then NY allows its own depreciation deduction)

### MCTMT verification

- **MCTMT threshold** — $50,000 USD (only taxed if net SE earnings in MCTD exceed $50,000)
- **MCTMT rate** — 0.34% (on net SE earnings > $50,000 allocated to MCTD)  _(Section 7 — NY-specific tax framework > Metropolitan Commuter Transportation Mobility Tax (MCTMT))_
- **Net SE earnings allocation to MCTD** — Net self-employment earnings allocated to MCTD
- **MCTMT amount flow** — MCTMT amount → Form MTA-6

### Estimated tax reconciliation

- **Federal safe harbor** — Federal: 4 quarterly payments cross-checked against safe harbor (100% prior year tax if AGI ≤ $150K, 110% if AGI > $150K)
- **NY State safe harbor** — NY State: payments on IT-2105 cross-checked against NY safe harbor (100% prior year NY tax or 90% current year)
- **UBT estimated tax quarterly payment threshold** — $3,400 USD (quarterly payments required if UBT liability expected to exceed this amount)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **IT-2105.9 underpayment penalty** — Form IT-2105.9 (NY underpayment penalty) if applicable

### Additions to federal AGI (common for freelancers)

- **QBI deduction add-back** — NY does not allow the §199A deduction. Full federal QBI deduction amount added back on IT-225 Line 1 (code A-201)  _(IT-225 Line 1 (code A-201))_
- **Bonus depreciation add-back** — If federal return claimed bonus depreciation, NY requires add-back of the federal bonus amount, then allows NY depreciation (generally MACRS without bonus). IT-225 code A-110.  _(IT-225 code A-110)_
- **Other states' municipal bond interest** — Interest from non-NY state/local bonds is added to NY income

### Subtractions from federal AGI (common for freelancers)

- **US government obligation interest** — Interest on US Treasury securities subtracted from NY income (IT-225 code S-103)  _(IT-225 code S-103)_
- **College tuition subtraction** — Up to $10,000 per eligible student (IT-225 code S-106) USD  _(IT-225 code S-106)_
- **NY depreciation subtraction** — Replacement depreciation deduction for assets where bonus depreciation was added back (IT-225 code S-110)  _(IT-225 code S-110)_

### NYC UBT credit mechanism

- **NYC UBT not deductible on Schedule C** — The taxpayer cannot deduct NYC UBT as a business expense on the federal Schedule C (it is a tax, not a deductible business expense).
- **NYC UBT credit generation** — NYC UBT paid generates a partial credit against NYC personal income tax (IT-201 Line 51)  _(IT-201 Line 51)_
- **NYC UBT credit amount** — The credit equals the lesser of: (a) the UBT tax, or (b) the NYC personal income tax before the credit
- **Double-taxation prevention** — Effectively prevents double-taxation of NYC business income at both UBT and personal income tax levels, but the credit is not always dollar-for-dollar

## Section 5 — Refusals

- **R-NY-1** — Upstream skill did not run. Name the specific skill and refuse until it executes.  _(R-NY-1)_
- **R-NY-2** — Multi-state allocation required. If income sourced to states other than NY was not identified at intake and appears in documents, refuse. Multi-state allocation requires IT-203/credit for taxes paid analysis.  _(R-NY-2)_
- **R-NY-3** — NYC UBT allocation dispute. If the taxpayer performed significant business activity outside NYC but is a NYC resident, allocation percentage is complex. Flag for reviewer if allocation is not clearly 100%.  _(R-NY-3)_
- **R-NY-4** — Partnership/S-corp income discovered. K-1 income appearing in documents that was not disclosed at intake. Refuse and recommend CPA.  _(R-NY-4)_
- **R-NY-5** — NY PTET (Pass-Through Entity Tax) election. If the SMLLC elected into NY PTET, different treatment applies. Refuse unless PTET skill is available.  _(R-NY-5)_

### Documents

1. **Executive summary** — filing status, income, federal tax, NY tax, NYC tax, NYC UBT, MCTMT, total liability, refund/balance due
2. **Federal Form 1040 worksheet** — line-by-line
3. **Schedule C** — sole prop P&L
4. **Schedule SE** — SE tax
5. **Schedule 1, 2, 3** — adjustments, additional taxes, credits
6. **Form 8995 or 8995-A** — QBI
7. **Form 2210** — federal underpayment penalty (if applicable)
8. **Form 1040-ES** — 2026 federal estimated tax schedule
9. **NY IT-201 worksheet** — line-by-line state return
10. **IT-225** — NY addition and subtraction modifications
11. **NYC-202 worksheet** — UBT computation (if NYC resident)
12. **IT-2105** — 2026 NY estimated tax schedule
13. **IT-2105.9** — NY underpayment penalty (if applicable)
14. **Form MTA-6** — MCTMT (if applicable)
15. **1099-NEC batch** — contractor information returns (if applicable)
16. **Reviewer brief** — comprehensive narrative
17. **Taxpayer action list** — deadlines, amounts, payment methods

### Reviewer brief structure

```markdown
# Complete Return Package: [Taxpayer Name] — Tax Year 2025

## Executive Summary
- Filing status: [X]
- Residence: New York ([NYC / rest of state])
- Business: Sole proprietor / SMLLC disregarded
- Federal total tax: $X
- NY State tax: $X
- NYC personal income tax: $X
- NYC UBT: $X
- MCTMT: $X
- Total 2025 tax liability: $X
- Total payments (federal + NY + NYC): $X
- Net refund or balance due: $X

## Federal Return
[Federal assembly content]

## New York State Return (IT-201)
- Federal AGI: $X
- NY additions: $X (QBI add-back $X, bonus depreciation $X, other $X)
- NY subtractions: $X
- NY AGI: $X
- NY deduction (standard/itemized): $X
- NY taxable income: $X
- NY tax (from table/worksheet): $X
- NYC personal income tax: $X
- NYC UBT credit applied: $X
- NY household credit: $X (if applicable)
- Net NY/NYC tax: $X
- NY estimated payments applied: $X
- NY balance due or refund: $X

## NYC Unincorporated Business Tax (if applicable)
- Gross business income in NYC: $X
- Allocable deductions: $X
- NYC UBT taxable income: $X
- Exemption applied: $X
- UBT at 4%: $X
- UBT credits: $X
- Net UBT: $X
- UBT estimated payments: $X
- UBT balance due or refund: $X

## MCTMT (if applicable)
- Net SE earnings in MCTD: $X
- MCTMT (0.34%): $X

## Cross-jurisdiction reconciliation
- Federal AGI matches IT-201 starting point: [verified]
- QBI add-back computed correctly: [verified]
- NYC UBT credit does not exceed NYC personal income tax: [verified]
- All estimated payments allocated correctly: [verified]

## Reviewer attention flags
[Aggregated flags]

## Positions taken
[With citations to IRC, NY Tax Law, NYC Admin Code]

## Planning notes for 2026
- NY PTET election consideration (if beneficial)
- NYC UBT estimated tax adjustment
- Federal/NY/NYC estimated tax coordination
- S-corp election analysis (potential NYC UBT savings)
```

## Executive Summary

- Filing status: [X]
- Residence: New York ([NYC / rest of state])
- Business: Sole proprietor / SMLLC disregarded
- Federal total tax: $X
- NY State tax: $X
- NYC personal income tax: $X
- NYC UBT: $X
- MCTMT: $X
- Total 2025 tax liability: $X
- Total payments (federal + NY + NYC): $X
- Net refund or balance due: $X

## Federal Return

[Federal assembly content]

## New York State Return (IT-201)

- Federal AGI: $X
- NY additions: $X (QBI add-back $X, bonus depreciation $X, other $X)
- NY subtractions: $X
- NY AGI: $X
- NY deduction (standard/itemized): $X
- NY taxable income: $X
- NY tax (from table/worksheet): $X
- NYC personal income tax: $X
- NYC UBT credit applied: $X
- NY household credit: $X (if applicable)
- Net NY/NYC tax: $X
- NY estimated payments applied: $X
- NY balance due or refund: $X

## NYC Unincorporated Business Tax (if applicable)

- Gross business income in NYC: $X
- Allocable deductions: $X
- NYC UBT taxable income: $X
- Exemption applied: $X
- UBT at 4%: $X
- UBT credits: $X
- Net UBT: $X
- UBT estimated payments: $X
- UBT balance due or refund: $X

## MCTMT (if applicable)

- Net SE earnings in MCTD: $X
- MCTMT (0.34%): $X

## Cross-jurisdiction reconciliation

- Federal AGI matches IT-201 starting point: [verified]
- QBI add-back computed correctly: [verified]
- NYC UBT credit does not exceed NYC personal income tax: [verified]
- All estimated payments allocated correctly: [verified]

## Reviewer attention flags

[Aggregated flags]

## Positions taken

[With citations to IRC, NY Tax Law, NYC Admin Code]

## Planning notes for 2026

- NY PTET election consideration (if beneficial)
- NYC UBT estimated tax adjustment
- Federal/NY/NYC estimated tax coordination
- S-corp election analysis (potential NYC UBT savings)

## Section 7 — Taxpayer action list structure

```markdown

## Taxpayer Action List

### Before April 15, 2026:
1. Review and sign return package
2. Pay federal balance due: $X via EFTPS / IRS Direct Pay
3. Pay NY balance due: $X via NY DTF Online Services
4. Pay NYC UBT balance due: $X via NYC DOF eFiling (if applicable)
5. Pay 2026 Q1 federal estimated tax: $X
6. Pay 2026 Q1 NY estimated tax: $X (25% of annual estimate)
7. Pay 2026 Q1 NYC UBT estimated tax: $X (if applicable)
8. File MCTMT annual return (if applicable)

### Before June 16, 2026:
1. Pay 2026 Q2 federal estimated tax: $X
2. Pay 2026 Q2 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q2 NYC UBT estimated tax: $X (if applicable)

### Before September 15, 2026:
1. Pay 2026 Q3 federal estimated tax: $X
2. Pay 2026 Q3 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q3 NYC UBT estimated tax: $X (if applicable)

### Before January 15, 2027:
1. Pay 2026 Q4 federal estimated tax: $X
2. Pay 2026 Q4 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q4 NYC UBT estimated tax: $X (if applicable)

### Ongoing:
1. Collect W-9 from new contractors before payment
2. Track business expenses with receipts
3. Monitor income for UBT exemption phaseout
4. Consider S-corp election if net SE income exceeds $150K+ (reduces SE tax and eliminates UBT)
```

### Before April 15, 2026:

1. Review and sign return package
2. Pay federal balance due: $X via EFTPS / IRS Direct Pay
3. Pay NY balance due: $X via NY DTF Online Services
4. Pay NYC UBT balance due: $X via NYC DOF eFiling (if applicable)
5. Pay 2026 Q1 federal estimated tax: $X
6. Pay 2026 Q1 NY estimated tax: $X (25% of annual estimate)
7. Pay 2026 Q1 NYC UBT estimated tax: $X (if applicable)
8. File MCTMT annual return (if applicable)

### Before June 16, 2026:

1. Pay 2026 Q2 federal estimated tax: $X
2. Pay 2026 Q2 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q2 NYC UBT estimated tax: $X (if applicable)

### Before September 15, 2026:

1. Pay 2026 Q3 federal estimated tax: $X
2. Pay 2026 Q3 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q3 NYC UBT estimated tax: $X (if applicable)

### Before January 15, 2027:

1. Pay 2026 Q4 federal estimated tax: $X
2. Pay 2026 Q4 NY estimated tax: $X (25% of annual estimate)
3. Pay 2026 Q4 NYC UBT estimated tax: $X (if applicable)

### Ongoing:

1. Collect W-9 from new contractors before payment
2. Track business expenses with receipts
3. Monitor income for UBT exemption phaseout
4. Consider S-corp election if net SE income exceeds $150K+ (reduces SE tax and eliminates UBT)

## Section 8 — Self-checks

**Check NY-A1 — All upstream skills executed.**
**Check NY-A2 — Federal AGI correctly flows to IT-201 Line 19.**
**Check NY-A3 — QBI deduction added back on IT-225 (NY does not allow §199A).**
**Check NY-A4 — NYC UBT computed if NYC resident with business income.**
**Check NY-A5 — NYC UBT credit does not exceed NYC personal income tax.**
**Check NY-A6 — MCTMT computed for MCTD-area self-employed with earnings > $50K.**
**Check NY-A7 — NY estimated tax underpayment penalty evaluated (IT-2105.9).**
**Check NY-A8 — Bonus depreciation add-back and replacement NY depreciation computed.**
**Check NY-A9 — NY standard vs itemized deduction: correct election made (NY allows different election than federal).**
**Check NY-A10 — Payment instructions include all four jurisdictions where applicable (federal, NY, NYC personal, NYC UBT).**

## Section 9 — Output files

Three files:

1. **`[taxpayer_slug]_2025_master.xlsx`** — Sheets: Cover, Income, Schedule C, Schedule SE, Retirement, SE Health, QBI, Schedule 1, Form 1040, Form 2210, IT-201, IT-225, NYC-202, IT-2105.9, MTA-6, 1099-NEC batch, 2026 Est Tax (Fed+NY+NYC).

2. **`reviewer_brief.md`** — Full narrative covering federal, NY State, NYC, MCTMT, cross-jurisdiction reconciliation, flags, citations, planning.

3. **`taxpayer_action_list.md`** — Step-by-step with dates, amounts, and payment URLs (EFTPS, NY DTF, NYC DOF).

## Section 10 — Known gaps

1. NY PTET election analysis not automated (requires entity-level election before filing deadline)
2. NYC UBT allocation for taxpayers performing work both inside and outside NYC is complex and may require reviewer judgment
3. NY bonus depreciation add-back computation requires detailed asset-by-asset tracking
4. Form IT-2658 (group estimated tax for partnerships) not applicable but flagged to avoid confusion
5. NYC-210 (Claim for NYC School Tax Credit) automatically claimed on IT-201 if eligible — verify $125 (single) or $250 (MFJ) credit
6. NY Earned Income Credit (30% of federal EIC) — verify if applicable

## End of Skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
