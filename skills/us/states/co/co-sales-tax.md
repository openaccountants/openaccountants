---
name: co-sales-tax
description: >
  Colorado 2026 state and state-administered sales/use tax for physical-presence,
  remote and marketplace sellers. Covers nexus, sourcing, software, exemptions,
  DR 0100 filing and the boundary with self-collecting home-rule cities.
  Load us-sales-tax first; delivery fees and SUTS have a separate owner.
version: 2.1
jurisdiction: US-CO
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
depends_on:
  - us-sales-tax
---

# Colorado sales and use tax v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Retailers making Colorado sales during 2026. State and state-administered local
obligations and each self-collecting home-rule city's obligations are distinct.
A state exemption does not establish a home-rule exemption.

Load `us-sales-tax` for the federal framework. `co-retail-delivery-and-suts` owns
retail delivery fees and SUTS operations; `co-income-tax`, `co-corporate-tax` and
`co-payroll` own their separate jobs. This skill does not set a combined local rate.

## Ask the client first

1. Physical locations, inventory, workers, events and other Colorado presence.
2. Current/prior calendar-year Colorado sales, separating direct, qualified facilitated and wholesale sales.
3. Products, software delivery/licence terms and exemption certificates.
4. Customer receipt location and exact delivery address.
5. State/home-rule accounts, assigned periods and prior gross sales/tax liability.
6. Whether a qualifying facilitator actually collects the tax on each channel.

## Rates, bands and thresholds

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| State sales/use rate | 2.9%; local taxes are additional and product/address dependent | https://tax.colorado.gov/sales-tax-guide |
| Remote economic nexus | Colorado retail sales exceeding $100,000 in current or preceding calendar year; physical presence is separate | https://tax.colorado.gov/sales-tax-guide |
| Current-year crossing | Begin collection first day of first month commencing at least 90 days after crossing; a preceding-year crossing requires collection throughout current year | https://tax.colorado.gov/sales-tax-guide |
| Quarterly eligibility | Monthly tax collected less than $1,100 and more than $50; use assigned frequency | https://tax.colorado.gov/sales-tax-guide |
| Annual eligibility | Monthly tax collected $50 or less; use assigned frequency | https://tax.colorado.gov/sales-tax-guide |
| Return/payment deadline | 20th following assigned monthly, quarterly or annual period; next business day on weekend/holiday | https://tax.colorado.gov/sales-tax-guide |
| Mandatory e-filing | From January 2026, prior-year annual gross sales of goods/services of $500,000 or more before deductions | https://tax.colorado.gov/sales-tax-guide |
| Mandatory EFT | Prior-year state sales tax liability greater than $75,000; exclude local liability | https://tax.colorado.gov/sales-tax-guide |
| State vendor service fee | None for periods beginning on/after January 1, 2026; local allowance may differ | https://tax.colorado.gov/sales-tax-guide |
| Late-payment penalty | 10% plus 0.5% per month, maximum 18%; interest separate | https://tax.colorado.gov/sales-tax-guide |
| 2026 interest | Regular 11%; discounted 8% if DOR payment conditions met | https://tax.colorado.gov/sales-tax-guide |
| Manufacturing machine price test | More than $500 plus all other exemption conditions, not price alone | https://tax.colorado.gov/sales-use-tax-topics-manufacturing |

## The method, step by step

1. **Establish collection liability.** Physical presence includes locations,
   inventory, employees and selling events. Do not apply the remote safe harbour
   to an in-state seller. For remote-only sellers, include taxable and exempt
   Colorado retail sales. DOR's economic test has no transaction-count trigger.
2. **Separate facilitated sales.** Marketplace-only sellers need no own licence
   for sales for which a qualifying facilitator collects. For multichannel
   sellers, the DOR marketplace publication excludes qualified facilitated sales
   from the seller's direct-sales economic threshold. Retain the certification/
   agreement and collection records. Physical presence remains a separate test.
   Source: https://tax.colorado.gov/sites/default/files/SUTT_Marketplaces.pdf,
   marketplace-seller provisions, pages 6-7.
3. **Source to receipt.** Counter pickup generally sources to the retailer;
   delivery to where the purchaser or designated recipient receives it. If
   receipt location is unknown, use the DOR's ordered address/records fallbacks.
   A ZIP code alone does not establish a combined rate.
4. **Classify the transaction.** Ordinary tangible property, including clothing,
   is generally taxable absent exemption. Digital goods can be taxable, with
   software separately treated below. Services generally are not taxable, but
   enumerated utility/telephone services are exceptions. Prepared food and
   short-term lodging have their own rules.
5. **Test delivery charges twice.** Exclusion requires both a separable delivery
   service and a separately stated charge. A separate invoice line alone is
   insufficient. Apply the separate delivery-fee skill to any motor delivery.
6. **Apply state and local layers.** Use the exact address, product and date in
   the DOR lookup/certified database. Preserve evidence of proper use to support
   any database protection. State-administered local exemptions can differ from
   state exemptions. Check each self-collecting city's law/account separately.
7. **Register.** Apply through MyBizColorado or CR 0100 for the sales account/
   licence and licensed locations. DOR licences expire December 31 of odd years.
   Revenue Online handles state filing; SUTS is explained by its separate owner.
8. **Prepare DR 0100.** Reconcile site/period gross sales, deductions, exemptions,
   taxable sales and each jurisdiction's tax. Use actual current instructions
   for exact lines; final 2026 line mapping has not been fully checked here.
   Deduct no state vendor fee. Save submission confirmation and separately
   match payment amount, account, period and receipt. Use the assigned cycle.
9. **Address consumer use tax.** Untaxed taxable purchases used in Colorado can
   create use tax. The 2025-2026 filing cycle Book 104 cover discontinues
   DR 0104US and directs consumers to DR 0252. State consumer use tax DR 0251/
   DR 0252 is not filed through SUTS. Local use tax is a separate system;
   motor-vehicle/construction exceptions need their specific instructions.

Method source: https://tax.colorado.gov/sales-tax-guide. Consumer-use boundary:
https://tax.colorado.gov/SUTS-FAQ and
https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf (cover).

### Transaction patterns

| Pattern | State/state-administered rule | Official source |
|---|---|---|
| Ordinary goods/clothing | Generally taxable unless documented exemption | https://tax.colorado.gov/sales-tax-guide |
| Grocery food | Qualifying home-consumption food can be exempt; prepared food, candy, soft drinks and exclusions differ; SNAP/WIC and local options matter | https://tax.colorado.gov/sites/default/files/Sales%204.pdf |
| Prepared food | Generally taxable, subject to the publication's specific exceptions | https://tax.colorado.gov/sites/default/files/Sales%204.pdf |
| Downloaded software, application-service-provider access, load-and-leave | Exempt under 2026 software rule; January 2027 change is separate | https://tax.colorado.gov/sales-use-tax-topics-computer-software |
| Prepackaged software | Taxable in 2026 only if prepackaged, nonnegotiable tear-open licence and tangible-media delivery, all required | https://tax.colorado.gov/sales-use-tax-topics-computer-software |
| Professional services | Generally not state taxable; enumerated services/home-rule law can differ | https://tax.colorado.gov/sales-tax-guide |
| Manufacturing machinery | Colorado use, price condition above, historic investment-credit qualification, direct/predominant manufacturing use for property sold for profit, all required | https://tax.colorado.gov/sales-use-tax-topics-manufacturing |
| Manufacturing ingredients | Must enter finished product; manufacturing aids not automatically ingredients | https://tax.colorado.gov/sales-use-tax-topics-manufacturing |
| Prescription drugs | Qualifying prescribed/dispensed drugs exempt; practitioner-furnished rules separate | https://tax.colorado.gov/sites/default/files/documents/SUTT_Medical_Exemptions_July_2022.pdf |
| OTC drugs | Generally taxable retail purchases even if recommended; practitioner-furnished drugs and specific items have exceptions | https://tax.colorado.gov/sites/default/files/documents/SUTT_Medical_Exemptions_July_2022.pdf |
| Resale | Genuine resale with valid exemption support; own consumption is not resale | https://tax.colorado.gov/sales-tax-guide |

The food PDF is a historical DOR publication still linked in current guidance,
not a newly issued 2026 form. Local food, medical and software rules need their
own check. Do not repeat the old blanket OTC exemption or downloaded-software tax.

## Worked cases

### Delivery charge conditions, worked both ways

An invented retailer sells $1,000 of state-taxable goods and charges $20 delivery.
If delivery is both separable and separately stated, state tax is $29. If it is
inseparable, state tax is $29.58, a $0.58 difference. Actual contract facts control;
renaming the charge does not elect an exemption. Local tax and delivery fees are separate.

```oa-check
name: Colorado 2026 delivery charge conditions
inputs:
  goods: 1000
  delivery: 20
  rate: 0.029
steps:
  separable_state_tax: goods * rate
  inseparable_state_tax: (goods + delivery) * rate
  difference: inseparable_state_tax - separable_state_tax
expected:
  separable_state_tax: 29
  inseparable_state_tax: 29.58
  difference: 0.58
```

### Manufacturing versus office use

A $10,000 machine satisfies every published manufacturing condition in one scenario
and is general office equipment in another. Assuming no other exemption, state tax
is zero for the qualifying machine and $290 for office use. Local results are separate.

```oa-check
name: Colorado machinery use conditions
inputs:
  cost: 10000
  state_rate: 0.029
steps:
  qualified_state_tax: cost * 0
  office_state_tax: cost * state_rate
  difference: office_state_tax - qualified_state_tax
expected:
  qualified_state_tax: 0
  office_state_tax: 290
  difference: 290
```

## Checks before finalising

- Test physical presence and current/prior sales before the remote exception.
- Separate direct/facilitated channels, state/local layers and delivery-fee accounts.
- Match software conditions to 2026, not the January 2027 amendment.
- Verify certificates, date, exact address and each applicable local exemption.
- Reconcile gross sales, deductions, tax and payment; remove the state vendor fee.

## When to refuse or refer

Refer unresolved nexus, self-collecting home-rule law, mixed transactions,
manufacturing qualification, motor vehicles, construction and special excises.
Do not quote an unsourced statewide maximum rate, city count or SST membership.

## Sources

| Source | URL | Reading scope | Read on |
|---|---|---|---|
| DOR sales tax | https://tax.colorado.gov/sales-tax-guide | Read for sourcing, nexus, shipping, filing thresholds, 2026 e-filing/vendor-fee change, EFT, penalties and local boundaries | 2026-11-13 |
| DOR software | https://tax.colorado.gov/sales-use-tax-topics-computer-software | Read for all 2026 software conditions and exemptions, separately effective 2027 change | 2026-11-13 |
| DOR medical | https://tax.colorado.gov/sites/default/files/documents/SUTT_Medical_Exemptions_July_2022.pdf | Read for pages 1-2 prescribed, practitioner-furnished and OTC rules; not all device categories | 2026-11-13 |
| DOR food | https://tax.colorado.gov/sites/default/files/Sales%204.pdf | Read for pages 1-3 home food, exclusions, SNAP/WIC and local differences; historical issue | 2026-11-13 |
| DOR manufacturing | https://tax.colorado.gov/sales-use-tax-topics-manufacturing | Read for ingredients/aids and all basic machinery conditions | 2026-11-13 |
| DOR marketplaces | https://tax.colorado.gov/sites/default/files/SUTT_Marketplaces.pdf | Read for pages 6-7 seller registration, direct-sales threshold and evidence | 2026-11-13 |
| DOR SUTS FAQ | https://tax.colorado.gov/SUTS-FAQ | Read for state consumer-use forms excluded from SUTS and separate fee/amendment handling | 2026-11-13 |
| DOR Book 104, 2025-2026 filing cycle | https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf | Read for cover discontinuing DR 0104US in favour of DR 0252, not final 2026 return mapping | 2026-11-13 |

Not yet confirmed: final 2026 DR 0100 line mapping, current address-specific DR 1002 rates, each home-rule city's software/food/medical law, complete exemption-document retention and specialist vehicle/construction/use-tax treatment. Old maximum combined rate, national-lowest claim, approximate city count and SST-associate assertion remain unverified and must not be used.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
