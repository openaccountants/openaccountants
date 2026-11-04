---
name: gf-import-octroi-and-vat
description: "French Guiana goods-import reference for businesses and other importers using the July 2026 territorial octroi de mer tariff. Distinguishes VAT non-application from external and regional octroi, explains customs-value calculations and separates import rates from local-production rates. Includes verified tariff examples, evidence needed before claiming exemptions, and the date boundary for the revised tariff. Covers goods rather than services, and does not determine customs classification, origin preferences, valuation adjustments or every relief. This source-cited draft requires independent review and transaction-specific confirmation before a customs declaration is filed."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gf-import-octroi-and-vat"
  jurisdiction: "GF"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# French Guiana: goods imports, octroi de mer and VAT

## Scope and filing basis

French customs states that VAT is not applicable in Guyane, while imports are within external octroi de mer regardless of provenance, subject to exemptions. Regional octroi shares its base. The base is customs value; liability arises on entry or release for consumption following a suspensive regime, and assessment is on the customs declaration. An invoice without VAT therefore does not establish a tax-free import. [Customs import guidance](https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom).

This Guide uses the enacted **AP-2026-47 tariff effective 1 July 2026**, article 4. Earlier transactions require the earlier schedule. Article 1 replaces the tariff annex previously amended in January 2026; article 2 leaves the framework's other provisions unchanged. [Deliberation, pages 2–3](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf).

## Select the correct tariff column

The annex separates **external taxation** (imports) from **internal taxation** (local production), each with separate octroi and regional-octroi columns. These are not interchangeable. Physical PDF page 5, labelled tariff page 2 of 198, gives:

| Code and goods | Import OM | Import OMR | Internal OM | Internal OMR |
|---|---:|---:|---:|---:|
| 0101 21 00: live pure-bred breeding horses | 2% | 3% | 2% | 3% |
| 0105 11 11: female breeding/multiplication chicks of laying breeds, within the heading's weight conditions | 7% | 3% | 0% | 1% |

[Enacted tariff annex, physical page 5](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf). These are classification-specific examples, not general animal or agricultural rates. The internal figures illustrate why choosing the column matters; they do not establish whether a producer is liable or exempt.

## Calculation workflow

1. Record the declaration/chargeable-event date, exact goods specification, tariff classification, origin and customs procedure.
2. Establish customs value from the valuation rules and supporting invoice, freight and insurance evidence. This Guide does not independently resolve valuation adjustments.
3. Retrieve the date-effective tariff row and use its two **external** rates.
4. Test a claimed exemption against the operative deliberation, activity code, goods code, end use and evidence. The CTG publishes separate legally operative annexes and Excel convenience versions expressly labelled non-binding. Its economic-activity relief does not automatically remove regional octroi. [CTG tariff and relief index](https://www.ctguyane.fr/octroi-de-mer-tarif-exoneration/).
5. Compute each levy separately on the confirmed base, then reconcile to the customs declaration. Keep other customs charges separate; the examples below calculate only OM and OMR.

Assume a confirmed customs value of **€10,000**, the stated code, and no exemption:

- Code 0101 21 00: €10,000 × 2% = €200 OM; €10,000 × 3% = €300 OMR; **€500 total**.
- Code 0105 11 11: €700 OM + €300 OMR = **€1,000 total**. Substituting its internal 0%/1% columns would incorrectly produce €100.

The customs-value base and same-base treatment come from [customs guidance](https://www.douane.gouv.fr/demarche/importer-un-bien-dans-un-drom); the rates come from the [July tariff](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf). Examples assume all classification conditions have been proved and exclude other charges.

## Exemptions and boundaries

Do not price goods using the historic average rates on older customs summaries. The operative product row and any valid relief control the result. CTG lists production and non-production activity annexes with different effective dates, plus a distinct space-sector regime from August 2026. Check the applicable annex rather than inferring eligibility from an industry label. [CTG index](https://www.ctguyane.fr/octroi-de-mer-tarif-exoneration/).

Article 3 of AP-2026-47 preserves relevant exemption treatment following a simple nomenclature update only for corresponding products, pending a new local deliberation; it does not permit changing the nature or destination of goods. Document any code correspondence. [Deliberation, pages 2–3](https://www.ctguyane.fr/www/wp-content/uploads/2026/07/delib.ctg-ap-2026-47-modif-tgom-2026-complet.pdf).

## Self-checks and limitations

Confirm the transaction date, external column, exact code, customs value and both levies. Retain the enacted schedule and any exemption evidence with the declaration. Do not use the example as a binding classification ruling.

Source-cited draft awaiting independent review. Services, income taxes, full exemption procedures, local-production liability, penalties, origin and valuation disputes are outside scope. The complete post-July amendment chain has not been independently reviewed. VAT code recodification and precise invoice wording require separate current-law verification.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gf-import-octroi-and-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gf-import-octroi-and-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
