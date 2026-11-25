---
name: singapore-transfer-pricing
description: "Use this skill whenever asked about Singapore transfer pricing rules, documentation or IRAS compliance for Year of Assessment 2026 and 2027. Trigger on transfer pricing Singapore, Singapore TP documentation, section 34D, section 34E surcharge, section 34F, IRAS transfer pricing, master file Singapore, local file Singapore, related party transactions form, RPT S$15 million, cost plus 5% routine support services, related party loans indicative margin, APA Singapore. Covers the arm's length rule, who must prepare documentation (gross revenue over S$10 million), timing, 5-year retention, the S$10,000 fine, the 5% surcharge on the amount of a section 34D adjustment, the RPT form in Form C, and the 5% cost mark-up for routine support services."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/singapore-transfer-pricing"
  jurisdiction: "SG"
  tax_year: "2026"
  last_updated: "2026-11-22"
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

1. **Apply the arm's length principle.** Where related party conditions differ from arm's length conditions, IRAS may adjust to increase the Singapore profit or reduce the loss (section 34D(1A)). Select the method that gives the most reliable result from the available data and comparability adjustments. Consider comparable uncontrolled price (CUP), resale price, cost plus, transactional net margin (TNMM) or profit split.
2. **Is documentation required?** Yes if gross revenue from the trade or business is more than S$10 million for the basis period, or documentation was required for the immediately preceding basis period. Exemptions in the Rules cover, for example, domestic related party transactions (other than loans) between parties subject to the same tax rate, and transactions at or below the applicable category thresholds. From YA 2026, the separate category limits are S$15 million each for goods bought, goods sold, loans granted and loans received, and S$2 million for each specified category of other transactions. Apply the Rule 4 aggregation and exclusion rules.
3. **What it holds.** A group overview relevant to the Singapore operations and detailed entity information: functional analysis and transfer pricing analysis of the related party transactions (in line with the OECD master file and local file).
4. **When.** Complete it by the filing due date of the income tax return; do not submit it with the return; provide it within 30 days starting on the date IRAS serves its written notice. A simplified document can use qualifying documentation for the same related party and transaction type from either of the previous two basis periods if the conditions in Rule 3 are met. From YA 2026, include a dated declaration and attach the qualifying documentation. Keep it at least 5 years from the end of the basis period of the transaction.
5. **RPT form.** If related party transactions disclosed in the financial statements exceed S$15 million, answer "Yes" at item 31 of Form C and complete the Related Party Transactions tab. Total the related party income statement amounts other than key management compensation, directors’ fees and dividends, then add the year-end balances of loans and non-trade amounts due to or from related parties.
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
| Surcharge on an adjustment under section 34D (section 34E, from YA 2019) | 5% of the adjustment, whether or not extra tax results | same |
| RPT form in Form C, related party transactions over | S$15 million | same |
| Routine support services mark-up (Annex C) | cost plus 5% | same |
| OECD simplified approach for low value-adding services | 5% profit mark-up | same |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Gross revenue S$9 million this year, but documentation was required last year | Documentation still required this year for transactions outside the Rule 4 exemptions |
| Domestic sale of goods between two Singapore companies taxed at the same rate | Exempt from documentation (not a loan) |
| Domestic related party loan | Loan-specific exemptions apply. Check the agreement date, whether each party carries on a borrowing and lending business and whether the parties agreed to the indicative margin |
| IRAS adjustment produces no extra tax (for example, losses) | 5% surcharge still applies to the adjustment amount; IRAS may remit for good cause |
| Uncharged or notional share-based compensation costs | Include all share-based compensation costs in the TNMM full cost mark-up base. From YA 2026, exclude uncharged or notional costs from the service revenue computation. The one-off measure required revised computations by 15 November 2026 for YA 2022 and by 28 February 2027 for YAs 2023 to 2025 |
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

Case 2, decision: charge routine support at cost plus 5% or do a benchmark? A Singapore company provides only to group companies Annex C support services costing S$800,000 in total (all costs included). At cost plus 5% the charge is S$840,000 and IRAS is prepared to accept it without a benchmarking study. A reliable benchmark supporting a 3% mark-up for these services gives a charge of S$824,000 and S$16,000 less Singapore service income. If the entire difference is taxed at 17%, the Singapore company’s tax difference is S$2,720 before exemptions, losses, rebates and foreign effects. Choose a defensible pricing method and compare the expected tax effects and compliance costs for both parties.

```oa-check
name: Routine support services, cost plus 5% versus a 3% benchmark
inputs:
  costs: 800000
steps:
  - charge_5: costs * 1.05
  - charge_3: costs * 1.03
  - difference: charge_5 - charge_3
  - tax_difference: difference * 0.17
expected:
  charge_5: 840000.00
  charge_3: 824000.00
  difference: 16000.00
  tax_difference: 2720.00
```

## When to refuse or refer

| Trigger | Message |
| --- | --- |
| APA, MAP or arbitration | "These follow IRAS's dispute prevention and resolution guidance; refer." |
| Country-by-country reporting | "CbCR has its own rules and thresholds; refer." |
| Pillar Two (income inclusion rule, domestic top-up tax) | "Out of scope; refer." |
| Intangibles migration, cost contribution arrangements, financial guarantees | "Complex; refer." |

## Filing and payment

Documentation is kept, not filed. The RPT form is part of Form C when the S$15 million test is met. Pay the section 34E surcharge within one month after IRAS serves written notice, including during an objection or appeal, unless the deadline is extended.

## Completion checklist

- Revenue test and prior-year test done; exemptions checked transaction by transaction.
- Documentation dated by the return due date; retention diarised.
- RPT form test done from the financial statements.
- Routine services checked against Annex C and the "only related parties" condition.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRAS transfer pricing (read for documentation deadlines and fines, RPT calculation, routine services, loan margins and the transitional share-based compensation deadlines) | https://www.iras.gov.sg/taxes/corporate-income-tax/specific-topics/transfer-pricing | 2026-11-24 |
| IRAS Transfer Pricing Guidelines, ninth edition (read for paragraphs 5.105, 5.120, 6.18, 9.7 and 10.50 on reliable methods, remuneration, documentation exemptions, surcharge exceptions and APA fees) | https://www.iras.gov.sg/media/docs/default-source/e-tax/etaxguide_cit_transfer-pricing-guidelines.pdf | 2026-11-24 |
| Income Tax Act 1947 (read for sections 34D to 34F on adjustment powers, surcharge and documentation) | https://sso.agc.gov.sg/Act/ITA1947?ProvIds=pr34D-,pr34E-,pr34F-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |
| Transfer Pricing Documentation Rules 2018 (read for rule 4 category aggregation, thresholds and other exemptions) | https://sso.agc.gov.sg/SL/ITA1947-S93-2018?ProvIds=pr4-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |
| Transfer Pricing Documentation Rules 2018 (read for rule 3 qualifying past documentation and dated declaration) | https://sso.agc.gov.sg/SL/ITA1947-S93-2018?ProvIds=pr3-&ValidDate=20261122&ViewType=Advance | 2026-11-24 |
| IRAS corporate income tax rates (read for the standard 17% rate used in case 2) | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes | 2026-11-24 |

Not yet confirmed: the client’s APA processing time, any charges for a unilateral case involving a jurisdiction without a tax treaty with Singapore, and whether a particular pricing benchmark is reliable for the client’s facts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `singapore-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/singapore-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
