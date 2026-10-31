---
name: kuwait-tax
description: Use this skill whenever asked about Kuwait taxation, corporate income tax, ZAKAT, or VAT status. Kuwait does NOT have VAT. CIT at 15% applies to foreign entities only. Kuwaiti entities pay ZAKAT. DMTT at 15% for qualifying MNEs from 1 Jan 2025. ALWAYS read before handling Kuwait tax work.
version: 2.0
jurisdiction: KW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Kuwait |
| VAT/GST status | NOT IMPLEMENTED |
| CIT | 15% flat on foreign-owned share of profits |
| ZAKAT | 1% of net profits (listed Kuwaiti companies) |
| NLST | 2.5% of net profits (listed companies) |
| KFAS | 1% of net profits (shareholding companies) |
| DMTT | 15% on MNEs with global revenue >= EUR 750M (from 1 Jan 2025) |
| Personal income tax | None |
| Authority | Ministry of Finance, Department of Income Tax |
| Portal | https://www.mof.gov.kw |
| Currency | KWD |
| Primary legislation | Income Tax Decree No. 3/1955 as amended by Law No. 2/2008; ZAKAT Law 46/2006 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from NBK, KFH, Gulf Bank, Burgan Bank, Al Ahli United, Boubyan, or any Kuwaiti bank.

## Section 3 -- Supplier pattern library

### 3.1 Kuwaiti banks

**Kuwaiti banks supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NBK, NATIONAL BANK OF KUWAIT | EXCLUDE | No VAT system |
| KFH, KUWAIT FINANCE HOUSE | EXCLUDE | Same |
| GULF BANK | EXCLUDE | Same |
| BURGAN BANK, BOUBYAN BANK | EXCLUDE | Same |

### 3.2 Government

**Government supplier patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MOF, MINISTRY OF FINANCE | EXCLUDE | Tax payment |
| CUSTOMS | Customs duty only (5% CET) | No VAT |
| PIFSS, PUBLIC INSTITUTION FOR SOCIAL SECURITY | EXCLUDE | Social insurance |

## Section 4 -- Worked examples

### Example 1 -- Foreign branch CIT

UK company branch in Kuwait. Net profits KWD 100,000. CIT at 15% = KWD 15,000. File by 15th of 4th month after year-end.

### Example 2 -- Mixed ownership

Company 70% Kuwaiti, 30% US-owned. Profits KWD 200,000. CIT on 30% foreign share = KWD 60,000 x 15% = KWD 9,000.

## Section 5 -- Classification rules

### 5.1 No VAT

- **No VAT** — No VAT registration, returns, invoicing, or recovery in Kuwait.

### 5.2 CIT (foreign entities only)

- **CIT foreign entities only** — 15% flat on foreign-owned share. Kuwaiti-owned exempt from CIT. GCC nationals treated as foreign.

### 5.3 ZAKAT (Kuwaiti listed companies)

- **ZAKAT Kuwaiti listed companies** — 1% of net profits for companies listed on Boursa Kuwait.

### 5.4 Customs

- **Customs rate** — 5% CIF standard (GCC Common External Tariff).

## Section 6 -- No VAT return

CIT return due 15th of 4th month after year-end. Audited Arabic financial statements required.

## Section 7 -- No reverse charge

No VAT system means no reverse charge.

## Section 8 -- No input deductibility

No VAT input recovery. Foreign VAT is irrecoverable cost.

## Section 9 -- Filing, deadlines, and penalties

**Filing and deadlines**

| Obligation | Deadline |
| --- | --- |
| CIT return | 15th of 4th month after year-end |
| Advance CIT | 25% quarterly instalments |
| Tax retention (govt contracts) | 5% of contract value withheld |

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late filing | 1% per month (max 50%) |
| Failure to register | Backdated assessment |

- **Social insurance PIFSS Kuwaiti nationals** — 10.5% employee + 11.5% employer percent

## Section 10 -- Edge cases, test suite, and escalation

### Edge cases

**EC1 -- GCC national.** Saudi-owned business in Kuwait: treated as foreign, CIT 15%.

**EC2 -- Mixed ownership.** CIT on foreign share only. ZAKAT on Kuwaiti share (if listed).

**EC3 -- Government contractor.** 5% retention credited against CIT.

**EC4 -- Anticipating VAT.** No legislation enacted. Do not register or charge VAT.

**EC5 -- Digital services.** No VAT. CIT if PE exists (escalate).

**EC6 -- Free trade zone.** CIT exemptions may apply. Escalate.

### Test suite

**Test 1 -- Foreign branch.** KWD 100,000 profit. Expected: CIT KWD 15,000.

**Test 2 -- Kuwaiti company.** 100% Kuwaiti, not listed. Expected: no CIT, no ZAKAT.

**Test 3 -- Mixed ownership.** 60% Kuwaiti, 40% foreign, KWD 200K profit. Expected: CIT on KWD 80K = KWD 12,000.

**Test 4 -- VAT question.** Expected: "Kuwait does not have VAT."

**Test 5 -- Government retention.** KWD 50,000 payment. Expected: 5% retention = KWD 2,500.

### Prohibitions

- NEVER state Kuwait has VAT
- NEVER apply CIT to 100% Kuwaiti entities
- NEVER apply ZAKAT to foreign entities
- NEVER treat GCC nationals as Kuwaiti for CIT
- NEVER compute numbers -- engine handles arithmetic

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
