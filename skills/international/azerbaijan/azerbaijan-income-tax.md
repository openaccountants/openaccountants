---
name: azerbaijan-income-tax
description: 'Use this skill for 2026 Azerbaijan individual income tax working papers for residents, non-residents, employees and individual entrepreneurs. It covers ordinary business profit, annual non-business income, final dividend, interest and rental taxation, the general simplified turnover alternative, micro and listed-service exemptions, business losses, advances and the temporary social-payment credit. Trigger on Azerbaijan personal tax, entrepreneur tax, simplified tax, software developer exemption, rent, dividends, foreign income and annual income return. Use the payroll skill for monthly salaries and the contributions skill for insurance. Property-transfer and fixed-receipt computations are expressly incomplete. Checked against the law (tier 2); no accountant has signed it off.'
version: 0.2
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Azerbaijan Individual Income Tax v0.2

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Resident and non-resident individuals under [Tax Code art. 13.2.5–13.2.6, 95–100](https://e-qanun.az/frameworks/46/f_46948.html). Residents include individuals physically present for more than 182 days in the calendar year and persons in Azerbaijan state service abroad. If presence in neither country exceeds 182 days, apply permanent home, centre of vital interests, habitual abode and citizenship in that order. Residence brings worldwide income into scope; non-residents are taxed on Azerbaijan-source income. The departure-year rule is in the cross-border skill.

Classify employment, entrepreneurial profit and non-business income separately. A registered entrepreneur is not automatically a simplified taxpayer. For salary, use azerbaijan-payroll; for contributions, use azerbaijan-social-contributions. This skill also covers ordinary investments, rent, business losses and the general simplified turnover alternative. Specialist fixed-receipt trades and the full land/building transfer computation remain outside its implemented calculations.

## Rates, bands and thresholds

All figures are AZN unless stated otherwise. These are 2026 figures.

| Item | Amount / rule | Tax year | Official source |
|---|---|---|---|
| Entrepreneurial taxable profit | 20% | 2026 | [Tax Code art. 101.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Annual non-business income, unless a specific final tax applies | 14% | 2026 | [Tax Code art. 101.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| Standard monthly salary | 14% up to 2,500; 350 + 25% above 2,500 | 2026 | [Tax Code art. 101.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Private non-oil/non-gas monthly salary | 3% up to 2,500; 75 + 10% over 2,500 through 8,000; 625 + 14% above 8,000 | 1 Jan–31 Dec 2026 | [Tax Code art. 101.1-1.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Later private non-oil monthly salary schedule | 2027: 5% up to 2,500; 125 + 10% over 2,500 through 8,000; 675 + 14% above 8,000. From 2028: 7%; 175 + 10%; 725 + 14% | 1 Jan 2027 / from 1 Jan 2028 | [Tax Code art. 101.1-1.2–101.1-1.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Primary employment exemption | 200/month if monthly income is at most 2,500; 2,400 annually if annual income is at most 30,000 | 2026 | [Tax Code art. 102.1.6](https://e-qanun.az/frameworks/46/f_46948.html) |
| Resident-company dividend; dividend from non-resident enterprise to individual | 5%, subject to specific exemptions | 2026 | [Tax Code art. 122.1, 101.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| Azerbaijan-source interest | 10%, subject to exemptions | 2026 | [Tax Code art. 123.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Rent and royalties | 14%; qualifying privately owned residential premises rented to individuals: 10% | 2026 | [Tax Code art. 124.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Qualifying micro entrepreneur exemption | 75% of qualifying business income; average monthly employees at least 3 and no compulsory social-insurance debt | 2026 | [Tax Code art. 102.1.30](https://e-qanun.az/frameworks/46/f_46948.html) |
| Listed small-service activities | 75% exemption; listed-activity annual gross income at most 45,000 | 2026 | [Tax Code art. 102.1.30-1, 102.9](https://e-qanun.az/frameworks/46/f_46948.html) |
| Ordinary simplified turnover tax | 2%; taxable operations at most 200,000 over rolling 12 months and no exclusion | 2026 | [Tax Code art. 218.1.1, 218.5–218.6, 220.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Individual business loss carryforward | Up to 3 subsequent years, business income only | 2026 | [Tax Code art. 121.2](https://e-qanun.az/frameworks/46/f_46948.html) |
| Micro entrepreneur social-payment credit | 25% of own annual compulsory social insurance, capped at income tax after loss relief | 1 Jan 2024–31 Dec 2026 | [Tax Code art. 152.3](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

1. Assemble worldwide income for a resident, or Azerbaijan-source income for a non-resident. Identify income taxed finally under arts. 122–124 and 150.1.9–150.1.10 and remove it from aggregate income under art. 100. Do not apply the annual 14% tax again to such income.
2. For entrepreneurial income, use documented business revenue less expenses incurred to earn it, compulsory business payments and tax depreciation. Apply arts. 108–119 and the corporate skill for capital purchases, non-deductible personal expenditure, interest restrictions and depreciation. Deduct only costs connected with earning business income and documented as the law requires (art. 108.1); for a home, car or phone also used privately, deduct only the evidenced business share. Micros can choose cash or accrual accounting; other business sizes use accrual under art. 130.4. A business loss cannot reduce salary or rent.
3. For the general micro exemption, establish micro status using Cabinet Decision 556: employee band 1–10 and annual income at most 200,000, with the higher size result controlling. Then test the separate average-employment and contribution-debt requirements in art. 102.1.30. Annual average employment is the sum of monthly headcounts divided by 12. Exclude sham transactions. Allocate expenses between taxable and exempt income under art. 108.2, so the exemption reduces net qualifying profit proportionately; it does not permit a full deduction of the costs attributable to exempt income.
4. The separate art. 102.1.30-1 list covers software development, design/decorating, translation, advertising, research, science/education/culture/sports services, legal/audit/accounting/financial advice, journalism, market research, valuation, delivery/courier excluding motor freight, tour guiding and service exports. Test the 45,000 gross limit. If other activities exist, listed activities must supply at least 50% of total annual revenue. If an employee becomes an entrepreneur and supplies the same services wholly or partly to the former employer within one year of starting the business, this exemption is unavailable (art. 102.9).
5. Compute tax on net taxable business income at 20%, after qualifying brought-forward business losses. Apply the art. 152.3 credit, then subtract advances. Do not carry a business loss beyond its statutory life or use losses incurred before entering the profit-tax regime, subject to art. 121.3.

For passive income, check art. 102 before applying a headline rate. It exempts state pensions and specified benefits (temporary incapacity benefit is excepted), family gifts/inheritances, and the qualifying part of other gifts/inheritances under art. 102.1.3. It also exempts qualifying small resident-company dividends under art. 102.1.22-1 and listed resident-company securities income under art. 102.1.22-2. AZN deposits with a domestic bank or local foreign-bank branch have an exemption for monthly interest up to 200 per bank (art. 102.1.22-3). Collect the instrument and bank evidence before applying an exemption. Rent of a dwelling to an individual has the specific 10% rule; a hotel or hotel-type accommodation does not receive that rate. If the tenant is not tax-registered, the landlord or appointed tax agent pays and files under art. 124.1.

For the simplified regime, test art. 218.5 exclusions before calculating 2% of gross receipts plus non-sales income, excluding income already withheld at source (arts. 219.1, 220.1). Excluded groups include financial institutions, rental/royalty recipients, wholesalers, specified licensed businesses, manufacturers averaging more than 10 workers per quarter and businesses with opening fixed-asset residual value above 1,000,000, subject to statutory exceptions. A business serving the public retains eligibility for a limited amount of invoiced business work only if it passes the quarterly 30% test in art. 218.6; exported services to non-resident businesses enter that test. General low turnover alone is insufficient. From 1 January 2026, qualifying retail and services to unregistered persons paid through POS terminals count at 0.5 for the rolling eligibility threshold (art. 218.1-1); the 2% tax still uses actual taxable receipts. Art. 219.5 replaces individual income tax and VAT for the qualifying simplified activity, not every other tax or contribution.

## Deadlines and filing

Register as an entrepreneur before starting activity; register other unwithheld/foreign income no later than the date the right to receive it arises ([Tax Code art. 33.4](https://e-qanun.az/frameworks/46/f_46948.html)). The annual return is required from individual entrepreneurs, individuals with income that is not (or cannot be) taxed at source, residents with income from abroad including royalties, and non-residents with Azerbaijan-source income not taxed at source (art. 149.1.3–149.1.4). File the annual Gəlir vergisinin bəyannaməsi and settle the balance by 31 March following the tax year, hence 31 March 2027 for 2026 ([Tax Code art. 149.1–149.2, 152.1](https://e-qanun.az/frameworks/46/f_46948.html)). File electronically through the State Tax Service's Internet Tax Office, retaining income and deduction records under art. 71.4.

Business advances are due within 15 days after each quarter. The ordinary methods are one quarter of prior-year tax, or current-quarter gross taxable revenue times the prior-year tax/gross-revenue coefficient; notify the method by 15 April. The cumulative-profit method and 75% minimum in art. 151.5 concern new/no-prior-activity-or-profit taxpayers, not every entrepreneur. Credit advances at annual settlement ([Tax Code art. 151](https://e-qanun.az/frameworks/46/f_46948.html)).

Simplified taxpayers file and pay quarterly by the following month's 20th. The annual regime election/opt-out is due by 20 April; new taxpayers select on registration, with the statutory restrictions on changing method ([Tax Code art. 218.2, 221.2–221.3](https://e-qanun.az/frameworks/46/f_46948.html)). Suspension or cessation triggers an income-tax return within 30 days under art. 149.3. An individual whose income is fully covered by final withholding does not automatically need another annual return; an optional recalculation/refund return is available under art. 149.5.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Failing to apply for tax registration within the art. 33.4 period attracts AZN 200, and failing to report the place of activity or a change in registration details attracts AZN 40 (art. 58.2). Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

## Cross-border points

Use the cross-border skill for domestic source tests, treaties, foreign-tax credit and CFCs. Under [Tax Code art. 127](https://e-qanun.az/frameworks/46/f_46948.html), foreign income/profit tax paid on foreign-source income is creditable only up to the Azerbaijan tax on that income. Foreign income must still be identified and reported where required by art. 149.1.4. Do not treat a transfer from abroad as proof of either income or exemption. For non-resident employment, art. 102.1.2 requires a non-resident employer payment with no Azerbaijan PE payment or connection; check the exact facts and applicable treaty.

## Two worked examples that recompute

### Ordinary entrepreneur

Assume no exemptions, no brought-forward losses, no art. 152.3 credit and fully documented deductible costs. Revenue of 120,000 less costs of 70,000 produces 50,000 taxable profit. Tax is 10,000; after 7,500 advances the balance is 2,500 (arts. 101.3, 108, 152).

```oa-check
name: AZ ordinary entrepreneur 2026
inputs:
  revenue: 120000
  costs: 70000
  advances: 7500
steps:
  - profit: revenue - costs
  - tax: profit * 0.20
  - balance: tax - advances
expected:
  profit: 50000
  tax: 10000
  balance: 2500
```

### Listed service with a former-employer exclusion

A sole software developer has 40,000 revenue and 10,000 deductible costs. Assume the art. 102.1.30-1 income limit is met, but the developer supplied the same services to the former employer within one year of starting. Art. 102.9 removes that exemption. There are no employees, so the general micro exemption also fails. Profit is 30,000; tax before credit is 6,000. If documented own social payments are 960, the 2026 art. 152.3 credit is 240, leaving 5,760 before advances. This example assumes micro size status and no other credit restrictions.

```oa-check
name: AZ former employer exclusion and micro social credit 2026
inputs:
  revenue: 40000
  costs: 10000
  own_social: 960
steps:
  - profit: revenue - costs
  - tax_before_credit: profit * 0.20
  - credit: min(tax_before_credit, own_social * 0.25)
  - tax: tax_before_credit - credit
expected:
  profit: 30000
  tax_before_credit: 6000
  credit: 240
  tax: 5760
```

## Ask the client first

- Where were you present and resident, and did you leave during the year?
- Is each receipt employment, business, rent, investment, gift or asset-sale income, and what tax was already withheld?
- What are the activity, customer mix, gross receipts, worker headcounts and prior regime election?
- Are there former-employer services, micro-size evidence or unpaid social contributions?
- What deductions, losses, social payments, foreign taxes and advances are evidenced?
- Were there land/building sales or a fixed-receipt activity requiring the missing specialist computation?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 13, 33, 57–59, 95–102, 108–130, 149–152, 218–221 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Cabinet Decision 556, size table and notes | https://e-qanun.az/framework/41048 | 2026-10-31 |

Not yet confirmed: a three-month extension of the annual return deadline (cited by the old version of this skill from a secondary source; not found in art. 149); complete geographic land/building disposal calculation and fixed-receipt individual trades; specialized bank-deposit exemptions beyond the monthly allowance. These are not calculated here.

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
