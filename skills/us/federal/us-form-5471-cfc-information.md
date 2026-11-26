---
name: us-form-5471-cfc-information
description: Determine US federal Form 5471 filing categories, ownership and attribution, required schedules, deadlines, penalties and missed-year routing for tax year 2026. Includes four worked cases and the 2026 ownership and inclusion changes; specialist reporting and relief questions are referred.
version: "2.4"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: situation-rules
---

# US Form 5471: who files, which category, which schedules, tax year 2026

> **Source-cited draft.** Federal filing guidance. Resolve the facts and the applicable tax year before using it for a return.

A US person must test every Form 5471 filer category; CFC ownership alone does not settle the filing. Attach a separate form for each applicable foreign corporation to the filer's return by that return's due date, including extensions ([IRS instructions, Who Must File; When and Where To File](https://www.irs.gov/instructions/i5471)). The ordinary US shareholder threshold is **10% or more** of vote or value; a CFC requires **more than 50%** owned by US shareholders on any day, applying the ownership rules below ([sections 951(b)](https://uscode.house.gov/us/usc/t26/s951/) and [957(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm)).

## Scope and who this is for

This Guide covers federal Form 5471 category decisions, the schedule checklist, filing exceptions, deadlines and penalty exposure. For substantive subpart F, net CFC tested income (NCTI), section 250, section 962 and section 960 calculations, use `us-gilti-fdii-beat`; individual credits go to `us-foreign-tax-credit-1116`. These are routing pointers, not clearance of those Guides.

For ordinary Category 5 purposes, US persons include citizens or residents, domestic partnerships and corporations, and estates or trusts that are not foreign under section 7701(a)(31). Category 4 also includes individuals with effective section 6013(g) or (h) elections; Categories 2/3 have their own US-person rules ([IRS category definitions](https://www.irs.gov/instructions/i5471)). For territorial residence, treaty residence, electing spouses or unusual trusts: **Check this point with one of our partner accountants.** Do not extend the ordinary list across categories without checking its exceptions.

Other reporting routes: `us-form-5472-foreign-owned-us`, `us-fbar-and-fatca-8938`, `us-foreign-trust-reporting`, `us-form-1120-c-corp`, `us-form-1065-partnership`, and `us-irs-collections-and-controversy`. For foreign partnerships (Form 8865) or PFICs (Form 8621): **Check this point with one of our partner accountants.**

## Ask the client first

Obtain the ownership chart on every day of the relevant foreign year: names, residence, stock classes, votes, value, options and acquisition/disposition dates. Obtain family and entity relationships, officer/director roles, the foreign tax year, local accounts and functional currency, taxes, distributions, loans, earlier Forms 5471, section 965 balances, other filers' copies and all IRS notices with mailing dates. Check whether 2022 to 2025 returns omitted foreign income. Ask about deaths, estates and actual beneficiary interests. Hold a conclusion when an input is missing; do not invent zero holdings, filing history, an allocation date or another person's filing.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or date | Source |
| --- | --- | --- |
| Ordinary US shareholder, applying section 958(a)/(b) | 10% or more of vote or value | [Section 951(b)](https://uscode.house.gov/us/usc/t26/s951/) |
| Ordinary CFC | More than 50% of vote or value owned by US shareholders on any day | [Section 957(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm) |
| Category 4 control | More than 50% of vote or value at any time in the filer's tax year | [Section 6038(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Categories 2/3 stock threshold | 10% or more of vote or value; apply their separate attribution rules | [Section 6046(a)(2)](https://uscode.house.gov/us/usc/t26/s6046/) |
| Section 954(b)(4) high-tax comparison | Effective rate greater than 90% of the 21% section 11 rate: 18.9% (derived). This comparison alone does not establish an exclusion or election | [Section 954(b)(4)](https://uscode.house.gov/us/usc/t26/s954/); [section 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |

### Step 1: ownership and attribution

For the ordinary CFC and US shareholder tests, section 958(a)(2) attributes stock through **foreign** corporations, partnerships, estates and trusts proportionately. Constructive ownership uses section 318 with section 958(b)'s modifications ([section 958](https://uscode.house.gov/us/usc/t26/s958/)). Keep the inclusion ownership test separate from constructive status. For domestic partnership filing versus partners' inclusions: **Check this point with one of our partner accountants.**

- Section 318 family attribution includes spouse, children, grandchildren and parents; exclude a spouse legally separated under a decree of divorce or separate maintenance. A legally adopted child counts as a child by blood. It does not list siblings ([section 318(a)(1)](https://uscode.house.gov/us/usc/t26/s318/)).
- For CFC tests, stock owned by a nonresident alien individual is not attributed through the family rule to a citizen or resident alien individual ([section 958(b)(1)](https://uscode.house.gov/us/usc/t26/s958/)).
- **Categories 2/3 differ:** section 6046(c)'s family includes whole- and half-blood siblings, spouse, ancestors and lineal descendants. Do not apply the CFC family list to these reporting events ([section 6046(c)](https://uscode.house.gov/us/usc/t26/s6046/)).
- For section 318(a)(2)(C) corporate attribution, section 958(b)(3) substitutes 10% for 50%. When applying section 318(a)(2)(A) to (C), an entity owning more than 50% of votes is treated as owning all voting stock. Vote attribution can therefore differ from proportional value attribution ([section 958(b)(2)/(3)](https://uscode.house.gov/us/usc/t26/s958/)). For options, trusts and reattribution questions beyond these stated rules: **Check this point with one of our partner accountants.**

For foreign corporation years **beginning after 31 December 2025**, restored section 958(b)(4) prevents section 318(a)(3)(A) to (C) from attributing foreign-owned stock down to a US person for these CFC tests. A foreign sister is no longer a CFC **on that basis alone**; test other ownership and section 951B separately ([Public Law 119-21, section 70353](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)). For section 951B's foreign-controlled shareholder regime, its inclusions and Form 5471 reporting: **Check this point with one of our partner accountants.** No non-filing conclusion is authorized here for that regime.

### Step 2: categories

Use the [IRS Categories of Filers](https://www.irs.gov/instructions/i5471), testing all categories that could apply.

| Category | Decision |
| --- | --- |
| 1a/1b/1c | Section 965 SFC history, Schedule J/P balances and the Category 1 subtypes: Check this point with one of our partner accountants. |
| 2 | A US citizen/resident officer or director where a US person acquires stock meeting the 10% requirement, or an additional 10% of vote or value. The officer need not own shares. [IRS Category 2](https://www.irs.gov/instructions/i5471) |
| 3 | A US person acquires stock reaching 10% with existing stock, separately acquires an additional 10%, becomes a US person while meeting 10%, or disposes of enough stock to fall below 10%. Section 953(c) insurance cases are referred below. Include the required statement of related indebtedness and subscribers' names, addresses, identifying numbers and shares subscribed. [IRS Category 3](https://www.irs.gov/instructions/i5471) |
| 4 | A US person controls more than 50% of votes or value at any time in its tax year. Control passes through a chain where each relevant holding exceeds 50%; use section 6038(e)(2)'s ownership rules, rather than assuming all category tests coincide. [Section 6038(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| 5 | Under the December 2025 instructions, a US shareholder of a CFC during the foreign year ending with/within its year, owning stock on the last CFC day. Category 5a is a Category 5 filer who is neither 5b nor 5c. This instruction's last-day wording does **not** remove a seller's 2026 any-day inclusion under Step 5. [IRS Category 5](https://www.irs.gov/instructions/i5471) |
| 5b/5c | Foreign-controlled CFC classification, relatedness and category-specific relief, including years beginning in 2025: Check this point with one of our partner accountants. |

For a seller who does not meet the December 2025 last-day category wording, the current reporting decision is held: **Check this point with one of our partner accountants.** Do not infer that there is no Form 5471 obligation from these older instructions.

If both Category 4 and 5a apply, check **only box 4**, but complete all required information for both. A person filing for others checks its own categories ([IRS item B](https://www.irs.gov/instructions/i5471)).

### Step 3: schedules

Use the [IRS Filing Requirements for Categories of Filers chart](https://www.irs.gov/instructions/i5471). Supply the union of all applicable requirements without duplication; file a required schedule even when all amounts are zero. For Schedules E, I-1, J, P and Q, which are completed by category, a single instance for any separate category meets that zero-schedule requirement.

| Filer | Identifying information on page 1 plus |
| --- | --- |
| Category 2 | Schedule O Part I |
| Category 3, ordinary case | Schedules A, B Parts I/II, C, F, G, G-1, O Part II |
| Sole owner satisfying 4 and 5a | All six pages and separate E, G-1, H, I-1, J, M, P, Q and R; H-1 only if an applicable corporation for CAMT |

Category 1 and 5b/5c schedule selections and CAMT H-1 eligibility: **Check this point with one of our partner accountants.** Category 5a filers who are not Category 4 use their own chart column, not the sole-owner list.

**Schedule B Part I:** for ordinary Category 3/4 reporting, list US persons owning at any time in the annual accounting period at least 10% of votes or value directly or indirectly through foreign entities. Constructive-only status is not sufficient for this population. The section 953(c) insurance population has a separate rule: **Check this point with one of our partner accountants.** For Part II's category-specific direct owners and FDE/regarded-owner reporting: **Check this point with one of our partner accountants.** ([IRS Schedule B](https://www.irs.gov/instructions/i5471)).

**Accounting:** Schedule C uses functional currency and US GAAP, translated using US GAAP principles. Under DASTM, C's functional-currency column uses local hyperinflationary currency under US GAAP and its dollar column uses US GAAP translation; Schedule H reconciles to the tax result. Schedule F generally uses a functional-currency balance sheet translated using US GAAP; DASTM instead uses the tax balance-sheet rules of regulation 1.985-3(d) ([IRS Schedules C/F](https://www.irs.gov/instructions/i5471)).

Use each schedule's prescribed translation method. Report exchange rates as foreign currency units per US dollar using the divide-by convention, rounded to **at least four places**, and more if four would materially distort the rate or dollar result. Do not use a universal average-income/spot-balance-sheet recipe ([IRS Other Reporting Requirements](https://www.irs.gov/instructions/i5471)).

Detailed completion of A, E/E-1, G/G-1, H/H-1, I/I-1, J, M, O, P, Q and R, including cost sharing, E&P/PTEP, income groups, foreign taxes, related transactions and distributions: **Check this point with one of our partner accountants.** Use the matching schedule section of the IRS instructions; this Guide supplies the filing checklist, not those calculations.

### Step 4: filing exceptions

A Category 1, 3, 4 or 5 constructive owner can use the US-person exception only when it has **no direct interest**, is required to report solely through constructive ownership from another US person, and that person files all information required of it. Obtain the complete filed copy. The instructions do not require a statement for this exception ([IRS category exceptions](https://www.irs.gov/instructions/i5471)).

For Categories 1, 4 and 5, the nonresident-alien constructive-owner exception requires **no direct or indirect interest** and a filing requirement arising solely through constructive ownership from a nonresident alien ([IRS category exceptions](https://www.irs.gov/instructions/i5471)).

Category 2 has separate exceptions ([IRS Category 2 exceptions](https://www.irs.gov/instructions/i5471)):

- Immediately after the reportable acquisition, three or fewer US persons own **95% or more of value**, and the acquirer files the acquisition as Category 3.
- Alternatively, the US acquirer for whom the officer/director would report has no direct interest, is required to furnish information solely through constructive ownership from a US person, and that attributing US person supplies all required Category 2 information. This tests the acquirer, not whether the officer owns stock.

For multiple filers, item H, separate I/H-1/P, statements and their exceptions: **Check this point with one of our partner accountants.** Do not treat another person's return as automatically covering the client. For foreign-controlled CFC exceptions, section 953(d) insurance elections, dormant-corporation summary filing under Rev. Proc. 92-70, alternative information under Rev. Proc. 2019-40 and penalty waivers: **Check this point with one of our partner accountants.** Inactivity alone does not establish eligibility for a summary filing.

### Step 5: 2026 changes and inclusions

- **NCTI and QBAI:** for taxable years beginning after 31 December 2025, section 951A uses net CFC tested income and the deemed tangible return based on QBAI is repealed. Route the computation to `us-gilti-fdii-beat` ([Public Law 119-21, section 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).
- **One-month deferral:** repeal applies to specified foreign corporation years beginning after 30 November 2025. For a corporation that was a specified foreign corporation on 30 November 2025, the first year beginning after that date ends with the first required year ending after it and can be short. A change required by the repeal is treated as corporation-initiated and consented to. For determining the required shareholder year, multiple-majority-shareholder issues, Notice 2025-72 foreign-tax allocation and the Schedule E statement: **Check this point with one of our partner accountants.** ([Section 70352](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).
- **Any-day subpart F inclusion:** for foreign corporation years beginning after 31 December 2025, a US shareholder owning section 958(a) stock on any day includes its pro rata subpart F income for periods when it owned that stock, was a US shareholder and the company was a CFC. The inclusion is in the shareholder year containing its last section 958(a) ownership day in that CFC year. Section 956 retains a last-CFC-day ownership test. Constructive status alone does not satisfy section 958(a) ([section 951(a)](https://uscode.house.gov/us/usc/t26/s951/); [section 70354 effective date](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).
- For the dividend transition under Notice 2025-75, its timing/taxable-income/documentation conditions, proposed-regulation reliance and Schedule G/Worksheet A placement: **Check this point with one of our partner accountants.** Do not use an unconfirmed line number.
- For section 954(c)(6) related-CFC look-through and its payment, attribution and deficit conditions: **Check this point with one of our partner accountants.** Permanence does not make every inter-CFC payment exempt.

### Step 6: penalties and exposure

| Failure | Exposure and conditions | Source |
| --- | --- | --- |
| Section 6038(a) information not furnished on time | USD 10,000 for each foreign corporation's annual accounting period | [Section 6038(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Same failure continues more than 90 days after mailed notice | Another USD 10,000 for each 30-day period or fraction after the 90 days; addition capped at USD 50,000, so base plus addition can reach USD 60,000 (derived) per failure | [Section 6038(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Section 6038 foreign-tax-credit reduction | Applicable section 901/960 taxes reduced by 10%, plus 5% per 3-month period or fraction after the 90-day notice period. Cap per failure: greater of USD 10,000 or the entity's income for its period; reduce the reduction by the section 6038(b) penalty for the same period | [Section 6038(c)(1)-(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Section 6046 reporting failure or incomplete information | Section 6679: USD 10,000 unless reasonable cause is shown. After more than 90 days from mailed notice, USD 10,000 per 30-day period or fraction; continuing addition capped at USD 50,000 | [Section 6679(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6679.htm) |

Under section 6038(c)(4)(B), the information deadline and start of the 90-day notice period are treated as no earlier than the last day reasonable cause existed, **as shown to the Secretary's satisfaction**. For evidence, adviser reliance, illness/disaster and actual relief claims: **Check this point with one of our partner accountants.**

Section 6501(c)(8) means assessment for a related return, event or period cannot expire **before three years after the information is furnished**; it is not an automatic closing date. Only if the failure was due to reasonable cause **and not willful neglect** is that extension confined to related items ([section 6501(c)(8)](https://uscode.house.gov/us/usc/t26/s6501/)).

For criminal penalties, section 6662(j), assessed notices, litigation and procedural defenses: **Check this point with one of our partner accountants.**

### Step 7: fixing missed years

The delinquent international information return procedure is available only where the taxpayer is not under IRS civil examination or criminal investigation and has not already been contacted about these delinquent information returns. File delinquent Forms 5471 with an amended return under normal instructions. Include a reasonable-cause statement **if asserting reasonable cause**; penalties may be assessed without first considering it ([IRS delinquent procedure](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures)). It is not automatic penalty relief, even if all income and tax were reported.

For streamlined foreign/domestic eligibility, residency, covered return and FBAR years, Forms 14653/14654, the domestic miscellaneous penalty and exclusions from relief: **Check this point with one of our partner accountants.** For willfulness, examination, criminal investigation or a certification under penalty of perjury: **Check this point with one of our partner accountants.**

### Step 8: related reporting

For inclusion placement on the shareholder return, final-year line numbers, PTEP exclusion/order, successor proof, section 961 basis limits and excess distributions, section 962 interactions, section 986(c) currency gain/loss, Form 8938 duplication/Part IV, treaty disclosures on Form 8833, section 245A dividends, section 338/304 transactions, Form 8886, Form 8858 and branch/disregarded-entity attachments: **Check this point with one of our partner accountants.** The earlier blanket distribution, basis and duplicated-asset rules must not be used without those conditions.

## Boundary and exception table

| Facts | Treatment |
| --- | --- |
| 8% directly and spouse 4% | 12% for the CFC shareholder test; section 6046's family definition must still be applied separately |
| Nonresident alien parent holds 40% | Excluded from the family attribution to a US child for the CFC tests |
| 51% value, 30% vote | The value prong can satisfy control and CFC ownership thresholds |
| New US resident already holding 15%, or first acquisition reaching 10% | Test Category 3; Category 5 separately needs its CFC/category conditions |
| Foreign parent, US subsidiary and foreign sister, including a 10% indirect US owner; year begins in 2025 | Category 5b/5c, relatedness and exceptions: Check this point with one of our partner accountants. |
| Same structure, year begins after 31 December 2025 | Apply restored section 958(b)(4), then separately consider section 951B; no blanket non-filing conclusion |
| Foreign year ends 30 June 2026; filer has calendar year | Ordinary annual-period reporting falls in the 2026 return; see the separate any-day inclusion rule above |
| Dormant company, domestic partnership or differing high-tax elections | Check this point with one of our partner accountants. |

### Red flags at review

Hold the conclusion for missing family/entity holdings, missing transaction dates, unexplained section 965/PTEP balances, inconsistent currency translations, absent filing evidence or an IRS notice. Obtain the notice and evidence before choosing a response; do not assume a notice is mistaken. High-tax elections and inconsistent shareholder filings: **Check this point with one of our partner accountants.**

### Defaults when a fact is missing

Ask for the missing record and hold the affected decision. Keep another person's filing and any claimed exception unrelied-on until the filed copy and applicable conditions are established.

## Worked cases

**Case 1, a decision: which category, which schedules?** Dana, a US citizen, has owned 8% of the only class of stock of a Portuguese company since 2023. Her husband, also a US citizen, owns 4%. Dana's US-citizen brother owns 40%. Foreign individuals own the remaining 48%. Nothing was bought or sold in 2026; Dana is not an officer or director.

For the ordinary CFC tests, Dana counts 8% + 4% = 12%; the brother's 40% is not attributed to her under section 318, but he is a US shareholder himself. Count the underlying shares once: 8% + 4% + 40% = 52%, so the company is a CFC. Dana's 12% is not control. No Category 3 acquisition is stated; also check the other Category 3 triggers before excluding that category. She and her husband meet the December 2025 Category 5 definition and are ordinary 5a filers, subject to testing any foreign-controlled special facts; use the Category 5a chart column. Neither can use the constructive-owner exception because both own directly. Category 1 history and joint filing: **Check this point with one of our partner accountants.** ([IRS categories/exceptions](https://www.irs.gov/instructions/i5471)).

Alternative: the brother owns 35% and foreigners 53%, so US shareholder stock is 47%. That is not a CFC under the ordinary test, so no ordinary Category 5; there is also no control or stated Category 2/3 event. A final no-filing answer still requires clearing Category 1 history and other special regimes. The difference between 52% and 47% is **5 percentage points**. Exactly 50% fails the ordinary CFC test; exactly 10% satisfies the shareholder threshold.

```oa-check
name: Category decision, Dana, 2026 (CFC at 52%, not at 47%)
inputs:
  dana_direct: 0.08
  spouse_direct: 0.04
  brother_direct: 0.40
  brother_alternative: 0.35
steps:
  - dana_counted: dana_direct + spouse_direct
  - us_shareholder_flag: 1 - ceil(clamp(0.10 - dana_counted, 0, 1))
  - us_shareholder_stock: dana_direct + spouse_direct + brother_direct
  - cfc_flag: ceil(clamp(us_shareholder_stock - 0.50, 0, 1))
  - category_4_flag: ceil(clamp(dana_counted - 0.50, 0, 1))
  - us_shareholder_stock_alternative: dana_direct + spouse_direct + brother_alternative
  - cfc_flag_alternative: ceil(clamp(us_shareholder_stock_alternative - 0.50, 0, 1))
expected:
  dana_counted: 0.12
  us_shareholder_flag: 1
  us_shareholder_stock: 0.52
  cfc_flag: 1
  category_4_flag: 0
  us_shareholder_stock_alternative: 0.47
  cfc_flag_alternative: 0
```

**Case 2, penalty exposure for missed years.** Leo, a US citizen in Texas, wholly owns two foreign companies and filed no Form 5471 for 2023, 2024 or 2025 (six failures, each a section 6038(b) failure as Category 4). One IRS notice covers all six. He files everything 150 days after the notice was mailed, with no reasonable cause accepted.

Base: 2 x 3 x USD 10,000 = USD 60,000. Continuing failure: (150 - 90) / 30 = 2 periods; USD 20,000 per failure, below the USD 50,000 addition cap. Six additions total USD 120,000; combined total USD 180,000. Any section 6038(c) tax-credit reduction is coordinated with the monetary penalties. Assessment cannot expire before three years after the information is supplied; that is not a guaranteed closing date. The existing IRS notice defeats the delinquent procedure's no-prior-contact condition. Respond through the notice/penalty-response route in `us-irs-collections-and-controversy`: **Check this point with one of our partner accountants.** ([Section 6038](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm); [IRS eligibility](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures)).

```oa-check
name: Section 6038(b) penalties, 2 corporations x 3 years, filed 150 days after notice
inputs:
  corporations: 2
  years: 3
  base_penalty: 10000
  days_after_notice: 150
  grace_days: 90
  period_days: 30
  continuing_cap: 50000
steps:
  - failures: corporations * years
  - base_total: failures * base_penalty
  - periods: ceil(max(days_after_notice - grace_days, 0) / period_days)
  - continuing_per_failure: min(periods * base_penalty, continuing_cap)
  - continuing_total: failures * continuing_per_failure
  - total: base_total + continuing_total
expected:
  failures: 6
  base_total: 60000
  periods: 2
  continuing_per_failure: 20000
  continuing_total: 120000
  total: 180000
```

**Case 3, inheritance through a US estate.** Joseph, a US citizen, owned 60% of a Mexican manufacturing company and filed Form 5471 every year. He died in April 2026; his US estate holds the 60% through the end of 2026, and his will splits the estate equally between his US-citizen children Mark and Anna. Mark owns no shares himself.

If 60% describes value and the equal estate interests are proportional beneficiary interests, each child's constructive value interest is 60% / 2 = 30%. Do not assume that is the voting percentage. If the estate holds more than 50% of votes, section 958(b)(2)'s all-vote modification can produce a 50% constructive voting interest for each equal beneficiary. Establish stock rights and beneficiary interests first ([sections 318(a)(2)(A)](https://uscode.house.gov/us/usc/t26/s318/) and [958(b)(2)](https://uscode.house.gov/us/usc/t26/s958/)).

On a qualifying 60%-control holding the estate meets Category 4 and, if the ordinary CFC/category facts apply, 5a; box 4 is checked. Mark and Anna can use the US constructive-owner exception only if neither has a direct interest, their filing arises solely through the estate's constructive attribution, and the estate files all their required information. Their stated constructive interests alone are not section 958(a) ownership. Do not allocate all 2026 inclusions to the estate: separately analyze Joseph's pre-death ownership and the estate's post-death ownership under the any-day rule. The precise April death date and income allocation are missing. **Check this point with one of our partner accountants.** A later direct distribution of 30% to each child creates a Category 3 acquisition event; apply the acquisition-year rules ([IRS Category 3](https://www.irs.gov/instructions/i5471)).

**Case 4, a sole owner after the 2026 changes.** Sarah, a US citizen, owns 100% of a Singapore company with a calendar tax year. For 2026 she meets Category 4 and ordinary 5a; check box 4 and use the sole-owner checklist above, with no H-1 for an individual. The original case describes services income and a foreign rate below 18.9%, but gives neither the service/related-party facts nor a computed effective rate. Do not conclude from that alone that the income is outside subpart F or that a high-tax exclusion fails. The QBAI-based tangible return is repealed for this 2026 year. For income classification, high-tax election, section 962 and the Singapore account's FBAR obligation: **Check this point with one of our partner accountants.** ([IRS categories/chart](https://www.irs.gov/instructions/i5471); [section 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).

## When to refuse or refer

Each following code is an explicit hold on its specialist point: **Check this point with one of our partner accountants.**

| Code | Point held |
| --- | --- |
| R-5471-951B | Foreign-controlled shareholder inclusions and reporting |
| R-5471-WILLFUL | Willfulness, examination/investigation and certifications |
| R-5471-NOTICE | Penalty notices, assessment and response |
| R-5471-965 | Section 965 and Category 1/PTEP reconstruction |
| R-5471-INSURANCE | Section 953(c)/(d), captives and insurance reporting |
| R-5471-FSC | Foreign sales corporation rules |
| R-5471-CAMT | Applicable-corporation status and H-1 |
| R-5471-REORG | Section 338/304, reorganizations and liquidations |
| R-5471-PFIC | PFIC overlap and Form 8621 |
| R-5471-SHORT | Required year, short-year allocation and Notice 2025-72 |

## Filing and payment

Attach Form 5471 to the filer's income tax, partnership or exempt-organization return and meet its due date including valid extensions. A ready but unfiled form is not timely ([IRS filing instructions](https://www.irs.gov/instructions/i5471)).

| Ordinary calendar-year 2026 filer | Return due date | Source |
| --- | --- | --- |
| Individual Form 1040 | 15 April 2027 | [Section 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |
| Domestic C corporation Form 1120 | 15 April 2027 | [Section 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |
| Partnership Form 1065 or S corporation Form 1120-S | 15 March 2027 | [Section 6072(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |

For Forms 4868/7004, overseas individual extensions, fiscal years, disaster relief, estimated taxes and inclusion payments: **Check this point with one of our partner accountants.** No payment-extension conclusion follows from a filing extension.

Ordinarily report the foreign annual accounting period ending with or within the filer's tax year; Schedule O uses events in the filer's year. Keep that reporting period distinct from the 2026 inclusion timing above ([section 6038(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm); [IRS annual accounting period instructions](https://www.irs.gov/instructions/i5471)).

A correction goes with an amended return under that return's amendment instructions: mark Form 5471 “Corrected” and attach a statement identifying the changes ([IRS Corrections to Form 5471](https://www.irs.gov/instructions/i5471)).

## Completion checklist

Retain the ownership and category decision, sources and tax-year applicability, schedule chart, exception evidence and filing receipt. Match the complete return and attachments; route every specialist hold above before relying on that point. Do not substitute this checklist for the referred calculation or reporting decisions.

## Sources

The December 2025 instructions supply the filing framework. Statutory 2026 changes control over older instruction wording. Existing completed November 22/23 reads were reused where applicable; exact passages for retained rules were recovered and read on 2026-11-26. These are bounded operative reads, not a claim to have read every source in full.

| Source and scope | URL | Read on |
| --- | --- | --- |
| IRS Form 5471 instructions, categories, chart, exceptions, B/C/F, currency, filing and correction passages; December 2025 framework | https://www.irs.gov/instructions/i5471 | 2026-11-26 |
| Section 951(a)/(b), current any-day inclusions and shareholder threshold | https://uscode.house.gov/us/usc/t26/s951/ | 2026-11-26 |
| Section 957(a), ordinary CFC threshold; territorial/insurance exceptions referred | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm | 2026-11-26 |
| Section 958(a)/(b), ownership; current text includes restored paragraph (4) | https://uscode.house.gov/us/usc/t26/s958/ | 2026-11-26 |
| Section 318(a)(1)/(2), family and estate attribution | https://uscode.house.gov/us/usc/t26/s318/ | 2026-11-26 |
| Section 6046(a)/(c), reporting thresholds and separate family definition | https://uscode.house.gov/us/usc/t26/s6046/ | 2026-11-26 |
| Public Law 119-21, sections 70323 and 70352-70354, amendments and effective dates | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26 |
| Section 6038, reporting, control, monetary and credit penalties, reasonable-cause timing | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm | 2026-11-26 |
| Section 6679(a), monetary penalties and reasonable cause | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6679.htm | 2026-11-26 |
| Section 6501(c)(8), minimum assessment period and related-items condition | https://uscode.house.gov/us/usc/t26/s6501/ | 2026-11-26 |
| Section 954(b)(4), statutory effective-rate comparison; election mechanics referred | https://uscode.house.gov/us/usc/t26/s954/ | 2026-11-26 |
| Section 11(b), corporate rate used solely for the derived high-tax comparison | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-26 |
| Section 6072(a)/(b), ordinary calendar-year return deadlines | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-26 |
| IRS delinquent international information return procedure, eligibility and submission/penalty conditions | https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures | 2026-11-26 |

Not yet confirmed: seller reporting under final applicable 2026 instructions; section 951B reporting; Category 1/5b/5c and foreign-controlled relief; joint-filer mechanics; dormant and alternative-information eligibility; detailed schedules and income/PTEP/basis/credit calculations; high-tax election mechanics; dividend transition and Schedule G placement; short-year tax allocation; streamlined eligibility/relief; other-form reporting, extensions and notice defenses. These points are non-usable holds with the partner-accountant referral above, not assertions that no official guidance exists.
