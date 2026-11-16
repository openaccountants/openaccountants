---
name: dtt-template
description: >
  Reusable research and authoring template for bilateral Double Tax Treaty
  summaries. Trigger on "DTT template", "treaty corridor template", "create new
  DTT skill" or "add new treaty corridor". No placeholder is a tax rule or rate.
  Copy into a distinct corridor path, replace every placeholder with sourced
  findings, and apply the tax-skill standard before using the resulting summary.
jurisdiction: GLOBAL
tax_year: 2026
tax_year_notes: "2026 authoring workflow; no bilateral treaty or taxpayer period cleared by this template"
last_updated: 2026-11-16
version: 0.2
depends_on: []
tier: 2
category: cross-border
domain: tax
type: router
---

# [Country A] ↔ [Country B] Double Tax Treaty (DTT) summary template

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this skill to prepare a new bilateral treaty research file. It remains discoverable
in the treaty-corridors directory for template-creation workflows; it is not a completed
corridor summary. The template supplies an intake, a topic inventory and a publication
gate. It supplies no bilateral tax entitlement, rate, filing deadline or computation.

Copy it to the actual corridor, for example
`skills/global/cross-border/treaty-corridors/eg-sa/dtt-summary.md`. Set a distinct name,
description and jurisdiction pair, actual period, update date and numeric version.
Choose the resulting skill's shape for its real job. A populated tax summary must meet
the applicable tax-skill headings, sources and recomputing-example requirements;
retaining this template's `router` label cannot excuse missing calculations.

## Ask the client first

- Which source and residence jurisdictions, covered territory and tax are involved?
- Who is the recipient, payer and beneficial owner, where relevant? Obtain entity or
  individual status, residence evidence, fiscal transparency and ownership facts.
- What is the payment or gain, its gross/net currency amount, contract and relevant
  payment, credit, transaction and tax-period dates? Identify any gross-up provision.
- Which domestic liability, exemption, source rule, permanent establishment (PE),
  fixed base or other connection needs treaty analysis? Obtain the relevant facts.
- Is relief sought at source, by refund, in the residence return or through a dispute
  process? What documents, prior filings, notifications and decisions already exist?

Do not ask again for facts already evidenced in the file. Record genuinely missing
inputs and the conclusions they prevent. Leave the outcome conditional until resolved.

## The method, step by step

### Establish the actual instruments and dates

Retrieve the official bilateral text, protocols and any replacement or termination
instrument. Record authentic languages, signature, entry into force and effective
application separately, for each relevant tax and direction. Inspect taxes/persons
covered, territorial definitions and saving, transition and termination provisions.
Keep an official source URL and pinpoint beside every populated finding. Do not treat
the agreement's title or signing announcement as proof of an effective benefit.

For possible BEPS MLI modifications, check both parties' coverage, positions,
reservations, choices, notifications and applicable effect dates. Signature alone is
insufficient; dates may differ by tax and direction. Use the [OECD step-by-step tool](https://www.oecd.org/tax/treaties/step-by-step-tool-on-the-application-of-the-MLI.pdf)
with the [MLI text](https://legalinstruments.oecd.org/public/doc/358/body-text.en.html),
including Articles 2, 28 and 34–35. Resolve compatibility and subsequent changes.
The [matching database](https://www.oecd.org/en/data/tools/beps-mli-matching-database.html)
helps locate the pair's positions; no pair was tested for this template.

Populate this identification sheet, replacing the bracketed prompts:

| Field | Required entry and evidence |
|---|---|
| Treaty name | [Exact official agreement title and official text URL] |
| Signed | [Signature date; signing source] |
| In force | [Entry-into-force date; official notification] |
| Effective application | [Tax, direction and relevant payment/period trigger; article and dates] |
| Current version | [Original, each effective protocol, replacement, termination and transition] |
| MLI status | [Each party's status; pair coverage, operative matches and effective dates] |
| Jurisdictions covered | [Country A and Country B codes; treaty territorial scope] |
| Last verified | [Actual date sources were opened and operative text read] |
| Key note | [Most material evidenced feature and its conditions] |

### Populate the income and withholding register

For each row record: domestic charge/exemption and official source; treaty provision
and official source; taxpayer, income and beneficial-ownership conditions where
applicable; amount/base/cap; holding and timing requirements; PE/fixed-base connection;
anti-abuse eligibility; collection/refund procedure. Distinguish a gross withholding
cap from net-basis assessment, exclusive allocation, credit or exemption. Do not turn
permission to tax a gain into an invented withholding percentage. Leave an absent
article marked absent and analyse the relevant alternative rather than inventing it.

| Income category to investigate | Required treaty-specific distinctions |
|---|---|
| Portfolio dividends | [Rate or allocation, recipient and beneficial-owner conditions] |
| Substantial-holding dividends | [Holding percentage/type, holding period, qualifying recipient and rate] |
| Interest | [Definition, caps, government or other exemptions, excess/connected interest] |
| Royalties | [Definition and category splits, cap and exemptions; whether technical assistance is included] |
| Technical services | [Separate provision if present; otherwise evidenced classification and allocation] |
| Immovable-property capital gains | [Taxing rights, property definition and domestic assessment] |
| Share capital gains | [Property-rich/substantial holdings or other distinctions and relevant testing period] |
| Pensions | [Private/public or other categories; allocation, conditions and collection] |
| Directors' fees | [Covered recipient/capacity, allocation and domestic collection] |

This is an empty research register, not a rate table. Insert only actual verified
figures with tax year, complete conditions and official URL per numeric row. Keep
domestic and treaty findings separate; do not select a rate until eligibility and
procedure have been established. Gross-up calculations require the actual contract.

### Complete the article-by-article inventory

The labels below preserve the original template's topic prompts. They are navigation
labels, not an assertion that a particular treaty uses these article numbers or rules.
Replace them with the actual numbering. Record absent provisions and cross-references.
For each topic, set out the complete conditions, exceptions and result for each state.

| Original topic label | Research entry required from the actual instruments |
|---|---|
| Article 4: resident and tie-breakers | [Definition, exclusions and relief eligibility; individual permanent home, centre of vital interests, habitual abode, nationality and mutual-agreement tests only where applicable; separate non-individual rule] |
| Article 5: permanent establishment | [Fixed-place and exclusions, construction/installation and service tests if present, agent/independent-agent rules, related-party/anti-fragmentation and contract-splitting modifications] |
| Article 6: immovable-property income | [Property, situs, permitted taxing rights, income covered and exceptions] |
| Article 7: business profits | [Allocation, PE dependence where relevant, attribution and exceptions/cross-references] |
| Article 8: shipping and air transport | [Activities and international-traffic definition, allocation criterion and exceptions; do not prefill effective management] |
| Article 9: associated enterprises | [Arm's-length adjustment, corresponding relief and applicable procedural limits] |
| Article 10: dividends | [All rates, shareholding/holding-period tests, beneficial ownership and government/other exemptions] |
| Article 11: interest | [Definition, rates, exemptions, connected payments and special relationships] |
| Article 12: royalties | [Definitions, category rates, technical-assistance treatment and exemptions if present] |
| Article 13: capital gains | [Immovable property, PE assets, ships/aircraft, relevant shares and residual property, including exceptions] |
| Article 14: independent personal services | [Whether article exists; fixed-base/day tests, period and attribution if present; alternative article if absent] |
| Article 15: employment | [Workplace allocation and every exception condition, employer/remuneration-borne tests and period/day counting] |
| Article 16: directors' fees | [Company residence, recipient capacity, allocation and covered remuneration] |
| Article 17: artistes and sportspersons | [Personal activities, diverted income and public-funding/other exceptions] |
| Article 18: pensions | [Actual categories, allocation and exceptions] |
| Article 19: government service | [Salary versus pension, paying state, services/residence/nationality and business exceptions] |
| Article 20: students and trainees | [Eligible persons, visits, payment source, purpose, duration and exemptions] |
| Article 21: other income | [Residual scope, allocation, PE/fixed-base connection and any source-state rule] |
| Article 23: double-tax relief | [Credit/exemption method in each state, base/limits, progression, subject-to-tax or other conditions and domestic claim procedure] |

Read the rest of the actual treaty as well. This inventory is not permission to omit
other taxes, nondiscrimination, exchange of information, assistance, entitlement or
administrative/final provisions that affect the question. A model convention is a
research aid, not the selected bilateral instrument.

### Research residency certificates and collection procedures

Fill separate Country A and Country B entries for issuing authority, acceptable
format (original/electronic/copy), certificate period and facts certified, language,
translation, authentication or apostille/legalisation **if required**, submission
recipient, relief-at-source or pay-and-refund route, forms, deadlines and evidence.
Record how domestic rules and the treaty interact, plus official URLs/read dates.
Do not assume a certificate by itself establishes every condition of entitlement.

Retain an Egypt-specific research field only for a corridor involving Egypt:
verify the relevance, current status and actual conditions of Ministerial Decree
771/2009 and any later procedures before stating a pay-and-refund rule. Record any
claimed controversy with its authority and unresolved effect. Obtain the real
[Country B] procedure separately; do not copy Egypt's process into it.

### Research MAP, arbitration and anti-abuse

Complete a Country A / Country B matrix for competent authority, official contact
and submission channel, deadline and trigger, eligibility, required documents,
domestic-remedy interaction and arbitration availability/conditions. Keep the Egypt
contact prompt "Egyptian Tax Authority (ETA), Conflict Resolution Department,
Ministry of Finance" as **unconfirmed** until checked in the relevant current official
procedure. Likewise verify any proposed Ministry of Finance, ZATCA or MoF contact.

MLI Article 16 has compatibility and reservation rules; arbitration under Article 18
needs both parties' election and further conditions. Do not promise acceptance or a
successful agreement. For treaty shopping, obtain the actual PPT/LOB text and effective
application, including any MLI Article 7 modifications. Evaluate all conditions,
exceptions and available competent-authority relief; do not infer entitlement from
residence or a reduced rate alone. [MLI primary text](https://legalinstruments.oecd.org/public/doc/358/body-text.en.html).

### Link the domestic skills and hand off

Preserve the upstream slots `[countryA]-corporate-tax`, `[countryA]-withholding-tax`
and `[countryB]-corporate-tax`. Resolve each to an existing relevant skill and record
its actual scope/period; add a missing-coverage note if no matching skill exists.
Carry domestic CIT interaction, domestic withholding and treaty refund mechanics
into the handoff. A cross-reference does not independently validate its contents.

The resulting corridor file must include a source register, every old-topic
destination for a rewrite, calculations appropriate to its shape, unresolved items
and independent source review. Leave professional sign-off pending until actually
obtained. Check dates and version against main immediately before publication.

## Authoring route checks

These are qualitative authoring checks, with no invented tax amount or rate.

- **Blank rate slot:** the author has a portfolio-dividend placeholder and a real
  domestic rate but has not retrieved the bilateral text. Keep the treaty field
  unresolved, identify the missing authority and hand off for retrieval. Do not
  publish the domestic rate as the treaty cap or treat the placeholder as zero.
- **Both countries signed the MLI:** the proposed summary merely records signatures.
  Return to the instrument/date gate; obtain force, pair coverage, positions and
  effect evidence before using any claimed modification. Leave the bilateral
  analysis conditional; a signed instrument is not a completed matching analysis.

## When to refuse or refer

Stop an unsupported entitlement, rate selection, filing or payment instruction
when the applicable instrument, period, condition or procedure is unresolved. Keep
unaffected evidenced research, list the missing dependency and obtain source or
qualified professional review. Refer disputed residence, beneficial ownership,
PPT/LOB, PE attribution, competing authentic texts, refund eligibility and MAP or
arbitration strategy. Do not generate a residency certificate, invent a contact,
submit a claim or manufacture a review decision from this template.

## Sources

| Source | Read for | Read date and boundary |
|---|---|---|
| [OECD MLI official text](https://legalinstruments.oecd.org/public/doc/358/body-text.en.html) | Articles 1–2; 7(1)–(7); 16 including compatibility/reservations; 18; 28(1)–(3); 30; 34–36 including effect-date exceptions | 2026-11-16. General modification gates only; no bilateral match, current party position, rate or national procedure reviewed here. |
| [OECD applying the MLI step by step](https://www.oecd.org/tax/treaties/step-by-step-tool-on-the-application-of-the-MLI.pdf) | Both pages: force, covered agreement, reservations/choices, notifications/compatibility and effect, including exception warnings | 2026-11-16. Secretariat tool dated June 2017, used with the primary text and actual current positions when populating a corridor. |
| [OECD MLI matching database landing page](https://www.oecd.org/en/data/tools/beps-mli-matching-database.html) | About section: matching outcomes, positions and historical-data function; linked manual/database identified | 2026-11-16. Landing page read; no database match or manual asserted read. |

Not yet confirmed: every bracketed bilateral field and all actual treaty/domestic rates, periods, thresholds, entitlements, collection procedures and contacts remain unpopulated. The original template's 6-month construction prompt, 183-day independent/employment prompts, "typically 1 year" TRC validity and suggested 3-year MAP deadline are not established for an unspecified treaty; obtain the actual rule and all conditions instead. Its presumed effective-management shipping allocation, default individual/entity tie-breakers, technical-assistance royalty definition, capital-gains/pensions/government/student/other-income allocations and universal original-TRC/authentication requirements likewise are prompts requiring actual bilateral/national verification. Egypt Decree 771/2009, Egypt pay-and-refund/controversy and the named Egypt/other contact suggestions have not been researched for a real corridor here and are not usable instructions. Commercial summaries may help discovery but do not replace the missing official instruments. No claim that a particular OECD Model edition automatically applies to a bilateral treaty is made.
