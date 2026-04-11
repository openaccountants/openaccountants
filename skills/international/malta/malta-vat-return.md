---
name: malta-vat-return
description: Use this skill whenever asked to prepare, review, or create a Malta VAT return (VAT3 form) or Article 11 annual declaration for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT3", "create the return", "Article 11 declaration", or any request involving Malta VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Malta VAT classification rules, box mappings, deductibility rules, reverse charge treatment, capital goods thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work.
---

# Malta VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Malta |
| Jurisdiction Code | MT |
| Primary Legislation | VAT Act Chapter 406, Laws of Malta |
| Supporting Legislation | 10th Schedule (blocked categories); Article 22(4) (partial exemption); Article 24 (capital goods) |
| Tax Authority | Commissioner for Revenue (CFR), Malta |
| Filing Portal | https://cfr.gov.mt (VAT Online) |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated By | Michael Cutajar, Kevin Farrugia (warranted accountants) |
| Validation Date | March 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption pro-rata, sector-specific deductibility. Tier 3: complex group structures, non-standard supplies. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A warranted accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to warranted accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT number** [T1] -- MT + 8 digits for Article 10
2. **VAT registration type** [T1] -- Article 10 (standard), Article 11 (small enterprise exempt), or Article 12
3. **VAT period** [T1] -- quarterly start month, or annual for Article 11
4. **Industry/sector** [T2] -- impacts deductibility (e.g., hospitality can deduct entertainment; confirm with reviewer)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (pro-rata rate needed; reviewer must confirm rate)
6. **Does the business trade goods for resale?** [T1] -- impacts Box 27/28/29 classification
7. **Excess credit brought forward** [T1] -- from prior period (Box 44)
8. **Does the client have employees?** [T1] -- impacts SSC/FSS obligations (separate from VAT, out of scope of this skill)

For Article 11 clients [T1]: also ask about other income sources (rental income counts toward EUR 35,000 threshold).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, contractor payments, tax payments, loan repayments, dividends, bank charges = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act Cap. 406, Article 2 (definitions of taxable supply)

### 1b. Determine Counterparty Location [T1]
- Malta (local): supplier/customer country is MT
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, etc.)
- **Note:** UK is Non-EU post-Brexit. Gibraltar is Non-EU. Channel Islands are Non-EU.

### 1c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize to nearest standard rate: 0%, 5%, 7%, 12%, 18%
- Boundaries: <= 1% = 0%; 2-6% = 5%; 6-9.5% = 7%; 9.5-15% = 12%; >= 15% = 18%
- **Legislation:** VAT Act Cap. 406, 5th Schedule (reduced rates)

### 1d. Determine Expense Category [T1]
- Capital goods: only if gross amount >= EUR 1,160 (Article 24 threshold)
- Items below EUR 1,160 go to Services & Overheads, NOT Capital Goods
- Resale: goods bought to literally resell (not inputs consumed in delivering a service)
- Overhead/services: everything else
- **Legislation:** VAT Act Cap. 406, Article 24 (Capital Goods Scheme)

---

## Step 2: Box Assignment (100% Deterministic) [T1]

**Legislation:** VAT Act Cap. 406, Article 20 (output tax); Article 21 (input tax deduction); CFR VAT3 form guidance.

### Purchases -- Local (Malta Supplier)

| VAT Rate | Category | Box | Tax Box |
|----------|----------|-----|---------|
| 0% | Any (not resale) | null (no entry) | -- |
| 0% | Resale | Box29 | -- |
| 5% | Overhead | Box32 | 38 |
| 7% | Overhead | Box31a | 37a |
| 12% | Overhead | Box31b | 37b |
| 18% | Overhead | Box31 | 37 |
| 5% | Resale | Box28 | 35 |
| 18% | Resale | Box27 | 34 |
| Any | Capital (>= EUR 1,160) | Box30 | 36 |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Box | Notes |
|------|-----|-------|
| Physical goods | Box9 / Box13 | Also creates Box3 / Box6 output |
| Services | Box9a / Box13a | Also creates Box3 / Box6 output |
| Capital >= EUR 1,160 | Box10 / Box14 | Also creates Box3 / Box6 output |
| Out-of-scope (wages etc) | null | NEVER reverse charge |
| Local consumption (hotel, restaurant, taxi) | null | VAT paid at source abroad |

### Purchases -- Non-EU Supplier (Reverse Charge)

| Type | Box | Notes |
|------|-----|-------|
| All services/goods | Box11 / Box15 | Also creates Box4 / Box7 output |
| Out-of-scope | null | NEVER reverse charge |
| Local consumption | null | VAT paid at source abroad |

### Sales -- Local

| Rate | Box | Tax Box |
|------|-----|---------|
| 18% | Box18 | 23 |
| 12% | Box18b | 23b |
| 7% | Box18a | 23a |
| 5% | Box19 | 24 |
| 0% (zero-rated/export) | Box20 | -- |
| 0% (exempt) | Box21 | -- |

### Sales -- EU/Non-EU

| Location | Box |
|----------|-----|
| EU B2B | Box1 |
| Non-EU | Box2 |

---

## Step 3: Reverse Charge Mechanics [T1]

**Legislation:** VAT Act Cap. 406, Article 19 (reverse charge on intra-EU acquisitions); Article 20 (reverse charge on services from abroad).

For EU and non-EU purchases where supplier charged 0% VAT:
1. Report net amount in acquisition box (Box 9/9a/10/11)
2. Self-assess output VAT at 18% in Box 6/7
3. Claim input VAT at 18% in Box 13/13a/14/15
4. Net effect: zero for fully taxable businesses

**The VAT return must show BOTH sides (output and input) for reverse charge.**

### Exceptions to Reverse Charge
- Out-of-scope categories (wages, bank charges, dividends etc): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi, conference, car rental): NOT reverse charge, foreign VAT paid at source
- EU supplier charged their local VAT > 0%: NOT reverse charge, foreign VAT is part of expense

---

## Step 4: Deductibility Check

### Blocked Categories (10th Schedule, Malta VAT Act) [T1]
**Legislation:** VAT Act Cap. 406, 10th Schedule, Item 3.
These have ZERO VAT recovery regardless of anything else:
- Entertainment (Item 3(1)(b))
- Motor vehicles (Item 3(1)(a)(iv-v)) -- exception: taxi, delivery, car rental
- Tobacco (Item 3(1)(a)(i))
- Alcohol (Item 3(1)(a)(ii))
- Art/antiques (Item 3(1)(a)(iii))
- Pleasure craft (Item 3(1)(a)(iv))
- Personal use (Item 3(1)(c))

Blocked categories OVERRIDE partial exemption. Check blocked FIRST.

### Registration-Based Recovery [T1]
- Article 10: full recovery (subject to category rules)
- Article 11: NO recovery (enforced by trigger)
- Article 12: NO recovery

### Partial Exemption (Article 22(4)) [T2]
**Legislation:** VAT Act Cap. 406, Article 22(4).
If business makes both taxable and exempt supplies:
`Recovery % = (Taxable Supplies / Total Supplies) * 100`
**Flag for reviewer: pro-rata calculation must be confirmed by warranted accountant before applying. Annual adjustment may be required.**

---

## Step 5: Derived Box Calculations

```
Box 5  = Box 1 + Box 2 + Box 3 + Box 4
Box 8  = Box 6 + Box 7
Box 12 = Box 9 + Box 9a + Box 10 + Box 11
Box 16 = Box 13 + Box 13a + Box 14 + Box 15
Box 17 = Box 8 - Box 16
Box 22 = Box 18 + Box 18a + Box 18b + Box 19 + Box 20 + Box 21
Box 25 = Box 23 + Box 23a + Box 23b + Box 24
Box 26 = Box 17 + Box 25
Box 33 = Box 27 + Box 28 + Box 29 + Box 30 + Box 31 + Box 31a + Box 31b + Box 32
Box 39 = Box 34 + Box 35 + Box 36 + Box 37 + Box 37a + Box 37b + Box 38

IF Box 39 > Box 26 THEN
  Box 42 = (Box 39 - Box 26) + (Box 41 - Box 40)  -- Excess Credit
  Box 43 = 0
ELSE
  Box 42 = 0
  Box 43 = (Box 26 - Box 39) + (Box 40 - Box 41)  -- Tax Payable
END

Box 45 = Box 43 - Box 44  -- Net after B/F credit
```

---

## Step 6: Key Thresholds

| Threshold | Value |
|-----------|-------|
| Capital Goods Scheme | EUR 1,160 gross |
| Article 11 exemption | EUR 35,000 domestic turnover |
| EU goods (Art 12 trigger) | EUR 10,000/calendar year |
| EU services (Art 12 trigger) | Any amount (no threshold) |

---

## Step 7: Filing Deadlines

| Registration | Period | Deadline |
|-------------|--------|----------|
| Article 10 (e-filing) | Quarterly | 21st of month after quarter end |
| Article 10 (paper) | Quarterly | 14th of month after quarter end |
| Article 11 | Annual (Jan-Dec) | 15 March following year |
| Article 12 | Monthly | 15th of following month |

---

## Step 8: Article 11 Declaration (4-Box Form)

Article 11 clients file a simplified annual declaration, NOT the VAT3:

| Box | Description | Classification |
|-----|-------------|----------------|
| 1 | Sales of Goods | goods_sale |
| 2 | Provision of Services | services_sale |
| 3 | Purchases of stock for re-sale | resale_stock |
| 4 | Purchases of Capital Assets | capital_asset |

General expenses do NOT appear on the declaration (P&L only).
Article 11 clients CANNOT recover input VAT.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box -- it is 100% deterministic from facts
- NEVER classify items below EUR 1,160 as Capital Goods (Box 30/Box 10)
- NEVER apply reverse charge to out-of-scope categories
- NEVER apply reverse charge to local consumption services abroad
- NEVER allow Article 11/12 clients to claim input VAT
- NEVER confuse zero-rated (Box 20, input VAT deductible) with exempt without credit (Box 21, input VAT NOT deductible)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER confuse Article 11 4-box declaration with VAT3 structure
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 9: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Article 10 client pays for a hotel in Italy via credit card. Invoice shows Italian VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged and paid at source. Treat as overhead expense. No VAT boxes. Italian VAT is an irrecoverable cost embedded in the expense.
**Legislation:** VAT Act Cap. 406, Article 19(3) -- local consumption exclusion.

### EC2 -- Subscription software from non-EU provider (e.g. Google, AWS, Notion) [T1]
**Situation:** Monthly charge from a US company, no VAT shown on invoice.
**Resolution:** Reverse charge applies. Box 11 (net) / Box 15 (input VAT at 18%) / Box 4 (output VAT at 18%) / Box 7. Net effect zero for fully taxable Article 10 client.
**Legislation:** VAT Act Cap. 406, Article 20 (services received from outside Malta).

### EC3 -- Mixed invoice: goods + services from EU supplier [T1]
**Situation:** EU supplier invoice covers both physical goods and installation services.
**Resolution:** Split by line item. Physical goods go to Box 9 / Box 13. Services go to Box 9a / Box 13a. If line items are not broken out, [T2] flag for reviewer to confirm split with client.

### EC4 -- Motor vehicle expense [T1]
**Situation:** Client purchases or leases a car.
**Resolution:** Input VAT BLOCKED under 10th Schedule Item 3(1)(a)(iv-v). Exception only if the vehicle is used exclusively for: taxi services, driving instruction, car rental as a business activity, or hearse services. If client claims business-only use, [T2] flag for reviewer confirmation before allowing recovery.

### EC5 -- Airbnb / short-term rental income [T2]
**Situation:** Client earns income from renting a property short-term via Airbnb.
**Resolution:** Short-term rental (under 3 months) is a taxable supply for VAT purposes in Malta. Output VAT at 7% applies if Article 10 registered. However, if client is Article 11, this income counts toward the EUR 35,000 threshold. Flag for reviewer: confirm rental duration, Article classification, and whether the EUR 35,000 threshold has been breached across all income sources.
**Legislation:** VAT Act Cap. 406, 5th Schedule Part 2 (7% accommodation supplies).

### EC6 -- Client invoices EU customer, charges 0% VAT [T1]
**Situation:** Article 10 client provides services to an EU business (B2B) and invoices at 0%.
**Resolution:** This is an EU B2B service supply. Report net amount in Box 1. No output VAT. Customer accounts for reverse charge in their own jurisdiction. Confirm B2B status (customer must be VAT registered in their EU country). If customer is a private individual (B2C), [T2] flag for reviewer -- different place of supply rules may apply.

### EC7 -- Credit notes [T1]
**Situation:** Client receives a credit note from a supplier.
**Resolution:** Reverse the original entry. If original was Box 31 / Box 37, credit note reduces Box 31 / Box 37 by the credit note amount. Net figures are reported. Do not create a separate negative entry in a different box.

### EC8 -- VAT on imports (physical goods from Non-EU arriving in Malta) [T2]
**Situation:** Client imports physical goods from the US / UK / China etc.
**Resolution:** VAT on physical goods imports is collected by Malta Customs at the border, not via reverse charge on the VAT return. The VAT paid to Customs appears on the import entry (C88 document). This is recoverable input VAT but must be entered from the Customs document, not reverse charged. Flag for reviewer: confirm client has the C88 and that the amount matches.

### EC9 -- Fuel [T1]
**Situation:** Client purchases fuel.
**Resolution:** Fuel for business vehicles where the vehicle itself is not blocked is recoverable. Fuel for blocked motor vehicles (personal cars) is also blocked. Apply the same logic as the underlying vehicle. If vehicle category is uncertain, [T2] flag for reviewer.

### EC10 -- Director fees received [T1]
**Situation:** Self-employed client receives director fees from a company.
**Resolution:** Director fees are outside the scope of VAT (not a supply of services for VAT purposes under Maltese law). Do not include on VAT return. Report on income tax return only.

---

## Step 10: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to warranted accountant.

- **Self-employed chargeable income:** Revenue minus allowable deductions. Allowable deductions broadly follow trading expense principles.
- **Tax rates (2025):** Progressive bands 0% / 15% / 25% / 35%. Married and single rates differ.
- **15% flat rate option:** Available for certain categories of self-employed individuals with gross income below thresholds. Conditions apply.
- **SSC (Social Security Contributions):** Separate obligation under Cap. 318. Class 2 contributions for self-employed. Rates and ceilings change annually. Out of scope of this skill.
- **FSS / FS3 / FS5:** Employer obligations for employees. Entirely separate from VAT. See FSS skill (separate).

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Warranted accountant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to warranted accountant. Document gap.
```

---

## Step 12: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard local purchase, 18% VAT overhead
**Input:** Malta supplier, office supplies, gross EUR 236, VAT EUR 36, net EUR 200, not resale, Article 10 client.
**Expected output:** Box 31 = EUR 200, Box 37 = EUR 36. Input VAT recoverable in full.

### Test 2 -- EU software subscription, reverse charge
**Input:** US supplier (Notion), monthly fee USD 20 (~EUR 18), no VAT on invoice, Article 10 client.
**Expected output:** Box 11 = EUR 18, Box 15 = EUR 3.24 (18%), Box 4 = EUR 18, Box 7 = EUR 3.24. Net VAT effect = zero.

### Test 3 -- Capital goods purchase
**Input:** Malta supplier, laptop EUR 1,450 gross, VAT EUR 221 (18%), net EUR 1,229. Article 10 client.
**Expected output:** Box 30 = EUR 1,229, Box 36 = EUR 221. Capital goods threshold met (EUR 1,229 net > EUR 1,160 gross threshold -- note: apply gross amount test, EUR 1,450 >= EUR 1,160).

### Test 4 -- EU B2B sale, zero rated
**Input:** Article 10 client invoices German company EUR 500 for consulting, charges 0% VAT, German customer is VAT registered.
**Expected output:** Box 1 = EUR 500. No output VAT. No input VAT entries.

### Test 5 -- Article 11 client, purchase of capital asset
**Input:** Article 11 client purchases a desk for EUR 800.
**Expected output:** Article 11 declaration Box 4 = EUR 800. No VAT recovery. No VAT3 entry.

### Test 6 -- Motor vehicle, blocked
**Input:** Article 10 client purchases a private car, EUR 25,000, VAT EUR 3,814 (18%).
**Expected output:** Box 31 = EUR 21,186 (net), Box 37 = EUR 0. VAT BLOCKED under 10th Schedule. No input VAT recovery.

### Test 7 -- EU hotel, local consumption exception
**Input:** Article 10 client pays for hotel in France EUR 300 including French VAT EUR 40.
**Expected output:** No VAT return entry. Expense is EUR 300 gross including irrecoverable foreign VAT. Not reverse charge.

### Test 8 -- Reverse charge, both sides
**Input:** EU supplier (Irish company) provides legal services EUR 1,000, invoices at 0% VAT. Article 10 client.
**Expected output:** Box 9a = EUR 1,000 (acquisition, services), Box 13a = EUR 180 (input VAT 18%), Box 3 = EUR 1,000 (output base), Box 6 = EUR 180 (output VAT 18%). Net VAT = zero.

---

## Contribution Notes (For Non-Malta Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all box numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the capital goods threshold (EUR 1,160) with your jurisdiction's equivalent.
5. Replace the small enterprise exemption threshold (EUR 35,000) with your jurisdiction's equivalent.
6. Replace the EU country list with the list relevant to your jurisdiction's trading bloc, if applicable.
7. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
8. Have a warranted or licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a warranted practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
