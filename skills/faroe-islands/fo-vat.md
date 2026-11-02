---
name: fo-vat
description: >
  Calculate Faroese MVG for ordinary businesses in 2026 by distinguishing
  taxable sales, supplies with no output VAT but input recovery, and exempt
  activities without input recovery. Covers registration, domestic and imported
  goods, specified foreign services, invoices, credit notes, mixed-use input
  allocation, vehicles, capital adjustments, refunds, cessation and current
  quarterly administration. Trigger on Faroe Islands VAT, MVG, foreign services,
  DKK 50000 registration, input VAT, property use changes, VAT refunds and
  business transfers. Uses the current VAT Act and proportional-deduction
  regulation. Records the Q2 payment-date source conflict rather than assuming
  the return deadline changes the statutory payment clause. Specialist refunds
  and unresolved foreign-service implementation need separate evidence.
version: 0.4
jurisdiction: FO
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Faroe Islands VAT registration and returns v0.4

> **Checked against the law for 2026.** This Guide has no professional attestation
> for the revised content. It prepares classification and calculation working
> papers; the stated source conflicts and implementation gaps remain open.

## Who this applies to

Calculate Faroese MVG by separating taxable sales, supplies with no output
VAT but input recovery, and exempt activities without input recovery. The
Faroese VAT territory and charge arise under Act 136/1992 §§1–3. Foreign
business activity can require registration independently of income-tax PE
status. Danish/EU VAT rules are not a substitute for this Act ([law][law]).

Section 4 exempts annual sales **below DKK 50,000**. Exactly DKK 50,000 does
not satisfy that wording. Determine annual business sales rather than profit,
and separate the exempt activities under §2(3). A registered business does
not stop accounting for VAT solely because later sales fall below the
threshold; TAKS describes cancellation as a separate choice where turnover
stays low ([§§4–5][law]; [TAKS tourism guidance][tourism]).

Register at least eight days before activity starts, subject to the security
provisions. Businesses with the same owner are generally notified together,
with separate-registration requests possible for separate accounts. Approved
joint registration is treated as one business; joint liabilities apply.
A foreign business without a local branch registers through a resident
person/local establishment unless the Hoyvík treaty exception applies.
Do not infer that exception from all foreign residence ([§§5 and 25][law]).

## Rates, bands and thresholds

| Item | 2026 rule | Official authority |
|---|---|---|
| Standard VAT | 25% of VAT-exclusive taxable value | [Act §14](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| VAT in a standard-rated gross price | 20% of VAT-inclusive amount, equivalent to 25/125 | [§§13(3), 17(1)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Ordinary small-sales exemption | Annual sales strictly below DKK 50,000 | [§4](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Specified foreign supplier services | More than DKK 50,000 annual sales; §28(2)(7)–(13), used in the Faroes, with paragraph 3 exceptions | [§28(1)–(3)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Exempt activities | No output VAT and no ordinary recovery for directly attributable purchases | [§§2(3), 15–16](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24); [regulation §1](https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi) |
| Listed no-output supplies | §12 supplies retain the applicable input-recovery route; distinguish from §2 exemption | [§§12, 15–16](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24); [TAKS examples](https://www.taks.fo/fo/vinna/mvg/mvg-og-ferdavinna) |
| Equipment capital-adjustment threshold | Depreciable equipment costing more than DKK 20,000 excluding VAT | [Regulation §§8 and 10](https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi) |
| Qualifying property works | More than DKK 50,000 taxable value per year for extensions/rebuilding/modernisation/repair/maintenance | [Regulation §10(3)](https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi) |
| Capital adjustment | Five accounting years for equipment; ten for property/qualifying works, including acquisition year | [Regulation §11(2)](https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi) |
| Foreign unregistered buyer's specified-service payment | Within ten days after receipt of service, on paragraph 4 conditions | [§28(4)–(5)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |

**Temporary fuel rule.** Act 36/2026 inserts §12(1)(v) for specified petrol/
diesel tariff codes. It was published 15 May 2026 and takes effect the next
day: the listed sales fall within that no-output provision from **16 May
through 31 July 2026**. Before 16 May and from 1 August, that temporary clause
does not exclude the sale from ordinary VAT. The amending Act's repeal on
1 January 2027 does not extend its express 31 July sales end date. Check the
six listed tariff codes, not every fuel or energy product ([amending Act
§§1–2 and publication record][fuel]; [current §12(1)(v)][law]).

## The base

### Sales classification and taxable amount

Standard-rated value is the consideration excluding MVG. Include relevant
other duties, packaging, freight/insurance, connection/establishment charges,
commissions and financing supplements. Separately evidenced interest on the
outstanding purchase price can be outside the value under §7(3). Owner/
non-business withdrawals generally use purchase/production cost; barter uses
the ordinary selling price or the specified calculated price. Connected-party
value can be adjusted under §9 ([§§7–9 and 11][law]).

Exempt §2(3) services include qualifying healthcare, social care, education,
certain cultural activity, sport, passenger transport with the bus exception,
specified postal services, property letting/management, insurance/finance,
gaming, artistic activity, funeral services, tourist-guide/agency services,
water supply and the tightly conditioned charity second-hand shop. The
exceptions inside each category matter: a concert or commercial non-route
bus service is not automatically exempt because it is cultural/transport.
Restaurant and bar sales are not hotel-room sales ([§2(3)][law]).

Section 12 separately excludes listed supplies from output-taxable sales,
including exports and qualifying services abroad, directly linked foreign
freight, specified foreign-account goods work/design, qualifying ships/
aircraft and work on them, newspapers, listed books/audiobooks, specified
fishing supplies, hotel/guesthouse rooms and camping sites, prescription
medicine, specified vegetables and baby nappies. Use the actual item/code
and conditions. TAKS confirms the zero-output/input-recovery distinction for
qualifying accommodation. A §2 exempt activity has a different input result
([§12][law]; [TAKS tourism guidance][tourism]).

The tax period follows actual supplies. Timely invoices can determine the
supply timing under §13(2). For an advance received before supply/invoicing,
80% of the gross advance enters the taxable-sales base; standard VAT on that
base is 20% of the gross receipt. Returns, established bad debts and later
collections adjust their statutory 80% bases. Discounts requiring later
conditions need the prescribed credit-note treatment. Do not treat an unpaid
invoice as an established bad debt automatically ([§13][law]).

### Input recovery and mixed activity

Deduct supported supplier VAT invoiced in the period and the import VAT
imposed under §27, only with the eligible-use rules and invoice/customs
proof. Direct fully recoverable activity gets its supported input; direct
exempt/nonregistered activity gets none. Shared expenditure uses recoverable
activity sales excluding VAT divided by total sales for the accounting year.
Prior-year sales support provisional periods, with a final adjustment after
year end; a new business uses its actual period sales. Private use requires
a supported business-use estimate, not an invented flat percentage
([§§15–16, 18(4)][law]; [regulation §§1–2][reg]).

Section 16(3) blocks specified food for proprietor/staff, owner/staff housing,
benefits in kind, staff welfare/holiday facilities and gifts. Apply the
express statutory exceptions rather than importing another country's
entertainment percentage. Property construction allocation uses relevant
business-building costs; equal-standard rooms can use floor area. Direct
repair costs follow the relevant rooms; common repairs use the prescribed
area proportion. Housing and non-optioned letting are excluded from business
rooms for this purpose ([§16(3)][law]; [regulation §§3–4][reg]).

For vehicles at most **3,500 kg actual total weight**, purchase/lease input
needs exclusive use in taxable sales activity; mixed private use does not
create a proportional purchase deduction. Vehicles over that weight follow
the specified business-use rules. Operating costs have a separate full-input
rule even with partial business use; **lease payments are not operating
costs** for it. Regulation §5 also requires annual taxable sales exceeding
**DKK 20,000**. Retain weight, use, sales and cost classification evidence
([regulation §5][reg]).

### Capital adjustments, sale and cessation

Maintain an asset register with original VAT, acquisition year, initial
recovery proportion, current use and remaining adjustment years. Annual
adjustment compares current recovery with acquisition-year recovery:
`original VAT × proportion change × 1/5` for equipment, or `× 1/10` for
property/qualifying works. A change **below ten percentage points** is
outside the annual adjustment requirement; exactly ten is not below it.
The regulation restricts upward adjustments where there was no original
recovery or a prior full nonrecoverable-use adjustment. Full nonrecoverable
use and specified transfers can accelerate the remaining period. A buyer's
assumption needs the actual eligibility and written acknowledgement, not
an automatic carryover ([regulation §§10–16][reg]).

Sales of business machinery/stock and withdrawals at deregistration are
within §11(4), subject to the specific exceptions. A transfer of a whole
business or part to a new operator running a registered business can fall
outside output-taxable sales under §12(5). Notify TAKS of the new operator,
address and transferred asset sale price within eight days. Property and
capital-adjustment succession still require their own conditions. Disposal
of a vehicle whose acquisition VAT could not be deducted has the separate
rule in regulation §9(3) ([§§11–12][law]; [regulation §§9, 12–14][reg]).

## Deadlines and filing

| Obligation | Rule | Official authority |
|---|---|---|
| Registration notice | At least eight days before starting; security exception | [§5(5)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Owner/management/location changes | Within eight days after change | [§5(5)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Q1/Q3/Q4 return | One month and ten days after quarter; ordinary 10 May/10 November/10 February | [§20(1)–(2)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Q2 return | 24 August | [§20(1)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Statutory payment clause | One month and ten days after the tax period; Q2 conflict below | [§22(1)](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Annual stock count/accounting records | Retain five years after accounting year end, including §4-exempt businesses | [§19](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |
| Refund on timely submitted return | Within three weeks after receipt, subject to verification obstruction and prior-period return/offset conditions | [§24](https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24) |

**Q2 payment source conflict.** Section 20 expressly moves the Q2 **return**
to 24 August. Section 22(1)'s **payment** clause still says one month and ten
days after period end, which gives 10 August. TAKS's current return page
calls 24 August both the filing and payment deadline. No separate instrument
reconciling that difference has been verified here. Apply the statute for
the calculation and do not rely on the later date for payment without the
relevant authority. Preserve the actual assessed/payment notice and this
conflict for review ([§§20, 22 and 32(4)][law]; [current TAKS guidance][returns]).

TAKS accepts the return through **Vinnugluggin**. Its current page also gives
a manual route with a DKK 250 administrative fee and moves listed weekend/
holiday deadlines to the next working day. File nil periods. Regular credit
businesses can apply for monthly/weekly settlement; the law requires an
application one month before the period change and sets a two-year restriction
on returning to quarterly settlement. Refunds require earlier returns and
offset earlier VAT/interest as provided in §24 ([§§20, 24, 35][law];
[TAKS procedure][returns]).

Invoices need issue date, supplier/recipient names and addresses, supply
nature/quantity/price and the VAT amount or the prescribed gross-price VAT
identification. A registered customer can require explicit VAT and net line
prices. Correct post-invoice returns/discounts with a credit note and extra
charges with a supplementary invoice. Distinguish taxable/exempt lines,
retain duplicates and customs VAT evidence; the limited retail simplifications
do not erase a registered buyer's request right. A nonregistered business
must not charge VAT as if registered. Incorrectly shown VAT is payable unless
the mistake is corrected with the buyer ([§§17–19][law]).

## Penalties and interest

Late return increases the period liability by **1%**, minimum **DKK 300**,
maximum **DKK 1,000**. TAKS can grant the statutory special-circumstances
relief and make a provisional assessment where no return arrives. The law
also provides cancellation procedures after repeated estimated periods;
cancellation is not permission to continue taxable activity unregistered
([§21][law]).

Unpaid VAT attracts **0.7% for each commenced month** from its due date.
Section 22 also covers the late-return increment and booked interest.
Additional assessments use §32's demand/payment rules and interest runs from
the statutory §22 due date under §32(4). Do not substitute commercial-debt
interest. Intentional/grossly negligent misinformation, records failures and
specified registration breaches have fines under §33; specified evasion and
continued activity after refused/withdrawn registration can attract a fine
or up to two years' imprisonment. No fixed fine tariff is invented here
([§§22, 32–34][law]).

## Cross-border points

Imports of goods are subject to §27: ordinary import VAT is **25%** of the
customs value plus applicable customs/other import duties, excluding this
VAT itself. Keep customs notices and importer/use evidence. Only the actual
customs/Act exemptions qualify; an overseas invoice is not an export of the
Faroese buyer's goods. Processing/repair abroad followed by reimport has the
specific cost-plus-transport/insurance and permission rule. Export relief
needs the actual export/performance conditions under §12. Nonresident
refund routes under §§36–36a need their implementing conditions rather
than an automatic domestic-return credit ([§§12, 18 and 27][law]).

For foreign services, apply **§28's actual categories**, not a generic EU
B2B reverse-charge rule:

- Foreign suppliers of paragraph 2 items **7–13** must register/charge where
  annual qualifying sales exceed DKK 50,000 and services are used in the
  Faroes. Those items include movable-property hire, local property services,
  specified events, work/valuations on local movables, telecoms and broadcasts.
- Paragraph 3 excludes items **1–6 and 8–13** sold to a registered Faroese
  business entitled to recover all the VAT. Its list omits item 7; do not
  silently give equipment hire the same exclusion.
- Individuals, public institutions and others **not VAT registered** buying
  foreign items **1–6** used in the Faroes must pay under paragraphs 4–5.
  Those items include rights, advertising, professional/advisory/data services,
  staff supply, restraint obligations and intermediaries. They keep service
  records for five years and pay/notify within ten days of service receipt.
  Paragraph 4 does not state the supplier's DKK 50,000 threshold.
- Imported services equivalent to an exempt domestic supply have paragraph
  6's exemption. Test that exemption before computing a charge.

For a registered customer that cannot recover all the VAT, paragraph 3's
full-recovery exclusion does not apply. A foreign supplier within paragraph
1 therefore registers and charges 25% on a taxable item 7–13 service used
in the Faroes when its relevant annual sales exceed DKK 50,000. The customer
then applies the ordinary input rules to the supplier's actual Faroese VAT
invoice. Registration alone neither removes this supplier charge nor gives
the customer full input recovery. For example, assume an established item
12 telecommunications supply used in the Faroes, a foreign supplier with
DKK 60,000 qualifying annual sales, and a DKK 10,000 net invoice. Supplier
VAT is DKK 2,500. If this is a shared business overhead and final eligible
turnover is 60% of total turnover, the customer's supported input recovery
is DKK 1,500 and unrecovered VAT DKK 1,000. Assume no private use, blocked
input, domestic-equivalent exemption or special allocation rule. These are
case amounts, not statutory allowances ([§§15–17, 28(1)–(3), (6)][law];
[regulation §1][reg]).

Keep the different items 1–6 branch separate: paragraph 1 does not list
those services, while paragraph 4 expressly addresses an unregistered
recipient. Those provisions alone do not establish a registered partly
recovering customer's liability for a foreign consultancy invoice. That
specific branch and particular bundled/digital classifications remain
unconfirmed; do not invent a general reverse charge or an exemption.

The local-representative/Hoyvík exception is separate from these charging
and recovery tests. No Danish/EU territorial entitlement is assumed
([§§5, 25 and 28][law]).

## Two worked examples that recompute

### 1. Ordinary fully taxable business

Assume DKK 100,000 of standard-rated sales excluding VAT and DKK 10,000 of
fully deductible input VAT evidenced in the period. Output is DKK 25,000;
net due is DKK 15,000. A gross DKK 125 standard-rated sale contains DKK 25
VAT, not DKK 31.25 ([§§14–16][law]).

```oa-check
name: Faroese ordinary output and eligible input VAT
inputs:
  net_sales: 100000
  rate: 0.25
  supported_input_vat: 10000
  gross_price: 125
steps:
  output_vat: net_sales * rate
  vat_payable: output_vat - supported_input_vat
  vat_in_gross_price: gross_price * rate / (1 + rate)
expected:
  output_vat: 25000
  vat_payable: 15000
  vat_in_gross_price: 25
```

### 2. Shared input and equipment-use adjustment

Assume annual standard-rated sales excluding VAT of DKK 300,000 and exempt
sales of DKK 200,000, no other sales or special allocation, and DKK 20,000
shared-input VAT. Recovery is 60%, giving DKK 12,000. Separate qualifying
equipment cost DKK 100,000 excluding VAT (original VAT DKK 25,000) had full
recovery at acquisition and remains in its adjustment period. Current
recovery falls to 60%; the annual reduction is 25,000 × (1 − 0.60) / 5 =
DKK 2,000. Net input after this reduction is DKK 10,000. This is a supported
40-point change; neither private vehicle rules nor full change-of-use
acceleration is assumed ([regulation §§1, 10–11, 14, 16][reg]).

```oa-check
name: Faroese mixed activity and annual equipment adjustment
inputs:
  taxable_net_sales: 300000
  exempt_sales: 200000
  shared_input_vat: 20000
  original_equipment_vat: 25000
  original_recovery: 1
  equipment_years: 5
steps:
  recovery: taxable_net_sales / (taxable_net_sales + exempt_sales)
  eligible_shared_input: shared_input_vat * recovery
  annual_repayment: original_equipment_vat * (original_recovery - recovery) / equipment_years
  net_input_after_adjustment: eligible_shared_input - annual_repayment
expected:
  recovery: 0.60
  eligible_shared_input: 12000
  annual_repayment: 2000
  net_input_after_adjustment: 10000
```

## Ask the client first

- What activities, locations and annual sales establish registration and supply classification?
- Which invoices/customs notices and actual taxable, exempt or private uses support input recovery?
- What capital assets, acquisition-year recovery and subsequent use changes exist?
- What foreign service category, customer registration and full/partial recovery status apply?
- What return periods, assessed payment dates, prior returns and debts affect filing/refunds?
- Is there a business transfer, cessation or special property/vehicle scheme requiring separate conditions?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Current Act 136/1992, consolidated through Act 36/2026, §§1–36a and amendment notes; actual register text read in normal browser and saved HTML | https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24 | 2026-10-25 |
| Regulation 35/2000, proportional input and capital adjustments, §§1–18; register status current | https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi | 2026-10-25 |
| Act 36/2026 §§1–2, temporary fuel clause and publication 15 May 2026 | https://www.logir.fo/Logtingslog/36-fra-15-05-2026-um-broyting-i-logtingslog-um-meirvirdisgjald-Meirvirdisgjaldslogin | 2026-10-25 |
| TAKS quarterly return/refund procedure, fee and dates, with Q2 payment conflict above | https://www.taks.fo/fo/vinna/mvg/at-lata-inn-mvg-uppgerd | 2026-10-25 |
| TAKS VAT/tourism guidance, exempt versus zero-output/input recovery and mixed use | https://www.taks.fo/fo/vinna/mvg/mvg-og-ferdavinna | 2026-10-25 |
| Current VAT Act §§15–17 and 28(1)–(6), registered partial-recovery customer of an item 7–13 foreign service | https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24 | 2026-10-28 |

Not yet confirmed: separate authority reconciling Q2 payment under §22 with TAKS's later guidance date; the distinct foreign-service items 1–6 liability branch for a registered partial-recovery customer and particular bundled/digital cases; detailed Hoyvík representative exception and nonresident refund procedure. The item 7–13 positive supplier-charge/input-recovery method is supplied above. Voluntary property, charity/energy/vehicle refund schemes and other specialist conditions require separate sources. Independent whole-pack AI review accepted the previous v0.3 for partial tier-2 draft publication on 25 October 2026; the current addition requires ledger-based review. Professional attestation remains pending; VAT remains partial for the stated ordinary implementation gap.

[law]: https://logir.fo/Logtingslog/136-fra-08-09-1992-um-meirvirdisgjald-sum-seinast-broytt-vid-logtingslog-nr-28-fra-24
[reg]: https://logir.fo/Kunngerd/35-fra-20-03-2000-um-lutfalsligan-fradrattarraett-fyri-meirvirdisgjald-og-um-javnan-av-inngangandi-avgjaldi
[fuel]: https://www.logir.fo/Logtingslog/36-fra-15-05-2026-um-broyting-i-logtingslog-um-meirvirdisgjald-Meirvirdisgjaldslogin
[returns]: https://www.taks.fo/fo/vinna/mvg/at-lata-inn-mvg-uppgerd
[tourism]: https://www.taks.fo/fo/vinna/mvg/mvg-og-ferdavinna

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
