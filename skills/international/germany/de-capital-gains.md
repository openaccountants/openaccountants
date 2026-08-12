---
name: de-capital-gains
description: "Use this skill for any German capital gains tax question. Trigger on: \"Abgeltungsteuer\", \"capital gains Germany\", \"CGT Germany\", \"Kapitalertragsteuer\", \"Sparer-Pauschbetrag\", \"sell shares Germany\", \"German exit tax\", \"Wegzugsbesteuerung\", \"leaving Germany tax shares\", \"crypto Germany CGT\", \"German investment gains\", \"German shareholder 1% rule\". Covers Abgeltungsteuer flat rate, annual exemption, offsetting losses, exit tax on departure."
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - de-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Capital Gains

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany |
| System | Abgeltungsteuer (withholding tax on investment income) |
| Rate | 25% + 5.5% solidarity surcharge = **26.375%** total |
| Annual exemption (Sparer-Pauschbetrag) | **€1,000** single / **€2,000** joint (from 2023) |
| Loss offsetting | Capital losses can only offset capital gains |
| Church tax | Additional 8-9% on the 25% base if member |
| Exit tax | Yes — on departure with substantial shareholdings |
| Primary legislation | Einkommensteuergesetz (EStG) §20, §32d |
| Tax authority | Bundeszentralamt für Steuern / local Finanzamt |
| Verified by | Pending — German Steuerberater sign-off required |

## Section 2 — What is Taxed: Abgeltungsteuer

- **Abgeltungsteuer scope** — The Abgeltungsteuer (withholding/flat tax) applies to: Capital gains from disposal of shares, bonds, funds, ETFs; Dividends; Interest income; Gains from derivatives, CFDs, options; Crypto asset gains (treated as private sale transactions under §23 EStG)  _(§23 EStG)_
- **Final withholding tax nature** — The 26.375% is a final withholding tax — German banks withhold it automatically. Income subject to Abgeltungsteuer is NOT added to the progressive income tax base (no further top-up unless electing progressive rates and the marginal rate is lower).

## Section 3 — Annual Exemption (Sparer-Pauschbetrag)

Each individual has an annual tax-free allowance:

**Sparer-Pauschbetrag allowance table**

| Status | Allowance |
| --- | --- |
| Single individual | **€1,000** |
| Jointly assessed couple | **€2,000** |

- **Allowance coverage and carry-forward** — The allowance covers all investment income (dividends + interest + gains combined). Unused allowance cannot be carried forward.
- **Freistellungsauftrag** — Instruct your German bank to apply the exemption automatically (up to the €1,000/€2,000 limit across all banks).

## Section 4 — Loss Offsetting Rules

- **Loss offsetting (Verlustverrechnungstopf)** — Capital losses (Verlustverrechnungstopf) can only be offset against capital gains: Share losses can only offset share gains (stricter rule from 2020); Other capital losses (e.g. bond gains) can offset each other; Unused losses carry forward indefinitely to future years; Capital losses cannot offset employment income or other income
- **Verlustbescheinigung** — Annual capital loss certificate issued by banks (Verlustbescheinigung) — can be used when filing tax return.

## Section 5 — Substantial Shareholdings: Different Rules

- **Substantial shareholding taxation — Teileinkünfteverfahren** — For substantial holdings (≥1% shareholding in a company), gains are NOT taxed under Abgeltungsteuer. Instead, they are taxed under the Teileinkünfteverfahren: 60% of the gain is included in taxable income; Taxed at the progressive income tax rate (up to 45%); Effective rate: up to 27% (60% × 45%)
- **Applicability regardless of company location** — This applies regardless of whether the company is German or foreign.

## Section 6 — Exit Tax (Wegzugsbesteuerung) — CRITICAL

- **Exit tax imposition** — Germany imposes an exit tax (§6 AStG) when an individual leaves Germany and holds a qualifying shareholding.  _(§6 AStG)_
- **Qualifying holding** — ≥1% shareholding in a corporation at any point in the preceding 5 years.  _(§6 AStG)_
- **Trigger** — Departure from Germany (ceasing German tax residence).
- **What happens** — Deemed disposal of the shares at market value — unrealised gains are taxed as if the shares were sold on the day of departure.
- **Exit tax rate** — Teileinkünfteverfahren (60% of gain at progressive rates)
- **Deferral options** — Moving within EU/EEA: tax can be deferred interest-free until actual disposal. Moving to third country (e.g. UAE, Singapore, UK): tax is immediately payable (or can be paid in 7 annual instalments in some cases)

This is a major planning consideration for anyone leaving Germany with significant company shareholdings.

## Section 7 — Crypto Assets

- **Crypto taxation under §23 EStG** — Cryptocurrency gains in Germany are subject to special rules under §23 EStG (not Abgeltungsteuer): Holding period < 1 year: gain fully taxable at progressive rates (no flat 26.375%); Holding period ≥ 1 year: completely exempt from tax; Annual exemption for §23 gains: €1,000 total (not the €1,000 Sparer-Pauschbetrag); Loss offsetting: §23 losses only offset §23 gains  _(§23 EStG)_

See `de-crypto-tax` for full crypto analysis.

## Section 8 — Sources

- EStG §20 (investment income), §32d (Abgeltungsteuer), §23 (private sale transactions)
- AStG §6 (exit tax)
- Bundesfinanzministerium: bundesfinanzministerium.de
- BMF-Schreiben on Abgeltungsteuer

> **Working paper only.** Exit tax (§6 AStG) analysis requires shareholding history and market value determination — engage a German Steuerberater before departing Germany with shareholdings ≥1%.

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
