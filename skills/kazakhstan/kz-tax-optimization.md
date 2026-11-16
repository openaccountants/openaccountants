---
name: kz-tax-optimization
description: "Kazakhstan 2026 lawful regime comparisons: conditional income-tax break-even, VAT, payroll adjustment, customer deductions and Astana Hub eligibility."
version: 1.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: tax

type: decision
---

# Kazakhstan lawful regime comparisons v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Legal planning for Kazakhstan ИП and small businesses choosing between eligible simplified and general taxation, with separate VAT, liability and Astana Hub questions. This is a comparison of documented facts and lawful elections, not advice to conceal turnover, split businesses artificially or disguise employment. General-regime profit and simplified statutory income are different bases.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Simplified versus general rate inputs | Use current eligible local rate from kz-simplified-regime and the applicable income band from kz-income-tax; do not assume every taxpayer gets the national default | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Simplified base and payroll adjustment | Art. 724 contains a specific employee-income-cost adjustment after the cumulative-income trigger; “no costs ever” is incomplete | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Customer-side consequence | General-regime buyer expenses from simplified suppliers are restricted under art. 286(16); B2B itself is not prohibited | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| VAT and regime | Special-regime taxpayers cannot have ordinary registered-VAT status (art. 99); general-regime registration uses its own turnover test | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Astana Hub eligibility | Art. 17 registered legal entity, at least 90% priority ICT income, including specifically associated income counted under art. 17, and own-production conditions where relevant; simplified participation excluded by art. 723 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Compute both lawful candidates with the same projected transactions and period. For simplified, establish all eligibility/ownership/activity conditions, actual maslikhat rate and any payroll adjustment. For general taxation, substantiate deductions, loss history and the correct annual band. Compare income tax, own social payments, employee costs, VAT pricing/recovery, administration, liability and customer-side deductibility; do not call an income-tax-only result an overall optimum.

When the confirmed simplified rate is 4% and the general profit is entirely within its 10% band, with no special adjustments, equal income tax occurs at a 40% margin, derived from 4%/10%. Above that margin simplified income tax is lower; below it general income tax is lower. This is conditional arithmetic, not a universal legal break-even. Rates, payroll adjustment, VAT, progressive-band exposure and customer effects change it.

Forecast income against the actual eligible regime ceiling and the distinct general-regime VAT test using `kz-simplified-regime` and `kazakhstan-vat`. The test is not generically a rolling period, and special-regime crossing of the general VAT threshold alone does not create ordinary registration. Actual regime eligibility failure and transition dates still matter. Never advise suppressing required registration or moving invoices artificially to avoid it.

For an IT contractor, screen actual entity/participant/activity conditions under art. 17 and the separate benefits under arts. 738 onward. A freelance ИП does not automatically become an Astana Hub participant. Do not claim accreditation, blanket CIT/ИПН/VAT/payroll exemption or guaranteed savings. Evaluate lawful contribution choices under `kz-social-contributions`; minimums/caps and actual-income bounds do not permit invented income. Review genuine employee-versus-contractor facts rather than an invoice label.

## Deadlines and filing

Document the assumptions, source each elected rate and regime, record valid notification/effective dates and compare the lawful cases before acting. Filing, payment, VAT transition and company/accounting setup use their dedicated skills; the planning comparison is not a filed return or a retrospective election.

## Penalties and interest

No penalty saving is assumed. Artificial turnover splitting, disguised employment, concealed receipts and skipped mandatory registration are refusal cases. Keep the actual facts for a professional assessment.

## Cross-border points

Non-residence, branches, related ownership, foreign clients/suppliers, treaty relief and regulated activities need specific analysis. Legal-entity distributions and Astana Hub benefits cannot be reduced to the ordinary ИП comparison.

## Two worked examples that recompute

Case 1: preserved designer persona, hypothetical income KZT 15,000,000 and 80% documented margin, confirmed eligible 4% simplified rate and general lower-band 10%. Simplified income tax KZT 600,000 versus general KZT 1,200,000; simplified saves KZT 600,000 before other effects.

```oa-check
name: Designer income-tax decision
inputs:
  income: 15000000
  margin: 0.8
steps:
  - profit: income * margin
  - simplified: income * 0.04
  - general: profit * 0.10
  - simplified_saving: general - simplified
expected:
  profit: 12000000
  simplified: 600000
  general: 1200000
  simplified_saving: 600000
```

Case 2: preserved reseller persona, hypothetical income KZT 40,000,000 and 15% documented margin under the same conditional rates. Simplified income tax KZT 1,600,000 versus general KZT 600,000; general saves KZT 1,000,000 before other costs and VAT/customer effects. The IT-contractor persona separately requires the Astana Hub eligibility screen.

```oa-check
name: Reseller income-tax decision
inputs:
  income: 40000000
  margin: 0.15
steps:
  - profit: income * margin
  - simplified: income * 0.04
  - general: profit * 0.10
  - general_saving: simplified - general
expected:
  profit: 6000000
  simplified: 1600000
  general: 600000
  general_saving: 1000000
```

## Ask the client first

- Current/projected income, actual costs and documentary evidence?
- Legal form, residence, activity, ownership and eligible regimes/local rates?
- Staff, payroll-cost adjustment and contribution exemptions?
- VAT status, imports, customer type and pricing/deduction effects?
- For IT: actual legal entity, participant registration and qualifying income?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 17, 99–101, 286(16), 363, 716, 723–726, 738 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |

Not yet confirmed: Taxpayer-specific enacted local rate, precise Astana Hub qualification/benefit computation, full employment-law classification and current portal election implementation. The old blanket 40% break-even and rolling-VAT-test shortcuts are now expressly conditional/corrected.
