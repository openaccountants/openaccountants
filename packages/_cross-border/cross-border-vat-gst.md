---
name: cross-border-vat-gst
description: "VAT, GST, and sales tax compliance for international digital businesses. Use when the user asks about: VAT, GST, sales tax, value added tax, goods and services tax, EU VAT, UK VAT, VAT OSS, One-Stop Shop, VAT registration, reverse charge, Merchant of Record, Paddle, Lemon Squeezy, Stripe Tax, digital services tax, DST, IOSS, Import One-Stop Shop, B2C digital VAT, B2B reverse charge, VIES validation, Australia GST, Singapore GST, Japan JCT, consumption tax, Canada GST/HST, US sales tax, economic nexus, SaaS tax, digital product tax, VAT compliance, VAT threshold, EU B2C sales, cross-border VAT, international VAT, when to register for VAT, VAT penalties, late registration, Mehrwertsteuer, TVA, IVA, 消費税, or any question about indirect tax compliance for businesses selling digital products or services internationally."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross Border VAT GST

## Cross-Border VAT/GST Compliance — International Digital Businesses

> **Based on work by [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise)**, licensed under MIT. Adapted for the OpenAccountants format.

> **Disclaimer:** This skill provides general guidance on VAT/GST compliance for digital services. VAT rules are complex, jurisdiction-specific, and change frequently. Consult a qualified indirect tax advisor before registering, filing, or taking positions on VAT/GST obligations. Errors can result in retroactive assessments, penalties, and interest.

## Core Decision: Do You Need to Collect Tax from Customers?

The answer depends on three factors:

1. **WHERE** is the customer located?
2. **WHAT** are you selling (digital product, SaaS, physical goods, consulting)?
3. **HOW MUCH** do you sell into that jurisdiction?

## Compliance Strategy by Revenue Level

**Compliance Strategy by Revenue Level**

| Revenue Level | Recommendation | Estimated Cost |
| --- | --- | --- |
| <€10,000 from any single jurisdiction | Monitor only — below most thresholds | $0 |
| €10,000–€100,000 with global customers | Use a Merchant of Record (Paddle, Lemon Squeezy) — they handle all tax | 5–10% of revenue |
| >€100,000 with concentrated markets | Self-register in top 2–3 markets + Stripe Tax for automation | $2,000–5,000/year in accounting |

### Merchant of Record (MoR) Decision Framework

**Merchant of Record (MoR) Decision Framework**

| Revenue | Complexity Tolerance | Recommendation |
| --- | --- | --- |
| <$50,000 | Any | MoR (Paddle / Lemon Squeezy) |
| $50,000–$200,000 | Low | MoR |
| $50,000–$200,000 | High | Self-register top markets + Stripe Tax |
| >$200,000 | Any | Self-register + accountant + Stripe Tax |

**MoR services (Paddle, Lemon Squeezy, FastSpring)** act as the legal seller:
- They collect VAT/GST from customers
- They file and remit VAT to each country
- You receive net payment
- Cost: 5–10% of revenue (includes payment processing)

## EU VAT (Value Added Tax)

### When It Applies

- **EU VAT applicability** — Selling digital products/services (SaaS, ebooks, courses, software) to EU consumers (B2C); applies regardless of where YOUR company is registered
- **EU B2C VAT registration threshold** — €10,000/year EUR/year (total EU B2C sales → must register)

### EU VAT Rates (Digital Services)

**EU VAT Rates (Digital Services)**

| Country | Standard Rate |
| --- | --- |
| Germany | 19% |
| France | 20% |
| Netherlands | 21% |
| Spain | 21% |
| Italy | 22% |
| Ireland | 23% |
| Sweden | 25% |

### VAT OSS (One-Stop Shop)

- **VAT OSS mechanics** — Register in ONE EU country → report all EU B2C sales through one portal; no need to register in each country separately; available to non-EU businesses via "Non-Union OSS" scheme; file quarterly returns

### B2B Sales to EU

- **B2B reverse charge and VIES validation** — If the EU customer provides a valid VAT number → reverse charge (0% VAT; customer self-assesses). Always validate EU VAT numbers via VIES system before zero-rating.  _(https://ec.europa.eu/taxation_customs/vies/)_

## UK VAT

### When It Applies

- **UK VAT applicability and threshold** — Selling digital services to UK consumers (B2C). No threshold for non-UK businesses — must register from first sale. UK businesses: £90,000 threshold.

### UK VAT Rate

- **UK VAT standard rate** — 20% % (standard rate)

## US Sales Tax

### When It Applies

- **US sales tax nexus rules** — Selling to US customers (digital or physical). "Nexus" required: physical presence OR economic nexus. Economic nexus: most states trigger at $100,000 in sales OR 200 transactions/year.

### Key Facts

US has NO federal sales tax — it is state-by-state (45 states + DC)
Digital products/SaaS taxability varies by state:
- **Taxable in:** TX, NY, PA, WA, and ~20 others
- **Not taxable in:** CA (SaaS), GA, MO, and others
If you have no US nexus: you may not need to collect (rules evolving)

### Solutions

**Solutions**

| Tool | Cost | Detail |
| --- | --- | --- |
| Stripe Tax | $0.50/transaction | Automatic calculation and collection |
| TaxJar / Avalara | Varies | Full compliance automation |
| Paddle / Lemon Squeezy | 5–10% of revenue | MoR handles everything |

## Australia GST

**Australia GST**

| Factor | Detail |
| --- | --- |
| Trigger | Selling digital services to Australian consumers (B2C) |
| Threshold | AUD 75,000/year in Australian sales |
| Rate | **10%** on digital supplies |
| Filing | Quarterly BAS (Business Activity Statement) |
| Non-resident suppliers | Must register for GST if above threshold |

## Singapore GST

**Singapore GST**

| Factor | Detail |
| --- | --- |
| Trigger | Taxable turnover >SGD 1,000,000/year (mandatory); voluntary registration available |
| Non-resident digital services | Must register if >SGD 100,000 in SG consumer sales |
| Rate | **9%** (increased from 8% in 2024) |
| Filing | Quarterly |

## Japan Consumption Tax (JCT — 消費税)

**Japan Consumption Tax (JCT — 消費税)**

| Factor | Detail |
| --- | --- |
| Trigger | Foreign businesses selling digital services to Japanese consumers |
| Threshold | Must register regardless of revenue threshold |
| Rate | **10%** (8% reduced rate for some items) |

## New Zealand GST

**New Zealand GST**

| Factor | Detail |
| --- | --- |
| Trigger | Non-resident suppliers of digital services to NZ consumers |
| Threshold | NZD 60,000/year in NZ sales |
| Rate | **15%** |

## Canada GST/HST

**Canada GST/HST**

| Factor | Detail |
| --- | --- |
| Trigger | Non-resident suppliers selling digital services to Canadian consumers |
| Threshold | CAD 30,000/year in Canadian sales |
| Rate | 5% GST (federal) + 0–10% provincial (HST combined up to 15%) |
| Registration | Simplified registration available for non-residents |

## Filing Deadlines Summary

**Filing Deadlines Summary**

| Jurisdiction | Filing Frequency | Typical Deadline |
| --- | --- | --- |
| EU VAT OSS | Quarterly | End of month after quarter |
| UK VAT | Quarterly | 1 month + 7 days after period |
| Australia GST | Quarterly | 28 days after quarter |
| Singapore GST | Quarterly | 1 month after quarter |
| Japan JCT | Annually or semi-annually | 2 months after fiscal year end |
| Canada GST/HST | Annually or quarterly | Varies by reporting period |
| US Sales Tax | Varies by state | Monthly / quarterly / annually |

## Digital Services Tax (DST) — NOT the Same as VAT

- **DST definition** — DST is a revenue-based tax on digital services. Unlike VAT (transaction-level, charged to customers) and corporate tax (profit-based), DST is calculated on gross revenue and comes out of your own revenue.

### DST Rates and Thresholds

**DST Rates and Thresholds**

| Country | DST Rate | Global Revenue Threshold | Local Revenue Threshold |
| --- | --- | --- | --- |
| UK | 2% | £500M global | £25M UK |
| France | 3% | €750M global | €25M France |
| Italy | 3% | €750M global | €5.5M Italy |
| Spain | 3% | €750M global | €3M Spain |
| Turkey | 7.5% | €750M global | TRY 20M Turkey |
| India (Equalization Levy) | 2% | **No threshold** | ₹2 crore (~$240K) |
| Kenya | 1.5% | **No threshold** | KES 0 (all digital services) |

**For most small businesses:** The high global revenue thresholds in Europe (£500M, €750M) make DST irrelevant.

**Exceptions — India and Kenya have NO global revenue threshold:**
- **India Equalization Levy:** 2% on gross consideration for non-resident e-commerce operators selling digital services to Indian customers. Must register and file quarterly.
- **Kenya Digital Service Tax:** 1.5% on gross transaction value. No minimum threshold.

**Your India/Kenya Revenue action table**

| Your India/Kenya Revenue | Action |
| --- | --- |
| <$10,000/year | Monitor; enforcement limited at this scale |
| $10,000–$50,000/year | Consult tax advisor; weigh registration cost vs exposure |
| >$50,000/year | Register and comply; enforcement risk is real |

## Penalties and Remediation

### Late Registration Penalties

- **EU late registration penalty structure** — Most EU countries impose penalties for selling above the €10,000 threshold without registration: - **Minimum penalty:** ~€500 (small/first-time violation) - **Maximum penalty:** ~5% of unpaid VAT (sustained non-compliance) - Interest accrues from the date VAT was originally due

### Voluntary Disclosure Programs

**Voluntary Disclosure Programs**

| Jurisdiction | Program | Penalty Reduction |
| --- | --- | --- |
| EU (most countries) | Voluntary correction | 50–75% reduction |
| UK | Unprompted disclosure to HMRC | Best terms (~30% of maximum) |
| Australia | Voluntary disclosure | Significant reduction; no penalty if minor |
| US | Voluntary Disclosure Programs (VDP) | Varies by state; generally 50%+ reduction |

**"Unprompted" means you contact the authority before they contact you.** Once an audit begins, voluntary disclosure terms are lost.

### Remediation Steps

1. Stop selling into the affected jurisdiction until registered (or switch to MoR immediately)
2. Calculate total VAT owed retroactively from the date the threshold was crossed
3. File voluntary disclosure with the relevant tax authority
4. Pay outstanding VAT + reduced penalty + accrued interest
5. Register going forward through standard process

### When to Get Professional Help

- **Professional help exposure threshold** — €5,000 EUR (If total exposure exceeds this or involves multiple countries, hire a VAT specialist. Typical remediation cost: €500–2,000 per engagement.)

## Physical Goods — Key Differences from Digital Services

**Physical Goods — Key Differences from Digital Services**

| Dimension | Digital Services | Physical Goods |
| --- | --- | --- |
| Delivery | Instant, borderless | Shipping, customs clearance |
| VAT trigger | Customer location | Import entry |
| Additional taxes | DST (rare) | Customs duty, tariffs |
| Complexity | Medium | High |

### EU Physical Goods (Post-2021)

- **EU physical goods import VAT rules** — No de minimis exemption — ALL imports subject to VAT (was €22 before 2021). Customs duty threshold: €150 still applies. IOSS (Import One-Stop Shop): Lets non-EU sellers collect and remit VAT at point of sale for goods <€150. Without IOSS, carrier or customs collects VAT from buyer on delivery (poor customer experience).

### US De Minimis (Section 321)

- **US de minimis customs duty exemption** — $800 USD USD/day/importer (Shipments ≤$800 USD per day per importer: exempt from customs duty. Above $800: customs duty + potential tariffs apply. Threshold under legislative review — verify before building logistics around it.)

## Platform Income — VAT Threshold Aggregation

- **Aggregation of platform income for VAT threshold purposes** — If earning across multiple platforms (YouTube, Patreon, Substack, Gumroad), aggregate total EU digital services revenue for VAT threshold purposes: - EU VAT OSS threshold: €10,000/year across ALL EU B2C digital sales (not per platform) - Gumroad and Paddle handle VAT for their platform sales (they are MoR) - Stripe, Patreon, and AdSense do NOT handle VAT — the seller is responsible

## Official Sources & Further Reading

- **EU VAT OSS:** https://vat-one-stop-shop.ec.europa.eu
- **EU VIES VAT Number Validation:** https://ec.europa.eu/taxation_customs/vies/
- **UK HMRC — VAT for digital services:** https://www.gov.uk/guidance/vat-on-digital-services
- **Australia ATO — GST on digital supplies:** https://www.ato.gov.au/Business/International-tax-for-business/GST-on-imported-services-and-digital-products/
- **Singapore IRAS — GST for digital services:** https://www.iras.gov.sg
- **Japan NTA — JCT:** https://www.nta.go.jp
- **Canada CRA — GST/HST for non-residents:** https://www.canada.ca/en/revenue-agency.html
- **Stripe Tax:** https://stripe.com/tax
- **Paddle:** https://www.paddle.com
- **Lemon Squeezy:** https://www.lemonsqueezy.com

## closing-notes

*Data reflects 2024–2026 rules. VAT/GST thresholds, rates, and registration requirements change frequently. Verify all figures with official sources and a qualified indirect tax advisor.*
*Original content: [Artin (@ar-gen-tin)](https://github.com/ar-gen-tin/panrise) — MIT License.*
*OpenAccountants — open-source accounting skills for AI — info@openaaccountants.com*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
