---
name: latvia-income-tax
description: "Latvian personal income tax (IIN) for tax year 2026, for resident employees, self-employed people, pensioners and people with capital income. Covers the 25.5% and 33% bands with the threshold tied to the EUR 105,300 maximum social insurance base, the 3% surcharge above EUR 200,000, the fixed EUR 570 monthly non-taxable minimum, EUR 250 monthly dependant relief, the EUR 12,000 pensioner minimum, eligible expenses, capital income at 25.5%, business income and losses, the annual return (1 March to 1 June, or 1 April to 1 July), payment dates, penalties and 0.05% a day late interest. Trigger on: Latvia income tax, gada ienākumu deklarācija, neapliekamais minimums, Latvian capital gains tax, self-employed Latvia. Out of scope: payroll withholding (latvia-payroll), social contributions (latvia-social-contributions), non-residents (lv-cross-border), company tax (lv-corporate-income-tax), microenterprise planning (latvia-tax-optimization)."
jurisdiction: LV
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia: personal income tax (2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from the consolidated Law On Personal Income Tax (PIT Law), the law On State Social Insurance, the Law On Taxes and Fees (LTF) and the Administrative Liability Law, in the versions in force for 2026, and from the State Revenue Service (VID) rate and annual return pages. See Sources for how they were read.

Related skills in this pack:

- Monthly withholding by employers (wage tax, the wage tax book): [latvia-payroll](latvia-payroll.md).
- Social contributions (VSAOI), the solidarity tax and self-employed contributions: [latvia-social-contributions](latvia-social-contributions.md).
- Non-residents, residence tests, treaties and foreign tax credit: [lv-cross-border](lv-cross-border.md).
- Company profit tax and the reduced-rate dividend regime at company level: [lv-corporate-income-tax](lv-corporate-income-tax.md).
- Microenterprise tax and the self-employed versus company choice: [latvia-tax-optimization](latvia-tax-optimization.md).

## Who this applies to

- **Residents** pay tax on worldwide income. Residence is set by the LTF (declared home in Latvia, or 183 days in any 12-month period). The residence rules are in [lv-cross-border](lv-cross-border.md).
- **Employees.** The employer withholds 25.5% wage tax each month (PIT Law s. 15(3)). The 33% band and the surcharge are settled in the annual return.
- **Self-employed people** registered with VID as performing economic activity. They must register before they start (PIT Law s. 28(6)). Business income is taxed in the annual return at the progressive rates. There are no advance payments: s. 18 was repealed from 2023.
- **Pensioners** get a larger non-taxable minimum (EUR 12,000 a year, s. 12(5)), applied by the pension payer.
- **People with capital income** (interest, taxable dividends, capital gains, crypto gains, investment account income) pay 25.5% on it, outside the bands (s. 15(5)).
- **Out of scope here.** Non-residents are taxed on Latvian-source income only and get no non-taxable minimum or reliefs, unless they are EU/EEA residents earning over 75% of their total income in Latvia (s. 12(2), s. 13(4)); see [lv-cross-border](lv-cross-border.md). Microenterprise tax payers are taxed under the Microenterprise Tax Law instead (s. 15(10)); see [latvia-tax-optimization](latvia-tax-optimization.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Annual income up to the maximum social insurance base | 25.5% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(2)(1)) |
| Annual income above the maximum social insurance base | 33% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(2)(2)) |
| Maximum social insurance base, which is the band threshold | EUR 105,300 a year | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 14(5)) |
| Monthly wage tax withheld by employer | 25.5% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(3)) |
| Surcharge on total income above EUR 200,000 | 3% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15.1) |
| Non-taxable minimum, fixed | EUR 570 a month (EUR 6,840 a year) | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 12(1)) |
| Pensioner non-taxable minimum | EUR 12,000 a year | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 12(5)) |
| Relief for each dependant | EUR 250 a month (EUR 3,000 a year) | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 13(1.2)) |
| Eligible expenses (education, medical, health insurance, donations) | Up to 50% of taxable income, max EUR 600 (EUR 600 per family member for education and medical) | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 10(1.3)) |
| Private pension and accumulating life insurance contributions | Up to 10% of income, max EUR 4,000 a year | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 10(1.9)) |
| Capital income and capital gains | 25.5% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(5)) |
| Dividends paid under CIT Law s. 4.2 (reduced company rate) | 6% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(5.1)) |
| Capital gains on deals started but not finished by 31 Dec 2024 | 20% (2025 to 2027) | 2026 | https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes |
| Rental income without a registered business (notified to VID) | 10% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(6)(3), s. 11(12)) |
| Minimum tax for a registered self-employed person with no or low business tax | EUR 50 | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 19(2.1)) |
| Employee social contribution (deductible) | 10.50% (total 34.09%, employer 23.59%) | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 18(1)) |
| Late payment interest | 0.05% a day | 2026 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam (s. 29(2)) |

The non-taxable minimum is a fixed amount. The old income-tested "differentiated" minimum was repealed from 1 January 2025 (PIT Law transitional provision 202). The minimum and dependant relief apply only to income taxed at the s. 15(2) and 15(3) rates, not to capital income (s. 12(9), s. 13(3)).

## The taxable base

1. **Collect the annual income** taxed at the progressive rates: salary, business profit, pensions, rental income under the general regime, royalties, lottery wins over EUR 3,000 (s. 15(24)).
2. **Deduct social contributions** paid by the person (s. 10(1)(1)) and the solidarity tax (s. 10(1)(1.1)). In the annual return, the deductible contributions are reduced by any part of the solidarity tax moved to the PIT account (s. 10(1.10)).
3. **Deduct the non-taxable minimum** (EUR 6,840 for a full year, s. 12(1)), dependant relief (EUR 250 a month per dependant, s. 13(1.2)), disability and repressed-person reliefs (s. 13(1)(4)), and eligible expenses within the caps (s. 10).
4. **Tax the result**: 25.5% up to EUR 105,300 and 33% on the excess (s. 15(2)). Employees have already had 25.5% withheld each month; the return settles the difference.
5. **Capital income is taxed separately** at 25.5% (s. 15(5)). A capital gain is the sale price less the purchase cost and later improvements. Losses on one asset offset gains on another in the same year. A net loss is not carried forward and does not offset other income (s. 11.9(9), (10)).
6. **Dividends** from a company that paid corporate income tax on the distributed profit are exempt (s. 9(1)(2.1)). Dividends paid under the reduced CIT rate in CIT Law s. 4.2 are taxed at 6% instead (s. 9(3.9), s. 15(5.1)). See [lv-corporate-income-tax](lv-corporate-income-tax.md).
7. **Surcharge**: 3% on the excess of total income over EUR 200,000. Total income counts all taxable income, including capital income and capital gains, and also exempt dividends under s. 9(1)(2.1) and (2.2) (s. 15.1(2)). It is paid through the annual return (s. 19(2.6)).
8. **Main home exemption**: a gain on real estate owned over 60 months and used as the declared home for at least 12 months in a row in that period is exempt (s. 9(1)(33)). Related exemptions are in s. 9(1)(33.1) to (34.3).

**Business income (self-employed).** Taxable income is business receipts less documented business costs (s. 11). Business losses can be carried forward for three years against later business profit only (s. 11(9)). They cannot offset other income (s. 19(2)). A registered person with no business tax, or with business tax of EUR 50 or less, pays EUR 50 by 23 June (s. 19(2.1)), with exceptions in s. 19(2.2) to (2.4). Social contributions for the self-employed are in [latvia-social-contributions](latvia-social-contributions.md).

**Microenterprise tax payers.** Their microenterprise income is taxed under the Microenterprise Tax Law, not at the PIT rates (s. 15(10)). Eligible expenses and reliefs do not apply to it (s. 10(5)). See [latvia-tax-optimization](latvia-tax-optimization.md).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Annual return (gada ienākumu deklarācija), general window | 1 March to 1 June 2027 for tax year 2026 | PIT Law s. 19(5) |
| Annual return if income at the s. 15(2) rates exceeds EUR 105,300 | 1 April to 1 July 2027 | PIT Law s. 19(5); VID annual return page |
| Payment of tax due, income up to EUR 105,300 | 23 June 2027 | PIT Law s. 19(3) |
| Payment of tax due, income above EUR 105,300 | 23 July 2027 | PIT Law s. 19(3) |
| Instalments if tax due exceeds EUR 640 | Thirds on 23 June, 23 July, 23 August (or 23 July, 23 August, 23 September above EUR 105,300) | PIT Law s. 19(3)(1), (2) |
| Quarterly capital gains return (gains over EUR 1,000 in the quarter) | 15th of the month after the quarter | PIT Law s. 19(5.3) |
| Annual capital gains return (quarterly gains up to EUR 1,000) | 15 January 2027 | PIT Law s. 19(5.3) |
| Register as self-employed | Before starting the activity | PIT Law s. 28(6) |

**Who must file.** VID says a return is compulsory when tax was not fully withheld during the year, or when the person is responsible for paying the tax themselves (for example a self-employed person, a seaman or a landlord). The law adds:

- anyone with business income (s. 20(4)(1));
- anyone who owes extra tax because of the 33% band or the 3% surcharge (s. 20(4)(2));
- residents with income from outside the EU, or other income not taxed at source (VID annual return page);
- residents whose exempt income exceeds EUR 10,000 must show it in the return (s. 19(2)).

Returns are filed in VID's Electronic Declaration System (EDS). VID pre-fills the data it holds. If a person who must file does not, VID's calculation in the EDS draft stands and becomes payable (s. 19(5.4), s. 20(2)). Others may file voluntarily to claim eligible expenses, and can file or correct a return for the three previous years (VID annual return page). Overpayments are refunded within three months of filing (s. 19(4)), or automatically under s. 20.1 when no return is required.

## Penalties and interest

| Breach | Consequence | Source |
|---|---|---|
| Late payment | 0.05% of the unpaid tax for each day late, from the day after the due date | LTF s. 29(2); PIT Law s. 31.1(2), s. 31(3) |
| Return filed 3 to 10 days late | Warning or fine of 5 to 14 fine units (EUR 25 to 70) | LTF s. 141(1) |
| Return filed 11 to 20 days late | 15 to 30 units (EUR 75 to 150) | LTF s. 141(2) |
| Return filed 21 to 30 days late | 31 to 56 units (EUR 155 to 280) | LTF s. 141(3) |
| Return filed over 30 days late or not filed | 57 to 140 units (EUR 285 to 700) | LTF s. 141(4) |
| Tax understated (found in an audit) by up to 15% of the tax due | Penalty of 20% of the understated tax, plus the tax and late interest | LTF s. 32(4); PIT Law s. 31.3(1) |
| Tax understated by more than 15% | Penalty of 30% of the understated tax | LTF s. 32(5) |
| First offence, returns and payments on time, cooperation | Penalty halved | LTF s. 32(7) |
| Unregistered business activity | Tax, late interest and a 50% penalty | LTF s. 34; PIT Law s. 32(2) |

One fine unit is EUR 5 (Administrative Liability Law s. 16(2)).

## Cross-border points

- Non-residents pay tax only on Latvian-source income, mostly by withholding at source. They do not get the non-taxable minimum, dependant relief or most eligible expenses, unless they are EU/EEA residents earning over 75% of their total income in Latvia (s. 10(3), (4), s. 12(2), s. 13(4)).
- An employee covered by another country's social insurance pays 33% wage tax on monthly pay above one twelfth of EUR 105,300 (s. 15(16)).
- Residents earning salary in another EU state do not report it in the return; income from outside the EU must be reported (VID annual return page).
- Foreign income in the return is taxed at the person's average weighted rate (s. 19(1.1)). Foreign tax credit and treaties: s. 24.
- A foreign national with a long-stay visa under Immigration Law s. 11(5) (remote worker) may choose 15% on that income for 365 days (s. 15(19.2)).
- Remigrating diaspora pensioners keep the foreign country's pension exemption (s. 12(13) to (19)).

For residence, treaties, withholding on payments to non-residents and exit rules, use [lv-cross-border](lv-cross-border.md).

## Worked examples

**Example 1: employee with one child.** A resident employee earns EUR 30,000 gross salary in 2026 and supports one child under 18 all year. No other income and no eligible expenses. Employee social contributions are 10.5% of salary, EUR 3,150. Deduct those, the EUR 6,840 non-taxable minimum and EUR 3,000 dependant relief (EUR 250 x 12). Taxable income is EUR 17,010, all below EUR 105,300, so it is all taxed at 25.5%: tax EUR 4,337.55. If the employer applied the minimum and relief through the wage tax book each month, the withholding already matches and no return is required.

```oa-check
name: Employee EUR 30,000 salary, one dependant (2026)
inputs:
  salary: 30000
  months: 12
  dependants: 1
steps:
  - vsaoi: salary * 0.105
  - ntm: 570 * months
  - dependant_relief: 250 * months * dependants
  - taxable: salary - vsaoi - ntm - dependant_relief
  - tax: taxable * 0.255
expected:
  vsaoi: 3150
  ntm: 6840
  dependant_relief: 3000
  taxable: 17010
  tax: 4337.55
```

**Example 2: salary plus a large share sale (surcharge).** A resident employee earns EUR 60,000 salary and sells shares in 2026 for a gain of EUR 250,000. No dependants. Salary: EUR 60,000 less 10.5% contributions (EUR 6,300) and the EUR 6,840 minimum leaves EUR 46,860, taxed at 25.5%: EUR 11,949.30. The gain is capital income at 25.5%: EUR 63,750. Total income for the surcharge is EUR 310,000 (salary plus gain, s. 15.1(2)). The excess over EUR 200,000 is EUR 110,000, so the 3% surcharge is EUR 3,300. Total tax is EUR 78,999.30. The person must file the annual return (s. 20(4)(2)) and pay the surcharge with it (s. 19(2.6)). The gain is also declared in a quarterly capital gains return.

```oa-check
name: Salary EUR 60,000 plus capital gain EUR 250,000, surcharge (2026)
inputs:
  salary: 60000
  gain: 250000
steps:
  - vsaoi: salary * 0.105
  - ntm: 570 * 12
  - prog_base: salary - vsaoi - ntm
  - prog_tax: prog_base * 0.255
  - gain_tax: gain * 0.255
  - surcharge_income: salary + gain
  - surcharge: max(surcharge_income - 200000, 0) * 0.03
  - total_tax: prog_tax + gain_tax + surcharge
expected:
  vsaoi: 6300
  prog_base: 46860
  prog_tax: 11949.30
  gain_tax: 63750
  surcharge: 3300
  total_tax: 78999.30
```

## Ask the client first

1. Were you a Latvian tax resident for all of 2026 (declared home, days in Latvia)? If not, use [lv-cross-border](lv-cross-border.md).
2. What income did you have: salary, registered business, rental, pension, dividends, interest, share or crypto sales, foreign income? Which country paid each?
3. Did your income at the progressive rates exceed EUR 105,300, or your total income exceed EUR 200,000? This sets the band, the surcharge and the filing window.
4. Did you give your wage tax book to an employer or pension payer, and for which months?
5. Who did you support in 2026 (children, students up to 24, a non-working spouse), and does any of them have their own income?
6. Do you have receipts for education, medical costs, health insurance, donations, private pension or life insurance payments?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli), consolidated with amendments to 3 December 2025 in force 1 January 2026: ss. 9, 10, 11, 11.9, 12, 13, 15, 15.1, 18, 19, 20, 28, 31, 31.1, 31.3, 32; transitional provision 202 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-24 |
| Law On State Social Insurance (Par valsts sociālo apdrošināšanu), consolidated with amendments to 16 April 2026: ss. 14(5), 18(1) | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu | 2026-10-24 |
| Law On Taxes and Fees (Par nodokļiem un nodevām), consolidated: ss. 29, 32, 34, 141 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 |
| Administrative Liability Law (Administratīvās atbildības likums): s. 16 | https://likumi.lv/ta/id/303007 | 2026-10-24 |
| VID, personal income tax rates (updated 31 December 2025) | https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes | 2026-10-24 |
| VID, annual income return (who must file, windows, late interest) | https://www.vid.gov.lv/lv/gada-ienakumu-deklaracija | 2026-10-24 |

likumi.lv and vid.gov.lv refused connections from our network on 23 and 24 October 2026. All texts were read from Internet Archive (web.archive.org) copies made in 2026: the PIT Law captured 1 September 2026, the law On State Social Insurance 3 October 2026, the LTF 18 September 2026, the Administrative Liability Law 10 August 2026, the VID rates page 12 October 2026 and the VID annual return page 9 September 2026.

Not yet confirmed: whether the EUR 200,000 surcharge base in s. 15.1(2) is gross taxable income or income after social contributions and the non-taxable minimum (example 2 uses the gross amounts; VID's page says only "total income"); whether the EUR 105,300 band test is applied before or after deductions; the payment date for tax shown on quarterly capital gains returns (not found in the PIT Law text read); the 2026 microenterprise tax rate and threshold (Microenterprise Tax Law not read); the Cabinet regulation on eligible expenses (not read); the disability and politically repressed person relief amounts set by Cabinet regulation (not read); amendments to the PIT Law adopted after 1 September 2026.
