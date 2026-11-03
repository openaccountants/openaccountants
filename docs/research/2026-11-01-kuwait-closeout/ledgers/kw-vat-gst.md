# kw-vat-gst: figure and rule ledger

Guide: `skills/kuwait/kw-vat-gst.md`. Read date 2026-11-01. The source IDs, blob hashes and precise reading boundaries are preserved in [sources](../sources.md). [Immutable old-topic destinations](../old-topic-destinations.md) also preserve every substantive merge-base row and non-operative hold.

| ID | Guide section / rule or figure | Act, article, page | Exact decisive original-language quote | Official URL | Read date / SHA-256 / read scope |
|---|---|---|---|---|---|
| I1 | Rates, bands and thresholds / Deadlines and filing: Only proves list contents read; no VAT/excise legal absence established. All no-tax consequences held. | MOF visible laws index, financial/tax section | قوانين مالية وضريبية | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx | 2026-11-01; `931dff554b121c5e2a8164d66f64065b529739f84eab1ba6eb0b7b06912a0e56`; Current visible financial/tax laws title list read. Title absence cannot establish non-enactment. |
| I2 | Rates, bands and thresholds / Deadlines and filing: Title search only; no VAT/exciselegalabsence established. | MOF visible decree-laws index, financial/tax section | في مجال الشؤون المالية والضريبية | https://www.mof.gov.kw/MOFDesicions/mofDesicions2.aspx | 2026-11-01; `149446be443b2e5db98b9a6ace297a126955e94e6eca1230fbda4ee879e1249b`; Current visible financial/tax decree-law titles read, including DMTT157/2024 and1955/2008 laws. Not a complete gazette search. |
| I3 | Rates, bands and thresholds / Deadlines and filing: Index contents only; not nationwide legal-status opinion or electronicfilingwalkthrough. | MOF resolutions index, tax titles | قرارات | https://www.mof.gov.kw/MOFDesicions/mofDesicions3.aspx | 2026-11-01; `b3b731c103cd63b2458312de97698939c8c39bcbd56e67779ebbb8b0613aeb4c`; Current visible resolution titles read including income-tax, Zakat and DMTT material. Title absence cannot establish non-enactment. |

## Worked-case recomputation and non-legal instructions

The example inputs are stipulated facts, not legal thresholds. These exact cases are executed by `scripts/check-examples.py --require` and re-read by the fresh reviewer:

**Example 1.** A foreign supplier's invoice states KWD 1,000 net and KWD 200 foreign tax. The gross invoice is KWD 1,200. Record those components for review; the arithmetic does not establish that KWD 200 is deductible, refundable or a final cost.

```oa-check
name: Reconcile foreign invoice without assuming recoverability
inputs:
  net_price: 1000
  invoiced_foreign_tax: 200
steps:
  - invoice_total: net_price + invoiced_foreign_tax
expected:
  invoice_total: 1200.00
```

**Example 2 (decision).** A supplier quotes KWD 2,000 and proposes adding 5% labelled Kuwait VAT without providing the law. That proposal adds KWD 100 and produces a KWD 2,100 invoice. Request the legal basis and hold the disputed KWD 100 for review. Do not accept the charge or reject it as legally impossible solely from the GCC framework or an MOF index search. The 5% is the supplier's hypothetical proposal, not a verified Kuwait tax rate.

```oa-check
name: Quantify proposed disputed charge before deciding its legal basis
inputs:
  quoted_price: 2000
  supplier_proposed_rate: 0.05
steps:
  - disputed_charge: quoted_price * supplier_proposed_rate
  - proposed_total: quoted_price + disputed_charge
expected:
  disputed_charge: 100.00
  proposed_total: 2100.00
```

Intake questions collect facts, not legal answers. Portal URLs are entry points only: current authenticated screens, form fields, acknowledgement and payment-reference instructions are not claimed as read. Bank patterns in the routing Guide are search cues and exclude only automatic computation, never transaction history. Metadata, team attribution and general-reference notice are not accountant attestation.

## Non-operative source holds

NON-OPERATIVE HOLDS. The inherited assertions that Kuwait has no VAT/GST, no general consumption or sales tax, no excise, no registration, return, invoice tax, reverse charge, input recovery or penalties, and that foreign VAT is irrecoverable. Current enactment, commencement and implementation dates require affirmative official evidence. Historical GCC VAT Framework Agreement (2017), claimed 5% framework rate, GCC Excise Framework Agreement (2016) and Kuwait signature/domestic-adoption status have not been read at source. Historical customs 5% of CIF on most goods, higher tobacco/product rates and the description of customs as the main indirect tax remain unverified; customs.gov.kw access failure was reported by the prior writer, not treated as a source reading. Old domestic zero-VAT invoice cases and digital-services no-VAT conclusion must not be used as current tax advice.
