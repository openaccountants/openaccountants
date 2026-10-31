---
name: az-corporate-income-tax
description: 'Use this skill for 2026 Azerbaijan corporate profit tax working papers for resident enterprises, permanent establishments and commercial income of non-profit organisations. It covers residence, ordinary taxable profit, documented business deductions, depreciation and repairs, losses, micro relief, the general simplified turnover alternative, catering turnover taxation, advances and annual settlement. Trigger on Azerbaijan corporate income tax, profit tax, company losses, tax depreciation, micro company, quarterly advances, simplified tax and PE remittance. Cross-border, CFC and treaty matters also require the dedicated cross-border skill. Sector, territorial and investment incentives require separate eligibility analysis. Checked against the law (tier 2); no accountant has signed it off.'
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.1
category: international
---

# Azerbaijan Corporate Income Tax v0.1

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Resident enterprises, non-resident enterprises with Azerbaijan permanent establishments (PEs), and non-commercial organisations earning business income under [Tax Code art. 103–104](https://e-qanun.az/frameworks/46/f_46948.html). A legal person established under Azerbaijan law or with its place of management in Azerbaijan is resident. Management means the place where necessary commercial decisions and daily practical management occur, not merely the registered location of its supervisory body ([Tax Code art. 13.2.5.3](https://e-qanun.az/frameworks/46/f_46948.html)). Residents include foreign-source income; PE taxation uses attributable Azerbaijan-source profit.

First check whether the activity falls within a statutory PSA/pipeline or special economic-zone regime, a specific exemption or the simplified-tax alternative. This skill implements ordinary corporate profit tax and the general small-business alternative. Investment, park, sector and territorial incentives require their own eligibility documents. Tax residence, withholding and CFC calculations also require the cross-border skill.

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Corporate/PE taxable profit | 20% | 2026 | [Tax Code art. 105.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Corporate losses | Carry forward up to 5 subsequent years | 2026 | [Tax Code art. 121.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Buildings, structures and capital land improvements | Depreciation up to 7% | 2026 | [Tax Code art. 114.3.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Machinery/equipment; working animals; other fixed assets | Up to 20% | 2026 | [Tax Code art. 114.3.2, 114.3.4, 114.3.7](https://e-qanun.az/frameworks/46/f_46948.html) |
| High-tech computing, vehicles, geological/pre-extraction costs | Up to 25% | 2026 | [Tax Code art. 114.3.2-1, 114.3.3, 114.3.5](https://e-qanun.az/frameworks/46/f_46948.html) |
| Intangibles | Unknown useful life: up to 10%; known life: proportionate over useful years | 2026 | [Tax Code art. 114.3.6](https://e-qanun.az/frameworks/46/f_46948.html) |
| Micro business profit exemption | 75%; average monthly employees at least 3 and no compulsory social-insurance debt | 2026 | [Tax Code art. 106.1.20](https://e-qanun.az/frameworks/46/f_46948.html) |
| Ordinary simplified tax | 2% of taxable receipts, qualifying rolling operations at most 200,000 | 2026 | [Tax Code art. 218.1.1, 220.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Large-turnover catering simplified regime | 8%; qualifying public POS receipts 6% | 6%: 1 Jan 2026–31 Dec 2028 | [Tax Code art. 218.1.2, 220.1-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Foreign/related-party loan interest ceiling | 125% of comparable interbank auction rate or published average rate | 2026 | [Tax Code art. 110.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Specified foreign-debt capital restriction | Interest on debt exceeding twice net assets disallowed, subject to statutory exclusions | 2026 | [Tax Code art. 110.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| Dividend / PE profit remittance tax | 5%, subject to exemptions/treaties | 2026 | [Tax Code art. 122.1, 126](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

Start from documented revenue and expenses, then reconcile accounting profit to tax profit. Resident enterprises include foreign PE income, foreign dividends, interest and royalties unless exempt; non-residents with a PE include only attributable income ([Tax Code art. 104.1–104.4](https://e-qanun.az/frameworks/46/f_46948.html)). Remove income that is exempt and the related costs. Allocate genuinely inseparable costs using taxable revenue as a proportion of total revenue under art. 108.2. Non-profits separate commercial income from exempt donations and subscriptions (art. 106.1.2).

Use accrual accounting for small, medium and large taxpayers; micros choose cash or accrual (art. 130.4). Under arts. 134–136, recognise rights to revenue and liabilities for costs, not simply bank movements. Keep invoices, contracts and evidence of performance. Deduct business-purpose expenditure and compulsory payments documented as required by art. 108.1. Add back capital expenditure, private/non-commercial costs, tax profit charges, financial sanctions and interest, unsupported or sham purchases, and other non-deductible expenditure under arts. 109 and 119.1. Art. 119.2 permits specified representation, employee housing/food and related costs only under the prescribed norms set out below. Art. 109.8 caps the specified purchase-act/cash-register-receipt deductions at 2% of the greater of annual income and expenses for each statutory case, with the listed goods exclusions.

Capital purchases are not an immediate expense. Use the residual-value method for each asset category, separately for each building; intangibles follow art. 114.3.6. Start with opening tax residual value after prior depreciation, add current qualifying acquisitions and capitalised excess repair costs, and deduct residual value of disposals under art. 114.6. Apply the selected statutory rate. Do not depreciate bare land, art, the other excluded assets in art. 114.2, or assets not placed in service. Art. 114.8 permits residual write-off when residual value is below 500 or below 5% of original cost. Include disposal proceeds above the asset's residual value in income (art. 114.7). Repair deductions are limited under art. 115: buildings/land improvements 2%, machinery/computing/vehicles other than trucks 5%, other assets 3%, trucks 8% of prior year-end residual value. Capitalise excess repairs; preserve any permitted unused repair allowance under that article. Micro and small enterprises can use the increased depreciation coefficients in arts. 114.3-2–114.3-3; do not assume size from turnover alone.

For [Cabinet Decision 492, paragraphs 1.2–4.4](https://nk.gov.az/uploads/doc/docs/674d98557ed68.pdf), the prescribed limits include VAT:

- Ordinary employee meals are deductible up to 5 per employee per working day. Direct employee reimbursement must be cashless; employer-prepared meals require documented ingredient purchases; external catering requires an electronic invoice. Days absent or on business travel do not qualify. The separate 5 daily preventive-food/milk allowance for the specified hazardous/heavy/underground workers is additional to that ordinary meal allowance. Seagoing crews instead use their distinct 25 AZN daily Caspian or USD 25 daily outside-Caspian allowance, without the ordinary meal allowance (paragraphs 2.1–2.5).
- Employee residential rent deduction is min(50% of eligible annual rent, 1% of annual revenue). A notarised lease with the employee or employer as tenant and cashless employer payment to the employee or landlord are required (paragraphs 3.1–3.2).
- Representation deduction is separately min(50% of eligible annual representation costs, 1% of annual revenue). Costs must be cashless, substantiated and documented. The defined guest reception/cooperation costs include specified visas, transport, hotels, meals, translation and souvenirs. Recreation, entertainment and disease prevention/treatment are excluded (paragraphs 4.1–4.4). Do not combine the housing and representation limits into one 1% pool or deduct the full invoice merely because it is a business meeting.

For ordinary domestic business travel, [Cabinet Decision 14, paragraph 1](https://frameworks.e-qanun.az/13/f_13154.html) sets the daily norm at 125 in Baku, 100 in Nakhchivan city, 95 in Ganja/Sumgayit and 90 elsewhere; 70% of the norm is the hotel component. Under Tax Code art. 108.4, actual documented domestic travel expense is deductible within the norm, with the daily-expense documentation exception. If hotel proof is missing, only 50% of the norm's hotel component is deductible. Under art. 109.7, expenditure above the applicable norm is disallowed. Paragraphs 4–5 of Decision 14 separate the daily norm (hotel and daily subsistence/local services) from documented travel to/from the destination. For foreign travel, retrieve the exact country/city and currency row of Decision 14 Appendix 1 and apply the appropriate statutory category/addition, rather than substituting the domestic amount. The consolidated source includes 2026 special protocol/security-personnel amendments; they do not extend the ordinary private-business limits.

Foreign and related-party borrowing requires three separate checks: the comparable-rate ceiling in art. 110.1, arm's-length adjustment under art. 110.2 and the foreign-debt restriction in art. 110.3. For the last check, foreign banks/credit institutions and bonds traded on foreign exchanges are excluded; resident banks and credit organisations are outside that restriction. A commercially reasonable interest rate does not remove the capital restriction.

Deduct eligible unexpired corporate losses against later profit, retaining the origin year and utilisation history. Art. 121.3 restricts pre-profit-tax-regime losses and carryovers of foregone depreciation during exempt periods. The five-year period differs from the individual entrepreneur's three years. Apply qualifying exemptions before computing 20% tax; deduct foreign-tax credit and instalments at settlement, without crediting more foreign tax than the Azerbaijan tax on that income (art. 127).

For micro relief, Cabinet Decision 556 uses employee and revenue size criteria and the larger classification controls. Then apply the distinct art. 106.1.20 requirements: average employment at least three, no social debt and no sham-transaction relief. Apply art. 108.2 so costs of exempt income are not deducted twice. This is not an unconditional 5% tax for every small company. Qualifying startup innovation profit is exempt for three years from the startup certificate under art. 106.1.23. Other incentives are outside the calculation scope here.

For simplified tax, use actual taxable receipts and non-sales income under art. 219.1. Confirm all art. 218 exclusions and the quarterly invoiced-business-sales/services 30% exceptions. The ordinary 2% rate has no Baku 4% split. Qualifying retail/public-service POS receipts from 1 January 2026 count at 0.5 only when testing the rolling eligibility threshold (art. 218.1-1). The ordinary simplified corporate taxpayer is outside profit tax and VAT under art. 219.5. For catering above the threshold, the separate regime in arts. 218.1.2 and 220.1-1 uses 8% on other receipts and, from 1 January 2026 to 31 December 2028, 6% on qualifying services to the public paid through POS integrated with the cash register. Do not halve taxable receipts when applying 6%.

## Deadlines and filing

File the Mənfəət vergisinin bəyannaməsi and pay the annual balance by 31 March following the year: 31 March 2027 for 2026 ([Tax Code art. 149.2, 152.1](https://e-qanun.az/frameworks/46/f_46948.html)). Submit via the State Tax Service Internet Tax Office. Commercial registration/tax registration is handled under arts. 33–34; identify the PE registration event before activity.

Pay advances within 15 days after each quarter. Under art. 151.1, each is one quarter of prior-year tax; art. 151.2 instead permits current-quarter gross taxable revenue times the prior-year tax/revenue ratio. Notify the annual method by 15 April, and submit the required current-tax statement for the second method. New or previously inactive/no-taxable-profit businesses use the cumulative-profit process in art. 151.5 with its 75% minimum. The annual tax credits these payments and reconciles excess advances under art. 151.6. Do not apply a universal 75% advance rule to established profitable companies.

Simplified returns/payments are quarterly by the next month's 20th; the election/opt-out is generally by 20 April (arts. 218.2, 221.2–221.3). Suspension requires a return within 30 days under art. 149.3. Liquidating entities/PEs file profit tax within 30 days of presenting the liquidation balance to the registration authority (art. 149.4). Keep tax records for at least five years under art. 71.4.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

## Cross-border points

PE net profits remitted to the non-resident attract 5% in addition to profit tax (art. 126). Classify non-PE source payments under arts. 122–125; ordinary service withholding is not a replacement for PE profit tax where a PE exists. Screen controlled transactions under art. 14-1 and CFCs under art. 14-2. Treaty relief requires the relevant treaty and administrative procedure; a foreign invoice or shareholder address proves neither. The cross-border skill covers these steps, including foreign-tax credit and the facts needed for cessation/departure.

## Two worked examples that recompute

### Ordinary corporate profit and annual settlement

Assume the company has no exemption, foreign income or restricted costs. Revenue is 600,000; deductible operating costs are 400,000 and tax depreciation is 20,000. Profit of 180,000 gives tax of 36,000. Advances of 30,000 leave 6,000 payable (arts. 104, 105, 152).

```oa-check
name: AZ ordinary corporate settlement 2026
inputs:
  revenue: 600000
  costs: 400000
  depreciation: 20000
  advances: 30000
steps:
  - profit: revenue - costs - depreciation
  - tax: profit * 0.20
  - balance: tax - advances
expected:
  profit: 180000
  tax: 36000
  balance: 6000
```

### Depreciation and an expiring loss

An ordinary enterprise has 100,000 profit before tax depreciation, an eligible machinery pool of 120,000 and a 30,000 unexpired loss. At the assumed elected maximum 20% machinery rate, depreciation is 24,000. Profit after depreciation and loss is 46,000; tax is 9,200. The loss is assumed available under art. 121.1, not a pre-entry simplified-regime loss. No increased micro/small coefficient is elected.

```oa-check
name: AZ machinery and corporate loss 2026
inputs:
  pre_depreciation_profit: 100000
  machinery_pool: 120000
  loss: 30000
steps:
  - depreciation: machinery_pool * 0.20
  - taxable_profit: max(0, pre_depreciation_profit - depreciation - loss)
  - tax: taxable_profit * 0.20
expected:
  depreciation: 24000
  taxable_profit: 46000
  tax: 9200
```

## Ask the client first

- Where was the entity formed and where are commercial decisions and daily management made?
- Is there a PSA, park/startup/investment certificate, territorial incentive or simplified-tax election?
- What revenue, expenses, asset/repair registers and tax-accounting method are evidenced?
- What are the headcounts, size classification, social debt and customer mix?
- What are the loss years, advances, foreign taxes, related parties and foreign debt terms?
- Are there distributions, PE remittances, a suspension or liquidation?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 13, 33–34, 57–59, 103–130, 149–152, 218–221 | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Cabinet Decision 492, paras. 1.2–4.4, expense limits and conditions | https://nk.gov.az/uploads/doc/docs/674d98557ed68.pdf | 2026-10-31 |
| Cabinet Decision 14, domestic norms, foreign country/city Appendix 1 and 2026 amendments | https://frameworks.e-qanun.az/13/f_13154.html | 2026-10-31 |
| Cabinet Decision 556, size criteria | https://e-qanun.az/framework/41048 | 2026-10-31 |

Not yet confirmed: None within the stated ordinary-regime scope. Horizontal-monitoring straight-line depreciation and special incentive computations are outside scope; foreign travel uses the actual official country/city row, not a generic rate.

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
