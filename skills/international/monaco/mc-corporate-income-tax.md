---
name: mc-corporate-income-tax
description: "Monaco business profits tax working paper for 2026, covering industrial and commercial enterprises, the inclusive foreign turnover boundary, separate rights income scope, ordinary rate, losses, conditional new activity relief, advances, filing deadlines and statutory sanctions. Use for Monaco corporate income tax, ISB, foreign turnover, loss carryforward and tax instalment questions. Computes the executive remuneration ceiling, financing restrictions, participation deduction and ordinary accounting to tax adjustments. Includes loss carryback, disposals, reinvestment, cessation and filing controls. Source cited draft awaiting a named Monaco professional review."
jurisdiction: MC
category: international
tax_year: 2026
last_updated: 2026-10-25
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.3
---

# Monaco business profits tax (ISB)

> **Source-cited draft.** Checked 25 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Who this applies to

Tax year 2026, ordinary Monaco impôt sur les bénéfices (ISB). Despite this inherited filename, the tax applies to industrial or commercial enterprises **whatever their legal form**, including an individual proprietor. Article 1(1)(a) brings an enterprise operating in Monaco into scope when **at least 25%** of its turnover arises from operations outside Monaco, directly or through an intermediary. Exactly 25% is inside the statutory boundary. A separate article 1(1)(b) limb covers companies receiving specified patent, trademark, manufacturing-process or literary/artistic rights income. Do not apply the turnover gate to that separate limb. [Ordinance 3.152, arts. 1–4](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Article 3 tests goods destinations and where services, rights or rented property are used. A customer's address alone is insufficient. On-site retail cash sales in Monaco are expressly excluded from foreign sales under that article. A government summary uses “more than 25%”; this Guide follows the inclusive statutory wording.

## Rates, bands and thresholds

| Item | Amount | Period | Official source |
|---|---|---|---|
| Ordinary ISB | 25% | From 1 January 2022, including 2026 | [Art. 21](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Industrial/commercial foreign turnover gate | At least 25% | 2026 | [Art. 1(1)(a)](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Ordinary loss-use ceiling | EUR 1,000,000 plus 50% of profit above EUR 1,000,000 | 2026 | [Art. 7](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Each ordinary advance | One fifth of reference tax | 2026 | [Art. 31](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152) |
| Qualifying new-activity taxable fractions | Exempt period, then 25%, 50%, 75% | Successive statutory periods | [Arts. 1–3](https://legimonaco.mc/tnc/ordonnance/1991/10-17-10.324) |

## The base

Start from the article 8 net-asset bridge: closing net assets minus opening net assets, minus capital introduced, plus proprietor/partner withdrawals. Include disposal gains. Value inventory at cost or the lower closing market price; work in progress at cost. Reconcile the accounting result to tax, recording each addition and deduction separately. Ordinary business expenses, actual depreciation within industry practice and precisely identified probable provisions booked and disclosed in the year are deductible. Reverse unused or misapplied provisions. Add back ISB itself, tax fines, bribes and the private hunting, leisure-home and yacht expenses specified in article 9. This is not a flat tax on turnover. [Arts. 8–9](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

For passenger vehicles acquired or leased in 2026, the depreciation cost ceiling is EUR 18,300 ordinarily, EUR 30,000 for emissions below 20 g/km, EUR 20,300 for 20 to below 60 g/km, and EUR 9,900 above 130 g/km. Add back depreciation attributable to cost over the applicable ceiling; the analogous lessor-depreciation fraction of rent is restricted for leases other than non-renewable rentals of at most three months. Retain the disallowed depreciation when determining the later disposal gain as article 9(3) directs. Do not apply a generic capital-allowance percentage. [Art. 9(1)–(4)](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

**Executive remuneration.** First require real work and an amount consistent with international practice. For annual turnover `T` up to EUR 3.5 million for services or EUR 7 million for other businesses, use `B = 125000` or `250000` respectively, and `n = ceil(max(T - B, 0) / B)`. The highest-paid executive's salary ceiling is `67680 × (1 + 0.75 × min(n, 7) + 0.8 × max(n - 7, 0))`. The initial EUR 67,680 is the **fixed 1 October 2001 reference**, not the current social-security ceiling. Count a fraction of an additional band as a whole band. For turnover above the scope ceiling, the actual-work/non-excessive rule applies instead of extrapolating the scale. Article 13 permits an increase of up to 15% for personal functional expenses; other executives' deductible remuneration cannot exceed 75% of the remuneration and flat-rate expenses under paragraph 1. Save turnover classification, band count, actual remuneration and add-back in the reconciliation. [Ordinance 373, art. 2(4)](https://legimonaco.mc/tnc/ordonnance/2006/01-26-373/); [Ordinance 3.152, art. 13](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

**Interest and net finance.** Article 9(1)(3) restricts shareholder-loan interest to the Banque de France advances reference rate plus two percentage points. For shareholders controlling management, the aggregate eligible advances also cannot exceed half the share capital. The Banque de France’s decision of 8 July 2005 article 2 defines its advances-on-securities reference as the ECB marginal lending facility **plus two percentage points**; Monaco article 9 adds **a further two points**. Thus the derived ceiling is the marginal lending rate plus four points, not the French company current-account deduction rate. The ECB history gives the following effective periods checked through 25 October 2026: 1 January–16 June, marginal 2.40%, Banque advances 4.40%, Monaco ceiling **6.40%**; 17 June–15 September, 2.65% / 4.65% / **6.65%**; from 16 September to this check, 2.90% / 4.90% / **6.90%**. Split the balance/time calculation where rates or advances change and recheck later changes for a period closing after this research date. Retain the rate history and calculation. [Banque de France decision, arts. 1–2](https://www.banque-france.fr/system/files/2023-10/Banque%20de%20France%20-%20D%C3%A9cision%20du%20Gouverneur%20du%208%20juillet%202005.pdf); [ECB effective-date history](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html). Then apply article 9(5): deductible net finance costs are limited to the greater of EUR 3 million for the statutory period (with its twelve-month adjustment) and 30% of the pre-loss tax result increased by net finance costs, allowed depreciation/provisions and asset-disposal gains/losses as prescribed. Carry disallowed net costs to later years under the same cap; unused capacity lasts five years. If average related-company debt exceeds 1.5 times equity (opening or closing, at the enterprise's election), the related-debt fraction instead has the EUR 1 million/10% limit; only one third of its disallowed amount carries forward and unused capacity does not. Relatedness includes majority ownership, actual decision power and common control. Keep these two carry schedules separate. [Art. 9(1)(3), (5)](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Article 12 permits specified fees, royalties and commissions paid to Monaco residents only if the recipient is independent and the underlying act/payment is genuine, with sufficient evidence. Article 14 separately restores normal conditions for foreign transactions. [Arts. 12–14](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

**Participations.** Article 15 applies to a Monaco company limited by shares holding at least 20% of the payer. Check the permitted registered shares/interests and uninterrupted holding since subscription/issue, or acquisition and holding in the required form for **more than two consecutive years** at distribution. Deduct qualifying net participation income less the expense quota: 20% below a 35% holding, 10% from 35% to below 50%, 5% from 50%. The quota cannot exceed the investor's total actual expenses for the tax period. There is no article 22 foreign credit on the participation income removed under this provision. This is not a universal dividend exemption for every SARL. [Art. 15](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Separate foreign-operation net profits **and losses** excluded by article 1(2): foreign permanent establishments, habitual complete business cycles abroad and qualifying foreign representatives. Do not remove all foreign-customer profit. Ordinary loss use is `min(available loss, positive profit, 1000000 + 0.5 × max(profit - 1000000, 0))`; carry the unused loss forward. Article 7 increases the million-euro amount for qualifying debt waivers in the specified insolvency procedures. A capital company subject to ISB (the statute’s « société de capitaux soumise à l’impôt sur les bénéfices ») can elect article 7 bis carryback against the **preceding year's undistributed profit**, limited to the lower of that profit and EUR 1 million, by the loss-year return deadline. The resulting non-taxable claim pays ISB over the next five years; refund the unused remainder after that period. No carryback in the cessation, merger or liquidation year, and no unrestricted assignment of the claim. [Arts. 1(2), 7–7 bis](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

**Disposals and continuity.** Article 10 permits deferral of eligible in-business fixed-asset gains if the enterprise attaches an undertaking to reinvest the gain **plus original cost** in permitted business fixed assets within three years after the disposal-year close. Deduct the deferred gain from the replacement asset's tax cost; failed reinvestment brings it into the deadline-year result. Article 11(1) permits the specified direct-family/spouse continuation of an individual business only at unchanged asset values. Article 11(2)'s qualifying company-merger relief excludes inventory and requires the merger deed and carryover depreciation/gain bases. For total/partial transfer or cessation, article 11(3) includes fixed-asset disposal gains at one half if less than five years after creation/purchase of the business, or one fifth after that period. These rules require transaction-specific classification; moving abroad is not a general tax-free exit. [Arts. 10–11, 29](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

New-activity relief runs through the end of the twenty-third month following the creation month, then three successive twelve-month periods with taxable fractions of one quarter, one half and three quarters. Timely declaration is a condition. Exclude banking/finance, insurance and property management/rental under article 1. Article 2 bars a new company whose capital is held **more than 50% directly or indirectly by other companies**. Its deemed-indirect branches include an associate managing/presiding over another company in the listed offices; an associate with spouse/minor children holding **at least 25%** in another enterprise; or an associate exercising functions in an enterprise with similar/complementary activity. Test these branches separately from direct legal ownership. Article 3 also excludes concentration, restructuring, extension or takeover of pre-existing activities. Do not describe this as an automatic two-year exemption for every new company. [Arts. 1–3](https://legimonaco.mc/tnc/ordonnance/1991/10-17-10.324).

## Deadlines and filing

File the article 23 declaration and supporting reconciliations with the Direction des Services Fiscaux (DSF) within three months after year end. If no financial year closes in a calendar year, file before 1 April of the following year. Article 23 lists turnover, remuneration, accounts, adjustments and foreign-tax evidence. Prepare the results declaration, balance sheet, profit and loss account, depreciation/provision schedules, remuneration and distributions statement, adjustments, foreign-operation split and foreign-tax receipts for DSF. The government filing procedure identifies results form **353-0018_01-2019**. Lodge or send it to DSF with certified accounts (balance sheet, profit/loss and income statement), depreciation/provision and general-expense schedules, attendance and applicable meeting reports/minutes, and the relevant remuneration, reinvestment, loss-carryback, credit and foreign-tax exhibits. Pay the balance by cheque, transfer or cash with payment form **353-0016_01-2012**. These form identifiers, documents and routes were read on the government procedure page; its linked PDF downloads returned 403 and no account submission or payment was performed. Follow the native article 23 deadline, rather than the English page’s ambiguous “final three months” translation. [Government ISB declaration/payment procedure](https://monentreprise.gouv.mc/en/themes/accounting-obligations-and-tax/tax/taxes-on-profits/how-to-declare-and-pay-corporate-income-tax). [Art. 23](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Ordinary advances fall in February, May, August and November. Each is one fifth of tax on the statutory reference result, with annualisation for non-twelve-month periods and the prior-result/true-up rule where the latest declaration is not yet due. The balance is due by the declaration deadline. A reduction declaration has its own fifteen-day advance notice and error conditions; do not simply stop payments. For sale/cessation, including a company seat or establishment moving abroad, file for the final period in the month following the effective event month; the corresponding tax is immediately payable. Transferor and transferee have joint liability. Directors/managers/legal representatives have the separate article 30 joint liability. Carry advance overpayments forward; article 32 permits refund if the business ends or has losses for two successive years. [Arts. 29, 31–32](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

Disclose non-employee fees, commissions, royalties and similar article 23(5) payments exceeding EUR 75 per recipient in the first three months of the year. Omission removes the deduction, subject to the first-offence correction rule, in addition to the ordinary fine. The results declaration also identifies interest exceeding EUR 500 per recipient under article 23(1)(9). Maintain books for ten years under Commercial Code article 13; DSF can inspect the supporting records and require a sworn translation of foreign-language accounts under article 24. [Arts. 23–24](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152); [Commercial Code, arts. 10–13](https://legimonaco.mc/code/code-commerce/).

## Penalties and interest

Article 34 sets a EUR 15–75 late-results-declaration fine and EUR 1–15 for specified missing information. Article 35's late-payment rule, where the required declarations/formalities are complete, is 3% if paid within the month after the due date, plus 1% for each additional month or fraction. Other good-faith contraventions and assessment adjustments can attract penalties up to 150% of omitted or jeopardised tax; article 37 prescribes a fine equal to four times the tax for bad faith or fraud, with further consequences. These are different triggers, not a single penalty to apply to every late return. A reasoned proposed assessment adjustment allows twenty days for observations under article 26. Article 33 normally ends the recovery/refund limitation at the end of the third calendar year following the year of the relevant accounting close; specified notice interrupts recovery limitation. Send refund petitions to DSF and follow article 41 for contested assessments. [Arts. 34–37](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152).

## Cross-border points

Article 22 permits evidenced foreign-income-tax credit against Monaco tax on the same income, with gross-up. Article 15 excludes credit on the participation income removed under that provision. Establish entity, holding, income and treaty conditions first. See [cross-border](mc-cross-border.md) and [transfer pricing](mc-transfer-pricing.md). Use the linked transfer-pricing Guide for the EUR 750 million country-by-country reporting screen. This ordinary business Guide does not compute multinational minimum-tax, bank/insurance or specialised tax-credit regimes. Project 1.129 is legislative history and is not evidence of operative obligations. [Arts. 15, 22–23](https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152); [Project 1.129](https://legimonaco.mc/projet/1.129).

## Two worked examples that recompute

### Ordinary business and advances

An in-scope enterprise has EUR 100,000 of reconciled taxable profit, no relief, loss or credit. ISB is EUR 25,000. Assume the correctly established reference profit for all four advances is EUR 80,000: reference tax EUR 20,000, each advance EUR 4,000, total EUR 16,000, balance EUR 9,000. Articles 21 and 31 control; the example assumes no interim reference change.

```oa-check
name: Ordinary ISB and four unchanged-reference advances
inputs:
  profit: 100000
  reference_profit: 80000
steps:
  - tax: profit * 0.25
  - reference_tax: reference_profit * 0.25
  - advance: reference_tax / 5
  - paid: advance * 4
  - balance: tax - paid
expected:
  tax: 25000
  advance: 4000
  balance: 9000
```

### Loss ceiling edge

An in-scope business has EUR 2,000,000 profit before ordinary carried losses and EUR 2,000,000 eligible losses. The ceiling is EUR 1,500,000, leaving taxable profit EUR 500,000, ISB EUR 125,000 and EUR 500,000 losses carried forward. This assumes no special insolvency increase or continuity restriction. Article 7 supplies the ceiling.

```oa-check
name: Ordinary loss ceiling above EUR one million
inputs:
  profit: 2000000
  loss: 2000000
steps:
  - ceiling: 1000000 + max(0, profit - 1000000) * 0.5
  - used: min(loss, profit, ceiling)
  - taxable: profit - used
  - tax: taxable * 0.25
  - remaining_loss: loss - used
expected:
  used: 1500000
  tax: 125000
  remaining_loss: 500000
```

## Ask the client first

- What is the legal form, activity, rights income and financial year end?
- Where are goods delivered and services or rights used, and what is the evidenced turnover split?
- What foreign operations, group payments and director remuneration exist?
- What losses, relief conditions, foreign taxes and prior advances are documented?
- What is the group's size and structure for the CbCR screen and specialist minimum-tax assessment?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Government ISB declaration/payment, forms and supporting-document checklist, browser read | https://monentreprise.gouv.mc/en/themes/accounting-obligations-and-tax/tax/taxes-on-profits/how-to-declare-and-pay-corporate-income-tax | 2026-10-25 |
| Banque de France decision of 8 July 2005, arts. 1–2, advances reference | https://www.banque-france.fr/system/files/2023-10/Banque%20de%20France%20-%20D%C3%A9cision%20du%20Gouverneur%20du%208%20juillet%202005.pdf | 2026-10-25 |
| ECB official rate history, effective 11 June 2025, 17 June and 16 September 2026 | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-25 |
| Ordinance 3.152, arts. 1–15, 21–26, 29–37, 41–42 | https://legimonaco.mc/tnc/ordonnance/1964/03-19-3.152 | 2026-10-25 |
| Ordinance 10.324, arts. 1–3 | https://legimonaco.mc/tnc/ordonnance/1991/10-17-10.324 | 2026-10-25 |
| Project 1.129, project status and explanatory introduction only | https://legimonaco.mc/projet/1.129 | 2026-10-25 |
| Ordinance 373, art. 2(4), executive scale | https://legimonaco.mc/tnc/ordonnance/2006/01-26-373/ | 2026-10-25 |
| Commercial Code, arts. 10–13, books and retention | https://legimonaco.mc/code/code-commerce/ | 2026-10-25 |
| Government ISB page, scope, rate, executive-scale limits and document links, read in normal browser | https://monentreprise.gouv.mc/en/themes/accounting-obligations-and-tax/tax/other-taxes-and-duties/corporate-income-tax | 2026-10-25 |

**Not yet confirmed:** specialised sector, multinational minimum-tax and tax-credit calculations. Retain the effective-date shareholder-interest calculation and DSF form version used. The ordinary statutory methods and filing obligations above are established; this research did not access a taxpayer account.

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
