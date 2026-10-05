---
name: cross-border-tax-workflow-base
description: Foundation workflow base for cross-border / international personal-tax content skills. Contains the residency-map intake, the sequenced-plan output contract (a cross-border answer is an ORDERED set of steps, not N separate answers), the cross-border conservative-default principle, the AUDIT FLASH POINT marker convention, the double-tax-relief / treaty-bridge convention, and the mandatory human hand-off. This skill provides workflow architecture only — it contains no country-specific or topic-specific rules. It MUST be loaded alongside a topic content skill (e.g. us-feie-ftc, us-foreign-trust-reporting) and the relevant country skills. This base is the foundation every international content skill loads on top of.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-10-05
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross-border tax workflow: the shared method for any case that touches more than one country

Figures are for tax year 2026. This Guide carries no rates, thresholds or amounts, and it does not expire with a tax year. It is the shared method every cross-border case follows: the residence of each person in each country, the source of each item of income, the treaty tie-breaker where two countries both claim a person as resident, relief by credit or by exemption, and the forms that claim the relief and report the facts. The country and topic Guides hold the rules and figures. `cross-border-tax-router` decides which of them to load; this Guide decides how they are put together.

## What this file is

The shared method that every cross-border country and topic Guide loads on top of. It carries no country rule and no topic rule of its own. Those live in the topic Guides (for example `us-feie-ftc`, `us-foreign-tax-credit-1116`, `us-fbar-fatca-reporting`, `us-cfc-gilti`, `us-foreign-trust-reporting`, `us-expatriation-exit-tax`) and in each country's own Guides (for example `us-tax-residency`, `uk-statutory-residence-test`, `uk-non-dom`, `mt-non-dom`, `ie-non-dom`, `cy-non-dom`, `ca-tax-residency`, `leaving-australia-tax-residency-cgt`).

A topic Guide needs this method, and this method computes nothing without the topic and country Guides. Load all three, in the order `cross-border-tax-router` fixed.

Currency. Each country and topic Guide states its own tax year. This method does not depend on a year.

The output is a working paper for a licensed accountant, never a filed return. Cross-border information returns carry heavy penalties, and many cross-border events cannot be undone once done. The work ends by handing the working paper to a licensed accountant in the lead country before the person acts.

## The method, step by step

1. **Residence of each person, in each country, under that country's own law.** Run each country's domestic test separately. The US treats a non-citizen as resident if they meet the green card test or the substantial presence test for the calendar year, and a person can be both non-resident and resident in the same year, which needs a dual-status return ([IRS: determining an individual's tax residency status](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)). The UK looks at each tax year separately under the statutory residence test ([HMRC RDR3](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3)). Record citizenship too: a US citizen or resident alien is taxed on worldwide income wherever they live ([IRS: US citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)). Route the tests themselves to the country Guides.
2. **Treaty tie-breaker, where two countries both treat the person as resident.** For the US, the residence tests do not override a treaty's definition of residence, so a dual-resident taxpayer can still claim treaty benefits if the treaty contains a tie-breaker rule. A person the tie-breaker treats as resident of the other country is a non-resident alien in figuring US income tax, but is treated as a US resident for other purposes ([IRS Publication 519](https://www.irs.gov/publications/p519)). In the UK and US convention the tests run in order: permanent home; if there is a permanent home in both States, the centre of vital interests; if that cannot be determined, or there is no permanent home in either State, habitual abode; then nationality; then mutual agreement between the competent authorities ([UK and US double taxation convention, Article 4](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force)). Stop at the first test that gives one answer. Read the named treaty for every other pair of countries, since wording differs.
3. **Source of each item of income or gain.** For each item, record which country it arises in and whether that country taxes non-residents on it. A UK resident "may be taxed on your foreign income by the UK and by the country where your income is from" ([GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)). For a UK resident's capital gain, GOV.UK says the person usually pays tax in the country of residence and is exempt in the country where the gain is made, with no claim needed. For a gain on an asset that cannot be taken out of the country, such as land or a house, or that the person is using for business in that country, the person will need to pay tax in both countries and get relief from the UK (same page). The country Guide holds each source rule.
4. **Who has the primary right, and how the other country gives relief.** For each item taxed by more than one country, name the mechanism. By credit: the US lets a person subject to US tax on foreign-taxed income take either a credit or an itemised deduction for qualifying foreign income taxes ([IRS: foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit)); route to `us-foreign-tax-credit-1116`. By exclusion or exemption: if a US person elects to exclude foreign earned income or housing costs, no credit is allowed for taxes on the excluded income (same IRS page), and if the person takes the credit, one or both exclusion elections may be considered revoked (same IRS page); route the choice to `us-feie-ftc`. By treaty: the UK and US convention requires the US to allow its residents and citizens a credit for UK income tax, subject to the limits of US law (Article 24 of the convention linked in step 2). In the UK, Foreign Tax Credit Relief is usually claimed on the tax return, and the relief can be less than the foreign tax paid. Foreign Tax Credit Relief cannot be claimed where the double taxation agreement requires the tax to be claimed back from the source country. Without an agreement, relief is usually still given unless the foreign tax does not correspond to UK Income Tax or Capital Gains Tax ([GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)).
5. **Check the saving clause before any treaty benefit for a US citizen or resident.** Most US treaties contain a saving clause that preserves the right of the United States to tax its citizens and residents as if the treaty had not come into effect, although many treaties have exceptions ([IRS Publication 519](https://www.irs.gov/publications/p519)). In the UK and US convention this is Article 1, paragraph 4, with the exceptions in paragraph 5 (convention linked in step 2).
6. **The forms that claim relief and report the facts, in each country.** A relief not claimed on the right form is not relief. A dual-resident taxpayer who claims treaty benefits files Form 1040-NR with Form 8833 attached and computes tax as a non-resident alien ([IRS Publication 519](https://www.irs.gov/publications/p519)). Americans abroad get the exclusion and the credit only by filing a US return, and US taxpayers with foreign financial accounts over the reporting threshold must report them on FinCEN Form 114 even when the accounts produce no taxable income ([IRS: US citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)). For a UK resident, where income is exempt from foreign tax but taxed in the UK, or where the treaty requires it, relief must be applied for in the source country, with HMRC confirming residence ([GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)). List every information return the facts trigger, not only the income forms; the thresholds and deadlines are in the topic Guides.
7. **Order the steps and say why.** Test residence changes before sales, characterise entities before distributions, and test expatriation before later sales (see Section 1, Layer B). A treaty tie-breaker that treats a green card holder as a non-resident alien can in certain instances trigger the section 877A expatriation tax ([IRS Publication 519](https://www.irs.gov/publications/p519)), so test both together. A country may treat a departing resident as having sold certain types of property at their fair market value on departure, even if they were not sold: Canada calls this a deemed disposition ([CRA: leaving Canada](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html)).
8. **Hand off** the working paper as in Section 8.

## Ask the client first

- In which countries were you resident, under each country's own rules, during the year, and on which dates did that change?
- Do you have a home available to you in more than one country, and where are your family and main economic ties?
- Which passports do you hold, and do you hold or have you ever held a US green card?
- Which income, gains or assets arise in which country, and has any country already withheld or charged tax on them?
- Do you hold foreign bank, brokerage or pension accounts, or interests in foreign companies, trusts or funds?
- Have you already claimed treaty relief or filed a certificate of residence in any country for this year?

## Section 1: The sequenced-plan output contract

A cross-border answer is not a stack of single-country answers. It is an ordered plan. Every cross-border topic Guide produces both layers below.

### Layer A: Reference layer (the rules)

For each country and topic engaged, a faithful, cited statement of the rule (statute, form or treaty article), set out as decision steps an assistant can reason over. Layer A answers "What does each system require, and where is it written?" Every rule cites its source, for example section 911, section 877A, Form 3520, or the treaty article.

### Layer B: Executable layer (the sequenced plan)

A step-by-step procedure that takes the person's facts and the order of events fixed by `cross-border-tax-router`, and produces an ordered list of steps. Each step states:

1. What happens (the event, and when).
2. Which country taxes it, and on what basis (citizenship, residence, domicile or source), citing the Layer A rule.
3. How double tax is relieved at that step (credit, exemption or exclusion, treaty relief article, re-sourcing, tie-breaker), citing the article or section.
4. Which forms the step triggers in each country, with the deadlines from the topic Guides.
5. Why the step sits where it does, and what breaks if it moves.

Rule: every Layer B step references the Layer A rule it carries out. No position without a cited source, and no treaty benefit asserted without the article and the form that claims it.

## Section 2: The double-tax-relief and treaty-bridge convention

The most valuable part of a cross-border answer is the bridge: how the systems' taxing rights are reconciled so the same income is not taxed twice without relief. For every item that more than one country taxes, state:

- Which country has the primary taxing right and which gives relief.
- The mechanism: foreign tax credit, exemption or exclusion, a treaty relief article, treaty re-sourcing of income (in the UK and US convention, Article 24 for a United States citizen who is a resident of the United Kingdom), a residence tie-breaker, or a reduced treaty withholding rate.
- The form that actually claims it (for example Form 1116 or Form 8833 in the US, and the exclusion form set out in `us-feie-ftc`; the Self Assessment return in the UK).
- The double tax the mechanism leaves in place. In the UK, relief can be smaller than the foreign tax paid, where a smaller amount is set by the double taxation agreement or the income would have been taxed at a lower rate in the UK ([GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)). A US person cannot take a credit for tax on income they chose to exclude ([IRS: foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit)).

The saving clause caveat. Most US treaties let the US tax its citizens and residents as if the treaty had not come into effect, although many treaties have exceptions ([IRS Publication 519](https://www.irs.gov/publications/p519)). Never assert a treaty benefit for a US citizen or resident without checking the saving clause and its exceptions first.

## Section 3: AUDIT FLASH POINT convention

Mark every position that a tax authority (the IRS, HMRC, the ATO and others) commonly challenges with a bold marker:

> **AUDIT FLASH POINT:** [the judgement at issue, why it is contested, the evidence behind the position taken, and the form or disclosure that supports it.]

These are the positions a reviewing accountant must personally own. List every flash point the case triggers in the reviewer brief. Never bury one.

Typical cross-border flash points: the date residence ended and the day-count evidence; treaty residence tie-breakers; grantor or non-grantor trust characterisation; the choice between exclusion and credit and the tests behind the exclusion; covered expatriate status and exit tax valuations; foreign funds held by a US person; reasonable-cause positions for late information returns; and any position that rests on facts in another country the preparer cannot check.

## Section 4: Conservative-default principle (cross-border edition)

When facts are incomplete and a position could go either way across a border, take the position that is harder to challenge and leaves a reporting trail, say that you have done so, and name the fact that would change the answer. When unsure:

- Assume the broader taxing right applies (for example that US citizenship or residence taxation reaches the item).
- Assume the reporting obligation is triggered and the information return is filed, rather than assuming an exemption. An unnecessary information return costs little; a missed one can carry penalties.
- Assume the higher-tax characterisation of an entity or instrument until a fact shows otherwise.

Never pick the favourable treatment silently. Aggressive positions (for example a treaty benefit for a US citizen or resident that is not among the exceptions to the saving clause, or a decision not to file) need an explicit, documented instruction and a licensed accountant's sign-off. They are never the default.

## Section 5: Structured intake (the residency map)

If facts needed for Layer B are missing, ask for them in one structured block before computing. Never piecemeal, never by guessing. The map in `cross-border-tax-router` Step 0 is the intake; restate any gaps here, grouped by the decision they unlock:

~~~
To put this in order, these facts are still needed:
  1. [Fact], used in [step / rule]
  2. [Fact], used in [step / rule]
  ...
If [fact] is not available, the plan assumes [the broader taxing right / that the reporting
obligation applies] (Section 4) and flags it for your accountant.
~~~

## Section 6: Universal self-checks

Before delivering output, check (each topic Guide adds its own checks):

- [ ] Both layers produced, with a cited rule for every step
- [ ] Residence tested in each country under its own law, and a tie-breaker run where two countries claim the person
- [ ] Source recorded for every item of income or gain
- [ ] The answer is an ordered plan, not separate country answers
- [ ] The order of events stated and justified (what breaks if a step moves)
- [ ] For every item taxed by more than one country, the relief mechanism and the form that claims it stated
- [ ] Saving clause checked before any treaty benefit for a US citizen or resident
- [ ] Every information return the facts trigger listed, not only the income forms. For a US person, take the forms and their tests from the topic Guides: FinCEN Form 114 and Form 8938 from `us-fbar-fatca-reporting`, Forms 3520 and 3520-A from `us-foreign-trust-reporting`, and Form 5471 from `us-cfc-gilti`. Interests in foreign partnerships and foreign funds have no topic Guide here, so flag them as open items for the licensed accountant.
- [ ] Every figure traced to a country or topic Guide and its official source; none stated from memory
- [ ] Every triggered AUDIT FLASH POINT listed in the reviewer brief
- [ ] Conservative default applied and flagged wherever facts were missing
- [ ] Any uncovered country rule, named treaty article, foreign fund or estate item flagged as an open item, not improvised
- [ ] The output labelled as an unreviewed working paper, and the hand-off in Section 8 done

## Section 7: Output specification

Deliver, in this order:

1. Situation map: citizenship, residence in each country, domicile where relevant, and the event, in one block.
2. The sequenced plan: the ordered Layer B steps (event, who taxes, relief, forms, why it sits there).
3. Reference trace: the rule, form or treaty article behind each step.
4. Double-tax bridge summary: per item, the primary right, the relief mechanism, the claiming form, and what is left over.
5. Information-return checklist: every information return triggered, with the deadlines and penalties taken from the topic Guides.
6. Reviewer brief: the judgements taken, every AUDIT FLASH POINT, the conservative defaults applied, and the open items the licensed accountant must clear.
7. Hand-off, as in Section 8.

## Section 8: Review status and the mandatory hand-off

Every cross-border output is an unreviewed working paper. It is drafted from statutes, forms and treaties, and no licensed accountant has signed the specific plan. Never present it as reviewed by an accountant.

The work must end by handing the working paper to a person. Before the person takes any step that cannot be undone (selling, distributing, giving up residence, giving up citizenship or a green card, filing), tell them plainly: this is a working paper, not advice to act on yet; a licensed accountant in the lead country should review it, and that accountant signs off and, if engaged, files. The lead country is the one with the primary taxing right or the largest exposure: usually where the person is or will be resident, or the US where citizenship taxation dominates. Give the accountant the situation map and the full sequenced plan.

## When to refuse or refer

- Refuse to assert a treaty benefit without the article, the saving clause check for a US person, and the form that claims it.
- Refuse to state a rate, threshold or deadline from memory. Take it from the country or topic Guide, or flag it.
- Refer any position that depends on the full text of a named treaty article, or on a mutual agreement between tax authorities.
- Refer before the person takes any step that cannot be undone.
- Refer foreign funds held by a US person, cross-border estate, gift or inheritance questions, and any country with no Guide.
- Refer late or missed information returns before anything is filed.

## Section 9: Disclaimer

These Guides give computational and interpretive guidance on cross-border personal tax. They are not tax or legal advice, not an engagement, and not a filed return. Cross-border outcomes turn on entity, residence and treaty facts and significant judgement, and the order of events often changes the result. Have every output reviewed and signed by a qualified, licensed accountant in each relevant country before acting on it. Penalties on cross-border information returns can be severe; when in doubt, file and ask.

## Sources

- [IRS: determining an individual's tax residency status](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)
- [IRS: US citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)
- [IRS: foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit)
- [IRS Publication 519, US tax guide for aliens](https://www.irs.gov/publications/p519)
- [UK and US double taxation convention, as amended by the 2002 protocol](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force)
- [HMRC RDR3, statutory residence test guidance](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3)
- [GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)
- [CRA: leaving Canada, emigrants](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html)

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
