---
name: canada-tax-optimization
description: >
  Use this Tier 2 reference when working through LEGAL tax minimization
  strategies for Canadian taxpayers: individuals, sole proprietors and small
  business owners (CCPCs). Trigger on phrases like "reduce my tax Canada", "tax
  planning", "RRSP vs TFSA", "salary vs dividends", "income splitting", "TOSI",
  "small business deduction", "LCGE", "capital gains inclusion", "CRA", or any
  question about structuring affairs to legally minimize Canadian tax. Covers
  entity selection, registered account optimization, deduction strategies, loss
  utilization, timing, GST/HST planning, CPP optimization and red lines, each
  tied to the provision that allows it, for calendar 2026. Read this skill
  before giving Canadian tax optimization advice. It has no accountant sign-off,
  holds Quebec tax figures and does not authorise filing, payment or a tax position.
version: 1.2
jurisdiction: CA
tax_year: 2026
tax_year_notes: "Calendar 2026 (1 January to 31 December 2026), read at 5 November 2026. Federal text is the Justice Laws consolidation current to 21 June 2026. Quebec tax figures are held. The Productivity Mega Deduction and the $39,000 Class 10.1 ceiling are held as not shown in the regulations read."
last_updated: 2026-11-05
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
---

# Canada Tax Optimization v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers legal tax planning under the Income Tax Act, R.S.C. 1985, c. 1 (5th Supp.) (ITA), the Excise Tax Act (ETA), the Canada Pension Plan and the Employment Insurance Act, in Canadian dollars. It is for residents of Canada who are individuals, sole proprietors, or owner-managers of Canadian-controlled private corporations (CCPCs). The Canada Revenue Agency (CRA) administers these laws. Quebec and Alberta have no corporation tax collection agreement with the CRA, so their corporate tax sits outside the CRA table used here.

**Period label:** calendar 2026 (1 January to 31 December 2026), read at 5 November 2026. The individual tax year is the calendar year. A corporation's year is its own fiscal period (ITA s 249.1).

Non-residents, trusts as taxpayers, farm and fishing property, and financial institutions are outside this file. Quebec tax amounts are held. The federal EI, instalment and abatement figures that mention Quebec are stated from federal sources. Provincial personal amounts other than Ontario and British Columbia appear only where a row says so.

Each figure has one home where a sibling guide owns it. See `ca-capital-gains`, `ca-fed-cpp-ei`, `ca-fed-t1-return`, `ca-fed-t1135`, `ca-fed-t2125`, `ca-fed-instalments`, `ca-tax-residency`, `canada-gst-hst`, `canada-payroll`, `canada-formation`, `canada-transfer-pricing`, `qc-corporate-tax-co17`, `qc-individual-return`, `on-individual-return`, `on-tax-credits` and `on-eht`. Most of those carry 2025 figures. Where a sibling differs from this file, check the primary source before relying on either.

### What this file is

This is a Tier 2 source-cited draft, pending review, with no accountant sign-off. Earlier versions carried a reviewer entry. This version changes the content, so under template rule 11 that entry does not carry to this text, and the guide returns to Tier 2 until it is approved again. The change makes no finding about any earlier review.

Each strategy here is a rule with its conditions. It becomes advice only once a named client's facts meet those conditions. Do not tell a client a step is right for them because this file lists it. State the condition, then what the facts show.

### What the workflow base requires

This file depends on `bookkeeping-workflow-base`, which owns ledger work, its tiers, its question round and its outputs. This file is a planning reference and is not the base's country skill: that is `canada-bookkeeping`.

- **Refusal.** If a request needs a ledger, posting, adjustment or output file and `canada-bookkeeping` is not loaded, stop at base Step 1 and send exactly: "I need a country-specific bookkeeping skill loaded alongside this workflow base. Which jurisdiction are these accounts for?" Do no partial classification.
- **Operational hold.** A text search of `canada-bookkeeping` at 5 November 2026 found no conservative default slot or materiality threshold slot of the kind base Section 7 asks for. Until those are confirmed, do not produce ledger output from this file. Use it as a reference.
- **Question threshold:** CAD 0. No item is filtered on amount, as no Canadian floor was set.
- **Order.** Questions come before any output: base Step 5.5 runs before Step 6. What stays unanswered is Needs Input. Do not build a working paper with assumed answers first.
- **Defaults.** A default stands only where the law read fixes the result of the missing fact. An unknown province, residence, share class, associated group, deduction room or relief condition is Needs Input.

### How to read the status words

- **Enacted** means the text is in the consolidated Act or regulation read.
- **Administrative** means a CRA or Finance publication gives the figure under an indexing or practice rule. The Act read does not print the figure.
- **Proposed** means a government announced it. It is not law on the text read.
- **Withdrawn** means proposed and then abandoned. It was never law.
- **Held** means not proved here. Use it only side by side with the enacted position and only with a reviewer.

The federal consolidation read does not include application provisions. A start date in a row comes from the provision's own wording or the cited publication.

## Rates, bands and thresholds

Label: calendar 2026, read at 5 November 2026.

### Federal individual rates

| Taxable income (CAD) | Rate | Status | Source |
| --- | --- | --- | --- |
| 0 to 58,523 | 14% | Enacted rate, ITA s 117(2)(a), as amended by 2026, c. 2 (Bill C-4). Band indexed under s 117.1 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| Over 58,523 to 117,045 | 20.5% | Enacted rate, s 117(2). Administrative band | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 117,045 to 181,440 | 26% | Same | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 181,440 to 258,482 | 29% | Same | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 258,482 | 33% | Same | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |

The lowest rate was 14.5% for 2025 ([Federal Tax Expenditures 2026](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-2.html), on Bill C-4, [royal assent 12 March 2026](https://www.parl.ca/legisinfo/en/bill/45-1/c-4)). It is 14% for 2026 on the CRA table and in ITA s 117(2)(a). The consolidation shows no 14.5%, and the 2025 application text is held. Credits at the 'appropriate percentage' use the lowest rate for the year (ITA s 248(1)). Section 118(11) adds a top-up credit for 2025 to 2030 where the credits listed in its formula exceed the appropriate percentage of the first band: the excess times 7.14% for 2026 and 3.45% for 2025. Credits in the examples stay below that level.

### Combined rates

| Item | Amount | Status | Source |
| --- | --- | --- | --- |
| Top combined rate, provinces and territories other than Quebec | 44.5% (Nunavut) to 54.8% (Newfoundland and Labrador) | Administrative. 33% plus each CRA 2026 top provincial rate. T4127 Table 8.2 shows a provincial surtax only for Ontario | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html and https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/other-rates-amounts-26e.csv |
| Ontario top combined rate | 53.53% | Computed: 33% + 13.16% x 1.56, with surtax of 20% and 36% at the top | https://www.ontario.ca/laws/statute/07t11 and https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/other-rates-amounts-26e.csv |
| Quebec combined rate | Held | Revenu Quebec's rate page returned 403 and was not retried. T4127 shows a 16.5% federal abatement | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/other-rates-amounts-26e.csv |

### Federal credits and amounts for 2026

| Item | Amount (CAD) | Status | Source |
| --- | --- | --- | --- |
| Basic personal amount | 16,452, falling to 14,829 as income rises from 181,440 to 258,482 | Administrative figures. Formula enacted, ITA s 118(1.1) | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Canada employment amount | 1,501 | Administrative. ITA s 118(10) | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Disability amount | 10,341 | Administrative. ITA s 118.3 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Medical expense ceiling | Lesser of 3% of net income and 2,890 (2,834 for 2025) | Administrative figure. ITA s 118.2(1) | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Tradesperson's tools threshold | 1,501 | Administrative. ITA s 8(1)(s) | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Lifetime capital gains exemption | 1,275,000 (1,250,000 for 2025) | Administrative figure. ITA s 110.6(2) and (2.1), indexed from 2026 by s 117.1 | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html |
| Alternative minimum tax | 20.5% of adjusted taxable income over 181,440, less the basic minimum tax credit | Enacted, ITA s 127.51. Band figure administrative | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ and https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |

### Corporate rates

| Item | Rate or limit | Status | Source |
| --- | --- | --- | --- |
| Federal general rate | 15% net: 38% (s 123) less 10% abatement (s 124) less 13% reduction (s 123.4) | Enacted | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ and https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Federal small business rate | 9% net: the 19% deduction in s 125(1.1) replaces the 13% | Enacted | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ and https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Business limit | $500,000 shared by associated corporations, s 125(2) and (3) | Enacted | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| Tax on CCPC investment income | Additional 10 2/3%, s 123.3. Refund mechanism in s 129 | Enacted | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |

Provincial rates, excluding Quebec and Alberta, from the CRA table:

| Province or territory | Lower rate | Higher rate | Business limit | Source |
| --- | --- | --- | --- | --- |
| British Columbia | 2% | 12% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Manitoba | Nil | 12% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| New Brunswick | 2.5% | 14% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Newfoundland and Labrador | 2.0% from 1 January 2026 (2.5% before) | 15% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Northwest Territories | 2% | 11.5% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Nova Scotia | 1.5% | 14% | $700,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Nunavut | 3% | 12% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Ontario | 2.2% from 1 July 2026 (3.2% before), prorated by days, Taxation Act, 2007, s 31(4) | 11.5% | $500,000 | https://www.ontario.ca/laws/statute/07t11 and https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Prince Edward Island | 1% | 15% | $600,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Saskatchewan | 1% | 12% | $600,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Yukon | Nil | 12% | $500,000 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html |
| Alberta | Held: the CRA table excludes it and the Alberta page read gives the $500,000 threshold, not the rate | Held | $500,000 | https://www.alberta.ca/corporate-income-tax |
| Quebec | Held | Held | Held | unverified, CRA table excludes it |

### Dividends

| Item | Non-eligible dividend | Eligible dividend | Status | Source |
| --- | --- | --- | --- | --- |
| Gross-up | 15% | 38% | Enacted, ITA s 82(1)(b) | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| Federal credit | 9/13 of the gross-up | 6/11 of the gross-up | Enacted, ITA s 121 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| Ontario credit, years ending before 2027 | 22.895% of the gross-up | 36.3158% of the gross-up | Enacted, Taxation Act, 2007, s 19.1 | https://www.ontario.ca/laws/statute/07t11 |
| Ontario credit, years ending after 2026 | 15.2283% of the gross-up | 36.3158% of the gross-up | Enacted, same section | https://www.ontario.ca/laws/statute/07t11 |
| British Columbia credit | 15% of the gross-up | 43 11/19% of the gross-up | Enacted, Income Tax Act (BC) s 4.69 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 |

Other provincial dividend credits were not read and are held.

### Capital gains

| Item | Amount | Status | Source |
| --- | --- | --- | --- |
| Inclusion rate | One half, ITA s 38(a) and (b) | Enacted | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| Two-thirds inclusion rate | Never law | Withdrawn. Proposed in Budget 2024, deferred on 31 January 2025 to 1 January 2026, cancelled by the Prime Minister on 21 March 2025. Finance confirms it was not proceeded with | https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-2.html, https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase and https://www.canada.ca/en/department-finance/news/2025/01/government-of-canada-announces-deferral-in-implementation-of-change-to-capital-gains-inclusion-rate.html |

### Registered plans

| Plan | 2026 amount | Status | Source |
| --- | --- | --- | --- |
| RRSP dollar limit | $33,810 for 2026 and $35,390 for 2027. Room is the lesser of the limit and 18% of prior-year earned income, less pension adjustments, plus unused room | Administrative figures. ITA s 146(1), s 146(5) and s 204.2(1.1) | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html |
| TFSA dollar limit | $7,000. Total of annual limits 2009 to 2026 is $109,000, which only someone aged 18 or over and resident in Canada in every year since 2009 has in full | Administrative figures. ITA s 207.01(1) | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html |
| FHSA | $8,000 plus a carryforward of up to $8,000, $40,000 lifetime deduction | Enacted, ITA s 146.6 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ |
| RESP | $50,000 lifetime contributions. CES grant of 20% of the contribution, up to $500 on $2,500 of current room, $1,000 a year with unused room, $7,200 lifetime | Enacted, ITA s 204.9 and Canada Education Savings Act s 5 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ and https://laws-lois.justice.gc.ca/eng/acts/C-3.6/ |
| RDSP | $200,000 lifetime contributions. Grant up to $3,500 on $1,500 of contributions, or $1,000 on $1,000, by income. Bond up to $1,000. Caps: $10,500 grant a year, $70,000 grant lifetime, $20,000 bond lifetime | Enacted, ITA s 146.4 and Canada Disability Savings Act ss 6 and 7. Income thresholds not read | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ and https://laws-lois.justice.gc.ca/eng/acts/C-3.5/ |

### Payroll contributions

| Item | 2026 amount | Status | Source |
| --- | --- | --- | --- |
| CPP base | 5.95% each from employee and employer on $3,500 to $74,600. Maximum $4,230.45 each, $8,460.90 self-employed | Administrative figures. Canada Pension Plan | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| CPP second contributions | 4% each on $74,600 to $85,000. Maximum $416 each, $832 self-employed | Administrative figures | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html and https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| EI, outside Quebec | Employee 1.63% to $68,900, maximum $1,123.07. Employer maximum $1,572.30 | Administrative figures | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| EI, Quebec | Employee 1.30%, maximum $895.70. Employer maximum $1,253.98 | Administrative figures | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| QPP and QPIP | Held | Not read | unverified, no source read |

### Interest rates

| Item | Rate | Status | Source |
| --- | --- | --- | --- |
| Prescribed rate for taxable benefits and loans | 3% in each quarter of 2026 | Administrative. Income Tax Regulations s 4301 | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html, https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q2.html, https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q3.html and https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html |
| Interest on overdue tax, Q4 2026 | 7% | Administrative | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html |

### GST/HST

| Item | Amount | Status | Source |
| --- | --- | --- | --- |
| GST | 5%, ETA s 165(1) | Enacted | https://laws-lois.justice.gc.ca/eng/acts/E-15/ |
| HST | 13% Ontario, 14% Nova Scotia, 15% New Brunswick, Newfoundland and Labrador, Prince Edward Island | Administrative table. ETA s 165(2) | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html |
| Small supplier limit | $30,000, ETA s 148 | Enacted | https://laws-lois.justice.gc.ca/eng/acts/E-15/ |
| Quick Method limit | Total threshold amount of $400,000, Streamlined Accounting (GST/HST) Regulations s 16 | Enacted | https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-51/ |
| New housing rebate | Up to $6,300, phased out from $350,000 to $450,000, ETA s 254(2) | Enacted | https://laws-lois.justice.gc.ca/eng/acts/E-15/ |

## The base

### Sole proprietor or CCPC

- **Sole proprietor.** Business income is taxed at personal marginal rates. A business loss offsets other income in the year (ITA s 3). There are no payroll remittances on the owner's own earnings. The owner pays both halves of CPP on self-employed earnings with the return. Employees bring ordinary payroll duties.
- **CCPC.** A corporation that was a CCPC throughout the year deducts the small business deduction rate on the least of 3 amounts (ITA s 125(1)): (a) its income from active businesses carried on in Canada, with specified partnership and specified corporate income, less active business and specified partnership losses, subject to the exclusions in s 125(1)(a)(i); (b) taxable income less the amounts in s 125(1)(b)(i) to (iii), which turn on foreign tax credits and on income that an Act of Parliament keeps out of Part I tax; and (c) the business limit. The federal rate on that amount is 9%. The combined rate on the table above runs from 9% (Manitoba, Yukon) to 12% (Nunavut). Ontario is 11.2% after 30 June 2026 and about 11.70% across calendar 2026. Alberta and Quebec are held.
- **Integration.** Corporate and personal tax on the same income is designed to approximate personal tax alone. The gap varies by province, year and income. Measure it: do not assume it.
- **When to incorporate.** No primary source read sets a profit level at which incorporating pays, so the rule of thumb of about $70,000 to $80,000 is held and must not be given as a test. The result depends on the owner's spending needs, province, deferral period, CPP and RRSP goals and compliance cost. Deferral arises only on profit left in the corporation.

**Business limit grinds.** The $500,000 limit is reduced by the greater of 2 amounts, and cannot fall below nil (ITA s 125(5.1)):

- Taxable capital: `A x B / 90,000`, where A is the business limit before this reduction and `B = 0.225% x max(C - 10,000,000, 0)`. C is taxable capital employed in Canada. If the corporation is not associated in the current or the preceding year, it is the corporation's own figure for the preceding year (s 125(5.1)(a)(i)). If it is not associated in the current year but was in the preceding year, it is the corporation's own figure for the current year (subparagraph (ii)). If it is associated in the current year, it is the total for the corporation and each corporation it is associated with, each for its last taxation year that ended in the preceding calendar year (subparagraph (iii)).
- Passive income: `D / 500,000 x 5 x max(E - 50,000, 0)`, where D is the same limit and E is the adjusted aggregate investment income of the corporation and every corporation associated with it, for taxation years that ended in the preceding calendar year.

A corporation's limit is `max(limit - greater of the 2 amounts, 0)`, so at E of $150,000 a $500,000 limit is nil. Section 125(5.2) deems a related, non-associated corporation associated for the passive income test if property was lent or transferred to it and one of the reasons was to reduce E. A year under 51 weeks prorates the limit (s 125(5)(b)). Ontario does not parallel the passive income grind (https://www.ontario.ca/document/corporations-tax/corporate-income-tax). Other provinces are held.

**Passive income in a CCPC.** A corporation is not a shelter for investment income. Section 123.3 adds 10 2/3% to federal tax, part of which is refundable through s 129 when taxable dividends are paid. Whether retained investing beats personal investing depends on rates, the dividend refund and the grind above, so it stays a modelled question.

### Salary or dividends

| Factor | Salary | Dividends |
| --- | --- | --- |
| Corporate deduction | Yes, if reasonable (ITA s 67) | No |
| CPP | Yes, on pensionable earnings | No |
| EI | Yes, unless the person controls more than 40% of the voting shares (EI Act s 5(2)(b)), or the employer and employee do not deal at arm's length (s 5(2)(i)). A related employer and employee are treated as dealing at arm's length only if the Minister is satisfied under s 5(3)(b). The other s 5(2) exclusions were not tested | No |
| RRSP room | Yes, 18% of earned income (ITA s 146(1)) | No: dividends are not earned income |
| Child care deduction | Salary counts for the 2/3 earned income limit (ITA s 63) | Dividends do not |
| Personal tax | Marginal rates | Gross-up and dividend tax credit |
| Admin | T4 and remittances | T5 |

- **RRSP room from salary.** 2026 room needed $187,833.34 of 2025 earned income to reach $33,810. 2027 room needs $196,611.12 of 2026 earned income to reach $35,390.
- **Eligible or non-eligible.** Income taxed at the small business rate generally pays out as non-eligible dividends. An eligible dividend needs the written designation at payment in ITA s 89(14) and a general rate income pool. An excessive designation has its own tax (ITA s 89(1) and Part III.1). Do not assume eligible treatment on small business income.
- **No universal answer.** Model each year with the client's province, income, spending, RRSP and CPP goals and retained earnings. Example 1 shows how the result moves.
- **Ontario change.** The non-eligible dividend credit rate falls for years ending after 2026. The Ontario lower corporate rate fell for days after 30 June 2026. A 2026 result does not carry to 2027.

### TOSI (tax on split income)

TOSI taxes split income at the highest individual percentage with limited credits (ITA s 120.4(2) and (3)). It applies to a 'specified individual': an individual, not a trust, resident in Canada at the end of the year (or immediately before death). Someone who had not turned 17 before the year also needs a parent resident in Canada at any time in the year.

Split income is the following, less excluded amounts (ITA s 120.4(1)):

- (a) Taxable dividends on shares not listed on a designated stock exchange, other than mutual fund corporation shares, and s 15 amounts on unlisted shares.
- (b) A partnership's share of income from a related business, or from renting property where a related person is actively engaged or holds an interest.
- (c) Trust income of the same kinds, other than from a mutual fund trust or a trust deemed by s 143(1).
- (d) Income on debt of a private corporation, partnership or trust, with exceptions for fully exempt interest, listed or publicly traded debt and bank or credit union deposits.
- (e) Taxable capital gains or profits from disposing after 2017 of unlisted shares, or of partnership, trust or debt interests linked to split income or to such shares.

**Salary is not on that list.** Excess pay to a family member is a reasonableness problem under ITA s 67, not a TOSI problem.

An amount escapes TOSI if it is an excluded amount. Test each limb:

| Limb of 'excluded amount' | Who | Condition |
| --- | --- | --- |
| (a) | Had not turned 24 before the year | Property acquired because of the death of a parent, or of any person if the individual is a full-time post-secondary student in the year or qualifies for the s 118.3 disability amount |
| (b) | Any age | Property acquired under a transfer described in s 160(4) |
| (c) | Any age | Taxable capital gain arising because of s 70(5) |
| (d) | Any age | Taxable capital gain on qualified farm or fishing property or qualified small business corporation shares, unless s 120.4(4) or (5) would deem it a dividend |
| (e)(i) | Turned 17 before the year | Not derived from a related business |
| (e)(ii) | Turned 17 before the year | Derived from an excluded business of the individual |
| (f)(i) | Turned 17 but not 24 before the year | Safe harbour capital return |
| (f)(ii) | Turned 17 but not 24 before the year | Reasonable return, looking only at the individual's arm's length capital |
| (g)(i) | Turned 24 before the year | Income or taxable capital gain from excluded shares |
| (g)(ii) | Turned 24 before the year | Reasonable return, having regard to the work done, property contributed, risks assumed, amounts already paid and other relevant factors, for the individual and each source individual |

- **Excluded business.** The individual is actively engaged on a regular, continuous and substantial basis in the year, or in any 5 prior taxation years. The current-year route does not apply to split income limb (e). Working an average of at least 20 hours a week during the part of the year the business operates is deemed to meet the test (s 120.4(1.1)(a)). The deeming rule is one way to meet the test.
- **Excluded shares.** All 3 conditions must hold. Less than 90% of the corporation's business income for its last year came from services, and it is not a professional corporation. Immediately before the time, the individual owns shares with at least 10% of the votes and at least 10% of the value of all issued shares. All or substantially all of its income is not derived from a related business other than its own.
- **Spouse aged 65.** An amount is deemed excluded if it would be excluded for the spouse or common-law partner and that person turned 64 before the year, or for a spouse who has died (s 120.4(1.1)(c)).
- **Left out here.** Section 120.4(1.1)(b) carries a deceased person's contributions, work and age to inherited property. Section 120.4(1.1)(d) adds greater certainty rules. Section 120.4(1.1)(e) treats a spouse or common-law partner living separate and apart at the end of the year, because of a breakdown of the relationship, as unrelated. Section 120.4(4) applies where a specified individual who had not turned 17 before the year has a taxable capital gain, other than an excluded amount, from shares transferred to a non-arm's length person, except shares of a class listed on a designated stock exchange or of a mutual fund corporation. The gain is deemed not to be a taxable capital gain, and twice the amount is deemed a taxable dividend that is not an eligible dividend. Section 120.4(5) applies the same doubling to an amount that s 104(13) or 105(2) would include, to the extent it is attributable to such a gain of a trust. Read them where they arise. Any Quebec parallel is held.

### Attribution and prescribed rate loans

Income from property lent or transferred to a spouse is attributed back to the lender (ITA s 74.1). Capital gains (s 74.2) and transfers to minors (s 74.1(2)) have their own rules, not restated here. Section 74.5(2) switches attribution off for a loan only if both conditions are met:

1. Interest is charged at no less than the lesser of the prescribed rate when the loan was made and an arm's length rate.
2. Interest for the year and each earlier year is paid no later than 30 days after the year end.

Miss a payment date and the exception fails for that year and later years. The prescribed rate was 3% in each quarter of 2026. The rate is tested when the loan is made, so a later rise does not change it. Lending before a quarterly rise locks in the lower rate, if the loan suits the family on its own investment case. The lender reports the interest. The borrower can deduct it only if ITA s 20(1)(c) is met, and keeps the excess return.

### Deductions and credits

| Item | Provision | Rule and condition |
| --- | --- | --- |
| Home office, employee | ITA s 8(1)(f), 8(1)(i), 8(13), 8(10) | The work space must be where the duties are principally performed, or be used exclusively in the period to earn the employment income and regularly and continuously to meet customers or others. Limited to income from that employment, excess carried forward. Employer certificate T2200 required |
| Home office, self-employed | ITA s 18(12) | Principal place of business, or used exclusively to earn business income and regularly and continuously to meet clients, customers or patients. Limited to business income, excess carried forward. The claim is the work space's share of rent, mortgage interest, utilities, insurance and property tax, each allowable only to that share |
| Moving | ITA s 62 and s 248(1) 'eligible relocation' | The old home must be at least 40 km further from the new work location than the new home is. Deduct against income at the new location. The student limb is left out here |
| Carrying charges | ITA s 20(1)(c) | Reasonable interest on borrowed money used to earn business or property income, under a legal obligation |
| Investment counsel fees | ITA s 20(1)(bb) | Not commissions. Paid to a person whose principal business is advising on specific shares or securities, or includes administering or managing them, for that advice or those services |
| Medical | ITA s 118.2 | 14% credit for 2026 (14.5% for 2025, on Federal Tax Expenditures 2026) on expenses above the ceiling. Premiums, dental costs, prescriptions and travel each need a limb of s 118.2(2). The limbs were not tested here, except that travel needs at least 40 km under (g) and 80 km under (h) |
| Disability | ITA s 118.3 | Amount of $10,341, credited at 14%, not a credit of that size. Transferable on the terms of s 118.3(2) and (3). Eligibility is the door to an RDSP |
| Northern residents | ITA s 110.7 | At least 6 consecutive months in prescribed zones. Residency deduction and travel benefit. Zones and daily amounts held |
| Union and professional dues | ITA s 8(1)(i)(i), (iv), (v) | Employment deduction for the dues those subparagraphs list: professional dues to keep a status recognised by statute, and union dues |
| Child care | ITA s 63 | $8,000 for a child under 7 at year end, $5,000 for another eligible child, $11,000 if the disability amount can be claimed for the child. Eligible child: under 16 at any time in the year, or dependent by infirmity. Limited to 2/3 of earned income. The lower-income supporting person claims, with the exceptions in s 63(2) |
| Apprentice mechanic tools | ITA s 8(1)(r) | Cost above the greater of $2,501 for 2026 ($1,000 plus the Canada employment amount) and 5% of the income the paragraph counts |
| Tradesperson's tools | ITA s 8(1)(s) | Lesser of $1,000 and tools cost over $1,501 (2026) |
| Charitable gifts | ITA s 118.1 | See Timing |

### Capital cost allowance

| Class | Rate (Income Tax Regulations s 1100(1)(a)) | Property | Source |
| --- | --- | --- | --- |
| 1 | 4% | Buildings, including those acquired after 1987, as Schedule II describes | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 8 | 20% | Property not in another class, such as furniture, fixtures and machinery, as Schedule II describes | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 10 | 30% | Motor vehicles within Schedule II | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 10.1 | 30% | Passenger vehicle above the prescribed cost, each in a separate class | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 12 | 100% | Items Schedule II lists, including a tool costing under $500, other than an electronic communication or data processing device (paragraph (h)), and computer software other than systems software (paragraph (o)) | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 50 | 55% | General-purpose electronic data processing equipment and systems software | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |
| 54 | 30%, with its own first-year factor in Regulation 1100(2) | Zero-emission vehicle not in Class 16 or 55 | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ |

- **Vehicle ceilings.** Regulation 7307(1), read at 21 June 2026, gives $38,000 for automobiles acquired after 2024. Finance announced $39,000 for acquisitions on or after 1 January 2026. That is proposed on the text read: **held**. The zero-emission ceiling is $61,000 plus sales tax (Regulation 7307(1.1)). Finance's release gives $1,100 a month for leases and $350 a month for interest.
- **Accelerated Investment Incentive.** Accelerated property is acquired after 20 November 2018 and before 2025 and available for use before 2028. Reaccelerated property is acquired after 2024 and available before 2034 (Regulation 1104(4) and (4.01)). The half-year rule does not apply to either. For general classes Regulation 1100(2) also adds 1/2 of net additions if the property was available before 2024 (accelerated) or before 2030 (reaccelerated), and nothing after those dates. So the first-year claim is 1.5 times the normal rate, or 3 times a half-year claim. Classes 12, 13, 14, 15, 43.1, 44, 46, 50, 53 to 56 and 59, and property in paragraphs (1)(v) and (ze), have their own factors: read the descriptions of A and A.1 for the class and year. Straddle years use Regulation 1100(2.01) and (2.011).
- **Available for use.** No CCA arises until property is available for use (ITA s 13(26) to (28)). Buying in December does not by itself give a claim.
- **Rental property.** CCA cannot create or increase a rental loss (Regulation 1100(11)).
- **Immediate expensing.** Regulation 1100(0.1) allows the least of the immediate expensing limit, up to $1.5 million a year, the undepreciated capital cost of designated immediate expensing property and, for a person other than a CCPC, the income from the business or property in which it is used, computed without regard to ITA s 20(1)(a). Associated eligible persons share the limit (Regulation 1104(3.2) and (3.3)). Property in Classes 1 to 6, 14.1, 17, 47, 49 and 51 is excluded. A CCPC needed acquisition after 18 April 2021, and an individual or Canadian partnership acquisition after 2021. Availability for use had to be before 2025 for an individual, or a Canadian partnership all of whose members were individuals throughout the year, and before 2024 in any other case. The property also had to meet limb (c) of the definition in Regulation 1104(3.1). Either it had not been used before acquisition and no one had deducted an amount for it under ITA s 20(1)(a) or s 20(16) for a year ending before acquisition. Or it was not acquired in the circumstances in (c)(ii)(A), a deemed prior deduction or reduced undepreciated capital cost, and had not been owned or acquired before by the person or by a non-arm's length person. On the regulations read, those windows have closed.
- **Productivity Mega Deduction.** A Finance backgrounder of September 2026 proposes permanent immediate expensing for most depreciable property acquired on or after 15 September 2026, with listed exclusions. **Proposed, held.** Do not claim it on the text read.

### Losses

- **Non-capital losses:** carry back 3 years and forward 20 years (ITA s 111(1)(a)). Corporate losses stay in the corporation.
- **Net capital losses:** carry back 3 years and forward without limit against taxable capital gains (ITA s 111(1)(b)). In the year of death and the prior year they may offset any income, as s 111(2) sets out, subject to the reduction in s 111(1.1)(b) as modified there.
- **Allowable business investment loss:** one half of a business investment loss (ITA s 38(c)). A business investment loss needs a disposition to an arm's length person, or a s 50(1) deemed disposition, of a share of a small business corporation or a qualifying debt (ITA s 39(1)(c)). It is deductible against all income. Earlier capital gains exemption claims reduce it (s 39(9)). The unused part enters the non-capital loss. Its later treatment in s 111(8) is held.
- **Superficial loss:** nil for the seller if the seller or an affiliated person acquires the same or an identical property in the 30 days before or after, and holds it at the end of that period (ITA s 54 and s 40(2)(g)(i)). Paragraphs (c) to (h) of the definition except some dispositions. The denied loss is added to the substituted property's cost (s 53(1)(f)).
- **Spouse transfers.** A spouse is an affiliated person (ITA s 251.1). A transfer to a spouse rolls over at cost unless the transferor elects out (ITA s 73(1)). If elected out at fair market value, the loss is superficial where the spouse holds the property 30 days later. Attribution may also apply. A transfer does not simply 'trigger a loss'.
- **Offsetting gains.** Capital gains and losses can be realised in the same year to offset. Crystallising a loss before year end is sound only outside the superficial loss period.

### Timing

| Strategy | Rule and condition |
| --- | --- |
| RRSP contribution | Premiums paid by 60 days after year end can be deducted for the year (ITA s 146(5)). For 2026 that is 1 March 2027. A deduction can be held back for a higher-income year. A plan cannot mature after the end of the year the annuitant turns 71 (s 146(2)(b.4)), so check age before relying on the 60 days |
| Deferring self-employed income | Amounts rendered are receivable, and an account is treated as rendered on the day it would have been rendered without undue delay (ITA s 12(1)(b)). Delaying an invoice past 31 December does not by itself defer income |
| Deferring employment income | Employees are taxed on receipt (ITA s 5). A deferred bonus can be a salary deferral arrangement (s 248(1)) if one of the main purposes of the right is to postpone tax. An employer must pay within 180 days of its year end to keep its deduction in that year (s 78(4)) |
| Prepaying expenses | Amounts for services rendered after year end, for interest, taxes, rent or royalties for a later period, and for insurance for a later period are not deductible until then (ITA s 18(9)). A prepayment does not accelerate those deductions |
| Buying CCA assets | Buying before year end helps only if the property is available for use in the year |
| Charitable gifts | Credit at the lowest rate on the first $200, 33% to the extent income is above the top bracket, and 29% on the rest (ITA s 118.1(3)). Gifts carry forward 5 years. Gifts by a spouse or common-law partner can count, so one spouse can pool them and pass the $200 line once (s 118.1(1) 'total charitable gifts'). The limit is the lesser of income and 75% of income with add-ons (s 118.1(1) 'total gifts') |
| Capital gains deferral | No holding period discount was found in s 38 or s 39, so holding only defers: a gain is realised on disposition. A CCPC does not shelter passive income, as the corporate section above shows |
| LCGE crystallisation | Realising a gain on qualifying shares to use the exemption: see below |
| Prescribed rate loan | Lock in a lower rate before a quarterly rise: see above |

**Capital gains exemption.** ITA s 110.6(2.1) gives a resident individual, not a trust, a deduction on gains from qualified small business corporation shares, to a lifetime limit of $1,275,000 of gains for 2026 (half that as a deduction). All of these must hold:

- At the determination time the share is a share of a small business corporation, owned by the individual, their spouse or common-law partner, or a related partnership. A small business corporation is a CCPC with all or substantially all of the fair market value of its assets used principally in an active business carried on primarily in Canada by it or a related corporation, or being shares or debt of connected small business corporations (ITA s 248(1)).
- Through the prior 24 months no one owned the share except the individual or a related person or partnership, subject to the exceptions in the definition.
- Through those 24 months it was a share of a CCPC with more than 50% of the fair market value of its assets meeting the active business test, with stacking rules where holding companies are involved.
- The claim fits the annual gains limit and cumulative gains limit, and is reduced by a cumulative net investment loss (ITA s 110.6(1)).
- The individual is resident in Canada throughout the year (s 110.6(2.1)). Part-year residence rules are left out here.

Section 110.6(6) and (7) can deny it. Crystallising raises the cost of the shares, but it does not change the conditions, and it can create alternative minimum tax (Example 3). Check the share tests with a reviewer before any step. Whether it is wise depends on the client's future sale, AMT cash and provincial position.

### GST/HST

- **Registration.** A person making taxable supplies in Canada in a commercial activity must register, unless they are a small supplier, or within ETA s 240(1)(b) (real property sold outside a business) or (c) (a non-resident not carrying on business in Canada). A small supplier's consideration for taxable supplies made inside or outside Canada, with those of its associates at the start of the quarter, is $30,000 or less over the 4 preceding calendar quarters ($50,000 for a public service body). Goodwill, financial services and sales of capital property do not count (s 148(1)). If the amount in one calendar quarter passes the limit, the person stops being a small supplier immediately before that time (s 148(2)). Taxi businesses must register regardless (s 240(1.1)). Voluntary registration allows input tax credits (ITCs), but tax must then be charged. Section 240(3) was not read in full.
- **Quick Method.** A specified registrant whose total threshold amount is $400,000 or less, and that carried on commercial activities throughout the prior 365 days, can elect (Streamlined Accounting (GST/HST) Regulations s 16(1)). The total threshold amount annualises tax-included taxable supplies by the registrant and its associates, excluding financial services and sales of real property or capital assets (s 2(3)). These are not specified registrants: listed financial institutions, charities, selected public service bodies, public institutions, qualifying non-profit organisations, and anyone who in the prior 4 fiscal quarters gave legal, accounting or actuarial services in a professional practice, or book-keeping, financial consulting, tax consulting or tax return preparation services. The rate depends on where the establishment and the supply are (s 15(5)). For an Ontario establishment making an Ontario supply it is 4.4% if the cost of goods bought for resale in the threshold period is at least 40% of the basic threshold amount, and otherwise 8.8%. For a non-participating province establishment making a supply in such a province it is 1.8% or 3.6% on the same test. Read s 15(5) for any other pair. The method often suits a service business with few inputs, if the sums compare well with actual ITCs. How it treats ITCs on capital property is held.
- **ITCs.** ETA s 169(1) allows credits to the extent property or services are for commercial activities. Section 169(4) needs prescribed information before the return. The Input Tax Credit Information (GST/HST) Regulations s 3 set it by amount: under $100, supplier name, invoice date and total. $100 to under $500, add the supplier's registration number and tax details. $500 or more, add the recipient's name, terms of payment and a description of each supply.
- **Vehicles.** Section 169(1) gives credits to the extent of commercial use for inputs generally. The passenger vehicle rules in ETA ss 199 to 202 are held. A logbook is evidence of use, and no statutory logbook duty was read here.
- **Real property.** Self-supply rules deem a sale and purchase where a builder occupies or rents a new residential complex (ETA s 191). The new housing rebate is the lesser of $6,300 and 36% of the total tax paid where consideration is $350,000 or less, phased out to nil at $450,000 (s 254(2)). A first-time home buyer has an additional rebate up to $50,000 for agreements after 19 March 2025 and before 2031, phased out from $1,000,000 to $1,500,000 (s 254(2.1)). The rebate conditions need testing in full.
- **Place of supply.** The rate follows the place of supply rules, which depend on the supply. A supplier does not choose a rate. Do not plan on moving a supply to a lower-rate province without the facts changing. Schedule IX was not read: held.
- **Exports.** Only the supplies in Schedule VI, Part V are zero-rated, on their own conditions. For example, section 1 needs a non-consumer recipient, prompt export, no use in Canada first, and evidence. ITCs stay available on zero-rated supplies, which are taxable at 0% (ETA s 165(3)).

### CPP and EI planning

- **Self-employed.** Both halves: 11.9% on the first ceiling and 8% on the second.
- **Owner-managers on dividends only.** No CPP contributions and no CPP accrual from that income. That trades lower current cost for lower pension.
- **Cost of CPP.** The 2026 maximum on both halves of both tiers is $9,292.90 (2 x $4,646.45), before the deduction and credit in ITA ss 60(e), 60(e.1) and 118.7. An owner who does not need the benefits avoids this with dividends. EI is nil for an owner above the 40% line.
- **Building entitlement.** Maximum 2026 contributions need pensionable earnings of $85,000 or more. Earnings above the $3,500 exemption bring some contributions. Pension amounts are not modelled here, so 'minimum salary' levels are held.
- **EI for the self-employed.** Part VII.1 of the EI Act provides special benefits by agreement. Its entry terms and premiums are held. Dividends carry no EI premium and no EI entitlement.
- **Trade-off.** Balance CPP against RRSP room, which needs earned income.

### Registered accounts

- **RRSP.** Deductible. Growth is deferred. Withdrawals are income.
- **TFSA.** No deduction. Growth and withdrawals are free of tax within room. Tax applies to excess amounts (ITA s 207.02).
- **FHSA.** Deduct up to the annual limit, with a qualifying withdrawal free of tax. To open one, the CRA requires age 18, or 19 where that is the province's contract age, age 71 or under at 31 December of the opening year, Canadian residence, and first-time home buyer status. That status needs no principal residence in a qualifying home the person owned or jointly owned in the calendar year or the prior 4 calendar years. It also needs either no spouse or common-law partner when opening, or no such residence in a home that person owned or jointly owned in the same period (https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/opening-your-fhsas.html). The participation period ends at the end of the year after the earliest of the 14th anniversary of the first account, turning 70 and the first qualifying withdrawal (ITA s 146.6(1)).
- **RESP.** No deduction. Grants added. Growth and grants are taxed to the student when paid as educational assistance (ITA s 146.1). Additional grant on lower incomes (Canada Education Savings Act s 5(4)).
- **RDSP.** Needs a beneficiary eligible for the disability amount. No deduction. Contributions end after the year the beneficiary turns 59.

**Order of use.** A sensible order depends on facts, so state it as a condition:

1. FHSA, if the client qualifies and intends to buy a home.
2. Employer RRSP or pension matching, if offered and the plan terms suit the client.
3. TFSA, if the client's bracket is low now and expected to rise.
4. RRSP, if the marginal rate now exceeds the rate expected at withdrawal (Example 2).
5. RESP, if a child has unused grant room.
6. Non-registered, with Canadian dividends and capital gains (one half inclusion), subject to the client's rate, income-tested benefits and asset mix.

## Deadlines and filing

| When | What | Basis |
| --- | --- | --- |
| January | New TFSA and FHSA room. Check the prescribed rate before lending | ITA s 207.01, s 146.6, Reg 4301 |
| February | Model the RRSP and TFSA split before the RRSP date | Practice |
| 1 March 2027 | Last day for RRSP premiums deductible for 2026. In 2026 CRA gave 2 March, as 1 March fell on a Sunday | ITA s 146(5), https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html |
| 15 March, 15 June, 15 September, 15 December | Individual instalments, if the instalment threshold is met: net tax owing over $3,000, or $1,800 for a Quebec resident. See `ca-fed-instalments` | ITA s 156, s 156.1 |
| 31 March | T1-OVP for RRSP excess contributions | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html |
| 30 April 2027 | 2026 return, and tax owing for all individuals, including CPP on self-employed earnings. EI premium timing for an opted-in self-employed person is held | ITA s 150(1)(d)(i), s 248(1), Canada Pension Plan s 33 |
| 15 June 2027 | 2026 return for an individual who carried on a business, and their cohabiting spouse. Tax was still due 30 April | ITA s 150(1)(d)(ii) |
| 30 June 2027 | Taxes on TFSA excess, if applicable | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html |
| 6 months after corporate year end | T2 return | ITA s 150(1)(a) |
| 3 months after corporate year end | Balance of tax for a corporation that was a CCPC throughout the year and meets the small business conditions in paragraph (d) of the definition. 2 months otherwise | ITA s 248(1) 'balance-due day' |
| Corporate year end | A corporation's fiscal period may not end more than 53 weeks after it began (s 249.1(1)(a)), and no statute read fixes 30 June or another date. A professional corporation that is a member of a partnership within s 249.1(1)(b)(ii) has a calendar year limit, unless the business is not carried on in Canada (s 249.1(1)(b)(iii)). Changing a year end needs the Minister's concurrence (s 249.1(7)). Review the salary and dividend mix before the year end | ITA s 249.1(1), (7) |
| September | Model the year-end position and check instalments | Practice |
| October and November | Harvest gains and losses outside the superficial loss period. Make gifts. Prepaying expenses helps only as s 18(9) allows | ITA s 54, s 118.1, s 18(9) |
| 31 December | TFSA contributions for the calendar year. RESP contributions for that year's grant. Trust amounts paid or payable to beneficiaries (ITA s 104(24)). Pay salary or bonus by this date for 2026 earned income (ITA s 5). RRSP premiums for someone who turns 71 in the year, as the plan matures by the end of that year (s 146(2)(b.4)). T3 and T5013 slip dates held | As cited |

Deal with the CRA through its portals: individuals use [My Account](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-individuals/account-individuals.html) and businesses use [My Business Account](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/business-account.html). Alberta corporations file the AT1 with Alberta using its net file service (https://www.alberta.ca/corporate-income-tax). Revenu Quebec filing is held.

## Penalties and interest

| Trigger | Consequence | Basis |
| --- | --- | --- |
| Dividends to family inside TOSI | Tax at the top rate, limited credits, interest | ITA s 120.4, s 161 |
| Superficial loss | Loss denied to the seller | ITA s 54, s 40(2)(g)(i) |
| Pay to family members above what is reasonable | Deduction denied. Not TOSI | ITA s 67 |
| Personal expenses paid by a corporation | Shareholder benefit | ITA s 15(1) |
| Shareholder loan | Included in the debtor's income, unless the debtor is a corporation resident in Canada or a partnership of them, or the debt is a pertinent loan or indebtedness, or an exception applies. It is not a deemed dividend. The exceptions are: a debt in the ordinary course of the creditor's business, or a loan in an ordinary money lending business that meets the 90% arm's length test, with bona fide repayment arrangements (s 15(2.3)); a loan to an employee who is not a specified employee, or an employee's home, new treasury share or work vehicle loan, if employment and not a shareholding is the reason and bona fide repayment arrangements were made (s 15(2.4)); a private corporation's loan to its own trust for buying and selling shares from or to non-specified employees (s 15(2.5)); a loan for a qualifying business transfer to an employee ownership trust, with arrangements to repay within 15 years (s 15(2.51)); and a loan repaid within one year after the lender's year end and not part of a series (s 15(2.6)). Imputed interest under s 80.4(2) does not apply to a loan so included (s 80.4(3)(b)), and s 80.4(3)(a) and (c) are further exceptions. Each limb of s 15(2.4) and (2.5) has more detail, so read it where it arises | ITA s 15(2) |
| Automobile benefits | Standby charge and operating benefit | ITA s 6(1)(e), (k), (l), s 6(2) |
| Non-arm's length purchase above fair market value, or disposal for no proceeds or less than it. Also a gift to any person | Cost or proceeds deemed to be fair market value. A non-arm's length purchase below value, or sale above it, is outside s 69(1)(a) and (b) | ITA s 69(1). Section 247 applies only where a non-resident participant is involved |
| Late T1135 | Greater of $100 and $25 a day for up to 100 days, so a maximum of $2,500 | ITA s 162(7) |
| T1135 failure, knowing or grossly negligent | $500 a month for up to 24 months, less the s 162(7) penalty, then further penalties | ITA s 162(10), (10.1) |
| Unreported income, including underground economy activity | Penalties for repeated failure or gross negligence. How the CRA matches third-party data is held as not read | ITA s 163(1), (2) |
| RRSP over-contribution | 1% a month on the cumulative excess, which sits above a $2,000 allowance for someone who turned 18 in a preceding year. Waiver possible | ITA s 204.1(2.1), (4), s 204.2(1.1) |
| TFSA excess | 1% a month | ITA s 207.02 |
| FHSA excess | 1% a month | ITA s 207.021 |
| Aggressive tax shelters and mandatory disclosure failure | Reportable transaction, for a taxpayer: $500 a week up to the greater of $25,000 and 25% of the tax benefit, or for a corporation with assets of $50 million or more, $2,000 a week up to the greater of $100,000 and 25%. Advisers and promoters have a separate penalty. Uncertain tax treatment: $2,000 a week, up to $100,000. The notifiable transaction penalty in s 237.4 and the 2023 start dates are held | ITA s 237.3(8), s 237.4, s 237.5(5) |
| Overdue tax | Interest at the prescribed rate, 7% in Q4 2026 | ITA s 161, https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html |

### General anti-avoidance rule

ITA s 245 applies where a transaction gives a tax benefit, is an avoidance transaction, and is abusive.

- **Avoidance transaction (s 245(3)).** Unless it may reasonably be considered that obtaining the tax benefit is not one of the main purposes, a transaction resulting in a tax benefit, or in a series that does, is an avoidance transaction. This is a lower bar than the earlier 'primarily' test.
- **Abuse (s 245(4)).** Misuse of a provision or abuse of the Act read as a whole. Sections 245(4.1) and (4.2) add an economic substance indicator.
- **Consequence (s 245(2), (5.1)).** The benefit is denied. A penalty of 25% of the amount in s 245(5.1) can apply, unless the transaction was disclosed under s 237.3 or 237.4. Under s 245(5.2) it also does not apply if it was reasonable to conclude that s 245(2) would not apply, relying on published administrative guidance or court decisions about an identical or almost identical transaction. The reassessment period extends by 3 years unless the transaction was disclosed (s 152(4)(b)(viii)).

Application dates are not in the consolidation and are held.

Each planning step in this file sits under s 245. A step that fits a provision's words can still fail it. Series of steps need a reviewer.

### Disclosure rules

ITA s 237.3 requires reporting of a reportable transaction and s 237.4 of a notifiable transaction. Section 237.5 requires a reporting corporation to report uncertain tax treatments: a corporation with relevant financial statements, assets carrying at $50 million or more and a return to file. The hallmarks in ss 237.3 and 237.4 were not reduced to a test here, so a shelter or series goes to a reviewer.

### Red lines

- Never advise claiming personal expenses as business deductions.
- Never advise hiding income or assets offshore without proper disclosure (T1135, T1134).
- Never advise ignoring TOSI when splitting income with family members.
- Never advise repurchasing securities within 30 days to claim a loss. The loss is superficial.
- Never advise backdating transactions or documents.

A request for any of these is a refusal: state the trigger and stop that step.

## Cross-border points

- **T1135.** A specified Canadian entity whose specified foreign property cost more than $100,000 at any time in the year files by its filing-due date (ITA s 233.3(1), (3)). See `ca-fed-t1135`.
- **T1134.** A reporting entity files for each foreign affiliate within 10 months after year end (ITA s 233.4(4)).
- **Non-arm's length cross-border pricing.** ITA s 247 applies. See `canada-transfer-pricing`.
- **Residence.** The rules here assume residence in Canada throughout. Becoming or ceasing to be resident can change the capital gains exemption, TFSA, FHSA and RRSP results. See `ca-tax-residency`.
- **Interprovincial.** An individual's income is taxed in the province of residence on the last day of the year, unless they have business income from a permanent establishment outside it (Income Tax Regulations s 2601). Corporate taxable income is allocated to provinces under Part IV of the Regulations.

## Two worked examples that recompute

All examples use calendar 2026. They are illustrations for source checking, not advice. Each states what it leaves out.

### Example 1: salary or dividends, Ontario and British Columbia

**Stated inputs.** One CCPC, with one shareholder-manager resident in the province on 31 December 2026 and no other income, spouse or dependants. The corporation's only permanent establishment is in that province, so all its taxable income is allocated there. The salary is assumed reasonable under ITA s 67. Pre-owner active business income is $200,000 for a year ending 31 December 2026. The corporation is not associated, has adjusted aggregate investment income under $50,000 and taxable capital under $10 million. All after-tax income is paid out in 2026. The owner controls more than 40% of the votes, so no EI. Only basic personal, Canada employment and CPP credits are claimed. Employer health tax is nil in Ontario if the corporation is an eligible employer under the $1,000,000 exemption (Employer Health Tax Act, as read). The BC levy was not read and is excluded.

Ontario surtax uses the 2026 thresholds of $5,818 and $7,446 in [T4127 Table 8.2](https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/other-rates-amounts-26e.csv). They are the $4,006 and $5,127 in Taxation Act, 2007, s 16(1), indexed each year under s 23(1), paragraph 4, and s 23(2) and (3). The yearly chain of index factors was not recomputed. Surtax is computed before the Ontario dividend tax credit (s 5(1), paragraphs 5 and 6). The Ontario Health Premium on combined income follows s 24(2): $750 from $72,600 to $200,000, then 25% of the excess up to $900.

Salary is $195,353.55, as $4,646.45 of the $200,000 pays employer CPP. CPP splits as base credit $3,519.45 and deduction $1,127 ($711 first additional, $416 second).

```oa-check
name: Ontario 2026 all salary
inputs:
  pre_tax: 200000
  employer_cpp: 4646.45
  employee_cpp: 4646.45
  enhanced_deduction: 1127
  base_cpp: 3519.45
  cea: 1501
steps:
  - salary: pre_tax - employer_cpp
  - ti: salary - enhanced_deduction
  - fed_gross: pct(min(ti, 58523), 14) + pct(clamp(ti - 58523, 0, 58522), 20.5) + pct(clamp(ti - 117045, 0, 64395), 26) + pct(clamp(ti - 181440, 0, 77042), 29) + pct(max(ti - 258482, 0), 33)
  - bpa: 16452 - 1623 * min(max(ti - 181440, 0) / 77042, 1)
  - fed_tax: max(fed_gross - pct(bpa + cea + base_cpp, 14), 0)
  - on_gross: pct(min(ti, 53891), 5.05) + pct(clamp(ti - 53891, 0, 53894), 9.15) + pct(clamp(ti - 107785, 0, 42215), 11.16) + pct(clamp(ti - 150000, 0, 70000), 12.16) + pct(max(ti - 220000, 0), 13.16)
  - on_basic: max(on_gross - pct(12989 + base_cpp, 5.05), 0)
  - on_surtax: pct(max(on_basic - 5818, 0), 20) + pct(max(on_basic - 7446, 0), 36)
  - health_premium: 600 + pct(min(600, ti - 72000), 25)
  - net_cash: round(salary - employee_cpp - fed_tax - on_basic - on_surtax - health_premium, 2)
expected:
  salary: 195353.55
  ti: 194226.55
  fed_tax: 37672.60
  on_basic: 16908.26
  on_surtax: 5624.47
  health_premium: 750.00
  net_cash: 129751.77
```

```oa-check
name: Ontario 2026 all non-eligible dividend
inputs:
  pre_tax: 200000
steps:
  - on_low: (3.2 * 181 + 2.2 * 184) / 365
  - corp_tax: pct(pre_tax, 9 + on_low)
  - dividend: pre_tax - corp_tax
  - gross_up: pct(dividend, 15)
  - ti: dividend + gross_up
  - fed_gross: pct(min(ti, 58523), 14) + pct(clamp(ti - 58523, 0, 58522), 20.5) + pct(clamp(ti - 117045, 0, 64395), 26) + pct(clamp(ti - 181440, 0, 77042), 29) + pct(max(ti - 258482, 0), 33)
  - bpa: 16452 - 1623 * min(max(ti - 181440, 0) / 77042, 1)
  - fed_tax: max(fed_gross - pct(bpa, 14) - gross_up * 9 / 13, 0)
  - on_gross: pct(min(ti, 53891), 5.05) + pct(clamp(ti - 53891, 0, 53894), 9.15) + pct(clamp(ti - 107785, 0, 42215), 11.16) + pct(clamp(ti - 150000, 0, 70000), 12.16) + pct(max(ti - 220000, 0), 13.16)
  - on_basic: max(on_gross - pct(12989, 5.05), 0)
  - on_surtax: pct(max(on_basic - 5818, 0), 20) + pct(max(on_basic - 7446, 0), 36)
  - on_credit: pct(gross_up, 22.895)
  - on_tax: max(on_basic + on_surtax - on_credit, 0)
  - health_premium: 750 + pct(min(600, ti - 200000), 25)
  - net_cash: round(dividend - fed_tax - on_tax - health_premium, 2)
expected:
  corp_tax: 23391.78
  dividend: 176608.22
  ti: 203099.45
  fed_tax: 22634.69
  on_tax: 18427.98
  health_premium: 900.00
  net_cash: 134645.55
```

```oa-check
name: Ontario 2026 salary of 100000 with the rest as non-eligible dividend
inputs:
  pre_tax: 200000
  salary: 100000
  employer_cpp: 4646.45
  employee_cpp: 4646.45
  enhanced_deduction: 1127
  base_cpp: 3519.45
  cea: 1501
steps:
  - corp_income: pre_tax - salary - employer_cpp
  - on_low: (3.2 * 181 + 2.2 * 184) / 365
  - corp_tax: pct(corp_income, 9 + on_low)
  - dividend: corp_income - corp_tax
  - gross_up: pct(dividend, 15)
  - ti: salary - enhanced_deduction + dividend + gross_up
  - fed_gross: pct(min(ti, 58523), 14) + pct(clamp(ti - 58523, 0, 58522), 20.5) + pct(clamp(ti - 117045, 0, 64395), 26) + pct(clamp(ti - 181440, 0, 77042), 29) + pct(max(ti - 258482, 0), 33)
  - bpa: 16452 - 1623 * min(max(ti - 181440, 0) / 77042, 1)
  - fed_tax: max(fed_gross - pct(bpa + cea + base_cpp, 14) - gross_up * 9 / 13, 0)
  - on_gross: pct(min(ti, 53891), 5.05) + pct(clamp(ti - 53891, 0, 53894), 9.15) + pct(clamp(ti - 107785, 0, 42215), 11.16) + pct(clamp(ti - 150000, 0, 70000), 12.16) + pct(max(ti - 220000, 0), 13.16)
  - on_basic: max(on_gross - pct(12989 + base_cpp, 5.05), 0)
  - on_surtax: pct(max(on_basic - 5818, 0), 20) + pct(max(on_basic - 7446, 0), 36)
  - on_tax: max(on_basic + on_surtax - pct(gross_up, 22.895), 0)
  - health_premium: 600 + pct(min(600, ti - 72000), 25)
  - net_cash: round(salary - employee_cpp + dividend - fed_tax - on_tax - health_premium, 2)
expected:
  corp_income: 95353.55
  dividend: 84201.10
  fed_tax: 29361.53
  on_tax: 19921.37
  net_cash: 129521.75
```

```oa-check
name: British Columbia 2026 all salary against all non-eligible dividend
inputs:
  pre_tax: 200000
  employer_cpp: 4646.45
  employee_cpp: 4646.45
  enhanced_deduction: 1127
  base_cpp: 3519.45
  cea: 1501
steps:
  - salary: pre_tax - employer_cpp
  - ti_s: salary - enhanced_deduction
  - fed_s: pct(min(ti_s, 58523), 14) + pct(clamp(ti_s - 58523, 0, 58522), 20.5) + pct(clamp(ti_s - 117045, 0, 64395), 26) + pct(clamp(ti_s - 181440, 0, 77042), 29) + pct(max(ti_s - 258482, 0), 33)
  - bpa_s: 16452 - 1623 * min(max(ti_s - 181440, 0) / 77042, 1)
  - fed_tax_s: max(fed_s - pct(bpa_s + cea + base_cpp, 14), 0)
  - bc_s: pct(min(ti_s, 50363), 5.6) + pct(clamp(ti_s - 50363, 0, 50365), 7.7) + pct(clamp(ti_s - 100728, 0, 14920), 10.5) + pct(clamp(ti_s - 115648, 0, 24782), 12.29) + pct(clamp(ti_s - 140430, 0, 49975), 14.7) + pct(clamp(ti_s - 190405, 0, 75140), 16.8) + pct(max(ti_s - 265545, 0), 20.5)
  - bc_tax_s: max(bc_s - pct(13216 + base_cpp, 5.6), 0)
  - net_salary: round(salary - employee_cpp - fed_tax_s - bc_tax_s, 2)
  - corp_tax: pct(pre_tax, 11)
  - dividend: pre_tax - corp_tax
  - gross_up: pct(dividend, 15)
  - ti_d: dividend + gross_up
  - fed_d: pct(min(ti_d, 58523), 14) + pct(clamp(ti_d - 58523, 0, 58522), 20.5) + pct(clamp(ti_d - 117045, 0, 64395), 26) + pct(clamp(ti_d - 181440, 0, 77042), 29) + pct(max(ti_d - 258482, 0), 33)
  - bpa_d: 16452 - 1623 * min(max(ti_d - 181440, 0) / 77042, 1)
  - fed_tax_d: max(fed_d - pct(bpa_d, 14) - gross_up * 9 / 13, 0)
  - bc_d: pct(min(ti_d, 50363), 5.6) + pct(clamp(ti_d - 50363, 0, 50365), 7.7) + pct(clamp(ti_d - 100728, 0, 14920), 10.5) + pct(clamp(ti_d - 115648, 0, 24782), 12.29) + pct(clamp(ti_d - 140430, 0, 49975), 14.7) + pct(clamp(ti_d - 190405, 0, 75140), 16.8) + pct(max(ti_d - 265545, 0), 20.5)
  - bc_tax_d: max(bc_d - pct(13216, 5.6) - pct(gross_up, 15), 0)
  - net_dividend: round(dividend - fed_tax_d - bc_tax_d, 2)
  - dividend_lead: net_dividend - net_salary
expected:
  fed_tax_s: 37672.60
  bc_tax_s: 18361.90
  net_salary: 134672.60
  fed_tax_d: 22959.04
  bc_tax_d: 16313.53
  net_dividend: 138727.43
  dividend_lead: 4054.83
```

| Result (2026 cash to the owner) | Ontario | British Columbia |
| --- | --- | --- |
| All salary | $129,751.77 | $134,672.60 |
| Salary of $100,000, rest as dividend | $129,521.75 | Not run |
| All non-eligible dividend | $134,645.55 | $138,727.43 |
| Dividend lead over all salary | $4,893.78 | $4,054.83 |

**Decision point.** On these inputs, of the cases run, all non-eligible dividends leave the most 2026 cash in each province, and the lead differs by province. It buys that lead by giving up CPP accrual and RRSP room: all salary creates $35,163.64 of 2027 RRSP room (18% of $195,353.55), and the $100,000 salary creates $18,000. Neither is priced here, and nor is retained income, so this does not show that dividends are better. A $100,000 blend is not shown to be optimal: on 2026 cash it is the lowest of the 3 in Ontario. AMT does not arise: the minimum amount is below regular federal tax in each case. Rerun with the client's real inputs. For years ending after 2026 the Ontario credit and corporate rates differ.

BC's lowest rate here is the 5.6% in s 4.1 and the CRA table. T4127 shows 6.14% for payroll annualisation, which is not the statutory rate.

### Example 2: RRSP or TFSA, federal only

**Stated inputs.** A 30-year-old with taxable income of $60,000, $7,000 to invest, RRSP and TFSA room for $7,000 plus the reinvested refund, 6% a year for 30 years (growth factor 5.743491), federal tax only. Provincial tax and income-tested benefits are left out, so this understates both rates.

The deduction spans 2 bands: $1,477 is at 20.5% and $5,523 at 14%, so the refund is $1,076.01, not 20.5% of $7,000.

```oa-check
name: RRSP and TFSA after-tax outcome with refund reinvested in a TFSA
inputs:
  contribution: 7000
  income: 60000
  growth: 5.743491
  out_low: 14
  out_high: 20.5
steps:
  - at_upper: min(max(income - 58523, 0), contribution)
  - refund: pct(at_upper, 20.5) + pct(contribution - at_upper, 14)
  - future: contribution * growth
  - tfsa_only: round(future, 2)
  - rrsp_low: round(future - pct(future, out_low) + refund * growth, 2)
  - rrsp_high: round(future - pct(future, out_high) + refund * growth, 2)
  - breakeven_percent: round(refund / contribution * 100, 2)
expected:
  refund: 1076.01
  tfsa_only: 40204.44
  rrsp_low: 40755.84
  rrsp_high: 38142.55
  breakeven_percent: 15.37
```

**Decision point.** With the refund reinvested, the RRSP beats the TFSA only if the withdrawal rate is below 15.37%, the rate the deduction earned here. At 14% the RRSP is ahead by $551.40. At 20.5% the TFSA is ahead by $2,061.89 on the rounded results. A client who spends the refund has a different result. A comparison with a taxable account is not computed, as no tax rate on its growth is stated.

### Example 3: capital gains exemption on a share sale, federal only

**Stated inputs.** A resident individual sells shares in 2026 with a $1,000,000 capital gain. The shares meet all of the QSBC tests. No exemption was used before, no cumulative net investment loss, no other income. Federal tax only, basic personal amount only.

Without the deduction, taxable income is $500,000, but adjusted taxable income is the full $1,000,000, so minimum tax can apply on that side too (ITA ss 127.5 and 127.51). With the deduction, regular tax is nil, and AMT counts the gain at 100% and allows a deduction of 7/5 of the amount claimed (s 127.52(1)(d) and (h)(ii)). The basic minimum tax credit is 1/2 of the s 118(1) credit (s 127.531(a)). Each side's federal tax is the higher of regular tax and minimum tax.

```oa-check
name: LCGE gain of 1000000 regular tax against minimum tax
inputs:
  gain: 1000000
  bpa_at_income: 14829
steps:
  - taxable_gain: gain / 2
  - exemption_room: 1275000 / 2
  - deduction: min(taxable_gain, exemption_room)
  - no_claim_gross: pct(58523, 14) + pct(58522, 20.5) + pct(64395, 26) + pct(77042, 29) + pct(taxable_gain - 258482, 33)
  - no_claim_regular: no_claim_gross - pct(bpa_at_income, 14)
  - min_tax_credit: pct(bpa_at_income, 14) / 2
  - no_claim_amt: pct(gain - 181440, 20.5) - min_tax_credit
  - no_claim_tax: max(no_claim_regular, no_claim_amt)
  - no_claim_carryover: no_claim_tax - no_claim_regular
  - adjusted_income: gain - deduction * 7 / 5
  - amt_before_credit: pct(max(adjusted_income - 181440, 0), 20.5)
  - amt: max(amt_before_credit - min_tax_credit, 0)
  - federal_saving: no_claim_tax - amt
  - saving_if_credit_nil: no_claim_tax - amt_before_credit
expected:
  deduction: 500000
  no_claim_regular: 136899.99
  no_claim_amt: 166766.77
  no_claim_tax: 166766.77
  no_claim_carryover: 29866.78
  adjusted_income: 300000
  amt_before_credit: 24304.80
  amt: 23266.77
  federal_saving: 143500.00
  saving_if_credit_nil: 142461.97
```

**Decision point.** Minimum tax applies on both sides on these inputs. Federal tax for 2026 is $166,766.77 without the claim and $23,266.77 with it, a 2026 saving of $143,500.00. The simple figure of 33% on the $500,000 taxable gain, $165,000, overstates the saving, as it ignores the lower bands, the basic personal amount and minimum tax on both sides. Whether the s 118(1) credit counts in the T691 computation when regular tax is nil is held: if it does not, AMT with the claim is $24,304.80 and the saving is $142,461.97. The excess of minimum tax over regular tax is $23,266.77 with the claim and $29,866.78 without it. Each can be carried forward 7 years, and is deductible only to the extent a later year's regular tax exceeds that year's minimum amount (ITA s 120.2(1) and (3)), so a client with no later income may not recover it. No later recovery is valued here. Provincial tax, Ontario or other provincial AMT, and income-tested benefits are outside this example.

## Ask the client first

Questions come before any output, and an unanswered fact stays Needs Input.

1. **Who and where.** Province of residence on 31 December 2026, residence history, age, spouse or common-law partner, dependants, and any corporation's province of permanent establishment.
2. **Income.** Each type for 2025 and expected 2026: employment, self-employed, dividends, rental, capital gains, foreign, and any other. Marginal rate now, and expected rate at withdrawal.
3. **Corporation.** CCPC status, year end, shareholders, associated corporations, adjusted aggregate investment income, taxable capital, balance of general rate income pool, payroll history. Family members paid: age, shares held, and work done.
4. **Registered room.** RRSP and FHSA room from the latest notice of assessment, TFSA room from My Account, RESP and RDSP status, pension adjustments, and the client's CPP and retirement goals.
5. **Assets and transactions.** Planned sale, share history for 24 months, cost and acquisition dates of assets, available for use dates, prior capital gains exemption claims, cumulative net investment loss, unused losses, foreign property cost, and any trade within 30 days.
6. **Evidence and intent.** Documents supporting each claim, such as the T2200, invoices with s 3 information, loan agreements with interest dates and receipts, and the purpose of any transaction series.

### Completion checks

- Every step cites the provision that allows it and states its condition.
- Proposed or withdrawn measures are labelled and not computed as law.
- The salary and dividend result names province, year and inputs.
- Each family payment is tested against ss 120.4, 67 and 74.1.
- Quebec and other held items are flagged, not estimated.
- A reviewer signs off before any client acts.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Income Tax Act, Justice Laws XML current to 21 June 2026, read in part: the sections cited, except ss 70(5), 104(13), 105(2), 143(1) and 160(4), which are named only as cross-references in s 120.4 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/ | 2026-11-05 |
| Income Tax Regulations, Justice Laws XML current to 21 June 2026, read in part: ss 1100, 1104, 2601, 4301, 7307, Part IV in part and the Schedule II classes cited | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/ | 2026-11-05 |
| Excise Tax Act, Justice Laws XML current to 21 June 2026, read in part: ss 148, 165, 169(1) and (4), 191, 240, 254 and Schedule VI Part V | https://laws-lois.justice.gc.ca/eng/acts/E-15/ | 2026-11-05 |
| Canada Pension Plan, Justice Laws XML current to 19 October 2026, read in part: s 33 | https://laws-lois.justice.gc.ca/eng/acts/C-8/ | 2026-11-05 |
| Employment Insurance Act, Justice Laws XML current to 21 June 2026, read in part: s 5(2) and (3) and Part VII.1 definitions only | https://laws-lois.justice.gc.ca/eng/acts/E-5.6/ | 2026-11-05 |
| Canada Education Savings Act, Justice Laws XML, file current to 17 July 2025, read in part: s 5 | https://laws-lois.justice.gc.ca/eng/acts/C-3.6/ | 2026-11-05 |
| Canada Disability Savings Act, Justice Laws XML, file current to 21 June 2019, read in part: ss 6 and 7 | https://laws-lois.justice.gc.ca/eng/acts/C-3.5/ | 2026-11-05 |
| Streamlined Accounting (GST/HST) Regulations, file current to 14 April 2025, read in part: ss 2, 15 and 16 | https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-51/ | 2026-11-05 |
| Input Tax Credit Information (GST/HST) Regulations, file current to 20 June 2024, read in part: s 3 | https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/ | 2026-11-05 |
| Taxation Act, 2007 (Ontario), e-Laws from 1 July 2026, read in part: ss 5, 9, 16, 19.1, 23, 24, 31 and 32 | https://www.ontario.ca/laws/statute/07t11 | 2026-11-06 |
| Employer Health Tax Act (Ontario), e-Laws from 27 November 2025, read in part: the exemption text | https://www.ontario.ca/laws/statute/90e11 | 2026-11-05 |
| Income Tax Act (British Columbia), current to 27 October 2026, read in part: ss 4.1 and 4.69 | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_01 | 2026-11-05 |
| CRA, tax rates and brackets for the current year, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-05 |
| CRA, indexation adjustment for 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html | 2026-11-05 |
| CRA, corporation tax rates, page modified 21 October 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html | 2026-11-05 |
| CRA, MP, DB, RRSP, DPSP, TFSA limits, YMPE and YAMPE table, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html | 2026-11-05 |
| CRA, CPP contribution rates, maximums and exemptions, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | 2026-11-05 |
| CRA, EI premium rates and maximums, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html | 2026-11-05 |
| CRA, prescribed interest rates, Q1 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html | 2026-11-05 |
| CRA, prescribed interest rates, Q2 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q2.html | 2026-11-05 |
| CRA, prescribed interest rates, Q3 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q3.html | 2026-11-05 |
| CRA, prescribed interest rates, Q4 2026, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q4.html | 2026-11-05 |
| CRA, T4127 July 2026, Table 8.1 CSV, read in part: the passages cited | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/rates-income-thresholds-constants-26e.csv | 2026-11-05 |
| CRA, T4127 July 2026, Table 8.2 CSV, read in part: the passages cited | https://www.canada.ca/content/dam/cra-arc/formspubs/pub/t4127-jul/other-rates-amounts-26e.csv | 2026-11-05 |
| CRA, important dates for individuals, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-05 |
| CRA, opening your FHSAs, read in part: eligibility | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/opening-your-fhsas.html | 2026-11-05 |
| CRA, GST/HST rates by province, read in part: the passages cited | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html | 2026-11-05 |
| CRA, My Account page, read in part: the service name | https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-individuals/account-individuals.html | 2026-11-05 |
| CRA, My Business Account page, read in part: the service name | https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/business-account.html | 2026-11-05 |
| Finance, 2026 automobile limits, release of January 2026, read in part: the passages cited | https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html | 2026-11-05 |
| Finance, Productivity Mega Deduction backgrounder, read in part: the passages cited | https://www.canada.ca/en/department-finance/news/2026/09/government-of-canada-introduces-new-productivity-mega-deduction-to-boost-canadas-advantage-as-the-most-competitive-g7-country-for-new-business-inve.html | 2026-11-05 |
| Finance, deferral of the capital gains inclusion rate change, 31 January 2025, read in part: the passages cited | https://www.canada.ca/en/department-finance/news/2025/01/government-of-canada-announces-deferral-in-implementation-of-change-to-capital-gains-inclusion-rate.html | 2026-11-05 |
| Finance, Federal Tax Expenditures 2026, Part 2, read in part: capital gains inclusion rate and first personal rate passages | https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-2.html | 2026-11-05 |
| LEGISinfo, Bill C-4, read in part: status | https://www.parl.ca/legisinfo/en/bill/45-1/c-4 | 2026-11-05 |
| Prime Minister, release of 21 March 2025, read in part: the passages cited | https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase | 2026-11-05 |
| Ontario, corporate income tax page, read in part: small business deduction | https://www.ontario.ca/document/corporations-tax/corporate-income-tax | 2026-11-05 |
| Alberta, corporate income tax page, read in part: threshold and AT1 filing | https://www.alberta.ca/corporate-income-tax | 2026-11-05 |

Not yet confirmed: all Quebec tax rates and credits, and QPP and QPIP amounts (Revenu Quebec returned 403); Alberta's corporate rates; provincial dividend credits other than Ontario and BC; whether the $39,000 Class 10.1 ceiling has been enacted; the Productivity Mega Deduction and other Budget 2025 or Spring Economic Update 2026 proposals not shown in the text read; application dates of the 2024 GAAR changes; the application text for the 14.5% rate for 2025; the yearly chain of Ontario index factors behind the T4127 amounts; ETA Schedule IX and ss 199 to 202; s 118.2(2) limb by limb; northern zones and daily amounts; EI Part VII.1 entry terms; T3 and T5013 slip dates; RDSP income thresholds; the later treatment of unused ABILs in s 111(8); T691 credit mechanics when regular tax is nil; Quick Method ITCs on capital property; a profit level for incorporating; CRA data matching; and the slots missing from `canada-bookkeeping`.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 1.2 | 2026-11-05 | Converted to the upstream template. Tied each strategy to its provision and condition. Corrected stale 2026 figures, the salary and dividend example, the TOSI and attribution citations, the timing strategies and the GAAR test. Held Quebec and proposed measures. Returned to Tier 2 under template rule 11. |
| 1.1 | 2026-11-01 | Previous version, in the older layout. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
