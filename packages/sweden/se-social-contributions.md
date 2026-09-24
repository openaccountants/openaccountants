---
name: se-social-contributions
description: Use this skill whenever asked about Swedish self-employed social contributions (egenavgifter). Trigger on phrases like "egenavgifter", "Swedish self-employed contributions", "F-skatt", "Swedish social insurance", "Skatteverket egenavgifter", "enskild firma avgifter", or any question about social contribution obligations for a self-employed client in Sweden. Covers the ~28.97% combined rate, component breakdown, age-based reductions, and deductibility. ALWAYS read this skill before touching any Sweden social contributions work.
version: 2.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: self-employed social contributions

Figures are for tax year 2026.

## Scope and required records

Use this method to prepare the contribution working paper for an individual sole trader or natural-person partner in a Swedish trading partnership. It covers active business own contributions (egenavgifter), passive-business special payroll tax, the provisional return deduction and its later reconciliation. It does not compute personal income tax, VAT, employee payroll, or pension-cost special payroll tax.

## Ask the client first

- Confirm the records and decisions below before selecting a calculation branch.

Obtain the business form, income year, birth year, active/passive classification, pension and sickness-benefit decisions, Swedish social-insurance coverage, chosen sickness waiting period, tax-adjusted business result, prior return and final assessment, and preliminary-tax decision. Ask separately about partnership interests, foreign work, employer-paid contributions on business receipts, cessation and regional relief. Label a missing item and pause only the affected calculation.

F-tax/FA-tax affects collection and payer obligations; its absence alone does not prove that all business income is exempt from contributions. With FA-tax, separate employment withholding from business preliminary tax. A partnership partner generally pays personal preliminary tax through SA-tax; do not invent a sole-trader F-tax registration requirement. [F-tax](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/registeringabusiness/approvalforftax.4.676f4884175c97df4192308.html), [personal preliminary tax](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/preliminarskatt.html).

## The method, step by step

1. Establish the business classification and social-insurance coverage.
2. Select the income-year rate, contribution components and provisional deduction.
3. Build the return base and reconcile the prior deduction against assessed contributions.
4. Calculate charges, then apply documented relief and its floors/caps.
5. Reconcile preliminary payments, the final assessment and next-year return.

### Classify income and coverage

Business requires independence, continuity and a profit purpose. Hobby income belongs to a different return route. Assess activity across the individual's sole-trader businesses together: work-dependent consulting or craft activity can be active even at low hours; asset-management activity requires its own work-intensity assessment. Passive business is not capital income. Partnership interests are separate businesses; a deficit in one cannot simply cancel another's contribution-liable surplus. Salary and capital-income items do not enter this business calculation. [Classification](https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/enskildnaringsverksamhet/inkomstavnaringsverksamhet.4.361dc8c15312eff6fd2b612.html).

For foreign work, identify where activities occur and obtain the applicable social-security decision/certificate before choosing Swedish charges. Income-tax residence alone is insufficient. Keep foreign-coverage income separate; record the certificate's dates and covered activities. Do not treat an unverified assertion about A1 coverage as an exemption. The governing Swedish contribution rules recognise EU law and social-security agreements. [Social Contributions Act, chapter 1 and chapter 3](https://data.riksdagen.se/dokument/sfs-2000-980.html).

## Select the rate and provisional deduction

| Income/status in the income year | Contribution or tax rate | Maximum provisional deduction |
|---|---:|---:|
| Active, born 1959 or later, ordinary coverage and seven-day sickness waiting period | 28.97% | 25%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Active, born 1938–1958 | 10.21% | 10%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Active, born 1937 or earlier | 0% | 0%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Active, born 1959 or later, full old-age pension throughout the year, including both income and premium pensions | 10.21% | 10%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Active, born 1959 or later, full sickness or activity compensation during all or part of the year | 10.21% | 10%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Passive business | 24.26% | 20%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |
| Estate after a person who died during this income year or earlier | 24.26% | 20%  [Skatteverket](https://www.skatteverket.se/egenavgifter) |

Use documented benefit status, not merely early retirement or partial pension. Age-only pension treatment requires reaching 67 at the start of the year. [Current table](https://www.skatteverket.se/egenavgifter), [statutory pension/status rules](https://data.riksdagen.se/dokument/sfs-2000-980.html).

The ordinary total comprises sickness 3.64%, parental 2.00%, pension 10.21%, survivor 0.30%, labour-market 0.10%, work-injury 0.10% and general payroll charge 12.62%. The latter is a tax. Keep components when applying relief floors. [Components and waiting periods](https://www.skatteverket.se/egenavgifter).

For an elected waiting period, replace only the sickness component: one day 3.75%; seven days 3.64%; fourteen days 3.54%; thirty days 3.34%; sixty days 3.08%; ninety days 2.90%. Apply that selected component up to ten price base amounts and 3.64% above that boundary. The price base amount is SEK 59,200, making the boundary SEK 592,000. The remaining components continue on their applicable base; this boundary is not an overall contribution cap. Obtain the effective election dates if it changed during the year. [Waiting-period table](https://www.skatteverket.se/egenavgifter), [price base amount](https://www.skatteverket.se/omoss/pressochmedia/nyheter/2025/nyheter/nyalagarochregler2026.5.1522bf3f19aea8075ba32a2.html).

## Build the return base

Start from the tax-adjusted business computation, after the relevant income-tax adjustments and before the current provisional contribution deduction. Do not substitute revenue, withdrawals or bank balance. Keep a bridge from accounting result through every tax adjustment.

Exclude sickness/rehabilitation benefits and net income on which the payer owes employer contributions from the own-contribution base. For the latter, allocate related expenses; use proportionate allocation where direct matching is not possible, and retain the declaration disclosure at point 10.5. Apply the exclusions to both the deduction calculation and contribution-base reconciliation so exempt income is not accidentally charged. [Contribution base](https://www.skatteverket.se/egenavgifter), [chapter 3, sections 9–12](https://data.riksdagen.se/dokument/sfs-2000-980.html).

### Sole trader: NE schedule

Bring back the previous allowed provisional deduction in R40. Deduct the previously assessed contributions in R41. Complete R42 from the return's adjustments, then calculate the applicable provisional deduction in R43 on the eligible base. The provisional deduction is a return adjustment, not a bookkeeping expense. Continue the remaining NE fields to the declared surplus/deficit; do not assume R42 minus R43 is always the final contribution base when other adjustments or exempt receipts exist. Preserve both the before-deduction base and the final contribution-liable net income as distinct numbers. [NE and reconciliation instructions](https://www.skatteverket.se/egenavgifter).

### Partnership partner: N3A schedule

Use the agreed, tax-adjusted personal share, not the partnership's entire accounting profit. Reverse the previous deduction at point 25 and deduct assessed contributions at point 26. Where several businesses share an assessment, allocate those charges using their prior-year results. Sum points 20–26 at point 27; a positive eligible result supports the current provisional deduction at point 28. Sickness benefit is entered separately at point 29. Point 30 transfers to the active or passive business box in the personal return. Keep each partnership allocation and the individual aggregate relief calculation. [N3A instructions](https://www.skatteverket.se/foretag/inkomstdeklaration/deklarerasomdelagareihandelsbolag/fyllain3abilagan.4.2fb39afe18dabf1e4d251d9.html).

## Calculate charges and relief

Let B be the final contribution-liable net income, after the provisional deduction and relevant exclusions. No own contributions are due when B is below SEK 1,000. At the boundary the exemption no longer applies. A loss does not create a negative contribution or a credit against another business. Determine any loss carry-forward or other use separately. [Contribution Act](https://data.riksdagen.se/dokument/sfs-2000-980.html), [loss guidance](https://www.skatteverket.se/foretag/drivaforetag/foretagsformer/enskildnaringsverksamhet/underskott.4.361dc8c15312eff6fd32a54.html).

For the ordinary seven-day route, gross combined charge is B × 28.97%. For pension-only or passive routes use the appropriate table rate. Where the waiting period differs, split the sickness calculation at its boundary and add the other components. [Skatteverket](https://www.skatteverket.se/egenavgifter)

The general special deduction applies to eligible active business contribution income exceeding SEK 40,000, for a person below 67 at the start of the year who is not pension-only. Calculate the lesser of 7.5% of the eligible business base and SEK 15,000, constrained by the pension floor. Apply against own contributions first, then the general payroll charge. It is calculated automatically by the authority; check it once across eligible business income. There is no first-years-of-business eligibility condition. [General deduction law](https://data.riksdagen.se/dokument/sfs-2023-748.html).

### Regional relief

Check the exact fixed-establishment location against the statutory support-area list; a postal address in a named county alone is insufficient. Separate income from that establishment. For eligible own contributions, the provisional regional amount is 10% of that base, at most SEK 18,000 annually, with the pension floor. Pension-only cases are excluded. Apply against the general payroll charge first. [Regional relief law, sections 2–6 and annex](https://data.riksdagen.se/dokument/sfs-2001-1170.html).

Check sector exclusions, including steel/lignite/coal, transport and related infrastructure, and principally financial/insurance or specified intragroup activities. Obtain other de minimis aid and related-enterprise records, and determine the applicable general, agriculture or fisheries regulation; mixed-sector rules can change which regime applies. Do not presume unused state-aid capacity. Record the NACE code at point 13.2 and the agricultural/fisheries indicators when required; claim the relief at point 13.1. [Current declaration guidance](https://www.skatteverket.se/egenavgifter), [statutory conditions](https://data.riksdagen.se/dokument/sfs-2001-1170.html).

For a partnership, the aggregate partner relief attributable to that partnership is capped at SEK 85,200 and allocated proportionately to taxable shares. Employer-side regional relief can share that ceiling: obtain the partnership/employer's amounts before allocating the remaining allowance. An individual using both employer and own-contribution regional deductions also has a combined annual SEK 85,200 cap. Check the pension floor after combined relief; never subtract a second deduction blindly from a total already reduced. If aid eligibility or shared-cap evidence is missing, report the charge before regional relief and the specific unresolved claim. [Sections 6–6d](https://data.riksdagen.se/dokument/sfs-2001-1170.html).

## Payments, reconciliation and corrections

Use the authority's preliminary-tax decision and due dates; do not set monthly remittances by dividing an estimated contribution alone. Preliminary tax also reflects personal income tax and other relevant income. The usual payment date is the twelfth; the issued schedule controls holiday and other exceptions. Submit a revised preliminary income declaration when the expected result changes, continuing the current decision until replaced. [Preliminary business tax](https://www.skatteverket.se/foretag/skatterochavdrag/skattekontobetalaochfatillbaka/preliminarskattforforetagochforeningar.4.233f91f71260075abe8800010616.html).

In the following return, reconcile the allowed provisional deduction to assessed contributions even after cessation. A reassessment changing a deduction also changes its reversal in the following year's return; a changed assessed contribution is adjusted in R41 for the year of the reassessment decision. Retain a year-by-year bridge and amend all affected returns. Use the current official form, instructions and filing deadline for the income year; do not carry forward a fixed May date from an older guide. [Reassessment workflow](https://www.skatteverket.se/egenavgifter).

## Worked checks

All monetary inputs below are hypothetical SEK amounts. These are calculation checks, not final assessment notices; amounts shown to two decimals illustrate arithmetic, not statutory intermediate rounding. Reconcile the final whole-krona assessment with the official service. [Skatteverket](https://www.skatteverket.se/egenavgifter)

- **Ordinary trader:** Born 1985, active Swedish coverage, seven-day waiting period, no regional relief or exclusions. Eligible NE base before R43 is 200,000. A 25% provisional deduction is 50,000; resulting B is 150,000. Gross charge is 43,455; general relief is 11,250; estimated combined charge is 32,205. The relief base is the post-deduction 150,000, not 200,000. [Skatteverket](https://www.skatteverket.se/egenavgifter)
- **Relief boundary:** With already established B of 40,000, general relief is zero; gross combined charge is 11,588. At B of 40,100, relief is 3,007.50 and gross charge is 11,616.97, leaving 8,609.47 before any regional relief.
- **Contribution boundary:** Already established B of 999 incurs no own contributions. At B of 1,000, the ordinary combined charge is 289.70 with no general relief.
- **Pension-only:** Born 1958, active business, eligible pre-deduction base 200,000. Provisional deduction 20,000; B 180,000; pension contribution 18,378; no general relief.
- **Passive business:** Eligible pre-deduction base 200,000; provisional deduction 40,000; B 160,000; special payroll tax 38,816. Do not apply the active-business general relief.
- **Different waiting period:** Already established B 600,000 and a documented thirty-day election throughout the year. Sickness charge is 592,000 × 3.34% plus 8,000 × 3.64% = 20,064. Other components total 25.33%, giving 151,980. Gross combined charge is 172,044; eligible capped general relief 15,000 leaves 157,044 before regional relief. [Skatteverket](https://www.skatteverket.se/egenavgifter)
- **Partnership reconciliation:** Prior allowed deduction 50,000 and allocated assessed charges 32,205 give a net upward adjustment of 17,795 at points 25–26. Keep allocation evidence; do not deduct the entire multi-business assessment again.
- **Loss and salary:** A sole-trader loss of 30,000 does not produce negative contributions and does not reduce an unrelated partnership contribution base. Employment payroll stays outside this computation.
- **Regional evidence missing:** An eligible-looking establishment without aid-history or shared-cap evidence produces a charge before regional relief plus an unresolved relief calculation. Do not assert the full cap is available.

## Required working-paper output

Return: taxpayer and income year; classification and coverage evidence; pre-deduction base; rate/status and waiting-period decision; prior reversal and assessed-charge allocation; current provisional deduction; exclusions; final contribution base; gross components; each relief and floor/cap check; estimated charge; preliminary payments; exact NE/N3A fields; source dates; unresolved items; and next-year reconciliation amounts. Keep the contribution estimate distinct from personal income tax and from the final assessment.

## When to refuse or refer

- Do not calculate a Swedish charge until unresolved international coverage or benefit-status facts are established.
- Do not claim regional relief without the establishment, sector, aid-history and shared-cap evidence. Calculate the supported pre-relief charge while resolving the claim.
- If the starting tax-adjusted result cannot be reconciled, resolve the income-tax working paper before calculating contributions.

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
