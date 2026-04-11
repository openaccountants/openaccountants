---
name: belarus-vat
description: Use this skill whenever asked to prepare, review, or advise on a Belarus VAT return or any transaction classification for Belarusian VAT purposes. Trigger on phrases like "Belarus VAT", "Belarusian VAT", "MNS filing", "VAT in Belarus", or any request involving Belarusian VAT obligations. This skill contains the complete Belarus VAT classification rules, rate structure, return form mappings, deductibility rules, reverse charge treatment, EAEU-specific rules, and filing deadlines. ALWAYS read this skill before touching any Belarusian VAT-related work.
---

# Belarus VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Belarus |
| Jurisdiction Code | BY |
| Tax Name | VAT (Nalog na Dobavlennuyu Stoimost / NDS) |
| Primary Legislation | Tax Code of the Republic of Belarus, Special Part, Chapter 14 (Articles 112-136) |
| Supporting Legislation | Decree of the President No. 361; EAEU Treaty Protocol on Indirect Taxes; Resolution of the MNS on VAT return forms |
| Tax Authority | Ministry of Taxes and Duties (MNS -- Ministerstvo po Nalogam i Sboram) |
| Filing Portal | https://portal.nalog.gov.by (Electronic declaration system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: EAEU trade, partial deduction, free economic zones. Tier 3: transfer pricing, complex restructuring, criminal tax liability. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and UNP (Taxpayer Identification Number)** [T1] -- 9 digits
2. **VAT registration status** [T1] -- standard VAT payer, simplified regime (without VAT), or individual entrepreneur
3. **VAT period** [T1] -- monthly or quarterly (depends on revenue threshold)
4. **Filing frequency** [T1] -- monthly if prior-year revenue exceeded BYN 2,115,000; quarterly otherwise
5. **Industry/sector** [T2] -- impacts specific exemptions
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional deduction rules apply
7. **Does the business trade within the EAEU?** [T2] -- Impacts import/export treatment
8. **Free Economic Zone (FEZ) resident?** [T2] -- Special VAT benefits may apply
9. **Accumulated VAT credits** [T1] -- from prior periods

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social fund contributions, dividends, loan repayments, fines = OUT OF SCOPE
- **Legislation:** Tax Code Article 112 (taxable objects)

### 1b. Determine Counterparty Location [T1]
- Belarus (domestic): supplier/customer registered in Belarus
- EAEU: Russia (RU), Kazakhstan (KZ), Armenia (AM), Kyrgyzstan (KG)
- Non-EAEU foreign: all other countries
- **Note:** EAEU members follow the Protocol on Indirect Taxes under the EAEU Treaty

### 1c. Determine VAT Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 20% | Standard rate -- most goods and services | Article 122(1) |
| 10% | Reduced rate -- food products, children's goods, medicines and medical devices per Presidential list; agricultural produce by qualifying domestic producers | Article 122(1.2) |
| 0% | Zero rate -- exports of goods, international transport services, certain re-exported goods | Article 122(1.1) |
| Exempt | Medical services, educational services, financial services, residential rental, cultural services, and others listed in Article 118 | Article 118 |

### 1d. Specific 10% Rate Categories [T1]

The 10% rate applies to:
- Food products included in the list established by Presidential decree
- Children's goods included in the list established by Presidential decree
- Medicines and medical devices (sales and imports)
- Agricultural products produced and sold by domestic agricultural producers: crops (excluding flowers and ornamental plants), store cattle, fish, and hive products produced in Belarus

**Note:** Belarus has a broad 10% rate covering food, children's goods, and medicines (similar to Russia's approach), in addition to domestically produced agricultural products.

### 1e. Exempt Supplies (Article 118) [T1]

The following are exempt from VAT (no output tax, no input tax recovery):
- Medical and veterinary services (licensed)
- Educational services (state-accredited institutions)
- Banking and financial services (with exceptions)
- Insurance and reinsurance services
- Securities transactions
- Residential property (first-time transfer)
- Burial and memorial services
- Religious goods produced by religious organizations
- Postal services (universal, by state operator)
- Public transportation (urban)
- Cultural and sporting events (admission, subject to conditions)

### 1f. Determine Expense Category [T1]
- Fixed assets: acquisition cost recorded as capital asset with useful life > 12 months
- Goods for resale: purchased to resell without transformation
- Raw materials: consumed in production
- Services/overheads: rent, utilities, consulting, etc.

---

## Step 2: VAT Return Form Structure [T1]

**The VAT return is filed electronically via the MNS portal. The declaration form is prescribed by MNS resolution.**

**Legislation:** Tax Code Article 136; MNS Resolution on VAT declaration forms

### Part I -- Tax Base and Output VAT

| Line | Description | Rate |
|------|-------------|------|
| 1 | Taxable turnover at 20% | 20% |
| 1a | Output VAT at 20% | calculated |
| 2 | Taxable turnover at 10% | 10% |
| 2a | Output VAT at 10% | calculated |
| 3 | Turnover at 0% (confirmed exports) | 0% |
| 4 | Exempt turnover | - |
| 5 | Turnover not recognized as object of taxation | - |
| 6 | Tax base for import VAT (EAEU) | varies |
| 7 | VAT on EAEU imports | calculated |
| 8 | Total output VAT | sum |

### Part II -- Input VAT Deductions

| Line | Description |
|------|-------------|
| 9 | Input VAT on domestic purchases |
| 10 | VAT paid on imports (customs) |
| 11 | VAT paid on EAEU imports |
| 12 | Input VAT on fixed assets |
| 13 | Total input VAT deductions |

### Part III -- VAT Payable / Refundable

| Line | Description |
|------|-------------|
| 14 | VAT payable (if line 8 > line 13) |
| 15 | VAT refundable / carried forward (if line 13 > line 8) |

### Appendix (Pradashennie)

Detailed breakdown of:
- Export operations by country and contract
- EAEU import details
- Adjustments and corrections

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Domestic Reverse Charge [T1]

Belarus does not have a broad domestic reverse charge like some EU countries. However:
- Services from foreign entities with no Belarusian establishment: the Belarusian buyer must self-assess and pay VAT at 20%
- Applies to services where the place of supply is Belarus under Article 117

### 3b. EAEU Imports (Russia, Kazakhstan, Armenia, Kyrgyzstan) [T2]

Goods imported from EAEU member states:
- No customs border, no customs VAT
- Buyer self-assesses VAT on the imported goods
- Files a separate EAEU import VAT declaration by the 20th of the month following the month goods were accepted
- Pays VAT by the same deadline
- Claims input VAT deduction after payment and filing
- Must submit an Application for Import of Goods and Payment of Indirect Taxes (with supporting documents)

**Legislation:** EAEU Treaty Protocol on Indirect Taxes

### 3c. Non-EAEU Imports [T1]

Goods imported from non-EAEU countries:
- VAT collected by Belarusian Customs at the border
- Rate: 20% (or 10% for eligible agricultural goods)
- Customs VAT is recoverable as input VAT
- Requires customs declaration as documentary evidence

### 3d. Exports [T1]

Exports of goods are zero-rated under Article 122(1.1):
- Exporter must confirm 0% rate with documentary evidence within 180 days
- Required documents: contract, transport documents, customs declarations
- If 180-day deadline is missed: output VAT at 20% (or 10%) is charged on the export

**EAEU exports:** 0% rate confirmed with Application for Import from the EAEU buyer's country tax authority

---

## Step 4: Input VAT Deduction Rules

### 4a. General Conditions for Deduction (Article 131-133) [T1]

Input VAT is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. Goods/services are recorded in accounting
3. A valid primary accounting document (invoice/ESСHF) is available
4. For imports: customs/EAEU declaration and payment confirmation available

### 4b. Electronic Invoicing (ESCHF) [T1]

Belarus uses a mandatory electronic VAT invoice system called ESCHF (Elektronny Schyot-Faktura):
- All VAT payers must issue ESCHF through the MNS portal
- ESCHF must be created within specified deadlines after the supply
- Input VAT deduction requires a valid ESCHF signed by the buyer
- Both seller and buyer must sign the ESCHF electronically

**Without a properly executed ESCHF, input VAT deduction is denied.**

### 4c. Blocked Input VAT (Non-Deductible) [T1]

Input VAT is NOT deductible for:

| Category | Legislation |
|----------|-------------|
| Goods/services used for exempt operations | Article 133 |
| Goods/services used for non-business purposes | Article 133 |
| Entertainment and hospitality expenses (meals, events for clients) | Article 133 |
| Motor vehicles for personal use | Article 133 |
| Goods/services acquired with budget funds | Article 133 |

### 4d. Proportional Deduction [T2]

If a business makes both taxable and exempt supplies:
- Separate accounting of input VAT is required
- Input VAT on costs directly attributable to taxable operations: fully deductible
- Input VAT on costs directly attributable to exempt operations: not deductible
- Input VAT on mixed-use costs: proportional deduction based on revenue split

**Proportion formula:**
```
Deductible % = (Taxable turnover / Total turnover) * 100
```

**Flag for reviewer: proportional split must be confirmed by practitioner.**

---

## Step 5: Derived Calculations [T1]

```
Total Output VAT (Part I, line 8) =
    VAT at 20% (line 1a)
  + VAT at 10% (line 2a)
  + VAT on EAEU imports (line 7)

Total Input VAT (Part II, line 13) =
    Input VAT on domestic purchases (line 9)
  + VAT paid on customs imports (line 10)
  + VAT paid on EAEU imports (line 11)
  + Input VAT on fixed assets (line 12)

IF line 8 > line 13 THEN
    Line 14 = line 8 - line 13  (VAT payable)
    Line 15 = 0
ELSE
    Line 14 = 0
    Line 15 = line 13 - line 8  (VAT refundable/carried forward)
END
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Monthly filing threshold | Prior-year revenue > BYN 2,115,000 | Article 136 |
| Quarterly filing | Prior-year revenue <= BYN 2,115,000 | Article 136 |
| Simplified regime (no VAT) | Gross revenue <= BYN 500,000 per year | Decree 36 / Tax Code Chapter 32 |
| Export 0% confirmation deadline | 180 calendar days | Article 122 |
| Fixed asset classification | Useful life > 12 months | Accounting standards |
| ESCHF creation deadline | Seller: by 10th of month following supply | MNS Resolution |
| ESCHF buyer signature deadline | Buyer: within 30 days of receipt | MNS Resolution |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| VAT return (monthly filers) | Monthly | 20th of the month following the reporting month | Article 136 |
| VAT payment (monthly filers) | Monthly | 22nd of the month following the reporting month | Article 136 |
| VAT return (quarterly filers) | Quarterly | 20th of the month following the quarter end | Article 136 |
| VAT payment (quarterly filers) | Quarterly | 22nd of the month following the quarter end | Article 136 |
| EAEU import declaration | Monthly | 20th of the month following the month of acceptance | EAEU Protocol |
| EAEU import VAT payment | Monthly | 20th of the month following the month of acceptance | EAEU Protocol |
| ESCHF issuance by seller | Per supply | 10th of the month following the supply | MNS Resolution |
| Export 0% documentary package | Per shipment | 180 days from customs/transport date | Article 122 |

---

## Step 8: Free Economic Zones (FEZ) [T2]

Belarus has several Free Economic Zones offering preferential tax treatment:
- FEZ "Brest", FEZ "Vitebsk", FEZ "Gomel-Raton", FEZ "Grodnoinvest", FEZ "Minsk", FEZ "Mogilev"
- FEZ residents may benefit from VAT exemptions on certain operations
- Sales of goods produced within the FEZ and sold to other FEZ residents or exported may be exempt or zero-rated
- Domestic sales by FEZ residents to non-FEZ entities are generally subject to standard VAT

**Flag for reviewer: FEZ-specific VAT treatment requires case-by-case analysis based on the specific FEZ regulations and the Presidential Decree governing the zone.**

---

## Step 9: Edge Case Registry

### EC1 -- EAEU import from Russia [T2]

**Situation:** Belarusian company imports machinery from Russia. Value RUB 5,000,000 (converted to BYN at exchange rate).
**Resolution:** Self-assess VAT at 20% on the BYN-equivalent value. File EAEU import application by the 20th of the following month. Pay VAT by the same deadline. Claim input deduction after payment and filing. Exchange rate: official National Bank of Belarus rate on the date goods are accepted in accounting. Flag for reviewer: confirm goods classification, exchange rate, and that Application for Import is properly completed.
**Legislation:** EAEU Treaty Protocol, Tax Code Article 131

### EC2 -- Services from foreign provider with no Belarusian establishment [T1]

**Situation:** Belarusian company engages a German consulting firm for management consulting. No Belarusian office/registration.
**Resolution:** Belarusian buyer self-assesses VAT at 20% on the payment amount. Place of supply is Belarus (buyer location for B2B services). VAT is paid to the budget. Input VAT is deductible if the services are used for taxable operations.
**Legislation:** Article 117 (place of supply), Article 114

### EC3 -- ESCHF not signed by buyer within 30 days [T1]

**Situation:** Seller issues ESCHF, but buyer fails to sign within 30 days.
**Resolution:** Input VAT deduction is denied until the ESCHF is properly signed. The buyer must contact the seller and resolve the ESCHF status. If the seller cancels the ESCHF, a new one must be issued. No deduction without a valid, buyer-signed ESCHF.
**Legislation:** MNS Resolution on ESCHF procedures

### EC4 -- Export to Russia with incorrect Application for Import [T2]

**Situation:** Belarusian exporter to Russia applies 0% rate but the Russian buyer's Application for Import contains errors or is not confirmed by the Russian FNS.
**Resolution:** Without a properly confirmed Application for Import from the Russian tax authority, the 0% rate cannot be verified. If not confirmed within 180 days, the Belarusian exporter must charge 20% VAT on the export. Flag for reviewer: follow up with Russian buyer for corrected documentation.
**Legislation:** EAEU Treaty Protocol

### EC5 -- Sale of software / IT services by HTP resident [T2]

**Situation:** A Belarus High Technology Park (HTP) resident sells software development services.
**Resolution:** HTP residents under Decree No. 8 (on Digital Economy Development) enjoy significant tax benefits, including potential VAT exemptions on certain IT services. However, the specifics depend on the type of service, the client location, and current HTP regulations. Flag for reviewer: HTP VAT treatment requires specialist analysis.
**Legislation:** Decree of the President No. 8 (2017), HTP Regulations

### EC6 -- Mixed taxable and exempt operations [T2]

**Situation:** A company provides both taxable consulting and exempt educational services.
**Resolution:** Separate accounting mandatory. Proportional deduction of mixed-use input VAT based on revenue split. Flag for reviewer: confirm the allocation methodology and verify that direct attribution has been applied first.
**Legislation:** Article 133, Article 131

### EC7 -- Credit note / adjustment of previously reported VAT [T1]

**Situation:** Seller issues a corrective ESCHF reducing the previously invoiced amount.
**Resolution:** The buyer must reduce their input VAT deduction in the period the corrective ESCHF is received (not the original period). The seller reduces output VAT in the period the corrective ESCHF is issued. Both parties adjust their declarations for the current period.
**Legislation:** Tax Code Article 129, MNS Resolution on ESCHF

### EC8 -- Simplified regime entity exceeding threshold [T1]

**Situation:** An individual entrepreneur on the simplified regime (no VAT) exceeds the BYN 500,000 revenue threshold mid-year.
**Resolution:** The entity must transition to standard VAT registration from the month following the month in which the threshold was exceeded. VAT must be charged on all supplies from that point forward. Input VAT on prior purchases (stock on hand) may be partially recoverable. Flag for reviewer: transitional rules are complex.
**Legislation:** Tax Code Chapter 32, Article 326

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT treatment -- classification is deterministic from facts and legislation
- NEVER apply input VAT deduction without a valid, buyer-signed ESCHF
- NEVER allow simplified regime entities to claim input VAT deductions
- NEVER apply 0% rate on exports without confirmed documentary evidence within 180 days
- NEVER ignore self-assessment obligations on services from foreign providers
- NEVER confuse EAEU imports (self-assessed, no customs) with non-EAEU imports (customs-collected)
- NEVER apply the 10% rate to goods not on the Presidential list -- verify the item is on the approved food, children's goods, or medicines list
- NEVER omit the EAEU Application for Import when claiming 0% on EAEU exports
- NEVER accept an unsigned ESCHF as basis for input VAT deduction
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 10: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

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

**Input:** Belarusian company sells consulting services to Belarusian client. Net BYN 10,000. VAT at 20%.
**Expected output:** Part I line 1: tax base = BYN 10,000. Output VAT line 1a = BYN 2,000. ESCHF issued.

### Test 2 -- Domestic purchase with input VAT deduction

**Input:** Belarusian company purchases office equipment from Belarusian supplier. Gross BYN 2,400 including VAT BYN 400. Valid ESCHF signed by buyer.
**Expected output:** Part II line 9: input VAT = BYN 400. Fully deductible.

### Test 3 -- EAEU import from Russia

**Input:** Belarusian company imports raw materials from Russia. Value BYN 50,000 (converted at NBB rate). Goods accepted on March 10.
**Expected output:** Self-assessed VAT = BYN 50,000 * 20% = BYN 10,000. EAEU import declaration filed by April 20. VAT paid by April 20. Input VAT of BYN 10,000 claimed after payment and filing.

### Test 4 -- Export to Kazakhstan at 0%

**Input:** Belarusian company exports furniture to Kazakhstan. Invoice value BYN 30,000. Application for Import confirmed by Kazakhstan tax authority within 180 days.
**Expected output:** Part I line 3: turnover at 0% = BYN 30,000. No output VAT. Related input VAT deductible.

### Test 5 -- Services from EU provider (reverse charge)

**Input:** Belarusian company engages a Polish law firm for legal advice. Fee EUR 5,000 (equivalent BYN 17,500). No Belarusian registration by the Polish firm.
**Expected output:** Self-assessed VAT = BYN 17,500 * 20% = BYN 3,500. VAT paid to budget. Input VAT of BYN 3,500 deductible if used for taxable operations. Net effect zero for fully taxable business.

### Test 6 -- Blocked entertainment expense

**Input:** Belarusian company hosts a client dinner. Gross BYN 600 including VAT BYN 100.
**Expected output:** Input VAT of BYN 100 is NOT deductible. Entertainment is a blocked category. Expense recorded at gross amount BYN 600.

### Test 7 -- Agricultural producer sale at 10%

**Input:** Agricultural enterprise (>50% revenue from agriculture) sells grain to a Belarusian food processor. Net BYN 80,000. VAT at 10%.
**Expected output:** Part I line 2: tax base = BYN 80,000. Output VAT line 2a = BYN 8,000.

### Test 8 -- Simplified regime entity issues invoice with VAT

**Input:** Simplified regime individual entrepreneur (below BYN 500,000 threshold) issues an invoice showing VAT of BYN 500.
**Expected output:** Simplified regime entities should NOT charge VAT. If VAT is shown on the invoice, the entity may be required to remit it to the budget. No input VAT deduction is available. Flag for reviewer: verify registration status and correct invoicing practice.

---

## Step 12: Penalties and Interest [T1]

Non-compliance with Belarusian VAT obligations results in the following penalties:

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of VAT return | Up to 1% of tax due per month of delay (max 10%) | Tax Code Article 14.2 |
| Late payment of VAT | Interest at refinancing rate of the National Bank + penalty | Tax Code Article 52 |
| Understatement of tax liability | 20% of the understated amount | Tax Code Article 14.4 |
| Intentional understatement | 40% of the understated amount | Tax Code Article 14.4 |
| Failure to issue ESCHF | Administrative fine per violation | MNS administrative procedures |
| Failure to register for VAT when required | Back-assessment of VAT plus penalties | Tax Code Article 14.2 |
| Incorrect ESCHF information | ESCHF may be invalidated; input VAT deduction denied | MNS Resolution |

**Interest on late payments** is calculated at the refinancing rate of the National Bank of the Republic of Belarus, accruing daily from the due date until the date of payment.

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Belarus uses the Belarusian Ruble (BYN) as its national currency
- All VAT returns must be filed in BYN
- Foreign currency transactions must be converted to BYN at the official National Bank of Belarus (NBB) exchange rate
- For domestic transactions: BYN amounts as invoiced
- For imports: NBB rate on the date of customs declaration or EAEU goods acceptance
- For services from non-residents: NBB rate on the date of payment or accrual (whichever triggers the tax point)
- For exports: NBB rate on the date of the supply (shipping date)

**Exchange rate gains/losses from timing differences are NOT VAT events -- they are income tax/accounting items only.**

---

## Step 14: Record Keeping Requirements [T1]

VAT payers must maintain the following records for a minimum of 10 years:

| Record | Requirement |
|--------|-------------|
| ESCHF (electronic invoices) | Stored electronically via MNS system; accessible for audit |
| Purchase ledger | Detailed record of all input VAT claims with ESCHF references |
| Sales ledger | Detailed record of all output VAT with ESCHF references |
| Import documentation | Customs declarations, EAEU applications, payment confirmations |
| Export documentation | Contracts, transport documents, Applications for Import (EAEU) |
| VAT returns (filed copies) | All submitted declarations with confirmation receipts |
| Bank statements | Supporting payment evidence for imports and tax payments |
| Contracts | Underlying agreements for all significant transactions |

**The MNS may request any of these records during a tax audit (kameral'naya or vyezdnaya proverka).**

---

## Contribution Notes

This skill requires validation by a licensed Belarusian tax practitioner. Key areas requiring local expertise:

1. Current ESCHF technical requirements and deadlines
2. FEZ and HTP specific VAT rules
3. EAEU Protocol implementation specifics
4. Simplified regime transitional rules
5. Annual threshold updates and legislative amendments

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
