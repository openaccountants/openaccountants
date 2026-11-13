---
jurisdiction: PY
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: paraguay-iva
  XB: paraguay-cross-border
partial:
  IT-IND: "Employee IPS treatment in the IRP entry-threshold computation is not confirmed."
  IT-CORP: "Computer-equipment depreciation life is not confirmed."
  VAT: "Current IVA withholding percentages are not confirmed."
  PR: "The overtime hourly basis for above-minimum monthly salaries is not confirmed."
  TP: "The interquartile-range computation is not established."
  XB: "PE, business-profits, employment and capital-gains treaty allocation rules are not set out."
---

# Paraguay: tax pack

Paraguay's national tax authority is the Dirección Nacional de Ingresos Tributarios (DNIT, Ley 7143/2023). Amounts in this pack use guaraníes (G). The ordinary IRE and IRP fiscal year coincides with the calendar year under Ley 6380 arts. 7 and 52; monthly IVA, payroll and contributions have their own periods. The seven Guides below cover 2026. A current tax-year label does not establish complete coverage or professional approval of a taxpayer's filing.

## Domains

| Domain | Covering Guide | Tax year | Quality |
|---|---|---|---|
| IT-IND, individual income tax | [Income tax](paraguay-income-tax.md) | 2026 | sourced from the law |
| IT-CORP, business income tax | [Corporate income tax](paraguay-corporate-income-tax.md) | 2026 | sourced from the law |
| VAT / IVA | [IVA](paraguay-iva.md) | 2026 | sourced from the law |
| SC, social contributions | [Social contributions](paraguay-social-contributions.md) | 2026 | checked against the law |
| PR, payroll | [Payroll](paraguay-payroll.md) | 2026 | sourced from the law |
| TP, transfer pricing | [Transfer pricing](paraguay-transfer-pricing.md) | 2026 | sourced from the law |
| XB, cross-border | [Cross-border](paraguay-cross-border.md) | 2026 | checked against the law |

Quality and completeness are separate. These are tier-2 source-based Guides, not accountant approval of a particular case. “Checked against the law” records the completed independent source check within the Guide's stated limits; “sourced from the law” is used conservatively where this follow-up does not establish that complete check. Payroll's corrected v0.3 is independently reviewed in [PR #1411](https://github.com/openaccountants/openaccountants/pull/1411); its open review is not a claim that main already contains it.

## What still needs doing

The `partial` entries name ordinary computation gaps acknowledged in the owning Guides: employee IPS treatment in the IRP entry threshold, computer-equipment depreciation life, current IVA withholding percentages, above-minimum monthly overtime hourly basis, the TP interquartile calculation, and substantive treaty allocation beyond the selected withholding topics. Resolve each in its owner with sources and review before removing its partial note. The cross-border Guide also leaves operational INR/IDU coverage of the pre-2019 treaties unconfirmed; selected treaty caps are not a complete treaty analysis.

Specialist work outside the ordinary workflows includes maquila and investment incentives, free zones and tourism incentives, special VAT/refund schemes, specialist financial/insurance and restructuring rules, occupation-specific/collective wage minima, public/special pension funds and posted-worker agreements, complex TP valuations/disputes and additional treaty-rate tables. SC also bounds parallel bank-worker medical contributions, pay-in-kind valuation and special occupational bases. These specialist exclusions alone do not create a blanket SC partial or close the six ordinary gaps above.

## Official sources

These are the authorities and original-law collections used by the pack, not a claim that this README re-audits every figure. Read dates are 11 November 2026; each owner keeps its detailed article, amendment and regulation record.

| Source | Official URL | Read on |
|---|---|---|
| Ley 7143/2023, DNIT creation and authority | https://www.bacn.gov.py/leyes-paraguayas/12282/ley-n-7143-que-crea-la-direccion- | 2026-11-11 |
| Ley 6380/2019, IRE/IRP fiscal periods and national tax framework, BACN original | https://www.bacn.gov.py/leyes-paraguayas/9332/ley-n-6380-de-modernizacion-y-simplificacion-del-sistema-tributario-nacional | 2026-11-11 |
| Banco Central del Paraguay, official statement of the guaraní monetary unit under its organic law | https://www.bcp.gov.py/es/web/institucional/w/comunicado-sobre-monedas-virtuales-o-criptomonedas | 2026-11-11 |
| DNIT current tax-law collection, regulations linked by the owners | https://www.dnit.gov.py/web/portal-institucional/leyes | 2026-11-11 |
| IPS monthly contribution calendar, read with the social-contribution Guide | https://portal.ips.gov.py/sistemas/ipsportal/contenido.php?c=353 | 2026-11-11 |
| MTESS Res. 670/2026, minimum-wage instrument cited by payroll | https://www.mtess.gov.py/wp-content/uploads/2026/07/Resolucion-MTESS-N%C2%B0-670-REGLAMENTACION-SALARIO-2026.pdf | 2026-11-11 |

Tracked in [Complete the Paraguay pack](https://github.com/openaccountants/openaccountants/issues/312). This map follows the quality/scope distinctions in the pack template; its `partial` metadata is consumed by the coverage report.
