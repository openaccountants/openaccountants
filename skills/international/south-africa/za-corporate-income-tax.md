---
name: za-corporate-income-tax
description: "South African corporate income tax for companies and close corporations, for years of assessment ending 1 April 2026 to 31 March 2027, under the Income Tax Act 58 of 1962 and the Tax Administration Act 28 of 2011. Covers residence, the flat 27% company rate, the small business corporation (SBC) bands and qualifying tests, SBC allowances, the assessed loss cap (higher of R1 million and 80% of taxable income), provisional tax, the underestimation and late-payment penalties, interest, the ITR14, fixed administrative penalties, dividends tax and withholding on payments to non-residents. Trigger on: South Africa company tax, CIT rate South Africa, SBC tax rates, small business corporation, ITR14, IRP6 company, provisional tax company, assessed loss 80%, Pty Ltd tax, close corporation tax. Out of scope: individuals (za-income-tax), payroll and UIF/SDL (za-payroll-paye-uif-sdl), VAT (za-vat-return), turnover tax for micro businesses, transfer pricing (south-africa-transfer-pricing)."
version: 0.1
jurisdiction: ZA
tax_year: 2026
last_updated: 2026-10-29
category: international
tier: 2
---

# South African corporate income tax: 2026/27 rates, SBC bands, losses, provisional tax and filing

The law is the Income Tax Act 58 of 1962 ("ITA"). Penalties and procedure come from the Tax Administration Act 28 of 2011 ("TAA"). This skill reads the SARS-provided consolidation of both Acts (the ITA as updated to Government Gazette 55220 of 19 August 2026) and SARS's own rate pages. The South African Revenue Service (SARS) administers the tax through eFiling. The currency is the rand (R).

**Tax year.** A company's year of assessment is its financial year. The figures here apply to **years of assessment ending on any date from 1 April 2026 to 31 March 2027**. SARS calls this the 2026/27 year; for a February year end it is the "2027" year of assessment (1 March 2026 to 28 February 2027). The 25 February 2026 Budget left the company rate unchanged and moved the SBC 0% band from R95 750 to R99 000. A rate change announced in the Budget takes effect from the announced date for 12 months, subject to Parliament enacting it (ITA s5(2)).

## Who this applies to

- **Resident companies.** A person other than a natural person is resident if it is incorporated, established or formed in South Africa, or has its place of effective management in South Africa (ITA s1, "resident" para (b)). A company that a tax treaty deems exclusively resident in the other country is not resident. Residents are taxed on worldwide income.
- **Non-resident companies** with South African-source income, typically through a branch. Passive income paid to non-residents is mostly taxed by withholding; see "Cross-border points".
- **Close corporations and co-operatives** are companies for this purpose and pay the same rates.
- **Personal service providers** are no longer taxed under a separate rate. They pay tax as a company or trust (SARS rates page). A personal service provider can never be an SBC (s12E(4)(a)(iv)).

Not covered here, refer to a specialist: mining and long-term insurers (special formulas); REITs; headquarter companies; Special Economic Zone companies (SARS says approved SEZ companies may qualify for a 15% rate, subject to requirements; the qualifying rules were not read); Global Minimum Tax (Pillar Two); controlled foreign companies; reorganisation rules (ss41–47); the R&D allowance; turnover tax for micro businesses; transfer pricing (see south-africa-transfer-pricing).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Company rate (all companies other than SBCs and special regimes) | 27% of taxable income | YAs ending 1 Apr 2026 – 31 Mar 2027 (same since YAs ending on or after 31 Mar 2023; 28% before) | SARS, Companies, Trusts and SBC rates page; SARS Budget 2026 FAQs |
| SBC band 1 | 0% on R0 – R99 000 | YAs ending 1 Apr 2026 – 31 Mar 2027 | SARS rates page |
| SBC band 2 | 7% of taxable income above R99 000, up to R365 000 | same | SARS rates page |
| SBC band 3 | R18 620 + 21% of taxable income above R365 000, up to R550 000 | same | SARS rates page |
| SBC band 4 | R57 470 + 27% of taxable income above R550 000 | same | SARS rates page |
| SBC bands, prior year | 0% to R95 750; 7% above R95 750; R18 848 + 21% above R365 000; R57 698 + 27% above R550 000 | YAs ending 1 Apr 2025 – 31 Mar 2026 | SARS rates page |
| SBC gross income ceiling | R20 million a year (pro rata by months if trading less than 12 months) | current | ITA s12E(4)(a)(i) |
| SBC investment and personal service income limit | not more than 20% of all non-capital receipts and accruals plus capital gains | current | ITA s12E(4)(a)(iii) |
| Assessed loss set-off cap (companies) | the higher of R1 million and 80% of taxable income before s20 | current | ITA s20(1)(a)(i) |
| Dividends tax | 20% of dividends paid | current | ITA s64E(1)(a) |
| Interest on late or underpaid tax | 10.25% a year from 2 March 2026 | from 2 Mar 2026 | SARS Budget 2026 FAQs |
| Interest on refunds of overpaid provisional tax | 6.25% a year from 2 March 2026 | from 2 Mar 2026 | SARS Budget 2026 FAQs |
| Provisional tax underestimation penalty | 20% of the shortfall (see "Penalties") | current | ITA Fourth Schedule para 20(1) |
| Late provisional tax penalty | 10% of the amount not paid | current | ITA Fourth Schedule para 27(1) |

**SBC band formula.** For taxable income `TI` in a year ending 1 April 2026 to 31 March 2027:

- `TI <= 99 000`: tax 0
- `99 000 < TI <= 365 000`: `(TI - 99 000) x 7%`
- `365 000 < TI <= 550 000`: `18 620 + (TI - 365 000) x 21%`
- `TI > 550 000`: `57 470 + (TI - 550 000) x 27%`

The fixed amounts are the tax on the band below: 266 000 x 7% = 18 620, and 18 620 + 185 000 x 21% = 57 470.

## The taxable base

**Who is an SBC (s12E(4)(a)).** All four tests must be met for the whole year of assessment:

1. It is a close corporation, co-operative, private company or personal liability company, and **every shareholder or member is a natural person at all times** during the year.
2. **Gross income does not exceed R20 million.** If it traded for less than 12 months, reduce the R20 million in proportion to the months traded (a part month counts as a full month).
3. **No shareholder or member holds shares or any equity interest in any other company** at any time in the year. Allowed exceptions include listed shares, collective investment scheme portfolios, less than 5% of certain co-operatives and co-operative banks, friendly societies, s12J venture capital companies, a company that has never traded and owned assets worth no more than R5 000, and a company that has taken liquidation or deregistration steps under s41(4).
4. **Not more than 20%** of all non-capital receipts and accruals plus capital gains is investment income and income from rendering a personal service, taken together. "Investment income" covers dividends, foreign dividends, royalties, rent from immovable property, annuities, interest (s24J) and proceeds from investing or trading in financial instruments, marketable securities or immovable property (s12E(4)(c)). "Personal service" means listed professional services (for example accounting, consulting, engineering, IT, law and management) performed personally by a holder of an interest or a connected person, unless the company employs three or more full-time unconnected employees in that service throughout the year (s12E(4)(d)). The company must not be a personal service provider.

A company that fails any test pays the flat 27% for that year.

**SBC allowances (s12E).** An SBC may deduct 100% of the cost of plant or machinery used directly in a process of manufacture (or a similar process) in a trade other than mining or farming, in the year it is first brought into use (s12E(1)). For its other s11(e) wear-and-tear assets it may elect 50% in the first year, 30% in the second and 20% in the third (s12E(1A)). Cost is the lesser of actual cost and an arm's-length cash price including direct installation cost (s12E(2)). No s12E deduction is allowed on an asset that received the s12BA renewable-energy deduction (s12E(3B)).

**Assessed losses (s20).**

- An assessed loss is the amount by which s11 deductions exceed income (s20(2)). Section 20 sets no time limit on the carry-forward. The set-off is against income "from carrying on any trade" (s20(1)); the rule that lets a person carry a loss forward in a year with no income (s20(2A)(b)) applies only to persons other than companies.
- A company (other than a mining company, which has its own version) may set off a balance of assessed loss brought forward only up to the **higher of R1 million and 80% of taxable income** worked out before s20 (s20(1)(a)(i)). The excess carries forward.
- The cap does not apply to a company that has taken steps under s41(4) to liquidate, wind up or deregister, unless it withdraws them (proviso to s20(1)(a)).
- A loss from a trade carried on outside South Africa cannot be set off against South African-source income (s20(1), proviso (b)).

**Dividends received** are exempt from normal tax under s10(1)(k)(i), except dividends from a headquarter company and the dividends listed in its provisos (for example most REIT dividends). A dividend (other than a distribution of an asset in specie) whose beneficial owner is a resident company is exempt from dividends tax (s64F(1)(a)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Provisional tax, first payment (IRP6) | within 6 months after the start of the year of assessment: half of the estimated normal tax for the year, less employees' tax and the s6quat foreign tax rebate | ITA Fourth Schedule para 23(1)(a) |
| Provisional tax, second payment (IRP6) | by the last day of the year of assessment: the full estimated tax less the first payment (and less employees' tax and the s6quat rebate) | para 23(1)(b) |
| First payment skipped | when the year of assessment is 6 months or shorter | para 23(2) |
| Voluntary additional (top-up) payment | an optional extra payment to avoid or reduce s89quat interest on underpaid provisional tax. That interest runs from the "effective date": seven months after year end for a company with a February year end, six months after year end otherwise. It applies only where a company's taxable income exceeds R20 000 | para 23A(1); ITA s89quat(1)–(2) |
| Company income tax return (ITR14) | within 12 months after the company's financial year end, on eFiling | SARS FAQ, When must the ITR14 return be submitted |
| Record keeping | five years from the date the return is submitted (longer while an audit, objection or appeal is open) | TAA ss29(3)(a), 32 |

Worked dates for a 28 February 2027 year end: first payment by 31 August 2026, second payment by 28 February 2027, s89quat effective date 30 September 2027, ITR14 by 28 February 2028.

## Penalties and interest

- **Late provisional tax:** a 10% penalty on any amount not paid in time under para 23 (or para 25(1)), imposed under TAA Chapter 15 (Fourth Schedule para 27(1); TAA s213).
- **Underestimating provisional tax (para 20(1)(a)), taxable income above R1 million.** If the company's final estimate is less than 80% of its actual taxable income, SARS must impose a penalty of 20% of the difference between:
  - the tax on 80% of the actual taxable income, and
  - the employees' tax and provisional tax paid by the end of the year.
- **Underestimating, taxable income R1 million or less (para 20(1)(b)).** A penalty applies if the final estimate is below 90% of actual taxable income and also below the basic amount: 20% of the difference between the lesser of the tax on 90% of taxable income and the tax on the basic amount, and the employees' and provisional tax paid by year end.
- The para 20 penalty is reduced by any para 27(1) late-payment penalty on the second payment (para 20(2B)). SARS may remit it if the estimate was seriously calculated and not deliberately or negligently understated (para 20(2)).
- **Interest** runs on late or underpaid tax at the prescribed rate: 10.25% a year from 2 March 2026 (SARS Budget 2026 FAQs). Late provisional tax payments carry interest under ITA s89bis(2); a shortfall on assessment carries interest under s89quat(2) from the effective date.
- **Fixed administrative penalty (TAA ss210–211)** applies to non-compliance listed in a Commissioner public notice, other than late payment that carries a percentage penalty. The amount depends on the company's assessed loss or taxable income for the preceding year:

  | Preceding year | Penalty a month |
  |---|---|
  | Assessed loss | R250 |
  | R0 – R250 000 | R250 |
  | R250 001 – R500 000 | R500 |
  | R500 001 – R1 000 000 | R1 000 |
  | R1 000 001 – R5 000 000 | R2 000 |
  | R5 000 001 – R10 000 000 | R4 000 |
  | R10 000 001 – R50 000 000 | R8 000 |
  | Above R50 000 000 | R16 000 |

  The penalty increases by the same amount for each month, or part of a month, that the failure continues more than one month after the penalty assessment. The increases stop after 35 months, or 47 months after the non-compliance if SARS cannot deliver the assessment (s211(2)). A listed company, a company whose gross receipts or accruals for the preceding year exceed R500 million, and a company in a group that includes either, are treated as item (vii) (R8 000) unless they fall in item (viii) or did not trade (s211(3)).

## Cross-border points

- **Residence** turns on incorporation or place of effective management, subject to treaty tie-breakers (s1 "resident" (b)). A company that stops being resident is treated as non-resident from that day.
- **Dividends tax** is 20% of dividends paid by a company other than a headquarter company (s64E(1)(a)). The Minister may announce a different rate in the Budget. Treaty relief can reduce it for non-resident shareholders.
- **Withholding on payments to non-residents** (SARS Budget 2026 FAQs):
  - royalties: 15%, final tax on the gross amount;
  - interest: 15%, final tax (exemptions for interest paid by the government or banks, and on listed debt);
  - foreign entertainers and sportspersons: 15%;
  - disposal of immovable property by a non-resident seller: 10% where the seller is a company.
- **Foreign losses** are ring-fenced from South African-source income (s20(1) proviso (b)).
- **Foreign tax credits** under s6quat reduce provisional tax (para 23(1)). From 28 February 2026 SARS's ITR14 system carries forward foreign tax above the s6quat limit to the next year (SARS Corporate Income Tax page, "System enhancements and legal changes").

## Worked examples

### Example 1: small business corporation, taxable income R420 000

Ndlovu Engineering (Pty) Ltd has a 28 February 2027 year end. Two brothers own all the shares and own no other shares except listed shares. Gross income is R6.4 million. Investment income and personal-service income are under 5% of receipts. Taxable income is R420 000.

- It meets all four SBC tests, so the SBC bands apply.
- R420 000 falls in band 3: R18 620 + (R420 000 - R365 000) x 21% = R18 620 + R11 550 = **R30 170**.
- At the flat 27% the tax would be R113 400. Qualifying as an SBC saves R83 230.
- The edge: if one brother also held 10% of an unlisted company at any time in the year, test 3 fails. The company would then pay 27%, even though nothing else changed.

```oa-check
name: SBC taxable income R420 000, YA ending 28 Feb 2027
inputs:
  ti: 420000
steps:
  - band2_tax: (365000 - 99000) * 0.07
  - band3_tax: band2_tax + (550000 - 365000) * 0.21
  - sbc_tax: band2_tax + (ti - 365000) * 0.21
  - flat_tax: ti * 0.27
  - saving: flat_tax - sbc_tax
expected:
  band2_tax: 18620.00
  band3_tax: 57470.00
  sbc_tax: 30170.00
  flat_tax: 113400.00
  saving: 83230.00
```

### Example 2: company at 27%, assessed loss cap and the underestimation penalty

Karoo Logistics (Pty) Ltd has a 28 February 2027 year end. Its taxable income before s20 is R6 000 000. It brings forward an assessed loss of R5 500 000. Its second provisional estimate was R900 000 of taxable income, and it paid provisional tax of R243 000 (27% of R900 000) by 28 February 2027. It has no employees' tax credits.

- **Loss cap:** the higher of R1 000 000 and 80% x R6 000 000 = R4 800 000. So R4 800 000 is the cap.
- **Loss used:** R4 800 000 of the R5 500 000. R700 000 carries forward to the next year.
- **Taxable income:** R6 000 000 - R4 800 000 = R1 200 000.
- **Normal tax:** 27% = R324 000.
- **Underestimation test:** taxable income is above R1 million, so the 80% test applies. 80% of R1 200 000 is R960 000. The estimate of R900 000 is below that, so a penalty applies.
- **Penalty:** 20% x (tax on R960 000 = R259 200, less R243 000 paid) = **R3 240**.
- **Balance due on assessment:** R324 000 - R243 000 = R81 000, plus s89quat interest on it from the effective date (30 September 2027) unless a top-up is paid before then.

```oa-check
name: Company TI R6m before s20, loss b/f R5.5m, estimate R900 000
inputs:
  ti_before_s20: 6000000
  loss_bf: 5500000
  estimate: 900000
  rate: 0.27
steps:
  - loss_cap: max(1000000, ti_before_s20 * 0.80)
  - loss_used: min(loss_bf, loss_cap)
  - loss_cf: loss_bf - loss_used
  - taxable_income: ti_before_s20 - loss_used
  - normal_tax: taxable_income * rate
  - paid: estimate * rate
  - tax_on_80pct: taxable_income * 0.80 * rate
  - penalty: max(0, (tax_on_80pct - paid) * 0.20)
  - balance_due: normal_tax - paid
expected:
  loss_cap: 4800000.00
  loss_used: 4800000.00
  loss_cf: 700000.00
  taxable_income: 1200000.00
  normal_tax: 324000.00
  paid: 243000.00
  tax_on_80pct: 259200.00
  penalty: 3240.00
  balance_due: 81000.00
```

## Ask the client first

1. Year-end date. It fixes which rate table applies and the provisional tax dates.
2. Who owns the shares, and do any shareholders hold shares in other companies? Gross income and the share of investment and personal-service income. These decide SBC status.
3. The assessed loss brought forward, and whether the company has started liquidation or deregistration steps.
4. Both provisional tax estimates and the amounts paid, with dates.
5. Any foreign income or foreign tax paid, payments to non-residents, and dividends declared.
6. Whether the company is in a special regime: Special Economic Zone, mining, insurance, REIT, headquarter company, micro business on turnover tax, or a multinational group within the scope of the Global Minimum Tax.

## Sources

| Source | URL | Read on |
|---|---|---|
| SARS, Companies, Trusts and Small Business Corporations (SBC) rates (company 27%, SBC bands 2026/27 and 2025/26, trusts, personal service providers) | https://www.sars.gov.za/tax-rates/income-tax/companies-trusts-and-small-business-corporations-sbc/ | 2026-10-29 |
| SARS, Budget 2026 Frequently Asked Questions (CIT 27%, SBC bands, SEZ 15%, interest rates from 2 March 2026, non-resident withholding rates) | https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/ | 2026-10-29 |
| Income Tax Act 58 of 1962, SARS-provided consolidation to GG 55220 of 19 August 2026 (s1 "company" and "resident", s5(2), s10(1)(k), s12E, s20, s64E, s64F, s89bis, s89quat; Fourth Schedule paras 20, 23, 23A, 27) | https://sars.mylexisnexis.co.za/ (linked from https://www.sars.gov.za/legal-counsel/primary-legislation/) | 2026-10-29 |
| Tax Administration Act 28 of 2011, SARS-provided consolidation to GG 54447 of 1 April 2026 (ss29, 32, 210, 211, 213) | https://sars.mylexisnexis.co.za/ (linked from https://www.sars.gov.za/legal-counsel/primary-legislation/) | 2026-10-29 |
| SARS FAQ, When must the ITR14 return be submitted to SARS | https://www.sars.gov.za/faq/faq-when-must-the-itr14-return-be-submitted-to-sars/ | 2026-10-29 |
| SARS, Corporate Income Tax (2 February 2026 system enhancements and legal changes) | https://www.sars.gov.za/types-of-tax/corporate-income-tax/ | 2026-10-29 |

Not yet confirmed:
- The 2026 Rates and Monetary Amounts and Amendment of Revenue Laws Act. The Gazette text was not read. The 2026/27 SBC bands come from SARS's rate pages; under ITA s5(2) a rate change announced in the Budget applies for 12 months subject to Parliament enacting it.
- Whether a late ITR14 is listed in the TAA s210 public notice. The notice was not read.
- The Special Economic Zone rules (s12R).
- The remaining s89quat rules (interest on overpayments, remission); only s89quat(1)–(2) were read.
