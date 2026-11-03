---
name: kuwait-tax
description: "Routing and bookkeeping treatment for Kuwait tax work in tax year 2026. Covers bank statement patterns for Kuwaiti banks, the Ministry of Finance, customs and PIFSS, the supporting records needed before classifying them, corporate income tax for a foreign branch, the 5% retention, Zakat, DMTT, and test cases. Use whenever asked to classify Kuwait transactions or handle Kuwait tax work, and for the held question of current Kuwait VAT implementation. Points to the detailed Kuwait skills for each tax. Not signed off by an accountant."
version: 2.2
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax v2.2

Tax year 2026.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone classifying Kuwait bank lines or starting Kuwait tax work. Rates live in the [corporate income tax](kw-corporate-income-tax.md), [VAT](kw-vat-gst.md) and [payroll](kw-payroll-social.md) skills.

Minimum input: a bank statement from NBK, KFH, Gulf Bank, Burgan Bank, Al Ahli United, Boubyan or any Kuwaiti bank.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| VAT or GST | unverified: NON-OPERATIVE HOLD, see [VAT](kw-vat-gst.md) | 2026 | https://www.mof.gov.kw/MOFDesicions/mofDesicions1.aspx |
| Corporate income tax | 15% of confirmed ordinary net taxable income, outside DMTT; Kuwaiti/Gulf/mixed ownership is held (reg. art. 9) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Zakat | 1% annual net profit, Kuwaiti public/closed shareholding companies outside Law 46 art. 4 exclusions and DMTT | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf |
| NLST | 2.5% annual net profit, listed Kuwaiti companies outside DMTT (Law 19 art. 12) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf |
| DMTT | 15% effective minimum; EUR 750m consolidated revenue in two of four prior periods, subject to entity exclusions; periods from 1 January 2025, not a flat profit tax | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf |
| Personal income tax | Own trade/work income exempt unless it represents a corporate body's share (reg. art. 8(2)) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Retention | 5% of contract or each payment for in-scope ordinary-tax payers/payees, until MOF release (reg. arts. 37 to 39); DMTT public-circular carve-out is separately scoped in corporate Guide | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Late filing | 1% per 30 days or part (reg. art. 34). No 50% cap appears in the text | 2026 | same |
| KFAS | unverified: NON-OPERATIVE HOLD, historical figure in Sources | 2026 | unverified |
| Customs | unverified: NON-OPERATIVE HOLD, historical figure in Sources | 2026 | unverified |
| PIFSS | unverified: see [payroll](kw-payroll-social.md) | 2026 | unverified |

## The base

Supplier patterns are search cues, not final tax or ledger classifications. EXCLUDE below means exclude from automatic tax-rate computation until the underlying document is obtained, not omit the transaction from books:

| Pattern | Treatment | Notes |
|---|---|---|
| NBK, NATIONAL BANK OF KUWAIT | EXCLUDE | Obtain bank fee, interest or transfer support |
| KFH, KUWAIT FINANCE HOUSE | EXCLUDE | Obtain underlying bank document |
| GULF BANK | EXCLUDE | Obtain underlying bank document |
| BURGAN BANK, BOUBYAN BANK | EXCLUDE | Obtain underlying bank document |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Reconcile to MOF assessment or payment receipt |
| CUSTOMS | HOLD | Obtain customs declaration and charge breakdown; no rate established here |
| PIFSS, PUBLIC INSTITUTION FOR SOCIAL SECURITY | EXCLUDE | Reconcile to PIFSS assessment; coverage/rates held |

VAT, reverse charge, input recovery and foreign-tax recoverability are source holds in [VAT](kw-vat-gst.md). Do not make a no-VAT or irrecoverable-cost classification from a bank description.

## Deadlines and filing

Income tax return by the 15th day of the 4th month after period end, with audited Arabic statements; four equal instalments on the 15th of the 4th, 6th, 9th and 12th months. The earlier "25% quarterly advance" wording meant these instalments, which follow period end.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill. An unfiled return or inadequate records can lead to estimated assessment under reg. art. 19; it is not described here as a penalty automatically triggered by registration failure alone.

## Cross-border points

- Contractor outside DMTT with established ordinary income-tax retention: hold 5% under reg. art. 37 until MOF authorises release or directs remittance under arts. 38 and 39. Retention is not automatically a final tax or credit; reconcile any MOF remittance.
- Digital services: VAT implementation is held; corporate income-tax source and scope need a separate check. Escalate before deciding tax.
- Free trade zone: escalate; exemptions were not read.
- Gulf-owned or mixed-owned business: escalate, see Sources.

Test cases: confirmed ordinary-tax foreign branch outside DMTT, no exemption/losses, KWD 100,000 taxable income gives KWD 15,000; VAT question is referred to the current-status hold; in-scope ordinary-tax contract payment KWD 50,000 gives retention KWD 2,500. Mixed-ownership and wholly Kuwaiti cases remain held in Sources.

Do not assert VAT presence or absence from an index alone. Never apply Zakat to a company subject to Decree 3 of 1955 (Law 46 art. 4).

## Two worked examples that recompute

**Example 1.** A foreign branch outside DMTT with confirmed ordinary income-tax liability and no exemption or losses: KWD 100,000 at 15% gives KWD 15,000, filed by the 15th of the 4th month.

```oa-check
name: Foreign branch
inputs:
  income: 100000
steps:
  - tax: income * 0.15
expected:
  tax: 15000.00
```

**Example 2 (decision).** A payer within reg. art. 37 pays KWD 50,000 to a foreign contractor outside DMTT with an established ordinary-tax retention obligation. Without an MOF release, retain KWD 2,500 and pay KWD 47,500. With an actual MOF release of this payment, retention is zero and cash payment KWD 50,000. The release document decides the branch; failure to retain/remit can make the payer liable for the tax (arts. 38 and 39).

```oa-check
name: Retention
inputs:
  payment: 50000
steps:
  - held: payment * 0.05
  - paid: payment - held
  - held_with_mof_release: payment * 0
  - paid_with_mof_release: payment - held_with_mof_release
expected:
  held: 2500.00
  paid: 47500.00
  held_with_mof_release: 0.00
  paid_with_mof_release: 50000.00
```

## Ask the client first

- Foreign, Kuwaiti or Gulf owned, and in what shares?
- Listed or closed shareholding?
- Group revenue over EUR 750m?
- Any contract with a government body?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; prior writer read all 23 pages by OCR; closeout re-read cited articles and neighbouring clauses in Arabic OCR, PDF p. 8 visually checked | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |
| Law 46 of 2006, English text, arts. 1 to 5 read | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf | 2026-11-01 |
| Law 19 of 2000, art. 12 read | https://www.mof.gov.kw/Desicions/Decree/PDF/LawNo19Of2000NationalLabor.pdf | 2026-11-01 |
| Decree-Law 157 of 2024, issuing articles and arts. 1 to 22, 29 to 34, 36, 38 and 41; Arabic OCR clauses and neighbours read; penalty PDF p. 10 visually checked; prior writer also checked p. 11 | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf | 2026-11-01 |

Not yet confirmed: NON-OPERATIVE HOLDS. Historical no-VAT, no reverse charge, no input recovery, foreign VAT irrecoverability and no-VAT bank exclusions (see VAT Guide); customs 5% of CIF, tobacco exceptions; PIFSS 10.5% employee and 11.5% employer and all coverage details (see payroll Guide). Mixed ownership: how the 15% applies to a company part owned by Kuwaiti and part by foreign holders, and the Kuwaiti and Gulf exemption itself, including the earlier statements here that Gulf nationals are foreign and also exempt (the texts read define the taxpayer as any corporate body; Ministerial Decision 3 of 1989 on equal treatment of Gulf nationals is named in the NLST rule but the copy on the MOF site is a different document); KFAS 1% contribution; the 2.5% and 1% interaction with Free Trade Zone exemptions under Law 26 of 1995; the extension of the FY 2026/2027 DMTT retention carve-out and five-year transfer direction to private payers; DMTT Executive Regulations detail (Ministerial Resolution 55 of 2025, not read beyond the title page); any business profits tax draft, for which no enacted text was found; the old cap of 50% on the late filing fine, which no text read supports. Earlier worked cases that taxed the foreign share of a mixed company (70/30 and 60/40 at KWD 200,000) and test 2 (100% Kuwaiti, unlisted, no tax) are held here until that point is confirmed.

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
