---
name: sm-tax-overview
description: >
  Overview of the San Marino tax system for 2026 and a router to the detailed San Marino skills. Covers the tax year, currency and authorities, residence and worldwide taxation, the IGR income tax with eight bands from 9% to 35%, the 18% rate for companies and for business and professional income in tax years 2026 to 2030 (17% statutory), the 50% new-company rate cut, the single-stage import tax (monofase) at 17% in place of VAT, ISS social contributions and FONDISS, withholding on payments abroad, the 31 July return deadline, and the 2026 reforms (Law 141/2025, Delegated Decree 156/2026, domestic e-invoicing from 2027). Use for a first answer on San Marino tax, comparing San Marino with Italy, or choosing which San Marino skill to load.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.5
---

# San Marino tax overview v0.5

## Section 1: Scope

A one-page map of San Marino tax for 2026, with the headline figures and which skill to load for the detail. It does no calculation of its own.

## Section 2: Key facts

| Item | 2026 position | Source |
|---|---|---|
| Tax year | Calendar year; returns for 2026 due 31 July 2027 | [IGR art 93(1)][igr] |
| Currency | Euro | |
| Tax authority | UO Ufficio Tributario, Dipartimento Finanze e Bilancio | [Finance department][finance] |
| Social security | ISS (Istituto per la Sicurezza Sociale) and the FONDISS supplementary pension | [ISS circular 2187/UC/2026][iss] |
| Residence | Individuals: registered residence or actual stay for most of the year, or centre of vital interests. Companies: registered office or effective management for most of the year | [IGR arts 10, 42][igr] |
| Scope | Residents on worldwide income; non-residents on San Marino-source income | [IGR arts 1, 5][igr] |
| Personal income tax (IGR) | Eight bands, 9% to 35% (top band over 80,000) | [IGR Annex C][igr] |
| Business and professional income of individuals | 18% separate rate for 2026 to 2030 | [Law 141/2025, art 54(6)][l141] |
| Corporate IGR | 18% for 2026 to 2030 (statutory 17%) | [Law 141/2025, art 54(6)][l141]; [IGR art 43][igr] |
| New-company incentive | 50% rate cut for five tax periods if the article 73 conditions are met (9% in 2026) | [IGR art 73][igr] |
| VAT | None. Single-stage import tax (monofase), ordinary rate 17% | [DD 183/2011, art 1][dd183] |
| Employee social contributions | 7.80% ISS plus 2.50% FONDISS | [ISS circular 2187/UC/2026][iss] |
| Employer pension and FONDISS | 17.60% plus 2.50% (other employer funds on top) | [ISS circular 2187/UC/2026][iss] |
| Withholding on payments abroad | 13% interest, 5% dividends to individuals, 20% professional services, 10% equipment rentals | [IGR arts 102-104][igr] |
| Domestic e-invoicing | Optional from 1 October 2026; required from 1 January 2027 for operators with prior-year revenue of 100,000 or more | [DD 133/2026, arts 2, 11][dd133] |

The 2026 reform: Law 141/2025 applies from tax year 2026 ([Law 141/2025, art 54(1)][l141]); Delegated Decree 156/2026 of 12 October 2026 corrected it, also from 2026 ([DD 156/2026, art 19][dd156]).

## Section 3: Which skill to load

| Question | Skill |
|---|---|
| Individual income tax, wages, pensions, self-employed income, SMaC credit, family credits | `sm-income-tax` |
| Company tax, losses, new-company incentive, advances | `sm-corporate-income-tax` |
| Import tax (monofase), trading with Italy, e-invoicing | `sm-vat-gst` |
| Payroll withholding, ISS and FONDISS contributions, self-employed contributions | `sm-payroll-social` |
| Related-party pricing and advance agreements | `sm-transfer-pricing` |
| Non-residents, withholding on payments abroad, foreign tax credit, permanent establishment | `sm-cross-border` |
| Setting up an SRL or SPA | `sm-company-formation` |

## Section 4: Ask the client first

1. Is the client an individual, sole trader, professional or company?
2. Resident in San Marino in 2026, and where else they have ties?
3. Which income or transactions: wages, business, property, imports, payments abroad?
4. Any link with Italy (frontier work, Italian customers or suppliers)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025 | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |
| Law 141/2025 of 12 November 2025, art 54 | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html | 2026-10-30 |
| Delegated Decree 156/2026 of 12 October 2026 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33 | 2026-10-30 |
| Delegated Decree 183/2011 (import tax 17%) | https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html | 2026-10-30 |
| Delegated Decree 133/2026 (domestic e-invoicing) | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538 | 2026-10-30 |
| ISS circular 2187/UC/2026 of 22 April 2026 | https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html | 2026-10-30 |
| San Marino Finance department, national taxation page | https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html | 2026-10-24 |

Not yet confirmed: nothing in this overview beyond what the linked skills list.

[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[l141]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[dd156]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[dd183]: https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html
[dd133]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538
[iss]: https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html
[finance]: https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html

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
