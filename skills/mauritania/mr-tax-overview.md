---
name: mr-tax-overview
description: "Prepare a source-based Mauritania research file for tax-category routing and source-currentness triage in the 2026 country pack. Use this Guide to identify the taxpayer, classify the transaction, assemble the relevant documents and compare the cited statutory baseline with later amendments. It covers the stated ordinary cases, computation conditions, filing obligations and worked decisions, with official source links and explicit limits. Trigger phrases include Mauritania tax, DGI, taxpayer registration, taxable base, payment deadline and compliance evidence. This is a partial research draft: the complete operative amendment chain and current submission procedures are not established, and no licensed accountant has attested this revision."
jurisdiction: MR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
tax_year_notes: "2026 research draft; cited historical baseline and selected later replacements; operative amendment chain incomplete"
---

# Mauritania Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research draft, source baseline only.** The computations below reproduce the cited official code/provisions, not a certified complete statement of operative 2026 law. The January 2023 official code lists amendments only through the January 2022 Finance Act. Selected later Finance Acts were read, including the 2024 transfer-pricing replacement, but the complete commencement/publication chain is not closed. The signed/stamped rectifying Finance Act is visibly numbered 2026-035 on physical page 6. It changes material expense, digital-service and compliance rules; the retained comparison-column headings do not establish proposal status, and its upload date does not prove the operative date. [N02] Resolve the amendment file before using these baselines to file, pay or advise. No accountant has signed this revision.

## Who this applies to

A router for a 2026 Mauritania research file. Choose the taxpayer, income/payment category, period and relevant sibling Guide before computing. Source presence is not comprehensive coverage. This pack retains all seven tax domains as partial until the enactment chain and ordinary filing procedures are established.

## Rates, bands and thresholds

| Item | Rule and conditions | Official source |
|---|---|---|
| Accounting year [C10] | Close accounts at 31 December, except for a transfer or cessation of activity during the year under art. 50(3). A new enterprise can close its first balance sheet at the following year-end, but must prepare a provisional operating account at the first 31 December, tax it immediately and deduct that tax from the first balance-sheet assessment. These ordinary year-end examples assume no midyear transfer or cessation. | [CGI art. 50(3)–(5)](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf) |
| 2026 initial financial tax/TTE changes [N01] | The Ministry’s signed/stamped January 2026 initial Finance Act visibly bears number 2026-001 on physical page 6 (printed page 3). Its art. 3.1 replaces CGI art. 278 financial-operations-tax rates and creates electronic-transaction tax under arts. 293 octies–terdecies, distinct from ordinary VAT. The complete publication/commencement chain and application of the later rectifying Act remain required before transaction advice. | [Law 2026-001, physical p. 6 identity; art. 3.1, printed pp. 3–5](https://www.finances.gov.mr/sites/default/files/2026-01/Loi%20de%20Finances%20pour%20l%E2%80%99ann%C3%A9e%202026.pdf) |
| 2026 rectifying changes requiring commencement reconciliation [N02] | The Ministry’s signed/stamped 2026 rectifying Finance Act visibly bears number 2026-035 on physical/printed page 6. Its art. 3.1 contains replacement expense/NIF controls, digital-service place/liability/platform rules, a TTE cap, supplier reports and professional-account/audit rules. Retained comparison-column headings do not make this signed text merely a proposal. The precise publication/commencement chain and implementing measures are not established here; neither the upload date nor the handwritten number alone establishes when each rule applies. | [Law 2026-035, physical p. 6 identity; art. 3.1, printed pp. 6–18](https://www.finances.gov.mr/sites/default/files/2026-08/LFR%202026%20FR.pdf) |

## The base

- **Tax and legal persons [C01].** IS replaces IBIC and IMF. Capital companies, including a single-member SARL, fall within IS; classify other entities under arts. 2–4 before computing. [CGI arts. 1–4](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).
- **Separate individual business tax [I01].** IBAPP taxes habitual own-account profit-making activity of natural persons and qualifying persons outside IS. Use Mauritanian profits and treaty allocations under art. 71, rather than applying one worldwide-income statement to every category of personal income. [CGI arts. 68–71](https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf).

| Job | Destination |
|---|---|
| Mauritania Corporate Income Tax | [mr-corporate-income-tax](mr-corporate-income-tax.md) |
| Mauritania Individual Income Tax | [mr-income-tax](mr-income-tax.md) |
| Mauritania Payroll and Social Contributions | [mr-payroll-social](mr-payroll-social.md) |
| Mauritania VAT | [mr-vat-gst](mr-vat-gst.md) |
| Mauritania Transfer Pricing and CbCR | [mr-transfer-pricing](mr-transfer-pricing.md) |
| Mauritania Cross-border Tax | [mr-cross-border](mr-cross-border.md) |
| Mauritania Company Formation | [mr-company-formation](mr-company-formation.md) |

## Deadlines and filing

No new universal deadline is supplied here. Read the destination Guide and resolve its source/currentness holds.

## Penalties and interest

No verified general formation/routing penalty or interest percentage is supplied here. Obtain the applicable legal provision for the actual filing or breach; use the tax-specific destination Guide.

## Cross-border points

The old universal worldwide-income/exemption assertion is not a safe routing rule. Salary, business profits, capital income, property and nonresident services each have a separate legal classification. See the linked destination Guide rather than using a headline rate for a different income type.

## Two worked examples that recompute

### 1. Year-end routing before deadlines

Assume the baseline ordinary IS calendar is applicable and a company closes on 31 December with final tax MRU 250,000 and no credits. Allocate 100,000, 75,000 and 75,000 to the following March, June and September dates using C11 in the company Guide. Do not treat those dates as VAT or salary remittance dates.

```oa-check
name: Year-end routing before deadlines
inputs:
  tax: 250000
steps:
  - march: tax * 0.4
  - june: tax * 0.3
  - september: tax - march - june
  - check_total: march + june + september
expected:
  march: 100000
  june: 75000
  september: 75000
  check_total: 250000
```

### 2. Choose payroll calendar by liability, not one universal date

For an assumed January payroll, the cited private CNAM decree uses day 10 of February, while the ITS code uses day 15 of February. The nominal calendar difference is five days. Reserve each liability separately: assumed CNAM 900 and ITS 2,100 require 3,000 total, not a single tax payment. This arithmetic does not establish weekends/extensions or the CNSS due date.

```oa-check
name: Choose payroll calendar by liability, not one universal date
inputs:
  cnam: 900
  its: 2100
  cnam_day: 10
  its_day: 15
steps:
  - total: cnam + its
  - calendar_day_difference: its_day - cnam_day
expected:
  total: 3000
  calendar_day_difference: 5
```

## Ask the client first

- Who earns the income and who pays it?
- What legal form and which income/payment category?
- What period, accounting close and actual payment/accrual dates?
- Domestic work/supply or foreign party/project/treaty?
- Which operative original/amending texts and filing evidence have been read?

## Sources

| Source and exact scope read | URL | Read on |
|---|---|---|
| cgi2023: Official version cover/amendment list and selected CGI arts. 1–14, 23–24, 40–48, 49–67, 68–98, 99–118, 119–137, 150–157, 209–215 (exemption list introductory categories only), 216–221, 227–250, 253–254, LPF L.131–L.139. Not the entire 168-page code or full sector/special regimes. | https://finances.gov.mr/sites/default/files/2023-03/CGI-Fr-2023.pdf | 2026-11-01 |
| lfi2026: Art. 3.1 financial-operations/electronic-transaction tax text, printed pp. 3–5, and introductory provisions. Physical page 6 (printed 3) visually read: signed/stamped law 2026-001. Exact publication/commencement chain remains unresolved; no upload-date commencement inference. | https://www.finances.gov.mr/sites/default/files/2026-01/Loi%20de%20Finances%20pour%20l%E2%80%99ann%C3%A9e%202026.pdf | 2026-11-01 |
| lfr2026: Signed/stamped law 2026-035 identity visually read on physical page 6; art. 3.1 comparison text printed pp. 6–18, covering art. 14, 210, 219, 221/221bis, 249bis/ter, 293decies, LPF L.8/L.8bis/L.16bis/L.20/L.25/L.26. Operative commencement and implementing texts not established. | https://www.finances.gov.mr/sites/default/files/2026-08/LFR%202026%20FR.pdf | 2026-11-01 |

Not yet confirmed: full 2026 enactment/commencement chain and operative August rectifying changes; foreign tax relief/treaties and all sector regimes not expressly worked in sibling Guides; complete local property, customs/excise, incentives, financial tax and electronic-transaction computations; currency redenomination legal instrument and rounding conventions outside the provisions cited; independent review and any credentialed accountant attestation.

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
