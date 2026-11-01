---
name: bj-vat-gst
description: "Benin 2026 VAT: prepare a monthly calculation for confirmed VAT taxpayers, classify exemptions and zero-rated exports, test deduction conditions and the BTP fuel limit, and screen foreign/platform transactions under the June rectifying law. Threshold instrument and completed filing remain unresolved. Two executable cases; no accountant attestation."
jurisdiction: BJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Benin monthly VAT working paper v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Prepare a monthly Benin VAT working paper in 2026 for a business whose registration/status and the classification of its transactions have been established. The charge covers independent economic supplies, including electronic-commerce sales and platform commissions. A person must not decide registration from the legacy turnover-threshold assertion: article 228 delegates the threshold to a ministerial order, which was not obtained for this draft. [CGI 2026, art. 223](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=100) [CGI 2026, art. 224](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=100) [CGI 2026, art. 226](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=102) [CGI 2026, art. 228](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103)

The code distinguishes persons within scope from persons required to charge VAT. Falling below the threshold does not immediately end obligations: article 226 retains them for three consecutive exercises. The article 229 small-business exemption has government-customer and fiscal-flagrance exceptions. Voluntary option under article 225 has its own application and eligibility conditions. Hold status changes until the actual threshold instrument and facts are checked. [CGI 2026, art. 225](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=101) [CGI 2026, art. 226](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=102) [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103)

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Ordinary rate | 18% of the applicable taxable base | [CGI 2026, art. 241](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=116) |
| Qualifying exports | Zero rate under article 230, with the export/assimilated-operation and deduction conditions; not every foreign-customer invoice is an export | [CGI 2026, art. 230](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=111) |
| Books and newspapers | Books exempt; composition/printing/sales of newspapers and periodicals exempt except advertising, announcements and similar receipts | [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103) |
| Medical and educational services | The specified medical/hospital services exclude veterinary care; education must fit the public/private/assimilated institution conditions and does not exempt uniform or other unrelated goods sales | [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103) |
| Food and agriculture | Use article 229(2)(b) product wording, origin/processing conditions and article 229(16) agricultural activities. No exemption for every processed food business is inferred | [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103) |
| Banking and insurance | Specified operations subject to TAFA fall under article 229(12), rather than an exemption for everything supplied by the sector | [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103) |
| Domestic gas | Gas for domestic use under article 229(17); the separate 2026 cylinder/accessory rule has its own goods and date conditions | [CGI 2026, art. 229](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103); [LF 2026, art. 7](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=3) |
| Electric/hybrid motorcycles and battery systems | The specific article 12 DD/VAT exemption begins 1 January 2026; charging/swapping scope and regulatory goods list must be checked. Article 13 preserves separate named levies | [LF 2026, art. 12](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=3); [LF 2026, art. 13](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf#page=4) |
| Registration threshold | Unverified amount: obtain the operative ministerial order; this calculation presupposes confirmed VAT status | [CGI 2026, art. 228](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=103) |

## The base

1. Reconcile every invoice to supply date, nature, place, taxable/exempt/zero-rate category and valid documentary support. Goods place rules are in article 233. Service place rules are in article 234 with the rectifying-law platform addition described below. For ordinary goods, the delivery/fact-generating event determines exigibility; for services, immovable works and the specified public contracts, it is receipt of the price, advances or deposits. Non-import advances make VAT due on that amount even before completion. Article 235 also prevents the fact-generating event falling after a total or partial invoice; resolve unusual timing before calculation. [CGI 2026, art. 233](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=112) [CGI 2026, art. 234](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=112) [CGI 2026, art. 235](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=113) [CGI 2026, art. 236](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=114)
2. The ordinary domestic base is the consideration received or receivable; import bases include the specified customs value and charges and exclude VAT itself. Genuine evidenced price reductions and exact reimbursed disbursements have article 240 conditions. Special margin bases and public-contract rules require separate review. [CGI 2026, art. 237](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=114) [CGI 2026, art. 238](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=115) [CGI 2026, art. 240](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=115) [CGI 2026, art. 242](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=116)
3. Deduct only qualifying business inputs, recorded and used for the business, with the required document: normalised invoice, import declaration and payment proof, self-supply declaration, or withholding receipt. The supplier must be liable for VAT. Check the right's timing; omitted deductions have the article 245 cut-off, and qualifying purchases at or above FCFA 100,000 before VAT require the specified non-cash payment methods. [CGI 2026, art. 243](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=116) [CGI 2026, art. 244](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=116) [CGI 2026, art. 245](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=116)
4. Apply exclusions before a mixed-use apportionment. Passenger/mixed-use vehicles and their services, fuel, lodging/reception and gifts have article 247 restrictions and exceptions. The qualifying industrial/BTP machinery fuel rule excludes tourism/passenger-transport vehicles; for BTP the eligible input deduction is limited to 90% of the VAT on the purchase invoice. Do not treat that as a general 90% rule for all business fuel. [CGI 2026, art. 247](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=117)
5. Directly allocate inputs to taxable and non-deductible activity first. Only common inputs use the article 249 ratio; exclude its specified transactions from the fraction, round the percentage up to the next whole unit, use the provisional prior-year/forecast ratio and regularise with the final ratio by 30 April of the following year. [CGI 2026, art. 248](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=118) [CGI 2026, art. 249](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=118)
6. Reconcile output VAT, eligible input VAT, withholding receipts and prior credit. Excess eligible deductions carry forward; a refund requires a qualifying article 253 case and article 254 documents/time limits, not an assumption that any credit is refundable. [CGI 2026, art. 252](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=120) [CGI 2026, art. 253](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=120) [CGI 2026, art. 254](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=121)

## Deadlines and filing

File the prescribed monthly statement and pay the amount due by the 10th of the following month, showing taxable/non-taxable transactions, gross tax, detailed deductions and tax due or credit. Any VAT stated on an invoice is payable by that fact under article 260, so do not treat a wrong VAT invoice as harmless. [CGI 2026, art. 259](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=123) [CGI 2026, art. 260](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=124)

Prepare a return reconciliation and evidence pack for [DGI e-services](https://e-services.impots.bj/). This draft did not access authenticated return fields, payment references or confirmations. Withheld VAT and imports have separate article 261–263 procedures; where they apply, obtain and reconcile the actual customs/withholding evidence before the authorised filer submits. This is not a customs declaration or completed VAT filing. [CGI 2026, art. 261](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=124) [CGI 2026, art. 262](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=124) [CGI 2026, art. 263](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=124)

## Penalties and interest

General filing/payment sanctions and the conditional 2026 first-declaration relief are recorded once in the [overview](bj-tax-overview.md#penalties-and-interest). Assess the facts before using any relief. This working paper does not prepare a penalty assessment. A late nil/credit VAT declaration specifically incurs FCFA 50,000 per month or part month, capped at FCFA 500,000, under article 496(2). Do not replace that special rule with a percentage of zero tax. [CGI 2026, art. 496](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=220)

## Cross-border points

For a non-domiciled supplier, article 262 requires a Benin representative; in its absence, the recipients/beneficiaries and specified billing/collection persons owe VAT and penalties. This is more conditional than an automatic reverse charge for every imported service. The place of the underlying service must first be established. [CGI 2026, art. 234](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=112) [CGI 2026, art. 262](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=124)

LFR article 14 adds platform place rules: online platform services follow the beneficiary's residence; online sales/service commissions are located in Benin where any specified operator, seller/buyer, provider/user is there at the transaction; property-related services follow the property's location. Article 258 separately charges operators with collecting/remitting the supply VAT and commission VAT and obtaining registration. Verify the exact transaction and avoid charging the same VAT twice through the operator and recipient. [LFR 2026, art. 14](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=4) [CGI 2026, art. 258](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf#page=123)

Platforms handling Benin property rentals also need the distinct rental-withholding assessment under LFR article 13, owned by the [cross-border Guide](bj-cross-border-withholding.md). A VAT result does not settle that withholding. [LFR 2026, art. 13](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf#page=4)

## Two worked examples that recompute

**Ordinary taxable month.** Assume confirmed VAT status, no special base or withholding, FCFA 10 million of ordinary taxable consideration and FCFA 720,000 of fully eligible, evidenced input VAT. Output VAT is 1.8 million and net payable is 1.08 million.

```oa-check
name: Ordinary monthly VAT
inputs:
  taxable_consideration: 10000000
  eligible_input_vat: 720000
steps:
  output_vat: taxable_consideration*0.18
  net_vat: output_vat-eligible_input_vat
expected:
  output_vat: 1800000
  net_vat: 1080000
```

**BTP machinery fuel decision.** Assume the documented purchase qualifies specifically for the article 247 BTP machinery-fuel exception and is not for a passenger/tourism vehicle. VAT on the invoice is FCFA 180,000. The 90% limit allows 162,000; 18,000 is excluded. A full-credit comparison would overstate the deduction by 18,000. If the use/classification is unresolved, hold the deduction instead of using the percentage.

```oa-check
name: BTP qualifying machinery fuel limit
inputs:
  invoice_vat: 180000
steps:
  allowed_input_vat: invoice_vat*0.90
  excluded_input_vat: invoice_vat-allowed_input_vat
  full_credit_overstatement: invoice_vat-allowed_input_vat
expected:
  allowed_input_vat: 162000
  excluded_input_vat: 18000
  full_credit_overstatement: 18000
```

## Ask the client first

- What are the month, VAT status, threshold/option evidence and any status-change facts?
- What goods/services, dates, customers, places and exemption/export evidence are involved?
- Is there a platform, foreign supplier, representative, public contract or VAT withholding?
- Which normalised invoices/import/payment documents and supplier-status evidence support deductions?
- Are inputs excluded, BTP machinery fuel, mixed use, capital disposals or subject to regularisation?
- What prior credits, refund claims, omitted deductions and filed acknowledgements exist?

## Sources

| Official source | What was actually read | Read on |
|---|---|---|
| [DGI official CGI, 2026 edition](https://apisiteweb.impots.bj/media/6adcbd46ab83b_B%C3%A9nin-Code%20G%C3%A9n%C3%A9ral%20des%20Imp%C3%B4ts%202026.pdf) | Articles 223–230, 232–238, 240–249, 252–254, 258–263 and 496(2), including adjacent conditions in the extracted official text. The cover consolidates the original 2026 finance law, not the June rectifying law. | 2026-11-01 |
| [Signed original finance law 2025-22](https://budgetbenin.bj/storage/2025/12/Loi-des-finances-2026.pdf) | Fiscal arts. 1–17, PDF pages 1–5 read; arts. 2–17 visually checked. No claim to have reviewed the budget tables. | 2026-11-01 |
| [Signed law 2026-10 of 24 June 2026](https://apisiteweb.impots.bj/media/6adcb8249c4ab_B%C3%A9nin-Loi%20de%20finances%20rectificative%202026.pdf) | Tax provisions arts. 1–19 and final arts. 48–49, PDF pages 1–6 and 17 visually read; adjacent article 20 heading read. OCR of the whole capture is not a whole-law review. | 2026-11-01 |

Not yet confirmed: operative ministerial order setting the registration threshold and hence the legacy FCFA 50 million claim; product-specific tariff decisions and full medical-products list classification; regulatory implementation of motorcycle/battery relief; special margin/public-contract computations and authenticated platform/representative filing; authenticated DGI portal screens, exact field identifiers and payment-confirmation workflow; later instruments not identified by the sources read; application to a particular taxpayer. Independent pack review is pending; no accountant has attested to this version. The code's stale 2024 footnote is not authority for 2026 relief: the signed original 2026 finance law was read separately.

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
