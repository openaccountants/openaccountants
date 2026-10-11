---
name: au-div7a
description: >
  Use this skill whenever asked about Division 7A of the ITAA 1936 -- private company loans, payments or debt forgiveness to shareholders or their associates, complying loan agreements, minimum yearly repayments, the benchmark interest rate, distributable surplus, unpaid present entitlements (UPEs) to corporate beneficiaries after Bendel, use of company assets by shareholders, or deemed dividends. Trigger on phrases like "Div 7A", "Division 7A", "shareholder loan", "director loan account", "debit loan", "minimum yearly repayment", "benchmark interest rate", "complying loan", "deemed dividend", "distributable surplus", "UPE", "bucket company", "unpaid present entitlement", or when a GL shows debit balances in shareholder/director accounts. ALWAYS read this skill before touching any Div 7A work.
version: 1.1
jurisdiction: AU
tax_year: 2026
last_updated: 2026-10-12
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Division 7A -- Private Company Loans Skill v1.1

## Australia Division 7A -- Private Company Loans Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** The High Court decided *Commissioner of Taxation v Bendel* [2026] HCA 18 on 10 June 2026: a UPE owed to a corporate beneficiary is not, of itself, a Div 7A loan. The ATO's decision impact statement (26 June 2026) accepts the decision. Several ATO products are under review or awaiting withdrawal -- Rule 11 carries the status table as at 1 August 2026. Verify before relying.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Australia |
| Primary Legislation | ITAA 1936 Part III Division 7A (ss 109B-109ZE) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027) |
| Benchmark interest rate (2026-27) | 8.77% (2025-26: 8.37%; 2024-25: 8.77%) |
| Complying loan maximum terms | 7 years unsecured; 25 years where 100% secured by registered real-property mortgage with market value (net of prior-ranking liabilities) >= 110% of the loan when first made |
| Complying agreement deadline | In writing BEFORE the company's lodgment day (earlier of due date and actual lodgment -- s 109D(6)) |
| First minimum yearly repayment | Due in the income year AFTER the year the loan is made |
| Deemed dividend cap | Distributable surplus (s 109Y); proportional reduction across provisional dividends |
| UPE to corporate beneficiary | NOT a Div 7A loan while the company stays passive (*Bendel* [2026] HCA 18) -- s 100A and Subdiv EA risks survive |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown lodgment day | Assume the EARLIER plausible date -- the deadline for agreements and repayments |
| Unknown loan agreement status | Assume NO written agreement; flag urgently (fixable only before lodgment day) |
| Debit balance in shareholder/director account | Treat as a Div 7A loan candidate until characterised |
| Unknown distributable surplus | Compute exposure at full value; flag the s 109Y cap as unquantified |
| UPE on trust balance sheet | Passive UPE = no Div 7A loan (post-Bendel), but flag s 100A / Subdiv EA screen (T2-1, T2-2) |
| Company asset used privately | Assume s 109CA payment at arm's-length value; check minor (<$300) and licence-fee carve-outs |
| Repayment near year end followed by redraw | Assume s 109R disregard applies; flag |

## Section 3 -- GL sweep library

**GL sweep library**

| GL pattern | Likely issue | Action |
| --- | --- | --- |
| Debit balance -- shareholder / director loan account | s 109D loan candidate | Loan register (Section 7); agreement status; MYR check |
| Drawings account not cleared to salary/dividend | Payments (s 109C) or loan | Characterise before lodgment day -- fixable until then |
| "Loan -- related trust" (asset side) | Actual loan back from company to trust | Div 7A loan -- Bendel does NOT help actual loans |
| UPE / beneficiary entitlement owed TO the company (in the trust's books) | Post-Bendel: not a loan while passive | s 100A / Subdiv EA screen; do not convert without advice |
| Motor vehicles, boats, property with private use by shareholders | s 109CA asset-use payment | Arm's-length value less consideration; minor/licence carve-outs |
| Journal writing off a related-party receivable | s 109F forgiveness | Deemed dividend at year end, subject to surplus |
| Interest income at exactly the benchmark rate | Existing complying loan | Verify MYR actually paid, not just interest accrued |

## Section 3 -- GL sweep library

Div 7A work starts with the balance sheet, not the loan register the client says exists.

## Section 4 -- Worked examples

### Example 1 -- New loan, saved by a complying agreement

Company advances $100,000 to a shareholder in March 2027 (2026-27 year). Return due date assumed 15 May 2028 (tax-agent lodgment program) and lodged that day, so lodgment day = 15 May 2028 -- an earlier due date or earlier actual lodgment would move the deadline, so establish both dates first. A written 7-year complying agreement at >= benchmark interest is signed 1 April 2028 -- before lodgment day.

No deemed dividend in 2026-27 (s 109N). The first minimum yearly repayment falls due in 2027-28, computed with the 2027-28 benchmark rate.

### Example 2 -- Minimum yearly repayment arithmetic

Amalgamated 7-year loan made in 2025-26; $100,000 unrepaid at 30 June 2026. MYR for 2026-27 (benchmark 8.77%):

```
Remaining term T = 7 - (years between end of loan year [30 Jun 2026]
                        and end of prior year [30 Jun 2026]) = 7
MYR = P x I / (1 - (1/(1+I))^T)
    = $100,000 x 0.0877 / (1 - (1/1.0877)^7)
    = $8,770 / 0.444817
    = $19,716 (nearest dollar)
```

### Example 3 -- Shortfall, capped by distributable surplus

Same loan; the shareholder repays only $10,000 in 2026-27. Shortfall = $9,716 -> deemed dividend at 30 June 2027, but only up to the company's distributable surplus (s 109Y). If surplus is $4,000, the dividend is $4,000 (and the company must give written statements where multiple provisional dividends are reduced proportionally).

### Example 4 -- UPE to a bucket company, post-Bendel

Trust resolves a $150,000 distribution to its corporate beneficiary in June 2027; the entitlement remains unpaid, and the company does nothing to call for payment.

**Not a Div 7A loan** (*Bendel* [2026] HCA 18; ATO DIS 26 June 2026 -- passive UPEs are not financial accommodation, sub-trust or not). Surviving risks to flag: s 100A reimbursement-agreement analysis (R-AU-D7A-1), Subdiv EA where the trust pays/lends to the company's shareholders, and any ACTIVE step (converting the UPE to a loan, satisfaction by promissory note) that creates a real s 109D(3) loan. Any call or demand for payment ends the passive characterisation this example relies on -- whether unenforced forbearance after a demand amounts to financial accommodation is unresolved, so escalate the moment the company does anything other than nothing. UPEs already converted to complying loans before Bendel stay loans.

### Example 5 -- Private use of a company asset

Company-owned holiday house used by the shareholder's family for 2 weeks; market rent $800/week; nothing paid.

s 109CA payment = arm's-length value less consideration = $1,600 -> deemed dividend at year end (subject to surplus). Carve-outs checked: not minor (>= $300 notional value), no licence fee paid (a market-rate licence fee would zero it), none of the dwelling exceptions apply. Continuing availability re-tests at the start of each income year.

### Example 6 -- The repay-and-redraw trap

Shareholder repays $20,000 on 25 June 2027, redraws $25,000 on 15 July 2027. A reasonable person concludes the repayment was intended to be re-borrowed: s 109R disregards the $20,000 for MYR purposes. Exception that DOES work: setting off a declared dividend or salary (assessable to the shareholder) against the loan -- s 109R(3) preserves set-offs of assessable amounts.

## Section 5 -- Tier 1 rules

### Rule 1 -- The three trigger events

- **The three trigger events** — Payments (s 109C, including s 109CA asset use), loans (s 109D), and debt forgiveness (s 109F) by a private company to a shareholder or associate (current or former, on the reasonable-person test) are deemed unfranked dividends at the end of the company's income year -- each capped by distributable surplus (Rule 8). Franking exceptions: the s 109RB discretion can allow franking, and s 109RC family-breakdown dividends (marriage/relationship breakdown obligations) are frankable without any discretion.  _(s 109C, s 109CA, s 109D, s 109F; s 109RB; s 109RC)_
- **Associate** — **Associate** (s 318 ITAA 1936, summarised): relatives of the shareholder; partners and their spouses and children; trustees of trusts under which the shareholder or an associate benefits; and companies the shareholder or associates control. Directors are caught only as shareholders or associates of shareholders -- confirm status when a debit director account is not held by a shareholder.  _(s 318 ITAA 1936)_

### Rule 2 -- Loans and the lodgment-day escape

- **Loans and the lodgment-day escape** — A loan is a deemed dividend unless, before the LODGMENT DAY (earlier of the return's due date and actual lodgment -- s 109D(6)): it is fully repaid, or a complying s 109N agreement is in place. Loan is defined widely: advances, provision of credit or any other form of financial accommodation (s 109D(3)).  _(s 109D(6); s 109N; s 109D(3))_

### Rule 3 -- Complying loan criteria (s 109N)

- **Complying loan criteria** — All three, before lodgment day: written agreement; interest for each year after the loan year at or above that year's benchmark rate; term within the maximum -- 7 years unsecured, or 25 years where 100% of the loan is secured by a registered mortgage over real property whose market value (net of prior-ranking secured liabilities) is at least 110% of the loan when first made.  _(s 109N)_

### Rule 4 -- Benchmark interest rate

- **Benchmark interest rate 2026-27** — 8.77% (2025-26: 8.37%; 2024-25: 8.77%) % (RBA Indicator Lending Rates -- bank variable housing loans rate last published before the start of the income year; always match the rate to the year being computed)  _(s 109N(2))_

### Rule 5 -- Amalgamated loans and minimum yearly repayments (s 109E)

- **Minimum yearly repayment (MYR)** — Constituent loans to one entity in a year, unrepaid at lodgment day, saved by s 109N, sharing a maximum term, amalgamate. From the income year AFTER the loan year, each year's MYR is: ``` MYR = P x I / (1 - (1/(1+I))^T) P = amount unrepaid at the end of the previous income year I = CURRENT year's benchmark rate T = remaining term = longest constituent term - years elapsed between the end of the loan year and the end of the prior income year; the resulting DIFFERENCE is rounded UP to the next whole number if not already whole (s 109E(7) rounds the remaining term itself, never the elapsed years) ``` Shortfall between amounts paid and the MYR = deemed dividend at year end (subject to surplus).  _(s 109E; s 109E(7))_

### Rule 6 -- Payments and asset use (ss 109C, 109CA)

- **Payments and asset use** — Payment = amounts paid/credited/transferred to, on behalf of, or for the benefit of the entity; property transfers valued at arm's length less consideration. A loan is not a payment. Use of a company asset (including under lease/licence) is a payment: first use, then re-tested at the start of each later income year; value = arm's-length amount for the use less consideration given. Carve-outs: minor use (< $300 notional value, s 58P criteria), otherwise-deductible use, certain dwellings, and NIL where an arm's-length licence fee is paid.  _(ss 109C, 109CA; s 58P)_

### Rule 7 -- Debt forgiveness (ss 109F, 109G)

- **Debt forgiveness** — Forgiveness (including debt parking and reasonable-person "won't insist" conclusions) = deemed dividend of the amount forgiven. Death does NOT automatically forgive a shareholder's loan -- no statutory death exception exists; ATO ID 2012/77 deems a dividend to the legal personal representative where forgiveness occurs during estate administration; escalate estate cases. Exclusions: debts owed by other companies (non-trustee), bankruptcy, loans already deemed dividends (full s 109D exclusion; dollar-for-dollar s 109E reduction), Commissioner's undue-hardship discretion.  _(ss 109F, 109G; ATO ID 2012/77)_

### Rule 8 -- Distributable surplus (s 109Y)

- **Distributable surplus** — ``` Distributable surplus = Net assets + Division 7A amounts - Non-commercial loans - Paid-up share value - Repayments of non-commercial loans ``` Net assets per the accounting records (less present legal obligations and specified provisions; Commissioner may substitute values for significant under/overvaluation). "Division 7A amounts" = current-year s 109C and s 109F dividends only. Where total provisional dividends exceed the surplus, each is reduced proportionally and the company must give recipients written statements.  _(s 109Y)_

### Rule 9 -- Anti-avoidance on repayments (s 109R)

- **Anti-avoidance on repayments** — Repayments are disregarded where a reasonable person concludes the entity intended to re-borrow a similar or larger amount, or borrowed from the company to fund the repayment. PRESERVED: set-offs of dividends, salary/wages or other assessable withholding-covered amounts, and arm's-length property-transfer balances (s 109R(3)-(4)).  _(s 109R; s 109R(3)-(4))_

### Rule 10 -- Exclusions and the discretion

- **Exclusions and the discretion** — s 109K: payments/loans to other companies (not as trustee) excluded. s 109L: amounts otherwise assessable or made non-assessable elsewhere. s 109M: loans in the ordinary course of business on usual arm's-length terms. s 109RB: the Commissioner may disregard a deemed dividend (or allow franking) for honest mistakes/inadvertent omissions -- factors include corrective action and speed, prior history; escalate applications (R-AU-D7A-3).  _(ss 109K, 109L, 109M, 109RB)_

### Rule 11 -- UPEs after Bendel: guidance status (as at 1 August 2026)

**UPEs after Bendel: guidance status (as at 1 August 2026)**

| Item | Status |
| --- | --- |
| *Bendel* [2026] HCA 18 (10 June 2026, 5:2) | Passive UPE to corporate beneficiary is not a s 109D loan |
| ATO decision impact statement | Issued 26 June 2026; accepts the decision; comments closed 24 July 2026 |
| TD 2022/11 | Announced-to-withdraw (DIS para 43); still technically in force with under-review banner |
| TR 2010/3 | Withdrawn since 1 July 2022 (pre-Bendel); historical only |
| TR 2022/4 + PCG 2022/2 (s 100A) | IN FORCE, under review -- s 100A remains the live ATO angle on UPEs |
| PCG 2017/13, TR 2015/4, TD 2015/20, TD 2011/15 | Under review, none withdrawn |
| Withdrawn-ruling protection | s 358-20(3) Sch 1 TAA: favourable withdrawn rulings keep applying to pre-withdrawal arrangements |
| Legislative response | 2018-19 Budget UPE measure still unenacted (prospective from Royal Assent); 2026-27 Budget: 30% minimum tax on discretionary trusts from 1 July 2028 with corporate beneficiaries denied the offset -- consultation closed 31 July 2026, not yet law |

### Rule 11 -- UPEs after Bendel: guidance status (as at 1 August 2026)

Practical position for 2026-27: a passive UPE creates no Div 7A consequence; actual loans company-to-trust remain Div 7A loans; converted UPEs stay loans; s 100A and Subdiv EA screens always run.

## Section 6 -- Tier 2 catalogue

### T2-1 -- s 100A screen

- **s 100A screen** — **Trigger:** UPE + benefits flowing to someone other than the presently entitled beneficiary, or distribution patterns outside ordinary family/commercial dealing. **Action:** refuse analysis (R-AU-D7A-1); document the pattern; escalate.  _(s 100A)_

### T2-2 -- Subdivision EA/EB

- **Subdivision EA/EB** — **Trigger:** the trust owing the UPE makes payments or loans to the company's shareholders/associates. **Action:** map flows; escalate (R-AU-D7A-2).  _(Subdivision EA/EB)_

### T2-3 -- 25-year loan security adequacy

- **25-year loan security adequacy** — **Trigger:** secured loan claimed; valuation or registration unverified. **Issue:** 110% net-of-prior-ranking test applies AT the time the loan is first made. **Action:** sight the registered mortgage and contemporaneous valuation; flag gaps.

### T2-4 -- Distributable surplus valuation

- **Distributable surplus valuation** — **Trigger:** net assets in the accounts look under/overstated (e.g. assets at historical cost, unrecorded liabilities). **Issue:** Commissioner's substitution power. **Action:** flag; do not self-adjust values.

### T2-5 -- Trust minimum tax horizon (announced, not law)

- **Trust minimum tax horizon (announced, not law)** — **Trigger:** structuring decisions for bucket companies extending past 1 July 2028. **Issue:** 2026-27 Budget announced 30% minimum tax on discretionary trusts (corporate beneficiaries denied the offset) from 1 July 2028, with restructure rollover relief from 1 July 2027 -- consultation only, not enacted. **Action:** note on any advice touching 2028+; escalate planning.  _(2026-27 Budget)_

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
  Amount unrepaid at end of PRIOR year (P): AUD [____]
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
2. Lodgment day is the master date -- agreements, repayments and characterisation are all fixable only before it. Establish it before anything else.
3. MYR uses the CURRENT year's benchmark against the PRIOR year-end balance -- the two most common errors are wrong-year rates and computing from the current balance.
4. Interest accrued is not repayment: the MYR must actually be paid (or validly set off).
5. UPEs: check the trust's books, not just the company's -- the company's balance sheet may not show the entitlement.

## Section 9 -- Onboarding fallback

If the client provides only financial statements:

1. Sweep both company and any trust balance sheets per Section 3
2. Build the loan register with agreement status UNKNOWN flagged per loan
3. Compute MYRs on stated balances at 8.77%, all assumptions listed
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

### Primary sources (verified 1 August 2026)

**Primary sources**

| Topic | Source |
| --- | --- |
| Benchmark rates | ato.gov.au -- Division 7A benchmark interest rate (QC 17928, updated 1 July 2026) |
| Statute | ITAA 1936 Compilation No. 192 (C2026C00333, 1 July 2026): ss 109C-109Y |
| MYR formula and steps | s 109E(6); ato.gov.au Division 7A loans (QC 17341, updated 2 July 2026) |
| Bendel | [2026] HCA 18 (10 June 2026); ATO decision impact statement 26 June 2026 |
| s 100A | TR 2022/4; PCG 2022/2 (both in force, under review) |
| Budget trust measures | 2026-27 Budget (12 May 2026); Treasury consultation paper 8 July 2026 |

### Test suite

**Test 1:** $100,000 unrepaid at prior year end, 7-year loan made last year, 2026-27 MYR. -> T = 7; MYR = $8,770 / 0.444817 = $19,716.

**Test 2:** Loan made 2024-25 (7-year), MYR for 2026-27. -> T = 7 - 1 = 6.

**Test 3:** No written agreement by lodgment day, loan unrepaid. -> Deemed dividend of the loan amount at end of the loan year, capped by distributable surplus.

**Test 4:** MYR $19,716; shareholder pays $10,000 cash and sets off a $9,716 declared dividend (assessable). -> MYR satisfied; set-off preserved by s 109R(3).

**Test 5:** $20,000 repaid 25 June, $25,000 redrawn 15 July. -> Repayment disregarded (s 109R); MYR shortfall computed as if unpaid.

**Test 6:** Passive UPE $150,000 to bucket company. -> No Div 7A loan (Bendel). Convert it to a complying loan by agreement -> it IS a loan from conversion; stays a loan.

**Test 7:** Holiday house, market rent $800/week, 2 weeks' private use, nothing paid. -> s 109CA payment $1,600 (not minor; no licence fee).

**Test 8:** Provisional dividends $80,000; distributable surplus $30,000. -> Dividends reduced proportionally to $30,000 total; written statements required.

**Test 9:** Loan to a sister Pty Ltd (not trustee). -> Excluded (s 109K). Same loan to a company acting as trustee -> NOT excluded.

**Test 10:** Shareholder dies; executor asks whether the loan is forgiven. -> No automatic forgiveness; estate cases escalate (Rule 7).

### Prohibitions

- NEVER use a benchmark rate from the wrong year (2026-27 = 8.77%)
- NEVER compute the MYR from the current-year balance -- P is the PRIOR year-end unpaid amount
- NEVER treat a passive UPE as a Div 7A loan post-Bendel -- and NEVER clear a UPE structure without the s 100A / Subdiv EA screen
- NEVER count a repayment that was re-borrowed (except valid s 109R(3) set-offs of assessable amounts)
- NEVER assert a deemed dividend above distributable surplus
- NEVER treat a company-to-company loan as caught (s 109K) unless the recipient acts as trustee
- NEVER advise forgiveness, refinancing, or restructures -- compute exposure, escalate strategy
- NEVER present figures as definitive

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

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
