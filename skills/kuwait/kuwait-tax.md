---
name: kuwait-tax
description: "Routing and bookkeeping treatment for Kuwait tax work in tax year 2026. Covers bank statement patterns for Kuwaiti banks, the Ministry of Finance, customs and PIFSS, how to classify them given no VAT, corporate income tax for a foreign branch, the 5% retention, Zakat, DMTT, and test cases. Use whenever asked to classify Kuwait transactions or handle Kuwait tax work, and for Kuwait VAT status. Kuwait has no VAT. Points to the detailed Kuwait skills for each tax. Not signed off by an accountant."
version: 2.1
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax v2.1

Tax year 2026.

## Who this applies to

Anyone classifying Kuwait bank lines or starting Kuwait tax work. Rates live in the [corporate income tax](kw-corporate-income-tax.md), [VAT](kw-vat-gst.md) and [payroll](kw-payroll-social.md) skills.

Minimum input: a bank statement from NBK, KFH, Gulf Bank, Burgan Bank, Al Ahli United, Boubyan or any Kuwaiti bank.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| VAT or GST | Not implemented | 2026 | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx |
| Corporate income tax | 15% of net taxable income (reg. art. 9) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Zakat | 1% of net profit, public and closed shareholding companies. The earlier text said listed only; the law also covers closed companies | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf |
| NLST | 2.5% of net profit, listed companies | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf |
| DMTT | 15%, groups at EUR 750m or more, from 1 January 2025 | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf |
| Personal income tax | None | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Retention | 5% of the contract or each payment (reg. art. 37) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Late filing | 1% per 30 days or part (reg. art. 34). No 50% cap appears in the text | 2026 | same |
| KFAS | unverified: 1% of net profit, shareholding companies | 2026 | unverified |
| Customs | unverified: 5% of CIF | 2026 | unverified |
| PIFSS | unverified: see [payroll](kw-payroll-social.md) | 2026 | unverified |

## The base

Supplier patterns for bank lines:

| Pattern | Treatment | Notes |
|---|---|---|
| NBK, NATIONAL BANK OF KUWAIT | EXCLUDE | No VAT system |
| KFH, KUWAIT FINANCE HOUSE | EXCLUDE | Same |
| GULF BANK | EXCLUDE | Same |
| BURGAN BANK, BOUBYAN BANK | EXCLUDE | Same |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS | Customs duty only | No VAT |
| PIFSS, PUBLIC INSTITUTION FOR SOCIAL SECURITY | EXCLUDE | Social insurance |

No VAT means no reverse charge and no input recovery; foreign VAT is an irrecoverable cost.

## Deadlines and filing

Income tax return by the 15th day of the 4th month after period end, with audited Arabic statements; four equal instalments on the 15th of the 4th, 6th, 9th and 12th months. The earlier "25% quarterly advance" wording meant these instalments, which follow period end.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill. A failure to register leads to an estimated assessment (reg. art. 19).

## Cross-border points

- Government contractor: 5% retention is held until MOF clears release, then set against tax due.
- Digital services: no VAT; income tax if the activity is Kuwait-source. Escalate.
- Free trade zone: escalate; exemptions were not read.
- Gulf-owned or mixed-owned business: escalate, see Sources.

Test cases: foreign branch KWD 100,000 gives KWD 15,000; VAT question gives "Kuwait does not have VAT"; government payment KWD 50,000 gives retention KWD 2,500.

Never state Kuwait has VAT. Never apply Zakat to a company subject to Decree 3 of 1955 (Law 46 art. 4).

## Two worked examples that recompute

**Example 1.** Foreign branch: KWD 100,000 at 15% gives KWD 15,000, filed by the 15th of the 4th month.

```oa-check
name: Foreign branch
inputs:
  income: 100000
steps:
  - tax: income * 0.15
expected:
  tax: 15000.00
```

**Example 2 (decision).** A customer pays a foreign contractor KWD 50,000. Hold KWD 2,500 or become liable for the tax (reg. arts. 37 and 39). Holding is the only safe choice until MOF approves release.

```oa-check
name: Retention
inputs:
  payment: 50000
steps:
  - held: payment * 0.05
  - paid: payment - held
expected:
  held: 2500.00
  paid: 47500.00
```

## Ask the client first

- Foreign, Kuwaiti or Gulf owned, and in what shares?
- Listed or closed shareholding?
- Group revenue over EUR 750m?
- Any contract with a government body?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; all 23 pages read in Arabic by OCR, art. 9 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |
| Law 46 of 2006, English text, arts. 1 to 5 read | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf | 2026-11-01 |
| Law 19 of 2000, art. 12 read | https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf | 2026-11-01 |
| Decree-Law 157 of 2024, issuing articles and arts. 1, 16, 17, 19, 20, 22, 29 to 34, 36, 38; Kuwait Al-Youm supplement 1719, 31 Dec 2024; read in Arabic by OCR, pp. 10 and 11 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf | 2026-11-01 |

Not yet confirmed: Mixed ownership: how the 15% applies to a company part owned by Kuwaiti and part by foreign holders, and the Kuwaiti and Gulf exemption itself, including the earlier statements here that Gulf nationals are foreign and also exempt (the texts read define the taxpayer as any corporate body; Ministerial Decision 3 of 1989 on equal treatment of Gulf nationals is named in the NLST rule but the copy on the MOF site is a different document); KFAS 1% contribution; the 2.5% and 1% interaction with Free Trade Zone exemptions under Law 26 of 1995; the extension of the 5% retention rule beyond the FY 2026/2027 text for private payers; DMTT Executive Regulations detail (Ministerial Resolution 55 of 2025, not read beyond the title page); any business profits tax draft, for which no enacted text was found; the old cap of 50% on the late filing fine, which no text read supports. Earlier worked cases that taxed the foreign share of a mixed company (70/30 and 60/40 at KWD 200,000) and test 2 (100% Kuwaiti, unlisted, no tax) are held here until that point is confirmed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
