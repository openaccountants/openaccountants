---
name: eu-oss-digital
description: "Use this skill whenever a business sells digital services (electronically supplied services) B2C to consumers in other EU member states and needs to determine the correct VAT treatment. Trigger on phrases like \"OSS\", \"One-Stop-Shop\", \"MOSS\", \"Mini One-Stop-Shop\", \"digital services VAT\", \"electronically supplied services\", \"B2C cross-border EU\", \"EU VAT on digital\", \"EUR 10,000 threshold\", \"destination country VAT rate\", \"non-Union OSS\", or any request involving the VAT treatment of digital services sold to EU consumers. This skill contains the complete OSS rules, the EUR 10,000 threshold, destination VAT rate table, filing requirements, consumer location evidence rules, and the Union vs non-Union OSS distinction. ALWAYS read this skill before advising on any B2C digital services VAT question."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eu-oss-digital"
  jurisdiction: "GLOBAL"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# EU OSS Digital

## Skill Metadata

**Skill Metadata**  _(https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1)_

| Field | Value |
| --- | --- |
| Jurisdiction | EU (all 27 member states) |
| Primary Legislation | Council Directive 2006/112/EC, Articles 58, 59c (threshold), 369a-369k (Union OSS), Articles 358-369 (non-Union OSS) |
| Supporting Legislation | Council Implementing Regulation (EU) No 282/2011 (Art 7 and Annex I: ESS definitions; Art 24a-24f: consumer location); Council Implementing Regulation (EU) 2019/2026 |
| Scope | B2C sales of electronically supplied services (ESS) / digital services by EU and non-EU sellers to EU consumers |
| Key Threshold | EUR 10,000 annual cross-border B2C digital sales threshold |
| Contributor | OpenAccountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: OSS eligibility, threshold check, rate lookup, filing obligations. Tier 2: consumer location evidence, mixed supplies (digital + physical), marketplace rules. Tier 3: complex group structures, deemed supplier rules for marketplaces. |
| Cross-references | `eu-reverse-charge.md`, `eu-vat-directive.md`, country-specific VAT return skills |

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a qualified accountant.

## Step 0: Pre-Check Questions [T1]

- **Pre-check questions** — 1. Is the seller VAT-registered (or required to be registered) in an EU member state, or established outside the EU? Determines Union vs non-Union OSS. 2. Is the customer a private individual (B2C)? OSS is exclusively for B2C supplies. B2B cross-border services use the reverse charge (see eu-reverse-charge.md). 3. Is the service an "electronically supplied service" (ESS)? See Step 1 for definitions. 4. What is the total value of cross-border B2C digital sales to other EU member states in the current and preceding calendar year? Determines whether the EUR 10,000 threshold is exceeded. 5. In which EU member state is the consumer located? Determines the applicable VAT rate. If items 1-3 are unknown, STOP.

## Step 1: What Qualifies as an Electronically Supplied Service (ESS)? [T1]

- **Electronically supplied service (ESS)** — A service delivered over the internet or electronic network, the nature of which renders its supply essentially automated, involving minimal human intervention, and impossible to ensure in the absence of information technology.  _(VAT Directive Art 7(1) of Implementing Regulation 282/2011; Art 58 of the VAT Directive)_

### ESS -- YES (qualifies) [T1]

**ESS -- YES (qualifies) [T1]**

| Category | Examples |
| --- | --- |
| Software and apps | Downloads of software, apps, games, updates, add-ons, SaaS |
| Digital content | E-books, online newspapers/magazines, digital music, streaming video/audio, podcasts |
| Online courses | Pre-recorded courses, automated e-learning with no live instructor |
| Cloud services | Web hosting, cloud storage, online backup |
| Advertising | Online advertising services (banner ads, search engine ads) |
| Digital images/templates | Stock photos, website templates, design files |
| Online gaming | MMO subscriptions, in-game purchases, online gambling |

### ESS -- NO (does NOT qualify) [T1]

**ESS -- NO (does NOT qualify) [T1]**

| Category | Why Not ESS |
| --- | --- |
| Live online teaching/consulting | Significant human intervention -- this is a standard B2B/B2C service, not ESS |
| Physical goods ordered online | Physical delivery = goods, not ESS |
| Professional services via email | Email is the medium, not the service itself |
| Telephone/fax services | Telecoms, not ESS (separate rules under Art 58) |
| Physical event tickets sold online | The event is the supply, not the online sale |
| Bespoke software development | Custom work with significant human input is not automated |

## Step 2: The EUR 10,000 Threshold [T1]

- **EUR 10,000 threshold** — EUR 10,000 EUR  _(VAT Directive Art 58(2); introduced by Directive (EU) 2017/2455)_

### Rule

- **Threshold rule** — An EU-established seller whose total cross-border B2C sales of ESS (and intra-EU distance sales of goods) to consumers in OTHER EU member states do NOT exceed EUR 10,000 (or national currency equivalent) in the current AND preceding calendar year may: Charge their home country's VAT rate on all B2C digital sales to other EU countries. Report on their domestic VAT return (no OSS registration needed).  _(VAT Directive Art 58(2); introduced by Directive (EU) 2017/2455)_

### When the threshold is exceeded [T1]

- **When the threshold is exceeded** — Once the EUR 10,000 threshold is exceeded (cumulative across ALL other EU member states, not per country): The seller MUST charge the destination country's VAT rate on each sale. The seller should either: Register for OSS in their home member state (recommended), or Register for VAT in each destination member state (complex, expensive, not recommended for small businesses).  _(VAT Directive Art 58(2); introduced by Directive (EU) 2017/2455)_

### Threshold does NOT apply to [T1]

- **Threshold exclusions** — Non-EU sellers: Must always charge the destination rate (no threshold benefit). Must use the non-Union OSS or register in each member state. Sellers established in more than one EU member state: The threshold does not apply; must use OSS or register locally.  _(VAT Directive Art 58(2); introduced by Directive (EU) 2017/2455)_

## Step 3: How OSS Works [T1]

### Union OSS (for EU-established sellers)

**Union OSS (for EU-established sellers)**  _(https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1)_

| Feature | Detail |
| --- | --- |
| Who can register | Any business established in an EU member state |
| Where to register | In the member state where the business is established (Member State of Identification -- MSI) |
| What is reported | All B2C supplies of services taxable in member states where the seller is not established (not only ESS), plus intra-Community distance sales of goods, broken down by destination country and VAT rate |
| Filing frequency | Quarterly |
| Filing deadline | End of the month following the quarter (e.g., Q1 Jan-Mar: deadline 30 April) |
| Payment | Single payment to the MSI tax authority, which distributes to destination countries |
| VAT rate charged | Destination country's rate (see Step 4) |
| Input VAT recovery | NOT through OSS. Seller recovers input VAT through their domestic VAT return or via the VAT refund procedure (Directive 2008/9/EC) |

### Non-Union OSS (for non-EU sellers)

**Non-Union OSS (for non-EU sellers)**  _(https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1)_

| Feature | Detail |
| --- | --- |
| Who can register | Any business NOT established in the EU that makes B2C ESS sales to EU consumers |
| Where to register | In any EU member state of the seller's choice (MSI) |
| What is reported | All B2C services supplied to EU consumers (not only ESS), broken down by destination country and VAT rate |
| Filing frequency | Quarterly |
| Filing deadline | End of the month following the quarter |
| Payment | Single payment to the chosen MSI |
| VAT rate charged | Destination country's rate |
| Input VAT recovery | Via the special refund procedure in Directive 86/560/EEC (13th Directive), which is more restrictive |
| IMPORTANT | Non-EU sellers who do NOT register for non-Union OSS must register for VAT individually in every member state where they have consumers |

## Step 4: EU VAT Rate Table for Digital Services (ESS) [T1]

**EU VAT Rate Table for Digital Services (ESS)**  _([Rates as of April 2026. Always verify for rate changes.](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax))_

| Country | Code | Standard Rate | Reduced Rate (if applicable to ESS) | Notes |
| --- | --- | --- | --- | --- |
| Austria | AT | 20% | -- |  |
| Belgium | BE | 21% | -- |  |
| Bulgaria | BG | 20% | -- |  |
| Croatia | HR | 25% | -- |  |
| Cyprus | CY | 19% | -- |  |
| Czech Republic | CZ | 21% | -- |  |
| Denmark | DK | 25% | -- |  |
| Estonia | EE | 24% | -- | Increased from 22% on 1 July 2025 |
| Finland | FI | 25.5% | -- | Increased from 24% in 2024 |
| France | FR | 20% | 5.5% on e-books, digital press |  |
| Germany | DE | 19% | 7% on e-books |  |
| Greece | GR | 24% | -- |  |
| Hungary | HU | 27% | -- | Highest rate in EU |
| Ireland | IE | 23% | zero rate on e-books, e-newspapers; second reduced rate on e-periodicals |  |
| Italy | IT | 22% | 4% on e-books |  |
| Latvia | LV | 21% | -- |  |
| Lithuania | LT | 21% | -- |  |
| Luxembourg | LU | 17% | 3% on e-books | Lowest standard rate in EU |
| Malta | MT | 18% | -- | Lowest standard rate for general ESS |
| Netherlands | NL | 21% | -- |  |
| Poland | PL | 23% | -- |  |
| Portugal | PT | 23% | 6% on e-books |  |
| Romania | RO | 21% | 11% on e-books, e-newspapers |  |
| Slovakia | SK | 23% | -- |  |
| Slovenia | SI | 22% | -- |  |
| Spain | ES | 21% | 4% on e-books |  |
| Sweden | SE | 25% | 6% on e-books |  |

### Key observations:

- Rates range from 17% (Luxembourg) to 27% (Hungary).
- **E-books and digital press** enjoy reduced rates in many countries (FR 5.5%, DE 7%, IT 4%, ES 4%, SE 6%).
- Standard digital services (software, SaaS, streaming, cloud) are charged at the standard rate in virtually all countries.

## Step 5: Determining the Consumer's Location [T1]

- **Consumer location evidence requirement** — The seller must collect two pieces of non-contradictory evidence to determine the consumer's country.  _(Implementing Regulation 282/2011, Articles 24b-24f)_

### Acceptable Evidence [T1]

**Acceptable Evidence [T1]**

| Evidence Type | Example |
| --- | --- |
| Billing address | Address on file / payment instrument |
| IP address geolocation | Country determined by IP address |
| Bank details | Country of the bank issuing the payment card |
| SIM card country code | Mobile country code for mobile purchases |
| Location of the consumer's fixed land line | If payment made via fixed line |
| Other commercially relevant information | Delivery preferences, language settings, contract details |

### Rules [T1]

- **Consumer location rules** — 1. Two items of non-contradictory evidence are required. If two items point to the same country, that is the consumer's country. 2. If evidence is contradictory (e.g., IP address says Germany, billing address says France): use the billing address as the default, unless there is reason to believe it is incorrect. [T2] 3. Where these supplies from an establishment in a member state do not exceed EUR 100,000 in the current and the preceding calendar year, the seller may rely on one item of evidence listed in points (a) to (e) of Art 24f (e.g. billing address, IP address, bank details) provided by a person involved in the supply other than the seller or the customer. 4. Sellers must retain evidence records for 10 years from the end of the year of the transaction.  _([Implementing Regulation 282/2011, Articles 24b-24f](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1))_

## Step 6: Filing the OSS Return [T1]

### Quarterly Periods and Deadlines

**Quarterly Periods and Deadlines**

| Quarter | Period | Filing + Payment Deadline |
| --- | --- | --- |
| Q1 | 1 January -- 31 March | 30 April |
| Q2 | 1 April -- 30 June | 31 July |
| Q3 | 1 July -- 30 September | 31 October |
| Q4 | 1 October -- 31 December | 31 January (following year) |

### What to Include on the OSS Return [T1]

- **What to include on the OSS return** — For each member state of consumption: 1. Standard rate applicable 2. Total taxable amount at that rate 3. Total VAT at that rate 4. Reduced rate applicable (if any) 5. Total taxable amount at reduced rate 6. Total VAT at reduced rate

### Nil Returns [T1]

- **Nil returns** — If no B2C ESS sales were made in the quarter, a nil return MUST still be filed. If reminders are issued for three immediately preceding return periods and each return is not submitted within 10 days after the reminder, the seller is regarded as persistently failing to comply and is excluded from OSS, and from all special schemes for two years.  _(https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1)_

### Currency [T1]

- **Currency** — The OSS return is made out in EUR, but an MSI that has not adopted the euro (e.g., Sweden, Denmark, Poland) may require it in its national currency. Sales made in other currencies are converted at the ECB exchange rate published for the last day of the quarter.  _(https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1)_

### Corrections [T1]

- **Corrections** — Corrections to previous quarters are made on a subsequent quarterly return (not by amending the original), within three years of the date on which the original return was due. The correction is reported in a separate section showing the member state, period, and adjusted amounts.  _(https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1)_

## Step 7: Non-Union OSS for Non-EU Sellers [T1]

### When to Use

- **When to use non-Union OSS** — A non-EU seller (e.g., US, UK, Australian, Indian company) that sells digital services B2C to EU consumers must either: 1. Register for non-Union OSS in one EU member state of their choice, OR 2. Register for VAT individually in every member state where they have consumers.

### Popular MSI Choices for Non-EU Sellers

**Popular MSI Choices for Non-EU Sellers**

| Country | Why Chosen |
| --- | --- |
| Ireland (IE) | English-speaking, established tech ecosystem, helpful Revenue Commissioners |
| Netherlands (NL) | English-friendly, efficient Belastingdienst, Amsterdam tech hub |
| Luxembourg (LU) | Lowest standard rate (17%), but rate of MSI is irrelevant -- destination rate applies |
| Estonia (EE) | Digital-first government, e-Residency programme, simple online registration |

### Note

The choice of MSI does NOT affect the VAT rate charged. The destination country's rate always applies. The MSI choice affects only the administrative relationship (filing portal, language, customer service).

## PROHIBITIONS

- **Prohibitions** — 1. NEVER apply OSS to B2B transactions. OSS is exclusively for B2C. 2. NEVER charge the seller's home country rate on cross-border B2C digital sales when the EUR 10,000 threshold has been exceeded. 3. NEVER use OSS to recover input VAT. Input VAT recovery is handled through the domestic VAT return or refund procedure, not OSS. 4. NEVER assume that non-Union OSS registration in one country means the seller is VAT-registered in that country for all purposes. Non-Union OSS is a special scheme only. 5. NEVER skip filing a nil return. Three missed returns = potential OSS deregistration. 6. NEVER classify live, interactive human services (e.g., live teaching, live consulting calls) as electronically supplied services. 7. NEVER forget to retain consumer location evidence for 10 years.

## Edge Cases

### EC1 -- Mixed supply: digital content + physical goods [T2]

- **EC1 -- Mixed supply: digital content + physical goods** — Situation: A seller bundles an e-book (digital) with a printed workbook (physical goods) sold as a single package to an EU consumer. Resolution: If the supply is a single composite supply, the principal element determines the VAT treatment. If the digital element is ancillary, standard distance selling rules for goods apply (not OSS for ESS). If they are independent supplies, each is treated separately. Flag for reviewer.

### EC2 -- Live-streamed course vs pre-recorded course [T2]

- **EC2 -- Live-streamed course vs pre-recorded course** — Situation: A course is both live-streamed (with a live instructor answering questions in real time) AND recorded for later viewing. Resolution: The live element involves significant human intervention and is NOT an ESS. The pre-recorded element IS an ESS. If sold separately, each has its own treatment. If sold as a bundle, the principal element determines classification. Flag for reviewer.

### EC3 -- Marketplace / platform as deemed supplier [T3]

- **EC3 -- Marketplace / platform as deemed supplier** — Situation: A freelancer sells digital products through a marketplace (e.g., app store, online platform). The platform collects payment from the consumer. Resolution: Under Art 9a of Implementing Regulation 282/2011, the platform may be the "deemed supplier" and responsible for collecting and remitting VAT. The freelancer's supply to the platform is then treated as B2B (no VAT, reverse charge). The platform handles OSS. Escalate to determine whether the platform is a deemed supplier.  _(Art 9a of Implementing Regulation 282/2011)_

### EC4 -- UK post-Brexit [T1]

- **EC4 -- UK post-Brexit** — Situation: A UK seller sells digital services to EU consumers after Brexit. Resolution: The UK is not an EU member state. The seller must use non-Union OSS (register in one EU member state) or register for VAT in each EU member state where they have consumers. The EUR 10,000 threshold does NOT apply to non-EU sellers.

### EC5 -- Customer claims to be a business but has no VAT number [T2]

- **EC5 -- Customer claims to be a business but has no VAT number** — Situation: A customer says they are a business but cannot provide a valid VAT identification number verifiable via VIES. Resolution: Without a valid VAT number, the supply must be treated as B2C. Charge the destination country's VAT rate via OSS. If the customer later provides a valid VAT number, the seller may issue a credit note and re-invoice under reverse charge.

## Test Suite

### Test 1 -- Below threshold, EU seller

Input: German sole trader sells EUR 8,000 of digital courses (pre-recorded) to consumers across 5 EU countries in the year. Prior year was EUR 6,000. Expected: Below EUR 10,000 threshold in both current and prior year. Seller MAY charge German 19% VAT on all sales and report on domestic German VAT return. OSS registration is optional.

### Test 2 -- Above threshold, EU seller

Input: Same German sole trader now has EUR 12,000 in cross-border B2C digital sales in the year. One sale of EUR 500 is to a French consumer. Expected: Threshold exceeded. Must charge destination rate. French sale: 20% VAT = EUR 100. Register for Union OSS in Germany. File quarterly OSS return.

### Test 3 -- Non-EU seller (US company)

Input: US SaaS company sells EUR 50,000 of software subscriptions to EU consumers across 10 countries. Expected: Non-Union OSS required (or individual registrations). No EUR 10,000 threshold benefit. Register in one EU member state (e.g., Ireland). Charge destination country rate for each sale. File quarterly.

### Test 4 -- E-book to France (reduced rate)

Input: Italian seller sells an e-book for EUR 15 to a French consumer via OSS. Expected: France reduced rate for e-books = 5.5%. VAT = EUR 0.83. Report on OSS return under France, reduced rate.

### Test 5 -- Live online consulting (NOT ESS)

Input: Maltese consultant provides a 1-hour live Zoom consultation to a German consumer for EUR 200. No automation, fully interactive. Expected: This is NOT an electronically supplied service. OSS for ESS does NOT apply. Standard B2C service rules apply: place of supply = Malta (Art 45, seller's country), charge Maltese VAT at 18% = EUR 36. Report on Maltese domestic VAT return.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. VAT rates and thresholds are subject to change. Always verify current rates before filing. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

If you would like a licensed accountant to review your VAT position, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eu-oss-digital` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eu-oss-digital. If neither is available, confirm every figure against the official source pages cited above before relying on it.
