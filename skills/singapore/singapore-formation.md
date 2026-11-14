---
name: singapore-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Singapore. Trigger on phrases like "set up a company in Singapore", "Pte Ltd", "ACRA registration", "Singapore company formation", "register a business Singapore", "BizFile+", "Singapore incorporation", "company secretary Singapore", "resident director Singapore", "Employment Pass", or any question about starting a business entity in Singapore. Covers entity types (Pte Ltd, LLP, sole proprietorship), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Singapore company formation.
version: 2.0
jurisdiction: SG
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - company-formation-workflow-base
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Singapore company formation v2.0

Calendar-2026 formation and ongoing requirements. Incorporation, bank onboarding, tax residence, work permission and permission to conduct a regulated business are distinct outcomes. A submitted form is not an approval.

## Scope and who this is for

A founder or accountant registering a Singapore local company through ACRA's Bizfile. Entity comparison is a selection aid, not a universal Pte Ltd recommendation. Partnerships, LLPs, public and regulated companies need their own structure-specific work before filing. Currency is SGD; ACRA administers company registration, IRAS tax and MOM work passes.

| Structure | Legal personality and liability | Ownership and tax boundary | Source |
|---|---|---|---|
| Sole proprietorship | No separate personality; owner has unlimited liability | One owner; profits taxed to the owner | [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/) |
| Partnership | No separate personality; partners have unlimited liability | Generally 2 to 20 partners, with professional exceptions; tax follows partner type | [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/) |
| LLP | Separate legal person; protection does not excuse a partner's own wrongful acts | At least 2 partners, no maximum; locally resident manager required; partner-level tax | [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/) |
| Private company | Separate person; shareholder liability limited | At least one shareholder/director; private-company shareholder maximum 50; corporate tax | [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/) |
| Public company | Separate person; share-capital and guarantee types differ | No private-company shareholder maximum; public-company requirements need a separate assessment | [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/) |

Foreign ownership does not remove resident officer/manager, work-pass, sector or licensing conditions. Do not assume all sectors permit every ownership arrangement. Read the current structure requirements for the actual founder.

## Ask the client first

- Proposed activities and SSIC codes, customers, regulated work and any cross-border trade.
- Every legal/beneficial owner, ownership percentage, nominator/controller, nationality and residence.
- Proposed director's eligibility, ordinary residence, disqualifications and pass-issuer permission where applicable.
- Share classes, rights, number, currency, issued commitment, actual payment and non-cash consideration.
- Registered Singapore address, public-access hours, consent and residential-use permissions where relevant.
- Name, structure, proposed FYE and first accounting period, constitution and persons authorised to endorse/file.
- Expected taxable turnover, employees and work location, secretary/auditor arrangements, existing group and bank KYC readiness.

Do not default to a company from a claimed tax-saving threshold. Liability, extraction, commercial purpose, administration and immigration facts all matter.

## Rates, bands and thresholds

| Item | Current boundary | Source |
|---|---|---|
| Name application | S$15; approved name used within 120 days, then released | [Official source](https://www.acra.gov.sg/resources/guides-forms/apply-for-new-business-entity-name/) |
| Company registration | S$300; name plus ordinary registration = S$315, excluding service costs/capital | [Official source](https://www.acra.gov.sg/manage/companies/service-transaction-fees/) |
| Annual-return filing | S$60; separate from formation | [Official source](https://www.acra.gov.sg/manage/companies/service-transaction-fees/) |
| Share capital, company requiring it | At least S$1 in issued share capital; issued commitment and actual paid-up amount are distinct | [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/deciding-on-share-capital-share-types/) |
| Secretary appointment | Within six months of registration; secretary cannot be the sole director | [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/) |
| Auditor appointment | Within three months unless actually exempt | [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/) |
| Ordinary non-listed company's AR | Within seven months of FYE; eight where it has share capital and an overseas branch register | [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-annual-returns-companies/deadline-requirements/) |
| Listed company's AR | Within five months of FYE; six with share capital and an overseas branch register | [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-annual-returns-companies/deadline-requirements/) |
| Private-company ordinary AGM | Within six months of FYE, subject to an applicable AGM exemption/dispensation; not a universal first 18-month grace period | [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/choosing-a-companys-financial-year-end/) |
| ECI | Within three months of FYE unless waiver/specific exemption applies; ordinary waiver requires annual revenue at most S$5m AND nil ECI before SUTE/PTE | [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing) |
| Corporate return | Ordinary Form C-S/C-S (Lite)/C due 30 November of the relevant YA; identify first accounts/YA, not merely the following calendar year | [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies) |
| Corporate headline tax | 17%; no universal effective 8.5% on every new company's first S$200,000 | [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| SUTE, qualifying first three consecutive YAs | 75% exemption first S$100,000 normal income and 50% next S$100,000; residence, incorporation, shareholder and activity conditions apply | [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) |
| Small-company audit thresholds | Private company, ordinarily at least two of revenue ≤S$10m, assets ≤S$10m, full-time employees ≤50 for the immediate past two consecutive FYs; startup/group/continuation conditions below | [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/preparing-financial-statements/audit-exemptions/) |
| 2026 EP salary starting points | S$5,600 general / S$6,200 financial services for age 23 or below, rising by age; COMPASS ordinarily also applies | [Official source](https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility) |

A share commitment is not an expense or registration fee. Enter actual issued and paid-up amounts separately; never mark capital paid without evidence. The current guide permits unpaid/partly-paid share capital, so the former universal S$1 paid-up minimum and "at or after incorporation" payment promise are not certified. Non-cash consideration needs its actual terms/valuation and filing classification. [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/deciding-on-share-capital-share-types/)

## The method, step by step

1. Choose the structure using the liability/ownership facts. Overseas foreigners engage a CSP; a FIN holder checks with the pass issuer before accepting a role. Confirm the local director and secretary plan. [Official source](https://www.acra.gov.sg/register/business/choosing-business-structure/)
2. Reserve the name in Bizfile's **Apply for new business entity name** service. Select structure and SSIC; review the declaration, pay, save the transaction ID, receipt and approval expiry. Referral/review is not instant approval. Do not use the former unsupported 60-day/S$10 renewal promise. [Official source](https://www.acra.gov.sg/resources/guides-forms/apply-for-new-business-entity-name/)
3. Assemble constitution (model or customised), office/FYE, officer/shareholder details, nominators/controllers and actual capital/allotments. The filer must qualify; the name reserver normally must be a proposed director or secretary, or use a CSP. [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/)
4. In Bizfile choose **Register → Register new entity → Register new business entity**. Retrieve the name transaction, complete company/position-holder data, ROND/RONS and RORC questions, capital/allotments and constitution. Review, submit, obtain endorsements where required and pay. Save acknowledgement and receipt. [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/)
5. Check the Bizfile inbox for the actual outcome, incorporation notice and UEN. Download the Business Profile; do not label an application receipt a certificate of successful incorporation. Most applications are approved soon after payment, but complex/referral cases have separate processing periods. [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/)
6. After approval, arrange Corppass, company registers, bank onboarding, the secretary and any auditor. Check business licences/trade permits before operations and CSN if hiring. Tax and GST obligations are separate from ACRA's annual return. [Official source](https://www.acra.gov.sg/register/business/after-registering/local-company/)

### Bank account opening

Use the chosen institution's current checklist. ACRA identifies authorised signatories, director/owner identity checks, board decisions and certified company documents; it notes most directors may need to be physically present. Prepare the business description, source of funds, constitution, profile, ownership chart and address evidence as requested. No universal 25% bank KYC cut-off or completion timeline is certified here. [Official source](https://www.acra.gov.sg/register/business/after-registering/local-company/)

The old examples of banks/platforms are not recommendations or proof they provide a regulated deposit account. ACRA currently lists ANEXT Bank, Bank of China, CIMB, DBS, Maybank, OCBC, State Bank of India and UOB. Product eligibility and protection must be checked with the actual provider. [Official source](https://www.acra.gov.sg/register/business/after-registering/local-company/)

### Cost and timeline workpaper

Separate government charges, share capital and private quotes. Obtain actual quotes for secretary, registered office, nominee director if appropriate, accounting/tax and audit. Do not quote the former first-year totals or market ranges as statutory costs. A nominee remains a real director with duties; it is not a way around work or disclosure rules. [Official source](https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/)

Sequence name approval → complete documents/endorsement → payment → registration outcome → required licences/work authorisation → bank and operational readiness. A bank's KYC or MOM's decision may outlast incorporation. Do not promise "ready to trade in one week" or rank Singapore's speed without evidence.

## Boundary and exception table

| Situation | Action and limit |
|---|---|
| No qualifying local director | Hold incorporation until a lawful director arrangement exists. A paid nominee service is not the only theoretical way to appoint an eligible director and is not automatically recommended. |
| Pass holder wants to be director or work | Check pass issuer and role. An EP/S Pass label alone does not prove ordinary residence/permission. Incorporation does not authorise employment. |
| EP application | Use MOM's age/sector/application-date salary table, COMPASS unless exempt, and actual advertising requirements. No official S$50,000 company-capital guarantee was found. New applications from 1 Jan 2027 use higher starting salaries S$6,000/S$6,600, with age progression; renewal timing differs. [Official source](https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility) |
| Small private company seeks audit exemption | Two-of-three test, new-company current-year route, group including foreign entities, and continuing/disqualifying conditions must all be considered. Corporate shareholders do not automatically bar exemption. [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/preparing-financial-statements/audit-exemptions/) |
| Audit-exempt company | Financial-statement preparation/filing remains a separate question. Apply actual dormant-relevant/solvent-EPC exemption or Full/Simplified XBRL/PDF category; "only larger companies use XBRL" is wrong. [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-financial-statements-in-xbrl-format/requirements-exemptions/) |
| First accounts span more than one YA | Allocate the income/expenses to the proper YAs. A missing IRAS notification is not a filing exemption. [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies) |
| Nil ECI | Apply the two-part waiver, not "always file nil". Annual return and final corporate return are still separate obligations. [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing) |
| Nominee/controller or regulated activity | Record actual nominators/controllers and exemption basis. Do not provide a shell-company concealment or licensing bypass. |
| Residential office / foreign document / apostille | Obtain the applicable authority and receiving institution's requirements; this pass does not certify every zoning/notarisation outcome. |

## Worked cases

**Ordinary registration budget:** a private company reserves one approved name and completes one registration, with no special UEN or private service charge. Government setup charges are 15+300=315. A later annual return adds 60, so 375 is the combined government amount across these distinct events, not a first-year all-inclusive quote. Share capital is separate. [Official source](https://www.acra.gov.sg/manage/companies/service-transaction-fees/)

```oa-check
name: Distinguish formation charges from later annual return
inputs:
  name_fee: 15
  registration_fee: 300
  annual_return_fee: 60
steps:
  - formation_charges: name_fee + registration_fee
  - combined_distinct_events: formation_charges + annual_return_fee
expected:
  formation_charges: 315
  combined_distinct_events: 375
```

**Nil ECI is not a universal waiver:** a company with 5,000,000 annual revenue and nil pre-exemption ECI meets the ordinary two-part waiver; the same revenue with 100,000 ECI does not. Neither conclusion waives ACRA AR or the final corporate return. [Official source](https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing)

## When to refuse or refer

- R-SG-F1: No qualifying resident director: hold; do not invent eligibility.
- R-SG-F2: Missing secretary: arrange appointment within the sourced period; no blanket promise of automatic strike-off is made.
- R-SG-F3: Capital/EP: refuse an invented S$50,000 approval threshold; obtain actual funding and MOM eligibility evidence.
- R-SG-F4: Shell/AML: refuse concealment, false owner/controller statements and conduit arrangements without lawful purpose.
- R-SG-F5: Missing ECI: test waiver before deciding filing; resolve an estimated assessment with IRAS, not by ignoring it.
- R-SG-F6: Work permission: hold activities requiring an appropriate valid work pass; ownership and incorporation are not permission to work.

Refer public/regulated structures, bespoke share rights, non-cash valuation, director disqualification, immigration, exemptions and disputed filings to their respective qualified practitioners. Do not file, accept declarations, hire or pay without the client's authorised process.

## Filing and payment

Maintain the office, officers, members, capital, controller and nominee records, with current electronic/central filings where required. Appoint any required auditor and keep proper annual accounts. Calendar the actual FYE-based AR and AGM requirements and separately ECI/final tax returns. [Official source](https://www.acra.gov.sg/register/business/after-registering/local-company/)

For the AR use Bizfile's **File annual returns** service, review company/officer/shareholder details, AGM status and applicable financial statements, submit and pay the separate S$60. Retain acknowledgement, receipt and updated record. [Official source](https://www.acra.gov.sg/manage/companies/service-transaction-fees/) The financial-statement filing category depends on company type, size and public accountability, not audit exemption alone. [Official source](https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-financial-statements-in-xbrl-format/requirements-exemptions/)

For tax use the company's authorised Corppass/myTax Portal access and correct UEN. GST registration follows taxable-turnover retrospective/prospective tests; load `sg-gst-return` for filing/InvoiceNow and input-tax requirements. Apply for a CPF Submission Number where hiring requires it and use the actual payroll schedule: the former "statutory due by 14th" shorthand is not re-certified. [Official source](https://www.acra.gov.sg/register/business/after-registering/local-company/) ECI waiver and corporate return deadlines use the separate IRAS sources above.

## Completion checklist

- Structure, owners, local director eligibility and pass permission established.
- Name transaction/expiry, SSIC, FYE, office, constitution, capital/allotments and nominee/controller facts reconciled.
- Endorsements/payment followed by actual incorporation outcome, UEN and Business Profile retained.
- Bank KYC, Corppass, registers, licences, work permission and employee registrations resolved separately.
- Secretary/auditor and AR/AGM/ECI/final-return calendar set using the actual company/FYE/exemption facts.
- Government fees, paid-up capital and private quotes separated; no promised bank/EP outcome.

## Sources

| Source and scope read | Official URL | Read on |
|---|---|---|
| Read for legal personality/liability, owner/partner limits, corporate versus partner tax, foreign CSP and local-manager requirements. | https://www.acra.gov.sg/register/business/choosing-business-structure/ | 2026-11-14 |
| Read for SSIC/structure selection, service sequence, payment/transaction ID, 120-day use and release, referrals; no old renewal promise. | https://www.acra.gov.sg/resources/guides-forms/apply-for-new-business-entity-name/ | 2026-11-14 |
| Read for required data, ten-step Bizfile process, controller/nominee questions, issued/paid capital, endorsement/payment and actual incorporation outcome. | https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/registering-via-bizfile/ | 2026-11-14 |
| Read for issued versus paid capital, minimum issued capital and unpaid/part-paid/non-cash distinctions. | https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/deciding-on-share-capital-share-types/ | 2026-11-14 |
| Read for local eligibility, FIN pass-issuer check, secretary/sole-director boundary, appointments and nominee duties. | https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/appointing-company-directors-other-key-officers/ | 2026-11-14 |
| Read for name, company registration and annual-return government charges. | https://www.acra.gov.sg/manage/companies/service-transaction-fees/ | 2026-11-14 |
| Read for Corppass, bank prerequisites, registers, licences, staff CSN and separation of operations from registration. | https://www.acra.gov.sg/register/business/after-registering/local-company/ | 2026-11-14 |
| Read for listed/non-listed and overseas-branch-register AR periods, including dormant live companies. | https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-annual-returns-companies/deadline-requirements/ | 2026-11-14 |
| Read for private-company AGM/AR examples and actual FYE boundaries. | https://www.acra.gov.sg/register/business/registering-different-business-structures/local-company/choosing-a-companys-financial-year-end/ | 2026-11-14 |
| Read for preparation versus filing, dormant/solvent-EPC distinction and Full/Simplified XBRL/PDF categories; not a fresh certification of every exemption definition. | https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/filing-financial-statements-in-xbrl-format/requirements-exemptions/ | 2026-11-14 |
| Read for two-of-three thresholds, startup/group/continuation and separate financial-statement filing; Companies Act s205C and Thirteenth Schedule referenced by ACRA. | https://www.acra.gov.sg/manage/companies/legal-requirements-common-offences/preparing-financial-statements/audit-exemptions/ | 2026-11-14 |
| Read for age/sector salary tables, 2027 new-application/2028 renewal distinction, COMPASS and advertising boundary. | https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility | 2026-11-14 |
| Read for three-month ECI period, 5m/nil pre-exemption waiver, specific exempt categories and estimated assessment handling. | https://www.iras.gov.sg/taxes/corporate-income-tax/estimated-chargeable-income-%28eci%29-filing | 2026-11-14 |
| Read for preceding-year basis, first accounts across YAs, 30 November return and separate ECI obligation. | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/basic-guide-to-corporate-income-tax-for-companies | 2026-11-14 |
| Read for 17% headline and PTE/SUTE bands, first-three-YA and residence/shareholder/activity conditions. | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes | 2026-11-14 |

Not yet confirmed: current individual bank KYC documents/timing, a universal beneficial-owner 25% cut-off, residential zoning and apostille requirements, work-pass decision or a universal 50,000 paid-capital threshold. The old private annual ranges (secretary 300-900; office 200-500; nominee 1,500-4,000; accounting 800-2,500; audit 2,000-8,000), first-year totals (foreign 3,100-8,200; local 1,400-3,700), formation/bank/EP/tax-file timing promises, 60-day/10-dollar name renewal, universal 1-dollar paid-up requirement, blanket corporate-tax-file automation and fixed payroll 14th due date are not usable guidance without their own current official evidence. Exact AGM exemption/dispensation conditions and sector-specific foreign ownership remain case-specific. Historical replacement of Memorandum/Articles in 2014, company-name suffix, public-company subtype, custom rights and legal disputes require their actual statutory text, which was not newly opened here.
