---
name: north-macedonia-payroll
description: "Use this skill to calculate North Macedonia salary withholding and gross-to-net pay for calendar year 2026. Trigger on payroll, MPIN, salary PIT, employee tax, employer cost, director fees, benefits in kind, contribution cap, personal reduction or denar salary. It covers ordinary employment, separately classified director and service payments, taxable benefits, the 2026 monthly reduction, the July pension/unemployment rate change, monthly filing and payment, employee records and annual PIT reconciliation. Use the social-contributions skill for insured-group classification and special bases, and the cross-border skill for foreign salary and treaty applications. The calculations produce reviewable working papers and do not constitute a licensed accountant’s sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
---

# North Macedonia payroll withholding v0.3

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

Domestic payers of salary, salary compensation and employer-performance payments calculate salary PIT and insurance per employee/month. [PIT arts. 14-17, 80, 84-85][pit] cover both residents and local employment of nonresidents; art. 16(1)(7) expressly gives the salary base reduction to a nonresident employee of a resident payer. Standalone board/management fees and temporary personal services are income from work but use their own art. 16 base. Insurance follows actual status in the contributions skill, rather than the payment label.

This is ordinary withholding. Labour-law minimum pay, overtime, leave entitlements and immigration permissions must be established from the employment documents and governing labour rules before this tax calculation. Do not treat a contribution floor as the minimum salary payable.

## Rates, bands and thresholds

| Item | Amount | Period | Official provision |
|---|---|---|---|
| Salary PIT | 10% | 2026 | [PIT art. 11][pit] |
| Salary/pension reduction | 10,932 monthly; published annual 131,184 | 2026 | [PIT arts. 10, 17][pit]; [2026 publication][allowance] |
| Ordinary employee pension | 18.8% / 19.9% | January-June / July-December wage months | [Contributions Law art. 25][social]; [UJP dated table][rates] |
| Employee health and additional health | 7.5% and 0.5% | 2026 | [Contributions Law arts. 10-11, 25][social] |
| Employee unemployment | 1.2% / 0.1% | January-June / July-December wage months | [Contributions Law arts. 12, 25][social]; [dated table][rates] |
| Employee contribution base floor / ceiling | 34,570 / 1,106,256 per month, UJP-published amounts | 2026 | [Contributions Law arts. 15-16][social]; [2026 bases][bases] |
| Private-use company vehicle benefit | 1% monthly of prior 31 December book value, less employee consideration; acquisition-year/lease valuation follows its specific rule | 2026 | [PIT art. 16(1)(2-b),(2-v)][pit] |
| Late-payment interest | 0.03% per overdue day | 2026 | [Tax Procedure Law art. 123][procedure] |

Art. 25 expressly switches with the **July wage**; do not change a June arrears calculation merely because it is paid in July. PIT rate/reduction for salary also follow the month to which salary relates (PIT art. 92(2)).

## The base

**Ordinary full-month gross-to-net worksheet:**

1. Establish gross salary, taxable salary compensation and performance payments for the month. Include taxable work benefits and excess reimbursements using their statutory bases; separate noncash benefits from cash available for payout (PIT arts. 15-16).
2. For the ordinary employee class, use contributory salary subject to the arts. 15-16 floor and ceiling, then compute each fund with the wage-period rates. Ordinary total is 28% in both periods, but the fund split changes. The social-contributions skill handles part-time/absence exceptions, other insured groups and employer-funded extended-service insurance.
3. Salary PIT base is gross salary less applicable compulsory insurance less the month's available salary reduction. Do not produce a negative PIT base or cash refund from unused monthly reduction. Apply 10% (PIT arts. 9-11, 16-17; [MPIN rulebook art. 3][contrib-rules]).
4. Cash salary net is cash gross less employee insurance, salary PIT and authorised nontax deductions. Do not pay out a noncash benefit as salary cash. Employer cost includes contractual gross and any separately employer-borne legal contribution, including designated extended-service pension; do not add the same employee deduction twice.
5. Reconcile gross, each fund, taxable base, PIT and net to MPIN and bank payment. Keep analytical decimals until applying accepted MPIN rounding. The examples retain two decimals and do not assert a statutory universal rounding convention.

**Benefits and fees:** art. 16 values employer-provided housing at comparable local rent, or the employer's paid rent where rented. Company private vehicle use uses the specific monthly 1% valuation; acquisition-year/lease vehicles follow art. 16(1)(2-v), not a guessed current resale value. Free/discounted employer/related-company equity is market value at acquisition less price paid (art. 16(1)(2-g)); listed securities, vouchers and goods/services follow art. 16's specified market/nominal rules. Keep each benefit in its appropriate insurance and PIT category; a taxable benefit is not automatically cash salary.

For standalone directors' fees and occasional service fees, art. 16(1)(5) uses the receipt's amount and does not give the ordinary salary reduction. Their contribution treatment is established separately; uninsured executive directors/managers have a specific pension/health class. Do not promise that all service contracts have no insurance. A self-employed professional's business receipts instead belong in the income-tax/business skill.

**Allowances and losses:** exempt reimbursements require the exact [PIT art. 12][pit] conditions and evidence; an unexplained transfer or label is not an exemption. [UJP hours guidance step 2][hours] calculates gross salary and the personal reduction proportionately to hours worked where the employee works fewer than the full month hours. Use full-month hours and actual worked hours, not a calendar-day fraction. For ordinary part-time and joining/leaving months, apply the employee hours-based floor and ceiling in the social-contributions skill, with floor top-ups declared separately. Its mixed work/sickness formula separates effective-work insurance from replacement payments. The salary reduction is not duplicated on unrelated income. Reconcile the right actually used across salary/pension payers to the art. 10 annual limit. Business or investment losses do not form an automatic negative item in a salary withholding calculation.

For a lump-sum self-employed proprietor who also employs staff, distinguish
UJP's own-proprietor contribution calculation from the employer's continuing
employee MPIN duty. [UJP's current implementation notice](https://ujp.gov.mk/mk/javnost/soopstenija/pogledni/1284?print=1)
confirms the split from July 2026. Use the social-contributions skill for that
route; a proprietor's receipt is not an employee salary merely because MPIN is
used.

## Deadlines and filing

Register the employer/remitter and the person's insurance status with the competent bodies. Obtain the UJP identification/signing access and use the accepted electronic MPIN workflow under [rulebook arts. 4-7][contrib-rules]. Keep entry, change and cessation records and the final wage month aligned with the insurance register; cessation does not cancel returns for earlier months.

[PIT art. 85(9)][pit] and [Contributions Law art. 18][social]: monthly salary MPIN by the **10th of the next month**, separately by individual. Correct rejected or incorrect submissions and obtain UJP confirmation before payment. PIT is remitted at each salary payment (PIT art. 92). Contributions mature on payment; if ordinary salary is unpaid, contributions mature by the **15th of the next month** (Contributions Law art. 24). Do not generalise that contribution maturity into a separate unpaid-salary PIT payment deadline.

Other covered domestic income: e-PDD calculation **before each payment**, UJP approval, then withholding/remittance **at payment** (PIT arts. 84-85, 92). Standalone director insurance calculations are likewise before payment (Contributions Law art. 18(3)).

Issue the PIT/contribution calculation with each payment (PIT art. 85(10)); the contribution certified statement is due no later than **15 days after payment**, with annual contribution summary by **15 February 2027** (Contributions Law art. 22). The individual's annual PIT return is supplied by **30 April 2027**, confirmed/corrected by **31 May**, and annual balance due **30 June**, with assessment adjustments due **15 days after service** (PIT arts. 96-100). It does not replace monthly withholding.

## Penalties and interest

[PIT art. 108][pit] payer failures to calculate/pay or comply with art. 85: micro legal person **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent. Responsible-person ranges are respectively **EUR 50-250**, **100-500**, **150-500**, **200-500**. [Contributions Law arts. 28-a, 28-b][social] separately sanction incorrect/late MPIN and salary paid without timely contributions; use the offence and remitter-size classification. [Tax Procedure Law art. 123][procedure] charges interest at **0.03% daily** from the day after maturity. The payer guarantees withheld PIT under PIT art. 102. UJP can assess tax and contributions for **5 years** from the end of the year in which the event occurred, **10 years** for tax evasion, with an absolute 10-year cut-off (Tax Procedure Law art. 110); collection of assessed amounts lapses **10 years** after the year they fell due (art. 122-a).

## Cross-border points

Local work, tax residence, employer identity, PE bearing the cost and the particular treaty determine foreign salary taxation; do not assume an exemption from fewer than 183 days alone. Salary paid abroad to a resident requires self-reporting where no local payer withholds. [PIT art. 88(2)][pit] gives **31 March next year** for foreign salary/pension with foreign tax paid, while other foreign income follows the ordinary monthly art. 88 timetable. The art. 8 foreign credit is capped to domestic tax on the income. Social-insurance agreements and evidence must be tested separately from tax treaties.

## Two worked examples that recompute

**Simple: June salary 50,000, full allowance.** Employee fund deductions are pension 9,400, health 3,750, additional health 250 and unemployment 600. Total 14,000; PIT base 25,068, PIT 2,506.80, net 33,493.20. Ordinary employer gross cost is 50,000, assuming no separately employer-borne extra.

```oa-check
name: MK June 2026 ordinary salary
inputs:
  gross: 50000
  allowance: 10932
steps:
  - pension: gross * 0.188
  - health: gross * 0.075
  - injury_health: gross * 0.005
  - unemployment: gross * 0.012
  - contributions: pension + health + injury_health + unemployment
  - base: max(0, gross - contributions - allowance)
  - pit_tax: base * 0.10
  - net: gross - contributions - pit_tax
expected:
  pension: 9400
  health: 3750
  injury_health: 250
  unemployment: 600
  contributions: 14000
  base: 25068
  pit_tax: 2506.80
  net: 33493.20
```

**Edge: July salary 1,500,000 above the contribution cap.** Contributions use 1,106,256, with the new pension/unemployment split; the salary PIT base still starts with the entire salary. Two-decimal fund amounts total 309,751.68. PIT is 117,931.63 and net 1,072,316.69. The example assumes a single remitter, full reduction and no additional benefits or extended-service charge.

```oa-check
name: MK July 2026 salary above insurance cap
inputs:
  gross: 1500000
  allowance: 10932
steps:
  - insurance_base: min(max(gross, 34570), 1106256)
  - pension: round(insurance_base * 0.199, 2)
  - health: round(insurance_base * 0.075, 2)
  - injury_health: round(insurance_base * 0.005, 2)
  - unemployment: round(insurance_base * 0.001, 2)
  - contributions: pension + health + injury_health + unemployment
  - base: max(0, gross - contributions - allowance)
  - pit_tax: round(base * 0.10, 2)
  - net: gross - contributions - pit_tax
expected:
  insurance_base: 1106256
  pension: 220144.94
  health: 82969.20
  injury_health: 5531.28
  unemployment: 1106.26
  contributions: 309751.68
  base: 1179316.32
  pit_tax: 117931.63
  net: 1072316.69
```

## Ask the client first

- What wage month and cash/noncash gross components are being paid?
- Is the person an employee, standalone director, occasional contractor or registered business?
- What insurance status, hours, absences and other employers apply?
- What salary/pension reduction has already been used and what corrections remain?
- Where was work performed, who bears the cost and what foreign tax/insurance evidence exists?

## Sources

| Official source | URL | Read on |
|---|---|---|
| UJP September 2026 proprietor/employee MPIN duty distinction | https://ujp.gov.mk/mk/javnost/soopstenija/pogledni/1284?print=1 | 2026-10-24 |
| UJP, gross salary calculation guidance, steps 2-4 | https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1 | 2026-10-24 |
| Personal Income Tax Law, consolidated through Gazette 274/2022 | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Mandatory Social Insurance Contributions Law, through Gazette 148/2026 | https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf | 2026-10-24 |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| UJP, 2026 reduction, publication 23-6493/1 of 17 December 2025, under PIT art. 10(4) | https://www.ujp.gov.mk/e/plakjanje/licno_osloboduvanje | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| UJP, dated contribution-rate tables | https://www.ujp.gov.mk/en/vodic/category/641?print=1 | 2026-10-24 |
| UJP, 22 January 2026 contribution-base announcement | https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187 | 2026-10-24 |
| Contribution calculation/payment rulebook, MPIN structure | https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf | 2026-10-24 |

[pit]: https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf
[hours]: https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1
[social]: https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf
[allowance]: https://www.ujp.gov.mk/e/plakjanje/licno_osloboduvanje
[rates]: https://www.ujp.gov.mk/en/vodic/category/641?print=1
[bases]: https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187
[contrib-rules]: https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf

Not yet confirmed: The 2026 statutory minimum wage amount and the Employment Agency registration steps before a new hire starts (labour law, not checked in this review). Specialist protected-hours, non-working and benefit-replacement insurance computations outside this ordinary employee scope. The separate first-calendar-year professional issue in the social-contributions skill concerns self-employed insurance, not employee salary withholding.

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
