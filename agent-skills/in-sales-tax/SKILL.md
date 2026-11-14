---
name: in-sales-tax
description: "Indiana sales and use tax in 2026. Covers the 7% state rate, remote-seller threshold, software, food and medical boundaries, manufacturing, sourcing and filing. Load us-sales-tax for the multistate framework."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-sales-tax"
  jurisdiction: "US-IN"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Indiana sales and use tax v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** 7% state sales/use tax. Remote economic nexus requires revenue exceeding $100,000; the old transaction-count test was repealed retroactively to January 1, 2024. Special transaction taxes require separate checks. Built from the law; Not yet approved.

## Who this applies to

Indiana retailers, remote sellers, marketplace businesses and purchasers with untaxed taxable Indiana use. Load `us-sales-tax`, then apply Indiana's rules. A remote-sales safe harbour does not remove an independent physical-presence obligation. Source: [Bulletin 89](https://secure.in.gov/dor/files/sib89.pdf).

## Rates, bands and thresholds

| Item | Amount / condition | Official source |
|---|---|---|
| State sales/use rate | 7%; no general local sales-tax addition | [DOR sales page](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/), [FAQ](https://www.in.gov/dor/i-am-a/business-corp/business-faq/) |
| Remote economic nexus | Gross revenue exceeding $100,000 in the current or preceding calendar year; statutory scope and marketplace exclusions matter | [Bulletin 89; IC 6-2.5-2-1](https://secure.in.gov/dor/files/sib89.pdf) |
| Transaction count | Separate 200-transaction test repealed from January 1, 2024 | [Bulletin 89](https://secure.in.gov/dor/files/sib89.pdf) |
| Additional taxes | Food/beverage, county innkeeper and other activity taxes are separate; 7% is not a universal all-tax maximum | [DOR sales page](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/) |
| Streamlined Sales Tax | Full member; state legislation still controls | [Bulletin 90](https://www.in.gov/dor/files/sib90.pdf) |

For remote revenue, include the categories specified in Bulletin 89, including relevant exempt/wholesale transactions. A provider of solely nontaxable services is not automatically within the rule merely because revenue is large. Facilitators and marketplace sellers have different counting rules; determine which qualifying facilitated sales are excluded from a seller's calculation.

## The base

| Existing topic | Correct boundary | Official source |
|---|---|---|
| General tangible property and clothing | Ordinary retail property taxable unless a specific exemption applies | [DOR sales page](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/) |
| Grocery / prepared food | Qualifying unheated food without utensils can be exempt; candy, soft drinks, alcohol and dietary supplements are excluded categories. Prepared-food rules have bakery/manufacturer exceptions | [Bulletin 29, pages 1-4](https://www.in.gov/dor/files/reference/sib29.pdf) |
| SaaS / remote software | Access without download or possession generally falls outside software tax; examine applets and bundles | [Bulletin 8, pages 6-9](https://www.in.gov/dor/files/sib08.pdf) |
| Downloaded canned software | Prewritten software transferred by download taxable; a licence label does not remove the transfer | [Bulletin 8](https://www.in.gov/dor/files/sib08.pdf) |
| Professional / repair services | Examine genuinely separate services, bundled goods and taxable categories; selling goods does not make every separate service taxable | [DOR example](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/), [Bulletin 8](https://www.in.gov/dor/files/sib08.pdf) |
| Manufacturing equipment | Direct use in direct production requires integral/essential and immediate-impact tests; not every factory purchase qualifies | [Bulletin 64, effective October 1, 2026](https://www.in.gov/dor/files/reference/sib64.pdf) |
| Prescription / OTC drugs | No blanket OTC exemption. Check drug, prescription/order and dispenser conditions; particular insulin, oxygen and blood provisions have exceptions | [Bulletin 48, pages 1-4](https://www.in.gov/dor/files/reference/sib48.pdf) |
| Resale | Existing statutory topic retained; current certificate completion, acceptance and retention rules remain unconfirmed | [DOR exemption chapter link](https://www.in.gov/dor/i-am-a/business-corp/business-faq/) |

**Sourcing hierarchy.** [Bulletin 96; IC 6-2.5-13](https://www.in.gov/dor/files/sib96.pdf) starts with receipt at the seller's business, otherwise known purchaser/donee receipt location. If unknown, use the good-faith ordinary-record address, then transaction/payment address, then statutory origin fallback. Carrier possession is not purchaser receipt. FOB/title wording alone does not decide sourcing. Rentals, vehicles and other special transactions need their own rules.

**Use tax.** Check taxable purchases without seller collection and inventory withdrawals. The [DOR FAQ](https://www.in.gov/dor/i-am-a/business-corp/business-faq/) describes credit for qualifying sales tax paid to another state, up to Indiana's rate. Verify actual payment and eligibility.

## Deadlines and filing

1. Register through [INBiz](https://inbiz.in.gov/) and obtain a Registered Retail Merchant Certificate for each retail location. Keep accounts/returns current for renewal. See [DOR sales registration](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/).
2. Use the assigned sales-tax account and period in [INTIME](https://intime.dor.in.gov/). Reconcile gross sales, exemptions, taxable sales, collected tax and purchaser use tax separately. Save return acceptance and payment confirmation.
3. File active zero periods. Follow the assigned frequency and actual due date; do not borrow payroll's thresholds. Complete current sales-frequency rules and form lines remain unconfirmed.
4. Check additional registrations for special activities. Consolidated accounts can need annual RP-11. See [DOR sales page](https://www.in.gov/dor/i-am-a/business-corp/sales-tax/).

## Penalties and interest

Unfiled zero periods can still trigger penalties. Complete current late-filing, late-payment, negligence, interest and trust-tax liability rules were not verified here. Obtain the applicable notice/provision before computing an assessment.

## Cross-border points

Physical presence, economic nexus, marketplace collection, sourcing and purchaser use tax are separate questions. A seller's Indiana location does not alone determine another state's receipt. Lack of collection does not prove Indiana use is exempt; credits require evidence of qualifying tax actually paid.

## Two worked examples that recompute

**Sales and use tax.** Invented retailer has $10,000 taxable Indiana sales and $2,000 taxable Indiana purchases, with documented eligible 5% other-state sales tax on those purchases. Sales tax is $700. Use tax before credit is $140, credit $100, residual $40. Special activity taxes and exemptions are outside these assumptions.

```oa-check
name: Indiana sales and use tax separate bases
inputs:
  taxable_sales: 10000
  taxable_purchases: 2000
  qualifying_other_state_rate: 0.05
steps:
  sales_tax: taxable_sales * 0.07
  use_before_credit: taxable_purchases * 0.07
  credit: min(use_before_credit, taxable_purchases * qualifying_other_state_rate)
  residual_use: use_before_credit - credit
expected:
  sales_tax: 700
  use_before_credit: 140
  credit: 100
  residual_use: 40
```

**Remote threshold, both ways.** Invented seller has no physical presence or other registration trigger and only revenue within the statutory test. Exactly $100,000 does not exceed the threshold; $100,001 exceeds it by $1. Transaction count alone does not revive the repealed test. This establishes the boundary, not an unverified registration start date.

```oa-check
name: Indiana remote revenue boundary
inputs:
  at_limit: 100000
  above_limit: 100001
steps:
  excess_at_limit: max(0, at_limit - 100000)
  excess_above_limit: max(0, above_limit - 100000)
expected:
  excess_at_limit: 0
  excess_above_limit: 1
```

## Ask the client first

- What year, physical presence, current/prior Indiana revenue apply?
- What goods, software download/possession terms, services and bundles are sold?
- Where does the buyer receive/use property, with what address evidence?
- What marketplace collections, exemptions and certificates are documented?
- What purchases, other-state tax payments, account notices and special activities exist?

## Sources

| Source | URL | Read for | Read for on |
|---|---|---|---|
| DOR sales page | https://www.in.gov/dor/i-am-a/business-corp/sales-tax/ | Read for rate, RRMC, location certificates, zero periods, special registrations and RP-11; live basic Firecrawl retrieval succeeded | 2026-11-13 |
| DOR business FAQ | https://www.in.gov/dor/i-am-a/business-corp/business-faq/ | Read for use-tax examples, other-state credit and linked exemption chapter | 2026-11-13 |
| Bulletin 89; IC 6-2.5-2-1 | https://secure.in.gov/dor/files/sib89.pdf | Read for pages 1-4 for revenue scope, transaction-test repeal, physical-presence and marketplace distinctions | 2026-11-13 |
| Bulletin 8 | https://www.in.gov/dor/files/sib08.pdf | Read for pages 6-9 for downloads, remote access and applet/bundle qualifications | 2026-11-13 |
| Bulletin 29, September 2025 | https://www.in.gov/dor/files/reference/sib29.pdf | Read for pages 1-4 for food, utensils and bakery/manufacturer exceptions | 2026-11-13 |
| Bulletin 48 | https://www.in.gov/dor/files/reference/sib48.pdf | Read for pages 1-4 for drug/order/dispenser conditions and exceptions | 2026-11-13 |
| Bulletin 64, September 2026 | https://www.in.gov/dor/files/reference/sib64.pdf | Read for introduction/direct-use pages 1-2; not a complete equipment schedule | 2026-11-13 |
| Bulletin 96; IC 6-2.5-13 | https://www.in.gov/dor/files/sib96.pdf | Read for general hierarchy, receipt/carrier definition and special-rule boundaries | 2026-11-13 |
| Bulletin 90 | https://www.in.gov/dor/files/sib90.pdf | Read for introduction for full membership and continuing state-law control | 2026-11-13 |

Not yet confirmed: complete sales filing-frequency thresholds/due dates, ST-103 lines and nexus registration-start timing; resale certificates; full service/bundle/manufacturing rules; all food/medical exceptions; delivery-charge allocation; local food/beverage and innkeeper rates/bases; leases, vehicles, direct mail and special sourcing. The limited readings above do not certify whole bulletins. Old universal instructions to avoid local taxes, exempt all SaaS/OTC drugs or refuse arithmetic are withdrawn.

## Disclaimer

Informational only. Review by qualified professional required before filing.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
