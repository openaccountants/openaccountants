---
name: cross-border-tax-workflow-base
description: "2026 cross-border personal-tax working-paper method: residency-map intake, ordered plan, source trace, double-tax relief bridge, information-return checklist, unresolved-facts holds and accountant hand-off. Load with cross-border-tax-router and the relevant topic and country Guides; this method does not determine country residence, treaty entitlement or filing obligations. Includes a conditional UK foreign-tax-credit arithmetic example."
version: "1.1"
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-26
category: international
type: cross-country-method
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Cross-border tax workflow: the shared method for any case that touches more than one country v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope and who this is for

Tax year 2026. Produce an ordered working paper for cross-border personal tax, with a cited rule behind each proposed step and visible holds wherever facts or law remain unresolved. `cross-border-tax-router` selects the topic and country Guides; this base explains how to join them. Check each destination's scope, year and official sources before using it. A link alone does not establish that the destination settles the case.

Keep all relevant subjects: domestic residence, citizenship and green-card history, domicile where relevant, source of income and gains, treaty residence, relief by credit/exemption/exclusion, information returns and the order of events. Topic routes include `us-foreign-earned-income-2555`, `us-foreign-tax-credit-1116`, `us-fbar-fatca-reporting`, `us-gilti-fdii-beat`, `us-form-5471-cfc-information`, `us-foreign-trust-reporting` and `us-expatriation-exit-tax`. Country routes include `us-tax-residency`, `uk-statutory-residence-test`, `uk-non-dom`, `mt-non-dom`, `ie-non-dom`, `cy-non-dom` and `ca-tax-residency`. Preserve `leaving-australia-tax-residency-cgt` as an Australian routing destination only; this base supplies no Australian rule or figure.

The output remains an unreviewed working paper until the specific plan receives professional review. Do not file, elect, sell, distribute or change a person's status from this workflow. No country rate is set here; the UK case below demonstrates arithmetic under explicit assumptions, rather than determining the person's UK liability.

## Ask the client first

Read the available case record and documents before asking. Collect missing facts together:

- Residence claimed in each country, domestic-test evidence, dates of changes and each country's tax-year period.
- Homes available, family and economic ties, travel dates and day-count records.
- All citizenships and current or former US green-card status, separately from residence.
- Each income item, gain, asset, source-country connection and transaction date; tax withheld, assessed, paid or refundable.
- Foreign bank, brokerage and pension accounts; companies, trusts, partnerships and funds, with ownership and beneficiary details.
- Prior returns, treaty claims, residence certificates, elections and deadlines already approaching.

Record evidence and uncertainty alongside each answer. Do not treat a passport, a residence certificate or the client's residence description as the completed legal analysis.

## The method, step by step

1. **Build the residence map.** Examine each country's domestic residence question separately using its country Guide and official source. For the US, route green-card, substantial-presence, first-year election and dual-status questions to `us-tax-residency`; for the UK, use `uk-statutory-residence-test` for the relevant period. Record citizenship separately: US citizens and resident aliens are generally subject to US tax on worldwide income under the Internal Revenue Code, including when abroad ([IRS, opening worldwide-income statement](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)). This does not decide exceptions, treaty status, taxable amounts or filing duties.
2. **Identify the actual treaty question.** Where both countries may claim residence, obtain the operative treaty, protocols, scope, effective dates and residence definition before considering a tie-breaker. For the UK–US convention, use Article 4 as the reading route, including its definition/scope provisions before any permanent-home, centre-of-vital-interests, habitual-abode, nationality or competent-authority question. Do not apply that hierarchy to another treaty by analogy. The residence outcome, US income-tax versus other-purpose status, and Forms 1040-NR/8833 application need case-specific review: **Check this point with one of our partner accountants.**
3. **Map each income or gain.** Record its character, owner, dates, location and source connections; then investigate each country's domestic and treaty treatment. For UK foreign income/gains, keep separate questions for ordinary investments, immovable property and business assets; do not infer an exemption or dual liability simply from the asset's location. Obtain the country rule and any relevant treaty article. If that treatment is unresolved, mark it **undetermined — do not use** and **Check this point with one of our partner accountants.**
4. **Build the relief bridge.** Investigate credit, deduction, exemption, exclusion, re-sourcing and source-country refunds without promising that all double tax disappears. Use `us-foreign-tax-credit-1116` alongside `us-foreign-earned-income-2555` when comparing US credit and exclusion. The IRS states that a foreign tax credit cannot be taken for taxes on income excluded under the foreign-earned-income or foreign-housing elections; claiming that credit may cause one or both elections to be considered revoked ([IRS, foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit)). Other eligibility, credit limitations and elections come from those Guides and their sources. For the UK, Foreign Tax Credit Relief is usually claimed through the tax return; the agreement may limit it or require a source-country refund instead ([GOV.UK, if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)). Check entitlement and foreign-tax minimisation before applying the worked-case arithmetic.
5. **Read the saving clause and exceptions.** For a proposed US treaty benefit, identify the relevant treaty's saving clause, its scope and every potentially applicable exception. For the UK–US convention, Articles 1(4)–(5) are the reading route and Article 24 is the relief/re-sourcing research route. These references do not establish entitlement or eliminate citizenship taxation. The actual benefit and its interaction with residence and citizenship are referred: **Check this point with one of our partner accountants.**
6. **Build the forms checklist.** For each country, research both income-tax and information returns, claims, elections, residence certifications, disclosure exceptions, deadlines and signatures. Do not assume every relief requires a separate form or that a form alone earns relief. For a possible US dual-resident treaty position, investigate Forms 1040-NR/8833 through `us-tax-residency`. For foreign accounts, investigate FinCEN Form 114 and Form 8938 through `us-fbar-fatca-reporting`, including accounts with no taxable income. For trusts use `us-foreign-trust-reporting` for Forms 3520/3520-A; for companies use `us-form-5471-cfc-information`. Preserve foreign-partnership/Form 8865 and foreign-fund/PFIC/Form 8621 questions from the workflow's original reporting checklist; these are research prompts, not findings that filing is required. For unresolved partnership/fund filing and late or missed returns: **Check this point with one of our partner accountants.**
7. **Order the events and dependencies.** Analyse proposed residence changes before assessing a sale, entity/trust character before a distribution, and possible expatriation before a later sale. Keep the Canadian departure/deemed-disposition question in `ca-tax-residency`, and a green-card treaty position together with `us-expatriation-exit-tax`: research long-term-resident status and section 877A rather than inferring no exposure from a residence tie-breaker. Record actual event dates and possible intervening filings. For departure-tax or expatriation application: **Check this point with one of our partner accountants.** Do not recommend changing the order until both countries' consequences are established.
8. **Hand off the paper.** Send the situation map, evidence trace, ordered plan, computations and unresolved items to the engaged accountant for review before action. Follow the hand-off policy below; do not claim an engagement or completed review from a tool call or Guide label.

### The sequenced-plan output contract

Produce both layers for every topic engaged:

**Layer A: Reference layer.** State the applicable rule with the official statute, form instructions or treaty article, its conditions, effective period and exact source passage. Sections 911 and 877A and Form 3520 are examples of identifiers to locate, not universal rules. Where a source or operative condition is missing, keep the question visible and withhold the legal conclusion.

**Layer B: Sequenced plan.** Each step records the event and date; which country may tax it and on what proven basis; any established relief and residual tax; the applicable forms and deadlines; and why this step depends on earlier steps. Link every conclusion to Layer A. Distinguish a confirmed requirement from a question still being researched. A pending dependency blocks the affected recommendation while allowing independent steps to continue.

### The double-tax relief and treaty-bridge convention

For each item potentially taxed by more than one country, record:

- Each country's claimed taxing basis and any established treaty allocation; do not force every case into one exclusive primary right.
- Relief considered and its eligibility, limits, timing and evidence: credit, deduction, exemption/exclusion, reduced withholding, re-sourcing or residence question.
- The actual return entry, separate claim or disclosure if required, with the official procedure; research Form 1116, Form 2555, Form 8833 and UK Self Assessment only where relevant.
- Foreign tax withheld versus finally payable, available source-country refunds, relief used and residual exposure. Keep state-tax treatment as a separate question; do not assume a treaty binds a US state.

A UK claim cannot simply credit all withholding. TIOPA 2010 section 33 limits credit to what would remain after reasonable steps to minimise foreign tax under domestic law and the treaty; section 36 limits income-tax credit by reference to the income from the particular source ([section 33](https://www.legislation.gov.uk/ukpga/2010/8/section/33), [section 36](https://www.legislation.gov.uk/ukpga/2010/8/section/36)). Use the applicable computation rather than treating gross withholding as automatically creditable. Without a treaty, investigate unilateral relief instead of assuming relief is impossible or guaranteed.

### AUDIT FLASH POINT convention

Use **AUDIT FLASH POINT** for a material contested judgement identified from the facts and evidence. Explain the judgement, the contrary view, the supporting evidence and any disclosure under consideration. The marker is a review flag, not evidence that an authority commonly challenges every listed subject or that a disclosure removes risk.

Review prompts include residence cessation/day counts; treaty residence; grantor/non-grantor trust character; exclusion versus credit and exclusion eligibility; covered-expatriate status/valuations; foreign funds; reasonable cause for late returns; and facts the preparer cannot verify in another country. Actual unresolved treatment remains referred. Include each material flag in the reviewer brief.

### Conservative-default principle (cross-border edition)

The default is an explicit hold. If a missing fact changes tax, relief, characterisation or filing, label that issue **undetermined — do not use**, identify the missing evidence and its dependent steps, and preserve the applicable deadline for urgent review. Do not assume broader taxing rights, a higher-tax characterisation or a filing obligation. Do not file a return merely as a precaution without establishing its requirements.

A hypothetical scenario may help explain a dependency if its assumptions and non-usable status are explicit. It must not become the person's recommended position. Favourable treatment, adverse treatment, a treaty election and non-filing all need their legal conditions established; an instruction or signature cannot replace those conditions.

### Structured intake (the residency map)

Restate only unresolved facts after searching the available record. Group them by the decision they unlock:

~~~
Facts still needed for this working paper:
  1. [Fact/evidence], used in [step / rule]
  2. [Fact/evidence], used in [step / rule]
If [fact] is unavailable, [affected issue] remains undetermined — do not use.
[Independent step] can continue; [dependent recommendation] is held.
~~~

### Universal self-checks and output specification

Deliver the following in order, and check the evidence behind each part:

1. **Situation map:** citizenship/green-card history, residence question in each country, relevant domicile, dates and events; facts separated from conclusions.
2. **Sequenced plan:** both layers, cited dependencies and justified order; source and character considered for each income/gain, without independent country answers that contradict one another.
3. **Reference trace:** applicable-year rule/form/article, exact official source passage and conditions behind every conclusion and figure.
4. **Double-tax bridge:** per item, established taxing rights, relief mechanism, claim procedure and residual; treaty/saving-clause application held if unresolved.
5. **Information-return checklist:** every relevant form investigated, with confirmed tests/deadlines/penalties traced to topic sources; unresolved foreign partnership/fund duties visible.
6. **Reviewer brief:** judgements, every AUDIT FLASH POINT, holds, evidence gaps and uncovered-country/treaty/estate questions. No missing-fact assumption presented as fact.
7. **Hand-off:** label the output an unreviewed working paper and obtain the relevant professional review before action.

### Review status and the mandatory hand-off

This workflow itself supplies no professional approval of a person's plan. Preserve any genuine review of a specific paper and its scope accurately. Choose the lead accountant by the case's established exposure and the countries involved, documenting the choice rather than assuming citizenship or residence determines it alone. Give that accountant the full situation map and sequenced plan, with review in other relevant countries where needed.

Tell the person plainly: this is a working paper pending review, not an engagement or filed return. Review is required before selling, distributing, giving up residence, citizenship or a green card, making an election or filing from this plan. Do not assert that an accountant has signed or will file unless that engagement and review actually exist. If an authorised review tool is available, its receipt is a request record, not completed review. Missing facts require prompt escalation, not automatic filing.

## Worked cases

Hypothetical 2026 facts, not a real client. A UK-resident individual receives a foreign-company dividend with GBP 1,500 withheld. Preserve the supplied GBP 1,000 UK tax on that same dividend as an input from the UK computation, not a rate calculated here. Assume the dividend remains taxable in the UK (no exemption/FIG claim), all GBP 1,500 is qualifying foreign tax after reasonable minimisation and treaty limits, the UK credit limit for that source is GBP 1,000, and no other limit reduces the claim. Credit is conditional on entitlement under the applicable arrangements: [TIOPA section 18](https://www.legislation.gov.uk/ukpga/2010/8/section/18). The minimisation and source-income limits are [sections 33](https://www.legislation.gov.uk/ukpga/2010/8/section/33) and [36](https://www.legislation.gov.uk/ukpga/2010/8/section/36); [HMRC INTM161210](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161210) states the general lesser-of limit.

Under those assumptions, min(1,500, 1,000) = GBP 1,000 credit, leaving GBP 500 foreign tax unrelieved by this UK credit and GBP 0 UK tax still due on the item. GOV.UK says the claim is usually made on the tax return, and it is unavailable where the agreement requires a source-country refund instead ([GOV.UK](https://www.gov.uk/tax-foreign-income/taxed-twice)). The GBP 500 is not a promised refund or a final statement about another relief. For actual dividend eligibility, reduced treaty withholding or a source-country reclaim: **Check this point with one of our partner accountants.** If the assumed foreign tax or UK limit changes, recompute before using the result.

```oa-check
name: UK Foreign Tax Credit Relief capped at the UK tax on the same income (hypothetical amounts)
inputs:
  foreign_tax_withheld: 1500
  uk_tax_on_same_income: 1000
steps:
  - uk_relief: min(foreign_tax_withheld, uk_tax_on_same_income)
  - foreign_tax_not_relieved_in_uk: foreign_tax_withheld - uk_relief
  - uk_tax_still_due_on_item: uk_tax_on_same_income - uk_relief
expected:
  uk_relief: 1000
  foreign_tax_not_relieved_in_uk: 500
  uk_tax_still_due_on_item: 0
```

For a US citizen in the original corresponding scenario, retain the dividend/credit question in `us-foreign-tax-credit-1116` with the actual treaty and saving-clause review. The foreign-earned-income alternative remains a separate scenario routed to `us-foreign-earned-income-2555`; it does not characterise this dividend as earned income. The no-credit-on-excluded-income boundary in step 4 still applies. Do not transfer the UK calculation or its figures to US tax.

## When to refuse or refer

Refuse a usable tax, treaty, filing or event-order conclusion without its operative conditions and evidence. Refuse figures from memory or assumptions that trigger filing. Keep the precise missing issue visible; do not improvise another country's rule.

For actual treaty application/competent-authority agreement; foreign partnerships/funds/PFICs; cross-border estate, gift or inheritance; uncovered-country treatment; departure/expatriation; and late or missed information-return positions: **Check this point with one of our partner accountants.** Preserve the question and documents in the paper and seek review before the affected action.

## Sources

| Source and exact scope read | URL | Read on |
| --- | --- | --- |
| IRS worldwide-income opening statement; completed router read reused for the same limited boundary, not residence/treaty/form entitlement. | https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad | 2026-11-26 |
| IRS foreign-tax-credit page: exclusion interaction and revocation paragraph; eligibility and reduced-treaty-tax caveats read for context. | https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit | 2026-11-26 |
| TIOPA section 18: entitlement, reduction and arrangements conditions, subsections (1)–(6). | https://www.legislation.gov.uk/ukpga/2010/8/section/18 | 2026-11-26 |
| TIOPA section 33: all reasonable minimisation steps and objective standard, subsections (1)–(3). | https://www.legislation.gov.uk/ukpga/2010/8/section/33 | 2026-11-26 |
| TIOPA section 36: source-income limit, ordering and calculation conditions, subsections (1)–(7); formula also read in official XML. | https://www.legislation.gov.uk/ukpga/2010/8/section/36 | 2026-11-26 |
| HMRC INTM161210: general lesser-of/overall limits; following dividend pointer checked as company guidance, not imported into this individual's case. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm161210 | 2026-11-26 |
| GOV.UK: claim procedure, agreement limits/source-country reclaim, unilateral-relief caveat and foreign-gains context. | https://www.gov.uk/tax-foreign-income/taxed-twice | 2026-11-26 |

Not yet confirmed: no person's residence, treaty benefit, foreign-source treatment, exclusion, departure/exit-tax exposure, information-return obligation or relief entitlement is determined here. Named-treaty application, partnership/fund/PFIC, estate/gift/inheritance, uncovered-country and late-return positions remain explicit referrals. Australian content is routing only. The conditional UK example does not establish a client's tax or source-country refund; the US alternative requires its own computation.
