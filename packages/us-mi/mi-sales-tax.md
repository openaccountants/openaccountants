---
name: mi-sales-tax
description: Apply Michigan sales and use tax for 2026, covering the 6% sales tax on retail sales of tangible personal property, the 4% rate on residential electricity, gas and home heating fuel, the 6% use tax on goods brought into Michigan or bought from sellers who did not collect tax (with credit for tax paid to another state, and use tax on telecommunications and hotel stays), the ban on any city or local sales or use tax, the yearly sales tax licence, and the sales, use and withholding (SUW) returns due on the 20th with an annual return by February 28. Trigger on "Michigan sales tax", "MI sales tax", "Michigan use tax", "Michigan sales tax rate", "Michigan sales tax return", "Form 5080 sales tax", "General Sales Tax Act". Load us-sales-tax first for the general US method and us-sales-tax-nexus-50-state-matrix for remote seller nexus.
version: "3.0"
jurisdiction: US-MI
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Michigan sales and use tax, 2026

> **Source-cited draft.** Built from Treasury's Sales and Use Taxes page, its Filing Requirements FAQ, and its SUW filing frequency and due date pages, read on 2026-11-13. The General Sales Tax Act (1933 PA 167) and Use Tax Act (1937 PA 94) could not be opened on the Legislature site that day (bot check). No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Michigan sales tax is **6%** of the total price of taxable retail sales of tangible personal property; residential electricity, natural or artificial gas and home heating fuels are taxed at **4%**. Use tax is also **6%**, on taxable items brought into Michigan or bought from out-of-state sellers that did not collect, with credit for tax paid to another state. No city or local unit may add a sales or use tax, so the rate is the same everywhere in the state. Returns are monthly or quarterly by the **20th** of the following month, plus an annual return by **February 28**. Source: [Treasury, Sales and Use Taxes](https://www.michigan.gov/taxes/business-taxes/sales-use-tax).

## Scope and who this is for

**In scope.** Sellers who sell tangible personal property to the final consumer in Michigan; buyers who owe use tax; the rates, licence and returns.

**Out of scope.**

| Topic | Where it goes |
|---|---|
| General US sales tax method, marketplace and exemption certificate basics | `us-sales-tax` |
| Whether a remote seller must register (economic nexus) | `us-sales-tax-nexus-50-state-matrix` |
| Item-by-item taxability (food, clothing, software, SaaS, manufacturing) | Not confirmed in this version: see "Not yet confirmed" |
| Withholding on the same SUW return | `mi-payroll` |
| Michigan corporate income tax | `mi-corporate-income-tax` |

## Ask the client first

1. What is sold, to whom (final consumer or reseller), and is it delivered in Michigan?
2. Is the client registered and holding a current Michigan sales tax licence?
3. For residential customers: is the sale electricity, gas or home heating fuel?
4. For purchases: did the seller charge Michigan tax, another state's tax, or none?
5. What SUW filing frequency has Treasury assigned?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| Sales tax, retail sales of tangible personal property to the final consumer | 6% of the total price of taxable retail sales | [Treasury, Sales and Use Taxes](https://www.michigan.gov/taxes/business-taxes/sales-use-tax) |
| Sales tax, electricity, natural or artificial gas and home heating fuels for residential use | 4% | same |
| Use tax | 6% of the total price of taxable items brought into Michigan or bought from out-of-state retailers that do not collect | same |
| Local sales or use tax | None: cities and local units may not impose either | same |
| Sales tax licence | Valid January 1 to December 31 | same |
| Monthly return | 20th of the following month | same |
| Quarterly return | April 20, July 20, October 20, January 20 | same |
| Annual return | February 28 of the following year, for every filer | same |
| Accelerated payers | Pre-payment by the 20th of the current month and a reconciliation payment by the 20th of the next | same |

### Step 1: is the sale taxable?

1. A retail sale of tangible personal property to the final consumer is taxable at 6% unless an exemption applies. Check exemptions against the General Sales Tax Act before relying on one (not confirmed in this version).
2. Residential electricity, gas and home heating fuel: 4%.
3. A sale for resale is not a retail sale to the final consumer; keep the buyer's exemption claim.

### Step 2: register

1. Register with Treasury (Michigan Treasury Online) to receive a sales tax licence before selling; the licence runs for the calendar year.

### Step 3: collect and report

1. Charge 6% (or 4%) of the total price. Do not add any city or county tax.
2. On each return report gross sales, taxable and non-taxable together, then the deductions down to taxable sales (Filing Requirements FAQ; Form 5095 worksheet).
3. File on the frequency Treasury assigns, even if no tax is due. Sales, use and withholding share one frequency and one return.

### Step 4: use tax on purchases

1. When the client buys taxable goods without Michigan tax (from an out-of-state seller that did not collect, or brought into Michigan), it owes 6% use tax.
2. Credit is given for sales or use tax paid to another state.
3. Use tax also applies to certain services, including telecommunications and hotel and motel accommodations.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| A Detroit store sells a USD 1,000 table | 6%, USD 60; no Detroit sales tax exists | Treasury, Sales and Use Taxes |
| Home heating oil delivered to a house | 4% | same |
| Electricity for a factory (not residential) | Not the residential 4% rate; check the Act for any industrial exemption | same |
| Business buys USD 5,000 of equipment online, no tax charged | 6% use tax, USD 300 | same |
| Same purchase with 4% tax paid to another state | 2% Michigan use tax after credit | same |
| Hotel stay in Michigan | Use tax applies to accommodations | same |
| No sales in a quarter | Still file the return | Filing Requirements FAQ |
| Missed quarterly returns, client wants to file only the annual | Not allowed; the annual return reconciles, it does not replace | Filing Requirements FAQ |

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| Whether a buyer is reselling | Charge tax unless an exemption claim is held |
| Whether a utility sale is residential | Use 6% |
| Whether another state's tax was paid | No credit until shown |

### Red flags to raise with the client

- Invoices showing a "Michigan local" or city sales tax: none exists.
- A business with heavy out-of-state online purchases and no use tax on its returns.
- Returns not filed on Treasury's assigned frequency.

## Worked cases

**Case 1, retail sale and a residential fuel sale.** A Michigan retailer sells furniture for USD 1,000 and, separately, home heating fuel for USD 2,400 to a household. Sales tax: USD 1,000 x 6% = USD 60, and USD 2,400 x 4% = USD 96. Total USD 156.

```oa-check
name: Michigan sales tax, general and residential fuel rates (2026)
inputs:
  furniture: 1000
  heating_fuel: 2400
steps:
  - tax_furniture: furniture * 0.06
  - tax_fuel: heating_fuel * 0.04
  - total_tax: tax_furniture + tax_fuel
expected:
  tax_furniture: 60.00
  tax_fuel: 96.00
  total_tax: 156.00
```

**Case 2, a decision: does the client owe Michigan use tax?** A Michigan company buys USD 5,000 of equipment from a seller in another state for use in Michigan. The seller charged that state's 4% tax (USD 200). Without credit the Michigan use tax would be USD 300; with credit for the other state's tax it is USD 300 - USD 200 = USD 100. Decision: yes, report USD 100 of use tax and keep the invoice showing the other state's tax. Had the seller charged nothing, the full USD 300 would be due.

```oa-check
name: Michigan use tax with credit for another state (2026)
inputs:
  price: 5000
  mi_rate: 0.06
  other_state_rate: 0.04
steps:
  - mi_use_tax: price * mi_rate
  - other_state_tax: price * other_state_rate
  - use_tax_due: max(mi_use_tax - other_state_tax, 0)
expected:
  mi_use_tax: 300.00
  other_state_tax: 200.00
  use_tax_due: 100.00
```

## When to refuse or refer

| Situation | Action |
|---|---|
| Whether a specific product or service is exempt | Refer to the General Sales Tax Act and Treasury guidance; not confirmed here |
| Remote seller nexus | `us-sales-tax-nexus-50-state-matrix` |
| Audit, assessment or voluntary disclosure | Refer to a Michigan sales tax specialist |
| Penalty and interest computation | Use Treasury's penalty and interest calculator; rates not confirmed here |

## Filing and payment

1. Register on Michigan Treasury Online and get the sales tax licence.
2. File each SUW return by the 20th after the period (quarters: April 20, July 20, October 20, January 20) and pay with it on MTO.
3. File the annual return by February 28 of the next year.
4. A due date on a weekend or state holiday moves to the next business day.
5. Amend with Form 5092 (monthly or quarterly) or Form 5082 (annual), completing only the tax being amended.

## Completion checklist

- [ ] Licence current for 2026.
- [ ] 6% on taxable retail sales; 4% only on residential electricity, gas and heating fuel.
- [ ] No local tax added.
- [ ] Use tax accrued on untaxed purchases, with credit for other states' tax.
- [ ] Gross sales reported including non-taxable sales.
- [ ] Returns on the assigned frequency; annual return by February 28.

## Sources

| Source | URL | Read on |
|---|---|---|
| Sales and Use Taxes (Treasury). Read for the 6% and 4% rates, use tax, the local tax ban, the licence, due dates and accelerated payments. | https://www.michigan.gov/taxes/business-taxes/sales-use-tax | 2026-11-13 |
| Filing Requirements FAQ (Treasury). Read for nil returns, the calendar tax year, frequency, gross sales and amended returns. | https://www.michigan.gov/taxes/business-taxes/sales-use-tax/information/filing-requirements-faq | 2026-11-13 |
| Filing Frequency (Treasury). Read for how Treasury assigns the SUW frequency. | https://www.michigan.gov/taxes/business-taxes/payroll-service-providers/filing-frequency | 2026-11-13 |
| Filing and Payment Due Dates (Treasury). Read for the monthly, quarterly and annual due dates. | https://www.michigan.gov/taxes/business-taxes/payroll-service-providers/filing-and-payment-due-dates | 2026-11-13 |

Not yet confirmed: the remote seller economic nexus threshold (the old version said $100,000 or 200 transactions; MCL 205.52b and Treasury's remote seller page could not be opened); Streamlined Sales Tax membership; the taxability of grocery food, prepared food, clothing, prescription drugs, prewritten and downloaded software, SaaS, professional services and industrial processing equipment; the dollar thresholds for monthly, quarterly and annual filing; penalty and interest rates.
