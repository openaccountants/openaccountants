---
name: france-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a French VAT return (déclaration de TVA CA3) for a self-employed individual or small business under the régime réel normal in France. Trigger on phrases like "prepare CA3", "French VAT return", "TVA", "déclaration de TVA", "classify these transactions for French VAT", or any request involving France VAT filing. This skill covers France only, régime réel normal (monthly CA3) and régime réel simplifié (annual CA12 with two advance payments). Micro-entreprise (franchise en base de TVA), partial exemption, and margin schemes are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any French VAT work.
version: 2.0
---

# France VAT Return Skill (CA3 / CA12) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | France (République française) |
| Standard rate | 20% |
| Reduced rates | 10% (restaurants, transport, renovation works, prepared food), 5.5% (food staples, books, energy renovation, cultural events), 2.1% (press, certain medicines) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | CA3 (régime réel normal, monthly or quarterly); CA12 (régime réel simplifié, annual) |
| Filing portal | https://www.impots.gouv.fr (espace professionnel) |
| Authority | Direction Générale des Finances Publiques (DGFiP) |
| Currency | EUR only |
| Filing frequencies | Monthly (réel normal, turnover > €254,000 services / €840,000 goods); Quarterly (réel normal, VAT < €4,000/year); Annual with advance payments (réel simplifié) |
| Deadline | CA3: between 15th and 24th of following month (exact date depends on company identifier); CA12: 2nd working day after 1 May |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key CA3 lines (the lines you will use most):**

| Line | Meaning |
|---|---|
| 01 | Sales of goods and services at 20% (net) |
| 02 | Sales of goods and services at 5.5% (net) |
| 03 | Sales of goods and services at 10% (net) |
| 04 | Sales of goods and services at 2.1% (net) |
| 04B | Intra-EU acquisitions (net) |
| 05 | Imports (net, since 2022 auto-liquidation) |
| 06 | Sales of goods to other EU member states (net, 0%) |
| 06A | Intra-EU B2B services (Art. 283-2 reverse charge out, net) |
| 07 | Exports outside EU (net, 0%) |
| 07A | Other non-taxable operations |
| 08 | Output VAT on line 01 (20%) |
| 09 | Output VAT on line 02 (5.5%) |
| 09B | Output VAT on line 03 (10%) |
| 09C | Output VAT on line 04 (2.1%) |
| 10 | Total output VAT |
| 17 | Output VAT on intra-EU acquisitions |
| 18 | Output VAT on services from EU (autoliquidation) |
| 19 | Deductible VAT on immobilisations (capital goods) |
| 20 | Deductible VAT on other goods and services (ABS) |
| 21 | Other deductible VAT |
| 22 | Credit from prior period (report de crédit) |
| 23 | Total deductible VAT |
| 24 | Credit de TVA (if line 23 > line 10+17+18) |
| 25 | Net VAT due (if line 10+17+18 > line 23) |
| 28 | VAT payable (line 25 minus any adjustments) |

**Conservative defaults — France-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic France |
| Unknown B2B vs B2C status for EU customer | B2C, charge 20% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (autoliquidation, line 05 equivalent) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | €5,000 |
| HIGH tax-delta on a single conservative default | €400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | €10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any French or international business bank: BNP Paribas, Société Générale, Crédit Agricole, LCL, Banque Populaire, Caisse d'Épargne, La Banque Postale, CIC, Revolut Business, Wise Business, N26 Business, Qonto, or any other.

**Recommended** — sales invoices for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices for any input VAT claim above €400, the client's TVA number in writing (FR + 2 check digits + 9-digit SIREN).

**Ideal** — complete invoice register (FEC-compatible), SIRET number, prior period CA3, reconciliation of line 22 credit carried forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all → hard stop. If bank statement only without invoices → proceed but record in the reviewer brief: "This CA3 was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above €400 are supported by compliant tax invoices (factures) and that all reverse-charge classifications match the supplier's invoice."

### France-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-FR-1 — Micro-entreprise / franchise en base de TVA.** *Trigger:* client is under the franchise en base (turnover below €36,800 services / €91,900 goods for 2025/2026) and has not opted for VAT. *Message:* "Micro-entrepreneurs under the franchise en base de TVA are exempt from charging and collecting VAT. They do not file a CA3 or CA12. This skill cannot prepare a return for a franchise en base client. If you have opted for VAT (option pour la TVA), please confirm and provide your FR TVA number."

**R-FR-2 — Partial exemption (prorata de déduction).** *Trigger:* client makes both taxable supplies and exempt-without-credit supplies (financial, medical, educational, insurance) and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Your input VAT must be apportioned under the coefficient de déduction / prorata rules (Articles 206 to 214 of Annexe II to the CGI). Please use a qualified expert-comptable to determine the prorata before input VAT is claimed."

**R-FR-3 — Margin scheme (régime de la marge).** *Trigger:* client deals in second-hand goods, art, antiques, or collectables under the margin scheme. *Message:* "Margin scheme transactions (TVA sur la marge) require transaction-level margin computation. Out of scope for this skill."

**R-FR-4 — Real estate (TVA immobilière).** *Trigger:* client deals in new construction, building land, or property transactions subject to TVA immobilière. *Message:* "Real estate VAT (TVA immobilière) is complex and fact-specific. Out of scope for this skill. Please consult an expert-comptable."

**R-FR-5 — VAT group (groupe TVA).** *Trigger:* client is part of a VAT group under Article 256 C of the CGI. *Message:* "VAT groups require consolidation across the group. Out of scope."

**R-FR-6 — Fiscal representative.** *Trigger:* non-resident supplier or client with a fiscal representative in France. *Message:* "Non-resident registrations with fiscal representatives have specific obligations beyond this skill. Please use a qualified comptable."

**R-FR-7 — DOM-TOM filing.** *Trigger:* client is based in an overseas department/territory (Guadeloupe, Martinique, Réunion, Guyane, Mayotte). *Message:* "DOM-TOM territories have specific reduced rates (8.5% standard in Guadeloupe/Martinique/Réunion, 0% for some categories) that differ from mainland France. This skill covers metropolitan France only."

**R-FR-8 — Income tax instead of VAT.** *Trigger:* user asks about annual income tax (impôt sur le revenu, IS, BNC, BIC) instead of TVA. *Message:* "This skill only handles French VAT returns (CA3/CA12). For income tax, use a dedicated French income tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 French banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BNP PARIBAS, BNP | EXCLUDE for bank charges/fees | Financial service, exempt |
| SOCIETE GENERALE, SOC GEN, SG | EXCLUDE for bank charges/fees | Same |
| CREDIT AGRICOLE, CA, CRCAM | EXCLUDE for bank charges/fees | Same |
| LCL, CREDIT LYONNAIS | EXCLUDE for bank charges/fees | Same |
| BANQUE POPULAIRE, BPCE | EXCLUDE for bank charges/fees | Same |
| CAISSE D'EPARGNE, CE | EXCLUDE for bank charges/fees | Same |
| LA BANQUE POSTALE | EXCLUDE for bank charges/fees | Same |
| CIC, CREDIT MUTUEL | EXCLUDE for bank charges/fees | Same |
| QONTO | EXCLUDE for bank charges/fees | Check for separate taxable subscription invoices |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTERETS, INTEREST, AGIOS | EXCLUDE | Interest income/expense, out of scope |
| PRET, EMPRUNT, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 French government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| DGFIP, IMPOTS.GOUV, TRESOR PUBLIC | EXCLUDE | Tax payment (TVA, IS, IR), not a supply |
| DIRECTION GENERALE DES FINANCES | EXCLUDE | Tax payment |
| URSSAF | EXCLUDE | Social charges (cotisations sociales), not a VATable supply |
| CPAM, ASSURANCE MALADIE | EXCLUDE | Social security, not a supply |
| RSI, SSI | EXCLUDE | Social security for self-employed |
| GREFFE, TRIBUNAL DE COMMERCE | EXCLUDE | Court/registry fees, sovereign acts |
| CFE, COTISATION FONCIERE | EXCLUDE | Local business tax, not a supply |
| CVAE | EXCLUDE | Contribution on added value, not a supply |
| PREFECTURE, SOUS-PREFECTURE | EXCLUDE | Government administrative fees |
| INPI | EXCLUDE | Trademark/patent office, government fee |

### 3.3 French utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| EDF, ELECTRICITE DE FRANCE | Domestic 20% | 20 (input) | Electricity — standard rate overhead |
| ENGIE, GDF SUEZ | Domestic 20% or 5.5% | 20 (input) | Gas: subscription at 20%, energy portion may be 5.5% for residential heating — check invoice |
| TOTAL ENERGIES, TOTALENERGIES | Domestic 20% | 20 (input) | Energy/fuel supplier |
| ORANGE, ORANGE BUSINESS | Domestic 20% | 20 (input) | Telecoms/broadband — overhead |
| FREE, FREE MOBILE, FREE SAS | Domestic 20% | 20 (input) | Telecoms/broadband — overhead |
| SFR, ALTICE | Domestic 20% | 20 (input) | Telecoms/broadband |
| BOUYGUES TELECOM | Domestic 20% | 20 (input) | Telecoms/broadband |
| OVH, OVH SAS, OVHCLOUD | Domestic 20% | 20 (input) | Hosting, French entity |
| VEOLIA, SUEZ EAU | Domestic 5.5% | 20 (input) | Water supply at reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AXA, AXA FRANCE | EXCLUDE | Insurance, exempt |
| MAIF, MACIF, MATMUT, MAAF | EXCLUDE | Mutual insurance, exempt |
| GROUPAMA, GENERALI FRANCE | EXCLUDE | Insurance, exempt |
| AG2R, MALAKOFF HUMANIS | EXCLUDE | Complementary insurance/prévoyance, exempt |
| ASSURANCE, PRIME D'ASSURANCE | EXCLUDE | All insurance exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| LA POSTE (standard mail) | EXCLUDE for standard postage | | Universal postal service, exempt |
| LA POSTE (parcels, Colissimo) | Domestic 20% | 20 | Non-universal services are taxable |
| CHRONOPOST | Domestic 20% | 20 | Express courier, taxable |
| DHL EXPRESS FRANCE | Domestic 20% | 20 | Express courier, taxable |
| UPS FRANCE, TNT FRANCE, FEDEX | Domestic 20% or EU reverse charge | 20 or 17/18 | Check billing entity — French or EU |
| MONDIAL RELAY | Domestic 20% | 20 | Parcel delivery, French entity |

### 3.6 Transport (France domestic)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| SNCF, OUIGO | Domestic 10% | 20 (input) | Rail transport at reduced rate |
| RATP, METRO, BUS RATP | Domestic 10% | 20 (input) | Public transport, reduced rate |
| UBER FR, UBER FRANCE | Domestic 10% (transport) / 20% (delivery) | 20 | Underlying ride at 10%; check Uber Eats vs rides |
| BOLT FR, HEETCH | Domestic 10% | 20 | Ride-hailing, transport reduced rate |
| AIR FRANCE (domestic) | Domestic 10% | 20 | Domestic flights at 10% |
| AIR FRANCE, RYANAIR, EASYJET (international) | EXCLUDE / 0% | | International flights exempt |
| TAXI, G7, TAXIS BLEUS | Domestic 10% | 20 | Local taxi, reduced rate |
| AUTOROUTE, VINCI AUTOROUTES, SANEF, APRR | Domestic 20% | 20 | Motorway tolls at 20% |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| CARREFOUR, AUCHAN, LECLERC, INTERMARCHE | Default BLOCK input VAT | Personal provisioning. Deductible only if hospitality/catering business. |
| LIDL, MONOPRIX, FRANPRIX, CASINO | Default BLOCK | Same |
| PICARD, LEADER PRICE, SUPER U | Default BLOCK | Same |
| RESTAURANT, BRASSERIE, CAFE, BISTRO | Default BLOCK | Entertainment — see Section 5.12 for France-specific partial recovery rules |

### 3.8 SaaS — EU suppliers (reverse charge, autoliquidation line 17/18)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger autoliquidation (Art. 283-2 CGI).

| Pattern | Billing entity | Line | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 17/18 + 20 | Autoliquidation: output on 17 or 18, input on 20 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 17/18 + 20 | Autoliquidation |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 17/18 + 20 | Autoliquidation |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 17/18 + 20 | Autoliquidation |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 17/18 + 20 | Autoliquidation |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 17/18 + 20 | EU, autoliquidation |
| DROPBOX | Dropbox International Unlimited (IE) | 17/18 + 20 | Autoliquidation |
| SLACK | Slack Technologies Ireland Ltd (IE) | 17/18 + 20 | Autoliquidation |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 17/18 + 20 | EU, autoliquidation |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 17/18 + 20 | Autoliquidation |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | 17/18 + 20 | Transaction fees may be exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (autoliquidation, line 05 equivalent)

| Pattern | Billing entity | Line | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 17/18 + 20 | LU entity → EU autoliquidation |
| NOTION | Notion Labs Inc (US) | 05 + 20 | Non-EU autoliquidation (import of services) |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 05 + 20 | Non-EU autoliquidation |
| OPENAI, CHATGPT | OpenAI Inc (US) | 05 + 20 | Non-EU autoliquidation |
| GITHUB (standard plans) | GitHub Inc (US) | 05 + 20 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 05 + 20 | Non-EU autoliquidation |
| CANVA | Canva Pty Ltd (AU) | 05 + 20 | Non-EU autoliquidation |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) — check invoice | 05 + 20 or 17/18 + 20 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 05 + 20 | Non-EU autoliquidation |

### 3.10 SaaS — the exception (NOT reverse charge)

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU autoliquidation line 17/18 + 20 (Luxembourg entity) | Standard EU reverse charge applies. If invoice shows French TVA charged, treat as domestic 20%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | EU autoliquidation line 17/18 + 20 | Stripe IE entity — separate line item from transaction fees |
| SUMUP, SQUARE, ZETTLE | Check invoice | If French entity: domestic 20%; if IE/EU entity: autoliquidation |

### 3.12 Professional services (France)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| EXPERT COMPTABLE, CABINET COMPTABLE | Domestic 20% | 20 | Always deductible |
| AVOCAT, CABINET D'AVOCATS | Domestic 20% | 20 | Deductible if business legal matter |
| NOTAIRE (business-related fees) | Domestic 20% | 20 | Notarial fees on business transactions |
| COMMISSAIRE AUX COMPTES, CAC | Domestic 20% | 20 | Audit fees, always deductible |
| ARCHITECTE, GEOMETRE | Domestic 20% | 20 | Professional services |
| CHAMBRE DE COMMERCE, CCI | EXCLUDE | Registration/membership fees, government body |
| CHAMBRE DES METIERS, CMA | EXCLUDE | Same |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| URSSAF | EXCLUDE | Social contributions |
| POLE EMPLOI, FRANCE TRAVAIL | EXCLUDE | Employment agency, social contribution |
| RETRAITE, CIPAV, CNAV | EXCLUDE | Pension/retirement contributions |
| SALAIRE, PAIE, VIREMENT SALAIRE | EXCLUDE | Wages — outside VAT scope |
| MUTUELLE (employee complementary) | EXCLUDE | Social benefit, not VATable |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| LOYER COMMERCIAL, BAIL COMMERCIAL | Domestic 20% | Commercial lease where landlord opted to charge VAT (option à la TVA) |
| LOYER, BAIL (residential, no VAT) | EXCLUDE | Residential lease exempt |
| FONCIER, TAXE FONCIERE | EXCLUDE | Property tax, not a supply |
| SCI (with TVA invoiced) | Domestic 20% | Commercial property via SCI with TVA option |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| VIREMENT INTERNE, VIR INTERNE | EXCLUDE | Internal movement |
| VIREMENT ENTRE COMPTES | EXCLUDE | Own-account transfer |
| DIVIDENDE | EXCLUDE | Dividend payment, out of scope |
| REMBOURSEMENT PRET, ECHEANCE | EXCLUDE | Loan repayment, out of scope |
| RETRAIT DAB, RETRAIT ESPECES | TIER 2 — ask | Default exclude; ask what cash was spent on |
| APPORT, APPORT PERSONNEL | EXCLUDE | Owner injection |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a France-based self-employed IT consultant (having opted for TVA / régime réel). They illustrate the trickiest cases.

### Example 1 — Non-EU SaaS autoliquidation (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.9). No VAT on the invoice. This is a service received from a non-EU supplier. The French client must self-assess VAT (autoliquidation) under Art. 283-1 CGI. Output VAT is declared, and simultaneously input VAT is deducted on line 20. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line (input) | Line (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 2.94 | 20% | 20 | 05 | N | — | — |

### Example 2 — EU service, autoliquidation (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
Google Ireland Limited is an IE entity — standard EU autoliquidation. Google Ads is a service. Output VAT on line 17 or 18 (EU acquisitions), input VAT on line 20. Both sides must appear on the return. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line (input) | Line (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 170.00 | 20% | 20 | 17/18 | N | — | — |

### Example 3 — Entertainment, partially recoverable in France

**Input line:**
`15.04.2026 ; BRASSERIE LIPP PARIS ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant transaction. Unlike Malta, France does NOT have a hard block on business entertainment. Business meals (repas d'affaires) are deductible at 20% if justified by a business purpose and documented with attendee names. However, personal meals and unjustified entertaining are blocked. Default: block, flag for reviewer. If confirmed as justified business entertainment with documentation → deductible at 20%.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | BRASSERIE LIPP PARIS | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Restaurant: confirm business purpose and attendees for deduction" |

### Example 4 — Capital goods (immobilisation)

**Input line:**
`18.04.2026 ; DELL FRANCE SAS ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
The gross amount is €1,595. In France, assets with a unit value exceeding €500 HT (net of VAT) are typically capitalised as immobilisations. €1,595 TTC / 1.20 = €1,329.17 HT > €500. This is a capital goods purchase. Input VAT goes to line 19 (TVA déductible sur immobilisations), not line 20.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL FRANCE SAS | -1,595.00 | -1,329.17 | -265.83 | 20% | 19 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice FR-2026-018 IT consultancy March ; +3,500.00 ; EUR`

**Reasoning:**
Incoming €3,500 from a German company (DE IBAN). The client is providing IT consulting services. B2B place of supply for services is the customer's country (Germany) under the general rule (Art. 259-1 CGI / Art. 44 VAT Directive). The client invoices at 0% with mention "Autoliquidation — Art. 283-2 du CGI / Art. 196 Directive 2006/112/CE". Report on line 06A (services intracommunautaires). No output VAT. Confirm: (a) customer is VAT-registered — verify German USt-IdNr on VIES; (b) the invoice carries the correct reverse-charge mention.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 06A | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, blocked for VP

**Input line:**
`28.04.2026 ; ARVAL FRANCE ; DEBIT ; Lease payment Peugeot 3008 ; -650.00 ; EUR`

**Reasoning:**
Car lease payment. In France, input VAT on passenger vehicle (VP — véhicule de tourisme) leases is NOT deductible for most businesses (Art. 206-IV Annexe II CGI). Exceptions: taxis, driving schools, car rental businesses, commercial vehicles (VU — véhicule utilitaire). For an IT consultant leasing a passenger car, VAT is blocked. Note: diesel/petrol fuel for VP is 80% deductible; electric vehicle charging is 100% deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ARVAL FRANCE | -650.00 | -650.00 | 0 | — | — | Y | Q3 | "Véhicule de tourisme: VAT blocked. Is this a VU (commercial vehicle)?" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the line mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 20% (Art. 278 CGI)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales → line 01 / line 08. Purchases → line 20 (ABS) or line 19 (immobilisations).

### 5.2 Reduced rate 10% (Art. 278 bis, 279 CGI)

Applies to: restaurant meals (food and non-alcoholic drinks on-premises), passenger transport, renovation works on residential buildings (over 2 years old), hotels and holiday accommodation, prepared food for immediate consumption. Sales → line 03 / line 09B. Purchases → line 20.

### 5.3 Reduced rate 5.5% (Art. 278-0 bis CGI)

Applies to: food staples (not prepared/on-premises), books (printed and digital since 2012), theatre and live performances, energy renovation works (insulation, heating upgrades), water supply. Sales → line 02 / line 09. Purchases → line 20.

### 5.4 Super-reduced rate 2.1% (Art. 281 quater to 281 nonies CGI)

Applies to: press publications (print and online since 2014), certain reimbursable medicines (Sécurité Sociale list), first showings of films and theatrical performances under certain conditions. Sales → line 04 / line 09C. Very narrow — default to 20% if uncertain.

### 5.5 Zero rate and exempt with credit

Exports outside EU → line 07 (zero-rated, requires export evidence / DAU). Intra-EU B2B supplies of goods → line 06 (zero-rated, requires customer VAT number verified on VIES, transport proof, compliant invoice with mention obligatoire). Intra-EU B2B services → line 06A (place of supply is customer's country, no French VAT, requires customer VAT number and reverse-charge mention).

### 5.6 Exempt without credit (Art. 261 CGI)

Medical and paramedical services, education and training (under certain conditions), insurance, financial services, residential rent, certain cultural and sporting activities. These are excluded from the VAT return — no output VAT, no input VAT deduction on related costs. If significant, partial exemption rules apply — **R-FR-2 refuses** if non-de-minimis.

### 5.7 Local standard purchases

Input VAT on a compliant facture from a French supplier is deductible for purchases used in taxable business activity. Subject to blocked-input rules (5.12) and the capital goods rules (5.9). Map overhead to line 20. Map capital goods to line 19.

### 5.8 Autoliquidation — EU services received (Art. 283-2 CGI)

When the client receives a service from an EU supplier and the supplier invoices at 0% with a reverse-charge note: output VAT on line 17 or 18, input VAT on line 20. Net effect zero for a fully taxable client. If the EU supplier charged their local VAT (e.g. Irish 23%), that is NOT autoliquidation — treat as an expense with irrecoverable foreign VAT.

### 5.9 Autoliquidation — EU goods received (acquisitions intracommunautaires)

Physical goods from an EU supplier: output VAT on line 17 (line 04B for the base), input VAT on line 20 or 19 (if immobilisation).

### 5.10 Autoliquidation — non-EU services and imports

For services received from outside the EU where no VAT was charged: output VAT and input VAT both self-assessed. Since 1 January 2022, import VAT on goods is also auto-liquidated on the CA3 (line 05 for base, line 20/19 for input deduction) — no more paying VAT at customs.

### 5.11 Capital goods (immobilisations)

If net (HT) value > €500: line 19 for input VAT. If net ≤ €500: line 20 as current expenditure. Capital goods may be subject to regularisation over 5 years (movable property) or 20 years (immovable property) if use changes.

### 5.12 Blocked input VAT (Art. 206 Annexe II CGI and related)

The following categories have restricted or zero VAT recovery:
- Passenger vehicles (véhicules de tourisme): purchase, lease, maintenance — blocked. Exceptions: taxis, driving schools, car rental, funeral vehicles. Commercial vehicles (VU) fully deductible.
- Fuel: diesel/petrol for VP 80% deductible; GPL/electricity 100% deductible; diesel/petrol for VU 100% deductible.
- Accommodation (hébergement): hotel stays for staff are NOT deductible. Hotel stays paid for clients/third parties ARE deductible.
- Gifts and cadeaux d'affaires: blocked if unit value > €73 TTC per beneficiary per year. Below threshold: deductible.
- Personal use items: not deductible.
- **Business meals (repas d'affaires) ARE deductible at 20% with proper justification** (names of attendees, business purpose). This is a key France-specific difference from Malta and other jurisdictions with hard entertainment blocks.

### 5.13 Régime réel simplifié (CA12)

CA12 clients file annually and pay two advance payments (acomptes) in July and December. The annual CA12 has similar structure to the CA3 but covers the full year. This skill can prepare CA12 data — accumulate monthly/quarterly totals into annual figures.

### 5.14 Sales — local domestic (any rate)

Charge 20%, 10%, 5.5%, or 2.1% as applicable. Map to line 01/02/03/04 as appropriate.

### 5.15 Sales — cross-border B2C

Goods to EU consumers above €10,000 EU-wide threshold → **R-EU-5 (OSS refusal) from eu-vat-directive fires**. Digital services to EU consumers above €10,000 → same. Below threshold → French VAT at applicable rate.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* TOTAL, SHELL, BP, ESSO, AVIA, fuel receipts. *Why insufficient:* vehicle type (VP vs VU) determines deductibility. *Default:* 0% recovery. *Question:* "Is this a passenger vehicle (VP — blocked) or a commercial vehicle (VU — deductible)? Diesel/petrol for VP is 80% deductible for fuel only."

### 6.2 Restaurants and entertainment

*Pattern:* any named restaurant, brasserie, café, traiteur. *Why insufficient:* France allows deduction of business meals with proper justification, but personal meals are blocked. *Default:* block. *Question:* "Was this a justified business meal (repas d'affaires) with external guests? If yes, provide attendee names for the file."

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe, PayPal. *Why insufficient:* same brand can bill from Ireland (EU autoliquidation), US (non-EU autoliquidation), or France (domestic 20%). *Default:* non-EU autoliquidation line 05 + 20. *Question:* "Could you check the invoice? I need the legal entity name and country."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Default:* exclude as owner injection (apport personnel). *Question:* "The €X transfer from [name] — is this a customer payment, your own money going in, or a loan?"

### 6.5 Incoming transfers from individual names (not owner)

*Pattern:* incoming from private-looking counterparties. *Default:* domestic B2C sale at 20%, line 01/08. *Question:* "For each: was it a sale? Business or consumer customer? Country?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or foreign currency. *Default:* domestic 20%. *Question:* "What was this — B2B with a VAT number, B2C, goods or services, and which country?"

### 6.7 Large one-off purchases (potential immobilisations)

*Pattern:* single invoice near €500 HT threshold, or labelled "laptop", "equipment", "machinery". *Default:* if HT > €500 → line 19; if HT ≤ €500 → line 20. *Question:* "Could you confirm the total invoice amount including VAT?"

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Orange, Free, SFR personal lines; home electricity. *Default:* 0% if mixed without declared %. *Question:* "Is this a dedicated business line or mixed-use? What business percentage?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as drawings. *Question:* "Was this a contractor payment with an invoice, wages, a refund, or a personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* DAB, retrait espèces, retrait guichet. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* loyer, bail, monthly to a landlord-sounding counterparty. *Default:* no VAT (residential default). *Question:* "Is this a commercial property where the landlord has exercised the option for TVA?"

### 6.12 Foreign hotel and accommodation

*Pattern:* hotel or accommodation charged abroad. *Default:* exclude from input VAT (French VAT not recoverable on foreign hotel). *Question:* "Was this a business trip?" (For income tax records, still deductible.)

### 6.13 Airbnb income

*Pattern:* Airbnb payouts. *Default:* [T2] flag for reviewer. *Question:* "Is this furnished rental (LMNP/LMP)? Duration? Tourist accommodation at 10%?"

### 6.14 Subcontractor reverse charge (construction)

*Pattern:* payments to construction subcontractors. *Why insufficient:* since 2014, construction subcontracting in France triggers a domestic reverse charge (autoliquidation Art. 283-2 nonies CGI). The subcontractor invoices without VAT and the main contractor self-assesses. *Default:* [T2] flag for reviewer. *Question:* "Is this a construction subcontractor subject to domestic autoliquidation?"

### 6.15 Platform sales (Amazon, eBay, Etsy)

*Pattern:* incoming from Amazon Payments EU, Etsy Payments, PayPal, Stripe. *Default:* if client sells to EU consumers across multiple countries above €10,000, R-EU-5 OSS refusal fires. For France-only or below-threshold: treat gross as line 01 base at 20%; platform fees as separate EU autoliquidation. *Question:* "Do you sell to buyers outside France? Total EU cross-border sales for the year?"

---

## Section 7 — Excel working paper template (France-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the France-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Line code") accepts only valid CA3 line codes from Section 1 of this skill. Use blank for excluded transactions. For autoliquidation transactions, enter both the input line and output line separated by a slash in column H.

### Sheet "Line Summary"

One row per line. Column A is the line number, column B is the description, column C is the value computed via formula. Mandatory rows:

```
Output:
| 01 | Sales 20% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "01") |
| 02 | Sales 5.5% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "02") |
| 03 | Sales 10% net | =SUMIFS(Transactions!E:E, Transactions!H:H, "03") |
| 06 | Intra-EU B2B goods (0%) | =SUMIFS(Transactions!E:E, Transactions!H:H, "06") |
| 06A| Intra-EU B2B services (0%) | =SUMIFS(Transactions!E:E, Transactions!H:H, "06A") |
| 07 | Exports (0%) | =SUMIFS(Transactions!E:E, Transactions!H:H, "07") |
| 08 | Output VAT 20% | =C[01_row]*0.20 |
| 09 | Output VAT 5.5% | =C[02_row]*0.055 |
| 09B| Output VAT 10% | =C[03_row]*0.10 |
| 10 | Total output VAT | =SUM(08,09,09B) |

Autoliquidation:
| 04B| Intra-EU acquisitions net | =SUMIFS(Transactions!E:E, Transactions!H:H, "04B") |
| 05 | Non-EU imports/services net | =SUMIFS(Transactions!E:E, Transactions!H:H, "05") |
| 17 | Output VAT EU acquisitions | =C[04B_row]*0.20 |
| 18 | Output VAT EU services | (separate if needed) |

Input:
| 19 | Input VAT immobilisations | =SUMIFS(Transactions!F:F, ..., "19") |
| 20 | Input VAT ABS (other goods/services) | =SUMIFS(Transactions!F:F, ..., "20") |
| 22 | Credit carried forward | (manual entry) |
| 23 | Total deductible VAT | =SUM(19,20,21,22) |

Bottom line:
| 25 | Net VAT due | =MAX(0, C[10]+C[17]+C[18]-C[23]) |
| 24 | Credit de TVA | =MAX(0, C[23]-C[10]-C[17]-C[18]) |
| 28 | VAT payable | =C[25] |
```

### Sheet "Return Form"

Final CA3-ready figures.

```
IF line 23 > (line 10 + line 17 + line 18):
  Line 24 = credit de TVA
  Line 25 = 0
ELSE:
  Line 24 = 0
  Line 25 = net VAT due
  Line 28 = Line 25 (minus any adjustments)
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for any row where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/france-vat-<period>-working-paper.xlsx
```

---

## Section 8 — French bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these France-specific patterns.

**CSV format conventions.** French banks typically export in CSV with semicolon delimiters and DD/MM/YYYY dates. Common columns: Date, Libellé (description), Débit, Crédit, Solde. Qonto and Revolut use ISO dates. BNP and SG exports may include operation codes (VIR = virement, CB = carte bancaire, CHQ = chèque, REM = remise, PRLV = prélèvement).

**French language variants.** Some descriptions appear in French: loyer (rent), salaire/paie (salary), intérêts (interest), virement (transfer), cotisations (contributions), facture (invoice), remboursement (refund). Treat as the English equivalent.

**Operation code prefixes.** VIR = bank transfer, CB = card payment, PRLV = direct debit (prélèvement), CHQ = cheque, REM = cheque deposit, TIP = interbank payment title. The prefix helps classify — CB payments are typically purchases, VIR CREDIT incoming are typically sales.

**Internal transfers and exclusions.** Own-account transfers between the client's accounts. Labelled "VIR INTERNE", "virement entre comptes". Always exclude.

**Refunds and reversals.** Identify by "remboursement", "annulation", "avoir", "storno". Book as a negative in the same line as the original transaction.

**URSSAF and social charges.** Monthly or quarterly URSSAF debits (PRLV URSSAF) are social contributions, not VATable. Always exclude. These can be large amounts — do not confuse with business purchases.

**impots.gouv.fr payments.** Tax payments (TVA, IS, IR, CFE) appearing as "DGFIP", "TRESOR PUBLIC", or "IMPOTS.GOUV". Always exclude — these are tax settlements, not supplies.

**Foreign currency transactions.** Convert to EUR at the transaction date rate. Use the ECB reference rate or the rate shown on the bank statement.

**IBAN country prefix.** FR = France. IE, LU, NL, DE = EU. US, GB, AU, CH = non-EU. A French IBAN does not automatically mean a French VAT registration — always cross-check.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* sole trader (EI/EIRL) names often match account holder; company names end in "SARL", "SAS", "EURL", "SA". *Fallback:* "Are you a sole trader (EI), EURL, SARL, SAS, or other?"

### 9.2 VAT regime
*Inference rule:* if filing CA3, they are réel normal. If mention of annual filing, réel simplifié. *Fallback:* "Are you under régime réel normal (monthly CA3) or régime réel simplifié (annual CA12)?"

### 9.3 TVA number
*Inference rule:* FR-format TVA numbers sometimes appear on invoices. *Fallback:* "What is your French TVA number? (FR + 2 digits + SIREN)"

### 9.4 Filing period
*Inference rule:* first and last transaction dates. *Fallback:* "Which month does this CA3 cover?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales descriptions. *Fallback:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* URSSAF, PAYE outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* presence of medical/financial/educational/residential rental income. *Fallback:* "Do you make any exempt sales?" *If yes and non-de-minimis → R-FR-2 refuses.*

### 9.8 Credit carried forward
*Inference rule:* not inferable. Always ask. *Question:* "Do you have a credit de TVA from the prior period? (Line 22)"

### 9.9 Cross-border customers
*Inference rule:* foreign IBANs on incoming. *Fallback:* "Do you have customers outside France? EU or non-EU? B2B or B2C?"

### 9.10 Construction subcontracting
*Inference rule:* construction-related counterparties in payments. *Conditional fallback:* "Do you subcontract construction work? (Domestic autoliquidation may apply.)"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, written in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). The France-specific content (line mappings, rates, thresholds, blocked categories) is based on the Code Général des Impôts and DGFiP guidance.

### Sources

**Primary legislation:**
1. Code Général des Impôts (CGI) — Articles 256 to 298 (TVA provisions)
2. Annexe II au CGI — Articles 205 to 242 (deduction rules)
3. Annexe IV au CGI — specific exemptions

**DGFiP guidance:**
4. Notice CA3 (formulaire 3310-CA3) and completion notes — https://www.impots.gouv.fr
5. BOFiP-Impôts — Bulletin Officiel des Finances Publiques (TVA section)
6. DGFiP guidance on autoliquidation (intra-EU and non-EU services)

**EU directive (loaded via companion skill):**
7. Council Directive 2006/112/EC — implemented via eu-vat-directive companion skill
8. Council Implementing Regulation 282/2011

**Other:**
9. VIES validation — https://ec.europa.eu/taxation_customs/vies/
10. ECB euro reference rates — https://www.ecb.europa.eu/stats/eurofxref/

### Known gaps

1. The supplier pattern library covers common French and international counterparties but not every local SME.
2. DOM-TOM specific rates (8.5%, 2.1%, 1.75%) are not covered — R-FR-7 refuses.
3. Construction subcontracting domestic reverse charge (Art. 283-2 nonies) is flagged T2 only.
4. The capital goods threshold (€500 HT) is the standard accounting threshold — verify with current guidance.
5. Red flag thresholds are conservative starting values.
6. Business meals deductibility (unlike Malta's hard block) requires documentation — the skill flags but cannot verify attendee lists.
7. Fuel deduction percentages (80% for VP diesel/petrol) are 2025/2026 values — verify annually.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. 10 sections. Supplier pattern library with French banks, utilities, government, SaaS, transport, food, professional services. Six worked examples. Tier 1 and Tier 2 catalogues. Excel template. Bank statement reading guide. Onboarding fallback.
- **v1.0:** Initial skill, standalone monolithic document.

### Self-check (v2.0)

1. Quick reference at top with line table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 15 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. Excel template specification: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 8 France-specific refusals present: yes (Section 2, R-FR-1 through R-FR-8).
9. Reference material at bottom: yes (Section 10).
10. Business meals partial deductibility (key France difference from Malta): yes (Section 5.12 + Example 3).
11. Motor vehicle VP/VU distinction: yes (Section 5.12 + Example 6).
12. Capital goods immobilisation threshold: yes (Section 5.11 + Example 4).
13. EU B2B service sale (line 06A) and VIES verification: yes (Example 5).
14. Non-EU SaaS autoliquidation: yes (Example 1 + Section 3.9).
15. Construction subcontracting domestic reverse charge flagged: yes (Section 6.14).

## End of France VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a CA3 without all three files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, commissaire aux comptes, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
