---
name: gm-company-formation
description: "company formation for The Gambia (tax year 2026): Single Window steps, 2024 fee order, annual returns. Built from official GRA, SSHFC and Ministry of Justice pages."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gm-company-formation"
  jurisdiction: "GM"
  tax_year: "2026"
  last_updated: "2026-11-01"
---

# Gambia Company Formation and Entity Choice

## Who this applies to

Founders registering in The Gambia through the Single Window Registry. Types on the MoJ page: sole proprietorship, partnership, company (including limited by guarantee), foreign or external company.

## Rates, bands and thresholds

Fees are set by the 2024 Order. The older fee list on the MoJ page is lower and superseded.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Sole proprietorship registration | D1,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Company, share capital up to D500,000 | D15,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Above D500,000 to D1,000,000 | D20,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Above D1,000,000 to D10,000,000 | D25,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Above D10,000,000 | D30,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Company limited by guarantee | D10,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Foreign company | D20,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Name reservation including search | D500 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Company annual returns filing | D1,500 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Extension for late annual returns | D500 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |
| Transfer of share, change of directors | D1,000 | 2026 | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 |

## The base

The fee band follows share capital. A non-resident shareholder or director needs a Gambian agent's particulars. A foreign company needs an agent permanently resident in The Gambia.

## Deadlines and filing

Company steps:
1. Reserve the name.
2. Complete form SWR 7.
3. Attach Memorandum and Articles, company TIN card, and ID of shareholders, directors and secretary.
4. Pay the fee.
5. File annual returns each year.

Foreign company: parent's certified Memorandum and Articles (English translation if needed), ID of parent directors, shareholders and secretary, TIN card, board resolution or power of attorney appointing the agent, form CO38. Sole proprietor: form SWR 3, ID and TIN card. Partnership: name reservation, form SWR7, registered deed, TIN card, partners' ID.

Tax return: see [corporate](gm-corporate-income-tax.md). Staff: see [payroll](gm-payroll-social.md).

## Penalties and interest

Late annual returns take a D500 extension fee. Other penalties are on the Not yet confirmed line.

## Cross-border points

Foreign company registration above. Expatriate staff trigger quota tax.

## Two worked examples that recompute

Share capital D750,000: registration D20,000 plus name D500.

```oa-check
name: Fees
inputs:
  reg: 20000
  name: 500
steps:
  - total: reg + name
expected:
  total: 20500.00
```

Decision: capital of D500,000 or D600,000. The higher band costs D5,000 more.

```oa-check
name: Band step
inputs:
  low: 15000
  high: 20000
steps:
  - gap: high - low
expected:
  gap: 5000.00
```

## Ask the client first

- Entity type?
- Share capital?
- Non-resident shareholders or directors?
- Foreign parent?

## Sources

| Source | URL | Read on |
|---|---|---|
| Single Window Registry Services (Fee Schedule) Order, 2024, Legal Notice 16 of 2024 (whole, scanned), read in full for this skill | https://www.moj.gm/download-file/878f710c-710a-11ef-bbb8-025103a708b7 | 2026-11-01 |
| MoJ Companies Division page (registration steps; its fee list predates the 2024 Order), read for the rows cited | https://www.moj.gm/companies-division | 2026-11-01 |
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |

Not yet confirmed: The Companies Act 2013 text. Minimum number of incorporators (old: two). Minimum capital and the 25% subscription rule (old file, law firm source). Form S.V.3 (old file; the MoJ page names SWR 7). One-day timeline. Municipal trade licence and SSHFC employer registration steps (old file, no official source). Annual return date. Statutory audit thresholds.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-01. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gm-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gm-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
