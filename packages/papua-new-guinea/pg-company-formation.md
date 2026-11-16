---
name: pg-company-formation
description: >
  Register an ordinary PNG company or overseas company in 2026. Follow the IPA name, company application, certification and annual-return workflow, identify ownership and resident-director requirements, budget published registry fees and separate incorporation from tax registration. Property-transfer duty, sector licences and unresolved foreign-control facts require additional evidence.
jurisdiction: PG
category: formation
tax_year: 2026
last_updated: 2026-11-16
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Papua New Guinea company formation and entity choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Incorporate an ordinary PNG company or register an existing overseas company with the Investment Promotion Authority (IPA), then identify the separate foreign-investment and tax registrations. Current procedural instructions were read in the public registry; no application was submitted. Business-name registration for a sole trader is a different process and does not create a company. Partnerships, incorporated associations, regulated financial entities and resource projects need their own legal analysis.

### Quick reference

| Requirement or registry fee | Rule and conditions | Official source |
|---|---|---|
| Essential structure | At least 1 share, 1 shareholder and 1 director; this is not a statement that a regulated business has no capital requirement | [Companies Act s. 11](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf) |
| PNG-incorporated company resident director | At least 1 director ordinarily resident in PNG; a director must be a natural person and meet disqualification rules | [Companies Act ss. 128-130](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf) |
| Name reservation | Required before registration; reservation ordinarily available for 2 months under the Act | [Companies Act ss. 21-23](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf) |
| Domestic incorporation, A-1 | PGK 400 online; PGK 600 paper with N-1 addendum | [IPA service-fee schedule, A-1](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US) |
| Overseas registration, A-2 | PGK 450 online | [IPA service-fee schedule, A-2](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US) |
| Foreign enterprise certification | PGK 2,000 for the ordinary company applications A-20 or A-21, separate from incorporation | [IPA service-fee schedule](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US) |
| Annual return | AR-1 PNG company PGK 250; AR-2 overseas company PGK 750, excluding any late fee | [IPA service-fee schedule](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US) |

A share has no nominal or par value. The ordinary incorporation provisions reviewed set a minimum number of shares, not a general cash-capital amount. Check licences, solvency, issue consideration and any sector-specific minimum before saying that no minimum capital applies. [Companies Act ss. 11, 39, 41-47](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf).

## Ask the client first

Obtain the proposed activity, legal form, ownership and ultimate beneficial owners, citizenship and control arrangements, director details and ordinary residence, reserved name, registered office, address for service, share classes and consideration, constitution choice, and whether an overseas entity already exists. For foreign investment obtain intended locations, activity codes, funding, business plan and any sector licences. Identify an authorised filer. Do not request a client's login credentials.

## The method, step by step

1. **Choose the entity.** A PNG company has separate legal personality from incorporation; an overseas registration registers the existing foreign entity. A sole trader's business name does not limit the proprietor's liability. Record the tax treatment separately using `pg-corporate-income-tax` or `pg-income-tax`. [Companies Act ss. 11-16 and overseas-company Part](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf); [IPA registration guide](https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName).
2. **Check activity and ownership before trading.** Under the Investment Promotion Act, a foreign enterprise is one that is neither a national enterprise nor a citizen, or one declared foreign by the Minister. A national enterprise needs more than 50% citizen ownership, directly or indirectly, and must not be controlled by a non-citizen under agreements or in practice. Consequently an evenly split ownership structure cannot be cleared from the registry webpage's abbreviated ownership wording. Apply the statute and investigate control. [Investment Promotion Act s. 3, ss. 25-25A](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/IPA-Act-1992.pdf).
3. **Set up access and reserve the name.** On the IPA registry, the filer uses their own client account, selects Business Entities, then the appropriate PNG or Overseas Company name reservation. Approval of a name is required before completing the company application. Public entity searches are available separately from filing authority. [IPA incorporation instructions](https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName).
4. **Prepare the incorporation record.** Collect company name, directors, share and shareholder details, relevant addresses, activity and declaration. Keep signed director, secretary if any, and shareholder consents at the registered office and produce them when requested. A registered office must be in PNG, identifiable and accessible, with its actual location recorded; a postal box alone does not meet this requirement. [Companies Act ss. 13, 13A, 128-130, 161](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf).
5. **Handle the constitution correctly.** The Act allows a company with or without a constitution. The registry help page nonetheless describes an upload in its generic incorporation instructions. If choosing the statutory default, obtain the registry's accepted filing treatment rather than inventing a compulsory constitution or uploading a fictitious one. A constitution that is adopted must be provided in the required certified form. [Companies Act ss. 13, 27-32](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf); [IPA form instructions](https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName).
6. **Complete A-1 or A-2.** Review all tabs, declarations and payment before submitting. For an existing overseas company use Part XX, not the ordinary PNG-incorporation resident-director rule. Section 382 includes an office/agency/branch, a share-transfer office, specified property administration and commercial State licences/authorities in carrying on business. It excludes a bank account, internal meetings, litigation, certain independent-contractor sales, orders accepted abroad, debts/securities, an isolated transaction completed within 1 month that is not recurrent, and passive investment/property holding when those facts alone apply. Refer mixed branches rather than treating the list as an all-purpose exemption. Reserve the overseas name before carrying on business under section 382B and apply for registration within 1 month of commencing to carry on business under section 383. A-2 must include directors and local business-address details, evidence of incorporation and the constitution instrument if any, with the required certified English translations. Identify one or more persons resident or incorporated in PNG authorised to accept local service, with the required residential and postal addresses. [Companies Act ss. 382-387](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf). Save a draft if incomplete. IPA reviews the application, may request information and emails a certificate if approved. Do not promise a processing duration: the public instructions give a review sequence, not a guaranteed turnaround. [IPA company-registration instructions](https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName).
7. **Complete separate foreign certification before business begins.** A certificate of incorporation is not a foreign-enterprise certificate. Check reserved and restricted activities, exemption eligibility, the approved locations and certificate conditions. The statutory certification rule is broader than merely issuing shares to a foreign holder; a certificate does not override another licence. The amended system requires the following separate maintenance controls. A certificate expires if no covered business activity commences within 1 year after issue, and is invalid during suspension or after cancellation under section 29A. File the annual status report in the anniversary month of issue under section 29B. Subject to section 32, notify altered application particulars in writing within 10 working days under section 28(7). For a foreign enterprise, changes in ownership, shareholding, beneficial ownership or control normally require a new certificate application within 10 working days. Section 32(3) has separate exceptions: the less than 10% in any 1 year or less than 25% since-certification tests, specified unchanged-holding-company subsidiary changes, listed foreign enterprises and qualifying subsidiaries of listed foreign enterprises. Do not assume an exception from an unexplained ownership percentage; obtain the full ownership history and apply the actual branch. A citizen/national enterprise becoming foreign through the specified ownership changes applies within 1 month under section 32(4). These duties do not establish approval or displace reserved/restricted-activity rules. [Amended ss. 28(7), 29A-29B and 32](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Investment_Promotion_(Amendment)_Act_2023_CERTIFIED.pdf). [Investment Promotion Act ss. 25-29 and 2023 amendment](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Investment_Promotion_(Amendment)_Act_2023_CERTIFIED.pdf). Current guide paths are Business Entities then Foreign Certification, with A-20 for an overseas company or A-21 for a local company. [IPA certification instructions](https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName).
8. **Set up tax and employer compliance.** Obtain the IRC tax identity and actual tax registrations, GST status, payroll-withholding registration and, if relevant, authorised superannuation-fund arrangements. Neither an IPA certificate nor a business bank account establishes those tax statuses. Use the relevant sibling skill; no estimated tax registration timing or threshold is substituted here.
9. **Maintain the company.** Diarise the annual return in its allocated month and keep officers, addresses, shares and beneficial-ownership records current. An ordinary newly incorporated company does not file an annual return in its year of incorporation. For an overseas company, use section 391: submit the return during the allocated month, date and compile its information as at a day within that month, and attach the company/group financial statements required by section 390 when it carries on business in PNG. Section 390 contains PNG-business statements, Registrar acceptance and Gazette-class-exemption conditions; do not assume foreign accounts automatically suffice. The first-registration-calendar-year annual-return exception does not cover a company deemed registered under section 445. The overseas allocated-month procedure is distinct from domestic section 215. [Companies Act ss. 390-391](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf). The annual return is separate from income tax and annual financial statements. The 2022 amendment adds beneficial-owner and annual-return information; use the current registry form rather than an old paper checklist. [Companies Act s. 215](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf); [Companies Amendment Act 2022, amended s. 72 and Schedule 6](https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/22A_45.pdf).

### Exceptions and held topics

| Situation | Action |
|---|---|
| Foreign control with minority shareholding | Analyse control, not just the percentage displayed on a share register |
| Existing company that missed re-registration | Check register status and the applicable restoration route; do not simply incorporate again or promise administrative restoration |
| Transfer of land or property into the entity | Obtain the conveyance, consideration, market value, instrument and current Stamp Duties Act schedule; no property-transfer rate is authorised by this incorporation skill |
| Partnership, business name or association | Use the matching legal route, not company forms |
| Bank, insurer, mining, petroleum or LNG business | Obtain the sector approvals and project terms before choosing capital, tax or licensing treatment |

## Worked cases

### Domestic company and annual-return budget

A straightforward online PNG incorporation, followed by an ordinary later-year annual return, uses the separate published A-1 and AR-1 fees. This is a fee budget, not a tax calculation or a promise of approval. Name reservation, professional fees and licences are not included. [IPA fee schedule](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US).

```oa-check
name: PNG online incorporation and later annual return
inputs:
  incorporation: 400
  annual_return: 250
steps:
  - total: incorporation + annual_return
expected:
  total: 650
```


### Local company that also needs foreign certification

If the legal ownership/control analysis establishes foreign-enterprise status, add the A-21 fee to A-1. Do not charge the overseas-company A-2 fee for a newly created PNG company. [IPA fee schedule A-1 and A-21](https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US).

```oa-check
name: PNG incorporation with separate foreign certification
inputs:
  incorporation: 400
  certification: 2000
steps:
  - total: incorporation + certification
expected:
  total: 2400
```


## When to refuse or refer

Do not lodge with unresolved beneficial ownership, disqualified directors, an unapproved name, an activity reserved to citizens or incomplete required foreign certification. For a PNG-incorporated company, stop if its required resident director or accessible registered office is missing. For an overseas company, stop if its required local service recipient, application particulars or incorporation/constitution evidence is missing. Refer property-transfer duty, sector capital, immigration, court restoration and disputed registry status for PNG legal advice. Never create an account, pay or submit an application without the client's express instruction.

## Sources

Read on 16 November 2026. A scoped read does not certify every provision in a long Act.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for Companies Act 1997, IPA consolidation to 2014: ss. 11-16, 21-32, 39-47, 128-130, 161, 215 and full Part XX ss. 382-391, including carrying-on-business exclusions and financial-statement exceptions | https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Companies_Act_1997_(consolidated_to_2014).pdf | 2026-11-16 |
| Read for Companies Amendment Act 2022: beneficial owners, re-registration and annual-return information | https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/22A_45.pdf | 2026-11-16 |
| Read for Investment Promotion Act, definitions and ss. 25-29 | https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/IPA-Act-1992.pdf | 2026-11-16 |
| Read for Investment Promotion Amendment Act 2023: full amended ss. 28-29D and 32 with neighbouring clauses, including certificate validity, report calendar, changes and exceptions | https://www.ipa.gov.pg/Documentation/PG/ActsAndRegulations/Investment_Promotion_(Amendment)_Act_2023_CERTIFIED.pdf | 2026-11-16 |
| Read for IPA current registration and certification workflow | https://www.ipa.gov.pg/public/howto.aspx?cn=RegisterBusinessName | 2026-11-16 |
| Read for IPA current service fees, company and foreign-certification rows | https://www.ipa.gov.pg/public/prescribedforms.aspx?lang=en-US | 2026-11-16 |

Not yet confirmed: A current official property-transfer stamp-duty schedule, guaranteed processing times and sector-specific capital requirements. The foreign-certification webpage simplifies ownership differently from the statutory national-enterprise definition; control and evenly split ownership require the statutory analysis above. No filing was performed.
