---
name: us-ny-freelance-intake
description: Entry point for a New York resident freelancer, sole proprietor or single-member LLC owner who wants help with a 2026 federal and New York return. Runs a scope check (entity, residence, multi-state income, open years), asks for the documents, reads them, fills the gaps, and hands a confirmed fact sheet to us-ny-return-assembly, naming which federal and New York skills apply (IT-201, NYC UBT, MCTMT, estimated tax, LLC fee). Carries no rates of its own; every figure is in the linked skill. Trigger on "I'm a freelancer in New York", "NYC self-employed taxes", "I have an LLC in NY", "New York freelance tax return", "I live in Manhattan and do contracting". Full-year New York residents only.
version: "2.0"
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# New York freelancer intake, tax year 2026

> **Source-cited draft.** Routing built from the New York Tax Department's IT-201 and IT-2105 instructions and the NYC Department of Finance UBT page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** This skill decides whether the client is in scope, gathers the documents and facts, and routes them. A full-year New York resident who is a sole proprietor or a single-member LLC disregarded for federal tax goes through the federal skills, then `ny-it-201-resident-return`, plus `nyc-ubt` if the business is carried on in New York City, the MCTMT if self-employment earnings are allocated to the MCTD, and `ny-estimated-tax` for 2027 payments, and finally `us-ny-return-assembly`. It states no tax figures: each threshold lives in the skill that owns it.

## Scope and who this is for

In scope: a full-year New York State resident (New York City, Yonkers or rest of state) who is a sole proprietor or the owner of a single-member LLC disregarded for federal tax, filing Form 1040 and Form IT-201 for tax year 2026.

Out of scope, and where it goes:

| Situation | Skill or action |
| --- | --- |
| Moved into or out of New York State or New York City during 2026, or lives outside New York | `ny-residency-leaving-new-york` (Form IT-203); refer the return |
| Multi-member LLC or partnership | `us-form-1065-partnership`; refer |
| S corporation or C corporation | refer (New York Article 9-A is `ny-corporate-franchise-article-9a`) |
| Should the client become an S corporation? | `us-s-corp-election-decision` |
| Income taxed by another state | `us-multi-state-residency-and-allocation`; refer |

## Ask the client first

1. **Business structure:** sole proprietor, single-member LLC, multi-member LLC, S corporation, C corporation, or not sure. If not sure: did they file Form 2553, or receive a W-2 from their own business? Either means an S corporation.
2. **Where did they live all of 2026,** and did they move? New York City (the five boroughs), Yonkers, rest of New York State, part-year, or outside New York.
3. **Where is the work done?** Home office or office address, and whether any work is done outside New York City or outside the MCTD counties.
4. **Filing status and dependents** for 2026.
5. **Any 2026 income from other states, K-1s, rental property, active trading, foreign accounts, or employees on payroll?**
6. **Were the 2025 returns filed, and is any year under audit or amended?**

## The method, step by step

1. **Open with one message:** a one-line greeting, a one-line summary of the flow (scope check, upload, gaps, handoff), and a reminder that everything produced must be reviewed by a credentialed tax professional (EA, CPA or tax attorney) before filing. Then ask the scope questions at once, using the host's structured question tool where it has one.
2. **Scope check, first batch:** structure (question 1), residence (question 2), revenue range for 2026 (record it; it tells `nyc-ubt` whether a return may be due). Stop on any answer in the refusal table below.
3. **Scope check, second batch:** filing status (question 4), the 2025 return (question 6), the special items (question 5), whether New York estimated payments were made in 2026 (all four, some, none, not sure), and income from outside New York.
4. **Ask for the documents in one list:**
   - business bank and card statements for 2026 (CSV or PDF);
   - every 1099-NEC, 1099-MISC and 1099-K, and any W-2 from side employment;
   - 1095-A, B or C;
   - year-end retirement account statements;
   - federal, New York State and New York City estimated payment confirmations for 2026;
   - the 2025 federal return, Form IT-201 and, if filed, Form NYC-202 or NYC-202S;
   - any Tax Department or NYC Department of Finance notices;
   - LLC formation papers (Articles of Organization filed with the New York Department of State).
5. **Read the documents and extract:**
   - bank: total deposits (gross receipts), client payments, IRS (EFTPS) payments, New York State DTF payments, NYC Department of Finance payments, retirement contributions, health insurance premiums, business expenses by type, contractor payments, any New York LLC filing fee paid;
   - each 1099: payer, TIN, amount, matched to deposits;
   - the 2025 returns: federal AGI and total tax; IT-201 New York AGI, taxable income, state tax, city taxable income and city tax; the household credit; UBT paid. These feed the 2026 estimated tax safe harbour (`ny-estimated-tax`) and the federal one (`us-quarterly-estimated-tax`);
   - retirement statements: plan type, contributions and dates (limits in `us-self-employed-retirement`).
6. **Confirm in one compact summary:** identity, filing status, dependents, residence (city, Yonkers or rest of state), structure; gross receipts by client; expenses by category; the New York flags (UBT likely or not, MCTMT zone, state and city estimates paid). Ask "Is any of this wrong?"
7. **Fill the gaps** that documents rarely answer: home office (exclusive use, square feet); the share of work done in New York City if any is done outside; the source of health insurance (NY State of Health marketplace, employer, COBRA); commuter benefits from any W-2 job; the MCTD county where the business is carried on.
8. **Route and hand off.** Set the flags and pass the fact sheet to `us-ny-return-assembly`, which runs the skills in order:

| Flag | Set when | Skill |
| --- | --- | --- |
| Federal core | always | `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction`, `us-federal-return-assembly`, `us-quarterly-estimated-tax` |
| Contractors paid | the client paid contractors | `us-1099-nec-issuance` |
| State return | always | `ny-it-201-resident-return` |
| NYC UBT | business carried on wholly or partly in New York City | `nyc-ubt` |
| MCTMT | business carried on in an MCTD county (the five boroughs, Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester) | `ny-mctmt` (the IT-201 lines are in `ny-it-201-resident-return`) |
| State estimates | always, for 2027 | `ny-estimated-tax` |
| LLC fee | single-member LLC | `ny-llc-filing-fee-it-204-ll` |
| PTET question | the client asks about the pass-through entity tax | `ny-pte-tax-ptet` |

9. **Handoff message:** "Intake complete. Handing off to the return assembly workflow. You will receive: a working paper (federal, New York State and New York City lines), a reviewer brief with positions, citations and flags, the form packages (1040, IT-201, NYC-202 if it applies), 2027 estimated tax schedules (federal, New York State, New York City), and an action list with deadlines."

## When to refuse or refer

| Code | Trigger | What to say |
| --- | --- | --- |
| R-NYI-1 | Multi-member LLC | "Multi-member LLCs file Form 1065 as partnerships. You need a CPA familiar with partnership returns and New York PTET elections." |
| R-NYI-2 | S corporation or C corporation | "I do not cover corporate returns. Form 1120-S or 1120 and New York Form CT-3 or CT-3-S need a CPA." |
| R-NYI-3 | Lives outside New York, or moved into or out of New York State or New York City in 2026 | "I am set up for full-year New York residents only. A part-year or nonresident return (Form IT-203, with IT-360.1 for the city) needs a CPA who handles them." See `ny-residency-leaving-new-york`. |
| R-NYI-4 | A skipped year, an amended return or an open audit | "Skipped years or returns under audit need a CPA who can assess penalty exposure and represent you." |
| R-NYI-5 | Income from other states | "Multi-state allocation and the credit for tax paid to another state need a CPA who handles multi-state returns." |
| R-NYI-6 | Rental property, active crypto or day trading, foreign accounts over USD 10,000, employees on payroll, or K-1 income | Stop, name the item, and refer: these are outside the freelancer workflow. |

When a refusal fires: stop, state the specific reason, say what to do next, and do not work around it.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IT-201-I (2025). Read for who files Form IT-201 (full-year residents) and the New York City, Yonkers and MCTMT lines. | https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf | 2026-11-13 |
| IT-2105-I (2026). Read for the MCTD counties and zones and who must pay estimated tax. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| NYC Department of Finance, Unincorporated business tax. Read for who is subject to the UBT. | https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page | 2026-11-13 |
| Residency FAQ. Read for full-year, part-year and New York City residence. | https://www.tax.ny.gov/pit/file/nonresident-faqs.htm | 2026-10-03 |

Not yet confirmed: the 2026 Form IT-201 instructions are not published; this skill carries no figures, so nothing here depends on them.
