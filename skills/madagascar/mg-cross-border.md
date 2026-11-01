---
name: mg-cross-border
description: "Madagascar 2026 domestic non-resident service withholding, royalty boundary, residence and PE screening; treaty and capital-income rates remain expressly partial."
jurisdiction: MG
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 1.0
---

# Madagascar cross-border: non-resident services and PE triage

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Use before paying a foreign service provider or deciding whether a foreign enterprise has a taxable presence. Obtain residence, beneficial recipient, activity location and actual-use facts. Resident companies are within IR on income regardless of origin; non-residents are within scope on Malagasy-source income, subject to treaties (01.01.04–05). A foreign incorporation address alone does not settle residence: seat and/or effective management in Madagascar are relevant. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Rates, bands and thresholds

| Domestic rule and conditions | 2026 rate / time test | Official source |
|---|---|---|
| Service remuneration to non-resident without a fixed business installation in Madagascar, or with an installation not constituting a PE, materially supplied or effectively used in Madagascar; treaty reserved and public-contract exception | 10% of sums paid | [CDI 01.01.14 II-A](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Royalties of any nature paid by a resident to a non-resident; treaty reserved | 10% | [CDI 01.01.14 II-C](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Construction, assembly or installation project and linked supervision | PE when duration exceeds 120 days | [CDI 01.01.02 g)](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Services including consultancy through staff/engaged personnel, same or connected project | PE when aggregate exceeds 90 days in a one-year period beginning or ending in relevant tax year | [CDI 01.01.02 h)](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |

These duration tests do not replace the general fixed-place PE rule. A management place, branch, office, factory, workshop or extraction site can qualify. The article also excludes the listed storage, display, processing-by-another, purchase/information and preparatory/auxiliary operations subject to its conditions.

## The base

First classify service, royalty, capital income, employment or public-contract income. For a service under 01.01.14 II-A, use the amount paid to the foreign provider; check whether a gross-up clause changes contractual consideration. Test treaty entitlement and the actual applicable article before reducing domestic withholding. The accredited representative withholds/remits; absent one, the party receiving the materially performed service must withhold and remit. For royalties, the resident legal-person payer remits under II-C. A PE case needs profit attribution under ordinary IR and [TP](mg-transfer-pricing.md), rather than mechanically applying final gross service withholding. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Deadlines and filing

For II-A service withholding, the representative or substituted recipient remits to the competent Receveur des Impôts **before** the 15th of the month after withholding. For II-C royalties the stated deadline is **by** the 15th of the month after payment. Keep the contract, invoice, service/use evidence, residence/treaty evidence, gross amount, withholding computation, representative accreditation and remittance receipt. Obtain the current prescribed intermittent declaration and payment reference from the managing fiscal unit before submission; its boxes and portal steps have not been confirmed. [CDI 01.01.14 II](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Penalties and interest

CDI 20.01.54.1 has specific intermittent withholding sanctions: an omitted service withholding/remittance attracts 10% of rights due, at least MGA 20,000; for persons themselves subject to IR the text limits that sanction to minimum-tax or exempt cases. Collected intermittent tax not paid over attracts 40%, at least MGA 100,000. Preserve those conditions and distinguish omission from collection without remittance. Late payment and representative-specific consequences require 20.01.53 and 53.3; do not apply a salary-penalty percentage to foreign services. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Cross-border points

Imported-service TVA is separate and belongs to [TVA](mg-vat-gst.md). Foreign salary pay belongs to [IRSA](mg-income-tax.md). The LFI text contains non-resident-dividend language under 01.01.14 II-B; the July LFR repeals II-B and amends 01.04.02 6° to cover dividends and securities-disposal gains of resident/non-resident natural and legal persons. Do not use the repealed separate IR provision for a payment after the LFR takes effect. The LFR also adds 10% under II-D for interest received by non-resident banks/credit establishments on lending operations, excluding 01.01.03 8° interest. This Guide does not compute those capital-income cases or pre/post-transition payments. Treaty rates, treaty-entry dates, foreign-tax-credit mechanics and exit/capital-disposal rules require separate source verification.

## Two worked examples that recompute

Assume a non-treaty foreign provider has no Madagascar PE, the service is effectively used in Madagascar, and the ordinary II-A rule applies rather than a public-contract regime. VAT is excluded from both cases.

```oa-check
name: Gross invoice withholding
inputs:
  gross_fee: 10000000
steps:
  - withholding: gross_fee * 0.10
  - paid_to_supplier: gross_fee - withholding
expected:
  withholding: 1000000
  paid_to_supplier: 9000000
```

Second, a hypothetical contract requires the supplier to receive a fixed net amount and the payer bears the withholding. Gross up the contractual consideration; this assumption must come from the signed contract.

```oa-check
name: Net contract gross up
inputs:
  net_fee: 9000000
steps:
  - gross_fee: net_fee / (1 - 0.10)
  - withholding: gross_fee * 0.10
  - net_check: gross_fee - withholding
expected:
  gross_fee: 10000000
  withholding: 1000000
  net_check: 9000000
```

## Ask the client first

Get payer/provider legal forms, tax residences, treaty evidence, contract and gross/net clause, service delivery/use locations, site and personnel day counts by connected project, fixed facilities and decision authority, representative status, related parties, public-contract status and payment date. Ask whether any amount is interest, dividend, royalty or salary.

## Sources

| Source and provisions actually read | Read on |
|---|---|
| [DGI 2026 CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), 01.01.02,04–05,14 II; 01.04.02–04; 20.01.53,53.3,54.1 | 2026-11-01 |
| [Signed Loi 2026-004, LFR 2026](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), tax amendments and article 22 entry provision read | 2026-11-01 |

**Not yet confirmed:** Exact radio/posted publication date activating the July LFR under article 22; do not resolve a transaction at that transition without the publication evidence. operative treaty network/rates and relief procedure, historical dividend IR/IRCM interaction before LFR entry and current capital-income payment procedure, loan-interest exemptions and payment procedure, treaty PE overrides, foreign tax credits, exit and property/share-disposal regimes, current intermittent filing form/portal. Old headline dividend/interest figures are not an executable withholding table.
