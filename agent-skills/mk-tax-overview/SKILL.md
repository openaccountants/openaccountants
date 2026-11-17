---
name: mk-tax-overview
description: "North Macedonia tax routing for calendar year 2026. Use for an initial North Macedonia tax overview, choosing the right income-tax, company-tax, payroll, social-insurance, VAT, transfer-pricing or cross-border skill. Covers individuals, sole traders, resident companies, local permanent establishments, employers and VAT taxpayers. Identifies the primary charging laws, the different annual filing routes and the July 2026 contribution-rate change without substituting a headline rate for the actual category computation. This is a supporting router to the seven computational skills, not an additional computational tax domain. Read the linked skill and its scope and unresolved items before preparing a calculation. Built from the law (tier 2); Not yet approved by a licensed North Macedonia accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mk-tax-overview"
  jurisdiction: "MK"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# North Macedonia tax overview and routing v0.2

## Scope

Calendar year **2026**. Use the [pack README](README.md) to identify the
computational route and remaining core gaps. This supporting overview supplies
no alternative rate engine. North Macedonia's Public Revenue Office (UJP)
administers the linked ordinary taxes. A skill checked against the law is not an
accountant's attestation.

## Ask the client first

- What person/entity and insured status actually earns or pays the income?
- What income category, activity, residence and foreign connection are involved?
- Which year/wage month and filing form does the question concern?
- Is there a loss, reduced-hours month, first-year activity or transfer changing
  the computation, or a departure requiring the README's exit gap to be settled?

## The method, step by step

### Choose the computation

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

### Annual and monthly handover

The individual/business **DLD-DB** and personal **DLD-GDP** procedures are
different. PIT arts. 96–100 require the business balance by 15 March after the
year, while UJP supplies the individual's annual return by 30 April for
confirmation/correction by 31 May. Their payment rules differ. Follow the
[individual skill](north-macedonia-income-tax.md), including first-year advances.
UJP's current forms list confirms the short names: [DLD-DB](https://www.ujp.gov.mk/mk/obrasci/opis/207)
is the self-employment annual tax balance, filed electronically through e-pdd.ujp.gov.mk
and also to the Central Register; [DLD-GDP](https://www.ujp.gov.mk/mk/obrasci/opis/222)
is the annual return UJP prepares for the individual to confirm or correct.

Corporate **DB/DB-VP** follows the annual-account deadline, including the
electronic-filing route, under Profit Tax Law arts. 35 and 39–41. UJP's
[DB form page](https://www.ujp.gov.mk/mk/obrasci/opis/60) allows DB by 15 March where the annual
account went to the Central Register electronically, and 60 days from the opening of
liquidation, bankruptcy or a status change; [DB-VP](https://www.ujp.gov.mk/mk/obrasci/opis/65) is
filed in the annual-account period, including through etax.ujp.gov.mk. Use the
[corporate skill](mk-corporate-income-tax.md) for the applicable form, annual
balance, advances and exceptions. Do not replace all deadlines with a single
end-of-February date.

Contributions remain monthly. The ordinary employee total is 28% in both
2026 periods, but the pension/unemployment split changes with July–December
wage months under Contributions Law art. 25. Other insured classes have different
fund coverage. Read the [social](north-macedonia-social-contributions.md) and
[payroll](north-macedonia-payroll.md) skills before using a bundled percentage.

## Boundary and exception table

| Fact | Route/control |
|---|---|
| Incorporation or foreign bank account | Establish the actual taxpayer, residence, source and treaty facts; neither fact alone decides the tax outcome. |
| Same worker/invoice engages several taxes | Load each relevant skill; VAT, insurance and income tax are separate obligations. |
| Ordinary employee versus proprietor/director | Classify insured group first; the ordinary 28% total is derived for the employee funds, not a universal payment rate. |
| June salary paid in July | Use the wage month and the corresponding fund split; do not switch the June liability merely from bank-payment date. |
| Business loss, reduced hours or first-year activity | Load the specific income/social/payroll rules and their limits; do not import corporate loss relief into PIT. |
| Departure or deemed disposal | README's explicit exit gap remains unresolved; do not assert a nil charge or a completed departure computation. |

## Worked cases

**Ordinary company handoff.** A resident company has a fully reconciled ordinary taxable profit of MKD 2,000,000, with no eligible turnover election, losses, credits or relief assumed. At the [Profit Tax Law art. 2](https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf#page=1) 10% rate, analytical tax is MKD 200,000. Load the corporate skill for the DB reconciliation, advances and annual-account filing route; do not send it to the individual's DLD-DB merely because it has a single owner.

```oa-check
name: MK router resident company ordinary tax handoff
inputs:
  reconciled_taxable_profit: 2000000
steps:
  - ordinary_profit_tax: reconciled_taxable_profit * 0.10
expected:
  ordinary_profit_tax: 200000
```

**Wage-period handoff across July.** An ordinary employee has an agreed contribution base of MKD 50,000 for each of June and July, already checked against the applicable floor/cap and insured status. [UJP's dated table](https://www.ujp.gov.mk/en/vodic/category/641?print=1) and [art. 25](https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf#page=13) give June pension/unemployment 18.8%/1.2%, July 19.9%/0.1%; ordinary health/additional health are 7.5%/0.5%. Both totals are MKD 14,000 (derived 28%), but pension rises MKD 550 and unemployment falls MKD 550. Load payroll plus social contributions and retain both fund splits, even if both wages are paid after July starts. This is not a universal insurance computation for proprietors/directors or special statuses.

```oa-check
name: MK router June versus July employee fund handoff
inputs:
  contribution_base: 50000
steps:
  - june_pension: contribution_base * 0.188
  - june_unemployment: contribution_base * 0.012
  - july_pension: contribution_base * 0.199
  - july_unemployment: contribution_base * 0.001
  - common_health: contribution_base * (0.075 + 0.005)
  - june_total: june_pension + june_unemployment + common_health
  - july_total: july_pension + july_unemployment + common_health
  - pension_change: july_pension - june_pension
  - unemployment_change: july_unemployment - june_unemployment
expected:
  june_pension: 9400
  june_unemployment: 600
  july_pension: 9950
  july_unemployment: 50
  common_health: 4000
  june_total: 14000
  july_total: 14000
  pension_change: 550
  unemployment_change: -550
```

## When to refuse or refer

Refuse a calculation without taxpayer/income/insured classification, the relevant period, source records and the actual election/decision where needed. Route specialist minimum-global-tax, regulated-sector/state-aid and treaty questions to their operative law. The seven category skills retain their stated scope and unresolved items; this router does not override them or supply a universal exemption.

## Filing and payment

Hand over a calendar by taxpayer and form: DLD-DB business balance, DLD-GDP personal reconciliation, company DB/DB-VP, monthly MPIN, VAT and foreign/related-party filings where applicable. Keep original deadlines, payment dates, responsible person, submission evidence and corrections separate. The company annual-account deadline cannot replace the individual's 15 March/30 April/31 May sequence. Obtain the current live portal fields through the relevant filing route rather than inventing them from this overview.

## Completion checklist

- Each taxpayer, income category, year/wage month and foreign connection has a selected skill.
- Company and individual returns, contribution groups and VAT status are not conflated.
- Loss, reduced-hour, first-year and July transition conditions are handed over explicitly.
- The output records both the loaded skills and all unresolved facts/boundaries.

## Sources

| Actual material read | Official URL | Read on |
|---|---|---|
| Read for PIT residence/category/business/salary/annual handover: arts. 4-11, 16-17, 19-30, 55-57, 96-100; visually read PDF pages 2-3, 8-13, 17-18, 30-31 | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-11-15 |
| Read for company/PE charging and ordinary rate arts. 2, 4-6, related-party routing art. 12/12-a, annual-account/turnover filing arts. 35, 39-41; PDF pages 1-2, 5, 12-13 | https://www.ujp.gov.mk/files/attachment/0000/0965/Zakon_za_danok_na_dobivka_199_2023.pdf | 2026-11-15 |
| Read for contribution categories/base and July wage rates arts. 7, 10-16, 25; PDF pages 2-4, 6-10, 13 | https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf | 2026-11-15 |
| Read for dated ordinary fund-rate table, January-June versus July-December 2026, HTML | https://www.ujp.gov.mk/en/vodic/category/641?print=1 | 2026-11-15 |
| Read for VAT subject/taxpayer routing arts. 2, 9 and foreign representative boundary; PDF pages 1, 4 | https://www.ujp.gov.mk/files/attachment/0000/0986/______________________________________.____________267____30.12.2025.pdf | 2026-11-15 |
| Read for UJP forms list entries and form pages DLD-DB (opis 207), DLD-GDP (opis 222), DB (opis 60) and DB-VP (opis 65): short names, who files, portal and deadline text, HTML | https://www.ujp.gov.mk/mk/obrasci/opis/207 | 2026-11-17 |
| Same, DLD-GDP page | https://www.ujp.gov.mk/mk/obrasci/opis/222 | 2026-11-17 |
| Same, DB page | https://www.ujp.gov.mk/mk/obrasci/opis/60 | 2026-11-17 |
| Same, DB-VP page | https://www.ujp.gov.mk/mk/obrasci/opis/65 | 2026-11-17 |

Not yet confirmed: UJP still publishes the PIT consolidation through Gazette 274/2022 and the Profit Tax Law consolidation through Gazette 199/2023 as current (law pages checked 2026-11-17); later Gazette amendments were not separately searched. This router does not resolve the core gaps identified in the README and computational skills. No minimum-global-tax computation or universal exemption is asserted. A licensed professional must review the actual facts, records and statutory treatment before filing or acting.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mk-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mk-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
