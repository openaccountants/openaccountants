---
name: azerbaijan-tax-optimization
description: Use this skill whenever asked about reducing tax in Azerbaijan, tax planning, or legal strategies to minimise tax for a small business or entrepreneur in Azerbaijan in tax year 2026. Trigger on phrases like "reduce tax Azerbaijan", "simplified tax 2%", "micro business Azerbaijan", "startup exemption", "Azerbaijan dividends 5%", "tech park Azerbaijan", "liberated territories tax", "Nakhchivan tax exemption", "save tax Azerbaijan", "tax planning Azerbaijan". This skill covers the 2% simplified turnover tax and its exclusions (including the 30% business-customer test), the 75% micro-business relief, the 3-year startup exemption, technology-park, industrial-park and territorial exemptions, dividend taxation and the deemed-dividend rule, and the anti-avoidance red lines. The computations themselves are out of scope (az-corporate-income-tax, azerbaijan-income-tax, azerbaijan-payroll, azerbaijan-social-contributions, azerbaijan-vat, azerbaijan-cross-border). ALWAYS read this skill before advising on any Azerbaijani tax optimisation.
version: 0.2
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Tax Optimization

## Azerbaijan Tax Optimization Skill v0.2

**Tier 2, checked against the law. Sources: the Tax Code of the Republic of Azerbaijan (consolidated text including Law 476-VIIQD of 30 September 2026, read on e-qanun.az on 31 October 2026), and the Small and Medium Business Development Agency (KOBİA) page on the startup certificate. Figures must agree with [azerbaijan-income-tax](azerbaijan-income-tax.md), [az-corporate-income-tax](az-corporate-income-tax.md), [azerbaijan-payroll](azerbaijan-payroll.md) and [azerbaijan-social-contributions](azerbaijan-social-contributions.md); where they differ, those skills win. Not signed off by an Azerbaijani tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Azerbaijan |
| Currency | AZN (manat) |
| Headline levers | **2% simplified turnover tax**; 75% micro-business relief; 3-year startup exemption; technology-park, industrial-park and territorial exemptions |
| Ordinary rates | Company profit tax **20%**; individual entrepreneur profit **20%** |
| Simplified tax | **2% of gross receipts** (taxable operations ≤ AZN 200,000 in any rolling 12 months, not VAT-registered, no exclusion); catering above AZN 200,000: **8%**, and **6%** on cashless POS receipts for services to the public from 1 Jan 2026 to 31 Dec 2028 |
| Dividends | **5%** withheld at source; not taxed again in the recipient's hands |
| Anti-avoidance | Eligibility exclusions, the 30% business-customer test, deemed dividends, substance for park and territorial reliefs |

> **Azerbaijan's headline is the 2% simplified tax**, uniform across the country. It is not open to every small business: a business that mainly invoices other registered taxpayers, wholesales, rents out property, earns royalties or needs a licence is excluded (Tax Code arts. 218.5, 218.6).

## Section 2 -- Simplified Tax (2% of turnover)

- **Simplified tax rate**: 2% of gross receipts from goods, work and services plus non-sales income, for a business not registered for VAT whose taxable operations are AZN 200,000 or less in every month of any rolling 12-month period _(Tax Code arts. 218.1.1, 219.1, 220.1)_.
- **Threshold weighting**: cashless POS-terminal receipts from retail trade and from services to persons not registered with the tax authority count at 0.5 towards the AZN 200,000 test _(art. 218.1-1)_.
- **Catering above AZN 200,000**: catering businesses above the threshold pay simplified tax at 8%; the base from cashless POS receipts for services to the public is taxed at 6% from 1 January 2026 for 3 years. The POS terminal must be integrated with the cash register _(arts. 218.1.2, 220.1-1)_.
- **What it replaces**: a company paying simplified tax is not liable for VAT or profit tax; an individual entrepreneur is not liable for income tax or VAT _(art. 219.5)_. Property tax is not replaced: Law 454-VQD of 16 December 2016 struck "and property tax" from art. 219.5, so a simplified-tax company still pays property tax on its assets.
- **No expense deduction under simplified tax**: tax is on gross receipts, so it suits a business whose real margin is above 10% (2% of turnover equals 20% profit tax at a 10% margin). Above AZN 200,000, or once VAT-registered, the profit-tax system applies.
- **Who is excluded** _(art. 218.5)_: producers of excisable or compulsorily labelled goods; credit institutions, insurers, investment funds and managers, licensed securities firms, pawnshops; non-state pension funds; persons earning income from renting out property or from royalties; natural monopolies; persons whose fixed assets had a residual value above AZN 1,000,000 at the start of the year; public legal entities; producers with more than 10 employees on average in a quarter; wholesale traders; persons doing work or services other than for persons not registered as taxpayers (the public); sellers of gold, jewellery, diamonds and furs; and licensed activities (compulsory-insurance agents and the listed exceptions aside).
- **The 30% test** _(arts. 218.6, 218.7)_: a retailer keeps the regime while e-invoiced wholesale sales are no more than 30% of its total trade in the quarter. A business serving the public keeps the regime while e-invoiced work for companies and registered individuals (including invoiced services to non-resident businesses) is no more than 30% of its total services in the quarter. Above 30%, the right ends from the 1st of the month after that quarter.
- **Election and filing**: elect, or opt out, by 20 April each year; the choice holds to the year end; a new business uses the method in its registration application _(art. 218.2)_. Returns and payment quarterly, by the 20th of the month after the quarter _(arts. 221.2, 221.3)_.
- **Dividends from a small company**: dividends paid to the individual founders of a resident company that keeps income and expense records, is not VAT-registered and has operations up to AZN 200,000 in any rolling 12 months are exempt from income tax _(art. 102.1.22-1)_ and from simplified tax _(art. 218-1.1.4)_.
- **Micro entrepreneur social credit**: an individual micro entrepreneur on simplified tax deducts 25% of the compulsory social insurance paid for themselves in the quarter from that quarter's simplified tax (not more than the tax), from 1 January 2024 for 3 years _(art. 221.1-1)_.
- **Standard rates** (the old research gap is closed): profit tax 20% for companies and permanent establishments _(art. 105.1)_; 20% on an individual entrepreneur's taxable profit _(art. 101.3)_. There is no "5% of net profit" micro regime; the micro relief is a 75% exemption with conditions (Section 3), which is not an unconditional 5% rate for every small company.

### Worked example: simplified tax against profit tax with micro relief

A non-VAT retail company has 150,000 of receipts and 120,000 of deductible costs. It has no exclusion and stays under AZN 200,000. On simplified tax it pays 150,000 × 2% = 3,000. On profit tax its profit is 30,000 and tax is 6,000. If it qualifies for the micro relief (micro size, average of at least 3 employees, no social insurance debt), 75% of the profit is exempt, so tax is 30,000 × 25% × 20% = 1,500. Here the micro relief beats the simplified tax; without it, the simplified tax wins.

```oa-check
name: AZ simplified vs profit tax with micro relief 2026
inputs:
  receipts: 150000
  costs: 120000
steps:
  - simplified_tax: receipts * 0.02
  - profit: receipts - costs
  - profit_tax: profit * 0.20
  - micro_taxable: profit * 0.25
  - micro_profit_tax: micro_taxable * 0.20
expected:
  simplified_tax: 3000
  profit: 30000
  profit_tax: 6000
  micro_profit_tax: 1500
```

## Section 3 -- Startup, Micro & Regional Incentives

**Startup, Micro & Regional Incentives**

| Incentive | Detail | Source |
| --- | --- | --- |
| Micro business relief | 75% of a micro company's (or micro individual entrepreneur's) business profit is exempt if the average monthly number of employees in the year is at least 3 and there is no compulsory social insurance debt. Average = sum of monthly headcounts ÷ 12. When the business grows out of micro size, a credit of 75% of the profit tax paid in the previous 3 micro years is given. Not available for income from sham (goodsless) transactions. Micro size follows the Cabinet size criteria: see [az-corporate-income-tax](az-corporate-income-tax.md). | Tax Code arts. 106.1.20, 102.1.30 |
| Listed small services | 75% of income is exempt for individuals with listed activities (software development, design, translation, advertising, legal, audit, accounting, financial advice, tour guiding, service exports and others) earning up to AZN 45,000 a year from them (revenue, before expenses). Lost if a former employee starts the same activity as an entrepreneur and supplies the same services to the former employer within one year. A person who also has other activities qualifies only if the listed activities give at least 50% of annual total income. Detail: [azerbaijan-income-tax](azerbaijan-income-tax.md). | Tax Code art. 102.1.30-1, 102.9 |
| Startup certificate | A micro or small startup holding a "Startap" certificate pays no profit tax (company) or income tax (individual entrepreneur) on profit from innovation activity for 3 years from the certificate date. A startup is a business based on an innovative initiative that meets the set criteria and holds the certificate; innovation activity means creating new or improved goods, work, services or processes from research and development. KOBİA issues the certificate, after its Expert Council's opinion, only to micro or small enterprises registered as taxpayers; where the applicant's founder is a medium or large enterprise, that founder's share may not exceed 49%. | Tax Code arts. 106.1.23, 102.1.31, 13.2.77, 13.2.80; KOBİA startup certificate page |
| Liberated territories | Residents of the liberated territories are exempt from profit (income), property, land and simplified tax for 10 years from 1 January 2023; their shareholders' dividends are exempt for the same period. Financial services, road freight and budget-funded contracts by outside contractors are excluded. Conditions by activity: production counts only for a taxpayer registered and producing there; wholesale, construction and business services count only for supplies to liberated-territory residents (supplies outside or exports lose the exemption); tourism, retail, catering and other public services count when registered and operating there. A resident doing the same activity elsewhere in Azerbaijan loses the exemption; other activities elsewhere need separate income and expense records. | Tax Code arts. 226.2, 226.3, 227.1, 227.3, 227.4 |
| Nakhchivan | The same profit, property, land, simplified tax and dividend exemptions apply to Nakhchivan residents (registered there or centrally and operating directly in Nakhchivan) for 10 years from 1 January 2026, under the same art. 226.3 and 227.4 conditions. | Tax Code art. 226.4 |
| Industrial and technology parks | A legal entity resident in an industrial or technology park is exempt on income from its park activity for 10 years from the reporting year of registration (individual entrepreneurs: art. 102.1.21). The exemption also covers technology-park residents doing system integration and software development outside the park. Dividends paid by those off-park technology-park firms are exempt for 10 years from the certificate year. Property and land in the park are exempt for 10 years (also for the off-park technology-park firms). A park resident is a person holding the park resident registration certificate issued under the rules set by the executive authority and operating in the park (a technology-park resident: in or outside the park). | Tax Code arts. 13.2.52, 13.2.53, 106.1.13, 106.1.13-1, 102.1.21, 199.7, 207.3 |
| Industrial-park residents in set activities | Profit from the specified activity of a resident of a park created by the designated body is exempt for 6 years from 1 January 2025. | Tax Code art. 106.1.13-2 |
| Technology-park specialists | Specialists employed in system integration and software work by an off-park technology-park resident pay 5% income tax on monthly employment income for 7 years from 1 January 2026. Detail: [azerbaijan-payroll](azerbaijan-payroll.md). | Tax Code art. 101.7.2 |
| SME clusters | Profit of an SME cluster company is exempt for 7 years from entry in the cluster register. | Tax Code art. 106.1.21 |
| Employer contribution subsidy | A state reimbursement of part of the employer's social insurance applies only to employers in the liberated territories and qualifying Nakhchivan producers, not to every private employer. Schedule and conditions: [azerbaijan-social-contributions](azerbaijan-social-contributions.md). | Social Insurance Law art. 14-1 (via that skill) |

Law 476-VIIQD of 30 September 2026 changes arts. 101.7, 102.1.21, 102.1.31, 106.1.13, 106.1.13-1 and 106.1.23 from 1 January 2027. Those changes are not applied here.

## Section 4 -- Dividends & Extraction

- **Dividend withholding tax**: 5% withheld at source on dividends paid by a resident company _(Tax Code art. 122.1)_. Once withheld, the dividend is not taxed again in the hands of the individual or company that receives it, and is not taxed again when paid on as a dividend _(art. 122.2)_.
- **Deemed dividends**: company assets or cash passed to a founder for purposes outside the business (other than loans to the founder or repayment of the founder's loans), and payment of a founder's debts to others, are treated as dividends and taxed at 5% at source _(art. 122.4)_.
- **Exempt routes**: dividends from a qualifying small company to individual founders (art. 102.1.22-1); dividends of liberated-territory and Nakhchivan residents (arts. 227.3, 226.4); dividends paid by off-park technology-park software firms for 10 years (art. 106.1.13-1).

A company paying 5% on dividends, or a technology-park company with the profit and dividend exemptions, can be highly efficient for IT and software founders, provided the activity, registration certificate and substance tests are met.

## Section 5 -- Red Lines (do not cross)

- **Eligibility red line**: the 2% simplified tax requires taxable operations of AZN 200,000 or less, non-VAT status and no art. 218.5 exclusion; a business mainly invoicing registered customers fails the 30% test. The startup exemption requires the certificate and profit from innovation activity. AUDIT FLASH POINT: misusing the certificates or regimes is challengeable.
- **Substance requirement**: park and territorial exemptions require registration as a resident and real activity there (for the liberated territories and Nakhchivan, tax registration there or centrally and activity carried out directly there, arts. 226.2, 226.4, with the activity conditions in art. 227.4).
- **No business splitting**: do not split a business to stay under AZN 200,000 without substance.
- **No goodsless transactions**: the micro reliefs do not apply to income from sham transactions (arts. 102.1.30, 106.1.20).
- **No disguised extraction**: cash or assets taken out for private purposes are deemed dividends (art. 122.4).

## PROHIBITIONS

- **Prohibition, simplified tax misuse**: NEVER present the 2% simplified tax for a VAT-registered business, above AZN 200,000, for an excluded activity, or for a business whose e-invoiced business sales exceed 30% in the quarter.
- **Prohibition, startup exemption misuse**: NEVER apply the startup exemption without the certificate, micro or small status and genuine innovation activity.
- **Prohibition, unconditional micro rate**: NEVER describe the micro relief as a flat 5% tax; it needs an average of at least 3 employees and no social insurance debt.
- **Prohibition, contradicting other skills**: NEVER contradict the rates in [azerbaijan-income-tax](azerbaijan-income-tax.md), [az-corporate-income-tax](az-corporate-income-tax.md), [azerbaijan-payroll](azerbaijan-payroll.md) or [azerbaijan-social-contributions](azerbaijan-social-contributions.md).
- **Prohibition, presenting unconfirmed points as confirmed**: NEVER present the items on the Not yet confirmed line as confirmed, nor optimisation as definitive advice; route to a licensed Azerbaijani tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Azerbaijan) before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.


## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of the Republic of Azerbaijan, consolidated text including Law 476-VIIQD of 30 September 2026: arts. 13.2.52, 13.2.53, 13.2.77, 13.2.80, 101.3, 101.7, 102.1.21, 102.1.22-1, 102.1.30, 102.1.30-1, 102.1.31, 102.9, 105.1, 106.1.13, 106.1.13-1, 106.1.13-2, 106.1.20, 106.1.21, 106.1.23, 122.1, 122.2, 122.4, 199.7, 207.3, 218, 218-1, 219.1, 219.5, 220.1, 220.1-1, 221.1-1, 221.2, 221.3, 226, 227 (amendment note to art. 219.5: Law 454-VQD of 16 December 2016) | https://frameworks.e-qanun.az/46/f_46948.html | 2026-10-31 |
| Small and Medium Business Development Agency (KOBİA), "Startap" certificate page | https://smb.gov.az/az/nav/startap-sehadetnamesi | 2026-10-31 |

Not yet confirmed: the property-tax exemption for micro enterprises in the old version (no micro rule found in art. 199 or elsewhere in the Tax Code; a simplified-tax company is not exempt from property tax, since art. 219.5 no longer lists it); the Cabinet size criteria for micro status (taken from az-corporate-income-tax, not re-read); the full startup criteria in Cabinet of Ministers Decision 20 of 29 January 2021 (not read; only the KOBİA summary above); the park activity lists and the industrial-park activities in art. 106.1.13-2; the employer contribution subsidy schedule (Social Insurance Law art. 14-1, not re-read here; see azerbaijan-social-contributions); the Law 476-VIIQD changes from 1 January 2027; the old "10-year tech-park CIT exemption for system integration and software" is confirmed, but the conditions for issuing the industrial-park and technology-park resident registration certificates are not (the Tax Code only refers to rules set by the executive authority).

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
