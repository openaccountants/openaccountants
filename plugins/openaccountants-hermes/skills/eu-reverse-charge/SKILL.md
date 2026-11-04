---
name: eu-reverse-charge
description: "Use this skill whenever a cross-border B2B service transaction occurs between EU member states and the question is whether the reverse charge mechanism under Article 196 of the VAT Directive applies. Trigger on phrases like \"reverse charge\", \"B2B services EU\", \"intra-community services\", \"Article 196\", \"EC Sales List\", \"self-assess VAT\", \"cross-border VAT EU\", or any request involving the VAT treatment of services supplied between businesses in different EU countries. This skill contains the complete decision logic for determining when reverse charge applies, how the supplier and customer each report it, the EC Sales List obligations, and the country-specific box mappings that link back to each country's VAT return skill. ALWAYS read this skill before classifying any intra-EU B2B service transaction."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/eu-reverse-charge"
  jurisdiction: "GLOBAL"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# EU Reverse Charge

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | EU (all 27 member states) |
| Primary Legislation | Council Directive 2006/112/EC, Articles 44, 45, 56, 196 |
| Supporting Legislation | Council Implementing Regulation (EU) No 282/2011; Regulation (EU) No 904/2010 (admin cooperation / VIES) |
| Scope | B2B services between EU member states where place of supply shifts to the customer's country |
| Contributor | OpenAccountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard B2B service reverse charge, ESL reporting, supplier zero-rating. Tier 2: Art 45 exceptions (land, events, transport), mixed B2B/B2C supplies. Tier 3: complex group structures, PE-based place of supply, triangulation. |
| Cross-references | `malta-vat-return.md`, `germany-vat-return.md`, `france-vat-return.md`, `italy-vat-return.md`, `uk-vat-return.md`, `slovakia-vat-return.md`, `eu-vat-directive.md` |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a qualified accountant and document the gap.

## Step 0: Pre-Check Questions [T1]

- **Pre-check question 1: supplier VAT registration** — Is the supplier VAT-registered in an EU member state? If no, this skill does not apply (see `non-eu-export-services.md` or consider non-Union OSS).  _(Step 0: Pre-Check Questions [T1])_
- **Pre-check question 2: customer VAT registration in different state** — Is the customer VAT-registered in a DIFFERENT EU member state? If same country, this is a domestic transaction -- use the relevant country skill.  _(Step 0: Pre-Check Questions [T1])_
- **Pre-check question 3: customer is a business (B2B)** — Is the customer a business (B2B)? Confirmed by a valid VAT identification number verifiable via VIES. If the customer is a private individual (B2C), reverse charge does NOT apply -- the supplier charges their own country's VAT (or uses OSS; see `eu-oss-digital.md`).  _(Step 0: Pre-Check Questions [T1])_
- **Pre-check question 4: nature of the service** — What is the nature of the service? Needed to check Art 44/45 exceptions.  _(Step 0: Pre-Check Questions [T1])_
- **Stop condition for unknown pre-checks** — If items 1-3 are unknown, STOP. Do not classify the transaction.  _(Step 0: Pre-Check Questions [T1])_

## Step 1: Decision Tree -- Does Reverse Charge Apply? [T1]

**Legislation:** VAT Directive Art 44 (general B2B rule), Art 45 (general B2C rule), Art 46-59 (specific exceptions), Art 196 (reverse charge obligation).

### Decision Tree Table

**Decision Tree Table**  _([Step 1: Decision Tree -- Does Reverse Charge Apply? [T1]](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_

| Step | Question | If YES | If NO |
| --- | --- | --- | --- |
| 1 | Is the customer a taxable person (business) acting as such? Verify via VIES. | Go to Step 2 | **STOP.** B2C rules apply. Supplier charges own VAT rate or uses OSS. Reverse charge does NOT apply. |
| 2 | Is the supplier established in a different EU member state from the customer? | Go to Step 3 | **STOP.** Domestic supply. Use country-specific skill. |
| 3 | Is the service related to immovable property (land, buildings)? Art 47. | **STOP.** Place of supply = where property is located. No reverse charge. Supplier may need to register in that country. [T2] | Go to Step 4 |
| 4 | Is the service admission to a cultural, artistic, sporting, scientific, educational, or entertainment event attended in person? Art 53 (Art 53 does not apply where the attendance is virtual). | **STOP.** Place of supply = where event takes place. No reverse charge. [T2] | Go to Step 5 |
| 5 | Is the service short-term hire of a means of transport (<=30 days, <=90 days for vessels)? Art 56(1). | **STOP.** Place of supply = where vehicle put at disposal. No reverse charge. [T2] | Go to Step 6 |
| 6 | Is the service restaurant/catering on board transport (ship, plane, train) within EU? Art 57. | **STOP.** Place of supply = point of departure. No reverse charge. [T2] | Go to Step 7 |
| 7 | Is the service passenger transport? Art 48. | **STOP.** Place of supply = where transport takes place proportionally. No reverse charge. [T2] | Go to Step 8 |
| 8 | **Reverse charge applies.** Place of supply = customer's country under Art 44. Customer self-assesses VAT under Art 196. Supplier invoices without VAT. | -- | -- |

### Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2]

**Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2]**  _(Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2])_

| Exception | Article | Place of Supply |
| --- | --- | --- |
| Immovable property services | Art 47 | Location of property |
| Passenger transport | Art 48 | Where transport takes place |
| Goods transport (B2C only) | Art 49 | Where transport takes place |
| Cultural/sporting/educational event admission | Art 53 | Where event takes place |
| Restaurant and catering | Art 55 | Where physically carried out |
| Short-term hire of transport | Art 56(1) | Where put at disposal |
| Restaurant/catering on board transport | Art 57 | Point of departure |

- **Flag exceptions as T2** — If the service falls into any exception above, flag as [T2] and determine place of supply under the specific article. Do not apply reverse charge.  _(Summary of Art 44/45 Exceptions (Services NOT Subject to Standard B2B Reverse Charge) [T2])_

## Step 2: How the Supplier Treats It [T1]

- **Invoice without VAT** — The supplier's invoice must show EUR 0.00 VAT.  _(Step 2: How the Supplier Treats It [T1])_
- **Required invoice notation** — Include the notation: "Reverse charge -- Article 196 of Council Directive 2006/112/EC" or equivalent national wording.  _(Step 2: How the Supplier Treats It [T1])_
- **Include both VAT numbers** — Include both VAT numbers: Supplier's own VAT number AND customer's VAT number (verified via VIES).  _(Step 2: How the Supplier Treats It [T1])_
- **Report on EC Sales List (ESL)** — The supply of services must be reported on the EC Sales List (also called "Recapitulative Statement") for the relevant period. Report the customer's VAT number and the total value of services supplied.  _(Step 2: How the Supplier Treats It [T1])_
- **Report on the VAT return** — The supply appears as a zero-rated / out-of-scope B2B EU sale. The specific box depends on the supplier's country.  _(Step 2: How the Supplier Treats It [T1])_

### Supplier-Side Country Box Mappings [T1]

**Supplier-Side Country Box Mappings [T1]**  _([Supplier-Side Country Box Mappings [T1]](https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf))_

| Supplier Country | VAT Return Box for EU B2B Services | ESL Filing |
| --- | --- | --- |
| Malta (MT) | Box 1 (EU supplies) | Quarterly ESL to CFR |
| Germany (DE) | Kennziffer 21 (nicht steuerbare sonstige Leistungen gemäß § 18b Satz 1 Nummer 2 UStG) | Zusammenfassende Meldung (ZM), monthly or quarterly |
| France (FR) | Line E2 (autres opérations non imposables) | Etat récapitulatif (DES), monthly |
| Italy (IT) | VE34 (operazioni non soggette per carenza del requisito di territorialità) | Elenchi Intrastat servizi, monthly or quarterly |
| Slovakia (SK) | Row 15 (services Art 15(10) of Slovak VAT Act) | Quarterly ESL (Súhrnný výkaz) |
| UK | N/A -- UK left the EU on 31 January 2020. Reverse charge between UK and EU does NOT apply under Art 196. See `non-eu-export-services.md`. | N/A |

*For countries not listed above, refer to the country-specific VAT return skill or escalate [T2].*

## Step 3: How the Customer Treats It [T1]

- **Self-assess output VAT** — Self-assess output VAT at the customer's domestic standard rate on the net value of the service.  _(Step 3: How the Customer Treats It [T1])_
- **Simultaneously claim input VAT** — Simultaneously claim input VAT (same amount, same return) if the service is used for taxable supplies and is not in a blocked category.  _(Step 3: How the Customer Treats It [T1])_
- **Net effect for fully taxable business** — Net effect = zero for a fully taxable business. But both sides MUST appear on the VAT return.  _(Step 3: How the Customer Treats It [T1])_
- **Report on Intrastat / acquisition section** — Report on Intrastat / acquisition section of the VAT return if required by the member state.  _(Step 3: How the Customer Treats It [T1])_

### Customer-Side Country Box Mappings [T1]

**Customer-Side Country Box Mappings [T1]**  _([Customer-Side Country Box Mappings [T1]](https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf))_

| Customer Country | Acquisition Box (Net) | Output VAT Box | Input VAT Box | Net Effect |
| --- | --- | --- | --- | --- |
| Malta (MT) | Box 9a (EU services) | Box 3 / Box 6 | Box 13a | Zero (if fully taxable) |
| Germany (DE) | KZ 46 (sonst. Leistungen eines im anderen EU-Land ansässigen Unternehmers) | KZ 47 | KZ 67 (Vorsteuer) | Zero (if fully taxable) |
| France (FR) | Line A3 (achats de prestations de services fournies par un prestataire non établi en France) | Line 08/09 | Line 20 | Zero (if fully taxable) |
| Italy (IT) | VJ3 (acquisti di beni e servizi da soggetti residenti all'estero) | VJ3 (output) | VF1-VF13 by rate (input) | Zero (if fully taxable) |
| Slovakia (SK) | Row 11/12 (nadobudnutie z EU) | Row 11/12 output | Row 20 input | Zero (if fully taxable) |

## Step 4: EC Sales List (ESL) Requirements [T1]

- **Who must file** — Any VAT-registered business that supplies services to a business in another EU member state where reverse charge applies under Art 196.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_
- **What to report** — Customer's VAT identification number + total value of services for the period.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_
- **Frequency** — Monthly under VAT Directive Art 263(1); member states may allow a quarterly statement for services (Art 263(1c)) (e.g., France monthly DES for services).  _([Regulation (EU) No 904/2010; VAT Directive Art 262-263.](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_
- **Deadline** — Varies by member state, within a period not exceeding one month (VAT Directive Art 263); check the national deadline, which can be shorter.  _([Regulation (EU) No 904/2010; VAT Directive Art 262-263.](https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1))_
- **Penalty for non-filing** — Varies by member state. Can range from EUR 50 to EUR 5,000+ per missed filing.  _(Regulation (EU) No 904/2010; VAT Directive Art 262-263.)_

### Critical Rule [T1]

- **Non-filing does not change VAT treatment** — Failure to file the ESL does NOT change the VAT treatment. The reverse charge still applies. But non-filing triggers penalties and may cause the customer's tax authority to query the acquisition.  _(Critical Rule [T1])_

## Step 5: VIES Validation [T1]

- **VIES verification requirement** — Before applying reverse charge, the supplier MUST verify the customer's VAT number via the VIES (VAT Information Exchange System) database: https://ec.europa.eu/taxation_customs/vies/  _(Step 5: VIES Validation [T1])_
- **VIES confirms valid** — If VIES confirms the number is valid: proceed with reverse charge.  _(Step 5: VIES Validation [T1])_
- **VIES shows invalid** — If VIES shows the number is invalid: DO NOT apply reverse charge. Charge domestic VAT. Advise the customer to resolve their VAT registration.  _(Step 5: VIES Validation [T1])_
- **VIES temporarily unavailable** — If VIES is temporarily unavailable: document the attempt. Retry. If consistently unavailable, apply reverse charge but retain evidence of the check attempt.  _(Step 5: VIES Validation [T1])_

## Step 6: Worked Examples

### Example 1 -- Standard consulting, MT supplier to DE customer [T1]

**Facts:** Maltese VAT-registered consultant invoices a German company (valid DE VAT number) EUR 5,000 for management consulting.
**Analysis:** B2B, general service (Art 44 applies), no exceptions. Reverse charge applies.
**Supplier (MT):** Invoice EUR 5,000, 0% VAT, notation "Reverse charge Art 196". Report in Box 1. Report on ESL.
**Customer (DE):** Self-assess 19% output VAT = EUR 950 (KZ 47). Claim EUR 950 input VAT (KZ 67). Net = zero.

### Example 2 -- Software development, DE supplier to FR customer [T1]

**Facts:** German freelance developer invoices a French company (valid FR VAT number) EUR 10,000 for custom software development.
**Analysis:** B2B, general service under Art 44, no exceptions. Reverse charge applies.
**Supplier (DE):** Invoice EUR 10,000, 0% VAT. Report in KZ 21. File ZM (ESL).
**Customer (FR):** Self-assess 20% output VAT = EUR 2,000 (Line 08/09). Claim EUR 2,000 input VAT (Line 20). Net = zero.

### Example 3 -- Legal services, IT supplier to MT customer [T1]

**Facts:** Italian law firm invoices a Maltese company (valid MT VAT number) EUR 3,000 for legal advice on a contract.
**Analysis:** B2B, general service under Art 44. Legal services are not in Art 45 exceptions. Reverse charge applies.
**Supplier (IT):** Invoice EUR 3,000, 0% VAT, "inversione contabile Art 196". Report in VE34. File Intrastat.
**Customer (MT):** Box 9a = EUR 3,000. Box 6 = EUR 540 (18%). Box 13a = EUR 540. Net = zero.

### Example 4 -- Architectural services for property in France, MT supplier to DE customer [T2]

**Facts:** Maltese architect invoices a German company EUR 8,000 for designing a building located in France.
**Analysis:** Service related to immovable property (Art 47). Place of supply = France (where the property is). Reverse charge under Art 196 does NOT apply. The Maltese supplier may need to register for VAT in France and charge French VAT at 20%.
**Flag:** T2 -- reviewer must confirm whether French VAT registration is required or whether the customer can self-assess under French domestic reverse charge rules for construction services.

### Example 5 -- Conference admission in Spain, FR supplier to NL customer [T2]

**Facts:** French event organiser sells admission tickets (EUR 500) for a conference in Spain to a Dutch company.
**Analysis:** Admission to an event (Art 53). Place of supply = Spain. Standard reverse charge does NOT apply. Supplier may need to charge Spanish VAT or register in Spain.
**Flag:** T2 -- escalate to determine whether the French organiser must register in Spain.

### Example 6 -- Marketing services, NL supplier to SK customer [T1]

**Facts:** Dutch marketing agency invoices a Slovak company (valid SK VAT number) EUR 15,000 for digital marketing campaign.
**Analysis:** B2B, general service (Art 44), no exceptions. Reverse charge applies.
**Supplier (NL):** Invoice EUR 15,000, 0% VAT. Report on ESL. Report as intracommunautaire dienst on Dutch return.
**Customer (SK):** Row 11/12 = EUR 15,000. Output VAT at 23% = EUR 3,450. Input VAT = EUR 3,450. Net = zero.

### Example 7 -- Accounting services, MT supplier to IT customer [T1]

**Facts:** Maltese CPA invoices an Italian company (valid IT VAT number) EUR 2,000 for bookkeeping services.
**Analysis:** B2B, general service under Art 44. No exceptions. Reverse charge applies.
**Supplier (MT):** Invoice EUR 2,000, 0% VAT. Box 1 = EUR 2,000. Report on ESL.
**Customer (IT):** Self-assess at 22% = EUR 440 output. Claim EUR 440 input. Net = zero.

### Example 8 -- Training seminar (in-person), DE supplier to AT customer [T2]

**Facts:** German training company invoices an Austrian company EUR 4,000 for a 3-day in-person training seminar held in Germany.
**Analysis:** If this is admission to an event (Art 53), place of supply = Germany (where seminar takes place) -- no reverse charge. However, if the seminar is a bespoke training service (not admission to an event open to the public), then Art 44 applies and reverse charge applies.
**Flag:** T2 -- determine whether the training qualifies as "admission to an event" (Art 53) or a bespoke B2B service (Art 44). The CJEU in case C-647/17 (Srf konsulterna) held that a five-day course on accountancy and management supplied solely to taxable persons and requiring advance registration and payment is admission to an event under Art 53, not a general Art 44 service.

## Step 7: Common Mistakes [T1]

**Step 7: Common Mistakes [T1]**  _([Step 7: Common Mistakes [T1]](https://publications.europa.eu/resource/cellar/6b06c8b6-43f0-11ea-b81b-01aa75ed71a1.0006.03/DOC_1))_

| # | Mistake | Correct Treatment |
| --- | --- | --- |
| 1 | Applying reverse charge to B2C supplies | Reverse charge ONLY applies to B2B (Art 196). For B2C, supplier charges own country's VAT or uses OSS. |
| 2 | Not reporting on the EC Sales List | ESL filing is mandatory for all intra-EU B2B services where reverse charge applies. Non-filing triggers penalties. |
| 3 | Customer forgets to self-assess both output AND input VAT | BOTH sides must appear on the return. Missing the output side means undeclared VAT liability. |
| 4 | Not verifying the customer's VAT number via VIES | VIES verification is required. Invalid number = no reverse charge = must charge domestic VAT. |
| 5 | Applying reverse charge to property-related services | Art 47 exception: place of supply = where property is located. Reverse charge does NOT apply. |
| 6 | Confusing "zero-rated" with "exempt" | Intra-EU B2B services under reverse charge are zero-rated (supplier retains input VAT recovery). They are NOT exempt supplies. |
| 7 | Applying reverse charge to post-Brexit UK transactions | UK is not an EU member state since 31 January 2020. Art 196 does not apply to UK-EU transactions after the transition period ended on 31 December 2020. |
| 8 | Customer in a partially exempt business not adjusting input VAT | If the customer makes exempt supplies, they cannot fully recover the self-assessed input VAT. Partial exemption rules of the customer's country apply. |

## PROHIBITIONS

- **Prohibition 1** — NEVER apply reverse charge to B2C transactions.  _(PROHIBITIONS)_
- **Prohibition 2** — NEVER apply reverse charge without verifying the customer's VAT number via VIES.  _(PROHIBITIONS)_
- **Prohibition 3** — NEVER skip the EC Sales List filing obligation when reverse charge applies.  _(PROHIBITIONS)_
- **Prohibition 4** — NEVER apply reverse charge to services falling under Art 45-59 exceptions without checking the specific place of supply rule.  _(PROHIBITIONS)_
- **Prohibition 5** — NEVER apply reverse charge to transactions involving the UK (post-Brexit).  _(PROHIBITIONS)_
- **Prohibition 6** — NEVER assume reverse charge nets to zero for partially exempt businesses -- check the customer's input VAT recovery position.  _(PROHIBITIONS)_
- **Prohibition 7** — NEVER issue an invoice with domestic VAT when reverse charge applies -- this results in double taxation if the customer also self-assesses.  _(PROHIBITIONS)_

## Edge Cases

### EC1 -- Customer has a VAT number but is a non-taxable legal person [T2]

**Situation:** The customer has a VAT identification number (e.g., for intra-EU goods acquisitions) but is not a taxable person acting as such (e.g., a government body, a holding company with no economic activity).
**Resolution:** Art 44 requires the customer to be a "taxable person acting as such." A non-taxable legal person with a VAT number for goods acquisitions may not qualify. Flag for reviewer. In most cases, if the customer has an active VAT number verified via VIES, reverse charge applies.

### EC2 -- Supplier has a fixed establishment in the customer's country [T2]

**Situation:** A German company supplying services to a French customer also has a fixed establishment (branch) in France. Does the French branch trigger domestic treatment instead of reverse charge?
**Resolution:** If the French fixed establishment is NOT involved in the supply, reverse charge still applies (Art 44; Art 192a of the VAT Directive + Implementing Regulation Art 53). If the fixed establishment IS involved, the supply is domestic. Flag for reviewer to determine which establishment is making the supply.

### EC3 -- Chain of services (intermediary) [T2]

**Situation:** Company A (MT) supplies a service to Company B (DE), who re-supplies it to Company C (FR). Who applies reverse charge?
**Resolution:** Each link in the chain is treated independently. A→B: reverse charge applies (MT→DE). B→C: reverse charge applies (DE→FR). Each supplier reports on their respective ESL. Flag for reviewer if the intermediary's involvement is unclear.

### EC4 -- Services straddling B2B and B2C (mixed customer) [T2]

**Situation:** A customer is both a business and a private individual (e.g., a sole trader purchasing services partly for business, partly for personal use).
**Resolution:** If the customer provides their VAT number and the service is for their business activity, reverse charge applies. If the purchase is for personal use (even by a VAT-registered person), it is B2C. Flag for reviewer to confirm the business purpose.

### EC5 -- Continuous services spanning multiple periods [T1]

**Situation:** A monthly retainer service (e.g., EUR 2,000/month) is invoiced quarterly at EUR 6,000.
**Resolution:** Reverse charge applies to each tax point. The tax point for continuous services is typically the end of each billing period or the date of payment, whichever is earlier (Art 64 of the VAT Directive). Report in the period in which the tax point falls. ESL reporting follows the same period.

## Test Suite

### Test 1 -- Standard B2B consulting, MT to DE

**Input:** Maltese consultant (MT VAT number valid), German customer (DE VAT number valid via VIES), consulting service EUR 5,000.
**Expected:** Supplier: Box 1 = EUR 5,000, 0% VAT, ESL filed. Customer: KZ 46 = EUR 5,000, output VAT 19% = EUR 950, input VAT EUR 950.

### Test 2 -- B2C digital service, MT to DE

**Input:** Maltese company sells to a German private individual (no VAT number) an online course for EUR 200.
**Expected:** Reverse charge does NOT apply. Supplier charges German VAT rate 19% = EUR 38 via OSS (if registered) or registers in Germany. See `eu-oss-digital.md`.

### Test 3 -- Property-related service (Art 47 exception)

**Input:** French architect invoices a Belgian company EUR 10,000 for designing a building in Belgium.
**Expected:** Reverse charge under Art 196 does NOT apply. Place of supply = Belgium (Art 47). French architect may need to register for Belgian VAT or Belgian domestic reverse charge for construction services may apply. Flag T2.

### Test 4 -- Post-Brexit UK supplier to EU customer

**Input:** UK company invoices a Dutch company EUR 8,000 for IT consulting. UK company is not VAT-registered in any EU state.
**Expected:** Art 196 reverse charge does NOT apply (UK is not EU). The Dutch company may still need to self-assess Dutch VAT under Dutch domestic rules for services received from outside the EU. See `non-eu-export-services.md`.

### Test 5 -- Customer's VAT number is invalid

**Input:** Italian company invoices a Spanish company EUR 3,000 for design services. Spanish VAT number fails VIES validation.
**Expected:** Reverse charge does NOT apply. Italian supplier must charge Italian VAT at 22% = EUR 660. Invoice total = EUR 3,660. No ESL filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `eu-reverse-charge` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/eu-reverse-charge. If neither is available, confirm every figure against the official source pages cited above before relying on it.
