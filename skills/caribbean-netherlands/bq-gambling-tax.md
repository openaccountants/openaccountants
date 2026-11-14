---
name: bq-gambling-tax
description: >
  Analyse 2026 gambling tax in Bonaire, Sint Eustatius and Saba.
  Use for licensed operators, lotteries, other domestic prizes and foreign
  prizes of BES residents or entities. Separates operator margins, prize bases,
  withholding and self-assessment, including exemptions, aggregation, loss carry,
  gross-up and reporting periods. Includes primary legislation, implementing
  rules, current authority guidance and fictional boundary calculations. This
  source-cited draft holds actual licensing, delegated register details, wider
  tax-borne arrangements, form mapping and unresolved operational cases. Load
  with the universal workflow base and applicable BES companions; professional
  review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 statutory gambling-tax branches; establish operator licence, residence, period and actual prize facts"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
---

# Bonaire, Sint Eustatius and Saba: gambling tax in 2026

Classify the game, organiser, licence, recipient and taxable event before
applying a rate. A licensed casino's margin, a lottery prize subject to
withholding and a resident's foreign prize are different statutory branches.
Belastingwet BES chapter VIIa supplies the tax; the licensing instruments and
actual permission must be established separately. This reference does not
authorise an activity or determine a live licence. [B1]

Load `workflow-base` and applicable BES tax/domain companions. Preserve source
gates, confirmed profile, refusals, the four universal outputs and all
applicable domain outputs/checks. Use `bq-tax-compliance` for general procedure
and `bq-double-tax-relief` for the selected foreign-prize relief branch. This
Tier 2 reference supplies conditional tax components. Unknown mandatory
conditions hold the complete financial output package; it does not certify
every country slot or an operational engagement.

## Taxpayer, game and base

| Belastingwet BES article 7a.1 | Person identified and base |
|---|---|
| (a) Domestic game under the specified Wet hazardspelen BES I/II licence | Licensed operator; normally period stakes received minus prizes made available. If another person supplies the prizes, use the statutory alternative receipts for providing participation. |
| (b) Domestic game under a Loterijwet BES licence | Licensed operator identified by this provision; tax on prizes is collected by withholding under article 7a.8. |
| (c) Other domestic game outside the licensed (a)/(b) games | Prize recipient; prize base and self-assessment under article 7a.10. |
| (d) Foreign game | Prize recipient resident or established in BES; prize base and self-assessment under article 7a.10, with any applicable relief separately tested. |

[B1, articles 7a.1 and 7a.3–7a.10][B1]

Article 7a.2 includes chance-based prizes where participants generally lack
predominant influence, excluding life insurance and premium loans. Its contest
branch excludes the specified scientific/artistic or general-public-interest
performances. Domestic status depends on the residence/establishment of one
or more organising persons/entities; other games are foreign under paragraph
3. An app's branding, server address, place of payment or the winner's travel
location alone does not settle this statutory classification. [B1]

Article 7a.3 defines prizes to include goods with economic value and values
non-cash prizes at their value in economic exchange. Establish the actual
right, valuation and event rather than using an advertisement's headline
or assuming only the cash element counts. A player's stakes are not a general
deduction from the prize base in branches (b)–(d); test the specific exemption
below. The margin branch belongs to (a). [B1]

## Prize exemptions, aggregation and rate

For branches (b), (c) and (d), article 7a.4 exempts:

- A prize **not exceeding USD 600**.
- A prize **not exceeding the performance/stake corresponding to the
  participation giving entitlement to that prize**.

For the exemption test, specified lottery/contest prizes owed by the same
debtor, on tickets or parts of tickets from the same chance event, are treated
as one prize. Keep the actual debtor, event and participation evidence. These
are exemption conditions, not permission to deduct USD 600 or all stakes from
every larger prize. Do not apply the prize exemption to a licensed casino's
period margin. [B1]

Article 7a.5 sets **10%**. Paragraph 2 expressly prescribes a **100/90**
gross-up when, in branch (c), the person owing the prize bears the tax.
The corresponding legal branch must be established before using that formula;
do not silently extend this paragraph to every lottery/operator arrangement.
Fractional-cent and actual return-entry rounding remain held. [B1]

### Fictional prize components

These cases stipulate an ordinary branch (b)/(c)/(d) prize as indicated,
economic value in USD, the stated aggregation facts, no other exemption or
foreign relief, and no tax-borne arrangement except the final row. They test
tax components, not actual eligibility, a complete return or another tax.
[B1]

| Facts | Component result |
|---|---|
| Prize 600, corresponding stake 10 | Exempt at the inclusive 600 boundary. |
| Prize 601, stake 10 | Taxable full prize 601; tax 60.10, with no 600 deduction. |
| Prize 620, corresponding stake 620 | Exempt under the separate stake condition. |
| Prize 621, corresponding stake 620 | Neither exemption met; full-prize tax 62.10, not 0.10 on the difference. |
| Two lottery prizes of 350 from the same debtor and chance event, total corresponding stake 20 | Aggregate prize 700; tax 70. Separate small ticket amounts do not satisfy the exemption. |
| Branch (c), promised net prize 900, payer bears tax | Grossed prize 900 × 100 / 90 = 1,000; tax 100; net 900. |

The base, taxpayer and collection mechanism must remain separate. The same
rate does not make licensed lotteries and other domestic prizes the same
filing branch.

## Licensed casino/operator margin and losses

For article 7a.1(a), article 7a.3(1)(a) uses stakes received and prizes made
available in the period, or its alternative participation receipts where
another person supplies prizes. Article 7a.6 makes the period tax payable on
return, due as a tax debt on the period's last day. A negative difference is
offset against positive differences of following periods in chronological
order. It is not an immediate refund or a loss that may be used twice. [B1]

Implementing regulation article 8.8a normally assigns calendar months. For a
twelve-month accounting year not matching the calendar year, accounting-year
months replace calendar months. The inspector may assign another period in
special cases; permanent cessation shortens the period to the elapsed part.
Establish the actual assigned period and notice. Do not copy this monthly
rule into every prize recipient's point-in-time return. [RULES]

Article 8.11(3) retains the return duty for a period in which no tax is due.
A negative margin therefore does not by itself remove the filing obligation.
[B1]; `bq-tax-compliance`

The following fictional sequence stipulates the ordinary stakes-minus-prizes
branch, consecutive assigned periods, no other opening loss or adjustment,
and established USD amounts. It does not determine a real operator's receipts,
licence or deductible business expenses. [B1]

| Period | Stakes | Prizes made available | Current difference | Earlier loss used | Taxable positive remainder | Tax | Loss carried forward |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10,000 | 12,000 | -2,000 | 0 | 0 | 0 | 2,000 |
| 2 | 20,000 | 15,000 | 5,000 | 2,000 | 3,000 | 300 | 0 |
| 3 | 8,000 | 7,000 | 1,000 | 0 | 1,000 | 100 | 0 |

Retain each originating and absorbed loss separately and reconcile the
opening/closing schedule to period records. Administrative costs or all other
corporate losses are not additional deductions from this statutory gambling
margin merely because they are business expenses.

## Withholding, self-assessment and records

Under article 7a.8, branch (b)'s operator withholds when the prize is made
available and remits on return. The provision addresses prizes whose cash
element is insufficient: the stated missing withholding is deemed withheld,
with recovery from the recipient and suspension of non-cash delivery permitted
on its conditions. Do not erase the tax because a prize is non-cash or record
both a net and gross payout as separate prizes. Actual tax-borne arrangements
outside the express branch (c) gross-up remain held for their complete basis.
[B1]

For branches (c)/(d), article 7a.10 requires payment on return and lists debt
events: receipt, set-off, availability, becoming interest-bearing, or becoming
due and collectible. A delayed physical handover alone does not necessarily
delay the statutory event. Use general filing/payment rules, including article
8.11's applicable fifteen-day period/event term, with the actual classification
and any valid extension. Assessment collection has a different clock. [B1];
`bq-tax-compliance`

Articles 7a.7 and 7a.9 require the specified tax registers under delegated
rules. Article 7a.9 also requires the dated withholding note on the recipient's
request once the prize is paid, credited, set off or delivered. General tax
records, language and retention duties remain applicable. Exact delegated
register/note fields and actual form mapping were not completed here. Keep
game/licence classification, period, stakes, prizes, economic valuations,
exemptions, aggregation, loss usage, withholding, remittance and receipt
evidence reconciled; a payment record alone is not the tax calculation. [B1]

The reviewer retains actual identities, CRIB/tax numbers, permit originals and
bank details outside the agent. Use stable case references and sanitised
established amounts. Do not collect or submit ID documents, tax numbers or
bank details. No filing, payment or licensing submission is authorised here.

## Foreign prizes and public guidance limits

The unilateral relief decree's article 19 exempts a BES-resident/established
recipient's foreign-game prize when its specified similar-tax condition is
met, including the stated European Netherlands branch. Article 1's instrument
priority and the actual foreign charge still matter. Foreign income withholding
or a platform fee is not automatically a similar gambling tax. Do not replace
this exemption by an invented credit for every foreign amount. [UNI];
`bq-double-tax-relief`

The authority page confirms the 10% rate, ordinary prize exemptions, operator
margin and negative-difference carry. Its general paragraph calls the winner
the taxpayer while describing organiser withholding. The statute instead
identifies distinct persons in article 7a.1 and branch (b)'s operator in
article 7a.8. Preserve those statutory distinctions. The page's broad discussion
of an organiser bearing tax is not proof that article 7a.5(2)'s express branch
(c) formula applies to every branch. Conflicting actual instructions or forms
need prompt professional clarification, not an unverified default. [G-TAX]; [B1]

The page's fifteen-day-after-prize statement does not replace a licensed
casino's assigned period. Its assessment-objection summary does not remove
article 8.92(2)'s separate payment/withholding objection trigger. Establish the
correct remedy, decision/event, payment duty and source using
`bq-tax-compliance`. No bank reference, actual taxpayer submission or portal
mapping was tested. [G-TAX]; [B1]; [RULES]

## Completion conditions and primary sources

Unknown game, licence, residence, prize/right, valuation, aggregation, period,
exemption, foreign tax, carry, method or source remains Needs Input or a hold.
Follow each applicable refusal and its canonical message. Check the correct
taxpayer/base before using 10%; inclusive boundaries; full-prize taxation
where exemptions fail; FIFO operator losses; branch-specific gross-up; no
duplicated prize/payment; all universal/domain outputs; and professional review.

This reference does not complete licensing law, delegated register details,
all bilateral instruments, income/corporate treatment, indirect taxes, actual
forms, rounding or a complete country pack. No live operator, player, licence,
authority submission, engagement workbook or practitioner sign-off was used.

Read on 17 October 2026: the full gambling-tax chapter, articles 7a.1–7a.10;
implementing article 8.8a; the unilateral decree, including articles 1 and 19;
and the full current authority page. General procedure is reused from the
separate compliance reference. Licensing instruments, original gazette chains,
delegated register rules and actual downloaded forms were not reviewed here.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[UNI]: https://wetten.overheid.nl/BWBR0029674/2011-03-05
[G-TAX]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/kansspelbelasting-bedrijven/wanneer-kansspelbelasting

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
