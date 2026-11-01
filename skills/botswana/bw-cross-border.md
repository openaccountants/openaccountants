---
name: bw-cross-border
description: >
  Botswana cross-border tax for 2026-27: non-resident withholding, repatriated profit, foreign tax credit, low tax entities, capital gains of non-residents, remote services VAT. Use for inbound or outbound Botswana questions.
version: 0.2
jurisdiction: BW
category: international
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Botswana Cross-Border Tax v0.2

> **General reference only.** This skill is general tax reference material. It has not been reviewed for any specific person's facts. Check figures against the official sources named here.

Tax year: 2026-27 (1 July 2026 to 30 June 2027). The Income Tax Act, 2026, Tax Administration Act, 2026 and Value Added Tax Act, 2026 commenced on 1 July 2026 and replace the old Cap. 52:01 and Cap. 50:03 regimes.

## Who this applies to

Non-residents earning in Botswana, residents with foreign income, and payers abroad.

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Dividend to non-resident | 10% | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (Sch 1 para 6) |
| Interest, royalty, technical fee, director's fee | 15% | 2026-27 | same |
| Repatriated profit of a PE | 10% | 2026-27 | same |
| Entertainer | 10% | 2026-27 | same |
| Insurance premium | 3% | 2026-27 | same |
| Capital gain of a non-resident with no Botswana PE, withheld by buyer | 10% of gross consideration | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (Sch 1 para 6, s 132(3)) |
| Remote supplier VAT threshold | P500,000 | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=958:value-added-tax-act-2026 (Sch 5 para 3) |

## The base

- Withholding on non-residents is final (s 140). Tax treaties can exempt amounts (Sch 2 Pt VI para 1).
- Payment to an address abroad triggers withholding (s 132(2)). IFSC payers and some collective investment undertakings are excused (s 132(5)).
- Buyer or seller can ask BURS to vary the capital gain rate (s 132(4)).
- Foreign tax credit: lesser of foreign tax paid and Botswana tax on that income, by business and investment class, paid within two years (s 96).
- Low tax entity: a resident holding 50% or more includes A x B of investment income (s 119).

## Deadlines and filing

Pay withholding within 14 days after the month (s 138). PE non-resident tax falls due with the return (s 125(2)). Remote suppliers file quarterly via https://eservices.burs.org.bw/remote-services/home.

## Penalties and interest

See [company tax](bw-corporate-income-tax.md). The payer is personally liable.

## Cross-border points

Treaty rate first if a treaty applies; keep a residence certificate.

## Two worked examples that recompute

Example 1. Technical fee P500,000 at 15% = P75,000.

```oa-check
name: Technical fee
inputs:
  fee: 500000
steps:
  - wht: fee * 0.15
expected:
  wht: 75000.00
```

Example 2. A decision: branch or subsidiary on P1,000,000 profit fully paid out. Subsidiary: tax P245,000, dividend tax on P755,000 at 10%. Branch, if all is repatriated, gives the same rates.

```oa-check
name: Paid out
inputs:
  profit: 1000000
steps:
  - tax: profit * 0.245
  - second: (profit - tax) * 0.10
  - total: tax + second
expected:
  tax: 245000.00
  second: 75500.00
  total: 320500.00
```

## Ask the client first

- Who is paying whom, and from where?
- Recipient's residence, and is there a treaty?
- Any presence or staff in Botswana?
- Assets in Botswana being sold?
- Foreign tax paid?

## Sources

| Source | Link | Read |
|---|---|---|
| Income Tax Act, 2026 (No. 13 of 2026), read: ss 7, 8, 17, 28, 34 to 37, 53, 96, 117, 119, 123 to 144, Schedules 1 to 3; Regulations SI 92 and Commencement Order SI 93 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 | 2026-11-01 |
| Value Added Tax Act, 2026 (No. 15 of 2026), read: ss 7 to 9, 12 to 14, 28, 54, 57, 65, 66, Schedules 1, 2, 5; Regulations SI 94 and Order SI 95 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=958:value-added-tax-act-2026 | 2026-11-01 |
| Tax Administration Act, 2026 (No. 14 of 2026), read: ss 14, 18, 27, 41, 98, 101 to 103; Regulations SI 90 regs 3, 4, 21, 28, 30, 33, 34 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026 | 2026-11-01 |

Not yet confirmed: the list of treaties and their rates (no official list opened); how repatriated profit is measured in s 99 (not read in full).

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
