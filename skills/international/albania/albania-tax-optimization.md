---
name: albania-tax-optimization
description: Use this skill whenever asked about reducing tax in Albania, tax planning, or legal strategies to minimise tax for a self-employed person or small business in Albania. Trigger on phrases like "reduce tax Albania", "0% tax small business Albania", "simplified profit tax", "freelancer Albania", "self-employed vs company Albania", "save tax Albania", "tax planning Albania". This skill covers the 0% rate for traders, the self-employed and entities with gross income up to ALL 14m (to 2029, Law 29/2023 art. 69(1)(dh)), the repeal of the old simplified profit tax, the freelancer single-client reclassification rule, the standard rates above the thresholds, and the anti-avoidance red lines. ALWAYS read this skill before advising on any Albanian tax optimisation.
version: 0.2
jurisdiction: AL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania Tax Optimization

## Albania Tax Optimization Skill v0.1

Albania Tax Optimization Skill v0.1

**Tier 2, source-cited draft. Sources: Law No. 29/2023 on income tax, consolidated to Law No. 81/2025, as published by the General Directorate of Taxes ([tatime.gov.al](https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf), read 2026-10-23). Figures must agree with `albania-income-tax.md` / `albania-social-contributions.md`. NOT yet signed off by an Albanian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Albania |
| Currency | ALL (lek) |
| Headline lever | **0% PIT** for self-employed / small business with gross income ≤ **ALL 14,000,000** — until 31 Dec 2029 |
| VAT threshold | ALL 5,000,000 (~€40k) |
| Self-employed contributions | ~24.4% combined |
| Anti-avoidance | Freelancer single-client reclassification rule |

> **Albania's headline is a temporary 0% rate:** individual traders, the self-employed and entities with **gross income up to ALL 14,000,000 a year** pay **0% income tax until 31 December 2029** (Law 29/2023 art. 69(1)(dh)). It is a threshold, not a band: above ALL 14,000,000 of gross income there is no 0% at all.

## Section 2 -- The 0% Small-Business Regime

- **0% rate**: individual traders, the self-employed and entities with gross income up to ALL 14,000,000 a year pay 0% on the whole business profit until 31 Dec 2029. The test is gross income, not profit.  _(Law 29/2023 art. 69(1)(dh); see `albania-income-tax`)_
- **Old simplified profit tax**: repealed. It sat in Chapter III of Law No. 9632/2006 on local taxes, which Law 29/2023 art. 71(2) repealed; the art. 69(1)(dh) 0% rate is the small-business regime now.  _(Law 29/2023 arts. 69(1)(e), 71(2))_
- **Above ALL 14,000,000 of gross income**: individual traders and the self-employed pay 15% on taxable profit up to ALL 14,000,000 and 23% on the rest, on the whole profit. Entities pay corporate income tax at 15% (see `al-corporate-tax`).  _(Law 29/2023 arts. 24(2), 41)_

This makes Albania extremely efficient for profitable solo/micro service businesses under the cap — but social contributions (~24.4%) and VAT (above ALL 5m) still apply.

## Section 3 -- The Freelancer Single-Client Rule (key constraint)

- **Recharacterisation threshold - single client** — Self-employment income can be recharacterised (toward employment-style treatment) if ≥ 80% of earnings come, directly or indirectly, from one client. percent
- **Recharacterisation threshold - few clients** — Self-employment income can be recharacterised (toward employment-style treatment) if ≥ 90% of revenue comes from fewer than three clients. percent
- **Non-resident exception** — Exception: this does not apply where the self-employed person supplies services exclusively to non-resident individuals/entities without an Albanian permanent establishment.

> **AUDIT FLASH POINT.** A single-client "freelancer" is the primary reclassification target. Diversify clients, or fall within the non-resident exception, and document it.

## Section 4 -- Red Lines (do not cross)

- **Single-client / few-client reclassification** — Single-client / few-client reclassification (Section 3) — the main risk.
- **Mandatory VAT registration** — VAT registration is mandatory above ALL 5m turnover — don't ignore it.
- **Time-limited regime** — The 0% regime is time-limited (to 2029) and income-capped — model the cliff at ALL 14m and the 2030 reversion.
- **No fragmentation without substance** — Don't fragment one business across entities to stay under the cap without substance.

## PROHIBITIONS

- **Prohibition 1** — NEVER present the 0% regime without the ALL 14m cap and the 2029 sunset.
- **Prohibition 2** — NEVER present single-client freelancing as safe self-employment (unless the non-resident exception genuinely applies).
- **Prohibition 3** — NEVER ignore the ALL 5m VAT threshold or the ~24.4% contributions.
- **Prohibition 4** — NEVER contradict the rates in `albania-income-tax.md` / `albania-social-contributions.md`.
- **Prohibition 5** — NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Albanian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Albania) before acting upon.

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
