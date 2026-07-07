---
name: sri-lanka-sscl
description: ALWAYS read this skill before touching any Sri Lanka Social Security Contribution Levy (SSCL) work. Use whenever asked about SSCL on turnover for importers, manufacturers, service providers, wholesalers/retailers, or financial-service businesses in Sri Lanka. Trigger on phrases like "Sri Lanka SSCL", "Social Security Contribution Levy", "2.5% turnover levy Sri Lanka", "liable turnover Sri Lanka", or "SSCL registration Sri Lanka". Covers the SSCL at 2.5% on liable turnover, the activity-dependent liable-turnover fraction, and its in-force status (most recently amended by the SSCL Amendment Act No. 24 of 2025). Out of scope — income tax, corporate tax, VAT, and withholding tax (separate skills).
jurisdiction: LK
domain: international
tax_year: 2025
reviewed_by: Lal kumarasiri
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sri-lanka-sscl

## Sri Lanka — Social Security Contribution Levy (SSCL) — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com).** Research-grade (tier 2), drafted from official IRD sources — pending sign-off by a Sri Lankan CA / IRD-registered practitioner. Not tax advice.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country / authority | Sri Lanka — Inland Revenue Department (IRD) |
| Tax | Social Security Contribution Levy (SSCL) — a turnover-based levy, separate from VAT and income tax |
| Currency | LKR |
| **Rate** | **2.5% on liable turnover** |
| Liable turnover | An **activity-dependent fraction (25%–100%) of gross turnover** — NOT gross turnover itself |
| Status | **In force** (most recently amended by the SSCL Amendment Act No. 24 of 2025) |
| Principal statute | Social Security Contribution Levy Act (2022), as amended — VERIFY the exact principal-Act number/year |
| Registration threshold | **Not asserted — VERIFY** (a quarterly liable-turnover threshold applies; confirm current LKR figure with the IRD) |
| Validated by | Pending — Sri Lankan CA / IRD-registered practitioner |
| Skill version | 1.0 |

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Liable-turnover fraction for the activity unclear | Apply the **higher** fraction (up to 100%) and flag |
| Registration obligation borderline (threshold) | Treat as registrable and flag — VERIFY threshold |
| Whether SSCL applies to a supply | Apply 2.5% on the liable fraction and flag for reviewer |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Required inputs** — Business activity classification (importer / manufacturer / service provider / wholesaler-retailer / financial services — drives the liable-turnover fraction); gross turnover for the period; SSCL registration status; any exemptions claimed.

### Refusal catalogue

- **R-LK-SSCL-1 — Liable-turnover fraction tables** — The exact 25%–100% fraction per activity class is set by the SSCL Act/schedules and changes by amendment — this skill states the principle but does NOT assert the per-activity fraction table. VERIFY against the current SSCL Act and IRD guidance; escalate.  _(R-LK-SSCL-1)_
- **R-LK-SSCL-2 — Registration threshold** — The quarterly liable-turnover registration threshold is NOT asserted here — VERIFY the current LKR figure with the IRD.  _(R-LK-SSCL-2)_
- **R-LK-SSCL-3 — Exemptions / sector treatment** — Exempt supplies and sector-specific treatment are schedule-driven — escalate.  _(R-LK-SSCL-3)_
- **R-LK-SSCL-4 — Cross-skill** — Income tax / corporate / VAT / WHT → the respective Sri Lanka skills.  _(R-LK-SSCL-4)_

## Section 3 — Tier 1 rules

### 3.1 Rate and base

- **SSCL rate on liable turnover** — 2.5% percent (Charged on liable turnover, which is an activity-dependent fraction (25%–100%) of gross turnover)  _(Section 3 — Tier 1 rules, 3.1 Rate and base)_
- **Over-statement risk of applying 2.5% to gross turnover** — Applying 2.5% directly to gross turnover for every activity over-states the levy for activities with a sub-100% fraction.  _(Section 3 — Tier 1 rules, 3.1 Rate and base)_
- **SSCL formula** — SSCL = 2.5% × (liable-turnover fraction × gross turnover)  _(Section 3 — Tier 1 rules, 3.1 Rate and base)_
- **Liable-turnover fraction dependency** — The liable-turnover fraction depends on the activity class (importer, manufacturer, service provider, wholesaler/retailer, financial services). The per-activity fraction is not asserted in this skill — VERIFY against the current SSCL Act and IRD schedule.  _(Section 3 — Tier 1 rules, 3.1 Rate and base)_

### 3.2 Status

- **SSCL in-force status** — SSCL is in force for YA 2025/26, most recently amended by the SSCL Amendment Act No. 24 of 2025. (Note: the existing VAT skill flags SSCL status as volatile — this skill confirms it is currently in force, but the practitioner should re-confirm the in-force status and any rate/fraction changes at the date of supply.)  _(Section 3 — Tier 1 rules, 3.2 Status)_

## Section 4 — Worked example (illustrative — confirm the liable fraction)

A manufacturer with gross turnover LKR 100,000,000 in a period, where the applicable liable-turnover fraction is (illustratively) 50%:

```
Liable turnover = 50% × 100,000,000 = 50,000,000
SSCL = 2.5% × 50,000,000 = LKR 1,250,000
```

The 50% fraction is illustrative only — the real fraction must be taken from the current SSCL schedule for the activity class.

## Section 5 — Filing

SSCL is administered by the IRD. Return/payment frequency and due dates — VERIFY against the current IRD SSCL guidance (not asserted here).

## Section 6 — Sources

1. IRD SSCL page — https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Social%20Security%20Contribution%20Levy%20(SSCL).aspx
2. IRD YA 2025/26 tax chart (SSCL 2.5% on liable turnover) — https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx

**Known gaps / VERIFY:** principal-Act number/year; per-activity liable-turnover fractions; registration threshold; filing frequency and due dates; exemptions.

## Prohibitions

- NEVER apply 2.5% to **gross** turnover for an activity whose liable-turnover fraction is below 100% — that over-states the levy.
- NEVER assert a per-activity liable-turnover fraction, a registration threshold, or filing dates this skill flags as VERIFY.
- NEVER treat SSCL as suspended — it is currently in force (re-confirm at the date of supply).
- NEVER file or instruct filing — produce a working paper for practitioner review.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Sri Lankan professional (CA / IRD-registered tax practitioner) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. To speak with a licensed accountant who verifies skills for your jurisdiction — **no liability until both parties sign an engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**
