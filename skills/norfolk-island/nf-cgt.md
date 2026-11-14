---
name: nf-cgt
description: >
  Establish selected Norfolk Island capital gains and losses for 2026-27.
  Use for asset disposals, contract dates, the Norfolk pre-reform transition,
  capital proceeds, cost base, loss ordering, discount eligibility, homes,
  collectables and foreign-resident property. Covers the October 2026
  property and ownership-interest amendments and conditional renewable-energy
  concession. Includes primary legislation, fictional calculations and
  source-period checks. Distinguishes current-year rules from enacted 2027
  changes, capital losses from deductions, and transfer fees from CGT.
  Preserves residence, valuation, treaty, withholding, specialised-event and
  actual-return gates, applicable workflow outputs and professional review.
  This reference does not complete the country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Ordinary 1 July 2026 to 30 June 2027 income year; sources checked 18 October 2026; foreign-resident amendments apply by their October 2026 event and assessment rules; 2027 reforms identified separately"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
  - nf-income-tax
  - nf-company-tax
---

# Norfolk Island: capital gains, losses and foreign-resident property

Establish the entity, residence history, asset and ownership interest,
acquisition and event dates, income year, proceeds, valuation, cost and
reduced cost bases, earlier losses and claimed relief. Record reviewer-held
evidence readiness. Do not query private ownership records or obtain client,
identity or bank documents through this reference.

Load `workflow-base` and `nf-tax-system`, then the individual income-tax or
corporate income-tax workflow base and substantive references appropriate
to the entity. Preserve the confirmed profile, source and period gates,
refusals, four universal outputs and applicable domain outputs and checks.
Mandatory facts remain Needs Input and unresolved law remains held. The
figures below are selected components, not an actual return, conveyance or
complete capital, property or country pack.

## Establish the territory, period and applicable text

Income Tax Assessment Act section 960-505 expressly includes **Norfolk
Island** in Australia when the term is used geographically. The ATO's
Norfolk individual guidance includes investment/capital-gains and foreign
income in the tax profile. Residence, source and particular exemptions
still require their own tests; an NF address is not a universal exemption.
[DICT]; [NI]

The latest published assessment-Act compilation checked was **C267,
27 August–30 September 2026**, with an express warning about unincorporated
commenced amendments. The current rules require this source chain:

| Source | Application that matters here |
|---|---|
| Assessment Act C267 | Read selected operative provisions, not merely its latest-version label. [CGT]; [FOREIGN] |
| Tax Reform No. 1 Act 2026 | Division 102 amendments apply to assessments for the income year **including 1 July 2027** and later years. For the ordinary 2026–27 year, retain the previous five-step net-gain method. Current section 115-100 separately retains the ordinary discount branch for events **before 1 July 2027**. [REFORM1, Schedule 1 item 82][REFORM1]; [PREVIOUS]; [CGT] |
| Tax Reform No. 2 Act 2026 | The selected residential-property exception extensions in Schedule 4 apply to **2027–28 and later income years**. They do not establish a current-year blanket dwelling exemption. [REFORM2] |
| Tax Adviser Misconduct and Other Measures Act 2026 | Schedules 2–3 commenced **1 October 2026**. Division 855 amendments apply to **CGT events on or after that day**; other assessment-Act amendments have an income-year-start application rule. The Agreements Act amendment applies from that day. [OCTOBER, section 2 and Schedule 2 item 39][OCTOBER] |

This guide's ordinary calculations assume the income year ending **30 June
2027**. A substituted accounting period needs its own application analysis.
Do not import the latest seven-step residential/quarantine method into that
ordinary year, or project a current discount/exemption unchanged beyond its
statutory boundary. Enacted 2027 indexation, minimum-tax and other changes
require a separate computation. [REFORM1]; [REFORM2]

## Preserve the Norfolk transition

Transitional Provisions Act section 102-25(2) requires **all four** conditions:

1. The entity was a prescribed person under the former territorial exemption
   division because of Norfolk residence on or before **23 October 2015**.
2. It acquired the CGT asset on or before that day.
3. The asset is not already a pre-CGT asset.
4. A hypothetical CGT event immediately before **24 October 2015** would
   have produced a gain or loss disregarded because of that prescribed
   status. [TRANS]

When the conditions hold, Parts 3-1 and 3-3 apply with references to
**20 September 1985 read as 24 October 2015**. For a qualifying ordinary
disposal, read that substitution with event A1's acquisition-date exception.
Do not substitute the Cocos market-value rebasing rule or assume that
everything owned by someone with an NF address qualifies. Establish the
historical prescribed status and hypothetical treatment for the particular
asset. Separate improvements, later interests and other events need their
own analysis. [TRANS]; [CGT, section 104-10][CGT]

The acquisition-date record exception in subsection (3)(b) is limited.
Subsection (4)'s election concerns **Cocos subsection (1)**, not an election
to disapply the Norfolk rule. No universal market-value uplift or permanent
exclusion from every later CGT provision is established here. [TRANS]

## Identify the event and capital amount

A CGT asset can be property, a legal/equitable right, part of an asset,
goodwill or a partnership interest. Identify capital versus revenue,
trading-stock, depreciating-asset and special regimes before computing.
Section 118-20 can reduce a capital gain where an amount is otherwise
included in income, with exceptions; it does not make the ordinary-income
amount disappear. [CGT, sections 108-5 and 118-20][CGT]

Under **CGT event A1**, disposal ordinarily involves a change of ownership.
Its time is **the disposal contract**, or, without a contract, the ownership
change. A contract that fails before completion does not produce an A1
event merely because it was signed. Compulsory acquisition has a separate
earliest-event rule. Event selection under section 102-25 also has priority
and concurrent-event exceptions; not every cancellation, grant, death or
restructure is A1. [CGT, sections 102-25 and 104-10][CGT]

For A1:

- A gain arises when **capital proceeds exceed cost base**.
- A loss arises when **capital proceeds are below reduced cost base**.
- Proceeds between those two bases can produce neither. The bases are not
  interchangeable. [CGT, section 104-10][CGT]

Capital proceeds generally include money **received or receivable** and
the event-date market value of other property received or receivable.
Net GST, if applicable, has its own adjustment. A cash deposit, loan payout
or net settlement receipt is not automatically the proceeds. [CGT,
section 116-20][CGT]

Section 116-30 substitutes market value in specified no-proceeds,
unvalued-proceeds and non-arm's-length/C2 cases, with exceptions. Section
112-20 separately governs the acquirer's substituted first cost-base
element. A gift is not automatically outside CGT, and a related-person
land-transfer fee's valuation rule does not settle either CGT amount.
Use `nf-property-transfers` for those separate fees and levies. [CGT]

## Cost base and loss controls

Section 110-25 has five cost-base elements, subject to adjustments:

| Element | Selected content |
|---|---|
| Acquisition | Money paid/payable and acquisition-date market value of other property given/payable, subject to substituted bases. |
| Incidental costs | Qualifying acquisition/event costs under section 110-35, including relevant transfer costs, duty, brokerage and professional costs with their conditions. |
| Ownership costs | Specified holding costs for assets acquired after **20 August 1991**, subject to the deduction and asset-class restrictions. |
| Capital expenditure | Qualifying expenditure to increase/preserve value or install/move the asset; the goodwill restriction matters. |
| Title | Qualifying capital expenditure to establish, preserve or defend title or a right over the asset. [CGT] |

Do not add expenses twice. Section 110-45 excludes specified deductible or
recouped expenditure and adjusts for relevant previous-owner deductions.
Input-tax-credit and other adjustments also matter. Reduced cost base has
its own third element and exclusions under section 110-55, and excludes
indexation; it is not simply the five cost-base amounts copied unchanged.
Actual indexation, corporate distribution and special reduced-base
formulas remain subject to their applicable rules. [CGT]

A net capital loss is **not deductible from assessable income**. For the
ordinary 2026–27 net-gain calculation:

1. Apply current-year capital losses to current-year capital gains.
2. Apply unapplied earlier net capital losses, in the order they arose.
3. Apply the available discount to the remaining eligible gains.
4. Apply qualifying small-business concessions under their own conditions.
5. Add the remaining gains into the **net capital gain included in assessable
   income**. [PREVIOUS, sections 102-5 and 102-15][PREVIOUS];
   [CGT, section 102-10][CGT]; [REFORM1, Schedule 1 item 82][REFORM1]

The earlier method permits choices about which gains losses reduce;
special loss classes and restrictions remain. Do not discount the gain
before deducting the losses, use the same loss twice, or apply the later
residential-category priority to this ordinary year. Bankruptcy/debt-release,
company/trust continuity and other special rules require separate analysis.
[PREVIOUS]; [CGT]

## Ordinary discount and asset-class relief

For a qualifying ordinary individual gain from an event **before 1 July
2027**, the current section 115-100 branch specifies **50%**, subject to
foreign/temporary-residence and other conditions. A discount capital gain
requires an eligible entity, the relevant post-September-1999 event,
non-indexed calculation, and generally an asset acquired **at least
12 months before** the event. Deemed acquisition, event exclusions and
anti-avoidance rules can change the result. A company does not receive the
ordinary individual's discount merely because its shareholder is an
individual. The separate foreign renewable-energy provision below is a
different statutory branch. [CGT, sections 115-10 to 115-30 and 115-100]
[CGT]

Sections 115-105/110 can apply where an individual had foreign or temporary
residence during the relevant period after **8 May 2012**, including trust
and carried-over residence-history cases. Establish the full testing period
and applicable apportionment before selecting a discount. Residence at the
sale date alone does not establish 50%. Complying-superannuation, trust,
affordable-housing and other special percentages or rules require their
particular conditions. [CGT]

For a confirmed collectable, section 118-10 generally disregards a gain
or loss where the relevant **first cost element is A$500 or less**; an
interest has a distinct whole-asset market-value test. Above the exemption,
collectable losses can offset **collectable gains only**, with their own
carryforward ordering. [CGT, sections 108-10 and 118-10][CGT]

For a confirmed personal-use asset, section 118-10 generally disregards a
gain where that first element is **A$10,000 or less**. Personal-use losses
are disregarded. Land, a stratum unit and specified separate buildings or
structures are **not** personal-use assets under section 108-20(3); private
use does not itself place a house within that threshold. Confirm actual
asset classification and any special rule. [CGT]

## Main residence: test the conditions separately

Section 118-110's basic case requires an individual and main-residence use
throughout the ownership period, with separate deceased-estate and
income-producing-use rules. Its foreign-resident exclusion and conditional
life-events test can prevent relief: a continuous foreign-residence period
**over six years** is an excluded-resident branch; six years or less does
not by itself satisfy the specified life events. [CGT]

Adjacent-land relief requires the same event and relevant private/domestic
use. The ordinary area cap is **two hectares including the land under the
dwelling**, with a particular rule for an earlier CGT event affecting the
exempt area. A large NF
property does not obtain full relief merely because a house stands on it.
[CGT, section 118-120][CGT]

The absence choice in section 118-145 can continue main-residence treatment
for a former home. Income-producing use generally has a **six-year** maximum
per qualifying period; non-income-producing absence has a different rule.
Other dwelling choices, returning to live in the dwelling, special cases
and the foreign-resident exclusion still matter. The absence rule is not a
blanket exemption for a foreign resident. [CGT]

Section 118-192 can substitute first-income-use market value if its partial
exemption, first-use timing and prior full-exemption conditions hold. It is
not a revaluation election for every rental property. Do not combine it
with the Norfolk transition or a transfer-fee valuation without testing
each rule. Full partial-exemption, deceased-estate and rollover calculations
remain held for the actual facts. [CGT]

## Foreign residents: apply the October 2026 overlay

Section 855-10 ordinarily disregards a foreign resident's gain **or loss**
on a non-taxable-Australian-property asset, subject to the full rules.
Taxable Australian property includes the statutory real-property,
indirect-interest, permanent-establishment, option/right and residence-exit
categories. An asset or share has to be classified before the exclusion
can be used. Norfolk's inclusion in geographic Australia matters for this
analysis. [FOREIGN]; [DICT]

For events from **1 October 2026**, Act 86 expands the real-property branch
to specified property related to Australian land and things fixed or
installed on it, **water entitlements** relating to Australian resources,
and specified options/rights. The new definition includes specified
interests, personal rights, licences, contractual rights and installed
things, regardless of particular state/territory or general-law fixture
treatment. Do not use the old land-and-lease wording alone. [OCTOBER,
Schedule 2 items 14–20 and 39][OCTOBER]

An indirect real-property interest has **two distinct tests**. The
non-portfolio test generally uses **10% or more**, including the relevant
associates and participation rules, and the specified current/historical
holding periods. The principal-asset test uses **TARP value exceeding
non-TARP value**, with tracing, anti-purpose and duplication rules. Act 86
adds a principal-asset **365-day lookback**, unless a determined-time branch
applies, and treats specified Australian mining information as TARP for
this purpose. Passing a percentage at sale alone is insufficient.
[FOREIGN, sections 855-25 to 855-32][FOREIGN]; [DICT, section 960-195][DICT];
[OCTOBER]

The Agreements Act amendment addresses treaty meanings where an agreement
refers the relevant real-property expression to Australian law. It does
not establish that every treaty applies to every NF transaction or that
every treaty uses that reference. Verify the actual agreement's territorial
scope, residence, property/source articles, eligibility and relief.
[OCTOBER, Schedule 2 item 21][OCTOBER]

Acquisition withholding is a separate purchaser/declaration/notice analysis.
Act 86 adds conditions for relying on specified declarations, including
transaction aggregation and an exception where the relevant statutory
amount is **less than A$50 million**. This is **not** a general threshold
below which CGT or all acquisition withholding disappears. Its notice
timing includes distinct period-length branches. This reference does not
select the withholding rate, form, actual notice deadline, declaration or
remittance for a transaction. [OCTOBER, Schedule 2 items 22–37][OCTOBER]

### Conditional renewable-energy concession

Act 86 Schedule 3 inserts a separate transitional Division 855. For the
specified foreign residents **other than individuals**, or trustees of
foreign trusts, a qualifying gain is treated as a discount capital gain
with **50%**, regardless of whether it otherwise meets the ordinary
discount classification. It requires all the asset, status and event
conditions; events must occur from commencement and **before 1 July 2040**.
[OCTOBER]

The relevant Australian renewable-energy asset must be TARP and have the
specified primary renewable-generation/production or electricity-storage
purpose. A qualifying indirect interest must also meet its particular
requirements. Its renewable-energy asset test generally requires RE value
**at least three times** other TARP value, with indirect tracing,
anti-purpose and duplicated-asset adjustments. Equal-to-three-times meets
that numerical limb; it does not establish the whole concession. This is
not an exemption for every energy business, every foreign individual or
every company. [OCTOBER, Schedule 3][OCTOBER]

## Fictional 2026–27 component checks

Assume each stated classification and amount is established, no unmentioned
exemption, rollover or adjustment applies, and the ordinary income year
ends June 2027. These are components before actual return and other-income
calculations. [CGT]; [PREVIOUS]; [TRANS]; [OCTOBER]

1. **Eligible resident individual's ordinary shares:** A$50,000 acquisition,
   A$1,000 eligible acquisition costs and A$1,500 eligible disposal costs
   give **A$52,500 cost base**. A$90,000 proceeds produce **A$37,500 gain**.
   A$5,000 current losses and A$2,500 available older losses leave
   **A$30,000** before discount. With all ordinary discount conditions met,
   the selected net-gain component is **A$15,000**. It is included in income;
   it is not a separate tax bill.
2. **Ordinary resident company, same amounts:** with no special concession,
   **A$30,000** remains after those losses. The individual shareholder's
   status has not supplied a 50% company discount. Company income, other
   deductions, rate and offsets require `nf-company-tax`.
3. **Loss-allocation choice:** A$20,000 non-discount gain, A$40,000 eligible
   50%-discount gain and A$10,000 current losses give **A$30,000 net gain**
   if losses reduce the non-discount gain first. Applying them to the
   discount gain instead gives **A$35,000**. This illustrates the ordinary
   2026–27 choice, not the later category-priority method.
4. **Separate bases:** cost base A$70,000, reduced cost base A$60,000 and
   proceeds A$65,000 yield **neither an A1 gain nor an A1 loss**. A sale at
   A$55,000 instead gives **A$5,000 capital loss**, subject to restrictions.
5. **Ordinary gift, no relief:** cost base A$10,000 and event-date market
   value A$30,000 give **A$20,000 gain** when the no-proceeds substitution
   applies. Zero cash proceeds have not established a nil gain.
6. **Norfolk cutoff:** an asset acquired on 23 October 2015 with all four
   section 102-25(2) conditions met can reach A1's substituted pre-cutoff
   disregard for a 2026–27 disposal. Acquisition on **24 October 2015**
   fails that acquisition limb. Neither case establishes the treatment of
   separate improvements or a later-year event.
7. **Foreign-interest numerical limbs:** TARP A$5 million and non-TARP
   A$5 million do not satisfy the principal-asset strict-excess test;
   A$5,000,001 TARP against A$5 million does. A relevant 10% holding meets
   the non-portfolio numerical threshold, but neither test alone establishes
   the other or replaces the October lookback and tracing requirements.
8. **Renewable numerical limb:** RE value A$9 million and other TARP
   A$3 million satisfy the three-times limb; A$8,999,999 and A$3 million
   do not. Only if **all** concession conditions are met does a remaining
   A$1 million qualifying gain have a **A$500,000** discounted component.

The A$500 and A$10,000 asset exemptions are inclusive first-element tests;
the non-portfolio threshold is inclusive, the principal-asset comparison
is strict, and the renewable comparison is inclusive. Keep their bases,
classes and conditions separate.

## Records, reconciliation and remaining work

Sections 121-20 to 121-30 require records relevant to possible capital
gains/losses, including dates, amounts, parties, valuations and cost-base
adjustments. The retention rule generally runs until **five years after
it becomes certain that no further relevant CGT event can happen**, not
five years after acquisition. Limited exemptions, rollovers and the Norfolk
acquisition-date exception do not justify destroying all evidence. [CGT];
[TRANS]

For each actual asset, reconcile the event, residence, territorial/source
position, proceeds, both bases, exemptions, current/older/class-restricted
losses, discount and concessions to the applicable year's return and
schedule. Preserve the income-tax or company workflow's required
deliverables. CGT inclusion, purchaser withholding and property-transfer
fees have distinct bases and timing.

Still open: full event catalogue and asset valuation; residence-exit/entry,
foreign discount apportionment and treaty outcomes; complete company/trust,
estate, small-business and rollover conditions; current instruments and
forms for actual acquisitions; full main-residence apportionment; enacted
2027 computations and remaining country topics. Missing facts or sources
remain held rather than being replaced with assumed exemptions or rates.

## Primary sources and provenance

Checked **18 October 2026**. This is a **Tier 2 source-cited draft awaiting
professional review**. Current Register records and the unincorporated
amendment list were checked alongside selected provisions. Earlier and
latest sections were compared; the previous net-gain method is used only
with the amending Act's application rule, not as a claim that an old
compilation is current in full.

The relevant October foreign-resident schedules and their commencement and
application provisions were read in full. Large assessment-Act volumes
were read in selected sections. Omitted image formulas and statutory
examples were not represented as verified; complex formulas are not used
in these fictional components. No actual client or ownership records were
queried, and no return, declaration, registration or payment was submitted.

[NI]: https://www.ato.gov.au/norfolk-island/norfolk-island-residents-and-individual-tax
[TRANS]: https://www.ato.gov.au/law/view/print?DocID=PAC%2F19970040%2F102-25
[CGT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_3/document_3.html
[PREVIOUS]: https://www.legislation.gov.au/C2004A05138/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_3/document_3.html
[FOREIGN]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[REFORM1]: https://www.legislation.gov.au/C2026A00049/asmade
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade

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
