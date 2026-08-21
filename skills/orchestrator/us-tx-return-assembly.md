---
name: us-tx-return-assembly
description: Final orchestrator skill that assembles the complete federal and Texas compliance filing package for Texas resident sole proprietors and single-member LLCs disregarded for federal tax. Consumes outputs from all federal content skills (bookkeeping, Schedule C/SE, QBI, retirement, SE health insurance, quarterly estimated tax, federal assembly, 1099-NEC) and Texas compliance skills (franchise tax Form 05-102 or 05-158/05-169, sales tax where applicable) to produce a single unified reviewer package. Texas has no state income tax, so the assembly focuses on federal return accuracy plus Texas franchise tax filing and sales tax compliance verification. Reconciles federal return totals with Texas franchise tax total revenue computation and verifies sales tax obligations are met.
version: 1.0
jurisdiction: US-TX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Tx Return Assembly

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

- Do NOT ask "how deep do you want me to go." Produce the full package.
- Do NOT announce token counts or tool calls.
- Do NOT ask which deliverables to prioritize.
- Do NOT re-validate scope that intake already validated.
- Do NOT pause between content skills to check in.
- Self-checks are targets, not blockers. Flag failures for reviewer and continue.
- Texas has no income tax return. This skill focuses on: (1) Federal return completeness, (2) Texas franchise tax compliance, (3) Texas sales tax compliance.

## Section 1 — Scope

Produces the complete federal + Texas compliance package for:
- Full-year Texas residents
- Sole proprietors or single-member LLCs disregarded for federal tax
- Tax year 2025
- Filing Form 1040 (federal) + Texas franchise tax report (Form 05-102 or 05-158/05-169) + Texas sales tax returns (if applicable)

## Section 2 — Execution order

0. **Step 1** — us-sole-prop-bookkeeping
0. **Step 2** — us-schedule-c-and-se-computation
0. **Step 3** — us-self-employed-retirement
0. **Step 4** — us-self-employed-health-insurance
0. **Step 5** — us-qbi-deduction
0. **Step 6** — us-federal-return-assembly
0. **Step 7** — us-quarterly-estimated-tax
0. **Step 8** — us-1099-nec-issuance
0. **Step 9** — tx-franchise-tax
0. **Step 10** — tx-sales-tax-compliance
0. **Step 11** — THIS SKILL — final assembly and verification

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

### Texas franchise tax consistency

- **Below threshold — total revenue matches books** — Total revenue computed from books matches Form 05-102 reporting
- **No-tax-due threshold (2025)** — 2,470,000 USD (2025 threshold)
- **Form 05-102 filing status** — Form 05-102 (No Tax Due Report) filed or flagged for filing
- **PIR accuracy** — Public Information Report (PIR) data current and accurate
- **Franchise tax filing deadline** — Filing deadline: May 15, 2026 (for Dec 31 year-end)
- **Above threshold — Form 05-158 revenue line** — Total revenue → Form 05-158 (Texas Franchise Tax Report) Line 1
- **Margin computation** — Total revenue minus greatest of (COGS, compensation, 30% of revenue, $1M)
- **Apportionment factor** — Texas receipts / total receipts (if applicable)
- **Taxable margin flow** — Taxable margin → Form 05-158 applicable line
- **Margin tax rate above threshold — other** — 0.75% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **Margin tax rate above threshold — retail/wholesale** — 0.375% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **Franchise tax due computation** — Franchise tax due
- **EZ Computation comparison** — 0.331% × apportioned total revenue — determine if lower (Form 05-169)
- **Franchise tax payments and credits** — Franchise tax payments and credits
- **Total revenue definition for TX franchise tax** — Per Texas Tax Code §171.1011, total revenue includes: Gross receipts from Schedule C (federal); Other income items per IRC §61 that are not specifically excluded. Excludes: flow-through funds that are not revenue to the entity, certain pass-through distributions.  _(Texas Tax Code §171.1011)_
- **Cross-check between Schedule C and TX total revenue** — Schedule C Line 1 (gross receipts) should approximate total revenue reported on TX franchise tax return. Differences may arise from: Returns and allowances (Schedule C Line 2); Income items not on Schedule C (interest, other income); Items excluded from TX total revenue by statute.

### Texas sales tax consistency (if applicable)

- **Taxable sales reporting match** — Taxable sales reported on sales tax returns match invoices/receipts for taxable items
- **Sales tax collected matches deposits** — Sales tax collected matches deposits in bank statement
- **Sales tax remitted matches Comptroller payments** — Sales tax remitted matches Comptroller payments
- **Filing frequency correct** — Filing frequency correct (monthly/quarterly/annually)
- **No unfiled periods** — No unfiled periods with active permit
- **Zero returns filing** — If no taxable sales and permit is active: $0 returns filed

### Federal estimated tax verification

- **Quarterly payments verified** — Four quarterly payments verified against bank statement / EFTPS records
- **Safe harbor analysis** — Safe harbor analysis: 100% of 2024 tax (if 2024 AGI ≤ $150K) or 110% of 2024 tax (if 2024 AGI > $150K)
- **Underpayment penalty** — If underpaid: Form 2210 penalty computed
- **No state estimated tax note** — Note: no state estimated tax exists in Texas — only federal

### No state income tax deduction on federal return

- **No deduction of TX state income tax** — Texas residents cannot deduct state income tax on federal Schedule A (because there is none). However: Texas sales tax paid can be deducted on Schedule A Line 5a (state and local general sales tax) as an alternative to state income tax; IRS provides optional sales tax tables or taxpayer can use actual records; For 2025: SALT deduction cap remains $10,000 ($5,000 MFS) — may limit benefit
- **SALT deduction cap 2025** — 10,000 USD ($5,000 MFS)

### Franchise tax interaction with federal positions

- **QBI no TX interaction** — QBI deduction (§199A): No Texas equivalent or interaction. QBI is purely federal.
- **Depreciation used for COGS** — Depreciation: Texas franchise tax uses federal depreciation for COGS computation. No state-level depreciation difference.
- **Retirement contributions not relevant** — Retirement contributions: Not relevant to franchise tax (franchise tax is on revenue/margin, not personal deductions).

### Texas LLC annual obligations

- **No annual franchise tax payment below threshold** — No annual franchise tax payment for entities below threshold — only the No Tax Due Report filing
- **Public Information Report (PIR)** — Must be filed annually with the franchise tax report. Lists registered agent, principal office, officers/directors/managers.
- **Secretary of State annual report** — No annual report filing fee in Texas (unlike many states). LLC maintains standing as long as franchise tax report is filed.
- **Registered agent requirement** — Must maintain a registered agent in Texas. Failure results in administrative forfeiture.

### Forfeiture risk

- **Forfeiture process** — If a Texas LLC fails to file the franchise tax report (even the No Tax Due Report): Texas Comptroller notifies the entity; After notice period, Comptroller certifies forfeiture to Secretary of State; Secretary of State forfeits the entity's right to transact business; Reinstatement requires filing all delinquent reports + paying penalties and fees; Flag for reviewer if any prior filings were missed

## Section 5 — Refusals

- **R-TX-1** — Upstream skill did not run. Name the specific skill.
- **R-TX-2** — Revenue exceeds $2.47M and margin computation is complex. If COGS includes items requiring IRC §263A UNICAP analysis or compensation includes complex benefit allocations, flag for franchise tax specialist.
- **R-TX-3** — Multi-state apportionment needed. If the entity has receipts from customers outside Texas and performs services in multiple states, Texas apportionment factor requires analysis. Flag for reviewer.
- **R-TX-4** — Sales tax audit or dispute. If the taxpayer has received a sales tax audit notice or is in dispute with the Comptroller, refuse and recommend sales tax attorney.
- **R-TX-5** — Combined group reporting. If the SMLLC is part of a combined group for Texas franchise tax purposes, refuse. Combined group reporting requires specialized computation.

### Documents

1. **Executive summary** — filing status, income, federal tax, franchise tax status, sales tax status, total liability, refund/balance due
2. **Federal Form 1040 worksheet** — line-by-line
3. **Schedule C** — sole prop P&L
4. **Schedule SE** — SE tax
5. **Schedule 1, 2, 3** — adjustments, additional taxes, credits
6. **Form 8995 or 8995-A** — QBI
7. **Form 2210** — federal underpayment penalty (if applicable)
8. **Form 1040-ES** — 2026 federal estimated tax schedule
9. **Texas franchise tax worksheet:**
   - Total revenue computation
   - Threshold determination ($2.47M)
   - If below threshold: Form 05-102 data (entity name, SOS file number, NAICS code, principal office, registered agent)
   - If above threshold: margin computation, rate determination, tax due
10. **Texas sales tax compliance summary** (if applicable):
    - Permit number and filing frequency
    - Taxable vs exempt sales analysis
    - Sales tax collected and remitted by period
    - Outstanding returns (if any)
11. **1099-NEC batch** — contractor information returns
12. **Reviewer brief** — comprehensive narrative
13. **Taxpayer action list** — deadlines, amounts, payment methods

### Reviewer brief structure

```markdown
# Complete Return Package: [Taxpayer Name] — Tax Year 2025

## Executive Summary
- Filing status: [X]
- Residence: Texas
- Business: Sole proprietor / SMLLC disregarded
- Federal total tax: $X
- Texas franchise tax: $0 (below threshold) OR $X
- Texas sales tax remitted: $X (if applicable)
- Total 2025 federal tax liability: $X
- Total federal payments: $X
- Federal refund or balance due: $X
- No state income tax (Texas)

## Federal Return
[Federal assembly content]

## Texas Franchise Tax
- Entity: [LLC name] (SOS file number: XXXXXXXXXX)
- Accounting year end: December 31, 2025
- Total revenue: $X
- No-tax-due threshold: $2,470,000
- Status: [Below threshold — No Tax Due / Above threshold — tax of $X due]
- Filing: Form 05-102 (No Tax Due) + Public Information Report
- Due date: May 15, 2026
- Extension available: November 15, 2026

## Texas Sales Tax (if applicable)
- Permit: [number] / Filing frequency: [monthly/quarterly/annually]
- Taxable sales: $X
- Tax collected: $X
- Tax remitted: $X
- Outstanding returns: [none / list]
- Recommendation: [continue permit / close permit if no taxable sales]

## Federal Estimated Tax (2026)
- No state estimated tax required (Texas has no income tax)
- Federal safe harbor amount: $X
- Recommended quarterly payments: $X per quarter
- Due dates: April 15, June 16, September 15, January 15

## Cross-jurisdiction reconciliation
- Schedule C gross receipts align with TX franchise tax total revenue: [verified]
- Federal estimated payments verified against EFTPS records: [verified]
- Sales tax collected matches bank deposits: [verified, if applicable]

## Reviewer attention flags
[Aggregated flags]

## Positions taken
[With citations to IRC, Texas Tax Code]

## Planning notes for 2026
- Monitor revenue against $2.47M franchise tax threshold
- S-corp election consideration (reduces SE tax; franchise tax treatment changes)
- Franchise tax EZ Computation vs Long Form comparison if approaching threshold
- Sales tax permit maintenance or closure
- Consider SALT deduction: sales tax vs $0 income tax on federal Schedule A
```

## Executive Summary

- Filing status: [X]
- Residence: Texas
- Business: Sole proprietor / SMLLC disregarded
- Federal total tax: $X
- Texas franchise tax: $0 (below threshold) OR $X
- Texas sales tax remitted: $X (if applicable)
- Total 2025 federal tax liability: $X
- Total federal payments: $X
- Federal refund or balance due: $X
- No state income tax (Texas)

## Federal Return

[Federal assembly content]

## Texas Franchise Tax

- Entity: [LLC name] (SOS file number: XXXXXXXXXX)
- Accounting year end: December 31, 2025
- Total revenue: $X
- No-tax-due threshold: $2,470,000
- Status: [Below threshold — No Tax Due / Above threshold — tax of $X due]
- Filing: Form 05-102 (No Tax Due) + Public Information Report
- Due date: May 15, 2026
- Extension available: November 15, 2026

## Texas Sales Tax (if applicable)

- Permit: [number] / Filing frequency: [monthly/quarterly/annually]
- Taxable sales: $X
- Tax collected: $X
- Tax remitted: $X
- Outstanding returns: [none / list]
- Recommendation: [continue permit / close permit if no taxable sales]

## Federal Estimated Tax (2026)

- No state estimated tax required (Texas has no income tax)
- Federal safe harbor amount: $X
- Recommended quarterly payments: $X per quarter
- Due dates: April 15, June 16, September 15, January 15

## Cross-jurisdiction reconciliation

- Schedule C gross receipts align with TX franchise tax total revenue: [verified]
- Federal estimated payments verified against EFTPS records: [verified]
- Sales tax collected matches bank deposits: [verified, if applicable]

## Reviewer attention flags

[Aggregated flags]

## Positions taken

[With citations to IRC, Texas Tax Code]

## Planning notes for 2026

- Monitor revenue against $2.47M franchise tax threshold
- S-corp election consideration (reduces SE tax; franchise tax treatment changes)
- Franchise tax EZ Computation vs Long Form comparison if approaching threshold
- Sales tax permit maintenance or closure
- Consider SALT deduction: sales tax vs $0 income tax on federal Schedule A

## Section 7 — Taxpayer action list structure

```markdown
## Taxpayer Action List

### Before April 15, 2026:
1. Review and sign federal return package
2. Pay federal balance due: $X via EFTPS / IRS Direct Pay
3. Pay 2026 Q1 federal estimated tax: $X via EFTPS
4. No state income tax payment required (Texas)

### Before May 15, 2026:
1. File Texas franchise tax report:
   - Form 05-102 (No Tax Due Report) — if total revenue ≤ $2.47M
   - OR Form 05-158/05-169 — if total revenue > $2.47M with payment of $X
2. File Public Information Report (PIR) with franchise tax report
3. File online at Texas Comptroller WebFile: https://comptroller.texas.gov/taxes/franchise/

### Before June 16, 2026:
1. Pay 2026 Q2 federal estimated tax: $X via EFTPS

### Before September 15, 2026:
1. Pay 2026 Q3 federal estimated tax: $X via EFTPS

### Before January 15, 2027:
1. Pay 2026 Q4 federal estimated tax: $X via EFTPS

### Sales tax (if applicable — ongoing):
1. File sales tax returns per assigned frequency ([monthly/quarterly/annually])
2. Remit collected sales tax to Texas Comptroller by the 20th of the month following the reporting period
3. If filing timely: claim 0.5% timely filing discount (capped at $500/month)

### Ongoing:
1. Collect W-9 from new contractors before payment
2. Track business expenses with receipts
3. Monitor total revenue against $2.47M franchise tax threshold
4. Maintain registered agent for LLC
5. Consider S-corp election analysis if net SE income exceeds $150K+
6. Federal SALT deduction: keep receipts for sales tax paid on large purchases (potential Schedule A deduction)
```

### Before April 15, 2026:

1. Review and sign federal return package
2. Pay federal balance due: $X via EFTPS / IRS Direct Pay
3. Pay 2026 Q1 federal estimated tax: $X via EFTPS
4. No state income tax payment required (Texas)

### Before May 15, 2026:

1. File Texas franchise tax report:
   - Form 05-102 (No Tax Due Report) — if total revenue ≤ $2.47M
   - OR Form 05-158/05-169 — if total revenue > $2.47M with payment of $X
2. File Public Information Report (PIR) with franchise tax report
3. File online at Texas Comptroller WebFile: https://comptroller.texas.gov/taxes/franchise/

### Before June 16, 2026:

1. Pay 2026 Q2 federal estimated tax: $X via EFTPS

### Before September 15, 2026:

1. Pay 2026 Q3 federal estimated tax: $X via EFTPS

### Before January 15, 2027:

1. Pay 2026 Q4 federal estimated tax: $X via EFTPS

### Sales tax (if applicable — ongoing):

1. File sales tax returns per assigned frequency ([monthly/quarterly/annually])
2. Remit collected sales tax to Texas Comptroller by the 20th of the month following the reporting period
3. If filing timely: claim 0.5% timely filing discount (capped at $500/month)

### Ongoing:

1. Collect W-9 from new contractors before payment
2. Track business expenses with receipts
3. Monitor total revenue against $2.47M franchise tax threshold
4. Maintain registered agent for LLC
5. Consider S-corp election analysis if net SE income exceeds $150K+
6. Federal SALT deduction: keep receipts for sales tax paid on large purchases (potential Schedule A deduction)

## Section 8 — Self-checks

**Check TX-A1 — All upstream skills executed.**
**Check TX-A2 — Federal return internally consistent (all flow-through lines verified).**
**Check TX-A3 — Texas franchise tax total revenue computed and compared to $2.47M threshold.**
**Check TX-A4 — Franchise tax filing obligation identified (Form 05-102 or 05-158/05-169).**
**Check TX-A5 — Sole prop without LLC correctly excluded from franchise tax (only LLCs file).**
**Check TX-A6 — Sales tax applicability evaluated (custom software exempt vs SaaS/canned software taxable).**
**Check TX-A7 — No state estimated tax referenced (Texas has no income tax).**
**Check TX-A8 — Federal estimated tax safe harbor correctly applied (110% if AGI > $150K).**
**Check TX-A9 — May 15 franchise tax deadline included in action items.**
**Check TX-A10 — SALT deduction evaluated: sales tax deduction on Schedule A vs zero state income tax.**
**Check TX-A11 — LLC forfeiture risk assessed (are prior franchise tax reports current?).**

## Section 9 — Output files

Three files:

1. **`[taxpayer_slug]_2025_master.xlsx`** — Sheets: Cover, Income, Schedule C, Schedule SE, Retirement, SE Health, QBI, Schedule 1, Form 1040, Form 2210, TX Franchise Tax, TX Sales Tax (if applicable), 1099-NEC batch, 2026 Federal Est Tax.

2. **`reviewer_brief.md`** — Full narrative covering federal return, Texas franchise tax, Texas sales tax, cross-jurisdiction reconciliation, flags, citations, planning notes.

3. **`taxpayer_action_list.md`** — Step-by-step with dates, amounts, and payment URLs (EFTPS for federal, Texas Comptroller WebFile for franchise/sales tax).

## Section 10 — Known gaps

1. Texas franchise tax margin computation for entities above $2.47M requires detailed COGS or compensation analysis not fully automated
2. Sales tax nexus analysis for e-commerce/SaaS businesses requires fact-specific determination per Texas Comptroller rules
3. Texas R&D credit (franchise tax credit) analysis not included — available for qualifying research activities
4. Combined group reporting for entities under common ownership not supported
5. Texas economic development incentives (Chapter 313, enterprise zones) not evaluated
6. Franchise tax extension (to November 15) requires 90% of tax paid by May 15 if tax is due

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
