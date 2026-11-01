---
name: bf-vat
description: >
  Burkina Faso VAT reference for the 2026 tax year, covering ordinary domestic supplies, the reduced hospitality and domestic-air rates, imported services, input-tax allocation, monthly returns and statutory VAT withholding. Use for TVA, eSINTAX preparation, export deduction rights, goods-exporter refund eligibility, mixed taxable and exempt activity, platform sales and the evidence needed to credit withholding. It corrects blanket turnover and exemption assumptions by stating the statutory conditions and linking business-regime thresholds to their existing home. Two executable cases cover the monthly balance and the refund-versus-carry-forward decision. Commodity classification, exemption certificates, refund execution and authenticated portal steps remain expressly limited.
jurisdiction: BF
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.1
---

# Burkina Faso VAT (TVA) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use for ordinary 2026 TVA workpapers. Taxable transactions include goods, work and services under CGI arts. 298–299, including imports, non-resident services/intangibles, certain self-supplies and platform transactions. RNI taxpayers carrying on taxable business are liable by art. 300; the State/public bodies are liable for industrial/commercial activities. Determine the income-tax regime and options through [business income](bf-income-tax.md), rather than copying turnover thresholds here. [CGI arts. 298–300](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

The old absolute prohibition on VAT below RNI is incomplete. Art. 301 permits an irrevocable option for the listed agricultural/fishing operators regardless of turnover and for RNI road carriers' transport activity, effective the first day of the option month. Art. 307(1) expressly reserves arts. 301/530 options when exempting ordinary RSI/CME operations. A non-resident needs an accredited resident representative under art. 302; otherwise the recipient bears the tax and applicable penalties. [CGI arts. 301–302, 307(1), 530](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Rates, bands and thresholds

| Item and conditions | Rate/rule | Official source |
|---|---|---|
| Ordinary taxable operation with no exemption or reduced-rate qualification | 18% | [CGI art. 317](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Accommodation/catering supplied by approved hotels, restaurants and assimilated bodies; also domestic air transport | 10%; approval/supply scope matters | [CGI art. 317](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Fraction of a franc in assessed VAT | Round down to the lower franc | [CGI art. 317](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Exports of goods/services and assimilated operations | Exempt; input deduction only where the operation would be taxable domestically and all deduction conditions are met | [CGI arts. 307(2), 318, 321–322](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| DGE enterprises and qualifying goods exporters buying goods/services; paying bodies on payments to resident public-order contractors | Withhold 30% of the VAT, not 30% of the invoice; provide receipted individual certificate for supplier credit | [CGI art. 334(4), amended by Loi 021-2025/ALT art. 23](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Goods exporter for art. 328 refund category | More than 50% of turnover at export; reimbursement limited by preceding-year export percentage | [CGI art. 328(A)(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Listed export/leasing/extension refund application branch | Refundable credit greater than XOF 1 million; application within thirty days of the monthly declaration, subject also to art. 329's maximum period | [CGI art. 329(1)(a)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

The reduced rate also covers the qualifying hospitality supplies above. It is not restricted to domestic air transport. Do not infer any exemption merely from an industry label or an old list of finance-law additions.

## The base

**Output VAT.** Reconcile each operation's place, nature, taxable consideration, rate and tax point. Goods are located under art. 304, including dispatch and installation rules. Services executed in Burkina Faso, or executed abroad but used/exploited there, are taxable under art. 305; services executed locally but used abroad are treated as service exports. Real-estate, artistic/cultural/sporting and building-work rules have their own location tests. Travel-ticket sales commissions of travel agencies registered in Burkina Faso are deemed received there regardless of destination, transport mode or carrier’s registered office (art. 306). [CGI arts. 303–306](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

Under arts. 310–312, goods/services use the full consideration, construction the billed/contract/advance amount including subcontracted work, imports customs value plus border taxes, and self-supply cost. Include ancillary supplier charges and relevant duties except VAT itself, non-damages indemnities and qualifying price subsidies. Separately charged buyer-borne transport on an ex-works sale is excluded only on the statutory conditions. Ordinary invoiced trade discounts, qualifying deposit packaging, damages, investment grants/financial aid and justified disbursements are excluded under art. 312. Specialist second-hand/travel-agency margin methods require their separate arts. 313–314 analysis; this Guide does not apply those methods. [CGI arts. 310–314](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

Delivery, completed services, imports and self-supply have distinct tax points. Advance invoicing can accelerate the event/liability. Service/construction advances make VAT due on the advance even before completion; IBNC service taxpayers have the specific collection basis. Non-resident service/intangible imports trigger on invoicing or accounting, not a guessed cash date. Public-sector payment deferral requires the tax service's authorisation and visa conditions, not merely a public customer. [CGI arts. 315–316](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**Input VAT.** First exclude prohibited VAT under art. 319. The passenger/mixed-vehicle exclusion covers three to nine seats including the driver, with exceptions for resale as-is, acquisition by professional rental or leasing businesses for rental, public passenger transport, hotel-customer transport and driving instruction. It extends to the vehicles’ parts and accessories. Lodging is excluded except for staff responsible for surveillance or security of industrial units or worksites. Reception, restaurant, entertainment and travel costs are excluded except permanent-contract transport taking staff to work and collective staff needs at the workplace. Decoration is excluded unless it constitutes commercial, industrial or office furniture/equipment. Free or substantially undercost goods/services are excluded, except advertising items with a unit value below XOF 10,000 excluding VAT. Petrol, diesel and biofuel, and services relating to excluded goods, are also excluded. Illegally invoiced VAT is due from the issuer and not deductible by the recipient (art. 320). Then allocate direct taxable/export inputs, direct exempt inputs and common inputs separately (arts. 321–323). Qualifying export means taxable in the domestic regime; exporting an inherently exempt product does not create deduction rights. For common inputs use the statutory taxable/eligible-export turnover ratio, excluding the listed asset disposals, equipment grants, non-consideration insurance, disbursements and damages from its denominator. [CGI arts. 318–323](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

Use the preceding-year/forecast basis specified by art. 324 for provisional allocation; establish the definitive ratio and adjust before 30 April of the following year. Check art. 325 capital-asset adjustments separately when the definitive-ratio variation exceeds its statutory trigger. Input deduction arises when VAT becomes due; import VAT and third-party/reverse-charge/reassessed VAT must actually be paid, partially paid amounts only to that extent. Other input VAT must be separately stated on the invoice. Deduct in the month the right arises; an omitted deduction can be taken no later than 30 April next year. Excess authorised input is carried forward unless a verified refund category is used. [CGI arts. 324–327](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

**Exemptions.** Art. 307 includes qualifying medical treatment/hospital care, State-recognised education, legally constituted nonprofits acting within their objects, the specified social household water/electricity band, and international air transport/aviation operations with their conditions. It also distinguishes locally consumed unprocessed fresh/chilled/frozen food and meat, excluding imported frozen meat from the meat branch. Cement subject to its specific tax is an art. 307(27) exemption; that is not a general deduction-right rule. Art. 308 is a product-code schedule for specified medical/pharmaceutical goods, publications, animals, agricultural and other equipment, solar equipment and other products. Read the exact tariff classification and certificate conditions for the actual item. The schedule includes aviation fuel, specified cattle/sheep/goats, shea seeds, cashew nuts and Gallus domesticus fertilised eggs under their printed codes. Those headings do not exempt every item in those broad categories. The old claims for certified electronic-invoicing systems, an export-cement addition, local-processor conditions for nuts and precise finance-law commencement dates remain held below. [CGI arts. 307–308](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Deadlines and filing

1. Reconcile the month's taxable/exempt/imported/platform transactions, invoices, deduction evidence, opening credit and withholding certificates. Prepare the prescribed monthly TVA declaration, including a nil-operation month. File and pay by the 15th of the next month to the competent tax service. [CGI art. 334(1)–(3)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
2. Auto-liquidate non-resident services/intangibles in the monthly declaration. A non-resident public-order contractor has its distinct payer-withholding rule. Qualifying 30% withholding payers declare each supplier's identity/legal form/activity, IFU and addresses, invoice date/amount, payment date/amount and tax withheld, then remit by the same monthly deadline. Give the supplier an individual certificate annotated by the receiver with payment-receipt references. Supplier credit requires that evidence; do not deduct a customer's unremitted promise. [CGI art. 334(2)–(4)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
3. Platform operators must register and collect/declare/remit VAT on covered supplier sales and separately their own commissions under art. 334(5). The code permits online registration/declaration/payment and provides an access-suspension sanction. Current implementing-order procedure, exact eSINTAX forms/boxes, credentials, upload order and acknowledgement/payment-reference screens were not verified. This is preparation, not a tested live submission. [CGI art. 334(5)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
4. For a possible refund, first select an art. 328 category: eligible goods exporters, exclusively exporting service businesses with domestically taxable equivalents, approved investment-code extensions, loss of VAT status, leasing, specified ministerial nonprofit derogation or the specified mining category. Do not treat every carry-forward credit as cash refundable. Art. 329 imposes category-specific application windows and an overall six-month maximum from the stated refundable date; its text cancels a credit not requested within that maximum. Resolve that timing for the actual category before allowing a credit to age. A credit claimed for refund cannot also be carried forward unless the refund is rejected. [CGI arts. 328–329](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).
5. Refunds require the art. 330 three-column purchase schedule (supplier identity/address/IFU/regime; invoice dates/amounts; VAT) and category-specific invoices, import declarations/receipts and payment evidence. Exporters additionally need the relevant export/transport/customs evidence, buyer details and withholding receipt/detailed supplier schedule. Do not submit an ordinary VAT return as a complete refund dossier. Art. 331 provides a justified-claim tax-release certificate within two months and reimbursement within thirty days of that certificate; implementation and current claim forms remain unverified. [CGI arts. 330–331](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

Credit notes/cancelled or unpaid supplies require prior invoice correction before output adjustment; associated deducted input must be reversed. Cessation, destruction, separate under-value/free disposal, lost VAT status or reassignment to non-deductible use also require the art. 332 stock/capital-asset regularisation. Check that job before finalising the monthly balance. [CGI arts. 332–333](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Penalties and interest

| Failure and factual branch | Consequence | Official source |
|---|---|---|
| Missing invoice, separately stated VAT or irregular invoice wording | 100% of VAT due; illegal VAT invoicing 200% of wrongly invoiced amount; knowing wrongful recipient deduction can create joint liability | [CGI art. 776](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Late/missing monthly declaration | 25% plus 1% per month or fraction, minimum XOF 50,000 | [CGI art. 777(1)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Assessment on failure to declare | 50% plus 1% per month or fraction, minimum XOF 500,000 | [CGI art. 777(2)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Incomplete/inaccurate base | 50% good faith, 100% established bad faith, 200% fraud | [CGI art. 777(3)](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |
| Late/insufficient payment | 10%; if delay exceeds fifteen days, add 1% per month or fraction | [CGI art. 778](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) |

Keep declaration and payment failures distinct. Sanction cumulation and public-contract visa penalties need their own facts; no additive total is inferred here.

## Cross-border points

Use the location/import and reverse-charge rules above, not the supplier's foreign address alone. Exports retain deduction only on the domestic-taxability condition. Treaty income-tax relief does not establish VAT relief. The separate [non-resident services withholding](bf-nonresident-services-withholding.md) job is not a substitute for VAT auto-liquidation. [CGI arts. 299, 302–305, 318 and 334](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf).

## Two worked examples that recompute

**Monthly balance with certified withholding.** A fully taxable ordinary supplier invoices XOF 10 million excluding VAT to a DGE customer. Output VAT is XOF 1.8 million; the customer withholds XOF 540,000, so the supplier receives XOF 11.26 million. On valid input VAT XOF 450,000, no opening credit, and a receiver-annotated paid withholding certificate for the same period, the supplier's remaining VAT payment is XOF 810,000. The withheld amount does not change the output rate or input base.

```oa-check
name: Ordinary monthly VAT and certified withholding
inputs:
  sales: 10000000
  input_vat: 450000
steps:
  output_vat: floor(sales * 0.18)
  withheld_vat: output_vat * 0.30
  supplier_cash: sales + output_vat - withheld_vat
  balance: output_vat - input_vat - withheld_vat
expected:
  output_vat: 1800000
  withheld_vat: 540000
  supplier_cash: 11260000
  balance: 810000
```

**Decision: refundable exporter or carry-forward?** Assume a goods seller has XOF 2 million authorised credit, no other refund category, otherwise satisfies the claim dossier/timing rules, and the current and preceding-year export percentages match. At exactly 50% goods-export turnover it fails the “more than 50%” category and carries the XOF 2 million credit forward. At 60% it meets that category; the percentage limit gives XOF 1.2 million for refund, with XOF 800,000 outside that claimed amount. The credit claimed for refund cannot simultaneously be carried forward. This is an eligibility comparison, not an option to change the actual export percentage.

```oa-check
name: Goods-export refund boundary
inputs:
  credit: 2000000
  exact_threshold: 0.50
  qualifying_export_share: 0.60
steps:
  exact_threshold_refund: 0
  exact_threshold_carry: credit
  qualifying_refund: credit * qualifying_export_share
  unclaimed_remainder: credit - qualifying_refund
expected:
  exact_threshold_refund: 0
  exact_threshold_carry: 2000000
  qualifying_refund: 1200000
  unclaimed_remainder: 800000
```

## Ask the client first

- Which regime/options and approvals apply to the taxpayer and each supply?
- Where are goods delivered/installed and services performed and used?
- What are invoices, advances, actual payments and imported-service dates?
- Which inputs serve taxable, exempt or mixed activities, and which VAT is actually paid?
- Are withholding certificates receiver-annotated and supported by remittance receipts?
- For a refund, which category, current/prior export percentages, credit origin and dossier dates apply?

## Sources

| Source | Actual reading scope | Read on |
|---|---|---|
| [DGI official CGI 2026](https://dgi.bf/wp-content/uploads/2026/10/CGI-2026-v2.pdf) | Arts. 298–306, 310–334, 776–778; art.307 exemption branches noted above and selected art.308 product headings/neighbouring descriptions. Not every product-code row or implementing order was read; no authenticated eSINTAX session. | 2026-11-01 |

Not yet confirmed: current forms/boxes, platform implementing order, eSINTAX acknowledgements and payment references; full commodity classification/certificate execution; old claims for certified e-invoicing-system exemption, export-cement addition, local-processor conditions for shea/cashew and exact historical commencement dates; detailed capital-asset adjustment execution, refund-window interaction/category-specific filing and sanction cumulation. Independent conditional source review of this rewrite is accepted; no accountant has attested to it.

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
