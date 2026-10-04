---
name: malta-ssc
description: Use this skill whenever asked about Malta Social Security Contributions (SSC) for self-employed or self-occupied individuals. Trigger on phrases like "how much SSC do I pay", "Class 2 contributions", "social security self-employed", "SSC calculation", "SSC arrears", "do I need to pay SSC", "SSC and income tax", "DSS payment", "Class 2 quarterly debit", or any question about Malta SSC obligations for a self-employed client. Also trigger when classifying bank statement transactions that relate to DSS debits, SSC direct debits, or government social security payments from BOV, HSBC, or other Maltese banks. Also trigger when preparing a TA24 income tax return where SSC deductibility (Box 20) is relevant. This skill covers Class 2 rates, min/max caps, payment schedule, registration, penalties, interaction with income tax, TA22 part-time regime, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any SSC-related work.
version: 2.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta social security contributions: Class 2 (self-employed and self-occupied), Class 1 and the Maternity Leave Fund

## Scope ([Social Security Act, Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

This Guide covers Malta social security contributions under the Social Security Act (Cap. 318):

- **Class 2**, paid by self-occupied and self-employed people. This is the main subject.
- **Class 1**, paid by employees and their employers, and the employer-only **Maternity Leave Fund** contribution. These are summarised only. For payroll mechanics (basic weekly wage, FSS, FS5/FS3/FS7), use the malta-payroll Guide.

**Year.** This Guide is for tax year 2026 (contribution year 2026). Contributions run by *contribution year*, which "means the period starting from the first Monday in January and ending on the last Sunday before the first Monday in January of the following year" (article 2). The primary year here is contribution year 2026: Monday 5 January 2026 to Sunday 3 January 2027, which is 52 weeks. A Class 2 category is fixed on net earnings or income of "the calendar year immediately preceding the contribution year" (Tenth Schedule). So 2026 Class 2 turns on 2025 earnings.

**Sources.** Everything here comes from the Laws of Malta (legislation.mt). The MTCA website (mtca.gov.mt), which now administers contribution collection, refused our automated source checks on 25 September 2026. Anything that exists only there is marked **check**, with no figure.

**The figures problem.** The rate table in the law (the Tenth Schedule) on legislation.mt is the one substituted by [L.N. 10 of 2025](https://legislation.mt/getpdf/67a08f18b52f3e3cf8949c52), which "shall be deemed to have come into force on 1st January 2024". Its notes refer to pensionable income that "with effect from January 2024 is guaranteed at the amount of €27,679.09". These are **2024 figures**. We found no legal notice updating the table for 2025 or 2026, and [Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430) does not amend it. The weekly amounts rise each year in practice, so the **2025 and 2026 weekly minimum, maximum and band limits are check**: take them from MTCA's published Class 2 and Class 1 tables. The 15% and 10% rates, the categories and the rules below are current law.

**Not covered:** income tax, including whether and where contributions go on the tax return (see the malta-income-tax Guide); payroll withholding and FS forms (see malta-payroll); entitlement to benefits and pensions; cross-border cases under EU coordination rules or bilateral agreements (A1 certificates).

## Ask the client first

- **Date of birth.** On or before 31 December 1961, or on or after 1 January 1962? It sets the maximum (SC) and the top of the 15% band ([Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c)). Do not compute without it.
- **Age.** Under 65? The Act defines a self-employed person as one who "has not yet passed his sixty-fifth birthday". Over pension age, ask whether they still work and whether they draw a pension.
- **What they do.** A trade, business or profession producing earnings (self-occupied), or only passive income such as rent or investments (self-employed, not self-occupied)?
- **Net earnings or income for the previous calendar year** (2025 for 2026), taken net of expenses directly incurred. Is the 2025 income tax return filed?
- **Employment.** Are they also employed, full-time or part-time? Is the employer paying Class 1?
- **Status.** Married (and not legally separated or abandoned), single, full-time student, pensioner, part-time self-occupied woman, full-time farmer or breeder?
- **First year?** When did the self-occupation start, and was the person self-occupied before (a returner)?
- **Arrears.** Any unpaid or underpaid Class 2 from earlier years? Get the MTCA statement.
- **Special work.** Outworker, tourist guide, driver of a Government impressed vehicle, host family, homeworker?

## The method, step by step

1. **Classify the person** ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c), articles 2, 3 and 6). Every person who has passed their sixteenth birthday but not reached retirement is insured "either as an employed person, or as a self-employed person or as a self-occupied person" (article 3(1)). A person is **self-occupied** if engaged "in any activity through which earnings exceeding €910 per annum are being derived". A **self-employed person** is ordinarily resident in Malta, under 65, and neither employed nor self-occupied (for example, living on rents or investments).
2. **Check the exclusions and exemptions first** (articles 3(2), 6 and 12; see the boundary table). Some people owe nothing, or can apply for a low-income certificate.
3. **Measure the base.** For a self-occupied person, use *earnings*: income "from any economic activity ... net of expenses directly incurred", excluding bank interest, investment income, rents and ground rents, income not directly related to the activity, and the spouse's income (article 2). For a self-employed person, use *net income*: "total income net of expenses directly incurred in generating that income". In both cases exclude "Maternity Benefit, Children's Allowance and any ex-gratia Benefit payable under article 88" (Tenth Schedule).
4. **Use the previous calendar year.** The category for contribution year 2026 depends on 2025 net earnings or income.
5. **Pick the category** from the [Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c) table for the year (Part II for self-employed, Part III for self-occupied): SA flat minimum, SB 15% band, or SC flat maximum, with the maximum set by date of birth. For 2026 use MTCA's table (check).
6. **Compute the weekly amount** ([Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c)). In the SB band it is "the weekly equivalent of 15% of their annual net earnings calculated to the nearest cent": 15% of the annual figure divided by the weeks in the year (52 for 2026).
7. **Schedule payment** four-monthly, in arrears, for the periods ending on the last day of April, August and December, at MTCA (article 11).
8. **Deal with late or wrong payments** under article 116: interest from 1 January 2026, and the five-year window for the person's own requests.

## Class 2 figures, with years ([Cap. 318, Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

**Rates that do not change by year.** Class 2 in the SB band is 15% of the previous year's net earnings or income, as a weekly equivalent. The Government adds a contribution "equivalent to 50% of the contribution paid by the self-employed or self-occupied person" out of the Consolidated Fund (article 10(4)). That State share is not paid by the client.

**2026 weekly amounts and band limits: check.** Use MTCA's 2026 Class 2 table. Do not use the 2024 amounts below for 2026 bills.

### Self-occupied persons (Tenth Schedule, Part III): table in force from 1 January 2024 ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

| Category | Who (net earnings in the preceding calendar year) | Weekly contribution (2024 table) |
| --- | --- | --- |
| SA | Earnings "less than €12,028.92" | €34.70 flat. Reduced options below |
| SB, born 31 Dec 1961 or before | Earnings over €12,028.93, not over €22,000 | 15% of annual net earnings, weekly equivalent to the nearest cent |
| SB, born 1 Jan 1962 or after | Earnings over €12,028.93, not over "€27,678.08" (as printed) | 15% of annual net earnings, weekly equivalent |
| SC, born 31 Dec 1961 or before | Earnings over €22,000.01 | €63.46 flat |
| SC, born 1 Jan 1962 or after | Earnings over €27,679.09 | €79.84 flat |

Reduced SA options in Part III:

- A **part-time self-occupied woman**, a **full-time student** who is part-time self-occupied, or a **pensioner** who is part-time self-occupied, with earnings not over €12,028.92, may pay "15% of the annual net earnings" instead of the SA flat amount. Paying "less than €34.70 per week" may "result in the payment of a reduced contributory benefit or contributory pension" (Note 1).
- A **full-time farmer or breeder** pays €23.13 in SA, "10% of the annual net earning" in SB, and in SC €42.31 (born 1961 or before) or €53.23 (born 1962 or after).

### Self-employed persons, not self-occupied (Tenth Schedule, Part II): table in force from 1 January 2024 ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

| Category | Who (net income in the preceding calendar year) | Weekly contribution (2024 table) |
| --- | --- | --- |
| SP | Income that "Exceeds € 1,005 but does not exceed €10,567.92" (single persons who are not self-occupied only) | €30.48 |
| SA | Income "less than €12,028.92" | €34.70 |
| SB | Same bands as self-occupied (pre-1962 top €22,000.00; post-1962 top €27,679.08) | 15% weekly equivalent |
| SC | Over €22,000.01 (born 1961 or before) / over €27,679.09 (born 1962 or after) | €63.46 / €79.84 |

**How the flat amounts fit the 15% rule.** On the 2024 table the flat amounts are the 15% weekly equivalent at the band edges: €12,028.92 × 15% ÷ 52 = €34.70, €22,000 × 15% ÷ 52 = €63.46, and €27,679.09 × 15% ÷ 52 = €79.84. So the SC maximum is reached when earnings exceed the pensionable income ceiling for the person's birth cohort.

**Drafting slips in the 2024 table.** The table says SA is "less than €12,028.92" while SB starts "exceeds €12,028.93", leaving a one-cent gap. Part III prints the post-1962 SB ceiling as "€27,678.08" but Part II prints "€27,679.08". Treat these as typos and follow MTCA's table.

**Annual cost.** The Act sets weekly amounts. An annual figure is the weekly amount times the contribution weeks in the year. 2026 has 52 weeks; some years have 53 (2024 ran from Monday 1 January 2024 to Sunday 5 January 2025). Do not reuse an old annual total.

**Old figures you may see.** Earlier versions of this Guide quoted "2025" weekly amounts and annual totals. We could not find them in the law, so we have removed them. If a client quotes a figure, check it against MTCA's table for that year.

## Class 1 and the Maternity Leave Fund, in summary ([Cap. 318, article 7 and Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

- **Who and how much.** For every person in insurable employment "three contributions per week shall be payable ... one by the employed person, one by his employer, and one out of the Consolidated Fund" (article 7(1)). Employee and employer each pay 10% "calculated to the nearest cent" of the **basic weekly wage**, between a flat low-wage amount and a weekly maximum. The State adds "50% of the combined weekly contributions" (article 7(2)(b)).
- **Base.** The basic weekly wage excludes "overtime, any form of bonus, any extra allowances, any remuneration in kind and commissions" (article 2). With two insurable jobs, the person is treated as employed in the one "which carries the higher or highest basic wage or salary" (article 7(1)).
- **2024 table (Part I), not 2026.** Category A (under 18, basic weekly wage not over €213.54) €6.62 each side. Category B (18 and over, not over €213.54) €21.35 each side, or 10% if part-time and electing. Category C is 10%. Category D, the maximum, is €42.31 each side (born 1961 or before) and €53.23 (born 1962 or after). Categories E and F (students on work-study schemes) cap at €4.38 and €7.94. Part I prints the Category C and D boundary inconsistently ("€423.07", "€523.28", "€532.29", "€515.99"). **2026 weekly figures: check** on MTCA's Class 1 table. The malta-payroll Guide carries the detail.
- **Low earners.** An employee whose basic weekly earnings are below the national minimum wage for age 18 and over may elect 10% of actual pay instead of Category B. Since 1 January 2018 this applies "only ... to part-time employees whose weekly basic earnings from such part-time employment do not exceed the National Minimum Wage". A person with more than one part-time job and no full-time job may, from 1 January 2022, elect to pay on all part-time jobs up to "forty (40) hours" a week (article 7(2)(a)).
- **Employer's share stays with the employer.** An employer who deducts its own share from pay "shall be guilty of an offence" (article 8(2)).
- **Maternity Leave Fund (Part IV), employer only.** The employer pays 0.3% "calculated to the nearest cent" of the basic weekly wage. The 2024 table sets €0.20 (Category A), €0.64 (Category B), and a cap of €1.27 (born 1961 or before) or €1.60 (born 1962 or after); E and F cap at €0.13 and €0.24. 2026 amounts: check. Nothing is deducted from the employee, and it never applies to Class 2.

## Boundary and exception table ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

| Situation | Treatment | Law |
| --- | --- | --- |
| Activity earnings of €910 a year or less | Not self-occupied. May still be a self-employed person liable on other income, unless an exclusion below applies | art. 2 |
| Self-employed (not self-occupied), yearly means not over €1,005 (or €1,470 if married and wholly maintaining a spouse who is not self-occupied or employed) | Can apply for a "certificate of low income valid for twelve months" and is then exempt. May instead opt to pay SP (single) or SA (married). Not renewing within three months of expiry can make SP or SA payable | art. 12(1), (3) |
| Married, not legally separated or abandoned, not self-occupied | "shall not be deemed to be a self-employed person" from 5 January 2004, unless they elected to continue under the proviso | art. 3(2) |
| Full-time student at a recognised institution | Not self-employed or self-occupied, unless paid as a self-occupied person. Then the student SA option (15%) may apply | art. 6(1)(b), 6(2); Tenth Schedule Part III |
| Person receiving a pension under the Act "(other than an Injury Pension)" who is not gainfully occupied, or person receiving Social Assistance | Not self-employed or self-occupied | art. 6(1)(d), (f) |
| Past the 65th birthday | Outside the definitions of employed and self-employed person. Confirm with MTCA how the year of the birthday is handled (check) | art. 2 |
| Full-time employee who also has part-time self-occupied earnings | In practice Class 1 through the employer and no Class 2 on the side activity (check on mtca.gov.mt; the Act does not state this rule in terms) | art. 7; art. 14 |
| Liable to Class 1 and also self-occupied, wants Class 2 instead | Allowed only with approval, and only while the Class 2 rate "exceeds the aggregate applicable rate of Class One" (employer plus employee). Cannot switch back until self-occupation ends | art. 14 |
| Resident in Malta, employed abroad in non-insurable employment | May pay Class 1 instead of Class 2, on the Class 2 payment timetable; the foreign employer pays nothing | art. 13 |
| Earnings from acting as a host family | Elective exemption from Class 2 on those earnings | art. 12(4) |
| Self-occupied homeworker whose net earnings do not exceed 50% of the 18+ national minimum wage | Elective exemption | art. 12(5) |
| Outworker, tourist guide, driver of a Government impressed vehicle | Entitled to an extra amount equal to "1/16 of the remuneration" from the engager (or Government) towards Class 2 | art. 15(1) |
| Over 45, not gainfully occupied for five consecutive years, obtains a trading licence | Government pays the contributions on that self-occupation "for the first 52 weeks" | art. 15(7) |
| Aged 59 up to 65 and working or self-occupied; or aged 59 or over and receiving an Invalidity Pension, Carers Allowance, Increased Carers Allowance or Carers Grant; or aged 59 up to 65, not working, where paying brings them to "a minimum of ten (10) years paid contributions" for a pension | May pay "up to five years of arrears" at the SA rate of the year of the claim | art. 116(5) provisos |
| Abroad or in hospital when a Class 2 payment fell due | Deadline extends to "the 31st day of his return to Malta or discharge from hospital" | art. 116(1) proviso |

## Worked cases ([Cap. 318, Tenth Schedule](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

These use the 2024 table because it is the only one in the law we could read. For a 2026 bill, swap in MTCA's 2026 amounts (check). The 15% steps are current law.

**Case 1: SB band.** Self-occupied web developer, born 1990, 2025 net earnings €20,000. €20,000 sits inside the SB band on the 2024 table (confirm on the 2026 table). Annual base: €20,000 × 15% = **€3,000**. Weekly equivalent to the nearest cent: €3,000 ÷ 52 = **€57.69**. Over the 52 weeks of 2026 that is €2,999.88. It is paid four-monthly in arrears on MTCA's bills.

**Case 2: SC maximum, born 1962 or later.** Self-occupied, born 1975, 2025 net earnings €60,000. This exceeds the post-1962 ceiling, so SC applies. On the 2024 table the weekly amount is **€79.84**. The 2026 amount is check. Income above the ceiling adds nothing.

**Case 3: SC maximum, born 1961 or earlier, turning 65.** Self-occupied, born 20 June 1961, 2025 net earnings €60,000. The pre-1962 maximum applies: **€63.46** a week on the 2024 table. The client passes their 65th birthday in June 2026 and then falls outside the definition of a self-employed person. Ask MTCA how contributions for the rest of 2026 are handled (check), and refer any pension question.

**Case 4: SA minimum, and the part-time election.** Self-occupied, born 1990, 2025 net earnings €8,000. Below the SA limit, so the flat SA applies: **€34.70** a week on the 2024 table. If she is a part-time self-occupied woman (or a student or pensioner who is part-time self-occupied), she may pay 15% instead: €8,000 × 15% ÷ 52 = **€23.08** a week. Warn her that paying less than the SA amount may reduce contributory benefits and pension (Tenth Schedule, Part III, Note 1).

**Case 5: Passive income only.** Single, born 1985, not employed and not self-occupied, 2025 net rental income €9,000. This is a self-employed person. €9,000 is within the SP band (over €1,005, not over €10,567.92), so SP applies: **€30.48** a week on the 2024 table. If the same person were married and not separated, article 3(2) says they are not deemed self-employed, so no Class 2 is due. If their means were €900, they could apply for a low-income certificate (limit €1,005) and pay nothing while it lasts.

**Case 6: Late payment in 2026.** €500 of Class 2 due in 2026 is paid three months late. From 1 January 2026, article 116 charges interest per month at the rate in ITMA article 44(2A). That article sets 0.6% "for every month or part thereof", unless the Minister prescribes another rate. On that basis: €500 × 0.6% × 3 = **€9.00**. Confirm the rate applied on the MTCA statement (check).

## When to refuse or refer

- **Refuse to compute without the date of birth.** The maximum and the top of the SB band depend on it.
- **Refuse to give a 2025 or 2026 weekly amount, band limit or annual total from this Guide.** Those figures must come from MTCA's current Class 2 and Class 1 tables. The 2024 table is shown for method only.
- **Refer arrears and late charges.** Do not quantify unpaid contributions, interest or older-period additions without an official statement of what is due. Under article 116(4), "a notice by the Director ... showing the number and the amount of contributions" unpaid is "sufficient evidence ... unless the contrary is proved". For article 116 the "Director" is the Director General (Social Security), not the Commissioner for Tax and Customs (article 2), even though MTCA collects the payments. Which office issues the statement in practice is check.
- **Refer** disability, invalidity and carer situations, students and pensioners claiming an exclusion, religious-order and Libya-employment arrears provisions, court-ordered transfers of contributions (articles 8(6), 10(5)), and anyone past pension age.
- **Refer** cross-border cases: A1 certificates, EU coordination, bilateral agreements, and non-residents.
- **Flag for a Maltese warranted accountant**: an employee who is also a director drawing fees; a returner restarting self-occupation after years out; a mid-year switch between employment and self-occupation; a first year of self-occupation (see below); two part-time self-occupations with no employment.
- **Route** income tax questions, including how contributions are treated on the return, to the malta-income-tax Guide, and payroll mechanics to malta-payroll.

## Filing and payment ([Cap. 318, articles 11 and 116](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

**Who collects.** Class 2 is paid "at the Malta Tax and Customs Administration in such form and manner as may from time to time be determined by the Director" (article 11, as amended by [Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430), article 22). For articles 3 to 11 the "Director" is the Commissioner for Tax and Customs. Older bank statements may show payments to the Department of Social Security or Inland Revenue; newer ones should show MTCA.

**When.** "in arrears at intervals of four months ending on the last day of April, August and December of each year" (article 11), unless the Director has approved other arrangements. So there are three payment periods a year: January to April, May to August, and September to December. The exact due date and amount are on MTCA's bill (check). The rates for each period are those in the Tenth Schedule "for the four months ending on the last day of April, August and December" (article 10(3)). Earlier versions of this Guide said quarterly: that was wrong.

**First year.** The category depends on the previous year's earnings, which a new self-occupied person does not have. How MTCA bills the first year, and how it adjusts once the first income tax return is in, is check. Do not promise the SA minimum as a final figure.

**Adjustments.** The Director can require a person "to produce his income tax returns and/or assessments for the purpose of establishing his net income, or earnings" (article 133). Where a contribution was paid in the wrong class, category or rate, the difference can be claimed.

**Late or short payment.** Article 116(1) charges a further contribution on Class 2 not paid in time: 10% for periods before 3 July 1989, 5% up to 2 January 2000, and 1% per month after that. "as from 1st January 2026" the 1% per month charges are "substituted by interest per month as provided for in article 44(2A) of the Income Tax Management Act". [ITMA article 44(2A)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b) sets 0.6% "for every month or part thereof" or another rate the Minister prescribes. People born on or after 1 January 1962 also pay that interest on arrears settled under article 116(5). If dues and the further contribution are not settled within three months, the Director may serve a judicial letter that becomes an executive title after ten days unless challenged (article 116(2)). Unpaid Class 2 is a privileged claim over the person's estate (article 116(3)).

**Time limits.** The Director's claim for unpaid Class 2, or for a difference in rate, category or class, "shall be barred by the lapse of thirty years" (article 116(5)(i)). The person's own request to pay missed contributions, or to get a refund after an adjustment, is "null and void if submitted after attainment of pension age or after the lapse of five years from the time when the proper rate of contribution was due, whichever is the earlier" (article 116(5)(ii)). The old statement that the Department "can recover up to 5 years" was wrong.

**Reading bank statements.** Class 2 payments are statutory personal contributions: keep them out of VAT and out of business supplies. Payments go out; a credit from the Department (for example a pension or benefit) is income received, not a contribution. MTCA also collects income tax, provisional tax and FSS remittances, so a debit to MTCA (or to the Commissioner, Inland Revenue or CFR on older statements) is Class 2 only if its payment reference or the MTCA statement says so. A provisional tax payment is income tax, not a contribution: route it to the malta-income-tax Guide. Keep Class 1 paid by an employer (through the FSS remittance) separate from the client's own Class 2. An irregular lump sum marked as arrears may mix contributions and interest: get the MTCA breakdown before recording it.

## 2025 contribution year (settling now) ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

Contribution year 2025 ran from Monday 6 January 2025 to Sunday 4 January 2026. Its category turned on 2024 net earnings or income. Its bills, and any late interest, fall under the rules above; late charges for periods up to 31 December 2025 were 1% per month, and from 1 January 2026 interest applies (the transition for a debt spanning both periods is check). The 2025 weekly amounts are check on MTCA's 2025 table.

## Completion checklist ([Cap. 318](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c))

- [ ] Date of birth recorded: 31 December 1961 or before, or 1 January 1962 or after; age under 65 confirmed
- [ ] Status fixed: employed, self-occupied (earnings over €910) or self-employed; exclusions in articles 3(2) and 6 checked
- [ ] Low-income certificate, host-family, homeworker or start-up relief considered where relevant
- [ ] Base measured on the previous calendar year, net of directly incurred expenses, excluding interest, rents, spouse's income and the listed benefits
- [ ] Category taken from MTCA's table for the contribution year (2026: check), not from the 2024 table
- [ ] SB weekly amount = 15% of annual net earnings ÷ weeks in the year, to the nearest cent
- [ ] Reduced options (part-time women, students, pensioners, farmers) applied only where they fit, with the benefit warning given
- [ ] Payment periods ending April, August and December; MTCA bill due dates checked
- [ ] Arrears and late interest taken from an MTCA statement, not estimated
- [ ] Class 1 and Maternity Fund questions routed to malta-payroll; income tax treatment routed to malta-income-tax

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
