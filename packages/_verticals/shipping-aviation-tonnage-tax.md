---
name: shipping-aviation-tonnage-tax
description: "For 2026 shipping and aviation groups: classify vessel and aircraft activity, compute sourced UK daily tonnage profits, distinguish Singapore MSI awards and Hong Kong aircraft transitions, and test the separate international-shipping top-up-tax exclusion. Holds unconfirmed country rates, elections and flag conditions."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
---

# Shipping, aviation and tonnage-tax method v1.0

## Scope and quick reference

For 2026 ship owners, operators, charterers, ship managers, aircraft lessors and airlines. Build a vessel/aircraft and income-stream workpaper before choosing a country regime. Load `corporate-income-tax-workflow-base` and the actual country corporate-tax, withholding and treaty jobs. This does not replace vessel registration, maritime safety/IMO work, aviation safety, financing documents or a specialist leasing/tonnage election review.

Tonnage tax is not one worldwide rate on shipping receipts. In the UK it substitutes a calculated profit for qualifying commercial profit; the ordinary corporation-tax computation then uses the correct country rules. Other countries' exemptions, deemed profits and direct tonnage charges need their own legal tests. A maritime incentive, ship registry and tax residence do not mean the same thing. [HMRC TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010).

## Ask the client first

- Which legal entities, tax residences, group perimeter, reporting/tax periods and current elections or awards apply?
- What are each vessel's net and gross tonnage, flag, activity, ownership/charter terms, operating dates and management functions?
- Which income is core transport, ancillary, ship management, bareboat/full charter, asset disposal, leasing, finance or unrelated trade?
- Where are strategic/commercial functions, staff, decision makers and the ships' operations actually located?
- For aircraft, what are acquisition dates, lease types, lessees, asset costs, depreciation/tax claims and any transition election?
- Which accounting framework, top-up-tax scope, treaty route and security-interest/registration issues must be resolved?

## The method, step by step

1. Map entity, asset and activity separately. Check the country's entry conditions, group requirements, exclusions, election timing, duration and exit consequences from its own law. Do not import a global flag minimum or lock-in period.
2. Split qualifying shipping, ancillary activities, ship management and ordinary taxable profits. Track all asset disposals, losses, finance/foreign-exchange items and costs to the category that actually owns them.
3. For a tonnage computation, use certified tonnage, each complete statutory unit, actual eligible days and the current bands. A deemed profit is not the tax payable. For an exemption or concession, document the award and eligible income rather than substituting tonnage bands.
4. Assess aircraft leasing separately from shipping. Establish lessor status, activity, substance, acquisition/transition dates, elections and the applicable capital-cost rule. A securitisation or interest deduction is not automatic tax neutrality.
5. Reconcile the financial-reporting lease classification with tax ownership, depreciation, financing and treaty results. Do not replace the lessor's finance/operating assessment with the lessee's right-of-use model.
6. Separately assess top-up-tax scope and the actual international-shipping exclusion. A low tonnage-tax amount does not by itself prove top-up tax is due, nor does domestic tonnage treatment prove the international exclusion is available.
7. Produce the asset register, election/award evidence, qualifying-income bridge, country calculation and filing handoff, with unresolved facts and sources explicitly listed before sign-off.

Authority for the worked UK path is [TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010). The Singapore, Hong Kong and UK top-up-tax paths below have their own sources; countries without confirmed values remain named handoffs rather than a copied rate matrix.

## United Kingdom: tonnage profit

HMRC describes companies within corporation tax operating or managing qualifying ships strategically and commercially managed in the UK; qualifying group members enter together. Establish the detailed Schedule 22 rules, exclusions and actual election before using the table. Net tonnage drives the calculation, while the qualifying-ship test also uses gross tonnage. The guide identifies exclusions including fishing/factory ships, pleasure craft, harbour/river ferries, offshore installations, dedicated field tankers and certain tugs/dredgers. Do not treat every ferry, tug or dredger as the same activity.

For the following table, each amount is a daily **deemed profit**, not a direct tax rate, per complete unit of net tonnage. [HMRC TTM01010, qualifying ships and profit computation](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010).

| Band of net tonnage | Unit | Operated ship daily profit | Managed ship daily profit | Source |
| --- | --- | --- | --- | --- |
| Up to 1,000 | Each complete 100 net tons | GBP 0.60 | GBP 0.12 | [TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010) |
| From 1,001 to 10,000 | Each complete 100 net tons in the band | GBP 0.45 | GBP 0.09 | [TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010) |
| From 10,001 to 25,000 | Each complete 100 net tons in the band | GBP 0.30 | GBP 0.06 | [TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010) |
| Above 25,000 | Each complete 100 net tons in the band | GBP 0.15 | GBP 0.03 | [TTM01010](https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010) |

Multiply each ship's daily amount by the actual days operated/managed and aggregate. Establish the distinct ship-management conditions before using its lower column. Keep qualifying secondary/incidental income, asset gains, overseas shipping distributions and loan relationships within their actual statutory scope; unrelated profits remain taxed normally. Confirm flag/election/lock-in and transition rules for the period instead of inheriting a common EU flag condition.

### Worked case: complete bands and actual days

Assume one fully qualifying UK operated bulk carrier of 30,000 net tons, operated for 365 days within an established election, with no other adjustments or activity. The first band contributes GBP 6 daily, the next GBP 40.50, the next GBP 45 and the final GBP 7.50. Daily deemed profit is GBP 99 and annual tonnage profit GBP 36,135. This does not compute corporation tax; the manual's old hypothetical corporation-tax rate must not be reused as a current rate.

```oa-check
name: UK operated ship tonnage profit
inputs:
  net_tons: 30000
  days: 365
steps:
  band_one: floor(min(net_tons, 1000) / 100) * 0.60
  band_two: floor(max(min(net_tons, 10000) - 1000, 0) / 100) * 0.45
  band_three: floor(max(min(net_tons, 25000) - 10000, 0) / 100) * 0.30
  band_four: floor(max(net_tons - 25000, 0) / 100) * 0.15
  daily_profit: band_one + band_two + band_three + band_four
  annual_profit: daily_profit * days
expected:
  daily_profit: 99
  annual_profit: 36135
```

For a partial period or leap year, use actual qualifying days. Do not round tonnage up or substitute gross tonnage in these bands. Eligibility and an effective election remain prerequisites even when arithmetic works.

## Singapore: keep the award names and activities straight

The [Maritime and Port Authority's MSI page](https://www.mpa.gov.sg/maritime-singapore/what-maritime-singapore-offers/pro-business-environment/support-for-maritime-businesses/maritime-sector-incentive) distinguishes Approved International Shipping Enterprise (MSI-AIS), Shipping-related Support Services (MSI-SSS) and Maritime Leasing (MSI-ML). Do not describe MSI-SSS as the international-shipping award or MSI-ML as simply ship management.

MSI-AIS addresses international owners/operators and qualifying shipping income; MSI-SSS addresses approved support activities and incremental income; MSI-ML addresses ship/container leasing and eligible management. The page now describes an alternative net-tonnage basis for specified shipping awards as well as concessions. Obtain the actual approval, period, qualifying income, economic commitments and applicable law before claiming a benefit. Company spending/headcount requirements, application cut-offs, withholding arrangements and award terms remain a separate current-source task, not a blanket exemption for any Singapore ship company.

Singapore's Aircraft Leasing Scheme is a distinct aviation incentive. Do not equate its rate, manager conditions or approvals with maritime awards. Its current figures are held below rather than carrying the old approximate rate.

## Hong Kong: aircraft transition and ship leasing are different regimes

The [IRD aircraft-leasing page](https://www.ird.gov.hk/eng/tax/bus_ala.htm) distinguishes the earlier concession from amendments enacted in 2024. Do not apply the old global statement that half of gross lease income is the tax base. IRD's earlier regime describes a share of **net lease payments**, and its amendment section introduces acquisition-cost deductions, expanded leasing scope, interest rules, threshold requirements and a transition election. Read the transaction's acquisition/basis period and actual ordinance before selecting the old or amended method. The summary is not an election on the client's behalf; current numerical rate/base, depreciation transition and full substance tests remain held pending the applicable legal version.

Hong Kong shipping, ship leasing, ship-management services and aircraft leasing are separate categories. The [IRD qualifying-ship-lessor S11 instructions](https://www.ird.gov.hk/eng/faq/s11.htm) require the company's own basis period, ships and activities, not the whole group's vessel count by default. A market-wide "half-rate shipping" label is not a general rule. Confirm the actual ship-lessor/manager regime, amendments and concession conditions for the relevant assessment year.

## Ireland and Bermuda: aircraft and finance handoffs

For Ireland preserve the trading-versus-investment question, aircraft capital allowances, section 110 qualifying-company/SPV conditions, interest deduction/anti-avoidance, treaty residence/substance and top-up-tax scope. The old depreciation percentage, assertion of automatic neutrality and assumption that every lessor is a trade are not usable. Obtain the relevant Revenue/legislation source and election facts.

For Bermuda preserve securitisation, the aircraft registration/security-interest question and the in-scope multinational corporate-tax regime. Do not use a flag registration or Cape Town status to infer residence, a tax exemption or an enacted concession. Corporate-tax scope, commencement and transition values remain held for the country job.

## Other tonnage and shipping jurisdictions

Maintain individual country sheets for Greece, Cyprus, Malta, the Netherlands, Belgium, Denmark, Norway, Sweden, Germany, France, Italy, Spain, Ireland, Portugal, South Korea, India and Japan. Each sheet must establish:

- The law and current effective period, entity/operator/manager/charterer scope and actual entry election.
- The qualifying ship/activity, ownership or charter limits, commercial/strategic management functions and flag conditions.
- Whether the regime computes profit, charges a tax directly or exempts specified income; correct net/gross units and bands.
- Qualifying ancillary, ship-management, cabotage, asset-disposal and non-qualifying income treatment.
- Duration, renewal, exit/recapture, group requirements, losses, financing and filing route.

The former Greek fleet percentage, constitutional shorthand, common flag percentage, Norwegian distribution assertion, country band units, universal lock-in and claimed revised EU guideline date have not been confirmed. These are held questions, not conditions established by this guide. For US international ship/aircraft income, preserve the IRC section 883 reciprocal-exemption, ownership and documentation question for its existing country job; do not assume a foreign flag alone establishes relief.

## Top-up tax: do not overlook the international-shipping exclusion

The UK example is a separate statutory test from domestic tonnage tax. [HMRC MTT45610, Finance (No.2) Act 2023 sections 156-158](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45610) describes exclusion of qualifying international-shipping income and related costs from the effective-tax-rate calculation. It requires the specified strategic **or** commercial management condition for every relevant ship in the member's territory. It is not simply the domestic tonnage test carried over.

Core and ancillary activities have separate definitions and cost allocation. The ancillary exclusion is capped by reference to core profits for the territory; test the cap/adjustment and negative-profit cases before computing the amount. Keep this country's implementation separate from other jurisdictions. An airline's income is not international **shipping** income simply because both industries appear in this guide. Do not say a low nominal tonnage amount automatically produces top-up tax. [MTT45620](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45620), [MTT45630](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45630) and [MTT45635](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45635).

## Lease accounting and security interests

For ships and aircraft, keep lessor finance/operating classification, rental recognition, modifications, residual values, impairment, sale-and-leaseback and tax ownership separate. IFRS lessor classification is not the lessee's right-of-use accounting model, and another framework can differ. The detailed lessor requirements, rather than a statement that most industry leases are operating leases, must support the entry. The [AASB 16 official text](https://standards.aasb.gov.au/aasb-16-nov-2022) identifies the lease and lessee recognition boundary; detailed lessor application remains held pending the specific contract and full applicable section.

The Cape Town Convention/Aircraft Protocol question concerns international security interests, priority and insolvency remedies, not an automatic tax concession. For any financing structure, identify the asset, debtor, jurisdictions, declarations, effective dates and registrations and obtain the current treaty/domestic-law conclusion. No worldwide signatory claim or legal-priority opinion is supplied here.

## When to refuse or refer

- Missing certified tonnage, qualifying days, election, award or activity evidence: do not compute a final regime benefit.
- An unconfirmed flag, lock-in, treaty, depreciation or capital-cost transition rule: list the exact country and unresolved condition.
- Complex chartering, aircraft SPVs, finance leases, securitisations, Cape Town priority, top-up tax or disputed substance: obtain the specialist legal/tax conclusion before sign-off.

## Completion checklist

- Asset/period register and qualifying versus ordinary income reconcile.
- Operator, manager, owner, charterer, lessor and lessee roles are separated.
- Certified units/days and current bands match an effective election or award.
- Actual national flag, management, group, renewal, exit and filing conditions are established.
- Aircraft acquisition costs, finance/treaty and transition questions are separately documented.
- Top-up-tax shipping exclusion, costs, ancillary cap and country implementation are assessed before any top-up conclusion.
- All held figures remain outside the usable computation.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| HMRC TTM01010 | https://www.gov.uk/hmrc-internal-manuals/tonnage-tax-manual/ttm01010 | 2026-11-14 | Read for qualifying/excluded ships, management and group conditions, operated/managed daily profit bands, actual-day calculation and ordinary-profit boundary |
| Singapore MPA, Maritime Sector Incentive | https://www.mpa.gov.sg/maritime-singapore/what-maritime-singapore-offers/pro-business-environment/support-for-maritime-businesses/maritime-sector-incentive | 2026-11-14 | Read for the AIS/SSS/ML award descriptions, qualifying activities and alternative tonnage basis; no full award-law/economic-commitment verification claimed |
| Hong Kong IRD, aircraft leasing | https://www.ird.gov.hk/eng/tax/bus_ala.htm | 2026-11-14 | Read for earlier net-payment concession versus 2024 amendment/transition sections; summary does not replace current ordinance tests |
| Hong Kong IRD, S11 ship-lessor FAQ | https://www.ird.gov.hk/eng/faq/s11.htm | 2026-11-14 | Read for basis period and company-specific vessel/lease reporting; not a full ship regime rate confirmation |
| HMRC MTT45610 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45610 | 2026-11-14 | Read for international-shipping exclusion, per-ship management condition, ancillary limit and SBIE boundary |
| HMRC MTT45620 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45620 | 2026-11-14 | Read for core international-shipping activity and revenue/cost allocation |
| HMRC MTT45630 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45630 | 2026-11-14 | Read for ancillary activity, allocation and cap-adjustment handoff |
| HMRC MTT45635 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt45635 | 2026-11-14 | Read for the cap-adjustment question; detailed negative-profit case not implemented in this guide |
| AASB 16, November 2022 compilation | https://standards.aasb.gov.au/aasb-16-nov-2022 | 2026-11-14 | Read for identified-lease and recognition-exemption sections; detailed lessor application held |

Not yet confirmed: all national tonnage/flag/entry/exit/tenure/management/ancillary values for the named countries except the limited UK sourced path; claimed EU guideline update and uniform flag/lock-in rules; Greek fleet and constitutional shorthand; Norway distribution condition; full UK flag/election/transition and secondary/incidental rules; Singapore award-law/economic commitment details and Aircraft Leasing Scheme figures; Hong Kong current numerical concession, acquisition-cost transition and ship-leasing amendment conditions; Ireland trading/capital-allowance/section 110/interest/treaty conclusions; Bermuda corporate-tax and aircraft/security-interest conditions; US section 883 relief; Cape Town treaty/declarations and domestic-priority conclusion; full lessor accounting/US GAAP comparison; detailed top-up-tax ancillary-cap negative cases and non-UK implementation. The previous figures are not carried into usable guidance.
