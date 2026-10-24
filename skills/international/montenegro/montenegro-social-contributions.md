---
name: montenegro-social-contributions
description: "Prepare Montenegro 2026 social-contribution workpapers for employees, actual-income entrepreneurs, supplementary entrepreneurs, qualifying contract recipients and registered farmers. Determine insured status, gross or statutory base, pension/unemployment allocation, additional service contributions, exemptions, timing and annual refund routing. Includes six executable controls. Use for doprinosi, PIO, dopunska preduzetnička djelatnost, contribution floors, zimnica and annual pension ceilings. Adds the promulgated annual PIO refund procedure and Form 1 mapping. Current cap instrument, collective-agreement floors, special populations, actual submission/IRMS, international coordination and independent review remain open. Source-cited preparation draft; payroll income tax and municipal surtax require separate reconciliation."
version: 0.4
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
sources:
  - url: "https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0"
    title: "Ministry contribution-law consolidation through 160/25"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0"
    title: "Enacted 160/25 contribution amendment, applying January 2026"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0"
    title: "Ministry payroll calculation instruction through 103/24"
    as_of: "2026-10-24"
  - url: "https://www.sluzbenilist.me/propisi/362476/download"
    title: "107/23 annual pension-contribution refund rule and actual Form 1"
    as_of: "2026-10-24"
  - url: "https://www.monstat.org/cg/novosti.php?id=4638"
    title: "MONSTAT December and full-year 2025 earnings release"
    as_of: "2026-10-24"
---

# Montenegro social-contribution preparation v0.4

## Who this applies to

Build a contribution workpaper after classifying each person's insurance status and income. Employees, principal entrepreneurs, employed persons with supplementary business, directors, contract recipients and farmers have distinct provisions. A second payment does not automatically take the employee treatment or escape contributions because its recipient already has employment. [Articles 4–9, 11, 15, 18][law]

This source-cited draft replaces the retained 2025 secondary-source summary preserved at Git checkpoint `4692a57a`. The current Ministry consolidation through 160/25 and actual amendment were read. Amendment Article 8 applies the new provisions from 1 January 2026. No named accountant review, actual registration, accepted return, annual cap instrument or collective-agreement floor has been obtained. All seven country domains remain partial. [Law][law]; [amendment][amend]

The September government package also contains a **proposal**, not an enacted instrument verified here, to set Articles 15/16/18 insurance rates to zero. Its Article 5 specifies application from 1 January 2027. The scanned one-page proposal was visually read; neither it nor its government approval is evidence that zero rates apply to 2026 pay. Enacted status, final text and related Labour Fund changes require separate future-period verification. [Proposal Articles 1–5][proposal]

## Rates, bases and allocation

| Population/item | Contribution treatment | Source |
| --- | --- | --- |
| Ordinary insured employee | Employee PIO 10%; employer PIO 0%; employee unemployment 0.5%; employer unemployment 0.5% | Articles 15(1), 18(1) |
| Employee Labour Fund charge | Employer 0.2% on gross personal earnings under the payroll instruction; separate from the two insurance contributions listed in the law | Instruction Article 5; law Article 2 |
| Principal entrepreneur | PIO 10% and unemployment 1%, on the relevant statutory bases | Articles 5(1)(12), 7(1)(9), 9(7), 11(5), 15(2), 18(2) |
| Supplementary entrepreneur, employed person | PIO 10%, on Article 9(11) base; do not automatically add the principal-entrepreneur unemployment charge | Articles 4(11a), 5(1)(16), 7, 9(11), 15(2) |
| Qualifying contract recipient not insured on another basis | PIO 10% on taxable independent-activity income, not automatically gross cash | Articles 5(1)(13), 9(8), 15(2) |
| Additional credited service | Employer/entrepreneur additional PIO: 6%, 9%, 12%, 18%, 28% for the statutory 12-to-14/15/16/18/24 month categories | Articles 8, 16 |
| Registered qualifying farmer | Article 9 general base 20% of prior-year average gross monthly pay; Article 9a own mandatory base 12%, difference funded from budget | Articles 9(10), 9a, 15(2) |

Sources: [law][law]; [instruction][instruction]. Article 2 lists PIO and unemployment; the current text deletes the old health contribution provisions. That does not establish entitlement to health benefits or an exemption from other employment levies. The ordinary 10.5% employee/0.7% employer sum excludes additional service, special levies, income tax and municipal surtax; it is not a universal employer-cost rate. [Articles 2, 6, 10, 15–18][law]; [instruction Articles 4–6][instruction]

## Establish the base before multiplying

Employee gross earnings encompass salary for work/time, increases, salary compensation and specified other taxable remuneration, including direct work/performance-related payments. Record cash, noncash, reimbursement, arrears and compensation separately; a bank label is insufficient to decide the base. Article 18a has express exclusions and exceptions. [Articles 3a, 9(1), 18a][law]

The lowest monthly contribution base is the **gross basic salary prescribed by the general collective agreement for the relevant qualification category**, under Article 4(21). Article 9(1) applies that minimum to the specified employees. Do not replace it with an assumed net minimum wage gross-up. Obtain the operative agreement, category, working/insurance period and any current amendments before certifying a low-pay or part-period calculation. Labour-law minimum salary compliance is a separate check; no current numerical minimum is certified here. [Articles 4(21), 9(1), 11][law]

For principal entrepreneurs paying tax on actual income, Article 9(7) uses realised/estimated annual turnover: through EUR 9,000, 60% of prior-year average monthly gross pay; over 9,000 through 15,000, 100%; over 15,000, 150%. It permits a higher elected base. Article 11(5) supplies the corresponding ordinary unemployment base. Annual lump-sum taxpayers instead follow their legally determined taxable income. Do not confuse turnover, profit and the monthly contribution base. [Articles 4(23), 9(7), 11(5)][law]

Article 9(11), added for 2026 supplementary entrepreneurs, uses the same turnover-linked 60/100/150% monthly base structure with higher-base election. Existing employment is part of that status, not an automatic exemption from its PIO. Article 7's principal-entrepreneur category must not be silently extended to the separately defined supplementary status. Mixed-status cases need documented registration/classification. [Articles 4(11a), 5(1)(12) and (16), 7, 9(11), 15(2)][law]; [amendment Articles 1–4][amend]

For 2026, MONSTAT's full-year 2025 average gross monthly pay is EUR 1,206. The December-only EUR 1,220 and annual average net EUR 1,012 are different populations. Thus the statutory percentages yield 723.60 / 1,206 / 1,809 for the three turnover bands, before a valid higher election. Verify the relevant year and period each time. [Article 4(23)][law]; [MONSTAT release, 30 January 2026][stats]

Directors use Article 9(2) remuneration; qualifying contracts use Article 9(8) taxable income. Foreign workers, posted persons, citizens abroad, religious communities and compensation recipients have distinct status/base/payer rules. Article 11's reproduced numbering contains cross-reference tensions between categories and bases; do not resolve exceptional foreign/director cases by copying a mismatched row. Actual insurance legislation, agreement and authority interpretation remain necessary for those cases. [Articles 5, 7, 9, 11–13, 15, 21][law]

## Exclusions, suspensions and date gates

Article 18a addresses listed receipts and noncash benefits. Noncash remuneration replacing unpaid salary is an express exception to the noncash exclusion. Taxability and contribution liability are separate conclusions; an exclusion from this law is not proof of income-tax exemption. Retain the exact type, purpose, valuation, legal basis and supporting documents. [Article 18a][law]

From January 2026 the zimnica exclusion refers to **70% of previous-year average monthly gross pay**, replacing the former minimum-wage reference. For 2026 the resulting limit is EUR 844.20. Apply that only to a genuinely qualifying zimnica payment, with prior payments and applicable administration checked; do not relabel ordinary salary or infer exemption for every listed receipt up to that amount. [Article 18a(2)][law]; [amendment Articles 5, 8][amend]; [statistics][stats]

Article 18d grants the stated contribution relief to a person with acquired digital-nomad status receiving the described employment/independent-activity income from an employer not registered in Montenegro. Retain immigration status, payer and income evidence; remote work alone is insufficient. Full status procedure and interaction with other coverage/taxes remain open. Article 18c is expired, with Article 31a's historical 2023 limit; do not use it as a new-hire exemption in 2026. [Articles 18c–18d, 31a][law]; [amendment Article 6][amend]

Approved employment suspension and legally registered temporary cessation of principal independent activity follow Articles 19–20. The latter permits a request to continue contributions within five working days after temporary deregistration. Informal inactivity or no revenue is not documented cessation. Dispute/court-settlement arrears have Article 29b's rule referring to the rate when payment should have occurred; do not apply the current rate automatically to every historical award. [Articles 19–20, 29b][law]

## Annual ceiling and refund are a separate workpaper

Article 14(1) requires PIO calculation/payment across the different income bases. The annual maximum is fixed by the Ministry's yearly instrument; Article 22 provides a post-year refund application and decision. Do not use the old Guide's EUR 68,765 from a prior year, divide an annual amount into an assumed monthly cap, stop unemployment at a PIO maximum or promise an automatic payroll refund. [Articles 14, 22–24][law]

The operative **2026 maximum has not been retrieved**. The Gazette ceiling record found is explicitly for 2025; do not use it for 2026. Article 22 requires the insured person's post-year application by the end of the following calendar year, with an authority decision. Thus a 2026 claim is a 2027 application; eligibility/amount still require the correct annual maximum and actual paid contributions. No numeric 2026 capped/refund example is certified here. [Articles 14, 22–24][law]; [2025 ceiling record, discovery only][cap2025]

### Annual PIO refund procedure and actual Form 1

The actual promulgated 107/23 Gazette text and attached **Form 1** were read, including visual inspection of the form. It replaces the 42/12 refund rule. Use this PIO-specific process, not an old general-social-insurance ZPDO template still appearing in official search results. The Ministry reproduction names the form but omits it; the actual Gazette PDF contains both the rule and form. [Refund rule Articles 1–6 and Form 1][refund]

Prepare a person/year schedule of every insurance basis, payer, actual payment, reported contribution base/rate, cumulative base and supported annual maximum. Reconcile to payer reports and tax-authority records. The rule bases the post-year refund on paid-contribution data delivered to the tax authority, not an unpaid accrual or a new estimate. For several insurance bases, Article 4 allocates the refund to the basis whose contributions were paid after the annual maximum was reached. Preserve the chronology rather than allocating a refund pro rata across employers or choosing the highest rate automatically. Historical different rates need their actual period/payment rules. [Refund Articles 2, 4][refund]; [law Articles 14, 22][law]

| Application routing | Competent tax-office location under Article 3 |
| --- | --- |
| Employee | Employer's seat |
| Contractual remuneration, including qualifying royalty/service contracts | Individual's residence |
| Board/director remuneration | Payer's seat |
| Independent activity | Tax-registration location |

Source: [refund Article 3][refund]. For mixed statuses/payers in different offices, obtain the authority's competent-office direction; the rule does not justify a universal residence-office shortcut. An eUprava service listing inspected here gives generic residence wording and older agency names, which are not substituted for the rule's category-specific routing or treated as current successful electronic acceptance. [Rule][refund]; [service listing, access comparison only][refund-service]

The actual Form 1 requests the tax authority/regional office, claim year, insured person's name, basis of insurance, recipient/bank account/bank, applicant name/JMB/address and date. Enter the proper insured person and entitlement, not automatically the employer's account. Keep supporting person/year reconciliation, payer/authority contribution evidence, annual maximum and any representation authority with the submission. These are workpaper/evidence requirements; the printed form itself does not list a new universal attachment checklist. No invented mandatory notarisation or fee is added. [Form 1][refund]; [law Article 22][law]

The regional office decides by a formal decision. Article 4 requires refund **within 30 days of the decision**, not within 30 days of the application. Keep application receipt, any information requests, decision and payment reconciliation. The rule does not prescribe a separate decision-making deadline; current tax-procedure/appeal rules and payment offsets must be verified separately. Do not net an anticipated claim against current remittances. No unemployment/Labour Fund refund follows from this PIO maximum rule. [Refund Articles 1, 4][refund]; [law Articles 22–25][law]


## Computation workflow and evidence

1. Identify person, payer, legal status, work country, insurance periods and all concurrent activities. Check the applicable international agreement/coverage certificate before an exemption. [Articles 4–8][law]
2. Classify each payment and establish gross earnings or the statutory turnover/average-pay/taxable-income base. Record floor, exclusions, election and additional service evidence. [Articles 3a, 9–13, 18a–18d][law]
3. Calculate PIO, unemployment and employer Labour Fund separately, maintaining liability by person, period and payer. Keep PIT/surtax in the payroll workpaper. [Articles 15–18][law]; [instruction Articles 3–6][instruction]
4. Reconcile person totals to contribution control accounts, reports, payments and authority ledger. Preserve adjustments separately from current pay; do not net an unapproved annual refund against remittances. [Articles 21–25][law]
5. Escalate missing status, period/floor/cap evidence or inconsistent official form references before filing. A source-cited draft is not an accepted submission or professional attestation.

## Worked examples

Hypothetical full-month 2026 EUR preparation cases with established classification, no higher elected base, no relief except where stated and no annual refund applied. Ordinary employee gross is assumed above the applicable verified floor; no particular current numerical floor is asserted. Values are contribution controls, not complete payslips or filings.

### 1. Ordinary employee and separate employer charges

Gross contribution base 2,000; no special service/additional levy. PIO/unemployment deductions 210; employer unemployment/Labour Fund 14. Salary PIT/surtax and other possible employment costs are excluded from this control. [Articles 15, 18][law]; [instruction Articles 4–5][instruction]

```oa-check
name: Montenegro ordinary employee contributions
inputs:
  gross_base: 2000
steps:
  - employee_pio: gross_base * 0.10
  - employee_unemployment: gross_base * 0.005
  - employee_total: employee_pio + employee_unemployment
  - employer_unemployment: gross_base * 0.005
  - employer_labour_fund: gross_base * 0.002
  - employer_charges: employer_unemployment + employer_labour_fund
expected:
  employee_pio: 200
  employee_unemployment: 10
  employee_total: 210
  employer_unemployment: 10
  employer_labour_fund: 4
  employer_charges: 14
```

### 2. Principal actual-income entrepreneur, lower turnover band

Annual turnover 8,500, principal status and actual-income taxation established. Full-month 60% base uses prior-year average gross 1,206; PIO 72.36 plus unemployment 7.236, rounded separately to cents 7.24, total 79.60. This does not compute business income tax. [Articles 9(7), 11(5), 15(2), 18(2)][law]; [statistics][stats]

```oa-check
name: Montenegro principal entrepreneur contribution base
inputs:
  prior_average_gross: 1206
steps:
  - monthly_base: prior_average_gross * 0.60
  - pio: round(monthly_base * 0.10, 2)
  - unemployment: round(monthly_base * 0.01, 2)
  - total: pio + unemployment
expected:
  monthly_base: 723.60
  pio: 72.36
  unemployment: 7.24
  total: 79.60
```

### 3. Supplementary business alongside employment

Annual turnover 16,000, Article 5(1)(16) status established. Full-month base 150% × 1,206 = 1,809, PIO 180.90, in addition to the separately calculated employment PIO. No principal-business unemployment charge is added to this supplementary base. Annual refund remains separate. [Articles 5(1)(16), 7, 9(11), 14, 15(2)][law]; [amendment][amend]; [statistics][stats]

```oa-check
name: Montenegro supplementary entrepreneur pension
inputs:
  prior_average_gross: 1206
  employment_pio: 200
steps:
  - supplementary_base: prior_average_gross * 1.50
  - supplementary_pio: supplementary_base * 0.10
  - combined_pio_before_refund: employment_pio + supplementary_pio
expected:
  supplementary_base: 1809
  supplementary_pio: 180.90
  combined_pio_before_refund: 380.90
```

### 4. Registered farmer own contribution and budget difference

Qualifying farmer registration established. General base 20% and own mandatory base 12% of 1,206 produce total PIO 24.12, own payment 14.472 and budget difference 9.648, rounded here to 14.47 and 9.65. Actual quarterly assessment and authority allocation control payment. [Articles 9(10), 9a, 15(2), 21(8)][law]; [statistics][stats]

```oa-check
name: Montenegro registered farmer contribution allocation
inputs:
  prior_average_gross: 1206
steps:
  - general_base: prior_average_gross * 0.20
  - own_base: prior_average_gross * 0.12
  - total_pio: round(general_base * 0.10, 2)
  - own_pio: round(own_base * 0.10, 2)
  - budget_difference: total_pio - own_pio
expected:
  general_base: 241.20
  own_base: 144.72
  total_pio: 24.12
  own_pio: 14.47
  budget_difference: 9.65
```

### 5. Established additional service category

Employee base 2,000 and documented 12-month-to-15-month credited-service category. Additional employer PIO at 9% is 180, on top of ordinary employer unemployment/Labour Fund 14. Employee deductions remain 210. Eligibility and service records are assumptions, not a finding that any specific role qualifies. [Articles 8, 16(2)][law]; [instruction Articles 4–5][instruction]

```oa-check
name: Montenegro additional credited service employer charge
inputs:
  gross_base: 2000
steps:
  - extra_pio: gross_base * 0.09
  - ordinary_employer_charges: gross_base * 0.007
  - specified_employer_charges: extra_pio + ordinary_employer_charges
expected:
  extra_pio: 180
  ordinary_employer_charges: 14
  specified_employer_charges: 194
```

### 6. Qualifying zimnica exclusion limit

A documented qualifying 2026 zimnica payment is 800, with no prior use of the relevant exclusion. The 70% limit is 844.20, so the whole assumed payment falls within it. This tests the limit only; it does not establish the PIT result, a Labour Fund exclusion or treatment of an excess payment. [Article 18a(2)][law]; [amendment Articles 5, 8][amend]; [statistics][stats]

```oa-check
name: Montenegro 2026 zimnica contribution exclusion ceiling
inputs:
  prior_average_gross: 1206
  qualifying_payment: 800
steps:
  - exclusion_limit: prior_average_gross * 0.70
  - excluded_contribution_receipt: min(qualifying_payment, exclusion_limit)
  - headroom: exclusion_limit - excluded_contribution_receipt
expected:
  exclusion_limit: 844.20
  excluded_contribution_receipt: 800
  headroom: 44.20
```

## Reporting, payments, corrections and sanctions

Article 21 distinguishes the payer and deadline by population: ordinary employer contributions by the 15th for the previous month; specified foreign-employed citizens and religious-community cases quarterly; principal/supplementary entrepreneurs through the income-tax calculation/payment mechanism; specified board/contract receipts by the payer by the 15th; farmers under quarterly authority assessment. If an immune foreign/diplomatic payer does not pay the specified employee contributions, Article 21(7) gives the employee five days from receipt. Classify before applying a deadline. [Article 21][law]

The employment instruction additionally requires payment with remuneration, and for noncash earnings no later than the month's last working day. Its older OPD1 report references and retained historical calculation table are not proof of current IOPPD/IRMS fields. Do not interpret the contribution law's 15th-day rule as permission to defer payment due with salary. Actual current integrated reporting rules, form codes, portal schema, account references, correction sequence and period-specific transition notices remain to be reconciled in the payroll method. [Instruction Articles 7–10][instruction]

Article 22 requires an annual-cap refund application after year end, by the end of the following calendar year, decided by the tax authority. Preserve paid amounts and decision; no unemployment or Labour Fund refund is inferred from that PIO rule. Article 25 refers unresolved assessment, collection, interest and limitation matters to tax procedure, with its express PIO limitation exception. Exact current interest, appeal/stay and enforcement methods are still open. [Articles 22–25][law]

For Article 26's listed payer failures, statutory fines are EUR 2,000–20,000 for a legal person, 500–1,000 for its responsible person and 1,000–6,000 for an entrepreneur. Article 27 specifies 250–2,000 for its listed individual nonpayment cases. These are offence-specific ranges, not automatic charges for every late return. [Articles 26–27][law]

## Reviewer handoff and remaining evidence

Supply person/status/registration, all work and insurance periods, payer/residence, international coverage evidence, gross receipt classification, applicable floor/elected base, yearly statistics/cap, calculation and payment ledgers, additional-service records, actual form/acknowledgement, amendments and refund decisions. Bank narratives alone do not establish any of these.

Still open: current numerical floor and partial/multiple-employer application; operative 2026 cap, mixed-status competence and current refund submission/offset/remedy implementation; full benefit/exemption valuation and Labour Fund interactions; exceptional Article 11 cross-references; foreign/posted coverage agreements; farmer and supplementary-business assessment/reporting implementation; historical arrears; current IOPPD/IRMS fields, amendments, payment accounts and procedures; all other employment levies; independent country review and named accountant attestation. The payroll and individual Guides have been rebuilt for 2026; their current local-decision, forms/IRMS, specialist and procedural gaps remain open. Reconcile their stated bases and periods with this contribution method rather than treating companion presence as completed implementation.

## Sources

Read on **24 October 2026**. Source labels identify actual operative reading, not a completed taxpayer filing.

- [Contribution law][law], Ministry March 2026 DOCX consolidation through 160/25: Articles 1–27 and targeted 29b–33 read; historical transitional rates not applied as 2026 rates.
- [Enacted amendment][amend], 160/25 Articles 1–8: supplementary business, zimnica, digital-nomad and application gates read.
- [Payroll instruction][instruction], Ministry April 2026 reproduction through 103/24: Articles 1–10 and historical/reference material read. Old table/report references are disclosed, not certified as current IRMS implementation.
- [MONSTAT full-year 2025 release][stats], 30 January 2026: prior-year average gross 1,206 distinguished from net and December-only values.
- [September government proposal][proposal]: one-page scanned text visually inspected, including January 2027 application; enactment/final text not certified.
- [107/23 refund rule and actual Form 1][refund]: operative Articles 1–6 and form read; form visually inspected. 2026 cap and accepted electronic submission not obtained.
- [2025 ceiling record][cap2025]: discovery metadata only, not operative 2026 amount or current refund form.

[law]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[amend]: https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0
[instruction]: https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0
[stats]: https://www.monstat.org/cg/novosti.php?id=4638
[proposal]: https://wapi.gov.me/download/7edeb39c-81cc-4468-bd62-6cfc5a36443c?version=1.0
[refund]: https://www.sluzbenilist.me/propisi/362476/download
[refund-service]: https://m.euprava.me/usluge/detalji_usluge?generatedServiceId=245
[cap2025]: https://www.sluzbenilist.me/propisi/387933

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
