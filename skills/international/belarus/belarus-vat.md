---
name: belarus-vat
description: Compute ordinary Belarus value-added tax for the 2026 calendar year for domestic organisations and foreign permanent establishments, with specific routing for individual entrepreneurs and simplified taxpayers. Trigger on Belarus NDS, VAT registration, place of supply, reverse charge, input tax, electronic invoices, exports, monthly or quarterly VAT returns and import VAT. The skill sets out the standard, reduced and telecom rates, distinguishes exemptions from zero-rated turnover, explains signed electronic-invoice evidence and mixed-use credit allocation, and provides filing, payment, refund and correction rules with two recomputing examples. Foreign digital-consumer and distance-selling registrations and specialist sector schemes require their separate statutory procedures. Use alongside the corporate and cross-border skills; tier 2, checked against the law.
version: 2.1
jurisdiction: BY
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Belarus VAT, 2026 v2.1

## Who this applies to

2026 ordinary domestic VAT on supplies by organisations and relevant foreign businesses, plus import and purchaser tax-agent obligations. Art. 112 generally excludes Belarus individual entrepreneurs from VAT on their domestic sales, apart from the specified art. 129(7) case. It does not remove import or foreign-supplier purchaser obligations. Simplified organisations generally replace domestic-sales VAT under art. 326(1.2), while import/purchaser VAT remains. Do not invent a universal small-business turnover-registration threshold for ordinary organisations. [Code arts. 112, 114, 129(7), 326(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071).

General registration is under General Code arts. 69-70. A payer's domestic obligation follows legal status/regime and taxable operations; low turnover alone is not deregistration. On liquidation or a valid regime change, determine the effective cessation and final obligations under General Code art. 44 and Special Code arts. 127-137. Foreign digital-consumer and distance-selling registration under arts. 141-141-1 is a separate route, outside the computations here. [General Code arts. 44, 69-70](https://pravo.by/document/?guid=3871&p0=hk0200166); [Special Code arts. 127-141-1](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official act/article |
|---|---|---|---|
| Standard domestic supplies and imports, including electronic services | 20% | 2026 | [Code art. 122(3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Eligible listed food/children's goods, qualifying agricultural and medical products | 10%, only within statutory goods/registration conditions | 2026 | [Art. 122(2), Annex 26](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Telecommunications services | 25% | 2026 | [Art. 122(4)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Documented export goods and qualifying related services | 0% | 2026 | [Arts. 122(1), 123-126](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Ordinary reporting period | Month by default; eligible quarterly election; telecom monthly | 2026 | [Art. 127](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Input allocation ratio precision | At least 4 decimal places in percentage share | 2026 | [Art. 134(3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Ordinary electronic invoice issue deadline | 10th of following month, subject to specific exceptions | 2026 | [Art. 131(5)](https://pravo.by/document/?guid=3871&p0=hk0900071) |

## The base

1. **Classify the supply and place.** Domestic taxable turnover and imports are within art. 115, subject to exclusions. Goods use art. 116, including where located or dispatched. For services, art. 117 takes priority by category: immovable-property location, physical movable-property work, specified actually performed services, customer location for listed consultancy/accounting/legal/advertising/IP and similar services, then the residual supplier-location rule. Do not apply a single B2B customer-location rule to every service. EAEU transactions require the applicable treaty/indirect-tax protocol as well. [Arts. 115-117](https://pravo.by/document/?guid=3871&p0=hk0900071).
2. **Separate taxable, exempt and zero-rated turnover.** Art. 118 exemptions, including qualifying health, education and financial services, have their own conditions. Zero rating requires the evidence and deadlines in arts. 123-126; a foreign customer is not proof of zero rating. Keep export goods, transport and other services distinct. [Arts. 118, 122-126](https://pravo.by/document/?guid=3871&p0=hk0900071).
3. **Set the base and tax point.** Ordinarily base equals consideration including excise but excluding VAT (art. 120). Include statutory price supplements, contractual sanctions and relevant noncash/free transfers under arts. 115/120. Use shipment/performance and the specific timing rules of art. 121, not an assumed receipt rule for all domestic supplies. For tax-exclusive value, output VAT is base times rate; for tax-inclusive value, VAT is gross times rate divided by one plus rate. Track returns, cancellations, price changes and currency conversion under arts. 120-121/129-130 and issue corrected/additional invoices under art. 131. [Arts. 120-121, 128-131](https://pravo.by/document/?guid=3871&p0=hk0900071).
4. **Purchaser tax-agent VAT.** Where a foreign supplier is not registered and the supply is located in Belarus, the Belarus purchaser fulfils the obligation under art. 114 even when not an ordinary domestic VAT payer. Determine the base/rate and tax point under the applicable statutory provisions and create the purchaser electronic invoice. Claim purchaser input VAT only when the art. 132-133 payment, accounting and document conditions are met; no automatic immediate offset. [Arts. 114, 120-122, 129, 131-133](https://pravo.by/document/?guid=3871&p0=hk0900071).
5. **Establish credits.** Domestic input tax requires a seller invoice received and signed with the purchaser's electronic signature, accounted acquisition and, if elected, entry in the purchase book. Import tax requires payment and the customs or EAEU return/payment documents plus the portal invoice. Purchaser-agent tax requires the return and portal invoice and statutory payment conditions. An ordinary unpaid domestic supplier invoice is not disallowed solely because unpaid, subject to exceptions. Do not claim undocumented or exempt-use input tax. [Art. 132(1),(3)-(5)](https://pravo.by/document/?guid=3871&p0=hk0900071).
6. **Allocate mixed credits.** Use the accounting-policy separate-accounting or turnover-share method consistently through the calendar year; turnover share is default if no policy specifies the method. Under art. 134(3), the denominator and relevant turnover are VAT-inclusive, including statutory base adjustments. Allocate exempt-use ordinary input tax to costs under art. 133(3), distinguish capital/intangible credits, and apply art. 135's ordering and output-tax limits. Retain unutilised limited credits. Special eligible zero/reduced-rate credits are deductible beyond output tax under arts. 133(27)/135(2); do not call every excess a refundable cash balance. [Arts. 133-135](https://pravo.by/document/?guid=3871&p0=hk0900071).
7. **Net and reconcile.** Compute cumulative output VAT less allowable credits, adjusting for earlier period calculations/payments. Follow art. 137 for eligible excess-credit set-off/refund: apply to the inspectorate, reconcile arrears and retain the supporting documents. Under art. 137(2), with the VAT return on file, the decision is due within two working days of the written application, electronic acceptance confirmation or completion of the applicable check, and is sent within five working days. An ordinary verification inspection under art. 137(3) is appointed within two working days and the verification period is no more than fifteen working days from the refund application; liquidation and exported-oil-product cases have distinct timing. The ordinary set-off period is thirty calendar days after the decision; the remaining eligible balance is refunded within five working days after that period, subject to budget/tax debts. Art. 137(5-1) delays payment for an evidence notice or later inspection: apply its ten-working-day period after accepted evidence/desk-audit act, or five working days after the later inspection act, and never earlier than the ordinary refund deadline. Keep the return, application acceptance, decision, notices, offsets and payment trace. [Arts. 128, 135, 137](https://pravo.by/document/?guid=3871&p0=hk0900071).

**Non-EAEU customs imports.** For ordinary release for domestic consumption, Special Code art. 138(2),(5) gives `import VAT base = customs value + payable import duty + payable excise`, and `VAT = base × applicable Belarus VAT rate`. Establish customs value/classification and verify art. 119 exemptions and any procedure-specific relief before calculation. The declarant's obligation arises when customs registers the goods declaration; pay before release for domestic consumption unless a different lawful deadline/deferment applies. Use the customs declaration/payment/release process, retaining valuation, tariff, excise, payment and release records for the paid-import VAT credit under art. 132. The domestic-return 22nd-day deadline is not the customs-import payment deadline. Special procedures, conditional exemptions and release before declaration require their separate customs provisions. [Special Code arts. 119, 122, 132, 138](https://pravo.by/document/?guid=3871&p0=hk0900071); [EAEU Customs Code arts. 135, 136(1),(9), official treaty publication](https://docs.eaeunion.org/documents/236/2895/).

**25 July-31 December 2026 deferral.** Council Resolution 369 of 23 July 2026 permits legal entities an interest-free import-VAT deferral of no more than three months, counted from the day after release for domestic consumption, provided payment is secured. The goods declaration containing the required deferral information is the application. The act was published 24 July, takes effect after publication and runs through 30 June 2027. Before its 25 July commencement use the ordinary customs rules or another separately established relief. Record the granted due date and security; deferred VAT is not paid VAT for input-credit purposes until its payment conditions are met. [Resolution 369 paras. 1-2, official one-page PDF](https://pravo.by/document/?guid=12551&p0=C22600369); [Special Code art. 132](https://pravo.by/document/?guid=3871&p0=hk0900071).

**EAEU imports.** The owner importing goods from another EAEU member accounts for indirect tax even if it uses a special regime. Under EAEU Treaty Annex 18 paras. 13-20, take the contract purchase price plus excise where applicable at accounting acceptance, converting foreign currency at the National Bank rate on that date. Apply Belarus's relevant 20%/10% rate, then file the import indirect-tax return and pay by the 20th of the following month. This is monthly and separate from the domestic quarterly election. Submit the import-and-indirect-tax statement (four paper copies plus electronic version, or the prescribed signed electronic format), payment bank extract unless the authority confirms payment, transport/shipping evidence, invoices and contracts, plus the conditional intermediary/information documents in para. 20. Retain the authority's statement confirmation for the exporter's zero-rate evidence and the paid-import-VAT credit; do not claim ordinary domestic credit solely from the foreign seller's invoice. Non-EAEU customs imports instead use art. 138. [Special Code arts. 132, 138-139](https://pravo.by/document/?guid=3871&p0=hk0900071); [MNS official EAEU Treaty and Annex 18 publication](https://nalog.gov.by/eec/).

## Deadlines and filing

| Obligation | Rule | Official source |
|---|---|---|
| Ordinary return/payment | Return by 20th, payment by 22nd of month after reporting period | [Art. 136(1)-(2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Quarterly election | Mark previous-year return by 20 January; one correction by 20 February; new entities notify by 20th following registration month; specific first-object/transition cases follow art. 127 | [Art. 127(3)-(5)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Ordinary seller electronic invoice | Not before shipment/performance and by 10th following month; specific unconfirmed-document and transaction exceptions apply | [Art. 131(5)-(8)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Legal-entity import-VAT deferral from 25 July 2026 | Up to three months from day after release; interest-free with security; declaration is application; act runs through 30 June 2027 | [Resolution 369 paras. 1-2](https://pravo.by/document/?guid=12551&p0=C22600369) |
| Customs import VAT, ordinary domestic-consumption release | Pay before release unless a different lawful customs deadline applies; goods declaration/customs release process | [EAEU Customs Code art. 136(1),(9)](https://docs.eaeunion.org/documents/236/2895/) |
| EAEU import VAT | Return and payment by 20th of month after accounting acceptance; import statement and evidence accompany it | [Art. 139](https://pravo.by/document/?guid=3871&p0=hk0900071); [EAEU Treaty Annex 18 paras. 19-20](https://nalog.gov.by/eec/) |
| Liquidation/reorganisation | Final returns under General Code art. 44; seller invoices by the specific cessation/reorganisation dates in art. 131(7) | [General Code art. 44](https://pravo.by/document/?guid=3871&p0=hk0200166); [art. 131(7)](https://pravo.by/document/?guid=3871&p0=hk0900071) |

Use MNS electronic returns and the electronic-invoice portal. Retain sales, purchases, signed invoices, customs/import records, export proof and policy allocations. Correct the return for the legally affected period; an invoice correction alone does not automatically amend a filed return. Tax nonworking-day extensions follow General Code art. 4. [General Code arts. 4, 40](https://pravo.by/document/?guid=3871&p0=hk0200166); [Special Code arts. 131-137](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Penalties and interest

Late-payment interest under General Tax Code art. 55 is computed separately for each period of constant unpaid tax and National Bank refinancing rate: `unpaid tax × overdue calendar days × annual rate / 360 / 100`. Count from the day after the due date through payment; interest reflected in the audit decision on audit-assessed tax is capped at that assessed tax amount; apply art. 55(3) exclusions and art. 55(4)'s four-decimal interest-rate precision. Use the rate actually in force in each period, not a single assumed 2026 rate. [General Code art. 55](https://pravo.by/document/?guid=3871&p0=hk0200166).

For a business/agent return, Administrative Code art. 14.2(1)-(2) sets up to 1 basic unit for no more than 3 working days late; otherwise 2 basic units plus 0.5 per complete month, capped at 10. Repetition within a year invokes art. 14.2(4), 3 per complete or incomplete month, capped at 20. Under art. 14.4(1), business tax underpayment carries 40% of unpaid tax, minimum 2 basic units for an entrepreneur or 10 for a company, subject to the statutory notes, including timely voluntary correction/payment. Do not apply these amounts automatically to an ordinary individual or to a withholding default. [Administrative Code arts. 14.2 and 14.4](https://pravo.by/document/?guid=3871&p0=hk2100091). The basic unit is BYN 45 from 1 January 2026 ([Council Resolution 651 of 20 November 2025](https://pravo.by/document/?guid=12551&p0=C22500651)).

Foreign purchaser-agent defaults require Administrative Code art. 14.5 analysis. Apply the specific electronic-service foreign-payer grace provisions only to the taxpayers described in the notes to arts. 14.2/14.4; they are not a domestic VAT grace period. [Administrative Code arts. 14.2, 14.4-14.5](https://pravo.by/document/?guid=3871&p0=hk2100091).

## Cross-border points

Non-EAEU imports involve customs VAT under art. 138; EAEU imports involve art. 139 and the indirect-tax treaty procedure. Export zero rating requires the respective customs or EAEU evidence under arts. 123-124. Foreign service purchases require the place/purchaser analysis above. Foreign digital-consumer and distance-selling cases must be routed to arts. 141-141-1 before assuming no Belarus registration or tax. Direct-tax treaty business-profit relief does not settle VAT. [Arts. 114, 117, 123-124, 138-141-1](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Two worked examples that recompute

### 1. Ordinary domestic sales and fully supported credits

Tax-exclusive standard-rate sales are BYN 100,000 and eligible signed-invoice ordinary input VAT is 12,000. The credit is below output VAT and all use is taxable. Output VAT 20,000 less credit 12,000 leaves 8,000 payable.

```oa-check
name: BY 2026 standard VAT with supported credit
inputs:
  sales: 100000
  eligible_input: 12000
steps:
  output: sales * 0.20
  payable: output - eligible_input
expected:
  output: 20000
  payable: 8000
```

### 2. VAT-inclusive mixed turnover

The elected turnover-share method applies to BYN 10,000 common ordinary input tax, with no capital assets or special full-credit categories. Taxable sales are BYN 120,000 inclusive of 20,000 VAT, and exempt turnover is 80,000. Taxable share is 120,000 / 200,000 = 60%, rather than a ratio using taxable net sales. Credit is 6,000, exempt-use input cost 4,000 and VAT payable 14,000. All figures are cumulative for the same period.

```oa-check
name: BY 2026 mixed-use VAT-inclusive allocation
inputs:
  taxable_gross: 120000
  exempt_turnover: 80000
  common_input: 10000
steps:
  output: taxable_gross * 0.20 / 1.20
  share: taxable_gross / (taxable_gross + exempt_turnover)
  credit: common_input * share
  exempt_cost: common_input - credit
  payable: output - credit
expected:
  credit: 6000
  exempt_cost: 4000
  payable: 14000
```

## Ask the client first

- What are the entity status, domestic regime, UNP and effective regime-change dates?
- What exactly is supplied, where are goods/property and customers, and who contracts/pays?
- Which supplies are exempt, reduced-rate or zero-rated, and what documents prove that treatment?
- Are input invoices signed, acquisitions accounted and import/purchaser VAT paid?
- Which reporting-period election and allocation policy were validly filed/adopted?
- Are there imports, foreign suppliers, returns, advances, old credits, arrears or pending refunds?

## Sources

| Source and read scope | Official URL | Read on |
|---|---|---|
| Tax Code Special Part, arts. 112-141-1, 326(1.2), Annex 26 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-24 |
| Tax Code General Part, arts. 4, 40, 44, 55, 69-70 | https://pravo.by/document/?guid=3871&p0=hk0200166 | 2026-10-24 |
| Council Resolution 369 of 23 July 2026, paras. 1-2, official PDF p. 1; publication/commencement and secured import-VAT deferral | https://pravo.by/document/?guid=12551&p0=C22600369 | 2026-10-24 |
| EAEU Customs Code, treaty of 11 April 2017, arts. 135, 136(1),(9), official PDF physical pp. 340-350 (clause 9 on printed p. 347) | https://docs.eaeunion.org/documents/236/2895/ | 2026-10-24 |
| EAEU Treaty of 29 May 2014, Annex 18 paras. 13-20; official treaty PDF linked from MNS | https://nalog.gov.by/eec/ | 2026-10-24 |
| Administrative Code, arts. 14.2, 14.4-14.5 | https://pravo.by/document/?guid=3871&p0=hk2100091 | 2026-10-24 |
| Council Resolution 651 of 20 November 2025, paras. 1, 3, official PDF, basic unit BYN 45 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500651 | 2026-10-31 |

Pravo consolidated HTML was read in a normal browser after scripted access returned HTTP 403. Published PDFs were read in the official browser PDF viewer. Checked against the law (tier 2); no licensed Belarusian accountant has signed it off.

Not yet confirmed: Foreign digital-consumer, marketplace, tax-free retail and special sector workflows are outside this ordinary domestic/EAEU-import scope; no absence of tax or registration is inferred. Ordinary input credit, mixed allocation, filing and EAEU-import procedure are supplied.

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
