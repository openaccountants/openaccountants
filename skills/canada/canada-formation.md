---
name: canada-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Canada. Trigger on phrases like "set up a company in Canada", "Canadian incorporation", "Corporations Canada", "federal incorporation", "provincial incorporation", "CBCA", "Ontario corporation", "BC incorporation", "Inc. Canada", "Canadian company formation", "register a business Canada", or any question about starting a business entity in Canada. Covers federal vs provincial incorporation, entity types, registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Canadian company formation.
version: 1.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: Historical 2025 formation workpaper; separately dated 2026 fees, access routes and source checks do not recertify the entire skill for the current year.
last_updated: 2026-11-25
depends_on:
  - company-formation-workflow-base
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: formation
---

# Canada Formation

## Canada Company Formation Skill v1.1

This corrects a historical 2025 formation workpaper. **HOLD** blocks final use of an affected fee, eligibility, legal consequence, registration date or planning outcome until its actual source, period and conditions are established. A missing fee or condition is not zero cost or permission to trade. Fee examples below distinguish dated sources and arithmetic from universal price guarantees.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
That historical attribution does not approve this proposed correction. Unresolved statutory, source and input conditions are explicitly held below.

### Formation

- **Corporations Canada fee — online** — $200  _(Corporations Canada — corporationscanada.ic.gc.ca)_
- **Express service** — Federal surcharge $100; four-business-hour online service standard, not guaranteed elapsed completion. [Schedule 5](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [service standards](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times).
- **Processing time** — Federal online one-business-day service standard; bind completeness, actual business days and exceptions. [registrar standard](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times).
- **Annual return** — Federal $12 online / $40 by other means; ordinary 60-day anniversary rule covers incorporation, amalgamation or continuance and excludes the initial event year. [Schedule 5 item 1(k)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [registry rule](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act).
- **Director residency** — Ordinary CBCA rule: at least 25% resident Canadians, but at least one if fewer than four directors, not a majority. Special-sector/ownership rules in 105(3.1)-(4) are separate. [CBCA 105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html).
- **Min share capital** — HOLD a nationwide or all-province minimum-capital claim. Federal share issue requires fully paid fair-equivalent consideration; no zero-minimum inference permits unpaid issuance. [CBCA 25](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-25.html).
- **Ontario** — $300  _(ServiceOntario — Ontario Business Registry)_
- **British Columbia** — $350  _(BC Registry Services — bcregistry.gov.bc.ca)_
- **Alberta** — HOLD the old $283.25 amount: no operative fee row was read. Official instructions require government fee plus service-provider charge; do not substitute a commercial quote. [official process](https://www.alberta.ca/incorporate-alberta-corporation).
- **Quebec** — Dated 2025 incorporation fee $389; the current table read on 21 November 2026 states $397. These are different fee periods, not a proven wrong current fee. [2025 schedule, page 5](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/emploi-solidarite-sociale/registraire_entreprises/RE-101-T_REQ_Fees_Terms_Payment_2025.pdf); [current table](https://www.quebec.ca/entreprises-et-travailleurs-autonomes/tarifs-registraire-entreprises/societe-par-actions).
- **Requirement** — Federal corp must register in each province of business  _(CBCA s.15; provincial equivalent legislation)_
- **Fee range** — No universal $520 maximum: the read ordinary NL share-capital extra-provincial registration fee is $560. Ontario initial return $0 and BC Form 33 $350 are distinct cases, with actual category/name/service charges required. [NL item 9(a)](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf); [Ontario fees](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit); [BC fees](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry).
- **CRA Business Number** — Federal incorporation automatically supplies BN/RC; reuse the existing BN for applicable additional accounts. Current BRO access/entity/Quebec exceptions matter; import/export RM registration is through CBSA/CARM. [CRA federal BN/RC](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts/corporation-income-tax.html); [RM route](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/how-register/bn-import-export.html).
- **GST/HST registration** — Ordinary $30,000 small-supplier amount; bind worldwide taxable supplies/associates/exclusions and the single-quarter versus cumulative-quarter effective-date and application branches. HOLD actual registration date until those inputs are known. [CRA timing table and footnotes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html).
- **Corporate tax payment** — 2 months after year-end; 3 months only for a corporation that was a CCPC throughout the year, claimed the small business deduction (current or prior year), and whose associated-group prior-year taxable income did not exceed the business limit  _(ITA s.157(1); CRA — Corporate payments — canada.ca)_
- **Foreign ownership restrictions** — HOLD actual Investment Canada Act, sector, notification/security and ownership conditions; no operative complete review of these laws was read. Do not infer that a small or new business has no obligation.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD |
| Company registrar (federal) | Corporations Canada (ISED) -- corporationscanada.ic.gc.ca |
| Company registrar (provincial) | Varies by province (e.g., Ontario: ServiceOntario; BC: BC Registry Services; QC: Registraire des entreprises) |
| Key legislation | Canada Business Corporations Act (CBCA) -- federal; provincial equivalents (OBCA, BCBCA, etc.) |
| Typical formation time | Federal online one-business-day service standard only; provincial/bank/planning durations are held below. [registrar standard](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times) |
| Corporate tax rate | Federal general net rate 15%; HOLD actual provincial/year/eligibility calculation and business limit. The old combined examples are retained as non-universal holds under Sources. [CRA corporation rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) |
| Skill version | 1.1; [version in frontmatter](https://github.com/openaccountants/openaccountants/blob/874ec958a2102b09002571476de1cfc983443d64/skills/canada/canada-formation.md#L4) |

## Section 2 -- Entity Types Comparison

HOLD the broad provincial/entity/personality/liability/tax/name-protection comparison until the actual governing law and entity facts are bound. Federal CBCA evidence below does not verify all partnership, cooperative or provincial rules. Treat unverified cells as research topics, not formation advice.

**Entity Types Comparison**

| Feature | Sole Proprietorship | Partnership (GP/LP) | Federal Corporation (CBCA) | Provincial Corporation | Cooperative |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No (GP) / LP has some | Yes | Yes | Yes |
| Liability | Unlimited | GP: Unlimited; LP: Limited for limited partners | Limited | Limited | Limited |
| Min. founders | HOLD provincial rule | HOLD partnership rule | One or more eligible incorporators under 5; directors under 102 are a separate test, ordinarily at least one but distributing corporations require at least three with at least two who are neither officers nor employees of the corporation or an affiliate. HOLD share issuance/organization. [5](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-5.html); [102](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-102.html) | HOLD actual province | HOLD actual Act |
| Min. share capital | HOLD actual form | HOLD actual form | HOLD minimum/issuance result; fully paid consideration is required before federal share issue. [25](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-25.html) | HOLD actual province | HOLD actual Act |
| Jurisdiction | Province of residence | Province | Canada-wide (right to carry on business nationally) | Province of incorporation (must extra-provincially register elsewhere) | Federal or provincial |
| Tax treatment | Personal | Partners taxed individually | Corporate | Corporate | Corporate (special rules) |
| Name protection | Province only | Province only | Canada-wide | Province only | Varies |

**Federal vs Provincial Incorporation -- Key Decision**

| Factor | Federal (CBCA) | Provincial |
| --- | --- | --- |
| Name protection | Canada-wide | Province only |
| Right to operate | All provinces (must extra-provincially register) | Province of incorporation (must extra-provincially register in others) |
| Annual filing | Federal anniversary return plus actual applicable provincial obligations; nationwide annual rules not all read. [federal rule](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act) | HOLD actual provincial obligations; not every obligation is the same return |
| Cost | $200 + extra-provincial fees | Province-specific (e.g., Ontario $300 online) |
| Director residency | Ordinary at least 25%; fewer than four requires at least one; special-sector rules separate. [105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html) | Ontario residency requirement eliminated; HOLD the broader BC/QC/NS/NB propositions pending their current operative law. [Ontario instructions section 7](https://forms.mgcs.gov.on.ca/dataset/abc650b9-3b00-42ea-bdcd-ac455e58c9ed/resource/d414fced-f60e-472f-862a-f21530037776/download/on00224e.pdf) |

**Planning recommendation only:** the original federal/multi-province and provincial/single-province default is not a legal rule. HOLD an actual recommendation until registration, naming, sector, tax and ownership facts are established; no universal best structure is verified.

## Section 3 -- Registration Process (Federal)

### Step 1: Choose Corporate Name or Number

- **Corporate name/number rules** — Numbered corporation: no name search required (e.g., "12345678 Canada Inc."). Named corporation: NUANS name search included in online filing process. Name must include a legal element: "Inc.", "Incorporated", "Corporation", "Corp.", "Ltd.", "Limited", "Ltée", "Limitée"

### Step 2: Prepare Articles of Incorporation

Share classes and rights
Restrictions on share transfers (if any)
Number of directors (fixed or min/max range)
Restrictions on business activities (if any)
Optional financial-year-end planning, not a mandatory article item under section 6(1); HOLD actual fiscal-period requirements. [CBCA articles](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-6.html).

### Step 3: File Online with Corporations Canada

- **Filing process** — Federal fee $200 online / $250 by other means; express surcharge $100. One-business-day ordinary online and four-business-hour online express are service standards, not guarantees; bind actual complete filing and route. [Schedule 5 items 1(b)/4](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [current service table](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times).

### Step 4: Extra-Provincial Registration

- **Extra-provincial registration process** — Bind where the corporation actually carries on business and each province's current route/category. Ontario Canadian-corporation initial-return fee is $0; the old Form 2 label/current route is held. BC Form 33 fee is $350; NL ordinary share-capital registration is $560, disproving a $520 maximum. Quebec's old approximate $400 category remains held. Separate name/service fees may apply. [federal guidance](https://ised-isde.canada.ca/site/corporations-canada/en/register-federal-corporation-province-or-territory); [Ontario](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit); [BC](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry); [NL item 9(a)](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf).

### Step 5: Obtain Business Number (BN) from CRA

- **Business Number process** — Federal incorporation automatically assigns BN and corporation-income-tax RC account; do not apply for a second BN/RC. Register applicable optional GST/HST/payroll accounts using actual CRA routes and entity/access conditions. Import/export RM registration uses CBSA/CARM from 21 October 2024, reusing an existing BN. BN itself is free; incorporation/service fees are separate. [CRA BN/RC](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts/corporation-income-tax.html); [CRA access](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/how-register/resident.html); [RM change](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/how-register/bn-import-export.html); [CARM](https://www.canada.ca/en/border-services-agency/services/carm/register-modify-account.html); [BN fee statement](https://www.alberta.ca/common-business-number-program-in-alberta).

### Step 6: Municipal Business Licence (if required)

Some municipalities require a business licence
Check with local municipality

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Federal Corporation (CBCA) | HOLD unqualified minimum claim | No unpaid-issue inference | Under 25(3), issue only after fully paid money/property/past-service consideration of at least fair-equivalent value | Directors assess fair equivalence; 25(4) permits specified organization/reorganization charges and payments for property/past services reasonably expected to benefit the corporation to be considered, rather than imposing another mandatory valuation test. Apply 25(5)'s subscriber/non-arm's-length promise-to-pay exclusions. HOLD actual valuation and any no-requirement claim. [CBCA 25(3)-(5)](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-25.html) |
| Ontario Corporation (OBCA) | HOLD actual provincial minimum | HOLD actual paid-up rule | HOLD actual payment/issue conditions | HOLD provincial consideration/valuation rules; they were not operatively read |
| BC Corporation (BCBCA) | HOLD actual provincial minimum | HOLD actual paid-up rule | HOLD actual payment/issue conditions | HOLD provincial consideration/valuation rules; they were not operatively read |
| Quebec Corporation (QBCA) | HOLD actual provincial minimum | HOLD actual paid-up rule | HOLD actual payment/issue conditions | HOLD provincial consideration/valuation rules; they were not operatively read |

HOLD the nationwide no-minimum claim; no complete federal/provincial census was read. A federal no-fixed-dollar-minimum conclusion would not override fully paid share-issue consideration.

## Section 5 -- Costs Breakdown

### Federal Incorporation

**Federal Incorporation Costs**

| Cost Component | Amount (CAD) | Notes |
| --- | --- | --- |
| Corporations Canada (online) | $200 | One-business-day service standard, not guarantee. [Schedule 5](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [service table](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times) |
| Express service | +$100 | Four-business-hour online standard, subject to actual conditions. [Schedule 5](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [service table](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times) |
| Extra-provincial registration (read examples) | Ontario $0; BC $350; NL $560 | Category/name/service charges apply; not a national minimum/maximum census. [Ontario](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit); [BC Form 33](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry); [NL 9(a)](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf) |
| NUANS name search (if named) | Included in federal online process | No separate report need be ordered first; HOLD any separate pre-ordered price. [registrar process](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times) |
| Federal online plus one province, arithmetic only | Ontario $200; BC $550; NL $760 | Derived sums of read fee inputs, excluding separate name/service/express costs; no universal $280–$600 range. [federal](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html); [Ontario](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit); [BC](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry); [NL](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf) |

### Provincial Incorporation (Examples)

**Provincial Incorporation Fees**

| Province | Online Fee | Notes |
| --- | --- | --- |
| Ontario | $300 | Read provincial incorporation category; distinct from initial-return $0. [official table](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit) |
| British Columbia | $350 | Limited-company Form 1; separate name fee possible. [official table](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry) |
| Alberta | HOLD actual government/provider total | The old $283.25 was not source-bound; actual government plus provider charges required. [official instructions](https://www.alberta.ca/incorporate-alberta-corporation) |
| Quebec | 2025 $389; current table read 21 November 2026 $397 | Different fee periods; not a false finding that the current fee is wrong. [2025 page 5](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/emploi-solidarite-sociale/registraire_entreprises/RE-101-T_REQ_Fees_Terms_Payment_2025.pdf); [current table](https://www.quebec.ca/entreprises-et-travailleurs-autonomes/tarifs-registraire-entreprises/societe-par-actions) |

### Annual Maintenance

**Annual Maintenance Costs**

| Item | Cost (CAD) |
| --- | --- |
| Corporations Canada annual return | $12 online / $40 by other means. [Schedule 5 item 1(k)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html) |
| Provincial annual return | No universal $0–$50 range: NL ordinary extra-provincial share-capital return is $200 paper / $180 electronic; 9(j) $50 furniture-moving/tour-operator route requires no more than five trips in the return period; 9(i) no-share-capital no-fee route is separate. HOLD current operative fee/category before charging; the published schedule is dated 2016. [9(g)-(h)](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf) |
| Accountant fees | HOLD unsupported market estimate $1,500–$5,000/year; not a statutory charge or firm quote |
| Corporate tax return (T2) | HOLD actual agreed engagement/package; not automatically included |
| Extra-provincial renewal fees | Varies by province |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return (federal) | Within 60 days of anniversary date | Corporations Canada |
| Annual return (provincial) | Varies by province | Provincial registry |
| T2 corporate tax return | 6 months after fiscal year-end | CRA |
| Corporate tax payment | 2 months after year-end (3 months for qualifying CCPCs claiming the SBD) | CRA |
| GST/HST returns | Monthly, quarterly or annual under actual assigned/elected period; ordinary annual taxable supplies over $6 million have the monthly branch. HOLD actual population and elections | [CRA periods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/gst-hst-account/change-account.html) |
| Payroll remittances | Monthly or as required | CRA |
| T4/T5 information slips | Ordinary last day of February after payment year, with next-business-day and actual special-case rules | [CRA T5](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/return-investment-income-t5/t5-information-return/date.html); completed applicable payroll/T4 read reused |
| Directors' register and minutes | HOLD actual record type/location; section 20 permits other designated places and conditional outside-Canada storage | [CBCA 20](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-20.html) |
| Shareholder register | Bind actual statutory register/location; provincial rules not all read | [CBCA 20](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-20.html) |

## Section 7 -- Bank Account Opening

### Documents Typically Required

HOLD the account-specific legal/bank/identity requirements. The original list is an intake prompt, not proof every bank requires all-director ID or BN in every case. No current bank product/identity-law review was completed.

- **Required documents** — Certificate of Incorporation (federal or provincial) Articles of Incorporation Directors' resolution authorising account opening Government-issued ID for all directors and signing authorities Business Number from CRA Proof of business address

### Typical Timeline

HOLD these original market estimates: resident 1–5 days and non-resident 1–3 weeks have no verified government/bank service basis here and cannot predict actual opening or readiness.

- **Bank account opening timeline** — 1--5 days (major Canadian banks for Canadian residents) 1--3 weeks (non-resident founders)

### Common Banks

Illustrative original provider list only; current products, eligibility, geographic coverage and acceptance were not verified. No recommendation or account availability follows from inclusion.

Royal Bank of Canada (RBC), TD Bank, Scotiabank, BMO, CIBC (Big 5)
National Bank, Desjardins (QC) (large regional)
Wise Business, Airwallex (digital/international)

## Section 8 -- Foreign Founder Considerations

HOLD actual foreign-founder, banking, immigration, ownership and tax outcomes below unless a row supplies a bounded verified rule. Unread provincial and treaty/sector conditions cannot be inferred from federal online availability.

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Ordinary federal 25% resident Canadians, at least one if fewer than four; special rules separate. Ontario requirement eliminated. HOLD broader provincial assertions. [105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html); [Ontario 7](https://forms.mgcs.gov.on.ca/dataset/abc650b9-3b00-42ea-bdcd-ac455e58c9ed/resource/d414fced-f60e-472f-862a-f21530037776/download/on00224e.pdf) |
| Canadian-resident requirement workaround | HOLD current operative BC/NS/NB rules; not independently established by Ontario repeal or online filing |
| Nominee directors | Permitted but must comply with CBCA fiduciary duties |
| Physical presence required? | No -- online filing accepted |
| Apostille requirements | Foreign documents may require authentication for banking |
| Foreign ownership restrictions | HOLD actual Investment Canada Act/sector/notification/security conditions; small/new business is not automatically exempt |
| Social Insurance Number | Not required for incorporation; required for payroll if personally employed by the corporation |
| Non-resident tax implications | Non-resident corporations carrying on business in Canada are subject to Canadian tax on Canadian-source income |

## Section 9 -- Common Mistakes and Refusals

- **R-CA-F1 -- Director residency non-compliance (federal)** — Ordinary CBCA at least 25% resident Canadians; fewer than four requires at least one. Bind special-sector/ownership exceptions. HOLD the actual consequence/dissolution and BC/NS alternatives; those operative laws were not completely read. [CBCA 105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html).
- **R-CA-F2 -- Missing extra-provincial registration** — Determine the actual carrying-on-business/registration duty in each province. HOLD any litigation bar or consequence until that province's operative law is read; do not infer it from federal guidance alone. [registration guidance](https://ised-isde.canada.ca/site/corporations-canada/en/register-federal-corporation-province-or-territory).
- **R-CA-F3 -- GST/HST threshold ignorance** — Bind the ordinary $30,000 threshold population, associates/exclusions, single-quarter and cumulative-quarter crossing branches, effective dates and application timing. HOLD actual registration date and penalties until facts are bound. [CRA table/footnotes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html).
- **R-CA-F4 -- Confusing incorporation with business registration** — Sole proprietors and partnerships register a business name; they do not incorporate. Incorporation creates a separate legal entity with limited liability. These are fundamentally different.
- **R-CA-F5 -- Shell company for non-resident tax avoidance** — HOLD actual residence/treaty, source/PE, passive/conduit and GAAR conclusions; the complete operative rules were not read. Do not infer a universal worldwide-tax or anti-avoidance outcome from the incorporation label.

## Section 10 -- Timeline

HOLD the original duration/cumulative table below as an unsupported planning illustration. It does not establish government/bank standards or readiness. Filing/certificate steps may overlap; the old cumulative minima do not follow if those steps are separate and sequential. Federal BN/RC is automatic, so the old separate application delay is not a mandatory step. Multiple provinces, permits, calendar versus business days and banking dependencies require an actual plan.

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Decide federal vs provincial | 1 day | Day 1 |
| Prepare articles of incorporation | 1--3 days | Day 2--4 |
| File online (federal or provincial) | 1 day | Day 3--5 |
| Certificate of Incorporation received | 1 day (federal online) | Day 3--6 |
| Extra-provincial registration(s) | 1--10 days per province | Day 4--16 |
| CRA Business Number and tax accounts | 1--5 days (online) | Day 4--11 |
| Open bank account | 1--5 days (resident) / 1--3 weeks (non-resident) | Day 5--32 |
| **Ready to trade** |  | **As fast as 3--5 days (Canadian-resident, federal online)** |

## Conditional arithmetic checks

No numeric client case appeared in the baseline. The first check recomputes its existing fee inputs and the old $520 upper-bound hypothesis (not a current maximum). The second diagnoses the original sequential planning inputs; it is not a forecast or an actual BN/RC process. Original planning numbers remain above as held illustrations.

```oa-check
name: Read government-fee examples and old range arithmetic
inputs:
  federal_online: 200
  ontario_initial_return: 0
  bc_registration: 350
  nl_registration: 560
  old_assumed_upper: 520
steps:
  - ontario_total: federal_online + ontario_initial_return
  - bc_total: federal_online + bc_registration
  - nl_total: federal_online + nl_registration
  - old_assumed_minimum: federal_online + ontario_initial_return
  - old_assumed_maximum: federal_online + old_assumed_upper
expected:
  ontario_total: 200
  bc_total: 550
  nl_total: 760
  old_assumed_minimum: 200
  old_assumed_maximum: 720
```

```oa-check
name: Original separate sequential timeline is conditional arithmetic only
inputs:
  decision: 1
  articles_min: 1
  articles_max: 3
  filing: 1
  separate_certificate: 1
  registration_min: 1
  registration_max: 10
  assumed_accounts_min: 1
  assumed_accounts_max: 5
steps:
  - articles_finish_min: decision + articles_min
  - articles_finish_max: decision + articles_max
  - filing_finish_min: articles_finish_min + filing
  - filing_finish_max: articles_finish_max + filing
  - certificate_finish_min: filing_finish_min + separate_certificate
  - certificate_finish_max: filing_finish_max + separate_certificate
  - registration_finish_min: certificate_finish_min + registration_min
  - registration_finish_max: certificate_finish_max + registration_max
  - assumed_accounts_finish_min: registration_finish_min + assumed_accounts_min
  - assumed_accounts_finish_max: registration_finish_max + assumed_accounts_max
expected:
  articles_finish_min: 2
  articles_finish_max: 4
  filing_finish_min: 3
  filing_finish_max: 5
  certificate_finish_min: 4
  certificate_finish_max: 6
  registration_finish_min: 5
  registration_finish_max: 16
  assumed_accounts_finish_min: 6
  assumed_accounts_finish_max: 21
```

## Sources

Completed 21 November reads are reused after confirming the baseline is unchanged. Dates below are source-read dates, not a claim every fee was operative throughout the historical 2025 year. Current fee categories require the stated period and actual filing route; no nationwide fee/ownership/standards census was completed.

| Primary source | Completed read scope | Read date |
| --- | --- | --- |
| [Federal fee regulation](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2001-512/FullText.html) | Actual Schedule 5 item 1(b) incorporation, 1(k) annual return and item 4 express rows; not a historical consultation or remission table | 2026-11-21 |
| [Federal service table](https://ised-isde.canada.ca/site/corporations-canada/en/services-fees-and-processing-times) | Online incorporation/name-search and one-business-day/four-business-hour service standards; no unconditional completion guarantee | 2026-11-21 |
| [CBCA 105](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-105.html) | Ordinary 25% and fewer-than-four at-least-one rule, with special-sector/ownership rules in (3.1)-(4) kept separate | 2026-11-21 |
| [Ontario incorporation instructions](https://forms.mgcs.gov.on.ca/dataset/abc650b9-3b00-42ea-bdcd-ac455e58c9ed/resource/d414fced-f60e-472f-862a-f21530037776/download/on00224e.pdf) | Section 7 expressly says director-residency requirement eliminated | 2026-11-21 |
| [Enacted Ontario repeal](https://alpha.ola.org/sites/default/files/node-files/bill/document/pdf/2020/2020-12/b213ra_e.pdf) | 2020 chapter 34 Schedule 1 repeals 118(3); not inferred from a blog | 2026-11-21 |
| [NL fee schedule](https://www.gov.nl.ca/gs/files/registries-companies-fees-corp.pdf) | Items 9(a), (g)-(j): registration/annual-return amounts; 9(i) no-share-capital and 9(j) furniture-moving/tour-operator five-trip cases separate. Bounded 25 November read includes the 2016 schedule date and 2017 marked changes; present annual-fee currency held | 2026-11-21; bounded follow-up 2026-11-25 |
| [NL registry FAQ](https://www.gov.nl.ca/gs/faq/commercial-registration/) | Share-capital extra-provincial registration 560 corroborated by the actual FAQ answer. Bounded 25 November re-read; not a verification of every old FAQ item or annual fee | 2026-11-21; bounded follow-up 2026-11-25 |
| [Ontario fee table](https://www.ontario.ca/page/cost-time-required-to-register-change-search-for-business-name-corporation-not-for-profit) | Actual incorporation and CIA initial-return rows; Canadian federal initial return distinct from foreign extra-provincial licence | 2026-11-21 |
| [BC forms/fees](https://www2.gov.bc.ca/gov/content/employment-business/business/managing-a-business/permits-licences/businesses-incorporated-companies/forms-corporate-registry) | Limited-company Form 1 and extra-provincial Form 33 rows; separate name charges possible | 2026-11-21 |
| [Alberta incorporation process](https://www.alberta.ca/incorporate-alberta-corporation) | Government fee plus provider charge; no operative 283.25 fee row read, catalogue/API retrieval failed | 2026-11-21 |
| [Quebec current table](https://www.quebec.ca/entreprises-et-travailleurs-autonomes/tarifs-registraire-entreprises/societe-par-actions) | 397 fee in table updated 31 August 2026; not relabelled as a 2025 amount | 2026-11-21 |
| [Quebec 2025 fee schedule](https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/emploi-solidarite-sociale/registraire_entreprises/RE-101-T_REQ_Fees_Terms_Payment_2025.pdf) | Pages 2, 3, 5, 6: 2025 incorporation 389; page 2 for-profit legal-person/trust REGULAR annual registration column 104, distinct from partnership 62 and timely free updating declaration. Bounded 25 November original PDF layout re-read resolves column mapping | 2026-11-21; bounded follow-up 2026-11-25 |
| [Federal provincial-registration guidance](https://ised-isde.canada.ca/site/corporations-canada/en/register-federal-corporation-province-or-territory) | Register where carrying on business; provincial tests and actual route still need binding | 2026-11-21 |
| [CBCA 5](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-5.html) | Eligible individual/corporate incorporators; not a nationwide entity comparison | 2026-11-21 |
| [CBCA 6](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-6.html) | Articles content; optional fiscal-year provision not made mandatory | 2026-11-21 |
| [CBCA 10](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-10.html) | Legal-name elements; numbered-name illustration is not an assigned real company identity | 2026-11-21 |
| [CBCA 15](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-15.html) | Federal capacity separate from provincial registration duties | 2026-11-21 |
| [CBCA 20](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-20.html) | Record types/location, designated places and conditional outside-Canada storage | 2026-11-21 |
| [CBCA 25](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-25.html) | Subsections (3)-(5): fully paid before issue/fair equivalence; matters directors MAY consider under (4), subscriber/non-arm's-length promise-to-pay exclusions under (5). Bounded 25 November original-text re-read | 2026-11-21; bounded follow-up 2026-11-25 |
| [CBCA 102](https://laws-lois.justice.gc.ca/eng/acts/C-44/section-102.html) | Director minimum; distributing corporation requires at least three, including two who are neither officers nor employees of the corporation or an affiliate | 2026-11-21 |
| [CRA federal BN/RC](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts/corporation-income-tax.html) | Federal incorporation automatically supplies BN and corporation income-tax account | 2026-11-21 |
| [CRA import/export route](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/how-register/bn-import-export.html) | RM registration moved to CBSA/CARM from 21 October 2024; reuse existing BN | 2026-11-21 |
| [CBSA CARM](https://www.canada.ca/en/border-services-agency/services/carm/register-modify-account.html) | Actual import/export account route and existing BN reuse | 2026-11-21 |
| [CRA resident BRO](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/how-register/resident.html) | Applicable resident/entity/Quebec/access conditions, not every entity | 2026-11-21 |
| [CRA dated BRO access change](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2026/businesses-changes-are-coming-way-you-access-business-registration-online.html) | 14 July 2026 signed-in CRA access change, separately dated | 2026-11-21 |
| [Government BN fee statement](https://www.alberta.ca/common-business-number-program-in-alberta) | No cost for BN; separate incorporation/provider fees remain | 2026-11-21 |
| [CRA GST registration timing](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) | Ordinary 30000 amount, worldwide/associates/exclusions, single versus multiple quarters, dates and application timing | 2026-11-21 |
| [CRA assigned GST periods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/gst-hst-account/change-account.html) | Monthly/quarterly/annual table and ordinary over-6-million monthly branch; actual elections/scope not assumed | 2026-11-21 |
| [CRA T4012](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-before-you-start.html) | Applicable completed return/balance-payment deadlines reused; two/three-month eligibility conditions and filing/payment distinction | 2026-11-21 |
| [CRA corporate rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) | Applicable completed federal general net-rate read reused; no national combined provincial rate inferred | 2026-11-21 |
| [Federal annual policy](https://ised-isde.canada.ca/site/corporations-canada/en/business-corporations/policy-annual-filings-canada-business-corporations-act) | 60 days after relevant anniversary, initial event year excluded | 2026-11-21 |
| [CRA T5 due date](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/return-investment-income-t5/t5-information-return/date.html) | Last day of February after payments with next-business-day/public-holiday handling | 2026-11-21 |

**Not yet confirmed:** actual provincial residency and consideration rules beyond the read Ontario repeal/federal branches; Alberta's old $283.25; present operative NL annual-fee/category and applicable schedule currency; Quebec current foreign-registration category; separate pre-ordered NUANS $25; nationwide minimum capital, fees and provincial annual obligations; exact old Ontario Form 2 route; ownership/ICA/sector, immigration/SIN, corporate residence/treaty/GAAR, litigation/dissolution consequences; account-specific bank requirements/products/times; actual GST crossing/period and corporate-tax eligibility. The old 26.5% general / 12.2% small-business / first $500,000 examples are not universal national rules: the supported 2025 Ontario arithmetic does not establish current provincial rates or eligibility. Accountant $1,500–$5,000 and package inclusion, naming/commercial comparisons and the entire cumulative timeline remain unsupported market/planning policy. Holds block final advice; nine contradicted historical groups and a dated Quebec mismatch do not certify every legal proposition.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.
