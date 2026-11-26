---
name: mt-estimated-tax
description: Use this skill for Malta provisional tax (PT) in basis year 2026, mainly for self-employed individuals. Trigger on provisional tax Malta, PT instalments, PT1 notice, 30 April 31 August 21 December tax, PT reduction form, late provisional tax Malta, estimated tax Malta. Covers who pays, the PT benchmark (the tax in the self-assessment for the benchmark year of assessment with PT added back, so basis year 2024 for 2026), the 20%, 30% and 50% instalments on 30 April, 31 August and 21 December, new taxpayers, rent taxed at 15% kept out, the reduction form, additional tax at 0.6% a month or part with the 90% cut, the 30 June settlement, refunds and interest. Rates are in malta-income-tax.
version: "3.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
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
- Rates: [malta-income-tax](malta-income-tax.md). Rent: [mt-rental-income](mt-rental-income.md). Capital-gains provisional tax is a separate computation: [mt-capital-gains](mt-capital-gains.md).

Out of scope (refer): company PT detail beyond the benchmark rule, non-resident PT, mergers and divisions (rule 9), penalty disputes.

Built from the law: not yet approved by an accountant.

## Ask the client first

1. The official PT notice for 2026, or the 2024 self-assessment (YA 2025) showing tax payable and the PT taken into account.
2. When the business started, and whether a return was due for the benchmark year.
3. Whether 2026 tax will be lower than the benchmark (reduction form).
4. Which instalments were paid, how much, and on what dates.
5. Whether any rent is taxed at 15% on the TA24.
6. Whether a Commissioner's assessment for the benchmark year was notified before an instalment month.

## The method, step by step

1. **Who pays.** Every company; an individual liable to tax for the benchmark year of assessment, except one who could elect not to file under ITMA art. 12 for that year; any other person that is not a company or individual. The Commissioner can exempt by written notice (S.L. 372.18 rule 2(1)).
2. **Find the benchmark year of assessment**: the last one for which a return was due before 1 January of the year of the first instalment (rule 2(1)). For 2026, year of assessment 2025.
3. **Compute the PT benchmark.** Take the benchmark-year self-assessment tax payable and add back PT taken into account (rule 6(1)); tax deducted at source is not added back. A further return (AF1) filed after the start of the month before the first instalment is ignored (rule 6(2)). A Commissioner's article 31(5) assessment notified before the instalment month replaces it, again adding back PT taken into account (rule 6(3)). Without a self-assessment before the month preceding the instalment, use the article 31(3) determination notified before the instalment month, then the last earlier self-assessment furnished before the relevant cutoff, else nil (rule 7). A later self-assessment that changes the benchmark for a subsequent instalment recalculates it for all instalments of the basis period, preserving collection rights already accrued (rule 7(2)–(3)). A higher benchmark by written notice under rule 6(4) must follow the notice timing: a notice during or after an instalment month can require payment by that month's last day or a later date the Commissioner determines within the same basis period. Check the actual notice.
4. **Split 20 / 30 / 50**, never equal thirds (rule 5). Each PT payment is rounded to the nearest euro (rule 3(3)). If a rule 6(3)/(4) assessment/notice increases the benchmark, the second payment must bring cumulative PT to at least 50% of the new benchmark; the third must bring it to the full new benchmark, less payments already made. Do not merely apply 30% or 50% to an increased benchmark.
5. **New taxpayers.** A person who is not an individual has a nil benchmark for its first year of assessment; the second year uses its own computation for the first (rule 8). An individual has no automatic first-year exemption: apply the payer definition, rule 7 fallbacks and any notice; absence of a notice alone does not establish exemption.
6. **Excluded income.** For an individual who validly opts for the article 31D final-rent tax, the rent is separate chargeable income and is not declared in the ordinary return (article 31D(2)–(3)); do not add either that income or its separate final tax to ordinary PT. Ordinary-return rent affects the self-assessment used for the benchmark. Rent-option eligibility belongs in the rental Guide.
7. **Expected drop?** Exercise the option by delivering the prescribed reduction form; it may be exercised more than once (rule 10). Compute the estimate in the manner of rule 6, substituting estimated current-year amounts (rule 11). Each instalment falling due after the option is exercised is the lower of the normal amount and the positive excess, if any, of the estimate over PT already paid. A shortfall against actual tax bears additional tax (rule 12(2)). Flag for review before advising.
8. **Reconcile at year end**: reconcile current-year liability, credits, tax at source and PT available for set-off. Rule 14(3) first applies PT against additional tax due up to the settlement date, reducing the PT available against annual tax; additional tax left undischarged becomes tax due for that assessment year (rule 14(4)). For an ordinary individual filer the statutory settlement date is 30 June 2027 (S.L. 372.16 rules 2(c)(ii), 5(b)); refunds depend on article 48, not just subtraction of payments.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Due dates | 30 April, 31 August and 21 December of each basis period | All provisional tax payers | S.L. 372.18 rule 4(1): https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| Instalments | At least twenty percent, a further thirty percent and a further fifty percent of the PT benchmark (the rule writes them in words) | Benchmark applicable when each payment falls due | S.L. 372.18 rule 5: https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| PT benchmark | Tax payable in the benchmark-year self-assessment plus PT taken into account | Rule 6(1); fallbacks in rule 7 | same |
| First year, not an individual | Nil benchmark | Rule 8(1) | same |
| Additional tax on late PT | 0.6% of the unpaid PT for each calendar month or part | Periods from 1 June 2022 | S.L. 372.18 rule 14(1): https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 |
| Cut where actual tax is below the benchmark | Additional tax on the difference reduced by ninety percent (as the rule words it) | Rule 14(1), last proviso | same |
| Additional tax stops | No further additional tax for any month starting after the tax settlement date | Rule 14(2) | same |
| Tax settlement date, ordinary individual filer | 30 June of the year of assessment (30 June 2027 for 2026 income) | Subject to the taxpayer's applicable statutory category; no 2027 online extension assumed | S.L. 372.16 rules 2(c)(ii), 5(b): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Interest on tax unpaid after the settlement date | 0.6% for every month or part, capped at the tax | Tax payable on 31 August 2022 or later | S.L. 372.28 rule 2: https://legislation.mt/eli/sl/372.28/eng/pdf |
| No interest on top of PT additional tax | Interest under art. 44(2A) does not run on tax bearing this additional tax | ITMA art. 44(2B)(d) | Cap. 372: https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Refund interest | 0.6% for each month or part, capped at the repayment | Article 48(2A)/(2B) repayments after article 48(2C) offsets, from the applicable due date; periods from 1 September 2022 | Cap. 372 art. 48(2D): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Refund date, ordinary individual filer | Statutory refund date is 1 January after the year of assessment; MTCA guidance describes refund by 31 December for a timely return | Late/outstanding returns, offsets and payment/due-diligence rules can change the result; see below | S.L. 372.16 rule 6(b)(ii): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 ; Cap. 372 art. 48: https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| No benchmark self-assessment and no PT notice | Stop: obtain the tax account and test rule 7 determination/earlier-return/nil fallbacks; never infer exemption or estimate from income |
| First or second year of business | Check whether a return was due for the benchmark year |
| Income expected to drop | Pay per notice, or file the reduction form; never just pay less |
| Rent on TA24 | Excluded from the benchmark |

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| Self-employed three years, never filed | Test a notified determination, earlier self-assessment and nil fallback in order; a later qualifying return recalculates all instalments under rule 7(2) | Rule 7 |
| Benchmark year tax nil | No instalments (unless a notice sets one); voluntary payments prudent | Rule 6 |
| Employee turned self-employed mid-year | Test benchmark-year liability and eligibility for article 12 election, then rule 7 and any notice; employment change alone gives no exemption | Rules 2(1), 6, 7 |
| Client stops trading mid-year | File the reduction form | Rule 10 |
| PT notice differs from your figure | Reconcile operative benchmark, notice timing, cumulative catch-up and any valid reduction option; seek review where disputed | Rules 5–7, 10, 14 |
| Foreign income with double tax relief | Benchmark already net of the relief; confirm relief for the current year | Rule 6 |
| Benchmark return filed late | Rule 7 cutoffs govern individual payments; a later return can retrospectively recalculate all payments, preserving collection rights | Rules 6, 7(2)–(3) |
| Remission of additional tax | Commissioner discretion, only if satisfied payment was prevented by absence from Malta, serious sickness or a prescribed cause; no automatic waiver | ITMA art. 44(2) |

### Bank statement patterns

An MTCA payee, a year reference or April, August or December timing does not prove PT: the same authority collects SSC, VAT and other taxes. Confirm against the PT notice or tax account.

| Pattern | Treatment |
|---|---|
| MTCA, CFR, INLAND REVENUE, PROVISIONAL TAX, PT2026, INSTALMENT 1/2/3 | Candidate PT; confirm the allocation |
| Debit 15 April to 10 May, 15 August to 15 September, 1 to 31 December | Search windows only; never classify as PT without allocation evidence |
| Debit in June of the following year | May be settlement, arrears or another liability; confirm allocation |
| VAT, SSC, CLASS 2, FSS, PENALTY, INTEREST | Not PT |

Post confirmed PT as an income-tax payment, then reconcile to the tax account. Any deduction question belongs in the income-tax computation: Check this point with one of our partner accountants.

## Worked cases

### Case 1: benchmark and the 2026 instalments

The 2024 self-assessment (YA 2025) shows tax payable of EUR 3,000 after taking into account EUR 6,000 of PT. Benchmark EUR 9,000. Instalments EUR 1,800 (30 April 2026), EUR 2,700 (31 August 2026), EUR 4,500 (21 December 2026). If the 2026 self-assessment shows EUR 11,500, nothing was deducted at source and no PT is first applied to additional tax, EUR 2,500 is due by the ordinary statutory settlement date, 30 June 2027.

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

- **Overpayment.** PT paid EUR 10,000, tax EUR 7,200: provisional arithmetic excess EUR 2,800, assuming no additional-tax appropriation or other adjustment. Entitlement, due date and interest depend on the article 48 conditions below; do not promise a payment date from these inputs alone.
- **Rent excluded.** Benchmark year: EUR 3,000 tax in the return, plus EUR 1,500 paid on TA24 rent. Assuming EUR 3,000 is already the rule 6 benchmark with ordinary PT added back and the final-rent option is valid, PT is EUR 600, EUR 900, EUR 1,500; separate final-rent tax is not added.
- **Reduction form.** Benchmark EUR 1,000, estimate EUR 800: if the prescribed option is exercised before the affected instalments, rule 10 minimum payments are EUR 200, EUR 300, then EUR 300 (the last payment is the lower of EUR 500 and EUR 800 less EUR 500 already paid). If revised upward, rule 12 applies retrospectively; the estimate is not a final liability.

## When to refuse or refer

| Code | Trigger | Message |
|---|---|---|
| R-MT-PT-1 | Company or partnership PT beyond the benchmark rule, group or merger cases | "Check this point with one of our partner accountants." |
| R-MT-PT-2 | Non-resident PT | "Check this point with one of our partner accountants." |
| R-MT-PT-3 | Disputing PT additional tax or enforcement | "Check this point with one of our partner accountants." |
| R-MT-PT-4 | No benchmark self-assessment and no notice | Stop; do not estimate |

Never: use current-year income as the basis without a reduction form; skip payments because income will drop; split in thirds; include TA24 rent; present figures as final without confirming the operative benchmark; promise a refund date from payment arithmetic alone.

## Filing and payment

Use the official PT notice/tax account for the payment reference and current official payment instructions. No PT1 label or universal MaltaPost/payment-screen workflow is asserted here. Payment allocation or portal steps not established by the notice: Check this point with one of our partner accountants.

Deliver the prescribed reduction form before an instalment it is meant to affect. Rule 10 applies to payments falling due after the option is exercised. The Schedule's printed 1% declaration is historical wording; operative rule 14 gives the 2026 rate of 0.6%. MTCA's general cycle page describes [myTax](https://mytax.mtca.gov.mt/) access with e-ID and a 31 July online deadline; it does not establish a 2027-specific concession. Use the statutory 30 June 2027 settlement/return date unless an applicable official extension is confirmed. The 2027 online concession: Check this point with one of our partner accountants.

An AF1 is MTCA's prescribed further return; under rule 6(2), one filed after the beginning of the month before the first PT instalment is ignored for that benchmark. No general amendment time limit is decided here.

**Refund conditions.** Article 48(1A)/(1B) requires the prescribed outstanding income-tax returns and, for an FSS payer, annual reconciliations/earnings statements, plus VAT returns/declarations where registered. Article 48(2) also restricts refunds in default/incorrect-return cases. For a late return, article 48(2B)(i) uses the later of the last day of the sixth month following filing and the last day of the sixth month following the otherwise applicable refund date. If outstanding returns blocked payment, article 48(2B)(ii) sets the due date at the last day of the sixth month following their filing. Article 48(2C) permits deduction of tax, additional tax and interest due. Refund interest under article 48(2D) runs from the resulting due date, capped at the repayment. Article 48(8) makes the refund payable no later than fourteen days after it becomes due, with a possible further twelve months for due-diligence verification. MTCA additionally asks for updated bank details and all applicable income-tax/VAT returns. Individual entitlement/timing, defaults or disputed offsets: Check this point with one of our partner accountants. ([Cap. 372 art. 48](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b); [S.L. 372.16 rule 6](https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2).)

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
| Read S.L.372.18 rules 2–14 and Schedule (who pays, dates, 20/30/50, benchmark, fallbacks, new taxpayers, reduction, 0.6% additional tax, 90% cut, settlement date) | https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 | 2026-11-26 |
| S.L.372.28 rule2; completed 26Nov Class2 audit source read reused for unchanged interest rule | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-26 |
| Read Cap.372 arts42,44(1)–(2D),48(1)–(2D),48(8) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-26 |
| Read for MTCA Tax Return Cycle (30 June settlement, 31 July online, refund by 31 December, 0.6%) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-26 |
| Read for MTCA Manual on the Taxation of Rental Income (PT on rent declared in the return; 30 April, 31 August, 21 December) | https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf | 2026-11-26 |

| Read S.L.372.16 rules2,5,6 (ordinary individual statutory settlement/refund dates) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-26 |
| Read Cap.123 article31D(2)–(4), final-rent separation from ordinary individual chargeable income | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-26 |

Not yet confirmed: no unsupported claim remains usable. PT1 naming, payment-screen/MaltaPost details, any2027 online concession, individual refund determinations and the original company/nonresident/dispute cases are explicitly referred. The2019 booklet is not used as operative authority.
