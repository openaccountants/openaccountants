---
name: bf-payroll
description: >
  Burkina Faso payroll tax reference for the 2026 tax year, covering employer IUTS salary withholding and the separate employer-funded TPA. Use for monthly salary bands, current housing, function and transport exemptions, pension and professional-expense deductions, benefits in kind, family reductions, monthly remittance and the small-payment half-year option. It explains the statutory payroll records and annual statements, with two executable cases including a remittance-frequency decision. The Guide keeps CNSS and universal health contributions separate and does not certify their rates, the minimum wage or a complete employment-cost calculation. Current electronic forms, boxes and filing acknowledgements still require source confirmation.
jurisdiction: BF
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.1
---

# Burkina Faso payroll (IUTS and TPA) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

IUTS covers public/private salaries, allowances, bonuses and taxable benefits, including the specified company-manager remuneration in art. 105. Art. 107 covers Burkina employees regardless of status/nationality, domiciled employees even where work/employer is abroad, and non-residents where both the paid activity and employer are in Burkina Faso, subject to treaties. Do not confuse the salary tax with [business income](bf-income-tax.md). TPA is an employer tax on employers paying remuneration, subject to art. 227 exemptions. [CGI arts. 105, 107, 227](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

This computes IUTS/TPA only. [Social contributions](bf-social-contributions.md) remains a legacy Guide pending current CNSS/AMU rebuilding. Do not use its old figures as a verified 2026 payroll-cost component.

## Rates, bands and thresholds

| Monthly taxable IUTS income as printed in art. 112, XOF | Marginal rate | Official source |
|---|---|---|
| 0–30,000 | 0% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 30,100–50,000 | 12.10% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 50,100–80,000 | 13.90% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 80,100–120,000 | 15.70% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 120,100–170,000 | 18.40% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 170,100–250,000 | 21.70% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| 250,100 and above | 25% | [CGI art. 112](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

The rate article is **112**, not the old Guide's art. 110. Art. 110 values benefits in kind. The printed scale starts each next band at the next hundred; current administrative handling of an income amount between those printed hundred-unit boundaries is not established here. Do not invent a rounding rule. Cases below use exact hundreds.

| Item and conditions | Amount/rule | Official source |
|---|---|---|
| Housing allowance/benefit exemption | Lower of actual amount, 20% of defined gross salary and XOF 75,000/month | [CGI art. 106(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Function allowance/benefit for qualifying employment expenses expressly provided by text, status or contract | Lower of actual amount, 5% of defined gross salary and XOF 50,000/month | [CGI art. 106(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Transport/travel allowance/benefit exemption | Lower of actual amount, 5% of defined gross salary and XOF 30,000/month | [CGI art. 106(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Actual pension/retirement withholding deduction | Limited to 8% of contractual category base salary, excluding allowances | [CGI art. 111](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Professional-expense deduction | 25% of base salary; 20% for public P/A/B or 6/1/2 and equivalent private senior categories | [CGI art. 111](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Family reduction of calculated IUTS | 1/2/3/4 qualifying charges: 8%/10%/12%/14%; schedule stops at four | [CGI art. 113](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| TPA, unless employer exempt | 3% of total cash remuneration plus valued benefits in kind; CGA member base reduced 20% | [CGI arts. 228–229](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Optional half-year payment, IUTS and separately TPA | Monthly withheld IUTS or TPA amount no more than XOF 5,000; crossing the limit accelerates accumulated amounts | [CGI arts. 116(4), 230](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

## The base

1. Collect contractual category base salary, every allowance, bonus and benefit, actual social/pension withholdings and family evidence. Art. 105 taxes remuneration except its stated public-employer benefit exclusion and art. 106 exemptions. Other art. 106 exclusions include family assistance/allowances, civil/military pensions, qualifying honorary-distinction payments, dismissal compensation excluding notice/paid-leave amounts, retirement departure compensation and reciprocal diplomatic/consular remuneration. Do not extend an exemption beyond its stated payment or payer. [CGI arts. 105–106](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
2. Value benefits at actual cost under art. 110. For an enterprise fixed asset made available to the employee, monthly value is gross balance-sheet value × 5% ÷ 12. The listed benefit categories are leave travel/stay, water/electricity/telecommunications, personal taxes, domestic staff, housing/furnishings, and transport excluding collective transport. [CGI art. 110](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
3. For allowance caps, art. 106 defines gross salary as contractual category base plus all allowances/benefits minus social-contribution withholding. Combine allowance and benefit for the same purpose before its cap, so housing supplied plus housing cash does not receive two exemptions. This gross definition differs from the base-salary denominator for art. 111 deductions.
4. From gross remuneration plus taxable benefits subtract actual pension/retirement withholding up to the art. 111 limit, the professional-expense deduction for the employee's category and the allowed art. 106 franchises. Apply the progressive monthly scale to that net base, then the applicable family reduction (arts. 109–113).
5. A qualifying family charge must have no separate income: minor/infirm children or students younger than twenty-five; fully maintained orphans in the household under the same conditions; and one spouse. A salaried wife is taxed separately and uses charges not already used by the husband. Changes apply from the first day of the following month. Do not double-allocate dependants (art. 113).
6. Calculate TPA separately on total cash pay plus benefits valued as for IUTS, with the CGA base reduction if applicable. Do not apply the IUTS pension, professional or family deductions to the TPA base. Art. 227 exempts the State/local authorities and non-commercial public bodies, SONAPOST, diplomatic missions/organisations, private education/health businesses, nonprofits strictly within their objects, qualifying agricultural mutual credit, mutual/cooperative savings/credit bodies and the currency issuer. Check the exact employer category before using the exemption. [CGI arts. 227–229](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Deadlines and filing

1. Calculate and withhold IUTS monthly (art. 112). Record beneficiary, payment date/nature/amount and withholding in the payroll register/file or special book. Give each affected worker a withholding voucher. Keep the records through the end of the third year after the withholding year and make them available to tax agents (art. 115).
2. Prepare the administration's IUTS declaration and dated/signed payment statement: withholding period; payer designation/address/profession; total withheld. Declare and pay to the competent tax receiver in the first ten days of the next month. The half-year provision expressly defers payment, not a proven waiver of every monthly declaration. If the monthly amount stays at/below the table limit, payment can be in the first ten days of July/January for the elapsed half-year; when one month exceeds it, remit everything accumulated since half-year start by the next month's tenth day (art. 116).
3. Separately declare/pay TPA by the next month's tenth day on its prescribed form. Apply the same threshold/acceleration logic under art. 230. A small IUTS amount does not itself grant TPA deferral, or vice versa.
4. For IUTS, produce the prior-year nominative employer statement **before 30 April**: names, jobs/addresses, compensation/benefits after retirement deductions, period if under a year, dependent children at 31 December, function allowances, housing, transport and tax withheld (art. 117). TPA has its separate annual bases/monthly-payments summary **no later than 30 April** (art. 233).
5. Check special cessation/death timing: IUTS retained amounts are immediate on transfer outside the collection district or cessation/transfer of business; employer death requires payment in the first fifteen days of the next month. TPA is immediate on cessation, or within thirty days after employer death, with separate art. 233 annual-summary rules (arts. 116, 231, 233).

[CGI arts. 112, 115–117, 230–233, 671](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf). Current form names/IDs, boxes, eSINTAX uploads and acknowledgement/payment-reference screens have not been verified. Art. 671 permits specified cash, postal, cheque, bank and electronic methods and requires a regulatory receipt; retain it. A bank order alone does not establish payment by the deadline: the article uses the competent receiver's account credit date for transfer payments.

## Penalties and interest

| Failure and conditions | Statutory consequence | Official source |
|---|---|---|
| IUTS not withheld or insufficiently withheld | 50% of missed withholding plus 1% per month or fraction | [CGI art. 760](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| IUTS withheld, paid within sixty days after deadline | 25% of deferred withholding for each month or fraction | [CGI art. 761(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| IUTS withheld, paid more than sixty days after deadline | 100% plus 1% per month or fraction | [CGI art. 761(2)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| IUTS withheld but no payment | Personal assessment for withheld sums plus 200% and 1% per month or fraction | [CGI art. 761(3)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Breach of arts. 115–117/191 | 25% of evaded duties, minimum XOF 25,000 | [CGI art. 762](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| TPA late declaration / missing or insufficient declaration | 25% / 50% respectively | [CGI art. 769](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Missing annual TPA summary | Fixed XOF 50,000 | [CGI art. 769](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

Choose the factual branch; do not add overlapping penalties without establishing their interaction.

## Cross-border points

For art. 107, domicile follows permanent home, then vital interests, then the stated habitual presence of at least 183 days in twelve months where the previous tests cannot decide; treaty provisions take priority. That is not a standalone 183-day employment exemption. Art. 108 retains the stated domicile rules for paid leave abroad. A Burkina-domiciled recipient of foreign or diplomatic/international-organisation salary must calculate/pay under art. 114 where the employer did not withhold, and supply annual information under art. 118. Year-end total remuneration is regularised under art. 119; excess withholding can be reclaimed before 1 May of the following year. Treaty-specific relief is not established in this Guide. [CGI arts. 107–108, 114, 118–119](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Two worked examples that recompute

**Allowance caps and family reduction.** A non-senior employee has base XOF 200,000, housing XOF 60,000, qualifying function allowance XOF 20,000 and transport XOF 10,000. Actual social withholding is XOF 10,000, all of it a deductible pension contribution, and there are two qualifying family charges. These are inputs, not an assertion of a CNSS rate. Defined gross for exemptions is XOF 280,000. Housing exemption is XOF 56,000, function XOF 14,000 and transport XOF 10,000. After XOF 10,000 pension and XOF 50,000 professional deduction, taxable salary is XOF 150,000. The band tax is XOF 18,390 and IUTS after the 10% family reduction is XOF 16,551. For a non-exempt, non-CGA employer, TPA is XOF 8,700 on all XOF 290,000, with none of those IUTS deductions.

```oa-check
name: Salary exemptions and distinct TPA base
inputs:
  base: 200000
  housing: 60000
  function_allowance: 20000
  transport: 10000
  social: 10000
  pension: 10000
steps:
  remuneration: base + housing + function_allowance + transport
  defined_gross: remuneration - social
  housing_exempt: min(housing, defined_gross * 0.20, 75000)
  function_exempt: min(function_allowance, defined_gross * 0.05, 50000)
  transport_exempt: min(transport, defined_gross * 0.05, 30000)
  taxable: remuneration - min(pension, base * 0.08) - base * 0.25 - housing_exempt - function_exempt - transport_exempt
  band_tax: 20000 * 0.121 + 30000 * 0.139 + 40000 * 0.157 + (taxable - 120000) * 0.184
  iuts: band_tax * 0.90
  tpa: remuneration * 0.03
expected:
  housing_exempt: 56000
  function_exempt: 14000
  transport_exempt: 10000
  taxable: 150000
  band_tax: 18390
  iuts: 16551
  tpa: 8700
```

**Decision: can the employer keep the half-year TPA payment schedule?** January–April TPA is XOF 5,000 monthly. If May remains XOF 5,000 and June likewise, the employer can pay the XOF 30,000 half-year amount by 10 July. If May is XOF 5,001, the threshold is breached and XOF 25,001 for January–May must be paid by 10 June. The extra XOF 1 changes the payment deadline and accumulated cash due. It does not establish permission to omit declarations.

```oa-check
name: TPA half-year threshold decision
inputs:
  earlier_months: 4
  earlier_monthly_tpa: 5000
  may_below: 5000
  may_above: 5001
  june_below: 5000
steps:
  halfyear_payment_if_eligible: earlier_months * earlier_monthly_tpa + may_below + june_below
  accelerated_payment: earlier_months * earlier_monthly_tpa + may_above
  threshold_excess: may_above - 5000
expected:
  halfyear_payment_if_eligible: 30000
  accelerated_payment: 25001
  threshold_excess: 1
```

## Ask the client first

- What category and contractual base salary apply, and what allowances/benefits were actually paid?
- Which social/pension amounts were withheld, and which dependants qualify without double use?
- Where do the employee, employer and paid activity reside/occur, and is there foreign pay?
- Is the employer exempt from TPA or effectively a CGA member?
- What are each tax's monthly totals since half-year start and amounts already paid?
- Is there cessation, transfer, death, paid leave abroad or a year-end adjustment?

## Sources

| Source | Actual reading scope | Read on |
|---|---|---|
| [DGI official CGI 2026](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) | Edition statement; arts. 105–119, 227–233, 671 and 760–762/769, including benefit valuation, dependants, payment acceleration and special cessation/death rules. Relevant provisions read, not the full code. | 2026-11-01 |

Not yet confirmed: current form IDs/boxes, portal submission/acknowledgement workflow; administrative rounding between printed IUTS hundreds and final-tax rounding; SMIG decree/date/current amount; CNSS, voluntary insurance and separate AMU rates/bases/ceilings/deadlines; treaty relief and sanction cumulation. Independent review of this rewrite is pending; no accountant has attested to it.

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
