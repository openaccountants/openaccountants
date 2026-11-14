---
name: pk-formation
description: Use for pakistan business formation and entity selection. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: decision
---

# Pakistan business formation and entity selection v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Choose the entity from ownership, liability, governance, funding, profession and licensing facts. PSEB tax treatment is a separate eligibility test: a qualifying sole proprietor can use the export regime, so incorporation is not automatically the route to the lower rate. This 2026 formation skill uses the current available Companies Regulations 2024 consolidation reviewed 14 April 2026; tax examples expressly concern normal tax year 2026 (1 July 2025-30 June 2026).

## Ask the client first

Obtain founder count, individual/corporate identity and nationality/origin, residence, beneficial ownership/control chain, sector and professional restrictions, actual establishment/registered-office province, expected turnover/profits, capital/reserves, staffing, domestic/export split, clients' contracting requirements, limited-liability needs, co-founder/equity/IPO plans, charitable intent, budget and timing. Obtain existing business/reconstitution history, foreign investment/repatriation/visa needs and any licence/NOC. Do not turn a turnover estimate or desire for tax savings into the sole recommendation.

## The options

| Vehicle | Main fit and trade-off | Legal boundary/source |
|---|---|---|
| Sole proprietor | Single owner accepting personal liability and direct income-tax compliance; separate commercial records/banking evidence still needed | Income owner `pk-income-tax`; not SECP incorporation |
| General partnership/AOP | Genuine partners sharing business/profits and accepting partnership liability; documented deed, provincial Registrar of Firms/stamp/registration and separate tax identity need actual local law | Detailed Partnership Act 1932 s.69 enforcement/registration route remains to be confirmed; no assumed province form |
| LLP | Separate SECP LLP route for professional/partner governance and liability needs; do not assume company forms, liability exceptions or AOP tax classification without LLP law | LLPAct 2017/regulations and tax classification pending confirmation |
| SMC private company | Genuine single owner wanting corporate contracting/liability structure |1 member, minimum 1 director; statutory nominee/trustee role. [Act ss.14/154](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422) |
| Other private company | Multiple genuine owners, restricted share transfer, private capital | At least 2 members/2 directors; maximum 50 members excluding current employees, joint holders count as 1; no public subscription invitation. [ss.2(49)/14/154](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422) |
| Public unlisted/listed company | Public-capital/listing and governance needs; public incorporation is not itself PSX listing permission | At least 3 members;3 directors unlisted,7 listed; natural-person directors and public-interest female-representation rules. [ss.14/154](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422) |
| Section 42 company | Genuine nonprofit objects with licence, public-company governance and no private distribution | SECP licence before incorporation; use actual licence/Regulations 98-100, no automatic income-tax exemption. [Regulations 18/98-100](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf) |
| Trust/society | Genuine trust/association objects and local registration/governance | Provincial trust/charity and Societies Registration Act route, member/trustee counts and forms require separate law; do not reuse company incorporation forms |

The more-than 20-person gain-seeking association/partnership incorporation rule comes from **Companies Act s.9**, not Partnership Act s.4. Its exceptions include statutory bodies/associations other than partnerships, joint family, the specified joint-family partnership count, and professions that cannot practise as limited companies. Do not force an accountant/lawyer partnership into a prohibited company form. [s.9(1),(3)](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422).

## Rates, bands and thresholds

| Rule with conditions | Confirmed figure | Official source |
|---|---|---|
| Company name availability |60 days from availability letter; file incorporation within that period | [Regulation 3(2)-(3)](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf) |
| Registered office notification | Within 30 days of incorporation; change within 15 days, with specified intercity/province approvals | [Act s.21](https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422) |
| SMC nominee | Spouse, father, mother, brother, sister, son or daughter; nominee is not an invented second shareholder | [Form 1 para 2.11; regulation 17](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf) |
| UBO | At least 25% shares/votes or effective control, direct/indirect; trace legal-person chains with senior-manager fallback where no natural person identified | [Regulation 13(2)-(3), explanation](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf) |
| Section 42 member liability and startup donation | Member liability at least 200,000; **each promoter** startup donation at least 200,000 or required notified amount; nominating entity/government/body pays instead in the specified representative case | [Regulation 100(1)(iv)-(v)](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf) |
| Normal tax-year 2026 nonbank company headline |29%; qualifying statutory small company 20%, before separate adjustments/levies | [ITO First Schedule Part I Div II](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Statutory small-company test | Registered from 1 July 2005; paid-up capital plus undistributed reserves≤50,000,000; employees≤250 **at any time** in year; annual turnover≤250,000,000; no split/reconstitution of existing company; not s.2(59 A)SME | [ITO s.2(59 AB)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Qualifying services export |0.25% for PSEB-registered/certified qualifying IT/ITeS in tax years 2024-2026;1% other qualifying s.154A proceeds, with final-tax conditions/opt-out | [ITO s.154A; First Schedule Part III Div IVA](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf); `pk-it-export-tax` |

Do not substitute Companies Act small-sized financial-reporting thresholds for the **different income-tax small-company test**. Neither small-company headline 20% nor export 0.25% is an all-inclusive effective-tax promise. Section 113 minimum tax, s.113C alternative corporate tax, s.4C supertax, distributions/withholding, provincial tax and eligibility exclusions require their owner computations and actual period. The already approved `pk-corporate-tax` is not rewritten by this skill.

## The method, step by step

1. Screen foreign involvement, prohibited/restricted sector, real beneficial owner and professional rules first. Stop a green-light recommendation for restricted/regulated activity until the actual licence/NOC and foreign-investment rules are established. Do not use nominee shares to conceal ownership.
2. Separate nonprofit intent from a commercial profit-distributing business. Assess Section 42/trust/society with actual licensing/local law. Do not promise tax-free trading from charitable registration; ITO s.2(36)/s.100C and specific Schedule relief need their own conditions.
3. For public-funding/listing plans consider the public-company route and separate offering/PSX approvals. The old 3 year IPO horizon is a planning input, not a statutory trigger.
4. For genuine professional partners compare partnership/LLP/company only where professional law permits. For a solo owner compare proprietor and SMC; for genuine multiple founders compare private company and permitted partnership/LLP. A private company is not compelled merely by turnover, and a fictitious 1 share co-founder is not a solution for a solo owner.
5. For IT/ITeS exports test PSEB registration/certification and bank-realisation evidence alongside any entity. Pure domestic/nonqualifying services do not gain export relief. Separate domestic service income and provincial tax; PSEB does not itself create a provincial exemption or STZA holiday.
6. Compare actual compliance cost, liability/guarantees, client requirements, funding, exit and ownership changes as well as tax. Explain assumptions and outstanding licences/base-year law before the founder chooses.

## Formation and follow-through

For a company, confirm name/activity and any restricted word approval; prepare the correct memorandum/articles, capital/classes and genuine subscribers/directors/CEO details, CNIC/NICOP/passports, nominee where SMC, UBO information, office/correspondence and required licence/NOC. Regulation 8 allows separate or combined name/incorporation applications using **Form 1** with its actual enclosures. Electronic and physical branches differ. Pay the actual current Seventh Schedule fee, resolve deficiencies and retain the incorporation certificate/CUIN. The old standalone Form 21/Form 29/INC.8 checklist is not cleared as the current incorporation package. [Regulations 3/8/12-17; Form 1](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf).

Foreign corporate subscribers require profile/constitution/incorporation/board-authorisation and authentication documents; foreign individuals require identity/biodata/undertaking, with nationality/origin/security-clearance branches under regulation 19. Do not promise all cases incorporate before clearance or that all foreign investments need a universal BOI permit/USD 150,000 capital floor. Bank KYC, SBP foreign exchange/repatriation and work visa permissions are separate and need actual current sources. [Regulation 19](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf).

After incorporation verify actual FBR tax registration/linkage, separate business bank requirements, federal goods/provincial services registration, withholding and payroll/social-security coverage, local professional/trade/municipal registrations and sector licences. Do not promise automatic NTN within 1-3 days, bank attendance,4-10 day incorporation,2-4 week PSEB approval or 5-10 day STRN issuance. The actual PSEB documents/fees/renewal calendar require the current official procedure; the tax condition itself is sourced above.

Keep statutory registers, minutes/resolutions, ownership/charge/nominee and office changes, accounting records, return and financial-statement calendar. Form A's instructions provide 30 days from its relevant date and specific no-change branches; SMCs/private companies with paid-up capital≤3,000,000 and no changed particulars have an exception, while other no-change cases use the stated Form 24 route. Do not say every company files the same annual form regardless of facts. [Form A instructions 4-7](https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf). Load `pk-financial-statements` to separate accounting size, audit and filing thresholds; SMC is not a universal audit exemption.

Income-tax ordinary dates under s.118 differ from SECP dates: individual/AOP 30 September; company with tax year ending January-June 31 December, otherwise 30 September, subject to an actual extension. Load `pk-return-assembly`; do not treat the ordinary date as confirmed actual extended 2026 date. [ITO ss.118/119](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Worked cases

### Bilal's original Lahore case, preserved and corrected

Bilal is Pakistani,28, a solo Lahore software developer, no employees/home office, expected tax-year 2026 revenue 30,000,000,90% US/EU exports and 10% Lahore SME. He wants corporate substance and is cost-conscious. His brother falls within the permitted SMC nominee relationships; the nominee/trustee role does not make the brother a second equity owner. “Bilal Tech Solutions (SMC-Private) Limited” remains a proposed name subject to approval. Assumed 100,000 share capital is a planning input, not a sourced statutory floor.

Assume all export 0.25% conditions are independently met and supported domestic deductible costs are 1,500,000. The earlier domestic 1,500,000 taxable profit was given; do not let those costs reduce final-tax export proceeds as well.

```oa-check
name: Bilal proprietor export and domestic split
inputs:
  total_revenue: 30000000
  export_fraction: 0.9
  domestic_costs: 1500000
steps:
  - export_revenue: total_revenue * export_fraction
  - domestic_revenue: total_revenue - export_revenue
  - domestic_taxable_profit: domestic_revenue - domestic_costs
  - export_tax: export_revenue * 0.0025
  - domestic_individual_tax: 90000 + (domestic_taxable_profit - 1200000) * 0.20
  - combined_before_other_charges: export_tax + domestic_individual_tax
expected:
  export_revenue: 27000000
  domestic_revenue: 3000000
  domestic_taxable_profit: 1500000
  export_tax: 67500
  domestic_individual_tax: 150000
  combined_before_other_charges: 217500
```

```oa-check
name: Bilal company headline comparison conditional on full small-company test
inputs:
  qualifying_export_revenue: 27000000
  domestic_taxable_profit: 1500000
  proprietor_headline: 217500
steps:
  - export_tax: qualifying_export_revenue * 0.0025
  - domestic_company_headline_tax: domestic_taxable_profit * 0.20
  - company_headline_before_other_charges: export_tax + domestic_company_headline_tax
  - headline_difference: company_headline_before_other_charges - proprietor_headline
expected:
  export_tax: 67500
  domestic_company_headline_tax: 300000
  company_headline_before_other_charges: 367500
  headline_difference: 150000
```

These 217,500/367,500 headlines are **not final entity tax bills**: test minimum/alternative/super tax, expense allocation, actual credits, salary/distributions and compliance costs before choosing. The old 480,000 Punjab service-tax output,15%/7.5% dividend planning and 5-15 K/30-60 K formation-cost ranges are not cleared here. Bilal's actual Punjab service category/rate must be established. Director salary needs real services, company deduction rules and s.149 payroll; a tax-efficient label is not enough. If clients accept a proprietor, simplicity may prevail; limited liability/contracts can still justify SMC. A genuine incoming co-founder needs proper ownership/conversion advice, not a nominee share shortcut. The old 10,000,000 sole-proprietor suitability cutoff is planning-only and not a legal threshold.

## When to refuse or refer

Keep all original referral groups: foreign/negative-list investment and repatriation; banking/insurance/NBFC/capital-markets/modaraba; telecom/broadcasting; pharmaceutical/food/cosmetics/devices; oil/gas/power/mining; aviation/shipping; construction/PEC; healthcare/profession; STZA incentives; privacy/data-processing regulation; trusts/societies/NPO private-benefit risk; intricate ownership/exit, pre-existing debts and aggressive dividend/salary schemes. The named regulators are signposts requiring the operative approval, not proof of present eligibility. No green light for a regulated activity from an incorporation certificate alone.

## Completion checklist

Genuine owners/control and profession checked; entity choice explained beyond tax; actual licence/foreign/NPO conditions cleared; name/documents/capital/nominee correct; fees sourced at filing; certificate/tax/banking evidence retained; domestic/export treatment separated; SECP/accounting/audit/tax/payroll calendars assigned; outstanding matters explicit.

For the actual tax-year-2026 filing cycle, FBR Circular 04 of 2026-27 dated 15 October 2026 extends the filing date to **31 October 2026** for persons originally due 30 September 2026 and previously extended to 15 October. It does not extend every company return. Apply any individual further order only on its evidence; this circular does not itself state a general payment extension. [Official circular](https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf), read and scanned page inspected 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Companies Act 2017 ss.2(49),9,14/16,21/22 and 154, including adjacent conditions | https://www.secp.gov.pk/document/the-companies-act-2017-updated-18-aug-2022/?refresh=6991a886a9e0e1771153542&wpdmdl=45422 | 2026-11-14 |
| Read for Companies Regulations 2024 rr 3,8,12-19,99/100; Form 1 nominee/documents and Form A instructions; UBO explanation in r 13 | https://www.secp.gov.pk/wp-content/uploads/2026/04/Companies-Regulations-2024-updated-upto-25.07.2025-Reviewed-14042026.pdf | 2026-11-14 |
| Read for ITO s.2(59 AB), s.154A/First Schedule Div IVA, company Part I Div II and ordinary return dates; individual computation owned by `pk-income-tax` | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: provincial proprietor/partnership/trust/society forms/stamps/counts/enforcement, LLP liability/tax/registration, sectoral capital floors and licences, PSX free-float/independence/CFO rules, ordinary no-floor capital claim, secretary/CEO/AGM/director-election and conversion timings beyond the read provisions, complete NPO/s 100 C/PCP relief, current PSEB procedures/fees/renewals/incentives, foreign-investment/BOI/SBP/visa requirements, all formation service-cost/timing claims, complete tax 113/113 C/4 C/distribution result and each later 2026 change. Preserve these old subjects as explicit pending work; no unsourced operational amount is supplied.
