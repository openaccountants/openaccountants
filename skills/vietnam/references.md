---
name: vietnam-references
jurisdiction: VN
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Vietnam — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## googlesky/thue-2026

- Repository: [googlesky/thue-2026](https://github.com/googlesky/thue-2026)
- License: MIT
- Language: Vietnamese
- Scope: Vietnam 2026 personal income tax (thuế TNCN) computation data. Contains the new 5-bracket progressive rate schedule and updated personal/dependent deduction amounts per Luật số 109/2025/QH15 (effective 01/01/2026).
- Integration: MIT. Tax bracket data and deduction amounts directly used in the vietnam-pit skill.

## thangtd-0050/pit

- Repository: [thangtd-0050/pit](https://github.com/thangtd-0050/pit)
- License: Open source
- Language: Vietnamese / JavaScript
- Scope: Vietnam personal income tax (PIT) calculator implementation. Computes progressive tax from gross salary including social insurance deductions and dependent allowances.
- Integration: Reference implementation for PIT computation logic and validation of bracket calculations.

## Key legislative sources

| Reference | Description |
|---|---|
| Luật số 109/2025/QH15 | 2026 PIT reform — reduces brackets from 7 to 5, increases personal deduction to 15,500,000 VND/month, dependent deduction to 6,200,000 VND/month |
| Luật Thuế TNCN No. 04/2007/QH12 | Original PIT Law (amended 2012, 2014) |
| Thông tư 111/2013/TT-BTC | Implementation circular for PIT |
| Nghị quyết 954/2020/UBTVQH14 | CPI-triggered deduction adjustment mechanism |
| Luật Quản lý Thuế No. 38/2019/QH14 | Tax administration law |
