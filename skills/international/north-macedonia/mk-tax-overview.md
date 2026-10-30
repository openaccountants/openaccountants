---
name: mk-tax-overview
description: >
  North Macedonia tax routing for calendar year 2026. Use for an initial
  North Macedonia tax overview, choosing the right income-tax, company-tax,
  payroll, social-insurance, VAT, transfer-pricing or cross-border skill. Covers
  individuals, sole traders, resident companies, local permanent establishments,
  employers and VAT taxpayers. Identifies the primary charging laws, the different
  annual filing routes and the July 2026 contribution-rate change without
  substituting a headline rate for the actual category computation. This is a
  supporting router to the seven computational skills, not an additional
  computational tax domain. Read the linked skill and its scope and unresolved
  items before preparing a calculation. Checked against the law (tier 2) and awaiting
  licensed North Macedonia professional review.
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
version: 0.1
---

# North Macedonia tax overview and routing v0.1

## Scope

Calendar year **2026**. Use the [pack README](README.md) to identify the
computational route and remaining core gaps. This supporting overview supplies
no alternative rate engine. North Macedonia's Public Revenue Office (UJP)
administers the linked ordinary taxes. A skill checked against the law is not an
accountant's attestation.

## Choose the computation

| Facts or question | Skill | Primary law |
|---|---|---|
| Individual residence, salary versus independent fees, business income, rent, investment income or gains | [Individual income tax](north-macedonia-income-tax.md) | [PIT arts. 3–11 and category provisions](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf) |
| Resident company or foreign enterprise's local PE, accounting-to-tax reconciliation, losses and reinvestment | [Corporate profit tax](mk-corporate-income-tax.md) | [Profit Tax Law arts. 4–19, 28–41](https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf) |
| Domestic supplies, imports, foreign suppliers, registration and input recovery | [VAT](north-macedonia-vat.md) | [VAT Law](https://www.ujp.gov.mk/files/attachment/0000/0986/______________________________________.____________267____30.12.2025.pdf) |
| Employee, self-employed person, uninsured director or foreign-insurance question | [Mandatory social contributions](north-macedonia-social-contributions.md) | [Contributions Law arts. 7–18, 24–25](https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf) |
| Salary withholding, benefits, fees and gross-to-net | [Payroll](north-macedonia-payroll.md) | [PIT arts. 14–17, 80–85, 92](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf) |
| Related parties, pricing and documentation | [Transfer pricing](north-macedonia-transfer-pricing.md) | [Profit Tax Law arts. 12–15, 39](https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf) |
| Foreign payments/income, PE, residence evidence, treaty relief or departure | [Cross-border tax](north-macedonia-cross-border.md) | [PIT arts. 5–8](https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf); [Profit Tax Law arts. 20–27, 37](https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf) |

Residents' worldwide-income rules and nonresidents' local income/PE rules are
not interchangeable. Neither incorporation nor a foreign bank account determines
the treaty outcome. Separate VAT, insurance and income-tax obligations even when
they concern the same invoice or worker.

## Annual and monthly handover

The individual/business **DLD-DB** and personal **DLD-GDP** procedures are
different. PIT arts. 96–100 require the business balance by 15 March after the
year, while UJP supplies the individual's annual return by 30 April for
confirmation/correction by 31 May. Their payment rules differ. Follow the
[individual skill](north-macedonia-income-tax.md), including first-year advances.

Corporate **DB/DB-VP** follows the annual-account deadline, including the
electronic-filing route, under Profit Tax Law arts. 35 and 39–41. Use the
[corporate skill](mk-corporate-income-tax.md) for the applicable form, annual
balance, advances and exceptions. Do not replace all deadlines with a single
end-of-February date.

Contributions remain monthly. The ordinary employee total is 28% in both
2026 periods, but the pension/unemployment split changes with July–December
wage months under Contributions Law art. 25. Other insured classes have different
fund coverage. Read the [social](north-macedonia-social-contributions.md) and
[payroll](north-macedonia-payroll.md) skills before using a bundled percentage.

## Ask before routing

- What person/entity and insured status actually earns or pays the income?
- What income category, activity, residence and foreign connection are involved?
- Which year/wage month and filing form does the question concern?
- Is there a loss, reduced-hours month, first-year activity or transfer changing
  the computation, or a departure requiring the README's exit gap to be settled?

## Sources

| Official source | URL | Read on |
|---|---|---|
| PIT Law, cited articles and category/annual procedures | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Profit Tax Law, cited articles | https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Contributions Law through Gazette 148/2026 | https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf | 2026-10-24 |
| VAT Law through Gazette 267/2025 | https://www.ujp.gov.mk/files/attachment/0000/0986/______________________________________.____________267____30.12.2025.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |

Not yet confirmed: this router does not resolve the core gaps identified in the
README and computational skills. No minimum-global-tax computation or universal
exemption is asserted. A licensed professional must review the actual facts,
records and statutory treatment before filing or acting.

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
