---
name: nz-income-tax-ir3
description: >
  Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "IETC", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", "schedular withholding NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. Covers tax rates for 2024-25, 2025-26 and 2026-27, the IR3 structure, deductions, ACC levies, provisional tax, the IETC, penalties and the interaction with GST. Read this skill before touching any NZ income tax work.
version: 2.2
jurisdiction: NZ
tax_year: 2026
tax_year_notes: "Label 2026 means the tax year starting 1 April 2026 (2026-27, Inland Revenue's 2027 income year), whose annual rates are at Bill stage. Returns for 2024-25 and 2025-26 are also covered."
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
type: computation
---

# New Zealand income tax for self-employed individuals (IR3) v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Coverage: the label 2026 means the tax year starting 1 April 2026 (2026-27, which Inland Revenue calls the 2027 income year). The file also covers the returns for 2024-25 (1 April 2024 to 31 March 2025, the prior version's 'FY 2025' and Inland Revenue's 2025 income year) and 2025-26 (1 April 2025 to 31 March 2026, 'FY 2026' and the 2026 income year). The prior version's tax_year of 2025 did not say which of those it meant. IR3 question numbers below are from the 2026 return unless stated; the 2025 return numbers some later questions 1 higher.

## Who this applies to

New Zealand tax-resident natural persons with a 31 March balance date who file an IR3 with self-employed or schedular income, alone or alongside salary, rent, interest or dividends. Inland Revenue is the tax authority and myIR (myir.ird.govt.nz) is the filing portal. A person whose only income is schedular payments need not file an IR3, because Inland Revenue calculates the tax and invites an expense claim (IR3G 2026, Question 12).

### What this file is

This file is a Tier 2 reference with review pending. Each statement has 1 of 4 standings:

- **Enacted.** Read in the Act or regulations on legislation.govt.nz.
- **Practice.** Published by Inland Revenue or ACC. It shows how the agency applies the rule and is not itself the statute.
- **Bill.** Before Parliament and not law.
- **Held.** Not confirmed from a primary source. It is listed on the 'Not yet confirmed' line under Sources.

**Operational hold.** This file does not fill the complete country companion contract in `income-tax-workflow-base`, so it does not support unattended preparation:

- There is no employee-only fixture. The worked examples cover a self-employed client and a mixed client only.
- The pattern library and bank formats are carried from the prior version. Their narrations and file layouts were not tested against bank files.
- The annual rate of income tax for 2026-27 is at Bill stage, so a 2026-27 figure is an estimate.
- The companions `nz-provisional-tax`, `nz-acc-levies`, `nz-gst-return`, `new-zealand-gst`, `nz-tax-residency`, `nz-capital-gains` and `new-zealand-crypto-tax` have not been converted, and conflicts with them are listed under Source conflicts.

**Reviewer warning.** Any working paper produced under this file is a working paper only. It must show which inputs were confirmed and which are Needs Input, and it must carry the label 'estimated, not reviewed'.

### Question threshold

Tier 2 question threshold: NZD 0. No row is filtered on amount: a material question goes to the client or the reviewer whatever its size, because no text read sets a floor.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do not classify part of the file first. Where a trigger is only suspected, ask the client the question that resolves it.

- **R-NZ-1, GST position cannot be established.** Trigger: the client is or may be GST-registered, and the income or expense figures mix GST-inclusive and GST-exclusive amounts that the records cannot separate. Message: 'Stop. I cannot compute this return until GST status for the year and the GST in the income and expense figures are established.'
- **R-NZ-2, company income in the personal file.** Trigger: income of a company is mixed with personal income for the IR3. Message: 'Stop. Company income is not personal income. Only what the company paid you, such as salary or dividends, goes in the IR3. This needs a reviewer.'
- **R-NZ-3, non-resident.** Trigger: the client is not New Zealand tax resident and has New Zealand-source income. Message: 'Stop. This file does not cover non-residents. A different return and different tax rules apply, so this needs a reviewer.'
- **R-NZ-4, large vehicle claim without evidence.** Trigger: the claim rests on business use above 25% and the client has no actual records of business use and no logbook term, whether or not a kilometre rate election is in place. Message: 'Stop. A vehicle claim above 25% needs actual records or a logbook term. A kilometre rate election does not show the business share. Without one of them the claim cannot be prepared.'
- **R-NZ-5, possible employment.** Trigger: the client's main relationship looks like employment, with regular directed work for 1 payer. Message: 'Stop. This relationship may be employment. It cannot be treated as self-employment without a reviewer applying the Inland Revenue tests.'
- **R-NZ-6, outside coverage.** Trigger: the requested year is before 2024-25, or the person has a balance date other than 31 March. Message: 'Stop. This file covers individuals with a 31 March balance date for 2024-25 to 2026-27 only.'

### Required inputs

**Minimum viable:** the bank statement for the full tax year (1 April to 31 March) as CSV, PDF or pasted text, and confirmation of GST registration status for the year.

**Recommended:** client invoices, the Summary of Income, dividend statements, vehicle records, the ACC invoice, provisional tax payment receipts and the prior year IR3.

**Ideal:** complete accounting records (Xero or MYOB export), GST return summary, depreciation schedule and the prior year notice of assessment.

### Prohibitions

- Never include GST in income or expenses of a GST-registered person where the amount carried GST. Never strip 3/23 from an amount before verifying it carried GST at 15%.
- Never claim vehicle business use above 25% without actual records or a logbook term. A kilometre rate election sets the method; it does not show the business share.
- Never apply the 50% entertainment limit to a cost outside the rule, and never claim more than 50% of a cost within it.
- Never deduct provisional tax, income tax or GST payments to Inland Revenue.
- Never apply the IETC for a month in which a condition in section LC 13 failed, including Working for Families that the person or a partner is both entitled to and receiving (entitlement alone before 30 March 2025) or NZ Super.
- Never add the ACC earners' levy paid on self-employed income to RIT, or use it to test the NZD 5,000 provisional tax threshold.
- Never confuse the ACC earners' levy, invoiced by ACC and not in RIT, with the ACC work levy, a deductible expense.
- Never credit the earners' levy withheld with PAYE as income tax. Credit tax deducted after the levy (Box 11E).
- Never treat schedular net receipts as gross income. Gross up only from a verified rate or the Summary of Income.
- Never apply resident rates to non-residents.
- Never present a calculation as final. Label it 'estimated, not reviewed' and direct the client to a qualified New Zealand tax professional.

## Rates, bands and thresholds

### Personal income tax

Tax is imposed by section BB 1 of the Income Tax Act 2007 (ITA) at rates fixed by an annual taxing Act. Rates apply to taxable income, not to gross receipts.

**2025-26 and later Schedule 1 rates.** Enacted.

| Taxable income (NZD) | Rate | Tax on band | Cumulative tax | Official source |
| --- | --- | --- | --- | --- |
| 0 to 15,600 | 10.5% | 1,638.00 | 1,638.00 | [ITA Schedule 1 Part A cl 1 Table 1](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| 15,601 to 53,500 | 17.5% | 6,632.50 | 8,270.50 | [ITA Schedule 1 Part A cl 1 Table 1](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| 53,501 to 78,100 | 30% | 7,380.00 | 15,650.50 | [ITA Schedule 1 Part A cl 1 Table 1](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| 78,101 to 180,000 | 33% | 33,627.00 | 49,277.50 | [ITA Schedule 1 Part A cl 1 Table 1](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Over 180,000 | 39% | on excess | 49,277.50 + 39% | [ITA Schedule 1 Part A cl 1 Table 1](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |

The table was replaced from 1 April 2025 by section 37(1) of the Taxation (Budget Measures) Act 2024, applying for 2025-26 and later income years (section 37(4)). The annual rate for 2025-26 is set by section 3 of the Taxation (Annual Rates for 2025-26, Compliance Simplification, and Remedial Measures) Act 2026 (2026 No 8).

**2024-25 composite rates.** Enacted. The thresholds changed from 31 July 2024, so one composite table applies to the whole of 2024-25. Never apply it to another year.

| Taxable income (NZD) | Rate | Tax on band | Cumulative tax | Official source |
| --- | --- | --- | --- | --- |
| 0 to 14,000 | 10.5% | 1,470.00 | 1,470.00 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 14,001 to 15,600 | 12.82% | 205.12 | 1,675.12 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 15,601 to 48,000 | 17.5% | 5,670.00 | 7,345.12 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 48,001 to 53,500 | 21.64% | 1,190.20 | 8,535.32 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 53,501 to 70,000 | 30% | 4,950.00 | 13,485.32 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 70,001 to 78,100 | 30.99% | 2,510.19 | 15,995.51 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| 78,101 to 180,000 | 33% | 33,627.00 | 49,622.51 | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |
| Over 180,000 | 39% | on excess | 49,622.51 + 39% | [Taxation (Budget Measures) Act 2024 s 7(1), (4)](https://www.legislation.govt.nz/act/public/2024/19/en/latest/) |

The annual rate for 2024-25 is set by section 3 of the Taxation (Annual Rates for 2024-25, Emergency Response, and Remedial Measures) Act 2025 (2025 No 9). Inland Revenue's Tax rates for individuals page shows both tables. Taxable income of NZD 60,000 bears NZD 10,220.50 at the 2025-26 rates and NZD 10,485.32 at the 2024-25 rates.

**2026-27.** Bill. The Schedule 1 table above has no end date, but no annual taxing Act for 2026-27 was found at the read date. Clause 3 of the Taxation (Annual Rates for 2026-27, FBT Simplification, Foreign Investment Funds, and Remedial Measures) Bill, Government Bill 344-1, would set the 2026-27 rate at the Schedule 1 basic rates. Parliament's page, dated 16 September 2026, shows it at the Finance and Expenditure Committee and records that Parliament would dissolve on 1 October 2026, with a new committee to decide when submissions close. Label any 2026-27 figure as an estimate on Bill rates. Section 92A of the Tax Administration Act 1994 (TAA) allows assessment at basic rates before the annual Act passes, with an adjustment if the annual rates differ (section 92A(2)). It does not settle the rate.

### Independent earner tax credit (IETC)

Enacted in ITA subpart LC. Practice: IR3G 2026, Question 33. The test uses annual **net income**: total income from all sources less deductions and current-year losses, before losses brought forward (Box 30, 'Income after expenses').

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Credit if net income is NZD 24,000 or more | NZD 520 for a full year | 2025-26 and later | [ITA s LC 13(4)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Credit if net income is below NZD 24,000 | Nil | 2025-26 and later | [ITA s LC 13(4)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Abatement above NZD 66,000 | 13 cents for each complete dollar of the excess | 2025-26 and later | [ITA s LC 13(5)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Credit reaches nil | At NZD 70,000 net income | 2025-26 and later | [ITA s LC 13(2), (5)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Credit period | Whole months in which all conditions held | 2025-26 and later | [ITA s LC 13(6)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| 1 April to 30 July 2024 | NZD 520, abated above NZD 44,000 | 2024-25 | [ITA s LC 14](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| 31 July 2024 to 31 March 2025 | NZD 520, abated above NZD 66,000 | 2024-25 | [ITA s LC 15](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |

```text
2025-26 and later:
ietc = max(person_credit - abatement, 0) * credit_period_months / 12
person_credit = 520 if net_income >= 24000 else 0
abatement = 0.13 * max(floor(net_income) - 66000, 0)

2024-25, eligible all year, floored reading (sections LC 13(2), LC 14 and LC 15):
a = max(person_credit - 0.13 * max(floor(net_income) - 44000, 0), 0)
b = max(person_credit - 0.13 * max(floor(net_income) - 66000, 0), 0)
ietc = (a * 121 + b * 244) / 365

2024-25, eligible all year, printed boxes (IR3G 2025 worksheet, no floor at Boxes D and I):
a_printed = person_credit - 0.13 * max(floor(net_income) - 44000, 0)
b_printed = person_credit - 0.13 * max(floor(net_income) - 66000, 0)
ietc = (a_printed * 121 + b_printed * 244) / 365

2024-25, eligible for part of the year:
statute: (a * days_in_first_period + b * days_in_second_period) / 365
IR3G 2025 worksheet: (a * 121 + b * 244) / 365 * eligible_months / 12, with a and b floored or as printed
```

The 2 part-year routes give different results, and the prior version's months formula is the worksheet route, not the statutory one. Sections LC 14 and LC 15 say 'credit period days ÷ 365'. Show both figures and leave the choice to the reviewer.

The floor is a second open conflict, and it is held. Section LC 13(2) says 'positive amount' and IR3G 2025 says the credit applies to net income between NZD 24,000 and NZD 48,000 before 31 July 2024, which supports flooring each period. Sections LC 14 and LC 15 do not repeat 'positive', and the IR3G 2025 worksheet prints no floor at Boxes D and I. The 2 readings differ for net income above NZD 48,000. Show both figures and leave the choice to the reviewer. For a full year of eligibility, net income of NZD 45,000 gives NZD 476.90 on both readings. Net income of NZD 67,000 gives NZD 260.71 floored and NZD (558.11) on the printed boxes; no text read allows a negative credit.

The conditions in section LC 13(1) must all hold for the period. The person:

- is not receiving a main benefit, a veteran's pension or New Zealand superannuation
- is not both entitled to and receiving a Working for Families (WFF) tax credit
- is not the partner of a person who is both entitled to and receiving a WFF tax credit
- is not receiving an overseas equivalent of any of those payments, and has no partner receiving an overseas equivalent of a WFF tax credit
- is resident in New Zealand.

Section 105 of the 2025 No 9 Act added receipt to both WFF conditions on 30 March 2025. From that date, entitlement without receipt does not fail them. Up to 29 March 2025 the words were 'not entitled', so entitlement alone failed them, whether or not WFF was received.

Inland Revenue's practice is that a condition failing on 1 day in a month removes that whole month. The IETC is not listed in ITA s LA 6(1), a non-refundable credit left over is extinguished under section LA 5(2), and the IR3G worksheet floors the result at nil. It can be given through a tax code during the year or claimed in the IR3.

### Provisional tax

Full method detail is in `nz-provisional-tax`.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Liability threshold | RIT more than NZD 5,000, or an election under section RC 4 | All covered years | [ITA s RC 3(1)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| No obligation | RIT of the preceding tax year is NZD 5,000 or less | All covered years | [ITA s RC 3(3)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Standard method | 105% of preceding-year RIT, truncated to whole dollars | All covered years | [ITA s RC 5(2), (4B)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Standard method uplift when the preceding return is outstanding | 110% of RIT for the year before the preceding year, when that return is not yet due and not provided by the instalment date, other than instalment F | All covered years | [ITA s RC 5(3)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| GST ratio method limit | Preceding-year RIT more than NZD 5,000 and no more than NZD 150,000, plus the other tests in section RC 16 | All covered years | [ITA s RC 16](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Interest window, standard method | RIT under NZD 60,000 and no estimate, AIM, GST ratio or interest avoidance arrangement: no interest either way before the terminal tax date | All covered years | [TAA s 120KE(1), (2)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |

The **estimation method** is in sections RC 5(5) and RC 7 and requires a fair and reasonable estimate. **AIM** is in sections RC 5(5B) and RC 7B and has its own gates, including annual gross income of NZD 5,000,000 or less in the listed cases. Inland Revenue treats a person as on the standard option unless they choose otherwise (IR289: 'If you do not make a choice, the standard option will apply'). That is practice; whether the 105% or the 110% limb applies still needs the filing facts.

**New provisional taxpayers.** Enacted, ITA s YA 1 'initial provisional tax liability'. A natural person has one for a tax year if RIT was NZD 5,000 or less in each of the preceding 4 years, RIT is NZD 60,000 or more in that year, and in that year they stopped deriving income from employment and then started to derive income from a taxable activity. A one-off high RIT year for an established sole trader does not meet it. Practice (IR3G 2026, IR289): no provisional tax is payable in that year, and voluntary payments reduce the interest. Interest is calculated under TAA s 120KC as if provisional tax were payable (section RC 9(9)).

### GST thresholds used in this file

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Standard rate on taxable supplies by a registered person | 15% | All covered years | [Goods and Services Tax Act 1985 (GST Act) s 8(1)](https://www.legislation.govt.nz/act/public/1985/141/en/latest/) |
| Compulsory registration, looking back | Total value of supplies in the month and preceding 11 months has exceeded NZD 60,000, unless the Commissioner is satisfied the next 12 months will not exceed it | All covered years | [GST Act s 51(1)(a)](https://www.legislation.govt.nz/act/public/1985/141/en/latest/) |
| Compulsory registration, looking forward | Reasonable grounds to believe the next 12 months will exceed NZD 60,000, with the provisos in section 51(1)(c) and (d) | All covered years | [GST Act s 51(1)(b)](https://www.legislation.govt.nz/act/public/1985/141/en/latest/) |

The test is the value of supplies, excluding GST (section 51(6)), not gross income. GST returns are in `nz-gst-return` and `new-zealand-gst`.

### ACC levies

Levies are not income tax and are not in RIT. Rates are per NZD 100 of liable earnings. Regulation rates exclude GST; Inland Revenue's published rates include it.

| Levy | Rate or cap | Tax year | Official source |
| --- | --- | --- | --- |
| Earners' levy, GST-exclusive | NZD 1.45 | 2025-26 | [Accident Compensation (Earners' Levy) Regulations 2025 (SL 2025/18) reg 4](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/) |
| Earners' levy, GST-exclusive | NZD 1.52 | 2026-27 | [SL 2025/18 reg 4](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/) |
| Earners' levy, GST-exclusive | NZD 1.59 | 2027-28 and later | [SL 2025/18 reg 4](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/) |
| Earners' levy, GST-inclusive | NZD 1.60 | 2024-25 | [Inland Revenue, ACC earners' levy rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates); [IR3G 2025](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2025.pdf) |
| Earners' levy, GST-inclusive | NZD 1.67 | 2025-26 | [Inland Revenue, ACC earners' levy rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates); [IR3G 2026](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf) |
| Earners' levy, GST-inclusive | NZD 1.75 | 2026-27 | [Inland Revenue, ACC earners' levy rates](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates) |
| Maximum liable earnings | NZD 142,283 | 2024-25 | [ACC, Calculate your levies](https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies); [IR3G 2025](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2025.pdf) |
| Maximum liable earnings | NZD 152,790 | 2025-26 | [SL 2025/18 reg 5](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/); [SL 2025/17 reg 6](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/) |
| Maximum liable earnings | NZD 156,641 | 2026-27 | [SL 2025/18 reg 5](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/); [SL 2025/17 reg 6](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/) |
| Minimum liable earnings, self-employed over 30 hours a week | NZD 44,250 | 2024-25 | [ACC, Calculate your levies](https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies) |
| Minimum liable earnings, self-employed over 30 hours a week | NZD 49,365 | 2025-26 | [SL 2025/18 reg 6](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/); [SL 2025/17 reg 7](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/) |
| Minimum liable earnings, self-employed over 30 hours a week | NZD 50,501 | 2026-27 | [SL 2025/18 reg 6](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/); [SL 2025/17 reg 7](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/) |
| Work levy | By classification unit | 2025-26 and 2026-27 | [Accident Compensation (Work Account Levies) Regulations 2025 (SL 2025/17), amended by SL 2026/30, Schedules 1 to 3](https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/) |

NZD 139,384 was the 2023-24 maximum. The 2024-25 minimum is Practice, because the 2024-25 regulation was not read. For 2025-26 and later the minimum is a formula, not a flat base. A self-employed person who worked an average of more than 30 hours a week, whether or not as an employee, and earned less than the threshold pays, at GST-exclusive rates, 1.45 × [(NZD 49,365 − a) ÷ 100] for 2025-26, 1.52 × [(NZD 50,501 − a) ÷ 100] for 2026-27 and 1.59 × [(NZD 51,632 − a) ÷ 100] for 2027-28 and later, where a is the person's earnings as an employee (SL 2025/18 reg 6). The work levy minimum makes the same offset (SL 2025/17 regs 7 and 9). The minimum does not apply to a person working an average of 30 hours a week or less. Regulation 7 displaces both the minimum and the ordinary calculation on earnings, though the multiplier is the same (SL 2025/18 regs 4 and 7). A self-employed person who, in relation to the tax year, agrees with ACC under section 209 of the Accident Compensation Act 2001 to purchase weekly compensation pays 1.45 × [(1.25 × a) ÷ 100] for 2025-26, 1.52 × [(1.25 × a) ÷ 100] for 2026-27 and 1.59 × [(1.25 × a) ÷ 100] for 2027-28 and later, where a is now the agreed level of weekly compensation adjusted to an annual figure, whatever the person earned. The reg 5 maximum still applies (reg 4(4)). ACC's pages describe CoverPlus Extra as its optional product but do not cite section 209, so confirm the agreement from the ACC invoice. Under SL 2025/17 Part 3 the same person pays a compensation levy at Schedule 4, 5 or 6 rates, and the Work Account levy stays payable for any period with no agreement (regs 11 to 15). The Working Safer levy is collected by ACC for WorkSafe at a fixed rate per NZD 100, per ACC's invoice pages. Its rate is held. This file prints no classification unit rate, and the ACC Levy Guidebook 2026-27 was not read, because it is blocked at source. ACC invoices the self-employed person after filing, using income Inland Revenue passes on, so a first invoice can arrive in the second year. Levy detail is in `nz-acc-levies`.

### Kilometre rates

The method is Enacted (ITA s DE 12) and the Commissioner sets the rates under section DE 12(4). The 2025-26 rates are in the Income Tax (Kilometre Rates for the Business Use of Vehicles for the 2025-26 income year) Instrument 2026, OS 19/04 (KM 2026), and the 2024-25 rates in OS 19/04 (KM 2025). Both are published on Inland Revenue's Tax Technical site, not legislation.govt.nz, so this file labels them Practice. Inland Revenue publishes each year's rates after year end, so 2026-27 rates are held. The rates include depreciation, so a person on this method has no depreciation deduction (OS 19/04a, paragraph 12). Tier 1 applies to the business proportion of the first 14,000 km the vehicle travels in the year, business and private; Tier 2 applies beyond that. A vehicle type outside the table uses the costs method (OS 19/04a, paragraph 11).

| Vehicle | 2025-26 Tier 1 | 2025-26 Tier 2 | 2024-25 Tier 1 | 2024-25 Tier 2 | Official source |
| --- | --- | --- | --- | --- | --- |
| Petrol | NZD 1.20 | NZD 0.37 | NZD 1.17 | NZD 0.37 | [Inland Revenue, Kilometre rates 2025-2026 and 2024-2025](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026) |
| Diesel | NZD 1.30 | NZD 0.38 | NZD 1.26 | NZD 0.35 | [Inland Revenue, Kilometre rates 2025-2026 and 2024-2025](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026) |
| Petrol hybrid | NZD 0.90 | NZD 0.24 | NZD 0.86 | NZD 0.21 | [Inland Revenue, Kilometre rates 2025-2026 and 2024-2025](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026) |
| Electric | NZD 1.22 | NZD 0.23 | NZD 1.08 | NZD 0.19 | [Inland Revenue, Kilometre rates 2025-2026 and 2024-2025](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026) |

### Square metre rate for home offices

The method is Enacted (ITA s DB 18AA) and the Commissioner sets and publishes the rates under section DB 18AA(5). Practice: NZD 57.30 for 2025-26 and NZD 55.60 for 2024-25. The 2026-27 rate is held.

### Schedular withholding rates

Enacted. ITA Schedule 4 sets the default for each activity. Section RD 10B applies, in order, an elected rate (TAA s 24F(3)) or special rate (TAA s 24G), otherwise Schedule 4; a rate notified by the Commissioner (TAA s 24F(4)) overrides; and 45% applies where the recipient gives no name and tax file number. Inland Revenue's practice is that a chosen rate is at least 10%, or 15% for a non-resident on a temporary work or entry visa.

| Activity | Rate | Tax year | Official source |
| --- | --- | --- | --- |
| Non-resident contractors | 15% | All covered years | [ITA Schedule 4 Part A](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Directors' fees, examiners' fees, honoraria and listed payments | 33% | All covered years | [ITA Schedule 4 Part B](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Work or services relating to primary production | 15% | All covered years | [ITA Schedule 4 Part C](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Commercial cleaning or maintenance work | 20% | All covered years | [ITA Schedule 4 Part D](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Listed general contracting work | 15% | All covered years | [ITA Schedule 4 Part D](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Labour-only building or fishing boat work | 20% | All covered years | [ITA Schedule 4 Part E](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Sports, media, entertainment and public speaking | 25%, 20% or 15% by payment type | All covered years | [ITA Schedule 4 Part F](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Sales commission | 20% | All covered years | [ITA Schedule 4 Part G](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Purchases of schedular natural products | 25% | All covered years | [ITA Schedule 4 Part H](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Personal service rehabilitation payments | 10.5% | All covered years | [ITA Schedule 4 Part I](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Labour-hire arrangements | 20% | All covered years | [ITA Schedule 4 Part J](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Voluntary schedular payments | 20% | All covered years | [ITA Schedule 4 Part W](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |

## The base

### From receipts to net income

Taxable income is net income less any tax loss used (ITA s BC 5, s IA 4). Net income is total assessable income less deductions. A deduction needs the general permission in section DA 1 and must clear the general limitations in section DA 2.

| Item | IR3 2026 | Treatment |
| --- | --- | --- |
| Salary and wages | Question 11 | From the Summary of Income or payslips. Credit Box 11E, tax deducted after the earners' levy, not Box 11A |
| Schedular payments | Question 12 | Gross at Box 12B (GST-exclusive if registered), tax at Box 12A, related expenses at Box 12C, net at Box 12D. Not at Question 24, and not at Question 29 for the expenses |
| New Zealand interest | Question 13 | Gross, with RWT as a credit (ITA s LB 3) |
| New Zealand dividends | Question 14 | Net dividend plus imputation and RWT credits (ITA s LE 1). Take the imputation credit and RWT from the dividend statement. Excess imputation credits use Question 34 |
| Overseas income and tax | Question 17 | In NZD, with tax paid at Box 17A (ITA s LJ 2) |
| Residential rent | Question 22 and IR3R | See Rental below. Record the basis, portfolio or property. For 2024-25, interest also goes at Question 23 of the 2025 return (Boxes 23A to 23C). The prior version's 'Schedule E' is not a New Zealand form |
| Self-employed income | Question 24 | Net of business expenses, with the IR3B or IR10 support the return guide requires |
| Other expenses | Question 29 | For example a fee for preparing the return, interest charged by Inland Revenue and income protection premiums (IR3G 2026) |
| Losses | Question 31 | Boxes 31A and 31B |

Tax refunds, provisional tax and GST paid to Inland Revenue are neither income nor deductions (ITA s DB 1 for income tax; s CX 1 and s DB 2 for GST).

### GST and income tax

For a GST-registered person, output tax is excluded income (ITA s CX 1) and input tax is not deductible (ITA s DB 2), so the IR3 carries GST-exclusive amounts. Only strip GST from an amount after verifying it carried GST at 15%, using the taxable supply information, a supplier invoice or the GST return workings. A zero-rated supply, an exempt supply or a purchase from an unregistered supplier carries no GST to strip. Until verified, the GST treatment of that line is Needs Input. Verified at 15%: GST is amount × 3/23. Verified as not carrying GST: use face value. Test both cases where the line is material.

A person who is not registered reports income at face value and claims costs including GST (Inland Revenue, home business page).

### Schedular payments

Gross income is the amount before withholding. Take gross and tax from the Summary of Income (Boxes 12A and 12B) where it is available. Where it is not, gross = net received ÷ (1 − rate), using the rate actually applied. The prior version's 20% default has no statutory basis: rates run from a special rate or a 10% election up to 45%, so an unknown rate is Needs Input. Inland Revenue form IR330C is how a contractor chooses a rate. A rate election on file is evidence of the rate to be applied, not proof of what was withheld.

### Expenses

- **Entertainment.** Enacted, ITA subpart DD. Section DD 1(2) limits the deduction to 50% only for the kinds of entertainment in section DD 2 where the person has both a private and a business benefit. Sections DD 4 to DD 8 set further limits on the rule, and section DD 7 takes entertainment outside New Zealand out of the limit. The prior version applied 50% to all restaurant and cafe narrations; that is too wide. A person's own meals are private unless the extra-cost rules for remote locations or unusual hours apply (Inland Revenue, meal page). A business lunch with clients is 50% per Inland Revenue (IR268). Keep a record of the people, the date and the reason. Purely social cost is nil.
- **Motor vehicles.** Enacted, ITA subpart DE. It apportions a vehicle used partly for business; it does not apply to most companies, to a person whose only income is employment income, or to a vehicle used only to derive income (section DE 1(2)). Section DE 3 gives 2 ways to calculate the proportion of business use: actual records showing the reasons for and the distance of business journeys (section DE 5), and a logbook kept for at least 90 consecutive days that gives a term of up to 3 years, with total distance also recorded (sections DE 6 to DE 8). The method of deduction is a separate choice. A person elects the kilometre rate method in the return for the income year that includes the latest of 1 April 2017, the day they acquire the vehicle and the day they first use it for business (section DE 2B(1)). With no election they are treated as electing the costs method (section DE 2B(2)). Either election cannot be revoked and applies until the end of the income year of disposal (section DE 2B(3)). A kilometre rate election sets the method only: section DE 12(3)(c) still takes the business proportion from sections DE 5 to DE 11, and OS 19/04a says the person must use a logbook or actual records. With no records, no logbook term and no kilometre election, section DE 4 limits the deduction to the lesser of actual business use and 25%. So 25% is a cap, not a deemed share: if actual business use is unknown, the share is Needs Input. A client with a kilometre election and no records or logbook term is also Needs Input and never goes above 25%, because section DE 4(1)(c) takes them out of section DE 4 and the Act gives no figure (see Source conflicts). A person on the kilometre method records the odometer at each balance date and must be able to show when the vehicle passes 14,000 km (OS 19/04a, paragraphs 10 and 21). Travel between home and work is private.
- **Home office.** Enacted for the square metre method, ITA s DB 18AA, which a person may choose; Operational Statement OS 19/03 is Practice on how it runs. The formula is (a × b) + (c × d). Here a is mortgage interest, rates and rent paid in the year for the buildings and their curtilage, c is the area of the buildings that is separately identifiable and used primarily for the business, b is c ÷ total area of buildings on the premises, and d is the published rate. A person using it claims no other deduction for business use of the premises (section DB 18AA(4)). Otherwise apportion actual costs by time and space. For a farmhouse OS 19/03 points to IS 17/02, which was not read. The prior version's 'only if dedicated workspace' does not match that second route. Depreciation on the home itself is not allowed.
- **Phone and internet.** Practice. A private landline is 50%, business tolls 100% and a separate business line 100%. Internet use is a fair and reasonable estimate. The prior version's 'commonly 50-80%' is unsupported, so document the actual share.
- **ACC levies.** ITA s EF 3 allocates a levy deduction to the year it is due and payable, and is a timing rule, not a permission. The work levy on a business qualifies through section DA 1, with section EF 3(5)(c) naming the Work Account levy. Section EF 3(5)(d) also names the Earners' Account levy. Practice: IR3B Box 9 tells a person to include 'ACC levy payments for self-employment', amongst deductible expenses, which points to a deduction but does not name the earners' levy. No statute read gives the answer, so whether a self-employed person's earners' levy is deductible is held. Do not state either answer.
- **Tax-return costs.** ITA s DB 3. **Use of money interest payable.** ITA s DB 3B, allocated to the year paid by section EF 5. **Income tax and civil penalties.** Not deductible (ITA s DB 1).
- **Depreciation and new assets.** Subpart EE. Investment Boost in subpart DI allows a deduction of 20% of the cost, less listed contributions (section DI 5), for an asset never previously used or available for use in New Zealand, if chosen in the return (section DI 2). Depreciable property must first become available for use on or after 22 May 2025, and for other assets the expenditure must be incurred on or after that date. A dwelling, fixed life intangible property and the petroleum and mining rights listed are excluded (section DI 4(b)).
- **Mixed use.** A mixed personal and business cost needs a business share. Without one it is Needs Input, not nil and not a default. Holiday homes and similar assets fall under subpart DG and go to the reviewer.

### Losses

A tax loss arises under section IA 2. A person may use it to pay a shortfall penalty (section IA 3(1)), and the balance carries forward (section IA 3(4)), subject to overrides including bankruptcy (section IA 3B). It is subtracted from net income first (section IA 4(1)), in the order the losses arose (section IA 9). Ring-fenced (section IA 7) and schedular (section IA 8) losses have their own limits. A hobby has no loss: Inland Revenue's hobby tests decide whether there is a business at all. Confirm the balance from the prior return, Box 31A.

### Rental

Rental goes in Question 22 and the IR3R. Subpart DH, the residential interest limit, was repealed on 1 April 2025 (Taxation (Annual Rates for 2023-24, Multinational Tax, and Remedial Matters) Act 2024, section 48), so the prior version's 'interest deductibility limited' is out of date for 2025-26 onward. For 2024-25 the limit still applies. Enacted: the Act as at 30 March 2025 denies 20% of interest incurred from 1 April 2024 to 31 March 2025 where it falls within section DH 8(1), which covers disallowed residential property and grandparented residential interest (sections DH 2, DH 5, DH 7 and DH 8(2)), with the exemptions in section DH 4. Practice: IR3G 2025 says 80% can be claimed, whenever the property was acquired or the loan drawn down, with Boxes 23A to 23C at Question 23.

Section EL 4 limits residential deductions to residential income and carries the excess forward, on a portfolio basis unless the person chooses the property basis under section EL 6. Under the choice, the excess on a property carries forward against income from that property (section EL 6(3)). The choice is made by taking that tax position in the return for the year the property becomes residential rental property (section EL 6(4)), and it holds whilst the position continues (section EL 6(5)). Question 22 asks for the method: portfolio, individual property or a combination, with separate records, and a look-through company owner uses the company's method (IR3G 2026). Sections EL 5 and EL 7 release excess on a taxed disposal. The exclusions are in sections EL 9 to EL 13, and Inland Revenue lists a main home, mixed-use assets, revenue account land, farmland, business premises, some company land and employee accommodation.

### Bright-line property

Enacted. For a disposal under section CB 6A as replaced from 1 July 2024, an amount derived from disposing of residential land is income if the bright-line end date is within 2 years of the start date. The start date is usually the date the transfer instrument was registered (section CB 6A(2)). The end date is the earliest of the agreement to dispose, a gift, compulsory acquisition and a mortgagee sale, or else the date of disposal (section CB 6A(4)). Exclusions are in section CB 6A(5). The section applies where the end date is on or after 1 July 2024, whatever the purchase date (Taxation (Annual Rates for 2023-24, Multinational Tax, and Remedial Matters) Act 2024, section 8(4)). For an earlier end date, section CB 6A as at 30 June 2024 set a 10-year test and a 5-year test for new build land, and did not apply to land first acquired before 27 March 2021 (section CB 6A(1AB)). Practice: Inland Revenue gives 5 years for land acquired from 29 March 2018 to 26 March 2021. IR1229 sets out the 2-year test. Section CB 6A was later amended by the 2025 No 9 Act. Confirm purchase and sale dates with a reviewer. This file does not compute a gain. See `nz-capital-gains`.

### From net income to RIT

Follows ITA ss BC 5 to BC 8, LA 4, YA 1 'residual income tax' and the IR3G 2026 Question 36 worksheet (Question 37 in the 2025 return). Each floor down to `after_imputation` is printed in that worksheet. The `rit` floor comes from YA 1.

```text
taxable_income = max(net_income - tax_loss_used, 0)
tax = schedule rates on taxable_income
after_ietc = max(tax - ietc, 0)
after_overseas = max(after_ietc - overseas_tax_box_17a, 0)
after_imputation = max(after_overseas - (imputation_box_14 + excess_imputation_box_34), 0)
credits = overpaid_pie_tax_box_35c + tax_credit_subtotal_box_21a
rit = max(after_imputation - credits, 0)
excess_credits = max(credits - after_imputation, 0)
to_pay_or_refund = rit - excess_credits - provisional_tax_paid
```

Box 21A is the subtotal of tax credits in the return, including tax deducted at Boxes 11E and 12A and RWT. RIT is the positive amount, if any, left after the credits in YA 1, so it is never negative. Where credits are larger, RIT is nil and the excess is kept for settlement. The worksheet shows that excess at Box 14 as a credit, and Box 16 adds provisional tax to give the refund. Only refundable credits reach a refund. Section LA 6(1) lists those for PAYE, provisional tax, RWT and certain other items, and section LA 6(2) uses them against other years' tax and later provisional tax before any refund. ACC levies invoiced by ACC are not in this calculation. Where overseas tax exceeds the tax at that step, the worksheet prints nil and sends the reader to its note on tax paid overseas. Excess imputation credits carry forward (IR3G 2026). The credit ordering in law is section LA 4.

Early payment discount: Enacted, ITA ss RC 37 to RC 40, claimed at IR3 Question 37. A small-business person acts alone, as a partner or as a look-through company owner, uses no company or trust in the business, and derives income mainly from the business and not as interest, dividends, royalties, rent or beneficiary income (section RC 40). Section RC 37 needs no obligation under section RC 3(3), and either no earlier provisional tax liability and no earlier discount, or a period of 4 income years with no assessable business income since the latest such year. Section RC 38(1) needs income tax paid on or before balance date, a credit in the tax account from balance date to terminal tax date of at least the lesser of that payment and terminal tax, a filed return and an application on or before the last date for filing under TAA s 37(5). The discount is the rate times the lesser of the amount paid and 105% of RIT (section RC 38(3)). The rate is 2% above the paying rate at the end of the preceding tax year (section RC 38(4)(a)): 6.67% for the 2025 income year, 6.30% for 2026 and 4.25% for 2027, which match Inland Revenue's published rates. Application dates differ between sources: see Source conflicts.

### Tier 1 facts, Tier 2 judgement and defaults

No default below names a tax result that depends on an unverified fact.

| Situation | Treatment | Basis |
| --- | --- | --- |
| GST-inclusive or exclusive unclear | Needs Input for that line; R-NZ-1 if the file cannot be separated | GST Act s 8; ITA s CX 1, s DB 2 |
| Mixed personal and business cost | Needs Input | ITA s DA 1, s DA 2 |
| Home office | Square metre method or apportionment, both need the area figures | ITA s DB 18AA; Inland Revenue, home business page |
| Vehicle, no records, logbook term or kilometre election | Lesser of actual business use and 25%; actual use still needed | ITA s DE 4 |
| Vehicle, kilometre election, no records or logbook term | Needs Input; the Act gives no figure, and never above 25% | ITA ss DE 3, DE 4(1)(c), DE 12(3)(c); see Source conflicts |
| Schedular rate unknown | Needs Input; use the Summary of Income | ITA s RD 10B |
| ACC levy amount uncertain | Use the ACC invoice. An estimate uses the earners' levy, under SL 2025/18 reg 7 where weekly compensation is purchased, and the classification unit rate from `nz-acc-levies` and is labelled as such; the Working Safer rate stays held | SL 2025/18; SL 2025/17 |
| Provisional method not stated | Confirm with the client. Inland Revenue treats a person as standard unless they choose otherwise; 105% or 110% is Needs Input | Inland Revenue, standard option; ITA s RC 5 |
| IETC months unknown | Needs Input; no credit is calculated | ITA s LC 13 |
| GST status unknown | Needs Input; the prior 'non-registered, face value' fallback is withdrawn | GST Act s 51 |

### Reviewer attention thresholds

These are reviewer heuristics, not law, except where a source is shown.

| Flag | Threshold | Basis |
| --- | --- | --- |
| Provisional tax | RIT more than NZD 5,000: check obligation and payments | ITA s RC 3 |
| GST registration | Value of supplies has exceeded NZD 60,000 in 12 months: verify | GST Act s 51 |
| Vehicle | Vehicle expenses above 50% of all expenses: check the evidence | Heuristic |
| Cash | Cash income with no trail: document carefully | Heuristic |
| Single contractor | Regular, directed work for 1 payer: check R-NZ-5 | Inland Revenue, self-employed or employee |

### Classifying a bank line

Use this list before the Tier rules. If no pattern matches, ask. A match sets the category only: every row keeps the GST, schedular and business-share conditions above.

**Credits**

| Pattern | Return line | Treatment |
| --- | --- | --- |
| PAYMENT FROM [client] / TFR FROM [client] | Self-employed income | Gross revenue, standard bank credit from a client |
| INTERNET TFR / ONLINE PAYMENT [client] | Self-employed income | Revenue if from a business client |
| STRIPE PAYOUT / STRIPE PAYMENTS | Self-employed income, gross up | Gross up to pre-fee from the processor statement; fee deductible |
| PAYPAL TRANSFER / PAYPAL NZ | Self-employed income, gross up | As above |
| WINDCAVE SETTLEMENT / EFTPOS NZ SETTLEMENT | Self-employed income, gross up | As above |
| SQUARESPACE PAYMENTS / SQUARE NZ | Self-employed income, gross up | As above |
| SCHEDULAR PAYMENT (line annotation) | Question 12 | Gross up only from a verified rate or the Summary of Income |
| SALARY CREDIT [employer] | Question 11 | Not self-employed income. Take figures from the Summary of Income |
| INTEREST PAID / BANK INTEREST | Question 13 | Usually subject to RWT |
| DIVIDEND [company] | Question 14 | Include gross plus credits, from the dividend statement |
| IRD REFUND / INLAND REVENUE REFUND | Exclude | Tax refund |
| GST REFUND IRD | Exclude | GST refund, separate tax |
| RENTAL INCOME [property] | Question 22 | Not self-employed income |

**Debits**

| Pattern | Category | Treatment |
| --- | --- | --- |
| RENT [office/workspace] / COMMERCIAL RENT | Office rent | Deductible for business premises; home office under Expenses above |
| GENESIS ENERGY / MERIDIAN ENERGY / CONTACT ENERGY / MERCURY | Utilities | Business share |
| SPARK NZ / ONE NZ / 2DEGREES | Phone and internet | Business share, documented |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE / XERO / MYOB | Software subscriptions | Deductible if used in the business |
| CHARTERED ACCOUNTANTS / ACCOUNTANT / TAX AGENT | Accounting and tax fees | Deductible (ITA s DB 3), business fees through section DA 1 |
| INTERISLANDER / BLUEBRIDGE / AIR NZ / JETSTAR | Travel | Business purpose note required; personal is nil |
| HILTON / IBIS / NOVOTEL / AIRBNB | Accommodation | Business purpose required; personal is nil |
| Z ENERGY / BP NZ / MOBIL NZ / GULL | Fuel | Business share under Motor vehicles |
| AA NZ / VEHICLE REGISTRATION / NZTA | Vehicle costs | Business share under Motor vehicles |
| ACC LEVY / ACC INVOICE | ACC levies | Split by invoice. Work levy deductible; earners' levy held; not in RIT |
| INLAND REVENUE PROV TAX / IRD PROVISIONAL TAX | Exclude | Prepayment of income tax |
| GST PAYMENT IRD | Exclude | Separate tax |
| PROFESSIONAL INDEMNITY INS / PUBLIC LIABILITY INS | Business insurance | Deductible for business policies |
| LINKEDIN PREMIUM / SEEK ADVERTISE / TRADEME JOBS | Business platforms | Deductible if business use |
| COURIER POST / NZ POST / DHL NZ | Postage and courier | Business deliveries |
| BANK FEE / ACCOUNT FEE / ANZ MONTHLY FEE | Bank charges | Business account fees |
| XERO SUBSCRIPTION / MYOB SUBSCRIPTION | Accounting software | Deductible |
| TRAINING / COURSE / CONFERENCE | Professional development | Reviewer. The prior 'existing skills; new career not deductible' rule was not read in a primary source |
| SUBCONTRACTOR PAYMENT / CONTRACTOR INVOICE | Subcontract costs | Deductible; a schedular withholding obligation may apply |
| STRIPE FEES / PAYPAL FEES / SQUARE FEES | Processing fees | Deduct the gross-up difference |
| ENTERTAINMENT / MEALS CLIENT | Entertainment | 50% if within section DD 1; otherwise under Expenses above |

### Bank formats and amounts

| Bank | Format | Key fields |
| --- | --- | --- |
| ANZ NZ | CSV | Date,Description,Debit,Credit,Balance |
| BNZ (Bank of New Zealand) | CSV | Date,Tran Type,Particulars,Code,Reference,Amount,Balance |
| ASB Bank | CSV | Date,Unique Id,Tran Type,Cheque Number,Payee,Memo,Amount |
| Westpac NZ | CSV | Date,Narrative,Debit Amount,Credit Amount,Balance |
| Kiwibank | CSV | Date,Description,Debit,Credit,Balance |

| Narration | Meaning | Hint |
| --- | --- | --- |
| PAYMENT FROM [name] / TFR FROM [name] | Bank transfer in | Potential business income |
| INTERNET TFR | Online transfer | Income or expense |
| D/C (Direct Credit) | Direct credit | Potential income |
| D/D (Direct Debit) | Direct debit | Recurring expense |
| ATM WITHDRAWAL | Cash withdrawal | Personal, investigate |
| IRD PROV TAX / INLAND REVENUE | Tax payment | Prepayment, exclude |
| GST PAYMENT | GST remittance | Separate tax, exclude |
| INTEREST | Bank interest | Other income |
| ACC LEVY | ACC payment | Split by invoice; not in RIT |

New Zealand bank-to-bank transfers carry 3 fields the sender fills in: Particulars (usually the payer's name or invoice reference), Code (account code or project reference) and Reference (invoice number, date or other identifier). Combine all 3 to identify the source.

**Currency and rounding.** Compute in NZD and keep cents. The rules read fix 3 rounding points: IETC abatement counts complete dollars, a standard method amount truncates to whole dollars (ITA s RC 5(4B)) and a provisional tax instalment truncates to whole dollars (ITA s RC 9(13)). No general rounding rule for the return was read.

Dates are DD/MM/YYYY. Amounts have no thousands separator and a period decimal, for example 11500.00. ANZ and Westpac use separate Debit and Credit columns; BNZ and ASB use a single Amount column, positive for a credit and negative for a debit.

### Excel working paper

```text
NEW ZEALAND INCOME TAX WORKING PAPER (IR3, SELF-EMPLOYED)
estimated, not reviewed
Taxpayer: _______________  IRD Number: _______________
Tax year: 1 April ____ to 31 March ____     Income year label: ____

SECTION A, INCOME (GST-exclusive if registered)
                                        NZD
Gross self-employed receipts           ___________
Less: GST verified at 15%              (___________)
Self-employed income                   ___________
Schedular income, gross (Box 12B)      ___________
Other business income                  ___________
Other income (Questions 11 to 22)      ___________
TOTAL INCOME                           ___________

SECTION B, DEDUCTIBLE EXPENSES
Rent / workspace (business share)      ___________
Utilities (business share)             ___________
Phone / internet (business share)      ___________
Software subscriptions                 ___________
Accounting / tax agent fees            ___________
Legal fees                             ___________
Travel (business trips)                ___________
Accommodation (business travel)        ___________
Meals and entertainment (rule applied) ___________
Business insurance                     ___________
Bank charges (business account)        ___________
Motor vehicle (method: ______)         ___________
ACC work levy                          ___________
ACC earners' levy (held, reviewer)     ___________
Depreciation                           ___________
Subcontractor costs                    ___________
Payment processor fees                 ___________
Other business expenses                ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION C, NET AND TAXABLE INCOME
Total income less total expenses       ___________
Less: tax loss used (Box 31B)          (___________)
TAXABLE INCOME                         ___________

SECTION D, INCOME TAX
Tax at the rates for the year          ___________
Less: IETC (not below nil)             (___________)
Less: overseas tax (not below nil)     (___________)
Less: imputation (not below nil)       (___________)
Less: Box 21A credits, Box 35C PIE     (___________)
RIT (nil if credits are larger)        ___________
Excess credits (refundable only)       (___________)

SECTION E, ACC (ACC invoice; not part of RIT)
Earners' levy on liable earnings       ___________

SECTION F, PROVISIONAL TAX
Less: provisional tax paid             (___________)
BALANCE DUE / (REFUND)                 ___________
Next year standard, 105% or 110%       ___________

SECTION G, REVIEWER FLAGS
[ ] GST stripped only where verified at 15%?
[ ] Schedular payments grossed up from a verified rate?
[ ] Vehicle evidence reviewed and method recorded?
[ ] Entertainment rule applied line by line?
[ ] Home office method and area documented?
[ ] ACC invoice split by levy?
[ ] Provisional tax reconciled to the Inland Revenue account?
[ ] Foreign income converted at a recorded rate and source?
[ ] Tax year label checked against the rate table used?
```

## Deadlines and filing

Dates are for a 31 March balance date. Inland Revenue's practice is that an instalment date on a weekend or public holiday is met by the next working day (IR3G 2026, IR289).

| Item | Date | Tax year | Official source |
| --- | --- | --- | --- |
| Return due, no tax agent extension | 7 July after year end: 7 July 2025 | 2024-25 | [TAA s 37(1)(c)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Return due, no tax agent extension | 7 July 2026 | 2025-26 | [TAA s 37(1)(c)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Return due, no tax agent extension | 7 July 2027 | 2026-27 | [TAA s 37(1)(c)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Return due, tax agent extension | Date allowed, no later than the 31 March after year end: 31 March 2026 | 2024-25 | [TAA s 37(4), (5)(a)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Return due, tax agent extension | No later than 31 March 2027 | 2025-26 | [TAA s 37(4), (5)(a)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Return due, tax agent extension | No later than 31 March 2028 | 2026-27 | [TAA s 37(4), (5)(a)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Terminal tax | 7 February after year end: 7 February 2027 | 2025-26 | [ITA s RA 13(1), (2)(b), (3)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A column G](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Terminal tax, return linked to a tax agent with an extension | 7 April after that: 7 April 2027 | 2025-26 | [ITA s RA 13(2)(a), (3), (4)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A column H](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Terminal tax, other years | 7 February 2026, or 7 April 2026 if linked | 2024-25 | [ITA s RA 13](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Terminal tax, other years | 7 February 2028, or 7 April 2028 if linked | 2026-27 | [ITA s RA 13](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Provisional tax, 3 instalments | 28 August 2026, 15 January 2027 and 7 May 2027 | 2026-27 | [ITA s RC 9(3)](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A columns B, D, F](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Provisional tax, 6-monthly GST | 28 October 2026 and 7 May 2027 | 2026-27 | [ITA s RC 9](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A columns C, F](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |
| Provisional tax, GST ratio method | 6 dates: 28 June, 28 August, 28 October, 15 January, 28 February, 7 May | 2026-27 | [ITA s RC 9](https://www.legislation.govt.nz/act/public/2007/97/en/latest/); [Schedule 3 Part A columns A to F](https://www.legislation.govt.nz/act/public/2007/97/en/latest/) |

The agent date is an extension under section 37(4), not an automatic date. A 31 March year is measured from its own end: the prior version's '31 March of second following year' fits only if counted from the start of the year. Section 37(3) and (3B) allow other extensions.

**Filing.** File in myIR ('Returns and transactions', then 'File now' on the Returns tab), or through a tax agent. An individual who is not otherwise required to file must file if they have more than NZD 200 of income that has not been reported to Inland Revenue, and anyone self-employed files; check Inland Revenue's IR3 page for the full list. Inland Revenue says to wait until June to file where a payer has to send it information about payments. Attachments and supports are the IR10 (financial statement summary), IR3B, IR3F, IR3R, IR833 and IR1261 where the return guide calls for them. Inland Revenue issues a notice of assessment. Keep records under TAA s 22.

## Penalties and interest

Penalties are in Part 9 of the TAA.

| Penalty | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Late filing, net income below NZD 100,000 | NZD 50 | All covered years | [TAA s 139A(3)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Late filing, net income NZD 100,000 to NZD 1,000,000, both inclusive | NZD 250 | All covered years | [TAA s 139A(3)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Late filing, net income above NZD 1,000,000 | NZD 500 | All covered years | [TAA s 139A(3)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Late payment, on the day after the default date | 1% of the unpaid tax | All covered years | [TAA s 139B(2)(a)(i), (3)(a)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Late payment, at the end of the sixth day after the 1% is imposed | 4% of the tax then still to pay | All covered years | [TAA s 139B(2)(a)(ii)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Monthly incremental penalty | None for income tax or provisional tax for 2017-18 and later | All covered years | [TAA s 139B(2B)(c)](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Shortfall, not taking reasonable care | 20% | All covered years | [TAA s 141A](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Shortfall, unacceptable tax position | 20%, only if the income tax shortfall is more than both NZD 50,000 and 1% of the total tax figure | All covered years | [TAA s 141B](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Shortfall, gross carelessness | 40% | All covered years | [TAA s 141C](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Shortfall, abusive tax position | 100%, or 20% in the case in section 141D(3B) | All covered years | [TAA s 141D](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |
| Shortfall, evasion or similar | 150% | All covered years | [TAA s 141E](https://www.legislation.govt.nz/act/public/1994/166/en/latest/) |

The prior version's 'NZD 50/month up to NZD 300' and '1.5%/month ongoing' are not the law. A late filing penalty is a single amount and needs the notice steps in section 139A(2)(b) and (5). Inland Revenue says it charges NZD 50 first and adjusts once net income is known. Section 139B(1) applies to provisional tax without more; for other tax it needs either an earlier failure to pay on time in the prior 2 years or a notice setting a further date that is missed. No late payment penalty or interest arises if the amount outstanding after the due date is NZD 100 or less, and no interest is paid on overpaid tax of NZD 100 or less (section 183F(1)).

Section 183A lets the Commissioner remit a late filing or late payment penalty, and a shortfall penalty only under section 141AA, if an event or circumstance beyond the taxpayer's control caused the failure, it gives a reasonable justification or excuse, and the failure was corrected as soon as practicable (section 183A(1A)). An agent's act or omission, with a narrow exception, and the taxpayer's financial position do not count (section 183A(3)).

Reductions: section 141FB, to 50% if no disqualifying offence or penalty applies. For sections 141A to 141D the disqualifying penalty look-back is 4 years, or 2 years for PAYE, FBT, GST and RWT. For section 141E it runs back to 26 March 2003. Section 141G voluntary disclosure, pre-notification 100% for lack of reasonable care, unacceptable tax position or unacceptable interpretation and 75% otherwise, post-notification 40%; section 141H, 75% for adequate disclosure of a section 141B or 141D position; section 141I, 75% for a temporary shortfall. Section 141J limits the reduction where a voluntary disclosure is made for a temporary shortfall. Section 141JAA caps a reasonable care or unacceptable tax position penalty at NZD 50,000 when disclosed or determined in time, unless section 141K applies.

**Use of money interest.** Enacted in TAA Part 7 (sections 120A to 120L). Interest accrues daily at t × r ÷ 365 under section 120E, and Inland Revenue says it does not compound. Rates are set by the Commissioner under section 120H; no instrument was on legislation.govt.nz, so the rates below are Inland Revenue's published figures.

| From | Charged on underpayments | Paid on overpayments | Official source |
| --- | --- | --- | --- |
| 16 January 2026 | 8.97% | 2.25% | [Inland Revenue, Interest on overpayments and underpayments](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |
| 8 May 2025 | 9.89% | 3.27% | [Inland Revenue, Interest on overpayments and underpayments](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |
| 16 January 2025 | 10.88% | 4.30% | [Inland Revenue, Interest on overpayments and underpayments](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |
| 29 August 2023 | 10.91% | 4.67% | [Inland Revenue, Interest on overpayments and underpayments](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments) |

Interest payable is deductible under ITA s DB 3B in the year paid (section EF 5), and Inland Revenue describes it as deductible for business purposes. Interest paid to the taxpayer is income (section EF 4 allocates it). Exposure by method: sections 120KB to 120KE and `nz-provisional-tax`. Under TAA s 120KE(1) and (2), a person on the standard method, or with no obligation under section RC 3(3), whose RIT is under NZD 60,000 has no interest either way until terminal tax date, unless they estimated, used AIM or a GST ratio in the year or a provisional tax interest avoidance arrangement exists. Under section 120KE(3) and (4), a person who uses the GST ratio for the whole corresponding income year has no interest either way until terminal tax date on provisional tax for the period the ratio is used. Neither subsection turns on payment. Practice: Inland Revenue's ratio page speaks of a person who applies the option correctly and pays the provisional tax calculated, and IR289 says late payment penalties still apply.

## Cross-border points

**Residence.** Enacted in ITA s YD 1. A person is resident if they have a permanent place of abode in New Zealand (subsection (2)) or are personally present for more than 183 days in a 12-month period, from the first of those days (subsections (3) and (4)). Residence gained only under the day test stops after absence of more than 325 days in a 12-month period (subsection (5)). Part days count as present (subsection (8)). Section YD 1B on non-resident visitors was inserted from 1 April 2026; check it for 2026-27. Detail is in `nz-tax-residency`. A non-resident stops at R-NZ-3.

**Foreign income.** A resident is taxed on worldwide income (Inland Revenue, overseas income page). Report at Question 17 (Boxes 17A and 17B) with the Overseas income summary IR1261 where the return guide calls for it. A foreign tax credit is limited to New Zealand tax on that income segment (ITA s LJ 2), and a double tax agreement may change the result; check before claiming. Foreign investment funds and controlled foreign companies are out of this file.

**Foreign currency.** Enacted in ITA s YF 1. An amount converts at the close of trading spot rate on the date it must be measured (subsection (2)), or by a method the Commissioner allows (subsections (3), (5) and (6)). Approval FX 21/01, given under section YF 1(5), and Inland Revenue's currency page accept rates from the Commissioner, the Reserve Bank, another central bank or another appropriate source, a mid-month rate, and a rolling 12-month average for repeated transactions, not significant one-offs, which convert at a daily rate. Use a consistent source and keep the record. Do not use cash or foreign cheque rates. Financial arrangements, FIFs and CFCs have other rules. The prior version's 'Reserve Bank mid-rate on the date of receipt' and 'never year-end rate' are narrower than these rules: a measurement date is not always the receipt date, and Inland Revenue offers the end-of-month rate for a market value or balance at the start or end of the tax year. A foreign amount already paid out in NZD by the platform is not itself proof of the required rate.

## Two worked examples that recompute

These are invented fixtures. Every result needs the inputs confirmed first. Rates come from the tables above.

### Example 1: self-employed consultant, 2025-26

A sole trader, GST-registered for the whole year, confirms net income of NZD 68,000 at Box 30 on GST-exclusive figures. That includes NZD 5,000 gross schedular income, with NZD 1,000 tax deducted shown on the Summary of Income. There are no losses, no imputation credits and no overseas tax. They met every section LC 13 condition for all 12 months, and paid NZD 4,800 provisional tax. The 2025-26 return is filed by 28 August 2026.

```oa-check
name: NZ 2025-26 self-employed RIT, balance and next-year standard method
inputs:
  net_income: 68000
  schedular_tax: 1000
  provisional_paid: 4800
  months: 12
steps:
  - taxable_income: max(net_income, 0)
  - tax: 8270.50 + (taxable_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - after_ietc: max(tax - ietc, 0)
  - rit: after_ietc - schedular_tax
  - balance: rit - provisional_paid
  - standard_2026_27: floor(rit * 1.05)
  - instalment: standard_2026_27 / 3
expected:
  tax: 12620.50
  ietc: 260
  rit: 11360.50
  balance: 6560.50
  standard_2026_27: 11928
  instalment: 3976
```

Decision: 2025-26 RIT is more than NZD 5,000, so section RC 3(3) does not remove a 2026-27 obligation and that RIT sets the standard amount. Whether provisional tax is payable for 2026-27 still turns on that year's RIT (section RC 3(1)(a)). The 105% limb applies because the return was not outstanding under an extension at the instalment date. Had the return still been outstanding at 28 August 2026 under an agent extension, the first instalment would use 110% of 2024-25 RIT, which is a Needs Input.

Same client, but entitled to and receiving WFF for 3 months. The condition fails for those months, so the credit falls to 9 months.

```oa-check
name: NZ 2025-26 IETC with 9 eligible months
inputs:
  net_income: 68000
  schedular_tax: 1000
  months: 9
steps:
  - tax: 8270.50 + (net_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - rit: max(tax - ietc, 0) - schedular_tax
expected:
  ietc: 195
  rit: 11425.50
```

Same client, entitled to WFF for those 3 months but not receiving it. From 30 March 2025 section LC 13(1)(d) fails only on entitlement and receipt together, so all 12 months count.

```oa-check
name: NZ 2025-26 IETC with WFF entitlement but no receipt
inputs:
  net_income: 68000
  schedular_tax: 1000
  months_entitled_and_receiving: 0
steps:
  - months: 12 - months_entitled_and_receiving
  - tax: 8270.50 + (net_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - rit: max(tax - ietc, 0) - schedular_tax
expected:
  months: 12
  ietc: 260
  rit: 11360.50
```

A separate refund case. Tax after the worksheet floors is NZD 1,000, refundable withholding at Box 21A is NZD 1,500 and provisional tax paid is NZD 200.

```oa-check
name: NZ RIT nil with excess credits kept for settlement
inputs:
  after_imputation: 1000
  credits: 1500
  provisional_paid: 200
steps:
  - rit: max(after_imputation - credits, 0)
  - excess_credits: max(credits - after_imputation, 0)
  - to_pay_or_refund: rit - excess_credits - provisional_paid
expected:
  rit: 0
  excess_credits: 500
  to_pay_or_refund: -700
```

Decision: RIT is nil, not NZD (500), so it adds nothing to the NZD 5,000 test or the standard amount. The refund is NZD 700, on the assumption that the NZD 1,500 is a credit within section LA 6(1).

A separate levy case, outside RIT. A self-employed person worked more than 30 hours a week in 2025-26 and earned NZD 35,000 in all, NZD 5,000 of it as an employee.

```oa-check
name: NZ 2025-26 earners' levy with and without purchased weekly compensation
inputs:
  employee_earnings: 5000
  agreed_annual_higher: 40000
  agreed_annual_lower: 20000
steps:
  - no_agreement: round(1.45 * (49365 - employee_earnings) / 100, 2)
  - agreement_higher: round(1.45 * (1.25 * agreed_annual_higher) / 100, 2)
  - agreement_lower: round(1.45 * (1.25 * agreed_annual_lower) / 100, 2)
expected:
  no_agreement: 643.29
  agreement_higher: 725.00
  agreement_lower: 362.50
```

Decision: with no agreement, regulation 6 gives NZD 643.29. With an agreement, regulation 7 replaces it, even where the result is lower, as at NZD 20,000 agreed.

A vehicle line and a receipt line from the same client. The vehicle is a petrol car doing 18,000 km with 60% business use from a logbook term, and actual vehicle costs are NZD 14,000. A bank credit of NZD 11,500 is tested in both GST cases.

```oa-check
name: NZ 2025-26 vehicle method comparison and GST both cases
inputs:
  total_km: 18000
  business_share: 0.6
  actual_costs: 14000
  receipt: 11500
steps:
  - tier_1_km: min(total_km, 14000)
  - tier_2_km: max(total_km - 14000, 0)
  - kilometre_method: tier_1_km * business_share * 1.20 + tier_2_km * business_share * 0.37
  - logbook_method: actual_costs * business_share
  - no_evidence_cap: actual_costs * min(business_share, 0.25)
  - receipt_gst_verified: receipt - receipt * 3 / 23
  - receipt_zero_rated: receipt
expected:
  kilometre_method: 10968
  logbook_method: 8400
  no_evidence_cap: 3500
  receipt_gst_verified: 10000
  receipt_zero_rated: 11500
```

Decision: the kilometre method gives the larger deduction here, but only if this is the election year for the vehicle under section DE 2B. Otherwise the person is on the costs method. Either election cannot be revoked and holds until the end of the income year of disposal. Under both methods the 60% comes from the logbook term. With no records, no logbook term and no kilometre election, the deduction is the lesser of actual use and 25%, so NZD 3,500 at most. With a kilometre election and no records or logbook term, the share is Needs Input. The receipt is NZD 10,000 only if GST at 15% is verified.

### Example 2: mixed salary and self-employed, 2024-25

An employee earned NZD 19,000 salary and NZD 31,000 net self-employed income, so net income is NZD 50,000 at Box 31 of the 2025 return. Total PAYE on payslips was NZD 2,574.12. Earners' levy at the 2024-25 rate is NZD 304.00. They met every LC 13 condition all year. No other credits apply.

```oa-check
name: NZ 2024-25 mixed income RIT with composite rates and IETC
inputs:
  salary: 19000
  self_employed: 31000
  total_paye: 2574.12
steps:
  - net_income: salary + self_employed
  - tax: 7345.12 + (net_income - 48000) * 0.2164
  - a_floored: max(520 - 0.13 * max(floor(net_income) - 44000, 0), 0)
  - a_printed: 520 - 0.13 * max(floor(net_income) - 44000, 0)
  - b: max(520 - 0.13 * max(floor(net_income) - 66000, 0), 0)
  - ietc_floored: round((a_floored * 121 + b * 244) / 365, 2)
  - ietc_printed: round((a_printed * 121 + b * 244) / 365, 2)
  - earners_levy: min(salary, 142283) * 0.016
  - tax_deducted: total_paye - earners_levy
  - rit_floored: tax - ietc_floored - tax_deducted
  - rit_printed: tax - ietc_printed - tax_deducted
  - levy_left_in_floored: tax - ietc_floored - total_paye
  - levy_left_in_printed: tax - ietc_printed - total_paye
  - standard_floored: floor(rit_floored * 1.05)
  - standard_printed: floor(rit_printed * 1.05)
expected:
  tax: 7777.92
  a_floored: 0
  a_printed: -260
  b: 520
  ietc_floored: 347.62
  ietc_printed: 261.42
  earners_levy: 304
  tax_deducted: 2270.12
  rit_floored: 5160.18
  rit_printed: 5246.38
  levy_left_in_floored: 4856.18
  levy_left_in_printed: 4942.38
  standard_floored: 5418
  standard_printed: 5508
```

Decision: show both figures, because the floor is held. RIT is NZD 5,160.18 floored and NZD 5,246.38 on the printed boxes, and both are more than NZD 5,000. Crediting total PAYE instead of tax deducted gives NZD 4,856.18 or NZD 4,942.38, the wrong answer on the threshold either way. The standard amount is NZD 5,418 or NZD 5,508. Whether provisional tax was payable for 2024-25 still turns on 2023-24 RIT (section RC 3(3)), which the file does not show.

Same client, but a WFF entitlement ended on 30 September 2024, so they are eligible from 1 October 2024: 6 whole months, or 182 days, all in the second period. WFF entitlement excluded April to September 2024 under the rule in force before 30 March 2025, whether received or not. October 2024 to March 2025 remains eligible.

```oa-check
name: NZ 2024-25 part-year IETC by statute and by worksheet
inputs:
  net_income: 50000
  days_second_period: 182
  eligible_months: 6
steps:
  - a_floored: max(520 - 0.13 * max(floor(net_income) - 44000, 0), 0)
  - a_printed: 520 - 0.13 * max(floor(net_income) - 44000, 0)
  - b: max(520 - 0.13 * max(floor(net_income) - 66000, 0), 0)
  - by_statute: round(b * days_second_period / 365, 2)
  - by_worksheet_floored: round((a_floored * 121 + b * 244) / 365 * eligible_months / 12, 2)
  - by_worksheet_printed: round((a_printed * 121 + b * 244) / 365 * eligible_months / 12, 2)
  - difference_floored: by_statute - by_worksheet_floored
  - difference_printed: by_statute - by_worksheet_printed
expected:
  by_statute: 259.29
  by_worksheet_floored: 173.81
  by_worksheet_printed: 130.71
  difference_floored: 85.48
  difference_printed: 128.58
```

Decision: show all 3 figures. Sections LC 14 and LC 15 use days, and that figure does not depend on the floor because a has no days here. The IR3G 2025 worksheet uses months, and its figure depends on the floor. Do not choose by default.

### Bank line fixtures

Layouts are carried from the prior version and untested. Each treatment assumes the conditions stated.

| Line | Case | Treatment |
| --- | --- | --- |
| `03/01/2025,,PAYMENT FROM ACME LTD,,11500.00,` (ANZ) | IT consultant | NZD 10,000 if registered and GST at 15% is verified; NZD 11,500 if not registered or the supply carried no GST |
| `10/08/2025,SHELL SELECT QUEENSTOWN,120.00,,` (Westpac) | Photographer, 8,400 of 14,000 km business, logbook term | NZD 72. With no records, no logbook term and no kilometre election: lesser of actual use and 25%, so NZD 30 at most, on a GST-exclusive basis if registered. With a kilometre election and no records or logbook term: Needs Input |
| `15/03/2025,SCHEDULAR PAYMENT BUILDCO LTD,-,4000.00,` (ASB) | Plumber | At a verified 20%: gross NZD 5,000, credit NZD 1,000. At a verified 15%: gross NZD 4,705.88, credit NZD 705.88. Rate unknown: Needs Input |
| `28/02/2025,TT,STRIPE PAYOUT,CODE,REF,2185.00,` (BNZ) | Marketing consultant | Gross up from the Stripe statement: the prior example's NZD 2,254 and NZD 69 are illustrative, GST-exclusive if registered |
| `20/05/2025,PAYPAL TRANSFER USD,,,1850.00,` (Kiwibank) | Freelance writer | Income is the NZD amount at the rate rule under Foreign currency, not the bank credit by default |
| `01/09/2025,,WINDCAVE SETTLEMENT,,8500.00,` (ANZ) | E-commerce seller, NZD 95,000 of annual supplies | NZD 7,391.30 if GST at 15% is verified. Red flag: verify registration under GST Act s 51 |

## Ask the client first

1. **Year and residence.** Which tax year is this, were you New Zealand tax resident all year, and what is your balance date?
2. **GST.** Were you GST-registered all year, with which taxable period, and do the bank amounts include GST?
3. **Income sources.** Did you have salary, schedular payments (at what rate), rent (on the portfolio or property basis), dividends, interest or foreign income, and from which countries? Please send the Summary of Income and any dividend statements.
4. **Business use.** Do you use a vehicle or a home office for work, what actual records or logbook term do you have, in which year did the vehicle first go into business use, did you elect the kilometre rate in that year's return, and what area of the home is used?
5. **Credits and IETC.** For each month, were you or a partner entitled to Working for Families, and was it received? Did you or a partner have a main benefit, NZ Super, a veteran's pension or an overseas equivalent?
6. **Prior year and prepayments.** What was last year's RIT and return date, did you use a tax agent, and how much provisional tax have you paid this year, under which method?

### Completion checks

- [ ] Rate table matches the tax year, and 2024-25 composite rates are used for 2024-25 only?
- [ ] GST stripped only where verified, for a registered person?
- [ ] Schedular payments grossed up from a verified rate?
- [ ] Vehicle claim above 25% backed by actual records or a logbook term, the election checked against section DE 2B, and any other claim within section DE 4 or marked Needs Input?
- [ ] Entertainment rule applied by line?
- [ ] ACC earners' levy kept out of RIT, and removed from PAYE at Box 11E?
- [ ] ACC work levy included as a deductible expense?
- [ ] Provisional tax excluded from expenses?
- [ ] Foreign currency converted under section YF 1 with the source recorded?
- [ ] RIT recomputed with each floor shown?

## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Income Tax Act 2007 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/ | 2026-11-05 | Version as at 4 September 2026, read in part: sections and Schedules 1, 3 and 4 as cited, including sections DB 18AA, DE 2B to DE 12, EL 1 to EL 13 and RC 37 to RC 40 |
| Income Tax Act 2007, version as at 30 March 2025 | https://www.legislation.govt.nz/act/public/2007/97/en/2025-03-30/ | 2026-11-05 | Read in part: sections DH 1 to DH 8 and DH 10; section LC 13(1) |
| Income Tax Act 2007, version as at 30 June 2024 | https://www.legislation.govt.nz/act/public/2007/97/en/2024-06-30/ | 2026-11-05 | Read in part: section CB 6A; section LC 13(1) |
| Tax Administration Act 1994 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/ | 2026-11-05 | Version as at 1 October 2026, read in part: sections 22, 24F to 24H, 33, 37, 92A, 120A to 120L, 139A to 141K, 183A and 183F |
| Goods and Services Tax Act 1985 | https://www.legislation.govt.nz/act/public/1985/141/en/latest/ | 2026-11-05 | Read in part: sections 8, 19N, 20 and 51; section 19F not read |
| Accident Compensation Act 2001 | https://www.legislation.govt.nz/act/public/2001/49/en/latest/ | 2026-11-05 | Read in part: sections 168B, 208, 209, 211, 219, 220 and 222 |
| Taxation (Budget Measures) Act 2024 | https://www.legislation.govt.nz/act/public/2024/19/en/latest/ | 2026-11-05 | Read in part: sections 7 and 37 |
| Taxation (Annual Rates for 2023-24, Multinational Tax, and Remedial Matters) Act 2024 | https://www.legislation.govt.nz/act/public/2024/11/en/latest/ | 2026-11-05 | Read in part: sections 8, 47 and 48 |
| Taxation (Annual Rates for 2024-25, Emergency Response, and Remedial Measures) Act 2025 | https://www.legislation.govt.nz/act/public/2025/9/en/latest/ | 2026-11-05 | Read in part: sections 2(1), 3 and 105; section 5 through the ITA amendment note |
| Taxation (Annual Rates for 2025-26, Compliance Simplification, and Remedial Measures) Act 2026 | https://www.legislation.govt.nz/act/public/2026/8/en/latest/ | 2026-11-05 | Read in part: section 3; section 137 through the ITA amendment note |
| Taxation (Budget Measures) Act 2025 | https://www.legislation.govt.nz/act/public/2025/26/en/latest/ | 2026-11-05 | Subpart DI insertion, in part |
| Taxation (Budget Measures) Act 2026 | https://www.legislation.govt.nz/act/public/2026/25/en/latest/ | 2026-11-05 | Contents only, read for scope; no finding here rests on it |
| Accident Compensation (Earners' Levy) Regulations 2025 (SL 2025/18) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/ | 2026-11-05 | Read in full for regulations 4 to 9 |
| Accident Compensation (Work Account Levies) Regulations 2025 (SL 2025/17) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/ | 2026-11-05 | Read in part: regulations 6, 7, 9 and 11 to 15 and the Schedules' layout |
| Accident Compensation (Work Account Levies) Amendment Regulations 2026 (SL 2026/30) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/30/en/latest/ | 2026-11-05 | Read in part for the rate schedules |
| Government Bill 344-1 | https://www.legislation.govt.nz/bill/government/2026/344/en/latest/ | 2026-11-05 | Read in part: clause 3, clauses 116 and 131 and the explanatory note |
| Parliament, bill page | https://www3.parliament.nz/en/pb/sc/committees-press-releases/taxation-annual-rates-for-2026-27-fbt-simplification-foreign-investment-funds-and-remedial-measures-bill/ | 2026-11-05 | Read for committee stage, the dissolution note and submissions |
| Inland Revenue, Tax rates for individuals | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | 2026-11-05 | Read in full for both rate tables |
| Inland Revenue, IR3G 2026 and IR3G 2025 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf | 2026-11-05 | Read in part: questions cited, including Question 22 of the 2026 guide and Question 23 of the 2025 guide, by local extraction |
| Inland Revenue, IR3 2026 and 2025, IR3B, IR3R | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3/ir3-2026.pdf | 2026-11-05 | Read in part: box layout and the IR3B expense notes including Box 9, by local extraction |
| Inland Revenue, ACC earners' levy rates | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates | 2026-11-05 | Read in full for rates and maxima by year |
| Inland Revenue, Interest on overpayments and underpayments | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments | 2026-11-05 | Read in full for the rate table, the NZD 100 wording and deductibility |
| Inland Revenue, Kilometre rates 2025-2026 | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026 | 2026-11-05 | Read in full for rates; the 2024-2025 page likewise |
| Inland Revenue, schedular rate page | https://www.ird.govt.nz/income-tax/withholding-taxes/schedular-payments/getting-schedular-payments/work-out-and-declare-my-tax-rate-for-schedular-payments | 2026-11-05 | Read in full for chosen-rate limits |
| Inland Revenue, IETC page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc | 2026-11-05 | Read in part for income limits and the month rule |
| Inland Revenue, IR3 page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3 | 2026-11-05 | Read in part for who files and the June note |
| Inland Revenue, IR3 in myIR | https://www.ird.govt.nz/myir-help/what-you-can-do/how-to-file-an-ir3-individual-income-tax-return-in-myir | 2026-11-05 | Read in part for the filing steps |
| Inland Revenue, provisional tax | https://www.ird.govt.nz/income-tax/provisional-tax | 2026-11-05 | Read in part for who pays |
| Inland Revenue, standard option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option | 2026-11-05 | Read in part for the default and the 105% wording |
| Inland Revenue, ratio option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option | 2026-11-05 | Read in part for the interest statement |
| Inland Revenue, interest on provisional tax | https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax | 2026-11-05 | Read in part for the NZD 100 wording |
| Inland Revenue, first year in business | https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business | 2026-11-05 | Read in part for the early payment discount and rates |
| Inland Revenue, home business page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business | 2026-11-05 | Read in part for the formula and apportionment |
| Inland Revenue, vehicle page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses | 2026-11-05 | Read in part for methods and records |
| Inland Revenue, entertainment page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/entertainment-expenses | 2026-11-05 | Read in part for the 50% examples |
| Inland Revenue, meal page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/meal-expenses | 2026-11-05 | Read in part for meal rules |
| Inland Revenue, late filing penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties | 2026-11-05 | Read in part for the first charge |
| Inland Revenue, late payment penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties | 2026-11-05 | Read in part for the penalty steps |
| Inland Revenue, shortfall penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties | 2026-11-05 | Read in part for section 141K as stated |
| Inland Revenue, currency conversion | https://www.ird.govt.nz/managing-my-tax/overseas-currency-conversion-to-nz-dollars | 2026-11-05 | Read in part for accepted rates |
| Inland Revenue, residency page | https://www.ird.govt.nz/international-tax/individuals/tax-residency-status-for-individuals | 2026-11-05 | Read in part for the day tests |
| Inland Revenue, overseas income page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/types-of-individual-income/overseas-income | 2026-11-05 | Read in part for worldwide income |
| Inland Revenue, rental income page | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it | 2026-11-05 | Read in part for reporting |
| Inland Revenue, rental deductions page | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions | 2026-11-05 | Read in part for the basis and the exclusions |
| Inland Revenue, property interest rules | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions/property-interest-rules | 2026-11-05 | Read in part for the 2024-25 limit |
| Inland Revenue, how interest deductions are affected | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions/property-interest-rules/how-interest-deductions-are-affected | 2026-11-05 | Read in part for the 80% wording |
| Inland Revenue, bright-line test | https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test | 2026-11-05 | Read in part for the 2-year test |
| Inland Revenue, property sold before 1 July 2024 | https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/property-sold-before-1-july-2024 | 2026-11-05 | Read in part for the earlier periods |
| Inland Revenue, hobby page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/types-of-individual-income/hobbies-and-businesses/is-your-hobby-a-business | 2026-11-05 | Read in part for the hobby tests |
| Inland Revenue, self-employed or employee | https://www.ird.govt.nz/roles/employees/self-employed-or-employee | 2026-11-05 | Read in part for the employment tests |
| Inland Revenue, attribution page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/how-income-is-taxed/attribution-rule-for-income-from-personal-services | 2026-11-05 | Read in part for the threshold |
| Inland Revenue, registering for GST | https://www.ird.govt.nz/gst/registering-for-gst | 2026-11-05 | Read in part for the threshold wording |
| Inland Revenue, square metre rate 2026 | https://www.ird.govt.nz/updates/news-folder/2026/square-metre-rate-for-home-office-calculations-2026 | 2026-11-05 | Read in full for the published rates |
| Inland Revenue, Provisional tax guide IR289 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf | 2026-11-05 | Read in part for methods, interest and the early payment discount, by local extraction |
| Inland Revenue, Entertainment expenses guide IR268 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir268/ir268-2024.pdf | 2026-11-05 | Read in part for the 50% examples and records, by local extraction |
| Inland Revenue, Self-employed or an employee guide IR336 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir336/ir336-2020.pdf | 2026-11-05 | Read in part for the no single test wording, by local extraction |
| Inland Revenue, Bright-line property tax guide IR1229 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1229/bright-line-property-tax.pdf | 2026-11-05 | Read in part for the 2-year test, by local extraction |
| Operational Statement OS 19/03 | https://www.taxtechnical.ird.govt.nz/operational-statements/os-1903-square-metre-rate-for-the-dual-use-of-premises | 2026-11-05 | Read in full for the square metre rate method, with the PDF |
| Operational Statement OS 19/04a | https://www.taxtechnical.ird.govt.nz/operational-statements/os-1904-a-commissioner-s-statement-on-using-a-kilometre-rate-for-business-running-of-a-motor-vehicle | 2026-11-05 | Read in full for the kilometre method, with the PDF |
| OS 19/04 (KM 2026) Instrument | https://www.taxtechnical.ird.govt.nz/operational-statements/2026/os-19-04-km-2026 | 2026-11-05 | Read in full for the 2025-26 rates |
| OS 19/04 (KM 2025) | https://www.taxtechnical.ird.govt.nz/operational-statements/2025/os-19-04-km-2025 | 2026-11-05 | Read in full for the 2024-25 rates |
| Approval FX 21/01 | https://www.taxtechnical.ird.govt.nz/determinations/foreign-currency/approvals/fx-21-01 | 2026-11-05 | Read in full for approved sources and methods, with the PDF |
| ACC, Calculate your levies | https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies | 2026-11-05 | Read in full by Firecrawl, because direct access was blocked, for the minimum and maximum table |
| ACC, CoverPlus invoice | https://www.acc.co.nz/for-business/received-an-invoice/explaining-your-invoice/coverplus-invoice | 2026-11-05 | Read in full by Firecrawl, because direct access was blocked, for the minimum and maximum table |

### Source conflicts

- **IETC 2024-25 part year.** ITA ss LC 14 and LC 15 use days ÷ 365. The IR3G 2025 worksheet and the prior version use months ÷ 12. Both are shown.
- **IETC 2024-25 floor.** Section LC 13(2) says 'positive amount'. Sections LC 14 and LC 15 set formulas under the heading 'Amount of credit formula: section LC 13(2)' and do not repeat 'positive'. The IR3G 2025 worksheet prints no floor at Boxes D and I, and the guide's NZD 48,000 wording fits a floor. At NZD 50,000 net income the credit is NZD 347.62 floored and NZD 261.42 on the printed boxes, and Example 2 RIT is NZD 5,160.18 or NZD 5,246.38. Both are shown and this file picks neither.
- **WFF condition wording.** ITA s LC 13(1)(d) and (e) have needed entitlement and receipt together since 30 March 2025, and Inland Revenue's IETC page says the same. IR3G 2026 still says 'not entitled'. This file follows the Act.
- **RIT as a credit.** ITA s YA 1 makes RIT the positive amount, if any. IR3G 2026 calls Box 14 'your residual income tax' and lets it be a credit. This file treats RIT as nil and carries the excess separately; the refund is the same. The YA 1 list names no section LS credit, but the worksheet subtracts overpaid PIE tax at Box 11. This file follows the worksheet there, and a reviewer confirms RIT where Box 35C decides the NZD 5,000 threshold.
- **Kilometre election with no share evidence.** ITA s DE 4(1)(c) takes a person who elected the kilometre rate method out of section DE 4, and section DE 12(3)(c) takes the business proportion from sections DE 5 to DE 11, so the Act gives no figure for a person with no records or logbook term. OS 19/04a, paragraph 20, says section DE 4(2) limits deductions to a maximum of 25% in the absence of a logbook or actual records, if that percentage can be justified. This file treats the share as Needs Input, never goes above 25% and leaves the amount to the reviewer.
- **Early payment discount application date.** ITA s RC 38(1)(d) says on or before the last date for filing under TAA s 37(5). Inland Revenue's first year page and IR289 say the date the return has to be filed. IR3G 2026 says by 31 March of the following year. This file follows the Act.
- **Initial provisional tax wording.** ITA s YA 1 requires that in the tax year the person stopped deriving income from employment and then started to derive income from a taxable activity. IR3G 2026 omits the employment limb and IR289 includes it. This file follows the Act.
- **Reassessment interest.** ITA s EF 5(1) allocates deductible interest to the income year in which it is paid. Inland Revenue's interest page says interest on a reassessment is deductible only in the income year after the year of reassessment. This file follows the Act.
- **IR3G 2026 agent date.** Page 7 prints 'until 31 March 2026' for the 2026 return. TAA s 37 gives 31 March 2027. This file follows the Act.
- **GST threshold wording.** GST Act s 51 says 'has exceeded' or 'will exceed'. Inland Revenue says 'at least NZD 60,000'. This file follows the Act.
- **Interest minimum.** TAA s 183F(1)(b) and (d) say NZD 100 or less, as do IR289 and the provisional tax interest page. Inland Revenue's main interest page says 'amounts under NZD 100'. This file follows the Act.
- **Attribution threshold.** ITA s GB 27(2)(c) reads NZD 78,100. Inland Revenue's page, updated 18 March 2021, reads NZD 70,000. This file does not apply the rule; the Act is the higher source.
- **Sibling guides.** `nz-acc-levies` calls both the earners' and work levies deductible (section 6.2) and this file holds the earners' levy. It shows Working Safer at about NZD 0.08 with no primary source here. It labels tax year 2025 as 1 April 2025 to 31 March 2026, the opposite of the prior version of this file. `nz-provisional-tax` says AIM is 'under' NZD 5,000,000; the Act says 'NZD 5,000,000 or less'. `nz-provisional-tax` also ties the standard route's interest position to on-time payment, which TAA s 120KE does not, and states a first-year exemption more widely than the initial provisional tax definition. `nz-acc-levies` levies a person below the minimum on the minimum, with no employee earnings offset (SL 2025/18 reg 6). `nz-tax-residency` says '183 days or more'; ITA s YD 1(3) says 'more than 183 days'. `nz-gst-return` reuses code R-NZ-1 and states the threshold as 'NZD 60,000 taxable supplies in any 12-month period'; `new-zealand-gst` does too. Rates in `new-zealand-crypto-tax` match this file. The bright-line text in `nz-capital-gains` matches section CB 6A.

### Other legacy topics

- **Company income.** Only salary and dividends from the company appear in an IR3. Structure first: R-NZ-2. Shareholder-employee salary with no PAYE is at Question 20.
- **Attribution.** ITA s GB 27 can attribute personal services income to a person. Reviewer. See the conflict above.
- **Working for Families.** Calculations are out of this file. The IETC interaction is under Independent earner tax credit.
- **Tier 2 cases.** Hobby or business, employee or self-employed: Inland Revenue says no single test decides (IR336), and a person can be both. Reviewer.
- **Known gaps.** Company income tax; non-resident income and NRWT; bright-line gain computation; Working for Families calculations; GST return computation; KiwiSaver employer contribution calculations.
- **Excluded jurisdictions.** The prior version names no fixed excluded jurisdiction.

Not yet confirmed: the annual taxing Act for 2026-27 (Government Bill 344-1 only, and its commentary was not read); 2026-27 kilometre and square metre rates; the Working Safer levy rate and instrument (NZD 0.08 per NZD 100 in the prior version, not read in a primary source); whether a self-employed person's earners' levy is deductible; whether each 2024-25 IETC period credit is floored at nil, and the 2024-25 part-year route; the amount for a client with a kilometre election and no share evidence; ACC Levy Guidebook 2026-27 (blocked at source); classification unit rates in the guidebook; the training expense rule; the statutory source for the next working day practice; bank formats and narrations, untested.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template. Primary-source check. Corrected penalties, the IETC basis, the GST test, the schedular default, entertainment, vehicle cap, home office, rental, filing dates and the PAYE credit. Added refusals, an operational hold, Bill and enactment standing, and evidence files. Repaired after an independent check: vehicle evidence, the residential deduction basis, the IETC floor held, and the instruments read |
| 2.1 | November 2026 | ACC levy rates and caps by year (2025-26 and 2026-27); ACC earner levy removed from RIT and the computation flow |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats (ANZ, BNZ, ASB, Westpac, Kiwibank); transaction pattern library; Windcave/PayNow patterns; worked examples; prohibitions and disclaimer added |
| 1.0 | 2025 | Initial version |

