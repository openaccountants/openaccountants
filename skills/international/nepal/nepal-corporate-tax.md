---
name: nepal-corporate-tax
description: "ALWAYS read this skill before touching any Nepal corporate income tax work. Use whenever asked about Nepal company tax for a resident entity. Trigger on phrases like \"Nepal corporate tax\", \"Nepal CIT\", \"company tax Nepal\", \"25% corporate Nepal\", \"30% bank tax Nepal\", \"special industry rebate Nepal\", \"Section 11 Nepal\", \"Income Tax Act 2058 company\", or \"FY 2082/83 company\". Covers the Income Tax Act 2058 (2002) as amended by the Finance Act 2082: the 25% normal rate, the 30% sector rate (banks/insurance/telecom/liquor-tobacco/etc.), and the effective 20% for special industries. Out of scope — personal income tax (separate skill), TDS (separate skill), payroll/SSF, VAT, and sector special computational regimes."
jurisdiction: NP
domain: international
tax_year: 2025
reviewed_by: Ashish Bista
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# nepal-corporate-tax

## Nepal — Corporate Income Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com).** Research-grade (tier 2) for FY 2082/83. **Source provenance:** figures derive from Nepali professional-firm tax-fact publications (PKF T.R. Upadhya, Baker Tilly Nepal) reflecting the Income Tax Act 2058 and Finance Act 2082 — not re-anchored to primary IRD pages. A Nepali CA must confirm against the statute before reliance. Not tax advice.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ashish Bista** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Corporate Income Tax

- **Normal rate** — 25% (general companies, firms, industries)  _(Income Tax Act 2058 Sch.1 (PKF/Baker Tilly))_
- **Banks & financial institutions** — 30%  _(PKF; Baker Tilly)_
- **General (non-life) insurance** — 30%  _(PKF; Baker Tilly)_
- **Petroleum** — 30%  _(PKF; Baker Tilly)_
- **Cigarettes/tobacco/cigars/pan masala/alcohol/beer** — 30%  _(PKF; Baker Tilly)_
- **Telecom & internet service providers** — 30%  _(PKF; Baker Tilly)_
- **Money transfer; capital market/securities/merchant banking/broker** — 30%  _(PKF; Baker Tilly)_
- **Special industries (Section 11)** — Effective 20% (25% less a 20% rebate)  _(Income Tax Act 2058 s.11 (actNepal))_
- **Listed shares — resident entity (capital gains)** — 10%  _(Income Tax Act 2058 s.95Ka (PKF/Baker Tilly))_
- **Land/building — non-individual (entity) capital gains** — 1.5%  _(PKF; Baker Tilly)_
- **Annual return / instalment due dates** — Advance tax due Poush end (40%), Chaitra end (70%), Ashad end (100%); Final return due Ashwin end  _(Income Tax Act 2058 s. 94 & 96)_
- **Export / SEZ / sector concessions beyond Sec 11** — Startups (up to 100m turnover) exempt for 5 yrs; IT exports get 75% tax exemption  _(Finance Act 2083)_
- **IT Industry Bonus Shares** — 0% dividend tax on the capitalization of profits (bonus shares) issued by IT industries  _(Finance Act 2083)_
- **SEZ Rent Exemption** — 100% rent exemption for the first 3 years for new industries established in Special Economic Zones  _(Finance Act 2083)_
- **Tax Dispute Resolution (Waiver)** — One-time settlement window: principal tax + 1% fee (waives penalties/interest)  _(Finance Act 2083)_

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country / authority | Nepal — Inland Revenue Department (IRD), ird.gov.np |
| Currency | NPR |
| Income year | Shrawan 1 – Ashad end (BS); FY 2082/83 ≈ mid-July 2025 – mid-July 2026 |
| Primary legislation | Income Tax Act 2058 (2002), as amended by Finance Act 2082 |
| **Normal rate** | **25%** of taxable income (general companies, firms, industries) |
| **Sector rate** | **30%** — see §3.2 |
| **Special industries (Sec 11)** | Effective **20%** (25% normal less a 20% rebate) |
| Validated by | Pending — Nepali CA / registered tax practitioner |
| Skill version | 1.0 |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Sector unclear | Apply 25% normal |
| Whether 30% sector rate applies | Apply 30% if the entity is in any §3.2 sector; flag |
| Special-industry (Sec 11) rebate claimed | Apply 25% until eligibility confirmed; flag |

## Section 2 — Refusal catalogue

- **R-NP-CT-1** — Sector special computational regimes (banking provisioning, insurance, petroleum) — out of scope; escalate.  _(Section 2 — Refusal catalogue)_
- **R-NP-CT-2** — Special-industry / export / SEZ concessions beyond the headline Section 11 rebate — VERIFY against the Act; escalate.  _(Section 2 — Refusal catalogue)_
- **R-NP-CT-3** — Cross-skill. Personal → `nepal-income-tax`; TDS → `nepal-tds`; payroll/SSF → `nepal-payroll`; VAT → `nepal-vat`.  _(Section 2 — Refusal catalogue)_

## Section 3 — Tier 1 rates

### 3.1 Normal rate — 25%

- **Normal rate** — 25% (general companies, firms, industries)  _(Income Tax Act 2058 Sch.1 (PKF/Baker Tilly))_

### 3.2 Sector rate — 30%

- **Sector rate applicability** — A 30% rate applies to entities in these sectors: Banks and financial institutions (commercial/development banks, finance companies); General (non-life) insurance; Financial-transaction (money-transaction) entities; Petroleum; Cigarettes, tobacco, cigars, pan masala, alcohol, beer; Telecommunications and internet service providers; Money transfer; Capital market / securities / merchant banking / brokerage businesses  _(Income Tax Act 2058 (as amended by Finance Act 2082))_

### 3.3 Special industries — effective 20% (Section 11)

- **Special industries rebate mechanism** — "Special industries" under Section 11 receive a 20% rebate on the normal rate, yielding an effective 20% (25% × 80%). Confirm eligibility under Section 11.  _(Income Tax Act 2058 s.11)_

Rates are **unchanged from FY 2024-25**. **Source:** PKF Trunco; Baker Tilly; actNepal (Section 11 mechanism).

## Section 4 — Tier 2 (capital gains for entities)

- **Listed shares disposed by a resident entity** — 10%
- **Land/building owned by a non-individual (entity)** — 1.5%

(Individual rates are in `nepal-income-tax` / a CGT context.)

## Section 5 — Worked examples

- General company, taxable income NPR 20,000,000 → CIT = 25% × 20,000,000 = **NPR 5,000,000**.
- Commercial bank, taxable income NPR 20,000,000 → CIT = 30% × 20,000,000 = **NPR 6,000,000**.
- Qualifying special industry, taxable income NPR 20,000,000 → CIT = 20% × 20,000,000 = **NPR 4,000,000**.

## Section 6 — Filing

- Income year Shrawan 1 – Ashad end; file via IRD with PAN.
- Annual return + instalment due dates — **VERIFY** (not established by the research).

## Section 7 — Sources

Research-grade, FY 2082/83. **Secondary firm publications — re-anchor to primary IRD/statute:**
1. PKF T.R. Upadhya & Co. "Tax Rates 2082-83" — https://pkf.trunco.com.np/files/publications/1748841198_Tax%20Rates%202082-83_Final_250601_213028.pdf
2. Baker Tilly Nepal "Tax Fact 2025-2026" — https://bakertilly.com.np/storage/download/1750310698_Tax_Fact_2025-2026.pdf
3. Income Tax Act 2058 (2002), Section 11 + Schedule 1 — confirm at https://ird.gov.np
4. Finance Act 2082.

**Known gaps / VERIFY:** primary citations; full special-industry / export / SEZ concession schedule; annual return due dates.

## Prohibitions

- **Prohibitions** — - NEVER apply 25% to a §3.2 sector entity — those are 30%. - NEVER apply the Section 11 effective-20% without confirming special-industry eligibility. - NEVER present these as primary-IRD-confirmed — flag for verifier re-anchoring. - NEVER file or instruct filing — working paper for practitioner review only.

## Disclaimer

For informational and computational purposes only; not tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Nepali professional (CA / registered tax practitioner) before filing or acting upon. Latest verified version at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. **No liability until both parties sign an engagement letter** — book a free 30-minute call: **→ [Book a call](https://calendly.com/openaccountants-info/30min)**
