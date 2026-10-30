---
name: lv-corporate-income-tax
description: "Latvian corporate income tax for tax year 2026 under the Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums) in force from 1 January 2026. Latvia taxes a company only when it distributes profit: 20% of the amount divided by 0.8. Covers who pays, the optional 15% rate with a 0.85 divisor for dividends of companies owned only by individuals (plus 6% personal income tax), deemed distributions (non-business expenses, bad debts, excess interest, loans to related persons, transfer pricing adjustments), dividends received, the 36-month share disposal relief, pre-2018 profits and losses, the monthly return by the 20th and payment by the 23rd, the EUR 50 minimum, fines and 0.05% a day late interest. Trigger on: Latvia corporate tax, SIA dividend tax, 20/80, UIN deklarācija, uzņēmumu ienākuma nodoklis. Out of scope: payments to non-residents (lv-cross-border), transfer pricing documentation (lv-transfer-pricing), individuals (latvia-income-tax), micro-enterprise tax and planning (latvia-tax-optimization)."
version: 0.2
jurisdiction: LV
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia: corporate income tax (2026)

Latvia does not tax annual profit. A company pays corporate income tax (CIT) only for the month in which it distributes profit or makes a payment the law treats as a distribution. Retained profit carries no tax. The tax is 20% of the taxable amount after that amount is divided by 0.8, so a net dividend of 80 costs 20 of tax (CIT Law art. 3(1), art. 4(9)). From 1 January 2026 a company whose owners are only individuals can choose 15% with a 0.85 divisor on dividends; the individual then pays 6% personal income tax on the dividend.

## Who this applies to

- **Domestic companies** (iekšzemes uzņēmumi) and permanent establishments of foreign companies pay CIT on the base in art. 4 (CIT Law art. 2(1)(1) and (2)). From the reporting year starting in 2026, port authorities are also taxpayers (art. 2(1)(1)(d), transitional provision 53).
- **Non-residents** earning Latvian income are taxpayers for withholding purposes (art. 2(1)(3), art. 5). That side is in `lv-cross-border`.
- **Out:** individuals; sole traders who have not chosen to prepare annual accounts; budget-funded bodies whose business income is in the budget; private pension funds; investment funds and alternative investment funds (their investors pay); non-profit associations and foundations; religious organisations, trade unions and political parties (art. 2(2)).
- **Micro-enterprise taxpayers** (SIA, sole trader or farm registered for micro-enterprise tax) pay CIT inside micro-enterprise tax under the Micro-enterprise Tax Law, not under this skill (art. 2(4), art. 4(11)). Registering for that regime triggers a deemed dividend (art. 7(1)(3)).
- **Tonnage tax** companies have a separate base for qualifying shipping (art. 4(16) to 4(21)). Not covered here.
- **Credit institutions and consumer lenders** also pay an annual CIT top-up of 20% on the previous year's after-tax profit, less the CIT paid on dividends calculated in the top-up year (extraordinary dividends excluded) (art. 4.1(4)). Not covered in detail here.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General CIT rate | 20% of the taxable base | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 3(1)) |
| Divisor applied before the rate | taxable amount / 0.8 (25% of a net distribution) | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 4(9)) |
| Alternative rate on calculated dividends, companies owned only by individuals (optional) | 15% | from 1 Jan 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 3(5), art. 4.2(1)) |
| Divisor under the alternative rate | dividend / 0.85 | from 1 Jan 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 4.2(2)) |
| Personal income tax on dividends paid under art. 4.2 | 6% | from 1 Jan 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (art. 15(5.1), art. 9(3.9)) |
| Personal income tax on ordinary dividends from CIT-taxed profit | exempt | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (art. 9(1)(2.1)) |
| Representation and staff wellbeing costs treated as non-business | excess over 5% of prior-year gross payroll | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 8(2)(7)) |
| Bad debt with a provision, not recovered | taxed after 36 months (60 months if the debtor is insolvent) | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 9(1)(1)) |
| Thin capitalisation | interest on average debt above 4 x opening equity | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 10(1)) |
| Interest limitation | net interest above EUR 3,000,000: excess over 30% of profit before CIT plus interest and depreciation | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 10(3)) |
| Share disposal relief | gain on direct shares held at least 36 months offsets dividends | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 13(1)) |
| Minimum CIT for the reporting year | EUR 50 | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 17(11)) |
| Annual CIT top-up for banks and consumer lenders | 20% | 2026 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums (art. 4.1(4)(5)) |
| Late payment interest | 0.05% of unpaid tax per day | 2026 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam (art. 29(2)) |
| Fine unit for administrative fines | EUR 5 | 2026 | https://likumi.lv/ta/id/303007-administrativas-atbildibas-likums (art. 16(2)) |

## The taxable base

The base for a taxation period is the sum of the items in art. 4(2), divided by 0.8 (art. 4(1), 4(9)). Amounts follow the revenue and expense recognition rules of the Annual Accounts Law or IFRS (art. 4(4)).

**1. Distributed profit (art. 4(2)(1))**
- (a) calculated dividends, including extraordinary dividends;
- (b) payments treated as dividends;
- (c) deemed dividends under art. 7: a reduction of share capital (first out of capital that came from profit), completion of liquidation, or registration as a micro-enterprise taxpayer (art. 7(1), 7(3)).

The dividend is taxed in the period in which it is calculated (declared), not when it is paid.

**2. Deemed distributed profit (art. 4(2)(2))**
- (a) **Non-business expenses** (art. 8): costs not directly linked to the business, judged by economic substance. Examples in art. 8(2): benefits to shareholders or staff not taxed as their income; gifts and forgiven loans; donations outside the art. 12 relief; assets used for non-business purposes; representation and staff wellbeing costs above 5% of the prior year's gross payroll; representative cars; bribes; disproportionate penalties, or penalties paid to related or low-tax persons; fuel above the art. 8(5) limits. Advances where the deal has not started within 12 months are also caught (art. 8(2¹)). Items (a) and (f) do not apply where personal income tax was withheld (art. 4(3)).
- (b) **Bad debts** (art. 9): a provision for a debt not recovered within 36 months (60 months if insolvency proceedings started), or a direct write-off, unless the art. 9(3) conditions are met. Those require all recovery steps, and for example the debtor being in the EU/EEA or a treaty country, a court judgment with a bailiff's statement, or a small debt (up to EUR 20, or up to 0.2% of turnover capped at EUR 500). A debt recovered in the year drops out (art. 4(6)).
- (c) **Increased interest payments** (art. 10): interest on the part of average debt above four times opening equity (less revaluation and other reserves not from profit). Where net interest exceeds EUR 3,000,000, interest above 30% of profit before CIT plus interest and depreciation. The higher of the two is added (art. 10(4)). Loans from regulated EU/EEA or treaty-country lenders are outside the first test (art. 10(2)).
- (d) **Loans to related persons** (art. 11): a loan to a related person is a deemed distribution. Not caught: loans from a shareholder to the company; loans to the company's own foreign PE; loans up to the amount the company itself borrowed from unrelated persons; loans made in a year that starts with no retained earnings; loans up to opening share capital less earlier unrepaid loans; loans for 12 months or less (art. 11(3), 11(4)). The base is reduced when the loan is repaid (art. 11(5)).
- (e) **Transfer pricing adjustments**: income the company would have received, or costs it would not have had, if related-party deals were at market value (art. 4(2)(2)(e)). Deals with persons in a listed low-tax or no-tax jurisdiction count as related-party deals (art. 4(10)). Documentation and methods: `lv-transfer-pricing`.
- (f) Benefits a non-resident gives its staff or board that relate to its Latvian PE.
- (g) Liquidation quota: equity above the shareholders' contributions (art. 4(8)).
- (h) to (k) Assets transferred in a reorganisation (art. 18); assets moved to a foreign PE, or out of a Latvian PE, where Latvia loses the right to tax (exit charge, see `lv-cross-border`); hybrid mismatch results (art. 7.1).

Items (b), (c), (d), (e), (f), (i), (j) and (k) go into the base of the **last taxation period of the reporting year** (art. 4(5)). Non-business expenses (a) are taxed in the period they arise, except advances on deals not started within 12 months, which go into the last month of the reporting year (art. 8(2¹)(1)).

**3. Reliefs that reduce the base**
- **Dividends received** (art. 6): a company can reduce its calculated dividends by dividends it received in the same period from a payer that is a CIT payer in its home state, or on which tax was withheld at source. Not for dividends from a low-tax or no-tax jurisdiction, from a company that was a micro-enterprise taxpayer when it earned the profit, where the payer deducted the dividend, or where the main purpose is to use the exemption (art. 6(1), 6(3) to 6(5)). Unused received dividends carry forward in date order (art. 6(2)).
- **Share disposals** (art. 13): a gain on directly held shares held at least 36 months reduces calculated dividends, with carry-forward of any excess. Not for shares in low-tax jurisdiction companies, unlisted companies whose assets are more than 50% Latvian real estate, or fund units (art. 13(3), 13(4)).
- **Donations** to qualifying recipients (art. 12): not covered in detail here.

**3a. Controlled foreign companies (art. 6.1)**
- A company adds to its base the profit of a foreign company (or of its own foreign PE) that comes from non-genuine arrangements, where it holds, alone or with related persons, more than 50% of the shares or votes, or is entitled to more than 50% of the profit (art. 6.1(1) to 6.1(3)). An arrangement is non-genuine to the extent the foreign company would not take the risks or hold the assets if it were not controlled by a company that carries out the key management functions for them (art. 6.1(7)).
- The share of profit goes into the return for the last taxation period of the reporting year in which the foreign company's year ends (art. 6.1(5)).
- Not applied where the foreign company's annual profit is up to EUR 750,000, or its income other than from sales of goods and services is up to EUR 75,000, unless it is in a listed low-tax or no-tax jurisdiction or the tax authority found the arrangements in an audit (art. 6.1(8), 6.1(9)).
- Later dividends out of that already-taxed profit reduce the company's own dividend base (art. 6.1(10)).

**4. The 15% alternative for companies owned only by individuals (art. 4.2)**
- Condition: in the tax period (a calendar month, or a quarter for a company entitled to book quarterly, art. 3(2), 3(3)) in which the dividend is calculated, every shareholder (dalībnieks) is an individual (art. 4.2(1)). "Dalībnieks" means any owner of shares or anyone else with a non-debt right to share in profit (art. 1(7)), so the option is open to an AS as well as an SIA, as long as no shareholder is a company, fund or other entity.
- Scope: only calculated dividends under art. 4(2)(1)(a). Deemed dividends, payments treated as dividends and all deemed distributions stay at 20% / 0.8.
- It is a choice: the company "is entitled to choose" it for the dividends calculated in that tax period, so the test and the choice are made period by period (art. 4.2(1)).
- Computation: dividend / 0.85 x 15% (art. 3(5), art. 4.2(2)). The shareholder then pays 6% personal income tax on the dividend instead of the usual exemption (PIT Law art. 9(3.9), art. 15(5.1)).
- Who withholds the 6%: the company, when it calculates the dividend (CIT Law art. 16(5)). For personal income tax the dividend counts as paid on the day it is calculated (PIT Law art. 16.1(8)). The company pays the 6% into the single tax account by the 23rd of the following month (PIT Law art. 17(10)(12)) and reports the payment to VID by the 15th of the following month (PIT Law art. 17(11)(1)). For listed shares, the investment service provider that keeps the account withholds, on the payment date (PIT Law art. 16.1(8)).
- Start: inserted by the law of 3 December 2025, in force 1 January 2026.
- It is not a saving on the same profit. Take EUR 12,000 of profit paid out. Standard rule: the dividend divided by 0.8 is 12,000, so the dividend is 9,600, CIT is 2,400 and there is no personal income tax; the owner keeps 9,600 (art. 3(1), art. 4(9)). Option: the dividend divided by 0.85 is 12,000, so the dividend is 10,200, CIT is 1,800 and the company withholds 6%, which is 612 (art. 3(5), art. 4.2(2), art. 16(5)); the owner keeps 9,588. On the same profit the standard rule leaves the owner 12 more per 12,000.

**5. Losses and pre-2018 profit**
- There is no loss carry-forward under this system: losses do not reduce a distribution.
- Pre-2018 losses: a company with losses in its CIT return at 31 December 2017 could cut CIT on dividends by 15% of those losses, capped at 50% of the CIT on dividends each year, in the reporting year starting in 2018 and the next four reporting years (transitional provisions 13 and 14). That window has closed; nothing is left to use in 2026.
- Pre-2018 profit: dividends out of retained profit shown in the balance sheet at 31 December 2017 are outside the base. That profit is first reduced by later losses and by dividends already paid out of it, first in, first out (transitional provisions 8 to 10).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Taxation period | calendar month; a quarter for companies entitled under Accounting Law art. 13 to book documents quarterly | CIT Law art. 3(2), 3(3) |
| CIT return (UIN deklarācija) to the State Revenue Service (VID) | by the 20th of the month after the taxation period | art. 17(1) |
| Nil periods | no return needed for a period with no taxable item, except the last month of the reporting year | art. 17(3) |
| Return not filed by the 20th | the period is treated as nil; a later return counts as a correction (not for the last month of the year) | art. 17(4) |
| Payment | into the single tax account by the 23rd of the month after the taxation period | art. 17(7) |
| Year-end correction | no late interest on extra tax from correcting the last month's return for changes found while preparing annual accounts filed on time | art. 17(8) |
| Minimum tax | if CIT for the reporting year is under EUR 50, top up to EUR 50 in the last month's return; not for a company registered or liquidated in the year, one that paid at least EUR 100 of personal income tax or social contributions for an employee, or one in insolvency | art. 17(11), 17(12) |
| 6% personal income tax on art. 4.2 dividends | company withholds on the day the dividend is calculated; pays by the 23rd and reports to VID by the 15th of the following month | CIT Law art. 16(5); PIT Law arts. 16.1(8), 17(10)(12), 17(11)(1) |
| Due date on a holiday | moves to the next working day | Law on Taxes and Fees art. 29(3¹) |

## Penalties and interest

- **Late payment interest:** 0.05% of the unpaid tax for each day late (Law on Taxes and Fees art. 29(2)). For the single tax account it is charged on the 1st and 15th of each month, and not charged if the tax arrives by the last day of the month in which it was due (art. 29(2¹), 29(2²)(1)).
- **Under-declared tax found in an audit:** the tax, late interest to the start of the audit, and a fine of 20% of the under-declared tax if the shortfall is up to 15% of the tax due, or 30% if it is more (art. 32(1), 32(4), 32(5)). The fine is halved for a first offence where returns and payments were on time and the taxpayer cooperated (art. 32(7)). Amounts set in an audit are due within 30 days (art. 32(8)).
- **Voluntary correction:** a corrected return before any audit costs the tax and late interest only (art. 33.2(1)). After notice of an audit but before it starts, a 5% fine is added (art. 33.2(2)).
- **Late filing fines** (art. 141), in fine units of EUR 5 (Administrative Liability Law art. 16(2)):

| Days late | Fine |
|---|---|
| 3 to 10 | warning or 5 to 14 units (EUR 25 to 70); not applied to a single monthly or quarterly return up to 5 days late in 12 months |
| 11 to 20 | 15 to 30 units (EUR 75 to 150) |
| 21 to 30 | 31 to 56 units (EUR 155 to 280) |
| over 30, or not filed | 57 to 140 units (EUR 285 to 700) |

- Accounting breaches that reduce the base carry the same liability (CIT Law art. 19(1)).

## Cross-border points

- Withholding on payments to non-residents (management and consulting fees, real estate, payments to low-tax jurisdictions), permanent establishments, treaty relief and the exit charge on assets leaving Latvia: see `lv-cross-border`.
- Arm's length adjustments are taxed here as a deemed distribution at 20% / 0.8 in the last month of the reporting year. Who is related, documentation thresholds and penalties: see `lv-transfer-pricing`.
- Dividends from EU/EEA and treaty-country subsidiaries can reduce a Latvian company's own dividend base under art. 6, unless the payer is in a listed low-tax or no-tax jurisdiction.
- Any deal with a person in a listed low-tax or no-tax jurisdiction is treated as a related-party deal for deemed distributions (art. 4(10)).

## Worked examples

**Example 1. Holding SIA, standard 20%, December 2026.** A Latvian SIA owned by a German GmbH calculates a dividend of EUR 60,000 in December 2026. In the same month it received a EUR 25,000 dividend from its Latvian subsidiary, which paid CIT on that profit. Its representation costs for 2026 are EUR 9,000. Its gross payroll for 2025 was EUR 120,000, so the 5% cap is EUR 6,000 and EUR 3,000 is a non-business expense. The shareholder is a company, so the 15% option is not open. The received dividend reduces the calculated dividend to EUR 35,000 (art. 6(1)). The base is (35,000 + 3,000) / 0.8 = EUR 47,500 and the CIT is EUR 9,500. The December return is due by 20 January 2027 and the tax by 23 January 2027.

```oa-check
name: Holding SIA, dividend less dividend received, representation excess, December 2026
inputs:
  dividend_calculated: 60000
  dividend_received: 25000
  representation_costs: 9000
  prior_year_gross_payroll: 120000
steps:
  - taxable_dividend: max(dividend_calculated - dividend_received, 0)
  - representation_cap: prior_year_gross_payroll * 0.05
  - non_business: max(representation_costs - representation_cap, 0)
  - base: (taxable_dividend + non_business) / 0.8
  - cit: base * 0.20
expected:
  taxable_dividend: 35000
  representation_cap: 6000
  non_business: 3000
  base: 47500
  cit: 9500
```

**Example 2. SIA owned by two individuals, 15% option plus a loan to a sister company, 2026.** In March 2026 the SIA calculates a dividend of EUR 50,000 for its two individual shareholders and chooses the art. 4.2 rate. CIT is 50,000 / 0.85 x 15% = EUR 8,823.53, due by 23 April 2026. The SIA withholds 6% personal income tax from the dividend, EUR 3,000, reports it to VID by 15 April 2026 and pays it by 23 April 2026. Total tax is EUR 11,823.53 and the owners keep EUR 47,000. The profit used is 50,000 + 8,823.53 = EUR 58,823.53. Paid out under the standard rule, the same profit gives a dividend of 58,823.53 x 0.8 = EUR 47,058.82 with no personal income tax (art. 3(1), art. 4(9)), so on the same profit the option leaves the owners EUR 58.82 less. Comparing the same EUR 50,000 dividend (EUR 12,500 of CIT under the standard rule) is not like with like, because the owners would then keep EUR 50,000 rather than EUR 47,000. In June 2026 the SIA also lends EUR 10,000 for 24 months to a sister company owned by the same individuals. The SIA had retained earnings at 1 January 2026, opening share capital of EUR 3,000, no earlier unrepaid loans and no borrowings from unrelated lenders. The first EUR 3,000 is covered by share capital (art. 11(4)(3)); EUR 7,000 is a deemed distribution. It goes into the December 2026 return at the standard rate, because the 15% option covers only calculated dividends: 7,000 / 0.8 x 20% = EUR 1,750.

```oa-check
name: Individual-owned SIA, art. 4.2 dividend plus related-party loan, 2026
inputs:
  dividend: 50000
  loan_to_related: 10000
  share_capital: 3000
  earlier_unrepaid_loans: 0
steps:
  - cit_alternative: round(dividend / 0.85 * 0.15, 2)
  - pit_on_dividend: dividend * 0.06
  - total_alternative: cit_alternative + pit_on_dividend
  - net_alternative: dividend - pit_on_dividend
  - profit_used: dividend + cit_alternative
  - net_standard: round(profit_used * 0.8, 2)
  - standard_route_extra: net_standard - net_alternative
  - loan_exempt: min(loan_to_related, max(share_capital - earlier_unrepaid_loans, 0))
  - loan_taxable: loan_to_related - loan_exempt
  - cit_on_loan: loan_taxable / 0.8 * 0.20
  - total_company_cit: cit_alternative + cit_on_loan
expected:
  cit_alternative: 8823.53
  pit_on_dividend: 3000
  total_alternative: 11823.53
  net_alternative: 47000
  profit_used: 58823.53
  net_standard: 47058.82
  standard_route_extra: 58.82
  loan_taxable: 7000
  cit_on_loan: 1750
  total_company_cit: 10573.53
```

## Ask the client first

1. Who owns the company in the tax period (month, or quarter) in which the dividend is calculated: only individuals, or any company, trust or fund? This decides whether the 15% option is open.
2. Is the company registered for micro-enterprise tax or tonnage tax, or is it a bank or consumer lender? Each changes the regime.
3. Does it receive dividends or sell shareholdings, and from which countries? The art. 6 and art. 13 reliefs depend on it.
4. Are there loans to shareholders, sister companies or other related persons, and for how long? Plus opening share capital and retained earnings.
5. Does the company deal with related persons abroad, or with anyone in a listed low-tax jurisdiction? Deemed distributions and transfer pricing follow.
6. Does any retained profit date from before 1 January 2018? Dividends from it are outside the base.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums), version in force from 1 January 2026: arts. 1(7), 2, 3, 4, 4.1, 4.2, 6, 6.1, 7, 8, 9, 10, 11, 13, 16(5), 17, 19; transitional provisions 8 to 10, 13, 14, 53 | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-10-24 (likumi.lv refused the connection; read from the Internet Archive copy of 4 October 2026, https://web.archive.org/web/20261004132502/https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Law on Taxes and Fees (likums "Par nodokļiem un nodevām"): arts. 29, 32, 33.2, 141 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 (Internet Archive copy of 18 September 2026) |
| Law On Personal Income Tax (likums "Par iedzīvotāju ienākuma nodokli"): arts. 9(1)(2.1), 9(3.9), 15(5.1), 16.1(8), 17(10)(12), 17(11)(1) | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-24 (Internet Archive copy of 1 September 2026) |
| Administrative Liability Law (Administratīvās atbildības likums): art. 16 | https://likumi.lv/ta/id/303007-administrativas-atbildibas-likums | 2026-10-24 (Internet Archive copy of 10 August 2026, https://web.archive.org/web/20260810162753/https://likumi.lv/ta/id/303007-administrativas-atbildibas-likums) |
| State Revenue Service (VID) | https://www.vid.gov.lv | 2026-10-24 (refused the connection; not read) |

Not yet confirmed: the CIT return form and its annexes (the return regulation was not read); the art. 8(5) fuel limits and the art. 12 donation relief; any CIT Law amendment after the 4 October 2026 archive copy.

> Contributed by Michael Cutajar.

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
