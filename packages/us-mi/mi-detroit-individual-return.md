---
name: mi-detroit-individual-return
description: Use this skill whenever asked about Detroit (Michigan) city individual income tax for residents, non-residents who work in Detroit, or part-year residents. Trigger on phrases like "Detroit income tax", "City of Detroit return", "Form 5118", "Form 5119", "Form 5120", "Detroit resident tax", "Detroit non-resident allocation", "days worked in Detroit", "Form 5121", "Form 5123 estimated", "Uniform City Income Tax Act", "MCL 141.501".
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Detroit Individual Return

## Detroit Individual City Income Tax Skill — Residents, Non-Residents, Part-Year

> **Scope.** This skill covers the Detroit individual city income tax return (Forms 5118 / 5119 / 5120, administered by the Michigan Department of Treasury under the Uniform City Income Tax Act, MCL 141.501–141.787). It covers full-year Detroit residents, non-residents who earn Detroit-source compensation or business income, and part-year residents. Sole proprietors and single-member LLCs disregarded for federal tax are the primary users.
>
> **Companion skills.**
> - `mi-payroll.md` covers the employer side (Form 5321 withholding, Form 5469 employer guide, Form 5323). This skill covers the taxpayer side only.
> - `mi-income-tax.md` covers the Michigan state return (MI-1040). Detroit filings are administered separately and are not integrated with MI-1040, but share the April 15 deadline.
>
> **Quality tier.** Q3 — AI-drafted from public Michigan Treasury sources on 2026-05-28; not independently verified by a Michigan-licensed practitioner. All outputs require credentialed reviewer sign-off before filing.

## Section 1: Metadata

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Detroit, Michigan (US-MI, sub-state) |
| Tax type | City individual income tax |
| Primary forms | Form 5118 (Resident) / Form 5119 (Non-Resident) / Form 5120 (Part-Year) |
| Tax year | 2025 (returns filed in 2026) |
| Administering authority | Michigan Department of Treasury — City Tax Administration (since 2015) |
| Statutory basis | Uniform City Income Tax Act, MCL 141.501–141.787 (Act 284 of 1964); Detroit Income Tax Ordinance adopted thereunder |
| Filing deadline | April 15, 2026 |
| Version | 0.1 |
| Last updated | 2026-05-28 |
| Verified by | pending |
| Validation | AI-drafted — Q3 |

### Administrative history

**Administrative history table**

| Period | Administrator |
| --- | --- |
| Pre-2015 | City of Detroit — Income Tax Division (Coleman A. Young Municipal Center) |
| 2015 onward | Michigan Department of Treasury, City Tax Administration — under inter-governmental agreement with the City of Detroit per 2014 PA 198–202; state collects, all revenue net of administration retained by the city |

The 2014/2015 transition replaced the legacy Form D-1040(R) / D-1040(NR) / D-1040(L) with the current 5118 / 5119 / 5120 series. Some practitioner and software documentation still references "D-1040" — it is the predecessor of Form 5118.

### Sources consulted

**Sources consulted table**

| # | Source | URL |
| --- | --- | --- |
| 1 | 2025 City of Detroit Individual Income Tax Returns Forms and Instructions (5313 City Book) | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5313_City-Book.pdf |
| 2 | Form 5118 (2025) — Detroit Resident Income Tax Return | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118.pdf |
| 3 | Form 5119 (2025) — Detroit Non-Resident Income Tax Return | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5119.pdf |
| 4 | Form 5120 (2025) — Detroit Part-Year Resident Income Tax Return — Instructions | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5120-Instr.pdf |
| 5 | Form 5121 (2025) — City of Detroit Withholding Tax Schedule | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5121.pdf |
| 6 | Form 5469 (2025) — City of Detroit Income Tax Withholding Guide | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-Withholding/TY2025/5469_ty2025.pdf |
| 7 | Uniform City Income Tax Act (Act 284 of 1964) | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Act-284-of-1964 |
| 8 | MCL 141.613 — Non-resident income subject to tax | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-141-613 |
| 9 | MCL 141.651 — Employer withholding | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-141-651 |
| 10 | Honigman Miller Schwartz and Cohn LLP v City of Detroit, 505 Mich 284 (2020) | https://www.courts.michigan.gov/4a4dbc/siteassets/case-documents/opinions-orders/msc-term-opinions-(manually-curated)/19-20/157522.pdf |
| 11 | Michigan Treasury — Remote work / telecommuting guidance for city income tax | https://www.michigan.gov/taxes/questions/iit/accordion/covid19-tele/how-will-telecommuting-affect-an-employees-nonresident-city-income-tax-return |
| 12 | Michigan Treasury — Detroit Individual Income Tax filing landing page | https://www.michigan.gov/taxes/citytax/detroit/individual |

## Section 2: Quick reference — rates, exemption, thresholds

### Tax rates (TY 2025)

**Tax rates table**

| Taxpayer status | Rate | Source |
| --- | --- | --- |
| Detroit resident | 2.4% on all income, wherever earned | MCL 141.611; Detroit Ordinance |
| Non-resident | 1.2% on Detroit-source income only | MCL 141.611; MCL 141.613 |
| Part-year resident | 2.4% on income earned while resident + 1.2% on Detroit-source income earned while non-resident | Form 5120 instructions |

- **Detroit special rate authority** — Detroit is the only Michigan city with a 2.4%/1.2% rate. The Uniform City Income Tax Act caps non-Detroit cities at 1.0% resident / 0.5% non-resident; Detroit has special statutory authority for the higher rate under MCL 141.503(3).  _(MCL 141.503(3))_

### Personal exemption (TY 2025)

**Personal exemption table**

| Item | Amount | Source |
| --- | --- | --- |
| Personal / dependent exemption | $600 each | Form 5118 (2025) line instructions |

Detroit's exemption is **not** indexed and has remained at $600 for many years. It is distinct from the Michigan state personal exemption ($5,800 in 2026) — they are not coordinated.

### Filing deadline and extensions

**Filing deadline and extensions table**

| Item | Value |
| --- | --- |
| Annual return due | April 15, 2026 (for TY 2025) |
| Extension request | Form 5209 (City Application for Extension) — must be filed by April 15 with payment of estimated balance due |
| Automatic federal extension | Does **not** automatically extend the Detroit return — separate Form 5209 required |
| Electronic filing | Available via Michigan Treasury Online (MTO) and most major tax software |

### Estimated tax

**Estimated tax table**

| Item | Value |
| --- | --- |
| Threshold to require estimated payments | Expected city tax liability after withholding ≥ **$100** |
| Estimated voucher | Form 5123 — City Estimated Individual Income Tax Voucher |
| Quarterly due dates | April 15, June 15, September 15, January 15 |
| Underpayment penalty form | Form 5338 (sometimes referenced as Form 5125 in older releases — `[VERIFY:]` confirm with Treasury 2025 instructions) |

### Penalty and interest

**Penalty and interest table**

| Item | Rate / Amount |
| --- | --- |
| Late filing penalty | 5% of unpaid tax for first 2 months; +5% per month thereafter, max 25% |
| Late payment penalty | 1% per month, max 25% |
| Interest | Daily rate set by Treasury (federal short-term rate +1%, recomputed semi-annually) |

## Section 3: Detroit residency determination

Detroit residency is determined **independently** from Michigan state residency. A taxpayer can be a Michigan domiciliary for state purposes but non-resident of Detroit for city purposes (very common — anyone domiciled in the Detroit metro area outside the city limits). The reverse is rare but possible (Detroit resident temporarily absent from Michigan).

### Domicile test for Detroit (MCL 141.604)

- **Domicile definition** — A taxpayer is a Detroit resident for the tax year if their **domicile** — their fixed, permanent, principal home — is within the boundaries of the City of Detroit during the year.  _(MCL 141.604)_

**Domicile factors table**  _(MCL 141.604)_

| Factor | Indicia of Detroit domicile |
| --- | --- |
| Voter registration address | Detroit precinct |
| Driver license address | Detroit street address |
| Family home location | House/apartment within Detroit city limits |
| Mail delivery | Detroit address as principal mailing address |
| Bank account address | Detroit address |
| Length of physical presence | Greater part of the year within Detroit |
| Children's school enrollment | Detroit Public Schools Community District |

- **ZIP code not dispositive; verify boundary** — A "Detroit ZIP code" is not dispositive — many suburbs (Highland Park, Hamtramck, Grosse Pointe, Dearborn, Ferndale) share parts of 482xx ZIP codes but are independent municipalities. **Always verify the street address against the City of Detroit boundary using the City Assessor's property search before declaring residency.** Highland Park and Hamtramck are physically enclosed by Detroit but are separate cities with their own income taxes (Highland Park 2.0%/1.0%; Hamtramck 1.0%/0.5%).  _(City of Detroit Assessor's property search)_

### Part-year residency

- **Part-year filing requirement** — If the taxpayer moved into or out of Detroit during the year, Form 5120 is required. The taxpayer apportions income between the resident period (taxed at 2.4%) and the non-resident period (Detroit-source only, taxed at 1.2%).  _(Form 5120)_

## Section 4: The three filing patterns

### Pattern A — Full-year Detroit resident (Form 5118)

- **Pattern A rules** — - Taxes all income wherever earned at 2.4%. - Reports federal AGI starting point (Form 1040, Line 11). - Applies Detroit additions / subtractions on the front of Form 5118. - Claims personal exemptions ($600 × dependents). - Receives credit for tax paid to **another** Michigan city on non-Detroit-source wages (e.g., resident who works in Grand Rapids) — Form 5118 credit line — limited to lower of the other city's tax or Detroit's tax on the same income. - Files Form 5121 if there was any city withholding from W-2s.  _(Form 5118)_

### Pattern B — Non-resident with Detroit-source income (Form 5119)

- **Pattern B rules** — - Taxes only Detroit-source income at 1.2%. - Detroit-source income for non-residents (MCL 141.613) is limited to: 1. **Compensation** for work physically performed in Detroit (apportioned by days worked in Detroit / total work days); 2. **Net profit** from a business / profession carried on in Detroit, to the extent of the in-city business allocation percentage (Form 5327); 3. **Capital gains** and **rental income** from real or tangible personal property located in Detroit; 4. **Distributive share** of partnership / S-corp net profit attributable to Detroit business activity (see Section 7). - A non-resident generally does **not** owe Detroit tax on interest, dividends, pension, IRA distributions, Social Security, unemployment, or capital gains on intangibles — these are taxed only to Detroit residents.  _(MCL 141.613)_

### Pattern C — Part-year resident (Form 5120)

- **Pattern C rules** — - The year is split at the date of move. The taxpayer files a single Form 5120 combining: - The resident period: tax all income earned during that period at 2.4%; - The non-resident period: tax only Detroit-source income earned during that period at 1.2%. - Income is allocated by actual date received (cash basis) or by reasonable proration where the income is not date-identifiable (e.g., bonus tied to full year — typically prorated by days).  _(Form 5120)_

## Section 5: Income inclusions and exclusions

### Detroit treatment of common income items

**Income treatment table**

| Income type | Detroit resident (2.4%) | Detroit non-resident (1.2%) | Statutory basis |
| --- | --- | --- | --- |
| W-2 wages, salary, bonus, commission | **Taxable** on all wages | **Taxable** only on wages for work physically done in Detroit (apportion) | MCL 141.612 / 141.613 |
| Self-employment net profit (Schedule C) | **Taxable** on full net profit | **Taxable** on Detroit-apportioned share (Form 5327) | MCL 141.613(b) |
| Partnership K-1 (ordinary business income) | **Taxable** on full distributive share | **Taxable** on distributive share apportioned to Detroit business activity | MCL 141.613(c) |
| S-corp K-1 (ordinary business income) | **Taxable** if elected to pass through; see Section 9 (S-corp treatment note) | Generally **not taxable** to non-resident shareholder for city income tax purposes — Detroit treats S-corps differently from federal | `[VERIFY:]` Detroit Ordinance §6; Form 5119 instructions |
| Interest (bank, brokerage) | **Taxable** | **Not taxable** | MCL 141.612 |
| Dividends | **Taxable** | **Not taxable** | MCL 141.612 |
| Capital gain — intangibles (stocks, mutual funds) | **Taxable** | **Not taxable** | MCL 141.613 |
| Capital gain — real property in Detroit | **Taxable** | **Taxable** (Detroit-source) | MCL 141.613(d) |
| Rental income — Detroit property | **Taxable** | **Taxable** | MCL 141.613(d) |
| Rental income — non-Detroit property | **Taxable** | **Not taxable** | MCL 141.613 |
| Pension / annuity (private, state, federal) | **NOT TAXABLE** — Detroit excludes retirement income | **Not taxable** | Detroit Ordinance — retirement exclusion |
| IRA distributions (incl. Roth conversions) | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance — retirement exclusion |
| 401(k) / 403(b) distributions | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance — retirement exclusion |
| Social Security benefits | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance |
| Unemployment compensation | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance; Form 5118 instructions |
| Military pay (active duty) | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance — military exclusion |
| Worker's comp / disability | **NOT TAXABLE** | **Not taxable** | Detroit Ordinance |
| State / federal income tax refunds | **NOT TAXABLE** (Detroit does not pick up federal AGI inclusion of state refunds) | **Not taxable** | Form 5118 subtraction line |
| Gambling winnings | **Taxable** on full amount | **Taxable** if won at a Detroit-licensed casino (MotorCity, MGM Grand, Hollywood/Greektown) | MCL 141.613(g) [VERIFY] |
| Alimony received (pre-2019 decrees) | **Taxable** | **Not taxable** | Conforms to federal AGI definition |

**Key takeaway:** Detroit is more generous than the Michigan state return for **retired** taxpayers — pensions, IRAs, Social Security, and 401(k) distributions are entirely outside the Detroit base. This means a retired Detroit resident with only investment income and pensions typically owes **zero** Detroit tax even though they may owe Michigan state tax.

### Adjustments / deductions allowed (Form 5118, page 2)

**Deductions table**

| Deduction | Allowed? | Notes |
| --- | --- | --- |
| IRA contribution (above-the-line) | **Yes**, to extent allowed federally | Mirrors federal Form 1040 Schedule 1 deduction |
| Self-employment tax deduction (½ SE tax) | **Yes** | Mirrors federal §164(f) |
| Self-employed health insurance | **Yes** | Mirrors federal §162(l) |
| Self-employed retirement (SEP, Solo 401(k)) | **Yes** | Mirrors federal §404 deduction |
| Alimony paid (pre-2019 decrees) | **Yes** |  |
| Moving expenses | **Yes**, if moving **into** Detroit for a new principal job location; tied to historical federal §217 rules | Form 5118 specific deduction line |
| Renaissance Zone deduction | **Yes**, if the taxpayer's residence or business is within a designated Detroit Renaissance Zone | MCL 125.2681 et seq.; Form 5118 specific line |

## Section 6: Apportionment rules for non-residents

### Wage / salary apportionment — the "days worked in Detroit" formula

- **Days-worked apportionment formula** — Detroit uses a strict **days-worked-in-Detroit / total-work-days** ratio for non-resident wages. The formula appears on Form 5121 Part 3: ``` Detroit-source wages = Total wages × (Days actually worked in Detroit ÷ Total days actually worked) ``` Total work days = total compensated days minus vacation, holiday, sick, and paid leave days. The standard year is approximately 240–260 work days depending on the employer's calendar.  _(Form 5121 Part 3)_

### Post-COVID remote work treatment

- **Treasury telecommuting position** — This is the live audit issue for tax years 2020 onward. **Michigan Treasury's official position** (per the FAQ at michigan.gov/taxes covid19-tele, and the EY Tax News 2023-0758 summary): > A non-resident employee who telecommutes from a location **outside** Detroit does **not** owe Detroit tax on compensation for days worked from that outside location, even if the employer is based in Detroit. This means the standard apportionment is honored: a non-resident who spent 60 days physically in the Detroit office and 180 days working from their home in Royal Oak in 2025 would apportion 60/240 = 25% of their salary to Detroit. **However**, Detroit does **not** apply the "convenience of the employer" rule used by New York and Pennsylvania. The work-from-home days for the employer's convenience are still treated as days outside Detroit. The corollary the Treasury emphasizes (Regulation 13.2 of the legacy Detroit Income Tax Ordinance, carried forward): **"The mere fact that a non-resident employee takes work home with them and performs such work at their home does not permit allocation of compensation."** This applies to **occasional** off-hours work at home — a non-resident who normally works in the Detroit office and answers email evenings/weekends from home in the suburbs cannot claim those off-hours as "days outside Detroit." The allocation requires that the home location be the **regular, scheduled** work location for entire workdays.  _(Michigan Treasury COVID-19 telecommuting FAQ; Regulation 13.2, legacy Detroit Income Tax Ordinance)_

### Documentation required for non-resident allocation < 100%

**Documentation table**

| Documentation | Source |
| --- | --- |
| Employer letter listing actual days in Detroit vs. days at remote location | Form 5119 instructions; Form 5121 |
| Work-log / calendar / timesheet evidence | Treasury audit guidance |
| W-2 box 20 city code (`DET` or `DETRO`) reconciliation to Form 5121 | Form 5121 Part 3 |

- **Default to 100% without documentation** — Without contemporaneous documentation, Treasury defaults to **100% Detroit-source** apportionment for any W-2 showing Detroit withholding. This is a frequent audit adjustment.  _(Treasury audit guidance)_

### Honigman v. City of Detroit (Mich. 2020) — sourcing rule for services

- **Origin-based sourcing rule** — In *Honigman Miller Schwartz and Cohn LLP v. City of Detroit*, 505 Mich 284 (2020), the Michigan Supreme Court adopted an **origin-based sourcing rule** under MCL 141.623 for the sales factor used in business apportionment. The Court held that services rendered by attorneys physically working in the Detroit office were Detroit sales **regardless of where the client was located**. **Implication for self-employed non-residents:** if a non-resident sole proprietor performs services at a Detroit work location (e.g., a freelance software developer who commutes into a Detroit co-working space or client site), the income attributable to that physical work in Detroit is Detroit-source — even if the client is in California. This origin-based sourcing is the city analog of the more familiar "where the service is performed" rule. Conversely, a non-resident who performs all work remotely from their home outside Detroit, billing Detroit-based clients, has **no Detroit-source income** from those services, because no physical work occurs in Detroit. *Honigman* supports this conclusion by negative implication.  _(Honigman Miller Schwartz and Cohn LLP v City of Detroit, 505 Mich 284 (2020); MCL 141.623)_

## Section 7: Self-employed taxpayer treatment

### Schedule C net profit — resident

- **Resident Schedule C treatment** — A full-year Detroit resident sole proprietor reports the full federal Schedule C net profit on Form 5118 (after subtracting the ½ SE tax deduction and SE health insurance) at 2.4%. There is no apportionment — residents are taxed on worldwide income.  _(Form 5118)_

### Schedule C net profit — non-resident: Form 5327 business allocation

- **Business allocation formula intro** — A non-resident sole proprietor with any Detroit business activity must file **Form 5327 — Business Income Apportionment Schedule**. Form 5327 computes the in-city percentage as the average of three factors (MCL 141.621–141.624):  _(MCL 141.621–141.624)_

**Business allocation factors table**  _(Form 5327; MCL 141.621–141.624)_

| Factor | Numerator | Denominator |
| --- | --- | --- |
| Property | Avg. cost of real and tangible personal property used in business **in Detroit** | Total avg. cost of all business property |
| Payroll | Total compensation paid to employees for work done **in Detroit** | Total compensation paid to all employees |
| Sales / receipts | Gross revenue from **services performed in Detroit** (origin-based per *Honigman*) and from sales delivered to a Detroit destination | Total gross revenue |

- **Business allocation percentage formula** — ``` Business allocation % = (Property% + Payroll% + Sales%) / 3 ``` If a taxpayer has **no payroll** (one-person consultancy) or **no property** (no fixed location), the denominator of the average is reduced to exclude factors with both numerator and denominator zero (a "missing-factor" adjustment, MCL 141.624). For a typical solo freelance software developer with **no employees, no Detroit real estate, and all work done remotely from a home office outside Detroit**, all three factors will be zero in Detroit, and the allocation will be 0%. No Detroit tax is owed on the Schedule C even if some clients are Detroit-based.  _(MCL 141.624)_

### Home office consideration

- **Home office location requirement** — The home office must be located **inside Detroit city limits** for any allocation to Detroit to result from home-based work. Verify the address against the Detroit boundary as described in Section 3.  _(Section 3 boundary verification)_

## Section 8: Credits

### Credit for tax paid to another Michigan city (resident only)

- **Credit computation formula** — A full-year Detroit resident who earns wages or business income taxed by **another** Michigan city (Grand Rapids, Lansing, Flint, Pontiac, Hamtramck, Highland Park, etc.) receives a non-refundable credit on Form 5118. ``` Credit = lesser of: (a) the other city's tax actually paid on the doubly-taxed income, or (b) Detroit's 2.4% tax on the same doubly-taxed income. ``` This credit prevents double city-level taxation but does not refund any excess. Note: this is **not** a credit for Michigan state tax (no such credit exists at the city level) and not a credit for federal tax.  _(Form 5118)_

### Detroit homestead property tax credit

- **No city-level homestead credit** — Detroit does **not** offer a city-level homestead property tax credit on the Detroit return. The Michigan state-level credit is claimed on Form MI-1040CR (the Homestead Property Tax Credit) filed with the Michigan state return, not with Form 5118. Some practitioner guides conflate this — be careful. `[VERIFY:]` Confirm against TY 2025 5313 City Book that no new Detroit-specific homestead credit has been introduced for 2025.  _(Form MI-1040CR)_

### Renaissance Zone deduction (effectively a credit)

- **Renaissance Zone abatement** — Designated Detroit Renaissance Zones (e.g., portions of Midtown, the Eastern Market area, and several industrial zones — see City of Detroit Planning Department list) qualify residents and businesses located in the Zone for an income tax abatement under MCL 125.2681 et seq. The abatement phases out in the last three years of the Zone's designation. This is taken as a deduction line on Form 5118, not a tax credit.  _(MCL 125.2681 et seq.)_

## Section 9: Tier 1 deterministic rules + Tier 2 judgment rules

### Tier 1 — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| DET-T1-01 | Resident rate = 2.4%; Non-resident rate = 1.2% (TY 2025) | MCL 141.611; Detroit Ordinance |
| DET-T1-02 | Personal exemption = $600 per individual / dependent (TY 2025) | Form 5118 (2025) |
| DET-T1-03 | Filing deadline = April 15 of the year following the tax year | MCL 141.671 |
| DET-T1-04 | Resident is taxed on income wherever earned; non-resident is taxed only on Detroit-source income | MCL 141.612, 141.613 |
| DET-T1-05 | Social Security, unemployment compensation, military pay, pensions, IRA / 401(k) distributions are excluded from Detroit base | Detroit Ordinance — retirement exclusion |
| DET-T1-06 | Non-resident interest, dividends, and intangible-asset capital gains are NOT Detroit-source | MCL 141.613 |
| DET-T1-07 | Non-resident wage apportionment uses days-actually-worked-in-Detroit / total-work-days | Form 5121 Part 3; MCL 141.612 |
| DET-T1-08 | Resident gets credit for tax paid to another Michigan city, capped at Detroit's 2.4% on same income | Form 5118 credit line; MCL 141.689 |
| DET-T1-09 | Estimated tax required if expected liability after withholding ≥ $100 | Form 5123 instructions |
| DET-T1-10 | Forms: 5118 (Resident), 5119 (Non-Resident), 5120 (Part-Year). Form 5121 attached if any W-2 city withholding. | Treasury 2025 City Book |
| DET-T1-11 | Federal extension does NOT extend Detroit return — Form 5209 required | Form 5209 instructions |
| DET-T1-12 | Origin-based sourcing for service revenue under *Honigman* (2020) | 505 Mich 284 |

### Tier 2 — requires judgment

**Tier 2 rules table**

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| DET-T2-01 | **Detroit-vs-Michigan domicile** — taxpayer can be a Michigan resident and Detroit non-resident, or vice versa. Verify physical address against Detroit boundary (City Assessor parcel map). Highland Park and Hamtramck are NOT Detroit. | Use Detroit Open Data parcel viewer to confirm. |
| DET-T2-02 | **Remote work allocation** — non-resident working some days at Detroit office and some days at home in suburbs allocates by actual days. Treasury does NOT apply convenience-of-employer doctrine. Documentation (employer letter, calendar) required to support < 100%. | Without docs, audit default is 100% Detroit. |
| DET-T2-03 | **"Occasional work at home" trap** — Regulation 13.2 still bars allocation for incidental off-hours email/calls from home. The home must be the regular full-day work location. | Distinguish full-time WFH from "took work home." |
| DET-T2-04 | **Spouse in different residency status** — if one spouse is a Detroit resident and the other is not, they must file Detroit returns separately (Form 5118 for the resident; Form 5119 for the non-resident if they have Detroit-source income). They cannot file a joint Detroit return combining both residencies. | Use separate filing statuses on each form. |
| DET-T2-05 | **Part-year residency split date** — use actual move-in / move-out date. Income received before move-in date that was earned during a period of non-residency stays in the non-resident bucket. | Cash-basis allocation. |
| DET-T2-06 | **S-corp distributive share** — Detroit treats S-corps as separate taxable entities (NOT flow-through to shareholders for city tax purposes — different from federal). The S-corp pays Detroit corporate income tax on the entity's apportioned income; the resident shareholder is generally not double-taxed on the K-1 ordinary income. | This is a significant Detroit-specific deviation from federal pass-through. Flag for reviewer. `[VERIFY:]` Detroit Ordinance §6 and current treatment. |
| DET-T2-07 | **Partnership distributive share** — Detroit follows the federal flow-through treatment for partnerships. Resident partners include full distributive share; non-resident partners include Detroit-apportioned share via Form 5327 at the partnership level. | Different from S-corp treatment. |
| DET-T2-08 | **Renaissance Zone qualification** — depends on physical residence/business location within a designated Zone for the full taxable year and on Zone phase-out schedule. | Verify Zone status with Detroit Planning Dept. |
| DET-T2-09 | **Multi-Michigan-city situation** — resident of Detroit working in Grand Rapids: claim credit on Form 5118. Non-resident of Detroit working partly in Detroit and partly in Lansing: file Form 5119 for Detroit days, file Lansing's CF-1040 separately for Lansing days. | Separate non-resident returns for each city. |
| DET-T2-10 | **Estimated tax safe harbors** — Detroit has no statutory safe-harbor structure as detailed as the federal §6654; Treasury historically waives penalty if total payments ≥ prior year's liability and ≥ 70% of current year. | `[VERIFY:]` current safe-harbor mechanics from Form 5338 instructions. |

## Section 10: Worked examples

### Example 1 — Detroit resident sole prop with all-Detroit clients

**Facts.** Maya is a freelance software developer, single, age 34, domiciled year-round in a rented apartment on East Lafayette Street, Detroit (verified within Detroit city limits). She runs a single-member LLC disregarded for federal tax. 2025 federal Schedule C net profit: $110,000. She has no W-2 income. She paid $7,773 of ½ SE tax deduction and $8,400 of self-employed health insurance.

**Detroit computation (Form 5118)**

| Line | Item | Amount |
| --- | --- | --- |
| 1 | Federal AGI (from Form 1040 Line 11) | $93,827 |
|  | Subtractions (none — no pensions, SS, etc.) | $0 |
|  | Additions (none) | $0 |
|  | Detroit AGI | $93,827 |
|  | Less: personal exemption (1 × $600) | $(600) |
|  | Detroit taxable income | $93,227 |
|  | Detroit tax @ 2.4% | $2,237 |

No credit for tax paid to other city. No Detroit withholding. Full $2,237 owed on Form 5118, due April 15, 2026. Maya should have been making quarterly estimates on Form 5123 because liability exceeded $100.

### Example 2 — Detroit resident employee at a Detroit firm

**Facts.** Marcus, married filing jointly, age 41, domiciled in a single-family home on Conant Street, Detroit. His spouse Tasha is also a Detroit resident. Marcus earns $82,000 W-2 wages from a Detroit-headquartered employer; Detroit withholding (Box 19) of $1,968. Tasha earns $46,000 W-2 from an employer in Warren, MI (no Detroit withholding — Warren has no city income tax). They have two minor children. No other income.

**Detroit computation (Form 5118 — joint)**

| Line | Item | Amount |
| --- | --- | --- |
| 1 | Federal AGI | $128,000 |
|  | Additions / subtractions | $0 |
|  | Detroit AGI | $128,000 |
|  | Less: personal exemptions (4 × $600) | $(2,400) |
|  | Detroit taxable income | $125,600 |
|  | Detroit tax @ 2.4% | $3,014 |
|  | Less: Detroit withholding (Form 5121) | $(1,968) |
|  | Balance due | $1,046 |

Because both spouses are Detroit residents, both incomes are taxed at the 2.4% resident rate. Tasha's Warren wages are fully taxable to Detroit because Warren imposes no offsetting city tax (no credit available).

### Example 3 — Non-resident sole prop with some Detroit clients (apportionment edge case)

**Facts.** Priya is a freelance UX designer domiciled in Ferndale, MI (outside Detroit). Single, age 29. 2025 federal Schedule C net profit: $95,000. She works from her Ferndale home office most days, but spent **32 full days** physically at a client site in Detroit (an automotive firm in the New Center area), where she conducted user-testing sessions. She has no employees and no business property in Detroit. Total work days for the year: 230.

**Apportionment analysis (Form 5327)**  _(Form 5327)_

| Factor | Numerator | Denominator | Percentage |
| --- | --- | --- | --- |
| Property | $0 (no Detroit business property) | ~$2,000 (home office equipment, all in Ferndale) | 0% |
| Payroll | $0 (no employees) | $0 (no employees) | Excluded (missing factor) |
| Sales / receipts (services) | Services performed in Detroit = revenue earned on the 32 days physically in Detroit (origin-based per *Honigman*); estimate revenue tied to those 32 days ≈ $95,000 × (32/230) = $13,217 | $95,000 | 13.9% |

- **Apportionment percentage calc** — ``` Apportionment % = (0% + 13.9%) / 2 = 6.96% ``` (Payroll factor excluded because both numerator and denominator are zero; the average is taken over the remaining two factors per MCL 141.624.)  _(MCL 141.624)_

**Detroit computation (Form 5119)**

| Line | Item | Amount |
| --- | --- | --- |
|  | Schedule C net profit | $95,000 |
|  | Less: ½ SE tax deduction | $(6,712) |
|  | Less: SE health insurance | $(6,000) |
|  | Net business income | $82,288 |
|  | × Detroit apportionment 6.96% | $5,727 |
|  | Less: personal exemption (1 × $600) | $(600) |
|  | Detroit taxable income | $5,127 |
|  | Detroit tax @ 1.2% | $62 |

Below the $100 threshold for required estimated payments. Priya should **keep contemporaneous records** (Detroit client engagement letter, calendar, mileage log, client sign-in records) to support the 32 days during any audit. Without documentation, Treasury may default the apportionment to 100% Detroit-source ($82,288 × 1.2% = $987), a ~$925 adjustment.

## Section 11: Refusal catalogue

**Refusal catalogue table**

| ID | Situation | Action |
| --- | --- | --- |
| DET-R-01 | Multi-state apportionment beyond Michigan (e.g., taxpayer also has income sourced to Ohio, Illinois) | Refuse — out of scope; refer to a multi-state practitioner |
| DET-R-02 | Ownership of a partnership or S-corp with operations in multiple Michigan cities (Detroit + Grand Rapids + Lansing) | Refuse — multi-city apportionment requires entity-level review |
| DET-R-03 | Detroit corporate income tax (Form 5297 / 5301) — this skill is individual only | Refuse — separate skill required |
| DET-R-04 | Amended Detroit return (Form 5118-X equivalent) | Refuse — out of scope; refer to reviewer |
| DET-R-05 | Detroit casino gaming winnings allocation for non-residents | Refuse — narrow specialty; refer to reviewer |
| DET-R-06 | Renaissance Zone qualification dispute or Zone phase-out year mechanics | Refuse — refer to Detroit Planning Dept. and reviewer |
| DET-R-07 | Estate / trust filing a Detroit return (Form 5462) | Refuse — fiduciary filing out of scope |
| DET-R-08 | Highland Park, Hamtramck, or other Michigan city return (not Detroit) | Refuse — different jurisdiction; use city's own forms |
| DET-R-09 | Tax year other than the current TY 2025 | Refuse — rates and forms may differ; verify against year-specific Treasury instructions |
| DET-R-10 | "Convenience of employer" argument by a Detroit employer for an out-of-state remote worker | Refuse — not applicable in Michigan; flag as an audit risk if it arises |
| DET-R-11 | Detroit residency dispute with the City Assessor / Treasury (boundary question, multiple homes) | Refuse — refer to reviewer; gather documentary evidence first |
| DET-R-12 | S-corp K-1 with mixed-location business activity owned by Detroit resident | Refuse — Detroit's separate-entity treatment of S-corps requires entity-level analysis (see DET-T2-06) |

## Section 12: Form mapping

**Form mapping table**

| Detroit form | What it covers | Federal / state counterpart |
| --- | --- | --- |
| Form 5118 | Detroit Resident Individual Income Tax Return | Form 1040 (federal); MI-1040 (state) — neither integrates |
| Form 5119 | Detroit Non-Resident Individual Income Tax Return | N/A — city-only |
| Form 5120 | Detroit Part-Year Resident Income Tax Return | N/A — city-only |
| Form 5121 | City of Detroit Withholding Tax Schedule (attached to 5118/5119/5120 when W-2 city withholding shown) | Federal Form W-2 box 19/20 reconciliation |
| Form 5123 | City Estimated Individual Income Tax Voucher (quarterly) | Federal 1040-ES; MI-1040ES |
| Form 5209 | City Application for Extension of Time to File | Federal Form 4868 (does NOT extend Detroit) |
| Form 5327 | Business Income Apportionment Schedule (for non-resident Schedule C / partnership income) | N/A — city-only |
| Form 5338 | Underpayment of Estimated Tax Penalty Computation | Federal Form 2210; MI Form MI-2210 |
| Form 5469 | City of Detroit Income Tax Withholding Guide (employer reference; see `mi-payroll.md`) | IRS Publication 15 (Circular E) |
| Form 5462 | City Income Tax Return for Estates and Trusts (out of scope for this skill) | Federal Form 1041 |

## Section 13: Provenance and self-checks

### Provenance

- All rates, exemption amounts, and form names sourced from the Michigan Department of Treasury 2025 City of Detroit Individual Income Tax Returns Forms and Instructions (Form 5313 City Book).
- Statutory citations to the Uniform City Income Tax Act (MCL 141.501–141.787) and Detroit-specific provisions of that Act.
- Case law citation to *Honigman Miller Schwartz and Cohn LLP v. City of Detroit*, 505 Mich 284 (2020).
- Treasury policy on remote-work apportionment sourced from the official Treasury FAQ (michigan.gov/taxes COVID-19 telecommuting accordion) and cross-checked against EY Tax News 2023-0758 secondary summary.

### Self-checks before completing a Detroit return

1. Verify residency by **physical street address** against Detroit boundary — not by ZIP code, not by "metro Detroit."
2. Confirm form choice: 5118 (resident) / 5119 (non-resident) / 5120 (part-year) matches actual residency history.
3. If W-2 shows Box 19 Detroit withholding, attach Form 5121.
4. If non-resident allocating < 100% Detroit, confirm employer letter and day-by-day documentation are in client file.
5. If self-employed non-resident, confirm Form 5327 factors are computed and supported.
6. Confirm Detroit subtractions for pensions, IRA, Social Security, unemployment, military pay where applicable.
7. Confirm personal exemption ($600 × dependent count) is claimed.
8. Confirm no double-counting against MI-1040 (Detroit return is independent — does not flow to or from MI-1040).
9. Confirm federal extension was not relied on for Detroit deadline — if extension needed, Form 5209 must be on file.
10. Confirm quarterly estimated payments were made if prior year liability exceeded $100.

### Known uncertainties — `[VERIFY:]`

- Exact underpayment penalty form number for TY 2025 (5125 vs 5338) — confirm against current Treasury form catalogue.
- S-corp shareholder treatment for Detroit resident — Detroit Ordinance §6 historically treated S-corps as separate taxable entities, but practice may have evolved; confirm before relying on DET-T2-06.
- Whether the Detroit homestead-credit equivalent exists at the city level for TY 2025 — confirmed absent in older years but `[VERIFY:]` against current City Book.
- Treatment of gambling winnings from Detroit casinos for non-residents — confirm against MCL 141.613(g) and current Treasury policy.
- Detroit estimated-tax safe-harbor structure (prior-year vs current-year) — confirm against Form 5338 instructions for TY 2025.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
