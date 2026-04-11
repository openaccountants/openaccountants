---
name: brunei-tax
description: Use this skill whenever asked about Brunei Darussalam tax obligations, corporate tax, or the absence of VAT/GST. Trigger on phrases like "Brunei tax", "Brunei VAT", "Brunei GST", "corporate tax Brunei", "MOFE filing", or any request involving Brunei taxation. This skill clarifies that Brunei has NO VAT/GST and NO personal income tax, and covers the corporate income tax framework at 18.5%. ALWAYS read this skill before touching any Brunei tax-related work.
---

# Brunei Darussalam Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brunei Darussalam |
| Jurisdiction Code | BN |
| Primary Legislation | Income Tax Act (Chapter 35); Companies Income Tax Act (Chapter 97) |
| Supporting Legislation | Petroleum Income Tax Act; Stamp Act |
| Tax Authority | Revenue Division, Ministry of Finance and Economy (MOFE) |
| Filing Portal | MOFE Revenue Division offices |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: corporate tax rate, no VAT/GST, no personal income tax. Tier 2: petroleum tax, withholding tax. Tier 3: oil/gas PSAs, free trade zone operations. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Key Fact: NO VAT/GST in Brunei [T1]

**Brunei Darussalam does NOT impose any VAT, GST, sales tax, or consumption tax.**

There is:
- NO Value Added Tax (VAT)
- NO Goods and Services Tax (GST)
- NO sales tax
- NO service tax
- NO personal income tax
- NO capital gains tax
- NO payroll tax
- NO estate/inheritance tax

**This makes Brunei one of the few countries globally with no broad-based consumption tax and no personal income tax.**

---

## Step 1: Corporate Income Tax [T1]

**Legislation:** Companies Income Tax Act (Chapter 97).

### Rate
- **Standard corporate tax rate: 18.5%** on chargeable income
- Applies to all companies (resident and non-resident with Brunei-source income)

### Taxable Income
- Business profits derived in or from Brunei
- Rental income from property in Brunei
- Royalties and licence fees from Brunei sources
- Interest from Brunei sources

### Exempt Income
- Dividends received from companies already subject to Brunei tax
- Foreign-source income (generally not taxed if not remitted, subject to conditions)
- Income of approved enterprises under Pioneer Certificate

### Deductible Expenses [T1]
- Expenses wholly and exclusively incurred in the production of income
- Capital allowances on qualifying assets (initial and annual allowances)
- Bad debts (written off and proven irrecoverable)
- Interest on business loans
- Staff costs and contributions
- Repairs and maintenance

### Non-Deductible Expenses [T1]
- Private or personal expenses
- Capital expenditure (except via capital allowances)
- Entertainment (unless wholly for business promotion)
- Fines and penalties
- Donations (unless to approved institutions)
- Provisions (unless specific and proven)

---

## Step 2: Capital Allowances [T1]

**Legislation:** Companies Income Tax Act, Schedule.

| Asset Category | Initial Allowance | Annual Allowance |
|---------------|-------------------|------------------|
| Industrial buildings | 10% | 2% |
| Plant and machinery | 20% | 10% - 20% |
| Motor vehicles | 20% | 20% |
| Office equipment / furniture | 20% | 10% |
| Computer equipment | 20% | 20% - 40% |

---

## Step 3: Withholding Tax [T2]

**Legislation:** Companies Income Tax Act, Section 35.

| Payment Type | WHT Rate |
|-------------|----------|
| Royalties to non-residents | 10% |
| Technical/management fees to non-residents | 10% |
| Interest to non-residents | 2.5% |
| Rent of movable property to non-residents | 10% |

**Flag for reviewer: WHT rates may be reduced under Double Tax Agreements (DTAs). Brunei has DTAs with several countries. Check applicable treaty.**

---

## Step 4: Petroleum Income Tax [T3]

**Legislation:** Petroleum Income Tax Act.

- Petroleum companies operating under Production Sharing Agreements (PSAs) are subject to Petroleum Income Tax
- Rate: **55%** on petroleum income
- This is separate from the standard corporate tax
- Complex ring-fencing and cost recovery rules apply

**Do not classify petroleum income. Escalate to specialist.**

---

## Step 5: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Corporate tax rate | 18.5% |
| Petroleum tax rate | 55% |
| VAT/GST rate | N/A -- does not exist |
| Personal income tax rate | N/A -- does not exist |
| SME incentive (if applicable) | Per specific approval |

---

## Step 6: Filing Deadlines [T1]

| Category | Deadline |
|----------|----------|
| Corporate tax return | Within 6 months after end of financial year |
| Estimated tax payment | Per notice of assessment from MOFE |
| WHT remittance | Within 1 month of payment to non-resident |
| Financial year | Company chooses; most use calendar year |

---

## Step 7: Other Taxes and Levies [T1]

| Tax | Rate / Application |
|-----|-------------------|
| Stamp duty | Variable rates on documents (property transfers, shares) |
| Property tax | Based on annual value of property |
| Import duties | 0% - 30% depending on goods (no consumption tax) |
| Excise duties | On tobacco, alcohol, motor vehicles |

---

## PROHIBITIONS [T1]

- NEVER state that Brunei has VAT, GST, or any consumption tax -- it does not
- NEVER state that Brunei has personal income tax -- it does not
- NEVER apply VAT/GST concepts to Brunei transactions
- NEVER classify Brunei transactions into VAT boxes or GST categories
- NEVER confuse corporate income tax (18.5%) with consumption tax
- NEVER advise on petroleum tax without specialist involvement
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 8: Edge Case Registry

### EC1 -- Foreign company with Brunei branch [T2]
**Situation:** Foreign company operates a branch in Brunei.
**Resolution:** Branch is subject to corporate tax at 18.5% on Brunei-source income. No VAT obligations. WHT may apply on payments to head office. Flag for reviewer: confirm treaty application.

### EC2 -- Cross-border services to Brunei [T1]
**Situation:** Brunei company pays for services from Singapore provider.
**Resolution:** No VAT reverse charge (no VAT exists). WHT at 10% may apply if service is technical/management fee. Deductible for corporate tax if business-related.

### EC3 -- Online business in Brunei [T1]
**Situation:** E-commerce business operating from Brunei.
**Resolution:** Subject to corporate tax at 18.5% on profits. No VAT/GST to charge customers. No consumption tax filing required.

### EC4 -- Pioneer status enterprise [T2]
**Situation:** Company granted Pioneer Certificate.
**Resolution:** May receive tax holiday (reduced or zero corporate tax) for approved period. Conditions apply. Flag for reviewer: confirm Pioneer Certificate terms.

### EC5 -- Property rental income [T1]
**Situation:** Company earns rental income from Brunei property.
**Resolution:** Taxable at 18.5% corporate tax rate. Property tax also applies (separate obligation based on annual value). No VAT on rent.

### EC6 -- Employee remuneration [T1]
**Situation:** How is employee salary taxed?
**Resolution:** NO personal income tax in Brunei. Employees receive gross salary with no income tax deduction. Employer obligation: TAP (Tabung Amanah Pekerja / Employee Trust Fund) and SCP (Supplemental Contributory Pension) contributions.

---

## Step 9: Reviewer Escalation Protocol

When a [T2] situation is identified:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [most likely correct]
Action Required: Qualified accountant must confirm.
```

When a [T3] situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Refer to qualified accountant. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Corporate tax calculation
**Input:** Brunei company, chargeable income BND 1,000,000 for the year.
**Expected output:** Corporate tax at 18.5% = BND 185,000. No VAT/GST obligations.

### Test 2 -- No VAT on sales
**Input:** Brunei company sells goods locally for BND 50,000.
**Expected output:** No VAT/GST charged. No consumption tax return. Income subject to corporate tax only.

### Test 3 -- WHT on royalty payment
**Input:** Brunei company pays BND 100,000 royalty to UK company.
**Expected output:** WHT at 10% = BND 10,000. Remit within 1 month. Check UK-Brunei DTA for potential reduction.

### Test 4 -- Employee salary
**Input:** Employee earns BND 5,000/month.
**Expected output:** No income tax deduction. Employer contributes to TAP/SCP. Employee receives gross amount minus TAP/SCP employee share.

### Test 5 -- Import of goods
**Input:** Company imports machinery worth BND 200,000.
**Expected output:** Import duty at applicable rate (0-30%). No VAT/GST at customs. Capital allowance on machinery for corporate tax purposes.

### Test 6 -- Non-deductible expense
**Input:** Director's personal car expenses BND 20,000.
**Expected output:** Not deductible for corporate tax. No VAT implication (no VAT exists).

---

## Contribution Notes

This skill must be validated by a qualified accountant or tax advisor practicing in Brunei Darussalam before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Brunei.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
