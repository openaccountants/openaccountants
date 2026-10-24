---
jurisdiction: LI
version: 0.2
last_updated: 2026-10-24
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: li-income-tax
  IT-CORP: li-corporate-income-tax
  VAT: liechtenstein-vat
  SC: li-payroll-social
  PR: li-payroll-social
  TP: li-transfer-pricing
  XB: li-cross-border
partial:
  IT-IND: "2026 statutory state scales, wealth-income integration and selected loss/withholding rules prepared; full deductions, valuation, actual municipal rates, special cases and named local accountant review remain open."
  IT-CORP: "2026 base, minimum-tax exception, loss cap and equity-deduction preparation added; complete exemption, group, foreign, GloBE and filing application remain open."
  VAT: "2026 authority, registration, rates, acquisition tax, input and filing/correction method prepared; special supplies, complete legal chain, operational fields and named local accountant review remain open."
  SC: "2026 employee AHV/IV/FAK/VK and ALV rates/bases prepared; full self-employed, non-employed, pension/insurance, international and statutory scope remain open."
  PR: "2026 resident/nonresident wage withholding, schedule and remittance preparation added; treaty, benefit, exact calendar, full statutory and named local accountant review remain open."
  TP: "Statutory relationship, documentation routes, thresholds and method preparation added; benchmarks, detailed transaction/size interaction, CbCR and disputes remain open."
  XB: "Domestic residence/source/PE, withholding, selected foreign-credit and corporate exit preparation added; actual treaties, full special cases and operational claims remain open."
---

# Liechtenstein tax pack

Accountable owner: Michael. Active writer: ChatGPT support chat under [OWNERS.md](../../../OWNERS.md) and [issue #406](https://github.com/openaccountants/openaccountants/issues/406), local branch `codex/liechtenstein-country-completion`. This country batch uses consolidated draft [PR #514](https://github.com/openaccountants/openaccountants/pull/514), with one combined country content push after review and correction closure. The primary chat is writing Montenegro; Bosnia and Herzegovina is parked; Finland's reviewed batch is published separately at `af8d6057`, with its coverage gaps preserved.

The tax authority is the Liechtenstein Steuerverwaltung. Use the country's own tax and VAT Acts and its actual authority allocation. Swiss VAT practice applies by analogy with local deviations; it does not send every Liechtenstein taxpayer to the Swiss filing system. Sources below were read on 24 October 2026.

## Domains and existing work

| Domain | Source Guide | Status and next gap |
|---|---|---|
| IT-IND | [li-income-tax](li-income-tax.md) | Source-cited draft; 2026 statutory preparation added, specialist scope open |
| IT-CORP | [li-corporate-income-tax](li-corporate-income-tax.md) | Source-cited draft; 2026 statutory preparation added, specialist scope open |
| VAT | [liechtenstein-vat](liechtenstein-vat.md) | Source-cited draft; local 2026 method corrects filing route and unsupported merchant defaults |
| SC | [li-payroll-social](li-payroll-social.md) | Source-cited draft; ordinary employee contributions prepared, wider insurance coverage open |
| PR | [li-payroll-social](li-payroll-social.md) | Source-cited draft; residents also subject to wage withholding, with current schedule/source exceptions |
| TP | [li-transfer-pricing](li-transfer-pricing.md) | Source-cited draft; 2026 documentation/method preparation, application gaps open |
| XB | [li-cross-border](li-cross-border.md) | Source-cited draft; 2026 domestic/relief method, actual treaty application open |

The [formation](li-company-formation.md) Guide now reconciles selected GmbH/capital/reporting rules; the [overview](li-tax-overview.md) is a router with no standalone rates or liability calculation. Their existence does not resolve any core-domain gap. All eight Guides remain tier 2; no named Liechtenstein accountant review is claimed.

## Source preparation and next action

The local country draft provides 25 executable calculations across seven preparation Guides; the overview is a router. It replaces Swiss payroll approximations and universal Swiss VAT filing instructions with the Liechtenstein 2026 sources. A successful calculation or a source's HTTP response does not establish legal applicability or complete coverage. The dated research record identifies provisions read and access limitations.

The [independent whole-pack source review and correction record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md) identifies exact source revisions, findings and closure status. Apply its stated limits; this is a source/editorial review. Next: resolve the remaining source/application questions, obtain named local accountant review and establish actual filing/claim procedures. Verify publication and exact-head CI on PR #514; a local checkpoint alone is not publication. Keep this issue open and the consolidated PR draft; all seven domains remain partial. Named local accountant review and live filing are separate, unresolved gates.

## Official sources

Read 24 October 2026, scoped to the research record:

- [Tax Act, current consolidation 1 July 2026](https://www.gesetze.li/konso/pdf/2010340000), selected withholding, arm's-length, loss and rate/minimum-tax provisions. This is not a complete annual amendment audit.
- [Liechtenstein VAT Act, current consolidation 1 January 2026](https://www.gesetze.li/konso/pdf/2009330000), selected ordinary registration, supply, rates, deduction and procedure provisions.
- [2026 contribution bulletin](https://www.ahv.li/fileadmin/user_upload/Dokumente/Online-Schalter/MB/AHV-IV-FAK-MB-1-01-2026--AHV-IV-FAK-ALV-Beitraege.pdf), ordinary coverage, rates and contribution bases.
- [Wage-withholding bulletin, February 2026](https://www.llv.li/servicekonto/steuerverwaltung/quellensteuer-lohnsteuer-unselbstaendige-taetigkeit-und-ersatzeinkuenfte-merkblatt.pdf), with January 2026 treaty annex.
- [eMWST route](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/e-mwst), [registration and authority allocation](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/wer-ist-mwst-steuerpflichtig), [rate categories](https://www.llv.li/de/unternehmen/steuern-abgaben-versicherung/mehrwertsteuer/mwst-steuersaetze) and [Swiss practice by analogy](https://www.llv.li/de/landesverwaltung/steuerverwaltung/mehrwertsteuer/publikationen-zur-mehrwertsteuerpraxis).
