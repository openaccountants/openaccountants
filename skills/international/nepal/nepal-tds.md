---
name: nepal-tds
description: ALWAYS read this skill before touching any Nepal TDS / withholding tax work. Use whenever asked to compute or deduct Nepal withholding tax (TDS) on rent, interest, dividends, service/contract payments, or payments to non-residents under the Income Tax Act 2058. Trigger on phrases like "Nepal TDS", "Nepal withholding", "TDS rates Nepal", "Section 88 Nepal", "rent TDS Nepal 10%", "dividend TDS Nepal 5%", "interest TDS Nepal 6%", "contract TDS Nepal 1.5%", or "FY 2082/83 TDS". Out of scope — personal income tax computation (separate skill), corporate tax (separate skill), payroll/SSF salary TDS (use the payroll skill), and VAT.
jurisdiction: NP
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ashish Bista
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nepal Tds

## Nepal — TDS / Withholding Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com).** Research-grade (tier 2) for FY 2082/83. **Source provenance:** figures derive from Nepali professional-firm publications (PKF T.R. Upadhya, Union Nepal) reflecting the Income Tax Act 2058 §87–§88 and Finance Act 2082 — not re-anchored to primary IRD pages. A Nepali CA must confirm against the statute before reliance. Not tax advice.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ashish Bista** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### TDS (Withholding)

- **Rent (paid by a resident person)** — 10%  _(Income Tax Act 2058 s.88 (PKF s.7.1))_
- **Dividend (resident company/partnership)** — 5% (resident AND non-resident)  _(PKF s.7.1)_
- **Interest (Nepal source) — natural person not in business** — 6%  _(PKF s.7.1; Union Nepal)_
- **Interest (Nepal source) — entities** — 15%  _(PKF s.7.1)_
- **Contract/agreement payment to a non-resident** — 5%  _(PKF s.7.1)_
- **Resident contract/supply payments exceeding NPR 50,000** — 1.5%  _(PKF s.7.1)_
- **Flat 15% Section 88 on interest/rent/service** — REFUTED — do not use; the effective rates above govern  _(PKF s.7.1)_
- **10% dividend TDS** — 5% (10% figure refuted)  _(PKF s.7.1)_
- **Non-resident service/royalty/technical fees + DTAA** — 15% standard TDS (subject to lower rates if a DTAA applies)  _(Income Tax Act 2058 s.88)_
- **TDS deposit / return due dates** — 25th of the following Nepali month  _(Income Tax Act 2058 s.90)_
- **Consultancy & Service Fees (Resident)** — 1.5% (if VAT registered) / 15% (if not VAT registered)  _(Income Tax Act 2058 s.88)_
- **Freight & Transportation Services** — 1.5% (if VAT registered) / 2.5% (if not VAT registered)  _(Income Tax Act 2058 s.88)_
- **Windfall Gains (Prizes, Lottery)** — 25% (Final withholding)  _(Income Tax Act 2058 s.88)_

## Section 1 — Quick reference (rates, FY 2082/83 — "no change" from FY 2024-25)

**Payment type / Rate / Notes**

| Payment type | Rate | Notes |
| --- | --- | --- |
| **Rent** (paid by a resident person) | **10%** |  |
| **Dividend** (paid by resident company / partnership) | **5%** | Same to resident AND non-resident |
| **Interest** (Nepal source, from resident banks / FIs / cooperatives / debenture issuers / listed companies) | **6%** to a natural person (not in business); **15%** to entities |  |
| **Contract / agreement payment to a non-resident** | **5%** |  |
| **Contract payments exceeding NPR 50,000** | **1.5%** | Resident contract/supply payments |

**Field / Value**

| Field | Value |
| --- | --- |
| Country / authority | Nepal — Inland Revenue Department (IRD), ird.gov.np |
| Statute | Income Tax Act 2058 (2002) §87–§88, as amended by Finance Act 2082 |
| Income year | Shrawan 1 – Ashad end (BS); FY 2082/83 |
| Validated by | Pending — Nepali CA / registered tax practitioner |
| Skill version | 1.0 |

> **Refuted / do NOT use:** a flat 15% Section 88 TDS on interest/rent/service, and a 10% dividend TDS — both appear in some secondary commentary but were adversarially refuted; the effective FY 2082/83 rates above govern.

### Conservative defaults

**Ambiguity / Default**

| Ambiguity | Default |
| --- | --- |
| Recipient natural person vs entity (interest) | Treat as entity (15%) and flag |
| Resident vs non-resident recipient | Flag; non-resident service/royalty/technical fees beyond the 5% contract rate are VERIFY |
| Contract payment near NPR 50,000 threshold | Apply 1.5% if it exceeds 50,000 |

## Section 2 — Refusal catalogue

- **R-NP-TDS-1 — Salary TDS** — Employment withholding sequences with SSF — use `nepal-payroll`.
- **R-NP-TDS-2 — Non-resident service/royalty/technical fees + DTAA** — Beyond the 5% non-resident contract rate, the full non-resident Section 88 schedule and treaty overrides were NOT established — VERIFY; escalate.
- **R-NP-TDS-3 — Full Section 88 schedule** — Many payment categories exist beyond those listed; this skill covers the common ones. Confirm the full §88 table for FY 2082/83.

## Section 3 — Tier 1 rules

- **Tier 1 rules intro** — 

### 3.1 Rent — 10%

- **Rent** — TDS of 10% on rent paid by a resident person.

### 3.2 Dividend — 5%

- **Dividend** — TDS of 5% on dividends paid by a resident company/partnership — to both resident and non-resident recipients.

### 3.3 Interest — 6% / 15%

- **Interest** — On Nepal-source interest paid by resident banks, financial institutions, cooperatives, debenture issuers, or listed companies: 6% to a natural person who is not deriving the interest in the course of business; 15% to entities.

### 3.4 Contracts

- **Contracts** — Payment under a contract/agreement to a non-resident: 5%. Resident contract/supply payments exceeding NPR 50,000: 1.5%. **Source:** PKF Trunco "Tax Rates 2082-83" §7.1 (each marked "No change"); Union Nepal TDS guide.  _(PKF Trunco "Tax Rates 2082-83" §7.1; Union Nepal TDS guide)_

## Section 4 — Worked examples

- Rent NPR 200,000 to a resident landlord → TDS = 10% × 200,000 = **NPR 20,000**.
- Bank interest NPR 100,000 to an individual (not in business) → TDS = 6% × 100,000 = **NPR 6,000**.
- Dividend NPR 500,000 → TDS = 5% × 500,000 = **NPR 25,000**.
- Resident supply contract NPR 300,000 → TDS = 1.5% × 300,000 = **NPR 4,500**.

## Section 5 — Filing

TDS is deducted at payment and deposited to the IRD with a credit certificate to the payee. **Deposit/return due dates — VERIFY** against the IRD calendar (not established by the research).

## Section 6 — Sources

Research-grade, FY 2082/83. **Secondary firm publications — re-anchor to primary IRD/statute (§87–§88):**
1. PKF T.R. Upadhya & Co. "Tax Rates 2082-83" §7.1 — https://pkf.trunco.com.np/files/publications/1748841198_Tax%20Rates%202082-83_Final_250601_213028.pdf
2. Union Nepal — TDS in Nepal — https://unionnepal.com/tds-in-nepal
3. Income Tax Act 2058 (2002) §88 — confirm at https://ird.gov.np

**Known gaps / VERIFY:** full §88 schedule; non-resident service/royalty/technical-fee rates + DTAA; deposit/return due dates.

## Prohibitions

- NEVER use the refuted flat 15% (interest/rent/service) or 10% dividend rates — use the rates in §1.
- NEVER apply the 6% interest rate to an entity recipient — entities are 15%.
- NEVER assert non-resident service/royalty/technical-fee TDS this skill flags as VERIFY.
- NEVER present these as primary-IRD-confirmed — flag for verifier re-anchoring.
- NEVER file or instruct filing — working paper for practitioner review only.

## Disclaimer

For informational and computational purposes only; not tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Nepali professional (CA / registered tax practitioner) before filing or acting upon. Latest verified version at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
