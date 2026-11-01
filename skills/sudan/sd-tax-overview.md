---
name: sd-tax-overview
description: >
  Route Sudan tax questions and assemble a coordinated 2026 intake workpaper across personal income, company profits, VAT, payroll, formation, associated pricing and cross-border income. Match Sudan tax overview, business tax obligations, tax registration, compliance calendar, new business, foreign investor and الضرائب في السودان requests. This Guide identifies the source chain, evidence owners and unresolved release gates, while linking each figure to its single calculation home. Official statutes and amendments replace legacy unsourced assumptions, but the later enacted chain remains incomplete. Use this pack for broad source baseline preparation and a reviewable issue list. Neither current year metadata nor passing examples authorises filing, publication certification or a country complete claim.
version: 0.3
jurisdiction: SD
tax_year: 2026
last_updated: 2026-11-01
authored_by: Ahmed Hassan
review_status: pending_review
trust_label: Accountant-authored
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
---

# Sudan tax workpaper routing and release gates v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Individuals, employers, companies, foreign branches and investors planning ordinary Sudan tax work. This router does not duplicate every rate. Each linked Guide owns its calculation, conditions and quoted ledger. Sudan and South Sudan are separate jurisdictions. This is a 2026 intake/source-baseline pack with all seven mapped tax domains partial, not an operative 2026 law certification.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Period | Basis/assessment-year distinction and accounting-period approvals belong to the company-profit and cross-border Guides. | [ss.2,15; PDF11,27](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Income-tax registration | Specified activity requires TIN application; use actual prescribed form/data. | [s.82; PDF114–115](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Income-tax records | Statutory retention plus 2022 approved Arabic translation addition; the company Guide owns the full record rule. | [Income Tax Amendment 2022 s.2(1), PDF1](https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf) |
| Filing framework | Principal return-notice framework is not a confirmed universal 31 March self-assessment deadline. | [s.38; PDF58–61](https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf) |
| Company currentness | Justice notice identifies 2025 amendment; full amended chain remains a formation release gate. | [notice5July2025](https://moj.gov.sd/posts/post/998) |

## The base

| Job | Calculation and evidence owner |
|---|---|
| Individual employment, business/professional and rent | [Personal income tax](sd-income-tax.md) |
| Company profit, industrial classification, expenses, capital allowances and business losses | [Company profits](sd-corporate-income-tax.md) |
| VAT registration, invoice, monthly Form 3, input and export refund | [VAT](sd-vat-gst.md) |
| Social/health contribution bases, employment leave and termination | [Payroll](sd-payroll-social.md) |
| Company/branch documents, board, licences and annual accounts | [Formation](sd-company-formation.md) |
| Associated-person relationships and pricing | [Transfer pricing](sd-transfer-pricing.md) |
| Residence, source, foreign agents, withholding orders and treaty claims | [Cross-border](sd-cross-border-residence.md) |
| Capital disposals under separate Act | [Capital gains](sd-capital-gains.md) |

For every job, obtain the period and entity/fact classification, open the applicable operative instruments, reconcile amendments and identify the actual form/payment route BEFORE approving a computation. The official catalogue has principal Acts, regulations and annual amendments through 2022; its label is not proof of document identity or currentness. In particular the supposed 2021 regulations download is an Act copy, and the 2020 bundles contain cabinet approvals of proposed laws. The Justice Gazette index reaches October 2026, but an incomplete catalogue/read is not proof that no later tax changes occurred.

## Deadlines and filing

1. Collect identity/entity, TIN and registry/fund/VAT identifiers, contracts, books, invoices and prior notices. Link each registration to the appropriate Guide; one registration does not discharge all taxes.
2. Create a calendar from the actual applicable statute/regulation/notice, not a copied generic date. Income tax, VAT, employer list, company AGM/annual return and fund remittances have different rules and unresolved items.
3. Prepare a source-period computation and an issues table showing the missing enacted chain, applicable form/box, deadline, payment code and evidence required. Do not calculate an unsupported rate merely to fill a spreadsheet.
4. Hold the filing/payment/formation approval until every job-specific release gate clears. Record the actual submission acknowledgement and payment/registration decision afterwards. This research did not log into a portal or make any taxpayer action.
5. Save the source URL, article, short quote, read date and exact capture hash with the workpaper. Independent review and any later professional attestation are distinct from this writer record.

## Penalties and interest

Each tax/registration has its own offence and recovery provisions. No single general fine, monthly interest percentage or universal objection deadline applies across this router. Obtain the actual law, notice and service facts through the owner Guide.

## Cross-border points

Start with [cross-border](sd-cross-border-residence.md), then route foreign-service VAT and associated pricing separately. A treaty claim needs the actual operative order/text; no blanket treaty count, foreign credit, PE duration or withholding finality is certified. Investment/free-zone, Zakat, stamp/customs, local levies and exchange controls remain distinct specialist jobs.

## Two worked examples that recompute

### Ordinary importer-employer routing

A company importer with employees and no controlled/foreign service transaction needs company profit, VAT and payroll workpapers, plus formation/registration records. Four owners are routed. If a cross-border payment and controlled transaction are later found, two additional distinct owners are needed. Routing count does not approve any rate.

```oa-check
name: Importer employer tax job routing
inputs:
  company: 1
  vat: 1
  payroll: 1
  formation: 1
  cross_border_added: 1
  tp_added: 1
steps:
  - initial_owners: company+vat+payroll+formation
  - expanded_owners: initial_owners+cross_border_added+tp_added
expected:
  initial_owners: 4
  expanded_owners: 6
```

### Release-gate decision

Assume five required evidence gates for a specific job: operative chain, classification, documents, current form and payment route. Four are resolved but operative chain is not: one remains and release is blocked. After source reconciliation all five can be marked resolved; arithmetic alone does not mark them resolved.

```oa-check
name: Release gate evidence count
inputs:
  required: 5
  resolved_before: 4
  resolved_after: 5
steps:
  - open_before: max(required-resolved_before,0)
  - open_after: max(required-resolved_after,0)
expected:
  open_before: 1
  open_after: 0
```

## Ask the client first

- Person/entity, activities, employees, ownership and Sudan/foreign facts.
- Basis/accounting periods and the exact proposed transaction or filing.
- Current registrations, notices, prior returns and outstanding assessments.
- Books, invoices, payroll components, licences and foreign contracts.
- Source-period evidence and unresolved operative-law/form/payment questions.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| income-en; selected ss.2,15; PDF 11,27; s.82; PDF 114–115; s.38(1),(3)(a)–(b); PDF 58–61, taxpayer definition PDF 59; s.39(4)–(6); PDF 62–63; s.65(1)(i)–(j),(2); PDF 96–97 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Income-tax.pdf | 2026-11-01 |
| law 38-39; selected Income Tax Amendment 2022 s.2(1), PDF 1 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law38-39.pdf | 2026-11-01 |
| company-notice; selected notice 5 July 2025 read; not a full current consolidation | https://moj.gov.sd/posts/post/998 | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-tax-overview.md](../../evidence/ledgers/sd-tax-overview.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Legacy-topic controls below refer to the exact original material and line-independent destination records in [the complete old-topic map](../../evidence/ledgers/sd-old-topic-map.md). Each control retains its original rules, figures, groups, procedures and exceptions for source reconciliation. Supported content is replaced above with citations; any remaining original claim under that control is explicitly unconfirmed, not a usable default.

- SD-OLD-105: Section 1 - Quick reference. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-106: Section 2 - Tax structure map. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-107: Category 1 - Goods and Services Taxes. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-108: Category 2 - Income Taxes. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-109: Category 3 - Property and Transaction Taxes. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-110: Category 4 - Sector-specific and contractual. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-111: Sudan Taxation Chamber (مصلحة الضرائب السودانية). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-112: Related fiscal agencies. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-113: Section 4 - Sudan vs. South Sudan. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-114: Territorial + person hybrid. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-116: Reform timeline. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-117: Current status (as of 2026-07). Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-118: Section 7 - Currency and denomination considerations. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-119: Section 8 - Audit flash points summary. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-120: Section 9 - Reference material. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.
- SD-OLD-122: PROHIBITIONS. Residual legacy claims: not yet confirmed; see exact old content and destination in the map.

Not yet confirmed: Operative 2026 consolidated chain for every tax, complete 2021 income regulations, current tax/fund forms and payment instructions, company 2025/2026 amendments, contribution-base conflict, all current penalties and specific treaties. Legacy Zakat 2.5%/multiple zakat bases, stamp duty 0.1–15% and StampDuty 2019 title, customs 0–40%, property tax 10%, local 5–25%/5%levies, capital tax 0.1%, banking/insurance contributions, free-zone and investment holidays/initial allowances, tourism/digital/excise and special petroleum arrangements are not certified. These topics and all legacy source/procedure claims remain individually traceable in the destination map. No mechanical check establishes country completion. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.

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
