---
name: in-return-assembly
description: Final orchestrator skill that assembles the complete India filing package for India-resident self-employed individuals and professionals. Consumes outputs from all India content skills (india-gst for GSTR-3B/GSTR-1, in-income-tax for ITR-3/ITR-4, in-advance-tax for quarterly instalments, in-tds-freelance for TDS reporting) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all India content skills listed above. India full-year residents only. Self-employed individuals and professionals only.
version: 0.1
---

# India Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `in-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires CA signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for India self-employed returns. Every India content skill feeds into this one. The output is the complete reviewer package that a Chartered Accountant can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete India filing package for:
- Full-year Indian residents
- Self-employed individuals and professionals (sole proprietors)
- Financial year 2025-26 (Assessment year 2026-27)
- Filing GST returns (GSTR-3B + GSTR-1 if registered), ITR-3 or ITR-4, advance tax reconciliation, TDS credit reconciliation

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`india-gst`** -- GSTR-3B + GSTR-1 reconciliation (Q2 skill)
   - Runs first because GST turnover figures feed into the ITR
   - Reconcile GSTR-3B monthly/quarterly summaries with books
   - Verify GSTR-1 outward supply details match invoices
   - Reconcile ITC claimed with GSTR-2B auto-populated data
   - Output: GST turnover, output tax, ITC utilised, cash GST paid, reverse charge

2. **`in-income-tax`** -- ITR-3 or ITR-4 return (Q2 skill)
   - Depends on GST output: gross receipts must match GST turnover (ex-GST for regular taxpayer)
   - For ITR-4 (presumptive 44ADA): 50% deemed profit on gross receipts, no expense schedule
   - For ITR-3 (actual profit): full P&L with expense deductions, depreciation schedule, balance sheet
   - Output: total income, tax liability at applicable slab rates, regime comparison if requested

3. **`in-advance-tax`** -- Quarterly advance tax reconciliation (Q2 skill)
   - Depends on ITR: final tax liability determines whether advance tax was sufficient
   - Reconcile advance tax paid (from Form 26AS) against liability
   - Compute s.234B interest (default on advance tax shortfall -- if paid < 90% of assessed tax)
   - Compute s.234C interest (deferment -- quarterly shortfall in instalments: 15%/45%/75%/100%)
   - Output: advance tax schedule, shortfall computation, interest liability

4. **`in-tds-freelance`** -- TDS credit reconciliation (Q4 stub, flag)
   - Depends on ITR: TDS credits offset final tax liability
   - Reconcile Form 26AS TDS entries with income declared in ITR
   - Flag mismatches (TDS claimed but income not shown, or income shown but TDS not reflected)
   - **Status check:** in-tds-freelance is currently a Q4 stub. If the stub has substantive content, use it. If it is still a placeholder, compute TDS reconciliation using Form 26AS data from intake and flag in the reviewer brief that the dedicated skill was not available.
   - Output: TDS credit summary, mismatches, Form 26AS vs ITR reconciliation

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: GST turnover matches ITR gross receipts

| GST Output | ITR Input | Rule |
|-----------|-----------|------|
| GSTR-3B aggregate turnover (ex-GST) | ITR gross receipts from profession/business | Must match within INR 100 |
| GSTR-1 outward supplies | ITR Schedule BP / presumptive turnover | Turnover is ex-GST for regular registrants |
| Export of services (zero-rated) | ITR foreign income | Included in gross receipts, zero-rated for GST |

**If mismatch:** Flag for reviewer. Common causes: timing differences (invoice vs receipt basis), RCM supplies, credit notes, advances received but service not rendered.

### Cross-check 2: If 44ADA presumptive -- 50% deemed profit, no further expense deduction allowed

| Rule | Application |
|------|------------|
| Deemed profit = 50% of gross receipts | No deduction for actual expenses against professional income |
| Depreciation | NOT claimable under presumptive scheme |
| Partner remuneration / interest | Not applicable (sole proprietor) |
| Deductions under Ch VI-A (80C, 80D) | Still allowed (old regime) or standard deduction (new regime) -- these are from total income, not business income |

**If violation:** If the computation claims actual expenses AND declares 50% deemed profit, check fails. It is one or the other.

### Cross-check 3: Advance tax paid + TDS credits against final tax liability

| Component | Source | Rule |
|-----------|--------|------|
| Advance tax paid | Form 26AS Part C / challans | Sum of all advance tax payments during FY |
| TDS credits | Form 26AS Part A / TDS certificates | Sum of all TDS deducted and deposited |
| Self-assessment tax (if any) | Challan 280 | Paid before filing ITR |
| Total tax liability | ITR computation | Tax on total income + surcharge + cess |
| Tax payable / refund | Liability minus (advance tax + TDS + self-assessment) | Positive = payable; negative = refund |

**If advance tax + TDS < 90% of assessed tax:** s.234B interest applies at 1% per month (simple) from April of AY to date of filing or date of assessment.

**If quarterly advance tax instalments fell short:** s.234C interest applies at 1% per month for 3 months per shortfall quarter.

| Quarter | Due date | Cumulative % required |
|---------|----------|-----------------------|
| Q1 | 15 June | 15% |
| Q2 | 15 September | 45% |
| Q3 | 15 December | 75% |
| Q4 | 15 March | 100% |

For 44ADA presumptive: entire advance tax can be paid by 15 March (single instalment). s.234C does not apply if 100% paid by 15 March.

### Cross-check 4: Form 26AS TDS vs ITR income declaration

| Check | Rule |
|-------|------|
| Every TDS entry in 26AS Part A | Corresponding income must appear in ITR |
| TDS credit claimed in ITR | Must match 26AS (or AIS) within INR 1 |
| Mismatch entries | Flag: either TDS not deposited by deductor, or income not declared |
| TCS entries (26AS Part C) | If applicable, credit against tax liability |

**If mismatch:** Common causes: deductor filed TDS return late, wrong PAN quoted, income accounted in different FY. Flag for reviewer with specific entries.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, income, tax liability, GST position, advance tax, TDS credits, refund/balance due
2. **GST reconciliation worksheet** -- GSTR-3B vs books, GSTR-1 vs invoices, ITC reconciliation
3. **ITR computation worksheet** -- ITR-3 or ITR-4 schedule with all heads of income, deductions, tax computation
4. **Depreciation schedule** -- asset register with block, cost, date, rate, annual allowance, WDV (ITR-3 only)
5. **Advance tax reconciliation** -- quarterly payments vs requirement, s.234B/234C interest computation
6. **TDS credit reconciliation** -- Form 26AS vs ITR, mismatches flagged
7. **Cross-skill reconciliation summary** -- all four cross-checks with pass/fail and notes
8. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
9. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- FY 2025-26 (AY 2026-27)

## Executive Summary
- Filing status: [Individual -- Resident]
- Age category: [Below 60 / Senior / Super Senior]
- Business: Self-employed professional / sole proprietor
- Tax regime: [New regime / Old regime]
- Presumptive: [44ADA / 44AD / Actual profit (ITR-3)]
- ITR form: [ITR-3 / ITR-4]
- GST registration: [Regular / Composition / Unregistered]
- Gross receipts: INR X
- Deemed profit (if 44ADA) / Net profit (if ITR-3): INR X
- Total income: INR X
- Tax liability (including surcharge + cess): INR X
- Advance tax paid: INR X
- TDS credits: INR X
- Self-assessment tax paid: INR X
- Balance due / refund: INR X
- s.234B interest (if any): INR X
- s.234C interest (if any): INR X
- GST annual position: Output INR X, ITC INR X, cash paid INR X

## GST Returns
[Content from india-gst output]
- Registration type and state
- Monthly/quarterly GSTR-3B summary
- GSTR-1 outward supply reconciliation
- ITC claimed vs GSTR-2B auto-populated
- Reverse charge liability
- Zero-rated exports reconciliation
- Annual aggregate turnover

## Income Tax Return (ITR-3 / ITR-4)
[Content from in-income-tax output]
- Gross receipts from profession/business
- Deemed profit (44ADA) or actual P&L (ITR-3)
- Depreciation schedule (ITR-3 only)
- Income under other heads (interest, capital gains, etc.)
- Deductions under Chapter VI-A (old regime) or standard deduction (new regime)
- Total income
- Tax at applicable slab rates
- Surcharge (if total income > INR 50 lakh)
- Health and education cess (4%)
- Relief under s.87A (if total income <= INR 12,00,000 new regime)
- Total tax liability

## Advance Tax Reconciliation
[Content from in-advance-tax output]
- Quarterly advance tax payments made (dates and amounts)
- Required quarterly cumulative percentages (15/45/75/100)
- Shortfall computation per quarter
- s.234B interest computation (if advance tax < 90% of assessed tax)
- s.234C interest computation (if quarterly shortfall)
- Total interest payable

## TDS Credit Reconciliation
[Content from in-tds-freelance output or computed from Form 26AS]
- Deductor-wise TDS summary
- Section-wise TDS summary (194J, 194C, etc.)
- Form 26AS vs ITR reconciliation
- Mismatches and resolution notes
- TCS credits (if any)

## Cross-skill Reconciliation
- GST turnover vs ITR gross receipts: [pass/fail]
- 44ADA deemed profit -- no expense deduction: [pass/fail or N/A]
- Advance tax + TDS vs final liability: [pass/fail]
- Form 26AS TDS vs ITR income: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- Tax regime choice (old vs new) -- confirmation needed
- 44ADA lock-in implications if switching from/to presumptive
- Mixed-use expense percentages (phone, internet)
- Home office deduction (if claimed under ITR-3)
- Export of services zero-rating -- FIRC verification
- PAN-Aadhaar linkage status
- s.234B/234C interest exposure
- GST registration threshold monitoring (if approaching INR 20 lakh)
- Any high-value transactions flagged in AIS

## Positions Taken
[List with legislation citations]
- e.g., "Presumptive taxation under s.44ADA of the Income-tax Act, 1961 -- gross receipts INR 38,00,000 (below INR 75,00,000 threshold for digital receipts > 95%)"
- e.g., "New tax regime elected under s.115BAC -- no Chapter VI-A deductions claimed"
- e.g., "Export of services to USA -- zero-rated supply under s.16(1) IGST Act, LUT filed"
- e.g., "Laptop capitalised at INR 1,20,000 -- 40% depreciation under Block III (computers), IT Act 6th Schedule" (ITR-3 only)

## Planning Notes for FY 2026-27
- Advance tax schedule (quarterly instalments with amounts and dates)
- GST compliance calendar (monthly GSTR-3B, quarterly GSTR-1 if QRMP)
- 44ADA lock-in tracking (years remaining if opted in)
- Depreciation schedule continuing into next FY (WDV)
- Regime choice review (new vs old) based on projected income
- Any legislative changes in Union Budget 2026 affecting self-employed

## Client Action List

### Immediate (before 31 July 2026 -- ITR filing deadline):
1. Review this return package with your Chartered Accountant
2. Pay self-assessment tax of INR X via Challan 280 (if balance due)
3. File ITR on incometax.gov.in
4. E-verify ITR within 30 days of filing (Aadhaar OTP / net banking / DSC)

### If tax audit required (s.44AB -- turnover > INR 1 crore, or profit < presumptive threshold):
1. Tax audit report in Form 3CB-3CD due by 30 September 2026
2. ITR filing deadline extends to 31 October 2026

### Advance tax for FY 2026-27:
1. 15 June 2026: 1st instalment -- 15% of estimated tax = INR X
2. 15 September 2026: 2nd instalment -- cumulative 45% = INR X
3. 15 December 2026: 3rd instalment -- cumulative 75% = INR X
4. 15 March 2027: 4th instalment -- cumulative 100% = INR X
(If 44ADA: can pay 100% by 15 March 2027 in single instalment)

### GST filing calendar:
- GSTR-3B: 20th of following month (or quarterly if QRMP scheme)
- GSTR-1: 11th of following month (or quarterly if QRMP)
- GSTR-9 (annual): 31 December 2027

### Ongoing:
1. Issue GST-compliant tax invoices for all taxable supplies
2. Maintain books of account (if ITR-3) or preserve records (if 44ADA)
3. File GSTR-3B and GSTR-1 monthly/quarterly
4. Pay advance tax on quarterly due dates
5. Collect and file Form 16A (TDS certificates) from clients
6. Monitor aggregate turnover for GST registration threshold
7. Retain all invoices and financial records for 6 years (IT Act) / 6 years (GST Act)
```

---

## Section 5 -- Refusals

**R-IN-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-IN-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-IN-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-IN-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-IN-5 -- Out-of-scope item discovered during assembly.** E.g., capital gains requiring Schedule CG, rental income requiring Schedule HP, foreign assets requiring Schedule FA, or partnership income. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check IN-A1 -- All upstream skills executed.** india-gst, in-income-tax, in-advance-tax all produced output. in-tds-freelance produced output or was computed from Form 26AS data.

**Check IN-A2 -- GST turnover matches ITR gross receipts.** Within INR 100 tolerance.

**Check IN-A3 -- If 44ADA: 50% deemed profit, no expense deductions claimed.** Deemed profit = exactly 50% of gross receipts (or higher if voluntarily declared higher).

**Check IN-A4 -- Advance tax + TDS reconciled against final liability.** Total credits (advance tax + TDS + self-assessment tax) match the payment/refund position.

**Check IN-A5 -- s.234B interest computed correctly.** If advance tax paid < 90% of assessed tax, 1% simple interest per month from April AY to date of payment/assessment.

**Check IN-A6 -- s.234C interest computed correctly.** Quarterly shortfall interest at 1% for 3 months per deficient quarter.

**Check IN-A7 -- Form 26AS TDS matches ITR.** Every TDS entry in 26AS has corresponding income in ITR. Credits claimed match 26AS amounts.

**Check IN-A8 -- Tax regime correctly applied.** New regime: s.115BAC rates, no Ch VI-A deductions (except NPS 80CCD(2)). Old regime: regular slab rates, all deductions claimed.

**Check IN-A9 -- s.87A rebate applied if eligible.** New regime: if total income <= INR 12,00,000 (after standard deduction), rebate up to INR 25,000.

**Check IN-A10 -- Surcharge and cess correctly computed.** Surcharge applicable if total income > INR 50 lakh (10%/15%/25% tiers). Cess = 4% on tax + surcharge.

**Check IN-A11 -- Filing calendar is complete.** All deadlines for ITR, GST, advance tax, and TDS are listed with specific dates and amounts.

**Check IN-A12 -- Reviewer brief contains legislation citations.** Every position taken references the specific section of the Income-tax Act 1961, CGST Act 2017, or relevant rule.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025-26_india_master.xlsx`** -- Single master workbook containing every worksheet and computation. Sheets include: Cover, GST Reconciliation (GSTR-3B vs books), ITR Computation (ITR-3 or ITR-4), Depreciation Schedule (if ITR-3), Advance Tax Reconciliation, TDS Credit Reconciliation, s.234B/234C Interest, Cross-Check Summary. Use live formulas where possible -- e.g., ITR gross receipts cell references the GST turnover cell; advance tax shortfall references the ITR final liability. Verify no `#REF!` errors. Verify computed values match within INR 1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, GST returns, ITR, advance tax, TDS, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, advance tax quarterly calendar for FY 2026-27, GST filing calendar, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `in-freelance-intake` -- structured intake package (JSON)
- `india-gst` -- GSTR-3B/GSTR-1 reconciliation output
- `in-income-tax` -- ITR-3/ITR-4 computation output
- `in-advance-tax` -- Advance tax reconciliation and interest output
- `in-tds-freelance` -- TDS credit reconciliation output (or fallback computation from Form 26AS)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official ITR forms on incometax.gov.in.
2. E-filing is handled by the reviewer via the income tax portal, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. Tax audit (Form 3CB-3CD) preparation is not automated -- if audit is required, the skill flags it and the CA prepares the audit report separately.
5. in-tds-freelance is a Q4 stub. Until it is fleshed out, TDS reconciliation is computed using Form 26AS data from intake. This is a redundancy, not a gap -- the data source (Form 26AS) is the same.
6. Multi-year depreciation tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
7. Capital gains computation (Schedule CG) is out of scope.
8. Foreign assets reporting (Schedule FA) is out of scope.
9. Rental income (Schedule HP) is out of scope beyond noting it as other income.
10. The package is complete only for FY 2025-26; FY 2026-27 appears only as prospective planning.
11. State-level professional tax varies by state and is treated as a known deduction from intake, not independently computed.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for India jurisdiction with four content skills (GST, ITR, advance tax, TDS).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
