---
name: md-cross-border
description: "Moldova cross-border income tax for 2026: when a nonresident has a Moldovan permanent establishment (fixed place, construction over 6 months, services over 3 months, warehouses, dependent agents, and the preparatory exclusions), which nonresident income is Moldova-source under Fiscal Code art. 71 (including management and consulting fees paid by a resident wherever performed), withholding at source under art. 91 (12% general rate, 6% on dividends, 15% on dividends from 2008 to 2011 profits), payment and reporting by the 25th of the following month, treaty relief and the residence proof the payer must hold before payment, refunds when proof arrives late, and the foreign tax credit for residents. Use when a Moldovan company pays a foreign supplier, lender, licensor or shareholder, or a foreign company works in Moldova. Two worked examples recompute in CI. Checked against the law (Fiscal Code 1163/1997, text in force 30 October 2026). Treaty rates are out of scope."
version: 0.1
jurisdiction: MD
category: cross-border
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova cross-border tax v0.1

Tax year: 2026. Article references are to the Fiscal Code No. 1163/1997, consolidated text in force 30 October 2026.

## Who this applies to

- **Moldovan payers** (the persons listed in art. 90) who pay Moldova-source income to nonresidents: they withhold and pay the tax (art. 91, 92).
- **Nonresidents** earning Moldova-source income listed in art. 71, with or without a permanent establishment in Moldova (art. 73).
- **Moldovan residents** with foreign income that is also taxed in Moldova: foreign tax credit (art. 82).

### Permanent establishment

A permanent establishment (PE) is a fixed place of business through which a nonresident carries on business in Moldova, wholly or partly, directly or through a dependent agent (art. 5 pt 15). It includes:

- a place of management, branch, office, factory, plant, workshop, mine, oil or gas well, quarry or other place of extraction of natural resources or of growing crops (a);
- a building site, construction, assembly or installation project, or related technical supervision, servicing and operation of equipment, **only if it lasts more than 6 months** (b);
- sale of goods from warehouses in Moldova owned or rented by the nonresident (c);
- supply of other services or other activities **for more than 3 months**, except preparatory activities, employment and independent professional activity, unless the Code provides otherwise (d);
- any of the above carried on by a dependent agent, or a dependent agent keeping a stock of goods from which it delivers on the nonresident's behalf (e).

A PE does not arise from preparatory or auxiliary activity alone (art. 5 pt 15¹). Examples are facilities used only to store or display the nonresident's goods; a stock kept only for storage, display or processing by another person; a place used only to buy goods; a place used only for information, marketing, advertising or market research that is not the nonresident's core business; signing contracts under detailed written instructions; and construction activity under (b) not exceeding 6 months.

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| General withholding on art. 71 income paid to a nonresident (except sale of goods) | 12% | 2026 | [Fiscal Code art. 91(1) first dash][code] |
| Dividends paid to a nonresident | 6% | 2026 | [art. 91(1) fourth dash][code] |
| Dividends from undistributed profit of fiscal periods 2008 to 2011 | 15% | 2026 | [art. 91(1) second dash][code] |
| Amounts under art. 90¹(3¹) third dash (withdrawal of capital from 2010 to 2011 capitalisation of profit) | 15% | 2026 | [art. 91(1) third dash; art. 90¹(3¹)][code] |
| PE: construction, assembly, installation, supervision | more than 6 months | 2026 | [art. 5 pt 15(b)][code] |
| PE: other services or activities | more than 3 months | 2026 | [art. 5 pt 15(d)][code] |
| Prior-year residence certificate still valid | first 60 days of the next fiscal period, unless residence conditions change | 2026 | [art. 79³(2)][code] |
| Withheld tax payment and monthly report | by the 25th of the month after the month of payment | 2026 | [art. 92(1)-(2)][code] |
| Annual withholding report | by the 25th of the month after the fiscal year ends | 2026 | [art. 92(3)][code] |

Where a treaty and the Code give different rates, the more favourable rate applies (art. 79³(1)). Treaty rates by country are out of scope here.

## The base

### Moldova-source income of nonresidents (art. 71(1))

Income counts as Moldova-source whether it is received in Moldova or abroad. The main categories are:

- (a) sale of goods;
- (b) **management or consulting services in any field**, if paid by a resident (or are expenses of a Moldovan PE), **regardless of where the services are performed**;
- (b¹) other services **performed in Moldova** not listed elsewhere in the article;
- (c), (d) capital gains on capital assets located, registered or issued in Moldova; for nonresident individuals without business in Moldova, gains on government securities and local authority bonds are excluded;
- (e) dividends paid by a resident;
- (f) interest paid by a resident or charged to a Moldovan PE; for nonresident individuals, interest on government securities and local authority bonds is excluded;
- (g) income from assignment of claims; (h) contractual fines and penalties;
- (j) royalties paid by a resident or charged to a Moldovan PE;
- (k) rent, leasing, usufruct or superficies of property in Moldova; (k¹) leasing or rental of ships, aircraft, rail or road vehicles, including in international traffic;
- (l) insurance and reinsurance premiums;
- (m) transport services, except transport only between points outside Moldova;
- (n), (o) salaries, directors' and managers' fees and benefits paid by a resident employer or PE, regardless of where duties are performed;
- (p) payments from resident voluntary pension funds;
- (q) artists and athletes for activity in Moldova; (r) professional, sports, entertainment and other services performed in Moldova;
- (s) prizes; (t) commissions; (t¹) gambling and promotional winnings; (u) liquidation proceeds above the contributed capital.

Income from regular international air transport is not Moldova-source for a nonresident without a Moldovan PE (art. 71(2)).

### How the nonresident is taxed

- **No PE.** Art. 71 income other than sale of goods is taxed at source under art. 91, with no deductions (art. 73(1), (3)). Tax is withheld whatever the form or place of payment (art. 73(5)). Withholding applies even where the nonresident passes the income to third parties or its own branches abroad (art. 73(2)). Income from opening and running banks' correspondent accounts and settlements is excluded (art. 73(1)).
- **Employment income of nonresident individuals** under art. 71(1)(n) and (o) is withheld under art. 88, not art. 91 (art. 73(4), 91(2)(b)).
- **Income of a Moldovan PE** is outside art. 91 withholding (art. 91(2)(a)). It is taxed through the PE's own computation and return, which this skill does not cover.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Residence certificate or proof from the nonresident | before the income is paid | [art. 79³(2)][code] |
| Pay withheld tax to the budget | 25th of the month after the month of payment | [art. 92(1)][code] |
| Monthly withholding report to the SFS | 25th of the month after the month of payment | [art. 92(2)][code] |
| Annual report listing each recipient, payment and tax withheld | 25th of the month after the fiscal year ends; within 15 days of approval of the liquidation balance sheet if the payer is liquidated or split | [art. 92(3)][code] |

## Penalties and interest

- Withheld tax paid late carries daily late-payment interest under art. 228. The daily rate is the National Bank of Moldova base rate set in November of the previous year, rounded up to the next whole percent, plus 5 points, divided by the days in the year (art. 228(2)-(3)).
- If a treaty was applied incorrectly and tax was not paid, or only partly paid, the resident payer is liable under the Code (art. 79³(8)).
- Late or wrong reports are fined under art. 260(1). The fine is MDL 200 to 400 per report, capped at MDL 2,000, for the taxpayers in art. 232(b). It is MDL 500 to 1,000 per report, capped at MDL 10,000, for those in art. 232(a) and (c).

## Cross-border points

### Treaty relief

- A treaty that sets different rules prevails over the Code (art. 4(1), 79³(1)). It does not apply where a treaty resident is used to obtain benefits for a person not entitled to them (art. 4(2)). Treaties are interpreted using the OECD Model Commentary (art. 79³(1)).
- **Proof before payment** (art. 79³(2)):
  - A nonresident **individual** gives the payer an original paper or electronic residence certificate from the competent authority of the state of residence.
  - A nonresident **legal person** gives one of: a copy of its residence certificate; a document showing its registration in its state of residence; or an extract from the official website of that state's authority showing tax residence or registration.
  - A document in a foreign language needs a translation into the state language, unless it is in English or Russian.
  - A certificate is valid for the year or years it was issued for. One issued for a fiscal period also covers the first 60 days of the next period, unless residence conditions change.
  - Without the proof, the payer applies Moldovan domestic law.
- **Proof that arrives late.** If proof is presented after payment within the same calendar year, the recipient may ask the payer, in free form, to refund the excess. The payer recalculates at the treaty rate and files a corrected report (art. 79³(2¹)). Otherwise the excess is refunded on request within the limitation period (art. 79³(3)). The request is filed by the payer or another person authorised by the nonresident, and is paid only if that person has no tax arrears. There is no refund for income earned through a PE (art. 79³(4)).
- The SFS issues the nonresident a certificate of tax paid in Moldova. A refund after such a certificate, or a certificate after a refund, is subject to art. 79³(6)-(7).
- How a Moldovan resident obtains residence confirmation for treaty purposes is set by the Ministry of Finance (art. 79³(9)).

### Foreign income of residents

A taxpayer may credit income tax paid in any foreign state on income also taxed in Moldova (art. 82):

- It needs a document confirming the foreign tax, certified by the foreign competent authority, and translated unless in English or Russian (art. 82(1)).
- The credit cannot exceed the Moldovan tax on that income at Moldovan rates (art. 82(2)).
- It is taken in the period in which the income is taxed in Moldova (art. 82(3)).

### Related parties

Payments to affiliated nonresidents are also controlled transactions; see [md-transfer-pricing](md-transfer-pricing.md).

## Two worked examples that recompute

### Example 1: Consulting fee to a foreign company, no residence proof

In March 2026 a Moldovan company pays a nonresident company MDL 480,000 for management consulting performed entirely abroad. The nonresident has no Moldovan PE and gave no residence proof before payment.

Under art. 71(1)(b), management and consulting fees paid by a resident are Moldova-source wherever the work is done. Without proof, domestic law applies (art. 79³(2)). Withholding at 12% under art. 91(1): 480,000 × 12% = MDL 57,600. The net payment is MDL 422,400. The tax is paid and reported by 25 April 2026 (art. 92(1)-(2)).

```oa-check
name: Moldova 12% withholding on a consulting fee to a nonresident (2026)
inputs:
  fee: 480000
  rate: 0.12
steps:
  - withholding: fee * rate
  - net_paid: fee - withholding
expected:
  withholding: 57600
  net_paid: 422400
```

If the fee were for IT support performed abroad, and not management or consulting, the payer would test art. 71(1)(b¹), which needs performance in Moldova, before withholding.

### Example 2: Dividend to a nonresident shareholder partly from 2008 to 2011 profits

In 2026 a Moldovan company pays its nonresident corporate shareholder a dividend of MDL 1,000,000. Of that, MDL 250,000 comes from undistributed profit of 2010 and MDL 750,000 from 2024 profit. The shareholder gave no residence proof before payment.

The 2008 to 2011 portion is taxed at 15%: 250,000 × 15% = MDL 37,500. The rest is taxed at 6%: 750,000 × 6% = MDL 45,000. Total withholding is MDL 82,500 and the net dividend is MDL 917,500. If the shareholder presents proof later in 2026 and a treaty gives a lower rate, it asks the payer for a refund of the excess under art. 79³(2¹).

```oa-check
name: Moldova dividend withholding split between 2008-2011 profits and later profits (2026)
inputs:
  dividend: 1000000
  old_profit_part: 250000
  old_rate: 0.15
  current_rate: 0.06
steps:
  - tax_old: old_profit_part * old_rate
  - tax_current: (dividend - old_profit_part) * current_rate
  - total_withholding: tax_old + tax_current
  - net_dividend: dividend - total_withholding
expected:
  tax_old: 37500
  tax_current: 45000
  total_withholding: 82500
  net_dividend: 917500
```

## Ask the client first

1. **What exactly is the payment for: goods, management or consulting, other services, interest, royalties, rent, dividends, or salary?** The art. 71 category decides whether there is withholding and whether the place of performance matters.
2. **Where and for how long does the nonresident work in Moldova, and does it have an office, warehouse, site or dependent agent there?** The 3-month and 6-month PE tests and the PE exclusions decide between withholding and a PE return.
3. **Which state is the recipient resident in, and what proof will it give before payment?** Without valid proof before payment, the domestic rate applies.
4. **For dividends: from which years' profits is the distribution paid?** Profits of 2008 to 2011 carry 15%, not 6%.
5. **Is the recipient affiliated with the payer?** If so, transfer-pricing rules also apply.
6. **For a resident with foreign income: what foreign tax was paid, and is there certified proof?** The credit needs it and is capped at the Moldovan tax.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code No. 1163/1997, consolidated text in force 30 October 2026 (last amended by Law 235 of 2 October 2026): arts. 4, 5 pts 15 and 15¹, 71, 73, 79³, 82, 90¹(3¹), 91, 92, 228, 260(1) | https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro | 2026-10-30 |

[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro

Not yet confirmed: the list of double tax treaties in force and their rates and protocols (the Ministry of Finance list carries a 20 June 2022 status date and was not re-read); Moldova's position under the multilateral instrument; the withholding report forms; the art. 90 list of persons who must withhold; individual residence tests and tie-breakers; how a PE computes and files its taxable profit; State Tax Service practice on the art. 71(1)(b) and (b¹) service split (its pages returned a human check and were not read).
