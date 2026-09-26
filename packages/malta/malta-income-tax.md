---
name: malta-income-tax
description: "Use this skill whenever asked about Malta income tax for self-employed individuals. Trigger on phrases like \"how much tax do I pay\", \"income tax return\", \"self-assessment\", \"allowable deductions\", \"capital allowances\", \"provisional tax\", \"TA22 regime\", \"TA24\", \"chargeable income\", \"tax credits\", \"self-employed tax Malta\", or any question about filing or computing income tax for a self-employed or part-time self-employed client. Also trigger when preparing or reviewing the annual income tax return or a TA22, computing deductible expenses, or advising on provisional tax instalments. NOTE: TA24 is the 15% final tax form for RENTAL income (ITA Art. 31D) — if the user means rental income, see Section 5.11; the self-employed annual filing is the personal Income Tax Return. This skill covers tax rates (single/married/parent), the return working-paper structure, allowable deductions, capital allowances, provisional tax, the TA22 part-time regime, penalties, and interaction with VAT and SSC. ALWAYS read this skill before touching any income tax work."
version: 2.0
jurisdiction: MT
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta personal income tax: rates, residence, final taxes, provisional tax and filing

## Scope ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

This Guide covers Malta income tax for **individuals**: employees, the self-employed, part-time workers, landlords and people selling Maltese property. Malta taxes a calendar **basis year**, and the tax is charged for the following **year of assessment**.

- **Basis year 2026 = year of assessment 2027.** This is the primary year of this Guide. Its return is due by 30 June 2027.
- **Basis year 2025 = year of assessment 2026.** The dated section "2025 income (year of assessment 2026)" covers the returns being filed now. Their statutory date was 30 June 2026, so a return not filed yet is late (see "Filing and payment").

Marital and family status is tested "in the year immediately preceding the year of assessment", which means the basis year itself.

**Sources.** Every figure here comes from the Laws of Malta (legislation.mt): the Income Tax Act (Cap. 123), the Income Tax Management Act (Cap. 372), their subsidiary rules, and the Budget Measures Implementation Acts (Act IX of 2025 and Act III of 2026). The MTCA website (mtca.gov.mt) refused our automated source checks on 25 September 2026. So items that live only on MTCA's site are marked "check on mtca.gov.mt". These are form names (TA22, TA24, FS3, FS4), any online-filing extension, and the Class 2 contribution tables.

**Not covered:** companies and partnerships, a full non-resident computation, the special residence programmes (Global Residence Programme, Residents Scheme, highly qualified persons), double tax relief, VAT (see the Malta VAT Guide) and the detail of social security contributions.

## Ask the client first

- Which basis year? 2026 income (year of assessment 2027) uses the Act III of 2026 tables, which add four child categories. 2025 income (year of assessment 2026) uses only the three Act IX of 2025 tables.
- Residence: were you resident in Malta in that year? Domicile: are you domiciled in Malta, and are you ordinarily resident here? If not domiciled, how much foreign income arose, and how much of it was brought into Malta?
- Were you married and living together in that year? Do you file jointly (the default), separately (article 49A), or with a separate computation (article 50)?
- Children: how many, and how old? Each must be under 18, or under 23 and in full-time education. Did you have custody, or did you pay maintenance under article 12(1)(t)? Is either spouse an EU/EEA national or a long-term resident? If not, was each child born in Malta and resident in Malta?
- Single parent: did you have sole custody, receive the children's allowance as sole beneficiary, get no maintenance from the other parent, and live apart from them?
- What kinds of income: employment (FSS), self-employment (full-time or part-time), rent, dividends or interest, foreign income, or a property sale?
- Part-time work: were you in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice? Is the part-time work registered with Jobsplus and done for a different employer?
- Rent: is the property residential or a garage, or commercial? Is the tenant related to you? Is the lease registered as a long private residential lease?
- Provisional tax: what does your provisional tax statement show, and what have you paid?
- Were any returns or payments late?

## The method, step by step

1. **Fix the year.** Take the basis year of the income and add one to get the year of assessment. Status, custody and residence are all tested in the basis year.
2. **Decide residence and domicile.** A resident individual is taxed under article 56(1)(a) or (b). A non-resident uses the article 56(1)(c) scale unless an EU/EEA proviso applies. A resident who is not domiciled, or not ordinarily resident, is taxed on foreign income only when it is received in Malta, and is not taxed on foreign capital gains. Then test the €5,000 minimum tax for non-doms (article 56(27)). ([ITA art. 4 and 56](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
3. **Take out income taxed at a final rate.** This means part-time work (10%), rent where the 15% option is chosen, property transfers under article 5A, and final-withholding investment income. Keep this income out of the progressive computation unless the person opts to declare it. ([ITA art. 90A, 31D, 5A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
4. **Compute business profit.** Deduct outgoings "wholly and exclusively incurred in the production of the income" (article 14(1)). Remove anything barred by article 26: private or domestic spending, capital spending, improvements, recoverable amounts and voluntary payments. Add capital allowances under the Wear and Tear Rules (S.L. 123.01).
5. **Add the other income taxed at progressive rates.** This is employment income, rent where the 15% option is not taken (net of the S.L. 123.26 deductions), and any part-time income over its cap. The total is chargeable income. ([ITA art. 90A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
6. **Pick the rate table** for the basis year and status, then apply: chargeable income × rate − subtraction. A table does not apply unless every one of its conditions is met.
7. **Credit tax already paid.** This means FSS tax deducted by employers, provisional tax, and part-time tax paid on income the person opted to declare. The balance is due on the tax settlement date, which is the return date.
8. **File the return** by 30 June of the year of assessment. Pay the final taxes and file their statements by their own dates, most of them 30 April.
9. **Add interest and additional tax** for anything late. Interest is 0.6% a month, capped at the tax. Late-return additional tax follows Table A. ([ITMA art. 44](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b))
10. **Set up next year's provisional tax.** The benchmark comes from the last return. Pay 20%, 30% and 50% on 30 April, 31 August and 21 December. File a reduction form if this year's liability will be lower. ([P.T. Rules](https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4))

Order matters. If you apply the rate table before removing final-tax income, that income is taxed twice. If you pick a table without checking nationality and custody, the tax can be understated.

## Resident rate tables, basis year 2026 (year of assessment 2027) ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))

Tax = chargeable income × rate − subtraction. Act III of 2026, article 19, replaced article 56(1)(a) and (b). Its article 13(2)(b) makes the change "applicable from the year of assessment 2027".

| Status in the basis year | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% above (subtract) |
| --- | --- | --- | --- | --- |
| Single (other individual), art. 56(1)(b)(i) | €12,000 | over €12,000 and under €16,000 (€1,800) | over €16,000 and under €60,000 (€3,400) | over €60,000 (€9,400) |
| Married, joint, no qualifying child, art. 56(1)(a)(i) | €15,000 | over €15,000 and under €23,000 (€2,250) | over €23,000 and under €60,000 (€4,550) | over €60,000 (€10,550) |
| Parent, art. 56(1)(b)(ii) | €13,000 | over €13,000 and under €17,500 (€1,950) | over €17,500 and under €60,000 (€3,700) | over €60,000 (€9,700) |
| Married, 1 qualifying child, art. 56(1)(a)(ii) | €17,500 | over €17,500 and under €26,500 (€2,625) | over €26,500 and under €60,000 (€5,275) | over €60,000 (€11,275) |
| Married, 2 or more qualifying children, art. 56(1)(a)(iii) | €22,500 | over €22,500 and under €32,000 (€3,375) | over €32,000 and under €60,000 (€6,575) | over €60,000 (€12,575) |
| Parent, 1 qualifying child, art. 56(1)(b)(iv) | €14,500 | over €14,500 and under €21,000 (€2,175) | over €21,000 and under €60,000 (€4,275) | over €60,000 (€10,270, as enacted) |
| Parent, 2 or more qualifying children, art. 56(1)(b)(v) | €18,500 | over €18,500 and under €25,500 (€2,775) | over €25,500 and under €60,000 (€5,325) | over €60,000 (€11,325) |

**Note on €10,270.** The enacted text of Act III of 2026 and the consolidated Act both say "subtracting €10,270". That leaves a €5 step at €60,000: the 25% formula gives €10,725, but the 35% formula gives €10,730. A continuous table would subtract €10,275. Use the enacted €10,270. If the difference matters, check with MTCA whether it has been corrected.

### Who gets which table ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Married tables** (article 56(1)(a)) apply to a married couple resident in Malta and taxed jointly under article 49. If either spouse elected a separate return (article 49A), or the responsible spouse opted for a separate computation (article 50), each spouse uses the article 56(1)(b) tables instead. An EU/EEA national whose spouse is not resident can still use the married tables if the Commissioner is satisfied that at least 90% of the couple's worldwide income is from Malta.
- **Parent table** (article 56(1)(b)(ii)): the individual was a parent who kept a child in custody, or paid maintenance for the child under article 12(1)(t). The child must be not over 18, or not over 23 if in full-time education.
- **Qualifying-child tables** (married (ii) and (iii), parent (iv) and (v)) need **all** of the following:
  - custody of the child, or maintenance under article 12(1)(t). For the parent tables, custody can also cover a spouse's child or a certified cohabitant's child;
  - the same age test;
  - a spouse, the individual, or the individual's spouse must be an EU/EEA national or hold long-term resident status;
  - if nobody is an EU/EEA national, the child (or each of the two children) must have been born in Malta and be resident in Malta.
  
  If any condition fails, fall back to the married (i) or parent (ii) table.
- **Single parent with sole custody** (article 56(1)(b)(iii)) is taxed on the **married** table (a)(i), unless table (iv) or (v) gives a better result. The person must have been unmarried, widowed, separated or divorced, and must have met all four conditions:
  - wholly maintained, in sole custody, a child whose own income was not over €3,400. The child must be not over 18; or not over 23 and in full-time education or serving an apprenticeship; or incapacitated by infirmity. This rule has no nationality or born-in-Malta test;
  - sole beneficiary of the children's allowance;
  - no maintenance from the other parent;
  - not living with the other parent.

### 2025 income (year of assessment 2026) ([Act IX of 2025](https://legislation.mt/getpdf/6811d803cf7b7f36a4f360f5))

Act IX of 2025, article 15, set these tables. Its article 10(2)(a) makes them "applicable as from the year of assessment 2026". The four qualifying-child tables do **not** apply to 2025 income.

| Status (basis year 2025) | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% above (subtract) |
| --- | --- | --- | --- | --- |
| Single | €12,000 | €12,000 to €16,000 (€1,800) | €16,000 to €60,000 (€3,400) | over €60,000 (€9,400) |
| Married, joint | €15,000 | €15,000 to €23,000 (€2,250) | €23,000 to €60,000 (€4,550) | over €60,000 (€10,550) |
| Parent | €13,000 | €13,000 to €17,500 (€1,950) | €17,500 to €60,000 (€3,700) | over €60,000 (€9,700) |

The sole-custody single-parent rule quoted above is taken from the text that applies from year of assessment 2027. For 2025 income, check its wording on mtca.gov.mt.

### Non-residents ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

An individual not resident in Malta in the basis year pays tax under article 56(1)(c):

- 0% on the first €700;
- 20% on the next €2,400;
- 30% on the next €4,700;
- 35% on the remainder.

An EU/EEA national gets the resident tables if at least 90% of their worldwide income is from Malta. Other EU/EEA nationals have a cap based on their worldwide income. Refer non-resident cases (see "When to refuse or refer").

## Residence, domicile and the remittance basis ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Resident** (article 2): "an individual who resides in Malta except for such temporary absences as to the Commissioner may seem reasonable". There is no day count in the Act. The Act does not define domicile or ordinary residence.
- **Remittance basis** (article 4(1), provisos (i) and (ii)): a person who is not ordinarily resident **or** not domiciled in Malta is taxed on foreign income only "on the amount received in Malta". Foreign capital gains are not taxed at all.
- **Exceptions:** provisos (i) and (ii) do not apply to a long-term resident or to a holder of a permanent residence certificate or card. Nor do they apply to an individual "whose spouse is ordinarily resident and domiciled in Malta".
- **Minimum tax for non-doms** (article 56(27)) applies to an individual who meets all of these:
  - ordinarily resident but not domiciled, and taxed on the remittance basis;
  - not under a minimum-tax scheme;
  - foreign income **not less than €35,000** (a married couple taxed under article 49 counts both spouses' foreign income), not received, or not fully received, in Malta.

  Their tax is "not less than €5,000" a year. Tax paid under the Act counts towards the minimum, except tax on article 5A property transfers. If the person proves that tax on their worldwide income would be lower than the minimum, it is capped at that lower amount.

## Part-time work final tax ([Income Tax Act art. 90A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Who qualifies** (Part-time Work Rules, S.L. 123.39, rule 2): a person resident in Malta who has one of these:
  - full-time employment registered with Jobsplus;
  - a pension taxable in Malta;
  - full-time education or an apprenticeship.

  Article 90A(9) extends this to a spouse living with a qualifying spouse. The extension does not cover income from the spouses' relatives or their companies.
- **Rate:** 10% from year of assessment 2023 (article 90A(11)). Before that it was 15%. The tax is final, and the income is not declared in the return.
- **Caps** (rule 3(2)): the rate covers self-employed profit (article 4(1)(a)) up to €12,000, and part-time employment income (article 4(1)(b)) up to €10,000. Any **excess** is declared in the return at normal rates.
- **Conditions for the self-employed** (rule 4). All of these are required:
  - the part-time work is registered with Jobsplus;
  - no more than two employees, both part-time;
  - proper books are kept;
  - the work is done for someone other than the full-time employer;
  - the person is registered for VAT, unless not required to register or exempt.
- **Part-time employment:** the work must be registered with Jobsplus, done for a different employer, and not more than 30 hours a week (rule 5). The employer deducts the tax (article 90A(7)(a)).
- **Paying as a self-employed part-timer:** pay the tax by **30 April** of the year after the income was earned. Include a statement of accounts showing taxable net profit (ITMA article 42(4)(a)). The form is commonly called TA22; check on mtca.gov.mt.
- **Opting out:** the person may declare all part-time income in the return at progressive rates. Any final tax already paid is then credited or refunded (article 90A(2)).
- **Risks:** if the tax is unpaid by the due date and the Commissioner sends a notice, **all** the part-time income is taxed at progressive rates (article 90A(8)). The Commissioner can also refuse the regime if the work is really the person's normal activity (article 90A(10)).

## Rental income: the 15% option ([Income Tax Act art. 31D](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **What qualifies:** rent from a "tenement". This means a dwelling, or part of one, occupied as a home, or a garage. A commercial tenement or club qualifies only if it is not let to or from a related body of persons (article 31D(8)).
- **Tax:** 15% of **gross** rent received, with no deductions. It is final, with no set-off or refund, and the rent stays out of the return (article 31D(2)-(3)).
- **All tenements together:** if the option is taken for a year, it covers the rent from **all** the person's tenements (article 31D(4)).
- **Undeclared rent:** if an enquiry finds rent that was not declared, it is taxed at 35% of the gross, plus interest and additional tax. This applies whether or not the option was taken (article 31D(5)).
- **Payment:** by **30 April** of the following year, with the prescribed form (ITMA article 42(4)(c)). The form is commonly called TA24; check on mtca.gov.mt.
- **Long-let rebate** (S.L. 372.30): available with the 15% option on a private residential lease of two years or more, registered as a long private residential lease. The rebate by lease length and number of bedrooms:
  - at least two years but under three: €200 (one bedroom), €300 (two), €400 (three or more);
  - three years or more: €300 (one bedroom), €400 (two), €500 (three or more).

  The rebate is pro-rated in the first and last year of the lease, and cannot exceed 15% of that lease's rent.
- **Without the option**, the rent goes into the return at progressive rates. The S.L. 123.26 deductions are then:
  - interest;
  - ground rent or similar burdens;
  - any tourism licence fee;
  - 20% of what is left after ground rent and the licence fee. This 20% is not given on income from an emphyteutical concession.

  Rule 3 applies to income under ITA article 4(1)(f), which was "Repealed by Act XX of 1996"; rent is now charged under article 4(1)(e). Check with MTCA whether the rules still apply before you rely on them.

## Selling property in Malta: the article 5A final tax ([Income Tax Act art. 5A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

The tax is charged on the **transfer value**, not the gain, except in the inherited-property case. It is paid through the notary on the deed and is final.

| Transfer (made on or after 1 January 2015) | Rate | Provision |
| --- | --- | --- |
| General rule | 8% of transfer value | 5A(5)(a), proviso |
| Property acquired before 1 January 2004 (no promise of sale notified before 17 November 2014) | 10% of transfer value | 5A(5)(f) |
| Not part of a project, sold within five years of acquisition | 5% of transfer value | 5A(5)(e) |
| An individual (or two co-owners) declared in the deed of acquisition that it was bought as their sole ordinary residence; the transfer is within three years of acquisition; and at the transfer they own no other residential property (declared to the notary) | 2% of transfer value | 5A(5)(g) |
| Inherited after 24 November 1992, or donated more than five years before | 12% of (transfer value − acquisition value), unless the transferor elects otherwise | 5A(5)(b) |
| Inherited before 25 November 1992 | 7% of transfer value | 5A(5)(c) |

The 5% rate is lost in two cases. The first is where a related person owned the property as part of a project in the previous five years. The second is where works needing a development permit were done in those five years, unless the owner had declared it as their sole ordinary residence.

**No tax** is due (article 5A(4)) in these cases, among others:

- **Own residence:** a dwelling house, not part of a project, that meets all of these:
  - owned and occupied as the transferor's own residence for at least three consecutive years immediately before the transfer;
  - sold within 12 months of vacating it;
  - declared as the main residence.

  Periods of ownership by a spouse, or by a direct ascendant, from whom the property was inherited count towards the three years. On divorce or separation, the house counts as vacated only when the other spouse also leaves.
- **Donations** to a spouse, a descendant or ascendant (or their spouse), or, where there are no descendants, to a sibling or a sibling's descendant.
- **Transfers between spouses** on separation or divorce, or when the community of acquests is dissolved.

Refer projects, companies, trusts and special designated areas.

## Deductions and capital allowances for the self-employed ([Income Tax Act art. 14 and 26](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Test:** deduct only outgoings "wholly and exclusively incurred in the production of the income" (article 14(1)). Examples in article 14 include borrowing costs, business rent, repairs and bad debts.
- **Barred by article 26:**
  - private or domestic expenses;
  - capital spending, except as allowed under article 14;
  - improvements;
  - losses or expenses that are recoverable;
  - rent not paid to produce the income;
  - voluntary payments;
  - payments that are criminal offences.
- **Mixed use:** apportion the cost. Default to 0% until the business share is documented, for example for a home office, car or phone.
- **Entertainment:** the Act has no specific rule. Treat it as private unless the wholly and exclusively test is clearly met, and flag it.
- **Social security Class 2:** Part IV of the Act (articles 14 to 26) contains no deduction for social security contributions. Leave them out of the computation and record them as a memo.
- **Capital allowances** (article 14(1)(f), S.L. 123.01):
  - straight line, over at least the minimum number of years;
  - a full year's allowance in the year of acquisition, none in the year of disposal;
  - only where proper records of cost are kept;
  - reduced to the business-use share;
  - unused allowances carry forward;
  - total allowances cannot exceed original cost;
  - industrial buildings or structures get at most 2% of cost a year, excluding land. They also get an initial deduction of one-tenth (10%) of the capital expenditure in the year they are first used (article 14(1)(j));
  - cars and other vehicles for transporting people (S.L. 123.07 rule 3, [Income Tax (Deductions) Rules](https://legislation.mt/getpdf/66f65d8f3b56613c3cae68d9)): if the car cost more than €14,000, compute wear and tear, any initial deduction and the article 24 balancing allowance or charge as if it cost €14,000. For a leased car with a listed price over €14,000, the deductible lease payments are capped at lease payments × €14,000 ÷ listed price. Apply the business-use share after the cap. The rule does not cover vehicles not commonly used as private vehicles;
  - a sale or scrapping triggers a balancing statement (article 24).

| Asset (S.L. 123.01 Schedule) | Minimum years |
| --- | --- |
| Computers and electronic equipment; computer software | 4 |
| Motor vehicles; other machinery | 5 |
| Catering equipment; air-conditioners; medical equipment | 6 |
| Furniture, fixtures, fittings and soft furnishings; other plant | 10 |
| Electrical and plumbing installations and sanitary fittings | 15 |

## Provisional tax for the self-employed ([Payment of Provisional Tax Rules, S.L. 372.18](https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4))

- **Who pays:** an individual who was liable to tax in the benchmark year. This excludes anyone eligible for the article 12 election not to file, typically an employee whose income was all under FSS.
- **Benchmark:** the tax payable in the self-assessment for the benchmark year, adding back any provisional tax. The benchmark year is the last year of assessment whose return was due before the calendar year of the first payment. The benchmark is never this year's projected income. If there is no self-assessment and no Commissioner determination, the benchmark is nil (rule 7(1)(c)).
- **Due dates** (rule 4) and amounts (rule 5), all in the basis year:
  - at least 20% of the benchmark by 30 April;
  - a further 30% by 31 August;
  - a further 50% by 21 December.
- **Reduction** (rule 10): if this year's liability will be lower than the benchmark, file the P.T. reduction form. Payments can then be limited to the estimated liability.
- **Late provisional tax** (rule 14): additional tax of 0.6% for each month or part month, for periods from 1 June 2022. If the final self-assessment tax is below the benchmark, the additional tax on the difference is cut by 90%. The charge stops at the tax settlement date.

## Employees: the Final Settlement System ([FSS Rules, S.L. 372.14](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

- The employer deducts tax each pay period from the Main Tax Deduction Tables. The table depends on the employee's tax status declaration (form FS4) and the length of the pay period. A year-end adjustment in the final pay period applies the article 56(1)(a) or (b) rates.
- The employer gives the employee the Payee Statement of Earnings (commonly FS3) by **31 January** of the following year, or within seven days if the employment ends. The employer files its annual reconciliation statement by **15 February** (rules 21 and 22).
- **No return needed** (ITMA article 12) in either of these cases:
  - a resident individual whose income was **all** taxed at source under FSS and fully reported in the statements of earnings;
  - a resident individual with no business income whose total income did not exceed the 0% band.

  The Commissioner then makes a determination. If you disagree, file an adjustment form within ten years.
- From 1 January 2025, tax paid through FSS on income left out of a return does not count as "endangered tax" for the omission penalty (Schedule, item 1, as amended by Act IX of 2025).

## Social security Class 2 (summary only) ([Social Security Act, Cap. 318](https://legislation.mt/eli/cap/318/eng))

Self-occupied persons pay Class 2 contributions under the Social Security Act, Cap. 318, not the Income Tax Act. They are not deducted in the income tax computation (see above). For rates, caps, and the position of someone who is both employed and self-occupied, use the Malta social security Guide or check on mtca.gov.mt.

## Boundary and exception table ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Situation | Treatment |
| --- | --- |
| Chargeable income exactly at a band edge (e.g. €16,000 single) | The Act says "exceeds ... but is less than". Both formulas give the same tax at the edge (single: €600) |
| Married couple, no EU/EEA national, child born abroad | Married (a)(i) table, not (a)(ii) |
| Child aged 22 in full-time university study | Qualifies (not over 23 and in full-time education) |
| Child aged 20, working full-time | Does not qualify (over 18 and not in education) |
| Part-time self-employed profit of exactly €12,000 | All at 10%. Nothing is over the cap |
| Part-time work for a company owned more than 50% by the same shareholders as the full-time employer | Counts as the same employer, so the 10% regime is not available (rule 6(1)(a)) |
| Rent from a commercial tenement let to a related company | Not a tenement, so the 15% option is not available |
| Non-dom with €34,000 of foreign income not remitted | Below €35,000, so no minimum tax |
| Own home sold 13 months after moving out | Outside the 12-month window: 8% (5% if within five years of acquisition, 10% if acquired before 2004) |
| Provisional tax paid on 1 May | Late: 0.6% additional tax for that month |

## Worked cases ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

The amounts in these cases are invented. The rates come from the sources linked in the sections above.

**Case 1: single, self-employed, basis year 2026.**
- Facts: gross fees €45,000; allowable expenses €13,000; a laptop costing €1,500, written off over 4 years at €375 a year; Class 2 paid €3,000 (memo only); provisional tax paid €3,500.
- Net profit is €32,000. Less €375, chargeable income is €31,625.
- Tax: €31,625 × 25% − €3,400 = €4,506.25.
- Balance due by 30 June 2027: €4,506.25 − €3,500 = €1,006.25.

**Case 2: married couple with two children, basis year 2026 compared with 2025.**
- Facts: both spouses are EU nationals and file jointly. Their children, aged 10 and 14, live with them. Chargeable income is €40,000.
- 2026, table (a)(iii): €40,000 × 25% − €6,575 = €3,425.
- The same income in 2025, married table: €40,000 × 25% − €4,550 = €5,450.

**Case 3: part-time self-employed.**
- Facts: a full-time employee, registered with Jobsplus, also does part-time design work for other clients. The work is registered and has no employees. Net profit in 2026 is €15,000.
- Final tax: €12,000 × 10% = €1,200, paid by 30 April 2027 with the statement of accounts.
- The excess €3,000 goes into the 2026 return at progressive rates.

**Case 4: residential let on the 15% option.**
- Facts: a two-bedroom flat is let for all of 2026 on a registered five-year long private residential lease, at €18,000 a year.
- Tax: €18,000 × 15% = €2,700, less the €400 rebate = €2,300, due by 30 April 2027.
- The rebate is within its cap (15% of rent = €2,700).

**Case 5: property sale.**
- Facts: a flat bought in 2010 and never the seller's residence is sold in 2026 for €300,000.
- Tax: 8% × €300,000 = €24,000, withheld through the notary.
- If it had been bought in 2002: 10% × €300,000 = €30,000.
- If it had been the seller's own residence for three years and sold within 12 months of vacating: no tax.

**Case 6: provisional tax.**
- Facts: the self-assessment for year of assessment 2025 (the last return due before 2026) shows €5,000 of tax payable after adding back provisional tax.
- 2026 instalments: €1,000 by 30 April (20%), €1,500 by 31 August (30%) and €2,500 by 21 December (50%).

**Case 7: non-dom minimum tax.**
- Facts: an ordinarily resident, non-domiciled individual, taxed on the remittance basis and not in a minimum-tax scheme, has €50,000 of foreign income, none of it remitted, and €1,200 of Malta tax on Malta income.
- Foreign income is at least €35,000, so total tax must reach €5,000.
- Shortfall: €5,000 − €1,200 = €3,800, unless the person proves that tax on their worldwide income would be lower.

**Case 8: late return and late payment.**
- Filing: the return for year of assessment 2026 is filed eight months after 30 June 2026. Additional tax is €50 (later than 6 but within 12 months).
- Payment: if €2,000 of tax is paid five months late, interest is €2,000 × 0.6% × 5 = €60, capped at the tax.

## When to refuse or refer

- Refuse to pick a rate table without marital status, children's ages, custody or maintenance, and nationality or long-term resident status.
- Refer non-residents, part-year residents and dual residents, and all double tax relief claims.
- Refer the special schemes (Global Residence Programme, Residents Scheme, returning migrants, highly qualified persons) and anyone taxed at the article 56(11) flat rate.
- Refer disputed domicile or ordinary residence.
- Refer property transfers involving projects, companies, trusts, special designated areas, intra-group transfers or share transfers.
- Refer companies, partnerships and group structures.
- Refer arrears, enquiries, assessments and objections, and any omission already under enquiry.
- Refer the €10,270 table where the €5 difference matters, until MTCA confirms it. ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))
- Refer any question that turns on an MTCA notice you cannot see, such as an online-filing extension.

## Filing and payment ([Income Tax (Statutory Dates) Rules, S.L. 372.16](https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2))

| Item | Date or rule | Source |
| --- | --- | --- |
| Individual return and self-assessment | 30 June of the year of assessment (30 June 2027 for 2026 income) | S.L. 372.16 rule 2(c)(ii) |
| Balance of tax (tax settlement date) | Same date as the return | S.L. 372.16 rule 5(b) |
| 2025 income (year of assessment 2026) | Was due 30 June 2026. MTCA usually announces a later date for online filing; check the notice on mtca.gov.mt | S.L. 372.16 |
| Article 12 election (no return) | 30 April of the year of assessment | S.L. 372.16 rule 4(b) |
| Part-time self-employed tax | 30 April after the basis year | ITMA art. 42(4)(a) |
| 15% rental tax | 30 April after the basis year | ITMA art. 42(4)(c) |
| Provisional tax | 30 April, 31 August and 21 December of the basis year | S.L. 372.18 rule 4 |
| Interest on late tax | 0.6% for each month or part month, where the tax was payable on or after 31 August 2022; capped at the tax | ITMA art. 44(2A) |
| Late return, individuals (Table A) | €10 within 6 months; €50 within 12; €100 within 18; €150 within 24; €200 within 36; €300 within 48; €400 within 60; €500 after 60 months | ITA Schedule, item 2 |
| Omission from a return | 1.5% a month of endangered tax, for at most 60 months. Fully remitted if corrected within 12 months of the return date and before an enquiry notice. Otherwise 0.1% a month if corrected before an enquiry notice, or 0.75% a month after the notice but before assessment. No interest runs on this additional tax | ITA Schedule, items 5-9 |

Late-return additional tax can be remitted for a reasonable excuse. Insufficient funds and reliance on another person do not count (Schedule, item 4). Omission additional tax can be remitted in two cases: written advice from a tax professional was submitted with the return, or there was no fraud or gross neglect (item 8).

## Completion checklist ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- The basis year and year of assessment are stated, with the rate table for that year (Act IX of 2025 or Act III of 2026).
- Residence, domicile and ordinary residence are recorded. For a non-dom, the remittance basis and the €35,000 / €5,000 minimum tax test are applied.
- Every condition of the chosen table is checked, including nationality or Malta-born children for the child tables.
- Final-tax income (part-time work, 15% rent, property transfers) is kept out of the progressive computation, or the opt-out is recorded.
- Expenses meet article 14(1) and are not barred by article 26. Capital items go through S.L. 123.01 allowances, not expenses. Class 2 is a memo only.
- FSS tax, provisional tax and final-tax credits are reconciled to the statements of earnings and payment records.
- Next year's provisional tax is set from the benchmark, with a reduction form filed if the liability will fall.
- Dates are checked: 30 April items, the 30 June return, and the 31 August and 21 December instalments. Any MTCA extension is confirmed on mtca.gov.mt.
- Interest and additional tax are computed for anything late.
- The output is labelled as an estimate until reviewed.

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
