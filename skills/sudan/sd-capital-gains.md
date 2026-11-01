---
name: sd-capital-gains
description: >
  Prepare Sudan capital asset disposal workpapers for 2026 intake under the separate Capital Gains Tax Act 1986 and its opened signed 2019 rate amendment. Match Sudan capital gains, property sale, share disposal, gifts, deemed market value, loss carryforward and ضريبة الأرباح الرأسمالية questions. Covers individuals, companies, nonresident agents and estates, with cost evidence, representative liability, residential relief conditions and tax clearance before registration. Distinguish assets already within income tax balancing treatment from the separate capital gains charge. The later enacted chain and current forms remain unresolved. This Guide supports a broad source baseline calculation and document handoff, with explicit stops before assuming an exemption, transfer clearance or operative 2026 rate.
version: 0.2
jurisdiction: SD
tax_year: 2026
tax_year_notes: "2026 intake; opened historical statutory baseline only; later enacted chain unresolved"
last_updated: 2026-11-01
category: international
tier: 2
---

# Sudan capital asset disposal gains v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **2026 intake, partial statutory baseline.** Figures below reproduce identified opened instruments, not a completed operative 2026 consolidation. Before filing, paying, granting relief or advising registration, reconcile later enacted amendments and obtain the missing regulations, current forms and directions named in Sources. Passing arithmetic or format checks does not clear this gate. Amounts are source-period SDG; no currency redenomination or indexation is assumed.

## Who this applies to

Actual/deemed transfers of capital assets under a SEPARATE Act, including real property, vehicles, factories, intangibles and share interests. Company assets already subject to income-tax balancing treatment are excluded by s.5(2); classify that interaction first. This Guide corrects the old 20% capital-gain assertion but does not certify the opened 3% amendment as unchanged through 2026.

## Rates, bands and thresholds

| Item | Opened source wording and conditions | Official source |
|---|---|---|
| Opened signed 2019 rate | 3% of taxable GAIN under amended ScheduleII, replacing 2%; not 3% of sale proceeds. Later-law gate remains. | [Capital Gains Tax Amendment2019 s.2; PDF1](https://tax.gov.sd/wp-content/uploads/2025/02/law23.pdf) |
| Capital loss carryforward | No more than 3 years under s.8; separate from income-tax business losses. | [s.8; PDF8](https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf) |
| Sole home/land individual relief | 25% of SALE VALUE, only on the ScheduleI residential-plan/replacement conditions, once in lifetime; not an automatic 25% gain exemption. | [ScheduleI; PDF15](https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf) |
| In-kind revaluation condition | ScheduleI relief condition prohibits relevant asset/share disposal for 4 years; obtain all other conditions. | [ScheduleI; PDF15](https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf) |
| Payment/clearance | Pay within 30 days of assessment letter, subject to valid extension; obtain clearance before asset registration/transfer. | [ss.22–24; PDF12–13](https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf) |
| Initial objection | Written notice to the Secretary General within 30 days OF THE ASSESSMENT DATE, precisely stating the grounds, under s.20(1). That provision does not require a return for the initial objection; current additional form requirements remain unresolved. Further stages have separate payment/time conditions. | [s.20(1)–(2), s.21; PDF12](https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf) |

## The base

1. Identify asset, beneficial owner, legal/de facto transfer, transaction date and consideration. Reconcile company capital allowances/balancing adjustments so the same disposal is not blindly charged twice.
2. Review s.6 deemed market-price treatment for transfers outside the listed close-family/public-purpose categories. A listed relationship does not itself resolve every other charging provision. Document valuation and any gift/donor liability.
3. Under s.7 establish purchase/build cost, qualifying improvements, selling costs, planning-price difference and permitted prescribed costs, each with evidence. Do not substitute gross sale proceeds for net gain.
4. Track each capital loss and the s.8 carryforward window. Loss classification and support precede any offset; income-tax business loss figures are not imported.
5. For ScheduleI home/land relief obtain proof this is the person's only qualifying residential home/land, the residential-plan or timely replacement condition and prior lifetime use. The 25% amount references sale value; do not treat it as a universal full exemption. For in-kind revaluation obtain the required no-disposal and entity evidence.
6. Identify nonresident agent, donor, executor/administrator and other representative liability under ss.11–16. Retain enough assets to pay the tax and keep assessment/clearance evidence before distributing or registering ownership.

## Deadlines and filing

Assemble sale/transfer instrument, ownership/cost evidence, valuation, relief/loss schedule and taxpayer/representative details. Sections 17–19 provide assessment/return powers; the current form and portal boxes were not obtained. After receiving the assessment letter, apply s.22 payment timing and any written s.23 extension. Obtain the s.24 clearance certificate before registration/transfer; a tax calculation is not clearance. Preserve objection notices, acknowledgement and payment receipt. No actual asset registration, return, payment or clearance application was made.

## Penalties and interest

Section 27 contains offence/sanction provisions, and ss.20–21 provide staged objections. Current amended monetary penalties, court fees and procedural changes remain unconfirmed; do not invent a late-payment percentage or treat an objection as automatic suspension.

## Cross-border points

The Act expressly addresses nonresident agents and representatives. Establish domestic source, residence and the actual treaty/order through [cross-border](sd-cross-border-residence.md), rather than assuming foreign ownership eliminates local gain taxation. Gift, estate and incorporation relief need their exact statutory conditions.

## Two worked examples that recompute

### Net gain rather than proceeds

Assume taxable disposal outside income-tax balancing treatment: sale 1,000,000 less evidenced cost 600,000, improvements 100,000 and sale expenses 20,000 =gain 280,000. The opened 3% source-period rate gives 8,400;3% of gross price would wrongly give 30,000.

```oa-check
name: Capital gain net cost bridge
inputs:
  price: 1000000
  cost: 600000
  improvement: 100000
  selling: 20000
steps:
  - gain: price-cost-improvement-selling
  - tax: gain*0.03
  - incorrect_gross_tax: price*0.03
expected:
  gain: 280000
  tax: 8400
  incorrect_gross_tax: 30000
```

### Capital loss support and expiry decision

With current gain200,000 and a150,000 supported loss still inside the statutory carryforward period, illustrative net gain50,000 produces1,500 at the opened3% rate. If the loss is outside the period or unsupported, the base stays200,000 and tax6,000;4,500 is held pending evidence, not automatically claimed.

```oa-check
name: Capital loss eligible versus held
inputs:
  gain: 200000
  loss: 150000
steps:
  - eligible_base: max(gain-loss,0)
  - eligible_tax: eligible_base*0.03
  - held_tax: gain*0.03
  - difference: held_tax-eligible_tax
expected:
  eligible_base: 50000
  eligible_tax: 1500
  held_tax: 6000
  difference: 4500
```

## Ask the client first

- Asset, legal/beneficial owner, source, transfer date and consideration.
- Acquisition/build/improvement/sale evidence and any independent valuation.
- Company depreciation/balancing treatment and loss-year records.
- Relationship to recipient, gift/estate/representative authority.
- Residential relief evidence, replacement date and prior lifetime use.
- Assessment, objection, payment and transfer-clearance deadlines.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| capital-gains-en; selected ss.3,5; PDF 5–7; s.6; PDF 7; s.7; PDF 7–8; s.8; PDF 8; ss.22–24; PDF 12–13; ScheduleI; PDF 15; s.20(1)–(2), s.21; PDF 12; ss.11–16; PDF 9–10 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/Capital-Gains-.pdf | 2026-11-01 |
| law 23; selected Capital Gains Tax Amendment 2019 s.2; PDF 1 read; not a full current consolidation | https://tax.gov.sd/wp-content/uploads/2025/02/law23.pdf | 2026-11-01 |

Writer short-quote ledger: [evidence/ledgers/sd-capital-gains.md](../../evidence/ledgers/sd-capital-gains.md). Source hashes and actual read scopes are in the Sudan source manifest/read record. Independent review is pending; preserved platform attribution is historical metadata, not a new review of this version.

Not yet confirmed: Full later enacted capital-gains chain and current rate/base adjustments, current return and clearance form/portal, loss application details, complete ScheduleI government/charitable/diplomatic/reorganisation relief conditions, court/committee objection payment amounts and current sanctions. Residential relief is not automatically full or repeatable. No current stamp-duty/property registration fee or local property tax is approved here. Residual claims in all legacy-topic controls listed above remain held until individually reconciled.
