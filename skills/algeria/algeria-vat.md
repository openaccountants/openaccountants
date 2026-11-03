---
name: algeria-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for an Algeria TVA (Taxe sur la Valeur Ajoutee) return (G50 declaration) for any client. Trigger on phrases like 'prepare TVA return', 'Algeria VAT', 'G50 declaration', 'declaration TVA', 'DGI return', or any request involving Algeria VAT filing. Also trigger when classifying transactions for TVA purposes from bank statements, invoices, or other source data. This skill covers Algeria only and standard TVA-registered businesses under the regime reel. IFU (forfaitaire) taxpayers, hydrocarbon-sector entities, military procurement, and special conventions are in the refusal catalogue. ALWAYS read this skill before touching any Algeria TVA work."
version: 2.1
jurisdiction: DZ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Algeria VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). Amounts in Algerian dinars (DA or DZD). Primary authority: Direction Generale des Impots (DGI).

## Who this applies to

Real-regime businesses filing TVA on the monthly G n° 50. IFU taxpayers do not charge TVA, because IFU replaces it (CIDTA art. 282 bis). Hydrocarbons, defence contracts, ANDI incentives, material prorata and special conventions go to a local professional.

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Standard rate | 19% | Code TCA art. 21 | 2026 | https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee |
| Reduced rate | 9% | Listed items only, Code TCA art. 23 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| New 9% wording: housing | 9% | Building new homes, their sale, servicing, and rehabilitating old homes | 2026 | same |
| New 9% wording: health | 9% | Medical acts, and meals and lodging given to patients by health establishments | 2026 | same |
| New 9% wording: education | 9% | State-approved education and training, including preschool, with their lodging and meals | 2026 | same |
| New 9% wording: transport | 9% | Rail passengers and passengers by bus | 2026 | same |
| Cash limit for input TVA | Invoices above 1,000,000 DA including tax, paid in cash or bank deposit lose deduction | Code TCA | 2026 | https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee |
| Omitted deduction | Claim by 20 December of the next year | Code TCA art. 30 | 2026 | same |
| IFU ceiling | 8,000,000 DA; the old 15,000,000 DA figure was wrong | CIDTA art. 282 ter | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf |
| TAP | Removed; no longer on G n° 50 calculations | DGI circular, 13 Feb 2024 | 2026 | https://web.archive.org/web/20250219180444/http://mfdgi.gov.dz/fr/a-propos/actu-fr/circulaire-relative-a-la-suppression-de-la-taxe-sur-l-lactivite-professionnelle-tap |


## The base

Output TVA arises on taxable sales; input TVA is deductible if the G n° 50 carries the supplier statement (Code TCA art. 29). Businesses with mixed sales file actual percentages by 20 March and adjust by the same date the next year (art. 40, LF 2026 art. 57). Businesses taking payment without invoices through software or a till must hold an editor's commitment or accredited certificate on data integrity (new art. 51 bis, LF 2026 art. 58).

Purchase exemption (franchise): apply to your tax office; authorisations are issued yearly by the DGE, wilaya director or CDI head (art. 45 per https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee).

### Carried from the earlier version, not checked against the law

Patterns, defaults and refusal rules kept so no work is lost. Any figure here is unverified unless it also appears in the tables above; the tables win.

**Key G50 TVA lines**

| Line | Meaning |
| -- | -- |
| unverified: 1 | CA taxable a 19% (standard-rated sales net) |
| unverified: 2 | CA taxable a 9% (reduced-rated sales net) |
| unverified: 3 | CA exonere (exempt supplies net) |
| unverified: 4 | Exportations (export sales net, exempt with deduction) |
| unverified: 5 | Total CA (derived: 1+2+3+4) |
| unverified: 6 | TVA collectee a 19% (output TVA on Line 1) |
| unverified: 7 | TVA collectee a 9% (output TVA on Line 2) |
| unverified: 8 | TVA sur autoliquidation (reverse charge output) |
| unverified: 9 | Regularisations (adjustments) |
| unverified: 10 | Total TVA brute (derived: 6+7+8+9) |
| unverified: 11 | TVA sur achats de biens et services (input TVA on operating purchases) |
| unverified: 12 | TVA sur immobilisations (input TVA on capital goods) |
| unverified: 13 | TVA sur importations (customs TVA) |
| unverified: 14 | TVA autoliquidation input (reverse charge input) |
| unverified: 15 | Exclusions (blocked items) |
| unverified: 16 | Total TVA deductible (derived: 11+12+13+14-15) |
| unverified: 17 | TVA due (derived: 10-16) |
| unverified: 18 | Precomptes (advance TVA withholdings received) |
| unverified: 19 | Credit reporte (prior period credit) |
| unverified: 20 | TVA a payer / Credit (derived: 17-18-19) |

**Conservative defaults**

| Ambiguity | Default |
| -- | -- |
| unverified: Unknown rate on a sale | 19% |
| Unknown TVA status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Algeria |
| unverified: Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |
| unverified: Unknown SaaS billing entity | Reverse charge from non-resident (Line 8/14) |

**Red flag thresholds**

| Threshold | Value |
| -- | -- |
| unverified: HIGH single-transaction size | DZD 5,000,000 |
| unverified: HIGH tax-delta on a single conservative default | DZD 500,000 |
| unverified: MEDIUM counterparty concentration | >40% of output OR input |
| unverified: MEDIUM conservative-default count | >4 across the return |
| unverified: LOW absolute net TVA position | DZD 10,000,000 |

#### Required inputs

- **Minimum viable input**: Bank statement for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Algerian or international business bank: BNA, BEA, CPA, BADR, BDL, Societe Generale Algerie, AGB, Natixis Algerie, Al Baraka, or any other.
- **Recommended input**: Sales invoices for the period, purchase invoices for any input TVA claim above DZD 500,000, the client's NIF (Numero d'Identification Fiscale) in writing.
- **Ideal input**: Complete invoice register, prior period G50, reconciliation of credit reporte (Line 19).
- **Refusal policy if minimum is missing**: SOFT WARN. If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This G50 was produced from bank statement alone. The reviewer must verify that input TVA claims above DZD 500,000 are supported by compliant invoices with valid NIF and that all reverse-charge classifications match the supplier's invoice."

#### Algeria-specific refusal catalogue

- **R-DZ-1: IFU (forfaitaire) taxpayer**: Trigger: client is under the Impot Forfaitaire Unique regime (turnover below DZD 8,000,000 (see the rates table)). Message: "IFU taxpayers do not file TVA. They pay the Impot Forfaitaire Unique instead. This skill covers regime reel TVA only. If you have exceeded the DZD 8,000,000 (see the rates table) threshold, you must register for TVA and switch to regime reel."
- **R-DZ-2: Hydrocarbon sector**: Trigger: client operates in oil/gas exploration, production, or pipeline transport under the Hydrocarbons Law No. 19-13. Message: "Hydrocarbon-sector entities have a specific tax regime under the Hydrocarbons Law. Standard TVA rules do not apply. Please escalate to a specialist."
- **R-DZ-3: Military procurement**: Trigger: client supplies goods or services to the Algerian military under a defence contract. Message: "Military procurement contracts have specific TVA exemptions and conventions. Out of scope."
- **R-DZ-4: Partial exemption (prorata)**: Trigger: client makes both taxable and exempt supplies and the exempt proportion is material. Message: "Your input TVA must be apportioned using the prorata formula under Code TCA Art. 34. The annual prorata calculation requires the full-year turnover mix. Please use a commissaire aux comptes to determine the prorata rate before input TVA is claimed."  _(Code TCA Art. 34)_
- **R-DZ-5: ANDI investment incentive capital goods**: Trigger: client holds an ANDI investment certificate and claims TVA exemption on imported capital goods. Message: "ANDI investment incentives require verification of certificate validity and scope. Flag for reviewer."
- **R-DZ-6: Special conventions**: Trigger: client operates under a bilateral tax convention or special agreement with the Algerian government. Message: "Special conventions are outside this skill. Escalate to a qualified practitioner."


This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

#### 3.1 Algerian banks (fees exempt: exclude)

**Algerian banks pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| BNA, BANQUE NATIONALE D'ALGERIE | EXCLUDE for bank charges/fees | Financial service, exempt |
| BEA, BANQUE EXTERIEURE D'ALGERIE | EXCLUDE for bank charges/fees | Same |
| CPA, CREDIT POPULAIRE D'ALGERIE | EXCLUDE for bank charges/fees | Same |
| BADR, BDL, CNEP | EXCLUDE for bank charges/fees | Same |
| SOCIETE GENERALE ALGERIE, SGA | EXCLUDE for bank charges/fees | Same |
| AGB, GULF BANK ALGERIE | EXCLUDE for bank charges/fees | Same |
| AL BARAKA, NATIXIS ALGERIE | EXCLUDE for bank charges/fees | Same |
| INTERETS, INTEREST, AGIOS | EXCLUDE | Interest income/expense, exempt |
| PRET, CREDIT, EMPRUNT | EXCLUDE | Loan principal movement, out of scope |

#### 3.2 Algerian government and regulators (exclude entirely)

**Algerian government and regulators pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| DGI, DIRECTION GENERALE DES IMPOTS | EXCLUDE | Tax payment, not a supply |
| TRESOR PUBLIC | EXCLUDE | Government payment |
| unverified: DOUANES, DIRECTION DES DOUANES | EXCLUDE for duty, but check for customs TVA (Line 13) |  |
| CNAS, CASNOS | EXCLUDE | Social security, out of scope |
| CNRC, REGISTRE DE COMMERCE | EXCLUDE | Registration fee, sovereign act |
| ANDI, ANADE | EXCLUDE | Government agency fee |

#### 3.3 Algerian utilities

**Algerian utilities pattern table**

| Pattern | Treatment | Line | Notes |
| -- | -- | -- | -- |
| unverified: SONELGAZ, SONALGAZ | Domestic 19% | 11 | Electricity and gas: operating expense |
| unverified: SEAAL, ADE | Domestic 9% | 11 | Water supply: reduced rate |
| unverified: ALGERIE TELECOM, AT, MOBILIS | Domestic 19% | 11 | Telecoms: overhead |
| unverified: DJEZZY, OOREDOO | Domestic 19% | 11 | Mobile telecoms |

#### 3.4 Insurance (exempt: exclude)

**Insurance pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| SAA, CAAR, CAAT, CASH ASSURANCES | EXCLUDE | Insurance, exempt |
| ALLIANCE ASSURANCES, SALAMA | EXCLUDE | Same |
| ASSURANCE, TAAWIN | EXCLUDE | All exempt |

#### 3.5 Post and logistics

**Post and logistics pattern table**

| Pattern | Treatment | Line | Notes |
| -- | -- | -- | -- |
| ALGERIE POSTE | EXCLUDE for standard postal | Universal postal service, exempt |  |
| unverified: DHL ALGERIE, FEDEX, UPS | Domestic 19% | 11 | Express courier, taxable |
| unverified: EMS ALGERIE | Domestic 19% | 11 | Express postal, taxable |

#### 3.6 Fuel and transport

**Fuel and transport pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: NAFTAL | Domestic 19% for fuel (if business vehicle not blocked) | Check vehicle type |
| unverified: ETUSA, TRAMWAY | EXCLUDE or 0% | Public transport |
| unverified: AIR ALGERIE (domestic) | Domestic 9% | Tourism/transport reduced rate |
| AIR ALGERIE (international) | EXCLUDE / export | International flights |

#### 3.7 Food retail (blocked unless hospitality business)

**Food retail pattern table**  _(Code TCA Art. 30)_

| Pattern | Treatment | Notes |
| -- | -- | -- |
| UNO, ARDIS, PROMY CASH, HYPERMARCHE | Default BLOCK input TVA | Personal provisioning unless hospitality |
| unverified: RESTAURANT, CAFE, TRAITEUR | Default BLOCK | Entertainment blocked under Code TCA Art. 30 |

#### 3.8 SaaS: non-resident suppliers (reverse charge, Line 8/14)

**SaaS non-resident suppliers pattern table**

| Pattern | Billing entity | Line | Notes |
| -- | -- | -- | -- |
| unverified: GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 8/14 | Reverse charge: autoliquidation |
| unverified: MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) or US | 8/14 | Reverse charge |
| unverified: ADOBE | Adobe Systems (IE or US) | 8/14 | Reverse charge |
| unverified: META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 8/14 | Reverse charge |
| unverified: ZOOM | Zoom Video Communications (US) | 8/14 | Reverse charge |
| unverified: SLACK, ATLASSIAN, NOTION | Various non-resident | 8/14 | Reverse charge |
| unverified: ANTHROPIC, OPENAI, CHATGPT | US entity | 8/14 | Reverse charge |
| unverified: AWS, AMAZON WEB SERVICES | Various | 8/14 | Reverse charge |

#### 3.9 Payment processors

**Payment processors pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees, financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

#### 3.10 Professional services (Algeria)

**Professional services pattern table**

| Pattern | Treatment | Line | Notes |
| -- | -- | -- | -- |
| unverified: NOTAIRE, MAITRE, HUISSIER | Domestic 19% | 11 | Deductible if business purpose |
| unverified: EXPERT COMPTABLE, COMMISSAIRE | Domestic 19% | 11 | Always deductible |
| unverified: AVOCAT, CABINET D'AVOCATS | Domestic 19% | 11 | Deductible if business legal matter |

#### 3.11 Payroll and social security (exclude entirely)

**Payroll and social security pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| CNAS, CASNOS | EXCLUDE | Statutory social security |
| SALAIRE, PAIE, VIREMENT PERSONNEL | EXCLUDE | Wages, out of scope |
| IRG, IMPOT SUR LE REVENU | EXCLUDE | Income tax |

#### 3.12 Internal transfers and exclusions

**Internal transfers and exclusions pattern table**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| VIREMENT INTERNE, TRANSFER PROPRE | EXCLUDE | Internal movement |
| DIVIDENDE | EXCLUDE | Dividend, out of scope |
| REMBOURSEMENT PRET | EXCLUDE | Loan repayment, out of scope |
| RETRAIT DAB, RETRAIT ESPECES | Ask | Default exclude; ask what cash was spent on |

#### 5.3 Exempt supplies (Code TCA Art. 8-9)

- **Exempt supplies**: Bread, semolina, flour (basic staples), fresh milk, financial services (loan interest, life insurance), medical (public sector), education (authorized institutions), agricultural production at primary stage. No output TVA, no input TVA deduction on related costs.  _(Code TCA Art. 8-9)_

#### 5.4 Exports (Code TCA Art. 8)

- **Exports**: Exempt with full right to deduct input TVA: effectively zero-rated. Requires customs export documentation. Report in Line 4.  _(Code TCA Art. 8)_

#### 5.5 Reverse charge: autoliquidation (Code TCA Art. 14)

- **Reverse charge / autoliquidation**: When a TVA-registered person receives services from a non-resident: self-assess output TVA at applicable rate (19% or 9%) at Line 8, claim input TVA at Line 14. Net effect zero for fully taxable businesses.  _(Code TCA Art. 14)_

#### 5.6 Imports of goods

- **Imports of goods**: TVA paid at customs on imported goods. Report at Line 13. Deductible if goods are for taxable business activity.

#### 5.7 Blocked input TVA (Code TCA Art. 29-33)

- **Blocked input TVA categories**: Zero recovery with no exceptions unless noted: - Vehicles for personal transport (< 9 seats) unless taxi/hire (Art. 30) - Accommodation and lodging (Art. 30) - Entertainment and reception (Art. 30) - Personal use goods and services (Art. 31) - Petroleum products for blocked vehicles (Art. 30) - Purchases without proper invoice with NIF (Art. 33)  _(Code TCA Art. 29-33)_

#### 5.8 Capital goods

- **Capital goods classification**: Capital goods go to Line 12 (input TVA on immobilisations). Operating purchases go to Line 11. Classification based on useful life > 12 months and materiality.

#### 5.9 Precompte TVA (Code TCA Art. 41 bis)

- **Precompte TVA**: Certain designated entities (government, state enterprises, large taxpayers) withhold a precompte (typically 25% of TVA). Supplier claims credit on Line 18.  _(Code TCA Art. 41 bis)_

#### 5.10 TAP distinction

- **TAP (Taxe sur l'Activite Professionnelle)**: TAP (removed, see the rates table) is a separate turnover tax reported on the same G50 form. It is NOT TVA and is NOT recoverable as input tax. Never confuse TAP with TVA.


#### 6.1 Fuel and vehicle costs

- **Fuel and vehicle costs**: Pattern: Naftal, Shell, Total. Why insufficient: vehicle type unknown; if car, blocked regardless of use. Default: 0% recovery. Question: "Is this a passenger car (blocked) or a commercial vehicle used exclusively for business?"

#### 6.2 Restaurants and entertainment

- **Restaurants and entertainment**: Pattern: any restaurant, cafe, traiteur. Why insufficient: entertainment is hard blocked. Default: block. Question: "Was this entertainment? (Note: blocked regardless.)"

#### 6.3 Ambiguous SaaS billing entities

- **Ambiguous SaaS billing entities**: Pattern: Google, Microsoft, Adobe, Meta, Slack, Zoom where the legal entity is not visible. Default: reverse charge Line 8/14. Question: "Could you check the invoice for the legal entity name and country?"

#### 6.4 Round-number incoming transfers

- **Round-number incoming transfers**: Pattern: large round credit from owner-named counterparty. Default: exclude as owner injection. Question: "Is this a customer payment, your own capital injection, or a loan?"

#### 6.5 Incoming transfers from individual names

- **Incoming transfers from individual names**: Pattern: incoming from private-looking counterparties. Default: domestic sale at 19%, Line 1/6. Question: "Was it a sale? Which rate?"

#### 6.6 Large one-off purchases (potential capital goods)

- **Large one-off purchases**: Pattern: single large invoice. Default: if capital nature, Line 12; else Line 11. Question: "Is this a capital good (useful life > 12 months)?"

#### 6.7 Mixed-use phone, internet, home office

- **Mixed-use phone, internet, home office**: Pattern: Algerie Telecom, Mobilis personal lines. Default: 0% if mixed without declared %. Question: "Is this a dedicated business line or mixed-use?"

#### 6.8 Cash withdrawals

- **Cash withdrawals**: Pattern: retrait DAB, retrait especes. Default: exclude as owner drawing. Question: "What was the cash used for?"

#### 6.9 ANDI investment incentive imports

- **ANDI investment incentive imports**: Pattern: customs entry with ANDI certificate reference. Default: flag for reviewer. Question: "Do you hold a valid ANDI investment certificate? What is its scope?"

#### 6.10 Precompte calculation

- **Precompte calculation**: Pattern: payment from state enterprise with precompte deducted. Default: flag for reviewer to verify precompte rate. Question: "What precompte rate was applied? Do you have the withholding certificate?"

**CSV format conventions.** BNA and BEA exports typically use semicolon delimiters with DD/MM/YYYY dates. Common columns: Date, Libelle, Debit, Credit, Solde.

**French and Arabic language variants.** Descriptions may appear in French or transliterated Arabic. Treat as equivalent.

**Internal transfers and exclusions.** Own-account transfers between client's accounts. Always exclude.

**Refunds and reversals.** Identify by "remboursement", "annulation", "extourne". Book as negative in the same line as the original.

**Foreign currency transactions.** Convert to DZD at the Bank of Algeria official rate for the transaction date.


#### 9.1 Entity type and trading name

- **Entity type and trading name**: Inference rule: SARL, EURL, SPA, SNC in the name = company. Individual name = sole trader. Fallback: "Are you a sole trader or company?"

#### 9.2 TVA registration status

- **TVA registration status**: Inference rule: if asking for G50, they are regime reel. Fallback: "Are you registered for TVA under the regime reel?"

#### 9.3 NIF

- **NIF**: Inference rule: search statement descriptions. Fallback: "What is your NIF?"

#### 9.4 Filing period

- **Filing period**: Inference rule: first and last transaction dates. Fallback: "Which month does this cover?"

#### 9.5 Industry

- **Industry**: Inference rule: counterparty mix. Fallback: "What does the business do?"

#### 9.6 Exempt supplies

- **Exempt supplies onboarding**: Inference rule: presence of medical/financial/educational income. Fallback: "Do you make any TVA-exempt sales?" If yes and material, R-DZ-4 fires.

#### 9.7 Credit brought forward

- **Credit brought forward**: Inference rule: not inferable. Always ask. Question: "Do you have any credit reporte from the previous month? (Line 19)"

#### 9.8 Precompte credits

- **Precompte credits**: Inference rule: presence of state enterprise counterparties. Fallback: "Do you have precompte withholding certificates to claim? (Line 18)"

## Deadlines and filing

How to file and pay the monthly G50 (real regime):
1. Log in to Jibaya'tic if your tax centre uses it, or take the paper Serie G n° 50 to the tax receiver for your head office or main establishment (https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee).
2. Enter the month's taxable sales and output TVA, input TVA, and salary IRG withheld. Box numbers are unverified, so copy them from the form itself.
3. Attach the supplier statement Code TCA art. 29 requires for input TVA (https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee).
4. File within the first 20 days of the month after the period. Payment need not be on the same day as filing, but must fall inside the same time limit.
5. Keep the stamped copy or online acknowledgement as proof. E-payment delayed up to 10 days through no fault of the taxpayer or bank carries no penalty.

| Obligation | Deadline | Official URL |
|---|---|---|
| G n° 50 monthly | First 20 days of next month; January 2026 extended to 10 March, February to 26 March | https://web.archive.org/web/20261008093610/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-delais-g50-taxeformation-taxe-apprentissage |
| Instalment regime (acomptes) | Monthly 1/12 of last year's sales; year-end statement by 20 April; needs 6 months' activity and a permanent site | https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee |
| Prorata statement | 20 March | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |


## Penalties and interest

| Failure | Result | Official URL |
|---|---|---|
| General TVA breach | 25,000 DA fine (art. 114) | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| Fraud | 100,000 DA | same |
| No identification plates (art. 60) | 10,000 DA | same |
| Art. 61 breach | 50,000 DA | same |
| Late payment | CIDTA art. 402 penalties; 10%, then 3% a month, cap 25% | https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee |


## Cross-border points

Exports and non-resident services: the old skill treats exports as exempt with deduction and imported services as reverse charged. The Code TCA text was not opened, so both are unverified; see the carried section. Hydrocarbon and treaty cases are out of scope.

## Two worked examples that recompute

**Example 1, simple.** Sale of 500,000 DA including 19% TVA: net 420,168.07, TVA 79,831.93.

```oa-check
name: Standard sale, gross 500,000 DA
inputs:
  gross: 500000
steps:
  - net: round(gross / 1.19, 2)
  - tva: gross - net
expected:
  net: 420168.07
  tva: 79831.93
```

**Example 2, edge and decision: should a clinic supplier pay a 1,190,000 DA invoice in cash?** TVA 190,000 DA is lost in cash because the total exceeds 1,000,000 DA; by bank transfer or cheque it stays deductible. Cost of paying cash: 190,000 DA.

```oa-check
name: Cash limit on a 1,190,000 DA invoice
inputs:
  gross: 1190000
steps:
  - tva: gross - gross / 1.19
  - lost_if_cash: tva
expected:
  lost_if_cash: 190000.00
```

## Ask the client first

1. Real regime or IFU?
2. Month covered?
3. Any exempt or 9% sales?
4. Any payment above 1,000,000 DA in cash?
5. Credit carried forward and precompte certificates?
6. Passenger cars, entertainment or foreign services bought?

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi de finances pour 2026, JO n° 88 of 31 Dec 2025 (read: fiscal articles 5 to 29, 53 to 60); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf | 2026-11-01 |
| Loi de finances pour 2025, JO n° 84 of 26 Dec 2024 (read: arts. 7, 8, 22, 23, 26 to 29); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf | 2026-11-01 |
| DGI, TVA page, archived copy of 19 Feb 2025; dated 21 Oct 2023; read for the rates and steps cited | https://web.archive.org/web/20250219182700/http://mfdgi.gov.dz/fr/professionnels/services-pro/regime-reel/la-taxe-sur-la-valeur-ajoutee | 2026-11-01 |
| DGI, circular notice on removing TAP, 13 Feb 2024, archived copy; read for the rates and steps cited | https://web.archive.org/web/20250219180444/http://mfdgi.gov.dz/fr/a-propos/actu-fr/circulaire-relative-a-la-suppression-de-la-taxe-sur-l-lactivite-professionnelle-tap | 2026-11-01 |
| DGI notice extending G50 and TFP/TA, archived copy of 8 Oct 2026; read for the rates and steps cited | https://web.archive.org/web/20261008093610/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-delais-g50-taxeformation-taxe-apprentissage | 2026-11-01 |

mfdgi.gov.dz and cnas.dz refused every direct and Chrome connection on 2026-11-01; DGI pages are Internet Archive copies, marked as such.

Not yet confirmed: the exact Code TCA text for exemptions, reverse charge (art. 14 in the old skill), blocked input TVA (arts. 29 to 33 in the old skill), precompte (art. 41 bis, 25% in the old skill), prorata (art. 34) and exports; G50 line numbers 1 to 20 in the old skill, because no G50 form could be opened; standard rate on reduced-rate list items 1 to 4 and 6 to 36, which LF 2026 leaves unchanged and which we did not read in full; TVA treatment of each supplier in the pattern library; Jibayatic screen names and portal address.

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
