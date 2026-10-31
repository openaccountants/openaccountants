---
name: kosovo-vat
description: >
  Calculate ordinary Kosovo VAT for the 2026 tax year using current primary law and its amendments. Covers domestic and foreign registration, calendar-year turnover, standard and reduced rates, supply timing and value, eligible and blocked inputs, mixed taxable and exempt recovery, capital adjustments, stock credits, bad debts, refunds, invoices, monthly returns, imports, exports, foreign-service reverse charge and domestic construction. Distinguishes exemptions with and without recovery, services outside Kosovo, and specialist schemes whose separate implementation evidence is required. Use for TVSH, VAT returns, TV forms, purchase and sales books, reverse-charge invoices, input recovery, registration and VAT reconciliation. Preserves the distinction between an operative tax charge and an unconfirmed simplified procedure.
version: 2.1
jurisdiction: XK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Kosovo VAT v2.1

Tax year **2026**, checked against the law on **30 October 2026** (tier 2;
no licensed accountant has signed off this revision). Kosovo VAT (TVSH, tatimi
mbi vlerën e shtuar) is charged and paid in EUR. Apply VAT Law 05/L-037 with
the amendment 08/L-276 (published 27 December 2024, in force fifteen days
later under its art. 55), not the original PDF in
isolation. The Official Gazette lists no other amendment to the VAT law in
force for 2026.

## Who this applies to

A person independently carrying on economic activity is a taxable person under
arts. 3–5, whether profitable or not. Kosovo VAT applies to taxable domestic
goods/services and imports. Employees acting under their employer's direction
are not independent taxable suppliers merely because they receive wages
([05/L-037 arts. 3–5](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf)).

A Kosovo-established taxable person must register when calendar-year turnover
**exceeds EUR 30,000**. Article 6(1) taxes the part of the crossing supply that
exceeds the threshold; notify TAK within fifteen calendar days, effective from
the crossing date. Do not use a rolling twelve-month test, wait until the next
month or charge the full year's previously below-threshold receipts. Aggregate
the individual's businesses/locations under the registration rules. A person
who does not notify in time is registered compulsorily by TAK with retroactive
effect from the date the threshold was exceeded (art. 7(2)). Eligible persons
below the boundary can register voluntarily; TAK registers them from the date
it receives the request (arts. 6–8).

For the registration calculation, AI 03/2015 art. 7(1) includes supplies at
all rates and supplies exempt with or without input-credit rights. Do not
count only the 18% sales or assume that exempt turnover disappears from the
test. Registration does not turn an exempt supply into a taxable one.

Foreign suppliers have registration from the beginning of Kosovo economic
activity, without the domestic turnover allowance. Appoint a tax representative
and register within five days after appointment and before activity starts,
except where the only supplies fall within the recipient-liability cases in
art. 52(1.2)–(1.3) (arts. 6(5), (7)–(8), 52(5)).

This skill supplies the ordinary VAT calculation, including mixed use,
imports/exports, foreign services and domestic construction reverse charge.
Travel-agent/used-goods margins, flat-rate farmers, investment gold, tourist
refunds and the Albanian electricity-exchange special regime need their own
scheme evidence. They do not replace the ordinary rules.

## Rates, bands and thresholds

Amounts are EUR. The table applies to 2026, subject to the stated transaction
and period conditions.

| Item | Figure or rule | Official authority |
|---|---|---|
| Standard VAT | 18% | [05/L-037 art. 26(1)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Reduced VAT | 8%, only for the supplies and imports listed in art. 26(2) (below) and Annex 1 of the instruction; not all food, medical or IT expenditure | [Art. 26(2)–(3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [AI 03/2015 art. 36 and Annex 1](https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079) |
| Exempt with input recovery (no output VAT) | Exports, international vessel/aircraft supplies, international air and rail passenger transport, diplomatic/international-organisation/NATO-KFOR supplies, irrigation and Annex IV agricultural inputs | [Arts. 31–35, 36(3.2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Domestic compulsory registration | Calendar-year turnover above EUR 30,000 | [Arts. 6–7](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Registration notification | Fifteen calendar days from the obligation; effective crossing date | [Art. 7](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Foreign supplier representative/registration | Five days after appointment and before activity, subject to recipient-liability exception | [Art. 6(5)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Ordinary period and return/payment | Calendar month; by the following month's 20th | [Arts. 53–54](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Omitted input deduction | No later than the final tax period of the following calendar year | [Art. 38(2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Mixed private/business car costs | Maximum 50% input recovery, subject to use/eligibility | [Art. 36(5.2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Capital adjustment period | Five calendar years for capital goods; twenty for immovable property, including first-use year; no annual adjustment where the difference in the deductible proportion is less than 3% of the input VAT | [Art. 41(2)–(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Ordinary VAT-credit refund conditions | Three consecutive credit months; credit exceeds EUR 3,000 at end of third month; all past returns filed | [Art. 40(1)–(2.1)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Exporter refund route | Each period if credit exceeds EUR 3,000, customs/VAT compliance and past returns complete | [Art. 40(2.2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| General overpayment refund claim/review | Claim within three years of payment/right arising; TAK review within thirty calendar days | [08/L-257 art. 26(3)–(4)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| VAT bad-debt timing | At least six months after the relevant VAT period; initiate declaration procedures within twenty-four months of payment obligation | [05/L-037 art. 43](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [AI art. 64](https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079) |
| Records | At least six years; immovable-property documents twenty years under VAT-specific rules | [Arts. 56–57](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |

The 8% list in art. 26(2) covers, for supply and import: water other than
bottled water; electricity including transmission and distribution, central
heating, waste collection and other waste treatment; grains (barley, maize,
oats, rye, rice, wheat); grain products for human consumption (flour, pasta,
bread and similar); cooking oils from grains or oilseeds; dairy products; salt
for human consumption; eggs; textbooks and serial publications; books,
library lending and specified printed matter; information technology
equipment; medicines, pharmaceutical products and medical/surgical instruments
and devices; and medical equipment and aids for exclusive use by disabled
persons (including repair) and children's car seats. Use the actual legal
description and Annex 1 code. Any other taxable supply or import is 18%.

Agricultural inputs are not 8% items. Irrigation of farming land and the
goods in Annex IV of the law (breeding animals, seed, animal feed,
fertilisers, plant-protection products and listed agricultural machinery)
are exempt with input recovery (art. 33(2), art. 36(3.2)), and their import is
exempt (art. 29(2)). Determine an import exemption first: art. 29(1.10)–(1.12)
and AI art. 48 separately cover production lines and machinery, qualifying
production raw materials and IT equipment. A reduced domestic rate is not
proof that an otherwise exempt import bears that rate.

## The base

### Output VAT and time of supply

Use consideration received/receivable, including price-linked subsidies and
supplier-charged incidental costs, excluding VAT. Include non-VAT duties and
taxes; exclude qualifying discounts and evidenced disbursements in the
customer's name/on their behalf. Non-cash consideration and specified connected-
person transactions require the art. 24 open-market rules. A bank reference
alone does not establish the consideration, rate or tax treatment (art. 24).

Ordinary VAT is chargeable on supply. An earlier invoice or advance payment
can bring chargeability forward, on the amount paid in the latter case.
Continuous supplies and staged/long-term contracts have the timing in
art. 22(2), including interim certificates and year-end work measurement.
Do not postpone all construction VAT until final cash settlement. Imports
use the customs event rules in art. 23. Customs value plus the specified
non-VAT duties and incidental costs to the relevant destination determines
the import base (art. 25).

For a VAT-exclusive taxable amount `B`, output VAT is `B * rate`; for an
inclusive price `G`, extract `G * rate / (1 + rate)`. Split mixed-rate invoice
lines rather than applying an average guessed rate. Correct price/quantity
changes with linked debit/credit notes and adjust both parties' VAT records
(arts. 24–26, 41, 47; AI arts. 34–36, 65).

### Exemptions and input recovery

Classify three different outcomes: domestic taxable supply, exemption without
input recovery, and export/treatment carrying recovery. General B2B services
whose place is outside Kosovo are not a domestic zero-rated sale merely
because the customer is foreign. Arts. 27–28 exempt, without input recovery,
specified public-interest, financial, insurance and property transactions,
with their conditions. They include hospital and medical care, dental
technicians' services and dental prostheses, welfare, education and vocational training by recognised bodies,
newspapers and periodicals, public radio/television, public transport at
state-fixed prices, life and health insurance and reinsurance (not other
insurance classes), lending, payments, deposits, currency and securities
dealings (not debt collection), postal and fiscal stamps at nominal value,
gambling, land, residential houses/apartments, and leasing of immovable
property. Hotel accommodation, parking, permanently installed equipment and
machinery, safe boxes and commercial immovable-property leasing (other than
land) are excluded from the leasing exemption, so residential leasing stays
exempt and commercial leasing is taxable. International road passenger
transport is exempt without recovery under art. 28(4), unlike international
air and rail passenger transport, which art. 33(4) exempts with recovery. A
residential label does not decide every property transaction
([Arts. 27–28, 33](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf)).

Deduct eligible input VAT only when it is chargeable, the necessary invoice
or customs SAD is held, and the goods/services serve transactions with a
right to deduct. Import VAT is paid at customs at the same 18% or 8% rate as
the domestic supply and is deducted only with an SAD naming the taxable person
as consignee or importer (arts. 26(2), 36(2.2), 37(2.1), 52(3)). Article 36(3) preserves recovery for the specified foreign
activities and exports; do not disallow export inputs just because no domestic
output VAT is collected. No deduction arises from VAT wrongly charged by an
unauthorised supplier or above the lawful amount, even if paid. Correct the
supplier document instead (arts. 36–38).

Directly attribute inputs first. Art. 36(5.1) blocks input VAT on sport and
recreation yachts and boats, private aircraft, and cars and motorcycles used
only for non-business purposes, with their fuel, lubricants, spare parts and
closely linked services. It does not block vehicles used for leasing, renting
or resale, driving-school vehicles, or public and special line transport
vehicles (the last only for the share used in that activity). Block
representation costs (hosting and entertainment, including food, drinks and
accommodation) under art. 36(5.3), limit mixed private/business cars to 50%
under art. 36(5.2), apply immovable-property business-use apportionment, then apply art. 39 to genuinely
shared taxable/exempt inputs. Its ordinary proportion is eligible turnover
divided by eligible plus non-eligible turnover, with the statutory denominator
and exclusions. Exclude business capital-asset disposals and incidental
financial services; round the annual percentage **up** to the next integer.
Use the provisional prior-year ratio/eligible forecast, then reconcile the
actual year in the following January return. Real-use or separate-sector
methods require the specified TAK authority/notification and records
([Arts. 36(4)–(5), 39](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf)).

Adjust capital input tax over one-fifth or one-twentieth each year for the
change in recovery entitlement; under art. 41(4) no adjustment is made where
the difference in the deductible proportion is less than 3% of the input VAT.
A capital disposal during the adjustment period can require a single
remaining-period adjustment. New-registration stock credit needs an inventory,
supporting invoices and the conditions in art. 42; that stock deduction does
not itself confer a cash-refund right. Self-supplies, private withdrawal and
retained goods at cessation require arts. 11–12, 15–16 and 24(7), rather than
simply leaving the assets out of the final return.

### Bad debts and credit balances

Bad-debt relief is not automatic after six unpaid months. Establish court-
procedure requirements/the art. 43(5) EUR 500 exception, collection efforts,
proper timing and the bad-debt invoice. Related-party bad debts and repeated
transactions with the same debtor are restricted; AI art. 64(2) disapplies
the repeated-transactions restriction (art. 43(6.1)) for businesses carrying
out activities of general interest. Start declaration procedures within
twenty-four months. A later recovery creates the corresponding restored VAT
and linked "bad debt paid" invoice. The original Albanian art. 43(6.2) says
**related parties**; the English PDF's "contracted parties" mistranslation
must not exclude every debt arising from a contract
([Art. 43, original Albanian](https://gzk.rks-gov.net/ActDetail.aspx?ActID=11015&langid=1); [AI arts. 64–66](https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079)).

Carry excess eligible credit forward or claim a refund when the statutory
conditions are met. The ordinary and exporter routes in art. 40 are distinct;
keep all prior returns, customs and invoice evidence. Apply the general
procedure art. 26 to tax-debt offsets, claim time limits, thirty-day review
and refund interest where due. Under 08/L-257 art. 26(7), where a taxpayer has
been in credit for more than three consecutive months and owes tax debt above
EUR 5,000, TAK assesses the VAT credit, applies a valid credit against the debt
and refunds the rest. TAK retains a refund while required evidence is missing
or the return data is documented as incorrect, with no late-refund interest
for that retention period (VAT art. 40(3)). A pending supported refund is not permission
to stop filing, and a credit balance alone does not prove an immediate cash
entitlement. Document any legally retained amount and the reason
([VAT art. 40](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [08/L-257 art. 26](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)).

## Deadlines and filing

| Obligation | Action and deadline | Official authority |
|---|---|---|
| Compulsory/voluntary VAT registration | Notify within fifteen calendar days of compulsory trigger; voluntary registration effective on valid request | [Arts. 6–8](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| VAT return/payment | TV through TAK EDI, by 20th following the monthly period | [Arts. 53–54](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Purchase/sales books | LB and LSH monthly, by 20th with the VAT cycle | [TAK current timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/); [08/L-257 art. 43](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf) |
| VAT refund request | KRR form, from the 1st to the 20th of the month, once the art. 40 conditions are met | [Art. 40](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Invoice | Before the 15th of the month following the chargeable-event month | [Art. 44(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Cessation notice | Within fifteen days after activity ceases | [Art. 9(3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |
| Optional deregistration | Prior calendar-year supplies below threshold; TAK approval, two-month effect; minimum registration lock-in applies | [Art. 9(1)–(2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf) |

An approved below-threshold deregistration cannot occur during the registration
year or at least one additional calendar year. For a partial registration/
deregistration month, use the actual first/last period under art. 53; do not
invent a full extra month of liability. Liquidation/bankruptcy has its own
period and ongoing-monthly-return rules (arts. 9 and 53).

Invoices need the statutory date/sequence, fiscal/VAT identifiers, parties,
transaction description/date, base/rate/VAT and exemption/reverse-charge
reference as appropriate. Retain invoice originals/copies, customs documents,
linked notes, contracts and bank evidence under arts. 44–57. Reconcile output,
eligible input, reverse charge, adjustments and carried credit before settling
net VAT; do not invent EDI return-box numbers from an old form.

## Penalties and interest

Use current procedure Law 08/L-257, not the repealed 03/L-222 cited in older
instructions. Art. 99 charges EUR 50 per missed mandatory liability-producing
return for a business natural person, EUR 150 for a legal entity and EUR 20
for a non-business natural person. Art. 100(1) charges 15% of the understatement/
excess-credit difference where at most 10% of correct tax, and 25% where
larger. Art. 100(4) controls the overlap with art. 101. Failure to submit the
required electronic books is subject to art. 43(4)/101(1): EUR 150 for each
missing/inaccurate/incomplete statement, maximum EUR 3,000
([08/L-257 arts. 43, 99–101](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)).

Interest under art. 24 runs for each month or part-month, at most ten years,
at the Minister's rate published by TAK. A compliant instalment agreement
stops it from the following month; default reinstates it. The numeric 2026
rate is not confirmed here. Do not calculate arrears from a historical rate
or a rate for commercial debts.

## Cross-border points

Goods without transport are located where present on supply; transported
goods where dispatch or transport to the customer begins, with installation/assembly and gas/
electricity exceptions (art. 19). General B2B services follow the recipient's
business/receiving fixed establishment; general B2C follows the supplier.
Immovable property, event admission/activities, transport, catering and short-
term vehicle hire have the specific art. 20 rules. Obtain the actual service
and establishments before applying a foreign-customer shortcut.

For Kosovo-place supplies by a non-established supplier to a Kosovo VAT-
registered recipient, art. 52(1.2) makes the recipient liable, with
its express event-admission exception. Self-assess output VAT and separately
test input recovery; equal output and input is conditional on full entitlement,
not inherent in reverse charge. An unregistered recipient does not inherit
that clause simply by calling itself a business.

Domestic construction reverse charge follows AI 03/2015 art. 70 as amended
by AI 06/2016 art. 6: the listed construction services between VAT-declaring
taxable persons fall within recipient liability, regardless of contract date.
The amendment deleted the old construction-permit limitation. The supplier
issues a referenced reverse-charge invoice; the recipient accounts for VAT
and tests recovery. Do not extend that rule to every material-only sale or
to a consumer. Art. 52(1.4) also lets the Minister extend recipient liability
by sub-legal act to staff supplied for construction, scrap and waste, goods
given as security, retention-of-title goods and, as split out by 08/L-276
art. 48, immovable property sold by a judgment debtor in a compulsory sale.
Apply those categories only where an implementing act covers them ([VAT art. 52](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf); [AI art. 70](https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079);
[AI 06/2016 art. 6](https://gzk.rks-gov.net/ActDetail.aspx?ActID=13130)).

Export goods require actual dispatch/customs evidence under art. 31; a foreign
billing address alone is insufficient. Distinguish the exemption with input
recovery from a service outside Kosovo and from a domestic exemption without
recovery (art. 36(3)). Imports use arts. 23, 25 and 29–30, including the stated
production/IT approval procedures in AI art. 48.

For foreign electronic/telecom/broadcast supplies to Kosovo consumers, apply
the specific place rule. Law 08/L-276 art. 49 replaced VAT art. 61 with authority
for a ministerial special scheme; the original 2015 scheme text is not the
current provision. This skill does not cover a simplified registration
route whose implementing act is not confirmed here. Tourist refund commencement is also separate: AI 01/2018
art. 2 replaced the earlier fixed date with a capacity/infrastructure condition
for AI art. 51. Both are named specialist scope limits, not a basis to assume
no VAT on an otherwise taxable supply
([08/L-276 arts. 48–49](https://gzk.rks-gov.net/ActDetail.aspx?ActID=100032&langid=2); [AI 01/2018 art. 2](https://gzk.rks-gov.net/ActDetail.aspx?ActID=16042)).

## Two worked examples that recompute

### 1. Ordinary domestic month

Assume a VAT-registered trader, all sales domestic at 18%, EUR 10,000 VAT-
exclusive sales and EUR 5,000 fully eligible domestic purchases at 18%.
Valid invoices are held and no private/exempt-use, timing, credit or adjustment
restriction applies. Output VAT is EUR 1,800; input EUR 900; payment EUR 900.
The customer invoices total EUR 11,800. Costs stated here are hypothetical.

```oa-check
name: Kosovo ordinary domestic VAT month 2026
inputs:
  net_sales: 10000
  eligible_net_purchases: 5000
steps:
  - output_vat: net_sales * 0.18
  - input_vat: eligible_net_purchases * 0.18
  - net_vat_due: output_vat - input_vat
  - gross_customer_invoices: net_sales + output_vat
expected:
  output_vat: 1800
  input_vat: 900
  net_vat_due: 900
  gross_customer_invoices: 11800
```

### 2. Foreign service with partial recovery

Assume a Kosovo VAT-registered recipient buys a EUR 1,000 ordinary consultancy
service from a supplier with no Kosovo establishment. The receiving business
is in Kosovo and no special place/admission rule applies. It is a genuinely
shared cost, with a lawfully established art. 39 recovery fraction of 60,000/
100,000, or 60%, and no further blocked-input restriction. Reverse-charge
output is EUR 180; recoverable input is EUR 108. This transaction therefore
adds EUR 72 payable; it is not automatically VAT-neutral.

```oa-check
name: Kosovo foreign service reverse charge with mixed recovery 2026
inputs:
  service_fee: 1000
  eligible_turnover: 60000
  total_relevant_turnover: 100000
steps:
  - recovery_percentage: ceil(eligible_turnover / total_relevant_turnover * 100)
  - reverse_charge_output: service_fee * 0.18
  - permitted_input: reverse_charge_output * recovery_percentage / 100
  - net_transaction_vat: reverse_charge_output - permitted_input
expected:
  recovery_percentage: 60
  reverse_charge_output: 180
  permitted_input: 108
  net_transaction_vat: 72
```

## Ask the client first

1. What are the registration date, calendar-year turnover by activity, establishments and any representative or deregistration decision?
2. What goods/services, classifications, supply/advance/invoice dates and VAT-inclusive/exclusive prices apply?
3. Where are the goods, customers, receiving establishments, property/events and actual transport, and what customs/export evidence exists?
4. Which inputs are directly taxable, exempt, private, shared or blocked, and what recovery method and asset history are supported?
5. What credit, stock, capital-use changes, unpaid debts, linked notes and prior returns need reconciliation?
6. Do construction reverse charge, a particular exemption approval or a specialist scheme change the required treatment?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| VAT Law 05/L-037 arts. 3–9, 19–43, 44, 52–57 and Annex IV | https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L-037_ON_VALUE_ADDED_TAX___ANNEX.pdf | 2026-10-30 |
| Official Gazette record of 05/L-037 and its amendments (only 08/L-276 listed) | https://gzk.rks-gov.net/ActDetail.aspx?ActID=11015&langid=2 | 2026-10-30 |
| Original Albanian law, art. 43(6.2) related-party restriction | https://gzk.rks-gov.net/ActDetail.aspx?ActID=11015&langid=1 | 2026-10-30 |
| Law 08/L-276 arts. 48–49 and 55, amended VAT arts. 52 and 61 | https://gzk.rks-gov.net/ActDetail.aspx?ActID=100032&langid=2 | 2026-10-30 |
| AI 03/2015 arts. 7 and 64 (registration turnover, bad-debt 24 months and general-interest exception) | https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079 | 2026-10-30 |
| AI 03/2015 arts. 36, 48, 51, 65–66, 70 and Annex 1; read with amendments below | https://gzk.rks-gov.net/ActDetail.aspx?ActID=11079 | 2026-10-24 |
| AI 06/2016 arts. 4–6, construction amendment and prior tourist-date provision | https://gzk.rks-gov.net/ActDetail.aspx?ActID=13130 | 2026-10-30 |
| AI 01/2018 art. 2, replacement tourist-refund commencement condition | https://gzk.rks-gov.net/ActDetail.aspx?ActID=16042 | 2026-10-30 |
| Current tax-procedure Law 08/L-257 arts. 24, 26, 43, 99–101 | https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf | 2026-10-30 |
| TAK current TV/LB/LSH/KRR timetable | https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/ | 2026-10-30 |

Not yet confirmed: numeric 2026 tax late-interest rate; current instruments for the amended electronic-services special scheme and tourist-refund operational commencement; whether any sub-legal act implements recipient liability under VAT art. 52(1.4.2)–(1.4.7) beyond construction services (AI 03/2015 art. 70); full current Annex 1 code list of AI 03/2015 for 8% goods.

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
