---
name: il-customs-duty
description: Use this skill when calculating Israeli customs duty, VAT, and purchase tax on imports, or advising on free trade agreement preferences. Trigger on phrases like "import tax Israel", "customs duty Israel", "מכס", "mas kniya", "מס קנייה", "personal import Israel", "Amazon import Israel", "AliExpress import Israel", "Shaar Olami", "שער עולמי", "HS code Israel", "EUR.1 Israel", "FTA Israel", "landed cost Israel", or any Israeli customs and import duty query. ALWAYS read this skill before advising on Israeli import duties.
version: 1.0
jurisdiction: IL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Customs Duty

## Israel Customs and Import Duty Skill v1.0

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Israel (מדינת ישראל) |
| Scope | Customs duty, VAT, and purchase tax on imports |
| Currency | NIS (Israeli New Shekel — ₪) |
| VAT rate | 18% (effective January 2025) |
| Personal import threshold | USD 75 (as of May 2026 — verify before use) |
| Tariff lookup | Shaar Olami — https://shaarolami-query.customs.mof.gov.il/CustomspilotWeb/en/CustomsBook/Import/Doubt |
| Official calculator | https://www.gov.il/en/service/customs-tax-calculation-import-by-israelis |
| Exchange rates | Bank of Israel — https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/ |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed רואה חשבון or יועץ מס |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown personal import threshold | Use USD 75 — verify via official calculator |
| Unknown HS code (last 2 digits) | Do not guess — request pre-ruling from Israel Customs |
| Unknown origin of goods | Apply MFN duty rate (no FTA preference) |
| Unknown whether EUR.1 is valid | Treat as invalid — apply full duty |
| Unknown purchase tax rate | Check Shaar Olami for the specific 8-digit code |

## Section 2 — Import types

**Import types table**

| Type | Typical importer | Tax treatment |
| --- | --- | --- |
| Personal import, small parcel | Consumer ordering online | Exemption threshold applies |
| Personal import, high-value | Consumer buying jewelry, electronics | Full duty + VAT + purchase tax |
| Commercial import (B2B) | Osek Murshe importing stock | Full duty + VAT (VAT is recoverable); no threshold exemption |
| Gift | Individual sending to an Israeli | Treated as personal import, no special exemption |
| Oleh Hadash belongings | New immigrant | Separate Oleh exemption — consult the Aliyah unit |

### Courier vs postal clearance

Courier shipments (DHL, FedEx, UPS) are self-cleared by the courier, which bills the importer duty, VAT, and a handling fee. Israel Post parcels go through postal clearance: low-value items clear automatically, items above the threshold get a payment demand before delivery. The tax math is the same; fees and timelines differ.

## Section 3 — Personal import threshold

- **Personal import VAT exemption threshold** — USD 75 (cost of goods, excluding shipping and insurance)  _(As of May 2026)_

**Recent history:** The threshold was raised to USD 150 via a Smotrich decree in November 2025, then revoked by the Knesset on 24 February 2026, returning to USD 75. **Always verify the current threshold via the official calculator before quoting a number.**

**Personal import threshold tax treatment table**

| Value range | Tax treatment |
| --- | --- |
| Below USD 75 | No customs, no VAT, no purchase tax |
| USD 75 – USD 500 (approx) | VAT + purchase tax typically apply; customs duty often waived for personal imports |
| Above USD 500 | Full duty + VAT + purchase tax; commercial clearance rules apply |

- **Shipping and insurance treatment** — Shipping and insurance are excluded from the personal import threshold test but are included in CIF for commercial imports. Do not mix the two rules.

## Section 4 — HS code classification

- **HS code structure** — Israel uses the international Harmonized System at the 6-digit level plus 2 Israel-specific digits (positions 7 and 8)

1. Describe the product: material, function, packaging form, use, brand, model
2. Start from the 2- or 4-digit HS chapter (e.g., chapter 85 for electronics, chapter 61 for apparel)
3. Look up the full 8-digit code in Shaar Olami: https://shaarolami-query.customs.mof.gov.il/CustomspilotWeb/en/CustomsBook/Import/Doubt
4. **Do not guess the last 2 digits** — a US HTS code or EU CN code does NOT translate directly to the Israeli code

For certainty, request a free binding pre-ruling from Israeli Customs with a product description and catalog.

## Section 5 — Duty, VAT, and purchase tax rates

**Duty, VAT, purchase tax rates table**

| Tax | Typical range | Notes |
| --- | --- | --- |
| Customs duty | 0–12% (many goods duty-free under MFN bindings) | Varies by HS code |
| VAT | 18% standard | Applied on CIF + duty + purchase tax |
| Purchase tax (Mas Kniya — מס קנייה) | Only on specific items | Alcohol, tobacco, perfumes, some electronics, passenger cars — rates can be very high |

**Purchase tax is NOT a small rounding item.** Alcohol and tobacco can carry rates in the hundreds of percent.

## Section 6 — Landed cost calculation

The three taxes are calculated on a cascading base:

### 6.1 CIF value

- **CIF value formula** — CIF (NIS) = (product price + shipping + insurance) × USD-to-NIS rate  _(Israel Customs values goods at CIF: cost + insurance + freight.)_
- **Exchange rate to use** — Use the Bank of Israel daily rate for the clearance date.

### 6.2 Cascading tax formula

- **Cascading tax formula** — Duty            = CIF × duty rate Base after duty = CIF + duty Purchase tax    = base after duty × purchase tax rate Base for VAT    = base after duty + purchase tax VAT             = base for VAT × 0.18 Landed cost     = CIF + duty + purchase tax + VAT + broker fees + handling

### 6.3 Worked example — personal import above threshold

**Scenario:** Camera from Amazon US, USD 200 + USD 20 shipping.

**Worked example table**

| Line | Amount |
| --- | --- |
| Product price | USD 200 |
| Shipping | USD 20 |
| CIF (assuming USD/NIS 3.65) | NIS 803 |
| Customs duty (0% for digital cameras under MFN) | NIS 0 |
| Purchase tax (check HS code — typically 0% for cameras) | NIS 0 |
| VAT (18% on NIS 803) | NIS 145 |
| Broker/handling fee (typical parcel) | NIS 100–400 |
| **Estimated total landed cost** | **~NIS 1,048–1,348** |

## Section 7 — Free trade agreement (FTA) preferences

**FTA preferences table**

| Origin | Agreement | Origin proof required |
| --- | --- | --- |
| United States | US-Israel FTA (1985) | US Origin Invoice Declaration on the commercial invoice |
| European Union | EU-Israel Association Agreement | EUR.1 movement certificate, or invoice declaration under €6,000 |
| United Kingdom | UK-Israel Trade and Partnership Agreement (2019) | EUR.1 movement certificate, or invoice declaration under €6,000 |
| Canada | Modernized CIFTA (September 2019) | Form B239 certificate of origin |
| EFTA (CH, NO, IS, LI) | EFTA-Israel Free Trade Agreement | EUR.1 movement certificate |
| Mercosur (BR, AR, UY, PY) | Mercosur-Israel FTA (in force June 2010) | Mercosur-Israel certificate of origin |

A valid origin proof can eliminate the customs duty (but NOT VAT or purchase tax):

### EUR.1 requirements

- **EUR.1 signature requirement** — Must carry a wet-ink (original) signature — Israel does NOT accept electronically signed EUR.1 certificates
- **EUR.1 above €6,000** — For shipments above €6,000, an EUR.1 stamped by the origin country's customs is required
- **EUR.1 below €6,000** — For below €6,000, an invoice declaration by a non-approved exporter is sufficient
- **Approved-exporter status** — For repeat shipments, the exporter should apply for approved-exporter status so invoice declarations cover any value

Plan courier time for the original document to arrive

### Worked example — EU commercial import with EUR.1

**Scenario:** 50 Italian leather bags, CIF €12,000, HS 4202.21.xx.

**EUR.1 worked example table**

| Line | Without EUR.1 | With valid EUR.1 |
| --- | --- | --- |
| CIF | €12,000 | €12,000 |
| Duty (6–12% typical for leather bags) | €720–1,440 | €0 (waived) |
| Purchase tax | Typically 0% | 0% |
| VAT (18% on CIF + duty) | €2,290–2,419 | €2,160 |
| **Savings from EUR.1** | — | **€720–1,440 duty saved** |

Since CIF > €6,000, an EUR.1 movement certificate stamped by Italian customs is required (invoice declaration alone insufficient unless exporter holds approved-exporter status).

## Section 8 — Common errors

**Common errors table**

| Error | Consequence |
| --- | --- |
| Using US or EU HS code directly | Last 2 digits are Israel-specific — wrong code = wrong duty rate |
| Applying old personal import threshold (USD 150) | Reverted to USD 75 in February 2026 |
| Including shipping in personal threshold test | Shipping is excluded from the USD 75 test |
| Forgetting cascading tax calculation | VAT is on CIF + duty + purchase tax, not on product price alone |
| Accepting electronic EUR.1 | Israel requires wet-ink original |
| Assuming FTA removes all taxes | FTA removes duty only; VAT and purchase tax still apply |
| Underestimating purchase tax | Alcohol, tobacco, cars can have very high purchase tax rates |

## Section 9 — Tier 2 items (require professional input)

**Tier 2 items table**

| Item | Why it needs a professional |
| --- | --- |
| Binding HS classification pre-ruling | Complex product classification |
| Temporary import (ATA Carnet) | Different rules for goods temporarily entering Israel |
| Eilat free zone imports | Special zero-VAT zone rules |
| Oleh Hadash belongings exemption | Separate exemption schedule and eligibility rules |
| Anti-dumping duties | Certain goods from specific countries carry additional duties |
| Agricultural imports | Seasonal quotas and variable levies may apply |

## Section 10 — Reference material

**Reference material table**

| Resource | Reference |
| --- | --- |
| Israel Tax Authority | https://www.gov.il/en/departments/israel_tax_authority |
| Personal import calculator | https://www.gov.il/en/service/customs-tax-calculation-import-by-israelis |
| Shaar Olami tariff lookup | https://shaarolami-query.customs.mof.gov.il/CustomspilotWeb/en/CustomsBook/Import/Doubt |
| EU-Israel trade relationship | https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/israel_en |
| US-Israel FTA | https://www.trade.gov/us-israel-free-trade-agreement |
| Bank of Israel exchange rates | https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/ |
| CIFTA rules of origin | https://www.cbsa-asfc.gc.ca/publications/dm-md/d11/d11-5-6-eng.html |

## Disclaimer

> **חשוב:** כל המידע בקובץ זה מיועד למטרות מידע וחישוב בלבד. יש לבדוק כל עמדה מול רואה חשבון (Ro'eh Cheshbon) או יועץ מס (Yo'etz Mas) מוסמך לפני הגשה או פעולה.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional — such as a רואה חשבון (Ro'eh Cheshbon — CPA) or יועץ מס (Yo'etz Mas — tax advisor) licensed in Israel — before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
