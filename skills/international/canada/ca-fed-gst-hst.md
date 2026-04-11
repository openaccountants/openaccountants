---
name: ca-fed-gst-hst
description: >
  Canadian GST/HST return (GST34) for self-employed sole proprietors. Covers GST (5%) and HST rates by province, input tax credits (ITCs), quick method of accounting, annual vs quarterly filing, small supplier threshold ($30K), and place-of-supply rules. Complements canada-gst-hst.md which provides the full GST/HST framework.
version: 1.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - gst-workflow-base
related:
  - canada-gst-hst.md
---

# Canada GST/HST Return (GST34) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return — complementary to `canada-gst-hst.md`
**Status:** Complete

This file focuses on the practical GST34 return preparation for sole proprietors, including line-by-line guidance. For the broader GST/HST framework (rates, registration, supply classification), see `canada-gst-hst.md` in this directory.

**Tax year coverage.** This skill targets **fiscal periods ending in 2025**.

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **Forms:** GST34 (GST/HST Return for Registrants)
- **Entity types:** Sole proprietors and self-employed individuals registered for GST/HST
- Line-by-line computation for the GST34
- Quick method of accounting
- Annual information return (GST62)
- Rebates and adjustments

This skill does NOT cover:

- Partnerships, corporations, or non-profit organisations
- GST/HST new housing rebates
- Selected listed financial institutions
- Detailed provincial sales tax (PST/RST/QST) — see provincial skills

---

## Section 2 — Filing requirements

### 2.1 Registration threshold (small supplier)

| Category | Threshold | Source |
|----------|-----------|--------|
| Most businesses | $30,000 in taxable supplies in any single calendar quarter or in the last four consecutive calendar quarters | ETA s 148(1) |
| Taxi / ride-sharing | $0 — must register from the first ride | ETA s 240(1.1) |
| Non-resident digital services | $30,000 over 12 months (simplified registration) | ETA s 211.1 |

Once the threshold is exceeded, the person must register within 29 days. Source: ETA s 240(1).

### 2.2 Reporting periods

| Annual taxable supplies | Default period | Can elect |
|------------------------|----------------|-----------|
| <= $1.5M | Annual | Monthly or quarterly |
| $1.5M to $6M | Quarterly | Monthly or annual |
| > $6M | Monthly | N/A |

Source: ETA s 245, 246, 247.

### 2.3 Filing due dates

| Reporting period | Due date | Source |
|------------------|----------|--------|
| Monthly / quarterly | 1 month after the end of the reporting period | ETA s 238(1) |
| Annual (individual) | 15 June of the following year (if individual with Dec 31 fiscal year-end) | ETA s 238(2) |
| Annual (corporation) | 3 months after fiscal year-end | ETA s 238(2) |

**Payment due date for annual filers (individuals):** 30 April of the following year (even though the return is due 15 June). Quarterly instalment payments of net tax are required if net tax for the prior year exceeded $3,000. Source: ETA s 237.

---

## Section 3 — Rates and thresholds

| Province / Territory | Rate | Type | Source |
|---------------------|------|------|--------|
| Alberta, BC, Saskatchewan, Manitoba, Yukon, NWT, Nunavut | 5% | GST | ETA s 165(1) |
| Ontario | 13% | HST | ETA Sch VIII |
| New Brunswick | 15% | HST | ETA Sch VIII |
| Newfoundland and Labrador | 15% | HST | ETA Sch VIII |
| Nova Scotia | 15% | HST | ETA Sch VIII |
| Prince Edward Island | 15% | HST | ETA Sch VIII |

Note: British Columbia, Saskatchewan, and Manitoba charge GST (5%) federally plus their own provincial sales tax (PST) administered separately.

### 3.1 Quick method rates (2025)

| Type of business | Rate on GST supplies | Rate on HST supplies (ON 13%) | Source |
|-----------------|---------------------|-------------------------------|--------|
| Service providers (reselling < 40%) | 3.6% | 8.8% | ETA s 227, CRA guide RC4058 |
| Goods purchasers for resale (reselling >= 40%) | 1.8% | 4.4% | ETA s 227, CRA guide RC4058 |

Quick method eligibility: annual taxable supplies (incl. associates) <= $400,000. Not available for accounting, legal, financial consulting, or tax return preparation services. Source: ETA s 227(2).

---

## Section 4 — Computation rules

### 4.1 Regular method — GST34 line by line

**Line 101 — Total revenue:** Total taxable supplies made during the period (excluding GST/HST collected). Include zero-rated supplies. Exclude exempt supplies.

**Line 103 — GST/HST collected or collectible:** Total GST/HST charged on taxable supplies.

**Line 104 — Adjustments to Line 103:** Add: GST/HST on benefits to employees, bad debts recovered, change-in-use adjustments. Subtract: Bad debt write-offs (GST/HST portion), returned goods.

**Line 105 — Total GST/HST and adjustments:** = Line 103 + Line 104.

**Line 106 — Input tax credits (ITCs):** GST/HST paid on business purchases that qualify for ITCs.

ITC eligibility (all four conditions must be met):
1. The registrant acquired the property/service for use in commercial activities (ETA s 169(1))
2. The GST/HST was paid or became payable
3. The registrant has supporting documentation (invoice with supplier name, GST/HST number, amount of tax)
4. The ITC is claimed within 4 years (for most small businesses) — ETA s 225(4)

**Line 107 — Adjustments to Line 106:** Adjustments for recaptured ITCs (e.g., ON and PEI for large businesses on certain expenses — being phased out for ON), change-in-use.

**Line 108 — Total ITCs and adjustments:** = Line 106 + Line 107.

**Line 109 — Net tax:** = Line 105 - Line 108. If positive, amount is payable. If negative, the registrant may claim a refund.

**Lines 110-113 — Instalment credits and other payments:** Subtract any instalment payments already made during the period.

**Line 114 — Net amount payable or refundable.**

### 4.2 Quick method computation

**Step 1.** Calculate total revenue from taxable supplies (including GST/HST collected). This is the "GST/HST-included" amount.

**Step 2.** Apply the quick method remittance rate to the GST/HST-included revenue:
```
Remittance = (Revenue including GST/HST) x quick method rate
```

**Step 3.** Subtract 1% credit on the first $30,000 of eligible supplies (GST/HST-included) per fiscal year.

**Step 4.** ITCs are NOT claimed on most purchases under the quick method. Exception: ITCs may still be claimed on capital property purchases (cost > $30,000 before tax).

**Step 5.** The difference between GST/HST collected and the amount remitted is revenue to the registrant (included in business income on the T2125).

#### Worked example — quick method (service provider, ON 13%)

| Item | Amount |
|------|--------|
| Taxable supplies (excl HST) | $80,000 |
| HST collected (13%) | $10,400 |
| Total revenue incl HST | $90,400 |
| Quick method rate | 8.8% |
| Remittance = $90,400 x 8.8% | $7,955 |
| Less: 1% credit on first $30,000 = $300 | ($300) |
| Net remittance | $7,655 |
| Income pickup = $10,400 - $7,655 | $2,745 |

### 4.3 Quarterly instalment requirements for annual filers

Annual filers with net tax > $3,000 in the prior year must make quarterly instalment payments.

**Step 1.** Calculate 1/4 of the prior year net tax.

**Step 2.** Pay by the instalment due dates: last day of each fiscal quarter.

**Step 3.** Instalment interest is charged if payments are late or insufficient. Rate = prescribed CRA rate compounded daily.

---

## Section 5 — Edge cases and special rules

### 5.1 Place of supply for services

For determining whether GST or HST applies:
- Services performed at a specific location: place of supply = province where performed
- Services not tied to a location (e.g., consulting): place of supply = province of the recipient's business address
- Source: Place of Supply (GST/HST) Regulations SOR/2010-117

### 5.2 Zero-rated supplies

Included in Line 101 revenue but no GST/HST is charged. The registrant can still claim ITCs on inputs. Common zero-rated supplies: basic groceries, prescription drugs, medical devices, exports, certain agricultural products. Source: ETA Sch VI.

### 5.3 Exempt supplies

Excluded from Line 101 taxable revenue. No ITCs claimable on inputs used to make exempt supplies. Common exempt supplies: most health care, educational services, financial services, residential rent, most supplies by charities. Source: ETA Sch V.

### 5.4 Mixed-use (personal and business)

If a purchase is used partly for business and partly for personal purposes, only the business-use percentage of the GST/HST qualifies for ITCs. Maintain records of the apportionment.

### 5.5 Ceasing registration

When a sole proprietor ceases commercial activity, they must file a final return covering the period up to the cancellation date and account for any deemed disposition of business assets. Source: ETA s 171.

### 5.6 Digital products and non-resident suppliers

Non-resident suppliers of digital services to Canadian consumers must register under the simplified registration system and charge GST/HST (5% or the applicable HST rate). Source: ETA Div II.1.

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] Registration status confirmed (small supplier threshold checked)
- [ ] Correct HST rate applied based on place of supply
- [ ] All taxable supplies included in Line 101 / Line 103
- [ ] Exempt supplies excluded from taxable revenue
- [ ] Zero-rated supplies included in revenue but at 0% tax
- [ ] ITCs supported by documentation meeting the four conditions
- [ ] Quick method eligibility verified if used ($400K threshold, excluded professions)
- [ ] Quick method 1% credit on first $30,000 applied
- [ ] Instalment requirements checked for annual filers (> $3,000 threshold)
- [ ] Filing due date correctly identified (monthly/quarterly/annual)
- [ ] Rates and thresholds match 2025 fiscal period
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
