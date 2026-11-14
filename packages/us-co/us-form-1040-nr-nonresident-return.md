---
name: us-form-1040-nr-nonresident-return
description: >
  Compute a nonresident alien's 2026 U.S. income tax on Form 1040-NR. Covers who must file, the split between effectively connected income (taxed at the section 1 graduated rates after connected deductions) and U.S.-source FDAP income that is not effectively connected (30 percent, or a lower treaty rate, on the gross amount, with no deductions), the section 871(d) election for U.S. real property income, the bar on the standard deduction, dual-status years, and the section 6013(g) choice to be taxed as a resident. Trigger on "Form 1040-NR", "nonresident alien return", "effectively connected", "FDAP", "Schedule NEC", "dual-status alien", "30 percent withholding". Day-count residency is in us-tax-residency. Gain on a U.S. real property interest is in us-nonresident-cgt. Federal only.
version: "1.0"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Form 1040-NR, nonresident alien income tax, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 871 and 6651 (U.S. Code, 2024 edition, on govinfo.gov), Rev. Proc. 2025-32 (2026 rate tables and standard deduction), the 2025 Instructions for Form 1040-NR (the latest edition on irs.gov when read), and Publication 519 (2025), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A nonresident alien's U.S. tax is two computations added together. Effectively connected income, after deductions that belong to it, is taxed at the 2026 section 1 rates (for an unmarried person, 10 percent to USD 12,400 of taxable income and 12 percent to USD 50,400). U.S.-source fixed or determinable annual or periodical income that is not effectively connected is taxed at **30 percent of the gross amount**, or at a lower rate in a treaty the person qualifies for, and no deduction is allowed against it. A nonresident alien cannot claim the standard deduction, except a student or business apprentice who qualifies under Article 21(2) of the United States-India income tax treaty.

## Scope and who this is for

In scope: one nonresident alien individual's Form 1040-NR for calendar year 2026, including Schedule NEC for income that is not effectively connected, the section 871(d) real-property election, and a dual-status year in which the person was a nonresident for part of the year and a resident for the rest.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Green card test, substantial presence test, closer connection, Form 8840 and Form 8843 | `us-tax-residency` |
| Gain on a U.S. real property interest and FIRPTA withholding | `us-nonresident-cgt` |
| Schedule E rental income, expenses and depreciation once the rent is effectively connected | `us-schedule-e-rental-income` |
| Withholding forms W-8BEN, 1042 and 1042-S | `us-nonresident-withholding-1042-w-8` |
| Expatriation tax under section 877A | `us-expatriation-exit-tax` |
| Resident Form 1040 | `us-federal-income-tax-return-1040` |

## Ask the client first

1. **Status for every day of 2026.** Green card or not, days present in the United States, and whether a treaty tie-breaker is being claimed. If the person was a resident for any part of the year, this is a dual-status year or a resident return. Day counts are in `us-tax-residency`.
2. **Marriage.** Unmarried, or married, and whether the spouse was a U.S. citizen or resident alien on 31 December 2026. That decides the rate table and whether the section 6013(g) joint-resident election is open.
3. **Each U.S. item, and where the work was done.** Wages and business income (possible effectively connected income) separate from interest, dividends, rents, royalties and pensions (possible FDAP). Services performed outside the United States are generally foreign source.
4. **Treaty residence.** Country of tax residence, whether the person has a permanent establishment or fixed base in the United States, and the article relied on. Do not apply a treaty rate until that article is read.
5. **U.S. real property held for income**, and whether a section 871(d) election is already in force from an earlier year.
6. **Withholding already taken.** Forms 1042-S, W-2 and 8288-A. Withholding is a payment, not the tax.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Tax on U.S.-source FDAP that is not effectively connected | 30 percent of the amount received | [26 U.S.C. 871(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) |
| Effectively connected taxable income | Taxed under section 1 or 55 | [26 U.S.C. 871(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) |
| Unmarried individuals, top of the 10 percent band | USD 12,400 | [Rev. Proc. 2025-32, Table 3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Tax at the top of that 10 percent band | USD 1,240 | [Rev. Proc. 2025-32, Table 3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Unmarried individuals, top of the 12 percent band | USD 50,400 | [Rev. Proc. 2025-32, Table 3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing separately, top of the 10 percent band | USD 12,400 | [Rev. Proc. 2025-32, Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Married filing separately, top of the 12 percent band | USD 50,400 | [Rev. Proc. 2025-32, Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction, unmarried, for an India student or apprentice who qualifies | USD 16,100 | [Rev. Proc. 2025-32, section 4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Standard deduction for any other nonresident alien | not allowed | [IRS, Nonresident, figuring your tax](https://www.irs.gov/individuals/international-taxpayers/nonresident-figuring-your-tax) |
| Social security benefits included in the 30 percent base | 85 percent | [26 U.S.C. 871(a)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) |
| Failure-to-file addition, per month or fraction, cap | 5 percent, not over 25 percent | [26 U.S.C. 6651(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |
| Failure-to-pay addition, per month or fraction, cap | 0.5 percent, not over 25 percent | [26 U.S.C. 6651(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |

The 30 percent rate and the penalty percentages are not indexed. The band edges and the standard deduction are the 2026 figures in Rev. Proc. 2025-32. A married nonresident who does not elect resident treatment uses the married-filing-separately table, not the single table and not head of household. The 2025 instructions say a nonresident alien cannot use married filing jointly or head of household.

### Who files

File Form 1040-NR if, during the year, the person was a nonresident alien engaged in a U.S. trade or business (even with no U.S.-source income, and even if a treaty or a Code section exempts the income), or was not engaged in a U.S. trade or business but received U.S.-source income reportable on Schedule NEC and the U.S. tax on it was not fully withheld. Also file to claim a refund of tax withheld. A person temporarily present on an F, J, M or Q visa is treated as engaged in a U.S. trade or business, but files only if there is income subject to tax under section 871. Source: [2025 Instructions for Form 1040-NR, Table A](https://www.irs.gov/instructions/i1040nr) and [26 U.S.C. 871(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm).

### Split the income

1. **Effectively connected income.** A nonresident engaged in a U.S. trade or business is taxable under section 1 on taxable income that is effectively connected. In figuring that taxable income, gross income includes only the effectively connected gross income. Wages for services performed in the United States are the usual case. Report this income on page 1 of Form 1040-NR. Source: [26 U.S.C. 871(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) and [IRS, Taxation of nonresident aliens](https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens).
2. **FDAP that is not effectively connected.** Interest, dividends, rents, salaries, wages and other fixed or determinable annual or periodical U.S.-source income, to the extent it is not effectively connected, is taxed at 30 percent of the amount received. The tax is on the gross amount. No deduction is allowed against it. Report it on Schedule NEC (Form 1040-NR). The 2025 instructions put columns on Schedule NEC for 30 percent, 15 percent, 10 percent, and any other rate, including zero. Use 30 percent unless a treaty article you have read sets a different rate for this person. Source: [26 U.S.C. 871(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) and [Publication 519 (2025), The 30% Tax](https://www.irs.gov/publications/p519).
3. **Add the two taxes.** They are not one base. Withholding on Forms W-2 and 1042-S is claimed as a payment against the sum.

### Deductions

Deductions and losses are allowed only when they are properly allocated to effectively connected income. Do not deduct items that belong to exempt income or to income that is not effectively connected. A nonresident alien cannot claim the standard deduction. The exception is a student or business apprentice eligible for Article 21(2) of the United States-India income tax treaty, who may claim the standard deduction if they do not itemize. For 2026 that standard deduction is USD 16,100 for an unmarried person. Source: [IRS, Nonresident, figuring your tax](https://www.irs.gov/individuals/international-taxpayers/nonresident-figuring-your-tax) and [Publication 519 (2025), Itemized Deductions](https://www.irs.gov/publications/p519).

### Real property election (the decision)

U.S. rent that is not otherwise effectively connected is FDAP, taxed at 30 percent of the gross rent. The owner may elect under section 871(d) to treat all income from U.S. real property held for the production of income as effectively connected. The election covers rents and gains from that property. Net income is then taxed at the section 1 rates, so expenses and depreciation that belong to the property are allowed. The election stays in effect for later years unless it is revoked with the consent of the Secretary. After a revocation, a new election generally cannot be made before the fifth taxable year that begins after the first year the revocation is effective. Make the first election by a statement attached to the return, listing the property, the ownership, the location and the income. Publication 519 says to report the rent on Schedule E (Form 1040) and carry the net to Schedule 1 (Form 1040), Part I, line 5, attached to Form 1040-NR. Source: [26 U.S.C. 871(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm) and [Publication 519 (2025), Income From Real Property](https://www.irs.gov/publications/p519).

Choose the election when 30 percent of gross rent is more than the section 1 tax on net rent. Once made, it also applies in a later year when the property has little expense, so run both years before electing.

### Dual-status year

A dual-status year is a year the person changes between nonresident and resident. For the resident part, worldwide income is taxed. For the nonresident part, U.S.-source income is taxed, and all effectively connected income is taxed. Income that is not effectively connected during the nonresident part is taxed at 30 percent or a lower treaty rate, with no deductions against it. The standard deduction is not allowed even for the resident part. A joint return is not allowed unless the person elects to be taxed as a resident. The earned income credit, the credit for the elderly or disabled, and education credits are not allowed unless that election is made.

If the person was a resident on the last day of the year, file Form 1040 or 1040-SR, write "Dual-Status Return" across the top, and attach a statement of the nonresident-period income (Form 1040-NR may be the statement; write "Dual-Status Statement" across the top and do not sign it). If the person was a nonresident on the last day, file Form 1040-NR, write "Dual-Status Return" across the top, and attach Form 1040 or 1040-SR as the unsigned "Dual-Status Statement". Source: [2025 Instructions for Form 1040-NR, Dual-Status Taxpayers](https://www.irs.gov/instructions/i1040nr).

A married nonresident whose spouse was a U.S. citizen or resident alien on the last day of the year may elect to be taxed as a resident for the whole year and file a joint Form 1040 or 1040-SR. Worldwide income for the whole year is then taxed. The election is made once, by a statement, and it can give up treaty benefits. Do not file Form 1040-NR for the year of the election. Source: [2025 Instructions for Form 1040-NR, Election To Be Taxed as a Resident Alien](https://www.irs.gov/instructions/i1040nr).

### Section 1 tax on effectively connected taxable income

For an unmarried person, or for a married person required to use the separate table (the two tables match through the 12 percent band):

- Taxable income up to USD 12,400: 10 percent.
- Taxable income over USD 12,400 and not over USD 50,400: USD 1,240 plus 12 percent of the excess over USD 12,400.

Do not subtract the standard deduction unless the India treaty exception applies. Itemized deductions on Schedule A (Form 1040-NR) are only those connected to effectively connected income. The 2025 instructions say to use Schedule A (Form 1040-NR) with Form 1040-NR, not Schedule A (Form 1040).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| F, J, M or Q student, teacher or trainee with no income taxed under section 871 | Treated as engaged in a U.S. trade or business, but no Form 1040-NR if nothing on the listed income lines is taxable |
| Only U.S. dividends, and the 30 percent (or treaty) tax was fully withheld | No return required; file if the withholding was too high and a refund is due |
| Rent, no section 871(d) election, no U.S. trade or business | 30 percent of gross rent; expenses are not deductible |
| Section 871(d) election in force | Net real property income taxed at section 1 rates; election continues until revoked with consent |
| Present 183 days or more, U.S.-source capital gains not effectively connected | 30 percent of net U.S.-source capital gain under section 871(a)(2). Real property gain is in `us-nonresident-cgt` |
| Dual-status, resident on 31 December | Form 1040 is the return; Form 1040-NR is an unsigned statement |
| Dual-status, nonresident on 31 December | Form 1040-NR is the return; Form 1040 is an unsigned statement |
| Married to a citizen or resident on 31 December, election made | Joint Form 1040 on worldwide income; do not file Form 1040-NR for that year |
| India student or apprentice under Article 21(2), not itemizing | Standard deduction USD 16,100 if unmarried |

## Worked cases

**Case 1, a decision: section 871(d) election or 30 percent of gross rent.** An unmarried nonresident, not engaged in a U.S. trade or business and not a resident of a treaty country that reduces the rent article, owns one U.S. house held for rent. 2026 gross rent is USD 40,000. Expenses that belong to the house (tax, insurance, repairs, depreciation) are USD 28,000. No other U.S. income. No standard deduction.

Without the election, tax is 30 percent of USD 40,000, which is USD 12,000, and the USD 28,000 of expenses do nothing. With the election, effectively connected taxable income is USD 12,000. That is under USD 12,400, so the tax is 10 percent, USD 1,200. The election saves USD 10,800 this year. It then stays on until the Secretary consents to a revocation, so do not elect if next year's expenses are expected to collapse and 30 percent of a smaller gross rent would be less than the graduated tax on a near-gross net.

```oa-check
name: Section 871(d) election against 30 percent of gross rent (2026)
inputs:
  gross_rent: 40000
  expenses: 28000
  statutory_rate: 0.30
  band_10_top: 12400
steps:
  - net_rent: gross_rent - expenses
  - tax_no_election: gross_rent * statutory_rate
  - tax_with_election: net_rent * 0.10
  - saving: tax_no_election - tax_with_election
expected:
  net_rent: 12000.00
  tax_no_election: 12000.00
  tax_with_election: 1200.00
  saving: 10800.00
```

**Case 2, wages in the United States plus U.S. dividends.** An unmarried nonresident performed services in the United States and was paid USD 40,000 of wages, which are effectively connected. There are no connected deductions and no standard deduction, so effectively connected taxable income is USD 40,000. The same person received USD 2,000 of U.S. dividends that are not effectively connected, and no treaty reduces them.

Effectively connected tax: USD 1,240 plus 12 percent of (USD 40,000 minus USD 12,400). The excess is USD 27,600; 12 percent is USD 3,312; the section 1 tax is USD 4,552. Dividend tax: 30 percent of USD 2,000 is USD 600. Total U.S. income tax is USD 5,152, before subtracting withholding on the W-2 and the Form 1042-S.

```oa-check
name: Effectively connected wages plus FDAP dividends, unmarried (2026)
inputs:
  wages: 40000
  dividends: 2000
  band_10_top: 12400
  tax_at_10_top: 1240
steps:
  - excess: wages - band_10_top
  - eci_tax: tax_at_10_top + excess * 0.12
  - fdap_tax: dividends * 0.30
  - total_tax: eci_tax + fdap_tax
expected:
  excess: 27600.00
  eci_tax: 4552.00
  fdap_tax: 600.00
  total_tax: 5152.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NR-RESIDENT | Green card or substantial presence for the whole year, and no treaty tie-breaker | Stop. Use Form 1040 (`us-federal-income-tax-return-1040`) |
| R-NR-DAYS | The day count or the closer-connection exception is close | `us-tax-residency` before this skill |
| R-NR-FIRPTA | Sale of a U.S. real property interest | `us-nonresident-cgt` |
| R-NR-877A | Former citizen or long-term resident, covered expatriate | `us-expatriation-exit-tax` |
| R-NR-TREATY | A treaty rate is wanted and the article has not been read | Do not guess a rate. Read the treaty, then apply it |
| R-NR-ESTATE | The filer is a nonresident estate or trust | This skill is for an individual |

## Filing and payment

For a calendar year, the 2025 instructions state the rule in two branches. An employee who received wages subject to U.S. income tax withholding files by the 15th day of the 4th month after the tax year ends (for 2025, 15 April 2026). A person who did not receive such wages files by the 15th day of the 6th month (for 2025, 15 June 2026). The same rule applied to tax year 2026 is 15 April 2027 or 15 June 2027. If the date is a Saturday, Sunday or legal holiday, file the next business day. An extension of time to file is not an extension of time to pay: Publication 519 says interest runs on tax not paid by the regular due date, and a penalty may be charged. The 2025 instructions say a first-year substantial-presence extension is requested on Form 4868.

E-file Form 1040-NR, or mail it. With no payment, the 2025 instructions say individuals mail to Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215 USA. With a payment, mail to Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303 USA. The instructions say those addresses are for Forms 1040-NR filed in 2026 and may differ for returns filed after 2026.

The failure-to-file addition is 5 percent of the tax for each month or fraction, not over 25 percent, unless the failure is due to reasonable cause and not willful neglect. The failure-to-pay addition is 0.5 percent per month or fraction, not over 25 percent, on the same reasonable-cause condition. When both run for the same month, the failure-to-file addition is reduced by the failure-to-pay addition for that month (the statute nets them). The 60-day minimum addition is indexed; the 2026 dollar amount is not in the Code section read.

## Completion checklist

- Residency for each part of 2026 is decided before this return is chosen.
- Every item is labelled effectively connected or not, with the place the services were performed.
- Schedule NEC uses 30 percent unless a treaty article that was read says otherwise.
- No standard deduction, unless the India Article 21(2) exception is documented.
- A section 871(d) election is either already in force, newly made by a statement, or deliberately not made, and both taxes were computed before the choice.
- A dual-status year uses the right form as the return and the other form as an unsigned statement.
- Withholding on Forms W-2, 1042-S and 8288-A is claimed as a payment, not left as the tax.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 871 (govinfo, U.S. Code 2024 edition). Read for (a)(1) the 30 percent tax on FDAP that is not effectively connected, (a)(2) the 183-day capital-gain tax, (a)(3) the 85 percent of social security benefits, (b) the section 1 tax on effectively connected taxable income, (c) F, J, M and Q visitors, and (d) the real property election and the five-year bar after revocation. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partII-subpartA-sec871.htm | 2026-11-13 |
| 26 U.S.C. 6651 (govinfo, U.S. Code 2024 edition). Read for (a)(1) 5 percent a month capped at 25 percent, (a)(2) 0.5 percent a month capped at 25 percent, and (a) the 60-day minimum of the lesser of the indexed base or 100 percent of the tax. The indexed 2026 dollar minimum was not in this page. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for 2026 Table 3 (unmarried: not over USD 12,400 at 10 percent; over USD 12,400 but not over USD 50,400 at USD 1,240 plus 12 percent), Table 4 (married filing separately, same two edges), and section 4.14 standard deduction USD 16,100 for unmarried individuals. | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Instructions for Form 1040-NR (2025), the latest edition on irs.gov. Read for Table A (who must file), the India Article 21(2) filing exception at the 2025 standard deduction, Schedule NEC columns, dual-status filing (which form is the return), the resident-spouse election, due dates (15th day of the 4th or 6th month), and the Austin and Charlotte mailing addresses for returns filed in 2026. | https://www.irs.gov/instructions/i1040nr | 2026-11-13 |
| IRS, Taxation of nonresident aliens. Read for the two categories, graduated rates on effectively connected income after deductions, and 30 percent on FDAP with no deductions, reported on Schedule NEC. | https://www.irs.gov/individuals/international-taxpayers/taxation-of-nonresident-aliens | 2026-11-13 |
| IRS, Nonresident, figuring your tax. Read for the sentence that a nonresident cannot claim the standard deduction, and the India Article 21 exception. | https://www.irs.gov/individuals/international-taxpayers/nonresident-figuring-your-tax | 2026-11-13 |
| Publication 519 (2025), U.S. Tax Guide for Aliens. Read for The 30% Tax, Income From Real Property (the section 871(d) statement and Schedule E to Schedule 1, line 5), the standard-deduction bar, and Form 4868 as an extension of time to file with interest if the tax is not paid by the regular due date. | https://www.irs.gov/publications/p519 | 2026-11-13 |

Not yet confirmed: the 2026 Form 1040-NR, its instructions, and the 2026 edition of Publication 519 were not published when these pages were read, so 2026 line numbers are not stated as final. The 2026 indexed minimum failure-to-file addition under section 6651(a) (the Code prints a USD 435 base that is adjusted for years after 2020) was not on the page read. Underpayment interest rates for 2026 were not read. No treaty rate table is in this skill: a treaty rate is used only after that treaty's article is read for the person.
