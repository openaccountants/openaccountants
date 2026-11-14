---
name: hk-vat-gst
description: "Use this skill when asked about VAT, GST or sales tax in Hong Kong for 2026 (year of assessment 2026/27). Hong Kong has no VAT, GST or general sales tax, so there is no registration, return or reverse charge. It names the indirect charges that do exist and are often mistaken for VAT (hotel accommodation tax at 3% since 1 January 2025, stamp duty on Hong Kong stock at 0.1% for each of buyer and seller, property stamp duty) and how foreign businesses selling into Hong Kong should treat invoices. Built from the law, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hk-vat-gst"
  jurisdiction: "HK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Hong Kong: no VAT, no GST, no sales tax (2026)

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Hong Kong.

## Who this applies to

Anyone selling goods or services in or into Hong Kong, or buying from Hong Kong, who asks whether VAT, GST or sales tax applies. **Hong Kong has no value-added tax, goods and services tax or general sales tax.** There is therefore no VAT or GST registration, no registration threshold, no return filing and no reverse-charge mechanism on cross-border services. The taxes the Inland Revenue Department administers are profits tax, salaries tax, property tax, stamp duty, estate duty (abolished for deaths from 11 February 2006), betting duty, business registration fees and hotel accommodation tax. A limited number of indirect duties exist (stamp duty; excise duties on tobacco, liquor and fuel under the Customs and Excise Department), but none is a consumption VAT.

Mainland China VAT is a separate system: use `cn-vat`. Profits tax: `hk-corporate-income-tax`. Wider overview: `hong-kong-tax`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| VAT, GST or general sales tax | None | Not among the taxes the IRD administers; no registration threshold or return | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Hotel accommodation tax (HAT) | 3% of accommodation charges | Hotels and guesthouses; resumed from 1 January 2025 (0% from 1 July 2008 to 31 December 2024) | same |
| Stamp duty on Hong Kong stock | 0.1% of the consideration, paid by each of buyer and seller | Contract notes, from 17 November 2023 | same |
| Stamp duty on immovable property, up to HKD 4,000,000 | HKD 100 | From 26 February 2025; on the higher of price and market value | same |
| Stamp duty on immovable property, top band | 4.25% | Price above HKD 20,000,000; intermediate bands 1.5% to 3.75% with marginal relief | same |

## The base

There is no VAT base. For a seller:

1. **Do not charge VAT or GST** on invoices to Hong Kong customers; no Hong Kong VAT number exists.
2. **Foreign sellers** (for example an EU or UK business invoicing a Hong Kong customer) apply their own country's place-of-supply rules; Hong Kong adds no VAT on import of services or goods.
3. **Hotels and guesthouses** charge HAT at 3% on accommodation charges from 1 January 2025 and account for it to the Collector.
4. **Share and property transactions** bear stamp duty on the instrument (rates table; detail in `hong-kong-tax`).
5. **Excise goods** (tobacco, liquor above the threshold, hydrocarbon oil, methyl alcohol) bear duty under the Dutiable Commodities Ordinance; rates are not restated here.

## Deadlines and filing

No VAT returns exist. HAT returns are filed with the Collector by hotels and guesthouses for each period; stamp duty is paid when the instrument is stamped (time limits under the Stamp Duty Ordinance, Cap. 117). Profits tax filing: `hk-corporate-income-tax`.

## Penalties and interest

No VAT penalties exist. Late stamping of a chargeable instrument attracts penalties under Cap. 117 (rates not restated here; see Not yet confirmed).

## Cross-border points

- An EU, UK or other VAT-registered business buying services from a Hong Kong supplier usually self-accounts for its own VAT under its home reverse charge; the Hong Kong invoice carries no VAT.
- Goods imported into Hong Kong bear no import VAT or GST (Hong Kong is a free port); only dutiable commodities pay excise.
- Mainland China VAT applies to supplies in the Mainland, including cross-border sales from Hong Kong to Mainland buyers where Mainland rules make the buyer withhold: see `cn-vat`.

## Two worked examples that recompute

**Example 1: a UK consultant invoices a Hong Kong company HKD 200,000.** Hong Kong VAT: none. Hong Kong adds 0% to the invoice; the total payable is HKD 200,000 (the UK side follows UK place-of-supply rules).

```oa-check
name: HK 2026 service invoice, no VAT
inputs:
  fee: 200000
  hk_vat_rate: 0
steps:
  - hk_vat: fee * hk_vat_rate
  - total: fee + hk_vat
expected:
  hk_vat: 0
  total: 200000
```

**Example 2: hotel bill and share purchase, the two charges that look like VAT.** A guest pays HKD 10,000 of accommodation charges in 2026: HAT 3% = HKD 300. An investor buys Hong Kong shares for HKD 1,000,000: buyer's stamp duty 0.1% = HKD 1,000, and the seller pays another HKD 1,000. Total duty on the share deal: HKD 2,000.

```oa-check
name: HK 2026 HAT and stock stamp duty
inputs:
  room: 10000
  shares: 1000000
steps:
  - hat: room * 0.03
  - buyer_duty: shares * 0.001
  - total_stock_duty: buyer_duty * 2
expected:
  hat: 300
  buyer_duty: 1000
  total_stock_duty: 2000
```

## Ask the client first

1. Is the supply in Hong Kong, or into the Mainland (then `cn-vat`)?
2. Is the client a hotel or guesthouse (HAT)?
3. Does the deal involve Hong Kong shares or immovable property (stamp duty)?
4. Are dutiable commodities involved (excise)?
5. Which country's VAT rules apply on the other side of the transaction?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for the list of taxes administered, estate duty abolition from 11 February 2006, HAT at 3% from 1 January 2025, stamp duty on stock (0.1% each side) and property stamp duty bands | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, hotel accommodation tax page. Read for HAT returns; note that this page still shows the 0% waiver text, which the 2025/26 brief guide supersedes | https://www.ird.gov.hk/eng/tax/hat.htm | 2026-11-14 |

Not yet confirmed: stamp duty late-stamping penalty rates (Cap. 117 not opened as text); excise duty rates (Customs and Excise Department pages not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hk-vat-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hk-vat-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
