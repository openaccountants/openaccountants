---
name: ua-corporate-income-tax
description: "Ukrainian corporate income tax (податок на прибуток підприємств) for tax year 2026 under the Tax Code of Ukraine, section III and the martial-law transitional provisions. Covers who pays, the 18% base rate, 25% for financial institutions, 50% for banks in 2026, insurers' 3% and 0% rates, gambling and lottery rates, the accounting-profit base and the UAH 40 million small-taxpayer option, loss carry-forward with the 50% limit for large taxpayers, the advance payment on dividends, quarterly and annual returns, penalties and penalty interest, and 15% withholding on payments to non-residents. Trigger on: Ukraine corporate tax, CIT Ukraine, податок на прибуток, декларація з податку на прибуток, dividend advance payment Ukraine, bank tax 50%. Out of scope: sole proprietors and the simplified regime (ua-single-tax, ua-income-tax), VAT (ukraine-vat), payroll (ua-payroll), the country summary (ua-tax-overview)."
version: 0.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine: corporate income tax (2026)

Ukraine taxes a company on its profit for the year. The profit is the accounting result before tax from the financial statements, adjusted by the tax differences in section III of the Tax Code of Ukraine (TCU art. 134.1.1). The base rate is 18% (art. 136.1). Financial institutions other than insurers pay 25% (art. 136.1-1). Banks pay 50% for the 2026 tax periods (TCU section XX, subsection 4, point 73). All article numbers below are articles of the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010) unless another act is named.

## Who this applies to

- **Resident companies.** Legal entities doing business in Ukraine or abroad are resident taxpayers (art. 133.1.1). A company formed under foreign law is also a resident taxpayer if its place of effective management is in Ukraine (art. 133.1.5). Residents are taxed on profit from sources in Ukraine and abroad (art. 134.1.1).
- **Non-residents.** A non-resident is a taxpayer when it does business in Ukraine through a permanent establishment or receives Ukrainian-source income (art. 133.2). A permanent establishment is taxed on its profit like an independent company, at arm's length (art. 141.4.7). Other Ukrainian-source income of a non-resident is taxed by withholding at the payer (art. 141.4.2). See "Cross-border points".
- **Simplified-regime payers are out.** Businesses on the single tax (спрощена система, TCU section XIV chapter 1) do not pay corporate income tax (art. 133.5). They still withhold tax on Ukrainian-source payments to non-residents (art. 133.1.4, art. 137.5 "г" and "ґ"). The single tax is in `ua-single-tax`.
- **Non-profit organisations are out** if they meet art. 133.4 and are entered in the Register of non-profit institutions and organisations (art. 133.4, 133.4.5).
- **Diia City residents** may choose to pay tax "on special conditions": 9% on distributions and other listed payments instead of tax on annual profit (art. 136.8, 141.9-1). This skill names the regime only; its base rules are not covered here.
- **Defence City residents** may apply once to have their profit exempt from corporate income tax, from the first day of the next quarter, until 1 January 2036 or the year Ukraine joins the EU if earlier. Conditions: Defence City status, not a Diia City resident, no dividends paid except to the state or wholly state-owned companies, and no breach of the art. 39 and 39-2 reporting duties. The exempt profit must be invested in the listed development purposes (fixed assets, production facilities, technology, IP for state defence contracts) by 31 December of the following year, or tax is due on the unused part. These payers file quarterly (section XX, subsection 10, point 76.1). This skill names the regime only.
- **Military levy.** The military levy payers listed in TCU section XX, subsection 10, point 16-1 are individuals (art. 162.1) and single-tax payers. A company paying corporate income tax is not on that list, so the levy is not charged on company profit. The levy on salaries and dividends paid to individuals is in `ua-payroll` and `ua-income-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Base rate of corporate income tax (TCU art. 136.1) | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Financial institutions except insurers: profit, CFC profit, and the dividend advance (art. 136.1-1) | 25% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Banks: profit and dividend advance for the 2026 tax periods (section XX, subsection 4, point 73, added by Law No. 4698-IX of 3 Dec 2025) | 50% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Banks: 2024 tax year (point 70, Law No. 4015-IX) and 2023 tax year (point 68) | 50% | 2023, 2024 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Banks: 2025 tax year. Subsection 4 has no bank point for 2025, so the financial-institution rate applies (art. 136.1-1) | 25% | 2025 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Insurers: tax on insurance income, on top of the profit tax, general contracts (art. 136.2.1) | 3% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Insurers: long-term life, voluntary medical and private pension insurance contracts (art. 136.2.2) | 0% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Gambling: slot-machine halls, on income, on top of profit tax (art. 136.4.1) | 10% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Gambling: other gambling income less winnings paid (art. 136.4.2) | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Lotteries: tax on lottery income (art. 136.6) | 30% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Diia City residents taxed on special conditions (art. 136.8) | 9% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Small taxpayer: may skip most tax differences, and files annually, if prior-year income net of indirect taxes is not above (art. 134.1.1, art. 137.5 "в") | UAH 40,000,000 | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Large taxpayer: income over the last four quarters above, or taxes paid above (art. 14.1.24) | EUR 50,000,000 equivalent; EUR 1,500,000 equivalent | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Large taxpayer: share of the unrecovered loss usable in a period (art. 140.4.4) | 50% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Large taxpayer: loss used in full if not above this share of the period's profit (art. 140.4.4) | 10% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Thin capitalisation: debt on transactions with non-residents above equity by more than (art. 140.2) | 3.5 times | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Thin capitalisation: non-resident interest deductible up to (art. 140.2) | 30% of profit plus finance costs plus tax depreciation | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Add-back on purchases from listed low-tax states or listed untaxed foreign entity forms (art. 140.5.4) | 30% of the cost | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Donations to registered non-profits: add-back of the part above (art. 140.5.9) | 4% of prior-year taxable profit | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Donations, martial-law relief: no add-back up to this share of prior-year taxable profit, if more than 4% went to registered charities (section XX, subsection 4, point 72) | 8% | 2025 to end of the year martial law ends | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Controlled transactions: taxpayer income above, and transactions with one counterparty above (art. 39.2.1.7) | UAH 150,000,000; UAH 10,000,000 | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Fuel retailers: monthly advance per retail site (art. 141.14.2) | UAH 60,000; UAH 30,000 if only liquefied gas; UAH 45,000 if liquefied gas is 50% or more of litres | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Withholding on Ukrainian-source income of non-residents, general (art. 141.4.2) | 15% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Withholding on freight paid to non-residents (art. 141.4.4) | 6% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Insurance payments to non-residents (art. 141.4.5) | 0%, 4% or 12% by contract type | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Interest on Eurobond-funded loans meeting art. 141.4.11 | 5% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Profit of non-residents on discount bonds and treasury bills (art. 141.4.3) | 18% (the art. 136.1 rate) | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |

## The taxable base

**Start from the accounts.** The object of tax is profit from Ukrainian and foreign sources: the financial result before tax under national accounting standards or IFRS, increased or reduced by the tax differences in section III (art. 134.1.1). An increase reduces a loss or raises a profit; a reduction does the opposite.

**The UAH 40 million option.** If the company's annual income from all activities, net of indirect taxes, for the last annual reporting period is not above UAH 40 million, it may use the accounting result without the tax differences. It must still deduct prior-year losses and make the adjustments in art. 140.4.8, 140.5.16 and 140.6 (art. 134.1.1). If income later goes above UAH 40 million, the company applies all differences from that year (art. 134.1.1).

**Main differences.**
- **Depreciation.** Accounting depreciation and impairment are added back and tax depreciation is deducted, with minimum useful lives for fixed assets and intangibles (art. 138.1, 138.3.3, 138.3.4).
- **Thin capitalisation.** If debt on transactions with non-residents is more than 3.5 times equity, interest on that debt above 30% of the period's profit (before this difference and before losses) plus finance costs plus tax depreciation is added back. Debt and equity are averages of the start and end of the period (art. 140.2).
- **Payments to low-tax states.** 30% of the cost of goods, services and fixed assets bought from non-residents registered in states on the Cabinet of Ministers list, or from listed foreign entity forms that pay no corporate tax, is added back. Controlled transactions under art. 39 are excluded (art. 140.5.4).
- **Donations.** Gifts to organisations in the Register of non-profit institutions are added back to the extent they exceed 4% of the previous year's taxable profit (art. 140.5.9). For the periods from 2025 to the end of the calendar year in which martial law ends, the add-back is not made on gifts to organisations in that Register of up to 8% of the previous year's taxable profit, provided more than 4% of that profit went to charitable organisations in the Register. Gifts to an insurers' association whose membership is a licensing condition, and to organisations covered by art. 140.5.14, are outside this relief (section XX, subsection 4, point 72, added by Law No. 4254-IX of 25 Feb 2025).
- **Dividends received.** Dividends from other Ukrainian corporate income tax payers and single-tax payers are deducted (art. 140.4.1). Dividends from a non-resident are deducted if the holding is at least 10% for the whole calendar year and the payer is not in a state on the Cabinet of Ministers low-tax list (art. 140.4.3).
- **Controlled foreign companies.** Adjusted profit of a controlled foreign company is added to the controlling company's base and taxed at the base rate (art. 134.1.7, 136.7, 39-2). Foreign corporate tax paid by the CFC reduces the tax due (art. 137.9).
- **Transfer pricing.** Transactions with related non-residents and with listed low-tax states are controlled when the taxpayer's income is above UAH 150 million and transactions with that counterparty are above UAH 10 million in the year (art. 39.2.1.7). Prices must be at arm's length (art. 39).
- The full list of differences is in art. 138 to 140 and is not reproduced here.

**Losses.** A loss (negative object of tax) of earlier years reduces the financial result of later years (art. 140.4.4).
- A company that is not a large taxpayer deducts the whole unrecovered loss.
- A large taxpayer (income above EUR 50 million equivalent over the last four quarters, or taxes paid above EUR 1.5 million equivalent; art. 14.1.24) deducts no more than 50% of the unrecovered loss in a period. The rest carries forward on the same terms until used. If the unrecovered loss is not more than 10% of the period's positive object of tax before the loss, it is deducted in full (art. 140.4.4). This large-taxpayer limit first applied to the 2022 tax periods, and losses unrecovered at 1 January 2022 are used under it (section XX, subsection 4, point 4-2).
- Banks deduct no prior-year losses for the 2026 tax periods. The unused loss, including any 2026 loss, carries forward from 1 January 2027 (section XX, subsection 4, point 73). The same rule applied to banks for 2024 (point 70).

**Advance payment on dividends.** A company that decides to pay a dividend pays an advance corporate income tax payment to the budget before or at the time of the payment (art. 57.1-1.2).
- The base is the amount by which the dividend exceeds the object of tax for the year the dividend is paid from, if the tax for that year has been paid. If that tax is unpaid, the base is the whole dividend. The rate is the art. 136 base rate: 18%, or 25% for financial institutions (art. 136.1-1 "в"), or 50% for banks in 2026 (point 73).
- For a dividend for part of a year, the object of tax is taken pro rata to the months covered.
- The advance is credited against the corporate income tax of the period in which it is paid. Any excess carries forward. It is not refunded and cannot be set against other taxes (art. 57.1-1.2).
- No advance is due on dividends paid to individuals, on dividends a parent pays out of dividends it received, or on dividends up to the amount of tax-exempt profit (art. 57.1-1.3). Collective investment institutions and Diia City residents on special conditions are exempt from it (art. 57.1-1.6, 57.1-1.8).
- The advance is part of corporate income tax. It is not a tax on repatriation, so withholding under art. 141.4 still applies to a dividend paid to a non-resident (art. 57.1-1.5).

## Deadlines and filing

- **Tax periods.** The default periods are the calendar quarter, half-year, nine months and year. Returns are cumulative (art. 137.4).
- **Annual filers.** The tax period is the year for: companies registered during the year (for that first year); agricultural producers; companies whose income, net of indirect taxes, in the prior-year statement of financial results is not above UAH 40 million; and single-tax payers that withhold tax on payments to non-residents (art. 137.5). Agricultural producers may use a 1 July to 30 June year (art. 137.4.1).
- **Return deadlines.** Quarterly, half-year and nine-month returns are due within 40 calendar days after the end of the period (art. 49.18.2). The annual return is due within 60 calendar days after the end of the year (art. 49.18.3, 49.18.6). For the 2026 year that is 1 March 2027. If the last day is a weekend or holiday, the deadline moves to the next working day (art. 49.20).
- **Financial statements.** The quarterly or annual financial statements are filed with the return. Companies that must publish audited annual statements are excepted (art. 46.2).
- **Payment.** Tax declared in a return is paid within 10 calendar days after the last day for filing that return (art. 57.1). For the 2026 annual return, that is 11 March 2027.
- **Dividend advance.** Paid before or at the time the dividend is paid (art. 57.1-1.2).
- **Withholding on payments to non-residents.** Paid to the budget at the time of the payment (art. 141.4.2).
- **Fuel retailers.** The monthly advance per retail site is paid by the 20th of the current month (art. 141.14.1).
- **Record keeping.** Keep primary documents and accounting records for 1,825 days. Keep documents needed for transfer pricing (art. 39), CFC (art. 39-2) and non-resident withholding (art. 141.4) checks for 2,555 days (art. 44.3).

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Return not filed or filed late | UAH 340 per return; UAH 1,020 if fined for the same breach in the past year | TCU art. 120.1 |
| Agreed tax paid late, up to 30 days | 5% of the debt paid | art. 124.1 |
| Agreed tax paid late, more than 30 days | 10% of the debt paid | art. 124.1 |
| Late payment, intentional | 25% of the unpaid amount | art. 124.2 |
| Intentional late payment repeated within 1,095 days, or more than 90 days late | 50% of the unpaid amount | art. 124.3 |
| Tax assessed by the tax authority (understatement) | 10% of the assessed amount | art. 123.1 |
| Same, intentional | 25% | art. 123.2 |
| Intentional, repeated within 1,095 days | 50% | art. 123.3 |
| Withholding on a non-resident payment not withheld or not paid | 10%; 25% if intentional; 50% if repeated within 1,095 days; 75% the third time or more | art. 125-1 |
| Self-correction: amended return and payment before filing it | 3% of the understatement | art. 50.1 "а" |
| Self-correction: understatement added to the next period's return | 5% of the understatement | art. 50.1 "б" |
| Self-correction made without paying the self-assessed fine | 5% of the understatement | art. 120.2 |
| Penalty interest (пеня) on late payment | 120% a year of the National Bank of Ukraine discount rate, for each day late including the day of payment | art. 129.4 |
| Penalty interest on self-corrected amounts | 100% a year of the NBU discount rate, from the 91st day after the payment deadline | art. 129.1.3, 129.4 |

**Martial law, self-correction.** From 1 August 2023 until martial law ends, a company that self-corrects an understatement under art. 50 pays no art. 50.1 fine and no penalty interest (section XX, subsection 10, point 69.38). The 3% and 5% rows above apply again once martial law ends.

**Martial law.** A company that cannot file or pay on time because of martial law is released from liability, but must meet the obligation within six months after martial law ends or is lifted (section XX, subsection 10, point 69.1). A company that can file and pay on time does not get this relief.

## Cross-border points

- **Withholding at 15%.** A Ukrainian payer withholds 15% from Ukrainian-source income paid to a non-resident and pays it to the budget at the time of payment, unless a treaty in force sets a different rule (art. 141.4.2). The income covered includes interest, dividends, royalties, freight and engineering, operating lease rent, gains on Ukrainian real estate and certain shares, broker and agency fees, and cultural, sports and entertainment fees (art. 141.4.1). Income received through a Ukrainian permanent establishment is taxed with the PE, not by withholding (art. 141.4.2).
- **Other rates.** Freight 6% (art. 141.4.4). Insurance payments 0%, 4% or 12% by contract (art. 141.4.5). Interest on loans funded by Eurobonds listed on an approved exchange 5% (art. 141.4.11). Profit on discount bonds and treasury bills at the 18% rate (art. 141.4.3). Interest and gains on government and local bonds are not taxed, with an exception for some income of residents of listed low-tax states (art. 141.4.10).
- **Gross-up.** If the income is paid in kind, or tax was not withheld, the tax is grossed up: tax = paid amount x 100 / (100 - rate) - paid amount (art. 141.4.2).
- **Treaty rates.** The payer may apply a treaty rate itself at the time of payment if the non-resident gives a residence certificate and is the beneficial owner (art. 103.2 to 103.4). Treaty rates are not listed here.
- **Excess payments treated as dividends.** Payments to non-residents treated as dividends under art. 14.1.49, paragraphs 4 to 6 (such as amounts above arm's length), bear 15% withholding on the excess (art. 141.4.2).
- **Sale of Ukrainian assets between non-residents.** A non-resident buying, from another non-resident, shares whose value comes mostly from Ukrainian real estate withholds 15% of the gain and must register with the tax authority by the first payment (art. 141.4.2).
- **Foreign tax credit.** Foreign income tax paid by a resident company is credited, up to the Ukrainian tax for the period. A written confirmation from the foreign tax authority and a treaty in force are needed (art. 141.4.9).
- **Withholding by single-tax payers.** Single-tax payers paying non-residents withhold under art. 141.4 and report on an annual return (art. 133.1.4, 137.5).

## Worked examples

**Example 1. Small LLC, annual filer, 2026.** An LLC (ТОВ) had 2025 income, net of VAT, of UAH 30,000,000. That is not above UAH 40 million, so it files an annual 2026 return and may use its accounting result without tax differences (art. 134.1.1, 137.5). Its 2026 accounting profit before tax is UAH 2,400,000. It has an unrecovered loss of UAH 400,000 from earlier years. It is not a large taxpayer, so the whole loss is deducted (art. 140.4.4). Taxable profit is UAH 2,000,000 and the tax at 18% is UAH 360,000. The return is due by 1 March 2027 and the tax by 11 March 2027.

```oa-check
name: Small LLC under UAH 40m, full loss offset, 2026
inputs:
  prior_year_income: 30000000
  accounting_profit: 2400000
  loss_brought_forward: 400000
steps:
  - small_taxpayer_headroom: 40000000 - prior_year_income
  - taxable_profit: max(accounting_profit - loss_brought_forward, 0)
  - cit: taxable_profit * 0.18
expected:
  small_taxpayer_headroom: 10000000
  taxable_profit: 2000000
  cit: 360000
```

**Example 2. Large taxpayer with a loss, then a dividend to a foreign parent.** A large taxpayer has an unrecovered loss of UAH 10,000,000 at 1 January 2026. Its 2026 profit after all tax differences, before the loss, is UAH 8,000,000. The loss is more than 10% of that profit (UAH 800,000), so only 50% of the loss, UAH 5,000,000, is deducted (art. 140.4.4). Taxable profit is UAH 3,000,000 and the tax at 18% is UAH 540,000. The other UAH 5,000,000 of loss carries forward. The company pays the 2026 tax on time. In 2027 it pays a dividend of UAH 4,000,000 out of 2026 profit to its parent abroad. The dividend exceeds the 2026 object of tax by UAH 1,000,000, so the advance payment is 18% of that, UAH 180,000, paid before or with the dividend (art. 57.1-1.2). It is credited against the 2027 tax. The company also withholds 15% of the dividend, UAH 600,000, unless a treaty rate applies (art. 141.4.2).

```oa-check
name: Large taxpayer 50% loss limit, dividend advance and withholding
inputs:
  profit_before_loss: 8000000
  loss_brought_forward: 10000000
  dividend: 4000000
steps:
  - ten_percent_test: profit_before_loss * 0.10
  - loss_used: min(loss_brought_forward * 0.5, profit_before_loss)
  - taxable_profit: profit_before_loss - loss_used
  - cit_2026: taxable_profit * 0.18
  - loss_carried: loss_brought_forward - loss_used
  - advance_base: max(dividend - taxable_profit, 0)
  - dividend_advance: advance_base * 0.18
  - withholding: dividend * 0.15
expected:
  ten_percent_test: 800000
  loss_used: 5000000
  taxable_profit: 3000000
  cit_2026: 540000
  loss_carried: 5000000
  advance_base: 1000000
  dividend_advance: 180000
  withholding: 600000
```

## Ask the client first

1. What was the company's income, net of VAT, for 2025, and is it a large taxpayer? This sets annual or quarterly filing, the UAH 40 million option and the loss limit.
2. Is it a bank, another financial institution, an insurer, a gambling or lottery operator, a fuel retailer or a Diia City resident? Each has its own rate or rules.
3. What unrecovered losses does it carry from earlier years?
4. Does it plan dividends, to whom (individuals, Ukrainian companies, non-residents), and out of which year's profit?
5. Does it pay non-residents (interest, royalties, services, freight), deal with related non-residents or buy from listed low-tax states? Withholding, thin capitalisation, the 30% add-back and transfer pricing follow.
6. Is any part of the business in a territory affected by hostilities, so that it could not file or pay on time?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine (Податковий кодекс України), Law No. 2755-VI, consolidated text with amendments up to Law No. 4967-IX of 3 Sep 2026: arts. 14.1.24, 39.2.1.7, 44.3, 46.2, 49.18, 49.20, 50.1, 57.1, 57.1-1, 103.2-103.4, 120, 123, 124, 125-1, 129, 133, 134.1.1, 136, 137.4, 137.5, 137.9, 138, 140.2, 140.4, 140.5.4, 140.5.9, 141.4, 141.9-1, 141.14; section XX subsection 4 points 4-2, 68, 70, 72, 73; subsection 10 points 16-1, 69.1, 69.38, 76.1 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network, and again by curl and a browser tab at review on 30 Oct 2026; official text read via web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: the NBU discount rate that drives penalty interest in 2026; treaty withholding rates; the corporate income tax return form and its annexes (Ministry of Finance order not read); the full Diia City special-conditions base; the bank rate for 2027 and later; any amendment after the 12 October 2026 archive capture.

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
