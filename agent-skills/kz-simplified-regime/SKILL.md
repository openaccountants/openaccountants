---
name: kz-simplified-regime
description: "Kazakhstan 2026 simplified declaration and self-employed regimes: eligibility, income bases, local rates, payroll adjustment, transitions and deadlines."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-simplified-regime"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan special tax regimes v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Resident ИП and resident legal entities that satisfy all simplified-declaration conditions, and eligible natural persons using the separate self-employed regime. Reply in the user’s language while retaining ИП/ЖК, ТОО, СНР, МРП and the native regime names. For 2026 the special-regime list is self-employed, simplified declaration and peasant/farm households (art. 715); patent, retail tax and fixed-deduction are not current alternatives. Farming is outside this computation. General-regime income, VAT, social payments and corporate distributions route to their dedicated skills.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Simplified declaration eligibility | Annual income no more than 600,000 МРП, permitted activity and all art. 723 exclusions satisfied; no employee-number cap | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Simplified income-tax rate | 4% of the statutory base; maslikhat adjustment at most ±50%, giving 2%–6% derived bounds; confirm the enacted local rule (art. 726) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Self-employed eligibility | Kazakhstan citizen or қандас, not registered as ИП, no employees, permitted activity and income no more than 300 МРП in each month (art. 718) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Self-employed payment | 0% ИПН; 4% social payments comprising 1% each ОПВ, ОПВР, СО and ОСМС; not the ordinary ИП fixed contribution formula | https://www.gov.kz/org/minfin/documents/details/1030415?lang=ru |
| 2026 МРП | KZT 4,325, budget law art. 7; simplified ceiling KZT 2,595,000,000 and monthly self-employed ceiling KZT 1,297,500 are derived | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| Simplified payroll-cost adjustment | Eligible employee-income expenses reduce the base starting in the month cumulative income exceeds 24,000 МРП (art. 724); do not deduct all other business costs | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Simplified social tax and VAT | No social tax; no VAT-payer status, except import VAT and VAT for non-resident supplies (art. 722) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Test every exclusion in art. 723: corporate ownership above 25%; linked founders/participants using special regimes; an individual/ИП participating in a special-regime legal entity; non-profits; special/industrial-zone and Astana Hub participants; joint-activity contracts. Match the actual activity against the current prohibited list, not a generic “services allowed” assumption. The official regime FAQ identifies Government Resolution No. 970 of 14 November 2025 for simplified prohibited activities; the self-employed allowed list is a separate list. Do not treat a lack of staff as sufficient eligibility.

Simplified base is statutory income under art. 724, generally accrual, not simply the bank total. Include commissions under that article’s principal/agent rule, adjustments and non-sale income as applicable. An ИП lawfully exempt from accounting applies the special recognition rules in art. 725. Ordinary expenses are not deductible; the payroll-cost adjustment is a specific exception. Separate income subject to different valid maslikhat rates. The simplified payment is ИПН/КПН, not a 2025-style split into income tax and social tax. Own contributions and employee withholding remain separate. B2B supplies are permitted, but the general-regime buyer’s deduction restriction matters (art. 286(16)).

Self-employed receipts are recorded in e-Salyq Business, with app receipts and monthly income register (arts. 717–720). Internet-platform operators account for their covered payments under art. 721; exclude such income from duplicate self-assessment. The no-network exception uses a simple daily/monthly income record and the statutory payment-document route. Do not convert the monthly eligibility ceiling into a freely transferable annual allowance.

Transition: art. 840 required an eligible former special-regime taxpayer wishing to use simplified to notify before 1 March 2026. Former patent/mobile-app ИП without that notification were deregistered automatically on 1 March with effect from 1 January; this is not automatic commencement of the self-employed regime. That begins with the first qualifying app receipt, or the specified payment month in the no-network case. Other non-notifying taxpayers, except the listed transitional cases, defaulted to the general regime. For a later eligibility breach, art. 716 requires notice within 5 working days and makes the new regime effective on the date conditions fail. A transaction itself exceeding the ceiling requires notice before receiving its income. Do not use the old “next quarter” shortcut.

## Deadlines and filing

The simplified period is a half-year (art. 722). File the current simplified declaration in the taxpayer cabinet by the 15th of the second month after the half-year; pay by the 25th (art. 727). This corresponds to August after H1 and February after H2, subject to non-working-day rules. Use the current Form 910.00 package and retain receipt/acceptance, not an assumed old 910.01 line map. Employee withholding/reporting is separate (`kz-payroll`); ordinary monthly social payments remain separate (`kz-social-contributions`). Self-employed accounting/payment uses the app rather than a simplified half-year return. Ordinary monthly self-employed social-payment deadlines are the 25th of the following month under Social Code arts. 246 and 248; platform operators handle their covered receipts separately. Verify the app’s payment status and contribution allocations; do not assume app recording equals payment.

## Penalties and interest

Do not invent penalties for late election, turnover breach, late return or payment. A failed eligibility condition changes the applicable regime and can create VAT and accounting obligations; preserve the exact breach date for review.

## Cross-border points

Special-regime eligibility requires the specified resident/status conditions. Non-residents, branches, foreign-source complications, LLP distributions and treaty relief require specialist review. Special-regime VAT exceptions for imports and non-resident services remain obligations even though ordinary VAT registration is unavailable.

## Two worked examples that recompute

Case 1: Aigerim has hypothetical H1 income of KZT 9,000,000, no payroll adjustment, permitted web-design activity and a confirmed 4% local rate. Tax is KZT 360,000. If a valid maslikhat decision instead makes her activity’s rate 2%, tax is KZT 180,000; evidence of that decision is indispensable. This preserves both earlier Aigerim cases without inventing an actual local decision.

```oa-check
name: Aigerim confirmed local rate comparison
inputs:
  income: 9000000
steps:
  - national_tax: income * 0.04
  - valid_reduced_tax: income * 0.02
  - difference: national_tax - valid_reduced_tax
expected:
  national_tax: 360000
  valid_reduced_tax: 180000
  difference: 180000
```

Case 2: Daniyar’s hypothetical tutoring receipts are KZT 400,000 in a qualifying self-employed month after valid entry into that regime. Social payments are KZT 16,000, with KZT 4,000 for each component and no ИПН. His former patent status alone does not prove entry.

```oa-check
name: Daniyar app social-payment split
inputs:
  income: 400000
steps:
  - pension: income * 0.01
  - employer_pension: income * 0.01
  - social: income * 0.01
  - health: income * 0.01
  - total: pension + employer_pension + social + health
expected:
  total: 16000
  pension: 4000
  employer_pension: 4000
  social: 4000
  health: 4000
```

Case 3: Marat projects hypothetical H1 receipts of KZT 1,400,000,000 and H2 KZT 1,300,000,000. At the 2026 МРП, the annual ceiling is KZT 2,595,000,000; projected excess is KZT 105,000,000. Locate the actual breach transaction and notify under art. 716 rather than splitting annual totals arbitrarily.

```oa-check
name: Marat projected eligibility breach
inputs:
  h1: 1400000000
  h2: 1300000000
  mrp: 4325
steps:
  - ceiling: 600000 * mrp
  - excess: max(h1 + h2 - ceiling, 0)
expected:
  ceiling: 2595000000
  excess: 105000000
```

## Ask the client first

- Registration, residence/citizenship/қандас status and exact current regime?
- Actual activity, ownership/related participants and applicable allowed/prohibited list?
- Income by month and transaction, accounting status and employee-income costs?
- Staff, app/platform receipts and contribution history?
- Enacted local rate and filed notification/acceptance dates?
- Imports, foreign suppliers, VAT registration history and any eligibility breach?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 715–727, 840, 99 and 286(16) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |
| Read for self-employed contribution split and app/platform/no-network exceptions, questions 80–92 | https://www.gov.kz/org/minfin/documents/details/1030415?lang=ru | 2026-11-14 |
| Read for bookkeeping exemption and prohibited-list identification, questions 1–6 | https://www.gov.kz/situations/814/1716?lang=ru | 2026-11-14 |

Not yet confirmed: Specific local maslikhat rates; complete current permitted/prohibited-activity classification; exact 2026 electronic appendix/box mapping; liquidation, farm-household and LLP distribution computations. The old patent/retail/fixed-deduction rates, old staff cap and automatic self-employed migration are superseded historical topics, not available 2026 instructions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-simplified-regime` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-simplified-regime. If neither is available, confirm every figure against the official source pages cited above before relying on it.
