---
name: im-related-party-uk-treaty
description: >
  Prepare Isle of Man–UK associated-enterprise adjustment workpapers under
  Article 9 of the 2018 treaty. Identify relationships, reconcile a supported
  pricing adjustment and assemble corresponding-relief evidence. Domestic
  related-party rules, reporting and other treaties remain unverified.
jurisdiction: IM
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Isle of Man–UK related-party treaty adjustments v0.1

## Who this applies to

This scoped draft concerns enterprises in the Isle of Man–UK treaty corridor. Article 9(1) addresses direct or indirect participation in management, control or capital, including common participation in both enterprises. It permits profit adjustments where their commercial or financial conditions differ from independent-enterprise conditions and suppress profits. It states no universal ownership percentage in this test. [2018 agreement, Article 9][treaty]

Treaty residence and entitlement must first be established. See the [non-resident Guide](im-non-resident-income-tax.md) for the existing residence and dispute discussion. This draft does not establish a general domestic transfer-pricing filing regime or an exemption from one. Those questions require separate statutory verification.

## The adjustment and corresponding relief

Article 9(2) requires an appropriate adjustment where its conditions hold: one territory includes and taxes profits already taxed to the other enterprise, and the included profits reflect independent-enterprise conditions. Other treaty provisions and, where necessary, competent-authority consultation matter. A foreign assessment alone does not establish all conditions. [Article 9(2)][treaty]

Prepare the following workpaper as a practical evidence framework. This checklist is our preparation method, not a prescribed local-file filing requirement:

- Draw the ownership, management and control relationships, identifying each enterprise's residence and the relevant period.
- Identify the actual transaction, contractual terms, invoices, booked amounts and parties performing the work.
- Document the functions, assets and risks supporting the proposed independent-party result, together with the comparable evidence and its limitations.
- Reconcile the proposed adjustment to each enterprise's ledger and tax computation. Keep currencies, exchange assumptions and timing consistent.
- Obtain the foreign assessment, calculation, payment evidence and correspondence. Identify whether the same profits were taxed twice and how the proposed relief addresses that overlap.
- Record the authority, submission, decision and implementation evidence for relief. Keep domestic appeal and payment deadlines under separate control.

No markup, interest rate, method priority or documentation threshold is prescribed by this preparation checklist.

## Rates, bands and thresholds

Article 9 supplies a profit-adjustment mechanism, not a tax rate. Calculate any resulting tax only after establishing the enterprise's applicable domestic rate and base. This draft provides no universal safe harbour, ownership threshold, small-business exemption or automatic tax refund.

## Worked example

Assume reliable analysis establishes an independent-party price of GBP 95 per unit for 1,000 units sold for GBP 80 per unit. The assumed revenue shortfall is GBP 15,000. This calculation does not establish the comparable price, whether Article 9 applies, domestic adjustment power, tax rate or corresponding relief.

```oa-check
name: Isle of Man UK assumed associated enterprise pricing difference
inputs:
  units: 1000
  booked_unit_price: 80
  supported_unit_price: 95
steps:
  booked_revenue: units * booked_unit_price
  supported_revenue: units * supported_unit_price
  assumed_profit_adjustment: supported_revenue - booked_revenue
expected:
  booked_revenue: 80000
  supported_revenue: 95000
  assumed_profit_adjustment: 15000
```

## Ask the client first

- Which entities, residences, periods and relationships are involved?
- What was supplied, and what records support the price and actual conduct?
- Which authority adjusted which profits, and what tax was assessed and paid?
- What relief, objections or treaty requests have already been submitted?

## Sources and review limits

Read 23 October 2026: [enacted 2018 agreement, Article 9][treaty], retrieved in indexed official text. Direct browser retrieval rejected the XHTML content type. [Official instrument PDF][pdf] corroborates the adjustment text. Independent review and professional attestation remain outstanding.

Not yet confirmed: current domestic related-party/anti-avoidance rules and amendments; deductions and loans to participators; country-by-country reporting scope, notifications and filing; other treaties; detailed valuation and methods; current procedural requirements, sanctions and live relief routes. No not-applicable finding is made. This fills a scoped writing gap while the TP domain remains partial.

[treaty]: https://www.legislation.gov.uk/uksi/2018/1347/made
[pdf]: https://www.legislation.gov.uk/uksi/2018/1347/pdfs/uksi_20181347_en.pdf
