---
name: cyprus-tax-optimization
description: Use this skill whenever asked about reducing tax in Cyprus, tax planning, or legal strategies to minimise tax for an individual, freelancer, or company in Cyprus. Trigger on phrases like "reduce tax Cyprus", "Cyprus non-dom", "non-domiciled", "0% dividend tax", "SDC exemption", "Cyprus IP box", "3% tax IP", "Cyprus company dividends", "60-day rule", "save tax Cyprus", "tax planning Cyprus". This skill covers the non-dom regime (17 years 0% SDC on dividends/interest/rents), the company-plus-dividend extraction structure, the IP Box (~3% on qualifying IP), self-employment vs company, the personal-income reliefs, and the substance/anti-avoidance red lines. ALWAYS read this skill before advising on any Cyprus tax optimisation.
version: 0.1
jurisdiction: CY
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christos Thoma
review_status: current
category: tax-optimization
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus Tax Optimization

## Cyprus Tax Optimization Skill v0.1

**Tier 2 — research-verified. Sources: Cyprus Tax Department, PwC/KPMG/Deloitte Cyprus, 2026 tax-reform commentary. Figures must agree with `cyprus-income-tax.md` / `cyprus-social-contributions.md`. NOT yet signed off by a Cyprus tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Christos Thoma** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### cyprus-tax-optimization

- **Personal income tax — zero-rate band (2025)** — 0% on income up to €19,500  _(cyprus-income-tax.md)_
- **Personal income tax — zero-rate band (2026 reform)** — 0% on income up to €22,000  _(cyprus-income-tax.md)_
- **Personal income tax — bands above zero-rate threshold** — 20%, 25%, 30%, 35%  _(cyprus-income-tax.md)_
- **Corporate income tax (CIT) — current rate** — 15% standard corporate income tax rate from 1 January 2026; 12.5% applies up to 31 December 2025.  _(https://taxsummaries.pwc.com/cyprus/corporate/taxes-on-corporate-income ; https://www.pwc.com.cy/en/services/tax-legal-services/tax-advisory-services/the-cyprus-tax-reform.html)_
- **Corporate income tax (CIT) — OECD Pillar Two rate** — 15%  _(OECD Pillar Two)_
- **SDC (Special Defence Contribution) — non-dom exemption on dividends, interest and rental income** — 0%  _(Savva; KPMG)_
- **Self-employed social insurance rate — on deemed income** — ~16.6%  _(cyprus-social-contributions.md)_
- **Foreign pension — flat rate (above exempt amount)** — 5% flat rate on foreign pension income above EUR 5,000 from 1 January 2026; the taxpayer may elect annually to be taxed under normal PIT rates instead.  _(https://www.pwc.com.cy/en/publications/assets/tff-eng-2026.pdf)_
- **IP Box — effective tax rate on qualifying IP income** — ~3%  _(Mondaq; LCK)_
- **IP Box — deemed deduction on qualifying IP income** — 80% deemed deduction (leaving 20% taxable at corporate rate)  _(Mondaq; LCK)_
- **Non-dom regime — 0% SDC exemption period (base)** — 17 years of Cyprus tax residency  _(Savva; KPMG)_
- **Non-dom regime — extension period per block** — Two further 5-year blocks (up to 27 years total)  _(Savva; KPMG)_
- **Non-dom regime — lump-sum fee per 5-year extension block** — €250,000 per block  _(Savva; KPMG)_
- **Tax residency — standard day-count rule** — 183 days in Cyprus in a tax year
- **Tax residency — 60-day rule minimum days in Cyprus** — ≥60 days in Cyprus
- **Tax residency — 60-day rule: maximum days in any single other country** — No more than 183 days in any single other country
- **Tax residency — 60-day rule: must not be tax-resident elsewhere** — Removed from the 60-day tax residency rule from 1 January 2026. The individual may be tax resident elsewhere; other 60-day rule conditions must still be assessed.  _(https://www.pwc.com.cy/en/services/tax-legal-services/tax-advisory-services/the-cyprus-tax-reform.html)_
- **Expat / first-employment relief — high earner exemption** — 50% exemption on employment income for new residents earning above a salary threshold
- **Expat / first-employment relief — standard new-resident exemption** — Older first-employment relief: lower of 20% of remuneration or EUR 8,550/year where applicable. From 2026, a new Article 8(21B) incentive provides a 25% exemption capped at EUR 25,000 for qualifying individuals, for 7 years.  _(https://www.pwc.com.cy/en/publications/direct-tax-updates-2026/dtu-n4-2026.pdf ; https://www.pwc.com.cy/en/services/tax-legal-services/tax-advisory-services/the-cyprus-tax-reform.html)_
- **PIT on dividends for non-dom shareholder** — Dividends are exempt from PIT. A Cyprus tax resident non-domiciled individual is also exempt from SDC on dividends; GHS at 2.65% may apply on dividend income, subject to the EUR 180,000 annual GHS cap.  _(https://taxsummaries.pwc.com/cyprus/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/cyprus/individual/other-taxes)_
- **Personal income tax — maximum marginal rate** — 35%  _(cyprus-income-tax.md)_

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Cyprus |
| Currency | EUR |
| Headline levers | Non-dom (0% SDC on dividends/interest/rents); company + dividend extraction; IP Box (~3% on qualifying IP) |
| Personal income tax | 0% up to €19,500 (2025); 20/25/30/35% bands above. **2026 reform raises the 0% band to €22,000** — confirm against `cyprus-income-tax.md`. |
| Corporate tax | 12.5% → **15%** under OECD Pillar Two (confirm effective date) |
| SDC (Special Defence Contribution) | Applies to dividends/interest/rents of Cyprus-DOMICILED residents; **non-doms are exempt** |
| Self-employed social insurance | ~16.6% of deemed income |
| Anti-avoidance | Substance / place-of-effective-management; ATAD GAAR |

> **The Cyprus headline is the NON-DOM + COMPANY combo:** run profits through a Cyprus company (15% CIT from 1 January 2026; 12.5% up to 31 December 2025), then extract as dividends which — for a non-dom — bear **0% SDC and 0% PIT**. Total effective tax ≈ the corporate rate only.

## Section 2 -- Non-Dom Regime (the headline)

- **Non-dom 0% SDC on worldwide dividends, interest and rental income** — A Cyprus tax resident who is non-domiciled pays 0% SDC on worldwide dividends, interest and rental income for 17 years of residency (extendable by two further 5-year blocks via a €250,000 lump-sum fee each → up to 27 years).  _(Savva; KPMG)_
- **Becoming resident — routes** — 183-day rule, or 60-day rule: ≥60 days in Cyprus, no >183 days in any single country, plus a Cyprus tie (business/employment/directorship) and a residence (owned or rented). From 1 January 2026, the condition of not being tax-resident elsewhere is removed; other conditions must still be met.

**AUDIT FLASH POINT** — the 60-day route and non-dom status require genuine residency and ties; sham residency is challengeable. Confirm the client actually meets the day-count and tie tests.

## Section 3 -- Company + Dividend Extraction

**Section 3 -- Company + Dividend Extraction**

| Step | Treatment |
| --- | --- |
| Trade through a Cyprus company | 12.5–15% CIT on profits |
| Pay a modest director salary | Deductible; subject to PIT + social insurance; covers cover/pension |
| Distribute the rest as dividends | Non-dom shareholder: **0% SDC + 0% PIT** on dividends (GHS at 2.65% may apply, subject to the EUR 180,000 annual GHS cap) |

Net effect for a non-dom owner-manager: roughly the **corporate rate only** on extracted profit. Compare with operating as a **self-employed individual**, taxed on the progressive scale up to 35% — usually worse at higher incomes. **[RESEARCH GAP — model the salary/dividend split and confirm the GHS (health) contribution treatment on dividends.]**

## Section 4 -- IP Box (~3% on qualifying IP)

- **IP Box mechanics** — Qualifying IP income (patents, copyrighted software, etc.) gets an 80% deemed deduction, so only 20% is taxed at the corporate rate → ≈3% effective. Benefit is proportional to the R&D you actually incur (OECD modified nexus). Ideal for SaaS/tech/IP founders.  _(Mondaq; LCK)_

**AUDIT FLASH POINT** — the nexus rule ties the benefit to genuine R&D substance in Cyprus; acquired IP with no local development does not qualify. **[RESEARCH GAP — reviewer to confirm qualifying-asset definitions and the nexus fraction.]**

## Section 5 -- Personal Reliefs & Exemptions

**Section 5 -- Personal Reliefs & Exemptions**

| Relief | Detail |
| --- | --- |
| 0% band | Income up to €19,500 (2025) / €22,000 (2026 reform) is tax-free. |
| Expat / first-employment relief | 50% exemption for high-earning new residents (above a salary threshold) for a number of years; a separate 20% relief exists for others. **[RESEARCH GAP — reviewer to confirm current thresholds and durations after the 2026 reform.]** |
| Foreign pension | Taxed at a flat 5% above EUR 5,000 from 1 January 2026 (taxpayer may elect annually to be taxed under normal PIT rates instead). |
| Life insurance / provident / social insurance | Deductible up to a capped percentage of income. |

## Section 6 -- Red Lines (do not cross)

- **Substance & management** — A Cyprus company must be genuinely managed and controlled in Cyprus (board, decisions, substance) to be Cyprus-resident and to benefit. Letterbox companies are challengeable.
- **Non-dom residency must be real** — Meet the day-count and tie tests; don't fabricate residency.
- **IP Box needs real R&D** — Nexus approach; no benefit for parked, acquired IP.
- **ATAD GAAR / anti-abuse** — ATAD GAAR / anti-abuse applies to arrangements whose main purpose is a tax advantage without substance.

## PROHIBITIONS

- **Non-dom 0% SDC without residency confirmation** — NEVER present non-dom 0% SDC without confirming genuine Cyprus tax residency (60-day or 183-day test).
- **IP Box 3% without nexus condition** — NEVER present the IP Box 3% without the R&D-nexus / substance condition.
- **Substance-free company as tax shell** — NEVER advise a substance-free Cyprus company as a tax shell.
- **Contradicting other skills' rates** — NEVER contradict the rates/bands in `cyprus-income-tax.md` / `cyprus-social-contributions.md`.
- **Research gap figures presented as confirmed** — NEVER present any [RESEARCH GAP] figure as confirmed, nor present optimisation as definitive advice — route to a licensed Cyprus tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Cyprus) before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
