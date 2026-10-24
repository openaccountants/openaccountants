---
name: gr-vat-return
description: "Pointer for Greek VAT (ΦΠΑ) returns, tax year 2026. The full method lives in greece-vat-return: the VAT Code ratified by ν. 5144/2024 (which replaced ν. 2859/2000), the 24%, 13%, 6% and 4% rates, the 30% island reduction from 1 January 2026, the EUR 10,000 small business exemption and EU SME scheme, monthly and quarterly periodic returns and payment, input VAT and blocked costs, the reverse charge, intra-EU rules, OSS, refunds to foreign businesses and Tax Procedure Code fines. Trigger on \"Greek VAT return\", \"ΦΠΑ\", \"do the VAT Greece\", \"myAADE VAT\", \"TAXISnet VAT\". Load greece-vat-return instead of this file. Out of scope here: everything; see greece-vat-return, greece-einvoice (myDATA and e-invoicing) and gr-tax-overview."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gr-vat-return"
  jurisdiction: "GR"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Greek VAT return: use greece-vat-return (v0.1)

This file used to hold a copy of the Greek VAT return skill written under the old VAT Code (ν. 2859/2000), with 2025 figures and island rates that no longer match the law. It is now a pointer. Load **greece-vat-return** for the 2026 method, figures, worked examples and sources.

Headline 2026 figures, all from the VAT Code (ν. 5144/2024) in the Ministry of Finance codification to ν. 5313/2026:

- Rates: 24% standard; 13% for Annex III goods and services; 6% and 4% where Annex III says so (art. 26(1)).
- Islands: from 1 January 2026, rates are cut by 30% (to 17%, 9%, 4% and 3%) on the islands of the North Aegean Region, Samothrace and the Dodecanese with up to 20,000 inhabitants (art. 26(4A), (6)). Lesvos, Kos, Samos and Chios get the same cut under art. 26(4) through decision Α.1150/2021, which AADE circular Ε.2113/2025 confirms is still in force. The islands are listed in the annex to Ε.2113/2025. Tobacco and means of transport never get it (art. 26(4B)).
- Small business exemption: Greek turnover up to EUR 10,000 in the previous and current year (art. 44α(1)).
- Returns: monthly on double-entry books, quarterly on single-entry books, due by the last working day of the following month (art. 43(1), (4)).

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Code (ν. 5144/2024), Ministry of Finance administrative codification to ν. 5313/2026, arts. 26, 43, 44α | https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf | 2026-10-23 |
| AADE circular Ε.2113/31.12.2025 on the 30% island reduction, with the annex of islands | https://www.aade.gr/sites/default/files/2026-01/e2113_2025.pdf | 2026-10-23 |

Not yet confirmed: see the list at the end of greece-vat-return.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gr-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gr-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
