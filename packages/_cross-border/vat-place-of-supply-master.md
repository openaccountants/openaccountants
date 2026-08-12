---
name: vat-place-of-supply-master
description: "The definitive place-of-supply reference for cross-border VAT on services and goods. Use when the user asks about: place of supply, where is VAT due, which country's VAT, Art 44, Art 45, B2B place of supply, B2C place of supply, immovable property VAT, transport VAT, electronically supplied services place of supply, distance selling, chain transactions, triangulation, OSS decision tree, IOSS, intra-EU supply, import VAT, Art 47, Art 48, Art 53, Art 55, Art 56, Art 58, Art 31, Art 32, Art 33, Art 36a, US sales tax nexus, Australian GST on imports, India OIDAR, Japan consumption tax, freelancer cross-border VAT, \"where do I charge VAT\", or any question about determining the correct country for VAT/GST on a cross-border transaction."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# VAT Place Of Supply Master

## VAT Place of Supply — Master Reference for Cross-Border Transactions

> **Disclaimer:** This skill provides general guidance on VAT/GST place-of-supply rules. These rules are complex, jurisdiction-specific, and subject to change. Consult a qualified indirect tax advisor before taking positions on VAT obligations.

## Skill Metadata

- **Jurisdiction** — EU (all 27 member states) + non-EU comparison
- **Primary Legislation** — Council Directive 2006/112/EC, Articles 31–59c
- **Supporting Legislation** — Council Implementing Regulation (EU) No 282/2011
- **Scope** — Determining the correct country for VAT on cross-border supplies of goods and services
- **Contributor** — OpenAccountants
- **Validation Date** — May 2026
- **Skill Version** — 1.0
- **Cross-references** — `eu-reverse-charge.md`, `eu-oss-digital.md`, `non-eu-export-services.md`, `cross-border-vat-gst.md`

## Section 1: General Rules for Services

**Legislation:** VAT Directive 2006/112/EC, Articles 44 and 45.

There are two basic rules. Every service starts here before checking exceptions.

### Article 44 — B2B General Rule [T1]

- **Customer** — Taxable person acting as such (business with VAT number)  _(VAT Directive 2006/112/EC, Article 44)_
- **Place of supply** — Where the **customer** is established (or has a fixed establishment receiving the service)  _(VAT Directive 2006/112/EC, Article 44)_
- **VAT consequence** — Supplier invoices without VAT; customer self-assesses under reverse charge (Art 196 within EU)  _(VAT Directive 2006/112/EC, Article 44; Article 196)_
- **Verify** — Customer's VAT number via VIES before zero-rating  _(VAT Directive 2006/112/EC, Article 44)_

### Article 45 — B2C General Rule [T1]

- **Customer** — Non-taxable person (private individual)  _(VAT Directive 2006/112/EC, Article 45)_
- **Place of supply** — Where the **supplier** is established (or has a fixed establishment from which the service is supplied)  _(VAT Directive 2006/112/EC, Article 45)_
- **VAT consequence** — Supplier charges their own country's VAT rate  _(VAT Directive 2006/112/EC, Article 45)_
- **Exception** — Numerous special rules override Art 45 for specific service types (see Section 2)  _(VAT Directive 2006/112/EC, Article 45)_

### Quick Reference

**Quick Reference**  _(VAT Directive 2006/112/EC, Articles 44-45)_

| Scenario | Place of Supply | Who Accounts for VAT |
| --- | --- | --- |
| B2B general service | Customer's country | Customer (reverse charge) |
| B2C general service | Supplier's country | Supplier |

## Section 2: Special Rules for Services

These override the general rules above. Always check whether an exception applies before defaulting to Art 44/45.

### 2.1 Immovable Property — Article 47 [T1]

- **Applies to** — Valuation, estate agency, legal services related to property, construction, accommodation, property management, architect services  _(VAT Directive 2006/112/EC, Article 47)_
- **Place of supply** — Where the **property is located** — regardless of B2B/B2C and regardless of where supplier or customer is  _(VAT Directive 2006/112/EC, Article 47)_
- **Practical impact** — A German architect designing a building in Portugal must charge Portuguese VAT (or register there), even if the client is in Ireland  _(VAT Directive 2006/112/EC, Article 47)_
- **Common trap** — Freelancers forget that remote design work for foreign property still follows this rule  _(VAT Directive 2006/112/EC, Article 47)_

### 2.2 Passenger Transport — Article 48 [T1]

- **Place of supply** — Where the transport takes place, **proportional to distances covered** in each country  _(VAT Directive 2006/112/EC, Article 48)_
- **B2B/B2C** — Same rule applies to both  _(VAT Directive 2006/112/EC, Article 48)_
- **Example** — A bus journey from Belgium through Luxembourg to Germany: VAT is split proportionally across all three countries  _(VAT Directive 2006/112/EC, Article 48)_

### 2.3 Goods Transport (B2C only) — Article 49 [T2]

- **Place of supply** — Where the transport takes place, proportional to distances  _(VAT Directive 2006/112/EC, Article 49)_
- **B2B** — Art 44 applies instead (customer's country)  _(VAT Directive 2006/112/EC, Article 49)_
- **B2C intra-EU** — Place where transport begins, unless transport is between two member states — then destination  _(VAT Directive 2006/112/EC, Article 49)_

### 2.4 Cultural, Artistic, Sporting, Scientific, Educational, Entertainment Events — Articles 53–54 [T2]

**Events table**  _(VAT Directive 2006/112/EC, Articles 53-54)_

| Scenario | Article | Place of Supply |
| --- | --- | --- |
| B2B — admission to an event | Art 53 | Where the event **physically takes place** |
| B2C — admission and related services | Art 54 | Where the event physically takes place |
| B2B — services other than admission (e.g., organising, production) | Art 44 | Customer's country (general rule) |

**Key distinction:** "Admission" means the right to attend. Organising or sponsoring an event for a business client follows the general B2B rule (Art 44), not the event location rule.

ECJ case C-647/17 (*Srf konsulterna*): A seminar involving active participation for a business client is a B2B service under Art 44, not "admission" under Art 53.

### 2.5 Restaurant and Catering Services — Article 55 [T1]

- **Place of supply** — Where the services are **physically carried out**  _(VAT Directive 2006/112/EC, Article 55)_
- **On board transport** — See Art 57 — place of supply = point of departure within EU  _(VAT Directive 2006/112/EC, Article 57)_
- **B2B/B2C** — Same rule for both  _(VAT Directive 2006/112/EC, Article 55)_

### 2.6 Short-Term Hire of Transport — Article 56 [T1]

- **Short-term (≤30 days; ≤90 days for vessels)** — Where the means of transport is **put at the customer's disposal**  _(VAT Directive 2006/112/EC, Article 56)_
- **Long-term B2B** — Customer's country (Art 44)  _(VAT Directive 2006/112/EC, Article 56)_
- **Long-term B2C** — Supplier's country (Art 45), except pleasure boats = where put at disposal if supplier established there  _(VAT Directive 2006/112/EC, Article 56)_

### 2.7 Electronically Supplied Services, Telecoms, Broadcasting (B2C) — Article 58 [T1]

- **Applies to** — SaaS, downloads, streaming, e-books, online courses (pre-recorded), cloud hosting, telecoms, broadcasting — B2C only  _(VAT Directive 2006/112/EC, Article 58)_
- **Place of supply** — Where the **customer** is established / resides  _(VAT Directive 2006/112/EC, Article 58)_
- **B2B** — Art 44 applies instead (customer's country, reverse charge)  _(VAT Directive 2006/112/EC, Article 44)_
- **EUR 10,000 threshold (Art 59c)** — EU-established sellers below €10,000 total cross-border B2C digital sales may charge home-country VAT EUR  _(VAT Directive 2006/112/EC, Article 59c)_
- **Non-EU sellers** — No threshold benefit; must always charge destination-country rate  _(VAT Directive 2006/112/EC, Article 59c)_
- **Compliance** — Use OSS (One-Stop Shop) to report across all EU countries from a single registration  _(VAT Directive 2006/112/EC, Article 58)_

### 2.8 "Listed Services" to Non-EU Consumers (B2C) — Article 59 [T1]

Certain services supplied B2C to a person **outside the EU** are taxed where the customer is — making them outside the scope of EU VAT:

- Intellectual property / copyright licensing
- Advertising
- Consulting, legal, accounting, engineering
- Data processing, information supply
- Banking, financial, insurance services
- Staff supply
- Hiring of movable tangible property (except transport)
- Telecoms, broadcasting, electronically supplied services

**If the B2C service is NOT on this list** (e.g., personal services, cleaning, yoga instruction): place of supply remains the supplier's country under Art 45, even if the consumer is outside the EU.

## Section 3: Rules for Goods

### 3.1 Domestic Supply — No Transport (Article 31) [T1]

- **Place of supply** — Where the goods are **located at the time of supply**  _(VAT Directive 2006/112/EC, Article 31)_
- **Example** — Goods sold in a German shop to a walk-in customer: German VAT  _(VAT Directive 2006/112/EC, Article 31)_

### 3.2 Goods Dispatched or Transported (Article 32) [T1]

- **Place of supply** — Where the goods are located when **dispatch or transport to the customer begins**  _(VAT Directive 2006/112/EC, Article 32)_
- **Example** — German warehouse ships goods to a German customer: place of supply = Germany  _(VAT Directive 2006/112/EC, Article 32)_
- **Exception** — Distance selling rules (Art 33) and installation/assembly (Art 36) override this  _(VAT Directive 2006/112/EC, Article 32)_

### 3.3 Intra-EU Distance Selling (Article 33) [T1]

- **What** — Goods sold to consumers (B2C) or non-VAT-registered entities in another EU country  _(VAT Directive 2006/112/EC, Article 33)_
- **Place of supply** — Where dispatch or transport **ends** (customer's country)  _(VAT Directive 2006/112/EC, Article 33)_
- **EUR 10,000 threshold (Art 59c)** — EU sellers below €10,000 total cross-border B2C goods + digital services may treat place of supply as origin country EUR  _(VAT Directive 2006/112/EC, Article 59c)_
- **Above threshold** — Must charge destination-country VAT rate  _(VAT Directive 2006/112/EC, Article 33)_
- **Compliance** — Use Union OSS to report all intra-EU distance sales from one registration  _(VAT Directive 2006/112/EC, Article 33)_
- **Post-2021 change** — Individual country thresholds (€35,000/€100,000) replaced by single €10,000 EU-wide threshold  _(VAT Directive 2006/112/EC, Article 33)_

### 3.4 Imports from Outside the EU (Article 30/60-61) [T1]

- **Place of importation** — The EU member state where goods **enter the EU** (Art 60)  _(VAT Directive 2006/112/EC, Article 60)_
- **Suspensive arrangements** — If goods are placed under customs warehousing or transit, importation occurs where goods **leave** that arrangement (Art 61)  _(VAT Directive 2006/112/EC, Article 61)_
- **VAT due** — At importation, by the importer — collected by customs  _(VAT Directive 2006/112/EC, Article 30/60-61)_
- **IOSS alternative** — For goods ≤€150 sold B2C, use Import One-Stop Shop to collect VAT at point of sale  _(VAT Directive 2006/112/EC, Article 30/60-61)_

### 3.5 Installation or Assembly (Article 36) [T1]

- **Place of supply** — Where the goods are **installed or assembled**  _(VAT Directive 2006/112/EC, Article 36)_
- **Example** — German manufacturer ships and installs machinery in a French factory: place of supply = France  _(VAT Directive 2006/112/EC, Article 36)_

### 3.6 Chain Transactions (Article 36a) [T1]

Introduced by Directive (EU) 2018/1910 to simplify chain (successive) supplies:

- **Scenario** — Goods supplied A → B → C, shipped directly from A to C across EU borders  _(VAT Directive 2006/112/EC, Article 36a)_
- **Transport attributed to** — The supply **to** the intermediary operator (B)  _(VAT Directive 2006/112/EC, Article 36a)_
- **Intermediary operator** — A supplier in the chain (other than the first) who dispatches or arranges transport  _(VAT Directive 2006/112/EC, Article 36a)_
- **Exception** — If B communicates to A the VAT number issued by the dispatch member state, transport is attributed to B's supply to C  _(VAT Directive 2006/112/EC, Article 36a)_
- **Effect** — Only one supply in the chain is the intra-EU zero-rated supply; the other is a domestic supply  _(VAT Directive 2006/112/EC, Article 36a)_

**Simplified triangulation (Art 141):** In a three-party chain A (MS1) → B (MS2) → C (MS3), B can avoid registering in MS3 if all conditions of Art 141 are met. B issues an invoice with "reverse charge" and C self-assesses VAT in MS3.

## Section 4: OSS / IOSS Decision Tree

### When to register for One-Stop Shop

```
START: Do you sell goods or digital services B2C to consumers in other EU countries?
│
├─ NO → OSS not needed
│
├─ YES → Are you an EU-established business?
│   │
│   ├─ YES → Do your total cross-border B2C sales (goods + digital services)
│   │         exceed EUR 10,000/year?
│   │   │
│   │   ├─ NO → You MAY charge home-country VAT. OSS optional.
│   │   │        (But you can opt in to OSS voluntarily.)
│   │   │
│   │   └─ YES → You MUST charge destination-country VAT.
│   │             Register for UNION OSS in your home country.
│   │
│   └─ YES (established in >1 EU country) → EUR 10,000 threshold does NOT apply.
│         Register for Union OSS.
│
└─ YES → Are you a NON-EU business?
    │
    ├─ Selling digital services / telecoms / broadcasting B2C →
    │   Register for NON-UNION OSS in any EU country of choice.
    │   No threshold benefit. Always charge destination rate.
    │
    └─ Selling goods from outside EU, consignments ≤EUR 150 →
        Register for IOSS (Import One-Stop Shop).
        Collect VAT at checkout. Goods enter EU VAT-paid.
        Note: From 1 July 2026, EUR 3 flat customs duty also applies.
```

### OSS Comparison Table

**OSS Comparison Table**

| Scheme | Who | What | Filing |
| --- | --- | --- | --- |
| Union OSS | EU-established sellers | Intra-EU B2C distance sales of goods + B2C services in other EU states | Quarterly, home country |
| Non-Union OSS | Non-EU sellers | B2C digital/telecom/broadcasting services to EU consumers | Quarterly, any EU country |
| IOSS | Any seller (EU or non-EU) | Distance sales of imported goods ≤€150 to EU consumers | Monthly, home/chosen country |

## Section 5: Non-EU Rules Comparison

### 5.1 US Sales Tax Nexus

**US Sales Tax Nexus table**

| Aspect | US Rule |
| --- | --- |
| Tax type | Sales tax (state-level, not federal) |
| Place of supply equivalent | "Nexus" determines which state can tax you |
| Physical nexus | Office, warehouse, employee, or inventory in the state |
| Economic nexus (*South Dakota v. Wayfair*, 2018) | Most states: $100,000 in sales OR 200 transactions/year |
| Digital services | Taxability varies by state — SaaS taxable in ~25 states, not taxable in CA, GA, MO |
| No equivalent of reverse charge | Seller must collect and remit; no mechanism for buyer self-assessment in most states |
| Key difference from EU | No single national registration; must track nexus in 45+ states individually (or use automation like Stripe Tax, TaxJar, Avalara) |

### 5.2 Australian GST on Imports

**Australian GST on Imports table**

| Aspect | Australian Rule |
| --- | --- |
| Threshold | AUD 75,000/year in supplies to Australian consumers |
| Digital services B2C | Non-resident must register for GST and charge 10% |
| Low-value goods (≤AUD 1,000) | GST applies at point of sale since July 2018 |
| B2B | Reverse charge applies (Australian business self-assesses) |

### 5.3 India OIDAR (Online Information and Database Access or Retrieval)

**India OIDAR table**

| Aspect | Indian Rule |
| --- | --- |
| Applies to | Non-resident suppliers of OIDAR services to non-taxable Indian recipients (B2C) |
| Definition | Services delivered over the internet — substantially automated, minimal human intervention |
| Rate | 18% IGST |
| Registration | Simplified registration under GST for non-resident OIDAR suppliers |
| B2B | Indian business self-assesses under reverse charge |
| Equalization Levy | Separate 2% levy on non-resident e-commerce operators (no global revenue threshold) |

### 5.4 Japan Consumption Tax on Digital Services

**Japan Consumption Tax table**

| Aspect | Japanese Rule |
| --- | --- |
| Rate | 10% (8% reduced rate for food/beverages, not applicable to digital) |
| Non-resident digital services B2C | Must register and charge JCT regardless of revenue |
| B2B | Reverse charge applies for "specified services" received from abroad |
| Threshold | No de minimis for non-resident digital service providers to consumers |
| Invoice system | Qualified Invoice System (QIS) since October 2023 — registered invoices required for input tax credit |

### Comparison Summary

**Comparison Summary**

| Feature | EU | US | Australia | India | Japan |
| --- | --- | --- | --- | --- | --- |
| Tax type | VAT | Sales tax | GST | GST + EL | JCT |
| B2B mechanism | Reverse charge | N/A | Reverse charge | Reverse charge | Reverse charge |
| B2C digital | Customer location | Nexus-based | Customer location | Customer location | Customer location |
| Single registration | OSS | No (per-state) | Single ATO reg | Single GST reg | Single NTA reg |
| Threshold (B2C digital) | €10,000 (EU sellers) | $100K/200 txn per state | AUD 75,000 | Nil (simplified reg) | Nil |

## Section 6: Practical Decision Flowchart for Freelancers

**"I'm in Country A, my client is in Country B, and I'm providing [service type]. What VAT applies?"**

### Step 1: Classify the Supply

**Step 1 table**

| Question | If YES | If NO |
| --- | --- | --- |
| Are you selling **goods** (physical products)? | Go to Goods Flow (below) | Continue to Step 2 |

### Step 2: Identify the Customer

**Step 2 table**

| Question | If YES | If NO |
| --- | --- | --- |
| Is your client a **business** (with a VAT number)? | B2B → Go to Step 3 | B2C → Go to Step 4 |

### Step 3: B2B Service — Check Exceptions

**Step 3 table**

| Question | If YES | If NO |
| --- | --- | --- |
| Is the service related to **immovable property** (Art 47)? | VAT where property is located | Continue |
| Is the service **admission to an event** (Art 53)? | VAT where event takes place | Continue |
| Is it **short-term hire of transport** ≤30 days (Art 56)? | VAT where vehicle put at disposal | Continue |
| Is it **restaurant/catering** (Art 55)? | VAT where performed | Continue |
| Is it **passenger transport** (Art 48)? | VAT proportional to route | Continue |
| **None of the above?** | → **Art 44 applies.** Place of supply = client's country. Invoice without VAT. Client self-assesses (reverse charge in EU; self-assessment rules outside EU). |  |

### Step 4: B2C Service — Check Exceptions

**Step 4 table**

| Question | If YES | If NO |
| --- | --- | --- |
| Is it an **electronically supplied service, telecoms, or broadcasting** (Art 58)? | VAT where consumer is located. Use OSS if selling into EU. | Continue |
| Is the service related to **immovable property** (Art 47)? | VAT where property is located | Continue |
| Is it **admission to an event** (Art 54)? | VAT where event takes place | Continue |
| Is the consumer **outside the EU** and is the service on the Art 59 list? | Outside scope of EU VAT | Continue |
| **None of the above?** | → **Art 45 applies.** Place of supply = YOUR country. Charge your domestic VAT rate. |  |

### Goods Flow

**Goods Flow table**

| Question | If YES | If NO |
| --- | --- | --- |
| Are you shipping goods to a **consumer in another EU country**? | Distance selling (Art 33). Above €10,000 threshold → destination VAT. Use Union OSS. | Continue |
| Are you shipping goods from **outside the EU** to EU consumers, value ≤€150? | Use IOSS. Collect destination VAT at checkout. | Continue |
| Are goods **installed/assembled** at customer location (Art 36)? | VAT where installed | Continue |
| Standard domestic or B2B intra-EU supply? | Art 31/32 (origin) or intra-EU zero-rated supply + acquisition tax in destination |  |

### Common Freelancer Scenarios

**Common Freelancer Scenarios table**

| You are in... | Client is in... | Service | Result |
| --- | --- | --- | --- |
| Germany | France | Web development (B2B) | Art 44. No German VAT. French client reverse-charges at 20%. |
| Germany | France | Web development (B2C) | Art 45. Charge German 19% VAT. (Not a digital service — bespoke human work.) |
| Germany | France | SaaS subscription (B2C) | Art 58. Charge French 20% VAT. Report via OSS. |
| Malta | US | Consulting (B2B) | Art 44. Place of supply = US. No Malta VAT. Outside scope. |
| Malta | US | Pre-recorded online course (B2C) | Art 58/59. Place of supply = US (outside EU). No Malta VAT. But check US sales tax nexus. |
| UK | Germany | Design services (B2B) | UK is outside EU. No UK VAT (outside scope). German client self-assesses under German domestic rules. |
| India | Australia | Software dev (B2B) | Zero-rated export under IGST. No IGST if LUT filed. Australian client reverse-charges GST. |
| US | EU consumers | SaaS product (B2C) | Must register for non-Union OSS. Charge each EU country's VAT rate. No threshold benefit. |
| France | Switzerland | Architecture for property in France | Art 47. Property in France → French VAT at 20%, regardless of client location. |

## PROHIBITIONS

- **1** — NEVER default to Art 44 or Art 45 without checking the exceptions in Section 2.
- **2** — NEVER assume that all B2C services to foreign consumers are outside the scope of VAT. Only Art 59 "listed services" shift to the consumer's country for B2C.
- **3** — NEVER ignore the immovable property rule (Art 47). It overrides everything.
- **4** — NEVER apply the €10,000 threshold to non-EU sellers — they must always charge destination-country VAT.
- **5** — NEVER confuse "zero-rated" with "exempt." Zero-rated preserves input VAT recovery; exempt does not.
- **6** — NEVER skip VIES verification before zero-rating an intra-EU B2B supply.
- **7** — NEVER assume the same place-of-supply rules apply in all countries. Non-EU jurisdictions (US, Australia, India, Japan) have fundamentally different approaches.

## Edge Cases

### EC1 — Bespoke software vs. SaaS (ESS classification) [T2]

**Situation:** A developer builds custom software for a specific B2C client. Is this an electronically supplied service (Art 58)?
**Resolution:** Custom software development with significant human intervention is NOT an ESS. It is a standard service under Art 45 (B2C) or Art 44 (B2B). Pre-packaged SaaS delivered automatically IS an ESS. Flag for reviewer if the degree of customisation is unclear.

### EC2 — Remote worker creating PE risk [T2]

**Situation:** A UK freelancer works from Spain for 8 months serving UK clients. Does Spain become the "establishment" for place-of-supply purposes?
**Resolution:** If the freelancer becomes established in Spain (fixed establishment under Art 11 of Implementing Regulation 282/2011), the place of supply of their B2C services may shift to Spain. B2B services under Art 44 are unaffected (place of supply = client's country). Flag for reviewer — tax residency and PE risk should also be assessed.

### EC3 — Mixed digital and live service bundle [T2]

**Situation:** A course provider sells a package: pre-recorded videos (ESS) + live weekly coaching calls (not ESS) to an EU consumer.
**Resolution:** If a single composite supply, the principal element determines classification. If independent supplies, each follows its own rules. Pre-recorded = Art 58 (customer location). Live coaching = Art 45 (supplier location). Flag for reviewer to determine whether composite or independent.

### EC4 — Chain transaction with unknown intermediary role [T3]

**Situation:** A → B → C chain where goods ship directly from Poland to Portugal, but it is unclear whether B is the intermediary operator under Art 36a.
**Resolution:** Escalate. The attribution of transport determines which supply is zero-rated (intra-EU) and which is domestic. Incorrect attribution can cause double taxation or VAT loss. Requires review of contractual arrangements and Incoterms.

## Test Suite

### Test 1 — B2B consulting, Germany to France

**Input:** German consultant invoices French company (valid FR VAT number) EUR 5,000 for strategy consulting.
**Expected:** Art 44. Place of supply = France. No German VAT. Reverse charge. Supplier reports on ESL.

### Test 2 — B2C yoga class (non-listed service), Malta to US consumer

**Input:** Maltese instructor provides a private in-person yoga session in Malta to a US tourist. EUR 100.
**Expected:** Art 45. Not a listed service under Art 59. Place of supply = Malta. Charge Maltese VAT at 18%.

### Test 3 — B2C SaaS, US company to French consumer

**Input:** US SaaS company sells a EUR 20/month subscription to a French consumer.
**Expected:** Art 58. ESS B2C. Place of supply = France. Non-Union OSS required. Charge 20% French VAT.

### Test 4 — Architect, property in another country

**Input:** Italian architect designs a villa in Greece for a German client (B2B). EUR 15,000.
**Expected:** Art 47 (immovable property). Place of supply = Greece. Reverse charge does NOT apply under Art 196. Italian architect may need to register for Greek VAT.

### Test 5 — Distance selling, below threshold

**Input:** Spanish e-commerce seller ships EUR 8,000 of handmade goods to consumers across 5 EU countries. Prior year was EUR 7,000.
**Expected:** Below €10,000 threshold. May treat place of supply as Spain and charge Spanish VAT. OSS optional.

### Test 6 — Distance selling, above threshold

**Input:** Same seller now has EUR 15,000 in cross-border B2C goods sales.
**Expected:** Above threshold. Must charge destination-country VAT. Register for Union OSS.

## Official Sources

- **EU VAT Directive (consolidated):** https://eur-lex.europa.eu/eli/dir/2006/112
- **EC Place of Taxation guidance:** https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/place-taxation_en
- **EU OSS portal:** https://vat-one-stop-shop.ec.europa.eu
- **VIES VAT number validation:** https://ec.europa.eu/taxation_customs/vies/
- **Implementing Regulation 282/2011:** https://eur-lex.europa.eu/eli/reg_impl/2011/282
- **IOSS guidance (Irish Revenue):** https://www.revenue.ie (search "IOSS")

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. VAT rates, thresholds, and place-of-supply rules are subject to change. Always verify current rules with official sources and a qualified indirect tax advisor.

*Data reflects 2025–2026 rules. OpenAccountants — open-source accounting skills for AI — info@openaccountants.com*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
