---
name: us-form-1065-partnership
description: Prepare a US partnership Form 1065 workpaper for tax year 2026, distinguish guaranteed payments from profit allocations, reconcile Schedules K and K-1, test audit-regime eligibility, and calculate the late-return penalty. Form references and K-2/K-3 exceptions are explicitly limited to the 2025 editions; 2026 filing output is held until its edition is checked. Federal only.
version: "3.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: situation-rules
---

# US Form 1065 partnership return, tax year 2026

**Answer first.** A domestic partnership generally files Form 1065, but the ordinary filing rule excepts one with neither income nor expenditures treated as federal deductions or credits; a qualified opportunity fund or qualified derivatives dealer can still have a filing obligation. The ordinary calendar-2026 deadline is **15 March 2027**, with **15 September 2027** after a valid six-month extension. A services payment fixed without regard to income is a guaranteed payment, subject to deductibility and capitalization rules. [F] [E] [G]

> **Edition hold.** The Form 1065 and instruction pages read for this work are the **2025 editions**. All line, box, question and K-2/K-3 exception references below are 2025 references, not confirmation of a final 2026 layout or exception. Do not finalize a 2026 return or claim a 2026 K-2/K-3 exception from this Guide until the applicable final editions have been read. This is a source-cited draft; it carries no accountant approval. Under Circular 230 section 10.37, [advice must use reasonable factual/legal assumptions and relate law to facts](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37); these illustrations are not filing conclusions for other facts.

## Scope and who this is for

Federal partnership-return preparation for general and limited partnerships, LLPs and entities already established to be taxed as partnerships, including multi-member LLCs. LLCs classified as partnerships have the same filing requirements as domestic partnerships. [F]

Classification elections, a single-member LLC, spouses' community-property treatment or qualified joint venture, rental co-ownership, investment-club exclusions under section 761, publicly traded partnerships and foreign-partnership filing exceptions: **Check this point with one of our partner accountants.** Do not infer classification from an entity's name. Corporate-return routing: `us-form-1120-c-corp` or the Form 1120-S Guide; sole-proprietor routing: `us-sole-prop-bookkeeping`.

## Ask the client first

Obtain the agreement and amendments; every partner's identity, TIN, tax classification, residence and entry/exit date; services and management facts; fixed payments, minimum guarantees and profit priorities; receipts, assets and financial statements; tax-basis capital records; contributed/distributed property; loans, guarantees and lender documents; foreign income, taxes, entities and partners; K-3 notices and requests; prior returns, extension acknowledgements and penalty notices. Do not fill missing facts with tax conclusions.

## The method, step by step

### 1. Establish the year, deadline and form edition

Use the actual tax year. A non-calendar required year, section 444 election, section 7519 payment or business-purpose year: **Check this point with one of our partner accountants.**

| Item | Condition and amount | Official source |
| --- | --- | --- |
| Ordinary domestic deadline | 15th day of third month after year end; calendar 2026: 15 March 2027; fiscal year ending 30 June 2027: 15 September 2027. Weekend/legal-holiday relief can move a deadline; special foreign cases are held for referral. | [Form 1065 instructions, When To File](https://www.irs.gov/instructions/i1065) |
| Filing extension | Properly complete Form 7004 by the original deadline, estimate and pay tax if applicable; generally six months, calendar 2026 to 15 September 2027. It does not extend payment. | [Form 7004 instructions](https://www.irs.gov/instructions/i7004) |
| Section 6698 indexed rate | USD 260 per partner per month or fraction, for returns **required to be filed in 2027**, not every return filed that year; maximum 12 months, reasonable-cause exception. | [Rev. Proc. 2025-32 section 4.55](https://www.irs.gov/irb/2025-45_IRB), [section 6698](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6698.htm) |

### 2. Compute ordinary income and reconcile the partners

In the 2025 layout, page 1 line 23 is ordinary business income after deductions; rental and portfolio items are separately reported on Schedules K and K-1. Schedule K summarizes all partners' items; K-1 reports each partner's share. Attach a K-1 for every person who was a partner at any time during the year, including a departing partner, and furnish the partner copy. Reconcile each K-1 category to Schedule K. A change of interests during the year needs a section 706(d) allocation; do not allocate a full year's items solely from year-end percentages. [F] [Form 1065 (2025)](https://www.irs.gov/pub/irs-pdf/f1065.pdf)

### 3. Separate guaranteed payments from profit shares

Payments for services or use of capital are guaranteed payments to the extent determined without regard to partnership income. The recipient includes ordinary income in the taxable year within or with which ends the partnership year in which the payment is deducted as paid or accrued under its accounting method. A partnership deduction must satisfy section 162 and section 263 capitalization rules. An income-dependent profit allocation is not a line 10 guaranteed-payment deduction. [G] [F]

- **Minimum guarantee, original regulatory illustration:** 30% of income before guaranteed payments, with a USD 10,000 floor. At USD 20,000 income: USD 6,000 profit share and USD 4,000 guaranteed payment. At USD 60,000: USD 18,000 profit share and no guaranteed payment. [G, example 2]
- **Fixed payment plus loss, original illustration:** USD 10,000 for services plus 30% of income or loss; USD 9,000 loss after the payment gives USD 2,700 allocated loss, subject to section 704(d), plus USD 10,000 ordinary guaranteed-payment income. [G, example 3]
- **2025 reporting:** deductible trade/business guaranteed payments on page 1 line 10; Schedule K and K-1 4a services, 4b capital, 4c total. Partner medical insurance is included under the line 10 instructions. Syndication service payments are capital expenditures, not line 10 deductions; those instructions nevertheless place them on K/K-1 4b. [F]

Payments outside the partner capacity, disguised services/sales, property used to satisfy a guaranteed payment, and passive-income treatment of services versus capital payments: **Check this point with one of our partner accountants.**

### 4. Self-employment, capital, allocations and losses

**AUDIT FLASH POINT** — Use the 2025 self-employment worksheet for Schedule K line 14a and K-1 box 14 code A. The instructions include guaranteed payments for services to both general and limited partners; they do not complete box 14 for estates, trusts, corporations, exempt organizations or IRAs. Whether an LLC member or state-law limited partner qualifies for the section 1402(a)(13) exclusion, and any nonresident-alien/totalization position: **Check this point with one of our partner accountants.** Do not decide that exclusion from a label, hours test or management description alone. Partner tax computation routes to `us-schedule-c-and-se-computation`. [F]

**Tax-basis capital:** 2025 K-1 Item L uses the tax-basis transactional method when required; it is not required when Schedule B question 4 is Yes. It can differ from outside basis, which includes liabilities and partner-specific adjustments. Contributions use cash plus adjusted tax basis of property, reduced by associated liabilities assumed or attached to the property; the result can be negative. Missing capital roll-forward: **Check this point with one of our partner accountants.** [F]

**Allocations:** section 704(a) generally follows the agreement; under section 704(b), missing allocations or allocations without substantial economic effect follow the partner's interest under all facts and circumstances. Section 704(c) requires contributed-property allocations to account for basis versus value at contribution. Selecting a traditional, curative or remedial method, reverse layers, deficit restoration, qualified income offsets, shifting/transitory allocations or redesigning the agreement: **Check this point with one of our partner accountants.** [L]

**Liabilities and distributions:** recourse/nonrecourse classification, guarantees, section 752 tiers, qualified nonrecourse financing, distribution gain and sections 734/743/754 adjustments: **Check this point with one of our partner accountants.** A guarantee alone is not a safe instruction to allocate all debt or allow a loss.

**Loss limits:** the partner applies basis, at-risk, passive-activity and excess-business-loss limitations in that order; specific deduction limits can apply before at-risk and passive limits. In particular, section 704(d) limits allocated partnership loss to year-end adjusted outside basis. Do not present allocated losses below as immediately deductible. Partner-specific calculations, real-estate-professional status and short-term-rental exceptions require the partner's facts; route to the applicable partner Guide. [L] [Partner K-1 instructions](https://www.irs.gov/instructions/i1065sk1)

### 5. Section 199A information

The 2025 K-1 box 20 code Z statement reports potential qualified items, W-2 wages, UBIA, qualified PTP items and REIT dividends, identifying businesses, SSTBs and aggregations as applicable. The partner determines inclusion and the deduction. Guaranteed payments **for services** are excluded from QBI; a profit share is not automatically QBI. Aggregation elections and partner deduction thresholds: **Check this point with one of our partner accountants.** Route the partner computation to `us-qbi-deduction`. [F]

### 6. K-2/K-3 and small-partnership tests — 2025 only

The following is a **2025-edition reference**, held from use for a 2026 exemption pending the edition check. International reporting can be relevant even without foreign activity. [K]

| Test | All conditions, 2025 edition | Official source |
| --- | --- | --- |
| Domestic exception: activity | Domestic, non-QDD partnership; no foreign activity, or only passive-category foreign income (disregarding the high-taxed-income exception), creditable foreign tax no more than USD 300, with income and tax shown on a furnished/deemed-furnished payee statement. Foreign activity includes foreign taxes, foreign-source income/loss and interests in foreign corporations, partnerships, branches or disregarded entities. The remaining domestic-exception conditions below must also hold. | [K-2/K-3 instructions, domestic exception criterion 1](https://www.irs.gov/instructions/i1065s23) |
| Domestic exception: partners | All direct partners during the year: US citizen/resident-alien individuals; domestic decedents' estates with only such individual beneficiaries; domestic grantor trusts with only such individual grantors and beneficiaries; domestic non-grantor trusts with only such individual beneficiaries; S corporations; LLCs disregarded into one of those; or domestic partnerships whose direct partners are those preceding types. | [K-2/K-3 instructions, criterion 2](https://www.irs.gov/instructions/i1065s23) |
| Notice and requests | Notify by K-1 furnishing that K-3 is available on request; no request on/before the one-month date (one month before filing). For 2025 calendar filers on extension the latest date is 17 August 2026. Timely requests require filing relevant K-2/K-3 parts and furnishing the requesting partner's filed K-3 on the filing date. Later requests require that partner's requested K-3 within one month, without removing the exception for others. Annual requests are needed unless subsequent years are specifically requested. | [K-2/K-3 instructions, criteria 3–4 and request notes](https://www.irs.gov/instructions/i1065s23) |
| Small partnership | All four Schedule B question 4 conditions: receipts **less than USD 250,000**; year-end assets **less than USD 1 million**; K-1s filed and furnished by the extended deadline; neither filing nor required to file M-3. This removes L, M-1, M-2, page 1 Item F and K-1 Item L. Its separate K-2/K-3 exception also needs the notice and request rules above. | [K-2/K-3 instructions, small partnership exception](https://www.irs.gov/instructions/i1065s23) |

The alternative Form 1116 exemption exception: **Check this point with one of our partner accountants.** The original two-person domestic LLC holding an international mutual fund with more than USD 300 of foreign tax fails the 2025 domestic-exception activity test, but that alone does not require all K-2/K-3 parts; another exception may apply.

**M-3, 2025 edition:** triggered by year-end total assets or adjusted total assets of at least USD 10 million, receipts of at least USD 35 million, or a reportable entity partner owning/deemed owning directly or indirectly at least 50% of capital, profit or loss on any day. Required filers with year-end assets below USD 50 million, and voluntary filers, may complete only Part I plus M-1 instead of Parts II/III; the eased rules also remove Schedule C and Form 8916-A. Use the M-3 definitions. [Form 1065 instructions, Item J](https://www.irs.gov/instructions/i1065)

### 7. BBA audit regime

**AUDIT FLASH POINT** — Test the annual election out before preparing Schedule B-2. Under regulation 301.6221(b)-1, the count must be no more than **100 required K-1 statements**, adding the statements required from S corporation partners to their shareholders for the relevant year. Every direct partner must be eligible for the entire partnership year: individual, C corporation, qualifying foreign entity treated as a C corporation if domestic, S corporation, or estate of a deceased partner. Partnerships, trusts, disregarded entities, other estates, nominees, nonqualifying foreign entities and qualified subchapter S subsidiaries are ineligible. [B]

Elect on the timely return including extensions, disclose every partner during any part of the year and the required S corporation shareholder data (identity, correct US TIN or permitted alternative, classification and other required information), and notify partners **within 30 days** of election. It cannot be revoked without IRS consent. Use Schedule B-2; do not assume a future form question number. [B] [IRS election procedure](https://www.irs.gov/businesses/partnerships/elect-out-of-the-centralized-partnership-audit-regime)

Unless it validly elects out, designate a representative for each tax year. That person has sole BBA authority and binds the partnership and partners. Substantial US presence requires a US TIN, US street address/area-code telephone and availability to meet the IRS in the US. An entity representative must legally exist and have a designated individual meeting the same presence test. [P]

Imputed-underpayment modifications, push-out elections and interest, AAR versus amended-return corrections and representative changes: **Check this point with one of our partner accountants.** Do not use the old instruction equating the push-out election deadline with the statement-furnishing deadline.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No income and no deductible/creditable expenditure | Test the domestic filing exception and its QOF/QDD overrides; do not say every partnership always files. [F] |
| Fixed services payment versus priority share | Apply step 3 and the agreement; a missing agreement is a hold, not a default guaranteed payment. [G] |
| Partner described as limited or non-managing | Hold the self-employment classification in step 4. |
| Asset value exactly USD 1 million | Fails the **less-than** asset condition in the 2025 small-partnership test. [K] |
| Foreign partner or foreign taxes | Test the actual reporting parts and exceptions; no blanket domestic-only exemption. [K] |
| Missing 2026 form confirmation | Edition hold; no final 2026 line/box or exemption conclusion. |

## Worked cases

**Case 1 — fixed payment or profit priority, original 2026 inputs.** Two-member LLC; both US citizens; B manages full time and A is an investor with no management role. USD 90,000 for B before a 50/50 residual split, versus a 30% profit priority then a 50/50 split. Income before payment: USD 300,000 in the good year, USD 60,000 in the bad year. Assume the agreement validly supports the allocations, the services payment is currently deductible, all income/expense items are from a qualifying domestic trade or business, and there are no other adjustments. A's limited-partner status is **not established** by these facts. [G] [L] [F]

Good year: fixed payment leaves USD 210,000 ordinary income, USD 105,000 each; B has USD 90,000 services payment plus USD 105,000 share = USD 195,000. Profit priority gives B USD 90,000 + USD 105,000 = USD 195,000 and A USD 105,000. Potential QBI allocated to B is USD 105,000 versus USD 195,000, a USD 90,000 difference, before partner-specific adjustments; this is not the deduction. These use the 2025 line 23, box 1 and box 4a labels solely as a layout illustration. [G] [F]

Bad year: fixed payment leaves USD 30,000 loss, USD 15,000 each; B's USD 90,000 payment less allocated loss = USD 75,000 arithmetic net, subject to loss limits. Profit priority gives B USD 18,000 + USD 21,000 = USD 39,000 and A USD 21,000. If B is properly subject to the general-partner self-employment worksheet treatment and no worksheet adjustments apply, good-year earnings are USD 195,000 under either option; do not turn that conditional computation into a classification ruling for A or B. [G] [F] [L]

```oa-check
name: Guaranteed payment against profit priority, normal and bad year (2026)
inputs:
  income_good: 300000
  income_bad: 60000
  payment: 90000
  priority: 0.30
  share: 0.5
steps:
  - gp_box1_each_good: (income_good - payment) * share
  - gp_b_total_good: payment + gp_box1_each_good
  - gp_b_qbi_good: gp_box1_each_good
  - alloc_b_good: income_good * priority + (income_good - income_good * priority) * share
  - alloc_b_qbi_good: alloc_b_good
  - qbi_difference: alloc_b_qbi_good - gp_b_qbi_good
  - gp_box1_each_bad: (income_bad - payment) * share
  - gp_b_total_bad: payment + gp_box1_each_bad
  - alloc_b_bad: income_bad * priority + (income_bad - income_bad * priority) * share
  - alloc_a_bad: (income_bad - income_bad * priority) * share
expected:
  gp_box1_each_good: 105000.00
  gp_b_total_good: 195000.00
  alloc_b_good: 195000.00
  qbi_difference: 90000.00
  gp_box1_each_bad: -15000.00
  gp_b_total_bad: 75000.00
  alloc_b_bad: 39000.00
  alloc_a_bad: 21000.00
```

**Case 2 — late return, departing member, original 2026/2027 dates.** Calendar-year LLC: three members at 31 December 2026 and a fourth who sold out in June 2026. No extension; filed 2 June 2027. Assume no disaster/service-related deadline postponement and no penalty relief. Four persons were partners during the year; three months or fractions after 15 March 2027 gives 4 × USD 260 × 3 = **USD 3,120**. At 14 months late, cap at 12: **USD 12,480**. With a valid extension to 15 September 2027 and filing on 1 October 2027: one part-month, **USD 1,040**. Relief is a separate determination. [R] [N]

```oa-check
name: Section 6698 penalty, four partners (returns due in 2027)
inputs:
  partners: 4
  rate: 260
  months_late: 3
  months_very_late: 14
  months_after_extension: 1
steps:
  - penalty: partners * rate * min(months_late, 12)
  - penalty_capped: partners * rate * min(months_very_late, 12)
  - penalty_extended: partners * rate * min(months_after_extension, 12)
expected:
  penalty: 3120.00
  penalty_capped: 12480.00
  penalty_extended: 1040.00
```

**Foreign-partner fact pattern, inputs preserved.** Delaware LLP: active US C corporation 40%, passive-investor French-resident individual 30%, managing US-resident-alien individual 30%; two foreign customers with no withheld foreign tax; foreign dividends and withheld foreign tax from a brokerage fund. These partner types can satisfy BBA eligibility (individuals have no nationality restriction in that test), assuming they remain eligible throughout the year and all count/election conditions in step 7 hold. This does not establish income source from customer location. K-2/K-3 parts, foreign-partner self-employment/totalization, section 1446 withholding and Forms W-8/8804/8805/8813, and corporate foreign-tax-credit treatment: **Check this point with one of our partner accountants.** [B]

**Family-partnership fact pattern, inputs preserved.** Texas FLP: founder-owned single-member-LLC general partner 1%; founder limited partner 49%; two adult children 25% each. In 2020 the founder contributed a rental building worth USD 1,000,000, tax basis USD 200,000, mortgage USD 400,000; sold in 2026. Contribution-date difference = **USD 800,000**. Sale price, accumulated depreciation, remaining built-in gain, guarantees and lender qualifications are missing. Do not assume the 2026 gain, a zero ending section 704(c) balance, qualified nonrecourse status, passive status, a K-2/K-3 exemption or assets **over** USD 1 million. A direct disregarded-entity partner blocks the BBA election out. For the remaining applications: **Check this point with one of our partner accountants.** [L] [B]

## When to refuse or refer

For each topic below the action is: **Check this point with one of our partner accountants.** Do not finalize the affected treatment pending resolution.

| Existing code/topic | Hold |
| --- | --- |
| R-1065-CORP; R-1065-SMLLC | Corporate/S election or single-owner classification; route to the appropriate return Guide. |
| R-1065-PTP; section 761; spouse/co-owner cases | Special classification and filing exclusions. |
| R-1065-TIER; R-1065-BBA | Tiered/ineligible partner or uncertain election eligibility. |
| R-1065-743; R-1065-704C | Basis elections/adjustments, contribution layers and method selection. |
| R-1065-707A | Non-partner-capacity, disguised payment/sale or property payment. |
| R-1065-1061 | Carried-interest holding-period treatment. |
| R-1065-1446; R-1065-8865 | Foreign-partner withholding or foreign-partnership information returns. |
| R-1065-PUSH | Audit adjustments, push-out statements and AAR computation/correction. |
| R-1065-PTET | State pass-through elections, returns and withholding; use the state's Guide. |
| R-1065-SE | Limited-partner, LLC or cross-border self-employment classification. |
| R-1065-704B | Economic effect, capital-account provisions and allocation design. |
| R-1065-CAPITAL | Missing tax-basis capital reconciliation. |
| Attached forms and partner limits | Depreciation/section 179, property sales, rentals, business interest, research credit, noncash charity, listed-transaction/disclosure forms, farmland instalments and partner estimated taxes: use the applicable form-year instructions and specialist Guide; no threshold-only filing shortcut here. |

## Filing and payment

File and [furnish the required K-1s by the return deadline including a valid extension](https://www.ecfr.gov/current/title-26/section-1.6031%28b%29-1T); applicable K-2/K-3 schedules follow their own exceptions/request rules. Retain the acknowledgement and furnishing evidence. [F] [K]

E-filing under regulation 301.6011-3 applies with **at least 10 returns of any type** required during the calendar year ending with/within the partnership year (excluding schedules attached to the partnership return), or **more than 100 direct partners over the year**. The short-year count uses the calendar year in which that short year ends. Check hardship waivers, religious exemptions, IRS exemptions and unsupported electronic-return types before concluding paper filing is disallowed. [Electronic-filing regulation](https://www.ecfr.gov/current/title-26/section-301.6011-3)

Section 6698 applies to late **or incomplete** required returns, monthly or part-month up to 12, with the count of partners during **any part** of the year. It is assessed on the partnership; reasonable cause is an exception. A valid extension moves the lateness start; a late extension request does not establish one. Use the USD 260 rate only for returns required in 2027. [N] [R] [E]

First Time Abate, automatic administrative exemption, reasonable-cause evidence, Rev. Proc. 84-35 relief, and separate sections 6721/6722 K-1 penalty amounts/caps/correction tiers: **Check this point with one of our partner accountants.** No promise of relief from timely filing in three prior years alone. Partnership taxes/payments outside the ordinary income allocation, including section 7519 and audit underpayments, also remain on hold; do not assume a zero payment obligation.

## Completion checklist

Confirm classification, year and edition; resolve affected holds; reconcile K to every K-1 and capital records; document payments, allocations and loss-limit information; test K-2/K-3 exceptions with the applicable edition; document BBA election or representative; retain extension, filing and furnishing evidence. For K-1 identity, residence/type, percentages, liabilities/guarantees, contributions, distributions, built-in gains, credits, AMT and separate activities, use the applicable form-year instructions rather than the removed full-box catalogue.

## Sources

Read on **2026-11-26**, only for the stated passages. The statutory 2024-edition section 704 text is corroborated by the current 2025 IRS instructions for the retained allocation/basis rules; no newer contrary rule was identified in those passages.

| Reference | Official source and passages read | Read on |
| --- | --- | --- |
| F | [Form 1065 instructions (2025)](https://www.irs.gov/instructions/i1065): Who Must File and exceptions; When To File; Period Covered; Electronic Filing; Item J/M-3 eased requirements; line 10; K/K-1 sharing, payments, tax-basis capital, self-employment worksheet and code Z. | 2026-11-26 |
| Form | [Form 1065 (2025)](https://www.irs.gov/pub/irs-pdf/f1065.pdf): page 1 year, partner count and lines 10/23. | 2026-11-26 |
| E | [Form 7004 instructions (12/2025)](https://www.irs.gov/instructions/i7004): proper filing, deadline, extension period and payment. | 2026-11-26 |
| G | [Treas. Reg. 1.707-1(c)](https://www.ecfr.gov/current/title-26/section-1.707-1): guaranteed payments, deduction/capitalization, inclusion timing, examples 2–3. | 2026-11-26 |
| L | [26 USC 704(a)–(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapK-partI-sec704.htm): agreement, economic effect, contributed property, basis limit; [partner K-1 instructions (2025)](https://www.irs.gov/instructions/i1065sk1): loss-limit order. | 2026-11-26 |
| K | [K-2/K-3 instructions (2025)](https://www.irs.gov/instructions/i1065s23): domestic exception criteria/foreign-activity definition, request timing, small-partnership exception, Form 1116 alternative and filing/furnishing timetable. | 2026-11-26 |
| B | [Treas. Reg. 301.6221(b)-1(b)–(c)](https://www.ecfr.gov/current/title-26/section-301.6221%28b%29-1), [IRS election procedure](https://www.irs.gov/businesses/partnerships/elect-out-of-the-centralized-partnership-audit-regime): count, eligibility, timely annual election, disclosures and notice. | 2026-11-26 |
| P | [IRS representative guidance](https://www.irs.gov/businesses/partnerships/designate-or-change-a-partnership-representative): annual designation, authority, entity representative and substantial presence. | 2026-11-26 |
| R | [Rev. Proc. 2025-32 section 4.55](https://www.irs.gov/irb/2025-45_IRB): USD 260 for partnership returns required in 2027. | 2026-11-26 |
| N | [26 USC 6698(a)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6698.htm): late/incomplete returns, extension, reasonable cause, partner count, monthly cap and assessment. | 2026-11-26 |
| Advice | [Circular 230 section 10.37](https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.37): factual/legal assumptions and relating law to facts; [regulation 1.6031(b)-1T](https://www.ecfr.gov/current/title-26/section-1.6031%28b%29-1T): K-1 furnishing deadline. | 2026-11-26 |
| E-file | [Treas. Reg. 301.6011-3](https://www.ecfr.gov/current/title-26/section-301.6011-3): electronic requirements, exceptions and counting including short years. | 2026-11-26 |

Not yet confirmed: final 2026 form/box/question layout and K-2/K-3 exceptions; all applications explicitly held or referred above. They are not usable filing conclusions in this Guide. The original cases and both executable blocks retain their original years and inputs.

[F]: https://www.irs.gov/instructions/i1065
[E]: https://www.irs.gov/instructions/i7004
[G]: https://www.ecfr.gov/current/title-26/section-1.707-1
[G, example 2]: https://www.ecfr.gov/current/title-26/section-1.707-1
[G, example 3]: https://www.ecfr.gov/current/title-26/section-1.707-1
[L]: https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapK-partI-sec704.htm
[K]: https://www.irs.gov/instructions/i1065s23
[B]: https://www.ecfr.gov/current/title-26/section-301.6221%28b%29-1
[P]: https://www.irs.gov/businesses/partnerships/designate-or-change-a-partnership-representative
[R]: https://www.irs.gov/irb/2025-45_IRB
[N]: https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6698.htm
