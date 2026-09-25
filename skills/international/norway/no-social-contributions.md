---
name: no-social-contributions
description: Use this skill whenever asked about Norwegian social contributions (trygdeavgift) for self-employed individuals operating as enkeltpersonforetak (sole proprietorship). Trigger on phrases like "trygdeavgift", "Norwegian social security", "self-employed contributions Norway", "NAV contributions", "national insurance Norway", "how much trygdeavgift do I pay", or any question about social contribution obligations for a self-employed client in Norway. This skill covers the 10.9% rate on business income, minimum thresholds, payment schedule, interaction with trinnskatt and income tax, exemptions, and edge cases. ALWAYS read this skill before touching any Norway social contributions work.
version: 2.0
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway social contributions: 2026 self-employed national-insurance method

**Status: Source-cited draft by the OpenAccountants team.** Figures are for income year 2026. This is a replacement for the public `no-social-contributions` Guide’s sole-proprietor scope: Norwegian *trygdeavgift* for a self-employed person operating an `enkeltpersonforetak`. It also separates employer contributions so the two liabilities are not confused. It makes no accountant-attestation claim.

## The method, step by step

1. Confirm the membership outcome, rate category and official business `personinntekt` input.
2. Calculate each confirmed category at its rate, then apply the single lower-limit and aggregate phase-in ceiling.
3. Reconcile the advance-tax and annual-return records; separate any employer payroll obligations.

## Ask the client first

- What is the National Insurance membership outcome, effective period and collection route?
- What calculated `personinntekt` appears in the provisional or final business tax information, and what other rate-category income exists?
- What are the person’s age, activity type, cross-border/coverage facts, and any payroll-employer facts?

## 1. Gather the facts before calculating

Obtain and retain:

1. Tax residence plus National Insurance membership outcome and effective dates: compulsory, voluntary, partial, agreement/EEA-covered elsewhere, non-member, or the NAV pension exception.
2. Each income category’s calculated **personinntekt**, including the business figure shown in the provisional or final tax-return business information; never substitute revenue, accounting turnover, cash received or net business profit alone.
3. The person’s age in the income year, and whether the business is ordinary, fishing/hunting, or qualifying childminding.
4. Other wages, pension, benefits, business activities and any foreign work or social-security coverage.
5. The provisional-tax calculation, tax return, bookkeeping records and any advance-tax notices.

National Insurance membership is the eligibility gate. NAV says it can arise from residence or employment, is governed by the National Insurance Act and social-security agreements, and is not decided merely by citizenship, National Population Register entry or Norwegian tax payment. A person who is not a member does not pay the contribution, subject to the pension exception described by NAV. A person moving to Norway for a legal stay intended to last at least 12 months is generally a member from entry; a person working in Norway can also be compulsorily covered despite not living there. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme)

Do not calculate a Norwegian contribution where the income type or National Insurance membership is unknown. A voluntary, partial or agreement-based result also needs the relevant NAV/Skatteetaten decision and collection route before using the ordinary calculator. Cross-border workers, non-residents, seafarers and people with an A1 or other coverage certificate require a separate coverage review. NAV decides applicable-legislation and membership questions under the EEA rules and other social-security agreements, and an A1 or other form issued by another state is not by itself enough: Skatteetaten applies an exemption from Norwegian membership only once NAV has verified it. [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/) Under the EEA rules a worker is generally covered in one country; a posted worker can remain under the sending country’s system. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme)

### Boundary for business personal income

This Guide **consumes** the calculated business `personinntekt` from the taxpayer's provisional or final tax-return business information. It does not derive that number from bookkeeping. Skatteetaten starts the statutory calculation with net business income, then requires adjustments, including relevant capital income/costs, interest and tax-account items, risk-free return allowance and carried-forward negative personal income; its guidance also addresses spouse coordination. Therefore turnover, cash receipts and net business profit alone are not a safe contribution base. Obtain the official calculated figure or prepare that separate statutory calculation first. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/)

## 2. Determine the 2026 national-insurance rate

Skatteetaten’s current rate page gives the following 2026 rates:

| Personal-income category | 2026 rate | Source |
|---|---:|---|
| Ordinary salary, sickness benefit etc., age 17–69 | 7.6% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Ordinary business income | 10.8% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Primary business income from fishing, hunting or childminding in own home (children under 12 years of age or with special care needs), age 17–69 | 7.6% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Pension income; and salary, business income and pensions of persons aged under 17 or over 69 in the income year | 5.1% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |

For the core sole-proprietor case, use **10.8%** only on the confirmed 2026 business-personal-income base of a person aged 17 to 69 in the income year. Wage income is a separate category. Do not replace the business rate with an employer contribution rate.

The 7.6% business rate is conditional. Skatteetaten limits it to self-employed persons within fishing, hunting or childminding in own home, and for childminding only where the children are under 12 years of age or have special care needs. Childminding outside the home, or of older children without special care needs, stays at 10.8%. Where the activity is mixed, confirm how much of the business income is primary income from the qualifying activity before applying 7.6% to any of it. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

Age is tested for the income year. A person who is under 17 or over 69 in the income year pays 5.1% on salary and business income as well as on pensions, so a sole proprietor who is over 69 in the income year does not pay 10.8%. For someone who turns 17 or 70 during the year, confirm the age category Skatteetaten applies in the tax assessment rather than assuming it. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

**Rate-category examples (2026, illustrative):** a sole proprietor aged 72 with business personinntekt NOK 300,000 pays `300,000 × 5.1% = NOK 15,300`; a qualifying self-employed fisherman aged 40 with the same base pays `300,000 × 7.6% = NOK 22,800`. In both cases the 25% ceiling (NOK 50,087.50) is higher, so it does not reduce the amount. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

## 3. Apply the lower threshold and 25% phase-in cap

The 2026 lower limit is **NOK 99,650**. Below or at that base, no national-insurance contribution is due. Above the lower limit, the contribution can never exceed **25% of the amount above NOK 99,650**. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

There is **no upper income ceiling**. Once total personal income is above the lower limit, the contribution is calculated on the whole base in the usual way (Skatte-ABC: "beregnes trygdeavgift av hele grunnlaget på vanlig måte"); the 25% rule only limits the amount in the phase-in range. Do not cap the base at any pension or benefit ceiling. [Skatte-ABC P-15-4.3](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/)

For ordinary business income in the phase-in range:

```text
ordinary contribution = personinntekt × 10.8%
phase-in ceiling = (personinntekt − NOK 99,650) × 25%
2026 contribution = lower of those two amounts
```

Use the official tax-return calculation for filing. The worked arithmetic below is unrounded mathematical output displayed to two øre; it does not state a filing-rounding rule.

| Case | Confirmed personinntekt | Ordinary 10.8% calculation | Phase-in ceiling | Expected contribution |
|---|---:|---:|---:|---:|
| Source | [Skatteetaten national-insurance rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) | Same source | Same source | Illustrative arithmetic below |
| Boundary | NOK 99,650 | NOK 10,762.20 | NOK 0.00 | **NOK 0.00** |
| Phase-in | NOK 120,000 | NOK 12,960.00 | (120,000 − 99,650) × 25% = NOK 5,087.50 | **NOK 5,087.50** |
| Near crossover | NOK 175,000 | NOK 18,900.00 | (175,000 − 99,650) × 25% = NOK 18,837.50 | **NOK 18,837.50** |
| Ordinary-rate case | NOK 300,000 | NOK 32,400.00 | NOK 50,087.50 | **NOK 32,400.00** |
| Loss / nil base | Nil or negative | n/a | n/a | **NOK 0.00** |

The crossover is approximately NOK 175,440.14: below it the 25% ceiling can constrain the ordinary 10.8% amount; above it, the ordinary rate gives the lower result. This is derived arithmetic from the two official 2026 inputs, not an official threshold. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

## 4. Handle combined income correctly

The lower limit and taper apply to **total personinntekt**, not business turnover. For an owner of an `enkeltpersonforetak`, the calculated business personal-income amount is one contribution base. It is not simply net business profit less a generic capital-income label: use the official calculated amount described in section 1. Personinntekt is also the base used for bracket tax. [Skatteetaten 2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/) and [sole-proprietor personal-income method](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/)

Where the taxpayer has both salary and ordinary business personal income, first identify both bases and their current rates, then assess the lower limit and 25% ceiling against the taxpayer’s combined personal-income basis. Do not grant a second NOK 99,650 lower limit to the business merely because the taxpayer also has wage income. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) and [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

**Combined-income example:** salary NOK 100,000 and ordinary business personinntekt NOK 100,000 gives combined personinntekt NOK 200,000. The ordinary rate amounts are NOK 7,600 (salary) and NOK 10,800 (business), total NOK 18,400. The ceiling is `(200,000 − 99,650) × 25% = NOK 25,087.50`; the ordinary total is lower, so the phase-in ceiling does not reduce it. The wage and business categories still remain separate for rate selection and payroll reporting. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

### Aggregate calculation where income has different rates

Skatte-ABC confirms that the lower limit uses **total** personal income across low, middle and high rate bases, and that **total** national-insurance contribution cannot exceed 25% of total personal income above the lower limit. Calculate each confirmed category at its applicable rate, then apply one aggregate ceiling:

```text
total personal income = sum of confirmed low-, middle- and high-rate bases
ordinary total = sum of (each category base × its confirmed rate)
aggregate ceiling = max(0, total personal income − NOK 99,650) × 25%
total contribution = 0 if total personal income is at or below NOK 99,650;
                     otherwise lower of ordinary total and aggregate ceiling
```

For this aggregate working paper, first obtain the **officially coordinated and carry-forward-adjusted business result**. Then floor that final business contribution entry at zero before adding it to a salary or pension base. A remaining negative calculated business `personinntekt` therefore creates no negative contribution base and does not reduce the salary or pension entry. Do not floor an individual activity before the statutory business/spouse coordination is complete. Where that official coordinated result is unavailable, stop and resolve it before calculating. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/) and [Skatte-ABC: coordination of negative calculated business personal income](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.096/E-5.097/)

This produces the total liability without allocating a capped amount back to salary, business or pension components. Component allocation is unnecessary for this Guide's contribution total; use the official tax calculation if a filing system requires an allocation. [Skatte-ABC: personal income and national-insurance contributions](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/)

**Binding mixed-rate case:** salary NOK 60,000 plus ordinary business `personinntekt` NOK 60,000, age 40. Ordinary amounts are NOK 4,560 (`60,000 × 7.6%`) and NOK 6,480 (`60,000 × 10.8%`), total NOK 11,040. Total personal income is NOK 120,000 and the aggregate ceiling is `(120,000 − 99,650) × 25% = NOK 5,087.50`. The expected **total** contribution is therefore **NOK 5,087.50**. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) and [Skatte-ABC](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/)

## 5. Keep income-tax and employer liabilities separate

National-insurance contributions sit alongside ordinary income tax and any bracket tax; do not add a combined marginal rate from a prior year. The Guide’s calculation covers only the national-insurance layer and uses the official 2026 rate and lower-limit inputs. [Skatteetaten national-insurance rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

`Arbeidsgiveravgift` is the employer’s separate liability on wages and other qualifying remuneration for work and assignments. It is not charged on the sole proprietor’s own business profit or drawings: the owner pays the 10.8% personal contribution instead. As a main rule it is also not charged where the person paid carried out the work as part of their own business, so check contractor status before treating a payment to a self-employed person as wages. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)

**Zone and rate (2026).** The rate follows the zone of the municipality where the enterprise (or its registered sub-unit) must be registered in the Central Coordinating Register; a private individual employer uses the zone of their registered home address. Zones and rates are unchanged from 2025 to 2026. [Skatteetaten employer-contribution rates](https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/) and [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)

| Zone | General industries | Agriculture, forestry, fisheries etc. | Source |
|---|---:|---:|---|
| I | 14.1% | 14.1% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| Ia | 10.6% within the NOK 850,000 exemption amount, then 14.1% | 10.6% on all pay | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| II | 10.6% | 10.6% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| III | 6.4% | 6.4% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| IV | 5.1% | 5.1% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| IVa | 7.9% | 5.1% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |
| V | 0% | 0% | [2026 guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) |

Source for the table: [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/), points 4.2 and 4.6.

**Conditions that change the rate:**

- **Zone Ia exemption amount (fribeløp).** A zone Ia employer uses 10.6% until the difference between contributions at 14.1% and at 10.6% exceeds NOK 850,000 in the year, then 14.1% for the rest of the year. Skatteetaten puts the break-even at `850 000 / (0.141 − 0.106)`, about NOK 24.3 million of pay. There is **one** exemption amount per legal entity, however many sub-units it has, and a group is assessed as a whole. State administration bodies and health trusts get **no** exemption amount in zone Ia and pay 14.1% there. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)
- **Sector-excluded activities.** Employers in the steel sector, coal sector, financial and insurance sector (where it is the main activity) and in-group head-office and management-consultancy services (where it is the main activity) must pay 14.1% in every zone, except that they may use the zone rate within one NOK 850,000 exemption amount. For finance, insurance and head-office activity the 14.1% applies to all employees, even those doing other work. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)
- **Enterprises in economic difficulty**, and employers with an outstanding claim to repay illegal state aid, likewise pay 14.1% in all zones except within a NOK 850,000 exemption amount. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)
- **De minimis cap.** Reduced-rate aid under the exemption-amount rules and other de minimis aid together cannot exceed EUR 300,000 per legal entity or group over a 3-year period, even if the NOK 850,000 annual amount is not used up. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)
- **Work outside the registration zone.** For mobile (ambulatory) activity, where an employee does more than half of the month’s work in another zone, that zone’s rate applies to the matching share of pay; for remote work (such as a home office) this applies only if the other zone’s rate is higher. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)
- **Private households.** A private individual employer pays no employer contribution while the household’s total wages in the income year do not exceed NOK 60,000; above that, contribution is due on the whole amount. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)

**The extra 5% no longer applies.** The additional employer contribution of 5% on an income recipient’s pay above a yearly threshold (NOK 850,000 for 2024) entered into force on 1 January 2023 and was discontinued from 1 January 2025; Skatteetaten rejects an a-melding that reports it for payments made in 2025. Do not add it for 2026. [Skatteetaten: employer’s additional national insurance contributions](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employers-national-insurance-contributions-and-financial-activity-tax/employers-additional-national-insurance-contributions/)

**Employer worked case (2026):** a general-industry employer registered in zone I pays one employee NOK 1,200,000 in 2026. Contribution is `1,200,000 × 14.1% = NOK 169,200`. No extra 5% is added on the part above NOK 850,000, because that scheme ended on 1 January 2025. This employer rule does **not** change an individual sole proprietor’s 10.8% rate. [Skatteetaten employer-contribution rates](https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/)

**Foreign workers and cross-border employers.** Social contributions (both the personal contribution and the employer contribution) are paid in the country whose scheme covers the worker. NAV decides applicable-legislation and membership questions under the EEA rules and other social-security agreements. An A1 or other certificate from another state’s authority is **not** by itself a verified exemption: Skatteetaten applies an exemption only after NAV has verified it, including at the advance-tax stage. A foreign employer with no registered business address in Norway falls in zone I. For workers posted to Norway from the USA, Canada or South Korea who are members only of the sickness-benefit part of the scheme, the 2026 employer rate is 7%. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) and [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

A foreign employee on the voluntary PAYE scheme (kildeskatt på lønn) pays a flat 25% on wages in 2026 (22.5% if under 17 or over 69, and 17.4% if not a member of the National Insurance Scheme); the scheme is closed to income above NOK 725,050. Route those workers to the PAYE rules rather than this calculator. [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

## 6. Filing and payment controls

For self-employed income, include projected business profit and other income/wealth without withholding in the tax deduction card so Skatteetaten can calculate advance tax. A self-employed person with profit normally pays advance tax. It is generally invoiced four times, due 15 March, 15 June, 15 September and 15 December; an amount below NOK 2,000 is normally invoiced once. Skatteetaten takes weekends and holidays into account for those due dates. Update the tax deduction card as profits change; online changes can be made until 15 December. If an instalment is not paid by its deadline, the advance tax for the rest of the year falls due, Skatteetaten can start enforced collection of the remaining advance tax for the whole year, and interest on overdue payment is charged. [Skatteetaten advance tax](https://www.skatteetaten.no/en/person/taxes/tax-deduction-card-and-advance-tax/advance-tax/)

The advance-tax invoice is not a separate national-insurance return: it is the cash-collection route for the taxpayer’s projected tax liabilities. Check the annual tax return and assessment against the final business-personal-income calculation. Where underpaid tax is anticipated, Skatteetaten says additional advance tax may be paid by 31 May of the following year to avoid interest on the underpayment. [Skatteetaten underpaid tax](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-assessment/underpaid-tax/)

For an employer with payroll, file the a-melding by the 5th of the following month (next working day where the fifth is non-working); Skatteetaten cannot grant a deferral of that deadline. From January 2026, withheld tax is payable by the first working day after payroll. Employer national-insurance contributions for the two previous months are paid together on 15 January, 15 March, 15 May, 15 July, 15 September and 15 November, using the KID number from the a-melding feedback. A calculated employer contribution below NOK 100 for a settlement period need not be paid, but the a-melding must still be submitted. [Skatteetaten employer payment guidance](https://www.skatteetaten.no/en/business-and-organisation/employer/employers-national-insurance-contributions/payment-of-withholding-tax-and-employers-national-insurance-contributions/) and [a-melding deadlines](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/)

Submit the sole-proprietor tax return with its business information by **31 May** each year. The same official page says a weekend deadline is met on the next working day, and an extension must be requested before expiry. The final annual assessment is the control point for the contribution amount. [Skatteetaten: tax return for sole proprietorships](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/)

Keep the contribution outside the business-personal-income calculation: it is calculated on `personinntekt` and is additional to income tax. In particular, do not subtract an estimated national-insurance contribution from the official business `personinntekt` input. For the limited double-taxation-relief question, Skatteetaten’s 2026 guidance expressly says a taxpayer who is a member of the Norwegian National Insurance Scheme does not receive a deduction in or reduction of the contribution. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/) and [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

### Required working-paper output

Retain a short calculation record with: membership outcome and dates; every rate category and its official source base; the selected year and rates; each ordinary category amount; the one aggregate lower-limit/ceiling calculation; the unrounded estimate and the official assessed rounding outcome; the advance-tax amounts reconciled to that estimate; and every unresolved fact or referral. This record supports review of the calculation without presenting the illustrative arithmetic as the filed assessment.

Reconcile the business-personal-income calculation, advance-tax basis, annual return, payroll, a-melding feedback, payment identifiers and general ledger. Preserve corrections and the evidence for any changed contribution base.

## 7. Exceptions and decision rules

| Facts | Operational treatment |
|---|---|
| Ordinary sole proprietorship, compulsory member, age 17–69 | Calculate on the official business-personinntekt input at 10.8%, subject to lower limit/taper. |
| Fishing/hunting, or childminding in own home of children under 12 or with special care needs | Use the 7.6% business-income category only for primary business income from that activity, after confirming the conditions; other childminding stays at 10.8%. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Under 17 or over 69 in the income year | Use the 5.1% personal-income category, then apply the lower limit/taper. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| No business personinntekt or a loss | No contribution is produced by that negative/nil business base; do not treat turnover as the base. In a mixed calculation, after official business/spouse coordination and carry-forward treatment, enter zero for a remaining negative business result rather than netting it against salary or pension. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/) and [Skatte-ABC: coordination of negative calculated business personal income](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.096/E-5.097/) |
| Salary plus business income | Determine each rate, calculate each ordinary amount, then apply one aggregate lower-limit/taper formula to total personinntekt; do not give each stream a separate lower limit. Use the final official business result after statutory coordination; floor a remaining negative business contribution entry at zero. [Skatte-ABC](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/) |
| Voluntary, partial or agreement/EEA coverage; pension exception | Obtain the membership decision, dates and collection route. Do not apply the ordinary calculator until that evidence establishes the applicable Norwegian contribution. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme) |
| Employs others | Calculate employer contribution and a-melding/payments separately; it does not replace the owner’s contribution. Confirm zone, calculation code, sector exclusions, economic-difficulty status and any zone Ia or sector exemption amount before choosing a rate below 14.1%; do not add the discontinued extra 5%. [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/) [Skatteetaten employer rates](https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/) and [a-melding deadlines](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/) |
| Foreign coverage, a posted worker, or multi-country work | Establish which country’s scheme applies before a Norwegian contribution calculation. Treat a foreign A1 or similar certificate as unverified until NAV has verified the exemption; until then Skatteetaten does not apply it, even for advance tax. [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/) [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme) |

## When to refuse or refer

Do not use the ordinary calculator without the membership outcome, rate-category bases and official business `personinntekt`. Refer membership, cross-border, special-activity, reorganisation, certificate and employer classification questions to the applicable NAV or Skatteetaten route.

- Membership is voluntary, partial, disputed, covered elsewhere, or dependent on a pension exception.
- The personal-income calculation, activity category, age category, income allocation or coverage evidence is incomplete.
- The taxpayer needs a component allocation, special employer calculation, reorganisation result or cross-border coverage decision.

## 8. Escalate rather than infer

Professional review is required for unresolved National Insurance membership, Norway/EEA or other cross-border work, non-resident business, fishing/hunting/childminding classification, multiple activities with an unavailable official personal-income result, business reorganisations, social-security certificates, tax treaties and employee/contractor status. A simple nil or negative business-personal-income input produces no contribution from that business under this method. Check the selected year in each official Skatteetaten rate service immediately before filing.

Official sources were retrieved on 24 and 25 September 2026 and are retained as exact snapshots in this packet. The existing public Guide’s 2025 scope was inspected on 23 September 2026; its rates were not carried into this 2026 draft.

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
