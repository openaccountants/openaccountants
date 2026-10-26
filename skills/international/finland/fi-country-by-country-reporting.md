---
name: fi-country-by-country-reporting
description: >
  Prepare Finland country-by-country tax reporting and reporting-entity notifications for 2026 periods. Determine the group or standalone-with-PE threshold, ultimate-parent, secondary or surrogate role and the separate notification duty. Covers statutory foreign-parent failure conditions, information refusal, currency thresholds, jurisdictional revenue and tax aggregation, equity, employees, tangible assets and constituent-entity identifiers. Distinguish consolidated sales used for the threshold from country rows in the report. Includes MyTax and CSV preparation, report and notification deadlines, exchange evidence and sanctions. Trigger on CbCR, DAC4, maakohtainen raportti, reporting entity, EUR 750 million group or Finnish secondary reporting. Public company-law reporting and Pillar Two returns are separate obligations.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-26
version: 0.6
---

# Finland country-by-country reporting v0.6

## Who this applies to

Apply Assessment Procedure Act 1558/1995 §14d to Finnish ultimate-parent groups with at least one foreign constituent entity and preceding-period consolidated net sales at least EUR 750 million. The Act also covers a Finnish standalone enterprise with a foreign PE, the specified Finnish PEs of foreign enterprises, Finnish partnerships and Finnish-organised entities without a tax residence. Determine the full-report role and notification separately. This confidential tax CbCR is distinct from public company-law country reporting, Pillar Two returns and the [transfer-pricing documentation](fi-transfer-pricing.md). [Act §§14d–14e][law].

## Rates, bands and thresholds

| Item | Rule | Official source |
|---|---|---|
| Revenue threshold | At least EUR 750 million preceding accounting period | Act §14d(1),(4),(5) [text][law] |
| Notification | By final day of reported accounting period | Act §14d(11) [text][law] |
| Full report / parent-refusal notification | Within 12 months after period end | Act §14d(11) [text][law] |
| CbCR-specific tax increase | Up to EUR 25,000 for specified failures | Act §§32(1)(3),32a [text][law] |

## The base

### Establish the reporting perimeter and role

The ultimate parent is the entity required to consolidate under the applicable accounting law, or that would be required to consolidate if its equity were listed in its tax-residence jurisdiction, and that has no higher directly/indirectly controlling entity with that consolidation duty. Constituent entities include business units in the consolidated financial statements (or included under the hypothetical listing test), **entities excluded solely for size or materiality**, and their PEs where separate accounts are prepared for financial/regulatory/tax reporting or internal management. Obtain the full legal/consolidation perimeter, not only a list of material subsidiaries. Apply the threshold to the statutory preceding-period consolidated net sales separately from this entity-inclusion test. [Act §14d(2)–(4)][law]; [Vero detailed guidance §2][detail].

The Finnish ultimate parent generally files the full report. A foreign parent's report can reach Finland through exchange, but the Finnish entity must establish the parent's obligation and applicable exchange arrangements. If that route fails, examine surrogate and exceptional Finnish local-filing requirements; foreign ownership alone does not settle the issue. [CbCR overview][overview]

For non-euro accounts, the overview describes the ultimate parent's jurisdictional threshold and January 2015 currency basis. Do not mechanically convert the euro threshold at today's rate. Preserve the foreign law and January 2015 conversion evidence; the report currency is a separate choice from the threshold test. [CbCR overview][overview]

### Secondary and surrogate filing: apply each condition

Section 14d requires the Finnish secondary-filing screen where the foreign parent has no CbCR obligation, the specified non-EU international-agreement route lacks a CbCR exchange agreement by the deadline, or Vero has notified the relevant systemic failure. The threshold and entity conditions still apply. [Section 14d(5)][law]

A designated EU group filer can remove the secondary duty under the statutory conditions, but cannot be appointed under that exception without all required report information. For a designated non-EU filer, verify all five gates: local reporting obligation, timely Finnish exchange agreement, no relevant systemic-failure notification, notification in that jurisdiction and notification to Vero. Keep evidence for every gate. [Section 14d(7)][law]

If the parent refuses information despite a request, preserve the request/refusal, notify Vero and report the information obtained/held under the statutory rule; do not simply omit filing. The Act also extends specified duties to standalone foreign enterprises with qualifying Finnish PEs, Finnish partnerships and certain Finnish-organised entities without a tax residence. [Section 14d(6), (8) and (10)][law]

### Compile the report rather than only testing revenue

Under §14e, aggregate each tax jurisdiction's constituent-entity revenues, pre-tax profit/loss, paid and accrued income/source taxes, book equity, retained earnings, employees and tangible assets excluding cash/cash equivalents. Include the reporting entity's own jurisdiction and entities without residence, not only foreign subsidiaries. Retain entity/TIN, residence/incorporation jurisdiction, main activities, data-source and currency information. The threshold's consolidated-sales elimination is **not** permission to eliminate all intercompany revenue from jurisdictional report rows. [Act §14e][law].

Use one documented source policy consistently: consolidation packages, statutory/regulatory accounts or management reports. Explain changes and bridge the reporting period to the group's period. Split unrelated-party and associated-party revenue, exclude covered intercompany dividends, and report losses as negative figures. Attribute PE information to the PE jurisdiction, avoiding a second inclusion in the head-office totals. Distinguish cash income tax paid (including relevant withholding) from current-period accrued tax; deferred tax and prior-period provisions do not become current accrued tax merely because posted now. Keep a reconciliation for equity, retained earnings, full-time-equivalent employees and net tangible-asset values. [Detailed guidance §§5.1–5.3][detail].

For periods beginning from 1 January 2020, exclude covered intercompany dividends from **pre-tax profit/loss** as well as revenue; exclude their paid/accrued income taxes, including source withholding, from the tax rows. Group contributions are not revenue and are excluded from reported pre-tax profit/loss. Report book equity excluding retained earnings, with retained earnings in its separate field; PE equity/retained earnings belong to the head-office legal entity except the specified regulatory-capital case. These are the current guidance's §§5.3.1–5.3.5 rules, not the archived 2017 dividend treatment. The detailed guidance's older transmission references do not replace the current MyTax/Ilmoitin instructions below. [Current detailed CbCR guidance][detail].

Choose the report currency, document conversion rates and retain the source-currency bridge. MyTax permits the ultimate parent's consolidated-financial-statement currency; that choice does not change the threshold's January 2015 conversion route. In the CSV route report financial amounts as integers, use the official current-year template, country codes or X5 for no residence and the required entity/activity fields. An upload populates a draft: validate, preview and submit it. [MyTax report instructions][report]; [CSV instructions][csv].

## Deadlines and filing

The notification instructions cover Finnish-resident companies and qualifying Finnish PEs in an in-scope group. The PE condition refers to separate financial statements prepared for specified reporting, regulatory, tax or management purposes. Determine the full-report filer before completing the notification. [Notification instructions][notification]

Prepare the reporting entity's name, Finnish Business ID or foreign identifier as applicable, and the jurisdiction receiving the report. Preserve the filer-role decision and any other Finnish entities included in the notification. Vero describes including other Finnish subsidiaries in one notification; record which entities it actually covers rather than assuming group-wide completion. [Notification instructions][notification]

The MyTax guidance distinguishes an unfinished saved notification from a submitted one. Preview it, submit it and preserve the confirmation. Verify amendments and the represented entities before using a prior notification as a template. [Notification instructions][notification]

The notification is due at the reported period's end; the report and refusal notice are due within twelve months afterwards. For a calendar 2026 period, the unadjusted statutory dates are 31 December 2026 and 31 December 2027. Calendar the actual period and any statutory holiday rule rather than assuming notification and report share a deadline. [Act §14d(11)][law].

Use MyTax for notification and full report or Ilmoitin.fi using the appropriate year-specific notification/XML specification. Agents need the applicable Suomi.fi authorisation. Reconcile identifiers, roles and constituent entities, preserve the submission acknowledgement and resolve validation failures. Correct the submitted report through its correction route with a complete reconciled replacement; a saved template or CSV upload is not proof of filing. No taxpayer account upload is performed by this Guide. [Vero overview][overview]; [report instructions][report].

## Penalties and interest

Specified late, materially incomplete or incorrect CbCR notification/report failures carry a discretionary tax increase up to EUR 25,000 under §§32(1)(3),32a. It is not an automatic flat fee, not a threshold for tolerating missing entities and not a substantive transfer-pricing tax ceiling. Preserve the hearing, explanation and decision. No tax amount is computed from CbCR's revenue table itself; interest on an actual assessed tax follows its own decision and [prepayment rules](fi-prepayments.md). [Act §§32–32a][law].

## Cross-border points

For a foreign parent or surrogate, preserve the applicable reporting law, exchange agreement in force by the deadline, foreign notification and actual filing evidence. Check current exchange/systemic-failure status for that jurisdiction at filing; do not assume last year's exchange relationship still suffices. A refused parent-data request requires the statutory refusal notice and available-data report, not silence. CbCR aggregates are risk-assessment data; they do not establish an arm's-length price or a formulary allocation of taxable profit. [Act §§14d–14e,31][law].

## Two worked examples that recompute

### 1. Consolidated threshold

Assume euro-denominated consolidated net sales for the preceding period consist of EUR 760 million external revenue and EUR 40 million intragroup revenue eliminated in consolidation. The consolidated amount is EUR 760 million, EUR 10 million above the screening threshold. This assumes the consolidation is correct and the international-structure conditions are met; it does not identify the filer or establish local-filing duties.

```oa-check
name: Finland CbCR assumed consolidation threshold
inputs:
  external_revenue: 760000000
  intragroup_revenue: 40000000
  eliminated_intragroup_revenue: 40000000
  threshold: 750000000
steps:
  before_eliminations: external_revenue + intragroup_revenue
  consolidated_revenue: before_eliminations - eliminated_intragroup_revenue
  excess_over_threshold: consolidated_revenue - threshold
expected:
  before_eliminations: 800000000
  consolidated_revenue: 760000000
  excess_over_threshold: 10000000
```

### 2. Jurisdiction revenue reconciliation

Assume two constituent entities in one jurisdiction have unrelated-party revenues EUR 40 million and EUR 15 million, related-party revenues EUR 8 million and EUR 3 million, and no excluded dividends. The CbCR jurisdiction row includes EUR 55 million unrelated plus EUR 11 million related, total EUR 66 million. Do not eliminate the EUR 11 million using the threshold's consolidated-sales calculation. Source, currency and entity classifications are assumed established.

```oa-check
name: Finland CbCR jurisdiction revenue aggregation
inputs:
  entity_a_unrelated: 40000000
  entity_b_unrelated: 15000000
  entity_a_related: 8000000
  entity_b_related: 3000000
steps:
  unrelated_revenue: entity_a_unrelated + entity_b_unrelated
  related_revenue: entity_a_related + entity_b_related
  jurisdiction_total: unrelated_revenue + related_revenue
expected:
  unrelated_revenue: 55000000
  related_revenue: 11000000
  jurisdiction_total: 66000000
```

## Ask the client first

- What are the group period, consolidation basis, currency and preceding-period revenue?
- Which entity files the full report, where, and with what foreign-law/exchange evidence?
- Which Finnish entities and PEs need notification, and which are already covered?
- What refusal, surrogate arrangement or authority systemic-failure notice exists?
- How do country rows reconcile to entity records, current taxes, employees and assets?
- Which authorisations, submissions, corrections and acknowledgements exist?

## Sources

| Official source | Scope | Read date |
|---|---|---|
| [Assessment Procedure Act 1558/1995][law] | §§14d–14e,31–32a | 2026-10-26 |
| [Vero CbCR overview][overview] | Currency threshold, transmission and notification | 2026-10-26 |
| [Vero detailed CbCR guidance][detail] | §§4–5: roles and data definitions | 2026-10-26 |
| [MyTax full-report instructions][report] | Report roles, currency and submission | 2026-10-26 |
| [CSV instructions][csv] | Format and field aggregation | 2026-10-26 |
| [Notification instructions][notification] | Reporting entity and covered entities | 2026-10-23 |

Not yet confirmed: no taxpayer-specific foreign exchange relationship or filing is assumed. Confirm those live facts for the reporting period; the statutory ordinary reporting method is set out above.

[law]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[overview]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/
[report]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/country-by-country-report---how-to-file-the-report-in-mytax/
[notification]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/notification-of-the-reporting-entity-how-to-file-the-notification-in-mytax/
[detail]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/49771/verotuksen-maakohtainen-raportti3/
[csv]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/country-by-country-reporting-guidance-for-generating-csv-files/
