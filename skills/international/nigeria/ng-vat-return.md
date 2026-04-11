---
name: ng-vat-return
description: Use this skill whenever asked about Nigerian VAT returns for self-employed individuals. Trigger on phrases like "Nigeria VAT", "FIRS VAT", "7.5% VAT", "VAT return Nigeria", "value added tax Nigeria", "VAT filing Nigeria", or any question about VAT computation or filing for businesses in Nigeria. Covers the 7.5% standard rate, exempt supplies, registration requirements, monthly filing to FIRS, and input/output VAT computation. ALWAYS read this skill before touching any Nigerian VAT work.
---

# Nigeria VAT Return -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Nigeria |
| Jurisdiction Code | NG |
| Primary Legislation | Value Added Tax Act (VATA), Cap V1 LFN 2004, as amended by Finance Act 2020 |
| Supporting Legislation | Finance Act 2021, 2023; FIRS Regulations |
| Tax Authority | Federal Inland Revenue Service (FIRS) |
| Filing Portal | TaxPro Max (taxpromax.firs.gov.ng) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Nigerian chartered accountant |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: rate application, exempt list, return computation, filing deadlines. Tier 2: mixed supplies, non-resident digital services. Tier 3: international VAT recovery, transfer pricing implications. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before preparing any VAT return, you MUST know:

1. **VAT registration status** [T1] -- registered with FIRS; TIN
2. **Nature of supplies** [T1] -- standard-rated (7.5%), zero-rated, or exempt
3. **Monthly turnover** [T1] -- for threshold assessment
4. **Input VAT on purchases** [T1] -- with valid VAT invoices
5. **Whether any supplies are to government (WHT-VAT)** [T1]
6. **Whether client imports goods or services** [T2]

**Registration threshold:** Businesses with annual turnover of NGN 25,000,000 or less are exempt from VAT obligations (Finance Act 2020). If below threshold, STOP.

---

## Step 1: Registration [T1]

**Legislation:** VATA, s 8, as amended by Finance Act 2020

| Rule | Detail |
|------|--------|
| Mandatory registration | Taxable persons with turnover exceeding **NGN 25,000,000** per year |
| Exemption | Businesses with turnover <= NGN 25M are exempt from VAT registration and filing |
| Registration | Via TaxPro Max with FIRS |
| Timeline | Within 6 months of commencing business (if above threshold) |

---

## Step 2: Rates and Supply Classification [T1]

**Legislation:** VATA, s 2, First Schedule, as amended by Finance Act 2020

### VAT Rate [T1]

| Rate | Application |
|------|------------|
| **7.5%** | Standard rate on all taxable supplies (effective February 1, 2020) |
| **0%** | Zero-rated supplies (exports, certain humanitarian goods) |
| **Exempt** | Exempt supplies (First Schedule) |

### Exempt Supplies [T1]

| Category | Examples |
|----------|---------|
| Basic food items | Beans, yam, vegetables, fruits, cereals, fish, meat, poultry, milk, salt, cooking oil (raw/unprocessed) |
| Medical and pharmaceutical | Drugs, medical equipment, baby products |
| Educational | Books, newspapers, magazines, educational materials |
| Agricultural | Farm machinery, fertilizers, seeds, pesticides |
| Financial | Interest, commissions on lending |
| Real estate | Rent on residential property |
| Transportation | Public transport (mass transit) |

### Zero-Rated Supplies [T1]

| Category | Examples |
|----------|---------|
| Exports | Goods exported from Nigeria |
| Diplomatic supplies | Goods for foreign missions |
| Humanitarian | Supplies to humanitarian donor-funded projects |

---

## Step 3: VAT Invoice Requirements [T1]

**Legislation:** VATA, s 10

| Requirement | Detail |
|-------------|--------|
| VAT invoice must show | Supplier name, TIN, description of goods/services, quantity, price exclusive of VAT, VAT amount, total, date, sequential number |
| Retention | 5 years minimum |
| Input VAT claim | Only valid with a proper VAT invoice |

---

## Step 4: VAT Return Computation [T1]

| Step | Action |
|------|--------|
| 4.1 | Total standard-rated output supplies (exclusive of VAT) |
| 4.2 | Output VAT = Standard-rated supplies x 7.5% |
| 4.3 | Total exempt supplies (reported, no VAT) |
| 4.4 | Total zero-rated supplies (reported, 0% VAT) |
| 4.5 | Total input VAT on purchases (from valid VAT invoices) |
| 4.6 | Input VAT restriction: no credit for input VAT on exempt supplies [T2 for mixed] |
| 4.7 | Net VAT = Output VAT - Allowable input VAT |
| 4.8 | VAT payable to FIRS |

### Input Tax Restriction [T1]

- Input VAT is ONLY claimable on goods and services used for making taxable supplies
- No input VAT credit on exempt supplies
- [T2] If mixed taxable/exempt: apportion input VAT based on revenue ratio

---

## Step 5: Filing and Payment [T1]

**Legislation:** VATA, s 15

| Item | Detail |
|------|--------|
| Filing frequency | **Monthly** |
| Filing deadline | **21st of the following month** |
| Payment deadline | Same as filing deadline |
| Filing method | TaxPro Max (taxpromax.firs.gov.ng) |
| Nil returns | Must be filed even if no transactions |
| Currency | Nigerian Naira (NGN) |

---

## Step 6: Self-Accounting for Non-Resident Supplies [T2]

**Legislation:** VATA, s 10A (Finance Act 2020)

| Rule | Detail |
|------|--------|
| Digital services | Non-resident suppliers of digital services to Nigerian consumers must register and charge VAT |
| Self-accounting | If non-resident does not charge VAT, the Nigerian recipient may be required to self-account |
| Significant economic presence | Non-residents with significant economic presence in Nigeria may be deemed to have a taxable presence |

[T2] Flag for reviewer when client purchases services from non-residents.

---

## Step 7: Penalties [T1]

**Legislation:** VATA, s 16-18

| Offence | Penalty |
|---------|---------|
| Failure to register | NGN 50,000 for first month + NGN 25,000 per subsequent month |
| Late filing of return | 5% of tax due per month + NGN 50,000 |
| Late payment | 5% of amount due + interest at CBN MPR |
| Failure to issue VAT invoice | NGN 50,000 per offence |
| Failure to collect VAT | 150% of the uncollected amount + 5% interest per annum |

---

## Step 8: Edge Case Registry

### EC1 -- Turnover below NGN 25M threshold [T1]
**Situation:** Freelancer earns NGN 20,000,000 per year.
**Resolution:** Below the NGN 25M VAT threshold. Not required to register for VAT, charge VAT, or file VAT returns. Cannot claim input VAT.

### EC2 -- Mixed exempt and taxable supplies [T2]
**Situation:** Business sells both exempt food items and taxable consulting services.
**Resolution:** Output VAT only on consulting. Input VAT must be apportioned. Directly attributable input VAT follows its supply. Residual input is apportioned by revenue ratio. [T2] Flag for reviewer.

### EC3 -- Client charges VAT on exempt supply [T1]
**Situation:** Client charged 7.5% VAT on residential rent.
**Resolution:** INCORRECT. Residential rent is exempt. VAT should not have been charged. Client must issue credit note and refund the VAT to tenant. The incorrectly charged VAT is still owed to FIRS if collected.

### EC4 -- Foreign currency invoicing [T2]
**Situation:** Consultant invoices in USD.
**Resolution:** VAT must be computed in NGN. Use CBN exchange rate on the date of supply. [T2] Flag for reviewer on exchange rate source and date.

### EC5 -- Input VAT on capital assets [T1]
**Situation:** Business purchases computer equipment for NGN 2,000,000 + VAT.
**Resolution:** Input VAT of NGN 150,000 (7.5% x 2,000,000) is claimable in the period of purchase if the asset is used for making taxable supplies.

### EC6 -- Excess input VAT (refund) [T1]
**Situation:** Exporter has output VAT of NGN 0 and input VAT of NGN 500,000.
**Resolution:** Excess input VAT can be carried forward or a refund claim filed with FIRS. In practice, refunds are slow. Carry forward is more common.

---

## Step 9: Test Suite

### Test 1 -- Standard monthly return
**Input:** Taxable supplies NGN 5,000,000. Input VAT from purchases NGN 150,000.
**Expected output:**
- Output VAT: 5,000,000 x 7.5% = NGN 375,000
- Input VAT: NGN 150,000
- VAT payable: 375,000 - 150,000 = NGN 225,000

### Test 2 -- Exporter (refund position)
**Input:** Zero-rated exports NGN 10,000,000. Input VAT NGN 300,000.
**Expected output:**
- Output VAT: NGN 0
- Input VAT: NGN 300,000
- Refund/carry forward: NGN 300,000

### Test 3 -- Below threshold
**Input:** Annual turnover NGN 20,000,000.
**Expected output:** Not required to register. No VAT return filing obligation.

### Test 4 -- Mixed supplies
**Input:** Taxable supplies NGN 3,000,000, exempt supplies NGN 2,000,000. Total input VAT NGN 200,000 (none directly attributable).
**Expected output:**
- Taxable ratio: 3,000,000 / 5,000,000 = 60%
- Claimable input: 200,000 x 60% = NGN 120,000
- Output VAT: 3,000,000 x 7.5% = NGN 225,000
- VAT payable: 225,000 - 120,000 = NGN 105,000

### Test 5 -- Nil return
**Input:** No supplies or purchases in the month.
**Expected output:** File nil return by the 21st. VAT payable = NGN 0.

---

## PROHIBITIONS

- NEVER charge VAT on exempt supplies (basic food, medical, education, residential rent)
- NEVER claim input VAT without a valid VAT invoice
- NEVER require VAT registration for businesses below NGN 25,000,000 annual turnover
- NEVER apply a VAT rate other than 7.5% (the pre-2020 rate of 5% is no longer applicable)
- NEVER miss the 21st monthly filing deadline -- nil returns are still required
- NEVER claim input VAT on purchases used for exempt supplies
- NEVER ignore self-accounting obligations on imported services from non-residents
- NEVER present calculations as definitive -- always label as estimated and direct client to ICAN/ANAN member

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant (FCA/ACA) or accredited tax practitioner in Nigeria) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
