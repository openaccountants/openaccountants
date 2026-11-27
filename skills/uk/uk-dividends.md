---
name: uk-dividends
description: "UK individual dividend tax for 2026-27, with dated 2024-25 and 2025-26 cases. Covers the dividend allowance, income ordering, director salary and dividends, lawful distributions, close-company loans, foreign credit and reporting. Trigger on: dividend tax UK, dividend allowance, director dividends, salary vs dividends, SA100 dividends, dividend voucher, illegal dividend. Read with uk-income-tax-sa100, uk-national-insurance, uk-corporation-tax and uk-payments-on-account."
version: 1.5
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
source_checked: 2026-11-27
depends_on:
  - uk-income-tax-sa100
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# UK Dividends: income tax on dividends and director pay (2026-27)

## Who this applies to

Individuals receiving dividends outside tax wrappers, including owner-directors. Confirm residence, the tax year, all income, allowances and company facts before computing. Scottish taxpayers use UK dividend rates; Scottish non-savings rates remain separate. ISA dividends are exempt. Pension-wrapper eligibility and withdrawals: Check this point with one of our partner accountants.

Use `uk-income-tax-sa100` for the rest of the income tax computation, `uk-national-insurance` for NIC and `uk-corporation-tax` for company tax. A bank description alone does not establish UK/foreign origin, fund classification, a dividend entitlement or a valid waiver; obtain the voucher and records.

## Rates, bands and thresholds

| Item and conditions | Rate or amount | Year | Official source |
|---|---|---|---|
| Dividend nil-rate allowance per individual, after any Personal Allowance allocation; occupies bands | GBP 500 at 0% | 2024-25, 2025-26, 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A; https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |
| Dividend ordinary / upper / additional rates | 10.75% / 35.75% / 39.35% | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/4; https://www.gov.uk/tax-on-dividends |
| Historical dividend ordinary / upper / additional rates | 8.75% / 33.75% / 39.35% | 2024-25 and 2025-26 | https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |
| Personal Allowance, subject to entitlement and taper | GBP 12,570 | 2024-25 to 2026-27 | https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past |
| Basic rate limit / higher rate limit, income after allowances; eligible pension/Gift Aid extensions can change limits | GBP 37,700 / GBP 125,140 (higher limit derived from s.10(5A)) | 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/10 |
| Category A director from start of tax year: annual primary / secondary / upper earnings limits | GBP 12,570 / GBP 5,000 / GBP 50,270; employee 8% then 2%; employer 15% above secondary threshold | 2026-27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027; https://www.legislation.gov.uk/uksi/2001/1004/regulation/8 |
| Lower earnings limit; pay at/between this and primary threshold can protect the NIC record, not guarantee a complete qualifying year | GBP 129 weekly / GBP 6,708 annually | 2026-27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027; https://www.gov.uk/national-insurance |
| Company small profits / main rates: small rate requires UK residence, not a close investment-holding company, and augmented profits within adjusted lower limit | 19% / 25%; lower GBP 50,000 and upper GBP 250,000 for a full twelve-month period with no associates; shorten/divide limits where applicable | Financial year 2026 | https://www.legislation.gov.uk/ukpga/2025/8/section/13; https://www.legislation.gov.uk/ukpga/2025/8/section/14; https://www.legislation.gov.uk/ukpga/2010/4/section/18A; https://www.legislation.gov.uk/ukpga/2010/4/section/18D |

The ordinary and upper dividend increases are enacted by Finance Act 2026 s.4 for 2026-27 and subsequent years; they are not merely a Budget announcement. Do not apply them to the older cases below.

## The taxable base

**Order and allowances.** Under ITA 2007 s.16, dividends ordinarily sit above savings, which sit above other income. Allocate reliefs/allowances to produce the greatest income-tax reduction, subject to statutory restrictions (s.25); do not assume one allocation is always optimal. For the simple salary-only-plus-dividend cases below, the Personal Allowance is allocated to salary. At GBP 45,000 salary with full standard allowance and no band extensions, GBP 5,270 of basic band remains (50,270 − 45,000).

**The allowance is a rate, not a deduction.** The first GBP 500 of dividends is taxed at the dividend nil rate. Those GBP 500 still count as income and still use up the basic or higher rate band (ITA 2007 s.13A). This refers to dividends remaining after any Personal Allowance allocation. The allowance is per individual and tax year, not per account; there is no spouse transfer or carry-forward. Apply it to ordinary-rate dividend income first, then upper-rate, then additional-rate income. Dividends within unused Personal Allowance are not taxed.

**Computation.** Establish taxable income, reliefs, adjusted net income and allowance entitlement; allocate allowances lawfully; place dividends on top; apply the dividend nil rate, then the correct year's dividend rates to the remaining band slices. Above adjusted net income of GBP 100,000, the Personal Allowance falls by half the excess, with the remaining allowance rounded up to a whole pound; it is nil at GBP 125,140. Taxable dividends enter adjusted net income before Personal Allowance. Child Benefit, student-loan and other threshold interactions: Check this point with one of our partner accountants.

**Classify the receipt.** ITA 2007 s.19 includes UK and non-UK dividends, UK stock dividends, close-company loan releases charged under ITTOIA Part 4 Chapter 6, and relevant foreign distributions. Obtain the voucher rather than classify platform or bank text automatically.

- Authorised unit trusts: where distribution accounts show amounts available for distribution as dividends, s.389 treats a proportionate dividend as paid to unit holders; the approved personal pension scheme exception applies. Accumulation units are not exempt merely because cash is reinvested. Offshore funds, interest distributions and equalisation require separate classification.
- UK scrip replacing cash: income arises to the beneficially entitled individual under ss.410–411; s.412 normally uses the cash alternative, but market value applies if the difference equals or exceeds 15% of market value. Qualifying bonus share capital has its own market-value rule. Use SA101 Additional information for the 2025-26 return, not SA100 box 4; recheck the relevant year's form.
- Ordinary UK REIT property income distributions of exempt profits to an individual are UK property-business income under CTA 2010 s.548, outside dividend rates and allowance. Other distributions must be classified separately. Specialist REIT exceptions and tax withheld: Check this point with one of our partner accountants.
- Corporate bond returns versus dividends, distributions in specie, returns of capital, offshore funds and non-standard stock issues: Check this point with one of our partner accountants.

**Lawful distributions.** Companies Act 2006 s.830 permits distributions only from accumulated realised profits not already distributed/capitalised, less accumulated realised losses not written off as provided there. A current trading loss alone does not prohibit a dividend if sufficient distributable reserves remain. Under s.836, justify it using the relevant annual, interim or initial accounts complying with the applicable requirements. Under s.847 a member who knew or had reasonable grounds to believe a distribution contravened Part 23 is liable to repay it (or the relevant value for a non-cash distribution). Do not presume every director's knowledge. Other company-law restrictions and formalities: Check this point with one of our partner accountants. Keep the dividend voucher and declaration records.

**Salary versus dividends.** Genuine remuneration and employer NIC incurred wholly and exclusively for the trade can be deductible; remuneration timing restrictions apply (CTA 2009 ss.54, 1288). Dividends are ordinarily not deductible (s.1305). Genuine dividends carry no NIC; reclassification or employment-related arrangements are not covered by that statement. Salary payroll obligations apply; see `uk-national-insurance`.

For a category A director from the start of 2026-27, no other income and full Personal Allowance, GBP 12,570 salary gives no salary income tax or employee NIC, but employer NIC before relief is 15% × (12,570 − 5,000) = GBP 1,135.50. Salary GBP 5,000 creates no employer NIC on those annual facts. Pay below the lower earnings limit does not itself protect the NIC record; credits or other contributions may still do so. Do not infer a State Pension qualifying year from salary alone. Employment Allowance is unavailable on the sole-director/only employee liable for secondary Class 1 facts below; check other cases separately.

The following are **derived marginal illustrations per GBP 1 of company cost in 2026-27**, assuming England/Wales/Northern Ireland main income-tax rates, category A employee NIC at the stated band, employer NIC at 15% with no allowance, full deduction for salary/employer NIC, and a company whose actual marginal CT rate is exactly 19% or 25%. Ignore allowances, taper, benefit/loan interactions and marginal relief. These are not average extraction rates or an optimal salary recommendation.

Salary tax share = 1 − (1 − income-tax rate − employee-NIC rate) / 1.15. Dividend share = 1 − (1 − CT rate) × (1 − dividend rate).

| Band assumptions | Salary share, derived | Dividend share at 19% CT, derived | Dividend share at 25% CT, derived | Official rate inputs |
|---|---|---|---|---|
| Basic income tax 20%, employee NIC 8% | 37.39% derived | 27.71% | 33.06% | https://www.gov.uk/income-tax-rates; https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027; https://www.gov.uk/tax-on-dividends; https://www.legislation.gov.uk/ukpga/2025/8/section/13; https://www.legislation.gov.uk/ukpga/2025/8/section/14 |
| Higher income tax 40%, employee NIC 2% | 49.57% derived | 47.96% | 51.81% | same |
| Additional income tax 45%, employee NIC 2% | 53.91% derived | 50.87% | 54.51% | same |

On these assumptions, dividends at 25% marginal CT cost more than salary for higher/additional rates. Recompute on the actual facts; Scottish rates, marginal relief, Employment Allowance and taper can change the decision. Contract, IR35/intermediary, benefit and NIC record questions: Check this point with one of our partner accountants.

**Close-company loans.** Where CTA 2010 s.455 actually applies, the company's charge is tied to the dividend upper rate for the tax year of the loan: 35.75% for 2026-27, due nine months and one day after the lending accounting period ends. Repayment relief under s.458 requires a claim within four years from the end of the financial year of repayment/release/write-off. If repayment/release/write-off occurs on or after the charge's due date, relief cannot be given before nine months after that accounting period ends. Relief may be proportionate. Do not promise that repayment always eliminates tax: exceptions, indirect loans, replacement borrowing and repayment-matching/anti-avoidance require a separate review. Check this point with one of our partner accountants.

A release/write-off where the company is or was chargeable under s.455 can create individual dividend income on the debt released that tax year (ITTOIA ss.415–416; ITA s.19), subject to the settlor-relief exception. The company's relief is separate. Employment NIC, recipient identity and exception/anti-avoidance application: Check this point with one of our partner accountants.

**Dividend waivers.** Deed/timing/validity, entitlement, bounty/settlement tests, retained interest, spouse/civil-partner exceptions and minor-child/other-relative attribution: Check this point with one of our partner accountants. Do not treat every waiver as automatically taxable on the waiving shareholder or assume a class-wide waiver is safe.

## Deadlines and filing

Taxable dividends over the unused Personal Allowance and dividend allowance must be reported. If already sending Self Assessment, include dividend income even below the allowance. A small dividend does not cancel an existing notice to file or another filing obligation.

| Situation | Ordinary action | Official source |
|---|---|---|
| Dividend tax to pay, total dividends up to and including GBP 10,000, not already filing | Notify HMRC after the year ends on 5 April and before 5 October; request a tax-code change or contact the helpline | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |
| Total dividends over GBP 10,000 | Self Assessment; if not usually filing, notify/register by 5 October after the tax year | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |
| Ordinary 2026-27 return and balance, assuming normal timely notice | Paper 31 October 2027; online and balancing payment 31 January 2028. The corresponding 2025-26 dates are one year earlier | https://www.legislation.gov.uk/ukpga/1970/9/section/8; https://www.legislation.gov.uk/ukpga/1970/9/section/59B |

**Forms:** the SA100 2026 is for **2025-26**, not a proven 2026-27 box map. Its box 4 is UK-company dividends; box 5 includes other dividend distributions such as authorised unit trusts; stock dividends use SA101. Box 6 is net foreign dividends up to GBP 500, with tax in box 7, only where the notes' conditions are satisfied. If total UK plus foreign dividends exceed GBP 500 and deduction relief or Foreign Tax Credit Relief is relevant, use SA106 instead; FIG relief also requires the appropriate supplementary pages. Foreign income, relief elections, the small-income exception and the future 2026-27 form: Check this point with one of our partner accountants.

**Payments on account:** normally half of the preceding relevant Self Assessment amount on each 31 January and 31 July, unless the relevant amount is below GBP 1,000 or more than 80% was collected outside Self Assessment. Exactly 80% is not exempt on that test. Excluded charges, reductions, late notices and special collection dates: see `uk-payments-on-account`. For a normal 2026-27 balance, the first 2027-28 instalment is 31 January 2028 and the second 31 July 2028; a rise in dividends does not by itself establish the amount due.

## Penalties and interest

Late-filing, late-payment, notification and inaccuracy penalties depend on the operative regime, HMRC notices, conduct and defences, including MTD commencement and transitional rules. Check this point with one of our partner accountants. Do not apply the former penalty table universally to 2026-27.

Ordinary HMRC late-payment interest was 7.75% from 9 January to 23 November 2026, then 8% from 24 November 2026. Use the rate for each actual period, not a promise about the future January payment. See the dated HMRC rate table in Sources. Unlawful-distribution repayment to the company is separate from a tax penalty.

## Cross-border points

Foreign income, source-country withholding and UK residence/FIG/remittance treatment must be established separately. UK and foreign dividend income generally share the same annual dividend allowance; do not invent one allowance per country.

Foreign Tax Credit Relief is a claim, not an automatic offset of all tax withheld. TIOPA 2010 ss.9, 18, 33 and 36 require qualifying foreign tax, reasonable steps to minimise it under foreign law/treaty and the source-specific UK tax limit. No UK tax on the income means no foreign credit for it. Tax above an applicable treaty limit must be addressed with the foreign authority. FIG-relieved income cannot also receive FTCR. Do not assume credit and deduction relief can both be used for the same source. Country rates (including US/W-8BEN), exchange-rate selection, credit allocation across sources and non-resident UK withholding: Check this point with one of our partner accountants. See `uk-foreign-tax-and-withholding` and `uk-non-resident-sa109`.

## Worked examples

These are illustrative computations, rounding each displayed tax component to pennies. Actual return/software rounding and relief claims require the year's instructions. Unless stated otherwise, assume full Personal Allowance, no band extensions/other reliefs, no other income or threshold charges and ordinary UK tax treatment outside wrappers.

### Example 1: Priya, England, salary GBP 45,000 and dividends GBP 10,000, 2026-27

Taxable salary is GBP 32,430; the remaining basic band is GBP 5,270. The GBP 500 nil-rate dividend uses band. Tax on the next GBP 4,770 is GBP 512.78 and on the remaining GBP 4,730 is GBP 1,690.98: displayed component sum GBP 2,203.76. Before component rounding the total is GBP 2,203.75. Total dividends are not over GBP 10,000: if not otherwise required to file, notify HMRC after 5 April and before 5 October 2027 for its collection route; being at this boundary is not an unconditional exemption from filing.

```oa-check
name: GB 2026-27, salary 45000 and dividends 10000, England
inputs:
  salary: 45000
  dividends: 10000
  personal_allowance: 12570
  basic_band: 37700
  dividend_allowance: 500
steps:
  - band_left: basic_band - (salary - personal_allowance)
  - nil_slice: min(dividend_allowance, dividends)
  - basic_slice: max(min(dividends, band_left) - nil_slice, 0)
  - higher_slice: dividends - nil_slice - basic_slice
  - basic_tax: round(basic_slice * 0.1075, 2)
  - higher_tax: round(higher_slice * 0.3575, 2)
  - dividend_tax: basic_tax + higher_tax
expected:
  band_left: 5270
  basic_slice: 4770
  higher_slice: 4730
  basic_tax: 512.78
  higher_tax: 1690.98
  dividend_tax: 2203.76
```

### Example 2: sole director, salary GBP 12,570, company profit GBP 60,000, 2026-27

Retain the original one-director/only-employee facts. Assume the director is category A from the start of the tax year, remuneration/NIC are wholly for the trade and paid/deductible in the period, and the company is a UK-resident trading company, not a close investment-holding company. Its full twelve-month period is 1 April 2026–31 March 2027, no associates or other augmented profits/adjustments; distributable reserves and declaration cover the payment.

Employer NIC is GBP 1,135.50 with no Employment Allowance. Taxable/augmented profits are GBP 46,294.50, within the lower limit; CT at 19% is GBP 8,795.96 and dividends GBP 37,498.54. Salary uses the Personal Allowance, leaving the full basic band for dividends. Dividend tax is GBP 3,977.34, giving total company/NIC/dividend tax GBP 13,908.80, or 23.18% of original profit. Salary plus dividends is GBP 50,068.54 before dividend tax, **GBP 46,091.20 after it**. Ordinarily file and pay the 2026-27 balance by 31 January 2028, crediting any prior payments; payments on account are separate.

```oa-check
name: GB 2026-27, director salary 12570 plus dividends, company profit 60000
inputs:
  profit: 60000
  salary: 12570
  secondary_threshold: 5000
  dividend_allowance: 500
  basic_band: 37700
steps:
  - employer_nic: (salary - secondary_threshold) * 0.15
  - taxable_profit: profit - salary - employer_nic
  - corporation_tax: round(taxable_profit * 0.19, 2)
  - dividends: taxable_profit - corporation_tax
  - dividend_tax: round((min(dividends, basic_band) - dividend_allowance) * 0.1075, 2)
  - total_tax: corporation_tax + employer_nic + dividend_tax
  - extracted: salary + dividends
  - share_of_profit_pct: round(total_tax / profit * 100, 2)
expected:
  employer_nic: 1135.50
  taxable_profit: 46294.50
  corporation_tax: 8795.96
  dividends: 37498.54
  dividend_tax: 3977.34
  total_tax: 13908.80
  extracted: 50068.54
  share_of_profit_pct: 23.18
```

### Dated original cases restored from the earlier versions

- **Old Example 1, 2025-26; also the original prior-year 2024-25 rate scenario:** salary GBP 30,000, dividends GBP 8,000, no other income. Total GBP 38,000; salary taxable GBP 17,430, salary tax GBP 3,486; basic band left GBP 20,270. Nil-rate GBP 500, then GBP 7,500 × 8.75% = **GBP 656.25**. **Old Example 1b, 2026-27**, identical inputs: dividend tax **GBP 806.25**, an increase of **GBP 150**. No input/year is rolled forward.
- **Old Example 2, 2025-26** (the original historical rate scenario also matches 2024-25): salary GBP 48,000, UK dividends GBP 10,000. Salary taxable GBP 35,430; band left GBP 2,270. After GBP 500 nil-rate, GBP 1,770 × 8.75% = GBP 154.88 and GBP 7,730 × 33.75% = GBP 2,608.88: displayed sum **GBP 2,763.76** (unrounded aggregate GBP 2,763.75).
- **Old Example 3, 2024-25 director illustration:** original inputs were company profit GBP 60,000, salary GBP 12,570 and a **stipulated 25% CT rate**, with employer NIC 13.8% above GBP 9,100. On annual director/category A facts and deductible pay/NIC, recomputation gives NIC **GBP 478.86**, taxable profit **GBP 46,951.14**, CT **GBP 11,737.79**, dividends **GBP 35,213.35**, dividend tax **GBP 3,037.42**, total tax **GBP 15,254.07** (25.42%), extraction before personal tax **GBP 47,783.35**, after tax **GBP 44,745.93**. The old GBP 479 rounding and 24.2% result are not exact computations. This preserves the historical stipulated rate; it does **not** establish entitlement to 25% rather than small-rate/marginal-relief treatment. The case's missing company facts: Check this point with one of our partner accountants. The later 2026-27 replacement is Example 2 above.
- **Old Example 4, US dividends:** original USD 5,000 gross = GBP 3,950; stated 15% = USD 750 tax, supplied GBP 593; higher-rate UK income with the whole GBP 500 allowance available. At the same implied GBP 0.79 per USD, USD 750 equals **GBP 592.50**, so GBP 593 is a supplied rounded figure, not an exact conversion. Conditional on GBP 593 being the established admissible credit and all dividends remaining in the upper band, 2026-27 gross UK tax is GBP 1,233.38 and balance **GBP 640.38**; the original 2024-25/2025-26 rate version gives GBP 1,164.38 and **GBP 571.38**. If the admissible credit is GBP 592.50, the balances are **GBP 640.88 / GBP 571.88** respectively. The older GBP 1,333.13 gross-before-allowance figure less GBP 168.75 illustrates the older rate only. This is conditional arithmetic, not proof of treaty entitlement or filing rounding. Exchange-rate choice, allowable tax, source-specific UK cap and US treaty/rounding application: Check this point with one of our partner accountants.

Historical marginal comparison, **2024-25**, per GBP 1 and assuming full salary/NIC deduction, employer NIC 13.8%, ordinary employee NIC 8%/2%, main income tax 20%/40%/45% and **stipulated marginal CT 25%**: salary shares recompute to **36.73% / 49.03% / 53.43%**, dividend shares **31.56% / 50.31% / 54.51%**. The older approximate basic/higher figures are superseded. In 2026-27 the higher dividend share becomes **51.81%**, not 51.78%. Original salary alternatives GBP 9,100 (2024-25) and GBP 5,000 (2026-27) are not universal optimums; old LEL GBP 6,396 (2024-25) does not guarantee a full qualifying year. At 25% deductible CT the salary-only tax reduction on GBP 12,570 is GBP 3,142.50, not an exact GBP 3,143; actual eligibility/rate must be established.

## Ask the client first

- Tax year, residence/Scottish status, all income, reliefs and adjusted-net-income inputs.
- Vouchers, cash/stock/fund/PID classification, wrapper status and beneficial entitlement; do not infer from bank labels.
- Company residence, trade, twelve-month/short period, associates, augmented profit, deduction timing, reserves, pay periods, director appointment, NIC category and Employment Allowance facts.
- Foreign gross income and tax in original currency and sterling, conversion evidence, treaty entitlement and any FIG/remittance claim.
- Existing filing notices, prior Self Assessment tax/credits/payments on account; any loan balance, repayment/reborrowing or waiver.

## Sources

Read dates below identify exact provisions/paragraphs read, including completed reads reused after confirming the unchanged claim applies. No download/status code is treated as a source read.

| Source and part read | Official URL | Read date |
|---|---|---|
| ITA dividend nil-rate steps, income ordering/definition and allowance allocation: ss.13A, 16, 19, 25 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A; https://www.legislation.gov.uk/ukpga/2007/3/section/16; https://www.legislation.gov.uk/ukpga/2007/3/section/19; https://www.legislation.gov.uk/ukpga/2007/3/section/25 | 2026-11-27, operative sections read |
| FA2026 s.4 enactment and commencement | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-11-27, s.4 read |
| HMRC current/past dividend, allowance and income band rows | https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past | 2026-11-27, 2024-25 through 2026-27 rows read |
| HMRC tax on dividends, ISA and reporting paragraphs | https://www.gov.uk/tax-on-dividends; https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends | 2026-11-27, main text read |
| ITA ss.10, 35, 58: bands, allowance entitlement/taper and ANI; main rates | https://www.legislation.gov.uk/ukpga/2007/3/section/10; https://www.legislation.gov.uk/ukpga/2007/3/section/35; https://www.legislation.gov.uk/ukpga/2007/3/section/58; https://www.gov.uk/income-tax-rates; https://www.gov.uk/scottish-income-tax | 2026-11-26 completed SA100 reads reused; applicability 2026-11-27 |
| ITTOIA ss.389, 410–412: authorised trust and UK stock dividends | https://www.legislation.gov.uk/ukpga/2005/5/section/389; https://www.legislation.gov.uk/ukpga/2005/5/section/410; https://www.legislation.gov.uk/ukpga/2005/5/section/411; https://www.legislation.gov.uk/ukpga/2005/5/section/412 | 2026-11-27, all sections read |
| CTA2010 s.548 REIT distribution character and exceptions | https://www.legislation.gov.uk/ukpga/2010/4/section/548 | 2026-11-27, s.548 read |
| Companies Act ss.830, 836, 847: distributable profits, relevant accounts, unlawful distribution | https://www.legislation.gov.uk/ukpga/2006/46/section/830; https://www.legislation.gov.uk/ukpga/2006/46/section/836; https://www.legislation.gov.uk/ukpga/2006/46/section/847 | 2026-11-27, all sections read |
| CTA2009 ss.54, 1288, 1305: trade purpose, remuneration timing, dividend non-deduction | https://www.legislation.gov.uk/ukpga/2009/4/section/54; https://www.legislation.gov.uk/ukpga/2009/4/section/1288; https://www.legislation.gov.uk/ukpga/2009/4/section/1305 | 2026-11-27, all sections read |
| HMRC extraction guidance: payroll, dividends, no NIC, voucher | https://www.gov.uk/running-a-limited-company/taking-money-out-of-a-limited-company | 2026-11-27, salary/dividend paragraphs read |
| NIC annual-director period, current/historical rates and record protection; Employment Allowance | https://www.legislation.gov.uk/uksi/2001/1004/regulation/8; https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027; https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025; https://www.gov.uk/national-insurance; https://www.gov.uk/claim-employment-allowance/eligibility | 2026-11-26 completed NI reads reused; applicability 2026-11-27 |
| FY2026 CT rates and small-rate gateway/limits, FA2025 ss.13–14 and CTA2010 ss.18A–18E | https://www.legislation.gov.uk/ukpga/2025/8/section/13; https://www.legislation.gov.uk/ukpga/2025/8/section/14; https://www.legislation.gov.uk/ukpga/2010/4/section/18A; https://www.legislation.gov.uk/ukpga/2010/4/section/18D; https://www.legislation.gov.uk/ukpga/2010/4/section/18E | 2026-11-26 completed CT reads reused; applicability 2026-11-27 |
| CTA2010 ss.455, 458 and ITTOIA ss.415–416: loan charge, claim and release | https://www.legislation.gov.uk/ukpga/2010/4/section/455; https://www.legislation.gov.uk/ukpga/2010/4/section/458; https://www.legislation.gov.uk/ukpga/2005/5/section/415; https://www.legislation.gov.uk/ukpga/2005/5/section/416 | 2026-11-27, all sections read |
| TIOPA ss.9, 18, 33, 36: unilateral credit, entitlement, minimisation and cap | https://www.legislation.gov.uk/ukpga/2010/8/section/9; https://www.legislation.gov.uk/ukpga/2010/8/section/18; https://www.legislation.gov.uk/ukpga/2010/8/section/33; https://www.legislation.gov.uk/ukpga/2010/8/section/36 | 2026-11-27, all sections read |
| SA100 2026, TR3 boxes; SA150 TRG6 classification and foreign exception | https://assets.publishing.service.gov.uk/media/69c14d07cfa346b9d4704a8d/SA100-2026.pdf; https://assets.publishing.service.gov.uk/media/6a9ea8a5df4246cf45e469e0/SA150_Notes_2026.pdf | 2026-11-27, specified boxes/notes read; applies to 2025-26 |
| SA106 notes 2026, FTCR and dividend paragraphs; notes 2025 historical rates | https://assets.publishing.service.gov.uk/media/69bbd6144c478213a823ce14/SA106_Notes_2026.pdf; https://assets.publishing.service.gov.uk/media/67da810fa87d546feeda01d7/sa106_Notes_2025.pdf | 2026-11-27, specified paragraphs read for 2025-26/2024-25 |
| Ordinary return/balance/instalment dates, TMA ss.8, 59A, 59B | https://www.legislation.gov.uk/ukpga/1970/9/section/8; https://www.legislation.gov.uk/ukpga/1970/9/section/59A; https://www.legislation.gov.uk/ukpga/1970/9/section/59B; https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-26 completed SA100/POA reads reused; applicability 2026-11-27 |
| HMRC dated ordinary late-payment interest table | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22 completed UK bookkeeping read reused; 24 November effective-date applicability confirmed 2026-11-27 |

Not yet confirmed: the individually identified referred points above are non-usable holds, not assumed exemptions or permissions. Check this point with one of our partner accountants.
