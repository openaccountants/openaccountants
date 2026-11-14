---
name: kz-return-assembly
description: "Kazakhstan 2026 return assembly: reconcile records and calculations, select current forms, document unresolved items and retain submission evidence."
version: 0.2
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
depends_on:
  - kz-freelance-intake
tier: 2
domain: tax

type: router
---

# Kazakhstan return assembly v0.2

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Scope

Assembly of a Kazakhstan-resident ИП draft filing package after the upstream computations have been reviewed. It sequences forms and evidence; it does not recalculate income tax, VAT or contributions. Load `kz-freelance-intake` first. The output is a filing checklist and working papers for a qualified accountant, not an assertion that filing occurred.

## Ask the client first

- Accepted current regime/transition dates and taxpayer identity?
- Reviewed income, social-payment, payroll and VAT computations?
- Actual reporting periods, prior returns, balances and payment evidence?
- Current cabinet form/version and authority acceptance messages?
- Missing evidence, exemptions, extensions or unresolved questions?

## The method, step by step

1. Reconcile the intake package to registration and regime evidence. Route simplified to `kz-simplified-regime`, general-regime ИП to `kz-income-tax`, and eligible non-ИП self-employed cases to the app workflow rather than a Form 910.00 assumption.
2. Assemble the current income declaration: Form 910.00 for the simplified half-year job; Form 220.00 for general-regime ИП annual business income. The controlling periods/deadlines are arts. 722/727 and 420–421; load their owning skills for the actual calculation/calendar. Forms named here are job identifiers, not a certified current electronic box map.
3. Add the `kz-social-contributions` schedules and any `kz-payroll` withholding/quarterly Form 200.00 job. Contribution payment schedules remain separate from return deadlines. Confirm regime-specific reporting rather than assuming absence of staff removes every social-reporting obligation.
4. Add `kazakhstan-vat` and Form 300.00 only where required; imports/non-resident VAT can remain relevant without ordinary registration. Do not combine simplified status with ordinary registered-VAT status without resolving the contradiction.
5. Cross-check income across forms, contribution bases/caps and any payroll-cost adjustment. Keep prior credits, payments and amendments distinct from current-period liability. Stop if totals do not reconcile.
6. In the current taxpayer cabinet/e-Salyq channel, select the period and actual form version, transfer the reviewed values, check validation and obtain human authorization/signature for submission. Retain accepted declaration identifier/status, date, payment reference and fund allocations; an upload screen alone is not acceptance. Check amendments and outstanding notices.
7. Deliver the checklist: regime/status confirmed; eligible income within ceiling; correct income/social/payroll/VAT jobs; contribution caps/exemptions; forms/periods; statutory filing and payment dates from owning skills; accepted submissions and reconciled payments; unresolved items and accountant sign-off.

## Worked cases

Case 1: hypothetical reviewed income tax is KZT 360,000 and separately reviewed social payments KZT 130,050; payments already made against those jobs are KZT 300,000 and KZT 130,050 respectively. Outstanding income tax is KZT 60,000 and social balance is 0. Do not offset fund payments against income tax without a legal transfer.

```oa-check
name: Separate tax and fund ledgers
inputs:
  income_tax: 360000
  social: 130050
  income_paid: 300000
  social_paid: 130050
steps:
  - income_balance: income_tax - income_paid
  - social_balance: social - social_paid
  - outstanding: income_balance + social_balance
expected:
  income_balance: 60000
  social_balance: 0
  outstanding: 60000
```

Case 2: hypothetical VAT output KZT 800,000 and eligible input KZT 500,000 produce KZT 300,000 current net liability; an independently validated earlier credit KZT 100,000 leaves KZT 200,000. An unconfirmed prior credit must be excluded from the payment instruction until reconciled.

```oa-check
name: VAT balance assembly control
inputs:
  output: 800000
  eligible_input: 500000
  confirmed_credit: 100000
steps:
  - current_net: output - eligible_input
  - balance: current_net - confirmed_credit
expected:
  current_net: 300000
  balance: 200000
```

## When to refuse or refer

Refuse to mark the package filed-ready if regime, period, form, acceptance, balances or legal scope is unresolved. Do not file/sign on the user’s behalf in this workflow, invent electronic form fields, use the old flat general-regime rate shortcut or treat all deadlines as the same. Corporate, non-resident, liquidation or other specialist cases require a different package.

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 99, 420–421, 444–445, 504–506, 722–727 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Current portal fields/appendix versions and case-specific filing/payment dates until confirmed in the owning skill and accepted form. The old tentative calendar and flat general-regime shorthand are not reused.
