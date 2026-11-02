---
name: er-company-formation
description: "Entity forms in Eritrea under the Commercial Code in the Ministry of Justice copy: sole trader, partnership, private limited company and share company, with minimum members, capital and licensing law. Covers tax year 2026 in Eritrea from the gazette text. Use for questions such as: how to set up a company in Eritrea, minimum capital in Eritrea, private limited company in Eritrea, business licence in Eritrea."
jurisdiction: ER
category: formation
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea Company Formation and Entity Choice

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The newest income tax text we could open is Legal Notice 119/2012 and the newest sales tax text is Proclamation 117/2001. The Ministry of Justice list dated 2023 shows no later amendment to either. Nothing dated 2023 to 2026 could be opened, so check with the Inland Revenue Department that no later change exists.

## Who this applies to

Founders choosing a form. Forms listed by the Commercial Code include share company and private limited company; sole traders and partnerships also operate. Business licensing is under Proc 72/1995 and its amendment.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Private limited company members | 2 to 50 | Not fewer than two; cannot issue transferable securities | Commercial Code art 510, https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf |
| Private limited company capital | 15,000 | Code says "Ethiopian dollars" | art 512, https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf |
| Private limited share | At least 10 | Equal value | same |
| Share company capital | 50,000 | Code says "Ethiopian dollars" | art 306, https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf |
| Share par value | 10 |  | same |
| Share company members | At least 5 | Not fewer than five to establish | art 307, https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf |
| Restricted business | Banking, insurance | Private limited company may not do these | art 513, https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf |

## The base

A company is taxed at 30%; a sole trader on bands. See [Corporate income tax](er-corporate-income-tax.md).

## Deadlines and filing

Publicity and commercial register entries are required (art 520). Then tax registration and annual filing: category A within 4 months (Proc 62/1994 art 26). Keep records (Legal Notice 20/1995 art 16).

## Penalties and interest

See [Corporate income tax](er-corporate-income-tax.md). If members fall below two, a court can order dissolution unless fixed (art 511).

## Cross-border points

Foreign investment rules are in the Investment Proclamation 59/1994 (Ministry of Justice list), not read.

## Two worked examples that recompute

**Case 1: three founders, equal shares at the minimum capital.** 5,000 each.

```oa-check
name: Equal capital
inputs:
  capital: 15000
  founders: 3
steps:
  - each: capital / founders
expected:
  each: 5000.00
```

**Case 2, a decision: private limited or share company by capital?** Share company needs 35,000 more.

```oa-check
name: Capital gap
inputs:
  share_co: 50000
  plc: 15000
steps:
  - gap: share_co - plc
expected:
  gap: 35000.00
```

## Ask the client first

- Number of founders?
- Activity (banking and insurance are barred for a private limited company)?
- Foreign investors?
- Capital?

## Sources

| Source | URL | Read on |
|---|---|---|
| Commercial Code (Ministry of Justice copy), arts 304 to 306 and 510 to 513 read | https://mojeritrea.net/wp-content/uploads/2023/05/Commercial-Code.pdf | 2026-11-01 |
| Income Tax Proclamation 62/1994, read in full (scan, OCR) | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-01 |
| Income Tax Regulations, Legal Notice 20/1995, arts 7 to 20 and penalties read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf | 2026-11-01 |
| Ministry of Justice, thematic list of domestic legislations, section 16 read | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-01 |

Scans were read by OCR and the key rate pages checked by eye. The Library of Congress item pages show a security check, which we did not pass; the PDFs came straight from its public file host. Scanned gazettes use "Birr" in 1994 and "Nakfa" in later amendments.

Not yet confirmed: Old guide items not confirmed: nakfa conversion of the capital figures; one-member company (the law says two); name reservation, capital deposit and licence steps; timeline of 1 to 4 weeks; foreign investment licence. Old sources (formation vendors) were removed. Business licensing Proc 72/1995 was not read in full. No published 2026 amendment, circular or form could be opened; the Ministry of Finance site did not connect. No official portal or online filing page could be opened either.

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
