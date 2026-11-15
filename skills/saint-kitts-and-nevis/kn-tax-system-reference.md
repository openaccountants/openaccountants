---
name: kn-tax-system-reference
description: >
  Start here for how the Saint Kitts and Nevis tax system is built, for 2026: the
  income tax charge and its s 3(3) exclusion of income of persons other than companies
  from 1 May 1980, company residence by management and control and permanent
  establishment (Act 12 of 2021: more than six months for construction, more than 183
  days for services), who is assessed (companies, partnerships, trustees, representatives,
  unincorporated business tax persons), the currency rules (EC dollars for Inland
  Revenue taxes, any legal tender for customs), the year of assessment and basic year,
  and which authority runs what (Inland Revenue, Customs, Social Security Board,
  Federal and Nevis allocation). Routes rates and filing to the other Saint Kitts and
  Nevis skills. Trigger phrases include Saint Kitts tax system, St Kitts tax residence,
  St Kitts permanent establishment, Nevis tax, no personal income tax St Kitts.
version: "1.0"
jurisdiction: KN
tax_year: 2026
tax_year_notes: "Year of assessment 2026. Built on the revised statutes to 31 December 2017, the Inland Revenue Act revised to 31 December 2002 and the Income Tax (Amendment) Act 2021 (Act 12 of 2021, published 26 March 2021). Later amendments to these provisions were not checked; see the Not yet confirmed line."
last_updated: 2026-11-15
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis tax system reference

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this skill to select the relevant tax person, territorial branch, period, currency rule and authority before choosing a calculation or return skill. Establish the requested date, legal form, residence, income source, activity, island and representative capacity first.

The source periods are **31 December 2017** for the revised statutes, **31 December 2002** for the Inland Revenue Act and **26 March 2021** for the separate company amendment. They do not form a complete consolidation of all law at 2026. Rates, returns and payments are in the other Saint Kitts and Nevis skills:

| Question | Skill |
|---|---|
| Company income tax, rates and returns | [kn-corporate-income-tax](kn-corporate-income-tax.md) |
| Unincorporated business tax | [kn-unincorporated-business-tax](kn-unincorporated-business-tax.md) |
| Payments to non-residents, withholding | [kn-nonresident-withholding](kn-nonresident-withholding.md) |
| Housing and social development levy on pay | [kn-housing-social-development-levy](kn-housing-social-development-levy.md) |
| Social security contributions | [kn-social-security-contributions](kn-social-security-contributions.md) |
| VAT and import charges | [kn-vat-and-import-charges](kn-vat-and-import-charges.md) |
| Property tax and stamp duty | [kn-property-tax-stamp-duty](kn-property-tax-stamp-duty.md) |
| Special regimes and incentives | [kn-special-regimes](kn-special-regimes.md) |
| Forming a company | [kn-company-formation](kn-company-formation.md) |

## Ask the client first

1. What date, and which year of assessment, is the question about?
2. Is the taxpayer a company (local or foreign), a partnership, an individual in business, a trust or estate, or a representative?
3. For a company: where are its central mind, management and control ordinarily situated?
4. For a foreign enterprise: does it have a fixed place of business, a construction project lasting more than six months, or services by its personnel aggregating more than 183 days in a twelve-month period?
5. On which island does the business operate (Saint Kitts or Nevis)?
6. Is the question about an Inland Revenue tax, a customs charge or social security?

## The method, step by step

### Key figures

| Item | Figure and conditions | Official source |
|---|---|---|
| Income of persons other than companies | The s 3 charge does not apply to income accruing on or after 1 May 1980 to any person other than a company (s 3(3)) | [Cap. 20.22, s 3](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=11) |
| Foreign income of a temporary visitor | Not taxed if present for a temporary purpose only and not resident for periods totalling six months in the basic year (s 3 proviso) | [Cap. 20.22, s 3](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=10) |
| Permanent establishment, construction | A building site, construction, assembly or installation project, or supervision of one, only if it lasts more than six months | [Act 12 of 2021, s 3A](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=2) |
| Permanent establishment, services | Services by the enterprise's personnel only if they continue for periods aggregating more than 183 days in any twelve month period commencing or ending in the fiscal year | same |
| Resident company | Managed and controlled from within Saint Christopher and Nevis, whether or not registered there; managed and controlled means where the central mind, management and control is ordinarily situated (s 3A(4)) | same |
| Year of assessment | The twelve months commencing on the first day of January (s 2) | [Cap. 20.22, s 2](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=9) |
| Currency, Inland Revenue taxes | Tax shall be payable in Eastern Caribbean dollars (Cap. 20.52, s 20) | [Cap. 20.52, s 20](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=12) |
| Currency, customs | Customs duties, rates, charges and drawback may be paid in any currency being legal tender in Saint Christopher and Nevis (Cap. 20.04, s 262(b)) | [Cap. 20.04, s 262](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_04-Customs-Act.pdf#page=137) |

### 1. Territorial reach

Income Tax Act, Cap. 20.22, s 3 starts with specified income of any person accruing in, derived from or received in Saint Christopher and Nevis or elsewhere, whether received locally or not. Its income heads and qualifications must be read with **s 3(3)**: income accruing on or after **1 May 1980** to a person other than a company is excluded from the general charge. Historical personal rates, allowances and representative machinery do not undo that exclusion. Separate business taxes and withholding provisions require their own scope analysis. [Sections 2 to 3, physical pp 7 to 11](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=7)

The retained s 3 proviso charges the locally received amount of foreign **earned income arising to a person not ordinarily resident or not domiciled** in the Federation. Preserve that combined wording. A separate mixed local/foreign trade provision treats the whole profit as locally arising for a resident individual whose home is in the Federation. Another proviso concerns foreign income of a person present only temporarily, without an intention to establish residence, who has not actually resided locally for an aggregate 6 months in the basic year. These historical provisos remain subject to s 3(3); do not convert them into a current ordinary personal income charge. [Section 3, physical pp 10 to 11](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=10)

Act 12 of 2021 inserted s 3A. A resident company's assessable income includes its assessable income wherever arising. A non-resident company carrying on local trade or business through a local permanent establishment is assessed on income attributable to that establishment. This is not a charge on every foreign company's worldwide income. The amendment records assent and Gazette publication on 26 March 2021 and contains no postponed or appointed-day clause. Its operation from that date is a **source-based inference** from those records and Constitution s 42(3) to (4), which requires Gazette publication for operation whilst permitting postponement or retrospective legislation. [Amendment, physical pp 1 to 4](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=1) · [Constitution, physical p 36](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/The-Constitution-of-St-Christopher-and-Nevis.pdf#page=36)

The inserted permanent-establishment definition includes a fixed place of business, specified construction or related supervisory activity lasting **more than 6 months** and specified services exceeding **183 days** in its stated 12-month/fiscal-year frame. Its preparatory or auxiliary exceptions, anti-fragmentation conditions, dependent-agent branches and ordinary-course independent-agent exception must be applied together. The independent-agent exception is restricted where the agent acts exclusively or almost exclusively for one or more enterprises to which the agent is a related person. Control of one company by another does not alone establish a permanent establishment. Preserve the amendment's actual wording and awkward cross-references; obtain an interpretation where they affect a result. The services duration is not an individual residence test. [Inserted s 3A, physical pp 2 to 4](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=2)

Unincorporated Business Tax Act, Cap. 18.46, ss 2 to 4 separately applies to persons carrying on business in the Federation, subject to its exclusions. Its business definition excludes employment. Companies **registered under the Companies Act, Cap. 21.03**, and partnerships treated as companies and liable under the Income Tax Act are excluded. Do not expand those words into an exemption for every entity called a company or into an ordinary wage charge. The separate payment-withholding branches in Income Tax Act ss 36 to 37 require their own conditions. Detailed rates, relief, withholding conflicts and later instruments remain in the linked references. [UBT ss 2 to 4, physical pp 5 to 6](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf#page=5) · [Income Tax Act ss 36 to 37, physical pp 35 to 39](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=35)

### 2. Tax residence

Inserted s 3A(4) defines a resident company by **management and control from within Saint Christopher and Nevis, regardless of its registration location**. Management and control is where the company's central mind, management and control is ordinarily situated. Incorporation, a registered office or an agent address alone does not establish that factual test. [Act 12 of 2021, physical p 2](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=2)

The inspected Cap. 20.22 s 2 definitions do not supply a general individual residence day count. Ordinary personal income is subject to s 3(3)'s exclusion; residence can still matter for a particular withholding, exemption, relief or representative provision. Section 36(5) defines non-residence for its withholding section by a person not residing in the Federation as determined under the Act. The management/control wording in the shipping exemption and the residence rule confined to Commonwealth double-tax relief serve their own provisions. Do not substitute either rule, or the permanent-establishment services test, for a universal individual residence test. [Definitions, physical pp 7 to 9](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=7) · [Shipping exemption, physical p 15](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=15) · [Section 36(5), physical p 37](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=37) · [Section 89(6), physical p 58](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=58)

### 3. Taxpayer types and representatives

Cap. 20.22 s 2 includes a body of persons within 'person' and distinguishes 'individual'. Its body definition includes specified incorporated and unincorporated bodies; its company definition includes locally and foreign incorporated or registered companies. Apply those tax definitions rather than assuming that a company-law label fixes every tax result. [Section 2, physical pp 7 to 9](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=7)

Part V, ss 19 to 29, retains spouse, deceased-person, partnership, trustee, non-resident representative and attribution machinery. Its partnership and representative rules address the person assessable, required information and income attribution under their conditions. Read them with s 3(3) before inferring a substantive charge. A representative's filing or payment duties do not automatically classify the underlying estate, trust or partnership as a company. [Part V, physical pp 27 to 30](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=27)

Cap. 18.46 s 3 includes a partnership and a firm within 'person'. Section 5(5) to (8) permits a one-time election for Income Tax Act computation, continuing thereafter, and deems the resulting tax corporate tax. Section 6 makes the partners jointly and severally liable and addresses the designated responsible partner. Check the s 2 company/qualifying-partnership exclusions before selecting that route. Keep legal form, substantive charge, income attribution, election and responsible filer as separate questions. [UBT ss 2 to 6, physical pp 5 to 7](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf#page=5)

Tax Administration and Procedures Act, Cap. 20.52, s 2 separately includes specified withholding payers and exempt persons required to submit returns in 'taxpayer'. An information or withholding obligation can therefore arise without proving that every receipt of that person is charged to ordinary income tax. [Administration ss 2 to 3, physical pp 7 to 8](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=7)

### 4. Currency

Cap. 20.52 s 20 makes tax within that Act's scope payable in **Eastern Caribbean dollars**. Sections 2 to 3 define its scope by covered tax laws and other taxes administered by Inland Revenue; 'tax law' excludes laws imposing customs or excise duty. Read the scope before applying its payment rule. Section 21 identifies statutory payment places or authorised recipients, and s 10(5) permits the specified electronic authorisation. Those provisions do not establish which bank, portal or institution is currently approved or accepts a payment. [Scope, physical pp 7 to 8](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=7) · [Electronic arrangements, physical p 10](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=10) · [Payment, physical p 12](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=12)

Customs Act, Cap. 20.04, s 262(b) separately permits its specified customs duties, rates, charges and drawback to be paid in any currency that is legal tender in the Federation. Do not apply Cap. 20.52 s 20 indiscriminately to Customs or every Social Security remittance. [Customs s 262, physical p 137](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_04-Customs-Act.pdf#page=137)

ECCB Act, Cap. 21.06, Schedule Article 17(1) names the monetary unit as the Eastern Caribbean Dollar divided into 100 cents. Articles 18 to 20 separately address issue, legal tender, coin limits, altered notes or coins and withdrawal. Section 4 requires a Ministerial Gazette-appointed date for the Articles' local force. The complete appointment chain has **not** been established here; the Act's own recorded in-force date does not independently prove that separate appointment. Describe the scheduled denomination with that qualification. Interpretation Act s 2's British West Indian Currency definition alone supplies no general modern 'dollar' definition. No live exchange rate, conversion method or accepted payment channel is established. [ECCB ss 2 to 4, physical p 5](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-21_06-Eastern-Caribbean-Central-Bank-Act.pdf#page=5) · [Articles 17 to 20, physical pp 21 to 22](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-21_06-Eastern-Caribbean-Central-Bank-Act.pdf#page=21) · [Interpretation s 2, physical pp 5 to 10](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-01_02-Interpretation-Act.pdf#page=5)

### 5. Assessment periods

Cap. 20.22 s 2 defines the assessment year as the 12 months beginning on 1 January. Section 4 ordinarily assesses the preceding basic year ending on 31 December, subject to ss 68 to 69. The Commissioners may permit another trade accounting date; the corresponding basis continues for later assessments and a change can require reasonable adjustments. Income of the basic year can remain assessable even if no income arises in the assessment year. Preserve the stated permission and adjustment conditions. [Definitions and s 4, physical pp 9 to 12](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=9)

The assessment year, income/basic year, permitted accounting date, instalment cycle and return deadline are distinct. Cap. 18.46 s 5 uses monthly goods and services bases; s 7 supplies a separate quarterly return and payment cycle. The linked guide preserves the conflict between statutory monthly floors and quarterly agency allowances. A filing example or a quarterly allowance does not redefine the income-tax basic year or settle that computation conflict. [UBT ss 5 to 7, physical pp 6 to 7](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf#page=6) · [Unincorporated business tax skill](kn-unincorporated-business-tax.md)

### 6. Responsible authorities and island allocation

The 31 December 2002 Inland Revenue Act, Cap. 20.23, ss 2 to 4 establishes Inland Revenue under ministerial supervision and provides for the Comptroller and officers. Its revenue definition excludes collection assigned to Customs. Its old Schedule is not an exhaustive list of taxes introduced later. Cap. 20.52 ss 46 to 47 separately provides for the Comptroller and the assessment, collection, accounting and administration functions within that Act. Income Tax Act s 38 addresses appointments under that Act, including assessment-appeal Commissioners. Use the relevant instrument's actor and function. [Inland Revenue ss 2 to 4, physical p 5](https://lawcommission.gov.kn/wp-content/documents/Act02and09TOC/Ch-20_23-Inland-Revenue-Act.pdf#page=5) · [Administration ss 46 to 47, physical pp 20 to 21](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf#page=20) · [Income s 38, physical p 39](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=39)

Customs Act ss 2 and 4 to 6 separately defines its department and Comptroller, assigns administration and addresses authorisation and delegation. That mandate does not make Inland Revenue the collector of every customs duty. Social Security Act, Cap. 22.10, s 3 establishes the Social Security Board; s 14 requires the Board to appoint its Director as chief executive officer. Keep those contribution authorities distinct from Inland Revenue and Customs. [Customs, physical pp 12 and 17 to 18](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_04-Customs-Act.pdf#page=12) · [Social Security Board, physical p 10](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf#page=10) · [Director, physical p 12](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf#page=12)

Income Tax Act ss 83 to 84 contains Federal Government/Nevis Island Administration corporate-tax allocation provisions tied to business activities on the relevant island and the stated attribution conditions. They do not allocate solely by registered-office location. Their text refers to their coming into force; the underlying commencement instruments have not been independently established here. Do not infer a live revenue allocation or an island exemption from this orientation. Detailed property, entity and island regimes require their specific instruments. [Sections 83 to 84, physical pp 55 to 56](https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf#page=55)

## Boundary and exception table

Manual source-selection checks, not executed tax returns.

| Fictional case | Required classification |
|---|---|
| Ordinary employee receives wages after 1 May 1980 | Apply s 3(3) before historical personal tax or PAYE machinery; check separate payroll levies and Social Security. |
| Foreign-incorporated company is managed and controlled from within the Federation | Test inserted s 3A(4)'s actual central mind, management and control facts; registration abroad alone does not establish non-residence. |
| A person provides services for 184 days | Identify whether the stated corporate permanent-establishment services branch and its full period/activity conditions apply; do not infer individual tax residence from this number alone. |
| An unincorporated partnership proposes an income-tax computation election | Check UBT s 2 exclusions, the one-time continuing election and resulting corporate-tax treatment, separately from partner liability and the responsible filer. |
| A covered Inland Revenue payment and a Customs payment are proposed in foreign currency | Distinguish Cap. 20.52 s 20 from Customs s 262; establish the actual authority, legal tender, conversion and accepted channel before payment. |
| A company selects a non-December accounting date | Obtain the relevant Commissioners' permission and apply the continuing basis and adjustment rules; distinguish the tax assessment year from its accounting period and filing deadline. |
| A Nevis registered office is offered as the only allocation fact | Establish actual island business activity and the ss 83 to 84 conditions and commencement; do not substitute the address for attribution evidence. |

## Worked cases

### Case 1: a foreign consultancy's 184-day engagement

A foreign company sends two consultants to a client in Saint Kitts. Their work there aggregates 184 days in a twelve-month period that ends in the fiscal year. The services limb of the permanent establishment definition needs more than 183 days: 184 is 1 day over, so a permanent establishment exists under that limb and the company is assessed on the income attributable to it (s 3A). The 183 days is not an individual residence test. Source: [Act 12 of 2021](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=2).

```oa-check
name: Saint Kitts and Nevis services permanent establishment test, 184 days
inputs:
  service_days: 184
  threshold_days: 183
steps:
  - days_over: max(0, service_days - threshold_days)
  - pe_under_services_limb: min(1, days_over)
expected:
  days_over: 1
  pe_under_services_limb: 1
```

### Case 2 (decision): a construction contract of seven months or of five months

A foreign contractor can either run a seven-month installation project, or deliver the same job in five months. Seven months is more than six, so the site is a permanent establishment and the profit attributable to it is assessed in the Federation. Five months is not more than six, so the construction limb is not met; the company then checks the other limbs (fixed place of business, dependent agent) before concluding there is no permanent establishment. The anti-fragmentation conditions stop a project being split into short contracts to stay under six months. Company tax rates are in [kn-corporate-income-tax](kn-corporate-income-tax.md). Source: [Act 12 of 2021](https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf#page=2).

```oa-check
name: Saint Kitts and Nevis construction permanent establishment, seven against five months
inputs:
  months_long: 7
  months_short: 5
  threshold_months: 6
steps:
  - pe_long: min(1, max(0, months_long - threshold_months))
  - pe_short: min(1, max(0, months_short - threshold_months))
expected:
  pe_long: 1
  pe_short: 0
```

## When to refuse or refer

- Refuse to give a liability, exemption or filing result from this skill alone: route to the topic skill in the Scope table.
- Refuse to apply a personal income tax to an individual's ordinary income: s 3(3) excludes income of persons other than companies accruing on or after 1 May 1980; check the levy, unincorporated business tax and social security instead.
- Refer company residence where management and control facts are mixed or disputed, and any permanent establishment question turning on the dependent and independent agent wording.
- Refer Federal and Nevis allocation questions (ss 83 and 84): the commencement instruments were not established.
- Refer any question that depends on law made after the source periods above.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 20.22, revised to 31 December 2017 (Law Commission PDF): read for s 2 definitions (year of assessment, company, body of persons), s 3 and its provisos (six months temporary purpose, partly offshore trades), s 3(3) (no charge on income of persons other than companies from 1 May 1980), s 4 basic year, Part V persons assessable, ss 36 to 38, ss 83 to 84 | https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_22-Income-Tax-Act.pdf | 2026-11-15 |
| Income Tax (Amendment) Act 2021, Act 12 of 2021 (Law Commission PDF): read for inserted s 3A (resident company, management and control, permanent establishment: more than six months for construction, more than 183 days for services) and the 26 March 2021 Gazette publication | https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/2021/ACTs/Act-12-of-2021-Income-Tax-Amendment-Act-2021.pdf | 2026-11-15 |
| Tax Administration and Procedures Act, Cap. 20.52 (Law Commission PDF): read for ss 2 and 3 (taxpayer and scope; customs excluded from tax law), s 20 (tax payable in Eastern Caribbean dollars), s 21, ss 46 and 47 | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf | 2026-11-15 |
| Unincorporated Business Tax Act, Cap. 18.46 (Law Commission PDF): read for ss 2 to 7 (business, exclusions for companies registered under Cap. 21.03, the election and partner liability, the monthly and quarterly cycles) | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_46-Unincorporated-Business-Tax-Act.pdf | 2026-11-15 |
| Customs Act, Cap. 20.04, revised to 31 December 2017 (Law Commission PDF): read for s 262(b) (payment in any currency being legal tender) and ss 2 and 4 to 6 | https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-20_04-Customs-Act.pdf | 2026-11-15 |
| Constitution of Saint Christopher and Nevis (Law Commission PDF): read for s 42(3) and (4), publication in the Gazette before a law comes into operation | https://lawcommission.gov.kn/wp-content/documents/Annual-Laws/The-Constitution-of-St-Christopher-and-Nevis.pdf | 2026-11-15 |
| Eastern Caribbean Central Bank Act, Cap. 21.06 (Law Commission PDF): read for Schedule Article 17(1), the Eastern Caribbean Dollar divided into one hundred cents | https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-21_06-Eastern-Caribbean-Central-Bank-Act.pdf | 2026-11-15 |
| Interpretation Act, Cap. 1.02 (Law Commission PDF): read for the s 2 British West Indian Currency definition | https://lawcommission.gov.kn/wp-content/documents/Revised-Acts-of-St-Kitts-and-Nevis/Revised-Acts-of-St-Kitts-and-Nevis-2017/Ch-01_02-Interpretation-Act.pdf | 2026-11-15 |
| Inland Revenue Act, Cap. 20.23, revised to 31 December 2002 (Law Commission PDF): read for ss 2 to 4, the Department, the Comptroller and the exclusion of collection assigned to Customs | https://lawcommission.gov.kn/wp-content/documents/Act02and09TOC/Ch-20_23-Inland-Revenue-Act.pdf | 2026-11-15 |
| Social Security Act, Cap. 22.10 (Law Commission PDF): read for s 3 (Social Security Board) and s 14 (Director) | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf | 2026-11-15 |

Source limits (from Ryan Duguid's review): The 2017 revisions, older Inland Revenue Act and separate 2021 amendment support this dated orientation. Selected complete definitions, charging, company residence, permanent-establishment, persons-assessable, period, currency and authority provisions were reconciled. The Constitution is used for the identified commencement inference. The retained Social Security Act supplies Board and Director provisions; it does not resolve the contribution-rate conflict in the separate guide. The framework covers the 6 orientation components without certifying all later legislation, relief, exemptions, detailed tax calculations or operational procedures. The ECCB appointment and income-tax island-allocation commencement chains remain qualified. Later corporate rates, ordinary withholding conflicts, UBT computation differences, Social Security charging bridges, incentives and actual filing or payment conditions remain in their respective topics. Professional review is pending.

Not yet confirmed: amendments after 31 December 2017 (and after Act 12 of 2021) to the provisions cited; operation of Act 12 of 2021 from 26 March 2021 (inferred from assent and Gazette publication with Constitution s 42, no commencement clause); the ECCB Agreement appointment chain; the commencement of the Federal and Nevis allocation provisions (ss 83 and 84); accepted payment channels and conversion.
