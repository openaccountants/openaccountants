---
name: monaco-vat
description: Use this skill whenever asked to prepare, review, or advise on a Monaco VAT (TVA) return or any transaction classification for Monaco VAT purposes. Trigger on phrases like "Monaco VAT", "Monaco TVA", "Monaco tax", "TVA Monaco", or any request involving Monaco VAT obligations. Monaco is within the French VAT territory and applies French TVA rules at 20% standard rate. This skill is a reference wrapper that points to French TVA rules with Monaco-specific administrative details. ALWAYS read this skill before touching any Monaco VAT-related work.
---

# Monaco VAT (TVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Principality of Monaco |
| Jurisdiction Code | MC |
| Tax Name | TVA (Taxe sur la Valeur Ajoutee / VAT) |
| Primary Legislation | French Code General des Impots (CGI), Articles 256-298 (TVA provisions) -- applied in Monaco via the Franco-Monegasque Customs Convention |
| Supporting Legislation | Convention Douaniere Franco-Monegasque (1963, as amended); Convention Fiscale Franco-Monegasque (1963); EU VAT Directive 2006/112/EC (Monaco is within EU VAT territory as part of France) |
| Tax Authority | Direction des Services Fiscaux de Monaco (Monaco Tax Authority) -- for registration; Direction Generale des Finances Publiques (DGFiP, France) -- for TVA law |
| Filing Portal | Monaco: https://service-public-entreprises.gouv.mc; French TVA obligations via Nice tax office |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, basic classification, France-Monaco treatment. Tier 2: Monaco-specific administrative procedures, EEA/EU interactions. Tier 3: complex cross-border structures, Monaco-specific corporate provisions. |

---

## CRITICAL: Monaco Is Within French VAT Territory [T1]

**Monaco is treated as part of France for TVA (VAT) purposes.** This is a fundamental principle:

1. **French TVA law applies in full** in Monaco under the Franco-Monegasque Customs Convention of 1963.
2. **Monaco is part of the EU VAT territory** by virtue of being within the French VAT area (Article 6 of VAT Directive 2006/112/EC, read with Article 7(1)).
3. **Supplies between Monaco and France are DOMESTIC supplies** -- NOT imports/exports, NOT intra-community supplies.
4. **Supplies between Monaco and other EU member states follow the same rules as France-EU trade** -- i.e., standard intra-community supply/acquisition rules.
5. **Supplies between Monaco and non-EU countries follow the same rules as French exports/imports.**
6. **TVA rates, exemptions, and rules are IDENTICAL to France.**

**For all substantive TVA rules, rates, classifications, deductions, and calculations, French TVA law (CGI) applies. Refer to the France VAT skill for complete details.**

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know:

1. **Entity name and Monaco RCI number (Registre du Commerce et de l'Industrie)** [T1]
2. **French TVA number** [T1] -- FR + 2 check digits + 9 SIREN digits (issued by French tax authorities via Nice office)
3. **TVA registration status** [T1] -- standard regime, simplified regime, or franchise en base (small business exemption)
4. **TVA period** [T1] -- monthly (regime normal), quarterly (regime simplifie), or annual (for small businesses under simplified regime)
5. **Industry/sector** [T2] -- impacts reduced rates and exemptions
6. **Does the business make exempt supplies?** [T2] -- partial deduction rules apply
7. **Does the business trade with EU or non-EU countries?** [T1] -- intra-community and import/export rules
8. **Accumulated TVA credit** [T1] -- from prior periods

**If any of items 1-4 are unknown, STOP.**

---

## Step 1: TVA Rates (French Rates Apply) [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 20% | Standard rate -- most goods and services | CGI Article 278 |
| 10% | Intermediate reduced rate -- restaurant meals, prepared food, accommodation, passenger transport, renovation works (existing residential), certain agricultural products | CGI Article 279 |
| 5.5% | Reduced rate -- basic food products, books, energy supply (gas, electricity), cultural events, school canteens, medical equipment | CGI Article 278-0 bis |
| 2.1% | Super-reduced rate -- medicines reimbursable by social security, newspapers/press, live performances (first 140 shows), certain TV license fees | CGI Article 281 quater et seq. |
| 0% | Intra-community supplies (B2B), exports | CGI Article 262 |
| Exempt | Financial services, insurance, medical, educational, residential rental | CGI Article 261 |

---

## Step 2: Key Administrative Differences [T1]

While TVA law is French, there are administrative specifics for Monaco-based entities:

| Aspect | Monaco Specifics |
|--------|-----------------|
| Registration | Through the Direction des Services Fiscaux de Monaco, which coordinates with the French tax office in Nice (Direction Regionale des Finances Publiques des Alpes-Maritimes) |
| TVA number | Standard French format: FR + XX + SIREN (9 digits) |
| Filing | TVA returns (CA3 monthly or CA12 annual) filed with the Nice tax office |
| Payment | To the French Treasury (Tresor Public) via the Nice tax office |
| Audit | May be conducted by French tax inspectors or Monaco tax officials |
| Income tax | Monaco has NO personal income tax for individuals (but this does not affect TVA) |
| Corporate tax | Monaco applies French corporate tax (IS) for companies deriving >25% revenue from outside Monaco (specific convention rules) |
| Intra-community trade | Intrastat declarations (DEB/DES) filed the same way as French entities |

---

## Step 3: Supplies Between Monaco and France [T1]

Supplies between Monaco and metropolitan France are **domestic supplies**:
- Standard French TVA rates apply
- No import/export treatment
- No intra-community supply rules
- Invoice with French TVA
- No customs declaration
- Treated as if both parties were in France

---

## Step 4: Supplies Between Monaco and Other EU States [T1]

Monaco follows the same rules as France for intra-community trade:

### Intra-Community Supplies (Sales to EU B2B)
- Zero-rated (exempt with right of deduction)
- Requires valid customer VAT number (VIES verification)
- European Sales Listing (DES) must be filed
- Invoice without TVA, noting reverse charge

### Intra-Community Acquisitions (Purchases from EU B2B)
- Self-assess French TVA on the acquisition
- Report as both output and input TVA
- Net effect: zero for fully taxable businesses

### Distance Selling (B2C to EU)
- OSS (One-Stop Shop) rules apply as for French sellers
- If thresholds exceeded, TVA of destination country applies

---

## Step 5: Supplies Between Monaco and Non-EU Countries [T1]

Same as French export/import rules:

### Exports
- Zero-rated
- Customs export declaration required
- Input TVA fully deductible

### Imports
- TVA collected by French/Monaco Customs at the border
- Rate depends on goods classification
- Import TVA recoverable as input TVA

---

## Step 6: TVA Return Form [T1]

Monaco entities file the same French TVA return forms:

### CA3 (Monthly/Quarterly Return)

| Line | Description |
|------|-------------|
| 01-05 | Taxable operations by rate |
| 06 | Intra-community acquisitions |
| 07 | Imports |
| 08 | Total tax base |
| 08A-11 | Output TVA at each rate (20%, 10%, 5.5%, 2.1%) |
| 14-17 | TVA on intra-community acquisitions and imports |
| 18 | Regularizations |
| 19 | Total output TVA (TVA brute) |
| 20-23 | Deductible input TVA (on goods, services, fixed assets, other) |
| 24 | Total deductible TVA |
| 25 | Credit from prior period |
| 26 | Total deductions |
| 28 | TVA payable (if 19 > 26) |
| 29 | TVA credit (if 26 > 19) |

---

## Step 7: Input TVA Deduction Rules [T1]

Same as French rules:

### General Conditions
1. Goods/services for taxable operations
2. Valid invoice (facture) with all required mentions
3. TVA is due (exigible) -- for goods: at delivery; for services: at payment (option for debits available)
4. For imports: customs documentation

### Blocked Input TVA (Non-Deductible) [T1]

| Category | Legislation |
|----------|-------------|
| Exempt operations (financial, insurance, medical, etc.) | CGI Article 271 |
| Passenger vehicles (coefficient 0 unless for resale, taxi, rental, driving school) | CGI Article 206 Annex II |
| Petroleum products for vehicles (partial: 80% for diesel, 0% for petrol until recently -- check current rules) | CGI Article 298 |
| Accommodation, restaurant expenses for staff/directors (50% deductible for entertainment context) | CGI Article 206 Annex II |
| Gifts exceeding EUR 73 TTC per beneficiary per year | CGI Article 206 Annex II |
| Services related to exempt operations | CGI Article 271 |

### Proportional Deduction (Prorata) [T2]

For mixed taxable/exempt operations:

```
Coefficient de deduction = Coefficient d'assujettissement
                         * Coefficient de taxation
                         * Coefficient d'admission
```

**Three-coefficient system (French method):**
1. **Assujettissement:** Proportion of the good/service used for economic activity (vs. non-economic)
2. **Taxation:** Proportion of taxable (incl. zero-rated) turnover vs. total turnover
3. **Admission:** Legal restrictions (e.g., 0 for passenger vehicles, 0.8 for diesel)

**Flag for reviewer: prorata calculation in France/Monaco is complex. Confirm with practitioner.**

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| CA3 return (monthly, regime normal) | Monthly | 19th-24th of the following month (varies by location; Nice = 19th) | CGI Article 287 |
| CA3 return (quarterly, small regime normal) | Quarterly | 19th-24th of the month following quarter end | CGI Article 287 |
| CA12 return (regime simplifie) | Annual | 2nd business day after May 1 (for calendar year filers) | CGI Article 287 |
| Acomptes (regime simplifie) | Semi-annual | July and December | CGI Article 287 |
| DEB/DES (intra-community) | Monthly | 10th business day of following month | EU regulations |
| TVA payment | With return | Same as return deadline | CGI Article 287 |

---

## Step 9: Edge Case Registry

### EC1 -- Supply from Monaco to France [T1]

**Situation:** Monaco company sells goods to a French customer in Nice.
**Resolution:** Domestic supply. TVA at applicable French rate (20%, 10%, 5.5%, or 2.1%). No export/import treatment. No intra-community rules. Standard French invoice with TVA.

### EC2 -- Supply from Monaco to German company (intra-community) [T1]

**Situation:** Monaco company sells goods B2B to a German company with valid DE VAT number.
**Resolution:** Intra-community supply. Zero-rated. Customer's VAT number verified via VIES. DES filing required. Invoice notes "Autoliquidation / Reverse charge" -- buyer self-assesses German VAT.
**Legislation:** CGI Article 262 ter

### EC3 -- Purchase from Italian supplier (intra-community acquisition) [T1]

**Situation:** Monaco company buys goods from an Italian supplier. Italian supplier invoices without TVA.
**Resolution:** Intra-community acquisition. Self-assess French TVA at applicable rate (e.g., 20%). Report as both output and input TVA on CA3. Net effect zero for fully taxable business.
**Legislation:** CGI Article 256 bis

### EC4 -- Import from non-EU country (e.g., USA) [T1]

**Situation:** Monaco company imports goods from the US.
**Resolution:** Import treatment identical to French import. TVA collected by Customs. Rate depends on goods. Import TVA deductible. Customs declaration required.

### EC5 -- Restaurant meal at 10% [T1]

**Situation:** Monaco restaurant charges for dine-in meals.
**Resolution:** Restaurant meals at 10% (intermediate reduced rate). Alcoholic beverages at 20%. Must be separated if different rates apply. Take-away food of basic products may be at 5.5%.
**Legislation:** CGI Article 279

### EC6 -- Monaco entity with no personal income tax context [T1]

**Situation:** Questions arise about how Monaco's lack of personal income tax affects TVA.
**Resolution:** There is no interaction. TVA is a completely separate indirect tax applied under French law. Monaco's personal income tax exemption for individuals is irrelevant to TVA obligations. All TVA rules apply in full.

### EC7 -- Financial services (exempt) [T2]

**Situation:** Monaco-based financial services firm provides investment management.
**Resolution:** Financial services are generally exempt from TVA under CGI Article 261 C. However, certain financial services may be taxable by option. If exempt, input TVA on related costs is NOT deductible. If opting to tax, prorata coefficient applies. Flag for reviewer: determine exempt vs. option-to-tax status.
**Legislation:** CGI Article 261 C, Article 260 B

### EC8 -- Real property in Monaco [T2]

**Situation:** Company sells a commercial property in Monaco.
**Resolution:** Real property TVA treatment follows French rules. Sale of new commercial property (within 5 years of completion) is subject to TVA at 20%. Sale after 5 years is exempt (but option to tax may be exercised). Registration duties (droits d'enregistrement) may also apply. Flag for reviewer: verify property age and option-to-tax status.
**Legislation:** CGI Article 257, Article 261(5)

---

## PROHIBITIONS [T1]

- NEVER treat Monaco-France supplies as imports/exports or intra-community -- they are domestic
- NEVER apply different TVA rates than French rates
- NEVER apply separate Monaco VAT rules -- French CGI applies
- NEVER ignore intra-community obligations for Monaco-EU trade (other than France)
- NEVER assume Monaco's income tax exemption affects TVA treatment
- NEVER allow input TVA deduction on passenger vehicles (unless exception applies)
- NEVER allow input TVA on gifts exceeding EUR 73 per beneficiary per year
- NEVER confuse Monaco corporate tax rules with TVA rules
- NEVER compute any number -- handled by deterministic engine

---

## Step 10: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified practitioner must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified practitioner. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Domestic sale (Monaco to France) at 20%

**Input:** Monaco company sells consulting services to French client. Net EUR 10,000. TVA at 20%.
**Expected output:** Domestic supply. CA3 lines 01: EUR 10,000. Output TVA = EUR 2,000. Standard French invoice.

### Test 2 -- Intra-community supply to Germany

**Input:** Monaco company sells goods to German company (valid DE VAT number). EUR 50,000.
**Expected output:** Zero-rated intra-community supply. CA3 line 06. DES filed. Invoice with reverse charge mention.

### Test 3 -- Intra-community acquisition from Italy

**Input:** Monaco company buys goods from Italian supplier. EUR 20,000. Italian supplier invoices without TVA.
**Expected output:** Self-assess TVA at 20% = EUR 4,000. Report as output (line 14) and input (line 20). Net zero.

### Test 4 -- Import from USA

**Input:** Monaco company imports goods. Customs value EUR 15,000. Duty EUR 750.
**Expected output:** Import TVA = (EUR 15,000 + EUR 750) * 20% = EUR 3,150. Deductible.

### Test 5 -- Restaurant meal at 10%

**Input:** Monaco restaurant bills customer. Net EUR 500. TVA at 10%.
**Expected output:** Output TVA = EUR 50. CA3 line 09A (or equivalent 10% line).

### Test 6 -- Books at 5.5%

**Input:** Monaco bookshop sells books. Net EUR 3,000. TVA at 5.5%.
**Expected output:** Output TVA = EUR 165.

### Test 7 -- Blocked passenger vehicle

**Input:** Monaco company purchases a car. Gross EUR 30,000 including TVA EUR 5,000.
**Expected output:** Input TVA EUR 5,000 NOT deductible. Blocked (coefficient d'admission = 0).

### Test 8 -- Supply within Monaco

**Input:** Monaco company A sells services to Monaco company B. Net EUR 8,000. TVA at 20%.
**Expected output:** Domestic supply. Output TVA = EUR 1,600. Standard treatment.

---

## Contribution Notes

This skill requires validation by a licensed Monaco or French tax practitioner. The substantive TVA rules are French, but Monaco-specific administrative arrangements (Nice tax office, Monaco RCI, etc.) require local expertise.

**For complete TVA rules, always cross-reference French TVA law (Code General des Impots, Title II).**

Key areas requiring local expertise:
1. Monaco-specific registration procedures
2. Filing deadlines (Nice tax office specifics)
3. Corporate tax interaction (25% rule)
4. Real property transactions in Monaco
5. Financial services sector specifics

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
