---
name: ly-vat-gst
description: >
  Research indirect-tax classification for Libyan sales, service contracts and imported transactions. Retains the legacy VAT routing slug while distinguishing unconfirmed VAT non-applicability from the stamp-duty law actually read, including contract, assignment and company-capital examples. It distinguishes the source text actually read from unresolved later amendments, records the inputs that change the result, and supplies two recomputing working papers. Use it when researching Libyan tax in 2026, preparing an adviser brief, checking an earlier answer, or identifying which return and supporting records are needed. It is a partial research reference, subject to the currentness limits in the body, and it does not represent a local accountant's sign-off or a tested electronic submission.
jurisdiction: LY
category: international
tax_year: 2026
tax_year_notes: "2026 research edition; domestic amendment chain not closed"
tier: 2
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Libya VAT Status and Transaction Stamp Duties v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research edition, incomplete currentness check.** The domestic rules below are transcribed from the Tax Authority's official 2016 compilation. Its live legislation catalogue and history still identify Income Tax Law 7/2010 and Regulation 592/2010. That establishes the source text, not a complete amendment chain through 2026. Use the calculations as statutory research working papers; obtain the applicable later instruments and current filing instructions before acting. This pack remains partial and has no accountant attestation.

## Who this applies to

Businesses checking Libyan VAT/GST treatment or transaction stamp duties. The read official catalogues do not prove that no VAT or general sales tax exists in 2026. This Guide therefore does not certify VAT non-applicability, a registration threshold, return frequency or reverse-charge exclusion. It supplies the separate stamp-law rules that were actually read. The VAT domain remains partial, not "not applicable".

Stamp Law 12/2004 arts. 1-3 taxes the scheduled documents, transactions and events, including foreign instruments when used or performed in Libya. A turnover-based VAT assumption cannot replace that classification.

## Rates, bands and thresholds

| Transaction and condition | Amount in read statute | Authority | Official URL |
|---|---|---|---|
| Non-exempt supply, works, transport, concession and other service/work contracts | 1% of contract value, borne by contractor/undertaker | Law 8/2010 amended schedule item 28(a) | https://tax.gov.ly/assets/m2016.pdf |
| Assignment of such contract or part | 1% of one tenth of assigned contract value, equivalent to 0.1% | Law 8/2010 schedule item 28(b) | https://tax.gov.ly/assets/m2016.pdf |
| Company formation/capital increase by cash contribution | 5 per thousand of relevant capital, increase or new partner contribution | Stamp Law 12/2004 schedule item 30(a) | https://tax.gov.ly/assets/m2016.pdf |
| Proportional-duty rounding | Round upward to next half dinar | Stamp Law 12/2004 art. 10 | https://tax.gov.ly/assets/m2016.pdf |
| VAT/GST status, threshold, returns and reverse charge | unverified for 2026; absence is not established by this source set | Live authority catalogues are not an exhaustive legal-negative certificate | https://tax.gov.ly/Law1.aspx |

## The base

Identify the exact instrument, event, parties, value, date, place and use. Stamp arts. 2-6 determine when an instrument becomes taxable, how inseparable transactions are classified and how overlapping descriptions use the higher amount. A promise to contract is treated as the underlying contract under art. 5. Separate signed originals/copies require art. 7 analysis; do not assume one stamp pays every counterpart.

Use the amended 2010 schedule, not the superseded original service-contract percentage. Item 28 exempts individual/shared employment contracts, public passenger transport, water/electricity supply and telephone subscriptions. An ordinary subcontract is not the same legal act as an assignment: the old universal "subcontract 0.1%" claim was not supported. Determine which scheduled transaction actually occurred.

For company capital, the relevant cash, property or movable contribution and the party bearing duty come from item 30. Do not substitute a revenue or profit base. Apply the proportional-duty rounding rule after the duty computation.

Stamp art. 21 has party-specific public-budget and recognised non-profit exemptions. Public-sector involvement does not automatically exempt the other party's burden. Article 19 makes the statutory burden mandatory and parties jointly responsible for payment. Article 20 does not refund duty merely because the instrument later produces no benefit. Import service fees, customs tariff classification and investment exemptions require their own applicable instruments; no universal import percentage is established here.

## Deadlines and filing

1. Collect the full executed instrument and amendments, currency/value evidence, date and evidence of Libyan use for a foreign instrument. Classify it against the amended schedule and any proved exemption.
2. Establish the tax point under stamp art. 2. For cash/certified-cheque payment, present the instrument before use and no later than 60 days after liability under art. 11. The foreign instrument rule and its real-property exception need their exact facts; do not defer duty simply because execution was abroad.
3. Submit automatically extended or renewed instruments within 60 days of renewal/extension under art. 12; an unspecified or shorter extension is treated as a year for that rule. Supply all value elements or an additional declaration under art. 13. If value is unknown, art. 14 provides an authority-approved estimate and payment of the difference within 30 days of value determination.
4. Use authorised stamped paper, stamps, authority stamping or cash collection under art. 8 and Reg. 156/2004 arts. 1-4. Obtain a legible receipt/stamp identifying the instrument and retain the calculation and exemption evidence. Current electronic form and payment-reference steps were not verified; the public https://services.tax.gov.ly/ page requires login.
5. Do not create a VAT return, deduct input VAT or apply a reverse charge from this Guide. Close the legal-status research gap first.

## Penalties and interest

Stamp art. 16 imposes 2% of unpaid duty per month or part of at least 15 days, capped at 50%. This is separate from the income-tax late charge. Stamp art. 18 provides a 45-day objection period from notification and a fee of 10% of disputed duty, minimum LYD 10. The source is https://tax.gov.ly/assets/m2016.pdf; current amendments and enforcement practice remain unresolved.

## Cross-border points

Stamp art. 2 reaches an instrument created abroad when used/performed in Libya. A treaty dealing with income taxes does not establish a stamp exemption. Obtain customs documentation and any approved investment exemption rather than inferring import treatment from a VAT conclusion. Treaty income routing is in [Cross-border](ly-cross-border-tax.md).

## Two worked examples that recompute

**Service contract.** A non-exempt service contract is LYD 100,000. The amended item 28(a) duty is LYD 1,000. Exact half-dinar rounding does not change it.

```oa-check
name: Amended service contract duty
inputs:
  contract_value: 100000
steps:
  - raw_duty: contract_value * 0.01
  - duty: ceil(raw_duty * 2) / 2
expected:
  duty: 1000
```

**Assignment or new service decision.** LYD 20,000 is either the value of an assigned part of an existing qualifying contract or the value of a new non-exempt service contract. On an assignment, duty is LYD 20; on a new service contract it is LYD 200. The LYD 180 difference depends on the legal act, not the title "subcontract".

```oa-check
name: Contract assignment versus new service contract
inputs:
  transaction_value: 20000
steps:
  - assignment_duty: ceil(transaction_value / 10 * 0.01 * 2) / 2
  - new_contract_duty: ceil(transaction_value * 0.01 * 2) / 2
  - difference: new_contract_duty - assignment_duty
expected:
  assignment_duty: 20
  new_contract_duty: 200
  difference: 180
```

## Ask the client first

- Is this a sale, service, assignment, capital contribution, payment receipt or another scheduled instrument?
- Where and when was it executed, used, renewed or performed, and what is its full value?
- Which party-specific exemption and approved instrument support relief?
- Are there separate originals, linked instruments or value amendments?
- Which current legal source establishes VAT status or the actual customs/import charge?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Tax Authority, 2016 tax legislation compilation: Stamp Law 12/2004 arts. 1-21 (PDF pp. 122-127), original schedule items 28-30 (p. 141), Law 8/2010 amendment and item 28 (pp. 145-146), Reg. 156/2004 arts. 1-4 (pp. 147-150); original Arabic, local OCR checked against selected page images | https://tax.gov.ly/assets/m2016.pdf | 2026-11-01 |
| Tax Authority live law and regulation catalogues; law titles and the income-law history paragraph, not a consolidated 2026 certificate | https://tax.gov.ly/Law1.aspx ; https://tax.gov.ly/Law2.aspx ; https://tax.gov.ly/TaxHistory.aspx | 2026-11-01 |

Not yet confirmed: complete domestic amendment chain and administrative practice through 2026; 2026 VAT/GST or general sales-tax status, registration and return requirements and reverse charge; current customs/import-service charge; later stamp amendments; the claimed universal salary/payment stamp base; the old subcontract-rate generalisation.

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
