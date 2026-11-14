---
name: nz-company-financial-reporting-core
description: "Use for selected reporting readiness work for an ordinary New Zealand domestic company limited by shares. Trigger on financial reporting size tests, shareholder reporting elections, audit, registration of financial statements or annual reports to shareholders. Requires confirmed entity status, actual accounting periods, group perimeter, voting rights and applicable standards. Separates statutory size from accounting tier and each reporting duty. Produces selected working papers for qualified review; it cannot complete financial statement preparation, classify a financial markets participant, approve an audit exemption or submit accounts."
jurisdiction: NZ
category: financial-statements
tier: 2
review_status: pending_review
tax_year: 2026
tax_year_notes: "Reporting controls checked on 14 November 2026. Statutory size and XRB standards have separate period-start and early-adoption conditions. This is not an income-tax year."
last_updated: 2026-11-14
version: 0.1
depends_on:
  - workflow-base
  - financial-statements-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand company reporting, audit and annual reports v0.1

## Scope and source period

Prepare selected reporting-readiness working papers for an already selected ordinary domestic company limited by shares. Load [workflow-base](../../foundation/workflow-base.md) and [financial-statements-workflow-base](../../foundation/financial-statements-workflow-base.md). Retain their confirmation sequence, source conditions, refusals, mandatory country slots, outputs and qualified-review controls. This selected core is an incomplete country companion for preparing a set of financial statements.

Confirm that the company is a private sector for-profit entity and establish its actual regime. Companies required to prepare company or group statements under Financial Markets Conduct Act Part 7 subpart 3 or Financial Reporting Act section 55 are outside Companies Act Part 11 subpart 2. Public entities, public benefit entities, overseas companies' New Zealand businesses, listed entities, financial markets participants, climate reporting entities, co-operatives and other special regimes need their own source chain. A domestic subsidiary of an overseas company can remain within this core, but uses the relevant overseas-subsidiary size test. A 'private company' label alone establishes none of these facts. [Companies Act, ss197/198][C197], [FRA, definitions and s45][FRA-CURRENT], [XRB A1, paras2–13][XRB-A1-CURRENT].

The Companies Act consolidation reviewed is dated 1 July 2025. Its live warning list was checked on 14 November 2026 against the retained Deposit Takers, Employment Leave and Address Information amendments. The selected amendment items do not directly amend the reporting provisions used here or the selected subsidiary provisions in sections 5–8. This is a scoped review. Parts of the Deposit Takers Act have commenced; do not describe the whole Act as uncommenced. Revalidate the address-information transition from 18 November 2026 before relying on related company-record or disclosure procedures. [Live warnings][CA-VERSION], [Deposit Takers amendments][B126V5], [commencement][B126V3], [Employment Leave amendments][B126V6], [commencement][B126V4], [Address Act][B126V2], [address regulations][B126V7].

The FRA consolidation is dated 5 April 2026. Its live warning identifies the Legislation Amendment Act 2026, whose selected amendments affect FRA sections 27/28 rather than the size and audit provisions used below. The general commencement backstop was 2 November 2026. Do not rely on superseded section 27 wording to determine when an XRB standard takes effect. For each standard, record its own legal effective date and the accounting periods to which it applies. [FRA warnings][FRA-VERSION], [Legislation Amendment Act, s2 and Schedule4][LAA2026].

Use redacted summaries and synthetic labels. The professional retains private registers, identity documents, tax identifiers, banking details, credentials and signature authority and performs any authorised filing. No actual accounts, company classification, shareholder agreement, audit, signature or filing is established by these examples.

## Engagement and financial-statement completion gates

Obtain the actual constitution, company status, purpose/sector and financial markets status, accounting-period dates, balance-date history, group/control chart, relevant prior-period statements and accounting policies, current ownership/voting rights, first-day voting-shareholder count, meeting dates, notices, elections and parent-group reports. Establish their dates and legal effect. Missing or conflicting facts are Needs Input, with the affected decision and evidence required.

Do not proceed from this readiness review to statement preparation until every mandatory country slot in the financial-statements base is supported for the engagement:

| Mandatory slot | What this selected core establishes and what remains |
|---|---|
| 1. Reporting framework and legal regime | Selected company-law gates and XRB tier routes below. Actual entity, regime, election, framework, comparative requirements and approval sequence still need confirmation. |
| 2. Income statement format | Open: applicable framework's presentation, categories, subtotals and terminology. |
| 3. Balance sheet format | Open: applicable framework's presentation, classification and required line items. |
| 4. Chart of accounts mapping | Open: actual trial balance mapped to the verified framework, with reconciliation. |
| 5. Notes by reporting regime | Open: complete applicable notes and supported disclosure exemptions. RDR eligibility alone does not fill this slot. |
| 6. Depreciation | Open: recognition, components, methods, useful lives, residual values and part-period/disposal rules. |
| 7. Tax provision | Open: entity and period tax computation, current/deferred tax measurement and recognition location. A company tax headline rate cannot fill it. |
| 8. Filing requirements | Selected Companies Act registration route below. Other authorities, actual documents, prescribed fees, penalties, submission mechanics and any special regime remain to verify. |
| 9. Audit | Selected statutory gate and qualified-auditor controls below. Actual appointment, independence, scope, report and any other enactment remain to verify. |
| 10. Directors' report | Selected Companies Act annual-report preparation, contents and distribution below. Actual report and evidence remain to prepare/review. |
| 11. Going concern | Open: applicable basis, assessment period, evidence and disclosures. |
| 12. Currency and number format | Open: framework-specific functional/presentation currency and presentation/rounding requirements. Dollar amounts in threshold examples are not a currency determination. |

For a financial-statement preparation engagement, retain all 6 mandatory outputs: income statement, balance sheet, notes, year-end adjustment schedule, filing checklist and reviewer brief, plus the universal outputs of workflow-base. These reporting-readiness papers cannot replace that set. Hold statement drafting, filing-ready status and completion whilst any required slot, fact, reconciliation, confirmation or professional review is missing.

## Universal companion controls

### Intake and confirmation

Add the engagement facts listed above to the universal structured question form. Record legal form/registration; for-profit and private sector status; any FMC/FRA55 or other special regime; current and preceding actual periods/balance dates; all subsidiary/control relationships; the source and accounting basis of each measured amount; first-day voting-shareholders and joint parcels; actual meeting/service dates; constitution and provision-specific notices/resolutions; parent reports and lodgements; public accountability, tier election/adoption; proposed auditor; report recipients and outstanding documents. Do not collect private credentials or identifiers for these working papers.

Present the evidenced regime/framework determination and open matters with the bases' combined profile/framework confirmation. Wait for the required confirmation before trial-balance review. A missing fact does not authorise a guessed classification. The fuller statement-preparation contract remains incomplete until all country slots above are supported.

### Topical refusal catalogue

Apply every loaded catalogue, including the universal R-REVIEWER-MISSING and R-CONTENT-MISMATCH triggers and their exact loaded messages. Include each code's cleared/fired result and reason in the refusal trace. The following additional codes are defined for this selected core. When one fires, reproduce its message verbatim, explain the affected work and state the evidence/content needed. A hold on one decision does not establish another decision.

| Code | Trigger | Verbatim message |
|---|---|---|
| R-NZ-REPORT-REGIME | The requested company/period requires an out-of-scope or unverified reporting regime or applicable standard. | This company or reporting period requires reporting content outside this guide's verified scope. I cannot determine the affected duties from this guide. Load the applicable source-verified content and obtain qualified review before continuing that work. |
| R-NZ-REPORT-EVIDENCE | A requested size, election, exception, tier, audit, registration or report conclusion depends on missing/conflicting period, amount, rights, authority or delivery evidence. | Needs Input: the evidence required for this reporting decision is missing or conflicting. I cannot classify the company or apply the affected election or exception until the identified evidence is resolved. |
| R-NZ-FS-INCOMPLETE | Statement preparation or financial-statement workflow completion is requested whilst any mandatory country slot or required output is unsupported. | This selected reporting core is an incomplete companion for financial statement preparation. Do not begin statement drafting or mark the workflow complete. Load source-verified content for all mandatory country slots and retain every required output and professional review. |
| R-NZ-REPORT-CERTIFICATION | The user asks these working papers to establish an actual exemption, audit, signature or filing without the required professional authority, final documents or evidence. | I cannot certify an exemption, audit, signature or filing from these working papers. A qualified professional must verify the actual authority, final documents and evidence. |

### Defaults and reviewer attention

These are workflow holds, not additional statutory rules or elections. No factual ambiguity here authorises a guessed monetary value, legal status or supposedly conservative exemption.

| Ambiguity | Permitted default/action | Alternative and cash impact to disclose |
|---|---|---|
| Missing period, balance-date authority or applicable law/standard version | No date/version default. Hold the affected rule and request actual period/adoption evidence. | Identify the competing period rules; cash impact unquantified until resolved. |
| Missing size amount, accounting basis, subsidiary/control or holder/residence evidence | No zero, simple ledger-sum, ordinary-category or ownership default. Hold classification; request the reconciliation and applicable definitions. | Show each supported sensitivity separately; do not assign a legal result to an unsupported amount. Cost/cash impact unquantified. |
| Missing constitution, voting entitlement, meeting/service proof or period-specific choice | Do not presume an opt-in, opt-out, agreement or renewal from silence or an earlier year. Hold the claimed choice and obtain the actual evidence. | Compare supported duties with/without the proposed choice for review, without approving either unsupported classification; cost/cash impact unquantified. |
| Missing parent-group report, signature, date or lodgement/audit evidence | No parent exception inferred. Mark its specific condition unproved and hold the affected conclusion. | Distinguish preparation and registration conditions; do not invent otherwise exempt standalone accounts. Cost/cash impact unquantified. |
| Uncertain public accountability, tier election or early adoption | No Tier 2 or early-adoption default. Refer status/election to the qualified reviewer; apply Tier 1 only when the applicable evidenced A1 rules establish it. | Recognition/disclosure and cost effects require framework review; no guessed savings. |
| Missing working-day calendar, receipt/service facts or filing mechanics | No weekday-only deadline or completed-filing default. Mark the date/submission Needs Input. | Record the event and missing calendar/service evidence; fees, penalties and cash effects remain unquantified. |

The reviewer attention threshold for this core is **NZ$0**: flag every reporting-duty, exemption, election, audit, tier, signature or filing position regardless of stated cash effect or certainty. Flag every non-zero monetary reconciliation difference, including NZ$0.01, and every unresolved date or condition. This is an internal review policy, not a statutory materiality, audit threshold, currency determination or permission to ignore non-monetary defects. Record unquantified impacts as unquantified, not zero. Qualified review remains mandatory for every output.

### Period-specific figure reference

This table gathers the selected figures; apply their full conditions and period gates in the substantive sections, not the numbers alone.

| Figure/control | Selected amount or period | Primary authority |
|---|---|---|
| Direct ordinary-category size | Assets exceed $66m at each of 2 preceding balance dates, or revenue exceeds $33m in each of 2 preceding periods | [Section45(1)][FRA45], [former s45][FRA-PREV45] |
| Direct overseas-company/subsidiary size | Corresponding $22m assets or $11m revenue, with the same strict 2-observation test | [Section45(2)][FRA45], [former s45][FRA-PREV45] |
| New subsidiary size route | Periods commencing on/after 29 September 2025; exact (1)/(2) child test | [Schedule saving][REGSYSTEMS2025], [s45(2A)][FRA45] |
| Minimal inactive costs/interest | Paragraph (b) costs no more than $50; interest disregarded only up to those costs | [Section45(5)][FRA45] |
| Inactive declaration | Within 5 months after period end | [Section45(3)][FRA45] |
| Shareholder-count split | 10+ versus fewer than 10, counted at close of period's first day | [Sections199/200][C199], [preparation][C200] |
| Opting period | Earliest 6 months after start, annual meeting in period or qualifying short-period balance date | [Section207H][C207H] |
| Opt-out votes | At least 95% of entitled votes cast; eligibility and meeting conditions apply | [Sections207I][C207I], [207J][C207J] |
| Opt-in holding/timing | At least 5% voting shares; no later than 5 working days before opting-period end | [Section207K][C207K] |
| Financial statements/signature | Complete/date/sign within 5 months after balance date; 2 directors or sole director | [Sections201][C201], [202][C202] |
| Registration voting power/deadline | At least 25% meeting voting power in specified holder categories, plus large status; deliver within 5 months after balance date | [Sections207D][C207D], [207E][C207E] |
| Ordinary-residence limb for registration | Domicile, or specified living/usual-place test over immediately preceding 12 months | [Section207D(3)][C207D] |
| Registrar auditor-appointment notification | Casual vacancy unfilled for 1 month is one appointment-power route; notify within 5 working days after power arises | [Section207Q][C207Q] |
| Auditor's non-compliance report | Within 7 working days after signing, to Registrar and XRB | [Section207C][C207C] |
| Annual report | Prepare within 5 months after balance date; required board signatures by 2 directors or sole director | [Sections208][C208], [211][C211] |
| Annual-report waiver/permitted omissions | At least 95% voting shares, with the separate statutory conditions | [Sections208(4)][C208], [211(3)][C211] |
| Employee remuneration/benefits disclosure | At least $100,000 per annum, in $10,000 bands, excluding directors from that employee count | [Section211(1)(g)][C211] |
| Shareholder distribution/copy request | 20-working-day dispatch rules; 15-working-day request window; fulfil timely request as soon as practicable | [Sections209][C209], [209A][C209A] |
| Tax statements on written request | Free within 10 working days, report if any | [Section207F][C207F] |
| XRB A1 June2026 amendment | Effective 17 July 2026; mandatory periods beginning on/after 1 January 2027, qualified early adoption | [XRB2026/55][XRB-A1-AMEND] |

## Decision order and working papers

Record a separate evidenced conclusion for each decision, rather than carrying a single 'small', 'large' or 'exempt' label through the workflow:

1. Confirm the legal entity, reporting regime and actual accounting period. Resolve the section 197 alternative-regime exclusion first.
2. Establish the subsidiary/control perimeter and which version of section 45 applies. Reconcile the 2 preceding balance dates and accounting periods to the actual period under review.
3. Establish size using the applicable XRB A2 measurement basis. Test the specific subsidiary route and inactivity override separately.
4. Count voting shareholders under section 199 and establish any valid period-specific opt-in or opt-out.
5. Determine individual or group preparation and any parent-group exception. Determine the applicable XRB reporting tier/election separately.
6. Determine audit, qualified auditor, appointment/report duties and registration. A preparation exception does not by itself establish a registration exception.
7. Determine annual-report preparation, permitted omissions and shareholder distribution. An annual report is distinct from the Companies Office annual return.
8. Build the evidence-linked calendar and reviewer brief. Show each missing decision, responsible person, required evidence and next action. Never certify submission from a draft or deadline calculation alone.

Retain the applicable sources/versions, period calculation, measured size schedule, shareholder/voting reconciliation, each notice/resolution, parent-report evidence, decision matrix and calendar. Recheck the source chain when dates, facts, law or an election changes.

## Accounting periods, subsidiaries and statutory size

Use actual accounting periods and balance dates, including a first, short or changed period. Do not replace '2 preceding accounting periods' with 2 calendar years or automatically use the current year's trial balance. FRA definitions and sections 41–43 govern the accounting period/balance date. Confirm any non-default balance date and necessary authority. [FRA, ss5/41–43][FRA-CURRENT].

Establish subsidiary status under the applicable definitions. The Companies Act includes sections 5–8 and, except for section 207D, entities classified as subsidiaries under applicable financial reporting standards. The FRA also addresses subsidiary/control classification under standards. Board control, voting rights, relevant share/dividend rights, indirect chains and the section 8 qualifications can matter. Do not equate a percentage of issued shares with every control test, or carry the standards extension into section 207D where it is expressly excluded. [Companies Act, s198][C198], [ss5–8][CA-DEFINITIONS], [FRA, ss5/19][FRA-CURRENT].

### Select the size rule by period start

The 2025 amendment commenced on 29 September 2025, but FRA Schedule clause 8 saves the former sections 45/46 for accounting periods commencing before that date. The new subsidiary route is not applied retrospectively merely because the period ends after commencement. The corresponding XRB A2 amendment also applies to periods beginning on or after 29 September 2025. [Amendment Act, ss2/108/111 and Schedule6][REGSYSTEMS2025], [FRA, Schedule cl8][FRA-CURRENT], [former s45][FRA-PREV45], [XRB A2, para27][XRB-A2-CURRENT].

| Period under review | Section 45 approach |
|---|---|
| Begins before 29 September 2025 | Former section 45: the direct 2-period tests below, with the inactivity override. No new subsection (2A) route. |
| Begins on or after 29 September 2025 | Current section 45: direct 2-period tests, the precise subsection (2A) route and the inactivity override. |

For example, an ordinary 1 April 2025–31 March 2026 period uses the former rule. For an established annual 31 March cycle, its 2 preceding periods are the years ending 31 March 2024 and 31 March 2025. Verify the actual dates rather than assuming that cycle.

### Direct 2-period tests

| Entity category | Assets test | Revenue test |
|---|---|---|
| Section 45(1): entity other than an overseas company or subsidiary of an overseas company | Total assets of entity and its subsidiaries, if any, **exceed $66 million at each** of the 2 preceding balance dates | Total revenue of entity and its subsidiaries, if any, **exceeds $33 million in each** of the 2 preceding accounting periods |
| Section 45(2): overseas company or subsidiary of an overseas company | Corresponding total assets **exceed $22 million at each** preceding balance date | Corresponding total revenue **exceeds $11 million in each** preceding period |

Either the complete assets test or the complete revenue test suffices. Equality fails an 'exceeds' test. Exceeding assets in only 1 period and revenue in only the other does not satisfy either test. Use the correct statutory entity category and evidence-supported group perimeter. The legislative amounts are not automatically indexed each year. [Current s45][FRA45], [former s45][FRA-PREV45], [2021 threshold regulations][INFLATION2021].

For periods beginning on or after 29 September 2025, section 45(2A) adds a separate route: an entity has, at its balance date, at least 1 subsidiary that is large **under subsection (1)** for that same accounting period if the entity is within the subsection (1) category, or large **under subsection (2)** for that same period if the entity is within the subsection (2) category. Establish the subsidiary's applicable test and evidence. Do not simplify this to 'any large subsidiary', and do not assume that a subsidiary large solely under subsection (2A) satisfies the specified (1)/(2) condition. [Current s45(2A)][FRA45], [XRB A2, para6A][XRB-A2-HTML].

### Measure before comparing

FRA section 47 requires the relevant threshold standard to be applied. Under XRB A2 paragraphs 8–13:

- If statements are prepared in accordance with XRB accounting standards, use the respective total assets/revenue amounts prepared on the applicable Tier 2 accounting-standard basis at each relevant balance date or period.
- If statements are not prepared, or are not prepared on that specified basis, derive the amounts from accounting records as if the relevant Tier 2 standards applied.
- For a for-profit entity, revenue includes income, revenue and gains required in profit or loss, excluding other comprehensive income. Tax-return turnover, bank receipts and gross invoices are not automatic substitutes.
- Include net amounts only where the standards require or permit net recognition. Establish the applicable group/perimeter and accounting treatment, including relevant eliminations; do not simply add unadjusted ledgers.
- Use policies/standards applicable to each respective date/period. Paragraph 13 does not require retrospective adjustment of the first period merely for policy changes or standards becoming effective in the second.

Retain the reconciliation from source records to each measured amount, basis and adjustments. An unexplained amount is Needs Input rather than an assumed zero. [FRA, s47][FRA-CURRENT], [XRB A2, paras8–13][XRB-A2-HTML], [prior A2, paras8–13][XRB-A2-PRIOR].

## Inactive-entity override

An entity is not large for a period under FRA section 45(3) only if it is inactive for that period **and** delivers the prescribed declaration to the Registrar within 5 months after period end. Inactivity requires, during the period, no derived/deemed income, no expenses and no disposed/deemed-disposed assets, plus no subsidiaries at period end or all subsidiaries inactive. Apply all conditions. [FRA, s45(3)–(5)][FRA45].

Disregard only the specified items: statutory filing fees and associated accounting/other costs; bank charges or other minimal administration costs totalling no more than $50; and bank interest only to the extent it does not exceed those paragraph (b) charges/costs. Do not use statutory filing fees to increase the permitted interest amount, disregard ordinary trading or ignore the whole of an over-limit minimal-cost total. A late/missing declaration does not establish the override. [FRA, s45(5)][FRA45].

Regulation 9 prescribes the Schedule declaration form. It requires 2 directors or the sole director, the entity identifier and period end, with a statutory declaration under the Oaths and Declarations Act 1957 before an authorised witness. Companies Office directs the filer to 'Lodge other documents'; its online route requires the filer's RealMe login and Companies Register account. Prepare a redacted checklist and retain the professional's declaration/delivery evidence. No authenticated submission is performed here. [Regulations, reg9/Schedule][INACTIVE-REGS], [Companies Office inactivity guidance][INACTIVE-GUIDANCE], [lodging route][LODGE-DOCUMENTS].

This override removes the **large** route. Recheck independent public-entity, shareholder-count, opt-in and other-enactment duties. It does not waive section 194 accounting records, tax obligations or the separate Companies Office annual return. [Companies Act, ss194/200/206/208][C194], [preparation][C200], [audit][C206], [annual report][C208].

## Voting shareholders and period-specific choices

Count holders of voting shares at the close of the first day of the accounting period. Joint holders of a parcel count as 1 shareholder. Section 198 requires a currently exercisable meeting-voting right and excludes rights exercisable only on the specified default, class-right, liquidation or inconsequential-control matters. Reconcile the register and actual rights; a later register snapshot or headcount of all investors is insufficient. [Companies Act, ss198/199][C198], [count][C199].

The opting period runs from period start to the earliest of: 6 months after that start; the date of the annual meeting held within that period; or the balance date of a period shorter than 6 months because of registration or a changed balance date. Record the actual earliest endpoint. Establish working-day calculations under the applicable law/calendar rather than assuming weekdays alone. [Section207H][C207H].

| Choice | Eligibility and procedure | What it changes |
|---|---|---|
| Section 207I opt-out | 10+ shareholders; neither large nor public entity; constitution does not expressly disapply the section. At a shareholder meeting within the opting period, at least 95% of votes of shareholders entitled to vote and voting on the question approve. | Select sections 201/202, section 207 and/or section 208 explicitly, for the specified accounting period. |
| Section 207J large-company audit opt-out | Large company; neither public entity nor required to register statements under section 207E; constitution does not expressly disapply the section. Same meeting, opting-period and 95%-of-votes-cast requirement. | Section 207 only, for that period. It does not waive preparation, annual reports or audit under another enactment. |
| Section 207K opt-in | Non-large company with fewer than 10 shareholders. Holder(s) of at least 5% of voting shares give the company written notice within the opting period and no later than 5 working days before its end. | Select section 201 or 202, section 207 and/or section 208 explicitly, for that period. |

[Sections207I][C207I], [207J][C207J], [207K][C207K].

Keep eligibility, voting entitlement, meeting validity, notice/service and the exact provision/period in the working paper. A generic 75% resolution, a bare email agreement or a prior year's election is not sufficient evidence for these statutory conditions. Hold any proposed substitute mechanism for separately verified authority. Do not import the votes-cast denominator into section 207K's voting-share test, section 208(4)'s annual-report agreement or section 211(3)'s permitted-omission agreement.

## Preparation and parent-group exceptions

For the ordinary domestic scope, sections 201/202 apply where the company is large or a public entity, where it has 10+ shareholders without a valid relevant section 207I opt-out, or where a relevant section 207K opt-in applies. An out-of-scope regime must be resolved first. [Sections197/200][C197], [preparation gate][C200].

If the preparation provisions apply, use section 201 when there are no subsidiaries at balance date and section 202 group statements when there is at least 1. Applicable statements must comply with GAAP, be completed in relation to the relevant balance date, be dated and be signed on behalf of the company by 2 directors or its sole director, within 5 months after balance date. Preparation/signature is not established by a draft, a tax return or an auditor's engagement letter. [Sections201][C201], [202][C202].

The parent-group exceptions have conditions of their own:

- For a company A with no subsidiaries, section 200(3) excludes section 201 where A is a subsidiary at balance date of B, B is NZ-incorporated or registered/deemed registered under Part 18, GAAP group statements covering B, A and **all** B's other subsidiaries are completed for that balance date under an enactment and A has not opted into section 201 under section 200(1)(e).
- For A with subsidiaries, section 202(2) provides the corresponding group-statement exception with the specified parent, complete group coverage, same balance date and no relevant section 200(1)(e) opt-in.

Retain the parent's status, actual completed full-group statements, balance-date match and opt-in search. A parent promise, partial subgroup report or merely having an overseas parent cannot establish the exception. Check section 207D's distinct registration exception separately; it adds completion/signature timing and actual group-statement/auditor-report registration or lodgement conditions. [Sections200/202][C200], [group exception][C202], [registration exception][C207D].

## XRB accounting tier is a separate decision

XRB A1 applies when the entity prepares or opts under an enactment to prepare GPFR under XRB standards. Confirm the actual for-profit/public-benefit classification, public accountability, sector, period and election. Public accountability includes the specified publicly traded/in-process instruments and broad fiduciary holding as a primary business; the NZ FMC rules and qualifications also matter. Incidental holding does not by itself settle public accountability. Refer uncertain status for qualified determination. [XRB A1, paras2–13][XRB-A1-CURRENT].

For the scoped private sector for-profit company under the applicable pre-2027 rules, Tier 1 applies if it has public accountability, or if otherwise eligible Tier 2 has not been elected. An entity without public accountability that is not a large for-profit public sector entity may elect Tier 2 NZ IFRS RDR, subject to the transition rules. Being 'large' under FRA section 45 does **not** by itself force a private sector company into Tier 1. RDR is a supported disclosure regime, not permission to omit recognition, measurement or every note. Establish every applicable requirement and concession. [XRB A1, paras14–23][XRB-A1-CURRENT].

Where a Tier 2 entity acquires public accountability, Tier 1 applies for that same reporting period. Where a Tier 1 entity ceases to have public accountability, it remains Tier 1 for that period; Tier 2 may be elected for the following period if eligible. Check applicable transition requirements rather than changing tier on the event date or assuming that all accounting policies can remain unchanged. [XRB A1, paras24–30][XRB-A1-CURRENT].

Record the applicable version and any early adoption. The official A1 index identifies a prior March 2024 compilation, a February 2025 compilation applying to periods beginning on/after 1 January 2026 with earlier application permitted and a June 2026 compilation for periods beginning on/after 1 January 2027 with earlier application permitted. The selected for-profit paragraphs 14–30 in the prior and February 2025 compilations are identical; this is not whole-standard equivalence. [A1 index][XRB-A1-INDEX], [prior A1][XRB-A1-PRIOR], [February2025 A1][XRB-A1-CURRENT], [June2026 A1][XRB-A1-NEXT].

The instrument titled '2025 Amendments' was issued in June 2026, published on 19 June 2026 and took effect on 17 July 2026. Its mandatory application begins with the first period **beginning on/after 1 January 2027**, continuing thereafter. Early adoption requires a period beginning before that mandatory date which does not end before 17 July 2026, first application in that period's report and disclosure that the standard was applied. It applies in following periods too. The new public-accountability wording cannot be selected merely because today's date is after 17 July 2026. The public sector expense-threshold amendment is distinct from FRA's statutory assets/revenue tests. [XRB2026/55, paras0.5/0.6 and amendments][XRB-A1-AMEND].

## Audit, auditor and report controls

For the ordinary domestic scope, section 207 applies through section 206 to large companies, public entities, 10+ shareholder companies without a valid relevant section 207I opt-out and fewer-than-10 companies with a relevant section 207K opt-in, subject to the valid section 207J large-company opt-out. It requires a qualified auditor to audit the statements prepared under sections 201/202/204, **if any**. Do not invent an audit of nonexistent statements merely from a selected audit provision, or treat an exemption from this section as an exemption from every enactment. [Sections206][C206], [207][C207], [207J][C207J].

Section 207 itself supplies no separate universal audit deadline. Plan the audit early enough to meet applicable financial-statement registration, annual-report and other duties. Preserve their respective deadlines and required report content. [Sections207][C207], [207E][C207E], [211][C211].

Confirm that the proposed auditor is qualified **for that kind of entity** under FRA sections 35/36 and is not disqualified. The statutory categories and independence conditions matter; an accounting designation alone is insufficient. Check relevant membership/accreditation, licensing/recognition or registered corporate-audit-firm status and conflicts. FRA section 37 addresses partnership appointment by firm name and prohibits an unqualified partner acting; sections 38/39 address access to records and information/explanations. The professional must confirm the actual auditor and appointment evidence. [FRA, ss34–39][FRA-CURRENT], [s35][FRA35], [s37][FRA37].

Where an enactment requires audit, section 207P governs appointment at the annual meeting in the period and permits directors to appoint the first auditor before the first annual meeting. Automatic reappointment has exceptions and does not apply to the first auditor. Section 207Q gives the Registrar appointment powers after annual-meeting failure or a casual vacancy unfilled for 1 month, and requires company notification within 5 working days after that power becomes exercisable. Section 207R addresses written resignation to the board, shareholder notification as soon as practicable and filling a casual vacancy. Public entities use the Auditor-General route and are outside this core. Full replacement/retirement procedures require further source work; these selected controls are not the entire auditor lifecycle. [Sections207P][C207P], [207Q][C207Q], [207R][C207R], [207T][C207T].

Audit and report must follow applicable auditing/assurance standards; the auditor reports to shareholders. If the auditor's report indicates Companies Act non-compliance, the auditor must send the report and relevant statements to **both** the Registrar and XRB within 7 working days after signing. This is a separate reporting duty, not a general extension to the filing deadline. [Sections207A][C207A], [207B][C207B], [207C][C207C].

## Registration of financial statements

For a domestic company, section 207D(1)(b) requires **large** status and shares carrying, in aggregate, the right to exercise/control at least **25% of meeting voting power**, held by the listed categories: a body corporate incorporated outside NZ, its subsidiary or a person not ordinarily resident in NZ. Reconcile the actual holders, categories and powers without double counting. This is not investor headcount, a generic beneficial-ownership percentage or the separate section 45 overseas-subsidiary test. [Section207D][C207D].

For this section, ordinarily resident means domiciled in NZ **or** living in NZ with the place the person usually lives, and has lived for the immediately preceding 12 months, in NZ, allowing occasional absence. Do not substitute an income-tax residence conclusion for the statutory test. Section 198's standards-based subsidiary extension expressly does not apply in section 207D; establish the applicable Companies Act subsidiary relationship. [Sections207D(3)][C207D], [198][C198], [5–8][CA-DEFINITIONS].

Section 207D(2)'s parent exception requires the specified NZ-incorporated/registered parent, GAAP full-group statements covering B, A and all other B subsidiaries completed **and signed within section 202's time**, and a copy of those group statements **and the auditor's report** actually delivered for registration under the Act or lodged under another Act. Do not infer this from section 200/202's preparation exception alone. [Section207D(2)][C207D].

Where section 207E applies, deliver for registration within 5 months after balance date the statements completed under sections 201/202/204, **if any**, and auditor's report, **if any**, with any prescribed fee. Resolve the actual document set and filing mechanics before claiming readiness, especially where a parent preparation exception applies but the parent registration exception is not evidenced. No generic requirement to create an otherwise exempt standalone statement is inferred here. [Section207E][C207E].

## Annual report to shareholders

Section 208 has its own gate: large company, public entity, company subject to the specified FMC/FRA reporting, 10+ shareholders without a valid relevant section 207I opt-out or fewer than 10 with a relevant section 207K opt-in. The board must prepare the annual report within 5 months after balance date. It is distinct from the Companies Office annual return and from a copy of financial statements alone. [Section208][C208].

For a **large company**, section 208(4) removes the annual-report preparation duty only where no company/group statements are required under Part 11, FMC Part 7 **or any other enactment**, and holders of at least **95% of voting shares** agree for that period. A parent preparation exception alone, an audit opt-out or 95% of votes cast is insufficient. [Section208(4)][C208].

### Contents and permitted omissions

The annual report must be written and dated. Subject to the precise section 211(3) agreement, it includes:

- Material changes in the nature of the company's/subsidiaries' business or classes of business in which it has an interest, to the extent the board believes material for shareholders' appreciation of affairs and not harmful to the company's/subsidiaries' business.
- Financial/group statements required under Part 11, FMC Part 7 or another enactment, if any, and the auditor's report where required. If climate reporting applies, the specified climate matters must also be included; obtain the separate source chain.
- Interests-register entries; each director/former director's remuneration and benefits; non-director employee/former-employee remuneration and benefits at or above $100,000 per annum in $10,000 bands; total donations; directors at period end and those ceasing during the period; and audit fees separately from other fees payable to the auditor.
- Signature on behalf of the board by 2 directors or the sole director. Group-report preparers also include the specified section 211(1)(e)–(j) information for subsidiaries.

Holders of at least **95% of voting shares** may agree to omit **only** section 211(1)(a), (e)–(j) and subsection (2). This does not remove the written/dated requirement, required financials/audit/climate matters or signature. It does not waive preparation of the whole annual report. Section 211A is repealed and supplies no blanket inactive-company waiver. [Sections211][C211], [211A][C211A].

### Distribution and electronic access

Under section 209, send every shareholder a copy of the annual report **or** the prescribed notice at least **20 working days before the annual meeting**. If no annual meeting is required under section 120(5) or 122(4), send it within **20 working days after the report is prepared**. Establish the actual no-meeting authority; choosing not to meet is insufficient. Section 209(1) does not apply when section 208 does not require the annual report, subject to the actual conditions. [Section209][C209].

The notice must explain the right to request a free copy within **15 working days of receipt**, the electronic-copy right and how to obtain it, plus the prescribed concise-report statements if one was prepared. A concise report is not an arbitrary summary: section 209(5) specifies GAAP financial/group statements with any audit report or GAAP summary financial statements for the relevant company/group. Its detailed preparation standard remains outside this core. [Section209(3)/(5)][C209].

For a timely request, send the free annual report as soon as practicable. That full-report request becomes a standing annual request until revoked, except where section 208 does not require the report for the period. A timely concise-report request also requires a free copy as soon as practicable. The **15 working days** is the shareholder request window, not the company's delivery allowance. [Section209A][C209A].

Maintain electronic availability as described in the notice at all reasonable times from the notice date until the board's section 209(1) action for the next period, readily accessible for subsequent reference. The corresponding duty applies to a concise report where the notice says it was prepared. [Section209B][C209B].

A shareholder may give/revoke a written document waiver, but purporting to waive **both** the annual-report copy and notice is invalid where the duty applies. Retain each actual waiver and check its scope. The accidental-omission rule concerning validity of proceedings is not a substitute for compliant delivery. The FMC-specific alternative in section 209C requires separate work. [Sections212][C212], [213][C213], [209C][C209C].

## Tax statements, records and calendar

If no company/group statements are prepared under the Companies Act or FMC Part 7 but statements are prepared under/for Inland Revenue Acts, a shareholder may request them in writing at any time. Section 207F requires a free copy within **10 working days**, with auditor's report if any. This is not an audit-request power under section 207G. Maintain section 194 accounting records and separately establish tax-statement obligations, which this guide does not compute. [Sections207F][C207F], [207G][C207G], [194][C194], [195][C195].

| Event | Selected deadline/control | Evidence to retain |
|---|---|---|
| Applicable financial/group statements | Complete, date and sign within 5 months after balance date | Final GAAP statements, date, actual required director signatures and review |
| Applicable registration | Deliver within 5 months after balance date | Correct document set, fee basis, submission receipt and register readback |
| Inactive-entity override | Prescribed declaration delivered within 5 months after period end | Full inactivity reconciliation, declaration/witness and receipt |
| Annual-report preparation | Within 5 months after balance date | Written/dated final report and required board signatures |
| Shareholder report/notice | At least 20 working days before annual meeting, or verified no-meeting route within 20 working days after preparation | Actual event dates, calendar, recipients, dispatch and valid waiver evidence |
| Notice recipient's copy request | Within 15 working days after receipt | Receipt/request dates; free copy sent as soon as practicable |
| Tax statements under section 207F | Within 10 working days after written request | Actual request, free copy and delivery evidence |
| Auditor's non-compliance report under section 207C | Within 7 working days after report signing to both bodies | Auditor's report, statements and both delivery records |

The calendar does not replace eligibility, document or authority checks. Apply actual statutory time-calculation rules, holidays and service facts. No deadline is certified from the synthetic offsets below.

## Synthetic worked cases and self-checks

These cases use invented facts, no client data and independently assumed legal/calendar facts where stated. The executable blocks check arithmetic only; they do not establish statutory classification, valid resolutions, GAAP amounts or working-day calendars. Complete the accompanying decision trace and obtain qualified review.

### Case 1: equality is not exceeding

For a subsection (1) entity, properly measured preceding assets are $66,000,000/$67,000,000 and revenue $32,000,000/$33,000,000. Assume no applicable (2A) route or inactivity override. Neither complete test passes: first assets equal the threshold and second revenue equals it. Positive excess is needed at **both** dates or in **both** periods for the respective test.

```oa-check
name: NZ reporting strict threshold margins
inputs:
  assets_first: 66000000
  assets_second: 67000000
  revenue_first: 32000000
  revenue_second: 33000000
steps:
  assets_first_margin: assets_first - 66000000
  assets_second_margin: assets_second - 66000000
  revenue_first_margin: revenue_first - 33000000
  revenue_second_margin: revenue_second - 33000000
expected:
  assets_first_margin: 0
  assets_second_margin: 1000000
  revenue_first_margin: -1000000
  revenue_second_margin: 0
tolerance: 0
```

### Case 2: crossing different tests in different periods

Properly measured subsection (1) assets are $67,000,000/$65,000,000 and revenue $32,000,000/$34,000,000. Assume no other large route. Assets pass only first, revenue only second, so neither 2-period test passes. Do not OR the test separately within each year and then combine the years.

```oa-check
name: NZ reporting mixed two-period margins
inputs:
  assets_first: 67000000
  assets_second: 65000000
  revenue_first: 32000000
  revenue_second: 34000000
steps:
  assets_first_margin: assets_first - 66000000
  assets_second_margin: assets_second - 66000000
  revenue_first_margin: revenue_first - 33000000
  revenue_second_margin: revenue_second - 33000000
expected:
  assets_first_margin: 1000000
  assets_second_margin: -1000000
  revenue_first_margin: -1000000
  revenue_second_margin: 1000000
tolerance: 0
```

### Case 3: domestic overseas subsidiary uses the relevant category

A domestic company is independently established to be a subsidiary of an overseas company. Measured preceding assets are $22,000,000/$22,100,000 and revenue $11,100,000/$11,200,000. The subsection (2) revenue test passes in both periods, although the assets test fails at the first equality. Do not apply $66m/$33m merely because the subsidiary is incorporated in NZ. Assume no inactivity override.

```oa-check
name: NZ reporting overseas-subsidiary margins
inputs:
  assets_first: 22000000
  assets_second: 22100000
  revenue_first: 11100000
  revenue_second: 11200000
steps:
  assets_first_margin: assets_first - 22000000
  assets_second_margin: assets_second - 22000000
  revenue_first_margin: revenue_first - 11000000
  revenue_second_margin: revenue_second - 11000000
expected:
  assets_first_margin: 0
  assets_second_margin: 100000
  revenue_first_margin: 100000
  revenue_second_margin: 200000
tolerance: 0
```

### Case 4: new subsidiary route and period saving

In 2 separate hypothetical assessments, an entity in the subsection (1) category fails its own direct 2-period tests and acquires a subsidiary only during the current period. At current balance date that subsidiary is independently large under subsection (1) for the same period. For an assessment beginning 1 April 2025, the saved former rule has no (2A) route. For an otherwise equivalent assessment beginning 1 April 2026, current (2A)(a) supplies a large route. Assume no inactivity override. Do not retroactively import the route into the earlier period.

Variant: a subsidiary is large only under (2A), or meets only the other category's direct test. That label alone does not establish the specified (1)/(2) subsidiary condition. Obtain the actual statutory test and period evidence.

### Case 5: inactive costs and interest have different limits

Assume all other inactivity conditions, no subsidiaries and timely prescribed declaration. Statutory filing fees/associated costs are $200, minimal administration/bank costs $50 and bank interest $45. The specified items can be disregarded. The interest limit derives from the $50 costs, not $250 of combined costs. If minimal costs instead total $50.01, they fail the no-more-than-$50 condition; do not disregard the whole amount. If those costs remain $50 but interest is $50.01, the $0.01 excess is not disregarded. Either variant fails inactivity on the stated facts.

```oa-check
name: NZ reporting inactive-cost limits
inputs:
  statutory_costs: 200
  minimal_costs: 50
  interest: 45
  variant_minimal_costs: 50.01
  variant_interest: 50.01
steps:
  combined_costs: statutory_costs + minimal_costs
  minimal_limit_margin: 50 - minimal_costs
  disregarded_interest: min(interest, minimal_costs)
  variant_cost_excess: variant_minimal_costs - 50
  variant_interest_excess: max(0, variant_interest - minimal_costs)
expected:
  combined_costs: 250
  minimal_limit_margin: 0
  disregarded_interest: 45
  variant_cost_excess: 0.01
  variant_interest_excess: 0.01
tolerance: 0
```

Variant: valid inactivity removes large status, but the company has 12 section 199 shareholders and no valid opt-out. The independent 10+ shareholder preparation, audit and annual-report gates still require assessment. 'Inactive' is not an all-duties exemption.

### Case 6: first-day count, joint holders and narrow opt-in

At close of the first day there are 8 separate individual voting holders and 1 jointly held voting parcel held by 2 other individuals; 4 further persons hold only non-voting shares. The section 199 count is 9, not 10 or 14. A later count of 11 voting holders does not replace that first-day count. Assume a non-large company and no independent public-entity/other-enactment duty. Holders of 50 of 1,000 voting shares give a written notice selecting **audit only**. They meet the 5% holding threshold. The notice is valid only if the actual statutory timing/service conditions are established; selecting audit does not itself opt into preparation or the annual report. Section 207 still relates to the specified statements, if any.

```oa-check
name: NZ reporting shareholder count and opt-in holding
inputs:
  separate_holders: 8
  joint_parcels: 1
  notice_shares: 50
  voting_shares: 1000
steps:
  counted_holders: separate_holders + joint_parcels
  notice_percent: notice_shares / voting_shares * 100
expected:
  counted_holders: 9
  notice_percent: 5
tolerance: 0
```

### Case 7: earlier annual meeting shortens the opting period

For a 1 April 2026 start, a valid annual meeting held on 30 June 2026 makes that earlier date the endpoint rather than the 6-month endpoint. An attempted opt-out meeting on 1 July 2026 is outside that opting period. For an opt-in, independently verified calendar/service facts show a notice given 6 working days before the endpoint; it clears the 5-working-day condition. A notice given only 4 working days before does not. These offsets are assumed verified inputs, not calendar calculations.

```oa-check
name: NZ reporting opt-in timing margins
inputs:
  early_notice_working_days: 6
  late_notice_working_days: 4
steps:
  early_margin: early_notice_working_days - 5
  late_margin: late_notice_working_days - 5
expected:
  early_margin: 1
  late_margin: -1
tolerance: 0
```

### Case 8: 95% of votes cast is not 95% of voting shares

Assume a non-large, non-public company with 12 shareholders, an eligible constitution and a valid meeting within the opting period. All 1,000 voting shares carry 1 vote; 200 entitled votes are cast on an **audit-only** opt-out and 190 favour it. Approval is 95% of votes cast, sufficient for the stated section 207I route. Only 19% of all voting shares support it. Preparation and annual-report duties were not selected for opt-out. This vote does not establish section 211(3)'s 95%-of-voting-shares agreement. A section 208(4) waiver also has its separate large-company/no-required-statements conditions.

```oa-check
name: NZ reporting votes-cast and voting-share denominators
inputs:
  yes_votes: 190
  cast_votes: 200
  all_voting_shares: 1000
steps:
  cast_approval_percent: yes_votes / cast_votes * 100
  all_share_support_percent: yes_votes / all_voting_shares * 100
expected:
  cast_approval_percent: 95
  all_share_support_percent: 19
tolerance: 0
```

### Case 9: exactly 25% filing voting power blocks the large-company audit opt-out

A large domestic company has no parent registration exception. Distinct qualifying holders carry 80 and 170 of 1,000 meeting votes; all section 207D categories and powers are evidenced and there is no overlap. Their aggregate is exactly 25%, meeting the registration threshold. Section 207J is unavailable because section 207E applies, even if a 95%-of-votes-cast audit opt-out is proposed. The legal categories and large status cannot be proved by this arithmetic.

```oa-check
name: NZ reporting registration voting power
inputs:
  qualifying_votes_a: 80
  qualifying_votes_b: 170
  total_meeting_votes: 1000
steps:
  qualifying_votes: qualifying_votes_a + qualifying_votes_b
  qualifying_percent: qualifying_votes / total_meeting_votes * 100
expected:
  qualifying_votes: 250
  qualifying_percent: 25
tolerance: 0
```

### Case 10: parent preparation exception does not prove registration exception

A has no subsidiaries and is a subsidiary of an NZ-incorporated B. A has no relevant opt-in. GAAP full-group statements covering B, A and all other B subsidiaries are completed for A's balance date under an enactment, establishing the stated section 200(3) preparation exception. A independently meets section 207D(1)(b). There is no evidence that the required group statements were signed within time or that those statements **and auditor's report** were registered/lodged. Section 207D(2) is unproved. Return Needs Input for the registration plan and evidence, preserving section 207E's 'if any' wording; do not invent an otherwise exempt standalone statement or mark filing complete.

### Case 11: statutory size does not settle accounting tier or amendment adoption

An independently established private sector for-profit company is large under FRA section 45 but has no public accountability. Under the applicable A1 rules, eligible Tier 2 needs an actual election; absent that election use Tier 1. If public accountability arises in the period, Tier 1 applies that period. If it ceases in the period, retain Tier 1 for that period and assess eligible Tier 2 for the next.

A 31 March 2026 period end is before 17 July 2026, so it cannot be the early-adoption period for XRB2026/55. A 1 April 2026–31 March 2027 period may qualify only with actual application/disclosure and the other conditions; the calendar date alone does not adopt it. A period starting 1 January 2027 is within mandatory application. No actual entity's public accountability or election is presumed.

### Case 12: annual-report waiver and contents agreement are different

Assume a large company has **no** company/group statements required under Part 11, FMC Part 7 or another enactment. Holders of 950 of its 1,000 voting shares agree for the period, satisfying the stated section 208(4) holding threshold and, with all assumed conditions, removing that annual-report preparation duty. If any required statements exist, this route fails regardless of the agreement.

For a different company with a required annual report, the same 95% voting-share agreement under section 211(3) can remove only its listed optional content. Required financials/audit/climate matters, written/dated form and director signature remain. Neither a 95%-of-votes-cast resolution with fewer supporting shares nor a generic 'all reporting waived' entry proves these conditions.

```oa-check
name: NZ reporting annual-report agreement holding
inputs:
  supporting_voting_shares: 950
  total_voting_shares: 1000
steps:
  support_percent: supporting_voting_shares / total_voting_shares * 100
expected:
  support_percent: 95
tolerance: 0
```

### Case 13: employee bands include benefits and exclude directors from the employee count

For an annual report without a section 211(3) omission agreement, assume 4 non-director employees' annual remuneration/benefits totals are $99,999, $100,000, $109,999 and $110,000. The $100,000 total includes $99,500 remuneration plus $500 benefits. Count 2 employees in the $100,000–$109,999 band and 1 in $110,000–$119,999; the $99,999 employee is below the trigger. A director receiving $150,000 is separately disclosed under the director provision and is excluded from these employee counts. Verify actual statutory annual amounts and any group disclosures; these whole-dollar examples do not prescribe accounting rounding.

```oa-check
name: NZ reporting remuneration benefits and band boundaries
inputs:
  remuneration: 99500
  benefits: 500
  near_top_total: 109999
  next_band_total: 110000
steps:
  remuneration_total: remuneration + benefits
  first_band_index: floor((remuneration_total - 100000) / 10000)
  near_top_band_index: floor((near_top_total - 100000) / 10000)
  next_band_index: floor((next_band_total - 100000) / 10000)
expected:
  remuneration_total: 100000
  first_band_index: 0
  near_top_band_index: 0
  next_band_index: 1
tolerance: 0
```

### Case 14: distribution, requests and access are separate controls

Assume an actual applicable statutory working-day calendar has independently established that dispatch is 20 working days before the annual meeting. It meets that lead-time condition; dispatch 19 working days before does not. A shareholder's full-report request received on the 15th working day after receiving the notice is timely. Send the free report as soon as practicable and retain the standing annual request; do not treat 15 days as the delivery allowance. Maintain the promised electronic access until the next period's section 209(1) action, rather than removing it after the meeting.

Variant: the shareholder purports to waive both report and notice whilst section 209(1) applies. That waiver is invalid. A validly omitted annual meeting changes the dispatch trigger only if the actual section 120(5)/122(4) route is established.

```oa-check
name: NZ reporting independently supplied dispatch offsets
inputs:
  compliant_lead_working_days: 20
  short_lead_working_days: 19
steps:
  compliant_margin: compliant_lead_working_days - 20
  short_margin: short_lead_working_days - 20
expected:
  compliant_margin: 0
  short_margin: -1
tolerance: 0
```

### Case 15: tax statements and records remain after a reporting opt-out

Assume no Companies Act/FMC statements are prepared, but tax statements are prepared under/for Inland Revenue Acts. A shareholder's written section 207F request requires a free copy within 10 working days, with an auditor's report if any. A reporting opt-out does not eliminate this access duty or section 194 records. A Companies Office annual-return obligation must be checked separately, not marked satisfied by tax-statement delivery.

## Reviewer handoff and completion record

For each company/period, show the evidence and decision for: legal regime; period/version; subsidiary/control perimeter; both size tests and any (2A)/inactive route; first-day shareholder count; each election; individual/group preparation and parent exceptions; accounting tier and adoption; audit/qualified auditor/appointment; registration; annual report, permitted omissions and distribution; tax-statement access; and each calendar event. Cross-reference contrary evidence and unresolved matters rather than silently choosing a convenient answer.

The professional must review the actual source conditions, GAAP basis, resolutions/notices, signatures, auditor status, final documents and submission evidence. This guide supplies selected source-cited controls and synthetic arithmetic, not a completed financial-statement workflow, actual company exemption or practitioner review. Record every open mandatory slot and outstanding output. Do not award whole reporting-topic completion or filing status from this core.

Related selected company work: [register and annual return](nz-company-register-core.md), [capital, records and shareholder decisions](nz-company-capital-records-core.md) and [ordinary company IR4](nz-company-income-tax-ir4.md). Each retains its own scope, periods and completion gates.

## Topical self-check and revision record

Before delivering any permitted working paper, complete the universal and domain checks and record these additions:

1. Every regime/period, measured amount and subsidiary/ownership definition has evidence; the saved former/current rule and any standard adoption are correct.
2. Both observations in each size test use the required basis; equality, mixed-test passes, the exact (2A) child route and every inactivity condition are handled separately.
3. First-day shareholder count, joint parcels, voting rights, votes cast, voting shares and registration voting power are reconciled without denominator substitution.
4. Every selected provision, constitution condition, meeting/notice, opting period and working-day calculation is evidenced; no previous-period choice is silently carried forward.
5. Preparation, audit, registration and annual-report exceptions are tested independently, including parent-report completion, signature, timing and actual delivery where required.
6. Accounting tier/election/transition, qualified auditor and all mandatory report contents/signatures/distribution are established or explicitly held. Do not treat a content omission as a whole-report waiver.
7. The refusal trace covers every loaded code with the exact messages for fired codes; each default, alternative, cash impact and NZ$0 review flag is disclosed. All open conditions have a responsible person and next evidence/action in the reviewer brief.
8. No full financial-statement output, actual classification or completed filing is claimed from this core. All 12 mandatory country slots, 6 domain outputs, universal outputs, confirmation and review remain required for that engagement.

Revision: v0.1, 14 November 2026. Initial selected reporting-readiness core, period-specific size/standards controls and synthetic cases; source-cited tier 2 pending practitioner review. No full reporting-topic completion is recorded.

## Primary sources

Sources were checked on 14 November 2026. 'Latest' statute links can change; retain the consolidation, amendment/application and period evidence used. XRB compilations and the 2026 amendment have distinct effective/application conditions described above.

[C197]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320884/
[FRA-CURRENT]: https://www.legislation.govt.nz/act/public/2013/101/en/latest/
[XRB-A1-CURRENT]: https://www.xrb.govt.nz/dmsdocument/5470/
[CA-VERSION]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320887/?active_tab=version
[B126V5]: https://www.legislation.govt.nz/act/public/2023/35/en/latest/sections/LMS469579/
[B126V3]: https://www.legislation.govt.nz/act/public/2023/35/en/latest/sections/LMS469452/
[B126V6]: https://www.legislation.govt.nz/act/public/2026/48/en/latest/sections/LMS1506038/
[B126V4]: https://www.legislation.govt.nz/act/public/2026/48/en/latest/sections/LMS737990/
[B126V2]: https://www.legislation.govt.nz/act/public/2025/67/en/latest/
[B126V7]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/319/en/latest/
[FRA-VERSION]: https://www.legislation.govt.nz/act/public/2013/101/en/latest/sections/DLM5206501/?active_tab=version
[LAA2026]: https://www.legislation.govt.nz/act/public/2026/7/en/latest/
[C198]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320886/
[CA-DEFINITIONS]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/
[REGSYSTEMS2025]: https://www.legislation.govt.nz/act/public/2025/11/en/latest/
[FRA-PREV45]: https://www.legislation.govt.nz/act/public/2013/101/en/2022-10-27/sections/DLM5206501/
[XRB-A2-CURRENT]: https://www.xrb.govt.nz/dmsdocument/5793/
[FRA45]: https://www.legislation.govt.nz/act/public/2013/101/en/latest/sections/DLM5206501/
[INFLATION2021]: https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2021/307/en/latest/
[XRB-A2-HTML]: https://standards.xrb.govt.nz/standards-navigator/xrb-a2/
[XRB-A2-PRIOR]: https://www.xrb.govt.nz/dmsdocument/4303/
[INACTIVE-REGS]: https://www.legislation.govt.nz/regulation/public/2015/0117/latest/DLM6479993.html
[INACTIVE-GUIDANCE]: https://companies-register.companiesoffice.govt.nz/help-centre/financial-reporting/who-needs-to-submit-financial-statements/
[LODGE-DOCUMENTS]: https://companies-register.companiesoffice.govt.nz/help-centre/managing-your-online-account/lodging-other-documents/
[C194]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320874/
[C200]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320893/
[C206]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321101/
[C208]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321105/
[C199]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320887/
[C207H]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041581/
[C207I]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041583/
[C207J]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041584/
[C207K]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041585/
[C201]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320894/
[C202]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320895/
[C207D]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041571/
[XRB-A1-INDEX]: https://www.xrb.govt.nz/standards/accounting-standards/for-profit-entities/xrb-a1/
[XRB-A1-PRIOR]: https://www.xrb.govt.nz/dmsdocument/5156/
[XRB-A1-NEXT]: https://www.xrb.govt.nz/dmsdocument/5969/
[XRB-A1-AMEND]: https://www.xrb.govt.nz/dmsdocument/6091/
[C207]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321102/
[C207E]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041575/
[C211]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321118/
[FRA35]: https://www.legislation.govt.nz/act/public/2013/101/en/latest/sections/DLM4632944/
[FRA37]: https://www.legislation.govt.nz/act/public/2013/101/en/latest/sections/DLM4632947/
[C207P]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041591/
[C207Q]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041592/
[C207R]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041593/
[C207T]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041595/
[C207A]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041565/
[C207B]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041568/
[C207C]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041569/
[C211A]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321125/
[C209]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321107/
[C209A]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321111/
[C209B]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321113/
[C212]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321127/
[C213]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM321130/
[C209C]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM7077722/
[C207F]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041577/
[C207G]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM6041579/
[C195]: https://www.legislation.govt.nz/act/public/1993/105/en/latest/sections/DLM320875/

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
