---
name: nl-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Netherlands tax returns AND mentions freelancing, self-employment, ZZP, eenmanszaak, or sole proprietorship. Trigger on phrases like "help me do my taxes", "prepare my IB-aangifte", "I'm a ZZP'er in the Netherlands", "I'm a freelancer in the Netherlands", "do my taxes as a contractor", "prepare my BTW return and income tax", or any similar phrasing where the user is a Netherlands-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Netherlands self-employed tax workflow -- every other skill in the stack (nl-btw-return, nl-income-tax, nl-zvw, nl-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Netherlands full-year residents only; self-employed individuals and sole proprietors.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-28
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands freelance tax intake — 2025 returns and 2026 records

## Scope and who this is for

Figures are for tax year 2025 or tax year 2026 as explicitly labelled; do not mix columns.

Use this intake to collect and assess the records of a full-year Netherlands-resident individual working on their own account, including someone with employment alongside an eenmanszaak. It prepares a documented handoff; it does not calculate a complete return or submit anything. Being called a freelancer or ZZP'er, having a trade registration, or sending invoices does not settle income-tax entrepreneur status. Assess the actual activity. [Income sources and entrepreneur assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/)

Keep the income year separate from the year in which a return is prepared. This method distinguishes 2025 returns from 2026 records and estimates. The annual deduction sources differ. Future announcements are not inputs to either year's calculation. [2025 deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026 deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)

For a company, partnership allocation, migration, non-residence, overseas establishment, disputed worker status, death or business transfer, collect useful records but refer the affected analysis. Do not omit an out-of-scope item and describe the remaining package as a complete personal return. This is a workflow boundary, not a claim that those taxpayers cannot qualify for relief.

## Ask the client first

Ask related questions together, reuse answers already supported by documents, and mark assumptions explicitly. Use the available interface; no particular question tool is required.

- Which income year, which tax or return, and what is the requested output? Obtain the invitation, assessment, extension confirmation and correspondence showing the actual filing/payment position.
- Where did the person live and work during that year? Did residence, legal form, ownership or business activity change?
- Which activities and clients generated income? Which work was employment, independently contracted work, or a private activity? Obtain contracts and the facts of how the work was performed, not only the contract title.
- Is there employment income or a pension as well? Obtain annual statements and the time spent on other work.
- What is the legal form? Record registration details as evidence of form, not proof of tax eligibility.
- What is the VAT position, including the authority's KOR start/end confirmation and periods for which a return is ready? A zero-VAT invoice alone does not establish KOR participation. [KOR conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden) [KOR effects](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)
- What records support business hours, profit, investments, private use, prior relief and carryforwards? Unknown does not mean zero or ineligible.
- Is there a possible fiscal partner, jointly occupied property, children, annuity contributions, personal assets, foreign income or another tax matter? Capture dates and documents for separate assessment; do not infer fiscal partnership from a casual description of the relationship. [Fiscal partnership](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap)

## The method, step by step

1. Establish the income route before relief using the evidence and conditions below.
2. Collect the records and reconcile them using the evidence and conditions below.
3. Gather eligibility evidence without pre-awarding deductions using the evidence and conditions below.
4. Handle personal and mixed-use issues separately using the evidence and conditions below.
5. Produce a usable handoff using the evidence and conditions below.

### Step 1: Establish the income route before relief

For each activity, record whether it participates in economic activity outside the private sphere and whether profit can reasonably be expected. Then consider independence, capital, scale and time, customers, outward presentation, commercial risk and liability. Related activities can form a single income source only where their connection supports that conclusion. Document the evidence and any contrary facts. There is no automatic entrepreneur verdict from registration or a fixed customer-count shortcut. [Entrepreneur assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/)

Assess employment per engagement with the client: actual control, personal work and remuneration, viewed with all the circumstances. Examine working arrangements, integration into the client's organisation, duration, ability to substitute, how agreements and pay are set, commercial risk and outward entrepreneurship. A replacement clause or multiple customers is not a standalone safe harbour. Even an engagement outside employment does not automatically establish income-tax or VAT entrepreneurship. Unresolved employment classification requires specialist review before treating the remuneration as business profit. [Employment assessment](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/wanneer-is-sprake-van-loondienst)

Where there is taxable independent work but no income-tax enterprise, route it to income from other work (resultaat uit overige werkzaamheden). Business-profit relief cannot simply be carried across. VAT entrepreneur status is a separate assessment. Employment can coexist with a genuine business; classify the income streams rather than forcing the whole person into a single label. [Income-source distinctions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [Consequences of employment](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/werken-in-loondienst-gevolgen-opdrachtnemer)

### Step 2: Collect the records and reconcile them

Request the records needed for the agreed scope, then identify gaps:

| Record | Extract and check |
| --- | --- |
| Sales invoices, credit notes, contracts and receivables | Activity, customer, supply period, amount and VAT treatment; reconcile receipts and outstanding balances |
| Bank and payment-processor statements | Match transactions to evidence; separate loans, transfers, capital introduced, private withdrawals, refunds and business receipts |
| Purchase invoices, receipts and asset register | Business purpose, amount, recoverable VAT, private share, asset/cost distinction, commitment/payment/first-use dates |
| Bookkeeping and prior accounts | Opening balances, accruals, stock, assets, liabilities and continuity from the preceding year |
| Filed returns and assessments | Income year, tax type, submitted amounts, credits, provisional assessments, paid/refunded amounts and unresolved correspondence |
| Hours records | Actual business work and other work, dated activities, supporting calendars, invoices and quotations |
| Earlier relief decisions | Year-by-year entrepreneur status and zelfstandigenaftrek use; unused amounts and utilisation; any tax-neutral return from a company |
| Personal records relevant to scope | Employment statements, partner facts, property/loan documents, pension/annuity statements and private asset records; send to the relevant method |

A bank description is a clue, not a final tax classification. Revenue is not simply all deposits; expenditure is not automatically deductible. Apply the business-purpose test and separate private expenditure and capital assets. Recoverable VAT is excluded from income-tax costs; irrecoverable VAT can form part of an otherwise allowable cost or asset basis, subject to the same restrictions. [Business costs](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten) [Investment timing](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen)

Keep VAT and income-tax decisions separate. KOR affects VAT charging, routine returns and input recovery; it is not an exemption from income tax. KOR participation has effective dates and exceptional VAT-return situations. Reconcile VAT turnover to the income-tax records with explanations for differences, rather than forcing a VAT box to equal business profit. Use the current `nl-vat-return` or `netherlands-vat-return` Guide for VAT preparation. [KOR effects](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)

### Step 3: Gather eligibility evidence without pre-awarding deductions

The ordinary hours test requires at least 1,225 business hours in the calendar year, without reducing the threshold for a late start or early stop. Usually business time must also exceed other working time; that additional comparison does not apply if the person was not an entrepreneur in at least one of the preceding five years. Record both tests, rather than asking only for a yes/no hours assertion. [Hours criterion](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

Count actual business work, including administration, quotations and the business website; keep supporting evidence. Mere availability does not count. Do not invent hours or categorically exclude all business travel without assessing the work and evidence. Pregnancy interruption has a specific allowance for 16 weeks; related-person partnerships have exclusions, including unusual arrangements with at least 70% supporting activities. Refer disputed or exceptional hours rather than resolving them through a guessed buffer. [Hours evidence and exceptions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium)

For starter relief, obtain the preceding five years' entrepreneur status and independently established use of zelfstandigenaftrek, plus any relevant company-to-business return. A registration date or the number of times someone remembers claiming startersaftrek is not enough. Use `nl-zzp-deductions` to compute the result once the evidence is sufficient. [Starter conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek)

Keep an existing FOR reserve and unused zelfstandigenaftrek as separate ledgers. No new FOR reserve may be formed from 2023 onward. Existing reserves have release conditions, including circumstances while the business continues; do not default an unknown balance to nil. Unused zelfstandigenaftrek may be carried forward under its own conditions and requires assessment records. [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve) [Unused deduction](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek)

### Step 4: Handle personal and mixed-use issues separately

Home-office relief is exceptional. A separate entrance alone does not prove entitlement; record independence, facilities, use, other workspace and ownership/asset classification. Do not allocate a percentage of household rent or mortgage automatically. Use the authority's workspace tool or refer. [Home workspace](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/werkruimte_in_de_woning)

For fiscal partnership, collect the underlying facts and dates. Only specified common income and deductions can be allocated; business profit and employment income remain the person's own. Do not propose freely transferring tax credits or wage withholding between partners. Specified common items and dividend withholding have their own allocation rules. [Fiscal partnership and allocation](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap)

### Step 5: Produce a usable handoff

Return a short client summary and an evidence ledger. For each relevant fact include the income year, document or answer, amount if known, status (`supported`, `client-stated`, `estimated`, `missing`, `disputed`), and the calculation or decision it affects. Use explicit unknown values; never seed missing amounts with zero or eligibility with true.

The handoff must distinguish:

- facts collected from tax conclusions reached;
- business-source and employment conclusions from VAT registration;
- reconciled profit inputs from relief still awaiting evidence;
- current-year figures from historical carryforwards;
- work ready to calculate from matters requiring clarification or referral.

Record a remaining action, owner and consequence for every material gap. Continue independent record reconciliation while a gap is resolved, but do not mark dependent figures ready to file. Client confirmation corrects facts; it does not validate the tax treatment.

## Figures by year

These are routing checks, not prefilled awards. [2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026) [MKB exemption](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

| Item | 2025 | 2026 |
| --- | --- | --- |
| Ordinary zelfstandigenaftrek before pension-age adjustment, where eligible ([2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025), [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)) | €2,470 | €1,200 |
| Standard startersaftrek supplement, where eligible | €2,123 | €2,123 |
| MKB profit exemption after ondernemersaftrek | 12.7% | 12.7% |
| Ordinary business-hours threshold | 1,225 hours | 1,225 hours |

The hours threshold does not itself establish entrepreneur status. The MKB exemption has no hours-test condition but requires qualifying enterprise profit and also reduces an enterprise loss. Details, age adjustments and limitations belong in the deductions method. [Hours](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium) [MKB exemption](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)

## Boundary and exception table

| Situation | Intake action |
| --- | --- |
| Registered business, insufficient evidence of independent commercial activity | Leave entrepreneur status unresolved; do not award relief from registration alone |
| Established entrepreneur below the hours threshold | Keep business classification if otherwise supported; assess relief individually |
| Work labelled freelance but performed under possible employer control | Document actual arrangements and refer classification |
| No VAT on invoice | Determine reason: KOR, exempt supply, reverse charge or another rule; obtain evidence |
| A business bank payment to the tax authority | Match tax type, year and notice before treating it as a payment against liability |
| Business and employment alongside each other | Separate streams and compare hours where required |
| Home office without enough facts | Do not infer allowable costs from floor area alone |
| Missing old FOR or deduction decisions | Request records; mark the opening balance unknown |

The decisions above follow the cited source assessments; they are not presumptions of wrongdoing.

## Worked cases

These are illustrative decision checks, not client determinations.

- **Registration without proof:** a registered sole trader uploads a contract but nothing about actual control or commercial risk. Result: legal form recorded, entrepreneur and employment conclusions still open; no relief awarded from registration alone. [Assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/) [Employment](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/wanneer-is-sprake-van-loondienst)
- **Late start:** an established income-tax entrepreneur starts mid-year and has fewer than 1,225 evidenced business hours. Result: do not prorate the threshold or award ordinary zelfstandigenaftrek; retain the separate MKB assessment. [Hours](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium) [MKB](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling)
- **No VAT charged:** the invoice says VAT is reverse-charged; no KOR confirmation exists. Result: do not infer KOR. Record the actual VAT basis and obtain the relevant return/registration evidence. [KOR conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden)
- **An old reserve:** the client requests a new FOR contribution for 2026 and cannot find the prior balance. Result: no new contribution; request the historical ledger and assess any existing reserve's release conditions separately. [FOR](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve)
- **Filing-year confusion:** preparation takes place in 2026 for the 2025 income year. Result: use the 2025 deduction source and data; do not substitute the 2026 allowance. [2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025) [2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026)

## When to refuse or refer

- Pause the affected tax conclusion for unresolved source-of-income or employment status, foreign residence/work, company or partnership allocations, a disputed hours record, inherited business, cessation, historic reserve conversion, or a specialist personal-tax issue. Do not turn the employment-enforcement transition into a promise of immunity: normal enforcement resumed in 2025 and deliberate/default penalty treatment differs in 2026. [Enforcement](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/handhaving)

Downstream Guides are inputs to inspect, not permission to import stale figures. Before using `nl-income-tax`, `nl-deductions` or `nl-return-assembly`, check the actual year and each relevant source. If a dependent method conflicts with this evidence or remains unreviewed, retain the handoff and isolate that calculation; do not claim the complete return is ready.

## Completion checklist

- [ ] Income year, scope, legal form, residence and actual notices recorded.
- [ ] Income source, employment and VAT assessments separated.
- [ ] Every material amount tied to evidence, reconciliation or an explicit missing-data flag.
- [ ] Hours and starter history collected without presumed eligibility.
- [ ] No new FOR addition and no unknown opening balance silently treated as nil.
- [ ] Personal deductions, partner allocation and mixed-use issues routed separately.
- [ ] Correct-year deduction method selected; unresolved dependencies remain visible.
- [ ] Handoff identifies what is ready, what is provisional and what needs specialist review; no submission implied.

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
