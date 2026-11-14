---
name: cz-vat-return
description: "Pointer skill for Czech VAT (DPH), tax year 2026. The full method lives in czech-republic-vat-return, covering registration at CZK 2,000,000 calendar-year turnover (payer from 1 January next year) and CZK 2,536,500 (payer from the next day), the 21% and 12% rates, the VAT return (priznani k DPH), control statement (kontrolni hlaseni) and EC sales list (souhrnne hlaseni), monthly and quarterly periods and 25-day deadlines, domestic and cross-border reverse charge, unreliable payers, and penalties including control statement fines under section 101h of the VAT Act (235/2004 Coll.). Trigger phrases include Czech VAT, DPH, platce DPH, kontrolni hlaseni and priznani k DPH. Load czech-republic-vat-return instead of this file. Income tax is in cz-income-tax and cz-corporate-income-tax, non-residents in cz-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cz-vat-return"
  jurisdiction: "CZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Czech Republic: VAT (pointer) v1.0

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet.

## Scope

This file used to be a second copy of the Czech VAT return skill, with 2025 figures. There is now one Czech VAT skill for 2026: **[czech-republic-vat-return](czech-republic-vat-return.md)**. It holds registration, rates, the return, the control statement, the EC sales list, reverse charge, unreliable payers and penalties. This pointer carries no figures of its own (one figure, one home).

The slug stays so that links from [cz-income-tax](cz-income-tax.md), [cz-cross-border](cz-cross-border.md) and [cz-transfer-pricing](cz-transfer-pricing.md) still work.

## The method, step by step

1. Any Czech VAT question (DPH, plátce DPH, přiznání k DPH, kontrolní hlášení, souhrnné hlášení, reverse charge, unreliable payer): load [czech-republic-vat-return](czech-republic-vat-return.md) and answer from it.
2. If the question is only "what are the Czech VAT rates and the registration threshold", the headline table in [cz-tax-overview](cz-tax-overview.md) is enough; still name czech-republic-vat-return as the detail.
3. If the VAT question comes with income tax, also load [cz-income-tax](cz-income-tax.md) (individuals) or [cz-corporate-income-tax](cz-corporate-income-tax.md) (companies).
4. A non-resident supplier, a Czech fixed establishment question or a treaty point: also load [cz-cross-border](cz-cross-border.md).
5. A newly formed company asking when it must register: [cz-company-formation](cz-company-formation.md) for the formation steps, then czech-republic-vat-return for the registration.

## When to refuse or refer

- Partial exemption (pro rata) computations, special schemes (travel, second-hand goods), VAT groups and OSS returns: czech-republic-vat-return says these are not covered; refer to a Czech tax adviser.
- Customs, excise and energy taxes: out of scope of the Czech VAT skills.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 235/2004 Coll., VAT Act, version in force from 1 January 2026. Read for the scope of the VAT return, control statement and EC sales list duties that the full skill covers (§§ 6, 47, 101, 101c to 101i, 102) | https://e-sbirka.gov.cz/sb/2004/235/2026-01-01 | 2026-11-14 |

Not yet confirmed: see the list at the end of [czech-republic-vat-return](czech-republic-vat-return.md).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cz-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cz-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
