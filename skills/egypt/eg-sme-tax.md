---
name: eg-sme-tax
description: Use this skill whenever asked about Egypt's simplified or SME tax regime for small self-employed people, freelancers, professionals, sole proprietors, and small companies. Trigger on phrases like "Egypt simplified tax", "SME tax Egypt", "small business tax Egypt", "Law 6 of 2025 Egypt", "turnover tax Egypt", "freelancer simplified Egypt", "النظام الضريبي المبسط", "ضريبة على رقم الأعمال", "قانون 6 لسنة 2025", "حوافز المشروعات الصغيرة". Covers the integrated simplified tax regime under Law No. 6 of 2025 for businesses and professionals with annual turnover up to EGP 20 million, and routes unresolved Law 152 of 2020 classification questions to an accountant. AI replies in the user's language (English or Arabic).
version: 1.4
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Egypt SME turnover tax: 2026

> **General reference only.** This Guide has not been reviewed for a particular taxpayer's facts. Have an Egyptian tax professional review the position before filing or paying.

Egypt's Law 6 of 2025 taxes eligible projects on annual turnover, including professional activities. These rules cover tax year 2026. Reply in English or Arabic to match the user. حجم الأعمال means turnover; مصلحة الضرائب المصرية means the Egyptian Tax Authority (ETA).

## Who this applies to

- The ordinary entry ceiling is annual turnover of **EGP 20,000,000 inclusive**. A project requests the regime whether or not it was already tax-registered when the law took effect on **1 March 2025** (Law 6, arts. 1 and 16).
- ETA's Services Guide, section 18/2, p. 251, says projects already subject to Law 152/2020 move directly without another request. Establish that prior status; do not assume every small business qualifies for this transition.
- File returns by their legal deadlines and join ETA's electronic systems, including e-invoice or e-receipt according to the applicable mandatory phases, issuing the required documents (art. 3).
- Professional consultancy is excluded when **at least 90%** of annual turnover comes from professional advice to **one or two persons**. The Finance Minister may except activities (art. 4). For a claimed exception: Check this point with one of our partner accountants.
- Improper entry is excluded, including splitting an existing activity without economic justification; ETA bears the burden of proof (art. 4). Do not help fragment a business to qualify.
- Determine turnover from the relevant art. 2 evidence: the last final assessment for projects registered when the law began; the last return for those registered but not assessed then; the return for a project registered afterwards; or e-invoice/e-receipt data. ETA describes the new registrant's declaration as expected first-year turnover (Services Guide p. 249).

## Rates, bands and thresholds

Apply **one rate to the whole annual turnover**, rather than marginal slices. Costs, depreciation and a trading loss do not reduce this turnover charge (art. 10).

| Annual turnover (EGP) | Rate on whole turnover | Official source |
|---|---|---|
| Below 500,000 | 0.4% | [Law 6 art. 10(1)](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) |
| 500,000 to below 2,000,000 | 0.5% | [Law 6 art. 10(2)](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) |
| 2,000,000 to below 3,000,000 | 0.75% | [Law 6 art. 10(3)](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) |
| 3,000,000 to below 10,000,000 | 1% | [Law 6 art. 10(4)](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) |
| 10,000,000 to 20,000,000 inclusive | 1.5% | [Law 6 art. 10(5)](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) |

Use actual turnover at a boundary. Do not round it up to a higher band. The statute's EGP 20 million ceiling governs over the EGP 25 million printed in the Services Guide rate table.

**Existing participants' growth tolerance:** during the five years from the benefit request, turnover may exceed EGP 20 million **once**, by **no more than 20%** (up to EGP 24 million inclusive), at 1.5%. Exceeding that percentage, or repeating the breach within that period, ends the benefit **from the following year** (art. 10). This is not an entry ceiling of EGP 24 million. For the tax computation in a disqualifying breach year: Check this point with one of our partner accountants.

**Withdrawal:** no withdrawal before five years beginning the day after the benefit request (art. 5). A request to leave after two years therefore fails this condition. For transferred Law 152 projects without a request date, including the audit clock: Check this point with one of our partner accountants.

## The base

| Topic | Rule for projects subject to Law 6 | Source |
|---|---|---|
| Development fee and stamp duty | Exempt. Notarisation/registration fee relief covers formation contracts, business credit and mortgage contracts and other financing guarantees; the stated tax and fee relief also covers land-registration contracts needed to establish the project | Art. 7 |
| Fixed assets | Gains on disposing of fixed assets, machinery or production equipment are exempt | Art. 8 |
| Dividends | Distributions of profits resulting from the project's activity are outside the dividend tax specified by income tax law | Art. 9 |
| Withholding and advances | Projects are outside the Law 91 deduction/advance-payment system. ETA explains this covers deductions from payments to the project and the project's deductions from payments to counterparties. Cross-border withholding needs separate review below | Art. 11; Services Guide p. 247 |
| Income-tax return | Separate annual return, at the ordinary statutory deadlines; Form 20 إقرارات. ETA states 1 January–31 March for natural persons and within four months after financial year-end for legal persons | Art. 12; Decision 420 art. 2; Services Guide p. 248 |
| VAT return | For a project with a VAT-return obligation, every three months, during the following month, with payment | Art. 12 |
| Payroll tax | Obligation under this provision is the annual tax-settlement return with payment | Art. 12 |
| Examination | Income-tax and VAT returns examined after five years from the benefit request; this is a deferral, not permanent exemption | Art. 12 |

Other applicable income-tax, VAT and unified-procedure rules continue where Law 6 has no special provision (art. 6). For VAT registration, standard/special rates and schedule-tax classification: Check this point with one of our partner accountants.

## Deadlines and filing

[Finance Minister Decision 420/2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf), arts. 1–3, specifies:

- Join online on **Form 10/1 طلبات**; withdrawal uses **Form 11/1 طلبات**, subject to the five-year rule above.
- The annual commercial, industrial or professional income-tax return is **Form 20 إقرارات**.
- Keep a **fixed-asset register** and **raw-materials stock register**; **daily sales**, **daily purchases** and **tax summary books**; and **e-invoices or e-receipts**, as applicable. Records may be electronic or paper. Simplified records remain obligatory; this is not permission to keep none (Law 6 art. 13).

Use ETA's electronic tax system for merged offices or [the ETA portal](https://eservice.incometax.gov.eg/etax) for other offices. Select نظام المحاسبة المبسط and Form 10/1, enter the sales figure in numbers and words and its turnover measure, then submit the data and representative's details (Services Guide p. 249). ETA's guide says request corrections are recorded with the tax office and signed by both parties (p. 252).

For new-business registration forms and deadlines, or mapping individual boxes of Form 20 or the older Form 111: Check this point with one of our partner accountants.

## Penalties and interest

Penalty amounts, late-payment charges or ceilings, and consequences of a compliance failure beyond the stated entry conditions: Check this point with one of our partner accountants.

## Cross-border points

Cross-border income, payments, residency or treaty interaction: Check this point with one of our partner accountants.

## Worked examples

All turnover-tax figures below assume valid participation, compliance with art. 3 and no art. 4 exclusion. They illustrate income tax only. Compare the full general-system position over the commitment period before electing; profit alone does not establish general-system taxable income or the taxpayer's legal form.

**Freelance software developer:** turnover EGP 1,500,000, costs EGP 150,000, profit EGP 1,350,000. Turnover tax = **EGP 7,500**.

**Consultancy:** turnover EGP 12,000,000, profit approximately EGP 4,000,000. Turnover tax = **EGP 180,000**, provided the consultancy exclusion does not apply. Exactly 90% from one client meets that exclusion unless an applicable ministerial exception is established.

```oa-check
name: Freelancer and consultancy turnover tax
inputs:
  freelance_turnover: 1500000
  freelance_costs: 150000
  consultancy_turnover: 12000000
  consultancy_profit: 4000000
steps:
  - freelance_profit: freelance_turnover - freelance_costs
  - freelance_tax: freelance_turnover * 0.005
  - consultancy_tax: consultancy_turnover * 0.015
expected:
  freelance_profit: 1350000
  freelance_tax: 7500
  consultancy_tax: 180000
```

**Low-margin reseller:** turnover EGP 9,000,000 and profit EGP 200,000 give a margin of approximately **2.2222%**, with turnover tax **EGP 90,000**. The separate original **2% margin** case at EGP 9,000,000 implies profit **EGP 180,000**. These are different cases. For their general-system liabilities and which regime wins: Check this point with one of our partner accountants.

```oa-check
name: Distinct reseller profit inputs
inputs:
  turnover: 9000000
  profit: 200000
  alternative_margin: 0.02
steps:
  - simplified: turnover * 0.01
  - margin_percent: profit / turnover * 100
  - alternative_profit: turnover * alternative_margin
expected:
  simplified: 90000
  margin_percent: 2.2222222222
  alternative_profit: 180000
```

**Growth:** a participant's first breach in year 3 at EGP 22,000,000 is **10%** over the ceiling, within the one-time tolerance: tax **EGP 330,000**. If next year's turnover is EGP 26,000,000 (**30%** over), participation ends from the following year. A second breach at EGP 25,000,000 likewise ends it from the following year; do not turn the following-year rule into an immediate exit.

**Micro freelancer:** turnover EGP 400,000, profit EGP 360,000; turnover tax **EGP 1,600**. For the VAT registration and general-system comparison in this case: Check this point with one of our partner accountants.

```oa-check
name: Growth and microbusiness cases
inputs:
  ceiling: 20000000
  year_three_turnover: 22000000
  next_year_turnover: 26000000
  second_breach_turnover: 25000000
  micro_turnover: 400000
  micro_profit: 360000
steps:
  - first_excess_percent: (year_three_turnover / ceiling - 1) * 100
  - first_breach_tax: year_three_turnover * 0.015
  - next_excess_percent: (next_year_turnover / ceiling - 1) * 100
  - second_excess_percent: (second_breach_turnover / ceiling - 1) * 100
  - micro_tax: micro_turnover * 0.004
expected:
  first_excess_percent: 10
  first_breach_tax: 330000
  next_excess_percent: 30
  second_excess_percent: 25
  micro_tax: 1600
```

Other original band checks, on the same eligibility assumptions: EGP 1,200,000 × 0.5% = **6,000**; EGP 2,500,000 × 0.75% = **18,750**; EGP 8,000,000 × 1% = **80,000**; EGP 15,000,000 × 1.5% = **225,000**.

## Cases requiring individual review

- Past liabilities, open assessments, amnesty/settlement, including Law 151/2026 art. 4 and its correction: Check this point with one of our partner accountants.
- Law 152/2020 MSME size classifications or other development incentives: Check this point with one of our partner accountants.
- Free zones, special economic zones, oil and gas, banking, insurance or other special-sector regimes: Check this point with one of our partner accountants.

## Ask the client first

Establish turnover and its evidence for this and prior years; participation/request date or documented Law 152 status; previous breaches; professional-consultancy client concentration; electronic-system phase and filing compliance; legal form, costs and profit; and any special-sector or cross-border facts. Do not present an illustrative computation as a filed liability.

## Sources

| Official source | Relevant material read | Read on |
|---|---|---|
| [Law 6/2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) | All five pages; arts. 1–16 | 2026-11-26 |
| [Decision 420/2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) | Both Gazette pages; arts. 1–4 | 2026-11-26 |
| [ETA Services Guide, 2nd edition](https://eta.gov.eg/sites/default/files/2025-08/guide.of_.the_.egyptian.tax_.authority.services.second%20edition.pdf) | Section 18/2, PDF pp. 247–252 | 2026-11-26 |

Not yet confirmed for individual use: the referred cases above. Check this point with one of our partner accountants.
