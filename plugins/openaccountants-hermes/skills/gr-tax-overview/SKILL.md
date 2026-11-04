---
name: gr-tax-overview
description: "Source-cited draft: map of the Greek tax system for tax year 2026, with each headline figure tied to the law. Covers the tax year, who is taxed on worldwide income, the 2026 personal income tax scale (9% to 44%), the 22% corporate rate, the 24% standard VAT rate, the return windows for individuals and companies, AADE as the tax authority and e-EFKA for social insurance. Points to the pack's detailed skills: gr-income-tax, gr-corporate-income-tax, gr-cross-border, gr-efka, gr-employee-contributions, gr-vat-return, gr-capital-gains and gr-payroll. Trigger phrases: Greek tax system, taxes in Greece overview, Greece tax rates 2026, how Greece taxes income. Out of scope: any computation, which lives in the sibling skills named above."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gr-tax-overview"
  jurisdiction: "GR"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Greece Tax Overview

Source-cited draft: not reviewed by an accountant, not for filing. Built by Michael Cutajar and the OpenAccountants team.

A map of the main Greek taxes for tax year 2026. It computes nothing; each line points to the skill that holds the detail. Income tax figures are from the Ministry of Finance codification of the Income Tax Code (ΚΦΕ, ν. 4172/2013) with amendments up to ν. 5264/2025. VAT figures are from the AADE codification of the VAT Code (ν. 5144/2024), which replaced ν. 2859/2000.

## Greek tax system at a glance

| Item | 2026 position | Source | Detail |
|---|---|---|---|
| Tax year | Calendar year. A legal person keeping double-entry books may end its tax year on 30 June. No tax year exceeds 12 months | ΚΦΕ art. 8(1), [ΚΦΕ codification](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) | `gr-income-tax`, `gr-corporate-income-tax` |
| Currency | Euro (EUR) | | |
| Tax authority | Independent Authority for Public Revenue (AADE, Ανεξάρτητη Αρχή Δημοσίων Εσόδων) | [AADE](https://www.aade.gr/en) | |
| Basis of taxation | Greek tax residents are taxed on worldwide income; non-residents only on Greek-source income | ΚΦΕ art. 3(1) and (2), same | `gr-cross-border` |
| Personal income tax scale (employment, pension and business income) | 9% to EUR 10,000, 20% to 20,000, 26% to 30,000, 34% to 40,000, 39% to 60,000, 44% above EUR 60,000. Lower rates for parents and for under-30s | ΚΦΕ art. 15(1), as replaced by ν. 5246/2025 art. 3(1), same | `gr-income-tax` |
| Corporate income tax rate | 22% (from tax year 2021) | ΚΦΕ art. 58(1)(a), same | `gr-corporate-income-tax` |
| VAT standard rate | 24%; reduced rates 13%, and 6% or 4% where Annex III provides for them, for goods and services in Annex III | VAT Code (ν. 5144/2024) art. 26(1), [AADE codification circular Ε.2023/2025](https://www.aade.gr/egkyklioi-kai-apofaseis/e-2023-29-04-2025) | `gr-vat-return` |
| Personal income tax return | 15 March to 15 July of the following year, so 15 July 2027 for 2026 income | ΚΦΕ art. 67(3), same | `gr-income-tax` |
| Corporate income tax return | 15 March to 15 July of the following year for a 31 December year end; otherwise by the last working day of the sixth month after the year end | ΚΦΕ art. 68(2), same | `gr-corporate-income-tax` |
| Social insurance | e-EFKA. Employees and employers pay percentage contributions on pay; the self-employed pay fixed monthly amounts by category | [e-EFKA](https://www.efka.gov.gr) | `gr-employee-contributions`, `gr-efka` |

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Code (ν. 4172/2013), Ministry of Finance codification up to ν. 5264/2025: arts. 3, 8, 15, 58, 67, 68 | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-10-23 |
| AADE circular Ε.2023/29-04-2025, administrative codification of the VAT Code (ν. 5144/2024), text up to 31.12.2024: art. 26 | https://www.aade.gr/egkyklioi-kai-apofaseis/e-2023-29-04-2025 | 2026-10-23 |
| AADE home page | https://www.aade.gr/en | 2026-10-23 |
| e-EFKA home page | https://www.efka.gov.gr | 2026-10-23 |

Not yet confirmed: any amendment to the VAT Code rates made after 31 December 2024 (the AADE codification read runs to that date); any amendment to the Income Tax Code during 2026 after ν. 5264/2025.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gr-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gr-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
