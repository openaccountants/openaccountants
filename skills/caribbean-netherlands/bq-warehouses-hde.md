---
name: bq-warehouses-hde
description: >
  Analyse 2026 BES customs warehouses and trade-and-services warehouses
  (HDE). Use for operator permits, approved premises/goods, stock control,
  handling, transfers, admission conditions, withdrawal and selected tax
  connections. Separates storage from release, HDE admission from company
  residence, and ABB zero rates from exemptions. Includes primary law,
  delegated controls, authority guidance and fictional boundary cases.
  This source-cited draft holds actual permits, transitional admissions,
  mixed activities, disputed export references and complete tax bills.
  Load with the universal workflow base and BES companions; professional
  review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Selected warehouse/HDE controls checked on 17 October 2026; actual site, admission, permission and operative event required"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-customs-clearance
  - bq-customs-debt-remedies
  - bq-excise
  - bq-abb
  - bq-corporate-tax
  - bq-property-tax
---

# Bonaire, Sint Eustatius and Saba: customs warehouses and HDE

Establish the importing island, actual premises, operator, goods, customs
destination, permit, admission and transaction. Temporary storage (RTO),
customs warehousing, an HDE and an excise goods place (AGP) have different
legal conditions. A commercial warehouse, company registration or HDE
address alone does not establish a permitted customs regime or a tax
exemption. Use `bq-customs-clearance` for RTO and declarations and
`bq-excise` for the separate excise regime. [DAB]; [G-INDEX]

Load `workflow-base` and applicable domain/BES companions. Preserve source
gates, confirmed profile, refusals, four universal outputs and all domain
outputs/checks. This Tier 2 reference covers selected warehouse/HDE controls,
not a complete country pack or engagement. Unknown mandatory conditions
hold the complete financial output package.

## Customs warehouse: operator, premises and goods

DAB 2.99–2.101 distinguish warehouses usable by anyone from those operated
by a manager. The managing person must be BES-established and obtain the
inspector's permit on a written request with the necessary information and
evidence of economic need. Supervision/control must be practicable without
disproportionate administrative measures. A permit is not transferable;
a proposed takeover requires its own request. [DAB]

The inspector approves location, separation and construction before use.
The permit specifies goods, stock-account arrangements, handling,
destinations/terms, supervision and withdrawal conditions. It may prescribe
minimum entry/exit quantities and prohibit retail sale. For a warehouse
used by anyone, decree 2.41 applies specified conditions to the person
responsible under the warehousing declaration. Establish the actual permit
and responsible person; ownership alone is insufficient. [DAB]; [DECREE]

Official closure is the general arrangement. Approved reliance on the
manager's records instead requires adequate administrative safeguards and
security for potential duty. An “open” warehouse still requires customs
declarations and permissions. Article 2.100(2) additionally conditions
storage of excise goods on the chapter-IV rules. Do not infer permission
for every product from an ordinary-goods warehouse approval.
[DAB]; [DECREE]; [G-STORE]

## Movement, handling and records

Decree 2.44 requires destination-office permission for entry and use of
the movement document. Customs checks the seal, non-use and goods identity,
then returns the endorsed copy for discharge. A sale during storage does
not itself release the goods: responsibility stays with the person in
whose name they were stored unless the inspector permits transfer of that
responsibility. Entry, discharge, ownership and liability are separate
events. [DECREE]

The authority's transfer route covers stores on the **same island**,
including customs-warehouse/HDE combinations. It requires the destination
declaration, permissions, direct uninterrupted movement, the required
security, applicable sealing and discharge evidence. Establish an inter-island
export/import route separately; do not treat a same-island movement code as
a universal route between all BES islands. Actual code/form mapping remains
held. [G-MOVE]; [DAB]

Goods normally remain in the state in which they entered. Written request
and inspector permission can authorise handling to preserve condition,
improve presentation/trade quality or prepare distribution/resale.
That is not permission for unrestricted manufacturing, use or consumption;
excise goods have their separate rules. Decree 2.42 separately permits
specified refund/export, temporary-import and free-circulation storage
cases with their conditions. [DAB, article 2.104][DAB]; [DECREE]

The stock administration under decree 2.46 records destination-declaration
references, location, goods identity and handling. Record entry and exit
when they occur and make the remaining goods under the regime identifiable
at all times. Reconcile the physical inventory, goods account, approved
handling, movements and discharges. Customs' periodic control and excess/
shortage treatment are separate from commercial stock accounting. A theft
or insurance entry alone does not establish debt extinction; use
`bq-customs-debt-remedies`. [DAB]; [DECREE]

Decree 2.43(1) prohibits the listed warehouse goods presenting public-order,
safety, environmental, health, veterinary/phytosanitary or intellectual-property
risks. Special storage requirements may also be imposed. Regulation 5.1
applies that decree article correspondingly to HDE and separately prohibits
goods subject to an import/export/transit ban unless exempted. The penalties
reference distinguishes the decree's administrative and criminal provisions;
a same-numbered article in the Act is not interchangeable. [DECREE]; [RULES];
`bq-penalties-corrections`

## Storage term and withdrawal

Article 2.105 provides the general indefinite-storage position with its
specified inspector-set destination-term exception. Establish every actual
permit term; this does not extend RTO's separate clock. Decree 2.45 has
its special-circumstance extension route and deemed-import consequence
after the relevant extended term expires without exit. [DAB]; [DECREE]

Under 2.106, withdrawal can follow request, failed conditions, specified
non-compliance after warning, decisive bad information or cessation of
business. It must be written and reasoned. Goods remaining when the
warehouse permit is withdrawn must receive a further customs destination
within **three days from the withdrawal date**; failure produces deemed
import and regularisation measures. Establish the actual decision, calendar
and exceptions before giving an operational date. This goods rule is
different from HDE's entity-removal rule below. [DAB]

## HDE: area, activities and admission

An HDE requires ministerial establishment and precise site/building
boundaries under DAB 5.3. Entity admission is a separate inspector decision
under 5.4. Article 5.1 equates entry/exit of goods with customs-warehouse
entry/exit for duty and customs formalities; it does not make every
business operating nearby an admitted entity. [DAB]; [G-HDE]

For ordinary admission under 5.4, the applicant is a legal person with
share capital, with the stated HDE goods activities or qualifying services.
Article 5.2 defines those services, including specified repair/maintenance
and non-BES-directed international activities. Its exclusions include
financial services, royalty payments, insurance/reinsurance, management/
trust business and the named notarial, legal, public-accountancy, tax-advisory
and similar professional services. An accounting or advisory business is
not admitted merely because it serves foreign clients electronically. [DAB]

Unless a 5.8 permit applies, turnover from the stated activities must be
earned from non-BES resident/established persons or another HDE business.
The economic-development condition and each relevant statutory requirement
must be established; a projected turnover figure alone is insufficient
evidence of the permit or continuing conditions. [DAB]

| Article 5.4(2) requirement | Stated condition; actual application/admission still required |
|---|---|
| Services activity | Annual turnover at least **USD 80,000**, under the specified services branch. |
| Goods activity | Annual turnover at least **USD 800,000**, under the specified storage/processing/handling branch. The services and goods alternatives are not a single combined-turnover shortcut. |
| Employment | Permanent full-time work for at least **three BES-resident natural persons**. Do not round a headcount or assume part-time aggregation satisfies this text. |
| Admission investment | At least **USD 500,000**, such as business buildings, initial fitting-out or other qualifying investment. Establish its actual connection and evidence. |

[DAB]

Keep the ordinary admission branch separate from pre-existing permits,
saved-law cases and mixed activities whose method is not established here.
Use `bq-tax-system` for the need to examine transition provisions. The
HDE services **floor** of 80,000 is not the corporate small-body **ceiling**
of 80,000 under B1 5.2(2)(a); satisfying one amount comparison does not
establish the other regime. [DAB]; [B1]

Other/local deliveries and services require the inspector's written-request
permit under 5.8, with its term, conditions, possible refusal for the stated
socio-economic interest and withdrawal. Admission does not itself permit
unrestricted domestic trading. Under 5.5, withdrawal can have the specified
retroactive effect. Entity removal is required within **six months from
the dated withdrawal decision**, with immediate removal at its cost if
that term is not met. Do not use six months as the stock's automatic
untaxed-stay period. [DAB]

DAB 5.10 applies Belastingwet chapter VIII correspondingly to sections
1–4, without prejudice to customs chapters II and III. The precise decision
and legal route matter; do not copy a general remedy/collection term to
every HDE permission. Retain the actual decision and professional review.
[DAB]

## Separate tax connections

B1 5.2(3)(a) excludes an admitted HDE body from the chapter's deemed-European-
Netherlands residence rule. Paragraph 3(b)'s qualifying holding-company
route instead needs its own inspector decision and the stated participation/
asset conditions. Establish actual residence, admission and applicable
taxes with `bq-corporate-tax`; this is not blanket immunity from distributions,
payroll, minimum tax or foreign taxing rights. [B1]

B1 4.8(2) excludes property enjoyed through the named rights by an admitted
HDE entity from the stated improvement-value delay. Paragraph 3 has the
valuation-date transition at 1 January 2025. Identify the actual rights and
liable person; an HDE tenant's presence does not alone classify every
landlord's property. Apply `bq-property-tax` and relevant island charges
separately, with no automatic property-tax exemption. [B1]

For ABB, 6.17 distinguishes free-circulation/regime-ending imports from
its specified non-import regime/HDE movements. Its excise-goods paragraph
and AGP interactions need their own analysis; this guide does not determine
AGP ABB timing. B1 6.10(2)(d) lists specified zero-rated producer/export/HDE
goods supplies, while 6.11(1)(t)–(v) lists the particular HDE service and
input-supply exemptions. Operator activity, supplier/recipient, goods use,
destination and records matter. Zero rating, exemption, non-import and
input recovery are distinct; use `bq-abb` for the actual transaction. [B1]

The saved current texts leave an export-reference mismatch: tax regulation
6.6(1)'s goods zero-rate evidence clause and customs regulation 3.15(1)(a)'s
same-island re-import clause point to B1 6.10(2)(c), while the current Act
puts the specified producer/export/HDE goods branch in **(d)** and uses
**(c)** for the specified cars/vans without CO2 emissions. Keep the texts separate and
hold actual zero-rate/re-import application until the legal mapping is
verified. Do not silently change the delegated references. General exemption
records remain required under tax regulation 6.7(1). [B1]; [TAX-RULES]; [RULES]

The reviewed February 2026 correction concerns the ABB small-entrepreneur
threshold and other named matters; it does not amend these export pointers.
That examination is not proof that every other amending or interpretive
authority has been exhausted. The discrepancy and actual-application hold
also appear in `bq-personal-import-relief` and `bq-abb`. [CHANGE2026]

## Fictional boundary and stock checks

These cases stipulate the named ordinary branch and remaining verified
facts. They test components, not actual admission, tax relief or a bill:

| Stipulated facts | Component result |
|---|---|
| Services-only HDE application: annual turnover 79,999 versus 80,000 | The first is below the services floor; the second meets only that amount condition. |
| Goods-only application: 799,999 versus 800,000 | The first is below the goods floor; the second meets only that amount condition. |
| Relevant investment 499,999 versus 500,000 | The first is below the stated floor; the second meets only that amount condition. |
| Turnover meets the amount rule but required employment evidence is absent | Hold admission; neither an amount nor a company registration supplies the missing condition. |
| A permit is withdrawn and an HDE entity has six months to remove itself | Do not treat that as permission for goods to remain outside customs destination requirements for six months. |
| Goods change commercial owner while in the warehouse | Retain the existing named responsibility until inspector-approved transfer; sale does not establish release. |
| Stock starts at 100 units, with 20 evidenced exits and no other movements | Expected remainder is **100 − 20 = 80**. If physical stock is 79, investigate/reconcile the difference of **1**; do not invent a tax-free loss. |
| A warehouse/HDE address is supplied without the actual permit/admission | Hold regime treatment; do not infer a tax status from the address. |
| Export/re-import relief is requested using only the mismatched letter pointer | Preserve the source discrepancy and hold the actual treatment; do not select a favourable reading by default. |

## Verification and limits

Check actual operator/person, approved premises/goods, permit and admission;
stock evidence, movement permissions and discharge; permitted handling,
security and responsibility; period/withdrawal events; each HDE activity,
customer, turnover, job and investment condition; and separate tax/legal
bridges. Retain Needs Input/holds, evidence references and all workflow
outputs. The practitioner keeps original authorities, identities, tax
identifiers and bank details outside the agent.

Read on 17 October 2026: DAB 2.98–2.106 and 5.1–5.10; decree 2.40–2.46;
regulation 5.1 and 3.15; B1 4.8, 5.2, 6.10, 6.11 and 6.17; tax regulation
6.6–6.7; four complete storage/transfer authority pages; and the complete
February 2026 correction in HTML. Earlier declaration, debt, excise and
penalty provisions remain in their separate companions.

Actual site boundaries and permits, transitional/mixed admissions,
restricted-goods classification, unresolved export/re-import references,
AGP interactions, full tax calculations, external annexes/forms and live
operational cases are not completed. No private records, identity/tax
identifier or bank submission, admission/permit application, declaration,
payment, engagement workbook, PDF/OCR or practitioner sign-off was used.
No comprehensive-area credit is claimed.

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[DECREE]: https://wetten.overheid.nl/BWBR0029262/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[TAX-RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[G-STORE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/opslag-van-goederen/opslag-in-een-douane-entrepot
[G-HDE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/opslag-van-goederen/opslag-in-een-handels--en-dienstentrepot-hde
[G-MOVE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/douanebestemmingen/douane-entrepot-of-handels--en-dienstenentrepot-hde
[G-INDEX]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-bedrijven/invoer-doorvoer-en-uitvoer/opslag-van-goederen
[CHANGE2026]: https://zoek.officielebekendmakingen.nl/stcrt-2026-3708.html

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
