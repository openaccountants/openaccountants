---
name: sd-transfer-pricing
description: >
  Prepare Sudan associated person transaction workpapers for 2026 intake under the express Income Tax Act section 22 A and neighbouring nonresident pricing provisions. Match Sudan transfer pricing, related parties, arm length pricing, management charges, intercompany loans, associated companies and أسعار التحويل questions. Covers domestic and cross-border dealings, taxable and exempt parties, family and ownership relationships, pricing evidence and adjustment direction. The opened Act contradicts the legacy assertion that Sudan has no formal transfer pricing legislation. Full implementing regulations, agreed methods, documentation duties and later amendments remain unresolved. This Guide builds a transaction and evidence analysis while refusing invented annual thresholds, filing deadlines, safe harbours, master files or country reporting obligations.
version: 0.2
jurisdiction: SD
tax_year: 2026
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
last_updated: 2026-11-01
category: transfer-pricing
tier: 2
---

# Sudan associated person pricing v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Associated-person conditions that reduce a tax base or shift burden, whether parties are resident/nonresident or taxable/exempt. The job is to identify statutory association and prepare price-adjustment evidence under s.22 A, alongside the more specific s.22 nonresident rules. This is not a completed local documentation return or confirmation that a named international method is mandated.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Ownership association limb | Direct or indirect 50% or more by number OR value of shares; family and influence/partnership limbs remain independent. | [s.22A(3); PDF41](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Transaction scope | Residents/nonresidents and taxed/exempt associated persons are within s.22 A where the statutory tax-base/burden condition is met. | [s.22A(1); PDF40](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Pricing standard | Real value in natural dealings between unassociated persons; regulatory methods and agreements need the actual regulations. | [s.22A(2)–(3); PDF40–41](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Documentation/reporting thresholds | unverified: no actual annual documentation, master/local file, CbCR, transaction threshold or safe harbour obtained. | [s.22A(2)–(3); PDF40–41](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |

## The base

1. Gather the ownership chain by both share number and value, direct/indirect interests, family relationships, partnership interests and actual influence over taxable income. Below the ownership limb does not prove independence.
2. List each controlled transaction and party residence/tax status, contracts, functions, assets, risks, benefits and actual payment/booking. These are evidence inputs, not a claim that a particular OECD method has been enacted.
3. Test whether the associated conditions differ from unrelated dealings and reduce the base or shift tax burden under s.22 A. Prepare independent evidence for price/terms and adjustment direction. Do not call every accounting difference a tax adjustment.
4. For nonresident production/export or connected resident/nonresident pricing, read s.22 separately, including wholesale/allowance/profit-cap context. Do not replace the broader associated-person test with only a cross-border test.
5. Identify actual implementing regulations and any Secretary General agreement before choosing a mandatory method, documentation format or relief. The catalogue's 2021 regulation link resolves to another Act PDF; it does not fill this gap.
6. Deliver a transaction matrix, evidence comparables, preliminary adjustment and unresolved-law schedule to the reviewer. Hold filing, corresponding adjustment, advance pricing agreement and penalty conclusions until their operative instruments are available.

## Deadlines and filing

Section 22 A refers to regulations and permits method agreements. No actual standalone TP return, annual deadline, advance-agreement procedure, accepted method list, contemporaneous file threshold or CbCR instrument was read. Preserve material with the applicable income-tax records, obtain current authority instructions and link any eventual adjustment to the correct income-tax return. Do not invent a June deadline or an annual turnover threshold. No taxpayer submission was performed.

## Penalties and interest

No distinct TP documentation penalty or safe harbour was obtained. General income-tax audit, adjustment, avoidance and collection provisions must not be converted into a specific TP fine without the relevant provision.

## Cross-border points

The statute expressly includes domestic as well as cross-border association. [Cross-border residence](sd-cross-border-residence.md) owns source, agent and treaty-order issues; a tax treaty or foreign corresponding adjustment requires the actual operative text and procedure. No blanket OECD membership, treaty entitlement or foreign credit is inferred.

## Two worked examples that recompute

### Underpriced sale adjustment direction

Hypothetical 1000 units sold to an associated buyer at 80 instead of independently supported 100: arm length revenue 100,000 less booked 80,000 gives 20,000 potential upward adjustment. Actual application still requires the tax-base/burden condition and legally accepted evidence.

```oa-check
name: Controlled sale real value bridge
inputs:
  units: 1000
  book_price: 80
  supported_price: 100
steps:
  - book_revenue: units*book_price
  - supported_revenue: units*supported_price
  - upward_adjustment: supported_revenue-book_revenue
expected:
  upward_adjustment: 20000
```

### Ownership limb boundary and alternative grounds

An interest of49.9% is0.1percentage point below the50% limb;50% is exactly at it. The first interest is not an independence clearance: spouse, partnership or influence facts can still establish association. The decision is to continue the alternative-ground inquiry rather than waive pricing review.

```oa-check
name: Ownership threshold gap without independence shortcut
inputs:
  below: 49.9
  at_threshold: 50
  threshold: 50
steps:
  - below_gap: max(threshold-below,0)
  - threshold_gap: max(threshold-at_threshold,0)
expected:
  below_gap: 0.1
  threshold_gap: 0
```

## Ask the client first

- All parties, residence, taxable/exempt status and transaction amounts.
- Share number/value ownership chain, family, partnership and influence facts.
- Contracts, functions, assets, risks and actual price/payment evidence.
- Independent price/term evidence and effect on each taxable base.
- Prior agreements, audits, regulations and requested filing period.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| income-en; selected s.22 A(1); PDF 40; s.22 A(2)–(3); PDF 40–41; s.22 A(3); PDF 41; s.22(1); PDF 39–40; s.16(1)–(2); PDF 27–28 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-transfer-pricing.md](../../evidence/ledgers/sd-transfer-pricing.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-037: Transfer pricing. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Full implementing regulations, later enacted chain, mandatory methods, pricing agreements, advance procedures, domestic exemptions, contemporaneous documentation thresholds, deadlines, disclosure forms, CbCR/master/local file duties, safe harbours, specific penalties, corresponding adjustments and treaty dispute procedures. The legacy no-formal-TP claim is corrected by actual s.22 A, but this does not establish any annual compliance threshold. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.
