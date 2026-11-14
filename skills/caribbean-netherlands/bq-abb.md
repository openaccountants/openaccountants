---
name: bq-abb
description: >
  Analyse 2026 general expenditure tax in Bonaire, Sint Eustatius and Saba.
  Use for Caribbean Netherlands ABB, producer sales, taxable services, imported
  goods, island rates, passenger vehicles, producer input credit, reverse charge,
  small entrepreneur relief and filing records. Distinguishes the three islands,
  the USD 32,000 relief threshold and the separate USD 10,000 administration
  concession. Provides primary legislation, period corrections and hypothetical
  component calculations for a professional reviewer. This source-cited draft
  holds unresolved classifications, customs valuation, invoice rounding and
  actual return mapping. It does not establish a complete country pack or
  authorise filing or payment.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 ABB reference; retrospective threshold correction included"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
---

# Bonaire, Sint Eustatius and Saba: ABB in 2026

Establish the island, transaction and tax period before calculating general
expenditure tax, or *algemene bestedingsbelasting* (ABB). The rates and relief
conditions below provide a dated reference for a qualified professional. This
Tier 2 draft has no accountant sign-off and does not yet support a complete
operational ABB return. Read the scope, source conditions and completion register
before applying an isolated rate or example.

Load `workflow-base`. Preserve its profile confirmation, refusal handling, four
outputs, recalculation and review requirements. ABB is a distinct BES tax;
European Netherlands VAT rules do not supply missing ABB rules.

## Scope, period and completion conditions

This guide covers ordinary producer supplies, ordinary services, selected import
rates, producer input credit, the small entrepreneur scheme, and the common ABB
filing and record duties identified below. Bonaire, Sint Eustatius and Saba are
separate public bodies for these provisions. Record the relevant establishment,
customer and destination for each transaction, including movements between the
islands. [Belastingwet BES, articles 6.1–6.3, 6.6–6.7 and 6.17][B1]

It does not determine income tax, payroll, social insurance, property tax,
transfer duty, excise, customs value or tariff classification. Special exemption,
export, entrepot, real-estate and place-of-service branches require their complete
applicable authority and facts. Their identification here is a referral, not a
completed treatment.

The source comparison covers the Belastingwet BES consolidations for [1 January
to 20 February][B2], [21 February to 10 April][B3] and [from 11 April 2026][B1].
Article 6.22's
USD 32,000 amount applies retrospectively from 1 January 2026 under the correction
in [Staatscourant 2026/3708, articles IV and V(d)][C1]. Do not apply the obsolete
USD 30,000 text displayed in the first snapshot. The same instrument corrects
2025 to USD 31,000; this guide does not calculate a 2025 return.

Articles 6.10a and 6.19a retain an undated proposed-repeal annotation. The [original
repeal and its delayed commencement][H1] were removed by [Staatsblad 2018/504,
articles XXXI and XLIV(1)(k)][H2]. [Staatsblad 2023/500, article I(I), (M)][H3] subsequently
amended these island rules from 1 January 2024 under article VI(1). Apply the
operative island provisions, not the abandoned repeal.

Before an engagement calculation, verify applicable amendments and delegated
rules for the requested period. An editing date does not establish legal
currency. The following gaps hold their dependent calculation and the complete
universal output package; labelled reference examples remain available.

| Completion condition | Evidence still required before operational use |
|---|---|
| Taxable event and place | Producer status, establishments and recipient status; all applicable service exceptions and island movements |
| Special treatment | Full conditions and approvals for exemptions, zero rates, relief, insurance and sector rules |
| Imports | Operative customs classification, valuation, release procedure and any relief decision |
| Money and timing | Invoice-level fractional-cent method, any foreign-exchange evidence, tax points, adjustments and period allocation |
| Filing | Actual invitation, permitted period, current return instructions and field mapping, deadline extensions and non-working-day rules |
| Delivery | Recalculated workbook, all four universal outputs, consumer/portal validation and professional sign-off |

## 2026 rates and thresholds

These rates apply only after establishing a taxable transaction and excluding
any applicable special rule. Amounts are US dollars (USD). The producer supply
base is the consideration excluding ABB under article 6.9; the import base is
the customs value under article 6.18. They are not interchangeable. [B1]

| Item | Bonaire | Sint Eustatius and Saba | Authority |
|---|---:|---:|---|
| Ordinary taxable producer supply | 8% | 6% | B1, articles 6.10(1), 6.10a(1)(a) |
| Ordinary taxable service | 6% | 4% | B1, articles 6.10(2)(a), 6.10a(1)(b) |
| Taxable insurance, after exemption checks | 7% | 5% | Same provisions; article 6.11(1)(l) exemptions |
| Ordinary taxable import | 8% | 6% | B1, articles 6.19(1), 6.19a(1)(a) |
| CO2-emitting passenger car or van | 25% | Progressive table below | B1, articles 6.10(2)(b), 6.10a, 6.19(2)(a), 6.19a |
| Passenger car or van without CO2 emissions | Nil | Nil | B1, articles 6.10(2)(c), 6.19(2)(b) |
| Small entrepreneur annual turnover limit, excluding ABB | USD 32,000 or less | USD 32,000 or less | B1, article 6.22; C1, articles IV and V(d) |
| Separate administration concession: annual service turnover, excluding ABB | USD 10,000 or less | USD 10,000 or less | R1, article 6.14; additional conditions apply |

For a qualifying CO2-emitting car or van in Sint Eustatius or Saba, let `V` be
the established taxable consideration for a producer supply or established
customs value for an import. Apply the table cumulatively. Prove whether the
vehicle is unused; an invoice description alone does not establish that status.
Check the excluded vehicle categories in R1, article 1.2. [B1, articles 6.10a
and 6.19a]

| Value band | Used vehicle ABB | Unused vehicle ABB |
|---|---|---|
| Up to USD 20,000 | 18% of V | 10% of V |
| Over USD 20,000, up to USD 30,000 | USD 3,600 + 22% of (V − USD 20,000) | USD 2,000 + 22% of (V − USD 20,000) |
| Over USD 30,000 | USD 5,800 + 30% of (V − USD 30,000) | USD 4,200 + 30% of (V − USD 30,000) |

## Position rules

### Classify the event and establish the place

1. Identify a producer supply, service or import under article 6.2. A producer
   manufactures locally from raw materials, auxiliary materials or intermediate
   goods and meets the restriction concerning retail premises in article 6.1(b).
   Reselling goods does not by itself establish producer status. A reseller's
   import and separate services still require their own analysis. [B1]
2. Locate goods under article 6.6 and imports under article 6.17. Movement
   between public bodies can be an import; record the customs regime and release
   evidence. Do not infer that a movement within BES is tax free. [B1]
3. For services by a BES entrepreneur to a BES customer, article 6.7(1) locates
   the service in the provider's public body. Article 6.7(2) addresses foreign
   customers and foreign establishments. For a non-BES provider, article 6.7(3)
   generally uses the business customer's establishment for B2B services and the
   provider's establishment for B2C services, subject to articles 6.7a–6.7j. Those
   exceptions include property, transport, events, catering, vehicle hire and
   electronic services. Hold any unresolved branch. [B1]
4. Check exemptions and zero rates separately. Article 6.11 includes conditions
   for medical, education, insurance, housing, transport and other activities;
   R1, articles 6.7–6.11 and its annexes add requirements. For example, the hotel
   accommodation exemption depends on tourist tax actually being due under an
   island ordinance. A sector label alone is insufficient. [B1, R1]

There is no factual default for island, establishment, producer status, place,
vehicle status or exemption eligibility. Missing evidence produces Needs Input.

Use `bq-warehouses-hde` for selected warehouse/HDE controls. The current Act
places its specified producer/export/HDE goods zero-rate branch in 6.10(2)(d),
while R1 6.6(1) retains a goods pointer to (c). The customs re-import rule
has the same letter mismatch. Hold actual export/re-import application
until the legal mapping is verified, preserving records and the full
financial output-package hold. This source comparison does not newly
revalidate the other figures in this reference. [B1, R1]

### Determine the liable person, base and tax point

The supplier normally owes ABB. Article 6.12(2) can shift liability to a local
business or body for a producer supply or a service by a non-BES entrepreneur
when its establishment conditions are met. An uninvolved local fixed
establishment does not necessarily prevent that shift. Check article 6.12(3)
and delegated reverse-charge cases under R1, article 6.9. Insurance through an
intermediary has separate article 6.13 rules. [B1, R1]

For domestic supplies and services, use article 6.9's consideration excluding
ABB. It includes a greater amount actually paid and substitutes market value
where consideration is below market value. Check non-cash consideration,
self-supplies and foreign-currency conversion separately. For imports, article
6.18 adds the specified duties, charges and incidental costs to customs value,
excluding ABB itself and the specified domestic transport after entry. A
supplier's invoice price alone does not establish customs value. [B1]

Article 6.14 generally uses invoice issue or its required latest date where an
invoice is mandatory, and performance otherwise; payment makes tax due no later
than receipt. Producer B2B invoices under that article are due within 15 days
after the delivery month. Advances and continuous reverse-charged services have
additional rules. ABB shown incorrectly on a document can itself become due
under article 6.14(7); do not automatically reverse it in the working paper.
Prices offered for taxable goods and services must include ABB under article
6.24. Keep net, tax and gross amounts separately. [B1]

### Restrict producer input credit

Article 6.3 permits a producer credit for qualifying ABB paid to other producers
on prescribed invoices or paid on imports, only to the extent the goods are raw
materials, auxiliary materials or intermediate goods for that producer's taxable
manufactured supplies. It is not a general business input-tax deduction.
R1, article 6.3 governs intended use, actual-use corrections and mixed allocation.
No credit is available merely because an expense is business related. [B1, R1]

Record payment period, invoice or import evidence, qualifying use and any
correction. Small entrepreneur relief restricts credit under R1, article
6.3(8). Do not both exempt an input import and deduct tax never paid. A qualifying
producer import exemption requires the inspector's designation and conditions
under B1, article 6.20 and R1, article 6.11. Excess producer credit and bad-debt
or returned-goods relief follow different request procedures under B1, articles
6.15–6.16 and 6.21; do not net an unapproved bad-debt refund into ordinary tax.

### Separate small entrepreneur relief from administration relief

Article 6.22 relief requires a written request and inspector's decision.
Ordinarily it concerns a natural person resident, established or with a fixed
establishment in the relevant public body whose qualifying annual turnover,
excluding ABB, is no more than USD 32,000. Aggregate that person's businesses
and professions. A separate route for bodies performing exclusively or almost
exclusively social or cultural activities requires a request before those
activities begin; verify its conditions before applying it. [B1, article 6.22]

For the threshold, R1, article 6.13 excludes turnover from goods supplies outside
article 6.2(a), includes the specified supplier turnover on which the recipient
accounts for ABB, and preserves recipient reverse-charge liability despite
relief. Do not exclude exempt service turnover merely because no ABB is charged.
The decision does not remove every other chapter VI duty. Periodic turnover
reporting remains; an issued annual return can substitute under R1, article
6.13(2). Any issued return must still be filed. [B1, article 6.22(4), (6); R1;
G1, pages 46–48]

If qualifying turnover exceeds USD 32,000, relief lapses and ABB becomes due on
the year's taxable activities, payable on the first return of the next calendar
year. It is not tax solely on the excess. Article 6.22(7) separately permits a
written post-year refund request for a qualifying natural person without a
relief decision. Neither route permits silently marking a transaction tax free.
[B1, article 6.22(5), (7)]

R1, article 6.14's USD 10,000 concession concerns specified record obligations
for a non-producer meeting its relief conditions. It requires a separate written
request and decision, starts at the beginning of the following year, and still
requires organised invoices, payment records and reverse-charge records. It
ends when its conditions fail. Following voluntary termination, a renewed
request cannot be granted for five years. Do not apply it automatically to
every entrepreneur below USD 32,000. [R1]

## Filing, records and return presentation

R1, article 8.7 sets a calendar month as the ABB period; the inspector may permit
a calendar quarter. Use the actual invitation and permission. B1, articles
8.5 and 8.11 generally require filing and payment within 15 days after the
period ends and a nil return where no tax is due. If no return has been issued,
request one before payment is due. Verify applicable extensions and
non-working-day rules before assigning a calendar deadline. [B1, R1]

R1, article 8.2 requires electronic filing for the specified ABB administration
obligors and BES fiscal representatives, with a hardship exemption route.
The January 2026 ABB handbook, published on 8 April 2026, instructs whole-dollar
return entries with dollar cents rounded down. Preserve transaction precision
and show the return presentation adjustment separately. This instruction does
not establish an invoice-level fractional-cent method or the treatment of
negative adjustments. Current form mapping remains a completion condition.
[G1, page 40]

Keep reconcilable supply, service, import, export and payment records and invoice
copies under B1, articles 6.25, 8.86 and 8.89a, with R1, article 6.15. The general
tax retention duty is seven years under article 8.86(6). A different legal-person
or sector retention duty can also apply; seven years is not a universal
destruction date. Keep actual identifiers, bank details, credentials and filing
authentication with the reviewer, outside agent inputs and outputs.

## Hypothetical component positions

These examples use stipulated, established law and facts for 2026. They are
arithmetic and classification examples, not completed returns, relief decisions
or customs valuations. No factual default is used. All amounts are USD.

1. **Ordinary Bonaire service.** A Bonaire BES entrepreneur supplies an ordinary
   taxable service to a Bonaire business for established net consideration of
   1,000. No exemption, reverse charge or advance applies. ABB is 1,000 × 6% =
   60; the ABB-inclusive amount is 1,060. Classify as supplier service tax under
   B1, articles 6.2(b), 6.7(1), 6.9, 6.10(2)(a) and 6.12(1).
2. **Provider island controls the ordinary BES service.** The same Bonaire
   provider supplies the same ordinary service to a Saba business, with no
   foreign-establishment branch. Article 6.7(1) still places the service in
   Bonaire. On net consideration of 1,000, ABB is 60 and gross is 1,060. Do not
   substitute Saba's 4% service rate from the customer's address. The BES
   provider is outside article 6.12(2)'s non-BES service-provider limb.
3. **Producer input credit.** A confirmed Bonaire producer has taxable
   manufactured supplies with net consideration of 10,000, output ABB of
   10,000 × 8% = 800, and 240 of qualifying ABB paid in the same period on
   materials used wholly for those taxable supplies, with prescribed invoices.
   Under B1, article 6.3 and R1, article 6.3, credit is 240 and the component
   difference is 800 − 240 = 560. General overhead or service costs do not
   become deductible merely by joining this schedule. Other liabilities and
   return fields must be reconciled before a period result is deliverable.
4. **Used car in Sint Eustatius.** A qualifying emitting used passenger car has
   established import customs value of 35,000. B1, article 6.19a gives
   5,800 + (35,000 − 30,000) × 30% = 7,300 ABB. The tax plus established base is
   42,300; this is not a total landed-cost quotation. At 20,000 tax is 3,600;
   at 30,000 it is 5,800. The marginal rates do not apply to the whole value.
5. **Unused car in Saba.** With unused status and an established 35,000 customs
   value, the emitting vehicle instead uses article 6.19a(2):
   4,200 + (35,000 − 30,000) × 30% = 5,700 ABB. Tax plus base is 40,700.
   At 20,000 tax is 2,000; at 30,000 it is 4,200. Compared with example 4,
   the unused-status difference is 1,600. Missing status requires Needs Input.
6. **Relief does not remove recipient reverse charge.** A Saba natural-person
   business has a valid article 6.22 decision and qualifying annual turnover of
   20,000. It buys an ordinary taxable B2B service for net 1,000 from a non-BES
   provider with no involved Saba establishment. The verified article 6.7(3)(a)
   place is Saba and article 6.12(2) makes the recipient liable. ABB is
   1,000 × 4% = 40. R1, article 6.13(1)(b) preserves that liability; relief
   does not make it zero. No producer input-credit entitlement is stipulated.
7. **Exceeding the relief limit.** A Bonaire natural-person ordinary service
   business with a relief decision earns established ABB-exclusive taxable
   consideration of 32,500 in 2026. It has no other business, exemption,
   reverse charge or input credit. The 32,000 limit is exceeded; article
   6.22(5) makes the whole year's service ABB 32,500 × 6% = 1,950, payable on
   the first return of 2027. Charging 6% only on the 500 excess would give 30
   and understate this component by 1,920. If the amount received was instead
   an ABB-inclusive fixed price, establish the contract and article 6.9 base
   before calculating; the example does not convert gross receipts into net.
8. **Whole-dollar return display.** An established positive return-field
   amount of 123.99 is shown as 123 under G1, page 40. Retain 123.99 in the
   precision schedule and show a 0.99 presentation difference. Do not round
   each source transaction down to force that result; invoice rounding and
   aggregation still require their applicable method and actual form mapping.

## Defaults, questions and reviewer thresholds

| Missing item | Treatment | Alternative and disclosure |
|---|---|---|
| Island, period, establishment, event, place or vehicle status | Needs Input; no factual default | Obtain the missing evidence before applying a rate |
| Relief decision, exemption conditions, input-credit evidence or customs value | Needs Input; no factual default | An apparently higher tax amount cannot establish eligibility or unknown law |
| Invoice rounding, filing period or return instructions | Needs Input for the dependent calculation | Retain source precision; obtain the relevant method or notice |
| Applicable law or required delegated authority | Needs Input as a source condition | Identify and verify the authority; do not classify unknown law as a T2 factual assumption |

This version permits no substantive factual defaults, so no T2 cash-question
floor is used to authorise one. Ask essential factual questions even when cash
impact is small. For the universal question filter, the configured question
threshold is USD 0 where a later verified companion expressly permits a default.
Flag every ABB amount for reviewer sign-off at a USD 0 attention threshold,
including nil, refunds, relief, island/place boundaries and source holds.
These are workflow settings, not statutory thresholds. Preserve the base's
grouping rules and ten-question ceiling.

## Topical refusal catalogue

Needs Input identifies a missing fact or source and is not itself a refusal.
Run the universal catalogue and these codes; preserve the exact message when
a trigger applies. A refusal stops the workflow before partial return output.

| Code | Trigger | Verbatim message |
|---|---|---|
| R-BQ-ABB-SCOPE | The requested computation needs a tax, period or special transaction outside the verified scope | This request requires BES authority or a companion outside this ABB guide's verified scope. Load the required content and consult a qualified professional before calculating the affected obligation. |
| R-BQ-ABB-OPERATIONAL | Asked to produce a complete operational ABB return while this guide's completion conditions remain open | This ABB reference does not yet support a complete operational return. Resolve the completion conditions and retain a qualified professional reviewer before preparing the filing package. |
| R-BQ-ABB-AMBIGUITY | More than ten grouped factual questions remain necessary under the universal workflow | This ABB preparation needs more than ten grouped factual questions. Resolve the source records with the professional reviewer before restarting the workflow. |

## Output and intake additions

Retain the universal workbook, reviewer brief, action list and review checklist.
Add an **ABB position schedule** with a stable redacted record reference, island,
event, provider/customer establishment, place rule, liable person, tax point,
net base, rate, output ABB, qualifying producer credit, reverse charge, relief
decision reference, source pinpoint, precision amount and return presentation
adjustment. Map every universal transaction field to a column. Add separate
annual relief-turnover and customs-evidence schedules where applicable.

The brief must state which completion conditions were cleared, the actual filing
period, every source hold, and every universal and topical refusal code's
disposition. Show actual return fields only after verifying their current
instructions. A component example cannot substitute for the recalculated
workbook, a complete reconciliation or professional sign-off.

Infer the profile from redacted records and obtain the universal confirmation.
Ask for: the island and requested period; legal form and activities; provider
and customer establishments; producer premises and manufacturing facts; net
versus gross contract prices; tax points and advances; goods movements and
customs evidence; vehicle classification, emissions and unused status; relief
and import decisions; qualifying paid input ABB and use; all businesses' annual
turnover; filing invitations and period permissions; and the reviewing
professional's role. Do not request identity documents, tax identifiers, bank
details or authentication material.

## Review Checklist Items

- Confirm the 2026 period chain and retrospective USD 32,000 correction.
- Check the island rule before selecting a rate; resolve every service exception.
- Distinguish producer supplies, resale, services and imports without double counting.
- Prove vehicle classification, emissions, unused status and progressive boundaries.
- Restrict credit to qualifying paid producer inputs and reconcile use corrections.
- Check relief decisions, aggregate annual turnover and preserved reverse charge.
- Keep the USD 10,000 administration concession separate from USD 32,000 relief.
- Reconcile tax points, precision amounts, return presentation and actual field mapping.
- Confirm monthly or permitted quarterly filing, invitation, nil return and deadline rules.
- Preserve records, all four universal outputs, recalculation and professional sign-off.

## Primary source library

Sources were inspected on 16 October 2026. Statutes and operative delegated
rules govern; the handbook supplies the identified administrative instructions.
Captured text alone does not prove an unexamined cross-reference or a later
amendment. The completion conditions above remain part of every applied rule.

- **B1:** [Belastingwet BES, consolidation from 11 April 2026](https://wetten.overheid.nl/BWBR0029244/2026-04-11), chapter VI and the cited chapter VIII provisions.
- **B2:** [Belastingwet BES, 1 January 2026 snapshot](https://wetten.overheid.nl/BWBR0029244/2026-01-01), valid to 20 February 2026; read with the retrospective correction.
- **B3:** [Belastingwet BES, 21 February 2026 snapshot](https://wetten.overheid.nl/BWBR0029244/2026-02-21), valid to 10 April 2026.
- **R1:** [Uitvoeringsregeling Belastingwet BES](https://wetten.overheid.nl/BWBR0029332/2025-01-01), articles 1.2, 6.3–6.15, 8.2 and 8.7; displayed operative version from 1 January 2025.
- **C1:** [Staatscourant 2026/3708](https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html), articles III–V, retrospective 2025 and 2026 threshold corrections.
- **H1:** [Staatsblad 2010/847](https://zoek.officielebekendmakingen.nl/stb-2010-847.html), chapter II, article XVI(E), and chapter III, article II(4), the proposed repeal and delayed commencement.
- **H2:** [Staatsblad 2018/504](https://zoek.officielebekendmakingen.nl/stb-2018-504.html), articles XXXI and XLIV(1)(k), withdrawal of that chain.
- **H3:** [Staatsblad 2023/500](https://zoek.officielebekendmakingen.nl/stb-2023-500.html), article I(I), (M) and article VI(1), later island amendments and commencement.
- **G1:** Belastingdienst Caribisch Nederland, [Handboek ABB, version January 2026](https://www.belastingdienst-cn.nl/site/binaries/site-content/collections/documents/belastingdienst/abb/handboek-algemene-bestedingsbelasting/index/handboek-abb-versie-2026.pdf), published 8 April 2026, pages 40 and 46–48.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B2]: https://wetten.overheid.nl/BWBR0029244/2026-01-01
[B3]: https://wetten.overheid.nl/BWBR0029244/2026-02-21
[R1]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[C1]: https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html
[H1]: https://zoek.officielebekendmakingen.nl/stb-2010-847.html
[H2]: https://zoek.officielebekendmakingen.nl/stb-2018-504.html
[H3]: https://zoek.officielebekendmakingen.nl/stb-2023-500.html

## Revision and assurance

Version 0.1, 16 October 2026: initial 2026 ABB reference, with island rates,
retrospective relief correction, restricted producer credit and component
examples. Operational conditions remain open; no country-complete or
accountant-reviewed status is claimed.

This guide supports professional review and does not constitute tax, legal or
financial advice. The reviewer is responsible for the final treatment, filing
and payment. Recheck operative sources and the particular facts before reliance.

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
