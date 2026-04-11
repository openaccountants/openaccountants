---
name: egypt-vat
description: Use this skill whenever asked to prepare, review, or advise on an Egypt VAT return, VAT classification, table tax, or any matter involving Egyptian value-added tax. Trigger on phrases like "Egypt VAT", "Egyptian VAT return", "ETA filing", "table tax", "Law 67/2016", "e-invoicing Egypt", "e-receipt Egypt", or any request involving Egypt VAT obligations. This skill contains the complete Egypt VAT rate structure, table tax (schedule tax) rates, registration rules, input credit mechanics, e-invoicing requirements, and filing deadlines required to produce correct VAT compliance advice. ALWAYS read this skill before touching any Egypt VAT-related work.
---

# Egypt VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Arab Republic of Egypt |
| Jurisdiction Code | EG |
| Primary Legislation | Law No. 67 of 2016 (Value-Added Tax Law / قانون الضريبة على القيمة المضافة) |
| Supporting Legislation | Executive Regulations of Law 67/2016 (Decree No. 66 of 2017); Law No. 3 of 2022 (amendments); Law No. 157 of 2025 (construction/contracting VAT reform); Decree Nos. 417 and 418 of 2025 (VAT regulation amendments); Ministerial decrees on e-invoicing; Stamp Duty Law |
| Tax Authority | Egyptian Tax Authority (ETA / مصلحة الضرائب المصرية) |
| Filing Portal | ETA e-filing portal — https://eservice.tax.gov.eg; e-invoice portal — https://invoicing.eta.gov.eg; e-receipt portal |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: VAT rate, table tax rates, registration threshold, input/output mechanics, filing deadlines, e-invoicing rules. Tier 2: table tax on mixed supplies, free zone treatment, reverse charge on imported services. Tier 3: transfer pricing adjustments, tax treaty implications, complex restructuring. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax consultant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Tax Registration Number (TRN / رقم التسجيل الضريبي)** [T1] -- 9-digit number
2. **VAT registration status** [T1] -- Mandatory, voluntary, or not registered
3. **Industry sector** [T2] -- determines if standard VAT, table tax, or both apply
4. **Filing period** [T1] -- monthly (standard) or bi-monthly (for certain categories per ETA direction)
5. **Does the business export goods or services?** [T1] -- zero-rated treatment
6. **Does the business make exempt supplies?** [T2] -- impacts input VAT apportionment
7. **Does the business operate in a free zone?** [T2] -- special rules for investment zones and free zones
8. **Is the entity registered on the e-invoicing platform?** [T1] -- mandatory for all registered taxpayers
9. **Is the entity registered on the e-receipt platform?** [T1] -- mandatory for B2C transactions (phased rollout)
10. **VAT credit balance carried forward from prior period** [T1]

**If items 1-2 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: VAT Rate Structure [T1]

**Legislation:** Law 67/2016, Art. 3, 11; Table 1 (attached schedule).

### Standard Rate

| Rate | Applies To | Legislation |
|------|-----------|-------------|
| 14% | All taxable goods and services not subject to table tax or exemption | Law 67/2016, Art. 3 |
| 0% | Exported goods and services; goods/services to free zones; international transport | Law 67/2016, Art. 23 |
| Exempt | Goods and services listed in the exemption schedule (Law 67/2016, Art. 29) | Law 67/2016, Art. 29; Exemption Table |

### Table Tax (ضريبة الجدول) [T1]

**Legislation:** Law 67/2016, Art. 11; Schedule 1.

Table tax is a SEPARATE levy from VAT, applied to specific goods and services at prescribed rates. Some items are subject to table tax ONLY, others to BOTH table tax AND 14% VAT.

#### Table Tax -- Goods

| Item | Table Tax Rate/Amount | Also Subject to 14% VAT? | Legislation |
|------|----------------------|--------------------------|-------------|
| Petroleum products (gasoline, diesel, kerosene, LPG) | Specific amounts per litre/ton (varies by grade) | No (table tax only) | Schedule 1, Section 1 |
| Tobacco products — cigarettes (local) | 50% of retail price + specific amount per pack | Yes — 14% VAT on (price + table tax) | Schedule 1 |
| Tobacco products — cigarettes (imported) | 50% of CIF + customs + specific amount | Yes | Schedule 1 |
| Tobacco products — molasses (معسل) | 150% (local) / 100% + specific (imported) | No | Schedule 1 |
| Beer (alcoholic) | 200% | No | Schedule 1 |
| Other alcoholic beverages | 150% | No | Schedule 1 |
| Soft drinks / carbonated beverages | 8% | No | Schedule 1 |
| Cement | EGP 65 per ton (approximate; adjusted periodically) | Yes — 14% VAT on (price + table tax) | Schedule 1 |
| Iron and steel (rebar) | 8% | No | Schedule 1 |
| Passenger vehicles (1600cc and above) | 1-30% depending on engine capacity and type | Yes — 14% on top | Schedule 1 |
| Air conditioning units | 8% | Yes — 14% on top | Schedule 1 |

#### Table Tax -- Services

| Service | Table Tax Rate | Also Subject to 14% VAT? | Legislation |
|---------|---------------|--------------------------|-------------|
| Mobile telecommunications | 8% | Yes — 14% VAT on (price + table tax) | Schedule 1 |
| Professional and consultancy services (within table) | 10% | Yes — 14% on top | Schedule 1 |
| Contracting and construction (supply & installation) | Previously 5% table tax (abolished 18 July 2025 by Law 157/2025); now subject to standard 14% VAT with full input credit | No (moved to general VAT regime) | Law 157/2025 amending Law 67/2016 |
| Non-tourist hotels/restaurants | 0% table tax (subject to 14% VAT only) | Yes | General rule |
| Tourist facilities (hotels 1-3 star) | 5% table tax | Yes — 14% on top | Schedule 1 |
| Tourist facilities (4-5 star hotels) | 10% table tax | Yes — 14% on top | Schedule 1 |
| Night clubs / entertainment venues | 10-30% | Yes — 14% on top | Schedule 1 |

### Table Tax Calculation (Where Both Apply) [T1]

When an item is subject to BOTH table tax and 14% VAT:

```
Step 1: Table Tax = Selling Price x Table Tax Rate
Step 2: VAT Base = Selling Price + Table Tax
Step 3: VAT = VAT Base x 14%
Step 4: Total Tax = Table Tax + VAT
```

**Example:** Mobile telecom service priced at EGP 100:
- Table Tax = 100 x 8% = EGP 8
- VAT = (100 + 8) x 14% = EGP 15.12
- Total tax = EGP 23.12

---

## Step 2: Registration [T1]

**Legislation:** Law 67/2016, Art. 16-22.

### Registration Thresholds

| Category | Threshold | Legislation |
|----------|-----------|-------------|
| Mandatory registration (goods and services) | Annual turnover >= EGP 500,000 (reduced to EGP 250,000 effective 2026; newly mandated taxpayers must register by 31 March 2026) | Law 67/2016, Art. 16; 2025 amendments |
| Mandatory registration (table tax goods/services) | Any amount — no threshold | Law 67/2016, Art. 17 |
| Mandatory registration (importers) | Any amount — no threshold | Law 67/2016, Art. 17 |
| Voluntary registration | Below threshold — may elect to register | Law 67/2016, Art. 18 |
| Foreign e-service providers (simplified registration) | Providing digital services to Egyptian consumers | Law 3/2022 amendments |

### Registration Process [T1]

1. Apply at competent ETA office or via e-services portal
2. Obtain Tax Registration Number (TRN)
3. Register on the ETA e-invoicing platform (mandatory)
4. Register on e-receipt platform (mandatory for B2C, per phased rollout)
5. Begin filing monthly returns

### Deregistration [T1]

| Condition | Process |
|-----------|---------|
| Turnover falls below EGP 250,000 for 12 consecutive months (previously EGP 500,000; threshold reduced in 2026) | May apply for deregistration |
| Business cessation | Must deregister within 30 days |
| On deregistration | Must account for output VAT on remaining inventory at market value |

**Legislation:** Law 67/2016, Art. 20.

---

## Step 3: Output VAT Calculation [T1]

**Legislation:** Law 67/2016, Art. 10-12.

### Standard Supplies

```
Output VAT = Taxable Value x 14%
Taxable Value = Consideration received (or market value for non-arm's length transactions)
```

### Time of Supply [T1]

| Transaction Type | Tax Point | Legislation |
|-----------------|-----------|-------------|
| Sale of goods | Delivery or invoice date, whichever is earlier | Law 67/2016, Art. 6 |
| Rendering of services | Completion of service or payment, whichever is earlier | Law 67/2016, Art. 6 |
| Imports of goods | Date of customs release | Law 67/2016, Art. 7 |
| Imports of services | Date of payment or date service is rendered in Egypt | Law 67/2016, Art. 7 |
| Continuous supply (rent, subscriptions) | Each payment date or invoice date | Law 67/2016, Art. 6 |

### Deemed Supplies [T2]

| Situation | Treatment | Legislation |
|-----------|-----------|-------------|
| Self-supply (using own goods for non-business purposes) | Output VAT on market value | Law 67/2016, Art. 9 |
| Gifts exceeding EGP 200 per recipient per annum | Output VAT on market value | Law 67/2016, Art. 9 |
| Liquidation — remaining inventory | Output VAT on market value | Law 67/2016, Art. 9 |
| Related-party transactions below market value | ETA may adjust to market value | Law 67/2016, Art. 10 |

**Flag for reviewer: deemed supply valuation requires market value determination — confirm with tax consultant.**

---

## Step 4: Zero-Rated Supplies [T1]

**Legislation:** Law 67/2016, Art. 23.

| Zero-Rated Category | Details | Legislation |
|---------------------|---------|-------------|
| Export of goods | Goods physically exported from Egypt (proof: customs export declaration) | Art. 23(1) |
| Export of services | Services provided to non-residents for use outside Egypt | Art. 23(2) |
| Goods supplied to Free Zones | Goods entering approved free zones | Art. 23(3) |
| Services to Free Zones | Services rendered to entities in free zones for activities within the zone | Art. 23(3) |
| International transport | International passenger and cargo transport by Egyptian carriers | Art. 23(4) |
| Goods in transit | Goods transiting Egypt (not cleared for domestic consumption) | Art. 23(5) |
| Supplies to diplomatic missions | With reciprocity | Art. 23(6) |
| Machinery/equipment for new projects | During establishment phase (under Investment Law incentives) | Art. 23(8); Investment Law 72/2017 |

### Proof Requirements for Zero-Rating [T1]

| Category | Required Documents |
|----------|--------------------|
| Export of goods | Customs export declaration (بيان جمركي); shipping documents; payment proof |
| Export of services | Contract with foreign entity; proof service is for use outside Egypt; payment remittance |
| Free zone supplies | Free zone entity registration; goods entry certificate |

---

## Step 5: Exempt Supplies [T1]

**Legislation:** Law 67/2016, Art. 29; Exemption Schedule.

| Exempt Category | Description | Notes |
|----------------|-------------|-------|
| Basic foodstuffs | Bread, flour, rice, sugar, tea, milk, cooking oil, beans, lentils, fresh vegetables, fresh fruits, fresh meat, poultry, fish (unprocessed) | Exemption Table Item 1 |
| Health services | Medical services by hospitals, clinics, laboratories; pharmaceutical products | Item 2 |
| Education | Tuition fees by licensed schools, universities; educational materials | Item 3 |
| Financial services | Banking services (interest, commissions); insurance premiums; stock exchange transactions | Item 5 |
| Residential rent | Rental of residential property | Item 7 |
| Land sale | Sale of undeveloped land | Item 8 |
| Newspapers and magazines | Printed publications (not advertising) | Item 9 |
| Natural gas (for residential use) | Piped natural gas for residential consumption | Item 10 |
| Agricultural inputs | Seeds, fertilizers, pesticides, animal feed | Item 11 |
| Public transport | Public bus, metro, rail transport | Item 14 |
| Electricity (residential, up to threshold) | Electricity for residential use up to specified kWh | Item 15 |
| Precious metals | Gold, silver, platinum (raw form) | Item 17 |
| Disabled persons' equipment | Wheelchairs, prosthetics, hearing aids | Item 18 |
| Blood/blood products | For medical use | Item 19 |
| Weapons/ammunition | For military/security forces | Item 20 |

### Exempt vs Zero-Rated: Key Difference [T1]

| Treatment | Output VAT | Input VAT Credit |
|-----------|-----------|-----------------|
| Zero-rated (0%) | No output VAT | Input VAT IS recoverable |
| Exempt | No output VAT | Input VAT is NOT recoverable |

---

## Step 6: Input VAT Credit Rules [T1]

**Legislation:** Law 67/2016, Art. 22, 24, 25.

### Creditable Input VAT

| Document Type | Credit Available? | Conditions |
|--------------|------------------|------------|
| Tax invoice from registered supplier (e-invoice) | Yes | Must be valid e-invoice on ETA platform |
| Customs declaration (import VAT) | Yes | For goods imported for taxable activity |
| Reverse charge self-assessed VAT (imported services) | Yes | If services used for taxable supplies |

### Input VAT Deduction Rules [T1]

```
Net VAT Payable = Output VAT - Deductible Input VAT
If Input VAT > Output VAT: excess carried forward for 6 consecutive periods, then refundable
```

**Legislation:** Law 67/2016, Art. 22.

### Timing of Input VAT Deduction [T1]

Input VAT is deductible in the period in which the tax invoice is dated, OR in the FOLLOWING two periods. After two periods, the credit is lost unless a claim is filed with ETA.

**Legislation:** Law 67/2016, Art. 22(3).

### Blocked/Non-Deductible Input VAT [T1]

**Legislation:** Law 67/2016, Art. 24, 25.

| Blocked Category | Legislation |
|-----------------|-------------|
| Passenger vehicles and related expenses (fuel, maintenance) — unless core business activity (taxi, rental, driving school) | Art. 24(1) |
| Entertainment, hospitality, and recreation expenses | Art. 24(2) |
| Personal consumption by employees or owners | Art. 24(3) |
| Goods and services used for exempt supplies | Art. 25 |
| Purchases without valid e-invoice | Art. 22 |
| Table tax (ضريبة الجدول) on goods subject to table tax only (no VAT) | Not deductible — table tax on table-only items has no credit mechanism |

### Table Tax Input Credit [T2]

| Scenario | Treatment |
|----------|-----------|
| Item subject to both table tax AND VAT | The 14% VAT portion is deductible as input VAT; the table tax portion is NOT deductible as input VAT (it is a separate levy) |
| Item subject to table tax ONLY | No input credit whatsoever |

**Flag for reviewer: table tax interaction with VAT credits is a common source of error. Verify per specific item classification.**

### Mixed Supply Apportionment [T2]

**Legislation:** Law 67/2016, Art. 25; Executive Regulations Art. 67.

If a registered person makes both taxable and exempt supplies:

```
Deductible Input VAT = Total Input VAT x (Taxable Supplies / Total Supplies)
```

Annual adjustment required at year-end based on actual annual ratio.

**Flag for reviewer: apportionment ratio must be confirmed by tax consultant. Year-end adjustment may create additional liability or credit.**

---

## Step 7: VAT Return Structure [T1]

**Legislation:** Law 67/2016, Art. 14; Executive Regulations Art. 53-55.

### Filing Period and Deadline

| Aspect | Detail |
|--------|--------|
| Standard period | Monthly |
| Deadline | Last day of the month following the tax period |
| Portal | ETA e-filing portal |
| Payment | Same deadline as filing (last day of following month) |

**Example:** January return due by 28/29 February. February return due by 31 March.

### Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TRN, name, period) |
| Part 2 | Sales — domestic taxable supplies at 14% |
| Part 3 | Sales — zero-rated supplies |
| Part 4 | Sales — exempt supplies |
| Part 5 | Table tax supplies |
| Part 6 | Total output VAT |
| Part 7 | Purchases — domestic (with input VAT) |
| Part 8 | Purchases — imports (with import VAT) |
| Part 9 | Total deductible input VAT |
| Part 10 | Net VAT payable / (credit balance) |
| Part 11 | Table tax payable |
| Part 12 | Total payable (VAT + table tax) |
| Part 13 | Credit brought forward / refund applied |
| Part 14 | Balance payable / carried forward |

### Supporting Schedules [T1]

| Schedule | Content |
|----------|---------|
| Sales schedule | Invoice-level detail for all sales (linked to e-invoicing platform) |
| Purchase schedule | Invoice-level detail for all deductible purchases |
| Table tax schedule | Details of table tax goods/services sold |
| Reverse charge schedule | Imported services subject to reverse charge |
| Credit note schedule | Adjustments for returns, discounts |

---

## Step 8: E-Invoicing (الفاتورة الإلكترونية) [T1]

**Legislation:** Law 67/2016 (as amended); Finance Act 2020 amendments; ETA Decree No. 518/2020.

### E-Invoicing Requirements

| Phase | Entities Covered | Mandatory From |
|-------|-----------------|----------------|
| Phase 1 | Large taxpayers (Cairo centre) | November 2020 |
| Phase 2 | Medium taxpayers | 2021-2022 |
| Phase 3 | All remaining registered taxpayers | Completed by July 2023 |
| Phase 4 | All VAT-registered entities (full enforcement) | Ongoing |

### E-Invoice Technical Requirements [T1]

| Requirement | Detail |
|-------------|--------|
| Format | XML/JSON via ETA API or ETA desktop application |
| Digital signature | Required — using approved Egyptian digital certificate (from ITIDA-accredited provider) |
| Unique identifier | Each invoice receives a UUID from the ETA system |
| Real-time reporting | Invoices must be reported to ETA within 24 hours of issuance |
| Invoice content | Seller TRN, buyer TRN (if B2B), description, quantity, unit price, VAT amount, table tax (if applicable), total |
| Currency | EGP (foreign currency invoices must show EGP equivalent at CBE exchange rate) |
| Archive | Electronic records retained for 5 years |

### E-Receipt System (إيصال إلكتروني) [T1]

| Aspect | Detail |
|--------|--------|
| Applies to | B2C transactions (retail, services to individuals) |
| System | ETA e-receipt platform — separate from e-invoice |
| Rollout | Phased by ETA notification (major retailers first, then expanding) |
| Requirements | POS integration with ETA; unique receipt number; digital signature |
| Penalty for non-compliance | EGP 20,000 - 100,000 per incident; potential suspension of operations |

---

## Step 9: Reverse Charge on Imported Services [T1]

**Legislation:** Law 67/2016, Art. 7, 32.

### When Reverse Charge Applies

| Scenario | Treatment |
|----------|-----------|
| Registered Egyptian entity receives services from non-resident with no Egypt establishment | Egyptian buyer must self-assess and pay 14% VAT |
| Non-registered Egyptian entity receives services from non-resident | Must register and self-assess, or the non-resident must appoint a fiscal representative |
| Services from non-resident consumed in Egypt | Reverse charge applies |
| Services from non-resident consumed outside Egypt | Outside scope — no Egyptian VAT |

### Reverse Charge Procedure [T1]

1. Egyptian buyer calculates VAT at 14% on the gross payment to the non-resident
2. Reports as output VAT in the return (reverse charge section)
3. If the service is used for taxable supplies, buyer claims equal input VAT credit
4. Net effect: zero for fully taxable businesses
5. If the service is used for exempt supplies, no input credit — effective 14% cost

### Filing the Reverse Charge [T1]

Report in the reverse charge schedule of the monthly return. Pay the VAT by the return filing deadline.

---

## Step 10: Free Zone Treatment [T2]

**Legislation:** Law 67/2016, Art. 23, 30; Investment Law 72/2017.

### Types of Free Zones

| Zone Type | VAT Treatment |
|-----------|--------------|
| Public Free Zones (المناطق الحرة العامة) | Goods/services supplied TO the zone are zero-rated; goods/services within the zone among zone entities are outside scope; goods/services FROM zone to domestic market are subject to import VAT |
| Private Free Zones (المناطق الحرة الخاصة) | Similar treatment — goods entering are zero-rated; goods exiting to domestic market are taxed as imports |
| Investment Zones (مناطق الاستثمار) | May benefit from temporary zero-rating on machinery/equipment during establishment |
| Special Economic Zones (e.g., Suez Canal Economic Zone) | Specific regime per zone legislation — T2/T3 |

**Flag for reviewer: free zone VAT treatment is complex and varies by zone type, entity status, and activity. Always verify with tax consultant.**

---

## Step 11: Filing Deadlines and Penalties [T1]

### Deadlines

| Return | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| Monthly VAT return | Calendar month | Last day of the following month | Law 67/2016, Art. 14 |
| Table tax return | With VAT return | Same deadline | Law 67/2016, Art. 14 |
| Annual reconciliation | Calendar year | With final monthly return or per ETA directive | Executive Regulations |
| E-invoice reporting | Per transaction | Within 24 hours of issuance | ETA Decree |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | EGP 3,000 - 50,000 (first offence); doubled for repeat | Law 67/2016, Art. 69 |
| Late payment | Delay interest at CBE discount rate + 2% (calculated daily) | Law 67/2016, Art. 44 |
| Failure to register | Fine + retroactive assessment of VAT from the date registration was required | Law 67/2016, Art. 65 |
| Failure to issue e-invoice | EGP 20,000 - 100,000 per invoice; repeated offence: suspension | Law 67/2016, Art. 71 |
| Issuing false invoice | 2-5 years imprisonment + fine equal to the tax evaded or EGP 10,000-50,000 (higher) | Law 67/2016, Art. 67 |
| Tax evasion | Imprisonment (1-5 years) + fine (EGP 10,000-50,000 or tax amount, whichever is higher) + court costs | Law 67/2016, Art. 67 |
| Under-reporting output VAT | Additional tax + delay interest + penalty up to 3x the underpaid amount | Law 67/2016, Art. 68 |
| Failure to maintain records | EGP 2,000 - 10,000 | Law 67/2016, Art. 70 |
| Non-compliance with e-receipt | EGP 20,000 - 100,000 per incident | ETA notifications |

---

## Step 12: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | Annual turnover >= EGP 250,000 (reduced from EGP 500,000 effective 2026) | Law 67/2016, Art. 16; 2025 amendments |
| Table tax registration | No threshold (any amount) | Law 67/2016, Art. 17 |
| Gift deemed supply threshold | > EGP 200 per recipient per year | Law 67/2016, Art. 9 |
| Input VAT credit carry-forward | 6 consecutive periods, then refundable | Law 67/2016, Art. 22 |
| Input VAT deduction timing | Period of invoice or next 2 periods | Law 67/2016, Art. 22(3) |
| Record retention | 5 years | Law 67/2016, Art. 13 |
| E-invoice reporting | Within 24 hours of issuance | ETA Decree |

---

## Step 13: Withholding VAT [T2]

**Legislation:** Law 67/2016, Art. 16-1 (added by Law 3/2022).

### Withholding VAT Regime

| Agent | Obligation |
|-------|-----------|
| Government bodies and public sector entities | Must withhold VAT from payments to registered suppliers and remit to ETA |
| Designated private sector entities (per ETA notification) | Must withhold per ETA directive |

### Withholding Rate [T2]

The standard withholding is the full 14% VAT on the payment value. The supplier receives the net amount and claims credit for the withheld tax on their return.

**Flag for reviewer: withholding VAT compliance requires careful reconciliation between the withheld amount (per the withholding agent's records) and the supplier's return. Verify ETA notifications for applicable entities.**

---

## Step 14: Edge Case Registry

### EC1 -- Tobacco Products (Double Tax) [T1]
**Situation:** Manufacturer sells cigarettes domestically.
**Resolution:** Cigarettes are subject to BOTH table tax (50% of retail price + specific amount) AND 14% VAT. VAT is calculated on the table-tax-inclusive value. Both taxes must be reported: table tax in the table tax schedule, VAT in the standard output section.
**Legislation:** Law 67/2016, Schedule 1.

### EC2 -- Mobile Telecom Services [T1]
**Situation:** Telecom company bills customer for mobile services.
**Resolution:** Subject to 8% table tax AND 14% VAT. Table tax on the service price. VAT on the (price + table tax). Report both separately.
**Legislation:** Law 67/2016, Schedule 1.

### EC3 -- Financial Services (Exempt) [T1]
**Situation:** Bank provides lending services and charges interest.
**Resolution:** Banking services (interest, commissions, letter of credit fees) are EXEMPT from VAT. No output VAT. Input VAT on bank's purchases is NOT deductible. However, ancillary services (IT, marketing by non-bank suppliers to the bank) are taxable — the bank bears irrecoverable input VAT.
**Legislation:** Law 67/2016, Art. 29; Exemption Schedule Item 5.

### EC4 -- Foreign Digital Services (Reverse Charge) [T1]
**Situation:** Egyptian company subscribes to a US cloud service (SaaS).
**Resolution:** Reverse charge at 14%. Egyptian company self-assesses output VAT on the payment, claims equal input VAT credit (if used for taxable supplies). Net effect: zero for fully taxable businesses.
**Legislation:** Law 67/2016, Art. 7, 32.

### EC5 -- Sale of Real Estate [T2]
**Situation:** Developer sells a residential apartment.
**Resolution:** Sale of undeveloped land is exempt. Sale of buildings/apartments is taxable at 14% on the construction/development value (excluding land component). Apportionment between land (exempt) and building (taxable) required. Flag for reviewer.
**Legislation:** Law 67/2016, Exemption Schedule; Executive Regulations.

### EC6 -- Passenger Vehicle Purchase [T1]
**Situation:** Company purchases a passenger car for management use.
**Resolution:** The car may be subject to table tax (depending on engine capacity: 1-30%). Additionally, 14% VAT applies on top. Input VAT on the vehicle is BLOCKED (Art. 24(1)). The table tax is also non-recoverable. Total tax is an irrecoverable cost. Exception: taxi companies, car rental businesses, driving schools.

### EC7 -- Credit Notes / Returns [T1]
**Situation:** Seller issues a credit note for returned goods.
**Resolution:** Report in the credit note schedule of the monthly return. Seller reduces output VAT in the period the credit note is issued (must be via e-invoice platform). Buyer reduces input VAT in the same period.
**Legislation:** Law 67/2016, Art. 13; Executive Regulations Art. 41.

### EC8 -- Supplies to Diplomatic Missions [T1]
**Situation:** Supplier provides goods to a foreign embassy in Cairo.
**Resolution:** Zero-rated (0% VAT) with reciprocity. Input VAT on related purchases is fully deductible. Supplier must retain proof of diplomatic status and reciprocity confirmation from the Ministry of Foreign Affairs.
**Legislation:** Law 67/2016, Art. 23(6).

### EC9 -- Mixed Taxable and Exempt Business [T2]
**Situation:** A hospital (exempt medical services) also operates a pharmacy (taxable).
**Resolution:** Input VAT must be apportioned between taxable and exempt activities. Pharmacy-specific purchases: full input credit. Hospital-specific purchases: no input credit. Shared overheads: apportion per taxable/total revenue ratio. Annual adjustment required.
**Legislation:** Law 67/2016, Art. 25; Executive Regulations Art. 67.

### EC10 -- Importation of Machinery for New Projects [T2]
**Situation:** A new factory imports production machinery during the establishment phase.
**Resolution:** May benefit from zero-rating under the Investment Law (Law 72/2017) if approved by the General Authority for Investment (GAFI). Must obtain GAFI approval letter and present to customs. Flag for reviewer: eligibility must be confirmed.
**Legislation:** Law 67/2016, Art. 23(8); Investment Law 72/2017.

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
Action Required: Licensed Egyptian tax consultant must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax consultant. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard Domestic Sale at 14%
**Input:** Registered entity sells goods domestically. Invoice: EGP 114,000 VAT-inclusive. Rate: 14%.
**Expected output:** Sales amount = EGP 100,000. Output VAT = EGP 14,000. Report in Part 2 of return.

### Test 2 -- Export Sale (Zero-Rated)
**Input:** Manufacturer exports goods worth EGP 500,000. Customs export declaration obtained.
**Expected output:** Sales amount = EGP 500,000. Output VAT = EGP 0. Report in Part 3. Input VAT on related purchases fully refundable.

### Test 3 -- Mobile Telecom (Table Tax + VAT)
**Input:** Telecom company bills EGP 100 for mobile service.
**Expected output:** Table tax = EGP 8 (8%). VAT = (100 + 8) x 14% = EGP 15.12. Total tax = EGP 23.12. Customer pays EGP 123.12. Report table tax in Part 5, VAT in Part 2/6.

### Test 4 -- Input VAT on Domestic Purchase
**Input:** Manufacturer purchases raw materials. E-invoice: value EGP 200,000, VAT EGP 28,000.
**Expected output:** Input VAT = EGP 28,000. Deductible in full. Report in Part 7/9.

### Test 5 -- Passenger Vehicle (Blocked Input)
**Input:** Non-car-rental company purchases car. Price EGP 500,000 + table tax EGP 50,000 (10%) + VAT EGP 77,000 (14% on 550,000).
**Expected output:** Input VAT EGP 77,000 BLOCKED. Table tax EGP 50,000 non-recoverable. Total irrecoverable tax = EGP 127,000.

### Test 6 -- Reverse Charge (Imported Services)
**Input:** Egyptian company pays UK law firm EGP 100,000 for legal advice. UK firm has no Egypt presence.
**Expected output:** Reverse charge: output VAT = EGP 14,000 (14%). If used for taxable supplies: input VAT credit = EGP 14,000. Net effect = zero.

### Test 7 -- Exempt Supply (Medical Services)
**Input:** Hospital provides medical services. Revenue EGP 1,000,000.
**Expected output:** Exempt. No output VAT. Input VAT on hospital purchases NOT deductible. Report in Part 4 (exempt sales).

### Test 8 -- Cigarette Sale (Table Tax + VAT)
**Input:** Manufacturer sells cigarettes. Retail price EGP 50 per pack. Table tax: 50% x 50 = EGP 25 (simplified; actual may include specific amount).
**Expected output:** Table tax = EGP 25. VAT = (50 + 25) x 14% = EGP 10.50. Total tax per pack = EGP 35.50. Consumer pays EGP 85.50.

---

## PROHIBITIONS [T1]

- NEVER claim input VAT on passenger vehicles, entertainment, or personal consumption
- NEVER claim input VAT without a valid e-invoice registered on the ETA platform
- NEVER confuse table tax with VAT — they are separate levies with different rules
- NEVER assume table tax is deductible as input VAT — it generally is not
- NEVER confuse zero-rated (input VAT refundable) with exempt (input VAT not refundable)
- NEVER issue invoices outside the e-invoicing platform — non-compliant invoices are invalid
- NEVER claim input VAT credit after 2 periods following the invoice date without ETA approval
- NEVER ignore the further 14% VAT on items subject to both table tax and VAT
- NEVER register a taxpayer below EGP 250,000 threshold without voluntary election (unless table tax or importer) -- threshold reduced from EGP 500,000 to EGP 250,000 effective 2026
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not by the AI

---

## Step 17: VAT Compliance Calendar [T1]

### Monthly Filing Timeline

| Day | Action | Notes |
|-----|--------|-------|
| 1st of month | Prior month period closes | Begin compiling e-invoice data |
| 1st-10th | Download e-invoice/e-receipt data from ETA platforms | Reconcile with accounting records |
| 1st-10th | Reconcile output VAT (sales) with e-invoice platform | Verify all invoices transmitted within 24 hours |
| 10th-20th | Reconcile input VAT (purchases); verify supplier e-invoices exist on platform | Reject invoices not on ETA platform |
| 20th-25th | Calculate table tax on applicable items; prepare return | Both VAT and table tax sections |
| 25th-last day | Review, approve, file return and remit payment | ETA e-filing portal |
| Last day of month | Filing and payment deadline | Extended if falls on official holiday |

### Pre-Filing Checklist [T1]

| Step | Action |
|------|--------|
| 1 | Download all issued e-invoices from the ETA invoicing portal for the period |
| 2 | Download all received e-invoices (purchases) from the ETA platform |
| 3 | Reconcile e-invoice data with general ledger sales and purchase records |
| 4 | Identify table tax items and calculate table tax separately |
| 5 | For items subject to both table tax and VAT, calculate VAT on the table-tax-inclusive amount |
| 6 | Identify and exclude blocked input VAT (vehicles, entertainment, personal) |
| 7 | Calculate apportionment if mixed taxable/exempt supplies |
| 8 | Apply input VAT timing rule (deductible in invoice period or next 2 periods) |
| 9 | Include reverse charge amounts for imported services |
| 10 | Carry forward credit balance from prior period |
| 11 | Compute net payable (output VAT + table tax - deductible input VAT - credits) |
| 12 | File return and remit payment via ETA portal |

---

## Step 18: Industry-Specific VAT Rules [T2]

### Construction and Real Estate

| Transaction | VAT Rate | Table Tax | Notes |
|------------|----------|-----------|-------|
| Sale of new residential apartment | 14% on building value | None | Land portion exempt; apportion required |
| Sale of commercial property | 14% | None | Full value taxable |
| Construction/contracting services (supply & installation) | 14% | None (5% table tax abolished 18 July 2025 by Law 157/2025) | Contractor now charges standard 14% VAT with full input credit; previously subject to non-creditable 5% table tax |
| Cement supply | 14% VAT on (price + table tax) | EGP 65/ton (approx.) | Dual levy |
| Iron/rebar supply | 0% VAT | 8% table tax only | Table tax only |
| Sale of undeveloped land | Exempt | None | No tax |

### Tourism and Hospitality

| Transaction | VAT Rate | Table Tax | Notes |
|------------|----------|-----------|-------|
| 5-star hotel accommodation | 14% on (price + table tax) | 10% | Dual levy |
| 3-star hotel accommodation | 14% on (price + table tax) | 5% | Dual levy |
| Restaurant services (non-tourist) | 14% | None | Standard VAT only |
| Nile cruise services | 14% on (price + table tax) | 10% (tourist facility) | Dual levy |
| Tourist guide services | 14% | None | Standard |

### Telecommunications

| Transaction | VAT Rate | Table Tax | Notes |
|------------|----------|-----------|-------|
| Mobile voice/data | 14% on (price + table tax) | 8% | Dual levy |
| Fixed line services | 14% on (price + table tax) | 8% | Dual levy |
| Internet services | 14% on (price + table tax) | 8% | Dual levy |
| Equipment sales | 14% | None | Standard VAT only |

### Petroleum and Energy

| Transaction | VAT Rate | Table Tax | Notes |
|------------|----------|-----------|-------|
| Gasoline (Octane 95) | None (table tax only) | Specific per litre | Table tax only |
| Diesel | None (table tax only) | Specific per litre | Table tax only |
| LPG | None (table tax only) | Specific per ton | Table tax only |
| Natural gas (commercial) | 14% | None | Standard rate |
| Natural gas (residential) | Exempt | None | Exemption Schedule |

**Flag for reviewer: petroleum table tax amounts are adjusted by ministerial decree, sometimes quarterly. Verify current specific amounts.**

---

## Step 19: Dispute Resolution [T2]

**Legislation:** Law 67/2016, Art. 55-63.

| Stage | Forum | Deadline |
|-------|-------|----------|
| 1. Internal review | Request to ETA head of district | 30 days from assessment |
| 2. Internal committee | ETA Internal Committee of Appeal | 30 days from review decision |
| 3. Tax Court (لجان الطعن الضريبي) | Tax Dispute Resolution Committee | 30 days from committee decision |
| 4. Administrative Court | Court of first instance | 60 days from tax court decision |
| 5. Court of Appeal | Second instance | Per court rules |
| 6. Court of Cassation | Final appeal (on law only) | Per court rules |

### Settlement and Conciliation [T2]

The ETA may offer settlement for disputed amounts. Taxpayers may negotiate through the Tax Dispute Resolution Committees. Penalties may be reduced through settlement.

**Flag for reviewer: tax disputes should involve a licensed tax consultant. Do not respond to assessments without professional advice.**

---

## Step 20: Direct Tax Reference (Out of Scope) [T3]

This skill does NOT cover direct taxes. The following is reference only:

- **Corporate Income Tax:** Standard rate 22.5%. Oil/gas: 40.55%. Suez Canal Authority, EGPC, CBE: 40%. Legislation: Income Tax Law No. 91/2005.
- **Individual Income Tax:** Progressive rates 0-27.5%. Legislation: Law 91/2005.
- **Stamp Duty:** Various rates (0.1-1%) on contracts, financial instruments, etc. Legislation: Stamp Duty Law 111/1980.
- **Social Insurance:** Employer 18.75%, employee 11% (on basic salary, capped). Legislation: Social Insurance Law 148/2019.
- **Withholding Tax on Dividends:** 10%. Legislation: Law 91/2005.

---

## Contribution Notes

This skill covers the Egypt VAT framework as of early 2026. Egypt's VAT system underwent significant reform with the introduction of Law 67/2016, subsequent amendments (Law 3/2022), and the rollout of e-invoicing and e-receipts. Practitioners must monitor ETA decrees and ministerial announcements for rate adjustments, table tax changes, and e-invoicing platform updates.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
