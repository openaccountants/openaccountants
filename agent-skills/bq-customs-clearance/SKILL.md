---
name: bq-customs-clearance
description: "Analyse 2026 BES customs entry, destination declarations, temporary storage, acceptance, release, corrections and document discharge. Use for ordinary commercial sea or air consignments, authorised representation, evidence, separate procedural clocks and specified customs service or storage fees. Includes primary legislation, delegated controls, current authority guidance and fictional boundary cases. Separates declarations from relief eligibility and inspector permissions from automatic rights. This source-cited draft holds special craft, restricted goods, actual code mapping, forms, debt, appeal and unresolved operational cases. Load with the universal workflow base and BES tax references; professional review remains required before reliance."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bq-customs-clearance"
  jurisdiction: "BQ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bonaire, Sint Eustatius and Saba: customs clearance

> **Built from the law. Not yet approved.** Written by Ryan Duguid and imported from his fork; conformed to the OpenAccountants standard by Claude. Not reviewed by an accountant. All outputs must be reviewed by a qualified tax professional before filing or payment. Tax year 2026. Currency: US dollars (USD).

## Scope

Establish island, goods, conveyance, person, representation, arrival,
customs destination and actual permissions before selecting a procedure.
Pre-arrival notice, entry clearance, a destination declaration, acceptance,
release and discharge of a movement document are different events. Nil
import duty does not dispense with them or with ABB/excise. Use
`bq-customs-valuation`, `bq-abb` and `bq-excise` for the separate charges.
[DAB, articles 2.10–2.45][DAB]

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, confirmed profile, refusals, four universal outputs and all domain
outputs/checks. This Tier 2 reference covers selected ordinary commercial
clearance controls. Unknown mandatory conditions hold the complete financial
output package; no complete engagement or country pack is certified.

## Ask the client first

1. **How the goods arrive**: by sea or air, voyage or flight duration, and the arrival date and time.
2. **Who declares**: the importer, or an authorised representative, and their permissions.
3. **Where the goods are stored before release** (a temporary storage facility, RTO) and since when.
4. **Which documents are complete** and which are missing at declaration.
5. **Whether the goods are a personal consignment** or a commercial one.

## The method, step by step

### Person, authority and documents

A declarant must be able to present the goods and required documents.
Article 2.27 normally requires BES residence/establishment, with specified
export, temporary-import and occasional-declaration exceptions. Article 2.5
distinguishes direct representation, in another's name/account, from
indirect representation, in the representative's name for another's account.
The representative must state the capacity and have authority; falsely
claiming authority can result in being treated as acting for oneself.
A tool account, client instruction or transport invoice alone does not
establish the statutory capacity. [DAB]

The licensed customs-forwarder regime in article 2.6 has its own admission,
domicile, security and itemised-invoice conditions. Neither permission to
prepare a calculation nor access to an electronic system grants that status.
Keep actual authority and professional eligibility with the responsible
practitioner. [DAB]; [RULES, article 2.6][RULES]

Electronic declarations are the general rule, with prescribed or authorised
alternatives. Written declarations require the prescribed form, complete
truthful information, date and signature. Dutch is the default declaration
language, subject to article 2.32's document/international-form exception;
the separate English/Spanish/Dutch supporting-document rule is not a blanket
right to file in any of those languages. Keep invoice/value evidence,
transport documents, packing information and required permits identifiable.
[DAB, articles 2.29–2.36][DAB]; [DECREE, article 2.13][DECREE]

Regulation articles 2.28–2.32 govern completed forms, permission for automated
copies, electronic registration, attachments and records. The authority
describes Asycuda World and its manifest/declaration modules, with registration
and applicable exceptions. That public description is not verification of
the current client, every supported procedure or an actual user's access.
No software, authorisation form or account was installed or submitted here.
[RULES]; [ONLINE]; [DECL]

### Keep the clocks separate

The following rules concern ordinary commercial craft/consignments outside
the special exceptions. Establish the actual office calendar, local time,
written permission and notices. These are not one universal import deadline.
[DAB]; [RULES]

| Event | Ordinary rule and specific condition |
|---|---|
| Pre-arrival notice, sea | At least **24 hours before expected arrival**. If the voyage is shorter, no later than departure for the BES destination. |
| Pre-arrival notice, air | At least **12 hours before expected arrival**. If the flight is shorter, no later than departure. |
| Arrival notification | The captain/commander promptly notifies the inspector of arrival under regulation article 2.8(9). Prior notice is not that arrival notification. |
| Entry-clearance declaration | Normally within **six hours after arrival**, subject to the office-closing and immediate-clearance provisions below. |
| Destination declaration outside temporary storage | As soon as possible, no later than **twice 24 hours after submission of the entry declaration**. A justified inspector-approved extension is at most two days. |
| Destination for goods in temporary storage | **21 days after submission of the entry declaration**. A justified written request can obtain an extension to **at most 30 days total**. |

[RULES, article 2.8][RULES]; [DAB, articles 2.12 and 2.15][DAB]; [PRE]; [ENTRY]

Regulation article 2.8(12) addresses arrival within six hours before office
closing or after closing: entry clearance can/must, as specified, occur
on the next working day **before 10:00**. The inspector may instead demand
immediate clearance under paragraph 13. The authority entry page points
to paragraph 6 for the closing-time rule; in the reviewed current regulation,
paragraph 12 supplies it. Use the operative provision and actual notice,
not the stale cross-reference or an assumed general holiday extension.
[RULES]; [ENTRY]

Special craft, emergency/salvage movements, postal goods and travellers have
their own provisions. In particular, regulation article 2.8(6) and article
2.14(5) contain competing pre-arrival cross-references concerning exempt
craft; the authority's notice exemption list does not include pleasure
craft. This reference does not resolve a recreational-craft notice exemption
from those provisions. Hold actual special-craft treatment for authoritative
clarification rather than applying the commercial table or assuming no
notice. [RULES]; [PRE]

### Temporary storage, unloading and release

Unloading requires the prescribed place/time, permission and supervision,
with the specific emergency rule and notification. An unloading permission's
maximum period is not the destination-declaration period. A temporary store
(RTO) needs an approved location, management permit and security. The
manager's assumption of potential liability and the goods' in/out records
are separate from the owner's invoice and from a final import declaration.
[DAB, articles 2.11–2.16][DAB]; [RULES, articles 2.20–2.27][RULES]; [STORE]

RTO goods normally undergo only authorised treatments needed to preserve
their unchanged state. Transfer to another RTO requires the prescribed
manifest and assumption of liability. It **does not suspend or reset the
original storage clock**. If no permitted destination is given within the
applicable term, regulation article 2.25 deems import and provides recourse
to the manager's security. Establish the actual tax/debt branch separately;
do not assume the nil duty tariff removes every consequence. [RULES]; [STORE]

Acceptance registers the declaration. It does not itself release goods.
Article 2.42 separately requires completion of controls and destination
conditions, payment or required security, necessary permits and no established
infringement, with its conditional-release provisions. A green electronic
selection or an invoice marked paid does not establish every condition or
an unconditional right to remove goods. Post-release control remains possible
under article 2.45. [DAB]; [ONLINE]

### Incomplete declarations, correction and document discharge

An incomplete or simplified declaration requires inspector permission and
security. Decree article 2.11 requires minimum identity/description/value
information and sets an inspector-assigned completion period **no longer
than one month after acceptance**. Its replacement/completion rule preserves
the original acceptance date for the stated debt/formality purposes. A
commercial document accepted as a simplified declaration still needs the
required supplementary information. Missing data does not create a general
right to clear goods. [DAB, article 2.35][DAB]; [DECREE, articles 2.11–2.12][DECREE]

Keep these different correction and document routes distinct:

| Provision | Conditions and limit |
|---|---|
| Decree 2.9: amend an accepted declaration | Request and inspector permission; unavailable under this route after notice of intended control or discovery of incorrect/incomplete entries. |
| Decree 2.24: extend a document | Reasoned request received before expiry, goods still present and inspector permission. |
| Decree 2.22: revive an expired document | Goods still present, reasoned request within **60 days after expiry**, and inspector permission. It is not an automatic extension. |
| Decree 2.23: invalidate wrong-destination document | Request within **15 calendar days after acceptance**, unused goods, proven original eligibility/intended alternative destination and immediate new declaration, subject to inspector conditions. This is not a generic appeal deadline. |

[DECREE]

For a movement or temporary-import document, the responsible person must
obtain discharge using the endorsed destination/receipt evidence. Under
article 2.44, missing or incomplete return evidence leads to notice and a
separate **four-week** opportunity to establish the proper destination or
loss before the document is treated as wholly/partly undischarged. Decree
article 2.25 specifies assumption of liability, endorsement and complete or
partial discharge. Proof of a transport booking is not proof of discharge.
Actual debt, recovery and remedies require their complete separate branch.
[DAB]; [DECREE]

## Worked cases

### Fictional control cases

These cases stipulate ordinary commercial scope, no special exemption,
established permissions and the stated calendar/billing facts where needed.
They test procedural components, not actual clearances. [DAB]; [DECREE]; [RULES]

- A 30-hour sea voyage uses the 24-hour pre-arrival lead time. A three-hour
  sea voyage and a four-hour flight require notice no later than departure.
- Filing the entry declaration does not also establish the destination
  declaration or permission to remove goods. Its six-hour clock and the
  ordinary 48-hour destination clock have different starting events.
- Moving stock to a second RTO does not restart its 21 days. An approved
  30-day total does not grant another 30 days after the ordinary term.
- An accepted incomplete declaration does not authorise indefinite missing
  documents or change its original acceptance date merely on replacement.
- An amendment requested after announced control cannot use decree 2.9;
  later remedies must be established rather than invented.
- Goods present after document expiry require the revival route and its
  conditions, rather than a retrospective automatic extension.
- Qualifying government storage of 1.01 cubic metres for one complete
  chargeable billing day and part of another uses two cubic metres and two
  days: **2 × 2 × 20 = USD 80**. Actual billing-day definition is stipulated.
- A qualifying 60-minute official operation, with travel separately excluded
  and established third-party charges of 7, produces **2 × 10 + 7 = USD 27**.
  It does not establish a fee for ordinary work outside the listed categories.
- A personal consignment qualifying for the oral form at 1,500 does not
  thereby qualify for a 1,500 tax exemption.

### Recomputed cases

**Case 1, government storage fee.** Qualifying government storage of 1.01 cubic metres for one complete chargeable day and part of another counts as two cubic metres and two days at USD 20: USD 80.

```oa-check
name: Government storage fee, part units rounded up
inputs:
  cubic_metres: 1.01
  days: 1.5
  rate: 20
steps:
  - billed_m3: ceil(cubic_metres)
  - billed_days: ceil(days)
  - fee: billed_m3 * billed_days * rate
expected:
  billed_m3: 2
  billed_days: 2
  fee: 80
```

**Case 2, official operation fee.** A qualifying 60-minute official operation with travel excluded is charged as two half-hours at USD 10, plus established third-party charges of USD 7: USD 27.

```oa-check
name: Official operation fee with third-party charges
inputs:
  units: 2
  unit_fee: 10
  third_party: 7
steps:
  - fee: units * unit_fee + third_party
expected:
  fee: 27
```

## When to refuse or refer

| Code | Situation | Action |
|---|---|---|
| R-BQ-CC-SPECIAL | Special craft, restricted or prohibited goods | Refer to the Belastingdienst Caribisch Nederland customs desk |
| R-BQ-CC-DEBT | A customs debt, penalty or appeal has arisen | Refer to `bq-customs-debt-remedies` |
| R-BQ-CC-CODES | Actual declaration codes and form fields are needed | Refer: code mapping is not confirmed |

## Filing and payment

### Fees, receipts and declaration codes

Customs service costs arise in the specific decree article 2.1 categories,
such as requested work outside normal hours/places, specified information
or document work, supervision and other listed operations. Regulation
article 2.1 sets **USD 10 per half-hour** of official work and actual
third-party charges; official travel time is excluded. This is not a flat
fee for every import, and no fractional-half-hour billing method is inferred
here. [DAB, articles 2.2–2.3][DAB]; [DECREE]; [RULES]

Government-managed temporary/customs storage has the separate regulation
article 2.2 tariff of **USD 20 per cubic metre per day**, with partial cubic
metres and partial days counted whole. Do not impose this statutory tariff
on every private store or agent. Establish the actual chargeable facility,
volume, billing period, decision and any additional costs. [RULES]

Regulation article 2.34 prescribes the payment receipt's debtor, goods,
base/quantity, tax type/amount and import-date information. Reconcile the
taxes, authorised credit/security, fees, declaration, release and receipt
as separate records. A form or procedure code does not prove substantive
relief eligibility. [RULES]

The public declarations page gives inconsistent field-37 examples: one
separates a four-digit procedure and three-digit APC, another combines them
differently. Its household-effects example is not authority to choose a
relief code for an unverified case. Actual maintained form/code instructions,
permissions and relief evidence must be established before mapping or
submission; code selection remains held here. [DECL]

Regulation article 2.33 allows specified oral-declaration branches, including
traveller-accompanied personal goods up to **USD 1,500** and
traveller-accompanied other goods up to **USD 1,000**, subject to the inspector's ability to require electronic or
written filing. These concern declaration form, not tax-free allowances.
Special postal/gift and traveller relief is not completed here. [RULES]

## Completion checklist

### Verification and limits

Check the responsible person and actual authority; route and craft scope;
notice/arrival/declaration clocks; actual office calendar; permitted storage
and unchanged original clock; acceptance versus release; required security
and permits; amendment versus extension/revival/invalidation; discharge;
fee category and units; tax receipt; and actual code/relief evidence.
Keep unknown mandatory conditions as Needs Input or holds with all workflow
outputs and reviewer questions.

Read on 17 October 2026: customs-law articles 2.1–2.50; decree article 2.1,
2.9–2.13 and 2.21–2.25; regulation articles 2.1–2.34; and five complete
authority pages. Other customs debt, collection, penalties, appeal,
enforcement, controlled-goods, origin/AEO and relief branches, external form
annexes, client software, actual code mapping and live operating cases were
not completed. Special-craft uncertainty remains explicit. The practitioner
retains identities, original authorities, tax identifiers and bank details
outside the agent. No submission, registration, payment, licence, actual
engagement workbook or practitioner sign-off was used. No comprehensive-area
credit is claimed.

## Sources

| Source | URL | Read on |
|---|---|---|
| DAB. Read for the provisions this skill cites as [DAB]. | https://wetten.overheid.nl/BWBR0029236/2025-01-01 | 2026-10-17 |
| DECREE. Read for the provisions this skill cites as [DECREE]. | https://wetten.overheid.nl/BWBR0029262/2025-01-01 | 2026-10-17 |
| RULES. Read for the provisions this skill cites as [RULES]. | https://wetten.overheid.nl/BWBR0029309/2025-01-01 | 2026-10-17 |
| PRE. Read for the provisions this skill cites as [PRE]. | https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/binnenbrengen-en-lossing-van-goederen/pre-arrivalmelding | 2026-10-17 |
| ENTRY. Read for the provisions this skill cites as [ENTRY]. | https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/binnenbrengen-en-lossing-van-goederen/verklaring-tot-inklaring | 2026-10-17 |
| DECL. Read for the provisions this skill cites as [DECL]. | https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/douaneaangiften | 2026-10-17 |
| ONLINE. Read for the provisions this skill cites as [ONLINE]. | https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/online-aangifte-douane | 2026-10-17 |
| STORE. Read for the provisions this skill cites as [STORE]. | https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/opslag-van-goederen/opslag-in-een-ruimte-voor-tijdelijke-opslag-rto | 2026-10-17 |

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[DECREE]: https://wetten.overheid.nl/BWBR0029262/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[PRE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/binnenbrengen-en-lossing-van-goederen/pre-arrivalmelding
[ENTRY]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/binnenbrengen-en-lossing-van-goederen/verklaring-tot-inklaring
[DECL]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/douaneaangiften
[ONLINE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/online-aangifte-douane
[STORE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/opslag-van-goederen/opslag-in-een-ruimte-voor-tijdelijke-opslag-rto

Not yet confirmed: actual office hours and their effect on the clocks; the definition of a chargeable billing day (stipulated in the cases); declaration code and form-field mapping; the restricted-goods regimes. Sources were read by Ryan Duguid on 2026-10-17 and not re-opened on import.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bq-customs-clearance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bq-customs-clearance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
