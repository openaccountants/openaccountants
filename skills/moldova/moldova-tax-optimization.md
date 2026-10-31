---
name: moldova-tax-optimization
description: Use this skill whenever asked about reducing tax in Moldova, tax planning, or legal strategies to minimise tax for a self-employed person, IT business, or small company in Moldova, tax year 2026. Trigger on phrases like "reduce tax Moldova", "Moldova IT Park", "7% tax IT", "small business 4% Moldova", "turnover tax Moldova", "sole proprietor vs SRL", "Moldova dividends 6%", "independent entrepreneur Moldova", "defer corporate tax until dividends Moldova", "save tax Moldova", "tax planning Moldova". This skill covers the IT park 7%-of-revenue single tax, the 4% small-company regime, the independent entrepreneur 15% single tax, the standard 12% system, dividend extraction at 6%, the option to pay 2023 to 2026 corporate tax only when dividends are paid, and the eligibility and anti-avoidance red lines. ALWAYS read this skill before advising on any Moldovan tax optimisation. Computations sit in md-corporate-income-tax, moldova-income-tax, moldova-social-contributions and moldova-payroll.
version: 0.2
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova Tax Optimization

## Moldova Tax Optimization Skill v0.2

**Tier 2. Sources: the Fiscal Code of the Republic of Moldova (Codul fiscal nr. 1163/1997, consolidated to Law LP235 of 2 October 2026), read on 30 October 2026 and listed in Sources below. Figures must agree with `md-corporate-income-tax.md`, `moldova-income-tax.md` and `moldova-social-contributions.md`; those skills win if they differ. No Moldovan tax adviser has signed this off. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Moldova |
| Currency | MDL (leu) |
| Headline levers | **IT park 7% of sales revenue**; 4% small-company regime; independent entrepreneur 15% single tax; 6% on dividends; corporate tax on 2023 to 2026 profits deferred until dividends are paid |
| Standard income tax, individuals and companies | **12%** (Fiscal Code art. 15(a), (b)) |
| Dividends to resident individuals | **6%** withheld (art. 90^1(3^1)) |
| VAT registration threshold | over **MDL 1.7 million** in any 12 consecutive months from 1 March 2026; MDL 1.5 million before that date (art. 112(1); Law LP12/2026) |
| Anti-avoidance | IT park 70% eligible-revenue test; 4% regime closed to VAT payers, consultancy firms and owners of more than three small companies |

> **Moldova's headline is the IT park single tax:** 7% of monthly sales revenue, with a floor per employee, replaces income tax on profit and on salaries, employer social contributions, employees' health insurance premiums, local taxes, property tax and the road-use tax (Fiscal Code arts. 370, 372). For an IT business with a large payroll, this is usually the biggest lever.

## Section 2 -- IT Park (7% of sales revenue)

**IT Park (7% of sales revenue)**

| Feature | Detail |
| --- | --- |
| Tax | **7% of sales revenue** booked monthly, but at least **30% of the forecast average monthly wage per employee** each month, which is **MDL 5,220** per employee in 2026 (30% of the MDL 17,400 forecast wage, Government Decision 773/2025) (Fiscal Code arts. 369(1), (2), 370(1), (2)) |
| What it replaces | Income tax on business profit; income tax on salaries; employer social contributions; employees' health insurance premiums; local taxes; property tax; road-use tax for Moldovan-registered vehicles (art. 372(1)) |
| What it does not replace | Tax withheld under arts. 88(5), 89, 90, 90^1 and 91 (for example 6% on dividends and 12% on payments to non-residents), contributions on non-salary payments to individuals, VAT, excise and other road taxes (art. 372(2)) |
| Who | Legal entities and individuals registered as entrepreneurs who meet the conditions of the IT parks law (Law 77/2016) (art. 368(1)) |
| Eligibility test | **70% or more** of sales revenue from activities permitted under art. 8 of Law 77/2016, measured monthly on a cumulative basis; up to 2 months below 70% are allowed if the year as a whole reaches 70% (art. 368(2), (3)) |
| Permitted activities | Listed by CAEM code in Law 77/2016 art. 8: custom software (62.01), computer games publishing (58.21), other software publishing (58.29), IT consultancy (62.02), computer facilities management (62.03), other IT services (62.09), data processing and hosting (63.11), web portals (63.12), plus narrowly limited computer training, research and development, electronic components, specialised design, film and video post-production and game audio work |
| How long | Each park runs for a term set by Government decision, at most 20 years (Law 77/2016 art. 9(2)); a resident's contract runs at least 4 years and not past the park's term (art. 7(2)) |
| Filing and payment | Monthly return and payment by the 25th of the following month (art. 373(1), (2)) |
| Best for | Software and IT service firms with significant payroll, because the 7% also covers payroll taxes |

IT park residents cannot use the corporate tax deferral to the dividend date (art. 87(1^1)). Detail of the computation: [md-corporate-income-tax](md-corporate-income-tax.md).

## Section 3 -- 4% Small-Company Regime

- **4% small-company regime**: a company not registered for VAT may pay 4% of the income in its financial accounts instead of 12% on profit (Fiscal Code arts. 54^1, 54^2, 54^3). No profit computation; good for low-expense businesses below the VAT threshold.
- **Who is excluded**: farms, individual entrepreneurs, and companies where more than 60% of last year's sales came from business and management consultancy (CAEM 70.22) (art. 54^1(1)). A company with VAT-exempt supplies without deduction right above MDL 1.7 million uses the standard regime (art. 54^1(3^1)).
- **Choosing it**: record the choice in the accounting policy by 25 April, or for a new company by the 25th of the month after the quarter of registration (art. 54^1(3)).
- **When it ends**: from the date the company registers for VAT (art. 54^1(4)). Registration is compulsory once supplies pass MDL 1.7 million in any 12 consecutive months (art. 112(1), in force from 1 March 2026; MDL 1.5 million before that date, Law LP12/2026).
- **Payments**: quarterly by the 25th of the month after the quarter; annual report by 25 March (art. 54^4(2), (3)). No quarterly instalments under art. 84 and no 12% advance on interim dividends (arts. 84(4), 80^1(4)).

## Section 4 -- Standard System & Extraction (SRL / ÎI)

**Standard System & Extraction (SRL / ÎI)**

| Item | Rate |
| --- | --- |
| Corporate income tax (SRL) | **12%** of taxable income (art. 15(b)) |
| Individual entrepreneur (ÎI) | **12%** of annual taxable income (art. 15(a)) |
| Dividends to resident individuals | **6%** withheld (art. 90^1(3^1)) |
| Dividends between Moldovan companies | not taxable (art. 20 lit. z19)) |
| Independent entrepreneur (services only) | **15%** single tax on service income up to MDL 1,200,000 a year, **35%** above; includes income tax, social and health contributions and local taxes (arts. 69^20, 69^25) |
| Independent retail activity (individual, no excise goods) | **1%** of income, at least MDL 3,000 (arts. 69^6, 69^11(1)) |

- **Dividend vs salary extraction**: the owner can take profit as dividends at 6% instead of salary taxed at 12% plus contributions. Model salary against dividend with the contribution effect from [moldova-social-contributions](moldova-social-contributions.md) and [moldova-payroll](moldova-payroll.md).
- **Defer corporate tax until dividends are paid**: a company with at most 249 staff and turnover or total assets up to MDL 100 million may pay the 12% tax on 2023 to 2026 profits only when it distributes them, in proportion to the dividend paid over pre-tax profit (art. 87(1^1)). Profit kept in the company stays untaxed until then, and there are no quarterly instalments for those years (art. 84(6)). Not open to IT park residents, the 4% regime, individual entrepreneurs, farms, free zone residents, financial and insurance companies, and large trade companies. Worked example: [md-corporate-income-tax](md-corporate-income-tax.md).
- **Interim dividends**: on the standard regime, paying dividends during the year triggers an advance of 12% of the current year's profit from which they are paid, due by the 25th of the following month (art. 80^1(1), (1^1)).
- **Donations**: charitable and sponsorship donations to eligible recipients are deductible up to 5% of taxable income (art. 36(1), (2)).
- **Losses**: tax losses are carried forward and spread over the next five years (art. 32(1)).

## Section 5 -- Red Lines (do not cross)

- **IT park 70% test**: at least 70% of sales revenue must come from activities permitted under Law 77/2016; non-IT income placed in an IT park entity is a misuse (art. 368(2), (3)). AUDIT FLASH POINT.
- **4% regime conditions**: not for VAT-registered companies, consultancy companies above the 60% test, or a shareholder with more than 25% in more than three small companies, who must move the extra companies to the standard regime (art. 54^1(1), (3^2), (4)).
- **Independent entrepreneur scope**: the 15% regime covers service activities only (art. 69^20).
- **Under-declaration**: understating tax in a return costs 20% to 30% of the amount, and evasion 80% to 100% (art. 261(4), (5)). Understating income while using the dividend-date deferral costs MDL 1,000 to 10,000 (art. 260(6)).
- **Non-eligible income routing**: do not route non-eligible income through the 4% or 7% regimes.

## PROHIBITIONS

- **Non-IT revenue in IT Park**: NEVER place non-IT revenue in the IT park 7% regime to dodge tax (70% eligibility test).
- **4% regime for VAT-registered business**: NEVER present the 4% regime for a VAT-registered business; it is for companies not registered for VAT.
- **Single-client work as safe self-employment**: NEVER present single-client work as safe self-employment.
- **Deferral as a permanent saving**: NEVER present the art. 87(1^1) deferral as a tax saving; the tax is paid when profits are distributed.
- **Contradicting rate skills**: NEVER contradict the rates in `md-corporate-income-tax.md`, `moldova-income-tax.md` or `moldova-social-contributions.md`.
- **Unconfirmed figures as confirmed**: NEVER present items on the "Not yet confirmed" line as confirmed, nor optimisation as definitive advice; route to a licensed Moldovan tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Moldova) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Codul fiscal nr. 1163/1997, consolidated to LP235/2026 (in force 30.10.2026): arts. 15, 20 lit. z19), 32, 36, 54^1 to 54^4, 69^6, 69^11, 69^20, 69^25, 80^1, 84, 87, 90^1, 112, 260, 261, 368 to 373 | https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro | 2026-10-30 |
| Legea nr. 77/2016 cu privire la parcurile pentru tehnologia informației (to LP125/2024): arts. 7(2), 8, 9(2) | https://www.legis.md/cautare/getResults?doc_id=143443&lang=ro | 2026-10-30 |
| Government Decision 773 of 17 December 2025: forecast average monthly wage for 2026, MDL 17,400 | https://www.legis.md/cautare/getResults?doc_id=152066&lang=ro | 2026-10-30 |
| Law LP12 of 19 February 2026 amending Fiscal Code art. 112 (MDL 1.5 million to MDL 1.7 million, in force 1 March 2026) | https://www.legis.md/cautare/getResults?doc_id=153159&lang=ro | 2026-10-30 |

Not yet confirmed: the end date of the Moldova IT Park's own term (set by Government decision, not read); the date from which the MDL 1.7 million figure in art. 54^1(3^1) applies (the text in force on 30 December 2025 said MDL 1.2 million); the old "savings of 20% to 50% of the total tax burden" claim for IT park residents (no official source); whether single-client work by an ÎI or independent entrepreneur is reclassified as employment (no Fiscal Code rule found); 2026 salary contribution rates for the salary-vs-dividend comparison (see the sibling skills).

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
