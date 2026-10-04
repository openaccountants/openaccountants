---
name: ie-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing an Irish tax return AND mentions freelancing, self-employment, sole trader, LTD, contractor, or PSC in Ireland. Trigger on phrases like "Ireland tax return", "Form 11 Ireland", "Form 12 Ireland", "Irish sole trader", "Irish LTD CT1", "ROS Revenue Online Service", "self-assessment Ireland", "preliminary tax Ireland", "PRSI Class S", "USC Ireland", "Irish VAT registration", "Pillar Two QDMTT Ireland", or any similar phrasing where the user is an Irish tax resident self-employed individual, sole trader, partner, or small LTD director-shareholder. This is the REQUIRED entry point for the Irish freelance / SME workflow — every downstream skill in the stack (ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ireland-vat-return, ie-corporation-tax, ie-paye, ie-payroll, ie-cgt, ie-cat, ie-formation, ie-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Irish tax residents only (full-year residents under Section 819 TCA 1997, plus the 280-day combined test). ALWAYS read this skill first when starting an Irish freelance / SME tax workflow.
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland freelance and small business tax intake

This Guide is the first step for an Irish-resident self-employed person, sole trader, partner, or director-shareholder of a small private company limited by shares (LTD), including a one-person service company. It asks the questions that decide which Irish return applies and which other Guides to load, then hands a structured intake package to `ie-return-assembly`. Figures are for tax year 2026. The Irish tax year is the calendar year, 1 January to 31 December. In October and November 2026 most self-employed clients are doing two things at once: filing the 2025 Form 11 and paying 2026 preliminary tax. Ask which year the client means. This Guide holds only the few figures that decide routing. Rates, bands and credits live in the sibling Guides named below, so they are not repeated here.

## What this file is

The intake orchestrator for Irish-resident self-employed individuals, sole traders, partners, and small LTD director-shareholders, including personal service companies. Every downstream Irish Guide depends on this Guide producing a structured intake package first.

Job: (1) confirm the taxpayer is Irish tax resident, (2) capture domicile, which decides whether the remittance basis is possible, and ordinary residence, which `ie-non-dom` needs for other rules, (3) classify the regime (sole trader or partnership: Form 11 income tax, PRSI Class S and USC; LTD: Corporation Tax for the company plus the director's own return), (4) list the downstream Guides to run, (5) hand off to `ie-return-assembly`. Outputs are addressed to a qualified Irish tax professional (for example a Chartered Tax Adviser of the Irish Tax Institute, an ACA, ACCA or CPA, or an AITI-qualified agent registered on ROS). That professional signs off. This Guide is not the preparer of record.

Live sibling Guides this Guide routes to (all confirmed live in the catalog on 2 October 2026): `ie-income-tax-form11`, `ie-usc`, `ie-prsi-class-s`, `ie-preliminary-tax`, `ie-vat-return`, `ie-corporation-tax`, `ie-payroll`, `ie-cgt`, `ie-cat`, `ie-non-dom`, `ie-formation`, `ie-return-assembly`.

## Section 1: Quick reference, the routing figures

Only the figures that decide routing are here. Each table is one official page.

### Revenue, Who should register for Income Tax self-assessment?

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx |
| Must register for self-assessment if TAXABLE non-PAYE income is more than | EUR 5,000 | "You must register for self-assessment if: your taxable non-PAYE income exceeds €5,000 or your gross non-PAYE income exceeds €30,000." |
| OR must register if GROSS non-PAYE income is more than | EUR 30,000 | "your gross non-PAYE income exceeds €30,000. Note To declare non-PAYE income that does not exceed the above amounts, please submit a Form 12 online using myAccount" |

The two tests are joined by OR: crossing either one means the person must register for self-assessment. Both say "exceeds", so income exactly at a limit does not trigger that test. Below both limits, a PAYE worker declares the non-PAYE income on Form 12 instead. The same page also says a person "should" register if they are self-employed, or if their only or main income is rental, investment, foreign income (including foreign pensions), maintenance, PAYE-exempt fees, or profits from share options or share incentives ([Revenue, register for self-assessment](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). So the page says a self-employed person "should" register, and the "must" limits in the table catch anyone whose non-PAYE income passes either of them. A self-employed client below both limits: flag for the reviewer rather than assume Form 12. Route every self-assessed client to `ie-income-tax-form11`.

### Revenue, What are the VAT thresholds? (published 6 May 2026)

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx |
| Threshold, persons supplying services only | EUR 42,500 | "€42,500 , in the case of persons supplying services only." |
| Threshold, goods at the reduced or standard rate that the person manufactured or produced from zero-rated materials (same amount as services) | EUR 42,500 | "€42,500 , for persons supplying goods liable at the reduced or standard rates which they have manufactured or produced from zero rated materials." |
| Threshold, persons supplying goods | EUR 85,000 | "€85,000 , for persons supplying goods. €10,000 , for taxable persons making mail-order or intra-Community distance sales" |
| Threshold, goods and services together where goods are at least the share of turnover in the next row (other than the zero-rated-materials goods above) | EUR 85,000 | "€85,000 , for persons supplying both goods and services where 90% or more of the turnover is from the supplies of goods" |
| Share of turnover from goods needed for the goods threshold to apply to a mixed business | 90% | "90% or more of the turnover is from the supplies of goods, other than goods referred to above." |
| Threshold, mail-order or intra-Community distance sales of goods and cross-border TBE services into the State, counted across all EU Member States | EUR 10,000 | "€10,000 , for taxable persons making mail-order or intra-Community distance sales of goods and cross-border Telecommunications, Broadcasting and Electronic (TBE) services into the State." |
| Threshold, acquisitions from other EU Member States | EUR 41,000 | "€41,000 , for persons making acquisitions from other EU Member States." |

How to read the VAT table:

- Registration is obligatory when annual turnover "exceeds" the threshold. Below it, the person "may elect to register for VAT" ([Revenue, VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)).
- Turnover is the total value, excluding VAT, of the listed supplies "in a calendar year". It is not a rolling 12 months. Occasional disposals of business assets such as buildings, vehicles or machines are excluded from the count ([Revenue, VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)).
- A mixed business uses the goods threshold only if goods are 90% or more of turnover (the share in the table above). Otherwise the services threshold applies.
- A person not established in Ireland who supplies taxable goods or services to taxable customers in Ireland must register "irrespective of the level of turnover, unless they avail of the VAT SME Scheme" ([Revenue, VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)). This Guide refuses non-residents anyway (Section 8).
- A new business that has not yet made taxable supplies must register to reclaim VAT on its start-up costs ([Revenue, Who should register for VAT?](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/index.aspx)).
- A person carrying out only exempt or non-taxable activities may not register, except in certain situations such as acquiring goods from other Member States or receiving services from abroad ([Revenue, Who should register for VAT?](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/index.aspx)).

Route every VAT question, including rates, VAT3 returns and the reverse charge, to `ie-vat-return`.

### Department of Social Protection, SW14 PRSI Contribution Rates and User Guide, January 2026

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| Self-employed contributors pay Class S if annual income is this amount or more | EUR 5,000 | "Self-employed contributors with annual income of €5,000 or over pay Class S PRSI" |

The Class S test says "or over": income of exactly the amount in the table is caught. That is a different direction from the self-assessment test above, which says "exceeds". The two tests share a number but are different rules. Route the Class S rate and minimum contribution to `ie-prsi-class-s`.

### Department of Social Protection, PRSI and Family Employment

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/ |
| Shareholding at or above which a proprietary director is classified as self-employed for PRSI (directly or indirectly) | 50% | "From 1 July 2013 proprietary directors who own or control 50% or more of the shareholding of a company, either directly or indirectly e.g., through a holding company, are classified as self-employed and liable to pay PRSI at Class S." |

A director who owns or controls 50% or more (the share in the table above), counting shares held through a holding company, is classified as self-employed and pays Class S. A director below that share is not classified by this rule: refer the classification to `ie-prsi-class-s` and the reviewer.

### Revenue, Tax and Duty Manual Part 42-04-13, PAYE Taxpayers and Self-Assessment

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-04-13.pdf |
| Share of a company's share capital above which a director (controlling it directly or indirectly) is a proprietary director and a chargeable person who files Form 11 | 15% | "A proprietary director is a director who can control, either directly or indirectly, more than 15% of the share capital of a company. All proprietary directors are ‘chargeable persons’ and must be set up on Revenue’s record for the issue of a self-assessment return." |

This is the income tax test for which directors must file Form 11. It is a different rule from the PRSI Class S shareholding test in the table above: see Section 4.5. A director above the share in this table is a proprietary director and a chargeable person; route the director's own return to `ie-income-tax-form11`. A director at or below it is a non-proprietary director, for whom Revenue lists Form 12.

### Revenue, What is preliminary tax?

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Option 1: share of the tax due for the CURRENT tax year | 90% | "90% of the tax due for that tax year" |
| Option 2: share of the tax due for the immediately PREVIOUS tax year | 100% | "100% of the tax due for the immediately previous tax year" |
| Option 3: share of the tax due for the PRE-PRECEDING year, only when paying by direct debit, and not if that year's tax was nil | 105% | "105% of the tax due for the tax year preceding the immediately previous tax year" |
| Due date | 31 October of the tax year in question | "You must pay this by 31 October of the tax year in question." |

Preliminary tax covers Income Tax, PRSI and USC. It "must be equal to, or more than, the lowest amount" of the three options. The third option "only applies where you pay by direct debit" and "does not apply if the tax due for the pre-preceding year was nil". In the first year in self-assessment the client can choose either the previous-year option (usually nil, so generally nothing to pay) or the current-year option ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). Route the calculation to `ie-preliminary-tax`.

### Revenue eBrief No. 034/26, Pay and File Extension Date 2026

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| Extended date for the 2025 Form 11 balance and 2026 preliminary tax, ONLY if the 2025 Form 11 is filed AND the payment is made through ROS | 18 November 2026 | "the due date is extended to Wednesday 18 November 2026." |
| Date where the client does not both file and pay through ROS | 31 October 2026 | "the required date to submit both returns and payments is no later than 31 October 2026." |

By 31 October in a tax year the client must pay preliminary tax for that year, file the self-assessment return for the previous year, and pay any balance for the previous year ([Revenue, pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)). A late return carries a surcharge. Route surcharge and interest questions to `ie-income-tax-form11` and `ie-preliminary-tax`.

### Revenue, When and how do you pay and file CGT?

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx |
| Pay date, disposals 1 January to 30 November (initial period) | 15 December of the same year | "1 January and 30 November (the initial period), you must pay CGT by 15 December of the same year" |
| Pay date, disposals 1 December to 31 December (later period) | 31 January of the next year | "1 December and 31 December (the later period), you must pay CGT by 31 January of the next year." |
| CGT return | by 31 October of the following year | "You must file your CGT return on or before 31 October of the year that follows the date of disposal." |

CGT is paid on its own dates, not with the Income Tax balance ([Revenue, pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)). A self-assessed client reports gains in the CGT panel of Form 11; a person who does not need to make an Income Tax return can use Form CG1 ([Revenue, forms to complete](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx)). Route to `ie-cgt`.

### Regime decision tree at a glance

~~~
Irish tax resident for the year?  -> NO = REFUSE
   183 days or more in the tax year, OR 280 days or more over the
   tax year plus the preceding tax year taken together
   (30 days or less in a tax year: not resident on the 280-day test;
   see Section 4.1)
       |
Arrived in or left Ireland during the year?  -> YES = REFER (Section 8)
       |
Domiciled in Ireland?  Ordinarily resident?
       |
       +- Not domiciled in Ireland, or unclear
       |       -> remittance basis may be possible: flag, route ie-non-dom
       |
       +- Otherwise -> worldwide income basis
       |
Entity?
       |
       +- Sole trader / partner
       |       -> Form 11: ie-income-tax-form11
       |          + ie-prsi-class-s (Class S income test, Section 1)
       |          + ie-usc
       |          + ie-preliminary-tax
       |
       +- LTD (trading or investment)
       |       -> company: ie-corporation-tax
       |          + director's own return: ie-income-tax-form11
       |            (director controlling more than 15% of share capital: Form 11; at or below: non-proprietary director, Form 12; see the TDM table)
       |
       +- Large group in scope of Pillar Two -> REFUSE, refer to specialist
~~~

Parallel routing (independent of entity):

- Turnover in the calendar year more than the VAT threshold that fits the business (Section 1 table) → registration obligatory → route `ie-vat-return`. Below it, registration is optional: route only if the client elects or the reviewer flags it.
- Employees → route `ie-payroll`.
- Disposal of a chargeable asset → route `ie-cgt`.
- Gift or inheritance received → route `ie-cat`.
- Foreign domicile, or doubt about ordinary residence → route `ie-non-dom`.
- Entity unclear or not yet formed → route `ie-formation`.
- Always last → `ie-return-assembly`.

## Section 2: Workflow runbook (order of operations)

Strict order. Do not narrate steps.

1. **Opening.** One-line greeting, flow summary and reviewer reminder, then launch the refusal sweep.
2. **Refusal sweep.** A single `ask_user_input_v0` call with the 5 questions in Section 5.1.
3. **Document dump.** Ask the user to upload everything at once: bank statements, sales invoices, purchase invoices, prior Form 11 or CT1, ROS notices of assessment, payroll registers, VAT3 returns, RCT records if construction, forestry or meat processing. Do not insist on bank statements alone.
4. **Inference pass.** Parse every document; extract turnover, expenses, PAYE withheld, prior preliminary tax, VAT collected and reclaimed.
5. **Regime classification.** Apply the Section 4 decision tree using inferred turnover and the sweep answers.
6. **Confirmation.** Show the inferred summary, the proposed regime and the downstream Guide list; invite corrections.
7. **Gap filling.** `ask_user_input_v0` only for items documents cannot answer (domicile, ordinary residence, PPSN or tax reference number, marital status and assessment basis, ROS access).
8. **Handoff.** Produce the Section 6 summary and invoke `ie-return-assembly`.

Operating principles: use `ask_user_input_v0` for multiple choice; free text only for names and reference numbers. Batch up to 3 related independent questions. Never re-ask facts the documents already show. Put Irish terms in parentheses on first mention (for example "Personal Public Service Number (PPSN)"). All amounts in EUR.

## Section 3: Required inputs

Some are inferred from documents; the rest are gap-filled. All are needed before handoff.

- **Identity and registration:** legal name, PPSN (individuals; a sole trader uses their own PPSN for business correspondence with Revenue) or tax reference number (a partnership or company receives one from Revenue on registration), date of birth, marital or civil partnership status and assessment basis, ROS access (yes or no). Source for PPSN and tax reference number use: [Revenue, registering your business](https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx).
- **Residence and domicile:** days present in Ireland in the tax year and in the preceding tax year, domicile of origin and any domicile of choice, whether the person has been tax resident for three consecutive tax years (ordinary residence), year of arrival or departure.
- **Entity:** sole trader (own name or registered business name), partnership, LTD (CRO number, incorporation date, accounting year end), DAC or CLG. One-person service company indicators: single director-shareholder, services to one main client, and doubt about whether the relationship is really employment (Section 4.3).
- **Turnover:** gross turnover excluding VAT for the calendar year, split between goods and services, and between domestic, other EU business customers, EU consumers and customers outside the EU.
- **Tax history:** prior Form 11, Form 12 or CT1; outstanding preliminary tax or balances; losses carried forward; capital allowances.
- **Operational:** employee count, VAT registration status, RCT position (principal contractor or subcontractor in construction, forestry or meat processing), Local Property Tax position.
- **Documents:** bank statements, sales and purchase invoices, prior returns, ROS notices of assessment, employment detail summary if also employed, payroll register if an employer, VAT3 returns, RCT deduction summaries.

## The method, step by step

1. **Residence.** Count days present in Ireland in the tax year and the preceding tax year. A person is resident for the year with 183 days or more in it, or 280 days or more over the two years together; a person present for 30 days or less in a tax year is not resident in that year. Any part of a day counts as a day present ([Revenue, resident for tax purposes](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/resident-for-tax-purposes.aspx)). Not resident: refuse.
2. **Arrival or departure year.** If the client arrived in or left Ireland during the year, refer. Split-year treatment "applies to employment income only", so it does not help a self-employed client ([Revenue, split-year treatment in your year of arrival](https://www.revenue.ie/en/life-events-and-personal-circumstances/moving-to-or-from-ireland/moving-or-returning-to-ireland/split-year-treatment-in-your-year-of-arrival.aspx)).
3. **Domicile and ordinary residence.** The remittance basis is for a person who is Irish tax resident and not domiciled in Ireland. Tax and Duty Manual Part 05-01-21 states that it applies to 'persons who are not domiciled in the State' and that the separate basis for Irish citizens not ordinarily resident ceased 'for the tax year 2010 and subsequent tax years' ([Revenue, TDM Part 05-01-21](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-21.pdf)). Record ordinary residence as well: a person becomes ordinarily resident from the start of the fourth tax year after three consecutive tax years of residence ([Revenue, ordinarily resident](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/ordinarily-resident-tax-purposes.aspx)). If domicile is foreign or unclear, flag `remittance_basis_review` and route `ie-non-dom`. Do not decide it here.
4. **Self-assessment and the return.** A self-employed person files Form 11 on ROS and makes the self-assessment in its panel, covering Income Tax, PRSI and USC ([Revenue, forms to complete](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx)). A PAYE worker with side income applies the two tests in the self-assessment table in Section 1 ([Revenue, register for self-assessment](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). Route `ie-income-tax-form11` and `ie-usc`.
5. **PRSI Class S.** Apply the Class S income test in the SW14 table and the director shareholding test in the PRSI and Family Employment table ([DSP, SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); [DSP, PRSI and Family Employment](https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/)). Route `ie-prsi-class-s`.
6. **Preliminary tax and dates.** Record which of the three preliminary tax options in the Section 1 table the client can use, whether they pay by direct debit, and whether this is their first year in self-assessment ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). Record whether they will both file and pay through ROS, which decides the date in the eBrief table ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)). Route `ie-preliminary-tax`.
7. **VAT.** Pick the threshold row in the VAT table that fits the business, compare it with turnover for the calendar year, and set the registration flag ([Revenue, VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)). Route `ie-vat-return` if registered, obliged to register, or electing.
8. **Company.** For an LTD, route the company to `ie-corporation-tax` and the director to `ie-income-tax-form11` where the director controls more than the share in the TDM table; a director at or below it is a non-proprietary director, for whom Revenue lists Form 12; flag for the reviewer. Revenue describes Form 12 as the return "for employees, pensioners and non-proprietary directors" ([Revenue, pay and file CGT, forms list](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
9. **RCT.** If the client pays subcontractors in construction, forestry or meat processing, they are a principal contractor and "must register with Revenue" for RCT, with all RCT transactions through ROS ([Revenue, RCT for principal contractors](https://www.revenue.ie/en/self-assessment-and-self-employment/rct/rct-principal-contractors.aspx)). Flag it for the reviewer.
10. **Capital events and employees.** Disposal → `ie-cgt` (record the disposal date, which decides the payment date in the CGT table). Gift or inheritance → `ie-cat`. Employees → `ie-payroll`.
11. **Hand off** the Section 6.2 package to `ie-return-assembly`.

## Section 4: Regime decision tree, conditions and sources

### 4.1 Residency gate

- **Residence test.** Resident for a tax year with 183 days or more present in that year, OR 280 days or more in total over that year and the preceding year taken together. A person "will not be resident in Ireland if you are here for 30 days or less in a tax year". A day counts if the person is in Ireland "for any part of a day", with narrow exceptions for remaining airside and for being prevented from leaving by unforeseen and unavoidable circumstances ([Revenue, resident for tax purposes](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/resident-for-tax-purposes.aspx)).
- **Electing to be resident.** A person who arrives with the intention of being resident in the following tax year, and who will be resident then barring unforeseen circumstances, can choose to be tax resident in the year of arrival, and must tell Revenue in writing ([Revenue, resident for tax purposes](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/resident-for-tax-purposes.aspx)). This is an arrival-year case: refer (Section 8).
- **Split-year treatment.** Available on employment income only, in the year of arrival (and in the year of departure for someone leaving Ireland permanently to take up employment abroad) ([Revenue, split-year treatment in your year of arrival](https://www.revenue.ie/en/life-events-and-personal-circumstances/moving-to-or-from-ireland/moving-or-returning-to-ireland/split-year-treatment-in-your-year-of-arrival.aspx); [Revenue, moving to or from Ireland](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/moving-to-from-ireland.aspx)). A self-employed client in an arrival or departure year: refer.
- Full-year resident → continue. Not resident → refuse.

### 4.2 Domicile and ordinary residence gate

- **Domicile.** Domicile "broadly means living in a country with the intention of living there permanently". Everyone has a domicile of origin at birth and keeps it unless they gain a new one, which needs clear evidence of intending to live permanently in the new country and not to return ([Revenue, domicile and the domicile levy](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/domicile-domicile-levy.aspx)).
- **Remittance basis.** Revenue's page describes a person who is 'Irish tax resident, but non-ordinarily resident and not domiciled in Ireland for a tax year' and pays Irish tax on Irish source income and on foreign income 'to the extent that it is remitted into Ireland' ([Revenue, domicile](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/domicile-domicile-levy.aspx)). The rule itself is in Tax and Duty Manual Part 05-01-21: the remittance basis applies to 'persons who are not domiciled in the State', and ordinary residence has not been a condition since tax year 2010 ([Revenue, TDM Part 05-01-21](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-21.pdf)). This Guide does not decide it: route `ie-non-dom`.
- **Ordinary residence.** Three consecutive tax years of residence make a person ordinarily resident from the start of the fourth; it continues for three consecutive tax years after leaving ([Revenue, ordinarily resident](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/ordinarily-resident-tax-purposes.aspx)).
- If domicile is foreign or unclear: flag `remittance_basis_review`, route `ie-non-dom`. Do not assume.

### 4.3 Entity gate

- **Sole trader.** Registers with Revenue and uses their own PPSN for all business correspondence. A trading name different from their own name may be registered with the CRO on Form RBN1 ([Revenue, registering your business](https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx)). Return: Form 11. Route `ie-income-tax-form11`, `ie-prsi-class-s`, `ie-usc`, `ie-preliminary-tax`.
- **Partnership.** Revenue issues the partnership a Tax Reference Number. Each partner uses their own PPSN for personal returns; the partnership number is used for employer, VAT and RCT returns. A trading name different from the partners' names must be registered with the CRO on Form RBN1A ([Revenue, registering your business](https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx)). Route each partner as a sole trader for their own return, and flag the partnership return, Form 1 (Firms), for the reviewer ([Revenue, forms to complete](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx)).
- **Company (LTD, DAC, CLG).** Revenue issues the company a Tax Reference Number. The company must give Revenue a Statement of Particulars within 30 days of trading, on Form 11F CRO ([Revenue, registering your business](https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx)). Route the company to `ie-corporation-tax`. Route the director's own return to `ie-income-tax-form11` where the director controls more than the share in the TDM table; a director at or below it is a non-proprietary director, for whom Revenue lists Form 12; flag for the reviewer; Form 12 is listed for "non-proprietary directors" ([Revenue, pay and file CGT, forms list](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
- **Employee or self-employed?** Where a one-person company or contractor works mainly for one client, the question is whether the relationship is really employment. Revenue applies the Supreme Court's Karshan judgment, which sets five questions: Is there an exchange of a wage or other remuneration for work? Has the worker agreed to provide their services personally, with very limited or no option to delegate? Does the business control what, how, when and where the work is done? What do the facts and circumstances say about the true nature of the relationship? Is there any legislation that would change the answers? ([Revenue, RCT for principal contractors](https://www.revenue.ie/en/self-assessment-and-self-employment/rct/rct-principal-contractors.aspx)). Flag `employment_status_review` for the reviewer; do not decide it here.
- **Entity unclear or not yet formed:** route `ie-formation`.
- **Out of scope at this gate:** LTDs with more than 50 employees; groups with an Irish parent and overseas subsidiaries; large multinational groups in scope of the Pillar Two minimum tax rules. Refuse and refer (Section 8). These are scope limits of this Guide, not legal thresholds.

### 4.4 VAT registration gate

Use the VAT table in Section 1. Registration is obligatory once calendar-year turnover exceeds the threshold for the business's supply type. Elective registration below the threshold is allowed and can make sense to recover input VAT; a business that has not yet started supplying must register to reclaim VAT on start-up costs ([Revenue, VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx); [Revenue, Who should register for VAT?](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/index.aspx)). Rates, returns and cross-border rules: `ie-vat-return`.

### 4.5 PRSI Class S gate

Use the SW14 table (income test) and the PRSI and Family Employment table (director shareholding) in Section 1. Self-employed sole traders and partners with income at or above the Class S amount pay Class S; proprietary directors at or above the shareholding pay Class S. The rate changed during 2026; take it from `ie-prsi-class-s`, never from this Guide. The 50% PRSI test and the 15% income tax test are different rules with different directions ('50% or more' and 'more than 15%'); a director between them files Form 11 and is referred to `ie-prsi-class-s` for class.

### 4.6 USC gate

USC is part of the Form 11 self-assessment ([Revenue, forms to complete](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx)). Route bands, the exemption limit, reduced rates and the surcharge on non-PAYE income to `ie-usc`. Record whether non-PAYE income is large, so `ie-usc` checks the surcharge.

### 4.7 Preliminary tax gate

Use the preliminary tax and eBrief tables in Section 1. Capture: prior-year tax due, pre-preceding-year tax due, direct debit (yes or no), first year in self-assessment (yes or no), filing and paying through ROS (yes or no). Route `ie-preliminary-tax`.

### 4.8 Employer gate

Employees → route `ie-payroll`, which covers real-time payroll reporting, employer PRSI, PAYE and USC deductions.

### 4.9 CGT gate

Disposal of a chargeable asset (shares, a second property, crypto, a business) → route `ie-cgt`. Capture the disposal date: the CGT table in Section 1 shows that a disposal in December is paid by 31 January of the next year, not 15 December.

### 4.10 CAT gate

Gift or inheritance received → route `ie-cat`. Capture the relationship to the person who gave it and the valuation date. The 2026 ROS extension also covers CAT for valuation dates in the year ended 31 August 2026 when the return and payment are both made through ROS ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).

### 4.11 ROS channel

The Form 11 return and self-assessment are made through ROS ([Revenue, forms to complete](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx)). RCT compliance, filing and payment is conducted online through ROS ([Revenue, RCT](https://www.revenue.ie/en/self-assessment-and-self-employment/rct/index.aspx)). The 18 November extension applies only when the client both files and pays through ROS ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)). If the client has no working ROS access, flag it in `open_flags`: without it they cannot use the extended date.

## Ask the client first

These answers change the outcome. Ask them before anything else.

- How many days were you in Ireland in the tax year, and in the year before? Did you arrive in or leave Ireland during the year?
- Where were you born and where is your permanent home? Have you been tax resident in Ireland for each of the last three tax years?
- Do you trade in your own name, in a partnership, or through a company? If a company, what share do you own or control, including through a holding company?
- Which tax year are we working on: the 2025 return being filed now, the 2026 year, or both?
- What was your turnover excluding VAT in the calendar year, and how much of it was goods and how much services?
- Do you have employees, pay subcontractors in construction, forestry or meat processing, or work mainly for one client?

## Section 5: Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 Residence for the tax year:** 183 days or more in the year | Fewer than 183 days but 280 days or more over this year and last year together (and more than 30 days this year) | Arrived in or left Ireland during the year | Not resident | Not sure.
- **Q2 Domicile and ordinary residence:** Irish-domiciled | Foreign domicile of origin, tax resident in Ireland for each of the last three years | Foreign domicile of origin, not resident for all of the last three years | Not sure.
- **Q3 Entity:** Sole trader (own name) | Sole trader (registered business name) | Partnership | LTD, single director-shareholder | LTD, several directors or employees | DAC or CLG | Not sure.
- **Q4 Turnover excluding VAT for the calendar year, compared with the VAT table in Section 1:** Below the threshold for my type of supply | Above the services threshold but below the goods threshold | Above the goods threshold | Not sure (infer from documents).
- **Q5 Activity mix:** Services only | Goods only | Goods and services, goods 90% or more of turnover (the share in the VAT table) | Goods and services, goods less than that share | Construction, forestry or meat processing (RCT) | Financial services or investment funds.

**Routing table**

| Answer | Action |
| --- | --- |
| Q1 183 days, or 280-day test met | continue |
| Q1 arrived or left during the year | **REFER**: split-year treatment is for employment income only |
| Q1 not resident | **REFUSE** |
| Q1 not sure | ask for day counts; do not assume residence |
| Q2 Irish-domiciled | worldwide income basis; continue |
| Q2 foreign domicile, resident each of last three years | record ordinarily resident = yes; flag `remittance_basis_review`; route `ie-non-dom`; reviewer confirms |
| Q2 foreign domicile, not resident all three years, or not sure | flag `remittance_basis_review`; route `ie-non-dom`; reviewer confirms |
| Q3 sole trader or partnership | route `ie-income-tax-form11` + `ie-prsi-class-s` + `ie-usc` + `ie-preliminary-tax` |
| Q3 LTD single director-shareholder | route `ie-corporation-tax` + `ie-income-tax-form11` (director); flag `employment_status_review`; director's own return: Form 11 if more than 15% of share capital |
| Q3 LTD several directors, DAC or CLG | route `ie-corporation-tax`; if more than 50 employees **REFUSE** |
| Q3 not sure | route `ie-formation` first |
| Q4 below the threshold for the supply type | registration optional; flag below-threshold |
| Q4 above services but below goods threshold, and services only or goods less than the share | registration obligatory; route `ie-vat-return` |
| Q4 above services but below goods threshold, and goods only or goods at or above the share | registration optional unless the goods are made from zero-rated materials; flag for review |
| Q4 above the goods threshold | registration obligatory; route `ie-vat-return` |
| Q5 RCT | flag RCT; ask whether principal contractor or subcontractor |
| Q5 financial services or funds | **REFUSE** |

### 5.2 Secondary batched questions

- **Q6 Marital status and assessment:** Single | Married or civil partners, jointly assessed | Married or civil partners, separately assessed | Married or civil partners, single treatment | Widowed or surviving civil partner | Single parent.
- **Q7 Employees in the year:** None | 1 to 5 | 6 to 20 | More than 20.
- **Q8 VAT registration status:** Registered | Not registered, below threshold | Not registered, above threshold | Cancelled during the year | Not sure.
- **Q9 Preliminary tax for the year:** Paid in full by the due date | Paid in part | Not paid | First year in self-assessment | Not sure.

**Routing table**

| Answer | Action |
| --- | --- |
| Q6 jointly assessed | partner's PPSN required; `ie-income-tax-form11` applies joint bands and credits |
| Q6 separately assessed or single treatment | flag for reviewer; each spouse's position checked in `ie-income-tax-form11` |
| Q7 one or more employees | route `ie-payroll` |
| Q7 more than 20 | flag (larger payroll; confirm scope) |
| Q8 not registered and Q4 above threshold | flag **VAT registration overdue**; reviewer registers through ROS |
| Q8 cancelled | flag for reviewer (final VAT3 and annual return) |
| Q9 not paid, part paid or first year | flag `preliminary_tax_open`; route `ie-preliminary-tax` |

### 5.3 Capital events question

- **Q10 In the year did you:** Dispose of a chargeable asset (shares, second property, crypto, business) | Receive a gift or inheritance | Both | Neither | Not sure.

**Routing table**

| Answer | Action |
| --- | --- |
| Q10 disposal | route `ie-cgt`; capture the disposal date (1 January to 30 November, or December) |
| Q10 gift or inheritance | route `ie-cat`; capture relationship to the giver and the valuation date |
| Q10 both | route both |
| Q10 neither | skip |

### 5.4 Foreign income question

- **Q11 In the year did you have any foreign-source income, foreign bank accounts, foreign rental property, foreign pension or foreign shares?** Yes (one item) | Yes (several) | No | Not sure.

Any "Yes" → flag `foreign_source_income`. Foreign income is a reason Revenue says a person should register for self-assessment ([Revenue, register for self-assessment](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). The reviewer confirms double taxation agreement treatment, foreign tax credit, and remittance basis where Section 4.2 allows it. Route `ie-non-dom` where domicile is foreign.

### 5.5 ROS access

- **Q12 ROS access?** Yes, active | Yes, but not used for a long time | No, never registered | Started but hit problems.

Anything other than "Yes, active" → flag in `open_flags`. The 18 November extension needs both filing and payment through ROS (eBrief table, Section 1).

### 5.6 Onboarding fallback: no PPSN or tax reference number yet

If the user has no PPSN (individual) or the entity has no tax reference number, the workflow cannot complete. Flag `no_ppsn_trn`:

- Individual without a PPSN → refer; the client must obtain one before Revenue registration.
- Sole trader not yet registered → register through Revenue's eRegistration service, or on parts A and B of Form TR1 for Income Tax self-assessment ([Revenue, register for self-assessment](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). Route `ie-formation` for registration detail.
- Partnership or company not yet registered with Revenue → route `ie-formation`; Revenue issues the Tax Reference Number on registration ([Revenue, registering your business](https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx)).
- Company director identification requirements for CRO filings → route `ie-formation` and the reviewer.

## Section 6: Intake output template

### 6.1 Human-readable confirmation (shown to user)

~~~
INTAKE SUMMARY: Ireland, tax year [2025 return | 2026 year | both]

Taxpayer: [Name] | PPSN: [on file | missing] | Tax reference: [if entity]
Marital and assessment: [single | jointly assessed | separately assessed | single treatment]
Entity: [Sole trader | Partnership | LTD | DAC | CLG]
ROS: [active | dormant | not registered | problems]

RESIDENCE AND DOMICILE
  - Residence: 183-day test | 280-day test
  - Domicile: Irish | foreign
  - Ordinary residence: yes | no | unclear
  - Remittance basis review: yes | no

REGIME: [Form 11 | company plus director's Form 11]
  - Turnover (calendar year, excluding VAT): [amount]
  - Activity: services | goods | mixed (goods share) | RCT
  - VAT: registered | registration overdue | below threshold | electing
  - PRSI Class S: applies | does not apply | director classification to confirm
  - USC: part of Form 11; surcharge check flagged [yes | no]
  - Preliminary tax: option used; direct debit [yes | no]; first year [yes | no]
  - Pay and file date: 31 October 2026 | 18 November 2026 (ROS file AND pay)
  - Employees: [count]
  - CGT: [disposal yes or no; disposal date]
  - CAT: [gift or inheritance yes or no; relationship; valuation date]

DOWNSTREAM GUIDES:
  ie-income-tax-form11 [sole trader, partner, director],
  ie-preliminary-tax [self-assessed],
  ie-prsi-class-s [self-employed or proprietary director],
  ie-usc [self-assessed],
  ie-vat-return [registered, obliged or electing],
  ie-corporation-tax [LTD, DAC, CLG],
  ie-payroll [employees],
  ie-cgt [disposal],
  ie-cat [gift or inheritance],
  ie-non-dom [foreign domicile],
  ie-formation [entity unclear or not registered],
  ie-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED: listed below.

Confirm or correct anything above.
~~~

### 6.2 Structured intake package (internal JSON for ie-return-assembly)

~~~json
{
  "jurisdiction": "IE",
  "tax_year": 2026,
  "return_year_being_filed": 2025,
  "taxpayer": {
    "name": "", "ppsn": "", "tax_reference_number": "",
    "marital_status": "single|married_joint|married_separate|married_single_treatment|widowed|single_parent",
    "ros_access": "active|dormant|none|problems"
  },
  "residence_domicile": {
    "residence_test": "183_day|280_day|not_resident|unclear",
    "arrival_or_departure_year": false,
    "domicile": "irish|foreign|unclear",
    "ordinarily_resident": "yes|no|unclear",
    "remittance_basis_flag": false
  },
  "entity": {
    "type": "sole_trader|partnership|ltd|dac|clg",
    "cro_number": "",
    "incorporation_date": "",
    "accounting_year_end": "",
    "director_shareholding_band": "at_or_above_class_s_share|below|na",
    "employment_status_flag": false
  },
  "turnover": {
    "calendar_year_turnover_ex_vat_eur": 0,
    "activity_mix": "services|goods|mixed_goods_majority|mixed_services|rct",
    "goods_share_of_turnover": 0,
    "rct_role": "principal|subcontractor|none",
    "intra_eu_b2b_supplies": 0,
    "eu_consumer_sales": 0,
    "exports_outside_eu": 0
  },
  "vat": {
    "registered": false,
    "threshold_row_used": "",
    "registration_overdue_flag": false,
    "elective_registration": false
  },
  "prsi_usc": {
    "prsi_class_s_applicable": false,
    "usc_surcharge_check": false
  },
  "self_assessment": {
    "registered": false,
    "non_paye_test_met": false,
    "first_year": false
  },
  "preliminary_tax": {
    "prior_year_tax_due": 0,
    "pre_preceding_year_tax_due": 0,
    "direct_debit": false,
    "due_date": "2026-10-31",
    "ros_file_and_pay": false,
    "extended_date_if_ros": "2026-11-18"
  },
  "employment": {
    "has_employees": false, "employee_count": 0
  },
  "capital_events": {
    "cgt_disposal": false,
    "cgt_disposal_date": "",
    "cat_received": false,
    "cat_relationship": "",
    "cat_valuation_date": ""
  },
  "foreign_income_flag": false,
  "documents_received": [],
  "downstream_guides_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
~~~

## Section 7: Conservative defaults

When uncertain, prefer the stricter compliance outcome and flag it. All defaults are visible to the reviewer in `conservative_defaults_applied`.

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Residence borderline, no day count for the preceding year | Do not assume residence; ask for day counts; refuse if still unproven |
| Domicile unclear | Assume foreign domicile is possible; flag `remittance_basis_review`; tax foreign income as arising until the reviewer decides |
| Ordinary residence unclear | Record as unclear; it does not decide the remittance basis; `ie-non-dom` and the reviewer decide |
| Turnover close to the VAT threshold for the supply type | Treat as above; flag registration |
| Goods share of a mixed business close to the share in the VAT table | Treat as below the share; apply the services threshold |
| Director shareholding close to the Class S share, or held through a holding company | Count indirect holdings; treat as Class S; flag for review |
| Contractor working mainly for one client | Flag `employment_status_review` with the five Karshan questions |
| Sole trader or partnership unclear (shared trade) | Assume partnership; flag the partnership return, Form 1 (Firms) |
| Preliminary tax base unclear | Flag for `ie-preliminary-tax`; do not use the pre-preceding-year option unless direct debit is confirmed and that year's tax was not nil |
| CGT disposal date unclear | Ask; the payment date depends on whether it fell in December |
| Self-employed income close to the Class S amount | Treat as at or over (the test is "or over"); flag Class S |
| Foreign income, treaty position unclear | Tax as arising with no credit; reviewer claims any credit |
| ROS access unknown | Assume not active; use the 31 October 2026 date |

## When to refuse or refer

Protocol: stop the workflow, state the reason in one sentence, recommend a Chartered Tax Adviser (Irish Tax Institute) or an AITI-qualified ROS agent, and do not work around it.

- **Not resident** for the tax year: refuse.
- **Arrival or departure year** for a self-employed client: refer. Split-year treatment covers employment income only.
- **Remittance basis** claimed or possible: refer to the reviewer after routing `ie-non-dom`.
- **Employment status doubt** (one main client, personal service, client control): refer with the five Karshan questions.
- **LTD with more than 50 employees**, groups with an Irish parent and overseas subsidiaries, and large multinational groups in scope of the Pillar Two minimum tax rules: refuse.
- **Financial services or regulated investment funds:** refuse.
- **Charities, trusts and estates:** refuse; separate regimes.
- **No PPSN or tax reference number:** stop until registration is done.

Sample: "Stop. You arrived in Ireland during the year, so this is your year of arrival. Revenue's split-year treatment applies to employment income only, not to self-employment income, so I cannot prepare your Form 11 for this year alone. You need a Chartered Tax Adviser to handle the arrival year."

## Section 8: Refusal handling

Refusals fire from the refusal sweep or during the inference pass. The list in "When to refuse or refer" above is the in-scope refusal list. These are scope limits of this Guide. Where a refusal rests on a rule of law (residence, split-year treatment, remittance basis), the rule and its source are in Section 4.

### Reviewer escalation templates

~~~
REVIEWER FLAG
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified practitioner must confirm before advising client.
~~~

~~~
ESCALATION REQUIRED
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
~~~

## Section 9: Self-checks before handoff

Run all 14 before invoking `ie-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residence confirmed on the 183-day or 280-day test; arrival or departure year referred.
3. Domicile AND ordinary residence captured; remittance basis flag set wherever domicile is foreign or unclear.
4. Entity type set; employment status flag set for a single director-shareholder or contractor with one main client.
5. Calendar-year turnover recorded excluding VAT, with the goods and services split.
6. VAT threshold row from the Section 1 table chosen to fit the supply type; registration or overdue flag set.
7. Class S applicability set using the "or over" income test and, for directors, the shareholding test.
8. USC routed to `ie-usc`; surcharge check flagged where non-PAYE income is large.
9. Preliminary tax option recorded, with direct debit and first-year status.
10. Employee count set; `ie-payroll` in the downstream list if more than none.
11. CGT disposal date and CAT relationship and valuation date captured.
12. Foreign income flagged where applicable.
13. ROS status captured; the pay and file date chosen to match it; PPSN and tax reference gaps flagged.
14. All conservative defaults recorded; reviewer reminder present in opening and handoff.

## Section 10: Final handoff to ie-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer, entity and ROS status, (b) the regime selected, (c) downstream Guides in run order, (d) Guides not running and why, (e) a reviewer reminder (qualified Irish tax professional sign-off before ROS submission). Then invoke `ie-return-assembly` with the Section 6.2 package.

Example (hypothetical: sole trader, services only, single, no employees):

> Intake complete. Sole trader, IT consultancy, ROS active. Resident on the 183-day test, Irish-domiciled. Calendar-year turnover is above the services-only VAT threshold, so VAT registration is obligatory and the client is registered. Regime: Form 11 with PRSI Class S and USC. Preliminary tax for 2026 on the previous-year option; filing and paying through ROS, so the extended date applies. Running: ie-income-tax-form11, ie-preliminary-tax, ie-prsi-class-s, ie-usc, ie-vat-return, ie-return-assembly. Not running: ie-corporation-tax, ie-payroll, ie-cgt, ie-cat, ie-non-dom, ie-formation. Needs sign-off by a qualified Irish tax professional before ROS submission. Handing off now.

## Section 11: Cross-Guide references

**Inputs:** user documents and answers. **Output:** the Section 6.2 package consumed by `ie-return-assembly`.

Downstream Guides (through `ie-return-assembly`):

- `ie-income-tax-form11`: Form 11 self-assessment, income tax bands and credits, surcharges, the director's return.
- `ie-preliminary-tax`: the three preliminary tax options, first-year rules, interest on late payment.
- `ie-prsi-class-s`: Class S rate for 2026, minimum contribution, director classification.
- `ie-usc`: USC bands, exemption limit, reduced rates, surcharge on non-PAYE income.
- `ie-vat-return`: VAT rates, VAT3, annual return of trading details, reverse charge.
- `ie-corporation-tax`: company rates, CT1, close company surcharges, Pillar Two scope.
- `ie-payroll`: payroll, employer PRSI, PAYE and USC deductions.
- `ie-cgt`: CGT computation, annual exemption, reliefs, payment dates.
- `ie-cat`: gift and inheritance tax, group thresholds, returns.
- `ie-non-dom`: domicile, remittance basis, domicile levy.
- `ie-formation`: sole trader, partnership or company; CRO and Revenue registration.
- `ie-return-assembly`: final orchestrator (working paper, reviewer brief, action list).

## Section 12: Legislation named in the legacy Guide

The legacy Guide cited sections of the 1997 Taxes Consolidation Act, the Value-Added Tax Consolidation Act 2010, the Capital Acquisitions Tax Consolidation Act 2003, the Social Welfare Consolidation Act 2005 and the Companies Act 2014. Revenue's own pages, cited throughout, are the authority this Guide relies on. Revenue's residence pages point to the Tax and Duty Manual for Part 34 of the 1997 Taxes Consolidation Act (residence of individuals) ([Revenue, resident for tax purposes](https://www.revenue.ie/en/jobs-and-pensions/tax-residence/resident-for-tax-purposes.aspx)). For the employment status test, Revenue points to Tax and Duty Manual Part 05-01-30 ([Revenue, RCT for principal contractors](https://www.revenue.ie/en/self-assessment-and-self-employment/rct/rct-principal-contractors.aspx)).

## Sources

- Revenue, Who should register for Income Tax self-assessment?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx
- Revenue, What forms do you need to complete?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/forms-to-complete.aspx
- Revenue, Pay and file system: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx
- Revenue, What is preliminary tax?: https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx
- Revenue, eBrief No. 034/26: https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx
- Revenue, What are the VAT thresholds?: https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx
- Revenue, Who should register for VAT?: https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/index.aspx
- Revenue, How to know if you are resident for tax purposes: https://www.revenue.ie/en/jobs-and-pensions/tax-residence/resident-for-tax-purposes.aspx
- Revenue, How to know if you are ordinarily resident for tax purposes: https://www.revenue.ie/en/jobs-and-pensions/tax-residence/ordinarily-resident-tax-purposes.aspx
- Revenue, What is domicile and the domicile levy?: https://www.revenue.ie/en/jobs-and-pensions/tax-residence/domicile-domicile-levy.aspx
- Revenue, Tax and Duty Manual Part 05-01-21: https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-05/05-01-21.pdf
- Revenue, Tax and Duty Manual Part 42-04-13: https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-04-13.pdf
- Revenue, Moving to or from Ireland during the tax year: https://www.revenue.ie/en/jobs-and-pensions/tax-residence/moving-to-from-ireland.aspx
- Revenue, Split-year treatment in your year of arrival: https://www.revenue.ie/en/life-events-and-personal-circumstances/moving-to-or-from-ireland/moving-or-returning-to-ireland/split-year-treatment-in-your-year-of-arrival.aspx
- Revenue, Registering your business: https://www.revenue.ie/en/starting-a-business/starting-a-business/registering.aspx
- Revenue, Relevant Contracts Tax: https://www.revenue.ie/en/self-assessment-and-self-employment/rct/index.aspx
- Revenue, RCT for principal contractors: https://www.revenue.ie/en/self-assessment-and-self-employment/rct/rct-principal-contractors.aspx
- Revenue, When and how do you pay and file CGT?: https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx
- DSP, SW14 PRSI Contribution Rates and User Guide, January 2026: https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf
- DSP, PRSI and Family Employment: https://www.gov.ie/en/department-of-social-protection/publications/prsi-and-family-employment/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified Irish tax professional (a Chartered Tax Adviser of the Irish Tax Institute, an ACA, ACCA or CPA, or an AITI-qualified agent registered on ROS) before filing with Revenue via ROS or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants website.

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
