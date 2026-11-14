---
name: nf-uk-treaty-relief
description: >
  Establish selected Australia-UK treaty conditions for Norfolk Island in
  2026. Use for UK counterparties, dual residence, transparent entities,
  dividends, interest, royalties, permanent establishments and double-tax
  disputes. Covers geographic inclusion, covered persons and taxes, current
  MLI matching, conditional source-tax limits, purpose restrictions, credit
  coordination and the mutual-agreement notification clock. Includes primary
  instruments, authority texts, fictional components and boundary checks.
  Requires separate domestic liability, residence, beneficial ownership,
  payment and procedure evidence. Preserves universal and domain outputs
  and holds actual returns, claims and specialist computations. This Tier 2
  reference does not complete the treaty network or country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Sources checked 21 October 2026; Australian and UK tax years, payment dates and MLI effect dates must be established separately"
tier: 2
last_updated: 2026-10-21
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - cross-border-workflow-base
  - nf-tax-system
  - nf-investment-withholding
  - nf-foreign-income
---

# Norfolk Island: selected Australia-UK treaty relief

Establish the taxpayer, both domestic residence positions, relevant income,
source, covered tax, tax period and payment/event date before selecting
treaty treatment. A Norfolk address, a UK bank account or a certificate
alone does not establish every condition for relief.

Load `workflow-base`, `cross-border-workflow-base`, `nf-tax-system` and
the applicable individual or corporate income-tax and other domain bases.
Keep the confirmed profile, source and period gates, decisions, refusal
trace, 4 universal outputs, 5 cross-border map components and all
applicable domain outputs and checks. Missing law or a mandatory fact
holds affected work and the complete financial package. This guide permits
bounded reference explanations and labelled hypothetical components under
their stated assumptions; it does not clear a real payment or filing.

## Scope, periods and source order

This companion covers selected provisions of the **2003 Australia-UK
Convention**, as modified by the **MLI**. The convention entered into
force on **17 December 2003**; force and effect for a particular tax or
period are separate questions. The Treasury register identifies the pair
as MLI modified. Do not substitute the terminated 1967 agreement, a model
convention or another country's territorial definition. [REGISTER]; [AUTH]

Use the authentic convention, associated instruments, authentic MLI and
the applicable matching reservations/notifications. The HMRC and ATO
synthesised texts help identify modifications; their own introductions
say that the authentic legal texts take precedence. The ATO text records
an update on **30 June 2022**, including MAP footnotes. The HMRC text was
updated **31 May 2021**. [ATO-SYNTH]; [SYNTH]; [MLI]

For this pair, the synthesised effect provisions distinguish:

| MLI application | Selected effect date |
|---|---|
| Withholding at source in either State | Events giving rise to the tax on or after **1 January 2019**. |
| Other Australian taxes | Taxable periods beginning on or after **1 July 2019**. |
| Other UK corporation tax | Financial years beginning on or after **1 April 2020**. |
| Other UK income tax and capital gains tax | Years of assessment beginning on or after **6 April 2020**. |
| MLI MAP provisions | Cases presented on or after **1 January 2019**, with the stated exclusion for cases already ineligible before modification; not simply the general tax-period dates. |

[ATO-SYNTH, entry into effect and Article 26][ATO-SYNTH]; [MLI, Article 35][MLI]

Australian sources checked include Agreements Act **C47**, effective
**1 October 2026**; Assessment Act 1936 **C193**, effective that date;
Administration Act **C227**, effective that date; and Administration
Regulations **C17**, effective **27 August 2026**. The selected Division
770 wording is in Assessment Act 1997 **C267, 27 August-30 September 2026**,
read with the later October Acts 71 and 86. C267 alone is not described as
all-law current. The selected amendment targets do not replace the
ordinary offset provisions used here. [AGREEMENTS]; [RESIDENCE]; [ADMIN];
[REGS]; [FITO-LAW]; [REFORM2]; [OCTOBER]

The ATO's 2026 offset guidance concerns the **2025-26 return**. HMRC's
2026 FIG helpsheet also concerns its stated return year. Neither supplies
every rate, form or procedure for a later year. Verify amendments,
reservations, guidance and actual forms for the requested event before use.
[FITO-WHEN]; [FITO-LIMIT]; [FIG]

## Territory, persons, taxes and residence

Article **3(1)(b)** expressly includes **Norfolk Island** in the geographic
meaning of Australia. Article 3's UK definition covers Great Britain and
Northern Ireland and its specified offshore area. Do not silently extend
that definition to the Crown Dependencies or other territories. The
catalogue's NF identifier does not create a separate treaty partner.
[AUTH, Article 3][AUTH]

Articles **1 and 4** require a resident of one or both Contracting States.
Article **2** identifies covered taxes, including specified UK income,
corporation and capital gains taxes and Australian federal income tax,
petroleum resource rent tax and fringe benefits tax, with its later-tax
rule. This is not a treaty exemption from GST, local rates, customs or
social contributions. Test those regimes under their own instruments.
[AUTH, Articles 1-4][AUTH]

Apply each domestic residence test first. Australian individual residence
under section **6(1)** has alternative ordinary-residence, domicile,
physical-presence and specified Commonwealth-superannuation branches;
passing one can be sufficient. Do not decide residence from nationality,
a visa or day count alone. Companies have a separate statutory definition;
trusts and partnerships need their own analysis. The UK's SRT applies by
tax year, with automatic overseas, automatic UK and sufficient-ties tests
and separate split-year conditions. This companion does not compute those
full domestic tests. [RESIDENCE]; [TR, paragraphs 10-16][TR]; [SRT]

Article **4(2)** excludes a person liable to tax in a State only on income
or gains from sources there. Do not carry a historical description of
Norfolk's pre-2016 source-only tax system into current residence analysis.
Use `nf-tax-system` and `nf-income-tax` for the reforms and selected
Australian rules. [AUTH, Article 4][AUTH]

Apply the treaty's actual dual-residence sequence:

| Person | Required rule |
|---|---|
| Individual | Permanent home in one State; if available in both **or neither**, centre of vital interests. If that cannot be determined, nationality; if a national of both or neither, competent-authority mutual agreement. There is **no habitual-abode step** in this treaty's Article 4(3). [AUTH] |
| Other person | MLI Article 4 replaces the original automatic effective-management tie-breaker. The competent authorities endeavour to agree, considering effective management, incorporation/constitution and other factors. **Without agreement, no treaty tax relief or exemption** under the modified paragraph. Do not retain the general MLI text's discretionary partial-relief tail: Australia's Article 4(3)(e) choice removes it for this pair. [MLI]; [AU-POS]; [UK-POS]; [SYNTH] |
| Qualifying dual listed company arrangement | Preserve the specific Article 4(5)-(6) exception and all its listing/arrangement conditions. It is not the ordinary company rule. [AUTH]; [MLI, Article 4(2)][MLI] |

For transparent entities, MLI Article **3(1)** recognises income derived
by or through a wholly or partly transparent entity/arrangement only to
the extent that a State treats it as income of its resident for tax
purposes. Ownership percentage alone does not determine that amount.
Read this alongside the treaty's definitions and the modified saving
clause; do not deny all partnership income just because Article 3's
definition of a person excludes a partnership. [AUTH, Article 3][AUTH];
[MLI, Article 3][MLI]; [SYNTH, Article 1 boxes][SYNTH]

## Match the modifications and anti-abuse conditions

The final deposit positions list this pair as **Australia's agreement
40** and **the UK's agreement 6**. Read the governing notification or
reservation and the identified treaty provision together. A choice by
one country is not a matching bilateral choice. [AU-POS]; [UK-POS]

| Issue | Selected pair result and limit |
|---|---|
| Dividend holding periods | The UK reserves against **all MLI Article 8**. Do not append its **365-day** condition to the ordinary Article 10(2)(a) 5% branch. The convention's separate 12-month condition for its zero branch remains. [UK-POS, Article 8][UK-POS]; [MLI, Article 8][MLI] |
| Agent PE extension | Both countries reserve against **all MLI Article 12**. Do not import its principal-role test into this pair. Apply the convention's actual agent rules. [AU-POS]; [UK-POS]; [AUTH, Article 5][AUTH] |
| Activity exemptions | Australia chooses MLI Article 13 Option A; the UK makes Article 13(8) notifications without the same option. Option A does not apply bilaterally by Australia's choice alone. The matched Article 13(4) anti-fragmentation rule remains relevant to the convention's activity exemptions. [MLI, Article 13][MLI]; [AU-POS]; [UK-POS]; [SYNTH, Article 5][SYNTH] |
| Resident saving clause | MLI Article 11 replaces convention Article 24. Preserve its specified exceptions for Article 9(3) and Articles 15, 18, 19, 22, 25, 26 and 28. It does not abolish the double-tax relief or MAP provisions. [MLI]; [AU-POS]; [UK-POS]; [SYNTH, Article 1 box][SYNTH] |
| Principal purpose test | MLI Article 7(1) can deny a benefit where obtaining it was one of the arrangement/transaction's principal purposes, subject to the object-and-purpose exception. Article 7(4) competent-authority relief has its own request and determination conditions. Neither substance labels nor a nominal holding clears the test automatically. [MLI]; [AU-POS]; [UK-POS]; [SYNTH, MLI Article 7 box][SYNTH] |

The OECD list checked is dated **15 September 2026**. Its UK **31 May
2024** date identifies an **arbitration profile**, not a later notification.
Australia's **2 October 2020** notification links to an objection concerning
Denmark; it is not a UK-pair amendment. Preserve the table's columns and
linked document identities when checking later changes. [OECD]

## Selected source-tax limits and computation order

These are **conditional treaty ceilings**, not automatic tax charges.
Establish domestic liability, the correct taxpayer and gross component,
treaty residence, beneficial ownership, character, source, PE connection,
special relationships, Article 23 and purpose restrictions first. A lower
domestic charge or exemption is not increased to the treaty ceiling.
[AUTH, Articles 10-12 and 23][AUTH]; [SYNTH]; [AGREEMENTS]

| Income and complete qualifying branch | Source-State ceiling |
|---|---:|
| Dividend beneficially owned by a resident company of the other State holding **directly at least 10% of voting power**, outside the zero branch | **5% of gross**. [AUTH, Article 10(2)(a)][AUTH] |
| Other qualifying dividends under Article 10(2) | **15% of gross**. [AUTH, Article 10(2)(b)][AUTH] |
| Dividend beneficially owned by a resident company of the other State with **at least 80% of voting power for the 12-month period ending on declaration**, and the specified listing/ownership or competent-authority conditions | **No source-State tax** under Article 10(3). [AUTH] |
| Ordinary qualifying interest | **10% of gross**. [AUTH, Article 11(2)][AUTH] |
| Specified government/central-bank interest, or an unrelated financial institution dealing wholly independently with the payer | **No source-State tax**, subject to the applicable conditions; the financial-institution back-to-back/equivalent-arrangement exception permits **10% of gross**. [AUTH, Article 11(3)-(4)][AUTH] |
| Qualifying royalties within the treaty definition | **5% of gross**. [AUTH, Article 12(2)-(3)][AUTH] |

For the dividend zero branch, verify the **principal class of shares**,
recognised exchange and regular trading, qualifying direct/indirect listed
ownership or the actual competent-authority determination. The Article
10(3)(a)-(b) exchange references are specific; a company being listed
somewhere is insufficient. Article 10(8) defines the principal class.
Qualifying voting power is not interchangeable with a share's economic
percentage. [AUTH, Articles 3(1)(o) and 10][AUTH]

Interest's financial-institution definition concerns a bank or an
enterprise substantially deriving profits from raising debt finance or
taking interest-bearing deposits and using those funds to provide finance.
A related group treasury company or a lender's name does not establish
that exception. Its back-to-back limitation is distinct from the
government/central-bank branch. [AUTH, Article 11(3)-(4)][AUTH]

For interest and royalties, test the payer-residence source rule and the
exception where the debt/liability is connected with and borne by a PE.
For dividends, interest and royalties, apply each article's actual
effectively-connected-PE exception rather than retaining a gross ceiling
for a PE-attributable item. Special relationships can limit the interest
or royalty article to the amount expected without that relationship;
the excess needs its own domestic and treaty analysis. [AUTH, Articles
10(5), 11(6)-(8) and 12(4)-(6)][AUTH]

Treaty royalties cover the specified IP rights, know-how, ancillary
assistance, broadcasting/reproduction rights and forbearance. The domestic
definition's equipment limb is not itself in treaty Article 12(3). Do not
classify every software, service or equipment invoice from its label.
Agreements Act **17A(4)-(5)** separately excludes the specified royalties
from section 128B, including a domestic royalty paid to an agreement
resident where the agreement does not treat it as a royalty. That can
change classification and liability rather than merely reduce 30% to 5%.
Actual contracts, mixed rights and other assessment taxes remain separate.
[AUTH, Article 12][AUTH]; [AGREEMENTS, section 17A][AGREEMENTS];
[RESIDENCE, section 6 royalty definition][RESIDENCE]

For an Australian payment, coordinate with `nf-investment-withholding`:

1. Establish the domestic liability and any exemption before a percentage.
   Ordinary domestic dividend, interest and royalty rates are **30%, 10%
   and 30%** respectively; these do not establish chargeability. [RATES]
2. Apply the complete treaty branch. Agreements Act section **17A(1)**
   limits qualifying dividend/royalty withholding liability; interest
   and its exemption need their applicable liability/treaty provisions.
   [AGREEMENTS]; [AUTH, Articles 10-12][AUTH]
3. Test payer/intermediary and payment/credit triggers separately. Apply
   the actual collection branch and regulation **26** rounding. Schedule
   1 section **12-300** requires no Subdivision 12-F withholding where
   no withholding tax is payable and limits further withholding to that
   tax less amounts already withheld **from the same payment under that
   Subdivision**. Do not net unrelated taxes or payments. [ADMIN]; [REGS]
4. Establish registration, remittance, report, payment-summary and any
   refund/variation procedure under current sources. Treaty entitlement
   does not itself complete those processes. UK collection procedures
   need their own current authority; the Australian procedure cannot be
   copied to a UK payer. Hold actual forms, schemas and submissions here.

## PE, attribution and corresponding relief

Article **5** starts with a fixed place of business and adds specific
branches. Its **more-than-12-month** rules for construction/installation
and connected supervision/consultancy and substantial equipment do not
turn every fixed place or dependent-agent case into a 12-month test.
Preserve paragraph 4's aggregation of connected construction/project
activities of associated enterprises and its concurrent-period treatment,
the manufacturing/processing branch, actual agent authority, independent
agents and the matched anti-fragmentation rule. Control of a subsidiary
alone is insufficient. This is a screening reference, not a completed
PE opinion. [AUTH, Article 5][AUTH]; [SYNTH, Article 5 MLI box][SYNTH]

Article **7** generally permits source taxation of an enterprise's profits
only through the treaty PE and to the extent attributable to it, with
separate-enterprise, deduction and specific-income-article rules. Apply
this treaty's actual text; an OECD model revision is not an automatic
replacement. Keep PE profit attribution under **R-CB-S2** specialist
escalation. Article **9** associated-enterprise adjustments and its
corresponding adjustment are separate tests. Agreements Act section **24**
also has its own Commissioner-satisfaction condition. A foreign adjustment
does not automatically generate an equal refund or credit. [AUTH,
Articles 7 and 9][AUTH]; [AGREEMENTS, section 24][AGREEMENTS]

## Credits, limitations and dispute clocks

Article **22** coordinates credits subject to the applicable domestic
rules and treaty-compliant tax. Its corporate underlying-tax branches
have specific conditions; do not credit all foreign group taxes or
disregard an applicable domestic exemption. Use `nf-foreign-income` for
selected Australian inclusion, eligibility, translation, limits,
non-refundable use and amendment rules. UK domestic credit computations
and complete corporate relief remain held pending their own sources.
[AUTH, Article 22][AUTH]; [FITO-LAW]; [FITO-WHEN]; [FITO-LIMIT]

In particular, Division **770** distinguishes eligible tax from assessed,
withheld or paid tax. Tax must be correctly imposed under foreign law
and the treaty, matched to the relevant included income and actually or
validly deemed paid. Refund entitlement or the specified tax-linked
benefit can make it not paid to that extent under section **770-140**;
do not wait automatically for cash receipt. Treaty-excess foreign
withholding is a foreign-refund issue, not an automatic Australian credit.
[FITO-LAW, sections 770-10, 770-15 and 770-140][FITO-LAW]; [FITO-WHEN]

Article **23(1)** limits source-State relief in its actual remittance/
receipt-basis circumstances; paragraph **(2)** addresses income exempt
because the individual is a temporary resident under the other State's
law. Do not assume every Australian tax resident is a temporary resident,
or that all UK residents still use the old remittance basis. HMRC states
that the remittance basis ended on **6 April 2025**, with a conditional
**4-year FIG** claim regime for qualifying new residents following at
least **10 consecutive tax years** of non-UK residence. Eligibility,
claims, historical amounts and interaction with Article 23 need actual
current law and evidence; this guide does not decide that interaction
from the regime's name or guarantee source relief. [AUTH, Article 23][AUTH];
[FIG]; `nf-foreign-income`.

The modified Article **26** permits presentation to either competent
authority **within 3 years from first notification** of the action causing
taxation not in accordance with the convention. It is not 3 years from
return lodgment, audit completion or discovery by an adviser. Preserve
the effect/saved-case rule above and the implementation provision
notwithstanding domestic time limits. Do not infer that MAP suspends
objection, appeal, payment or collection deadlines, guarantees agreement
or revives an already ineligible case. Verify current competent-authority
intake requirements and the actual first notification. [ATO-SYNTH,
Article 26][ATO-SYNTH]; [MLI, Articles 16 and 35(4)][MLI]

The ATO text records an arbitration memorandum signed on **21 May 2021**.
The complete MLI Part VI, reservations, memorandum, acceptance, exclusions
and actual procedure are outside the verified computation scope here.
Do not promise automatic arbitration or a fixed result or completion date.
Domestic amendment/refund and dispute remedies require their own clocks;
use `nf-tax-amendments-objections` only within its verified scope.
[ATO-SYNTH, introduction and Article 26 notes][ATO-SYNTH]

## Intake, defaults and reviewer attention

Add these to the combined profile confirmation before computation:

- Taxpayer/entity, both domestic residence analyses, relevant treaty
  residence resolution and dates; distinguish beneficial owner and agent.
- Gross payment components, currency, source, debt/rights, declaration,
  payment/credit dates, payer/intermediary and any connected PE.
- Voting power, direct/indirect ownership, holding history, recognised
  listing and regular trading, or competent-authority determination.
- Transparency and income attribution, lender business and independence,
  funding chain, related-party terms and commercial purposes.
- Covered taxes and years, domestic exemption, Article 23 conditions,
  foreign tax paid/refundable, first disputed-action notification and
  required procedures. Record reviewer-held evidence readiness only.

| Ambiguity | Authorised treatment |
|---|---|
| Residence, beneficial ownership, source, classification or other required eligibility unknown | **Needs Input**; no factual default is authorised. Do not assume 0%, 15%, 30% or denial merely to produce a number. |
| Operative instrument, amendment, rate or procedure unresolved | Hold affected work and the complete package. A reviewer flag cannot establish law. |
| Actual facts support a known domestic treatment but relief is not yet established | Record the supported domestic position and the unresolved relief condition separately; the missing relief evidence does not prove every domestic liability element. |
| A hypothetical explicitly stipulates all conditions | Compute only the labelled component; it supplies no default for a real case. |

No monetary threshold clears a treaty condition. Flag **every** disputed
entitlement, non-individual dual residence, transparent-entity allocation,
PE/attribution issue, related-party excess, purpose issue, Article 23
interaction, foreign-tax refund and deadline uncertainty for the reviewer,
irrespective of cash magnitude. Quantify only established alternatives;
otherwise state the unknown impact. Add the reviewer's confirmed engagement
materiality threshold for routine reconciliations without suppressing these
mandatory flags. This is an attention policy, not a statutory threshold.

## Topical refusals and specialist holds

Retain the universal, cross-border and applicable domain catalogues and
their exact messages. Add these topical refusals to the refusal trace:

| Code | Trigger | Verbatim output |
|---|---|---|
| R-NFUK-INSTRUMENT | Requested computation relies on a different treaty partner, tax, territory or period without its required content/authority | "This Norfolk Island guide covers selected Australia-UK treaty provisions only. I cannot calculate the requested treaty result without the applicable instrument, period and country content." |
| R-NFUK-ENTITLEMENT | Asked to calculate or clear a treaty outcome despite unresolved mandatory residence, ownership, classification, source, PE or anti-abuse conditions | "The required treaty conditions are unresolved. I cannot clear the affected financial result or complete the output package until the missing authority and evidence are established." |
| R-NFUK-PROCEDURE | Asked to submit a return, relief/refund claim, MAP case or arbitration request using this reference, or to guarantee its outcome | "This reference does not provide a complete submission or a guaranteed relief outcome. The qualified reviewer must verify the actual procedure, documents and deadlines before acting." |

Missing facts ordinarily remain Needs Input. Apply the matching refusal
when its trigger arises; do not invent a new code. PE attribution retains
R-CB-S2 and unresolved residence/instrument disputes retain R-CB-S4. Treaty
shopping, evasion and other loaded hard refusals are not cleared by the
examples below. Private identifiers, original ownership records and
authentication stay with the reviewer; obtain no real client or bank data.

## Fictional 2026-27 components and boundary cases

All amounts are **Australian dollars**, with no currency conversion or
contractual gross-up. The monetary cases stipulate established domestic
liability, treaty residence, beneficial ownership, character, source, no
connected-PE or special-relationship exception, cleared Article 23 and
purpose conditions, and no lower domestic exemption except as stated.
For source ceilings, cash remaining is illustrative **if** the separately
established charge/collection equals that ceiling. These are components,
not actual withholding statements, returns, credit claims or refunds.

| Case and complete additional assumptions | Reproducible component |
|---|---|
| A$100,000 taxable unfranked dividend to a UK resident company with exactly 10% direct voting power; zero branch fails | Article 10(2)(a): A$100,000 × 5% = **A$5,000 ceiling**. At that charge, cash remaining is **A$95,000**. An assumed 365-day condition cannot displace this pair's branch. |
| A$10,000 taxable unfranked dividend beneficially owned by a UK resident individual | Article 10(2)(b): A$10,000 × 15% = **A$1,500 ceiling**; cash at that charge **A$8,500**. The corporate 10% holding branch cannot be selected for the individual. |
| A$1,000,000 dividend to a UK resident company with exactly 80% voting power for the full 12-month period ending on declaration; all Article 10(3)(a) recognised-listing/regular-trading requirements satisfied | Article 10(3): A$1,000,000 × 0% = **A$0 source-State tax**; cash **A$1,000,000** under the stipulated collection assumptions. With only 6 months' holding and all ordinary Article 10(2)(a) conditions instead met, the alternative ceiling is **A$50,000**, a difference of **A$50,000**. |
| A$20,000 ordinary interest to a UK resident beneficial owner, with no Article 11(3) exception | A$20,000 × 10% = **A$2,000 ceiling**; cash at that charge **A$18,000**. A fully qualifying unrelated, independent financial institution instead has **A$0** source tax; the stipulated Article 11(4) back-to-back exception restores a **A$2,000** ceiling. |
| A$8,000 payment entirely within Article 12's royalty definition to its qualifying UK resident beneficial owner | A$8,000 × 5% = **A$400 ceiling**; cash at that charge **A$7,600**. Actual software/equipment rights being unknown would hold this classification, not select 5%. |
| A$10,000 UK-source interest; the correct treaty-compliant UK tax is established as A$1,000, but A$2,500 was withheld and the A$1,500 excess is refundable | Only **A$1,000** can proceed to the Australian eligible-tax and limit tests; **A$1,500** is a separate foreign-refund matter. No assumed A$2,500 FITO or guaranteed refund. These stipulated figures are not a UK domestic rate table. |
| Transparent entity receives A$100,000; UK tax law treats A$60,000, and only that amount, as income of a UK resident | The transparent-entity resident-income gate covers **A$60,000**, not all A$100,000 from an ownership label. A **A$40,000** remainder needs its own taxpayer and entitlement analysis; no rate is selected. |
| Individual domestically resident in both States, no permanent home in either, centre of vital interests established in Australia | Article 4(3)(a) resolves treaty residence to Australia. Do not skip to nationality or insert habitual abode. A different domestic liability or Article 23 question still needs its own test. |
| Ordinary dual-resident company has Australian effective management but no competent-authority agreement; dual-listed exception does not apply | No treaty tax relief/exemption under the modified Article 4(4). The former automatic effective-management result is unavailable. Domestic taxation and further procedure require their own analysis. |
| Fixed business place used for 4 months | Duration alone does not clear PE. Test the actual fixed-place facts and applicable exceptions; do not apply a universal 12-month safe harbour. Attribution remains specialist work. |
| First notification precedes final audit completion by a year | Identify the actual first notification and 3-year MAP clock. Waiting until audit completion does not restart it; do not infer a domestic deadline extension. |
| UK FIG relief is claimed, or a visa is shown without Australian temporary-resident conditions | Hold the actual Article 23 and domestic interaction. A regime name, visa or guide date does not establish a source-tax exemption. |

## Output extension and working paper specification

For a completed engagement, preserve the universal **Excel working paper,
reviewer brief, action list and review checklist**, the applicable domain
outputs and all 5 cross-border map components: obligation matrix,
double-tax relief schedule, unified calendar, risk/hold register and
cross-border reviewer brief. Shared files must keep each component
identifiable. This reference does not supply an actual workbook, approved
filing schema or ready-to-submit package.

Add a **Treaty gates** sheet with a stable redacted item ID, taxpayer and
beneficial owner, domestic/treaty residence and period, tax and income
article, territorial provision, MLI matching/effect evidence, each
eligibility result, purpose/Article 23 result, domestic liability, gross
component, currency translation, ceiling, actual collection and difference.
Keep the universal transaction fields mapped, including classifications,
citations, exclusions, defaults and reviewer flags. Every input item must
appear exactly once; a gate sheet is supporting evidence, not a second
income booking.

Use formulas for amounts and summaries, retain source-labelled hardcoded
inputs and cross-sheet references, and run the base's required successful
recalculation and error checks. Unknowns are explicit holds, not zeroes.
The relief schedule must distinguish eligible tax, treaty excess, domestic
credit limit/use, refund route and unresolved corporate/UK relief. Add
first-notification evidence and distinct MAP, domestic dispute, remittance
and reporting dates to the sourced calendar. Do not invent form boxes or
dates to populate it. Hold the complete package if a required source,
schema, confirmation, procedure or recalculation condition is unmet.

Extend the reviewer brief with each accepted/rejected/held gate, operative
instrument versions, effect dates, domestic versus treaty treatment,
benefit/purpose evidence, computation trail and the exact missing action.
Address it to the credentialed reviewer and reconcile every figure with
the workbook and chat. The examples are not a substitute for that work.

## Review Checklist Items

Run all universal, cross-border and applicable domain checks, then verify:

1. Every person, entity, relevant territory, tax, event and period is accounted for.
2. Domestic residence, treaty residence and covered-person conditions are distinct.
3. The individual tie-breaker has no imported habitual-abode step; entity MAP and dual-listed rules remain separate.
4. Transparent income is supported by actual tax treatment, not an ownership assumption.
5. Authentic instruments, both final positions and applicable later changes support each claimed modification and effect date.
6. No UK MLI Article 8 holding period, unilateral Option A or reserved Article 12 rule was imported.
7. Voting power, direct holding, principal-class, exchange, trading and 12-month conditions match the selected dividend branch.
8. Beneficial ownership, source, actual debt/rights, independent-lender conditions, back-to-back arrangements and PE exceptions were checked.
9. Interest/royalty related-party excess, Article 23, the saving clause and the principal purpose test were considered separately.
10. Domestic liability, treaty ceiling, collection, rounding, prior withholding and reporting are independently supported.
11. No fixed-place PE was cleared by a generic 12-month test; attribution and corresponding relief retain their own conditions and escalation.
12. Eligible foreign tax excludes treaty excess and qualifying refundable amounts; income matching, currency, years and domestic limits reconcile.
13. First notification, effect/saved-case rules and each domestic deadline are evidenced; no automatic suspension or arbitration outcome was promised.
14. All monetary components recompute, rows reconcile and every applicable output and successful recalculation is present before delivery.
15. Mandatory unknowns stay held, no unpermitted default was used and every loaded refusal has its required trace and exact message where fired.
16. All flags, source gaps and professional decisions appear in the brief, action list and review checklist, with private records retained by the reviewer.

## Currency, validation and remaining coverage

Version **0.1**, checked **21 October 2026**: initial selected UK treaty
companion. Primary instruments, selected matching positions and current
Australian source chains were checked; the worked components are
fictional. Repository validation and arithmetic checks assess file and
instruction integrity. They do not establish real beneficial ownership,
residence, PE, purpose, entitlement or professional sign-off.

Employment, pensions, students, entertainers, offshore resources, gains,
inheritance, trusts, full company/transparent-entity regimes, all UK
domestic computations, actual credit/refund procedures and complete MAP/
arbitration remain outside this selected treatment. Other treaty partners
need their own instruments and evidence. No live model execution,
practitioner review, actual engagement package or comprehensive-country
acceptance is claimed. Keep all open Norfolk topic and country slots open
until their own sources, mandatory contract slots and reviews pass.

## Primary source library

The references below support the identified provisions, not a claim that
every page or every treaty article was reviewed. Recheck the live source
records and any later amendment or notification for actual work.

[REGISTER]: https://treasury.gov.au/tax-treaties/income-tax-treaties
[AUTH]: https://www.legislation.gov.uk/uksi/2003/3199/schedule/made
[SYNTH]: https://www.gov.uk/government/publications/australia-tax-treaties/synthesised-text-of-the-multilateral-instrument-and-the-2003-australia-uk-double-taxation-convention-in-force
[ATO-SYNTH]: https://www.ato.gov.au/law/view/document?DocID=MLI%2FMLI-UK-agreement
[MLI]: https://www.legislation.gov.uk/uksi/2018/630/pdfs/uksi_20180630_en.pdf
[AU-POS]: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/beps-mli/beps-mli-position-australia-instrument-deposit.pdf
[UK-POS]: https://assets.publishing.service.gov.uk/media/5b4860ac40f0b6633c0c96b4/Final_list_of_UK_reservations_and_notifications_made_on_deposit_of_the_instrument_of_ratification.pdf
[OECD]: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/beps-mli/beps-mli-signatories-and-parties.pdf
[AGREEMENTS]: https://www.legislation.gov.au/C1953A00082/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[RESIDENCE]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[TR]: https://www.ato.gov.au/law/view/document?DocID=TXR%2FTR20231%2FNAT%2FATO%2F00001
[SRT]: https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3
[ADMIN]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[REGS]: https://www.legislation.gov.au/F2017L01227/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[RATES]: https://www.legislation.gov.au/C2004A00086/2007-09-24/2007-09-24/text/original/epub/OEBPS/document_1/document_1.html
[FITO-LAW]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_9/document_9.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[FITO-WHEN]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/when-a-fito-applies
[FITO-LIMIT]: https://www.ato.gov.au/forms-and-instructions/foreign-income-tax-offset-rules-guide-2026/calculate-your-fito-or-offset-limit
[FIG]: https://www.gov.uk/government/publications/foreign-income-and-gains-fig-regime-self-assessment-helpsheet-hs266/hs266-foreign-income-and-gains-fig-regime-2026

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
