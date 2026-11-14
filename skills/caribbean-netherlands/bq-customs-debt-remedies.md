---
name: bq-customs-debt-remedies
description: >
  Analyse 2026 BES customs debt, statutory debtors, payment notices, monthly
  credit, security, refund requests, objections and first-instance appeals.
  Use after identifying an import, storage, movement or relief failure and
  its actual decision and service events. Separates customs procedure from
  domestic tax returns, permission from entitlement and refund grounds from
  objection deadlines. Includes primary legislation, delegated controls,
  authority guidance and fictional boundary cases. This source-cited draft
  holds actual liability, disputed service, special refund mapping, collection
  methods and higher appeals. Load with the universal workflow base and BES
  companions; professional review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Selected customs debt and remedy controls checked on 17 October 2026; actual events, charge and operative exceptions required"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-customs-clearance
  - bq-customs-valuation
  - bq-excise
---

# Bonaire, Sint Eustatius and Saba: customs debt and remedies

Identify the island, goods, customs destination, person, representation,
charge, event, decision and evidenced notification before selecting a debt
or remedy rule. Import duty's nil rate does not establish absence of ABB,
excise, costs or customs obligations. Use `bq-customs-valuation`, `bq-abb`
and `bq-excise` to establish each charge independently. [DAB]; [G-IMPORT]

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, confirmed profile, refusals, four universal outputs and all domain
outputs/checks. This Tier 2 reference supplies selected statutory controls,
not a complete controversy strategy or country pack. Unknown mandatory
conditions hold the complete financial output package.

## Choose the charge and procedural branch

Belastingwet BES article 6.21(1) applies customs legislation correspondingly
to levying and collecting import ABB. DAB article 4.5(1) applies the Act's
import-duty levy provisions correspondingly to import excise, without
prejudice to article 4.48. Domestic excise instead has article 4.3's separate
Belastingwet chapter-VIII bridge. Preserve the substantive tax's own
exceptions and relief conditions; correspondence does not make every duty
threshold an automatic ABB or excise allowance. [B1]; [DAB]

The authority's import page says payment is normally direct on declaration
and explains permitted monthly credit. The statutory outer payment term
below does not itself confer release of goods before payment/security.
Read `bq-customs-clearance` for acceptance, release and document discharge.
Do not substitute the general fifteen-day domestic remittance rule for
the actual customs branch. [G-IMPORT]; [DAB, articles 2.38 and 2.78][DAB]

## Debt event, person and evidence

| Branch | Event and person to establish |
|---|---|
| Ordinary import or temporary import with partial relief, article 2.69 | Debt arises on acceptance of the declaration; surrendering relief has its own surrender event. The declarant is debtor, with the represented person also liable in indirect representation. Suppliers of incorrect/incomplete declaration data are also debtors where the statutory knowledge test is met. |
| Irregular entry, article 2.70 | Use the actual irregular-entry event and the specified entry obligations. Entrants, knowing participants and knowing acquirers/holders have distinct tests. If the exact time cannot be established, paragraph 4 supplies the earliest-established-time rate rule. |
| Deemed declaration, article 2.70a | Deemed presentation, acceptance and release require article 2.29(2)'s conditions. A failed qualifying condition found on control is treated as irregular entry. |
| Temporary storage, article 2.71 | Identify the shortage, document-accounting shortfall or missed destination-declaration event. Debtor status follows the person who assumed responsibility under article 2.12(2), rather than every person with a transport invoice. |
| Undischarged document, warehouse shortage or removal from supervision, article 2.72 | Each branch has its own ascertainment/reporting event and debtor: named document holder, relevant warehouse operator/person, or remover and specified knowing participants/acquirers. |
| Failed relief, article 2.73 | Unauthorised change of destination, unmet conditions and relief obtained through bad information/substituted goods have different events. Establish the relief beneficiary and each additional statutory debtor. |

[DAB, articles 2.69–2.73 including 2.70a][DAB]

Article 2.74 distinguishes payment, qualifying remission of an unpaid amount,
and valid declaration/document invalidation. Its loss rule requires the
specified pre-release/non-import destination context and proof satisfactory
to the inspector of destruction, irretrievable loss or universal unusability
caused by the goods' nature, unforeseen circumstances or force majeure.
A missing-stock entry, theft allegation or insurance claim alone does not
establish that exception. Abandonment, supervised destruction and seizure
with forfeiture have their own conditions. [DAB]

Article 2.81 makes the statutory debtors jointly liable for the specified
tax, costs, interest and administrative penalties. Article 2.82 separately
addresses entity directors, including the director chain and specified
former directors. Article 2.83 permits recourse to the affected goods and
their packing in its unlawful-treatment circumstances, irrespective of
ownership. Determine actual liability professionally; these provisions do
not justify a journal automatically charging every director or owner. [DAB]

Business/professional persons and entities keep records and data carriers
showing relevant rights, obligations and customs facts for at least seven
years under article 2.52, in Dutch, Papiaments or English. Article 2.53
governs requested information and records; article 2.62 has inspection and
access duties. Under article 2.86(7), failure to comply fully with the named
2.52/2.53/2.62 duties can change the burden when objecting to a 2.76
post-assessment. Keep that trigger specific. [DAB]

The practitioner retains identity evidence, original authorities, tax
identifiers and bank details outside the agent. Use a sanitised evidence
register: case reference, declaration/document, event, debt branch, person,
amount by charge, decision, service evidence, payment/security allocation
and unresolved source or fact. No identity or filing submission is made here.

## Assessment, payment and credit

Articles 2.75–2.77 separate provisional determination, control adjustments
and post-assessment. A 2.76 post-assessment generally has five years from
the debt event, incorrect goods-account credit or refund. Its criminal-act
exception permits later assessment where that act prevented correct
determination. This is not an unconditional five-year write-off. The
applicable bases/rates follow the relevant debt event. [DAB]

Article 2.76(4) excludes post-assessment where the import-duty amount to be
recovered is **less than USD 8**. Article 2.78(8) separately disapplies its
paragraphs 5 and 6 where the customs debt is below USD 8. Keep their objects
and effects distinct; neither is a universal tax-free import value or a
blanket cancellation of costs, penalties or another charge. [DAB]

The payment invitation uses an assessment notice. Regulation 2.73 requires
the debtor's identifying details, decision reference/date, amount of duty,
interest, costs or penalty, and an objection clause. A combined notice can
contain several amounts. Retain distinct charge and service records.
[DAB, article 2.78][DAB]; [RULES]

| Article 2.78(5) branch | Statutory payment term |
|---|---|
| Amount communicated on the declaration or under 2.75(2) | No later than ten days after the communication. |
| Post-assessment | No later than ten days after the decision is delivered by registered letter or against dated receipt. |
| Receiver grants payment deferral | Within the actual granted term. A request is not a grant. |
| Administrative penalty imposed by separate decision | No later than ten days after delivery by registered letter or against dated receipt. |

[DAB]

Unpaid debt/penalty can be recovered against security under paragraph 6;
unpaid ordinary 2.69 debt has paragraph 7's post-assessment rule. Article
2.80 incorporates Belastingwet chapter VIII, title 5 for collection unless
otherwise provided. Establish every applicable exception, service event,
calendar and actual relief decision before producing dates or interest.
`bq-tax-compliance` records unresolved general collection methods; this
reference does not settle them by copying an ordinary assessment deadline.
[DAB]

Article 2.79 allows the receiver, on written request, to permit payment of
the month's amount within eight days after month-end. The debtor must be
BES-established, have continuing security and receive a permit; additional
conditions may apply. The authority requests business-register evidence,
expected declarations and credit amounts by import tax, and explains the
agreed credit/security amounts. A consolidated account is not itself the
permit, and awaiting its arrival does not establish an extended deadline.
[DAB]; [G-IMPORT]

## Security amount, form and release

Under articles 2.88–2.91, the actual or potential debtor provides security
by the inspector's term. The inspector requires only one security for the
particular goods or declaration and determines the amount using the
interests/risks, known debt or estimated debt as prescribed. Continuing
security requires a written request and decision; permission to use it at
several offices and withdrawal are separate decision matters. [DAB]

Article 2.90 says security **may** be omitted where potentially payable
import duty is below USD 56. This is discretionary and is not a goods-value
threshold, automatic release, cancellation of tax or permission to apply
the minimum excise-warehouse percentage. Regulation 2.74 separately permits
flat security for its temporary-import relief cases. [DAB]; [RULES]

Cash is in USD; a recognised guarantee has a written joint-liability
undertaking by a BES-established third party accepted by the inspector.
For continuing security, article 2.95 also permits acceptance of an
unencumbered BES property's mortgage with value at least 50% above the
security, or a qualifying pledge with value at least 25% above it.
Regulation 2.40 adds fire insurance naming the State as beneficiary,
the specified `hypothecair-belangverzekering` cover and deed covenants. Value alone
does not satisfy those conditions or compel acceptance. [DAB]; [RULES]

If security becomes inadequate, article 2.96 requires written notice and
allows supplementation or replacement within the inspector's term.
Article 2.97 releases security when the debt is extinguished, deemed not
to have arisen under 2.74 or can no longer arise. Partial release requires
a request and is subject to the amount justifying it. A customs refund,
release of collateral and return of an excise guarantee are different
ledger events. Apply `bq-excise` to its separate warehouse/stamp security.
[DAB]; [RULES, article 2.41][RULES]

## Decisions, objections and first-instance appeal

Article 2.84 generally requires a reasoned decision within nine months of
a written request containing the necessary evidence. A request to put an
oral decision in writing must be made within four weeks of that decision.
Refusal or failure to decide in time is treated as a decision. Article
2.85 separately governs retroactive withdrawal for knowingly/reasonably
knowable bad information and withdrawal/change for unmet conditions. [DAB]; [G-OBJECT]

Article 2.86 permits a reasoned objection to the listed classification,
calculation and statutory decisions within **two months** after its
specified communication, decision date or deemed-refusal event. Record
the particular trigger. Date and sign the objection; supplementary
motivation/evidence uses the authority's set term. Retain the receipt and
its recorded arrival date. Request the hearing in the objection if wanted;
the summons has at least seven days' notice. [DAB]

The inspector/receiver has nine months to decide the objection, with
refusal/silence equated to a decision. Article 2.87 permits first-instance
appeal within two months after the dated objection decision or expiry of
the 2.86(5) term. Do not silently import the general tax objection
extension into this customs provision. Objection costs follow B1 article
8.95: no objection fee; qualifying reimbursement requires a request before
the decision and the specified authority-caused unlawfulness. [DAB]; [B1]

The first-instance appeal incorporates B1 chapter VIII, title 8, section 3.
Article 8.103 specifies a signed, dated petition, party details, challenged
decision and grounds, with copies where possible and opportunities to cure
specified defects. Article 8.104 states a USD 30 court fee, payable within
six weeks after the clerk sends its notice, with its non-default exception
and refund on wholly/partly successful appeal. The appeal clock and fee
clock start from different events. [DAB]; [B1]

The incorporated court rules cover the response, hearing, representation,
evidence and judgment. Article 8.102 says an appeal does not suspend
payment. An objection is not proof of a payment-deferral grant either:
establish the actual suspension/relief basis. DAB 2.84(4)'s express
non-suspension rule concerns its specific body-search permission; it is
not relabelled as a universal objection rule. Enforcement opposition,
seizure complaints and higher appeals are separate branches requiring
their own procedure and deadlines. [DAB]; [B1]

## Refund request and its separate entitlement

DAB 3.144 includes repayment of paid duty and remission of charged but
unpaid duty. Article 3.145 generally requires a written request to the
inspector within five years **after the import declaration**, with available
proof and any required supplements. The liable person, payer, successor
or representative may request; payment goes to the eligible liable person,
payer or successor. Article 3.146 excludes refunds below USD 8 **per import
declaration or document**. The five-year request term is not a substitute
for a two-month objection protecting a challenged decision. [DAB]

| Ground | Conditions that remain necessary |
|---|---|
| No liability or excess amount, 3.149 | Prove no/ceased liability within its statutory scope, or an amount exceeding what could lawfully be collected. The inspector also acts on qualifying facts found within the 3.145 term. |
| Mistaken import declaration, 3.150 | Same goods, no incompatible use, already intended/qualified alternative destination at declaration, and prompt placement under it. |
| Rejected, defective, non-contractual or specified damaged goods, 3.151–3.152 | Relevant pre-release defect/non-conformity, no use beyond necessary testing, same goods, supervised destruction or re-export. Defects already reflected in the contract/price and post-discovery sale are exclusions. |
| Specified sender/order errors, later general legal restrictions or missed binding delivery dates, 3.153 | Establish the actual listed ground, no sale/use beyond necessary evaluation, same goods and supervised destruction or re-export. |
| International-organisation purchases, 3.154 | Establish the actual treaty refund provision and qualifying purchase; the organisation label alone is insufficient. |

[DAB]

Under 3.147, re-export for the 3.151/3.153 branches waits for the refund
decision unless the inspector permits earlier export. Preserve inspection
and identity evidence before disposing of the goods. Article 3.148 prohibits
incorrect/incomplete information and acts leading to unwarranted refunds.
[DAB]

For import ABB, tax regulation 6.12 incorporates the **3.145 request
procedure**. B1 6.21(2) separately concerns delegated substantive grounds
and conditions; this guide does not infer a refund amount from that
procedural bridge alone. Under 6.21(3), refunded import ABB cannot also be
input-deducted; a producer who already deducted it owes that amount on
the prescribed return. Reconcile the original tax, deduction, refund
decision, credit/payment and resulting ledger once each. Import excise
and domestic release/stamp refunds retain their own `bq-excise` branches.
[TAX-RULES]; [B1]; [DAB]

## Fictional boundary checks and completion

These stipulated components test the stated rule, not actual debt,
eligibility, accepted collateral or a complete filing calendar:

| Stipulated facts | Component result |
|---|---|
| Only duty post-assessment is considered: 7.99 versus 8 | 7.99 is below 2.76(4)'s threshold; 8 is not excluded by that amount rule alone. Other conditions remain necessary. |
| Potential duty is 55.99 versus 56 | The former falls within the stated discretionary security-omission threshold; neither creates an automatic waiver. The latter is outside that threshold. |
| Continuing-security amount is 1,000 and the relevant value rule applies | Mortgage value component: **1,000 × 1.50 = 1,500**; pledge value component: **1,000 × 1.25 = 1,250**. All property/deed/insurance/acceptance conditions still apply. |
| Permitted monthly credit is claimed without the permit/security evidence | Hold the credit treatment; an anticipated monthly statement does not establish permission. |
| An objection is filed against a communicated debt | Record the objection receipt and clock separately from payment; do not invent deferral. |
| A refund component is 7.99 versus 8 for one declaration/document | 7.99 is excluded by 3.146; 8 is not excluded on that amount ground alone. No aggregation across unrelated documents is inferred. |
| Defective goods were sold after the defect was discovered | Do not grant the 3.151 route without addressing 3.152's exclusion. |
| Goods for a 3.151 request are about to be re-exported before decision | Establish prior inspector permission under 3.147 or hold that step. |
| A refund is sought for an already input-deducted import ABB amount | Establish refund eligibility and decision, then preserve 6.21(3)'s producer adjustment; no double benefit. |

Check the charge bridge; event and person; decision/service evidence;
separate payment, objection, appeal, fee and refund clocks; actual security
and permissions; applicable calendar/exception; record duties and burden;
ground-specific refund proof; and single use of each payment/credit.
Unknown mandatory conditions remain Needs Input or holds with every
universal/domain output and professional-review question.

## Primary sources and limits

Read on 17 October 2026: DAB 2.51–2.97 including 2.70a, 3.144–3.154,
4.3–4.5 and 4.48; regulation 2.40–2.41 and 2.73–2.74; B1 6.21 and
8.95–8.116; tax regulation 6.12; and both complete authority pages below.
Earlier verified clearance, valuation and excise provisions remain in
their companions. Neither capturing a whole Act nor reading these selected
ranges certifies all its other provisions or their application.

Actual tax-specific correspondence of thresholds/refund grounds, disputed
notification, late admissibility, suspension, all collection/enforcement,
interest/remission methods, penalties, higher appeals, strategic/restricted
goods, substantive relief, external annexes, live forms/codes and portal
cases remain held. No PDF/OCR, private taxpayer records, identity/tax
identifier or bank submission, payment, guarantee, filing, engagement
workbook or practitioner sign-off was used. No comprehensive-area credit
is claimed.

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[TAX-RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[G-OBJECT]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/bezwaar-en-beroep-douane
[G-IMPORT]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/douanebestemmingen/invoer

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
