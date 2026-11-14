---
name: bq-transfer-tax
description: >
  Analyse 2026 transfer tax in Bonaire, Sint Eustatius and Saba. Use for
  property and registered-ship acquisitions, market values, consideration,
  exemptions, recent transfers, divided ownership, notarial deeds and
  registration evidence. Explains the statutory five-percent charge, separate
  transfer and annual-property bases, ABB interaction and document deadlines.
  Includes primary legislation, current authority guidance and conditional
  arithmetic examples. Distinguishes inheritance context from a completed estate
  tax analysis. This source-cited draft holds complex partitions, valuations,
  actual exemption eligibility, monetary rounding, payment calendars and
  return mapping. Load with the universal workflow base; professional review
  and confirmation of each transaction remain required.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 transfer-tax reference; instrument, acquisition and registration dates established separately"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - bq-property-tax
  - bq-abb
---

# Bonaire, Sint Eustatius and Saba: transfer tax in 2026

Establish the island, asset, legal right, parties, acquisition instrument,
effective event and valuation before computing transfer tax. The 5% rate does
not establish the taxable base or an exemption. An annual property-tax value
and a recent acquisition price are evidence to examine, rather than automatic
substitutes for the transfer's statutory market value.

Load `workflow-base` and preserve its intake, source gates, profile confirmation,
refusals, four universal outputs, recalculation and professional review. This
Tier 2 reference explains selected transfer rules and conditional arithmetic;
it does not certify a complete transaction, estate or country pack. Unfilled
mandatory country slots hold the complete financial output package.

## Assets and chargeable events

Belastingwet BES chapter VII taxes acquisitions by natural and legal persons.
Article 7.1 covers BES immovable property and the rights burdening it, and
ships registered in BES with gross volume of at least **20 cubic metres**.
The authority's short summary says registered ships; the statutory definition
supplies this size condition. Establish classification before treating any
boat, share or financing instrument as chargeable. [B1]; [G-SCOPE]

The transfer definition includes the specified creation, surrender and
termination of usufruct, use, habitation, easements, long lease, superficies,
ground rents and recovery/transfer actions. A transaction need not be an
ordinary freehold sale. Article 7.3(2) also treats the stated contribution by
a limited partner to an open limited partnership with shares as a transfer.
Articles 7.6–7.11 have separate community/partition/share rules. Do not assume
that a company-share label proves either a property acquisition or exemption.
[B1, articles 7.1–7.3 and 7.6–7.11][B1]

Article 7.2 requires the stated entity formations involving contributions of
property or ships to use a BES authentic deed, on pain of nullity. That legal
formality is separate from tax exemption and from the general civil-law rules.
Use `bq-formation` where an entity is being formed; do not treat this tax
reference as authority to draft or execute the instrument. [B1]

## Base, rate and recent transfers

Articles 7.12–7.13 impose **5% of market value**, with the value at least equal
to the consideration. An undervalue sale to a relative does not reduce the base
to the stated price. Conversely, do not disregard consideration above the
established market value. Establish the actual consideration, obligations,
rights and any separately acquired movables, with defensible valuation
evidence. Debt, land rights, noncash consideration and mixed assets need their
complete analysis before an actual base is selected. [B1]; [G-SCOPE]; [G-RATE]

For another transfer of the same property or ship **within six months**,
article 7.14 reduces value by the amount over which transfer tax or qualifying
ABB was due on the previous transfer by another person. For ABB, the rule
excludes the extent deductible or potentially deductible under article 6.3(a).
It reduces the base by an evidenced prior taxable amount, rather than granting
a second credit for all earlier tax or the earlier price. Establish asset
identity, dates, earlier liability/base and the ABB recovery position. The
wording concerns tax that was due; payment evidence alone cannot establish or
replace that legal condition. [B1]

The following fictional ordinary acquisitions stipulate a chargeable BES
freehold transfer, established market value and consideration, no exemption,
and no other base adjustment. The third case additionally stipulates a prior
transfer by another person of the same property within the statutory six-month
window, with an established USD 200,000 prior transfer-tax base. No other
transaction, liability or rounding rule is inferred. [B1]

| Item, USD | Price below market value | Price above market value | Qualifying recent transfer |
|---|---:|---:|---:|
| Established current market value | 300,000 | 300,000 | 230,000 |
| Established current consideration | 250,000 | 320,000 | 230,000 |
| Value before article 7.14 | 300,000 | 320,000 | 230,000 |
| Stipulated qualifying earlier taxable amount | 0 | 0 | 200,000 |
| Conditional current taxable base | 300,000 | 320,000 | 30,000 |
| Transfer tax at 5% | 15,000 | 16,000 | 1,500 |

These are arithmetic component checks, not an engagement conclusion. The
third case does not select treatment where the reduction exceeds current
value, prove the six-month date calculation, or settle a partial/mixed asset
or recoverable-ABB case. No negative base, refund or carried-forward reduction
is invented. No annual-property tax, notarial charge, cadastral fee or purchase
cost is included in the transfer-tax amount.

## Exemptions and ABB

Article 7.4 lists exemptions subject to its ministerial conditions/limits.
The authority's exemption page gives examples, rather than the complete tests.
Keep the legal category and evidence identifiable. [B1]; [G-EXEMPT]

| Statutory category | Condition or limit to establish |
|---|---|
| State/public body and specified wholly public-owned entities | The written non-competing-use declaration and the five-year change-of-use charge in article 7.4(1)(a), including indirect ownership where applicable. |
| Mixing of estates/property communities | The actual article 7.4(1)(b) event; no general exemption for every change in co-ownership. |
| Division of matrimonial community or estate | Acquirer's status as the entitled successor under article 7.4(1)(c). A purchase from an heir is not established as this division merely by that label. |
| Business contribution to a partnership/company | Actual business contribution within article 7.4(1)(d), with applicable conditions, rather than any isolated property contribution. |
| Other community divisions | Proven community/title and the limits in article 7.4(1)(e) and (2); the specialised articles 7.6–7.11 must be read where applicable. |
| Specified death-related agreement between co-owners | Article 7.4(1)(f) and 7.11 conditions, including absence of agreed compensation where required. |
| Newly manufactured building/work and related land | Article 7.4(1)(g), article 6.4(1)(f) and implementing regulation article 7.1: exemption applies only insofar as ABB is due on the delivery. |

The new-building exemption requires an established ABB charge. A new property,
an invoice mentioning ABB, an ABB-exempt transaction or an unverified supplier
classification does not alone establish relief. Apply `bq-abb` for the actual
delivery and liability, and retain its source conditions. This exemption and
article 7.14's earlier-transfer base reduction are different rules; do not
apply both automatically to the same amount. [B1]; [RULES]

Articles 7.5–7.11 address unproven communities, contributed assets, earlier
taxed interests, repeated divisions, transfers between co-owners and exit/death
agreements. Evidence of original contribution, succession, consideration and
previous tax matters. This reference holds actual complex partition, business
contribution and death-agreement computations; it does not replace their
special bases with the ordinary table above. [B1]

## Registration, return and payment evidence

The acquirer is the taxpayer under article 7.15; article 7.16 uses payment on
return. Where a notarial deed exists, implementing regulation article 8.3
provides for filing by offering the deed for registration. The prescribed
signed declaration identifies tax due and the specified separately acquired
movables/consideration information; relevant information may be in the deed
or signed annex under paragraph 2. Paragraph 3 permits an electronic deed copy
with the authority's cover sheet replacing that declaration. Registration of
the instrument is not by itself proof that every tax component was paid.
[B1]; [RULES]

The registration regulation supplies separate document deadlines. Count the
specified starting day out. Article 22 extends a last day falling on Saturday,
Sunday or a day legally equated to Sunday to the next working day. Establish
the actual instrument and applicable holiday calendar; do not assume every
deadline is fifteen days after a quarter. [REGISTRATION, articles 4–7 and 22][REGISTRATION]

| Instrument/event | Registration term under article 6 |
|---|---|
| Ordinary notarial deed, excluding paragraph 5's special documents | Within eight days after the deed date. |
| Covered judgment | Within eight days after the judgment date. |
| Bailiff's deed | Within four days after its date. |
| Foreign-made deed concerning a taxable transfer | Within three months after the deed date. |
| Stated wills and related documents after death/declaration of presumed death becomes known to the notary/custodian | Within thirty days, subject to the paragraph 5 territorial/residence conditions. |
| Other specified private/foreign instruments | Paragraph 6 gives no term for those outside paragraphs 4–5, but imposes registration before the specified official use. This is not a general exemption from registration. |

Articles 7–12 assign duties to the relevant notary, registrar and bailiff,
restrict specified use of unregistered documents, preserve exceptions, and
require a repertory with quarterly endorsement within the first ten days.
These professional record duties do not require an agent to collect private
wills, identity documents or legal originals. The reviewer/notary retains them
and supplies stable references and status confirmation. [REGISTRATION]

Tax remittance has its own governing provisions in articles 7.16–7.18 and
8.11; the filing-by-registration rule must be read with the actual instrument
and procedure. Article 7.22 permits the notary to require sufficient funds or
security before acting and imposes a specified deposit duty for judgment cases.
Do not treat money held by a notary as an authority receipt or invent a
quarterly payment calendar. This reference holds the actual remittance calendar
and field mapping until the applicable procedure is established. No payment,
deed execution or filing is authorised. [B1]; [RULES]; [G-RATE]

Reconcile the signed acquisition instrument, asset/right, consideration,
valuation, exemption or earlier-base evidence, return declaration/cover sheet,
registration number/date, notary settlement, tax liability and authority receipt.
Allocate mixed movables/property and fees explicitly. A bank debit or aggregate
notary payment alone does not establish the transfer-tax base or remittance.

## Conditions, refunds and collection

For an acquisition under a suspensive condition, article 7.17 allows the
acquirer to choose satisfactory security instead of the specified payment.
Proof that the condition was not met supports the stated release/refund route
on request. Do not treat a disputed contract or incomplete conveyance as an
automatic zero or refund. [B1]

Article 7.19 provides specific refund grounds and a supported written request
to the inspector, who decides by an objectionable decision. Articles 7.20–7.21
contain separate priority/collection periods, including the special rules for
unregistered deeds and judgments. A collection period is not an ordinary
return deadline or permission to destroy records. Actual refund amounts,
penalties, interest, objections and time-bar conclusions require their full
applicable procedural branch; they are held here. [B1]

## Estate context and completion conditions

The government's 27 June 2025 letter explains that the earlier profit and
succession taxes ceased in 2011 while transfer tax was retained. It also
discusses proposals for future reform. That historical explanation does not
establish a zero result for every 2026 inheritance, gift, foundation payment
or foreign-resident connection. A transfer-tax exemption for an estate division
does not establish inheritance/succession-tax treatment. This guide does not
complete the estate or cross-border analysis. [LETTER]; [B1]

No missing-fact default is authorised. Unknown title, asset, event, dates,
value, consideration, earlier liability, ABB recovery, exemption, rounding or
source condition remains Needs Input or a hold. Do not turn a missing valuation
into the purchase price or an unsupported exemption into zero.

Check scope before rate; market value and consideration; prior taxable amount
versus earlier tax; ABB due versus deductible; each exemption's full conditions;
ordinary acquisition versus partition; deed registration versus payment;
official receipts; event-specific dates and non-working days; and all universal
outputs and reviewer questions. No live conveyance, portal, engagement workbook
or practitioner sign-off was tested. This guide does not establish comprehensive
country coverage.

## Primary sources and verification scope

Read on 17 October 2026. The complete transfer chapter, articles 7.1–7.24,
matches the [January][B-JAN], [February][B-FEB] and [April][B1] 2026 versions
and the fresh current capture after explicit interface-label/whitespace removal.
The registration regulation was read in full. General implementing regulation
articles 7.1 and 8.3, relevant general-law provisions, the authority's overview,
rate and exemption pages, and the 2025 government letter were read. This does
not claim an exhaustive civil-law, estate, foreign-tax or historic review.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[B-JAN]: https://wetten.overheid.nl/BWBR0029244/2026-01-01
[B-FEB]: https://wetten.overheid.nl/BWBR0029244/2026-02-21
[RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[REGISTRATION]: https://wetten.overheid.nl/BWBR0029296/2011-01-01
[G-SCOPE]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/overdrachtsbelasting
[G-RATE]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/overdrachtsbelasting/tarief-overdrachtsbelasting
[G-EXEMPT]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-bedrijven/overdrachtsbelasting/vrijstelling-overdrachtsbelasting
[LETTER]: https://zoek.officielebekendmakingen.nl/kst-32893-7.html

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
