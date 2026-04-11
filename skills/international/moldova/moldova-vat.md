---
name: moldova-vat
description: Use this skill whenever asked to prepare, review, or advise on a Moldova VAT return or any transaction classification for Moldovan VAT purposes. Trigger on phrases like "Moldova VAT", "Moldovan VAT", "TVA Moldova", "SFS filing", "Fiscal Code Moldova", or any request involving Moldovan VAT obligations. This skill contains the complete Moldova VAT classification rules, rate structure, return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. ALWAYS read this skill before touching any Moldovan VAT-related work.
---

# Moldova VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Moldova |
| Jurisdiction Code | MD |
| Tax Name | TVA (Taxa pe Valoarea Adaugata / VAT) |
| Primary Legislation | Fiscal Code of the Republic of Moldova, Title III (Articles 93-131) |
| Supporting Legislation | Government Decision on VAT invoicing; Law on Customs Tariff; DCFTA provisions (EU Association Agreement) |
| Tax Authority | State Tax Service (SFS -- Serviciul Fiscal de Stat) |
| Filing Portal | https://servicii.fisc.md (SIA "Contul curent al contribuabilului") |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Moldovan tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: DCFTA impact, partial deduction, free economic zones, Transnistria trade. Tier 3: transfer pricing, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and IDNO (Identification Number)** [T1] -- state registration number
2. **TVA registration number** [T1] -- issued upon VAT registration
3. **VAT registration status** [T1] -- standard VAT payer, small enterprise (exempt), or non-registered
4. **VAT period** [T1] -- monthly (standard for all VAT payers)
5. **Industry/sector** [T2] -- impacts exemptions and reduced rate eligibility
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional deduction rules apply
7. **Does the business operate in a Free Economic Zone?** [T2] -- Special VAT rules apply
8. **Does the business trade with Transnistria?** [T2] -- Impacts VAT treatment
9. **Accumulated VAT credit** [T1] -- from prior periods
10. **EU DCFTA benefits applicable?** [T2] -- May affect customs/VAT on EU imports

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output TVA) or Purchase (input TVA)
- Salaries, social contributions, dividends, loan repayments, fines = OUT OF SCOPE
- **Legislation:** Fiscal Code Article 93 (taxable objects), Article 95 (taxable supply)

### 1b. Determine Counterparty Location [T1]
- Moldova (domestic): supplier/customer registered in Republic of Moldova
- EU: all 27 EU member states (relevant for DCFTA provisions)
- CIS/EAEU: Russia, Belarus, Kazakhstan, Ukraine, etc.
- Other foreign: all remaining countries
- **Note:** Transnistria (Pridnestrovian Moldavian Republic) has its own tax system; trade with Transnistria requires special treatment [T2]

### 1c. Determine VAT Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 20% | Standard rate -- most goods and services | Article 96(a) |
| 8% | Reduced rate -- specific categories (see below) | Article 96(b) |
| 0% | Zero rate -- exports of goods, international transport, diplomatic supplies | Article 104 |
| Exempt | Financial services, medical, educational, insurance, residential rental, and others (Article 103) | Article 103 |

### 1d. Reduced Rate (8%) Categories [T1]

The 8% rate applies to:
- Bread and bakery products
- Milk and dairy products
- Medicines and pharmaceutical products
- Natural and liquefied gas (supplied to population)
- Sugar (beet sugar)
- Hotel/accommodation services
- Food services (restaurants, cafes, canteens)
- Agricultural production (certain categories)
- Solid fuel (coal, firewood) for households

**Legislation:** Article 96(b), Government decisions on reduced rate categories

### 1e. Exempt Supplies (Article 103) [T1]

The following are exempt from TVA:
- Financial and banking services (interest, currency exchange, securities)
- Insurance and reinsurance services
- Medical services (licensed)
- Educational services (state-accredited)
- Residential property (sale and rental of residential dwellings)
- Postal services (universal, by state operator)
- Cultural, artistic, and sporting events (admission under conditions)
- Gambling and lottery services (separately taxed)
- Burial services
- Legal aid services (state-funded)
- Agricultural land transactions

### 1f. Determine Expense Category [T1]
- Fixed assets: acquisition cost above threshold with useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: VAT Return Form Structure (Declaratia TVA) [T1]

**The TVA declaration (Form TVA) is filed monthly via the SFS electronic portal.**

**Legislation:** Fiscal Code Article 115; SFS Order on VAT declaration form

### Section A -- Taxable Supplies (Output TVA)

| Box | Description | Rate |
|-----|-------------|------|
| A1 | Total taxable supplies at 20% -- tax base | 20% |
| A1.1 | Output TVA at 20% | calculated |
| A2 | Total taxable supplies at 8% -- tax base | 8% |
| A2.1 | Output TVA at 8% | calculated |
| A3 | Exports and zero-rated supplies | 0% |
| A4 | Exempt supplies (Article 103) | - |
| A5 | Total supplies | sum |
| A6 | Total output TVA | sum |

### Section B -- Acquisitions (Input TVA)

| Box | Description |
|-----|-------------|
| B1 | Total domestic acquisitions (excl. fixed assets) |
| B1.1 | Input TVA on domestic acquisitions |
| B2 | Acquisitions of fixed assets |
| B2.1 | Input TVA on fixed assets |
| B3 | Imports (customs value + duties) |
| B3.1 | TVA paid on imports (customs) |
| B4 | Services from non-residents (reverse charge base) |
| B4.1 | TVA self-assessed on services from non-residents |
| B5 | Total acquisitions |
| B6 | Total input TVA |

### Section C -- Settlement

| Box | Description |
|-----|-------------|
| C1 | TVA payable (if A6 > B6) |
| C2 | TVA credit (if B6 > A6) |
| C3 | TVA credit carried forward from prior period |
| C4 | TVA credit requested for refund |
| C5 | Net TVA payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When a Moldovan entity purchases services from a non-resident with no Moldovan registration:
- Place of supply determined under Article 111
- If place of supply is Moldova, buyer self-assesses TVA at 20% (or 8%)
- Self-assessed TVA is both output (Box A) and input (Box B)
- Net effect: zero for fully taxable businesses

**Legislation:** Fiscal Code Article 109, Article 111

### 3b. Imports of Goods [T1]

Goods imported into Moldova:
- TVA collected by Customs Service at the border
- Rate: 20% or 8% depending on classification
- Tax base: customs value + import duties + excise (if applicable)
- Customs TVA is recoverable as input TVA
- Requires customs declaration as documentary evidence

### 3c. Exports [T1]

Exports of goods outside Moldova:
- Zero-rated under Article 104
- Exporter must have customs declaration confirming export
- Related input TVA is fully deductible

### 3d. Trade with Transnistria [T2]

Supplies of goods to Transnistria:
- Treated as domestic supply for TVA purposes (Moldova does not recognize Transnistria as a separate customs territory de jure)
- However, de facto, goods crossing into Transnistria may face additional inspections
- Goods from Transnistria entering Moldova-controlled territory may be subject to import-like treatment
- **Flag for reviewer: Transnistria trade is politically and fiscally complex. Case-by-case analysis required.**

---

## Step 4: Input TVA Deduction Rules

### 4a. General Conditions (Article 102) [T1]

Input TVA is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. A valid tax invoice (factura fiscala) is available
3. Goods/services are recorded in accounting
4. For imports: customs declaration and payment confirmation available

### 4b. Tax Invoice (Factura Fiscala) Requirements [T1]

A valid factura fiscala must contain:
- Sequential number and date
- Seller's name, address, IDNO, TVA registration number
- Buyer's name, address, IDNO, TVA registration number
- Description of goods/services
- Quantity and unit price
- TVA rate and amount
- Total amount including TVA

**Since 2021, Moldova has been transitioning to electronic invoicing (e-Factura) via the SFS system.**

### 4c. Blocked Input TVA (Non-Deductible) [T1]

Input TVA is NOT deductible for:

| Category | Legislation |
|----------|-------------|
| Goods/services used for exempt operations | Article 102(7) |
| Entertainment and hospitality expenses | Article 102(7) |
| Motor vehicles for personal use (passenger cars) | Article 102(7) |
| Goods/services not used for business purposes | Article 102(7) |
| Goods/services acquired without proper tax invoice | Article 102(1) |
| Goods lost, stolen, or destroyed (except force majeure) | Article 102(7) |

### 4d. Proportional Deduction [T2]

If a business makes both taxable and exempt supplies:
- Separate accounting required
- Direct attribution first (costs clearly linked to taxable or exempt)
- Mixed-use costs: proportional deduction

**Proportion formula:**
```
Deductible % = (Taxable supplies / Total supplies) * 100
```

**Flag for reviewer: confirm allocation methodology.**

---

## Step 5: Derived Calculations [T1]

```
Total Output TVA (A6) = A1.1 + A2.1

Total Input TVA (B6) = B1.1 + B2.1 + B3.1 + B4.1

IF A6 > B6 THEN
    C1 = A6 - B6 (TVA payable)
    C2 = 0
ELSE
    C1 = 0
    C2 = B6 - A6 (TVA credit)
END

C5 = C1 - C3 (net payable after credit brought forward)
IF C5 < 0 THEN C5 = 0; excess remains as credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | Annual turnover > MDL 1,500,000 (increased from MDL 1,200,000 effective 1 January 2026) | Article 112(1) |
| Voluntary registration | Below threshold, may register voluntarily | Article 112(2) |
| TVA refund eligibility | Credit accumulated for 3+ consecutive months | Article 101(5) |
| Export refund | Within 45 days of application (expedited) | Article 101(5) |
| Fixed asset threshold | Per accounting standards (no specific TVA threshold) | Accounting standards |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| TVA declaration | Monthly | 25th of the month following the reporting month | Article 115(1) |
| TVA payment | Monthly | 25th of the month following the reporting month | Article 115(1) |
| Import TVA | Per import | At customs clearance | Customs Code |
| TVA refund application | When applicable | Submitted with declaration | Article 101 |

---

## Step 8: DCFTA and EU Association Agreement Impact [T2]

Moldova has a Deep and Comprehensive Free Trade Area (DCFTA) agreement with the EU:
- Reduces or eliminates customs duties on many goods traded with the EU
- Does NOT eliminate import TVA -- TVA is still charged on EU imports at the border
- Moldova is progressively aligning its tax legislation with EU standards
- Some VAT rules may change as alignment progresses

**Flag for reviewer: monitor legislative changes related to EU approximation.**

---

## Step 9: Edge Case Registry

### EC1 -- Import from EU with DCFTA preferential tariff [T2]

**Situation:** Moldovan company imports goods from Germany with zero customs duty under DCFTA.
**Resolution:** Even with zero customs duty, import TVA at 20% (or 8%) is still charged on the customs value. TVA base = customs value + 0 duty + excise (if any). The DCFTA preference affects customs duty only, not TVA. Input TVA is deductible.
**Legislation:** DCFTA Agreement, Fiscal Code Article 97

### EC2 -- Services from non-resident IT company [T1]

**Situation:** Moldovan company purchases cloud hosting from a US provider. No TVA on invoice.
**Resolution:** Reverse charge applies. Place of supply is Moldova (buyer location for B2B services). Self-assess TVA at 20%. Report in Box B4 (tax base) and Box B4.1 (self-assessed TVA). Also report as output in Box A. Net effect zero for fully taxable businesses.
**Legislation:** Fiscal Code Article 109, Article 111

### EC3 -- Trade with Transnistria entity [T2]

**Situation:** Moldovan company sells goods to a company in Tiraspol (Transnistria).
**Resolution:** De jure, this is a domestic sale within Moldova's territory. TVA at standard rate should be applied. However, de facto enforcement and documentation requirements are complex. The Transnistrian buyer may operate under a separate tax system and may not accept Moldovan tax invoices. Flag for reviewer: case-by-case analysis required.
**Legislation:** Fiscal Code (general provisions), Law on Transnistria trade

### EC4 -- Hotel services at 8% [T1]

**Situation:** Moldovan hotel charges for accommodation.
**Resolution:** Hotel/accommodation services are subject to the 8% reduced rate. Output TVA at 8% reported in Box A2/A2.1. Related input TVA on hotel operating costs (utilities, supplies) at 20% is fully deductible.
**Legislation:** Fiscal Code Article 96(b)

### EC5 -- Exempt financial services with mixed operations [T2]

**Situation:** A company provides both management consulting (taxable at 20%) and financial advisory services (exempt under Article 103).
**Resolution:** Separate accounting required. Input TVA on costs directly attributable to consulting: fully deductible. Input TVA on costs for exempt financial services: not deductible. Mixed costs: proportional split based on turnover ratio. Flag for reviewer: confirm allocation.
**Legislation:** Article 102(7), Article 103

### EC6 -- Credit note / return of goods [T1]

**Situation:** Buyer returns defective goods; seller issues a credit note.
**Resolution:** Seller reduces output TVA in the period the credit note is issued. Buyer reduces input TVA in the period the credit note is received. Corrective factura fiscala must be issued. Both parties adjust the current period declaration.
**Legislation:** Fiscal Code Article 98, Article 102

### EC7 -- IT Park resident [T2]

**Situation:** A company registered as a Moldova IT Park resident provides software development services.
**Resolution:** Moldova IT Park residents benefit from a single tax (7% of sales revenue for IT companies) which replaces several taxes including TVA. Such entities are generally not TVA payers and do not charge TVA on their services. However, they cannot recover input TVA on purchases. Flag for reviewer: verify IT Park residency status and applicable regime.
**Legislation:** Law No. 77/2016 on IT Parks

### EC8 -- Construction services (reverse charge for certain operations) [T2]

**Situation:** A Moldovan construction company provides building services.
**Resolution:** Moldova has introduced reverse charge mechanisms for certain construction services to combat fraud. The buyer (if a VAT payer) may be required to self-assess TVA instead of the seller charging it. Flag for reviewer: check current status of construction reverse charge provisions -- this has been subject to legislative changes.
**Legislation:** Fiscal Code amendments on construction reverse charge

---

## PROHIBITIONS [T1]

- NEVER let AI guess TVA treatment -- classification is deterministic from facts and legislation
- NEVER apply input TVA deduction without a valid factura fiscala or e-Factura
- NEVER allow non-registered entities to claim input TVA deductions
- NEVER apply 0% rate on exports without confirmed customs documentation
- NEVER ignore reverse charge obligations on services from non-residents
- NEVER apply the 8% rate to categories not specifically listed in Article 96(b)
- NEVER treat Transnistria trade as a simple domestic or export transaction without specialist review [T2]
- NEVER assume DCFTA eliminates import TVA -- it affects customs duties only
- NEVER apply IT Park single-tax treatment without verifying registration status
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

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
Action Required: Qualified tax practitioner must confirm before filing.
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

### Test 1 -- Standard domestic sale at 20%

**Input:** Moldovan company sells consulting services to a Moldovan client. Net MDL 50,000. TVA at 20%.
**Expected output:** Box A1 = MDL 50,000. Box A1.1 = MDL 10,000. Factura fiscala issued.

### Test 2 -- Domestic purchase with input TVA

**Input:** Moldovan company purchases office supplies from Moldovan supplier. Gross MDL 12,000 including TVA MDL 2,000. Valid factura fiscala received.
**Expected output:** Box B1 includes MDL 10,000 (net). Box B1.1 = MDL 2,000. Fully deductible.

### Test 3 -- Import from EU

**Input:** Moldovan company imports machinery from Italy. Customs value MDL 200,000. Customs duty MDL 0 (DCFTA). No excise.
**Expected output:** Import TVA = MDL 200,000 * 20% = MDL 40,000. Paid at customs. Box B3 = MDL 200,000. Box B3.1 = MDL 40,000. Input TVA deductible.

### Test 4 -- Accommodation service at 8%

**Input:** Moldovan hotel provides accommodation. Net MDL 5,000. TVA at 8%.
**Expected output:** Box A2 = MDL 5,000. Box A2.1 = MDL 400.

### Test 5 -- Services from non-resident (reverse charge)

**Input:** Moldovan company engages a UK consulting firm. Fee GBP 3,000 (equivalent MDL 67,500). No Moldovan registration.
**Expected output:** Self-assessed TVA = MDL 67,500 * 20% = MDL 13,500. Box B4 = MDL 67,500. Box B4.1 = MDL 13,500. Also reported as output TVA. Net effect zero.

### Test 6 -- Export of goods

**Input:** Moldovan company exports wine to Romania. Invoice MDL 100,000. Customs declaration confirmed.
**Expected output:** Box A3 = MDL 100,000. TVA rate = 0%. Related input TVA fully deductible.

### Test 7 -- Blocked entertainment expense

**Input:** Moldovan company hosts a client dinner. Gross MDL 3,600 including TVA MDL 600.
**Expected output:** Input TVA of MDL 600 is NOT deductible. Entertainment is a blocked category. Expense at gross MDL 3,600.

### Test 8 -- IT Park resident sale

**Input:** IT Park resident sells software development services for MDL 200,000.
**Expected output:** No TVA charged. IT Park single tax applies (7% of revenue = MDL 14,000). No TVA declaration filed. No input TVA recovery. [T2] -- verify IT Park status.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of TVA declaration | MDL 1,000-5,000 per declaration | Fiscal Code Article 261 |
| Late payment of TVA | 0.1% per day of the outstanding amount | Fiscal Code Article 228 |
| Understatement of tax | 30% of the understated amount | Fiscal Code Article 261 |
| Failure to register for TVA | Back-assessment plus penalties | Fiscal Code Article 112 |
| Issuing false invoices | Criminal liability for amounts exceeding threshold | Criminal Code |
| Failure to maintain records | Administrative fine | Fiscal Code |

**Interest accrues daily at 0.1% of the outstanding TVA amount from the due date until payment.**

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Moldova uses the Moldovan Leu (MDL) as national currency
- All TVA returns filed in MDL
- Foreign currency converted at the official National Bank of Moldova (BNM) rate
- Import transactions: BNM rate on the date of the customs declaration
- Services from non-residents: BNM rate on the date of the tax point
- Exports: BNM rate on the date of supply

**Exchange rate differences are income tax matters, not TVA events.**

---

## Step 14: Record Keeping Requirements [T1]

TVA payers must maintain the following records for a minimum of 6 years:

| Record | Requirement |
|--------|-------------|
| Tax invoices (facturi fiscale / e-Factura) | All issued and received, sequentially filed |
| Purchase ledger | All input TVA claims with invoice references |
| Sales ledger | All output TVA with invoice references |
| Import documentation | Customs declarations, payment confirmations |
| Export documentation | Contracts, customs declarations, transport documents |
| TVA declarations (filed copies) | All submitted returns with SFS confirmations |
| Bank statements | Payment evidence |
| Contracts and agreements | For significant transactions |

**SFS may request records during desk audits (control cameral) or field audits (control fiscal).**

---

## Step 15: Place of Supply Rules for Services [T1]

| Service Type | Place of Supply | Legislation |
|-------------|----------------|-------------|
| B2B general services | Where recipient is established | Article 111(1) |
| B2C general services | Where supplier is established | Article 111(2) |
| Immovable property services | Where property is located | Article 111(3) |
| Passenger transport | Where transport takes place | Article 111(4) |
| Cultural/entertainment/sporting events | Where event takes place | Article 111(5) |
| Restaurant/catering | Where services physically performed | Article 111(6) |
| Telecommunications/electronic services (B2C) | Where recipient is established | Article 111(7) |

---

## Contribution Notes

This skill requires validation by a licensed Moldovan tax practitioner. Key areas requiring local expertise:

1. Transnistria trade treatment and practical enforcement
2. IT Park specific rules and eligibility
3. DCFTA impact on customs and TVA alignment
4. Current reduced rate (8%) category list
5. E-Factura implementation status and requirements

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
