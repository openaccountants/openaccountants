---
name: mu-company-formation
description: >
  Company formation and entity choice in Mauritius for 2026. Covers the Companies Act 2001, domestic companies, public companies, Global Business and Authorised Companies, the resident director rule, small private company status, online incorporation, fees, annual registration fee, annual return and financial summary, beneficial ownership and timeframes at the Corporate and Business Registration Department. Use for setting up or running a Mauritius company.
jurisdiction: MU
category: formation
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Founders and advisers setting up or running a company in Mauritius, under the Companies Act 2001, registered with the Corporate and Business Registration Department (CBRD). Tax registration follows through [VAT](mauritius-vat.md) and [Payroll social](mu-payroll-social.md).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Incorporation fee | Free, private or public | Signed certificate Rs 300 on request; file summary Rs 100 | 2026 | https://companies.govmu.org/cbrd/incorporation-domestic-company/ |
| Resident director | At least 1 | Ordinarily resident in Mauritius (Companies Act) | 2026 | https://companies.govmu.org/cbrd/wp-content/uploads/2026/09/Companies-Act-200131-08-2026.pdf |
| Shareholders | At least 1 | s.21 essential requirements | 2026 | same |
| GBC and VCC directors | At least 2 resident | CBRD page | 2026 | https://companies.govmu.org/cbrd/incorporation-domestic-company/ |
| Small private company | Turnover under Rs 100 million | Not a Global Business Licence holder or First Schedule Financial Reporting Act entity | 2026 | https://companies.govmu.org/cbrd/wp-content/uploads/2026/09/Companies-Act-200131-08-2026.pdf |
| Annual fee, small to Rs 30m | Rs 500; Rs 750 late | Paid 3 to 20 January | 2026 | https://companies.govmu.org/cbrd/fees-payable-to-roc/ |
| Annual fee, Rs 30m to Rs 100m | Rs 2,500; Rs 3,750 late | same | 2026 | same |
| Annual fee, above Rs 100m | Rs 18,000; Rs 27,000 late | same | 2026 | same |
| Annual fee, public or foreign | Rs 27,000; Rs 40,500 late | same | 2026 | same |
| Annual fee, private GBC | Rs 18,000; Rs 27,000 late | same | 2026 | same |
| Annual fee, Authorised Company | USD 130; USD 200 late | same | 2026 | same |
| First financial year | Not over 18 months | CBRD obligations page | 2026 | https://companies.govmu.org/cbrd/statutory-obligations/ |
| Beneficial owner filing | Within 14 days of the share register entry | CBRD obligations page | 2026 | same |
| Director or secretary change | Within 28 days | same | 2026 | same |
| Annual return | Within 28 days of annual meeting | Financial statements within 6 months of balance sheet date | 2026 | same |

## The base

**Entity choice.** Private company: the common domestic vehicle. Public company. Global Business Company: main business from Mauritius, persons may be non-resident, licensed through the Financial Services Commission. Authorised Company: business, control and management outside Mauritius, not tax resident. A company may be owned by non-residents as long as the resident director rule is met. No minimum capital rule was found; a share company needs one or more shares. A public company or non-small private company's secretary must be qualified (s.165); a small private company is outside that rule.

## Deadlines and filing

1. Check the name is not identical to an existing name, nor on the prohibited list.
2. Incorporate online through the MNS Portal, or at the Registrar's office. A director, secretary, shareholder or representative applies.
3. Give the name, registered office, at least one resident director, shareholders. Corporate shareholders give a signatory letter.
4. Give Business Registration Card details: business name, principal place, nature, start date, workforce, contacts.
5. The Registrar issues the Certificate of Incorporation with a unique number.
6. Register for tax and as employer with the MRA.
7. Each year: pay the fee, hold the annual meeting, prepare statements.
8. File Annual Return (F24) with Financial Summary above Rs 100 million. Below that, Financial Summary only; a No Change Return (F26) where nothing changed; a full Annual Return whenever shares or the board changed.

## Penalties and interest

Failing to file is an offence by the company and every director, and the company may be removed from the register under s.309 (CBRD page). Late annual fees: table above.

## Cross-border points

A foreign company doing business registers under s.276, with authenticated incorporation documents, apostilled where the Hague Convention applies. Tax residence: [Cross-border](mu-cross-border.md).

## Two worked examples that recompute

**Example 1.** Company with turnover Rs 40 million paying the fee late: Rs 3,750, Rs 1,250 above the on-time Rs 2,500.

```oa-check
name: Late fee mid band
inputs:
  ontime: 2500
  late: 3750
steps:
  - extra: late - ontime
expected:
  extra: 1250.00
```

**Example 2. Decision: domestic company or GBC on director cost.** A domestic company needs 1 resident director, a GBC 2. At an assumed Rs 300,000 a year per director, the GBC costs Rs 300,000 more, and a Rs 17,500 higher annual fee for a small company.

```oa-check
name: GBC against domestic company on two costs
inputs:
  director: 300000
steps:
  - extra_director: director * 1
  - extra_fee: 18000 - 500
  - total: extra_director + extra_fee
expected:
  total: 317500.00
```

## Ask the client first

1. Where will the business operate and be managed?
2. Who are the owners and directors, and who lives in Mauritius?
3. Expected turnover?
4. Any regulated or licensed activity?
5. Selling mainly outside Mauritius?

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act 2001 consolidated to 31 August 2026: s.2(5) small company, s.21 essential requirements, s.132 director rule, s.165, s.195 read | https://companies.govmu.org/cbrd/wp-content/uploads/2026/09/Companies-Act-200131-08-2026.pdf | 2026-11-01 |
| CBRD incorporation page, read in full | https://companies.govmu.org/cbrd/incorporation-domestic-company/ | 2026-11-01 |
| CBRD fees page, 2026 table read | https://companies.govmu.org/cbrd/fees-payable-to-roc/ | 2026-11-01 |
| CBRD statutory obligations page, read in full | https://companies.govmu.org/cbrd/statutory-obligations/ | 2026-11-01 |

Not yet confirmed: the old cap of 25 shareholders on a private company, which we did not find; the audit exemption for small companies (Companies Act s.210 onward not read in full); incorporation timing of 1 to 3 weeks; the FSC licensing steps, as the FSC site returned no readable page.

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
