---
name: cross-border-workflow-base
description: >
  Master orchestrator for multi-jurisdiction cases. Coordinates all 7 accounting domains
  (tax, bookkeeping, payroll, VAT/GST, e-invoicing, financial statements, transfer pricing)
  across multiple countries. Use when the user mentions two or more jurisdictions, foreign
  income, relocation, foreign subsidiaries, importing/exporting, or remote workers abroad.
  This skill activates BEFORE any single-country skill when a cross-border element is detected.
  It produces a consolidated compliance map across all involved jurisdictions.
version: 1.1
category: foundation
depends_on:
  - tax-residency-planning
  - permanent-establishment-risk
  - withholding-tax-matrix
  - eu-social-security-coordination
  - eu-directives-cross-border
  - oecd-model-treaty-defaults
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: cross-border
---

# Cross-Border Workflow Base v1.1: Multi-Jurisdiction Method

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### What this file is

This is the **master orchestrator** for any case involving more than one jurisdiction. It coordinates all seven accounting domains across multiple countries and produces a unified compliance map. Its shared workflow, coordination controls and bounded authority illustrations do not establish a worldwide tax law. Each affected country, entity, period, treaty/protocol/MLI position and actual payment/supply needs its applicable law and current primary evidence. A treaty model, a customer's country and a named accountant's method are not themselves a completed country conclusion or approval of the client output.

**This file activates when a cross-border element is detected.** It sits above individual country skills and below the global router. The global router hands off to this skill when it detects multi-jurisdiction signals; this skill then loads the relevant country skills and coordinates them.

---

## Section 1 , When this skill activates (detection triggers)

Activate this skill when ANY of the following signals are present in the user's message or context:

| Signal Category | Examples |
|----------------|----------|
| Two or more countries mentioned | "I live in Germany but have clients in the US and UK" |
| Foreign income or clients | "I invoice clients abroad", "I receive payments from overseas" |
| Relocation or moving | "I'm moving from the UK to Portugal", "I relocated last year" |
| Foreign company or subsidiary | "My company has a branch in Ireland", "I set up an LLC in the US" |
| Importing or exporting | "I sell goods to EU customers", "I import from China" |
| Remote workers abroad | "My developer works from Poland", "I have a remote team in India" |
| Cross-border payments | "Withholding tax was deducted", "I need to claim treaty relief" |
| Digital nomad signals | "I work from different countries", "I travel while working" |
| Intercompany transactions | "Transfer pricing", "management fees between entities" |
| Social security abroad | "Which country do I pay social security in", "A1 certificate" |

**If none of these signals are present, do NOT activate this skill.** Hand off to the single-country workflow instead.

---

## The method, step by step

### Section 2: The cross-border intake workflow (10 steps)

Execute these ten steps in order. Do not skip. Do not reorder. Build evidence workpapers during the process; only assemble the final consolidated map after the necessary cross-domain checks. Unknowns remain explicit rather than invented as a higher-tax answer.

### Step 1 , Map all jurisdictions involved

Identify every country that has a role in the user's situation. Classify each:

| Role | Definition | Example |
|------|-----------|---------|
| **Resident country** | Each actual domestic residence claim and separate treaty result, individual or entity | Living in Germany is a fact to investigate, not automatic residence for every person/entity |
| **Source country** | Country determined by the actual income-type sourcing rule | A US payer does not by itself make service income US-source; place of performance can decide [IRS sourcing](https://www.irs.gov/individuals/international-taxpayers/source-of-income-personal-service-income) |
| **Company country** | Where a business entity is incorporated | Ireland (where the Ltd is registered) |
| **Employment country** | Where work is physically performed | Poland (where the remote worker sits) |
| **Supply country** | Actual goods movement, establishment, customer status, supply type and statutory place-of-supply rule | A French customer/delivery location is not alone a universal VAT conclusion [Commission place of taxation](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en) |

A single country may have multiple roles. List all. Read the complete record and timeline first, then identify the exact missing role/source/residence fact. Keep supported work moving; one jurisdiction may have disputed roles or multiple entities without an invented default.

### Step 2 , Classify the cross-border scenario type

Every cross-border case fits one or more of these types:

| Type | Description | Primary domains triggered |
|------|-------------|--------------------------|
| **Type A** | Freelancer/business with foreign clients | VAT place of supply + WHT + income tax |
| **Type B** | Relocated individual (mid-year or recent move) | Residency determination + split-year + exit tax |
| **Type C** | Company with foreign employees or remote workers | Payroll + social security coordination |
| **Type D** | Multi-entity group with cross-border transactions | Transfer pricing + PE risk + consolidated accounts |
| **Type E** | Digital nomad / no fixed base / perpetual traveller | Residency tie-breaker + PE risk + SS coordination |
| **Type F** | Foreign company formation | Formation + substance requirements + CFC rules |

A case may be multiple types simultaneously (e.g., a freelancer who relocated AND has foreign clients = Type A + Type B). Identify all applicable types.

### Step 3 , Load relevant country skills

For each jurisdiction identified in Step 1, determine which domain skills are needed:

1. **Tax** , income tax / corporate tax skill for the country
2. **Bookkeeping** , chart of accounts, transaction classification
3. **Payroll** , if employees or the user is employed there
4. **VAT/GST** , if supplies cross that border
5. **E-invoicing** , if the country mandates electronic invoicing
6. **Financial statements** , if filing obligations exist there
7. **Transfer pricing** , if related-party transactions cross that border

Load only the required country/domain methods using their actual returned slugs, versions, dates and approval labels. Check publication availability, not merely source presence. At the checked catalogue snapshot, `withholding-tax-matrix` and `eu-social-security-coordination` are held for sources and this method is consequently held as their dependent. Preserve the topics, but report an unavailable load honestly and use current official country/treaty evidence for any supported work; never pretend a held companion was retrieved. This update does not change their status or the generated catalogue.

### Step 4 , Determine tax residency

For each individual involved, determine their tax residency:

1. Apply each actual domestic residence test for the correct person/entity and tax year, retaining days, homes, family/economic ties, management and historic facts. A domestic day-count test is not interchangeable with a treaty employment exemption or PE test.
2. Only if an applicable treaty and dual domestic residence exist, apply its actual tie-breaker. For individuals, the familiar sequence investigates permanent home, closer personal/economic ties, habitual abode, nationality and competent-authority agreement when required. Apply the branches properly: no available permanent home moves to habitual abode, not a fabricated home test. Treaties can differ; do not substitute the model or assume nationality always resolves the case. [HMRC 2026 tie-breaker explanation](https://www.gov.uk/government/publications/dual-residents-hs302-self-assessment-helpsheet/dual-residents-2026-hs302).
3. Keep domestic residence, treaty residence, split-year treatment, tax scope and filing/claim duties separate. The individual cascade is not automatically the entity tie-breaker. No generic day count proves residence or non-residence.
4. Document supported conclusions, alternatives, required claims and unresolved facts. If ambiguous, show both potential domestic claims and the treaty/competent-authority work needed. Do not declare both final full-year residences or instruct duplicate filings merely to maximise obligations.
### Step 5 , Assess PE risk in each non-resident country

For each country where the user or their entity is NOT tax-resident but has activity:

1. Check the actual domestic taxable-presence rule and applicable treaty, protocol/MLI changes and dates; load the available PE method without treating it as enacted law.
2. Investigate actual place, permanence, disposal, business activity, construction/projects, exceptions/anti-fragmentation and agent authority or principal-role conditions under that instrument. No single generic three-part or fixed-days shortcut settles every PE type.
3. Preserve the service-PE inquiry, but use the treaty's actual inclusion, aggregation, activity and time threshold, not a universal UN-model number.
4. For home/remote work, distinguish the 2025 OECD Model Commentary from the wording and interpretation of the applicable treaty. Paragraphs 44.8 to 44.15 describe a generally-under-fifty-percent working-time indicator in a specified twelve-month window and fact/commercial-reason assessment at or above that level. It is not a worldwide automatic exemption or an automatic PE above the line, and does not decide agent or other PE grounds. [OECD Model update](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf).
5. Record evidenced no identified PE, conditional exposure or a supported PE determination separately from internal low/medium/high review priority. A risk flag alone does not prove a filing duty. Keep profit attribution as a specialist task, with the precise facts/instrument and deadlines to resolve.
### Step 6 , Determine VAT/GST treatment for cross-border supplies

For each supply that crosses a border:

1. Classify goods/services, actual customer status and establishments, goods dispatch/destination, ownership/chain, importer, consideration and dates.
2. For goods, test actual intra-Community supply/acquisition, export, import, stock transfer, chain/triangulation or distance-sale conditions and documentary proof. Cross-border movement alone does not prove exemption/zero rating, importer status or registration.
3. For services, apply the jurisdiction's actual place-of-supply rule and exceptions. The EU B2B/customer and B2C/supplier general rules have material property, transport, event/virtual-event, digital and other exceptions; they are not worldwide defaults. [Commission place-of-taxation guide](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en).
4. Separately determine liability, rate/exemption, supplier charge, customer reverse charge, import/deferred accounting and registrations/representative duties. A destination place of supply does not itself mean the supplier charges tax.
5. Preserve ordinary/OSS/IOSS and any SME or triangulation route as conditional enquiries. IOSS is not a digital-services route. If unclear, report the exact supply/fact/law gap and conditional treatments; do not assume destination treatment merely because it produces more obligations.
### Step 7 , Determine withholding tax exposure

For each cross-border payment:

1. Load `withholding-tax-matrix.md`
2. Determine actual source and residence separately by income type and facts; payer location may matter for some income but is not a general services sourcing rule. [IRS services sourcing](https://www.irs.gov/individuals/international-taxpayers/source-of-income-personal-service-income)
3. Classify the payment: services / royalties / interest / dividends
4. Look up domestic WHT rate in source country
5. Read the actual treaty/protocol/MLI article, in-force/effective dates and income classification; no treaty rate is inferred from a model or another country pair
6. Determine whether treaty benefits can be claimed (CoR available? Forms filed?)
7. Preserve Parent-Subsidiary and Interest & Royalties Directive eligibility enquiries for actually covered distributions/interest/royalties, including domestic implementation, qualifying entities/holdings, beneficial ownership and anti-abuse. An EU payer or ordinary service fee does not automatically qualify

**If unresolved:** show the actual supported domestic/treaty alternatives and required relief-at-source or refund/credit steps. Do not withhold an invented higher rate or promise the excess is recoverable. Preserve residence-certificate, beneficial-owner, form, deadline and payer/payee duty evidence; the residence certificate must come from the correct jurisdiction.

### Step 8 , Determine social security obligations

For each individual working across borders:

1. Determine personal, territorial and material scope of the actual EU/EEA/Swiss coordination instrument, UK Withdrawal Agreement/TCA or bilateral agreement, with current implementing and competent-institution rules. Tax residence is not automatically social-security residence.
2. Distinguish ordinary work-state coverage, qualifying temporary posting, simultaneous employed/self-employed work, civil-service or other special categories. In the EU guidance, eligible posting can retain sending-state coverage for up to twenty-four months subject to conditions and A1 evidence; it does not preserve every host-country payroll/employment exemption. [Commission posting FAQ](https://employment-social-affairs.ec.europa.eu/policies-and-activities/moving-working-europe/eu-social-security-coordination/frequently-asked-questions/faq-social-security-which-rules-apply-me_en).
3. Multi-state activity requires the actual residence/employer/activity analysis. The Commission describes at-least-twenty-five-percent working time/remuneration as a substantial-part indicator with the projected next twelve months and other circumstances considered; it is not a stand-alone rule for every mixed activity or telework exception.
4. Obtain the competent institution's determination/A1 and actual period, eligibility and any exceptional agreement. Where institutions disagree, the coordination system can apply one law provisionally; do not invent final double contributions as a default. If no applicable agreement exists, assess each domestic liability separately and identify genuine duplication. [Commission multi-state/provisional coverage](https://employment-social-affairs.ec.europa.eu/policies-and-activities/moving-working-europe/eu-social-security-coordination/frequently-asked-questions/faq-social-security-which-rules-apply-me_en).
### Step 9 , Identify transfer pricing requirements

If related-party cross-border transactions exist (intercompany services, management fees, IP licensing, loans):

1. Apply each country's actual related-party/transaction scope, whether pricing rules apply irrespective of a documentation exemption, and separate documentation thresholds
2. Use actual functional/comparability evidence to assess CUP, RPM, cost plus, TNMM, profit split or another locally accepted reliable method; do not impose a method by entity label
3. Check whether a Local File and/or Master File is required
4. Assess actual CbCR consolidated reference-period threshold/operator, filing entity, local/surrogate filing, exchange and notification rules, not a universal current-year amount
5. Flag any transaction where the pricing appears non-arm's-length

**Missing TP documentation:** flag the evidence/compliance enquiry, determine whether a legal documentation duty actually applies, and distinguish this from proof that pricing is wrong. Keep actual transaction reconciliation, method/benchmark gaps and country duties visible. [HMRC evidence proportionality](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030).

### Step 10 , Produce consolidated cross-border compliance map

Assemble all findings from Steps 4–9 into a single, structured output (format specified in Section 3).

---

## Section 3 , The compliance map output

The cross-border compliance map is the primary deliverable of this skill. It consists of five components:

### Component 1 , Country-by-country obligation matrix

| Country | Tax Residency | Income Tax Filing | VAT/GST Filing | Payroll Obligation | SS Contributions | E-invoicing | Financial Statements |
|---------|--------------|-------------------|----------------|-------------------|-----------------|-------------|---------------------|
| [country] | Resident / Non-resident / Treaty tie-breaker needed | Yes (form) / No / Conditional | Yes (form) / No / Registration needed | Yes / No | Yes (rate) / No / Covered by other country | Required / Not required | Required / Not required |

One row per country and affected entity/person where results differ. Every cell states supported yes/no/conditional/unresolved, actual source/date/fact, and task owner. No empty or falsely definitive answer; distinguish amount, filing, registration and review tasks.

### Component 2 , Double taxation relief summary

For each income type that is taxed in more than one country:

| Income Type | Taxed In | Taxed In | Relief Method | Treaty Article | Action Required |
|-------------|----------|----------|---------------|---------------|-----------------|
| Consulting fees | [actual residence/source and tax computation] | [other country, actual source rule and tax] | [actual exemption/credit/refund/no relief, separately tested] | [actual bilateral treaty article, not an automatic model article] | Obtain the residence certificate from the claimant's residence authority and the actual payer/claim forms; do not treat Indian Form 10F as a universal refund form |

### Component 3 , Unified filing calendar

| Obligation | Country | Form / Return | Period | Deadline | Frequency |
|-----------|---------|---------------|--------|----------|-----------|
| Income tax | DE illustrative workstream | ESt if applicable | [actual tax year] | [current official rule, extension and date] | [actual] |
| VAT return | DE illustrative workstream | UStVA if applicable | [assigned period] | [current rule and approved extension] | [actual assigned frequency] |
| WHT relief/refund or residence information | IN illustrative workstream | [actual purpose/form; Form 10F not certified as refund claim] | [actual payment/claim year] | [current official limitation/date] | [actual] |

All deadlines in one place, sorted chronologically. The thirty-day URGENT band is an internal planning policy; preserve every earlier application, payment or evidence task and actual legal deadline regardless of that band. Do not guess a deadline from a generic annual date.

### Component 4 , Risk flags

Categorize all identified risks:

| Priority | Risk | Country | Impact | Mitigation |
|----------|------|---------|--------|-----------|
| HIGH, illustrative priority | Four months on-site creates an assessment question, not an automatic PE | NL | Assess actual PE and tax filing separately from VAT establishment/registration | Obtain actual place/activity/contract/treaty evidence; removing a desk or limiting days is not automatic relief |
| HIGH, illustrative evidence gap | No documentation for assumed EUR 200,000 intercompany fee | DE-IE | Check actual pricing and separate documentation duty/exemption | Reconcile services, benefit, functions and actual country thresholds before concluding a breach |
| MEDIUM, illustrative review task | Treaty relief not yet established | IN | Tax paid may be creditable, refundable or irrecoverable; no assumed recoverable amount | Establish actual income article, claimant residence, forms, tax/claim cap and deadline |
| UNRESOLVED | Social coverage for an assumed two-week trip | FR | Short duration alone does not settle coverage or host duties | Seek actual competent-institution determination/A1 and separately assess host payroll/employment reporting |

### Component 5 , Reviewer brief for cross-border specialist

A narrative summary (similar to the VAT reviewer brief format) containing:

- One-paragraph situation summary
- Key determination made (residency, PE, applicable SS legislation)
- Highest-priority items requiring human verification
- Documents the reviewer should request from the client
- Evidence gaps, actual supported alternatives, legal application/claim deadlines and amounts potentially irrecoverable; no invented final obligation
- Refusal triggers checked and cleared

---

## Section 4 , Coordination rules (how domains interact across borders)

### Bookkeeping coordination

- **Primary chart of accounts**: use the actual reporting entity's approved chart and statutory/accounting/tax mappings; tax residence alone does not choose the chart
- **Multi-entity**: preserve each entity's separate records and actual applicable accounting framework; assess group control/consolidation requirements and exemptions separately
- **Intercompany eliminations**: identify actual consolidation scope/control, reconcile intragroup balances and eliminate only as required within that group/framework; not all related entities are subsidiaries. [IFRS 10 control-based scope](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/)
- **Currency**: functional, bookkeeping, tax and presentation currencies may differ. Distinguish transaction recognition/monetary versus non-monetary measurement from foreign-operation translation; historical-cost items are not all retranslated at closing. [AASB 121 paras. 20 to 26 and 38 to 42](https://standards.aasb.gov.au/aasb-121-oct-2023)
- **Cross-border transactions**: apply actual entity recognition/control, contractual substance and reporting framework, reconcile counterparties, dates/currency and explain legitimate differences; risk alone does not determine every accounting entry

### Payroll coordination

- **Which country's payroll system**: separately assess wage withholding, social coverage, labour/employer registration and any shadow payroll. A social-security determination does not choose every income-tax payroll duty
- **EU workers**: Regulation 883/2004 determines the single applicable legislation; employer registers with that country's authority
- **Posted workers (EU)**: a valid coverage determination/A1 supports the specified social-security legislation for its actual scope/period; host income-tax payroll, labour and notification duties remain separate
- **Non-EU bilateral**: Check totalization agreement for which country gets contributions
- **No agreement**: Employee may need payroll in both countries; flag for specialist
- **Remote workers**: The country where work is physically performed generally claims payroll obligations

### E-invoicing coordination

- **Domestic supplies**: Use the format of the country where the supply is taxable
- **Intra-EU B2B services**: determine actual place/liability/exemption and invoice legal references first; reverse charge does not itself settle structured-invoice or digital-reporting scope
- **Cross-border goods (intra-EU)**: verify both parties' actual invoicing/reporting/recipient and transaction conditions; buyer acquisition accounting does not prove supplier format compliance
- **Export to non-EU**: assess invoice/digital-reporting scope and export evidence separately; zero-rating eligibility does not remove a format or reporting duty
- **Country-specific mandates**: retain Italy, India and Saudi Arabia scope enquiries, but obtain actual entity/turnover/date/document/cross-border eligibility and exceptions rather than asserting all invoices are mandated

### Transfer pricing coordination

- **When required**: apply the actual country related-party/control/transaction rules; no universal ownership percentage or cross-border-only scope
- **Documentation**: determine actual prepare/retain/file/on-request and notification duties, thresholds and exemptions for each workstream; entity presence does not itself require a Local File
- **Methods**: use the most reliable applicable method under each country's law and adopted guidance version; an international edition is not automatically domestic law
- **Advance Pricing Agreements (APAs)**: assess actual availability, scope, terms, compliance assumptions and time/cost; an APA is not an unconditional elimination of all adjustment risk
- **Safe harbours**: check actual domestic acceptance, eligible service/cost base and exclusions; no universal simplified-services markup is supplied as a rule

### Financial statements coordination

- **Standalone vs consolidated**: establish each entity's actual reporting/filing/framework requirement and group control/exemptions; size alone does not define consolidation scope
- **GAAP conflicts**: retain German HGB/UK GAAP and other local-to-group mapping enquiries, applying the actual required group framework and consistent policies; consolidation is not a free choice between an arbitrary parent framework and IFRS
- **Audit requirements**: Check each country's audit threshold independently; an entity may require audit in one country but not another
- **Related-party disclosures**: apply actual framework definitions, materiality, required relationships/balances/terms and exemptions; do not assert every individual transaction must be separately disclosed
- **Consolidation exemptions**: Small groups may be exempt from consolidation in their parent state; check the size thresholds (total assets, revenue, employees) per country
- **Currency translation**: for the cited non-hyperinflationary foreign-operation presentation method, assets/liabilities use closing rate, income/expenses actual transaction-date rates and resulting differences OCI; an average is only a reliable approximation, not mandatory when FX fluctuates. Distinguish this from transaction remeasurement and hyperinflation. [AASB 121 paras. 38 to 42](https://standards.aasb.gov.au/aasb-121-oct-2023)

### VAT/GST coordination across borders

| Supply type | VAT treatment | Registration trigger |
|-------------|--------------|---------------------|
| B2B services (general-rule enquiry) | Actual customer status, establishment, supply type, exceptions and tax liability | Reverse charge may affect registration, but it is not a universal supplier exemption |
| B2C digital services | Actual customer location, supplier establishment and applicable EU/non-EU scheme | Assess ordinary/OSS and any qualifying SME route; IOSS is for qualifying imported goods, not digital services |
| Intra-EU goods | Confirm actual exempt/zero-rated supply and acquisition conditions/evidence | Establish actual supplier/buyer registrations and exceptions |
| Export of goods | Confirm actual destination, customs/export proof and exemption conditions | No automatic zero-rating or absence of registration/format duties |
| Import of goods | Identify importer, customs procedure, actual place/time and VAT liability | Determine registration, fiscal representation and any import/deferred/special route; entry alone is not automatic registration |
| Triangulation | Check actual chain, transport, identified parties, country conditions and invoicing | A conditional simplification, not a blanket exemption in a transit country |

These are assessment workstreams. [Commission place-of-taxation guidance](https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en) supports separating supply/transaction conditions; it does not certify a particular country's registration conclusion.
### Income tax coordination

- **Worldwide vs territorial**: Residence countries generally tax worldwide income; source countries tax only locally-sourced income
- **Credit vs exemption**: The treaty between the pair determines whether the residence country gives a credit for foreign tax or exempts the foreign income (see OECD Art 23A/23B)
- **Foreign tax credit limitations**: Credits are usually limited to the residence-country tax attributable to the foreign income , excess credits may carry forward (country-specific)
- **CFC rules**: If a controlled foreign subsidiary is in a low-tax jurisdiction, the parent's country may tax the subsidiary's undistributed profits (ATAD in EU; Subpart F/GILTI in US; § 7-14 AStG in Germany)
- **Legal interaction**: establish domestic charge/relief, actual treaty scope/eligibility/effective text and relevant EU law/implementation/anti-abuse separately. There is no blanket domestic-law-to-treaty-to-directive ladder that guarantees the most generous result

### Formation and substance coordination

- **Substance requirements**: investigate actual incorporation, residence, treaty, anti-abuse and economic-substance rules and genuine people/office/decision facts. Depending on the applicable conditions, issues can include:
  - Being treated as tax-resident elsewhere (where management and control actually exercised)
  - CFC rules in the parent's jurisdiction attributing income
  - Denial of treaty benefits under LOB/PPT clauses
- **Director residency**: check actual company-law/director and tax management/control requirements separately; a local nominee does not establish economic substance
- **Board meetings**: document where real decisions are actually made and by whom; minutes or an address do not substitute for genuine control
- **Bank accounts**: establish actual legal/commercial requirements and controls; a universal local-bank requirement or residence proof is not assumed
- **Economic nexus**: investigate actual people, functions, assets, risk and commercial reasons under the applicable rule; no universal requirement that every incorporated entity have local customers/revenue

---

## Section 5 , Conservative defaults for cross-border cases

When facts or law remain uncertain, keep supported alternatives and the exact evidence/claim deadlines visible. Maximising tax, duplicate contributions or deemed disposals is not a lawful universal default and can cause underpayments elsewhere or irrecoverable withholding.

| Ambiguity | Supported response | Evidence/action preserved |
|---|---|---|
| Dual domestic residence unclear | Record each potential claim and actual treaty test, not two final residences | Homes/ties/days, applicable treaty, claim forms and competent-authority route |
| PE presence borderline | Conditional PE investigation with actual rule/facts | Place/agent/activity/time evidence and separate filing/attribution enquiry |
| WHT domestic/treaty rate uncertain | Hold actual rate/eligibility, show only supported alternatives | Source/character, treaty benefits, certificate/forms and deadlines |
| VAT place uncertain | Hold affected tax/liability conclusion | Supply/customer/establishment/movement facts and exception rule |
| Social coordination unclear | Obtain competent determination and provisional rule where applicable | Actual covered law/A1 period, separate host payroll/employment duties |
| TP documentation absent | Assess actual documentation duty and pricing evidence separately | Scope/threshold/exemption, functions, methods and actual data |
| Treaty existence/effective date uncertain | Search actual official treaty/protocol/MLI text | Do not assert no treaty or assume treaties only remove procedural duties |
| Beneficial ownership challenged | Preserve claim eligibility as unresolved, not automatically denied | Actual rights, control, flow and anti-abuse conditions |
| Split-year potentially available | Apply domestic case conditions and actual dates | No assumed full-year dual residence or automatic departure-day split |
| Potential exit tax | Investigate actual person/asset/trigger/exemption/deferral | No automatic full deemed disposal from relocation alone |
| Foreign income classification uncertain | Preserve supported competing classifications and source/relief effects | Do not book tax in both states merely to appear conservative |
| Borderline multi-state social activity | Seek competent-institution assessment | Actual time/remuneration/residence/employer and any applicable exception |
| Substance/CFC concern | Apply actual residence, control, income, low-tax and exemption conditions separately | Substance facts do not by themselves prove a CFC inclusion |
| Intercompany price questioned | Check reliable comparables, actual functions and legal scope | Unsupported pricing is a review issue, not a proven non-arm's-length adjustment |
| Treaty-benefit eligibility unresolved | Hold final entitlement and protect applicable claim deadlines | Actual domestic/treaty conditions, documents and possible irrecoverable excess |

### Original bilateral example, corrected assessment

Assumed German-resident freelancer receives USD 50,000 from a US client and spends two weeks at that client's office. Retain this fact pattern, but do not certify a US zero rate, thirty-percent withholding, absence of PE or EU reverse charge from it. Source may depend on where the compensated work was actually performed; any relevant US service allocation needs the actual service days and income category, not payer address. The bilateral treaty/eligibility, German scope, VAT customer/supply facts, social coverage and filings remain separate checks. A short visit alone does not clear every PE type, and double-tax relief is not guaranteed to recover every excessive payment. [IRS service-source rule](https://www.irs.gov/individuals/international-taxpayers/source-of-income-personal-service-income), [HMRC relief limits as a country illustration](https://www.gov.uk/tax-foreign-income/taxed-twice).
## Section 6 , Self-checks (run before delivering the compliance map)

### Structural checks

**Check 1 , All jurisdictions covered.** Every country identified in Step 1 appears in the obligation matrix. No country silently dropped.

**Check 2 , No conflicting determinations.** If country A says "resident" and country B says "resident," the treaty tie-breaker is applied or both are flagged. Never deliver a map that says "resident in A" AND "non-resident in A" without explanation.

**Check 3 , Double taxation addressed.** Every income item taxed in two countries has an entry in the double-taxation relief summary. No double-taxed income is left without a relief mechanism identified.

**Check 4 , Filing calendar complete.** Every "Yes" in the obligation matrix has a corresponding entry in the filing calendar with a specific deadline.

**Check 5 , Risk flags populated.** Record evidenced risks and unresolved required checks. An assessed cross-border case can have no identified material risk; do not invent a flag to satisfy a count.

### Domain interaction checks

**Check 6 , SS and payroll consistent.** Reconcile actual social coverage, income-tax withholding, employer registrations and any shadow payroll separately. Different jurisdictions are not inherently an inconsistency.

**Check 7 , VAT and e-invoicing consistent.** Verify actual issuer/recipient/establishment/document/mandate scope; the place of taxation alone does not choose every invoice format/reporting duty.

**Check 8 , Transfer pricing and bookkeeping consistent.** Reconcile actual books/agreements/currencies and supported TP result or proposed adjustment; no silent ledger posting or forced identical local tax/accounting measurement. Explain differences and consolidate only within actual scope.

**Check 9 , PE and income tax consistent.** Distinguish potential PE from a supported determination and then assess actual filing/registration deadlines, exemptions and profit attribution. A risk flag is not an automatic yes.

**Check 10 , WHT and treaty relief consistent.** Reconcile lawful withholding with actual treaty cap/eligibility and relief-at-source/refund/credit limits, dates and country computations. Show unsupported or irrecoverable excess; do not promise recovery merely because tax was withheld.

### Conservative-default checks

**Check 11 , Every default disclosed.** Each provisional scenario, its actual supporting rule, missing evidence, alternative and impact is disclosed; no invented final obligations are hidden as conservative defaults.

**Check 12 , No silent assumptions.** No cell in the obligation matrix says "No" without an explicit basis. If the basis is "no treaty, no filing obligation under domestic law," state it.

**Check 13 , Reviewer actions clear.** The reviewer brief contains specific actions (not vague "review this") , "confirm actual A1 scope/period," "establish the applicable Dutch treaty PE test and activity history," "obtain the claimant's residence certificate and correct Indian claim evidence."

### Refusal and escalation checks

**Check 14 , Complexity ceiling.** The internal complexity triggers remain more than five countries, three entities or two scenario types: flag specialist coordination, preserve supported work and unresolved task ownership. These are workflow limits, not statutory thresholds.

**Check 15 , No prohibited advice given.** Verify that no output contains treaty shopping suggestions, nominee arrangements, or structuring advice that lacks substance.

**Check 16 , Temporal consistency.** All tax rules, rates, and thresholds cited are current for the relevant tax year. If the user's situation spans multiple tax years (e.g., relocation mid-year), each year uses that year's rules.

**Check 17 , Document completeness.** The reviewer brief lists every document the user needs to obtain (CoR, A1 certificate, Form 10F, W-8BEN, etc.) with the correct issuing/receiving authority, purpose and supported actual deadline. A processing-time estimate is not a legal claim deadline.

**Check 18 , Cross-reference integrity.** Every reference to another skill (e.g., "see withholding-tax-matrix.md") corresponds to a real file that exists in the skill set. Do not reference non-existent skills.

---

## Worked cases

### Credit relief does not guarantee recovery of all foreign tax

Assume a UK-resident individual's eligible non-trading foreign-income item has supported foreign tax 3,000 and UK Income Tax attributable to that same item 2,000. Assume all eligibility/source/treaty and ordering conditions are established. Under the cited UK individual credit limit, credit is 2,000, remaining UK tax on the item is nil and foreign excess of 1,000 is not refunded or deducted merely through that credit claim. It is not an automatic carryforward or a rule for every country's corporate/trading credit system. [HMRC limit of credit](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm165040).

```oa-check
name: Foreign tax credit is limited and excess is not automatically recovered
inputs:
  eligible_foreign_tax: 3000
  uk_tax_attributable_to_same_item: 2000
steps:
  - allowed_credit: min(eligible_foreign_tax, uk_tax_attributable_to_same_item)
  - remaining_uk_tax: uk_tax_attributable_to_same_item - allowed_credit
  - foreign_excess_not_recovered_by_this_credit: eligible_foreign_tax - allowed_credit
expected:
  allowed_credit: 2000
  remaining_uk_tax: 0
  foreign_excess_not_recovered_by_this_credit: 1000
```

### Home-office time indicator does not itself decide PE

Assume actual enterprise working time in the relevant twelve-month window totals 240 days, of which 96 are at the foreign home. The fraction is 40%, with 24 days to the halfway point. If home-working rises to 120 days, it is exactly 50%, requiring the model's facts/commercial-reason analysis rather than an automatic yes/no PE. Actual treaty interpretation, country reservations and other PE grounds still need their own evidence. This is a Model Commentary illustration, not a country safe harbour or a real employee conclusion. [OECD 2025 Model update, paragraphs 44.8 to 44.15](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf).

```oa-check
name: Homeworking ratio distinguishes below and at the model indicator
inputs:
  total_enterprise_workdays: 240
  current_home_workdays: 96
  indicator_fraction: 0.50
steps:
  - current_home_percentage: current_home_workdays / total_enterprise_workdays * 100
  - indicator_workdays: total_enterprise_workdays * indicator_fraction
  - days_to_indicator: indicator_workdays - current_home_workdays
  - percentage_at_indicator: indicator_workdays / total_enterprise_workdays * 100
expected:
  current_home_percentage: 40
  indicator_workdays: 120
  days_to_indicator: 24
  percentage_at_indicator: 50
```

## When to refuse or refer

### Section 7: Refusals

This skill MUST refuse to proceed and escalate to a human specialist when any of the following are detected:

### Hard refusals (immediate stop)

| Code | Trigger | Refusal message |
|------|---------|-----------------|
| R-CB-1 | Treaty shopping / aggressive structuring | "This arrangement appears designed to access treaty benefits without genuine economic substance. I cannot advise on treaty shopping structures. Please consult a qualified international tax advisor." |
| R-CB-2 | Nominee arrangements without substance | "Nominee structures without genuine economic activity in the nominee jurisdiction are outside my scope. A qualified advisor must review substance requirements." |
| R-CB-3 | Request to evade tax, conceal income/accounts or deliberately avoid required filing | Refuse concealment/evasion and refer the affected legal issue. Lawful reconstruction, correction and disclosure of past errors remain supported evidence/filing enquiries |
| R-CB-4 | Potential applicable sanctions/prohibited transaction or a user-set excluded scope | Hold the affected transaction for current party/activity/jurisdiction and licence/exemption screening by the appropriate legal specialist. No static country list in this tax method establishes a blanket legal prohibition |
| R-CB-5 | Concealment or evasion of required CRS/FATCA reporting | Refuse assistance hiding reportable accounts/persons or evading a required report; actual lawful scope/exemption and correction/disclosure enquiries remain subject to the applicable rules |
| R-CB-6 | Artificial profit shifting without substance | "Profit shifting to low-tax jurisdictions without corresponding economic activity and substance fails BEPS standards. I cannot advise on structures lacking substance." |
| R-CB-7 | Design intended to evade or conceal mandatory disclosure | Refuse concealment/evasion. A lawful arrangement being reportable is not itself illegal; retain assistance identifying existing DAC6 obligations and obtaining actual specialist reporting advice |

### Soft escalations (proceed with flag)

| Code | Trigger | Action |
|------|---------|--------|
| R-CB-S1 | More than 5 jurisdictions | Proceed but flag: "This case involves [N] jurisdictions and exceeds typical complexity. Output is indicative only. Specialist review essential." |
| R-CB-S2 | Profit attribution to PE | Proceed but do NOT compute attribution. Flag: "PE profit attribution requires specialist analysis. Filing obligation flagged but quantum not computed." |
| R-CB-S3 | Exit tax computation | Flag the exit tax trigger but do NOT compute the tax liability. "Potential exit-tax trigger in [country] requires the actual person/asset/law and departure facts; specialist calculation if established." |
| R-CB-S4 | Mutual Agreement Procedure needed | "Unresolved treaty/competent-authority issue: determine the actual MAP eligibility, claim deadline and process. No generic completion time or guaranteed resolution." |

---

## Section 8 , How this skill interacts with other skills

### Loading hierarchy

```
global-router.md
  → (detects cross-border signal)
  → cross-border-workflow-base.md (THIS FILE)
      → country skills (loaded per Step 3)
      → cross-border specialist skills (loaded per scenario type):
          - tax-residency-planning.md (Type B, E)
          - permanent-establishment-risk.md (Type A, C, D, E)
          - withholding-tax-matrix.md (Type A, D)
          - eu-social-security-coordination.md (Type C, E , EU only)
          - eu-directives-cross-border.md (Type D , EU only)
          - oecd-model-treaty-defaults.md (all types , treaty interpretation)
```

### Scenario routing table

| Scenario Type | Skills loaded | Primary output |
|---------------|--------------|----------------|
| Type A (foreign clients) | Country tax skill(s) + WHT matrix + PE risk + OECD defaults | Obligation matrix + WHT relief map |
| Type B (relocation) | Residency planning + country tax skills (both countries) + OECD Art 4 | Residency determination + split-year filing plan |
| Type C (foreign employees) | EU SS coordination (if EU) + country payroll skills | SS determination + payroll registration guidance |
| Type D (multi-entity) | TP skills + EU directives + PE risk + country tax skills | TP documentation plan + PE risk map + consolidated compliance |
| Type E (digital nomad) | Residency planning + PE risk + SS coordination + OECD defaults | Residency establishment plan + PE avoidance guidance |
| Type F (foreign formation) | Country formation skill + EU directives (if EU) + OECD defaults | Formation checklist + substance requirements + CFC analysis |

### Conflict resolution

- **If two country skills conflict on the same fact**: the country whose domestic law governs that fact wins (e.g., source country determines domestic WHT rate)
- **If a country skill and a cross-border skill conflict**: the actual applicable law/treaty/coordination instrument and facts decide; neither a generic cross-border file nor a country file wins merely by its label
- **If this orchestrator and a country skill specify different workflow steps**: follow this orchestrator's Steps 1–10 for the overall case; defer to the country skill's workflow for country-specific deliverables within each step

### Output ownership

- This skill owns: the compliance map (Section 3), the unified filing calendar, the risk flags, the cross-border reviewer brief
- Country skills own: individual country returns, country-specific workbooks, country-specific reviewer briefs
- Both produce outputs , this skill's output is the coordination layer that ties them together

---

## Section 9 , Reference material

### Validation status

This file is v1.1 of `cross-border-workflow-base`, updated as a shared 2026 evidence/coordination method. Illustrative cases below test method controls, not a live multi-country filing or accountant-reviewed legal conclusion.

### Known gaps

1. The 10-step workflow has not been stress-tested against cases with more than 3 countries simultaneously.
2. Transfer pricing documentation thresholds vary significantly by country and are not fully captured here , they come from individual country skills.
3. Multilateral claims require all actual bilateral instruments and domestic computations, source/credit ordering and unresolved facts; the former maximum-obligation defaults are not retained as usable tax guidance.
4. Social security coordination for non-EU cases relies on bilateral totalization agreements which this skill does not contain , it only flags the need and defers to country-specific bilateral agreement content.
5. The 2025 OECD update on remote work PE is in the Commentary, not the Model Articles themselves; many existing treaties have not been updated.

### Test suite

#### Test 1 , Type A: German freelancer with US and UK clients

**Input:** German tax resident freelancer invoices US clients ($80K) and UK clients (£30K). Works 100% from home in Berlin. No travel abroad.

**Expected assessment controls, not certified country outcomes:**
- Separate confirmed German residence/filing scope from the actual US/UK service-source, performance, presence and treaty enquiries. No foreign travel supports one factual input, not an automatic legal clearance.
- Determine actual customer status and service/establishment exception rules before VAT treatment; do not prescribe universal foreign-client reverse charge or an unverified German return box.
- Assess actual single-state social coverage and any applicable special facts. Record no identified risk only after evidence checks, not because a test hardcodes zero foreign rates.

#### Test 2 , Type B: UK resident relocating to Portugal mid-year

**Input:** UK resident moves to Portugal on 1 July. Continues freelancing for UK clients. No return to UK planned.

**Expected assessment controls, not certified country outcomes:**
- Test actual UK SRT/split-year case conditions and Portuguese residence/scope for each year, using full history/homes/ties and dates. A first-July move does not itself prove SRT Case 4 or Portuguese treaty residence.
- Investigate continuing UK place/agent/return activity and actual service sourcing. Assess UK/Portuguese VAT registration/deregistration from establishment/supply rules, not merely a domestic turnover limit.
- Determine the applicable UK/EU social instrument, competent determination and actual start/end dates; contributions do not automatically switch on payroll registration day.
- Preserve UK/Portuguese filing, NIF/social registration and exit/temporary-non-residence enquiries, without certifying an automatic UK exemption from every departure-related charge.

#### Test 3 , Type C: Dutch company with remote developer in Poland

**Input:** Dutch BV hires a full-time developer in Poland. Developer works from home in Warsaw. No Dutch travel.

**Expected assessment controls, not certified country outcomes:**
- Establish the developer's actual domestic/treaty residence and social coverage separately from the Dutch BV's residence, actual Warsaw home-office/agent PE facts and treaty rules.
- A full-time foreign home office is not automatically cleared by the 2025 Model Commentary; assess actual working-time window, commercial reason and applicable instrument. No-travel alone does not settle corporate PE.
- Assess Polish wage withholding/employer/social registration, contracts and any host reporting separately; a payroll provider/EoR label does not remove the actual employer's duties.
- Preserve employment-versus-service VAT classification, salary tax/reporting, entity employment-cost accounting and actual registration tasks. Record supported conditional results rather than blanket no-WHT/no-PE outcomes.

#### Test 4 , Type D: Irish subsidiary paying management fees to German parent

**Input:** German GmbH owns 100% of Irish Ltd. Irish Ltd pays €200K annual management fee to German GmbH.

**Expected assessment controls, not certified country outcomes:**
- Establish actual service benefit, functions, cost/pricing and both countries' related-party and documentation scope/exemptions. An assumed EUR 200,000 fee and full ownership do not prove both Local File thresholds are exceeded.
- Distinguish ordinary service fees from interest/royalty/directive categories, actual withholding/source rules and applicable treaty relief.
- Assess actual fixed-place/agent activity and service supply/VAT reverse-charge conditions; preserve German/Irish recognition, deductibility and filing enquiries without guaranteeing the fee deduction.
- Keep missing documentation and actual pricing evidence as separate risk/required-action findings, not automatic proof of non-arm's-length pricing.

### Change log

- **v1.1 (14 November 2026):** Replaces unsupported maximum-obligation defaults, separates source/residence/payroll/social/VAT/PE questions, corrects coordination and retains ten steps, six scenario types, five map components, eighteen checks, refusal IDs and four original scenarios.

- **v1.0 (May 2026):** Initial draft. Ten-step workflow, six scenario types, five-component compliance map output, eighteen self-checks, seven hard refusals plus four soft escalations. Four test cases.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Cross-border tax matters are inherently complex and fact-specific. All outputs must be reviewed and signed off by a qualified international tax professional before filing or acting upon.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC HS302 2026. Read for individual treaty tie-breaker purpose and full permanent-home/centre/habitual-abode/nationality sequence; not every US saving-clause or FIG claim detail | https://www.gov.uk/government/publications/dual-residents-hs302-self-assessment-helpsheet/dual-residents-2026-hs302 | 2026-11-14 |
| IRS personal service source. Read for actual place-of-performance, mixed-location/time allocation and benefit-specific exceptions; no automatic US withholding rate supplied | https://www.irs.gov/individuals/international-taxpayers/source-of-income-personal-service-income | 2026-11-14 |
| HMRC taxed twice. Read for relief-at-source/after-tax claims, correct residence evidence, treaty/unilateral relief and non-recoverable limits; not every specialist gain rule | https://www.gov.uk/tax-foreign-income/taxed-twice | 2026-11-14 |
| HMRC INTM165040. Read for opening individual credit limit and one/multiple income-source calculation; example confined to supported non-trading individual facts | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm165040 | 2026-11-14 |
| Commission place of taxation. Read for goods movement/import procedure discussion and services B2B/B2C general rules, property/transport/event/digital exceptions; registration/invoicing not inferred from place alone | https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en | 2026-11-14 |
| Commission applicable-social-legislation FAQ. Read for posting/A1 and full substantial-part/residence, future-period and provisional-law/multi-state coordination sections | https://employment-social-affairs.ec.europa.eu/policies-and-activities/moving-working-europe/eu-social-security-coordination/frequently-asked-questions/faq-social-security-which-rules-apply-me_en | 2026-11-14 |
| IFRS 10 About. Read for control-based consolidation and investment-entity exception, not the full paid standard | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/ | 2026-11-14 |
| OECD 2025 Model Tax Convention update. Read for Article 5 Commentary paragraphs 44.8 to 44.15, actual working-time window/conduct and commercial-reason conditions; not every example, country reservation or an enacted bilateral treaty | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/the-2025-update-to-the-oecd-model-tax-convention_c7031e1b/5798080f-en.pdf | 2026-11-14 |
| AASB 121 October 2023 compilation, applicable from January 2025 before January 2027. Read for paragraphs 20 to 34 and 38 to 42, transaction versus presentation translation, monetary/non-monetary treatment, reliable-average condition and OCI/hyperinflation distinctions | https://standards.aasb.gov.au/aasb-121-oct-2023 | 2026-11-14 |
| HMRC INTM483030. Read for opening proportionate documentation and accounting/adjustment/controlled-transaction/arm-length evidence classes; no foreign Local File threshold inferred | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm483030 | 2026-11-14 |

Not yet confirmed: every actual bilateral treaty/protocol/MLI effective text, residence/entity tie-breaker, split-year/exit/CFC/beneficial-owner/anti-abuse determination, domestic source/withholding and relief forms/rates/deadlines; Germany/India sample relief and ESt/UStVA calendar, correct Form 10F purpose and any actual refund limitation; current EU directive implementation/eligibility, VAT exemption/registration/OSS/IOSS/triangulation and invoice/digital-reporting scope; UK TCA/Withdrawal Agreement, EU telework/mixed-activity exceptions and non-EU bilateral social agreements; actual PE country interpretation/reservations and service/project thresholds; current TP/CbCR scopes and documentation thresholds; each actual reporting framework/control/audit/disclosure/FX rule and local formation/substance requirement. The four original country scenarios remain assessment cases, not verified legal outcomes. Former blanket dual-residence/contribution, destination-VAT, global ownership/markup, sample WHT percentages, fixed filing/refund dates and generic MAP-time shortcuts are not retained as usable guidance. Held companions remain unavailable until separately completed and published; this source rewrite alone does not make them live.
