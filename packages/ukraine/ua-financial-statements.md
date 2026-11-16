---
name: ua-financial-statements
description: Use this skill whenever asked about Ukrainian financial statements and financial reporting (фінансова звітність) for legal entities, or whether a self-employed person must prepare them. Trigger on phrases like "Ukraine financial statements", "фінансова звітність", "П(С)БО", "НП(С)БО", "IFRS Ukraine", "МСФЗ", "do I file accounts as a FOP", "balance sheet Ukraine", "звіт про фінансові результати", "Форма 1-м", "Форма 1-мс", "enterprise size category Ukraine", "micro small medium large enterprise Ukraine", "statutory audit Ukraine", "Держстат financial report", "ТОВ financial statements", or any question about who must prepare and file financial statements, which accounting standards apply, the simplified report forms, deadlines, or audit obligations. This skill is about FORMAL FINANCIAL STATEMENTS for legal entities. A FOP (sole proprietor) does NOT prepare these; defer FOP records to ua-bookkeeping and FOP tax to ua-single-tax / ua-income-tax. ALWAYS read this skill before any Ukrainian financial-statement or financial-reporting work.
version: 1.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
type: situation-rules
---

# Ukraine Financial Statements and Financial Reporting v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This is a **formal financial-reporting decision and reviewer brief for Ukrainian legal entities**, including a ТОВ (limited liability company), and relevant foreign legal-person branches/representative offices. It covers legal-form routing, financial-reporting size criteria, national versus IFRS framework, full versus reduced forms, separate filing/publication/audit duties and preserved cases. It does not prepare signed statutory statements, group/consolidation, bank/insurance/PIE sector disclosures or a full audit opinion.

**A ФОП is an individual entrepreneur, not a legal entity under Law 996-XIV's financial-statement scope.** Do not create a statutory company Balance or statutory financial-results report for a FOP merely because they say “my company”. Route records to `ua-bookkeeping`, single tax to `ua-single-tax`, general-system personal tax to `ua-income-tax`, VAT to `ukraine-vat`, and own ЄСВ/payroll to their owners. Tax returns, VAT and contributions remain separate. This does **not** say FOPs can never be respondents for other statistical surveys or need no evidence. [Law 996 art 2/3/11 as reproduced in current official answer](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques).

**Dating:** current source review 15 November 2026; concrete annual dates/examples below are the **2025-2026 filing cycle**. A 2026 annual report filed in 2027 needs its then-effective forms, official calendar and relief review. This is not a claim that the full current text of every named law/standard has been recovered. Direct Parliamentary accounting/audit law and standard texts were inaccessible; the positive bounded rules below use the identified genuine official explanations. No firm/vendor summary is authority.

**Quick reference:** UAH presentation, actual form-specific units; financial-reporting classification under **Law 996 art 2**, with annual-average EUR rate and a two-year category-change rule; national standards unless a mandatory/voluntary IFRS route applies. Medium/large/PIE/issuer or other special status triggers an audit/publication review, never automatic “no audit”. Contributor remains **Open Accountants Community**.

## Ask the client first

1. Register extract/legal form/date, tax status and reporting period. Distinguish FOP, ТОВ/АТ, foreign branch, nonprofit and budget institution; do not default an unknown legal person to “small”.
2. Prior financial-reporting category and **both preceding annual sets**, with actual balance-sheet assets, **net** sales revenue and average employees; first-year entities use their first annual indicators. Keep the classification history and any reorganization/cessation facts.
3. UAH amounts and documented NBU **average for the corresponding year**, or EUR equivalents already computed on that basis. A year-end spot rate is not the classification rate. Do not insert a guessed current EUR rate.
4. PIE/large, bank/insurer/pension/other financial institution, securities admission/public offer/PJSC, authorized rating agency, national natural monopoly, extractive activity, parent/group and Cabinet-listed activity evidence. Small size alone does not resolve these statuses.
5. Mandatory IFRS result or documented voluntary election, official Ukrainian-language standards/version, applicable taxonomy/schema, national form choice and any group/sector disclosure question.
6. CIT/nonprofit/other tax reporting obligations and frequency; statutory statistics respondent list, initial financial statements, audit engagement/status, post-audit changes, publication duties, actual channel/calendar/relief evidence and authorized signers.

Reuse facts already documented in intake/records. If a threshold is close or a status is unknown, flag and keep the draft on review hold; do not manufacture the higher category or assert a smaller category to omit disclosures. The old conservative defaults are preserved as **risk controls**, not false legal classifications: confirm legal form, do not downgrade, test actual indicators/history, investigate audit, use the official statutory framework/translation, and state missing evidence.

## Rates, bands and thresholds

These are **financial-reporting classification criteria**, not tax rates or the general SME-status definitions from another law. Use at least **2 (in words on the page) of the 3 listed indicators**, the hierarchy and change rule below. Each ceiling is inclusive.

| Law 996 category | Balance-sheet assets | Net sales revenue | Average employees | Condition/source |
|---|---|---|---|---|
| Micro | Up to **EUR 350000** | Up to **EUR 700000** | Up to **10** | At least 2 of 3; [996 art 2, current 2026 official criteria](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html) |
| Small | Up to **EUR 4000000** | Up to **EUR 8000000** | Up to **50** | **Not micro**, at least 2 of 3; [996 art 2](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html) |
| Medium | Up to **EUR 20000000** | Up to **EUR 40000000** | Up to **250** | **Not small**, at least 2 of 3; [996 art 2](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html) |
| Large | Over **EUR 20000000** | Over **EUR 40000000** | Over **250** | **Not medium**, at least 2 of 3; [996 art 2](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html) |

The official explanation prints 350/700 **thousand**,4/8/20/40 **million**; expanded numerals above are equivalent, not EUR 350/700. Use the **average official UAH/EUR rate for the corresponding year**. If starting from UAH, divide the relevant UAH figure by that verified average; do not convert the legal ceilings at 31 December's spot rate. Newly formed entities use indicators at the first annual statement date. An existing entity that does not meet its category criteria for **2 consecutive years (in words on the page)** moves to the appropriate category under the rule; one year's crossing alone does not establish immediate migration. Keep the timing assessment for the actual reporting year in the brief. [Full current criteria/currency/new-entity/change explanation](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html).

**Old “competing thresholds” correction:** the current official 2026 source expressly uses Law 996 art 2 for accounting classification. Do not substitute the general Law 4196-IX SME categories or Commission Recommendation 2003/361/EC for this test. The old alternative approximations (**9/49/249 staff; EUR 2 m/10 m/50 m revenue/43 m assets**) are retained here only as an **unconfirmed, withdrawn comparison**, not usable financial-reporting limits. Their complete current separate-purpose conditions have not been opened. The old uncertainty is resolved for the Law 996 criteria actually confirmed above; it does not authorize a final category without the company's history.

## The method, step by step

### 1. Route legal form and establish accounts

For a FOP, issue the no-company-financial-statements routing conclusion and preserve the tax/records handoff. For a legal entity, obtain the accounting records and prepare the appropriate financial statements from them; Law 996's accounting/financial-reporting duties apply. The original double-entry/from-registration instruction is an accounting-setup flag: do not assume every simplified/nonbusiness entity uses an identical mandatory double-entry method or invent a first-period rule without checking the applicable legal exception. Exact simplified-accounting and first/last-period exceptions remain a reviewer hold where not established. [Law 996 arts 2/3/11, current answer](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques).

Ordinary financial reporting is for the calendar year, with interim first-quarter/half-year/9-month periods and possible additional policy periods as explained officially. The tax-return period may differ, including the agricultural CIT route; do not equate every legal entity with an annual CIT filer. [Law 996 art 13 and 419 asexplained](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [TaxCode 46.2/137](https://tax.gov.ua/nk/).

**If the business incorporates a ТОВ:** company accounting, applicable full/reduced statements, authority-specific submissions and any audit/publication duties must now be assessed. A simplified tax regime does not turn the ТОВ into a FOP or remove accounts. This is a scope transition, not a promise every ТОВ files the same form/return to every authority.

### 2. Determine size before choosing a form

Document the underlying indicators, rate, prior category and both-year test. Test micro first, then small excluding micro, then medium excluding small, then large. Do not infer category from a colloquial “SME”, tax-regime label, registered capital, one employee number or one asset figure. Near-boundary/contradictory results block final form selection.

### 3. Select framework and forms, including exceptions

The national **П(С)БО / НП(С)БО** terminology refers to Ministry of Finance accounting standards; retain the exact current official standard name for the job. НП(С)БО1 governs the general set and НП(С)БО25 the eligible reduced set; bank/budget/IFRS reporting is a separate branch. [Official standards/form register](https://www.mof.gov.ua/uk/nacionalni-polozhennja1); [current scope/sets](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html).

| Branch | Statement package and boundary | Official source |
|---|---|---|
| Eligible micro under national standards | НП(С)БО25 **1-мс Balance +2-мс Financial Results**. Nonbusiness societies also appear in the current reduced-form scope. Exclude entities required to use IFRS; verify actual current form/version | [НП(С)БО25 scope/forms](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [current official answer](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques) |
| Eligible small under national standards | НП(С)БО25 **1-м Balance +2-м Financial Results**; relevant foreign legal-person branches/representatives also have this branch. Not every entity labelled small can ignore mandatory IFRS | [НП(С)БО25 scope/forms](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html) |
| Fuller national set | Balance/financial position **Form 1**; results/comprehensive income **Form 2**; cash flows **Form 3 direct or 3нindirect**; equity **Form 4**; notes **Form 5** where applicable. **Form 5 is separately approved by Order 302**, not literally an appendix created by НП(С)БО1. Apply actual note/disclosure exemptions | [Full components and Order 302](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [official form catalogue](https://www.mof.gov.ua/uk/nacionalni-polozhennja1) |
| Medium | Ordinary national full set unless mandatory or elected IFRS; management report separately. Actual size history and special status decide, not a single-year illustration | [Full set](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [management report](https://zir.tax.gov.ua/main/bz/view/?id=36833&src=ques) |
| Large / mandatory IFRS | Applicable full **IFRS** statements/disclosures, taxonomy and group/sector review. Do **not** call national Forms 1-5 the mandatory IFRS format simply because both have balance/results/cash/equity/notes | [Ministry IFRS rules](https://www.mof.gov.ua/uk/zaprovadzhennja-mizhnarodnih-standartiv-finansovoi-zvitnosti); [current mandatory scope](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques) |
| Voluntary fuller statements | Eligible reduced-form entities may choose НП(С)БО1 forms; verify the accounting policy and consistent presentation. This does not prove every micro entity may freely substitute any other reduced form | [Current official fuller-form option](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques); [national-forms explanation](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html) |

НП(С)БО25 displays amounts in **thousands of UAH with 1 decimal place (1 in words on the page)**; this specific rule is confirmed in the current answer. For the full/IFRS set verify that form's units/rounding; the old blanket “all statements in thousands” is not sufficient. Balance is **at a date**, results cover **a period**. Do not use date units/periods interchangeably. [Current 25 presentation rule](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques).

The original **17 February 2023 Group 3 legal-person choice between 1-мс/2-мс and 1-м/2-м** is retained as an unconfirmed historical form-election claim, **not** current permission. Current official explanations list category-based forms and a fuller НП(С)БО1 option; exact extra reduced-form elections and later changes require the current standard. The Ministry's 2026 register lists later accounting amendments, including **483/520 and 513**, so a 2027 schema must not be inferred from a 2026 explanation. The listed order/appendix files were not fully recovered; no operational cutover or cell/schema approval is given. [Official 2026 register](https://www.mof.gov.ua/uk/orders_of_the_Ministry_of_Finance_of_Ukraine_in_2026.).

### 4. Test mandatory IFRS and keep the official-language rule

Current Law 996 art 12-1 scope reproduced by the official answer includes **PIEs, public joint-stock companies, authorized rating agencies, extractive-industry entities, parent companies of groups containing PIEs, parents of large groups that are not themselves large, and Cabinet-listed activities**. Other entities can elect IFRS. Large status/financial/securities facts must be tested against the actual PIE definition and sector laws; the current full PIE definition/Cabinet list is not certified here. [Current official 12-1 scope](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques).

Preserve all original special flags: banks, insurers, nonstate pension funds, other financial institutions with their size exceptions, exchange-traded/publicly offered securities, PJSC, large entities, mineral/extractive activity and group parents. Do not treat every securities issuer or every minor mineral activity as automatically within an unqualified list. The old **banks-since 2011** historical date is not independently confirmed here and is not an effective-date instruction.

For statutory IFRS use standards **in the state language, officially published by the Ministry**. An English IASB text does not replace that statutory requirement. The Ministry states that **IFRS users**, including voluntary adopters, use the prescribed taxonomy/uniform electronic format; it is not “mandatory IFRS and most other national-standard companies use XBRL”. Verify the actual taxonomy, regulator, transition date, validation and receipt requirements before submission. Official translation access is territorially restricted; do not bypass it, and no full current IFRS standard text is claimed read here. [Ministry's operative framework/translation/taxonomy explanation](https://www.mof.gov.ua/uk/zaprovadzhennja-mizhnarodnih-standartiv-finansovoi-zvitnosti).

### 5. Make a separate audit and management-report decision

The current 2026 DPS explanation identifies annual publication with audit for the specified PIE/PJSC/national-natural-monopoly/extractive group, large nonissuers and **medium enterprises**, plus **micro/small other financial institutions**. Thus medium is a real audit-review route and micro/small is **not blanket audit exemption**. A company cannot get “no audit” solely from its size. The old “verify whether medium ever triggers audit” is replaced by this sourced duty; actual entity and special exemptions still need the current law/qualified auditor. [Law 996 art 14 groups,2026 official explanation](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html).

Law 2258-VIII remains the governing audit-law reference. Auditor eligibility/register entry, PIE engagement procurement/approval, independence/rotation, applicable ISA and official Ukrainian translation must be checked by the qualified auditor. The original public-tender/highest-governing-body/rotation instructions are retained as **specific review flags, not an approved universal procurement recipe**: full current 2258/related statutory procedures were not recovered. Do not issue an audit opinion or assert an entity's audit waiver from this partial review.

Under the current explanation, ordinary medium/large reporting includes a **management report**; budget/micro/small exclusions apply and medium entities may omit nonfinancial information. It is **separate from financial statements and not required as a CIT financial-statement appendix to DPS**. Group management reports, payments-to-government/nonfinancial or other PIE/sector disclosures require their own scope; do not append every one to every company by default. [Current management-report answer](https://zir.tax.gov.ua/main/bz/view/?id=36833&src=ques).

### 6. Separate submissions, publication, audit follow-up and relief

| Duty | Confirmed timing / action, with limits | Official source |
|---|---|---|
| Initial annual CIT-linked financial statements | **60 calendar days** after calendar-year end, with the actual tax calendar. **2025 annual CIT:2 March 2026**, correcting the old fixed 1 March. Financial statements/pre-audit balance and results as applicable are an integral appendix; quarterly filers/interim schedules follow their actual 137 periods. Not all legal entities owe a CIT return | [46.2/49.18.6/49.20/137](https://tax.gov.ua/nk/); [actual 2025 deadline](https://vin.tax.gov.ua/media-ark/news-ark/print-983219.html) |
| Statistics/general 419 annual submission | The official 419 explanation states **28 February** following year for eligible micro/small/nonbusiness national-standard annuals and specified preliminary balance/results for publication-obliged entities. The actual **2025-2026 statistics calendar gives 2 March 2026**, correcting the old unadjusted 28 February. Check actual respondent/form and any special recipient rules | [419 p 5 explanation](https://dp.tax.gov.ua/media-ark/news-ark/print-979811.html); [officialMarch 2026 calendar](https://www.kh.ukrstat.gov.ua/terminy-podannia-statystychnoi-zvitnosti-u-berezni-2026-roku) |
| Medium full annual 419 package | Official 419 explanation gives **1 June** following year for the medium full annual/consolidated package to the named 419 p 2 recipients except Treasury; this does not erase the separate initial tax/statistical obligations | [419 p 2/p 5 explanation](https://dp.tax.gov.ua/media-ark/news-ark/print-979811.html) |
| Audited annual follow-up to DPS | Publication-obliged CIT payers submit the annual statements subject to publication with audit **no later than 10 June** following reporting year under 46.2; **not the same as publication deadline**. Post-audit changes affecting the filed annual CIT require the 50.1 amendment route by that deadline, subject to applicable relief. Actual upload/schema/acceptance evidence still needed | [46.2/50.1](https://tax.gov.ua/nk/); [2026 actual follow-up explanation](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html) |
| Website/public publication | Original baseline **30 April** for specified PIE/PJSC/monopoly/extractive branches and **1 June** for specified large/medium/other-financial branches is retained only as an **unconfirmed current-calendar review item**. Current 2026 publication/audit duty groups are sourced, but full current 14/2115/sector commencement/war-relief conditions were not recovered. Do not treat these retained baseline dates or a June 10 tax-submission headline as permission or a final publication calendar | [Current duty groups](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html); exact current deadline/relief held |
| Tax-side wartime exception | The actual 69.1 paragraph exempts the specified publication-obliged CIT payers from Code liability for the specified missing/late audited annual financial statements and related tax amendment, with mandatory performance within **3 months (in words on the page)** after martial law ends/cancels. It does not waive all ordinary initial CIT/statistical duties or audit/publication forever; full individual/sector/other-law relief remains a referral | [Current 69.1 specific paragraph and 46.2](https://tax.gov.ua/nk/); [2026 official explanation](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html) |

Submission recipients also include management bodies, owners/founders under governing documents and workers on request; banks have their NBU route. DPS, statistics, regulator/taxonomy and public website are **distinct destinations**. The initial/pre-audit and audited versions must be linked and changes reconciled. A receipt for one channel proves neither another channel nor public publication. [419 recipients](https://dp.tax.gov.ua/media-ark/news-ark/print-979811.html); [management/bank distinctions](https://zir.tax.gov.ua/main/bz/view/?id=36833&src=ques).

For DPS use the applicable financial forms, correct period and schema, actual **ФЗ** attachment indicators and **НП(С)БО / МСФЗ** selection, signed by authorized persons; retain submitted files and acceptance evidence. Check required initial/pre-audit and audited versions separately. No authenticated Cabinet/form-cell test was done in this review. The current official explanation confirms the form/attachment mapping, not the adequacy of an individual filing. [DPSform/attachment instructions](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [audit follow-up](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html).

## Worked cases

### Original 1: a freelance developer asks whether to file accounts

**Oksana** is a ФОП, Group 3, freelance software developer, approximately **UAH 2500000 income in 2025**, no employees. Confirm that legal form; her income does not turn her into a legal entity. No statutory company financial statements, Balance or statutory financial-results report under this company workflow. Route income records to `ua-bookkeeping`, the quarterly single-tax route to `ua-single-tax` with its exceptions, own ЄСВ/levy to the appropriate owner; incorporation would require a fresh company decision. This is not a blanket exclusion from every statistical survey or permission to omit tax records. [Law 996 scope](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques).

### Original 2: the new design-agency ТОВ

First annual date **31 December 2025**; assets approximately **EUR 120000**, net revenue **EUR 410000**, average employees **6**. Assume these EUR equivalents were computed using the verified relevant annual average, the entity is newly formed and no mandatory-IFRS/sector exception exists. All 3 micro tests pass; headroom is **230000 assets,290000 revenue,4 employees**, derived. Unlike an existing entity with unknown history, a new entity uses its first annual indicators. The indicative reduced set is 1-мс/2-мс under 25; no final audit/publication exemption is granted until special-status screening is complete. Ordinary 2025 annual initial DPS/statistics dates above are **2 March 2026**, not old 1 March/28 February. Confirm actual tax/recipient obligations and form/version. [Criteria/newentity](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html); [forms](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [DPSdate](https://vin.tax.gov.ua/media-ark/news-ark/print-983219.html); [statisticsdate](https://www.kh.ukrstat.gov.ua/terminy-podannia-statystychnoi-zvitnosti-u-berezni-2026-roku).

```oa-check
name: First annual micro indicators and threshold headroom
inputs:
  assets_eur: 120000
  net_revenue_eur: 410000
  average_employees: 6
  micro_assets_ceiling: 350000
  micro_revenue_ceiling: 700000
  micro_staff_ceiling: 10
steps:
  assets_headroom: micro_assets_ceiling - assets_eur
  revenue_headroom: micro_revenue_ceiling - net_revenue_eur
  staff_headroom: micro_staff_ceiling - average_employees
expected:
  assets_headroom: 230000
  revenue_headroom: 290000
  staff_headroom: 4
```

### Original 3: logistics ТОВ with larger indicators

At **31 December 2025** assets approximately **EUR 9000000**, net revenue **EUR 22000000**, average employees **180**, not a financial institution or securities issuer. Compared with small ceilings, excesses are **EUR 5000000 /EUR 14000000 /130 employees**, derived; medium ceiling headroom is **EUR 11000000 /EUR 18000000 /70 employees**, derived. Thus the year's indicators fit the medium numerical band. **Actual classification still needs the previous category and two-year history**, not an immediate “crossed into medium” conclusion.

If the actual medium category is confirmed and no mandatory/elected IFRS branch applies, plan the national full set plus separate management report and the real audit/publication review. “Not finance or issuer” alone does not exclude every mandatory-IFRS category. Preserve the original June 1 medium package/publication flag, but apply the separate confirmed filing/follow-up dates and held publication calendar above. Do not finalize no-IFRS/audit/calendar conclusions from this illustration. [Criteria/history](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html); [nationalset](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html); [management](https://zir.tax.gov.ua/main/bz/view/?id=36833&src=ques); [currentauditgroups](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html).

```oa-check
name: Logistics indicators exceed small but fit medium ceilings
inputs:
  assets_eur: 9000000
  net_revenue_eur: 22000000
  average_employees: 180
  small_assets_ceiling: 4000000
  small_revenue_ceiling: 8000000
  small_staff_ceiling: 50
  medium_assets_ceiling: 20000000
  medium_revenue_ceiling: 40000000
  medium_staff_ceiling: 250
steps:
  assets_over_small: assets_eur - small_assets_ceiling
  revenue_over_small: net_revenue_eur - small_revenue_ceiling
  staff_over_small: average_employees - small_staff_ceiling
  assets_under_medium: medium_assets_ceiling - assets_eur
  revenue_under_medium: medium_revenue_ceiling - net_revenue_eur
  staff_under_medium: medium_staff_ceiling - average_employees
expected:
  assets_over_small: 5000000
  revenue_over_small: 14000000
  staff_over_small: 130
  assets_under_medium: 11000000
  revenue_under_medium: 18000000
  staff_under_medium: 70
```

## When to refuse or refer

1. Do not prepare/present statutory company financial statements for a FOP; confirm legal form and route tax/records. A voluntary management schedule is not a filed company statement.
2. Do not certify size, reduced form or audit result without the actual Law 996 criteria, annual-average FX and first-year/two-year history; do not substitute the unverified 4196 comparison.
3. Do not state “no audit” for medium/large/PIE/issuer or a special institution from size alone. Engage an appropriately qualified Ukrainian auditor for legal obligation and engagement requirements.
4. Do not impose IFRS on a national-standard entity without obligation/election, or national forms on a mandatory-IFRS entity. Resolve all group/sector/Cabinet flags.
5. Do not replace the Ministry's officially published state-language statutory IFRS/ISA requirements with an unsupported English-only filing claim; current full ISA/engagement rules remain auditor review.
6. Do not release a fixed date without distinguishing tax/statistics/audited follow-up/publication and actual-year/war/sector conditions. No 2027 form/calendar is approved here.
7. Do not sign off, file, submit or replace the qualified accountant/auditor. Produce the records/classification/framework/forms/recipients/calendar/audit/open-items brief for review only.
8. Refer consolidation, group reporting, PIE/nonfinancial/payments-to-government, banking, insurance and other sector disclosures to the competent qualified specialist; preserve every flagged obligation rather than silently excluding it.

Before completion check legal form/register, original accounting records, all classification inputs/annual rate/history, mandatory/elected framework, every required statement and separate management report, audit/engagement decision, all recipients and actual schema/date/receipt, post-audit reconciliation and unresolved hold. No missing field becomes a zero or a false “not required”.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [DPS,3 March 2026: classification](https://svp.tax.gov.ua/media-ark/news-ark/print-982204.html) | Read for Full operative body: Law 996 art 2 categories, hierarchy,2 of 3 indicators, first year,2 consecutive years and annual-average EUR; Code 49.4 electronic-filing classification. | 2026-11-15 |
| [Current ZIR 44104: forms and scope](https://zir.tax.gov.ua/main/bz/view/?id=44104&src=ques) | Read for Full answer: Law 996 arts 2/3/11 scope; NAS 1/25 forms, units and options;12-1 mandatory/voluntary IFRS including authorized rating agencies and current group categories; taxonomy and public-sector boundary. Not full original statutes/standards. | 2026-11-15 |
| [DPS,11 May 2026: national forms](https://ck.tax.gov.ua/media-ark/news-ark/print-1009161.html) | Read for Whole operative body: full/reduced sets, separate Order 302 notes, annual/interim periods, CIT appendix and pre-audit statements, attachment and standard indicators. | 2026-11-15 |
| [Ministry national standards/form register](https://www.mof.gov.ua/uk/nacionalni-polozhennja1) | Read for Operative listing 976-1096: NAS 1/25 titles, forms 1-4,3н and 5, condensed pairs. Links inspected; full linked standards unavailable. No cell/schema verification. | 2026-11-15 |
| [Ministry IFRS framework](https://www.mof.gov.ua/uk/zaprovadzhennja-mizhnarodnih-standartiv-finansovoi-zvitnosti) | Read for Whole operative body 962-971: mandatory/voluntary framework, official state-language publication, uniform taxonomy format for IFRS users and territorial copyright restriction. Not full IFRS standard texts. | 2026-11-15 |
| [Current ZIR 36833: management report](https://zir.tax.gov.ua/main/bz/view/?id=36833&src=ques) | Read for Full answer: medium/large scope and exclusions, medium nonfinancial option, separate report outside the DPS financial-statement appendix; bank, recipient, publication and attachment distinctions. | 2026-11-15 |
| [DPS,9 February 2026: recipients/timing](https://dp.tax.gov.ua/media-ark/news-ark/print-979811.html) | Read for Whole operative body:419 p 2 recipients, p 5 annual 28 February/medium 1 June rules and separate CIT 60 days. Actual 2026 calendar adjustments sourced separately. | 2026-11-15 |
| [Official statistics,March 2026 calendar](https://www.kh.ukrstat.gov.ua/terminy-podannia-statystychnoi-zvitnosti-u-berezni-2026-roku) | Read for Operative month calendar 59-108, especially annual statements due 2 March and qualified legal-entity/representative population. No individual respondent/form approval. | 2026-11-15 |
| [DPS,18 February 2026: annual CIT date](https://vin.tax.gov.ua/media-ark/news-ark/print-983219.html) | Read for Whole body: actual 2025 annual CIT deadline 2 March 2026,60 days, Sunday shift and required financial appendix. Other tax figures are not accounting-classification criteria. | 2026-11-15 |
| [DPS,9 June 2026: audited follow-up](https://if.tax.gov.ua/media-ark/news-ark/print-1018958.html) | Read for Entire operative 35 lines: publication/audit groups, DPS 10 June follow-up, pre-audit forms and flags, specific 69.1 liability relief and mandatory 3-month completion. Not full publication relief under other laws. | 2026-11-15 |
| [Current official Tax Code](https://tax.gov.ua/nk/) | Read for Full 46.2 with neighbors;49.4/49.18.6/49.20 and 137 periods;50.1 audit-change paragraph;69.1 specific audited-FS liability paragraph plus nearby inability context. Not whole Code, all 69.1 procedures or client relief. | 2026-11-15 |
| [Ministry 2026 orders register](https://www.mof.gov.ua/uk/orders_of_the_Ministry_of_Finance_of_Ukraine_in_2026.) | Read for October/November accounting-order list including 483/520/513/565 metadata. Linked 483/520 DOC files unsupported via web and download 403; no full change-package, effective-date or schema approval. | 2026-11-15 |

Not yet confirmed: full current 996/2258/419/NAS 1/NAS 25 statutory texts and all first/last-period or simplified-accounting exceptions; current PIE definition, Cabinet list and sector details; precise audit-register, procurement, approval, rotation and ISA requirements; applicable publication calendar and current 2115/sector/war relief; the old 17 February 2023 Group 3 reduced-form choice and bank-IFRS-since 2011 historical date; full later 483/520/513/565 change packages and 2027 forms, taxonomy, schema and calendar; actual annual NBU rate, company history, status and elections; separate-purpose 4196/EU SME comparison. Direct Parliament and ordinary-browser access failed; no failed response was counted as read. Unconfirmed branches remain outside usable filing instructions.

**Withdrawn original secondary research pointers:** Forvis Mazars, Crowe, PwC, BDO, KPMG, IFRS Foundation and IAS Plus (Deloitte). These original references are retained for provenance only; none is authority for this draft or claimed independently opened/read. The operative rules above rely on the official sources and stated limits.

## Disclaimer

This is bounded source-cited reference material contributed by the Open Accountants Community, checked in the scopes stated above. It is not legal, accounting or tax advice and does not replace sign-off by a qualified Ukrainian accountant or auditor. Reporting law, standards, forms, deadlines and martial-law measures change; every actual output requires the current applicable sources and qualified review before filing or action. The old blanket “research-verified May 2026” claim and vendor-source reliance are not inherited as present verification.

Part of openaccountants.com — open-source tax skills for the self-employed.
