---
name: ma-sales-tax
description: "Work out Massachusetts sales and use tax for 2026. Covers the 6.25% state rate, the clothing rule (tax only on the part of an item over $175), exempt grocery food, the meals tax and local option, taxable prewritten software including remote access, untaxed electronically delivered digital products, telecommunications, the $100,000 remote seller and marketplace threshold, resale certificates, use tax, filing frequency by liability and the advance payment rule. Trigger on \"Massachusetts sales tax\", \"MA sales tax\", \"MA use tax\", \"ST-9\", \"ST-4\", \"Massachusetts clothing exemption\", \"Massachusetts SaaS tax\". Load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ma-sales-tax"
  jurisdiction: "US-MA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Massachusetts sales and use tax, tax year 2026

> **Source-cited draft.** Built from the Massachusetts Department of Revenue (DOR) Guide to Sales and Use Tax and the DOR tax rates page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Massachusetts charges **6.25%** sales tax on sales and rentals of tangible personal property and telecommunications services, and the same **6.25%** use tax on items bought tax-free for use in the state. There are no local sales taxes on goods; cities and towns may add a local option tax on restaurant meals only. Clothing items of **$175** or less are exempt, and a dearer item is taxed only on the amount above $175. Grocery food is exempt. Prewritten software is taxed however it is delivered, including access on a remote server; other digital products delivered electronically (music, video, reading material) are not. A remote seller or marketplace must register once Massachusetts sales pass **$100,000** in a calendar year.

## Scope

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts (US-MA), [DOR](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Law | M.G.L. c. 64H (sales tax), c. 64I (use tax), c. 62C (administration), [DOR guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Portal | [MassTaxConnect](https://mtc.dor.state.ma.us/mtc/_/) |
| Returns | Form ST-9 (goods), Form STS (services), ST-10 and ST-11 (use tax), [DOR guide](https://www.mass.gov/guides/sales-and-use-tax) |

Covers vendors selling goods, software and telecommunications into or within Massachusetts, and businesses and individuals owing use tax. Not covered here: room occupancy excise and short-term rental fees, the marijuana excise, motor vehicle sales through the Registry, and the meals tax detail beyond the rate. The multistate nexus and marketplace framework is in `us-sales-tax` and `us-sales-tax-nexus-50-state-matrix`.

## Ask the client first

1. What is sold: goods, clothing, food, restaurant meals, software (downloaded, boxed or hosted), digital products, telecommunications, services?
2. Where the business is and what it does in Massachusetts (staff, stock, deliveries, installations, solicitors).
3. For a remote seller or marketplace: Massachusetts sales in 2025 and 2026 to date.
4. Whether buyers give resale or exemption certificates.
5. Last year's total sales tax liability (sets filing frequency and the advance payment rule).
6. Untaxed purchases used in Massachusetts (use tax).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Condition | Source |
| --- | --- | --- | --- |
| Sales tax rate | 6.25% | Sales or rentals of tangible personal property, including gas, electricity and steam, and telecommunications services | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Use tax rate | 6.25% | Property or telecommunications bought without Massachusetts tax for use in the state, including internet and mail order purchases and electronically transferred software | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Meals, prepared food and beverages | 6.25%, plus a local option tax where the city or town has adopted it | Restaurant food and on-premises consumption of any beverage | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Clothing | Exempt up to $175 per item; tax on the amount over $175 | Each item separately, whatever the bill total | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Remote seller and marketplace threshold | More than $100,000 of Massachusetts sales in a calendar year | Remote sales, or direct plus facilitated sales for a marketplace | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Annual filing | Liability of $100 or less | Return due 30 days after the year | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Quarterly filing | Liability from $101 up to $1,200 | Return due 30 days after the quarter | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Monthly filing | Liability of $1,201 or more | Return due 30 days after the month | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Advance payments | Required above $150,000 of cumulative tax liability in the prior year | Under G.L. c. 62C, s. 16B | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Interest on late payment | Federal short-term rate plus 4%, compounded daily | Unpaid tax | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Marijuana retail sales | 6.25% sales tax, 10.75% state excise, up to 3% local option | Adult use marijuana | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |

### Step 1. Is there a duty to register?

A business must register and collect if it sells, rents or leases tangible property or telecommunications in Massachusetts, buys for resale, has representatives soliciting orders in the state, delivers, repairs or installs in the state, or is a remote seller or marketplace above $100,000 of Massachusetts sales in a calendar year. New businesses register, file and pay electronically through MassTaxConnect.

### Step 2. Is each sale taxable?

| Pattern | Treatment |
| --- | --- |
| General tangible goods | Taxable at 6.25% |
| Clothing item $175 or less | Exempt |
| Clothing item over $175 | Taxable on the amount over $175 only |
| Grocery food for human consumption | Exempt |
| Restaurant meals and prepared food | Taxable at 6.25%, plus any local option meals tax |
| Prewritten (standardized) software, downloaded or physical | Taxable |
| Charges to access or use software on a remote server (SaaS) | Taxable |
| Software given with no charge where the customer really buys other goods or services | Not taxed |
| Music, video, reading material and other non-software digital products delivered electronically | Not taxed |
| Telecommunications services (phone, cellular) | Taxable |
| Cable television and internet access | Exempt |
| Professional and personal services not listed as taxable | Not taxed |
| Sales for resale to a registered vendor with Form ST-4 | Exempt |

### Step 3. Compute the tax

Taxable sales times 6.25%. For clothing, the taxable amount per item is the price less $175, never below zero. For restaurant meals, add the local option rate where adopted.

### Step 4. File and pay at the right frequency

Set the frequency from the year's liability (annual, quarterly, monthly), file Form ST-9 (goods) or STS (services) on MassTaxConnect, and pay with the return. Vendors over $150,000 of prior-year liability also make advance payments.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Customer did not pay yet | Vendor owes tax on the sale anyway; relief for bad debts comes only through the annual Form ST-BDR | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Buyer without Massachusetts nexus wants to buy for resale | Vendor cannot take Form ST-4 from it, but may take a signed statement on the buyer's letterhead (Directive 89-10) | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Drop shipment for a retailer with no Massachusetts nexus | The shipper with nexus collects; may accept a notarized letterhead statement instead of ST-4 | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Resale certificate for tobacco products | Invalid | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Software used in more than one state | Tax may be apportioned through an abatement request | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Business with untaxed purchases and no vendor registration | Form ST-10, due annually by April 15 | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Individual with untaxed purchases | Form ST-11, due annually by April 15, filed electronically | [DOR sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| No resale certificate on file | Treat the sale as taxable |
| Software delivery method unclear | Taxable either way if it is prewritten software |
| Clothing price per item not split out | Ask for the per-item prices; do not apply the $175 rule to the bill total |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Remote seller close to $100,000 of Massachusetts sales | Registration duty starts once the threshold is passed |
| Charging tax on downloaded music or e-books | Not taxable in Massachusetts, refund risk to customers |
| Not charging tax on SaaS | Remote software access is taxable |
| Restaurant in a town with the local option | Extra local meals tax due |

## Worked cases

**Case 1, a suit over the clothing limit.** A shop sells one suit for USD 200 and a shirt for USD 60 on one receipt. The shirt is exempt. The suit is taxed on USD 25, the amount over USD 175, so the tax is USD 1.56 (DOR's own example).

```oa-check
name: Clothing items against the 175 dollar limit
inputs:
  suit_price: 200
  shirt_price: 60
  limit: 175
  rate: 0.0625
steps:
  - suit_taxable: max(suit_price - limit, 0)
  - shirt_taxable: max(shirt_price - limit, 0)
  - tax: round((suit_taxable + shirt_taxable) * rate, 2)
expected:
  suit_taxable: 25.00
  shirt_taxable: 0.00
  tax: 1.56
```

**Case 2, decision: register as a remote seller, and how often to file?** An out-of-state online seller had USD 120,000 of Massachusetts sales in 2026, of which USD 96,000 is taxable goods and USD 24,000 exempt clothing under USD 175 per item. Sales passed USD 100,000, so it must register. Annual tax is USD 6,000. That is above USD 1,200, so it files monthly; average monthly tax is USD 500. Had Massachusetts sales been USD 95,000, it would be below the threshold and not required to register on that test.

```oa-check
name: Remote seller threshold and filing frequency
inputs:
  ma_sales: 120000
  taxable_sales: 96000
  threshold: 100000
  rate: 0.0625
  monthly_floor: 1201
steps:
  - over_threshold: max(ma_sales - threshold, 0)
  - annual_tax: taxable_sales * rate
  - margin_above_monthly_floor: annual_tax - monthly_floor
  - average_monthly_tax: annual_tax / 12
expected:
  over_threshold: 20000.00
  annual_tax: 6000.00
  margin_above_monthly_floor: 4799.00
  average_monthly_tax: 500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| REF-MAST-01 | Room occupancy, short-term rental community impact fee or convention center taxes | Refer: outside this skill |
| REF-MAST-02 | Marijuana retail taxes beyond the rates | Refer |
| REF-MAST-03 | Mixed software and services bundles (830 CMR 64H.1.3) | Flag for reviewer |
| REF-MAST-04 | Audit, dispute or abatement | Refer |

## Filing and payment

- Register on MassTaxConnect before the first taxable sale or once the remote threshold is passed.
- File Form ST-9 (goods) or STS (services) annually, quarterly or monthly by the 30th day after the period, and pay with the return. All new businesses file and pay electronically.
- Amend through the "amend" feature in MassTaxConnect.
- Use tax returns ST-10 and ST-11 are due by April 15.

## Completion checklist

- [ ] Registration duty tested, including the $100,000 remote threshold.
- [ ] Every product line mapped to taxable, exempt or not taxed.
- [ ] Clothing tested per item at $175.
- [ ] Local option meals tax applied where adopted.
- [ ] Resale certificates (ST-4) on file for exempt resales.
- [ ] Filing frequency matches liability; advance payments if over $150,000.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR, A Guide to Sales and Use Tax. Read for the 6.25% rates, $175 clothing rule and $200 suit example, food, software and digital products, telecommunications, $100,000 remote seller rule, filing frequencies, $150,000 advance payments, resale, ST-BDR, ST-10 and ST-11, interest. | https://www.mass.gov/guides/sales-and-use-tax | 2026-11-13 |
| DOR, Tax Rates (updated 30 Dec 2025). Read for the meals tax and local option, marijuana rates. | https://www.mass.gov/info-details/massachusetts-tax-rates | 2026-11-13 |

Not yet confirmed: the local option meals tax rate (set out in TIR 09-13, not read) and the list of towns that adopted it; Massachusetts sales tax holiday dates for 2026, not read; the treatment of manufacturing machinery and prescription drugs (exempt in the old file) was not on the pages read, so it is left to `us-sales-tax` and a reviewer.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ma-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ma-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
