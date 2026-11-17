---
name: latvia-tax-optimization
description: "Legal tax planning in Latvia for tax year 2026, for self-employed people and small companies. Covers the distributed-profits corporate income tax (0% on retained profit, 20% of the distribution divided by 0.8), the optional 15% rate with a 0.85 divisor plus 6% personal income tax for companies owned only by individuals, micro-enterprise tax at 25% of turnover and who may choose it, the self-employed (FIK) versus company (SIA) choice with 25.5% and 33% personal income tax and 31.07% social contributions, personal reliefs, and the deemed-distribution red lines. Trigger on: reduce tax Latvia, Latvia 0% retained profit, distributed profits tax, reinvested profit Latvia, micro-enterprise tax, mikrouzņēmuma nodoklis, FIK vs SIA, Latvia dividends, 15% dividend option, save tax Latvia, tax planning Latvia. Out of scope: computing the tax itself (latvia-income-tax, lv-corporate-income-tax, latvia-social-contributions, latvia-payroll, latvia-vat-return) and non-residents (lv-cross-border)."
version: 0.4
jurisdiction: LV
tax_year: 2026
last_updated: 2026-11-17
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Latvia Tax Optimization

## Latvia Tax Optimization Skill v0.4

**Tier 2, built from the law; not yet approved. Figures for tax year 2026 come from the Latvian tax laws on likumi.lv and the State Revenue Service (VID) pages, read on 17 November 2026; the Sources table at the end lists them. They agree with `latvia-income-tax`, `lv-corporate-income-tax`, `latvia-social-contributions` and `latvia-payroll`; if they ever differ, those skills win. Not yet signed off by a Latvian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

> **The Latvian headline mirrors Estonia: an SIA pays 0% on profit it keeps and reinvests, and corporate income tax only when it distributes.** Reinvesting defers distribution tax; deemed distributions and the annual minimum-tax exception below still apply.

## Scope

- **Who this is for:** a resident individual in business in Latvia in 2026 (self-employed, FIK, or individual merchant, IK) and the owners of a small limited liability company (SIA) choosing how to run and pay themselves.
- **The decisions it covers:** company (SIA) or self-employed; micro-enterprise tax or the general personal income tax regime; standard 20% dividend route or the 15% option; which personal reliefs to claim; and the deemed-distribution lines not to cross.
- **Not covered:** computing each tax in full (latvia-income-tax, lv-corporate-income-tax, latvia-social-contributions, latvia-payroll, latvia-vat-return) and non-residents (lv-cross-border).

## Ask the client first

- Expected turnover and real business expenses for the year (micro-enterprise tax is on turnover with no expense deduction; the VAT threshold caps it)?
- Is the business a company (SIA) or run by the individual (self-employed, IK, individual enterprise, farm)?
- Will profit be kept and reinvested, or paid out this year?
- Are all the company's members individuals in the month the dividend is calculated (15% option)?
- Other income: employment, pensions, income above EUR 105,300 or above EUR 200,000?
- Dependants, education or medical costs, donations, private pension or life insurance contributions?

## The method, step by step

### Key figures

| Item | Figure | Condition | Source |
|---|---|---|---|
| Corporate tax on retained profit | 0% distribution tax | Ordinary SIA distribution base only (CIT Law art. 4(1), (2)); the annual EUR 50 minimum tax may apply under art. 17(11), subject to art. 17(12) | [CIT Law art. 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) ; [VID, Corporate income tax](https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodoklis) |
| Corporate tax on a distribution | 20% of the amount divided by 0.8 | CIT Law art. 3(1), art. 4(9) | [CIT Law arts. 3, 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Corporate tax as a share of a net dividend | 25% (computed: 20% divided by 0.8) | Same articles; no ordinary personal income tax on that dividend once current Latvian CIT has been paid (PIT Law s. 9(1)(2.1)); it can still count towards the 3% surcharge | [CIT Law arts. 3, 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Optional dividend rate from 1 January 2026 | 15% after dividing the dividend by 0.85, plus 6% personal income tax on the dividend | Members only individuals in the period the dividend is calculated (CIT Law art. 3(5), art. 4.2); 6% under PIT Law s. 15(5.1), withheld by the company (CIT Law art. 16(5)) | [CIT Law arts. 3, 4.2, 16](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) ; [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Micro-enterprise tax | 25% of turnover | Micro-enterprise Tax Law arts. 5(2), 6; 80% of it is booked as the owner's social contributions, 20% as personal income tax (art. 8(1)) | [Micro-enterprise Tax Law](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| Micro-enterprise turnover cap | Expected turnover must not exceed the VAT registration threshold, EUR 50,000; actual VAT supply-value exclusions and status-loss timing are separate tests | Micro-enterprise Tax Law art. 4(1)(1); VAT Law art. 59(1) | [Micro-enterprise Tax Law art. 4](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) ; [VAT Law art. 59](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| Personal income tax on business income | 25.5% up to EUR 105,300 a year; 33% above | PIT Law s. 15(2); the band is the maximum social insurance base (Law on State Social Insurance s. 14(5)) | [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) ; [Law On State Social Insurance s. 14](https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu) |
| Additional rate | 3% on total annual income above EUR 200,000 | PIT Law s. 15.1 | [Law On Personal Income Tax s. 15.1](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Self-employed social contributions | 31.07% on a chosen base of at least EUR 780 a month when monthly profit reaches EUR 780, plus 10% for pensions on profit above that chosen base; below EUR 780, 10% on actual income only | VID, self-employed contributions page | [VID, Self-employed contributions](https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas) |
| Employee social contributions | 34.09% | Law on State Social Insurance s. 18(1) | [Law On State Social Insurance s. 18](https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu) |
| Minimum tax for a registered self-employed person | EUR 50 a year, paid by 23 June | If there is no taxable business income or the tax is under EUR 50 (PIT Law s. 19(2.1)); not in the year of registration and the next, the closing year, or if contributions or wage tax were paid (s. 19(2.2), (2.3)) | [Law On Personal Income Tax s. 19](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Minimum contribution base for employees | EUR 780 a month or EUR 2,340 a quarter | Applies to micro-enterprise employers too, subject to aggregation and exempt employee categories (VID, micro-enterprise tax page) | [VID, Micro-enterprise tax](https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis) |
| Private pension and accumulating life insurance | Together up to 10% of annual income and no more than EUR 4,000 a year; eligible fund/insurer and contract conditions in s. 10(1)(5), (6) apply, including at least a ten-year accumulating life policy | PIT Law s. 10(1.9) | [Law On Personal Income Tax s. 10](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Education, medical costs and donations | Together up to 50% of taxable income and no more than EUR 600 a year (EUR 600 for each family member for education and medical costs) | PIT Law s. 10(1.3) | [Law On Personal Income Tax s. 10](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| SIA representation and staff wellbeing costs | The part above 5% of the previous year's gross payroll on which social contributions were paid is a non-business expense | CIT Law art. 8(2)(7) | [CIT Law art. 8](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| SIA donation relief (choose one a year) | Up to 5% of last year's profit after tax; or up to 2% of last year's gross payroll; or a tax credit of 85% of the donation capped at 30% of the dividend tax | Only eligible recipients and genuine donations without consideration; art. 12(3), (5), (6) conditions apply, including the tax-debt test, no related-beneficiary or return benefit, and foreign-recipient evidence. Choose one relief for aggregate annual donations (CIT Law art. 12(1), (2)) | [CIT Law art. 12](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |

### Step 1. Deferral via a company (the core lever)

| Action | Tax |
| --- | --- |
| SIA earns profit and **keeps or reinvests** it | **0% distribution tax**, subject to the annual minimum below. VID: distribution tax is deferred until profit is distributed or a deemed distribution occurs  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| SIA **distributes** profit as dividends | 20% CIT on the dividend divided by 0.8, so 25% of the net dividend (CIT Law art. 3(1), 4(9)). The shareholder pays no personal income tax on a dividend from profit that has borne this CIT (PIT Law s. 9(1)(2.1))  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Non-business spending, bad debts, excess interest, loans to related persons, non-arm's-length prices | Taxed as deemed distributions (VID; CIT Law art. 4(2)(2), arts. 8 to 11). Keep business and private spending apart  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |

For anyone reinvesting to grow (hiring, equipment, expansion), the SIA defers distribution tax while profit remains in the business; the deemed-distribution and annual minimum-tax rules still apply. **This often beats working as a self-employed FIK**, whose profit is taxed every year at 25.5% and 33% with social contributions on top.

The ordinary SIA annual minimum is EUR 50: if annual CIT is below that amount, the last-period return tops it up. It does not apply in the registration year, the year liquidation finishes, an insolvency case, or a year with at least EUR 100 of PIT or social contributions paid for an employee (CIT Law art. 17(11), (12)). [CIT Law art. 17](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums)

### Step 2. The 15% option from 1 January 2026

- A company whose members are all individuals in the tax period (month, or quarter) in which the dividend is calculated may choose 15% instead of 20%. The dividend is divided by 0.85 instead of 0.8 (CIT Law art. 3(5), art. 4.2(1), (2)). The ordinary dividend exemption then does not apply, and the shareholder pays 6% personal income tax on the dividend (PIT Law s. 9(3.9), s. 15(5.1)). The company withholds it when it calculates the dividend (CIT Law art. 16(5); see lv-corporate-income-tax for dates).
- **What the option does to the total.** On a declared dividend of EUR 10,000, company tax is EUR 1,764.71 instead of EUR 2,500, but the shareholder then pays EUR 600 and keeps EUR 9,400, not EUR 10,000. Compared on the same profit, the two routes leave almost the same cash with the shareholder. Worked case 1 shows it. Choose the option on the client's own facts, not as a saving in itself.

### Step 3. Micro-enterprise tax (simplicity for the small)

- **Micro-enterprise tax coverage.** A single tax of 25% of turnover (Micro-enterprise Tax Law arts. 5(2), 6). Article 1(4) defines it as the owner's personal income tax and social contributions. VID also describes the single-payment regime as replacing separate CIT and business risk duty; that wording does not admit an SIA to the regime or exempt an employer's normal payroll obligations (art. 2.1). 80% of it goes to the owner's social insurance (art. 8(1)), so pensions and benefits can be lower; compare the actual contribution base and benefit entitlement rather than the nominal 31.07% self-employed or 34.09% employee rates (VID). The owner is socially insured from the day the status starts, and VSAA works out the contribution base for each month with turnover (art. 9(1), (2)).
- **Who can choose it.** Only an individual merchant (IK), an individual enterprise, a farm or fishing household, or an individual registered with VID as self-employed (art. 1(3)). An SIA cannot; an SIA that held the status lost it on 1 January 2022 (transitional provision 36). Expected turnover must not exceed the VAT registration threshold, which is EUR 50,000 a year, and the business must not plan to register for VAT before reaching it (art. 4(1)(1); VAT Law art. 59(1)). Since 1 July 2025 a person registered under the special VAT scheme for small businesses (VAT Law art. 139.2) may also use it (art. 1(3); VID).
- **Combining.** A person who owns more than one of these business forms can use micro-enterprise tax for only one of them (art. 2(2)). A micro-enterprise cannot at the same time pay personal income tax on its business income (art. 2(3), (4)); art. 2(5) preserves the PIT Law s. 11(12) notified property-letting exception. A taxpayer who stops and re-registers in the same year as a PIT or CIT payer cannot return to the regime that year or the next (art. 2(6)). Wages the owner earns as an employee elsewhere are taxed under the general rules; the articles read set no bar on the owner also being employed.
- **How to join.** At registration with the Enterprise Register or with VID, or by applying to VID by 15 December of the year before (art. 4(1), (3), (4); VID). From 2026 an individual expecting irregular activity may register for one or more specified quarters (art. 4(3.1); transitional provision 45).
- **How it ends.** Status ends from the next tax year if the micro-enterprise becomes, or must become, a registered VAT payer, except under the special scheme of VAT Law art. 139.2 (art. 4(8), (10)). It also ends if there is no turnover for two tax years in a row (three for a business that joined from the second quarter) (art. 4(8.1), (8.2)). The owner may switch back to the PIT or CIT regime no earlier than the end of the tax year (art. 4(7)).
- **Filing.** With no employees, a quarterly micro-enterprise tax return for each quarter with turnover, by the 15th of the month after the quarter; the tax is paid into the single tax account by the 23rd (art. 7(2), (3)). A business income account (SDI konts) at a bank can file and pay automatically (art. 7.1; VID).
- **Employees.** Their wages are taxed as normal: wage tax and social contributions (art. 2.1), with a minimum contribution base of EUR 780 a month or EUR 2,340 a quarter in 2026, subject to aggregation and exempt employee categories on the VID page; route the payroll assessment to latvia-payroll (VID).
- **Micro-enterprise limitations.** No deduction for expenses, since the tax is on turnover, and the turnover ceiling above.

Best for very small, low-expense activities; model it against the FIK and SIA routes (worked case 2).

### Step 4. Self-employed (FIK) vs micro-enterprise vs company (SIA)

| Route | Treatment | Best when |
| --- | --- | --- |
| **FIK** (self-employed) | Personal income tax on net business income at 25.5% up to EUR 105,300 and 33% above (VID; PIT Law s. 15(2)); minimum tax EUR 50 a year, except in the first two years and some other cases (PIT Law s. 19(2.1) to (2.4)). Social contributions 31.07% on a chosen base of at least EUR 780 a month when monthly profit reaches EUR 780, plus 10% for pensions on profit above that chosen base (VID; Social Insurance Law s. 14(18)). Pensioner and property-management rates differ; see latvia-social-contributions. Contributions paid are deducted once under PIT Law s. 10(1)(1); deductions reduce the lower band first under s. 3(2.4), s. 15(15) | Small, wants income now, simple, or real expenses are high  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| **Micro-enterprise** | 25% of turnover, no expense deduction, expected turnover not exceeding the VAT threshold (EUR 50,000); status-loss timing as in Step 3 (Micro-enterprise Tax Law arts. 4, 6) | Tiny, low expenses  [Official source](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| **SIA** | 0% distribution tax on retained profit, subject to the annual minimum; 20% (or the 15% option) on distribution; real expenses deductible; limited liability subject to the small-capital insolvency exception (CIT Law art. 3; Commercial Law arts. 137, 185.1(7)) | Reinvesting, growing, higher margins  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |

### Step 5. Deductions and reliefs

| Item | Treatment |
| --- | --- |
| Non-taxable minimum | EUR 550 a month in 2026 under the ordinary minimum, independent of income level; pensioner and other exclusions remain in PIT Law s. 12 (transitional provision 197(2); VID). See `latvia-income-tax`  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Dependants | EUR 250 a month for each eligible dependant; only one supporter claims it, and income, pension and benefit exclusions apply (PIT Law s. 13(1)(1), (1.2), (3), (5)). Apply it only to eligible progressive-rate income  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Education, medical costs and donations (eligible expenses) | Together up to 50% of taxable income and no more than EUR 600 a year, or EUR 600 for each family member for education and medical costs (PIT Law s. 10(1.3))  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Private pension (Pillar 3) and accumulating life insurance | Together up to 10% of annual income and no more than EUR 4,000 a year; eligible fund/insurer and contract conditions in s. 10(1)(5), (6) apply, including at least a ten-year accumulating life policy (PIT Law s. 10(1.9)); early pension withdrawals can trigger an income adjustment (s. 10(1.6)-(1.8))  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| SIA business expenses | Deductible against profit in effect, since only distributions are taxed; but private use and non-business spending are deemed distributions (CIT Law art. 8)  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| SIA representation and staff wellbeing costs | The part above 5% of the previous year's gross payroll on which social contributions were paid is a non-business expense, taxed (CIT Law art. 8(2)(7))  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| SIA donations | A non-business expense, taxed, unless they meet the relief in CIT Law art. 12(1) (art. 8(2)(4)). See `lv-corporate-income-tax`  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |

The individual reliefs above apply only to eligible progressive-rate income, not to micro-enterprise turnover or capital income (PIT Law s. 10(5), 12(9), 13(3)). Education and medical expenses must be eligible and documented; family amounts cannot be claimed twice. Donations require an eligible recipient, no consideration and no prohibited related beneficiary. [PIT Law s. 10](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli).

### Step 6. Red lines (do not cross)

- **Deemed distributions.** Non-business expenses (including benefits to members and staff that were not taxed as their income, gifts, and private use of company assets), loans to related persons, excess interest and non-arm's-length prices are taxed as if distributed (CIT Law art. 4(2)(2), arts. 8, 10, 11; VID). The detailed conditions and exceptions in arts. 9 to 11 still apply: a related-party loan is not automatically taxable in every case. Article 11(2)-(4) has lender, funding, capital and duration exceptions, and art. 11(5) addresses repayment. Route that assessment to lv-corporate-income-tax. You cannot avoid distribution tax merely by relabelling a withdrawal.
- **Substance requirement.** Non-business expenses are judged by the economic substance of the transaction, not only its legal form (CIT Law art. 8(1)). The SIA must carry on genuine business.
- **Micro-enterprise misuse.** **AUDIT FLASH POINT.** The micro-enterprise regime must not be used to dress up what is really employment, or a larger business split into pieces. The law's stated aim is to reduce the burden on micro-enterprises while respecting fair competition and social security (Micro-enterprise Tax Law art. 1.1), and an owner may use the regime for only one business form (art. 2(2)).

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| A member of the SIA is a company in the month the dividend is calculated | The 15% option is not available that period; 20% with the 0.8 divisor applies | CIT Law art. 4.2(1)  [Official source](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Dividend paid under the 15% option | The dividend exemption is switched off; 6% personal income tax withheld | PIT Law s. 9(3.9), 15(5.1); CIT Law art. 16(5)  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Micro-enterprise becomes or must become an ordinary VAT registrant, including a turnover excess beyond the EUR 5,000 tolerance | VAT registration under the VAT Law; micro status ends from the next tax year. The threshold is subject to art. 59(2), (3), (8)-(12); it is not a general exemption from cross-border registration | VAT Law art. 59(1), (4); Micro-enterprise Tax Law art. 4(8)  [Official source](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| Micro-enterprise registered under the special small-business VAT scheme | Keeps the micro status | Micro-enterprise Tax Law art. 4(10)  [Official source](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| No micro turnover for consecutive tax periods | Status ends from the next tax period after two consecutive periods without turnover; for a taxpayer registered from the second quarter, the test is three consecutive periods without turnover, including the registration period | Micro-enterprise Tax Law art. 4(8.1), (8.2)  [Official source](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| Self-employed with no taxable business income in a later year | EUR 50 minimum tax by 23 June of the following year, subject to all s. 19(2.2)-(2.4) exclusions: qualifying employee PIT/social contributions or own self-employed contributions; the registration year and next year; the business-closure or completed-liquidation year; and a proportional exclusion for days caring for a child under two or days of incapacity, pregnancy or childbirth leave covered by sick note B | PIT Law s. 19(2.1)-(2.4)  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Total income above EUR 200,000 | 3% additional rate, counting exempt dividends too | PIT Law s. 15.1  [Official source](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |

## Worked cases

### 1. SIA owned by one individual: standard 20% vs the 15% option (a decision)

An SIA owned by one individual has EUR 12,000 of profit to pay out in 2026, and pays all of it as a dividend plus the tax on it. The individual has no other income in this illustration, so no 3% surcharge arises.

- Standard route: the dividend divided by 0.8 must equal 12,000, so the dividend is 9,600 and CIT is 2,400. No personal income tax. The owner keeps 9,600.
- 15% option: the dividend divided by 0.85 must equal 12,000, so the dividend is 10,200 and CIT is 1,800. The company withholds 6%, which is 612. The owner keeps 9,588.
- The standard route leaves the owner EUR 12 more.

```oa-check
name: SIA owned by one individual, EUR 12,000 profit paid out, standard 20% vs 15% option, 2026
inputs:
  profit_paid_out: 12000
steps:
  - std_dividend: profit_paid_out * 0.8
  - std_cit: std_dividend / 0.8 * 0.20
  - std_owner_keeps: std_dividend
  - alt_dividend: profit_paid_out * 0.85
  - alt_cit: alt_dividend / 0.85 * 0.15
  - alt_pit: alt_dividend * 0.06
  - alt_owner_keeps: alt_dividend - alt_pit
  - difference: std_owner_keeps - alt_owner_keeps
expected:
  std_dividend: 9600
  std_cit: 2400
  std_owner_keeps: 9600
  alt_dividend: 10200
  alt_cit: 1800
  alt_pit: 612
  alt_owner_keeps: 9588
  difference: 12
```

### 2. Micro-enterprise tax or self-employed (FIK), worked both ways (a decision)

An ordinary non-pensioner resident, with no other income, no dependants and no other reliefs, chooses the minimum EUR 780 contribution base and expects EUR 30,000 of turnover in 2026, spread evenly over the year, under the VAT threshold. Contributions are rounded to cents each month; these are planning comparisons with no other contribution obligations. Two expense levels:

- **Micro-enterprise:** 25% of EUR 30,000 is EUR 7,500, whatever the expenses.
- **FIK with EUR 6,000 of expenses:** profit EUR 24,000, EUR 2,000 a month. Contributions: 31.07% of EUR 780 for 12 months (EUR 2,908.20) plus 10% of EUR 1,220 for 12 months (EUR 1,464.00): EUR 4,372.20. Taxable income after contributions (PIT Law s. 10(1)(1)) and the EUR 6,600 minimum: EUR 13,027.80; tax at 25.5%: EUR 3,322.09. Total EUR 7,694.29, which is EUR 194.29 more than micro-enterprise tax.
- **FIK with EUR 15,000 of expenses:** profit EUR 15,000, EUR 1,250 a month. Contributions EUR 2,908.20 plus 10% of EUR 470 for 12 months (EUR 564.00): EUR 3,472.20. Taxable income EUR 4,927.80; tax EUR 1,256.59. Total EUR 4,728.79, which is EUR 2,771.21 less than micro-enterprise tax.
- **Decision:** with low expenses the two routes are close (here micro-enterprise tax is EUR 194.29 cheaper, and books EUR 6,000 as the owner's social contributions against EUR 4,372.20); once expenses are a large share of turnover, the FIK route wins clearly. Contributions above the minimum, other income, or reliefs change the result: recompute on the client's figures.

```oa-check
name: EUR 30,000 turnover, micro-enterprise tax vs FIK at EUR 6,000 and EUR 15,000 of expenses, 2026
inputs:
  turnover: 30000
  expenses_low: 6000
  expenses_high: 15000
  min_base: 780
  monthly_minimum: 550
steps:
  - micro_tax: turnover * 0.25
  - micro_social_share: micro_tax * 0.80
  - minimum_year: monthly_minimum * 12
  - base_ssc: round(min_base * 0.3107, 2) * 12
  - profit_a: turnover - expenses_low
  - ssc_a: base_ssc + (profit_a / 12 - min_base) * 0.10 * 12
  - pit_a: round((profit_a - ssc_a - minimum_year) * 0.255, 2)
  - fik_a: ssc_a + pit_a
  - fik_minus_micro_a: fik_a - micro_tax
  - profit_b: turnover - expenses_high
  - ssc_b: base_ssc + (profit_b / 12 - min_base) * 0.10 * 12
  - pit_b: round((profit_b - ssc_b - minimum_year) * 0.255, 2)
  - fik_b: ssc_b + pit_b
  - micro_minus_fik_b: micro_tax - fik_b
expected:
  micro_tax: 7500
  micro_social_share: 6000
  minimum_year: 6600
  base_ssc: 2908.20
  ssc_a: 4372.20
  pit_a: 3322.09
  fik_a: 7694.29
  fik_minus_micro_a: 194.29
  ssc_b: 3472.20
  pit_b: 1256.59
  fik_b: 4728.79
  micro_minus_fik_b: 2771.21
```

## When to refuse or refer

- **Prohibition 1.** NEVER describe the SIA 0%-retained system as tax-free. It is deferral; CIT applies on distribution.
- **Prohibition 2.** NEVER advise taking company value out as "expenses" or loans to avoid the distribution tax. That triggers deemed-distribution tax.
- **Prohibition 3.** NEVER present the micro-enterprise regime without its turnover ceiling, its no-deduction trade-off and the potentially lower social insurance it buys.
- **Prohibition 4.** NEVER contradict the rates in `latvia-income-tax`, `lv-corporate-income-tax`, `latvia-social-contributions` or `latvia-payroll`.
- **Prohibition 5.** NEVER present the 15% option as a saving without comparing it on the client's own figures; and NEVER present unconfirmed points (listed under Sources) as confirmed, or optimisation as definitive advice. Route to a licensed Latvian tax adviser.
- Refer non-residents, group structures, holding companies, reorganisations and transfer pricing to lv-cross-border, lv-corporate-income-tax and lv-transfer-pricing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Latvia) before acting upon.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums), consolidated, arts. 2, 3, 4, 4.2, 8(1)-(2), 10, 11, 12, 16(5), 17 and article heading 9 read | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-11-17 |
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli), consolidated, s. 3(2), (2.4), 9(1)(2.1), (3.9), 10(1), (1.1)-(1.9), (5), 12(1), (2), (4), (5), (9), 13(1), (1.2), (3), (5), 15(2), (5), (5.1), (15), 15.1, 19(2.1)-(2.4) and transitional provision 197 read | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-11-17 |
| Micro-enterprise Tax Law (Mikrouzņēmumu nodokļa likums), consolidated, arts. 1, 1.1, 2, 2.1, 4 to 9 and transitional provisions 36, 45, 46 read | https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums | 2026-11-17 |
| VAT Law (Pievienotās vērtības nodokļa likums), consolidated, art. 59 read | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums | 2026-11-17 |
| Law On State Social Insurance (Par valsts sociālo apdrošināšanu), consolidated, s. 14(2), (5), (18) and 18 read | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu | 2026-11-17 |
| VID, Corporate income tax (page updated 29.10.2026, body read for the subjects used above) | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodoklis | 2026-11-17 |
| VID, Corporate income tax rates (page updated 16.01.2026, rates table read for the figures used above) | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodokla-likmes | 2026-11-17 |
| VID, Micro-enterprise tax (page updated 13.05.2026, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis | 2026-11-17 |
| VID, Micro-enterprise tax rate (page updated 22.05.2025, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodokla-likme | 2026-11-17 |
| VID, Self-employed social insurance contributions (page updated 08.10.2026, body read for the subjects used above) | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas | 2026-11-17 |
| VID, Personal income tax rates (page updated 31.12.2025, rates table read for the figures used above) | https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes | 2026-11-17 |
| VID, Mandatory annual income return (page body read: EUR 50 minimum tax, payment dates) | https://www.vid.gov.lv/lv/obligati-iesniedzama-gada-ienakumu-deklaracija | 2026-11-17 |
| Commercial Law, arts. 137, 185.1(7) read for member liability and the small-capital insolvency exception | https://likumi.lv/ta/id/5490-komerclikums | 2026-11-17 |

The specified source passages were read on 2026-11-17 from the preserved official-page captures made that day; the read date covers those passages, not every section of each law. The previous version (2026-10-30) read the laws from Internet Archive copies because likumi.lv did not respond that day and took the micro-enterprise rules from VID only; the Micro-enterprise Tax Law itself has now been read, which settles what happens when turnover passes the VAT threshold (status ends from the next tax year, art. 4(8)) and how the regime combines with other business income (art. 2).

Not yet confirmed: the Micro-enterprise Tax Law changes starting on 1 April 2027 (new art. 7.2 for starting micro-enterprise taxpayers and a new art. 1(1) definition; transitional provision 46), whose 2027 wording was not read; contribution outcomes for pensioners, property managers and agricultural or intellectual-property income are outside worked case 2; route those facts to latvia-social-contributions. Paid contributions in this case are deducted once under PIT Law s. 10(1)(1), which was read.
