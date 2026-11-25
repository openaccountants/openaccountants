---
name: ca-fed-t2125
description: Use this skill whenever asked about Canadian self-employment business income reported on Form T2125 (Statement of Business or Professional Activities). Trigger on phrases like "T2125", "business income Canada", "self-employed expenses", "CCA", "capital cost allowance", "home office Canada", "motor vehicle expenses CRA", "business-use-of-home", "sole proprietor Canada", "net business income", "business number BN", "fiscal year end", "GST ITC", or any question about computing, classifying, or reporting business income and expenses for a Canadian sole proprietor. Covers Parts 1-8 of T2125, allowable expenses, CCA classes and rates, AccII, business-use-of-home, motor vehicle expenses, GST/HST interaction, and net income computation. ALWAYS read this skill before touching any T2125 work.
version: 2.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: Historical 2025 return calculations and original example inputs; separately dated 2026 vehicle announcements do not recertify the whole workpaper for 2026.
last_updated: 2026-11-25
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# CA Fed T2125

## Canada Self-Employment (T2125) -- Sole Proprietor Skill v2.1

This corrects the historical 2025 workpaper. **HOLD** prevents final use of an affected result until its specified evidence or condition is established; it does not establish zero deduction, no tax or non-registration.

## Rates and thresholds

Reviewed against the cited tax authorities by Nathan Wiebe on 2026-06-21. That historical attribution does not approve this proposed correction. Unresolved source, eligibility and input conditions are explicitly held below.

### T2125 (Business)

- **GST/HST registration threshold** — $30,000 in any single calendar quarter or over 4 consecutive quarters — measured on worldwide taxable supplies (before expenses) of the person AND associated persons; excludes capital property, financial services, and goodwill on the sale of a business  _(ETA s.148; CRA — Small supplier — canada.ca)_
- **CCA deduction** — Discretionary — claim any amount from $0 up to the class maximum (never mandatory); unclaimed CCA stays in UCC for later years; watch recapture / terminal loss on disposition  _(ITA s.20(1)(a); ITR Schedule II)_
- **Business-use-of-home** — Principal place of business OR used exclusively to earn business income AND on a regular and continuous basis for meeting clients, customers or patients  _(ITA s.18(12))_
- **Meals deduction** — Ordinary 50% limit; qualifying long-haul meals and statutory exceptions are separate, not a universal cap. [CRA allowable-part rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html)
- **Vehicle expense — business-use %** — Claim only the business-use portion supported by records; CRA requires a logbook of business vs total kilometres (a full logbook year can support the sample-year method)  _(ITA s.18(1)(r); ITR 7307; CRA — Motor vehicle expenses — canada.ca)_
- **Fiscal year-end (sole props)** — Generally December 31; an eligible individual may elect a non-calendar fiscal period using Form T1139 (alternative method)  _(ITA s.249.1)_
- **Line 8299** — Gross business income follows the actual Part 3 adjusted-sales/fees and other-income sequence; do not start with an already-adjusted 8299 amount and subtract GST/HST again. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)
- **Stripe/PayPal fees** — Reconstruct customer amounts before processing fees, then apply the actual Part 3 sales/tax method; net bank payouts are not the gross-income measure. Bind the appropriate fee expense and records. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)
- **Line 8910** — Rent (business premises)  _(CRA — T4002 guide — canada.ca)_
- **Line 8220** — No line 8220 on Form T2125 — telephone and utilities are both claimed on line 9220  _(CRA — T4002 guide — canada.ca)_
- **Line 8860** — Professional fees (accounting, legal)  _(CRA — T4002 guide — canada.ca)_
- **Line 8710** — Interest and bank charges  _(CRA — T4002 guide — canada.ca)_
- **Line 8523** — Allowable meals/entertainment part, ordinarily 50% with actual exceptions; not the gross receipt followed by another add-back. [CRA line 8523](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html)
- **Line 8690** — Insurance  _(CRA — T4002 guide — canada.ca)_
- **Line 8810** — Office expenses  _(CRA — T4002 guide — canada.ca)_
- **Line 9281** — Motor vehicle — total of expenses × business %  _(CRA Form T2125 — canada.ca; CRA T4002 guide)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada -- Federal |
| Tax | Federal income tax on business income + CPP self-employed contributions |
| Currency | CAD only |
| Tax year | Calendar year (generally December 31; eligible individuals may elect a non-calendar fiscal period via Form T1139) |
| Primary legislation | Income Tax Act (ITA), R.S.C. 1985, c. 1 (5th Supp.) |
| Supporting legislation | Income Tax Regulations (ITR); Excise Tax Act (ETA) for GST/HST; CRA Guide T4002 |
| Tax authority | Canada Revenue Agency (CRA) |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Filing deadline | 15 June (self-employed), but tax owing due 30 April |
| Form | T2125 -- Statement of Business or Professional Activities |
| Contributor | Open Accountants Community |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |
| Skill version | 2.1; [version in frontmatter](https://github.com/openaccountants/openaccountants/blob/76e305ebf01c88beac728b387845fb83867b9828/skills/canada/ca-fed-t2125.md#L4) |

### Federal Tax Brackets (2025) [T1]

**Federal Tax Brackets (2025)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| Up to 57,375 | 14.5%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 57,375 through 114,750 | 20.5%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 114,750 through 177,882 | 26%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 177,882 through 253,414 | 29%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 253,414 | 33%; [2025 annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |

Provincial tax is additional. Each province has its own brackets. This skill covers federal only. **HOLD the old approximate 20%–54% range:** no country-wide extrema were verified. Bind province, income, credits, abatements and surtaxes before a combined-tax calculation. The 2025 lowest annual federal rate is 14.5%, distinct from the July/ongoing 14% rate.

### Basic Personal Amount (2025) [T1]

**Basic Personal Amount (2025)**

| Item | Amount (CAD) |
| --- | --- |
| Maximum basic personal amount, subject to actual residency/eligibility | $16,129 where 2025 line 23600 net income is $177,882 or less; [CRA BPA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html) |
| Minimum basic personal amount above the taper zone | $14,538 where 2025 line 23600 net income is $253,414 or more; [CRA BPA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html) |
| BPA clawback zone | Use actual line 23600 net income and worksheet between the thresholds; HOLD an individual result without those inputs. [CRA BPA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html) |

### CPP Self-Employed Contributions (2025) [T1]

**CPP Self-Employed Contributions (2025)**

| Item | Value |
| --- | --- |
| CPP rate (self-employed pay both portions) | 11.9% (2 x 5.95%) |
| CPP2 rate | 8% (2 x 4%) on earnings between first and second ceilings |
| First earnings ceiling | $71,300 |
| Second earnings ceiling | $81,200 |
| Basic exemption | $3,500 |
| Maximum CPP first tier (base plus first additional), excluding CPP2 | $8,068.20; [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) |
| Maximum CPP2 contribution | $792.00 |

For the ordinary full-year CPP self-employment case, line 22200 deducts half the **base** contribution plus all first and second additional self-employed contributions, not half of the whole payment. **HOLD employment overlap, Quebec, age/election and proration cases** until their actual Schedule 8 branch is established. CPP is not a T2125 expense. [2025 Schedule 8 Part 4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

### Key T2125 Thresholds [T1]

**Key T2125 Thresholds**

| Item | Value |
| --- | --- |
| GST/HST registration required | Over $30,000 in a single calendar quarter or over 4 consecutive quarters (person + associated persons) |
| CCA deduction | Discretionary -- any amount from $0 to the class maximum; unclaimed CCA stays in UCC |
| Instant asset write-off (legacy CEBA label) | HOLD that program label: the CCA sources do not verify it. Determine actual class, acquisition/availability regime and chosen deduction. [ITR 1100](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) |
| Business-use-of-home | Principal place of business OR exclusive income-earning use with regular and continuous client/customer/patient meetings; actual facts and loss limit required. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |

### Conservative Defaults [T1]

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown business-use % (vehicle, home, phone) | No claim without reasonable supporting records -- ask for the log |
| Unknown expense category | HOLD deduction/classification pending evidence; unknown is not a final finding of non-deductibility |
| Unknown CCA class | Do not depreciate -- ask |
| Unknown GST/HST status | HOLD status, timing and tax treatment; do not infer non-registration |
| Unknown whether expense is business or personal | HOLD pending business-purpose/use evidence; do not invent personal use |
| Unknown vehicle km split | No claim without a km log -- request it |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- bank statement for the full calendar year (January-December), confirmation of business activity and NAICS code.

Recommended -- all invoices issued, purchase receipts, vehicle km log, home office measurements, GST/HST returns filed, prior year T2125.

Ideal -- complete bookkeeping records, CCA schedule from prior year, motor vehicle log, T4 slips (if also employed), prior year Notice of Assessment.

### Refusal Catalogue

- **R-CA-1 -- Corporations** — Corporations file T2 corporate tax returns. This skill covers sole proprietors filing T2125 only.
- **R-CA-2 -- Partnerships** — Partnerships file T2125 at the partnership level with allocation to partners. Partnership-specific rules are out of scope.
- **R-CA-3 -- Non-residents** — Non-resident business income has different rules. Out of scope.
- **R-CA-4 -- SR&ED claims** — Scientific Research and Experimental Development tax credits require specialised review. Escalate.
- **R-CA-5 -- Farming/fishing income** — Farming (T2042) and fishing (T2121) have their own forms and special rules. Out of scope.

## Section 3 -- Transaction Pattern Library

These are candidate intake and matching patterns, not proof of income nature or deductibility. **HOLD final classification** until actual invoices, payees, business purpose/use, current-versus-capital treatment, tax method and form scope are established. The interest/dividend/rental/referral labels have not all been source-verified in this unit.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns (Credits on Bank Statement)**

| Pattern | T2125 Line | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT DEPOSIT, CLIENT PAYMENT, [client name] | Line 8299 (Gross revenue) | Business income | Core revenue |
| STRIPE PAYOUT, STRIPE TRANSFER | Line 8299 | Business income | Match to underlying invoices. Report gross (before Stripe fees). |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Line 8299 | Business income | Same -- report gross before fees |
| ETRANSFER [client name], INTERAC | Line 8299 | Business income | Common Canadian payment method |
| GST/HST REFUND, CRA GST REFUND | Check | May be income | GST/HST refund of ITCs: NOT income. Net income adjustment if previously expensed. |
| INTEREST, SAVINGS INTEREST | NOT T2125 | Interest income | Report on Line 12100, not T2125 |
| DIVIDEND | NOT T2125 | Dividend income | Report on Line 12000/12010 |
| EMPLOYMENT INCOME, SALARY | NOT T2125 | Employment income | T4 slip income |
| CRA REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund |
| RENTAL INCOME | NOT T2125 | Rental | Report on T776 |
| OWN TRANSFER, SAVINGS TRANSFER | EXCLUDE | Internal | Between own accounts |

### 3.2 Expense Patterns (Debits on Bank Statement)

**Expense Patterns (Debits on Bank Statement)**

| Pattern | T2125 Line | Tier | Treatment |
| --- | --- | --- | --- |
| RENT, OFFICE RENT, COMMERCIAL LEASE | Line 8910 (Rent) | T1 | Fully deductible if business premises |
| PROPERTY TAX (business premises) | Line 9180 (Property taxes) | T1 | Confirm actual business-property/current expense treatment; home-office allocation belongs in its separate computation. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| HYDRO, ELECTRICITY, GAS, ENBRIDGE, HYDRO ONE | Line 9220 (Utilities) | T2 | If home: business-use % only. If office: fully deductible. |
| BELL, ROGERS, TELUS, SHAW | Line 9220 (Telephone/utilities) | T2 | Business portion only |
| INTERNET, WIFI | Line 9220 | T2 | Business portion only |
| INSURANCE, BUSINESS INSURANCE, LIABILITY | Line 8690 (Insurance) | T1 | Fully deductible if business insurance |
| ACCOUNTING, BOOKKEEPER, CPA | Line 8860 (Professional fees) | T1 | Fully deductible |
| LAWYER, LEGAL FEE | Line 8860 | T1 | Deductible if business-related |
| OFFICE SUPPLIES, STAPLES, GRAND & TOY | Line 8811 (Office stationery and supplies) where that nature is established; 8810 is office expenses | T1 | Merchant name alone does not establish the category or deduction. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| BANK FEE, MONTHLY FEE, NSF | Line 8710 (Interest and bank charges) | T1 | Fully deductible for business account |
| STRIPE FEE, PAYPAL FEE, SQUARE FEE | Line 8710 | T1 | Payment processing fees: fully deductible |
| INTEREST (business loan) | Line 8710 | T1 | Fully deductible |
| ADVERTISING, GOOGLE ADS, META ADS, FACEBOOK | Line 8521 (Advertising) | T1 | Fully deductible |
| MEALS (client entertainment) | Line 8523 (Meals and entertainment) | T1 | Ordinary 50% limit, subject to actual statutory exceptions and expense evidence. [CRA meals](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html) |
| MEALS (business travel, alone) | Line 8523 | T1 | Ordinary 50% limit where eligible; actual exceptions/tax treatment require facts. [CRA meals](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html) |
| SOFTWARE, SUBSCRIPTION, SAAS | Line 8810 or 8860 | T1 | Fully deductible |
| TRAINING, COURSE, CONFERENCE | Line 9270 (Other expenses) | T1 | Fully deductible if business-related |
| GAS, FUEL, PETRO-CANADA, SHELL, ESSO | Motor vehicle expenses | T2 | Business km / total km. Keep a log. |
| CAR INSURANCE, AUTO INSURANCE | Motor vehicle expenses | T2 | Business km proportion only |
| CAR REPAIR, SERVICE, OIL CHANGE | Motor vehicle expenses | T2 | Business km proportion only |
| PARKING (business) | Motor vehicle or travel | T1 | Fully deductible if business purpose |
| CRA INCOME TAX, TAX INSTALMENT | EXCLUDE | Not deductible | Income tax is not a business expense |
| CRA GST PAYMENT, GST REMITTANCE | HOLD actual tax-method adjustment | T2 | Do not infer ordinary expense or apply universal net-of-GST treatment from the debit. Bind the actual Part 3/method sequence. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| CPP CONTRIBUTION | EXCLUDE from T2125 | T1 | Personal line 22200 uses half base plus all first/second additional CPP in the applicable self-employment branch. [Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) |
| PERSONAL, GROCERY, AMAZON (personal) | EXCLUDE | Not deductible | Personal expenses |
| COMPUTER, LAPTOP, EQUIPMENT (legacy $500 shortcut) | HOLD capital/current and class determination | T1 | $500 is a specific small-tool class boundary, not a universal capitalisation test. See 5.4/6.4. [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| MEMBERSHIP, DUES, PROFESSIONAL BODY | Line 8760 covers business taxes/licences/memberships; management/admin is 8871 | T1 | Bind actual expense nature and allowability; do not call 8760 management fees. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| SUBCONTRACTOR, CONTRACTOR PAYMENT | Line 8360 (Subcontracts) and 8340 (direct wage costs) are both in Part 3D cost of goods sold, for business income only | T2 | HOLD the branch/line for a professional-income filer; confirm allowable expense and actual business/professional branch. T4A fees threshold concerns calendar-year total over $500, with actual exceptions/form type. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf); [CRA fees reporting](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/reporting-fees-for-service/fact-sheet-reporting-fees-services.html) |

### 3.3 SaaS Subscriptions

**SaaS Subscriptions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Line 8810/8860 -- fully deductible | Operating expense |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Line 8810/8860 -- fully deductible | Same |
| AWS, HEROKU, DIGITAL OCEAN | Line 8810 -- fully deductible | Hosting costs |
| QUICKBOOKS, XERO, FRESHBOOKS, WAVE | Line 8860 -- fully deductible | Accounting software |

### 3.4 Internal Transfers and Exclusions

**Internal Transfers and Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, SAVINGS, TFSA, RRSP | EXCLUDE | Not business transaction |
| MORTGAGE, RENT (personal) | EXCLUDE (or home office %) | Personal. Home office portion in business-use-of-home. |
| ATM, CASH WITHDRAWAL | T2 -- ask | Default exclude |
| DONATION, CHARITY | EXCLUDE from T2125 | Personal tax credit, not business expense |

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Proprietor (Web Developer)

Input: Gross revenue CAD 95,000. Not GST registered (under $30K threshold last year, now over -- registration timing and GST-adjusted amounts held below). Expenses: home office (see below), software CAD 2,400, accounting CAD 1,500, subcontractor CAD 8,000, travel CAD 3,000, meals (50%) CAD 1,200 (deductible: CAD 600).

Home office: 1,200 sq ft house, 150 sq ft office (12.5%). Mortgage interest CAD 8,000, property tax CAD 4,000, utilities CAD 3,600, insurance CAD 1,800. Total: CAD 17,400 x 12.5% = CAD 2,175.

Assume eligible home/expense inputs, full-year CPP-only self-employment, no employment contributions, no Quebec, election or proration exception. **HOLD actual GST registration date and GST-adjusted income:** annual revenue alone does not supply quarter/supply dates, taxability or actual tax treatment. The following is conditional arithmetic, not a final return.

Computation:
- Revenue: CAD 95,000
- Combined cost deductions: 2,400 + 1,500 + 8,000 + 3,000 + 600 + 2,175 = CAD 17,675. For a business filer, place the CAD 8,000 subcontract cost in Part 3D/A6b, not again in Part 4/B13; home costs remain in their separate deduction. This grouped arithmetic does not assign all costs to one form part.
- Net business income: CAD 77,325
- Base CPP: (71,300 − 3,500) × 9.9% = CAD 6,712.20
- First additional CPP: 67,800 × 2% = CAD 1,356
- Second additional CPP: (77,325 − 71,300) × 8% = CAD 482
- Total CPP payable: **CAD 8,550.20**, including CPP2; CAD 8,068.20 covers only the first tier
- Separate line 22200 deduction: 6,712.20 / 2 + 1,356 + 482 = **CAD 5,194.10**, not half the total. [Schedule 8 Part 4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf)

### Example 2 -- Vehicle (Km-Based Apportionment)

Input: Total km driven: 25,000. Business km: 15,000 (60%). Vehicle costs: gas CAD 3,600, insurance CAD 2,400, repairs CAD 800, licence CAD 120. Car cost CAD 36,000 (Class 10).

Computation:
- Operating costs: (3,600 + 2,400 + 800 + 120) x 60% = CAD 4,152
- Full-rate CCA arithmetic: CAD 36,000 × 30% × 60% = CAD 6,480. Eligible 2025 RIIP at 1.5 times the full-rate base can give CAD 9,720; this is not 1.5 times an ordinary half-year deduction. **HOLD actual CCA** pending acquisition/available-for-use dates, regime, pool history and chosen amount. [ITR 1100](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html); [1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html)
- Total vehicle deduction: CAD 4,152 + CCA amount

### Example 3 -- Meals (50% Rule)

Input: CAD 2,500 in restaurant receipts for client meetings.

For this ordinary eligible scenario, assume CAD 2,500 is the relevant business cost after required GST/HST treatment and no exception applies. Allowable CAD 1,250 goes on line 8523; keep gross CAD 2,500 and the disallowance in the workpaper. Do not put the gross amount on the allowable-only line and add it back again. Other statutory exceptions and qualified long-haul rules remain separate. [CRA line 8523](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html)

### Example 4 -- CCA on Computer Equipment

Input: Laptop purchased for CAD 2,800. Class 50 (55% rate). First year.

Arithmetic only: 1.5 × 55% × CAD 2,800 = CAD 2,310, leaving CAD 490 if that deduction and no other pool adjustments apply. This is not a certified maximum or actual claim. Eligible 2025 Class 50 property can have a 100% first-year maximum under the enacted factors; a lower discretionary amount is not inherently unlawful. **HOLD classification, business use, acquisition/availability, eligibility, pool and chosen deduction** before using either result. [ITR 1100(2)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html); [1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html)

These checks recompute the original cases under their stated conditions. They do not bind actual GST timing, expense eligibility, CPP coverage or an enhanced CCA entitlement.

```oa-check
name: Original 2025 sole-proprietor case, full-year CPP conditions assumed
inputs:
  revenue: 95000
  software: 2400
  accounting: 1500
  subcontracts: 8000
  travel: 3000
  meals_cost: 1200
  home_interest: 8000
  home_property_tax: 4000
  home_utilities: 3600
  home_insurance: 1800
  business_area: 150
  total_area: 1200
  first_ceiling: 71300
  second_ceiling: 81200
  exemption: 3500
steps:
  - area_share: business_area / total_area
  - home_costs: home_interest + home_property_tax + home_utilities + home_insurance
  - home_claim: home_costs * area_share
  - ordinary_meals: meals_cost * 0.5
  - expenses_before_home: software + accounting + subcontracts + travel + ordinary_meals
  - total_expenses: expenses_before_home + home_claim
  - net_business_income: revenue - total_expenses
  - first_band: max(0, min(net_business_income, first_ceiling) - exemption)
  - base_cpp: first_band * 0.099
  - first_additional_cpp: first_band * 0.02
  - second_additional_cpp: max(0, min(net_business_income, second_ceiling) - first_ceiling) * 0.08
  - total_cpp: base_cpp + first_additional_cpp + second_additional_cpp
  - line_22200: base_cpp / 2 + first_additional_cpp + second_additional_cpp
expected:
  area_share: 0.125
  home_costs: 17400
  home_claim: 2175
  ordinary_meals: 600
  expenses_before_home: 15500
  total_expenses: 17675
  net_business_income: 77325
  first_band: 67800
  base_cpp: 6712.20
  first_additional_cpp: 1356
  second_additional_cpp: 482
  total_cpp: 8550.20
  line_22200: 5194.10
```

```oa-check
name: Original vehicle arithmetic, actual CCA regime held
inputs:
  total_km: 25000
  business_km: 15000
  fuel: 3600
  insurance: 2400
  repairs: 800
  vehicle_licence_cost: 120
  vehicle_cost: 36000
steps:
  - business_share: business_km / total_km
  - operating_costs: fuel + insurance + repairs + vehicle_licence_cost
  - business_operating_costs: operating_costs * business_share
  - full_rate_cca_arithmetic: vehicle_cost * 0.30 * business_share
  - conditional_enhanced_arithmetic: full_rate_cca_arithmetic * 1.5
expected:
  business_share: 0.6
  operating_costs: 6920
  business_operating_costs: 4152
  full_rate_cca_arithmetic: 6480
  conditional_enhanced_arithmetic: 9720
```

```oa-check
name: Original ordinary eligible meals case, no exception or further tax adjustment
inputs:
  relevant_meals_cost: 2500
steps:
  - allowable_line_8523: relevant_meals_cost * 0.5
expected:
  allowable_line_8523: 1250
```

```oa-check
name: Original laptop arithmetic, maximum and actual CCA entitlement held
inputs:
  cost: 2800
steps:
  - illustrative_deduction: cost * 0.55 * 1.5
  - residual_without_other_adjustments: cost - illustrative_deduction
expected:
  illustrative_deduction: 2310
  residual_without_other_adjustments: 490
```

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income [T1]

- **Business income** — Use the actual Part 3 sales/fees adjustment, other income and method-specific sequence to reach line 8299. Ordinary recoverable-tax treatment and Quick Method rules are different; HOLD unknown registration, timing, method or adjustments rather than subtracting tax twice. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)

### 5.2 Deductible Expenses [T1]

- **Deductible expenses** — Must be incurred to earn business income. Must be reasonable (s67). Personal or living expenses are not deductible (s18(1)(h)).  _(ITA s18)_

### 5.3 Meals and Entertainment [T1]

- **Meals and entertainment** — Ordinary limit 50%; qualifying long-haul meals 80%, with other statutory exceptions. **HOLD the allowed amount** until actual business/qualification/exception facts and tax treatment are established. [CRA allowable-part rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html)

### 5.4 Capital Cost Allowance (CCA) [T1]

**CCA Classes**  _(ITA s20(1)(a); ITR Schedule II)_

| Class | Base rate | Asset scope and required checks | Primary source |
| --- | --- | --- | --- |
| 1 | 4% | Building base rate; the old March 2007 description is not a universal class cutoff. HOLD actual class, acquisition facts and additional-allowance/election conditions | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 8 | 20% | Furniture/fixtures/equipment where the actual class definition fits; do not classify by merchant alone | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 10 | 30% | Actual vehicle/class conditions; the passenger limit is $38,000 before tax for 2025, with applicable tax adjustments. The separately dated 2026 announcement says $39,000; it does not relabel a 2025 acquisition | [2025 regulation](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html); [2026 announcement](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html) |
| 10.1 | 30% | 2025 passenger classification/cost threshold $38,000 before tax, not $37,000; actual vehicle/year/tax adjustments required | [2025 regulation](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html) |
| 12 | 100% | Qualifying small tools/software/cutlery and actual class conditions; no universal capital/current $500 test | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 43 | 30% | HOLD actual manufacturing-equipment class/year; Classes 29/53 exclusions matter, so not every 2025 addition belongs here | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 50 | 55% | Qualifying general processing hardware/systems software; HOLD network-infrastructure or other item classification rather than treating all data-network equipment alike | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 54 | 30% | Qualifying zero-emission passenger property; $61,000 stated cap has vehicle/year/tax conditions, not automatic entitlement | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html); [dated limit](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html) |
| 55 | 40% | Corresponds to qualifying ordinary Class 16 property; not every zero-emission vehicle outside Class 54. HOLD actual definition/year/availability | [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |

- **Passenger vehicle cost limit (2025)** — $38,000 before tax, with actual acquisition-year, vehicle and applicable tax adjustments. [Operative amendment](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html).
- **AccII and RIIP** — The original incentive's 1.5 factor applies to the full-rate net-addition base in its applicable stage, not 1.5 times an ordinary half-year deduction; that can triple the ordinary half-year amount. Current law separates pre-2025 AIIP from post-2024 RIIP with availability cutoffs and class/phase-out exceptions. **HOLD actual enhancement** until acquisition/available-for-use, eligible property, class and pool facts are bound. Class 50 may have different factors. [ITR 1100(2)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html); [1104 definitions](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html); [CRA original incentive](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/accelerated-investment-incentive.html).

### 5.5 Business-Use-of-Home [T1/T2]

**Business-Use-of-Home Conditions**  _(ITA s18(12))_

| Condition | Eligibility |
| --- | --- |
| Principal place of business | Eligibility route only; actual use, expenses and loss limit required. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |
| Exclusive income-earning use plus regular and continuous client/customer/patient meetings | Eligibility route only; actual use, expenses and loss limit required. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |
| Neither condition met | NO deduction |

- **Deductible home expenses** — Bind actual eligible rent/mortgage interest, property tax, utilities, insurance and maintenance, reasonable area and any relevant time/use allocation. An area fraction alone does not certify every bill. HOLD actual amount until the applicable 18(12)/Part 7 conditions and loss restriction are met. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html); [form Part 7](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)
- **Loss restriction** — Cannot create or increase a business loss. Excess carried forward to the next year.

### 5.6 Filing Deadlines [T1]

**Filing Deadlines**

| Item | Deadline |
| --- | --- |
| T1 filing (self-employed) | Ordinary 2025 return: 15 June 2026, subject to actual exceptions/holiday rules. [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) |
| Tax payment due | Ordinary 2025 balance: 30 April 2026; the self-employed filing date does not defer payment. [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) |
| Quarterly instalments | Where the actual ordinary obligation exists, nominal dates 15 March/June/September/December with weekend/holiday handling; not every self-employed person owes instalments. [CRA instalment dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) |
| T4A issuance (subcontractors) | Last day of February |
| GST/HST annual return | The 15 June filing/30 April payment route requires a sole proprietor with December 31 fiscal year-end and business income. Other annual cases differ; HOLD the date until the actual filer/period is bound. [CRA deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |

### 5.7 Penalties [T1]

**Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing | 5% of balance owing + 1% per month late (max 12 months) |
| Repeated late filing | 10% + 2% per complete month, maximum 20 months, only with the statutory demand and prior qualifying-penalty conditions; a repeat event alone is insufficient. HOLD actual liability. [ITA 162(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) |
| Late instalment | Instalment interest at prescribed rate |
| Knowing/grossly negligent false statement or omission | Apply the actual 163(2) tax/credit-base computation and liability conditions; $100 minimum and 50% statutory limb, not an unrestricted flat formula for every error. HOLD actual assessment. [ITA 163(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

- **Home office review** — Confirm principal place of business OR exclusive income-earning use with regular and continuous client/customer/patient meetings, actual area/time use and eligible costs. Apply the no-loss limit and actual carryforward rules. HOLD unclear inputs; measurements alone do not establish eligibility. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html); [form Part 7](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)

### 6.2 Motor Vehicle [T2]

- **Motor vehicle review** — Establish the required business/total-distance and use evidence under the actual applicable record/log method. HOLD a percentage without those records; missing records do not establish zero actual business use. The old audit-frequency assertion has not been verified. Confirm the evidence and reasonable percentage before final use.

### 6.3 Reasonableness (s67) [T2]

- **Reasonableness review** — All expenses must be "reasonable in the circumstances." CRA can deny excessive expenses even if legitimately incurred. Flag any single expense that appears disproportionate.  _(s67)_

### 6.4 CCA vs Expense [T2]

- **CCA vs expense determination** — HOLD actual capital/current and class determination: price, useful life or a merchant/product label alone does not settle it. Preserve the distinct subscription, perpetual-licence, hardware and network-equipment investigations; actual terms, asset nature and class exclusions matter. Do not automatically classify every perpetual licence as Class 12 or every hardware item as Class 50. [CRA class scope](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html)

## Section 7 -- Excel Working Paper Template

T2125 WORKING PAPER -- Tax Year 2025

A. GROSS INCOME
  A1. Raw sales/fees before Part 3 tax adjustments ___________
  A2. Actual method-specific Part 3 adjustments    ___________
  A3. Adjusted sales/fees under Part 3A or 3B       ___________
  A4. Other business income / actual Part 3C items ___________
  A5. Gross business/professional income, 8299     ___________
      HOLD if tax has already been removed; no duplicate subtraction
  A6. Part 3D cost of goods sold (business income only)
      A6a. Direct wage costs (8340)                ___________
      A6b. Subcontracts (8360)                     ___________
      A6c. Other Part 3D inputs: opening inventory,
           purchases and other costs              ___________
      A6d. Total costs less closing inventory
           gives cost of goods sold (8518)         ___________
  A7. Gross profit (8519) = A5 - A6d for business;
      use A5 for professional income without 3D   ___________

B. OPERATING EXPENSES (Part 4, CCA shown separately in D)
  B1. Advertising (8521)                           ___________
  B2. Allowable meals/entertainment (8523)         ___________
  B3. Subcontracts memo: included in A6b only;
      excluded from B13. HOLD professional branch ___________
  B4. Insurance (8690)                             ___________
  B5. Interest and bank charges (8710)             ___________
  B6. Management and admin (8871)                  ___________
  B7. Office expenses (8810)                       ___________
  B7a. Office stationery/supplies (8811)           ___________
  B7b. Direct business-property taxes (9180)       ___________
  B8. Professional fees (8860)                     ___________
  B9. Rent (8910)                                  ___________
  B10. Telephone and utilities (9220)              ___________
  B11. Travel (9200)                               ___________
  B12. Other expenses (9270) and remaining Part 4
       lines, itemised separately; no CCA/COGS/home ___________
  B13. Total operating expenses excluding CCA/home
       and the A6 cost-of-goods-sold amounts       ___________

C. NET INCOME BEFORE CCA AND HOME OFFICE
  C1. A7 - B13 (before CCA; C1 - D5 is 9369)        ___________

D. CCA
  D1. Class 8 (20%)                                ___________
  D2. Class 10/10.1 (30%)                          ___________
  D3. Class 50 (55%)                               ___________
  D4. Other classes                                ___________
  D5. Total CCA                                    ___________

E. BUSINESS-USE-OF-HOME
  E1. Business area %                              ___________
  E2. Total home costs                             ___________
  E3. Actual eligible use/time allocation, loss limit
      and carryforward under Part 7 / 18(12)       ___________

F. NET SOLE-PROPRIETOR INCOME (C1 - D5 - E3)       ___________
   Reconcile Part 4 total expenses 9368 to B13 + D5.
   This assumes no Part 5 partnership adjustments;
   HOLD other branches and reconcile actual 5D/9945/9946.

REVIEWER FLAGS:
  [ ] Vehicle km log available?
  [ ] Home office eligibility confirmed?
  [ ] CCA schedule reconciled from prior year?
  [ ] Ordinary meals limit or actual exception established?
  [ ] All T2 items flagged?

## Section 8 -- Bank Statement Reading Guide

### Canadian Bank Statement Formats

These are illustrative intake formats and fields, not a verified fixed schema for each bank. HOLD parser assumptions until the actual export, currency, direction, transfers and reconciliation are checked. They are not statutory tax evidence.

**Canadian Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| RBC, TD, BMO, Scotiabank, CIBC | CSV, PDF | Date, Description, Debit, Credit, Balance |
| Desjardins | CSV | Date, Description, Withdrawal, Deposit |
| Tangerine, Simplii, EQ Bank | CSV | Date, Transaction, Amount |
| Wise, Revolut | CSV | Date, Description, Amount, Currency |

### Key Canadian Banking Terms

**Key Canadian Banking Terms**

| Term | Classification Hint |
| --- | --- |
| e-Transfer / Interac | Very common -- check direction and counterparty |
| PAD (Pre-Authorized Debit) | Regular expense |
| POS | Point-of-sale purchase |
| Direct Deposit | Could be income or employment |
| NSF | Non-sufficient funds fee -- bank charge |
| Service Charge | Monthly bank fee |

## Section 9 -- Onboarding Fallback

ONBOARDING QUESTIONS -- CANADA T2125
1. What is your business name and NAICS code?
2. Do you have a Business Number (BN)?
3. Are you GST/HST registered?
4. Do you work from home? Is it your principal place of business?
5. Do you use a vehicle for business? Do you have a km log?
6. Any capital purchases this year? (computers, equipment, vehicles)
7. Do you have subcontractors you paid over $500?
8. Are you also employed (T4 income)?
9. Province of residence?
10. Prior year T2125 / CCA schedule available?

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Business income | ITA s9 |
| Deductible expenses | ITA s18 |
| Reasonableness | ITA s67 |
| Meals 50% limit | ITA s67.1 |
| CCA | ITA s20(1)(a); ITR Schedule II |
| Motor vehicle limits | ITA s67.2, s67.3; ITR 7307 |
| Business-use-of-home | ITA s18(12) |
| CPP self-employed | CPP Act s10, s12 |
| Filing deadlines | ITA s150(1) |
| Penalties | ITA s162, s163 |
| GST/HST | ETA Part IX |

### Interaction with GST/HST [T1]

**Interaction with GST/HST**

| Scenario | Income Tax Treatment |
| --- | --- |
| GST/HST sales treatment | Ordinary method: apply actual tax-removal adjustments before the form sequence reaches 8299. Both ordinary and Quick Method filers use Part 3A for business or Part 3B for professional income, then Part 3C. The Quick Method government-assistance calculation sits inside the selected 3A/3B branch; HOLD actual election, eligible sales and remittance-rate application. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| Ordinary recoverable ITCs | Remove recoverable tax from the ordinary expense cost; no duplicate recovery. Quick Method expense rules are separate. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| Actual non-registrant | Non-recoverable GST/HST can be part of the appropriate cost, subject to expense/capital/use rules; unknown status is not proof of non-registration. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| Non-recoverable tax | Apply the actual business-use/expense/capital rules; personal-use tax is not converted into a deductible business expense. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |
| Quick Method expenses | Include GST/HST as instructed for that method; do not apply a universal registrant net-of-tax rule. Bind the actual election, expense and Part 3 treatment. [2025 form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) |

## Sources

Completed 21 November reads are reused for this unchanged historical 2025 baseline. Source scopes below do not certify every individual expense, classification, registered status or enhanced CCA outcome. The form and some CRA pages retain proposal wording; the operative consolidation and Parliament's enactment record were checked separately. A stale proposal label does not establish that relief was unlegislated.

| Primary source | Completed read scope | Read date |
| --- | --- | --- |
| [ETA 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html), [CRA registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) | Subsections (1)-(2), actual threshold population/exclusions and CRA crossing/timing footnotes; annual revenue alone does not bind the example's registration date | 2026-11-21 |
| [CRA 2025 tax table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) | Annual table and transition footnote: “making the tax rate 14.5% for 2025”. Ongoing 14% is not substituted for the annual rate | 2026-11-21 |
| [CRA basic personal amount](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30000-basic-personal-amount.html) | 2025 federal amount/taper paragraph and line 23600 net-income basis; actual residency/claim still required | 2026-11-21 |
| [Schedule 8 landing page](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s8.html), [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) | Pages 1, 3, 6-7: scope/proration and Part 4 self-employment base, additional contributions and line 22200. Not a full employment-overlap/QPP/election computation | 2026-11-21 |
| [ITA 18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | Subsection (12)(a)-(c) completely read: home qualification, no-loss restriction and carryforward; area alone does not establish individual entitlement | 2026-11-21 |
| [T2125 landing page](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2125.html), [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf), [CRA expense list](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) | All nine form pages read in memory on 21 November. Bounded 25 November re-read of pages 2-4 resolves 3A/3B Quick Method branches, business-only 3D 8340/8360, 8518/8519 to Part 4, Part 5/home sequence. Exact captions: “Part 3B – Professional income”; “Subcontracts”. No bank merchant or actual expense certified | 2026-11-21; bounded follow-up 2026-11-25 |
| [ITR 1100](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) | Complete subsection (2) formula including A/A.1, B/B.1, C and Class 50 factor 9/11; base-rate evidence read separately. Actual eligibility/pool remains held | 2026-11-21 |
| [ITR 1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html), [Parliament C-15 record](https://www.parl.ca/legisinfo/en/bill/45-1/c-15) | Subsection (4.01) post-2024 acquisition, availability and eligibility conditions; Parliament record of royal assent on 26 March 2026. No new case is assumed eligible from the heading alone | 2026-11-21 |
| [2025 vehicle regulation](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html) | Prescribed $38,000 amendment, its 2025 applicability and explanatory text | 2026-11-21 |
| [Finance 2026 vehicle announcement](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html) | Dated 2026 limits and unchanged zero-emission cap; an official announcement, not a relabelled 2025 rule or complete vehicle-qualification review | 2026-11-21 |
| [CRA depreciable-property classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) | Relevant Classes 1/8/10/10.1/12/43/50/54/55 sections, exclusions and elections; class-specific dates and asset definitions remain essential | 2026-11-21 |
| [CRA accelerated incentive](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/accelerated-investment-incentive.html) | Original incentive structure and phase-out; enacted consolidation controls current cutoffs/factors | 2026-11-21 |
| [CRA individual dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html), [CRA instalment dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) | Completed 2025 return/payment dates in 2026 and nominal instalment/weekend handling reused from the completed instalment work; no universal instalment duty | 2026-11-21 |
| [CRA GST/HST deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) | Annual deadline criteria and exceptions; actual filer/period/payment route required | 2026-11-21 |
| [CRA fees-for-services reporting](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/reporting-fees-for-service/fact-sheet-reporting-fees-services.html) | Calendar reporting/threshold and nominal February distribution deadline; actual exclusions, tax treatment and form type still need binding | 2026-11-21 |
| [ITA 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) | Subsections (1)-(2), ordinary and demand/prior-penalty repeat conditions; not a second-time-only test | 2026-11-21 |
| [ITA 163](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html) | Subsection (2) liability/minimum and conditions; not foreign-return subsection (2.4), and not a complete individual assessment | 2026-11-21 |
| [CRA allowable meals amount](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html), [ITA 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) | Allowable part, exceptions and qualified long-haul treatment; subsections (1), (1.1), (2). Exact instruction: “calculate the allowable part you can claim for business use” | 2026-11-21 |
| [ITA 249.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html), [T1139](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1139.html) | Subsections (1), (4)-(5) and actual alternative-method applicability; not an automatic option for every business | 2026-11-21 |

**Not yet confirmed:** actual registration/supply timing and GST-adjusted revenue, Quick Method income/expense application, actual expense evidence and classification, the national combined-rate range, individual CPP coverage/overlap/election/proration, vehicle/class/acquisition/availability/pool and chosen CCA, laptop enhancement maximum/entitlement in the original case, home use/time/cost/loss/carryforward inputs, actual filing/penalty/relief conditions, every bank-pattern income/form referral or export schema, and the audit-frequency/legacy CEBA claims. These holds prevent final use of the affected conclusions; the conditional example arithmetic is not a filing result.

## PROHIBITIONS

- NEVER allow personal or living expenses as business deductions
- NEVER treat the ordinary 50% meals limit as universal; bind qualified long-haul and other statutory exceptions
- NEVER claim CCA without a prior-year UCC reconciliation
- NEVER claim home office if neither principal-place-of-business nor exclusive-use test is met
- NEVER allow home office to create or increase a business loss
- NEVER finalize a vehicle deduction without the actual required records and applicable log method
- NEVER exceed the passenger vehicle cost limit for CCA
- NEVER include income tax payments as business expenses
- NEVER include CPP as a T2125 expense; use the actual Schedule 8 base/additional split for line 22200
- NEVER apply the ordinary net-of-recoverable-tax shortcut universally to Quick Method income or expenses; follow the actual form method
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
