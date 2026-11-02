---
name: estonia-tax-optimization
description: "Lawful tax planning in Estonia for tax year 2026, for a self-employed person, freelancer or small company owner. Covers the entity choice (FIE, OÜ or entrepreneur account), the 0% tax on profit an OÜ keeps and the 22/78 tax when it pays out, the salary-or-dividend mix for an owner-manager and EMTA's view that a dividend cannot replace pay for active work, tax-free limits for entertainment, gifts, donations and employee health, the flat EUR 8,400 basic exemption (the 2025 income taper is gone), the II pillar rate choice, III pillar and training deductions, the participation exemption for holding companies, and the anti-avoidance red lines. Trigger on 'reduce tax Estonia', '0% corporate tax', 'FIE vs OÜ', 'salary vs dividend Estonia', 'ettevõtluskonto', 'Estonian holding company', 'tax planning Estonia'. Figures come from the Income Tax Act and EMTA. Out of scope: computing returns (estonia-income-tax, ee-corporate-income-tax), payroll (estonia-payroll), social tax (estonia-social-contributions), VAT (estonia-vat-return), cross-border structures (ee-cross-border)."
version: 0.2
jurisdiction: EE
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Tax Optimization

## Estonia Tax Optimization Skill v0.2

**Tier 2. Figures for 2026 from the Income Tax Act (tulumaksuseadus, TuMS), the Social Tax Act (SMS), the Funded Pensions Act (KoPS), the Simplified Business Income Taxation Act and EMTA pages, listed under Sources. They agree with `estonia-income-tax`, `ee-corporate-income-tax`, `estonia-social-contributions` and `estonia-payroll`; if they ever differ, those skills win. Not signed off by an Estonian tax adviser. Every suggestion needs review by a credentialed professional; aggressive positions are never advised.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Estonia |
| Currency | EUR |
| Personal income tax | Flat **22%** in 2025 and 2026. The 24% rate enacted for 2026 was cancelled before it took effect (TuMS § 4(1); Ministry of Finance) |
| Security tax | **None in 2026.** It was dropped for company profit and personal income before 2026 (Ministry of Finance, 18.06.2025) |
| Company tax (OÜ) | **0% on retained profit**; **22%** on distribution, charged as 22/78 of the net amount (TuMS § 4(1), (1^1), § 50(1)). The reduced 14/86 rate on regular dividends was **abolished from 1 January 2025** (TuMS § 4(4) repealed; EMTA) |
| Dividend in the owner's hands | Not taxable income of the individual; the company has paid (TuMS § 12(2)) |
| Social tax | 33% on employment pay and board fees; it funds state pension (20 points) and health insurance (13 points) (SMS § 7(1), § 10(2)) |
| Basic exemption 2026 | EUR 8,400 a year, flat, no income taper; EUR 9,312 from the year of pensionable age (TuMS § 23(1), § 23^5(1)) |
| Key optimisation levers | Entity choice and profit deferral (OÜ 0% on retained profit); salary-dividend mix; entrepreneur account for small income; tax-free limits; II and III pillar; participation exemption for holdings |
| Anti-avoidance | EMTA treats a dividend that replaces pay for active work as pay; substance over form (MKS § 84); substance needed for holding structures |

- **Personal income tax.** Flat 22% (2025 and 2026).
- **Company tax (OÜ).** 0% on retained profit; 22% on distribution (22/78 of the net amount). The reduced 14% rate on regular dividends was abolished from 1 January 2025.
- **Social tax.** 33% on employment pay and board fees (funds pension and health cover).

> **The single biggest Estonian lever is the OÜ deferral:** profit kept inside an OÜ is taxed at **0%** until it is distributed. Profit reinvested in the business does not trigger the 22% while it stays there. This is lawful deferral, not avoidance, and not an exemption.

## Section 2 -- Entity Choice & Profit Deferral (the core decision)

**Entity Choice & Profit Deferral**

| Structure | Best when | Tax treatment (2026) |
| --- | --- | --- |
| **OÜ** (private limited company) | Profit reinvested or retained; wants limited liability; building value | **0% on retained profit**; 22% (22/78) only when profit is distributed or treated as distributed; owner-manager can take a salary or board fee. Details: `ee-corporate-income-tax` |
| **FIE** (sole proprietor) | Small, simple, wants income in own hands now | Business income taxed every year: 22% income tax on the annual return, and 33% social tax on business income after allowed deductions, minimum EUR 3,508.56 and maximum EUR 36,867.60 a year (SMS § 2(5), § 7(1); EMTA). **No deferral**; unlimited personal liability. Details: `estonia-income-tax`, `estonia-social-contributions` |
| **Ettevõtluskonto** (entrepreneur account) | Small or side income from selling services and goods, few expenses, customers mainly private individuals | The bank holds back **20%** of every receipt (**22%, 24% or 26%** if in the II pillar at 2%, 4% or 6%); the 20% is 22/55 income tax and 33/55 social tax. No bookkeeping and no deductions. Above **EUR 40,000** of receipts in a calendar year the person must register as an FIE or company and for VAT. The holder cannot be VAT-registered or an FIE in the same or a similar activity. A company that pays for a service into an entrepreneur account pays 22/78 company income tax on the payment on top (EMTA's example: a EUR 100 service costs the company EUR 128.20). EMTA says only LHV Pank offers the account (Simplified Business Income Taxation Act § 2(2), § 4, § 8(2); EMTA). Details: `estonia-income-tax` |

- **The deferral play.** An OÜ that keeps profit to fund hiring, equipment or expansion pays no company income tax at that stage. Tax (22/78) arises only on distribution. For anyone reinvesting, the OÜ beats the FIE, whose profit is taxed every year. Most growing businesses should be an OÜ. Entity choice detail: `ee-company-formation`.
- **The entrepreneur account test.** It suits a person whose costs are low, because the 20% is charged on receipts, not on profit, and nothing can be deducted.

## Section 3 -- Salary vs Dividend (OÜ owner-managers)

**Salary vs Dividend**

| Route | Cost | Notes |
| --- | --- | --- |
| **Board-member fee or employee salary** | 33% social tax on top; 22% income tax withheld after the II pillar contribution and any basic exemption; employee salary also carries 1.6% + 0.8% unemployment premiums | Builds state pension and health cover through social tax (SMS § 10(2)). Unemployment premiums cover employees, officials and people working under service contracts (Unemployment Insurance Act § 3(1)); a board-member fee is not on that list |
| **Dividend** | 22/78 company income tax; **no social tax** | No pension or health cover built. Not taxed again in the owner's hands (TuMS § 12(2)) |

- **The optimisation.** Pay a reasonable market salary or board fee for the work actually done (it keeps health insurance and builds pension rights), then distribute the rest as dividends.

> **AUDIT FLASH POINT.** EMTA's guidance says: "A shareholder is entitled to dividends but the dividend may not replace salary." Dividends "may be deemed salary income if a management board member is not paid remuneration ... at all or these are paid in very small amounts", and dividends paid frequently, for example monthly, are likely to be seen as replacing that period's pay. If pay is at or near the usual level in the industry, EMTA sees no tax risk (EMTA, About the payment of labour taxes). The legal base is substance over form (MKS § 84). Set the salary defensibly and document it. Never advise zero-salary-all-dividend for an active owner.

### Worked comparison: EUR 10,000 paid out as dividend or as board fee

An OÜ has EUR 10,000 of cash it is willing to spend on its sole owner, who is the board member, is in the II pillar at 2%, and has already used the basic exemption on other income. As a dividend, the company pays the net dividend plus 22/78 on it, so the net dividend is 10,000 × 0.78 = 7,800 and the tax 2,200. As a board fee, the fee plus 33% social tax must fit in 10,000, so the gross fee is 10,000 ÷ 1.33. The II pillar 2% comes off first, then 22% income tax on the rest (TuMS § 42(6)). No unemployment premium applies to a board-member fee. The owner nets about EUR 2,053 more through the dividend, but the board fee buys health insurance and pension rights that the dividend does not.

```oa-check
name: OÜ owner, EUR 10,000 as dividend or board fee (2026)
inputs:
  budget: 10000
steps:
  - net_dividend: budget * 0.78
  - company_tax: budget - net_dividend
  - gross_fee: budget / 1.33
  - social_tax: budget - gross_fee
  - pillar2: gross_fee * 0.02
  - income_tax: (gross_fee - pillar2) * 0.22
  - net_fee: gross_fee - pillar2 - income_tax
  - dividend_advantage: net_dividend - net_fee
expected:
  net_dividend: 7800.00
  company_tax: 2200.00
  gross_fee: 7518.80
  social_tax: 2481.20
  pillar2: 150.38
  income_tax: 1621.05
  net_fee: 5747.37
  dividend_advantage: 2052.63
```

## Section 4 -- Deductions & Expenses (Estonia works differently)

Estonia has **no annual profit-tax computation** for a company, so "deductible expenses" do not reduce a yearly tax bill the way they do elsewhere. Genuine business expenses are simply **not taxed**. Spending that is not business-related, gifts, donations, entertainment and fringe benefits are taxed at 22/78 in the month they are paid, unless a tax-free limit covers them (TuMS §§ 48 to 51). Details: `ee-corporate-income-tax`.

**Deductions & Expenses**

| Item | Treatment (2026) |
| --- | --- |
| Genuine business expenses | Not taxed if wholly business-related and documented |
| Fringe benefits (private use of company assets, perks to staff and board) | Taxed: 22/78 income tax, plus 33% social tax on the benefit and on that income tax, both paid by the company (TuMS § 48(1), § 4(1^1); SMS § 2(1) point 7; `estonia-payroll`). Keep business and private use apart |
| Company car available for private use | Benefit of EUR 1.96 per kW a month; EUR 1.47 per kW if the car is older than five years (TuMS § 48(8)) |
| Employee health costs (sport, exercise, health services) | Tax-free up to EUR 400 per employee a year, if offered to all employees (TuMS § 48(5^5)) |
| Entertaining guests and business partners | Tax-free up to **EUR 50 a month**, plus **2%** of that month's payments subject to personal social tax if the company makes such payments; the excess is taxed at 22/78 (TuMS § 49(4)). Small for a solo OÜ, larger with a payroll |
| Advertising gifts | Tax-free up to EUR 21 per item, excluding VAT (TuMS § 49(1)) |
| Gifts and donations to listed associations | Tax-free up to **3%** of the year's payments subject to personal social tax, **or 10%** of the last financial year's profit; the company picks one limit (TuMS § 49(2), (3)) |

### Worked comparison: entertainment allowance in one month

In June 2026 an OÜ pays EUR 6,000 of salaries subject to social tax and spends EUR 400 entertaining clients. Its tax-free amount for June is EUR 50 plus 2% of 6,000. The excess is taxed as a distribution: 22/78 of the excess, declared on the TSD by 10 July.

```oa-check
name: OÜ entertainment allowance, June 2026
inputs:
  payroll: 6000
  spent: 400
steps:
  - allowance: 50 + payroll * 0.02
  - excess: max(spent - allowance, 0)
  - tax: excess * 22 / 78
expected:
  allowance: 170.00
  excess: 230.00
  tax: 64.87
```

## Section 5 -- Reliefs & Personal Allowances

**Reliefs & Personal Allowances**

| Relief | Detail |
| --- | --- |
| **Basic exemption (maksuvaba tulu)** | **2026: EUR 8,400 a year (EUR 700 a month), the same at every income level** (TuMS § 23(1)). 2025: up to EUR 7,848, tapered between income of EUR 14,400 and EUR 25,200 and nil above (EMTA, calculation of basic exemption until the end of 2025) |
| **Pensionable-age exemption** | EUR 9,312 a year (EUR 776 a month) from the year the person reaches pensionable age (TuMS § 23^5(1)) |
| **II-pillar funded pension** | 2% by default; the member may choose **4% or 6%**, which then holds for at least a calendar year (KoPS § 9). The contribution is deducted before income tax is withheld (TuMS § 42(6)). An application to change the rate that reaches the register by 30 November applies from 1 January of the next year (KoPS § 17^2(8)) |
| **III-pillar supplementary pension** | Deductible up to **15%** of the year's taxable income, maximum **EUR 6,000** (TuMS § 28(2)) |
| **Training costs and donations** | Together up to **EUR 1,200** a year, and not more than 50% of the person's Estonian taxable income (TuMS §§ 26, 27, 28^2(1)) |

- **Basic exemption.** 2026: EUR 8,400 a year, flat. The 2025 taper is gone.
- **II-pillar rate choice.** A higher rate raises retirement saving and cuts taxable pay, at the cost of take-home pay now.

> The 2025 taper created a "tax hump" between EUR 14,400 and EUR 25,200 of income, where the effective marginal rate was higher; timing income across years near that band could help. **From 2026 there is no taper, so this lever no longer exists** for 2026 income. It still matters for checking a 2025 return.

## Section 6 -- Holding / Participation Exemption

- **Participation exemption on dividends received.** An Estonian company that receives a dividend from a company in an EEA state or Switzerland that is liable to income tax there (not in a non-cooperative jurisdiction), and that held **at least 10%** of the shares, units or votes **at the time it received the dividend**, pays no income tax again when it passes that dividend on to its own shareholders. Dividends from other foreign companies qualify on the same 10% test only if tax was withheld on the dividend or the underlying profit was taxed (TuMS § 50(1^1) points 1 and 3). In both cases the exemption applies only if the company that paid the dividend could not deduct it from its own taxable profit (TuMS § 50(1^3)). This makes Estonia a workable EU holding location. Details: `ee-corporate-income-tax`.
- **No minimum holding period** is set in § 50(1^1): the test is the holding when the dividend is received.

**AUDIT FLASH POINT.** A holding structure must have genuine substance. A letterbox holding set up mainly for tax can be challenged: Estonian law taxes a transaction by its real economic substance where it was made to avoid tax (MKS § 84).

## Section 7 -- Red Lines (do not cross)

- **Market-salary expectation.** Active owner-managers must take a reasonable salary or board fee; all-dividend-no-salary is a pattern EMTA reclassifies as pay.
- **Substance for holdings.** The participation exemption needs real economic substance.
- **Business vs private.** Private spending booked as business creates taxable fringe benefits or distributions, not deductions.
- **OÜ 0% is deferral, not exemption.** Never present the OÜ system as "no tax": 22/78 applies on distribution.

## PROHIBITIONS

- **Zero-salary-all-dividend advice.** NEVER advise an active owner-manager to take zero salary and only dividends to avoid social tax.
- **Describing the OÜ regime as tax-free.** NEVER describe Estonia's OÜ regime as tax-free. It is 0% on RETAINED profit only; distributions are taxed at 22% (22/78).
- **Abolished 14% reduced dividend rate.** NEVER assume the abolished 14/86 rate still applies (gone from 1 January 2025).
- **Cancelled 2026 rises.** NEVER use a 24% income tax rate or a security tax for 2026: both were cancelled before they took effect.
- **Substance-free holding company advice.** NEVER advise a substance-free holding company to exploit the participation exemption.
- **Contradicting related skills.** NEVER contradict the rates and exemptions in `estonia-income-tax`, `ee-corporate-income-tax`, `estonia-social-contributions` or `estonia-payroll`.
- **Presenting suggestions as definitive advice.** NEVER present optimisation suggestions as definitive advice. Always route to a licensed Estonian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Estonia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Tulumaksuseadus (Income Tax Act), consolidated text in force 01.10.2026 to 31.12.2026, §§ 4, 12, 23, 23^5, 26, 27, 28, 28^2, 42, 48, 49, 50 (incl. 50(1^1), 50(1^3)) | https://www.riigiteataja.ee/et/akt/109072026066 | 2026-10-30 |
| Sotsiaalmaksuseadus (Social Tax Act), consolidated text in force from 26.10.2026, §§ 2, 7, 10 | https://www.riigiteataja.ee/et/akt/116102026014 | 2026-10-30 |
| Maksukorralduse seadus (Taxation Act), consolidated text in force from 26.10.2026, § 84 | https://www.riigiteataja.ee/et/akt/116102026010 | 2026-10-30 |
| Kogumispensionide seadus (Funded Pensions Act), consolidated text in force 01.06.2025 to 31.10.2026, § 9 | https://www.riigiteataja.ee/et/akt/103122024016 | 2026-10-30 |
| Kogumispensionide seadus (Funded Pensions Act), consolidated text in force from 31.10.2026, §§ 9, 17^2 (same § 9 wording) | https://www.riigiteataja.ee/et/akt/116102026006 | 2026-10-30 |
| Ettevõtlustulu lihtsustatud maksustamise seadus (Simplified Business Income Taxation Act), consolidated text in force from 01.01.2026, §§ 2, 4, 8 | https://www.riigiteataja.ee/et/akt/118122025016 | 2026-10-30 |
| Töötuskindlustuse seadus (Unemployment Insurance Act), consolidated text in force 01.10.2026 to 31.12.2026, § 3 | https://www.riigiteataja.ee/et/akt/130062026040 | 2026-10-30 |
| EMTA, tax rates (2024 to 2026) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates | 2026-10-30 |
| EMTA, entrepreneur account | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account | 2026-10-30 |
| EMTA, social tax of self-employed persons | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax | 2026-10-30 |
| EMTA, calculation of basic exemption | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption | 2026-10-30 |
| EMTA, about the payment of labour taxes (salary and dividends) | https://www.emta.ee/en/business-client/e-services-training-courses/advice/about-payment-labour-taxes | 2026-10-30 |
| Ministry of Finance, law changes in force in 2026 | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused | 2026-10-30 |
| Ministry of Finance, Riigikogu approved the security tax changes (18.06.2025) | https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused | 2026-10-30 |

Not yet confirmed: the EMTA salary-and-dividend guidance carries no 2026 date; its examples use older minimum-wage figures, so only its principles are relied on here.

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
