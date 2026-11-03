---
name: cf-property-tax
description: >
  Use this Central African Republic property Guide for 2026 research on the built-property contribution, rental-value floor, owner and tenant declarations and the separate personal rental-income base. It distinguishes the building levy from income tax, VAT and capital gains, preventing the same percentage from being applied to the wrong base. Search triggers include contribution foncière, F66, F67, F61 bis, rental property, landlord, principal home and property value. These are conditional provisions read in the Ministry’s official 2023 code, not an authenticated complete current consolidation. Unbuilt land, transfers, succession and live filing instructions remain outside the verified scope.
jurisdiction: CF
category: international
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
---

# Central African Republic built-property contribution and rent base v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** Owners and tenants of CAR built property, including the particular statutory exemption/ownership cases. The ordinary baseline cannot be used as final 2026 law without clearing its currentness hold. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

Built-property contribution applies annually to masonry-founded houses, factories, shops, hangars and factories, with attached industrial plant under article 168 and exemptions in article 169. It is distinct from income tax on rent and VAT. [CGI arts. 167–169](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B01).

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| Rate is 15% for individuals and legal persons not subject to IS, or 30% for IS-liable legal persons; nearest-XAF-10 rounding and XAF 30,000 minimum. Establish the taxpayer category and exemption first; this is not an across-the-board tax on market value. | 2026 research scope; CGI art. 177 [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger B03 |

## The base

Built-property base is rental value less a 40% allowance for deterioration, maintenance and repairs. Rental value is determined annually with the property position at 1 January and cannot be below 12% of market value or fixed-asset cost; round the base down to XAF 1,000. [CGI arts. 170–172](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B02).

The article 169 exemptions include the first residential property occupied as the owner/family’s principal home. Other exemptions have public-purpose, ownership, location or non-income conditions. A first-home exemption is not an exemption for all rental properties. [CGI art. 169(12)](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B04).

Individual net property income is gross rents less the statutory 40% charge allowance. Gross rents include tenant-borne owner expenses and relevant subsidies/indemnities, less landlord-borne tenant expenses. This category calculation is separate from the annual built-property contribution and does not alone establish final IRPP. [CGI arts. 14–16](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B08).

Identify the property and liable person at the statutory date, then test exemptions. Establish rental value from the stated statutory methods and value floor, apply the allowance, round the base and apply the correct taxpayer-category rate and minimum. For rental income, separately compute the individual category base and then classify the final tax/withholding through [individual tax](cf-income-tax.md) and [cross-border](cf-cross-border.md). Do not offset building contribution against rental tax without authority.

## Deadlines and filing

Each owner/debtor, including statutory exemption beneficiaries, submits one administration form per property before 1 February, model F66. The administration’s rental-value notice model F61 bis has a twenty-day approval/correction response. Current forms themselves were not fetched. [CGI arts. 171, 173](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B05).

Tenants, including diplomatic/consular and international bodies, file the specified landlord/property/rent statement before 15 January, model F67. Failure to declare rent timely can also deny the tenant’s income-tax deduction. [CGI art. 174](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B06).

The liable owner is identified at 1 January; usufruct, emphyteutic lease and building-on-another’s-land rules allocate liability differently. Assessment is at the property’s location, and payment is due by 31 March. [CGI arts. 175–177 bis](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger B07).

Obtain the current owner/tenant forms and prefilled valuation notice from the competent property-location office, verify values and respond with proof. Preserve submission acknowledgement and payment receipt. The named form references are taken from the law; actual current boxes, channel and payment instructions were not opened.

## Penalties and interest

CGI article 173 provides a specific late/non-declaration uplift, and article 177 bis a specific late-payment penalty, but their priority against the new LPF has not been reconciled. No final penalty total is presented; use [tax overview](cf-tax-overview.md) for the directly read general procedure provisions.

## Cross-border points

Property location, owner status and treaty rules can differ from personal residence. Nonresident withholding, land-rich-company capital gains and transfer taxes require separate verification; no flat foreign-owner CGT rate is supplied.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. Market-value floor changes the tax base

Assume a non-exempt individual building, market value XAF 20,000,000, actual assessed rent XAF 1,800,000, and the quoted baseline applies. The 12% floor is 2,400,000, so that rental value controls. After the 40% allowance the base is 1,440,000; at 15% the levy is 216,000, above the minimum.

```oa-check
name: Market-value floor changes the tax base
inputs:
  market: 20000000
  rent: 1800000
steps:
  - rental_value: max(rent,market*0.12)
  - base: floor(rental_value*0.60/1000)*1000
  - tax: max(round(base*0.15/10)*10,30000)
expected:
  rental_value: 2400000
  base: 1440000
  tax: 216000
```

### 2. Individual or IS company rate on the same building

Assume identical non-exempt rental value XAF 2,400,000 and no currentness issue. The rounded base is 1,440,000. An individual rate gives 216,000; an IS company rate gives 432,000. The ownership decision therefore needs the taxpayer-category test and the other taxes, not just market value.

```oa-check
name: Individual or IS company rate on the same building
inputs:
  rental_value: 2400000
steps:
  - base: floor(rental_value*0.60/1000)*1000
  - individual: max(round(base*0.15/10)*10,30000)
  - company: max(round(base*0.30/10)*10,30000)
  - difference: company-individual
expected:
  individual: 216000
  company: 432000
  difference: 216000
```

## Ask the client first

- Built or unbuilt property, location and use?
- Owner, usufructuary, lessee or builder on another’s land at the relevant date?
- Principal-home or other statutory exemption facts?
- Rental and market/cost values with supporting lease and valuation evidence?
- Individual or company taxpayer, prior forms/notices and rent paid/received?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| DGID official CGI edition marked updated 2023 (cover also says mise à jour 2022) | https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf | 2026-11-01; Read cited articles and neighbouring scope/definitions/exceptions; not all 442 pages. Mixed edition dates and later-law consolidation unresolved. |

Not yet confirmed: Later amendments/current property valuation instructions; unbuilt-land contribution, capital gains, registration/stamp/transfer and succession taxes; full exemptions and provisional exemptions; current F61 bis/F66/F67 forms and procedures; special/general penalty priority; how category rent income and final withholding interact for the actual recipient.
