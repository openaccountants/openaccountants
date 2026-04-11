---
name: nz-gst-return
description: Use this skill whenever asked about New Zealand GST returns for self-employed individuals. Trigger on phrases like "GST return", "GST101A", "GST rate NZ", "input tax", "output tax", "zero-rated", "GST registration", "taxable supply", or any question about GST filing for sole traders in New Zealand. Covers the 15% standard rate, zero-rated and exempt supplies, $60K registration threshold, invoice and payments basis, and GST101A return preparation. ALWAYS read this skill before touching any NZ GST work.
---

# NZ GST Return -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Goods and Services Tax Act 1985 (GSTA 1985) |
| Tax Authority | Inland Revenue (IR / Te Tari Taake) |
| Filing Portal | myIR (myir.ird.govt.nz) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a New Zealand chartered accountant (CA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: rate application, registration threshold, return computation, filing deadlines. Tier 2: mixed-use assets, second-hand goods, change of use adjustments. Tier 3: financial services, cross-border digital services, associated persons. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before preparing any GST return, you MUST know:

1. **GST registration status** [T1] -- registered or not; registration number
2. **Filing frequency** [T1] -- monthly, 2-monthly, or 6-monthly
3. **Accounting basis** [T1] -- invoice basis or payments (cash) basis
4. **Balance date** [T1] -- typically 31 March
5. **Nature of supplies** [T1] -- standard-rated (15%), zero-rated (0%), or exempt
6. **Total taxable supplies for the period** [T1]
7. **Total taxable purchases with GST invoices** [T1]

**If turnover is below $60,000 and client is not voluntarily registered, STOP. No GST filing required.**

---

## Step 1: Registration [T1]

**Legislation:** GSTA 1985, s 51

| Rule | Detail |
|------|--------|
| Mandatory registration | Taxable supplies exceed or are expected to exceed **$60,000** in any 12-month period |
| Voluntary registration | Any person making taxable supplies can register voluntarily |
| Minimum period | Must remain registered for at least 12 months once registered |
| Cancellation | Can deregister if supplies fall below $60,000 and not expected to exceed |

---

## Step 2: Rates and Supply Classification [T1]

**Legislation:** GSTA 1985, s 8, s 11, s 14

### GST Rate [T1]

| Rate | Application |
|------|------------|
| **15%** | Standard rate on all taxable supplies (since 1 October 2010) |
| **0%** | Zero-rated supplies |
| **Exempt** | No GST charged; no input tax claimable |

### Zero-Rated Supplies (0%) [T1]

| Category | Examples |
|----------|---------|
| Exports | Goods exported from NZ, services supplied to non-residents consumed offshore |
| Financial services (elected) | If provider has elected to zero-rate certain financial services |
| Going concern | Sale of a business as a going concern between registered persons |
| Residential land | Compulsory zero-rating on sales between registered persons |
| Fine metals | Gold, silver, platinum of certain fineness |

### Exempt Supplies [T1]

| Category | Examples |
|----------|---------|
| Financial services | Interest, loan fees, insurance premiums (unless zero-rated election) |
| Residential rent | Domestic rental accommodation |
| Donated goods and services | By non-profit bodies (under certain conditions) |

---

## Step 3: Accounting Basis [T1]

**Legislation:** GSTA 1985, s 19, s 19A

| Basis | Rule | Eligibility |
|-------|------|-------------|
| Invoice basis | Account for GST when invoice is issued or received | Default for all registered persons |
| Payments (cash) basis | Account for GST when payment is made or received | Taxable supplies < $2M in preceding 12 months |
| Hybrid basis | Invoice for sales, payments for purchases (or vice versa) | By application to IR |

---

## Step 4: GST101A Return -- Line-by-Line [T1]

**Form:** GST101A

| Box | Description | How to Populate |
|-----|-------------|-----------------|
| 5 | Total sales and income for the period | All income including GST-inclusive amounts, zero-rated, and exempt |
| 6 | Zero-rated supplies | Exports and other 0% supplies (included in Box 5) |
| 7 | Total purchases and expenses | All purchases including GST-inclusive, zero-rated, and exempt |
| 8 | GST on sales (output tax) | (Box 5 - Box 6 - exempt supplies) x 3/23 |
| 9 | GST on purchases (input tax) | (Box 7 - exempt purchases - private) x 3/23 |
| 10 | Adjustments -- increase | Prior period corrections that increase GST payable |
| 11 | Adjustments -- decrease | Prior period corrections that decrease GST payable |
| 12 | GST to pay or refund | Box 8 + Box 10 - Box 9 - Box 11 |

### The 3/23 Fraction [T1]

For GST-inclusive amounts at 15%, the tax fraction is 3/23 (i.e., 15/115 = 3/23).

---

## Step 5: Filing Frequency and Deadlines [T1]

**Legislation:** GSTA 1985, s 15, s 16

| Frequency | Eligibility | Deadline |
|-----------|-------------|----------|
| Six-monthly | Taxable supplies < $500,000 (can elect) | 28th of month after period end |
| Two-monthly | Default for most businesses | 28th of month after period end |
| Monthly | Taxable supplies > $24M or by election | 28th of month after period end |

### Two-Monthly Periods (Standard) [T1]

| Period | Months | Return Due |
|--------|--------|-----------|
| 1 | January -- February | 28 March |
| 2 | March -- April | 28 May |
| 3 | May -- June | 28 July |
| 4 | July -- August | 28 September |
| 5 | September -- October | 28 November |
| 6 | November -- December | 28 January |

---

## Step 6: Input Tax Rules [T1/T2]

**Legislation:** GSTA 1985, s 20, s 21

### Claimable Input Tax [T1]

Input tax is claimable on goods and services acquired for the principal purpose of making taxable supplies, if:
- The supply was made by a GST-registered person
- A valid tax invoice is held (for supplies over $50)
- The goods/services are used in the taxable activity

### Non-Claimable [T1]

| Item | Rule |
|------|------|
| Private or exempt use | No input tax credit |
| Entertainment (50% rule) | 50% of GST on entertainment is non-deductible |
| Motor vehicles (private use portion) | Apportion between business and private use [T2] |

### Change of Use Adjustments [T2]

If the proportion of taxable use changes, adjustments may be required. [T2] Flag for reviewer if mixed-use assets exceed $5,000.

---

## Step 7: Edge Case Registry

### EC1 -- Below $60K threshold but voluntarily registered [T1]
**Situation:** Freelancer earns $40,000 and is voluntarily GST-registered.
**Resolution:** Must continue filing GST returns and charging GST. Can deregister after 12 months of registration if supplies remain below $60,000. Must account for output tax on deregistration on assets held.

### EC2 -- Bad debts [T1]
**Situation:** Client issued invoice for $11,500 (incl. GST) but customer never paid.
**Resolution:** On invoice basis, output tax was already returned. After writing off the debt, claim a bad debt adjustment (Box 11) for the GST component: $11,500 x 3/23 = $1,500. Must have been written off as bad and been outstanding for at least 6 months.

### EC3 -- Private use of business asset [T2]
**Situation:** Laptop purchased for $2,300 (incl. GST), used 70% business, 30% private.
**Resolution:** Claim 70% of input tax: $2,300 x 3/23 x 70% = $210. [T2] Flag for reviewer on apportionment basis.

### EC4 -- Sale of a going concern [T1]
**Situation:** Client sells entire freelance business (equipment, client list, goodwill) to another registered person.
**Resolution:** Zero-rated (0%) if both parties are registered and the supply is of a going concern. No GST charged. Both parties must agree it is a going concern.

### EC5 -- Imported services (reverse charge) [T2]
**Situation:** Client purchases software subscription from a US company for $500/month.
**Resolution:** If the overseas supplier is not GST-registered in NZ and the client is registered, a reverse charge may apply. For most small self-employed, the overseas supplier now charges NZ GST on B2C digital services. [T2] Flag for reviewer if amounts are material.

### EC6 -- Late filing [T1]
**Situation:** GST return filed 3 months late.
**Resolution:** Late filing penalty of $250 applies. Interest on any unpaid GST from the original due date. Penalties increase for repeated late filing.

---

## Step 8: Test Suite

### Test 1 -- Standard two-monthly return
**Input:** Period Jan-Feb. Total sales (incl. GST) $23,000. Total purchases (incl. GST) $8,050. All standard-rated. No adjustments.
**Expected output:**
- Output tax: $23,000 x 3/23 = $3,000
- Input tax: $8,050 x 3/23 = $1,050
- GST payable: $3,000 - $1,050 = $1,950

### Test 2 -- Refund position (exporter)
**Input:** Total sales $50,000 (all zero-rated exports). Total purchases (incl. GST) $17,250.
**Expected output:**
- Output tax: $0 (zero-rated)
- Input tax: $17,250 x 3/23 = $2,250
- GST refund: $2,250

### Test 3 -- Mixed supplies with exempt income
**Input:** Total sales $34,500 (incl. GST) of which $11,500 is exempt (financial services). Purchases $11,500 (incl. GST, all for taxable activity).
**Expected output:**
- Taxable sales: $34,500 - $11,500 = $23,000
- Output tax: $23,000 x 3/23 = $3,000
- Input tax: $11,500 x 3/23 = $1,500 (but must apportion if purchases relate to both taxable and exempt)
- [T2] Apportionment needed -- flag for reviewer

### Test 4 -- Entertainment adjustment
**Input:** Business dinner $460 (incl. GST).
**Expected output:**
- GST content: $460 x 3/23 = $60
- Claimable: 50% x $60 = $30
- Non-claimable: $30

### Test 5 -- Below threshold, not registered
**Input:** Freelancer with $45,000 annual turnover, not registered.
**Expected output:** No GST obligations. Cannot charge GST. Cannot claim input tax.

---

## PROHIBITIONS

- NEVER charge GST if the person is not GST-registered
- NEVER claim input tax on private expenditure
- NEVER claim full input tax on entertainment -- the 50% restriction applies
- NEVER use a tax fraction other than 3/23 for the 15% rate
- NEVER allow a going concern zero-rating unless both parties are registered
- NEVER ignore the accounting basis -- invoice vs payments basis changes when GST is accounted for
- NEVER omit exempt supplies from Box 5 (total sales) -- they are included in total but excluded from GST calculation
- NEVER present calculations as definitive -- always label as estimated and direct client to IR or a qualified NZ chartered accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
