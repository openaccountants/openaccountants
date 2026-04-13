---
name: algeria-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Algeria TVA (Taxe sur la Valeur Ajoutee) return (G50 declaration) for any client. Trigger on phrases like "prepare TVA return", "Algeria VAT", "G50 declaration", "declaration TVA", "DGI return", or any request involving Algeria VAT filing. Also trigger when classifying transactions for TVA purposes from bank statements, invoices, or other source data. This skill covers Algeria only and standard TVA-registered businesses under the regime reel. IFU (forfaitaire) taxpayers, hydrocarbon-sector entities, military procurement, and special conventions are in the refusal catalogue. ALWAYS read this skill before touching any Algeria TVA work.
version: 2.0
---

# Algeria TVA Return Skill (G50 Declaration) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Algeria (People's Democratic Republic of Algeria) |
| Standard rate | 19% (taux normal) |
| Reduced rate | 9% (taux reduit: basic foodstuffs, pharmaceuticals, agricultural inputs, tourism/hotel, IT equipment, renewable energy) |
| Exempt supplies | Bread, semolina, flour, fresh milk, financial services (interest), medical (public), education, exports (exempt with right to deduct) |
| Return form | G50 (Serie G50 monthly declaration — includes TVA, TAP, and withholding sections) |
| Filing portal | https://jibayatic.mf.gov.dz (Jibayatic) |
| Authority | Direction Generale des Impots (DGI) |
| Currency | DZD (Algerian Dinar) only |
| Filing frequency | Monthly (regime reel); IFU taxpayers do not file TVA |
| Deadline | 20th of the month following the period |
| Contributor | Open Accountants Skills Registry |
| Validated by | Pending — requires validation by a licensed commissaire aux comptes in Algeria |
| Validation date | Pending |

**Key G50 TVA lines (the lines you will use most):**

| Line | Meaning |
|---|---|
| 1 | CA taxable a 19% (standard-rated sales net) |
| 2 | CA taxable a 9% (reduced-rated sales net) |
| 3 | CA exonere (exempt supplies net) |
| 4 | Exportations (export sales net, exempt with deduction) |
| 5 | Total CA (derived: 1+2+3+4) |
| 6 | TVA collectee a 19% (output TVA on Line 1) |
| 7 | TVA collectee a 9% (output TVA on Line 2) |
| 8 | TVA sur autoliquidation (reverse charge output) |
| 9 | Regularisations (adjustments) |
| 10 | Total TVA brute (derived: 6+7+8+9) |
| 11 | TVA sur achats de biens et services (input TVA on operating purchases) |
| 12 | TVA sur immobilisations (input TVA on capital goods) |
| 13 | TVA sur importations (customs TVA) |
| 14 | TVA autoliquidation input (reverse charge input) |
| 15 | Exclusions (blocked items) |
| 16 | Total TVA deductible (derived: 11+12+13+14-15) |
| 17 | TVA due (derived: 10-16) |
| 18 | Precomptes (advance TVA withholdings received) |
| 19 | Credit reporte (prior period credit) |
| 20 | TVA a payer / Credit (derived: 17-18-19) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 19% |
| Unknown TVA status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Algeria |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown SaaS billing entity | Reverse charge from non-resident (Line 8/14) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | DZD 5,000,000 |
| HIGH tax-delta on a single conservative default | DZD 500,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net TVA position | DZD 10,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Algerian or international business bank: BNA, BEA, CPA, BADR, BDL, Societe Generale Algerie, AGB, Natixis Algerie, Al Baraka, or any other.

**Recommended** — sales invoices for the period, purchase invoices for any input TVA claim above DZD 500,000, the client's NIF (Numero d'Identification Fiscale) in writing.

**Ideal** — complete invoice register, prior period G50, reconciliation of credit reporte (Line 19).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This G50 was produced from bank statement alone. The reviewer must verify that input TVA claims above DZD 500,000 are supported by compliant invoices with valid NIF and that all reverse-charge classifications match the supplier's invoice."

### Algeria-specific refusal catalogue

**R-DZ-1 — IFU (forfaitaire) taxpayer.** *Trigger:* client is under the Impot Forfaitaire Unique regime (turnover below DZD 15,000,000). *Message:* "IFU taxpayers do not file TVA. They pay the Impot Forfaitaire Unique instead. This skill covers regime reel TVA only. If you have exceeded the DZD 15,000,000 threshold, you must register for TVA and switch to regime reel."

**R-DZ-2 — Hydrocarbon sector.** *Trigger:* client operates in oil/gas exploration, production, or pipeline transport under the Hydrocarbons Law No. 19-13. *Message:* "Hydrocarbon-sector entities have a specific tax regime under the Hydrocarbons Law. Standard TVA rules do not apply. Please escalate to a specialist."

**R-DZ-3 — Military procurement.** *Trigger:* client supplies goods or services to the Algerian military under a defence contract. *Message:* "Military procurement contracts have specific TVA exemptions and conventions. Out of scope."

**R-DZ-4 — Partial exemption (prorata).** *Trigger:* client makes both taxable and exempt supplies and the exempt proportion is material. *Message:* "Your input TVA must be apportioned using the prorata formula under Code TCA Art. 34. The annual prorata calculation requires the full-year turnover mix. Please use a commissaire aux comptes to determine the prorata rate before input TVA is claimed."

**R-DZ-5 — ANDI investment incentive capital goods.** *Trigger:* client holds an ANDI investment certificate and claims TVA exemption on imported capital goods. *Message:* "ANDI investment incentives require verification of certificate validity and scope. Flag for reviewer."

**R-DZ-6 — Special conventions.** *Trigger:* client operates under a bilateral tax convention or special agreement with the Algerian government. *Message:* "Special conventions are outside this skill. Escalate to a qualified practitioner."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Algerian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BNA, BANQUE NATIONALE D'ALGERIE | EXCLUDE for bank charges/fees | Financial service, exempt |
| BEA, BANQUE EXTERIEURE D'ALGERIE | EXCLUDE for bank charges/fees | Same |
| CPA, CREDIT POPULAIRE D'ALGERIE | EXCLUDE for bank charges/fees | Same |
| BADR, BDL, CNEP | EXCLUDE for bank charges/fees | Same |
| SOCIETE GENERALE ALGERIE, SGA | EXCLUDE for bank charges/fees | Same |
| AGB, GULF BANK ALGERIE | EXCLUDE for bank charges/fees | Same |
| AL BARAKA, NATIXIS ALGERIE | EXCLUDE for bank charges/fees | Same |
| INTERETS, INTEREST, AGIOS | EXCLUDE | Interest income/expense, exempt |
| PRET, CREDIT, EMPRUNT | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Algerian government and regulators (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE | Tax payment, not a supply |
| TRESOR PUBLIC | EXCLUDE | Government payment |
| DOUANES, DIRECTION DES DOUANES | EXCLUDE for duty, but check for customs TVA (Line 13) |
| CNAS, CASNOS | EXCLUDE | Social security, out of scope |
| CNRC, REGISTRE DE COMMERCE | EXCLUDE | Registration fee, sovereign act |
| ANDI, ANADE | EXCLUDE | Government agency fee |

### 3.3 Algerian utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| SONELGAZ, SONALGAZ | Domestic 19% | 11 | Electricity and gas — operating expense |
| SEAAL, ADE | Domestic 9% | 11 | Water supply — reduced rate |
| ALGERIE TELECOM, AT, MOBILIS | Domestic 19% | 11 | Telecoms — overhead |
| DJEZZY, OOREDOO | Domestic 19% | 11 | Mobile telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SAA, CAAR, CAAT, CASH ASSURANCES | EXCLUDE | Insurance, exempt |
| ALLIANCE ASSURANCES, SALAMA | EXCLUDE | Same |
| ASSURANCE, TAAWIN | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| ALGERIE POSTE | EXCLUDE for standard postal | Universal postal service, exempt |
| DHL ALGERIE, FEDEX, UPS | Domestic 19% | 11 | Express courier, taxable |
| EMS ALGERIE | Domestic 19% | 11 | Express postal, taxable |

### 3.6 Fuel and transport

| Pattern | Treatment | Notes |
|---|---|---|
| NAFTAL | Domestic 19% for fuel (if business vehicle not blocked) | Check vehicle type |
| ETUSA, TRAMWAY | EXCLUDE or 0% | Public transport |
| AIR ALGERIE (domestic) | Domestic 9% | Tourism/transport reduced rate |
| AIR ALGERIE (international) | EXCLUDE / export | International flights |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| UNO, ARDIS, PROMY CASH, HYPERMARCHE | Default BLOCK input TVA | Personal provisioning unless hospitality |
| RESTAURANT, CAFE, TRAITEUR | Default BLOCK | Entertainment blocked under Code TCA Art. 30 |

### 3.8 SaaS — non-resident suppliers (reverse charge, Line 8/14)

| Pattern | Billing entity | Line | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 8/14 | Reverse charge — autoliquidation |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) or US | 8/14 | Reverse charge |
| ADOBE | Adobe Systems (IE or US) | 8/14 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 8/14 | Reverse charge |
| ZOOM | Zoom Video Communications (US) | 8/14 | Reverse charge |
| SLACK, ATLASSIAN, NOTION | Various non-resident | 8/14 | Reverse charge |
| ANTHROPIC, OPENAI, CHATGPT | US entity | 8/14 | Reverse charge |
| AWS, AMAZON WEB SERVICES | Various | 8/14 | Reverse charge |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees, financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.10 Professional services (Algeria)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| NOTAIRE, MAITRE, HUISSIER | Domestic 19% | 11 | Deductible if business purpose |
| EXPERT COMPTABLE, COMMISSAIRE | Domestic 19% | 11 | Always deductible |
| AVOCAT, CABINET D'AVOCATS | Domestic 19% | 11 | Deductible if business legal matter |

### 3.11 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| CNAS, CASNOS | EXCLUDE | Statutory social security |
| SALAIRE, PAIE, VIREMENT PERSONNEL | EXCLUDE | Wages, out of scope |
| IRG, IMPOT SUR LE REVENU | EXCLUDE | Income tax |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| VIREMENT INTERNE, TRANSFER PROPRE | EXCLUDE | Internal movement |
| DIVIDENDE | EXCLUDE | Dividend, out of scope |
| REMBOURSEMENT PRET | EXCLUDE | Loan repayment, out of scope |
| RETRAIT DAB, RETRAIT ESPECES | Ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Algeria-based self-employed IT consultant.

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:**
`05.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; DZD 2,160`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No TVA on the invoice. This is a service received from a non-resident. The Algerian client applies autoliquidation under Code TCA Art. 14. Both output TVA (Line 8) and input TVA (Line 14) must be reported. Net effect zero for fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line (input) | Line (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | NOTION LABS INC | -2,160 | -2,160 | 410 | 19% | 14 | 8 | N | — | — |

### Example 2 — Standard domestic sale at 19%

**Input line:**
`10.04.2026 ; SARL TECHNOSOFT ; CREDIT ; Invoice 2026-041 IT consulting April ; +500,000 ; DZD`

**Reasoning:**
Incoming payment from an Algerian company for IT consulting. Standard-rated at 19%. Report net in Line 1, output TVA in Line 6. The gross amount includes TVA: net = 500,000 / 1.19 = 420,168. TVA = 79,832.

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | SARL TECHNOSOFT | +500,000 | +420,168 | 79,832 | 19% | 1/6 | N | — | — |

### Example 3 — Entertainment, fully blocked

**Input line:**
`15.04.2026 ; RESTAURANT EL DJAZAIR ; DEBIT ; Business dinner ; -12,000 ; DZD`

**Reasoning:**
Restaurant transaction. Entertainment is blocked under Code TCA Art. 30. No input TVA recovery regardless of business purpose.

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT EL DJAZAIR | -12,000 | -12,000 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Capital goods purchase

**Input line:**
`18.04.2026 ; SPA DELL TECHNOLOGIES ; DEBIT ; Invoice Laptop XPS ; -250,000 ; DZD`

**Reasoning:**
Capital goods purchase. Input TVA goes to Line 12 (immobilisations), not Line 11 (operating). Net = 250,000 / 1.19 = 210,084. TVA = 39,916.

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | SPA DELL TECHNOLOGIES | -250,000 | -210,084 | -39,916 | 19% | 12 | N | — | — |

### Example 5 — Export sale (exempt with right to deduct)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice DZ-2026-015 IT consulting ; +3,500 ; EUR (DZD 518,000)`

**Reasoning:**
Export of services. Exempt with full right to deduct input TVA. Report in Line 4 (Exportations). No output TVA. Requires export documentation (service contract, proof of foreign consumption).

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +518,000 | +518,000 | 0 | 0% | 4 | N | — | — |

### Example 6 — Motor vehicle, blocked

**Input line:**
`28.04.2026 ; SARL SOVAC ; DEBIT ; Monthly lease payment Renault Clio ; -45,000 ; DZD`

**Reasoning:**
Car lease payment. Input TVA on passenger vehicles (< 9 seats) is blocked under Code TCA Art. 30. Exception only for taxi and hire vehicles. An IT consultant does not qualify. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | TVA | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | SARL SOVAC | -45,000 | -45,000 | 0 | — | — | Y | Q2 | "Motor vehicle: blocked" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 19% (Code TCA Art. 21)

Default rate for any taxable supply unless a reduced rate or exemption applies. Sales at Line 1 / Line 6. Purchases at Line 11.

### 5.2 Reduced rate 9% (Code TCA Art. 23)

Applies to: basic foodstuffs, pharmaceutical products, agricultural inputs, tourism/hotel services, IT equipment, renewable energy equipment. Sales at Line 2 / Line 7. Purchases at Line 11.

### 5.3 Exempt supplies (Code TCA Art. 8-9)

Bread, semolina, flour (basic staples), fresh milk, financial services (loan interest, life insurance), medical (public sector), education (authorized institutions), agricultural production at primary stage. No output TVA, no input TVA deduction on related costs.

### 5.4 Exports (Code TCA Art. 8)

Exempt with full right to deduct input TVA — effectively zero-rated. Requires customs export documentation. Report in Line 4.

### 5.5 Reverse charge — autoliquidation (Code TCA Art. 14)

When a TVA-registered person receives services from a non-resident: self-assess output TVA at applicable rate (19% or 9%) at Line 8, claim input TVA at Line 14. Net effect zero for fully taxable businesses.

### 5.6 Imports of goods

TVA paid at customs on imported goods. Report at Line 13. Deductible if goods are for taxable business activity.

### 5.7 Blocked input TVA (Code TCA Art. 29-33)

Zero recovery with no exceptions unless noted:
- Vehicles for personal transport (< 9 seats) unless taxi/hire (Art. 30)
- Accommodation and lodging (Art. 30)
- Entertainment and reception (Art. 30)
- Personal use goods and services (Art. 31)
- Petroleum products for blocked vehicles (Art. 30)
- Purchases without proper invoice with NIF (Art. 33)

### 5.8 Capital goods

Capital goods go to Line 12 (input TVA on immobilisations). Operating purchases go to Line 11. Classification based on useful life > 12 months and materiality.

### 5.9 Precompte TVA (Code TCA Art. 41 bis)

Certain designated entities (government, state enterprises, large taxpayers) withhold a precompte (typically 25% of TVA). Supplier claims credit on Line 18.

### 5.10 TAP distinction

TAP (Taxe sur l'Activite Professionnelle) at 1% (production) or 2% (services/commerce) is a separate turnover tax reported on the same G50 form. It is NOT TVA and is NOT recoverable as input tax. Never confuse TAP with TVA.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* Naftal, Shell, Total. *Why insufficient:* vehicle type unknown; if car, blocked regardless of use. *Default:* 0% recovery. *Question:* "Is this a passenger car (blocked) or a commercial vehicle used exclusively for business?"

### 6.2 Restaurants and entertainment

*Pattern:* any restaurant, cafe, traiteur. *Why insufficient:* entertainment is hard blocked. *Default:* block. *Question:* "Was this entertainment? (Note: blocked regardless.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom where the legal entity is not visible. *Default:* reverse charge Line 8/14. *Question:* "Could you check the invoice for the legal entity name and country?"

### 6.4 Round-number incoming transfers

*Pattern:* large round credit from owner-named counterparty. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own capital injection, or a loan?"

### 6.5 Incoming transfers from individual names

*Pattern:* incoming from private-looking counterparties. *Default:* domestic sale at 19%, Line 1/6. *Question:* "Was it a sale? Which rate?"

### 6.6 Large one-off purchases (potential capital goods)

*Pattern:* single large invoice. *Default:* if capital nature, Line 12; else Line 11. *Question:* "Is this a capital good (useful life > 12 months)?"

### 6.7 Mixed-use phone, internet, home office

*Pattern:* Algerie Telecom, Mobilis personal lines. *Default:* 0% if mixed without declared %. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.8 Cash withdrawals

*Pattern:* retrait DAB, retrait especes. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.9 ANDI investment incentive imports

*Pattern:* customs entry with ANDI certificate reference. *Default:* flag for reviewer. *Question:* "Do you hold a valid ANDI investment certificate? What is its scope?"

### 6.10 Precompte calculation

*Pattern:* payment from state enterprise with precompte deducted. *Default:* flag for reviewer to verify precompte rate. *Question:* "What precompte rate was applied? Do you have the withholding certificate?"

---

## Section 7 — Excel working paper template (Algeria-specific)

### Sheet "Transactions"

Columns: A (Date), B (Counterparty), C (Description), D (Gross DZD), E (Net DZD), F (TVA DZD), G (Rate), H (G50 Line), I (Default?), J (Question?), K (Excluded?), L (Notes).

### Sheet "G50 Summary"

One row per G50 line. Column A = line number, column B = description, column C = value computed via SUMIFS formula from Transactions sheet.

### Sheet "Return Form"

Final G50-ready figures:
```
Line 10 = Total TVA brute (output)
Line 16 = Total TVA deductible (input)
Line 17 = TVA due (10 - 16)
Line 20 = TVA a payer / Credit (17 - 18 - 19)
```

Positive Line 20 = payable to DGI. Negative = credit carried forward.

---

## Section 8 — Algeria bank statement reading guide

**CSV format conventions.** BNA and BEA exports typically use semicolon delimiters with DD/MM/YYYY dates. Common columns: Date, Libelle, Debit, Credit, Solde.

**French and Arabic language variants.** Descriptions may appear in French or transliterated Arabic. Treat as equivalent.

**Internal transfers and exclusions.** Own-account transfers between client's accounts. Always exclude.

**Refunds and reversals.** Identify by "remboursement", "annulation", "extourne". Book as negative in the same line as the original.

**Foreign currency transactions.** Convert to DZD at the Bank of Algeria official rate for the transaction date.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* SARL, EURL, SPA, SNC in the name = company. Individual name = sole trader. *Fallback:* "Are you a sole trader or company?"

### 9.2 TVA registration status
*Inference rule:* if asking for G50, they are regime reel. *Fallback:* "Are you registered for TVA under the regime reel?"

### 9.3 NIF
*Inference rule:* search statement descriptions. *Fallback:* "What is your NIF?"

### 9.4 Filing period
*Inference rule:* first and last transaction dates. *Fallback:* "Which month does this cover?"

### 9.5 Industry
*Inference rule:* counterparty mix. *Fallback:* "What does the business do?"

### 9.6 Exempt supplies
*Inference rule:* presence of medical/financial/educational income. *Fallback:* "Do you make any TVA-exempt sales?" If yes and material, R-DZ-4 fires.

### 9.7 Credit brought forward
*Inference rule:* not inferable. Always ask. *Question:* "Do you have any credit reporte from the previous month? (Line 19)"

### 9.8 Precompte credits
*Inference rule:* presence of state enterprise counterparties. *Fallback:* "Do you have precompte withholding certificates to claim? (Line 18)"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the 10-section Accora architecture. It supersedes v1.0. The Algeria-specific content (rate structure, G50 lines, blocked categories) requires validation by a licensed commissaire aux comptes in Algeria.

### Sources

1. Code des Taxes sur le Chiffre d'Affaires (Code des TCA), Ordonnance 76-104 as amended — Articles 2-3, 8-9, 14, 21, 23, 29-34, 36, 41 bis
2. Code des Procedures Fiscales
3. Loi de Finances annuelle
4. DGI Jibayatic portal — https://jibayatic.mf.gov.dz

### Known gaps

1. Supplier pattern library covers most common Algerian counterparties but not every regional SME.
2. Precompte rates vary by sector and designated entity — verify per DGI circular.
3. ANDI incentive scope varies by certificate — always verify.
4. The DZD 15,000,000 IFU threshold is as of current year — verify annually.

### Change log

- **v2.0 (April 2026):** Full rewrite to 10-section architecture. Supplier pattern library added. Worked examples added. Tier tags removed from inline text.
- **v1.0:** Initial skill with step-based structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
