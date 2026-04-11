---
name: bosnia-vat
description: Use this skill whenever asked to prepare, review, or advise on a Bosnia and Herzegovina VAT (PDV) return or any transaction classification for Bosnian VAT purposes. Trigger on phrases like "Bosnia VAT", "BiH VAT", "PDV", "ITA filing", "Bosnian tax", or any request involving Bosnian VAT obligations. This skill contains the complete BiH PDV classification rules, single-rate structure, return form mappings, deductibility rules, reverse charge treatment, and filing deadlines. Bosnia has a unique single-rate VAT system at 17%. ALWAYS read this skill before touching any Bosnian VAT-related work.
---

# Bosnia and Herzegovina VAT (PDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Bosnia and Herzegovina (BiH) |
| Jurisdiction Code | BA |
| Tax Name | PDV (Porez na Dodanu Vrijednost / VAT) |
| Primary Legislation | Law on Value Added Tax (Zakon o Porezu na Dodanu Vrijednost), Official Gazette BiH No. 9/05 (as amended) |
| Supporting Legislation | Rulebook on PDV implementation; Customs Policy Law; Rulebook on invoicing |
| Tax Authority | Indirect Taxation Authority (ITA BiH -- Uprava za Neizravno Oporezivanje BiH / UIO) |
| Filing Portal | https://www.uino.gov.ba (ITA electronic services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed BiH tax practitioner |
| Validation Date | April 2026 (web-verified; practitioner sign-off still pending) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, standard classification, basic input deductions. Tier 2: entity-level complexity (Federation/RS/Brcko), partial deduction, special schemes. Tier 3: transfer pricing, inter-entity disputes. |

---

## IMPORTANT: Constitutional Structure Note [T2]

Bosnia and Herzegovina has a unique constitutional structure:
- **Federation of Bosnia and Herzegovina (FBiH)** -- one entity
- **Republika Srpska (RS)** -- second entity
- **Brcko District** -- self-governing district

**PDV (VAT) is the ONLY tax administered at the state level** by the ITA BiH. All other taxes (income tax, corporate tax) are administered at entity level. This means PDV rules are uniform across BiH regardless of which entity the business is in.

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and ID number (Identifikacijski Broj)** [T1] -- 12 or 13 digits
2. **PDV registration number** [T1] -- issued by ITA BiH upon registration
3. **PDV registration status** [T1] -- registered PDV payer or non-registered (small business)
4. **VAT period** [T1] -- monthly (standard for all PDV payers)
5. **Entity location** [T1] -- FBiH, RS, or Brcko District (relevant for other taxes, not PDV)
6. **Industry/sector** [T2] -- impacts exemptions
7. **Does the business make exempt supplies?** [T2] -- partial deduction rules apply
8. **Does the business trade cross-border?** [T1] -- impacts import/export treatment
9. **Accumulated PDV credit** [T1] -- from prior periods

**If any of items 1-4 are unknown, STOP. Do not classify any transactions.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output PDV) or Purchase (input PDV)
- Salaries, social contributions, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** Law on PDV, Article 3-4 (taxable supply)

### 1b. Determine Counterparty Location [T1]
- Bosnia and Herzegovina (domestic): supplier/customer registered in BiH (any entity)
- EU: all 27 EU member states (BiH is not an EU member; customs apply)
- CEFTA: Serbia, North Macedonia, Montenegro, Kosovo, Albania, Moldova
- Other foreign: all remaining countries

### 1c. PDV Rate [T1]

**Bosnia has a SINGLE VAT rate:**

| Rate | Application | Legislation |
|------|-------------|-------------|
| **17%** | **ALL taxable supplies -- goods and services** | Article 24 |
| 0% | Zero rate -- exports of goods, international transport, diplomatic supplies | Article 25 |
| Exempt | Financial, insurance, medical, educational, and others (Article 24) | Article 24 |

**This is the simplest VAT rate structure in Europe.** There are NO reduced rates. All taxable supplies are at 17%.

### 1d. Exempt Supplies (Article 24) [T1]

The following are exempt from PDV:
- Financial and banking services (interest, deposits, currency exchange, securities)
- Insurance and reinsurance services
- Medical and dental services (by licensed institutions/practitioners)
- Educational services (by authorized institutions)
- Cultural, artistic, and sporting services (public interest, non-commercial)
- Postal services (universal, by state operator)
- Residential property rental
- Sale of agricultural land and forests
- Gambling and lottery (separately taxed)
- Burial services
- Social welfare services
- Stamps and fiscal marks (at face value)

### 1e. Determine Expense Category [T1]
- Fixed assets: per accounting standards, useful life > 12 months
- Goods for resale: purchased for direct resale
- Raw materials: consumed in production
- Services/overheads: everything else

---

## Step 2: PDV Return Form Structure [T1]

**The PDV return (PDV Prijava) is filed monthly via the ITA BiH electronic system. All PDV payers must file electronically.**

**Legislation:** Law on PDV Article 37-39; ITA Rulebook

### Part I -- Output PDV (Supplies)

| Box | Description | Rate |
|-----|-------------|------|
| 11 | Taxable domestic supplies -- tax base | 17% |
| 12 | Output PDV at 17% | calculated |
| 13 | Zero-rated supplies (exports) | 0% |
| 14 | Exempt supplies | - |
| 15 | Reverse charge -- services from abroad (tax base) | 17% |
| 16 | Output PDV on reverse charge | calculated |
| 17 | Total tax base for all supplies | sum |
| 18 | Total output PDV (12 + 16) | sum |

### Part II -- Input PDV (Acquisitions)

| Box | Description |
|-----|-------------|
| 21 | Domestic purchases -- tax base |
| 22 | Input PDV on domestic purchases |
| 23 | Imports -- customs value + duties |
| 24 | PDV paid on imports |
| 25 | Fixed asset acquisitions -- tax base |
| 26 | Input PDV on fixed assets |
| 27 | Input PDV on reverse charge (deductible) |
| 28 | Adjustments / corrections |
| 29 | Total input PDV (22 + 24 + 26 + 27 + 28) |

### Part III -- Settlement

| Box | Description |
|-----|-------------|
| 31 | PDV payable (if 18 > 29) |
| 32 | PDV credit (if 29 > 18) |
| 33 | PDV credit from prior period |
| 34 | PDV credit for refund |
| 35 | Net PDV payable |

---

## Step 3: Reverse Charge and Import Mechanisms

### 3a. Services from Non-Residents [T1]

When a BiH entity purchases services from a non-resident with no BiH registration:
- Place of supply determined under Article 8-12 of the Law on PDV
- If place of supply is BiH, buyer self-assesses PDV at 17%
- Report in Box 15 (tax base) and Box 16 (output PDV)
- Claim input PDV in Box 27 (if entitled to deduction)
- Net effect: zero for fully taxable businesses

**Legislation:** Article 8-12, Article 14(3)

### 3b. Imports of Goods [T1]

Goods imported into BiH:
- PDV collected by ITA Customs sector at the border
- Rate: 17% (single rate)
- Tax base: customs value + import duties + excise (if applicable)
- Customs PDV is recoverable as input PDV
- Requires customs declaration as documentary evidence

### 3c. Exports [T1]

Exports of goods outside BiH:
- Zero-rated under Article 25
- Requires customs export declaration
- Related input PDV is fully deductible

### 3d. CEFTA Trade [T1]

Trade with CEFTA members:
- Standard import/export treatment (customs apply)
- CEFTA reduces/eliminates customs duties on qualifying goods
- PDV still applies at 17% on imports
- Exports are zero-rated

---

## Step 4: Input PDV Deduction Rules

### 4a. General Conditions (Article 32-34) [T1]

Input PDV is deductible if ALL conditions are met:
1. Goods/services acquired for use in taxable operations
2. A valid tax invoice (porezna faktura) is available
3. Goods/services recorded in accounting
4. For imports: customs declaration and payment proof available

### 4b. Invoice Requirements [T1]

A valid porezna faktura must contain:
- Sequential number and date
- Seller's name, address, PDV registration number
- Buyer's name, address, PDV registration number
- Description of goods/services
- Quantity and unit price (excl. PDV)
- PDV rate (17%) and amount
- Total amount including PDV
- Date of supply (if different from invoice date)

### 4c. Blocked Input PDV (Non-Deductible) [T1]

Input PDV is NOT deductible for:

| Category | Legislation |
|----------|-------------|
| Goods/services used for exempt operations | Article 32(4) |
| Passenger vehicles (purchase, lease, fuel, maintenance) | Article 32(5)(a) |
| Entertainment, hospitality, and representation expenses | Article 32(5)(b) |
| Personal consumption of employees/directors/owners | Article 32(5)(c) |
| Goods/services without valid tax invoice | Article 32(1) |
| Goods/services not related to economic activity | Article 32(3) |
| Accommodation and meals for staff (unless at remote work site) | Article 32(5) |

### 4d. Proportional Deduction (Article 33) [T2]

If a business makes both taxable and exempt supplies:
- Separate accounting of input PDV required
- Direct attribution first
- Mixed-use costs: proportional deduction

**Pro-rata formula:**
```
Deductible % = (Taxable supplies + Zero-rated supplies) /
               (Taxable supplies + Zero-rated supplies + Exempt supplies) * 100
```

Round up to nearest whole percentage. Annual adjustment required.

**Flag for reviewer: confirm calculation and methodology.**

---

## Step 5: Derived Calculations [T1]

```
Total Output PDV (Box 18) = Box 12 + Box 16

Total Input PDV (Box 29) = Box 22 + Box 24 + Box 26 + Box 27 + Box 28

IF Box 18 > Box 29 THEN
    Box 31 = Box 18 - Box 29 (PDV payable)
    Box 32 = 0
ELSE
    Box 31 = 0
    Box 32 = Box 29 - Box 18 (PDV credit)
END

Box 35 = Box 31 - Box 33 (net payable after credit)
IF Box 35 < 0 THEN Box 35 = 0; excess remains as credit
```

---

## Step 6: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory PDV registration | Annual turnover > BAM 100,000 | Article 57 |
| Voluntary registration | Below threshold, may register voluntarily | Article 57 |
| Small business exemption | Annual turnover <= BAM 100,000 | Article 57 |
| PDV refund eligibility | Credit accumulated for 3+ months, or exporters | Article 36 |
| Export refund (expedited) | Within 30 days for predominantly export businesses | Article 36 |
| Fixed asset threshold | Per accounting standards | FBiH/RS accounting laws |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|------------|--------|----------|-------------|
| PDV return | Monthly | 10th of the month following the reporting month | Article 38 |
| PDV payment | Monthly | 10th of the month following the reporting month | Article 38 |
| Import PDV | Per import | At customs clearance | Customs Policy Law |
| Annual PDV reconciliation | Annual | March 10 following year | Article 38 |

**Note:** The 10th of the following month is notably earlier than most European jurisdictions. This tight deadline requires prompt bookkeeping.

---

## Step 8: PDV Revenue Allocation [T2]

A unique feature of BiH's PDV system is the revenue allocation mechanism:
- PDV revenue collected by ITA BiH is distributed among the entities (FBiH, RS, Brcko District)
- Distribution is based on final consumption coefficients
- This does not affect the taxpayer directly but is important for understanding the administrative context
- The Single Account (Jedinstveni Racun) holds all PDV revenue before distribution

---

## Step 9: Edge Case Registry

### EC1 -- Purchase of software from US company [T1]

**Situation:** BiH company subscribes to a US-based SaaS platform. No PDV charged.
**Resolution:** Reverse charge at 17%. Box 15 = net amount, Box 16 = PDV at 17%, Box 27 = deductible PDV. Net effect zero for fully taxable business.
**Legislation:** Article 8-12, Article 14(3)

### EC2 -- Export to Serbia (CEFTA) [T1]

**Situation:** BiH company exports goods to Serbia.
**Resolution:** Zero-rated export. Customs export declaration required. Box 13. Related input PDV fully deductible. CEFTA may reduce customs duty for the Serbian buyer, but BiH PDV treatment is standard.
**Legislation:** Article 25

### EC3 -- Mixed taxable and exempt operations [T2]

**Situation:** Company provides both taxable consulting and exempt financial advisory services.
**Resolution:** Separate accounting required. Direct attribution first. Mixed costs proportionally split. Flag for reviewer: confirm allocation.
**Legislation:** Article 33

### EC4 -- Passenger vehicle purchase [T1]

**Situation:** Company purchases a sedan for business use.
**Resolution:** Input PDV is BLOCKED under Article 32(5)(a). No deduction regardless of business use. Also blocked: fuel, maintenance, insurance related to passenger vehicles. Exception: vehicles used exclusively as taxis, rental fleet, or driving school.
**Legislation:** Article 32(5)(a)

### EC5 -- Inter-entity trade (FBiH to RS) [T1]

**Situation:** Company in FBiH sells goods to company in RS.
**Resolution:** This is a DOMESTIC supply within BiH. Standard 17% PDV applies. No import/export treatment. No customs. The fact that the entities have separate corporate tax systems does not affect PDV, which is state-level.
**Legislation:** Law on PDV (applies uniformly across BiH)

### EC6 -- Credit note / return of goods [T1]

**Situation:** Buyer returns goods; seller issues credit note.
**Resolution:** Seller reduces output PDV in the current period. Buyer reduces input PDV in the current period. Corrective invoice issued. Both adjust current PDV returns.
**Legislation:** Article 19, Article 32

### EC7 -- Construction services and real property [T2]

**Situation:** Construction company builds commercial property and sells it.
**Resolution:** Sale of new commercial property is generally subject to PDV at 17%. However, sale of used real property may be exempt. Flag for reviewer: determine if the property qualifies as "new" (first transfer within 2 years of completion) or "used."
**Legislation:** Article 24 (exemptions), Article 4

### EC8 -- Advance payment received [T1]

**Situation:** Company receives an advance payment of BAM 11,700 (including PDV).
**Resolution:** PDV on advance = BAM 11,700 * 17/117 = BAM 1,700. Output PDV is due in the period the advance is received. When goods/services are delivered, the advance PDV is offset against the final invoice PDV.
**Legislation:** Article 19, Article 22

---

## PROHIBITIONS [T1]

- NEVER let AI guess PDV treatment -- classification is deterministic from facts and legislation
- NEVER apply input PDV deduction without a valid tax invoice
- NEVER allow non-registered entities to claim input PDV deductions
- NEVER apply 0% rate on exports without customs documentation
- NEVER ignore reverse charge on services from non-residents
- NEVER apply any reduced rate -- BiH has ONLY 17% and 0%, no reduced rates
- NEVER allow input PDV on passenger vehicles, entertainment, or personal consumption
- NEVER treat inter-entity trade (FBiH/RS/Brcko) as import/export -- it is domestic
- NEVER miss the 10th of month deadline -- it is earlier than most jurisdictions
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

### Test 1 -- Standard domestic sale at 17%

**Input:** BiH company sells consulting services to local client. Net BAM 10,000. PDV at 17%.
**Expected output:** Box 11 = BAM 10,000. Box 12 = BAM 1,700.

### Test 2 -- Domestic purchase with input PDV

**Input:** BiH company purchases office supplies. Gross BAM 5,850 including PDV BAM 850. Valid invoice.
**Expected output:** Box 21 includes BAM 5,000. Box 22 = BAM 850. Fully deductible.

### Test 3 -- Import of goods

**Input:** Company imports raw materials from Turkey. Customs value BAM 20,000. Customs duty BAM 1,000. No excise.
**Expected output:** PDV base = BAM 21,000. Import PDV = BAM 21,000 * 17% = BAM 3,570. Box 23 = BAM 21,000. Box 24 = BAM 3,570. Deductible.

### Test 4 -- Services from non-resident (reverse charge)

**Input:** BiH company engages a German consulting firm. Fee EUR 5,000 (equivalent BAM 9,780). No BiH registration.
**Expected output:** Box 15 = BAM 9,780. Box 16 = BAM 1,663 (17%). Box 27 = BAM 1,663. Net zero.

### Test 5 -- Export of goods

**Input:** BiH company exports furniture to Austria. Invoice BAM 15,000. Customs declaration confirmed.
**Expected output:** Box 13 = BAM 15,000. PDV = 0%. Related input PDV fully deductible.

### Test 6 -- Blocked passenger vehicle

**Input:** Company purchases a car. Gross BAM 23,400 including PDV BAM 3,400.
**Expected output:** Input PDV of BAM 3,400 is NOT deductible. Blocked under Article 32(5)(a).

### Test 7 -- Inter-entity sale (FBiH to RS)

**Input:** Company in Sarajevo (FBiH) sells goods to company in Banja Luka (RS). Net BAM 8,000.
**Expected output:** Box 11 = BAM 8,000. Box 12 = BAM 1,360 (17%). Domestic supply. No import/export treatment.

### Test 8 -- Advance payment

**Input:** Company receives advance of BAM 5,850 from customer (including PDV).
**Expected output:** PDV on advance = BAM 5,850 * 17/117 = BAM 850. Box 12 includes BAM 850 output PDV.

---

## Step 12: Penalties and Interest [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of PDV return | BAM 500-1,500 per return | Law on PDV Article 51 |
| Late payment of PDV | 0.04% per day of the outstanding amount | Law on PDV Article 51 |
| Understatement of PDV | 50% of understated amount plus interest | Law on PDV |
| Failure to register for PDV when required | Back-assessment + BAM 1,000-3,000 | Law on PDV Article 57 |
| Failure to issue proper invoice | BAM 500-1,500 per instance | Law on PDV |
| Issuing false invoices | Criminal liability | Criminal Code BiH |
| Obstruction of ITA audit | BAM 1,000-5,000 | Law on Tax Administration |

**Interest on late payments accrues daily at 0.04% of the outstanding PDV liability.**

---

## Step 13: Currency and Exchange Rate Rules [T1]

- Bosnia and Herzegovina uses the Convertible Mark (BAM -- Konvertibilna Marka)
- BAM is pegged to the Euro at a fixed rate: BAM 1 = EUR 0.51129 (1 EUR = BAM 1.95583)
- The peg is maintained by the Central Bank of BiH under a currency board arrangement
- All PDV returns are filed in BAM
- Foreign currency transactions: convert at the official Central Bank of BiH middle rate on the transaction date
- Due to the fixed EUR peg, EUR-denominated transactions have a stable conversion
- Non-EUR currencies: Central Bank middle rate on the date of the transaction

---

## Step 14: Place of Supply Rules for Services [T1]

| Service Type | Place of Supply | Legislation |
|-------------|----------------|-------------|
| B2B general services | Where recipient is established | Article 8 |
| B2C general services | Where supplier is established | Article 8 |
| Immovable property services | Where property is located | Article 9 |
| Passenger transport | Where transport takes place | Article 10 |
| Cultural/entertainment events | Where event takes place | Article 10 |
| Restaurant/catering services | Where services performed | Article 10 |
| Telecommunications and electronic (B2C) | Where recipient is located | Article 11 |

---

## Step 15: Record Keeping [T1]

PDV payers must maintain the following records for a minimum of 10 years:

| Record | Requirement |
|--------|-------------|
| Tax invoices (issued and received) | Sequential, chronological order |
| Purchase and sales ledgers | Full PDV breakdowns |
| Import/export customs documentation | Original customs declarations |
| PDV returns (all filed copies) | With ITA confirmation/receipt |
| Contracts and agreements | For all significant transactions |
| Bank statements | Complete payment trail |
| Fiscal cash register records | Daily Z-reports for cash transactions |
| General ledger and journals | Full accounting records |

**ITA BiH may conduct both desk audits (kancelarijska kontrola) and field audits (terenska kontrola). Records must be available at the registered business premises.**

---

## Contribution Notes

This skill requires validation by a licensed BiH tax practitioner (certified accountant or tax advisor). Key areas requiring local expertise:

1. ITA BiH administrative procedures and audit practices
2. PDV revenue allocation mechanics (for advisory purposes)
3. Real property PDV treatment (new vs. used)
4. Entity-level tax interactions (income tax in FBiH vs. RS vs. Brcko)
5. Current registration thresholds and administrative updates

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
