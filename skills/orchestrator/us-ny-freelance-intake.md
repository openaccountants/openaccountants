---
name: us-ny-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their US federal or New York state tax return AND mentions freelancing, self-employment, software development, contracting, sole proprietorship, or a single-member LLC in New York. Trigger on phrases like "I'm a freelancer in New York", "NYC self-employed taxes", "I have an LLC in NY", "New York freelance tax return", "I live in Manhattan and do contracting", or any similar phrasing where the user is a New York-resident freelancer needing tax return preparation. This is the REQUIRED entry point for the New York freelance developer tax workflow. Uses upload-first workflow and ask_user_input_v0 for structured questions. New York full-year residents only; handles both NYC residents (subject to NYC UBT and city income tax) and rest-of-state residents. Sole proprietors and single-member LLCs disregarded for federal tax only.
version: 1.0
jurisdiction: US-NY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Ny Freelance Intake

## Section 1 — The opening

When triggered, respond with ONE message that:

1. One-line greeting
2. One-line summary of the flow (scope check → upload → gaps → handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by EA/CPA before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 federal + New York return ready. Quick scope check, then you upload your documents, then I fill gaps. Target: 10 minutes.
>
> Reminder: everything I produce needs signoff from a credentialed tax professional (EA, CPA, or tax attorney) before filing.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

## Section 2 — Refusal sweep

Present the first batch as a single `ask_user_input_v0` call with 3 questions:

```
Q1: "Business structure?"
    Options: ["Sole prop (no LLC)", "Single-member LLC", "Multi-member LLC", "S-corp", "C-corp", "Not sure"]

Q2: "Revenue range for 2025?"
    Options: ["Under $100K", "$100K–$250K", "$250K–$500K", "$500K–$1M", "Over $1M"]

Q3: "NYC resident (any of the 5 boroughs) or rest of NY state?"
    Options: ["NYC (Manhattan, Brooklyn, Queens, Bronx, Staten Island)", "Rest of NY state", "Part-year NYC / moved during 2025", "I don't live in NY"]
```

**Evaluate:**

- **Q1 = Sole prop or Single-member LLC** → continue
- **Q1 = Multi-member LLC** → stop. "Multi-member LLCs file Form 1065 as partnerships. You need a CPA familiar with partnership returns and NY PTET elections."
- **Q1 = S-corp or C-corp** → stop. "I don't cover corporate returns. S-corp (1120-S) and C-corp (1120) plus NY CT-3/CT-4 require a CPA."
- **Q1 = Not sure** → follow-up: "Did you file Form 2553 (S-corp election) or receive a W-2 from your own business? Yes to either = S-corp."

- **Q2** → record for downstream. Over $1M triggers additional NYC UBT considerations.

- **Q3 = NYC** → continue, flag NYC UBT (Form NYC-202) + NYC personal income tax (Form NYC-1127 if applicable)
- **Q3 = Rest of NY state** → continue, no NYC taxes
- **Q3 = Part-year NYC** → continue with flag: NYC part-year allocation required
- **Q3 = I don't live in NY** → stop. "I'm set up for full-year New York residents only. Non-residents need Form IT-203 and multi-state allocation. You need a CPA who handles non-resident returns."

**Second batch (after first batch passes):**

```
Q4: "Filing status?"
    Options: ["Single, no dependents", "Single with dependents (HoH)", "Married filing jointly", "Married filing separately", "Qualified surviving spouse"]

Q5: "Did you file a 2024 return normally?"
    Options: ["Yes", "No (skipped year)", "Yes but amended / under audit"]

Q6: "Any of these in 2025?" (multi-select)
    Options: [
      "Rental property income",
      "Active crypto/day trading",
      "Foreign bank account over $10K",
      "W-2 employees on payroll",
      "Partnership income (K-1 from another entity)",
      "None of the above"
    ]

Q7: "NYS estimated tax payments made in 2025?"
    Options: ["Yes, all 4 quarters", "Yes, some quarters", "No", "Not sure"]

Q8: "Do you also have income sourced outside NY?"
    Options: ["No, all income is NY-sourced", "Yes, some income from other states", "Yes, significant out-of-state income"]
```

**Evaluate Q4:** Record filing status. All options in scope.

**Evaluate Q5:**
- Yes → continue
- No or amended/under audit → stop. "Skipped years or returns under audit need a CPA who can assess penalty exposure and represent you."

**Evaluate Q6:**
- Any of the first five options selected → stop with appropriate refusal
- "None of the above" → continue

**Evaluate Q7:** Record for downstream estimated tax analysis.

**Evaluate Q8:**
- All NY-sourced → continue
- Some or significant out-of-state → stop. "Multi-state income allocation requires IT-203 schedules and credit-for-taxes-paid-to-other-states analysis. You need a CPA who handles multi-state returns."

- **Q1 = Multi-member LLC** — Multi-member LLCs file Form 1065 as partnerships. You need a CPA familiar with partnership returns and NY PTET elections.  _(Section 2 — Refusal sweep)_
- **Q1 = S-corp or C-corp** — I don't cover corporate returns. S-corp (1120-S) and C-corp (1120) plus NY CT-3/CT-4 require a CPA.  _(Section 2 — Refusal sweep)_
- **Q3 = I don't live in NY** — I'm set up for full-year New York residents only. Non-residents need Form IT-203 and multi-state allocation. You need a CPA who handles non-resident returns.  _(Section 2 — Refusal sweep)_
- **Q5 = No (skipped year) or amended/under audit** — Skipped years or returns under audit need a CPA who can assess penalty exposure and represent you.  _(Section 2 — Refusal sweep)_
- **Q8 = Some or significant out-of-state income** — Multi-state income allocation requires IT-203 schedules and credit-for-taxes-paid-to-other-states analysis. You need a CPA who handles multi-state returns.  _(Section 2 — Refusal sweep)_

## Section 3 — The dump

Once the refusal sweep passes, request the document dump:

> Scope is good. Upload everything you have for 2025:
>
> - Business bank statement(s) for 2025 (CSV or PDF)
> - Tax forms received (1099-NEC, 1099-MISC, 1095-A/B/C, W-2 from side employment)
> - Year-end retirement account statements
> - NYS/NYC estimated tax payment confirmations or cancelled checks
> - Your 2024 tax return (federal + NY)
> - Any NY-specific notices (DTF correspondence, NYC Finance letters)
> - LLC formation docs if applicable (Articles of Organization filed with NY DOS)
> - Anything else tax-related
>
> Drop it all in — I'll sort it out.

## Section 4 — The inference pass

Parse all documents and extract:

**Bank statement:**
- Total deposits (gross receipts)
- Client retainer payments
- IRS EFTPS payments (federal estimated tax)
- NY DTF payments (state estimated tax)
- NYC Finance payments (city estimated tax or UBT)
- Retirement contributions
- Health insurance premiums
- Business expenses (SaaS, equipment, travel)
- Contractor payments
- NY LLC filing fee ($25 biennial)

**1099-NEC received:**
- Payer name, TIN, Box 1 amount
- Cross-check against bank deposits

**Prior year return (federal + NY IT-201):**
- Federal total tax (1040 Line 24)
- Federal AGI (1040 Line 11)
- NY taxable income (IT-201 Line 38)
- NY tax (IT-201 Line 39)
- NYC taxable income (IT-201 Line 47, if NYC resident)
- NYC tax (IT-201 Line 48)
- NY household credit claimed
- NYC UBT paid (Form NYC-202)

**Retirement account statement:**
- Plan type, contributions, dates
- Solo 401(k) limits: $23,500 employee + employer up to §415(c) $70,000 total

- **NY LLC filing fee (biennial)** — $25 USD (biennial)  _(Section 4 — The inference pass)_
- **Solo 401(k) employee contribution limit** — $23,500 USD  _(Section 4 — The inference pass)_
- **Solo 401(k) total limit (employee + employer, §415(c))** — $70,000 USD  _(Section 4 — The inference pass)_

## Section 5 — The confirmation

Present compact summary showing extracted data. Structure:

> **Identity**
> - [Name], [filing status], [dependents]
> - Full-year NY resident ([NYC/rest of state])
> - [Business structure]
>
> **Income**
> - Gross receipts: $X
> - [Client breakdown]
>
> **Expenses**
> - [Category breakdown from bank statement]
>
> **NY-specific**
> - NYC UBT applicability: [Yes/No — triggered if NYC resident with business income]
> - NYC UBT allocation: [100% if all work in NYC]
> - NYS estimated payments made: $X
> - NYC estimated payments made: $X
>
> **Flags:**
> - [Any issues identified]
>
> **Is any of this wrong?**

## Section 6 — Gap filling

Things that usually need asking:

1. **Home office** — exclusive use test, square footage
2. **NYC UBT allocation** — percentage of business conducted in NYC (if any work done outside city)
3. **Health insurance source** — NY State of Health marketplace vs employer vs COBRA
4. **Commuter benefits** — transit pre-tax (if also W-2 employment)
5. **MCTMT** — Metropolitan Commuter Transportation Mobility Tax: applies to self-employment income > $50,000 for NYC-area taxpayers (rate: 0.34% of net SE earnings allocated to MCTD)

- **MCTMT rate on net SE earnings allocated to MCTD** — 0.34% (applies to self-employment income > $50,000 for NYC-area taxpayers)  _(Section 6 — Gap filling)_

## Section 7 — NY-specific tax framework

### New York State income tax (Form IT-201)

**2025 NY State income tax rates (full-year resident)**  _(Section 7 — NY-specific tax framework > New York State income tax (Form IT-201))_

| Rate | Bracket |
| --- | --- |
| 4.00% | $0–$8,500 |
| 4.50% | $8,501–$11,700 |
| 5.25% | $11,701–$13,900 |
| 5.50% | $13,901–$80,650 |
| 6.00% | $80,651–$215,400 |
| 6.85% | $215,401–$1,077,550 |
| 9.65% | $1,077,551–$5,000,000 |
| 10.30% | $5,000,001–$25,000,000 |
| 10.90% | Over $25,000,000 |

- **NY standard deduction (single, 2025)** — $8,000 USD  _(Section 7 — NY-specific tax framework > New York State income tax (Form IT-201))_
- **NY standard deduction (MFJ, 2025)** — $16,050 USD  _(Section 7 — NY-specific tax framework > New York State income tax (Form IT-201))_
- **NY itemized deduction basis** — Based on federal Schedule A with NY modifications (no SALT deduction add-back at state level, but NY limits itemized deductions for high earners)  _(Section 7 — NY-specific tax framework > New York State income tax (Form IT-201))_

### NYC personal income tax (NYC resident surcharge)

**2025 NYC resident surcharge rates**  _(Section 7 — NY-specific tax framework > NYC personal income tax (NYC resident surcharge))_

| Rate | Bracket |
| --- | --- |
| 3.078% | $0–$12,000 |
| 3.762% | $12,001–$25,000 |
| 3.819% | $25,001–$50,000 |
| 3.876% | $50,001 and over |

- **Additional NYC surcharge for high earners** — Additional NYC surcharge for taxable income > $500,000 effectively brings top combined NYC rate to approximately 3.876% + additional tiers.  _(Section 7 — NY-specific tax framework > NYC personal income tax (NYC resident surcharge))_

### NYC Unincorporated Business Tax (UBT) — Form NYC-202

- **UBT applicability** — Applies to any unincorporated business (sole prop, SMLLC) carried on in NYC  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **UBT tax rate** — 4% (of taxable income after exemption)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **UBT exemption** — $95,000 USD (phases out between $95,000 and $150,000 of NYC UBT taxable income)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **Partial credit against NYC personal income tax** — Partial credit against NYC personal income tax (Form NYC-1127 or IT-201 Line 51)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **UBT estimated tax quarterly payment threshold** — $3,400 USD (quarterly payments required if UBT liability expected to exceed this amount)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_

### Metropolitan Commuter Transportation Mobility Tax (MCTMT)

- **MCTMT applicability** — Applies to self-employed individuals with net earnings from self-employment allocated to the Metropolitan Commuter Transportation District (NYC + Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester)  _(Section 7 — NY-specific tax framework > Metropolitan Commuter Transportation Mobility Tax (MCTMT))_
- **MCTMT rate** — 0.34% (on net SE earnings > $50,000 allocated to MCTD)  _(Section 7 — NY-specific tax framework > Metropolitan Commuter Transportation Mobility Tax (MCTMT))_
- **MCTMT reporting and due dates** — Reported on Form MTA-6 (annual) or quarterly. Due dates align with estimated tax quarters  _(Section 7 — NY-specific tax framework > Metropolitan Commuter Transportation Mobility Tax (MCTMT))_

### NY estimated tax (Form IT-2105)

- **NY estimated tax requirement threshold** — $300 USD (required if NY tax liability expected to exceed this amount after credits and withholding)  _(Section 7 — NY-specific tax framework > NY estimated tax (Form IT-2105))_
- **Quarterly due dates** — April 15, June 15, September 15, January 15  _(Section 7 — NY-specific tax framework > NY estimated tax (Form IT-2105))_
- **Safe harbor** — 100% of prior year NY tax OR 90% of current year NY tax  _(Section 7 — NY-specific tax framework > NY estimated tax (Form IT-2105))_
- **Underpayment penalty computation** — Underpayment penalty: computed on Form IT-2105.9  _(Section 7 — NY-specific tax framework > NY estimated tax (Form IT-2105))_

## Section 8 — Handoff

Once gap-filling is complete, produce handoff message and invoke `us-ny-return-assembly`:

> Intake complete. Handing off to the return assembly workflow.
>
> You'll receive:
> 1. Excel working paper (federal + NY + NYC lines)
> 2. Reviewer brief with positions, citations, and flags
> 3. Form packages (1040, IT-201, NYC-202 if applicable)
> 4. 2026 estimated tax vouchers (federal + NY + NYC)
> 5. Action items with deadlines
>
> Starting now.

0. **Handoff to return assembly** — Once gap-filling is complete, invoke us-ny-return-assembly

## Section 9 — Refusal handling

When a refusal fires:
1. Stop the workflow
2. State the specific reason
3. Recommend the path forward
4. Do not try to work around the refusal

**Sample refusals:**

> Stop — you have partnership income from a K-1. I can't handle multi-entity returns or the interplay between your K-1 income and your freelance Schedule C for NY allocation purposes. You need a CPA.

> Stop — you moved out of NYC mid-year. Part-year NYC allocation on the UBT and city income tax requires Form NYC-1127 and careful day-counting. You need a CPA familiar with NYC part-year filings.

## Section 10 — Self-checks

**Check NY-IN1 — Refusal sweep used ask_user_input_v0.**
**Check NY-IN2 — NYC vs rest-of-state determined before proceeding.**
**Check NY-IN3 — UBT applicability flag set if NYC resident with business income.**
**Check NY-IN4 — Upload-first flow honored.**
**Check NY-IN5 — Documents parsed before gap-filling questions.**
**Check NY-IN6 — MCTMT flagged for MCTD-area taxpayers.**
**Check NY-IN7 — Filing status recorded for IT-201 rate determination.**
**Check NY-IN8 — Handoff to us-ny-return-assembly is explicit.**

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
