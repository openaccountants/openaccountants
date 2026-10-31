---
name: ee-corporate-income-tax
description: "Estonian corporate income tax for tax year 2026 under the Income Tax Act (tulumaksuseadus) consolidated text in force from 1 October 2026. Estonia taxes a company only when it distributes profit: 22% of the gross amount, charged as 22/78 of the net payment. Covers dividends, capital reductions, share buybacks and liquidation, deemed distributions (fringe benefits, gifts and donations, entertainment, non-business expenses, loans to shareholders), the participation exemption, the 2025 abolition of the 14/86 rate and the 7% withholding when 14/86-taxed dividends are passed on to individuals, the 18% quarterly advance tax for banks, exceeding borrowing costs, the cancelled 2026 rise to 24% and security tax, the monthly TSD return, interest and fines. Trigger on 'Estonia corporate tax', 'OÜ dividend tax', '22/78', 'distributed profit tax Estonia', 'TSD dividend', 'Estonian fringe benefit tax'. Out of scope: withholding on payments to non-residents and permanent establishments (ee-cross-border), transfer pricing (ee-transfer-pricing), individuals (estonia-income-tax), social tax (estonia-social-contributions), payroll (estonia-payroll), VAT (estonia-vat-return)."
version: 0.1
jurisdiction: EE
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia corporate income tax, tax year 2026

> **Source-cited draft.** Drafted from the Income Tax Act (tulumaksuseadus, TuMS) consolidated text in force 1 October to 31 December 2026, in Estonian and in the official English translation, the Taxation Act (maksukorralduse seadus, MKS) in force from 17 October 2026, Estonian Tax and Customs Board (EMTA) pages and Ministry of Finance notes, read on 2026-10-23 and 2026-10-24. No accountant has reviewed it. Do not file from it without review by a qualified Estonian professional.

Tax period: the calendar month for distributions and deemed distributions (TuMS § 3(2)). Currency: euro. Authority: Maksu- ja Tolliamet (EMTA); returns are filed in e-MTA.

See also: `ee-cross-border` (withholding on payments to non-residents, permanent establishments, foreign tax credit, exit tax), `ee-transfer-pricing` (§ 50(4) adjustments and documentation), `estonia-income-tax` (individuals), `estonia-social-contributions` (social tax), `estonia-payroll`, `estonia-vat-return`, `ee-tax-overview`, `ee-company-formation`.

## Who this applies to

**Resident companies.** A legal person founded under Estonian law is resident; so is an SE or SCE with its registered office in Estonia (TuMS § 6(2)). A resident legal person pays income tax on the objects in §§ 48 to 52^1 and withholds tax on the payments in § 41 (§ 6(2)). In practice this means an OÜ, AS, general or limited partnership (§ 50(1) names partnerships expressly) and a profit-making state agency (§ 2(3)).

**What is taxed.** Not the annual profit. Income tax is charged on profit when it is distributed, whatever the form, and on gifts and donations, costs of entertaining guests, expenses and payments not related to business, and assets moved out to a permanent establishment (§ 1(3)). Fringe benefits to employees and board members are taxed on the employer (§ 1(2), § 48). Profit the company keeps and reinvests is not taxed.

**Non-profit associations, foundations and religious associations** that are legal persons pay the same tax on gifts, non-business expenses and payments outside their statutory aims (§ 51(3), § 49(6)). Those entered on EMTA's list of associations with tax incentives (§ 11) have wider exemptions for gifts and entertainment (§ 49(2), (4), (6)).

**Credit institutions.** A resident credit institution and the Estonian branch of a non-resident credit institution also pay a quarterly advance income tax on profit (§ 47^1).

**Non-resident companies** with an Estonian permanent establishment pay under § 53 on profit moved out of the establishment. That regime and withholding on payments to non-residents are in `ee-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Income tax rate | 22% | 2026 | TuMS § 4(1), [riigiteataja.ee/akt/TuMS](https://www.riigiteataja.ee/akt/TuMS) |
| Gross-up for distributions and deemed distributions | Taxable amount ÷ 0.78 × 22%, so 22/78 of the net amount | 2026 | TuMS § 4(1^1); [EMTA tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates) |
| Reduced 14/86 rate on regular dividends | Abolished from 1 January 2025 (former § 50^1 repealed) | 2025 onward | TuMS § 4(4) and § 50^1, repealed by RT I, 30.06.2023, 107; EMTA tax rates |
| Withholding when a company passes on to an individual a dividend it received (exempt under § 50(1^1)) whose underlying profit was taxed at 14/86 under former § 50^1 | 7% | 2026 | TuMS § 61(68) |
| Planned rise to 24% (and 0.78 to 0.76) from 1 January 2026 | Cancelled before it took effect; the rate stays 22% for companies and individuals | 2026 | Enacted by § 3 of the act of 18.06.2025 (RT I, 08.07.2025, 1); deleted by § 1 of the act of 03.12.2025 (RT I, 18.12.2025, 3); [Ministry of Finance, 23.12.2025](https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused) |
| Security tax (julgeolekumaks) on company profit | Does not apply: the Security Tax Act (RT I, 02.01.2025, 2) was repealed before it took effect | 2026 | § 2 of the act of 18.06.2025 (RT I, 08.07.2025, 1); [Ministry of Finance, 18.06.2025](https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused) |
| Participation exemption, minimum holding | 10% of shares or votes at the time the dividend is received | 2026 | TuMS § 50(1^1) points 1 and 3 |
| Credit institution advance tax | 18% of the previous quarter's profit, no gross-up | 2026 | TuMS § 4(5), § 47^1 |
| Advertising gifts | Exempt up to EUR 21 per item, excluding VAT | 2026 | TuMS § 49(1) |
| Donations to listed associations | Exempt up to 3% of the year's payments subject to social tax, or 10% of last financial year's accounting profit (one limit, chosen by the company) | 2026 | TuMS § 49(2), (3) |
| Entertaining guests and partners | Exempt up to EUR 50 a month plus 2% of that month's payments subject to social tax | 2026 | TuMS § 49(4) |
| Employee health expenses | Exempt up to EUR 400 per employee a year, if offered to all employees | 2026 | TuMS § 48(5^5) |
| Employee accommodation | Exempt up to EUR 500 a month in Tallinn or Tartu, EUR 250 elsewhere, if the home is at least 50 km away and the employee owns no housing closer to work | 2026 | TuMS § 48(5^6) |
| Company car available for private use | EUR 1.96 per kW a month; EUR 1.47 per kW if the car is older than five years | 2026 | TuMS § 48(8) |
| Exceeding borrowing costs | Taxed above EUR 3,000,000 and 30% of EBITDA | 2026 | TuMS § 54^2(1) |
| Late payment interest | 0.06% a day | 2026 | MKS § 117(1), [riigiteataja.ee/akt/MKS](https://www.riigiteataja.ee/akt/MKS) |

## The taxable base

**The formula.** For every taxable object in § 1(2), (3), (4) and (6) to (8), the amount is divided by 0.78 and then multiplied by 22% (§ 4(1^1)). A net dividend of EUR 78 costs EUR 22 of tax; the shareholder gets EUR 78 and owes no further Estonian tax on it. The bank advance tax in § 47^1 is the one exception: 18% on profit, no gross-up.

**Dividends and other profit distributions** (§ 50(1)). Tax arises when the dividend is paid, in money or in kind. A bonus issue (profit capitalised into share capital) is not taxed.

**Capital reductions, share buybacks and other payments from equity** (§ 50(2)). When a company reduces share capital, redeems or returns shares, or pays out of equity in any other way, only the part that exceeds the money and assets the shareholders contributed to equity is taxed. Contributions by merging companies and on a division follow special rules in the same subsection. Keep a running record of contributions and earlier repayments.

**Liquidation and deletion** (§ 50(2^2)). A company deleted from the register pays tax on the market value of its assets, including liquidation proceeds, above the contributions not yet repaid. This does not apply where the assets continue in another Estonian company or an Estonian permanent establishment.

**The participation exemption** (§ 50(1^1)). No tax is due on a dividend paid out of:
1. a dividend received from a company resident in an EEA state (including Estonia) or Switzerland that is liable to income tax, if the company held at least 10% of its shares or votes when it received the dividend (point 1);
2. profit of the company's own permanent establishment in an EEA state or Switzerland (point 2);
3. a dividend from a company in any other state, on the same 10% test, if tax was withheld on the dividend or the underlying profit was taxed (point 3);
4. profit of a permanent establishment elsewhere that was taxed (point 4);
5. a few other sources already taxed: § 50(2^1) payments, fund income, a repaid loan taxed under § 50^2, CFC profit taxed under § 54^3, and assets taxed on exit under § 54^5 (points 5 to 9).

Points 1 and 3 never apply to a company in a non-cooperative jurisdiction, and apply only if the paying company could not deduct the dividend (§ 50(1^3)). The same exemption carries through capital reductions and liquidation payments funded by exempt income (§ 50(2^1)). Dividends received up to 31 December 2024 that the paying subsidiary taxed at 14/86 can still be passed on tax-free under point 1 or 3, on the 10% test. Passed on to a corporate shareholder they carry no further tax; passed on to an individual, resident or not, the company withholds 7% (§ 61(68); EMTA tax rates). The 7% applies only to such received dividends. A company's own profit was taxed at 14/86 only when it was distributed before 2025, so its own retained pre-2025 profit paid out in 2026 is taxed at 22/78 like any other profit (§ 4(1), § 50(1)).

**Fringe benefits** (§ 48). The employer pays income tax on any benefit in money's worth given to an employee, a board or council member, a contractor under a services contract, or a person selling goods to it for over six months (§ 48(3)). The list includes housing costs, private use of company property, non-statutory insurance premiums, loans below market rate (unless the interest is at least twice the rate last published under § 94(2) of the Law of Obligations Act), transfers below or purchases above market price, waived claims, and education not related to the job (§ 48(4)). Benefits to relatives of the employee, or from a group company, count too (§ 48(6)). Share options are not a benefit if the shares are acquired at least three years after grant (§ 48(5^3)). Social tax is also due on fringe benefits; see `estonia-social-contributions`.

**Gifts and donations** (§ 49). Taxed unless tax was already withheld under § 41 or paid as a fringe benefit. Exempt: advertising items up to EUR 21 excluding VAT; donations to associations on EMTA's § 11 list within the annual 3% or 10% limit, counted for the whole year (§ 49(2), (3)). The company can recalculate at year end (§ 54(6)).

**Entertaining guests and business partners** (§ 49(4), (5)). Meals, accommodation, transport and entertainment for guests are exempt up to EUR 50 a month plus 2% of that month's payments subject to individually registered social tax. Unused monthly room can be used against later months of the same year.

**Expenses not related to business** (§ 51). Taxed, unless already taxed under §§ 48 to 50. They include: fines and non-compliance levies, and interest paid under the Taxation Act (through § 34 point 3); seized property; increased-rate environmental charges and pollution damages; payments to a person taxed under the Simplified Business Income Taxation Act; bribes; membership fees of non-profits not linked to the business; payments with no valid source document; and services or obligations not related to the business (§ 51(2)). TSD annex 6 lists them under codes 6010 to 6080 (6010 fines, 6020 interest, 6060 membership fees, 6070 no source document, 6080 non-business obligations, assets and services).

**Other payments not related to business** (§ 52). Buying assets not related to the business, and securities, holdings, loans or advances involving a legal person in a non-cooperative jurisdiction, are taxed when paid. Banks have their own list (§ 52(3)). If the circumstances later end, the company can recalculate and claim a refund (§ 54(6)).

**Loans to shareholders** (§ 50^2). A loan to a shareholder, partner or member is taxed if the circumstances show it may be a hidden profit distribution. For a loan to a parent company, or to another subsidiary of the same parent, with a term over 48 months, the company must prove on request that the borrower can and intends to repay (§ 50^2(1)). A later dividend paid out of a repaid loan that was taxed under § 50^2 is not taxed again (§ 50(1^1) point 7).

**Transactions to obtain a tax advantage** (§ 5^1, § 54^1). Non-genuine arrangements are ignored and the company is taxed on the income it would have had or the expense it would not have incurred.

**Transfer pricing** (§ 50(4)). The difference between a related-party price and market value is taxed as a deemed distribution. See `ee-transfer-pricing`.

**Exceeding borrowing costs** (§ 54^2). A resident company, other than a financial undertaking, is taxed on net borrowing costs above both EUR 3,000,000 and 30% of tax-adjusted EBITDA for the financial year, to the extent they exceed its loss. Out of scope of the rule: a standalone company with no associated enterprise or permanent establishment, EU long-term public infrastructure loans, and a group member using the equity ratio escape (§ 54^2(1), (8)).

**Controlled foreign companies** (§ 54^3). Profit of a controlled foreign company from non-genuine arrangements is attributed to the Estonian company. The rule does not apply where the CFC's profit is up to EUR 750,000 and its non-trading income up to EUR 75,000 (§ 54^3(4)).

**Banks' advance tax** (§ 47^1). A credit institution pays 18% of the previous quarter's profit, after deducting the quarter's exempt § 50(1^1) income and losses of up to 19 previous quarters. The advances are credited against tax on its distributions, and overpaid advances can be refunded when tax is calculated on liquidation (§ 54(4^1)).

**Losses.** There is no loss carry-forward for distributions, because profit is not taxed as it is earned. The 19-quarter loss rule applies only to the bank advance tax.

**Pillar Two.** The Act's global minimum tax chapter (§§ 54^10 and 54^11) charges no top-up tax. It sets information duties for Estonian-parented groups with at least EUR 750 million of revenue in two of the four preceding years, and rules on where an entity is located. No top-up tax computation is in this skill.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Declare distributions, gifts, entertainment, non-business expenses, loans under § 50^2 and other §§ 49 to 53 objects | Monthly TSD return by the 10th of the month after the month of payment | TuMS § 54(2) |
| Declare fringe benefits | TSD by the 10th of the following month | TuMS § 54(1) |
| Pay the tax | By the 10th of the month after the tax period | TuMS § 54(4) |
| Bank advance tax return and payment | By the 10th of the third month of each quarter, on the previous quarter's profit | TuMS § 47^1(1), § 54(2^1) |
| Exceeding borrowing costs and CFC profit | Declare and pay by the 10th of the ninth month of the next financial year | TuMS § 54^4(3) to (6) |
| Certificate to a shareholder of § 50(2) payments | On request, by the 5th of the following month | TuMS § 50(9) |

A dividend paid on 15 March 2026 is declared and paid by 10 April 2026. Tax follows the payment date, not the date of the shareholder resolution (§ 50(1): "upon payment thereof"; EMTA tax rates page on the cash basis of the TSD).

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Late payment of tax, including advance payments | Interest of 0.06% a day from the day after the due date up to and including the payment day | MKS § 115(1), (5); § 117(1) |
| Instalment schedule | EMTA may cut the interest rate by up to 50% | MKS § 117(2) |
| Late return, failure to register, poor records, ignoring an EMTA order | Fine up to 300 fine units (EUR 2,400) for an individual; up to EUR 3,200 for a legal person | MKS § 154(1), (2); fine unit EUR 8, Penal Code § 47(1) |
| Intentionally false or missing data that reduces tax or raises a refund | Fine up to 300 fine units (EUR 2,400) for an individual; up to EUR 32,000 for a legal person | MKS § 153^1(1), (2); Penal Code § 47(1) |

Interest and fines paid to EMTA are themselves expenses not related to business, so paying them also triggers 22/78 (TuMS § 51(2) point 1 with § 34 point 3; TSD annex 6 codes 6010 and 6020). Criminal tax offences are outside this skill.

## Cross-border points

1. **Dividends to non-residents.** The company pays 22/78; there is no extra withholding on dividends to a non-resident, except the 7% when a received dividend taxed at 14/86 before 2025 is passed on to an individual (§ 61(68)). Details, treaty relief and the foreign tax credit under § 54(5) are in `ee-cross-border`.
2. **Foreign dividends coming in.** Use the § 50(1^1) exemption above. A dividend from outside the EEA and Switzerland qualifies only if foreign tax was withheld on it or the underlying profit was taxed.
3. **Non-cooperative jurisdictions.** Payments, holdings and loans involving them are taxed under § 52 when made, and their dividends never qualify for the exemption.
4. **Permanent establishments.** A foreign company's Estonian branch pays the same 22/78 when it moves profit out (§ 53); a resident company moving assets to its foreign branch pays exit tax (§ 54^5). Both are in `ee-cross-border`.
5. **Related-party pricing** with foreign group companies: `ee-transfer-pricing`.

## Worked examples

### Example 1: OÜ pays a dividend and entertains clients in May 2026

An OÜ with no foreign income pays its two shareholders a net dividend of EUR 40,000 in May 2026, out of profit earned since 2025. In the same month it spends EUR 900 on client dinners and makes EUR 20,000 of wage payments subject to social tax. It used its full entertainment allowance in every earlier month of 2026.

Dividend tax: 40,000 ÷ 0.78 × 22% = EUR 11,282.05 (§ 4(1^1), § 50(1)).

Entertainment: the exempt amount is 50 + 2% × 20,000 = EUR 450 (§ 49(4)). The taxable excess is 900 − 450 = EUR 450, and the tax is 450 ÷ 0.78 × 22% = EUR 126.92.

Total tax for May: EUR 11,408.97, declared on the TSD and paid by 10 June 2026.

```oa-check
name: OÜ dividend plus entertainment over the limit, May 2026
inputs:
  net_dividend: 40000
  entertainment: 900
  social_tax_payments: 20000
steps:
  - dividend_tax: net_dividend / 0.78 * 0.22
  - entertainment_limit: 50 + social_tax_payments * 0.02
  - entertainment_taxable: max(entertainment - entertainment_limit, 0)
  - entertainment_tax: entertainment_taxable / 0.78 * 0.22
  - total_tax: round(dividend_tax, 2) + round(entertainment_tax, 2)
expected:
  dividend_tax: 11282.05
  entertainment_limit: 450
  entertainment_tax: 126.92
  total_tax: 11408.97
```

### Example 2: Holding company with an exempt subsidiary dividend and a capital reduction

An Estonian holding OÜ owns 100% of a Latvian company that is liable to Latvian income tax. In March 2026 it receives a EUR 30,000 dividend from it, which the Latvian company could not deduct. In April 2026 it pays a net dividend of EUR 50,000 to its corporate shareholder. In the same month it reduces share capital and pays EUR 25,000 to that shareholder; total contributions to equity were EUR 10,000 and none has been repaid before.

Dividend: EUR 30,000 is paid out of the exempt Latvian dividend (§ 50(1^1) point 1: EEA company, at least 10% held when received). Only 50,000 − 30,000 = EUR 20,000 is taxed: 20,000 ÷ 0.78 × 22% = EUR 5,641.03.

Capital reduction: only the payment above contributions is taxed (§ 50(2)): 25,000 − 10,000 = EUR 15,000, so 15,000 ÷ 0.78 × 22% = EUR 4,230.77.

Total for April: EUR 9,871.80 (each line rounded to the cent), on the TSD by 10 May 2026. The edge case: if the money passed on were instead a dividend received in 2024 from an Estonian subsidiary that taxed it at 14/86, it would also be exempt for a corporate shareholder, but paid to an individual it would carry 7% withholding (§ 61(68)).

```oa-check
name: Holding OÜ, exempt EEA dividend and capital reduction, April 2026
inputs:
  net_dividend: 50000
  exempt_dividend_received: 30000
  capital_reduction_paid: 25000
  contributions: 10000
steps:
  - taxable_dividend: max(net_dividend - exempt_dividend_received, 0)
  - dividend_tax: taxable_dividend / 0.78 * 0.22
  - taxable_reduction: max(capital_reduction_paid - contributions, 0)
  - reduction_tax: taxable_reduction / 0.78 * 0.22
  - total_tax: round(dividend_tax, 2) + round(reduction_tax, 2)
expected:
  taxable_dividend: 20000
  dividend_tax: 5641.03
  reduction_tax: 4230.77
  total_tax: 9871.80
```

## Ask the client first

1. What will be paid out, when, and to whom (resident or not, company or individual)? The payment date sets the month.
2. Has the company received dividends from subsidiaries, and for each: country, holding percentage at receipt, and whether foreign tax was withheld or the profit taxed?
3. How much have shareholders contributed to equity, and how much of it has already been repaid? This decides the taxable part of a capital reduction or buyback.
4. Does the company hold dividends received from subsidiaries before 2025 that the subsidiary taxed at 14/86, and will any of them be passed on to individuals?
5. Are there loans to shareholders or group companies, and on what terms and repayment record?
6. What benefits, gifts, entertainment and non-business costs went through the company this year, and what are the monthly payments subject to social tax?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tulumaksuseadus (Income Tax Act), consolidated text in force 01.10.2026 to 31.12.2026 (RT 109072026066), §§ 1 to 7, 34, 47^1 to 54^10, 61(68) to (70) | https://www.riigiteataja.ee/akt/TuMS | 2026-10-24 |
| Income Tax Act, official English translation of the same version | https://www.riigiteataja.ee/en/akt/520102026008 | 2026-10-23 |
| Maksukorralduse seadus (Taxation Act), consolidated text in force from 17.10.2026 (RT 116102026009), §§ 115, 117, 153^1, 154 | https://www.riigiteataja.ee/akt/MKS | 2026-10-24 |
| Karistusseadustik (Penal Code), consolidated text in force 01.10.2026 to 31.12.2026, § 47(1) (fine unit EUR 8 from 1 January 2025) | https://www.riigiteataja.ee/et/akt/109072026028 | 2026-10-24 |
| Act of 18.06.2025 repealing the Security Tax Act and amending the Income Tax Act (RT I, 08.07.2025, 1), §§ 2 to 4 | https://www.riigiteataja.ee/et/akt/108072025001 | 2026-10-24 |
| Act of 03.12.2025 amending the act of 18.06.2025 and the Income Tax Act (RT I, 18.12.2025, 3), § 1 deletes the 24% rise | https://www.riigiteataja.ee/et/akt/118122025003 | 2026-10-24 |
| EMTA, Tax rates (22/78, end of 14/86, 7% withholding, cash basis of the TSD) | https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates | 2026-10-23 |
| EMTA, Payment of interests | https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests | 2026-10-23 |
| Minister of Finance regulation, TSD annex 6 (non-business expenses, codes 6000 to 6060) | https://www.riigiteataja.ee/aktilisa/1260/6202/0024/RM_m24_lisa7.pdf | 2026-10-23 |
| Ministry of Finance, 2026 law changes (rise to 24% cancelled, rate stays 22%) | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused | 2026-10-23 |
| Ministry of Finance, Riigikogu approves security tax changes (18.06.2025) | https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused | 2026-10-23 |
| Government of Estonia, 2026 state budget approved | https://valitsus.ee/en/news/government-approved-2026-state-budget | 2026-10-23 |

Not yet confirmed: which TSD annex carries dividends and capital reductions (only annex 6 was read, in the wording of Regulation No. 24 of 22.06.2020); how a company that received both 14/86-taxed and other dividends traces which of them a 2026 payment comes from; the social tax base on fringe benefits (in `estonia-social-contributions`).

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
