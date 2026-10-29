---
name: fi-property-transfer-tax
description: >
  Calculate Finnish transfer tax on direct real estate, buildings and housing or real-estate-company shares acquired in 2026. Establish the taxable consideration, property-company debt and ownership percentage before applying the statutory rate. Covers signing versus ownership-transfer deadlines, private and agent-assisted transactions, new construction, foreign buyers, indirect property interests, earnout consideration under the 2026 amendment, corrections, refunds and statutory late-filing sanctions. Trigger on varainsiirtovero, debt-free price, housing shares, property purchase, additional consideration or title registration. Annual real-estate tax is a separate liability, while rental income and disposal gains belong in the individual or corporate income-tax computation.
version: 0.5
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: property
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland property transfer tax v0.5

## Who this applies to

Use for an ordinary buyer of Finnish land, a qualifying leasehold/building or housing/real-estate-company shares. Identify the asset before applying a rate: ownership of housing shares is a securities acquisition even where it gives possession of a particular apartment. Tax is imposed on transfers for consideration; gifts and inheritance do not become taxable purchases merely because ownership changes. Exchanges, debt assumption and transfers using funds outside matrimonial/estate distributions require a consideration analysis. Corporate reorganisations and historical first-home claims are separate specialist transactions. [Transfer Tax Act 931/1996 §§1,4–5,15–18][law].

## Rates, bands and thresholds

| Item | Rule for 2026 contracts | Official source |
|---|---|---|
| Direct real estate and qualifying building/leasehold | 3% of purchase price or other consideration | Act §§5–6 [text][law] |
| Housing/real-estate-company shares and other taxable securities | 1.5% of statutory consideration; include applicable company debt | Act §20 [text][law] |
| Direct property ordinary payment | By title/leasehold registration application; otherwise within 6 months of contract | Act §7 [text][law] |
| Securities ordinary payment | Within 2 months of contract; agent/new-construction exceptions below | Act §21 [text][law] |
| Later contingent consideration | Separate 2 months after both obligation and amount confirmed after ordinary deadline | Act §§7(2),21(5), Act 1143/2025 transition [text][law] |
| Late title application | 20% of tax for each started 6-month delay, maximum 100% | Act §8 [text][law] |
| Voluntary late filing within 60 days | EUR 50 individual/estate; EUR 100 other taxpayer, per return, subject to statutory exceptions | Act §36b [text][law] |
| Tax increase | Ordinary 10% of added tax; statutory minimum EUR 75 individual/estate, EUR 150 other | Act §36a [text][law] |

## The base

### Direct property

Establish cash consideration plus the fair value of other consideration under §6, allocating supported amounts between the acquired property and any separately transferred assets. If no allocation is established, §6 can tax the whole consideration. A debt assumed as consideration is not excluded merely because cash goes to a lender. For an exchange, analyse each party's acquisition and its consideration, rather than taxing only a cash balancing amount. Record the acquired fraction and ensure the price already reflects it; do not multiply by the ownership fraction twice. [Act §§4–6][law].

Separate movable items only with evidence of what was sold and its defensible value. A plot and a building owned by different persons require separate titles and bases. A right to lease land is within §5 when its statutory registration/transfer conditions are met. For a pure gratuitous gift or inheritance, preserve the instrument and liability evidence; an accompanying paid acquisition remains separately analysable. [Act §§4–6][law].

### Housing and property-company shares

Start with cash plus the value of other consideration, including a contractual performance to a third party benefiting the seller within §20(1). Add debt allocated to the shares where §20(3)–(5) requires it: unpaid housing-company debt can be taxable even if the purchaser leaves the company to repay it through later charges. Reconcile the debt-free base to the deed, manager's certificate, loan ledger and ownership-transfer facts. Do not add a loan a second time where the stated debt-free consideration already includes it. [Act §20][law].

For newly built property-company shares, establish completion/approval for use, ownership transfer and construction-period debt under §20(5). Do not select an advertised cash price while excluding an allocated construction loan. The buyer's own bank financing does not independently add to the base when it merely finances consideration already included. [Act §20][law].

Multiply the correctly established base by 3% or 1.5%. A consideration stated in a foreign currency is converted to euros at the European Central Bank rate published for the payment date, and no tax is payable if the amount is under EUR 10. [Act §27][law]. For several buyers prepare each buyer's allocation and own return/payment; the total of their bases and tax must reconcile to the acquisition. [Act §§6,20,30][law].

### Exemption screen

First-home relief is abolished for contracts from 1 January 2024. Do not give a 2026 purchaser an age-based first-home exemption. Apply only the actual statutory exemption, such as a genuinely gratuitous acquisition, qualifying public-body acquisition or qualifying business transfer, after establishing all its conditions. Securities traded on an exchange have a specific exemption in §15a; that is not a general exemption for an apartment-share acquisition. Historic relief, reorganisations and fund structures require their own statutory analysis. [Act §§4,10,15,15a,17,43; repeal of §§11,25][law]; [Vero overview][overview].

## Deadlines and filing

File a transfer-tax return by the tax-payment deadline under §30, including an exempt business-transfer return where required. Corporate entities file electronically. Use the buyer's transfer-tax reference and retain the return receipt, payment and certificate. Filing does not itself pay the tax. [Act §§7,21,30][law]; [Vero filing instructions][filing].

| Transaction | Ordinary deadline / filer |
|---|---|
| Direct real estate requiring registration | Buyer files and pays by application; apply for title within 6 months of contract. An automatic application in the digital transaction service brings payment/filing to contract completion. |
| Building with no title/leasehold registration | Buyer files and pays within 6 months of contract. |
| Existing housing shares, private sale | Buyer files and pays within 2 months of signing. |
| Existing housing shares with real-estate agent | Pay at signing; agent supplies the return under its reporting duty. Confirm the certificate. |
| New construction within §21(2) | Buyer files and pays within 2 months after ownership transfer; agent involvement does not remove the buyer's duty. |

[Act §§7,21,30–31][law]; [Vero deadline table][deadlines]. For digital deeds signed on different dates, use the final required signature as the contract date. Apply next-business-day rules for a statutory holiday/weekend; calendar the registration application separately. [Vero filing instructions][filing]; [deadline table][deadlines].

For a **contract signed from 1 January 2026** with a true contingent earnout, report the clause on the original return and pay the known original tax by its ordinary deadline. If both obligation and amount become known by that deadline, include them by that original deadline. If confirmed later, correct the return with the amount and confirmation date and pay the additional tax within two months. This does not extend a fixed purchase-price instalment's deadline. Preserve the clause and evidence of confirmation, not just the bank-payment date. [Act §§7(2),21(5), Act 1143/2025][law]; [Vero earnout instructions][earnout].

A wrong return is corrected by a full replacement including unchanged information. A correctly filed tax that was underpaid requires the missing payment, not a fabricated new acquisition. If both declared and paid tax were too high, apply for a refund instead of expecting a replacement return alone to refund paid tax. Ordinary refund claims are within three years after the end of the year of the transfer; §40 has a separate ten-year maximum for the specified invalidation/unwinding grounds. Keep the signed deed and ground for relief. [Act §40][law]; [Vero correction procedure][corrections].

## Penalties and interest

Voluntary filing/correction within 60 days uses the late fee rather than the tax increase where §36b conditions hold. Outside that route, §36a imposes 10% of added tax ordinarily; repeated or manifest disregard 15–50%, estimated assessment 25%, unclear/unreasonable circumstances 5%, qualifying voluntary post-60-day correction 2%, with statutory minimums and waiver conditions. Do not select the smallest percentage without establishing its conditions. A late earnout return has its own sanction exposure. [Act §§36–36b][law]; [Vero earnout instructions][earnout].

Late title registration can add the separate §8 surcharge even if the transfer tax was already paid. If the property was transferred more than once before title is applied for, the applicant also pays the tax, with surcharges, on earlier transfers made in the three years before the application. [Act §§8–9][law]. Overdue tax also bears interest, **9.5% for days in 2026**, from the day after the payment deadline through payment. Do not use that rate for 2027 without confirming the annual rate. [Act §§8,28][law]; [Vero late-payment guidance][late].

## Cross-border points

Residence abroad does not remove tax on Finnish real estate or domestic property-company shares. The ordinary securities exemption where neither party is Finnish resident or a qualifying §16(1) branch does **not** extend to the property-company categories specified in §16(3). For foreign-issued securities, §18(2) requires **both** (1) the issuer's actual activity mainly comprises direct/indirect ownership or management of real estate and (2) more than 50% of its total assets consist of directly/indirectly held Finnish immovable property. At least one transfer party must also be Finnish resident or a **qualifying branch listed in §16(1)**. Either party can satisfy that residence/branch test; an arbitrary Finnish business branch is not sufficient. Establish the issuer's activity, asset values/property chain and both parties' status before taxing foreign shares. [Act §§16,18][law].

The buyer has the ordinary filing/payment duty. Section 23 adds responsibility for the party required to collect tax, an intermediary real-estate agent and the specified company; it does not create a buyer withholding rule merely because the seller is foreign. In the ordinary securities case governed by §16(2), the **seller** must collect from the specified nonresident buyer unless the buyer has paid voluntarily. Read that rule together with the property-share exception in §16(3), rather than applying it indiscriminately to housing shares. Foreign buyers obtain the Finnish identifier/reference and file/pay under Vero's process. The seller's income tax on the disposal is separate. [Act §§16,21,23,30][law]; [Vero corporate-stock guidance][stock]; [individual cross-border](fi-individual-cross-border-residence.md).

## Two worked examples that recompute

### 1. Housing shares and the debt-free base

Assume cash consideration EUR 180,000, allocated unpaid company debt EUR 60,000, no other consideration and no exemption. The base is EUR 240,000, giving EUR 3,600 tax. Cash-only tax would omit EUR 900.

```oa-check
name: Finland housing share debt free price
inputs:
  cash_consideration: 180000
  allocated_company_debt: 60000
  transfer_tax_rate: 0.015
steps:
  established_base: cash_consideration + allocated_company_debt
  transfer_tax: established_base * transfer_tax_rate
  cash_only_tax: cash_consideration * transfer_tax_rate
  omitted_tax: transfer_tax - cash_only_tax
expected:
  established_base: 240000
  transfer_tax: 3600
  cash_only_tax: 2700
  omitted_tax: 900
```

### 2. Later contingent consideration

Assume a February 2026 direct-property contract, EUR 250,000 original taxable consideration and EUR 50,000 earnout whose obligation and amount become confirmed in November, after the original deadline. Tax on the original base is EUR 7,500; additional tax EUR 1,500, total EUR 9,000. File the correction and pay the additional tax within two months of confirmation. No exemption applies.

```oa-check
name: Finland contingent real estate consideration tax
inputs:
  original_consideration: 250000
  later_confirmed_consideration: 50000
  rate: 0.03
steps:
  original_tax: original_consideration * rate
  additional_tax: later_confirmed_consideration * rate
  combined_tax: original_tax + additional_tax
expected:
  original_tax: 7500
  additional_tax: 1500
  combined_tax: 9000
```

## Ask the client first

- What asset, issuer, property chain and ownership fraction are acquired?
- What are the contract, final signature, completion and ownership-transfer dates?
- What cash, noncash consideration, allocated company debt and contingent terms exist?
- What are both parties' residence and any Finnish branch facts?
- Is there an agent, registration application or claimed statutory exemption?
- Which returns, payments, corrections and certificates already exist?

## Sources

| Official source | Scope | Read date |
|---|---|---|
| [Transfer Tax Act 931/1996][law] | §§4–9,15–23,27,30–31,36–36b,40; current 2026 wording and 1143/2025 transition | 2026-10-26 |
| [Vero overview][overview] | Rates and first-home transition | 2026-10-26 |
| [Vero filing instructions][filing] and [deadline table][deadlines] | Transaction clocks, identifiers, signatures and returns | 2026-10-26 |
| [Vero earnout instructions][earnout] | 2026 contingent-consideration return correction | 2026-10-26 |
| [Vero correction procedure][corrections] | Replacement versus payment/refund | 2026-10-26 |
| [Vero corporate-stock guidance][stock] | Nonresident transaction classification | 2026-10-23 |
| [Vero late-payment guidance][late] | Interest and sanctions | 2026-10-26 |

Not yet confirmed: none for the ordinary acquisition computation above. Reorganisations, special fund/public-body exemptions and pre-2024 first-home claims require their own transaction-specific analysis.

[law]: https://www.finlex.fi/fi/lainsaadanto/1996/931
[overview]: https://www.vero.fi/en/individuals/property/transfer-tax/
[filing]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/
[deadlines]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/table-of-filing-and-payment-deadlines/
[earnout]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/reporting-an-earnout-price/
[corrections]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/errors-in-return-or-payment/
[stock]: https://www.vero.fi/en/individuals/property/transfer-tax/corporate-stock/
[late]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/if-your-transfer-tax-return-or-your-payment-is-overdue/

> Contributed by Michael Cutajar.

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
