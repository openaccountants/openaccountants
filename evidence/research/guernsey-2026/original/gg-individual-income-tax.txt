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

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Who this applies to

Prepare ordinary calendar-year 2026 individual tax working papers for the Guernsey income-tax jurisdiction. Cap screening and conditional full-year cap comparisons are included; full statutory cap eligibility, resident-only elections, trusts, pension encashments and foreign-tax relief remain outside these calculations.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Residence and scope

Revenue Service guidance treats an individual as resident with at least 91 days in the year, or at least 35 days plus 365 days in the preceding four years. Principal residence includes 182 days, or 91 days plus 730 in the preceding four years, with an additional permanent-arrival rule. Sole residence also tests residence elsewhere. Record day counts, prior years and the subsequent-year evidence needed by the arrival rule. [Residence guidance and s3 extract](https://gov.gg/residency).

Section 3(4) counts presence at **midnight** for Guernsey and other places. Build the day schedule from travel/overnight evidence; do not count any daytime visit automatically. Section 3(2)'s solely-resident test deems residence elsewhere for that particular test by **91 days in that place**, not simply by a foreign passport or a foreign jurisdiction's tax label. Treaty residence remains separate. [Statutory section 3 extract, subsections (2) and (4)](https://gov.gg/CHttpHandler.ashx?id=167965&p=0).

For permanent arrival under section 3(3)(c), establish residence in the arrival year, sole/principal residence in the following year, and non-residence in the immediately preceding year. A permanent-home intention alone does not satisfy all three conditions. Section 3(5)–(6) permits Director-issued exceptional-circumstance guidance through a statement of practice; this is not a self-selected day-count exemption. [Section 3 extract](https://gov.gg/CHttpHandler.ashx?id=167965&p=0).

Do not treat an immigration permission or an address as the residence determination. Separately document which income enters the tax base and any treaty outcome.

## Rates, bands and thresholds

Income tax is 20%. The personal allowance is £15,200. Withdrawal starts at £85,000, at £1 for every £5 above it. Additional withdrawable reliefs follow a specified order; the protected pension amount and transfer rules require separate handling. [Rates and allowances](https://gov.gg/RStax-rates-and-allowances); [withdrawal rules](https://gov.gg/wopa).

| Selected item | 2026 amount / condition | Source |
|---|---|---|
| Personal allowance | £15,200 | [Rates page](https://gov.gg/RStax-rates-and-allowances) |
| Withdrawal threshold | £85,000 | [Withdrawal table](https://gov.gg/wopa) |
| Withdrawal ratio | £1 relief per £5 excess income | [Withdrawal rules](https://gov.gg/wopa) |
| Pension relief protected from withdrawal | £2,500 of otherwise eligible relief | [Withdrawal rules](https://gov.gg/wopa) |
| Principal-home mortgage interest relief | Maximum £3,500 per person, subject to entitlement | [2026 rates changes](https://gov.gg/RStax-rates-and-allowances) |
| Charge of child allowance | £9,800, subject to conditions and annual claim | [Rates page](https://gov.gg/RStax-rates-and-allowances) |

These are deductions/allowances, not equivalent cash tax refunds. Do not infer eligibility from the amount alone.

## The base and computation

For a case where the reviewer has established the relevant income base, full personal-allowance entitlement, no transferred allowance, no additional relief and no special regime:

1. Set income `I` to the reviewed base, not automatically to gross cash receipts.
2. Compute withdrawal `W = max(0, (I - 85,000) / 5)`.
3. Personal allowance `A = max(0, 15,200 - W)`.
4. Preliminary tax `T = max(0, I - A) × 20%`.
5. Reconcile credits, withholding and payments separately. For additional reliefs, replace this simplified model with the published ordered withdrawal calculation.

| Assumed income | Allowance after withdrawal | Tax before credits |
|---|---:|---:|
| £50,000 | £15,200 | £6,960 |
| £85,000 | £15,200 | £13,960 |
| £100,000 | £12,200 | £17,560 |
| £161,000 | £0 | £32,200 |

At the allowance-only exhaustion boundary, £85,000 + 5 × £15,200 = £161,000. This does not establish exhaustion of additional reliefs.

### Ordered withdrawal beyond the personal allowance

For a full-year case, establish the relevant income for withdrawal **before subtracting the allowances being withdrawn**. Calculate the withdrawal amount, then apply it in this published order: personal allowance; dependent relative; charge of children; infirm person; housekeeper; mortgage interest; pension contributions above the protected £2,500. At each step remove no more than that category's eligible amount and carry unused withdrawal into the next category. The protected pension amount is not a new allowance for someone who has no eligible contribution. [Withdrawal FAQ, categories and order](https://gov.gg/wopa).

The withdrawal page says arrivals/departures require a proportionately reduced income threshold. Its historical worked examples use older thresholds and allowances; do not copy them into 2026. The precise part-year apportionment and the full statutory income definition remain to be verified before automating those cases. [Withdrawal FAQ](https://gov.gg/wopa).

### Transfers and specific relief conditions

A transfer requires unused allowance and the required agreement, not merely marriage or shared residence. The rates page requires **both parties to submit annual returns**, including leaving automatic assessment where needed. If the donor later needs the transferred allowance, the recipient's assessment changes. Transferred allowances are also subject to the recipient's high-income withdrawal. The guidance includes a separate cohabiting-with-children transfer route; use its form and conditions rather than treating every cohabiting couple as eligible. [Rates page, transfers](https://gov.gg/RStax-rates-and-allowances); [withdrawal FAQ, spouses](https://gov.gg/wopa).

The charge-of-child route covers qualifying lone parents who are not cohabiting, with the specified family-allowance or higher-education condition. The alternative married/cohabiting route requires the stated whole-year total-incapacity and employed-childcarer conditions **and** the family-allowance or full-time higher-education condition. The allowance must be requested each year and claimants must file a return. Check the family facts against the complete guidance rather than counting all parents. [Rates page, charge of child](https://gov.gg/RStax-rates-and-allowances).

For rent-a-room relief, the rates page permits up to **two furnished rooms** in the principal private residence, let to a **non-family member over 18**, with up to **£10,000 per room**. A self-contained unit, guesthouse or B&B business does not fit that stated route. Gross rent above the per-room allowance remains taxable under the page's rule; it is not an exemption for all receipts once the letting qualifies. Other rental deductions, allocation and interaction require separate review. [Rates page, rent a room](https://gov.gg/RStax-rates-and-allowances).

## Tax-cap screening before using the ordinary calculation

Revenue Service says spouses elect separately from 2023; the former joint cap is not a general current couple entitlement. Special Alderney/Open Market grandfathering needs separate review. Cap users receive no personal allowances; arrival/departure years require apportionment. Qualifying income generally includes foreign income and Guernsey bank interest; other Guernsey income needs separate treatment. A cap election can use the appropriate cap form instead of a full income-detail return. Self-employed, non-employed and pension-age electors face maximum weekly social contributions. Confirm their contribution category and current maximum before comparing elections. [Revenue Service, introductory rules, qualifying income and social contributions](https://gov.gg/taxcap).

The linked monetary table, page 5, excludes Guernsey/Alderney property income, Guernsey pension/annuity triviality payments and lump sums above the tax-free limit, and, from 2023, unauthorised payments from approved pension/annuity schemes. Do not model these receipts as absorbed by a worldwide cap. Identify each excluded receipt and verify its separate tax treatment. [Monetary Values, page 5](https://gov.gg/CHttpHandler.ashx?id=174308&p=0).

**2026 amounts now corroborated:** the rates page links a different document, **Monetary Values 2026, V2 dated 16 July 2026**. Page 5 confirms £160,000 for qualifying non-Guernsey income and £320,000 for worldwide income, subject to exclusions. These cap **tax liability**, not taxable income. The same page lists £60,000 for the Open Market and new Alderney property regimes, subject to Sixth Schedule eligibility; it marks the former Alderney resident cap unavailable from 31 December 2025. Do not carry that former £65,000 cap into 2026. The Alderney property regime began in 2025 and covers arrival plus three following years on an individual basis. This table does not establish a particular person's eligibility or grandfathered amount. [2026 table, page 5](https://gov.gg/CHttpHandler.ashx?id=185595&p=0).

The old cap-page download still ends at 2024. Use the newer table for 2026 figures, while retaining the guidance for its stated mechanics and exceptions. The linked consolidated law returned HTTP 403. Full statutory eligibility, election deadlines, apportionment and special-cap transitions remain open; these examples do not resolve them.

For a cap elector in the applicable category, the 2026 table lists maximum weekly contributions of £468.72 (Class 2 self-employed), £420.80 (Class 3 non-employed under pension age), or £135.51 (Class 3 non-employed over pension age). Assess these separately from income tax, using the applicable contribution weeks. [2026 table, page 6](https://gov.gg/CHttpHandler.ashx?id=185595&p=0); [cap-election consequence](https://gov.gg/taxcap).

### Conditional full-year cap comparisons

Assume one individual, full-year qualifying residence, valid elections and independently established income classification. Exclude credits, pension payments, special property caps and part-year rules. All amounts below are reviewed taxable income, not gross receipts. Compare ordinary 20% taxation with the qualifying-income route (qualifying tax limited to £160,000, other income taxed separately) and the combined route (included income tax limited to £320,000). Guernsey property tax remains additional. No personal allowances apply on these assumed high incomes. [Cap mechanics](https://gov.gg/taxcap); [2026 limits and exclusions, page 5](https://gov.gg/CHttpHandler.ashx?id=185595&p=0).

**Qualifying-income route:** £1 million qualifying income, £100,000 other included Guernsey income and £20,000 taxable Guernsey rent. Ordinary tax is £224,000. The qualifying route gives £160,000 + £20,000 + £4,000 = **£184,000**. The combined route gives £220,000 + £4,000 = £224,000, so it offers no reduction on these facts. A cap is not a compulsory charge above ordinary liability.

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

**Combined route with excluded rent:** change the other included income to £1 million. Ordinary tax is £404,000; the qualifying route gives £364,000. The combined route gives £320,000 plus £4,000 property tax, or **£324,000**. Reporting £320,000 as total tax would omit the property exclusion. Social contributions remain additional in both examples.

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

**Screening example:** a married couple cannot simply combine their income under the former general joint cap. Review each person's election and income categories. If either receives a pension triviality payment or Guernsey rental income, isolate it for separate tax analysis before comparing a cap with ordinary taxation. This is a classification check, not a computed cap liability. [Cap guidance](https://gov.gg/taxcap); [exclusions, page 5](https://gov.gg/CHttpHandler.ashx?id=174308&p=0).

## Deadlines, filing and evidence

The Revenue Service states **30 November 2026 for the 2025 personal return**. Do not relabel that as the 2026-return deadline. Check the notice for the relevant year and retain confirmation of any automatic-assessment exemption. [Personal returns](https://gov.gg/revenue-service/personal-tax-returns).

Collect employment and investment statements, foreign income/tax records, residence-day evidence, pension records and each allowance's supporting documents. An unused allowance transfer must be supported by both parties' positions and consent; do not assume it remains available when the transferor's income changes. [Allowances guidance](https://gov.gg/RStax-rates-and-allowances).

People living in, working in or receiving income from Guernsey must file unless the Director has given written dispensation. Changed circumstances require reassessment of that dispensation. A business owner must submit accounts with the personal return. Online and paper routes exist; keep the submission confirmation or receipt. [Personal-return guidance](https://gov.gg/revenue-service/personal-tax-returns).

### Non-resident income and agency

The personal-return guidance requires an agent for a non-resident individual's Guernsey income, with responsibility for deduction, returns and tax collection. Its agent definition includes a manager or someone paying/receiving income for the non-resident. Deducted tax must reach Revenue Service **within one month of deduction**, with the non-resident deduction form. Direct assessment is a concession requiring prior agreement, not an election made by omitting the agent. The page identifies rent, pensions, employment, business and partnership income as categories requiring review. Treaty and source exemptions must be checked separately before calculating a deduction. [Agency and non-resident returns](https://gov.gg/revenue-service/personal-tax-returns).

### Departure form versus annual return

The departure form can replace the departure-year return only for permanent departure with earnings/bank-interest income alone, subject to its exclusions. File both where there is other income, a Guernsey property to be let, allowances beyond the personal allowance, principal-home mortgage relief, retirement-annuity-trust contributions, allowance transfers, or a Guernsey personal/occupational pension with a destination outside the UK. A UK destination alone does not establish exemption from filing. [Departure form, page 1](https://gov.gg/CHttpHandler.ashx?id=101103&p=0).

Use separate forms for spouses. Include departure/return intentions, forwarding address, income through departure and final payslip; self-employed people attach accounts/computations. For retained rental property, provide expected rent to 31 December, letting/repair arrangements and rent-collector details. The form's income fields do not override its annual-return exclusions. [Form, pages 1–6](https://gov.gg/CHttpHandler.ashx?id=101103&p=0).

**Boundary examples:** a permanent salary-and-bank-interest departure with only the personal allowance fits the stated replacement route. Add a Guernsey property to be let: both forms are required. Neither outcome determines residence, treaty relief or departure-year tax apportionment. [Form, page 1](https://gov.gg/CHttpHandler.ashx?id=101103&p=0).

For continuing Guernsey income after departure, the penalties guidance requires a full-year income declaration. Reconcile the departure form with the later return and the non-resident agency rules above. [Revenue Service departure FAQ](https://gov.gg/taxpenalties).

## Penalties and interest

Revenue Service currently describes an individual late-return penalty of £200 plus £10 daily. Filing within 30 days of the initial penalty removes the daily component; filing later triggers daily penalties back to the initial penalty date, not merely after day 30. The CRS/FATCA exception is outside this calculation. The page's displayed deadline concerns the 2023 return; use the year-specific notice for the actual filing deadline. [Penalty calculation guidance](https://gov.gg/taxpenalties).

**Conditional arithmetic:** if the notice and receipt establish 40 chargeable days, the unreduced individual penalty is £200 + 40 × £10 = £600. If filing satisfies the 30-day grace condition, only £200 remains. Confirm the day count against the notice; this example does not decide inclusive-date counting. [Penalty guidance](https://gov.gg/taxpenalties).

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

For income below the personal allowance, the guidance limits the late-filing penalty to £50 **after the return is received and assessment issued**. Low income does not dispense with filing. An appeal alone does not stop daily accrual: file and retain submission evidence. [Penalty FAQ](https://gov.gg/taxpenalties).

### Appeal and collection are separate

The linked Form 690(b), dated 12/21, gives a 30-day appeal period from the penalty order's issue date, citing section 76. Complete the year, charged amount, own calculation and grounds; sign and retain the order and filing evidence. Late applicants must explain lateness; acceptance is not automatic. For medical grounds, attach evidence connecting the condition to inability to file; for timely filing, attach the online submission number or paper receipt. An adviser needs signed authority. The form lists **taxpenaltyqueries@gov.gg** for penalty appeals. [Current linked appeal form, page 1](https://gov.gg/CHttpHandler.ashx?id=101085&p=0).

Collection is suspended only if the Director confirms it in writing; otherwise pay by the due date or arrange payment. This is distinct from stopping further daily penalties by filing. Page 2 expects filing within 14 days after the impediment ends and leaves disputed reasonable grounds to the Tribunal. The £50 no-liability restriction does not apply to companies. [Form, pages 1–2](https://gov.gg/CHttpHandler.ashx?id=101085&p=0).

The form remains the authority's linked operational document but is dated 2021. Current statutory text, full late-appeal/Tribunal procedure, late-payment surcharges and interest remain unverified here. Do not extend the penalty-appeal clock to assessment appeals.

### Tribunal preparation and further appeal

The Tribunal's currently linked guidance states that it reflects February 2022 law, reviewed April 2023. Section 1 requires written grounds to the Director within 30 days of assessment/order issue, or notification of a surcharge/supplement. Preserve the relevant triggering document; these are different events. Check current legislation before relying on this older procedure. [Guidance, pages 2 and 8](https://gov.gg/CHttpHandler.ashx?id=122165&p=0).

For a hearing, follow the Clerk's case-management directions for evidence, arguments, agreed facts and bundles. Do not treat the usual preparation periods as fixed deadlines. Check the proposed agreed facts before consenting. A late appeal needs an explanation and can be dismissed; new grounds have a separate discretion where omission was not wilful or unreasonable. [Pages 13–15](https://gov.gg/CHttpHandler.ashx?id=122165&p=0).

Further appeal to the Royal Court is on law, not a rehearing of facts. The guidance requires notice to the Tribunal President within 21 days from issue of the full written decision, identifying legal grounds to the Clerk, followed by a case-stated process. This is not the original 30-day appeal clock. Verify the current court rules with an advocate before filing. [Page 19](https://gov.gg/CHttpHandler.ashx?id=122165&p=0).

## Cross-border residence evidence

Revenue Service distinguishes registration certificates, domestic residence certificates and treaty residence forms. Its guidance requires residence/registration before a certificate request and a completed Guernsey return before signing a treaty residence form. Do not present a registration certificate as a treaty tie-break decision. For UK claims, apply the [UK–Guernsey treaty Guide](gg-uk-treaty-employment-and-relief.md) as well as domestic residence. [Residence certificates guidance](https://gov.gg/residency).

## Two worked examples that recompute

**Personal allowance only.** Assume a full-year case with £100,000 reviewed withdrawal/tax income, full initial £15,200 allowance entitlement and no other reliefs. Withdrawal is (£100,000 − £85,000) / 5 = £3,000; remaining allowance £12,200; income tax before credits £17,560. [Rates](https://gov.gg/RStax-rates-and-allowances); [withdrawal](https://gov.gg/wopa).

```oa-check
name: Guernsey 2026 personal allowance withdrawal
inputs:
  income: 100000
  threshold: 85000
  personal_allowance: 15200
steps:
  - withdrawal: max(0, (income - threshold) / 5)
  - retained_allowance: max(0, personal_allowance - withdrawal)
  - tax: max(0, income - retained_allowance) * 0.20
expected:
  withdrawal: 3000
  retained_allowance: 12200
  tax: 17560
```

**Protected pension edge case.** Assume £200,000 full-year reviewed income, eligible personal allowance £15,200, eligible mortgage relief £3,500 and **independently established deductible** pension contributions £5,000, with no other allowances. Withdrawal is £23,000. It removes £15,200 personal allowance, £3,500 mortgage relief, then the £2,500 withdrawable pension portion. The remaining £1,800 withdrawal does not remove the protected £2,500. Tax before credits is (£200,000 − £2,500) × 20% = **£39,500**. This does not establish pension-scheme eligibility or the ordinary contribution deduction limit. [Withdrawal order and protection](https://gov.gg/wopa).

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

## Ask the client first

- What are the midnight day counts for this year, the previous four years and the following-year arrival test?
- What income sources and foreign tax/residence positions exist?
- Which allowances, pension contributions and mortgage amounts have supporting entitlement evidence?
- Has allowance been transferred, and have both parties filed and agreed?
- Is there a written filing dispensation, agency arrangement or direct-assessment concession?
- Is a cap election being considered, and what are each spouse’s income categories, arrival/departure dates, contribution status and prior special-cap elections?
- What returns, assessments, notices and payments have already been made?

## Forward changes

The tax-reform page describes personal-tax and GST changes for 2029 and corporate changes for 2027. They are not substituted into the 2026 calculation. Track enactment and commencement separately. [Tax reform timetable](https://gov.gg/taxreform).

## Self-checks and output

- Retain the relevant source version, the applicable period and the facts establishing scope.
- Reconcile every input to the client's records; keep estimates separate from actual amounts.
- Recompute the example and boundary cases before applying the method.
- Record exclusions and unresolved points explicitly. Do not convert a missing source into an exemption.
- Deliver a calculation, evidence list, filing calendar and reviewer questions. Record the exact revision reviewed.

## Sources

Read on 22 October 2026: [residence guidance](https://gov.gg/residency), [section 3 extract](https://gov.gg/CHttpHandler.ashx?id=167965&p=0), [2026 rates and reliefs](https://gov.gg/RStax-rates-and-allowances), [withdrawal guidance](https://gov.gg/wopa) and [personal-return guidance](https://gov.gg/revenue-service/personal-tax-returns). The [reform timetable](https://gov.gg/taxreform) remains a future-change reference. Full statutory base/relief verification, part-year rules, resident-only elections, full cap eligibility and special-regime transitions, pension limits, complete penalties and independent review remain open.

## Disclaimer

General tax and accounting reference material only. These drafts have not been professionally attested. A qualified professional in the relevant jurisdiction must check the facts, current law, elections and deadlines before anyone files, pays or acts on an output.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
