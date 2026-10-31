---
name: nl-payroll-tax
description: "Dutch payroll (loonheffingen) and the work-cost scheme (werkkostenregeling, WKR) for tax year 2026. Running payroll: wage tax and national insurance withheld under the Wet LB 1964, white and green tables, special-remuneration tables, the 2026 combined bands (35.75%, 37.56%, 49.50%) and the AOW-age bands, the payroll tax credits applied by one employer, the 52% anonymous rate, employer premiums (AWf, Aof, Wko, Whk, Ufo) and the Zvw levy on the EUR 79,409 cap, the director's customary wage of EUR 58,000, minimum wage, holiday pay and the transition payment, the monthly and four-weekly loonaangifte calendar, corrections, the EUR 83 and 3% penalties, payslips and the annual statement. WKR and employer final levies: whether a benefit is wage, the targeted exemptions and nil valuations, designating final-levy wage, the customary test (30% and EUR 2,400 per person), the free space of 2.00% up to EUR 400,000 and 1.18% above, the 80% final levy, the group (concern) election, settlement in the second return period of 2027, gifts to non-employees (45% / 75%), the van final levy and grossed-up final levy on assessments. Trigger phrases: loonheffing, loonaangifte, Dutch payroll, loonstrook, witte tabel, groene tabel, bijzondere beloningen, anoniementarief, minimumloon, vakantiegeld, nulaangifte, betaalverzuimboete, werkkostenregeling, WKR, vrije ruimte, eindheffing, eindheffingsloon, gerichte vrijstelling, nihilwaardering, concernregeling, gebruikelijkheidstoets, kerstpakket, onbelaste vergoeding, reiskostenvergoeding, thuiswerkvergoeding. Out of scope: company car (nl-company-car); expat scheme (netherlands-30-percent-ruling); premiums in depth and the self-employed (nl-social-contributions); cross-border (nl-cross-border)."
version: 1.2
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
  - payroll-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: payroll (loonheffingen), work-cost scheme (WKR) and final levies 2026

## Who this applies to

Every employer who pays wages to an employee and is a withholding agent (inhoudingsplichtige) under the Wet op de loonbelasting 1964 (Wet LB). That covers Dutch companies and foreign employers with a Dutch permanent establishment or that register voluntarily. The employer withholds wage tax and national insurance together, pays employer premiums for the employee insurances and the Zvw, files one loonaangifte per period, and pays it.

The same withholding agent, when it gives employees allowances, benefits in kind or facilities on top of cash wage, applies the work-cost scheme. The scheme decides whether each item is taxed with the employee, is exempt, or is designated as final-levy wage that the employer bears. This skill also covers the other final levies an employer pays in its own name: gifts to business contacts and non-employees, a van used in turn by several employees, and grossed-up final levy on an assessment.

Use the Handboek Loonheffingen 2026 (version March 2026), in particular chapters 6, 7, 9, 10, 13 and 14, paragraph 4.2 and chapters 22 to 25, with the rates appendix, edition 4 of 25 June 2026. Edition 4 raised the tax-free mileage allowance to EUR 0.25 from 1 January 2026 and corrects two figures from earlier editions: the general credit base runs "up to and including" EUR 29,736, and the employment credit ends at EUR 132,920 (not EUR 132,290). For a 2025 correction, use the 2025 tables.

Out of this skill: private use of a company car, see nl-company-car; the expat scheme (a targeted exemption), see netherlands-30-percent-ruling; premium rules in depth and the self-employed, see nl-social-contributions; who is insured where and treaty allocation, see nl-cross-border. Annual income tax of the employee: nl-income-tax.

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
| Mileage allowance, targeted exemption | EUR 0.25 per km (from 1 January 2026, approved ahead of the Tax Plan 2027) | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte |
| Home-working allowance, targeted exemption | EUR 2.45 per day | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 13) |
| Relocation, targeted exemption | moving of household effects plus EUR 7,750 | 2026 | same |
| Discount on own products, targeted exemption | at most 20% per product and EUR 500 a year | 2026 | same; https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (para. 22.1.8) |
| Meal value (no more than incidental business character) | EUR 4.05 per breakfast, lunch or dinner | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 12) |
| Housing and lodging value | EUR 7.00 per day | 2026 | same |
| Final levy on gifts to non-employees | 45% if value is at most EUR 136; 75% of the full value above | 2026 | same; https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (para. 25.4) |
| Final levy, van used in turn by several employees | EUR 451 per van per year | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf (table 12) |
| Grossed-up final levy (tabeltarief), resident, under AOW age, credits not applied | 55.60% up to EUR 38,883; 60.10% to EUR 78,426; 98.00% above | 2026 | same (table 5.1) |
| Final levy on severance above EUR 700,000 / on early-retirement (RVU) payments | 75% / 57.70% | 2026 | same (table 12) |
| Band 1, under AOW age: wage tax 8.10% + AOW 17.90% + Anw 0.10% + Wlz 9.65% | 35.75% up to EUR 38,883 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Band 2 | 37.56% from EUR 38,883 to EUR 78,426 | 2026 | same |
| Band 3 | 49.50% above EUR 78,426 | 2026 | same |
| Band 1, AOW age, born 1946 or later (no AOW premium) | 17.85% up to EUR 38,883 | 2026 | same |
| Band 1, born 1945 or earlier | 17.85% up to EUR 41,123 | 2026 | same |
| General credit (algemene heffingskorting), under AOW age | EUR 3,115; reduces 6.398% above EUR 29,736; nil at EUR 78,426 | 2026 | same |
| General credit, AOW age | EUR 1,556; reduces 3.195% | 2026 | same |
| Employment credit (arbeidskorting), under AOW age | max EUR 5,685 (reached at EUR 45,592); reduces 6.510% above EUR 45,592; nil at EUR 132,920 | 2026 | same |
| Employment credit, AOW age | max EUR 2,840; reduces 3.250% | 2026 | same |
| Elderly credit (ouderenkorting) | EUR 2,067; reduces above EUR 46,002; nil at EUR 59,782 | 2026 | same |
| Anonymous rate (no name, address or BSN given) | 52%, no credits | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 26b) |
| AWf (unemployment fund), low / high | 2.74% / 7.74% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Aof (disability fund), small employer / medium and large | 6.27% / 7.63% | 2026 | same |
| Wko surcharge (childcare) | 0.50% | 2026 | same |
| Whk (return-to-work fund) | rate on the employer's own notice | 2026 | same (sector table 10) |
| Ufo (government employers only) | 0.68% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf |
| Employer Zvw levy / withheld Zvw contribution | 6.10% / 4.85% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Maximum premium and contribution wage | EUR 79,409 a year; EUR 6,617.41 a month; EUR 6,108.38 per four weeks | 2026 | same (table 11) |
| Small employer (2024 premium wage sum) | up to and including EUR 1,082,500; medium up to EUR 4,330,000 | 2026 | same (table 9) |
| Customary wage, substantial-interest director | at least EUR 58,000 | 2026 | same (table 12) |
| Expat scheme salary norm / under-30 master's / cap | more than EUR 48,013 / more than EUR 36,497 / WNT cap EUR 262,000 | 2026 | same (tables 12, 13) |
| Minimum wage, age 21 and over | EUR 14.71 an hour from 1 Jan; EUR 14.99 from 1 Jul | 2026 | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 |
| Holiday allowance (vakantiebijslag) | at least 8% of gross annual wage | 2026 | https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld |
| Transition payment cap | EUR 102,000, or one gross annual salary if higher | 2026 | https://www.rijksoverheid.nl/vraag-en-antwoord/ontslag/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen |

## The taxable base

**Part A: allowances, benefits and facilities (WKR).** Work through each allowance, benefit or facility in six steps (handbook para. 10.1).

1. **Is it wage?** Items given because of the employment are wage. Costs the employee pays on the employer's behalf and that are reimbursed (intermediary costs) are not. Keep the evidence for that line.
2. **Targeted exemption or nil valuation?** Targeted exemptions (gerichte vrijstellingen, art. 31a(2)) include business travel and commuting at EUR 0.25 a km, home working at EUR 2.45 a day, temporary stays for work, courses and study, relocation, necessary tools, computers and phones, own-product discounts, health and safety items and the expat allowance. A targeted exemption still has to be designated as final-levy wage, but the Belastingdienst presumes this where the amount does not exceed the norm. Nil valuations apply to items in kind on the workplace (for example workplace facilities that meet the conditions). If an item could fall under both, treat it as a nil valuation (para. 4.12.5). Neither uses the free space.
3. **Designate or tax with the employee.** For the rest, the employer chooses per item and per employee, no later than the moment it pays or provides it. The choice is final; only a genuine administrative error may be corrected. If an item is in neither box at an audit, the Belastingdienst treats it as employee wage for a past year and as final-levy wage for the current year if customary (para. 10.1.3).
4. **Always employee wage, never final-levy wage:** a company car for private use, a company home (except housing away from home for the work), fines, items not designated in time, the part failing the customary test, former-employment wage (with three exceptions) and the interest benefit on a staff mortgage loan (art. 31(5)). Items to former employees that current employees also get (a Christmas package, own-product discounts) are always final-levy wage.
5. **Customary test.** Designated items may not deviate more than 30% from what is customary for comparable employees. A total of EUR 2,400 per person per year is accepted as customary, but not where pay is below the statutory minimum wage or for interns. The part above the 30% limit is the employee's wage. The Belastingdienst carries the burden of showing a designation is not customary.
6. **Free space and levy.** Free space is 2.00% of the employer's total fiscal wage (column 14 of the wage ledger) up to EUR 400,000 and 1.18% above. Leave out fees of artists and professional athletes. If former-employment wage is more than 10% of the total, leave it out of the base. A new employer does not annualise. Compare designated wage (excluding targeted exemptions and nil valuations) with the free space. The excess bears 80% final levy. Unused space does not carry over.
7. **Group election.** Employers linked by at least a 95% interest may pool their fiscal wage and designated items. The free space is computed once on the combined wage (no separate first band per entity), and the group member with the highest fiscal wage pays the levy. The choice is made each year, at the latest with the second-period return of the next year.
8. **Items in kind** are valued at market value (own products: the price to a third party, or market value). A total of employee contributions for the same item may be netted against the total value, but not below nil.
9. **Mileage top-up.** EUR 0.25 applies from 1 January 2026 (policy decision of the State Secretary for Finance, announced by the Belastingdienst on 25 June 2026). If you paid EUR 0.23 or less, you may pay the EUR 0.02 difference tax-free with a later wage. If you taxed the excess over EUR 0.23 as wage, correct the earlier returns. If you paid 80% final levy on it, offset that levy in a later return.

**Part B: running the payroll (wage tax, national insurance, premiums).**

10. **Wage.** Everything the employee gets from the employment: cash, benefits in kind, allowances. Employer Zvw levy is an employer cost; it is not wage and is not deducted from net pay. The wage-tax base, the premium base (employee insurances) and the Zvw base usually match but are recorded separately. Pension contributions follow the actual scheme; there is no standard percentage.
11. **Which table.** White tables for current employment. Green tables for income from former employment (pensions, many benefits). A one-off payment for current work stays white. Choose the period (day, week, four weeks, month, quarter), the age column (under or over AOW age), and whether the employee asked for the payroll tax credits. An employee asks for the credits with one employer or payer at a time.
12. **Special remuneration.** Bonuses, a once-a-year holiday allowance and similar payments use the special-remuneration table (white or green). The rate depends on the employee's annual wage, normally the previous year's wage; for a new starter, estimate the full current year. Holiday pay paid monthly joins the monthly wage.
13. **Do not shortcut the tables.** The bands and credits above are annual. The withholding for a period comes from the official period table or the software that implements it. A net-pay agreement needs a gross-up in the software. The annual figures are for checks and the employee's own return.
14. **Anonymous rate.** If the employee does not give name, address, place of residence or BSN, withhold 52% with no credits (Wet LB art. 26b). If the BSN is missing for reasons outside both parties' control (for example a municipal delay), the handbook allows normal withholding; record the reason.
15. **Employer premiums.** AWf low applies to a written indefinite contract that is not on-call, to young workers under 21 with at most 48 paid hours in four weeks (52 in a month), and to BBL trainees. Otherwise AWf high. Revise to high if the contract ends within two months of starting, or if paid hours exceed contracted hours by more than 30% in the year (this test does not apply where contracted hours average more than 30 a week). Aof low for small employers; size uses the 2024 premium wage sum. Even a small employer always pays the high Aof (7.63%) on UWV benefits it passes on to the employee (WW, ZW, WAO/WIA, paid through a werkgeversbetaling or as own-risk bearer), on WAZO benefits (such as pregnancy and maternity benefit), on Toeslagenwet supplements, and on old-scheme wachtgeld. Report these in the Aof uitkering boxes (Handboek §7.5). Whk is on the employer's notice. Premiums and the Zvw run on the capped base with cumulative period calculation (VCR, Handboek ch. 6). At each wage payment: (1) take the cumulative wage from 1 January; (2) take the cumulative maximum for all pay periods so far (EUR 6,617.41 a month, EUR 6,108.38 per four weeks, EUR 79,409 for the year); (3) take the lower of the two; (4) subtract the cumulative base already charged at earlier payments; (5) charge premiums on the difference; (6) round to 2 decimals. A period with no wage adds no room. So when wages vary month to month, unused room from a low month is used later in the year, and the annual cap is not a fresh allowance every month. The employer may recover up to half of the WGA part of Whk from net pay, never the ZW part.
16. **Director-shareholder.** A working shareholder with a substantial interest takes a customary wage: the highest of the most comparable employment, the highest-paid other employee, and EUR 58,000 (Wet LB art. 12a). If the customary wage for all work is EUR 5,000 or less, no fictitious wage is added. Insurance and Zvw status are determined separately.
17. **Employment-law inputs.** Pay at least the hourly minimum wage for the age band (youth rates for ages 15 to 20). Holiday allowance at least 8%; a CAO may remove it only if the wage is at least 108% of minimum wage. The transition payment is one third of a monthly salary per full year of service plus a pro rata part, capped as in the table.
18. **Sickness pay and statutory leave.** A sick employee keeps 70% of wage for 104 weeks, and for the first 52 weeks at least the statutory minimum wage; the wage counted is capped at the daily maximum premium wage (BW Book 7 art. 629(1)). Statutory leave is at least four times the agreed weekly working time per year (art. 634(1)). That statutory minimum expires six months after the end of the year in which it was earned, unless the employee could not reasonably take it (art. 640a).

## Deadlines and filing

- **Registration.** Register as employer before the first wage payment; the Belastingdienst assigns a loonheffingennummer and the return period (month or four weeks).
- **Return and payment** are due on the same day. Monthly 2026: one month after the period, for example September due 31 October 2026, December due 31 January 2027. Four-weekly: period 10 (7 September to 4 October) due 4 November 2026; period 13 due 31 January 2027. Use the official calendar. Payment must be received by the due date.
- **Nil returns.** A nihilaangifte when there were no employees in the period; a nulaangifte when there were employees but no wage was paid (for example an unpaid director). Keep filing until the Belastingdienst confirms deregistration.
- **Filing route.** Payroll software or an intermediary, or Mijn Belastingdienst Zakelijk for a small payroll. A rejected message is not a filed return.
- **Corrections.** Before the deadline, send the complete return again. After the deadline, correct in a later return; prior-year and specific cases use a separate correction. If you find the error yourself and a separate correction is needed, send it within 8 weeks of discovery.
- **Objection.** Disagreeing with the law as applied (not an error) is by objection within 6 weeks after payment.
- **Employee documents.** A payslip at the first payment and whenever it changes. An annual statement (jaaropgaaf) after the year end, reconciled to the final returns.
- **Designation:** at the latest when the item is paid or provided. No notice to the Belastingdienst is needed; the payroll records show it.
- **WKR final levy for 2026:** report and pay with the return for the second period of 2027 (February 2027 for monthly filers). An employer may settle earlier, or pay on account during the year and square up by that same return. If withholding ends during the year, settle in the return for the period in which it ends. No levy is reported if designated wage stays within the free space.
- **Group election for 2026:** decide by the return for the second period of 2027.
- **Gifts to non-employees:** the 45% / 75% final levy is available for gifts to business contacts given at the same time and for the same occasion to your own employees, and for gifts to agency workers and freelancers (para. 25.4). Report the final levy in the return for the period in which the recipient receives the gift. Tell the recipient that final levy is applied (general terms may do this) and record who received it.

## Penalties and interest

- **Late filing.** Grace period of 7 calendar days after the due date. Later or not at all: EUR 83. An incorrect or incomplete return can also attract EUR 83. Repeated or exceptional cases: up to EUR 6,709.
- **Late payment.** Grace period of 7 calendar days. Within it, no penalty if the previous return was paid on time and in full; otherwise 3%, minimum EUR 50, maximum EUR 6,709. After it: 3% of the late amount, minimum EUR 50, maximum EUR 6,709. Unpaid amounts found later are assessed (naheffingsaanslag) with the same 3% penalty.
- **Corrections** that lead to extra payment normally count as late payment too.
- **Late or missing payment of WKR final levy** is a payment default on the loonaangifte; the late-filing and late-payment penalties above apply.
- **Interest.** On a negative correction, if the refund takes longer than 8 weeks, interest runs from 8 weeks after the correction is received.
- **Director liability.** Directors can be personally liable for unpaid wage tax; report an inability to pay promptly (Invorderingswet 1990).
- **Assessment (naheffingsaanslag).** Wage on which tax was not paid becomes a final-levy element (art. 31(1)(a)). The levy then runs at the grossed-up table rate (tabeltarief), because the employer is treated as having borne the tax at once (art. 31(3)). For a resident under AOW age without credits, that rate is 55.60% in band 1, 60.10% in band 2 and 98.00% above EUR 78,426. The employer may ask, with the data needed, to assess the employee's wage normally instead.
- **Designation rules.** An item above the 30% customary limit, or not designated in time, is employee wage. If it was not withheld, it is assessed as above.

## Cross-border points

- **Withholding versus insurance.** Decide separately whether Dutch wage tax applies (domestic law and the treaty) and whether the employee is insured for Dutch social security (EU Regulation 883/2004 or a bilateral agreement; an A1 or certificate of coverage). A worker can owe Dutch wage tax and be insured abroad, or the other way round. Use the table column that matches the tax and insurance position.
- **Foreign employers** without a permanent establishment can register voluntarily to run Dutch payroll.
- The free space is computed on the Dutch fiscal wage in the wage ledger. Wage for which the Netherlands has no taxing right and which is not in column 14 does not count. Check the ledger rather than adding foreign payroll.
- **Expat allowance (30% ruling):** a targeted exemption under art. 31a. Up to 30% tax-free in 2026 if the Belastingdienst has decided and the salary norm is met. From 1 January 2026 the transitional rule ended and the allowance is capped at 30% of the WNT norm (EUR 262,000), and some costs of incoming employees (higher cost of living abroad, private calls home) can no longer be reimbursed tax-free. Detail and the fall to 27% from 2027: netherlands-30-percent-ruling.
- **Gifts to foreign business contacts** can use the 45% / 75% final levy if given at the same time and occasion to the employer's own employees.
- Residence, treaties, the 183-day test, and insurance and tax allocation for employees working abroad: nl-cross-border.

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

**Example 3. Annual check of wage tax for a full-year employee.** An employee under AOW age earns EUR 48,000 in 2026 from one employer, asked for the credits there, and has no other income. Band 1 is 38,883 at 35.75%; band 2 is the remaining 9,117 at 37.56%. The general credit falls by 6.398% of the wage above 29,736. The employment credit falls by 6.510% of the wage above 45,592. Over the year the period tables should withhold close to this total; small differences come from period rounding.

```oa-check
name: Employee EUR 48,000, under AOW age, credits with this employer (2026)
inputs:
  wage: 48000
steps:
  - band1: min(wage, 38883) * 0.3575
  - band2: max(min(wage, 78426) - 38883, 0) * 0.3756
  - band3: max(wage - 78426, 0) * 0.495
  - gross: band1 + band2 + band3
  - ahk: max(3115 - max(wage - 29736, 0) * 0.06398, 0)
  - ak: max(5685 - max(wage - 45592, 0) * 0.0651, 0)
  - withheld: max(gross - ahk - ak, 0)
expected:
  gross: 17325.02
  ahk: 1946.47
  ak: 5528.24
  withheld: 9850.31
```

**Example 4. Employer premiums on a wage above the monthly cap.** A small employer pays EUR 7,000 a month, every month, on a written indefinite contract (AWf low). The employer's Whk notice says 1.5% (an assumed figure for the example). The premium base is capped at EUR 6,617.41 a month. Because every month is over the cap, cumulative calculation gives the same base each month. Zvw uses the same cap.

```oa-check
name: Small employer, EUR 7,000 monthly wage, capped premiums (2026)
inputs:
  wage: 7000
  cap: 6617.41
  whk: 1.5
steps:
  - base: min(wage, cap)
  - awf: base * 0.0274
  - aof: base * 0.0627
  - wko: base * 0.005
  - whk_amt: base * whk / 100
  - zvw: base * 0.061
  - total: awf + aof + wko + whk_amt + zvw
expected:
  base: 6617.41
  awf: 181.32
  aof: 414.91
  wko: 33.09
  whk_amt: 99.26
  zvw: 403.66
  total: 1132.24
```

## Ask the client first

1. Total 2026 fiscal wage per withholding agent (column 14), and how much of it is former-employment wage or artists' and athletes' fees.
2. A list of every allowance, gift, facility and reimbursement in 2026: what, to whom, value including VAT, any employee contribution, and how it was booked (employee wage, final-levy wage, targeted exemption).
3. Is any entity linked to others by a 95% or more interest, and do they want the group election?
4. Does anyone receive designated items above EUR 2,400 in the year, or earn at or near the minimum wage?
5. Gifts to business contacts, agency workers or freelancers, and were the recipients told final levy applies?
6. Any van used in turn by several employees, and any past items not booked at all?
7. Return period (month or four weeks), so we know which 2027 return carries the settlement.
8. Is the employer registered, and what does its current Whk notice say? Is it small, medium or large for Aof?
9. For each employee: identity and BSN, date of birth (AOW age, youth minimum wage), country of residence and where they work.
10. The contract: indefinite or fixed, on-call or not, contracted hours. This decides AWf low or high.
11. Has the employee asked for the payroll tax credits with this employer, and do they have another job or a benefit?
12. Is anyone a director with a substantial interest, an expat with a 30% decision, or working partly abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), para. 4.2, 4.12.5, ch. 6, 7 (incl. §7.5), 9, 10, 13, 14, 22, 25.4 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-27 |
| Belastingdienst, rates appendix loonheffingen 2026, edition 4 (25 June 2026), tables 5.1, 9, 10, 11, 12, 13 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-10-27 |
| Belastingdienst, period codes and filing and payment dates 2026 | https://download.belastingdienst.nl/belastingdienst/docs/tijdvakcodes-aangiftedatums-betaaldatums-lh2101t62fd.pdf | 2026-10-27 |
| Wet op de loonbelasting 1964, art. 12a, 20a, 22, 26b, 31 and 31a | https://wetten.overheid.nl/BWBR0002471/2026-01-01 | 2026-10-27 |
| Belastingdienst, mileage allowance EUR 0.25 (news of 25 June 2026) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte | 2026-10-27 |
| Rijksoverheid, minimum wage 2026 | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 | 2026-10-27 |
| Rijksoverheid, holiday allowance | https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld | 2026-10-27 |
| Burgerlijk Wetboek Book 7, art. 629, 634, 640a | https://wetten.overheid.nl/BWBR0005290/2026-01-01 | 2026-10-27 |
| Rijksoverheid, transition payment | https://www.rijksoverheid.nl/vraag-en-antwoord/ontslag/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen | 2026-10-27 |
| Tweede Kamer, Belastingplan 2027, explanatory memorandum (kst. 37022 nr. 3) | https://zoek.officielebekendmakingen.nl/kst-37022-3.html | 2026-10-27 |

Not yet confirmed: the Belastingplan 2027 proposes abolishing the own-products exemption from 2027 (a bill, not law; do not apply to 2026). These older points were not re-read and stay out until checked: maternity and partner leave and their UWV benefits, working-time limits, the full payslip content list, third-party payments reporting, the employee-count limit for filing in Mijn Belastingdienst Zakelijk, the exact customary-wage exceptions for start-ups and loss-making companies, the overtime revision method for multiple contracts and business transfers, director-liability reporting deadlines in the Invorderingswet 1990, and the detailed conditions of the tools, training, workplace and bicycle exemptions (handbook ch. 22 to 23).

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
