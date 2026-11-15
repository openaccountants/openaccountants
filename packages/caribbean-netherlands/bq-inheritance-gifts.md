---
name: bq-inheritance-gifts
description: >
  Analyse inheritance and gift tax scope for Bonaire, Sint Eustatius and
  Saba in 2026. Use for the former Antillean succession tax, European
  Netherlands residence connections, emigrant donors or estates, entity gifts
  and related BES transfers or distributions. Explains saved liabilities,
  territorial definitions and distinct ten-year and one-year deemed-residence
  tests. Includes primary statutes, current authority guidance and fictional
  classification cases. This source-cited draft holds actual estate valuation,
  exemptions, foreign relief, forms and civil-law qualification. Load with
  the universal workflow base and applicable tax references; professional
  review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Inheritance/gift scope checked on 17 October 2026; this is not a tax-rate or estate-administration calculation"
tier: 2
last_updated: 2026-11-14
version: 0.2
type: situation-rules
domain: estate-wealth-tax
depends_on:
  - workflow-base
  - bq-transfer-tax
  - bq-corporate-tax
  - bq-double-tax-relief
---

# Bonaire, Sint Eustatius and Saba: inheritance and gifts

> **Built from the law. Not yet approved.** Written by Ryan Duguid and imported from his fork; conformed to the OpenAccountants standard by Claude. Not reviewed by an accountant. All outputs must be reviewed by a qualified tax professional before filing or payment. Tax year 2026. Currency: US dollars (USD).

## Scope

The former Antillean succession tax was not continued as a general tax on
new BES events after the transition period. That does not establish that a
gift or inheritance connected with BES has no tax consequence. European
Netherlands residence, deemed residence, another country's law, BES property
transfers or entity distributions need separate decisions. [MONEY]; [LETTER];
[SW]; [B1]

Load `workflow-base` and the applicable domain and BES references. Preserve
source gates, profile confirmation, refusals, four universal outputs and all
domain outputs/checks. Unknown mandatory legal conditions hold the complete
financial output package. This Tier 2 guide establishes selected scope tests;
it does not complete an estate, gift return or country pack.

## Ask the client first

1. **Is it a death or a gift**, and its date.
2. **The deceased's or donor's nationality** and residence history, especially any residence in the European Netherlands and when it ended.
3. **Whether the donor is a legal person**, and where it is established.
4. **What is transferred**, including any BES property right or registered ship.
5. **Any liability that arose before 10 October 2010** under the former Antillean succession tax.

## The method, step by step

### Key figures

| Item | Figure | Source |
|---|---|---|
| European Netherlands deemed residence, Dutch national who lived there (death or gift) | Ten years after leaving | SW, article 3(1): https://wetten.overheid.nl/BWBR0002226/2026-01-01 |
| European Netherlands deemed residence, any donor who lived there (gift only) | One year after leaving | SW, article 3(2): https://wetten.overheid.nl/BWBR0002226/2026-01-01 |

### Former succession tax and saved liabilities

Wet geldstelsel BES article 13b(1)(g) names the
**Successiebelastingverordening 1908**. Paragraphs 1–3 preserve specified
pre-transition rights, obligations and legal relationships. Paragraph 4's
continuation of the listed old instruments as law is limited to the
transition period, which article 13a ends on **1 January 2011**. Those are
different rules: ending temporary application to new events does not cancel
saved liabilities or settle their collection and limitation issues. [MONEY]

The commencement decree introduced the new framework on 1 January 2011,
with its stated exceptions and times. The government's 27 June 2025 letter
affirmatively explains that succession tax ceased effective 2011 while
transfer tax was retained. The current Belastingwet BES list and local
taxing framework do not supply a replacement general inheritance/gift charge.
The letter's reform discussion is not itself enacted 2026 law. [START];
[LETTER]; [B1, articles 1.2–1.3][B1]; [FIN, articles 40–65][FIN]

An undated future repeal marker attached to retained transition provisions
is not proof that temporary application continues indefinitely. Conversely,
do not apply a current-event scope result to an old estate, existing legal
relationship or unresolved historic assessment. Those cases require their
saved instruments, dates and procedural branch. [MONEY]

### European Netherlands residence tests

Successiewet 1956 article 1(1) charges inheritance by reference to a deceased
person resident in Netherlands at death and gifts by reference to the donor
resident there when giving. Under AWR article 2(3)(c), the statutory
Netherlands definition is European Netherlands, distinct from BES. Actual
residence is assessed from circumstances under AWR article 4(1), with the
specified crew rule in paragraph 2. The recipient's BES address or the
location of the receiving bank alone does not settle this test. [SW]; [AWR]

Do not stop at current residence. The Successiewet supplies these additional
tests:

| Provision | Condition and consequence |
|---|---|
| Article 3(1) | A Dutch national who lived in European Netherlands and dies or makes a gift within ten years after leaving it with residence is deemed resident there at that event. Nationality, former residence, actual departure and event dates must all be established. |
| Article 3(2) | A person who lived there and makes a gift within one year after leaving with residence is deemed resident there, without prejudice to paragraph 1. This is not limited to Dutch nationals and is not a general one-year inheritance rule. |
| Article 2(1)–(2) | Specified Dutch State employees posted for diplomatic/consular or treaty work are deemed resident, with the stated partner and dependent-child extension. Ordinary overseas employment does not itself prove this category. |
| Article 2(3) | For a legal-person donor, its place of establishment is treated as its residence. Do not substitute the beneficiary's residence or an individual emigrant rule. |

[SW]

These provisions establish a possible charging connection, not the amount
of tax. Actual exemptions, relationship/partner status, valuation, deemed
acquisitions, aggregation, debts, other relief, filing and payment must be
analysed under their complete applicable rules. Article 1 contains special
gift/acquisition and timing rules, including suspensive conditions; a transfer
of cash is not the only possible taxable event. No national tariff or
exemption amount is supplied here. [SW, articles 1–3][SW]

The authority's current foreign-inheritance and foreign-gift pages summarise
residence and emigrant conditions. Their general examples do not remove the
statute's special residence, event or entity rules. They also direct a
separate foreign-tax and double-tax analysis. Exact anniversary cases,
disputed residence, changes in nationality and complex legal instruments
remain held here rather than resolved by rounding years of absence. [ESTATE];
[GIFT]; [SW]

### Separate BES and foreign charges

An inherited or gifted BES property interest still requires the transfer-tax
analysis, including the actual acquisition, partition or death-related
agreement and any conditional exemption. A division exemption does not make
every purchase from an heir exempt. Entity or foundation payments can require
the distribution-tax branch. Subsequent rent, business receipts, disposal and
annual property ownership have their own tax treatment. Use the substantive
companions rather than recording the entire event as tax-free because the
former succession tax ended. [B1]; `bq-transfer-tax`; `bq-corporate-tax`;
`bq-income-tax`; `bq-property-tax`

Another country may use different residence, asset or recipient connections.
Identify its charge and the actual relief instrument. The reviewed
Belastingregeling voor het land Nederland tax list does not include
inheritance or gift tax; do not automatically apply its income allocation or
credit formulas to an estate. `bq-double-tax-relief` is a routing reference,
not proof of estate relief. Actual treaty/unilateral estate relief and any
credit, deduction or exemption computation remain open. [BRN, article 2][BRN];
[ESTATE]

## Worked cases

### Fictional classification cases

The following cases stipulate the stated facts, no special article 2 posting
and no other residence fiction unless mentioned. They test individual scope
branches, not a final tax amount, foreign tax or a filing exemption. All dates
and eligibility still require verification in an actual engagement. [SW];
[MONEY]; [B1]

| Stipulated facts | Result for the named branch |
|---|---|
| Dutch national lived in European Netherlands, moved residence to Bonaire eight years before dying in 2026 | Article 3(1) deemed residence applies; BES residence does not remove the European Netherlands inheritance connection. |
| Same facts, with a gift rather than death | The same ten-year branch applies to the gift. |
| Non-Dutch donor moved from European Netherlands to Saba six months before a gift in 2026 | Article 3(2)'s one-year gift branch applies despite non-Dutch nationality. |
| Same non-Dutch person dies after six months, instead of giving | Article 3(2) supplies no inheritance fiction. Establish actual residence and other rules; do not manufacture a one-year death rule. |
| Dutch national never lived in European Netherlands and is established as resident only in BES | Nationality alone does not satisfy article 3(1). It requires former European Netherlands residence. |
| Dutch national left eleven years before the gift, with no later residence there and no other fiction | The stipulated facts fall outside article 3(1)'s ten-year branch; this is not a conclusion about every other tax. |
| Donor is a legal person | Establish its place of establishment under article 2(3); an individual shareholder's travel history does not settle donor residence. |
| A 2026 gift includes a BES property right | No general former succession-tax charge is inferred; separately determine transfer tax, other taxes and any residence connection. |

Keep a sanitised event timeline, source/provision, person/entity classification,
residence/departure and nationality findings, asset/right schedule and each
tax's separate result. The responsible practitioner retains identities,
original civil instruments, tax identifiers and bank details outside the
agent. Do not collect or submit those documents or details here.

### Recomputed cases

**Case 1, a Dutch national eight years after leaving.** A Dutch national who left the European Netherlands for Bonaire in 2018 dies in 2026: eight years have passed, inside the ten-year branch, so the European Netherlands inheritance connection applies (first row of the table above). Someone who left in 2015 is eleven years out and outside it.

```oa-check
name: Ten-year deemed residence test, 2026 death
inputs:
  event_year: 2026
  left_a: 2018
  left_b: 2015
steps:
  - years_a: event_year - left_a
  - years_b: event_year - left_b
  - inside_a: 10 - years_a
  - outside_b: years_b - 10
expected:
  years_a: 8
  years_b: 11
  inside_a: 2
  outside_b: 1
```

**Case 2, a decision: give now or later?** A non-Dutch donor moved from the European Netherlands to Saba six months ago. A gift now falls inside the one-year gift branch; waiting until a full year has passed takes the gift outside it. On these facts the donor would wait about six more months (derived).

```oa-check
name: One-year gift branch, months remaining
inputs:
  months_since_move: 6
steps:
  - months_to_wait: 12 - months_since_move
expected:
  months_to_wait: 6
```

## When to refuse or refer

| Code | Situation | Action |
|---|---|---|
| R-BQ-IG-NL | A European Netherlands inheritance or gift tax liability arises | Refer: rates, exemptions and the return belong to European Netherlands law |
| R-BQ-IG-SAVED | A pre-transition succession-tax liability may survive | Refer: saved-law analysis needed |
| R-BQ-IG-CIVIL | Civil-law qualification of the estate or gift is unclear | Refer to a notary |

## Completion checklist

### Verification and completion limits

Check the deceased/donor rather than only the recipient; actual and deemed
residence; ten-year versus one-year scope; gift versus death; individual
versus entity; event timing; saved liabilities; property/distribution
consequences; and the covered-tax list before relief. Preserve all workflow
outputs, holds, reviewer questions and professional review.

Read on 17 October 2026: the currency law's articles 13a–13b; Successiewet
articles 1, 1a, 1b, 2 and 3; AWR article 2 and article 4(1)–(2); the two
complete authority pages; the full commencement decree/explanatory note and
2025 government letter; and the identified BES/FinBES scope provisions.
The BRN covered-tax list is reused from the separate relief review.
No complete civil-law, estate valuation, tariff/exemption, foreign relief,
historic-law or filing review was performed. No private estate, actual
engagement workbook, submission or practitioner sign-off was used.

## Sources

| Source | URL | Read on |
|---|---|---|
| MONEY. Read for the provisions this skill cites as [MONEY]. | https://wetten.overheid.nl/BWBR0028551/2012-07-01 | 2026-10-17 |
| START. Read for the provisions this skill cites as [START]. | https://zoek.officielebekendmakingen.nl/stb-2010-848.html | 2026-10-17 |
| LETTER. Read for the provisions this skill cites as [LETTER]. | https://zoek.officielebekendmakingen.nl/kst-32893-7.html | 2026-10-17 |
| B1. Read for the provisions this skill cites as [B1]. | https://wetten.overheid.nl/BWBR0029244/2026-04-11 | 2026-10-17 |
| FIN. Read for the provisions this skill cites as [FIN]. | https://wetten.overheid.nl/BWBR0028151/2023-01-01 | 2026-10-17 |
| SW. Read for the provisions this skill cites as [SW]. | https://wetten.overheid.nl/BWBR0002226/2026-01-01 | 2026-10-17 |
| AWR. Read for the provisions this skill cites as [AWR]. | https://wetten.overheid.nl/BWBR0002320/2026-10-01 | 2026-10-17 |
| BRN. Read for the provisions this skill cites as [BRN]. | https://wetten.overheid.nl/BWBR0029675/2025-01-01 | 2026-10-17 |
| ESTATE. Read for the provisions this skill cites as [ESTATE]. | https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/ik-heb-een-erfenis-uit-het-buitenland-waar-betaal-ik-erfbelasting | 2026-10-17 |
| GIFT. Read for the provisions this skill cites as [GIFT]. | https://www.belastingdienst.nl/wps/wcm/connect/nl/schenken/content/ik-krijg-een-schenking-uit-het-buitenland-moet-ik-aangifte-schenkbelasting-doen | 2026-10-17 |

[MONEY]: https://wetten.overheid.nl/BWBR0028551/2012-07-01
[START]: https://zoek.officielebekendmakingen.nl/stb-2010-848.html
[LETTER]: https://zoek.officielebekendmakingen.nl/kst-32893-7.html
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[FIN]: https://wetten.overheid.nl/BWBR0028151/2023-01-01
[SW]: https://wetten.overheid.nl/BWBR0002226/2026-01-01
[AWR]: https://wetten.overheid.nl/BWBR0002320/2026-10-01
[BRN]: https://wetten.overheid.nl/BWBR0029675/2025-01-01
[ESTATE]: https://www.belastingdienst.nl/wps/wcm/connect/nl/erfbelasting/content/ik-heb-een-erfenis-uit-het-buitenland-waar-betaal-ik-erfbelasting
[GIFT]: https://www.belastingdienst.nl/wps/wcm/connect/nl/schenken/content/ik-krijg-een-schenking-uit-het-buitenland-moet-ik-aangifte-schenkbelasting-doen

Not yet confirmed: estate valuation, exemptions and rates under European Netherlands law (outside this skill); foreign relief; forms; whether the one-year period ends exactly twelve months after departure or on the following day. Sources were read by Ryan Duguid on 2026-10-17 and not re-opened on import.
