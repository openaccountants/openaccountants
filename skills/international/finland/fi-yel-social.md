---
name: fi-yel-social
description: Use this skill whenever asked about Finland YEL pension insurance or social security for self-employed persons. Trigger on phrases like "YEL", "YEL insurance", "yrittäjän eläkelaki", "self-employed pension Finland", "Finnish pension insurance", "entrepreneur pension", "YEL income", "YEL contribution", "sickness allowance Finland", "disability pension self-employed Finland", "new entrepreneur discount", or any question about mandatory social insurance obligations for Finnish self-employed. Covers YEL contribution rates, income thresholds, provider selection, tax deductibility, and social security benefits. ALWAYS read this skill before advising on Finnish self-employed social insurance.
version: 1.4
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-23
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - fi-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland YEL and self-employed social insurance v1.4 — 2026 editorial draft

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified or an attestation.

**Scope:** Use this method for ordinary Finnish self-employment to screen YEL eligibility, set proposed confirmed income, arrange the policy, calculate the 2026 contribution and route the tax deduction. It also flags the 2026 health insurance contributions and unemployment-fund conditions that depend on confirmed income. It does not decide international social-security coordination, disputed worker status, MYEL, benefit entitlement or a provider's individual decision.

## Rates and decision figures

| Item | 2026 figure or worked amount | Source / qualification |
| --- | --- | --- |
| Source | Figures in this table | [ETK YEL FAQs](https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/faqs-on-yel-insurance/); [Työeläke YEL income](https://www.tyoelake.fi/en/pensions-for-the-self-employed/what-is-yel-income/) |
| Annual lower / upper confirmed income | €9,423.09 / €214,000 | Eligibility limits. |
| Contribution / new-entrepreneur reduction | 24.40% / 22% | Initial reduction has the stated historical conditions. |
| Senior Oy shareholder test | more than 30% alone / more than 50% with family | Shares or voting rights. |
| Contribution flexibility | 10–100% increase / 10–20% reduction | Provider route and terms apply. |
| Review cap / pension accrual / unemployment-security income | €4,000 / 1.5% / €15,481 | Review and benefit rules have separate conditions. |
| Health insurance (Vero, 2026): self-employed daily allowance contribution | 1.11% where annual income is €17,255 or more; 0.23% where it is less | Age 16 to 67; Vero uses the YEL confirmed income. Health care contribution 1.10%; YEL replaces relevant business income/own-company wages for this contribution too (section 5a). |
| Ordinary illustrative contribution | €30,000 × 24.40% = €7,320; €7,320 ÷ 12 = €610 | A mathematical example, not an invoice schedule. |
| Eligible illustrative reduction | €7,320 × 78% = €5,709.60 | Apply only after confirming history. |

## Ask the client first

- When did the self-employment begin, and has it lasted (or will it last) at least four months without interruption, and when does the month after the 18th birthday begin?
- Is the person drawing an old-age, early old-age, partial old-age, disability or unemployment pension?
- Does the person also have a job (employment or service relationship)? It does not remove the YEL obligation.
- Does a spouse or other family member work in the business, are they paid, and does the spouse have split earnings in taxation?
- Has the person taken out voluntary pension insurance? It does not replace YEL.
- What work does the person actually perform, for how many hours, and what would an equally qualified outsider be paid?
- What are the entity, contract, ownership, voting-right and senior-position facts?
- Which countries are involved, and is there an A1 or applicable-country decision?
- Which pension provider, prior YEL periods, payer and provider quote apply?

## 1. Collect the record

Retain date of birth; any pension being drawn; work start, duration, hours, role, skills and responsibility; entity and contract facts; shares, votes, position and relevant family ownership; country/A1 facts; pension history; provider quote; payer; outsider-wage evidence; and the field, turnover, work-scope and professional-skill data used for the provider calculation service. Do not set YEL income from revenue, profit, dividends or a preferred benefit level. The one exception is a light entrepreneur using an invoicing service: there the size of the invoicing indicates the value of the work input.

## 2. Eligibility

YEL is required only if all of these hold: the person works in the activity (simply owning a company is not enough); is self-employed, not in an employment or service relationship; has reached the beginning of the calendar month after their 18th birthday and is below the age end for their birth year; the qualifying self-employment has lasted at least four months without interruption; they live in Finland, or live in another EU country while working as self-employed in Finland (the EU Regulation or a social security agreement can displace this); and 2026 annual confirmed income is at least €9,423.09. Self-employment carried on alongside a job, or seasonally, is covered if it meets these conditions: the employment does not remove the YEL obligation, and TyEL for the job and YEL for the business run side by side. Voluntary pension insurance does not replace YEL. The obligation ends at 68 for people born in 1957 or earlier, 69 for 1958–1961, and 70 for 1962 or later, and it ends at the end of the calendar month in which the person reaches that age.

The lower age boundary follows YEL Act section 4(1)(1): turning 18 during a month does not start coverage that day. [YEL Act, section 4](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

The 2026 upper confirmed-income limit is €214,000. A kiosk operated for three months each year can still require YEL where the seasonal activity continues year to year and the other conditions are met: the YEL policy is continuous and valid year round.

Pensioners: a person drawing an old-age or early old-age pension does not have to take out YEL; they may take it out voluntarily. A person drawing a partial old-age pension must keep valid YEL if the self-employment continues. Drawing a disability or unemployment pension does not remove the obligation.

By business form:

- Sole trader (with or without a business name): YEL if the conditions are met. Where both spouses work in the business and it is registered in one spouse's name, both spouses are insured under YEL. For a spouse who is not paid, ETK states the test: the spouse works in the company, has split earnings in taxation, and meets the other YEL conditions. Another unpaid family member working in the business is also self-employed under YEL; a paid family member other than the spouse is insured under TyEL.
- General partnership: each partner who works in the company needs YEL. Limited partnership: the active (responsible) partner who works in it needs YEL; a silent partner is not YEL-insured (TyEL if paid).
- Oy: a shareholder in a senior position needs YEL only where they hold more than 30% alone or more than 50% with family members, of the shares or the votes, directly or through an intermediary company. A shareholder who does not work in the company is not insured. The same more than 30% / more than 50% test applies to a cooperative member in a leadership position.

A light entrepreneur using an invoicing service is, as a rule, self-employed and needs YEL if the work is not totally random and the work input reaches the 2026 limit. The worker can still be in an employment relationship with the ordering party; an employee belongs in TyEL. Refer multi-country, MYEL, grant, disputed family-work and disputed-status facts; in unclear cases the Finnish Centre for Pensions decides.

## 3. Confirmed income and review controls

Confirmed income is the annual value of the work performed, broadly the wage for an equally qualified outsider. Set the value at an annual level even where the business begins part-way through the year; do not prorate the confirmed-income assessment for a midyear start. The provider uses the common calculation service. It considers field median wage, turnover, the value and amount of work, business scope and professional skills. The resulting recommendation has ±30% leeway. Turnover is an input to the recommendation; it is not the determinant of confirmed income.

Record the recommendation, its inputs and the work evidence. Explain any departure with substantiated part-time, hours, staffing, unusual-work, pay or other work-input facts. Do not mechanically choose either leeway boundary. Aggregate work input across companies; one policy can cover it. The provider makes the appealable confirmed-income decision.

The 2023 reform: providers review YEL income every three years. For income confirmed before the reform, its first two review increases are capped at €4,000 each without the entrepreneur's consent to a higher increase. From 2026 the transition also caps the first review before 1 January 2029 for income first confirmed to start during 2023–2025. A higher increase is permitted with the entrepreneur's consent. The cap is neither annual nor an automatic increase. Record the qualifying history, notice, evidence, consent and decision. [YEL Act, commencement provisions for Acts 1157/2022 and 1400/2025](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

At the beginning of each year, the provider adjusts confirmed income using the wage coefficient under section 89. Contact the provider when business operations change. Ordinary income changes are not retrospective; section 112a provides a disability-pension exception, which requires separate review. This differs from late policy arrangement, which can cover the current and three preceding years. The statute's base-year monetary figures are not automatically the 2026 indexed amounts. [YEL Act, sections 89 and 112a](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

## The method, step by step

1. Collect the eligibility, ownership, work-input, country, history and payer evidence.
2. Test the ordinary eligibility conditions, the business-form test and any pension being drawn; refer an international or disputed-status case.
3. Obtain and evidence the provider calculation-service recommendation, then retain the confirmed-income decision.
4. Choose a provider, arrange the policy, calculate the stated contribution and preserve its terms.
5. Route the deduction by payer (once only), flag the health insurance contributions and the unemployment-fund conditions, preserve paid-contribution evidence and retain review/late-arrangement records.

## 4. Arrange and calculate

Choose an earnings-related pension insurance company, or where eligible an industry pension fund. Obtain its current quote and preserve the provider, policy effective date, payment-frequency choice and terms. Do not use a universal instalment date, late-interest rate or payment plan.

Arrange YEL within six months of starting qualifying self-employment. Section 109 sets that deadline; section 143 authorises ETK compulsory insurance after an uncorrected notice, limited to the current and three preceding calendar years. Section 122 provides a neglect-fee ceiling equal to the neglected-period contribution, with statutory discretion/waiver conditions: the State Treasury decides on the provider's application. Section 115 excludes compulsory-insurance cases from the startup reduction. Do not calculate a fee or infer the maximum is automatic. Provider invoice terms remain separate. [YEL Act, sections 109, 115, 122 and 143](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

For 2026:

    annual standard contribution = confirmed income × 24.40%
    monthly equivalent = annual standard contribution ÷ 12

A newly self-employed person whose self-employment began on or after 1 January 2013 receives a 22% reduction for the initial 48 months, whatever their age. If the first self-employment period is shorter than 48 months, the unused months can be used in a second period; ask the provider to apply them. All self-employment periods beginning in 2001 or later count in calculating the period. Confirm the history with the provider before applying it. Exception flagged above: no reduction where ETK has insured the person compulsorily.

Planned change: ETK reports that the government intends a YEL reform from the start of 2028 under which the start-up reduction would be dropped. It is not the law for 2026; recheck before relying on the reduction for periods from 2028.

Contribution flexibility is temporary: an increase of 10–100% or reduction of 10–20% can apply under the provider’s current route. The person must notify the provider, the change is valid for one year at a time, and the restrictions on reducing are stricter than on increasing. It does not change confirmed income and does not change Kela benefits. Retain the provider confirmation and terms. Pensionable earnings follow contributions actually paid where flexibility, partial payment, non-payment or expiry applies; if a whole year's contributions are left unpaid, that year's earnings count as zero.

## 5. Tax and pension routing

YEL contributions are fully deductible. If the company pays, deduct them as a company expense. A sole trader who pays personally chooses one route for the tax year: the business tax return (Form 5) as a business expense, their own pre-completed personal return, or their spouse's pre-completed return (Other deductions, YEL or MYEL contributions line). If the contributions are booked as expenses in the business accounts but claimed on a personal or spouse's return, add them back on Form 5 under Other non-deductible expenses so the deduction is not claimed twice. Preserve payer and payment evidence before preparing the return.

For 2026, pension accrues at 1.5% of annual confirmed income for every age group. Ordinarily:

    annual pension accrual = annual confirmed income × 1.5%

The provider record controls actual accrual where flexibility or unpaid contributions applies.

## 5a. Health insurance and unemployment security

**Health insurance contributions (2026).** Confirmed YEL income is relevant to both insured-person contributions. For health care, it replaces the relevant business income and own-company wages; other earned income not replaced remains in the base. Do not charge health care on both the replaced income and YEL income. The daily allowance contribution uses wage income and YEL/MYEL income, with the YEL-specific supplement applied to YEL income. [Vero prepayment bases](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/how-is-the-current-years-total-of-prepayments-calculated/); [Vero insurance-related data, section 3.4](https://www.vero.fi/en/incomes-register/companies-and-organisations/detailed-guidance/64633/reporting-data-to-the-incomes-register-insurance-related-data10/)

For 2026, Vero lists 1.10% health care on wage/work income and, for self-employed persons aged 16–67, daily allowance of 1.11% at annual income of at least €17,255 or 0.23% below it. Apply the correct substituted base and other-income rules before using those rates; this is not a complete mixed-income assessment formula. These insured-person contributions are collected through income taxation, separately from the pension provider's invoice. The employer health contribution on actual own-company wages is a separate employer liability. Reconcile the person's tax card/assessment. [Vero tax bases](https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/tax-bases/); [Vero health insurance contribution](https://www.vero.fi/en/incomes-register/companies-and-organisations/employers/earnings-payment-data/employers-are-obliged-to-insure-their-employees/health-insurance-contribution/)

**Kela benefits.** Kela's sickness allowance and daily allowances for parents use the YEL confirmed income for the 12-month reference period before the calendar month preceding the start of the allowance, averaged if it changed. Wage income from the person's own company and business income are not included. If the person is both self-employed and in paid employment outside their own business, both income sources are used. Contribution flexibility does not change these benefits. Refer the exact benefit amount to Kela.

**Unemployment security.** The earnings-related daily allowance for the self-employed requires all of: self-employment for at least 15 months within the 48 months before unemployment; membership of the Entrepreneur Fund (the unemployment fund for entrepreneurs) over the same time; and YEL confirmed income higher than the annually set limit, €15,481 in 2026 (Työeläke.fi's YEL income page and the ETK booklet word this as at least €15,481; treat income exactly at the limit as a point to confirm with the Entrepreneur Fund). As a rule the business must end first. A person who is not a fund member can get only the general benefit paid by Kela. Meeting the €15,481 figure alone does not establish entitlement.

## 6. Worked checks

**Below threshold:** documented annual work input below €9,423.09 means ordinary mandatory YEL does not arise on these facts. Recheck if scope or hours change.

**Ordinary contribution:** confirmed income of €30,000 gives €30,000 × 24.40% = €7,320 annual standard contribution and €7,320 ÷ 12 = €610 monthly equivalent. The monthly amount is mathematical, not an invoice schedule.

**New entrepreneur:** if the €30,000 case is eligible for the 22% reduction, €7,320 × 78% = €5,709.60. Confirm history before relying on the result.

**Review cap:** insurance began in 2023, so its first three-year review falls in 2026. That start year is within the 2023–2025 extension, so the €4,000 increase cap applies at this first review. Insurance begun in 2024 reaches its first three-year review later. Retain the review notice and evidence; no increase is automatic.

**Late arrangement:** check actual work dates. The person may arrange insurance for the current and three prior years; after unheeded ETK admonition, ETK can arrange it at the person's expense. Late insurance can also bring a neglect fee set by the State Treasury, and compulsory insurance by ETK removes the start-up reduction (YEL sections 115, 122 and 143; confirm with the provider). Obtain actual provider terms rather than calculating a fee.

**Recurring seasonal kiosk:** a kiosk operates for three months each year. Because the activity continues year to year, test the other YEL gates and, if they are met, arrange continuous year-round YEL rather than treating each season as an isolated three-month activity.

**Retired sole trader:** a person born in 1960 draws an old-age pension and keeps trading with work input above €9,423.09. YEL is not mandatory; it may be taken out voluntarily. If the pension were a partial old-age pension instead, YEL would be mandatory while the self-employment continues.

**Unpaid spouse:** a sole trader's spouse works in the business without pay and has split earnings in taxation. If the other YEL conditions are met on the spouse's own work input, the spouse needs YEL; do not treat them as uninsured. A paid spouse working in the business is also insured under YEL, not TyEL.

**Side business:** an employee with a full-time job also runs a sole-trader business whose work input is above €9,423.09 for more than four uninterrupted months. The job's TyEL cover does not remove the obligation: YEL is needed for the business.

**Deduction route:** a sole trader books 2026 YEL contributions as a business expense but wants the deduction on the spouse's return. Claim them on the spouse's return and add them back on Form 5 as Other non-deductible expenses; never claim both.

**Midyear start:** a qualifying business begins in July. Estimate confirmed income as the annual value of the work using the outsider-wage/work-input method; do not halve that assessment solely because the start date is midyear. The provider’s decision and actual policy-period terms control.

**Changed business:** the provider has indexed confirmed income at the start of the year, then the business operations materially change. Give the change facts to the provider and obtain its new decision; ordinary changes are prospective. The disability-pension exception in section 112a needs separate review before ruling out a retrospective change. A late-policy arrangement is a different rule. [YEL Act, section 112a](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

### Review-cap arithmetic with no consent to exceed it

Assume current indexed confirmed income of EUR 20,000, a proposed review result of EUR 27,000, verified eligibility for the EUR 4,000 transition cap and no consent to a higher increase. The capped result is EUR 24,000. Annual indexation, different review histories, consent and disability cases are separate; the calculation does not establish the correct work-input value.

```oa-check
name: Finland assumed eligible YEL review cap without higher consent
inputs:
  current_indexed_income: 20000
  proposed_review_income: 27000
  established_transition_cap: 4000
steps:
  proposed_increase: proposed_review_income - current_indexed_income
  capped_increase: min(proposed_increase, established_transition_cap)
  capped_review_income: current_indexed_income + capped_increase
expected:
  proposed_increase: 7000
  capped_increase: 4000
  capped_review_income: 24000
```

## Executable contribution examples

The standard rate and new-entrepreneur reduction below were rechecked against [ETK's self-employed page](https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/self-employed/) on 23 October 2026. The independent source review and its selected verification limits are recorded in the [country README](README.md#evidence-and-next-action); remaining specialist and named accountant review are separate. These controls reproduce existing illustrative amounts; they do not establish eligibility or insurer billing terms.

### Standard full-year contribution

Assume EUR 30,000 confirmed income and ordinary full-year liability, without flexibility or other adjustments. The monthly equivalent is arithmetic, not a provider payment schedule.

```oa-check
name: Finland 2026 assumed standard YEL contribution
inputs:
  confirmed_annual_income: 30000
  contribution_rate: 0.244
  months: 12
steps:
  annual_contribution: confirmed_annual_income * contribution_rate
  monthly_equivalent: annual_contribution / months
expected:
  annual_contribution: 7320
  monthly_equivalent: 610
```

### Confirmed new-entrepreneur reduction

Assume the same base and confirmed entitlement to the 22% reduction for the full period. An insurer must establish that entitlement separately.

```oa-check
name: Finland assumed eligible YEL startup reduction
inputs:
  confirmed_annual_income: 30000
  contribution_rate: 0.244
  eligible_reduction: 0.22
steps:
  standard_contribution: confirmed_annual_income * contribution_rate
  contribution_after_reduction: standard_contribution * (1 - eligible_reduction)
expected:
  standard_contribution: 7320
  contribution_after_reduction: 5709.60
```

## When to refuse or refer

- Multi-country work, A1 and applicable-country decisions.
- Disputed employment, MYEL, grant and public-sector coverage.
- Retirement, disability or unemployment-pension facts.
- Provider invoice, payment-plan and late-charge terms.
- Exact benefit amount and Entrepreneur Fund eligibility decisions.
- The amount of any neglect fee: the State Treasury decides it on the provider's application; do not calculate it.

## Sources

Direct statutory check, 23 October 2026: [Self-Employed Persons' Pensions Act 1272/2006](https://www.finlex.fi/fi/lainsaadanto/2006/1272), sections 4, 89, 109, 112–112a, 114–115, 122 and 143, plus the displayed review-transition provisions. Official HTML statutory text was extracted after the browser reader proved incomplete; hashes are in the country research record. This closes selected statutory gaps, not every annual decree, social-benefit rule or exception in the earlier operational draft. Named Finnish accountant review remains open; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action).

- [Finnish Centre for Pensions: FAQs on YEL insurance](https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/faqs-on-yel-insurance/)
- [Finnish Centre for Pensions: self-employed](https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/self-employed/)
- [Finnish Centre for Pensions: pension insurance of the self-employed, 2026 booklet (PDF)](https://www.etk.fi/wp-content/uploads/2026/02/pension-insurance-of-the-self-employed.pdf)
- [Finnish Centre for Pensions: 2026 pension changes](https://www.etk.fi/en/topical-issues/how-earnings-related-pensions-will-change-in-2026/)
- [Työeläke.fi: what is YEL income?](https://www.tyoelake.fi/en/pensions-for-the-self-employed/what-is-yel-income/)
- [Työeläke.fi: insure your self-employment](https://www.tyoelake.fi/en/pensions-for-the-self-employed/insure-your-self-employment/)
- [Työeläke.fi: when do I need insurance?](https://www.tyoelake.fi/en/pensions-for-the-self-employed/when-do-i-need-insurance/)
- [Työeläke.fi: pension amount and contributions](https://www.tyoelake.fi/en/pensions-for-the-self-employed/pension-amount-and-contributions/)
- [Työeläke.fi: social security of the self-employed](https://www.tyoelake.fi/en/pensions-for-the-self-employed/social-security-of-the-self-employed-based-on-confirmed-income/)
- [Työeläke.fi: the Finnish Centre for Pensions supervises](https://www.tyoelake.fi/en/pensions-for-the-self-employed/the-finnish-centre-for-pensions-supervises/)
- [Vero: pension premiums (YEL)](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/pension-premiums-yel/)
- [Vero: prepayment bases, YEL/MYEL subsection](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/how-is-the-current-years-total-of-prepayments-calculated/), read 23 October 2026
- [Vero: insurance-related data, section 3.4](https://www.vero.fi/en/incomes-register/companies-and-organisations/detailed-guidance/64633/reporting-data-to-the-incomes-register-insurance-related-data10/), effective 1 January 2026; read 23 October 2026
- [Vero: tax bases for 2026](https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/tax-bases/)
- [Vero: health insurance contribution (Incomes Register)](https://www.vero.fi/en/incomes-register/companies-and-organisations/employers/earnings-payment-data/employers-are-obliged-to-insure-their-employees/health-insurance-contribution/)

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
