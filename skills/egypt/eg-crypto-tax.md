---
name: eg-crypto-tax
description: Use this skill whenever asked about the legal status or taxation of cryptocurrency in Egypt , Bitcoin, stablecoins, tokens, NFTs, mining, staking, or trading , for individuals, freelancers, or small businesses. Trigger on phrases like "crypto tax Egypt", "is crypto legal in Egypt", "Bitcoin Egypt tax", "cryptocurrency Egypt", "ضريبة العملات المشفرة", "هل البيتكوين قانوني في مصر", "العملات الرقمية مصر", or any request to classify, compute, or explain Egyptian tax on crypto gains. ALWAYS read this skill before touching any Egypt crypto question. The AI must reply in the user's language (English or Arabic / Egyptian Arabic).
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Crypto Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers how Egyptian income tax reaches cryptocurrency gains, for individuals and small businesses, tax year 2026. Reply in the user's language, English or Arabic.

## Who this applies to

Individuals and small businesses with crypto income: trading, mining, staking, airdrops, NFTs, DeFi and P2P. Companies: `eg-corporate-tax`. Legal permission to deal in crypto is a separate question and needs an Egyptian lawyer before any tax work; the rule the old skill cited could not be opened (see Sources). State this first in every answer: "If you deal in crypto in Egypt, a lawyer must first confirm whether the activity is permitted."

## Rates, bands and thresholds

No crypto rate exists in the tax laws read. Laws 91/2005, 7/2024, 151/2026, 206/2020 and 6/2025 do not mention it. The ordinary table applies to whatever falls within a charge. The table is held in `eg-income-tax`, one home for those figures.

| Item | Rule | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Rates | `eg-income-tax` table | Individual whose gains are income under the classes below | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf |
| Charge on organised activity | Commercial profit, even from a single deal (art. 19 item 3), or the class covering income from any profession or activity not otherwise listed | Law 91 art. 19; art. 32 item 3 as replaced by Law 53/2014 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf |
| Listed-securities exemption | Does not apply | Covers securities listed on the Egyptian exchange (Law 151/2026) | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf |

## The base

If activity is regular and profit-seeking, treat the year's net gain as income from activity on the normal base. If there is no crypto-specific rule, say so: no cost-basis method, FX method, loss rule or filing line is published. Keep complete records in EGP at the date of each trade and show the method chosen. Open questions the AI must state rather than fill: which class applies, whether a one-off disposal is caught at all, losses, and treatment of mining, staking, airdrops, NFTs, DeFi yield and P2P.

Do not say gains are tax-free because no rule exists. Do not give a rate as settled for crypto. Declaring may also be evidence of the activity, which is a lawyer's question.

## Deadlines and filing

Individuals file the annual return before 1 April of the following year, and the steps are in `eg-income-tax`. No crypto line exists on any form read. A person starting an activity notifies ETA within 30 days.

## Penalties and interest

Fines and the delay charge are in `eg-income-tax`. Penalties under banking law are not stated here; see Sources.

## Cross-border points

A foreign exchange does not take income out of the charge. Under Law 91 art. 6 and art. 32 item 3 (Law 53/2014) a resident pays on income realised abroad if Egypt is the centre of the activity. Art. 3 defines Egyptian-source income. Foreign-exchange and capital-control rules are out of scope. Moving funds across the border goes to the lawyer.

## Two worked examples that recompute

**Case 1. Trader treated as active, net gain EGP 300,000.** 1,500 + 2,250 + 26,000 + 22.5% on 100,000 = 52,250, after the legal check.

```oa-check
name: Active trader, net gain 300,000
inputs:
  gain: 300000
steps:
  - tax: 1500 + 2250 + 26000 + (gain - 200000) * 0.225
expected:
  tax: 52250.00
```

**Case 2. Decision: which table row.** Gains of 600,000 keep the 0% band and pay 124,750. Gains of 610,000 lose it and pay 131,250. So 10,000 more gain costs 6,500 more tax. Treatment of each row is the ordinary table, not a crypto rule.

```oa-check
name: Row step at 600,000
inputs:
  low: 600000
  high: 610000
steps:
  - tax_low: 1500 + 2250 + 26000 + 45000 + (low - 400000) * 0.25
  - tax_high: 5500 + 2250 + 26000 + 45000 + (high - 400000) * 0.25
  - step_cost: tax_high - tax_low
expected:
  tax_low: 124750.00
  tax_high: 131250.00
  step_cost: 6500.00
```

Responses by question:
- "Is Bitcoin legal, how is it taxed?" Lawyer first; no crypto tax rule published; ordinary table if the income is caught.
- "I profited on a foreign exchange." One reading, labelled as such, then accountant and lawyer. No firm figure without records.
- "Can I run an exchange?" Lawyer only. No structuring or tax planning for it.

## Ask the client first

1. Resident? 2. What activity, how often, through which platform? 3. Realised gains in EGP for 2026. 4. Records of cost? 5. Other income, to pick the table row. 6. Has a lawyer advised on permission?

Hand over to a lawyer and an accountant for any real filing. Never encourage crypto dealing and never say funds are protected.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 91 of 2005: arts. 3, 6, 19, 32 (OCR) | https://eta.gov.eg/sites/default/files/2024-03/law_no.91-2005.pdf | 2026-11-01 |
| Law 53 of 2014, arts. 6 and 32 as replaced | https://eta.gov.eg/sites/default/files/2024-03/law_no.53-2014.pdf | 2026-11-01 |
| Law 7 of 2024 (page images read) | https://eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf | 2026-11-01 |
| Law 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.151.of_.2026.pdf | 2026-11-01 |
| Central Bank of Egypt banking-laws index (lists Law 194 of 2020; the PDF refused both fetch and archive, text unread) | https://www.cbe.org.eg/ar/laws-regulations/laws/banking-laws | 2026-11-01 |

Not yet confirmed: Law 194 of 2020 art. 206 (prior Central Bank approval for issuing, trading, promoting or running crypto platforms), its penalties, whether any licence was ever granted, and the Central Bank's public warnings: all in the old skill, none opened today. The 2018 Dar al-Ifta fatwa (a religious opinion, not a statute). Any ETA statement on crypto. The grep of tax laws used OCR text, so a spelling variant could escape it.

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
