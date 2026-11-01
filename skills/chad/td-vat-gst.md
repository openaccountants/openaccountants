---
name: td-vat-gst
description: "Prepare Chad VAT working papers for 2026, distinguishing the principal rate from provincial and communal additional centimes, classifying ordinary and reduced supplies, and testing input support. Covers place of supply, tax points, taxable-base rounding, domestic invoices, imports, foreign services, buyer self-liquidation, mixed-activity deduction, monthly preparation and credit/refund conditions. Use for Chad TVA, hotel VAT, import VAT, electronic normalised invoices, VAT credit or non-established supplier intake. Two cases recompute output principal and centimes without assuming input-credit mechanics. Lower-regime contradictions, commodity overlaps, cement rates and current platform and filing screens remain explicit gaps, so the VAT domain remains partial."
jurisdiction: TD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.1
---

# Chad value added tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Businesses carrying out taxable economic activities in Chad, including taxable supplies, imports, self-supplies and used-in-Chad foreign services. Establish article 230 exemption status and article 229 regime before charging tax. This 2026 working paper computes ordinary domestic VAT principal, additional centimes, supported inputs and the payment balance. Nonresident platform implementation, commodity/exemption conflicts and live filing screens remain open. [CGI arts 226–234](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF arts 29–31](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=34).

Article 229, as replaced in 2026, sets real normal at annual turnover excluding tax of at least 500million; RSI includes 100million to below500million and, in paragraphIV, 50million to below100million. ParagraphII's100million VAT threshold and paragraphsIII–IV's RSI authorisation need reconciliation for the lower band. IGL natural persons are below50million; this is not a settled universal VAT-registration threshold for every company. Hold an unresolved boundary case for written regime confirmation. [LF art30](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=38).

## Rates, bands and thresholds

Tax year:2026; amounts in XAF/FCFA. Determine exemption, then the principal rate, then centimes. A zero rate and an exemption are distinct classifications.

| Transaction/condition | Rate or amount | Official source |
|---|---|---|
| Ordinary taxable operation outside reduced/zero classes | Principal17.5% | [CGI238, LF32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=49) |
| Specified production/sale list including sugar, oil, soap, textiles and reinforcing iron; local agro-industry products/by-products excluding alcohol and craft/fishing materials | Principal9%, subject to exact transaction/classification | [CGI238, LF32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=49) |
| Lodging/restoration services of hotels, restaurants and lodging establishments | Principal9% | [CGI238, LF32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=49) |
| Exports, air transport, outward aircraft jetA1 supply and aircraft maintenance/repair | Principal0% within statutory category | [CGI238, LF32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=49) |
| Centimes additionnels on VAT | 10% of VAT principal, not10points of taxable base | [LF73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=81) |
| Ordinary taxable base combining17.5% principal and10% centimes on principal | Effective19.25% | [CGI238 plus LF73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=81) |
| Reduced9% principal plus centimes | Effective9.9% | [CGI238 plus LF73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=81) |
| Taxable base rounding | Round down to nearest1,000 | [CGI237](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| Cash-paid invoice input restriction | Invoice excluding tax at least500,000 | [CGI241(6)](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |

New article238 also names milk, yoghurt, butter, cheese and meat in the9% list, while new230(15) retains overlapping exempt commodity wording. Hold these transactions until import/sale/production and tariff classification resolve the overlap. Cement has a specific reduced rate linked to Community texts, but no number in article238: do not assign9% by analogy. [LF arts31–32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=44).

## The base

1. Map goods, services, imports, self-supplies and any exemption to the actual contract. Goods delivered in Chad and services, rights or leased objects used/exploited there meet article231's territorial rules. A non-established supplier needs a solvent accredited resident representative; failing that, the customer pays on its behalf under article232. Separate that route from new229(V)'s buyer self-liquidation. [CGI arts226–232](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
2. Determine tax point: goods generally on delivery, imports on customs declaration, services on collected price/advances. Public-sector dealings use collection rules. Authorised debit accounting does not postpone VAT on an advance received first and excludes public-sector business. [CGI arts233–234](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
3. Build gross consideration including accessory charges and applicable non-VAT taxes; remove supported true disbursements and commercial discounts. Import base is customs value plus customs duty and excise, excluding VAT and article120 prepayment. Round the taxable base down to1,000; do not apply that rounding rule to the VAT amount. [CGI arts235–237](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
4. Apply the principal rate, calculate centimes at10% of principal and retain the two separately. The19.25%/9.9% figures are derived arithmetic, not replacement principal rates. [CGI238, LF32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=49); [LF73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=81).
5. For new229(V), test supplier status and transaction: supplier outside IGL, or IGL supplier whose operation crosses50million, supplies goods/services to a VAT-assujetti and invoice omits VAT. The assujetti self-liquidates, collects and remits under source-withheld VAT rules, with deduction only under ordinary conditions. Do not turn this into a blanket tax on every small supplier or skip the actual predicate. [LF30, new229(V)](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=39).
6. Build an invoice-level input register. Article239 requires business necessity and supporting domestic/import/self-supply documents. Domestic input follows its taxable-operation month; foreign services have the following-month rule and special third-party VAT slip. Exercise deduction by the end of the second following fiscal year. [CGI239](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
7. Test article241–242 exclusions before deduction: private consumption, relevant lodging/entertainment/transport, gifts, specified fuel, passenger/mixed vehicles and costs, subject to the actual statutory business-transport/staff-bus exceptions. Cash-paid invoices at or above the table threshold are excluded. An expense being deductible for IS does not establish input-VAT recovery. [CGI241–242](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
8. New246 requires an electronic normalised invoice with both NIFs, precise quantity/description/unit price excluding tax, date, number, VAT rate/amount, totals excluding/including tax. Foreign-supplier invoices have the stated exceptions. A known taxpayer's good-faith missing NIF has a5% invoice penalty exception; an unknown/unlisted supplier is not cured by it. Do not certify a document from its appearance alone. [LF33](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=50).
9. For mixed activities use article243: taxable receipts plus exports over total receipts excluding tax, with statutory exclusions (self-supplies, specified equipment grants, asset disposals, non-consideration damages and disbursements). Calculate actual monthly proportions, round to nearest1% and report the calculation. Approved separate sectors need their own conditions. A capital-asset change before the end of the fourth following year triggers article244's repayment reduced by one fifth per elapsed year or part; noncapital reuse in nontaxable activity calls for full repayment. [CGI243–244](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).
10. Reconcile output principal, centimes, supported input lines, credits and prior payments in their distinct declaration fields. Do not infer unacquired input-centimes/refund screen mechanics from the effective rate. The cases below use no input credit, so no unsupported centimes-offset assumption is hidden in them.

## Deadlines and filing

Specific article229(III), expressly reproduced in LF30, requires monthly declarations for both real and RSI; articles886–887 require a nil declaration marked “Néant” when applicable and declaration/payment within the first15days of the next month. Article38(V)'s quarterly RSI wording conflicts. Use the express monthly instruction for preparation and obtain DGI resolution before relying on quarterly filing. [LF30](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=39); [CGI38, 886–887](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef).

Prepare period sales, output rate/classes, additional levy, self-liquidation, invoice-by-invoice eligible inputs, prorata and credit movements. File through e-Tax under new996, reconcile its assessment and save declaration/receipt and payment evidence. Current production portal address, form boxes, normalised-invoice implementation channel and payment-reference screens have not been acquired; no filing-ready claim is made. [LF37](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=56).

New891 carries credits for up to24months. Traders' quarterly credits above5million require validation; refund-claimed credits cannot also offset the following return. Good standing and normalised invoices/import papers, non-redevance evidence and electronic supplier-payment evidence are among the revised conditions; taxpayers with qualifying established-exemption conventions are excluded under its stated rule. Do not promise a cash refund from a credit balance alone. [LF35](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=54).

## Penalties and interest

Article1068 specifies300,000 for missing/late returns or bad-faith nil returns,5% per month or part for late payment capped at50% and cumulative with the return fine, and100,000 for missing prorata support. Invoice, withholding and fraud offences have separate rules, including article1069. LF73 also applies centimes to the principal and relevant increases. Classify the breach before computing a notice; these are not all-purpose cumulative additions. [CGI1068–1069](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=81).

## Cross-border points

Article231's place-of-use test and232's representative/customer collection rules apply separately from customs import valuation and from article227's electronic-commerce/platform obligations amended by LF29. Retain foreign contracts, customs clearance and payment evidence; distinguish exemption from zero rate and the input consequences. The [import-eligibility Guide](td-import-exemption-eligibility.md) owns the accepted narrow September order, including its wheat hold; it is not a domestic VAT exemption decision. Do not convert air transport's0% wording into a universal exemption for all international transport. [CGI231–239](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF29,32](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf#page=34).

## Two worked examples that recompute

### Ordinary invoice with centimes

Taxable selling consideration is1,234,567 before tax, with no credit/withholding complication. Round the base down to1,234,000. Principal is215,950 and centimes21,595; total output tax237,545. The1,472,112 gross commercial amount below adds that tax to the original consideration; it does not silently round the actual selling price.

```oa-check
name: Standard output VAT and additional centimes
inputs:
  consideration: 1234567
steps:
  base: floor(consideration / 1000) * 1000
  principal: base * 0.175
  centimes: principal * 0.10
  output_tax: principal + centimes
  commercial_total: consideration + output_tax
expected:
  base: 1234000
  principal: 215950
  centimes: 21595
  output_tax: 237545
  commercial_total: 1472112
```

### Determine the actual supply before selecting a rate

A qualifying hotel lodging/restoration service has taxable base2,000,000. Its9% principal is180,000 and centimes18,000, total198,000. An unrelated ordinary taxable service on the same base gives385,000. The187,000 difference demonstrates why the contract and service classification must precede rate selection; the taxpayer cannot elect hotel treatment for an unrelated service. No input claim is assumed.

```oa-check
name: Qualifying hotel versus ordinary service classification
inputs:
  base: 2000000
steps:
  reduced_principal: base * 0.09
  reduced_centimes: reduced_principal * 0.10
  reduced_output: reduced_principal + reduced_centimes
  ordinary_principal: base * 0.175
  ordinary_centimes: ordinary_principal * 0.10
  ordinary_output: ordinary_principal + ordinary_centimes
  difference: ordinary_output - reduced_output
expected:
  reduced_output: 198000
  ordinary_output: 385000
  difference: 187000
```

## Ask the client first

- What DGI regime, turnover, NIF and VAT entitlement establish the taxpayer's status?
- What goods/services, tariff classes, customers, place of delivery/use and exemptions are involved?
- What delivery, invoicing, advances, collection and customs dates determine the period?
- Which normalised invoices, payment modes, foreign-service slips and imports support inputs?
- What mixed activities, asset changes, carried credits, refund claims and DGI confirmations exist?

## Sources

| Primary source | Read on | Actual reading |
|---|---|---|
| [Archived official CGI2025 ministry publication, capture2025-07-20](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) | 2026-11-01 | Source researcher read arts38,226–246,886–891,1068–1069 and neighbours, recorded as V01–V17; current LF overlay applied; not whole-code review |
| [Enacted LF2026](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) | 2026-11-01 | Arts29–35,37,73: platform, regime, exemption, rate, invoice, credit and centimes changes; scanned49 and81 visually checked; new text distinguished from old |

Not yet confirmed: lower RSI50–100million entitlement and quarterly/monthly conflict; cement implementing rate; overlapping milk/meat exemption and reduced-rate cases; complete electronic-platform/nonresident procedure; foreign/input-centimes allocation and current e-Tax boxes, payment and normalised-invoice workflow; complete commodity tariff table, banking/financial/medical/educational exemption classification and special refund paths. These keep VAT partial. For independent AI source review and its limits, see the [country README](README.md). No accountant attestation.

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
