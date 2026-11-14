---
name: singapore-transfer-pricing
description: "Use this skill whenever asked about Singapore transfer pricing rules, documentation or IRAS compliance for Year of Assessment 2026 and 2027. Trigger on transfer pricing Singapore, Singapore TP documentation, section 34D, section 34E surcharge, section 34F, IRAS transfer pricing, master file Singapore, local file Singapore, related party transactions form, RPT S$15 million, cost plus 5% routine support services, related party loans indicative margin, APA Singapore. Covers the arm's length rule, who must prepare documentation (gross revenue over S$10 million), timing, 5-year retention, the S$10,000 fine, the 5% surcharge on the amount of any adjustment, the RPT form in Form C, and the 5% cost mark-up for routine support services."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/singapore-transfer-pricing"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Singapore transfer pricing, YA 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Have a qualified adviser review before relying on it.

## Scope

Transactions between related parties of a Singapore taxpayer: the arm's length rule in section 34D of the Income Tax Act 1947, the surcharge in section 34E, documentation under section 34F and the Income Tax (Transfer Pricing Documentation) Rules 2018, and IRAS's e-Tax Guide on Transfer Pricing Guidelines. Singapore is not an OECD member but follows the OECD Transfer Pricing Guidelines and is in the Inclusive Framework. Corporate tax computation: `sg-income-tax` and the company skill; GST valuation effects: `singapore-gst`.

## Ask the client first

1. **Gross revenue** from the trade or business for the basis period, and whether documentation was required for the previous basis period.
2. **The related party transactions**: types (goods, services, loans, royalties), counterparties, countries, values.
3. **Value of related party transactions in the financial statements** (RPT form test).
4. **Any concessionary rate or incentive** in Singapore for either party.
5. **Routine support services** provided only to related parties.
6. **Group size** (country-by-country reporting) and any APA or MAP in place.

## The method, step by step

1. **Apply the arm's length principle.** Where related party conditions differ from arm's length conditions, IRAS may adjust to increase the Singapore profit or reduce the loss (section 34D(1A)). Use the most appropriate method (CUP, resale price, cost plus, TNMM, profit split); there is no strict hierarchy, and CUP is preferred where reliable comparables exist.
2. **Is documentation required?** Yes if gross revenue from the trade or business is more than S$10 million for the basis period, or documentation was required for the immediately preceding basis period. Exemptions in the Rules cover, for example, domestic related party transactions (other than loans) between parties subject to the same tax rate, and transactions below category thresholds.
3. **What it holds.** A group overview relevant to the Singapore operations and detailed entity information: functional analysis and transfer pricing analysis of the related party transactions (in line with the OECD master file and local file).
4. **When.** Complete it by the filing due date of the income tax return; do not submit it with the return; provide it within 30 days of an IRAS request. It may be refreshed once every 3 years, with a simplified document in between, if the details stay accurate and relevant. Keep it at least 5 years from the end of the basis period of the transaction.
5. **RPT form.** If related party transactions disclosed in the financial statements exceed S$15 million, answer "Yes" at item 31 of Form C and complete the Related Party Transactions tab.
6. **Routine support services.** Services in Annex C of the e-Tax Guide provided only to related parties may be charged at cost plus 5%, counting all costs. Services outside Annex C may use the 5% profit mark-up of the OECD simplified approach for low value-adding intra-group services if its conditions are met.
7. **Related party loans.** IRAS publishes indicative margins over base reference rates (for example, risk-free rates such as SORA) for qualifying loans; check the current table on the IRAS page.

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Documentation required, gross revenue more than | S$10 million | https://www.iras.gov.sg/taxes/corporate-income-tax/specific-topics/transfer-pricing |
| Provide documentation after an IRAS request | 30 days | same |
| Refresh cycle | once every 3 years | same |
| Retention | at least 5 years from the end of the basis period | same |
| Fine for documentation offences (from YA 2019) | up to S$10,000 | same |
| Surcharge on a transfer pricing adjustment (s. 34E, from YA 2019) | 5% of the adjustment, whether or not extra tax results | same |
| RPT form in Form C, related party transactions over | S$15 million | same |
| Routine support services mark-up (Annex C) | cost plus 5% | same |
| OECD simplified approach for low value-adding services | 5% profit mark-up | same |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Gross revenue S$9 million this year, but documentation was required last year | Documentation still required this year |
| Domestic sale of goods between two Singapore companies taxed at the same rate | Exempt from documentation (not a loan) |
| Domestic related party loan | Not covered by the domestic exemption; check the loan rules |
| IRAS adjustment produces no extra tax (for example, losses) | 5% surcharge still applies to the adjustment amount; IRAS may remit for good cause |
| Uncharged or notional share-based compensation costs | IRAS set out a revised position for YA 2026 and a one-off measure for YAs 2022 to 2025; read the IRAS page before advising |
| Routine services also sold to third parties | The 5% Annex C mark-up does not apply |

## Worked cases

Case 1. IRAS adjusts a company's related party service income upwards by S$2,000,000 for YA 2026. The company has tax losses, so no extra tax arises. The section 34E surcharge is 5% of the adjustment: S$100,000, payable unless IRAS remits it.

```oa-check
name: Section 34E surcharge on a S$2 million adjustment
inputs:
  adjustment: 2000000
steps:
  - surcharge: adjustment * 0.05
expected:
  surcharge: 100000.00
```

Case 2, decision: charge routine support at cost plus 5% or do a benchmark? A Singapore company provides only to group companies Annex C support services costing S$800,000 in total (all costs included). At cost plus 5% the charge is S$840,000 and IRAS is prepared to accept it without a benchmarking study. A benchmark showing a 3% median would give S$824,000, S$16,000 less income, but needs a study and carries audit risk. The figure that decides it is whether S$16,000 of income outweighs the cost of the study.

```oa-check
name: Routine support services, cost plus 5% versus a 3% benchmark
inputs:
  costs: 800000
steps:
  - charge_5: costs * 1.05
  - charge_3: costs * 1.03
  - difference: charge_5 - charge_3
expected:
  charge_5: 840000.00
  charge_3: 824000.00
  difference: 16000.00
```

## When to refuse or refer

| Trigger | Message |
| --- | --- |
| APA, MAP or arbitration | "These follow IRAS's dispute prevention and resolution guidance; refer." |
| Country-by-country reporting | "CbCR has its own rules and thresholds; refer." |
| Pillar Two (income inclusion rule, domestic top-up tax) | "Out of scope; refer." |
| Intangibles migration, cost contribution arrangements, financial guarantees | "Complex; refer." |

## Filing and payment

Documentation is kept, not filed. The RPT form is part of Form C when the S$15 million test is met. The surcharge is raised by IRAS with the adjustment.

## Completion checklist

- Revenue test and prior-year test done; exemptions checked transaction by transaction.
- Documentation dated by the return due date; retention diarised.
- RPT form test done from the financial statements.
- Routine services checked against Annex C and the "only related parties" condition.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the section 34F documentation requirements, exemptions, timing, refresh, retention, S$10,000 fine, 5% surcharge, RPT form at S$15 million, 5% routine support services and OECD simplified approach, indicative loan margins, the YA 2026 share-based compensation position | https://www.iras.gov.sg/taxes/corporate-income-tax/specific-topics/transfer-pricing | 2026-11-14 |

Not yet confirmed: the country-by-country reporting threshold (old file: consolidated revenue of S$1,125 million) and filing deadline (12 months); the APA fees (old file S$10,000 and S$30,000) and processing times; the edition and date of the e-Tax Guide (old file: 8th edition, November 2025); the 4-year time limit for assessments in the old file; the category thresholds for documentation exemptions in Rule 4 (in the e-Tax Guide PDF, not opened).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `singapore-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/singapore-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
