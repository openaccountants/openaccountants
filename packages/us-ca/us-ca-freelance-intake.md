---
name: us-ca-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their US federal or California state tax return AND mentions freelancing, self-employment, software development, contracting, sole proprietorship, or a single-member LLC. Trigger on phrases like "help me do my taxes", "prepare my 2025 return", "I'm a freelance developer", "I have an LLC in California", "I'm self-employed", "do my taxes as a contractor", or any similar phrasing where the user is a California-resident freelancer needing tax return preparation. This is the REQUIRED entry point for the Accora freelance developer tax workflow — every other skill in the stack (us-sole-prop-bookkeeping, us-schedule-c-and-se-computation, us-qbi-deduction, us-self-employed-retirement, us-self-employed-health-insurance, us-quarterly-estimated-tax, us-federal-return-assembly, ca-540-individual-return, ca-estimated-tax-540es, ca-smllc-form-568, ca-form-3853-coverage, us-1099-nec-issuance, us-ca-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow — the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured refusal sweep and profile questions instead of one-at-a-time prose. Built for speed — freelance software developers expect concise, direct interaction. California full-year residents only; sole proprietors and single-member LLCs disregarded for federal tax only.
version: 0.2
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California freelancer intake: scoping a sole proprietor or single-member LLC before the federal and California returns

## Scope and who it is for

This Guide is the intake step for a **full-year California resident** who works for themselves as a sole proprietor, or through a **single-member LLC that is disregarded** for federal tax. It is written for tax year 2026, with a dated section for 2025 returns that are still being finished on extension.

Intake does not compute the return. It decides three things:

- whether the client is in scope;
- which documents are needed;
- which later work each answer routes to.

The computation lives in two other Guides:

- `us-federal-return-assembly` covers Schedule C, Schedule SE, the self-employed deductions, QBI and Form 2210;
- `ca-540-individual-return` covers Form 540, Schedule CA (540) and California estimated tax.

The LLC's own California charges are covered in `ca-llc-fee-and-tax`. Figures were checked on 25 September 2026.

A single-member domestic LLC files Schedule C "unless you have elected to treat the domestic LLC as a corporation" ([Schedule C instructions](https://www.irs.gov/instructions/i1040sc)). California requires the same classification as the federal one: "An LLC must have the same classification for both California and federal tax purposes" ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)).

## Ask the client first

Ask the scope questions first. Any answer that points out of scope ends the intake for that item (see "When to refuse or refer").

- **Residency.** Did the client live in California for the whole tax year? A part-year resident or nonresident files Form 540NR, which is out of scope.
- **Entity.** Is it a sole proprietorship with no LLC, a single-member LLC, or something else? Has the client ever filed Form 8832 or Form 2553 (a corporation or S corporation election), or received a W-2 from their own business? Is the business owned with a spouse?
- **Tax year.** Which year is being prepared: 2025 (on extension) or 2026? Keep the two years' figures apart.
- **Filing status and dependents.** What is the filing status for the year, and who are the dependents? Several thresholds below are lower for married filing separately.
- **What the business does.** Does it provide services only, or does it also sell or lease physical goods? The answer decides whether a seller's permit is needed.
- **Who the client paid.** Did the client pay anyone for work in the year? For each person, get the name, entity type (from the person's Form W-9), the amount, how it was paid (check, bank transfer, card or payment app), and how the work was controlled.
- **Other income and assets.** Ask about wages, rental property, K-1s, capital gains, and digital assets. For foreign financial accounts, list every account and get **each account's highest balance** during the year. If those highest balances add up to more than $10,000, treat the FBAR test as met and route to `us-fbar-fatca-reporting`.
- **Prior year.** Get the prior-year federal and California returns, or at least federal AGI, federal total tax, California AGI and California total tax. These set the safe harbours for estimated tax.
- **Payments made.** List federal and California estimated payments with dates and amounts. For an LLC, list what was paid on FTB forms 3522 and 3536.
- **Health coverage by month.** Who was covered, by what kind of plan, and was Covered California coverage paid with an advance premium tax credit (Form 1095-A)?
- **Home office and vehicle.** Is part of the home used **regularly and exclusively** for the business? Is a vehicle used for business, and is there a mileage log?
- **Retirement plan.** What plan type (SEP, solo 401(k), SIMPLE or IRA), when was it set up, when was the deferral election made, and what was contributed and when? Test the timing like this ([Pub. 560](https://www.irs.gov/publications/p560)):
  - **New solo 401(k) adopted after year end.** "a sole proprietor with no employees can adopt a section 401(k) plan after the end of the tax year, provided the plan is adopted by the tax filing deadline (without regard to extensions)". This relief applies only when **all** of these hold: it is a **new** plan, it is the plan's **first plan year**, the owner is the **only participant**, and the elective deferrals are **paid to the plan** by the return due date **without extensions**.
  - **Existing 401(k) plan.** The deferral election for a year must be made by **31 December** of that year (the last day of the tax year for a calendar-year sole proprietor). The regulation says "a self-employed individual may not make a cash or deferred election with respect to compensation for a partnership or sole proprietorship taxable year after the last day of that year" ([Treas. Reg. §1.401(k)-1(a)(6)(iii)](https://www.law.cornell.edu/cfr/text/26/1.401%28k%29-1)). Only the deposit can follow later.
  - **Employer (profit-sharing) and SEP contributions.** These can be made up to the due date **including extensions** of the return. A SEP can also be set up as late as that date.
  - Route the timing rules to `us-secure-2-and-retirement-updates`, and the limits and deduction to `us-federal-return-assembly`.
- **Location.** Which city and county is the business in? This is needed for local permits.

## Documents to collect

- Business bank and card statements for the full year. For a disregarded LLC, include any personal account used for the business.
- Every Form 1099-NEC, 1099-MISC and 1099-K received, plus client invoices or a sales ledger. Income is reportable whether or not a form arrived (see step 2 below).
- Forms W-9 from everyone the client paid, and any contracts with them.
- Prior-year federal and California returns.
- Proof of estimated payments. Use the IRS online account and the client's MyFTB account; bank lines alone are not enough.
- Form 1095-A (Covered California) or other coverage records for each month.
- Retirement plan statements and the plan adoption document.
- A fixed-asset list with purchase dates and costs. California depreciation differs from federal, so both records are needed.
- For an LLC: the Secretary of State filing date, and FTB notices. For a seller: the CDTFA permit number.

## The method, step by step

1. **Confirm scope.** Check full-year residency, the entity and its classification, and the tax year. Stop and refer on any out-of-scope answer.
2. **Reconcile gross receipts.** Build receipts from the bank and the invoices, then tie them to the forms. The IRS says: "Whether or not you receive a Form 1099-K, you must still report any income on your tax return" ([IRS: Understanding your Form 1099-K](https://www.irs.gov/businesses/understanding-your-form-1099-k)). If the total in box 1 of the Forms 1099-NEC is more than the receipts reported, the Schedule C instructions require an explanation ([Schedule C instructions, line 1](https://www.irs.gov/instructions/i1040sc)). A payment app or online marketplace must issue Form 1099-K when a client's payments total over $20,000 in more than 200 transactions, but it may also issue one below that level. Personal transfers on a 1099-K are not income; record why each was excluded.
3. **Self-employment tax.** Schedule SE is needed if net earnings from self-employment are $400 or more ([IRS: Self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes)). The computation is done in `us-federal-return-assembly`.
4. **Home office.** A deduction needs **regular and exclusive** use of part of the home for business, and that part must be the principal place of business (or meet one of the other tests on the IRS page) ([IRS: Home office deduction](https://www.irs.gov/businesses/small-businesses-self-employed/home-office-deduction)). A desk in a room that is also used for living fails the exclusive-use test. Record the square footage of the office and of the whole home only if the tests are met.
5. **Digital assets.** Every federal return must answer "Yes" or "No" to the digital asset question. It asks whether, at any time in the year, the client received a digital asset "as a reward, award or payment for property or services" or sold, exchanged or otherwise disposed of one ([IRS: Digital assets](https://www.irs.gov/filing/digital-assets)). Holding only, with no receipt or disposal, is generally a "No". Buying with real currency without selling, and moving assets between the client's own wallets, are also "No", unless a transfer fee was paid in digital assets. Any disposal or crypto payment routes to capital-gains work.
6. **People the client paid (worker classification).** Classify each person before looking at information returns.
   - California uses the **ABC test**. A worker is an employee "unless the hiring entity satisfies all three" conditions: (A) the worker is free from the hiring entity's control and direction, both under the contract and in fact; (B) the work is outside the usual course of the hiring entity's business; and (C) the worker is customarily engaged in an independently established trade or business of the same kind ([LWDA: ABC test](https://www.labor.ca.gov/employmentstatus/abctest/)).
   - The EDD notes that some workers fall under exceptions where the Borello multifactor test applies instead. It also notes that employee wages are subject to California payroll taxes and payments to independent contractors are not ([EDD: Employee or independent contractor](https://edd.ca.gov/en/payroll_taxes/ab-5/)).
   - Anyone who is an employee means payroll registration and payroll returns. That is out of scope here; refer it.
7. **Information returns the client must file (as a payer).**
   - **Federal Form 1099-NEC.** File it for nonemployee compensation paid for services in the course of the trade or business, to someone who is not an employee.
     - The threshold is **$2,000 or more** for payments in 2026. For tax years beginning after 2025, "the minimum threshold amount ... increased to $2,000" ([Instructions for Forms 1099-MISC and 1099-NEC (2026)](https://www.irs.gov/instructions/i1099mec)).
     - For 2025 payments it was **$600 or more** ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)).
     - Payments to a corporation, including an LLC taxed as a C or S corporation, are generally not reported. Attorneys' fees are the exception.
     - Card payments, and payments settled through a **third party settlement organization** (TPSO: a payment app or online marketplace that settles the payment), are reported by the payment settlement entity on Form 1099-K, and "are not subject to reporting on Form 1099-MISC or Form 1099-NEC". The TPSO files a 1099-K only when the payee's total "exceeds $20,000 in more than 200 transactions" ([IRS: Understanding your Form 1099-K](https://www.irs.gov/businesses/understanding-your-form-1099-k)); below that, the client still files no 1099-NEC for it.
     - A transfer straight from one bank account to another (for example Zelle, or a transfer from the client's banking app) moves money between the two banks; it is **not** a card payment and is not settled by a TPSO. The Form 1099-K instructions also say "automated clearing houses do not qualify as TPSOs" ([Instructions for Form 1099-K](https://www.irs.gov/instructions/i1099k)). Treat it like a check: 1099-NEC if the $2,000 threshold is met.
     - Form 1099-NEC must be filed "on or before January 31" of the following year.
   - **California DE 542 (Report of Independent Contractors).** A payer must report to the EDD when **all** of these apply: (a) it must file a federal 1099-NEC or 1099-MISC for the services; (b) it pays **$600 or more**, or enters into a contract for **$600 or more**; and (c) the contractor is an individual, sole proprietor or single-member LLC. The report is due within 20 calendar days of paying $600, or of entering into a $600 contract, whichever is earlier. The penalty is **$24** per failure without good cause, and **$490** if the failure is intentional or the report is false ([EDD: Independent contractor reporting](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/)).
     - Condition (a) depends on the federal filing requirement, which rose to $2,000 for 2026. The EDD page still states $600 (checked 25 September 2026). For a 2026 payment between $600 and $2,000, confirm with the EDD before deciding that no DE 542 is due.
8. **Seller's permit.** The CDTFA says: "If you are doing business in California and intend to sell or lease tangible personal property subject to sales tax sold at retail, you are required to have a seller's permit" ([CDTFA: Permits and licenses](https://www.cdtfa.ca.gov/services/permits-licenses.htm)). A services-only freelancer does not meet that trigger. If the client sells hardware, prints or other goods, route to sales-tax work. Whether a particular digital product or bundle is taxable is a question for the CDTFA's own guidance; do not decide it at intake.
9. **Local permits and business tax.** A city or county business licence or business tax is set locally, so check the client's city and county. The CDTFA points to **CalGold** for "other federal, state, or local government permits that may be required for your business" (same CDTFA page). Record the city and the licence or account number.
10. **Single-member LLC charges (California).** An LLC that is organized in California, registered there, or doing business there must:
    - pay the **$800** annual tax by the 15th day of the 4th month of its tax year, on FTB form 3522;
    - estimate and pay the LLC fee by the 15th day of the 6th month, on FTB form 3536;
    - file Form 568 by the original due date ([FTB: Limited liability company](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)).

    The fee is owed when California total income is **$250,000** or more. It is **$900** from $250,000 up to, but not including, **$500,000**, and it rises in bands above that ([R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.)). The fee base is gross income **plus** cost of goods sold, assigned to California. It is not the bank-deposit total and not profit.

    The first-year exemption from the annual tax applied only to tax years beginning from 2021 through 2023 (FTB page above), so an LLC formed in 2024, 2025 or 2026 owes $800 for its first year. For a first taxable year beginning in 2027 to 2029, the annual tax is **$400** ([SB 180](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB180)). Route all of this to `ca-llc-fee-and-tax`. A sole proprietor with no LLC owes none of these charges.
11. **California differences to flag for the state return.** "In general, California R&TC does not conform to the OBBBA" ([Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)). At intake, flag the following for `ca-540-individual-return`:
    - any asset expensed federally under bonus depreciation or §179, which needs a separate California depreciation record ([FTB Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf));
    - HSA contributions;
    - the QBI deduction, which does not carry to California.
12. **Health coverage.** California has its own individual mandate. A return that cannot confirm full-year coverage for everyone in the household goes to FTB form 3853 to test for the individual shared responsibility penalty ([2025 Form 540 instructions, line 92](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)). Covered California coverage with an advance premium tax credit also needs federal Form 8962. That is handled in `us-federal-return-assembly`.
13. **Estimated tax, both governments.** Test next year's (and the current year's) payments with the rules below, and record any shortfall for Form 2210 (federal) and FTB form 5805 (California).
14. **Hand off.** Pass on the scope answers, the reconciled receipts, the list of people paid and their filings, open flags, and the payment history.

## Thresholds and figures, with years

| Item | Year | Figure | Source |
|---|---|---|---|
| Schedule SE required | 2026 and 2025 | Net SE earnings of $400 or more | [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |
| Form 1099-NEC filing threshold (payer) | Payments in 2026 | $2,000 or more | [i1099mec (2026)](https://www.irs.gov/instructions/i1099mec) |
| Form 1099-NEC filing threshold (payer) | Payments in 2025 | $600 or more | [i1099mec (2025)](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf) |
| Form 1099-K from a payment app or marketplace | Current IRS page | Over $20,000 in more than 200 transactions | [IRS](https://www.irs.gov/businesses/understanding-your-form-1099-k) |
| DE 542 contractor report | Current EDD page | $600 or more paid or contracted | [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/) |
| FBAR | Every year | Aggregate value of foreign accounts over $10,000 at any time (add each account's highest balance) | [FinCEN](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) |
| Federal estimated tax required | 2026 | Expected to owe at least $1,000 after withholding and credits | [Pub. 505](https://www.irs.gov/publications/p505) |
| California estimated tax required | 2026 | Expected to owe at least $500 ($250 MFS) | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| California LLC annual tax | 2026 | $800 | [FTB](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) |
| California LLC fee starts | 2026 | California total income of $250,000 or more | [R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| Safe harbours, federal and California | 2026 | Smaller of 90% of 2026 tax or 100% of 2025 tax; 110% if 2025 AGI over $150,000 | [Pub. 505](https://www.irs.gov/publications/p505); [540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |

### Estimated tax for 2026

**Federal** ([Pub. 505](https://www.irs.gov/publications/p505)).

- Payments are required if the client expects to owe at least $1,000 **and** expects withholding and credits to be less than the smaller of:
  - 90% of the 2026 tax; or
  - 100% of the 2025 tax. The 2025 return must cover 12 months.
- Use 110% in place of 100% if 2025 AGI was **more than** $150,000 ($75,000 if the 2026 filing status is married filing separately), unless at least two-thirds of gross income is from farming or fishing.
- Due dates: April 15, 2026; June 15, 2026; Sept. 15, 2026; Jan. 15, 2027.

**California** ([2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)).

- Payments are required if the client expects to owe at least $500 ($250 married/RDP filing separately) **and** expects withholding and credits to be less than the smaller of:
  - 90% of the 2026 tax; or
  - 100% of the 2025 tax, including AMT.
- Use 110% of the 2025 tax if 2025 California AGI was **more than** $150,000 ($75,000 MFS).
- If 2026 California AGI is **equal to or greater than** $1,000,000 ($500,000 MFS), the prior-year option is not available and the estimate must be based on the 2026 tax.
- Installments are 30% of the required annual payment by April 15, 2026, 40% by June 15, 2026, **nothing** for September 15, 2026, and 30% by January 15, 2027.
- Filing the 2026 return by January 31, 2027 and paying the whole balance replaces the fourth installment.
- The federal September payment still falls due even though California has none. Do not copy the California pattern to the IRS, or the other way round.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| 2025 AGI exactly $150,000 | Not "more than" $150,000, so the 100% prior-year test applies (federal and California) | [Pub. 505](https://www.irs.gov/publications/p505); [540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| 2026 California AGI exactly $1,000,000 | "Equal to or greater than", so there is no prior-year safe harbour for California | [540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| LLC with California total income exactly $250,000 | In the $900 band ("$250,000 or more") | [R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| Contractor paid $2,000 in 2026 by Zelle or another bank-to-bank transfer | Not a TPSO payment, so 1099-NEC is due ($2,000 or more) | [i1099k](https://www.irs.gov/instructions/i1099k); [i1099mec](https://www.irs.gov/instructions/i1099mec) |
| Contractor paid $1,999 in 2026 | Below the $2,000 federal 1099-NEC threshold; check the EDD position on DE 542 | [i1099mec](https://www.irs.gov/instructions/i1099mec) |
| Contractor paid by card, or through a payment app or marketplace that settles the payment (a TPSO) | No 1099-NEC from the client; the payment entity reports on 1099-K if its own threshold is met | [i1099mec](https://www.irs.gov/instructions/i1099mec) |
| Contractor is an S corporation (per W-9), paid by check | Generally no 1099-NEC (corporation exception), unless it is for legal services | [i1099mec](https://www.irs.gov/instructions/i1099mec) |
| Contractor is a single-member LLC owned by an individual | Not a corporation: 1099-NEC if paid $2,000 or more (2026 payments), and the DE 542 test applies | [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/) |
| Net SE earnings just under $400 | No SE tax, but Schedule C is still filed | [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |
| Two foreign accounts with highest balances of $6,000 and $5,000 in the year | Together over $10,000, so treat the FBAR test as met; refer to `us-fbar-fatca-reporting` | [FinCEN](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) |
| Desk in a shared living room | Fails exclusive use; no home office deduction | [IRS](https://www.irs.gov/businesses/small-businesses-self-employed/home-office-deduction) |
| Business owned by spouses as community property | May be treated as a sole proprietorship or as a partnership; the choice is a reporting position, so refer it | [Schedule C instructions](https://www.irs.gov/instructions/i1040sc) |

## Worked cases

**Case 1: ordinary 2026 intake, single-member LLC.** A single software contractor lived in Oakland all year. Her LLC was organized in 2023 and is disregarded. She sells services only.

- 2025 federal AGI was $140,000 and California AGI was $140,000. 2025 California tax was $8,000. She expects to owe more than $500 to California ([540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)).
- AGI was not over $150,000, so California's prior-year test is 100%: a required annual payment of up to $8,000. The installments are $2,400 by April 15, 2026, $3,200 by June 15, 2026, nothing in September, and $2,400 by January 15, 2027.
- The LLC's 2026 California total income is $180,000. That is below $250,000, so there is no LLC fee, but the $800 annual tax and Form 568 are due ([FTB](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html); [R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.)).
- No seller's permit is needed, because she sells no tangible goods. Record the city business licence.

**Case 2: boundary, LLC fee.** Same facts, but California total income is exactly $250,000. The LLC fee is $900, estimated on FTB form 3536 by June 15, 2026.

**Case 3: exclusion, payments to others in 2026.**

- **$2,500 by bank transfer to an individual designer** who is free from control and runs her own business. File a 1099-NEC by January 31, 2027, and a DE 542 within 20 days of paying $600 ([i1099mec](https://www.irs.gov/instructions/i1099mec); [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/)).
- **$2,500 by check to a web-hosting S corporation.** No 1099-NEC under the corporation exception, and no DE 542 because the payee is not an individual, sole proprietor or single-member LLC ([i1099mec](https://www.irs.gov/instructions/i1099mec)).
- **$1,500 through a payment app (a TPSO) to an individual.** It is not reportable by the client on Form 1099-NEC. The TPSO reports it on Form 1099-K only if the payee's total from that platform exceeds $20,000 in more than 200 transactions ([i1099mec](https://www.irs.gov/instructions/i1099mec); [IRS: Understanding your Form 1099-K](https://www.irs.gov/businesses/understanding-your-form-1099-k)).
- **$2,500 by Zelle to another individual contractor.** A bank-to-bank transfer is not a TPSO payment, so the client files a 1099-NEC by January 31, 2027, and the DE 542 test applies as above ([i1099k](https://www.irs.gov/instructions/i1099k)).

**Case 4: the 2026 threshold change.** A contractor was paid $1,200 in 2025 and $1,200 in 2026 ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf); [2026 instructions](https://www.irs.gov/instructions/i1099mec)).

- **2025:** a 1099-NEC was due by January 31, 2026, because $1,200 is $600 or more ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)).
- **2026:** no 1099-NEC is required, because $1,200 is below $2,000. The DE 542 answer for 2026 needs EDD confirmation (step 7; [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/)).

**Case 5: refer.** A client moved from Oregon to California in July. This is a part-year resident, so Form 540NR is needed. Stop the intake and refer.

## When to refuse or refer

- The client was a part-year resident or a nonresident (Form 540NR), or has income taxed by another state.
- A multi-member LLC or partnership (Form 1065), an S corporation or C corporation election, or a spouse-owned business where the partnership or community-property choice is open.
- Employees, or any worker who fails the ABC test: payroll registration and returns are needed.
- Foreign accounts whose highest balances add up to more than $10,000 (FBAR), foreign income, or rental property.
- Disposals of digital assets or crypto received as payment, beyond simple reporting.
- Sales of tangible goods where the sales-tax treatment is unclear, or an existing CDTFA account with unfiled returns.
- Unfiled prior years, IRS or FTB notices, or amended returns.
- Any figure that cannot be traced to a document or an official page. Flag it; do not estimate it.

## Filing and payment steps with deadlines

| What | 2026 tax year | Source |
|---|---|---|
| Federal estimated payments | April 15, June 15 and Sept. 15, 2026; Jan. 15, 2027 | [Pub. 505](https://www.irs.gov/publications/p505) |
| California estimated payments | 30% April 15, 2026; 40% June 15, 2026; none September 15; 30% January 15, 2027 | [540-ES](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| LLC annual tax (FTB form 3522) | 15th day of the 4th month of the tax year | [FTB](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) |
| LLC fee estimate (FTB form 3536) | 15th day of the 6th month of the tax year | [FTB](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) |
| Form 1099-NEC for 2026 payments | January 31, 2027 | [i1099mec](https://www.irs.gov/instructions/i1099mec) |
| DE 542 | Within 20 calendar days of reaching $600 paid or contracted | [EDD](https://edd.ca.gov/en/payroll_taxes/independent_contractor_reporting/) |
| Federal and California returns | Due in April 2027; see the two return Guides for extension rules | `us-federal-return-assembly`, `ca-540-individual-return` |

### 2025 returns still open (dated section)

- **Federal.** A Form 4868 extension moves the filing date to October 15, 2026, for most calendar-year taxpayers ([Form 4868](https://www.irs.gov/pub/irs-pdf/f4868.pdf)). It does not extend the time to pay.
- **California.** "California grants an automatic extension until October 15, 2026 to file your return, although your payment is still due by April 15, 2026" ([FTB due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-personal.html)).
- **Figures for 2025.** Use the 2025 figures in both return Guides. The 1099-NEC threshold for 2025 payments was $600 or more ([2025 instructions](https://www.irs.gov/pub/irs-prior/i1099mec--2025.pdf)), and those forms were due January 31, 2026. If they were missed, file late and flag the penalty exposure for review.
- **Estimated tax for 2025.** Test the 2025 payments against the 2024 tax with the same 90%, 100% and 110% rules, using the 2025 versions of Pub. 505 and form 540-ES ([Pub. 505](https://www.irs.gov/publications/p505)).

## Completion checklist

- [ ] Full-year California residency confirmed; entity and federal/California classification recorded.
- [ ] Tax year fixed; 2025 and 2026 figures kept apart.
- [ ] Gross receipts reconciled to bank deposits, invoices and every 1099-NEC, 1099-MISC and 1099-K. Excluded deposits explained.
- [ ] Digital asset question answered from the facts, not assumed.
- [ ] Every person paid classified under the ABC test. The 1099-NEC ($2,000 for 2026, $600 for 2025) and DE 542 obligations listed, with dates.
- [ ] Seller's permit trigger tested; city and county permits noted.
- [ ] LLC: $800 annual tax, fee band on California total income, form 3536 estimate and Form 568 routed to `ca-llc-fee-and-tax`.
- [ ] Home office tested for regular and exclusive use; vehicle records requested if used.
- [ ] Health coverage recorded by month; FTB form 3853 and Form 8962 flagged where needed.
- [ ] Federal and California safe harbours tested, and the next year's schedule set (federal four dates; California 30%, 40%, nothing, 30%).
- [ ] California non-conformity items (depreciation, HSA, QBI) flagged for `ca-540-individual-return`.
- [ ] Out-of-scope items referred; a credentialed preparer reviews before filing.

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
