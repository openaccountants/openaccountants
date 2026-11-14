---
name: mt-estimated-tax
description: Use this skill for Malta provisional tax (PT) in basis year 2026, mainly for self-employed individuals. Trigger on provisional tax Malta, PT instalments, PT1 notice, 30 April 31 August 21 December tax, PT reduction form, late provisional tax Malta, estimated tax Malta. Covers who pays, the PT benchmark (the tax in the self-assessment for the benchmark year of assessment with PT added back, so basis year 2024 for 2026), the 20%, 30% and 50% instalments on 30 April, 31 August and 21 December, new taxpayers, rent taxed at 15% kept out, the reduction form, additional tax at 0.6% a month or part with the 90% cut, the 30 June settlement, refunds and interest. Rates are in malta-income-tax.
version: "3.0"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Malta provisional tax, basis year 2026

## Scope

Provisional tax (PT) is the in-year payment of income tax under the Income Tax Management Act, Cap. 372, art. 42, and the Payment of Provisional Tax (P.T.) Rules, S.L. 372.18. This skill computes and checks the **2026** instalments (basis year 2026, year of assessment 2027), mainly for **self-employed individuals**, and reconciles them with the return.

- PT benchmark for 2026: the self-assessment for the benchmark year of assessment, normally year of assessment 2025 (basis year 2024).
- Instalments: 20% by 30 April 2026, 30% by 31 August 2026, 50% by 21 December 2026.
- Rates: [malta-income-tax](malta-income-tax.md). Rent: [mt-rental-income](mt-rental-income.md). Capital gains provisional tax (7% within fifteen days) is a different charge: [mt-capital-gains](mt-capital-gains.md).

Out of scope (refer): company PT detail beyond the benchmark rule, non-resident PT, mergers and divisions (rule 9), penalty disputes.

Built from the law: not yet approved by an accountant.

## Ask the client first

1. The PT notice for 2026 (MTCA calls it PT1), or the 2024 self-assessment (YA 2025) showing tax payable and the PT taken into account.
2. When the business started, and whether a return was due for the benchmark year.
3. Whether 2026 tax will be lower than the benchmark (reduction form).
4. Which instalments were paid, how much, and on what dates.
5. Whether any rent is taxed at 15% on the TA24.
6. Whether a Commissioner's assessment for the benchmark year was notified before an instalment month.

## The method, step by step

1. **Who pays.** Every company; an individual liable to tax for the benchmark year of assessment, except one who could elect not to file under ITMA art. 12 for that year; any other person that is not a company or individual. The Commissioner can exempt by written notice (S.L. 372.18 rule 2(1)).
2. **Find the benchmark year of assessment**: the last one for which a return was due before 1 January of the year of the first instalment (rule 2(1)). For 2026, year of assessment 2025.
3. **Compute the PT benchmark.** "The amount of tax payable, if any, for the benchmark year of assessment as shown in the self assessment ... and adding back provisional tax taken into account in the said self assessment" (rule 6(1)). Tax deducted at source is not added back. A further return (AF1) filed after the start of the month before the first instalment is ignored (rule 6(2)). A Commissioner's art. 31(5) assessment notified before the instalment month replaces it (rule 6(3)). With no self-assessment before the month preceding the instalment, use the Commissioner's art. 31(3) determination, then the last earlier self-assessment, else nil (rule 7). The Commissioner may set a higher benchmark by notice.
4. **Split 20 / 30 / 50**, never equal thirds (rule 5).
5. **New taxpayers.** A person who is not an individual has a nil benchmark for its first year of assessment; the second year uses its own computation for the first (rule 8). An individual has no automatic first-year exemption: test the existing benchmark liability and any notice. With none, no PT is due and the tax is settled with the return.
6. **Excluded income.** Rent taxed at the 15% final tax on TA24 is not in the self-assessment, so not in the benchmark; rent declared in the return is.
7. **Expected drop?** File the reduction form (Schedule to S.L. 372.18) with the estimated tax; no approval needed, can be filed more than once (rule 10). Each later instalment is the lower of the normal amount and the estimate less PT paid. A shortfall against the actual tax bears additional tax (rule 12(2)). Flag for review before advising.
8. **Reconcile at year end**: balance = tax per the 2026 self-assessment less PT paid less tax at source; pay by 30 June 2027, or a refund.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Due dates | 30 April, 31 August and 21 December of each basis period | All provisional tax payers | S.L. 372.18 rule 4(1): https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| Instalments | At least 20%, a further 30% and a further 50% of the PT benchmark | Benchmark applicable when each payment falls due | S.L. 372.18 rule 5: https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| PT benchmark | Tax payable in the benchmark-year self-assessment plus PT taken into account | Rule 6(1); fallbacks in rule 7 | same |
| First year, not an individual | Nil benchmark | Rule 8(1) | same |
| Additional tax on late PT | 0.6% of the unpaid PT for each calendar month or part | Periods from 1 June 2022 | S.L. 372.18 rule 14(1): https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| Cut where actual tax is below the benchmark | Additional tax on the difference reduced by 90% | Rule 14(1), last proviso | same |
| Additional tax stops | No further additional tax for any month starting after the tax settlement date | Rule 14(2) | same |
| Tax settlement date, individual | 30 June of the year of assessment (30 June 2027) | Online return by 31 July (MTCA) | MTCA Tax Return Cycle: https://mtca.gov.mt/personal-tax/individual/tax-return-cycle |
| Interest on tax unpaid after the settlement date | 0.6% for every month or part, capped at the tax | Tax payable on 31 August 2022 or later | S.L. 372.28 rule 2: https://legislation.mt/eli/sl/372.28/eng/pdf |
| No interest on top of PT additional tax | Interest under art. 44(2A) does not run on tax bearing this additional tax | ITMA art. 44(2B)(d) | Cap. 372: https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Refund interest | 0.6% for each month or part | Periods from 1 September 2022 | Cap. 372 art. 48(2D): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Refund date, individual | Refund issued by 31 December of the filing year if the return was in time; interest from 1 January after | Return filed on time; all returns filed; bank details in My Account | MTCA Tax Return Cycle: https://mtca.gov.mt/personal-tax/individual/tax-return-cycle |

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| No benchmark self-assessment and no PT notice | Stop: ask for the PT1 or the 2024 self-assessment; never estimate from income |
| First or second year of business | Check whether a return was due for the benchmark year |
| Income expected to drop | Pay per notice, or file the reduction form; never just pay less |
| Rent on TA24 | Excluded from the benchmark |

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| Self-employed three years, never filed | Benchmark = the Commissioner's determination; filing replaces it | Rule 7 |
| Benchmark year tax nil | No instalments (unless a notice sets one); voluntary payments prudent | Rule 6 |
| Employee turned self-employed mid-year | No benchmark if no return was due; settle with the return | Rule 2(1) |
| Client stops trading mid-year | File the reduction form | Rule 10 |
| PT notice differs from your figure | Reconcile; pay the notice or file the reduction form; query separately | Rule 14 runs on any shortfall |
| Foreign income with double tax relief | Benchmark already net of the relief; confirm relief for the current year | Rule 6 |
| Benchmark return filed late | Determination until filed, then the self-assessed tax | Rules 6, 7 |
| Remission of additional tax | Only absence from Malta, serious sickness or a prescribed cause | ITMA art. 44(2) |

### Bank statement patterns

An MTCA payee, a year reference or April, August or December timing does not prove PT: the same authority collects SSC, VAT and other taxes. Confirm against the PT notice or tax account.

| Pattern | Treatment |
|---|---|
| MTCA, CFR, INLAND REVENUE, PROVISIONAL TAX, PT2026, INSTALMENT 1/2/3 | Candidate PT; confirm the allocation |
| Debit 15 April to 10 May, 15 August to 15 September, 1 to 31 December | Likely 1st, 2nd, 3rd instalment if payee is MTCA |
| Debit in June of the following year | Settlement with the return, not PT |
| VAT, SSC, CLASS 2, FSS, PENALTY, INTEREST | Not PT |

A PT payment is a tax payment, not a deductible business cost.

## Worked cases

### Case 1: benchmark and the 2026 instalments

The 2024 self-assessment (YA 2025) shows tax payable of EUR 3,000 after taking into account EUR 6,000 of PT. Benchmark EUR 9,000. Instalments EUR 1,800 (30 April 2026), EUR 2,700 (31 August 2026), EUR 4,500 (21 December 2026). If the 2026 self-assessment shows EUR 11,500 and nothing was deducted at source, EUR 2,500 is due by 30 June 2027.

```oa-check
name: PT benchmark from the 2024 self-assessment, 2026 instalments and settlement
inputs:
  tax_payable_2024: 3000
  pt_taken_2024: 6000
  tax_2026: 11500
steps:
  - benchmark: tax_payable_2024 + pt_taken_2024
  - april: pct(benchmark, 20)
  - august: pct(benchmark, 30)
  - december: pct(benchmark, 50)
  - total: april + august + december
  - balance_june_2027: tax_2026 - total
expected:
  benchmark: 9000.00
  april: 1800.00
  august: 2700.00
  december: 4500.00
  total: 9000.00
  balance_june_2027: 2500.00
```

### Case 2: late first instalment, with and without the 90% cut

The EUR 1,800 April 2026 instalment is paid on 15 July 2026: May, June and part of July, three months. If 2026 tax is at least the benchmark, additional tax is 0.6% x 3 on EUR 1,800 = EUR 32.40. If the 2026 tax turns out to be EUR 7,000 against a EUR 9,000 benchmark, the April instalment on the actual tax would have been EUR 1,400; the charge on the EUR 400 difference is cut by 90%: EUR 25.20 + EUR 0.72 = EUR 25.92.

```oa-check
name: Late April 2026 PT, 3 months or part, full charge and 90 percent cut
inputs:
  unpaid: 1800
  due_on_actual: 1400
  months_part: 2.5
steps:
  - months: ceil(months_part)
  - full_charge: pct(unpaid, 0.6) * months
  - on_actual: pct(due_on_actual, 0.6) * months
  - on_difference_cut: pct(unpaid - due_on_actual, 0.6) * months * 0.10
  - reduced_charge: on_actual + on_difference_cut
expected:
  months: 3
  full_charge: 32.40
  on_actual: 25.20
  on_difference_cut: 0.72
  reduced_charge: 25.92
```

### Further cases (prose)

- **Overpayment.** PT paid EUR 10,000, tax EUR 7,200: EUR 2,800 refunded by 31 December of the filing year if the return was on time; then 0.6% a month interest.
- **Rent excluded.** Benchmark year: EUR 3,000 tax in the return, plus EUR 1,500 paid on TA24 rent. PT on EUR 3,000 only: EUR 600, EUR 900, EUR 1,500.
- **Reduction form.** Benchmark EUR 1,000, estimate EUR 800: pay EUR 200, EUR 300, then EUR 300.

## When to refuse or refer

| Code | Trigger | Message |
|---|---|---|
| R-MT-PT-1 | Company or partnership PT beyond the benchmark rule, group or merger cases | "Company instalment dates follow the accounting period and group rules apply. Please consult a warranted accountant." |
| R-MT-PT-2 | Non-resident PT | "Non-resident provisional tax is outside this skill. Please consult a warranted accountant." |
| R-MT-PT-3 | Disputing PT additional tax or enforcement | "Penalty disputes need legal analysis. Please escalate to a warranted accountant or tax advocate." |
| R-MT-PT-4 | No benchmark self-assessment and no notice | Stop; do not estimate |

Never: use current-year income as the basis without a reduction form; skip payments because income will drop; split in thirds; include TA24 rent; present figures as final without the PT notice; promise a refund date unless the return was on time and bank details are in My Account.

## Filing and payment

Pay each instalment by its due date online (MTCA online payments) or at Malta Post using the PT notice reference. File a reduction form on the Schedule to S.L. 372.18 before the instalment it should affect. The 2026 return and self-assessment is filed on [myTax](https://mytax.mtca.gov.mt/) with e-ID; the tax settlement date is 30 June 2027 and the online return date 31 July 2027. A correction after filing is an AF1, but an AF1 filed after the start of the month before the first instalment does not change that year's benchmark (rule 6(2)).

## Completion checklist

- [ ] Benchmark self-assessment or PT notice in hand.
- [ ] 20/30/50 split; three due dates stated.
- [ ] TA24 rent excluded.
- [ ] New-business rule checked.
- [ ] Reduction form flagged for review where used.
- [ ] Year-end reconciliation and refund or balance shown.
- [ ] Output labelled estimated until the PT notice is confirmed.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for S.L. 372.18 rules 2, 4, 5, 6, 7, 8, 10, 12 and 14 (who pays, dates, 20/30/50, benchmark, fallbacks, new taxpayers, reduction, 0.6% additional tax, 90% cut, settlement date) | https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 | 2026-11-14 |
| Read for S.L. 372.28 rule 2 (0.6% interest for tax payable from 31 August 2022, capped) | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-14 |
| Read for Cap. 372 arts 42, 44(1), 44(2), 44(2A), 44(2B)(d) and 48(2D) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-14 |
| Read for MTCA Tax Return Cycle (30 June settlement, 31 July online, refund by 31 December, 0.6%) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-14 |
| Read for MTCA Manual on the Taxation of Rental Income (PT on rent declared in the return; 30 April, 31 August, 21 December) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-11-14 |

Not yet confirmed: the PT1 notice name and the refund conditions (all returns filed, bank details in My Account), which come from MTCA pages not the law; the MTCA provisional tax booklet (2019 edition, not re-read); whether MTCA has extended the 2027 return date.
