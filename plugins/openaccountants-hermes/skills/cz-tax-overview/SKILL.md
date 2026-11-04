---
name: cz-tax-overview
description: "Use this skill as the entry point for Czech tax in tax year 2026. It gives the headline figures and points to the skill that holds the detail: individual income tax at 15% and 23% above CZK 1,762,812 (36 times the 2026 average wage of CZK 48,967), the basic credit of CZK 30,840, corporate income tax at 21%, VAT at 21% and 12% with the CZK 2,000,000 registration threshold, late payment interest, and the return deadlines for 2026 (1 April, 3 May and 1 July 2027). Trigger on: Czech tax overview, taxes in the Czech Republic, Czech tax rates 2026, daně v ČR. Out of scope: the detail of each tax, which lives in cz-employee-income-tax, cz-income-tax, cz-corporate-income-tax, cz-vat-return, cz-employee-contributions, cz-social-health, cz-payroll, cz-transfer-pricing and cz-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cz-tax-overview"
  jurisdiction: "CZ"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Czech Republic: tax overview (2026) v0.1

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet. Figures come from the consolidated laws on e-Sbírka and from financnisprava.gov.cz and cnb.cz, read on 23 October 2026, and match the other 2026 skills in this pack. It is a map, not a computation: open the linked skill before advising.

## The system at a glance

- **Tax year.** The calendar year for individuals. Companies use the calendar year or a financial year (Income Taxes Act ("ITA") § 21a).
- **Currency.** Czech koruna (CZK).
- **Authority.** The Financial Administration (Finanční správa) and its tax offices collect income tax and VAT. Social insurance goes to ČSSZ and health insurance to the health insurers.
- **Residence.** Individuals are resident if they have a home in the Czech Republic or stay at least 183 days in the calendar year (ITA § 2(2), (4)). Companies are resident if their seat or place of management is in the Czech Republic (ITA § 17(3)). Residents are taxed on worldwide income, non-residents on Czech-source income only. Detail: [cz-cross-border](cz-cross-border.md).
- **Main laws.** Act No. 586/1992 Coll. on Income Taxes, Act No. 280/2009 Coll., the Tax Code, and Act No. 235/2004 Coll. on VAT.

## Headline figures for 2026

| Item | Rate or amount | Year | Source | Detail |
|---|---|---|---|---|
| Individual income tax | 15% up to 36 times the average wage; 23% above | 2026 | [ITA § 16(1)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) | [cz-employee-income-tax](cz-employee-income-tax.md), [cz-income-tax](cz-income-tax.md) |
| Average wage for tax purposes | CZK 48,967 (CZK 46,278 times 1.0581, rounded up) | 2026 | ITA § 21g(2); Act 589/1992 § 23b(4); [Government Regulation 365/2025 § 1](https://e-sbirka.gov.cz/sb/2025/365) | cz-income-tax |
| 23% threshold (36 times CZK 48,967) | CZK 1,762,812 | 2026 | computed from the row above | cz-employee-income-tax |
| Basic taxpayer credit | CZK 30,840 a year | 2026 | ITA § 35ba(1)(a) | cz-employee-income-tax |
| Corporate income tax | 21% (5% basic investment funds, 0% pension funds) | 2026 | ITA § 21(1) to (3) | [cz-corporate-income-tax](cz-corporate-income-tax.md) |
| Withholding on payments to non-residents | 15%; 35% to states outside the EU and EEA with no treaty, tax information exchange agreement or multilateral information exchange convention in force | 2026 | ITA § 36(1) | cz-cross-border |
| VAT rates | 21% standard; 12% reduced | 2026 | [VAT Act § 47(1)](https://e-sbirka.gov.cz/sb/2004/235/2026-01-01) | [cz-vat-return](cz-vat-return.md) |
| VAT registration (established business) | turnover over CZK 2,000,000 in a calendar year: VAT payer from 1 January of the next year; over CZK 2,536,500: from the day after | 2026 | VAT Act § 6(1), (2)(b) | cz-vat-return |
| Late payment interest on tax | CNB repo rate on the first day of the half-year plus 8 points: 11.50% a year for January to June 2026, 11.75% for July to December 2026 | 2026 | [Tax Code § 251a(5), § 252(4)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01); [Government Regulation 351/2013 § 2(1)](https://e-sbirka.gov.cz/sb/2013/351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) | cz-corporate-income-tax |

Social and health insurance rates for 2026 are in [cz-employee-contributions](cz-employee-contributions.md) (employees and employers) and [cz-social-health](cz-social-health.md) (the self-employed). Payroll withholding is in [cz-payroll](cz-payroll.md), and transfer pricing in [cz-transfer-pricing](cz-transfer-pricing.md).

## Income tax return deadlines for tax year 2026

Individual and corporate income tax returns follow the same rule. The return is due within 3 months after the end of the tax period. It is 4 months if filed electronically after the 3-month date, and 6 months if a tax adviser files after the 3-month date or the accounts must be audited (Tax Code § 136(1), (2)). A deadline on a Saturday, Sunday or public holiday moves to the next working day (Tax Code § 33(4)). The tax is due on the last day for filing (Tax Code § 135(3)).

For the calendar year 2026:

- paper or electronic: **1 April 2027**;
- electronic, after 1 April: **3 May 2027**, because 1 May 2027 is a Saturday and a public holiday;
- tax adviser, or audited accounts: **1 July 2027**.

For the 2025 return the Financial Administration gave 1 April, 4 May and 1 July 2026 ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). The 2027 dates are counted the same way.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force from 1 August 2026: §§ 2, 16, 17, 21, 21a, 21g, 35ba, 36 | https://e-sbirka.gov.cz/sb/1992/586/2026-08-01 | 2026-10-23 |
| Act No. 589/1992 Coll., social security premiums, version in force from 1 July 2026: § 23b(4) (average wage rounded up to whole CZK) | https://e-sbirka.gov.cz/sb/1992/589/2026-07-01 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 33, 135, 136, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-10-23 |
| Act No. 235/2004 Coll., VAT Act, version in force from 1 January 2026: §§ 6, 47 | https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 | 2026-10-23 |
| Government Regulation No. 365/2025 Coll. (general assessment base for 2024 and coefficient) | https://e-sbirka.gov.cz/sb/2025/365 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2(1) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Finanční správa, Daň z příjmů fyzických osob, obecné informace (2025 filing dates) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed: the Financial Administration had not published the filing dates for 2026 returns; 1 April, 3 May and 1 July 2027 are counted from Tax Code §§ 33(4) and 136.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cz-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cz-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
