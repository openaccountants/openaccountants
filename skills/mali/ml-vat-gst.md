---
name: ml-vat-gst
description: >
  Mali VAT research draft for 2026, using the older DGI tax-code and procedure-code text while holding the operative current amendment chain unresolved. Use it to prepare conditional domestic VAT workpapers for registration classification, standard and reduced rates, exports and exemptions, tax-exclusive consideration, goods and services tax points, input-tax restrictions, mixed-use allocations and the real-normal versus real-simplified filing distinction. It corrects the former Guide's blanket monthly-return statement and its simplified zero-rate and imported-services descriptions. Two executable examples test output/input tax and mixed-use deduction arithmetic. Current tariff lists, amendments, refund procedures, official forms and authenticated portal steps remain unverified. No current-law approval or accountant attestation is claimed.
jurisdiction: ML
category: international
tax_year: 2026
tax_year_notes: "2026 research draft only; older DGI source baseline, operative 2026 amendment chain unproved."
version: 0.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mali VAT source-reference draft v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft; operative 2026 law is unproved.** This is a conditional source-reference workpaper, not an approved current-law computation. The DGI online consolidation contains amendments labelled through 2017 in the provisions used here. No complete later amendment chain or enacted 2026 fiscal Annex U has been reconciled. Read every rule below as a statement of that identified source baseline, not proof it applies unchanged in 2025 or 2026. Do not calculate a client's 2026 liability or instruct a 2026 filing from this draft. The current-year metadata identifies the research job; it is not evidence of currentness or a technical retrieval/publication safeguard.

## Who this applies to

The older code taxes independent economic supplies for consideration in Mali and imports. Ordinary taxable activities include sales, services, construction and self-supplies under their conditions. Article 192 lists compulsory categories at tax-exclusive annual turnover of at least XOF 50 million; importers are included regardless of turnover. Do not treat that threshold as a universal importer exemption. [CGI arts. 186–194](https://www.dgi.gouv.ml/CGI/).

Real-normal and real-simplified VAT modes refer to the business-regime provisions. Establish the actual mode before choosing a filing/payment calendar; the [corporate Guide](ml-corporate-income-tax.md) records the source regime thresholds and exceptions. Synthetic-regime persons must not charge VAT on their invoices merely because a customer requests it. [CGI art. 186; LPF art. 115](https://www.dgi.gouv.ml/CGI/).

## Rates, bands and thresholds

| Item | Older DGI source baseline, not approved 2026 law | Official source |
|---|---|---|
| Ordinary non-exempt goods/services | 18% | [CGI art. 229, Loi 11-078](https://www.dgi.gouv.ml/CGI/) |
| Reduced-rate listed goods | 5%, only the goods/tariff entries in the designated point D list, including listed computer and solar-production equipment; not a generic reduced rate for all essentials | [CGI point D after art. 195 and art. 229](https://www.dgi.gouv.ml/CGI/) |
| Exports | Article 195.I.1 calls direct exports and specified assimilated operations exempt; art. 208 preserves deduction subject to its condition. Do not replace that legal structure with an unconditional 0% label | [CGI arts. 195.I.1, 208](https://www.dgi.gouv.ml/CGI/) |
| Exemptions | Specific lists/conditions: for example grains, raw meat, approved education, health/veterinary services, and financial/insurance operations under their specific taxes | [CGI art. 195.I–IV](https://www.dgi.gouv.ml/CGI/) |
| Liability threshold for listed categories | Tax-exclusive annual turnover at least XOF 50 million; importers regardless of turnover | [CGI art. 192, LF 2017](https://www.dgi.gouv.ml/CGI/) |
| General monthly return, real-normal | First fifteen days of next month, including nil returns | [LPF art. 110(2)](https://www.dgi.gouv.ml/CGI/) |
| Real-simplified | Annual regularisation by 15 May after closing; quarterly advances under art. 322(3), not identical to real-normal monthly returns | [LPF arts. 110(3), 322(3)](https://www.dgi.gouv.ml/CGI/) |
| Return tax rounding | Down to XOF 5 | [LPF art. 111](https://www.dgi.gouv.ml/CGI/) |

## The base

1. Classify each transaction's territorial location, exemption/tariff status and applicable mode before calculation. For sales, services and works the source uses the relevant consideration/contract amount; import base is its defined customs-border value. Other taxes and incidental charges enter the base unless a stated exception applies; qualifying direct price reductions, true damages and supported agent disbursements are excluded. Do not deduct the supplier's own expenses from sales. [CGI arts. 196, 198–203](https://www.dgi.gouv.ml/CGI/).
2. Separate the event creating the charge from when tax is payable. Goods generally follow delivery; ordinary services become payable on collection of price/advances. An authorised debit method cannot defer tax already triggered by an earlier collection. Works have their execution/earlier-receipt rule, and imports their release-to-consumption rule. Thus unpaid invoices cannot all be placed in one VAT month by a universal cash or accrual assumption. [CGI arts. 204–206](https://www.dgi.gouv.ml/CGI/).
3. Compute output tax by the supported class and period. Establish the current product classification before using the older reduced list; its computer/solar examples do not prove every modern product qualifies. [CGI point D and art. 229](https://www.dgi.gouv.ml/CGI/).
4. Reconcile deductible input tax to eligible taxable or qualifying export operations and proper evidence. Customs tax must appear on the release declaration/equivalent; domestic tax must be separately shown on the invoice. The invoice/NIF and actual transaction matter. Exclusions include private/personnel use, most passenger/mixed-use vehicles and related costs, subject to their explicit exceptions. Do not deduct every amount marked VAT. [CGI arts. 207–215, 225; LPF art. 115](https://www.dgi.gouv.ml/CGI/).
5. Allocate inputs exclusively supporting deductible operations fully, those exclusively supporting non-deductible operations at zero, and shared inputs under the source prorata. The fraction uses deductible-operation receipts over relevant total products, excludes specified capital disposals/capital subsidies/insurance/disbursement amounts and self-supplies, excludes VAT, and rounds the percentage upward to a whole unit. The provisional fraction is based on the prior year or new-business estimates, with subsequent regularisation. [CGI arts. 216–223](https://www.dgi.gouv.ml/CGI/).
6. Impute eligible input tax in its entitlement month, or by 15 May of the following year after an omission under the source rule. Excess deductions carry forward. Article 227 sets a requested quarterly refund route with eligibility restrictions, supporting evidence and potential targeted control; it is not an automatic payment. Current refund forms/procedures are unresolved. [CGI arts. 224–228](https://www.dgi.gouv.ml/CGI/).

## Deadlines and filing

The older source requires an existence declaration and registration request within ten days of starting taxable activity; NIF is necessary to invoke deduction rights. Mid-year liability changes and crossing the synthetic threshold have specific notification/tax-point rules, not retrospective assumed liability for every prior transaction. [CGI art. 194; LPF arts. 112–114](https://www.dgi.gouv.ml/CGI/).

Real-normal returns cover the previous month's operations within the first fifteen days of the following month, including nil periods; payment has an explicit next-working-day rule. Real-simplified has annual regularisation by 15 May and quarterly advances payable within fifteen days after the quarter, with its next-working-day rule. The older advance coefficients are 0.80% of quarterly taxable movable-goods turnover and 3% of taxable service turnover, deducting eligible fixed-asset VAT from the computed advance. Do not substitute the advance coefficient for the final VAT rate. [LPF arts. 110–111, 322](https://www.dgi.gouv.ml/CGI/).

Prepare the supported sales/tax-point schedule, input-tax/exclusion schedule, shared-cost fraction, credits/advances and payment reconciliation. The administration supplies the prescribed return; actual current form identifiers and boxes were not obtained. Obtain the current authorised route before submission and retain the filed return, acknowledgement and payment receipt. The older LPF requires receipts and recording of payment; that does not verify today's portal menus. Imports follow the customs route. [LPF arts. 110–116, 322–326](https://www.dgi.gouv.ml/CGI/). This is held source-reference preparation, not an instruction to file a 2026 return.

## Penalties and interest

In the older monthly-return rules, late filing before notice carries 25%, reduced to 5% where delay does not exceed one month; after notice the stated rate is 50%. The XOF 50,000 minimum applies in all these late-filing branches, including pre-notice 25% and 5%, rather than only after notice. Continued non-filing ten days after notice leads to official assessment and a 100% increase. A late nil return has XOF 50,000 penalty. These are separate branches, not simultaneous additions. [LPF art. 119](https://www.dgi.gouv.ml/CGI/).

Omissions/inaccuracies have 50% of tax compromised, or 100% if good faith cannot be accepted; abusive VAT invoicing has a separate double-tax fine. Late payment under article 328 adds 2% per month on the stated tax/penalty base, counting a fraction of a month as full and capped at 20%. The exact notice, assessment and source start-date cross-references must be examined before client calculation. Current amendments and all sanction combinations remain unresolved. [LPF arts. 120–122, 328–329](https://www.dgi.gouv.ml/CGI/).

## Cross-border points

The source locates goods by their presence at delivery/import/installation, works by execution and services by execution or use/exploitation in Mali. Services used abroad have stated immovable-property and event exceptions; without proof of an outside place, Mali is presumed. Export relief therefore needs classification and evidence, not merely a foreign customer address. [CGI arts. 195–196, 208](https://www.dgi.gouv.ml/CGI/).

A taxable person established abroad must appoint an accredited Mali representative responsible for formalities/payment. Failing that, the customer pays for the foreign person, including relevant penalties. This is the actual source mechanism behind the former imported-service shorthand; do not claim an unrestricted universal reverse charge or automatic matching deduction. Determine territoriality, person liable and input-credit conditions separately. [CGI arts. 196–197, 207–225; LPF art. 116](https://www.dgi.gouv.ml/CGI/).

## Two worked examples that recompute

Both are conditional tests of the older DGI provisions, not approved 2026 liabilities. Assume the business is real-normal, ordinary supplies are correctly classified, periods established, evidence valid and no later amendment applies.

**Sales, discount and recoverable purchases.** Goods consideration XOF 12 million before a qualifying direct discount of XOF 1 million gives a XOF 11 million base. Output VAT XOF 1.98 million less supported eligible invoice input tax XOF 720,000 leaves XOF 1.26 million, already a multiple of five. No unproved reduced-rate or exemption claim enters the case.

```oa-check
name: Older Mali VAT source test, consideration and inputs
inputs:
  price: 12000000
  qualifying_discount: 1000000
  eligible_input_tax: 720000
steps:
  taxable_base: price - qualifying_discount
  output_tax: taxable_base * 0.18
  net_tax: output_tax - eligible_input_tax
  return_tax: floor(net_tax / 5) * 5
expected:
  taxable_base: 11000000
  output_tax: 1980000
  return_tax: 1260000
```

**Direct attribution or shared-input fraction?** Supported deductible-operation receipts are XOF 21 million and non-deductible receipts XOF 10 million, all net of VAT with no excluded denominator items. The ratio is 67.7419%, rounded up to 68%. Shared input VAT XOF 300,000 therefore permits XOF 204,000. An additional XOF 100,000 exclusively attributable to taxable operations is fully deductible; XOF 50,000 solely attributable to exempt operations is not. Correct total is XOF 304,000, compared with the wrong XOF 306,000 if the 68% fraction were applied indiscriminately to all inputs. The decision is input attribution, not optional selection of a larger credit.

```oa-check
name: Older Mali VAT source test, direct attribution decision
inputs:
  eligible_receipts: 21000000
  other_receipts: 10000000
  shared_input: 300000
  direct_eligible: 100000
  direct_exempt: 50000
steps:
  prorata_percent: ceil(eligible_receipts / (eligible_receipts + other_receipts) * 100)
  shared_deduction: shared_input * prorata_percent / 100
  correct_deduction: shared_deduction + direct_eligible
  wrong_blanket_deduction: (shared_input + direct_eligible + direct_exempt) * prorata_percent / 100
  overstatement: wrong_blanket_deduction - correct_deduction
expected:
  prorata_percent: 68
  correct_deduction: 304000
  wrong_blanket_deduction: 306000
  overstatement: 2000
```

## Ask the client first

- Which year, registration status, NIF and real/synthetic tax mode apply, and was there a threshold crossing?
- What are the exact goods/services, tariff classifications, exemptions and domestic/foreign supply/use locations?
- What delivery, execution, invoice, receipt and debit-authorisation evidence establishes each tax month?
- Which purchase invoices/customs documents support inputs and are they direct taxable, direct exempt, shared or excluded costs?
- What credits, advances, refunds, payments and notices already exist?
- Has the operative current amendment chain, prescribed return and authorised filing route been obtained?

## Sources

| Source and actual scope | URL | Read on |
|---|---|---|
| DGI, CGI and LPF online consolidation; exact articles cited above and their neighbouring provisions, older amendment labels through 2017; not a 2026 consolidation | https://www.dgi.gouv.ml/CGI/ | 2026-11-01; selected chapters read offline, not the entire code |

Not yet confirmed: complete later amendment chain, enacted 2026 fiscal Annex U and operative 2026 rates/thresholds; complete current exempt/reduced tariff list; current registration/refund forms, boxes, authentication and filing/payment sequence; current sanction interactions and debit-method permissions. Listed older exceptions are not a current exemption opinion. No current-year approval or accountant attestation is claimed.

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
