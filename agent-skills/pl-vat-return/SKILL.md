---
name: pl-vat-return
description: "Pointer for Polish VAT returns in tax year 2026. The method is in poland-vat-return, which covers registration (VAT-R), the 23%, 8%, 5% and 0% rates, the PLN 240,000 small-business exemption and the EU SME scheme, the JPK_V7M and JPK_V7K files due on the 25th, KSeF e-invoicing from 1 February and 1 April 2026, split payment above PLN 15,000, the white list, reverse charge, the 30% additional liability and 10.50% late interest. Trigger phrases include Polish VAT return, JPK_V7M, JPK_V7K, deklaracja VAT and plik JPK. Load poland-vat-return for any of these."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pl-vat-return"
  jurisdiction: "PL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Polish VAT return: see poland-vat-return (v3.0)

## Scope

This skill duplicated `poland-vat-return`. The content now lives in one place: [poland-vat-return](poland-vat-return.md), refreshed for tax year 2026 from the VAT Act (Dz.U. 2026 poz. 1263), the Tax Ordinance and the Ministry of Finance. The slug stays so existing links keep working (for example from [pl-cross-border](pl-cross-border.md) and [pl-cit-corporate-tax](pl-cit-corporate-tax.md)). This pointer holds no figures of its own: every figure in the description has its home, source and read date in poland-vat-return.

## The method, step by step

1. Any Polish VAT question (VAT-R, rates, the PLN 240,000 exemption, JPK_V7M or JPK_V7K, split payment, the white list, reverse charge, penalties): load [poland-vat-return](poland-vat-return.md) and answer from it.
2. A KSeF e-invoicing question (who must issue structured invoices in 2026, the carve-outs, offline modes, fines from 2027): load [poland-einvoice](poland-einvoice.md).
3. VAT on cross-border supplies together with permanent establishment or withholding points: also load [pl-cross-border](pl-cross-border.md).
4. A company also asking about corporate tax: also load [pl-cit-corporate-tax](pl-cit-corporate-tax.md).

## When to refuse or refer

- Changes that take effect on 1 January 2027 under Dz.U. 2026 poz. 1270 (reverse charge on exempt supplies, deregistration): poland-vat-return does not cover them; say so and refer to a Polish tax adviser.
- Excise, customs and the retail sales tax: outside the Polish VAT skills.

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act, consolidated text Dz.U. 2026 poz. 1263. Read for the scope that poland-vat-return covers (the PLN 240,000 exemption in art. 113 and the transitional rule for 2025 sales between PLN 200,000 and PLN 240,000) | https://api.sejm.gov.pl/eli/acts/DU/2026/1263/text.pdf | 2026-11-14 |

Not yet confirmed: see the list at the end of [poland-vat-return](poland-vat-return.md).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pl-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pl-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
