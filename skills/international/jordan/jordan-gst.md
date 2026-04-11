---
name: jordan-gst
description: Use this skill whenever asked to prepare, review, or advise on Jordan General Sales Tax (GST) returns, GST registration, or GST classification. Trigger on phrases like "Jordan GST", "Jordan VAT", "Jordan sales tax", "ISTD return", "Jordan tax return", or any request involving Jordanian indirect tax compliance. Jordan imposes a General Sales Tax (GST) at 16% under the General Sales Tax Law No. 6 of 1994. This skill contains the complete GST classification rules, rate structure, registration thresholds, return procedures, and filing deadlines. ALWAYS read this skill before handling any Jordan GST work.
---

# Jordan General Sales Tax (GST) Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Jordan |
| Jurisdiction Code | JO |
| Primary Legislation | General Sales Tax Law No. 6 of 1994 (as amended) |
| Supporting Legislation | General Sales Tax Regulations; Special Sales Tax Law (excise); Income Tax Law No. 34 of 2014 |
| Tax Authority | Income and Sales Tax Department (ISTD) |
| Filing Portal | https://www.istd.gov.jo |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Jordanian tax practitioner |
| Validation Date | Pending |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate application, exempt supplies, zero-rated supplies, registration threshold, filing deadlines. Tier 2: sector-specific exemptions, input tax apportionment, free zone treatment. Tier 3: customs disputes, tax treaty interaction, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and tax identification number (TIN)** [T1]
2. **GST registration status** [T1] -- mandatory or voluntary
3. **GST period** [T1] -- monthly or bi-monthly (based on turnover)
4. **Industry/sector** [T2] -- impacts exemptions and special rates
5. **Does the business make exempt supplies?** [T2] -- if yes, input tax apportionment required
6. **Does the business import goods?** [T1] -- impacts customs GST treatment
7. **Does the business operate in a free zone?** [T2] -- special GST treatment applies
8. **Does the business export goods or services?** [T1] -- zero-rating may apply

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: GST Rate Structure [T1]

### Standard Rate

| Rate | Application |
|------|-------------|
| **16%** | Standard rate on most goods and services |

### Special Rates [T1]

| Rate | Application |
|------|-------------|
| 0% | Exports of goods; certain basic foodstuffs (bread, rice, sugar, milk, etc.) |
| 4% | Telecommunications services (domestic) |
| 5% | Certain specified services |
| 8% | Certain specified goods |
| 10% | Certain specified goods and services |
| 16% | Standard rate -- all supplies not specifically listed at another rate |
| 24% | Special Sales Tax on certain digital / telecom services (non-resident digital service providers) [T2] |

**Legislation:** General Sales Tax Law No. 6 of 1994, Schedules.

### Zero-Rated Supplies [T1]

The following are zero-rated (0% GST, input tax recoverable):
- Exports of goods outside Jordan [T1]
- Goods supplied to free zones [T2] -- conditions apply
- International transport services [T1]
- Certain basic foodstuffs specified by Cabinet decision [T1]

### Exempt Supplies (No GST, No Input Recovery) [T1]

The following are exempt from GST:
- Financial services (banking, insurance) [T1]
- Medical and health services [T1]
- Educational services [T1]
- Residential rental (unfurnished) [T1]
- Agricultural products (unprocessed) [T1]
- Government-to-government transactions [T2]
- Charitable organizations (conditions apply) [T2]

**Legislation:** General Sales Tax Law, Schedule of Exempt Supplies.

---

## Step 2: GST Registration [T1]

### Mandatory Registration

| Criterion | Threshold |
|-----------|-----------|
| Annual taxable turnover (goods, non-SST) | JOD 75,000 or more |
| Annual taxable turnover (services) | JOD 30,000 or more |
| Annual taxable turnover (goods under SST) | JOD 10,000 or more |
| Importers | Mandatory regardless of turnover |
| Service providers receiving services from abroad | Mandatory (reverse charge) |

### Voluntary Registration [T1]

Businesses below the applicable threshold (JOD 75,000 / 30,000 / 10,000) may register voluntarily if they:
- Make taxable supplies [T1]
- Can demonstrate legitimate business activity [T2]

### Registration Process [T1]

1. Apply to ISTD with commercial registration, national ID, and financial records
2. ISTD issues GST registration certificate and TIN
3. Registration is effective from the date of application or as directed by ISTD

### Deregistration [T2]

Voluntary deregistration is possible if:
- Taxable supplies fall below the threshold for 12 consecutive months
- Business ceases to make taxable supplies
- ISTD approval required

---

## Step 3: Transaction Classification Rules [T1]

### 3a. Determine Transaction Type [T1]
- Sale of goods (output GST) or Purchase of goods/services (input GST)
- Salaries, government levies, loan repayments, dividends = OUT OF SCOPE

### 3b. Determine Place of Supply [T1]
- Goods: where the goods are delivered or made available
- Services: where the service is performed or where the recipient is established
- Imports: at point of entry into Jordan (customs)
- Exports: zero-rated if goods leave Jordan

### 3c. Determine GST Rate [T1]
- Check against the rate schedules (0%, 4%, 5%, 8%, 10%, 16%)
- Default to 16% if not specifically listed at another rate
- Calculate from amounts: `rate = gst_amount / net_amount * 100`

### 3d. Determine Expense Category [T1]
- Capital goods: fixed assets used in the business
- Inventory/resale: goods purchased for resale
- Overhead/services: general business expenses

---

## Step 4: GST Return Form [T1]

### Return Structure

The GST return filed with ISTD contains the following main sections:

| Section | Description |
|---------|-------------|
| Output GST | GST collected on sales at each applicable rate |
| Input GST | GST paid on purchases (deductible) |
| Imports | GST paid at customs on imported goods |
| Exports | Zero-rated export sales |
| Exempt supplies | Sales exempt from GST (no output, no input recovery) |
| Net GST | Output GST minus deductible input GST |

### Output GST Reporting [T1]

Report output GST by rate:
- 16% standard rate supplies
- Special rate supplies (4%, 5%, 8%, 10%) -- each reported separately
- Zero-rated supplies (reported but no GST)
- Exempt supplies (reported but no GST)

### Input GST Recovery [T1]

- Input GST on purchases related to taxable supplies: **fully recoverable** [T1]
- Input GST on purchases related to exempt supplies: **NOT recoverable** [T1]
- Input GST on mixed-use purchases: **apportioned** [T2]

### Input Tax Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```
**Flag for practitioner: apportionment method must be agreed with ISTD. Annual adjustment may be required.**

---

## Step 5: Reverse Charge Mechanism [T1]

### When Reverse Charge Applies

- Services received from a non-resident supplier [T1]
- The Jordanian recipient must self-assess GST at 16% [T1]
- Report as both output GST and input GST on the return [T1]
- Net effect is zero for fully taxable businesses [T1]

### Reverse Charge Procedure [T1]

1. Identify service received from non-resident with no Jordanian GST registration
2. Self-assess output GST at 16% on the service value
3. Claim input GST at 16% if the service relates to taxable supplies
4. Report both on the GST return for the relevant period

### Exceptions [T1]

- Goods imported physically: GST collected by Customs at border, NOT via reverse charge
- Services consumed entirely outside Jordan: NOT subject to Jordanian GST
- Services from suppliers with Jordanian GST registration: normal input GST treatment

---

## Step 6: Imports and Customs GST [T1]

### GST on Imports

- All goods imported into Jordan are subject to GST at the applicable rate [T1]
- GST is assessed on the CIF value plus customs duties [T1]
- GST is collected by Jordan Customs at the point of entry [T1]
- GST paid at customs is recoverable as input GST if goods are for taxable supplies [T1]

### Documentation [T1]

- Customs declaration (Single Administrative Document)
- Proof of GST payment at customs
- Import invoices

### Free Zone Imports [T2]

- Goods entering free zones may be exempt from GST
- GST applies when goods leave the free zone for domestic consumption
- Flag for practitioner: free zone rules are complex and vary by zone

---

## Step 7: Special Sales Tax (Excise) [T1]

Jordan imposes a Special Sales Tax on certain goods, in addition to GST:

| Product | Special Tax Rate |
|---------|-----------------|
| Tobacco products | Variable, high rates |
| Alcohol | Variable, high rates |
| Fuel and petroleum | Specific rates per unit |
| Motor vehicles | Based on engine capacity and type |
| Soft drinks and energy drinks | Specified rates |

**Legislation:** Special Sales Tax provisions within the General Sales Tax Law.

**Note:** Special Sales Tax is SEPARATE from GST. Both may apply to the same transaction. The special tax is generally computed first, then GST applies on the total including special tax. [T2]

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| Large taxpayers (annual turnover > JOD 1 million) | Monthly | End of the month following the tax period |
| Other registered taxpayers | Bi-monthly | End of the month following the bi-monthly period |
| Import GST | At time of import | Paid at customs clearance |

### Bi-Monthly Periods [T1]

| Period | Months | Filing Deadline |
|--------|--------|----------------|
| Period 1 | January - February | 31 March |
| Period 2 | March - April | 31 May |
| Period 3 | May - June | 31 July |
| Period 4 | July - August | 30 September |
| Period 5 | September - October | 30 November |
| Period 6 | November - December | 31 January |

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | JOD 100 - JOD 500 per return |
| Late payment | 4% of tax due for the first week; 1% per week thereafter |
| Tax evasion | Fines and imprisonment under law |
| Failure to register | Backdated registration plus penalties |
| Failure to issue invoices | Fines per ISTD schedule |

---

## Step 9: Invoice Requirements [T1]

GST-registered businesses must issue invoices containing:

1. Supplier name, address, and TIN [T1]
2. Customer name, address, and TIN (for B2B) [T1]
3. Invoice date and sequential number [T1]
4. Description of goods/services [T1]
5. Quantity and unit price [T1]
6. GST rate applied [T1]
7. GST amount separately stated [T1]
8. Total amount including GST [T1]

**Invoices must be in Arabic.** Bilingual invoices (Arabic + English) are acceptable. [T1]

---

## Step 10: Deductibility Rules [T1]

### Non-Deductible Input GST [T1]

Input GST is NOT recoverable on:
- Entertainment and hospitality expenses [T1]
- Motor vehicles for personal use [T1]
- Goods and services not related to taxable business activity [T1]
- Purchases related to exempt supplies [T1]

### Blocked Categories [T1]

- Personal-use goods [T1]
- Gifts and donations (unless for business promotion, subject to limits) [T2]
- Passenger vehicles (unless core business activity is transport or car rental) [T1]

---

## PROHIBITIONS [T1]

- NEVER apply a GST rate other than the legislated rates (0%, 4%, 5%, 8%, 10%, 16%)
- NEVER allow input GST recovery on exempt supplies
- NEVER ignore the reverse charge on services from non-resident suppliers
- NEVER treat imports as zero-rated (GST is paid at customs)
- NEVER allow input GST recovery on blocked categories
- NEVER file a return without confirming the correct filing period (monthly vs bi-monthly)
- NEVER issue GST invoices without Arabic text
- NEVER assume free zone treatment without confirming specific zone rules with practitioner
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 11: Edge Case Registry

### EC1 -- Services from foreign SaaS provider [T1]
**Situation:** Jordanian company subscribes to US-based software (e.g., Salesforce). No GST on invoice.
**Resolution:** Reverse charge applies. Self-assess output GST at 16%. Claim input GST at 16% if related to taxable supplies. Net effect zero for fully taxable business.
**Legislation:** General Sales Tax Law No. 6/1994, reverse charge provisions.

### EC2 -- Export of services [T2]
**Situation:** Jordanian consulting firm provides services to a client in UAE.
**Resolution:** Services exported outside Jordan may be zero-rated, but conditions must be met: (a) service is performed for a non-resident; (b) benefit of service is received outside Jordan. Flag for practitioner: "benefit received outside Jordan" test requires professional judgement.

### EC3 -- Mixed-use purchase (taxable + exempt activities) [T2]
**Situation:** Company provides both taxable consulting and exempt financial services. Purchases office rent.
**Resolution:** Input GST on rent must be apportioned between taxable and exempt activities. Apportionment ratio based on relative turnover or other ISTD-agreed method. Flag for practitioner to confirm method.

### EC4 -- Free zone to domestic supply [T1]
**Situation:** Goods stored in Aqaba Special Economic Zone are sold to a customer in Amman.
**Resolution:** GST applies when goods leave the free zone for domestic consumption. GST is assessed on the value at the point of exit from the zone. Customs formalities apply.

### EC5 -- Telecommunications services at 4% [T1]
**Situation:** Mobile phone company bills JOD 100 for monthly services.
**Resolution:** GST at 4% applies to telecommunications services, not the standard 16%. Output GST = JOD 4. Input GST on related purchases is recoverable at the rate paid (which may be 16% on equipment purchases).

### EC6 -- Credit notes [T1]
**Situation:** Supplier issues a credit note for returned goods.
**Resolution:** Credit note reduces output GST in the period issued. Must contain the same information as the original invoice plus reference to original invoice number. Adjust the GST return accordingly.

### EC7 -- Government contracts [T2]
**Situation:** Company provides services to a Jordanian government ministry.
**Resolution:** Government entities may withhold income tax at source. GST still applies at the standard rate on the supply. The withholding is for income tax, not GST. Confirm whether the government entity is GST-registered for any reverse charge implications.

---

## Step 12: Income Tax Reference (Out of Scope) [T3]

This skill does not compute income tax. Reference only:

- **Corporate income tax rate:** 20% standard; higher for banks (35%), telecoms (24%), mining (30%)
- **Personal income tax:** Progressive rates 5% to 30%
- **Social security:** 21.75% total (employer 14.25%, employee 7.5%)
- **Filing:** Annual income tax returns to ISTD

Escalate all income tax questions to a licensed practitioner.

---

## Step 13: Test Suite

### Test 1 -- Standard domestic sale at 16%
**Input:** Jordanian company sells goods for JOD 1,000 net to a local customer.
**Expected output:** Output GST = JOD 160 (16%). Total invoice = JOD 1,160. Report in standard rate section of GST return.

### Test 2 -- Export of goods, zero-rated
**Input:** Jordanian manufacturer exports goods worth JOD 5,000 to Saudi Arabia.
**Expected output:** GST at 0%. Report JOD 5,000 in zero-rated exports section. All input GST on related purchases is recoverable.

### Test 3 -- Reverse charge on foreign service
**Input:** Jordanian company receives IT consulting from UK firm, USD 2,000 (approx JOD 1,420), no GST on invoice.
**Expected output:** Self-assess output GST JOD 227.20 (16%). Claim input GST JOD 227.20. Net effect zero if fully taxable.

### Test 4 -- Telecom services at special rate
**Input:** Jordanian telecom company invoices JOD 50,000 for monthly services.
**Expected output:** Output GST at 4% = JOD 2,000. Not 16%.

### Test 5 -- Exempt supply, no recovery
**Input:** Jordanian bank provides financial services. Revenue JOD 100,000. Purchases JOD 20,000 (GST paid JOD 3,200).
**Expected output:** No output GST on financial services (exempt). Input GST of JOD 3,200 is NOT recoverable.

### Test 6 -- Import of goods
**Input:** Jordanian retailer imports electronics from China. CIF value JOD 10,000. Customs duty 10% = JOD 1,000.
**Expected output:** GST base = JOD 11,000 (CIF + duty). GST at 16% = JOD 1,760. Paid at customs. Recoverable as input GST.

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
Action Required: Licensed Jordanian tax practitioner must confirm.
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

This skill covers Jordan's General Sales Tax system. Key differences from EU-style VAT:
1. The tax is called "General Sales Tax" (GST), not VAT
2. Multiple special rates exist (4%, 5%, 8%, 10%) in addition to the standard 16%
3. Special Sales Tax (excise) is a separate layer applied to specific goods
4. ISTD administers both income tax and GST
5. Invoices must be in Arabic

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
