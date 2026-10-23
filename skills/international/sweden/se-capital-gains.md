---
name: se-capital-gains
description: "Sweden capital gains tax: 30% on capital income, ISK investment savings account (schablonbeskattning), exit tax on departure. Trigger on: \"Sweden CGT\", \"capital gains Sweden\", \"Sweden 30% capital gains\", \"ISK account Sweden\", \"investeringssparkonto\", \"sell shares Sweden\", \"Sweden exit tax\", \"Sweden capital income tax\"."
version: 1.0
jurisdiction: SE
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SE Capital Gains

## Quick reference

**Quick reference**

| Item | Value |
| --- | --- |
| CGT rate | **30%** on capital income (kapitalinkomst) |
| ISK (investment savings account) | Standard income of 3.55% of the capital base for 2026, taxed at 30% (1.065%), after a tax-free amount on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings |
| Capital loss offset | 70% of losses can offset capital gains |
| Legislation | Inkomstskattelagen (IL), chapter 41–48 |
| Tax authority | Skatteverket (skatteverket.se) |

## Capital gains on shares and securities

- **CGT rate on shares/securities** — 30% percent (taxed as capital income (kapitalinkomst))
- **Capital losses deductibility** — Only 70% of capital losses can be deducted against capital gains. Example: SEK 100,000 loss → SEK 70,000 deductible against gains. Net unused losses: 30% of remaining loss can be deducted against other capital income; the rest is lost.

## ISK — Investment Savings Account (Investeringssparkonto)

- **ISK** — The ISK is a tax wrapper for investments that replaces per-transaction CGT with an annual flat fee
- **Annual schablonbeskattning** — Standard income (schablonintäkt) = capital base × (government borrowing rate at 30 November of the year before + 1 point), at least 1.25% (IL 42 kap. 36 §). For 2026: 2.55% + 1 = 3.55%. The capital base is one quarter of the sum of the account value on the first day of each quarter plus deposits made in that quarter (IL 42 kap. 37 §). Standard income is capital income taxed at 30%.
- **Tax-free amount (from 2026)** — A deduction removes the standard income on the first SEK 300,000 of combined ISK, capital insurance and PEPP savings, ISK first (IL 42 kap. 48 §; SEK 150,000 in 2025). Skatteverket gives it automatically. So for 2026 the tax is 1.065% of the capital base above SEK 300,000, and nil on a base of SEK 300,000 or less.
- **ISK tax treatment of disposals, dividends, contributions** — No CGT on individual disposals within the ISK (IL 42 kap. 42 §). Dividends within the ISK: not separately taxed. Contributions in/out: no tax event.

The ISK is highly favourable for active investors — all gains and dividends subject to one small annual charge rather than 30% per transaction.

**Example (2026).** An ISK with a capital base of SEK 800,000, no capital insurance or PEPP. Standard income 800,000 × 3.55% = SEK 28,400. Deduction 300,000 × 3.55% = SEK 10,650. Taxable capital income SEK 17,750. Tax at 30% = SEK 5,325.

```oa-check
name: ISK capital base SEK 800,000 (2026)
inputs:
  capital_base: 800000
  borrowing_rate: 0.0255
  tax_free_base: 300000
steps:
  - schablon_rate: max(borrowing_rate + 0.01, 0.0125)
  - standard_income: capital_base * schablon_rate
  - deduction: min(standard_income, tax_free_base * schablon_rate)
  - taxable_capital: standard_income - deduction
  - tax: taxable_capital * 0.30
expected:
  standard_income: 28400.00
  deduction: 10650.00
  taxable_capital: 17750.00
  tax: 5325.00
```

## Interest on loans (from 2026)

- **Which interest is deductible** — From income year 2026 interest is deductible in capital only on loans with qualifying security or lender (IL 42 kap. 6 a-6 g §§): a credit institution or mortgage lender loan secured on real property, a site-leasehold or a tenant-owner flat (6 b §); a credit institution or securities firm loan secured on listed securities or fund units (6 c §); a pawnbroker loan (6 d §); and a loan secured on the vehicle, boat, ship or aircraft it financed, where seller and lender are both businesses (6 e §). The lender must be in the EEA or a state with an information-exchange treaty with Sweden (6 f §). Interest on unsecured consumer loans and credit cards is not deductible.
- **Effect on a share sale** — Interest on a margin loan secured on listed shares stays deductible against the 30% capital income, or gives the capital deficit credit (30% up to SEK 100,000, 21% above). The deficit credit is in [se-employee-income-tax](se-employee-income-tax.md).

## Real property

- **Primary residence (privatbostad) sale tax** — 22% tax on 22/30 of the gain = effective rate ~16% on the gross gain percent (primary residence)
- **Other residential property sale tax** — 22% on the full gain percent (other residential property)
- **Deferral relief (uppskovsavdrag)** — Deferral relief (uppskovsavdrag) available on sale of primary residence if reinvesting.

## Exit tax

- **Exit tax on emigration** — When a Swedish tax resident emigrates and holds deferred gains (e.g. from the uppskovsavdrag / deferral relief on real property), those deferred gains are crystallised on departure. Sweden may also apply exit taxation on unrealised share gains in certain circumstances.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), as amended to SFS 2026:1393: 42 kap. 6 a-6 g, 36-37, 42, 48 §§ | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Skatteverket, belopp och procent inkomstår 2026 (schablonintäkt på investeringssparkonto, statslåneränta) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |
| Skatteverket, värdepapper | https://www.skatteverket.se/privat/skatter/vardepapper | not re-read |

Not yet confirmed: the capital loss rules, the property gain fractions, deferral relief and the exit-tax text in this skill were not updated in this refresh and are being checked against IL 45-48 kap.

> Working paper only. ISK schablonbeskattning rates change annually — confirm the
> current year rate from Skatteverket. Have a qualified Swedish tax adviser (skatterådgivare)
> review.

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
