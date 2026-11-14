---
name: nl-freelance-intake
description: "ALWAYS USE THIS SKILL when a user asks for help preparing their Netherlands tax returns AND mentions freelancing, self-employment, ZZP, eenmanszaak, or sole proprietorship. Trigger on phrases like \"help me do my taxes\", \"prepare my IB-aangifte\", \"I'm a ZZP'er in the Netherlands\", \"I'm a freelancer in the Netherlands\", \"do my taxes as a contractor\", \"prepare my BTW return and income tax\", or any similar phrasing where the user is a Netherlands-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Netherlands self-employed tax workflow, and every other skill in the stack (nl-vat-return, nl-income-tax, nl-zzp-deductions, nl-social-contributions, nl-return-assembly) depends on this skill running first to produce a structured intake package. Uses an upload-first workflow, where the user shares all their documents and the skill infers as much as possible before asking grouped questions. Built for speed. Netherlands full-year residents only"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-freelance-intake"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Netherlands freelance tax intake: 2025 returns and 2026 records

## Scope and who this is for

Tax year 2026, with the 2025 return (being prepared now) labelled separately. Figures are for tax year 2025 or tax year 2026 as explicitly labelled; do not mix columns.

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

## Rates, bands and thresholds

These are routing checks, not prefilled awards. The computation belongs to `nl-zzp-deductions`.

| Item | 2025 | 2026 | Condition | Source |
| --- | --- | --- | --- | --- |
| Ordinary zelfstandigenaftrek, 2025 | EUR 2,470 | | Entrepreneur, meets the hours test, below AOW age at 1 January; capped at profit before ondernemersaftrek unless the startersaftrek applies; 50% at AOW age | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 |
| Ordinary zelfstandigenaftrek, 2026 | | EUR 1,200 | Same conditions | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026 |
| Startersaftrek supplement | EUR 2,123 | EUR 2,123 | Not an entrepreneur in 1 or more of the 5 preceding years and zelfstandigenaftrek used no more than twice in that period | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek |
| MKB profit exemption, share of profit after ondernemersaftrek | 12.7% | 12.7% | Qualifying enterprise profit; no hours test; also reduces a loss | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling |
| Ordinary business-hours threshold | 1,225 hours | 1,225 hours | Calendar year, not prorated; usually also more than half of working time unless not an entrepreneur in 1 of the 5 preceding years | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium |
| Pregnancy interruption counted as hours | 16 weeks | 16 weeks | Interruption of work as entrepreneur through pregnancy | same |
| Unused zelfstandigenaftrek carry-forward | 9 years | 9 years | Only against later profit above that year's zelfstandigenaftrek | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 |

The hours threshold does not itself establish entrepreneur status. The MKB exemption has no hours-test condition but requires qualifying enterprise profit and also reduces an enterprise loss. Details, age adjustments and limitations belong in the deductions method (`nl-zzp-deductions`).

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

Keep VAT and income-tax decisions separate. KOR affects VAT charging, routine returns and input recovery; it is not an exemption from income tax. KOR participation has effective dates and exceptional VAT-return situations. Reconcile VAT turnover to the income-tax records with explanations for differences, rather than forcing a VAT box to equal business profit. Use the current `nl-vat-return` skill for VAT preparation. [KOR effects](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)

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

### Handoff sanity check (2026)

Once the evidence supports entrepreneur status, the hours test and no starter relief, the deductions skill should return these figures for a 2026 profit of EUR 50,000. The intake uses this only to check that the handoff reached the right year's figures (EUR 1,200, not the 2025 EUR 2,470).

```oa-check
name: Handoff check, 2026 profit 50000, ordinary zelfstandigenaftrek, no starter
inputs:
  profit: 50000
  zelfstandigenaftrek: 1200
steps:
  - after_ondernemersaftrek: profit - zelfstandigenaftrek
  - mkb_exemption: after_ondernemersaftrek * 0.127
  - taxable_profit: after_ondernemersaftrek - mkb_exemption
expected:
  after_ondernemersaftrek: 48800
  mkb_exemption: 6197.60
  taxable_profit: 42602.40
```

## When to refuse or refer

- Pause the affected tax conclusion for unresolved source-of-income or employment status, foreign residence/work, company or partnership allocations, a disputed hours record, inherited business, cessation, historic reserve conversion, or a specialist personal-tax issue. Do not turn the employment-enforcement transition into a promise of immunity: normal enforcement resumed on 1 January 2025 (back-assessments no earlier than 1 January 2025 unless bad faith); no penalties were imposed in 2025, and from 1 January 2026 the Belastingdienst can impose penalties for intent or gross fault (vergrijpboetes) but not yet default penalties (verzuimboetes). [Enforcement](https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/handhaving)

Downstream Skills are inputs to inspect, not permission to import stale figures. Before using `nl-income-tax`, `nl-deductions` or `nl-return-assembly`, check the actual year and each relevant source. If a dependent method conflicts with this evidence or remains unreviewed, retain the handoff and isolate that calculation; do not claim the complete return is ready.

## Completion checklist

- [ ] Income year, scope, legal form, residence and actual notices recorded.
- [ ] Income source, employment and VAT assessments separated.
- [ ] Every material amount tied to evidence, reconciliation or an explicit missing-data flag.
- [ ] Hours and starter history collected without presumed eligibility.
- [ ] No new FOR addition and no unknown opening balance silently treated as nil.
- [ ] Personal deductions, partner allocation and mixed-use issues routed separately.
- [ ] Correct-year deduction method selected; unresolved dependencies remain visible.
- [ ] Handoff identifies what is ready, what is provisional and what needs specialist review; no submission implied.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Belastingdienst, when are you an entrepreneur for income tax | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/ | 2026-11-14. Read for the entrepreneur criteria (independence, capital, size and time, customers, risk) and the other-work route |
| Belastingdienst, zelfstandigenaftrek 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 | 2026-11-14. Read for EUR 2,470, the profit cap, startersaftrek EUR 2,123, the 9-year carry-forward and the AOW-age halving |
| Belastingdienst, zelfstandigenaftrek 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026 | 2026-11-14. Read for EUR 1,200 in 2026 and startersaftrek EUR 2,123 |
| Belastingdienst, startersaftrek | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek | 2026-11-14. Read for EUR 2,123 and the 5-preceding-years and BV-return conditions |
| Belastingdienst, MKB profit exemption | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling | 2026-11-14. Read for 12.7% in 2025 and 2026 of profit after ondernemersaftrek |
| Belastingdienst, hours criterion | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium | 2026-11-14. Read for 1,225 hours, the more-than-half test and its 5-year exception, 16 weeks pregnancy, availability not counting, the 70% supporting-work exclusion |
| Belastingdienst, KOR conditions | https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden | 2026-11-14. Read for KOR participation conditions |
| Belastingdienst, what joining the KOR means | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling | 2026-11-14. Read for the KOR effects on invoicing, returns and input VAT |
| Belastingdienst, fiscal partnership 2026 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/fiscaal_partnerschap | 2026-11-14. Read for who is a fiscal partner and which common items can be allocated |
| Belastingdienst, when is there employment | https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/wanneer-is-sprake-van-loondienst | 2026-11-14. Read for the employment tests (authority, personal work, pay) and the circumstances weighed |
| Belastingdienst, consequences of employment for the contractor | https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/werken-in-loondienst-gevolgen-opdrachtnemer | 2026-11-14. Read for the income-tax consequences when work is employment |
| Belastingdienst, enforcement of working relationships | https://www.belastingdienst.nl/wps/wcm/connect/nl/arbeidsrelaties/content/handhaving | 2026-11-14. Read for the end of the moratorium on 1 January 2025, no penalties in 2025, vergrijpboetes possible from 2026 |
| Belastingdienst, business costs | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/zakelijke_kosten | 2026-11-14. Read for the business-purpose test for costs |
| Belastingdienst, investment scheme conditions | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/investeringsaftrek_en_desinvesteringsbijtelling/voorwaarden_investeringsregelingen | 2026-11-14. Read for commitment, payment and first-use timing of investments |
| Belastingdienst, oudedagsreserve (FOR) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve | 2026-11-14. Read for no new FOR from 2023 and release of an existing reserve |
| Belastingdienst, unused zelfstandigenaftrek | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek | 2026-11-14. Read for the carry-forward of unused zelfstandigenaftrek |
| Belastingdienst, workspace in the home | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/werkruimte_in_de_woning | 2026-11-14. Read for the independent-workspace conditions |

Not yet confirmed: none for the figures in the table; the outcome of any individual entrepreneur or employment assessment always rests on the facts and is not settled by this intake.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-freelance-intake` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-freelance-intake. If neither is available, confirm every figure against the official source pages cited above before relying on it.
