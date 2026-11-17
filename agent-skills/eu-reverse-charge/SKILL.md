---
name: eu-reverse-charge
description: "Use this skill whenever a cross-border B2B service transaction occurs between EU member states and the question is whether the reverse charge mechanism under Article 196 of the VAT Directive applies. Trigger on phrases like \"reverse charge\", \"B2B services EU\", \"intra-community services\", \"Article 196\", \"EC Sales List\", \"self-assess VAT\", \"cross-border VAT EU\", or any request involving the VAT treatment of services supplied between businesses in different EU countries. This skill contains the complete decision logic for determining when reverse charge applies, how the supplier and customer each report it, the EC Sales List obligations, and the country-specific box mappings that link back to each country's VAT return skill. ALWAYS read this skill before classifying any intra-EU B2B service transaction."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eu-reverse-charge"
  jurisdiction: "GLOBAL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# EU Reverse Charge v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This skill applies the EU service-place and customer-liability framework for 2026. Its core job is ordinary cross-border Article 44 services received in an EU member state. It covers the supplier and customer, customer evidence, exception services, invoicing, recapitulative statements, partial deduction, branches, service chains, mixed private use and continuous supplies. It does not prepare a national return without the current country overlay. A supplier can be outside the EU; Article 196 tests non-establishment in the customer member state, not EU citizenship or incorporation.

Use `eu-oss-digital` for eligible B2C digital supplies and the relevant national VAT-return skill for rates, exemptions, registration, tax points, fields, payments and penalties. Property, physical event admission, transport and catering need their specific place rules and then their liability rule. Domestic reverse charges, goods triangulation and complex group structures require the relevant country skill and reviewer.

The original working tags [T1], [T2] and [T3] mean respectively a rule with known facts, a fact-sensitive review point, and a referral boundary. They are not professional approval, a licence or permission to file without review. Unknown essential facts stop classification.

### Quick reference

| Question | Rule and conditions | Official source |
|---|---|---|
| Who accounts for ordinary business services? | Article 44 receiving-establishment place, then Article 196 customer liability where supplier is not established there for the supply; check recipient status, actual use and exemptions | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Short transport hire exception | Not more than 30 days (in words on the page), or 90 days for vessels; continuous possession/use, actual disposal place under Article 56 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Article 196 invoice deadline | By the 15th day of the month following the chargeable event (in words on the page), Article 222; check the actual tax point and competent invoice law | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Recapitulative statement | Article 263 monthly framework with national quarterly-services option, within no more than 1 month after the period (in words on the page); Article 262 excludes services exempt where taxable | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

## Ask the client first

1. Where are the supplier and customer business and fixed establishments, and which establishment provides or receives this service?
2. What exactly is supplied, and is it for business, exclusively private or mixed use? Obtain the contract and invoice.
3. What is the recipient's taxable-person or VAT-identified legal-person status, with VIES/registration and identity evidence?
4. Is the service subject to a special place rule, exemption or cross-border SME exemption?
5. What are the service, payment and successive-account dates and reporting period?
6. What deduction entitlement and current national return/statement obligations apply?


- **Pre-check question 1: supplier VAT registration**  -  Establish the supplier's taxable status and all relevant establishments/registrations. Article 196 can include a supplier outside the EU; lack of an EU VAT number alone does not exclude it.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Pre-check question 2: customer VAT registration in different state**  -  Identify the EU receiving establishment and relevant registration. If supplier and customer are established in the same state for this supply, stop the Article 196 test; establish the actual place under the general or special rule before deciding national treatment. Do not rely solely on registration-country codes.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Pre-check question 3: customer is a business (B2B)**  -  Is the customer a business (B2B)? Determine status and use under Regulation Articles 18-19; a valid VIES number is evidence, not the complete test. If the customer is a private individual (B2C), reverse charge does NOT apply -- apply the B2C place rule, exemption and any eligible OSS route (see `eu-oss-digital.md`).  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Pre-check question 4: nature of the service**  -  What is the nature of the service? Needed to check specific place-of-supply rules.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Stop condition for unknown pre-checks**  -  If items 1-3 are unknown, STOP. Do not classify the transaction.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


## The method, step by step

### Step 1: Decision Tree -- Does Reverse Charge Apply? [T1]

**Legislation:** VAT Directive Art 44 (general B2B rule), Art 45 (general B2C rule), Art 46-59 (specific exceptions), Art 196 (reverse charge obligation).

### Decision Tree Table

**Decision Tree Table**  _([Step 1: Decision Tree -- Does Reverse Charge Apply? [T1]](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_

| Step | Question | If YES | If NO |
| --- | --- | --- | --- |
| 1 | Is the customer a taxable person acting as such or a non-taxable legal person identified for VAT and treated as taxable under Article 43(2)? Establish status and business use under Regulation 282/2011 Articles 18-19; VIES is one evidence route. | Go to Step 2 | **STOP.** B2C rules apply. Determine the applicable B2C place rule and any exemption; use OSS only for eligible taxable supplies. Reverse charge does NOT apply.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 2 | Is the supplier not established in the customer member state for this supply, taking account of any intervening fixed establishment? | Go to Step 3 | **STOP this Article 196 test.** The supplier-establishment condition for Article 196 fails. Still determine the actual general or special place rule and national liability; same-country establishments do not make a foreign-property or foreign-admission service domestic. Use the country skill.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 3 | Does the service have a sufficiently direct connection with identified immovable property (land, buildings)? Article 47 and Regulation Article 31a; general advice or plans not tied to a particular plot are not automatically included. | **STOP.** Place of supply = where property is located. Article 196 does not decide liability. Check the property-state national reverse charge before deciding whether the supplier must register. [T2] | Go to Step 4  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 4 | Is the service admission to a cultural, artistic, sporting, scientific, educational, or entertainment event attended in person? Art 53 (Art 53 does not apply where the attendance is virtual). | **STOP.** Place of supply = where event takes place. Article 196 does not decide liability; check national recipient-liability rules. [T2] | Go to Step 5  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 5 | Is the service short-term hire of a means of transport (<=30 days (in words on the page), <=90 days for vessels)? Art 56(1). | **STOP.** Place of supply = where vehicle put at disposal. Article 196 does not decide liability; check national recipient-liability rules. [T2] | Go to Step 6  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 6 | Is the service restaurant/catering on board transport (ship, plane, train) within EU? Art 57. | **STOP.** Place of supply = point of departure. Article 196 does not decide liability; check national recipient-liability rules. [T2] | Go to Step 7  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 7 | Is the service passenger transport? Art 48. | **STOP.** Place of supply = where transport takes place proportionally. Article 196 does not decide liability; check national recipient-liability rules. [T2] | Go to Step 8  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 8 | Is this ordinary restaurant/catering physically supplied away from the onboard Article 57 case? | **STOP.** Article 55 locates the service where physically carried out; check national liability. | Otherwise go to Step 9. https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| 9 | **Reverse charge applies.** Place of supply = the receiving business or fixed establishment's state under Art 44. Customer self-assesses VAT under Art 196, subject to any applicable exemption. Supplier invoices without its own VAT; this is not a universal 0% rate. | -- | --  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

### Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2]

**Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2]**  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).

| Exception | Article | Place of Supply |
| --- | --- | --- |
| Services with a sufficiently direct connection to immovable property under Regulation 31a | Art 47 | Location of property  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Passenger transport | Art 48 | Where transport takes place  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Goods transport to B2C, except intra-Community transport | Art 49 | Where transport takes place proportionately; intra-Community B2C goods transport instead starts at the departure place under Article 50  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Cultural/sporting/educational event admission | Art 53 | Where event takes place  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Restaurant and catering | Art 55 | Where physically carried out  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Short-term hire of transport | Art 56(1) | Where put at disposal  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Restaurant/catering on board transport | Art 57 | Point of departure  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

- **Flag exceptions as T2**  -  If the service falls into any exception above, flag as [T2] and determine place of supply under the specific article. Do not apply Article 196 solely by assuming the Article 44 general rule; separately check national recipient liability.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


### Step 2: How the Supplier Treats It [T1]

- **Invoice without VAT**  -  For an ordinary taxable Article 196 supply the supplier does not charge its own VAT. Show the net consideration and reverse-charge mention; do not describe the supply as universally zero-rated.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Required invoice notation**  -  Include the mention "Reverse charge" required by Article 226(11a). "Reverse charge -- Article 196 of Council Directive 2006/112/EC" is a useful expanded notation, subject to national invoice rules, not the Directive's mandatory full wording.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Include both VAT numbers**  -  Apply the competent invoice law and Article 226(3)-(4) identification requirements. For an EU supplier identified for the supply, include its VAT number and the customer number under which the customer is liable. A non-EU supplier does not acquire an EU number merely from this rule; verify its own invoice requirements. Where Article 18(1)(b) supports a customer still awaiting a number, resolve the applicable registration, invoice and statement requirements before issuing or filing; do not invent a VAT number or treat the evidence route as an invoice-content waiver.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Report on EC Sales List (ESL)**  -  For a qualifying outgoing intra-EU service in Article 262(1)(c), file the recapitulative statement for the national period, with customer VAT number and service value. Exclude services exempt in the customer state; do not impose this EU statement automatically on a non-EU supplier.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Report on the VAT return**  -  An Article 44 service supplied to an establishment abroad is reported according to the supplier state's rules for services whose place is abroad. It is not automatically a zero-rated or exempt domestic supply. The specific field depends on country and return edition.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


### Step 3: How the Customer Treats It [T1]

- **Self-assess output VAT**  -  Determine the service's taxable value, applicable local rate or exemption and tax point, then self-assess output VAT. A standard rate is used only if this service falls within that rate. Apply the country skill and current law rather than assuming all services have the standard rate.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Simultaneously claim input VAT**  -  Claim only the input tax actually deductible under Articles 168, 173 and 178(f), subject to local evidence, use, blocked-input and timing rules. Equal output and input in the same return is conditional on full entitlement and the required formalities, not automatic.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Net effect for fully taxable business**  -  On full entitlement and the same-period deduction facts, equal output and eligible input produce zero net tax. Fully taxable status alone does not remove blocked-input or timing restrictions. Output liability must still be reported; claim only permitted input.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Report on Intrastat / acquisition section**  -  Report in the country's recipient-liability services fields. Do not call a service an intra-Community acquisition of goods or an Intrastat goods movement. Separate national service statistics can still apply; verify them in the country skill.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


### Step 4: EC Sales List (ESL) Requirements [T1]

- **Who must file**  -  A VAT-identified taxable person supplying services to the persons in Article 262(1)(c), other than services exempt in the state where taxable, for which the recipient is liable under Article 196. Intra-EU service statements and national registration rules must be checked; this is not a statement obligation on every non-EU supplier.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_
- **What to report**  -  Customer's VAT identification number + total value of services for the period.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_
- **Frequency**  -  Monthly under VAT Directive Art 263(1); member states may allow a quarterly statement for services (Art 263(1c)) (e.g., France monthly DES for services).  _([Regulation (EU) No 904/2010; VAT Directive Art 262-263.](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_
- **Deadline**  -  Varies by member state, within a period not exceeding one month (VAT Directive Art 263); check the national deadline, which can be shorter.  _([Regulation (EU) No 904/2010; VAT Directive Art 262-263.](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_
- **Penalty for non-filing**  -  Varies by member state. The old unsourced EUR 50 to EUR 5,000+ range is reserved under Not yet confirmed and must not be used to estimate liability.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_

### Critical Rule [T1]

- **Non-filing does not change VAT treatment**  -  Failure to file a statement does not, by itself, switch Article 196 customer liability to supplier liability: check the actual Article 44/196 conditions. Correct the statement and any return, and determine national penalties separately. A services reporting omission is not an acquisition of goods.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


### Step 5: VIES Validation [T1]

- **VIES verification requirement**  -  For an EU customer communicating a VAT number, obtain confirmation of its validity and associated identity under Regulation 282/2011 Article 18(1)(a). Use VIES: https://ec.europa.eu/taxation_customs/vies/. Retain the result with the customer identity, service-use and establishment evidence. Article 18(1)(b) separately permits a customer who has applied for a number to be assessed from other proof with reasonable commercial verification.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **VIES confirms valid**  -  If the number is valid, continue the service, business-use, establishment, exemption and liability tests. A valid number alone does not prove that every service is an Article 44/196 supply.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **VIES shows invalid**  -  If VIES shows invalid, investigate the identifier and customer evidence and advise the customer to resolve registration. Do not automatically charge domestic VAT: a pending-registration case can satisfy Article 18(1)(b), and customer status, use, place and national obligations still determine the result. Refer unresolved evidence rather than guessing.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **VIES temporarily unavailable**  -  If VIES is unavailable, document the attempt and retry. An outage does not establish the customer's status; collect lawful corroboration and obtain review before invoicing or filing. The failed attempt alone is not a legal safe harbour.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


### Reporting fields actually checked

For France, the 2026 CA3 notice identifies E2 for services to a foreign-established customer, A3 for taxable general-rule services received from a non-established supplier, and the appropriate rate/output and deduction fields. DES applies to qualifying outgoing intra-EU services, excluding services exempt in the customer state. For Slovakia, the current DPHv25 form uses 09b/10b for standard-rate recipient-liable services and the eligible standard-rate deduction in aggregate row 19; rows 11/12 concern triangulation goods, not ordinary services. Do not force outgoing Article 44 services into old row 15: the authority excludes transactions located outside Slovakia from the domestic return. For a German recipient of ordinary Article 44 services from an entrepreneur established in another EU state, the 2026 form row 30 uses KZ 46 for base and KZ 47 for output; deductible section 13b input uses row 41/KZ 67. German outgoing section 18b services use row 35/KZ 21. These identifiers do not apply indiscriminately to non-EU suppliers: the form separately has other recipient-liable services in row 32/KZ 84/85. Current Malta identifiers remain reserved. Italian annual IVA 2026 instructions cover tax period 2025: the 2025-2026 filing cycle confirms VE34 for qualifying outside-territory supplies, VJ3 for relevant foreign supplier purchases and VF1-VF13 by rate for eligible purchases. It does not confirm annual fields for tax period 2026, which remain reserved, nor the separate Intrastat service thresholds.

| Filing instruction | Conditions | Official source |
|---|---|---|
| France E2 / A3 | Respect supplier versus recipient direction; rate and deduction depend on the actual service and use | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf |
| France DES within 10 working days after the month | Only the qualifying outgoing intra-EU services in the notice; do not substitute the goods statement | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf |
| Germany KZ 21 / 46 / 47 / 67 | 2026 form: outgoing qualifying EU service / EU-established supplier recipient base / output / permitted section 13b input; other foreign cases need the other form branch | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=7 |
| Italy VE34 / VJ3 / VF1-VF13 | 2025-2026 filing cycle only, tax period 2025; not confirmation of tax-period 2026 annual fields | https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 |
| France output 08 / eligible input 20 | Metropolitan standard-rate service and eligible non-capital service purchase; apply actual deduction conditions | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf |
| Slovakia 09b / 10b / 19 | Standard-rate ordinary recipient-liable service; row 19 only to extent deductible, not an automatic full claim | https://pfseform.financnasprava.sk/Formulare/eFormVzor/DP/form.616.html |
| Slovakia outgoing services | Place abroad is excluded from the domestic return; separately determine summary statement | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie |
## Boundary and exception table


### EC1 -- Customer has a VAT number but is a non-taxable legal person [T2]

**Situation:** The customer has a VAT identification number (e.g., for intra-EU goods acquisitions) but is not a taxable person acting as such (e.g., a government body, a holding company with no economic activity).
**Resolution:** Article 43(2) treats a non-taxable legal person identified for VAT as taxable for the place-of-services rules; Article 196 expressly includes it. Confirm the actual registration and capacity/use rather than assuming this group is excluded. Regulation Article 19 governs exclusively private use.

### EC2 -- Supplier has a fixed establishment in the customer's country [T2]

**Situation:** A German company supplying services to a French customer also has a fixed establishment (branch) in France. Does the French branch trigger domestic treatment instead of reverse charge?
**Resolution:** If the French fixed establishment is NOT involved in the supply, reverse charge still applies (Art 44; Art 192a of the VAT Directive + Implementing Regulation Art 53). If the fixed establishment IS involved, the supply is domestic. Flag for reviewer to determine which establishment is making the supply.

### EC3 -- Chain of services (intermediary) [T2]

**Situation:** Company A (MT) supplies a service to Company B (DE), who re-supplies it to Company C (FR). Who applies reverse charge?
**Resolution:** Each link in the chain is treated independently. A→B: reverse charge applies (MT→DE). B→C: reverse charge applies (DE→FR). Each qualifying outgoing intra-EU supplier reports the relevant link under Article 262(1)(c), excluding services exempt in the receiving state; check each supplier's national statement conditions. Flag for reviewer if the intermediary's involvement is unclear.

### EC4 -- Services straddling B2B and B2C (mixed customer) [T2]

**Situation:** A customer is both a business and a private individual (e.g., a sole trader purchasing services partly for business, partly for personal use).
**Resolution:** Exclusively private use, including staff private use, is B2C. A single service intended for both business and private use follows Article 44 if there is no abusive practice; do not split that single supply mechanically by use. Check place, supplier establishment and liability separately. Confirm business purpose under Regulation Article 19.

### EC5 -- Continuous services spanning multiple periods [T1]

**Situation:** A monthly retainer service (e.g., EUR 2,000/month) is invoiced quarterly at EUR 6,000.
**Resolution:** Reverse charge applies to each tax point. Article 64(1) generally treats successive-account/payment services as completed at the end of their relevant periods. Article 65 governs payments before supply, while Article 64(2) covers Article 196 continuous services supplied for more than 1 year without accounts or payment: deemed completion at each calendar year-end until completion. Article 66's national timing derogations do not apply to Article 196 services. Determine the actual contract/tax point and national reporting period, not a universal invoice-date rule.


The fixed-establishment test includes the resources actually intervening in fulfilment; mere accounting, invoicing or collection support is not intervention. Issuing under the local establishment VAT number creates the Regulation Article 53(2) presumption unless rebutted. A supplier with its business establishment in the tax state cannot use Article 192a merely because that office did not intervene (Regulation Article 54).

Sources for these boundaries: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 (Articles 43-45, 64-66, 192a, 196) and https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 (Articles 19, 53-54).

## Worked cases

Unless a case expressly changes the facts, assume ordinary taxable professional services, no applicable exemption or SME relief, a supplier not established in the receiving state for the supply, a qualifying business recipient and full same-period deduction supported by the required evidence. Case prices are illustrative inputs exclusive of VAT, including the B2C regression test price. Exceptions and national filing identifiers still require the stated checks.


### Example 1 -- Standard consulting, MT supplier to DE customer [T1]

**Facts:** Maltese VAT-registered consultant invoices a German company (valid DE VAT number) EUR 5,000 for management consulting.
**Analysis:** B2B, general service (Art 44 applies), no exceptions. Reverse charge applies.
**Supplier (MT):** Invoice EUR 5,000, no supplier VAT charge, notation "Reverse charge Art 196". Report in the national outgoing-services field (current Malta identifier reserved below). Report on the applicable services recapitulative statement, unless exempt in the customer state.
**Customer (DE):** Self-assess 19% output VAT = EUR 950 (KZ 47). Claim EUR 950 input VAT (KZ 67). Net = zero.

### Example 2 -- Software development, DE supplier to FR customer [T1]

**Facts:** German freelance developer invoices a French company (valid FR VAT number) EUR 10,000 for custom software development.
**Analysis:** B2B, general service under Art 44, no exceptions. Reverse charge applies.
**Supplier (DE):** Invoice EUR 10,000, no supplier VAT charge. Report in KZ 21. File ZM (ESL).
**Customer (FR):** Self-assess 20% output VAT = EUR 2,000 (standard-rate output Line 08). Claim EUR 2,000 input VAT (Line 20). Net = zero.

### Example 3 -- Legal services, IT supplier to MT customer [T1]

**Facts:** Italian law firm invoices a Maltese company (valid MT VAT number) EUR 3,000 for legal advice on a contract.
**Analysis:** B2B, general service under Art 44. Legal services are not in Art 45 exceptions. Reverse charge applies.
**Supplier (IT):** Invoice EUR 3,000, no supplier VAT charge, "inversione contabile Art 196". Use the current Italian outgoing-services field and verify the separate service-statistics obligation; the old VE34/Intrastat mapping remains reserved below.
**Customer (MT):** Self-assessed output on EUR 3,000 at 18% is EUR 540. Deductible input is EUR 540 only on the stated full-entitlement/same-period facts; net is zero. Current Malta return identifiers are reserved under Not yet confirmed.

### Example 4 -- Architectural services for property in France, MT supplier to DE customer [T2]

**Facts:** Maltese architect invoices a German company EUR 8,000 for designing a building located in France.
**Analysis:** Service related to immovable property (Art 47). Place of supply = France (where the property is). Reverse charge under Art 196 does NOT apply. The Maltese supplier may need to register for VAT in France and charge French VAT at 20%.
**Flag:** T2 -- reviewer must confirm whether French VAT registration is required or whether the customer can self-assess under French domestic reverse charge rules for construction services.

### Example 5 -- Conference admission in Spain, FR supplier to NL customer [T2]

**Facts:** French event organiser sells admission tickets (EUR 500) for a conference in Spain to a Dutch company.
**Analysis:** Admission to an event (Art 53). Place of supply = Spain. Standard reverse charge does NOT apply. Check Spanish liability, exemption and registration; Article 196 is not the applicable liability rule for physical admission.
**Flag:** T2 -- escalate to determine whether the French organiser must register in Spain.

### Example 6 -- Marketing services, NL supplier to SK customer [T1]

**Facts:** Dutch marketing agency invoices a Slovak company (valid SK VAT number) EUR 15,000 for digital marketing campaign.
**Analysis:** B2B, general service (Art 44), no exceptions. Reverse charge applies.
**Supplier (NL):** Invoice EUR 15,000, no supplier VAT charge. Report on the applicable services recapitulative statement, unless exempt in the customer state. Use the applicable Dutch outgoing-services field; the exact field is not sourced here.
**Customer (SK):** Standard-rate base row 09b = EUR 15,000 and output row 10b = EUR 3,450. Output VAT at 23% = EUR 3,450. Eligible standard-rate input in row 19 = EUR 3,450 on these fully deductible facts. Net = zero.

### Example 7 -- Accounting services, MT supplier to IT customer [T1]

**Facts:** Maltese CPA invoices an Italian company (valid IT VAT number) EUR 2,000 for bookkeeping services.
**Analysis:** B2B, general service under Art 44. No exceptions. Reverse charge applies.
**Supplier (MT):** Invoice EUR 2,000, no supplier VAT charge. Report EUR 2,000 in the current national outgoing-services field; the Malta identifier remains reserved. Report on the applicable services recapitulative statement, unless exempt in the customer state.
**Customer (IT):** Self-assess at 22% = EUR 440 output. Claim EUR 440 input. Net = zero.

### Example 8 -- Training seminar (in-person), DE supplier to AT customer [T2]

**Facts:** German training company invoices an Austrian company EUR 4,000 for a 3-day in-person training seminar held in Germany.
**Analysis:** If this is admission to an event (Art 53), place of supply = Germany (where the seminar takes place); Article 196 does not apply to that admission, and any domestic liability rule must be checked separately. However, if the seminar is a bespoke training service (not admission to an event open to the public), do not conclude Article 44 merely because registration is restricted; establish the actual admission/service facts before liability.
**Flag:** T2 -- determine whether the training qualifies as "admission to an event" (Art 53) or a bespoke B2B service (Art 44). In C-647/17 (Srf konsulterna), judgment of 13 March 2019, paragraphs 13-15 and 25-36, the Court included a 5-day accountancy/management course supplied solely to taxable persons within Article 53. Advance registration and payment did not exclude admission. Check the actual physical admission/service facts rather than assuming a closed professional course falls under Article 44. [Official judgment](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=ecli%3AECLI%3AEU%3AC%3A2019%3A195).


### Regression cases from the original test suite

### Test 1 -- Standard B2B consulting, MT to DE

**Input:** Maltese consultant (MT VAT number valid), German customer (DE VAT number valid via VIES), consulting service EUR 5,000.
**Expected:** Supplier: the national outgoing-services field (current Malta identifier reserved below) = EUR 5,000, no supplier VAT charge, ESL filed. Customer: KZ 46 = EUR 5,000, output VAT 19% = EUR 950, input VAT EUR 950.

### Test 2 -- B2C digital service, MT to DE

**Input:** Maltese company sells to a German private individual (no VAT number) an online course for EUR 200.
**Expected:** Reverse charge does NOT apply. If this is an automated electronically supplied course taxable in Germany, not an exempt supply or a qualifying Article 59c home-state supply, German standard VAT on EUR 200 is EUR 38 at 19%; eligible supplies can use OSS or require local registration. Establish seller facts and course classification before that conclusion. See `eu-oss-digital.md`.

### Test 3 -- Property-related service (Art 47 exception)

**Input:** French architect invoices a Belgian company EUR 10,000 for designing a building in Belgium.
**Expected:** Reverse charge under Art 196 does NOT apply. Place of supply = Belgium (Art 47). French architect may need to register for Belgian VAT or Belgian domestic reverse charge for construction services may apply. Flag T2.

### Test 4 -- Post-Brexit UK supplier to EU customer

**Input:** UK company invoices a Dutch company EUR 8,000 for IT consulting. UK company is not VAT-registered in any EU state.
**Expected:** For the stated ordinary IT-consulting service to the Dutch business, Article 44 locates the service in the Netherlands and Article 196 applies if the UK supplier is not established there for the supply and no exemption applies. UK status does not disqualify the EU-side reverse charge. See `non-eu-export-services.md`.

### Test 5 -- Customer's VAT number is invalid

**Input:** Italian company invoices a Spanish company EUR 3,000 for design services. Spanish VAT number fails VIES validation.
**Expected:** STOP for evidence resolution. An invalid VIES result does not alone establish B2C or Italian place of supply. Apply Regulation Article 18, including the pending-registration route where its conditions are met, then determine the actual place, rate, liability, invoice and statement. The old EUR 660 / EUR 3,660 outcome at 22% is not a valid automatic result.


### Recomputing cases and decision boundary

The example prices are inputs, not legal thresholds. The rate rows below are current standard-rate references used only for the stated ordinary taxable professional services; test any reduced rate, exemption, use-and-enjoyment rule or SME exemption before computing. Germany and France ordinary full-deduction examples have no net payment attributable to the service, but their output and eligible input entries are still required.

| Example destination | Standard rate | Conditions and source |
|---|---|---|
| Germany | 19% | Ordinary taxable consulting; UStG section 12(1): https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| France | 20% | Ordinary taxable software development, metropolitan France; 2026 CA3 notice: https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf |
| Malta | 18% (in words on the page) | Ordinary taxable legal services; Cap. 406 art 19(1): https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Slovakia | 23% | Ordinary taxable marketing; Act 222/2004 section 27(1): https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Sprievodca/Sprievodca_danami/2026/2026.01.13_DPH_2026.pdf |
| Italy | 22% | Ordinary taxable bookkeeping; official EU standard-rate table; national field/source detail still reserved: https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |

```oa-check
name: Malta consultant to fully taxable German business
inputs:
  fee: 5000
  rate: 0.19
  deductible_fraction: 1
steps:
  output_vat: fee * rate
  deductible_input: output_vat * deductible_fraction
  net_service_vat: output_vat - deductible_input
expected:
  output_vat: 950
  deductible_input: 950
  net_service_vat: 0
```

For the same qualifying supply, assume that a properly determined national deduction fraction is 40% rather than full deduction. This is an illustrative input, not a statutory deduction percentage or a free election. The customer still accounts for all output tax; choosing to deduct all of it would understate the service's net liability by EUR 570. Check the country's attribution, pro-rata, blocked-input and adjustment rules. Directive Articles 168, 173 and 178(f) govern the framework.

```oa-check
name: German recipient with established partial deduction
inputs:
  fee: 5000
  rate: 0.19
  permitted_fraction: 0.40
steps:
  output_vat: fee * rate
  deductible_input: output_vat * permitted_fraction
  payable_for_service: output_vat - deductible_input
  understatement_if_full_deduction: output_vat - deductible_input
expected:
  output_vat: 950
  deductible_input: 380
  payable_for_service: 570
  understatement_if_full_deduction: 570
```

## When to refuse or refer


- **Prohibition 1**  -  NEVER apply reverse charge to B2C transactions.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 2**  -  NEVER assume customer status from an unverified identifier; use the lawful Article 18 evidence routes and refer unresolved status.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 3**  -  NEVER skip a recapitulative-statement obligation that actually applies under Article 262(1)(c) and national procedure; do not invent one for an exempt service or non-EU supplier.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 4**  -  NEVER apply reverse charge to services falling under Art 45-59 exceptions without checking the specific place of supply rule.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 5**  -  NEVER infer EU-side liability from the UK's former EU membership: apply Article 44/196 to a non-established UK supplier where its actual conditions hold, and use UK law for UK-side liability.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 6**  -  NEVER assume reverse charge nets to zero for partially exempt businesses -- check the customer's input VAT recovery position.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).
- **Prohibition 7**  -  NEVER issue an invoice with domestic VAT when reverse charge applies -- this results in double taxation if the customer also self-assesses.  [VAT Directive](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1); [Implementing Regulation](https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1).


Refuse a filing conclusion when recipient status, business use, the receiving establishment, exemption, special place rule, supplier intervention or current local reporting fields remain unresolved. Retain the question and identify the country skill or professional review needed; do not turn missing evidence into domestic VAT by default.

## Filing and payment

For Article 196 services, Article 222 requires an invoice no later than the 15th day of the month after the chargeable event (in words on the page). Apply Article 226 content and the competent national invoice law, record the correct tax point, submit the actual national VAT return and any required services statement, retain receipt and payment reference, and reconcile self-assessed output with permitted input deduction. A zero net amount does not remove reporting. National procedures, deadlines, late-filing/late-payment penalties and interest are country-specific; unresolved fields are not completed by analogy. The exact national rates and service-specific relief must come from the country overlay.

## Completion checklist


**Step 7: Common Mistakes [T1]**  _([Step 7: Common Mistakes [T1]](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_

| # | Mistake | Correct Treatment |
| --- | --- | --- |
| 1 | Applying reverse charge to B2C supplies | Article 196 requires its recipient/service conditions; an exclusively private customer needs the applicable B2C place/exemption rules, not an automatic home-rate result.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 2 | Not reporting on the EC Sales List | Check Article 262(1)(c), including the exempt-in-customer-state exclusion, and national procedure. Non-filing triggers penalties.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 3 | Customer forgets to self-assess both output AND input VAT | Report the output liability and only the permitted input deduction. Zero net tax requires full same-period entitlement; omission of output can be a reporting defect even when eligible input offsets it.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 4 | Not verifying the customer's VAT number via VIES | Establish customer status under Regulation Article 18. Invalid VIES does not alone settle place, liability or the pending-registration evidence route.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 5 | Applying reverse charge to property-related services | Article 47 puts the service at the property. Article 196 does not determine liability, but national recipient liability can apply under Article 194.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 6 | Confusing "zero-rated" with "exempt" | Article 44 determines place and Article 196 liability; this is not a universal zero rate. Any exemption and the supplier's deduction entitlement need their own tests, including Article 169.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 7 | Applying reverse charge to post-Brexit UK transactions | For an EU recipient of an Article 44 service, Article 196 can apply to a non-established UK supplier. For a UK recipient use UK law. The original 2020 Brexit dates do not establish a supplier-location exclusion in Article 196.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| 8 | Customer in a partially exempt business not adjusting input VAT | Deduct only input attributable to deductible activities under the country's direct-attribution and mixed-use rules. A partly exempt business can still fully deduct a service used exclusively for eligible taxable supplies; exempt turnover alone does not fix this service's deduction fraction.  https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |


This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| VAT Directive, read for Articles 43-59c (place/status and exceptions), 64-66 (tax points), 168-178 (deduction framework), 192a-196 (liability), 214 (identification), 222/226 (invoicing), 262-264 (statements) | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 | 2026-11-14 |
| Implementing Regulation, read for Articles 18-24 (status/use/establishment), 31a-33 (property/events), 53-54 (supplier intervention) | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | 2026-11-14 |
| Germany UStG, read for section 12(1) standard rate and neighboring reduced-rate scope | https://www.gesetze-im-internet.de/ustg_1980/__12.html | 2026-11-14 |
| Germany ELSTER 2026, read for recipient-liability/outgoing-services and input-tax instructions | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_ustva_2026 | 2026-11-14 |
| France 2026 CA3 notice, read for service place/liability, DES, E2, A3, rate/output and deduction instructions | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf | 2026-11-14 |
| Malta Cap.406, read for Article 19 standard-rate scope; national return fields not confirmed | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-14 |
| Slovakia official 2026 Act, read for section 27 standard/reduced-rate scope | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Sprievodca/Sprievodca_danami/2026/2026.01.13_DPH_2026.pdf | 2026-11-14 |
| Slovakia DPHv25, read for recipient-liable services rate-specific rows and deduction aggregates | https://pfseform.financnasprava.sk/Formulare/eFormVzor/DP/form.616.html | 2026-11-14 |
| Slovakia tax-return guidance, read for exclusion of transactions with place outside Slovakia | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie | 2026-11-14 |
| EU Your Europe, read for all member-state standard rates and regional/rate-category warnings | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm | 2026-11-14 |
| Germany BMF 2026 forms, read for USt1A rows 30-35 and 41, the EU-established/other supplier branches and adjacent notes | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=7 | 2026-11-14 |
| France actual CA3 2026 form, read for A3/E2 and standard output 08/eligible service input 20; notice supplies the conditions | https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5377.pdf | 2026-11-14 |
| Italy IVA 2026 instructions, read for tax-period 2025 label and VE34/VF1-VF13/VJ3 with neighboring scope; 2025-2026 filing cycle only | https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 | 2026-11-14 |
| C-647/17 (Srf konsulterna), read for full judgment paragraphs 1-37 and operative part from official PDF text returned by web retrieval; fresh URL currently redirects to generic OJ | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=ecli%3AECLI%3AEU%3AC%3A2019%3A195 | 2026-11-14 |

Not yet confirmed: current Malta return identifiers and national service-statistics/ESL periods not expressly sourced here; Italian annual fields for tax period 2026 (the available IVA 2026 source is the 2025-2026 filing cycle); the old country-field cells below are retained solely as unresolved historical claims and are not filing instructions. The old generic ESL-penalty range EUR 50 to EUR 5,000+ has no established common EU legal basis and must not be used. National exemptions, including any qualifying SME exemption, VAT-group effects, deduction restrictions and use-and-enjoyment overlays must be checked for the actual case. No national field unsupported below is implied verified by the EU Directive.

### Preserved unresolved country cells from the original

- Not confirmed for 2026; old cell only: Malta (MT) ; Box 1 (EU supplies) ; Quarterly ESL to CFR
- Not confirmed for 2026; old cell only: Italy (IT) ; VE34 (operazioni non soggette per carenza del requisito di territorialità) ; Elenchi Intrastat servizi, monthly or quarterly
- Not confirmed for 2026; old cell only: Malta (MT) ; Box 9a (EU services) ; Box 3 / Box 6 ; Box 13a ; Zero (if fully taxable)
- Not confirmed for 2026; old cell only: Italy (IT) ; VJ3 (acquisti di beni e servizi da soggetti residenti all'estero) ; VJ3 (output) ; VF1-VF13 by rate (input) ; Zero (if fully taxable)

Confirmed corrections: the old Slovakia supplier row 15 and recipient rows 11/12/output 11/12/input 20 are replaced in usable instructions by the opened current form and authority guidance above. The old post-Brexit exclusion and zero-rate terminology are corrected in the same topics, not silently carried into the unresolved field register.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eu-reverse-charge` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eu-reverse-charge. If neither is available, confirm every figure against the official source pages cited above before relying on it.
