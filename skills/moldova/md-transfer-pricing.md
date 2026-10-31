---
name: md-transfer-pricing
description: "Moldova transfer pricing for fiscal periods from 2025, applied in 2026: who is an affiliated person (25% voting participation, effective control, close family, a company and its permanent establishment), which local and cross-border transactions are controlled, the MDL 20 million aggregate threshold for the annual transfer-pricing information, the transfer-pricing file prepared only on request of the State Tax Service within 120 days, the five transfer-pricing methods, voluntary and corresponding adjustments, advance pricing agreements and their fees, and the Fiscal Code art. 260 fines. Use for Moldovan related-party pricing, intra-group loans, the 25 June filing for calendar-year companies, IT park residents' single-tax adjustment report, and planning an APA. Two worked examples recompute in CI. Checked against the law (Fiscal Code 1163/1997, consolidated text in force 30 October 2026, and Law 187/2025). Not an arm's-length benchmark for a specific transaction."
version: 0.1
jurisdiction: MD
category: transfer-pricing
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova transfer pricing v0.1

Tax year: fiscal periods from 2025 onward, as applied in 2026. Law 187/2025 rewrote Fiscal Code art. 226¹⁹ and applies it from fiscal period 2025 (Law 187/2025 art. XXVI(1)(b)). Article references are to the Fiscal Code No. 1163/1997 unless stated.

## Who this applies to

The arm's-length principle applies when a taxpayer determines taxable income from transactions with affiliated persons (art. 226¹⁸(1)). The chapter covers local and cross-border transactions between affiliated persons (art. 226¹⁸(2)).

**Affiliated persons** (art. 226¹⁷(1) pt 1):

- two individuals who are spouses or relatives up to the second degree inclusive;
- an individual and a legal person, where the individual holds, directly or indirectly (counting holdings of affiliated persons), at least 25% of the voting participations, or effectively controls it;
- two legal persons, where one holds at least 25% of the other's voting participations or effectively controls it, or a third person holds at least 25% in both or controls both;
- a legal person and its permanent establishment.

Effective control means the factual and legal power to decide on the company's activity, by appointing or dismissing the majority of the supervisory board, the executive body or the auditors, or by contract, articles or shareholder agreement. Indirect control is holding through one or more other persons (art. 226¹⁷(1) pt 1).

**Controlled transactions** (art. 226¹⁷(1) pts 6, 7, 9, 10):

- A transaction is any sale, purchase, supply or receipt of services, assignment, leasing, credit, loan, or other transfer of any interest or right to use tangible or intangible property.
- A **cross-border transaction** is between a resident and a nonresident outside Moldova.
- A **local transaction** is narrower than "any resident-to-resident deal". It is a transaction between residents where one or both are residents of a free economic zone or an IT park, or apply different income tax rates or a different taxable base. Two ordinary resident companies on the same regime are not in a local transaction under pt 9.

**Out of scope or deemed arm's length:**

- A price, or price elements, set by legal act or court decision is deemed arm's length (art. 226¹⁸(3)).
- Art. 226¹⁹ filing does not apply to Moldovan citizens who are individuals not carrying on business (art. 226¹⁹(9)).
- Transactions covered by an advance pricing agreement do not count toward the threshold or the documentation (art. 226¹⁹(4)).

The burden of proving arm's-length pricing is on the taxpayer (art. 226¹⁸(7)). Definitions are completed by, and the chapter is applied with regard to, the OECD Transfer Pricing Guidelines (art. 226¹⁷(2), 226¹⁸(8)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Affiliation participation test | at least 25% of voting participations, direct or indirect | 2026 | [Fiscal Code art. 226¹⁷(1) pt 1][code] |
| Annual TP information threshold | total value of transactions with all affiliated persons in the fiscal period, excluding VAT, of MDL 20,000,000 or more | periods from 2025 | [art. 226¹⁹(1)][code]; [Law 187/2025 art. II pt 19][l187] |
| TP file | prepared and submitted only on SFS request | periods from 2025 | [art. 226¹⁹(1), (3)][code] |
| TP information deadline | 25th day of the sixth month after the end of the fiscal period (25 June 2026 for calendar 2025) | periods from 2025 | [art. 226¹⁹(2)][code] |
| TP file deadline | 120 days from the request, but not before the TP information deadline | periods from 2025 | [art. 226¹⁹(3)][code] |
| Corrected TP file after an SFS adjustment decision | within 30 days of notification of the decision | 2026 | [art. 226¹⁹(6)][code] |
| SFS answer to a corresponding-adjustment request | 30 working days from receipt | 2026 | [art. 226²²(3)][code] |
| APA fee, unilateral | MDL 30,000 per type of transaction | 2026 | [art. 226²⁸(1)(a)][code] |
| APA fee, bilateral or multilateral | MDL 50,000 per type of transaction | 2026 | [art. 226²⁸(1)(b)][code] |
| APA term | up to 5 fiscal periods including the application period; rollback to the last 2 finished periods | 2026 | [art. 226²⁶][code] |
| APA extension or revision request | at least 60 days before the APA expires | 2026 | [art. 226²⁵(8)][code] |

The threshold test is "equal to or more than" MDL 20 million: exactly MDL 20,000,000 meets it. The former MDL 50 million tier with automatic file submission, the 25th-of-the-third-month deadline and the 60-day file deadline belong to the pre-2025 text and do not apply to fiscal periods from 2025.

## The base

### Building the threshold amount

Add the value of all transactions with all affiliated persons in the fiscal period, excluding VAT (art. 226¹⁹(1)). Then apply art. 226¹⁹(7):

- Leave out advances received or paid, exchange differences and revaluation differences on assets and liabilities arising from transactions with affiliated persons. Currency-exchange transactions themselves stay in.
- For leasing, credit and loans, count **only the interest** under art. 12 pt 7) calculated in the fiscal period, not the principal.
- Leave out transactions covered by an APA (art. 226¹⁹(4)).

### Pricing methods

The methods are (art. 226²⁰(3)):

1. comparable price (CUP);
2. cost plus;
3. resale price;
4. transactional net margin;
5. profit split;
6. any other method recognised in the OECD Guidelines.

The SFS uses the most appropriate method (art. 226²⁰(4)). It chooses that method by the content of the transaction and the functional analysis of functions, assets and risks, reliable information including independent transactions, the taxpayer's documents, the degree of comparability, and the individual circumstances (art. 226²⁰(5)). Where the SFS proves the taxpayer's method is not arm's length, it may apply another listed method (art. 226²⁰(7)).

Comparable information can come from the taxpayer's or the counterparty's own uncontrolled transactions, any source that describes comparable transactions or persons, and information the SFS receives under international agreements (art. 226²⁴).

### Adjustments

- **SFS adjustment or estimate.** Where the principle is not respected, the SFS may adjust income or expenses of either party. Where the taxpayer does not provide the data needed, the SFS may estimate them (art. 226²⁰(1)-(2)). The audit follows chapter 11 of Title V (art. 226²⁰(6)).
- **No VAT effect.** A TP adjustment does not change the VAT on supplies and purchases (art. 226¹⁸(6)).
- **Voluntary adjustment.** The taxpayer may adjust its own income or expenses. For prior periods it must file corrected TP information or a corrected TP file, and corrected returns under art. 188 (art. 226²³).
- **Resident-to-resident corresponding adjustment.** An SFS adjustment of one resident binds the affiliated resident. After the art. 252(3) term the SFS issues a decision to the other party, which may then file a corrected income tax return (art. 226²¹).
- **Resident-to-nonresident corresponding adjustment.** Relief runs through the double tax treaty with the nonresident's state. The resident files an adjustment request with proof of the foreign adjustment. The SFS decides within 30 working days to confirm, refuse with reasons, or order an audit (art. 226²²).
- **IT park residents.** Single tax arising from a TP adjustment is reported on a separate single-tax report for transactions with affiliated persons by the 25th of the sixth month after the fiscal period (art. 373(1¹), in force 1 January 2026 under Law 187/2025 art. XXVI(1)(d)).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| TP information (threshold met) | 25th of the sixth month after the fiscal period ends; 25 June 2026 for calendar-year 2025 | [art. 226¹⁹(2)][code] |
| TP file (on SFS request only) | 120 days from the request, not before the information deadline | [art. 226¹⁹(3)][code] |
| Corrected TP information | under art. 188 | [art. 226¹⁹(5)][code] |
| Corrected TP file | up to 30 days from notification of the SFS adjustment decision | [art. 226¹⁹(6)][code] |
| IT park single-tax TP report | 25th of the sixth month after the fiscal period | [art. 373(1¹)][code] |
| APA annual compliance report | by the income tax return deadline, for each period covered | [art. 226²⁹(1)][code] |

The form, content and filing method of the TP information and the TP file are set by the Ministry of Finance (art. 226¹⁹(8)).

**Transition for 2024 transactions.** By derogation, the 2024 TP file was due only on SFS request within 120 days of the request. Missing the earlier art. 226¹⁹(4¹) deadline is not an offence (Law 187/2025 art. XXVI(3)). The IT park single-tax report for 2024 transactions was due by 25 December 2025 (Law 187/2025 art. XXVI(4)).

## Penalties and interest

| Offence | Fine | Source |
|---|---|---|
| Late TP information | MDL 30,000 to 50,000 | [art. 260(7)][code] |
| False TP information that reduced or evaded tax | MDL 60,000 to 90,000 | [art. 260(8)][code] |
| TP information not submitted | MDL 100,000 to 150,000 | [art. 260(9)][code] |
| Late TP file | MDL 30,000 to 50,000 | [art. 260(10)][code] |
| TP file with false information that reduced or evaded tax | MDL 150,000 to 200,000 | [art. 260(11)][code] |
| TP file not submitted | MDL 300,000 to 500,000 | [art. 260(12)][code] |

Tax due after an adjustment carries late-payment interest for each day from the day after the due date to the day of payment (art. 228(2)). The daily rate is set each year from the National Bank of Moldova base rate for short-term monetary policy operations set in November of the previous year. That rate is rounded up to the next whole percent, increased by 5 points, divided by the number of days in the year, and rounded to 4 decimals (art. 228(3)). A taxpayer that finds an error and files a corrected return pays interest capped at the additional tax (art. 228(2¹)).

## Cross-border points

- A permanent establishment is an affiliated person of its legal person, so head office to PE dealings are controlled transactions (art. 226¹⁷(1) pt 1).
- Double taxation after an adjustment with a nonresident affiliate is removed only through the applicable double tax treaty (art. 226²²(1)).
- A bilateral or multilateral APA is possible only where a double tax treaty exists with the affiliate's state. If the foreign authority refuses, or does not answer within 6 months of the application, the SFS informs the taxpayer. The taxpayer then has 30 days to withdraw and recover the fee, switch to a unilateral APA, or narrow a multilateral request to a bilateral one (art. 226²⁵(1), (6)-(7)).
- An APA can be requested by a resident or by a registered PE or branch of a nonresident legal person. It cannot cover transactions already under an ongoing or completed TP audit (art. 226²⁵(2)-(3)).
- Withholding tax on payments to nonresidents is a separate obligation; see [md-cross-border](md-cross-border.md).

## Two worked examples that recompute

### Example 1: Does a distributor meet the MDL 20 million threshold?

A Moldovan company's 2025 transactions with affiliated persons, all excluding VAT: sales of goods to its foreign parent MDL 12,400,000; purchases from a sister company MDL 6,100,000; a MDL 40,000,000 loan from the parent with interest for 2025 of MDL 1,650,000; exchange differences on the loan MDL 310,000; an advance received of MDL 900,000.

Under art. 226¹⁹(7), count the interest only (not the principal) and leave out the exchange differences and the advance. Total = 12,400,000 + 6,100,000 + 1,650,000 = MDL 20,150,000. That is MDL 150,000 above the threshold. The company files TP information by 25 June 2026 and prepares a TP file only if the SFS asks for it.

```oa-check
name: Moldova TP threshold, distributor with intra-group loan (periods from 2025)
inputs:
  sales_to_parent: 12400000
  purchases_from_sister: 6100000
  loan_interest: 1650000
  threshold: 20000000
steps:
  - counted_total: sales_to_parent + purchases_from_sister + loan_interest
  - amount_over_threshold: counted_total - threshold
expected:
  counted_total: 20150000
  amount_over_threshold: 150000
```

Had the advance and exchange differences been wrongly included, the total would be MDL 21.36 million; had the interest also been left out, it would be MDL 18.5 million and below the threshold. The base must follow art. 226¹⁹(7).

### Example 2: Late information, no file on request, and interest on an adjustment

A company files its 2025 TP information late. It then does not provide the TP file within 120 days of an SFS request. The SFS adjusts income and the extra income tax is MDL 100,000, paid 90 days after it was due. For the arithmetic only, assume a November base rate that rounds up to 6% (the actual rate is not confirmed here).

Fine range: art. 260(7) MDL 30,000 to 50,000 plus art. 260(12) MDL 300,000 to 500,000, so MDL 330,000 to 550,000. Daily interest rate: (6 + 5) / 365 = 0.030137%, rounded to 0.0301%. Interest: 100,000 × 0.0301% × 90 = MDL 2,709.

```oa-check
name: Moldova TP fines and art. 228 interest on an adjustment (assumed 6% base rate)
inputs:
  late_info_min: 30000
  late_info_max: 50000
  no_file_min: 300000
  no_file_max: 500000
  base_rate_pct: 6
  extra_tax: 100000
  days_late: 90
steps:
  - fines_min: late_info_min + no_file_min
  - fines_max: late_info_max + no_file_max
  - daily_rate_pct: round((base_rate_pct + 5) / 365, 4)
  - interest: extra_tax * daily_rate_pct / 100 * days_late
expected:
  fines_min: 330000
  fines_max: 550000
  daily_rate_pct: 0.0301
  interest: 2709
```

## Ask the client first

1. **Who are the counterparties, and what is the ownership or control link?** The 25% voting test, effective control and family links decide whether a transaction is controlled at all.
2. **For resident counterparties: is either party in a free economic zone or an IT park, or on a different income tax rate or base?** If not, the deal is not a "local transaction" under art. 226¹⁷(1) pt 9.
3. **The 2025 and 2026 totals with all affiliated persons, excluding VAT, split into sales, purchases, services, loan interest, advances and exchange differences.** This decides the MDL 20 million test.
4. **What is the fiscal period?** The information deadline runs from the end of the period, so a non-calendar period moves the date.
5. **Has the SFS sent a TP file request, an audit notice or an adjustment decision, and on what date?** The 120-day and 30-day clocks run from those dates.
6. **Does any transaction fall under an existing or planned APA?** APA transactions leave the threshold, and the fee is charged per type of transaction.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code No. 1163/1997, consolidated text in force 30 October 2026 (last amended by Law 235 of 2 October 2026): arts. 226¹⁷ to 226³⁰, 228, 260(7) to (12), 373(1¹) | https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro | 2026-10-30 |
| Law No. 187 of 10 July 2025 amending certain normative acts (Monitorul Oficial 379-380, art. 491): art. II pts 19 and 28, art. XXVI(1)(b), (1)(d), (3) and (4) | https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro | 2026-10-30 |

[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro
[l187]: https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro

Not yet confirmed: the Ministry of Finance form, content and filing channel for the TP information and the TP file, including master-file and local-file contents under Order 9/2024 as amended by Orders 21/2025 and 8/2026 (the orders were not read); whether the false-information fines in art. 260(8) and (11) are deferred to periods from 2028 (the State Tax Service pages returned a human check and were not read); the National Bank of Moldova base rate for the 2026 interest calculation; how long the TP file must be kept (the former six-year rule in art. 226¹⁹(5) is not in the current text); the length of the art. 252(3) term before a resident corresponding adjustment.
