---
name: us-tx-freelance-intake
description: "Entry point for a Texas-resident freelancer, sole proprietor or single-member LLC owner who wants their 2026 federal return and Texas compliance prepared. Runs the scope check, collects documents, fills gaps and hands off to us-tx-return-assembly. Texas has no individual income tax, so the Texas side is the franchise tax Public Information Report for an LLC ($2,650,000 no tax due threshold on annualized revenue), sales tax if taxable items are sold, and unemployment tax if there are employees. Trigger on \"I'm a freelancer in Texas\", \"Texas self-employed taxes\", \"I have an LLC in TX\", \"Houston contractor tax return\", \"Austin freelance developer\", \"Dallas sole proprietor\". Texas residents only; sole proprietors and single-member LLCs disregarded for federal tax only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-tx-freelance-intake"
  jurisdiction: "US-TX"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Texas freelancer intake, tax year 2026

> **Source-cited draft.** The Texas figures are from the Texas Comptroller's franchise tax page and 2026 instructions (Form 05-915), Tax Code Chapter 171 and Article 8 of the Texas Constitution, read on 2026-11-13. Federal figures live in the federal skills named below. No accountant has reviewed it. Everything produced needs sign-off from a credentialed tax professional before filing.

**Answer first.** A full-year Texas resident files no state income tax return: Texas may not tax individuals' net incomes. What this intake has to settle is (1) the federal return, (2) whether the client has an LLC, because an LLC (even a disregarded single-member one) must file a Texas Public Information Report every year by 15 May and owes franchise tax only above **$2,650,000** of annualized revenue, while a sole proprietor with no LLC files nothing for franchise tax, (3) whether anything sold is taxable for Texas sales tax, and (4) whether there are employees (Texas Workforce Commission unemployment tax). Then it hands off to `us-tx-return-assembly`.

## Scope

In scope: one Texas-resident individual, full year 2026, with self-employment income as a sole proprietor or through a single-member LLC disregarded for federal tax, filing Form 1040 with Schedule C. The intake routes; it does not compute.

Out of scope: multi-member LLCs and partnerships, S and C corporations, part-year residents, and the other cases in "When to refuse or refer".

## Ask the client first

1. **Business structure:** sole proprietor (no LLC), single-member LLC, multi-member LLC, S corporation or C corporation, or not sure (then ask whether Form 2553 was filed or the owner gets a W-2 from the business).
2. **2026 revenue of the business, and when the LLC was formed.** Under USD 1 million, USD 1 million to USD 2,650,000, or over USD 2,650,000; if the LLC was formed during 2026, the revenue must be annualized before comparing (see Worked cases).
3. **Filing status and dependants for 2026.**
4. **Does the business sell goods, software, or services Texas taxes, and does it hold a Texas sales tax permit?**
5. **Employees in 2026?** If yes, Texas unemployment tax applies (`tx-payroll`) on top of federal payroll.
6. **Work performed in person in other states, rental property, foreign accounts, or a prior year not filed or under audit?** These end the intake (see refusals).

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Texas individual income tax | None (prohibited) | [Texas Constitution, Article 8, Section 24-a](https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm) |
| Franchise tax no tax due threshold, 2026 and 2027 reports (annualized total revenue) | USD 2,650,000 | [Texas Comptroller, franchise tax](https://comptroller.texas.gov/taxes/franchise/) |
| Annualizing a short period | Total revenue / days in period x 365 | [Form 05-915 (2026), Annualized Total Revenue](https://comptroller.texas.gov/forms/05-915.pdf) |
| Franchise tax report and PIR due date | 15 May each year (17 May 2027 for 2026, since 15 May 2027 is a Saturday) | [Texas Comptroller, franchise tax: due dates](https://comptroller.texas.gov/taxes/franchise/) |

All other Texas figures belong to `tx-franchise-tax`, `tx-payroll` and the Texas sales tax skill named in this folder's README; federal figures belong to the federal skills.

### Step 1: scope check

Ask questions 1, 2, 3 and 6 together (with structured choices where the client supports them). Then:

- Sole proprietor or single-member LLC: continue.
- Multi-member LLC, S corporation or C corporation: stop (R-TX-IN-ENTITY).
- Any item in question 6: stop with the matching refusal.
- Revenue over USD 2,650,000 with an LLC: continue only if a reviewer will handle the franchise tax computation; flag it for `tx-franchise-tax`.

### Step 2: collect documents (upload first)

Ask for everything in one message:

- Business bank and card statements for 2026 (CSV or PDF).
- Forms 1099-NEC, 1099-MISC, 1099-K and 1095-A, B or C received.
- Federal estimated tax payment confirmations for 2026.
- The 2025 federal return.
- For an LLC: the Certificate of Formation, the Texas taxpayer number and Webfile number, and any Comptroller letters or past PIRs.
- Texas sales tax permit and returns, if any.
- TWC account letters and quarterly reports, if there are employees.
- Retirement plan year-end statements and health insurance premium records.

### Step 3: read the documents before asking anything

From the bank statements: total deposits (gross receipts, which also drive the franchise tax test), client payments by payer, IRS payments, Comptroller payments (sales tax, franchise tax), TWC payments, retirement contributions, health premiums, contractor payments. From the 1099s: payer, TIN and amount, matched to deposits. From the 2025 return: total tax and AGI (for the safe harbour in `us-quarterly-estimated-tax`). From the Comptroller file: the entity's status, the last PIR filed, and whether any report is late.

### Step 4: confirm, then fill gaps

Show a short summary (identity, structure, gross receipts by client, expense totals, the Texas items: LLC yes or no, annualized revenue against USD 2,650,000, sales tax permit, employees) and ask "Is any of this wrong?". Then ask only what is missing, usually: home office (exclusive use, square feet), business miles split before and after 1 July 2026 (`us-schedule-c-and-se-computation`), the health insurance source, and, for an LLC, the Secretary of State file number and formation date.

### Step 5: hand off

Hand the confirmed facts to `us-tx-return-assembly`, which runs the federal skills, then `tx-franchise-tax`, the sales tax skill and `tx-payroll` as needed.

## Boundary and exception table

| Situation | Route |
| --- | --- |
| Sole proprietor with no LLC | No franchise tax filing at all; federal plus sales tax and payroll if relevant |
| Single-member LLC, any revenue | PIR every year by 15 May, even with no tax; franchise tax report only above USD 2,650,000 annualized |
| LLC formed during 2026 | Annualize 2026 revenue before the threshold test |
| Pure custom services, nothing taxable sold | Likely no sales tax permit needed; confirm under the sales tax skill |
| Sales tax permit held but no taxable sales | Returns still due while the permit is open; consider closing it (sales tax skill) |
| Employees in Texas | `tx-payroll` for TWC; federal payroll under `us-form-941-940-payroll` |
| Prior PIRs not filed | Flag: forfeiture risk and personal liability (`tx-franchise-tax`) |

## Worked cases

**Case 1, an LLC formed part way through the year.** A developer forms a Texas single-member LLC on 1 September 2026 and bills USD 900,000 by 31 December 2026: 122 days. Annualized revenue: USD 900,000 / 122 x 365 = USD 2,692,622.95, above USD 2,650,000. Although actual revenue is far below the threshold, the 2027 report is not PIR-only: route it to `tx-franchise-tax` for an E-Z or Long Form computation on the actual USD 900,000 (the annualized figure is used only for the tests).

```oa-check
name: Annualizing a short first period for the no tax due test
inputs:
  revenue: 900000
  days: 122
  threshold: 2650000
steps:
  - annualized: revenue / days * 365
  - over_threshold: annualized - threshold
expected:
  annualized: 2692622.95
  over_threshold: 42622.95
```

## When to refuse or refer

| Code | Situation | Message |
| --- | --- | --- |
| R-TX-IN-ENTITY | Multi-member LLC, partnership, S corporation or C corporation | Entity returns (Form 1065, 1120-S, 1120) and their franchise tax reports need a CPA |
| R-TX-IN-MULTI | Work performed in person in other states | Other states may tax that income even though Texas does not; needs a multi-state preparer (`us-multi-state-residency-and-allocation`) |
| R-TX-IN-RENT | Rental property | Outside this workflow |
| R-TX-IN-FOREIGN | Foreign financial accounts over the reporting limits | Outside this workflow (`us-fbar-and-fatca-8938`) |
| R-TX-IN-HIST | Prior year not filed, amended, or under audit | Refer to a CPA |
| R-TX-IN-PART | Part-year Texas resident | Refer: the other state's return comes first |
| R-TX-IN-SALES | Sells prewritten software, SaaS or goods across many Texas localities | Continue only with the sales tax skill and a reviewer |

## Filing and payment

The intake files nothing. It records for the action list: the federal return due 15 April 2027 and the 2026 estimated tax dates (from `us-quarterly-estimated-tax`); for an LLC, the PIR (and report if needed) due 17 May 2027; sales tax and TWC dates if they apply.

## Completion checklist

- Structure confirmed: sole proprietor or single-member LLC.
- Revenue annualized if the LLC is new, and compared with USD 2,650,000.
- Sales tax and employees questions answered.
- Documents read before any gap question.
- Refusals checked.
- Handoff to `us-tx-return-assembly` made explicitly.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Texas Constitution Article 8. Read for Section 24-a (no tax on individuals' net incomes). | https://statutes.capitol.texas.gov/Docs/CN/htm/CN.8.htm | 2026-11-13 |
| Texas Comptroller, Franchise Tax page. Read for the $2,650,000 threshold and the 15 May due date with the next-business-day rule. | https://comptroller.texas.gov/taxes/franchise/ | 2026-11-13 |
| Form 05-915, 2026 Franchise Tax Report Information and Instructions. Read for sole proprietorships not subject (except single member LLCs), disregarded entities, and annualized total revenue. | https://comptroller.texas.gov/forms/05-915.pdf | 2026-11-13 |

Not yet confirmed: the 2027 franchise tax instructions are not yet published; the 17 May 2027 date applies the next-business-day rule to 15 May 2027.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-tx-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-tx-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
