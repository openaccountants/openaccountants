---
name: latvia-tax-optimization
description: "Legal tax planning in Latvia for tax year 2026, for self-employed people and small companies. Covers the distributed-profits corporate income tax (0% on retained profit, 20% of the distribution divided by 0.8), the optional 15% rate with a 0.85 divisor plus 6% personal income tax for companies owned only by individuals, micro-enterprise tax at 25% of turnover and who may choose it, the self-employed (FIK) versus company (SIA) choice with 25.5% and 33% personal income tax and 31.07% social contributions, personal reliefs, and the deemed-distribution red lines. Trigger on: reduce tax Latvia, Latvia 0% retained profit, distributed profits tax, reinvested profit Latvia, micro-enterprise tax, mikrouzņēmuma nodoklis, FIK vs SIA, Latvia dividends, 15% dividend option, save tax Latvia, tax planning Latvia. Out of scope: computing the tax itself (latvia-income-tax, lv-corporate-income-tax, latvia-social-contributions, latvia-payroll, latvia-vat-return) and non-residents (lv-cross-border)."
version: 0.2
jurisdiction: LV
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia Tax Optimization

## Latvia Tax Optimization Skill v0.2

**Tier 2, sourced from the law. Figures for tax year 2026 come from the Latvian tax laws and the State Revenue Service (VID); the Sources table at the end lists them. They agree with `latvia-income-tax`, `lv-corporate-income-tax`, `latvia-social-contributions` and `latvia-payroll`; if they ever differ, those skills win. Not yet signed off by a Latvian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Latvia |
| Tax year | 2026 (calendar year for individuals) |
| Currency | EUR |
| Headline levers | Distributed-profits CIT (0% retained / 20% on distribution); the optional 15% dividend rate for companies owned only by individuals; micro-enterprise tax; FIK vs SIA |
| Corporate tax (SIA) | **0% on retained profit; 20% only when profit is distributed or treated as distributed**, after dividing the amount by 0.8, so 25% of a net dividend (CIT Law art. 3(1), art. 4(9)) |
| Optional rate from 1 Jan 2026 | 15% after dividing the dividend by 0.85, plus 6% personal income tax on the dividend, for companies whose members are only individuals (CIT Law art. 3(5), art. 4.2; PIT Law s. 15(5.1)) |
| Micro-enterprise tax | **25% of turnover**, one payment in place of PIT, CIT, the business risk duty and social contributions; open only to individuals and their unincorporated businesses with turnover under the VAT threshold (VID) |
| Self-employed (FIK) | Personal income tax of **25.5%** on annual income up to EUR 105,300 and **33%** above it, plus 3% on total income above EUR 200,000 (PIT Law s. 15(2), 15.1); social contributions 31.07% on at least EUR 780 a month (VID) |
| Anti-avoidance | Expenses judged by economic substance; non-business spending and loans to related persons are taxed as distributions (CIT Law art. 8, art. 11) |

> **The Latvian headline mirrors Estonia: an SIA pays 0% on profit it keeps and reinvests, and corporate income tax only when it distributes.** Reinvest, and the tax is deferred for as long as the profit stays in the company.

## Section 2 -- Deferral via a Company (the core lever)

**Deferral via a Company (the core lever)**

| Action | Tax |
| --- | --- |
| SIA earns profit and **keeps or reinvests** it | **0% CIT**. VID: tax is deferred until profit is distributed or spent on things that do not develop the business |
| SIA **distributes** profit as dividends | 20% CIT on the dividend divided by 0.8, so 25% of the net dividend (CIT Law art. 3(1), 4(9)). The shareholder pays no personal income tax on a dividend from profit that has borne this CIT (PIT Law s. 9(1)(2.1)) |
| Non-business spending, bad debts, excess interest, loans to related persons, non-arm's-length prices | Taxed as deemed distributions (VID; CIT Law art. 8 to 11). Keep business and private spending apart |

For anyone reinvesting to grow (hiring, equipment, expansion), the SIA defers all corporate tax until cash is taken out. **This often beats working as a self-employed FIK**, whose profit is taxed every year at 25.5% and 33% with social contributions on top.

- **The 15% option from 1 January 2026.** A company whose members are all individuals in the tax period (month, or quarter) in which the dividend is calculated may choose 15% instead of 20%. The dividend is divided by 0.85 instead of 0.8 (CIT Law art. 3(5), art. 4.2(1), (2)). The ordinary dividend exemption then does not apply, and the shareholder pays 6% personal income tax on the dividend (PIT Law s. 9(3.9), s. 15(5.1)). The company withholds it when it calculates the dividend (CIT Law art. 16(5); see lv-corporate-income-tax for dates).
- **What the option does to the total.** On a declared dividend of EUR 10,000, company tax is EUR 1,764.71 instead of EUR 2,500, but the shareholder then pays EUR 600 and keeps EUR 9,400, not EUR 10,000. Compared on the same profit, the two routes leave almost the same cash with the shareholder. The worked comparison below shows it. Choose the option on the client's own facts, not as a saving in itself.

**Worked comparison.** An SIA owned by one individual has EUR 12,000 of profit to pay out in 2026, and pays all of it as a dividend plus the tax on it.

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

## Section 3 -- Micro-Enterprise Tax (simplicity for the small)

- **Micro-enterprise tax coverage.** A single tax of 25% of turnover (VID). It replaces personal income tax, corporate income tax, the business risk duty and the owner's social contributions (VID). 80% of it goes to the owner's social insurance, so pensions and benefits are lower than under the 31.07% self-employed or 34.09% employee rates (VID).
- **Who can choose it.** Only an individual merchant (IK), an individual enterprise, a farm or fishing household, or an individual registered with VID as self-employed. An SIA cannot. Expected turnover must not exceed the VAT registration threshold, which is EUR 50,000 a year (VID; VAT Law art. 59(1)). Since 1 July 2025 a person registered under the special VAT scheme for small businesses (VAT Law art. 139.2) may also use it (VID).
- **How to join.** At registration, or by applying to VID by 15 December of the year before (VID).
- **Filing.** With no employees, a quarterly micro-enterprise tax return for each quarter with turnover, by the 15th of the month after the quarter. A business income account (SDI konts) at a bank can file and pay automatically (VID).
- **Employees.** Their wages are taxed as normal: wage tax and social contributions, with a minimum contribution base of EUR 780 a month or EUR 2,340 a quarter in 2026 (VID).
- **Micro-enterprise limitations.** No deduction for expenses, since the tax is on turnover, and the turnover ceiling above.

Best for very small, low-expense activities; model it against the FIK and SIA routes.

## Section 4 -- Self-Employed (FIK) vs Company (SIA)

**Self-Employed (FIK) vs Company (SIA)**

| Route | Treatment | Best when |
| --- | --- | --- |
| **FIK** (self-employed) | Personal income tax on net business income at 25.5% up to EUR 105,300 and 33% above (VID; PIT Law s. 15(2)); minimum tax EUR 50 a year, except in the first two years and some other cases (VID). Social contributions 31.07% on at least EUR 780 a month, plus 10% for pensions on income above EUR 780 (VID) | Small, wants income now, simple |
| **Micro-enterprise** | 25% of turnover, no expense deduction, turnover under EUR 50,000 (VID) | Tiny, low expenses |
| **SIA** | 0% on retained profit; 20% (or the 15% option) on distribution; real expenses deductible; limited liability (CIT Law art. 3) | Reinvesting, growing, higher margins |

## Section 5 -- Deductions & Reliefs

**Deductions & Reliefs**

| Item | Treatment |
| --- | --- |
| Non-taxable minimum | EUR 550 a month in 2026, the same for everyone (PIT Law transitional provision 197(2); VID). See `latvia-income-tax` |
| Dependants | EUR 250 a month for each dependant (PIT Law s. 13(1.2)) |
| Education, medical costs and donations (eligible expenses) | Together up to 50% of taxable income and no more than EUR 600 a year, or EUR 600 for each family member for education and medical costs (PIT Law s. 10(1.3)) |
| Private pension (Pillar 3) and accumulating life insurance | Together up to 10% of annual income and no more than EUR 4,000 a year (PIT Law s. 10(1.9)) |
| SIA business expenses | Deductible against profit in effect, since only distributions are taxed; but private use and non-business spending are deemed distributions (CIT Law art. 8) |
| SIA representation and staff wellbeing costs | The part above 5% of the previous year's gross payroll is a non-business expense, taxed (CIT Law art. 8(2)(7)) |
| SIA donations | A non-business expense, taxed, unless they meet the relief in CIT Law art. 12(1) (art. 8(2)(4)). See `lv-corporate-income-tax` |

## Section 6 -- Red Lines (do not cross)

- **Deemed distributions.** Non-business expenses (including benefits to members and staff that were not taxed as their income, gifts, and private use of company assets), loans to related persons, excess interest and non-arm's-length prices are taxed as if distributed (CIT Law art. 8, 10, 11; VID). You cannot take value out tax-free by calling it something else.
- **Substance requirement.** VID judges whether an expense is business-related by its economic substance, not only its legal form (CIT Law art. 8(1)). The SIA must carry on genuine business.
- **Micro-enterprise misuse.** The micro-enterprise regime must not be used to dress up what is really employment, or a larger business split into pieces. AUDIT FLASH POINT.

## PROHIBITIONS

- **Prohibition 1.** NEVER describe the SIA 0%-retained system as tax-free. It is deferral; CIT applies on distribution.
- **Prohibition 2.** NEVER advise taking company value out as "expenses" or loans to avoid the distribution tax. That triggers deemed-distribution tax.
- **Prohibition 3.** NEVER present the micro-enterprise regime without its turnover ceiling, its no-deduction trade-off and the lower social insurance it buys.
- **Prohibition 4.** NEVER contradict the rates in `latvia-income-tax`, `lv-corporate-income-tax`, `latvia-social-contributions` or `latvia-payroll`.
- **Prohibition 5.** NEVER present the 15% option as a saving without comparing it on the client's own figures; and NEVER present unconfirmed points (listed under Sources) as confirmed, or optimisation as definitive advice. Route to a licensed Latvian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Latvia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums), art. 3, 4, 4.2, 8, 10, 11, 16 (Internet Archive copy of 4 October 2026) | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-10-30 |
| Law on Personal Income Tax (Par iedzīvotāju ienākuma nodokli), s. 9, 10, 13, 15, 15.1, transitional provision 197 (Internet Archive copy of 1 September 2026) | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-30 |
| VAT Law (Pievienotās vērtības nodokļa likums), art. 59 (Internet Archive copy of 16 October 2026) | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums | 2026-10-30 |
| VID, Corporate income tax | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodoklis | 2026-10-30 |
| VID, Corporate income tax rates | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodokla-likmes | 2026-10-30 |
| VID, Micro-enterprise tax | https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis | 2026-10-30 |
| VID, Micro-enterprise tax rate | https://www.vid.gov.lv/lv/mikrouznemumu-nodokla-likme | 2026-10-30 |
| VID, Self-employed social insurance contributions | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas | 2026-10-30 |
| VID, Personal income tax rates | https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes | 2026-10-30 |
| VID, Mandatory annual income return | https://www.vid.gov.lv/lv/obligati-iesniedzama-gada-ienakumu-deklaracija | 2026-10-30 |

likumi.lv did not respond on 2026-10-30, so the law texts were read from the Internet Archive copies dated above. VID pages were read live.

Not yet confirmed: the Micro-enterprise Tax Law itself (likumi.lv did not respond and the Internet Archive has no 2026 copy), so the micro-enterprise rules come from VID only; what happens when a micro-enterprise's turnover passes the VAT threshold during the year; and any statutory limits on using the regime alongside employment.

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
