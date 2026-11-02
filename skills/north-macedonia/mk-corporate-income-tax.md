---
name: mk-corporate-income-tax
description: "Use this skill for North Macedonia corporate profit tax for calendar year 2026. It covers resident companies, local permanent establishments of foreign companies, the ordinary profit-tax reconciliation and eligible small-company turnover taxation. Trigger on Macedonian corporate tax, profit tax, DB return, DB-VP, reinvested profit, tax losses, related-party interest, depreciation, corporate instalments or nonresident withholding. It sets out accounting-to-tax adjustments, deductible costs, loss approval, investment relief, advance payments and annual balances, with two recomputing examples. Use the transfer-pricing and cross-border skills for detailed related-party documentation and treaty procedures. This tier 2 skill, checked against the law, supports working papers and has no licensed accountant’s sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
category: international
---

# North Macedonia corporate income tax v0.3

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

[Profit Tax Law arts. 4-6][cit] tax resident legal persons on domestic and foreign profits and nonresident permanent establishments on local business profits. A resident is established or seated in North Macedonia. The tax period is the calendar year, or the actual shorter operating period (art. 38). Classify the entity before computing tax: eligible micro/small companies can enter the arts. 31-36 turnover regime; qualifying nonprofits use the distinct art. 4-a economic-activity regime.

This is ordinary company tax. Minimum global top-up tax, regulated financial-sector computations and industrial-zone state aid need their separate legislation. Do not treat a threshold or exemption in this skill as an exemption from another tax.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official provision |
|---|---|---|---|
| Ordinary profit tax | 10% | 2026 | [Profit Tax Law art. 2][cit] |
| Eligible small/micro company's exempt annual revenue band | Total revenue not above 3,000,000 | 2026 | [Arts. 31-32][cit] |
| Eligible turnover-tax election band and rate | 3,000,001-6,000,000 total revenue; 1% on total revenue | 2026 | [Arts. 33-34][cit] |
| Election consistency | 3 years including election year while within the election band | 2026 | [Art. 33(2)][cit] |
| Qualifying nonprofit economic revenue | 1% on amount above 1,000,000 | 2026 | [Art. 4-a(3)-(4)][cit] |
| Entertainment disallowance | 90% | 2026 | [Art. 9(1)(8)][cit] |
| Qualifying public-interest donations / sponsorship deduction caps | 5% / 3% of total annual revenue | 2026 | [Art. 9(1)(9)-(10)][cit] |
| Loss carryforward | Maximum 3 years counted from loss year; oldest first, UJP approval | 2026 | [Art. 19][cit] |
| Nonresident shareholder thin capitalisation | At least 20% holding; loans exceeding 3 times shareholder's capital share; first 3 operating years excluded | 2026 | [Art. 15][cit] |
| Reinvested-profit asset retention | 5 years; actual qualifying reinvestment of prior-year profit reduces base | 2026 | [Art. 28][cit] |
| Foreign legal-person WHT | 10% of listed gross income, treaty relief conditional | 2026 | [Arts. 20-23][cit] |
| Late-payment interest | 0.03% daily | 2026 | [Tax Procedure Law art. 123][procedure] |
| Late-filing surcharge | Up to 10% of the tax assessed by law | 2026 | [Tax Procedure Law art. 55][procedure] |

## The base

**Ordinary calculation:** accounting revenue minus accounting expenses, plus disallowed expenses and understated income, less specific statutory reductions, approved losses and eligible reinvestment. Apply 10%, then admissible credits and advances (arts. 7-19, 28, 37-41). Do not tax all distributions as a substitute for current profit tax.

1. Reconcile accounting profit to supported business expenditure. Add back private/nonbusiness spending, disguised distributions, 90% entertainment, donations/sponsorship above the applicable caps, disallowed employee benefits, tax/fine/late-public-debt charges, WHT borne for others, and other items in art. 9. Apply that article's individual employee-reimbursement limits, not PIT exemptions by analogy. Ordinary wages and business expenditure remain in accounting expenses except for statutory disallowances.
2. Depreciation: art. 9-a and the [Decree arts. 2-7][depreciation] permit cost-based straight-line depreciation for eligible assets over EUR 500 equivalent with useful life over one year, starting when available for use. The nomenclature rate can increase by up to 50% under decree art. 4. Remove depreciation on revaluation excess and amounts above tax limits; art. 17-a permits the specific subsequent reversal of previously disallowed depreciation. Do not depreciate an already fully depreciated asset again. UJP consent for full unusable-asset write-off is requested by 31 January following the year (art. 9-a(5)).
3. Receivables: impairment is generally added back, subject to the bank/insurer and registered, administrator-confirmed insolvency/liquidation claims exceptions in art. 10. Loans advanced and not repaid within that same year are added back under art. 11 except loans to resident legal persons. Previously taxed recoveries/loan repayments reduce the base only within the documented previously taxed amount (art. 17). Permanent write-offs have the separate art. 9(1)(17) restriction.
4. Apply related-party pricing under arts. 12-12-b, interest under art. 13, related-party default interest under art. 14 and thin capitalisation under art. 15. For related-party loans, [Profit Rulebook art. 4][profit-rules] supplies the independent corporate fallback where the origination-date comparable rate cannot be substantiated: matching-maturity **EURIBOR for foreign-currency loans or SKIBOR for denar loans plus one percentage point**, as the borrowing-interest ceiling and lending-interest minimum respectively. Retain the benchmark and origination/interest-period evidence. The TP skill explains the 300 million revenue and domestic-transaction exclusions from arts. 12/12-a. Those exclusions do not cancel arts. 9(1)(7), 13-15. For thin capitalisation, test qualifying debt at period start and end and determine average shareholder equity from paid capital, reserves excluding revaluation, retained profits and uncovered losses. Disallow interest attributable to the excess portion, including covered guarantees/deposit-backed borrowing; apply the new-company and financial-shareholder exclusions exactly.
5. Deduct resident-company dividend income only where already taxed at the distributing taxpayer (art. 18). Maintain evidence; this is a base reduction for qualifying resident dividends, not a universal participation exemption for foreign dividends.
6. Carry an accounting loss reduced by disallowed expenses under art. 19, within the statutory three-year window counted from its year, oldest first. Apply using UJP approval; request **DD-01 by 31 March next year**. UJP has **60 days** to decide. Status changes described in art. 19(3) prevent use. Do not create a carryback or roll expired losses forward.
7. Reinvestment relief under art. 28 uses actual investment from prior-year profit in business-expansion real estate, plant, equipment, software and patents, including qualifying finance leases. Ordinary passenger cars, furniture, audiovisual/household equipment, art and administrative assets are excluded. Keep the profit allocation, invoices, commissioning and asset-retention evidence. Disposal within five years or termination of finance lease recaptures the relief; unsupported use and failure to determine/pay recapture trigger the specific **fivefold tax** rule in art. 28(5)-(6). File/pay **DD-DO within 30 days** of disqualifying disposal/termination (art. 39(2)).

**Turnover regime:** first verify arts. 31-33 eligibility. Banking, finance, insurance and gambling/amusement activities are excluded. Total revenue from all sources, not profit or taxable VAT turnover, controls. Eligible companies not above 3 million have no annual turnover tax; those in the election band elect 1% on the whole revenue, not only excess over 3 million. Revenue over 6 million or abusive related-party arrangements cause removal under art. 36; recompute ordinary profit tax and credit turnover tax already paid. UJP records eligible companies from annual-account data (art. 35). Filing still applies to exempt companies.

**Historical retained profits:** [art. 48][cit] separately charges profit tax when accumulated profits earned in **2009-2013** are distributed after the current law took effect. Use **DD-ID** for that distribution charge; keep it separate from the current year's accounting-profit tax and the recipient's dividend PIT/withholding. Identify the earnings vintage before treating a payment as an ordinary already-taxed-profit distribution.

## Deadlines and filing

Obtain and maintain the company/PE's tax registration. A PE registers at commencement of activity (art. 6(7)). Use UJP electronic tax services. [Arts. 35, 39][cit] tie **DB** or **DB-VP** to the annual-account deadline. [UJP's filing instructions][cit-filing] confirm **end of February**, or **15 March where the annual account is submitted electronically**. These dates fall in **2027 for 2026 accounts**, with the applicable nonworking-day rule; the cited 2026 announcement concerns 2025 accounts, not an extension for 2026 accounts. P/TC accompanies DB where TP documentation applies (art. 39(5)). Nonprofit economic income uses DB-NP/VP.

Annual balance/turnover tax is paid within **30 days after the annual-account/return deadline** (arts. 39(3)-(4), 41). Ordinary monthly advances are the prior annual tax divided by twelve, adjusted by the cumulative retail-price growth specified in art. 40, payable within **15 days after each month**. [Implementing rulebook art. 13][profit-rules] addresses a prior short period and no prior assessed tax; use actual operating months for the short-period basis. Turnover-regime/nonprofit taxpayers in art. 40(4) do not pay ordinary monthly profit-tax advances. Overpayment refund: request UJP, statutory decision within **60 days** (art. 41).

On conversion/reorganisation or liquidation, use arts. 25-27 for continuity and closing accounts. A status change requires accounts and return for the year to the registered change date; liquidation includes the period through completion before distribution of the residue. Deregistration does not remove final tax obligations.

## Penalties and interest

[Art. 43][cit] inaccurate data reducing the base: legal-person fines micro **EUR 600-2,000**, small **1,200-4,000**, medium **3,600-12,000**, large **6,000-20,000**, in MKD equivalent. [Arts. 44-46][cit] cover late payments/advances, withholding and absent/late returns or TP records, with micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, and separate responsible-person fines. Classify the actual offence; do not aggregate ranges as automatic charges. A late return can also carry a separate late-filing surcharge of up to **10%** of the tax ([Tax Procedure Law art. 55][procedure]). UJP can assess for **5 years** from the end of the year of the taxable event, **10 years** for tax evasion (art. 110). Late debt bears [Tax Procedure Law art. 123][procedure] interest from the next day at 0.03% per day. The fivefold reinvestment recapture is distinct from these fines.

## Cross-border points

Foreign profit tax credited under art. 37 is limited to North Macedonia tax at 10% on the foreign profit; obtain proof from the foreign tax authority. Listed nonresident legal-person income is withheld at payment under arts. 20-23. WHT is generally final for that receipt; income of a PE uses its proper attribution. Taxed PE profit remittance is expressly excluded from WHT by art. 21(2), as are specified government/bank-deposit interest items. Treaty relief needs approved/certified documentation before payment. Submit **DD-I by 15 February next year** (art. 24); see the cross-border skill. Artificial arrangements lose domestic/treaty benefits under art. 42-a.

## Two worked examples that recompute

**Simple: ordinary profit reconciliation.** Accounting profit is 2,000,000, including 100,000 entertainment and 20,000 fines. Add back 90,000 and 20,000 (art. 9). Tax on 2,110,000 is 211,000. With 180,000 advances, balance is 31,000.

```oa-check
name: MK 2026 corporate reconciliation
inputs:
  profit: 2000000
  entertainment: 100000
  fines: 20000
  advances: 180000
steps:
  - base: profit + entertainment * 0.90 + fines
  - tax: base * 0.10
  - balance: tax - advances
expected:
  base: 2110000
  tax: 211000
  balance: 31000
```

**Edge: an eligible turnover election.** A qualifying small company has 5,000,000 total revenue, has validly elected the regime and satisfies the election consistency rule. Art. 34 taxes the whole 5,000,000 at 1%: 50,000. Previously paid profit-tax advances of 30,000 leave 20,000 payable; no deduction of expenses or 3 million band from the turnover base.

```oa-check
name: MK 2026 turnover election whole revenue
inputs:
  revenue: 5000000
  advances: 30000
steps:
  - tax: revenue * 0.01
  - balance: tax - advances
expected:
  tax: 50000
  balance: 20000
```

## Ask the client first

- What is the legal residence, operating period, activity and PE status?
- What is total revenue, entity size and existing turnover election history?
- Which expenses, receivables, depreciation and related-party balances need adjustments?
- Which approved losses remain within their window, and were status changes made?
- Which prior profits funded investments or distributions, including 2009-2013 earnings requiring DD-ID, and were investment assets retained?
- Which advances, foreign taxes and nonresident payments have evidence?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Profit Tax Law, consolidated through Gazette 199/2023 | https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Depreciation Decree, Gazette 277/2019 | https://www.ujp.gov.mk/files/attachment/0000/0157/Uredba_za_amortizacija__277-_219.pdf | 2026-10-24 |
| Profit Tax implementing rulebook, consolidated through Gazette 6/2020 | https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf | 2026-10-24 |
| UJP, 25 February 2026 DB/DB-VP filing instructions (2025 returns filed in 2026) | https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1204 | 2026-10-24 |

[cit]: https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf
[depreciation]: https://www.ujp.gov.mk/files/attachment/0000/0157/Uredba_za_amortizacija__277-_219.pdf
[profit-rules]: https://www.ujp.gov.mk/files/attachment/0000/0990/______________________________________________________________________________________________________________________________________________.pdf
[cit-filing]: https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1204

Not yet confirmed: None within the stated scope.

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
