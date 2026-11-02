---
name: sj-svalbard-coal-export-duty
description: >
  Compute Svalbard coal-export duty for budget year 2026. Covers the
  exporter and producer liabilities, seasonal average FOB valuation,
  CIF freight and insurance adjustments, own-vessel bunker exclusion,
  cumulative tonnage bands, records, assessment, payment and appeal.
  Use for Svalbard coal duty, kullavgift, coal exports and shipping-season
  duty workpapers. Other minerals need their own charging decision.
  Reconciles the complete shipping season before applying the successive
  value-based bands, separates exporter and producer records, and checks
  shipment security against the actual requirement. Distinguishes the tax
  office assessment from the preparer's calculation and the appeal clock
  from the payment obligation. Flags the current filing format, annual
  coal-specific interest rate and quantities beyond the verified band
  schedule for confirmation before filing or payment.
jurisdiction: SJ
category: international
job: coal-export-duty
tax_year: 2026
last_updated: 2026-10-31
version: 0.1
tier: 2
---

# Svalbard: coal-export duty in 2026 v0.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source-cited draft.** Independent AI review is not accountant attestation.

## Who this applies to

The exporter of coal from Svalbard owes the duty imposed by the [2026 Storting decision FOR-2025-12-19-2781](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2781), administered under [Act of 17 July 1925 no.2 §§1–6](https://lovdata.no/dokument/NL/lov/1925-07-17-2). Where another person produced the exported material, that producer is jointly responsible for the corresponding part of the duty (§3).

The Act also supplies machinery for oil, other minerals and rock **if a charging duty has been imposed**. Its broad title does not itself impose the coal rate on every mineral. The verified annual decision here charges coal for budget year 2026. It is not authority for 2027 exports or a general mineral-production tax.

## Rates, bands and thresholds

All bands below are from the [complete 2026 coal-duty decision](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2781). Each percentage applies to the value of coal within that band. The band widths increase; they are not ten equal bands.

| Cumulative taxable tonnes in the shipping-season schedule | Width | Duty on that band's value | Official source |
|---|---:|---:|---|
| First 100,000 | 100,000 tonnes | 1.0% | https://lovdata.no/dokument/STV/forskrift/2025-12-19-2781 |
| Over 100,000 through 300,000 | 200,000 tonnes | 0.9% | same |
| Over 300,000 through 600,000 | 300,000 tonnes | 0.8% | same |
| Over 600,000 through 1,000,000 | 400,000 tonnes | 0.7% | same |
| Over 1,000,000 through 1,500,000 | 500,000 tonnes | 0.6% | same |
| Over 1,500,000 through 2,100,000 | 600,000 tonnes | 0.5% | same |
| Over 2,100,000 through 2,800,000 | 700,000 tonnes | 0.4% | same |
| Over 2,800,000 through 3,600,000 | 800,000 tonnes | 0.3% | same |
| Over 3,600,000 through 4,500,000 | 900,000 tonnes | 0.2% | same |
| Over 4,500,000 through 5,500,000 | 1,000,000 tonnes | 0.1% | same |
| Exporter/producer records | Submit by 31 December | Record and evidence obligation | [Act §3](https://lovdata.no/dokument/NL/lov/1925-07-17-2) |
| Payment and ordinary appeal | Each within six weeks from the statutory dispatch/availability event | An appeal does not suspend payment | [Act §§5–6](https://lovdata.no/dokument/NL/lov/1925-07-17-2) |

The cumulative limits are sums of the enacted successive widths. They are derived worksheet boundaries, not additional statutory rates. The decision does not state a further rate beyond its last listed band. Do not extrapolate a negative rate or assert a zero rate for quantities outside that verified schedule.

## The base

Use the exporter’s entire shipping-season record, not one vessel or invoice in isolation ([Act §§2–3](https://lovdata.no/dokument/NL/lov/1925-07-17-2)).

1. Identify exported coal by type, quantity, producer, achieved price and shipping costs. Reconcile vessel/loading records to sales invoices and producer accounts.
2. Exclude bunker coal the exporter uses in its own, hired or time-chartered ships under §2. Keep actual-use evidence. Do not exclude coal merely because a buyer later burns it as fuel.
3. At shipping-season end, establish the achieved average **FOB price per tonne**. For CIF sales deduct the paid freight and insurance to reach FOB. For hired/time-chartered ships, calculate average freight per tonne from actual costs. Where costs cannot be established, or the exporter uses its own ships, §2 calls for a discretionary freight valuation having regard to other paid freight and the circumstances. Do not enter an invented freight percentage.
4. For the supported cumulative schedule, calculate tonnes in each band as `max(0, min(total_tonnes, upper_limit)-lower_limit)`. Multiply each band's tonnes by the supported average FOB value and that band's rate. Sum the results. For mixed sales terms, reconcile all sales to the same FOB basis before calculating the average.
5. Show separately each producer's corresponding jointly liable share. Preserve the allocation and supporting producer accounts; do not treat producer payment as a second duty on the same coal.
6. Submit the statutory records and evidence to the tax office. The tax office **assesses the duty** under §4. Reconcile the office's assessment to the working paper before paying; the examples are calculations, not self-issued assessments.

**Shipment security:** [Act §2 fourth paragraph](https://lovdata.no/dokument/NL/lov/1925-07-17-2) allows the exporter to be required, at shipment, to provide security corresponding to a percentage of the cargo's estimated value, with further rules prescribed by the King. Establish whether such a requirement applies and retain its actual percentage, valuation and evidence of security. No fixed security percentage is supplied here; the annual duty rate is not an automatic security percentage.

The coal duty is distinct from company income tax. Reconcile its treatment in the company working papers under the relevant deduction/timing rules; do not subtract it from the coal-duty FOB base just because it is a tax cost.

## Deadlines and filing

[Act §3](https://lovdata.no/dokument/NL/lov/1925-07-17-2) requires a shipping-season book stating the exported goods' nature, quantity, producer, achieved prices and shipping expenses. Send it, with the prescribed evidence, to the tax office **by 31 December**. A separate producer sends a copy of its delivery accounts by the same date. Provide a representative in Norway where required by the section. Preserve proof of delivery and answer requests for additional information under §4.

The source prescribes records and the recipient, not an electronic form number. A current coal-specific electronic transmission route, departmental book format and form boxes have not been verified here. Confirm the tax office's accepted submission channel and prescribed evidence before the deadline; do not substitute the ordinary company income-tax return or a customs declaration for this separate book. This operational gap is explicit below.

Under [Act §5](https://lovdata.no/dokument/NL/lov/1925-07-17-2), the office sends the calculation by registered letter to the stated Norwegian address of the liable person/representative, or makes it available at the office in the specified nonresident/no-representative case. The ordinary appeal must **reach the tax office within six weeks** from that dispatch/availability event. An extension can be granted on application; it is not automatic. An appeal not fully accepted by the tax office proceeds to the Svalbard tax appeals board, with the opportunity for a further statement.

Payment is also due **within six weeks** of that event under §6. Pay the assessed sum even if appealing. If the final decision reduces it, the excess is refunded. Use the assessment's actual payment instructions and retain the reference, receipt and reconciliation; no account number or payment reference is invented here.

## Penalties and interest

[Act §6](https://lovdata.no/dokument/NL/lov/1925-07-17-2) imposes interest on overdue duty amounts of at least **NOK 100**, at the departmental rate fixed for the year. The current coal-specific annual rate has not been verified; do not import the ordinary income-tax arrears rate.

Under §4, failure to keep/submit the required book, accounts or requested information can forfeit the right to appeal unless sufficient excuse is established. Section 9 provides fines for the listed record and information failures; it does not set a flat fine in kroner.

Section 7 permits supplementary assessment at the Ministry's request where the exporter wholly or substantially escaped assessment. The ordinary request limit is **five years after the end of the year in which assessment should have occurred**, extended to **ten years for criminal conduct**. Death/dissolution has a separate **two-year** outer condition within those unexpired limits. Supplementary interest runs from **30 April of the year payment should have occurred**. Section 8 makes the duty an enforceable basis for execution. Keep these rules separate from ordinary company income-tax additional-tax percentages.

## Cross-border points

Export from Svalbard is the charging event in this decision. Do not replace achieved FOB valuation with a foreign customs value or assume the duty disappears because the exporter/producer is abroad. The Norway-representative, producer-account and assessment-delivery rules above remain relevant. Imports into the destination customs territory require a separate destination-country analysis.

## Two worked examples that recompute

**Single band.** The exporter ships 50,000 taxable tonnes in the season, with supported average FOB value NOK 1,000 per tonne. There are no bunker exclusions or other adjustments. Duty is NOK 500,000, subject to the tax office's assessment.

```oa-check
name: Svalbard coal export duty first band 2026
inputs:
  tonnes: 50000
  fob_per_tonne: 1000
steps:
  band_value: tonnes*fob_per_tonne
  duty: band_value*0.01
expected:
  band_value: 50000000
  duty: 500000
```

**Bunker exclusion, CIF conversion and band crossing.** Total outward coal is 155,000 tonnes, including 5,000 tonnes actually used as qualifying own-vessel bunker coal. The 150,000 taxable tonnes have CIF sales of NOK 165 million; paid freight is NOK 15 million and insurance NOK 3 million, all attributable to those taxable sales. FOB value is NOK 147 million, average NOK 980 per taxable tonne. Duty is NOK 980,000 on the first 100,000 tonnes plus NOK 441,000 on the next 50,000: NOK 1,421,000. Applying the first-band rate to all coal would overstate the duty by NOK 49,000. Neither the bunker exclusion nor the freight amounts are presumed without evidence.

```oa-check
name: Svalbard coal CIF bunker and second-band decision 2026
inputs:
  outward_tonnes: 155000
  qualifying_bunker_tonnes: 5000
  taxable_sales_cif: 165000000
  paid_freight: 15000000
  paid_insurance: 3000000
steps:
  taxable_tonnes: outward_tonnes-qualifying_bunker_tonnes
  fob_value: taxable_sales_cif-paid_freight-paid_insurance
  average_fob: fob_value/taxable_tonnes
  first_band: min(taxable_tonnes,100000)*average_fob*0.01
  second_band: max(0,min(taxable_tonnes,300000)-100000)*average_fob*0.009
  duty: first_band+second_band
  incorrect_flat_duty: fob_value*0.01
  overstatement: incorrect_flat_duty-duty
expected:
  taxable_tonnes: 150000
  fob_value: 147000000
  average_fob: 980
  first_band: 980000
  second_band: 441000
  duty: 1421000
  overstatement: 49000
```

## Ask the client first

- What coal was exported in the complete shipping season, and who exported and produced it?
- What quantities and achieved prices do invoices, vessel records and producer accounts prove?
- Which sales are CIF or FOB, and what paid freight/insurance or discretionary freight valuation supports the conversion?
- Which coal was actually used as qualifying bunker coal, and in whose vessels?
- Have the prescribed book/accounts been delivered, and what assessment, representative, dispatch date and payment instructions exist?
- Are there unassessed exports, an appeal or an outstanding payment requiring the actual annual interest rate?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Enacted coal-export duty decision for budget year 2026, entire schedule | https://lovdata.no/dokument/STV/forskrift/2025-12-19-2781 | 2026-10-31 |
| Coal/mineral export duty Act of 17 July 1925 no.2, complete §§1–11 | https://lovdata.no/dokument/NL/lov/1925-07-17-2 | 2026-10-31 |

Not yet confirmed: Current coal-specific electronic filing channel/departmental book format and prescribed evidence, the current coal-duty late-interest rate, and treatment of exports beyond the last enacted band shown. Other minerals need an actual charging decision. No invented form, rate, destination duty or permanent exemption is supplied. This Guide supplies the enacted ordinary coal computation and statutory process; the operational limits prevent a claim that this job is fully verified for filing.
