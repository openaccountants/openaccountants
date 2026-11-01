---
name: sd-cross-border-residence
description: >
  Prepare Sudan cross-border residence and income source workpapers for 2026 intake from the actual Income Tax Act, with specific statutory alternatives and missing implementing instruments recorded. Match Sudan tax residency, 183 days, foreign company, branch, nonresident withholding, double tax treaty, foreign income and الإقامة الضريبية questions. Covers individuals and entities, ordinary residence, multi-period presence, local agents, foreign income discretion and ministerial treaty orders. Do not equate domicile, citizenship or incorporation with the complete residence test. The later enacted chain, payment rate orders, treaty texts and full income regulations remain unresolved. Build the evidence and routing decision first, and stop before applying an assumed withholding percentage, treaty benefit or foreign tax credit.
version: 0.1
jurisdiction: SD
tax_year: 2026
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
last_updated: 2026-11-01
category: cross-border
tier: 2
---

# Sudan residence foreign income and withholding intake v 0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Individuals and non-individuals with Sudan/foreign facts, payers to foreign companies, agents and treaty claims. Income categories and computations belong to [personal income](sd-income-tax.md), [company profits](sd-corporate-income-tax.md), [VAT](sd-vat-gst.md) or [capital gains](sd-capital-gains.md). Residence, domestic charge, collection and treaty relief are distinct decisions.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Individual residence alternatives | Ordinary residence excluding reasonable temporary absence accepted by Secretary General; OR presence EXCEEDING 183 days; OR presence in current and BOTH preceding basis periods exceeding 12 months in total. Domicile is separately defined. | [s.2 resident/domiciled; PDF12,14–16](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Non-individual residence | Supervision and management exercised in Sudan. Foreign incorporation alone does not settle this. | [s.2 resident; PDF16](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Territorial charge | Resident Sudan and foreign income; nonresident Sudan-source income. Foreign-income exemption for tax paid abroad requires ministerial exercise, not automatic credit. | [s.9; PDF22–23](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Treaty priority | An effective ministerial order giving effect to actual double-tax arrangements is required; no list/count or specific rate certified. | [s.33; PDF55](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Nonresident-company collection rate | unverified: s.65(1)(k) delegates gross-income percentage to ministerial order. No universal 14%,15% or final-tax treatment assumed. | [s.65(1)(a)–(k); PDF94–96](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| On-account remittance/credit | Deposit within 1 month under s.65; certificate and audited-return/payment-evidence conditions matter. This is not a universal monthly PAYE due date. | [s.65(1)(i)–(j),(2); PDF96–97](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |

## The base

1. Identify basis and assessment periods under s.2; collect arrival/departure evidence for the current and both preceding basis periods. Preserve partial-day and temporary-absence questions rather than invent a day-count convention.
2. Test ordinary residence separately. For deemed residence,183 exact days does not satisfy the express exceeding 183 limb. The three-period limb also requires presence in each of the specified periods and more than 12 months total, not merely a generic rolling-year total. Domicile is a different defined term; do not treat intention to settle as an automatic third numeric test.
3. For an entity, document where supervision and management actually occur, distinguishing registration, shareholders and operational decision makers. Do not import an effective-management treaty tie-breaker without the treaty.
4. Map each receipt to Sudan or foreign source and the appropriate statutory income category. Residents' foreign income is within the domestic charge; ministerial foreign-income exemption is discretionary. A foreign tax receipt alone does not create a mechanical foreign-tax credit.
5. Identify Sudan agent/branch exposure under s.34 and payment collection under s.65. Obtain the actual ministerial rate order and payer/payee scope before withholding. Reconcile on-account certificates to the return; do not assume finality or treaty reduction.
6. For relief, obtain the operative treaty/order, entry-into-force dates, eligible person and income article, residence certificate, beneficial-entitlement conditions and claim procedure. No 17 treaty count, six-month PE rule or automatic local-agent exemption is established.

## Deadlines and filing

TIN application is governed by s.82 for specified activities, including prescribed form/data. Before payer remittance obtain the actual collection order, return and payment code, gross/net contract terms, currency, period and certificate requirements. Section 65 on-account collections include the deposit and evidence provisions cited above; nonresident agency can create collection responsibility independent of a completed treaty claim. Current electronic forms, monthly employer remittance date, clearance process and payment channels remain held. Retain eventual filing acknowledgement, payer certificate and receipt. No login, TIN lookup or payment was attempted.

## Penalties and interest

Unpaid collection, inaccurate returns and evasion can engage the general Act. The applicable current sanction amounts, departure-security directions and treaty-dispute procedure require the actual notice/regulation. Do not estimate penalties from an assumed withholding rate.

## Cross-border points

This is the cross-border routing home. A foreign-service payment can separately require VAT add-and-remit under s.28(5), and an associated payment can require [TP](sd-transfer-pricing.md) review. A company registry branch, domestic tax agent and treaty permanent establishment are different concepts. Obtain the actual clause before applying a PE duration or branch-remittance conclusion.

## Two worked examples that recompute

### Strict presence boundary

Assume no ordinary-residence or three-period ground has yet been established. At 183 days the excess above 183 is zero and the single-period limb is not met;184 days exceeds it by 1 day and satisfies that limb. The 183 day person still needs the other residence tests. This deliberately rejects the old at-least 183 shortcut.

```oa-check
name: Residence exceeding183 boundary
inputs:
  days_a: 183
  days_b: 184
  boundary: 183
steps:
  - case_a_excess: max(days_a-boundary,0)
  - case_b_excess: max(days_b-boundary,0)
expected:
  case_a_excess: 0
  case_b_excess: 1
```

### Resident versus nonresident source perimeter

Assume Sudan income100,000 and foreign income20,000, all otherwise taxable in the same category. Before any relief, residence puts120,000 in the domestic charge perimeter; nonresidence puts100,000. The20,000 difference shows why residence precedes rate calculation; this is not a foreign-credit calculation.

```oa-check
name: Income scope residence comparison
inputs:
  sudan_income: 100000
  foreign_income: 20000
steps:
  - resident_scope: sudan_income+foreign_income
  - nonresident_scope: sudan_income
  - scope_difference: resident_scope-nonresident_scope
expected:
  resident_scope: 120000
  nonresident_scope: 100000
  scope_difference: 20000
```

## Ask the client first

- Current and two preceding basis periods, travel logs and ordinary-residence/temporary-absence facts.
- Entity supervision/management, registration and local agent/branch activities.
- Each income category, place of source/performance, payer/payee and gross/net terms.
- Foreign tax proof and actual treaty/order, residence certificate and claim history.
- Collection notices, ministerial rate order, currency and credit certificates.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| income-en; selected ss.2,15; PDF 11,27; s.2 resident/domiciled; PDF 12,14–16; s.2 resident; PDF 16; s.9; PDF 22–23; s.33; PDF 55; s.34; PDF 56; s.65(1)(a)–(k); PDF 94–96; s.65(1)(i)–(j),(2); PDF 96–97; s.62(1),(6); PDF 90–91; s.82; PDF 114–115 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-cross-border-residence.md](../../evidence/ledgers/sd-cross-border-residence.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-027: Withholding tax rates on payments. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-040: Double taxation treaties. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-044: Example 4 - Withholding on payment to non-resident contractor. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-053: PAYE withholding. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-056: Step 1 - Determine residency. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-062: Residence - non-individual (companies). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-067: Example 1 - Resident employee, moderate income. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-068: Example 2 - Non-resident consultant. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-115: Residency tests. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-121: Section 10 - Risk-classified treatment summary. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Later enacted chain, partial-day convention, residence certificate/tie-breaker procedures and specific treaty texts/status; permanent-establishment duration, construction/service-agent thresholds, branch-remittance tax and foreign-exchange permissions; actual ministerial withholding orders and rates for services, interest, royalties, dividends, imports/exports and petroleum contracts, residence-dependent finality, current treaty reduction and foreign-credit procedures. Current return, payment code, payer remittance deadline and departure clearance remain incomplete. The old 17 treaty count, six-month PE and universal 14% nonresident collection claims are not approved. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.
