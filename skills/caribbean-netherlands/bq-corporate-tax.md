---
name: bq-corporate-tax
description: >
  Analyse 2026 entity taxation in Bonaire, Sint Eustatius and Saba. Use for
  corporate residence decisions, distribution tax, holding companies, substance
  tests, participation exemptions, gross-ups and minimum-tax screening.
  Distinguishes BES status from European Netherlands corporate and dividend
  taxation, distributions from accounting profit, and ordinary returns from
  minimum-tax obligations. Includes primary legislation, current authority
  guidance, conditional examples and reconciliation controls. Records outdated
  guidance, separate retention duties and unresolved foundation withholding.
  This source-cited draft holds foreign relief, special entities, exit valuations,
  minimum-tax computations and unmapped returns. Load with the corporate income
  tax workflow base; professional review remains required.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 status and distribution rules; separate minimum-tax reporting periods"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
  - bq-formation
  - bq-financial-statements
---

# Bonaire, Sint Eustatius and Saba: entity and distribution taxes in 2026

Establish the entity's actual residence, legal form, inspector's decision and
continuing conditions before choosing a tax regime. Incorporation in BES does
not establish a general zero corporate-tax outcome. Distribution tax and the
minimum-tax overlay have different bases, taxpayers and deadlines.

Load `workflow-base` and `corporate-income-tax-workflow-base`. Preserve their
intake, source gates, profile confirmation, refusals, four universal outputs,
corporate reviewer-brief components and 18 checks. This Tier 2 reference supplies
selected regime and distribution rules. It does not populate every corporate
companion slot or authorise a complete financial output package. A required
unfilled slot remains a hold; labelled conditional reference examples remain
available within their assumptions.

## Entity, residence and decision

Belastingwet BES article 1.5 determines residence from the circumstances.
Chapter V uses its own entity definition: article 5.1 covers specified companies,
cooperatives/associations, foundations, designated funds and other listed forms.
Do not assume that every partnership or foreign arrangement is an ordinary NV.
Tax identity and registration evidence stay with the authorised reviewer outside
the agent; record stable references and the established classification. [B1]

Article 5.2(1) generally deems an actually BES-established chapter V entity to be
established in the **European Netherlands** for this chapter. Its express
exception concerns BES-established foundations and designated funds
(*doelvermogens*). The following routes must be distinguished. [B1, article 5.2][B1]

| Route | Statutory conditions and evidence |
|---|---|
| Small ordinary entity, article 5.2(2)(a) | Inspector's decision on request; annual turnover at most USD 80,000 **and** assets ordinarily at most USD 200,000 **and** none of the listed financial, royalty, insurance/reinsurance, management or trust-service activities. |
| Asset-composition route, article 5.2(2)(b) | Inspector's decision; no more than 50% of assets ordinarily comprise the listed investments, participations, liquidity, assets made available to persons outside BES and other specified foreign financing assets. Apply the complete categories, not only foreign securities. |
| Substance route, article 5.2(2)(c) | Inspector's decision; ordinarily at least three BES-resident people in full-time permanent work, independently performing the specified asset activities with matching powers/responsibilities, **and** BES premises worth at least USD 50,000 available for at least 24 months. The listed financial/management/trust activities additionally require the specified own office and customary facilities. |
| Admitted trade/services warehouse, article 5.2(3)(a) | Actual admission under Customs and Excise BES chapter V; the residence fiction does not apply. A licence application or informal zone description is insufficient. |
| Holding route, article 5.2(3)(b) | Inspector's decision; at least 50% participation in an admitted warehouse entity or one with an article 5.2(2) decision, with the holding's other assets meeting the article 5.2(2)(b) test. |

The paragraph 2 routes are alternatives; their internal conditions remain
cumulative where stated. A turnover below USD 80,000 alone does not establish
the small-entity route. Possessing three employees alone does not establish
the substance route. Article 5.2(6) has a specific rule for assets made available
to individuals staying in BES who are not resident there; do not classify every
tourist-use asset as a foreign-use asset without that provision. [B1]; [G-STATUS]

Retain the request, decision, effective period and supporting calculations.
Article 5.2(7) allows the qualifying decision from the start of the first
calendar year specified in the request in which the conditions are met, subject
to its limit of no earlier than 24 months before the inspector receives the
request. This is not automatic retrospective approval or an extension of a
return deadline. Establish the actual decision and period. [B1]

A paragraph 2 or 3 decision lapses immediately after actual BES residence ends,
warehouse admission occurs, or its conditions cease to be met. Warehouse
admission may supply a different statutory route; the lapse does not itself
select the new outcome. Reassess changes in activities, assets, people, premises,
ownership and residence. [B1, article 5.2(4)][B1]

### European Netherlands and other taxes

The European Netherlands Corporate Income Tax Act article 2(9) and Dividend
Tax Act article 1(6) expressly carry the BES residence fiction into their
respective regimes. Determine the legal form, scope, exemptions and any
applicable relief there before computing a liability. This guide does not
supply those regimes' complete profit, loss, deduction, rate or filing rules.
Missing BES approval does not permit a guessed Dutch amount or a BES zero.
[NL-CIT]; [NL-DIV]; [G-FAQ]

The authority explains that BES does not levy the ordinary profit tax replaced
by its distribution/property system. That statement does not exempt an entity
from distribution tax, national property tax, ABB, employer charges, island
levies, foreign obligations or the statutory minimum-tax overlay. Use
`bq-property-tax`, `bq-abb`, `bq-payroll` and `bq-social-contributions` for their
own applicable rules. A sole trader uses `bq-income-tax`. [G-FAQ]; [B1]

Chapter V taxes the defined distribution, rather than an ordinary annual
accounting-profit computation. Do not subtract accounting depreciation,
interest, losses or a generic corporate credit from a declared dividend merely
because those items appear in financial statements. Nor may retained profit be
treated as proof that no deemed distribution or other tax applies. Company-law
distribution capacity and accounting recognition remain separate questions
under `bq-financial-statements`. [B1, articles 5.3–5.8][B1]

## Distributions and exemptions

Article 5.4 includes direct and indirect profit distributions under any name
or form, specified buybacks/liquidation amounts above nominal value, specified
unpaid-capital share issues, capital repayments unless the stated nominal-capital
reduction condition is met, profit-right payments and foundation/fund
distributions. An entry labelled loan, reimbursement or capital repayment does
not establish exclusion. Noncash proceeds use market value at the time made
available. Trace the resolution, rights, capital history, consideration and
valuation before classification. [B1]

Article 5.7 permits withholding to be omitted for its specified categories:

- A qualifying participation held by an entity meeting the stated BES status,
  where it belongs to that entity's BES business assets. Article 5.2(5) imports
  **article 13(2)** of the European Netherlands Corporate Income Tax Act for
  the participation definition. For ordinary shares, that paragraph uses at
  least 5% of nominal paid-up capital; other forms have their own tests. This
  does not import the entire Dutch participation-exemption regime or make the
  separate 50% holding-company status test a dividend exemption threshold.
- Specified foundation/fund distributions for qualifying public/social-benefit
  institutions or purposes within the *Rijk*, with a separate designation route
  for qualifying institutions or purposes outside it. The implementing
  regulation article 5.1 requires a written request and the inspector's
  conditions for that outside-Rijk route. A charitable label alone is
  insufficient.
- Foundation/fund payments qualifying under the specified Wage Tax BES
  article 6A pension arrangement. An ordinary pension label does not settle
  the arrangement's qualification.

[B1, articles 5.2(5) and 5.7][B1]; [NL-CIT, article 13(2)][NL-CIT]; [RULES]

Establish the payer, recipient, status, business-asset relationship and full
exemption conditions before omitting withholding. A foreign shareholder,
connected company or matching tax rate is not by itself an exemption. Treaty
relief, foreign credits, beneficial ownership, pension and nonprofit qualification
remain held until their operative sources and facts are established.

### Foundation withholding requires separate resolution

Article 5.1(1)(c) includes foundation/fund beneficiaries, and article 5.2(1)
excludes those BES-established forms from its ordinary residence fiction.
The authority says they fall within distribution tax without a residence
decision. However, article 5.6(2)'s withholding-agent definition expressly refers
to article 5.2's **second or third paragraphs**. This reference does not resolve
that interaction or infer that every foundation is either exempt or an ordinary
paragraph 2 company. Actual foundation/fund withholding is held for a supported
professional determination. The ordinary NV examples below do not cover it.
[B1]; [G-FAQ]

## Rate, timing and fictional computations

For 2026, article 5.5 sets **7.5% of the distribution**. If the payer bears the
tax, multiply the net amount by `100 / 92.5` to establish the gross base, then
apply 7.5%. Do not apply 7.5% to the desired net amount alone. The authority
records the change from 5% to 7.5% from 1 January 2025; the old percentage is not
a 2026 rate. [B1]; [G-RATE]

Under article 5.6, withholding occurs when proceeds are made available. The
resolution, crediting/set-off, enforceable entitlement and actual payment need
review; a later bank debit is not the sole timing evidence. Where tax exceeds
the cash proceeds, paragraph 5 provides the deemed-withholding and recovery
mechanism, including possible suspension of noncash delivery. This guide does
not compute a noncash or insufficient-cash case. [B1]

These fictional 2026 cases stipulate an ordinary BES NV with an effective
article 5.2(2) decision, continuing qualification, established corporate
distribution capacity, a cash distribution made available, no withholding
exemption or foreign relief, and no other transaction. They do not establish
any real entity's status. [B1]

| Item, USD | Tax withheld from a gross distribution | Payer bears tax on a promised net amount | Second payer-borne case |
|---|---:|---:|---:|
| Stipulated amount | 25,000 gross | 18,500 net | 23,125 net |
| Gross taxable distribution | 25,000 | 20,000 | 25,000 |
| Distribution tax, 7.5% of gross | 1,875 | 1,500 | 1,875 |
| Recipient cash entitlement | 23,125 | 18,500 | 23,125 |
| Total distribution/payable components | 25,000 | 20,000 | 25,000 |

The first arithmetic journal debits the established distribution/equity amount
USD 25,000 and credits recipient liability USD 23,125 plus tax liability
USD 1,875. In the second, total distribution USD 20,000 equals recipient
liability USD 18,500 plus tax USD 1,500. Neither records a completed payment or
prescribes accounting recognition without the applicable framework and evidence.
Payer-borne tax is included in the gross distribution, not added a second time.

The authority's gross-up example for a USD 50,000 desired net amount reports
USD 4,054 tax. The statutory formula produces USD 4,054.054054… before rounding.
This guide neither treats the displayed whole-dollar example as an established
general rounding rule nor silently certifies a cents-based return. The examples
above use exact arithmetic amounts. Actual fractional-cent treatment and return
field rounding remain held. [B1]; [G-RATE]

The recipient's own income-tax or foreign-tax position is separate. Do not
automatically treat withholding as final, deduct it twice, or add a second
unreconciled tax at a matching rate. Establish the applicable income category,
credit and evidence through the recipient's rules and `bq-income-tax`.

## Returns, evidence and changes

Distribution tax uses calendar quarters. Filing and remittance are generally
due within fifteen days after the quarter under articles 8.5 and 8.11. Article
5.6(4) specifically dispenses with the return if **no proceeds were made
available in the quarter**. A distribution with an asserted exemption is not
the same as no distribution. Do not copy the no-return exception into payroll,
ABB, annual accounts or minimum tax. [B1]; [G-FAQ]

Read the actual return invitation, period and any extension. Article 8.11(5)
extends the payment-on-return fifteen-day term by a granted filing extension's
duration. Determine applicable non-working-day rules before producing actual
dates. A residence-decision application does not itself suspend filing or
payment. [B1]

The implementing regulation article 8.2 requires electronic distribution-tax
returns by an administration-obligated person, with its specific waiver route
where electronic filing is unreasonably burdensome. Authority guidance also
offers paper forms. That availability does not prove that a particular company
has an electronic-filing waiver. Establish the actual obligation and authorised
method; the ordinary online route is MijnCN. The reviewer holds identifiers,
access and payment details and performs any filing/payment outside the agent.
[RULES]; [G-FILE]

Article 5.9 requires a dated distribution note when proceeds are paid, credited,
set off or delivered. It identifies issuer and recipient, availability date,
description/amount and tax withheld. Notes must be consecutively numbered,
possibly by series, and duplicates kept for five years in that order, subject
to the stated ministerial waiver power. General tax administration has its own
seven-year duty under article 8.86; company-law retention is separately addressed
in `bq-financial-statements`. The shorter note period does not authorise deletion
of a record still required under another rule. [B1]; [G-FILE]

Reconcile the distribution resolution and valuation to each recipient's note,
gross entitlement, withholding, net payable, general ledger, quarterly return
and authority receipt. Match a remittance to the entity, period and actual
reference. A bank transfer alone does not establish a dividend, deductible
expense or tax payment. Keep unapplied payments and differences visible.

Article 5.8 deems a distribution immediately before the stated loss of
qualification, actual BES residence or BES treaty/arrangement residence. Do not
delay review until cash is paid or a company is formally dissolved. Establish
valuation, rights and the applicable treatment before calculating an exit;
this reference holds actual exit, liquidation and restructuring computations.
Use `bq-formation` and `bq-financial-statements` for separate corporate events
and annual reporting. [B1]

## Minimum-tax screening is a separate obligation

BES chapter VIIb applies the Minimum Tax Act 2024, with its express changes and
exclusions, to the covered BES group entities and defined permanent
establishments. Do not conclude that the absence of ordinary BES profit tax
removes this overlay. The imported law's article 2.1 generally tests consolidated
group revenue of at least **EUR 750 million** in at least two of the four
immediately preceding reporting years, with the stated shorter-history rule,
excluded-entity revenue inclusion and proportional adjustment for non-twelve-month
years. Group restructurings have further rules. [B1, article 7b.1][B1]; [MIN-TAX]

Article 2.2 separately defines excluded entities and qualifying owned entities,
with conditions and an election. A foundation, fund, pension or charity label
does not prove that exclusion. The 15% minimum-tax rate is part of the defined
top-up system, not a flat 15% corporate tax on every BES company's accounting
profit. Jurisdictional income, adjusted covered taxes, exclusions, safe harbours
and elections require their complete applicable rules. This guide supplies no
top-up computation or blanket zero conclusion. [MIN-TAX, articles 1.2 and 2.1–3.1][MIN-TAX]

Keep tax returns/payments separate from the top-up information return and
notification. BES article 7b.2 generally uses a tax-return deadline set no earlier
than seventeen months after period-end and payment within seventeen months.
Article 7b.8 conditionally sets the transition tax-return deadline no earlier
than twenty months after period-end, payment within twenty months, and
information/notification within eighteen months. Paragraph
4 limits that transition route; article 7b.9 adds specific rules for the
specified early-ending years. Establish the entity's reporting year and
complete exceptions before selecting a calendar or treating a deadline as met.
Do not apply distribution tax's quarterly fifteen-day rule here. [B1]

## Completion conditions and self-checks

No missing-fact default is authorised. Unknown residence, decision, continued
qualification, ownership, distribution character, valuation, exemption,
rounding, payment allocation or operative source remains Needs Input or a hold.
Preserve all corporate-base refusal codes and their canonical messages.

This reference does not complete the mandatory slots for European Netherlands
profit taxation, foreign establishments/relief, transfer pricing, group relief,
special sectors, foundation withholding, minimum-tax computation, penalties,
actual forms/rounding or accounting tax provision. A clear scope statement is
not permission to omit a required component of a complete output.

Check the applicable regime before a rate; 50% status versus participation
definition; conjunctive versus alternative conditions; gross versus net promise;
availability versus payment; note/return/ledger reconciliation; no duplicated
recipient credit or payer-borne tax; each retention duty; minimum-tax scope and
separate periods; and all universal/domain outputs. Obtain professional review.
No live taxpayer, portal filing, engagement workbook or professional sign-off
was tested. This guide does not establish comprehensive country coverage.

## Primary sources and read scope

Read on 17 October 2026. The complete BES distribution-tax chapter was read and
compared across the [January][B-JAN], [February][B-FEB] and [April][B1] 2026 texts and a fresh current
capture: after removing explicit interface labels and whitespace, it matches.
Selected general provisions and the complete BES minimum-tax chapter were read.
The European Netherlands Acts were read only for the cited residence and
participation/scope provisions, rather than their entire tax computations.
Current authority pages, including collapsed FAQ answers, were read in full.

The establishment page retains an old 95% discussion before describing its
50% replacement, and its statute link selects 2018. The current statute and
2024-onwards explanation govern this reference's 50% route. Its introductory
residence-request statement must also be read with the statutory warehouse and
foundation exceptions. The FAQ's gross-up sentence visibly retains an old
denominator alongside 92.5; this guide uses article 5.5 and the dedicated rate
page. The published electronic/paper and foundation interactions retain the
specific controls above, rather than being resolved by a simplified summary.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B-JAN]: https://wetten.overheid.nl/BWBR0029244/2026-01-01
[B-FEB]: https://wetten.overheid.nl/BWBR0029244/2026-02-21
[RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[NL-CIT]: https://wetten.overheid.nl/BWBR0002672/2026-01-01
[NL-DIV]: https://wetten.overheid.nl/BWBR0002515/2025-01-01
[MIN-TAX]: https://wetten.overheid.nl/BWBR0049111/2026-04-11
[G-FAQ]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/opbrengstbelasting/veel-gestelde-vragen-en-antwoorden-qa
[G-STATUS]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/opbrengstbelasting/vestigingsplaatsbeschikking
[G-RATE]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/opbrengstbelasting/tarief-opbrengstbelasting
[G-FILE]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/opbrengstbelasting/aangifte-opbrengstbelasting

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
