---
name: bq-customs-valuation
description: >
  Determine 2026 BES customs valuation and its relationship to import duty,
  ABB and excise. Use for export-sale prices, connected parties, packing,
  freight, insurance, assists, royalties, excluded costs, alternative valuation
  methods, evidence and foreign currency. Explains the statutory nil import
  duty and why it does not remove other import charges or formalities.
  Includes primary legislation, current authority guidance and a fictional
  component reconciliation. This source-cited draft holds actual classification,
  exemptions, customs procedures, exchange-rate evidence, forms and unresolved
  operational cases. Load with the universal workflow base and BES companions;
  professional review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Customs valuation checked on 17 October 2026; actual acceptance, import and debt dates established separately"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-abb
  - bq-excise
---

# Bonaire, Sint Eustatius and Saba: customs valuation

Determine the actual island, goods, customs destination, declarant, import
event, valuation method and applicable version before calculating an import
charge. Douane- en Accijnswet BES article 3.2 expressly sets import duty at
**USD nil**. This is affirmative support for that tariff, not an exemption
from import ABB, excise, controls, declarations or prohibited-goods rules.
Articles 1.1–1.4 give the separate customs territory, definitions, control
functions and charges. [DAB]; [AUTH]

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, confirmed profile, refusals, four universal outputs and all domain
outputs/checks. This Tier 2 reference covers valuation and charge separation;
it does not complete customs clearance, an actual return or a country pack.
Unknown mandatory conditions hold the complete financial output package.

## Price is the start of a method

Article 3.7 normally values goods when the customs declaration is accepted.
Article 3.14 supplies an ordered hierarchy:

1. Transaction value, if its conditions are met.
2. Transaction value of identical goods.
3. Transaction value of similar goods.
4. Deductive value.
5. Computed value.
6. Reasonable means consistent with the specified valuation principles.

The importer may request the stated reversal of deductive and computed
methods. The hierarchy is not a free choice of whichever gives the lowest
tax or is easiest to find. A gift, no-sale movement, damaged shipment or
unsupported invoice needs its actual branch; do not use an invented zero
price or a retail advertisement without the relevant method. [DAB,
articles 3.6–3.24][DAB]

Article 3.16 starts from the price actually paid or payable for goods sold
for export to BES, adjusted under articles 3.18–3.19. It covers indirect
payments and has conditions concerning restrictions, unquantifiable price
conditions, subsequent proceeds and connected parties. Separately allocated
quantities, pre-import loss/damage and goods used in a third country have
their own paragraphs. A supplier invoice alone does not establish acceptance.
[DAB]

Connected status is defined in article 3.6, including the specified control,
shareholding, employment, business and family connections. Exclusive agency
or distribution alone does not establish it without a listed criterion.
Connection alone also does not reject transaction value: article 3.17 tests
price influence or the stated closely approximating values, with the required
adjustments and evidence. Keep the customs analysis separate from a generic
transfer-pricing conclusion. [DAB]

## Transaction-value adjustments

Add only qualifying amounts not already included in the price. Article
3.18 requires objective, quantifiable data and addresses inspector decisions
where costs span transactions. Do not double-count an inclusive freight
invoice or allocate an assist using an invented percentage. [DAB]

| Article 3.18 addition | Conditions to establish |
|---|---|
| Commission/brokerage, containers and packing | Buyer-borne amounts not already included; buying commissions are separately excluded. Reusable packing has a proportional allocation on request. |
| Buyer-supplied materials, parts, tools, moulds and consumed materials | Supplied free or at reduced cost for production/export and not already in the price; allocate the actual value proportionately. |
| Specified engineering, development, artwork and designs | Work outside BES necessary for production, with the stated research/preliminary-design exclusion. |
| Royalties/licence fees | Related to the goods and payable as a condition of sale, excluding the specified reproduction right. |
| Subsequent proceeds benefiting the seller | The actual attributable resale, transfer or use proceeds. |
| Freight, insurance, loading and handling to entry | Actual relevant amounts; free/own transport and uninsured goods have the statutory usual-cost rule. |

[DAB]

Article 3.19 excludes the following **when distinguished from the price**:
specified post-import construction, installation, assembly, maintenance or
technical assistance; local import/sale taxes; qualifying customs-storage
costs; proven relieved origin/export-country taxes; BES reproduction rights;
buying commissions; and qualifying post-entry transport/insurance/handling,
subject to the postal-cost exception. Financing interest needs the written
agreement, separate identification, actual goods price and ordinary-rate
conditions. The cash-discount provision has a **2% invoice-value ceiling**.
These are legal categories, not a deduction for all business expenses.
[DAB]

For an installed machine, identify the actual pre/post-import work and
separate price evidence before excluding installation. For free freight or
buyer-owned transport, zero cash paid does not alone mean zero freight in
customs value. A claimed deduction with no required separation or proof
remains held. [DAB]

## Alternative methods and evidence

| Method | Rule to preserve |
|---|---|
| Identical/similar goods, articles 3.20–3.21 | Export to BES at the same or approximately the same time; adjust evidenced trade-level, quantity and transport differences. Where more than one qualifying transaction value exists, use the lowest under the stated rule. Do not select an unrelated low online price. |
| Deductive, article 3.22 | Use the qualifying unit resale price in the greatest aggregate quantity at the first post-import trade level to unrelated buyers. The later-sale branch is limited to 90 days, with the stated commission/profit, local transport and tax deductions. Processed goods require the requested branch and added-value adjustment. |
| Computed, article 3.23 | Production/material costs plus the appropriate producing-country profit/general costs and transport/insurance/loading/handling to entry. A generic cost-plus margin is not evidence. |
| Reasonable means, article 3.24 | Use available BES data consistently with the statutory/international valuation principles. Local production prices, export-country domestic prices, the listed export prices, minimum values and arbitrary/fictitious values are prohibited bases. |

[DAB]

The inspector can reject insufficiently supported values under article 3.15,
with its reasons/response and decision provisions. Articles 3.8–3.11 require
valuation information and evidence, including separate computation/method
details in applicable cases. An exception from a particular value declaration
does not eliminate the underlying valuation or every customs declaration.
Actual documents, notices, authorised representation, clearance and remedies
need their complete procedural branch. [DAB]

## Foreign currency, duty rounding and ABB

Article 3.12 supplies the official-rate date and fallback sequence, including
its separately specified publication/currency branches and revaluation rule.
Record the currency, relevant debt date, applicable published rate, direction
and calculation. A card settlement rate, today's web converter or guessed
exchange rate is not automatically that statutory rate. No live FX publication
or conversion is established here; unresolved rate evidence holds the result.
[DAB]

Article 3.5 contains rounding rules **for import duty**, including upward
value/unit and line-duty rounding. Do not copy them into every excise or ABB
calculation. Petrol has its own express partial-hectolitre rule in
`bq-excise`. Actual monetary/return rounding beyond the established branch
remains held. [DAB]

Belastingwet BES article 6.18 starts import ABB from customs value and adds
the stated import rights, taxes and levies, excluding the import ABB itself,
and the prescribed incidental costs. Its transport paragraph excludes the
specified post-arrival transport. Keep the customs transaction value and
the ABB statutory additions separate; excise is not added twice or ABB
charged recursively on itself. Establish amounts already included before
adding any commission, packing, freight or insurance again. [B1]; [AUTH]

The authority page describes ordinary import ABB as **8% on Bonaire** and
**6% on Saba/Sint Eustatius**, with exceptions. It both describes a progressive
vehicle branch for Saba/Sint Eustatius and repeats an unqualified 25% vehicle
sentence. That duplication does not establish one vehicle rate everywhere.
Use the actual vehicle definitions, statutory tariff and exceptions through
`bq-abb`; no vehicle or traveller exemption is computed here. The page's
traveller-baggage freight statement likewise does not replace the special
relief and valuation rules for an actual traveller. [AUTH]; [B1]

### Fictional component reconciliation

Assume a Bonaire taxable import, an acceptable export-sale transaction value,
USD inputs, all stated additions qualifying and separately established,
none already included in another line, no exemption and an ordinary 8% ABB
rate. The excise component of 100 is independently stipulated, rather than
derived from the goods' price. [DAB]; [B1]; [AUTH]

| Item | USD |
|---|---:|
| Actual export-sale price | 1,000 |
| Qualifying packing not included in price | 40 |
| Freight to entry not included in price | 100 |
| Insurance to entry not included in price | 10 |
| Qualifying allocated assist not included in price | 50 |
| Customs transaction value | **1,200** |
| Import duty at statutory nil tariff | **0** |
| Independently established excise | **100** |
| ABB base, with no other adjustment | **1,300** |
| ABB, 1,300 × 8% | **104** |
| These three import-tax components combined | **204** |

A separately evidenced qualifying post-import installation charge of 200
would not enter this transaction value under article 3.19; an unseparated
invoice does not establish that deduction. Packing/freight already included
in the price must not be added a second time. A linked buyer and seller
do not automatically invalidate the price, and a no-sale gift does not
justify a fictitious zero. These are classification controls, not actual
case findings. [DAB]

## Verification and limits

Check island, goods, destination and event; method order and conditions;
actual direct/indirect price; related-party evidence; every addition and
exclusion; allocation and duplicate amounts; relevant FX source/date;
customs value versus ABB base; duty versus excise versus ABB; correct
rounding; and separate relief, procedure and professional review. Keep
unknown mandatory conditions as Needs Input or holds, with all workflow
outputs and reviewer questions preserved.

Read on 17 October 2026: customs-law articles 1.1–1.4 and 3.1–3.24 in full,
Belastingwet BES article 6.18 and the full current authority import page.
A fresh customs-law capture matches the saved source byte-for-byte.
The complete customs-formality, representation, relief, debt, appeal and
enforcement chapters, implementing valuation details, actual FX publications,
HS classification, forms and operational cases were not reviewed here.
No private invoice, identity/tax number, bank details, submission, engagement
workbook or practitioner sign-off was used. No comprehensive-area credit
is claimed.

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[AUTH]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-particulieren/invoerbelastingen-particulieren

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
