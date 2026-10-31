---
name: turkey-pit
description: "Turkish personal income tax (gelir vergisi) for tax year 2026 under the Income Tax Law no. 193 (GVK), for residents and non-residents with business, professional, wage, rental and investment income. Covers full and limited liability and the six-month residence test, the 2026 tariff (15% to 40%, with the separate wage scale), the seven income categories, the 2026 rental exemption of TRY 58,000, the young entrepreneur exemption, the half exemption for dividends, personal deductions, losses, the 20-year foreign income exemption for new residents from 2026, the annual return and its two instalments, quarterly provisional tax including the fourth quarter, penalties and late-payment interest. Trigger on: gelir vergisi, Turkish income tax, yıllık beyanname, geçici vergi, kira geliri vergisi, serbest meslek kazancı, GİB. Out of scope: payroll withholding and SGK premiums (tr-payroll-social), company tax (tr-corporate-income-tax), VAT (turkey-vat), the overview (tr-tax-overview)."
version: 1.1
jurisdiction: TR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Türkiye: personal income tax (gelir vergisi) (2026) v1.1

Turkish income tax is charged on individuals under the Gelir Vergisi Kanunu no. 193 (GVK) and collected by the Revenue Administration (Gelir İdaresi Başkanlığı, GİB). The tax year is the calendar year and the currency is the Turkish lira (TRY). The fixed amounts in the GVK are raised each year by a General Communiqué; the 2026 amounts below come from Communiqué no. 332 (Official Gazette 31 December 2025, no. 33124, 5th repeat), as written into the consolidated GVK text on mevzuat.gov.tr. That text includes the 2026 amending laws 7577, 7578, 7582 and 7587.

## Who this applies to

- **Full liability (tam mükellefiyet).** Individuals settled in Türkiye are taxed on their worldwide income (GVK art. 3). A person is settled in Türkiye if their legal domicile is in Türkiye, or if they stay in Türkiye continuously for more than six months in a calendar year; temporary absences do not break the stay (art. 4).
- **Not settled despite a long stay.** Foreigners who come for a specific, temporary job or assignment (business people, scientists, experts, officials, journalists and similar), or to study, for treatment, rest or travel, are not settled even after six months. Nor are people held in Türkiye by detention, imprisonment or illness (art. 5).
- **Limited liability (dar mükellefiyet).** Individuals not settled in Türkiye are taxed only on income earned in Türkiye (art. 6). Business income is earned in Türkiye only if the person has a workplace or permanent representative there and the income is earned through it (art. 7).
- **Turkish citizens posted abroad** by Turkish public bodies or Turkish-based firms stay fully liable, but income taxed abroad is not taxed again (art. 3(2)).
- **Out of this skill:** monthly payroll withholding, SGK premiums and stamp tax on wages (see [tr-payroll-social](tr-payroll-social.md)); companies ([tr-corporate-income-tax](tr-corporate-income-tax.md)); VAT ([turkey-vat](turkey-vat.md)); the simple method (basit usul) and the tradesman exemption (esnaf muaflığı), which this skill does not cover.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tariff, all income other than wages | 15% to TRY 190,000; TRY 28,500 + 20% to TRY 400,000; TRY 70,500 + 27% to TRY 1,000,000; TRY 232,500 + 35% to TRY 5,300,000; TRY 1,737,500 + 40% above | 2026 | GVK art. 103 with Communiqué 332 amounts, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.193.pdf |
| Tariff, wage income | 15% to TRY 190,000; TRY 28,500 + 20% to TRY 400,000; TRY 70,500 + 27% to TRY 1,500,000; TRY 367,500 + 35% to TRY 5,300,000; TRY 1,697,500 + 40% above | 2026 | GVK art. 103 |
| Rental exemption, residential lettings | TRY 58,000 of the year's gross rent | 2026 | GVK art. 21(1) |
| Rental exemption lost if gross wages, investment, rental and other income together exceed | TRY 1,500,000 (the wage scale's third band) | 2026 | GVK art. 21(2), art. 103 |
| Lump-sum expense for rental income (instead of actual costs) | 15% of gross rent; locked in for two years | 2026 | GVK art. 74 |
| Young entrepreneur exemption (under 29, first business, first three tax years) | Profit up to TRY 400,000 (the tariff's second band) | 2026 | GVK mükerrer art. 20, art. 103 |
| Dividends from Turkish companies | Half exempt | 2026 | GVK art. 22(3) |
| Dividend withholding | 15% | 2026 | Presidential Decision 9286, art. 1 (GVK art. 94(6)), https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf |
| Investment and rental income not withheld, no return needed if the year's total is at most | TRY 22,000 | 2026 | GVK art. 86(1)(d) |
| Wages from one employer, fully withheld: no return up to | TRY 5,300,000 (fourth band) | 2026 | GVK art. 86(1)(b) |
| Wages from a second employer: no return if second-employer wages do not exceed | TRY 400,000, and total wages do not exceed TRY 5,300,000 | 2026 | GVK art. 86(1)(b) |
| Withheld multiple-employer wages, investment and rental income: no return if total does not exceed | TRY 400,000 | 2026 | GVK art. 86(1)(c) |
| Personal insurance premiums (life at 50%) deductible | Up to 15% of declared income and the annual gross minimum wage | 2026 | GVK art. 89(1) |
| Education and health spending (self, spouse, minor children, in Türkiye, documented) | Up to 10% of declared income | 2026 | GVK art. 89(2) |
| Donations to public bodies, public-benefit associations and tax-exempt foundations | Up to 5% of declared income (10% in priority development regions) | 2026 | GVK art. 89(4) |
| Disability allowance (monthly, from wages) | TRY 12,000 (1st degree), TRY 7,000 (2nd), TRY 3,000 (3rd) | 2026 | GVK art. 31 |
| Provisional tax rate | 15% (the first band rate) | 2026 | GVK mükerrer art. 120 |
| Loss carry-forward | 5 years | 2026 | GVK art. 88 |
| Foreign income exemption for new residents | 20 years | 2026 | GVK mükerrer art. 20/D (Law 7582) |

## The taxable base

**Seven income categories** (GVK art. 2): business income (ticari kazanç), agricultural income (zirai kazanç), wages (ücret), professional income (serbest meslek kazancı), rental income from immovable property and rights (gayrimenkul sermaye iradı, art. 70), investment income such as interest and dividends (menkul sermaye iradı, art. 75), and other gains (diğer kazanç ve iratlar, art. 80, including capital gains). Each is computed net under its own rules, then the declarable categories are added together on the annual return (art. 85).

**Computation.** Add the net income of each declarable category. Deduct the art. 89 deductions. Apply the art. 103 tariff to the total (art. 104). The wage scale applies to wage income; the other scale applies to everything else. Deduct provisional tax paid in the year and tax withheld at source on income included in the return (mükerrer art. 120; art. 121). Foreign tax on foreign income is credited up to the Turkish tax on that income, if the foreign tax is a personal income tax and is documented (art. 123).

**Rental income.** The first TRY 58,000 of gross residential rent in 2026 is exempt, unless the rent is not declared or is under-declared, or the person must file for business, agricultural or professional income, or their gross wages, investment income, rental income and other income together exceed TRY 1,500,000 (art. 21). Against the taxable rent the owner deducts either actual costs (art. 74: utilities paid by the owner, management, insurance, taxes and fees, depreciation, repairs, maintenance; interest on loans for let property other than dwellings, a rule in force for the 2025 tax year onward under Law 7566; for one let dwelling, 5% of its purchase price for five years from the purchase year instead) or a 15% lump sum. The lump-sum choice cannot be changed for two years. Fines and tax penalties are not deductible.

**Dividends.** Half of a dividend from a fully liable Turkish company is exempt. Tax withheld on the dividend (15%) is credited in full against the return if the dividend is declared (art. 22(3)). Half of a dividend from a foreign joint-stock or limited company is also exempt if the person owns at least 50% of its paid-in capital and the dividend is brought to Türkiye by the return deadline (art. 22(4)).

**Young entrepreneurs.** A fully liable individual who opens a first business, agricultural or professional activity before turning 29 is exempt on profit up to TRY 400,000 (2026) for three tax years from the start, if they notified the start on time, run the business themselves, all partners qualify, and the business was not taken over from a spouse or relative to the third degree. A return is still required. The exemption does not reduce tax withheld at source (mükerrer art. 20).

**Losses.** A loss in one category is set against the others in the same year (except losses in "other gains" under art. 80). An unused loss is carried forward for five years. Foreign business losses are deductible only with an audited report from the foreign country (art. 88).

**Exempt wages.** The wage exemptions in art. 23 include employer-provided meals (or a meal payment up to TRY 300 a working day in 2026), employer-provided transport (or a transport payment up to TRY 158 a day), and the minimum-wage exemption under art. 23(18). These are applied in payroll; see [tr-payroll-social](tr-payroll-social.md).

## Deadlines and filing

- **Annual return (Yıllık Gelir Vergisi Beyannamesi).** GVK art. 92 says the return is filed from 1 to 25 March of the following year. GİB's current table of filing and payment dates says by the last day of March, 23:59. Use GİB's date for filing, and treat the 25 March statutory date as the safe date. Returns are filed with GİB electronically.
- **Payment.** The tax is paid in two equal instalments, in March and July (GVK art. 117). GİB's table gives the end of March and the end of July. Where agricultural income is 75% or more of total income, GİB's table gives November and December.
- **Leaving Türkiye or death.** A person who leaves the country in the year files within the 15 days before leaving; for a death, within four months (art. 92).
- **Provisional tax (geçici vergi).** Business and professional taxpayers pay provisional tax at 15% on cumulative quarterly profit, for all four quarters from the 2025 tax year (Law 7566 removed the "first nine months" limit). The law says each quarter is declared by the 14th and paid by the 17th day of the second month after the quarter (mükerrer art. 120); GİB's table gives the 17th for both: 17 May, 17 August, 17 November and 17 February. Tax withheld in the same period is deducted. Provisional tax is credited against the annual tax; any remainder is offset against other tax debts or refunded on written request by the end of that year.
- **Who files.** Every business, agricultural and professional taxpayer files, even with no profit (art. 85). Others file when their income passes the art. 86 limits in the rates table. Young entrepreneurs file even inside the exemption.

## Penalties and interest

- **Late filing.** A return filed late is a first-degree irregularity (VUK art. 352). The 2026 fine is TRY 17,000 for first-class traders and professionals, TRY 8,700 for second-class traders, TRY 6,000 for other people filing returns and TRY 4,000 for simple-method taxpayers (VUK table 1 with VUK Communiqué 588).
- **Tax loss (vergi ziyaı).** If tax is lost, the penalty is one times the lost tax; three times where false or misleading documents are involved. For a return filed late but before an audit starts, the penalty is halved. It rises by 50% where the person carried on business without registering (VUK art. 344).
- **Late payment.** Unpaid tax carries a late-payment surcharge (gecikme zammı) of 3.7% for each month, computed daily for part months, set by Presidential Decision 10556 (Official Gazette 13 November 2025) under Law 6183 art. 51.
- **Not issuing an invoice or receipt.** Each missing invoice, expense voucher, producer receipt or self-employment receipt draws a special irregularity penalty of 10% of the amount, at least TRY 17,000 for the first finding in a calendar year (VUK art. 353(1), 2026 amount).

## Cross-border points

- **New residents from 2026.** A person who becomes settled in Türkiye from 1 January 2026, and who had no domicile and no tax liability in Türkiye in the previous three calendar years, is exempt on income earned outside Türkiye for 20 years. Earlier liability only for Turkish rental income, investment income or capital gains does not block the exemption. Exempt foreign income is not declared; costs linked to it are not deductible; foreign tax on it is not credited (GVK mükerrer art. 20/D, added by Law 7582, in force 4 June 2026).
- **Foreign tax credit.** Residents credit foreign personal income tax on foreign income up to the Turkish tax on that income, computed by its share of total income, with documents certified by the Turkish consulate. Without the documents by the instalment date, the tax on that income is deferred for one year (art. 123).
- **Foreign income timing.** Foreign income is earned when it is booked in Türkiye or, if that is prevented, when the person can dispose of it (art. 85).
- **Non-residents.** A non-resident does not file for Turkish wages, professional income, investment income, rental income or other income that was fully taxed by withholding in Türkiye (art. 86(2)). Wages paid in foreign currency by an employer with no legal or business seat in Türkiye, out of profits it earns outside Türkiye, are exempt (art. 23(14)).
- **Treaties.** A tax treaty can lower Turkish withholding on dividends, interest and royalties. Treaty rates are not covered here.

## Worked examples

### Example 1: Freelance software developer, 2026

A resident freelance developer (serbest meslek erbabı) invoices TRY 1,200,000 in 2026 and has documented business costs of TRY 300,000. Net professional income is TRY 900,000. On the non-wage scale, the tax is 15% of the first TRY 190,000 (TRY 28,500), 20% of the next TRY 210,000 (TRY 42,000) and 27% of the remaining TRY 500,000 (TRY 135,000): TRY 205,500 in total. She paid TRY 120,000 of provisional tax during 2026. The balance of TRY 85,500 is paid in two instalments of TRY 42,750, by the end of March and the end of July 2027. Any tax withheld by her business clients would also be deducted; this example assumes none.

```oa-check
name: Freelance developer, net income TRY 900,000 (2026 non-wage tariff)
inputs:
  fees: 1200000
  costs: 300000
  provisional_paid: 120000
steps:
  - income: fees - costs
  - band_15: min(income, 190000) * 0.15
  - band_20: max(min(income, 400000) - 190000, 0) * 0.20
  - band_27: max(min(income, 1000000) - 400000, 0) * 0.27
  - band_35: max(min(income, 5300000) - 1000000, 0) * 0.35
  - band_40: max(income - 5300000, 0) * 0.40
  - tax: band_15 + band_20 + band_27 + band_35 + band_40
  - balance: tax - provisional_paid
  - instalment: balance / 2
expected:
  income: 900000
  tax: 205500
  balance: 85500
  instalment: 42750
```

### Example 2: Employee who also lets a flat (the rental exemption is lost)

A resident employee earns gross wages of TRY 2,000,000 in 2026 from one employer, all taxed by withholding, and lets a flat for TRY 300,000 a year. The wages stay off the return, because one employer's wages under TRY 5,300,000 are not declared (art. 86(1)(b)). But because the gross wages exceed TRY 1,500,000, the TRY 58,000 rental exemption is lost (art. 21(2)). He takes the 15% lump-sum expense, so taxable rent is TRY 255,000. Tax on the non-wage scale is TRY 28,500 on the first TRY 190,000 plus 20% of TRY 65,000 (TRY 13,000): TRY 41,500. Had his gross wages been TRY 1,400,000, the exemption would apply: TRY 242,000 of taxable rent, less 15%, is TRY 205,700, and the tax would be TRY 31,640. The flag step below is 1 when wages are TRY 1,500,000 or less and 0 above it.

```oa-check
name: Rental income with the exemption lost (gross wages TRY 2,000,000, 2026)
inputs:
  gross_wages: 2000000
  rent: 300000
steps:
  - exemption_flag: min(max(1500000 - gross_wages + 1, 0), 1)
  - exemption: 58000 * exemption_flag
  - taxable_rent: (rent - exemption) * 0.85
  - band_15: min(taxable_rent, 190000) * 0.15
  - band_20: max(min(taxable_rent, 400000) - 190000, 0) * 0.20
  - band_27: max(min(taxable_rent, 1000000) - 400000, 0) * 0.27
  - tax: band_15 + band_20 + band_27
expected:
  exemption: 0
  taxable_rent: 255000
  tax: 41500
```

## Ask the client first

1. Where is your legal domicile, and how many days were you in Türkiye in 2026? If you moved to Türkiye in 2026, were you resident or taxable in Türkiye in 2023, 2024 or 2025?
2. What kinds of income did you have: business, professional, wages (from how many employers), rent, interest, dividends, gains, foreign income?
3. For rental income: is the property residential, what was the gross rent, and do you want actual costs or the 15% lump sum (and which did you use last year)?
4. Did you pay provisional tax in 2026, and was tax withheld from your fees, rent or dividends?
5. Were you under 29 when you first registered a business, and in which year did it start?
6. Do you have documented education, health, insurance or donation spending to deduct?

## Sources

| Source | URL | Read on |
|---|---|---|
| Gelir Vergisi Kanunu no. 193, consolidated (2026 amounts from Communiqué 332; amendments to Law 7587): arts. 2-7, 20, 20/D, 21, 22, 23, 31, 74, 85, 86, 88, 89, 92, 94, 103, 104, 117, 120, 121, 123 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.193.pdf | 2026-10-31 |
| Vergi Usul Kanunu no. 213, consolidated (2026 amounts from VUK Communiqué 588): arts. 344, 352, 353 and penalty table 1 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.213.pdf | 2026-10-31 |
| Law 6183 on collection of public receivables, art. 51 (3.7% a month, Presidential Decision 10556) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6183.pdf | 2026-10-31 |
| GİB, Beyanname verme ve ödeme süreleri (filing and payment dates table) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-10-31 |
| Presidential Decision 9286 (dividend withholding 10% to 15%), Official Gazette 22 December 2024 no. 32760 | https://www.resmigazete.gov.tr/eskiler/2024/12/20241222-15.pdf | 2026-10-31 |

Not yet confirmed: withholding rates on professional fees, rent and interest under decision 2009/14592 (not read); the simple method (basit usul) and the tradesman exemption (art. 9) amounts; capital gains (art. 80 and 81, including the 2026 exemption amount in mükerrer art. 80); crypto-asset gains; the exemption for severance pay (kıdem tazminatı, art. 25) and its 2026 ceiling; the state contribution to private pensions (BES, Law 4632) and the deduction for employer pension contributions; sponsorship deductions (art. 89(5)-(10) read in part only); whether the self-employed deduct their own social security premiums as a business expense (art. 68 and 40 not read for this); the legal basis for GİB's end-of-March filing date when art. 92 says 25 March; the procedure communiqué for the art. 20/D exemption; treaty rates. The cumulative monthly withholding table from the old version is now in tr-payroll-social.
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
