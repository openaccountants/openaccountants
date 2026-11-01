---
name: kw-company-formation
description: "Company formation and entity choice in Kuwait for tax year 2026, with the tax consequences. Covers WLL, closed and public shareholding companies, direct investment licences under Law 116 of 2013, tax exemption up to ten years, tax card and first registrations. Use for questions on setting up in Kuwait, foreign ownership, KDIPA licence, 100% ownership, which entity pays Zakat or NLST, or tax steps after incorporation. Company-law and incorporation procedures are non-operative holds. Any tax incentive requires its actual grant and is not a DMTT exemption. Not signed off by an accountant."
version: 0.3
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Company Formation and Entity Choice v0.3

Tax year 2026.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders and foreign investors choosing a vehicle in Kuwait.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Direct investment ownership | Up to 100% foreign capital for a Kuwaiti company established for licensed direct investment under Law 116/2013 art. 12, subject to the statutory licensing basis | 2026 | https://kdipa.gov.kw/wp-content/uploads/2021/08/law1162013.pdf |
| Licensed investment exemption | A granted exemption covers its specified taxes and duration, up to ten years from actual operation (arts. 27 and 29). A licence alone is not an exemption; Law 157/2024 art. 12 disallows tax exemptions against DMTT | 2026 | same |
| Expansion | Licensed expansion: exemption grant under arts. 27(2) and 29, for no less than the original exemption period, from actual production/operation of the expansion | 2026 | same |
| Imports for the investment | Granted relief can wholly/partly exempt qualifying direct-investment imports (art. 27(3)); five-year restrictions on disposal/other use and payment of duties on permitted disposal apply. This is not the general customs tariff | 2026 | same |
| WLL | unverified: NON-OPERATIVE HOLD. WLL characteristics, shareholder numbers and capital are not established | 2026 | unverified |
| Closed KSC and public KSCP | unverified: NON-OPERATIVE HOLD. Capital, liability and listing status require current company-law evidence | 2026 | unverified |
| Kuwaiti partner | unverified: NON-OPERATIVE HOLD. Do not impose the historical partner percentage | 2026 | unverified |
| Incorporation time | unverified: NON-OPERATIVE HOLD. No incorporation timeline is established | 2026 | unverified |

## The base

Determine the tax regime and exemptions before comparing entities. Law 46/2006 names public and closed Kuwaiti shareholding companies, with the art. 4 exclusions; it does not name WLLs. This does not establish a WLL's overall tax cost or resolve Kuwaiti/Gulf/mixed-ownership income-tax liability. Use [corporate income tax](kw-corporate-income-tax.md) for the regime conditions.

## Deadlines and filing

1. Obtain the current entity-specific MOCI/Kuwait Business Center incorporation procedure. Portal entry point: https://kbc.moci.gov.kw. Name reservation, notarisation, capital deposit, licence, Chamber membership, register entry and their sequence are held, not an operational checklist.
2. Obtain the KDIPA licence and separate incentive decision. Law 116/2013 arts. 27 and 29 govern the requested benefit, not an automatic ten-year holiday.
3. For a taxable corporate body, complete registration and tax-card steps under reg. arts. 11 and 12 through [corporate income tax](kw-corporate-income-tax.md).
4. Hold the annual renewal, Chamber and PIFSS workflow until its current official requirements are read. The sourced tax return requirements remain in the corporate Guide.

## Penalties and interest

See the [corporate income tax](kw-corporate-income-tax.md) skill.

## Cross-border points

A foreign company can also work through an agent, and is still taxed on that activity. Agency contracts go with the tax card application (reg. art. 12).

## Two worked examples that recompute

**Example 1.** A foreign corporate body outside DMTT has KWD 500,000 of confirmed taxable income before an actual full income-tax exemption grant covering the period. The ordinary income-tax comparison is KWD 75,000 without the grant and zero with it, a KWD 75,000 difference. A licence without the grant does not support zero, and the grant cannot exempt DMTT (Law 116 arts. 27/29; Law 157 art. 12).

```oa-check
name: Value of exemption
inputs:
  income: 500000
steps:
  - tax_without_grant: income * 0.15
  - tax_with_actual_full_grant: income * 0
  - saved: tax_without_grant - tax_with_actual_full_grant
expected:
  tax_without_grant: 75000.00
  tax_with_actual_full_grant: 0.00
  saved: 75000.00
```

**Example 2 (decision).** Compare only the Law 46 contribution for KWD 100,000 annual net profit: an otherwise in-scope Kuwaiti closed KSC, outside DMTT and the art. 4 exclusions, has KWD 1,000 contribution. A WLL is not a shareholding company named in Law 46, so that contribution comparison is zero for it. This does not establish either entity's total tax or justify choosing the WLL until ownership, income tax and company-law constraints are settled.

```oa-check
name: KSC contribution
inputs:
  profit: 100000
steps:
  - ksc_contribution: profit * 0.01
  - wll_law46_contribution: profit * 0
  - contribution_difference: ksc_contribution - wll_law46_contribution
expected:
  ksc_contribution: 1000.00
  wll_law46_contribution: 0.00
  contribution_difference: 1000.00
```

## Ask the client first

- Who are the shareholders and their nationalities?
- What activity, and what does the current KDIPA eligibility or exclusion decision say?
- Will it seek a KDIPA licence?
- Will it list?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 116 of 2013, English text, arts. 12, 24 to 29 and 34 read; checked against Arabic lawbook arts. 12, 27 and 29 | https://kdipa.gov.kw/wp-content/uploads/2021/08/law1162013.pdf | 2026-11-01 |
| Law 46 of 2006, English text, arts. 1 to 5 read | https://www.mof.gov.kw/Desicions/Decree/PDF/Law46_2006e.pdf | 2026-11-01 |
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; prior writer read all 23 pages by OCR; closeout re-read cited articles and neighbouring clauses in Arabic OCR, PDF p. 8 visually checked | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |

| Arabic Law 46/2006 arts. 1 to 5 and English official translation, annual contribution and exclusions read | https://www.mof.gov.kw/Desicions/Decree/PDF/Q46-2006.pdf | 2026-11-01 |
| Arabic Law 116/2013 arts. 12, 24 to 29, and 34 read in official KDIPA lawbook (law text only, not the later regulations) | https://kdipa.gov.kw/wp-content/uploads/2023/09/KDIPA-lawbookarabic.pdf | 2026-11-01 |
| DMTT art. 12, no exemption against this tax, with arts. 3 to 16 read | https://www.mof.gov.kw/Desicions/Decree/PDF/DecreeLawDMTTNo157of2024.pdf | 2026-11-01 |

Not yet confirmed: NON-OPERATIVE HOLDS. WLL liability limited to capital, one shareholder, status as common small-business vehicle, no fixed minimum and historical KWD 1,000 suggestion; KSC capital divided into shares and public-company/listing equivalence; these old descriptions are not company-law instructions. Companies Law 1 of 2016 text: moci.gov.kw law pages gave no document link. Minimum capital for WLL, KSC and KSCP, including activity-specific adequacy requirements. The 51% partner rule. Historical two-to-six-week timeline and the complete old incorporation order (name reservation, notarisation, capital deposit, commercial licence, Chamber, commercial register, PIFSS and DIT). Chamber membership and licence renewal details. Whether the KFAS contribution falls on closed KSCs.

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
