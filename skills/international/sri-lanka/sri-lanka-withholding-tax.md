---
name: sri-lanka-withholding-tax
description: ALWAYS read this skill before touching any Sri Lanka withholding tax / Advance Income Tax (AIT) work. Use whenever asked to compute, deduct, or reconcile Sri Lanka WHT/AIT on interest, dividends, rent, service fees, royalties, or payments to non-residents under the Inland Revenue Act No. 24 of 2017 as amended by Act No. 02 of 2025. Trigger on phrases like "Sri Lanka WHT", "Sri Lanka AIT", "advance income tax Sri Lanka", "interest WHT Sri Lanka 10%", "dividend WHT Sri Lanka", "rent WHT Sri Lanka", "non-resident WHT Sri Lanka", "SEC/2025/E circular", or "withholding certificate Sri Lanka". Out of scope — personal income tax computation (separate skill), corporate income tax (separate skill), SSCL, VAT, and APIT/PAYE on employment (covered by the income-tax / payroll skills).
jurisdiction: LK
domain: international
tax_year: 2025
reviewed_by: Lal kumarasiri
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sri-lanka-withholding-tax

## Sri Lanka — Withholding Tax / Advance Income Tax (AIT) — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com).** Research-grade (tier 2), drafted from official IRD sources for YA 2025/26 — pending sign-off by a Sri Lankan CA / IRD-registered practitioner. Not tax advice.

## Section 1 — Quick reference (rate table, effective 1 April 2025)

**Rate table (payment type / rate / notes)**  _(IRD Circulars SEC/2025/E/02 & E/03)_

| Payment type | Rate | Notes |
| --- | --- | --- |
| **Interest or discount** | **10%** | Raised from 5% effective 1 April 2025 (IRD Circulars SEC/2025/E/02 & E/03). Resident individuals may self-declare for relief where assessable income does not exceed the LKR 1,800,000 relief |
| **Dividends** | **15%** | Resident companies distributing dividends |
| **Resident rent** | **10%** | Where rent exceeds LKR 100,000 per calendar month |
| **Resident service fees** | **5%** | Independent professional service fees, aggregate over LKR 100,000/month |
| **Royalties** | **14%** |  |
| **Non-resident rent / service fees / insurance premiums** | **14%** | Single non-resident bucket |

- ****Interest or discount**** — **10%**  _(Raised from 5% effective 1 April 2025 (IRD Circulars SEC/2025/E/02 & E/03). Resident individuals may self-declare for relief where assessable income does not exceed the LKR 1,800,000 relief)_
- ****Dividends**** — **15%**  _(Resident companies distributing dividends)_
- ****Resident rent**** — **10%**  _(Where rent exceeds LKR 100,000 per calendar month)_
- ****Resident service fees**** — **5%**  _(Independent professional service fees, aggregate over LKR 100,000/month)_
- ****Royalties**** — **14%**
- ****Non-resident rent / service fees / insurance premiums**** — **14%**  _(Single non-resident bucket)_

**Field / Value table**

| Field | Value |
| --- | --- |
| Country / authority | Sri Lanka — Inland Revenue Department (IRD) |
| Currency | LKR |
| Statute | Inland Revenue Act No. 24 of 2017, as amended by Act No. 02 of 2025 (eff. 1 April 2025) |
| Year of assessment | 1 April – 31 March |
| Mechanism | AIT (Advance Income Tax) deducted at source by the payer; creditable against the recipient's income tax |
| Validated by | Pending — Sri Lankan CA / IRD-registered practitioner |
| Skill version | 1.0 |

- **Country / authority** — Sri Lanka — Inland Revenue Department (IRD)
- **Currency** — LKR
- **Statute** — Inland Revenue Act No. 24 of 2017, as amended by Act No. 02 of 2025 (eff. 1 April 2025)
- **Year of assessment** — 1 April – 31 March
- **Mechanism** — AIT (Advance Income Tax) deducted at source by the payer; creditable against the recipient's income tax
- **Validated by** — Pending — Sri Lankan CA / IRD-registered practitioner
- **Skill version** — 1.0

### Conservative defaults

**Conservative defaults (ambiguity table)**

| Ambiguity | Default |
| --- | --- |
| Payment type unclear | Apply the rate for the most specific matching category; if still unclear, flag |
| Resident vs non-resident recipient unconfirmed | Treat as non-resident (14%) and flag |
| Rent/service-fee monthly threshold borderline | Apply WHT if aggregate exceeds LKR 100,000/month |
| Self-declaration for interest relief claimed | Require the recipient's declaration on file; else withhold 10% |

- **Payment type unclear** — Apply the rate for the most specific matching category; if still unclear, flag
- **Resident vs non-resident recipient unconfirmed** — Treat as non-resident (14%) and flag
- **Rent/service-fee monthly threshold borderline** — Apply WHT if aggregate exceeds LKR 100,000/month
- **Self-declaration for interest relief claimed** — Require the recipient's declaration on file; else withhold 10%

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Payer identity & TIN; recipient legal name, TIN, and **residency status**; nature of payment (interest, dividend, rent, service fee, royalty); gross amount and period; any self-declaration for relief (interest); for non-residents, treaty residence certificate where treaty relief is claimed.

### Refusal catalogue

- **R-LK-WHT-1 — APIT / PAYE on employment** — Employment withholding is APIT, not this AIT regime — use `sri-lanka-income-tax` / `sri-lanka-payroll`.  _(R-LK-WHT-1)_
- **R-LK-WHT-2 — Treaty rate claim without a residence certificate** — Apply the statutory non-resident rate; do not apply a treaty cap without the certificate. Escalate treaty analysis.  _(R-LK-WHT-2)_
- **R-LK-WHT-3 — Sector special regimes (banking, insurance, capital markets)** — Out of scope — escalate.  _(R-LK-WHT-3)_
- **R-LK-WHT-4 — VAT / SSCL withholding** — Different regimes — use `sri-lanka-vat` / `sri-lanka-sscl`.  _(R-LK-WHT-4)_

## Section 3 — Tier 1 rules

### 3.1 Interest or discount — 10%

- **Interest or discount** — 10%  _(IRD tax chart YA 2025/26; PN/IT/2025-01; IRD Circulars SEC/2025/E/02 and SEC/2025/E/03)_
- **Interest/discount deduction and self-declaration relief** — Deduct 10% on interest or discount paid (raised from 5% effective 1 April 2025). A resident individual whose assessable income does not exceed the LKR 1,800,000 personal relief may self-declare to the payer to reduce/avoid the deduction — require the declaration on file.  _(IRD tax chart YA 2025/26; PN/IT/2025-01; IRD Circulars SEC/2025/E/02 and SEC/2025/E/03)_

### 3.2 Dividends — 15%

- **Dividends** — 15%  _(Section 3.2 Dividends — 15%)_

### 3.3 Resident rent — 10%

- **Resident rent** — 10%  _(Section 3.3 Resident rent — 10%)_
- **Resident rent monthly threshold** — LKR 100,000 per calendar month  _(Section 3.3 Resident rent — 10%)_

### 3.4 Resident service fees — 5%

- **Resident service fees** — 5%  _(Section 3.4 Resident service fees — 5%)_
- **Resident service fee aggregate threshold** — LKR 100,000 per month aggregate  _(Section 3.4 Resident service fees — 5%)_

### 3.5 Royalties — 14%

- **Royalties** — 14%  _(Section 3.5 Royalties — 14%)_

### 3.6 Non-residents — 14%

- **Non-resident rent, service fees, insurance premiums** — 14%  _(Section 3.6 Non-residents — 14%)_
- **Non-resident treaty cap condition** — Subject to any applicable double-tax treaty cap, which requires a residence certificate.  _(Section 3.6 Non-residents — 14%)_

## Section 4 — Tier 2

- **Credit / final tax** — AIT deducted is generally creditable against the recipient's income tax. Whether a given deduction is creditable vs final depends on the recipient and payment type — VERIFY per the IRA for each stream.
- **Self-declaration mechanics (interest)** — The relief self-declaration is recipient-specific and time-bound; the payer must hold it before applying a reduced/zero deduction.
- **Treaty relief** — Reduced rates for non-residents require a tax-residence certificate and beneficial-ownership confirmation — escalate.

## Section 5 — Worked examples

### 5.1 Interest paid to a resident company

- **AIT on interest to resident company** — AIT = 10% × 1,000,000 = LKR 100,000 withheld and remitted; recipient credits it.  _(Section 5.1 Interest paid to a resident company)_

### 5.2 Resident rent above threshold

- **AIT on resident rent above threshold** — Company pays LKR 150,000/month rent to a resident landlord (> LKR 100,000) → AIT = 10% × 150,000 = LKR 15,000/month.  _(Section 5.2 Resident rent above threshold)_

### 5.3 Service fee to a non-resident consultant

- **AIT on service fee to non-resident consultant** — Payment LKR 2,000,000 to a non-resident for services → AIT = 14% × 2,000,000 = LKR 280,000 (subject to any treaty cap with a residence certificate).  _(Section 5.3 Service fee to a non-resident consultant)_

## Section 6 — Filing and payment

- **Deduction and remittance mechanics** — AIT is deducted at the time of payment and remitted to the IRD, with a withholding certificate issued to the recipient.

Remittance and statement due dates — VERIFY against the current IRD WHT/AIT schedule (not asserted here).

## Section 7 — Conservative defaults

**Conservative defaults (situation table)**

| Situation | Default |
| --- | --- |
| Residency unconfirmed | Non-resident 14%; flag |
| Interest self-declaration not on file | Withhold 10% |
| Treaty cap claimed without certificate | Apply statutory rate |
| Payment-type ambiguity | Most specific category; flag |
| Any figure flagged VERIFY | Flag for reviewer |

- **Residency unconfirmed** — Non-resident 14%; flag
- **Interest self-declaration not on file** — Withhold 10%
- **Treaty cap claimed without certificate** — Apply statutory rate
- **Payment-type ambiguity** — Most specific category; flag
- **Any figure flagged VERIFY** — Flag for reviewer

## Section 8 — Sources

1. IRD YA 2025/26 tax chart — https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx
2. IRD Notice PN/IT/2025-01 (26.03.2025) — https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/666/PN_IT_2025-01_26032025_E.pdf
3. IRD Circular SEC/2025/E/02 — https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2025_E_02_E.pdf
4. IRD Circular SEC/2025/E/03 — https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2025_E_03_e.pdf

**Known gaps / VERIFY:** creditable-vs-final characterisation per stream; AIT remittance and statement due dates; full treaty-rate schedule.

## Prohibitions

- NEVER apply the old 5% interest rate for periods from 1 April 2025 — it is 10%.
- NEVER apply a treaty-reduced non-resident rate without a tax-residence certificate.
- NEVER skip WHT on resident rent over LKR 100,000/month or resident professional service fees over LKR 100,000/month aggregate.
- NEVER assert remittance/statement dates this skill flags as VERIFY.
- NEVER file or instruct filing — produce a working paper for practitioner review.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Sri Lankan professional (CA / IRD-registered tax practitioner) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. To speak with a licensed accountant who verifies skills for your jurisdiction — **no liability until both parties sign an engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**
