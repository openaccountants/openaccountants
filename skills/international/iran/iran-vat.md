---
name: iran-vat
description: Use this skill whenever asked to prepare, review, or advise on Iran VAT returns, VAT registration, or VAT classification. Trigger on phrases like "Iran VAT", "Iranian VAT", "INTA tax", "Iran tax return", "Iran value added tax", or any request involving Iranian VAT compliance. Iran imposes VAT at 10% under the VAT Law of 2008 as amended by the 2025 Budget Act. The Iranian National Tax Administration (INTA) administers the tax. ALWAYS read this skill before handling any Iran VAT work.
---

# Iran VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Iran (Islamic Republic of) |
| Jurisdiction Code | IR |
| Primary Legislation | Value Added Tax Law (approved 2008, effective 2008) |
| Supporting Legislation | VAT Implementing Regulations; Direct Tax Act (1988, as amended); Municipal Tax provisions |
| Tax Authority | Iranian National Tax Administration (INTA / Sazman-e Omur-e Maliyati) |
| Filing Portal | https://tax.gov.ir (INTA portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Iranian tax practitioner |
| Validation Date | Pending |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate, exempt supplies, zero-rated exports, registration, filing deadlines. Tier 2: municipal tax interaction, sector-specific exemptions, sanctions impact, input tax apportionment. Tier 3: oil/gas sector, free trade zones, sanctions-related complications. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and economic code (tax ID)** [T1]
2. **VAT registration status** [T1] -- registered or exempt
3. **VAT period** [T1] -- seasonal (quarterly)
4. **Industry/sector** [T2] -- impacts exemptions
5. **Does the business make exempt supplies?** [T2] -- if yes, input tax apportionment required
6. **Does the business import goods?** [T1] -- customs VAT treatment
7. **Does the business export goods or services?** [T1] -- zero-rating
8. **Does the business operate in a Free Trade-Industrial Zone?** [T2] -- special treatment

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: VAT Rate Structure [T1]

### Standard Rate

| Component | Rate |
|-----------|------|
| **VAT (effective 2025 Budget Act)** | **10%** |

**Legislation:** VAT Law of 2008, as amended; Budget Act approved 6 February 2025 (paragraph (I) of Note (1) of the Single Article) set the VAT rate at 10%.

**Note:** Prior to the 2025 Budget Act the rate was structured as 9% VAT + 1% municipal tax (Avarez). The 2025 Budget Act sets the combined rate at 10%. Practitioners should confirm whether the 9%+1% split is still reported separately on the return or whether the 10% is now a single line. [T2]

### Rate Application [T1]

- The 10% rate applies to most goods and services [T1]
- Input tax credit applies against the full 10% [T1]

### Zero-Rated Supplies (0%, Input Tax Recoverable) [T1]

- Exports of goods outside Iran [T1]
- Exports of services (conditions apply) [T2]
- Goods supplied to Free Trade-Industrial Zones [T2]

### Exempt Supplies (No VAT, No Input Recovery) [T1]

The following are exempt from VAT:
- Unprocessed agricultural products [T1]
- Livestock and poultry (live) [T1]
- Aquatic products (unprocessed) [T1]
- Bread and flour [T1]
- Books, newspapers, and magazines [T1]
- Medical and pharmaceutical products (specified list) [T1]
- Medical and health services [T1]
- Educational services [T1]
- Banking and insurance services [T1]
- Public transport (rail, urban buses) [T1]
- Residential property (first sale may be exempt, conditions) [T2]
- Handicrafts (specified) [T2]
- Carpets (handmade) [T1]
- Gold bullion and coins [T2]

**Legislation:** VAT Law of 2008, Article 12 (exemptions list).

---

## Step 2: VAT Registration [T1]

### Mandatory Registration

| Phase | Scope |
|-------|-------|
| Phase 1 (2008) | Large enterprises, manufacturers, importers |
| Phase 2 (2009-2010) | Medium enterprises |
| Phase 3 (2011+) | Gradually extended to smaller businesses |
| Current (2026) | All businesses exceeding the annual turnover threshold |

### Registration Threshold [T1]

- Businesses with annual turnover exceeding the threshold set by INTA must register [T1]
- The threshold is periodically adjusted by INTA [T2]
- Importers must register regardless of turnover [T1]

### Registration Process [T1]

1. Apply through INTA portal (tax.gov.ir)
2. Obtain economic code (tax identification number)
3. Register for VAT through the online system
4. INTA issues VAT registration confirmation

### Exemptions from Registration [T1]

- Businesses making only exempt supplies [T1]
- Businesses below the turnover threshold (unless voluntarily registered) [T1]

---

## Step 3: Transaction Classification Rules [T1]

### 3a. Determine Transaction Type [T1]
- Sale of goods/services (output VAT) or Purchase (input VAT)
- Salaries, government levies, loan repayments = OUT OF SCOPE

### 3b. Determine Place of Supply [T1]
- Goods: location of delivery within Iran
- Services: where the service is performed
- Imports: at Iranian customs
- Exports: zero-rated if goods/services leave Iran

### 3c. Determine VAT Rate [T1]
- 10% (9% VAT + 1% municipal) for all taxable supplies
- 0% for exports
- Exempt: no VAT

### 3d. Calculate VAT [T1]
- `VAT = Net Amount * 9%`
- `Municipal Tax = Net Amount * 1%`
- `Total Tax = Net Amount * 10%`
- `Gross = Net + Total Tax`

---

## Step 4: VAT Return Structure [T1]

### Return Form

The VAT return filed with INTA contains:

| Section | Description |
|---------|-------------|
| Sales (Output) | Taxable sales at 10% |
| Sales -- Zero-rated | Exports and zero-rated supplies |
| Sales -- Exempt | Exempt supplies |
| Purchases (Input) | Taxable purchases at 10% |
| Imports | VAT paid at customs |
| Net Tax | Output VAT minus Input VAT |
| VAT component | 9% portion |
| Municipal tax component | 1% portion |

### Output VAT Reporting [T1]

- Report all taxable sales at the combined 10% rate
- Separate the 9% VAT and 1% municipal tax components
- Zero-rated exports: report value, no tax
- Exempt supplies: report value, no tax

### Input VAT Recovery [T1]

- Input VAT on purchases related to taxable supplies: **fully recoverable** [T1]
- Input VAT on purchases related to exempt supplies: **NOT recoverable** [T1]
- Input VAT on mixed-use purchases: **apportioned** [T2]
- VAT paid at customs on imports: **recoverable** if for taxable supplies [T1]

### Input Tax Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```
**Flag for practitioner: method must be consistent and may require INTA approval.**

---

## Step 5: Reverse Charge Mechanism [T1]

### When Reverse Charge Applies

- Services received from a non-resident supplier not registered with INTA [T1]
- The Iranian recipient must self-assess VAT at 10% [T1]

### Procedure [T1]

1. Identify service from non-resident supplier
2. Self-assess output VAT at 10% (9% VAT + 1% municipal)
3. Claim input VAT at 10% if service relates to taxable supplies
4. Report both on the VAT return

### Exceptions [T1]

- Goods imported physically: VAT collected by Customs, not via reverse charge [T1]
- Services consumed entirely outside Iran: not subject to Iranian VAT [T1]

---

## Step 6: Imports and Customs VAT [T1]

### VAT on Imports

- All goods imported into Iran are subject to VAT at 10% [T1]
- VAT base: CIF value plus customs duties plus any commercial profit tax [T1]
- VAT collected by Iran Customs (IRICA) at point of entry [T1]
- VAT paid at customs is recoverable as input VAT [T1]

### Documentation [T1]

- Customs declaration
- Proof of VAT payment
- Import invoice
- Bill of lading / airway bill

### Free Trade-Industrial Zones [T2]

Iran has several Free Trade-Industrial Zones (e.g., Kish, Qeshm, Chabahar, Arvand, Aras):
- Goods entering free zones from abroad: exempt from VAT and customs duties [T2]
- Goods entering Iran from free zones: treated as imports, VAT applies [T2]
- Services within free zones: may be exempt [T2]
- Flag for practitioner: free zone rules vary and require specialist advice

---

## Step 7: Filing Deadlines [T1]

### Seasonal (Quarterly) Filing

| Season | Months | Filing Deadline |
|--------|--------|----------------|
| Spring | Farvardin - Khordad (Mar 21 - Jun 21) | 15th day of Tir (approx. July 6) |
| Summer | Tir - Shahrivar (Jun 22 - Sep 22) | 15th day of Mehr (approx. October 7) |
| Autumn | Mehr - Azar (Sep 23 - Dec 21) | 15th day of Dey (approx. January 5) |
| Winter | Dey - Esfand (Dec 22 - Mar 20) | 15th day of Farvardin (approx. April 4) |

**Note:** Iran uses the Solar Hijri (Jalali) calendar. Filing deadlines are expressed in Jalali dates. Gregorian equivalents are approximate.

### Payment [T1]

- VAT payable must be remitted with the return by the deadline [T1]
- Electronic filing through INTA portal [T1]
- Payment via banking system [T1]

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | 10% of tax due as penalty |
| Late payment | 2.5% per month on unpaid VAT |
| Failure to register | Backdated assessment plus penalties |
| Failure to issue invoices | Penalties per INTA schedule |
| Tax evasion | Fines plus potential criminal penalties |

---

## Step 8: Invoice Requirements [T1]

VAT invoices must contain:

1. Supplier name, address, and economic code [T1]
2. Customer name, address, and economic code (B2B) [T1]
3. Invoice date (Jalali calendar) and sequential number [T1]
4. Description of goods/services [T1]
5. Quantity and unit price [T1]
6. VAT amount (9%) separately stated [T1]
7. Municipal tax amount (1%) separately stated [T1]
8. Total amount including taxes [T1]

**Invoices must be in Farsi (Persian).** [T1]

---

## Step 9: Deductibility Rules [T1]

### Non-Deductible Input VAT [T1]

Input VAT is NOT recoverable on:
- Personal-use goods and services [T1]
- Purchases related to exempt supplies [T1]
- Entertainment (above limits) [T2]
- Passenger vehicles for personal use [T1]

### Blocked Categories [T1]

- Motor vehicles for personal use (unless transport/taxi business) [T1]
- Personal consumption items [T1]
- Gifts and donations (unless for documented business promotion) [T2]

---

## Step 10: Key Thresholds

| Threshold | Value |
|-----------|-------|
| VAT rate | 9% |
| Municipal tax rate | 1% |
| Combined effective rate | 10% |
| Filing frequency | Quarterly (seasonal) |
| Late filing penalty | 10% of tax due |
| Late payment penalty | 2.5% per month |
| Loss carry-forward (income tax) | 5 years (not VAT-related) |

---

## PROHIBITIONS [T1]

- NEVER apply a rate other than 10% to standard taxable supplies
- NEVER allow input VAT recovery on exempt supplies
- NEVER ignore the reverse charge on services from non-resident suppliers
- NEVER treat imports as zero-rated (VAT is paid at customs)
- NEVER allow input VAT recovery on blocked categories
- NEVER ignore the municipal tax component (1%) -- it is always collected with VAT
- NEVER assume Free Trade Zone rules without confirming specific zone provisions
- NEVER issue invoices without Farsi text
- NEVER use Gregorian dates on official filings (Jalali/Solar Hijri calendar is required)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 11: Edge Case Registry

### EC1 -- Split between VAT and municipal tax [T1]
**Situation:** Invoice shows 10% total tax. How to report on return?
**Resolution:** Split into 9% VAT and 1% municipal tax. Both are reported separately on the VAT return. Input credit applies against the full 10%.
**Legislation:** VAT Law of 2008.

### EC2 -- Free Trade Zone to mainland [T1]
**Situation:** Company in Kish Free Zone sells goods to customer in Tehran.
**Resolution:** Treated as an import into Iran. VAT at 10% applies when goods leave the free zone. Customs formalities required. Customer pays VAT at the customs checkpoint.

### EC3 -- Agricultural exemption [T1]
**Situation:** Farmer sells unprocessed wheat.
**Resolution:** Exempt from VAT under Article 12. No output VAT charged. No input VAT recovery on related purchases.

### EC4 -- Foreign SaaS subscription [T1]
**Situation:** Iranian company subscribes to cloud services from a non-resident provider.
**Resolution:** Reverse charge applies. Self-assess output VAT at 10% (9% + 1%). Claim input VAT if for taxable supplies. Note: international payment restrictions may affect the transaction itself but do not change the VAT treatment.

### EC5 -- Export with documentation [T1]
**Situation:** Iranian manufacturer exports carpets (machine-made) to Germany.
**Resolution:** Zero-rated if proper export documentation exists: customs export declaration, bill of lading, proof of delivery. Without documentation, 10% VAT applies.

### EC6 -- Medical supplies exemption [T1]
**Situation:** Pharmaceutical company sells medicines listed in the exempt schedule.
**Resolution:** Exempt from VAT. No output VAT. Input VAT on manufacturing inputs is NOT recoverable. This is a cost to the pharmaceutical company.

### EC7 -- Construction services [T2]
**Situation:** Construction company provides building services.
**Resolution:** Construction services are generally taxable at 10%. However, residential property rules may create complexity. Flag for practitioner: distinction between construction services and property sales requires professional judgement.

---

## Step 12: Income Tax Reference (Out of Scope) [T3]

This skill does not compute income tax. Reference only:

- **Corporate income tax rate:** 25%
- **Personal income tax:** Progressive rates
- **Withholding tax on payments to non-residents:** Various rates
- **Social security:** Employer 23%, Employee 7%

Escalate all income tax questions to a licensed practitioner.

---

## Step 13: Test Suite

### Test 1 -- Standard domestic sale
**Input:** Iranian company sells goods for IRR 100,000,000 net.
**Expected output:** VAT (9%) = IRR 9,000,000. Municipal tax (1%) = IRR 1,000,000. Total tax = IRR 10,000,000. Gross = IRR 110,000,000.

### Test 2 -- Export, zero-rated
**Input:** Iranian company exports goods to Turkey, value USD 10,000.
**Expected output:** VAT at 0%. Report in zero-rated section. Input VAT on related purchases is recoverable.

### Test 3 -- Reverse charge on foreign service
**Input:** Iranian company receives consulting from Indian firm, USD 5,000. No Iranian VAT on invoice.
**Expected output:** Self-assess VAT 9% + municipal 1% = 10% on IRR equivalent. Claim input VAT at 10% if for taxable supplies.

### Test 4 -- Exempt supply (medical)
**Input:** Pharmaceutical company sells exempt medicines for IRR 500,000,000. Purchases raw materials IRR 200,000,000 + VAT IRR 18,000,000 + municipal IRR 2,000,000.
**Expected output:** No output VAT. Input VAT of IRR 20,000,000 NOT recoverable.

### Test 5 -- Import of goods
**Input:** Iranian trader imports electronics from China. CIF value IRR 1,000,000,000. Customs duty 10% = IRR 100,000,000.
**Expected output:** VAT base = IRR 1,100,000,000. VAT (9%) = IRR 99,000,000. Municipal (1%) = IRR 11,000,000. Total = IRR 110,000,000. Paid at customs. Recoverable.

### Test 6 -- Free zone to domestic
**Input:** Company in Qeshm Free Zone sells goods worth IRR 300,000,000 to customer in Isfahan.
**Expected output:** Treated as import. VAT at 10% applies at customs checkpoint. VAT = IRR 30,000,000.

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Iranian tax practitioner must confirm.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax practitioner. Document gap.
```

---

## Contribution Notes

This skill covers Iran's VAT system under the VAT Law of 2008. Key features:
1. The effective rate is 10% (9% VAT + 1% municipal tax)
2. Both components must be tracked and reported separately
3. Iran uses the Solar Hijri (Jalali) calendar for all tax purposes
4. Invoices and filings must be in Farsi
5. Free Trade-Industrial Zones have special treatment requiring case-by-case analysis
6. International sanctions may affect cross-border transactions but do not change domestic VAT rules

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
