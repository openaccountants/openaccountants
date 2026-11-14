---
name: nf-gst
description: >
  Classify Norfolk Island transactions under Australian GST territorial,
  registration, export and input-credit rules for 2026. Use for Norfolk
  GST, mainland sales, voluntary registration, goods exported to the island,
  tax invoices, mixed business use and credit timing questions. Covers
  indirect tax zone definitions, current and projected turnover, exact
  threshold boundaries, supplier and recipient export conditions, and
  fictional standard-rate computations. Includes primary legislation and
  regulations. This source-cited reference requires the universal and VAT
  workflow bases and holds special schemes, actual return preparation and
  missing legal or transaction conditions; it is not a complete country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "GST Act compilation 96 from 1 January 2026; regulations compilation 5 from 1 November 2025; checked 17 October 2026"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - vat-workflow-base
  - nf-tax-system
---

# Norfolk Island: GST territorial and mainland transaction rules

Load `workflow-base`, `vat-workflow-base` and `nf-tax-system`. Preserve
their source/period gates, profile confirmation, refusals, all universal
and VAT-domain outputs and checks. This reference covers selected ordinary
transactions. It does not fill every country slot, special regime or
mandatory operational output. A missing required source, fact or slot
prevents a deliverable financial result.

## Establish the territory and connection for each supply

GST Act section 195-1 excludes the external Territories from the **indirect
tax zone**, with its separate offshore-installation qualification. The ATO
confirms that the former Norfolk Island GST ceased on **1 July 2016** and
that Australian GST does not apply to Norfolk island transactions. Use
that summary with the statutory connection and exemption tests below.
Norfolk residence alone does not decide mainland dealings. [ACT2, section
195-1][ACT2]; [ATO]

A taxable supply generally requires consideration, an enterprise,
connection with the indirect tax zone, and registration or a requirement
to register. It remains outside taxable-supply treatment to the extent it
is GST-free or input taxed. Determine all conditions and any special rule.
[ACT1, sections 9-5 and 9-20][ACT1]

Section 9-25 distinguishes:

- Goods delivered or made available in the zone, goods removed from it,
  goods imported by the supplier, and offshore low-value goods rules.
- Real property by the location of the property or underlying land.
- Other things, including where the thing is done, the supplier's enterprise
  connection, specified rights/options and Australian-consumer supplies.

For section 9-25(7), the Australian-consumer test excludes an entity whose
Australian residence arises solely because the income-tax definition
includes external Territories. It also tests registration and enterprise
purpose. An Australian postal address, citizenship or Norfolk customer
label alone cannot replace those tests. Sections 9-26–9-27 and special
rules can affect connection; actual digital/low-value imports, agents,
reverse charges and mixed supplies require further analysis. [ACT1]

Goods sold and delivered wholly on Norfolk, without a statutory zone
connection, do not become taxable merely because the seller registers
for GST. Conversely, goods supplied from the mainland to Norfolk can be
connected supplies requiring an export exemption. Separate the supplier's
sale from any importation and identify the actual importer. No customs,
excise or biosecurity exemption is established by this guide. [ACT1,
sections 9-25 and 38-185][ACT1]; [ATO]

## Registration and turnover boundaries

For the ordinary section 23-5 test, an entity carrying on an enterprise
must register when GST turnover **meets** the registration threshold.
The regulations specify **AUD 75,000**, or **AUD 150,000 for a non-profit
body**, replacing the lower fallback figures printed in section 23-15.
Exactly the applicable threshold qualifies. Establish non-profit status
and any special registration rule separately. [ACT1, sections 23-5–23-15][ACT1];
[REG, sections 23-15.01–23-15.02][REG]

Section 188-10 meets the threshold when projected turnover is at or above
it, or current turnover is at or above it and the Commissioner is not
satisfied that projected turnover is below it. The windows differ:

| Measure | Statutory window and important adjustments |
|---|---|
| Current GST turnover | The 12 months ending at the end of the current month. |
| Projected GST turnover | The current month and the next 11 months. |
| Both | Exclude the specified input-taxed, non-consideration and non-enterprise supplies; disregard supplies not connected with the zone and the other statutory exclusions. Apply group and special rules where relevant. |
| Projected only | Section 188-25 excludes specified transfers of capital assets and supplies solely consequent on ceasing or substantially/permanently reducing the enterprise. This is not a general exclusion from current turnover. |

[ACT2, sections 188-10–188-25][ACT2]

Thus island receipts are excluded **because the supplies lack the relevant
connection**, rather than through a universal deduction for any receipt
labelled Norfolk. A GST-free export can remain connected and count toward
turnover; GST-free and outside-scope are different classifications.
Check the specific non-resident and other statutory exclusions before
including a GST-free supply. [ACT1, section 9-25(2)][ACT1]; [ACT2]

An eligible enterprise may register voluntarily under section 23-10.
Registration does not establish that every purchase is creditable or that
every sale is taxable. An unregistered entity required to register must
apply in the approved form within **21 days** of becoming required.
The Commissioner's registration decision sets its effective date and tax
periods. [ACT1, sections 23-10 and 25-1–25-10][ACT1]

Backdating under section 25-10 is generally limited to **four years before
the decision**, with the stated fraud/evasion exception. Section 25-15
brings relevant supplies, acquisitions and importations from the effective
date into the GST system. Do not claim backdated credits while omitting
taxable sales for that period. Actual registration, cancellation, ABN and
return arrangements require their own checks; use reviewer-held identifier
readiness and never submit TFNs or bank details through this workflow.
[ACT1]; [ATO]

## Mainland goods exported to Norfolk

Section 38-185(1) item 1 generally requires the **supplier to export** the
goods before or within **60 days** after receiving any consideration, or
an earlier invoice, subject to a further period allowed by the Commissioner.
Item 2 instead uses the final-instalment payment or earlier final-instalment
invoice for a qualifying instalment contract requiring export. Do not use
that later event for every part-payment arrangement. [ACT1]

Identify who exports under the actual contract, transport arrangements and
documents. A Norfolk destination or the buyer's plan to carry the goods
there does not itself establish that the supplier exports them. The Act
also contains a **deemed supplier-export** route in subsection (3), requiring:

- Supply before export to an entity that is neither registered nor required
  to register, and export by that entity.
- The specified export entry under Customs Act section 113.
- No use or alteration after supply beyond what is necessary for export.
- Sufficient supplier-held documentary evidence of export.
- Where the recipient is the specified external-Territory individual, the
  required declaration that the relevant tourist refund payments have not
  been sought, including the wine provision where applicable.

All conditions and timing must be established. A voluntarily GST-registered
Norfolk buyer cannot automatically use the subsection (3) route that
requires an unregistered recipient. Actual supplier export under item 1
is a separate route and is not conditioned on the same recipient status.
[ACT1, section 38-185(1) and (3)][ACT1]

Reimportation rules also differ: subsection (2) removes GST-free treatment
under items 1–6 when the supplier reimports, while subsection (3)'s final
sentence retains its stated taxable-reimportation qualification. Preserve
the actual route. Associate supplies, ships/aircraft, recreational boats,
stores, accompanied baggage, tourist refunds and the exact customs-entry
application need their own rules. No refund or automatic extension is
selected here. [ACT1, section 38-185][ACT1]

Services and rights need their own section 38-190 analysis. That provision
contains property, recipient, effective-use/enjoyment and other conditions,
plus limitations for rights/options, specified residential property and
supplies provided to another entity. Goods export rules cannot establish
a services exemption. Hold actual service/transport/rights treatment
where those conditions or supporting instruments are unresolved. [ACT1]

## Tax amount, purchase credits and timing

For a wholly standard-rated taxable supply, GST is **10% of value**.
Section 9-75 generally values a money price at **10/11 of the GST-inclusive
price**, so the GST component is **1/11 of that price**. Use the mixed-supply
rules and other special valuation rules where applicable. [ACT1, sections
9-70–9-80][ACT1]

A creditable acquisition needs all section 11-5 conditions: creditable
purpose, a taxable supply to the purchaser, consideration and registration
or a requirement to register. Under section 11-15, private/domestic use
and input-taxed connections generally restrict creditable purpose, subject
to its express exceptions, including the outside-zone enterprise branch.
Registration, a business label or GST printed on an invoice alone does
not settle every condition. Disputed/excess GST requires separate analysis;
this guide decides no such refund or credit. [ACT1, sections 11-5–11-30][ACT1]

For an otherwise ordinary partly creditable acquisition, section 11-30
applies the full input credit, extent of creditable purpose and extent of
consideration separately. Reconcile any adjustments and special credit
rules before calculating a return's net amount. [ACT1]

Sections 29-5 and 29-10 distinguish ordinary invoice/payment attribution
from an established cash basis. A required tax invoice can postpone credit
attribution until the relevant return is given while it is held, subject
to statutory exceptions. Section 29-80 and regulation 29-80.01 provide the
specified low-value exception where supply **value does not exceed AUD
75**. For a wholly standard-rated money supply, that is a price of
**AUD 82.50 including GST**. The exception does not itself establish an
entitlement to credit. [ACT1]; [REG]

Section 93-5 generally ends credit entitlement to the extent it has not
been taken into account in an assessment within **four years after the
required return date** for the tax period identified by section 29-10(1)
or (2). Read sections 93-10 and 93-15 and any other applicable rules.
This is not simply a purchase-date anniversary or the separate registration
backdating clock. Establish actual attribution, return due dates, documents
and assessment history. This guide assigns no live BAS period, extension,
filing/payment deadline or accounting-method election. [ACT1, Division 93][ACT1]

## Fictional computations and classification cases

Amounts are AUD and do not establish an actual business's eligibility.
The computation cases stipulate valid registration, ordinary single-rate
supplies, credit entitlement and attribution, with no adjustments or
special scheme unless the row says otherwise.

| Stipulated facts | Result |
|---|---|
| Only 1,000,000 of local Norfolk goods sales, all lacking zone connection, and no other relevant supplies or special registration rule | Those supplies are disregarded for current/projected turnover. Their gross receipts alone do not meet the ordinary registration test. |
| An ordinary enterprise has projected relevant turnover of exactly 75,000 | It meets the ordinary threshold. The word “over” in one older ATO summary does not create a strict greater-than boundary. |
| A qualifying non-profit body's projected relevant turnover is exactly 150,000 | It meets that threshold; non-profit status is stipulated, not inferred from its name. |
| A capital asset is sold, with projected turnover otherwise below threshold | Apply section 188-25 to projected turnover and separately test current turnover and section 188-10; do not automatically remove the sale from both windows. |
| Taxable mainland sale value 1,000 | GST 100; total price 1,100. A local Norfolk delivery would require a different connection classification. |
| Wholly creditable purchase price 550 including standard-rate GST | GST component and full credit are 50. |
| Same purchase, 80% creditable purpose, all consideration provided | Credit 40. If the purchaser provides only half the consideration and the ordinary partly-creditable rule applies, credit is 20. |
| Output GST 100 and established input credit 40 in the same period, with no adjustments | Net amount 60. This is an example, not a completed BAS. |
| Invoice at relative day 0, part-payment at day 10, item 1 export only after day 60 | Establish an allowed extension or another applicable route; the later part-payment does not restart the ordinary clock. |
| Recipient carries goods away but is registered for GST | Do not assume subsection 38-185(3) deems supplier export. Examine the actual supplier/export route and all conditions. |
| Purchase invoice is missing and only its gross price is known | Hold entitlement/attribution pending the required facts, invoice or established exception; do not infer a credit solely from a division by 11. |

Check connection, enterprise, registration status/effective date, both
turnover windows, exemptions, importer/exporter, evidence, value versus
price, credit purpose/consideration, attribution and actual return period.
Keep missing required facts as Needs Input and unresolved law on hold.

## Primary sources and limits

Checked on 17 October 2026: selected GST Act provisions in compilation 96,
effective **1 January 2026**, registered **30 January 2026**, and GST
regulations compilation 5, effective/registered **1 November 2025**. The
live Register identified each as latest. Read sections 9-5, 9-20, 9-25,
9-70–9-80, 11-5–11-30, 17-5–17-10, 23-5–23-20, 25-1–25-15, 29-5–29-10, 29-70–29-80,
38-185–38-190, 93-5–93-15, 188-10–188-25 and the indirect-tax-zone
definition, with the specific cited regulation provisions. Native HTML
formula alternative text supplied the formulas omitted by plain extraction.
Other contextual provisions and special rules have not been comprehensively
verified. The ATO Norfolk page carries a **15 September 2022** update date;
the operative threshold boundary is checked against the Act and regulations.

Full import/customs treatment, all exemptions, financial supplies, property,
digital/low-value goods, reverse charges, groups/agents, cancellation,
special accounting, adjustments, excess-GST refunds, actual returns and
operational output testing remain open. GSTR 2002/6 was acquired as a
guidance lead, but its authorised consolidated PDF has not been verified
in this batch; no administrative extension is selected from that HTML.
This Tier 2 reference confers no accountant sign-off or comprehensive
Norfolk pack acceptance.

[ACT1]: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html
[ACT2]: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html
[REG]: https://www.legislation.gov.au/F2019L00417/2025-11-01/text
[ATO]: https://www.ato.gov.au/norfolk-island/tax-for-businesses/gst-transactions-with-mainland-australia

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
