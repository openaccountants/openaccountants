---
name: estonia-tax-optimization
description: "Lawful Estonia planning for tax year 2026: compare FIE, OÜ and entrepreneur-account cash flows, profit deferral, actual-work remuneration, current rates and verified allowances. Preserves anti-avoidance refusals and routes detailed computations to the country tax skills. Company entertainment conditions, foreign participation exemption and pension-election timing are held under Sources, not current instructions. Use for FIE versus OÜ, entrepreneur account, salary versus dividend and Estonian tax planning."
version: 0.3
jurisdiction: EE
tax_year: 2026
last_updated: 2026-11-16
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: decision
domain: tax-optimization
---

# Estonia Tax Optimization

## Estonia Tax Optimization Skill v0.3

**Tier 2. Figures for 2026 from the Income Tax Act (tulumaksuseadus, TuMS), the Social Tax Act (SMS), the Funded Pensions Act (KoPS), the Simplified Business Income Taxation Act and EMTA pages, listed under Sources. They agree with `estonia-income-tax`, `ee-corporate-income-tax`, `estonia-social-contributions` and `estonia-payroll`; if they ever differ, those skills win. Not signed off by an Estonian tax adviser. Every suggestion needs review by a credentialed professional; aggressive positions are never advised.**

## Scope

Choose between the existing FIE, OÜ and entrepreneur-account options for 2026, with the conditions and anti-avoidance limits below. This does not file a return or approve a structure.

## Ask the client first

- What work is performed, where, by whom, and through which existing registration?
- What are receipts, documented expenses and reinvestment needs, and who are the customers?
- What active owner work needs reasonable remuneration, and what payroll/pension cover already exists?
- What residence, related parties, shareholder holdings, received dividends and actual substance are involved?
- Which allowances have already been used, and what are the exact payment and reporting dates?

## The method, step by step

1. Compare the entity options below using receipts, costs, liability and reinvestment, not a headline tax rate.
2. Price actual work as salary or board remuneration before considering distributions. Keep the anti-avoidance refusals below.
3. Test every relief's eligibility and remaining allowance, then use the relevant domain Guide for its computation and filing.
4. Work both cash-out alternatives and document the non-tax consequences. A lower immediate cash tax alone does not choose the structure.
5. Refer unresolved statutory/source conditions listed below before relying on a relief.

### Section 1 -- Quick Reference

**Quick Reference**

| Field | Value | Official source |
| --- | --- |---|
| Country | Republic of Estonia | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Currency | EUR | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Personal income tax | Flat **22%** in 2025 and 2026. The 24% rate enacted for 2026 was cancelled before it took effect (TuMS § 4(1); Ministry of Finance) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Security tax | **None in 2026.** It was dropped for company profit and personal income before 2026 (Ministry of Finance, 18.06.2025) | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused |
| Company tax (OÜ) | **0% on retained profit**; **22%** on distribution, charged as 22/78 of the net amount (TuMS § 4(1), (1^1), § 50(1)). The reduced 14/86 rate on regular dividends was **abolished from 1 January 2025** (TuMS § 4(4) repealed; EMTA) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends |
| Dividend in the owner's hands | Not taxable income of the individual; the company has paid (TuMS § 12(2)) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends |
| Social tax | 33% on employment pay and board fees; the detailed pension/health allocation is held pending its operative source (SMS § 7(1), § 10(2)) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Basic exemption 2026 | EUR 8,400 a year, flat, no income taper; EUR 9,312 from the year of pensionable age (TuMS § 23(1), § 23^5(1)) | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption |
| Key optimisation levers | Entity choice and profit deferral (OÜ 0% on retained profit); salary-dividend mix; entrepreneur account for small income; tax-free limits; II and III pillar; holding exemptions only after the held conditions are resolved | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Anti-avoidance | EMTA treats a dividend that replaces pay for active work as pay; substance over form (MKS § 84); substance needed for holding structures | https://www.emta.ee/en/business-client/e-services-training-courses/advice/about-payment-labour-taxes |

- **Personal income tax.** Flat 22% (2025 and 2026).
- **Company tax (OÜ).** 0% on retained profit; 22% on distribution (22/78 of the net amount). The reduced 14% rate on regular dividends was abolished from 1 January 2025.
- **Social tax.** 33% on employment pay and board fees (funds pension and health cover).

> **The single biggest Estonian lever is the OÜ deferral:** profit kept inside an OÜ is taxed at **0%** until it is distributed. Profit reinvested in the business does not trigger the 22% while it stays there. This is lawful deferral, not avoidance, and not an exemption.

### Section 2 -- Entity Choice & Profit Deferral (the core decision)

**Entity Choice & Profit Deferral**

| Structure | Best when | Tax treatment (2026) | Official source |
| --- | --- | --- |---|
| **OÜ** (private limited company) | Profit reinvested or retained; wants limited liability; building value | **0% on retained profit**; 22% (22/78) only when profit is distributed or treated as distributed; owner-manager can take a salary or board fee. Details: `ee-corporate-income-tax` | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends |
| **FIE** (sole proprietor) | Small, simple, wants income in own hands now | Business income taxed every year: 22% income tax on the annual return, and 33% social tax on business income after allowed deductions, a confirmed maximum EUR 36,867.60 a year; annual-floor and boundary-subtraction conditions are held in estonia-income-tax (SMS § 2(5), § 7(1); EMTA). A qualifying FIE special account can defer tax on eligible retained business receipts; this is not an OÜ profit-distribution regime. Unlimited personal liability. Details: `estonia-income-tax`, `estonia-social-contributions` | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax |
| **Ettevõtluskonto** (entrepreneur account) | Small or side income from selling services and goods, few expenses, customers mainly private individuals | The bank holds back **20%** of every receipt (**22%, 24% or 26%** if in the II pillar at 2%, 4% or 6%); the 20% is 22/55 income tax and 33/55 social tax. No bookkeeping and no deductions. Above **EUR 40,000** of receipts in a calendar year the person must register as an FIE or company and for VAT. The interaction with existing FIE/VAT registration is held pending its operative source; do not recommend the account without resolving that eligibility question. A company that pays for a service into an entrepreneur account pays 22/78 company income tax on the payment on top (EMTA's example: a EUR 100 service costs the company EUR 128.20). EMTA says only LHV Pank offers the account (Simplified Business Income Taxation Act § 2(2), § 4, § 8(2); EMTA). Details: `estonia-income-tax` | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account |

- **The deferral play.** An OÜ that keeps profit to fund hiring, equipment or expansion pays no company income tax at that stage. Tax (22/78) arises only on distribution. Compare it with the FIE special-account rules before choosing: eligible timely deposits can also defer FIE income, subject to statutory restrictions. Liability, administration, deductible costs and actual remuneration also matter; reinvestment alone does not establish that an OÜ is better. Entity choice detail: `ee-company-formation`.
- **The entrepreneur account test.** It suits a person whose costs are low, because the 20% is charged on receipts, not on profit, and nothing can be deducted.

### Section 3 -- Salary vs Dividend (OÜ owner-managers)

**Salary vs Dividend**

| Route | Cost | Notes | Official source |
| --- | --- | --- |---|
| **Board-member fee or employee salary** | 33% social tax on top; 22% income tax withheld after the II pillar contribution, any basic exemption and, for employee salary, the employee’s 1.6% unemployment premium; employee salary also carries an employer premium of 0.8%. Board-member fees carry neither unemployment premium | Builds state pension and health cover through social tax (SMS § 10(2)). Unemployment premiums cover employees, officials and people working under service contracts (Unemployment Insurance Act § 3(1)); a board-member fee is not on that list | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums |
| **Dividend** | 22/78 company income tax; **no social tax** | No pension or health cover built. Not taxed again in the owner's hands (TuMS § 12(2)) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends |

- **The optimisation.** Pay a reasonable market salary or board fee for the work actually done (it keeps health insurance and builds pension rights), then distribute the rest as dividends.

> **AUDIT FLASH POINT.** EMTA's guidance says: "A shareholder is entitled to dividends but the dividend may not replace salary." Dividends "may be deemed salary income if a management board member is not paid remuneration ... at all or these are paid in very small amounts", and dividends paid frequently, for example monthly, are likely to be seen as replacing that period's pay. If pay is at or near the usual level in the industry, EMTA sees no tax risk (EMTA, About the payment of labour taxes). The legal base is substance over form (MKS § 84). Set the salary defensibly and document it. Never advise zero-salary-all-dividend for an active owner.

### Section 4 -- Deductions & Expenses (Estonia works differently)

Estonia has **no annual profit-tax computation** for a company, so "deductible expenses" do not reduce a yearly tax bill the way they do elsewhere. Genuine business expenses are simply **not taxed**. Spending that is not business-related, gifts, donations, entertainment and fringe benefits are taxed at 22/78 in the month they are paid, unless a tax-free limit covers them (TuMS §§ 48 to 51). Details: `ee-corporate-income-tax`.

**Deductions & Expenses**

| Item | Treatment (2026) | Official source |
| --- | --- |---|
| Genuine business expenses | Not taxed if wholly business-related and documented | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Fringe benefits (private use of company assets, perks to staff and board) | Taxed: 22/78 income tax, plus 33% social tax on the benefit and on that income tax, both paid by the company (TuMS § 48(1), § 4(1^1); SMS § 2(1) point 7; `estonia-payroll`). Keep business and private use apart | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/fringe-benefits |
| Company car available for private use | Benefit of EUR 1.96 per kW a month; EUR 1.47 per kW if the car is older than five years (TuMS § 48(8)) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting |
| Employee health costs (sport, exercise, health services) | Tax-free up to EUR 400 per employee a year, if offered to all employees (TuMS § 48(5^5)) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Entertaining guests and business partners | Held pending the operative allowance conditions; do not compute a tax-free limit from the archived example | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Advertising gifts | Income-tax exemption up to EUR 21 per item, excluding VAT (TuMS § 49(1)); a VAT-registered giver separately accounts for output VAT on free promotional goods worth more than EUR 10 excluding VAT where their input VAT was deducted | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/gifts-and-donations |
| Gifts and donations to listed associations | Tax-free up to **3%** of the year's payments subject to personal social tax, **or 10%** of the profit of the last financial year completed as at 1 January of the donation calendar year; the company picks one limit for the annual summary (TuMS § 49(2), (3)) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/gifts-and-donations |

### Section 5 -- Reliefs & Personal Allowances

**Reliefs & Personal Allowances**

| Relief | Detail | Official source |
| --- | --- |---|
| **Basic exemption (maksuvaba tulu)** | **2026: EUR 8,400 a year (EUR 700 a month), the same at every income level** (TuMS § 23(1)). 2025: up to EUR 7,848, tapered between income of EUR 14,400 and EUR 25,200 and nil above (EMTA, calculation of basic exemption until the end of 2025) | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption |
| **Pensionable-age exemption** | EUR 9,312 a year (EUR 776 a month) from the year the person reaches pensionable age (TuMS § 23^5(1)) | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption |
| **II-pillar funded pension** | Current contribution rates are 2%, 4% or 6%. The election deadline and minimum duration are held pending the operative pension rules | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| **III-pillar supplementary pension** | Deductible up to **15%** of the year's income taxable in Estonia, excluding entrepreneur-account and Estonia-exempt foreign employment/dividend income, maximum **EUR 6,000**, only within the part of those same limits not used by employer contributions (TuMS § 28(2)) | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/contributions-supplementary-funded-pension |
| **Training costs and donations** | Together up to **EUR 1,200** a year, and not more than 50% of the person's Estonian taxable income (TuMS §§ 26, 27, 28^2(1)) | https://fin.ee/riigi-rahandus-ja-maksud/maksu-ja-tollipoliitika/maksud |

- **Basic exemption.** 2026: EUR 8,400 a year, flat. The 2025 taper is gone.
- **II-pillar rate choice.** A higher rate raises retirement saving and cuts taxable pay, at the cost of take-home pay now.

> The 2025 taper created a "tax hump" between EUR 14,400 and EUR 25,200 of income, where the effective marginal rate was higher; timing income across years near that band could help. **From 2026 there is no taper, so this lever no longer exists** for 2026 income. It still matters for checking a 2025 return.

### Section 6 -- Holding / Participation Exemption

Refer to ee-corporate-income-tax and an Estonian adviser for a proposed holding structure. The detailed exemption and no-minimum-holding-period claims are preserved below but held pending a readable operative source. Do not implement them from this planning summary.

### Section 7 -- Red Lines (do not cross)

- **Market-salary expectation.** Active owner-managers must take a reasonable salary or board fee; all-dividend-no-salary is a pattern EMTA reclassifies as pay.
- **Substance for holdings.** The participation exemption needs real economic substance.
- **Business vs private.** Private spending booked as business creates taxable fringe benefits or distributions, not deductions.
- **OÜ 0% is deferral, not exemption.** Never present the OÜ system as "no tax": 22/78 applies on distribution.

### PROHIBITIONS

- **Zero-salary-all-dividend advice.** NEVER advise an active owner-manager to take zero salary and only dividends to avoid social tax.
- **Describing the OÜ regime as tax-free.** NEVER describe Estonia's OÜ regime as tax-free. It is 0% on RETAINED profit only; distributions are taxed at 22% (22/78).
- **Abolished 14% reduced dividend rate.** NEVER assume the abolished 14/86 rate still applies (gone from 1 January 2025).
- **Cancelled 2026 rises.** NEVER use a 24% income tax rate or a security tax for 2026: both were cancelled before they took effect.
- **Substance-free holding company advice.** NEVER advise a substance-free holding company to exploit the participation exemption.
- **Contradicting related skills.** NEVER contradict the rates and exemptions in `estonia-income-tax`, `ee-corporate-income-tax`, `estonia-social-contributions` or `estonia-payroll`.
- **Presenting suggestions as definitive advice.** NEVER present optimisation suggestions as definitive advice. Always route to a licensed Estonian tax adviser.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Estonia) before acting upon.

## Worked cases

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

### Worked decision: entrepreneur account or ordinary FIE, low and material expenses

Assume a full-year resident below pensionable age, not in the II pillar, with only the stated business income, the full EUR 8,400 exemption available, EUR 40,000 receipts, no special-account deferral and no foreign or other VAT-registration trigger. Compare cash after actual business costs. At zero expenses, the account withholds EUR 8,000, leaving EUR 32,000; the ordinary FIE method leaves EUR 25,306.65. With EUR 20,000 of documented deductible costs, the account still withholds EUR 8,000 and leaves EUR 12,000, whereas the ordinary FIE method leaves EUR 13,577.32. Thus the immediate cash comparison changes with costs; it does not establish the best legal form. Both computed FIE social-tax amounts exceed four ordinary advances and remain below the confirmed annual cap; these are ordinary computations, not annual-minimum or maximum-subtraction cases. Any exception, boundary adjustment or additional registration trigger requires the domain Guide and resolution of its held conditions. [EMTA entrepreneur account](https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account); [EMTA FIE social tax](https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax); [EMTA basic exemption](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption).

```oa-check
name: Estonia entrepreneur account versus ordinary FIE, two expense levels, 2026
inputs:
  receipts: 40000
  low_cost: 0
  material_cost: 20000
steps:
  - account_tax: receipts * 0.20
  - account_cash_low: receipts - low_cost - account_tax
  - adjusted_low: (receipts - low_cost) / 1.33
  - social_low: adjusted_low * 0.33
  - tax_low: max(adjusted_low - 8400, 0) * 0.22
  - fie_cash_low: receipts - low_cost - social_low - tax_low
  - account_cash_material: receipts - material_cost - account_tax
  - adjusted_material: (receipts - material_cost) / 1.33
  - social_material: adjusted_material * 0.33
  - tax_material: max(adjusted_material - 8400, 0) * 0.22
  - fie_cash_material: receipts - material_cost - social_material - tax_material
expected:
  account_tax: 8000
  account_cash_low: 32000
  social_low: 9924.81
  tax_low: 4768.54
  fie_cash_low: 25306.65
  account_cash_material: 12000
  social_material: 4962.41
  tax_material: 1460.27
  fie_cash_material: 13577.32
```

## When to refuse or refer

Refuse the zero-salary/dividend substitution, substance-free holding structures and private-business mixing prohibited above. Refer any choice requiring unresolved residence, foreign tax, treaty or source conditions. The comparisons show tax mechanics, not permission to replace remuneration for work with dividends.

## Filing and payment

Use estonia-income-tax for form A/E and FIE advances, ee-corporate-income-tax for monthly distributions/TSD, and estonia-payroll for actual remuneration. Keep the route's registration and payment deadlines distinct. No election or relief is assumed made by reading a comparison.

## Completion checklist

- [ ] Both options compared with the client's actual costs and cash needs.
- [ ] Work/remuneration, social protection and anti-avoidance conditions documented.
- [ ] Relief conditions and prior allowance use checked.
- [ ] Relevant domain filing workflow loaded; unresolved source conditions held.

## Sources

Historical statutory rows retain their original recorded dates. The current full texts were not reopened on 16 November 2026; only the explicitly scoped 16 November authority-page rows are new reads.

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

| Read for 2026 PIT, company tax, exemption, pension rates and employee-health limit: EMTA tax rates | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates | 2026-11-16 |
| Read for active-work remuneration, substance and dividend substitution; historical example amounts not used: EMTA labour-tax guidance | https://www.emta.ee/en/business-client/e-services-training-courses/advice/about-payment-labour-taxes | 2026-11-16 |
| Read for FIE special-account deferral, eligible amounts, ten-working-day conditions and form E table 2: EMTA special account | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/special-account | 2026-11-16 |
| Read for entrepreneur-account rates, receipt basis, costs, client types and company payer example: EMTA entrepreneur account | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account | 2026-11-16 |
| Read for company distributions, old-rate transition and TSD annex 7/INF 1: EMTA taxation of dividends | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/taxation-dividends | 2026-11-16 |
| Read for promotional gifts EUR 21 and donation 3%/10% conditions, plus distinction from employee fringe benefits: EMTA gifts and donations | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/gifts-and-donations | 2026-11-16 |

| Read for general car fringe-benefit rates EUR 1.96/1.47 per kW and VAT-use conditions: EMTA passenger cars | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting | 2026-11-16 |
| Read for III-pillar income scope, deduction order and refund capacity: EMTA supplementary pension | https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/contributions-supplementary-funded-pension | 2026-11-16 |
| Read for unemployment insurance exclusions, including board fees and FIE: EMTA premiums | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/unemployment-insurance-premiums | 2026-11-16 |
| Read for fringe-benefit tax on the benefit plus income tax and TSD annex 4: EMTA fringe benefits | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/fringe-benefits | 2026-11-16 |

Not yet confirmed: the EMTA salary-and-dividend guidance carries no 2026 date; its examples use older minimum-wage figures, so only its principles are relied on here. Company-car rates are supported by the EMTA passenger-car chapter. The detailed 20/13 social-tax allocation, entrepreneur-account eligibility alongside FIE/VAT registration, and full operative statutory conditions for the company entertainment allowance, foreign participation exemption and pension elections could not be reopened in Riigi Teataja. Historical references remain for independent source review, not a claim of fresh verification; do not implement those positions until the operative conditions are confirmed.

### Held original detail, not instructions

The following original passages and example remain solely to preserve their topics for source completion. Their arithmetic is reproducible, but that does not establish eligibility. Do not apply these positions or the entertainment calculation until the missing operative conditions are read.

### Section 6 -- Holding / Participation Exemption

- **Participation exemption on dividends received.** An Estonian company that receives a dividend from a company in an EEA state or Switzerland that is liable to income tax there (not in a non-cooperative jurisdiction), and that held **at least 10%** of the shares, units or votes **at the time it received the dividend**, pays no income tax again when it passes that dividend on to its own shareholders. Dividends from other foreign companies qualify on the same 10% test only if tax was withheld on the dividend or the underlying profit was taxed (TuMS § 50(1^1) points 1 and 3). In both cases the exemption applies only if the company that paid the dividend could not deduct it from its own taxable profit (TuMS § 50(1^3)). This makes Estonia a workable EU holding location. Details: `ee-corporate-income-tax`.
- **No minimum holding period** is set in § 50(1^1): the test is the holding when the dividend is received.

**AUDIT FLASH POINT.** A holding structure must have genuine substance. A letterbox holding set up mainly for tax can be challenged: Estonian law taxes a transaction by its real economic substance where it was made to avoid tax (MKS § 84).

| Entertaining guests and business partners | Tax-free up to **EUR 50 a month**, plus **2%** of that month's payments subject to personal social tax if the company makes such payments; the excess is taxed at 22/78 (TuMS § 49(4)). Small for a solo OÜ, larger with a payroll | https://www.riigiteataja.ee/et/akt/109072026066 | Held original reference, not reopened on 2026-11-16 |

| **II-pillar funded pension** | 2% by default; the member may choose **4% or 6%**, which then holds for at least a calendar year (KoPS § 9). The contribution is deducted before income tax is withheld (TuMS § 42(6)). An application to change the rate that reaches the register by 30 November applies from 1 January of the next year (KoPS § 17^2(8)) | https://www.riigiteataja.ee/et/akt/109072026066 | Held original reference, not reopened on 2026-11-16 |

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


Held original allocation clause, not instructions: 33% on employment pay and board fees; it funds state pension (20 points) and health insurance (13 points) (SMS § 7(1), § 10(2))

Held original entrepreneur-account eligibility clause, not instructions: The holder cannot be VAT-registered or an FIE in the same or a similar activity.
