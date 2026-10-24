---
name: fi-country-by-country-reporting
description: >
  Screen Finland country-by-country reporting, identify the reporting entity,
  distinguish notification from the full report and prepare submission records.
  Local-filing exceptions, current statutory reconciliation and exchange checks
  remain outstanding.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.4
---

# Finland country-by-country reporting v0.4

## Who this applies to

Vero's guidance uses preceding-period consolidated net sales of **at least EUR 750 million**, together with the relevant international structure, for CbCR screening. The full-report instructions also address Finnish-resident standalone enterprises with a foreign PE. This is a group reporting test, distinct from the documentation-size rules in the [transfer-pricing Guide](fi-transfer-pricing.md). [Full-report instructions][report]

Read the source and limits below before using this draft for a filing. Assessment Procedure Act sections 14d–14e, 32 and 32a were directly checked in the official Finnish statutory text on 23 October 2026. Live exchange relationships, detailed application and named Finnish accountant review remain open. [Assessment Procedure Act][law]

## Filing roles and the threshold

The Finnish ultimate parent generally files the full report. A foreign parent's report can reach Finland through exchange, but the Finnish entity must establish the parent's obligation and applicable exchange arrangements. If that route fails, examine surrogate and exceptional Finnish local-filing requirements; foreign ownership alone does not settle the issue. [CbCR overview][overview]

For non-euro accounts, the overview describes the ultimate parent's jurisdictional threshold and January 2015 currency basis. Do not mechanically convert the euro threshold at today's rate. The detailed currency and local-filing rules still require case-specific verification. [CbCR overview][overview]

### Secondary and surrogate filing: apply each condition

Section 14d requires the Finnish secondary-filing screen where the foreign parent has no CbCR obligation, the specified non-EU international-agreement route lacks a CbCR exchange agreement by the deadline, or Vero has notified the relevant systemic failure. The threshold and entity conditions still apply. [Section 14d(5)][law]

A designated EU group filer can remove the secondary duty under the statutory conditions, but cannot be appointed under that exception without all required report information. For a designated non-EU filer, verify all five gates: local reporting obligation, timely Finnish exchange agreement, no relevant systemic-failure notification, notification in that jurisdiction and notification to Vero. Keep evidence for every gate. [Section 14d(7)][law]

If the parent refuses information despite a request, preserve the request/refusal, notify Vero and report the information obtained/held under the statutory rule; do not simply omit filing. The Act also extends specified duties to standalone foreign enterprises with qualifying Finnish PEs, Finnish partnerships and certain Finnish-organised entities without a tax residence. [Section 14d(6), (8) and (10)][law]

## Notification of the reporting entity

The notification instructions cover Finnish-resident companies and qualifying Finnish PEs in an in-scope group. The PE condition refers to separate financial statements prepared for specified reporting, regulatory, tax or management purposes. Determine the full-report filer before completing the notification. [Notification instructions][notification]

Prepare the reporting entity's name, Finnish Business ID or foreign identifier as applicable, and the jurisdiction receiving the report. Preserve the filer-role decision and any other Finnish entities included in the notification. Vero describes including other Finnish subsidiaries in one notification; record which entities it actually covers rather than assuming group-wide completion. [Notification instructions][notification]

The MyTax guidance distinguishes an unfinished saved notification from a submitted one. Preview it, submit it and preserve the confirmation. Verify amendments and the represented entities before using a prior notification as a template. [Notification instructions][notification]

## Dates and submission

Section 14d(11) requires the reporting-entity notification **by the final day of the reported accounting period** and the report/refusal notification **within twelve months after that day**. Track them separately. Section 14e specifies jurisdiction data and entity/activity/source/currency information. Confirm the actual period, including a year-end change. [Assessment Procedure Act][law]; [full-report instructions][report]

Vero's 2023 service-change notice describes an extension request through MyTax where notification cannot be made on time. It does not itself establish a granted extension for a current taxpayer. Obtain the applicable authority decision before relying on a later date. The notice records the closure of Lomake.fi in February 2024; preserve it as historical service evidence. [Service-change notice][service]

The current MyTax full-report instructions offer individual entry and CSV upload for financial/entity data. The overview also describes Ilmoitin.fi and XML; use the current specification for the selected route and report year. Check agent authorisation and preserve the submission confirmation. No live account or file upload was tested. [Full-report instructions][report]; [CbCR overview][overview]

## Penalty screen

Sections 32(1)(3) and 32a provide a maximum EUR 25,000 increase for the specified late or materially incomplete/incorrect CbCR notification/report failures. Establish the actual breach, procedure and decision; the maximum is not an automatic charge and does not replace the missing information. [Assessment Procedure Act][law]

## Preparation workpaper

This is our practical reconciliation framework, not an additional statutory form:

1. Record the reported period, previous-period revenue, consolidation basis and entities included.
2. Identify the ultimate parent, reporting entity and any surrogate or proposed local filer.
3. Obtain evidence of foreign filing obligations and exchange conditions.
4. Reconcile jurisdiction totals and constituent-entity identifiers to the underlying records.
5. Track notification and full-report submission separately, retaining confirmations and corrections.

## Worked example

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

### 2. Exact threshold boundary

The [full-report instructions][report] were opened directly on 23 October 2026 and say EUR 750 million **or more**. Assume established preceding-period euro consolidated net sales of exactly EUR 750 million and the required international structure. The numerical threshold is met at equality; filer identity and exceptional local-filing conditions still need their separate tests.

```oa-check
name: Finland CbCR exact assumed euro threshold
inputs:
  established_consolidated_revenue: 750000000
  threshold: 750000000
steps:
  difference_from_threshold: established_consolidated_revenue - threshold
expected:
  difference_from_threshold: 0
```

## Ask the client first

- What are the group period, consolidation basis, currency and preceding-period revenue?
- Which entity files the full report, in which jurisdiction, and with what evidence?
- Which Finnish entities and PEs exist, and what notifications already cover them?
- Are there exchange failures, surrogate arrangements or authority notices?
- What submission confirmations and corrections are available?

## Sources and review limits

Official Vero text retrieved through the search index on 23 October 2026:

- [Consolidated Finnish Assessment Procedure Act][law], sections 14d–14e, 32 and 32a, read directly from the official page's embedded statutory text; retrieval hashes are in the country research record.

- [CbCR overview][overview].
- [Full-report MyTax instructions][report].
- [Reporting-entity notification instructions][notification].
- [MyTax service-change notice][service].

Not yet confirmed: remaining amendment/procedural interactions; case-specific secondary/surrogate eligibility and live exchange relationships; detailed data-category definitions; current transmission schemas and authorisations; actual extension decisions and calendar application. Named Finnish accountant review remains outstanding; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action). Reporting and country coverage remain partial.

[law]: https://www.finlex.fi/fi/lainsaadanto/1995/1558

[overview]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/
[report]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/country-by-country-report---how-to-file-the-report-in-mytax/
[notification]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/notification-of-the-reporting-entity-how-to-file-the-notification-in-mytax/
[service]: https://vero.fi/en/About-us/newsroom/news/uutiset/2023/country-by-country-reporting-in-mytax/
