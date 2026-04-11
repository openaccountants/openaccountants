---
name: pakistan-sales-tax
description: Use this skill whenever asked to prepare, review, or advise on Pakistan sales tax returns, federal or provincial, sales tax classification, or any matter involving Pakistan's indirect tax system. Trigger on phrases like "Pakistan sales tax", "FBR return", "IRIS portal", "federal sales tax", "Sindh sales tax", "Punjab sales tax", "KP sales tax", "sales tax on goods", "sales tax on services", "SRB", "PRA", "KPRA", or any request involving Pakistan sales tax compliance. This skill contains the complete Pakistan federal sales tax rate structure, provincial sales tax rates on services, input/output mechanics, IRIS filing rules, zero-rated and exempt categories, and withholding agent obligations. ALWAYS read this skill before touching any Pakistan sales tax-related work.
---

# Pakistan Sales Tax Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Islamic Republic of Pakistan |
| Jurisdiction Code | PK |
| Primary Legislation | Sales Tax Act, 1990 (Federal — on goods); Provincial sales tax legislation (on services) |
| Supporting Legislation | Sales Tax Rules, 2006; SRO notifications; Federal Excise Act, 2005; Customs Act, 1969 (import stage); Provincial Acts: Sindh Sales Tax on Services Act 2011, Punjab Sales Tax on Services Act 2012, KP Finance Act 2013, Balochistan Sales Tax on Services Act 2015, ICT (Tax on Services) Ordinance 2001 |
| Tax Authority | Federal Board of Revenue (FBR) — goods; Sindh Revenue Board (SRB) — Sindh services; Punjab Revenue Authority (PRA) — Punjab services; KPRA — KP services; BRA — Balochistan services; ITA — ICT services |
| Filing Portal | IRIS (Inland Revenue Information System) — https://iris.fbr.gov.pk (Federal); SRB e-filing — https://e.srb.gos.pk; PRA e-filing — https://pra.punjab.gov.pk; KPRA — https://kpra.kp.gov.pk |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending — requires validation by a licensed Pakistan Chartered Accountant (CA) or tax practitioner |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: federal sales tax rate, provincial rates, input/output mechanics, filing deadlines, zero-rated categories. Tier 2: SRO-based exemptions/concessions, withholding agent determinations, provincial vs federal jurisdiction disputes. Tier 3: customs valuation, transfer pricing on imports, anti-dumping, complex refund claims. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed CA/tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and National Tax Number (NTN)** [T1] -- 7-digit NTN issued by FBR
2. **Sales Tax Registration Number (STRN)** [T1] -- 13-digit for federal; separate registration for provincial (SRB/PRA/KPRA/BRA)
3. **Business type** [T1] -- Manufacturer, importer, wholesaler, distributor, retailer, service provider, or exporter
4. **Province(s) of operation** [T1] -- determines which provincial sales tax on services applies (Sindh, Punjab, KP, Balochistan, ICT)
5. **Is the entity on the Active Taxpayers List (ATL)?** [T1] -- non-ATL entities face higher withholding rates
6. **Filing period** [T1] -- monthly (standard for all registered persons)
7. **Does the business export goods?** [T1] -- zero-rated treatment; export refund implications
8. **Is the entity a withholding agent?** [T2] -- government departments, autonomous bodies, and specified companies must withhold sales tax
9. **Is the entity in a SRO-based concessionary regime?** [T2] -- various SROs grant reduced rates or exemptions for specific sectors
10. **Excess input tax carried forward from prior period** [T1]

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: Federal Sales Tax on Goods [T1]

**Legislation:** Sales Tax Act, 1990 (STA 1990), Section 3.

### Standard Rate

| Rate | Applies To | Legislation |
|------|-----------|-------------|
| 18% | All taxable goods manufactured in or imported into Pakistan (standard rate) | STA 1990, s.3(1) |
| 0% | Zero-rated goods (Fifth Schedule to STA 1990) | STA 1990, s.4 |
| Exempt | Exempt goods (Sixth Schedule to STA 1990) | STA 1990, s.13 |
| Reduced rates | Specific goods under various SROs (e.g., 1%, 2%, 5%, 10%, 12% for specified items) | Various SROs |

### Taxable Event [T1]

| Event | When Tax Applies | Legislation |
|-------|-----------------|-------------|
| Domestic supply | At time of supply (invoice date or delivery, whichever is earlier) | STA 1990, s.2(44), s.3 |
| Import | At time of customs clearance (paid along with customs duty) | STA 1990, s.3(1)(b) |
| Deemed supply | Self-consumption, gifts, free samples, transfer between units | STA 1990, s.2(33) read with s.3 |

### Further Tax on Supplies to Unregistered Persons [T1]

| Rate | Applies When | Legislation |
|------|-------------|-------------|
| 3% (additional) | Sales by registered manufacturer/importer to unregistered buyer | STA 1990, s.3(1A) |

This additional 3% is levied on top of the standard 18%, making the effective rate 21% for supplies to unregistered persons.

---

## Step 2: Provincial Sales Tax on Services [T1]

**Legislation:** Provincial Acts (see metadata).

### Provincial Rates Summary

| Province / Territory | Standard Rate | Key Legislation |
|---------------------|---------------|-----------------|
| Sindh (SRB) | 15% | Sindh Sales Tax on Services Act, 2011 (amended by Sindh Finance Act 2025) |
| Punjab (PRA) | 16% | Punjab Sales Tax on Services Act, 2012 |
| Khyber Pakhtunkhwa (KPRA) | 15% | KP Finance Act, 2013 |
| Balochistan (BRA) | 15% | Balochistan Sales Tax on Services Act, 2015 |
| Islamabad Capital Territory (ICT) | 16% | ICT (Tax on Services) Ordinance, 2001 |
| Azad Jammu & Kashmir (AJK) | 15% | AJK Sales Tax on Services Act |

### Reduced Rates by Province (Selected) [T2]

| Province | Service Category | Rate |
|----------|-----------------|------|
| Sindh | IT services, BPO, call centres | 3-8% (concessionary, per Second Schedule Part II) |
| Sindh | Restaurants (non-franchise) | 5-8% (varies, per Second Schedule Part II) |
| Punjab | IT exports | 0% |
| Punjab | Construction services | 16% |
| KP | Telecommunications | 15% |
| ICT | Hotels and restaurants | 16% |

**Flag for reviewer: reduced rates change frequently via provincial finance acts and notifications. Verify current rate for the specific service category.**

### Federal vs Provincial Jurisdiction [T2]

| Supply Type | Tax Authority | Rate |
|------------|---------------|------|
| Goods (tangible movable property) | FBR (Federal) | 18% |
| Services (general rule) | Provincial authority where service is performed/rendered | Varies by province |
| Goods + services bundled | Split required: goods portion to FBR, services portion to province | T2 — flag for reviewer |
| Imported services | Federal (FBR) — reverse charge on imports | 18% |
| Telecommunications | Provincial (after 18th Amendment) | Provincial rate |
| Financial services | Federal or Provincial — depends on nature | T2 — disputed |

**Flag for reviewer: the federal/provincial split on certain services (banking, insurance, franchisor fees) remains contested. Always verify current jurisdiction.**

---

## Step 3: Registration [T1]

**Legislation:** STA 1990, s.14; Sales Tax Rules 2006, Chapter II.

### Mandatory Registration

| Person | Must Register? | Legislation |
|--------|---------------|-------------|
| Manufacturer with annual turnover > PKR 10,000,000 | Yes | STA 1990, s.14 |
| Importer (any amount) | Yes (registered at customs stage) | STA 1990, s.14 |
| Wholesaler/distributor | Yes (if annual turnover > PKR 10,000,000) | STA 1990, s.14 |
| Retailer (Tier 1) — large retailers, chain stores, operating in air-conditioned space | Yes | STA 1990, s.14; Third Schedule |
| Exporter | Yes | STA 1990, s.14 |
| Service provider (provincial registration) | Per provincial threshold (varies) | Provincial Acts |

### Active Taxpayers List (ATL) [T1]

| Status | Consequence |
|--------|-------------|
| On ATL | Standard withholding rates apply |
| NOT on ATL | Withholding rates increased (typically double the normal rate) |

FBR publishes the ATL periodically. Entities must file income tax returns to remain on the ATL.

---

## Step 4: Output Tax Calculation [T1]

**Legislation:** STA 1990, s.3, s.7.

### For Manufacturers and Importers

```
Output Tax = Value of Supply x 18%
Value of Supply = Transaction value (exclusive of sales tax)
```

If price is tax-inclusive:
```
Value of Supply = Tax-inclusive Price / 1.18
Output Tax = Value of Supply x 18%
```

### Retail Price Based Assessment [T1]

For goods listed in the Third Schedule to STA 1990 (including beverages, cement, paints, household electrical goods, etc.), sales tax is levied on the **retail price** printed on the package, not the transaction value.

**Legislation:** STA 1990, s.3(2)(a); Third Schedule.

### Value of Supply for Imports [T1]

```
Value for Sales Tax = Customs Value + Customs Duty + Federal Excise Duty (if any) + Other Charges
Import Sales Tax = Value x 18%
```

**Legislation:** STA 1990, s.2(46)(a).

---

## Step 5: Input Tax Credit Rules [T1]

**Legislation:** STA 1990, s.7, s.8.

### Creditable Input Tax

| Source | Credit Available? | Conditions |
|--------|------------------|------------|
| Tax paid on domestic purchases (from registered suppliers) | Yes | Valid tax invoice with STRN; supplier must be on CREST/ATL |
| Tax paid on imports (customs paid receipts) | Yes | Goods Declaration (GD) with sales tax paid |
| Provincial sales tax on services used in manufacturing | Yes — cross-crediting under certain conditions | FBR-SRB/PRA mutual credit arrangement |

### Input Tax Adjustable Against Output Tax [T1]

```
Net Tax Payable = Output Tax - Admissible Input Tax
If Input Tax > Output Tax: excess carried forward (or refund claimed if exporter)
```

**Legislation:** STA 1990, s.7(1).

### Blocked/Non-Admissible Input Tax [T1]

**Legislation:** STA 1990, s.8(1); SRO 490(I)/2004 (with amendments).

| Blocked Category | Legislation |
|-----------------|-------------|
| Vehicles (all types, including passenger cars) — unless dealer/manufacturer | STA 1990, s.8(1)(a) |
| Entertainment, gifts, and giveaways | STA 1990, s.8(1)(a) |
| Goods/services not used in taxable supplies | STA 1990, s.8(1)(b) |
| Purchases from unregistered suppliers (no valid STRN) | STA 1990, s.8(1)(c) |
| Food, beverages, garments for staff/directors | STA 1990, s.8(1)(a) |
| Construction materials (unless in construction business) | STA 1990, s.8(1)(ca) |
| Input on exempt supplies | STA 1990, s.8(1)(b) |
| Purchases where invoice does not meet prescribed format | SRO 490(I)/2004 |

### Apportionment for Mixed Supplies [T2]

If a registered person makes both taxable and exempt supplies:

```
Admissible Input Tax = Total Input Tax x (Taxable Supplies / Total Supplies)
```

**Flag for reviewer: apportionment method must be applied consistently. FBR may challenge methodology.**

---

## Step 6: Zero-Rated Supplies [T1]

**Legislation:** STA 1990, s.4; Fifth Schedule.

### Key Zero-Rated Categories

| Category | Items | Fifth Schedule Part |
|----------|-------|-------------------|
| Exports | All goods exported from Pakistan | Part I |
| Supplies to diplomats | Goods to diplomatic missions with reciprocity | Part I |
| IT exports | Software, IT services exported (zero-rated under SRO 1125(I)/2011) | SRO-based |
| Essential items (when specified) | Certain food items, agricultural inputs (per annual budget SRO) | Part II (varies) |
| Supplies to EPZs/SEZs | Goods supplied to Export Processing Zones, Special Economic Zones | Part I |

### Export Refund Mechanism [T2]

Exporters may claim refund of input tax paid on purchases used in exported goods:

| Refund Method | Process | Timeline |
|--------------|---------|----------|
| FASTER (Fully Automated Sales Tax e-Refund) | Automated refund through FASTER module in IRIS | Target: 72 hours (actual may vary) |
| Manual refund claim | File application with Collectorate; audit may be required | 60-120 days typically |
| Sales Tax Refund Bonds (DTRE) | Duty and Tax Remission for Exports scheme | Upon export |

**Legislation:** STA 1990, s.10; SRO 711(I)/2007 (FASTER); SRO 450(I)/2001 (DTRE).

**Flag for reviewer: refund claims are frequently audited. Documentation must be comprehensive. Verify FASTER eligibility.**

---

## Step 7: Exempt Supplies [T1]

**Legislation:** STA 1990, s.13; Sixth Schedule.

### Key Exempt Categories

| Category | Items | Notes |
|----------|-------|-------|
| Basic foodstuffs | Wheat, rice, pulses, fresh vegetables, fresh fruits, fresh meat, live animals | Table I, Sixth Schedule |
| Agricultural inputs | Seeds, fertilizers, pesticides, tractors, agriculture machinery | Table I |
| Medical / pharmaceutical | Pharmaceutical raw materials, finished drugs, medical equipment, surgical instruments | Table I |
| Education | Books, textbooks, printed materials | Table I |
| Energy | Crude oil, natural gas (for specified use), electricity (residential up to specified consumption) | Table I |
| Arms / defence | Military equipment (for government use) | Table I |
| Gold / precious metals | Gold bars, silver bars (for certain uses) | Table I |
| Handicrafts | Handicrafts produced by cottage industry | Table I |

### Exempt vs Zero-Rated: Key Difference [T1]

| Treatment | Output Tax | Input Tax Credit |
|-----------|-----------|-----------------|
| Zero-rated (0%) | No output tax charged | Input tax IS recoverable (refundable) |
| Exempt | No output tax charged | Input tax is NOT recoverable |

---

## Step 8: Sales Tax Return Structure [T1]

**Legislation:** STA 1990, s.26; Sales Tax Rules 2006, Rule 18.

### Filing Period and Deadline

| Aspect | Detail |
|--------|--------|
| Period | Monthly (calendar month) |
| Deadline | 18th of the following month (extended deadlines announced periodically) |
| Portal | IRIS — https://iris.fbr.gov.pk |
| Form | Sales Tax Return (electronically via IRIS) |

### Return Sections

| Section | Description |
|---------|-------------|
| Section A | General information (NTN, STRN, period) |
| Section B | Domestic sales — taxable supplies |
| Section C | Export sales — zero-rated supplies |
| Section D | Exempt supplies |
| Section E | Total output tax |
| Section F | Domestic purchases — input tax |
| Section G | Import purchases — input tax |
| Section H | Total admissible input tax |
| Section I | Net tax payable / refundable |
| Section J | Tax already deposited (advance tax, withholding) |
| Section K | Balance payable / refundable |

### Annexures Required with Return [T1]

| Annexure | Content |
|----------|---------|
| Annex A | Sales to registered persons (invoice-level detail) |
| Annex B | Sales to unregistered persons |
| Annex C | Purchases from registered persons (invoice-level detail) |
| Annex D | Import details (GD number, date, customs station) |
| Annex E | Sales returns / debit-credit notes |
| Annex F | Purchases from unregistered persons |
| Annex G | Summary of provincial sales tax on services (if applicable) |
| Annex H | Withholding agent details (if applicable) |
| Annex I | POS integrated invoice data (for Tier 1 retailers) |

### Invoice-Level Reporting [T1]

All supplies to registered persons must be reported at individual invoice level in Annex A, including:
- Buyer STRN
- Invoice number and date
- Taxable value
- Sales tax amount
- HS code (for goods)

---

## Step 9: Withholding of Sales Tax [T2]

**Legislation:** STA 1990, s.3(7); SRO 660(I)/2007 (with amendments).

### Withholding Agents

| Agent Category | Withholding Obligation |
|---------------|----------------------|
| Federal/provincial government departments | Must withhold sales tax from payments to registered suppliers |
| Autonomous bodies and public sector enterprises | Must withhold |
| Companies listed on Pakistan Stock Exchange | Must withhold on specified goods/services |
| Specified large taxpayers | As notified by FBR |

### Withholding Rates [T2]

| Scenario | Rate |
|----------|------|
| Standard withholding (ATL supplier) | 1/5th of sales tax (i.e., approximately 3.6% of gross value) |
| Non-ATL supplier | 1/4th of sales tax or higher per SRO |
| Unregistered supplier | Full rate (18% or more) |

**Flag for reviewer: withholding rates and applicable SROs change frequently. Verify current rate via latest FBR notification.**

---

## Step 10: E-Invoicing and POS Integration [T1]

**Legislation:** STA 1990, s.2(14A); SRO 1279(I)/2020; Finance Act 2021.

### Point of Sale (POS) Integration

| Requirement | Detail |
|-------------|--------|
| Mandatory for | Tier 1 retailers (large retailers, chain stores, restaurants, hotels, etc.) |
| System | FBR POS integration — real-time reporting of each invoice to FBR |
| Incentive | 1% reduction in sales tax rate (effective rate 17% instead of 18%) for POS-integrated retailers — Finance Act 2024 |
| Non-compliance penalty | PKR 500,000 per POS (or 200% of tax involved, whichever is higher) |

### Electronic Invoicing [T1]

| Aspect | Detail |
|--------|--------|
| Tax invoice format | Must include: supplier name, STRN, buyer name, buyer STRN (if registered), date, serial number, description of goods, quantity, value, sales tax amount, total |
| Invoice retention | 6 years from the date of filing the return |
| Electronic record keeping | FBR may require electronic records; IRIS auto-populates from invoices |

---

## Step 11: Federal Excise Duty (FED) — Related Reference [T1]

**Legislation:** Federal Excise Act, 2005.

FED is a separate levy but interacts with sales tax:

| Item | FED Rate | Interaction with Sales Tax |
|------|----------|---------------------------|
| Cigarettes (Tier 1) | PKR 6,500 per 1,000 sticks (approximate, changes annually) | FED + sales tax both apply |
| Cigarettes (Tier 2) | PKR 1,650 per 1,000 sticks (approximate) | FED + sales tax both apply |
| Beverages (carbonated) | 13-20% | FED applies; sales tax on FED-inclusive value |
| Cement | PKR 2 per kg | FED + sales tax |
| Telecommunication services | 16% | FED on telecom (federal), not provincial sales tax |
| Air travel | 5-10% | FED applies |

**FED is computed before sales tax. Sales tax value of supply includes FED.**

---

## Step 12: Filing Deadlines and Penalties [T1]

### Deadlines

| Return | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| Federal sales tax return | Monthly | 18th of following month | STA 1990, s.26 |
| Sindh sales tax return (SRB) | Monthly | 15th of following month | Sindh SST Act, s.29 |
| Punjab sales tax return (PRA) | Monthly | 15th of following month | Punjab SST Act, s.30 |
| KP sales tax return (KPRA) | Monthly / Quarterly (for small service providers) | 15th of following month | KP Finance Act |
| Withholding statements | Monthly | With sales tax return | SRO 660(I)/2007 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of return | PKR 5,000 per day or 1% of tax due per day (higher of the two; max 100% of tax) | STA 1990, s.33(1) |
| Failure to register | PKR 10,000 or 5% of tax due (higher) | STA 1990, s.33(3) |
| Tax fraud / evasion | Up to 100% of tax evaded + imprisonment (up to 5 years for criminal prosecution) | STA 1990, s.33(5), s.37 |
| Failure to issue invoice | PKR 25,000 per instance or 3% of tax (higher) | STA 1990, s.33(7) |
| Failure to maintain records | PKR 10,000 per instance | STA 1990, s.33(8) |
| Non-integration of POS (retailers) | PKR 500,000 per POS | Finance Act 2021 |
| Late payment | Default surcharge: KIBOR + 3% per annum, calculated daily | STA 1990, s.34 |

---

## Step 13: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Federal sales tax registration (manufacturers) | Annual turnover > PKR 10,000,000 | STA 1990, s.14 |
| Standard federal sales tax rate | 18% | STA 1990, s.3 |
| Further tax on unregistered buyers | Additional 3% | STA 1990, s.3(1A) |
| POS integration tax reduction | 1% (effective 17%) | Finance Act 2024 |
| Invoice retention | 6 years | STA 1990, s.22 |
| Default surcharge | KIBOR + 3% per annum | STA 1990, s.34 |
| Export refund FASTER target | 72 hours | FBR circulars |

---

## Step 14: Edge Case Registry

### EC1 -- Goods vs Services Classification [T2]
**Situation:** Client provides "turnkey" solutions combining goods (hardware) and services (installation, maintenance).
**Resolution:** Must split into goods component (federal sales tax at 18%) and services component (provincial sales tax at applicable rate). If not separated, entire supply may be taxed at 18% federal rate. Flag for reviewer for apportionment methodology.
**Legislation:** STA 1990, s.2(33); various tribunal decisions.

### EC2 -- Input Tax from Non-ATL Supplier [T1]
**Situation:** Registered person purchases from a supplier not on the Active Taxpayers List.
**Resolution:** Input tax from non-ATL suppliers is inadmissible. Additionally, withholding rate is higher. Verify supplier ATL status before accepting input tax credit.
**Legislation:** STA 1990, s.8(1); FBR Circular.

### EC3 -- Inter-Provincial Service Supply [T2]
**Situation:** A Punjab-registered service provider renders services in Sindh.
**Resolution:** Tax jurisdiction follows the place where the service is rendered/consumed. If service is performed in Sindh, Sindh sales tax (SRB) applies at 15%, not Punjab rate. The service provider may need to register with SRB. Flag for reviewer.
**Legislation:** Respective provincial Acts; constitutional provisions (18th Amendment).

### EC4 -- Import of Services (Reverse Charge) [T1]
**Situation:** Pakistan company pays a foreign company for software licensing (no Pakistan establishment).
**Resolution:** Pakistan buyer must self-assess and pay sales tax at 18% on the value of imported services. File under "imports" section of the return. Input credit may be available if services are used for taxable supplies.
**Legislation:** STA 1990, s.3(1)(b) read with s.2(33A).

### EC5 -- Sales Tax on Electricity Bills [T1]
**Situation:** Sales tax is charged on commercial electricity bills.
**Resolution:** Sales tax on electricity is levied at source by the distribution company (DISCO). The buyer can claim input tax credit for the sales tax portion of the electricity bill if the electricity is used for taxable manufacturing activity. Residential consumption is exempt up to specified units.
**Legislation:** STA 1990, Sixth Schedule; SRO notifications.

### EC6 -- Used/Second-Hand Goods [T2]
**Situation:** Registered person sells used machinery or equipment.
**Resolution:** Sales tax at 18% applies on the transaction value. If the item was previously claimed as input tax, output tax is due on sale. If no input tax was ever claimed (e.g., purchased from unregistered person), flag for reviewer regarding whether output tax applies and at what value.
**Legislation:** STA 1990, s.3; FBR rulings.

### EC7 -- Sales Tax Refund for Exporters (Stuck Refund) [T2]
**Situation:** Exporter has been waiting for refund longer than 72 hours under FASTER.
**Resolution:** If FASTER refund is delayed, exporter may file a manual refund claim with the Large Taxpayer Unit (LTU) or Regional Tax Office (RTO). Post-refund audit is common. Maintain complete chain of purchase-to-export documentation. Flag for reviewer.
**Legislation:** STA 1990, s.10; FASTER rules.

### EC8 -- Cottage Industry / Small Manufacturer Exemption [T1]
**Situation:** Small manufacturer with annual turnover below PKR 10,000,000.
**Resolution:** Not required to register for federal sales tax. However, if voluntarily registered, must comply with all filing obligations. Provincial service obligations may still apply if providing services.
**Legislation:** STA 1990, s.14.

### EC9 -- Credit / Debit Notes [T1]
**Situation:** Sales return or price adjustment after original invoice.
**Resolution:** Issue a debit note (additional tax) or credit note (reduced tax). Report in Annex E of the sales tax return. Adjust output tax in the period the note is issued. Buyer must correspondingly adjust input tax.
**Legislation:** STA 1990, s.9; Sales Tax Rules 2006, Rule 22.

### EC10 -- E-Commerce and Marketplace Sales [T2]
**Situation:** Seller operates through an e-commerce marketplace (e.g., Daraz).
**Resolution:** The marketplace may act as withholding agent for sales tax. If the seller is registered, they file their own return and claim credit for tax withheld by the marketplace. If unregistered and below threshold, marketplace withholding may be the final tax. Flag for reviewer for specifics.
**Legislation:** Finance Act 2023 amendments; FBR notifications on e-commerce.

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Pakistan CA or tax practitioner must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed CA/tax practitioner. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard Domestic Sale of Goods
**Input:** Registered manufacturer sells goods to registered buyer. Invoice: PKR 118,000 (tax-inclusive). Rate: 18%.
**Expected output:** Value of supply = PKR 100,000. Output tax = PKR 18,000. Report in Section B of return, Annex A (with buyer STRN).

### Test 2 -- Sale to Unregistered Person (Further Tax)
**Input:** Registered manufacturer sells goods to unregistered buyer. Value: PKR 100,000 (excluding tax).
**Expected output:** Sales tax = PKR 18,000 (18%). Further tax = PKR 3,000 (3%). Total sales tax = PKR 21,000. Report in Section B and Annex B.

### Test 3 -- Export (Zero-Rated)
**Input:** Exporter ships goods worth PKR 500,000 to a US buyer. Export declaration obtained.
**Expected output:** Output tax = PKR 0 (zero-rated). Report in Section C. Input tax on related purchases fully refundable.

### Test 4 -- Input Tax on Domestic Purchase
**Input:** Registered manufacturer buys raw materials from registered supplier. Invoice: value PKR 200,000, sales tax PKR 36,000. Supplier is on ATL.
**Expected output:** Input tax = PKR 36,000. Admissible. Report in Section F, Annex C.

### Test 5 -- Input Tax from Non-ATL Supplier (Blocked)
**Input:** Registered person purchases goods from supplier NOT on ATL. Invoice shows sales tax PKR 18,000.
**Expected output:** Input tax = PKR 18,000. NOT admissible (supplier not on ATL). Cannot claim credit.

### Test 6 -- Import of Goods
**Input:** Importer clears goods at customs. Customs value PKR 1,000,000. Customs duty PKR 100,000. No FED.
**Expected output:** Value for sales tax = PKR 1,100,000. Import sales tax = PKR 198,000 (18%). Paid to customs. Input credit available. Report in Section G, Annex D.

### Test 7 -- Service Provider (Sindh)
**Input:** IT company in Karachi provides IT services to local client. Invoice: PKR 115,000 (tax-inclusive). SRB rate: 15%.
**Expected output:** Value = PKR 100,000. Sindh sales tax = PKR 15,000. File with SRB, not FBR.

### Test 8 -- Import of Services (Reverse Charge)
**Input:** Pakistan company pays US consulting firm PKR 500,000 for advisory services. No Pakistan presence.
**Expected output:** Self-assess federal sales tax = PKR 90,000 (18%). Report as import of services. Input credit available if used for taxable supplies.

---

## PROHIBITIONS [T1]

- NEVER claim input tax from suppliers not on the Active Taxpayers List
- NEVER claim input tax without a valid tax invoice containing supplier STRN
- NEVER claim input tax on vehicles, entertainment, personal consumption, or gifts
- NEVER confuse federal sales tax (goods) with provincial sales tax (services) — different authorities, different rates, different returns
- NEVER ignore the further tax (3%) on supplies to unregistered persons
- NEVER file a federal return for provincial services or vice versa
- NEVER ignore POS integration requirements for Tier 1 retailers
- NEVER assume export refund will be automatic — documentation and FASTER/manual procedures apply
- NEVER confuse zero-rated (input credit available) with exempt (no input credit)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not by the AI

---

## Step 17: Sales Tax Compliance Calendar [T1]

### Monthly Filing Timeline

| Day | Action | Notes |
|-----|--------|-------|
| 1st of month | Prior month period closes | Begin compiling invoices |
| 1st-5th | Reconcile Annex A (sales to registered) with accounting records | Match STRN, invoice numbers |
| 1st-5th | Reconcile Annex C (purchases from registered) with supplier data | Verify ATL status of all suppliers |
| 5th-10th | Reconcile import data (Annex D) with customs GDs | Match GD numbers, values |
| 10th-15th | Prepare return; calculate output, input, further tax, withholding | All sections A-K |
| 15th-17th | Review and approve return | Internal review before submission |
| 18th | Filing and payment deadline (Federal) | IRIS portal |
| 15th | Filing deadline (SRB/PRA/KPRA) | Provincial portals |

### Pre-Filing Checklist [T1]

| Step | Action |
|------|--------|
| 1 | Verify all suppliers are on the Active Taxpayers List (ATL) |
| 2 | Ensure all tax invoices meet prescribed format (STRN, amounts, description) |
| 3 | Reconcile POS data with sales records (Tier 1 retailers) |
| 4 | Calculate further tax on sales to unregistered persons |
| 5 | Prepare withholding schedules (if withholding agent) |
| 6 | Reconcile provincial sales tax obligations separately from federal |
| 7 | Apply any SRO-based exemptions or reduced rates (with documentation) |
| 8 | Calculate net payable: output - input - withholding credits |
| 9 | Generate CPR (Computerized Payment Receipt) for payment |
| 10 | File return via IRIS and retain acknowledgment |

---

## Step 18: Industry-Specific Rules [T2]

### Textile Sector

| Item | Treatment | Legislation |
|------|-----------|-------------|
| Raw cotton | Exempt (Sixth Schedule) | STA 1990, Sixth Schedule |
| Yarn (manufactured) | Taxable at 18% | Standard rate |
| Fabric (manufactured) | Taxable at 18% (or reduced per SRO) | SRO-dependent |
| Garments (export) | Zero-rated | Fifth Schedule |
| Machinery for textiles | Reduced rate (per SRO) | SRO 1125(I)/2011 and successors |

### Pharmaceutical Sector

| Item | Treatment | Legislation |
|------|-----------|-------------|
| Raw materials for drugs | Exempt or reduced (per Sixth Schedule) | Sixth Schedule |
| Finished pharmaceutical products | Exempt (most) | Sixth Schedule |
| Medical devices | Exempt (selected items) | Sixth Schedule |
| Cosmetics / personal care (non-pharmaceutical) | Taxable at 18% | Standard rate |

### Automobile Sector

| Item | Treatment | Legislation |
|------|-----------|-------------|
| Locally assembled vehicles | 18% + FED (varies by engine capacity) | STA 1990 + FED Act |
| Imported vehicles (CBU) | 18% + customs duty + FED + additional customs duty | Multiple levies |
| Spare parts (imported) | 18% + customs duty | STA 1990 |
| Electric vehicles (EVs) | Reduced rates per EV policy | SRO-based incentives |

### IT and Technology

| Item | Treatment | Legislation |
|------|-----------|-------------|
| IT exports (software, BPO) | Zero-rated (federal) | SRO 1125(I)/2011 |
| IT services (domestic, Sindh) | 3-8% (concessionary SRB rate, Second Schedule Part II) | SRB notifications / Sindh Finance Act 2025 |
| IT services (domestic, Punjab) | 16% (standard PRA rate) | PRA standard |
| Hardware imports | 18% + customs duty | Standard |
| Mobile phones (imported) | 18% + regulatory duty + PTA levy | Multiple levies |

**Flag for reviewer: industry-specific SROs change with each Finance Act. Always verify current applicable SRO.**

---

## Step 19: DTRE Scheme (Duty and Tax Remission for Exports) [T2]

**Legislation:** SRO 450(I)/2001 (with amendments).

### Overview

The DTRE scheme allows exporters to procure raw materials, components, and packing materials without paying customs duty and sales tax, provided the inputs are used in manufacturing exported goods.

| Aspect | Detail |
|--------|--------|
| Eligibility | Registered manufacturers who export or supply to direct exporters |
| Coverage | Customs duty, sales tax, FED, and additional customs duty on imported inputs |
| Application | Apply to FBR for DTRE approval; submit input-output ratios |
| Verification | Post-clearance audit by FBR; must demonstrate inputs were used in exported goods |
| Penalty for misuse | Recovery of all remitted duties/taxes + penalties |

### DTRE vs Export Refund

| Feature | DTRE | Export Refund (FASTER) |
|---------|------|-----------------------|
| Timing | Tax not paid upfront | Tax paid, then refunded |
| Cash flow | Better (no outlay) | Worse (cash tied up until refund) |
| Documentation | Input-output ratios required | Purchase/export chain required |
| Audit risk | High (post-clearance) | High (pre/post-refund) |
| Eligibility | Manufacturers only | All exporters |

---

## Step 20: Dispute Resolution [T2]

**Legislation:** STA 1990, s.45A-46.

| Stage | Forum | Deadline |
|-------|-------|----------|
| 1. Show cause notice | Issued by officer (assessment/audit) | Response within 30 days |
| 2. Order-in-Original (OIO) | Adjudication by Assistant/Deputy Commissioner | Within 120 days of show cause |
| 3. First appeal | Commissioner (Appeals) | Within 30 days of OIO |
| 4. Second appeal | Appellate Tribunal Inland Revenue (ATIR) | Within 30 days of Commissioner's order |
| 5. Reference to High Court | On question of law only | Within 90 days of ATIR order |
| 6. Supreme Court | Leave to appeal | Per court rules |

### Alternative Dispute Resolution (ADR) [T2]

FBR offers ADR under the Customs Act and STA 1990. Taxpayer may apply for ADR committee to resolve disputes. Committee includes FBR officers and external members.

**Flag for reviewer: all tax disputes should involve a qualified tax practitioner. Do not respond to show cause notices without professional advice.**

---

## Step 21: Direct Tax Reference (Out of Scope) [T3]

This skill does NOT cover direct taxes. The following is reference only:

- **Corporate Income Tax:** Standard rate 29% (banking: 39%). Small company: 20% (turnover <= PKR 250 million). Legislation: Income Tax Ordinance, 2001.
- **Individual Income Tax:** Progressive rates 0-35%. Legislation: Income Tax Ordinance, 2001.
- **Capital Gains Tax:** Rates vary by asset type and holding period. Legislation: Income Tax Ordinance, 2001.
- **Minimum Tax:** 1.25% of turnover. Legislation: ITO 2001, s.113.
- **Super Tax:** 1-10% (depending on sector and income level). Legislation: ITO 2001, s.4B.

---

## Contribution Notes

This skill covers the Pakistan federal and provincial sales tax framework as of early 2026. Pakistan's sales tax system is subject to frequent changes through Finance Acts, SROs, and FBR circulars. Practitioners must monitor FBR and provincial revenue authority notifications regularly.

**A skill may not be published without sign-off from a licensed practitioner (Chartered Accountant or registered tax practitioner) in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
