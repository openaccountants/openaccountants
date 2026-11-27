---
name: au-div7a
description: >
  Use this skill whenever asked about Division 7A of the ITAA 1936 -- private company loans, payments or debt forgiveness to shareholders or their associates, complying loan agreements, minimum yearly repayments, the benchmark interest rate, distributable surplus, unpaid present entitlements (UPEs) to corporate beneficiaries after Bendel, use of company assets by shareholders, or deemed dividends. Trigger on phrases like "Div 7A", "Division 7A", "shareholder loan", "director loan account", "debit loan", "minimum yearly repayment", "benchmark interest rate", "complying loan", "deemed dividend", "distributable surplus", "UPE", "bucket company", "unpaid present entitlement", or when a GL shows debit balances in shareholder/director accounts. ALWAYS read this skill before touching any Div 7A work.
version: 1.2
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
---

# Australia Division 7A -- Private Company Loans Guide v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Period and proof scope.** The original tax_year 2026 denotes the 2026–27 income year (1 July 2026–30 June 2027). Rates below apply to companies with a 30 June year end; a substituted accounting period needs its own rate and dates. This update checks the law and calculations; it does not renew the frozen human approval. Historical guidance-status and proposal points expressly held below are not usable tax positions.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 7A (ss 109B-109ZE) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Benchmark interest rate (2026-27) | 8.77% (2025-26: 8.37%; 2024-25: 8.77%); 30 June year end only. [ATO rates](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate) |
| Complying loan maximum terms | 7 years for other loans; 25 years where 100% secured by registered real-property mortgage with market value (net of prior-ranking liabilities) >= 110% of the loan when first made; refinancing may shorten these terms. [s 109N](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) |
| Complying agreement deadline | In writing BEFORE the company's lodgment day (earlier of due date and actual lodgment -- s 109D(6)) |
| First minimum yearly repayment | Due in the income year AFTER the year the loan is made |
| Deemed dividend cap | Distributable surplus (s 109Y); proportional reduction across provisional dividends |
| UPE to corporate beneficiary | NOT a Div 7A loan while the company stays passive (*Bendel* [2026] HCA 18) -- s 100A and Subdiv EA risks survive |
| Contributor | Open Accountants |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown lodgment day | Establish both due date and actual lodgment; show any estimate as an urgent, unconfirmed scenario. New-loan repayment/agreement deadline differs from the annual MYR deadline. |
| Unknown loan agreement status | Urgently obtain the agreement; do not certify compliance from missing records. Discretionary relief is not automatic. |
| Debit balance in shareholder/director account | Treat as a Div 7A loan candidate until characterised |
| Unknown distributable surplus | Compute exposure at full value; flag the s 109Y cap as unquantified |
| UPE on trust balance sheet | Passive UPE = no Div 7A loan (post-Bendel), but flag s 100A / Subdiv EA screen (T2-1, T2-2) |
| Company asset used privately | Assume s 109CA payment at arm's-length value; check minor (<$300) and licence-fee carve-outs |
| Repayment near year end followed by redraw | Obtain purpose and funding evidence; dates alone do not establish the reasonable-person test. |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Obtain the company GL (shareholder/director/associate loans and drawings), prior-year Div 7A schedules, dated loan agreements and terms, both return due date and actual lodgment history. Obtain trust deeds and distribution minutes for UPEs, financial statements for distributable surplus, declared-dividend and mutual set-off evidence, asset-use facts and consideration. Reconcile the full repayment history, pre-lodgment repayments, registered security and inception valuations, franking records, and prior ATO correspondence/discretion applications. A GL label is a candidate, not proof of a loan or relationship.

### Refusal catalogue

- **R-AU-D7A-1 — Section 100A:** map the distribution, beneficiary and other person's benefit. The old assertion of trustee top-marginal tax with an unlimited amendment period is held, not a determination of this case. Check this point with one of our partner accountants.
- **R-AU-D7A-2 — Interposed entities and Subdivision EA/EB:** map every payment, loan, forgiveness and trust entitlement. The old Subdiv E/EA/EB limb-by-limb determination instructions are held for specialist application; do not assume one Commissioner's determination rule applies to every limb. Check this point with one of our partner accountants.
- **R-AU-D7A-3 — Discretion:** assemble mistake, correction, timing, hardship and prior-history evidence; do not promise relief under ss 109Q, 109RB or 109RD. Check this point with one of our partner accountants.
- **R-AU-D7A-4 — Planning:** compute current ordinary exposure below; forgiveness, refinancing, conversion and restructuring strategy is held. Check this point with one of our partner accountants.

## Section 3 -- GL sweep library

**GL sweep library**

| GL pattern | Likely issue | Action |
| --- | --- | --- |
| Debit balance -- shareholder / director loan account | s 109D loan candidate | Loan register (Section 7); agreement status; MYR check |
| Drawings account not cleared to salary/dividend | Payments (s 109C) or loan | Establish the actual transaction; payment-to-loan conversion has its own s 109D(4A) deadline |
| "Loan -- related trust" (asset side) | Actual loan back from company to trust | Div 7A loan -- Bendel does NOT help actual loans |
| UPE / beneficiary entitlement owed TO the company (in the trust's books) | Post-Bendel: not a loan while passive | s 100A / Subdiv EA screen; do not convert without advice |
| Motor vehicles, boats, property with private use by shareholders | s 109CA asset-use payment | Arm's-length value less consideration; minor/licence carve-outs |
| Journal writing off a related-party receivable | s 109F forgiveness | Deemed dividend at year end, subject to surplus |
| Interest income at exactly the benchmark rate | Existing complying loan | Verify MYR actually paid, not just interest accrued |

Div 7A work starts with the balance sheet, not the loan register the client says exists.

## Section 4 -- Worked examples

### Example 1 -- New loan, saved by a complying agreement

Company advances $100,000 to a shareholder in March 2027 (2026-27 year). Return due date assumed 15 May 2028 (tax-agent lodgment program) and lodged that day, so lodgment day = 15 May 2028 -- an earlier due date or earlier actual lodgment would move the deadline, so establish both dates first. A written 7-year complying agreement at >= benchmark interest is signed 1 April 2028 -- before lodgment day.

No deemed dividend in 2026-27 (s 109N). The first minimum yearly repayment falls due in 2027-28, computed with the 2027-28 benchmark rate.

### Example 2 -- Minimum yearly repayment arithmetic

Amalgamated 7-year loan made in 2025-26; $100,000 unrepaid at 30 June 2026. Assume no qualifying repayments before that loan year’s lodgment day that would reduce first-year principal, and no special refinancing. MYR for 2026-27 (benchmark 8.77%):

```
Remaining term T = 7 - (years between end of loan year [30 Jun 2026]
                        and end of prior year [30 Jun 2026]) = 7
MYR = P x I / (1 - (1/(1+I))^T)
    = $100,000 x 0.0877 / (1 - (1/1.0877)^7)
    = $8,770 / 0.444817
    = $19,716 (nearest dollar)
```

### Example 3 -- Shortfall, capped by distributable surplus

Same loan; the shareholder repays only $10,000 in 2026-27. Shortfall = $9,716 -> deemed dividend at 30 June 2027, but only up to the company's distributable surplus (s 109Y). If surplus is $4,000 and there are no other provisional dividends, the dividend is $4,000. Where s 109Y reduces a dividend, give the recipient a written statement as soon as possible after year end; multiple provisional dividends share the cap proportionally. The displayed $19,716 and $9,716 are nearest-dollar illustrations; retain cents in the working paper.

### Example 4 -- UPE to a bucket company, post-Bendel

Trust resolves a $150,000 distribution to its corporate beneficiary in June 2027; the entitlement remains unpaid, and the company does nothing to call for payment.

**Not, of itself, a s 109D loan:** on the expressly passive facts, the UPE alone does not create a loan, whether held on separate trust or not ([ATO DIS paragraphs 26–39](https://www.ato.gov.au/law/view/document?DocID=LIT%2FICD%2FM47%2F2025%2F00001)). This is not a clearance under s 100A or Subdiv EA/EB. Read the deed, resolutions, accounts and dealings. If steps actually satisfy or convert the entitlement into a s 109D(3) loan, it stays a loan; Bendel does not reinstate the UPE. A demand, promissory note, variation or other active dealing requires its own characterisation; no automatic outcome is supplied. Check this point with one of our partner accountants.

### Example 5 -- Private use of a company asset

Company-owned holiday house used by the shareholder's family for 2 weeks; market rent $800/week; nothing paid. Assume the users are established shareholders/associates and company permission/right is evidenced.

s 109CA payment = arm's-length value less consideration = $1,600 -> deemed dividend at year end (subject to surplus). Carve-outs checked: not minor (>= $300 notional value), no licence fee paid (a market-rate licence fee would zero it), none of the dwelling exceptions apply. Continuing availability re-tests at the start of each income year.

### Example 6 -- The repay-and-redraw trap

Shareholder repays $20,000 on 25 June 2027, redraws $25,000 on 15 July 2027. A reasonable person concludes the repayment was intended to be re-borrowed: s 109R disregards the $20,000 for MYR purposes. A genuine set-off of a dividend payable by the same company to that borrower is preserved by s 109R(3); document mutual obligations and the effective payment. Other preserved payments and the specific refinancing exceptions are in Rule 9.

## Section 5 -- Tier 1 rules

### Rule 1 -- The three trigger events

- **The three trigger events** — Payments (s 109C, including s 109CA asset use), loans (s 109D), and debt forgiveness (s 109F) by a private company to a shareholder or associate (current or former, on the reasonable-person test) are deemed unfranked dividends at the end of the company's income year -- each capped by distributable surplus (Rule 8). Franking exceptions: the s 109RB discretion can allow franking, and s 109RC applies to a statutory family law obligation, with franking at the company’s benchmark franking percentage (or 100% if it has none), subject to Part 3-6.  _(s 109C, s 109CA, s 109D, s 109F; s 109RB; s 109RC)_
- **Associate:** s 109ZD imports s 318. A director title alone does not establish the shareholder/associate relationship. The old relatives/partners/spouses/children/trust-beneficiary/controlled-company summary is an incomplete checklist, not a connected-party conclusion. Full s 318 classification is held where the relationship is not established. Check this point with one of our partner accountants.

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 2 -- Loans and the lodgment-day escape

- **Loans and the lodgment-day escape** — A loan is a deemed dividend unless, before the LODGMENT DAY (earlier of the return's due date and actual lodgment -- s 109D(6)): it is fully repaid, or a complying s 109N agreement is in place. Loan is defined widely: advances, provision of credit or any other form of financial accommodation (s 109D(3)).  _(s 109D(6); s 109N; s 109D(3))_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 3 -- Complying loan criteria (s 109N)

- **Complying loan criteria** — All three, before lodgment day: written agreement; interest for each year after the loan year at or above that year's benchmark rate; term within the maximum -- 7 years unsecured, or 25 years where 100% of the loan is secured by a registered mortgage over real property whose market value (net of prior-ranking secured liabilities) is at least 110% of the loan when first made.  _(s 109N)_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 4 -- Benchmark interest rate

- **Benchmark interest rate 2026-27** — 8.77% (2025-26: 8.37%; 2024-25: 8.77%) for 30 June companies (RBA Indicator Lending Rates -- bank variable housing loans rate last published before the start of the income year; always match the rate to the year being computed)  _(s 109N(2))_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 5 -- Amalgamated loans and minimum yearly repayments (s 109E)

Constituent loans to the same entity, made in the same income year, unrepaid before lodgment day and saved by s 109N, amalgamate only if they share the same maximum term. Keep separate amalgamated loans separate. The amalgamated principal is the qualifying constituent amounts still unpaid before that loan year’s lodgment day (s 109E(3)).

From the year after the loan year, pay each MYR **within that income year** (30 June for these examples), not by the later return-lodgment day. [Sections 109E(1)–(7)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html) and [ATO manual computation](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/in-detail/division-7a-loans):

```
MYR = P × I / (1 − (1 / (1 + I))^T)
P = prior-year-end unpaid amalgamated principal, subject to the first-year adjustment below
I = current income year's benchmark rate
T = longest constituent term minus years between the end of the loan year and end of the prior year
Round that difference UP if fractional: s 109E(6), not s 109E(7).
```

**First-year adjustment:** qualifying repayments before the loan year’s lodgment day reduce the amalgamated opening principal, even when paid after that year end. Do not also count those payments towards the following year’s MYR. In later years use the unrepaid amalgamated principal at the prior year end. Section 109E(7) allocates payments on the basis of benchmark interest on the balance from time to time; accrued interest alone is not an actual repayment. An unpaid MYR shortfall is the provisional dividend, subject to s 109Y and any applicable s 109Q relief. Special security/refinancing changes under ss 109E(3A)–(3B), 109N(3A)–(3D) require a fresh schedule. Check this point with one of our partner accountants.

### Rule 6 -- Payments and asset use (ss 109C, 109CA)

- **Payments and asset use** — Payment = amounts paid/credited/transferred to, on behalf of, or for the benefit of the entity; property transfers valued at arm's length less consideration. A loan is not a payment. Use of a company asset (including under lease/licence) is a payment at first permitted use, or first right to use when the provider cannot use it or provide it to another entity; continuing use/right is a separate payment at the start of each later income year of the entity; value = arm's-length amount for the use less consideration given. Carve-outs: minor use (< $300 notional value, s 58P criteria), otherwise-deductible use, certain dwellings, and NIL where an arm's-length licence fee is paid.  _(ss 109C, 109CA; s 58P)_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 7 -- Debt forgiveness (ss 109F, 109G)

- **Debt forgiveness** — s 109F covers forgiveness, specified debt parking and a reasonable-person conclusion that the company will not insist on payment; only the first forgiveness counts. Discharge by a transfer of property is excluded from s 109F(3), but the transfer has its own payment valuation. The dividend is the forgiven amount, subject to s 109Y. Section 109G excludes debts owed by another company outside its trustee capacity, forgiveness because the debtor becomes bankrupt or under Part X of the Bankruptcy Act 1966, and qualifying loans already treated as dividends under s 109D (or former s 108). Earlier s 109E dividends instead reduce the forgiveness dividend dollar for dollar, not below zero. The s 109G(4) hardship discretion requires undue hardship, capacity to repay when incurred, and loss of foreseeable capacity through circumstances beyond the debtor's control; it is not automatic. [Sections 109F–109G](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

**Estate hold:** the original shareholder-death/executor case and ATO ID 2012/77 legal-personal-representative outcome are preserved as a non-usable question. Do not treat death as evidence of an actual forgiveness or certify an estate liability/result from this Guide. Check this point with one of our partner accountants.

### Rule 8 -- Distributable surplus (s 109Y)

- **Distributable surplus** — ``` Distributable surplus = Net assets + Division 7A amounts - Non-commercial loans - Paid-up share value - Repayments of non-commercial loans ``` Net assets are the non-negative excess of accounting-record assets over present legal obligations and the specified depreciation, annual/long-service leave, intellectual-property/trade-mark amortisation and prescribed provisions. The Commissioner may substitute values for significant asset or provision under/overvaluation. "Division 7A amounts" = current-year s 109C and s 109F dividends only. Where total provisional dividends exceed the surplus, each is reduced proportionally and the company must give each affected recipient a written statement as soon as possible after year end showing distributable surplus and the total provisional dividends. Apply the statutory definitions of non-commercial loans, paid-up share capital and repayments; these are not ordinary-language labels or a retained-earnings shortcut.  _(s 109Y)_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 9 -- Anti-avoidance on repayments (s 109R)

A payment is disregarded where a reasonable person, on all circumstances, would conclude that the borrower intended at payment to obtain company loans totalling a similar or larger amount, or had already obtained such loans to fund that payment. Two dates alone are insufficient. This affects new-loan repayment, MYR and principal computations.

Section 109R(3) preserves genuine set-offs of a company dividend payable to that borrower; specified work/income-support withholding payments and benefits, and payments covered by TAA Schedule 1 s 12-55; and the qualifying unpaid arm's-length property-transfer balance. Section 109R(4) preserves an actual payment by another entity of an amount it owes the borrower that is assessable to the borrower in that or an earlier year. Document the actual obligations and payment.

**The exception list is not limited to set-offs.** Sections 109R(5)–(7) also preserve specified refinancing: qualifying arm's-length subordination caused by circumstances beyond the borrower's control; 7-year to 25-year refinancing with the statutory term reduction; and 25-year to 7-year refinancing with any required reduction. Do not apply an exception from its label alone; full conditions and term changes need specialist confirmation. Check this point with one of our partner accountants. [Section 109R and s 109N(3A)–(3D)](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html).

### Rule 10 -- Exclusions and the discretion

- **Exclusions and the discretion** — s 109K: payments/loans to other companies (not as trustee) excluded. s 109L: amounts otherwise assessable or made non-assessable elsewhere. s 109M: loans in the ordinary course of business on usual arm's-length terms. s 109RB: the Commissioner may disregard a deemed dividend (or allow franking) for honest mistakes/inadvertent omissions -- factors include corrective action and speed, prior history; escalate applications (R-AU-D7A-3).  _(ss 109K, 109L, 109M, 109RB)_

Source: [ITAA 1936](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27.

### Rule 11 -- UPEs after Bendel: operative boundary and archived status matrix

The High Court dismissed the appeal in *Commissioner of Taxation v Bendel* [2026] HCA 18 on 10 June 2026 (majority 5:2). The [ATO decision impact statement](https://www.ato.gov.au/law/view/document?DocID=LIT%2FICD%2FM47%2F2025%2F00001), issued 26 June 2026 with comments due 24 July 2026, accepts that passive UPEs, without more, are not s 109D loans. Apply the actual-dealings boundary in Example 4; s 100A and Subdiv EA risks survive.

The original **1 August 2026** matrix remains identifiable below. The prior sweep read the review notices on 21 November; that did not prove every product's current substantive application or a completed withdrawal. For any current reliance on a ruling, withdrawal protection or proposed legislation, the following rows are **non-usable holds**, not a substitute for operative law:

| Original item | Destination / limit |
| --- | --- |
| TD 2022/11 | DIS paragraph 43 announces withdrawal. Do not infer a completed withdrawal, or use its inconsistent passive-UPE rule. Current instrument status/application held. Check this point with one of our partner accountants. |
| TR 2010/3 | Historical withdrawal from 1 July 2022 and possible pre-July 2022 arrangement protection: individual reliance held. Check this point with one of our partner accountants. |
| TR 2022/4 and PCG 2022/2 | DIS paragraph 44 lists these s 100A products for review; their full current content and arrangement-specific application held. Check this point with one of our partner accountants. |
| PCG 2017/13, TR 2015/4, TD 2015/20, TD 2011/15 | All remain in the topic inventory. DIS paragraph 44 lists review, not a blanket conclusion that none has since been withdrawn. Current status/application held. Check this point with one of our partner accountants. |
| Withdrawn-ruling protection / TAA Schedule 1 s 358-20(3) | DIS paragraph 45 describes favourable protection for schemes begun before withdrawal; whether a particular scheme qualifies is held. Check this point with one of our partner accountants. |
| 2018–19 Budget UPE proposal / prospective Royal Assent start | Preserve as an unresolved legislative-status question; do not call it operative law or certify its current unenacted status. Check this point with one of our partner accountants. |
| 2026–27 Budget trust proposals | Original unverified rates/dates and offset/rollover questions are retained under Sources: Not yet confirmed. No enacted-status, eligibility or planning conclusion is supplied. Check this point with one of our partner accountants. |

Practical computation remains available: a passive UPE alone does not supply an ordinary loan principal; an actual company-to-trust loan or genuinely converted UPE is tested as a loan under ss 109D/109N. Refer the surviving trust and interposed-entity questions in Section 2.

## Section 6 -- Tier 2 catalogue

### T2-1 -- s 100A screen

- **s 100A screen** — **Trigger:** UPE + benefits flowing to someone other than the presently entitled beneficiary, or distribution patterns outside ordinary family/commercial dealing. **Action:** refuse analysis (R-AU-D7A-1); document the pattern; escalate.  _(s 100A)_

### T2-2 -- Subdivision EA/EB

- **Subdivision EA/EB** — **Trigger:** the trust owing the UPE makes payments or loans to the company's shareholders/associates. **Action:** map flows; escalate (R-AU-D7A-2).  _(Subdivision EA/EB)_

### T2-3 -- 25-year loan security adequacy

- **25-year loan security adequacy** — **Trigger:** secured loan claimed; valuation or registration unverified. **Issue:** 110% net-of-prior-ranking test applies AT the time the loan is first made. **Action:** sight the registered mortgage and contemporaneous valuation; flag gaps.

### T2-4 -- Distributable surplus valuation

- **Distributable surplus valuation** — **Trigger:** net assets in the accounts look under/overstated (e.g. assets at historical cost, unrecorded liabilities). **Issue:** Commissioner's substitution power. **Action:** flag; do not self-adjust values.

### T2-5 -- Trust minimum-tax horizon (held proposal inputs)

For planning touching 2028+, retain all original proposed dates, rates and offset/rollover questions in Rule 11. These are not usable law or a forecast. Check this point with one of our partner accountants.

### T2-6 -- Loans that are really wages

- **Loans that are really wages** — **Trigger:** regular round-amount "loans" matching a pay cycle. **Issue:** may be salary/wages (PAYG withholding, super) rather than Div 7A loans -- different regime entirely. **Action:** characterise with the client; flag both exposures.

## Section 7 -- Excel working paper template

```
AUSTRALIA DIVISION 7A -- LOAN REGISTER
Company: [name]   Income year: 2026-27   Lodgment day: [earlier of due date / lodged]
Prepared: [date]

PER COUNTERPARTY (shareholder / associate)
  Name and relationship:          [____]
  Opening balance (per prior WP): AUD [____]
  New advances this year:         AUD [____]
  Agreement (written, pre-lodgment-day, rate >= benchmark, term OK): [YES/NO/PENDING]
  Term / security (7yr | 25yr + registered mortgage + 110% test at inception): [____]
  Prior-year amalgamated principal, first-year adjustment reconciled (P): AUD [____]
  Benchmark rate (I, current year): 8.77%
  Remaining term (T, rounded up):  [____]
  MYR = P x I / (1 - (1/(1+I))^T): AUD [____]
  Repayments made (excl. s 109R-disregarded; incl. valid set-offs): AUD [____]
  Shortfall:                       AUD [____]
  s 109CA asset-use payments:      AUD [____]
  Forgiveness events:              AUD [____]

DISTRIBUTABLE SURPLUS (s 109Y)
  Net assets:                      AUD [____]
  + Division 7A amounts (109C/109F this year): AUD [____]
  - Non-commercial loans:          AUD [____]
  - Paid-up share value:           AUD [____]
  - Repayments of non-commercial loans: AUD [____]
  = Distributable surplus:         AUD [____]
  Provisional dividends total:     AUD [____]
  Proportional reduction applied:  [YES/NO -- written statements issued?]

UPE SCREEN (post-Bendel)
  UPEs owed to the company:        AUD [____]
  Company action taken (calls, conversion, notes)? [____]
  s 100A / Subdiv EA flags:        [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

## Section 8 -- Reading guide

1. Balance sheet first: every related-party debit balance is a candidate until characterised.
2. Establish both new-loan lodgment day and the annual MYR year-end deadline. Do not use the return deadline for an existing loan’s MYR. Late discretionary relief requires an actual decision.
3. MYR uses the current year’s benchmark and prior-year amalgamated principal, after the first-year pre-lodgment adjustment in Rule 5. Do not count an adjusted payment twice.
4. Interest accrued is not repayment: the MYR must actually be paid (or validly set off).
5. UPEs: check the trust's books, not just the company's -- the company's balance sheet may not show the entitlement.

## Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep both company and any trust balance sheets per Section 3
2. Build the loan register with agreement status UNKNOWN flagged per loan
3. Compute provisional MYR scenarios only when loan year, term, first-year adjustment and 30 June company scope are established; otherwise leave an explicit input hold
4. Compute distributable surplus from the accounts as given
5. **Flag:** "Register built from financial statements only. Agreements, security documents, repayment evidence and trust distribution minutes not sighted. Lodgment day unconfirmed. Reviewer must confirm before any position is taken."

## Section 10 -- Reference material

### Key figures

**Key figures**

| Item | Value |
| --- | --- |
| Benchmark rate 2026-27 / 2025-26 / 2024-25 | 8.77% / 8.37% / 8.77% |
| Maximum terms | 7 years unsecured; 25 years secured (110% net-value test at inception) |
| First MYR | Income year after the loan year |
| Asset-use minor exception | < $300 notional value (s 58P criteria) |
| Deemed dividend character | Unfranked (exceptions: s 109RB discretion; s 109RC family-breakdown dividends frankable) |

## Sources

| Source / operative use | Official source and date read |
| --- | --- |
| ITAA 1936, compilation 193, 1 October 2026: ss 109C–109G, 109K–109N, 109R, 109RB–109RD, 109Y and 109ZD | [Federal Register, operative text](https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html), read 2026-11-27. Formula definitions and statutory exceptions read; not a claim to have read the whole Act. |
| Current and historical benchmark rates; substituted accounting periods | [ATO rates](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate), read 2026-11-27 from indexed official text (ordinary direct access returned HTTP 403). |
| MYR formula/manual steps and first-year principal adjustment | [ATO loans](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/in-detail/division-7a-loans), read 2026-11-27 from indexed official text; cross-checked to s 109E. |
| Bendel operative UPE boundary, actual converted loans, surviving trust risks, guidance review | [ATO DIS, paragraphs 26–45](https://www.ato.gov.au/law/view/document?DocID=LIT%2FICD%2FM47%2F2025%2F00001), read 2026-11-27 from indexed official text; prior 2026-11-21 reading of the court order and relevant majority reasoning reused, not a new whole-judgment review. |
| Generally unfranked character | [ATO dividend treatment](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/payments-and-other-benefits-affected/tax-treatment-of-division-7a-dividends), read 2026-11-27 from indexed official text; family-law conditions checked in s 109RC. |
| Asset-use minor-benefit limit | [ATO use of assets](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/private-company-benefits-division-7a-dividends/in-detail/division-7a-use-of-assets), read 2026-11-27 from indexed official text; valuation and other exclusions checked in s 109CA. |

Not yet confirmed: original proposal inputs only — proposed 30% minimum trust tax from 1 July 2028, corporate-beneficiary offset denial, consultation close 31 July 2026, restructure rollover from 1 July 2027, and the 2018–19 UPE proposal’s prospective Royal Assent start. These inputs are preserved for the specialist question; none is certified as operative or currently unenacted. Also held: current individual guidance withdrawal/application statuses and protected historical arrangements; estate/LPR outcome under ATO ID 2012/77; full s 318 connected-party classification; fact-specific s 100A, Subdiv E/EA/EB, dwelling-exception, hardship, refinancing and restructure conclusions; all Rule 11 proposal inputs and their current enacted status. These narrow points remain non-usable holds. Check this point with one of our partner accountants.

### Test suite

**Test 1:** $100,000 unrepaid at prior year end, 7-year loan made last year, 2026-27 MYR; no additional qualifying pre-lodgment repayment or refinancing. -> T = 7; MYR = $8,770 / 0.444817 = $19,716.

**Test 2:** Loan made 2024-25 (7-year), MYR for 2026-27. -> T = 7 - 1 = 6.

**Test 3:** No written agreement by lodgment day, loan unrepaid, no other statutory exclusion/relief. -> Deemed dividend of the amount still unrepaid before lodgment day at end of the loan year, capped by distributable surplus.

**Test 4:** MYR $19,716; shareholder pays $10,000 cash and sets off a $9,716 declared dividend (assessable). -> MYR satisfied; set-off preserved by s 109R(3).

**Test 5:** $20,000 repaid 25 June 2027, $25,000 redrawn 15 July 2027. Assume the reasonable-person intent finding in Example 6 and no preserved-payment exception. -> Repayment disregarded (s 109R); dates alone do not prove it.

**Test 6:** Passive UPE $150,000 to bucket company. -> No Div 7A loan (Bendel). Convert it to a complying loan by agreement -> it IS a loan from conversion; stays a loan.

**Test 7:** Holiday house, market rent $800/week, 2 weeks' private use, nothing paid; permission/right established and no dwelling or otherwise-deductible exception. -> s 109CA payment $1,600 (not minor; no licence fee).

**Test 8:** Provisional dividends $80,000; distributable surplus $30,000. -> Dividends reduced proportionally to $30,000 total; written statements required.

**Test 9:** Loan to a sister Pty Ltd (not trustee). -> Excluded (s 109K). Same loan to a company acting as trustee -> NOT excluded.

**Test 10:** Shareholder dies; executor asks whether the loan is forgiven. -> Estate liability and forgiveness outcome held under Rule 7. Check this point with one of our partner accountants.

### Recomputed checks

The following reproduce the original inputs. Dollar rounding is for illustration, not a new statutory rounding rule.

```oa-check
name: Original Examples 2-3 and Tests 1-4, 2026-27 MYR
inputs:
  principal: 100000
  rate: 0.0877
  term: 7
  cash: 10000
  setoff: 9716
  surplus: 4000
steps:
  q: 1 / (1 + rate)
  q2: q * q
  q4: q2 * q2
  denominator: 1 - q4 * q2 * q
  myr: principal * rate / denominator
  shortfall: max(0, myr - cash)
  capped_dividend: min(shortfall, surplus)
  combined_payment: cash + setoff
  remaining_term_test_2: term - 1
expected:
  denominator: 0.444817075488
  myr: 19715.9697396672
  shortfall: 9715.9697396672
  capped_dividend: 4000
  combined_payment: 19716
  remaining_term_test_2: 6
```

```oa-check
name: Original asset-use and distributable-surplus cases
inputs:
  weeks: 2
  weekly_rent: 800
  consideration: 0
  provisional: 80000
  surplus: 30000
steps:
  asset_payment: weeks * weekly_rent - consideration
  reduction_factor: surplus / provisional
  total_dividends: provisional * reduction_factor
expected:
  asset_payment: 1600
  reduction_factor: 0.375
  total_dividends: 30000
```

### Prohibitions

- NEVER use a benchmark rate from the wrong year (2026-27 = 8.77%)
- NEVER use a current-year closing balance for MYR; reconcile the prior-year amalgamated principal and first-year pre-lodgment adjustment
- NEVER treat a passive UPE as a Div 7A loan post-Bendel -- and NEVER clear a UPE structure without the s 100A / Subdiv EA screen
- Apply the reasonable-person test and all relevant s 109R exceptions before disregarding or counting a payment; the preserved-payment list includes specific refinancing cases
- NEVER assert a deemed dividend above distributable surplus
- NEVER treat a company-to-company loan as caught (s 109K) unless the recipient acts as trustee
- NEVER advise forgiveness, refinancing, or restructures -- compute exposure, escalate strategy
- NEVER present figures as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.
