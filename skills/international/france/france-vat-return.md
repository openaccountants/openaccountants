---
name: france-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a French VAT return (déclaration de TVA CA3) for a self-employed individual or small business under the régime réel normal in France. Trigger on phrases like "prepare CA3", "French VAT return", "déclaration TVA France", "classify transactions for France", "TVA française", "autoliquidation", "reverse charge France", or any request involving French VAT filing. Covers régime réel normal only. Franchise en base de TVA, régime simplifié (CA12), micro-entreprise, margin schemes, travel agents, agricultural flat rate, partial exemption (prorata), and VAT groups (groupe TVA) are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.2.0+ and eu-vat-directive v0.1+. ALWAYS read before touching French VAT work.
version: 0.1
---

# France VAT Return Skill (CA3, Régime Réel Normal) v0.1

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | France (France métropolitaine — Corsica and DOM-TOM out of scope for v0.1) |
| Return form | CA3 — déclaration mensuelle ou trimestrielle de TVA (régime réel normal) |
| Tax | TVA (Taxe sur la Valeur Ajoutée) |
| Governing law | Code général des impôts (CGI), primarily articles 256 through 298 sexdecies. **See recodification note in Section 10 — from 1 September 2026 VAT provisions move to the Code des Impositions sur les Biens et Services (CIBS) under Ordonnance n° 2025-1247 of 17 December 2025.** This v0.1 cites the CGI as currently in force. |
| Authority | Direction Générale des Finances Publiques (DGFiP) |
| Filing portal | impots.gouv.fr — compte professionnel, either EDI-TVA or EFI (échange de formulaires informatisé) |
| Currency | EUR only |
| Standard rate | 20% (art. 278 CGI) |
| Intermediate rate | 10% (art. 278 bis, 278 quater, 278 sexies A, 278 septies, 279 CGI) |
| Reduced rate | 5.5% (art. 278-0 bis CGI) |
| Super-reduced rate | 2.1% (art. 281 quater CGI) |
| Filing frequencies | Monthly (default for régime réel normal), or quarterly if annual TVA due is below €4,000 |
| Deadline | Between 15th and 24th of the following month, depending on the first letter of the company name and the département (set by local DGFiP) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.2.0 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |

**Key CA3 fields (the cadres you will use most):**

| Cadre / Ligne | Meaning |
|---|---|
| Ligne A1 | Ventes, prestations de services (France métropolitaine) — net taxable at standard/intermediate/reduced rates |
| Ligne A2 | Autres opérations imposables — typically intra-Community acquisitions of services (autoliquidation), import of services from outside the EU |
| Ligne A3 | Acquisitions intracommunautaires (goods) — self-assessed output TVA |
| Ligne A4 | Opérations en provenance de Monaco (treated as internal French VAT, not cross-border) |
| Ligne B1 | Livraisons intracommunautaires (exempt intra-Community supplies of goods, art. 262 ter I CGI) |
| Ligne B2 | Exportations hors UE (exempt exports, art. 262 I CGI) |
| Ligne B3 | Other exempt operations — typically B2B services to EU customers (art. 259-1° CGI / art. 44 directive) |
| Ligne B4 | Livraisons d'électricité, gaz, chaleur et froid (special regime) |
| Cadre I | TVA brute collectée (output VAT by rate) |
| Cadre II | TVA déductible (input VAT, separated by type: immobilisations, autres biens et services) |
| Ligne 16 | TVA nette due (positive = payable) |
| Ligne 24 | Crédit de TVA (negative = credit carried forward or refundable) |

**Numéro de TVA intracommunautaire format:** FR + 2 check digits (alphanumeric) + 9 digits of SIREN (e.g., FR32123456789). The 9-digit SIREN is the company identifier; the 2 check digits are computed from the SIREN. The full SIRET (14 digits) identifies a specific établissement and is used in e-invoicing routing.

**Refusal catalogue quick index:** R-FR-1 through R-FR-14 in Section 2.

**Conservative defaults — France-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Category | Default | French-specific note |
|---|---|---|
| Unknown rate on a sale | 20% | Taux normal (art. 278 CGI) |
| Unknown VAT status of a purchase | Not deductible | Requires a facture compliant with art. 242 nonies A Annexe II CGI |
| Unknown counterparty country | France domestic | If IBAN starts with anything other than FR or if counterparty name is foreign, re-check |
| Unknown customer status (B2B vs B2C) | B2C with 20% | Applies the conservative customer-side treatment |
| Unknown vehicle business use | 0% deductible (cars) | Art. 206 IV Annexe II CGI — input TVA on passenger cars (VP — véhicules de tourisme) is **entirely blocked** regardless of business use. This is stricter than the German 50% default and the Italian 40% cap. |
| Unknown restaurant / business meal | Deductible if business purpose documented | Different from Germany and Italy — France allows deduction on business meals provided the "frais de réception" are justified. Default to blocked pending documentation. |
| Unknown fuel (gasoline vs diesel) | Diesel 80% deductible, gasoline 80% deductible | Since 2022 gasoline and diesel are treated identically at 80% deductible for passenger vehicles (art. 298 4° CGI). Commercial vehicles: 100%. |
| Gift to customer | Blocked if unit value > €73 TTC (2025) | Art. 206 IV-2-3° Annexe II CGI — low-value gift threshold, revalued annually |
| Telephone / mobile | 100% deductible if documentable business use | France does not impose a statutory cap on mobile phone deduction (unlike Italy's 50%). Default: block unless business use is clear from the data or context. |
| Hotels | Deductible at 10% TVA rate for accommodation | Hotels are at the 10% intermediate rate, full deduction for business travel |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

- Single transaction HIGH threshold: €5,000
- Tax delta HIGH threshold: €500
- Period total HIGH threshold: €50,000

## Section 2 — France-specific refusal catalogue (R-FR-1 through R-FR-14)

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-FR-1 — Franchise en base de TVA.**
*Condition.* The user is registered under the franchise en base (art. 293 B CGI) — the small-business scheme where turnover is below the thresholds (€37,500 services / €85,000 commerce as of 2026) and the taxpayer does not charge TVA, does not recover input TVA, and does not file CA3 returns.
*Message.* "You operate under the franchise en base de TVA (art. 293 B CGI), which means you do not charge TVA on your invoices, do not recover input TVA, and do not file CA3 returns. Your invoices should carry the mandatory mention 'TVA non applicable, art. 293 B du CGI'. This skill targets the régime réel normal and cannot produce a return for a franchise en base taxpayer — there is no return to produce. If you have exceeded the franchise threshold during the period, you need an expert-comptable to handle the transition to régime réel."

**R-FR-2 — Régime simplifié d'imposition (CA12).**
*Condition.* The user is on the régime réel simplifié, filing an annual CA12 with two provisional acomptes during the year rather than monthly or quarterly CA3.
*Message.* "You are on the régime réel simplifié (RSI), which files an annual CA12 declaration rather than periodic CA3. The CA12 computation includes régularisations and the two provisional acomptes during the year that this skill does not handle. This skill targets only the régime réel normal with monthly or quarterly CA3 filing. You need an expert-comptable to prepare the CA12."

**R-FR-3 — Micro-entreprise.**
*Condition.* The user operates as a micro-entrepreneur (formerly auto-entrepreneur) under the régime micro-BIC or micro-BNC, which generally means they are also under franchise en base unless they've opted out.
*Message.* "You operate as a micro-entrepreneur. If your turnover is below the franchise threshold and you have not opted for TVA, you do not file a TVA return at all (see R-FR-1). If you have opted for TVA, your profile description should confirm this — in that case, please tell me explicitly so I can proceed. Without confirmation, the default assumption for a micro-entrepreneur is franchise en base, which this skill cannot handle."

**R-FR-4 — E-invoicing mandate (réforme de la facturation électronique).**
*Condition.* The user is within the scope of the phased French e-invoicing mandate. Rollout per the February 2026 Finance Bill and current DGFiP guidance: from **1 September 2026**, all businesses subject to French VAT must be able to **receive** e-invoices via a Plateforme Agréée (PA) or the Portail Public de Facturation (PPF) directory; large and intermediate-sized companies (grandes entreprises and ETI) must also **issue** e-invoices from this date. From **1 September 2027**, small enterprises (PME) and micro-enterprises subject to TVA must also issue e-invoices. Both dates carry an optional three-month extension to 1 December of the same year.
*Handling.* This is not a simple "issue refusal" — it depends on the user's size and the current date. The skill should handle it as follows:
  1. **If the current date is before 1 September 2026:** no e-invoicing refusal applies. Proceed normally, but note in the reviewer brief that the user should be preparing for PA selection and onboarding.
  2. **If the current date is on or after 1 September 2026 AND the user is a grande entreprise or ETI:** the user must already be issuing e-invoices via a PA. If the profile inference in Step 3 of the workflow suggests no PA is in place, fire this refusal.
  3. **If the current date is on or after 1 September 2026 AND the user is a PME or micro-entreprise:** the user must already be able to receive e-invoices. If the profile inference suggests the receive obligation is not met, fire this refusal. The issue obligation does not yet apply until 1 September 2027.
  4. **If the current date is on or after 1 September 2027:** all VAT-registered businesses must be both issuing and receiving e-invoices via a PA. If profile inference suggests either obligation is unmet, fire this refusal.
*Message (when fired).* "As of [current date], French VAT-registered businesses of your size are required to [receive / issue and receive] electronic invoices via a Plateforme Agréée (PA) accredited by the DGFiP. Your profile does not indicate an accredited platform is in place. You cannot legally operate without PA compliance and this skill cannot prepare a CA3 for a business that is not meeting its e-invoicing obligations. Contact an expert-comptable or select a PA from the DGFiP's published list at impots.gouv.fr before any return can be prepared. This is not optional — it is a legal requirement under the loi de finances and the associated DGFiP implementing texts."
*Terminology note.* The PA (Plateforme Agréée) terminology replaced the earlier PDP (Plateforme de Dématérialisation Partenaire) terminology in the February 2026 Finance Bill. References to PDP in older documents now mean PA. The PPF (Portail Public de Facturation) remains the central directory and data hub but is no longer a free billing service — all actual invoice transmission goes through an accredited PA.

**R-FR-5 — Partial exemption (prorata de déduction).**
*Condition.* The user makes both taxable and exempt supplies (opérations exonérées under art. 261 CGI) above de minimis, requiring the prorata de déduction mechanism under art. 271 CGI and art. 205-206 Annexe II CGI.
*Reason.* French prorata is structurally complex — it distinguishes between the coefficient d'assujettissement, coefficient de taxation, and coefficient d'admission, combined as the coefficient de déduction. The calculation requires annual régularisation and sector-specific adjustments.
*Message.* "Your business makes both taxable and exempt supplies, which triggers the prorata de déduction under art. 271 CGI. French prorata is computed using three separate coefficients (assujettissement, taxation, admission) and requires annual régularisation in the December return. This is substantially more complex than ordinary input TVA recovery and this skill does not handle it. You need an expert-comptable with experience in partial exemption to set up the prorata methodology."

**R-FR-6 — Margin schemes (régime de la marge bénéficiaire).**
*Condition.* The user resells second-hand goods, works of art, antiques, or collectors' items under the régime particulier de la marge bénéficiaire (art. 297 A ff. CGI).
*Message.* "Your business involves the resale of second-hand goods, works of art, antiques, or collectors' items under the régime de la marge bénéficiaire (art. 297 A CGI). This scheme requires item-by-item margin tracking and specific invoicing mentions that cannot be derived from a bank statement. You need an expert-comptable familiar with the régime de la marge."

**R-FR-7 — Travel agents (régime des agences de voyages).**
*Condition.* The user operates a travel agency reselling travel and accommodation under art. 266-1-e CGI.
*Message.* "Your business is subject to the régime particulier des agences de voyages under art. 266-1-e CGI, which has specialized VAT rules quite different from standard TVA. This skill cannot handle the travel agents margin scheme."

**R-FR-8 — Agricultural flat rate (régime du remboursement forfaitaire agricole).**
*Condition.* The user operates under the agricultural flat-rate reimbursement scheme.
*Message.* "You operate under the régime du remboursement forfaitaire agricole, which uses compensation percentages rather than actual input TVA. This skill cannot handle the agricultural flat rate."

**R-FR-9 — VAT group (groupe TVA / assujetti unique).**
*Condition.* The user is part of a groupe TVA (assujetti unique) under art. 256 C CGI.
*Message.* "Your business is part of a groupe TVA (French VAT group) under art. 256 C CGI, where multiple related entities are treated as a single taxable person (assujetti unique). The group return is prepared by the representing entity with specific intra-group transaction handling that this skill does not support. You need the group representative's expert-comptable."

**R-FR-10 — Construction reverse charge (autoliquidation sous-traitance BTP).**
*Condition.* The user is a subcontractor in the construction sector (bâtiment et travaux publics) providing services to another business that is itself the main contractor, subject to the internal reverse charge under art. 283 2 nonies CGI.
*Message.* "You work as a sous-traitant in the BTP sector, where the autoliquidation de la sous-traitance applies under art. 283 2 nonies CGI. The construction reverse charge has strict conditions about when it applies, what invoicing mentions are required, and how it interacts with other obligations. This skill does not handle the BTP reverse charge. You need an expert-comptable with construction sector experience."

**R-FR-11 — Import with postponed accounting (autoliquidation à l'importation).**
*Condition.* The user imports goods from outside the EU and uses the generalized postponed accounting regime that became mandatory from 1 January 2022 (art. 1695 II CGI).
*Reason.* Since 2022, autoliquidation de la TVA à l'importation is **mandatory** for all taxable persons identified for VAT in France. The import TVA is declared and deducted on the same CA3 (in ligne A2 and cadre II respectively), with a specific reference to the importation. The bank statement does not show the import TVA as a separate flow because no cash changes hands for the TVA itself — this must be reconciled against the monthly data file provided by the DGDDI (customs) via the "service en ligne des données mensuelles de TVA à l'importation."
*Message.* "Your business imports goods from outside the EU. Since 1 January 2022, French import TVA is subject to mandatory autoliquidation under art. 1695 II CGI — you report the import TVA in ligne A2 of your CA3 and simultaneously deduct it in cadre II, with no cash payment at the border. The amounts must match the DGDDI monthly data file available via your espace professionnel on impots.gouv.fr. This reconciliation cannot be derived from a bank statement alone. You need to provide the DGDDI monthly data export, or this skill cannot reliably compute your import TVA position."

**R-FR-12 — DEB / Déclaration d'échanges de biens (EMEBI).**
*Condition.* The user's cross-border supplies of goods within the EU exceed the EMEBI threshold (post-2022 reform, statistical reporting is separated from tax reporting — the tax side is the TVA Etat Récapitulatif (ESL equivalent), the statistical side is the EMEBI).
*Message.* "Your business has intra-Community movements of goods that may trigger the EMEBI statistical declaration and the TVA Etat Récapitulatif (ESL) fiscal declaration. These are separate filings from the CA3 and are submitted via DEBWEB2. This skill handles only the CA3 return and flags the EMEBI / ESL obligation in the reviewer brief — it does not produce those filings. If your EMEBI obligations are not already being handled by an expert-comptable, you need to address that before filing."

**R-FR-13 — Cash accounting election (TVA sur les encaissements) mismatched with régime.**
*Condition.* Service providers by default are on TVA sur les encaissements (TVA due on cash receipt), while providers of goods are on TVA sur les débits (TVA due on invoice issue). A mismatch between the user's actual regime and the data basis is a refusal trigger.
*Message.* "Your business combines supplies of goods (TVA sur les débits — TVA due at invoice date) and services (TVA sur les encaissements — TVA due at cash receipt, unless you have opted for débits). The two bases interact in specific ways and the bank statement alone is insufficient to distinguish them without knowing which basis applies to each line. You need to confirm whether you have opted for TVA sur les débits for your services, and ideally provide your invoice register in addition to the bank statement. This skill v0.1 assumes a single basis throughout; mixed bases require an expert-comptable."

**R-FR-14 — Corsica or DOM-TOM operations.**
*Condition.* The user has operations in Corsica (with its specific reduced rates of 13%, 0.9%, etc.) or the DOM (Guadeloupe, Martinique, La Réunion, where the standard rate is 8.5% and special rates apply), or operations mixing France métropolitaine with these zones.
*Message.* "Your business appears to involve operations in Corsica or the DOM-TOM, which have specific VAT rates and rules different from France métropolitaine (Corsica: 20%, 13%, 10%, 2.1%, 0.9% under art. 297 CGI; DOM: 8.5% standard rate, reduced rates per art. 294 CGI). This skill v0.1 covers France métropolitaine only. You need an expert-comptable familiar with the Corsican or overseas territories VAT rules."

## Section 3 — French supplier pattern library (literal lookup table)

When you encounter these counterparties, apply the treatment indicated. The table is derived from public corporate disclosures, French tax authority guidance (BOFiP), and common business practice as of v0.1; reviewer must confirm for high-value transactions.

### 3.1 — French telecommunications

| Supplier | Typical IBAN / context | Treatment |
|---|---|---|
| Orange S.A. (ex France Télécom) | FR IBAN | Domestic 20% — fixed line, mobile, internet. Business contracts typically show "Orange Business Services" on invoices. No statutory cap on mobile deduction. Default deductible if business use is documented. |
| SFR (Société Française du Radiotéléphone — Altice) | FR IBAN | Same as Orange — domestic 20% |
| Bouygues Telecom | FR IBAN | Same |
| Free / Iliad S.A. | FR IBAN | Same |
| Sosh (Orange subsidiary) | FR IBAN | Consumer-tier Orange brand — treat as Orange but default to personal unless business use is established |
| Red by SFR | FR IBAN | Consumer-tier SFR — same treatment as Sosh |

### 3.2 — French energy, water, and utilities

| Supplier | Treatment |
|---|---|
| EDF (Électricité de France) | Domestic — rate depends on use. **Since 1 August 2025, electricity and gas subscriptions are all at 20% standard rate** (previously 5.5% for the subscription component). Consumption is at 20%. For business use, fully deductible. |
| ENGIE (ex GDF Suez) | Same structure as EDF — 20% from 1 August 2025, fully deductible for business use |
| TotalEnergies Électricité et Gaz | Same |
| Eni Gas & Power France | Same |
| Veolia Eau / Suez Eau France | Water supply — 5.5% reduced rate for water (art. 278-0 bis CGI), deductible if business use |

### 3.3 — French banks and financial services

| Supplier | Treatment |
|---|---|
| BNP Paribas | Bank fees — exempt under art. 261 C CGI (EU Article 135). Excluded from CA3. No input TVA. |
| Crédit Agricole (regional Caisses) | Same |
| Société Générale | Same |
| Crédit Mutuel | Same |
| BPCE (Banque Populaire, Caisse d'Épargne) | Same |
| La Banque Postale | Same — banking services exempt |
| Boursorama Banque, Fortuneo, Hello Bank, N26, Revolut Bank (France) | Same exemption |
| Stripe Payments Europe (Ireland) | EU reverse charge on the Stripe platform fee component — but the actual payment processing flows are not VAT events. See Example 4 in Section 4. |

### 3.4 — French insurance

| Supplier | Treatment |
|---|---|
| AXA France | Insurance premiums — exempt art. 261 C CGI (EU Article 135). Excluded from CA3. No input TVA. |
| Allianz France | Same |
| Generali France | Same |
| Groupama | Same |
| MAIF / MACIF / MAAF | Same |
| MMA (Mutuelles du Mans Assurances) | Same |
| CNP Assurances | Same |

### 3.5 — French tax authority, URSSAF, and statutory bodies

| Supplier / Counterparty | Treatment |
|---|---|
| DGFiP — impots.gouv.fr (tax payments) | Excluded — tax authority payment, not a supply. Flag for reviewer if unusual amount. Common line descriptions: "DGFIP", "Trésor Public", "IMPOT", "PLF". |
| URSSAF (Union de Recouvrement des cotisations de Sécurité Sociale et d'Allocations Familiales) | Excluded — social security contributions, outside VAT scope |
| Caisse Nationale de l'Assurance Maladie (CNAM) / CPAM | Excluded — health insurance contributions |
| Pôle Emploi / France Travail | Excluded — unemployment insurance |
| Chambre de Commerce et d'Industrie (CCI) — contribution annuelle | **Excluded — statutory contribution to a public-law body, NOT subject to VAT.** Do NOT claim input VAT on CCI annual fees regardless of invoice format. This is the French equivalent of the German IHK / Italian Camera di Commercio zero-VAT rule. |
| Chambre des Métiers et de l'Artisanat (CMA) | Excluded — same logic as CCI |
| Ordres professionnels (Ordre des avocats, Ordre des experts-comptables, Ordre des architectes, etc.) — cotisations annuelles | Excluded — statutory contribution to a public-law professional order, outside VAT scope |
| Commune / Mairie — taxes locales (taxe foncière, CFE — Cotisation Foncière des Entreprises, CVAE) | Excluded — local taxes, outside VAT scope. CFE and CVAE are corporate taxes, not VAT. |

### 3.6 — French postal service

| Supplier | Treatment |
|---|---|
| La Poste — timbres et courrier ordinaire (lettres, colis suivis via Colissimo ordinaire) | Services relevant du service universel postal are **exempt under art. 261-4-11° CGI**. No TVA charged, no input TVA recovery. |
| La Poste — Colissimo Expert, Chronopost | Competitive courier services are at 20% standard rate — these are NOT part of the universal service exemption |
| Chronopost (La Poste subsidiary) | Domestic 20% |
| DPD France | Domestic 20% |
| UPS France | Domestic 20% if billed from UPS France; if billed from UPS NL or elsewhere, EU reverse charge |
| FedEx France | Domestic 20% |
| DHL Express France | Domestic 20% if billed from DHL France; if billed from DHL Germany or elsewhere, EU reverse charge |

### 3.7 — French public transport and rail

| Supplier | Treatment |
|---|---|
| SNCF Voyageurs (TGV, Intercités, TER) | Passenger rail — **10% intermediate rate** under art. 279 b quater CGI |
| Trenitalia France (Paris-Lyon-Milan) | Same 10% |
| Ouigo (SNCF subsidiary) | Same 10% |
| RATP (Paris metro, bus, RER A and B) | 10% passenger transport |
| Île-de-France Mobilités (Navigo pass) | 10% passenger transport |
| Urban transport networks in Lyon (TCL), Marseille (RTM), Bordeaux (TBM), Lille (ilévia), Toulouse (Tisséo), Strasbourg (CTS), Nantes (TAN), Nice (Lignes d'Azur) | 10% passenger transport |
| Vinci Autoroutes / APRR / Sanef — péages autoroute | **20% standard rate** — road tolls, fully deductible if business use |
| BlaBlaCar (carpooling) | Not a VAT supply for the driver (peer-to-peer ride sharing); BlaBlaCar's own fee is a service subject to 20% but typically embedded |

### 3.8 — Airlines and air transport

| Supplier | Treatment |
|---|---|
| Air France — international flights | Exempt under art. 262 II 4° CGI (international air transport) |
| Air France — domestic flights (e.g. Paris-Nice, Paris-Toulouse) | 10% intermediate rate (art. 279 b quater) |
| Transavia France (Air France-KLM subsidiary) | Same treatment based on origin/destination |
| Ryanair (billed from Ireland) | International flights exempt; domestic French flights taxable at 10% but Ryanair billing entity is Irish — check invoice |
| easyJet | Similar — check billing entity |
| Lufthansa / KLM / Iberia for flights departing France | Generally billed from home country; apply place-of-supply rules |

### 3.9 — French hotels, restaurants, and hospitality

| Category | Treatment |
|---|---|
| French hotels (business travel) | **10% intermediate rate** on accommodation (art. 279 a bis CGI). Ancillary services (parking, minibar) at 20% or 10% depending on the item. For CA3 purposes apply 10% on the full gross unless the invoice breaks out ancillaries. Input TVA recoverable if the trip is documented business purpose. |
| French restaurants — food and non-alcoholic beverages | **10% intermediate rate** (art. 279 m CGI) |
| French restaurants — alcoholic beverages | **20% standard rate** — alcohol is always at the taux normal even when served in a restaurant |
| Business meals (frais de réception) | Deductible if business purpose is documented (client, supplier, staff meeting, conference). Unlike the German Bewirtungsbeleg formalism, France has less rigid documentation but the burden of proof on "intérêt direct de l'exploitation" lies with the taxpayer. Default: blocked pending documentation confirmation. |
| Bars / cafés | Coffee and non-alcoholic drinks 10%; alcohol 20%. Single-line bar receipts default to blocked (unclear business purpose). |
| French Airbnb (accommodation) | Via Airbnb Ireland UC — EU reverse charge on the Airbnb service fee component only. The accommodation itself is billed by the host (TVA-registered or franchise en base). Check the invoice structure. |

### 3.10 — French supermarkets and food retail

| Supplier | Treatment |
|---|---|
| Carrefour, Auchan, Leclerc, Intermarché, Casino, Monoprix, Franprix, Picard, Lidl France, Aldi France | Mixed — most food items at 5.5% (art. 278-0 bis D), prepared food and restauration at 10%, non-food items and alcohol at 20%. Default to blocked for single-transaction supermarket purchases (assume private provisioning) unless clear business purpose in description. |
| Metro Cash & Carry France | B2B wholesaler — presumption shifts slightly toward business use, but still default blocked without specific description |

### 3.11 — Fuel stations

| Supplier | Treatment |
|---|---|
| TotalEnergies stations, BP France, Shell France, Esso France, Avia, Intermarché carburant, Leclerc carburant | Domestic 20% on fuel. **Input TVA on fuel for passenger vehicles (véhicules de tourisme) is deductible at 80% for both diesel and essence since 2022** (art. 298 4° CGI — the equalization was phased in between 2017 and 2022). Commercial vehicles (véhicules utilitaires, camions) get 100% deduction. **Passenger vehicles themselves (purchase, lease, repair, insurance) — input TVA is entirely blocked under art. 206 IV Annexe II CGI, which is stricter than the fuel rule.** |

### 3.12 — Universal SaaS suppliers (EU reverse charge — autoliquidation)

These are the same universal patterns that appear in Germany and Italy. The treatment is EU reverse charge (autoliquidation under art. 283-2 CGI, implementing art. 196 of the directive): the supplier does not charge TVA, the user self-accounts for 20% output TVA (reported in ligne A2 on the CA3) and simultaneously claims 20% input TVA (reported in cadre II), net cash zero.

| Supplier | Billing entity | Treatment |
|---|---|---|
| Google Ireland Ltd | IE IBAN | EU autoliquidation 20% — Google Ads, Google Workspace, Google Cloud (EMEA) |
| Microsoft Ireland Operations | IE IBAN | EU autoliquidation 20% — Microsoft 365, Azure, GitHub Enterprise |
| Adobe Systems Software Ireland | IE IBAN | EU autoliquidation 20% — Creative Cloud, Acrobat |
| LinkedIn Ireland Unlimited | IE IBAN | EU autoliquidation 20% |
| Meta Platforms Ireland | IE IBAN | EU autoliquidation 20% — Facebook Ads, Instagram Ads |
| Slack Technologies Ireland | IE IBAN | EU autoliquidation 20% |
| Dropbox International Unlimited Company | IE IBAN | EU autoliquidation 20% |
| Atlassian Pty (Ireland) | IE IBAN | EU autoliquidation 20% — Jira, Confluence |
| Stripe Payments Europe Ltd | IE IBAN | EU autoliquidation 20% — Stripe platform fees |
| Uber BV | NL IBAN | EU autoliquidation 20% — Uber ride bookings and Uber for Business |
| Booking.com B.V. | NL IBAN | EU autoliquidation 20% — commission on hotel bookings |
| Zoom Video Communications | US entity billing EU | Non-EU reverse charge art. 283-2 — autoliquidation 20% |
| Fiverr International | Israeli entity | Non-EU reverse charge art. 283-2 — autoliquidation 20% |

### 3.13 — AWS (the branch-billing exception)

AWS EMEA SARL bills most EU customers through local branches with local VAT registration. For French customers, the billing entity may be "AWS EMEA SARL Succursale France" or similar, with a French SIREN / numéro de TVA intracommunautaire and 20% French TVA charged on the invoice. **If the IBAN is French and the invoice shows French TVA, treat as domestic 20% (not as reverse charge).** If the IBAN is Luxembourg and the invoice shows no VAT with a reverse-charge note, treat as EU autoliquidation. This is the same exception structure as the German and Italian AWS cases. Always check the invoice rather than defaulting to one treatment or the other.

### 3.14 — Apple and consumer-tier app stores

| Supplier | Treatment |
|---|---|
| Apple Distribution International (Ireland) — Apple One, iCloud+, App Store | Check billing entity on invoice. Consumer subscriptions billed on a personal Apple ID are typically personal expenses — default to excluded. Apple Business Essentials billed on a business account with SIREN is a B2B service — EU autoliquidation 20%. |
| Google Play Store consumer purchases | Similar — default excluded as personal unless clearly business |

### 3.15 — Anthropic and AI services

| Supplier | Treatment |
|---|---|
| Anthropic PBC — Claude Pro (individual tier) | Consumer-tier on personal email → default excluded as personal |
| Anthropic PBC — Claude Team / Claude Enterprise | Business tier with SIREN on invoice → non-EU reverse charge art. 283-2, autoliquidation 20% |
| OpenAI LLC — ChatGPT Plus (individual) | Default excluded as personal |
| OpenAI LLC — ChatGPT Team / Enterprise | Non-EU reverse charge autoliquidation 20% |
| Mistral AI (French company) | Domestic 20% — Mistral is a French company based in Paris, so supplies to French customers carry French TVA directly |

### 3.16 — Amazon (intra-Community acquisitions and local billing)

| Pattern | Treatment |
|---|---|
| Amazon.fr marketplace sale billed by a French seller | Domestic 20% (or 5.5% for books under art. 278-0 bis D), check invoice |
| Amazon EU Sarl with LU IBAN | Intra-Community acquisition of goods — report in ligne A3 with self-assessed 20% and deduct in cadre II |
| Amazon Web Services (see 3.13) | See AWS branch exception |
| Amazon consumer purchases on .fr with an FR IBAN | Depends on the seller — if the invoice shows a French SIREN it's domestic; if it shows an LU VAT number it's an intra-Community acquisition |

## Section 4 — Worked examples

The worked examples below use a hypothetical client: **Sophie Laurent, graphic designer in Toulouse (graphiste indépendante), operating as an EURL (entreprise unipersonnelle à responsabilité limitée) under the régime réel normal, SIREN 823456789, Atelier in rue de la Dalbade 15 Toulouse, monthly CA3 filer.** This client does NOT correspond to any test fixture used to validate this skill — the examples are drawn from a fictional profile distinct from the Hamburg UX designer (Germany) and the Milan architect (Italy).

### Example 1 — The AWS branch exception

Bank line: `AWS EMEA SARL SUCCURSALE FRANCE -780.00 EUR "AWS compute charges"`. IBAN on payment: FR.

**Wrong treatment:** EU autoliquidation under art. 283-2. This is the default assumption for "AWS EMEA SARL" because the parent entity is Luxembourg.

**Right treatment:** Domestic 20% — the "Succursale France" designation and the French IBAN together indicate AWS is billing from its French branch with a French SIREN and French TVA. The invoice will show French TVA charged. Treat as a normal domestic purchase: net 650.00, TVA 130.00 deductible in cadre II (autres biens et services). Post to ligne A1 on the input side — wait, inputs don't go to A1, A1 is for sales. The input side goes in cadre II only; the net taxable amount for a pure input does not appear on the output cadres. Correct CA3 mapping: net is implicit, TVA déductible 130.00 in cadre II "autres biens et services."

**Reviewer note:** confirm by inspecting the actual AWS invoice. The bank statement alone is not sufficient to confirm branch billing.

### Example 2 — The passenger vehicle full block (stricter than Germany and Italy)

Bank line: `TOTAL ENERGIES STATION TOULOUSE -95.00 EUR`. Sophie's EURL owns a passenger car (véhicule de tourisme) used mostly for client visits in the Toulouse metro area.

**Germany/Italy approach:** partial cap (Germany 50% default, Italy 40%). You might expect a similar partial deduction in France.

**Right French treatment:** This is **fuel** for a passenger vehicle, which is governed by art. 298 4° CGI — **80% of the TVA on fuel is deductible** regardless of vehicle category (since 2022, diesel and gasoline are equalized).

- Gross: €95.00
- Net: 95 / 1.20 = €79.17
- Full input TVA at 20%: €15.83
- Recoverable at 80%: €12.67

For cadre II: €12.67. For the blocked portion (€3.17): disclose in the brief.

**Note on vehicle itself:** if the same bank statement showed a line for the vehicle's purchase, lease, repair, or insurance, that would be **entirely blocked** under art. 206 IV Annexe II CGI — input TVA on passenger vehicles themselves is 100% non-deductible, which is stricter than Germany's and Italy's partial caps. Only fuel has the 80% rule. This distinction is important: fuel is 80%, everything else about the passenger car is 0%. If the bank line says "CARROSSERIE MARTIN -450 EUR repair péage voiture" the right treatment is fully blocked, not 80%.

### Example 3 — Hotel at 10% intermediate rate

Bank line: `HOTEL DU CAPITOLE TOULOUSE -156.00 EUR "nuitée conférence web design"`.

**Treatment:** French hotels are at the 10% intermediate rate (art. 279 a bis CGI), not the standard 20%.

- Gross: €156.00
- Net: 156 / 1.10 = €141.82
- TVA at 10%: €14.18 — fully recoverable in cadre II "autres biens et services" because the description "nuitée conférence web design" establishes business purpose

If you default to 20% by mistake (as you would for Germany), you would compute TVA as 156/1.20 = 130, TVA 26.00 — that's €11.82 of TVA that doesn't exist. The CA3 would overstate input TVA by €11.82 and the return would be rejected on audit reconciliation against the hotel's own CA3.

The 10% rate for hotels is not a small-cash-impact quirk — it materially changes the recoverable TVA on any business trip line and it must be applied correctly.

### Example 4 — Stripe platform fees (the payment processor pattern)

Bank line: `STRIPE PAYMENTS EUROPE -47.30 EUR "Stripe fee April 2026"`. IBAN: IE.

**What's happening.** Sophie uses Stripe to accept payments from her clients. Her clients pay via Stripe, Stripe takes a 2.9% + €0.25 fee per transaction, and transfers the net to Sophie's account. The fee that Stripe charges for this service is a B2B service from an Irish supplier to a French business — it qualifies for EU autoliquidation under art. 283-2 CGI.

**Treatment of the Stripe fee line:**
- Net: €47.30 (the fee is stated net of TVA because Stripe does not charge French TVA on a B2B EU service)
- Self-assessed output TVA at 20%: €9.46 in ligne A2
- Input TVA deduction at 20%: €9.46 in cadre II
- Net cash effect on the CA3: zero

**Common misclassification:** treating the Stripe fee as a "bank fee" (exempt art. 261 C) because Stripe is a financial services company. This is wrong — the Stripe platform fee is consideration for an electronic service, not for banking or payment-initiation services in the art. 261 C sense. BOFiP guidance on this has evolved, but the current DGFiP position is that payment service platform fees from non-French EU providers are subject to reverse charge, not to the banking exemption. Reviewer should confirm for the specific period.

**Separate question:** the actual money flows from clients through Stripe to Sophie are NOT VAT events on their own. The VAT is on Sophie's invoices to her clients (output TVA on each invoice) and on Stripe's fees (reverse charge as above). The bank line showing "STRIPE PAYMENTS EUROPE +4,500.00 EUR" when a client payment arrives is a transfer, not a sale — the underlying sale is the invoice Sophie issued, which is the VAT event. Make sure the classification separates these correctly.

### Example 5 — Business meal (frais de réception)

Bank line: `RESTAURANT MICHEL SARRAN TOULOUSE -284.00 EUR "déjeuner client Airbus"`.

**Treatment:** the description "déjeuner client Airbus" establishes business purpose. French frais de réception are deductible if "engagés dans l'intérêt direct de l'exploitation" and properly documented (BOFiP-TVA-DED-30-30-30). Unlike Germany's formal Bewirtungsbeleg requirement, France has less prescriptive documentation, but the burden of proof is on the taxpayer.

- Gross: €284.00
- Split: food at 10%, wine at 20% — restaurants typically issue a split invoice. Without the invoice in hand, default to the conservative treatment: assume 100% at the higher 20% rate, which underestimates the recoverable TVA and is the conservative direction.
- Conservative computation: net 236.67, TVA 47.33, fully deductible
- Realistic computation (with invoice): the food portion (say €220) at 10% = TVA €20.00, the wine (say €64) at 20% = TVA €10.67, total TVA €30.67

The conservative approach recovers more TVA than the realistic approach because it assumes the higher rate across the whole amount. This is *anti-conservative* for the tax authority — we are overstating deduction. The correct conservative default is the **lower** TVA amount, which means assuming food at 10% across the whole gross, yielding TVA of €25.82. Block this at zero until the invoice is provided and then the user can compute the actual split.

**Reviewer brief entry:** flag this as a Tier 2 question — the invoice needs to be inspected to split food from alcohol at 10% vs 20%. Cash swing on this single line is roughly €5-20 depending on alcohol proportion.

### Example 6 — CCI annual contribution

Bank line: `CCI HAUTE GARONNE -120.00 EUR "cotisation annuelle 2026"`.

**Wrong treatment:** Assume an invoice was issued with 20% TVA and claim €20 input TVA.

**Right treatment:** Excluded. The Chambre de Commerce et d'Industrie (CCI Haute-Garonne in this case, for Toulouse) is a public-law body (établissement public administratif) and the cotisation annuelle is a statutory contribution, NOT consideration for a taxable supply. No TVA is charged. There is no input TVA to recover. Mark the line as excluded with reason "CCI statutory contribution, outside VAT scope."

**This is the French equivalent of the German IHK zero-VAT rule and the Italian Camera di Commercio rule.** The same class of error (hallucinated input VAT on a statutory contribution) is the single highest-risk attention failure in all three countries. Do not let it past.

## Section 5 — Tier 1 deterministic rules (compressed)

These are the rules applied silently by the classifier when the data unambiguously resolves the treatment.

**5.1 — Domestic B2B sale to a French SIREN customer.** 20% standard, or reduced rate per CGI if the goods/services qualify. Report in cadre I at the appropriate rate and ligne A1.

**5.2 — Domestic B2C sale.** Same rates. Same reporting. Different invoice requirements (simplified invoice allowed below threshold).

**5.3 — Intra-Community supply of goods to an EU VAT-registered customer.** Exempt under art. 262 ter I CGI (directive art. 138). Report in ligne B1 with no output VAT. Triggers ESL (État Récapitulatif des Clients for services, or equivalent for goods via EMEBI). Conditions: customer VAT verified on VIES, goods physically transported out of France, proof of transport retained, invoice shows both numéros de TVA intracommunautaire and the "Exonération TVA, art. 262 ter I du CGI" note. If any condition fails, reclassify as domestic 20%.

**5.4 — B2B service to a VAT-registered EU customer.** Exempt / non-taxable in France under art. 259-1° CGI (directive art. 44). Place of supply is the customer's country. Report in ligne B3. Triggers ESL.

**5.5 — B2B service to a non-EU customer.** Non-taxable in France under art. 259-1° CGI. Report in ligne B3 (exempt operations). No ESL for non-EU recipients.

**5.6 — Purchase from EU supplier (goods).** Acquisition intracommunautaire under art. 256 bis CGI. Self-assess 20% output TVA in ligne A3 and claim 20% input TVA in cadre II (net cash zero unless partial exemption or blocked input). Requires invoice from EU supplier with both numéros de TVA intracommunautaire.

**5.7 — Purchase of services from EU supplier (reverse charge — autoliquidation).** Under art. 283-2 CGI and art. 44 of the directive. Self-assess 20% in ligne A2, claim 20% in cadre II. Net zero. The Irish/Luxembourg SaaS stack (Google, Microsoft, Adobe, Slack, Dropbox, etc.) is the dominant case.

**5.8 — Purchase from non-EU supplier (services).** Reverse charge under art. 283-2 CGI. Same mechanics as EU reverse charge — self-assess 20% in ligne A2, claim 20% in cadre II, net zero. Zoom, Fiverr, US-based consultants, Anthropic business tier all fall here.

**5.9 — Import of goods from outside the EU.** **Mandatory autoliquidation under art. 1695 II CGI since 1 January 2022** — report import TVA in ligne A2 and deduct in cadre II. NO cash payment at the border for the TVA itself. The amounts must be reconciled against the DGDDI monthly data file. See R-FR-11 — this skill does not handle imports without the DGDDI export.

**5.10 — Exempt-without-credit supplies.** Sales of banking / insurance / medical / educational services are exempt under art. 261 CGI. If the business makes any exempt supplies above de minimis, fire R-FR-5 (partial exemption / prorata).

**5.11 — Passenger vehicle expenses.** Blocked under art. 206 IV Annexe II CGI — 0% deductible on purchase, lease, repair, insurance, maintenance. **Exception: fuel at 80%** under art. 298 4° CGI. Commercial vehicles: 100% if used for business.

**5.12 — Business gifts above €73 per recipient per year (2025 threshold, revalued annually).** Blocked under art. 206 IV-2-3° Annexe II CGI. Below €73: deductible.

**5.13 — Frais de réception (business meals).** Deductible if business purpose is documented ("intérêt direct de l'exploitation"). Default blocked pending documentation.

**5.14 — Standard rate applies by default.** If the rate is not explicitly identified in the supplier pattern library or the description, assume 20% (art. 278 CGI — taux normal as the residual rule).

## Section 6 — France-specific Tier 2 ambiguity catalogue

Applied after the EU-wide T2-EU catalogue in `eu-vat-directive` Section 12.

**T2-FR-1 — Restaurant alcohol split.** *Pattern:* restaurant bill where food (10%) and alcohol (20%) are likely mixed. *Why:* bank line doesn't split. *Question:* "Does your invoice split food from alcoholic beverages?" *Default:* blocked pending invoice.

**T2-FR-2 — Passenger vehicle vs commercial vehicle.** *Pattern:* fuel or vehicle expense on an unspecified vehicle. *Why:* bank line doesn't distinguish véhicule de tourisme from véhicule utilitaire. *Question:* "Is the vehicle a passenger car (véhicule de tourisme — fuel 80% / vehicle itself 0%) or a commercial vehicle (véhicule utilitaire — 100%)?" *Default:* passenger car.

**T2-FR-3 — Electricity/gas rate change (post-1 August 2025).** *Pattern:* EDF or ENGIE line that may straddle the 1 August 2025 rate change. *Why:* invoices spanning the cutover may apply different rates to the subscription component vs consumption. *Question:* "For the period before 1 August 2025, apply 5.5% on subscription; after, 20%. Is your invoice period entirely after 1 August 2025?" *Default:* assume entirely after (simplest case) unless evidence otherwise.

**T2-FR-4 — E-invoicing readiness.** *Pattern:* the current date is approaching or past the user's applicable e-invoicing deadline (1 September 2026 for receive-all / large-issue, 1 September 2027 for SME-issue). *Why:* compliance status is not on the bank statement. *Question:* "Are you set up with a Plateforme Agréée (PA) accredited by the DGFiP for e-invoicing?" *Default:* if user is an SME and date is before September 2027, note in brief but do not refuse; if after, fire R-FR-4.

**T2-FR-5 — TVA sur les encaissements vs débits.** *Pattern:* service provider. *Why:* default basis for services is TVA sur les encaissements (cash receipt), not TVA sur les débits. *Question:* "For your services, are you on TVA sur les encaissements (default, TVA due at payment) or have you opted for TVA sur les débits (TVA due at invoice issue)?" *Default:* encaissements for services, débits for goods.

**T2-FR-6 — ESL / EMEBI obligations.** *Pattern:* intra-Community supplies or acquisitions in the period. *Why:* whether the user is already filing ESL and EMEBI is not on the bank statement. *Question:* "Do you already file the TVA Etat Récapitulatif (ESL) and the EMEBI statistical declaration for your cross-border EU flows?" *Default:* flag in brief; do not refuse.

**T2-FR-7 — Corsica or DOM-TOM operations.** *Pattern:* Corsican or overseas supplier/customer. *Why:* Corsica and DOM have specific rates. *Question:* confirms geographic scope. *Default:* if confirmed, fire R-FR-14.

## Section 7 — Excel working paper template (France-specific overlay)

The base specification is in `vat-workflow-base` Section 3. This section provides the France-specific overlay.

**Sheet 1 — "Transactions".** 12 columns: Date, Counterparty, Description, Gross (EUR), Net (EUR), TVA (EUR), Rate, CA3 ligne, Treatment, Default? (Y/N), Q-Ref, Excluded reason.

**Sheet 2 — "CA3 Summary".** Aggregates by CA3 ligne:

| Ligne | Description | Formula |
|---|---|---|
| A1-20% | Ventes France 20% | `=SUMIFS(Transactions!E:E,Transactions!H:H,"A1",Transactions!G:G,0.20)` |
| A1-10% | Ventes France 10% | `=SUMIFS(Transactions!E:E,Transactions!H:H,"A1",Transactions!G:G,0.10)` |
| A1-5.5% | Ventes France 5.5% | `=SUMIFS(Transactions!E:E,Transactions!H:H,"A1",Transactions!G:G,0.055)` |
| A2 | Autres opérations imposables (autoliquidation) | `=SUMIFS(Transactions!E:E,Transactions!H:H,"A2")` |
| A3 | Acquisitions intracommunautaires | `=SUMIFS(Transactions!E:E,Transactions!H:H,"A3")` |
| B1 | Livraisons intracommunautaires | `=SUMIFS(Transactions!E:E,Transactions!H:H,"B1")` |
| B2 | Exportations hors UE | `=SUMIFS(Transactions!E:E,Transactions!H:H,"B2")` |
| B3 | Services intra-UE et non-UE | `=SUMIFS(Transactions!E:E,Transactions!H:H,"B3")` |
| TVA collectée | Output VAT total | `=SUMIFS(Transactions!F:F,Transactions!I:I,"output")` |
| TVA déductible immobilisations | Input VAT on fixed assets | `=SUMIFS(Transactions!F:F,Transactions!I:I,"input-immo")` |
| TVA déductible autres | Input VAT other | `=SUMIFS(Transactions!F:F,Transactions!I:I,"input-autres")` |
| Ligne 16 | TVA nette due | `=TVA collectée - TVA déductible immobilisations - TVA déductible autres` |

**Sheet 3 — "Return Form".** Lays out the CA3 cadres with the final values.

**Color conventions:** yellow highlight on every row with Default? = Y.

**Mandatory recalc step:** `python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/france-vat-<period>-working-paper.xlsx`. Verify `status: success, total_errors: 0`.

## Section 8 — French bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Section 1 Step 6, plus these France-specific patterns.

**CSV format conventions.** French business banks export in varied formats. Common columns: Date opération, Date valeur, Libellé, Débit, Crédit, Solde, Référence. Date format: DD/MM/YYYY. Decimal separator: comma (1 234,56 EUR). Thousand separator: space (not comma, not period). Currency: EUR.

**Common French bank description codes:**
- VIR = virement (wire transfer)
- PRLV = prélèvement (direct debit)
- CB = carte bancaire (card payment)
- RETRAIT DAB = cash withdrawal from ATM
- REMISE CHEQUE = check deposit
- AGIOS / INTERETS DEBITEURS = overdraft interest (exempt art. 261 C)
- COMMISSIONS BANCAIRES = bank fees (exempt art. 261 C)
- IMPOT / PLF / DGFIP = tax authority payment (excluded)
- URSSAF = social security contribution (excluded)
- SALAIRE / PAIE = payroll (excluded as payroll, not a VAT event)
- CVAE / CFE = corporate tax (excluded)

**Internal transfers and exclusions.** Virement interne between own accounts, retrait DAB, remise chèque, rémunération du dirigeant (gérant EURL), dividendes, apports en compte courant, remboursement d'emprunt principal (interest may be exempt), URSSAF, impôts (IS, CFE, CVAE, DGFiP payments), salaires.

**French supplier name abbreviation patterns:**
- "CRED AGR" / "CAM" / "C AGR" — Crédit Agricole
- "SG" / "STE GENERALE" — Société Générale
- "BNPP" — BNP Paribas
- "CMB" / "CRED MUT" — Crédit Mutuel
- "ORANGE" / "FR TELECOM" (legacy) — Orange
- "EDF" — Électricité de France
- "GDF" / "ENGIE" — Engie
- "SNCF" — Société Nationale des Chemins de Fer
- "RATP" — Régie Autonome des Transports Parisiens

**SIREN and SIRET in descriptions.** French bank descriptions sometimes include the counterparty's SIREN (9 digits) or SIRET (14 digits). These are useful for verifying counterparty identity. The first 9 digits of a SIRET are the SIREN; the last 5 are the NIC (numéro interne de classement) identifying the specific établissement.

## Section 9 — Onboarding (fallback only — use after Step 3 of the workflow base)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first (Step 3) and only confirming with the user in Step 4. The questions below are a *fallback* — ask only the questions the data could not answer at all.

**Q1. Regime check.** "Are you in the régime réel normal (CA3), régime réel simplifié (CA12), or franchise en base de TVA?" Only régime réel normal is supported by this skill.

**Q2. Micro-entrepreneur status.** "Are you operating as a micro-entrepreneur? If yes, have you explicitly opted for TVA?" Default assumption: micro-entrepreneur means franchise en base unless explicitly told otherwise (fires R-FR-3).

**Q3. Filing frequency.** "Are you on monthly or quarterly CA3 filing?" Monthly is the default; quarterly only if annual TVA due is below €4,000.

**Q4. E-invoicing PA status.** "Are you set up with a Plateforme Agréée (PA) for e-invoicing? If yes, which one?" Context-dependent refusal per R-FR-4.

**Q5. Partial exemption check.** "Does your business earn any exempt income (interest, insurance commission, medical services, residential rent, educational services)?" If yes, fire R-FR-5.

**Q6. Construction sector check.** "Do you work as a sous-traitant in the BTP sector?" If yes, fire R-FR-10.

**Q7. Import activity.** "Do you import goods from outside the EU? If yes, do you have access to the DGDDI monthly data file for import TVA reconciliation?" If yes to imports but no to DGDDI data, fire R-FR-11.

**Q8. Vehicle use.** "Do you have a vehicle used for the business? Is it a véhicule de tourisme (0% deduction except 80% on fuel) or a véhicule utilitaire (up to 100%)?"

**Q9. Geographic scope.** "Are all your operations in France métropolitaine, or do you have any operations in Corsica or the DOM-TOM?" If yes to Corsica/DOM, fire R-FR-14.

**Q10. TVA basis.** "For your services, are you on TVA sur les encaissements or have you opted for TVA sur les débits?" This affects how bank statement data maps to VAT events.

## Section 10 — Reference material

### Validation status

This is v0.1 of `france-vat-return`. Drafted in April 2026 from public sources accessed at draft time, including Légifrance (Code général des impôts articles 256 through 298 sexdecies), the Bulletin officiel des finances publiques (BOFiP), DGFiP guidance on the e-invoicing reform, and various expert-comptable commentary on 2026 rate changes. **Not practitioner-validated.** The supplier pattern library, refusal catalogue, Tier 1 rules, and worked examples are all derived from public sources and should be treated as v0.1 — likely to contain errors that only a French expert-comptable would catch.

### Critical pending updates (CIBS recodification)

**Ordonnance n° 2025-1247 of 17 December 2025** moves VAT legislation from the Code général des impôts (CGI) into a new Code des Impositions sur les Biens et Services (CIBS), effective **1 September 2026**. This v0.1 cites CGI articles throughout because they are still in force as of the draft date. **From 1 September 2026, all article citations in this skill will need wholesale updating to reference the CIBS.** The substantive rules are being transposed, not changed, but the article numbering and code references will all shift. A v0.2 of this skill will need to be issued before or by 1 September 2026 to reflect the recodification. Until then, any CGI citation in this skill should be understood as "the rule in CGI art. X, which will become CIBS art. Y from 1 September 2026."

### E-invoicing rollout — verified state as of April 2026

Based on the February 2026 Finance Bill (PLF 2026), DGFiP guidance, and current BOFiP:

- **1 September 2026:** all French VAT-registered businesses must be able to receive e-invoices via a PA. Large enterprises (grandes entreprises, GE) and intermediate-sized enterprises (entreprises de taille intermédiaire, ETI) must also issue e-invoices from this date. Option to extend to 1 December 2026.
- **1 September 2027:** SMEs (PME) and micro-enterprises that are TVA-registered must issue e-invoices from this date. Option to extend to 1 December 2027.
- **Terminology change:** "Plateforme Agréée (PA)" replaces the earlier "Plateforme de Dématérialisation Partenaire (PDP)." The PPF (Portail Public de Facturation) is scaled back to directory and data hub functions — it no longer offers free billing services, so all businesses must use an accredited PA.
- **Pilot phase:** ran from 24 February 2026 through end of August 2026 with 60,000 businesses voluntarily testing the system.

These dates and rules are as of April 2026 and are subject to change via subsequent Finance Bills or DGFiP guidance. R-FR-4 should be treated as the live refusal mechanism but the specific dates in its conditions may need updating.

### Specific known limitations

1. The CA3 field mapping in Section 7 is simplified relative to the actual CA3 form, which has more granular lignes for specific transaction types. v0.1 covers the common cases.
2. The ESL (TVA Etat Récapitulatif) and EMEBI (statistical) filings are flagged but not generated. Skill produces only the CA3.
3. The DGDDI monthly data file reconciliation for import TVA is not implemented; imports trigger R-FR-11.
4. Franchise en base, régime réel simplifié, micro-entreprise (without TVA option), margin schemes, travel agents, agricultural flat rate, prorata, VAT group, BTP reverse charge, and Corsica/DOM-TOM are all in the refusal catalogue.
5. Prorata de déduction (partial exemption) is completely out of scope — the French three-coefficient system is not modelled.
6. TVA sur les encaissements vs débits is flagged as a Tier 2 question but not modelled as a structural difference in the skill.
7. Rate of 8.5% in the DOM, 13% in Corsica, and various other territorial rates are not supported.
8. Rate change cutover on 1 August 2025 (electricity/gas subscriptions from 5.5% to 20%) and 1 October 2025 (photovoltaic panels from 10% to 5.5%) are noted as Tier 2 flags but not automatically handled.

### Sources

1. Code général des impôts (CGI): https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577
2. Bulletin officiel des finances publiques (BOFiP): https://bofip.impots.gouv.fr
3. DGFiP e-invoicing portal: https://www.impots.gouv.fr/facturation-electronique
4. Ordonnance n° 2025-1247 of 17 December 2025 (CIBS recodification): https://www.legifrance.gouv.fr
5. Loi de finances pour 2026 (PLF 2026, adopted 2 February 2026)
6. EU Directive 2006/112/EC via `eu-vat-directive` v0.1
7. Industry commentary: EY France tax alerts, BDO France e-invoicing updates, Pagero compliance portal, Taxually, Vertex, Avalara (as background cross-reference for dates and terminology; primary sources above are authoritative)

### Change log

- **v0.1 (April 2026):** Initial draft following the germany-vat-return v0.3.1 and italy-vat-return v0.1 architecture. Three-tier model: loads on top of vat-workflow-base v0.2.0 and eu-vat-directive v0.1. Covers régime réel normal monthly/quarterly CA3 only. Fourteen R-FR refusals including the phased e-invoicing mandate (R-FR-4) with date-dependent handling. Supplier pattern library has roughly 55 entries across 16 sub-categories. Six worked examples from a hypothetical Toulouse graphic designer (Sophie Laurent). Not practitioner-validated. Drafted after live web search of current French e-invoicing state and 2026 TVA rates to avoid training-data staleness; sources accessed April 2026. CIBS recodification flagged as a known pending update (1 September 2026).

### Self-check (v0.1 of this document)

1. Quick reference at top: yes (Section 1).
2. Refusal catalogue distinct from EU-wide: yes (14 R-FR refusals in Section 2, on top of R-EU-1 through R-EU-12).
3. Supplier library as literal lookup table: yes (Section 3, 16 sub-tables).
4. Worked examples drawn from a hypothetical non-test client distinct from Germany/Italy: yes (Toulouse graphic designer Sophie Laurent, Section 4 — distinct from Hamburg UX designer and Milan architect).
5. Tier 1 rules compressed: yes (Section 5, fourteen rules).
6. Tier 2 catalogue distinct from EU-wide: yes (seven T2-FR entries in Section 6).
7. Excel template specification with mandatory recalc: yes (Section 7).
8. French bank statement reading guide: yes (Section 8).
9. Onboarding as fallback only: yes (Section 9, ten questions).
10. Reference material at bottom with validation status: yes (Section 10).
11. AWS branch exception explicit: yes (Section 3.13 and Example 1).
12. Apple consumer trap explicit: yes (Section 3.14).
13. CCI zero-VAT explicit: yes (Section 3.5 and Example 6).
14. Passenger vehicle 0% + 80% fuel rule explicit: yes (Section 3.11, Section 5.11, and Example 2).
15. Hotel 10% rate explicit: yes (Section 3.9 and Example 3).
16. Stripe platform fee pattern explicit: yes (Section 4 Example 4).
17. E-invoicing phased rollout with date-dependent refusal: yes (R-FR-4 in Section 2).
18. CIBS recodification flagged: yes (Section 10).

## End of France VAT Return Skill v0.1

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.2.0 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a CA3 without all three files loaded.

**Practitioner review note:** this skill has not been reviewed by a French expert-comptable. Before this skill is used for any real return, it should be reviewed line-by-line by a practitioner with experience in the régime réel normal and CA3 filings. The refusal catalogue, the supplier pattern library rates, and the e-invoicing mandate refusal timing are the three areas most likely to need practitioner correction.

**CIBS recodification note:** this skill cites CGI articles. From 1 September 2026, those articles move to the CIBS under Ordonnance n° 2025-1247. A v0.2 will be needed before that date to update all citations.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
