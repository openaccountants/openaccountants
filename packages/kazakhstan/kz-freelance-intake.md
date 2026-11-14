---
name: kz-freelance-intake
description: "Kazakhstan 2026 freelance intake: reconcile source documents, residence, regime, income classification and evidence before computation."
version: 0.2
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
tier: 2
domain: tax

type: router
---

# Kazakhstan self-employed intake v0.2

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Scope

Entry point for Kazakhstan-resident self-employed individuals/ИП, not a corporate return preparer. It establishes facts and routes to the correct current job. Respond in the user’s language and retain ИП/жеке кәсіпкер, ТОО, упрощённая декларация/оңайлатылған декларация and общеустановленный режим/жалпыға бірдей режим. Patent/патент and retail tax/розничный налог are historical documents to reconcile, not 2026 routes.

## Ask the client first

- Individual/ИП or ТОО, residence and period?
- Current registration/notification and actual activity code, employees and ownership?
- Bank receipts, primary documents, prior returns and app/platform history?
- VAT status, imports/foreign suppliers, income pattern and any regime breach?

Parse uploaded records before gap questions. Confirm the complete inferred picture once. Do not re-ask visible facts or narrate internal phases. Unknown residence, regime, turnover or VAT status stays unresolved; do not assume the former “resident, simplified, below threshold, not VAT registered” package.

## The method, step by step

1. For ТОО, non-residence or a complex foreign/ownership case, stop this individual workflow and refer. For an individual, establish whether they are registered ИП or eligible for the distinct non-ИП self-employed regime.
2. Read the registration extract, accepted notifications and tax-cabinet status. Load `kz-simplified-regime` for the permitted 2026 regimes, eligibility ceilings, local rate and transition rules. A historical Form 911.00/patent receipt, retail-tax record or old Form 910.00 does not establish a valid current election; art. 840 controls transition. Current general-regime ИП income routes to `kz-income-tax`; no old patent/retail branch remains.
3. Collect all Kaspi/Halyk and other bank/account records in KZT/RUB/USD/EUR, primary sales/cost documents, prior Forms 910.00, 911.00, 220.00 and 300.00 where relevant, and social-payment histories. Accept partial uploads; record gaps. Separate business receipts from own-account transfers, loans and personal funds; do not equate all bank credits with taxable income. Reconcile income recognition under the selected regime.
4. For an ИП lawfully exempt from accounting, foreign-currency operations are translated at the official rate on the operation date under art. 220; do not use a presumed annual average or receipt-date rule for every accounting taxpayer. Preserve original currency, dates and rate evidence.
5. Check annual/monthly income and each transaction against the exact applicable special-regime condition in `kz-simplified-regime`. Resolve VAT registration under `kazakhstan-vat` separately. In 2026 special-regime status excludes ordinary VAT registration (art. 99), though import/non-resident VAT exceptions remain. An apparent simplified-plus-VAT combination requires reconciliation rather than automatic continuation of both.
6. If a condition fails, record the actual breach date/transaction and use art. 716 transition rules from `kz-simplified-regime`; do not split the year mechanically into “before/after” without the legal effective date.
7. Pass a structured package to the income-regime skill, `kz-social-contributions`, `kazakhstan-vat` where applicable, then `kz-return-assembly`. Include entity/status, period, activity/ownership/staff, regime evidence, reconciled income, VAT analysis, social-payment status, missing records and every assumption.

## Worked cases

Case 1: hypothetical bank credits KZT 12,000,000 include KZT 2,000,000 own-account transfers and KZT 1,000,000 documented loan proceeds. Potential business receipts are KZT 9,000,000 before regime-specific recognition. The routing input is reconciled receipts, not all credits.

```oa-check
name: Intake receipt reconciliation
inputs:
  credits: 12000000
  transfers: 2000000
  loans: 1000000
steps:
  - receipts: credits - transfers - loans
expected:
  receipts: 9000000
```

Case 2: hypothetical foreign service receipt is USD 1,000, official operation-date rate KZT 500/USD and a separate KZT 20,000 documented loan principal repayment credit. For the exempt-accounting ИП scope of art. 220, translated service receipt is KZT 500,000 and total bank credit KZT 520,000; route KZT 500,000 subject to recognition checks. The exchange rate is an example input, not a published rate.

```oa-check
name: Intake foreign-currency evidence
inputs:
  usd: 1000
  official_rate: 500
  loan_credit: 20000
steps:
  - service_receipt: usd * official_rate
  - bank_credit: service_receipt + loan_credit
expected:
  service_receipt: 500000
  bank_credit: 520000
```

## When to refuse or refer

Do not compute tax, invent rates/ceilings, infer an election solely from old forms, file, or resolve corporate/non-resident, farm, complex ownership or ambiguous transition facts automatically. A conservative workpaper flag can preserve missing information; it cannot turn an unknown eligibility condition into a fact.

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 99–101, 220, 715–727 and 840 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Unprovided taxpayer residence, actual election, activity, current form status, local rate or transaction evidence. Old patent/retail routes, 3% defaults, automatic low-turnover assumption and SNR-plus-VAT permission are superseded.
