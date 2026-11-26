---
name: malta-ssc
description: Use this skill whenever asked about Malta Social Security Contributions (SSC) for self-employed or self-occupied individuals in contribution year 2026. Trigger on phrases like how much SSC do I pay, Class 2 contributions, social security self-employed, SSC calculation, SSC arrears, do I need to pay SSC, SSC and income tax, DSS payment, Class 2 debit, or any question about Malta SSC obligations for a self-employed client, including classifying bank statement lines for SSC debits. Covers who is self-occupied (earnings over EUR 910) or self-employed, the exclusions and low-income certificate, the 2026 Class 2 categories SP, SA, SB and SC with the 15% band and the two birth-cohort maxima, reduced options for part-time women, students, pensioners and farmers, four-monthly payment to MTCA, interest on late Class 2 from 1 January 2026, time limits and the first year. Class 1 and the Maternity Leave Fund are in malta-payroll.
version: "3.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Malta social security contributions: Class 2 for the self-occupied and self-employed, 2026

## Scope

This skill covers Class 2 social security contributions under the Social Security Act, Cap. 318, paid by **self-occupied** and **self-employed** people, for **contribution year 2026**. Class 1 (employees and employers) and the employer-only Maternity Leave Fund contribution are in [malta-payroll](malta-payroll.md); this file states only the Class 1 rules that decide which class applies.

**Year.** A contribution year "means the period starting from the first Monday in January and ending on the last Sunday before the first Monday in January of the following year" (art. 2). Contribution year 2026 runs from Monday 5 January 2026 to Sunday 3 January 2027: 52 weeks. A Class 2 category is fixed on net earnings or income of "the calendar year immediately preceding the contribution year" (Tenth Schedule): 2026 Class 2 turns on 2025 earnings.

**Figures.** The weekly amounts for 2026 are MTCA's published 2026 Class 2 table. The consolidated Tenth Schedule retrieved for this read still displays older amounts (its pension-ceiling note refers to 2024); use the schedule for the quoted classification and percentage rules, and MTCA’s expressly dated table for the 2026 amounts and bands. Do not substitute the older schedule amounts for the 2026 table.

**Not covered:** income tax, including how contributions are treated on the return ([malta-income-tax](malta-income-tax.md)); payroll and FS forms ([malta-payroll](malta-payroll.md)); benefits and pensions; cross-border cases (A1 certificates, EU coordination, bilateral agreements).

Built from the law: not yet approved by an accountant.

## Ask the client first

1. **Date of birth.** On or before 31 December 1961, or on or after 1 January 1962? It sets the maximum and the top of the 15% band. Record pension entitlement and whether a pension has been claimed. Article 3 uses “retirement”, which is defined separately in article 2; do not assume that everyone below 65 remains liable.
2. **What they do.** A trade, business or profession producing earnings (self-occupied), or only passive income such as rent or investments (self-employed)?
3. **2025 net earnings or income**, net of expenses directly incurred; is the 2025 return filed? For a low-income certificate, collect the capital, property, trust, income and marital facts needed for the Second Schedule Part I means test.
4. **Employment.** Also employed, full-time or part-time, with the employer paying Class 1?
5. **Status.** Married (not separated or abandoned), single, full-time student (age), pensioner, part-time self-occupied woman, full-time farmer or breeder; outworker, tourist guide, government-impressed vehicle driver, host family, homeworker?
6. **First year or returner, and arrears.** When did self-occupation start? Any unpaid Class 2 (get the MTCA statement)?

## The method, step by step

1. **Classify the person** (arts 2, 3 and 6). Everyone past their sixteenth birthday and below retirement is insured "either as an employed person, or as a self-employed person or as a self-occupied person" (art. 3(1)). **Self-employed**: ordinarily resident in Malta, has not yet passed the sixty-fifth birthday, and neither employed nor self-occupied. **Self-occupied**: the article 2 definition adds activity producing earnings exceeding EUR 910 a year. The insured-person test also requires that retirement has not been reached: for birth years 1959–1961 pension age is 64; if still occupied and not receiving a pension, the retirement definition can defer the date until a pension application or age 65, whichever is earlier. Earlier cohorts and any uncertain retirement date: Check this point with one of our partner accountants. ([Cap. 318 arts 2–3](https://legislation.mt/eli/cap/318/eng/pdf).)
2. **Exclusions and exemptions first** (arts 3(2), 6, 12; boundary table).
3. **Measure the base.** Self-occupied: *earnings*, income "from any economic activity ... net of expenses directly incurred", excluding bank interest, investment income, rents and ground rents, income not related to the activity, and the spouse's income (art. 2). Self-employed: *net income*, "total income net of expenses directly incurred in generating that income". In both, exclude "Maternity Benefit, Children's Allowance and any ex-gratia Benefit payable under article 88" (Tenth Schedule).
4. **Use 2025** for the 2026 category.
5. **Pick the category** from the 2026 table: SP, SA, SB or SC, with the SB ceiling and SC amount set by date of birth.
6. **Weekly amount.** In SB: "the weekly equivalent of 15% of their annual net earnings calculated to the nearest cent", that is 15% of the annual figure divided by the weeks in the year (52 for 2026). For the 2026 reduced farmer rates, MTCA requires a full-time farmer identified by the Department of Agriculture. Breeder eligibility beyond that identification: Check this point with one of our partner accountants.
7. **Payment**: four-monthly in arrears, periods ending on the last day of April, August and December, at MTCA (art. 11).
8. **Late or wrong payments** under art. 116.

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Self-occupied threshold | Earnings exceeding EUR 910 a year | Below it, not self-occupied | Cap. 318 art. 2: https://legislation.mt/eli/cap/318/eng/pdf |
| SP, single and not self-occupied | EUR 31.97 a week | 2025 net income EUR 1,006 to EUR 11,082.72; single persons who are not self-occupied only | MTCA Class 2 rates 2026: https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-2---social-security-contribution-rates/2026 |
| SA | EUR 36.18 a week (farmers EUR 24.12) | 2025 net income or earnings EUR 910 to EUR 12,543.72 | same |
| SA reduced option | 15% of annual net earnings instead of EUR 36.18 | Part-time self-occupied woman, full-time student under 24 who is part-time self-occupied, or part-time self-occupied pensioner, earnings not over EUR 12,543.72; paying less may reduce benefits | same |
| SB, born by 31 December 1961 | 15% weekly equivalent (farmers 10%) | EUR 12,543.73 to EUR 25,499.99 | same |
| SC, born by 31 December 1961 | EUR 73.56 a week (farmers EUR 49.04) | EUR 25,500 and over | same |
| SB, born from 1 January 1962 | 15% weekly equivalent (farmers 10%) | EUR 12,543.73 to EUR 29,083.35 | same |
| SC, born from 1 January 1962 | EUR 83.89 a week (farmers EUR 55.93) | EUR 29,083.36 and over | same |
| State share | 50% of the contribution paid by the person, from the Consolidated Fund | Not paid by the client | Cap. 318 art. 10(4): https://legislation.mt/eli/cap/318/eng/pdf |
| Low-income certificate | Yearly means under the Second Schedule Part I not over EUR 1,005; EUR 1,470 for the married category in article 12(1)(i) | Self-employed, not self-occupied; application, Director’s acceptance and no relevant change in circumstances; certificate valid twelve months. Capital and means conditions below also apply | Cap. 318 art. 12(1): https://legislation.mt/eli/cap/318/eng/pdf |
| Payment periods | Four months ending on the last day of April, August and December | Unless the Director approves other arrangements | Cap. 318 art. 11: https://legislation.mt/eli/cap/318/eng/pdf |
| Late Class 2, from 1 January 2026 | Interest per month at the ITMA art. 44(2A) rate, 0.6% for every month or part | Replaces the 1% a month further contribution; the rate rule caps total interest at the unpaid tax amount. Obtain the official assessment for arrears and any cross-2025/2026 debt | Cap. 318 art. 116(1) proviso: https://legislation.mt/eli/cap/318/eng/pdf ; rate in S.L. 372.28: https://legislation.mt/eli/sl/372.28/eng/pdf |
| Director's claim | Barred after thirty years | Unpaid Class 2 or a rate, category or class difference | Cap. 318 art. 116(5)(i): https://legislation.mt/eli/cap/318/eng/pdf |
| Person's own request to pay or adjust | Void after pension age or five years from when the proper rate was due, whichever is earlier | Subject to the specific article 116(5) provisos, including the age-59 options below; specialist cases are referred | Cap. 318 art. 116(5): https://legislation.mt/eli/cap/318/eng/pdf |
| First calendar year | Lowest rate, SA | New self-occupied person without prior earnings (DSS guidance) | DSS Social Security Contributions: https://socialsecurity.gov.mt/en/information-and-applications-for-benefits-and-services/social-security-contributions/social-security-contributions/ |

The flat amounts are the 15% weekly equivalent at the band edges: EUR 12,543.72 x 15% / 52 = EUR 36.18 and EUR 29,083.36 x 15% / 52 = EUR 83.89. Income above the cohort ceiling adds nothing. An annual figure is the weekly amount times the contribution weeks (52 in 2026; some years have 53). Do not reuse an old annual total.

## Boundary and exception table

| Situation | Treatment | Law |
|---|---|---|
| Activity earnings EUR 910 a year or less | Not self-occupied; may still be self-employed on other income | Art. 2 |
| Self-employed, not self-occupied, claiming low income | Apply the Second Schedule Part I capital/means test as well as the article 12 annual limit; apply to the Director. Exemption lasts while the certificate is valid and no relevant circumstances change. SP (single) or SA (married) may be elected instead; renewal more than three months late can trigger SP/SA at the Director’s discretion. Separated, non-gainfully-occupied person may elect to exclude spousal maintenance | Art. 12(1)–(3) and Second Schedule Part I |
| Married, not self-occupied | Article 3(2) says “not legally separated or who has not been abandoned by his spouse”; do not apply a blanket zero liability where separation/abandonment or a historic election is involved. Pre-5 January 2004 continuation and the specified early-retirement election require their own conditions. Check this point with one of our partner accountants. | Art. 3(2) |
| Full-time student | Article 6(1)(b) concerns full-time education/training at a Government-recognised institution; payment as self-occupied and article 6(2)’s self-occupied activity exception must be checked before applying the exclusion. Where liable and part-time self-occupied, the MTCA SA student option requires age under 24 | Art. 6(1)(b), (2); MTCA 2026 table |
| Pensioner under the Act (not an Injury Pension) not gainfully occupied, or on Social Assistance | Not self-employed or self-occupied under article 6(1)(d)/(f). A self-occupied widow retaining Widows’ Pension under articles 32(2)/41 is still self-occupied | Art. 6(1)(d), (f) |
| Reaching pension age or the 65th birthday | Apply both the article 2 retirement definition and article 3 insured-person test; the self-employed definition has a separate 65th-birthday limit. Do not compute a full year automatically. Check this point with one of our partner accountants. | Arts 2–3 |
| Insurably employed with a part-time side activity | The article 2 self-employed definition excludes an employed person; use Class 1, subject to the article 14 approved substitution below. Determine actual insurable employment before treating a side activity as exempt | Arts 2, 7, 14 |
| Liable to Class 1, also self-occupied, wants Class 2 | Request and Director’s approval required; own Class 2 must exceed combined employer and employee Class 1. Approval is revoked when that condition ceases. No reversion until self-occupation ceases and the Director is informed | Art. 14 |
| Ordinarily resident in Malta, employed abroad under a contract of service outside insurable employment | May request Class 1 instead of Class 2, from the date determined by the Director (not later than the request); no employer share. Class 2 payment form/timetable applies while both conditions continue | Art. 13 |
| Host family earnings | Elective exemption on those earnings | Art. 12(4) |
| Homeworker, net earnings not over 50% of the 18+ national minimum wage | Elective exemption | Art. 12(5) |
| Outworker, tourist guide, government-impressed vehicle driver | Extra 1/16 of remuneration from the engager/Government towards Class 2, excluding article 14 cases. “Outworker” means physical manufacture in own time, away from the engager’s premises, at piece rates; vehicle must be impressed by Government under its procedure | Art. 15(1), (3) |
| Over 45, not gainfully occupied at least five consecutive years, obtains Trading Licences Act licence for self-occupation | Entitled to receive from Government the contributions payable from that self-occupation for the first 52 weeks; do not assume the contribution itself disappears | Art. 15(7) |
| Aged at least 59 but below 65 and gainfully occupied/self-occupied; or age 59+ receiving the specified Invalidity Pension/Carer’s Allowance/Increased Carer’s Allowance/Carer’s Grant; or at least 59 but below 65, not occupied, whose payment produces at least ten paid years for a pension | Article 116(5) gives the five-year arrears option at the SA rate of the claim year; the latter categories may be granted it. Establish the exact category and official amount. Check this point with one of our partner accountants. | Art. 116(5) provisos |
| Abroad or in hospital when payment fell due | For a self-employed/self-occupied person or article 13 person who proves this to the Director’s satisfaction, prescribed time extends to the 31st day after return/discharge | Art. 116(1) proviso |

**Low-income means test.** Under [Second Schedule Part I](https://legislation.mt/eli/cap/318/eng/pdf), means include the value of property that is or could be invested or put to profitable use, including trust property, excluding the home, furniture, jewellery and personal effects. The listed cash, securities, trust capital and non-profitable urban immovable property (excluding the home) must not together exceed EUR 9,320 (single/widowed) or EUR 16,310 (married). This is a capital disqualification as well as an annual-means test. The first EUR 585 of capital is disregarded where the limits are met; the specified urban property is treated as producing 5.5% annually. Count income or privilege that is or could be enjoyed, including trust entitlements, with the paragraph 3 exclusions for assistance, pensions, benefits and allowances under the Act; friendly-society/trade-union sickness benefit; charitable funds; other pensions except a Malta Dockyard Act article 16A pension; and the first EUR 470 from hand knitting, lace making, crochet and embroidery at home without mechanical processes. The EUR 1,005/1,470 amount alone never proves exemption. For a means computation or eligibility not settled by these conditions: Check this point with one of our partner accountants.

### Bank statement lines

Class 2 is a personal contribution: keep it out of VAT and business supplies. MTCA also collects income tax, provisional tax and FSS: a debit to MTCA (or CFR, Inland Revenue, DSS on older statements) is Class 2 only if the reference or the MTCA statement says so. A provisional tax payment is income tax. Keep an employer's Class 1 separate. A lump sum marked arrears may mix contributions and interest: get the breakdown. A pension or benefit credit is a receipt, not a contribution payment; this is a bank-reconciliation description, not a decision that the receipt is taxable.

## Worked cases

Full-year liability is assumed after the status tests; all clients are invented. The original hypothetical inputs are retained; these examples do not decide retirement, low-income means or arrears eligibility.

### Case 1: SB band, born 1990

Self-occupied web developer, 2025 net earnings EUR 20,000, inside SB. Weekly: EUR 20,000 x 15% / 52 = EUR 57.69; over 52 weeks EUR 2,999.88. Billed four-monthly in arrears.

```oa-check
name: Class 2 SB 2026, net earnings EUR 20,000, weekly to the cent
inputs:
  prior_net: 20000
  weeks: 52
steps:
  - weekly: round(prior_net * 0.15 / weeks, 2)
  - annual_paid: weekly * weeks
expected:
  weekly: 57.69
  annual_paid: 2999.88
```

### Case 2: part-time woman, pay SA flat or elect 15% (a decision)

A part-time self-occupied woman, born 1990, 2025 net earnings EUR 8,000. SA flat: EUR 36.18 a week, EUR 1,881.36 for 2026. Electing 15%: EUR 8,000 x 15% / 52 = EUR 23.08 a week, EUR 1,200.16: she pays EUR 681.20 less, but paying below EUR 36.18 may reduce contributory benefits and pension. The trade-off is cash now against benefit entitlement.

```oa-check
name: Class 2 2026, SA flat versus 15 percent election, earnings EUR 8,000
inputs:
  prior_net: 8000
  sa_weekly: 36.18
  weeks: 52
steps:
  - elected_weekly: round(prior_net * 0.15 / weeks, 2)
  - annual_sa: sa_weekly * weeks
  - annual_elected: elected_weekly * weeks
  - saving: annual_sa - annual_elected
expected:
  elected_weekly: 23.08
  annual_sa: 1881.36
  annual_elected: 1200.16
  saving: 681.20
```

### Further cases (prose)

- **SC, born 1975**, earnings EUR 60,000: EUR 83.89 a week; EUR 4,362.28 over 52 weeks.
- **SC, born 20 June 1961**, earnings EUR 60,000: EUR 73.56 a week while liable; the person is already beyond the cohort’s pension age of 64 at the start of 2026. Whether liability continues depends on the article 2 retirement conditions; no full-year amount is given. Check this point with one of our partner accountants.
- **Passive income only**, single, born 1985, 2025 rent EUR 9,000: if insured and otherwise liable, SP at EUR 31.97. For the married alternative apply article 3(2), including historic elections, before deciding that nothing is due. EUR 900 of annual income alone does not establish exemption: capital, deemed income, exclusions and the certificate conditions must also be checked. Check this point with one of our partner accountants.
- **Late payment**: EUR 500 due in 2026 paid three months late: if three chargeable months/parts are established, EUR 500 x 0.6% x 3 = EUR 9.00, below the EUR 500 cap. This conditional arithmetic does not determine the chargeable months or an older debt’s transition: use the official statement. Check this point with one of our partner accountants.

## When to refuse or refer

- **No date of birth: do not compute.**
- **Do not use the 2024 Tenth Schedule figures for a 2026 bill.** A 2025 bill needs MTCA's 2025 table.
- **Arrears and late charges:** take them from an official statement. A Director's notice of unpaid contributions is "sufficient evidence ... unless the contrary is proved" (art. 116(4)); "Director" means the Director General (Social Security) or the Commissioner for Tax and Customs (art. 2 proviso).
- **Special cases:** disability, invalidity and carer cases; students and pensioners claiming an exclusion; religious-order and Libya-employment arrears; court-ordered transfers of contributions (arts 8(6), 10(5)); anyone at or past pension age; cross-border and non-resident cases. Check this point with one of our partner accountants.
- **Status requiring an individual determination:** an employee-director drawing fees; a returner; a mid-year switch between employment and self-occupation; first-year commencement weeks; two part-time self-occupations with no employment. Check this point with one of our partner accountants.
- Students aged 24 or more claiming the reduced option: the consolidated Tenth Schedule has no age limit, MTCA's footnote says not reached 24 and the DSS page says under 25; do not infer an age-24 entitlement from these conflicting guidance pages. Check this point with one of our partner accountants.

## Filing and payment

**Who collects.** Class 2 is paid "at the Malta Tax and Customs Administration in such form and manner as may from time to time be determined by the Director" (art. 11).

**When.** "in arrears at intervals of four months ending on the last day of April, August and December of each year" (art. 11): January to April, May to August, September to December. The due date and amount are on MTCA's bill. Rates per period are those "for the four months ending on the last day of April, August and December" (art. 10(3)). Not quarterly.

**First year.** DSS guidance lets a new self-occupied person pay SA in the first calendar year because prior earnings are not available: EUR 36.18 a week in 2026. Determine the actual commencement weeks separately: Check this point with one of our partner accountants.

**Adjustments.** The Director can require the income tax returns or assessments to establish net income or earnings (art. 133); a payment in the wrong class, category or rate gives a difference to claim or pay.

**Late payment.** From 1 January 2026 the further contribution on late Class 2 is "substituted by interest per month as provided for in article 44(2A) of the Income Tax Management Act and the Income Tax (Rate of Interest) Rules" (art. 116(1) proviso): 0.6% for every month or part; the rate rule caps total interest at the debt amount. Article 116(2) permits a judicial letter after dues remain unsettled for three months; it becomes an executive title ten days after service unless challenged in time, including a court-granted extension of no more than thirty days on just cause. Proceedings and the article 116(3) privileged claim over the estate require individual advice: Check this point with one of our partner accountants.

**2025 contribution year** (Monday 6 January 2025 to Sunday 4 January 2026), settling now: category on 2024 earnings; do not use this Guide’s 2026 rate table for that year. A debt spanning 2025 and 2026 needs the official contribution statement and the applicable transition determination: Check this point with one of our partner accountants.

## Completion checklist

- [ ] Date of birth and age recorded.
- [ ] Status fixed; exclusions in arts 3(2), 6 and 12 checked.
- [ ] Base on 2025: activity earnings exclude the article 2 interest, rents and spouse income; passive-income net income is a different base. Apply the listed benefit exclusions to the applicable category.
- [ ] Category from MTCA's 2026 table.
- [ ] SB weekly = 15% / 52 to the cent; reduced options only where they fit, with the benefit warning.
- [ ] Payment periods April, August, December; bill dates checked.
- [ ] Arrears from an MTCA statement.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for MTCA Class 2 rates 2026 (SP, SA, SB, SC, farmers, reduced option footnote, self-occupied and self-employed definitions) | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-2---social-security-contribution-rates/2026 | 2026-11-26 |
| Read Cap. 318 arts 2–3, 6–7, 10–15, 116, 133, Second Schedule Part I and Tenth Schedule Parts II–III rules (15%, 10%, weekly equivalent, previous calendar year) | https://legislation.mt/eli/cap/318/eng/pdf | 2026-11-26 |
| Read for S.L. 372.28 rule 2 (0.6% interest rate that art. 116 now applies) | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-26 |
| Read for DSS Social Security Contributions page (first-year SA for a new self-occupied person) | https://socialsecurity.gov.mt/en/information-and-applications-for-benefits-and-services/social-security-contributions/social-security-contributions/ | 2026-11-26 |

Not yet confirmed: no unsupported claim remains usable. The student age-24 conflict, earlier-cohort/individual retirement, first-year commencement weeks, breeder eligibility beyond the 2026 farmer identification, cross-year arrears, procedural/means determinations and the original specialist cases are explicitly referred above. This Guide supplies no 2025 rates or universal bill/portal instructions.
