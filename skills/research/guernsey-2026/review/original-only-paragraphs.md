
# README.md FULL ORIGINAL-ONLY PARAGRAPHS
---
jurisdiction: GG
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  XB: gg-uk-treaty-employment-and-relief
---

# Guernsey tax pack: source-cited drafts

Owner Michael, confirmed in [issue #397](https://github.com/openaccountants/openaccountants/issues/397). Work is consolidated in [PR #514](https://github.com/openaccountants/openaccountants/pull/514). This is a gap register, not a completeness or attestation claim. Territory and year must be checked in each Guide; the UK treaty's geographical definition does not cover every Bailiwick island.

| Domain | Draft | Remaining work |
|---|---|---|
| IT-IND | [Individual tax](gg-individual-income-tax.md) | Residence day-count law, allowance withdrawal, selected reliefs and conditional 2026 cap comparisons drafted; cap figures confirmed in July 2026 official table, with former Alderney cap cessation distinguished. Departure filing routes and individual penalty/appeal-form steps now drafted. Full statutory base/cap eligibility, special-cap transitions, part-year computations, payment/interest and complete Tribunal procedure remain open |
| IT-CORP | [Corporate tax/substance](gg-corporate-tax-substance.md) | Registration/residence evidence, activity rates and filing/penalty guidance expanded; statutory substance scope, governance, CIGA map and high-risk IP evidence/return rules and substance penalty/appeal and inspection-response procedures added; full residence/base, losses, distributions, remaining enforcement cross-references, licensing cross-references and minimum-tax depth remain open |
| VAT / consumption | [GST transition](gg-gst-transition.md), policy scope only | October 2026 adopted conditions and published 2029 timetable verified; current tax scope, enacted commencement, customs/excise, registration, returns and penalties remain open |
| SC, PR | [Payroll/social insurance](gg-payroll-social-insurance.md), [secondary pensions](gg-secondary-pensions.md) | Classification, dividend timing, ordinary benefits, vehicle/housing rules and employer procedures expanded; statutory penalty reconciliation, special periods/benefit categories, specialist pension cases and international coverage still open |
| TP | [UK treaty adjustment rules](gg-uk-treaty-employment-and-relief.md#associated-enterprises-and-corresponding-adjustments), limited corridor coverage | Dated OECD profile treatment of MAP access and bilateral APAs now drafted. Domestic connected-party rules and documentation remain unverified; official legal library and practice-page access failed. Treaty material does not establish a complete domestic regime |
| Capital / property | [Property document duty](gg-property-document-duty.md) | Graduated rates, surcharge repeal, conditional downsizing calculations and Court/registration procedure; full charging law, exemptions, anti-avoidance scope, payment/claims/penalties and other property taxes remain open |
| XB | [UK treaty employment and relief](gg-uk-treaty-employment-and-relief.md) | Pension/government-service and student allocation conditions now drafted; claim operations, domestic ordinary-residence and pension lump-sum treatment, domestic PE implementation; capital-gains/offshore allocation now drafted, with domestic valuation/disposal filing open; published arbitration procedure and conflicting effective-status evidence now recorded; other corridors and exit/non-resident rules |

The VAT entry is an unresolved programme consumption-tax scope, not an assertion of a current Guernsey VAT. No reviewed not-applicable finding has been made. Nine Guides are present. All nine have received independent AI source/editorial review within their stated scopes; none is professionally attested in this work. The review records preserve unresolved substantive and operational gaps. A domain mapping establishes draft presence only.

Accounting milestone drafts: [formation](gg-company-formation.md) and [accounts/reporting](gg-company-accounts-and-reporting.md). The audit-exemption primary-source gap remains in the accounts Guide.

Sources and access dates are recorded in the new Guides and [research](../../../docs/research/); all nine Guides now have structured source metadata, which does not establish complete source verification. Remaining review, resolution of source gaps, required checks, merge and verified platform ingestion remain necessary before acceptance. Keep issue #397 open while these gaps remain.

## Independent source-review records

# gg-company-accounts-and-reporting.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-company-accounts-and-reporting
description: >
  Guernsey company accounting and reporting reference for ordinary local trading companies limited by shares. Covers transaction records, retention, annual accounts, financial periods, member circulation, audit-waiver timing and the separate annual validation. Includes December-incorporation and advance-waiver examples, a document workflow and explicit gaps for audit-excluded companies and specialised entities. Prepared for 2026 from Guernsey Registry primary guidance, including the current annual-validation page and directors handbook. The underlying consolidated law was inaccessible during this pass; this is a source-cited research draft requiring legal and independent review before filing or relying on audit relief.
jurisdiction: GG
category: financial-statements
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.4
verified_by: pending
sources:
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=174582&p=0"
    title: "Limited Companies civil penalties, July 2026"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=174583&p=0"
    title: "Annual-validation civil penalties, July 2026"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/companyfees"
    title: "Guernsey Registry: Limited Companies fee schedule, effective 1 December 2025"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=186495&p=0"
    title: "Guernsey Registry: Guidance for directors of new local trading companies"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/article/183449/Annual-Validation---Companies"
    title: "Guernsey Registry: Annual Validation - Companies"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/resolutions"
    title: "Guernsey Registry: Resolutions and Waivers"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=5097&p=0"
    title: "Guernsey Registry: Audit Exemption Waiver Resolutions"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=172173&p=0"
    title: "Company annual validation questions and options: 2026 onwards"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=173525&p=0"
    title: "Company Annual Validation Guidance: issued 4 December 2024"
    as_of: "2026-10-22"
---

The primary sources here are Registry guidance. The official consolidated-law website returned HTTP 403 during this research. The text of the current law and all audit-exclusion regulations have not been independently reconciled; no audit eligibility conclusion is certified here.

The detailed audit note links regulations identifying companies prohibited from exemption. Those regulations remain unreconciled here: do not infer that a small turnover, private ownership or an annual-validation tick box establishes eligibility. The note also contains old filing-charge and January-only validation statements; this Guide does not adopt those outdated administrative details.

The current Registry page requires annual validation between **1 January and the last day of February**, using details as at **31 December**. Companies incorporated in December of the preceding year are excepted from that cycle. Submissions use the Online Services Portal; the fee depends on company classification. [Annual validation guidance](https://www.guernseyregistry.com/article/183449/Annual-Validation---Companies).

Thus an ordinary company already registered before December 2025 files its 2026 validation by **28 February 2026**, based on 31 December 2025 details. A company incorporated in December 2025 falls within the stated exception for that cycle. This does not waive accounts, tax or other notices.

The how-to guide dated 4 December 2024 says on page 2 “unless they were incorporated in the previous year”, whereas the current annual-validation webpage specifies **December** of the previous year. Do not extend the exception to all newly incorporated companies based on the broader sentence. The discrepancy remains for statutory reconciliation; the December case is common to both descriptions. [How-to guidance](https://www.guernseyregistry.com/CHttpHandler.ashx?id=173525&p=0); [Registry annual-validation page](https://www.guernseyregistry.com/article/183449/Annual-Validation---Companies).

Check the six-year retention starting point, the financial-period length, the December-incorporation boundary, the advance waiver date and separate 30-day filing date. Prohibited audit-exemption categories, voting mechanics, approval/signature requirements and specialised-company rules remain to verify before this topic is accepted as complete.

General reference only. A qualified Guernsey professional must review the facts and current law before filing or relying on relief. This draft is not accountant-attested.


# gg-company-formation.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-company-formation
description: >
  Guernsey local company incorporation reference covering the licensed applicant, founder, director, registered office and resident agent, application documents, ownership information, person registration and Registry fees. Includes a recomputable fee example and post-incorporation handover controls. Based on primary Registry guidance checked in October 2026; current statutory reconciliation, complex ownership and specialised entities remain outside this research draft. Independent review is pending.
jurisdiction: GG
category: formation
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://www.guernseyregistry.com/companyformation"
    title: "Guernsey Registry: Incorporating a Company"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/companyfees"
    title: "Guernsey Registry: Limited Companies fee schedule, effective 1 December 2025"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/newcompanyinfo"
    title: "Guernsey Registry: Information for newly incorporated companies"
    as_of: "2026-10-22"
  - url: "https://www.guernseyregistry.com/CHttpHandler.ashx?id=186495&p=0"
    title: "Guernsey Registry: Guidance for directors of new local trading companies"
    as_of: "2026-10-22"
---

This Guide covers the incorporation process for an ordinary local trading company limited by shares. The Registry's directors handbook addresses Guernsey residents setting up such businesses. Cell companies, regulated activities, overseas migrations, guarantees and complex ownership require additional analysis. The current consolidated Companies Law could not be retrieved during this research; the requirements below are sourced to the Registry's own guidance, not presented as an independently reconciled statutory opinion. [Directors handbook, introduction](https://www.guernseyregistry.com/CHttpHandler.ashx?id=186495&p=0).

Only a corporate service provider (CSP) holding a **full fiduciary licence from the Guernsey Financial Services Commission (GFSC)** can apply to the Registrar to incorporate a company. A founder's portal account does not replace that applicant requirement. The Registry requires at least one founder member, at least one director and a registered office in Guernsey. A resident agent must be a Guernsey-resident director or a CSP, unless an exemption applies. This Guide does not establish any resident-agent exemption. [Incorporation guidance](https://www.guernseyregistry.com/companyformation).

Still to verify: current consolidated statutory provisions and amendments, name restrictions, resident-agent exemptions, complex beneficial-owner tests, regulated-sector permissions and specialised company forms. Independent source review and professional attestation are pending. This Guide's presence does not establish comprehensive Guernsey coverage.


# gg-corporate-tax-substance.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-corporate-tax-substance
description: >
  Prepare calendar-year 2026 corporate tax classification and compliance working papers. This draft does not calculate Pillar Two, regulated-sector special rules, exemption applications or every company-law obligation. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: "0.9"
verified_by: pending
sources:
  - url: "https://gov.gg/RStax-rates-and-allowances"
    title: "2026 changes: definition of a distribution"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=141223&p=0"
    title: "Income Tax (Substance Requirements) (Implementation) Regulations 2021, regulations 1, 3–10, 13–27, 30, 37–40"
    as_of: "2026-10-22"
  - url: "https://gov.gg/economicsubstance"
    title: "Revenue Service economic substance, current implementation and guidance links"
    as_of: "2026-10-22"
  - url: "https://gov.gg/RevenueService/Companies"
    title: "Company guidance"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=118096&p=0"
    title: "Form 707 non-resident status 02/26"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=183549&p=0"
    title: "Form 706 foreign-company registration 08/21"
    as_of: "2026-10-22"
  - url: "https://gov.gg/taxpenalties"
    title: "Penalty FAQ, current figures with stale introductory deadline"
    as_of: "2026-10-22"
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guernsey corporate tax, distributions and substance v0.9

The form says acceptance produces a letter detailing future responsibilities. It separately screens Guernsey-source income, a Guernsey PE, local staff, resident beneficial members, participator loans and international reporting. It expressly retains ETI returns where staff exercise functions in Guernsey. Keep that acceptance letter and each continuing-obligation assessment. **The domestic statutory residence/exclusion test is not fully established by this form; obtain it before deciding residence.** For the UK corridor, also consult the [treaty Guide](gg-uk-treaty-employment-and-relief.md). [Form 707, introduction and sections 4–5](https://gov.gg/CHttpHandler.ashx?id=118096&p=0).

The retail wording is **taxable profit more than £500,000**, not turnover of £500,000. The guidance alone does not resolve aggregation or the precise charging base at the threshold, so this draft does not invent an excess-only calculation or an exemption at the boundary. Property development, land exploitation and rent also need their own classification. [Company guidance, rates](https://gov.gg/RevenueService/Companies).

Regulation 30 replaced section 4(1)(a) with a test covering control in Guernsey **or** central management and control in Guernsey in the year of charge, and changed 'incorporated' to 'registered' in section 4(1)(b). This is direct evidence of that amendment, not the complete current section 4 or its non-residence exclusions. Reconcile the full provision and later amendments before giving a residence conclusion. [Regulation 30](https://gov.gg/CHttpHandler.ashx?id=141223&p=0).

### Distribution and loan reporting

The company guidance requires the company to deduct/pay the distribution tax and make a quarterly distribution-reporter return identifying recipient, date, amount and tax. Non-resident beneficial-member treatment requires evidence of non-residence before payment without deduction. Qualifying loans use the same reporter; repayment within **six years** permits a claim for the tax attributable to the repaid part. This is not an automatic accounting reversal. Exact distribution/loan tax computations, statutory scope and payment deadlines still need verification. [Company guidance, distributions and qualifying loans](https://gov.gg/RevenueService/Companies).

The 2026 changes page states that repayments of loans **to shareholders** are treated as dividends, excluding repayment of commercial loans by trading companies. This concerns a company repaying its borrowing from a shareholder; it is distinct from the preceding qualifying-loan case where the company lent money and receives a repayment. Do not apply the six-year tax-repayment claim to both directions. Record lender, borrower, original advance, repayment recipient, trading status and evidence supporting any commercial-loan exclusion. The guidance does not establish the complete amended statutory definition, connected-person scope or transition rules; obtain those before calculating a charge or accepting an exclusion. [Revenue Service, 2026 changes, definition of a distribution](https://gov.gg/RStax-rates-and-allowances).

**Established mixed income.** Assume review has established separate ordinary taxable income £100,000, intermediate-category income £30,000 and Guernsey rental taxable income £20,000, with no overriding wider-base or minimum-tax rule. At 0%, 10% and 20%, ordinary company tax is **£7,000**. The example does not establish deductions, stream classification, loss offsets or Pillar Two treatment. [Company rates](https://gov.gg/RevenueService/Companies).

```oa-check
name: Guernsey established corporate income streams
inputs:
  standard_income: 100000
  intermediate_income: 30000
  rental_income: 20000
steps:
  - standard_tax: standard_income * 0
  - intermediate_tax: intermediate_income * 0.10
  - rental_tax: rental_income * 0.20
  - total_tax: standard_tax + intermediate_tax + rental_tax
expected:
  standard_tax: 0
  intermediate_tax: 3000
  rental_tax: 4000
  total_tax: 7000
```

**Daily-penalty catch-up.** Assume no successful appeal/reduction and a corporate return submitted after the 30-day concession period, with **35 chargeable days established from the Order and submission dates**. The guidance calculation is £300 + 35 × £50 = **£2,050**, not merely five daily penalties. A return qualifying for the within-30-day concession would retain the £300 initial penalty without daily penalties. This example does not decide inclusive date counting or the Order's validity. [Penalty FAQ](https://gov.gg/taxpenalties).

```oa-check
name: Guernsey corporate daily penalty after concession period
inputs:
  initial_penalty: 300
  daily_rate: 50
  established_chargeable_days: 35
steps:
  - daily_penalty: daily_rate * established_chargeable_days
  - total_penalty: initial_penalty + daily_penalty
expected:
  daily_penalty: 1750
  total_penalty: 2050
```

Read on 22 October 2026: [company guidance](https://gov.gg/RevenueService/Companies), [non-resident Form 707](https://gov.gg/CHttpHandler.ashx?id=118096&p=0), [foreign registration Form 706](https://gov.gg/CHttpHandler.ashx?id=183549&p=0) and [penalty FAQ](https://gov.gg/taxpenalties). Also read the [2021 substance regulations](https://gov.gg/CHttpHandler.ashx?id=141223&p=0) and [current substance index](https://gov.gg/economicsubstance); the [reform timetable](https://gov.gg/taxreform) remains a future-change reference. Source versions and limitations are recorded in the research file. Independent source review, domestic residence law, detailed deductions/losses, distribution computation, minimum tax and publication checks remain open.

# gg-gst-transition.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-gst-transition
description: >
  Prepare Guernsey and Alderney GST transition working papers from the October 2026 approved tax reform package. Distinguish the published 2029 timetable and illustrative price calculations from enacted charging, registration and return requirements. Covers the adopted commencement safeguards, operational evidence needed before implementation, and the relationship with income-tax, social-security and benefit changes. Use for GST readiness, planned pricing and review of reform assumptions. This source-cited draft does not establish a current GST liability, a complete consumption-tax regime, customs treatment or a reviewed not-applicable determination. Enacted rules remain outstanding; the source-review record states the scope reviewed.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://gov.gg/taxreform"
    title: "States of Guernsey, approved Tax Reform package and timetable"
    as_of: "2026-10-22"
  - url: "https://statesvoting-records.gov.gg/Propositions/Details/2682"
    title: "P.2026/49 Proposition 1 as amended, carried 2 October 2026"
    as_of: "2026-10-22"
  - url: "https://statesvoting-records.gov.gg/Propositions/Details/2787"
    title: "P.2026/49 Proposition 15, direction to prepare legislation"
    as_of: "2026-10-22"
---

## Sources and acceptance gaps

All three sources in frontmatter were read on 22 October 2026: [official timetable](https://gov.gg/taxreform), [adopted commencement conditions](https://statesvoting-records.gov.gg/Propositions/Details/2682) and [legislation direction](https://statesvoting-records.gov.gg/Propositions/Details/2787). The latter two record votes carried on 2 October 2026. This draft records a verified policy transition, not comprehensive VAT/GST coverage, professional attestation or a determination that consumption taxes are inapplicable. Current domestic tax scope, customs/excise, enacted implementation, operational rules and current-law reconciliation remain open. Independent source review is recorded in the pack README.

# gg-individual-income-tax.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-individual-income-tax
description: >
  Prepare ordinary calendar-year 2026 individual tax working papers for the Guernsey income-tax jurisdiction. Cap screening and conditional full-year cap comparisons are included; full statutory cap eligibility, resident-only elections, trusts, pension encashments and foreign-tax relief remain outside these calculations. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: "0.8"
verified_by: pending
sources:
  - url: "https://gov.gg/CHttpHandler.ashx?id=122165&p=0"
    title: "Tribunal guidance: February 2022 law, reviewed April 2023"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=101103&p=0"
    title: "Leaving Guernsey, Alderney or Herm, RS-FRM-LVG-348-v1"
    as_of: "2026-10-22"
  - url: "https://gov.gg/taxpenalties"
    title: "Revenue Service late-return penalties guidance"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=101085&p=0"
    title: "Penalty appeal Form 690(b), 12/21, pages 1–2"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=185595&p=0"
    title: "Monetary Values 2026, V2 16 July 2026, pages 5–6"
    as_of: "2026-10-22"
  - url: "https://gov.gg/taxcap"
    title: "Revenue Service tax-cap guidance; historical examples are dated"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=174308&p=0"
    title: "Monetary Values, 2024 to 2018, page 5 cap exclusions"
    as_of: "2026-10-22"
  - url: "https://gov.gg/residency"
    title: "Residence guidance"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=167965&p=0"
    title: "Income Tax Law section 3 extract"
    as_of: "2026-10-22"
  - url: "https://gov.gg/RStax-rates-and-allowances"
    title: "Rates and allowances including 2026 changes"
    as_of: "2026-10-22"
  - url: "https://gov.gg/wopa"
    title: "Withdrawal of allowances, current table and historical examples"
    as_of: "2026-10-22"
  - url: "https://gov.gg/revenue-service/personal-tax-returns"
    title: "Personal returns and agency guidance"
    as_of: "2026-10-22"
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guernsey individual income tax and residence v0.8

The withdrawal page says arrivals/departures require a proportionately reduced income threshold. Its historical worked examples use older thresholds and allowances; do not copy them into 2026. The precise part-year apportionment and the full statutory income definition remain to be verified before automating those cases. [Withdrawal FAQ](https://gov.gg/wopa).

The old cap-page download still ends at 2024. Use the newer table for 2026 figures, while retaining the guidance for its stated mechanics and exceptions. The linked consolidated law returned HTTP 403. Full statutory eligibility, election deadlines, apportionment and special-cap transitions remain open; these examples do not resolve them.

```oa-check
name: Guernsey 2026 qualifying cap comparison
inputs:
  qualifying: 1000000
  other_included: 100000
  property: 20000
steps:
  - ordinary: (qualifying + other_included + property) * 0.20
  - qualifying_route: min(qualifying * 0.20, 160000) + (other_included + property) * 0.20
  - combined_route: min((qualifying + other_included) * 0.20, 320000) + property * 0.20
expected:
  ordinary: 224000
  qualifying_route: 184000
  combined_route: 224000
```

```oa-check
name: Guernsey 2026 combined cap leaves property tax outside
inputs:
  qualifying: 1000000
  other_included: 1000000
  property: 20000
steps:
  - ordinary: (qualifying + other_included + property) * 0.20
  - qualifying_route: min(qualifying * 0.20, 160000) + (other_included + property) * 0.20
  - combined_route: min((qualifying + other_included) * 0.20, 320000) + property * 0.20
expected:
  ordinary: 404000
  qualifying_route: 364000
  combined_route: 324000
```

```oa-check
name: Guernsey individual late return outside daily penalty grace
inputs:
  initial_penalty: 200
  daily_rate: 10
  confirmed_chargeable_days: 40
steps:
  - daily_penalty: confirmed_chargeable_days * daily_rate
  - unreduced_total: initial_penalty + daily_penalty
expected:
  daily_penalty: 400
  unreduced_total: 600
```

The form remains the authority's linked operational document but is dated 2021. Current statutory text, full late-appeal/Tribunal procedure, late-payment surcharges and interest remain unverified here. Do not extend the penalty-appeal clock to assessment appeals.

Further appeal to the Royal Court is on law, not a rehearing of facts. The guidance requires notice to the Tribunal President within 21 days from issue of the full written decision, identifying legal grounds to the Clerk, followed by a case-stated process. This is not the original 30-day appeal clock. Verify the current court rules with an advocate before filing. [Page 19](https://gov.gg/CHttpHandler.ashx?id=122165&p=0).

```oa-check
name: Guernsey 2026 ordered relief withdrawal protects eligible pension portion
inputs:
  income: 200000
  threshold: 85000
  personal_allowance: 15200
  eligible_mortgage: 3500
  eligible_pension: 5000
  protected_pension_limit: 2500
steps:
  - withdrawal: max(0, (income - threshold) / 5)
  - personal_removed: min(personal_allowance, withdrawal)
  - remaining_withdrawal: withdrawal - personal_removed
  - mortgage_removed: min(eligible_mortgage, remaining_withdrawal)
  - pension_withdrawable: max(0, eligible_pension - protected_pension_limit)
  - pension_removed: min(pension_withdrawable, remaining_withdrawal - mortgage_removed)
  - retained_pension: eligible_pension - pension_removed
  - unused_withdrawal: remaining_withdrawal - mortgage_removed - pension_removed
  - tax: (income - retained_pension) * 0.20
expected:
  withdrawal: 23000
  personal_removed: 15200
  mortgage_removed: 3500
  pension_removed: 2500
  retained_pension: 2500
  unused_withdrawal: 1800
  tax: 39500
```

Read on 22 October 2026: [residence guidance](https://gov.gg/residency), [section 3 extract](https://gov.gg/CHttpHandler.ashx?id=167965&p=0), [2026 rates and reliefs](https://gov.gg/RStax-rates-and-allowances), [withdrawal guidance](https://gov.gg/wopa) and [personal-return guidance](https://gov.gg/revenue-service/personal-tax-returns). The [reform timetable](https://gov.gg/taxreform) remains a future-change reference. Full statutory base/relief verification, part-year rules, resident-only elections, full cap eligibility and special-regime transitions, pension limits, complete penalties and independent review remain open.

# gg-payroll-social-insurance.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-payroll-social-insurance
description: >
  Prepare ordinary 2026 Class 1 payroll, a Class 2 review checklist and Class 3 classification/assessment working papers. Includes ordinary benefit valuation, vehicle and housing scales, and ETI reporting. Secondary pensions and mixed-status cases still need further work. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GG
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: "0.7"
verified_by: pending
sources:
  - url: "https://gov.gg/non-employedcontributions"
    title: "Class 3 non-employed contribution guidance; historical rate references excluded"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=185595&p=0"
    title: "Monetary Values 2026 V2, page 6"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=202739&p=0"
    title: "Benefits in Kind Guide 2026, sections 1–12, Fact Sheets 1–2 and cited Statements of Practice"
    as_of: "2026-10-22"
  - url: "https://gov.gg/employers"
    title: "Employer webpage"
    as_of: "2026-10-22"
  - url: "https://gov.gg/SScontributions"
    title: "Contribution classification guidance"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=102818&p=0"
    title: "2026 rates leaflet"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=175677&p=0"
    title: "Employer Guide 2025"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=196680&p=0"
    title: "SIC1 published 22 December 2025"
    as_of: "2026-10-22"
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guernsey payroll and social contributions v0.7

```oa-check
name: Guernsey Class 3 allowance applies after exemption test
inputs:
  established_income: 24960
  lower_limit: 24960
  non_employed_allowance: 11122
  rate: 0.118
steps:
  - margin_above_lower: established_income - lower_limit
  - assessment_base: established_income - non_employed_allowance
  - annual_rate_arithmetic: assessment_base * rate
expected:
  margin_above_lower: 0
  assessment_base: 13838
  annual_rate_arithmetic: 1632.884
```

The same guidance describes a written surcharge appeal to the Director within **30 days**, limited to legal liability or calculation, not an employer's error or oversight. Check the assessment notice and statutory appeal provisions for the exact time trigger and procedure. The underlying current penalty legislation remains an explicit source gap; these figures are attributed guidance, not a complete verified penalty opinion.

```oa-check
name: Guernsey eligible recurring benefit with annual exemption
inputs:
  monthly_cost: 100
  annual_exemption: 900
  months: 12
steps:
  - monthly_exemption: annual_exemption / months
  - monthly_taxable_benefit: max(0, monthly_cost - monthly_exemption)
  - annual_taxable_benefit: monthly_taxable_benefit * months
expected:
  monthly_exemption: 75
  monthly_taxable_benefit: 25
  annual_taxable_benefit: 300
```

```oa-check
name: Guernsey employer-paid income tax on benefit
inputs:
  taxable_benefit: 5000
  tax_rate: 0.20
steps:
  - grossed_income: taxable_benefit / (1 - tax_rate)
  - tax_reimbursement: grossed_income - taxable_benefit
  - total_tax: grossed_income * tax_rate
  - after_tax_value: grossed_income - total_tax
expected:
  grossed_income: 6250
  tax_reimbursement: 1250
  total_tax: 1250
  after_tax_value: 5000
```

```oa-check
name: Guernsey ordinary car benefit cost includes trade-in value
inputs:
  gross_car_cost: 30000
  extras: 3000
  employee_extras_payment: 2000
  benefit_rate: 0.20
steps:
  - benefit_cost: gross_car_cost + extras - employee_extras_payment
  - annual_benefit: benefit_cost * benefit_rate
expected:
  benefit_cost: 31000
  annual_benefit: 6200
```

```oa-check
name: Guernsey car business-use strict percentage boundary
inputs:
  total_miles: 10000
  boundary_business_miles: 7500
  above_business_miles: 7510
  gross_cost: 30000
steps:
  - boundary_percent: boundary_business_miles / total_miles * 100
  - above_percent: above_business_miles / total_miles * 100
  - ordinary_benefit: gross_cost * 0.20
expected:
  boundary_percent: 75
  above_percent: 75.1
  ordinary_benefit: 6000
```

```oa-check
name: Guernsey furnished accommodation with valid rental-value election
inputs:
  established_emoluments: 40000
  furnished_rate: 0.175
  verified_rental_value: 6000
steps:
  - percentage_benefit: established_emoluments * furnished_rate
  - benefit_with_valid_election: min(percentage_benefit, verified_rental_value)
expected:
  percentage_benefit: 7000
  benefit_with_valid_election: 6000
```

All read on 22 October 2026: [Benefits in Kind Guide 2026](https://gov.gg/CHttpHandler.ashx?id=202739&p=0), [employer webpage](https://gov.gg/employers), [contribution classification guidance](https://gov.gg/SScontributions), [2026 rates leaflet pp19–20](https://gov.gg/CHttpHandler.ashx?id=102818&p=0), [Employer Guide 2025 pp9–10 and 16–19](https://gov.gg/CHttpHandler.ashx?id=175677&p=0), and [SIC1](https://gov.gg/CHttpHandler.ashx?id=196680&p=0). The dated 2026 leaflet controls current contribution amounts; the 2025 manual is used only for the cited procedural guidance. Independent review and direct statutory reconciliation remain outstanding.

# gg-property-document-duty.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-property-document-duty
description: >
  Prepare Guernsey property document-duty working papers for 2026 conveyances, including graduated rates, the repealed additional-property surcharge, conditional downsizing relief and transaction evidence. Use for document duty, property purchase costs, realty versus personalty and the 2025 surcharge transition. This source-cited draft covers the island of Guernsey and does not extend these rates to Alderney or Sark. It supplies recomputable examples using established chargeable realty values, not a valuation opinion. Full statutory exemptions, anti-avoidance transactions, registration and payment procedures remain review requirements. Retain the transaction date, official source version and advocate's classification before relying on a calculation.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.3
verified_by: pending
sources:
  - url: "https://www.guernseyroyalcourt.gg/article/1638/Conveyances-and-Bonds"
    title: "HM Greffier: registration, duty assessment and collection"
    as_of: "2026-10-22"
  - url: "https://www.guernseyroyalcourt.gg/article/1919/Conveyances"
    title: "Advocate preparation and presentation of conveyances"
    as_of: "2026-10-22"
  - url: "https://www.guernseyroyalcourt.gg/article/3186/The-Contracts-Court"
    title: "Contracts Court witnessing and registration sequence"
    as_of: "2026-10-22"
  - url: "https://www.guernseyroyalcourt.gg/article/1921/Document-Duty"
    title: "Royal Court document-duty overview"
    as_of: "2026-10-22"
  - url: "https://parliament.gg/parliamentary-business/assets/questions/2026-16"
    title: "21 May 2026 official response, question 11, current rates and examples"
    as_of: "2026-10-22"
  - url: "https://parliament.gg/parliamentary-business/assets/propositions/P2025-121"
    title: "2026 Budget, duty amendment ordinances and paragraphs 5.87–5.96"
    as_of: "2026-10-22"
  - url: "https://parliament.gg/parliamentary-business/hansard/hansard-14-33"
    title: "5 November 2025 Hansard, pages 63–65, budget propositions 12 and 13"
    as_of: "2026-10-22"
---

# Guernsey property document duty v0.3

The Royal Court describes duty on prescribed documents presented to it, with transaction-dependent rates, fixed amounts and exemptions. That overview alone is insufficient to classify every instrument. The linked legal-library index returned HTTP 403 during research, so the full current charging law, valuation rules and exemptions remain to be reconciled. [Court overview](https://www.guernseyroyalcourt.gg/article/1921/Document-Duty).

```oa-check
name: Guernsey document duty 500000 boundary
inputs:
  additional_value: 100
steps:
  - boundary_duty: 300000 * 0.0225 + 200000 * 0.035
  - additional_duty: additional_value * 0.04
  - above_boundary_duty: boundary_duty + additional_duty
expected:
  boundary_duty: 13750
  additional_duty: 4
  above_boundary_duty: 13754
```

# gg-secondary-pensions.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-secondary-pensions
description: >
  Prepare 2026 Guernsey secondary-pension enrolment and contribution working papers for employers. Covers designated and voluntary employees, phased employer start dates, minimum contributions, the earnings base, enrolment deferral, opt-outs, refunds, re-enrolment and quarterly reporting. Distinguishes payments to the pension provider from Revenue Service returns and social-insurance contributions. Use for workplace pension setup, payroll contribution calculations and compliance reviews. Based on official employer guidance checked in October 2026. Direct statutory reconciliation, detailed enforcement, scheme-specific conditions and independent review remain outstanding; this source-cited draft does not establish comprehensive payroll coverage or professional attestation.
jurisdiction: GG
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://gov.gg/secondary-pensions-employer-guidance"
    title: "Employer scope and operative dates"
    as_of: "2026-10-22"
  - url: "https://gov.gg/article/196678/How-much-do-we-need-to-pay"
    title: "Contributions and calculation"
    as_of: "2026-10-22"
  - url: "https://gov.gg/article/196666/What-do-we-need-to-do-Pension-scheme-not-included-in-contract-of-employment"
    title: "Non-compulsory scheme employer duties"
    as_of: "2026-10-22"
  - url: "https://gov.gg/article/196679/Opting-in-and-out"
    title: "Opting in and out"
    as_of: "2026-10-22"
  - url: "https://gov.gg/Secondary-Pensions"
    title: "Secondary pensions reporting"
    as_of: "2026-10-22"
  - url: "https://gov.gg/CHttpHandler.ashx?id=102818&p=0"
    title: "2026 contribution limits, pp19–20"
    as_of: "2026-10-22"
---

The official guidance identifies penalties for employer non-compliance, including fines or imprisonment, and late-return penalties. This Guide has not verified the current statutory amounts, offence elements, notice/appeal procedures or interest rules. Do not import income-tax or social-insurance penalty amounts into this separate regime. [Employer guidance](https://gov.gg/secondary-pensions-employer-guidance); [secondary pensions overview](https://gov.gg/Secondary-Pensions).

## Sources and remaining work

All frontmatter sources were read on 22 October 2026. Exact page titles, URLs and hashes are in the accompanying research record. The guide is based on authority guidance, with direct statutory reconciliation still outstanding. Detailed notice timing, new-employer commencement, age boundaries, absence/status changes, specialist schemes, enforcement and independent review remain open. Neither this file's presence nor its arithmetic checks establish comprehensive pension or country coverage.

# gg-uk-treaty-employment-and-relief.md FULL ORIGINAL-ONLY PARAGRAPHS
---
name: gg-uk-treaty-employment-and-relief
description: >
  Apply the UK–Guernsey treaty's residence and ordinary employment-income tests and prepare a Guernsey foreign-tax-credit working paper. Covers territorial scope, individual and entity residence conflicts, the three short-visit employment conditions, the credit ceiling, permanent establishments, business-profit attribution, associated-enterprise adjustments, dividend/interest/royalty conditions, pensions and government-service distinctions, student support, capital-gains allocation, offshore overrides, mutual-agreement time limits and the published arbitration procedure with an official status discrepancy. Contains checked day-count and credit examples. Based on the official 2018 Agreement and Protocol and current HMRC treaty-status evidence checked in October 2026. This source-cited draft does not establish payroll clearance, all withholding categories, claim forms or complete cross-border coverage; independent professional review remains pending.
jurisdiction: GG
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.9
verified_by: pending
sources:
  - url: "https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/dispute-resolution/guernsey-dispute-resolution-profile.pdf"
    title: "Guernsey Dispute Resolution Profile, updated 17 March 2025, questions 2, 5–12 and 16–17"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/government/publications/guernsey-tax-treaties/2021-uk-guernsey-exchange-of-letters-in-force"
    title: "December 2021 exchange of letters: Article 27 effective 1 January 2022"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/government/publications/guernsey-tax-treaties/uk-guernsey-memorandum-of-understanding-on-arbitration-under-article-25-of-the-agreement"
    title: "UK–Guernsey arbitration memorandum: procedure and effective-date clause"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/hmrc-internal-manuals/double-taxation-relief/dt8602"
    title: "HMRC DT8602 treaty summary, payment-category conditions"
    as_of: "2026-10-22"
  - url: "https://assets.publishing.service.gov.uk/media/5c470999ed915d38b0437c54/2018_Guernsey-UK_Double_Taxation_Agreement_in_force.pdf"
    title: "UK–Guernsey Agreement and Protocol 2018, Articles 1–7, 9–14, 17–19, 21–28"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/government/publications/guernsey-tax-treaties"
    title: "HMRC Guernsey tax treaties, entry into force and effective dates"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/hmrc-internal-manuals/double-taxation-relief/dt8600"
    title: "HMRC DT8600, Guernsey agreements in force"
    as_of: "2026-10-22"
---

```oa-check
name: PE anti-fragmentation ownership boundary
inputs:
  total_equal_interests: 100
  at_boundary: 50
  above_boundary: 51
steps:
  - boundary_percentage: at_boundary / total_equal_interests * 100
  - above_percentage: above_boundary / total_equal_interests * 100
expected:
  boundary_percentage: 50
  above_percentage: 51
```

```oa-check
name: Supported PE profit bridge before domestic tax
inputs:
  attributed_revenue: 200000
  established_allowable_costs: 130000
  supported_profit_adjustment: 10000
steps:
  - initial_profit: attributed_revenue - established_allowable_costs
  - revised_profit: initial_profit + supported_profit_adjustment
expected:
  initial_profit: 70000
  revised_profit: 80000
```

```oa-check
name: Property-income dividend treaty ceiling is not a minimum tax
inputs:
  gross_dividend: 10000
  ceiling_rate: 0.15
  higher_domestic_tax: 2000
  lower_domestic_tax: 1000
steps:
  - ceiling: gross_dividend * ceiling_rate
  - higher_case_tax: min(higher_domestic_tax, ceiling)
  - lower_case_tax: min(lower_domestic_tax, ceiling)
expected:
  ceiling: 1500
  higher_case_tax: 1500
  lower_case_tax: 1000
```

```oa-check
name: Non-resident ownership strict less-than boundary
inputs:
  total_equal_shares: 100
  below_boundary_shares: 24
  boundary_shares: 25
steps:
  - below_percentage: below_boundary_shares / total_equal_shares * 100
  - boundary_percentage: boundary_shares / total_equal_shares * 100
expected:
  below_percentage: 24
  boundary_percentage: 25
```

**Recommended evidence:** identify the transaction and both enterprises, ownership/control links, contracts and actual conduct, the pricing method and comparables, each territory's original profit and tax computations, the assessment adjustment and the amount of overlapping profit. These are working-paper controls, not a verified Guernsey statutory master-file/local-file requirement. Domestic anti-avoidance and deduction rules still need primary-source verification before this constitutes a Guernsey transfer-pricing Guide.

```oa-check
name: Associated-enterprise profit adjustment and excess interest
inputs:
  supported_service_price: 120000
  actual_service_price: 90000
  actual_interest: 50000
  supported_independent_interest: 40000
steps:
  - profit_adjustment: supported_service_price - actual_service_price
  - excess_interest: actual_interest - supported_independent_interest
expected:
  profit_adjustment: 30000
  excess_interest: 10000
```

```oa-check
name: Guernsey UK property-rich interest value boundary
inputs:
  total_value: 1000000
  boundary_property_value: 500000
  higher_property_value: 510000
steps:
  - boundary_percent: boundary_property_value / total_value * 100
  - higher_percent: higher_property_value / total_value * 100
expected:
  boundary_percent: 50
  higher_percent: 51
```

```oa-check
name: Guernsey UK offshore associated activity overlap
inputs:
  enterprise_days: 22
  associated_days: 14
  simultaneous_days: 6
steps:
  - aggregated_days: enterprise_days + associated_days - simultaneous_days
  - additional_nonoverlapping_day: aggregated_days + 1
expected:
  aggregated_days: 30
  additional_nonoverlapping_day: 31
```

## Sources and remaining work

Official [Agreement and Protocol](https://assets.publishing.service.gov.uk/media/5c470999ed915d38b0437c54/2018_Guernsey-UK_Double_Taxation_Agreement_in_force.pdf), [HMRC treaty-status page](https://www.gov.uk/government/publications/guernsey-tax-treaties) [DT8600](https://www.gov.uk/hmrc-internal-manuals/double-taxation-relief/dt8600) and [DT8602](https://www.gov.uk/hmrc-internal-manuals/double-taxation-relief/dt8602), accessed 22 October 2026. Dividend, interest and royalty allocation conditions are drafted, but full domestic withholding/claim operations remain open. Business-profit allocation and PE tests are drafted, with domestic implementation still open. Pension, government-service and student allocation conditions are now drafted; domestic definitions, pension lump sums and operational relief remain open. Capital-gains and offshore allocation are now drafted; domestic charging, valuation and disposal filing remain open. Other treaty corridors and exit issues are not comprehensively covered. Claim operations, domestic related-party and deduction rules, domestic relief interactions and independent source/professional review remain pending.