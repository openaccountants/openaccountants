---
name: tm-vat-gst
description: "Turkmenistan VAT, tax year 2026, from the Tax Code: 15% and 0% (art. 103), who is a payer and who is not (privately owned legal persons are outside VAT, art. 95), zero-rated and exempt supplies, monthly periods for legal persons and half-yearly for entrepreneurs, returns by the 20th and payment by the 25th, tax agent withholding on foreign suppliers."
version: 1.1
jurisdiction: TM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Turkmenistan VAT

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file without professional review.

## Who this applies to

VAT payers are legal persons and individual entrepreneurs carrying out the taxable transactions in art. 96 (Tax Code of Turkmenistan, art. 95(1)). Art. 95(2) excludes four categories: the Central Bank; contractors and subcontractors under the Law "On Hydrocarbon Resources" (but they are payers for transactions not relating to petroleum work); **legal persons in private ownership**; and individual entrepreneurs for activity under the simplified system. The Code sets no turnover threshold: liability turns on who the person is and what it does. Taxable transactions (art. 96): supplying goods, works, services and property rights, and construction-installation work for own needs (not installing or repairing equipment), located by the place-of-supply rules in arts 98 and 99. Because the private-ownership exclusion is so wide, confirm it with a practitioner before relying on it.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate (art. 103) | 15% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Zero rate for art. 105 transactions (art. 103) | 0% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Return (art. 111(1)) | Not later than the 20th of the month after the reporting period | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Payment (art. 111(3)) | Not later than the 25th of the month after the reporting period | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Entrepreneurs and partnerships without a legal person: payment (art. 111(5)) | By 1 September for January to June; by 1 March for July to December | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |

For state-fixed prices, and where the tax authority uses a VAT-inclusive market price, the VAT is extracted at rate / (100 + rate): 15/115 at 15% (art. 103).

## The base

**Zero-rated (art. 105):** exports of own or purchased goods with confirmed crossing of the customs border, except natural and associated gas, oil and their processed products; direct exports by a resident processor of products made from crude oil and gas condensate bought from non-residents (the third paragraph applied 1 June to 31 December 2021 and was restored from publication of the law of 30 November 2024); international carriage of passengers and goods (not journeys that start and end in Turkmenistan, even if the vehicle leaves the country); producers' sales of own textiles to resident exporters with customs confirmation; export freight and handling, transit of foreign cargo, supplies to and servicing of international vessels and aircraft, duty-free sales, supplies for official use of diplomatic missions and international organisations, qualifying fund-financed supplies and sales of own agricultural produce; supplies to the Government foreign-currency reserve, the Stabilisation Fund's charitable funds and the named children's charitable fund; supplies to qualifying petroleum contractors and subcontractors for petroleum work (not other activities, not undeterminable or inseparable mixed use; the recipient notifies the supplier before invoicing).

**Exempt (art. 106(1)), examples:** public urban passenger transport (not taxis), free warranty repairs, medicines and medical equipment, veterinary and sanitary services, healthcare and dental prosthetics (non-therapeutic cosmetic services are not exempt), care of the sick, disabled and elderly, education, and insurance and reinsurance by insurers. Check each limb's conditions.

**Input VAT:** registered payers offset VAT on business purchases against output VAT (not re-read for this guide).

## Deadlines and filing

- **Periods (art. 104).** Legal persons, and partnerships with at least one legal person: tax and reporting period is the calendar month. Individual entrepreneurs, and partnerships with no legal person: tax period the calendar year, reporting periods 1 January to 30 June and 1 July to 31 December.
- **Returns and payment (art. 111).** Return by the 20th and payment by the 25th of the month after the reporting period. Entrepreneurs and partnerships without a legal person pay on the tax authority's notice (sent by 1 August and 1 February) by 1 September and 1 March.
- **Tax agents (arts 108(2), 111(2) and (4)).** A resident legal entity, a locally registered individual entrepreneur, or a foreign entity operating through a local branch, representative office or permanent establishment, buying a taxable Turkmen supply from an unregistered foreign legal entity or foreign entrepreneur, withholds VAT at payment. A supplier who shows local tax registration is not withheld from. The agent remits at the withholding deadline, or within fifteen days of it if paying abroad; if it pays after the end of the tax period in which the transaction took place, it funds the VAT itself (calculated at the transaction date, or the period end for long-term contracts) and recovers it later. The agent reports payees and amounts by the 20th of the month after payment; the foreign supplier then files no return for those transactions. If no agent can withhold, the foreign supplier registers and accounts for VAT itself.
- **Special deadlines (art. 111(6)).** The Ministry of Finance and Economy may set other deadlines for designated categories, not more than thirty days after the statutory ones.

## Penalties and interest

Not read for this guide (Tax Code general part).

## Cross-border points

Imports: VAT on imports is part of art. 96's charge; the import base and customs procedure were not re-read. Foreign suppliers: see the tax agent rule above. Exports of hydrocarbons are outside the export zero rate.

## Two worked examples that recompute

**1. Legal person (not privately owned), March 2026.** Taxable sales TMT 100,000 excluding VAT; input VAT TMT 6,000. Output VAT TMT 15,000; payable TMT 9,000; return by 20 April, payment by 25 April 2026 (derived).

```oa-check
name: Turkmenistan monthly VAT
inputs:
  sales: 100000
  input_vat: 6000
steps:
  - output_vat: sales * 0.15
  - payable: output_vat - input_vat
expected:
  output_vat: 15000
  payable: 9000
```

**2. State-fixed price TMT 11,500 including VAT.** VAT is 11,500 times 15/115 = TMT 1,500 (derived).

```oa-check
name: Turkmenistan VAT extracted from fixed price
inputs:
  price: 11500
steps:
  - vat: price * 15 / 115
expected:
  vat: 1500
```

## Ask the client first

- Legal person or entrepreneur? Ownership (state, private, foreign)?
- Any petroleum contracts, or simplified-system activity?
- Exports, international carriage, textile sales to exporters?
- Payments to foreign suppliers without Turkmen registration?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Turkmenistan, Russian text on the Mejlis site, arts 95, 103 to 106, 108 and 111 (Read for payers, rates, zero rate, exemptions, periods and dates) | https://mejlis.gov.tm/single-code/10?lang=ru | 2026-11-14 |
| Tax Code of Turkmenistan, state-language text (Read by Ryan Duguid; agrees with the Russian on these articles) | https://mejlis.gov.tm/single-code/10?lang=tm | 2026-11-11 |
| Law of 30 November 2024 amending legislative acts, parts I(2)(3) and II (Read by Ryan Duguid for restoring the processed-hydrocarbon export rule) | https://turkmenistan.gov.tm/ru/post/90313/zakon-turkmenistana-o-vnesenii-izmenenij-i-dopolneniya-v-nekotorye-zakonodatelnye-akty-turkmenistana-7 | 2026-11-11 |

Not yet confirmed: the scope of the art. 95(2) private-ownership exclusion in practice; input VAT documentation; import VAT base; category-specific Ministry deadlines; return forms; penalties. The old guide's monthly period for everyone was wrong for entrepreneurs.
