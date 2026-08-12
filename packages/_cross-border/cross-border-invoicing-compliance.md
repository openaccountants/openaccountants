---
name: cross-border-invoicing-compliance
description: "Cross-border invoicing rules — which country's requirements apply, what goes on the invoice, and how to handle e-invoicing mandates. Use when the user asks about: cross-border invoice, invoicing foreign client, reverse charge invoice, multi-currency invoice, self-billing cross-border, credit note cross-border, e-invoicing cross-border, which invoicing rules apply, Article 219a, supplier country invoicing, Italy SDI foreign, India IRN cross-border, Mexico CFDI foreign, invoice retention cross-border, archiving invoices, ECB exchange rate, VAT currency conversion, recipient-created invoice, or any question about the correct format, content, or process for invoices crossing borders."
version: 1.0
jurisdiction: INTL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross Border Invoicing Compliance

## Cross-Border Invoicing Compliance

> **Disclaimer:** This skill provides general guidance on cross-border invoicing rules. Invoice requirements are jurisdiction-specific and evolving rapidly due to e-invoicing mandates. Consult a qualified advisor before relying on this information for compliance.

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Multi-jurisdiction (EU, UK, US, India, Italy, Mexico, and general principles) |
| Primary Legislation | EU: VAT Directive 2006/112/EC, Articles 217–240; Art 219a (invoicing rules applicable); ViDA Directive (phased 2028–2035) |
| Scope | Invoice format, content, currency, e-invoicing, and archiving requirements for cross-border transactions |
| Contributor | OpenAccountants |
| Validation Date | May 2026 |
| Skill Version | 1.0 |
| Cross-references | `eu-reverse-charge.md`, `vat-place-of-supply-master.md`, `eu-oss-digital.md`, country-specific e-invoicing skills |

## Section 1: General Principle — Whose Rules Govern the Invoice?

### The Basic Rule — Article 219a(1) [T1]

- **Basic invoicing rule** — Invoicing follows the rules of the Member State where the supply is deemed to take place (i.e., the place-of-supply country).  _(Article 219a(1))_

### The Exceptions — Article 219a(2) [T1]

**The Exceptions — Article 219a(2)**  _(Article 219a(2))_

| Exception | When It Applies | Whose Rules |
| --- | --- | --- |
| **(a) Reverse charge — supplier not established in supply country** | B2B intra-EU services where customer self-assesses VAT (Art 196) | **Supplier's** country sets the invoicing rules |
| **(b) Supply outside the EU** | Services deemed supplied outside the EU | **Supplier's** country sets the invoicing rules |
| **Self-billing under reverse charge** | Customer issues the invoice on behalf of the supplier | Place-of-supply country's rules apply (basic rule) |
| **Non-EU supplier making taxable supplies in EU** | Non-EU seller with EU-taxable transactions | Place-of-supply country's rules always apply (no exception) |

### Practical Impact [T1]

**Practical Impact**

| Scenario | Whose Invoicing Rules? |
| --- | --- |
| German consultant invoices French company (B2B reverse charge) | **Germany** (supplier's rules — exception (a)) |
| French company sells goods domestically | **France** (place of supply = France) |
| Italian company invoices US client for consulting | **Italy** (supply outside EU — exception (b)) |
| US company sells SaaS to French consumer via non-Union OSS | **France** (place of supply = France; non-EU supplier — no exception) |
| Dutch company issues self-billing invoice for services received from Malta under reverse charge | **Netherlands** (self-billing under reverse charge = basic rule) |

## Section 2: EU Cross-Border Invoicing (Intra-EU B2B)

### Mandatory Invoice Content for Intra-EU B2B Under Reverse Charge [T1]

**Mandatory Invoice Content for Intra-EU B2B Under Reverse Charge**  _(VAT Directive Art 226)_

| Element | Requirement |
| --- | --- |
| Invoice number | Sequential, unique |
| Date of issue | Date the invoice is created |
| Date of supply | Date the service was performed or goods delivered (if different from issue date) |
| Supplier identification | Full name, address, VAT identification number |
| Customer identification | Full name, address, **VAT identification number** (verified via VIES) |
| Description | Nature and quantity of goods supplied or extent and nature of services |
| Taxable amount | Net amount in the agreed currency |
| VAT rate | N/A for reverse charge (0%) |
| VAT amount | EUR 0.00 or blank |
| **Reverse charge notation** | **Mandatory.** Must state "Reverse charge" or equivalent in the relevant language |
| Reference to legislation | "Article 196, Council Directive 2006/112/EC" or national equivalent |

### Reverse Charge Notation by Country [T1]

**Reverse Charge Notation by Country**

| Country | Notation |
| --- | --- |
| English | "Reverse charge — Article 196, Council Directive 2006/112/EC" |
| German | "Steuerschuldnerschaft des Leistungsempfängers — § 13b UStG" |
| French | "Autoliquidation — Article 196, Directive 2006/112/CE" |
| Italian | "Inversione contabile — Art. 196, Direttiva 2006/112/CE" |
| Spanish | "Inversión del sujeto pasivo — Artículo 196, Directiva 2006/112/CE" |
| Dutch | "BTW verlegd — Artikel 196, Richtlijn 2006/112/EG" |
| Portuguese | "Autoliquidação — Artigo 196.º, Diretiva 2006/112/CE" |

### Time Limits for Issuing Invoices [T1]

- **General EU deadline** — The VAT Directive requires invoices to be issued by the 15th of the month following the month in which the supply took place. Individual member states may impose shorter deadlines.  _(Art 222)_

### Time Limits for Issuing Invoices [T1]

**Time Limits for Issuing Invoices by Country**

| Country | Deadline |
| --- | --- |
| Germany | Immediately, but no later than 6 months after supply (§14 UStG) |
| France | By the 15th of the following month |
| Italy | By the 15th of the following month (12th for immediate invoices) |
| Spain | By the 15th of the following month |
| Netherlands | Before the 15th of the following month |
| Belgium | By the 15th of the following month |

## Section 3: Reverse Charge Invoice Requirements

### What Changes on the Invoice When Reverse Charge Applies [T1]

**What Changes on the Invoice When Reverse Charge Applies**

| Normal Invoice | Reverse Charge Invoice |
| --- | --- |
| Shows VAT rate (e.g., 19%) | Shows 0% or no VAT line |
| Shows VAT amount (e.g., EUR 950) | Shows EUR 0.00 or omits VAT amount |
| No special notation needed | **Must include reverse charge notation** |
| Only supplier's VAT number required | **Both** supplier and customer VAT numbers required |
| Customer pays gross amount | Customer pays net amount only |

### Customer's Obligations Upon Receiving a Reverse Charge Invoice [T1]

- **Customer obligations on receipt of reverse charge invoice** — 1. Self-assess output VAT at local rate on the net amount. 2. Claim input VAT on the same return (if entitled — fully taxable business). 3. Both entries must appear on the VAT return (see eu-reverse-charge.md for box mappings). 4. Report on Intrastat / acquisition reporting if required by the member state.  _(eu-reverse-charge.md)_

### Common Mistakes [T1]

**Common Mistakes**

| Mistake | Consequence |
| --- | --- |
| Supplier charges domestic VAT instead of reverse charge | Customer pays VAT they shouldn't. Double taxation risk if customer also self-assesses. Supplier must issue credit note. |
| Missing reverse charge notation | Invoice does not meet legal requirements. Customer's tax authority may deny input VAT deduction. |
| Customer's VAT number not on invoice | Cannot prove B2B nature. Tax authority may reclassify as B2C. |
| Supplier doesn't verify VAT number via VIES | If number is invalid, reverse charge does not apply. Supplier liable for domestic VAT. |

## Section 4: Multi-Currency Invoicing

### Which Currency for VAT Calculation? [T1]

**Which Currency for VAT Calculation?**  _(VAT Directive Art 230)_

| Jurisdiction | Rule |
| --- | --- |
| **EU (VAT Directive Art 230)** | VAT amount must be expressed in the currency of the Member State where the supply takes place. If invoiced in a foreign currency, convert using ECB rate or national customs rate. |
| **ECB exchange rate** | Use the rate on the **date of the chargeable event** (typically date of supply). Alternatively, some member states accept the rate on the date of invoice. |
| **UK** | HMRC accepts the rate at the date of supply. Use HMRC, ECB, or a reputable financial source. |
| **US** | No VAT — but for sales tax, use the exchange rate on the date of transaction. |

### Practical Guidance for Multi-Currency Invoices [T1]

**Practical Guidance for Multi-Currency Invoices**

| Element | Best Practice |
| --- | --- |
| Invoice currency | Invoice in whatever currency the contract specifies (USD, GBP, EUR, etc.) |
| VAT amount | Convert to the local currency using the applicable exchange rate |
| Exchange rate source | ECB daily rate (EU), HMRC rate (UK), Federal Reserve rate (US) |
| Document the rate | State the exchange rate and source on the invoice or in your records |
| Consistency | Use the same exchange rate source consistently — switching sources can trigger audit queries |

### OSS Returns and Currency [T1]

**OSS Returns and Currency**

| Scheme | Currency Required |
| --- | --- |
| Union OSS / Non-Union OSS | EUR. If your MSI doesn't use EUR, convert at ECB rate on the last day of the quarter. |
| IOSS | EUR |
| Domestic VAT return | Local currency of the member state |

## Section 5: Self-Billing / Recipient-Created Invoices Cross-Border

### What Is Self-Billing? [T1]

- **Self-billing / recipient-created tax invoice** — Self-billing (or recipient-created tax invoice) is where the customer issues the invoice on behalf of the supplier. This is permitted under Art 224 of the VAT Directive, subject to conditions.  _(Art 224, VAT Directive)_

### Conditions for Self-Billing [T1]

**Conditions for Self-Billing**

| Condition | Requirement |
| --- | --- |
| Prior agreement | Supplier and customer must have a **written agreement** that the customer will issue invoices on the supplier's behalf |
| Acceptance procedure | There must be a mechanism for the supplier to accept or reject each invoice |
| Invoicing rules | Follow the rules of the **place-of-supply** country (Art 219a basic rule applies to self-billing under reverse charge) |

### Cross-Border Self-Billing [T2]

**Cross-Border Self-Billing**

| Scenario | Whose Rules? |
| --- | --- |
| Dutch customer self-bills for services received from Italian supplier (reverse charge) | **Netherlands** (place of supply = Netherlands; self-billing under reverse charge follows basic rule, not supplier's rules) |
| US customer self-bills for services from German supplier | **Germany** (supply outside EU — exception (b) — supplier's rules) |

### Common Use Cases

- Large retailers issuing invoices to many small suppliers
- Royalty payments where recipient calculates the amount
- Commission arrangements where the principal issues invoices to agents

## Section 6: Credit Notes and Corrections Cross-Border

### When to Issue a Credit Note [T1]

**When to Issue a Credit Note**

| Trigger | Action |
| --- | --- |
| Price reduction after supply | Issue credit note referencing original invoice |
| Return of goods | Issue credit note for returned items |
| Invoice error (wrong amount, wrong VAT) | Issue credit note + new corrected invoice |
| Retrospective discount (e.g., volume rebate) | Issue credit note at end of period |

### Credit Note Requirements (EU) [T1]

**Credit Note Requirements (EU)**  _(VAT Directive Art 219)_

| Element | Requirement |
| --- | --- |
| Format | "Any document or message that amends and refers specifically and unambiguously to the initial invoice" |
| Reference | Must cite the original invoice number and date |
| Content | Corrected amounts, including VAT adjustments |
| Reverse charge credit notes | Same reverse charge notation as original. Customer must reverse their self-assessment. |

### Cross-Border Credit Note Complications [T2]

**Cross-Border Credit Note Complications**

| Issue | Guidance |
| --- | --- |
| Different reporting periods | Credit note may fall in a different quarter from the original invoice. Report in the period the credit note is issued. |
| OSS corrections | Corrections to previous OSS quarters are made on the **next** regular quarterly return (not by amending the original). |
| Currency differences | If exchange rate has changed since the original invoice, use the rate at the date of the credit note for the adjustment. |
| Customer in a different country has already filed | Customer must adjust their VAT return in the period the credit note is received. |

## Section 7: Country-Specific E-Invoicing Quirks

### Italy — SDI (Sistema di Interscambio) [T1]

**Italy — SDI (Sistema di Interscambio)**

| Element | Rule |
| --- | --- |
| Mandate | All Italian-established businesses must issue e-invoices via SDI (since 2019 for domestic; since July 2022 for cross-border) |
| Cross-border sales | Italian businesses must submit an XML e-invoice to SDI even when invoicing foreign customers. The Esterometro was abolished in 2022; replaced by SDI reporting. |
| Format | FatturaPA XML format. SDI validates the invoice before forwarding. |
| Foreign supplier selling to Italy | Not required to use SDI (unless established in Italy). The Italian buyer self-assesses VAT and reports via SDI using document types TD17–TD19. |
| 2026 update | SDI technical specs v1.9.1 effective May 15, 2026. New validation checks (error 00327 for VAT Groups). |
| ViDA impact | EU ViDA Directive will require alignment with EN16931 standard. Italy's SdI clearance model may need adaptation by 2035. |

### India — IRN (Invoice Reference Number) [T1]

**India — IRN (Invoice Reference Number)**

| Element | Rule |
| --- | --- |
| Mandate | E-invoicing mandatory for businesses with turnover ≥₹5 crore (since August 2023) |
| Cross-border exports | Export invoices must also be reported to the Invoice Registration Portal (IRP) and receive an IRN. Tax invoice must include QR code. |
| Format | JSON schema submitted to IRP. IRP validates, generates IRN + QR code, digitally signs. |
| Foreign supplier to India | Not required to use IRP. Indian buyer handles GST under reverse charge. |
| Key fields for exports | Supply type = "EXPWP" (export with payment of IGST) or "EXPWOP" (export without payment — under LUT). Shipping bill details required. |

### Mexico — CFDI (Comprobante Fiscal Digital por Internet) [T1]

**Mexico — CFDI (Comprobante Fiscal Digital por Internet)**

| Element | Rule |
| --- | --- |
| Mandate | All invoices by Mexican-established entities must be CFDI 4.0 format, issued through a PAC (Authorized Certification Provider) with real-time SAT clearance |
| Cross-border sales | Mexican entity invoicing a foreign client not registered with SAT must still generate a CFDI through the clearance process. Use RFC "XEXX010101000" for foreign recipients. |
| Foreign supplier to Mexico | Not required to issue CFDI. Mexican buyer may need to issue a CFDI for the foreign payment (complemento de pagos). |
| Penalties | Non-compliance: 5%–10% of invoice amount. Fraudulent CFDI: criminal liability (prison). SAT has expedited powers to suspend digital certificates. |
| Complements | Specific transaction types require CFDI complements: payroll (nómina), foreign trade (comercio exterior), payments (pagos), tax withholdings (retenciones). |

### EU ViDA (VAT in the Digital Age) — Phased Rollout [T1]

**EU ViDA (VAT in the Digital Age) — Phased Rollout**

| Date | Change |
| --- | --- |
| July 2028 | Deemed supplier rules for platforms (accommodation, transport). Strengthened reverse charge. |
| July 2030 | **Mandatory e-invoicing for intra-EU B2B transactions.** Digital reporting requirements. E-invoicing becomes default form. EN16931 standard. |
| 2035 | Italy's SdI derogation expires. Full ViDA alignment required. |

## Section 8: Archiving Obligations When Invoicing Cross-Border

### Whose Retention Rules Apply? [T1]

**Whose Retention Rules Apply?**  _(VAT Directive Articles 244–248)_

| Rule | Detail |
| --- | --- |
| **General principle** | Each member state sets its own retention period and format requirements for invoices related to supplies made in its territory. |
| **Supplier** | Must retain copies of issued invoices per the rules of the member state where they are established. |
| **Customer** | Must retain received invoices per the rules of the member state where they are established. |
| **Cross-border** | Both parties retain under their own country's rules. If these differ, the stricter rule is the safest approach. |

### Retention Periods by Country [T1]

**Retention Periods by Country**

| Country | Retention Period | Format |
| --- | --- | --- |
| Germany | **10 years** (§14b UStG) | Original format (paper or electronic). Electronic invoices must remain in electronic form. |
| France | **10 years** (Art L102B, Livre des Procédures Fiscales) | Electronic invoices in original electronic format |
| Italy | **10 years** (Art 2220, Codice Civile) | Must be stored via approved electronic conservation ("conservazione sostitutiva") |
| Spain | **4 years** (Art 29.2, Ley General Tributaria) + additional years if open audit | Original format |
| Netherlands | **7 years** (Art 52 AWR) | Original format |
| UK | **6 years** (VAT Regulations 1995) | Original format |
| Belgium | **7 years** (Art 60 Code TVA) | Original format |
| US | **Varies by state** — typically 3–7 years for sales tax; 7 years recommended | Any legible format |

### Key Principles for Cross-Border Archiving [T1]

**Key Principles for Cross-Border Archiving**

| Principle | Guidance |
| --- | --- |
| **Authenticity of origin** | You must be able to prove who issued the invoice (digital signature, EDI, internal controls) |
| **Integrity of content** | The invoice content must not have been altered after issue |
| **Legibility** | The invoice must be readable (human or machine) throughout the retention period |
| **Storage location** | EU: May store outside the member state, but must provide online access to the tax authority on request (Art 247) |
| **Language** | Some countries (France, Germany, Italy) may require invoices to be in the local language or translatable on request during audit |

## PROHIBITIONS

- **Prohibitions list** — 1. NEVER issue an intra-EU B2B reverse charge invoice without the mandatory notation. The invoice is legally deficient without it. 2. NEVER assume the supplier's country rules always apply. Check Art 219a — the basic rule is place-of-supply country. 3. NEVER invoice in a foreign currency without documenting the exchange rate used for VAT conversion. 4. NEVER issue a credit note without referencing the original invoice number and date. 5. NEVER assume foreign suppliers to Italy don't need to worry about SDI — if established in Italy, SDI is mandatory. 6. NEVER treat Mexican CFDI requirements as optional for cross-border sales by Mexican entities. 7. NEVER destroy electronic invoices and store only paper copies. Many jurisdictions require retention in original electronic format. 8. NEVER assume one retention period fits all. Apply the rules of your own country AND consider the rules of the transaction country.  _(Art 219a)_

## Test Suite

### Test 1 — Intra-EU reverse charge invoice, DE to FR

**Input:** German consultant invoices French company (valid FR VAT) EUR 5,000 for advisory services.
**Expected:** Invoice follows German rules (Art 219a exception (a)). No VAT. Notation: "Steuerschuldnerschaft des Leistungsempfängers" or "Reverse charge — Art 196 Directive 2006/112/EC." Both VAT numbers on invoice.

### Test 2 — Italian company invoicing US client

**Input:** Italian software company invoices US client EUR 20,000 for development services.
**Expected:** Supply outside EU (Art 219a exception (b)). Italian invoicing rules apply. Must submit XML to SDI (post-July 2022). No VAT (out of scope). Retain for 10 years in electronic conservation.

### Test 3 — Multi-currency, Maltese company invoicing in USD

**Input:** Maltese company invoices a Japanese client USD 10,000 for consulting. Place of supply = Japan.
**Expected:** Maltese invoicing rules (exception (b)). Invoice in USD is fine. If VAT were applicable, convert to EUR at ECB rate on date of supply. Retain for Maltese period.

### Test 4 — Credit note for OSS sale

**Input:** German e-commerce seller issued an OSS invoice to an Italian consumer in Q1. In Q2, the consumer returns the goods.
**Expected:** Issue credit note referencing original invoice. Report the correction on the Q2 OSS return under Italy, not by amending Q1.

### Test 5 — Mexican company invoicing foreign client

**Input:** Mexican SaaS company invoices a Colombian client $5,000/month for software.
**Expected:** Must issue CFDI 4.0 via PAC with real-time clearance. Use RFC "XEXX010101000" for foreign recipient. Complemento de comercio exterior may be required.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Invoicing requirements are evolving rapidly due to e-invoicing mandates worldwide. Always verify current rules with official sources and a qualified advisor.

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
