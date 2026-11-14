---
name: ck-company-tax-vat
description: >
  Prepare selected Cook Islands ordinary company residence, income-source,
  basic income-tax and domestic VAT components for a credentialed reviewer
  in 2026. Use for director-control and effective-management tests, concurrent
  resident directors, reconciled taxable income, VAT accounting basis,
  invoice and payments timing, input evidence, registration boundaries and
  quarterly-election questions. Includes primary sources, fictional worked
  positions, explicit source gates and reviewer checks. Holds the conflicting
  company payment calendar, unverified threshold Orders, international entities,
  incomplete returns and other special regimes. This source-cited draft does
  not establish a complete return, operational readiness or comprehensive
  Cook Islands coverage.
jurisdiction: CK
category: international
tax_year: 2026
tax_year_notes: "Selected ordinary company and domestic VAT components checked 24 October 2026; actual engagement calculations require the current-law and input gates below"
tier: 2
last_updated: 2026-10-24
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
  - vat-workflow-base
verified_by: pending
---

# Cook Islands: ordinary company tax and VAT components

## Scope and source gates

This reference provides bounded working-paper components for an ordinary
domestic company and ordinary domestic VAT transactions. It establishes
neither a complete company tax computation nor a VAT return. Load workflow-base,
corporate-income-tax-workflow-base for company income-tax work and
vat-workflow-base for VAT work. Preserve their source conditions,
profile confirmation, refusals, outputs and checks. Missing country slots,
regional/legal-framework companions or runtime capabilities prevent a complete
VAT workflow; this component does not waive those requirements.

Use the selected rules only after verifying their operative primary law for
the requested period. The official site states a consolidation as at
1 December 2025 and directs users to later Laws as Made; its selected VAT
amendment table already includes the 2026 amendment. Neither metadata nor a
negative search certifies completeness through the engagement date. Check
material amendments, commencement, regulations, Orders and actual notices.
An unresolved source condition holds the affected engagement calculation.
The fictional examples below remain reference illustrations under their
express assumptions. [Official consolidation date][LAW-DATE];
[official legislation information][LAW-HELP];
[income-tax amendment table][IT-PREFACE]; [VAT amendment table][VAT-PREFACE]

Two specific gates remain open:

- **Company payment calendar:** Income Tax Act section 179, section 15(2)
  and Schedule 3 clause 1 give 1 May and 1 November for an ordinary December
  balance in the stated statutory sequence. MFEM's published company calendar
  gives 1 June and 1 December, with a 1 May return. No operative bridge has
  been established here. Preserve both positions and obtain the instrument,
  applicable notice or exercised Collector authority before selecting payment
  dates. A filing extension is not assumed to shift payments: section 180
  expressly contemplates an interim return when the extended return is still
  outstanding at the first instalment. Section 190's additional-tax timing
  is not a due-date amendment. [15][IT-15]; [179][IT-179]; [180][IT-180];
  [190][IT-190]; [Schedule 3][IT-CALENDAR]; [MFEM calendar][MFEM-CALENDAR]
- **Compulsory VAT threshold:** Section 12(1)(a) prints NZD 40,000 but expressly
  permits another amount by Order in Executive Council. Public title/index
  searches have not established an exhaustive current-through Order series.
  Obtain the applicable amount and its effective dates before an actual
  compulsory-registration conclusion. The conditional NZD 40,000 examples
  are not evidence that no Order exists. The separate voluntary amount in
  section 12(4)(c) is NZD 20,000 and has no equivalent express substitution
  wording. It still requires the ordinary current-law and Collector gates.
  [Registration][VAT-12]; [official publication limits][LAW-HELP]

Overseas/international companies, trusts, groups, insurers, banks, charities,
regulated activities, mining, property disposals, transfer pricing, foreign
tax credits, withholding, payroll, social contributions and other special
regimes require separate sources. A domestic incorporation certificate does
not settle residence, foreign income, VAT registration or exemption. Use
ck-company-registry-reporting for its selected company-law component; its
formation, reporting and ownership holds remain.

## Intake and primary sources

Retain redacted evidence and stable references, with identifiers, credentials,
bank details and identity documents kept outside this workflow. Confirm:

- Requested income year and VAT return period, balance date, currency,
  company type/history, activities and applicable special regimes.
- Actual director control and effective management, with dates and evidence;
  every director's independently established residence and concurrent tenure.
  Record facts throughout the income year and when income is derived.
- Each income stream, business/contract performance locations and any mixed
  source. Obtain the reviewed taxable-income reconciliation, exemptions,
  deductions, losses and adjustments before applying the basic rate.
- VAT registration/liability and effective date, taxable activity, complete
  rolling-year and forward-year supply values, exempt supplies, relevant
  imported services and any Collector-satisfied exclusion or threshold Order.
- Actual accounting-basis election and notification, evidence of no election
  if that statutory default is invoked, any approved change and transition.
- Supply type/place, supplier and recipient status, invoice/payment/delivery
  dates, tax actually charged, prescribed documents, taxable purpose, related
  parties and special valuation conditions. A bank line or brand is insufficient.
- Monthly/quarterly status, notice and absence of overdue returns, Collector's
  first quarterly due date, threshold changes, actual calendars and extensions.
- Complete adjustments, prior claims, credits/debits, bad debts, imports,
  use changes and other streams. Establish a nil amount independently rather
  than treating an absent record as nil. Obtain reviewer attention thresholds.

Read the identified complete provisions and their applicable definitions.
The source library is selected, not a claim that every country law was audited.

| Primary source | Component |
|---|---|
| Income Tax Act 1997, sections 2, 39-40 and 42 | Company/person, assessable and taxable income definitions, charge, basic rates and exemption gate. [2][IT-2]; [39][IT-39]; [40][IT-40]; [42][IT-42]. |
| Income Tax Act, sections 80, 82-84 and Schedule 1 clause 2 | Residence, income-source scope, mixed-source discretion and company rate. [80][IT-80]; [82][IT-82]; [83][IT-83]; [84][IT-84]; [company rates][IT-RATES]. |
| Original Income Tax Amendment Act 2013, sections 2, 16-18 and 36/Schedule | Selected residence/source changes and replacement rate schedule from 1 January 2014; historical exceptions do not become 2026 rules. [2013 original][IT-2013]. |
| Original Income Tax (Company Residence) Amendment Act 2021, sections 2/4 | The 3 company tests apply to all companies from 1 January 2023; the 2022 election is historical. [2021 original][IT-2021]. |
| Income Tax Act, sections 8-9, 15, 179-180, 188 and 190 with Schedule 3 | Separate return, payment and penalty conditions; company payment sequence remains held. [8][IT-8]; [9][IT-9]; [15][IT-15]; [179][IT-179]; [180][IT-180]; [188][IT-188]; [190][IT-190]; [Schedule 3][IT-CALENDAR]. |
| VAT Act 1997, sections 2-8, 10-13 and Schedule 1 | Definitions, taxable activity, timing/value/place, imported services, charge, rates, registration/cancellation and exemptions. [2][VAT-2]; [3][VAT-3]; [4][VAT-4]; [4A][VAT-4A]; [5][VAT-5]; [6][VAT-6]; [7][VAT-7]; [8][VAT-8]; [10][VAT-10]; [11][VAT-11]; [12][VAT-12]; [13][VAT-13]; [exempt supplies 1][VAT-EXEMPT], [2][VAT-EXEMPT2], [3][VAT-EXEMPT3], [4][VAT-EXEMPT4] and [5][VAT-EXEMPT5]. |
| VAT Act, sections 15-19 and 42 | Return period, accounting basis, net tax, payment, invoice/adjustment evidence and records. [15][VAT-15]; [15A][VAT-15A]; [15B][VAT-15B]; [16][VAT-16]; [17][VAT-17]; [18][VAT-18]; [19][VAT-19]; [42][VAT-42]. |
| Original VAT Amendment Act 2014, sections 2/4 and 12-16 | Selected 15% rate, registration amounts, imported-service inclusion and tax-fraction changes, applying from 1 April 2014. Its tourism transition is historical. [2014 original][VAT-2014]. |
| Original VAT Amendment Act 2023, sections 2/4/5 and Schedule | 1 July 2023 quarterly election and consequential return-period changes, including sections 16/17. [2023 original][VAT-2023]. |
| Original VAT Amendment Act 2026, sections 2/4/5 | Selected import exemptions, commencing the day after 26 May 2026 assent; no ordinary-rate or registration conclusion follows from those import changes. [2026 original][VAT-2026]. |

## Period-specific figures

| Item | Selected rule | Source |
|---|---|---|
| Ordinary company basic rate | Resident under section 82: 20 cents per taxable-income dollar; not so resident: 28 cents. Overseas insurance companies excluded. | [Schedule 1 clause 2][IT-RATES] |
| Natural-person director residence input | Home in Cook Islands **and** personal presence **more than 183 days** in a 12-month period, under section 82(1). This is not the company's residence test. | [82][IT-82] |
| Domestic-company director branch | At least 3 resident directors concurrently at any moment during the income year; control and effective-management branches are independent alternatives. | [82(2)][IT-82] |
| Ordinary VAT standard rate | 15% of established VAT-exclusive supply value. For an ordinary wholly standard-rated price inclusive of that VAT, the tax fraction is 15/115 = 3/23. | [6][VAT-6]; [11][VAT-11] |
| Printed compulsory registration amount | NZD 40,000, subject to the unresolved applicable-Order gate; strictly exceeded, not merely equalled. | [12(1)][VAT-12] |
| Voluntary-registration supply amount | Likely to exceed NZD 20,000 over the specified year; application and Collector eligibility/effective-date conditions apply. | [12(4)-(5)][VAT-12] |
| Compulsory application interval | Within 21 days of becoming liable; actual endpoint requires the applicable time-computation/calendar chain. | [12(3)][VAT-12] |
| Quarterly election amount | NZD 300,000 or less under section 15(1A), with notice and no overdue returns; section 15(1D) separately requires exit on a past-year or expected forward-year increase over NZD 300,000. | [15][VAT-15] |
| Ordinary monthly return/payment rule | Return by the following month's 20th day, or the immediately succeeding working day; tax payment follows the return's filing day. Final dates need the complete calendar. | [15(1)][VAT-15]; [17(1)][VAT-17] |
| VAT records | At least 5 years after the relevant return period ends, subject to the specific statutory exceptions and a written investigation extension of up to 3 further years. | [42][VAT-42] |

## Corporate workflow contract

For company income-tax work, complete all 26 intake fields in
corporate-income-tax-workflow-base Section 4 through the universal read,
infer and confirm steps. The selected country intake above supplements those
fields. Before computation, evaluate all loaded refusal catalogues, including
R-CIT-1 through R-CIT-12. A fired refusal stops computation and requires its
canonical code and complete Trigger message verbatim from the base. Missing
trigger or message evidence requires Needs Input. Record cleared and fired
codes in the reviewer brief or initial refusal reply. Ordinary scope, a
reviewer's taxable-income input and bounded component status cannot waive
these controls. A current audit or notice of deficiency fires R-CIT-6;
disputed residence fires R-CIT-9 and dual residence or hybrid mismatches
fires R-CIT-12. The sector, aggressive-position, material reorganisation,
insolvency and Pillar Two refusals also remain applicable.

Preserve the base's order: approved accounting profit before tax, cited
book-to-tax reconciliation and losses, basic rate, eligible credits and
offsets, then independently evidenced payments and the payable/refundable
balance. Trace each benefit and payment once. Preserve the cross-border and
Pillar Two analyses, current/deferred tax provision and filing assembly.
This guide supplies only the selected classification and basic-rate steps;
an unsupported preceding reconciliation or subsequent credit, payment or
provision is held. A known rate does not establish a complete computation.

Deliver all 7 reviewer-brief sections in the corporate base, its filing
assembly and all 4 universal outputs. Run all 18 corporate self-checks in
addition to the 18 universal checks and the applicable VAT checks. Record
unmet checks and missing slots as held; an illustrative rate result cannot
turn them into passed checks or a completed return. Use the country slot
status below to identify missing law, facts and operational evidence.

## Company classification and rate component

1. Confirm the entity falls within section 2's company definition and this
   ordinary scope. A Cook Islands company is a defined term, not a synonym
   for a company deemed resident. International-entity treatment is held.
2. Apply all 3 alternatives in section 82(2). Cook Islands director control
   can satisfy paragraph (a) even where decision-making also occurs abroad.
   Effective management in Cook Islands independently satisfies paragraph (b).
   Paragraph (c) requires a Cook Islands company and at least 3 resident
   directors at the same moment in the income year. Three people serving
   sequentially without the required overlap do not satisfy that branch.
   Unknown facts cannot establish failure of all branches. [82][IT-82]
3. Establish director residence separately. Section 82(1)'s home and
   more-than-183-day conditions are cumulative. Exactly 183 is not more than
   183; 184 days alone does not establish a home. Do not substitute a
   company-law director's address or the registry's residence requirement.
   Changes, conflicting residence claims or period attribution are held.
4. Record the income-source scope separately from its taxable amount.
   Section 80 covers a resident's income from all sources when derived whilst
   resident and Cook Islands source income of residents or non-residents,
   subject to the Act. Section 83 includes business carried on and contracts
   made or wholly/partly performed in Cook Islands. A foreign payer or bank
   does not by itself make income foreign-source. Mixed-source attribution
   requires section 84's just-and-reasonable Collector treatment, not a guessed
   days, sales or headcount ratio. [80][IT-80]; [83][IT-83]; [84][IT-84]
5. Obtain an independently supported taxable-income reconciliation under the
   Act. Accounting profit, turnover and cash receipts are not automatically
   taxable income. Resolve exemptions, deductions, loss treatment, special
   exemptions, foreign income and credits outside this rate component.
   Multiply the established non-negative taxable-income input by 0.20 or 0.28
   for the applicable ordinary company branch. This produces the basic-rate
   component before credits, provisional payments, assessments and penalties.
   A negative input requires separate loss analysis, not a negative tax refund.
   [2][IT-2]; [39][IT-39]; [40][IT-40]; [42][IT-42]; [rates][IT-RATES]

Annual tax returns and the registry annual return are different duties.
Section 8 generally requires the income return; section 9 needs Collector
consent for a non-December annual balance election. Section 15 and Schedule 3
determine the applicable return branch, subject to actual extensions and
calendar law. This guide does not select a payment sequence or treat the
basic-rate component as the balance payable. [8][IT-8]; [9][IT-9]; [15][IT-15]

## Ordinary VAT mechanics

### Registration and activity

Establish a continuous or regular activity involving supplies for
consideration under section 4. Profit intention is unnecessary, but the
specified private hobbies, employment services and exempt activity exclusions
remain. Section 10 charges registered persons, a term that includes persons
liable to register, not just those holding an administrative certificate.
Do not wait for a certificate to consider possible backdated liability.
[Definitions][VAT-2]; [activity][VAT-4]; [charge][VAT-10]

For an unregistered person, separately test the year ending at a month end
and the year starting at a month start. The former needs actual total value
exceeding the established threshold; the latter needs reasonable grounds
for believing it will exceed that amount. Do not replace these with a tax-year
total, a single month's receipts or an automatic turnover annualisation.
Disregard exempt supplies. A cessation, substantial permanent reduction or
replacement-capital exclusion requires the Collector to be satisfied; an
asset-sale label is insufficient. Use section 6 value with section 12(7)'s
tax exclusion. [12(1)-(3), (7)][VAT-12]

Section 12(8) includes qualifying imported services received, ignoring only
section 4A(1)(a)'s registered-recipient requirement. All other imported-service
conditions remain, including the hypothetical lack of full input recovery
in section 4A(1)(e). Do not add every overseas software bill. Actual imported
service tax, valuation, related parties and recovery need the separate complete
chain; the ordinary domestic net-tax worksheet below does not compute them.
[4A][VAT-4A]; [12(8)][VAT-12]

Voluntary application is not automatic registration at NZD 20,000. Establish
the existing/intended activity and likely supply value over the stated year,
apply in the prescribed form and obtain the Collector's determination under
section 12(5). Confirm the effective date separately. Falling below a threshold
does not itself cancel an existing registration: apply section 13 and the
Collector's cancellation date, with existing liabilities preserved.
[12(4)-(6)][VAT-12]; [13][VAT-13]

### Basis, period and supply treatment

Under section 15A, a person may elect invoice or payments basis and must
notify the Collector in the prescribed form. Established failure to elect
engages the statutory payments-basis default. Missing records do not prove
failure to elect. A change needs Collector approval and the applicable
transition under sections 15A/15B; do not switch the worksheet midstream or
duplicate opening debtors/creditors. [15A][VAT-15A]; [15B][VAT-15B]

For an ordinary supply outside section 5's special timing branches, time of
supply is the earliest tax invoice, supplier payment receipt or delivery.
Invoice-basis section 16 uses the time-of-supply period. Payments basis uses
amounts to the extent received for outputs or paid for deductible inputs in
the period. It is not simply the invoice total. Progressive, periodic, hire,
hire-purchase, undetermined-price and other special timing cases are held.
[5][VAT-5]; [16(3)-(4)][VAT-16]

Establish domestic place of supply using sections 7/8 and the actual fixed
establishment/activity facts. A foreign supplier name, customer address or
invoice currency does not settle place. Exempt and zero-rated supplies differ:
the definition of taxable supply includes zero rating, whilst exempt supplies
have their own Schedule 1 and section 10(3) conditions. Do not classify all
financial-sector charges as exempt; Schedule 1 clause 1 lists particular
services and excludes mere advice from its arranging branch. Actual exports,
zero rating, imported goods and mixed or special supplies remain held here.
[2][VAT-2]; [7][VAT-7]; [8][VAT-8]; [10][VAT-10]; [11][VAT-11];
[Schedule 1 clause 1][VAT-EXEMPT]

### Ordinary domestic ledger calculation

Use this calculation only for established ordinary standard-rated domestic
supplies with their correct value and period. Related-party discounts,
non-money consideration, composite transactions and other special valuation
require their own section 6 analysis. Where the price is genuinely wholly
inclusive of 15% VAT, gross × 3/23 gives the tax and gross × 20/23 the exclusive
value. This algebra cannot create VAT on a non-taxable purchase. Keep exact
fractions and transaction precision separately from any subsequently verified
form-rounding requirement. [6][VAT-6]; [11][VAT-11]

Section 16's ledger adds applicable output tax and additions and deducts only
eligible amounts. For an ordinary domestic acquisition, establish the other
person's registration, tax payable on the supply, correct basis/period and
taxable acquisition purpose. Whole taxable purpose permits the whole eligible
amount. Partial taxable purpose for a non-car/non-pick-up permits only the
established extent, using the section 16(6) circumstances/Collector conditions.
A partially taxable car or pick-up needs the Collector's equitable extent
by written notice. A self-selected mileage percentage cannot replace it.
[16(3)-(6)][VAT-16]

Hold the required section 18 tax invoice or section 19 note when filing,
unless an established statutory exception applies. Do not infer the prescribed
particulars from a generic receipt. This guide does not establish the current
small-invoice Order or prescribed-form fields, so neither is a shortcut for
missing evidence. Section 16(8) permits qualifying later deductions, including
a later-held invoice and amounts not previously included; check prior claims
and prohibit duplicate recovery. Nonregistered services do not acquire a
domestic input-tax amount merely through the 3/23 fraction. Secondhand goods
have a distinct rule and are held here. [16(7)-(8), (10)][VAT-16]; [18][VAT-18]

For a section 19 cancellation/variation/return, preserve the event, original
tax, corrected tax and period when correction becomes apparent. A seller's
excess tax is deducted in that later period. A recipient who already deducted
too much adds the excess in the period when the credit note or knowledge is
received; a note is not the sole possible trigger. Increased tax and debit
notes have their separate subsection (2)/(8) branches. [19][VAT-19]

Reconcile every other section 16 addition/deduction and adjustment separately,
including bad debts, imports, insurance, use changes and transitions. Missing
information is not nil. A positive net is tax payable under section 17; a
negative net is a refund due under section 29, not proof of cash paid or its
timing. Refund administration and a complete return remain held. [16][VAT-16]

### Filing frequency, payment and records

Monthly returns are the ordinary section 15(1) branch. Quarterly filing requires
the section 15(1A) election in the Collector-specified form/manner and no
overdue returns at election. It is not automatic below NZD 300,000. Apply the
separate section 15(1D) exit when the past-year or expected forward-year value
increases over NZD 300,000: finish the current quarter at its due time, then
begin monthly returns for the next month. Hold a disputed initial case where
the 2 measures conflict rather than using the word 'or' to ignore (1D).
The Collector specifies the first quarterly due date; do not invent a
quarter-end-plus-20-day date. Section 17 links payment to the required filing
day. Actual extensions and working-day endpoints need their complete chain.
[15][VAT-15]; [17][VAT-17]; [2023 amendment and Schedule][VAT-2023]

Section 42 generally requires sufficient records in Cook Islands, in English
and New Zealand currency for at least 5 years after the relevant return period.
Outside-country storage requires written Collector authorisation; electronic
access alone does not establish it. The written investigation extension,
retention waiver and liquidated-company provisions are specific exceptions,
not blanket defaults. Keep company-law and income-tax retention duties separate.
[42][VAT-42]

## Fictional worked positions

All amounts below are NZD and all entities/records are fictional. Each row
assumes the stated law, ordinary scope, current source conditions and all
unmentioned prerequisites are established for that illustration. Nil other
adjustments are expressly established in the net-tax cases. Actual engagement
source holds above remain. No row establishes a complete return.

| Case | Established facts | Computation and disposition |
|---|---|---|
| C01 | Ordinary domestic company; directors exercise control in Cook Islands, also make decisions abroad; 2 resident directors. Reviewed taxable income 82,000. | Paragraph (a) passes independently of the 3-director branch: resident; basic-rate component 82,000 × 0.20 = 16,400. [IT-82] [IT-RATES] |
| C02 | No director control in Cook Islands, but effective management is there; 1 resident director. Reviewed taxable income 50,000. | Paragraph (b) passes: 50,000 × 0.20 = 10,000 basic-rate component. [IT-82] [IT-RATES] |
| C03 | Cook Islands company; (a)/(b) independently fail; 3 established resident directors overlap for 1 day in the income year. Reviewed taxable income 60,000. | Paragraph (c) passes at a moment in that year: 60,000 × 0.20 = 12,000. Do not impose a whole-year or company 183-day condition. [IT-82] [IT-RATES] |
| C04 | Same scope and taxable income as C03, but 3 different resident directors serve sequentially and at most 2 overlap; (a)/(b) independently fail throughout the relevant period. | The paragraph (c) branch fails; not deemed resident under section 82. Basic-rate component 60,000 × 0.28 = 16,800. This does not establish a foreign regime or a final balance payable. [IT-82] [IT-RATES] |
| C05 | Director A has a Cook Islands home and exactly 183 days' presence in the relevant 12 months; B has that home and 184 days; C has 184 days but no such home. | Under the stated section 82(1) test A fails the strict day boundary, B passes both conditions and C fails the home condition. Do not count all 3 as resident directors. Conflicting residence/period facts still require review. [IT-82] |
| C06 | Company has 2 established resident directors; control and effective-management evidence are missing. | Needs Input. Neither a 20% result nor a supposedly conservative 28% result is established. [IT-82] [IT-RATES] |
| C07 | A non-resident ordinary company has an established Cook Islands business income stream and a contract partly performed there, with a foreign payer. Mixed-source allocation has not been established. | Cook Islands source must be considered under section 83; foreign payment does not settle it. Hold the taxable amount and section 84 attribution; do not apply a guessed 50% split. [IT-80] [IT-83] [IT-84] |
| V01 | Registered person, invoice basis; ordinary local sales value 20,000, eligible local acquisition value 10,000; time of supply is in the period, documents held and wholly taxable purpose. | Output 20,000 × 0.15 = 3,000; input 10,000 × 0.15 = 1,500; selected net 3,000 − 1,500 = 1,500 payable component. [VAT-5] [VAT-11] [VAT-16] |
| V02 | Same facts, expressed as wholly 15% VAT-inclusive sales 23,000 and purchases 11,500, with actual charged tax reconciled. | Output 23,000 × 3/23 = 3,000; input 11,500 × 3/23 = 1,500; exclusive values 20,000 and 10,000; net 1,500. Applying 15% to gross would be wrong. [VAT-6] [VAT-11] [VAT-16] |
| V03 | Established payments basis; ordinary VAT-inclusive sales invoice 1,150, only 575 received in period; eligible purchase invoice 460, only 230 paid in period, wholly taxable purpose and required documents held. | Output 575 × 3/23 = 75; input 230 × 3/23 = 30; net 75 − 30 = 45. Unpaid balances are not included merely because invoiced. [VAT-15A] [VAT-16] |
| V04 | Same invoices/partial payments as V03, but established invoice basis and both ordinary times of supply fall in the period. | Output 1,150 × 3/23 = 150; input 460 × 3/23 = 60; net 90. Basis changes the period amount; no transition is assumed. [VAT-5] [VAT-15A] [VAT-16] |
| V05 | Ordinary eligible non-car acquisition has evidenced VAT 90 and established taxable acquisition extent exactly 2/3 under section 16(6); output VAT 150. | Deduction 90 × 2/3 = 60; net 150 − 60 = 90. Keep the exact extent, not a rounded 66% proxy. [VAT-16] |
| V06 | Partially taxable car has VAT 150; taxpayer proposes 60% mileage use; no Collector written equitable extent. | Hold the deduction. 150 × 60% = 90 is not an authorised amount under section 16(5)(c). [VAT-16] |
| V07 | A verified nonregistered supplier provides an ordinary service for 1,150 with no VAT payable/charged; no distinct self-assessment applies. Output VAT is 150. | Ordinary domestic input tax is 0; do not invent 150 from the gross fraction. Selected net is 150. This is a known legal/input result, not a missing-invoice default. [VAT-16] |
| V08 | Eligible ordinary acquisition VAT 150, invoice required but not held when the current return is filed; current output VAT 300. The valid invoice is held when a later return is filed, all later eligibility conditions pass and no prior claim was made; later output is 300. | Current deduction is 0 under (7), current net 300. Later deduction 150 under (8), later net 150. The missing invoice does not create permanent forfeiture or permit duplicate recovery. [VAT-16] [VAT-18] |
| V09 | Ordinary sale tax 150 was accounted for; consideration is subsequently reduced so correct tax is 120. The seller identifies the correction and recipient receives the credit note in the same later period; recipient had deducted 150. | Seller later deduction 150 − 120 = 30; recipient later addition 30. These belong to separate entities' ledgers, not a zero combined tax entry. [VAT-19] |
| V10 | Conditional example only: applicable compulsory threshold is established as 40,000; qualifying past-year values are respectively 39,999.99, 40,000 and 40,000.01; forward-year test independently fails. | Only 40,000.01 exceeds that amount. Equality alone does not trigger (1)(a). Actual registration conclusions remain held if the Order gate is unresolved. [VAT-12] |
| V11 | Conditional 40,000 threshold established; qualifying supply value 39,000 plus 2,000 from replacing plant. Collector satisfaction with the sole-replacement exclusion is established. | 41,000 − 2,000 = 39,000 for that test; not exceeded. Without the Collector condition, do not silently remove 2,000. The forward-year test remains separate. [VAT-12] |
| V12 | Conditional 40,000 threshold established; domestic qualifying value 38,000 plus received imported services value 3,000. All section 4A conditions except registered-recipient status pass, including lack of full hypothetical deduction. | Section 12(8) total 38,000 + 3,000 = 41,000 exceeds the assumed amount. If full hypothetical recovery instead applies, that service fails (4A)(1)(e); do not include it automatically. Actual imported-service tax remains held. [VAT-4A] [VAT-12] |
| V13 | Intended taxable activity from a specified date; likely supplies over its following year are exactly 20,000 in one scenario and 20,001 in another; all other voluntary application facts established. | Exactly 20,000 does not exceed the printed voluntary amount; 20,001 passes that amount limb. Neither is automatic registration: obtain Collector eligibility and effective date. [VAT-12] |
| V14 | Registered person has both relevant supply measures of 300,000, no overdue returns, proper quarterly notice and Collector first due date established. Later during a quarter the expected forward-year amount rises to 300,001. | Equality does not alone defeat the amount limb. On the later increase, finish the current quarter at its required time, then furnish monthly returns for the immediately following month. Do not switch mid-quarter. [VAT-15] [VAT-17] |
| V15 | Both measures are 250,000, but an overdue return exists when the proposed quarterly election is made. | Section 15(1B) prevents that election then. A low turnover figure does not establish quarterly filing. [VAT-15] |
| V16 | Established ordinary invoice-basis period has output tax 150 and eligible input tax 300, with all additions/adjustments independently nil. | 150 − 300 = −150: refund due component of 150 under section 16(9), subject to section 29. No cash refund date or complete return is established. [VAT-16] |

## Holds, refusals and defaults

| Hold | Trigger | Required evidence or work |
|---|---|---|
| H01 | Requested period/current material law not established | Operative primary chain, including subsequent laws, commencement and actual instruments; metadata is insufficient. |
| H02 | Special entity, group, activity, overseas/international treatment or disputed scope | Separate applicable law and professional classification. |
| H03 | Director control, effective management, concurrent tenure or residence incomplete | Dated evidence for every relevant branch; do not choose a higher rate as a default. |
| H04 | Taxable income, exemptions, deductions, losses, credits or source attribution unresolved | Reviewed reconciliation and any required Collector treatment; no accounting-profit shortcut. |
| H05 | Company provisional/final payment calendar or assessment amounts requested | Resolve the statutory/MFEM conflict and actual notices, instalment rules and credits before selecting amounts/dates. |
| H06 | Applicable compulsory VAT threshold/Order unknown | Current amount and effective dates from authoritative instruments; conditional examples do not close the gate. |
| H07 | Registration, cancellation, taxable activity or effective date unresolved | Actual values, reasonable grounds, applications and Collector determinations; no certificate-only or automatic-cancellation assumption. |
| H08 | Basis election, absence of election or approved transition unknown | Prescribed notice and history; apply sections 15A/15B before period allocation. |
| H09 | Place/time/value, exemption, zero rating, imports or related-party/special supply unresolved | Complete transaction-specific law and evidence; no brand/currency/rate default. |
| H10 | Acquisition purpose, required invoice/note or prior claim unresolved | Actual tax and prescribed documents, established extent and any Collector written car/pick-up determination. |
| H11 | Other additions/deductions, bad debts, use changes or refund administration incomplete | Reconcile every applicable adjustment and administrative condition; missing amounts are not nil. |
| H12 | Quarterly eligibility, notice, overdue status, first date or exit sequence unresolved | Apply all section 15 conditions and Collector date; disputed inconsistent initial measures require review. |
| H13 | Actual working-day/deadline or retention endpoint requested | Complete interpretation, holidays/declarations, event date, period and applicable notice/exception; no invented extension. |
| H14 | Complete return, portal/form mapping, supplier catalogue, regional companion or runtime capability missing | Complete every required country/domain slot, output and check before operational delivery. |

| Code | Trigger | Verbatim output |
|---|---|---|
| R-CK-TAX-INPUT | A required ordinary company/VAT fact is missing or inconsistent. | "Needs Input: a required Cook Islands company tax or VAT fact is missing or inconsistent. Identify the fact and its effect before applying the affected rule." |
| R-CK-TAX-SOURCE | Applicable law or a necessary interpretation is unresolved. | "The requested Cook Islands tax or VAT output is on hold because its applicable authority is incomplete or unresolved. Identify the missing authority and obtain qualified local review before proceeding." |
| R-CK-VAT-RETURN | A complete VAT return is requested without every mandatory companion, country slot, runtime capability and output. | "This Cook Islands VAT component is incomplete for return preparation. Complete the required companions, country slots, runtime capabilities, outputs and checks before preparing or delivering a return." |
| R-CK-VAT-QUESTIONS | More than 10 grouped factual questions remain after the loaded bases' permitted filtering. | "More than 10 questions remain after the required filtering and grouping. This Cook Islands VAT workflow cannot complete the return. Please refer the records and unresolved questions to a qualified practitioner." |

Retain every applicable universal/domain refusal and exact runtime stop message.
An unknown fact is Needs Input; an unresolved rule is a source hold. These
labels do not waive a fired refusal or permit partial classified-return delivery.

| Ambiguity | Permitted disposition |
|---|---|
| Unknown law, rate, threshold, scope, source allocation or calendar | Hold; no higher-tax legal default. |
| Missing residence, registration, basis, notice, taxable-use or document evidence | Needs Input; no assumed absence, zero, full use, payment basis or monthly/quarterly election. |
| Actual evidence establishes no accounting-basis election | Section 15A(2)'s statutory payments basis, with evidence recorded; this is not a default for missing records. |
| Actual evidence establishes a required invoice is not held at filing | Apply section 16(7) to that deduction and preserve the possible later section 16(8) route; do not invent an invoice exception. |
| Missing other tax, adjustment or credit information | Hold affected totals; no assumed nil. |

Flag every source hold, boundary, eligibility failure, missed date, partial
purpose and incomplete output regardless of cash amount. Obtain and record
the reviewer's HIGH transaction/tax-delta, MEDIUM concentration, LOW position
and question-filter thresholds before a complete VAT workflow. This component
sets none, and no EUR threshold is imported. No missing fact has an authorised
cash-floor default; an unknown impact remains flagged.

## Working paper and acceptance checks

Extend the universal working paper with separate company-residence/source,
basic-rate and VAT component schedules. Record source/version/effective date,
confirmed facts, rule branch, exact value basis, calculation, result, hold,
missing evidence and reviewer action. Preserve natural-person residence,
concurrent-director history, company residence and income attribution as
separate fields. Show gross, exclusive value, charged VAT, eligible VAT,
accounting basis, time/payment event and return period separately.

Use identifiable ledger labels for components, not invented return box codes.
Reconcile each transaction once, retain exclusions with reasons and trace
additions/deductions to their statutory branch. The actual form and complete
return workbook remain held. All 4 universal outputs and every VAT domain
output/check remain required for an engagement. A component calculation does
not substitute for a recalculated workbook, reviewer brief, action list or
review checklist. The corporate workflow contract above also remains
mandatory for company income-tax work.

| Corporate country contract slots | Component status and remaining work |
|---|---|
| Regime identification | CK, selected Income Tax Act provisions and MFEM authority identified. Current filing form, portal/format and complete filing mechanics held; the conflicting payment/instalment calendar remains held. |
| Rates | Ordinary resident 20% and nonresident 28% basic-rate component on reviewed taxable income only. Small-company, reduced/activity, surcharge and branch-profits regimes require separate current-law verification; none is assumed nil or inapplicable. |
| Adjustments | Complete non-deductible expense, exempt-income, depreciation and interest-limitation rules and the PBT reconciliation held. Supplied taxable income needs independent review. |
| Losses | Carryforward period and caps, carryback, ownership restrictions and group relief held. A negative amount is not an evidenced loss balance or refund. |
| Credits | R&D, IP/patent, foreign-tax, investment and withholding credit eligibility, ordering and carryforwards held. No credit or absence of credit is inferred from the rate result. |
| Filing mechanics | Prescribed forms, submission portal/format, supporting schedules and audit thresholds held. A registry return is not an income-tax return. |
| Anti-avoidance | Complete GAAR, CFC, hybrid and any corresponding special inclusion rules held. The corporate base's refusals still apply. |
| Pillar Two overlay | Current QDMTT, IIR, UTPR and domestic top-up position held. Test group scope and preserve R-CIT-11; no non-enactment inference follows from missing sources. |
| Cross-references | Withholding, Pillar Two, disclosure, IP/R&D, free-zone and transfer-pricing companions require verified applicability and country content. Their absence does not establish an exemption or a completed workflow. |

| VAT country contract slots | Component status and remaining work |
|---|---|
| 1-2. Rates | Ordinary 15% component only; complete zero/reduced/exempt/special treatment remains open. |
| 3-4. Return fields and portal | Current prescribed form, exact fields and authenticated filing procedure held. |
| 5. Deadlines | Selected monthly and quarterly rules only; actual dates/extensions/first quarterly date require evidence. |
| 6-7. Supplier and exclusion patterns | Comprehensive evidenced supplier catalogue and country exclusion mapping held; names alone cannot establish VAT. |
| 8-10. Refusals, questions and defaults | Selected component catalogue above; complete transaction catalogue and companion refusals held. Unknown facts have no invented tax default. |
| 11. Worked examples | Selected fictional positions above; no complete transaction-classification or return acceptance claimed. |
| 12. Excel template | Component fields specified; official box mapping, full template and verified runtime/recalculation held. |
| 13. Attention thresholds | Reviewer values required and not established here. |
| 14. Required inputs | Component intake above; complete-return minimum/recommended/ideal manifest and its refusal policy held. |

Before accepting a component, check all of the following:

- The required corporate base is loaded for company tax; all 26 intake
  fields, 12 refusal codes, 7 brief sections and 18 corporate checks remain
  mandatory. Missing country slots stay held rather than silently defaulted.
- Requested period, ordinary scope and applicable law are established; the
  payment-calendar and threshold-Order holds have not been silently cleared.
- All 3 company residence branches and director home/day/concurrency facts
  are separate; foreign payer, incorporation or address is not a shortcut.
- The rate applies to reviewed taxable income, with no negative-tax/loss,
  accounting-profit, final-payment or foreign-credit inference.
- Registration uses the correct rolling/forward windows, strict excess,
  exclusions, imported-service conditions and Collector effective dates.
- Basis evidence, ordinary/special time of supply, value and partial payments
  put each amount in the correct period with no duplication.
- Actual charged tax, supplier status, prescribed invoice/note, acquisition
  extent and car/pick-up written determination support every deduction.
- Later-invoice and note/knowledge adjustments use the correct later period;
  other additions/adjustments and prior claims reconcile independently.
- Exact fractions, sign and precision are retained. Form rounding, return
  box mapping, refunds, holidays and storage permissions are not invented.
- Quarterly election, overdue status, Collector date and next-month-after-
  current-quarter exit are checked separately from the amount boundary.
- Every source item, hold, refusal and reviewer flag appears in its required
  working paper, brief, action list and review checklist. Complete domain
  slots and outputs remain mandatory; component checks do not establish
  professional sign-off or comprehensive jurisdiction acceptance.

Version 0.1, checked 24 October 2026. This adds selected ordinary company and
VAT components and records explicit unresolved source/operational gates.
Tier 2, pending_review and verified_by pending remain. Complete tax returns,
payroll, social, cross-border, property, reporting and other compliance topics
remain open. Recheck primary law for a later period or changed fact pattern.

[LAW-DATE]: https://cookislandslaws.gov.ck/api/retrieve_web_text_master/HomePanel-HeadingSecond
[LAW-HELP]: https://cookislandslaws.gov.ck/api/retrieve_help_page
[IT-PREFACE]: https://cookislandslaws.gov.ck/api/display_pages/INCOME%20TAX%20ACT%201997
[VAT-PREFACE]: https://cookislandslaws.gov.ck/api/display_pages/VALUE%20ADDED%20TAX%20ACT%201997
[IT-2]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S2_htm
[IT-8]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S8_htm
[IT-9]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S9_htm
[IT-15]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S15_htm
[IT-39]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S39_htm
[IT-40]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S40_htm
[IT-42]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S42_htm
[IT-80]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S80_htm
[IT-82]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S82_htm
[IT-83]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S83_htm
[IT-84]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S84_htm
[IT-RATES]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_ITA_ITA97_SCH1_CL2_htm
[IT-179]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S179_htm
[IT-180]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S180_htm
[IT-188]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S188_htm
[IT-190]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_ITA_ITA97_S190_htm
[IT-CALENDAR]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_ITA_ITA97_SCH3_CL1_htm
[IT-2013]: https://www.mfem.gov.ck/_files/ugd/dbdf40_6ba91c45683e4f9699b77b7bffbd96e2.pdf
[IT-2021]: https://www.mfem.gov.ck/_files/ugd/dbdf40_893ff82f06544d5d93729009dcf86ad6.pdf
[MFEM-CALENDAR]: https://www.mfem.gov.ck/_files/ugd/dbdf40_87b3c94f47854a4e956a21865546b948.pdf
[VAT-2]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S2_htm
[VAT-3]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S3_htm
[VAT-4]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S4_htm
[VAT-4A]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S4A_htm
[VAT-5]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S5_htm
[VAT-6]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S6_htm
[VAT-7]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S7_htm
[VAT-8]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S8_htm
[VAT-10]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S10_htm
[VAT-11]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S11_htm
[VAT-12]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S12_htm
[VAT-13]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S13_htm
[VAT-15]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S15_htm
[VAT-15A]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S15A_htm
[VAT-15B]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S15B_htm
[VAT-16]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S16_htm
[VAT-17]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S17_htm
[VAT-18]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S18_htm
[VAT-19]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S19_htm
[VAT-42]: https://cookislandslaws.gov.ck/api/display_pages/sect_LOCI_VATA_VATA97_S42_htm
[VAT-EXEMPT]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_VATA_VATA97_SCH1_CL1_htm
[VAT-EXEMPT2]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_VATA_VATA97_SCH1_CL2_htm
[VAT-EXEMPT3]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_VATA_VATA97_SCH1_CL3_htm
[VAT-EXEMPT4]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_VATA_VATA97_SCH1_CL4_htm
[VAT-EXEMPT5]: https://cookislandslaws.gov.ck/api/display_pages/clause_LOCI_VATA_VATA97_SCH1_CL5_htm
[VAT-2014]: https://www.mfem.gov.ck/_files/ugd/dbdf40_80a266044fa7415c913c673207fb75e0.pdf
[VAT-2023]: https://parliamentci.wpenginepowered.com/wp-content/uploads/2023/04/Value-Added-Tax-Amendment-Act-2023-No.-02.-signed-copy.pdf
[VAT-2026]: https://parliamentci.wpenginepowered.com/wp-content/uploads/2026/05/Value-Added-Tax-Amendment-Act-2026-No.-4.pdf

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
