---
name: pr-federal-residence-and-filing
description: "Decide, for tax year 2026, whether a United States citizen or resident alien is a bona fide resident of Puerto Rico for federal tax, which income is Puerto Rico source, what section 933 excludes, and which federal and Puerto Rico returns are required. Covers the five presence alternatives (183 days, 549 days with 60 in each year, no more than 90 days in the United States, no more than USD 3,000 of United States earned income, no significant connection), the tax home and closer connection tests, the year-of-move rules, the time-basis source rule for services, the gain rule for property held before the move, United States Government and military pay, the Publication 1321 standard deduction apportionment and filing test, and Form 8898 when worldwide gross income is more than USD 75,000. Trigger on \"bona fide resident of Puerto Rico\", \"section 933\", \"section 937\", \"Form 8898\", \"Publication 570\", \"Publication 1321\", \"move to Puerto Rico\", \"do I file a US return from Puerto Rico\". Federal ru"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pr-federal-residence-and-filing"
  jurisdiction: "PR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Puerto Rico: federal residence, income source and filing, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 933 and 937, Treas. Reg. 1.937-1, IRS Publication 570 (2025, the edition current on the read date), IRS Publication 1321 (October 2026) and the Form 8898 instructions (Rev. October 2024), read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Three separate decisions, in this order. **1. Residence:** a United States citizen or resident alien is a bona fide resident of Puerto Rico for 2026 only if they meet one of five presence alternatives (at least **183 days** in Puerto Rico; or at least **549 days** over 2024 to 2026 with at least **60 days** in each year; or no more than **90 days** in the United States; or no more than **USD 3,000** of United States earned income and more days in Puerto Rico than in the United States; or no significant connection to the United States) **and** have no tax home outside Puerto Rico **and** no closer connection to the United States or a foreign country. **2. Source:** each item of income is sourced on its own rules; pay for services is sourced where the work is done. **3. Returns:** a full-year bona fide resident excludes Puerto Rico source income from federal gross income under section 933, except pay as a United States Government employee. They file a Puerto Rico return on worldwide income, a federal Form 1040 only if their non-excluded income meets the apportioned filing test, and Form 1040-SS if they owe only self-employment tax. Form 8898 is due in the year residence starts or ends when worldwide gross income is more than **USD 75,000**.

## Scope and who this is for

In scope: United States citizens and resident aliens who live, or plan to live, in Puerto Rico in tax year 2026, and the federal questions that decide what they file: bona fide residence (section 937(a) and Treas. Reg. 1.937-1), the source of each income item (section 937(b)), the section 933 exclusion, the year of a move, and the federal filing test after the exclusion.

A nonresident alien of the United States does not use the five presence alternatives. They use the substantial presence test of Publication 519 with "Puerto Rico" put in place of "United States", and the closer-connection-to-a-foreign-country discussion there is ignored. [Publication 570, Special rule for nonresident aliens](https://www.irs.gov/pub/irs-pdf/p570.pdf).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The Puerto Rico individual return, rates and exemptions | `pr-individual-income-tax` |
| Federal self-employment tax and Form 1040-SS | `pr-self-employment-tax` |
| Act 60 resident-investor and export-services decrees | `pr-act-60-incentives` |
| Puerto Rico regular corporate tax | `pr-company-income-tax` |
| 2026 federal standard deduction and other 1040 amounts | `us-2026-federal-tax-changes` |
| Foreign tax credit mechanics (Form 1116) | `us-foreign-tax-credit-1116` |
| Child tax credit and earned income credit amounts | `us-child-tax-credit-and-eitc` |
| Nonresident alien federal return | `us-form-1040-nr-nonresident-return` |

## Ask the client first

1. **Status:** United States citizen, green-card holder (resident alien) or nonresident alien. Member of the United States Armed Forces, or civilian spouse of one.
2. **Days:** days physically present in Puerto Rico, in the United States and elsewhere, for 2026, 2025 and 2024, with any days for medical treatment, a declared disaster or evacuation, travel outside both, or study.
3. **Work and ties:** where the main place of business or employment is; permanent home in the United States; where the spouse and children under 18 live; voter registration; driver's licence; banking; where belongings are.
4. **Move:** the date the person moved to or from Puerto Rico, and whether they were a bona fide resident in any of the three years before.
5. **Income by item:** wages (and the employer, including any United States Government agency), self-employment work days by location, interest and dividends by payer, rents by property location, gains, with the date each investment was bought and its value on the day the tax home moved.
6. **Size:** worldwide gross income for 2026, including income to be excluded, before deductions (for Form 8898).

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Presence alternative 1 | At least 183 days in Puerto Rico | In the tax year | [Treas. Reg. 1.937-1(c)(1)(i)](https://www.ecfr.gov/current/title-26/section-1.937-1) |
| Presence alternative 2 | At least 549 days in Puerto Rico | Over the tax year and the 2 years before, with at least 60 days in each of the 3 years | [Treas. Reg. 1.937-1(c)(1)(ii)](https://www.ecfr.gov/current/title-26/section-1.937-1) |
| Presence alternative 3 | No more than 90 days in the United States | In the tax year | [Treas. Reg. 1.937-1(c)(1)(iii)](https://www.ecfr.gov/current/title-26/section-1.937-1) |
| Presence alternative 4 | No more than USD 3,000 of United States earned income | And more days in Puerto Rico than in the United States in the tax year | [Publication 570, Presence Test](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Days outside both Puerto Rico and the United States counted as Puerto Rico days | Up to 30 days | Only if Puerto Rico days already exceed United States days; not used for the 60-day minimum in alternative 2 | [Publication 570, Days of presence in a territory](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Rental home counted as a permanent home | Personal use above the greater of 14 days or 10% of fair-rent days | For the significant connection test | [Publication 570, Permanent home](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Year of moving to Puerto Rico | Not a resident in any of the 3 prior years; no outside tax home or closer connection in the last 183 days of the year; resident for each of the 3 following years | Satisfies the tax home and closer connection tests for the move year | [Publication 570, Year of Moving to a Territory](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Leaving Puerto Rico, part-year residence | Bona fide resident for at least 2 tax years before the year of the move | United States citizen only; resident for the part of the year before the move | [26 U.S.C. 933(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec933.htm) |
| De minimis rule: no Puerto Rico source income | Services in Puerto Rico for 90 days or less and USD 3,000 or less earned | Not a bona fide resident, and not working for a person engaged in business in Puerto Rico | [Publication 570, De minimis exception](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Gain on property held before becoming resident | Not Puerto Rico source | If a United States citizen or resident (not a Puerto Rico resident) in any of the 10 years before the year of sale; an election splits the gain by holding period | [Publication 570, Special Rules for Gains From Dispositions of Certain Property](https://www.irs.gov/pub/irs-pdf/p570.pdf) |
| Form 8898 filing threshold | Worldwide gross income more than USD 75,000 | In the year residence starts or ends; spouse's income not counted; excluded income included | [Form 8898 instructions, Who Must File](https://www.irs.gov/pub/irs-pdf/i8898.pdf) |
| Form 8898 penalty | USD 1,000 | For not filing, or filing incomplete or wrong information, unless reasonable cause | [Form 8898 instructions, Penalty](https://www.irs.gov/pub/irs-pdf/i8898.pdf) |
| Federal filing test, married filing separately | Gross income subject to United States tax of USD 5 or more | After the section 933 exclusion | [Publication 1321 (October 2026), Who Must File](https://www.irs.gov/pub/irs-pdf/p1321.pdf) |

None of these figures is indexed. Publication 570 (2025) is the latest edition on the read date; its tests come from section 937 and Treas. Reg. 1.937-1, which have not changed for 2026.

### Step 1: the presence test

Meet any one of the five alternatives. Count a day in Puerto Rico for any part of a day physically there; a day spent partly in the United States and partly in Puerto Rico is a Puerto Rico day. Days away for qualifying medical treatment (of the person, a parent, spouse or child), during a 14-day period of a declared major disaster or a mandatory evacuation, or serving in the United States as an elected or full-time official of Puerto Rico also count as Puerto Rico days; keep the documents the IRS can ask for within 30 days. Days in the United States as a student, at a charitable sports event, for medical treatment, in transit of less than 24 hours, or kept away by a disaster, are not United States days. [Publication 570, Days of Presence](https://www.irs.gov/pub/irs-pdf/p570.pdf).

A significant connection to the United States means a permanent home there, current voter registration anywhere in the United States, or a spouse or child under 18 whose main home is there (other than a child there as a student or living with a divorced or separated parent). [Treas. Reg. 1.937-1(c)(5)](https://www.ecfr.gov/current/title-26/section-1.937-1); [Publication 570, Significant Connection](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 2: the tax home test

There must be no tax home outside Puerto Rico at any time in the year. The tax home is the regular or main place of business, employment or post of duty, wherever the family home is; with no main place of business it is where the person regularly lives; an itinerant's tax home is wherever they work. Days in the United States as a student or as a Puerto Rico official are ignored, and a seafarer on a vessel used mainly in local and international waters is not treated as having an outside tax home for that reason alone. [Publication 570, Tax Home](https://www.irs.gov/pub/irs-pdf/p570.pdf); [26 U.S.C. 937(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec937.htm).

### Step 3: the closer connection test

At no time in the year may the person have a closer connection to the United States or a foreign country than to Puerto Rico. Compare the Puerto Rico ties with the total of United States and foreign ties: permanent home, family, belongings (cars, furniture, clothing, jewellery), social, political, cultural, professional and religious memberships, routine banking, business activity, driver's licence, voting, charities supported, the residence named on forms, and forms filed (such as Form W-8BEN or W-9). Spending 183 days in Puerto Rico does not cure a failed closer connection test. Publication 570's own example: a founder who moved to Puerto Rico in 2025 while spouse, children, mail, banking, licence and voter registration stayed in California was not a bona fide resident. [Publication 570, Closer Connection](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 4: the year of a move

- **Moving in (2026 arrival):** the tax home and closer connection tests are met for 2026 if the person was not a bona fide resident in any of 2023 to 2025, had no outside tax home or closer connection in the last 183 days of 2026, and is a bona fide resident in each of 2027 to 2029. They must still meet a presence alternative for 2026. Whether 2026 then qualifies is known only later; plan the 2026 return and the Form 8898 on that basis.
- **Leaving Puerto Rico (United States citizen):** if bona fide resident for at least the 2 tax years before the year of the move, the person is a bona fide resident for the part of the year before the move, and Puerto Rico source income for that part is excluded under section 933(2) (again not United States Government pay). Publication 570's example: resident all of 2023 and 2024, moved to Nevada on 5 May 2025, resident from 1 January to 4 May 2025. The rest of the year is not covered. [26 U.S.C. 933(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec933.htm); [Publication 570, Puerto Rico under Year of Moving From a Territory](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 5: source each item of income

| Item | Where it is sourced |
| --- | --- |
| Wages, fees and self-employment income for services | Where the work is performed; split by days worked (time basis) when work is done in both places |
| Housing and education fringe benefits of an employee working in both places | Geographical basis |
| Social security benefits | United States source |
| Pension | Contributions: where the work was done; earnings: where the pension trust is |
| Interest | Residence of the payer |
| Dividends | Where the corporation was created or organized |
| Rents and gains on real property | Location of the property |
| Gains on personal property | Seller's tax home, subject to the pre-residence gain rule in the table above |
| Royalties | Natural resources: location; patents and copyrights: where used |
| Inventory | Purchased: where sold; produced: allocated under Treas. Reg. 1.863-3 |
| Military pay on active duty | The member's state of legal residence: Puerto Rico source for a bona fide resident even when served elsewhere |

Sources: [Publication 570, Table 2-1 and Compensation for Labor or Personal Services](https://www.irs.gov/pub/irs-pdf/p570.pdf); [Publication 1321, Source of Income](https://www.irs.gov/pub/irs-pdf/p1321.pdf). Income treated as United States source, or effectively connected with a United States business, is never Puerto Rico source. [26 U.S.C. 937(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec937.htm).

Where the customer or employer is does not decide the source of services performed in Puerto Rico, and paying mainland work into a Puerto Rico bank account does not make it Puerto Rico source. A self-employed person uses the basis that most correctly reflects the facts, usually days worked. [Publication 570, Time basis](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 6: apply section 933

For a person who is a bona fide resident for the **entire** year, Puerto Rico source income is excluded from federal gross income, except amounts received for services as an employee of the United States or any of its agencies. No deduction or credit allocable to the excluded income is allowed. [26 U.S.C. 933(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec933.htm).

### Step 7: which returns

| Person | Puerto Rico return | Federal return |
| --- | --- | --- |
| United States citizen or resident alien, bona fide resident | Worldwide income, with a credit for United States income tax on United States source income | Form 1040 on worldwide income less excluded Puerto Rico income, only if the step 8 filing test is met; none if all income is Puerto Rico source |
| Same, with self-employment income and no Form 1040 needed | As above | Form 1040-SS (see `pr-self-employment-tax`) |
| Bona fide resident who is a nonresident alien of the United States | Worldwide income | Form 1040 or 1040-SR on income other than Puerto Rico source (United States Government pay included), treated as a nonresident alien for everything else: no standard deduction, no joint return |
| United States citizen or resident alien, not a bona fide resident | Puerto Rico source income only (including wages for work in Puerto Rico) | Form 1040 on worldwide income, with a foreign tax credit for Puerto Rico tax on income not exempt from United States tax |
| Nonresident alien, not a bona fide resident | Puerto Rico source income only | Form 1040-NR |

Source: [Publication 570, Which Returns To File](https://www.irs.gov/pub/irs-pdf/p570.pdf). Income from a third country is foreign source under both systems and may also need a return there; a foreign tax credit is generally available on one of the returns.

**United States Government employees.** Wages and cost-of-living allowances paid by the United States Government for work in Puerto Rico are Puerto Rico source and taxed by Puerto Rico, and the wages are also taxed by the United States because section 933 excepts them. The cost-of-living allowances are excludable from United States gross income and, up to that amount, from Puerto Rico gross income if the evidence is attached to the Puerto Rico return. A foreign tax credit relieves the double tax. [Publication 570, Special Rules for Puerto Rico](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 8: the federal filing test after the exclusion

The standard deduction is apportioned before the filing test. Multiply the standard deduction for the filing status (2026 amounts in `us-2026-federal-tax-changes`; the Publication 1321 worksheet prints them) by gross income subject to United States tax over total gross income from all sources, including excluded Puerto Rico income. File Form 1040 if gross income subject to United States tax is equal to or more than that result; married filing separately files at USD 5. Enter the same apportioned amount on Form 1040 line 12e with the words "Standard Deduction modified due to excluded income under section 933." [Publication 1321 (October 2026)](https://www.irs.gov/pub/irs-pdf/p1321.pdf).

### Step 9: deductions and credits on the federal return

- Itemized deductions not tied to one income item (medical, real estate tax, mortgage interest) are allowed in the ratio of income subject to United States tax over income from all sources; charitable gifts follow Treas. Reg. 1.861-8(e)(12)(i). [Publication 1321, Itemized Deductions](https://www.irs.gov/pub/irs-pdf/p1321.pdf).
- No qualified business income deduction on excluded Puerto Rico self-employment income, and no deduction for half of self-employment tax on excluded self-employment income. [Publication 1321, Qualified Business Income Deduction](https://www.irs.gov/pub/irs-pdf/p1321.pdf).
- Excluded income counts in modified AGI for income limits on credits and the Schedule 1-A deductions (tips, overtime, seniors); the car loan interest deduction is apportioned. [Publication 1321, New Deductions](https://www.irs.gov/pub/irs-pdf/p1321.pdf).
- No earned income credit for a household in Puerto Rico. The refundable part of the American opportunity credit is paid by the Puerto Rico Treasury. [Publication 1321, Credits](https://www.irs.gov/pub/irs-pdf/p1321.pdf).
- Foreign tax credit: reduce Puerto Rico tax by the part allocable to excluded income (excluded income less its expenses, over all income taxed by Puerto Rico less its expenses), entered on Form 1116 Part III line 12. [Publication 1321, Foreign Tax Credit](https://www.irs.gov/pub/irs-pdf/p1321.pdf).
- Net investment income tax can apply when modified AGI from non-Puerto Rico sources exceeds the threshold; a bona fide resident who owes it files Form 1040 with Form 8960. [Publication 570, Net Investment Income Tax](https://www.irs.gov/pub/irs-pdf/p570.pdf).

### Step 10: Form 8898

Section 937(c) requires notice when a person takes the position that bona fide residence began or ended. File Form 8898 for the year in which worldwide gross income is more than USD 75,000 and the person (a) claims to have become a bona fide resident after a year filed as a United States citizen or resident but not as a resident, (b) claims to have stopped being a bona fide resident after a year filed as a resident, or (c) claims to have become a resident of Puerto Rico after a year required to file as a resident of the CNMI, Guam or the USVI. Worldwide gross income is all income before deductions, including excluded income and foreign income; the threshold is more than USD 75,000, not USD 75,000 or more. Each spouse files their own form. [26 U.S.C. 937(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec937.htm); [Form 8898 instructions](https://www.irs.gov/pub/irs-pdf/i8898.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| A Puerto Rico address, voter card, Hacienda registration or Act 60 decree | Does not by itself meet any federal test; run steps 1 to 3 |
| 183 days in Puerto Rico but family and home in the United States | Presence met; closer connection probably fails; not a bona fide resident |
| More than 90 days in the United States | Still possible under alternative 1, 2, 4 or 5 |
| Retired couple, 160 days in Puerto Rico plus a long trip abroad | Up to 30 trip days count as Puerto Rico days if Puerto Rico days already exceed United States days |
| Arrived mid-2026 | Full-year section 933(1) applies only if the year-of-move rule makes the person resident for the whole year; otherwise only the part-year rules apply and the result depends on later years |
| Left mid-2026 after at least 2 full years of residence | Section 933(2) excludes Puerto Rico source income earned before the move; the rest of the year is federally taxed |
| United States Government civilian or military employee | Federal tax on the government pay; foreign tax credit for Puerto Rico tax on it |
| Active-duty member whose legal residence is Puerto Rico | Military pay is Puerto Rico source wherever served; still taxed federally as government pay |
| Civilian spouse under the Military Spouses Residency Relief Act | May keep the prior tax residence; service income is then sourced there |
| Shares bought while living in the United States, sold after the move | Gain is not Puerto Rico source, unless the special election splits it by holding period |
| Self-employed with clients only on the mainland, all work done in Puerto Rico | Puerto Rico source; excluded from federal income tax; federal self-employment tax still applies |
| Remote employee working some days on the mainland | Time-basis split; the mainland days are United States source and can trigger a Form 1040 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Day counts | Do not conclude residence; ask for a dated calendar |
| Where the work was done each day | Treat days without evidence as not Puerto Rico days |
| Whether the client will stay 3 more years (arrival year) | Prepare both outcomes; flag the year-of-move dependency |
| Worldwide gross income | Assume Form 8898 is needed in a move year |
| Purchase date and value at move of investments | Do not treat the gain as Puerto Rico source |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Spouse or children under 18 live on the mainland | Significant connection and closer connection both at risk |
| Mainland home kept and used | Permanent home in the United States |
| Still registered to vote on the mainland | Significant connection |
| Move year with income above USD 75,000 and no Form 8898 | USD 1,000 penalty |
| Large gain soon after arrival | Pre-residence gain rule |
| Employer payroll on the mainland with no day log | Source of wages cannot be shown |

## Worked cases

**Case 1, a decision: must a couple file Form 1040?** Publication 1321's own 2026 example. A married couple, both under 65, are United States citizens and bona fide residents of Puerto Rico for all of 2026. They received USD 15,000 of Puerto Rico source income excluded under section 933, USD 20,000 of federal wages and USD 6,000 of interest from a United States bank. They do not itemize. Gross income subject to United States tax is USD 26,000; gross income from all sources is USD 41,000. The 2026 joint standard deduction in the worksheet is USD 32,200. The ratio is 0.6341, so the allowable standard deduction is USD 20,418.02, entered as USD 20,418. Because USD 26,000 is more than USD 20,418, they must file Form 1040 (the unapportioned USD 32,200 would wrongly suggest no filing). If the USD 20,000 had been Puerto Rico source private wages instead, gross income subject to United States tax would be USD 6,000, the ratio 0.1463 and the allowance USD 4,710.86: they would still have to file, because USD 6,000 is more than that.

```oa-check
name: Publication 1321 apportioned standard deduction, joint (2026)
inputs:
  us_taxable_gross: 26000
  pr_excluded: 15000
  std_deduction_joint: 32200
  alt_us_taxable_gross: 6000
steps:
  - total_gross: us_taxable_gross + pr_excluded
  - ratio: round(us_taxable_gross / total_gross, 4)
  - allowed: std_deduction_joint * ratio
  - must_file_margin: us_taxable_gross - allowed
  - alt_ratio: round(alt_us_taxable_gross / (alt_us_taxable_gross + 35000), 4)
  - alt_allowed: std_deduction_joint * alt_ratio
  - alt_margin: alt_us_taxable_gross - alt_allowed
expected:
  total_gross: 41000
  ratio: 0.6341
  allowed: 20418.02
  must_file_margin: 5581.98
  alt_ratio: 0.1463
  alt_allowed: 4710.86
  alt_margin: 1289.14
```

**Case 2, a decision: does a remote employee become a Form 1040 filer?** A single United States citizen is a bona fide resident of Puerto Rico for all of 2026 (250 days in Puerto Rico, 70 in the United States, home and family in Puerto Rico). She is paid USD 80,000 by a mainland employer and has no other income. She worked 180 days in Puerto Rico and 60 days in the employer's New York office. On a time basis, USD 60,000 is Puerto Rico source (180 over 240 days) and excluded; USD 20,000 is United States source. The apportioned standard deduction (2026 single USD 16,100 from the Publication 1321 worksheet) is USD 16,100 times 20,000 over 80,000, which is USD 4,025. USD 20,000 is more than USD 4,025, so she must file Form 1040 and report the USD 20,000. Had all 240 work days been in Puerto Rico, all USD 80,000 would be excluded and no Form 1040 would be required.

```oa-check
name: Time-basis source and filing test, single remote employee (2026)
inputs:
  pay: 80000
  pr_days: 180
  us_days: 60
  std_deduction_single: 16100
steps:
  - pr_source: pay * pr_days / (pr_days + us_days)
  - us_source: pay - pr_source
  - allowed: std_deduction_single * us_source / pay
  - must_file_margin: us_source - allowed
expected:
  pr_source: 60000
  us_source: 20000
  allowed: 4025
  must_file_margin: 15975
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PRF-NRA | Nonresident alien of the United States | Apply the substantial presence test of Publication 519 as adapted in Publication 570; refer for the Form 1040 or 1040-NR position |
| R-PRF-MIL | Armed Forces member or spouse with mixed legal residence | Refer: military sourcing and the Military Spouses Residency Relief Act need the orders and prior residence |
| R-PRF-GAIN | Sale of investments held before the move, or the holding-period election | Refer: Treas. Reg. 1.937-2(f) and (k) computation not done here |
| R-PRF-INVENTORY | Inventory produced in one place and sold in the other | Refer: Treas. Reg. 1.863-3 allocation |
| R-PRF-DOUBLE | The IRS and Hacienda tax the same income | Refer: competent authority request under Rev. Proc. 2006-23 |
| R-PRF-DECREE | The question is the Act 60 decree itself | Use `pr-act-60-incentives` |

## Filing and payment

- **Puerto Rico return** for calendar 2026: to Hacienda by 15 April 2027 (see `pr-individual-income-tax`).
- **Form 1040** for 2026, if step 8 requires it: due 15 April 2027; an automatic 6-month extension with Form 4868 to 15 October 2027 extends filing, not payment. The 2-month automatic extension for people living outside the United States **and Puerto Rico** does not apply to a person living in Puerto Rico. Mail without payment to Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215, USA; with payment to Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303, USA. [Publication 570, When To File and Where to file](https://www.irs.gov/pub/irs-pdf/p570.pdf).
- **Form 1040-SS**, if only self-employment tax is owed: see `pr-self-employment-tax`.
- **Form 8898**: mail separately from the return, by the due date of Form 1040 including extensions, to Internal Revenue Service, 3651 S. IH 35, MS 4301 AUSC, Austin, TX 78741. Do not attach it to the return. [Form 8898 instructions, When and Where To File](https://www.irs.gov/pub/irs-pdf/i8898.pdf).
- **Estimated tax** to the IRS on Form 1040-ES if federal income tax, self-employment tax, Additional Medicare Tax or net investment income tax will be owed (see `us-quarterly-estimated-tax`).

## Completion checklist

- Day calendar for 2024 to 2026 with the special-day categories marked.
- Presence alternative named, tax home located, closer connection factors listed.
- Move-year rule applied, with the 3-year look-back and look-forward recorded.
- Each income item sourced on its own rule, with the time-basis computation for services.
- United States Government pay separated.
- Federal filing test run with the apportioned standard deduction.
- Form 8898 decided against the more-than-USD-75,000 test in any move year.
- Evidence kept: travel calendar, work-location records, home and family facts, main business location, income-by-source schedule, prior returns.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 933 (govinfo, U.S. Code 2024 edition). Read for (1) the full-year exclusion and the United States Government employee exception, and (2) the 2-year departure rule. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec933.htm | 2026-11-14 |
| 26 U.S.C. 937 (govinfo). Read for (a) the 183-day, tax home and closer connection tests, (b) the source rules and (c) the reporting requirement. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartD-sec937.htm | 2026-11-14 |
| Treas. Reg. 1.937-1 (eCFR, read through the eCFR renderer). Read for (c)(1)(i) to (v) the five presence alternatives and (c)(5) significant connection. | https://www.ecfr.gov/current/title-26/section-1.937-1 | 2026-11-14 |
| IRS Publication 570 (2025). Read for chapter 1 (presence test, day counting, significant connection, tax home, closer connection, year of move, Form 8898), chapter 2 (Table 2-1, time basis, de minimis, gains), chapter 3 (Puerto Rico returns, government employees, military) and chapter 4 (when to file, extensions, net investment income tax). | https://www.irs.gov/pub/irs-pdf/p570.pdf | 2026-11-14 |
| IRS Publication 1321 (October 2026). Read for who must file, the standard deduction worksheet and its 2026 example, the source table, deduction and credit rules and Form 8898. | https://www.irs.gov/pub/irs-pdf/p1321.pdf | 2026-11-14 |
| Instructions for Form 8898 (Rev. October 2024). Read for who must file (more than USD 75,000), when and where to file and the USD 1,000 penalty. | https://www.irs.gov/pub/irs-pdf/i8898.pdf | 2026-11-14 |

Not yet confirmed: Publication 570 for 2026 returns was not published on the read date, so the 2025 edition is used for rules that come from section 937 and Treas. Reg. 1.937-1; the 2026 standard deduction amounts are taken from the Publication 1321 worksheet and owned by `us-2026-federal-tax-changes`; the Puerto Rico side of the United States Government cost-of-living allowance exclusion was not read in the Puerto Rico Code.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pr-federal-residence-and-filing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pr-federal-residence-and-filing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
