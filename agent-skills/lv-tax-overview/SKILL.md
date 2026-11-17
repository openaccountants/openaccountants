---
name: lv-tax-overview
description: "Tax overview for Latvia, tax year 2026: the State Revenue Service (VID), the calendar tax year, residence (declared home or 183 days in any 12 months), personal income tax at 25.5% and 33% with the band at EUR 105,300 and a 3% surcharge above EUR 200,000, the EUR 550 monthly non-taxable minimum, corporate income tax of 20% on distributed profit divided by 0.8 (optional 15% with a 0.85 divisor plus 6% personal tax for companies owned only by individuals), micro-enterprise tax at 25% of turnover, VAT at 21% with a EUR 50,000 registration threshold, social contributions of 34.09%, and the main filing and payment dates. Trigger on: Latvia tax overview, Latvian tax system, how is Latvia taxed, VID deadlines, Latvia tax rates 2026. For detail use latvia-income-tax, lv-corporate-income-tax, latvia-vat-return, latvia-social-contributions, latvia-payroll, lv-cross-border, lv-transfer-pricing and latvia-tax-optimization."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lv-tax-overview"
  jurisdiction: "LV"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Latvia Tax Overview

This is a map of the Latvian tax system for tax year 2026, not a computation skill. Each row gives the headline figure, its conditions and the official text it comes from, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

Latvia is an EU member state with a euro tax system run by the State Revenue Service (Valsts ieņēmumu dienests, VID). Personal income tax has two bands plus a surcharge on very high income. Company profit is taxed only when it is distributed or treated as distributed. The specified passages of the laws published on likumi.lv were read from preserved official captures on 17 November 2026; likumi.lv states that its consolidated texts are informative and that the official publication prevails in a conflict.

**Quick answer (2026).** Personal income tax 25.5% up to EUR 105,300 a year and 33% above, plus 3% on total income above EUR 200,000. Non-taxable minimum EUR 550 a month. Company tax 20% of distributed profit divided by 0.8, so 25% of a net dividend; no distribution tax on profit kept, subject to the annual minimum-tax exception below. Micro-enterprise tax 25% of turnover. VAT 21%, registration threshold EUR 50,000. Social contributions 34.09% for an employee. Late payment interest 0.05% a day.

## Ask the client first

- Is the person resident in Latvia (declared home, 183 days in any 12-month period, or a Latvian citizen employed abroad by the Latvian government)?
- What kind of income: employment, business (self-employed), capital, or dividends from a Latvian company?
- Individual, individual merchant (IK), micro-enterprise taxpayer or company (SIA or AS)?
- Domestic supplies in the calendar year (VAT threshold and return period)?
- Does annual income taxed at the progressive rates exceed EUR 105,300 (return window and payment dates move)?

## Rates, bands and thresholds

All rows are for 2026 unless a row says otherwise.

| Item | Figure | Condition | Source |
|---|---|---|---|
| Tax year, individuals | Calendar year | PIT Law s. 19(2): the return shows all income of the "taksācijas periodā (kalendāra gadā)". Detail: `latvia-income-tax` | [Law On Personal Income Tax s. 19](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Corporate income tax period | Calendar month; a quarter for a payer entitled under Accounting Law art. 13 to book its documents once a quarter | CIT Law art. 3(2), (3). Detail: `lv-corporate-income-tax` | [CIT Law art. 3](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Currency | Euro (EUR) | The thresholds in the tax laws are set in euro | [Law On Personal Income Tax](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Tax authority | State Revenue Service (VID); returns and annual reports through its Electronic Declaration System (EDS) | Annual Reports Law art. 97(1): reports go to VID in the "Elektroniskajā deklarēšanas sistēmā" | [Annual Reports Law art. 97](https://likumi.lv/ta/id/277779-gada-parskatu-un-konsolideto-gada-parskatu-likums) |
| Resident individual | Declared home in Latvia; or 183 days or more in any 12-month period that starts or ends in the tax year; or a Latvian citizen employed abroad by the Latvian government | Law on Taxes and Fees art. 14(2); art. 14(3) sets the arrival and departure dates. Detail: `lv-cross-border` | [Law on Taxes and Fees art. 14](https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam) |
| Resident company | Set up and registered, or required to be set up and registered, under Latvian law | Law on Taxes and Fees art. 14(4); others are non-residents (art. 14(5)) | [Law on Taxes and Fees art. 14](https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam) |
| What is taxed | Residents: income from Latvia and abroad; non-residents: income from Latvia only | PIT Law s. 2(1), (2); Law on Taxes and Fees art. 14(5). Detail: `lv-cross-border` | [Law On Personal Income Tax s. 2](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Personal income tax, progressive rates | 25.5% on annual income up to the maximum social insurance base; 33% on the part above it | PIT Law s. 15(2). The base is EUR 105,300 a year (Law on State Social Insurance s. 14(5)); deductions reduce the lower band first under s. 3(2.4), with relief at 25.5% under s. 15(15). Detail: `latvia-income-tax` | [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) ; [Law On State Social Insurance s. 14](https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu) |
| Monthly wage tax withholding | 25.5% | Employers withhold on monthly taxable income (PIT Law s. 15(3)); a person under another state's social insurance system pays 33% on monthly wages above one twelfth of the maximum base (s. 15(16)). Detail: `latvia-payroll` | [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Capital income and capital gains | 25.5% | PIT Law s. 15(5); not for dividends under the 15% company option, which take 6% (s. 15(5.1)) | [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Additional rate (surcharge) | 3% on total annual income above EUR 200,000 | Counts taxable income including capital income and gains, plus exempt dividends and liquidation quotas under s. 9(1)(2.1), (2.2) (PIT Law s. 15.1(1), (2)); paid in the annual return (s. 19(2.6)) | [Law On Personal Income Tax s. 15.1, 19](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Monthly non-taxable minimum | EUR 550 a month in 2026 under the ordinary minimum, independent of income level | Ordinary minimum only: pensioners and the exclusions in s. 12 have different rules. PIT Law transitional provision 197(2); EUR 510 in 2025 (197(1)); s. 12(1) itself sets EUR 570, which applies once the transitional amounts end (computed: provision 197 covers only 2025 and 2026). Detail: `latvia-income-tax` | [Law On Personal Income Tax s. 12, transitional provision 197](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Corporate income tax rate | 20% of the taxable base, after the base is divided by 0.8 | CIT Law art. 3(1), art. 4(9). Profit kept is outside the distribution base (art. 4(2)); the annual EUR 50 minimum tax can still apply (art. 17(11), (12)). Detail: `lv-corporate-income-tax` | [CIT Law art. 3, 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Corporate income tax on a net dividend | 25% of the net amount (computed: 20% divided by 0.8) | Same articles; the shareholder then pays no personal income tax on that dividend (PIT Law s. 9(1)(2.1)) | [CIT Law art. 3, 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Deemed distributions | Non-business expenses, qualifying bad debts, excess interest, related-person loans within art. 11 and non-arm's-length transfer pricing adjustments | CIT Law art. 4(2)(2)(a) to (k), subject to the detailed conditions and exceptions in arts. 8 to 11. Detail: `lv-corporate-income-tax`, `lv-transfer-pricing` | [CIT Law art. 4](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| Alternative dividend rate, from 1 January 2026 | 15% on calculated dividends, divided by 0.85; the individual then pays 6% personal income tax | Only a company whose members, in the period the dividend is calculated, are all individuals (CIT Law art. 3(5), art. 4.2(1), (2)); 6% under PIT Law s. 15(5.1), the s. 9(1)(2.1) exemption switched off by s. 9(3.9). Detail: `lv-corporate-income-tax` | [CIT Law art. 3, 4.2](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) ; [Law On Personal Income Tax s. 15](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) |
| Micro-enterprise tax | 25% of turnover; one payment for the owner's social contributions and personal income tax | Micro-enterprise Tax Law arts. 1(4), 5(2), 6. Only an individual merchant, individual enterprise, farm or fishing household, or individual registered with VID for business; expected turnover not above the VAT registration threshold (art. 1(3), 4(1)). Detail: `latvia-tax-optimization` | [Micro-enterprise Tax Law](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| VAT standard rate | 21% | VAT Law art. 41(1)(1). Detail: `latvia-vat-return` | [VAT Law art. 41](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| VAT reduced rates | 12% and 5% | VAT Law art. 41(1)(2), for the goods and services listed in art. 42 | [VAT Law art. 41](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) ; [VID, VAT rates](https://www.vid.gov.lv/lv/pievienotas-vertibas-nodokla-likmes) |
| VAT registration threshold | EUR 50,000 of domestic supplies in a calendar year, without VAT | A domestic business may stay unregistered at or under it (VAT Law art. 59(1)), subject to the supply-value rules and exceptions in art. 59(2), (3), (8)-(12). Prior-year excess and cross-border services can remove that right. An excess of no more than EUR 5,000 permits year-end registration, with the application timing in art. 59(5)-(7) | [VAT Law art. 59](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| Social contributions, employee insured for all risks | 34.09%: 23.59% employer, 10.50% employee | Law on State Social Insurance s. 18(1). Detail: `latvia-social-contributions`, `latvia-payroll` | [Law On State Social Insurance s. 18](https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu) |
| Social contributions, self-employed | 31.07% on a chosen base of at least EUR 780 a month when monthly profit reaches EUR 780, plus 10% for pensions on profit above that chosen base; below EUR 780 only the 10% pension contribution on actual income | Ordinary non-pensioner, non-property-management rate; agricultural and intellectual-property timing exceptions use latvia-social-contributions. VID, self-employed contributions page (updated 08.10.2026); Social Insurance Law s. 14(18). Detail: `latvia-social-contributions` | [VID, Self-employed contributions](https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas) |
| Late payment interest | 0.05% of the unpaid tax for each day late | Unless a tax law sets another rate; for the single tax account, calculation on the 1st and 15th and the reliefs in art. 29(2.1), (2.2) apply. Payment dates on weekends or holidays move to the next working day (art. 29(3.1)) | [Law on Taxes and Fees art. 29](https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam) |

## Main deadlines

| Deadline | Rule | Source |
|---|---|---|
| Annual personal income tax return | 1 March to 1 June of the next year; 1 April to 1 July if income taxed at the s. 15(2) rates is above the maximum social insurance base (EUR 105,300). A return can be filed or corrected for three years, for example to claim a refund | [Law On Personal Income Tax s. 19](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) ; [VID, Annual income return](https://www.vid.gov.lv/lv/gada-ienakumu-deklaracija) |
| Paying personal income tax due on the annual return | By 23 June. Above EUR 105,300 of such income, by 23 July. Tax over EUR 640 can be paid in three equal parts: 23 June, 23 July and 23 August, or 23 July, 23 August and 23 September above EUR 105,300 (PIT Law s. 19(3)) | [Law On Personal Income Tax s. 19](https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli) ; [VID, Mandatory annual income return](https://www.vid.gov.lv/lv/obligati-iesniedzama-gada-ienakumu-deklaracija) |
| Corporate income tax return | By the 20th of the month after each tax period (CIT Law art. 17(1)). A period with no taxable base needs no return, except the last month of the reporting year (art. 17(3)). The tax is paid into the single tax account by the 23rd (art. 17(7)) | [CIT Law art. 17](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums) |
| VAT return and payment | Return within 20 days after the end of the tax period (VAT Law art. 118(1)); tax within 23 days (art. 119(1)). The period is a month if taxable supplies were over EUR 50,000 in the previous or current year, or for the intra-EU transactions listed in art. 115(1); the first six calendar months after registration are monthly too (art. 115(2)) | [VAT Law arts. 115, 118, 119](https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| Annual financial statements | Filed with VID within a month of approval, and no later than five months after the year end for micro and small companies, or seven months for medium and large companies and parents preparing consolidated accounts (Annual Reports Law art. 97(1)) | [Annual Reports Law art. 97](https://likumi.lv/ta/id/277779-gada-parskatu-un-konsolideto-gada-parskatu-likums) |
| Annual report of an individual enterprise, farm or fishing household | Required once turnover in the previous reporting year is over EUR 300,000 | [VID, Annual reports](https://www.vid.gov.lv/lv/gada-parskati) |
| Micro-enterprise tax | Quarterly return by the 15th of the month after the quarter, only for a quarter with turnover; tax by the 23rd (Micro-enterprise Tax Law art. 7(2), (3)) | [Micro-enterprise Tax Law art. 7](https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums) |
| Self-employed contributions | Quarterly report in EDS by 17 April, 17 July, 17 October and 17 January; payment by the 23rd of the same months | [VID, Self-employed contributions](https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas) |

The ordinary SIA annual minimum is EUR 50: if annual CIT is below that amount, the last-period return tops it up. It does not apply in the registration year, the year liquidation finishes, an insolvency case, or a year with at least EUR 100 of PIT or social contributions paid for an employee (CIT Law art. 17(11), (12)). [CIT Law art. 17](https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums)

## Worked example

A resident has EUR 126,600 of income subject to progressive PIT in 2026 before the ordinary minimum, and is not a pensioner or another person excluded from that minimum. This illustration assumes no deductible contributions or other reliefs; it isolates the minimum and the band allocation. It is not a self-employed filing computation: paid contributions must be supplied separately and allocated to the lower band first, rather than deducted before testing the EUR 105,300 threshold. The non-taxable minimum for the year is EUR 550 x 12 = EUR 6,600 (PIT Law transitional provision 197(2)), leaving total taxable income of EUR 120,000. The deductions come off the lower band first (PIT Law s. 3(2.4), s. 15(15)): 25.5% on EUR 98,700 (EUR 25,168.50) plus 33% on EUR 21,300 (EUR 7,029.00), giving EUR 32,197.50. Total income is under EUR 200,000, so no 3% surcharge. Because the income is above EUR 105,300, the return is filed between 1 April and 1 July 2027 and, as the tax is over EUR 640, it can be paid in three parts by 23 July, 23 August and 23 September 2027 (PIT Law s. 19(3), (5)).

```oa-check
name: Resident, EUR 126,600 progressive-rate income before deductions, ordinary minimum only, 2026
inputs:
  income_before_minimum: 126600
  monthly_minimum: 550
  band_limit: 105300
steps:
  - minimum: monthly_minimum * 12
  - taxable: income_before_minimum - minimum
  - band_low: (min(income_before_minimum, band_limit) - minimum) * 0.255
  - band_high: max(income_before_minimum - band_limit, 0) * 0.33
  - tax: band_low + band_high
  - instalment: tax / 3
expected:
  minimum: 6600
  taxable: 120000
  band_low: 25168.50
  band_high: 7029.00
  tax: 32197.50
  instalment: 10732.50
```

## Which skill next

- Personal income tax detail: latvia-income-tax
- Company tax on distributions and deemed distributions: lv-corporate-income-tax
- VAT registration, rates and returns: latvia-vat-return
- Social contributions and payroll: latvia-social-contributions, latvia-payroll
- Non-residents and treaties: lv-cross-border; related-party pricing: lv-transfer-pricing
- Choosing between self-employment, micro-enterprise tax and a company: latvia-tax-optimization
- Setting up a business: lv-company-formation

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Taxes and Fees (Par nodokļiem un nodevām), consolidated, art. 14(2)-(5), art. 29(2)-(3.1) read | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-11-17 |
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli), consolidated, s. 2, 3(2), (2.4), 9(1)(2.1), (3.9), 12(1), (2), (4), (5), (9), 15(2), (3), (5), (5.1), (15), (16), 15.1, 19(2), (2.1)-(2.6), (3), (5) and transitional provision 197 read | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-11-17 |
| Corporate Income Tax Law (Uzņēmumu ienākuma nodokļa likums), consolidated, arts. 3, 4, 4.2, 8(1)-(2), article headings 9 to 11, 16(5) and 17 read | https://likumi.lv/ta/id/292700-uznemumu-ienakuma-nodokla-likums | 2026-11-17 |
| Micro-enterprise Tax Law (Mikrouzņēmumu nodokļa likums), consolidated, arts. 1, 2, 2.1, 4 to 9 and transitional provisions 36, 45, 46 read | https://likumi.lv/ta/id/215302-mikrouznemumu-nodokla-likums | 2026-11-17 |
| VAT Law (Pievienotās vērtības nodokļa likums), consolidated, arts. 41, 59, 115, 118 and 119 read | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums | 2026-11-17 |
| Law On State Social Insurance (Par valsts sociālo apdrošināšanu), consolidated, s. 14(2), (5), (18) and 18 and transitional provision 102 read | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu | 2026-11-17 |
| Annual Reports and Consolidated Annual Reports Law, consolidated, art. 97 read | https://likumi.lv/ta/id/277779-gada-parskatu-un-konsolideto-gada-parskatu-likums | 2026-11-17 |
| Accounting Law (Grāmatvedības likums), consolidated, art. 13 read | https://likumi.lv/ta/id/324249-gramatvedibas-likums | 2026-11-17 |
| VID, Personal income tax rates (page updated 31.12.2025), rates table read | https://www.vid.gov.lv/lv/iedzivotaju-ienakuma-nodokla-likmes | 2026-11-17 |
| VID, Mandatory annual income return (page body read: filing window and payment parts) | https://www.vid.gov.lv/lv/obligati-iesniedzama-gada-ienakumu-deklaracija | 2026-11-17 |
| VID, Annual income return (page body read: three-year correction, filing window) | https://www.vid.gov.lv/lv/gada-ienakumu-deklaracija | 2026-11-17 |
| VID, Corporate income tax (page updated 29.10.2026, body read: deferral and deemed distributions) | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodoklis | 2026-11-17 |
| VID, Corporate income tax rates (page updated 16.01.2026, rates table read for the figures used above) | https://www.vid.gov.lv/lv/uznemumu-ienakuma-nodokla-likmes | 2026-11-17 |
| VID, Micro-enterprise tax (page updated 13.05.2026, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodoklis | 2026-11-17 |
| VID, Micro-enterprise tax rate (page updated 22.05.2025, body read for the subjects used above) | https://www.vid.gov.lv/lv/mikrouznemumu-nodokla-likme | 2026-11-17 |
| VID, Self-employed contributions (page updated 08.10.2026, body read: rates, EUR 780 base, report and payment dates) | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas | 2026-11-17 |
| VID, VAT rates (page updated 30.09.2026, rates table read for the figures used above) | https://www.vid.gov.lv/lv/pievienotas-vertibas-nodokla-likmes | 2026-11-17 |
| VID, Annual reports (page body read: EUR 300,000 rule for individual enterprises and farms) | https://www.vid.gov.lv/lv/gada-parskati | 2026-11-17 |

The specified source passages were read on 2026-11-17 from the preserved official-page captures made that day; the read date covers those passages, not every section of each law. The previous version (2026-10-30) read the laws from Internet Archive copies because likumi.lv did not respond that day; the live consolidated texts now replace those copies.

Not yet confirmed: the Micro-enterprise Tax Law changes that start on 1 April 2027 (new art. 7.2 for starting micro-enterprise taxpayers and a new art. 1(1) definition; transitional provision 46): the 2027 wording was not read, so nothing above relies on it.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lv-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lv-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
