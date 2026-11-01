---
name: fo-estate-income-tax
description: >
  Prepare Faroese death-year income-tax and estate-income workpapers for
  2026 deaths, separating the deceased, an undivided surviving spouse,
  public administration and private administration. Determines final
  provisional-tax treatment, an election for final assessment, inclusive
  settlement thresholds, opening information, estate-period income,
  the small-income exemption and the private-estate handoff to heirs.
  Covers tax carrying values, distributions of securities, current D03
  probate fields, ordinary return procedures, deadlines and sanctions.
  Trigger on Faroe Islands deceased taxpayer, deyðsbúgv, final tax return
  after death, section 14 inventory and estate tax clearance. Inheritance
  duty uses the separate succession Guide. Precise unresolved allowance,
  payment and current-year return implementation branches stay explicit.
jurisdiction: FO
category: income-tax
job: death-year-and-estate-income-tax
tax_year: 2026
tier: 2
trust_label: Built by Michael Cutajar and the OpenAccountants team
last_updated: 2026-10-31
version: 0.1
---

# Faroe Islands death-year and estate income tax v 0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this Guide for the deceased's final income period and the separate income
of an estate. The deceased's own liability ends at death. An estate taken
into probate administration in the Faroes is a full taxpayer under Tax Act
§1(1)(7); an overseas-administered estate requires the actual §2 source and
limited-liability conditions. Inheritance duty on capital passing to an heir
is a separate job in [the succession Guide](fo-inheritance-duty.md), rather
than estate income tax. [Tax Act §§1–2, 11, 15–20][tax]

If a surviving spouse immediately retains the community estate undivided,
§13 assesses the spouse on the couple's death-year income, with separate
calculations for deceased and survivor; the survivor fully succeeds to the
deceased's tax position. The same pre-death rule applies where the community
estate remains undivided but the deceased's separate property is divided;
that separate property still needs the §14 opening information. Do not
apply the provisional-tax finality rule to that mixed case.
[Tax Act §§13, 14(8), 39][tax]

In other cases, pre-death provisional tax due, or required withholding on
income earned before death, is final **unless** the estate or TAKS validly
requires final assessment. Even an estate too small to undergo division uses
that provisional-finality rule. Confirm the election and dates before
reopening a death-year calculation. [Tax Act §14(1)–(5), (9)][tax]

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Death-year additional tax | On valid final assessment, adjusted final tax at least DKK 5,000 above paid provisional tax is payable; exactly DKK 5,000 qualifies | [Tax Act §14(2)](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Death-year refund | Paid provisional tax at least DKK 100 above adjusted final tax is recoverable; exactly DKK 100 qualifies | [Tax Act §14(2)](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Estate income exemption | Division directly following death, final inventory both made and submitted to the tax authority within 15 months, and taxable estate income no more than DKK 25,000 | [Tax Act §15(2)](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| National ordinary estate rate | 40% of the ordinary taxable estate income, subject to the statutory exemption/allowance question below; this is expressly the national rate | [Assessment Act §6](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| Estate allowance cross-reference | Assessment Act §6 grants DKK 25,000 to estates meeting Tax Act §15(2)'s conditions. A blanket deduction for every estate closed within 15 months, regardless of income, is not established here | [Assessment Act §6](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |

The current Tax Act says **“minst”**, at least, for both settlement thresholds.
TAKS's linked 2015 estate guidance instead says greater than in its narrative.
Use the inclusive statutory thresholds above and the §78/§79 adjustments
required by §14(2), not an unadjusted tax difference. Ordinary personal rates,
credits and annualisation are owned by [the individual-tax Guide](fo-individual-income-tax.md).
[Tax Act §§14(2), 24(2), 40(1)][tax]; [TAKS G.2.1][guidance]

The national rate does not prove an all-in estate rate. Tax Act §41(6) places
the estate in the deceased's last tax municipality; §§46–47 prescribe the
municipal base/rate and rounding, and §54(2) the combined national, municipal
and church ceiling. Reconcile the actual municipal assessment separately
using the municipal data in the individual-tax Guide. The precise estate
application of those components and the §6 allowance above the §15(2) income
ceiling are unresolved here; do not publish an unconditional 40% total-tax
quote or a guessed blanket allowance. [Tax Act §§41(6), 46–47, 54][tax];
[Assessment Act §6][rates]

## The base

1. **Separate pre-death earned income.** Include all A-income earned up to
   death even if paid later, and B-income up to death. Where final assessment
   is elected/required, compute the death-year income under the deceased's
   rules and the applicable personal annualisation method, then reconcile
   provisional payments and §78/§79 adjustments. Do not include that same
   earned income again as post-death estate income. The survivor separately
   reports their A-income and B-income outside the estate.
   [Tax Act §§14, 24(2), 40(1)–(2)][tax]
2. **Make a tax-value opening schedule.** For depreciable assets use the
   previous year-end tax carrying value, with permitted proportionate
   pre-death depreciation. Adjust a machinery/equipment pool for intervening
   purchases and sales before depreciation. Keep this tax schedule beside
   D03's death-date sale-value inventory; one is not a substitute for the
   other. [Tax Act §14(6)][tax]; [D03 pp 2–4][opening]
3. **Identify the estate period.** Public administration includes income from
   death to the final closing/division date and income realised on
   distributions. If the period is shorter than 15 months it is one income
   period; where not closed within 15 months, ordinary annual returns apply,
   the first period ending on the next 31 December. Apply ordinary income
   computation but no investment-fund reserve. Assets retain original
   acquisition cost and depreciation history; sale gains/losses are treated
   as for the deceased. On final division the specified depreciable/§27 assets
   are treated as sold at market value and relevant reserves recaptured.
   Apply the separate Capital Income Act §12 distribution rule below.
   [Tax Act §§15, 24(3), 40(3)–(7)][tax]
4. **Test exemption before applying a rate.** The final inventory must both be
   made and reach the tax authority within the stated 15-month period, the
   division must directly follow death, and income must not exceed the table's
   limit. A reopened public estate is expressly outside that exemption.
   Do not confuse the probate court's earlier one-year closing requirement
   with the tax exemption's outer limit. [Tax Act §§15(2), 18(1)][tax];
   [succession Guide](fo-inheritance-duty.md)
5. **Private estate still open at 15 months.** Within one month after expiry,
   file an inventory identifying assets already allocated, joint allocations
   and unallocated assets, plus the ordinary return for death through expiry.
   Estate liability ends then; thereafter heirs/spouse are taxed in proportion
   to their shares. Unsold/unallocated assets enter the estate's closing
   gain/loss computation as if sold at the stated values under §§16–17, and
   those values become the recipients' acquisition bases. Do not extend the
   estate's liability indefinitely merely because distribution is unfinished.
   [Tax Act §§16–17][tax]
6. **Track changes of administration.** Division of an undivided estate during
   the survivor's life moves community income into the estate from court
   approval and requires an opening statement within two months; the §15(2)
   clock starts at that approval. Conversion of directly administered
   public/private estates to undivided spouse administration applies §13
   from death and cancels the corresponding §14 assessment. A public-to-private
   transfer after 15 months triggers §17's handoff at transfer; a private-to-public
   transfer after 15 months does not restore estate taxpayer status. Reopened
   public estates become taxable on the court's reopening decision; reopened
   private estates tax the owners. [Tax Act §§18–19][tax]
7. **Keep securities distributions separate.** Capital Income Act §12 excludes
   the distribution gain/loss and gives the securities recipient the deceased's
   tax position only within its conditions. Those rules do not apply where the
   spouse/heir/legatee is not fully liable in the Faroes or is treaty-resident
   elsewhere; then the distribution's gain/loss is included in the estate's
   taxable income. A sale by the estate is not automatically an exempt
   distribution. Capital interest/dividends and capital-tax computation remain
   under that Act and the [individual-tax capital method](fo-individual-income-tax.md),
   rather than being folded into the ordinary estate rate without analysis.
   [Capital Income Act §§9–12, 14, 16][capital]; [Tax Act §40(6)][tax]

## Deadlines and filing

**Opening information and final-assessment decision.** Appoint the responsible
estate contact under §20(2). Prepare D03, the separate tax-carrying-value
schedule and a January-to-death earned-income statement. The deadline is
**six months after death**, or, if the administration method was decided later
than four months after death, **two months after that decision**. An estate
requesting final assessment must notify TAKS and submit the ordinary death-year
return within that same deadline. TAKS's own request has the separate
§14(5) clocks: six months after death, extended to two months after receipt
where the opening statement arrives later than four months; notification
to the estate must also occur within two months after receipt. Preserve
receipts and notifications. [Tax Act §§14(3)–(5), 20(2)][tax]

The current court-linked **six-page D03** identifies the deceased, spouse,
earlier-deceased spouse, contact, refund account and community/separate
property in sections A–E. Asset boxes 1–23 and debt boxes 24–31 produce net
assets in box 32; box 33 discloses benefits outside the estate and box 34 gifts.
The responsible person dates/signs in blue ink and sends the original to
**Skiftirættin, C. Pløyensgøta 1, PO Box 28, 110 Tórshavn, not email**; the court
forwards it to TAKS. Attach the tax-value/income schedules rather than
silently replacing the form's market values with tax values. The separate
closing inventory and court-to-TAKS approval/inheritance-duty invoice workflow
are detailed in [the succession Guide](fo-inheritance-duty.md).
[D03, all six pages][opening]; [Tax Act §14(3), (6)][tax]

**Ordinary estate return.** Tax Act §100(3) gives estates a **1 July** annual
return deadline; this does not displace the special death-year, closure or
15-month handoff clocks. Sections 102–103 require signature and accounts with
opening/closing balance sheets. The current TAKS **2025 return filed in 2026**
calendar expressly includes estates among entities with a V-number receiving
a return and requires accounts even where exempt. Its linked instructions
say use **Vinnugluggin → Sjálvuppgáva → Sjálvuppgáva**, attach accounts on the
same page, and use **Sjálvuppgáva → Kapitalvinningssjálvuppgáva** for a required
capital return. The published attachment labels distinguish company types
(“Skattlig sundurgreining”) from associations (“Skattaroknskapur”); they do
not expressly establish the estate-specific attachment label or every box.
Use the actual estate's issued return, entity identity and period; retain
the submitted return/accounts, portal acknowledgement and assessment.
[Tax Act §§100, 102–103][tax]; [TAKS estate-inclusive calendar][calendar];
[TAKS current return instructions][return]

These are the dated current instructions, not proof of a 2026
form not read here or a right to use the deceased's personal credentials. The linked
exceptional paper-return PDF returned 404 and the normal in-app browser was
unavailable. Estate-specific current-year fields, authority setup and the
special-period submission/acknowledgement sequence still need verification;
the Guide does not invent them. The closing inventory is not itself a
substitute for every income-tax return required by §§14/17/40/100.
[TAKS current return instructions][return]; [Tax Act §§14, 17, 40, 100][tax]

**Payment and clearance.** Reconcile TAKS's assessment, provisional payments,
any recoverable death-year refund and the actual demand. Section 80(5) says
estate tax plus final-assessment arrears falls due three months after issue,
with a timely deadline on the 20 th of the payment month, moved for a Saturday
or holiday. Section 81 also lists estates in its ordinary October/November/
December instalment machinery. The exact application between these two
provisions to a particular estate demand is not resolved here. Record and
follow the actual demand's earlier applicable date while that classification
is settled; do not replace it with inheritance duty's six-week clock.
[Tax Act §§80(5), 81][tax]

Public administrators must also provide the §127 information without request
within **two months after death** where the property left is at least
**DKK 25,000**. Its tax-authority claim-notification period runs two months
from the last requested information; do not close before the statutory
periods expire without the stated no-claim confirmation. These are separate
from the ordinary D03 deadline. [Tax Act §127(1)–(2)][tax]

## Penalties and interest

For a missing/late §14 opening statement the court can impose daily fines
and move private administration to public administration; it **must** do so
if the statement remains missing three months after the deadline. No fixed
DKK daily amount is given in §14(7). For an incomplete/late ordinary return,
§104 permits estimated income and specifies a DKK 1,000–5,000 fine, with total
income tax increased by 2% if fewer than seven days late and 5% if seven or
more days late; the special-circumstances remission mechanism is not an
automatic waiver. Intentional/grossly negligent misleading estate information
is covered by §142(3), referring to §141's sanctions. [Tax Act §§14(7), 104, 141–142][tax]

Income-tax late payment generally bears **0.7% per commenced month from the
due date** under §135; §81 separately states its instalment interest rule.
Reconcile the actual demand and commencement of each month, not a daily
pro-rata approximation. The succession duty's daily interest and one-third
late-declaration addition are different charges, owned by its Guide.
[Tax Act §§81, 135][tax]; [succession Guide](fo-inheritance-duty.md)

## Cross-border points

For foreign-administered estates test the precise §2 source categories;
Faroese property alone is not proof that every foreign receipt is taxable
here. For securities distribution prove the beneficiary's full Faroese tax
liability **and** treaty residence before using §12's carryover; actual
nonresident distribution is a recognition trigger under §12(4). Resolve
actual treaty provisions and foreign credits through the
[cross-border Guide](fo-cross-border-payments.md), including its stated
limits. Inheritance-duty domicile and foreign-property rules do not decide
income-tax residence or capital-gain recognition. [Tax Act §§1–2][tax];
[Capital Income Act §12][capital]

## Two worked examples that recompute

### 1. Exact statutory settlement thresholds

Fictional valid final-assessment cases; the final-tax figures below already
include every §78/§79 adjustment and the applicable personal calculation.
With adjusted final tax DKK 45,000 and provisional paid DKK 45,100, the estate
can recover **DKK 100**. With adjusted final tax DKK 50,000 and provisional
DKK 45,000, it must pay **DKK 5,000**. Both exact thresholds qualify under
“minst”; the old guidance's strict-greater wording would incorrectly reject
both. This checks settlement, not a second computation of personal tax.
[Tax Act §14(2)][tax]

```oa-check
name: Faroese death-year inclusive settlement thresholds
inputs:
  refund_case_provisional: 45100
  refund_case_adjusted_final: 45000
  arrears_case_provisional: 45000
  arrears_case_adjusted_final: 50000
steps:
  refund_difference: refund_case_provisional - refund_case_adjusted_final
  arrears_difference: arrears_case_adjusted_final - arrears_case_provisional
  refund_threshold_margin: refund_difference - 100
  arrears_threshold_margin: arrears_difference - 5000
expected:
  refund_difference: 100
  arrears_difference: 5000
  refund_threshold_margin: 0
  arrears_threshold_margin: 0
```

### 2. Decide whether to request final assessment

Fictional divided estate, no §13 spouse treatment. A qualified computation
already establishes provisional paid DKK 70,000 and adjusted final tax
DKK 64,000. A timely request plus ordinary death-year return produces a
recoverable DKK 6,000; without a valid request from either party, §14(1)
leaves provisional tax final and no refund arises from merely preparing
an inventory. The financial difference is DKK 6,000. If the same election
instead produced adjusted final tax DKK 76,000, the estate would owe
DKK 6,000. Check the full computation, benefits and downside before deciding;
file the election by its own deadline rather than waiting for final probate
clearance. [Tax Act §14(1)–(5)][tax]

```oa-check
name: Faroese estate final-assessment election decision
inputs:
  provisional_paid: 70000
  verified_refund_case_final: 64000
  verified_adverse_case_final: 76000
  no_election_refund: 0
steps:
  timely_election_refund: provisional_paid - verified_refund_case_final
  financial_advantage: timely_election_refund - no_election_refund
  adverse_election_payment: verified_adverse_case_final - provisional_paid
expected:
  timely_election_refund: 6000
  financial_advantage: 6000
  adverse_election_payment: 6000
```

## Ask the client first

- What are the death date, probate method/approval date, property regime,
  surviving spouse's undivided-estate decision and any later method change?
- What earned A/B-income, paid/withholdable provisional tax, personal credits,
  carrying values and §78/§79 adjustments belong before death?
- What income, expenses, disposals, depreciation/reserves and distributions
  arose after death, and when was each asset allocated and the inventory filed?
- What proves each securities recipient's tax liability/treaty residence,
  original basis and the estate's ordinary versus capital-income treatment?
- What contact appointment, V-number, authority/access, D03 receipts, ordinary
  returns, election notices, tax assessments, demands and payments exist?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Current Tax Act 109/2023, current through 2026 amendments; §§1–2,11–20,24,39–41,46–47,54,80–81,100–104,127,135,141–142 | https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt | 2026-10-31 |
| Assessment Act 87/1983, current §6 | https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170 | 2026-10-31 |
| Capital Income Act 164/2001 current through 127/2024, §§9–12,14,16 | https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173 | 2026-10-31 |
| Current court-linked D03, all six pages; original delivery and asset/debt fields | https://domstoldk.euwest01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf 01.umbraco.io/media/tfjl 4 r 3 d/d 03-uppger%C 3%B 0-yvir-ogn-og-skuld-vi%C 3%B 0-dey%C 3%B 0 a-sambaert-14-%C 3%AD-skattal%C 3%B 3 gini-241023.pdf | 2026-10-31 |
| TAKS estate guidance G.1–G.2, dated 2015; current statute controls settlement-threshold conflict | https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/g-deydsbugv | 2026-10-31 |
| TAKS current inheritance/estate information | https://www.taks.fo/fo/borgari/skattur/skattur-og-arvur | 2026-10-31 |
| TAKS estate-inclusive 2025 return calendar, filing 1 July 2026 | https://www.taks.fo/fo/taks/taks-kalendarin/freist-at-lata-inn-sjalvuppgavu-2025-hja-feloegum | 2026-10-31 |
| TAKS 2025 entity-return instructions, portal menus and accounts attachments | https://www.taks.fo/fo/vinna/sjalvuppgava-2025/sjalvuppgava | 2026-10-31 |

Not yet confirmed: application of the Assessment Act§6 allowance where income exceeds Tax Act§15(2)'s ceiling; final estate-specific municipal/church computation and credits; precise reconciliation of §§80(5)/81 payment machinery for each estate assessment; current-year estate return boxes/attachments, authority setup and special-period submission/acknowledgement beyond the dated 2025-return instructions; full inherited-loss/foreign-credit and unusual recapture computations. These are actual implementation gaps, not exemption conclusions. The supported death-year election, opening statement, estate-period and handoff methods do not certify a complete ordinary estate tax computation. This source-cited tier-2 draft is pending independent review and professional attestation.

[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[rates]: https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170
[capital]: https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173
[guidance]: https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/g-deydsbugv
[opening]: https://domstoldk.euwest01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf 01.umbraco.io/media/tfjl 4 r 3 d/d 03-uppger%C 3%B 0-yvir-ogn-og-skuld-vi%C 3%B 0-dey%C 3%B 0 a-sambaert-14-%C 3%AD-skattal%C 3%B 3 gini-241023.pdf
[calendar]: https://www.taks.fo/fo/taks/taks-kalendarin/freist-at-lata-inn-sjalvuppgavu-2025-hja-feloegum
[return]: https://www.taks.fo/fo/vinna/sjalvuppgava-2025/sjalvuppgava
