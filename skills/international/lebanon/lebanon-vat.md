---
name: lebanon-vat
description: Use this skill whenever asked to prepare, review, or advise on Lebanon VAT returns, VAT registration, or VAT classification. Trigger on phrases like "Lebanon VAT", "Lebanese VAT", "TVA Lebanon", "Lebanon tax return", "MOF Lebanon", or any request involving Lebanese VAT compliance. Lebanon imposes VAT at 11% under Law 379/2001 (Cabinet approved increase to 12% in Feb 2026, pending Parliament). WARNING: Lebanon's ongoing economic crisis may affect enforcement, exchange rate treatment, and practical compliance [T2]. ALWAYS read this skill before handling any Lebanon VAT work.
---

# Lebanon VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Lebanon |
| Jurisdiction Code | LB |
| Primary Legislation | Law No. 379 of 2001 (VAT Law) |
| Supporting Legislation | Decree No. 7336 of 2002 (VAT Implementing Regulations); Decree No. 144 of 1959 (Income Tax) |
| Tax Authority | Ministry of Finance (MOF) |
| Filing Portal | https://www.finance.gov.lb |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Lebanese tax practitioner |
| Validation Date | Pending |
| Last Research Update | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate, exempt supplies, zero-rated exports, registration threshold, filing deadlines. Tier 2: exchange rate treatment during crisis, enforcement status, partial exemption, free zone supplies. Tier 3: crisis-era regulatory changes, parallel market rates, restructuring of tax administration. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## CRITICAL WARNING: Economic Crisis Impact [T2]

Lebanon has been experiencing a severe economic and financial crisis since 2019. This affects VAT compliance in several ways:

1. **Exchange rate uncertainty:** The official exchange rate and market rate may diverge significantly. VAT calculations on foreign-currency transactions require careful treatment. [T2]
2. **Enforcement capacity:** MOF enforcement may be reduced due to institutional challenges. This does NOT remove legal obligations. [T2]
3. **Banking restrictions:** Capital controls may affect VAT payment mechanisms. [T2]
4. **Legislative changes:** Emergency measures may modify VAT rules. Monitor MOF communications. [T2]
5. **Staff shortages at MOF:** Processing of refunds and assessments may be delayed. [T2]

**Flag for practitioner: ALL Lebanon VAT work should be reviewed by a local practitioner who is current on crisis-era developments.**

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and fiscal number** [T1]
2. **VAT registration status** [T1] -- registered or not
3. **VAT period** [T1] -- quarterly
4. **Industry/sector** [T2] -- impacts exemptions
5. **Does the business make exempt supplies?** [T2] -- if yes, input tax apportionment required
6. **Does the business import goods?** [T1] -- customs VAT treatment
7. **Does the business export goods or services?** [T1] -- zero-rating
8. **Currency of transactions** [T2] -- LBP, USD, or both (critical during crisis)
9. **Which exchange rate is being used?** [T2] -- official Banque du Liban rate, Sayrafa rate, or market rate

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: VAT Rate Structure [T1]

### Standard Rate

| Rate | Application | Status |
|------|-------------|--------|
| **11%** | Standard rate on all taxable goods and services | Rate in force under Law 379/2001 |
| **12%** | Proposed new standard rate | Cabinet-approved February 2026; requires Parliamentary ratification [T2] |

**Legislation:** Law No. 379 of 2001, Article 8. Cabinet approved a VAT increase to 12% in February 2026 to fund public-sector salary increases. As of April 2026, Parliamentary approval is pending. **Flag for practitioner: confirm whether the 12% rate has been enacted before applying it.**

Lebanon has a single standard VAT rate. There are no reduced rates.

### Zero-Rated Supplies (0% VAT, Input Tax Recoverable) [T1]

- Exports of goods outside Lebanon [T1]
- International transport services [T1]
- Supplies to duty-free zones (conditions apply) [T2]

### Exempt Supplies (No VAT, No Input Recovery) [T1]

The following are exempt from VAT:
- Financial and banking services [T1]
- Insurance services [T1]
- Medical and hospital services [T1]
- Educational services (schools and universities) [T1]
- Residential rental [T1]
- Public transport [T1]
- Unprocessed agricultural products [T1]
- Printed books, newspapers, and periodicals [T1]
- Gold and precious metals (investment grade) [T2]
- Government and diplomatic supplies [T2]

**Legislation:** Law No. 379 of 2001, Articles 15-16.

---

## Step 2: VAT Registration [T1]

### Mandatory Registration

| Criterion | Threshold |
|-----------|-----------|
| Annual taxable turnover | LBP 100,000,000 (pre-crisis threshold) |
| Importers | Subject to VAT at customs regardless of turnover |

**Important [T2]:** The LBP 100,000,000 threshold was established when 1 USD = 1,507.5 LBP (official rate). Due to the currency crisis, this threshold is effectively negligible in real terms. Practically, most businesses with any meaningful turnover will exceed it. Flag for practitioner: threshold may be revised by MOF.

### Voluntary Registration [T1]

Businesses below the threshold may register voluntarily to recover input VAT on purchases.

### Registration Process [T1]

1. Submit application to MOF with commercial registration and supporting documents
2. MOF issues VAT registration certificate
3. Business must display certificate at premises
4. VAT number format: fiscal number assigned by MOF

---

## Step 3: Transaction Classification Rules [T1]

### 3a. Determine Transaction Type [T1]
- Sale of goods/services (output VAT) or Purchase (input VAT)
- Salaries, government levies, loan repayments, dividends = OUT OF SCOPE

### 3b. Determine Place of Supply [T1]
- Goods: location of delivery
- Services: where the service provider is established (general rule)
- Imports: at Lebanese customs
- Exports: zero-rated if goods leave Lebanon

### 3c. Determine VAT Rate [T1]
- 11% for all taxable supplies (single rate)
- 0% for exports and zero-rated supplies
- Exempt: no VAT charged, no input recovery

### 3d. Calculate VAT [T1]
- `VAT = Net Amount * 11%`
- `Gross = Net + VAT`
- `Net = Gross / 1.11`

---

## Step 4: VAT Return Structure [T1]

### Return Form

The VAT return filed with MOF contains:

| Section | Description |
|---------|-------------|
| A. Output VAT | VAT collected on domestic taxable supplies at 11% |
| B. Zero-rated supplies | Export and other zero-rated sales (0% output) |
| C. Exempt supplies | Exempt revenue (no VAT) |
| D. Total supplies | Sum of A + B + C |
| E. Input VAT on domestic purchases | VAT paid on local purchases at 11% |
| F. Input VAT on imports | VAT paid at customs |
| G. Total input VAT | E + F |
| H. Net VAT | Output VAT (A) minus Input VAT (G) |

### Output VAT Reporting [T1]

- All taxable domestic sales at 11%
- Zero-rated exports: reported as sales but at 0%
- Exempt supplies: reported separately, no VAT

### Input VAT Recovery [T1]

- Input VAT on purchases related to taxable supplies: **fully recoverable** [T1]
- Input VAT on purchases related to exempt supplies: **NOT recoverable** [T1]
- Input VAT on mixed-use: **apportioned** [T2]
- Input VAT paid at customs on imports: **recoverable** if for taxable supplies [T1]

### Input Tax Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```
**Flag for practitioner: apportionment method must be consistent. Annual adjustment required.**

---

## Step 5: Reverse Charge Mechanism [T1]

### When Reverse Charge Applies

- Services received from a non-resident supplier with no VAT registration in Lebanon [T1]
- The Lebanese recipient must self-assess VAT at 11% [T1]

### Procedure [T1]

1. Identify service from non-resident supplier
2. Self-assess output VAT at 11% on the service value
3. Claim input VAT at 11% if service relates to taxable supplies
4. Report both on the VAT return

### Currency Issues [T2]

- If the invoice is in foreign currency, convert to LBP for VAT purposes
- **Flag for practitioner:** Which exchange rate to use is critical. The official rate, Sayrafa rate, or market rate may produce vastly different results. Consult practitioner on current MOF guidance regarding the applicable rate.

---

## Step 6: Imports and Customs VAT [T1]

### VAT on Imports

- All goods imported into Lebanon are subject to VAT at 11% [T1]
- VAT base: CIF value plus customs duties plus any excise [T1]
- VAT collected by Lebanese Customs at point of entry [T1]
- VAT paid at customs is recoverable as input VAT [T1]

### Documentation [T1]

- Customs declaration
- Proof of VAT payment
- Import invoice

### Duty-Free Zones [T2]

- Beirut Free Zone and other designated areas have special treatment
- Goods entering free zones may be suspended from VAT
- VAT applies when goods leave free zone for domestic consumption
- Flag for practitioner: confirm current status of free zone rules

---

## Step 7: Filing Deadlines [T1]

| Period | Deadline |
|--------|----------|
| Q1 (January - March) | 20 April |
| Q2 (April - June) | 20 July |
| Q3 (July - September) | 20 October |
| Q4 (October - December) | 20 January |

**Filing is quarterly for all VAT-registered businesses.** [T1]

**Legislation:** Law No. 379 of 2001, Article 30.

### Payment [T1]

- VAT payable must be remitted with the return by the deadline
- Electronic filing available through MOF portal (when operational) [T2]
- Paper filing accepted at MOF offices [T1]

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | LBP 50,000 per day (pre-crisis amount) |
| Late payment | 1.5% per month on unpaid VAT |
| Failure to register | Backdated assessment plus penalties |
| Failure to issue invoices | Fines per MOF schedule |
| Tax evasion | Criminal penalties |

**Note [T2]:** Penalty amounts in LBP may be effectively negligible due to currency devaluation. MOF may issue updated penalty schedules. Flag for practitioner.

---

## Step 8: Invoice Requirements [T1]

VAT invoices must contain:

1. Supplier name, address, and fiscal number [T1]
2. Customer name, address, and fiscal number (B2B) [T1]
3. Invoice date and sequential number [T1]
4. Description of goods/services [T1]
5. Quantity and unit price [T1]
6. VAT rate (11%) [T1]
7. VAT amount separately stated [T1]
8. Total amount including VAT [T1]
9. Currency of the transaction [T1]

**Invoices may be in Arabic, French, or English.** [T1]

---

## Step 9: Deductibility Rules [T1]

### Non-Deductible Input VAT [T1]

Input VAT is NOT recoverable on:
- Entertainment and hospitality [T1]
- Personal-use goods and services [T1]
- Passenger vehicles (unless transport/rental business) [T1]
- Purchases related to exempt supplies [T1]
- Gifts and free samples (above de minimis thresholds) [T2]

### Blocked Categories [T1]

- Motor vehicles for personal/mixed use [T1]
- Tobacco and alcohol (personal consumption) [T1]
- Club memberships and recreational expenses [T1]

---

## Step 10: Key Thresholds

| Threshold | Value |
|-----------|-------|
| VAT rate | 11% (12% pending Parliamentary approval, Cabinet-approved Feb 2026) |
| Registration threshold | LBP 100,000,000 annual turnover |
| Filing frequency | Quarterly |
| Filing deadline | 20th of month following quarter end |
| Late payment interest | 1.5% per month |

---

## PROHIBITIONS [T1]

- NEVER apply any rate other than 11% to standard taxable supplies (Lebanon has only one rate)
- NEVER allow input VAT recovery on exempt supplies
- NEVER ignore the reverse charge on services from non-resident suppliers
- NEVER treat imports as zero-rated (VAT is paid at customs)
- NEVER allow input VAT recovery on blocked categories
- NEVER use an exchange rate without confirming with practitioner which rate MOF currently requires [T2]
- NEVER assume pre-crisis rules apply unchanged during the economic crisis
- NEVER assume MOF systems are operational without confirming [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 11: Edge Case Registry

### EC1 -- Foreign currency invoicing during crisis [T2]
**Situation:** Lebanese company invoices in USD. What exchange rate for VAT?
**Resolution:** Flag for practitioner. Multiple exchange rates exist (official BDL rate, Sayrafa platform rate, parallel market rate). MOF guidance on which rate to use for VAT purposes may change. The safest approach is to follow the most recent MOF circular. Do NOT default to any rate without practitioner confirmation.

### EC2 -- VAT refund delays [T2]
**Situation:** Business has excess input VAT and requests a refund from MOF.
**Resolution:** Flag for practitioner. VAT refunds have been subject to significant delays during the economic crisis. Refunds may be carried forward as credits indefinitely. Cash refunds from MOF may not be practically obtainable. Advise client to maintain refund documentation and carry forward.

### EC3 -- Services from non-resident, dual currency [T2]
**Situation:** Jordanian consultant invoices in USD, Lebanese company pays in LBP.
**Resolution:** Reverse charge applies at 11%. The VAT base is the USD invoice amount converted to LBP at the applicable rate. Flag for practitioner: conversion rate is critical. Self-assess output VAT and claim input VAT in LBP.

### EC4 -- Export of goods, proof requirements [T1]
**Situation:** Lebanese manufacturer exports goods to Iraq.
**Resolution:** Zero-rated if proper export documentation exists: customs export declaration, bill of lading, proof of delivery abroad. Without documentation, standard 11% VAT applies. Maintain all export records for audit.
**Legislation:** Law 379/2001, Article 17.

### EC5 -- Banking services (exempt) with input tax [T1]
**Situation:** Lebanese bank purchases IT equipment for LBP 50,000,000.
**Resolution:** Banking services are exempt. Input VAT on purchases related to exempt banking services is NOT recoverable. Bank cannot claim back the 11% VAT paid on IT equipment.

### EC6 -- Restaurant and hospitality [T1]
**Situation:** Restaurant charges customer LBP 1,000,000 for a meal.
**Resolution:** Restaurant services are taxable at 11%. Output VAT = LBP 110,000. Note: entertainment expenses incurred by other businesses at this restaurant are blocked for input VAT recovery by the customer.

### EC7 -- Construction and real estate [T2]
**Situation:** Developer constructs residential apartments and sells them.
**Resolution:** Sale of new residential property may be subject to VAT at 11%. Distinction between first sale (taxable) and subsequent sales (may be exempt or subject to registration tax). Flag for practitioner: real estate VAT treatment in Lebanon requires specialist advice.

---

## Step 12: Income Tax Reference (Out of Scope) [T3]

This skill does not compute income tax. Reference only:

- **Corporate income tax rate:** 17%
- **Personal income tax:** Progressive rates 2% to 25%
- **Built property tax:** Annual tax on rental value
- **Registration fees:** On real estate transactions
- **Stamp duty:** On contracts and documents

**Note [T2]:** Tax collection and enforcement have been severely impacted by the economic crisis. Legal obligations remain but practical compliance varies.

Escalate all income tax questions to a licensed practitioner.

---

## Step 13: Test Suite

### Test 1 -- Standard domestic sale at 11%
**Input:** Lebanese company sells goods for LBP 10,000,000 net.
**Expected output:** Output VAT = LBP 1,100,000 (11%). Total = LBP 11,100,000.

### Test 2 -- Export, zero-rated
**Input:** Lebanese company exports goods to France, value USD 5,000.
**Expected output:** VAT at 0%. Report in zero-rated section. Input VAT on related purchases is recoverable.

### Test 3 -- Reverse charge on foreign service
**Input:** Lebanese company hires UK law firm for USD 10,000. No Lebanese VAT on invoice.
**Expected output:** Self-assess output VAT at 11% on LBP equivalent. Claim input VAT at 11% if for taxable supplies. Exchange rate: flag for practitioner.

### Test 4 -- Exempt supply (financial services)
**Input:** Lebanese bank earns LBP 500,000,000 in interest income. Purchases office supplies LBP 20,000,000 + VAT LBP 2,200,000.
**Expected output:** No output VAT (exempt). Input VAT of LBP 2,200,000 NOT recoverable.

### Test 5 -- Import of goods
**Input:** Lebanese retailer imports goods from Turkey. CIF value LBP 100,000,000. Customs duty 5% = LBP 5,000,000.
**Expected output:** VAT base = LBP 105,000,000. VAT at 11% = LBP 11,550,000. Paid at customs. Recoverable as input VAT.

### Test 6 -- Blocked input VAT (entertainment)
**Input:** Lebanese company hosts client dinner, bill LBP 5,000,000 + VAT LBP 550,000.
**Expected output:** Output side: restaurant charges 11%. Input side: company cannot recover LBP 550,000 (entertainment blocked).

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
Action Required: Licensed Lebanese tax practitioner must confirm. Given the ongoing economic crisis, verify current MOF enforcement position.
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

This skill covers Lebanon's VAT system under Law 379/2001. Key considerations:
1. Lebanon has a single VAT rate of 11% -- no reduced rates
2. The ongoing economic crisis (since 2019) materially affects practical compliance [T2]
3. Exchange rate treatment is the single most significant practical challenge [T2]
4. MOF operational capacity may be limited [T2]
5. Legal obligations under the VAT law remain in force regardless of crisis conditions [T1]

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
