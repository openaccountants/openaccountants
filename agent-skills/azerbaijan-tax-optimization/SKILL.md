---
name: azerbaijan-tax-optimization
description: "Use this skill whenever asked about reducing tax in Azerbaijan, tax planning, or legal strategies to minimise tax for a small business or entrepreneur in Azerbaijan in tax year 2026. Trigger on phrases like \"reduce tax Azerbaijan\", \"simplified tax 2%\", \"micro business Azerbaijan\", \"startup exemption\", \"Azerbaijan dividends 5%\", \"tech park Azerbaijan\", \"liberated territories tax\", \"Nakhchivan tax exemption\", \"save tax Azerbaijan\", \"tax planning Azerbaijan\". This skill covers the 2% simplified turnover tax and its exclusions (including the 30% business-customer test), the 75% micro-business relief, the 3-year startup exemption, technology-park, industrial-park and territorial exemptions, dividend taxation and the deemed-dividend rule, and the anti-avoidance red lines. The computations themselves are out of scope (az-corporate-income-tax, azerbaijan-income-tax, azerbaijan-payroll, azerbaijan-social-contributions, azerbaijan-vat, azerbaijan-cross-border). ALWAYS read this skill before advi"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/azerbaijan-tax-optimization"
  jurisdiction: "AZ"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Azerbaijan Tax Optimization v0.4

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Compare legal 2026 tax options for an Azerbaijani small company or individual entrepreneur. Produce an evidence-backed planning working paper and recommendation for a local tax adviser. This Guide covers simplified tax, micro/startup relief, park and territorial incentives, dividends and anti-avoidance. It does not prepare a return or establish eligibility for a certificate. Read the linked corporate, individual, VAT, payroll, social-contribution and cross-border Guides for their computations. Operative law controls any conflict; do not assume a sibling text overrides the statute. No accountant has approved this version.

### Quick reference

| Field | Value | Official source |
| --- | --- | --- |
| Country | Republic of Azerbaijan | https://frameworks.e-qanun.az/46/f_46948.html |
| Currency | AZN (manat) | https://frameworks.e-qanun.az/46/f_46948.html |
| Headline levers | **2% simplified turnover tax**; 75% micro-business relief; 3-year startup exemption; technology-park, industrial-park and territorial exemptions | https://frameworks.e-qanun.az/46/f_46948.html |
| Ordinary rates | Company profit tax **20%**; individual entrepreneur profit **20%** | https://frameworks.e-qanun.az/46/f_46948.html |
| Simplified tax | **2% of gross receipts** (weighted taxable operations ≤ AZN 200,000 in any rolling 12 months, not VAT-registered, no exclusion); eligible catering electing simplified tax above weighted AZN 200,000: **8%**, and **6%** on cashless POS receipts for services to the public from 1 Jan 2026 to 31 Dec 2028 | https://frameworks.e-qanun.az/46/f_46948.html |
| Dividends | **5%** withheld at source; not taxed again in the recipient's hands | https://frameworks.e-qanun.az/46/f_46948.html |
| Anti-avoidance | Eligibility exclusions, the 30% business-customer test, deemed dividends, substance for park and territorial reliefs | https://frameworks.e-qanun.az/46/f_46948.html |

> **Azerbaijan's headline is the 2% simplified tax**, uniform across the country. It is not open to every small business: a business that mainly invoices other registered taxpayers, wholesales, rents out property, earns royalties or needs a licence is excluded (Tax Code arts. 218.5, 218.6).
## Ask the client first

- Which entity, residence, activity and tax year apply?
- What are actual and forecast rolling taxable operations, quarterly customer mix and qualifying POS receipts by transaction date?
- What are deductible costs, profit margin, fixed-asset value and VAT status?
- What are monthly headcounts, official size classification and social-insurance arrears?
- What certificates, registration dates and evidenced park/territorial activities exist, including activities elsewhere?
- Are there prior-employer services, private extractions or proposed distributions?

## The method, step by step

### 1. Test eligibility before comparing tax

- **Simplified tax rate**: 2% of receipts from goods, work, services and property plus non-sales income (excluding income already taxed at source), for a business not registered for VAT whose taxable operations are AZN 200,000 or less in every month of any rolling 12-month period _(Tax Code arts. 218.1.1, 219.1, 220.1)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Threshold weighting**: cashless POS-terminal receipts from retail trade and from services to persons not registered with the tax authority from taxable operations after 1 January 2026 count at 0.5 towards the AZN 200,000 test. Earlier receipts remain unweighted (Law 297-VIIQD art. 18.1; STS 2026 FAQ, printed p. 13) _(art. 218.1-1)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Catering above AZN 200,000**: qualifying catering businesses above the weighted threshold may elect simplified tax at 8% by a written application within 10 days from the first of the month after exceeding the threshold (STS 2026 FAQ, printed p. 13); the base from cashless POS receipts for services to the public is taxed at 6% from 1 January 2026 for 3 years. The POS terminal must be integrated with the cash register _(arts. 218.1.2, 220.1-1)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **What it replaces**: a company paying simplified tax is not liable for VAT or profit tax; an individual entrepreneur is not liable for income tax or VAT _(art. 219.5)_. Property tax is not replaced: Law 454-VQD of 16 December 2016 struck "and property tax" from art. 219.5, so a simplified-tax company does not obtain a property exemption merely from that status. A separate exemption may apply, including the micro-business exemption in art. 199.14 below. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **No expense deduction under simplified tax**: tax is on gross receipts, so, before micro relief and other taxes, it is cheaper than ordinary profit tax when the real margin is above 10% (2% of turnover equals 20% profit tax at a 10% margin). Exceeding the weighted threshold generally requires reassessment of VAT/profit-tax status; qualifying catering has the separate regime above. Never replace the statutory weighted threshold with gross unweighted receipts. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Who is excluded** _(art. 218.5)_: producers of excisable or compulsorily labelled goods; credit institutions, insurers, investment funds and managers, licensed securities firms, pawnshops; non-state pension funds; persons earning income from renting out property or from royalties; natural monopolies; persons whose owned fixed assets had a residual value above AZN 1,000,000 at the start of the year (the art. 218.1.2 catering and art. 218.4 special-taxpayer categories are excepted from this asset exclusion); public legal entities; producers with more than 10 employees on average in a quarter; wholesale traders; persons doing work or services other than for persons not registered as taxpayers (the public), except the special transport category in art. 218.4.1 and fixed-activity individuals in art. 220.10; sellers of gold and jewellery/household articles made from gold, diamonds and furs; and licensed activities (compulsory-insurance agents and the listed exceptions aside). [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **The 30% test** _(arts. 218.6, 218.7)_: a retailer keeps the regime while e-invoiced wholesale sales are no more than 30% of its total trade in the quarter, excluding non-sales income. A business serving the public keeps the regime while e-invoiced work for companies and registered individuals (including invoiced services to non-resident businesses) is no more than 30% of its total services/work in the quarter, excluding non-sales income. Apply these retention tests also to mixed operations consisting of goods, work and services. Above 30%, the right ends from the 1st of the month after that quarter. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Election and filing**: elect, or opt out, by 20 April each year; the choice holds to the year end; a new business uses the method in its registration application _(art. 218.2)_. Returns and payment quarterly, by the 20th of the month after the quarter _(arts. 221.2, 221.3)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Dividends from a small company**: dividends paid to the individual founders of a resident company that keeps income and expense records, is not VAT-registered and has operations up to AZN 200,000 in any rolling 12 months are exempt from income tax _(art. 102.1.22-1)_ and from simplified tax _(art. 218-1.1.4)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Micro entrepreneur social credit**: an individual micro entrepreneur on simplified tax deducts 25% of the compulsory social insurance paid for themselves in the quarter from that quarter's simplified tax (not more than the tax), from 1 January 2024 for 3 years _(art. 221.1-1)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Standard rates** (the old research gap is closed): profit tax 20% for companies and permanent establishments _(art. 105.1)_; 20% on an individual entrepreneur's taxable profit _(art. 101.3)_. There is no "5% of net profit" micro regime; the micro relief is a 75% exemption with conditions (Section 3), which is not an unconditional 5% rate for every small company. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).


### 2. Test reliefs and certificates

**Startup, Micro & Regional Incentives**

| Incentive | Detail | Source |
| --- | --- | --- |
| Micro business relief | 75% of a micro company's (or micro individual entrepreneur's) business profit is exempt if the average monthly number of employees in the year is at least 3 and there is no compulsory social insurance debt. Average = sum of monthly headcounts ÷ 12. Where a micro company failed the relief conditions and moves out of micro size in the following reporting year, a credit of 75% of the profit tax paid in the previous 3 micro years is given. Not available for income from sham (goodsless) transactions. Micro size follows the Cabinet criteria; the current KOBİA FAQ describes at most 10 employees and AZN 200,000 annual income, with the higher category controlling. This size test is separate from the 3-employee relief condition. See [az-corporate-income-tax](az-corporate-income-tax.md). | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code arts. 106.1.20, 102.1.30 |
| Listed small services | 75% of income is exempt for individuals with listed activities (software development, design, translation, advertising, legal, audit, accounting, financial advice, tour guiding, service exports and others) earning up to AZN 45,000 a year from them (revenue, before expenses). Lost if a former employee starts the same activity as an entrepreneur and supplies the same services to the former employer within one year. A person who also has other activities qualifies only if the listed activities give at least 50% of annual total income. Detail: [azerbaijan-income-tax](azerbaijan-income-tax.md). | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code art. 102.1.30-1, 102.9 |
| Startup certificate | Use an actual valid "Startap" certificate; do not infer entitlement to it from this summary. A micro or small startup holding that certificate pays no profit tax (company) or income tax (individual entrepreneur) on profit from innovation activity for 3 years from the certificate date. A startup is a business based on an innovative initiative that meets the set criteria and holds the certificate; innovation activity means creating new or improved goods, work, services or processes from research and development. KOBİA issues the certificate, after its Expert Council's opinion, only to micro or small enterprises registered as taxpayers; where the applicant's founder is a medium or large enterprise, that founder's share may not exceed 49%. | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code arts. 106.1.23, 102.1.31, 13.2.77, 13.2.80; KOBİA startup certificate page https://smb.gov.az/az/nav/startap-sehadetnamesi |
| Liberated territories | Residents of the liberated territories are exempt from profit (income), property, land and simplified tax for 10 years from 1 January 2023; their shareholders' dividends are exempt for the same period. Financial services and road freight are excluded. Budget-funded contractor supplies are also excluded, except supplies by resident contractors conducting production inside the liberated territory. A locally registered non-producing contractor does not qualify for that exception. Conditions by activity: production counts only for a taxpayer registered and producing there, and permits sales of those produced/extracted/processed goods within or outside the liberated territory, including exports; wholesale, construction and business services count only for supplies to liberated-territory residents (supplies outside or exports lose the exemption); tourism, retail, catering and other public services count when registered and operating there. A resident doing the same activity elsewhere in Azerbaijan loses the exemption; other activities elsewhere need separate income and expense records. | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code arts. 226.2, 226.3, 227.1, 227.3, 227.4 |
| Nakhchivan | The same profit, property, land, simplified tax and dividend exemptions apply to Nakhchivan residents (registered there or centrally and operating directly in Nakhchivan) for 10 years from 1 January 2026, under the same art. 226.3 and 227.4 conditions. | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code art. 226.4 |
| Industrial and technology parks | Require an actual valid resident registration certificate; do not infer entitlement from this summary. A legal entity resident in an industrial or technology park is exempt on income from its park activity for 10 years from the reporting year of registration (individual entrepreneurs: art. 102.1.21). The exemption also covers technology-park residents doing system integration and software development outside the park. Dividends paid by those off-park technology-park firms are exempt for 10 years from the certificate year. Property and land in the park are exempt for 10 years from the registration reporting year (also for qualifying off-park technology-park firms). A park resident is a person holding the park resident registration certificate issued under the rules set by the executive authority and operating in the park (a technology-park resident: in or outside the park). | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code arts. 13.2.52, 13.2.53, 106.1.13, 106.1.13-1, 102.1.21, 199.7, 207.3 |
| Industrial-park residents in set activities | Profit from the specified activity of a resident of a park created by the designated body is exempt for 6 years from 1 January 2025. Do not apply until the designated activity list and actual resident status are verified. | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code art. 106.1.13-2 |
| Technology-park specialists | Specialists employed in system integration and software work by an off-park technology-park resident pay 5% income tax on monthly employment income for 7 years from 1 January 2026. Detail: [azerbaijan-payroll](azerbaijan-payroll.md). | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code art. 101.7.2 |
| SME clusters | Profit of an SME cluster company is exempt for 7 years from entry in the cluster register. | https://frameworks.e-qanun.az/46/f_46948.html; Tax Code art. 106.1.21 |
| Employer contribution subsidy | Check eligibility for any employer social-insurance reimbursement under Social Insurance Law arts. 14-1.1 and 14-1.1-1 in the linked Guide; no entitlement is determined here. Schedule and conditions: [azerbaijan-social-contributions](azerbaijan-social-contributions.md). | Social Insurance Law art. 14-1 (via that Guide; no amount claimed here), https://frameworks.e-qanun.az/3/f_3813.html |
| Micro property-tax exemption | Micro businesses are exempt, except where owned fixed assets at the start of the year have residual value above AZN 1,000,000. This separate relief can cover a simplified taxpayer; simplified status itself does not remove property tax. | Tax Code art. 199.14: https://frameworks.e-qanun.az/46/f_46948.html |

Micro size source: KOBİA current FAQ, restating Decision 556: https://smb.gov.az/az/nav/en-cox-verilen-suallar. The register copy could not be opened; full startup-decision and park-certificate conditions remain on the Not yet confirmed line.

Law 476-VIIQD of 30 September 2026 changes arts. 101.7, 102.1.21, 102.1.31, 106.1.13, 106.1.13-1 and 106.1.23 from 1 January 2027. Those changes are not applied here.


### 3. Compare extraction after company tax

- **Dividend withholding tax**: 5% withheld at source on dividends paid by a resident company _(Tax Code art. 122.1)_. Once withheld, the dividend is not taxed again in the hands of the individual or company that receives it, and is not taxed again when paid on as a dividend _(art. 122.2)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Deemed dividends**: company assets or cash passed to a founder for purposes outside the business (other than loans to the founder or repayment of the founder's loans), and payment of a founder's debts to others, are treated as dividends and taxed at 5% at source _(art. 122.4)_. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Exempt routes**: dividends from a qualifying small company to individual founders (art. 102.1.22-1); dividends of liberated-territory and Nakhchivan residents (arts. 227.3, 226.4); dividends paid by off-park technology-park software firms for 10 years (art. 106.1.13-1). [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).

A company paying 5% on dividends, or a technology-park company with the profit and dividend exemptions, can be highly efficient for IT and software founders, provided the activity, registration certificate and substance tests are met.


## Worked cases

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

### Low-margin company: the ordinary system wins

A non-VAT company with AZN 150,000 receipts and AZN 140,000 deductible costs has AZN 10,000 profit. Assume no simplified-tax exclusion and no micro relief entitlement. Simplified tax is AZN 3,000, ordinary profit tax AZN 2,000, so ordinary profit tax is lower by AZN 1,000. This compares business tax only; assess VAT, distributions, social contributions and compliance separately. Source: Tax Code arts. 105.1, 218-220 above.

```oa-check
name: AZ low margin ordinary versus simplified decision
inputs:
  receipts: 150000
  costs: 140000
steps:
  - profit: receipts - costs
  - simplified_tax: receipts * 0.02
  - ordinary_tax: profit * 0.20
  - ordinary_saving: simplified_tax - ordinary_tax
expected:
  profit: 10000
  simplified_tax: 3000
  ordinary_tax: 2000
  ordinary_saving: 1000
```

## When to refuse or refer

- **Eligibility red line**: the 2% simplified tax requires weighted taxable operations of AZN 200,000 or less, non-VAT status and no art. 218.5 exclusion; a business mainly invoicing registered customers fails the 30% test. The startup exemption requires the certificate and profit from innovation activity. **AUDIT FLASH POINT**: misusing the certificates or regimes is challengeable. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **Substance requirement**: park and territorial exemptions require registration as a resident and real activity there (for the liberated territories and Nakhchivan, tax registration there or centrally and activity carried out directly there, arts. 226.2, 226.4, with the activity conditions in art. 227.4). [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **No business splitting**: do not split a business to stay under the weighted AZN 200,000 threshold without substance. [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **No goodsless transactions**: the micro reliefs do not apply to income from sham transactions (arts. 102.1.30, 106.1.20). [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).
- **No disguised extraction**: cash or assets taken out for private purposes are deemed dividends (art. 122.4). [Tax Code](https://frameworks.e-qanun.az/46/f_46948.html).

### Prohibitions

- **Prohibition, simplified tax misuse**: NEVER present the 2% simplified tax for a VAT-registered business, above the statutory weighted AZN 200,000 threshold, for an excluded activity, or for a business whose e-invoiced business sales exceed 30% in the quarter.
- **Prohibition, startup exemption misuse**: NEVER apply the startup exemption without the certificate, micro or small status and genuine innovation activity.
- **Prohibition, unconditional micro rate**: NEVER describe the micro relief as a flat 5% tax; it needs an average of at least 3 employees and no social insurance debt.
- **Prohibition, contradicting other skills**: Read the law and reconcile a conflict before using the rates in [azerbaijan-income-tax](azerbaijan-income-tax.md), [az-corporate-income-tax](az-corporate-income-tax.md), [azerbaijan-payroll](azerbaijan-payroll.md) or [azerbaijan-social-contributions](azerbaijan-social-contributions.md).
- **Prohibition, presenting unconfirmed points as confirmed**: NEVER present the items on the Not yet confirmed line as confirmed, nor optimisation as definitive advice; route to a licensed Azerbaijani tax adviser.

## Completion checklist

Reconcile customer mix, transaction dates, cost evidence and micro status before comparing regimes. Run both tax options, then assess extraction and other taxes separately. Preserve each certificate, substantive activity test and expiry date. Report unresolved points to the adviser and refuse to manufacture relief or accountant approval.

### Disclaimer

This Guide and its outputs are informational and computational working papers. All outputs require review by a qualified local professional before acting.

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of the Republic of Azerbaijan, selected operative text and neighboring exceptions read, including future Law 476-VIIQD annotations: arts. 13.2.52, 13.2.53, 13.2.77, 13.2.80, 101.3, 101.7, 102.1.21, 102.1.22-1, 102.1.30, 102.1.30-1, 102.1.31, 102.9, 105.1, 106.1.13, 106.1.13-1, 106.1.13-2, 106.1.20, 106.1.21, 106.1.23, 122.1, 122.2, 122.4, 199.7, 199.14, 207.3, 218, 218-1, 219.1, 219.5, 220.1, 220.1-1, 221.1-1, 221.2, 221.3, 226, 227 (amendment note to art. 219.5: Law 454-VQD of 16 December 2016) | https://frameworks.e-qanun.az/46/f_46948.html | 2026-11-16 |
| KOBİA, startup certificate summary and criteria paragraphs read | https://smb.gov.az/az/nav/startap-sehadetnamesi | 2026-11-16 |
| KOBİA FAQ, ordinary size and higher-category paragraphs read | https://smb.gov.az/az/nav/en-cox-verilen-suallar | 2026-11-16 |
| STS 2026 FAQ, printed p. 13, POS commencement and catering election paragraphs read | https://www.taxes.gov.az/uploads/2026/faq/FAQ2026.pdf | 2026-11-16 |

Not yet confirmed: the complete current Decision 556 register copy and new-business classification details (register transport failed; ordinary size/higher-category tests read in KOBİA FAQ); the full startup criteria in Cabinet of Ministers Decision 20 of 29 January 2021 (not read; only the KOBİA summary above); the park activity lists and the industrial-park activities in art. 106.1.13-2; the employer contribution subsidy schedule (not computed here; use the contributions Guide); the Law 476-VIIQD changes from 1 January 2027; the old "10-year tech-park CIT exemption for system integration and software" is confirmed, but the conditions for issuing the industrial-park and technology-park resident registration certificates are not (the Tax Code only refers to rules set by the executive authority).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `azerbaijan-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/azerbaijan-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
