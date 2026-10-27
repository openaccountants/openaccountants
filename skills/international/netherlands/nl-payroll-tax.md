---
name: nl-payroll-tax
description: "Dutch work-cost scheme (werkkostenregeling, WKR) and employer final levies for tax year 2026: whether a benefit is wage, the targeted exemptions and nil valuations, designating final-levy wage, the customary test (30% and EUR 2,400 per person), the free space of 2.00% up to EUR 400,000 and 1.18% above, the 80% final levy, the group (concern) election, settlement in the second return period of 2027, gifts to non-employees (45% / 75%), the van final levy and grossed-up final levy on assessments. Trigger phrases: werkkostenregeling, WKR, vrije ruimte, eindheffing, eindheffingsloon, gerichte vrijstelling, nihilwaardering, concernregeling, gebruikelijkheidstoets, kerstpakket, onbelaste vergoeding, reiskostenvergoeding, thuiswerkvergoeding. Out of scope: running payroll, tables, credits, premiums, the return calendar and penalties (netherlands-payroll); company car (nl-company-car); expat scheme (netherlands-30-percent-ruling); premiums in depth (nl-social-contributions); cross-border (nl-cross-border)."
version: 1.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: work-cost scheme (WKR) and final levies 2026

## Who this applies to

Every Dutch withholding agent (inhoudingsplichtige) that gives employees allowances, benefits in kind or facilities on top of cash wage. The work-cost scheme decides whether each item is taxed with the employee, is exempt, or is designated as final-levy wage that the employer bears. It also covers the other final levies an employer pays in its own name: gifts to business contacts and non-employees, a van used in turn by several employees, and grossed-up final levy on an assessment.

Use the Handboek Loonheffingen 2026 (March 2026), chapter 10, paragraph 4.2 and chapters 22 to 25, with the rates appendix, edition 4 of 25 June 2026. Edition 4 raised the tax-free mileage allowance to EUR 0.25 from 1 January 2026.

Running payroll itself (tables, credits, employee and employer premiums, return calendar, corrections, penalties, customary wage of a director, minimum wage and holiday pay) is in netherlands-payroll; this skill does not repeat it. Company car private use: nl-company-car. The 30% expat allowance (a targeted exemption): netherlands-30-percent-ruling. Annual income tax of the employee: nl-income-tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Free space (vrije ruimte), first band | 2.00% of total fiscal wage up to and including EUR 400,000 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 13) |
| Free space, above EUR 400,000 | 1.18% of the excess | 2026 | same; https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 31a(3)) |
| WKR final levy on designated wage above the free space | 80% | 2026 | same (art. 31a(1)) |
| Customary test: designation may not deviate more than | 30% from what is customary | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (para. 4.2) |
| Accepted as customary in any case | EUR 2,400 per person per year in total | 2026 | same |
| Former-employment wage excluded from the free-space base if above | 10% of total fiscal wage | 2026 | same (para. 10.1.4) |
| Group (concern) election: ownership link | at least 95% | 2026 | same (para. 10.2) |
| Mileage allowance, targeted exemption | EUR 0.25 per km (from 1 January 2026) | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte |
| Home-working allowance, targeted exemption | EUR 2.45 per day | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 13) |
| Relocation, targeted exemption | moving of household effects plus EUR 7,750 | 2026 | same |
| Discount on own products, targeted exemption | at most 20% per product and EUR 500 a year | 2026 | same; https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (para. 22.1.8) |
| Meal value (no more than incidental business character) | EUR 4.05 per breakfast, lunch or dinner | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 12) |
| Housing and lodging value | EUR 7.00 per day | 2026 | same |
| Final levy on gifts to non-employees | 45% if value is at most EUR 136; 75% of the full value above | 2026 | same; https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (para. 25.4) |
| Final levy, van used in turn by several employees | EUR 451 per van per year | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 12) |
| Grossed-up final levy (tabeltarief), resident, under AOW age, credits not applied | 55.60% up to EUR 38,883; 60.10% to EUR 78,426; 98.00% above | 2026 | same (table 5.1) |
| Final levy on severance above EUR 700,000 / on early-retirement (RVU) payments | 75% / 57.70% | 2026 | same (table 12) |

## The taxable base

Work through each allowance, benefit or facility in six steps (handbook para. 10.1).

1. **Is it wage?** Items given because of the employment are wage. Costs the employee pays on the employer's behalf and that are reimbursed (intermediary costs) are not. Keep the evidence for that line.
2. **Targeted exemption or nil valuation?** Targeted exemptions (gerichte vrijstellingen, art. 31a(2)) include business travel and commuting at EUR 0.25 a km, home working at EUR 2.45 a day, temporary stays for work, courses and study, relocation, necessary tools, computers and phones, own-product discounts, health and safety items and the expat allowance. A targeted exemption still has to be designated as final-levy wage, but the Belastingdienst presumes this where the amount does not exceed the norm. Nil valuations apply to items in kind on the workplace (for example workplace facilities that meet the conditions). If an item could fall under both, treat it as a nil valuation (para. 4.12.5). Neither uses the free space.
3. **Designate or tax with the employee.** For the rest, the employer chooses per item and per employee, no later than the moment it pays or provides it. The choice is final; only a genuine administrative error may be corrected. If an item is in neither box at an audit, the Belastingdienst treats it as employee wage for a past year and as final-levy wage for the current year if customary (para. 10.1.3).
4. **Always employee wage, never final-levy wage:** a company car for private use, a company home (except housing away from home for the work), fines, items not designated in time, the part failing the customary test, former-employment wage (with three exceptions) and the interest benefit on a staff mortgage loan (art. 31(5)). Items to former employees that current employees also get (a Christmas package, own-product discounts) are always final-levy wage.
5. **Customary test.** Designated items may not deviate more than 30% from what is customary for comparable employees. A total of EUR 2,400 per person per year is accepted as customary, but not where pay is below the statutory minimum wage or for interns. The part above the 30% limit is the employee's wage. The Belastingdienst carries the burden of showing a designation is not customary.
6. **Free space and levy.** Free space is 2.00% of the employer's total fiscal wage (column 14 of the wage ledger) up to EUR 400,000 and 1.18% above. Leave out fees of artists and professional athletes. If former-employment wage is more than 10% of the total, leave it out of the base. A new employer does not annualise. Compare designated wage (excluding targeted exemptions and nil valuations) with the free space. The excess bears 80% final levy. Unused space does not carry over.
7. **Group election.** Employers linked by at least a 95% interest may pool their fiscal wage and designated items. The free space is computed once on the combined wage (no separate first band per entity), and the group member with the highest fiscal wage pays the levy. The choice is made each year, at the latest with the second-period return of the next year.
8. **Items in kind** are valued at market value (own products: the price to a third party, or market value). A total of employee contributions for the same item may be netted against the total value, but not below nil.
9. **Mileage top-up.** EUR 0.25 applies from 1 January 2026 (Secretary of State decision of 17 May 2026). How to correct earlier 2026 payments at EUR 0.23 is in netherlands-payroll.

## Deadlines and filing

- **Designation:** at the latest when the item is paid or provided. No notice to the Belastingdienst is needed; the payroll records show it.
- **WKR final levy for 2026:** report and pay with the return for the second period of 2027 (February 2027 for monthly filers). An employer may settle earlier, or pay on account during the year and square up by that same return. If withholding ends during the year, settle in the return for the period in which it ends. No levy is reported if designated wage stays within the free space.
- **Group election for 2026:** decide by the return for the second period of 2027.
- **Gifts to non-employees:** report the final levy in the return for the period in which the recipient receives the gift. Tell the recipient that final levy is applied (general terms may do this) and record who received it.
- **Return dates, corrections and payment rules** for the loonaangifte: netherlands-payroll.

## Penalties and interest

- **Late or missing payment of WKR final levy** is a payment default on the loonaangifte; the late-filing and late-payment penalties in netherlands-payroll apply.
- **Assessment (naheffingsaanslag).** Wage on which tax was not paid becomes a final-levy element (art. 31(1)(a)). The levy then runs at the grossed-up table rate (tabeltarief), because the employer is treated as having borne the tax at once (art. 31(3)). For a resident under AOW age without credits, that rate is 55.60% in band 1, 60.10% in band 2 and 98.00% above EUR 78,426. The employer may ask, with the data needed, to assess the employee's wage normally instead.
- **Designation rules.** An item above the 30% customary limit, or not designated in time, is employee wage. If it was not withheld, it is assessed as above.

## Cross-border points

- The free space is computed on the Dutch fiscal wage in the wage ledger. Wage for which the Netherlands has no taxing right and which is not in column 14 does not count. Check the ledger rather than adding foreign payroll.
- **Expat allowance (30% ruling):** a targeted exemption under art. 31a. From 1 January 2026 the transitional rule ended and the allowance is capped at 30% of the WNT norm (EUR 262,000), and some costs of incoming employees (higher cost of living abroad, private calls home) can no longer be reimbursed tax-free. Detail: netherlands-30-percent-ruling.
- **Gifts to foreign business contacts** can use the 45% / 75% final levy if given at the same time and occasion to the employer's own employees.
- Insurance and tax allocation for employees working abroad: nl-cross-border.

## Worked examples

**Example 1. One employer, free space exceeded.** An employer's 2026 fiscal wage in column 14 is EUR 1,250,000. Former-employment wage is EUR 60,000, under 10% of the total, so it stays in the base. It designated EUR 30,000 of customary benefits as final-levy wage (gifts, a staff party, a gym subscription), separate from tax-free mileage and home-working allowances. Free space is 2% of the first 400,000 plus 1.18% of the rest. The 80% levy on the excess is paid with the February 2027 return.

```oa-check
name: WKR final levy, single employer, fiscal wage EUR 1,250,000 (2026)
inputs:
  wage: 1250000
  designated: 30000
steps:
  - space: min(wage, 400000) * 0.02 + max(wage - 400000, 0) * 0.0118
  - excess: max(designated - space, 0)
  - levy: excess * 0.8
expected:
  space: 18030
  excess: 11970
  levy: 9576
```

**Example 2. Group election.** Company A (fiscal wage EUR 300,000, designated EUR 9,000) and company B (fiscal wage EUR 500,000, designated EUR 6,000) are linked by a 100% shareholding. Separately, A has free space of EUR 6,000 and pays 80% on EUR 3,000; B has free space of EUR 9,180 and pays nothing. Pooled, the free space is computed once on EUR 800,000, so only one first band applies. B, with the higher fiscal wage, pays the group levy. Here the group election saves EUR 576.

```oa-check
name: WKR group election versus separate calculation (2026)
inputs:
  wage_a: 300000
  wage_b: 500000
  des_a: 9000
  des_b: 6000
steps:
  - space_a: min(wage_a, 400000) * 0.02 + max(wage_a - 400000, 0) * 0.0118
  - space_b: min(wage_b, 400000) * 0.02 + max(wage_b - 400000, 0) * 0.0118
  - separate_levy: max(des_a - space_a, 0) * 0.8 + max(des_b - space_b, 0) * 0.8
  - wage_group: wage_a + wage_b
  - space_group: min(wage_group, 400000) * 0.02 + max(wage_group - 400000, 0) * 0.0118
  - group_levy: max(des_a + des_b - space_group, 0) * 0.8
  - saving: separate_levy - group_levy
expected:
  space_a: 6000
  space_b: 9180
  separate_levy: 2400
  space_group: 12720
  group_levy: 1824
  saving: 576
```

## Ask the client first

1. Total 2026 fiscal wage per withholding agent (column 14), and how much of it is former-employment wage or artists' and athletes' fees.
2. A list of every allowance, gift, facility and reimbursement in 2026: what, to whom, value including VAT, any employee contribution, and how it was booked (employee wage, final-levy wage, targeted exemption).
3. Is any entity linked to others by a 95% or more interest, and do they want the group election?
4. Does anyone receive designated items above EUR 2,400 in the year, or earn at or near the minimum wage?
5. Gifts to business contacts, agency workers or freelancers, and were the recipients told final levy applies?
6. Any van used in turn by several employees, and any past items not booked at all?
7. Return period (month or four weeks), so we know which 2027 return carries the settlement.

## Sources

| Source | URL | Read on |
|---|---|---|
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), para. 4.2, 4.12.5, ch. 10, 22, 25.4 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-27 |
| Belastingdienst, rates appendix loonheffingen 2026, edition 4 (25 June 2026), tables 5.1, 12, 13 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-10-27 |
| Wet op de loonbelasting 1964, art. 31 and 31a | https://wetten.overheid.nl/BWBR0002471/2026-01-01 | 2026-10-27 |
| Belastingdienst, mileage allowance EUR 0.25 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte | 2026-10-27 |
| Tweede Kamer, Belastingplan 2027, explanatory memorandum (kst. 37022 nr. 3) | https://zoek.officielebekendmakingen.nl/kst-37022-3.html | 2026-10-27 |

Not yet confirmed: the Belastingplan 2027 proposes abolishing the own-products exemption from 2027 (a bill, not law; do not apply to 2026). The old version's general payroll topics now live in netherlands-payroll. These old points were not re-read today and stay out until checked: maternity and partner leave with UWV benefit, working-time limits, sickness pay in the second year, the full payslip content list, the ten-employee limit for filing in Mijn Belastingdienst Zakelijk, the high Aof rate on UWV benefits paid through the employer, and the detailed conditions of the tools, training, workplace and bicycle exemptions (handbook ch. 22 to 23).

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
