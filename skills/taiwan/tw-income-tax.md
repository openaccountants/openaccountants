---
name: tw-income-tax
description: Use this skill whenever asked about Taiwan individual income tax (綜合所得稅) for tax year 2026, filed in May 2027. Trigger on phrases like "Taiwan income tax", "綜合所得稅", "個人所得稅", "Taiwan tax return", "eFiling Taiwan", "National Taxation Bureau", "執行業務所得", "freelancer Taiwan", or any question about computing or filing Taiwan personal income tax. It gives the 2026 brackets (5% to 40%, first band to NT$610,000), the NT$101,000 exemption, NT$136,000 standard deduction, NT$227,000 salary deduction, the special deductions, professional expense rates, dividends, non-residents and the basic tax. Built from the law, not reviewed by an accountant.
version: "2.0"
jurisdiction: TW
tax_year: 2026
tax_year_notes: "Calendar tax year 2026 (民國115年度), filed 1 to 31 May 2027. CPI-indexed amounts from MOF announcement of 27 November 2025. Professional expense rates are the 2025 (114年度) standard published March 2026; the 2026 standard is not yet issued."
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Taiwan individual income tax (綜合所得稅), tax year 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Taiwan.

## Who this applies to

Individuals with Taiwan-source income for calendar year 2026 (民國115年度). A resident (domiciled in Taiwan, or present 183 days or more in the year) files a consolidated return for the household (taxpayer, spouse and claimed dependants) and is taxed at progressive rates. A non-resident (under 183 days) is generally taxed by final withholding. Currency: New Taiwan dollar (NT$). Authority: Ministry of Finance (財政部), through the National Taxation Bureaus (國稅局). Return: eFiling, filed 1 to 31 May 2027 for 2026 income. Main law: Income Tax Act (所得稅法); also Income Basic Tax Act (所得基本稅額條例) and Tax Collection Act (稅捐稽徵法).

Out of scope: business tax on sales (`taiwan-vat`), company tax (`tw-corporate-income-tax`), health insurance (`tw-nhi`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Band 1 | 5%, progressive difference 0 | Net income NT$0 to 610,000 | https://www.ntbt.gov.tw/multiplehtml/1b82b380e1a34de9afd204d39b007db2 |
| Band 2 | 12%, less 42,700 | NT$610,001 to 1,380,000 | same |
| Band 3 | 20%, less 153,100 | NT$1,380,001 to 2,770,000 | same |
| Band 4 | 30%, less 430,100 | NT$2,770,001 to 5,190,000 | same |
| Band 5 | 40%, less 949,100 | Above NT$5,190,000 | same |
| Personal exemption (免稅額) | NT$101,000 per person | Taxpayer, spouse, each qualifying dependant; 2026 (2025: 97,000) | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c |
| Exemption, aged 70 or over | NT$151,500 per person | Taxpayer, spouse, or dependent lineal ascendant aged 70 or over | same |
| Standard deduction, single | NT$136,000 | 2026 (2025: 131,000) | same |
| Standard deduction, married | NT$272,000 | Same | same |
| Salary special deduction (薪資所得特別扣除額) | Up to NT$227,000 per earner | 2026 (2025: 218,000) | same |
| Disability special deduction | NT$227,000 per person | 2026 | same |
| Basic tax (AMT) deduction for individuals | 750萬 (7.5 million NT dollars) | Not adjusted for 2026 | same |
| Savings and investment special deduction | Up to 27萬元 (270 thousand NT dollars) per household | Bank interest and listed items | https://www.ntbt.gov.tw/multiplehtml/f4e3899a499b4f05821af5a5afadd2f5 |
| Tertiary tuition special deduction | Up to NT$25,000 per child | Recognised college or university | same |
| Preschool child special deduction (6 and under) | NT$150,000 first child; NT$225,000 each further child | Subject to the exclusions below | same |
| Long-term care special deduction | NT$180,000 per person | Qualifying long-term care need; subject to the exclusions below | same |
| Rent special deduction | Up to NT$180,000 per household | Rented home for own use in Taiwan, no own home; exclusions below | same |
| Exclusions for preschool, long-term care and rent | Not available | If the marginal rate is 20% or more, the 28% dividend option is chosen, or basic income exceeds 750萬元 | same |
| Itemised: insurance premiums | Up to NT$24,000 per person | NHI premiums without limit | same |
| Itemised: donations | Up to 20% of gross consolidated income | Government, defence and listed cultural donations without limit | same |
| Itemised: home mortgage interest | Up to 30萬元 (300 thousand NT dollars), less the savings deduction used | One owner-occupied home in Taiwan | same |
| Late payment surcharge (滯納金) | 1% for each 3 days late, capped at 10% | From 2022 (Tax Collection Act art. 20) | https://www.ntbt.gov.tw/singlehtml/2dbb2b6ec3714b469267299f687be37c?cntId=6047d2df3fb144a6abb413dd828da9b7 |
| Professional expense rate, lawyers | 30% | 2025 (114年度) standard, for those without proper books | https://law-out.mof.gov.tw/LawContent.aspx?id=GL011721 |
| Professional expense rate, CPAs and bookkeepers | 35% | Same | same |
| Professional expense rate, architects and engineers (技師) | 35% | Same | same |
| Professional expense rate, authors | 30% of fees after the statutory exemption | Self-publishing 75% | same |
| Professional expense rate, performers | 45% | Same | same |
| Professional expense rate, insurance brokers | 26% | Same | same |
| Professional expense rate, programmers (程式設計師) | 20% | Same | same |

## The base

### Income categories (所得類別)

| Category | Chinese | Description |
| --- | --- | --- |
| 1 | 營利所得 | Business or profit income (sole proprietor, partnership, dividends) |
| 2 | 執行業務所得 | Professional practice income (lawyers, doctors, accountants, freelancers) |
| 3 | 薪資所得 | Salary and wages |
| 4 | 利息所得 | Interest |
| 5 | 租賃所得 | Rent |
| 6 | 權利金所得 | Royalties |
| 7 | 財產交易所得 | Property transaction income |
| 8 | 競技、競賽及機會中獎之獎金 | Prizes and lottery winnings |
| 9 | 退職所得 | Retirement income |
| 10 | 其他所得 | Other income |

### Professional practice income (執行業務所得)

Professionals with proper books report actual income less documented expenses. The MOF expense standard is only for those who did not file, keep books or produce records; it estimates net income as revenue times (1 less the expense rate). The 2025 standard (rates table) applies to 2025 income; the 2026 standard is normally issued in the following spring. Correction: the old file gave CPAs 30% and software developers 30%; the MOF standard gives CPAs 35% and programmers 20%. Doctors have several rates (for example 40% for general practice); check the standard line by line.

### Computation worksheet

1. **Gross consolidated income (綜合所得總額):** salary, professional, business, interest, rent, other income of the household (dividends included unless the 28% separate option is chosen).
2. **Less exemptions:** NT$101,000 per person (151,500 for those aged 70 or over).
3. **Less the larger of** the standard deduction (136,000 single, 272,000 married) **and** itemised deductions (donations, insurance premiums, medical and childbirth costs at qualifying hospitals net of insurance, disaster losses with proof, home mortgage interest, political donations).
4. **Less special deductions:** salary (up to 227,000 per earner), savings and investment (up to 270,000), disability (227,000), tuition (25,000), preschool (150,000 or 225,000), long-term care (180,000), rent (180,000), property transaction losses.
5. **Basic living expense difference (基本生活費差額):** if the per-person basic living expense times household size exceeds the total of exemptions and the listed deductions, the excess is also deducted (2025 amount NT$213,000 per person; the 2026 amount is not yet confirmed).
6. **Net consolidated income (綜合所得淨額)** times the band rate, less the progressive difference.
7. **Less** dividend credit (if dividends included), withholding and prepaid tax.
8. **Compare** with the basic tax (AMT) if basic income exceeds 750萬元.

### Dividends (since 2018)

Choose the better of: (A) include dividends in consolidated income and claim an 8.5% credit capped at NT$80,000 per household; or (B) tax dividends separately at 28%. (B) suits taxpayers whose marginal rate is above 28%. Choosing (B) removes the preschool, long-term care and rent special deductions. The 8.5% and NT$80,000 figures are not confirmed on an official page in this pass.

### Married filing

Married couples file one return. Salary income (and, separately, other income) of a spouse may be computed separately, with that spouse's own exemption and salary deduction; eFiling compares the methods.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown filing status | Single |
| Unknown deduction method | Standard deduction unless itemised clearly exceeds it |
| Unknown residency | Present 183 days or more: resident |
| Unknown withholding | Verify against the eFiling pre-filled data |
| Business or employment | Employment unless clear independent activity |

## Deadlines and filing

| Item | Detail |
| --- | --- |
| Filing and payment period | 1 to 31 May 2027 for 2026 income (moved to the next working day if it ends on a holiday) |
| Methods | eFiling (網路申報) at the MOF portal, mobile filing, paper filing at a National Taxation Bureau, or by a tax agent |
| Authentication | Citizen Digital Certificate, NHI card with password, mobile ID, bank certificate, TW FidO |
| Withholding statements | Payers report withholding in January and issue statements to recipients |
| Instalments and extensions | On application for hardship; rules not restated here |

## Penalties and interest

Late payment: surcharge of 1% for every 3 days late, up to 10% (Tax Collection Act art. 20, from 1 January 2022), then interest. Correction: the old file said 1% per 2 days, up to 15%, the rule before 2022. Under-reporting and failure to file attract fines under Income Tax Act art. 110 (rates not restated here).

## Cross-border points

| Rule | Detail |
| --- | --- |
| Resident | Domiciled in Taiwan, or present 183 days or more in the year: progressive rates |
| Non-resident | Final withholding on Taiwan-source income; non-resident salary at 18% (6% where the monthly salary is at most 1.5 times the basic wage), professional fees 20%, dividends 21% (not confirmed on an official page in this pass) |
| Overseas income | Not in regular consolidated income; included in basic income for the AMT if the household's overseas income is NT$1,000,000 or more |
| Basic tax (AMT) | Basic income above NT$7,500,000 is taxed at 20%; pay the higher of regular tax and basic tax (20% not confirmed in this pass) |
| Real property sold (房地合一) | Property acquired from 1 January 2016 is taxed separately on the gain; resident rates by holding period 45% (2 years or less), 35% (2 to 5 years), 20% (5 to 10 years), 15% (over 10 years); self-use residence relief (not confirmed in this pass) |

## Two worked examples that recompute

**Example 1: single freelance programmer without books, 2026.** Revenue NT$2,000,000; expense rate 20% (2025 standard, used as the estimate) gives net professional income 1,600,000. Bank interest 30,000. Gross 1,630,000. Less exemption 101,000, standard deduction 136,000 and savings deduction 30,000: net 1,363,000. Tax: 1,363,000 x 12% less 42,700 = NT$120,860. (The old file used 30% and 2025 amounts and forgot the savings deduction.)

```oa-check
name: TW 2026 single freelance programmer, deemed 20% expenses
inputs:
  revenue: 2000000
  interest: 30000
steps:
  - professional: revenue * (1 - 0.20)
  - gross: professional + interest
  - net: gross - 101000 - 136000 - min(interest, 270000)
  - tax: net * 0.12 - 42700
expected:
  professional: 1600000
  net: 1363000
  tax: 120860
```

**Example 2: decision, compute the wife's salary separately or not (2026).** Husband salary 1,800,000; wife salary 700,000; one child aged 3. Combined: gross 2,500,000 less exemptions 303,000, standard deduction 272,000, two salary deductions 454,000 and preschool deduction 150,000 = 1,321,000; tax 1,321,000 x 12% less 42,700 = 115,820. Separate salary computation: wife 700,000 less her exemption 101,000 and salary deduction 227,000 = 372,000 at 5% = 18,600; rest of household 1,800,000 less 202,000, 272,000, 227,000 and 150,000 = 949,000 at 12% less 42,700 = 71,180; total 89,780. Separate computation saves NT$26,040. The preschool deduction is kept because the marginal rate stays below 20%.

```oa-check
name: TW 2026 married couple, combined vs separate salary computation
inputs:
  husband: 1800000
  wife: 700000
steps:
  - combined_net: husband + wife - 3 * 101000 - 272000 - 2 * 227000 - 150000
  - combined_tax: combined_net * 0.12 - 42700
  - wife_net: wife - 101000 - 227000
  - wife_tax: wife_net * 0.05
  - rest_net: husband - 2 * 101000 - 272000 - 227000 - 150000
  - rest_tax: rest_net * 0.12 - 42700
  - separate_tax: wife_tax + rest_tax
  - saving: combined_tax - separate_tax
expected:
  combined_net: 1321000
  combined_tax: 115820
  separate_tax: 89780
  saving: 26040
```

## Ask the client first

1. Residence in 2026: domicile, days in Taiwan.
2. Household: spouse, children (ages), dependants aged 60 or 70 or over.
3. Each income type for 2026, and whether professional income is from proper books.
4. Dividends and the household's marginal rate (28% option).
5. Rent or mortgage, insurance, medical, donations (itemised or special deductions).
6. Overseas income and large insurance or unlisted share gains (basic tax).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Taipei National Taxation Bureau, applicable rates. Read for the 2026 (115年度) brackets and progressive differences | https://www.ntbt.gov.tw/multiplehtml/1b82b380e1a34de9afd204d39b007db2 | 2026-11-14 |
| MOF, 2026 amounts table (PDF attached to the 27 November 2025 announcement). Read for the exemption, standard, salary and disability deductions, brackets and the 7,500,000 basic tax deduction | https://www.mof.gov.tw/download/bb34472701e4443c910788e792dae85c | 2026-11-14 |
| MOF, announcement of 2026 amounts. Read for the 4.13% CPI adjustment and May 2027 filing | https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=34b463dc8f1b49f29d440d92a6fd5139 | 2026-11-14 |
| Taipei National Taxation Bureau, exemptions and deductions (2025 page for residents). Read for the special and itemised deduction amounts, exclusions and the 213,000 basic living expense for 2025 | https://www.ntbt.gov.tw/multiplehtml/f4e3899a499b4f05821af5a5afadd2f5 | 2026-11-14 |
| MOF, 2025 professional expense standard (114年度執行業務者費用標準). Read for the expense rates | https://law-out.mof.gov.tw/LawContent.aspx?id=GL011721 | 2026-11-14 |
| Taipei National Taxation Bureau, surcharge calculation. Read for the 3-day steps and the 10% cap | https://www.ntbt.gov.tw/singlehtml/2dbb2b6ec3714b469267299f687be37c?cntId=6047d2df3fb144a6abb413dd828da9b7 | 2026-11-14 |

Not yet confirmed: the 2026 basic living expense per person; the 2026 professional expense standard; the dividend credit (8.5%, NT$80,000) and 28% option figures; the basic tax rate of 20%; non-resident withholding rates (18%, 6%, 20%, 21%); house and land tax rates by holding period; political donation limits (old file: NT$200,000); withholding rates for residents (old file: 10% on professional fees, rent, interest, prizes). The Income Tax Act text on law.moj.gov.tw did not load in this pass.
