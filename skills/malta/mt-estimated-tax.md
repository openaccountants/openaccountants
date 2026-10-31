---
name: mt-estimated-tax
description: 'Use this skill whenever asked about Malta provisional tax (estimated tax) for self-employed or self-occupied individuals. Trigger on phrases like "provisional tax Malta", "estimated tax", "PT instalments", "how much provisional tax do I pay", "20% 30% 50%", "April instalment", "August instalment", "December instalment", "PT benchmark", "PT reduction form", "refund of provisional tax", "Chapter 372", "ITMA article 42", or any question about Malta''s advance income tax payment obligations. Covers basis year 2026: the three-instalment schedule (20/30/50 on 30 April, 31 August, 21 December), the PT benchmark taken from the self-assessment two years earlier, first-year rules, the PT reduction form, interest of 0.6% a month on late payment, and settlement with the tax return by 30 June. ALWAYS read this skill before touching any Malta provisional tax work.'
version: 2.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MT Estimated Tax

## Malta Provisional Tax (PT) -- Self-Employed Skill v2.1

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

Tax year: basis year 2026 (year of assessment 2027). The PT benchmark for 2026 comes from the self-assessment for basis year 2024. Rates are in [malta-income-tax](malta-income-tax.md); rental income is in [mt-rental-income](mt-rental-income.md).

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax | Income tax provisional payments (Provisional Tax / PT) |
| Primary legislation | Income Tax Management Act, Chapter 372, Article 42(2); Payment of Provisional Tax (P.T.) Rules, S.L. 372.18 (L.N. 48 of 2000) |
| Authority | Commissioner for Tax and Customs / Malta Tax and Customs Administration (MTCA) |
| Portal | https://mtca.gov.mt (myTax) |
| Currency | EUR only |
| Payment schedule | Three instalments: 20% by 30 April, 30% by 31 August, 50% by 21 December |
| Computation basis | PT benchmark: the tax payable in the self-assessment for the basis year two years earlier, adding back the PT paid for that year (for 2026: basis year 2024, YA 2025). The Commissioner may set a higher benchmark by written notice |
| Who pays | Every company; an individual liable to tax in Malta for the benchmark year of assessment, except one who could elect under Article 12 ITMA (no return) for that year; any other person that is not a company or an individual. The Commissioner can exempt by written notice (S.L. 372.18, rule 2(1)) |
| First year of business | No PT; the tax for that year is paid with the return by 30 June of the next year |
| Late payment | Additional tax of 0.6% of the unpaid PT for each calendar month or part (S.L. 372.18, rule 14(1), for periods from 1 June 2022; MTCA pages say from 1 September 2022). Cut by 90% on the part of the benchmark above the tax the self-assessment shows. Stops at the tax settlement date |
| Tax year | Basis year 2026 |
| Review status | Source-cited draft: not reviewed by an accountant |

**Instalment schedule summary**

| Instalment | Percentage | Due date |
| --- | --- | --- |
| 1st | 20% | 30 April |
| 2nd | 30% | 31 August |
| 3rd | 50% | 21 December |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| No benchmark-year self-assessment or PT notice available | STOP: request the PT notice (PT1) or the basis year 2024 self-assessment |
| First or second year of business | Check whether a return was due for the benchmark year; if not, no PT benchmark |
| Income expected to drop | Pay per notice, or file a PT reduction form; do not simply pay less |
| Rental income taxed at the 15% final tax (TA24) | Not in the return, so not in the benchmark |
| Overpayment treatment | Refunded by 31 December of the year the return is filed, if the return was filed on time and bank details are in My Account |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- the self-assessment for the benchmark year (basis year 2024 for 2026 PT): tax underpaid and PT paid for that year; OR the PT notice (PT1) issued by MTCA. One of these is mandatory.

**Recommended** -- current year of assessment, any PAYE or withholding tax deducted at source in the current year, the client's TIN.

**Ideal** -- the full benchmark-year return and tax statement, any PT notice received, bank statements showing PT payments, any PT reduction form filed.

**Refusal policy if minimum is missing -- HARD STOP.** Without the benchmark-year self-assessment or a PT notice, provisional tax cannot be computed. Do not estimate from income figures.

### Refusal catalogue

- **R-MT-PT-1 -- Group companies or partnership PT**: Trigger: client asks about PT for a company or partnership. Message: "This skill covers provisional tax for self-employed individuals only. Companies also pay PT, with instalment dates that follow their accounting period. Please consult a warranted accountant."  _(Section 2 -- Refusal catalogue)_
- **R-MT-PT-2 -- Non-resident PT obligations**: Trigger: client is non-resident or asks about PT for non-residents. Message: "Non-resident provisional tax obligations are outside the scope of this skill. Please consult a warranted accountant."  _(Section 2 -- Refusal catalogue)_
- **R-MT-PT-3 -- PT penalty disputes**: Trigger: client asks about disputing PT penalties or CFR enforcement. Message: "Penalty disputes require legal analysis. Please escalate to a warranted accountant or tax advocate."  _(Section 2 -- Refusal catalogue)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a provisional tax payment. Do not second-guess.

### 3.1 CFR provisional tax debits

**CFR provisional tax debits**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MTCA, CFR, COMMISSIONER FOR REVENUE | PT payment | Match with April/August/December timing to identify which instalment |
| INLAND REVENUE MALTA | PT payment | Legacy name, same authority |
| PROVISIONAL TAX, PROV TAX, PT PAYMENT | PT payment | Explicit description |
| TAX INSTALMENT, TAX INST | PT payment | Generic instalment label |

### 3.2 Timing-based identification

**Timing-based identification**

| Debit date range | Likely instalment | Confidence |
| --- | --- | --- |
| 15 April -- 10 May | 1st instalment (20%) | High if payee is CFR |
| 15 August -- 15 September | 2nd instalment (30%) | High if payee is CFR |
| 1 December -- 31 December | 3rd instalment (50%) | High if payee is CFR |
| 1 June -- 30 June (following year) | Settlement with the return | Not PT |
| Any other date to MTCA | Late payment or adjustment | Flag for reviewer |

### 3.3 Related but NOT provisional tax

**Related but NOT provisional tax**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VAT DEPARTMENT, VAT PAYMENT | EXCLUDE from PT | VAT payment, separate obligation |
| SSC, SOCIAL SECURITY, CLASS 2 | EXCLUDE from PT | Social security contribution |
| FSS, FINAL SETTLEMENT | EXCLUDE from PT | PAYE final settlement system |
| PENALTY, INTEREST CFR | EXCLUDE from PT | Late payment charge, not PT principal |

### 3.4 Bank transfer references

**Bank transfer references**

| Reference pattern | Treatment | Notes |
| --- | --- | --- |
| PT followed by year (e.g., PT2025) | PT payment for that year | Common bank transfer reference format |
| YA followed by year | PT payment for that year of assessment | Alternative reference format |
| INSTALMENT 1, INSTALMENT 2, INSTALMENT 3 | PT payment, specific instalment | Self-identified |

## Section 4 -- Worked examples

### Example 1 -- Standard three-instalment computation

The 2024 self-assessment (YA 2025) shows tax underpaid of EUR 3,000, and EUR 6,000 of PT was paid for 2024. The 2026 PT benchmark is EUR 3,000 + EUR 6,000 = EUR 9,000. Tax deducted at source is not added back. The 2026 instalments are 20%, 30% and 50% of that.

| Instalment | Percentage | Amount | Due date |
| --- | --- | --- | --- |
| 1st | 20% | EUR 1,800 | 30 April 2026 |
| 2nd | 30% | EUR 2,700 | 31 August 2026 |
| 3rd | 50% | EUR 4,500 | 21 December 2026 |
| **Total** | **100%** | **EUR 9,000** |  |

```oa-check
name: PT benchmark from the 2024 self-assessment, 2026 instalments
inputs:
  tax_underpaid_2024: 3000
  pt_paid_2024: 6000
steps:
  - benchmark: tax_underpaid_2024 + pt_paid_2024
  - april: pct(benchmark, 20)
  - august: pct(benchmark, 30)
  - december: pct(benchmark, 50)
  - total: april + august + december
expected:
  benchmark: 9000.00
  april: 1800.00
  august: 2700.00
  december: 4500.00
  total: 9000.00
```

### Example 2 -- Reconciliation with the return (underpayment)

**Input:** Total PT paid for 2026 = EUR 8,000. Tax per the 2026 self-assessment = EUR 11,500.

**Output:** Balance due = EUR 11,500 - EUR 8,000 = EUR 3,500, payable by the tax settlement date, 30 June 2027.

### Example 3 -- Reconciliation with the return (overpayment)

**Input:** Total PT paid = EUR 10,000. Tax per the self-assessment = EUR 7,200.

**Output:** Overpayment = EUR 2,800. If the return was filed on time, MTCA refunds it by 31 December of the filing year; after that, interest runs in the taxpayer's favour at 0.6% a month. The refund needs all income tax and VAT returns filed and bank details in My Account.

### Example 4 -- Rental income at 15% excluded from PT basis

**Rental income excluded from PT basis**

| Instalment | Amount |
| --- | --- |
| 1st (20%) | EUR 600 |
| 2nd (30%) | EUR 900 |
| 3rd (50%) | EUR 1,500 |

The benchmark is EUR 3,000: the 15% tax on rent was paid with the TA24 and never entered the return.

### Example 5 -- Late payment interest

The first 2026 instalment of EUR 1,800 was due 30 April 2026 and paid 15 July 2026. Interest is 0.6% for each calendar month or part of a month. May, June and the part of July give 3 months, so EUR 32.40. This assumes the 2026 tax is not below the benchmark; otherwise the 90% cut in rule 14(1) applies to the difference.

```oa-check
name: Late April 2026 PT instalment, paid 15 July, 0.6% per month or part
inputs:
  unpaid: 1800
  rate_pct: 0.6
  months_part: 2.5
steps:
  - months: ceil(months_part)
  - interest: pct(unpaid, rate_pct) * months
expected:
  months: 3
  interest: 32.40
```

### Example 6 -- Bank statement classification

**Input line:** `30.04.2026 ; MTCA ONLINE PAYMENT ; DEBIT ; PT2026 INST 1 ; -1,800.00 ; EUR`

**Classification:** Provisional tax payment, 1st instalment for basis year 2026. Not a deductible expense for VAT or income tax purposes: this is a tax payment, not a business cost.

## Section 5 -- Computation rules

### 5.1 Standard computation (benchmark year)

- **Standard computation (benchmark year)**: The PT benchmark for a basis year is the tax payable in the self-assessment for the basis year two years earlier, adding back the PT paid for that year. Tax deducted at source stays deducted. ``` benchmark = tax_underpaid_line + PT_paid_for_benchmark_year PT_instalment_1 = benchmark x 20% PT_instalment_2 = benchmark x 30% PT_instalment_3 = benchmark x 50% ``` Do NOT divide by three equally. The split is always 20/30/50. If no self-assessment was filed for the benchmark year before the month preceding the instalment, the benchmark is the tax in the Commissioner's Article 31(3) determination (the estimated tax statement); without one, the last earlier self-assessment; without either, nil. The Commissioner can set a higher benchmark by written notice.  _(S.L. 372.18, rules 2(1), 5, 6(1), 6(4), 7(1); MTCA PT booklet Q3, Q8)_

### 5.2 Year-end reconciliation

- **Year-end reconciliation**: ``` balance_due = self_assessment_tax - total_PT_paid - tax_at_source if balance_due > 0: pay by 30 June of the following year if balance_due < 0: refund by 31 December if the return was filed on time ```  _(Section 5.2)_

### 5.3 First year and new businesses

- **First year and new businesses**: In the first year of business there is no PT; the tax is paid with the return by 30 June of the following year. The benchmark year of assessment is the last one for which a return was due before 1 January of the year of the first instalment (S.L. 372.18, rule 2(1)). An individual whose business starts in 2025 files the first return for YA 2026 by 30 June 2026, so the first PT is for basis year 2027, on a benchmark from basis year 2025. The Commissioner may exempt a person, or set a benchmark, by written notice.  _(S.L. 372.18, rule 2(1); MTCA PT booklet Q2, Q11)_

### 5.4 Excluded income

- **Excluded income**: Income taxed at a final tax outside the return (for example the 15% on rent paid with the TA24) is not in the self-assessment, so it is not in the benchmark. Rent declared in the return under the normal system IS in the benchmark.  _(Section 5.4; MTCA manual on rental income)_

## Section 6 -- Penalties and interest

### 6.1 Late payment interest

**Late payment interest**

| Element | Rate |
| --- | --- |
| Interest rate | 0.6% per month or part thereof (from 1 September 2022) |
| Runs from | Due date of each instalment |
| Stops | No further additional tax on unpaid PT for any month starting after the tax settlement date, 30 June of the year of assessment (S.L. 372.18, rule 14(2); S.L. 372.16, rule 5) |
| 90% reduction | Where the self-assessed tax is below the PT benchmark, the additional tax on the difference is cut by 90% (S.L. 372.18, rule 14(1), last proviso) |
| Shortfall after the year | Tax unpaid after the 30 June settlement date bears interest of 0.6% for each month or part; total interest cannot exceed the tax (S.L. 372.28, rule 2) |

### 6.2 Interest computation

- **Interest computation**: ``` interest = unpaid_amount x 0.6% x months_or_part_overdue ``` Interest accrues per instalment independently. The charge on the part of the benchmark above the tax actually due is cut by 90% (rule 14(1), last proviso, still in force after L.N. 99 of 2022).  _(S.L. 372.18, rule 14)_

## Section 7 -- Adjustments and reductions

- **Adjustments and reductions**: If the taxpayer expects the tax for the year to be lower than the benchmark, they file the PT reduction form in the Schedule to S.L. 372.18 giving the estimated tax. No approval is needed, and the form can be filed more than once in a year (rule 10(2)). Each later instalment is the lower of the normal 20/30/50 amount and the estimate less PT already paid (rule 10(3)). The instalments still follow the original benchmark (20% and 30%) until the reduced total is reached; the last instalment is the balance. Example: benchmark EUR 1,000, estimate EUR 800: pay EUR 200, EUR 300, then EUR 300. Risk: if the tax for the year exceeds the reduced total, interest runs on the shortfall. Flag for reviewer before advising any PT reduction.  _(S.L. 372.18, rules 10 to 12; MTCA PT booklet Q9; MTCA FAQ 5)_

## Section 8 -- Edge cases

**EC1 -- No self-assessment for the benchmark year.** Client has been self-employed for 3 years but never filed a return. The benchmark is the tax in the Commissioner's estimated tax statement. Filing the return replaces it with the self-assessed figure. Flag for reviewer -- client must regularise filing history urgently.

**EC2 -- Benchmark year resulted in zero tax.** Tax liability = EUR 0. PT = EUR 0. No instalments required. However, if current year income is expected to exceed the personal allowance, voluntary PT payments are prudent.

**EC3 -- Mid-year switch from employment to self-employment.** First year of self-employment. If the benchmark year had no return due (employment only, taxed under FSS), there is no PT benchmark yet. Tax on the self-employed income is settled with the return. Flag for reviewer.

**EC4 -- Rental income at the 15% final tax.** Rent taxed at 15% on the TA24 is not in the return, so it is outside the benchmark. Rent declared in the return is inside it.

**EC5 -- Overpayment.** If the return was filed on time, MTCA refunds by 31 December, with interest at 0.6% a month after that. The refund is held until all income tax and VAT returns are filed and bank details are in My Account.

**EC6 -- Client ceases self-employment mid-year.** File a PT reduction form with the estimated tax for the year. The return reconciles the actual liability.

**EC7 -- PT notice differs from client calculation.** The notice sets the benchmark. Pay the stated amount, or file a PT reduction form, and query separately. Paying less without a reduction form triggers interest on the shortfall.

**EC8 -- Foreign source income with DTR.** The benchmark is the tax payable in the benchmark-year self-assessment, which already reflects double taxation relief. Flag for reviewer to confirm DTR availability in the current year.

**EC9 -- Late filing of the benchmark-year return.** Until it is filed, the benchmark is the estimated tax statement. Once filed, the benchmark is revised to the self-assessed tax.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Benchmark-year self-assessment (two years earlier) confirmed, or PT notice obtained
- [ ] 20/30/50 split applied (NOT equal thirds)
- [ ] Rent taxed at the 15% final tax excluded from PT basis
- [ ] All three instalment due dates stated (30 Apr, 31 Aug, 21 Dec)
- [ ] Year-end reconciliation formula presented
- [ ] First-year / new business rule checked
- [ ] Any adjustment request flagged for reviewer
- [ ] Overpayment treatment explained (credit vs refund)
- [ ] Penalty rates stated if relevant
- [ ] Output labelled as estimated until the PT notice is confirmed

## Section 10 -- Test suite

### Test 1 -- Standard three-instalment computation

**Input:** PT benchmark (2024 self-assessment) = EUR 9,000.
**Expected:** 1st = EUR 1,800 (30 Apr). 2nd = EUR 2,700 (31 Aug). 3rd = EUR 4,500 (21 Dec). Total = EUR 9,000.

### Test 2 -- Zero prior year tax

**Input:** Benchmark-year tax = EUR 0.
**Expected:** PT = EUR 0. No instalments due. Flag: advise voluntary payments if current year income expected to exceed threshold.

### Test 3 -- Underpayment reconciliation

**Input:** Total PT paid = EUR 8,000. Self-assessment tax = EUR 11,500.
**Expected:** Balance due = EUR 3,500. Due by 30 June of the following year.

### Test 4 -- Overpayment reconciliation

**Input:** Total PT paid = EUR 10,000. Self-assessment tax = EUR 7,200.
**Expected:** Overpayment = EUR 2,800. Refunded by 31 December if the return was filed on time.

### Test 5 -- Late payment penalty

**Input:** 1st instalment EUR 1,800 due 30 April. Paid 15 July (2.5 months, counted as 3).
**Expected:** Interest = EUR 1,800 x 0.6% x 3 = EUR 32.40.

### Test 6 -- First year, no prior assessment

**Input:** First year of self-employment. No return due for the benchmark year.
**Expected:** No PT for the year. Tax paid with the return by 30 June of the following year. Flag for reviewer if a PT notice arrives anyway.

### Test 7 -- Rental income excluded

**Input:** Benchmark year: EUR 3,000 tax in the return on SE income, plus EUR 1,500 paid on rent with the TA24 (15%).
**Expected:** PT on EUR 3,000 only. 1st = EUR 600, 2nd = EUR 900, 3rd = EUR 1,500.

## Prohibitions

- NEVER compute PT without the benchmark-year self-assessment or a PT notice
- NEVER use current year estimated income as the basis: PT follows the benchmark year (two years earlier) unless a PT reduction form is filed
- NEVER advise skipping PT payments because income is expected to drop: file a PT reduction form
- NEVER divide by three equally -- the split is always 20/30/50
- NEVER include income taxed at a final tax outside the return (rent at 15%) in the PT basis
- NEVER present PT figures as definitive without a PT notice: label as estimated
- NEVER advise on PT penalty disputes without escalating to a warranted accountant
- NEVER promise a refund date unless the return was filed on time and bank details are in My Account

## Ask the Client First

- The PT notice (PT1) for 2026, or the 2024 self-assessment showing tax underpaid and PT paid.
- The year the business started, and whether a return was due for 2024.
- Whether 2026 tax will be lower than the benchmark (for a PT reduction form).
- Which instalments have been paid, and on what dates.
- Whether any rent is taxed at 15% on the TA24.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, Provisional Tax and Social Security Contributions booklet (2019 edition, linked from the Tax Return Cycle page) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-cycle/pt-booklet730742a2-5244-4a68-81a5-6af28f61d15f.pdf | 2026-10-23 |
| MTCA, Tax Return Cycle (30 June settlement, 0.6% interest, refunds by 31 December) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-10-23 |
| MTCA, FAQs General Questions (PT reduction form; 0.6% per month or part from 1 September 2022) | https://mtca.gov.mt/personal-tax/legal-and-technical/faqs/faqs---general-questions | 2026-10-23 |
| MTCA, Manual on the Taxation of Rental Income (Article 42 ITMA, PT on rent) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-10-23 |
| MTCA, Budget Measures Implementation Act 2026 overview (no change to PT) | https://mtca.gov.mt/business-tax/legislative-developments/2026 | 2026-10-23 |
| Income Tax Management Act, Cap. 372, Article 42(2) | https://legislation.mt/eli/cap/372/eng | 2026-10-23 |
| Payment of Provisional Tax (P.T.) Rules, S.L. 372.18 (as amended to L.N. 99 of 2022), rules 2 to 14 | https://legislation.mt/eli/sl/372.18/eng | 2026-10-23 |
| Income Tax (Rate of Interest) Rules, S.L. 372.28, rule 2 | https://legislation.mt/eli/sl/372.28/eng | 2026-10-23 |
| Income Tax (Statutory Dates) Rules, S.L. 372.16, rules 2 and 5 | https://legislation.mt/eli/sl/372.16/eng | 2026-10-23 |

Not yet confirmed: the start date of the 0.6% rate for PT (rule 14(1) says periods from 1 June 2022; MTCA pages say 1 September 2022; this does not change any 2026 figure); the 31 December refund date and refund interest, taken from the MTCA Tax Return Cycle page rather than Article 48 ITMA.

> Contributed by Michael Cutajar.

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
