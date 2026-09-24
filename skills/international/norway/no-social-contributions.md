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

Do not calculate a Norwegian contribution where the income type or National Insurance membership is unknown. A voluntary, partial or agreement-based result also needs the relevant NAV/Skatteetaten decision and collection route before using the ordinary calculator. Cross-border workers, non-residents, seafarers and people with an A1 or other coverage certificate require a separate coverage review. Under the EEA rules a worker is generally covered in one country; a posted worker can remain under the sending country’s system. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme)

### Boundary for business personal income

This Guide **consumes** the calculated business `personinntekt` from the taxpayer's provisional or final tax-return business information. It does not derive that number from bookkeeping. Skatteetaten starts the statutory calculation with net business income, then requires adjustments, including relevant capital income/costs, interest and tax-account items, risk-free return allowance and carried-forward negative personal income; its guidance also addresses spouse coordination. Therefore turnover, cash receipts and net business profit alone are not a safe contribution base. Obtain the official calculated figure or prepare that separate statutory calculation first. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/)

## 2. Determine the 2026 national-insurance rate

Skatteetaten’s current rate page gives the following 2026 rates:

| Personal-income category | 2026 rate | Source |
|---|---:|---|
| Ordinary salary, sickness benefit etc., age 17–69 | 7.6% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Ordinary business income | 10.8% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Primary business income from fishing, hunting or childminding in own home | 7.6% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Pension income and listed age groups | 5.1% | [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |

For the core sole-proprietor case, use **10.8%** only on the confirmed 2026 business-personal-income base. Wage income is a separate category. Do not replace the business rate with an employer contribution rate.

## 3. Apply the lower threshold and 25% phase-in cap

The 2026 lower limit is **NOK 99,650**. Below or at that base, no national-insurance contribution is due. Above the lower limit, the contribution can never exceed **25% of the amount above NOK 99,650**. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/)

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

`Arbeidsgiveravgift` is the employer’s separate liability on wages and other qualifying remuneration. It is geographically and activity differentiated. The employer’s registered location, actual activity and calculation code determine the rate; general-industry rates range from 0% in zone V to 14.1% in zone I. [Skatteetaten employer-contribution rates](https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/) and [2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)

For a zone Ia employer, the 10.6% rate is available until the advantage versus 14.1% reaches NOK 850,000, after which the 14.1% rate applies for the rest of the year. Apply the published advantage formula only to a confirmed payroll case. This employer rule does **not** change an individual sole proprietor’s 10.8% rate. [Skatteetaten 2026 employer contribution guidance](https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/)

## 6. Filing and payment controls

For self-employed income, include projected business profit and other income/wealth without withholding in the tax deduction card so Skatteetaten can calculate advance tax. A self-employed person with profit normally pays advance tax. It is generally invoiced four times, due 15 March, 15 June, 15 September and 15 December; an amount below NOK 2,000 is normally invoiced once. Skatteetaten takes weekends and holidays into account for those due dates. Update the tax deduction card as profits change. [Skatteetaten advance tax](https://www.skatteetaten.no/en/person/taxes/tax-deduction-card-and-advance-tax/advance-tax/)

The advance-tax invoice is not a separate national-insurance return: it is the cash-collection route for the taxpayer’s projected tax liabilities. Check the annual tax return and assessment against the final business-personal-income calculation. Where underpaid tax is anticipated, Skatteetaten says additional advance tax may be paid by 31 May of the following year to avoid interest on the underpayment. [Skatteetaten underpaid tax](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-assessment/underpaid-tax/)

For an employer with payroll, file the a-melding by the 5th of the following month (next working day where the fifth is non-working). From January 2026, withheld tax is payable by the first working day after payroll; employer national-insurance contributions are paid collectively every other month. [Skatteetaten employer payment guidance](https://www.skatteetaten.no/en/business-and-organisation/employer/employers-national-insurance-contributions/payment-of-withholding-tax-and-employers-national-insurance-contributions/) and [a-melding deadlines](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/)

Submit the sole-proprietor tax return with its business information by **31 May** each year. The same official page says a weekend deadline is met on the next working day, and an extension must be requested before expiry. The final annual assessment is the control point for the contribution amount. [Skatteetaten: tax return for sole proprietorships](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/sole-proprietorships/)

Keep the contribution outside the business-personal-income calculation: it is calculated on `personinntekt` and is additional to income tax. In particular, do not subtract an estimated national-insurance contribution from the official business `personinntekt` input. For the limited double-taxation-relief question, Skatteetaten’s 2026 guidance expressly says a taxpayer who is a member of the Norwegian National Insurance Scheme does not receive a deduction in or reduction of the contribution. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/) and [2026 advance-assessment guidance](https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/)

### Required working-paper output

Retain a short calculation record with: membership outcome and dates; every rate category and its official source base; the selected year and rates; each ordinary category amount; the one aggregate lower-limit/ceiling calculation; the unrounded estimate and the official assessed rounding outcome; the advance-tax amounts reconciled to that estimate; and every unresolved fact or referral. This record supports review of the calculation without presenting the illustrative arithmetic as the filed assessment.

Reconcile the business-personal-income calculation, advance-tax basis, annual return, payroll, a-melding feedback, payment identifiers and general ledger. Preserve corrections and the evidence for any changed contribution base.

## 7. Exceptions and decision rules

| Facts | Operational treatment |
|---|---|
| Ordinary sole proprietorship, compulsory member, age 17–69 | Calculate on the official business-personinntekt input at 10.8%, subject to lower limit/taper. |
| Fishing/hunting or childminding at home of qualifying children | Use the 7.6% business-income category only after confirming the activity conditions. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| Under 17 or over 69 in the income year | Use the 5.1% personal-income category, then apply the lower limit/taper. [Skatteetaten rates](https://www.skatteetaten.no/en/rates/national-insurance-contributions/) |
| No business personinntekt or a loss | No contribution is produced by that negative/nil business base; do not treat turnover as the base. In a mixed calculation, after official business/spouse coordination and carry-forward treatment, enter zero for a remaining negative business result rather than netting it against salary or pension. [Skatteetaten: personal income in a sole proprietorship](https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/income-in-business/personinntekt-i-enkeltpersonforetak/) and [Skatte-ABC: coordination of negative calculated business personal income](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/e-5-enkeltpersonforetak--beregnet-personinntekt-foretaksmodellen/E-5.096/E-5.097/) |
| Salary plus business income | Determine each rate, calculate each ordinary amount, then apply one aggregate lower-limit/taper formula to total personinntekt; do not give each stream a separate lower limit. Use the final official business result after statutory coordination; floor a remaining negative business contribution entry at zero. [Skatte-ABC](https://www.skatteetaten.no/rettskilder/type/handboker/skatte-abc/gjeldende/p-15-personinntekt--trygdeavgiftpensjonspoengpensjonsbeholdning/P-15.027/P-15.035/) |
| Voluntary, partial or agreement/EEA coverage; pension exception | Obtain the membership decision, dates and collection route. Do not apply the ordinary calculator until that evidence establishes the applicable Norwegian contribution. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme) |
| Employs others | Calculate employer contribution and a-melding/payments separately; it does not replace the owner’s contribution. [Skatteetaten employer rates](https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/) and [a-melding deadlines](https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/) |
| Foreign coverage, a posted worker, or multi-country work | Establish which country’s scheme applies before a Norwegian contribution calculation. [NAV membership guidance](https://www.nav.no/en/home/rules-and-regulations/membership-of-the-national-insurance-scheme) |

## When to refuse or refer

Do not use the ordinary calculator without the membership outcome, rate-category bases and official business `personinntekt`. Refer membership, cross-border, special-activity, reorganisation, certificate and employer classification questions to the applicable NAV or Skatteetaten route.

- Membership is voluntary, partial, disputed, covered elsewhere, or dependent on a pension exception.
- The personal-income calculation, activity category, age category, income allocation or coverage evidence is incomplete.
- The taxpayer needs a component allocation, special employer calculation, reorganisation result or cross-border coverage decision.

## 8. Escalate rather than infer

Professional review is required for unresolved National Insurance membership, Norway/EEA or other cross-border work, non-resident business, fishing/hunting/childminding classification, multiple activities with an unavailable official personal-income result, business reorganisations, social-security certificates, tax treaties and employee/contractor status. A simple nil or negative business-personal-income input produces no contribution from that business under this method. Check the selected year in each official Skatteetaten rate service immediately before filing.

Official sources were retrieved on 24 September 2026 and are retained as exact snapshots in this packet. The existing public Guide’s 2025 scope was inspected on 23 September 2026; its rates were not carried into this 2026 draft.

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
