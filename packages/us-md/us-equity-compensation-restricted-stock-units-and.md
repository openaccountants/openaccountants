---
name: us-equity-compensation-restricted-stock-units-and
description: Compute and withhold US federal tax on equity pay for tax year 2026 - restricted stock and the 30-day section 83(b) election, restricted stock units, nonstatutory and incentive stock options, the 22% optional and 37% mandatory flat rates on supplemental wages above $1 million, the $184,500 social security wage base and Additional Medicare Tax, the 2026 AMT on an ISO exercise with the 50% exemption phase-out from Public Law 119-21 ($90,100 single exemption, $500,000 phase-out start), the Form 1099-B basis trap on Form 8949, and the section 83(i) deferral election for private companies. Trigger on "RSU tax", "stock options tax", "ISO AMT", "83(b) election", "supplemental wage withholding", "sell to cover", "83(i)". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Equity compensation, tax year 2026: RSUs, stock options, supplemental wage withholding, ISO AMT and the section 83(i) election

> **Source-cited draft.** Built from IRS Pub. 15 (2026), Pub. 15-T (2026), Pub. 15-B (2026), Rev. Proc. 2025-32, Public Law 119-21 section 70107, 26 U.S.C. 53, 55, 56, 83 and 422, Treas. Reg. 1.61-2, 1.83-3, 1.83-4 and 31.3402(g)-1, Notice 2018-97, IRS Pub. 525 (2025), Topic 427 and the Instructions for Forms 6251, 8949 and 3921, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** RSU settlements and NSO exercises are **supplemental wages**: the employer may withhold a flat **22%** while the employee's supplemental wages for the year stay at or under **USD 1 million**, and must withhold **37%** on the excess. Social security applies up to the **USD 184,500** wage base, Medicare at **1.45%** with no cap, plus **0.9%** Additional Medicare Tax withholding over **USD 200,000**. A large vest withheld at 22% often leaves tax unpaid (Case 2). Restricted stock lets the employee elect under **section 83(b) within 30 days** of transfer to be taxed at grant. An ISO exercise is not regular income but is an **AMT adjustment**; for 2026 the exemption (**USD 90,100** single, **USD 140,200** joint) phases out at **50%** above **USD 500,000** (USD 1,000,000 joint), twice as fast as in 2025, so AMT bites sooner (Case 1). Always correct the Form 1099-B basis on Form 8949, or the same income is taxed twice.

## Scope and who this is for

In scope: employees and founders who hold restricted stock, RSUs, NSOs or ISOs, and their advisers; and employers and their payroll agents that transfer stock to employees for services or settle RSUs or options in stock, operating chapter 24 withholding and reporting on Form W-2 and Form 941. The section 83(i) part applies only where the corporation is an eligible corporation and the individual a qualified employee.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Sale of the shares and capital gain rates | `us-capital-gains` |
| Section 1202 exclusion for founders' stock | `us-section-1202-qsbs` |
| The employer's Form 941 and Form 940 filings and deposits | `us-form-941-940-payroll` |
| Estimated tax to cover a withholding shortfall | `us-quarterly-estimated-tax` |
| Wider 2026 changes | `us-2026-federal-tax-changes` |
| Non-employee service providers, partners, equity in a partnership or LLC, state withholding | refer |

## Ask the client first

1. **What is the award:** restricted stock, an RSU, an NSO, an ISO under section 422(b), or an ESPP right under section 423(c)? For an ISO, the grant date and the value at grant against the USD 100,000 first-exercisable limit.
2. **For restricted stock:** the transfer date, and whether a section 83(b) election was filed within 30 days.
3. **Supplemental wages already paid in 2026** by the whole employer group, against USD 1 million, and whether income tax was withheld from regular wages this year or last.
4. **For an ISO:** the spread at exercise, the rest of the 2026 income, and whether the shares will be sold in 2026, within 2 years of grant or within 1 year of exercise.
5. **For section 83(i):** is any stock of the corporation readily tradable, did it buy back stock in 2025, and has the employee ever been CEO or CFO, or a 1-percent owner or one of the 4 highest paid officers in 2026 or the 10 preceding years?
6. **For any sale:** the basis on Form 1099-B, and whether the option was granted before or after 2013.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Optional flat withholding rate on supplemental wages, while the year's supplemental wages from the employer group are not more than USD 1 million (only if income tax was withheld from regular wages this year or last) | 22% | [IRS Pub. 15 (2026), section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Mandatory flat rate on supplemental wages above USD 1 million in the calendar year, regardless of Form W-4 | 37% | [IRS Pub. 15 (2026), section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Calendar-year supplemental wage threshold for the mandatory rate (all businesses under common control count) | USD 1 million | [IRS Pub. 15 (2026), section 7](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security wage base | USD 184,500 | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security tax rate, employee and again employer | 6.2% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Medicare tax rate, employee and again employer, no wage base | 1.45% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Additional Medicare Tax withholding, employee only, on wages over USD 200,000 | 0.9% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Additional Medicare Tax withholding threshold, per employee per calendar year | USD 200,000 | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| AMT exemption, unmarried individuals | USD 90,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption, joint returns or surviving spouses | USD 140,200 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption, married filing separately | USD 70,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption phase-out threshold, unmarried (fully phased out at USD 680,200) | USD 500,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption phase-out threshold, joint (fully phased out at USD 1,280,400) | USD 1,000,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT exemption phase-out threshold, married filing separately (fully phased out at USD 640,200) | USD 500,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess taxable income above which the 28% AMT rate applies (USD 122,250 married filing separately) | USD 244,500 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT rate up to that amount / above it | 26% / 28% | [26 U.S.C. 55(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm) |
| AMT exemption phase-out rate, taxable years beginning after 31 December 2025 | 50% | [Public Law 119-21, section 70107](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Standard deduction, single | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| ISOs first exercisable in a calendar year, by value at grant, per individual, all plans of the employer group | USD 100,000 | [26 U.S.C. 422(d)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm) |
| ISO holding periods: from grant / after transfer of the share | 2 years / 1 year | [26 U.S.C. 422(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm) |
| ISO employment condition: employee from grant until this long before exercise | 3 months | [26 U.S.C. 422(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm) |
| Section 83(b) election deadline after the transfer (irrevocable without IRS consent) | 30 days | [26 U.S.C. 83(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm) |
| Section 83(i) election deadline after the earlier of transferable or vested | 30 days | [26 U.S.C. 83(i)(4)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm) |
| Section 83(i) maximum deferral after the earlier of transferable or vested | 5 years | [26 U.S.C. 83(i)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm) |
| Section 83(i) plan coverage: share of US employees granted options or RSUs with the same rights | not less than 80% | [IRS Pub. 15-B (2026)](https://www.irs.gov/pub/irs-pdf/p15b.pdf) |
| Income tax withholding rate when 83(i) deferred income is included | 37% | [IRS Pub. 15-B (2026)](https://www.irs.gov/pub/irs-pdf/p15b.pdf) |
| Section 83(i) redemption limit: share of the year's buybacks that must be deferral stock | not less than 25 percent | [26 U.S.C. 83(i)(4)(B)(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm) |

Only the part of supplemental wages above USD 1 million is withheld at 37%; the part up to it follows the ordinary supplemental wage rules (the optional 22%, or aggregation with regular wages). Pub. 15-T (2026) says its methods "can't be used if the 37% mandatory flat rate withholding applies or if the 22% optional flat rate withholding is used". Section 70107 of Public Law 119-21 also removed the end date of the higher exemption amounts and indexes the USD 1,000,000 joint threshold only for taxable years beginning after 2026, with 2025 as the base year.

### Steps

1. **Identify each award and its taxable event** under [26 U.S.C. 83](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm): transfer of restricted stock, vesting, RSU settlement or option exercise. An option that fails the ISO rules, or exceeds the section 422(d) limit, is an NSO.
2. **Restricted stock:** decide on the section 83(b) election within 30 days of the transfer; file a written statement or Form 15620 with the service center where the return is filed and give the employer a copy ([Pub. 525](https://www.irs.gov/pub/irs-pdf/p525.pdf)). Not for options; for RSUs see below.
3. **RSU settlement and NSO exercise:** treat the income as supplemental wages ([Treas. Reg. 31.3402(g)-1](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1)). Withhold at 22% or by aggregation while the year's supplemental wages stay at or under USD 1 million; 37% on the excess, whatever the Form W-4 says.
4. **Social security** up to USD 184,500, **Medicare** on all of it, **Additional Medicare** once wages from you pass USD 200,000. Deposits and Form 941: `us-form-941-940-payroll`.
5. **Sell-to-cover:** shares sold or withheld to fund the withholding are still wages; the employee's basis in them equals their value at settlement, so the sale shows little or no gain once basis is corrected ([Treas. Reg. 1.61-2(d)(2)(i)](https://www.ecfr.gov/current/title-26/section-1.61-2)).
6. **Test the employee's own position:** compare 22% with the employee's 2026 marginal rate (brackets in Rev. Proc. 2025-32). Case 2 shows the gap.
7. **Before an ISO exercise,** compute the 2026 AMT with Form 6251, the exemption, the 50% phase-out and the 26% and 28% rates. Case 1 shows how fast the exemption goes.
8. **Keep Form 3921** for each ISO exercise (grant date, exercise date, price, value), and Form 3922 for ESPP shares in the cases its instructions list ([Instructions for Forms 3921 and 3922](https://www.irs.gov/pub/irs-pdf/i3921.pdf)).
9. **AMT credit:** AMT from an ISO adjustment (a timing item) becomes a minimum tax credit for later years under section 53, usable only to the extent regular tax exceeds the tentative minimum tax in that year ([26 U.S.C. 53(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartG-sec53.htm)); claim it on Form 8801. AMT from exclusion items, such as the standard deduction add-back, creates no credit (section 53(d)(1)(B)).
10. **ISO sale:** test both holding periods. A sale in the same calendar year as exercise is a disqualifying disposition and removes that year's AMT adjustment ([Instructions for Form 6251](https://www.irs.gov/pub/irs-pdf/i6251.pdf)).
11. **Any sale:** correct the Form 1099-B basis on Form 8949 with code B ([Instructions for Form 8949](https://www.irs.gov/pub/irs-pdf/i8949.pdf)).
12. **Section 83(i), private companies only:** test the corporation (no stock readily tradable on an established market in any preceding calendar year; a written plan covering not less than 80% of US employees with the same rights and privileges; the redemption limit) and the employee (not an excluded employee). Qualified stock comes only from an option exercise or RSU settlement, never a restricted stock award, and not where the employee may take cash instead (Pub. 525).
13. **Section 83(i) election:** the corporation gives the section 83(i)(6) notice; the employee elects within 30 days under Notice 2018-97, not on Form 15620. No election if the employee made a section 83(b) election for the same stock, or if any stock of the corporation is readily tradable before the election (section 83(i)(4)(B)). An 83(i) election on an option exercise means the option is no longer an ISO (Pub. 15-B).
14. **Section 83(i) payroll:** the election defers income tax only and "has no effect on the application of social security, Medicare, and FUTA taxes" (Pub. 15-B). When the deferral ends, include the amount in wages, withhold income tax at 37%, report it in Form W-2 box 12 code GG, and report the total deferred at year end with code HH. Recover withholding paid from the employer's own funds before 1 April of the following year ([Notice 2018-97](https://www.irs.gov/pub/irs-drop/n-18-97.pdf)).
15. **Where the official pages are silent, say so.** None of the pages read gives a valuation method for private company stock, and this skill states none.

## Boundary and exception table

### How each award is taxed

| Award | Rule |
| --- | --- |
| Restricted stock, no election | Under section 83(a), the value less any amount paid is included in the first year the shares are transferable or not subject to a substantial risk of forfeiture, whichever is earlier. It is wages; Treas. Reg. 31.3402(g)-1 lists "wage income recognized on the lapse of a restriction on restricted property transferred from an employer to an employee" as supplemental wages. Dividends before vesting are compensation (Pub. 525) |
| Restricted stock with a section 83(b) election | Value at transfer less the amount paid is included in the year of transfer; later growth is not compensation at vesting; if the shares are later forfeited "no deduction shall be allowed in respect of such forfeiture" (section 83(b)(1)). Dividends are dividends |
| RSU at grant | An RSU is a promise to deliver shares or cash later; for section 83, property excludes "an unfunded and unsecured promise to pay money or property in the future" (Treas. Reg. 1.83-3(e)). Nothing is transferred at grant and there is no 83(b) election. This is our reading; confirm for any funded or secured RSU |
| RSU at settlement | Notice 2018-97 describes the income "that would otherwise be included under section 83(a) upon ... the settlement of a restricted stock unit (RSU)". The value of the shares at settlement is wages and is not regular wages (our reading of the regulation's general definition), so supplemental wage withholding applies; social security and Medicare apply too |
| NSO at grant | No income unless the option has a readily determinable fair market value; an option not traded on an established market qualifies only if transferable, immediately exercisable in full, free of significant restrictions, and its privilege can be readily valued (Pub. 525; [Topic 427](https://www.irs.gov/taxtopics/tc427)) |
| NSO at exercise | The spread (value less price paid) is compensation at exercise, or at vesting if the shares received are still substantially nonvested. It is supplemental wages ("income recognized on the exercise of a nonstatutory stock option"), reported in Form W-2 boxes 1, 3 (up to the wage base) and 5, and box 12 code V (Pub. 15-B) |
| ISO, regular tax | No income at grant or exercise (Pub. 525; Topic 427) |
| ISO, payroll taxes | Social security, Medicare and FUTA wages "don't include remuneration resulting from the exercise of an incentive stock option or an employee stock purchase plan option, or from any disposition of stock acquired by exercising such an option" (Pub. 15-B) |
| ISO, AMT | Section 56(b)(3) switches off section 421 for the AMT, so the spread is an adjustment ([26 U.S.C. 56](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec56.htm)). Measured at vesting for shares still unvested at exercise, unless the holder elects by the 30th day after the transfer to take it at exercise; no adjustment if the shares are sold in the same year (Instructions for Form 6251). Line 2i on the 2025 form; check the 2026 form. Keep separate regular and AMT basis records |
| ISO, qualifying disposition | Held past both holding periods: the whole gain over the price paid is capital gain |
| ISO, disqualifying disposition | Ordinary income up to the spread at exercise, the rest capital gain. Where the disposition is a sale or exchange "with respect to which a loss (if sustained) would be recognized", the ordinary income "shall not exceed the excess (if any) of the amount realized on such sale or exchange over the adjusted basis" (section 422(c)(2)); a sale to a related person or a wash sale gets no cap. Pub. 525 states only the general rule. The employer reports the spread in Form W-2 box 1, but withholding "isn't required" and it is not wages for social security, Medicare or FUTA (Pub. 15-B) |
| ISOs over the USD 100,000 limit | The excess is treated as NSOs, by value at grant, in grant order (section 422(d)(2) and (3)) |

### Basis on Form 1099-B

- For compensatory options granted after 2013, the broker's basis "won't reflect any amount you included in income upon grant or exercise of the option. Increase your basis by any amount you included in income" (Instructions for Form 8949).
- Shares delivered on an RSU settlement: basis is "the amount paid for the property increased by the amount of such difference included in gross income" (Treas. Reg. 1.61-2(d)(2)(i)). Restricted stock follows the same rule in Treas. Reg. 1.83-4(b)(1) ([eCFR](https://www.ecfr.gov/current/title-26/section-1.83-4)), with or without an 83(b) election.
- Where Form 1099-B is wrong, enter code B in column (f) of Form 8949 and the adjustment in column (g), or the correct basis in column (e), as the instructions direct for the box checked.

### Section 83(i): events and excluded employees

| Item | Rule |
| --- | --- |
| Events that end the deferral (the earliest) | 5 years after the earlier of transferable or vested; the first date the stock becomes transferable (including to the employer); the date the employee first becomes an excluded employee; the first date any stock of the issuer becomes readily tradable on an established securities market; the date the employee revokes the election (section 83(i)(1)(B)) |
| Excluded: ownership | A 1-percent owner (section 416(i)(1)(B)(ii)) at any time in the calendar year or the 10 preceding calendar years (section 83(i)(3)(B)(i)) |
| Excluded: CEO or CFO | Anyone who "is or has been at any prior time" the CEO or CFO or acting in that capacity; no look-back limit (section 83(i)(3)(B)(ii)) |
| Excluded: family | A section 318(a)(1) family member of a person in the CEO or CFO test (section 83(i)(3)(B)(iii)) |
| Excluded: officers | One of the 4 highest compensated officers for the year or any of the 10 preceding years (section 83(i)(3)(B)(iv)) |
| Redemptions | No election if the corporation bought any outstanding stock in the preceding calendar year, unless not less than 25 percent of the total dollar amount bought is deferral stock and sellers were chosen on a reasonable basis (section 83(i)(4)(B)(iii)) |
| Value included at the end of deferral | The value at vesting, even if the stock has since fallen: "notwithstanding whether the value of the stock has declined during the deferral period" (Notice 2018-97) |
| 80% requirement and notice | Notice 2018-97 addresses "the 80% requirement of section 83(i)(2)(C)(i)(II)"; a reasonable good faith interpretation counts as compliance until further guidance |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether an 83(b) election was filed | Assume not; ask for the stamped copy or IRS acknowledgment |
| Supplemental wages already paid this year | Treat as above USD 1 million for a large vest until payroll confirms |
| ISO or NSO | Treat as NSO until the grant documents show section 422 terms |
| Grant date of an option sold | Treat the Form 1099-B basis as excluding the compensation element |
| Fair market value of private stock | Stop; valuation is not covered |

### Red flags to raise

| Flag | Why it matters |
| --- | --- |
| RSU vest withheld at 22% for an employee in the 32% or 35% band | Withholding shortfall; estimated tax or a Form W-4 change |
| ISO exercise late in the year with no AMT projection | Large AMT under the 2026 50% phase-out |
| Form 1099-B basis of zero or the option price only | Double taxation unless corrected on Form 8949 |
| 83(b) election mailed late | Invalid; vesting-date taxation applies |
| 83(i) employee who was ever CEO or CFO | Excluded employee for life |

## Worked cases

**Case 1, a decision: exercise ISOs in 2026?** A single filer has USD 200,000 of wages and no other income or deductions. Taxable income is USD 183,900 after the USD 16,100 standard deduction; regular tax is USD 17,966 plus 24% of the USD 78,200 above USD 105,700, USD 36,734. The holder can exercise 10,000 vested ISOs at USD 5 when the shares are worth USD 45: a USD 400,000 AMT adjustment (cash paid USD 50,000; no regular tax income). AMTI is USD 183,900 + USD 16,100 (standard deduction added back) + USD 400,000 = USD 600,000. The exemption of USD 90,100 is cut by 50% of the USD 100,000 above USD 500,000, to USD 40,100. Taxable excess USD 559,900: 26% of USD 244,500 = USD 63,570 plus 28% of USD 315,400 = USD 88,312, tentative minimum tax USD 151,882, AMT USD 115,148. Without the exercise, AMTI is USD 200,000, the full exemption applies, tentative minimum tax is 26% of USD 109,900 = USD 28,574, below regular tax, so no AMT. The USD 115,148 becomes a minimum tax credit carried forward (all of it here, since the exclusion items alone produce no net minimum tax), usable only when regular tax exceeds tentative minimum tax. Selling the shares in 2026 removes the adjustment but makes the spread ordinary income. Recommend exercising fewer options in 2026, sized so AMT stays near zero, unless the holder can fund the AMT and expects to use the credit.

```oa-check
name: ISO exercise and the 2026 AMT, single
inputs:
  wages: 200000
  standard_deduction: 16100
  iso_spread: 400000
  exemption: 90100
  phaseout_start: 500000
  rate_break: 244500
steps:
  - taxable_income: wages - standard_deduction
  - regular_tax: 17966 + 0.24 * (taxable_income - 105700)
  - amti: taxable_income + standard_deduction + iso_spread
  - exemption_allowed: max(exemption - 0.50 * max(amti - phaseout_start, 0), 0)
  - taxable_excess: amti - exemption_allowed
  - tmt: 0.26 * min(taxable_excess, rate_break) + 0.28 * max(taxable_excess - rate_break, 0)
  - amt: max(tmt - regular_tax, 0)
  - tmt_without_exercise: 0.26 * (wages - exemption)
expected:
  taxable_income: 183900
  regular_tax: 36734
  amti: 600000
  exemption_allowed: 40100
  taxable_excess: 559900
  tmt: 151882
  amt: 115148
  tmt_without_exercise: 28574
```

**Case 2, an RSU vest withheld at the flat rate.** A single filer has already been paid USD 250,000 of salary in 2026. 1,000 RSUs settle in shares worth USD 150 each, USD 150,000 of supplemental wages, the only supplemental wages this year. Withholding: 22% income tax, USD 33,000; no social security (wage base already reached); Medicare 1.45%, USD 2,175; Additional Medicare 0.9%, USD 1,350; sell-to-cover funds USD 36,525. Income tax: taxable income without the RSU is USD 233,900, tax USD 41,024 plus 32% of the excess over USD 201,775, USD 51,304; with it USD 383,900, tax USD 58,448 plus 35% of the excess over USD 256,225, USD 103,134.25. The RSU causes USD 51,830.25 of income tax, so the shortfall against the 22% withholding is USD 18,830.25, to be paid through estimated tax or a higher Form W-4 amount for the rest of 2026. Each share kept has a basis of USD 150; correct any different Form 1099-B basis on Form 8949 with code B.

```oa-check
name: RSU vest, flat-rate withholding against actual tax (2026, single)
inputs:
  salary: 250000
  rsu_value: 150000
  standard_deduction: 16100
steps:
  - withheld_income_tax: rsu_value * 0.22
  - medicare: rsu_value * 0.0145
  - additional_medicare: rsu_value * 0.009
  - sell_to_cover: withheld_income_tax + medicare + additional_medicare
  - ti_without: salary - standard_deduction
  - tax_without: 41024 + 0.32 * (ti_without - 201775)
  - ti_with: salary + rsu_value - standard_deduction
  - tax_with: 58448 + 0.35 * (ti_with - 256225)
  - rsu_tax: tax_with - tax_without
  - shortfall: rsu_tax - withheld_income_tax
expected:
  withheld_income_tax: 33000
  medicare: 2175
  additional_medicare: 1350
  sell_to_cover: 36525
  tax_without: 51304
  tax_with: 103134.25
  rsu_tax: 51830.25
  shortfall: 18830.25
```

The bracket bases above (USD 17,966, USD 41,024 and USD 58,448) are the single 2026 table amounts in Rev. Proc. 2025-32.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-EQ-STATE | State and local tax on equity pay, including sourcing for employees who moved or worked in several states | Refer |
| R-EQ-409A | Social security and Medicare timing for RSUs or deferred units that settle after vesting (section 3121(v)(2)), and section 409A for deferred units and discounted options | Refer |
| R-EQ-10PCT | ISOs granted to a holder of more than 10 percent of the voting power, ISO modifications, ESPP offerings under section 423 beyond the reporting step | Refer |
| R-EQ-AMT | AMT with other preference items, foreign tax credit, or a minimum tax credit already carried forward | Run the full Form 6251 and Form 8801; refer if unsure |
| R-EQ-FORMS | Due dates, penalties and e-filing rules for Forms 3921, 3922 and W-2 | Not stated here; see `us-form-941-940-payroll` and the form instructions |
| R-EQ-NONEMP | Equity for non-employees or partners, by a partnership or LLC, or by a non-US parent | Refer |
| R-EQ-SEC | Securities law questions, including section 16(b), beyond the effect section 83(c)(3) gives it | Refer |
| R-EQ-VALUE | Valuation of private company stock, or a disputed fair market value | Refer |
| R-EQ-1202 | Section 1202 exclusion on stock from options or restricted stock | `us-section-1202-qsbs` |

## Filing and payment

Employer: withhold at each settlement or exercise; report RSU and NSO income in Form W-2 boxes 1, 3 and 5 (NSO spread also box 12 code V; 83(i) codes GG and HH); deposit and report on Form 941 (`us-form-941-940-payroll`); file Form 3921 for each ISO exercise and Form 3922 where required. Employee: file the 2026 Form 1040 by **15 April 2027** with Form 6251 for an ISO adjustment, Form 8949 and Schedule D for sales with basis corrected, and Form 8801 in later years for the credit. A withholding shortfall is paid by estimated tax (the 2026 instalments, the last due 15 January 2027) or extra withholding; see `us-quarterly-estimated-tax`.

## Completion checklist

- Each award classified and its taxable event dated.
- 83(b) election decided and filed within 30 days of any restricted stock transfer.
- Supplemental wage withholding at 22% or 37% applied by calendar-year total; FICA and Additional Medicare applied.
- Employee's actual 2026 tax compared with the withholding; shortfall covered.
- ISO exercise sized against a 2026 AMT projection with the 50% phase-out; Form 3921 kept.
- Every sale's Form 1099-B basis checked and corrected on Form 8949.
- 83(i) eligibility (corporation and employee) tested before any election.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Pub. 15 (2026). Read for section 7 supplemental wages (22%, 37%, USD 1 million), the USD 184,500 wage base, 6.2%, 1.45%, 0.9% over USD 200,000. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| IRS Pub. 15-T (2026). Read for its methods not applying when the flat rates are used. | https://www.irs.gov/pub/irs-pdf/p15t.pdf | 2026-11-13 |
| IRS Pub. 15-B (2026). Read for stock options, the FICA exclusion for ISOs, section 83(i) (80%, 37%) and W-2 codes V, GG and HH. | https://www.irs.gov/pub/irs-pdf/p15b.pdf | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 AMT exemptions, phase-out thresholds, the USD 244,500 break, the single brackets and the standard deduction. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Public Law 119-21, section 70107. Read for the 50% phase-out rate for taxable years beginning after 31 December 2025 and the indexing change. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 55 (govinfo, 2024 edition). Read for (b)(1)(A) 26% and 28%. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm | 2026-11-13 |
| 26 U.S.C. 56 (govinfo). Read for (b)(3), the ISO adjustment. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec56.htm | 2026-11-13 |
| 26 U.S.C. 53 (govinfo). Read for (c) and (d)(1)(B), the minimum tax credit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartG-sec53.htm | 2026-11-13 |
| 26 U.S.C. 422 (govinfo). Read for (a)(1) and (a)(2), (c)(2) and (d). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partII-sec422.htm | 2026-11-13 |
| 26 U.S.C. 83 (govinfo). Read for (a), (b), (c)(3) and (i). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec83.htm | 2026-11-13 |
| Treas. Reg. 31.3402(g)-1 (eCFR). Read for what counts as supplemental wages. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1 | 2026-11-13 |
| Treas. Reg. 1.83-3 (eCFR). Read for (e), the definition of property. | https://www.ecfr.gov/current/title-26/section-1.83-3 | 2026-11-13 |
| Treas. Reg. 1.83-4 (eCFR). Read for (b), basis. | https://www.ecfr.gov/current/title-26/section-1.83-4 | 2026-11-13 |
| Treas. Reg. 1.61-2 (eCFR). Read for (d)(2)(i), basis of vested shares. | https://www.ecfr.gov/current/title-26/section-1.61-2 | 2026-11-13 |
| IRS Pub. 525 (2025). Read for options, restricted property, 83(b) and 83(i) procedure. | https://www.irs.gov/pub/irs-pdf/p525.pdf | 2026-11-13 |
| IRS Topic 427, Stock options. | https://www.irs.gov/taxtopics/tc427 | 2026-11-13 |
| Instructions for Form 6251 (2025). Read for the ISO adjustment, the 30-day election and Form 8801. | https://www.irs.gov/pub/irs-pdf/i6251.pdf | 2026-11-13 |
| Instructions for Form 8949 (2025). Read for the basis of compensatory option stock and code B. | https://www.irs.gov/pub/irs-pdf/i8949.pdf | 2026-11-13 |
| Instructions for Forms 3921 and 3922. | https://www.irs.gov/pub/irs-pdf/i3921.pdf | 2026-11-13 |
| Notice 2018-97. Read for section 83(i) guidance, recovery before 1 April and the value at vesting. | https://www.irs.gov/pub/irs-drop/n-18-97.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Form 6251 and Form 8949 and the 2026 Pub. 525 were not yet published when read, so the 2025 rules are used and the Form 6251 line number (2i in 2025) must be rechecked on the 2026 form.
