---
name: global-marketplaces-banking-fees
description: "Pattern library for online marketplaces (Etsy, eBay, Amazon Seller, AliExpress, Mercari, Depop, Vinted, Fiverr, Upwork, Toptal, Catalant, Andela, Patreon, Substack, Gumroad, Lemonsqueezy, Beehiiv, Whop) and recurring bank / payment-platform fees (wire fees, currency conversion, FX spreads, ATM fees, monthly account fees, overdraft, returned cheque). Provides bank-statement variations, classification, VAT/GST treatment, marketplace facilitator collection rules (post-Wayfair US states; EU marketplace deemed-supplier; UK platform reporting under DAC7-equivalent), and the 1099-K threshold reduction for US sellers (USD 5,000 for 2024, USD 600 for 2026 per OBBBA confirmation). Does NOT cover: cloud (see global-cloud-infrastructure), productivity SaaS (see global-productivity-tools), ad platforms (see global-ad-platforms), payment processors (see global-payment-processors)."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: pattern
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Global Marketplaces Banking Fees

## Global Marketplaces & Banking Fees Pattern v0.1

## Section 1 — Marketplaces (seller-side classification)

For a freelancer or e-commerce seller, marketplace transactions involve gross sales, fees, and platform-collected sales tax / VAT. Bank statements show only the net deposit.

### 1.1 Marketplace fee patterns

**Marketplace fee patterns**

placeholder

**Marketplace fee patterns table**  _(1.1 Marketplace fee patterns)_

| Marketplace | Bank statement variations | Fee structure | VAT/GST notes |
| --- | --- | --- | --- |
| **Etsy** | `ETSY.COM`, `ETSY*PMT`, `ETSY IRELAND` | Listing fee + 6.5% transaction + 3% + USD 0.25 payment processing | Etsy Ireland for EU; collects EU OSS VAT on B2C |
| **eBay** | `EBAY INC`, `EBAY COMM PMT`, `EBAY EUROPE` | 12.9% + USD 0.30 (FVF); plus optional store subscription | EU marketplace deemed-supplier rules; collects VAT on imported goods ≤ EUR 150 (IOSS) |
| **Amazon Seller** | `AMAZON SELLER`, `AMAZON PAYMENTS`, `AMAZON SERVICES EUROPE`, `AMAZON MKTPLACE PMTS` | Referral fee 6-45% by category; FBA fees; ad fees | Amazon collects "marketplace tax" in US states; EU/UK deemed-supplier for imports ≤ EUR/£150 |
| **AliExpress** | `ALIEXPRESS.COM`, `ALIBABA.COM` | n/a (buyer-side) | Buyer-side patterns mostly |
| **Mercari** | `MERCARI.COM` | 10% selling fee + payment processing | US / Japan operations |
| **Depop** | `DEPOP LTD` | 10% + payment fee | Etsy subsidiary |
| **Vinted** | `VINTED UAB`, `VINTED LTD` | Buyer-side fee (no seller fee); shipping fee | Lithuania HQ; EU marketplace |
| **Fiverr** | `FIVERR INTERNATIONAL`, `FIVERR.COM` | 20% Fiverr commission (5% of gig + 15% withhold) | Israel HQ |
| **Upwork** | `UPWORK INC`, `UPWORK GLOBAL` | 10% client fee + freelancer membership tiers | US HQ |
| **Toptal** | `TOPTAL LLC` | Variable commission | US HQ |
| **Catalant** | `CATALANT TECH` | Commission | US HQ |
| **Patreon** | `PATREON INC`, `PATREON*` | 8-12% by tier + 2.9% + USD 0.30 payment processing | US HQ |
| **Substack** | `SUBSTACK INC` | 10% + Stripe processing | US HQ |
| **Gumroad** | `GUMROAD INC` | 10% + Stripe processing | US HQ |
| **Lemon Squeezy** | `LEMON SQUEEZY`, `LEMONSQUEEZY` | 5% + USD 0.50 + Stripe; collects sales tax for sellers | Acquired by Stripe 2024 |
| **Beehiiv** | `BEEHIIV INC` | Tiered subscription + ad share | US HQ |
| **Whop** | `WHOP INC` | Commission on digital products | US HQ |
| **OnlyFans** | `OF*ONLYFANS`, `FENIX INTL LTD` | 20% platform fee | UK HQ (Fenix International) |
| **Twitch** | `TWITCH INTERACTIVE` | Revenue share with Amazon | Amazon subsidiary |
| **YouTube Creator** | `GOOGLE *YOUTUBE`, `GOOGLE PAYMENTS` | Ad share + Super Chat etc. | Google Ireland for EU |

### 1.2 Marketplace facilitator US sales tax

- **Marketplace facilitator collection thresholds (US states)** — Most US states (45+) require marketplaces above thresholds (typically $100k sales or 200 transactions) to collect and remit state sales tax on behalf of third-party sellers. Sellers report gross sales to marketplace but don't have independent sales tax obligation in those states for marketplace-facilitated transactions.  _([T1])_

### 1.3 EU marketplace deemed-supplier

- **EU Marketplace Deemed Supplier rules (from 1 July 2021)** — From 1 July 2021, EU Marketplace Deemed Supplier rules: - Distance sales of goods imported into EU ≤ EUR 150: marketplace deemed supplier (IOSS scheme) - B2C goods supply from a third country by a non-EU seller via marketplace: marketplace deemed supplier - Domestic B2C sales by non-EU seller via marketplace into EU consumer: marketplace deemed supplier  _([T1])_

### 1.4 Form 1099-K thresholds (US)

- **Form 1099-K reporting threshold** — Reduced under American Rescue Plan to USD 600 from 2022; transition relief delayed: - 2024: USD 5,000 threshold - 2025: USD 2,500 - 2026 onwards: USD 600 (confirmed by OBBBA P.L. 119-21 July 2025) Form 1099-K is reported by third-party settlement organisations (Stripe, PayPal, marketplaces). USD  _([T1])_

### 1.5 EU DAC7 platform reporting

- **EU DAC7 platform reporting requirement** — Council Directive (EU) 2021/514 requires reporting platforms to provide data on sellers' transactions to tax authorities. Effective 1 January 2023 for reporting 2024. Coordinates with OECD Model Rules for Reporting by Digital Platform Operators.  _([T1])_

### 1.6 UK Online Sales Tax / Platform Reporting

- **UK OECD model rules platform reporting** — UK has implemented OECD model rules from 1 January 2024 for platforms with sellers of goods, services, accommodation, transport. Platforms must report seller data to HMRC.  _([T1])_

## Section 2 — Banking and payment fees

### 2.1 Recurring fee patterns

**Recurring fee patterns table**  _(2.1 Recurring fee patterns)_

| Pattern | Bank statement variations | Default category |
| --- | --- | --- |
| **Wire fee** | `WIRE FEE`, `OUTGOING WIRE`, `INTERNATIONAL WIRE` | Bank charges / Other expenses |
| **Currency conversion fee** | `FX FEE`, `FOREIGN EXCH FEE`, `CURRENCY CONVERSION`, `0.5% INTL FEE` | Bank charges / Currency loss |
| **ATM fee** | `ATM FEE`, `OUT-OF-NETWORK ATM`, `INTERAC FEE` | Bank charges |
| **Monthly account fee** | `MONTHLY FEE`, `ACCT MAINT FEE`, `BANK ACCOUNT FEE` | Bank charges |
| **Overdraft fee** | `OVERDRAFT FEE`, `NSF FEE`, `INSUFFICIENT FUNDS` | Bank charges (note: deductibility may be restricted by purpose) |
| **Returned cheque fee** | `RETURNED CHK FEE`, `RETURNED ITEM FEE` | Bank charges |
| **PayPal sending fee** | `PAYPAL *FEE`, `PYPL FEE` | Bank charges / Payment processing |
| **Stripe transaction fee** | `STRIPE FEE`, `STRIPE *PROCESSING` | Bank charges / Payment processing |
| **Card swap / replacement** | `CARD REPLACEMENT`, `NEW CARD FEE` | Bank charges |
| **Wire receive fee** | `WIRE RECEIVED FEE`, `INTL WIRE IN FEE` | Bank charges |
| **Inactivity fee** | `INACTIVITY FEE`, `DORMANT ACCOUNT FEE` | Bank charges |
| **Foreign transaction fee (card)** | `FOREIGN TRANSACTION FEE`, `3% FX` | Bank charges / Currency loss |
| **SWIFT fee** | `SWIFT FEE`, `SWIFT MSG FEE` | Bank charges |
| **Verified by Visa** | `VBV FEE` | Bank charges |

### 2.2 Currency conversion accounting

- **Currency conversion accounting treatment** — Multi-currency transactions create FX gain/loss: - IFRS: IAS 21 — settle at spot rate at transaction; revalue monetary items at closing rate - US GAAP: ASC 830 — same principle Bank-imposed FX spreads (e.g., 0.5% above interbank) are typically classified as bank charges, not FX loss. Strict accountants reclassify as a finance cost.  _([T1])_

### 2.3 VAT on bank fees

- **VAT exemption on bank fees** — Most bank fees are exempt from VAT under "financial services" exemption (Article 135 PVD; IRC ITA s.135; etc.). Specific advisory or non-financial services from a bank may be taxable.  _([T1])_

## Self-checks

- [ ] Marketplace gross sales vs net deposit reconciled
- [ ] Marketplace fees recognised as expense
- [ ] Marketplace facilitator sales tax recognised (US states)
- [ ] EU OSS / IOSS / deemed-supplier treatment confirmed where applicable
- [ ] 1099-K reconciled to actual gross sales (US sellers)
- [ ] DAC7 platform data cross-referenced (EU sellers)
- [ ] Bank fees classified consistently
- [ ] FX gain/loss separated from bank fee
- [ ] Output flags every unusual line for reviewer

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
