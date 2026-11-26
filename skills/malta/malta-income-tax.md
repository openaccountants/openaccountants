---
name: malta-income-tax
description: "Use this skill whenever asked about Malta income tax for self-employed individuals. Trigger on phrases like \"how much tax do I pay\", \"income tax return\", \"self-assessment\", \"allowable deductions\", \"capital allowances\", \"provisional tax\", \"TA22 regime\", \"TA24\", \"chargeable income\", \"tax credits\", \"self-employed tax Malta\", or any question about filing or computing income tax for a self-employed or part-time self-employed client. Also trigger when preparing or reviewing the annual income tax return or a TA22, computing deductible expenses, or advising on provisional tax instalments. NOTE: TA24 is the 15% final tax form for RENTAL income (ITA Art. 31D) ; if the user means rental income, see the Rental income section; the self-employed annual filing is the personal Income Tax Return. This skill covers tax rates (single/married/parent), the return working-paper structure, allowable deductions, capital allowances, provisional tax, the TA22 part-time regime, penalties, and interaction with VAT and SSC. ALWAYS read this skill before touching any income tax work."
version: 2.4
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 1
reviewed_by: Michael Cutajar
reviewed_on: 2026-11-15
domain: income-tax
type: computation
---

# Malta personal income tax: rates, residence, final taxes, provisional tax and filing

## Scope

This skill covers Malta income tax for **individuals**: employees, the self-employed, part-time workers, landlords and people selling Maltese property. Malta taxes a calendar **basis year**, and the tax is charged for the following **year of assessment**.

- **Basis year 2026 = year of assessment 2027.** This is the primary year of this skill. Its return is due by 30 June 2027.
- **Basis year 2025 = year of assessment 2026.** The dated section “2025 income (year of assessment 2026)” preserves that earlier-year computation. The general statutory date was 30 June 2026, but MTCA extended filing and payment to 31 July 2026 (see "Filing and payment").

Marital and family status is tested "in the year immediately preceding the year of assessment", which means the basis year itself.

**Source scope.** The whole Guide was audited on 26 November 2026. Operative rate/status, part-time, FSS/no-return and statutory-date sources were read; completed same-day SSC, provisional-tax, rental, deductions and property source reads were reused after checking their applicability. Unresolved specialist positions below are non-usable referrals, not instructions to claim relief.

**Not covered:** companies and partnerships, a full non-resident computation, the special residence programmes (Global Residence Programme, Residents Scheme, and the Highly Skilled Individuals Rules, [L.N. 20 of 2026](https://legislation.mt/eli/ln/2026/20/eng/pdf), effective from 1 January 2026 with rule 12 transitional provisions for existing beneficiaries, rather than automatic cancellation of every legacy benefit), double tax relief, VAT (see the Malta VAT Guide) and the detail of social security contributions.

## Ask the client first

- Which basis year? 2026 income (year of assessment 2027) uses the Act III of 2026 tables, which add four child categories. 2025 income (year of assessment 2026) uses only the three Act IX of 2025 tables.
- Residence: were you resident in Malta in that year? Domicile: are you domiciled in Malta, and are you ordinarily resident here? If not domiciled, how much foreign income arose, and how much of it was brought into Malta?
- Were you married and living together in that year? Do you file jointly (the default), separately (article 49A), or with a separate computation (article 50)?
- Children: how many, and how old? Each must be not over 18, or not over 23 and in full-time education. Did you have custody, or did you pay maintenance under article 12(1)(t)? Is either spouse an EU/EEA national or a long-term resident? If not, was each child born in Malta and resident in Malta?
- Single parent: did you have sole custody, receive the children's allowance as sole beneficiary, get no maintenance from the other parent, and live apart from them?
- What kinds of income: employment (FSS), self-employment (full-time or part-time), rent, dividends or interest, foreign income, or a property sale?
- Part-time work: were you in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice? Is the part-time work registered with Jobsplus and done for a different employer?
- Rent: is the property residential or a garage, or commercial? Is the tenant related to you? Is the lease registered as a long private residential lease?
- Provisional tax: what does your provisional tax statement show, and what have you paid?
- Were any returns or payments late?

## The method, step by step

1. **Fix the year.** Take the basis year of the income and add one to get the year of assessment. Status, custody and residence are all tested in the basis year.
2. **Decide residence and domicile.** A resident individual is taxed under article 56(1)(a) or (b). A non-resident uses the article 56(1)(c) scale unless an EU/EEA proviso applies. A resident who is not domiciled, or not ordinarily resident, can qualify for the article 4 remittance treatment only if its permanent-status/spouse exclusions do not apply. Establish actual foreign source and income/capital classification before applying it. Then test the €5,000 minimum tax for non-doms (article 56(27)). ([ITA art. 4 and 56](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
3. **Take out income taxed at a final rate.** This means part-time work (10%), rent where the 15% option is chosen, property transfers under article 5A, and final-withholding investment income. Each regime has its own election/mandatory-treatment rule: do not assume all final taxes can be opted back into progressive rates. Part-time opt-out is described below; property article 5A tax is ordinarily final, and separate-return spouses have special rental rules. ([ITA art. 90A, 31D, 5A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
4. **Compute business profit.** Deduct outgoings "wholly and exclusively incurred in the production of the income" (article 14(1)). Remove anything barred by article 26: private or domestic spending, capital spending, improvements, recoverable amounts and voluntary payments. Apply capital allowances under the Wear and Tear Rules (S.L. 123.01), including same-source profit and cumulative-cost limits.
5. **Add the other income taxed at progressive rates.** This is employment income, rent where the 15% option is not taken (net of the S.L. 123.26 deductions), and any part-time income over its cap. Reconcile the applicable total and statutory deductions/allowances to reach chargeable income; do not claim every personal relief as a business expense. ([ITA art. 90A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))
6. **Pick the rate table** for the basis year and status, then apply: chargeable income × rate − subtraction. A table does not apply unless every one of its conditions is met.
7. **Credit tax already paid.** This means FSS tax deducted by employers, provisional tax, and part-time tax paid on income the person opted to declare. The balance is due on the tax settlement date, normally the individual return date; article 12 electors have the prescribed notice-based settlement rule, and companies are outside this Guide.
8. **File the return** by 30 June of the year of assessment. Pay the final taxes and file their statements by their own dates, most of them 30 April.
9. **Add interest and additional tax** for anything late. For tax due on/after 31 August 2022, interest is 0.6% per month or part capped at tax, subject to article 44(2B) exceptions (specified FSS collection direction, additional tax, mutual-agreement procedure) ([ITMA art. 44(2A)](https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b)). Late-return additional tax follows Table A ([ITA art. 56(12)(c) and Schedule, item 2](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c)).
10. **Set up next year's provisional tax.** The benchmark comes from the specified benchmark year, normally the basis year two years before the payment year. Ordinary payments 20%/30%/50% are due 30 April/31 August/21 December, rounded to nearest euro. Increased benchmarks need cumulative catch-up, and a late benchmark return can revise earlier instalments. A reduction requires a prescribed statement by the relevant instalment date, with underestimation consequences. See `mt-estimated-tax`. ([P.T. Rules](https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4))

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
| Parent, 1 qualifying child, art. 56(1)(b)(iv) | €14,500 | over €14,500 and under €21,000 (€2,175) | over €21,000 and under €60,000 (€4,275) | over €60,000 (€10,270; MTCA's table shows €10,275) |
| Parent, 2 or more qualifying children, art. 56(1)(b)(v) | €18,500 | over €18,500 and under €25,500 (€2,775) | over €25,500 and under €60,000 (€5,325) | over €60,000 (€11,325) |

**Parent with one qualifying child above €60,000: use €10,270, the figure in the Act.** Act III of 2026, article 19, sets the subtraction in article 56(1)(b)(iv) at **€10,270**, and the consolidated Act prints the same figure. MTCA's amended 13 April 2026 communication and its current 2026 table publish **€10,275**. The Act is the law, so compute with €10,270. Tell the user that MTCA's table shows €10,275: the Act's figure gives €5 more tax at every income in this band, and €10,275 is the figure that joins the 25% and 35% bands at €60,000. Act III of 2026 and the consolidated Act were read again on 26 November 2026. [Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430); [Consolidated Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c); [MTCA amended table](https://mtca.gov.mt/docs/default-source/documents/2026-tax-rates.pdf?sfvrsn=37563fb2_5).

### Who gets which table ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Married tables** (article 56(1)(a)) apply to a married couple resident in Malta and taxed jointly under article 49. If either spouse elected a separate return (article 49A), or the responsible spouse opted for a separate computation (article 50), each spouse uses the article 56(1)(b) tables instead. An EU/EEA national whose spouse is not resident can still use the married tables if the Commissioner is satisfied that at least 90% of the couple's worldwide income is from Malta.
- **Parent table** (article 56(1)(b)(ii)): the individual was a parent who kept a child in custody, or paid maintenance for the child under article 12(1)(t). The child must be not over 18, or not over 23 if in full-time education.
- **Qualifying-child tables** (married (ii) and (iii), parent (iv) and (v)) need **all** of the following:
  - for the married tables (a)(ii) and (a)(iii), the couple kept the child (or the two children) in their custody. Maintenance does not count for these tables (article 56(1)(a)(ii)(A) and (iii)(A));
  - for the parent tables (b)(iv) and (b)(v), the individual kept the child in custody (their own child, a spouse's child or a certified cohabitant's child) or paid maintenance for their own child under article 12(1)(t) (article 56(1)(b)(iv)(A) and (v)(A));
  - the same age test;
  - a spouse, the individual, or the individual's spouse must be an EU/EEA national or hold long-term resident status;
  - if nobody is an EU/EEA national, the child (or each of the two children) must have been born in Malta and be resident in Malta.
  
  If any condition fails, fall back to the married (i) or parent (ii) table.
- **Single parent with sole custody** (article 56(1)(b)(iii)) is taxed on the **married** table (a)(i), unless table (iv) or (v) gives a better result. The person must have been unmarried, widowed, separated or divorced, and must have met all four conditions:
  - wholly maintained, in sole custody, a child whose own income was not over €3,400. The child must be not over 18; or not over 23 and in full-time education or serving an apprenticeship; or incapacitated by infirmity. This rule has no nationality or born-in-Malta test;
  - where a children's allowance is payable, recognised by the Director General (Social Security) as its sole beneficiary;
  - no maintenance from the other parent;
  - not living with the other parent.

Article 49A separate-return elections require both spouses' qualifying trade/employment/past-employment pension income or the specified public-deed marital property system, the prescribed form and an effective election (normally the following assessment year). Revocation has its own joint-notice and five-year re-entry restriction. Article 50 covers specified active/past-employment-pension income, normally aggregates other income with the higher active-income spouse, excludes benefit-only cases and cannot run with an effective 49A election. These are different methods; unresolved eligibility/allocation/election timing: Check this point with one of our partner accountants.

### 2025 income (year of assessment 2026) ([Act IX of 2025](https://legislation.mt/getpdf/6811d803cf7b7f36a4f360f5))

Act IX of 2025, article 15, set these tables. Its article 10(2)(a) makes them "applicable as from the year of assessment 2026". The four qualifying-child tables do **not** apply to 2025 income.

| Status (basis year 2025) | 0% up to | 15% band (subtract) | 25% band (subtract) | 35% above (subtract) |
| --- | --- | --- | --- | --- |
| Single | €12,000 | €12,000 to €16,000 (€1,800) | €16,000 to €60,000 (€3,400) | over €60,000 (€9,400) |
| Married, joint | €15,000 | €15,000 to €23,000 (€2,250) | €23,000 to €60,000 (€4,550) | over €60,000 (€10,550) |
| Parent | €13,000 | €13,000 to €17,500 (€1,950) | €17,500 to €60,000 (€3,700) | over €60,000 (€9,700) |

The sole-custody single-parent rule quoted above is taken from the text that applies from year of assessment 2027. A 2025 sole-custody claim requires the historical operative conditions: Check this point with one of our partner accountants. Do not automatically transplant the 2026 wording.

### Non-residents ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

An individual not resident in Malta in the basis year pays tax under article 56(1)(c):

- 0% on the first €700;
- 20% on the next €2,400;
- 30% on the next €4,700;
- 35% on the remainder.

An EU/EEA national may use paragraph(b) tables if the Commissioner is satisfied at least 90% of worldwide income is Malta-derived; married paragraph(a) rates additionally require its conditions and 90% of the couple's worldwide income. Associated resident exemptions/deductions/credits/refunds then apply. Otherwise the statutory worldwide-income-proportion cap may apply. Actual computation/source/treaty facts: Check this point with one of our partner accountants.

## Residence, domicile and the remittance basis ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Resident** (article 2): "an individual who resides in Malta except for such temporary absences as to the Commissioner may seem reasonable". This definition itself supplies no fixed day count. Article 13 has a separate temporary-purpose/no-residence-intent/six-month provision, so do not claim the whole Act has no time test. Actual residence, domicile or ordinary-residence application: Check this point with one of our partner accountants.
- **Remittance basis** (article 4(1), provisos (i) and (ii)): a person who is not ordinarily resident **or** not domiciled in Malta is taxed on foreign income only "on the amount received in Malta". Foreign capital gains are outside the charge only if the provisos apply; determine source/classification and exclusions first.
- **Exceptions:** provisos (i) and (ii) do not apply from the year of grant and subsequent years to the specified long-term resident or holder of a permanent residence certificate/card under the named legislation. Nor do they apply to an individual "whose spouse is ordinarily resident and domiciled in Malta".
- **Minimum tax for non-doms** (article 56(27)) applies to an individual who meets all of these:
  - ordinarily resident but not domiciled, and taxed on the remittance basis;
  - not under a minimum-tax scheme;
  - foreign income **not less than €35,000** (a married couple taxed under article 49 counts both spouses' foreign income), not received, or not fully received, in Malta.

  Their tax is "not less than €5,000" a year. For this comparison use Malta income tax before relief under articles 74–94, excluding article 5A tax and including Malta tax withheld at source. If the individual proves to the Commissioner's satisfaction a lower worldwide-basis liability, that lower amount applies. Foreign capital gains/source/remittance treatment is not proved merely by an offshore account or transferring sale proceeds.

## Part-time work final tax ([Income Tax Act art. 90A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Who qualifies** (Part-time Work Rules, S.L. 123.39, rule 2): a person resident in Malta who has one of these:
  - full-time employment registered with Jobsplus;
  - a pension taxable in Malta;
  - full-time education or an apprenticeship.

  Article 90A(9) extends this to a spouse living with a qualifying spouse. The extension applies only without an effective article 49A separate-return election. If entitlement depends on the extension, rule 3(2) excludes income from the specified spouse/adoptive child/ascendants/descendants/their spouses/siblings/their spouses and companies in which the individual or those persons are direct/indirect shareholders.
- **Rate:** 10% from year of assessment 2023 (article 90A(11)). Before that it was 15%. The tax is final, and the income is not declared in the return.
- **Caps** (rule 3(2)): the rate covers self-employed profit (article 4(1)(a)) up to €12,000, and part-time employment income (article 4(1)(b)) up to €10,000. Any **excess** is declared in the return at normal rates.
- **Conditions for the self-employed** (rule 4). All of these are required:
  - the part-time work is registered with Jobsplus;
  - no more than two employees, both part-time;
  - proper books are kept;
  - the work is done for someone other than the full-time employer; rule 6 treats companies controlled and beneficially owned more than 50% by the same shareholders as one employer, and specified controlled Government entities likewise;
  - the person is registered for VAT, unless not required to register or exempt.
- **Part-time employment:** the work must be registered with Jobsplus, done for a different employer, and not more than 30 hours per week unless the applicable wage regulation order treats that as full time; special police extra-duty exceptions apply. Employment benefits and specified Government office/board/director fees are excluded by rules 3(3)/6(2). The employer deducts qualifying tax under article 90A(7)(a); low-income FS4 directions have their own conditions.
- **Paying as a self-employed part-timer:** pay the tax by **30 April** of the year after the income was earned. Include a statement of accounts showing taxable net profit (ITMA article 42(4)(a)). MTCA identifies the service as TA22. Payment alone does not establish eligibility; keep the complete approved statement.
- **Opting out:** the person may declare all part-time income in the return at progressive rates. Any final tax already paid is then credited or refunded (article 90A(2)).
- **Risks:** if the tax is unpaid by the due date and an article 13(7) written enquiry notice is received, **all** the part-time income is taxed at progressive rates (article 90A(8)). The Commissioner can also refuse the regime if the work is really the person's normal activity or ancillary to it (article 90A(10)).

## Rental income: the 15% option ([Income Tax Act art.31D](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- **Qualifying rent:** a tenement is a dwelling/part occupied or to be occupied as a home, or a garage. A commercial tenement/club is excluded when let to/from a related body of persons under article 31D(8); the related-company residential rule requires actual dwelling use. Establish rights, tenant, purpose and relatedness; see `mt-rental-income`.
- **Tax:** optional 15% of qualifying gross rent received, no expense deduction, credit/set-off/refund; excluded from progressive income when validly final-taxed. The election for a year applies to all the person's qualifying tenements, not a choice property by property (31D(2)–(4)). Article 49A(5) can deem a separately filing spouse to elect final rent tax unless other chargeable income, excluding the specified rental/investment income, is at least the applicable zero-rate band. Check this point with one of our partner accountants for unresolved election scope.
- **Undeclared rent:** article 31D(5) applies 35% of gross plus applicable charges where the person omitted rent from a return or statement required for that rent and an article 13(7) enquiry identifies it; this is not a general alternative rate.
- **Payment:**30 April following the receipt year with the prescribed statement; MTCA identifies TA24. No future online return extension is inferred.
- **Long-let rebate:** S.L. 123.201 rules 3–10 require a valid article 31D final-tax election, registration as a long private residential lease and a qualifying term. At least 2 butunder 3 years: EUR 200/300/400 for 1/2/3+ bedrooms; at least 3 years: EUR 300/400/500. The maximum is 15% of that lease's rent, with first/last-year pro-rata. Early termination, joint interests, actual rebate rounding and other eligibility details: Check this point with one of our partner accountants; see `mt-rental-income`.
- **Progressive rent:** S.L. 123.26 prescribes interest on income-producing capital; rent/ground rent/similar burden; applicable tourism-licence fee; and 20% of rent after those rent/ground-rent burdens and licence fee, before interest. Exclude duplicate deductions; the 20% does not apply to emphyteutical concessions. The text still cross-refers to repealed 4(1)(f), while current rent is 4(1)(e); MTCA's rental manual expressly applies these deductions. Work per property without a negative taxable-rent amount. See `mt-rental-income`; unresolved contractual receipt/deduction/rounding: Check this point with one of our partner accountants.

## Selling property in Malta: the article 5A final tax ([Income Tax Act art. 5A](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

The tax is ordinarily charged on the **transfer value**, with the special twelve-percent excess-over-acquisition-value rule described below. It is paid through the notary on the deed and is final.

| Transfer (made on or after 1 January 2015) | Rate | Provision |
| --- | --- | --- |
| Ordinary post 2015 rule, subject to other 5A(5) rates and historical project/SDA promise-notice provisos | 8% of transfer value | 5A(5)(a), proviso  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Property acquired before 1 January 2004 (no promise of sale notified before 17 November 2014) | 10% of transfer value | 5A(5)(f)  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Not part of a project, sold within five years of acquisition, subject to related-owner/development-work conditions below | 5% of transfer value | 5A(5)(e)  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| An individual (or two co-owners) declared in the deed of acquisition that it was bought as their sole ordinary residence; the transfer is within three years of acquisition; and at the transfer they own no other residential property (declared to the notary) | 2% of transfer value | 5A(5)(g)  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Inherited after 24 November 1992 (except the judicial-auction limb below), or qualifying donation older than 5 years |12% of positive transfer-value excess over statutory acquisition value; election-out and donation/project exceptions require analysis | 5A(5)(b)  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |
| Inherited before 25 November 1992, or inherited on/after then and transferred by judicial auction |7% of transfer value | 5A(5)(c)  [Income Tax Act](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c) |

The 5% rate is lost in two cases. The first is where a related person owned the property as part of a project in the previous five years. The second is where works needing a development permit were done in those five years, subject to the acquisition-deed sole-ordinary-residence intention exception, and the exclusion of works permitted by an order without an application. Test the transferor and related persons, not just works by the current owner; acquisition-history deeming rules also apply. Special donation/old-project/SDA/election-out cases: Check this point with one of our partner accountants.

**No tax** is due (article 5A(4)) in these cases, among others:

- **Own residence:** a dwelling house, not part of a project, that meets all of these:
  - owned and occupied as the transferor's own residence for at least three consecutive years immediately before the transfer;
  - sold within 12 months of vacating it;
  - declared by election to the Commissioner as the main residence in the prescribed manner.

  The specified period during which a spouse/direct ascendant owned and occupied an inherited house counts as the heir's ownership; it does not automatically count as the heir's occupation. Part-property relief, altered use and the main-residence election require the operative conditions. For a qualifying three-year spousal residence followed by divorce/separation, the special vacating rule can depend on when the other spouse leaves. Check this point with one of our partner accountants for any unresolved condition.
- **Donations** to a spouse, a descendant or ascendant (or their spouse), or, where there are no descendants, to a sibling or a sibling's descendant.
- **Transfers between spouses** on separation or divorce, or when the community of acquests is dissolved.

The table is conditional, not a final rate selection. For projects, companies, trusts, special designated areas, acquisition-value calculations or any unproved exemption/rate condition: Check this point with one of our partner accountants. Use `mt-property-transfer-tax-the-sale-immovable` for the complete transfer workflow.

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
- **Entertainment:** record purpose/evidence/private element; no blanket deduction or prohibition follows from the label. Check this point with one of our partner accountants.
- **Social security Class 2:** record payments separately; this Guide does not prove either a deduction or a statutory prohibition. Check this point with one of our partner accountants before adopting their tax treatment.
- **Capital allowances** (article 14(1)(f), S.L. 123.01):
  - straight line, over at least the minimum number of years;
  - a full-year allowance under rule 7(a) only where part-year production use is solely due to acquisition/completion; listed disposal events before the last day give no annual allowance, while last-day cases require separate analysis;
  - only where proper records of cost are kept;
  - reduced to the business-use share;
  - unused allowances carry forward against the same source where its profits are insufficient;
  - total allowances cannot exceed original cost;
  - industrial buildings or structures get at most 2% of cost a year, excluding land. Article 14(1)(j)also specifies one-tenth initial expenditure in first-use year, with source-profit/cost limits. Classification and the actual industrial-building computation: Check this point with one of our partner accountants;
  - cars and other vehicles for transporting people (S.L. 123.07 rule 3, [Income Tax (Deductions) Rules](https://legislation.mt/getpdf/66f65d8f3b56613c3cae68d9)): if the car cost more than €14,000, compute wear and tear, any initial deduction and the article 24 balancing allowance or charge as if it cost €14,000. For a leased car with a listed price over €14,000, the deductible lease payments are capped at lease payments × €14,000 ÷ listed price. Apply the business-use share after the cap. The rule excludes unsuitable private vehicles and those wholly/mainly for public hire/carriage or ordinary-course driving instruction. Lease wear-burden/short-use/replacement rules apply; actual lease or excluded-vehicle case: Check this point with one of our partner accountants;
  - a sale/scrapping may require an article 24 balancing statement; actual event/source continuity/history/amount/limits: Check this point with one of our partner accountants. Related-party/non-onerous acquisitions and use by a non-owner bearing wear have their own rules 8–10.

| Asset (S.L. 123.01 Schedule) | Minimum years |
| --- | --- |
| Computers and electronic equipment; computer software | 4 |
| Motor vehicles; other machinery | 5 |
| Catering equipment; air-conditioners; medical equipment | 6 |
| Furniture, fixtures, fittings and soft furnishings; other plant | 10 |
| Electrical and plumbing installations and sanitary fittings | 15 |

## Provisional tax for the self-employed ([Payment of Provisional Tax Rules, S.L. 372.18](https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4))

- **Who pays:** an individual who was liable to tax in the benchmark year under the rules. This excludes anyone eligible for the article 12 election not to file, typically an employee whose income was all under FSS.
- **Benchmark:** the tax payable in the self-assessment for the benchmark year, adding back any provisional tax. The benchmark year is the last year of assessment whose return was due before the calendar year of the first payment. The benchmark is never this year's projected income. If the benchmark-year self-assessment is absent, use the applicable Commissioner determination; absent that, rule 7 can fall back to an earlier self-assessment before nil. Do not assume nil solely because one return is missing.
- **Due dates** (rule 4) and amounts (rule 5), all in the basis year:
  - at least 20% of the benchmark by 30 April;
  - a further 30%by 31 August (cumulative 50%using any increased benchmark);
  - a further 50% by 21 December (cumulative 100%using any increased benchmark). Round payments to nearest euro; late-return benchmark revisions may retrospectively affect each instalment.
- **Reduction** (rule 10): if this year's liability will be lower than the benchmark, submit the prescribed reduction statement by the relevant instalment date. The estimate must meet rules 10–12; later reduction does not erase earlier default. See `mt-estimated-tax` for appropriation/catch-up/underestimation.
- **Late provisional tax** (rule 14): additional tax of 0.6% for each month or part month, for periods from 1 June 2022. If the final self-assessment tax is below the benchmark, the additional tax on the difference is cut by 90%. The charge stops at the tax settlement date, has the rule 14 cap and payment-first appropriation conditions; see `mt-estimated-tax`.

## Employees: the Final Settlement System ([FSS Rules, S.L. 372.14](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3))

- The employer deducts tax each pay period using the cumulative formula, normally required unless MTCA directs otherwise; payers with fewer than ten “full-time payees” as defined by the Main method can opt for Main Tax Deduction Tables, without using both methods concurrently. The table depends on the employee's tax status declaration (form FS4) and the length of the pay period. A year-end adjustment in the final pay period applies article 56 rates only where the payer has complete computation data, including earlier Main-source FS3s where relevant; it does not establish the employee's complete non-payroll liability.
- The employer gives the employee the Payee Statement of Earnings (commonly FS3) by **31 January** of the following year, or within seven days of earlier termination subject to rule 28. The employer files its annual reconciliation statement by **15 February** (rules 21 and 22).
- **Eligibility for election not to file** (ITMA article 12), subject to a signed prescribed declaration, required particulars/documents and delivery by 30 April:
  - a resident individual whose income was **all** taxed at source under FSS and fully reported in statements of earnings held in the individual's possession;
  - a resident individual with no business income whose total income did not exceed the 0% band.

  Married living-together spouses are tested together unless article 49A separate returns are effective. An article 12 election deems optional income undisclosed and, where eligible, the more advantageous article 50 computation. Article 12A separately permits a written MTCA no-return notice; higher undisclosed income than shown requires a return. MTCA can still require a return. Article 31(2A) permits an adjustment form within ten years of notification of a determination under 31(1)/(2); filing after three months changes the repayment-interest trigger. Other correction/assessment procedures differ. Check this point with one of our partner accountants for unresolved notice/election/adjustment facts.
- From 1 January 2025, tax paid through FSS on income left out of a return does not count as "endangered tax" for the omission penalty (Schedule, item 1, as amended by Act IX of 2025).

## Social security Class 2 (summary only) ([Social Security Act, Cap. 318](https://legislation.mt/eli/cap/318/eng))

Self-occupied persons pay Class 2 contributions under the Social Security Act, Cap. 318, not the Income Tax Act. Their deductibility is an unresolved referral above, not a proven prohibition. For rates, caps, and the position of someone who is both employed and self-occupied, use the Malta social security Guide ; any unresolved liability: Check this point with one of our partner accountants.

## Boundary and exception table ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

| Situation | Treatment |
| --- | --- |
| Chargeable income exactly at a band edge (e.g. €16,000 single) | The Act says "exceeds ... but is less than". Both formulas give the same tax at the edge (single: €600) |
| Married couple, no EU/EEA national, child born abroad | New qualifying-child table birth/residence test fails; establish eligibility for ordinary married or other lawful table |
| Child aged 22 in full-time university study | Qualifies (not over 23 and in full-time education) |
| Child aged 20, working full-time | Does not qualify (over 18 and not in education) |
| Part-time self-employed profit of exactly €12,000 | All at 10%. Nothing is over the cap |
| Part-time work for a company owned more than 50% by the same shareholders as the full-time employer | Counts as the same employer, so the 10% regime is not available (rule 6(1)(a)) |
| Rent from a commercial tenement let to a related company |15% exclusion only after statutory relatedness and tenement use established; see rental section |
| Non-dom with €34,000 of foreign income not remitted | Below €35,000, so no minimum tax |
| Own home sold 13 months after moving out |Ordinary 12-month vacating condition not met; no automatic 8%/5%/10% selection. Check this point with one of our partner accountants |
| Provisional tax paid on 1 May | Late: 0.6% additional tax for that month |

## Worked cases

The amounts in these cases are invented. The rates come from the sources linked in the sections above.

**Case 1: single, self-employed, basis year 2026.**
- Facts: gross fees €45,000; allowable expenses €13,000; a laptop costing €1,500, written off over 4 years at €375 a year; Class 2 paid €3,000 (tax treatment unresolved separately); provisional tax paid €3,500.
- Conditional working paper: assume documented qualifying laptop use/acquisition, sufficient same-source profits, no prior/related-party allowance limit, and no Class 2 deduction in this illustration. This does not resolve the actual Class 2 position. Net profit €32,000 less €375 gives €31,625.
- Tax: €31,625 × 25% − €3,400 = €4,506.25.
- Balance due by 30 June 2027: €4,506.25 − €3,500 = €1,006.25.

```oa-check
name: Case 1, single self-employed, basis year 2026
inputs:
  fees: 45000
  expenses: 13000
  laptop_cost: 1500
  provisional_paid: 3500
steps:
  - wear_and_tear: laptop_cost / 4
  - chargeable: fees - expenses - wear_and_tear
  - tax: chargeable * 0.25 - 3400
  - balance_due: tax - provisional_paid
expected:
  chargeable: 31625
  tax: 4506.25
  balance_due: 1006.25
```

**Case 2: married couple with two children, basis year 2026 compared with 2025.**
- Facts: both spouses are EU nationals and file jointly. Their children, aged 10 and 14, live with them. Assume Malta residence and maintenance under their custody in each relevant year; all qualifying conditions are established. Chargeable income is €40,000.
- 2026, table (a)(iii): €40,000 × 25% − €6,575 = €3,425.
- The same income in 2025, married table: €40,000 × 25% − €4,550 = €5,450.

```oa-check
name: Case 2, married with two children, 2026 table (a)(iii) against the 2025 married table
inputs:
  chargeable: 40000
steps:
  - tax_2026: chargeable * 0.25 - 6575
  - tax_2025: chargeable * 0.25 - 4550
  - saving: tax_2025 - tax_2026
expected:
  tax_2026: 3425
  tax_2025: 5450
  saving: 2025
```

**Case 3: part-time self-employed.**
- Facts: a full-time employee, registered with Jobsplus, also does part-time design work for other clients. The work is registered and has no employees. Net profit in 2026 is€15,000. Assume all residence, activity, proper-books, VAT, employee and different-employer conditions are met.
- Final tax: €12,000 × 10% = €1,200, paid by 30 April 2027 with the statement of accounts.
- The excess €3,000 goes into the 2026 return at progressive rates.

```oa-check
name: Case 3, part-time self-employed, 10% final tax capped at 12,000
inputs:
  profit: 15000
  cap: 12000
steps:
  - at_final_rate: min(profit, cap)
  - final_tax: at_final_rate * 0.10
  - excess_to_return: max(profit - cap, 0)
expected:
  final_tax: 1200
  excess_to_return: 3000
```

**Case 4: residential let on the 15% option.**
- Facts: a two-bedroom flat is let for all of 2026 on a registered five-year long private residential lease, at €18,000 a year.
- Assuming a valid article 31Doption, qualifying registered lease throughout the relevant year, correct rebate entitlement and no early-termination restriction:€18,000×15%=€2,700 less €400=€2,300, due 30 April 2027. See `mt-rental-income`; the assumed result does not establish joint-interest or rebate-rounding eligibility.
- The rebate is within its cap (15% of rent = €2,700).

**Case 5: property sale.**
- Facts: a flat bought in 2010 and never the seller's residence is sold in 2026 for €300,000.
- Assuming ordinaryarticle 5Acoverage, no exemption/specialrate/project/SDA/historicalpromise exception and€300,000 statutorytransfer value:8%×€300,000=€24,000 through the notary.
- If bought in 2002 and all 5A(5)(f)conditions apply, including no qualifying pre 17 November 2014 promise notice:10%×€300,000=€30,000.
- If the seller's own residence for three years and sold within 12 months of vacating, exemption is nil only with all 5A(4)(c)conditions, including qualifying dwelling/no-project/main-residence election. Check this point with one of our partner accountants for any unresolved condition.

**Case 6: provisional tax.**
- Facts: the self-assessment for year of assessment 2025 (the last return due before 2026) shows €5,000 of tax payable after adding back provisional tax.
- Assuming no revised/increased benchmark, reduction or credits altering amounts:2026 instalments€1,000 by 30 April(20%),€1,500 by 31 August(30%),€2,500 by 21 December(50%).

**Case 7: non-dom minimum tax.**
- Facts: an ordinarily resident, non-domiciled individual, taxed on the remittance basis and not in a minimum-tax scheme, has €50,000 of foreign income, none of it remitted, and €1,200 of Malta tax on Malta income.
- Assuming the permanent-status/spouse exclusions do not disapply remittance basis, the €1,200 is eligible pre-double-tax-relief Malta tax, noarticle 5A tax included and all 56(27)conditions met, the €35,000 threshold is exceeded and minimum €5,000 applies.
- Shortfall: €5,000 − €1,200 = €3,800, unless the person proves that tax on their worldwide income would be lower.

**Case 8: late return and late payment.**
- Filing: the return for year of assessment 2026 is filed eight months after the extended 31 July 2026 deadline. Additional tax is €50 (later than 6 but within 12 months).
- Payment: if €2,000 of tax is paid five months late, assuming exactly five chargeable calendar months/parts and no article 44(2B)exception, interest€2,000×0.6%×5=€60, capped at tax.

## When to refuse or refer

- Refuse to pick a rate table without marital status, children's ages, custody or maintenance, and nationality or long-term resident status.
- Refer non-residents, part-year residents and dual residents, and all double tax relief claims.
- Refer the special schemes (Global Residence Programme, Residents Scheme, returning migrants, and the Highly Skilled Individuals Rules, [L.N. 20 of 2026](https://legislation.mt/eli/ln/2026/20/eng/pdf), effective from 1 January 2026 with rule 12 transitional provisions for existing beneficiaries, rather than automatic cancellation of every legacy benefit) and anyone taxed at the article 56(11) flat rate.
- Refer disputed domicile or ordinary residence.
- Refer property transfers involving projects, companies, trusts, special designated areas, intra-group transfers or share transfers.
- Refer companies, partnerships and group structures.
- Refer arrears, enquiries, assessments and objections, and any omission already under enquiry.
- For a parent with one qualifying child above €60,000, compute with the Act's €10,270 and say that MTCA's table shows €10,275. ([Act III of 2026](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430))
- Refer any question that turns on an MTCA notice you cannot see, such as an online-filing extension.

## Filing and payment ([Income Tax (Statutory Dates) Rules, S.L. 372.16](https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2))


**Year-specific override, read 26 November 2026:** MTCA extended both manual and electronic individual returns for year of assessment 2026 (basis 2025), and the related tax payment, to **31 July 2026**. Use that actual date for late charges, not the general 30 June date. The statutory date for basis 2026 / assessment 2027 remains **30 June 2027** unless a later notice changes it. [MTCA notice, 3 June 2026](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline).

| Item | Date or rule | Source |
| --- | --- | --- |
| Individual return and self-assessment | 30 June of the year of assessment (30 June 2027 for 2026 income) | S.L. 372.16 rule 2(c)(ii) |
| Balance of tax (tax settlement date) | Normally return date; article 12 elector has prescribed notice-based date, not earlier than return date | S.L. 372.16 rule 5(a)–(b) |
| 2025 income (year of assessment 2026) | Filing and related payment extended to **31 July 2026**, both manual and electronic, by the MTCA 3 June 2026 notice | [MTCA notice, 3 June 2026](https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline) |
| Article 12 election (no return) | 30 April of the year of assessment | S.L. 372.16 rule 4(b) |
| Part-time self-employed tax | 30 April after the basis year | ITMA art. 42(4)(a) |
| 15% rental tax | 30 April after the basis year | ITMA art. 42(4)(c) |
| Provisional tax | 30 April, 31 August and 21 December of the basis year | S.L. 372.18 rule 4 |
| Interest on late tax | 0.6% for each month or part month, where the tax was payable on or after 31 August 2022; capped at the tax | ITMA art. 44(2A) |
| Late return, individuals (Table A) | €10 within 6 months; €50 within 12; €100 within 18; €150 within 24; €200 within 36; €300 within 48; €400 within 60; €500 after 60 months | ITA Schedule, item 2 |
| Omission from a return | 1.5% a month of endangered tax, capped at 60 times the applicable monthly rate. Fully remitted if corrected within 12 months of the return date and before an enquiry notice. Otherwise 0.1% a month if corrected before an enquiry notice, or 0.75% a month after the notice but before assessment. No interest runs on this additional tax | ITA Schedule, items 5-9 |

Late-return additional tax can be remitted for a reasonable excuse. Insufficient funds and reliance on another person do not count (Schedule, item 4). Omission additional tax can be remitted in two cases: qualifying original written professional advice submitted by the return date and not spurious/frivolous, or proven no fraud/art/contrivance/gross or wilful neglect. These are discretionary remission routes; complexity alone is insufficient (item 8).

## Completion checklist ([Income Tax Act, Cap. 123](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c))

- The basis year and year of assessment are stated, with the rate table for that year (Act IX of 2025 or Act III of 2026).
- Residence, domicile and ordinary residence are recorded. For a non-dom, the remittance basis and the €35,000 / €5,000 minimum tax test are applied.
- Every condition of the chosen table is checked, including nationality or Malta-born children for the child tables.
- Final-tax income (part-time work, 15% rent, property transfers) is kept out of the progressive computation, or a legally available opt-out is recorded; never assume all final-tax regimes permit one.
- Expenses meet article 14(1) and are not barred by article 26. Capital items go through S.L. 123.01 allowances, not expenses. Class 2 deductibility is an explicit referral, recorded separately pending resolution.
- FSS tax, provisional tax and final-tax credits are reconciled to the statements of earnings and payment records.
- Next year's provisional tax uses the statutory benchmark/rounding/catch-up, with a valid timely reduction statement where appropriate.
- Dates are checked: 30 April items, the 30 June return, and the 31 August and 21 December instalments. Any MTCA extension is confirmed on mtca.gov.mt.
- Interest and additional tax are computed for anything late.
- The output is labelled as an estimate until reviewed.

## Sources

Whole-Guide read 26 November 2026; completed same-day research reused only where the operative rule and applicability are unchanged. Source copies are tracked separately; no completeness assertion here.

| Source and passage actually read | URL | Read for on |
|---|---|---|
| Read for Cap 123 arts 2,4/13 residence,14/26 deductions,49–50 elections,56 all 2026 tables/minimum,90A; completed rental/property operative reads reused after applicability checks | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c|2026-11-26|
| Read for Act III 2026 arts 13(2)(b)/19: YA 2027 commencement and tables, including parent-one-child 10270 subtraction |https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430|2026-11-26|
| Read for Act IX 2025 arts 10(2)(a),15–16: YA 2026 tables and FSS endangered-tax exclusion |https://legislation.mt/getpdf/6811d803cf7b7f36a4f360f5|2026-11-26|
| Read for MTCA 2026 amended table including conflicting 10275 parent deduction; law 10270 retained, discrepancy disclosed |https://mtca.gov.mt/docs/default-source/documents/2026-tax-rates.pdf?sfvrsn=37563fb2_5|2026-11-26|
| Read for Cap 372 arts 12/12A/13,31(2A),42/44 and 19 records; completed same-day payment/source reads reused |https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b|2026-11-26|
| Read for Provisional Tax Rules whole 8 pages, completed same-day research applied |https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4|2026-11-26|
| Read for Statutory Dates Rules 2,4–5, completed personal-tax research applied |https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2|2026-11-26|
| Read for MTCA actual YA 2026 individual filing/payment extension operative body |https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline|2026-11-26|
| Read for Part-Time Work Rules2–10whole | https://legislation.mt/eli/sl/123.39/eng/pdf |2026-11-26|
| Read for MTCA part-time FAQ operative body: caps, excess and spouse amounts; not a substitute for statutory eligibility |https://mtca.gov.mt/personal-tax/individual/faqs/faqs1|2026-11-26|
| Read for rental deduction rule3 and rental rebate rules3–10, completed same-day rental research applicability confirmed |https://legislation.mt/eli/sl/123.26/eng/pdf ; https://legislation.mt/eli/sl/123.201/eng/pdf|2026-11-26|
| Read for MTCA rental manual relevant tax content, confirming current4(1)(e)deduction application; completed same-day research applied |https://mtca.gov.mt/docs/default-source/documents/manual-on-taxation-of-rental-incomee26fd6c3-a420-4cb8-b7c4-0b7e1137b7de.pdf|2026-11-26|
| Read for Wear and Tear Rules whole 3 pages and Deductions Rules whole 6 pages, completed planning/bookkeeping reads applied |https://legislation.mt/eli/sl/123.1/eng/pdf;https://legislation.mt/getpdf/66f65d8f3b56613c3cae68d9|2026-11-26|
| Read for FSS Rules 6–7,11,21–22,Schedule B year-end data and method conditions; annual statement periods actual read |https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3|2026-11-26|
| Read for LN 20/2026 rules 1(2),12 transition; no automatic legacy-benefit cancellation claim |https://legislation.mt/eli/ln/2026/20/eng/pdf|2026-11-26|
| Read for Cap 318 completed same-day liability/category/concurrent-work read applied; actual amounts routed to SSC Guide |https://legislation.mt/eli/cap/318/eng/pdf|2026-11-26|

Not yet confirmed: Class 2 deductibility, entertainment cases, specific historical sole-custody claims, source/residence disputes, specialist rental/property/election/allowance/assessment facts and future 2027 extensions are non-usable referrals above. Check this point with one of our partner accountants.
