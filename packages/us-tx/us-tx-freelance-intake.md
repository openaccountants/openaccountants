---
name: us-tx-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their US federal tax return AND mentions freelancing, self-employment, software development, contracting, sole proprietorship, or a single-member LLC in Texas. Trigger on phrases like "I'm a freelancer in Texas", "Texas self-employed taxes", "I have an LLC in TX", "Houston contractor tax return", "Austin freelance developer", or any similar phrasing where the user is a Texas-resident freelancer needing tax return preparation. This is the REQUIRED entry point for the Texas freelance developer tax workflow. Texas has no state income tax but has franchise tax and sales tax obligations. Uses upload-first workflow and ask_user_input_v0 for structured questions. Texas residents only. Sole proprietors and single-member LLCs disregarded for federal tax only.
version: 1.0
jurisdiction: US-TX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Tx Freelance Intake

## Section 1 — The opening

When triggered, respond with ONE message that:

1. One-line greeting
2. One-line summary of the flow (scope check → upload → gaps → handoff)
3. One-line note: Texas has no income tax, so this focuses on federal + TX franchise tax + TX sales tax compliance
4. One-line reviewer reminder
5. Launch the refusal sweep immediately

**Example first message:**

> Let's get your 2025 federal return ready. Texas doesn't have a state income tax, so we'll focus on federal plus Texas franchise tax and sales tax compliance. Quick scope check, then documents, then gaps. Target: 10 minutes.
>
> Reminder: everything I produce needs signoff from a credentialed tax professional before filing.
>
> Scope check:

Then immediately call `ask_user_input_v0`.

## Section 2 — Refusal sweep

First batch:

```
Q1: "Business structure?"
    Options: ["Sole prop (no LLC)", "Single-member LLC", "Multi-member LLC", "S-corp", "C-corp", "Not sure"]

Q2: "Revenue range for 2025?"
    Options: ["Under $250K", "$250K–$1M", "$1M–$2.47M", "Over $2.47M"]

Q3: "Filing status?"
    Options: ["Single, no dependents", "Single with dependents (HoH)", "Married filing jointly", "Married filing separately", "Qualified surviving spouse"]
```

**Evaluate:**

- **Q1 = Sole prop or Single-member LLC** → continue
- **Q1 = Multi-member LLC** → stop. "Multi-member LLCs file Form 1065 as partnerships. Texas franchise tax for partnerships adds complexity. You need a CPA."
- **Q1 = S-corp or C-corp** → stop. "Corporate returns (1120-S, 1120) plus Texas franchise tax margin computation for entities require a CPA."
- **Q1 = Not sure** → follow-up: "Did you file Form 2553 or receive a W-2 from your own business?"

- **Q2** → record for franchise tax analysis:
  - Under $250K → almost certainly below no-tax-due threshold ($2.47M), minimal franchise tax concerns
  - $250K–$1M → below threshold, no franchise tax but must still file Form 05-102 (No Tax Due Report) if the entity exists
  - $1M–$2.47M → below threshold, still file Form 05-102
  - Over $2.47M → franchise tax applies, flag for detailed computation

- **Q3** → record filing status

**Second batch:**

```
Q4: "Do you have a Texas sales tax permit?"
    Options: ["Yes, active permit", "No permit", "Had one but closed it", "Not sure if I need one"]

Q5: "Did you file a 2024 return normally?"
    Options: ["Yes", "No (skipped year)", "Yes but amended / under audit"]

Q6: "Any of these in 2025?" (multi-select)
    Options: [
      "Rental property income",
      "Active crypto/day trading",
      "Foreign bank account over $10K",
      "W-2 employees on payroll",
      "Income from clients in other states where you traveled to perform work",
      "None of the above"
    ]

Q7: "Federal estimated tax payments made in 2025?"
    Options: ["Yes, all 4 quarters", "Yes, some quarters", "No", "Not sure"]

Q8: "Texas franchise tax: does your total revenue exceed $2.47 million?"
    Options: ["No, well under $2.47M", "Close to the threshold", "Yes, over $2.47M", "Not sure"]
```

**Evaluate Q4:**
- Yes, active permit → flag for sales tax compliance review
- No permit → evaluate if one is needed (see Section 7 below)
- Had one but closed → confirm no outstanding returns
- Not sure → ask follow-up about whether taxpayer sells taxable goods/services

**Evaluate Q5:**
- Yes → continue
- No or under audit → stop. Recommend CPA.

**Evaluate Q6:**
- Any of first five selected → stop with appropriate refusal
- "None of the above" → continue

**Evaluate Q7:** Record for federal estimated tax analysis.

**Evaluate Q8:**
- No, well under → no franchise tax due, but may still need to file Form 05-102
- Close to threshold → flag for careful revenue calculation
- Yes, over → franchise tax computation required, flag for detailed margin analysis
- Not sure → will determine from documents

**Refusal for out-of-state income:**
> Stop — you performed work in other states. Even though Texas has no income tax, the other states may claim you owe income tax there (economic nexus for services). You need a CPA who handles multi-state filing obligations.

- **Refusal: Multi-member LLC** — Multi-member LLCs file Form 1065 as partnerships. Texas franchise tax for partnerships adds complexity. You need a CPA.  _(Section 2 — Refusal sweep, Q1 evaluation)_
- **Refusal: S-corp or C-corp** — Corporate returns (1120-S, 1120) plus Texas franchise tax margin computation for entities require a CPA.  _(Section 2 — Refusal sweep, Q1 evaluation)_
- **Refusal: 2024 return not filed normally or under audit** — stop. Recommend CPA.  _(Section 2 — Refusal sweep, Q5 evaluation)_
- **Refusal: Out-of-state income items in Q6** — Any of first five selected → stop with appropriate refusal  _(Section 2 — Refusal sweep, Q6 evaluation)_
- **Refusal: out-of-state income** — Stop — you performed work in other states. Even though Texas has no income tax, the other states may claim you owe income tax there (economic nexus for services). You need a CPA who handles multi-state filing obligations.  _(Section 2 — Refusal sweep)_

## Section 3 — The dump

> Scope is good. Upload everything you have for 2025:
>
> - Business bank statement(s) for 2025 (CSV or PDF)
> - Tax forms received (1099-NEC, 1099-MISC, 1095-A/B/C)
> - Year-end retirement account statements
> - Federal estimated tax payment confirmations
> - Your 2024 federal tax return
> - Texas franchise tax correspondence or prior filings (Form 05-102 or 05-158/05-169)
> - Texas sales tax permits or returns (if applicable)
> - LLC Certificate of Formation (if applicable, filed with TX Secretary of State)
> - Texas Comptroller correspondence
> - Anything else tax-related
>
> Drop it all in — I'll sort it out.

## Section 4 — The inference pass

Parse all documents and extract:

**Bank statement:**
- Total deposits (gross receipts — critical for franchise tax threshold)
- Client payments with names
- IRS EFTPS payments (federal estimated tax)
- Retirement contributions
- Health insurance premiums
- Business expenses
- Contractor payments
- Texas Comptroller payments (franchise tax, sales tax)
- Texas Secretary of State fees ($300 LLC formation / $0 annual)

**1099-NEC received:**
- Payer name, TIN, Box 1 amount
- Cross-check against deposits

**Prior year federal return:**
- Federal total tax (1040 Line 24)
- Federal AGI (1040 Line 11)

**Texas franchise tax prior filings:**
- Prior year filing type (No Tax Due, EZ Computation, Long Form)
- Prior year total revenue reported
- Entity type on file with Comptroller

**Retirement account statement:**
- Plan type, contributions, dates

## Section 5 — The confirmation

Present compact summary:

> **Identity**
> - [Name], [filing status], [dependents]
> - Texas resident
> - [Business structure]
>
> **Income**
> - Gross receipts: $X
> - [Client breakdown]
>
> **Expenses**
> - [Category breakdown]
>
> **Texas-specific**
> - Total revenue for franchise tax: $X
> - Franchise tax threshold ($2.47M): [above/below]
> - Franchise tax filing obligation: [No Tax Due report / actual tax due]
> - Sales tax permit: [active/none/needed]
> - Sales tax collected: $X (if applicable)
>
> **Federal estimated taxes paid:** $X
>
> **Flags:**
> - [Any issues]
>
> **Is any of this wrong?**

## Section 6 — Gap filling

Things that usually need asking:

1. **Home office** — exclusive use test, square footage
2. **Sales tax nexus** — does the taxpayer sell taxable tangible personal property or taxable services in Texas? (most software consulting is NOT taxable for TX sales tax, but custom software vs. canned software distinction matters)
3. **Franchise tax entity information** — confirm SOS file number, entity formation date, accounting period end date
4. **Health insurance source** — marketplace (no state exchange in TX, uses healthcare.gov) vs employer vs COBRA vs health sharing ministry
5. **Vehicle use** — if any business mileage

## Section 7 — Texas-specific tax framework

### Texas has no state income tax

- **No state income tax** — Article VIII, §24-a of the Texas Constitution prohibits a state personal income tax unless approved by voters in a statewide referendum. There is no state income tax return to file.  _(Article VIII, §24-a of the Texas Constitution)_

### Texas franchise tax (margin tax)

- **What it is** — A tax on entities (including LLCs and sole proprietorships with an LLC filing) doing business in Texas. Reported to the Texas Comptroller.  _(Section 7 — Texas franchise tax (margin tax))_
- **Who must file** — All taxable entities formed in Texas or doing business in Texas. Includes LLCs, corporations, partnerships, LLPs. Sole proprietors without an LLC are NOT subject to franchise tax. Single-member LLCs ARE subject to franchise tax (even though disregarded for federal purposes).  _(Section 7 — Texas franchise tax (margin tax))_
- **No-tax-due threshold (2025)** — $2,470,000 USD (annualized total revenue; if at or below, file Form 05-102 (Public Information Report / No Tax Due Report), no tax owed; if exceeds, compute franchise tax)  _(Section 7 — Texas franchise tax (margin tax), No-tax-due threshold (2025))_
- **Margin tax rate above threshold — retail/wholesale** — 0.375% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **Margin tax rate above threshold — other** — 0.75% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **Margin computation (if tax due)** — Total revenue (gross receipts from TX operations) minus the greatest of: Cost of goods sold (COGS); Compensation (W-2 wages + benefits); 30% of total revenue (simplified method); $1 million (standard deduction equivalent). The result is "taxable margin". Tax = taxable margin × applicable rate.  _(Section 7 — Texas franchise tax (margin tax), Margin computation (if tax due))_
- **EZ Computation (Form 05-169)** — Available if total revenue ≤ $20 million. Rate: 0.331% of apportioned total revenue (no margin deductions). Simpler calculation, may result in higher or lower tax.  _(Section 7 — Texas franchise tax (margin tax), EZ Computation (Form 05-169))_
- **Filing deadlines** — Annual report due May 15 (for accounting year ending December 31). Extension available to November 15. Public Information Report (PIR) filed with the franchise tax return.  _(Section 7 — Texas franchise tax (margin tax), Filing deadlines)_
- **For most freelance developers with SMLLCs under $2.47M revenue** — File Form 05-102 (No Tax Due) + Public Information Report by May 15. No tax payment required. Failure to file can result in forfeiture of LLC status by Texas Secretary of State.  _(Section 7 — Texas franchise tax (margin tax), For most freelance developers with SMLLCs under $2.47M revenue)_

### Texas sales tax

- **State rate** — 6.25%  _(Section 7 — Texas sales tax, State rate)_
- **Local additions** — Up to 2% (total max 8.25%)  _(Section 7 — Texas sales tax, Local additions)_
- **Applicability to software/tech services** — Custom software (written for a single customer): NOT taxable in Texas. Canned (prewritten) software delivered electronically: Taxable. SaaS: Texas Comptroller Rule 3.330 — generally taxable as "data processing services" (20% of value taxable after statutory exemption). IT consulting/programming services (labor to create custom code): NOT taxable. Hardware repair or maintenance contracts: Taxable.  _(Texas Comptroller Rule 3.330; Section 7 — Texas sales tax, Applicability to software/tech services)_
- **For most freelance software developers** — If providing custom development services to clients: NO sales tax obligation. If selling a prewritten software product or SaaS: sales tax permit required, must collect and remit.  _(Section 7 — Texas sales tax, For most freelance software developers)_
- **Sales tax permit** — Free to obtain from Texas Comptroller. If permit is active, returns must be filed even if no tax collected ($0 returns). Filing frequency: monthly, quarterly, or annually (Comptroller assigns based on volume). If no taxable sales: consider closing permit to avoid filing obligation.  _(Section 7 — Texas sales tax, Sales tax permit)_

### Texas does NOT have:

- State income tax
- City/county income tax
- Gross receipts tax (other than franchise tax)
- Estate tax (no state-level estate tax)
- Inheritance tax

## Section 8 — Handoff

> Intake complete. Handing off to the return assembly workflow.
>
> You'll receive:
> 1. Excel working paper (federal return lines + TX franchise tax computation)
> 2. Reviewer brief with positions, citations, and flags
> 3. Federal form package (1040 + supporting schedules)
> 4. TX franchise tax filing checklist (Form 05-102 or 05-158/05-169)
> 5. TX sales tax compliance summary (if applicable)
> 6. 2026 federal estimated tax vouchers
> 7. Action items with deadlines
>
> Starting now.

0. **Handoff to return assembly workflow** — Intake complete. Handing off to the return assembly workflow.
0. **Handoff to us-tx-return-assembly** — Explicit handoff to the return assembly workflow (us-tx-return-assembly) per Self-check TX-IN9.

## Section 9 — Refusal handling

- **Refusal: LLC revenue above $2.47M** — Stop — your LLC revenue is above $2.47M. Texas franchise tax at this level requires detailed margin computation with COGS vs compensation analysis, apportionment calculations, and potentially the EZ Computation comparison. You need a CPA or franchise tax specialist.  _(Section 9 — Refusal handling)_
- **Refusal: sells prewritten software products** — Stop — you sell prewritten software products to customers. Texas sales tax compliance for software products requires analysis of delivery method, bundling, and local jurisdiction rates. You need a CPA familiar with Texas sales tax for technology companies.  _(Section 9 — Refusal handling)_
- **Refusal: multi-state travel income (CA/NY)** — Stop — you have income from work performed in California and New York while traveling. Those states will likely assert income tax nexus. You need a multi-state CPA even though Texas has no income tax.  _(Section 9 — Refusal handling)_

## Section 10 — Self-checks

**Check TX-IN1 — Refusal sweep used ask_user_input_v0.**
**Check TX-IN2 — Revenue range captured for franchise tax threshold analysis.**
**Check TX-IN3 — Sole prop vs SMLLC distinction made (sole prop without LLC = no franchise tax filing).**
**Check TX-IN4 — Sales tax applicability evaluated (custom software vs SaaS vs products).**
**Check TX-IN5 — Upload-first flow honored.**
**Check TX-IN6 — Documents parsed before gap-filling.**
**Check TX-IN7 — Federal estimated tax payments tracked (no state estimated tax in TX).**
**Check TX-IN8 — Franchise tax filing deadline (May 15) noted in action items.**
**Check TX-IN9 — Handoff to us-tx-return-assembly is explicit.**

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
