---
name: us-ca-freelance-intake
description: Intake for a full-year California resident freelancer, sole proprietor or single-member LLC owner before the 2026 federal and California returns are prepared. Decides whether the client is in scope, which documents to collect, and which skill each answer routes to. California items covered here are the ABC test for anyone the client paid, the EDD DE 542 independent contractor report ($600, 20 calendar days, $24 and $490 penalties), the CDTFA seller's permit trigger, local permits through CalGold, the same-classification rule for an LLC, health coverage by month, and the California estimated tax test. Federal figures are routed by slug, not restated. Trigger on "help me do my taxes", "I'm a freelancer in California", "self-employed California", "I have an LLC in California", "contractor taxes California", "prepare my 2026 return". Load first, then us-ca-return-assembly.
version: "1.0"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# California freelancer intake: scoping a sole proprietor or single-member LLC before the federal and California returns, tax year 2026

> **Source-cited draft.** Built from the FTB limited liability company page, the 2025 Schedule CA (540) instructions, the 2026 Form 540-ES instructions, the 2025 FTB 3853 instructions, the EDD independent contractor reporting page, the Labor and Workforce Development Agency ABC test page, the CDTFA permits and licenses page and 26 CFR 1.401(k)-1 (eCFR), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Intake does not compute the return. It answers three questions: is the client in scope (full-year California resident; sole proprietor or single-member LLC disregarded for federal tax; tax year 2026, or 2025 on extension), which documents are needed, and where each answer goes. The California points to settle at intake are: anyone the client paid is an employee unless all three parts of the ABC test hold; a contractor who is an individual, sole proprietor or single-member LLC paid or contracted $600 or more must be reported to the EDD on form DE 542 within 20 calendar days; selling or leasing taxable goods needs a CDTFA seller's permit; an LLC owes the $800 annual tax and files Form 568 (`ca-llc-fee-and-tax`); and California does not follow the One Big Beautiful Bill Act.

## Scope and who this is for

In scope: a full-year California resident who works for themselves as a sole proprietor or through a single-member LLC disregarded for federal tax. "An LLC must have the same classification for both California and federal tax purposes" (FTB). Intake hands off to:

| Work | Skill |
| --- | --- |
| Build order of the whole package | `us-ca-return-assembly` |
| Federal Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| Federal estimates | `us-quarterly-estimated-tax` |
| Federal 1099-NEC and 1099-K thresholds and filing | `us-1099-nec-issuance`, `us-1099-k-and-payment-processors` |
| Retirement plan timing and limits | `us-self-employed-retirement`, `us-secure-2-and-retirement-updates` |
| Foreign accounts | `us-fbar-fatca-reporting` |
| California Form 540 and the figures | `ca-540-individual-return`, `ca-income-tax` |
| California estimates | `ca-estimated-tax-540es` |
| California health coverage penalty | `ca-form-3853-coverage` |
| LLC annual tax, fee and Form 568 | `ca-llc-fee-and-tax`, `ca-smllc-form-568` |
| Sales and use tax | `california-sales-tax` |
| Employees | `ca-payroll` |

## Ask the client first

1. **Residency.** In California for the whole tax year? A part-year resident or nonresident files Form 540NR: route to `ca-residency-leaving-california`.
2. **Entity.** Sole proprietor, single-member LLC or something else? Any Form 8832 or 2553 election, any W-2 from the client's own business, any co-owner or spouse owner?
3. **Tax year and filing status.** 2025 on extension or 2026; filing status and dependents. Keep the two years' figures apart.
4. **What the business does.** Services only, or does it also sell or lease physical goods (seller's permit)?
5. **Who the client paid.** For each person: name, entity type from the Form W-9, amount, how paid (check, bank transfer, card or payment app), date the total reached $600, and how the work was controlled.
6. **Prior year and payments.** 2025 federal and California returns (AGI and total tax), and every 2026 federal and California estimated payment with dates; for an LLC, payments on FTB forms 3522 and 3536.

Then also ask, before the documents: other income and assets (wages, rental, K-1s, capital gains, digital assets, foreign accounts with each account's highest balance), health coverage by month for each household member (Forms 1095-A, B or C), home office (regular and exclusive use) and vehicle (mileage log), retirement plan type, adoption date and deferral election date, and the city and county of the business.

## The method, step by step

1. **Confirm scope.** Full-year residency, entity and classification, tax year. Stop and refer on any out-of-scope answer.
2. **Collect the documents** (list below).
3. **Reconcile gross receipts** from bank deposits and invoices to every 1099-NEC, 1099-MISC and 1099-K. Income is reportable whether or not a form arrived; personal transfers on a 1099-K are excluded with a reason recorded. Thresholds: `us-1099-k-and-payment-processors`.
4. **Digital assets.** Answer the federal digital asset question from the facts. Any receipt as payment or any disposal routes to capital-gains work.
5. **Classify everyone the client paid (California ABC test).** A worker is an employee "unless the hiring entity satisfies all three" conditions: (A) free from the hiring entity's control and direction, under the contract and in fact; (B) the work is outside the usual course of the hiring entity's business; (C) the worker is customarily engaged in an independently established trade, occupation or business of the same nature. Any employee means payroll registration: refer (`ca-payroll`).
6. **Information returns the client owes as a payer.**
   - Federal Form 1099-NEC: threshold, corporation exception, card and payment-app exclusion and the January 31 due date are in `us-1099-nec-issuance`. A bank-to-bank transfer (Zelle, an app from the client's bank) is not a third party settlement organization payment, so it is treated like a check.
   - California DE 542: report to the EDD when **all** hold: the client must file a federal Form 1099-NEC or 1099-MISC for the services; it paid $600 or more, or entered into a contract for $600 or more, in a calendar year; and the contractor is an individual, sole proprietor or single-member LLC. Due within 20 calendar days of the payment or contract reaching $600. Penalty $24 per failure without good cause, $490 if intentional or false.
   - The DE 542 condition (a) depends on the federal filing requirement. The EDD page still prints $600; where the federal 1099-NEC threshold for 2026 payments is higher than the amount paid (`us-1099-nec-issuance`), confirm with the EDD before concluding that no DE 542 is due.
7. **Seller's permit.** "If you are doing business in California and intend to sell or lease tangible personal property subject to sales tax sold at retail, you are required to have a seller's permit" (CDTFA). A services-only freelancer does not meet that trigger. Goods sellers route to `california-sales-tax`; do not decide at intake whether a digital product or bundle is taxable.
8. **Local permits.** City and county business licences and business taxes are local; the CDTFA points to CalGold. Record the city and licence number.
9. **Single-member LLC.** An LLC doing business in California, organized here or registered with the Secretary of State pays the $800 annual tax by the 15th day of the 4th month of its tax year, may owe the LLC fee, and files Form 568. Route all of it to `ca-llc-fee-and-tax`; a sole proprietor with no LLC owes none of it.
10. **California differences to flag.** "In general, California R&TC does not conform to the OBBBA" (Schedule CA (540) instructions). Flag for `ca-540-individual-return`: any asset expensed federally under bonus depreciation or section 179 (separate California depreciation record), HSA contributions and earnings, and the QBI deduction (none in California).
11. **Health coverage.** If full-year coverage for every household member cannot be confirmed, route to `ca-form-3853-coverage`. Covered California with advance premium tax credit also needs federal Form 8962.
12. **Estimated tax.** Test 2026 California estimates with `ca-estimated-tax-540es` (30%, 40%, nothing, 30%) and federal estimates with `us-quarterly-estimated-tax` (four dates). Do not copy one pattern to the other.
13. **Retirement plan timing.** A self-employed person's cash or deferred election for a 401(k) must be made by the last day of the tax year: "a self-employed individual may not make a cash or deferred election with respect to compensation for a partnership or sole proprietorship taxable year after the last day of that year" (26 CFR 1.401(k)-1(a)(6)(iii)). Only the deposit can follow. A new solo 401(k) adopted after year end, employer contributions and SEPs: `us-secure-2-and-retirement-updates`.
14. **Hand off** the scope answers, reconciled receipts, the payee list with filings and dates, open flags and the payment history to `us-ca-return-assembly`.

### Documents to collect

- Business bank and card statements for the year (and any personal account used for the business).
- Every Form 1099-NEC, 1099-MISC and 1099-K, plus invoices or a sales ledger.
- Forms W-9 and contracts for everyone paid.
- 2025 federal and California returns.
- Proof of estimated payments from the IRS online account and MyFTB (bank lines alone are not enough).
- Forms 1095-A, 1095-B or 1095-C for each month.
- Retirement plan statements and the adoption document.
- A fixed-asset list with dates and costs, with both federal and California depreciation.
- For an LLC: Secretary of State filing date and FTB notices. For a seller: the CDTFA permit number.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| DE 542 reporting trigger | $600 or more paid, or a contract for $600 or more, in a calendar year | Contractor is an individual, sole proprietor or single-member LLC, and a federal 1099-NEC or 1099-MISC is required | [EDD independent contractor reporting](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/) |
| DE 542 due | Within 20 calendar days of reaching $600 | Payment or contract, whichever is first | same |
| DE 542 penalty | $24 per failure without good cause; $490 if intentional or false | Per report | same |
| ABC test | All three parts must hold, or the worker is an employee | California employment status | [LWDA ABC test](https://www.labor.ca.gov/employmentstatus/abctest/) |
| LLC annual tax | $800 | Doing business, organized or registered in California; detail in `ca-llc-fee-and-tax` | [FTB limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) |
| California estimates required | Expected 2026 tax of at least $500 ($250 separate) after withholding and credits | Detail in `ca-estimated-tax-540es` | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Health coverage penalty | Any month without coverage or an exemption | Detail in `ca-form-3853-coverage` | [2025 FTB 3853 instructions](https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf) |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Contractor paid by Zelle or bank-to-bank transfer | Not a payment-app (TPSO) payment: treat like a check for 1099-NEC (`us-1099-nec-issuance`) and test DE 542 |
| Contractor paid by card or through a payment app that settles the payment | No 1099-NEC from the client; the platform reports on 1099-K if its threshold is met |
| Contractor is an S corporation per the W-9, paid by check | Generally no 1099-NEC (corporation exception, except legal services) and no DE 542 (not an individual, sole proprietor or single-member LLC) |
| Contractor is a single-member LLC owned by an individual | Not a corporation: 1099-NEC test applies, and the DE 542 test applies |
| Payments to one contractor reach $600 only with the third invoice | DE 542 is due 20 calendar days after that third payment |
| Desk in a shared living room | Fails exclusive use: no home office deduction |
| Business owned by spouses as community property | Sole proprietorship or partnership is a reporting choice: refer |
| Two foreign accounts with highest balances of $6,000 and $5,000 | Together over $10,000: treat the FBAR test as met and route to `us-fbar-fatca-reporting` |
| Moved to California mid-year | Part-year resident, Form 540NR: stop and refer |

## Worked cases

### Case 1: when the DE 542 falls due

In 2026 the client pays an individual designer, who passes the ABC test, $250 on March 2 (day 61), $250 on April 1 (day 91) and $200 on May 1 (day 121). The running total first reaches $600 with the May 1 payment ($700). The DE 542 is due within 20 calendar days of that date: by May 21 (day 141). The federal 1099-NEC for the year is tested separately in `us-1099-nec-issuance`; condition (a) of the DE 542 needs that federal filing requirement, so confirm both together.

```oa-check
name: CA DE 542 due date from cumulative payments (2026)
inputs:
  p1: 250
  p2: 250
  p3: 200
  day_p3: 121
steps:
  - after_p2: p1 + p2
  - after_p3: after_p2 + p3
  - short_after_p2: max(600 - after_p2, 0)
  - due_day: day_p3 + 20
expected:
  after_p2: 500
  after_p3: 700
  short_after_p2: 100
  due_day: 141
```

### Case 2: does the client need California estimates for 2026? (decision)

A freelancer with a part-time W-2 job expects 2026 California tax of $4,000 and California withholding of $3,700. The balance is $300, under the $500 threshold in `ca-estimated-tax-540es`, so no 2026 California estimates are required. If a new contract lifts expected tax to $6,000, the balance is $2,300, so estimates are needed; at the 30% and 40% shares that is $690 by April 15 and $920 by June 15 (on the balance, before the 90%/100% test narrows it).

```oa-check
name: CA 2026 estimates required or not, intake test
inputs:
  tax_low: 4000
  tax_high: 6000
  withholding: 3700
  threshold: 500
steps:
  - balance_low: tax_low - withholding
  - needs_low: clamp(balance_low - threshold + 1, 0, 1)
  - balance_high: tax_high - withholding
  - needs_high: clamp(balance_high - threshold + 1, 0, 1)
  - q1_high: balance_high * 0.3
  - q2_high: balance_high * 0.4
expected:
  balance_low: 300
  needs_low: 0
  balance_high: 2300
  needs_high: 1
  q1_high: 690
  q2_high: 920
```

## When to refuse or refer

- Part-year resident or nonresident (Form 540NR), or income taxed by another state.
- A multi-member LLC or partnership, a corporation or S corporation election, or a spouse-owned business where the partnership or community-property choice is open.
- Employees, or any worker who fails the ABC test.
- Foreign accounts over the FBAR level, foreign income, or rental property.
- Disposals of digital assets or crypto received as payment, beyond simple reporting.
- Sales of goods where the sales tax treatment is unclear, or an existing CDTFA account with unfiled returns.
- Unfiled prior years, IRS or FTB notices, or amended returns.
- Any figure that cannot be traced to a document or an official page: flag it, do not estimate it.

## Filing and payment

| What | 2026 tax year | Where |
| --- | --- | --- |
| California estimated payments | 30% April 15, 2026; 40% June 15, 2026; none September 15; 30% January 15, 2027 | `ca-estimated-tax-540es` |
| Federal estimated payments | Four dates | `us-quarterly-estimated-tax` |
| DE 542 | Within 20 calendar days of reaching $600 paid or contracted | [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/) |
| Form 1099-NEC for 2026 payments | January 31, 2027 | `us-1099-nec-issuance` |
| LLC annual tax and fee, Form 568 | 15th day of the 4th month (annual tax); see the LLC skill | `ca-llc-fee-and-tax` |
| Federal and California returns | April 15, 2027; California extends filing (not paying) automatically to October 15, 2027 | `ca-540-individual-return` |

**2025 returns still open.** The California automatic extension ran to October 15, 2026, with payment due April 15, 2026. Use the 2025 figures in each return skill.

## Completion checklist

- [ ] Full-year California residency confirmed; entity and same federal and California classification recorded.
- [ ] Tax year fixed; 2025 and 2026 figures kept apart.
- [ ] Gross receipts reconciled to deposits, invoices and every 1099; excluded deposits explained.
- [ ] Digital asset question answered from the facts.
- [ ] Every person paid classified under the ABC test; 1099-NEC and DE 542 obligations listed with dates.
- [ ] Seller's permit trigger tested; city and county permits noted.
- [ ] LLC items routed to `ca-llc-fee-and-tax`.
- [ ] Home office and vehicle tested; health coverage recorded by month.
- [ ] California and federal estimates tested separately.
- [ ] California non-conformity items flagged for `ca-540-individual-return`.
- [ ] Out-of-scope items referred; handed to `us-ca-return-assembly`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FTB limited liability company page. Read for the same-classification sentence, the $800 annual tax and the doing-business conditions. | https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html | 2026-11-13 |
| 2025 Schedule CA (540) instructions. Read for "In general, California R&TC does not conform to the OBBBA". | https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html | 2026-11-13 |
| 2026 Instructions for Form 540-ES. Read for section B, the $500 and $250 test. | https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf | 2026-11-13 |
| 2025 Instructions for form FTB 3853. Read for the month-by-month coverage rule. | https://www.ftb.ca.gov/forms/2025/2025-3853-instructions.pdf | 2026-11-13 |
| EDD independent contractor reporting. Read for the three conditions, $600, 20 calendar days and the $24 and $490 penalties. | https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/ | 2026-11-13 |
| Labor and Workforce Development Agency, ABC test (through Firecrawl). Read for the three conditions. | https://www.labor.ca.gov/employmentstatus/abctest/ | 2026-11-13 |
| CDTFA permits and licenses. Read for the seller's permit sentence and CalGold. | https://www.cdtfa.ca.gov/services/permits-licenses.htm | 2026-11-13 |
| 26 CFR 1.401(k)-1 (eCFR). Read for (a)(6)(iii), the self-employed election deadline. | https://www.ecfr.gov/current/title-26/section-1.401(k)-1 | 2026-11-13 |

Not yet confirmed: whether the EDD will apply the DE 542 condition (a) by the federal 2026 1099-NEC threshold or keep $600 for every payee (the EDD page still prints $600 on 2026-11-13); the Borello exceptions to the ABC test (the EDD AB 5 page was not re-read).
